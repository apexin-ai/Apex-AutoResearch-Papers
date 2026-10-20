# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032813 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/13e5f08b-3dc1-43e8-aae0-fe1160ce0172.jsonl`
- **Structured JSON:** [`bae050682eb43d1078bd.json`](../../sessions/ba/bae050682eb43d1078bd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T04:04:55.300Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T04:04:55.300Z",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032813 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Original framing holds intact. Headline: \"Variance structure is benchmark-conditional — item dominance on knowledge retrieval, interaction dominance on reasoning — rendering universal reproducibility recipes illusory.\" All three claims survive as stated. Infrastructure crossing is a clean confirmatory null (validates isolated-factor studies). D-study budgets are the actionable deliverable, differentiated by benchmark and metric. IRT vs G-theory comparison lands as standalone contribution (4× item difference explained by multi-facet accounting). AAAI submission on schedule with full confidence.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T04:04:55.303Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T04:04:55.303Z",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

## Round 1

54 recorded events

### User

_source line 3 · 2026-05-21T04:04:55.334Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032813 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Original framing holds intact. Headline: "Variance structure is benchmark-conditional — item dominance on knowledge retrieval, interaction dominance on reasoning — rendering universal reproducibility recipes illusory." All three claims survive as stated. Infrastructure crossing is a clean confirmatory null (validates isolated-factor studies). D-study budgets are the actionable deliverable, differentiated by benchmark and metric. IRT vs G-theory comparison lands as standalone contribution (4× item difference explained by multi-facet accounting). AAAI submission on schedule with full confidence.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "fcb16a4e-0813-4fa9-ba4a-a5eb615d5c29",
  "type": "user",
  "uuid": "f69729b1-ca38-4068-82c9-c6a0e8d7515a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T04:04:55.333Z_

```json
{
  "parentUuid": "f69729b1-ca38-4068-82c9-c6a0e8d7515a",
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
  "uuid": "51b40c83-2d9f-4231-a8c7-d69237a95cf5",
  "timestamp": "2026-05-21T04:04:55.333Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T04:04:55.333Z_

```json
{
  "parentUuid": "51b40c83-2d9f-4231-a8c7-d69237a95cf5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d9efa4e0-6217-423b-8fbe-c612953b5191",
  "timestamp": "2026-05-21T04:04:55.333Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
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
  "aiTitle": "Generate complete simulation paper for NLP variance study",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

### Assistant

_source line 7 · 2026-05-21T04:04:58.176Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9efa4e0-6217-423b-8fbe-c612953b5191",
  "isSidechain": false,
  "requestId": "req_011CbF3yc9C7hZJes4E3WRUs",
  "type": "assistant",
  "uuid": "3bd7340e-edbb-4df1-bed7-2429d0e61aaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XrvRJ5vy9BZtWAkZpKDXNm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11447,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11447
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

_source line 8 · 2026-05-21T04:04:59.051Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VuAyzAGaj2xrCWn2Q68b6u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bd7340e-edbb-4df1-bed7-2429d0e61aaa",
  "isSidechain": false,
  "requestId": "req_011CbF3yc9C7hZJes4E3WRUs",
  "type": "assistant",
  "uuid": "1e0ab072-2cf5-4aa6-a201-3f6e958d3ec1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XrvRJ5vy9BZtWAkZpKDXNm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11447,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11447
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

_source line 9 · 2026-05-21T04:04:59.181Z_

<details open><summary>🔧 Tool call — Read · `toolu_011XsKsd7pUbjCqpMorQwBg4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e0ab072-2cf5-4aa6-a201-3f6e958d3ec1",
  "isSidechain": false,
  "requestId": "req_011CbF3yc9C7hZJes4E3WRUs",
  "type": "assistant",
  "uuid": "778f2cd6-06b5-4935-8d35-0cca202a550f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XrvRJ5vy9BZtWAkZpKDXNm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11447,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11447
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

_source line 10 · 2026-05-21T04:04:59.189Z_

<details><summary>↩ Tool result · `toolu_011XsKsd7pUbjCqpMorQwBg4`</summary>

```text
1	# Paper Framing — nlp_variance_gtheory
2	
3	## Target Venue
4	- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)
5	- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)
6	- Extended: TACL (rolling)
7	
8	## Title
9	Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics
10	
11	## Core Claims (3 条，可证伪)
12	
13	**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation (MVP: 58.4% on MMLU single-model; expected to decrease with model-as-facet reanalysis). Its magnitude is hypothesized to be benchmark-dependent — weakening on reasoning tasks where temperature/seed interactions increase — but this gradient requires exp-002 confirmation. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating whether a systematic benchmark-dependent gradient exists, and (c) deriving D-study implications specific to LLM evaluation.
14	**Fallback narratives**: (A) If gradient confirmed → "benchmark-conditional variance structure"; (B) If gradient not significant → "item dominance is universal but magnitude varies"; (C) If model-as-facet reduces item_id below 30% → pivot to "model×item interaction is the dominant source" — narrative direction changes substantially.
15	
16	**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), "infrastructure" is currently limited to the precision facet.
17	
18	**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.
19	
20	## Contributions (3 条，明确区分)
21	
22	1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.
23	
24	2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.
25	
26	3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).
27	
28	## Story Spine
29	
30	**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.
31	
32	**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.
33	
34	**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.
35	
36	**Headline result template**: "In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (X-Y%, benchmark-dependent [placeholder: fill after exp-001/002]), while direct infrastructure×methodology interactions are negligible. Variance structure [is/is not] benchmark-conditional [pending exp-002]. D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional."
37	
38	## Hook (Counter-Intuitive Quantified Claim)
39	"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory."
40	
41	## Narrative Strategy
42	- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)
43	- **Tension**: "No universal recipe" — the field seeks standardization but variance structure varies qualitatively across task types
44	- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)
45	- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)
46	- **Figure plan** (4 figures minimum):
47	  1. Problem illustration: same model, different benchmark → different dominant variance source
48	  2. G-theory facet diagram showing crossed design
49	  3. Stacked-bar variance decomposition across benchmarks (signature figure)
50	  4. D-study projection curves: G vs item count for different benchmarks
51	- **Key framing shifts from Dream feedback**:
52	  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty
53	  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient
54	  - Cross-benchmark gradient is the **primary novel finding**
55	  - "Fully crossed" language qualified to MMLU exp-001 only; other benchmarks use reduced designs
56	
57	## Venue Fit Risks
58	- AAAI: Strong fit for "evaluation methodology" track. Risk: tight 9-week timeline requires overlapping experiments with writing.
59	- Reviewer concern 1: "Only open-weight models, not API models" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.
60	- Reviewer concern 2: "G-theory is borrowed methodology, not novel" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.
61	- Reviewer concern 3: "Item dominance is obvious from measurement theory" — Acknowledge explicitly. Contribution is quantification (X-Y%, pending exp-001/002), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.
62	
63	## Anticipated Reviewer Concerns & Planned Responses
64	1. **"Only N GPU types"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to "numerical precision" and frame hardware as future work.
65	2. **"float32 engine confound"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.
66	3. **"Only MMLU"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.
67	4. **"Small item sample"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.
68	5. **"No training-time analysis"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.
69	6. **"Missing scale validation"** → exp-005 (14B models)
70	7. **"G-theory may not be right framework"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.
71	8. **"Separability claim is metric-dependent"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.
72	9. **"FP32 degradation is already known (Yuan 2025)"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.
73	10. **"Incremental over Mesting (2026)"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.
74	11. **"Model not treated as G-theory facet"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.
75	12. **"No CIs on variance components"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.
76	13. **"Missing related work — IRT, tinyBenchmarks, Bouthillier"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.
77	14. **"Diagnostic tool claim unsubstantiated"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as "empirical analysis + data release."
78	15. **"Fine-tuning uses encoder-only RoBERTa"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.
79	
80	## Design Decisions
81	- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.
82	- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.
83	- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.
84	- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.
85	- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.
86	- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as "reduced crossing" rather than "fully crossed."
87	- **Gemma2 float16 exclusion**: Gemma2 architecture does not support float16 inference (vLLM numerical instability guard). Cross-model analysis uses bf16+fp32 (balanced). fp16 data from Llama/Mistral/Qwen used in within-model analyses. bf16≈fp16 difference <0.1pp (D005).
88	
89	## Methodological Defenses (Dream #2 审稿问题逐条应对)
90	
91	### MD1. Binary Data in G-theory
92	**Issue**: Standard G-theory assumes continuous, approximately normal response variables. Binary 0/1 data violates this; item variance is mechanically linked to item difficulty via Bernoulli p(1-p).
93	**Defense strategy**: (a) Report correlation between Bernoulli variance p_i(1-p_i) and observed item variance — quantify how much item_id is "mechanical" vs informative; (b) Run parallel analysis on text_exact_match (continuous metric) to show variance structure is robust across metrics; (c) Discuss generalized G-theory (Brennan 2001 Ch.12) in Limitations; (d) Cite Lalor et al. (2019) who used IRT (also assumes latent continuous) on binary NLP data without this criticism being fatal.
94	
95	### MD2. Fixed vs Random Facet Sensitivity
96	**Issue**: Temperature (2-3 design points) and ordering (4 systematic rotations) are not randomly sampled from a universe — treating them as random facets may be inappropriate.
97	**Defense strategy**: Run sensitivity analysis with temperature and ordering as fixed facets. If variance decomposition changes <5%, report as robust. If substantial, discuss implications and present both analyses. This directly addresses Reviewer concern.
98	
99	### MD3. Separability Claim Scope
100	**Issue**: Separability (<0.3%) holds for knowledge benchmarks but not reasoning tasks (GSM8K=3.0%, MATH=2.5%).
101	**Defense**: Qualify all separability claims as "under binary scoring on knowledge-retrieval benchmarks." Present benchmark-conditional separability as a finding (not a limitation): "separability itself varies across task types."
102	
103	### MD4. D-study Optimization Documentation
104	**Issue**: Optimization procedure undocumented; Table 10 arithmetic anomaly (fewer items → higher G).
105	**Defense**: Document grid search procedure (bounds, step sizes, objective function). Verify and explain any non-monotonicity (likely due to joint optimization across facets where reallocating item budget to prompt/seed is more efficient).
106	
107	### MD5. G-coefficient Interpretation
108	**Issue**: G=0.22 for 200 items ≠ "MMLU is unreliable" (standard MMLU uses ~14K items).
109	**Defense**: (a) Clearly distinguish "G for our 200-item subsample design" from "reliability of full MMLU"; (b) Report D-study projection to 14K items; (c) Frame G=0.22 as "cost of subsampling" rather than "MMLU is broken."
110	
111	### MD6. Bootstrap Independence
112	**Issue**: Item-level bootstrap with replacement creates ~127 unique items per 200-item resample, violating independence.
113	**Defense**: (a) Implement delete-1 jackknife as comparison; (b) If bootstrap and jackknife CIs are similar (within 20%), report as robust; (c) Discuss limitation in Methods.
114	
115	### MD7. IRT vs G-theory Comparison
116	**Issue**: tinyBenchmarks recommends ~100 items, D-study recommends 420. 4× discrepancy unexplained.
117	**Defense**: Direct comparison showing G-theory accounts for prompt/seed/ordering dimensions that IRT ignores. The 4× difference is the "cost of multi-facet reliability" — G-theory's budget is larger because it targets reliability across ALL facets, not just items. This comparison is a potential standalone contribution.
118	
119	### MD8. Cross-benchmark Design Asymmetry
120	**Issue**: MMLU uses 3 prec × 3 temp, other benchmarks use 2 × 2.
121	**Defense**: Re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7) and compare variance decomposition. If <5% change, report as robust to design reduction.
122	
123	### MD9. Title-Content Alignment
124	**Issue**: Title promises "Evaluation Metrics" but logprob analysis is minimal.
125	**Defense**: Expand logprob analysis across all benchmarks in exp-004, OR adjust title to "...Across Benchmarks and Models."
126	
127	## Required Bibliography (minimum 25 references)
128	Key references to include beyond current literature_map:
129	- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA
130	- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP
131	- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP
132	- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling
133	- Perlitz et al. (2023) — Efficient LLM benchmarking
134	- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition
135	- Shavelson & Webb (1991) — G-theory primer (canonical)
136	- Brennan (2001) — G-theory textbook (canonical)
137	- Lu et al. (2022) — Option ordering effects in MC evaluation
138	- Pezeshkpour & Hruschka (2024) — Option ordering effects
139	- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)
140	- Sellam et al. (2022) — MultiBERTs, multi-seed training
141	- Dehghani et al. (2021) — Benchmark Lottery
142	- Biderman et al. (2024) — Evaluation reproducibility lessons
143	- Vania et al. (2021) — IRT item properties in NLP
144	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "778f2cd6-06b5-4935-8d35-0cca202a550f",
  "isSidechain": false,
  "promptId": "fcb16a4e-0813-4fa9-ba4a-a5eb615d5c29",
  "type": "user",
  "uuid": "2792a71e-66a0-4950-b386-e1c8b06ec817",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/paper_framing.md",
      "content": "# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation (MVP: 58.4% on MMLU single-model; expected to decrease with model-as-facet reanalysis). Its magnitude is hypothesized to be benchmark-dependent — weakening on reasoning tasks where temperature/seed interactions increase — but this gradient requires exp-002 confirmation. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating whether a systematic benchmark-dependent gradient exists, and (c) deriving D-study implications specific to LLM evaluation.\n**Fallback narratives**: (A) If gradient confirmed → \"benchmark-conditional variance structure\"; (B) If gradient not significant → \"item dominance is universal but magnitude varies\"; (C) If model-as-facet reduces item_id below 30% → pivot to \"model×item interaction is the dominant source\" — narrative direction changes substantially.\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \"infrastructure\" is currently limited to the precision facet.\n\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.\n\n## Contributions (3 条，明确区分)\n\n1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.\n\n2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.\n\n3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\n\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\n\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\n\n**Headline result template**: \"In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (X-Y%, benchmark-dependent [placeholder: fill after exp-001/002]), while direct infrastructure×methodology interactions are negligible. Variance structure [is/is not] benchmark-conditional [pending exp-002]. D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\n- **Tension**: \"No universal recipe\" — the field seeks standardization but variance structure varies qualitatively across task types\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\n- **Figure plan** (4 figures minimum):\n  1. Problem illustration: same model, different benchmark → different dominant variance source\n  2. G-theory facet diagram showing crossed design\n  3. Stacked-bar variance decomposition across benchmarks (signature figure)\n  4. D-study projection curves: G vs item count for different benchmarks\n- **Key framing shifts from Dream feedback**:\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\n  - Cross-benchmark gradient is the **primary novel finding**\n  - \"Fully crossed\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious from measurement theory\" — Acknowledge explicitly. Contribution is quantification (X-Y%, pending exp-001/002), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \"numerical precision\" and frame hardware as future work.\n2. **\"float32 engine confound\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\n8. **\"Separability claim is metric-dependent\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\n9. **\"FP32 degradation is already known (Yuan 2025)\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\n10. **\"Incremental over Mesting (2026)\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\n11. **\"Model not treated as G-theory facet\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\n12. **\"No CIs on variance components\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\n13. **\"Missing related work — IRT, tinyBenchmarks, Bouthillier\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\n14. **\"Diagnostic tool claim unsubstantiated\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \"empirical analysis + data release.\"\n15. **\"Fine-tuning uses encoder-only RoBERTa\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"\n- **Gemma2 float16 exclusion**: Gemma2 architecture does not support float16 inference (vLLM numerical instability guard). Cross-model analysis uses bf16+fp32 (balanced). fp16 data from Llama/Mistral/Qwen used in within-model analyses. bf16≈fp16 difference <0.1pp (D005).\n\n## Methodological Defenses (Dream #2 审稿问题逐条应对)\n\n### MD1. Binary Data in G-theory\n**Issue**: Standard G-theory assumes continuous, approximately normal response variables. Binary 0/1 data violates this; item variance is mechanically linked to item difficulty via Bernoulli p(1-p).\n**Defense strategy**: (a) Report correlation between Bernoulli variance p_i(1-p_i) and observed item variance — quantify how much item_id is \"mechanical\" vs informative; (b) Run parallel analysis on text_exact_match (continuous metric) to show variance structure is robust across metrics; (c) Discuss generalized G-theory (Brennan 2001 Ch.12) in Limitations; (d) Cite Lalor et al. (2019) who used IRT (also assumes latent continuous) on binary NLP data without this criticism being fatal.\n\n### MD2. Fixed vs Random Facet Sensitivity\n**Issue**: Temperature (2-3 design points) and ordering (4 systematic rotations) are not randomly sampled from a universe — treating them as random facets may be inappropriate.\n**Defense strategy**: Run sensitivity analysis with temperature and ordering as fixed facets. If variance decomposition changes <5%, report as robust. If substantial, discuss implications and present both analyses. This directly addresses Reviewer concern.\n\n### MD3. Separability Claim Scope\n**Issue**: Separability (<0.3%) holds for knowledge benchmarks but not reasoning tasks (GSM8K=3.0%, MATH=2.5%).\n**Defense**: Qualify all separability claims as \"under binary scoring on knowledge-retrieval benchmarks.\" Present benchmark-conditional separability as a finding (not a limitation): \"separability itself varies across task types.\"\n\n### MD4. D-study Optimization Documentation\n**Issue**: Optimization procedure undocumented; Table 10 arithmetic anomaly (fewer items → higher G).\n**Defense**: Document grid search procedure (bounds, step sizes, objective function). Verify and explain any non-monotonicity (likely due to joint optimization across facets where reallocating item budget to prompt/seed is more efficient).\n\n### MD5. G-coefficient Interpretation\n**Issue**: G=0.22 for 200 items ≠ \"MMLU is unreliable\" (standard MMLU uses ~14K items).\n**Defense**: (a) Clearly distinguish \"G for our 200-item subsample design\" from \"reliability of full MMLU\"; (b) Report D-study projection to 14K items; (c) Frame G=0.22 as \"cost of subsampling\" rather than \"MMLU is broken.\"\n\n### MD6. Bootstrap Independence\n**Issue**: Item-level bootstrap with replacement creates ~127 unique items per 200-item resample, violating independence.\n**Defense**: (a) Implement delete-1 jackknife as comparison; (b) If bootstrap and jackknife CIs are similar (within 20%), report as robust; (c) Discuss limitation in Methods.\n\n### MD7. IRT vs G-theory Comparison\n**Issue**: tinyBenchmarks recommends ~100 items, D-study recommends 420. 4× discrepancy unexplained.\n**Defense**: Direct comparison showing G-theory accounts for prompt/seed/ordering dimensions that IRT ignores. The 4× difference is the \"cost of multi-facet reliability\" — G-theory's budget is larger because it targets reliability across ALL facets, not just items. This comparison is a potential standalone contribution.\n\n### MD8. Cross-benchmark Design Asymmetry\n**Issue**: MMLU uses 3 prec × 3 temp, other benchmarks use 2 × 2.\n**Defense**: Re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7) and compare variance decomposition. If <5% change, report as robust to design reduction.\n\n### MD9. Title-Content Alignment\n**Issue**: Title promises \"Evaluation Metrics\" but logprob analysis is minimal.\n**Defense**: Expand logprob analysis across all benchmarks in exp-004, OR adjust title to \"...Across Benchmarks and Models.\"\n\n## Required Bibliography (minimum 25 references)\nKey references to include beyond current literature_map:\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\n- Perlitz et al. (2023) — Efficient LLM benchmarking\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\n- Shavelson & Webb (1991) — G-theory primer (canonical)\n- Brennan (2001) — G-theory textbook (canonical)\n- Lu et al. (2022) — Option ordering effects in MC evaluation\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\n- Dehghani et al. (2021) — Benchmark Lottery\n- Biderman et al. (2024) — Evaluation reproducibility lessons\n- Vania et al. (2021) — IRT item properties in NLP\n",
      "numLines": 144,
      "startLine": 1,
      "totalLines": 144
    }
  },
  "sourceToolAssistantUUID": "778f2cd6-06b5-4935-8d35-0cca202a550f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032813 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory…",
  "leafUuid": "2792a71e-66a0-4950-b386-e1c8b06ec817",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper for NLP variance study",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

### Tool result

_source line 13 · 2026-05-21T04:04:59.332Z_

<details><summary>↩ Tool result · reported error · `toolu_01VuAyzAGaj2xrCWn2Q68b6u`</summary>

```text
File content (28906 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e0ab072-2cf5-4aa6-a201-3f6e958d3ec1",
  "isSidechain": false,
  "promptId": "fcb16a4e-0813-4fa9-ba4a-a5eb615d5c29",
  "type": "user",
  "uuid": "154d8bf2-854f-44da-a701-418c6609d717",
  "toolUseResult": "Error: File content (28906 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "1e0ab072-2cf5-4aa6-a201-3f6e958d3ec1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-21T04:05:02.180Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the experiment data in parts since it's too large.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "154d8bf2-854f-44da-a701-418c6609d717",
  "isSidechain": false,
  "requestId": "req_011CbF3yu9e2TPy9g4iqJHN9",
  "type": "assistant",
  "uuid": "15d42b81-6943-4ac2-9f87-d04e6295aff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TatMgpBLu1w45JLZ5bMXbM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4873,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 23288,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 282,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4873,
          "output_tokens": 160,
          "cache_read_input_tokens": 23288,
          "cache_creation_input_tokens": 282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 282
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

_source line 15 · 2026-05-21T04:05:02.753Z_

Now let me read the experiment data in chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15d42b81-6943-4ac2-9f87-d04e6295aff4",
  "isSidechain": false,
  "requestId": "req_011CbF3yu9e2TPy9g4iqJHN9",
  "type": "assistant",
  "uuid": "9a68e1df-ef4e-4bd0-863e-097181f5277c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TatMgpBLu1w45JLZ5bMXbM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4873,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 23288,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 282,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4873,
          "output_tokens": 160,
          "cache_read_input_tokens": 23288,
          "cache_creation_input_tokens": 282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 282
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

_source line 16 · 2026-05-21T04:05:05.047Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P3qEYaae325RtT55hmaikn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/experiment_data.json",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a68e1df-ef4e-4bd0-863e-097181f5277c",
  "isSidechain": false,
  "requestId": "req_011CbF3yu9e2TPy9g4iqJHN9",
  "type": "assistant",
  "uuid": "f7cb6d49-0641-4bad-bf5b-0bdc47cb2311",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TatMgpBLu1w45JLZ5bMXbM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4873,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 23288,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 282,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4873,
          "output_tokens": 160,
          "cache_read_input_tokens": 23288,
          "cache_creation_input_tokens": 282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 282
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

_source line 17 · 2026-05-21T04:05:05.333Z_

<details><summary>↩ Tool result · `toolu_01P3qEYaae325RtT55hmaikn`</summary>

```text
1	[
2	  {
3	    "name": "Full-scale MMLU precision study (4 models)",
4	    "description": "4 models × 3 precisions (Gemma bf16+fp32 only) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items. V0 enforce_eager across all precisions eliminates float32 engine confound. Llama data already collected (239,200 records). Gemma workaround: bf16+fp32 only; cross-model analysis uses balanced bf16+fp32 subset.\n",
5	    "results": {
6	      "total_records": 950400,
7	      "models_complete": 4,
8	      "gemma_workaround": "bf16_fp32_only (fp16 excluded due to vLLM numerical guard)",
9	      "conditions_per_model_3prec": 1296,
10	      "conditions_per_model_2prec": 864,
11	      "accuracy_llama_bf16": 0.711,
12	      "accuracy_llama_fp16": 0.711,
13	      "accuracy_llama_fp32": 0.604,
14	      "accuracy_qwen_bf16": 0.723,
15	      "accuracy_qwen_fp16": 0.722,
16	      "accuracy_qwen_fp32": 0.621,
17	      "accuracy_mistral_bf16": 0.648,
18	      "accuracy_mistral_fp16": 0.649,
19	      "accuracy_mistral_fp32": 0.558,
20	      "accuracy_gemma_bf16": 0.698,
21	      "accuracy_gemma_fp32": 0.601,
22	      "overall_accuracy": 0.668,
23	      "avg_item_id_pct_binary": 57.1,
24	      "avg_residual_pct_binary": 17.5,
25	      "avg_precision_item_pct_binary": 7.0,
26	      "avg_temp_item_pct_binary": 6.8,
27	      "avg_prompt_item_pct_binary": 5.5,
28	      "avg_seed_item_pct_binary": 2.1,
29	      "avg_ordering_item_pct_binary": 1.5,
30	      "avg_precision_main_pct_binary": 1.2,
31	      "avg_temp_main_pct_binary": 0.5,
32	      "avg_prompt_main_pct_binary": 0.3,
33	      "avg_prec_x_temp_pct_binary": 0.2,
34	      "avg_residual_pct_text": 38.0,
35	      "avg_prompt_item_pct_text": 36.2,
36	      "avg_temp_main_pct_text": 16.5,
37	      "avg_temp_item_pct_text": 3.8,
38	      "avg_prec_x_temp_pct_text": 1.1,
39	      "avg_item_id_pct_text": 2.0,
40	      "g_coeff_binary_200item": 0.36,
41	      "g_coeff_text_match_200item": 0.96,
42	      "fp32_degradation_all_models": true,
43	      "fp32_gap_bf16_avg_pp": 8.9,
44	      "fp32_gap_consistent_across_models": true,
45	      "null_predictions_total": 128,
46	      "null_pct": 0.01
47	    },
48	    "tables": [
49	      {
50	        "name": "Table 1: Per-model variance decomposition — binary scoring",
51	        "columns": [
52	          "component",
53	          "llama_pct",
54	          "qwen_pct",
55	          "mistral_pct",
56	          "gemma_pct",
57	          "avg_pct"
58	        ],
59	        "rows": [
60	          {
61	            "component": "item_id",
62	            "llama_pct": 57.2,
63	            "qwen_pct": 55.8,
64	            "mistral_pct": 59.1,
65	            "gemma_pct": 56.4,
66	            "avg_pct": 57.1
67	          },
68	          {
69	            "component": "residual",
70	            "llama_pct": 17.6,
71	            "qwen_pct": 18.2,
72	            "mistral_pct": 16.3,
73	            "gemma_pct": 17.8,
74	            "avg_pct": 17.5
75	          },
76	          {
77	            "component": "precision:item_id",
78	            "llama_pct": 7.1,
79	            "qwen_pct": 7.3,
80	            "mistral_pct": 6.5,
81	            "gemma_pct": 7.2,
82	            "avg_pct": 7.0
83	          },
84	          {
85	            "component": "temperature:item_id",
86	            "llama_pct": 6.9,
87	            "qwen_pct": 6.5,
88	            "mistral_pct": 7.2,
89	            "gemma_pct": 6.6,
90	            "avg_pct": 6.8
91	          },
92	          {
93	            "component": "prompt:item_id",
94	            "llama_pct": 5.4,
95	            "qwen_pct": 5.8,
96	            "mistral_pct": 5.2,
97	            "gemma_pct": 5.6,
98	            "avg_pct": 5.5
99	          },
100	          {
101	            "component": "seed:item_id",
102	            "llama_pct": 2.0,
103	            "qwen_pct": 2.3,
104	            "mistral_pct": 1.9,
105	            "gemma_pct": 2.1,
106	            "avg_pct": 2.1
107	          },
108	          {
109	            "component": "ordering:item_id",
110	            "llama_pct": 1.5,
111	            "qwen_pct": 1.4,
112	            "mistral_pct": 1.6,
113	            "gemma_pct": 1.4,
114	            "avg_pct": 1.5
115	          },
116	          {
117	            "component": "precision",
118	            "llama_pct": 1.1,
119	            "qwen_pct": 1.3,
120	            "mistral_pct": 1.2,
121	            "gemma_pct": 1.1,
122	            "avg_pct": 1.2
123	          },
124	          {
125	            "component": "temperature",
126	            "llama_pct": 0.5,
127	            "qwen_pct": 0.4,
128	            "mistral_pct": 0.5,
129	            "gemma_pct": 0.6,
130	            "avg_pct": 0.5
131	          },
132	          {
133	            "component": "prompt_template",
134	            "llama_pct": 0.3,
135	            "qwen_pct": 0.4,
136	            "mistral_pct": 0.2,
137	            "gemma_pct": 0.3,
138	            "avg_pct": 0.3
139	          },
140	          {
141	            "component": "precision:temperature",
142	            "llama_pct": 0.2,
143	            "qwen_pct": 0.3,
144	            "mistral_pct": 0.1,
145	            "gemma_pct": 0.2,
146	            "avg_pct": 0.2
147	          },
148	          {
149	            "component": "other_interactions",
150	            "llama_pct": 0.2,
151	            "qwen_pct": 0.3,
152	            "mistral_pct": 0.2,
153	            "gemma_pct": 0.7,
154	            "avg_pct": 0.3
155	          }
156	        ]
157	      },
158	      {
159	        "name": "Table 2: Per-model variance decomposition — text_exact_match",
160	        "columns": [
161	          "component",
162	          "llama_pct",
163	          "qwen_pct",
164	          "mistral_pct",
165	          "gemma_pct",
166	          "avg_pct"
167	        ],
168	        "rows": [
169	          {
170	            "component": "residual",
171	            "llama_pct": 38.5,
172	            "qwen_pct": 37.2,
173	            "mistral_pct": 39.1,
174	            "gemma_pct": 37.3,
175	            "avg_pct": 38.0
176	          },
177	          {
178	            "component": "prompt:item_id",
179	            "llama_pct": 35.8,
180	            "qwen_pct": 37.0,
181	            "mistral_pct": 35.5,
182	            "gemma_pct": 36.4,
183	            "avg_pct": 36.2
184	          },
185	          {
186	            "component": "temperature",
187	            "llama_pct": 16.8,
188	            "qwen_pct": 16.0,
189	            "mistral_pct": 16.5,
190	            "gemma_pct": 16.7,
191	            "avg_pct": 16.5
192	          },
193	          {
194	            "component": "temperature:item_id",
195	            "llama_pct": 3.5,
196	            "qwen_pct": 4.2,
197	            "mistral_pct": 3.6,
198	            "gemma_pct": 3.8,
199	            "avg_pct": 3.8
200	          },
201	          {
202	            "component": "precision:temperature",
203	            "llama_pct": 1.2,
204	            "qwen_pct": 1.0,
205	            "mistral_pct": 1.1,
206	            "gemma_pct": 1.0,
207	            "avg_pct": 1.1
208	          },
209	          {
210	            "component": "item_id",
211	            "llama_pct": 1.8,
212	            "qwen_pct": 2.3,
213	            "mistral_pct": 1.9,
214	            "gemma_pct": 2.1,
215	            "avg_pct": 2.0
216	          },
217	          {
218	            "component": "precision:item_id",
219	            "llama_pct": 1.2,
220	            "qwen_pct": 1.1,
221	            "mistral_pct": 1.3,
222	            "gemma_pct": 1.2,
223	            "avg_pct": 1.2
224	          },
225	          {
226	            "component": "other",
227	            "llama_pct": 1.2,
228	            "qwen_pct": 1.2,
229	            "mistral_pct": 1.0,
230	            "gemma_pct": 1.5,
231	            "avg_pct": 1.2
232	          }
233	        ]
234	      },
235	      {
236	        "name": "Table 3: Accuracy by model × precision × temperature",
237	        "columns": [
238	          "model",
239	          "precision",
240	          "T0.0",
241	          "T0.3",
242	          "T0.7"
243	        ],
244	        "rows": [
245	          {
246	            "model": "Llama-3.1-8B",
247	            "precision": "bf16",
248	            "T0.0": 0.729,
249	            "T0.3": 0.709,
250	            "T0.7": 0.695
251	          },
252	          {
253	            "model": "Llama-3.1-8B",
254	            "precision": "fp16",
255	            "T0.0": 0.73,
256	            "T0.3": 0.709,
257	            "T0.7": 0.695
258	          },
259	          {
260	            "model": "Llama-3.1-8B",
261	            "precision": "fp32",
262	            "T0.0": 0.625,
263	            "T0.3": 0.601,
264	            "T0.7": 0.587
265	          },
266	          {
267	            "model": "Qwen3-8B",
268	            "precision": "bf16",
269	            "T0.0": 0.742,
270	            "T0.3": 0.721,
271	            "T0.7": 0.706
272	          },
273	          {
274	            "model": "Qwen3-8B",
275	            "precision": "fp16",
276	            "T0.0": 0.741,
277	            "T0.3": 0.72,
278	            "T0.7": 0.705
279	          },
280	          {
281	            "model": "Qwen3-8B",
282	            "precision": "fp32",
283	            "T0.0": 0.643,
284	            "T0.3": 0.618,
285	            "T0.7": 0.602
286	          },
287	          {
288	            "model": "Mistral-7B",
289	            "precision": "bf16",
290	            "T0.0": 0.668,
291	            "T0.3": 0.645,
292	            "T0.7": 0.631
293	          },
294	          {
295	            "model": "Mistral-7B",
296	            "precision": "fp16",
297	            "T0.0": 0.669,
298	            "T0.3": 0.646,
299	            "T0.7": 0.632
300	          },
301	          {
302	            "model": "Mistral-7B",
303	            "precision": "fp32",
304	            "T0.0": 0.578,
305	            "T0.3": 0.555,
306	            "T0.7": 0.541
307	          },
308	          {
309	            "model": "Gemma-2-9B",
310	            "precision": "bf16",
311	            "T0.0": 0.718,
312	            "T0.3": 0.696,
313	            "T0.7": 0.681
314	          },
315	          {
316	            "model": "Gemma-2-9B",
317	            "precision": "fp32",
318	            "T0.0": 0.622,
319	            "T0.3": 0.598,
320	            "T0.7": 0.583
321	          }
322	        ]
323	      }
324	    ],
325	    "figures": [],
326	    "analysis": "exp-001 在四个模型上复现并巩固了 MVP 的 item dominance 发现。关键观察： (1) item_id 在 55-59% 的窄区间内波动，模型间标准差仅 1.4pp——这不是单一模型的 偶然特性，而是 MMLU item difficulty 分布的固有统计结构；(2) FP32 降幅在所有模型上 均为 8-9pp，确认 V0 enforce_eager 修复后这是一致的引擎级效应，而非 precision 本身； (3) binary 与 text_match 呈现完全不同的方差层级——这为 Claim 3 (metric-conditional budget) 提供了最直接的证据来源；(4) 所有 precision×method 直接交互在 binary 下 ≤0.3%，在 text_match 下 ≤1.2%，为 Claim 2 separability 提供了 MMLU 上的强支撑。 Gemma bf16+fp32 workaround 成功，cross-model balanced analysis 使用 bf16+fp32 子集。\n\n\nitem_id 在 57% 水平保持稳定是因为 200-item stratified sample 保留了 MMLU 跨学科难度分布——item difficulty 变异本身就是 Bernoulli p(1-p) 的直接后果， 在 multiple-choice knowledge retrieval 中 p 值从 0.1 到 0.95 分布极广。四个 模型的 item_id% 在 55-60% 范围内波动（Mistral 略高因其整体准确率较低导致 item difficulty 更分散），这与 single-model MVP 结果(58.4%)一致——模型间差异 不改变 item-level 方差主导地位。FP32 在所有模型上均出现 ~8-9pp 降幅，因为 V0 enforce_eager 模式下 FP32 使用低效的 eager-mode attention 计算路径， 这是 vLLM 引擎层面的系统性效应而非精度本身的问题。bf16≈fp16 差异 <0.2pp 验证了 D005 结论。precision×temperature 交互在 binary scoring 下仅 0.2%， 因为 binary 对 logit 做 argmax 截断后，precision 和 temperature 的联合效应 被离散化消除；而 text_match 下 1.1% 可检测，因浮点非结合性在长文本生成中 逐 token 累积。G=0.36(binary) 反映了 item dominance 下 200 items 不足以 平均化 item-level 噪声，而 G=0.96(text_match) 说明 prompt-item 交互一旦 被 text-level 连续度量吸收后可靠性大幅提升。\n"
327	  },
328	  {
329	    "name": "Item resampling stability test",
330	    "description": "3 independent stratified 200-item MMLU samples (seeds 0/7/99) × Llama-3.1-8B × 3 precisions × 3 prompts × 3 seeds × 2 orderings = 54 conditions per sample. Tests whether headline item_id% finding is artifact of specific item draw.\n",
331	    "results": {
332	      "total_records_per_sample": 10800,
333	      "total_records": 32400,
334	      "sample_0_item_id_pct": 57.5,
335	      "sample_7_item_id_pct": 55.8,
336	      "sample_99_item_id_pct": 58.6,
337	      "item_id_mean_across_samples": 57.3,
338	      "item_id_sd_across_samples": 1.4,
339	      "item_id_range_pp": 2.8,
340	      "residual_range_pp": 1.8,
341	      "precision_item_range_pp": 1.2,
342	      "temp_item_range_pp": 1.5,
343	      "pairwise_item_overlap_pct": 0,
344	      "stratification_match": "14 MMLU subjects represented in all 3 samples",
345	      "g_binary_sample_0": 0.35,
346	      "g_binary_sample_7": 0.37,
347	      "g_binary_sample_99": 0.34,
348	      "g_binary_range": 0.03
349	    },
350	    "tables": [
351	      {
352	        "name": "Table 4: Cross-sample variance decomposition stability",
353	        "columns": [
354	          "component",
355	          "sample_0",
356	          "sample_7",
357	          "sample_99",
358	          "mean",
359	          "sd"
360	        ],
361	        "rows": [
362	          {
363	            "component": "item_id",
364	            "sample_0": 57.5,
365	            "sample_7": 55.8,
366	            "sample_99": 58.6,
367	            "mean": 57.3,
368	            "sd": 1.4
369	          },
370	          {
371	            "component": "residual",
372	            "sample_0": 17.2,
373	            "sample_7": 18.5,
374	            "sample_99": 16.8,
375	            "mean": 17.5,
376	            "sd": 0.9
377	          },
378	          {
379	            "component": "precision:item_id",
380	            "sample_0": 7.1,
381	            "sample_7": 7.5,
382	            "sample_99": 6.5,
383	            "mean": 7.0,
384	            "sd": 0.5
385	          },
386	          {
387	            "component": "temperature:item_id",
388	            "sample_0": 6.5,
389	            "sample_7": 7.2,
390	            "sample_99": 6.8,
391	            "mean": 6.8,
392	            "sd": 0.4
393	          },
394	          {
395	            "component": "prompt:item_id",
396	            "sample_0": 5.8,
397	            "sample_7": 5.0,
398	            "sample_99": 5.6,
399	            "mean": 5.5,
400	            "sd": 0.4
401	          },
402	          {
403	            "component": "seed:item_id",
404	            "sample_0": 2.2,
405	            "sample_7": 1.8,
406	            "sample_99": 2.1,
407	            "mean": 2.0,
408	            "sd": 0.2
409	          },
410	          {
411	            "component": "ordering:item_id",
412	            "sample_0": 1.4,
413	            "sample_7": 1.7,
414	            "sample_99": 1.3,
415	            "mean": 1.5,
416	            "sd": 0.2
417	          },
418	          {
419	            "component": "precision",
420	            "sample_0": 1.2,
421	            "sample_7": 1.1,
422	            "sample_99": 1.3,
423	            "mean": 1.2,
424	            "sd": 0.1
425	          },
426	          {
427	            "component": "other",
428	            "sample_0": 1.1,
429	            "sample_7": 1.4,
430	            "sample_99": 1.0,
431	            "mean": 1.2,
432	            "sd": 0.2
433	          }
434	        ]
435	      }
436	    ],
437	    "figures": [],
438	    "analysis": "Stability test 是对 headline claim 的关键防御。2.8pp range 远小于 \"item_id >40%\" threshold 的裕度（即使最低样本的 55.8% 也远超 40%）。这允许论文自信声称 item dominance 是 MMLU 的结构性属性。该结果也校准了 bootstrap CI 的预期宽度——exp-004 的 1000-resample bootstrap 应产生 ~3-4pp 的 95% CI，与这里观察到的 cross-sample 变异一致。\n\n\n三次独立 stratified sampling 从 MMLU 的 ~14K items 中抽取 200 items，每次样本 完全不同（0 overlap），但由于分层抽样保证了学科分布一致性，item difficulty 的总体 分布在每个样本中都近似复现了 full MMLU 的难度谱。item_id% 在 55.8-58.6% 范围内 波动（SD=1.4pp）是 expected 的抽样方差——200 items 的 bootstrap SE 约为 1.5pp （后续 exp-004 会精确量化）。若方差分解对特定 item 选择敏感（例如某些 \"adversarial\" items 驱动结果），我们会看到 >5pp 的波动；2.8pp 的 range 落在统计噪声范围内， 确认 item dominance 是 MMLU 难度分布的总体特性而非样本偶然。G-coefficient 同样稳定 （range=0.03），进一步验证 D-study 推断的可靠基础。\n"
439	  },
440	  {
441	    "name": "Multi-benchmark replication (GSM8K, ARC, HellaSwag)",
442	    "description": "4 models × 2 precisions (bf16/fp16; Gemma bf16 only) × 6 prompts × 6 seeds × 2 temperatures (T=0.0, T=0.7) × 4 orderings × 200 items per benchmark. Reduced design (2 prec × 2 temp vs exp-001's 3×3) due to GPU budget. Tests cross-benchmark variance gradient — the primary novel finding.\n",
443	    "results": {
444	      "total_records_gsm8k": 403200,
445	      "total_records_arc": 403200,
446	      "total_records_hellaswag": 403200,
447	      "total_records_all": 1209600,
448	      "benchmarks_complete": 3,
449	      "models_with_data_per_benchmark": 4,
450	      "acc_gsm8k_llama": 0.518,
451	      "acc_gsm8k_qwen": 0.612,
452	      "acc_gsm8k_mistral": 0.385,
453	      "acc_gsm8k_gemma": 0.492,
454	      "acc_arc_llama": 0.782,
455	      "acc_arc_qwen": 0.815,
456	      "acc_arc_mistral": 0.738,
457	      "acc_arc_gemma": 0.795,
458	      "acc_hellaswag_llama": 0.762,
459	      "acc_hellaswag_qwen": 0.788,
460	      "acc_hellaswag_mistral": 0.721,
461	      "acc_hellaswag_gemma": 0.755,
462	      "gsm8k_item_id_pct": 22.4,
463	      "gsm8k_temp_item_pct": 18.5,
464	      "gsm8k_residual_pct": 24.8,
465	      "gsm8k_seed_item_pct": 12.3,
466	      "gsm8k_prompt_item_pct": 10.2,
467	      "gsm8k_temp_main_pct": 4.5,
468	      "gsm8k_prec_item_pct": 3.2,
469	      "gsm8k_ordering_item_pct": 2.1,
470	      "gsm8k_prec_main_pct": 0.8,
471	      "gsm8k_prec_x_temp_binary": 0.6,
472	      "gsm8k_other_pct": 0.6,
473	      "arc_item_id_pct": 43.7,
474	      "arc_residual_pct": 20.3,
475	      "arc_temp_item_pct": 9.8,
476	      "arc_prompt_item_pct": 8.5,
477	      "arc_prec_item_pct": 6.2,
478	      "arc_seed_item_pct": 4.5,
479	      "arc_ordering_item_pct": 2.8,
480	      "arc_temp_main_pct": 1.5,
481	      "arc_prec_main_pct": 1.2,
482	      "arc_prec_x_temp_binary": 0.3,
483	      "arc_other_pct": 1.2,
484	      "hellaswag_item_id_pct": 38.2,
485	      "hellaswag_residual_pct": 22.5,
486	      "hellaswag_temp_item_pct": 12.3,
487	      "hellaswag_prompt_item_pct": 9.8,
488	      "hellaswag_seed_item_pct": 6.5,
489	      "hellaswag_prec_item_pct": 4.8,
490	      "hellaswag_ordering_item_pct": 2.4,
491	      "hellaswag_temp_main_pct": 1.5,
492	      "hellaswag_prec_main_pct": 0.8,
493	      "hellaswag_prec_x_temp_binary": 0.4,
494	      "hellaswag_other_pct": 0.8,
495	      "gradient_order": "MMLU(57.1) > ARC(43.7) > HellaSwag(38.2) > GSM8K(22.4)",
496	      "gradient_total_pp": 34.7,
497	      "gradient_monotonic": true,
498	      "gradient_is_clean": true,
499	      "max_prec_x_method_binary_all_benchmarks": 0.6,
500	      "g_binary_gsm8k_200item": 0.48,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7cb6d49-0641-4bad-bf5b-0bdc47cb2311",
  "isSidechain": false,
  "promptId": "fcb16a4e-0813-4fa9-ba4a-a5eb615d5c29",
  "type": "user",
  "uuid": "68c25f70-ae9b-4a20-909d-da61b119ec13",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full-scale MMLU precision study (4 models)\",\n    \"description\": \"4 models × 3 precisions (Gemma bf16+fp32 only) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items. V0 enforce_eager across all precisions eliminates float32 engine confound. Llama data already collected (239,200 records). Gemma workaround: bf16+fp32 only; cross-model analysis uses balanced bf16+fp32 subset.\\n\",\n    \"results\": {\n      \"total_records\": 950400,\n      \"models_complete\": 4,\n      \"gemma_workaround\": \"bf16_fp32_only (fp16 excluded due to vLLM numerical guard)\",\n      \"conditions_per_model_3prec\": 1296,\n      \"conditions_per_model_2prec\": 864,\n      \"accuracy_llama_bf16\": 0.711,\n      \"accuracy_llama_fp16\": 0.711,\n      \"accuracy_llama_fp32\": 0.604,\n      \"accuracy_qwen_bf16\": 0.723,\n      \"accuracy_qwen_fp16\": 0.722,\n      \"accuracy_qwen_fp32\": 0.621,\n      \"accuracy_mistral_bf16\": 0.648,\n      \"accuracy_mistral_fp16\": 0.649,\n      \"accuracy_mistral_fp32\": 0.558,\n      \"accuracy_gemma_bf16\": 0.698,\n      \"accuracy_gemma_fp32\": 0.601,\n      \"overall_accuracy\": 0.668,\n      \"avg_item_id_pct_binary\": 57.1,\n      \"avg_residual_pct_binary\": 17.5,\n      \"avg_precision_item_pct_binary\": 7.0,\n      \"avg_temp_item_pct_binary\": 6.8,\n      \"avg_prompt_item_pct_binary\": 5.5,\n      \"avg_seed_item_pct_binary\": 2.1,\n      \"avg_ordering_item_pct_binary\": 1.5,\n      \"avg_precision_main_pct_binary\": 1.2,\n      \"avg_temp_main_pct_binary\": 0.5,\n      \"avg_prompt_main_pct_binary\": 0.3,\n      \"avg_prec_x_temp_pct_binary\": 0.2,\n      \"avg_residual_pct_text\": 38.0,\n      \"avg_prompt_item_pct_text\": 36.2,\n      \"avg_temp_main_pct_text\": 16.5,\n      \"avg_temp_item_pct_text\": 3.8,\n      \"avg_prec_x_temp_pct_text\": 1.1,\n      \"avg_item_id_pct_text\": 2.0,\n      \"g_coeff_binary_200item\": 0.36,\n      \"g_coeff_text_match_200item\": 0.96,\n      \"fp32_degradation_all_models\": true,\n      \"fp32_gap_bf16_avg_pp\": 8.9,\n      \"fp32_gap_consistent_across_models\": true,\n      \"null_predictions_total\": 128,\n      \"null_pct\": 0.01\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Per-model variance decomposition — binary scoring\",\n        \"columns\": [\n          \"component\",\n          \"llama_pct\",\n          \"qwen_pct\",\n          \"mistral_pct\",\n          \"gemma_pct\",\n          \"avg_pct\"\n        ],\n        \"rows\": [\n          {\n            \"component\": \"item_id\",\n            \"llama_pct\": 57.2,\n            \"qwen_pct\": 55.8,\n            \"mistral_pct\": 59.1,\n            \"gemma_pct\": 56.4,\n            \"avg_pct\": 57.1\n          },\n          {\n            \"component\": \"residual\",\n            \"llama_pct\": 17.6,\n            \"qwen_pct\": 18.2,\n            \"mistral_pct\": 16.3,\n            \"gemma_pct\": 17.8,\n            \"avg_pct\": 17.5\n          },\n          {\n            \"component\": \"precision:item_id\",\n            \"llama_pct\": 7.1,\n            \"qwen_pct\": 7.3,\n            \"mistral_pct\": 6.5,\n            \"gemma_pct\": 7.2,\n            \"avg_pct\": 7.0\n          },\n          {\n            \"component\": \"temperature:item_id\",\n            \"llama_pct\": 6.9,\n            \"qwen_pct\": 6.5,\n            \"mistral_pct\": 7.2,\n            \"gemma_pct\": 6.6,\n            \"avg_pct\": 6.8\n          },\n          {\n            \"component\": \"prompt:item_id\",\n            \"llama_pct\": 5.4,\n            \"qwen_pct\": 5.8,\n            \"mistral_pct\": 5.2,\n            \"gemma_pct\": 5.6,\n            \"avg_pct\": 5.5\n          },\n          {\n            \"component\": \"seed:item_id\",\n            \"llama_pct\": 2.0,\n            \"qwen_pct\": 2.3,\n            \"mistral_pct\": 1.9,\n            \"gemma_pct\": 2.1,\n            \"avg_pct\": 2.1\n          },\n          {\n            \"component\": \"ordering:item_id\",\n            \"llama_pct\": 1.5,\n            \"qwen_pct\": 1.4,\n            \"mistral_pct\": 1.6,\n            \"gemma_pct\": 1.4,\n            \"avg_pct\": 1.5\n          },\n          {\n            \"component\": \"precision\",\n            \"llama_pct\": 1.1,\n            \"qwen_pct\": 1.3,\n            \"mistral_pct\": 1.2,\n            \"gemma_pct\": 1.1,\n            \"avg_pct\": 1.2\n          },\n          {\n            \"component\": \"temperature\",\n            \"llama_pct\": 0.5,\n            \"qwen_pct\": 0.4,\n            \"mistral_pct\": 0.5,\n            \"gemma_pct\": 0.6,\n            \"avg_pct\": 0.5\n          },\n          {\n            \"component\": \"prompt_template\",\n            \"llama_pct\": 0.3,\n            \"qwen_pct\": 0.4,\n            \"mistral_pct\": 0.2,\n            \"gemma_pct\": 0.3,\n            \"avg_pct\": 0.3\n          },\n          {\n            \"component\": \"precision:temperature\",\n            \"llama_pct\": 0.2,\n            \"qwen_pct\": 0.3,\n            \"mistral_pct\": 0.1,\n            \"gemma_pct\": 0.2,\n            \"avg_pct\": 0.2\n          },\n          {\n            \"component\": \"other_interactions\",\n            \"llama_pct\": 0.2,\n            \"qwen_pct\": 0.3,\n            \"mistral_pct\": 0.2,\n            \"gemma_pct\": 0.7,\n            \"avg_pct\": 0.3\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 2: Per-model variance decomposition — text_exact_match\",\n        \"columns\": [\n          \"component\",\n          \"llama_pct\",\n          \"qwen_pct\",\n          \"mistral_pct\",\n          \"gemma_pct\",\n          \"avg_pct\"\n        ],\n        \"rows\": [\n          {\n            \"component\": \"residual\",\n            \"llama_pct\": 38.5,\n            \"qwen_pct\": 37.2,\n            \"mistral_pct\": 39.1,\n            \"gemma_pct\": 37.3,\n            \"avg_pct\": 38.0\n          },\n          {\n            \"component\": \"prompt:item_id\",\n            \"llama_pct\": 35.8,\n            \"qwen_pct\": 37.0,\n            \"mistral_pct\": 35.5,\n            \"gemma_pct\": 36.4,\n            \"avg_pct\": 36.2\n          },\n          {\n            \"component\": \"temperature\",\n            \"llama_pct\": 16.8,\n            \"qwen_pct\": 16.0,\n            \"mistral_pct\": 16.5,\n            \"gemma_pct\": 16.7,\n            \"avg_pct\": 16.5\n          },\n          {\n            \"component\": \"temperature:item_id\",\n            \"llama_pct\": 3.5,\n            \"qwen_pct\": 4.2,\n            \"mistral_pct\": 3.6,\n            \"gemma_pct\": 3.8,\n            \"avg_pct\": 3.8\n          },\n          {\n            \"component\": \"precision:temperature\",\n            \"llama_pct\": 1.2,\n            \"qwen_pct\": 1.0,\n            \"mistral_pct\": 1.1,\n            \"gemma_pct\": 1.0,\n            \"avg_pct\": 1.1\n          },\n          {\n            \"component\": \"item_id\",\n            \"llama_pct\": 1.8,\n            \"qwen_pct\": 2.3,\n            \"mistral_pct\": 1.9,\n            \"gemma_pct\": 2.1,\n            \"avg_pct\": 2.0\n          },\n          {\n            \"component\": \"precision:item_id\",\n            \"llama_pct\": 1.2,\n            \"qwen_pct\": 1.1,\n            \"mistral_pct\": 1.3,\n            \"gemma_pct\": 1.2,\n            \"avg_pct\": 1.2\n          },\n          {\n            \"component\": \"other\",\n            \"llama_pct\": 1.2,\n            \"qwen_pct\": 1.2,\n            \"mistral_pct\": 1.0,\n            \"gemma_pct\": 1.5,\n            \"avg_pct\": 1.2\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 3: Accuracy by model × precision × temperature\",\n        \"columns\": [\n          \"model\",\n          \"precision\",\n          \"T0.0\",\n          \"T0.3\",\n          \"T0.7\"\n        ],\n        \"rows\": [\n          {\n            \"model\": \"Llama-3.1-8B\",\n            \"precision\": \"bf16\",\n            \"T0.0\": 0.729,\n            \"T0.3\": 0.709,\n            \"T0.7\": 0.695\n          },\n          {\n            \"model\": \"Llama-3.1-8B\",\n            \"precision\": \"fp16\",\n            \"T0.0\": 0.73,\n            \"T0.3\": 0.709,\n            \"T0.7\": 0.695\n          },\n          {\n            \"model\": \"Llama-3.1-8B\",\n            \"precision\": \"fp32\",\n            \"T0.0\": 0.625,\n            \"T0.3\": 0.601,\n            \"T0.7\": 0.587\n          },\n          {\n            \"model\": \"Qwen3-8B\",\n            \"precision\": \"bf16\",\n            \"T0.0\": 0.742,\n            \"T0.3\": 0.721,\n            \"T0.7\": 0.706\n          },\n          {\n            \"model\": \"Qwen3-8B\",\n            \"precision\": \"fp16\",\n            \"T0.0\": 0.741,\n            \"T0.3\": 0.72,\n            \"T0.7\": 0.705\n          },\n          {\n            \"model\": \"Qwen3-8B\",\n            \"precision\": \"fp32\",\n            \"T0.0\": 0.643,\n            \"T0.3\": 0.618,\n            \"T0.7\": 0.602\n          },\n          {\n            \"model\": \"Mistral-7B\",\n            \"precision\": \"bf16\",\n            \"T0.0\": 0.668,\n            \"T0.3\": 0.645,\n            \"T0.7\": 0.631\n          },\n          {\n            \"model\": \"Mistral-7B\",\n            \"precision\": \"fp16\",\n            \"T0.0\": 0.669,\n            \"T0.3\": 0.646,\n            \"T0.7\": 0.632\n          },\n          {\n            \"model\": \"Mistral-7B\",\n            \"precision\": \"fp32\",\n            \"T0.0\": 0.578,\n            \"T0.3\": 0.555,\n            \"T0.7\": 0.541\n          },\n          {\n            \"model\": \"Gemma-2-9B\",\n            \"precision\": \"bf16\",\n            \"T0.0\": 0.718,\n            \"T0.3\": 0.696,\n            \"T0.7\": 0.681\n          },\n          {\n            \"model\": \"Gemma-2-9B\",\n            \"precision\": \"fp32\",\n            \"T0.0\": 0.622,\n            \"T0.3\": 0.598,\n            \"T0.7\": 0.583\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-001 在四个模型上复现并巩固了 MVP 的 item dominance 发现。关键观察： (1) item_id 在 55-59% 的窄区间内波动，模型间标准差仅 1.4pp——这不是单一模型的 偶然特性，而是 MMLU item difficulty 分布的固有统计结构；(2) FP32 降幅在所有模型上 均为 8-9pp，确认 V0 enforce_eager 修复后这是一致的引擎级效应，而非 precision 本身； (3) binary 与 text_match 呈现完全不同的方差层级——这为 Claim 3 (metric-conditional budget) 提供了最直接的证据来源；(4) 所有 precision×method 直接交互在 binary 下 ≤0.3%，在 text_match 下 ≤1.2%，为 Claim 2 separability 提供了 MMLU 上的强支撑。 Gemma bf16+fp32 workaround 成功，cross-model balanced analysis 使用 bf16+fp32 子集。\\n\\n\\nitem_id 在 57% 水平保持稳定是因为 200-item stratified sample 保留了 MMLU 跨学科难度分布——item difficulty 变异本身就是 Bernoulli p(1-p) 的直接后果， 在 multiple-choice knowledge retrieval 中 p 值从 0.1 到 0.95 分布极广。四个 模型的 item_id% 在 55-60% 范围内波动（Mistral 略高因其整体准确率较低导致 item difficulty 更分散），这与 single-model MVP 结果(58.4%)一致——模型间差异 不改变 item-level 方差主导地位。FP32 在所有模型上均出现 ~8-9pp 降幅，因为 V0 enforce_eager 模式下 FP32 使用低效的 eager-mode attention 计算路径， 这是 vLLM 引擎层面的系统性效应而非精度本身的问题。bf16≈fp16 差异 <0.2pp 验证了 D005 结论。precision×temperature 交互在 binary scoring 下仅 0.2%， 因为 binary 对 logit 做 argmax 截断后，precision 和 temperature 的联合效应 被离散化消除；而 text_match 下 1.1% 可检测，因浮点非结合性在长文本生成中 逐 token 累积。G=0.36(binary) 反映了 item dominance 下 200 items 不足以 平均化 item-level 噪声，而 G=0.96(text_match) 说明 prompt-item 交互一旦 被 text-level 连续度量吸收后可靠性大幅提升。\\n\"\n  },\n  {\n    \"name\": \"Item resampling stability test\",\n    \"description\": \"3 independent stratified 200-item MMLU samples (seeds 0/7/99) × Llama-3.1-8B × 3 precisions × 3 prompts × 3 seeds × 2 orderings = 54 conditions per sample. Tests whether headline item_id% finding is artifact of specific item draw.\\n\",\n    \"results\": {\n      \"total_records_per_sample\": 10800,\n      \"total_records\": 32400,\n      \"sample_0_item_id_pct\": 57.5,\n      \"sample_7_item_id_pct\": 55.8,\n      \"sample_99_item_id_pct\": 58.6,\n      \"item_id_mean_across_samples\": 57.3,\n      \"item_id_sd_across_samples\": 1.4,\n      \"item_id_range_pp\": 2.8,\n      \"residual_range_pp\": 1.8,\n      \"precision_item_range_pp\": 1.2,\n      \"temp_item_range_pp\": 1.5,\n      \"pairwise_item_overlap_pct\": 0,\n      \"stratification_match\": \"14 MMLU subjects represented in all 3 samples\",\n      \"g_binary_sample_0\": 0.35,\n      \"g_binary_sample_7\": 0.37,\n      \"g_binary_sample_99\": 0.34,\n      \"g_binary_range\": 0.03\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Cross-sample variance decomposition stability\",\n        \"columns\": [\n          \"component\",\n          \"sample_0\",\n          \"sample_7\",\n          \"sample_99\",\n          \"mean\",\n          \"sd\"\n        ],\n        \"rows\": [\n          {\n            \"component\": \"item_id\",\n            \"sample_0\": 57.5,\n            \"sample_7\": 55.8,\n            \"sample_99\": 58.6,\n            \"mean\": 57.3,\n            \"sd\": 1.4\n          },\n          {\n            \"component\": \"residual\",\n            \"sample_0\": 17.2,\n            \"sample_7\": 18.5,\n            \"sample_99\": 16.8,\n            \"mean\": 17.5,\n            \"sd\": 0.9\n          },\n          {\n            \"component\": \"precision:item_id\",\n            \"sample_0\": 7.1,\n            \"sample_7\": 7.5,\n            \"sample_99\": 6.5,\n            \"mean\": 7.0,\n            \"sd\": 0.5\n          },\n          {\n            \"component\": \"temperature:item_id\",\n            \"sample_0\": 6.5,\n            \"sample_7\": 7.2,\n            \"sample_99\": 6.8,\n            \"mean\": 6.8,\n            \"sd\": 0.4\n          },\n          {\n            \"component\": \"prompt:item_id\",\n            \"sample_0\": 5.8,\n            \"sample_7\": 5.0,\n            \"sample_99\": 5.6,\n            \"mean\": 5.5,\n            \"sd\": 0.4\n          },\n          {\n            \"component\": \"seed:item_id\",\n            \"sample_0\": 2.2,\n            \"sample_7\": 1.8,\n            \"sample_99\": 2.1,\n            \"mean\": 2.0,\n            \"sd\": 0.2\n          },\n          {\n            \"component\": \"ordering:item_id\",\n            \"sample_0\": 1.4,\n            \"sample_7\": 1.7,\n            \"sample_99\": 1.3,\n            \"mean\": 1.5,\n            \"sd\": 0.2\n          },\n          {\n            \"component\": \"precision\",\n            \"sample_0\": 1.2,\n            \"sample_7\": 1.1,\n            \"sample_99\": 1.3,\n            \"mean\": 1.2,\n            \"sd\": 0.1\n          },\n          {\n            \"component\": \"other\",\n            \"sample_0\": 1.1,\n            \"sample_7\": 1.4,\n            \"sample_99\": 1.0,\n            \"mean\": 1.2,\n            \"sd\": 0.2\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Stability test 是对 headline claim 的关键防御。2.8pp range 远小于 \\\"item_id >40%\\\" threshold 的裕度（即使最低样本的 55.8% 也远超 40%）。这允许论文自信声称 item dominance 是 MMLU 的结构性属性。该结果也校准了 bootstrap CI 的预期宽度——exp-004 的 1000-resample bootstrap 应产生 ~3-4pp 的 95% CI，与这里观察到的 cross-sample 变异一致。\\n\\n\\n三次独立 stratified sampling 从 MMLU 的 ~14K items 中抽取 200 items，每次样本 完全不同（0 overlap），但由于分层抽样保证了学科分布一致性，item difficulty 的总体 分布在每个样本中都近似复现了 full MMLU 的难度谱。item_id% 在 55.8-58.6% 范围内 波动（SD=1.4pp）是 expected 的抽样方差——200 items 的 bootstrap SE 约为 1.5pp （后续 exp-004 会精确量化）。若方差分解对特定 item 选择敏感（例如某些 \\\"adversarial\\\" items 驱动结果），我们会看到 >5pp 的波动；2.8pp 的 range 落在统计噪声范围内， 确认 item dominance 是 MMLU 难度分布的总体特性而非样本偶然。G-coefficient 同样稳定 （range=0.03），进一步验证 D-study 推断的可靠基础。\\n\"\n  },\n  {\n    \"name\": \"Multi-benchmark replication (GSM8K, ARC, HellaSwag)\",\n    \"description\": \"4 models × 2 precisions (bf16/fp16; Gemma bf16 only) × 6 prompts × 6 seeds × 2 temperatures (T=0.0, T=0.7) × 4 orderings × 200 items per benchmark. Reduced design (2 prec × 2 temp vs exp-001's 3×3) due to GPU budget. Tests cross-benchmark variance gradient — the primary novel finding.\\n\",\n    \"results\": {\n      \"total_records_gsm8k\": 403200,\n      \"total_records_arc\": 403200,\n      \"total_records_hellaswag\": 403200,\n      \"total_records_all\": 1209600,\n      \"benchmarks_complete\": 3,\n      \"models_with_data_per_benchmark\": 4,\n      \"acc_gsm8k_llama\": 0.518,\n      \"acc_gsm8k_qwen\": 0.612,\n      \"acc_gsm8k_mistral\": 0.385,\n      \"acc_gsm8k_gemma\": 0.492,\n      \"acc_arc_llama\": 0.782,\n      \"acc_arc_qwen\": 0.815,\n      \"acc_arc_mistral\": 0.738,\n      \"acc_arc_gemma\": 0.795,\n      \"acc_hellaswag_llama\": 0.762,\n      \"acc_hellaswag_qwen\": 0.788,\n      \"acc_hellaswag_mistral\": 0.721,\n      \"acc_hellaswag_gemma\": 0.755,\n      \"gsm8k_item_id_pct\": 22.4,\n      \"gsm8k_temp_item_pct\": 18.5,\n      \"gsm8k_residual_pct\": 24.8,\n      \"gsm8k_seed_item_pct\": 12.3,\n      \"gsm8k_prompt_item_pct\": 10.2,\n      \"gsm8k_temp_main_pct\": 4.5,\n      \"gsm8k_prec_item_pct\": 3.2,\n      \"gsm8k_ordering_item_pct\": 2.1,\n      \"gsm8k_prec_main_pct\": 0.8,\n      \"gsm8k_prec_x_temp_binary\": 0.6,\n      \"gsm8k_other_pct\": 0.6,\n      \"arc_item_id_pct\": 43.7,\n      \"arc_residual_pct\": 20.3,\n      \"arc_temp_item_pct\": 9.8,\n      \"arc_prompt_item_pct\": 8.5,\n      \"arc_prec_item_pct\": 6.2,\n      \"arc_seed_item_pct\": 4.5,\n      \"arc_ordering_item_pct\": 2.8,\n      \"arc_temp_main_pct\": 1.5,\n      \"arc_prec_main_pct\": 1.2,\n      \"arc_prec_x_temp_binary\": 0.3,\n      \"arc_other_pct\": 1.2,\n      \"hellaswag_item_id_pct\": 38.2,\n      \"hellaswag_residual_pct\": 22.5,\n      \"hellaswag_temp_item_pct\": 12.3,\n      \"hellaswag_prompt_item_pct\": 9.8,\n      \"hellaswag_seed_item_pct\": 6.5,\n      \"hellaswag_prec_item_pct\": 4.8,\n      \"hellaswag_ordering_item_pct\": 2.4,\n      \"hellaswag_temp_main_pct\": 1.5,\n      \"hellaswag_prec_main_pct\": 0.8,\n      \"hellaswag_prec_x_temp_binary\": 0.4,\n      \"hellaswag_other_pct\": 0.8,\n      \"gradient_order\": \"MMLU(57.1) > ARC(43.7) > HellaSwag(38.2) > GSM8K(22.4)\",\n      \"gradient_total_pp\": 34.7,\n      \"gradient_monotonic\": true,\n      \"gradient_is_clean\": true,\n      \"max_prec_x_method_binary_all_benchmarks\": 0.6,\n      \"g_binary_gsm8k_200item\": 0.48,",
      "numLines": 500,
      "startLine": 1,
      "totalLines": 1942
    }
  },
  "sourceToolAssistantUUID": "f7cb6d49-0641-4bad-bf5b-0bdc47cb2311",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032813 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory…",
  "leafUuid": "68c25f70-ae9b-4a20-909d-da61b119ec13",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper for NLP variance study",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

### Tool call

_source line 20 · 2026-05-21T04:05:09.920Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HNQNbcQqWFqc4MoKa8xMQw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/experiment_data.json",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68c25f70-ae9b-4a20-909d-da61b119ec13",
  "isSidechain": false,
  "requestId": "req_011CbF3zLsCx6txhWu8fvRX9",
  "type": "assistant",
  "uuid": "44841ada-cdf3-47a5-8343-38862bde5ce3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwBJu2GayFcNoxFCPcqPVP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13257,
      "cache_read_input_tokens": 23570,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 23570,
          "cache_creation_input_tokens": 13257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13257
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

_source line 21 · 2026-05-21T04:05:10.211Z_

<details><summary>↩ Tool result · `toolu_01HNQNbcQqWFqc4MoKa8xMQw`</summary>

```text
500	      "g_binary_gsm8k_200item": 0.48,
501	      "g_binary_arc_200item": 0.42,
502	      "g_binary_hellaswag_200item": 0.44,
503	      "gsm8k_text_prec_x_temp_pct": 2.5,
504	      "gsm8k_text_prompt_item_pct": 28.3,
505	      "gsm8k_text_residual_pct": 25.1
506	    },
507	    "tables": [
508	      {
509	        "name": "Table 5: Cross-benchmark variance decomposition — binary scoring (single-model averages)",
510	        "columns": [
511	          "component",
512	          "MMLU",
513	          "ARC",
514	          "HellaSwag",
515	          "GSM8K"
516	        ],
517	        "note": "MMLU values from exp-001 included for comparison",
518	        "rows": [
519	          {
520	            "component": "item_id",
521	            "MMLU": 57.1,
522	            "ARC": 43.7,
523	            "HellaSwag": 38.2,
524	            "GSM8K": 22.4
525	          },
526	          {
527	            "component": "residual",
528	            "MMLU": 17.5,
529	            "ARC": 20.3,
530	            "HellaSwag": 22.5,
531	            "GSM8K": 24.8
532	          },
533	          {
534	            "component": "temp:item_id",
535	            "MMLU": 6.8,
536	            "ARC": 9.8,
537	            "HellaSwag": 12.3,
538	            "GSM8K": 18.5
539	          },
540	          {
541	            "component": "prompt:item_id",
542	            "MMLU": 5.5,
543	            "ARC": 8.5,
544	            "HellaSwag": 9.8,
545	            "GSM8K": 10.2
546	          },
547	          {
548	            "component": "seed:item_id",
549	            "MMLU": 2.1,
550	            "ARC": 4.5,
551	            "HellaSwag": 6.5,
552	            "GSM8K": 12.3
553	          },
554	          {
555	            "component": "prec:item_id",
556	            "MMLU": 7.0,
557	            "ARC": 6.2,
558	            "HellaSwag": 4.8,
559	            "GSM8K": 3.2
560	          },
561	          {
562	            "component": "ordering:item_id",
563	            "MMLU": 1.5,
564	            "ARC": 2.8,
565	            "HellaSwag": 2.4,
566	            "GSM8K": 2.1
567	          },
568	          {
569	            "component": "precision",
570	            "MMLU": 1.2,
571	            "ARC": 1.2,
572	            "HellaSwag": 0.8,
573	            "GSM8K": 0.8
574	          },
575	          {
576	            "component": "temperature",
577	            "MMLU": 0.5,
578	            "ARC": 1.5,
579	            "HellaSwag": 1.5,
580	            "GSM8K": 4.5
581	          },
582	          {
583	            "component": "prec:temp",
584	            "MMLU": 0.2,
585	            "ARC": 0.3,
586	            "HellaSwag": 0.4,
587	            "GSM8K": 0.6
588	          },
589	          {
590	            "component": "other",
591	            "MMLU": 0.6,
592	            "ARC": 1.2,
593	            "HellaSwag": 0.8,
594	            "GSM8K": 0.6
595	          }
596	        ]
597	      },
598	      {
599	        "name": "Table 6: Cross-benchmark gradient summary",
600	        "columns": [
601	          "benchmark",
602	          "task_type",
603	          "item_id_pct",
604	          "sum_method_x_item_pct",
605	          "dominant_interaction",
606	          "g_binary_200"
607	        ],
608	        "rows": [
609	          {
610	            "benchmark": "MMLU",
611	            "task_type": "knowledge_retrieval",
612	            "item_id_pct": 57.1,
613	            "sum_method_x_item_pct": 22.9,
614	            "dominant_interaction": "prec:item(7.0)",
615	            "g_binary_200": 0.36
616	          },
617	          {
618	            "benchmark": "ARC",
619	            "task_type": "science_reasoning",
620	            "item_id_pct": 43.7,
621	            "sum_method_x_item_pct": 31.8,
622	            "dominant_interaction": "temp:item(9.8)",
623	            "g_binary_200": 0.42
624	          },
625	          {
626	            "benchmark": "HellaSwag",
627	            "task_type": "commonsense",
628	            "item_id_pct": 38.2,
629	            "sum_method_x_item_pct": 35.8,
630	            "dominant_interaction": "temp:item(12.3)",
631	            "g_binary_200": 0.44
632	          },
633	          {
634	            "benchmark": "GSM8K",
635	            "task_type": "math_reasoning",
636	            "item_id_pct": 22.4,
637	            "sum_method_x_item_pct": 46.3,
638	            "dominant_interaction": "temp:item(18.5)",
639	            "g_binary_200": 0.48
640	          }
641	        ]
642	      },
643	      {
644	        "name": "Table 7: Separability test — direct infra×method interactions across benchmarks",
645	        "columns": [
646	          "benchmark",
647	          "metric",
648	          "prec_x_temp_pct",
649	          "prec_x_prompt_pct",
650	          "prec_x_seed_pct",
651	          "prec_x_ordering_pct",
652	          "max_direct"
653	        ],
654	        "rows": [
655	          {
656	            "benchmark": "MMLU",
657	            "metric": "binary",
658	            "prec_x_temp_pct": 0.2,
659	            "prec_x_prompt_pct": 0.1,
660	            "prec_x_seed_pct": 0.0,
661	            "prec_x_ordering_pct": 0.0,
662	            "max_direct": 0.2
663	          },
664	          {
665	            "benchmark": "ARC",
666	            "metric": "binary",
667	            "prec_x_temp_pct": 0.3,
668	            "prec_x_prompt_pct": 0.1,
669	            "prec_x_seed_pct": 0.0,
670	            "prec_x_ordering_pct": 0.0,
671	            "max_direct": 0.3
672	          },
673	          {
674	            "benchmark": "HellaSwag",
675	            "metric": "binary",
676	            "prec_x_temp_pct": 0.4,
677	            "prec_x_prompt_pct": 0.1,
678	            "prec_x_seed_pct": 0.0,
679	            "prec_x_ordering_pct": 0.1,
680	            "max_direct": 0.4
681	          },
682	          {
683	            "benchmark": "GSM8K",
684	            "metric": "binary",
685	            "prec_x_temp_pct": 0.6,
686	            "prec_x_prompt_pct": 0.2,
687	            "prec_x_seed_pct": 0.1,
688	            "prec_x_ordering_pct": 0.0,
689	            "max_direct": 0.6
690	          },
691	          {
692	            "benchmark": "MMLU",
693	            "metric": "text_match",
694	            "prec_x_temp_pct": 1.1,
695	            "prec_x_prompt_pct": 0.3,
696	            "prec_x_seed_pct": 0.1,
697	            "prec_x_ordering_pct": 0.0,
698	            "max_direct": 1.1
699	          },
700	          {
701	            "benchmark": "GSM8K",
702	            "metric": "text_match",
703	            "prec_x_temp_pct": 2.5,
704	            "prec_x_prompt_pct": 0.8,
705	            "prec_x_seed_pct": 0.3,
706	            "prec_x_ordering_pct": 0.1,
707	            "max_direct": 2.5
708	          }
709	        ]
710	      }
711	    ],
712	    "figures": [],
713	    "analysis": "exp-002 是论文的核心贡献实验。单调 gradient 的存在从根本上解释了文献中的矛盾发现—— Brittlebench 在 MMLU-类任务上发现 prompt 主导方差，而其他研究在 reasoning 任务上 发现 seed/temperature 更重要——两者都是对的，只是在不同 benchmark regime 中观察。 Claim 1 因此被精确化为 \"benchmark-conditional item dominance\"。Claim 2 在所有 benchmark 上成立（max direct infra×method = 0.6% binary），但 text_match 上的 benchmark-conditional separability 破裂（GSM8K text_match 达 2.5%）进一步支撑了 Claim 3 的 metric-conditional 论点。G-coefficient 反直觉地在 GSM8K 上更高（0.48 vs MMLU 0.36）——这是因为 MMLU 的极端 item 方差使得 200-item 采样不足以稳定估计， 而 GSM8K 的 item 方差较低意味着相同 item 数量下估计更稳定（尽管需要更多 prompt/seed replications 来控制 interaction 方差）。\n\n\nCross-benchmark gradient 的物理机制：MMLU 是 knowledge retrieval，答案由模型权重中 存储的事实决定——item difficulty（该事实是否被记忆）解释了大部分方差。ARC 是 science reasoning 但仍有大量事实检索成分，item_id 降至 43.7%。HellaSwag 是 commonsense completion，需要更多 contextual inference，temperature 和 seed 对生成路径的影响更大， item_id 降至 38.2%。GSM8K 是 multi-step arithmetic reasoning，每一步的 token sampling 引入 compounding uncertainty——temperature×item 跃升至 18.5% 因为不同难度的 题目对 sampling 随机性的敏感度差异巨大（简单的一步题几乎不受影响，复杂的五步题在每步都可能 偏离正确路径）。seed×item 12.3% 同理——CUDA 级非确定性在 multi-step generation 中 逐步累积。residual 在 GSM8K 达 24.8% 反映了未建模的高阶交互（prompt×seed×item 等）。 precision×temperature 在 binary 下始终 ≤0.6%——即使在 reasoning 任务上 aggregate-level separability 仍然成立，因为 precision 影响的是 logit 精度而 temperature 影响的是 sampling distribution，两者通过不同机制作用于输出。但在 text_match 下 GSM8K 的 precision×temperature 达 2.5%，因为 reasoning chain 的文本表达对浮点累积误差更敏感。 gradient 的单调性（57>44>38>22）不是拟合结果而是任务认知复杂度的直接映射。\n"
714	  },
715	  {
716	    "name": "Multi-hardware G-study",
717	    "description": "4 models × 2 GPU types (RTX PRO 6000 + A100-80GB) × 2 precisions (bf16/fp16; Gemma bf16 only) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items. Tests the core separability question: does hardware×methodology interaction exist beyond precision effects?\n",
718	    "results": {
719	      "total_records": 1382400,
720	      "gpu_types": [
721	        "RTX_PRO_6000_96GB",
722	        "A100_80GB"
723	      ],
724	      "models_complete": 4,
725	      "gpu_type_accuracy_rtx": 0.669,
726	      "gpu_type_accuracy_a100": 0.667,
727	      "gpu_type_gap_pp": 0.2,
728	      "gpu_type_main_pct_binary": 0.3,
729	      "gpu_x_precision_pct_binary": 0.2,
730	      "gpu_x_temperature_pct_binary": 0.1,
731	      "gpu_x_prompt_pct_binary": 0.1,
732	      "gpu_x_seed_pct_binary": 0.1,
733	      "gpu_x_ordering_pct_binary": 0.0,
734	      "gpu_x_method_total_binary": 0.5,
735	      "gpu_x_item_pct_binary": 1.8,
736	      "gpu_x_prec_x_item_pct_binary": 0.5,
737	      "gpu_x_precision_pct_text": 0.8,
738	      "gpu_x_temperature_pct_text": 0.4,
739	      "gpu_x_method_total_text": 1.5,
740	      "item_id_pct_with_gpu": 55.2,
741	      "residual_pct_with_gpu": 15.8,
742	      "gpu_all_terms_total_pct": 3.5,
743	      "separability_confirmed_binary": true,
744	      "separability_qualified_text": "partial — gpu×prec detectable at 0.8% text_match"
745	    },
746	    "tables": [
747	      {
748	        "name": "Table 8: Variance decomposition with GPU type facet — MMLU binary",
749	        "columns": [
750	          "component",
751	          "pct",
752	          "95% CI"
753	        ],
754	        "rows": [
755	          {
756	            "component": "item_id",
757	            "pct": 55.2,
758	            "95% CI": "[52.8, 57.6]"
759	          },
760	          {
761	            "component": "residual",
762	            "pct": 15.8,
763	            "95% CI": "[13.5, 18.1]"
764	          },
765	          {
766	            "component": "prec:item_id",
767	            "pct": 6.8,
768	            "95% CI": "[5.5, 8.1]"
769	          },
770	          {
771	            "component": "temp:item_id",
772	            "pct": 6.5,
773	            "95% CI": "[5.2, 7.8]"
774	          },
775	          {
776	            "component": "prompt:item_id",
777	            "pct": 5.3,
778	            "95% CI": "[4.1, 6.5]"
779	          },
780	          {
781	            "component": "seed:item_id",
782	            "pct": 2.0,
783	            "95% CI": "[1.3, 2.7]"
784	          },
785	          {
786	            "component": "gpu:item_id",
787	            "pct": 1.8,
788	            "95% CI": "[1.0, 2.6]"
789	          },
790	          {
791	            "component": "ordering:item_id",
792	            "pct": 1.4,
793	            "95% CI": "[0.8, 2.0]"
794	          },
795	          {
796	            "component": "precision",
797	            "pct": 1.1,
798	            "95% CI": "[0.5, 1.7]"
799	          },
800	          {
801	            "component": "temperature",
802	            "pct": 0.5,
803	            "95% CI": "[0.1, 0.9]"
804	          },
805	          {
806	            "component": "gpu_type",
807	            "pct": 0.3,
808	            "95% CI": "[0.0, 0.6]"
809	          },
810	          {
811	            "component": "gpu:precision",
812	            "pct": 0.2,
813	            "95% CI": "[0.0, 0.4]"
814	          },
815	          {
816	            "component": "gpu:temperature",
817	            "pct": 0.1,
818	            "95% CI": "[0.0, 0.3]"
819	          },
820	          {
821	            "component": "gpu:prompt",
822	            "pct": 0.1,
823	            "95% CI": "[0.0, 0.2]"
824	          },
825	          {
826	            "component": "gpu:seed",
827	            "pct": 0.1,
828	            "95% CI": "[0.0, 0.2]"
829	          },
830	          {
831	            "component": "prec:temp",
832	            "pct": 0.2,
833	            "95% CI": "[0.0, 0.4]"
834	          },
835	          {
836	            "component": "gpu:prec:item",
837	            "pct": 0.5,
838	            "95% CI": "[0.2, 0.8]"
839	          },
840	          {
841	            "component": "other",
842	            "pct": 2.1,
843	            "95% CI": "[1.2, 3.0]"
844	          }
845	        ]
846	      },
847	      {
848	        "name": "Table 9: Hardware separability — direct GPU×method interactions",
849	        "columns": [
850	          "interaction",
851	          "binary_pct",
852	          "text_match_pct",
853	          "binary CI contains 0?"
854	        ],
855	        "rows": [
856	          {
857	            "interaction": "gpu×precision",
858	            "binary_pct": 0.2,
859	            "text_match_pct": 0.8,
860	            "binary CI contains 0?": "yes"
861	          },
862	          {
863	            "interaction": "gpu×temperature",
864	            "binary_pct": 0.1,
865	            "text_match_pct": 0.4,
866	            "binary CI contains 0?": "yes"
867	          },
868	          {
869	            "interaction": "gpu×prompt",
870	            "binary_pct": 0.1,
871	            "text_match_pct": 0.2,
872	            "binary CI contains 0?": "yes"
873	          },
874	          {
875	            "interaction": "gpu×seed",
876	            "binary_pct": 0.1,
877	            "text_match_pct": 0.1,
878	            "binary CI contains 0?": "yes"
879	          },
880	          {
881	            "interaction": "gpu×ordering",
882	            "binary_pct": 0.0,
883	            "text_match_pct": 0.0,
884	            "binary CI contains 0?": "yes"
885	          },
886	          {
887	            "interaction": "total_direct",
888	            "binary_pct": 0.5,
889	            "text_match_pct": 1.5,
890	            "binary CI contains 0?": "-"
891	          }
892	        ]
893	      }
894	    ],
895	    "figures": [],
896	    "analysis": "exp-003 将 Claim 2 从 \"precision separability\" 扩展至 \"infrastructure separability\"。 关键发现：(1) GPU type 的所有 direct method 交互在 binary 下均不显著（CI 包含 0）， 这是一个强 confirmatory null，直接支持将 infrastructure 和 methodology 分开研究 的 isolated-factor 方法论；(2) gpu×item 1.8% 说明硬件差异不是 \"不存在\" 而是 \"item-conditional\"——只有 marginal difficulty 的 items 受影响，aggregate 上被冲销； (3) text_match 下 gpu×precision 0.8% 可检测，保持了 metric-conditional separability 的一致叙事。这为论文提供了将 \"infrastructure\" 定义从 \"numerical precision on single GPU\" 扩展到 \"numerical precision across GPU architectures\" 的实证基础。\n\n\nGPU type 在 aggregate 水平上几乎无影响（0.3% 主效应, 0.2pp 准确率差）因为两块 GPU 都使用相同的 vLLM 推理引擎和相同的 CUDA 计算流——差异仅来自微架构级的浮点舍入路径不同 (Ampere vs Ada Lovelace 的 FMA 实现)。gpu×precision 交互 0.2%(binary) 是因为不同 GPU 微架构下 bf16→fp32 的 upcasting 路径略有差异，但 argmax 截断后几乎不可检测。 gpu×item 1.8% 比 direct gpu×method 大一个数量级——这与 precision×item 的模式一致： 硬件差异只在 item level 上可检测（特定困难 items 的 logit margins 恰好在两个 GPU 上 有不同的舍入命运），但在 aggregate 层面被平均化。text_match 下 gpu×precision 0.8% 可检测，与 precision×temperature 在 text_match 下可检测的逻辑一致——浮点非结合性在 逐 token 文本生成中累积，不同硬件的累积路径不同。总体结论：separability 在 binary scoring 下成立，在 text_match 下需要限定——完美支撑 Claim 2 的 metric-qualified conditional separability 叙事。exp-003 将 \"infrastructure\" 从仅 precision 扩展到 precision + GPU type，大幅增强了 Claim 2 的外部效度。\n"
897	  },
898	  {
899	    "name": "Comprehensive analysis (model-as-facet, bootstrap, D-study, IRT comparison)",
900	    "description": "Pure analysis experiment — no GPU compute. Combines all data from exp-001/001b/002/003. 17 sub-analyses covering model-as-facet reanalysis, bootstrap CIs, D-study projections, IRT comparison, sensitivity analyses, and methodological defenses.\n",
901	    "results": {
902	      "item_id_model_as_facet_mmlu": 47.3,
903	      "model_x_item_pct_mmlu": 12.1,
904	      "model_main_pct_mmlu": 3.8,
905	      "model_x_precision_pct": 0.5,
906	      "model_x_temperature_pct": 0.3,
907	      "residual_model_as_facet_mmlu": 12.8,
908	      "item_id_maf_arc": 36.5,
909	      "item_id_maf_hellaswag": 31.4,
910	      "item_id_maf_gsm8k": 18.2,
911	      "model_x_item_maf_arc": 9.5,
912	      "model_x_item_maf_hellaswag": 8.8,
913	      "model_x_item_maf_gsm8k": 6.2,
914	      "cross_benchmark_gradient_maf_pp": 29.1,
915	      "gradient_still_monotonic": true,
916	      "bootstrap_resamples": 1000,
917	      "ci_width_item_id_mmlu_pp": 4.8,
918	      "ci_width_model_x_item_mmlu_pp": 3.5,
919	      "ci_width_prec_x_temp_mmlu_binary_pp": 0.4,
920	      "ci_item_id_mmlu_lower": 44.9,
921	      "ci_item_id_mmlu_upper": 49.7,
922	      "ci_prec_x_temp_binary_contains_zero": true,
923	      "ci_prec_x_temp_text_excludes_zero": true,
924	      "d_study_items_g90_mmlu_binary": 420,
925	      "d_study_allocation_mmlu_binary": "420 items × 3 prompts × 2 seeds × 1 temp × 1 ordering = 2520 evals",
926	      "d_study_items_g90_arc_binary": 320,
927	      "d_study_allocation_arc_binary": "320 items × 3 prompts × 3 seeds × 1 temp × 1 ordering = 2880 evals",
928	      "d_study_items_g90_hellaswag_binary": 290,
929	      "d_study_allocation_hellaswag_binary": "290 items × 3 prompts × 3 seeds × 1 temp × 2 orderings = 5220 evals",
930	      "d_study_items_g90_gsm8k_binary": 220,
931	      "d_study_allocation_gsm8k_binary": "220 items × 4 prompts × 4 seeds × 2 temps × 2 orderings = 14080 evals",
932	      "d_study_items_g90_mmlu_text": 85,
933	      "d_study_allocation_mmlu_text": "85 items × 2 prompts × 1 seed × 1 temp × 1 ordering = 170 evals",
934	      "reml_henderson_max_delta_pp": 1.8,
935	      "reml_henderson_conclusion": "robust — differences <2pp on all components",
936	      "logprob_item_id_mmlu": 52.3,
937	      "logprob_g_coeff_200item": 0.68,
938	      "logprob_prec_x_temp_pct": 0.4,
939	      "model_ranking_flips_across_conditions": 0,
940	      "model_ranking_stable": true,
941	      "ranking_note": "Qwen > Llama > Gemma > Mistral under all precision×temperature combos",
942	      "three_way_interactions_total_pct": 3.2,
943	      "max_single_three_way_pct": 1.1,
944	      "residual_after_three_way_pct": 9.6,
945	      "irt_recommended_items_mmlu": 100,
946	      "gtheory_recommended_items_mmlu": 420,
947	      "irt_gtheory_ratio": 4.2,
948	      "irt_gtheory_explanation": "G-theory 4.2× larger because it accounts for prompt/seed/ordering dimensions IRT ignores",
949	      "power_to_detect_1pct_interaction": 0.92,
950	      "power_to_detect_0_5pct_interaction": 0.71,
951	      "design_is_adequately_powered": true,
952	      "fixed_random_max_delta_pp": 2.8,
953	      "fixed_random_conclusion": "robust — item_id changes <3pp when temp/ordering treated as fixed",
954	      "bernoulli_observed_correlation": 0.82,
955	      "mechanical_variance_fraction": 0.35,
956	      "informative_item_id_after_correction": 30.7,
957	      "parallel_text_match_confirms": true,
958	      "jackknife_ci_width_item_id_pp": 5.2,
959	      "bootstrap_jackknife_ratio": 0.92,
960	      "bootstrap_jackknife_conclusion": "similar — bootstrap CI 8% narrower, within 20% threshold",
961	      "mmlu_3x3_item_id": 57.1,
962	      "mmlu_2x2_matched_item_id": 56.4,
963	      "design_asymmetry_delta_pp": 0.7,
964	      "design_asymmetry_conclusion": "robust — matched 2×2 design changes item_id by <1pp",
965	      "g_binary_14k_items_projection": 0.94,
966	      "g_text_14k_items_projection": 0.998,
967	      "logprob_item_id_arc": 48.1,
968	      "logprob_item_id_hellaswag": 44.5,
969	      "logprob_item_id_gsm8k": 31.2,
970	      "logprob_gradient_monotonic": true,
971	      "cost_per_g90_mmlu_binary_gpu_hours": 8.4,
972	      "cost_per_g90_gsm8k_binary_gpu_hours": 28.2
973	    },
974	    "tables": [
975	      {
976	        "name": "Table 10: Model-as-facet variance decomposition — MMLU binary",
977	        "columns": [
978	          "component",
979	          "single_model_avg_pct",
980	          "model_as_facet_pct",
981	          "delta"
982	        ],
983	        "rows": [
984	          {
985	            "component": "item_id",
986	            "single_model_avg_pct": 57.1,
987	            "model_as_facet_pct": 47.3,
988	            "delta": -9.8
989	          },
990	          {
991	            "component": "model×item",
992	            "single_model_avg_pct": "(in residual)",
993	            "model_as_facet_pct": 12.1,
994	            "delta": "+12.1"
995	          },
996	          {
997	            "component": "model",
998	            "single_model_avg_pct": "(not applicable)",
999	            "model_as_facet_pct": 3.8,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44841ada-cdf3-47a5-8343-38862bde5ce3",
  "isSidechain": false,
  "promptId": "fcb16a4e-0813-4fa9-ba4a-a5eb615d5c29",
  "type": "user",
  "uuid": "a205887e-1049-43e1-b099-5a9c5efaf7fa",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/experiment_data.json",
      "content": "      \"g_binary_gsm8k_200item\": 0.48,\n      \"g_binary_arc_200item\": 0.42,\n      \"g_binary_hellaswag_200item\": 0.44,\n      \"gsm8k_text_prec_x_temp_pct\": 2.5,\n      \"gsm8k_text_prompt_item_pct\": 28.3,\n      \"gsm8k_text_residual_pct\": 25.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Cross-benchmark variance decomposition — binary scoring (single-model averages)\",\n        \"columns\": [\n          \"component\",\n          \"MMLU\",\n          \"ARC\",\n          \"HellaSwag\",\n          \"GSM8K\"\n        ],\n        \"note\": \"MMLU values from exp-001 included for comparison\",\n        \"rows\": [\n          {\n            \"component\": \"item_id\",\n            \"MMLU\": 57.1,\n            \"ARC\": 43.7,\n            \"HellaSwag\": 38.2,\n            \"GSM8K\": 22.4\n          },\n          {\n            \"component\": \"residual\",\n            \"MMLU\": 17.5,\n            \"ARC\": 20.3,\n            \"HellaSwag\": 22.5,\n            \"GSM8K\": 24.8\n          },\n          {\n            \"component\": \"temp:item_id\",\n            \"MMLU\": 6.8,\n            \"ARC\": 9.8,\n            \"HellaSwag\": 12.3,\n            \"GSM8K\": 18.5\n          },\n          {\n            \"component\": \"prompt:item_id\",\n            \"MMLU\": 5.5,\n            \"ARC\": 8.5,\n            \"HellaSwag\": 9.8,\n            \"GSM8K\": 10.2\n          },\n          {\n            \"component\": \"seed:item_id\",\n            \"MMLU\": 2.1,\n            \"ARC\": 4.5,\n            \"HellaSwag\": 6.5,\n            \"GSM8K\": 12.3\n          },\n          {\n            \"component\": \"prec:item_id\",\n            \"MMLU\": 7.0,\n            \"ARC\": 6.2,\n            \"HellaSwag\": 4.8,\n            \"GSM8K\": 3.2\n          },\n          {\n            \"component\": \"ordering:item_id\",\n            \"MMLU\": 1.5,\n            \"ARC\": 2.8,\n            \"HellaSwag\": 2.4,\n            \"GSM8K\": 2.1\n          },\n          {\n            \"component\": \"precision\",\n            \"MMLU\": 1.2,\n            \"ARC\": 1.2,\n            \"HellaSwag\": 0.8,\n            \"GSM8K\": 0.8\n          },\n          {\n            \"component\": \"temperature\",\n            \"MMLU\": 0.5,\n            \"ARC\": 1.5,\n            \"HellaSwag\": 1.5,\n            \"GSM8K\": 4.5\n          },\n          {\n            \"component\": \"prec:temp\",\n            \"MMLU\": 0.2,\n            \"ARC\": 0.3,\n            \"HellaSwag\": 0.4,\n            \"GSM8K\": 0.6\n          },\n          {\n            \"component\": \"other\",\n            \"MMLU\": 0.6,\n            \"ARC\": 1.2,\n            \"HellaSwag\": 0.8,\n            \"GSM8K\": 0.6\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 6: Cross-benchmark gradient summary\",\n        \"columns\": [\n          \"benchmark\",\n          \"task_type\",\n          \"item_id_pct\",\n          \"sum_method_x_item_pct\",\n          \"dominant_interaction\",\n          \"g_binary_200\"\n        ],\n        \"rows\": [\n          {\n            \"benchmark\": \"MMLU\",\n            \"task_type\": \"knowledge_retrieval\",\n            \"item_id_pct\": 57.1,\n            \"sum_method_x_item_pct\": 22.9,\n            \"dominant_interaction\": \"prec:item(7.0)\",\n            \"g_binary_200\": 0.36\n          },\n          {\n            \"benchmark\": \"ARC\",\n            \"task_type\": \"science_reasoning\",\n            \"item_id_pct\": 43.7,\n            \"sum_method_x_item_pct\": 31.8,\n            \"dominant_interaction\": \"temp:item(9.8)\",\n            \"g_binary_200\": 0.42\n          },\n          {\n            \"benchmark\": \"HellaSwag\",\n            \"task_type\": \"commonsense\",\n            \"item_id_pct\": 38.2,\n            \"sum_method_x_item_pct\": 35.8,\n            \"dominant_interaction\": \"temp:item(12.3)\",\n            \"g_binary_200\": 0.44\n          },\n          {\n            \"benchmark\": \"GSM8K\",\n            \"task_type\": \"math_reasoning\",\n            \"item_id_pct\": 22.4,\n            \"sum_method_x_item_pct\": 46.3,\n            \"dominant_interaction\": \"temp:item(18.5)\",\n            \"g_binary_200\": 0.48\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 7: Separability test — direct infra×method interactions across benchmarks\",\n        \"columns\": [\n          \"benchmark\",\n          \"metric\",\n          \"prec_x_temp_pct\",\n          \"prec_x_prompt_pct\",\n          \"prec_x_seed_pct\",\n          \"prec_x_ordering_pct\",\n          \"max_direct\"\n        ],\n        \"rows\": [\n          {\n            \"benchmark\": \"MMLU\",\n            \"metric\": \"binary\",\n            \"prec_x_temp_pct\": 0.2,\n            \"prec_x_prompt_pct\": 0.1,\n            \"prec_x_seed_pct\": 0.0,\n            \"prec_x_ordering_pct\": 0.0,\n            \"max_direct\": 0.2\n          },\n          {\n            \"benchmark\": \"ARC\",\n            \"metric\": \"binary\",\n            \"prec_x_temp_pct\": 0.3,\n            \"prec_x_prompt_pct\": 0.1,\n            \"prec_x_seed_pct\": 0.0,\n            \"prec_x_ordering_pct\": 0.0,\n            \"max_direct\": 0.3\n          },\n          {\n            \"benchmark\": \"HellaSwag\",\n            \"metric\": \"binary\",\n            \"prec_x_temp_pct\": 0.4,\n            \"prec_x_prompt_pct\": 0.1,\n            \"prec_x_seed_pct\": 0.0,\n            \"prec_x_ordering_pct\": 0.1,\n            \"max_direct\": 0.4\n          },\n          {\n            \"benchmark\": \"GSM8K\",\n            \"metric\": \"binary\",\n            \"prec_x_temp_pct\": 0.6,\n            \"prec_x_prompt_pct\": 0.2,\n            \"prec_x_seed_pct\": 0.1,\n            \"prec_x_ordering_pct\": 0.0,\n            \"max_direct\": 0.6\n          },\n          {\n            \"benchmark\": \"MMLU\",\n            \"metric\": \"text_match\",\n            \"prec_x_temp_pct\": 1.1,\n            \"prec_x_prompt_pct\": 0.3,\n            \"prec_x_seed_pct\": 0.1,\n            \"prec_x_ordering_pct\": 0.0,\n            \"max_direct\": 1.1\n          },\n          {\n            \"benchmark\": \"GSM8K\",\n            \"metric\": \"text_match\",\n            \"prec_x_temp_pct\": 2.5,\n            \"prec_x_prompt_pct\": 0.8,\n            \"prec_x_seed_pct\": 0.3,\n            \"prec_x_ordering_pct\": 0.1,\n            \"max_direct\": 2.5\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-002 是论文的核心贡献实验。单调 gradient 的存在从根本上解释了文献中的矛盾发现—— Brittlebench 在 MMLU-类任务上发现 prompt 主导方差，而其他研究在 reasoning 任务上 发现 seed/temperature 更重要——两者都是对的，只是在不同 benchmark regime 中观察。 Claim 1 因此被精确化为 \\\"benchmark-conditional item dominance\\\"。Claim 2 在所有 benchmark 上成立（max direct infra×method = 0.6% binary），但 text_match 上的 benchmark-conditional separability 破裂（GSM8K text_match 达 2.5%）进一步支撑了 Claim 3 的 metric-conditional 论点。G-coefficient 反直觉地在 GSM8K 上更高（0.48 vs MMLU 0.36）——这是因为 MMLU 的极端 item 方差使得 200-item 采样不足以稳定估计， 而 GSM8K 的 item 方差较低意味着相同 item 数量下估计更稳定（尽管需要更多 prompt/seed replications 来控制 interaction 方差）。\\n\\n\\nCross-benchmark gradient 的物理机制：MMLU 是 knowledge retrieval，答案由模型权重中 存储的事实决定——item difficulty（该事实是否被记忆）解释了大部分方差。ARC 是 science reasoning 但仍有大量事实检索成分，item_id 降至 43.7%。HellaSwag 是 commonsense completion，需要更多 contextual inference，temperature 和 seed 对生成路径的影响更大， item_id 降至 38.2%。GSM8K 是 multi-step arithmetic reasoning，每一步的 token sampling 引入 compounding uncertainty——temperature×item 跃升至 18.5% 因为不同难度的 题目对 sampling 随机性的敏感度差异巨大（简单的一步题几乎不受影响，复杂的五步题在每步都可能 偏离正确路径）。seed×item 12.3% 同理——CUDA 级非确定性在 multi-step generation 中 逐步累积。residual 在 GSM8K 达 24.8% 反映了未建模的高阶交互（prompt×seed×item 等）。 precision×temperature 在 binary 下始终 ≤0.6%——即使在 reasoning 任务上 aggregate-level separability 仍然成立，因为 precision 影响的是 logit 精度而 temperature 影响的是 sampling distribution，两者通过不同机制作用于输出。但在 text_match 下 GSM8K 的 precision×temperature 达 2.5%，因为 reasoning chain 的文本表达对浮点累积误差更敏感。 gradient 的单调性（57>44>38>22）不是拟合结果而是任务认知复杂度的直接映射。\\n\"\n  },\n  {\n    \"name\": \"Multi-hardware G-study\",\n    \"description\": \"4 models × 2 GPU types (RTX PRO 6000 + A100-80GB) × 2 precisions (bf16/fp16; Gemma bf16 only) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items. Tests the core separability question: does hardware×methodology interaction exist beyond precision effects?\\n\",\n    \"results\": {\n      \"total_records\": 1382400,\n      \"gpu_types\": [\n        \"RTX_PRO_6000_96GB\",\n        \"A100_80GB\"\n      ],\n      \"models_complete\": 4,\n      \"gpu_type_accuracy_rtx\": 0.669,\n      \"gpu_type_accuracy_a100\": 0.667,\n      \"gpu_type_gap_pp\": 0.2,\n      \"gpu_type_main_pct_binary\": 0.3,\n      \"gpu_x_precision_pct_binary\": 0.2,\n      \"gpu_x_temperature_pct_binary\": 0.1,\n      \"gpu_x_prompt_pct_binary\": 0.1,\n      \"gpu_x_seed_pct_binary\": 0.1,\n      \"gpu_x_ordering_pct_binary\": 0.0,\n      \"gpu_x_method_total_binary\": 0.5,\n      \"gpu_x_item_pct_binary\": 1.8,\n      \"gpu_x_prec_x_item_pct_binary\": 0.5,\n      \"gpu_x_precision_pct_text\": 0.8,\n      \"gpu_x_temperature_pct_text\": 0.4,\n      \"gpu_x_method_total_text\": 1.5,\n      \"item_id_pct_with_gpu\": 55.2,\n      \"residual_pct_with_gpu\": 15.8,\n      \"gpu_all_terms_total_pct\": 3.5,\n      \"separability_confirmed_binary\": true,\n      \"separability_qualified_text\": \"partial — gpu×prec detectable at 0.8% text_match\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Variance decomposition with GPU type facet — MMLU binary\",\n        \"columns\": [\n          \"component\",\n          \"pct\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          {\n            \"component\": \"item_id\",\n            \"pct\": 55.2,\n            \"95% CI\": \"[52.8, 57.6]\"\n          },\n          {\n            \"component\": \"residual\",\n            \"pct\": 15.8,\n            \"95% CI\": \"[13.5, 18.1]\"\n          },\n          {\n            \"component\": \"prec:item_id\",\n            \"pct\": 6.8,\n            \"95% CI\": \"[5.5, 8.1]\"\n          },\n          {\n            \"component\": \"temp:item_id\",\n            \"pct\": 6.5,\n            \"95% CI\": \"[5.2, 7.8]\"\n          },\n          {\n            \"component\": \"prompt:item_id\",\n            \"pct\": 5.3,\n            \"95% CI\": \"[4.1, 6.5]\"\n          },\n          {\n            \"component\": \"seed:item_id\",\n            \"pct\": 2.0,\n            \"95% CI\": \"[1.3, 2.7]\"\n          },\n          {\n            \"component\": \"gpu:item_id\",\n            \"pct\": 1.8,\n            \"95% CI\": \"[1.0, 2.6]\"\n          },\n          {\n            \"component\": \"ordering:item_id\",\n            \"pct\": 1.4,\n            \"95% CI\": \"[0.8, 2.0]\"\n          },\n          {\n            \"component\": \"precision\",\n            \"pct\": 1.1,\n            \"95% CI\": \"[0.5, 1.7]\"\n          },\n          {\n            \"component\": \"temperature\",\n            \"pct\": 0.5,\n            \"95% CI\": \"[0.1, 0.9]\"\n          },\n          {\n            \"component\": \"gpu_type\",\n            \"pct\": 0.3,\n            \"95% CI\": \"[0.0, 0.6]\"\n          },\n          {\n            \"component\": \"gpu:precision\",\n            \"pct\": 0.2,\n            \"95% CI\": \"[0.0, 0.4]\"\n          },\n          {\n            \"component\": \"gpu:temperature\",\n            \"pct\": 0.1,\n            \"95% CI\": \"[0.0, 0.3]\"\n          },\n          {\n            \"component\": \"gpu:prompt\",\n            \"pct\": 0.1,\n            \"95% CI\": \"[0.0, 0.2]\"\n          },\n          {\n            \"component\": \"gpu:seed\",\n            \"pct\": 0.1,\n            \"95% CI\": \"[0.0, 0.2]\"\n          },\n          {\n            \"component\": \"prec:temp\",\n            \"pct\": 0.2,\n            \"95% CI\": \"[0.0, 0.4]\"\n          },\n          {\n            \"component\": \"gpu:prec:item\",\n            \"pct\": 0.5,\n            \"95% CI\": \"[0.2, 0.8]\"\n          },\n          {\n            \"component\": \"other\",\n            \"pct\": 2.1,\n            \"95% CI\": \"[1.2, 3.0]\"\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 9: Hardware separability — direct GPU×method interactions\",\n        \"columns\": [\n          \"interaction\",\n          \"binary_pct\",\n          \"text_match_pct\",\n          \"binary CI contains 0?\"\n        ],\n        \"rows\": [\n          {\n            \"interaction\": \"gpu×precision\",\n            \"binary_pct\": 0.2,\n            \"text_match_pct\": 0.8,\n            \"binary CI contains 0?\": \"yes\"\n          },\n          {\n            \"interaction\": \"gpu×temperature\",\n            \"binary_pct\": 0.1,\n            \"text_match_pct\": 0.4,\n            \"binary CI contains 0?\": \"yes\"\n          },\n          {\n            \"interaction\": \"gpu×prompt\",\n            \"binary_pct\": 0.1,\n            \"text_match_pct\": 0.2,\n            \"binary CI contains 0?\": \"yes\"\n          },\n          {\n            \"interaction\": \"gpu×seed\",\n            \"binary_pct\": 0.1,\n            \"text_match_pct\": 0.1,\n            \"binary CI contains 0?\": \"yes\"\n          },\n          {\n            \"interaction\": \"gpu×ordering\",\n            \"binary_pct\": 0.0,\n            \"text_match_pct\": 0.0,\n            \"binary CI contains 0?\": \"yes\"\n          },\n          {\n            \"interaction\": \"total_direct\",\n            \"binary_pct\": 0.5,\n            \"text_match_pct\": 1.5,\n            \"binary CI contains 0?\": \"-\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-003 将 Claim 2 从 \\\"precision separability\\\" 扩展至 \\\"infrastructure separability\\\"。 关键发现：(1) GPU type 的所有 direct method 交互在 binary 下均不显著（CI 包含 0）， 这是一个强 confirmatory null，直接支持将 infrastructure 和 methodology 分开研究 的 isolated-factor 方法论；(2) gpu×item 1.8% 说明硬件差异不是 \\\"不存在\\\" 而是 \\\"item-conditional\\\"——只有 marginal difficulty 的 items 受影响，aggregate 上被冲销； (3) text_match 下 gpu×precision 0.8% 可检测，保持了 metric-conditional separability 的一致叙事。这为论文提供了将 \\\"infrastructure\\\" 定义从 \\\"numerical precision on single GPU\\\" 扩展到 \\\"numerical precision across GPU architectures\\\" 的实证基础。\\n\\n\\nGPU type 在 aggregate 水平上几乎无影响（0.3% 主效应, 0.2pp 准确率差）因为两块 GPU 都使用相同的 vLLM 推理引擎和相同的 CUDA 计算流——差异仅来自微架构级的浮点舍入路径不同 (Ampere vs Ada Lovelace 的 FMA 实现)。gpu×precision 交互 0.2%(binary) 是因为不同 GPU 微架构下 bf16→fp32 的 upcasting 路径略有差异，但 argmax 截断后几乎不可检测。 gpu×item 1.8% 比 direct gpu×method 大一个数量级——这与 precision×item 的模式一致： 硬件差异只在 item level 上可检测（特定困难 items 的 logit margins 恰好在两个 GPU 上 有不同的舍入命运），但在 aggregate 层面被平均化。text_match 下 gpu×precision 0.8% 可检测，与 precision×temperature 在 text_match 下可检测的逻辑一致——浮点非结合性在 逐 token 文本生成中累积，不同硬件的累积路径不同。总体结论：separability 在 binary scoring 下成立，在 text_match 下需要限定——完美支撑 Claim 2 的 metric-qualified conditional separability 叙事。exp-003 将 \\\"infrastructure\\\" 从仅 precision 扩展到 precision + GPU type，大幅增强了 Claim 2 的外部效度。\\n\"\n  },\n  {\n    \"name\": \"Comprehensive analysis (model-as-facet, bootstrap, D-study, IRT comparison)\",\n    \"description\": \"Pure analysis experiment — no GPU compute. Combines all data from exp-001/001b/002/003. 17 sub-analyses covering model-as-facet reanalysis, bootstrap CIs, D-study projections, IRT comparison, sensitivity analyses, and methodological defenses.\\n\",\n    \"results\": {\n      \"item_id_model_as_facet_mmlu\": 47.3,\n      \"model_x_item_pct_mmlu\": 12.1,\n      \"model_main_pct_mmlu\": 3.8,\n      \"model_x_precision_pct\": 0.5,\n      \"model_x_temperature_pct\": 0.3,\n      \"residual_model_as_facet_mmlu\": 12.8,\n      \"item_id_maf_arc\": 36.5,\n      \"item_id_maf_hellaswag\": 31.4,\n      \"item_id_maf_gsm8k\": 18.2,\n      \"model_x_item_maf_arc\": 9.5,\n      \"model_x_item_maf_hellaswag\": 8.8,\n      \"model_x_item_maf_gsm8k\": 6.2,\n      \"cross_benchmark_gradient_maf_pp\": 29.1,\n      \"gradient_still_monotonic\": true,\n      \"bootstrap_resamples\": 1000,\n      \"ci_width_item_id_mmlu_pp\": 4.8,\n      \"ci_width_model_x_item_mmlu_pp\": 3.5,\n      \"ci_width_prec_x_temp_mmlu_binary_pp\": 0.4,\n      \"ci_item_id_mmlu_lower\": 44.9,\n      \"ci_item_id_mmlu_upper\": 49.7,\n      \"ci_prec_x_temp_binary_contains_zero\": true,\n      \"ci_prec_x_temp_text_excludes_zero\": true,\n      \"d_study_items_g90_mmlu_binary\": 420,\n      \"d_study_allocation_mmlu_binary\": \"420 items × 3 prompts × 2 seeds × 1 temp × 1 ordering = 2520 evals\",\n      \"d_study_items_g90_arc_binary\": 320,\n      \"d_study_allocation_arc_binary\": \"320 items × 3 prompts × 3 seeds × 1 temp × 1 ordering = 2880 evals\",\n      \"d_study_items_g90_hellaswag_binary\": 290,\n      \"d_study_allocation_hellaswag_binary\": \"290 items × 3 prompts × 3 seeds × 1 temp × 2 orderings = 5220 evals\",\n      \"d_study_items_g90_gsm8k_binary\": 220,\n      \"d_study_allocation_gsm8k_binary\": \"220 items × 4 prompts × 4 seeds × 2 temps × 2 orderings = 14080 evals\",\n      \"d_study_items_g90_mmlu_text\": 85,\n      \"d_study_allocation_mmlu_text\": \"85 items × 2 prompts × 1 seed × 1 temp × 1 ordering = 170 evals\",\n      \"reml_henderson_max_delta_pp\": 1.8,\n      \"reml_henderson_conclusion\": \"robust — differences <2pp on all components\",\n      \"logprob_item_id_mmlu\": 52.3,\n      \"logprob_g_coeff_200item\": 0.68,\n      \"logprob_prec_x_temp_pct\": 0.4,\n      \"model_ranking_flips_across_conditions\": 0,\n      \"model_ranking_stable\": true,\n      \"ranking_note\": \"Qwen > Llama > Gemma > Mistral under all precision×temperature combos\",\n      \"three_way_interactions_total_pct\": 3.2,\n      \"max_single_three_way_pct\": 1.1,\n      \"residual_after_three_way_pct\": 9.6,\n      \"irt_recommended_items_mmlu\": 100,\n      \"gtheory_recommended_items_mmlu\": 420,\n      \"irt_gtheory_ratio\": 4.2,\n      \"irt_gtheory_explanation\": \"G-theory 4.2× larger because it accounts for prompt/seed/ordering dimensions IRT ignores\",\n      \"power_to_detect_1pct_interaction\": 0.92,\n      \"power_to_detect_0_5pct_interaction\": 0.71,\n      \"design_is_adequately_powered\": true,\n      \"fixed_random_max_delta_pp\": 2.8,\n      \"fixed_random_conclusion\": \"robust — item_id changes <3pp when temp/ordering treated as fixed\",\n      \"bernoulli_observed_correlation\": 0.82,\n      \"mechanical_variance_fraction\": 0.35,\n      \"informative_item_id_after_correction\": 30.7,\n      \"parallel_text_match_confirms\": true,\n      \"jackknife_ci_width_item_id_pp\": 5.2,\n      \"bootstrap_jackknife_ratio\": 0.92,\n      \"bootstrap_jackknife_conclusion\": \"similar — bootstrap CI 8% narrower, within 20% threshold\",\n      \"mmlu_3x3_item_id\": 57.1,\n      \"mmlu_2x2_matched_item_id\": 56.4,\n      \"design_asymmetry_delta_pp\": 0.7,\n      \"design_asymmetry_conclusion\": \"robust — matched 2×2 design changes item_id by <1pp\",\n      \"g_binary_14k_items_projection\": 0.94,\n      \"g_text_14k_items_projection\": 0.998,\n      \"logprob_item_id_arc\": 48.1,\n      \"logprob_item_id_hellaswag\": 44.5,\n      \"logprob_item_id_gsm8k\": 31.2,\n      \"logprob_gradient_monotonic\": true,\n      \"cost_per_g90_mmlu_binary_gpu_hours\": 8.4,\n      \"cost_per_g90_gsm8k_binary_gpu_hours\": 28.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Model-as-facet variance decomposition — MMLU binary\",\n        \"columns\": [\n          \"component\",\n          \"single_model_avg_pct\",\n          \"model_as_facet_pct\",\n          \"delta\"\n        ],\n        \"rows\": [\n          {\n            \"component\": \"item_id\",\n            \"single_model_avg_pct\": 57.1,\n            \"model_as_facet_pct\": 47.3,\n            \"delta\": -9.8\n          },\n          {\n            \"component\": \"model×item\",\n            \"single_model_avg_pct\": \"(in residual)\",\n            \"model_as_facet_pct\": 12.1,\n            \"delta\": \"+12.1\"\n          },\n          {\n            \"component\": \"model\",\n            \"single_model_avg_pct\": \"(not applicable)\",\n            \"model_as_facet_pct\": 3.8,",
      "numLines": 500,
      "startLine": 500,
      "totalLines": 1942
    }
  },
  "sourceToolAssistantUUID": "44841ada-cdf3-47a5-8343-38862bde5ce3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032813 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory…",
  "leafUuid": "a205887e-1049-43e1-b099-5a9c5efaf7fa",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper for NLP variance study",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

### Tool call

_source line 24 · 2026-05-21T04:05:14.763Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KpAMMxDSRqSGDXVqpmBz4V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/experiment_data.json",
  "offset": 1000,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a205887e-1049-43e1-b099-5a9c5efaf7fa",
  "isSidechain": false,
  "requestId": "req_011CbF3zhgqyFzW3WAtJfeLy",
  "type": "assistant",
  "uuid": "2adcc024-7068-4550-aca9-9cee344c30de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCdhc1LhhgfQ1r4hUA97PL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8724,
      "cache_read_input_tokens": 36827,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8724,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 36827,
          "cache_creation_input_tokens": 8724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8724
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

_source line 25 · 2026-05-21T04:05:15.051Z_

<details><summary>↩ Tool result · `toolu_01KpAMMxDSRqSGDXVqpmBz4V`</summary>

```text
1000	            "delta": "+3.8"
1001	          },
1002	          {
1003	            "component": "residual",
1004	            "single_model_avg_pct": 17.5,
1005	            "model_as_facet_pct": 12.8,
1006	            "delta": -4.7
1007	          },
1008	          {
1009	            "component": "prec:item",
1010	            "single_model_avg_pct": 7.0,
1011	            "model_as_facet_pct": 6.5,
1012	            "delta": -0.5
1013	          },
1014	          {
1015	            "component": "temp:item",
1016	            "single_model_avg_pct": 6.8,
1017	            "model_as_facet_pct": 6.2,
1018	            "delta": -0.6
1019	          },
1020	          {
1021	            "component": "prompt:item",
1022	            "single_model_avg_pct": 5.5,
1023	            "model_as_facet_pct": 5.0,
1024	            "delta": -0.5
1025	          },
1026	          {
1027	            "component": "model×prec",
1028	            "single_model_avg_pct": "(in precision)",
1029	            "model_as_facet_pct": 0.5,
1030	            "delta": "+0.5"
1031	          },
1032	          {
1033	            "component": "model×temp",
1034	            "single_model_avg_pct": "(in temperature)",
1035	            "model_as_facet_pct": 0.3,
1036	            "delta": "+0.3"
1037	          },
1038	          {
1039	            "component": "other",
1040	            "single_model_avg_pct": 6.1,
1041	            "model_as_facet_pct": 5.5,
1042	            "delta": -0.6
1043	          }
1044	        ]
1045	      },
1046	      {
1047	        "name": "Table 11: Model-as-facet cross-benchmark gradient",
1048	        "columns": [
1049	          "benchmark",
1050	          "item_id_maf_pct",
1051	          "model_x_item_pct",
1052	          "gradient_from_mmlu_pp"
1053	        ],
1054	        "rows": [
1055	          {
1056	            "benchmark": "MMLU",
1057	            "item_id_maf_pct": 47.3,
1058	            "model_x_item_pct": 12.1,
1059	            "gradient_from_mmlu_pp": 0.0
1060	          },
1061	          {
1062	            "benchmark": "ARC",
1063	            "item_id_maf_pct": 36.5,
1064	            "model_x_item_pct": 9.5,
1065	            "gradient_from_mmlu_pp": -10.8
1066	          },
1067	          {
1068	            "benchmark": "HellaSwag",
1069	            "item_id_maf_pct": 31.4,
1070	            "model_x_item_pct": 8.8,
1071	            "gradient_from_mmlu_pp": -15.9
1072	          },
1073	          {
1074	            "benchmark": "GSM8K",
1075	            "item_id_maf_pct": 18.2,
1076	            "model_x_item_pct": 6.2,
1077	            "gradient_from_mmlu_pp": -29.1
1078	          }
1079	        ]
1080	      },
1081	      {
1082	        "name": "Table 12: D-study optimal allocations for G≥0.90 (binary scoring)",
1083	        "columns": [
1084	          "benchmark",
1085	          "items",
1086	          "prompts",
1087	          "seeds",
1088	          "temps",
1089	          "orderings",
1090	          "total_evals",
1091	          "cost_gpu_hours"
1092	        ],
1093	        "rows": [
1094	          {
1095	            "benchmark": "MMLU",
1096	            "items": 420,
1097	            "prompts": 3,
1098	            "seeds": 2,
1099	            "temps": 1,
1100	            "orderings": 1,
1101	            "total_evals": 2520,
1102	            "cost_gpu_hours": 8.4
1103	          },
1104	          {
1105	            "benchmark": "ARC",
1106	            "items": 320,
1107	            "prompts": 3,
1108	            "seeds": 3,
1109	            "temps": 1,
1110	            "orderings": 1,
1111	            "total_evals": 2880,
1112	            "cost_gpu_hours": 9.6
1113	          },
1114	          {
1115	            "benchmark": "HellaSwag",
1116	            "items": 290,
1117	            "prompts": 3,
1118	            "seeds": 3,
1119	            "temps": 1,
1120	            "orderings": 2,
1121	            "total_evals": 5220,
1122	            "cost_gpu_hours": 17.4
1123	          },
1124	          {
1125	            "benchmark": "GSM8K",
1126	            "items": 220,
1127	            "prompts": 4,
1128	            "seeds": 4,
1129	            "temps": 2,
1130	            "orderings": 2,
1131	            "total_evals": 14080,
1132	            "cost_gpu_hours": 28.2
1133	          }
1134	        ]
1135	      },
1136	      {
1137	        "name": "Table 13: D-study optimal allocations for G≥0.90 (text_exact_match)",
1138	        "columns": [
1139	          "benchmark",
1140	          "items",
1141	          "prompts",
1142	          "seeds",
1143	          "temps",
1144	          "orderings",
1145	          "total_evals"
1146	        ],
1147	        "rows": [
1148	          {
1149	            "benchmark": "MMLU",
1150	            "items": 85,
1151	            "prompts": 2,
1152	            "seeds": 1,
1153	            "temps": 1,
1154	            "orderings": 1,
1155	            "total_evals": 170
1156	          },
1157	          {
1158	            "benchmark": "ARC",
1159	            "items": 110,
1160	            "prompts": 2,
1161	            "seeds": 1,
1162	            "temps": 1,
1163	            "orderings": 1,
1164	            "total_evals": 220
1165	          },
1166	          {
1167	            "benchmark": "HellaSwag",
1168	            "items": 95,
1169	            "prompts": 2,
1170	            "seeds": 2,
1171	            "temps": 1,
1172	            "orderings": 1,
1173	            "total_evals": 380
1174	          },
1175	          {
1176	            "benchmark": "GSM8K",
1177	            "items": 150,
1178	            "prompts": 3,
1179	            "seeds": 2,
1180	            "temps": 1,
1181	            "orderings": 1,
1182	            "total_evals": 900
1183	          }
1184	        ]
1185	      },
1186	      {
1187	        "name": "Table 14: IRT (tinyBenchmarks) vs G-theory item recommendations",
1188	        "columns": [
1189	          "benchmark",
1190	          "irt_items",
1191	          "gtheory_items_binary",
1192	          "ratio",
1193	          "gtheory_items_text",
1194	          "irt_text_ratio"
1195	        ],
1196	        "rows": [
1197	          {
1198	            "benchmark": "MMLU",
1199	            "irt_items": 100,
1200	            "gtheory_items_binary": 420,
1201	            "ratio": 4.2,
1202	            "gtheory_items_text": 85,
1203	            "irt_text_ratio": 0.85
1204	          },
1205	          {
1206	            "benchmark": "ARC",
1207	            "irt_items": 75,
1208	            "gtheory_items_binary": 320,
1209	            "ratio": 4.3,
1210	            "gtheory_items_text": 110,
1211	            "irt_text_ratio": 1.47
1212	          },
1213	          {
1214	            "benchmark": "GSM8K",
1215	            "irt_items": 80,
1216	            "gtheory_items_binary": 220,
1217	            "ratio": 2.8,
1218	            "gtheory_items_text": 150,
1219	            "irt_text_ratio": 1.88
1220	          }
1221	        ]
1222	      },
1223	      {
1224	        "name": "Table 15: Bootstrap CIs on key variance components (MMLU, model-as-facet)",
1225	        "columns": [
1226	          "component",
1227	          "point_est",
1228	          "ci_lower",
1229	          "ci_upper",
1230	          "ci_width",
1231	          "overlaps next largest?"
1232	        ],
1233	        "rows": [
1234	          {
1235	            "component": "item_id",
1236	            "point_est": 47.3,
1237	            "ci_lower": 44.9,
1238	            "ci_upper": 49.7,
1239	            "ci_width": 4.8,
1240	            "overlaps next largest?": "no — gap to model×item"
1241	          },
1242	          {
1243	            "component": "model×item",
1244	            "point_est": 12.1,
1245	            "ci_lower": 10.4,
1246	            "ci_upper": 13.9,
1247	            "ci_width": 3.5,
1248	            "overlaps next largest?": "no — gap to residual"
1249	          },
1250	          {
1251	            "component": "residual",
1252	            "point_est": 12.8,
1253	            "ci_lower": 10.8,
1254	            "ci_upper": 14.8,
1255	            "ci_width": 4.0,
1256	            "overlaps next largest?": "yes — overlaps model×item"
1257	          },
1258	          {
1259	            "component": "prec:item",
1260	            "point_est": 6.5,
1261	            "ci_lower": 5.2,
1262	            "ci_upper": 7.8,
1263	            "ci_width": 2.6,
1264	            "overlaps next largest?": "yes — overlaps temp:item"
1265	          },
1266	          {
1267	            "component": "temp:item",
1268	            "point_est": 6.2,
1269	            "ci_lower": 4.9,
1270	            "ci_upper": 7.5,
1271	            "ci_width": 2.6,
1272	            "overlaps next largest?": "yes — overlaps prec:item"
1273	          },
1274	          {
1275	            "component": "prompt:item",
1276	            "point_est": 5.0,
1277	            "ci_lower": 3.8,
1278	            "ci_upper": 6.2,
1279	            "ci_width": 2.4,
1280	            "overlaps next largest?": "partial with temp:item"
1281	          },
1282	          {
1283	            "component": "model",
1284	            "point_est": 3.8,
1285	            "ci_lower": 1.5,
1286	            "ci_upper": 6.1,
1287	            "ci_width": 4.6,
1288	            "overlaps next largest?": "wide CI — 4 models"
1289	          },
1290	          {
1291	            "component": "prec:temp (binary)",
1292	            "point_est": 0.2,
1293	            "ci_lower": 0.0,
1294	            "ci_upper": 0.6,
1295	            "ci_width": 0.6,
1296	            "overlaps next largest?": "CI contains 0"
1297	          }
1298	        ]
1299	      },
1300	      {
1301	        "name": "Table 16: Sensitivity analyses summary",
1302	        "columns": [
1303	          "analysis",
1304	          "comparison",
1305	          "max_delta_pp",
1306	          "robust (&lt;threshold)?"
1307	        ],
1308	        "rows": [
1309	          {
1310	            "analysis": "REML vs Henderson",
1311	            "comparison": "all components",
1312	            "max_delta_pp": 1.8,
1313	            "robust (&lt;threshold)?": "yes (<5pp)"
1314	          },
1315	          {
1316	            "analysis": "Fixed vs random (temp/ordering)",
1317	            "comparison": "item_id",
1318	            "max_delta_pp": 2.8,
1319	            "robust (&lt;threshold)?": "yes (<5pp)"
1320	          },
1321	          {
1322	            "analysis": "3×3 vs matched 2×2 design",
1323	            "comparison": "item_id",
1324	            "max_delta_pp": 0.7,
1325	            "robust (&lt;threshold)?": "yes (<5pp)"
1326	          },
1327	          {
1328	            "analysis": "Bootstrap vs jackknife CI",
1329	            "comparison": "CI_width_ratio",
1330	            "max_delta_pp": 0.08,
1331	            "robust (&lt;threshold)?": "yes (<20%)"
1332	          },
1333	          {
1334	            "analysis": "Bernoulli correction",
1335	            "comparison": "informative item_id",
1336	            "max_delta_pp": 16.6,
1337	            "robust (&lt;threshold)?": "corrected value 30.7% still largest"
1338	          }
1339	        ]
1340	      },
1341	      {
1342	        "name": "Table 17: Logprob scoring — cross-benchmark variance (item_id%)",
1343	        "columns": [
1344	          "benchmark",
1345	          "binary",
1346	          "text_match",
1347	          "logprob"
1348	        ],
1349	        "rows": [
1350	          {
1351	            "benchmark": "MMLU",
1352	            "binary": 47.3,
1353	            "text_match": 2.0,
1354	            "logprob": 52.3
1355	          },
1356	          {
1357	            "benchmark": "ARC",
1358	            "binary": 36.5,
1359	            "text_match": 1.8,
1360	            "logprob": 48.1
1361	          },
1362	          {
1363	            "benchmark": "HellaSwag",
1364	            "binary": 31.4,
1365	            "text_match": 1.5,
1366	            "logprob": 44.5
1367	          },
1368	          {
1369	            "benchmark": "GSM8K",
1370	            "binary": 18.2,
1371	            "text_match": 8.0,
1372	            "logprob": 31.2
1373	          }
1374	        ]
1375	      }
1376	    ],
1377	    "figures": [],
1378	    "analysis": "exp-004 是论文的分析引擎。关键结论： (1) Model-as-facet 将 item_id 降至 47.3%，但它仍是最大单一方差来源且远超 40% threshold。 model×item 12.1% 的出现解释了为什么 single-model studies 高估 item dominance——不同 模型的 item difficulty profiles 不同（Qwen 在 STEM 上更强，Mistral 在 humanities 上 更强），single-model 将这种差异性混入 item_id。 (2) Bootstrap CI 将所有 point estimates 升级为区间估计，使论文的每一个方差数字都有 统计可信度。item_id 下界 44.9% > 40% threshold 确保 Claim 1 在统计意义上成立。 (3) D-study 分化是最 actionable 的 deliverable：MMLU 需要 420 items（IRT 的 4.2×） 但仅 2520 evals，而 GSM8K 仅 220 items 但 14080 evals——因为 reasoning 任务的 interaction 方差只能通过增加 prompt/seed replications 来控制，而非增加 items。这直接 回答了 \"how many items do I need\" 的实践者问题，且答案是 \"depends on your benchmark and your metric\"。 (4) 所有 sensitivity analyses 在 robustness threshold 内，使论文对方法论批评有预防性防御。 IRT vs G-theory 比较有潜力成为 standalone contribution 甚至独立论文。\n\n\n(a) Model-as-facet reanalysis将 item_id 从 57.1% 降至 47.3%：差值中 ~12.1% 重新归因为 model×item 交互（不同模型在不同 items 上有不同优势/劣势），~3.8% 归为 model 主效应 （模型间整体能力差异）。这是 G-theory 正确处理 nested vs crossed 设计的教科书结果—— single-model 分析将 model×item 方差混入 item_id 和 residual 中。关键是 item_id 即使 降至 47.3% 仍远超 40% threshold，且 cross-benchmark gradient 保持单调（29.1pp）， Claim 1 完全成立。 (b) Bootstrap CI width 4.8pp 足够窄以排斥 item_id 与 model×item 的重叠—— item_id 下界 44.9% vs model×item 上界 ~15.6%，无交集。precision×temperature 在 binary 下 CI 包含 0（不显著），在 text_match 下排除 0（显著）——精确支撑 metric-conditional separability。 (c) D-study projections 分化明显：MMLU 需要 420 items 但仅 2520 evals（item-dominated， 多 items 少 replications）；GSM8K 仅需 220 items 但 14080 evals（interaction-dominated， 少 items 多 replications）。这个 5.6× 的 eval budget 差异直接否定了 \"universal reproducibility recipe\" 的可能性——核心 deliverable。 (d-n) 所有 sensitivity analyses 均在 robustness threshold 内：REML vs Henderson <2pp, fixed vs random <3pp, design asymmetry <1pp, bootstrap vs jackknife <20%。这不是偶然—— 当 item_id 在 40-57% 量级主导时，方法论选择对结论的影响是二阶小量。 (h) IRT 4.2× ratio 是因为 tinyBenchmarks IRT 仅优化 item selection（假设单一 evaluation condition），而 G-theory D-study 在 items × prompts × seeds × temps × orderings 的 联合空间中优化——额外维度需要更多 items 来维持跨维度的可靠性。这个比较本身是 standalone contribution 级别的发现。 (l) Bernoulli 机械方差占 item_id 的 35%（correlation 0.82），但校正后 informative item_id 仍有 30.7%——远高于其他任何单一 component。parallel text_match 分析确认方差结构 在非 binary 度量下保持，驳斥 \"item dominance 仅是 binary scoring artifact\" 的批评。 (o) 14K items 下 G=0.94(binary) 说明 full MMLU 本身在 binary 下是 adequate 的， problem 在于 subsampling practices——这精确定位了 \"reproducibility gap\" 的来源。\n"
1379	  },
1380	  {
1381	    "name": "14B model scale extension",
1382	    "description": "Qwen3-14B + DeepSeek-R1-Distill-14B on datacenter GPUs, bf16/fp16 × reduced design (3 prompts × 3 seeds × 2 temps × 2 orderings × 200 MMLU items). Tests whether variance structure changes with model scale and architecture (dense vs reasoning-distilled).\n",
1383	    "results": {
1384	      "total_records": 28800,
1385	      "conditions_per_model": 72,
1386	      "acc_qwen14b_bf16": 0.758,
1387	      "acc_qwen14b_fp16": 0.757,
1388	      "acc_deepseek14b_bf16": 0.742,
1389	      "acc_deepseek14b_fp16": 0.741,
1390	      "item_id_pct_qwen14b": 54.2,
1391	      "item_id_pct_deepseek14b": 51.8,
1392	      "avg_item_id_pct_14b": 53.0,
1393	      "delta_vs_8b_avg_pp": -4.1,
1394	      "temp_item_pct_14b_avg": 7.8,
1395	      "prec_item_pct_14b_avg": 5.1,
1396	      "prompt_item_pct_14b_avg": 6.2,
1397	      "residual_pct_14b_avg": 15.5,
1398	      "deepseek_temp_item_pct": 9.2,
1399	      "deepseek_seed_item_pct": 4.1,
1400	      "deepseek_cot_length_variance_tokens": 85,
1401	      "variance_hierarchy_preserved": true,
1402	      "item_id_still_largest": true,
1403	      "scale_effect_direction": "slight decrease in item_id with scale"
1404	    },
1405	    "tables": [
1406	      {
1407	        "name": "Table 18: 14B vs 8B variance decomposition comparison (MMLU binary)",
1408	        "columns": [
1409	          "component",
1410	          "avg_8b_pct",
1411	          "qwen14b_pct",
1412	          "deepseek14b_pct",
1413	          "avg_14b_pct"
1414	        ],
1415	        "rows": [
1416	          {
1417	            "component": "item_id",
1418	            "avg_8b_pct": 57.1,
1419	            "qwen14b_pct": 54.2,
1420	            "deepseek14b_pct": 51.8,
1421	            "avg_14b_pct": 53.0
1422	          },
1423	          {
1424	            "component": "residual",
1425	            "avg_8b_pct": 17.5,
1426	            "qwen14b_pct": 16.2,
1427	            "deepseek14b_pct": 14.8,
1428	            "avg_14b_pct": 15.5
1429	          },
1430	          {
1431	            "component": "prec:item",
1432	            "avg_8b_pct": 7.0,
1433	            "qwen14b_pct": 5.4,
1434	            "deepseek14b_pct": 4.8,
1435	            "avg_14b_pct": 5.1
1436	          },
1437	          {
1438	            "component": "temp:item",
1439	            "avg_8b_pct": 6.8,
1440	            "qwen14b_pct": 6.5,
1441	            "deepseek14b_pct": 9.2,
1442	            "avg_14b_pct": 7.8
1443	          },
1444	          {
1445	            "component": "prompt:item",
1446	            "avg_8b_pct": 5.5,
1447	            "qwen14b_pct": 6.5,
1448	            "deepseek14b_pct": 5.8,
1449	            "avg_14b_pct": 6.2
1450	          },
1451	          {
1452	            "component": "seed:item",
1453	            "avg_8b_pct": 2.1,
1454	            "qwen14b_pct": 2.5,
1455	            "deepseek14b_pct": 4.1,
1456	            "avg_14b_pct": 3.3
1457	          },
1458	          {
1459	            "component": "other",
1460	            "avg_8b_pct": 4.0,
1461	            "qwen14b_pct": 8.7,
1462	            "deepseek14b_pct": 9.5,
1463	            "avg_14b_pct": 9.1
1464	          }
1465	        ]
1466	      }
1467	    ],
1468	    "figures": [],
1469	    "analysis": "exp-005 为 Claim 1 提供 scale robustness 证据，同时揭示了 reasoning-distilled 架构的 独特方差特征。DeepSeek-R1-Distill 的 CoT 生成引入了额外的 stochasticity source—— reasoning chain length 本身成为 temperature-dependent 的随机变量，解释了其 temp×item 和 seed×item 偏高。这与 exp-002 的 cross-benchmark gradient 互补：reasoning 方差不仅 在 benchmark 层面增加（GSM8K vs MMLU），在 architecture 层面也增加（reasoning-distilled vs dense）。论文中可作为 Discussion 中的 \"convergent evidence for the reasoning-variance hypothesis\" 呈现。\n\n\n14B 模型 item_id 略低于 8B（53% vs 57%）的原因：更大的模型在更多 items 上接近 ceiling performance（p→1），这些 items 的 Bernoulli p(1-p) 方差趋近于 0，压缩了 item 方差的 分布范围。但 item_id 仍远超 40%，因为 MMLU 的难度谱足够宽（即使 14B 也有大量 p<0.8 的 items）。DeepSeek-R1-Distill 的 temp×item 9.2% 略高于 Qwen 14B 的 6.5%，因为 reasoning-distilled 架构在推理链中引入了更多 token-level sampling 变异——chain-of-thought 的中间步骤数量本身受 temperature 影响，不同难度的 items 对此敏感度不同。但差异是量级性的 （2.7pp）而非质变，variance hierarchy 完全保留。bf16≈fp16 差异在 14B 上同样 <0.2pp， 与 8B 一致。总体：scale 不改变方差结构的基本形态，Claim 1 在 7B-14B 范围内成立。\n"
1470	  },
1471	  {
1472	    "name": "Fine-tuning G-study (RoBERTa-large)",
1473	    "description": "RoBERTa-large fine-tuned on SST-2/MNLI/RTE/COPA. Fully crossed: 6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 training runs per task × 4 tasks = 1728 total runs. Each trained model evaluated on full dev/test set. Tests whether variance hierarchy differs between inference-only and fine-tuning.\n",
1474	    "results": {
1475	      "total_training_runs": 1728,
1476	      "tasks": [
1477	        "SST-2",
1478	        "MNLI",
1479	        "RTE",
1480	        "COPA"
1481	      ],
1482	      "converged_runs_pct": 96.5,
1483	      "failed_runs": 61,
1484	      "failed_runs_note": "mostly RTE/COPA with high LR — expected instability",
1485	      "sst2_acc_range": [
1486	        0.918,
1487	        0.948
1488	      ],
1489	      "mnli_acc_range": [
1490	        0.852,
1491	        0.878
1492	      ],
1493	      "rte_acc_range": [
1494	        0.621,
1495	        0.738
1496	      ],
1497	      "copa_acc_range": [
1498	        0.58,
1499	        0.69
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2adcc024-7068-4550-aca9-9cee344c30de",
  "isSidechain": false,
  "promptId": "fcb16a4e-0813-4fa9-ba4a-a5eb615d5c29",
  "type": "user",
  "uuid": "3723ad56-2b29-42fc-bb9d-a85f5b40a6f8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/experiment_data.json",
      "content": "            \"delta\": \"+3.8\"\n          },\n          {\n            \"component\": \"residual\",\n            \"single_model_avg_pct\": 17.5,\n            \"model_as_facet_pct\": 12.8,\n            \"delta\": -4.7\n          },\n          {\n            \"component\": \"prec:item\",\n            \"single_model_avg_pct\": 7.0,\n            \"model_as_facet_pct\": 6.5,\n            \"delta\": -0.5\n          },\n          {\n            \"component\": \"temp:item\",\n            \"single_model_avg_pct\": 6.8,\n            \"model_as_facet_pct\": 6.2,\n            \"delta\": -0.6\n          },\n          {\n            \"component\": \"prompt:item\",\n            \"single_model_avg_pct\": 5.5,\n            \"model_as_facet_pct\": 5.0,\n            \"delta\": -0.5\n          },\n          {\n            \"component\": \"model×prec\",\n            \"single_model_avg_pct\": \"(in precision)\",\n            \"model_as_facet_pct\": 0.5,\n            \"delta\": \"+0.5\"\n          },\n          {\n            \"component\": \"model×temp\",\n            \"single_model_avg_pct\": \"(in temperature)\",\n            \"model_as_facet_pct\": 0.3,\n            \"delta\": \"+0.3\"\n          },\n          {\n            \"component\": \"other\",\n            \"single_model_avg_pct\": 6.1,\n            \"model_as_facet_pct\": 5.5,\n            \"delta\": -0.6\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 11: Model-as-facet cross-benchmark gradient\",\n        \"columns\": [\n          \"benchmark\",\n          \"item_id_maf_pct\",\n          \"model_x_item_pct\",\n          \"gradient_from_mmlu_pp\"\n        ],\n        \"rows\": [\n          {\n            \"benchmark\": \"MMLU\",\n            \"item_id_maf_pct\": 47.3,\n            \"model_x_item_pct\": 12.1,\n            \"gradient_from_mmlu_pp\": 0.0\n          },\n          {\n            \"benchmark\": \"ARC\",\n            \"item_id_maf_pct\": 36.5,\n            \"model_x_item_pct\": 9.5,\n            \"gradient_from_mmlu_pp\": -10.8\n          },\n          {\n            \"benchmark\": \"HellaSwag\",\n            \"item_id_maf_pct\": 31.4,\n            \"model_x_item_pct\": 8.8,\n            \"gradient_from_mmlu_pp\": -15.9\n          },\n          {\n            \"benchmark\": \"GSM8K\",\n            \"item_id_maf_pct\": 18.2,\n            \"model_x_item_pct\": 6.2,\n            \"gradient_from_mmlu_pp\": -29.1\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 12: D-study optimal allocations for G≥0.90 (binary scoring)\",\n        \"columns\": [\n          \"benchmark\",\n          \"items\",\n          \"prompts\",\n          \"seeds\",\n          \"temps\",\n          \"orderings\",\n          \"total_evals\",\n          \"cost_gpu_hours\"\n        ],\n        \"rows\": [\n          {\n            \"benchmark\": \"MMLU\",\n            \"items\": 420,\n            \"prompts\": 3,\n            \"seeds\": 2,\n            \"temps\": 1,\n            \"orderings\": 1,\n            \"total_evals\": 2520,\n            \"cost_gpu_hours\": 8.4\n          },\n          {\n            \"benchmark\": \"ARC\",\n            \"items\": 320,\n            \"prompts\": 3,\n            \"seeds\": 3,\n            \"temps\": 1,\n            \"orderings\": 1,\n            \"total_evals\": 2880,\n            \"cost_gpu_hours\": 9.6\n          },\n          {\n            \"benchmark\": \"HellaSwag\",\n            \"items\": 290,\n            \"prompts\": 3,\n            \"seeds\": 3,\n            \"temps\": 1,\n            \"orderings\": 2,\n            \"total_evals\": 5220,\n            \"cost_gpu_hours\": 17.4\n          },\n          {\n            \"benchmark\": \"GSM8K\",\n            \"items\": 220,\n            \"prompts\": 4,\n            \"seeds\": 4,\n            \"temps\": 2,\n            \"orderings\": 2,\n            \"total_evals\": 14080,\n            \"cost_gpu_hours\": 28.2\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 13: D-study optimal allocations for G≥0.90 (text_exact_match)\",\n        \"columns\": [\n          \"benchmark\",\n          \"items\",\n          \"prompts\",\n          \"seeds\",\n          \"temps\",\n          \"orderings\",\n          \"total_evals\"\n        ],\n        \"rows\": [\n          {\n            \"benchmark\": \"MMLU\",\n            \"items\": 85,\n            \"prompts\": 2,\n            \"seeds\": 1,\n            \"temps\": 1,\n            \"orderings\": 1,\n            \"total_evals\": 170\n          },\n          {\n            \"benchmark\": \"ARC\",\n            \"items\": 110,\n            \"prompts\": 2,\n            \"seeds\": 1,\n            \"temps\": 1,\n            \"orderings\": 1,\n            \"total_evals\": 220\n          },\n          {\n            \"benchmark\": \"HellaSwag\",\n            \"items\": 95,\n            \"prompts\": 2,\n            \"seeds\": 2,\n            \"temps\": 1,\n            \"orderings\": 1,\n            \"total_evals\": 380\n          },\n          {\n            \"benchmark\": \"GSM8K\",\n            \"items\": 150,\n            \"prompts\": 3,\n            \"seeds\": 2,\n            \"temps\": 1,\n            \"orderings\": 1,\n            \"total_evals\": 900\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 14: IRT (tinyBenchmarks) vs G-theory item recommendations\",\n        \"columns\": [\n          \"benchmark\",\n          \"irt_items\",\n          \"gtheory_items_binary\",\n          \"ratio\",\n          \"gtheory_items_text\",\n          \"irt_text_ratio\"\n        ],\n        \"rows\": [\n          {\n            \"benchmark\": \"MMLU\",\n            \"irt_items\": 100,\n            \"gtheory_items_binary\": 420,\n            \"ratio\": 4.2,\n            \"gtheory_items_text\": 85,\n            \"irt_text_ratio\": 0.85\n          },\n          {\n            \"benchmark\": \"ARC\",\n            \"irt_items\": 75,\n            \"gtheory_items_binary\": 320,\n            \"ratio\": 4.3,\n            \"gtheory_items_text\": 110,\n            \"irt_text_ratio\": 1.47\n          },\n          {\n            \"benchmark\": \"GSM8K\",\n            \"irt_items\": 80,\n            \"gtheory_items_binary\": 220,\n            \"ratio\": 2.8,\n            \"gtheory_items_text\": 150,\n            \"irt_text_ratio\": 1.88\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 15: Bootstrap CIs on key variance components (MMLU, model-as-facet)\",\n        \"columns\": [\n          \"component\",\n          \"point_est\",\n          \"ci_lower\",\n          \"ci_upper\",\n          \"ci_width\",\n          \"overlaps next largest?\"\n        ],\n        \"rows\": [\n          {\n            \"component\": \"item_id\",\n            \"point_est\": 47.3,\n            \"ci_lower\": 44.9,\n            \"ci_upper\": 49.7,\n            \"ci_width\": 4.8,\n            \"overlaps next largest?\": \"no — gap to model×item\"\n          },\n          {\n            \"component\": \"model×item\",\n            \"point_est\": 12.1,\n            \"ci_lower\": 10.4,\n            \"ci_upper\": 13.9,\n            \"ci_width\": 3.5,\n            \"overlaps next largest?\": \"no — gap to residual\"\n          },\n          {\n            \"component\": \"residual\",\n            \"point_est\": 12.8,\n            \"ci_lower\": 10.8,\n            \"ci_upper\": 14.8,\n            \"ci_width\": 4.0,\n            \"overlaps next largest?\": \"yes — overlaps model×item\"\n          },\n          {\n            \"component\": \"prec:item\",\n            \"point_est\": 6.5,\n            \"ci_lower\": 5.2,\n            \"ci_upper\": 7.8,\n            \"ci_width\": 2.6,\n            \"overlaps next largest?\": \"yes — overlaps temp:item\"\n          },\n          {\n            \"component\": \"temp:item\",\n            \"point_est\": 6.2,\n            \"ci_lower\": 4.9,\n            \"ci_upper\": 7.5,\n            \"ci_width\": 2.6,\n            \"overlaps next largest?\": \"yes — overlaps prec:item\"\n          },\n          {\n            \"component\": \"prompt:item\",\n            \"point_est\": 5.0,\n            \"ci_lower\": 3.8,\n            \"ci_upper\": 6.2,\n            \"ci_width\": 2.4,\n            \"overlaps next largest?\": \"partial with temp:item\"\n          },\n          {\n            \"component\": \"model\",\n            \"point_est\": 3.8,\n            \"ci_lower\": 1.5,\n            \"ci_upper\": 6.1,\n            \"ci_width\": 4.6,\n            \"overlaps next largest?\": \"wide CI — 4 models\"\n          },\n          {\n            \"component\": \"prec:temp (binary)\",\n            \"point_est\": 0.2,\n            \"ci_lower\": 0.0,\n            \"ci_upper\": 0.6,\n            \"ci_width\": 0.6,\n            \"overlaps next largest?\": \"CI contains 0\"\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 16: Sensitivity analyses summary\",\n        \"columns\": [\n          \"analysis\",\n          \"comparison\",\n          \"max_delta_pp\",\n          \"robust (&lt;threshold)?\"\n        ],\n        \"rows\": [\n          {\n            \"analysis\": \"REML vs Henderson\",\n            \"comparison\": \"all components\",\n            \"max_delta_pp\": 1.8,\n            \"robust (&lt;threshold)?\": \"yes (<5pp)\"\n          },\n          {\n            \"analysis\": \"Fixed vs random (temp/ordering)\",\n            \"comparison\": \"item_id\",\n            \"max_delta_pp\": 2.8,\n            \"robust (&lt;threshold)?\": \"yes (<5pp)\"\n          },\n          {\n            \"analysis\": \"3×3 vs matched 2×2 design\",\n            \"comparison\": \"item_id\",\n            \"max_delta_pp\": 0.7,\n            \"robust (&lt;threshold)?\": \"yes (<5pp)\"\n          },\n          {\n            \"analysis\": \"Bootstrap vs jackknife CI\",\n            \"comparison\": \"CI_width_ratio\",\n            \"max_delta_pp\": 0.08,\n            \"robust (&lt;threshold)?\": \"yes (<20%)\"\n          },\n          {\n            \"analysis\": \"Bernoulli correction\",\n            \"comparison\": \"informative item_id\",\n            \"max_delta_pp\": 16.6,\n            \"robust (&lt;threshold)?\": \"corrected value 30.7% still largest\"\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 17: Logprob scoring — cross-benchmark variance (item_id%)\",\n        \"columns\": [\n          \"benchmark\",\n          \"binary\",\n          \"text_match\",\n          \"logprob\"\n        ],\n        \"rows\": [\n          {\n            \"benchmark\": \"MMLU\",\n            \"binary\": 47.3,\n            \"text_match\": 2.0,\n            \"logprob\": 52.3\n          },\n          {\n            \"benchmark\": \"ARC\",\n            \"binary\": 36.5,\n            \"text_match\": 1.8,\n            \"logprob\": 48.1\n          },\n          {\n            \"benchmark\": \"HellaSwag\",\n            \"binary\": 31.4,\n            \"text_match\": 1.5,\n            \"logprob\": 44.5\n          },\n          {\n            \"benchmark\": \"GSM8K\",\n            \"binary\": 18.2,\n            \"text_match\": 8.0,\n            \"logprob\": 31.2\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-004 是论文的分析引擎。关键结论： (1) Model-as-facet 将 item_id 降至 47.3%，但它仍是最大单一方差来源且远超 40% threshold。 model×item 12.1% 的出现解释了为什么 single-model studies 高估 item dominance——不同 模型的 item difficulty profiles 不同（Qwen 在 STEM 上更强，Mistral 在 humanities 上 更强），single-model 将这种差异性混入 item_id。 (2) Bootstrap CI 将所有 point estimates 升级为区间估计，使论文的每一个方差数字都有 统计可信度。item_id 下界 44.9% > 40% threshold 确保 Claim 1 在统计意义上成立。 (3) D-study 分化是最 actionable 的 deliverable：MMLU 需要 420 items（IRT 的 4.2×） 但仅 2520 evals，而 GSM8K 仅 220 items 但 14080 evals——因为 reasoning 任务的 interaction 方差只能通过增加 prompt/seed replications 来控制，而非增加 items。这直接 回答了 \\\"how many items do I need\\\" 的实践者问题，且答案是 \\\"depends on your benchmark and your metric\\\"。 (4) 所有 sensitivity analyses 在 robustness threshold 内，使论文对方法论批评有预防性防御。 IRT vs G-theory 比较有潜力成为 standalone contribution 甚至独立论文。\\n\\n\\n(a) Model-as-facet reanalysis将 item_id 从 57.1% 降至 47.3%：差值中 ~12.1% 重新归因为 model×item 交互（不同模型在不同 items 上有不同优势/劣势），~3.8% 归为 model 主效应 （模型间整体能力差异）。这是 G-theory 正确处理 nested vs crossed 设计的教科书结果—— single-model 分析将 model×item 方差混入 item_id 和 residual 中。关键是 item_id 即使 降至 47.3% 仍远超 40% threshold，且 cross-benchmark gradient 保持单调（29.1pp）， Claim 1 完全成立。 (b) Bootstrap CI width 4.8pp 足够窄以排斥 item_id 与 model×item 的重叠—— item_id 下界 44.9% vs model×item 上界 ~15.6%，无交集。precision×temperature 在 binary 下 CI 包含 0（不显著），在 text_match 下排除 0（显著）——精确支撑 metric-conditional separability。 (c) D-study projections 分化明显：MMLU 需要 420 items 但仅 2520 evals（item-dominated， 多 items 少 replications）；GSM8K 仅需 220 items 但 14080 evals（interaction-dominated， 少 items 多 replications）。这个 5.6× 的 eval budget 差异直接否定了 \\\"universal reproducibility recipe\\\" 的可能性——核心 deliverable。 (d-n) 所有 sensitivity analyses 均在 robustness threshold 内：REML vs Henderson <2pp, fixed vs random <3pp, design asymmetry <1pp, bootstrap vs jackknife <20%。这不是偶然—— 当 item_id 在 40-57% 量级主导时，方法论选择对结论的影响是二阶小量。 (h) IRT 4.2× ratio 是因为 tinyBenchmarks IRT 仅优化 item selection（假设单一 evaluation condition），而 G-theory D-study 在 items × prompts × seeds × temps × orderings 的 联合空间中优化——额外维度需要更多 items 来维持跨维度的可靠性。这个比较本身是 standalone contribution 级别的发现。 (l) Bernoulli 机械方差占 item_id 的 35%（correlation 0.82），但校正后 informative item_id 仍有 30.7%——远高于其他任何单一 component。parallel text_match 分析确认方差结构 在非 binary 度量下保持，驳斥 \\\"item dominance 仅是 binary scoring artifact\\\" 的批评。 (o) 14K items 下 G=0.94(binary) 说明 full MMLU 本身在 binary 下是 adequate 的， problem 在于 subsampling practices——这精确定位了 \\\"reproducibility gap\\\" 的来源。\\n\"\n  },\n  {\n    \"name\": \"14B model scale extension\",\n    \"description\": \"Qwen3-14B + DeepSeek-R1-Distill-14B on datacenter GPUs, bf16/fp16 × reduced design (3 prompts × 3 seeds × 2 temps × 2 orderings × 200 MMLU items). Tests whether variance structure changes with model scale and architecture (dense vs reasoning-distilled).\\n\",\n    \"results\": {\n      \"total_records\": 28800,\n      \"conditions_per_model\": 72,\n      \"acc_qwen14b_bf16\": 0.758,\n      \"acc_qwen14b_fp16\": 0.757,\n      \"acc_deepseek14b_bf16\": 0.742,\n      \"acc_deepseek14b_fp16\": 0.741,\n      \"item_id_pct_qwen14b\": 54.2,\n      \"item_id_pct_deepseek14b\": 51.8,\n      \"avg_item_id_pct_14b\": 53.0,\n      \"delta_vs_8b_avg_pp\": -4.1,\n      \"temp_item_pct_14b_avg\": 7.8,\n      \"prec_item_pct_14b_avg\": 5.1,\n      \"prompt_item_pct_14b_avg\": 6.2,\n      \"residual_pct_14b_avg\": 15.5,\n      \"deepseek_temp_item_pct\": 9.2,\n      \"deepseek_seed_item_pct\": 4.1,\n      \"deepseek_cot_length_variance_tokens\": 85,\n      \"variance_hierarchy_preserved\": true,\n      \"item_id_still_largest\": true,\n      \"scale_effect_direction\": \"slight decrease in item_id with scale\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 18: 14B vs 8B variance decomposition comparison (MMLU binary)\",\n        \"columns\": [\n          \"component\",\n          \"avg_8b_pct\",\n          \"qwen14b_pct\",\n          \"deepseek14b_pct\",\n          \"avg_14b_pct\"\n        ],\n        \"rows\": [\n          {\n            \"component\": \"item_id\",\n            \"avg_8b_pct\": 57.1,\n            \"qwen14b_pct\": 54.2,\n            \"deepseek14b_pct\": 51.8,\n            \"avg_14b_pct\": 53.0\n          },\n          {\n            \"component\": \"residual\",\n            \"avg_8b_pct\": 17.5,\n            \"qwen14b_pct\": 16.2,\n            \"deepseek14b_pct\": 14.8,\n            \"avg_14b_pct\": 15.5\n          },\n          {\n            \"component\": \"prec:item\",\n            \"avg_8b_pct\": 7.0,\n            \"qwen14b_pct\": 5.4,\n            \"deepseek14b_pct\": 4.8,\n            \"avg_14b_pct\": 5.1\n          },\n          {\n            \"component\": \"temp:item\",\n            \"avg_8b_pct\": 6.8,\n            \"qwen14b_pct\": 6.5,\n            \"deepseek14b_pct\": 9.2,\n            \"avg_14b_pct\": 7.8\n          },\n          {\n            \"component\": \"prompt:item\",\n            \"avg_8b_pct\": 5.5,\n            \"qwen14b_pct\": 6.5,\n            \"deepseek14b_pct\": 5.8,\n            \"avg_14b_pct\": 6.2\n          },\n          {\n            \"component\": \"seed:item\",\n            \"avg_8b_pct\": 2.1,\n            \"qwen14b_pct\": 2.5,\n            \"deepseek14b_pct\": 4.1,\n            \"avg_14b_pct\": 3.3\n          },\n          {\n            \"component\": \"other\",\n            \"avg_8b_pct\": 4.0,\n            \"qwen14b_pct\": 8.7,\n            \"deepseek14b_pct\": 9.5,\n            \"avg_14b_pct\": 9.1\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-005 为 Claim 1 提供 scale robustness 证据，同时揭示了 reasoning-distilled 架构的 独特方差特征。DeepSeek-R1-Distill 的 CoT 生成引入了额外的 stochasticity source—— reasoning chain length 本身成为 temperature-dependent 的随机变量，解释了其 temp×item 和 seed×item 偏高。这与 exp-002 的 cross-benchmark gradient 互补：reasoning 方差不仅 在 benchmark 层面增加（GSM8K vs MMLU），在 architecture 层面也增加（reasoning-distilled vs dense）。论文中可作为 Discussion 中的 \\\"convergent evidence for the reasoning-variance hypothesis\\\" 呈现。\\n\\n\\n14B 模型 item_id 略低于 8B（53% vs 57%）的原因：更大的模型在更多 items 上接近 ceiling performance（p→1），这些 items 的 Bernoulli p(1-p) 方差趋近于 0，压缩了 item 方差的 分布范围。但 item_id 仍远超 40%，因为 MMLU 的难度谱足够宽（即使 14B 也有大量 p<0.8 的 items）。DeepSeek-R1-Distill 的 temp×item 9.2% 略高于 Qwen 14B 的 6.5%，因为 reasoning-distilled 架构在推理链中引入了更多 token-level sampling 变异——chain-of-thought 的中间步骤数量本身受 temperature 影响，不同难度的 items 对此敏感度不同。但差异是量级性的 （2.7pp）而非质变，variance hierarchy 完全保留。bf16≈fp16 差异在 14B 上同样 <0.2pp， 与 8B 一致。总体：scale 不改变方差结构的基本形态，Claim 1 在 7B-14B 范围内成立。\\n\"\n  },\n  {\n    \"name\": \"Fine-tuning G-study (RoBERTa-large)\",\n    \"description\": \"RoBERTa-large fine-tuned on SST-2/MNLI/RTE/COPA. Fully crossed: 6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 training runs per task × 4 tasks = 1728 total runs. Each trained model evaluated on full dev/test set. Tests whether variance hierarchy differs between inference-only and fine-tuning.\\n\",\n    \"results\": {\n      \"total_training_runs\": 1728,\n      \"tasks\": [\n        \"SST-2\",\n        \"MNLI\",\n        \"RTE\",\n        \"COPA\"\n      ],\n      \"converged_runs_pct\": 96.5,\n      \"failed_runs\": 61,\n      \"failed_runs_note\": \"mostly RTE/COPA with high LR — expected instability\",\n      \"sst2_acc_range\": [\n        0.918,\n        0.948\n      ],\n      \"mnli_acc_range\": [\n        0.852,\n        0.878\n      ],\n      \"rte_acc_range\": [\n        0.621,\n        0.738\n      ],\n      \"copa_acc_range\": [\n        0.58,\n        0.69",
      "numLines": 500,
      "startLine": 1000,
      "totalLines": 1942
    }
  },
  "sourceToolAssistantUUID": "2adcc024-7068-4550-aca9-9cee344c30de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032813 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory…",
  "leafUuid": "3723ad56-2b29-42fc-bb9d-a85f5b40a6f8",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper for NLP variance study",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

### Tool call

_source line 28 · 2026-05-21T04:05:20.083Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MBWu8PXjobQkMtHSq5h8k2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/experiment_data.json",
  "offset": 1500,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3723ad56-2b29-42fc-bb9d-a85f5b40a6f8",
  "isSidechain": false,
  "requestId": "req_011CbF414MJngfkxjnibmJhi",
  "type": "assistant",
  "uuid": "de01aae5-fa36-4a8a-9e43-231118218031",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Fm5QPDpR4QqktbtVzufQn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8359,
      "cache_read_input_tokens": 45551,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8359,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 45551,
          "cache_creation_input_tokens": 8359,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8359
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

_source line 29 · 2026-05-21T04:05:20.344Z_

<details><summary>↩ Tool result · `toolu_01MBWu8PXjobQkMtHSq5h8k2`</summary>

```text
1500	      ],
1501	      "avg_item_id_pct": 24.8,
1502	      "avg_seed_pct": 22.5,
1503	      "avg_lr_pct": 14.2,
1504	      "avg_seed_x_item_pct": 11.8,
1505	      "avg_data_shuffle_pct": 9.3,
1506	      "avg_lr_x_item_pct": 7.2,
1507	      "avg_shuffle_x_item_pct": 4.5,
1508	      "avg_gpu_pct": 1.5,
1509	      "avg_precision_pct": 0.8,
1510	      "avg_residual_pct": 3.4,
1511	      "sst2_item_id_pct": 32.5,
1512	      "sst2_seed_pct": 18.3,
1513	      "rte_item_id_pct": 15.8,
1514	      "rte_seed_pct": 28.2,
1515	      "copa_item_id_pct": 18.5,
1516	      "copa_seed_pct": 26.8,
1517	      "inference_item_id_pct_avg": 57.1,
1518	      "finetune_item_id_pct_avg": 24.8,
1519	      "inference_seed_pct_avg": 2.1,
1520	      "finetune_seed_pct_avg": 22.5,
1521	      "variance_hierarchy_differs": true,
1522	      "g_sst2_full_design": 0.72,
1523	      "g_rte_full_design": 0.45,
1524	      "g_copa_full_design": 0.48
1525	    },
1526	    "tables": [
1527	      {
1528	        "name": "Table 19: Per-task variance decomposition — fine-tuning (binary)",
1529	        "columns": [
1530	          "component",
1531	          "SST2",
1532	          "MNLI",
1533	          "RTE",
1534	          "COPA",
1535	          "avg"
1536	        ],
1537	        "rows": [
1538	          {
1539	            "component": "item_id",
1540	            "SST2": 32.5,
1541	            "MNLI": 28.2,
1542	            "RTE": 15.8,
1543	            "COPA": 18.5,
1544	            "avg": 23.8
1545	          },
1546	          {
1547	            "component": "seed",
1548	            "SST2": 18.3,
1549	            "MNLI": 20.5,
1550	            "RTE": 28.2,
1551	            "COPA": 26.8,
1552	            "avg": 23.5
1553	          },
1554	          {
1555	            "component": "learning_rate",
1556	            "SST2": 11.5,
1557	            "MNLI": 12.8,
1558	            "RTE": 17.2,
1559	            "COPA": 15.3,
1560	            "avg": 14.2
1561	          },
1562	          {
1563	            "component": "seed×item",
1564	            "SST2": 10.2,
1565	            "MNLI": 11.5,
1566	            "RTE": 13.5,
1567	            "COPA": 12.0,
1568	            "avg": 11.8
1569	          },
1570	          {
1571	            "component": "data_shuffle",
1572	            "SST2": 8.5,
1573	            "MNLI": 10.2,
1574	            "RTE": 8.8,
1575	            "COPA": 9.5,
1576	            "avg": 9.3
1577	          },
1578	          {
1579	            "component": "lr×item",
1580	            "SST2": 6.8,
1581	            "MNLI": 7.0,
1582	            "RTE": 7.5,
1583	            "COPA": 7.3,
1584	            "avg": 7.2
1585	          },
1586	          {
1587	            "component": "shuffle×item",
1588	            "SST2": 5.0,
1589	            "MNLI": 4.2,
1590	            "RTE": 4.0,
1591	            "COPA": 4.8,
1592	            "avg": 4.5
1593	          },
1594	          {
1595	            "component": "gpu",
1596	            "SST2": 1.8,
1597	            "MNLI": 1.5,
1598	            "RTE": 1.2,
1599	            "COPA": 1.5,
1600	            "avg": 1.5
1601	          },
1602	          {
1603	            "component": "precision",
1604	            "SST2": 0.8,
1605	            "MNLI": 0.7,
1606	            "RTE": 0.9,
1607	            "COPA": 0.6,
1608	            "avg": 0.8
1609	          },
1610	          {
1611	            "component": "residual",
1612	            "SST2": 4.6,
1613	            "MNLI": 3.4,
1614	            "RTE": 2.9,
1615	            "COPA": 3.7,
1616	            "avg": 3.6
1617	          }
1618	        ]
1619	      },
1620	      {
1621	        "name": "Table 20: Inference vs fine-tuning variance hierarchy comparison",
1622	        "columns": [
1623	          "rank",
1624	          "inference_component",
1625	          "inference_pct",
1626	          "finetune_component",
1627	          "finetune_pct"
1628	        ],
1629	        "rows": [
1630	          {
1631	            "rank": 1,
1632	            "inference_component": "item_id",
1633	            "inference_pct": 57.1,
1634	            "finetune_component": "item_id",
1635	            "finetune_pct": 23.8
1636	          },
1637	          {
1638	            "rank": 2,
1639	            "inference_component": "residual",
1640	            "inference_pct": 17.5,
1641	            "finetune_component": "seed",
1642	            "finetune_pct": 23.5
1643	          },
1644	          {
1645	            "rank": 3,
1646	            "inference_component": "prec:item",
1647	            "inference_pct": 7.0,
1648	            "finetune_component": "learning_rate",
1649	            "finetune_pct": 14.2
1650	          },
1651	          {
1652	            "rank": 4,
1653	            "inference_component": "temp:item",
1654	            "inference_pct": 6.8,
1655	            "finetune_component": "seed×item",
1656	            "finetune_pct": 11.8
1657	          },
1658	          {
1659	            "rank": 5,
1660	            "inference_component": "prompt:item",
1661	            "inference_pct": 5.5,
1662	            "finetune_component": "data_shuffle",
1663	            "finetune_pct": 9.3
1664	          }
1665	        ]
1666	      }
1667	    ],
1668	    "figures": [],
1669	    "analysis": "exp-006 将方差分析框架从 inference 扩展到 fine-tuning，揭示了本质不同的方差层级。 核心发现：fine-tuning 的 \"可重复性问题\" 主要来自训练随机性（seed + shuffle + lr），而非 evaluation-time 因素。这意味着 fine-tuning 的 D-study budget 完全不同：不是 \"多采 items 少做 replications\"，而是 \"多训练 seeds 少换 hyperparameters\"。infrastructure 因素（gpu + precision）在两种 regime 下都微不足道，说明 separability 是跨 regime 的。 RTE/COPA 上的极高 seed 方差呼应了 Dodge et al. (2020) 和 Sellam et al. (2022) 的发现， 并将其纳入了 G-theory 的统一框架。 注意限制：这是 encoder-only RoBERTa 的 classification fine-tuning，不能直接外推到 decoder LLM 的指令微调——后者的方差结构可能更复杂（RLHF 引入额外随机性）。论文需要 在 Limitations 中明确标注。\n\n\nFine-tuning 与 inference 的方差层级根本不同：inference 中 item_id 58% 主导是因为模型 权重固定，方差只来自 evaluation-time 因素（prompt、seed、precision 与 item difficulty 的 交互）。Fine-tuning 引入了 training-time 随机性——seed 决定权重初始化和 dropout mask 序列， 不同 seed 产生的模型在 loss landscape 上收敛到不同 local minima，导致完全不同的 item-level prediction patterns。seed 主效应 22.5% 反映了训练不稳定性在 aggregate accuracy 上的表现 （Dodge et al. 2020 报告了类似量级的种子效应）。seed×item 11.8% 说明不同 seed 不是均匀 地提升/降低所有 items 的准确率，而是改变了哪些 items 被正确分类——这正是 \"模型选择\" 偏差的 定量证据。LR 14.2% 反映了 fine-tuning hyperparameter sensitivity（尤其在小数据集 RTE/COPA 上）。item_id 降至 24.8% 是因为训练时所有 items 都被 \"看到\" 并影响了权重更新，不像 inference 中 items 是独立的 test probes。但 item_id 仍是第二大 component（SST-2 上甚至 仍是最大的），因为 dev/test set 的 difficulty 分布本身带来了不可消除的方差。 GPU 1.5% 和 precision 0.8% 在 fine-tuning 中同样微小，进一步支撑 infrastructure separability 在 fine-tuning regime 中同样成立。 小数据集任务（RTE=2490 train, COPA=400 train）上 seed 方差更大（28%/27%），因为 smaller datasets 的 optimization landscape 更不稳定。\n"
1670	  },
1671	  {
1672	    "name": "LayerCast precision mitigation on MMLU",
1673	    "description": "LayerCast (FP16 storage + FP32 compute) as additional precision condition, compared with standard bf16/fp16/fp32. Llama-3.1-8B × 4 precision conditions × 3 prompts × 3 seeds × 2 temps × 4 orderings × 200 MMLU items.\n",
1674	    "results": {
1675	      "total_records": 19200,
1676	      "conditions": 96,
1677	      "acc_layercast": 0.715,
1678	      "acc_bf16": 0.711,
1679	      "acc_fp16": 0.711,
1680	      "acc_fp32": 0.604,
1681	      "layercast_vs_bf16_gap_pp": 0.4,
1682	      "item_id_pct_with_layercast": 58.5,
1683	      "prec_item_pct_with_layercast": 4.2,
1684	      "prec_main_pct_with_layercast": 0.8,
1685	      "prec_x_temp_pct_with_layercast": 0.1,
1686	      "prec_item_reduction_vs_standard_pct": 40,
1687	      "prec_main_reduction_vs_standard_pct": 33,
1688	      "prec_x_temp_reduction_vs_standard_pct": 50,
1689	      "g_binary_layercast_200item": 0.38,
1690	      "g_improvement_vs_standard": 0.02,
1691	      "d_study_items_g90_with_layercast": 395,
1692	      "d_study_items_reduction_vs_standard": 25
1693	    },
1694	    "tables": [
1695	      {
1696	        "name": "Table 21: Standard vs LayerCast variance decomposition (MMLU binary)",
1697	        "columns": [
1698	          "component",
1699	          "standard_3prec_pct",
1700	          "with_layercast_pct",
1701	          "reduction_pct"
1702	        ],
1703	        "rows": [
1704	          {
1705	            "component": "item_id",
1706	            "standard_3prec_pct": 57.2,
1707	            "with_layercast_pct": 58.5,
1708	            "reduction_pct": "+1.3 (redistributed)"
1709	          },
1710	          {
1711	            "component": "prec:item",
1712	            "standard_3prec_pct": 7.1,
1713	            "with_layercast_pct": 4.2,
1714	            "reduction_pct": "-40.8"
1715	          },
1716	          {
1717	            "component": "temp:item",
1718	            "standard_3prec_pct": 6.9,
1719	            "with_layercast_pct": 7.0,
1720	            "reduction_pct": "+1.4 (unchanged)"
1721	          },
1722	          {
1723	            "component": "precision",
1724	            "standard_3prec_pct": 1.1,
1725	            "with_layercast_pct": 0.8,
1726	            "reduction_pct": "-27.3"
1727	          },
1728	          {
1729	            "component": "prec:temp",
1730	            "standard_3prec_pct": 0.2,
1731	            "with_layercast_pct": 0.1,
1732	            "reduction_pct": "-50.0"
1733	          },
1734	          {
1735	            "component": "residual",
1736	            "standard_3prec_pct": 17.6,
1737	            "with_layercast_pct": 17.8,
1738	            "reduction_pct": "+1.1 (unchanged)"
1739	          }
1740	        ]
1741	      }
1742	    ],
1743	    "figures": [],
1744	    "analysis": "exp-007 提供了一个 actionable mitigation recommendation：对于需要控制精度方差的研究者， LayerCast 是比 \"全部用 bf16\" 更好的选择，因为它既保留了 FP16 的内存效率又接近 FP32 的 计算精度。但核心发现是 negative 的——即使完全消除 precision 方差，MMLU reliability improvement 微乎其微（G: 0.36→0.38, items: 420→395），因为 item 方差主导。这强化了 论文的核心信息：precision standardization 不是 reproducibility 的关键杠杆，item sampling 才是。在论文中定位为 Discussion 中的 practical recommendation，而非独立 claim。\n\n\nLayerCast 在 FP16 精度下存储权重但以 FP32 精度执行计算，消除了计算过程中的精度损失 同时保留了内存效率。它产生接近 bf16 的准确率（+0.4pp，因为 FP32 compute path 略优于 bf16 的 bfloat16 compute）而非 fp32-V0-eager 的降幅。precision:item 交互从 7.0% 降至 4.2%——reduction 是 40% 而非 100%，因为 LayerCast 仍使用 FP16 存储（权重的低精度表示 仍引入 item-level 的微小差异），但 FP32 compute 消除了运算中的精度累积误差。precision 主效应从 1.2% 降至 0.8%——因为 LayerCast 的准确率更接近 bf16（0.4pp gap vs fp32 的 8.9pp gap），reducing inter-precision variability。precision×temperature 从 0.2% 降至 0.1%——本已微小的交互被进一步压缩。G-coefficient 仅改善 0.02（0.36→0.38）因为 precision 相关方差原本只占 ~8%，即使全部消除 G 也只提升 ~0.03。D-study 从 420→395 items（仅减 25）进一步说明 precision 不是 MMLU 可靠性的瓶颈——item 本身才是。LayerCast 的实用价值 在于它是一个 low-cost \"free lunch\"：几乎无性能损失的同时减少了一个 confound source。\n"
1745	  },
1746	  {
1747	    "name": "MATH benchmark — extreme reasoning endpoint",
1748	    "description": "4 models × bf16/fp16 (Gemma bf16 only) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 MATH items (stratified by difficulty level 1-5). Tests whether item dominance pattern reaches its minimum on the most reasoning-heavy benchmark, extending the gradient with a 5th data point.\n",
1749	    "results": {
1750	      "total_records": 403200,
1751	      "models_complete": 4,
1752	      "acc_llama_bf16": 0.228,
1753	      "acc_qwen_bf16": 0.342,
1754	      "acc_mistral_bf16": 0.165,
1755	      "acc_gemma_bf16": 0.258,
1756	      "overall_accuracy": 0.251,
1757	      "item_id_pct_binary": 16.8,
1758	      "temp_item_pct_binary": 21.3,
1759	      "residual_pct_binary": 24.5,
1760	      "seed_item_pct_binary": 14.7,
1761	      "prompt_item_pct_binary": 8.8,
1762	      "temp_main_pct_binary": 5.8,
1763	      "prec_item_pct_binary": 2.5,
1764	      "ordering_item_pct_binary": 2.2,
1765	      "prec_main_pct_binary": 0.6,
1766	      "prec_x_temp_binary": 0.5,
1767	      "other_binary": 2.3,
1768	      "gradient_5_benchmarks": "MMLU(57.1) > ARC(43.7) > HellaSwag(38.2) > GSM8K(22.4) > MATH(16.8)",
1769	      "gradient_total_pp_5bench": 40.3,
1770	      "gradient_monotonic_5bench": true,
1771	      "item_id_pct_text": 5.2,
1772	      "prompt_item_pct_text": 31.5,
1773	      "temp_main_pct_text": 18.2,
1774	      "temp_item_pct_text": 15.8,
1775	      "prec_x_temp_text": 2.8,
1776	      "residual_pct_text": 22.3,
1777	      "g_binary_200item": 0.51,
1778	      "g_text_200item": 0.62,
1779	      "d_study_items_g90_binary": 180,
1780	      "d_study_allocation_binary": "180 items × 5 prompts × 5 seeds × 2 temps × 2 orderings = 18000 evals",
1781	      "d_study_items_g90_text": 250,
1782	      "d_study_allocation_text": "250 items × 4 prompts × 3 seeds × 2 temps × 1 ordering = 6000 evals"
1783	    },
1784	    "tables": [
1785	      {
1786	        "name": "Table 22: MATH variance decomposition by difficulty level (binary, Qwen3-8B)",
1787	        "columns": [
1788	          "component",
1789	          "Level_1",
1790	          "Level_2",
1791	          "Level_3",
1792	          "Level_4",
1793	          "Level_5"
1794	        ],
1795	        "rows": [
1796	          {
1797	            "component": "item_id",
1798	            "Level_1": 28.5,
1799	            "Level_2": 22.1,
1800	            "Level_3": 16.5,
1801	            "Level_4": 12.8,
1802	            "Level_5": 8.2
1803	          },
1804	          {
1805	            "component": "temp:item",
1806	            "Level_1": 8.5,
1807	            "Level_2": 14.2,
1808	            "Level_3": 22.5,
1809	            "Level_4": 26.8,
1810	            "Level_5": 30.1
1811	          },
1812	          {
1813	            "component": "seed:item",
1814	            "Level_1": 5.2,
1815	            "Level_2": 10.8,
1816	            "Level_3": 15.2,
1817	            "Level_4": 18.5,
1818	            "Level_5": 22.0
1819	          },
1820	          {
1821	            "component": "residual",
1822	            "Level_1": 32.5,
1823	            "Level_2": 28.2,
1824	            "Level_3": 23.5,
1825	            "Level_4": 21.2,
1826	            "Level_5": 18.8
1827	          },
1828	          {
1829	            "component": "other",
1830	            "Level_1": 25.3,
1831	            "Level_2": 24.7,
1832	            "Level_3": 22.3,
1833	            "Level_4": 20.7,
1834	            "Level_5": 20.9
1835	          }
1836	        ]
1837	      },
1838	      {
1839	        "name": "Table 23: Extended 5-benchmark gradient summary",
1840	        "columns": [
1841	          "benchmark",
1842	          "task_type",
1843	          "cognitive_complexity",
1844	          "item_id_pct",
1845	          "sum_interactions_pct",
1846	          "g_binary_200"
1847	        ],
1848	        "rows": [
1849	          {
1850	            "benchmark": "MMLU",
1851	            "task_type": "knowledge",
1852	            "cognitive_complexity": 1,
1853	            "item_id_pct": 57.1,
1854	            "sum_interactions_pct": 22.9,
1855	            "g_binary_200": 0.36
1856	          },
1857	          {
1858	            "benchmark": "ARC",
1859	            "task_type": "science",
1860	            "cognitive_complexity": 2,
1861	            "item_id_pct": 43.7,
1862	            "sum_interactions_pct": 31.8,
1863	            "g_binary_200": 0.42
1864	          },
1865	          {
1866	            "benchmark": "HellaSwag",
1867	            "task_type": "commonsense",
1868	            "cognitive_complexity": 3,
1869	            "item_id_pct": 38.2,
1870	            "sum_interactions_pct": 35.8,
1871	            "g_binary_200": 0.44
1872	          },
1873	          {
1874	            "benchmark": "GSM8K",
1875	            "task_type": "math_simple",
1876	            "cognitive_complexity": 4,
1877	            "item_id_pct": 22.4,
1878	            "sum_interactions_pct": 46.3,
1879	            "g_binary_200": 0.48
1880	          },
1881	          {
1882	            "benchmark": "MATH",
1883	            "task_type": "math_hard",
1884	            "cognitive_complexity": 5,
1885	            "item_id_pct": 16.8,
1886	            "sum_interactions_pct": 49.5,
1887	            "g_binary_200": 0.51
1888	          }
1889	        ]
1890	      },
1891	      {
1892	        "name": "Table 24: D-study total evaluation budget comparison (G≥0.90 binary)",
1893	        "columns": [
1894	          "benchmark",
1895	          "items",
1896	          "total_evals",
1897	          "evals_per_item",
1898	          "relative_to_mmlu"
1899	        ],
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de01aae5-fa36-4a8a-9e43-231118218031",
  "isSidechain": false,
  "promptId": "fcb16a4e-0813-4fa9-ba4a-a5eb615d5c29",
  "type": "user",
  "uuid": "8ce520ca-6ce8-4f34-a5dd-233d3430f234",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/experiment_data.json",
      "content": "      ],\n      \"avg_item_id_pct\": 24.8,\n      \"avg_seed_pct\": 22.5,\n      \"avg_lr_pct\": 14.2,\n      \"avg_seed_x_item_pct\": 11.8,\n      \"avg_data_shuffle_pct\": 9.3,\n      \"avg_lr_x_item_pct\": 7.2,\n      \"avg_shuffle_x_item_pct\": 4.5,\n      \"avg_gpu_pct\": 1.5,\n      \"avg_precision_pct\": 0.8,\n      \"avg_residual_pct\": 3.4,\n      \"sst2_item_id_pct\": 32.5,\n      \"sst2_seed_pct\": 18.3,\n      \"rte_item_id_pct\": 15.8,\n      \"rte_seed_pct\": 28.2,\n      \"copa_item_id_pct\": 18.5,\n      \"copa_seed_pct\": 26.8,\n      \"inference_item_id_pct_avg\": 57.1,\n      \"finetune_item_id_pct_avg\": 24.8,\n      \"inference_seed_pct_avg\": 2.1,\n      \"finetune_seed_pct_avg\": 22.5,\n      \"variance_hierarchy_differs\": true,\n      \"g_sst2_full_design\": 0.72,\n      \"g_rte_full_design\": 0.45,\n      \"g_copa_full_design\": 0.48\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 19: Per-task variance decomposition — fine-tuning (binary)\",\n        \"columns\": [\n          \"component\",\n          \"SST2\",\n          \"MNLI\",\n          \"RTE\",\n          \"COPA\",\n          \"avg\"\n        ],\n        \"rows\": [\n          {\n            \"component\": \"item_id\",\n            \"SST2\": 32.5,\n            \"MNLI\": 28.2,\n            \"RTE\": 15.8,\n            \"COPA\": 18.5,\n            \"avg\": 23.8\n          },\n          {\n            \"component\": \"seed\",\n            \"SST2\": 18.3,\n            \"MNLI\": 20.5,\n            \"RTE\": 28.2,\n            \"COPA\": 26.8,\n            \"avg\": 23.5\n          },\n          {\n            \"component\": \"learning_rate\",\n            \"SST2\": 11.5,\n            \"MNLI\": 12.8,\n            \"RTE\": 17.2,\n            \"COPA\": 15.3,\n            \"avg\": 14.2\n          },\n          {\n            \"component\": \"seed×item\",\n            \"SST2\": 10.2,\n            \"MNLI\": 11.5,\n            \"RTE\": 13.5,\n            \"COPA\": 12.0,\n            \"avg\": 11.8\n          },\n          {\n            \"component\": \"data_shuffle\",\n            \"SST2\": 8.5,\n            \"MNLI\": 10.2,\n            \"RTE\": 8.8,\n            \"COPA\": 9.5,\n            \"avg\": 9.3\n          },\n          {\n            \"component\": \"lr×item\",\n            \"SST2\": 6.8,\n            \"MNLI\": 7.0,\n            \"RTE\": 7.5,\n            \"COPA\": 7.3,\n            \"avg\": 7.2\n          },\n          {\n            \"component\": \"shuffle×item\",\n            \"SST2\": 5.0,\n            \"MNLI\": 4.2,\n            \"RTE\": 4.0,\n            \"COPA\": 4.8,\n            \"avg\": 4.5\n          },\n          {\n            \"component\": \"gpu\",\n            \"SST2\": 1.8,\n            \"MNLI\": 1.5,\n            \"RTE\": 1.2,\n            \"COPA\": 1.5,\n            \"avg\": 1.5\n          },\n          {\n            \"component\": \"precision\",\n            \"SST2\": 0.8,\n            \"MNLI\": 0.7,\n            \"RTE\": 0.9,\n            \"COPA\": 0.6,\n            \"avg\": 0.8\n          },\n          {\n            \"component\": \"residual\",\n            \"SST2\": 4.6,\n            \"MNLI\": 3.4,\n            \"RTE\": 2.9,\n            \"COPA\": 3.7,\n            \"avg\": 3.6\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 20: Inference vs fine-tuning variance hierarchy comparison\",\n        \"columns\": [\n          \"rank\",\n          \"inference_component\",\n          \"inference_pct\",\n          \"finetune_component\",\n          \"finetune_pct\"\n        ],\n        \"rows\": [\n          {\n            \"rank\": 1,\n            \"inference_component\": \"item_id\",\n            \"inference_pct\": 57.1,\n            \"finetune_component\": \"item_id\",\n            \"finetune_pct\": 23.8\n          },\n          {\n            \"rank\": 2,\n            \"inference_component\": \"residual\",\n            \"inference_pct\": 17.5,\n            \"finetune_component\": \"seed\",\n            \"finetune_pct\": 23.5\n          },\n          {\n            \"rank\": 3,\n            \"inference_component\": \"prec:item\",\n            \"inference_pct\": 7.0,\n            \"finetune_component\": \"learning_rate\",\n            \"finetune_pct\": 14.2\n          },\n          {\n            \"rank\": 4,\n            \"inference_component\": \"temp:item\",\n            \"inference_pct\": 6.8,\n            \"finetune_component\": \"seed×item\",\n            \"finetune_pct\": 11.8\n          },\n          {\n            \"rank\": 5,\n            \"inference_component\": \"prompt:item\",\n            \"inference_pct\": 5.5,\n            \"finetune_component\": \"data_shuffle\",\n            \"finetune_pct\": 9.3\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-006 将方差分析框架从 inference 扩展到 fine-tuning，揭示了本质不同的方差层级。 核心发现：fine-tuning 的 \\\"可重复性问题\\\" 主要来自训练随机性（seed + shuffle + lr），而非 evaluation-time 因素。这意味着 fine-tuning 的 D-study budget 完全不同：不是 \\\"多采 items 少做 replications\\\"，而是 \\\"多训练 seeds 少换 hyperparameters\\\"。infrastructure 因素（gpu + precision）在两种 regime 下都微不足道，说明 separability 是跨 regime 的。 RTE/COPA 上的极高 seed 方差呼应了 Dodge et al. (2020) 和 Sellam et al. (2022) 的发现， 并将其纳入了 G-theory 的统一框架。 注意限制：这是 encoder-only RoBERTa 的 classification fine-tuning，不能直接外推到 decoder LLM 的指令微调——后者的方差结构可能更复杂（RLHF 引入额外随机性）。论文需要 在 Limitations 中明确标注。\\n\\n\\nFine-tuning 与 inference 的方差层级根本不同：inference 中 item_id 58% 主导是因为模型 权重固定，方差只来自 evaluation-time 因素（prompt、seed、precision 与 item difficulty 的 交互）。Fine-tuning 引入了 training-time 随机性——seed 决定权重初始化和 dropout mask 序列， 不同 seed 产生的模型在 loss landscape 上收敛到不同 local minima，导致完全不同的 item-level prediction patterns。seed 主效应 22.5% 反映了训练不稳定性在 aggregate accuracy 上的表现 （Dodge et al. 2020 报告了类似量级的种子效应）。seed×item 11.8% 说明不同 seed 不是均匀 地提升/降低所有 items 的准确率，而是改变了哪些 items 被正确分类——这正是 \\\"模型选择\\\" 偏差的 定量证据。LR 14.2% 反映了 fine-tuning hyperparameter sensitivity（尤其在小数据集 RTE/COPA 上）。item_id 降至 24.8% 是因为训练时所有 items 都被 \\\"看到\\\" 并影响了权重更新，不像 inference 中 items 是独立的 test probes。但 item_id 仍是第二大 component（SST-2 上甚至 仍是最大的），因为 dev/test set 的 difficulty 分布本身带来了不可消除的方差。 GPU 1.5% 和 precision 0.8% 在 fine-tuning 中同样微小，进一步支撑 infrastructure separability 在 fine-tuning regime 中同样成立。 小数据集任务（RTE=2490 train, COPA=400 train）上 seed 方差更大（28%/27%），因为 smaller datasets 的 optimization landscape 更不稳定。\\n\"\n  },\n  {\n    \"name\": \"LayerCast precision mitigation on MMLU\",\n    \"description\": \"LayerCast (FP16 storage + FP32 compute) as additional precision condition, compared with standard bf16/fp16/fp32. Llama-3.1-8B × 4 precision conditions × 3 prompts × 3 seeds × 2 temps × 4 orderings × 200 MMLU items.\\n\",\n    \"results\": {\n      \"total_records\": 19200,\n      \"conditions\": 96,\n      \"acc_layercast\": 0.715,\n      \"acc_bf16\": 0.711,\n      \"acc_fp16\": 0.711,\n      \"acc_fp32\": 0.604,\n      \"layercast_vs_bf16_gap_pp\": 0.4,\n      \"item_id_pct_with_layercast\": 58.5,\n      \"prec_item_pct_with_layercast\": 4.2,\n      \"prec_main_pct_with_layercast\": 0.8,\n      \"prec_x_temp_pct_with_layercast\": 0.1,\n      \"prec_item_reduction_vs_standard_pct\": 40,\n      \"prec_main_reduction_vs_standard_pct\": 33,\n      \"prec_x_temp_reduction_vs_standard_pct\": 50,\n      \"g_binary_layercast_200item\": 0.38,\n      \"g_improvement_vs_standard\": 0.02,\n      \"d_study_items_g90_with_layercast\": 395,\n      \"d_study_items_reduction_vs_standard\": 25\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 21: Standard vs LayerCast variance decomposition (MMLU binary)\",\n        \"columns\": [\n          \"component\",\n          \"standard_3prec_pct\",\n          \"with_layercast_pct\",\n          \"reduction_pct\"\n        ],\n        \"rows\": [\n          {\n            \"component\": \"item_id\",\n            \"standard_3prec_pct\": 57.2,\n            \"with_layercast_pct\": 58.5,\n            \"reduction_pct\": \"+1.3 (redistributed)\"\n          },\n          {\n            \"component\": \"prec:item\",\n            \"standard_3prec_pct\": 7.1,\n            \"with_layercast_pct\": 4.2,\n            \"reduction_pct\": \"-40.8\"\n          },\n          {\n            \"component\": \"temp:item\",\n            \"standard_3prec_pct\": 6.9,\n            \"with_layercast_pct\": 7.0,\n            \"reduction_pct\": \"+1.4 (unchanged)\"\n          },\n          {\n            \"component\": \"precision\",\n            \"standard_3prec_pct\": 1.1,\n            \"with_layercast_pct\": 0.8,\n            \"reduction_pct\": \"-27.3\"\n          },\n          {\n            \"component\": \"prec:temp\",\n            \"standard_3prec_pct\": 0.2,\n            \"with_layercast_pct\": 0.1,\n            \"reduction_pct\": \"-50.0\"\n          },\n          {\n            \"component\": \"residual\",\n            \"standard_3prec_pct\": 17.6,\n            \"with_layercast_pct\": 17.8,\n            \"reduction_pct\": \"+1.1 (unchanged)\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-007 提供了一个 actionable mitigation recommendation：对于需要控制精度方差的研究者， LayerCast 是比 \\\"全部用 bf16\\\" 更好的选择，因为它既保留了 FP16 的内存效率又接近 FP32 的 计算精度。但核心发现是 negative 的——即使完全消除 precision 方差，MMLU reliability improvement 微乎其微（G: 0.36→0.38, items: 420→395），因为 item 方差主导。这强化了 论文的核心信息：precision standardization 不是 reproducibility 的关键杠杆，item sampling 才是。在论文中定位为 Discussion 中的 practical recommendation，而非独立 claim。\\n\\n\\nLayerCast 在 FP16 精度下存储权重但以 FP32 精度执行计算，消除了计算过程中的精度损失 同时保留了内存效率。它产生接近 bf16 的准确率（+0.4pp，因为 FP32 compute path 略优于 bf16 的 bfloat16 compute）而非 fp32-V0-eager 的降幅。precision:item 交互从 7.0% 降至 4.2%——reduction 是 40% 而非 100%，因为 LayerCast 仍使用 FP16 存储（权重的低精度表示 仍引入 item-level 的微小差异），但 FP32 compute 消除了运算中的精度累积误差。precision 主效应从 1.2% 降至 0.8%——因为 LayerCast 的准确率更接近 bf16（0.4pp gap vs fp32 的 8.9pp gap），reducing inter-precision variability。precision×temperature 从 0.2% 降至 0.1%——本已微小的交互被进一步压缩。G-coefficient 仅改善 0.02（0.36→0.38）因为 precision 相关方差原本只占 ~8%，即使全部消除 G 也只提升 ~0.03。D-study 从 420→395 items（仅减 25）进一步说明 precision 不是 MMLU 可靠性的瓶颈——item 本身才是。LayerCast 的实用价值 在于它是一个 low-cost \\\"free lunch\\\"：几乎无性能损失的同时减少了一个 confound source。\\n\"\n  },\n  {\n    \"name\": \"MATH benchmark — extreme reasoning endpoint\",\n    \"description\": \"4 models × bf16/fp16 (Gemma bf16 only) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 MATH items (stratified by difficulty level 1-5). Tests whether item dominance pattern reaches its minimum on the most reasoning-heavy benchmark, extending the gradient with a 5th data point.\\n\",\n    \"results\": {\n      \"total_records\": 403200,\n      \"models_complete\": 4,\n      \"acc_llama_bf16\": 0.228,\n      \"acc_qwen_bf16\": 0.342,\n      \"acc_mistral_bf16\": 0.165,\n      \"acc_gemma_bf16\": 0.258,\n      \"overall_accuracy\": 0.251,\n      \"item_id_pct_binary\": 16.8,\n      \"temp_item_pct_binary\": 21.3,\n      \"residual_pct_binary\": 24.5,\n      \"seed_item_pct_binary\": 14.7,\n      \"prompt_item_pct_binary\": 8.8,\n      \"temp_main_pct_binary\": 5.8,\n      \"prec_item_pct_binary\": 2.5,\n      \"ordering_item_pct_binary\": 2.2,\n      \"prec_main_pct_binary\": 0.6,\n      \"prec_x_temp_binary\": 0.5,\n      \"other_binary\": 2.3,\n      \"gradient_5_benchmarks\": \"MMLU(57.1) > ARC(43.7) > HellaSwag(38.2) > GSM8K(22.4) > MATH(16.8)\",\n      \"gradient_total_pp_5bench\": 40.3,\n      \"gradient_monotonic_5bench\": true,\n      \"item_id_pct_text\": 5.2,\n      \"prompt_item_pct_text\": 31.5,\n      \"temp_main_pct_text\": 18.2,\n      \"temp_item_pct_text\": 15.8,\n      \"prec_x_temp_text\": 2.8,\n      \"residual_pct_text\": 22.3,\n      \"g_binary_200item\": 0.51,\n      \"g_text_200item\": 0.62,\n      \"d_study_items_g90_binary\": 180,\n      \"d_study_allocation_binary\": \"180 items × 5 prompts × 5 seeds × 2 temps × 2 orderings = 18000 evals\",\n      \"d_study_items_g90_text\": 250,\n      \"d_study_allocation_text\": \"250 items × 4 prompts × 3 seeds × 2 temps × 1 ordering = 6000 evals\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 22: MATH variance decomposition by difficulty level (binary, Qwen3-8B)\",\n        \"columns\": [\n          \"component\",\n          \"Level_1\",\n          \"Level_2\",\n          \"Level_3\",\n          \"Level_4\",\n          \"Level_5\"\n        ],\n        \"rows\": [\n          {\n            \"component\": \"item_id\",\n            \"Level_1\": 28.5,\n            \"Level_2\": 22.1,\n            \"Level_3\": 16.5,\n            \"Level_4\": 12.8,\n            \"Level_5\": 8.2\n          },\n          {\n            \"component\": \"temp:item\",\n            \"Level_1\": 8.5,\n            \"Level_2\": 14.2,\n            \"Level_3\": 22.5,\n            \"Level_4\": 26.8,\n            \"Level_5\": 30.1\n          },\n          {\n            \"component\": \"seed:item\",\n            \"Level_1\": 5.2,\n            \"Level_2\": 10.8,\n            \"Level_3\": 15.2,\n            \"Level_4\": 18.5,\n            \"Level_5\": 22.0\n          },\n          {\n            \"component\": \"residual\",\n            \"Level_1\": 32.5,\n            \"Level_2\": 28.2,\n            \"Level_3\": 23.5,\n            \"Level_4\": 21.2,\n            \"Level_5\": 18.8\n          },\n          {\n            \"component\": \"other\",\n            \"Level_1\": 25.3,\n            \"Level_2\": 24.7,\n            \"Level_3\": 22.3,\n            \"Level_4\": 20.7,\n            \"Level_5\": 20.9\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 23: Extended 5-benchmark gradient summary\",\n        \"columns\": [\n          \"benchmark\",\n          \"task_type\",\n          \"cognitive_complexity\",\n          \"item_id_pct\",\n          \"sum_interactions_pct\",\n          \"g_binary_200\"\n        ],\n        \"rows\": [\n          {\n            \"benchmark\": \"MMLU\",\n            \"task_type\": \"knowledge\",\n            \"cognitive_complexity\": 1,\n            \"item_id_pct\": 57.1,\n            \"sum_interactions_pct\": 22.9,\n            \"g_binary_200\": 0.36\n          },\n          {\n            \"benchmark\": \"ARC\",\n            \"task_type\": \"science\",\n            \"cognitive_complexity\": 2,\n            \"item_id_pct\": 43.7,\n            \"sum_interactions_pct\": 31.8,\n            \"g_binary_200\": 0.42\n          },\n          {\n            \"benchmark\": \"HellaSwag\",\n            \"task_type\": \"commonsense\",\n            \"cognitive_complexity\": 3,\n            \"item_id_pct\": 38.2,\n            \"sum_interactions_pct\": 35.8,\n            \"g_binary_200\": 0.44\n          },\n          {\n            \"benchmark\": \"GSM8K\",\n            \"task_type\": \"math_simple\",\n            \"cognitive_complexity\": 4,\n            \"item_id_pct\": 22.4,\n            \"sum_interactions_pct\": 46.3,\n            \"g_binary_200\": 0.48\n          },\n          {\n            \"benchmark\": \"MATH\",\n            \"task_type\": \"math_hard\",\n            \"cognitive_complexity\": 5,\n            \"item_id_pct\": 16.8,\n            \"sum_interactions_pct\": 49.5,\n            \"g_binary_200\": 0.51\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 24: D-study total evaluation budget comparison (G≥0.90 binary)\",\n        \"columns\": [\n          \"benchmark\",\n          \"items\",\n          \"total_evals\",\n          \"evals_per_item\",\n          \"relative_to_mmlu\"\n        ],",
      "numLines": 400,
      "startLine": 1500,
      "totalLines": 1942
    }
  },
  "sourceToolAssistantUUID": "de01aae5-fa36-4a8a-9e43-231118218031",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032813 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory…",
  "leafUuid": "8ce520ca-6ce8-4f34-a5dd-233d3430f234",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper for NLP variance study",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

### Tool call

_source line 32 · 2026-05-21T04:05:33.091Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L1xwWbYE1Goo3MuJMCsQYo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/experiment_data.json",
  "offset": 1900,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ce520ca-6ce8-4f34-a5dd-233d3430f234",
  "isSidechain": false,
  "requestId": "req_011CbF41Syb33abVzJBbkU79",
  "type": "assistant",
  "uuid": "a9829c88-810c-4483-8f53-45e8aa2bc88e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YSAfTLufRpG2LYuQhUKinQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7286,
      "cache_read_input_tokens": 53910,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 53910,
          "cache_creation_input_tokens": 7286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7286
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

_source line 33 · 2026-05-21T04:05:33.096Z_

<details><summary>↩ Tool result · `toolu_01L1xwWbYE1Goo3MuJMCsQYo`</summary>

```text
1900	        "rows": [
1901	          {
1902	            "benchmark": "MMLU",
1903	            "items": 420,
1904	            "total_evals": 2520,
1905	            "evals_per_item": 6,
1906	            "relative_to_mmlu": "1.0×"
1907	          },
1908	          {
1909	            "benchmark": "ARC",
1910	            "items": 320,
1911	            "total_evals": 2880,
1912	            "evals_per_item": 9,
1913	            "relative_to_mmlu": "1.1×"
1914	          },
1915	          {
1916	            "benchmark": "HellaSwag",
1917	            "items": 290,
1918	            "total_evals": 5220,
1919	            "evals_per_item": 18,
1920	            "relative_to_mmlu": "2.1×"
1921	          },
1922	          {
1923	            "benchmark": "GSM8K",
1924	            "items": 220,
1925	            "total_evals": 14080,
1926	            "evals_per_item": 64,
1927	            "relative_to_mmlu": "5.6×"
1928	          },
1929	          {
1930	            "benchmark": "MATH",
1931	            "items": 180,
1932	            "total_evals": 18000,
1933	            "evals_per_item": 100,
1934	            "relative_to_mmlu": "7.1×"
1935	          }
1936	        ]
1937	      }
1938	    ],
1939	    "figures": [],
1940	    "analysis": "exp-008 完成了 cross-benchmark gradient 的五点图景，MATH 作为 reasoning 极端端点提供了 最强的 gradient 证据。内部 difficulty-level 分析（Table 22）揭示了 gradient 的微观机制： 在 MATH 内部，Level 1 题目的方差结构类似 MMLU（item-dominated），Level 5 类似 \"pure stochastic process\"（interaction-dominated）——gradient 不是 benchmark 间的离散 跳跃而是连续的认知复杂度函数。 D-study budget 的极端分化（MMLU 2520 vs MATH 18000 evals）是论文 \"illusory universal recipe\" 论点的 strongest evidence。任何推荐 \"use N items and you're fine\" 的 guideline 都隐含了对 task type 和 metric 的假设——exp-008 证明这些假设不成立。 MATH 上 precision×temperature 0.5%(binary) 接近但未超过 0.8% threshold，保持了 Claim 2 的 universal 成立。但 text_match 2.8% 几乎达到 3.0% 上限，说明 MATH 是 separability 最脆弱的 benchmark——这与其 long-generation 特性一致。 论文中 exp-008 的数据与 exp-002 合并呈现为 5-benchmark gradient，不单独成章。\n\nMATH 代表了 reasoning intensity 的极端——每题需要多步数学推理，每步 token generation 都受 temperature 和 seed 影响，且步骤间有 error propagation（一步错全盘错）。这解释了 temp×item 21.3%（最高值，因为 temperature 对长推理链的影响在 easy 和 hard items 间有 巨大差异——Level 1 题目一步可解几乎不受 temperature 影响，Level 5 题目 8-10 步每步都可能 在不同 temperature 下走向不同推理路径）。seed×item 14.7% 同理——CUDA nondeterminism 在 长 generation 中逐步累积，其影响与 problem complexity 正相关。 item_id 16.8% 是五个 benchmark 中最低的，因为 MATH items 的 difficulty 分布与 MMLU 不同： 8B 模型在 MATH 上整体准确率只有 25%，大量 items 集中在 p<0.1（几乎不可能做对），这些 items 的 Bernoulli p(1-p) 方差极小，压缩了 item_id 的总贡献。residual 24.5% 反映了 大量未建模的高阶交互（temp×seed×item, prompt×seed×item），这些在短输出的 MC 任务中 可忽略但在长推理链中显著。 precision×temperature 在 binary 下 0.5%（接近 0.8% 上限但仍在范围内），在 text_match 下 2.8%——MATH 的长推理链使浮点非结合性效应最大化。 gradient 扩展到 5 点后仍单调，从 57.1% 降至 16.8%（40.3pp span），且趋势近似线性—— 认知复杂度与 item dominance 之间存在 systematic 的反比关系。这是 \"benchmark-conditional variance structure\" 论点的最强证据。 G=0.51(binary) 在 MATH 上反而高于 MMLU(0.36)——尽管 counter-intuitive，这是因为 MATH 的低 item 方差意味着 200 items 已足够 \"代表\" item universe，可靠性瓶颈在 prompt/seed replications 而非 item sampling。D-study 验证了这一点：MATH 仅需 180 items（最少）但 18000 evals（最多），是 MMLU 的 7.1×——\"no universal recipe\" 的极端案例。\n"
1941	  }
1942	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9829c88-810c-4483-8f53-45e8aa2bc88e",
  "isSidechain": false,
  "promptId": "fcb16a4e-0813-4fa9-ba4a-a5eb615d5c29",
  "type": "user",
  "uuid": "e549c7ee-6441-4d8b-9496-8f566b225b98",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/experiment_data.json",
      "content": "        \"rows\": [\n          {\n            \"benchmark\": \"MMLU\",\n            \"items\": 420,\n            \"total_evals\": 2520,\n            \"evals_per_item\": 6,\n            \"relative_to_mmlu\": \"1.0×\"\n          },\n          {\n            \"benchmark\": \"ARC\",\n            \"items\": 320,\n            \"total_evals\": 2880,\n            \"evals_per_item\": 9,\n            \"relative_to_mmlu\": \"1.1×\"\n          },\n          {\n            \"benchmark\": \"HellaSwag\",\n            \"items\": 290,\n            \"total_evals\": 5220,\n            \"evals_per_item\": 18,\n            \"relative_to_mmlu\": \"2.1×\"\n          },\n          {\n            \"benchmark\": \"GSM8K\",\n            \"items\": 220,\n            \"total_evals\": 14080,\n            \"evals_per_item\": 64,\n            \"relative_to_mmlu\": \"5.6×\"\n          },\n          {\n            \"benchmark\": \"MATH\",\n            \"items\": 180,\n            \"total_evals\": 18000,\n            \"evals_per_item\": 100,\n            \"relative_to_mmlu\": \"7.1×\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-008 完成了 cross-benchmark gradient 的五点图景，MATH 作为 reasoning 极端端点提供了 最强的 gradient 证据。内部 difficulty-level 分析（Table 22）揭示了 gradient 的微观机制： 在 MATH 内部，Level 1 题目的方差结构类似 MMLU（item-dominated），Level 5 类似 \\\"pure stochastic process\\\"（interaction-dominated）——gradient 不是 benchmark 间的离散 跳跃而是连续的认知复杂度函数。 D-study budget 的极端分化（MMLU 2520 vs MATH 18000 evals）是论文 \\\"illusory universal recipe\\\" 论点的 strongest evidence。任何推荐 \\\"use N items and you're fine\\\" 的 guideline 都隐含了对 task type 和 metric 的假设——exp-008 证明这些假设不成立。 MATH 上 precision×temperature 0.5%(binary) 接近但未超过 0.8% threshold，保持了 Claim 2 的 universal 成立。但 text_match 2.8% 几乎达到 3.0% 上限，说明 MATH 是 separability 最脆弱的 benchmark——这与其 long-generation 特性一致。 论文中 exp-008 的数据与 exp-002 合并呈现为 5-benchmark gradient，不单独成章。\\n\\nMATH 代表了 reasoning intensity 的极端——每题需要多步数学推理，每步 token generation 都受 temperature 和 seed 影响，且步骤间有 error propagation（一步错全盘错）。这解释了 temp×item 21.3%（最高值，因为 temperature 对长推理链的影响在 easy 和 hard items 间有 巨大差异——Level 1 题目一步可解几乎不受 temperature 影响，Level 5 题目 8-10 步每步都可能 在不同 temperature 下走向不同推理路径）。seed×item 14.7% 同理——CUDA nondeterminism 在 长 generation 中逐步累积，其影响与 problem complexity 正相关。 item_id 16.8% 是五个 benchmark 中最低的，因为 MATH items 的 difficulty 分布与 MMLU 不同： 8B 模型在 MATH 上整体准确率只有 25%，大量 items 集中在 p<0.1（几乎不可能做对），这些 items 的 Bernoulli p(1-p) 方差极小，压缩了 item_id 的总贡献。residual 24.5% 反映了 大量未建模的高阶交互（temp×seed×item, prompt×seed×item），这些在短输出的 MC 任务中 可忽略但在长推理链中显著。 precision×temperature 在 binary 下 0.5%（接近 0.8% 上限但仍在范围内），在 text_match 下 2.8%——MATH 的长推理链使浮点非结合性效应最大化。 gradient 扩展到 5 点后仍单调，从 57.1% 降至 16.8%（40.3pp span），且趋势近似线性—— 认知复杂度与 item dominance 之间存在 systematic 的反比关系。这是 \\\"benchmark-conditional variance structure\\\" 论点的最强证据。 G=0.51(binary) 在 MATH 上反而高于 MMLU(0.36)——尽管 counter-intuitive，这是因为 MATH 的低 item 方差意味着 200 items 已足够 \\\"代表\\\" item universe，可靠性瓶颈在 prompt/seed replications 而非 item sampling。D-study 验证了这一点：MATH 仅需 180 items（最少）但 18000 evals（最多），是 MMLU 的 7.1×——\\\"no universal recipe\\\" 的极端案例。\\n\"\n  }\n]",
      "numLines": 43,
      "startLine": 1900,
      "totalLines": 1942
    }
  },
  "sourceToolAssistantUUID": "a9829c88-810c-4483-8f53-45e8aa2bc88e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-21T04:06:08.791Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also read the research and writing skills to inform the paper writing style.

Actually, let me focus on writing the paper now. I have all the experiment data and framing. Let me synthesize it into a complete LaTeX paper.

Key experiments and their data:
1. exp-001: Full-scale MMLU precision study (4 models) - Tables 1-3
2. exp-001b: Item resampling stability test - Table 4
3. exp-002: Multi-benchmark replication (GSM8K, ARC, HellaSwag) - Tables 5-7


4. exp-003: Multi-hardware G-study - Tables 8-9
5. exp-004: Comprehensive analysis (model-as-facet, bootstrap, D-study, IRT) - Tables 10-17
6. exp-005: 14B model scale extension - Table 18
7. exp-006: Fine-tuning G-study (RoBERTa-large) - Tables 19-20
8. exp-007: LayerCast precision mitigation - Table 21
9. exp-008: MATH benchmark — extreme reasoning endpoint - Tables 22-24

The paper should cover the title and synthesize all these experiments into a cohesive narrative.

Now I'm mapping out the full paper structure. I'll start with the abstract and introduction, then move through the methodology section covering generalizability theory foundations and experimental design. The experiments section will walk through each study systematically—starting with the MMLU G-study, then item resampling stability, cross-benchmark variance gradients, and continuing through all the remaining analyses. This ensures every table from the data gets incorporated into the narrative. Writing the LaTeX paper... I need to map all nine experiments to their corresponding sections and tables, making sure each gets proper coverage. Since there are 24 tables total, I'll need to present them efficiently while still including all the data—combining or abbreviating where it makes sense without losing critical information. Now I'm writing the LaTeX document, aiming for clarity and completeness rather than polish, so reviewers can properly evaluate the work. I should stick to standard packages that will compile reliably with pdflatex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e549c7ee-6441-4d8b-9496-8f566b225b98",
  "isSidechain": false,
  "requestId": "req_011CbF42Ps6KCsgLpzZmrCQ7",
  "type": "assistant",
  "uuid": "03ae7d3e-951f-49a6-bc85-5d6d6ba2cce5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxiUiyGGKq322wJhxrcqkS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 61196,
      "output_tokens": 1561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1561,
          "cache_read_input_tokens": 61196,
          "cache_creation_input_tokens": 1761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1761
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

_source line 35 · 2026-05-21T04:06:08.793Z_

I have all the data. Let me check for pdflatex availability, then write the full paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03ae7d3e-951f-49a6-bc85-5d6d6ba2cce5",
  "isSidechain": false,
  "requestId": "req_011CbF42Ps6KCsgLpzZmrCQ7",
  "type": "assistant",
  "uuid": "87a543e2-c89c-4b88-bc29-1ee9eb5a9ba9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxiUiyGGKq322wJhxrcqkS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 61196,
      "output_tokens": 1561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1561,
          "cache_read_input_tokens": 61196,
          "cache_creation_input_tokens": 1761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1761
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

_source line 36 · 2026-05-21T04:06:08.948Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LwzcCvbi2687vhhB6SqXXL`</summary>

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
  "parentUuid": "87a543e2-c89c-4b88-bc29-1ee9eb5a9ba9",
  "isSidechain": false,
  "requestId": "req_011CbF42Ps6KCsgLpzZmrCQ7",
  "type": "assistant",
  "uuid": "fb8bdbef-4a6a-4f78-8ac9-22e6308ea7bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxiUiyGGKq322wJhxrcqkS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 61196,
      "output_tokens": 1561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1561,
          "cache_read_input_tokens": 61196,
          "cache_creation_input_tokens": 1761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1761
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

_source line 37 · 2026-05-21T04:06:08.974Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q4PcyXCqwZZ2K5edvVgSEX`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb8bdbef-4a6a-4f78-8ac9-22e6308ea7bc",
  "isSidechain": false,
  "requestId": "req_011CbF42Ps6KCsgLpzZmrCQ7",
  "type": "assistant",
  "uuid": "f277c66a-e8e1-429e-b645-eb8cafb726cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxiUiyGGKq322wJhxrcqkS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 61196,
      "output_tokens": 1561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1561,
          "cache_read_input_tokens": 61196,
          "cache_creation_input_tokens": 1761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1761
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

_source line 38 · 2026-05-21T04:06:09.098Z_

<details><summary>↩ Tool result · `toolu_01LwzcCvbi2687vhhB6SqXXL`</summary>

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
  "parentUuid": "fb8bdbef-4a6a-4f78-8ac9-22e6308ea7bc",
  "isSidechain": false,
  "promptId": "fcb16a4e-0813-4fa9-ba4a-a5eb615d5c29",
  "type": "user",
  "uuid": "e358f03e-017d-465b-846e-e2a5a82a374c",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)\nkpathsea version 6.4.1\nCopyright 2025 Han The Thanh (pdfTeX) et al.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fb8bdbef-4a6a-4f78-8ac9-22e6308ea7bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T04:06:09.143Z_

<details><summary>↩ Tool result · `toolu_01Q4PcyXCqwZZ2K5edvVgSEX`</summary>

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
  "parentUuid": "f277c66a-e8e1-429e-b645-eb8cafb726cb",
  "isSidechain": false,
  "promptId": "fcb16a4e-0813-4fa9-ba4a-a5eb615d5c29",
  "type": "user",
  "uuid": "8506e042-683f-4a82-b859-92403ed3d727",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f277c66a-e8e1-429e-b645-eb8cafb726cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 40 · 2026-05-21T04:06:09.147Z_

```json
{
  "parentUuid": "8506e042-683f-4a82-b859-92403ed3d727",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3e3b5335-7c9f-4a57-bfe6-700634b8b1b6",
  "timestamp": "2026-05-21T04:06:09.147Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 41 · 2026-05-21T04:06:14.151Z_

<details><summary>Logged reasoning block</summary>

```text
Good, pdflatex is available. Now let me write the full paper. This will be a long document. Let me write it carefully, ensuring all experiments and tables are covered.

I need to write a complete LaTeX paper with:
- All 8 experiments covered with sections/tables
- Data from experiment_data.json faithfully reproduced
- Proper academic structure

Let me write it now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e3b5335-7c9f-4a57-bfe6-700634b8b1b6",
  "isSidechain": false,
  "requestId": "req_011CbF453d1oboAmDDdPGjjK",
  "type": "assistant",
  "uuid": "ed0b9c99-c3aa-4d91-acc3-76923e868f65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvqJuDSwyNdmmTBhHvGk1d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1810,
      "cache_read_input_tokens": 62957,
      "output_tokens": 17083,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17083,
          "cache_read_input_tokens": 62957,
          "cache_creation_input_tokens": 1810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1810
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

_source line 42 · 2026-05-21T04:06:14.651Z_

Writing the full LaTeX paper now. This will be a substantial document covering all 8 experiments with 24 tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed0b9c99-c3aa-4d91-acc3-76923e868f65",
  "isSidechain": false,
  "requestId": "req_011CbF453d1oboAmDDdPGjjK",
  "type": "assistant",
  "uuid": "782abd80-826b-48f9-9e51-81ce72bc7444",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvqJuDSwyNdmmTBhHvGk1d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1810,
      "cache_read_input_tokens": 62957,
      "output_tokens": 17083,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17083,
          "cache_read_input_tokens": 62957,
          "cache_creation_input_tokens": 1810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1810
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

_source line 43 · 2026-05-21T04:11:13.125Z_

<details open><summary>🔧 Tool call — Write · `toolu_01KL4diQhF9HWoR1cQtRQPRG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/paper.tex",
  "content": "\\documentclass[11pt,twocolumn]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[margin=0.75in]{geometry}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{array}\n\\usepackage{xcolor}\n\\usepackage{caption}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{makecell}\n\\usepackage{enumitem}\n\\setlist{nosep}\n\n\\newcolumntype{R}{>{\\raggedleft\\arraybackslash}p{0.55cm}}\n\\newcolumntype{L}{>{\\raggedright\\arraybackslash}p{1.8cm}}\n\n\\title{Reproducibility Budgets for LLM Evaluation:\\\\A Generalizability Theory Analysis of Variance Sources\\\\Across Benchmarks, Models, and Evaluation Metrics}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nWhen LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, numerical precision, temperature, or item selection---let alone how these factors interact.\nWe present the first multi-benchmark Generalizability Theory (G-theory) analysis of LLM evaluation, crossing infrastructure factors (numerical precision, GPU type) with methodology factors (prompt template, random seed, sampling temperature, option ordering) across five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), four 7--9B models, two 14B models, and two evaluation metrics.\nThree findings emerge.\nFirst, item selection is the largest single variance source under binary scoring, but its dominance is \\emph{benchmark-conditional}: it accounts for 57.1\\% of variance on MMLU (knowledge retrieval) but only 16.8\\% on MATH (multi-step reasoning), with a monotonic gradient across all five benchmarks ($r=-0.99$ with cognitive complexity).\nSecond, direct infrastructure$\\times$methodology interactions are negligible under binary scoring ($\\leq$0.6\\% across all benchmarks), providing a confirmatory null result that validates isolated-factor study designs---though this separability breaks down under text-exact-match scoring (up to 2.8\\% on MATH).\nThird, reproducibility budgets are fundamentally benchmark- and metric-conditional: achieving $G\\geq0.90$ reliability requires 2{,}520 evaluations on MMLU but 18{,}000 on MATH under binary scoring, a 7.1$\\times$ difference that renders any ``universal reproducibility recipe'' illusory.\nWe further show that item-count recommendations from IRT-based approaches (e.g., tinyBenchmarks) are 2.8--4.2$\\times$ smaller than G-theory recommendations because they do not account for prompt, seed, and ordering facets.\nA fine-tuning G-study on RoBERTa reveals a qualitatively different variance hierarchy where training seed (23.5\\%) rivals item selection (23.8\\%), demonstrating that reproducibility budgets must be regime-specific.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nThe reproducibility of LLM evaluation is a growing concern.\nStudies report accuracy differences of up to 9 percentage points from numerical precision alone \\citep{yuan2025}, prompt sensitivity explaining 50\\% of observed variance \\citep{brittlebench2026}, and seed-driven fluctuations that reverse model rankings \\citep{biderman2024}.\nYet each study isolates at most two variance sources, implicitly assuming that factors not studied are separable from those that are.\nNo work has tested this assumption in a unified factorial design.\n\nThis gap matters practically.\nA benchmark maintainer deciding whether to standardize prompts, fix seeds, or mandate specific GPU hardware needs to know not just which factor matters most, but whether the answer depends on the benchmark, the evaluation metric, or the model.\nWithout this knowledge, any reproducibility guideline risks being either overly conservative (standardizing factors that contribute negligibly) or dangerously incomplete (ignoring interactions that inflate variance on specific task types).\n\nWe address this gap through Generalizability Theory (G-theory) \\citep{shavelson1991,brennan2001}, a psychometric framework that decomposes observed score variance into contributions from multiple facets simultaneously.\nUnlike ANOVA-based approaches \\citep{bouthillier2021}, G-theory yields Decision studies (D-studies) that project reliability under hypothetical measurement designs, enabling actionable resource allocation.\nUnlike IRT-based subsampling \\citep{polo2024,lalor2019}, G-theory accounts for prompt, seed, and ordering facets alongside items.\n\nOur analysis crosses infrastructure factors (numerical precision across GPU architectures) with methodology factors (prompt template, random seed, sampling temperature, option ordering) across five benchmarks, six models spanning 7B--14B parameters, and three evaluation metrics (binary, text-exact-match, log-probability).\nWe report three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Cross-benchmark variance gradient.} The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval, 57.1\\%) to interaction-dominated (math reasoning, 16.8\\% item, 49.5\\% interactions), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.\n\n\\item \\textbf{Confirmatory separability test.} Infrastructure$\\times$methodology interactions are negligible at the aggregate level ($\\leq$0.6\\% under binary scoring across all benchmarks and GPU types), validating isolated-factor study designs---with the caveat that separability is metric-conditional.\n\n\\item \\textbf{Task-specific reproducibility budgets.} D-study projections with bootstrap confidence intervals yield benchmark-specific, metric-conditional item/prompt/seed allocations for $G\\geq0.90$, contextualized against IRT-based recommendations.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Variance decomposition in ML evaluation.}\n\\citet{bouthillier2021} decomposed ML benchmark variance across hyperparameters, data splits, and random seeds via ANOVA, establishing the template for factorial variance decomposition.\n\\citet{henderson2018} documented high variance in deep RL evaluation.\n\\citet{dodge2020} and \\citet{sellam2022} quantified fine-tuning instability from seed and data order.\n\\citet{dehghani2021} showed that benchmark selection itself introduces systematic bias (the ``Benchmark Lottery'').\nOur work extends this tradition to LLM inference evaluation with a G-theory framework that supports D-study projections.\n\n\\paragraph{LLM evaluation sensitivity.}\n\\citet{yuan2025} documented up to 9\\% accuracy variation from hardware and numerical precision without factorial attribution.\n\\citet{brittlebench2026} quantified prompt sensitivity at 50\\% variance on fixed hardware.\n\\citet{mesting2026} adapted G-theory to five methodological facets in LLM evaluation but treated infrastructure as fixed and studied a single benchmark.\n\\citet{lu2022} and \\citet{pezeshkpour2024} documented option ordering effects.\n\\citet{hua2025} showed that log-likelihood scoring inflates apparent prompt sensitivity.\nWe unify infrastructure and methodology in a crossed factorial design across multiple benchmarks.\n\n\\paragraph{Item-level analysis and efficient evaluation.}\nIRT-based approaches \\citep{lalor2019,rodriguez2021,vania2021} analyze item-level properties for NLP evaluation.\n\\citet{polo2024} (tinyBenchmarks) used IRT for efficient subsampling, recommending $\\sim$100 items per benchmark.\n\\citet{perlitz2023} proposed efficient benchmarking via item selection.\nWe compare G-theory D-study recommendations against IRT baselines, showing a 2.8--4.2$\\times$ discrepancy explained by multi-facet accounting.\n\n\\paragraph{Generalizability Theory.}\nG-theory \\citep{cronbach1972,shavelson1991,brennan2001} extends classical test theory by decomposing variance across multiple random facets simultaneously.\nIt distinguishes G-studies (variance decomposition) from D-studies (reliability projection under alternative designs).\nG-theory has been applied extensively in educational testing and health measurement but only recently to ML evaluation \\citep{mesting2026}.\n\n% ============================================================\n\\section{Method}\n\n\\subsection{Generalizability Theory Background}\n\nIn G-theory, an observed score $X_{pijk\\ldots}$ for object of measurement $p$ (here, a model's response to an item) across facets $i,j,k,\\ldots$ is decomposed as:\n\\begin{equation}\nX_{pijk\\ldots} = \\mu + \\alpha_p + \\beta_i + \\gamma_j + (\\alpha\\beta)_{pi} + \\cdots + \\epsilon\n\\end{equation}\nwhere each term represents a variance component.\nThe G-coefficient quantifies reliability:\n\\begin{equation}\nG = \\frac{\\sigma^2_p}{\\sigma^2_p + \\sigma^2_{\\text{relative error}}}\n\\end{equation}\nwhere $\\sigma^2_{\\text{relative error}}$ is the sum of all variance components involving the object of measurement divided by their respective sample sizes.\n\nA D-study projects $G$ under hypothetical designs by varying facet sample sizes $n_i, n_j, \\ldots$, enabling optimal resource allocation.\nWe estimate variance components using Henderson's Method III \\citep{brennan2001} with REML as a robustness check.\n\n\\subsection{Experimental Design}\n\n\\paragraph{Facets.}\nWe cross the following facets:\n\\begin{itemize}\n\\item \\textbf{Item} ($n_i$=200 per benchmark): Stratified random sample from each benchmark's item pool.\n\\item \\textbf{Prompt template} ($n_p$=6): Diverse prompt formats (zero-shot, few-shot, instruction variants).\n\\item \\textbf{Random seed} ($n_s$=6): CUDA-level nondeterminism seeds.\n\\item \\textbf{Temperature} ($n_t$=2--3): $T \\in \\{0.0, 0.3, 0.7\\}$ (full design) or $\\{0.0, 0.7\\}$ (reduced).\n\\item \\textbf{Option ordering} ($n_o$=4): Systematic rotations of MC answer options.\n\\item \\textbf{Numerical precision}: bf16, fp16, fp32 (full); bf16, fp16 (reduced). Gemma-2 uses bf16+fp32 only due to fp16 numerical instability.\n\\item \\textbf{GPU type} (exp-003): RTX PRO 6000 vs.\\ A100-80GB.\n\\end{itemize}\n\n\\paragraph{Models.}\nPrimary: Llama-3.1-8B, Qwen3-8B, Mistral-7B, Gemma-2-9B (7--9B parameter range).\nScale extension: Qwen3-14B, DeepSeek-R1-Distill-14B.\nFine-tuning: RoBERTa-large.\n\n\\paragraph{Benchmarks.}\nMMLU (knowledge retrieval), ARC-Challenge (science reasoning), HellaSwag (commonsense), GSM8K (math reasoning), MATH (advanced math reasoning).\n\n\\paragraph{Evaluation metrics.}\nBinary correct/incorrect, text-exact-match on generated output, log-probability of correct answer.\n\n\\paragraph{Infrastructure.}\nAll inference uses vLLM 0.9.2 with V0 enforce\\_eager mode across all precision conditions to eliminate the float32 engine confound (where fp32 triggers slower eager-mode attention, degrading accuracy by $\\sim$8--9pp irrespective of precision effects).\n\n\\paragraph{Design variants.}\nMMLU uses the full $3 \\times 3$ precision$\\times$temperature design (exp-001); other benchmarks use a reduced $2 \\times 2$ design (exp-002) due to GPU budget constraints.\nWe verify robustness to this asymmetry by re-analyzing MMLU under a matched $2 \\times 2$ design ($\\Delta$item\\_id = 0.7pp).\n\n% ============================================================\n\\section{Experiments and Results}\n\nWe report eight experiments spanning 3.4M+ evaluation records.\n\n% ---- exp-001 ----\n\\subsection{MMLU G-Study (Exp-001)}\n\\label{sec:exp001}\n\nFour models $\\times$ 3 precisions (Gemma: bf16+fp32) $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings $\\times$ 200 items = 950{,}400 total records.\n\n\\paragraph{Accuracy.}\nOverall accuracy is 0.668. bf16 and fp16 produce near-identical results ($\\Delta < 0.2$pp across all models), while fp32 under V0 enforce\\_eager shows a consistent $\\sim$8.9pp degradation (Table~\\ref{tab:accuracy}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Accuracy by model, precision, and temperature (MMLU).}\n\\label{tab:accuracy}\n\\small\n\\begin{tabular}{llRRR}\n\\toprule\nModel & Prec. & \\footnotesize{T=0} & \\footnotesize{T=.3} & \\footnotesize{T=.7} \\\\\n\\midrule\n\\multirow{3}{*}{\\makecell[l]{Llama\\\\3.1-8B}} & bf16 & .729 & .709 & .695 \\\\\n & fp16 & .730 & .709 & .695 \\\\\n & fp32 & .625 & .601 & .587 \\\\\n\\midrule\n\\multirow{3}{*}{\\makecell[l]{Qwen\\\\3-8B}} & bf16 & .742 & .721 & .706 \\\\\n & fp16 & .741 & .720 & .705 \\\\\n & fp32 & .643 & .618 & .602 \\\\\n\\midrule\n\\multirow{3}{*}{\\makecell[l]{Mistral\\\\7B}} & bf16 & .668 & .645 & .631 \\\\\n & fp16 & .669 & .646 & .632 \\\\\n & fp32 & .578 & .555 & .541 \\\\\n\\midrule\n\\multirow{2}{*}{\\makecell[l]{Gemma\\\\2-9B}} & bf16 & .718 & .696 & .681 \\\\\n & fp32 & .622 & .598 & .583 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Variance decomposition---binary scoring.}\nItem selection dominates variance at 57.1\\% (range 55.8--59.1\\% across models), with remarkably low cross-model variability (SD = 1.4pp).\nAll direct infrastructure$\\times$methodology interactions sum to $\\leq$0.3\\% (Table~\\ref{tab:var_binary}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-model variance decomposition, binary scoring (\\%).}\n\\label{tab:var_binary}\n\\small\n\\begin{tabular}{lRRRRR}\n\\toprule\nComponent & \\rotatebox{60}{\\footnotesize Llama} & \\rotatebox{60}{\\footnotesize Qwen} & \\rotatebox{60}{\\footnotesize Mistr.} & \\rotatebox{60}{\\footnotesize Gem.} & \\rotatebox{60}{\\footnotesize Avg} \\\\\n\\midrule\nitem\\_id & 57.2 & 55.8 & 59.1 & 56.4 & 57.1 \\\\\nresidual & 17.6 & 18.2 & 16.3 & 17.8 & 17.5 \\\\\nprec:item & 7.1 & 7.3 & 6.5 & 7.2 & 7.0 \\\\\ntemp:item & 6.9 & 6.5 & 7.2 & 6.6 & 6.8 \\\\\nprompt:item & 5.4 & 5.8 & 5.2 & 5.6 & 5.5 \\\\\nseed:item & 2.0 & 2.3 & 1.9 & 2.1 & 2.1 \\\\\norder:item & 1.5 & 1.4 & 1.6 & 1.4 & 1.5 \\\\\nprecision & 1.1 & 1.3 & 1.2 & 1.1 & 1.2 \\\\\ntemperature & 0.5 & 0.4 & 0.5 & 0.6 & 0.5 \\\\\nprompt & 0.3 & 0.4 & 0.2 & 0.3 & 0.3 \\\\\nprec:temp & 0.2 & 0.3 & 0.1 & 0.2 & 0.2 \\\\\nother & 0.2 & 0.3 & 0.2 & 0.7 & 0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Variance decomposition---text-exact-match.}\nUnder text-exact-match scoring, the variance hierarchy inverts: residual (38.0\\%) and prompt:item (36.2\\%) dominate, while item\\_id drops to 2.0\\%.\nTemperature becomes a major main effect (16.5\\%), and precision$\\times$temperature rises to 1.1\\% (Table~\\ref{tab:var_text}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance decomposition, text-exact-match scoring (\\%).}\n\\label{tab:var_text}\n\\small\n\\begin{tabular}{lRRRRR}\n\\toprule\nComponent & \\rotatebox{60}{\\footnotesize Llama} & \\rotatebox{60}{\\footnotesize Qwen} & \\rotatebox{60}{\\footnotesize Mistr.} & \\rotatebox{60}{\\footnotesize Gem.} & \\rotatebox{60}{\\footnotesize Avg} \\\\\n\\midrule\nresidual & 38.5 & 37.2 & 39.1 & 37.3 & 38.0 \\\\\nprompt:item & 35.8 & 37.0 & 35.5 & 36.4 & 36.2 \\\\\ntemperature & 16.8 & 16.0 & 16.5 & 16.7 & 16.5 \\\\\ntemp:item & 3.5 & 4.2 & 3.6 & 3.8 & 3.8 \\\\\nitem\\_id & 1.8 & 2.3 & 1.9 & 2.1 & 2.0 \\\\\nprec:temp & 1.2 & 1.0 & 1.1 & 1.0 & 1.1 \\\\\nprec:item & 1.2 & 1.1 & 1.3 & 1.2 & 1.2 \\\\\nother & 1.2 & 1.2 & 1.0 & 1.5 & 1.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{G-coefficients.}\n$G_{\\text{binary}} = 0.36$ for 200 items (item dominance makes $G \\geq 0.90$ unreachable without expansion), while $G_{\\text{text}} = 0.96$ (already adequate).\n\n% ---- exp-001b ----\n\\subsection{Item Resampling Stability (Exp-001b)}\n\\label{sec:exp001b}\n\nTo verify that item dominance is not an artifact of our specific 200-item draw, we conduct three independent stratified samples (seeds 0, 7, 99) with zero item overlap.\nEach sample uses Llama-3.1-8B $\\times$ 3 precisions $\\times$ 3 prompts $\\times$ 3 seeds $\\times$ 2 orderings = 10{,}800 records.\n\nItem\\_id\\% ranges from 55.8\\% to 58.6\\% (SD = 1.4pp), well within expected sampling variability and far above any threshold for dominance (Table~\\ref{tab:stability}).\nG-coefficients are similarly stable (0.34--0.37, range = 0.03).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-sample variance decomposition stability (\\%).}\n\\label{tab:stability}\n\\small\n\\begin{tabular}{lRRRRR}\n\\toprule\nComponent & \\footnotesize{S0} & \\footnotesize{S7} & \\footnotesize{S99} & \\footnotesize{Mean} & \\footnotesize{SD} \\\\\n\\midrule\nitem\\_id & 57.5 & 55.8 & 58.6 & 57.3 & 1.4 \\\\\nresidual & 17.2 & 18.5 & 16.8 & 17.5 & 0.9 \\\\\nprec:item & 7.1 & 7.5 & 6.5 & 7.0 & 0.5 \\\\\ntemp:item & 6.5 & 7.2 & 6.8 & 6.8 & 0.4 \\\\\nprompt:item & 5.8 & 5.0 & 5.6 & 5.5 & 0.4 \\\\\nseed:item & 2.2 & 1.8 & 2.1 & 2.0 & 0.2 \\\\\norder:item & 1.4 & 1.7 & 1.3 & 1.5 & 0.2 \\\\\nprecision & 1.2 & 1.1 & 1.3 & 1.2 & 0.1 \\\\\nother & 1.1 & 1.4 & 1.0 & 1.2 & 0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---- exp-002 + exp-008 ----\n\\subsection{Cross-Benchmark Variance Gradient (Exp-002, Exp-008)}\n\\label{sec:gradient}\n\nWe extend the analysis to four additional benchmarks: ARC-Challenge, HellaSwag, GSM8K (Exp-002: 4 models $\\times$ reduced $2 \\times 2$ design $\\times$ 200 items each, 1{,}209{,}600 records), and MATH (Exp-008: same design, 403{,}200 records).\n\n\\paragraph{The gradient.}\nItem\\_id\\% decreases monotonically from MMLU (57.1\\%) to MATH (16.8\\%) as cognitive complexity increases, while methodology$\\times$item interactions increase correspondingly from 22.9\\% to 49.5\\% (Table~\\ref{tab:gradient}).\nThe gradient spans 40.3pp across five benchmarks and is perfectly monotonic.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark variance gradient, binary scoring (\\%).}\n\\label{tab:gradient}\n\\small\n\\begin{tabular}{lRRRRR}\n\\toprule\nComponent & \\rotatebox{60}{\\footnotesize MMLU} & \\rotatebox{60}{\\footnotesize ARC} & \\rotatebox{60}{\\footnotesize HSwag} & \\rotatebox{60}{\\footnotesize GSM} & \\rotatebox{60}{\\footnotesize MATH} \\\\\n\\midrule\nitem\\_id & 57.1 & 43.7 & 38.2 & 22.4 & 16.8 \\\\\nresidual & 17.5 & 20.3 & 22.5 & 24.8 & 24.5 \\\\\ntemp:item & 6.8 & 9.8 & 12.3 & 18.5 & 21.3 \\\\\nprompt:item & 5.5 & 8.5 & 9.8 & 10.2 & 8.8 \\\\\nseed:item & 2.1 & 4.5 & 6.5 & 12.3 & 14.7 \\\\\nprec:item & 7.0 & 6.2 & 4.8 & 3.2 & 2.5 \\\\\norder:item & 1.5 & 2.8 & 2.4 & 2.1 & 2.2 \\\\\nprecision & 1.2 & 1.2 & 0.8 & 0.8 & 0.6 \\\\\ntemperature & 0.5 & 1.5 & 1.5 & 4.5 & 5.8 \\\\\nprec:temp & 0.2 & 0.3 & 0.4 & 0.6 & 0.5 \\\\\nother & 0.6 & 1.2 & 0.8 & 0.6 & 2.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gradient summary.}\nTable~\\ref{tab:gradient_summary} shows the gradient alongside G-coefficients.\nCounter-intuitively, G increases from MMLU (0.36) to MATH (0.51): extreme item dominance on MMLU means 200 items are insufficient to stabilize estimates, while MATH's lower item variance makes the same count more representative (though more prompt/seed replications are needed).\n\n\\begin{table}[t]\n\\centering\n\\caption{Five-benchmark gradient summary.}\n\\label{tab:gradient_summary}\n\\small\n\\begin{tabular}{llcRRR}\n\\toprule\nBench. & Task & CC & \\footnotesize{item\\%} & \\footnotesize{$\\Sigma$int\\%} & \\footnotesize{$G_{200}$} \\\\\n\\midrule\nMMLU & knowledge & 1 & 57.1 & 22.9 & .36 \\\\\nARC & science & 2 & 43.7 & 31.8 & .42 \\\\\nHSwag & common. & 3 & 38.2 & 35.8 & .44 \\\\\nGSM8K & math & 4 & 22.4 & 46.3 & .48 \\\\\nMATH & math (hard) & 5 & 16.8 & 49.5 & .51 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2mm}\n\\begin{flushleft}\n\\footnotesize CC = cognitive complexity rank. $\\Sigma$int = sum of method$\\times$item interactions. $G_{200}$ = G-coefficient with 200 items, binary scoring.\n\\end{flushleft}\n\\end{table}\n\n\\paragraph{Separability across benchmarks.}\nDirect infrastructure$\\times$methodology interactions remain $\\leq$0.6\\% under binary scoring across all five benchmarks (Table~\\ref{tab:separability}).\nUnder text-exact-match, GSM8K reaches 2.5\\% and MATH reaches 2.8\\%, consistent with floating-point non-associativity accumulating through long generation chains.\n\n\\begin{table}[t]\n\\centering\n\\caption{Direct infra$\\times$method interactions (\\%).}\n\\label{tab:separability}\n\\small\n\\begin{tabular}{llRRR}\n\\toprule\nBenchmark & Metric & \\footnotesize{p$\\times$t} & \\footnotesize{p$\\times$pr} & \\footnotesize{max} \\\\\n\\midrule\nMMLU & binary & 0.2 & 0.1 & 0.2 \\\\\nARC & binary & 0.3 & 0.1 & 0.3 \\\\\nHellaSwag & binary & 0.4 & 0.1 & 0.4 \\\\\nGSM8K & binary & 0.6 & 0.2 & 0.6 \\\\\nMATH & binary & 0.5 & --- & 0.5 \\\\\n\\midrule\nMMLU & text & 1.1 & 0.3 & 1.1 \\\\\nGSM8K & text & 2.5 & 0.8 & 2.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2mm}\n\\begin{flushleft}\n\\footnotesize p$\\times$t = precision$\\times$temperature; p$\\times$pr = precision$\\times$prompt.\n\\end{flushleft}\n\\end{table}\n\n\\paragraph{Within-benchmark gradient (MATH).}\nMATH difficulty levels reveal the gradient operates \\emph{within} a benchmark: Level~1 items resemble MMLU (item\\_id = 28.5\\%), while Level~5 items show extreme interaction dominance (temp:item = 30.1\\%, seed:item = 22.0\\%, item\\_id = 8.2\\%; Table~\\ref{tab:math_levels}).\n\n\\begin{table}[t]\n\\centering\n\\caption{MATH variance by difficulty level (\\%, Qwen3-8B, binary).}\n\\label{tab:math_levels}\n\\small\n\\begin{tabular}{lRRRRR}\n\\toprule\nComponent & \\footnotesize{L1} & \\footnotesize{L2} & \\footnotesize{L3} & \\footnotesize{L4} & \\footnotesize{L5} \\\\\n\\midrule\nitem\\_id & 28.5 & 22.1 & 16.5 & 12.8 & 8.2 \\\\\ntemp:item & 8.5 & 14.2 & 22.5 & 26.8 & 30.1 \\\\\nseed:item & 5.2 & 10.8 & 15.2 & 18.5 & 22.0 \\\\\nresidual & 32.5 & 28.2 & 23.5 & 21.2 & 18.8 \\\\\nother & 25.3 & 24.7 & 22.3 & 20.7 & 20.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---- exp-003 ----\n\\subsection{Multi-Hardware Separability (Exp-003)}\n\\label{sec:hardware}\n\nWe extend the infrastructure facet beyond precision by crossing two GPU architectures (RTX PRO 6000 96GB vs.\\ A100-80GB): 4 models $\\times$ 2 GPUs $\\times$ 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings $\\times$ 200 items = 1{,}382{,}400 records.\n\nGPU type contributes 0.3\\% as a main effect, and all direct GPU$\\times$methodology interactions are negligible under binary scoring (total = 0.5\\%, all CIs contain zero; Table~\\ref{tab:gpu_sep}).\nThe gpu:item interaction (1.8\\%) indicates hardware effects are item-conditional---items near the decision boundary are sensitive to microarchitecture-level floating-point differences, but these cancel at the aggregate level.\n\n\\begin{table}[t]\n\\centering\n\\caption{GPU type separability: direct GPU$\\times$method interactions.}\n\\label{tab:gpu_sep}\n\\small\n\\begin{tabular}{lRRc}\n\\toprule\nInteraction & \\footnotesize{bin\\%} & \\footnotesize{text\\%} & \\footnotesize{CI$\\ni$0?} \\\\\n\\midrule\ngpu$\\times$precision & 0.2 & 0.8 & yes \\\\\ngpu$\\times$temperature & 0.1 & 0.4 & yes \\\\\ngpu$\\times$prompt & 0.1 & 0.2 & yes \\\\\ngpu$\\times$seed & 0.1 & 0.1 & yes \\\\\ngpu$\\times$ordering & 0.0 & 0.0 & yes \\\\\n\\midrule\ntotal direct & 0.5 & 1.5 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith GPU type as an additional facet, item\\_id remains the largest component at 55.2\\% [52.8, 57.6] and the overall variance structure is preserved (Table~\\ref{tab:gpu_full}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance decomposition with GPU facet (MMLU, binary).}\n\\label{tab:gpu_full}\n\\small\n\\begin{tabular}{lRl}\n\\toprule\nComponent & \\% & 95\\% CI \\\\\n\\midrule\nitem\\_id & 55.2 & [52.8, 57.6] \\\\\nresidual & 15.8 & [13.5, 18.1] \\\\\nprec:item & 6.8 & [5.5, 8.1] \\\\\ntemp:item & 6.5 & [5.2, 7.8] \\\\\nprompt:item & 5.3 & [4.1, 6.5] \\\\\nseed:item & 2.0 & [1.3, 2.7] \\\\\ngpu:item & 1.8 & [1.0, 2.6] \\\\\norder:item & 1.4 & [0.8, 2.0] \\\\\nprecision & 1.1 & [0.5, 1.7] \\\\\ngpu:prec:item & 0.5 & [0.2, 0.8] \\\\\ngpu\\_type & 0.3 & [0.0, 0.6] \\\\\nother & 3.3 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---- exp-004 ----\n\\subsection{Model-as-Facet Reanalysis (Exp-004)}\n\\label{sec:model_facet}\n\nTreating model as a crossed random facet (rather than analyzing per-model) properly attributes model$\\times$item interaction, which was previously confounded with item\\_id and residual.\n\nItem\\_id decreases from 57.1\\% to 47.3\\%, with 12.1\\% reassigned to model$\\times$item (Table~\\ref{tab:maf}).\nThe cross-benchmark gradient remains monotonic under model-as-facet analysis (Table~\\ref{tab:maf_gradient}), spanning 29.1pp from MMLU (47.3\\%) to GSM8K (18.2\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{Model-as-facet reanalysis (MMLU, binary, \\%).}\n\\label{tab:maf}\n\\small\n\\begin{tabular}{lRRr}\n\\toprule\nComponent & \\footnotesize{1-model} & \\footnotesize{MAF} & $\\Delta$ \\\\\n\\midrule\nitem\\_id & 57.1 & 47.3 & $-$9.8 \\\\\nmodel$\\times$item & --- & 12.1 & +12.1 \\\\\nmodel & --- & 3.8 & +3.8 \\\\\nresidual & 17.5 & 12.8 & $-$4.7 \\\\\nprec:item & 7.0 & 6.5 & $-$0.5 \\\\\ntemp:item & 6.8 & 6.2 & $-$0.6 \\\\\nprompt:item & 5.5 & 5.0 & $-$0.5 \\\\\nmodel$\\times$prec & --- & 0.5 & +0.5 \\\\\nmodel$\\times$temp & --- & 0.3 & +0.3 \\\\\nother & 6.1 & 5.5 & $-$0.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Model-as-facet cross-benchmark gradient.}\n\\label{tab:maf_gradient}\n\\small\n\\begin{tabular}{lRRR}\n\\toprule\nBenchmark & \\footnotesize{item\\%} & \\footnotesize{m$\\times$i\\%} & \\footnotesize{$\\Delta$MMLU} \\\\\n\\midrule\nMMLU & 47.3 & 12.1 & 0.0 \\\\\nARC & 36.5 & 9.5 & $-$10.8 \\\\\nHellaSwag & 31.4 & 8.8 & $-$15.9 \\\\\nGSM8K & 18.2 & 6.2 & $-$29.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Bootstrap Confidence Intervals and Sensitivity (Exp-004)}\n\\label{sec:bootstrap}\n\nWe compute 1{,}000-resample bootstrap CIs on all variance components (Table~\\ref{tab:bootstrap}).\nItem\\_id's lower bound (44.9\\%) is well-separated from the next-largest component, confirming its dominance is statistically robust.\nPrecision$\\times$temperature under binary scoring has a CI containing zero [0.0, 0.6], confirming non-significance; under text-exact-match, the CI excludes zero, confirming metric-conditional separability.\n\n\\begin{table}[t]\n\\centering\n\\caption{Bootstrap CIs, MMLU model-as-facet (\\%).}\n\\label{tab:bootstrap}\n\\small\n\\begin{tabular}{lRRRR}\n\\toprule\nComponent & Est. & Lo & Hi & Wid. \\\\\n\\midrule\nitem\\_id & 47.3 & 44.9 & 49.7 & 4.8 \\\\\nmodel$\\times$item & 12.1 & 10.4 & 13.9 & 3.5 \\\\\nresidual & 12.8 & 10.8 & 14.8 & 4.0 \\\\\nprec:item & 6.5 & 5.2 & 7.8 & 2.6 \\\\\ntemp:item & 6.2 & 4.9 & 7.5 & 2.6 \\\\\nprompt:item & 5.0 & 3.8 & 6.2 & 2.4 \\\\\nmodel & 3.8 & 1.5 & 6.1 & 4.6 \\\\\nprec:temp (bin) & 0.2 & 0.0 & 0.6 & 0.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMultiple sensitivity analyses confirm robustness (Table~\\ref{tab:sensitivity}): REML vs.\\ Henderson ($\\Delta < 2$pp), fixed vs.\\ random treatment of temperature/ordering ($\\Delta < 3$pp), design asymmetry (3$\\times$3 vs.\\ matched 2$\\times$2: $\\Delta = 0.7$pp), and bootstrap vs.\\ jackknife CIs (width ratio = 0.92, within 20\\% threshold).\n\nBernoulli mechanical variance accounts for 35\\% of observed item\\_id (correlation $r = 0.82$ between $p_i(1-p_i)$ and observed item variance), but the corrected ``informative'' item\\_id remains 30.7\\%---still the largest single component.\n\n\\begin{table}[t]\n\\centering\n\\caption{Sensitivity analyses summary.}\n\\label{tab:sensitivity}\n\\small\n\\begin{tabular}{lR}\n\\toprule\nAnalysis & max $\\Delta$pp \\\\\n\\midrule\nREML vs Henderson & 1.8 \\\\\nFixed vs random facets & 2.8 \\\\\n3$\\times$3 vs matched 2$\\times$2 & 0.7 \\\\\nBootstrap vs jackknife CI ratio & 0.92 \\\\\nBernoulli-corrected item\\_id & 30.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---- D-study ----\n\\subsection{D-Study Projections (Exp-004)}\n\\label{sec:dstudy}\n\nD-study projections reveal starkly different optimal allocations for achieving $G \\geq 0.90$ across benchmarks (Table~\\ref{tab:dstudy_binary}).\nMMLU requires 420 items but only 6 evaluations per item (2{,}520 total), reflecting item dominance.\nMATH requires only 180 items but 100 evaluations per item (18{,}000 total), reflecting interaction dominance.\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study allocations for $G \\geq 0.90$, binary scoring.}\n\\label{tab:dstudy_binary}\n\\small\n\\begin{tabular}{lRRRRRRR}\n\\toprule\nBench. & \\footnotesize{It.} & \\footnotesize{Pr.} & \\footnotesize{Se.} & \\footnotesize{Te.} & \\footnotesize{Or.} & \\footnotesize{Total} & \\footnotesize{GPU-h} \\\\\n\\midrule\nMMLU & 420 & 3 & 2 & 1 & 1 & 2520 & 8.4 \\\\\nARC & 320 & 3 & 3 & 1 & 1 & 2880 & 9.6 \\\\\nHSwag & 290 & 3 & 3 & 1 & 2 & 5220 & 17.4 \\\\\nGSM8K & 220 & 4 & 4 & 2 & 2 & 14080 & 28.2 \\\\\nMATH & 180 & 5 & 5 & 2 & 2 & 18000 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder text-exact-match scoring, budgets are 5--15$\\times$ smaller because item dominance is much weaker (Table~\\ref{tab:dstudy_text}).\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study allocations for $G \\geq 0.90$, text-exact-match.}\n\\label{tab:dstudy_text}\n\\small\n\\begin{tabular}{lRRRRRR}\n\\toprule\nBench. & \\footnotesize{It.} & \\footnotesize{Pr.} & \\footnotesize{Se.} & \\footnotesize{Te.} & \\footnotesize{Or.} & \\footnotesize{Total} \\\\\n\\midrule\nMMLU & 85 & 2 & 1 & 1 & 1 & 170 \\\\\nARC & 110 & 2 & 1 & 1 & 1 & 220 \\\\\nHSwag & 95 & 2 & 2 & 1 & 1 & 380 \\\\\nGSM8K & 150 & 3 & 2 & 1 & 1 & 900 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{IRT comparison.}\nIRT-based approaches (tinyBenchmarks) recommend 2.8--4.2$\\times$ fewer items than G-theory under binary scoring (Table~\\ref{tab:irt}), because IRT optimizes item selection under a single evaluation condition, ignoring prompt/seed/ordering facets.\nThis 4$\\times$ gap is the ``cost of multi-facet reliability.''\nUnder text-exact-match, the gap narrows or inverts because item variance is no longer dominant.\n\n\\begin{table}[t]\n\\centering\n\\caption{IRT vs G-theory item recommendations.}\n\\label{tab:irt}\n\\small\n\\begin{tabular}{lRRRRR}\n\\toprule\nBench. & \\footnotesize{IRT} & \\footnotesize{G-bin} & \\footnotesize{ratio} & \\footnotesize{G-text} & \\footnotesize{t-ratio} \\\\\n\\midrule\nMMLU & 100 & 420 & 4.2 & 85 & 0.85 \\\\\nARC & 75 & 320 & 4.3 & 110 & 1.47 \\\\\nGSM8K & 80 & 220 & 2.8 & 150 & 1.88 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Logprob Scoring Analysis (Exp-004)}\n\\label{sec:logprob}\n\nLog-probability scoring preserves item dominance more strongly than binary scoring across all benchmarks (Table~\\ref{tab:logprob}), with item\\_id ranging from 31.2\\% (GSM8K) to 52.3\\% (MMLU).\nThe gradient remains monotonic.\nThe logprob G-coefficient for MMLU (0.68 at 200 items) is substantially higher than binary (0.36), reflecting the richer information content of continuous scores.\nProjecting to full MMLU (14K items) yields $G = 0.94$ (binary) and $G = 0.998$ (text).\n\n\\begin{table}[t]\n\\centering\n\\caption{Item\\_id\\% across scoring metrics and benchmarks.}\n\\label{tab:logprob}\n\\small\n\\begin{tabular}{lRRR}\n\\toprule\nBenchmark & binary & text & logprob \\\\\n\\midrule\nMMLU & 47.3 & 2.0 & 52.3 \\\\\nARC & 36.5 & 1.8 & 48.1 \\\\\nHellaSwag & 31.4 & 1.5 & 44.5 \\\\\nGSM8K & 18.2 & 8.0 & 31.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---- exp-005 ----\n\\subsection{Scale Extension to 14B Models (Exp-005)}\n\\label{sec:scale}\n\nQwen3-14B and DeepSeek-R1-Distill-14B on a reduced MMLU design (bf16/fp16 $\\times$ 3 prompts $\\times$ 3 seeds $\\times$ 2 temperatures $\\times$ 2 orderings $\\times$ 200 items = 28{,}800 records).\n\nThe variance hierarchy is preserved at 14B scale, with item\\_id averaging 53.0\\%---a modest 4.1pp decrease from 8B models (Table~\\ref{tab:scale}).\nDeepSeek-R1-Distill shows elevated temp:item (9.2\\%) and seed:item (4.1\\%) interactions, consistent with its chain-of-thought reasoning architecture introducing additional sampling stochasticity.\n\n\\begin{table}[t]\n\\centering\n\\caption{8B vs 14B variance decomposition (MMLU, binary, \\%).}\n\\label{tab:scale}\n\\small\n\\begin{tabular}{lRRRR}\n\\toprule\nComponent & \\footnotesize{8B} & \\footnotesize{Q14B} & \\footnotesize{DS14B} & \\footnotesize{14B avg} \\\\\n\\midrule\nitem\\_id & 57.1 & 54.2 & 51.8 & 53.0 \\\\\nresidual & 17.5 & 16.2 & 14.8 & 15.5 \\\\\ntemp:item & 6.8 & 6.5 & 9.2 & 7.8 \\\\\nprompt:item & 5.5 & 6.5 & 5.8 & 6.2 \\\\\nprec:item & 7.0 & 5.4 & 4.8 & 5.1 \\\\\nseed:item & 2.1 & 2.5 & 4.1 & 3.3 \\\\\nother & 4.0 & 8.7 & 9.5 & 9.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---- exp-006 ----\n\\subsection{Fine-Tuning G-Study (Exp-006)}\n\\label{sec:finetune}\n\nTo test whether variance structure differs between inference and fine-tuning, we conduct a fully crossed G-study: RoBERTa-large fine-tuned on SST-2, MNLI, RTE, and COPA with 6 seeds $\\times$ 3 learning rates $\\times$ 4 data shuffles $\\times$ 3 GPUs $\\times$ 2 precisions = 432 runs per task (1{,}728 total, 96.5\\% converged).\n\nThe variance hierarchy is qualitatively different (Table~\\ref{tab:finetune}): training seed (23.5\\%) rivals item\\_id (23.8\\%) as the largest component, with learning rate (14.2\\%) and data shuffle (9.3\\%) as additional major sources.\nInfrastructure factors remain negligible (GPU: 1.5\\%, precision: 0.8\\%), extending the separability finding to the fine-tuning regime.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning variance decomposition (RoBERTa, avg over 4 tasks, \\%).}\n\\label{tab:finetune}\n\\small\n\\begin{tabular}{lRRRRR}\n\\toprule\nComponent & \\footnotesize{SST2} & \\footnotesize{MNLI} & \\footnotesize{RTE} & \\footnotesize{COPA} & \\footnotesize{Avg} \\\\\n\\midrule\nitem\\_id & 32.5 & 28.2 & 15.8 & 18.5 & 23.8 \\\\\nseed & 18.3 & 20.5 & 28.2 & 26.8 & 23.5 \\\\\nlearning rate & 11.5 & 12.8 & 17.2 & 15.3 & 14.2 \\\\\nseed$\\times$item & 10.2 & 11.5 & 13.5 & 12.0 & 11.8 \\\\\ndata shuffle & 8.5 & 10.2 & 8.8 & 9.5 & 9.3 \\\\\nlr$\\times$item & 6.8 & 7.0 & 7.5 & 7.3 & 7.2 \\\\\nshuffle$\\times$item & 5.0 & 4.2 & 4.0 & 4.8 & 4.5 \\\\\ngpu & 1.8 & 1.5 & 1.2 & 1.5 & 1.5 \\\\\nprecision & 0.8 & 0.7 & 0.9 & 0.6 & 0.8 \\\\\nresidual & 4.6 & 3.4 & 2.9 & 3.7 & 3.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:inf_vs_ft} contrasts the inference and fine-tuning hierarchies, showing the top-5 components differ qualitatively.\n\n\\begin{table}[t]\n\\centering\n\\caption{Inference vs fine-tuning variance hierarchy (top 5).}\n\\label{tab:inf_vs_ft}\n\\small\n\\begin{tabular}{clRclR}\n\\toprule\n\\# & \\multicolumn{2}{c}{Inference} & & \\multicolumn{2}{c}{Fine-tuning} \\\\\n\\cmidrule{2-3} \\cmidrule{5-6}\n1 & item\\_id & 57.1 & & item\\_id & 23.8 \\\\\n2 & residual & 17.5 & & seed & 23.5 \\\\\n3 & prec:item & 7.0 & & learn. rate & 14.2 \\\\\n4 & temp:item & 6.8 & & seed$\\times$item & 11.8 \\\\\n5 & prompt:item & 5.5 & & data shuffle & 9.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---- exp-007 ----\n\\subsection{LayerCast Precision Mitigation (Exp-007)}\n\\label{sec:layercast}\n\nLayerCast (fp16 storage + fp32 compute) reduces precision-related variance components by 27--50\\% relative to standard 3-precision analysis, while achieving accuracy comparable to bf16 (0.715 vs.\\ 0.711; Table~\\ref{tab:layercast}).\nHowever, the overall impact on reliability is marginal: $G$ improves from 0.36 to 0.38, and D-study items decrease from 420 to 395, because precision variance is a small fraction of total variance on MMLU.\n\n\\begin{table}[t]\n\\centering\n\\caption{Standard vs LayerCast variance decomposition (MMLU, binary, \\%).}\n\\label{tab:layercast}\n\\small\n\\begin{tabular}{lRRr}\n\\toprule\nComponent & Std. & LC & Reduction \\\\\n\\midrule\nitem\\_id & 57.2 & 58.5 & +1.3 \\\\\nprec:item & 7.1 & 4.2 & $-$41\\% \\\\\ntemp:item & 6.9 & 7.0 & +1\\% \\\\\nprecision & 1.1 & 0.8 & $-$27\\% \\\\\nprec:temp & 0.2 & 0.1 & $-$50\\% \\\\\nresidual & 17.6 & 17.8 & +1\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why the gradient exists.}\nThe monotonic decrease of item\\_id from MMLU to MATH reflects a fundamental shift in what determines correctness.\nOn knowledge-retrieval tasks, the answer is largely encoded in model weights; item difficulty (whether a given fact was memorized) dominates variance.\nOn reasoning tasks, correctness depends on a multi-step generation process where each token is influenced by temperature and seed; temperature$\\times$item interactions compound through the reasoning chain, as confirmed by the within-MATH difficulty-level analysis (Table~\\ref{tab:math_levels}).\n\n\\paragraph{Separability as a confirmatory null.}\nThe negligible infrastructure$\\times$methodology interactions under binary scoring validate the implicit assumption of prior isolated-factor studies \\citep{yuan2025,brittlebench2026}: researchers studying prompt sensitivity on fixed hardware, or hardware effects under a fixed prompt, are not missing a large confound.\nThis validation is metric-conditional: under text-exact-match, floating-point non-associativity accumulates through token generation, making precision$\\times$temperature detectable (1.1--2.8\\%).\n\n\\paragraph{Implications for evaluation practice.}\nThe 7.1$\\times$ budget difference between MMLU and MATH (Table~\\ref{tab:dstudy_binary}) means that any ``use $N$ items with $K$ seeds'' guideline implicitly assumes a specific variance structure.\nKnowledge benchmarks need more items and fewer replications; reasoning benchmarks need fewer items but many more replications.\nThe IRT--G-theory gap (Table~\\ref{tab:irt}) shows that item-focused efficiency approaches underestimate the true cost of reliable evaluation when prompt and seed variance are non-negligible.\n\n\\paragraph{Fine-tuning vs.\\ inference.}\nThe qualitative shift in variance hierarchy from inference (item-dominated) to fine-tuning (seed-dominated; Table~\\ref{tab:inf_vs_ft}) implies that reproducibility interventions must be regime-specific.\nFor fine-tuning, running multiple random seeds is more cost-effective than expanding test sets---the opposite of inference evaluation.\nInfrastructure factors remain negligible in both regimes, suggesting that hardware standardization is low-priority in either case.\n\n\\paragraph{LayerCast as a practical recommendation.}\nWhile LayerCast reduces precision-related variance by 27--50\\%, its impact on overall reliability is marginal because precision is not the bottleneck on MMLU.\nIt remains a ``free lunch'' for researchers who want to minimize one source of noise at negligible performance cost.\n\n% ============================================================\n\\section{Limitations}\n\n\\begin{enumerate}\n\\item \\textbf{Open-weight models only.} API models (studied by \\citealt{mesting2026}) have opaque infrastructure. Our analysis complements theirs but cannot be directly combined.\n\\item \\textbf{Binary data in G-theory.} Standard G-theory assumes continuous responses. We mitigate this by reporting parallel analyses on text-exact-match and logprob (continuous metrics), Bernoulli correction (informative item\\_id = 30.7\\%), and noting that IRT similarly uses binary data without this concern being fatal \\citep{lalor2019}.\n\\item \\textbf{Temperature and ordering as random facets.} With 2--3 design points each, these are not randomly sampled from a universe. Sensitivity analysis treating them as fixed changes item\\_id by $<$3pp.\n\\item \\textbf{Encoder-only fine-tuning.} The fine-tuning G-study uses RoBERTa classification. Decoder fine-tuning (instruction tuning, RLHF) likely has a more complex variance structure with additional stochasticity sources.\n\\item \\textbf{Two GPU types.} The hardware separability conclusion is based on RTX PRO 6000 vs.\\ A100. Additional architectures may reveal larger interactions, though the consistent null across both binary and text scoring on these two types is encouraging.\n\\item \\textbf{G-coefficient interpretation.} $G = 0.36$ for 200-item MMLU does not mean ``MMLU is unreliable''---full MMLU ($\\sim$14K items) projects to $G = 0.94$. Our results quantify the cost of subsampling, not the inadequacy of benchmarks.\n\\end{enumerate}\n\n% ============================================================\n\\section{Conclusion}\n\nWe have shown that the variance structure of LLM evaluation is benchmark-conditional, metric-conditional, and regime-conditional.\nItem selection dominates on knowledge-retrieval tasks (57.1\\% on MMLU) but yields to methodology$\\times$item interactions on reasoning tasks (16.8\\% on MATH), producing a monotonic gradient across five benchmarks.\nInfrastructure$\\times$methodology interactions are negligible under binary scoring, validating isolated-factor study designs.\nReproducibility budgets differ by 7.1$\\times$ across benchmarks, rendering universal recipes illusory.\nThe 4.2$\\times$ discrepancy between IRT and G-theory item recommendations reveals the ``cost of multi-facet reliability'' that item-focused approaches miss.\nThese findings provide the empirical foundation for benchmark-specific, metric-conditional evaluation protocols that balance reliability against computational cost.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Biderman et~al.(2024)]{biderman2024}\nBiderman, S., et~al. (2024).\n\\newblock Lessons from the trenches on reproducible evaluation of language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.14782}.\n\n\\bibitem[Bouthillier et~al.(2021)]{bouthillier2021}\nBouthillier, X., et~al. (2021).\n\\newblock Accounting for variance in machine learning benchmarks.\n\\newblock \\emph{Proceedings of Machine Learning and Systems}, 3.\n\n\\bibitem[Brennan(2001)]{brennan2001}\nBrennan, R.~L. (2001).\n\\newblock \\emph{Generalizability Theory}.\n\\newblock Springer-Verlag, New York.\n\n\\bibitem[{Brittlebench Team}(2026)]{brittlebench2026}\n{Brittlebench Team} (2026).\n\\newblock Brittlebench: Quantifying prompt sensitivity in LLM evaluation.\n\\newblock \\emph{Proceedings of NAACL}.\n\n\\bibitem[Cronbach et~al.(1972)]{cronbach1972}\nCronbach, L.~J., Gleser, G.~C., Nanda, H., \\& Rajaratnam, N. (1972).\n\\newblock \\emph{The Dependability of Behavioral Measurements}.\n\\newblock John Wiley \\& Sons.\n\n\\bibitem[Dehghani et~al.(2021)]{dehghani2021}\nDehghani, M., et~al. (2021).\n\\newblock The benchmark lottery.\n\\newblock \\emph{arXiv preprint arXiv:2107.07002}.\n\n\\bibitem[Dodge et~al.(2020)]{dodge2020}\nDodge, J., Ilharco, G., Schwartz, R., Farhadi, A., Hajishirzi, H., \\& Smith, N. (2020).\n\\newblock Fine-tuning pretrained language models: Weight initializations, data orders, and early stopping.\n\\newblock \\emph{arXiv preprint arXiv:2002.06305}.\n\n\\bibitem[Henderson et~al.(2018)]{henderson2018}\nHenderson, P., et~al. (2018).\n\\newblock Deep reinforcement learning that matters.\n\\newblock \\emph{Proceedings of AAAI}, 32(1).\n\n\\bibitem[Hua et~al.(2025)]{hua2025}\nHua, H., et~al. (2025).\n\\newblock Generation-based evaluation avoids scoring artifacts in LLM benchmarks.\n\\newblock \\emph{Proceedings of EMNLP}.\n\n\\bibitem[Lalor et~al.(2019)]{lalor2019}\nLalor, J.~P., Wu, H., \\& Yu, H. (2019).\n\\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.\n\\newblock \\emph{Proceedings of EMNLP-IJCNLP}, pp. 4249--4259.\n\n\\bibitem[Lu et~al.(2022)]{lu2022}\nLu, S., et~al. (2022).\n\\newblock Are emergent abilities in large language models just in-context learning?\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Messina \\& Scotta(2026)]{messina2026}\nMessina, A. \\& Scotta, M. (2026).\n\\newblock On the numerical non-associativity of transformer inference.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Mesting(2026)]{mesting2026}\nMesting, F. (2026).\n\\newblock Variance sources in LLM evaluation: A generalizability theory analysis.\n\\newblock \\emph{Proceedings of ACL}.\n\n\\bibitem[Perlitz et~al.(2023)]{perlitz2023}\nPerlitz, Y., et~al. (2023).\n\\newblock Efficient benchmarking (of language models).\n\\newblock \\emph{arXiv preprint arXiv:2308.11696}.\n\n\\bibitem[Pezeshkpour \\& Hruschka(2024)]{pezeshkpour2024}\nPezeshkpour, P. \\& Hruschka, E. (2024).\n\\newblock Large language models sensitivity to the order of options in multiple-choice questions.\n\\newblock \\emph{Findings of ACL}.\n\n\\bibitem[Polo et~al.(2024)]{polo2024}\nPolo, F.~M., et~al. (2024).\n\\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.\n\\newblock \\emph{Proceedings of ICML}.\n\n\\bibitem[Rodriguez et~al.(2021)]{rodriguez2021}\nRodriguez, P., Barrow, J., Hoyle, A.~M., Lalor, J.~P., Jia, R., \\& Boyd-Graber, J. (2021).\n\\newblock Evaluation examples are not equally informative: How should that change NLP leaderboards?\n\\newblock \\emph{Proceedings of ACL-IJCNLP}, pp. 4486--4503.\n\n\\bibitem[Sellam et~al.(2022)]{sellam2022}\nSellam, T., et~al. (2022).\n\\newblock MultiBERTs: BERT reproductions for robustness analysis.\n\\newblock \\emph{Proceedings of ICLR}.\n\n\\bibitem[Shavelson \\& Webb(1991)]{shavelson1991}\nShavelson, R.~J. \\& Webb, N.~M. (1991).\n\\newblock \\emph{Generalizability Theory: A Primer}.\n\\newblock Sage Publications.\n\n\\bibitem[Vania et~al.(2021)]{vania2021}\nVania, C., et~al. (2021).\n\\newblock Comparing test sets with item response theory.\n\\newblock \\emph{Proceedings of ACL-IJCNLP}.\n\n\\bibitem[Yuan et~al.(2025)]{yuan2025}\nYuan, Z., et~al. (2025).\n\\newblock Hardware lottery in LLM evaluation: Up to 9\\% accuracy variation from infrastructure choices.\n\\newblock \\emph{arXiv preprint}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "782abd80-826b-48f9-9e51-81ce72bc7444",
  "isSidechain": false,
  "requestId": "req_011CbF453d1oboAmDDdPGjjK",
  "type": "assistant",
  "uuid": "cc5ca031-4b6e-440f-bf97-830e739540b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvqJuDSwyNdmmTBhHvGk1d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1810,
      "cache_read_input_tokens": 62957,
      "output_tokens": 17083,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17083,
          "cache_read_input_tokens": 62957,
          "cache_creation_input_tokens": 1810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1810
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

_source line 44 · 2026-05-21T04:11:13.141Z_

<details><summary>↩ Tool result · `toolu_01KL4diQhF9HWoR1cQtRQPRG`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc5ca031-4b6e-440f-bf97-830e739540b9",
  "isSidechain": false,
  "promptId": "fcb16a4e-0813-4fa9-ba4a-a5eb615d5c29",
  "type": "user",
  "uuid": "c875ded2-4826-4f86-a6ce-38e4307570a4",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/paper.tex",
    "content": "\\documentclass[11pt,twocolumn]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[margin=0.75in]{geometry}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{array}\n\\usepackage{xcolor}\n\\usepackage{caption}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{makecell}\n\\usepackage{enumitem}\n\\setlist{nosep}\n\n\\newcolumntype{R}{>{\\raggedleft\\arraybackslash}p{0.55cm}}\n\\newcolumntype{L}{>{\\raggedright\\arraybackslash}p{1.8cm}}\n\n\\title{Reproducibility Budgets for LLM Evaluation:\\\\A Generalizability Theory Analysis of Variance Sources\\\\Across Benchmarks, Models, and Evaluation Metrics}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nWhen LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, numerical precision, temperature, or item selection---let alone how these factors interact.\nWe present the first multi-benchmark Generalizability Theory (G-theory) analysis of LLM evaluation, crossing infrastructure factors (numerical precision, GPU type) with methodology factors (prompt template, random seed, sampling temperature, option ordering) across five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), four 7--9B models, two 14B models, and two evaluation metrics.\nThree findings emerge.\nFirst, item selection is the largest single variance source under binary scoring, but its dominance is \\emph{benchmark-conditional}: it accounts for 57.1\\% of variance on MMLU (knowledge retrieval) but only 16.8\\% on MATH (multi-step reasoning), with a monotonic gradient across all five benchmarks ($r=-0.99$ with cognitive complexity).\nSecond, direct infrastructure$\\times$methodology interactions are negligible under binary scoring ($\\leq$0.6\\% across all benchmarks), providing a confirmatory null result that validates isolated-factor study designs---though this separability breaks down under text-exact-match scoring (up to 2.8\\% on MATH).\nThird, reproducibility budgets are fundamentally benchmark- and metric-conditional: achieving $G\\geq0.90$ reliability requires 2{,}520 evaluations on MMLU but 18{,}000 on MATH under binary scoring, a 7.1$\\times$ difference that renders any ``universal reproducibility recipe'' illusory.\nWe further show that item-count recommendations from IRT-based approaches (e.g., tinyBenchmarks) are 2.8--4.2$\\times$ smaller than G-theory recommendations because they do not account for prompt, seed, and ordering facets.\nA fine-tuning G-study on RoBERTa reveals a qualitatively different variance hierarchy where training seed (23.5\\%) rivals item selection (23.8\\%), demonstrating that reproducibility budgets must be regime-specific.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nThe reproducibility of LLM evaluation is a growing concern.\nStudies report accuracy differences of up to 9 percentage points from numerical precision alone \\citep{yuan2025}, prompt sensitivity explaining 50\\% of observed variance \\citep{brittlebench2026}, and seed-driven fluctuations that reverse model rankings \\citep{biderman2024}.\nYet each study isolates at most two variance sources, implicitly assuming that factors not studied are separable from those that are.\nNo work has tested this assumption in a unified factorial design.\n\nThis gap matters practically.\nA benchmark maintainer deciding whether to standardize prompts, fix seeds, or mandate specific GPU hardware needs to know not just which factor matters most, but whether the answer depends on the benchmark, the evaluation metric, or the model.\nWithout this knowledge, any reproducibility guideline risks being either overly conservative (standardizing factors that contribute negligibly) or dangerously incomplete (ignoring interactions that inflate variance on specific task types).\n\nWe address this gap through Generalizability Theory (G-theory) \\citep{shavelson1991,brennan2001}, a psychometric framework that decomposes observed score variance into contributions from multiple facets simultaneously.\nUnlike ANOVA-based approaches \\citep{bouthillier2021}, G-theory yields Decision studies (D-studies) that project reliability under hypothetical measurement designs, enabling actionable resource allocation.\nUnlike IRT-based subsampling \\citep{polo2024,lalor2019}, G-theory accounts for prompt, seed, and ordering facets alongside items.\n\nOur analysis crosses infrastructure factors (numerical precision across GPU architectures) with methodology factors (prompt template, random seed, sampling temperature, option ordering) across five benchmarks, six models spanning 7B--14B parameters, and three evaluation metrics (binary, text-exact-match, log-probability).\nWe report three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Cross-benchmark variance gradient.} The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval, 57.1\\%) to interaction-dominated (math reasoning, 16.8\\% item, 49.5\\% interactions), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.\n\n\\item \\textbf{Confirmatory separability test.} Infrastructure$\\times$methodology interactions are negligible at the aggregate level ($\\leq$0.6\\% under binary scoring across all benchmarks and GPU types), validating isolated-factor study designs---with the caveat that separability is metric-conditional.\n\n\\item \\textbf{Task-specific reproducibility budgets.} D-study projections with bootstrap confidence intervals yield benchmark-specific, metric-conditional item/prompt/seed allocations for $G\\geq0.90$, contextualized against IRT-based recommendations.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Variance decomposition in ML evaluation.}\n\\citet{bouthillier2021} decomposed ML benchmark variance across hyperparameters, data splits, and random seeds via ANOVA, establishing the template for factorial variance decomposition.\n\\citet{henderson2018} documented high variance in deep RL evaluation.\n\\citet{dodge2020} and \\citet{sellam2022} quantified fine-tuning instability from seed and data order.\n\\citet{dehghani2021} showed that benchmark selection itself introduces systematic bias (the ``Benchmark Lottery'').\nOur work extends this tradition to LLM inference evaluation with a G-theory framework that supports D-study projections.\n\n\\paragraph{LLM evaluation sensitivity.}\n\\citet{yuan2025} documented up to 9\\% accuracy variation from hardware and numerical precision without factorial attribution.\n\\citet{brittlebench2026} quantified prompt sensitivity at 50\\% variance on fixed hardware.\n\\citet{mesting2026} adapted G-theory to five methodological facets in LLM evaluation but treated infrastructure as fixed and studied a single benchmark.\n\\citet{lu2022} and \\citet{pezeshkpour2024} documented option ordering effects.\n\\citet{hua2025} showed that log-likelihood scoring inflates apparent prompt sensitivity.\nWe unify infrastructure and methodology in a crossed factorial design across multiple benchmarks.\n\n\\paragraph{Item-level analysis and efficient evaluation.}\nIRT-based approaches \\citep{lalor2019,rodriguez2021,vania2021} analyze item-level properties for NLP evaluation.\n\\citet{polo2024} (tinyBenchmarks) used IRT for efficient subsampling, recommending $\\sim$100 items per benchmark.\n\\citet{perlitz2023} proposed efficient benchmarking via item selection.\nWe compare G-theory D-study recommendations against IRT baselines, showing a 2.8--4.2$\\times$ discrepancy explained by multi-facet accounting.\n\n\\paragraph{Generalizability Theory.}\nG-theory \\citep{cronbach1972,shavelson1991,brennan2001} extends classical test theory by decomposing variance across multiple random facets simultaneously.\nIt distinguishes G-studies (variance decomposition) from D-studies (reliability projection under alternative designs).\nG-theory has been applied extensively in educational testing and health measurement but only recently to ML evaluation \\citep{mesting2026}.\n\n% ============================================================\n\\section{Method}\n\n\\subsection{Generalizability Theory Background}\n\nIn G-theory, an observed score $X_{pijk\\ldots}$ for object of measurement $p$ (here, a model's response to an item) across facets $i,j,k,\\ldots$ is decomposed as:\n\\begin{equation}\nX_{pijk\\ldots} = \\mu + \\alpha_p + \\beta_i + \\gamma_j + (\\alpha\\beta)_{pi} + \\cdots + \\epsilon\n\\end{equation}\nwhere each term represents a variance component.\nThe G-coefficient quantifies reliability:\n\\begin{equation}\nG = \\frac{\\sigma^2_p}{\\sigma^2_p + \\sigma^2_{\\text{relative error}}}\n\\end{equation}\nwhere $\\sigma^2_{\\text{relative error}}$ is the sum of all variance components involving the object of measurement divided by their respective sample sizes.\n\nA D-study projects $G$ under hypothetical designs by varying facet sample sizes $n_i, n_j, \\ldots$, enabling optimal resource allocation.\nWe estimate variance components using Henderson's Method III \\citep{brennan2001} with REML as a robustness check.\n\n\\subsection{Experimental Design}\n\n\\paragraph{Facets.}\nWe cross the following facets:\n\\begin{itemize}\n\\item \\textbf{Item} ($n_i$=200 per benchmark): Stratified random sample from each benchmark's item pool.\n\\item \\textbf{Prompt template} ($n_p$=6): Diverse prompt formats (zero-shot, few-shot, instruction variants).\n\\item \\textbf{Random seed} ($n_s$=6): CUDA-level nondeterminism seeds.\n\\item \\textbf{Temperature} ($n_t$=2--3): $T \\in \\{0.0, 0.3, 0.7\\}$ (full design) or $\\{0.0, 0.7\\}$ (reduced).\n\\item \\textbf{Option ordering} ($n_o$=4): Systematic rotations of MC answer options.\n\\item \\textbf{Numerical precision}: bf16, fp16, fp32 (full); bf16, fp16 (reduced). Gemma-2 uses bf16+fp32 only due to fp16 numerical instability.\n\\item \\textbf{GPU type} (exp-003): RTX PRO 6000 vs.\\ A100-80GB.\n\\end{itemize}\n\n\\paragraph{Models.}\nPrimary: Llama-3.1-8B, Qwen3-8B, Mistral-7B, Gemma-2-9B (7--9B parameter range).\nScale extension: Qwen3-14B, DeepSeek-R1-Distill-14B.\nFine-tuning: RoBERTa-large.\n\n\\paragraph{Benchmarks.}\nMMLU (knowledge retrieval), ARC-Challenge (science reasoning), HellaSwag (commonsense), GSM8K (math reasoning), MATH (advanced math reasoning).\n\n\\paragraph{Evaluation metrics.}\nBinary correct/incorrect, text-exact-match on generated output, log-probability of correct answer.\n\n\\paragraph{Infrastructure.}\nAll inference uses vLLM 0.9.2 with V0 enforce\\_eager mode across all precision conditions to eliminate the float32 engine confound (where fp32 triggers slower eager-mode attention, degrading accuracy by $\\sim$8--9pp irrespective of precision effects).\n\n\\paragraph{Design variants.}\nMMLU uses the full $3 \\times 3$ precision$\\times$temperature design (exp-001); other benchmarks use a reduced $2 \\times 2$ design (exp-002) due to GPU budget constraints.\nWe verify robustness to this asymmetry by re-analyzing MMLU under a matched $2 \\times 2$ design ($\\Delta$item\\_id = 0.7pp).\n\n% ============================================================\n\\section{Experiments and Results}\n\nWe report eight experiments spanning 3.4M+ evaluation records.\n\n% ---- exp-001 ----\n\\subsection{MMLU G-Study (Exp-001)}\n\\label{sec:exp001}\n\nFour models $\\times$ 3 precisions (Gemma: bf16+fp32) $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings $\\times$ 200 items = 950{,}400 total records.\n\n\\paragraph{Accuracy.}\nOverall accuracy is 0.668. bf16 and fp16 produce near-identical results ($\\Delta < 0.2$pp across all models), while fp32 under V0 enforce\\_eager shows a consistent $\\sim$8.9pp degradation (Table~\\ref{tab:accuracy}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Accuracy by model, precision, and temperature (MMLU).}\n\\label{tab:accuracy}\n\\small\n\\begin{tabular}{llRRR}\n\\toprule\nModel & Prec. & \\footnotesize{T=0} & \\footnotesize{T=.3} & \\footnotesize{T=.7} \\\\\n\\midrule\n\\multirow{3}{*}{\\makecell[l]{Llama\\\\3.1-8B}} & bf16 & .729 & .709 & .695 \\\\\n & fp16 & .730 & .709 & .695 \\\\\n & fp32 & .625 & .601 & .587 \\\\\n\\midrule\n\\multirow{3}{*}{\\makecell[l]{Qwen\\\\3-8B}} & bf16 & .742 & .721 & .706 \\\\\n & fp16 & .741 & .720 & .705 \\\\\n & fp32 & .643 & .618 & .602 \\\\\n\\midrule\n\\multirow{3}{*}{\\makecell[l]{Mistral\\\\7B}} & bf16 & .668 & .645 & .631 \\\\\n & fp16 & .669 & .646 & .632 \\\\\n & fp32 & .578 & .555 & .541 \\\\\n\\midrule\n\\multirow{2}{*}{\\makecell[l]{Gemma\\\\2-9B}} & bf16 & .718 & .696 & .681 \\\\\n & fp32 & .622 & .598 & .583 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Variance decomposition---binary scoring.}\nItem selection dominates variance at 57.1\\% (range 55.8--59.1\\% across models), with remarkably low cross-model variability (SD = 1.4pp).\nAll direct infrastructure$\\times$methodology interactions sum to $\\leq$0.3\\% (Table~\\ref{tab:var_binary}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-model variance decomposition, binary scoring (\\%).}\n\\label{tab:var_binary}\n\\small\n\\begin{tabular}{lRRRRR}\n\\toprule\nComponent & \\rotatebox{60}{\\footnotesize Llama} & \\rotatebox{60}{\\footnotesize Qwen} & \\rotatebox{60}{\\footnotesize Mistr.} & \\rotatebox{60}{\\footnotesize Gem.} & \\rotatebox{60}{\\footnotesize Avg} \\\\\n\\midrule\nitem\\_id & 57.2 & 55.8 & 59.1 & 56.4 & 57.1 \\\\\nresidual & 17.6 & 18.2 & 16.3 & 17.8 & 17.5 \\\\\nprec:item & 7.1 & 7.3 & 6.5 & 7.2 & 7.0 \\\\\ntemp:item & 6.9 & 6.5 & 7.2 & 6.6 & 6.8 \\\\\nprompt:item & 5.4 & 5.8 & 5.2 & 5.6 & 5.5 \\\\\nseed:item & 2.0 & 2.3 & 1.9 & 2.1 & 2.1 \\\\\norder:item & 1.5 & 1.4 & 1.6 & 1.4 & 1.5 \\\\\nprecision & 1.1 & 1.3 & 1.2 & 1.1 & 1.2 \\\\\ntemperature & 0.5 & 0.4 & 0.5 & 0.6 & 0.5 \\\\\nprompt & 0.3 & 0.4 & 0.2 & 0.3 & 0.3 \\\\\nprec:temp & 0.2 & 0.3 & 0.1 & 0.2 & 0.2 \\\\\nother & 0.2 & 0.3 & 0.2 & 0.7 & 0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Variance decomposition---text-exact-match.}\nUnder text-exact-match scoring, the variance hierarchy inverts: residual (38.0\\%) and prompt:item (36.2\\%) dominate, while item\\_id drops to 2.0\\%.\nTemperature becomes a major main effect (16.5\\%), and precision$\\times$temperature rises to 1.1\\% (Table~\\ref{tab:var_text}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance decomposition, text-exact-match scoring (\\%).}\n\\label{tab:var_text}\n\\small\n\\begin{tabular}{lRRRRR}\n\\toprule\nComponent & \\rotatebox{60}{\\footnotesize Llama} & \\rotatebox{60}{\\footnotesize Qwen} & \\rotatebox{60}{\\footnotesize Mistr.} & \\rotatebox{60}{\\footnotesize Gem.} & \\rotatebox{60}{\\footnotesize Avg} \\\\\n\\midrule\nresidual & 38.5 & 37.2 & 39.1 & 37.3 & 38.0 \\\\\nprompt:item & 35.8 & 37.0 & 35.5 & 36.4 & 36.2 \\\\\ntemperature & 16.8 & 16.0 & 16.5 & 16.7 & 16.5 \\\\\ntemp:item & 3.5 & 4.2 & 3.6 & 3.8 & 3.8 \\\\\nitem\\_id & 1.8 & 2.3 & 1.9 & 2.1 & 2.0 \\\\\nprec:temp & 1.2 & 1.0 & 1.1 & 1.0 & 1.1 \\\\\nprec:item & 1.2 & 1.1 & 1.3 & 1.2 & 1.2 \\\\\nother & 1.2 & 1.2 & 1.0 & 1.5 & 1.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{G-coefficients.}\n$G_{\\text{binary}} = 0.36$ for 200 items (item dominance makes $G \\geq 0.90$ unreachable without expansion), while $G_{\\text{text}} = 0.96$ (already adequate).\n\n% ---- exp-001b ----\n\\subsection{Item Resampling Stability (Exp-001b)}\n\\label{sec:exp001b}\n\nTo verify that item dominance is not an artifact of our specific 200-item draw, we conduct three independent stratified samples (seeds 0, 7, 99) with zero item overlap.\nEach sample uses Llama-3.1-8B $\\times$ 3 precisions $\\times$ 3 prompts $\\times$ 3 seeds $\\times$ 2 orderings = 10{,}800 records.\n\nItem\\_id\\% ranges from 55.8\\% to 58.6\\% (SD = 1.4pp), well within expected sampling variability and far above any threshold for dominance (Table~\\ref{tab:stability}).\nG-coefficients are similarly stable (0.34--0.37, range = 0.03).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-sample variance decomposition stability (\\%).}\n\\label{tab:stability}\n\\small\n\\begin{tabular}{lRRRRR}\n\\toprule\nComponent & \\footnotesize{S0} & \\footnotesize{S7} & \\footnotesize{S99} & \\footnotesize{Mean} & \\footnotesize{SD} \\\\\n\\midrule\nitem\\_id & 57.5 & 55.8 & 58.6 & 57.3 & 1.4 \\\\\nresidual & 17.2 & 18.5 & 16.8 & 17.5 & 0.9 \\\\\nprec:item & 7.1 & 7.5 & 6.5 & 7.0 & 0.5 \\\\\ntemp:item & 6.5 & 7.2 & 6.8 & 6.8 & 0.4 \\\\\nprompt:item & 5.8 & 5.0 & 5.6 & 5.5 & 0.4 \\\\\nseed:item & 2.2 & 1.8 & 2.1 & 2.0 & 0.2 \\\\\norder:item & 1.4 & 1.7 & 1.3 & 1.5 & 0.2 \\\\\nprecision & 1.2 & 1.1 & 1.3 & 1.2 & 0.1 \\\\\nother & 1.1 & 1.4 & 1.0 & 1.2 & 0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---- exp-002 + exp-008 ----\n\\subsection{Cross-Benchmark Variance Gradient (Exp-002, Exp-008)}\n\\label{sec:gradient}\n\nWe extend the analysis to four additional benchmarks: ARC-Challenge, HellaSwag, GSM8K (Exp-002: 4 models $\\times$ reduced $2 \\times 2$ design $\\times$ 200 items each, 1{,}209{,}600 records), and MATH (Exp-008: same design, 403{,}200 records).\n\n\\paragraph{The gradient.}\nItem\\_id\\% decreases monotonically from MMLU (57.1\\%) to MATH (16.8\\%) as cognitive complexity increases, while methodology$\\times$item interactions increase correspondingly from 22.9\\% to 49.5\\% (Table~\\ref{tab:gradient}).\nThe gradient spans 40.3pp across five benchmarks and is perfectly monotonic.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark variance gradient, binary scoring (\\%).}\n\\label{tab:gradient}\n\\small\n\\begin{tabular}{lRRRRR}\n\\toprule\nComponent & \\rotatebox{60}{\\footnotesize MMLU} & \\rotatebox{60}{\\footnotesize ARC} & \\rotatebox{60}{\\footnotesize HSwag} & \\rotatebox{60}{\\footnotesize GSM} & \\rotatebox{60}{\\footnotesize MATH} \\\\\n\\midrule\nitem\\_id & 57.1 & 43.7 & 38.2 & 22.4 & 16.8 \\\\\nresidual & 17.5 & 20.3 & 22.5 & 24.8 & 24.5 \\\\\ntemp:item & 6.8 & 9.8 & 12.3 & 18.5 & 21.3 \\\\\nprompt:item & 5.5 & 8.5 & 9.8 & 10.2 & 8.8 \\\\\nseed:item & 2.1 & 4.5 & 6.5 & 12.3 & 14.7 \\\\\nprec:item & 7.0 & 6.2 & 4.8 & 3.2 & 2.5 \\\\\norder:item & 1.5 & 2.8 & 2.4 & 2.1 & 2.2 \\\\\nprecision & 1.2 & 1.2 & 0.8 & 0.8 & 0.6 \\\\\ntemperature & 0.5 & 1.5 & 1.5 & 4.5 & 5.8 \\\\\nprec:temp & 0.2 & 0.3 & 0.4 & 0.6 & 0.5 \\\\\nother & 0.6 & 1.2 & 0.8 & 0.6 & 2.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gradient summary.}\nTable~\\ref{tab:gradient_summary} shows the gradient alongside G-coefficients.\nCounter-intuitively, G increases from MMLU (0.36) to MATH (0.51): extreme item dominance on MMLU means 200 items are insufficient to stabilize estimates, while MATH's lower item variance makes the same count more representative (though more prompt/seed replications are needed).\n\n\\begin{table}[t]\n\\centering\n\\caption{Five-benchmark gradient summary.}\n\\label{tab:gradient_summary}\n\\small\n\\begin{tabular}{llcRRR}\n\\toprule\nBench. & Task & CC & \\footnotesize{item\\%} & \\footnotesize{$\\Sigma$int\\%} & \\footnotesize{$G_{200}$} \\\\\n\\midrule\nMMLU & knowledge & 1 & 57.1 & 22.9 & .36 \\\\\nARC & science & 2 & 43.7 & 31.8 & .42 \\\\\nHSwag & common. & 3 & 38.2 & 35.8 & .44 \\\\\nGSM8K & math & 4 & 22.4 & 46.3 & .48 \\\\\nMATH & math (hard) & 5 & 16.8 & 49.5 & .51 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2mm}\n\\begin{flushleft}\n\\footnotesize CC = cognitive complexity rank. $\\Sigma$int = sum of method$\\times$item interactions. $G_{200}$ = G-coefficient with 200 items, binary scoring.\n\\end{flushleft}\n\\end{table}\n\n\\paragraph{Separability across benchmarks.}\nDirect infrastructure$\\times$methodology interactions remain $\\leq$0.6\\% under binary scoring across all five benchmarks (Table~\\ref{tab:separability}).\nUnder text-exact-match, GSM8K reaches 2.5\\% and MATH reaches 2.8\\%, consistent with floating-point non-associativity accumulating through long generation chains.\n\n\\begin{table}[t]\n\\centering\n\\caption{Direct infra$\\times$method interactions (\\%).}\n\\label{tab:separability}\n\\small\n\\begin{tabular}{llRRR}\n\\toprule\nBenchmark & Metric & \\footnotesize{p$\\times$t} & \\footnotesize{p$\\times$pr} & \\footnotesize{max} \\\\\n\\midrule\nMMLU & binary & 0.2 & 0.1 & 0.2 \\\\\nARC & binary & 0.3 & 0.1 & 0.3 \\\\\nHellaSwag & binary & 0.4 & 0.1 & 0.4 \\\\\nGSM8K & binary & 0.6 & 0.2 & 0.6 \\\\\nMATH & binary & 0.5 & --- & 0.5 \\\\\n\\midrule\nMMLU & text & 1.1 & 0.3 & 1.1 \\\\\nGSM8K & text & 2.5 & 0.8 & 2.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2mm}\n\\begin{flushleft}\n\\footnotesize p$\\times$t = precision$\\times$temperature; p$\\times$pr = precision$\\times$prompt.\n\\end{flushleft}\n\\end{table}\n\n\\paragraph{Within-benchmark gradient (MATH).}\nMATH difficulty levels reveal the gradient operates \\emph{within} a benchmark: Level~1 items resemble MMLU (item\\_id = 28.5\\%), while Level~5 items show extreme interaction dominance (temp:item = 30.1\\%, seed:item = 22.0\\%, item\\_id = 8.2\\%; Table~\\ref{tab:math_levels}).\n\n\\begin{table}[t]\n\\centering\n\\caption{MATH variance by difficulty level (\\%, Qwen3-8B, binary).}\n\\label{tab:math_levels}\n\\small\n\\begin{tabular}{lRRRRR}\n\\toprule\nComponent & \\footnotesize{L1} & \\footnotesize{L2} & \\footnotesize{L3} & \\footnotesize{L4} & \\footnotesize{L5} \\\\\n\\midrule\nitem\\_id & 28.5 & 22.1 & 16.5 & 12.8 & 8.2 \\\\\ntemp:item & 8.5 & 14.2 & 22.5 & 26.8 & 30.1 \\\\\nseed:item & 5.2 & 10.8 & 15.2 & 18.5 & 22.0 \\\\\nresidual & 32.5 & 28.2 & 23.5 & 21.2 & 18.8 \\\\\nother & 25.3 & 24.7 & 22.3 & 20.7 & 20.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---- exp-003 ----\n\\subsection{Multi-Hardware Separability (Exp-003)}\n\\label{sec:hardware}\n\nWe extend the infrastructure facet beyond precision by crossing two GPU architectures (RTX PRO 6000 96GB vs.\\ A100-80GB): 4 models $\\times$ 2 GPUs $\\times$ 2 precisions $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 3 temperatures $\\times$ 4 orderings $\\times$ 200 items = 1{,}382{,}400 records.\n\nGPU type contributes 0.3\\% as a main effect, and all direct GPU$\\times$methodology interactions are negligible under binary scoring (total = 0.5\\%, all CIs contain zero; Table~\\ref{tab:gpu_sep}).\nThe gpu:item interaction (1.8\\%) indicates hardware effects are item-conditional---items near the decision boundary are sensitive to microarchitecture-level floating-point differences, but these cancel at the aggregate level.\n\n\\begin{table}[t]\n\\centering\n\\caption{GPU type separability: direct GPU$\\times$method interactions.}\n\\label{tab:gpu_sep}\n\\small\n\\begin{tabular}{lRRc}\n\\toprule\nInteraction & \\footnotesize{bin\\%} & \\footnotesize{text\\%} & \\footnotesize{CI$\\ni$0?} \\\\\n\\midrule\ngpu$\\times$precision & 0.2 & 0.8 & yes \\\\\ngpu$\\times$temperature & 0.1 & 0.4 & yes \\\\\ngpu$\\times$prompt & 0.1 & 0.2 & yes \\\\\ngpu$\\times$seed & 0.1 & 0.1 & yes \\\\\ngpu$\\times$ordering & 0.0 & 0.0 & yes \\\\\n\\midrule\ntotal direct & 0.5 & 1.5 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith GPU type as an additional facet, item\\_id remains the largest component at 55.2\\% [52.8, 57.6] and the overall variance structure is preserved (Table~\\ref{tab:gpu_full}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance decomposition with GPU facet (MMLU, binary).}\n\\label{tab:gpu_full}\n\\small\n\\begin{tabular}{lRl}\n\\toprule\nComponent & \\% & 95\\% CI \\\\\n\\midrule\nitem\\_id & 55.2 & [52.8, 57.6] \\\\\nresidual & 15.8 & [13.5, 18.1] \\\\\nprec:item & 6.8 & [5.5, 8.1] \\\\\ntemp:item & 6.5 & [5.2, 7.8] \\\\\nprompt:item & 5.3 & [4.1, 6.5] \\\\\nseed:item & 2.0 & [1.3, 2.7] \\\\\ngpu:item & 1.8 & [1.0, 2.6] \\\\\norder:item & 1.4 & [0.8, 2.0] \\\\\nprecision & 1.1 & [0.5, 1.7] \\\\\ngpu:prec:item & 0.5 & [0.2, 0.8] \\\\\ngpu\\_type & 0.3 & [0.0, 0.6] \\\\\nother & 3.3 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---- exp-004 ----\n\\subsection{Model-as-Facet Reanalysis (Exp-004)}\n\\label{sec:model_facet}\n\nTreating model as a crossed random facet (rather than analyzing per-model) properly attributes model$\\times$item interaction, which was previously confounded with item\\_id and residual.\n\nItem\\_id decreases from 57.1\\% to 47.3\\%, with 12.1\\% reassigned to model$\\times$item (Table~\\ref{tab:maf}).\nThe cross-benchmark gradient remains monotonic under model-as-facet analysis (Table~\\ref{tab:maf_gradient}), spanning 29.1pp from MMLU (47.3\\%) to GSM8K (18.2\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{Model-as-facet reanalysis (MMLU, binary, \\%).}\n\\label{tab:maf}\n\\small\n\\begin{tabular}{lRRr}\n\\toprule\nComponent & \\footnotesize{1-model} & \\footnotesize{MAF} & $\\Delta$ \\\\\n\\midrule\nitem\\_id & 57.1 & 47.3 & $-$9.8 \\\\\nmodel$\\times$item & --- & 12.1 & +12.1 \\\\\nmodel & --- & 3.8 & +3.8 \\\\\nresidual & 17.5 & 12.8 & $-$4.7 \\\\\nprec:item & 7.0 & 6.5 & $-$0.5 \\\\\ntemp:item & 6.8 & 6.2 & $-$0.6 \\\\\nprompt:item & 5.5 & 5.0 & $-$0.5 \\\\\nmodel$\\times$prec & --- & 0.5 & +0.5 \\\\\nmodel$\\times$temp & --- & 0.3 & +0.3 \\\\\nother & 6.1 & 5.5 & $-$0.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Model-as-facet cross-benchmark gradient.}\n\\label{tab:maf_gradient}\n\\small\n\\begin{tabular}{lRRR}\n\\toprule\nBenchmark & \\footnotesize{item\\%} & \\footnotesize{m$\\times$i\\%} & \\footnotesize{$\\Delta$MMLU} \\\\\n\\midrule\nMMLU & 47.3 & 12.1 & 0.0 \\\\\nARC & 36.5 & 9.5 & $-$10.8 \\\\\nHellaSwag & 31.4 & 8.8 & $-$15.9 \\\\\nGSM8K & 18.2 & 6.2 & $-$29.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Bootstrap Confidence Intervals and Sensitivity (Exp-004)}\n\\label{sec:bootstrap}\n\nWe compute 1{,}000-resample bootstrap CIs on all variance components (Table~\\ref{tab:bootstrap}).\nItem\\_id's lower bound (44.9\\%) is well-separated from the next-largest component, confirming its dominance is statistically robust.\nPrecision$\\times$temperature under binary scoring has a CI containing zero [0.0, 0.6], confirming non-significance; under text-exact-match, the CI excludes zero, confirming metric-conditional separability.\n\n\\begin{table}[t]\n\\centering\n\\caption{Bootstrap CIs, MMLU model-as-facet (\\%).}\n\\label{tab:bootstrap}\n\\small\n\\begin{tabular}{lRRRR}\n\\toprule\nComponent & Est. & Lo & Hi & Wid. \\\\\n\\midrule\nitem\\_id & 47.3 & 44.9 & 49.7 & 4.8 \\\\\nmodel$\\times$item & 12.1 & 10.4 & 13.9 & 3.5 \\\\\nresidual & 12.8 & 10.8 & 14.8 & 4.0 \\\\\nprec:item & 6.5 & 5.2 & 7.8 & 2.6 \\\\\ntemp:item & 6.2 & 4.9 & 7.5 & 2.6 \\\\\nprompt:item & 5.0 & 3.8 & 6.2 & 2.4 \\\\\nmodel & 3.8 & 1.5 & 6.1 & 4.6 \\\\\nprec:temp (bin) & 0.2 & 0.0 & 0.6 & 0.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMultiple sensitivity analyses confirm robustness (Table~\\ref{tab:sensitivity}): REML vs.\\ Henderson ($\\Delta < 2$pp), fixed vs.\\ random treatment of temperature/ordering ($\\Delta < 3$pp), design asymmetry (3$\\times$3 vs.\\ matched 2$\\times$2: $\\Delta = 0.7$pp), and bootstrap vs.\\ jackknife CIs (width ratio = 0.92, within 20\\% threshold).\n\nBernoulli mechanical variance accounts for 35\\% of observed item\\_id (correlation $r = 0.82$ between $p_i(1-p_i)$ and observed item variance), but the corrected ``informative'' item\\_id remains 30.7\\%---still the largest single component.\n\n\\begin{table}[t]\n\\centering\n\\caption{Sensitivity analyses summary.}\n\\label{tab:sensitivity}\n\\small\n\\begin{tabular}{lR}\n\\toprule\nAnalysis & max $\\Delta$pp \\\\\n\\midrule\nREML vs Henderson & 1.8 \\\\\nFixed vs random facets & 2.8 \\\\\n3$\\times$3 vs matched 2$\\times$2 & 0.7 \\\\\nBootstrap vs jackknife CI ratio & 0.92 \\\\\nBernoulli-corrected item\\_id & 30.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---- D-study ----\n\\subsection{D-Study Projections (Exp-004)}\n\\label{sec:dstudy}\n\nD-study projections reveal starkly different optimal allocations for achieving $G \\geq 0.90$ across benchmarks (Table~\\ref{tab:dstudy_binary}).\nMMLU requires 420 items but only 6 evaluations per item (2{,}520 total), reflecting item dominance.\nMATH requires only 180 items but 100 evaluations per item (18{,}000 total), reflecting interaction dominance.\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study allocations for $G \\geq 0.90$, binary scoring.}\n\\label{tab:dstudy_binary}\n\\small\n\\begin{tabular}{lRRRRRRR}\n\\toprule\nBench. & \\footnotesize{It.} & \\footnotesize{Pr.} & \\footnotesize{Se.} & \\footnotesize{Te.} & \\footnotesize{Or.} & \\footnotesize{Total} & \\footnotesize{GPU-h} \\\\\n\\midrule\nMMLU & 420 & 3 & 2 & 1 & 1 & 2520 & 8.4 \\\\\nARC & 320 & 3 & 3 & 1 & 1 & 2880 & 9.6 \\\\\nHSwag & 290 & 3 & 3 & 1 & 2 & 5220 & 17.4 \\\\\nGSM8K & 220 & 4 & 4 & 2 & 2 & 14080 & 28.2 \\\\\nMATH & 180 & 5 & 5 & 2 & 2 & 18000 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder text-exact-match scoring, budgets are 5--15$\\times$ smaller because item dominance is much weaker (Table~\\ref{tab:dstudy_text}).\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study allocations for $G \\geq 0.90$, text-exact-match.}\n\\label{tab:dstudy_text}\n\\small\n\\begin{tabular}{lRRRRRR}\n\\toprule\nBench. & \\footnotesize{It.} & \\footnotesize{Pr.} & \\footnotesize{Se.} & \\footnotesize{Te.} & \\footnotesize{Or.} & \\footnotesize{Total} \\\\\n\\midrule\nMMLU & 85 & 2 & 1 & 1 & 1 & 170 \\\\\nARC & 110 & 2 & 1 & 1 & 1 & 220 \\\\\nHSwag & 95 & 2 & 2 & 1 & 1 & 380 \\\\\nGSM8K & 150 & 3 & 2 & 1 & 1 & 900 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{IRT comparison.}\nIRT-based approaches (tinyBenchmarks) recommend 2.8--4.2$\\times$ fewer items than G-theory under binary scoring (Table~\\ref{tab:irt}), because IRT optimizes item selection under a single evaluation condition, ignoring prompt/seed/ordering facets.\nThis 4$\\times$ gap is the ``cost of multi-facet reliability.''\nUnder text-exact-match, the gap narrows or inverts because item variance is no longer dominant.\n\n\\begin{table}[t]\n\\centering\n\\caption{IRT vs G-theory item recommendations.}\n\\label{tab:irt}\n\\small\n\\begin{tabular}{lRRRRR}\n\\toprule\nBench. & \\footnotesize{IRT} & \\footnotesize{G-bin} & \\footnotesize{ratio} & \\footnotesize{G-text} & \\footnotesize{t-ratio} \\\\\n\\midrule\nMMLU & 100 & 420 & 4.2 & 85 & 0.85 \\\\\nARC & 75 & 320 & 4.3 & 110 & 1.47 \\\\\nGSM8K & 80 & 220 & 2.8 & 150 & 1.88 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Logprob Scoring Analysis (Exp-004)}\n\\label{sec:logprob}\n\nLog-probability scoring preserves item dominance more strongly than binary scoring across all benchmarks (Table~\\ref{tab:logprob}), with item\\_id ranging from 31.2\\% (GSM8K) to 52.3\\% (MMLU).\nThe gradient remains monotonic.\nThe logprob G-coefficient for MMLU (0.68 at 200 items) is substantially higher than binary (0.36), reflecting the richer information content of continuous scores.\nProjecting to full MMLU (14K items) yields $G = 0.94$ (binary) and $G = 0.998$ (text).\n\n\\begin{table}[t]\n\\centering\n\\caption{Item\\_id\\% across scoring metrics and benchmarks.}\n\\label{tab:logprob}\n\\small\n\\begin{tabular}{lRRR}\n\\toprule\nBenchmark & binary & text & logprob \\\\\n\\midrule\nMMLU & 47.3 & 2.0 & 52.3 \\\\\nARC & 36.5 & 1.8 & 48.1 \\\\\nHellaSwag & 31.4 & 1.5 & 44.5 \\\\\nGSM8K & 18.2 & 8.0 & 31.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---- exp-005 ----\n\\subsection{Scale Extension to 14B Models (Exp-005)}\n\\label{sec:scale}\n\nQwen3-14B and DeepSeek-R1-Distill-14B on a reduced MMLU design (bf16/fp16 $\\times$ 3 prompts $\\times$ 3 seeds $\\times$ 2 temperatures $\\times$ 2 orderings $\\times$ 200 items = 28{,}800 records).\n\nThe variance hierarchy is preserved at 14B scale, with item\\_id averaging 53.0\\%---a modest 4.1pp decrease from 8B models (Table~\\ref{tab:scale}).\nDeepSeek-R1-Distill shows elevated temp:item (9.2\\%) and seed:item (4.1\\%) interactions, consistent with its chain-of-thought reasoning architecture introducing additional sampling stochasticity.\n\n\\begin{table}[t]\n\\centering\n\\caption{8B vs 14B variance decomposition (MMLU, binary, \\%).}\n\\label{tab:scale}\n\\small\n\\begin{tabular}{lRRRR}\n\\toprule\nComponent & \\footnotesize{8B} & \\footnotesize{Q14B} & \\footnotesize{DS14B} & \\footnotesize{14B avg} \\\\\n\\midrule\nitem\\_id & 57.1 & 54.2 & 51.8 & 53.0 \\\\\nresidual & 17.5 & 16.2 & 14.8 & 15.5 \\\\\ntemp:item & 6.8 & 6.5 & 9.2 & 7.8 \\\\\nprompt:item & 5.5 & 6.5 & 5.8 & 6.2 \\\\\nprec:item & 7.0 & 5.4 & 4.8 & 5.1 \\\\\nseed:item & 2.1 & 2.5 & 4.1 & 3.3 \\\\\nother & 4.0 & 8.7 & 9.5 & 9.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---- exp-006 ----\n\\subsection{Fine-Tuning G-Study (Exp-006)}\n\\label{sec:finetune}\n\nTo test whether variance structure differs between inference and fine-tuning, we conduct a fully crossed G-study: RoBERTa-large fine-tuned on SST-2, MNLI, RTE, and COPA with 6 seeds $\\times$ 3 learning rates $\\times$ 4 data shuffles $\\times$ 3 GPUs $\\times$ 2 precisions = 432 runs per task (1{,}728 total, 96.5\\% converged).\n\nThe variance hierarchy is qualitatively different (Table~\\ref{tab:finetune}): training seed (23.5\\%) rivals item\\_id (23.8\\%) as the largest component, with learning rate (14.2\\%) and data shuffle (9.3\\%) as additional major sources.\nInfrastructure factors remain negligible (GPU: 1.5\\%, precision: 0.8\\%), extending the separability finding to the fine-tuning regime.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning variance decomposition (RoBERTa, avg over 4 tasks, \\%).}\n\\label{tab:finetune}\n\\small\n\\begin{tabular}{lRRRRR}\n\\toprule\nComponent & \\footnotesize{SST2} & \\footnotesize{MNLI} & \\footnotesize{RTE} & \\footnotesize{COPA} & \\footnotesize{Avg} \\\\\n\\midrule\nitem\\_id & 32.5 & 28.2 & 15.8 & 18.5 & 23.8 \\\\\nseed & 18.3 & 20.5 & 28.2 & 26.8 & 23.5 \\\\\nlearning rate & 11.5 & 12.8 & 17.2 & 15.3 & 14.2 \\\\\nseed$\\times$item & 10.2 & 11.5 & 13.5 & 12.0 & 11.8 \\\\\ndata shuffle & 8.5 & 10.2 & 8.8 & 9.5 & 9.3 \\\\\nlr$\\times$item & 6.8 & 7.0 & 7.5 & 7.3 & 7.2 \\\\\nshuffle$\\times$item & 5.0 & 4.2 & 4.0 & 4.8 & 4.5 \\\\\ngpu & 1.8 & 1.5 & 1.2 & 1.5 & 1.5 \\\\\nprecision & 0.8 & 0.7 & 0.9 & 0.6 & 0.8 \\\\\nresidual & 4.6 & 3.4 & 2.9 & 3.7 & 3.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:inf_vs_ft} contrasts the inference and fine-tuning hierarchies, showing the top-5 components differ qualitatively.\n\n\\begin{table}[t]\n\\centering\n\\caption{Inference vs fine-tuning variance hierarchy (top 5).}\n\\label{tab:inf_vs_ft}\n\\small\n\\begin{tabular}{clRclR}\n\\toprule\n\\# & \\multicolumn{2}{c}{Inference} & & \\multicolumn{2}{c}{Fine-tuning} \\\\\n\\cmidrule{2-3} \\cmidrule{5-6}\n1 & item\\_id & 57.1 & & item\\_id & 23.8 \\\\\n2 & residual & 17.5 & & seed & 23.5 \\\\\n3 & prec:item & 7.0 & & learn. rate & 14.2 \\\\\n4 & temp:item & 6.8 & & seed$\\times$item & 11.8 \\\\\n5 & prompt:item & 5.5 & & data shuffle & 9.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---- exp-007 ----\n\\subsection{LayerCast Precision Mitigation (Exp-007)}\n\\label{sec:layercast}\n\nLayerCast (fp16 storage + fp32 compute) reduces precision-related variance components by 27--50\\% relative to standard 3-precision analysis, while achieving accuracy comparable to bf16 (0.715 vs.\\ 0.711; Table~\\ref{tab:layercast}).\nHowever, the overall impact on reliability is marginal: $G$ improves from 0.36 to 0.38, and D-study items decrease from 420 to 395, because precision variance is a small fraction of total variance on MMLU.\n\n\\begin{table}[t]\n\\centering\n\\caption{Standard vs LayerCast variance decomposition (MMLU, binary, \\%).}\n\\label{tab:layercast}\n\\small\n\\begin{tabular}{lRRr}\n\\toprule\nComponent & Std. & LC & Reduction \\\\\n\\midrule\nitem\\_id & 57.2 & 58.5 & +1.3 \\\\\nprec:item & 7.1 & 4.2 & $-$41\\% \\\\\ntemp:item & 6.9 & 7.0 & +1\\% \\\\\nprecision & 1.1 & 0.8 & $-$27\\% \\\\\nprec:temp & 0.2 & 0.1 & $-$50\\% \\\\\nresidual & 17.6 & 17.8 & +1\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why the gradient exists.}\nThe monotonic decrease of item\\_id from MMLU to MATH reflects a fundamental shift in what determines correctness.\nOn knowledge-retrieval tasks, the answer is largely encoded in model weights; item difficulty (whether a given fact was memorized) dominates variance.\nOn reasoning tasks, correctness depends on a multi-step generation process where each token is influenced by temperature and seed; temperature$\\times$item interactions compound through the reasoning chain, as confirmed by the within-MATH difficulty-level analysis (Table~\\ref{tab:math_levels}).\n\n\\paragraph{Separability as a confirmatory null.}\nThe negligible infrastructure$\\times$methodology interactions under binary scoring validate the implicit assumption of prior isolated-factor studies \\citep{yuan2025,brittlebench2026}: researchers studying prompt sensitivity on fixed hardware, or hardware effects under a fixed prompt, are not missing a large confound.\nThis validation is metric-conditional: under text-exact-match, floating-point non-associativity accumulates through token generation, making precision$\\times$temperature detectable (1.1--2.8\\%).\n\n\\paragraph{Implications for evaluation practice.}\nThe 7.1$\\times$ budget difference between MMLU and MATH (Table~\\ref{tab:dstudy_binary}) means that any ``use $N$ items with $K$ seeds'' guideline implicitly assumes a specific variance structure.\nKnowledge benchmarks need more items and fewer replications; reasoning benchmarks need fewer items but many more replications.\nThe IRT--G-theory gap (Table~\\ref{tab:irt}) shows that item-focused efficiency approaches underestimate the true cost of reliable evaluation when prompt and seed variance are non-negligible.\n\n\\paragraph{Fine-tuning vs.\\ inference.}\nThe qualitative shift in variance hierarchy from inference (item-dominated) to fine-tuning (seed-dominated; Table~\\ref{tab:inf_vs_ft}) implies that reproducibility interventions must be regime-specific.\nFor fine-tuning, running multiple random seeds is more cost-effective than expanding test sets---the opposite of inference evaluation.\nInfrastructure factors remain negligible in both regimes, suggesting that hardware standardization is low-priority in either case.\n\n\\paragraph{LayerCast as a practical recommendation.}\nWhile LayerCast reduces precision-related variance by 27--50\\%, its impact on overall reliability is marginal because precision is not the bottleneck on MMLU.\nIt remains a ``free lunch'' for researchers who want to minimize one source of noise at negligible performance cost.\n\n% ============================================================\n\\section{Limitations}\n\n\\begin{enumerate}\n\\item \\textbf{Open-weight models only.} API models (studied by \\citealt{mesting2026}) have opaque infrastructure. Our analysis complements theirs but cannot be directly combined.\n\\item \\textbf{Binary data in G-theory.} Standard G-theory assumes continuous responses. We mitigate this by reporting parallel analyses on text-exact-match and logprob (continuous metrics), Bernoulli correction (informative item\\_id = 30.7\\%), and noting that IRT similarly uses binary data without this concern being fatal \\citep{lalor2019}.\n\\item \\textbf{Temperature and ordering as random facets.} With 2--3 design points each, these are not randomly sampled from a universe. Sensitivity analysis treating them as fixed changes item\\_id by $<$3pp.\n\\item \\textbf{Encoder-only fine-tuning.} The fine-tuning G-study uses RoBERTa classification. Decoder fine-tuning (instruction tuning, RLHF) likely has a more complex variance structure with additional stochasticity sources.\n\\item \\textbf{Two GPU types.} The hardware separability conclusion is based on RTX PRO 6000 vs.\\ A100. Additional architectures may reveal larger interactions, though the consistent null across both binary and text scoring on these two types is encouraging.\n\\item \\textbf{G-coefficient interpretation.} $G = 0.36$ for 200-item MMLU does not mean ``MMLU is unreliable''---full MMLU ($\\sim$14K items) projects to $G = 0.94$. Our results quantify the cost of subsampling, not the inadequacy of benchmarks.\n\\end{enumerate}\n\n% ============================================================\n\\section{Conclusion}\n\nWe have shown that the variance structure of LLM evaluation is benchmark-conditional, metric-conditional, and regime-conditional.\nItem selection dominates on knowledge-retrieval tasks (57.1\\% on MMLU) but yields to methodology$\\times$item interactions on reasoning tasks (16.8\\% on MATH), producing a monotonic gradient across five benchmarks.\nInfrastructure$\\times$methodology interactions are negligible under binary scoring, validating isolated-factor study designs.\nReproducibility budgets differ by 7.1$\\times$ across benchmarks, rendering universal recipes illusory.\nThe 4.2$\\times$ discrepancy between IRT and G-theory item recommendations reveals the ``cost of multi-facet reliability'' that item-focused approaches miss.\nThese findings provide the empirical foundation for benchmark-specific, metric-conditional evaluation protocols that balance reliability against computational cost.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Biderman et~al.(2024)]{biderman2024}\nBiderman, S., et~al. (2024).\n\\newblock Lessons from the trenches on reproducible evaluation of language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.14782}.\n\n\\bibitem[Bouthillier et~al.(2021)]{bouthillier2021}\nBouthillier, X., et~al. (2021).\n\\newblock Accounting for variance in machine learning benchmarks.\n\\newblock \\emph{Proceedings of Machine Learning and Systems}, 3.\n\n\\bibitem[Brennan(2001)]{brennan2001}\nBrennan, R.~L. (2001).\n\\newblock \\emph{Generalizability Theory}.\n\\newblock Springer-Verlag, New York.\n\n\\bibitem[{Brittlebench Team}(2026)]{brittlebench2026}\n{Brittlebench Team} (2026).\n\\newblock Brittlebench: Quantifying prompt sensitivity in LLM evaluation.\n\\newblock \\emph{Proceedings of NAACL}.\n\n\\bibitem[Cronbach et~al.(1972)]{cronbach1972}\nCronbach, L.~J., Gleser, G.~C., Nanda, H., \\& Rajaratnam, N. (1972).\n\\newblock \\emph{The Dependability of Behavioral Measurements}.\n\\newblock John Wiley \\& Sons.\n\n\\bibitem[Dehghani et~al.(2021)]{dehghani2021}\nDehghani, M., et~al. (2021).\n\\newblock The benchmark lottery.\n\\newblock \\emph{arXiv preprint arXiv:2107.07002}.\n\n\\bibitem[Dodge et~al.(2020)]{dodge2020}\nDodge, J., Ilharco, G., Schwartz, R., Farhadi, A., Hajishirzi, H., \\& Smith, N. (2020).\n\\newblock Fine-tuning pretrained language models: Weight initializations, data orders, and early stopping.\n\\newblock \\emph{arXiv preprint arXiv:2002.06305}.\n\n\\bibitem[Henderson et~al.(2018)]{henderson2018}\nHenderson, P., et~al. (2018).\n\\newblock Deep reinforcement learning that matters.\n\\newblock \\emph{Proceedings of AAAI}, 32(1).\n\n\\bibitem[Hua et~al.(2025)]{hua2025}\nHua, H., et~al. (2025).\n\\newblock Generation-based evaluation avoids scoring artifacts in LLM benchmarks.\n\\newblock \\emph{Proceedings of EMNLP}.\n\n\\bibitem[Lalor et~al.(2019)]{lalor2019}\nLalor, J.~P., Wu, H., \\& Yu, H. (2019).\n\\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.\n\\newblock \\emph{Proceedings of EMNLP-IJCNLP}, pp. 4249--4259.\n\n\\bibitem[Lu et~al.(2022)]{lu2022}\nLu, S., et~al. (2022).\n\\newblock Are emergent abilities in large language models just in-context learning?\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Messina \\& Scotta(2026)]{messina2026}\nMessina, A. \\& Scotta, M. (2026).\n\\newblock On the numerical non-associativity of transformer inference.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Mesting(2026)]{mesting2026}\nMesting, F. (2026).\n\\newblock Variance sources in LLM evaluation: A generalizability theory analysis.\n\\newblock \\emph{Proceedings of ACL}.\n\n\\bibitem[Perlitz et~al.(2023)]{perlitz2023}\nPerlitz, Y., et~al. (2023).\n\\newblock Efficient benchmarking (of language models).\n\\newblock \\emph{arXiv preprint arXiv:2308.11696}.\n\n\\bibitem[Pezeshkpour \\& Hruschka(2024)]{pezeshkpour2024}\nPezeshkpour, P. \\& Hruschka, E. (2024).\n\\newblock Large language models sensitivity to the order of options in multiple-choice questions.\n\\newblock \\emph{Findings of ACL}.\n\n\\bibitem[Polo et~al.(2024)]{polo2024}\nPolo, F.~M., et~al. (2024).\n\\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.\n\\newblock \\emph{Proceedings of ICML}.\n\n\\bibitem[Rodriguez et~al.(2021)]{rodriguez2021}\nRodriguez, P., Barrow, J., Hoyle, A.~M., Lalor, J.~P., Jia, R., \\& Boyd-Graber, J. (2021).\n\\newblock Evaluation examples are not equally informative: How should that change NLP leaderboards?\n\\newblock \\emph{Proceedings of ACL-IJCNLP}, pp. 4486--4503.\n\n\\bibitem[Sellam et~al.(2022)]{sellam2022}\nSellam, T., et~al. (2022).\n\\newblock MultiBERTs: BERT reproductions for robustness analysis.\n\\newblock \\emph{Proceedings of ICLR}.\n\n\\bibitem[Shavelson \\& Webb(1991)]{shavelson1991}\nShavelson, R.~J. \\& Webb, N.~M. (1991).\n\\newblock \\emph{Generalizability Theory: A Primer}.\n\\newblock Sage Publications.\n\n\\bibitem[Vania et~al.(2021)]{vania2021}\nVania, C., et~al. (2021).\n\\newblock Comparing test sets with item response theory.\n\\newblock \\emph{Proceedings of ACL-IJCNLP}.\n\n\\bibitem[Yuan et~al.(2025)]{yuan2025}\nYuan, Z., et~al. (2025).\n\\newblock Hardware lottery in LLM evaluation: Up to 9\\% accuracy variation from infrastructure choices.\n\\newblock \\emph{arXiv preprint}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "cc5ca031-4b6e-440f-bf97-830e739540b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032813 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory…",
  "leafUuid": "c875ded2-4826-4f86-a6ce-38e4307570a4",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper for NLP variance study",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

### Assistant

_source line 47 · 2026-05-21T04:11:18.801Z_

Now compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c875ded2-4826-4f86-a6ce-38e4307570a4",
  "isSidechain": false,
  "requestId": "req_011CbF4TTc22rfbFFS7qj7Dc",
  "type": "assistant",
  "uuid": "32cd11d8-14ac-4000-99ed-fc4988afc3cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EsJX6epzrxfdPpRV2695aL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17149,
      "cache_read_input_tokens": 64767,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17149,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 64767,
          "cache_creation_input_tokens": 17149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17149
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

_source line 48 · 2026-05-21T04:11:19.819Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0188cXonKYgWTPqftc274gJu`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32cd11d8-14ac-4000-99ed-fc4988afc3cd",
  "isSidechain": false,
  "requestId": "req_011CbF4TTc22rfbFFS7qj7Dc",
  "type": "assistant",
  "uuid": "9cd27a70-ef90-4c41-b066-f7e0acefaf0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EsJX6epzrxfdPpRV2695aL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17149,
      "cache_read_input_tokens": 64767,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17149,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 64767,
          "cache_creation_input_tokens": 17149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17149
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

_source line 49 · 2026-05-21T04:11:20.433Z_

<details><summary>↩ Tool result · `toolu_0188cXonKYgWTPqftc274gJu`</summary>

```text
)

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
type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (10 pages, 238476 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cd27a70-ef90-4c41-b066-f7e0acefaf0f",
  "isSidechain": false,
  "promptId": "fcb16a4e-0813-4fa9-ba4a-a5eb615d5c29",
  "type": "user",
  "uuid": "0e2daf1a-8b88-417e-b5be-fadfdd605357",
  "toolUseResult": {
    "stdout": ")\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (10 pages, 238476 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9cd27a70-ef90-4c41-b066-f7e0acefaf0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-21T04:11:23.903Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0113LAsKmumw5kZM1seeW6Ts`</summary>

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
  "parentUuid": "0e2daf1a-8b88-417e-b5be-fadfdd605357",
  "isSidechain": false,
  "requestId": "req_011CbF4TzWNna1VyQynqc8zJ",
  "type": "assistant",
  "uuid": "d0481fbc-5eba-47ec-9b00-cbbe6f36bde0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYPWdxiX6LRkBNZ2jKVuAg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 81916,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 828,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 81916,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 828
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

_source line 51 · 2026-05-21T04:11:24.486Z_

<details><summary>↩ Tool result · `toolu_0113LAsKmumw5kZM1seeW6Ts`</summary>

```text
s/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (10 pages, 243963 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0481fbc-5eba-47ec-9b00-cbbe6f36bde0",
  "isSidechain": false,
  "promptId": "fcb16a4e-0813-4fa9-ba4a-a5eb615d5c29",
  "type": "user",
  "uuid": "109785ac-d2d5-4062-b473-c497785c1d4e",
  "toolUseResult": {
    "stdout": "s/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (10 pages, 243963 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d0481fbc-5eba-47ec-9b00-cbbe6f36bde0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-21T04:11:29.975Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ggfz7UE42JAZVDdq6jd6mv`</summary>

```json
{
  "command": "grep -c \"Warning\" /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/paper.log | head -1 && grep \"Error\" /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/paper.log | head -5",
  "description": "Check for errors in compilation log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "109785ac-d2d5-4062-b473-c497785c1d4e",
  "isSidechain": false,
  "requestId": "req_011CbF4UHqvDyCnFDUBj9AGe",
  "type": "assistant",
  "uuid": "fbfb4d4a-df12-40db-a9d0-58a29806a817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8nk1jKqG1H1C3nFsogmJa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 82744,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 82744,
          "cache_creation_input_tokens": 438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 438
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

_source line 53 · 2026-05-21T04:11:30.033Z_

<details><summary>↩ Tool result · `toolu_01Ggfz7UE42JAZVDdq6jd6mv`</summary>

```text
1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbfb4d4a-df12-40db-a9d0-58a29806a817",
  "isSidechain": false,
  "promptId": "fcb16a4e-0813-4fa9-ba4a-a5eb615d5c29",
  "type": "user",
  "uuid": "2bc38178-fa92-4fa3-8cdd-6e21c2f8076e",
  "toolUseResult": {
    "stdout": "1",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fbfb4d4a-df12-40db-a9d0-58a29806a817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-21T04:11:35.554Z_

编译成功，无错误。10 页 PDF 已生成。

论文覆盖全部 8 个实验（exp-001 到 exp-008），包含 24 个表格对应的 LaTeX 表格（部分合并呈现），结构为 Abstract → Introduction → Related Work → Method → Experiments (8 subsections) → Discussion → Limitations → Conclusion → Bibliography (21 references)。所有定量 claim 均来自 experiment\_data.json，未编造数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bc38178-fa92-4fa3-8cdd-6e21c2f8076e",
  "isSidechain": false,
  "requestId": "req_011CbF4UhYCHHVcJmxiMDEqW",
  "type": "assistant",
  "uuid": "da538a91-a629-4a7e-b54b-afa84c491038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CL1ZW78t81P4FE5vWn1kqh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 83182,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 83182,
          "cache_creation_input_tokens": 204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 204
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

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032813 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory…",
  "leafUuid": "da538a91-a629-4a7e-b54b-afa84c491038",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulation paper for NLP variance study",
  "sessionId": "13e5f08b-3dc1-43e8-aae0-fe1160ce0172"
}
```

---
