# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/4252ca06-67da-4be4-a2cb-c5a7e1cf56da.jsonl`
- **Structured JSON:** [`0e1648286899e6056e41.json`](../../sessions/0e/0e1648286899e6056e41.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T01:53:54.909Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T01:53:54.909Z",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Core \"DIF reveals benchmark problems\" narrative collapses. Reviewers converge on: DIF is a capability improvement detector, not a benchmark integrity tool. 38% instability = 38% of items are capability-sensitive (models improved on them). ρ=0.307 is the smoking gun for reviewers. GSM1K r=−0.478 is weaponized: \"DIF anti-correlates with contamination, confirming DIF captures capability, not contamination.\" ρ=0.997 trivializes downstream significance. Semi-synthetic injection dismissed as non-transferable to real contamination. Unidimensional MH on 57-subject MMLU called methodologically invalid by psychometrics-literate reviewer. Reframe required: pivot to \"DIF as capability archaeology / measurement efficiency\" paper. Title: \"Identifying Capability-Authentic Benchmark Items via Differential Item Functioning.\" The same data supports a different story — instability becomes signal, ρ=0.997 becomes \"benchmarks are 3× too large,\" r=−0.478 becomes the headline positive finding. Target ICLR 2027 as robust evaluation / measurement efficiency contribution.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T01:53:54.913Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T01:53:54.913Z",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-21T01:53:54.934Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Core "DIF reveals benchmark problems" narrative collapses. Reviewers converge on: DIF is a capability improvement detector, not a benchmark integrity tool. 38% instability = 38% of items are capability-sensitive (models improved on them). ρ=0.307 is the smoking gun for reviewers. GSM1K r=−0.478 is weaponized: "DIF anti-correlates with contamination, confirming DIF captures capability, not contamination." ρ=0.997 trivializes downstream significance. Semi-synthetic injection dismissed as non-transferable to real contamination. Unidimensional MH on 57-subject MMLU called methodologically invalid by psychometrics-literate reviewer. Reframe required: pivot to "DIF as capability archaeology / measurement efficiency" paper. Title: "Identifying Capability-Authentic Benchmark Items via Differential Item Functioning." The same data supports a different story — instability becomes signal, ρ=0.997 becomes "benchmarks are 3× too large," r=−0.478 becomes the headline positive finding. Target ICLR 2027 as robust evaluation / measurement efficiency contribution.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "41166657-dacb-41c2-9c9f-045334e8b1ff",
  "type": "user",
  "uuid": "47a11f22-90c3-4668-a540-5ec02930cf31",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T01:53:54.933Z_

```json
{
  "parentUuid": "47a11f22-90c3-4668-a540-5ec02930cf31",
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
  "uuid": "4803a39e-2a98-46d1-9a63-6106a6b1476f",
  "timestamp": "2026-05-21T01:53:54.933Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T01:53:54.933Z_

```json
{
  "parentUuid": "4803a39e-2a98-46d1-9a63-6106a6b1476f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b12516a8-2780-4b05-9aaf-5c3dc5198d27",
  "timestamp": "2026-05-21T01:53:54.933Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
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
  "aiTitle": "Generate worst-tier simulation paper from experiment data",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da"
}
```

---

### Assistant

_source line 7 · 2026-05-21T01:53:57.552Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b12516a8-2780-4b05-9aaf-5c3dc5198d27",
  "isSidechain": false,
  "requestId": "req_011CbEszBkrnuXaZuepkfC65",
  "type": "assistant",
  "uuid": "11ffdffc-06ed-4cc9-80f2-c68acf220c55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEgxux6u7gm9A3Gb3M5vmc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11458,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11458,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11458
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

_source line 8 · 2026-05-21T01:53:58.663Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T5GuDJxi2DAdhunNan99eU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11ffdffc-06ed-4cc9-80f2-c68acf220c55",
  "isSidechain": false,
  "requestId": "req_011CbEszBkrnuXaZuepkfC65",
  "type": "assistant",
  "uuid": "7c0cfcfe-7766-4c3a-94dd-8822bb8ae22d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEgxux6u7gm9A3Gb3M5vmc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11458,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11458,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11458
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

_source line 9 · 2026-05-21T01:53:58.741Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C9S7TvubaBX52ijGegZyEv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c0cfcfe-7766-4c3a-94dd-8822bb8ae22d",
  "isSidechain": false,
  "requestId": "req_011CbEszBkrnuXaZuepkfC65",
  "type": "assistant",
  "uuid": "bd20ebb2-3508-4a4f-9c19-670a6381f1a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEgxux6u7gm9A3Gb3M5vmc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11458,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11458,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11458
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

_source line 10 · 2026-05-21T01:53:58.749Z_

<details><summary>↩ Tool result · `toolu_01C9S7TvubaBX52ijGegZyEv`</summary>

```text
1	# Paper Framing — irt_equated_bench_regen
2	
3	## Target Venue
4	- Primary: ICLR 2027 (expected deadline ~October 2026)
5	
6	## Paper Type
7	Empirical analysis / psychometric characterization. Discovery paper, not methods paper. "DIF reveals benchmark structural problems," not "DIF detects contamination."
8	
9	## Core Claims (4 条, 可证伪)
10	
11	**Claim 1 (Temporal Comparability Concern)**: 38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. This instability persists within every subject domain (within-subject C%=31-45%, avg 38.1%), is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). This means cross-temporal MMLU score comparisons carry uncontrolled item-level variance.
12	- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%)
13	- Honesty requirement: ρ=0.307 means "item instability" may mainly reflect "models got better at those domains" — we cannot decompose 38% into contamination vs capability improvement
14	
15	**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).
16	- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)
17	- Framing: aggressive — "the field's standard validation approach is fundamentally mismatched for item-level detection"
18	
19	**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).
20	- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)
21	- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks
22	- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability
23	
24	**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:
25	1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.
26	2. **DIF items = discriminative signal carriers**: DIF removal causes significantly MORE ranking disruption than random removal (z=-8 to -49σ, 21/21 conditions). DIF items carry 1.09× cross-cohort accuracy swing vs 0.96× for stable items — they concentrate the information that differentiates model generations.
27	3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not "find bad items and remove" but "understand what changed and why." Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.
28	4. **Cross-benchmark validation — DIF captures capability, not contamination**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005; partial r=−0.385 controlling accuracy; permutation p=0.014). Contaminated models (high GSM8K-GSM1K gap: Phi, Gemma families) perform WORSE on DIF items. DIF captures genuine capability-discriminative items that contamination cannot fake — contamination produces shallow performance gains concentrated on non-DIF items. N=33 matched models, leave-one-out robust (min |r|=0.374).
29	- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_004 Step 3 (r=−0.478, p=0.005, 33 models)
30	- Growing Pains互补: "Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading" — mutual value positioning
31	- Caveats (→ limitations): super-family analysis limited to N≥20 families; GSM1K validation N=33 (CI wide); contamination gap is proxy, not ground truth
32	
33	## Story Spine
34	
35	**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.
36	
37	**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.
38	
39	**What we find**: Three discoveries, each a contribution:
40	
41	1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.
42	
43	2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.
44	
45	3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.
46	
47	4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K confirms: DIF flags anti-correlate with contamination (r=−0.478, p=0.005) — contaminated models can't fake performance on DIF items, which capture genuine capability differences. DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.
48	
49	**Headline result**: "Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF flags anti-correlate with contamination (r=−0.478, p=0.005): DIF captures genuine capability-discriminative items that contamination cannot replicate. We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000)."
50	
51	## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks
52	
53	Systematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.
54	
55	## Venue Fit
56	
57	- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.
58	- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 38% instability, (2) the ground truth meta-critique affecting the field, (3) the semi-synthetic framework. Frame as "bringing mature psychometric tools to characterize an urgent ML evaluation problem."
59	
60	## Anticipated Reviewer Concerns (updated for pivot)
61	
62	1. **"38% could just mean models got better"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.
63	
64	2. **"Ground truth critique is obvious — of course web labels don't capture differential effects"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.
65	
66	3. **"Semi-synthetic injection is artificial"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.
67	
68	4. **"DIF power is only sufficient for large effects"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.
69	
70	5. **"Only validated on MMLU"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.
71	
72	6. **"Higher methods (MIMIC, propensity-score) could solve the confounding"** — Acknowledged as future work. We frame our three-attempt negative results as "empirical observation" that motivates these directions, not as impossibility.
73	
74	## Dropped from Original Framing
75	
76	- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.
77	- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.
78	- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.
79	- **Detection as primary contribution**: Pivoted from "we detect contamination" to "we characterize benchmark properties."
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd20ebb2-3508-4a4f-9c19-670a6381f1a4",
  "isSidechain": false,
  "promptId": "41166657-dacb-41c2-9c9f-045334e8b1ff",
  "type": "user",
  "uuid": "aebd61a0-de3c-477a-982c-9bf7fc78f06e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: 38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. This instability persists within every subject domain (within-subject C%=31-45%, avg 38.1%), is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). This means cross-temporal MMLU score comparisons carry uncontrolled item-level variance.\n- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%)\n- Honesty requirement: ρ=0.307 means \"item instability\" may mainly reflect \"models got better at those domains\" — we cannot decompose 38% into contamination vs capability improvement\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\"\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items = discriminative signal carriers**: DIF removal causes significantly MORE ranking disruption than random removal (z=-8 to -49σ, 21/21 conditions). DIF items carry 1.09× cross-cohort accuracy swing vs 0.96× for stable items — they concentrate the information that differentiates model generations.\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\n4. **Cross-benchmark validation — DIF captures capability, not contamination**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005; partial r=−0.385 controlling accuracy; permutation p=0.014). Contaminated models (high GSM8K-GSM1K gap: Phi, Gemma families) perform WORSE on DIF items. DIF captures genuine capability-discriminative items that contamination cannot fake — contamination produces shallow performance gains concentrated on non-DIF items. N=33 matched models, leave-one-out robust (min |r|=0.374).\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_004 Step 3 (r=−0.478, p=0.005, 33 models)\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\" — mutual value positioning\n- Caveats (→ limitations): super-family analysis limited to N≥20 families; GSM1K validation N=33 (CI wide); contamination gap is proxy, not ground truth\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.\n\n**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\n\n**What we find**: Three discoveries, each a contribution:\n\n1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.\n\n2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.\n\n3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.\n\n4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K confirms: DIF flags anti-correlate with contamination (r=−0.478, p=0.005) — contaminated models can't fake performance on DIF items, which capture genuine capability differences. DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.\n\n**Headline result**: \"Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF flags anti-correlate with contamination (r=−0.478, p=0.005): DIF captures genuine capability-discriminative items that contamination cannot replicate. We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000).\"\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\n- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 38% instability, (2) the ground truth meta-critique affecting the field, (3) the semi-synthetic framework. Frame as \"bringing mature psychometric tools to characterize an urgent ML evaluation problem.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"38% could just mean models got better\"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 80
    }
  },
  "sourceToolAssistantUUID": "bd20ebb2-3508-4a4f-9c19-670a6381f1a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "aebd61a0-de3c-477a-982c-9bf7fc78f06e",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulation paper from experiment data",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da"
}
```

---

### Tool result

_source line 13 · 2026-05-21T01:53:59.024Z_

<details><summary>↩ Tool result · `toolu_01T5GuDJxi2DAdhunNan99eU`</summary>

```text
1	[
2	  {
3	    "name": "real_data_dif_mmlu",
4	    "description": "Apply MH DIF to METABENCH MMLU 5,219×12,508 matrix. Temporal cohort (2023 vs 2024-H1), ability-quintile cohort, within-family confound control, domain-specificity analysis.\n",
5	    "results": {
6	      "temporal_ets_c_pct": 31.3,
7	      "temporal_fpr_li_clean": 0.318,
8	      "temporal_enrichment": 0.96,
9	      "ability_ets_c_pct": 2.9,
10	      "within_family_llama2v3_c_pct": 61.3,
11	      "domain_spearman_rho": 0.307,
12	      "domain_spearman_p": 0.02,
13	      "sanity_random_split_c_pct": 0.18,
14	      "reviewer_interpretation": "capability_gain_detector"
15	    },
16	    "tables": [
17	      {
18	        "name": "Table 1: DIF Detection Summary Under Worst Interpretation",
19	        "columns": [
20	          "cohort_definition",
21	          "c_pct",
22	          "enrichment_vs_li",
23	          "reviewer_counterargument"
24	        ],
25	        "rows": [
26	          [
27	            "temporal_2023_vs_2024",
28	            31.3,
29	            0.96,
30	            "Capability gain across generations"
31	          ],
32	          [
33	            "ability_quintile",
34	            2.9,
35	            1.19,
36	            "Minimal DIF = items function consistently across ability levels (expected)"
37	          ],
38	          [
39	            "within_family_llama2v3",
40	            61.3,
41	            "N/A",
42	            "Same family, same data pipeline → pure capability gain"
43	          ],
44	          [
45	            "random_split_sanity",
46	            0.18,
47	            "N/A",
48	            "Confirms real signal, but signal = capability"
49	          ]
50	        ]
51	      },
52	      {
53	        "name": "Table 2: Domain Correlation Detail",
54	        "columns": [
55	          "metric",
56	          "value",
57	          "reviewer_spin"
58	        ],
59	        "rows": [
60	          [
61	            "spearman_rho_dif_vs_accuracy_gain",
62	            0.307,
63	            "DIF tracks capability improvement"
64	          ],
65	          [
66	            "p_value",
67	            0.02,
68	            "Significant correlation confirms confound"
69	          ],
70	          [
71	            "variance_explained",
72	            "9.4%",
73	            "Remainder is noise, not contamination signal"
74	          ]
75	        ]
76	      }
77	    ],
78	    "figures": [],
79	    "analysis": "The plan_001 results are empirically sound but narratively fatal under worst tier. The reframe salvages them: 31.3% \"instability\" becomes \"31% of items are capability- sensitive — they differentiate model generations.\" ρ=0.307 becomes evidence that DIF identifies items where genuine capability improvement concentrates. Enrichment=0.96 is reframed as \"DIF and contamination labels measure orthogonal constructs — DIF captures differential item functioning, not data leakage.\" The within-family result becomes the strongest evidence FOR the reframe: even within Llama family, DIF identifies where architectural/training improvements manifest at the item level.\n\n\nUnder worst tier, the actual results hold (these are already observed) but their interpretation collapses. ρ=0.307 (p=0.02) correlating DIF flags with domain-level accuracy improvement is seized by reviewers as causal evidence: items flagged by DIF are simply items where models improved. Enrichment=0.96 against Li et al. labels confirms zero relationship to contamination — reviewers read this as \"DIF doesn't detect contamination at all.\" The 61.3% within-family Llama-2-vs-3 C% is devastating: within the same family (same training pipeline, likely same data), DIF flags 61% of items, which reviewers attribute entirely to capability gain between generations. The sanity check (0.18%) proves DIF detects *something* real, but reviewers argue that \"something\" is capability improvement, not benchmark pathology. The meta-critique about Li et al. labels is dismissed: \"You haven't provided ANY ground truth showing DIF detects contamination — enrichment=0.96 is your only validation, and it failed.\"\n"
80	  },
81	  {
82	    "name": "rl_robustness_validation",
83	    "description": "Validate DIF robustness to RL training. Alignment-RL (DPO/ORPO, N=477) and reasoning-RL (GRPO/PPO, N≈13) cohorts. Compare DIF vs Min-K%/ConStat per-model degradation. Power analysis for partial exploitation.\n",
84	    "results": {
85	      "n_reasoning_rl_models": 13,
86	      "dif_flag_overlap_sft_vs_alignment_rl": 0.82,
87	      "dif_flag_overlap_sft_vs_reasoning_rl": 0.71,
88	      "mink_auroc_sft": 0.63,
89	      "mink_auroc_alignment_rl": 0.58,
90	      "mink_auroc_reasoning_rl": 0.44,
91	      "constat_auroc_sft": 0.67,
92	      "constat_auroc_reasoning_rl": 0.51,
93	      "dif_tpr_with_rl_in_cohort": 0.65,
94	      "dif_tpr_without_rl_in_cohort": 0.68,
95	      "bootstrap_ci_overlap": true,
96	      "delong_p_dif_vs_constat": 0.23,
97	      "tost_equivalence_p": 0.34,
98	      "partial_exploitation_detection_boundary": 0.55,
99	      "reviewer_score": 4.0
100	    },
101	    "tables": [
102	      {
103	        "name": "Table 3: RL Robustness Comparison (Underpowered)",
104	        "columns": [
105	          "method",
106	          "sft_auroc",
107	          "alignment_rl_auroc",
108	          "reasoning_rl_auroc",
109	          "95% CI width"
110	        ],
111	        "rows": [
112	          [
113	            "DIF_MH",
114	            0.69,
115	            0.66,
116	            0.65,
117	            "±0.14"
118	          ],
119	          [
120	            "Min-K%",
121	            0.63,
122	            0.58,
123	            0.44,
124	            "±0.18"
125	          ],
126	          [
127	            "ConStat",
128	            0.67,
129	            0.61,
130	            0.51,
131	            "±0.16"
132	          ]
133	        ]
134	      },
135	      {
136	        "name": "Table 4: Statistical Tests (All Non-Significant)",
137	        "columns": [
138	          "comparison",
139	          "test",
140	          "statistic",
141	          "p_value",
142	          "conclusion"
143	        ],
144	        "rows": [
145	          [
146	            "DIF_vs_ConStat_RL",
147	            "DeLong",
148	            "z=1.19",
149	            0.23,
150	            "Cannot reject H0"
151	          ],
152	          [
153	            "DIF_retention_equivalence",
154	            "TOST",
155	            "t=0.96",
156	            0.34,
157	            "Cannot claim equivalence"
158	          ],
159	          [
160	            "flag_overlap_SFT_vs_RL",
161	            "Bootstrap Jaccard",
162	            0.71,
163	            "CI [0.54, 0.88]",
164	            "Wide CI, inconclusive"
165	          ]
166	        ]
167	      }
168	    ],
169	    "figures": [],
170	    "analysis": "Experiment is fatally underpowered. N=13 reasoning-RL models cannot support any statistical claim. Under worst tier, this becomes ammunition: \"authors claim RL robustness but provide no evidence.\" Reframe option: drop RL robustness as a claim entirely, acknowledge in limitations, reposition the alignment-RL (N=477) result as \"DIF is stable across training objective variations\" without claiming reasoning-RL coverage. Under the capability-archaeology reframe, RL robustness is less central anyway — the question becomes \"do capability-authentic items remain stable across training paradigms?\" which is interesting but not load-bearing.\n\n\nWith only N=13 reasoning-RL models, no comparison reaches statistical significance. DIF flag overlap between SFT and RL-containing cohorts is 71%, which reviewers dismiss as \"you can't distinguish robustness from noise with N=13.\" The DeLong test p=0.23 means we cannot claim DIF outperforms ConStat. TOST equivalence test fails (p=0.34 > 0.05) — we can't even claim equivalence. Min-K% drops to 0.44 AUROC on reasoning-RL models, but reviewers note \"you're comparing DIF (group-level, N=477 cohort) against per-model detectors on 13 models — apples to oranges.\" The partial exploitation analysis shows detection boundary at p=0.55, meaning DIF misses contamination below 55% exploitation rate — reviewers call this \"DIF only detects extreme contamination, which is also detectable by simpler methods.\" The entire experiment is underpowered and reviewers recommend \"defer until more GRPO/PPO models exist on public leaderboards.\"\n"
171	  },
172	  {
173	    "name": "constat_perturbation_eval",
174	    "description": "Independent ConStat-style perturbation evaluation on 200+ MMLU items. Generate semantic reformulations, compare original vs reformulated performance, apply FDR-controlled detection.\n",
175	    "results": {
176	      "n_items_reformulated": 220,
177	      "n_models_tested": 15,
178	      "constat_detection_rate_non_rl": 0.41,
179	      "constat_detection_rate_rl": 0.12,
180	      "constat_fdr_controlled_rate": 0.28,
181	      "constat_vs_dif_overlap": 0.18,
182	      "paraphrase_quality_score": 0.73,
183	      "reformulation_difficulty_shift_mean": 0.08,
184	      "reviewer_critique": "paraphrase quality uncontrolled"
185	    },
186	    "tables": [
187	      {
188	        "name": "Table 5: ConStat vs DIF Detection Comparison",
189	        "columns": [
190	          "method",
191	          "detection_target",
192	          "rate_non_rl",
193	          "rate_rl",
194	          "per_model",
195	          "requires_cohort"
196	        ],
197	        "rows": [
198	          [
199	            "ConStat",
200	            "memorization",
201	            0.41,
202	            0.12,
203	            "Yes",
204	            "No"
205	          ],
206	          [
207	            "DIF_MH",
208	            "differential_functioning",
209	            0.313,
210	            "N/A (group-level)",
211	            "No",
212	            "Yes"
213	          ],
214	          [
215	            "overlap",
216	            "both_flag",
217	            0.18,
218	            "N/A",
219	            "-",
220	            "-"
221	          ]
222	        ]
223	      }
224	    ],
225	    "figures": [],
226	    "analysis": "ConStat comparison backfires under worst tier. It provides a foil that makes DIF look less like a contamination detector. Under reframe, this becomes irrelevant — DIF is repositioned as capability-item identifier, not competing with ConStat on contamination detection. Drop from reframed paper or move to appendix as \"related method comparison showing orthogonal signals.\"\n\n\nUnder worst tier, ConStat shows moderate detection on non-RL models (41%) — notably higher than DIF's enrichment=0.96 against contamination labels. Reviewers argue \"ConStat at least detects something correlated with memorization; DIF detects capability improvement.\" The 18% overlap between ConStat and DIF flags confirms they measure different constructs, but reviewers spin this negatively: \"DIF is orthogonal to contamination detection.\" The RL degradation (41%→12%) is expected but reviewers note \"at least ConStat provides per-model detection; DIF requires cohort structure.\" Paraphrase quality (0.73) is attacked: \"reformulations may introduce difficulty shifts (mean Δ=0.08), confounding detection.\" The entire comparison undermines DIF rather than supporting it — ConStat looks like the more direct contamination tool, and DIF looks like a capability change detector with no contamination detection ability.\n"
227	  },
228	  {
229	    "name": "dvd_generation_variance_eval",
230	    "description": "DVD generation variance evaluation on 10-15 open-weight models. 50 responses per item via temperature sampling, bimodal distribution detection for contamination.\n",
231	    "results": {
232	      "n_models": 12,
233	      "n_items_tested": 500,
234	      "dvd_bimodal_detection_rate": 0.23,
235	      "dvd_variance_auc": 0.58,
236	      "dvd_vs_dif_overlap": 0.14,
237	      "temperature_sensitivity": "high (results vary 15-30% across T=0.7 vs T=1.0)",
238	      "gpu_hours_used": 65,
239	      "generation_cost_barrier": "high",
240	      "reviewer_critique": "expensive and noisy"
241	    },
242	    "tables": [
243	      {
244	        "name": "Table 6: DVD Results Summary",
245	        "columns": [
246	          "metric",
247	          "value",
248	          "stability"
249	        ],
250	        "rows": [
251	          [
252	            "bimodal_detection_rate",
253	            0.23,
254	            "±0.09 across temperatures"
255	          ],
256	          [
257	            "variance_auc",
258	            0.58,
259	            "±0.07"
260	          ],
261	          [
262	            "dif_overlap",
263	            0.14,
264	            "stable"
265	          ],
266	          [
267	            "cost_per_model",
268	            "5.4 GPU-hrs",
269	            "fixed"
270	          ]
271	        ]
272	      }
273	    ],
274	    "figures": [],
275	    "analysis": "DVD is the weakest experiment under worst tier. Low AUC, high cost, temperature sensitivity, minimal DIF overlap. Under reframe, DVD is irrelevant — drop entirely. The capability-archaeology framing doesn't need generation variance.\n\n\nDVD shows weak detection (AUC=0.58, barely above chance) on only 12 models. The bimodal detection rate of 23% is unstable across temperature settings (15-30% variation), making the signal unreliable. Overlap with DIF is minimal (14%), confirming both methods detect different phenomena. Under worst tier, reviewers dismiss DVD as \"noisy, expensive, and only applicable to open-weight models.\" The 65 GPU-hour cost for testing 12 models × 500 items is criticized as impractical. More importantly, DVD's failure doesn't help DIF's case — reviewers note \"neither DVD nor DIF convincingly detects contamination; DIF detects capability change, DVD detects generation instability, neither detects what we actually care about.\" The experiment consumes resources without strengthening any claim.\n"
276	  },
277	  {
278	    "name": "ensemble_fusion",
279	    "description": "Fuse DIF + ConStat + DVD into multi-signal ensemble. Majority voting and weighted fusion. Cross-validate fusion weights.\n",
280	    "results": {
281	      "ensemble_2of3_precision": 0.31,
282	      "ensemble_2of3_recall": 0.15,
283	      "ensemble_weighted_auc": 0.62,
284	      "ensemble_fpr": 0.14,
285	      "uniform_weight_auc": 0.59,
286	      "optimized_weight_auc": 0.64,
287	      "cv_overfit_gap": 0.08,
288	      "dif_weight_in_optimized": 0.22,
289	      "constat_weight_in_optimized": 0.51,
290	      "dvd_weight_in_optimized": 0.27,
291	      "reviewer_critique": "ensemble of weak signals is still weak"
292	    },
293	    "tables": [
294	      {
295	        "name": "Table 7: Ensemble Performance (Worst Tier)",
296	        "columns": [
297	          "strategy",
298	          "precision",
299	          "recall",
300	          "auc",
301	          "fpr"
302	        ],
303	        "rows": [
304	          [
305	            "DIF_only",
306	            0.29,
307	            0.31,
308	            0.54,
309	            0.31
310	          ],
311	          [
312	            "ConStat_only",
313	            0.38,
314	            0.41,
315	            0.61,
316	            0.22
317	          ],
318	          [
319	            "DVD_only",
320	            0.24,
321	            0.23,
322	            0.58,
323	            0.28
324	          ],
325	          [
326	            "majority_2of3",
327	            0.31,
328	            0.15,
329	            0.55,
330	            0.14
331	          ],
332	          [
333	            "weighted_fusion_cv",
334	            0.35,
335	            0.32,
336	            0.64,
337	            0.19
338	          ]
339	        ]
340	      }
341	    ],
342	    "figures": [],
343	    "analysis": "Ensemble experiment is counterproductive under worst tier. It demonstrates DIF's weakness relative to ConStat for contamination detection. Under reframe, the entire plan_003 sequence should be dropped — the capability-archaeology paper doesn't need contamination detection ensemble. Save 150 GPU-hours.\n\n\nUnder worst tier, ensemble fusion fails to produce meaningful improvement. The 2-of-3 majority voting achieves only 15% recall because DIF, ConStat, and DVD flag largely non-overlapping items (Jaccard 0.14-0.18). Weighted fusion (AUC=0.64) barely beats uniform (0.59), and cross-validation reveals 0.08 overfit gap, suggesting the optimized weights don't generalize. Critically, DIF receives the lowest weight (0.22) in the optimized ensemble — reviewers read this as \"even the ensemble agrees DIF contributes least to contamination detection.\" The ensemble FPR of 0.14 technically meets the <0.10 target... no, it doesn't (0.14 > 0.10). Reviewers conclude: \"three individually weak contamination signals don't combine into a strong one. The fundamental problem — lack of ground truth — isn't solved by fusion.\" The entire plan_003 sequence (a+b+c) consumed 150 GPU-hours for a negative meta-result.\n"
344	  },
345	  {
346	    "name": "cross_benchmark_gsm8k",
347	    "description": "Replicate DIF on GSM8K (1,319 items × 6,702 models). Semi-synthetic validation. GSM1K contamination gap correlation as external validation.\n",
348	    "results": {
349	      "gsm8k_temporal_c_pct": 18.9,
350	      "gsm8k_semi_synthetic_delta_tpr_p10": 0.818,
351	      "gsm1k_pearson_r": -0.478,
352	      "gsm1k_pearson_p": 0.005,
353	      "gsm1k_partial_r": -0.385,
354	      "gsm1k_n_models": 33,
355	      "gsm1k_bootstrap_ci_r": [
356	        -0.71,
357	        -0.12
358	      ],
359	      "gsm1k_permutation_p": 0.014,
360	      "cook_d_max": "Deepseek-math-7b-rl",
361	      "leave_one_out_min_r": -0.374,
362	      "reviewer_reinterpretation": "anti-correlation confirms DIF=capability, not contamination"
363	    },
364	    "tables": [
365	      {
366	        "name": "Table 8: GSM1K Correlation Under Worst-Case Scrutiny",
367	        "columns": [
368	          "metric",
369	          "point_estimate",
370	          "95% CI",
371	          "reviewer_counterargument"
372	        ],
373	        "rows": [
374	          [
375	            "pearson_r",
376	            -0.478,
377	            "[-0.71, -0.12]",
378	            "CI includes near-zero; N=33 too small"
379	          ],
380	          [
381	            "partial_r",
382	            -0.385,
383	            "[-0.64, -0.04]",
384	            "Controlling accuracy weakens signal"
385	          ],
386	          [
387	            "permutation_p",
388	            0.014,
389	            "N/A",
390	            "Multiple testing not corrected"
391	          ],
392	          [
393	            "leave_one_out_min",
394	            -0.374,
395	            "N/A",
396	            "One model removal cuts 22% of effect"
397	          ]
398	        ]
399	      },
400	      {
401	        "name": "Table 9: Cross-Benchmark C% Instability",
402	        "columns": [
403	          "benchmark",
404	          "temporal_c_pct",
405	          "interpretation"
406	        ],
407	        "rows": [
408	          [
409	            "MMLU",
410	            31.3,
411	            "High instability or high capability sensitivity"
412	          ],
413	          [
414	            "GSM8K",
415	            18.9,
416	            "Lower instability — benchmark-dependent"
417	          ],
418	          [
419	            "delta",
420	            12.4,
421	            "No universal 'instability rate' — DIF is benchmark-specific"
422	          ]
423	        ]
424	      }
425	    ],
426	    "figures": [],
427	    "analysis": "The GSM1K correlation is the pivotal result. Under original framing, r=−0.478 is devastating (DIF anti-correlates with contamination). Under reframe, it becomes the HEADLINE: \"DIF identifies capability-authentic items that contamination cannot replicate.\" The wide CI (N=33) remains a vulnerability. The reframed paper should lead with this finding and frame it as: \"Contaminated models show inflated scores on non-DIF items (shallow memorization) but cannot maintain performance on DIF items (genuine capability discriminators).\" ΔTPR=0.818 is repositioned as \"calibration infrastructure\" rather than \"detection proof.\"\n\n\nUnder worst tier, the r=−0.478 result — the strongest cross-benchmark finding — is turned against the original narrative. Reviewers argue: \"DIF items anti-correlate with contamination gap. Models that are MORE contaminated (high GSM8K-GSM1K gap: Phi, Gemma) perform WORSE on DIF items. This proves DIF identifies items where genuine capability matters — contaminated models can't fake their way through these items. DIF is a capability detector, not a contamination detector.\" The bootstrap CI [-0.71, -0.12] is wide (N=33), and reviewers note \"this could be as weak as r=-0.12, barely meaningful.\" The ΔTPR=0.818 on semi-synthetic injection is dismissed: \"synthetic contamination (flipping incorrect→correct deterministically) doesn't resemble real contamination (partial memorization, shallow pattern matching). High ΔTPR on synthetic data doesn't validate real-world detection.\" The 18.9% temporal C% on GSM8K (vs 31.3% on MMLU) is spun as \"DIF flags vary wildly across benchmarks — no stable characterization.\" Deepseek-math-7b-rl as Cook's D outlier raises concerns about robustness of the correlation despite leave-one-out showing min |r|=0.374.\n"
428	  },
429	  {
430	    "name": "bifactor_irt_equating_pilot",
431	    "description": "Pilot bifactor IRT on MMLU (general factor + 57 subject factors). Anchor item selection, fixed-parameter calibration for replacement items.\n",
432	    "results": {
433	      "bifactor_convergence": false,
434	      "bifactor_rmsea": 0.11,
435	      "bifactor_cfi": 0.72,
436	      "bifactor_tli": 0.68,
437	      "n_subjects_57": 57,
438	      "n_items_12508": 12508,
439	      "n_models_5219": 5219,
440	      "anchor_items_selected": 0,
441	      "equating_rho": "N/A (model failed to converge)",
442	      "computation_time_hours": 48,
443	      "memory_peak_gb": 180,
444	      "reviewer_critique": "57-factor bifactor on 12K items is computationally intractable"
445	    },
446	    "tables": [
447	      {
448	        "name": "Table 10: Bifactor IRT Fit Diagnostics",
449	        "columns": [
450	          "metric",
451	          "value",
452	          "threshold",
453	          "verdict"
454	        ],
455	        "rows": [
456	          [
457	            "RMSEA",
458	            0.11,
459	            "<0.08",
460	            "FAIL"
461	          ],
462	          [
463	            "CFI",
464	            0.72,
465	            ">0.90",
466	            "FAIL"
467	          ],
468	          [
469	            "TLI",
470	            0.68,
471	            ">0.90",
472	            "FAIL"
473	          ],
474	          [
475	            "SRMR",
476	            0.09,
477	            "<0.08",
478	            "FAIL"
479	          ],
480	          [
481	            "convergence",
482	            "No (48h timeout)",
483	            "Yes",
484	            "FAIL"
485	          ],
486	          [
487	            "n_parameters",
488	            "~25,000",
489	            "<5,000 practical",
490	            "FAIL"
491	          ]
492	        ]
493	      }
494	    ],
495	    "figures": [],
496	    "analysis": "Bifactor failure is expected and, under worst tier, becomes evidence that MMLU is fundamentally unsuitable for IRT-based psychometric analysis. Reviewers cite this as proof that \"applying unidimensional psychometric methods to a 57-subject multidimensional benchmark is methodologically invalid.\" Under reframe, this is acknowledged honestly in limitations: \"MMLU's multidimensional structure exceeds current IRT modeling capacity; our within-subject analysis (plan_014) partially addresses this but doesn't eliminate the concern.\" Drop the equating pipeline entirely.\n\n\nUnder worst tier, bifactor IRT fails catastrophically. The 57-subject structure of MMLU means a bifactor model requires estimating 1 general + 57 specific factors — a 58-dimensional latent space with ~25,000 item parameters. This exceeds practical computational limits (180GB RAM, 48 hours without convergence). Even if forced to converge with simplifications (e.g., constraining factor loadings), fit indices are poor: RMSEA=0.11 (>0.08 threshold), CFI=0.72 (<0.90 threshold), TLI=0.68 (<0.90). The unidimensionality assumption underlying MH-DIF is confirmed as violated, but the alternative (bifactor) is intractable. Reviewers argue: \"You've demonstrated that the psychometric foundation of your method is inappropriate for MMLU, but provided no working alternative. Multidimensional DIF methods exist (MIMIC, MIRT-DIF) but you haven't implemented them.\" Anchor item selection fails because the bifactor model didn't converge — no equating is possible. The entire regeneration pipeline (plan_005 → plan_006 → plan_008) collapses at step one.\n"
497	  },
498	  {
499	    "name": "item_generation_calibration",
500	    "description": "Generate replacement items for DIF-flagged questions. LLM generation with construct constraints, student simulation calibration, difficulty correlation validation.\n",
501	    "results": {
502	      "n_items_generated": 300,
503	      "n_subjects_covered": 15,
504	      "difficulty_correlation_prompt": 0.18,
505	      "difficulty_correlation_student_sim": 0.34,
506	      "cognitive_level_match_rate": 0.45,
507	      "item_quality_human_eval": 0.61,
508	      "construct_alignment_score": 0.53,
509	      "holdout_panel_rho": 0.42,
510	      "gpu_hours_used": 180,
511	      "reviewer_critique": "difficulty calibration too weak for operational use"
512	    },
513	    "tables": [
514	      {
515	        "name": "Table 11: Item Generation Calibration Failure",
516	        "columns": [
517	          "calibration_method",
518	          "difficulty_rho",
519	          "claimed_in_literature",
520	          "achieved"
521	        ],
522	        "rows": [
523	          [
524	            "prompt_targeting",
525	            0.18,
526	            "0.10-0.45",
527	            "Low end"
528	          ],
529	          [
530	            "student_simulation",
531	            0.34,
532	            "0.75-0.82",
533	            "Far below"
534	          ],
535	          [
536	            "holdout_validation",
537	            0.42,
538	            ">0.90 needed",
539	            "Insufficient"
540	          ]
541	        ]
542	      }
543	    ],
544	    "figures": [],
545	    "analysis": "Item generation is the most expensive failure (180 GPU-hrs). Under worst tier, it actively undermines the paper — reviewers use it to argue \"you can't replace DIF items, and you've shown DIF items don't affect rankings (ρ=0.997), so what's the practical value?\" Under reframe, this experiment should not be run at all. The capability-archaeology paper frames DIF items as valuable signal carriers, not problems to be replaced. Save the 200 GPU-hour budget.\n\n\nUnder worst tier, item generation produces mediocre results. Prompt-based difficulty targeting yields ρ=0.18 (consistent with literature range 0.10-0.45 from arXiv 2602.06631 — on the low end). Student simulation calibration improves to ρ=0.34 but still far below the r=0.75-0.82 claimed in arXiv 2601.09953 — the discrepancy arises because student simulation was validated on simple math items, not MMLU's diverse knowledge domains. Cognitive level matching (45%) means over half of replacement items test different cognitive processes than originals. Construct alignment (53%) is poor — reviewers argue \"replacing items with construct-misaligned substitutes invalidates the benchmark more than the DIF items did.\" The holdout panel validation (ρ=0.42) shows replacement items don't preserve model rankings. Reviewers conclude: \"The cure is worse than the disease — DIF-flagged items at least produce stable rankings (ρ=0.997); replacements introduce genuine measurement error.\" 180 GPU-hours consumed for a negative result. Under reframe, this experiment is dropped entirely — the capability-archaeology paper doesn't need item replacement.\n"
546	  },
547	  {
548	    "name": "cumulative_bayesian_dif",
549	    "description": "Implement cumulative Bayesian DIF priors (Sinharay et al., 2006). Simulate 4 successive administrations. Show power improvement from evidence accumulation.\n",
550	    "results": {
551	      "single_admin_power_d10": 0.38,
552	      "cumulative_2_admin_power_d10": 0.49,
553	      "cumulative_3_admin_power_d10": 0.58,
554	      "cumulative_4_admin_power_d10": 0.64,
555	      "single_admin_fpr": 0.05,
556	      "cumulative_4_admin_fpr": 0.11,
557	      "fpr_inflation_per_admin": 0.02,
558	      "convergence_rate": 0.92,
559	      "reviewer_critique": "cumulative FPR inflation makes this impractical"
560	    },
561	    "tables": [
562	      {
563	        "name": "Table 12: Cumulative Bayesian DIF Power Trajectory",
564	        "columns": [
565	          "n_administrations",
566	          "tpr_d10",
567	          "tpr_d14",
568	          "fpr",
569	          "net_power_gain"
570	        ],
571	        "rows": [
572	          [
573	            1,
574	            0.38,
575	            0.68,
576	            0.05,
577	            "baseline"
578	          ],
579	          [
580	            2,
581	            0.49,
582	            0.78,
583	            0.07,
584	            "+0.11/+0.10"
585	          ],
586	          [
587	            3,
588	            0.58,
589	            0.84,
590	            0.09,
591	            "+0.09/+0.06"
592	          ],
593	          [
594	            4,
595	            0.64,
596	            0.87,
597	            0.11,
598	            "+0.06/+0.03"
599	          ]
600	        ]
601	      }
602	    ],
603	    "figures": [],
604	    "analysis": "Cumulative Bayesian is theoretically elegant but practically undermined by FPR inflation. Under worst tier, it's a distraction — reviewers see diminishing returns and growing false positives. Under reframe, it has modest value as \"longitudinal capability tracking infrastructure\" but is not central. Recommend moving to appendix or future work.\n\n\nUnder worst tier, cumulative Bayesian DIF shows power improvement (0.38→0.64 over 4 administrations for medium effects δ=1.0) but fails to reach the 0.70 target from the plan description. More critically, FPR inflates from 0.05 to 0.11 across 4 administrations — each administration's prior carries forward false positive evidence. Reviewers argue: \"With baseline FPR already at 31% in real data (plan_001), cumulative approaches will amplify false positives. You're accumulating evidence that items changed function — but we've established this is capability improvement, not contamination. You're building a more powerful detector of the wrong thing.\" The simulation uses idealized conditions (known item parameters, controlled drift) that don't match real MMLU conditions. Under reframe, this becomes interesting — \"cumulative tracking of capability-sensitive items across model generations\" — but the FPR inflation concern remains.\n"
605	  },
606	  {
607	    "name": "graceful_degradation_analysis",
608	    "description": "Formal analysis of benchmark validity under progressive item replacement (5%-50%). Validity metrics, theoretical bounds, empirical validation.\n",
609	    "results": {
610	      "rho_at_5pct_replacement": 0.998,
611	      "rho_at_10pct_replacement": 0.996,
612	      "rho_at_20pct_replacement": 0.991,
613	      "rho_at_50pct_replacement": 0.972,
614	      "reliability_alpha_original": 0.94,
615	      "reliability_alpha_50pct_replaced": 0.88,
616	      "construct_coverage_original": 57,
617	      "construct_coverage_50pct_replaced": 52,
618	      "theoretical_bound_rho_min": 0.95,
619	      "replacement_rate_at_bound": 0.38,
620	      "reviewer_critique": "confirms DIF removal doesn't matter"
621	    },
622	    "tables": [
623	      {
624	        "name": "Table 13: Graceful Degradation Curves",
625	        "columns": [
626	          "replacement_pct",
627	          "rank_rho",
628	          "reliability_alpha",
629	          "subjects_covered",
630	          "verdict"
631	        ],
632	        "rows": [
633	          [
634	            0,
635	            1.0,
636	            0.94,
637	            57,
638	            "baseline"
639	          ],
640	          [
641	            5,
642	            0.998,
643	            0.93,
644	            57,
645	            "negligible"
646	          ],
647	          [
648	            10,
649	            0.996,
650	            0.93,
651	            57,
652	            "negligible"
653	          ],
654	          [
655	            20,
656	            0.991,
657	            0.91,
658	            56,
659	            "minor"
660	          ],
661	          [
662	            31,
663	            0.987,
664	            0.9,
665	            55,
666	            "DIF removal point"
667	          ],
668	          [
669	            50,
670	            0.972,
671	            0.88,
672	            52,
673	            "still acceptable"
674	          ]
675	        ]
676	      }
677	    ],
678	    "figures": [],
679	    "analysis": "Graceful degradation is self-defeating under worst tier AND original framing. It proves removing DIF items doesn't matter, undermining significance. Under reframe, this becomes: \"MMLU is 3× larger than needed for stable rankings — DIF identifies the informative core (the items that DO contribute discriminative signal).\" The ρ=0.972 at 50% replacement becomes \"you could cut MMLU in half and preserve rankings — DIF tells you which half to keep.\" This is actually a strong reframe, turning the worst finding into a measurement efficiency contribution.\n\n\nUnder worst tier, graceful degradation analysis confirms the ρ=0.997 finding from plan_017 — removing/replacing up to 50% of items barely affects rankings (ρ=0.972). Reviewers weaponize this: \"Even replacing HALF the benchmark changes rankings by less than 3%. This proves MMLU is massively redundant, and DIF-flagged items are redundant too. Why should anyone care about 31% item instability if it doesn't affect rankings?\" Reliability drops from 0.94 to 0.88 at 50% replacement, but remains above acceptable thresholds (0.70). Construct coverage loses 5 of 57 subjects at 50% replacement — reviewers note \"acceptable.\" The theoretical bound (ρ≥0.95 up to 38% replacement) perfectly matches the DIF flagging rate (31.3%), which reviewers read as \"you can safely ignore everything DIF flags.\" This experiment depends on plan_005/006 (which fail), so the \"replacement\" is simulated via random item substitution rather than actual generated items — further reducing credibility.\n"
680	  },
681	  {
682	    "name": "item_focused_trees",
683	    "description": "Item-Focused Trees (Tutz & Berger, 2016) as alternative to categorical cohort DIF. Continuous covariate (release date). Compare detection power vs categorical MH.\n",
684	    "results": {
685	      "ift_detection_rate": 0.34,
686	      "ift_vs_mh_overlap": 0.78,
687	      "ift_unique_flags": 0.06,
688	      "mh_unique_flags": 0.04,
689	      "ift_uses_full_sample": true,
690	      "ift_avoids_cohort_splits": true,
691	      "ift_computational_cost_ratio": 12.0,
692	      "ift_release_date_coefficient_mean": 0.08,
693	      "ift_release_date_coefficient_std": 0.15,
694	      "reviewer_critique": "confirms temporal trend = capability gain"
695	    },
696	    "tables": [
697	      {
698	        "name": "Table 14: IFT vs MH Comparison",
699	        "columns": [
700	          "method",
701	          "flagging_rate",
702	          "unique_flags",
703	          "cost_ratio",
704	          "temporal_pattern"
705	        ],
706	        "rows": [
707	          [
708	            "MH_categorical",
709	            0.313,
710	            0.04,
711	            1.0,
712	            "Discrete cohort split"
713	          ],
714	          [
715	            "IFT_continuous",
716	            0.34,
717	            0.06,
718	            12.0,
719	            "Smooth positive trend"
720	          ],
721	          [
722	            "overlap",
723	            0.78,
724	            "-",
725	            "-",
726	            "Same underlying signal"
727	          ]
728	        ]
729	      }
730	    ],
731	    "figures": [],
732	    "analysis": "IFT provides marginal methodological value but under worst tier confirms the capability-improvement interpretation via smooth temporal trends. Under reframe, the smooth trend is actually interesting: \"capability-authentic items show predictable sensitivity to model generation — enabling prospective identification of items that will become less discriminative.\" Recommend as supplementary/appendix rather than main paper contribution.\n\n\nUnder worst tier, Item-Focused Trees detect 34% of items as having significant temporal DIF — nearly identical to MH's 31.3%. The 78% overlap confirms both methods detect the same phenomenon. The IFT release-date coefficient (mean=0.08, SD=0.15) is positive: items become easier over time, consistent with capability improvement. Reviewers read the continuous coefficient as: \"DIF is a smooth function of time, not a discrete shift — this is exactly what capability improvement looks like. If contamination caused DIF, we'd expect discrete jumps when specific training data became available.\" The 12× computational cost over MH makes IFT impractical at scale. Reviewers conclude: \"IFT confirms MH findings but adds computational cost and the interpretation that item changes are gradual (capability) not abrupt (contamination).\"\n"
733	  },
734	  {
735	    "name": "architecture_stratified_dif",
736	    "description": "DIF within decoder-only homogeneous subpopulation. IRT fit diagnostics. Compare FPR/TPR vs full-population DIF from plan_001.\n",
737	    "results": {
738	      "n_decoder_only": 3400,
739	      "decoder_only_c_pct": 33.1,
740	      "decoder_only_irt_rmsea": 0.092,
741	      "decoder_only_irt_cfi": 0.81,
742	      "decoder_only_irt_tli": 0.78,
743	      "decoder_only_irt_srmr": 0.073,
744	      "full_population_c_pct": 31.3,
745	      "delta_c_pct": 1.8,
746	      "fpr_decoder_only": 0.33,
747	      "fpr_full_population": 0.318,
748	      "tpr_delta_p05": -0.02,
749	      "reviewer_critique": "architecture homogeneity doesn't fix the problem"
750	    },
751	    "tables": [
752	      {
753	        "name": "Table 15: Architecture Stratification Results",
754	        "columns": [
755	          "population",
756	          "n_models",
757	          "c_pct",
758	          "rmsea",
759	          "cfi",
760	          "tli"
761	        ],
762	        "rows": [
763	          [
764	            "full_population",
765	            5219,
766	            31.3,
767	            "N/A (not computed)",
768	            "N/A",
769	            "N/A"
770	          ],
771	          [
772	            "decoder_only",
773	            3400,
774	            33.1,
775	            0.092,
776	            0.81,
777	            0.78
778	          ],
779	          [
780	            "delta",
781	            "-1819",
782	            "+1.8",
783	            "FAIL (>0.08)",
784	            "FAIL (<0.90)",
785	            "FAIL (<0.90)"
786	          ]
787	        ]
788	      },
789	      {
790	        "name": "Table 16: Detection Power Comparison",
791	        "columns": [
792	          "population",
793	          "fpr_baseline",
794	          "tpr_p05",
795	          "tpr_p10",
796	          "enrichment"
797	        ],
798	        "rows": [
799	          [
800	            "full_population",
801	            0.318,
802	            0.834,
803	            1.0,
804	            0.96
805	          ],
806	          [
807	            "decoder_only",
808	            0.33,
809	            0.82,
810	            0.99,
811	            0.95
812	          ],
813	          [
814	            "delta",
815	            "+0.012",
816	            "-0.014",
817	            "-0.01",
818	            "-0.01"
819	          ]
820	        ]
821	      }
822	    ],
823	    "figures": [],
824	    "analysis": "Architecture stratification is the critical missing experiment identified by worst-case Dream, and it produces the predicted negative result. Under worst tier, this closes the last escape route: DIF flagging rates cannot be reduced by controlling for architecture. The IRT misfit is structural (MMLU dimensionality) not population-driven. Under reframe, this becomes neutral: \"DIF item sensitivity is robust to population composition — capability-authentic items are identified regardless of architecture mix.\" The IRT fit concern is acknowledged honestly but framed as \"conservative: poor IRT fit means DIF may UNDERESTIMATE the true proportion of capability-sensitive items.\"\n\n\nUnder worst tier (explicitly specified in tier definition), architecture stratification fails to improve results. Decoder-only C% = 33.1% (vs 31.3% full population) — no meaningful reduction, slightly HIGHER. IRT fit remains poor: RMSEA=0.092 (>0.08), CFI=0.81 (<0.90), TLI=0.78 (<0.90). Removing encoder-decoder and hybrid architectures doesn't address the fundamental unidimensionality problem — MMLU's 57-subject structure violates unidimensional IRT regardless of architecture homogeneity. The C% increase from 31.3%→33.1% is within noise but reviewers spin it: \"architecture stratification made things WORSE — DIF flags more items in a homogeneous population, confirming that flags reflect capability variation, not architecture confounding.\" FPR and TPR are essentially unchanged (ΔFPR=+0.01, ΔTPR=−0.02). Reviewers familiar with psychometrics argue: \"RMSEA=0.092 on decoder-only models proves the IRT model is misspecified for MMLU. Your entire DIF analysis rests on an inappropriate measurement model. This is not fixable by subsetting — it requires multidimensional IRT, which you haven't implemented.\"\n"
825	  },
826	  {
827	    "name": "semi_synthetic_contamination_validation",
828	    "description": "Inject known contamination into METABENCH response matrix. Measure DIF TPR/FPR against controlled ground truth. Vary injection parameters.\n",
829	    "results": {
830	      "delta_tpr_p03": 0.222,
831	      "delta_tpr_p05": 0.508,
832	      "delta_tpr_p07": 0.664,
833	      "delta_tpr_p10": 0.674,
834	      "external_matching_fpr": 0.314,
835	      "within_matching_fpr_inflation": 0.186,
836	      "cross_subject_delta_fpr": 0.0,
837	      "cross_subject_delta_tpr_p05_avg": 0.36,
838	      "dose_response_present": true,
839	      "reviewer_critique": "synthetic injection mechanism unrealistic"
840	    },
841	    "tables": [
842	      {
843	        "name": "Table 17: Semi-Synthetic Results Under Worst Interpretation",
844	        "columns": [
845	          "injection_rate_p",
846	          "delta_tpr_standard",
847	          "delta_tpr_cross_subject",
848	          "reviewer_spin"
849	        ],
850	        "rows": [
851	          [
852	            0.3,
853	            0.222,
854	            0.18,
855	            "Below useful detection"
856	          ],
857	          [
858	            0.5,
859	            0.508,
860	            0.36,
861	            "Only works at 50%+ exploitation"
862	          ],
863	          [
864	            0.7,
865	            0.664,
866	            0.52,
867	            "High exploitation = easy detection"
868	          ],
869	          [
870	            1.0,
871	            0.674,
872	            0.62,
873	            "Saturates — ceiling effect"
874	          ]
875	        ]
876	      },
877	      {
878	        "name": "Table 18: Matching Strategy Comparison",
879	        "columns": [
880	          "matching",
881	          "fpr_baseline",
882	          "fpr_at_p10",
883	          "delta_fpr",
884	          "verdict"
885	        ],
886	        "rows": [
887	          [
888	            "standard_MH",
889	            0.298,
890	            0.616,
891	            "+0.318",
892	            "FPR inflates (contaminated matching var)"
893	          ],
894	          [
895	            "external_5subj",
896	            0.314,
897	            0.314,
898	            0.0,
899	            "FPR stable (clean matching var)"
900	          ],
901	          [
902	            "cross_subject",
903	            0.33,
904	            0.33,
905	            0.0,
906	            "FPR stable (recommended)"
907	          ]
908	        ]
909	      }
910	    ],
911	    "figures": [],
912	    "analysis": "Semi-synthetic validation is the strongest methodological contribution even under worst tier. The cross-subject matching innovation (ΔFPR=0.000) is genuinely novel and useful. Under reframe, the semi-synthetic framework is repositioned as \"calibration infrastructure for item sensitivity analysis\" — it characterizes how much differential signal is needed before DIF detects it, without claiming this maps to real contamination. The dose-response curve becomes \"sensitivity calibration\" rather than \"contamination detection power.\" This experiment survives the reframe relatively intact.\n\nUnder worst tier, semi-synthetic results (already observed) are technically sound but dismissed on ecological validity grounds. ΔTPR=0.508 at p=0.5 shows DIF detects injected contamination — but reviewers argue the injection mechanism (flip incorrect→correct with probability p) doesn't model real contamination. Real contamination involves: (1) partial memorization (model recalls fragments, not full answers), (2) shallow pattern matching (model exploits surface features), (3) chain-of-thought reasoning from memorized premises. None of these produce the clean incorrect→correct flipping that synthetic injection assumes. The dose-response curve (ΔTPR increases with p) is called \"trivially expected — of course flipping more answers makes items behave more differently.\" The cross- subject matching innovation (ΔFPR=0.000) is acknowledged as methodologically sound, but reviewers argue \"you've built a valid framework for detecting something that doesn't exist in the real world in this form.\" The gap between synthetic ΔTPR=0.508 and real enrichment=0.96 is the fatal disconnect: \"Your method works perfectly on synthetic contamination and not at all on real data — this means your synthetic model is wrong, not that your ground truth is wrong.\"\n"
913	  }
914	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c0cfcfe-7766-4c3a-94dd-8822bb8ae22d",
  "isSidechain": false,
  "promptId": "41166657-dacb-41c2-9c9f-045334e8b1ff",
  "type": "user",
  "uuid": "24cba543-cf46-4cb5-a094-cb93a326404e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"real_data_dif_mmlu\",\n    \"description\": \"Apply MH DIF to METABENCH MMLU 5,219×12,508 matrix. Temporal cohort (2023 vs 2024-H1), ability-quintile cohort, within-family confound control, domain-specificity analysis.\\n\",\n    \"results\": {\n      \"temporal_ets_c_pct\": 31.3,\n      \"temporal_fpr_li_clean\": 0.318,\n      \"temporal_enrichment\": 0.96,\n      \"ability_ets_c_pct\": 2.9,\n      \"within_family_llama2v3_c_pct\": 61.3,\n      \"domain_spearman_rho\": 0.307,\n      \"domain_spearman_p\": 0.02,\n      \"sanity_random_split_c_pct\": 0.18,\n      \"reviewer_interpretation\": \"capability_gain_detector\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: DIF Detection Summary Under Worst Interpretation\",\n        \"columns\": [\n          \"cohort_definition\",\n          \"c_pct\",\n          \"enrichment_vs_li\",\n          \"reviewer_counterargument\"\n        ],\n        \"rows\": [\n          [\n            \"temporal_2023_vs_2024\",\n            31.3,\n            0.96,\n            \"Capability gain across generations\"\n          ],\n          [\n            \"ability_quintile\",\n            2.9,\n            1.19,\n            \"Minimal DIF = items function consistently across ability levels (expected)\"\n          ],\n          [\n            \"within_family_llama2v3\",\n            61.3,\n            \"N/A\",\n            \"Same family, same data pipeline → pure capability gain\"\n          ],\n          [\n            \"random_split_sanity\",\n            0.18,\n            \"N/A\",\n            \"Confirms real signal, but signal = capability\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Domain Correlation Detail\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"reviewer_spin\"\n        ],\n        \"rows\": [\n          [\n            \"spearman_rho_dif_vs_accuracy_gain\",\n            0.307,\n            \"DIF tracks capability improvement\"\n          ],\n          [\n            \"p_value\",\n            0.02,\n            \"Significant correlation confirms confound\"\n          ],\n          [\n            \"variance_explained\",\n            \"9.4%\",\n            \"Remainder is noise, not contamination signal\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The plan_001 results are empirically sound but narratively fatal under worst tier. The reframe salvages them: 31.3% \\\"instability\\\" becomes \\\"31% of items are capability- sensitive — they differentiate model generations.\\\" ρ=0.307 becomes evidence that DIF identifies items where genuine capability improvement concentrates. Enrichment=0.96 is reframed as \\\"DIF and contamination labels measure orthogonal constructs — DIF captures differential item functioning, not data leakage.\\\" The within-family result becomes the strongest evidence FOR the reframe: even within Llama family, DIF identifies where architectural/training improvements manifest at the item level.\\n\\n\\nUnder worst tier, the actual results hold (these are already observed) but their interpretation collapses. ρ=0.307 (p=0.02) correlating DIF flags with domain-level accuracy improvement is seized by reviewers as causal evidence: items flagged by DIF are simply items where models improved. Enrichment=0.96 against Li et al. labels confirms zero relationship to contamination — reviewers read this as \\\"DIF doesn't detect contamination at all.\\\" The 61.3% within-family Llama-2-vs-3 C% is devastating: within the same family (same training pipeline, likely same data), DIF flags 61% of items, which reviewers attribute entirely to capability gain between generations. The sanity check (0.18%) proves DIF detects *something* real, but reviewers argue that \\\"something\\\" is capability improvement, not benchmark pathology. The meta-critique about Li et al. labels is dismissed: \\\"You haven't provided ANY ground truth showing DIF detects contamination — enrichment=0.96 is your only validation, and it failed.\\\"\\n\"\n  },\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"Validate DIF robustness to RL training. Alignment-RL (DPO/ORPO, N=477) and reasoning-RL (GRPO/PPO, N≈13) cohorts. Compare DIF vs Min-K%/ConStat per-model degradation. Power analysis for partial exploitation.\\n\",\n    \"results\": {\n      \"n_reasoning_rl_models\": 13,\n      \"dif_flag_overlap_sft_vs_alignment_rl\": 0.82,\n      \"dif_flag_overlap_sft_vs_reasoning_rl\": 0.71,\n      \"mink_auroc_sft\": 0.63,\n      \"mink_auroc_alignment_rl\": 0.58,\n      \"mink_auroc_reasoning_rl\": 0.44,\n      \"constat_auroc_sft\": 0.67,\n      \"constat_auroc_reasoning_rl\": 0.51,\n      \"dif_tpr_with_rl_in_cohort\": 0.65,\n      \"dif_tpr_without_rl_in_cohort\": 0.68,\n      \"bootstrap_ci_overlap\": true,\n      \"delong_p_dif_vs_constat\": 0.23,\n      \"tost_equivalence_p\": 0.34,\n      \"partial_exploitation_detection_boundary\": 0.55,\n      \"reviewer_score\": 4.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: RL Robustness Comparison (Underpowered)\",\n        \"columns\": [\n          \"method\",\n          \"sft_auroc\",\n          \"alignment_rl_auroc\",\n          \"reasoning_rl_auroc\",\n          \"95% CI width\"\n        ],\n        \"rows\": [\n          [\n            \"DIF_MH\",\n            0.69,\n            0.66,\n            0.65,\n            \"±0.14\"\n          ],\n          [\n            \"Min-K%\",\n            0.63,\n            0.58,\n            0.44,\n            \"±0.18\"\n          ],\n          [\n            \"ConStat\",\n            0.67,\n            0.61,\n            0.51,\n            \"±0.16\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: Statistical Tests (All Non-Significant)\",\n        \"columns\": [\n          \"comparison\",\n          \"test\",\n          \"statistic\",\n          \"p_value\",\n          \"conclusion\"\n        ],\n        \"rows\": [\n          [\n            \"DIF_vs_ConStat_RL\",\n            \"DeLong\",\n            \"z=1.19\",\n            0.23,\n            \"Cannot reject H0\"\n          ],\n          [\n            \"DIF_retention_equivalence\",\n            \"TOST\",\n            \"t=0.96\",\n            0.34,\n            \"Cannot claim equivalence\"\n          ],\n          [\n            \"flag_overlap_SFT_vs_RL\",\n            \"Bootstrap Jaccard\",\n            0.71,\n            \"CI [0.54, 0.88]\",\n            \"Wide CI, inconclusive\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Experiment is fatally underpowered. N=13 reasoning-RL models cannot support any statistical claim. Under worst tier, this becomes ammunition: \\\"authors claim RL robustness but provide no evidence.\\\" Reframe option: drop RL robustness as a claim entirely, acknowledge in limitations, reposition the alignment-RL (N=477) result as \\\"DIF is stable across training objective variations\\\" without claiming reasoning-RL coverage. Under the capability-archaeology reframe, RL robustness is less central anyway — the question becomes \\\"do capability-authentic items remain stable across training paradigms?\\\" which is interesting but not load-bearing.\\n\\n\\nWith only N=13 reasoning-RL models, no comparison reaches statistical significance. DIF flag overlap between SFT and RL-containing cohorts is 71%, which reviewers dismiss as \\\"you can't distinguish robustness from noise with N=13.\\\" The DeLong test p=0.23 means we cannot claim DIF outperforms ConStat. TOST equivalence test fails (p=0.34 > 0.05) — we can't even claim equivalence. Min-K% drops to 0.44 AUROC on reasoning-RL models, but reviewers note \\\"you're comparing DIF (group-level, N=477 cohort) against per-model detectors on 13 models — apples to oranges.\\\" The partial exploitation analysis shows detection boundary at p=0.55, meaning DIF misses contamination below 55% exploitation rate — reviewers call this \\\"DIF only detects extreme contamination, which is also detectable by simpler methods.\\\" The entire experiment is underpowered and reviewers recommend \\\"defer until more GRPO/PPO models exist on public leaderboards.\\\"\\n\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"Independent ConStat-style perturbation evaluation on 200+ MMLU items. Generate semantic reformulations, compare original vs reformulated performance, apply FDR-controlled detection.\\n\",\n    \"results\": {\n      \"n_items_reformulated\": 220,\n      \"n_models_tested\": 15,\n      \"constat_detection_rate_non_rl\": 0.41,\n      \"constat_detection_rate_rl\": 0.12,\n      \"constat_fdr_controlled_rate\": 0.28,\n      \"constat_vs_dif_overlap\": 0.18,\n      \"paraphrase_quality_score\": 0.73,\n      \"reformulation_difficulty_shift_mean\": 0.08,\n      \"reviewer_critique\": \"paraphrase quality uncontrolled\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: ConStat vs DIF Detection Comparison\",\n        \"columns\": [\n          \"method\",\n          \"detection_target\",\n          \"rate_non_rl\",\n          \"rate_rl\",\n          \"per_model\",\n          \"requires_cohort\"\n        ],\n        \"rows\": [\n          [\n            \"ConStat\",\n            \"memorization\",\n            0.41,\n            0.12,\n            \"Yes\",\n            \"No\"\n          ],\n          [\n            \"DIF_MH\",\n            \"differential_functioning\",\n            0.313,\n            \"N/A (group-level)\",\n            \"No\",\n            \"Yes\"\n          ],\n          [\n            \"overlap\",\n            \"both_flag\",\n            0.18,\n            \"N/A\",\n            \"-\",\n            \"-\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ConStat comparison backfires under worst tier. It provides a foil that makes DIF look less like a contamination detector. Under reframe, this becomes irrelevant — DIF is repositioned as capability-item identifier, not competing with ConStat on contamination detection. Drop from reframed paper or move to appendix as \\\"related method comparison showing orthogonal signals.\\\"\\n\\n\\nUnder worst tier, ConStat shows moderate detection on non-RL models (41%) — notably higher than DIF's enrichment=0.96 against contamination labels. Reviewers argue \\\"ConStat at least detects something correlated with memorization; DIF detects capability improvement.\\\" The 18% overlap between ConStat and DIF flags confirms they measure different constructs, but reviewers spin this negatively: \\\"DIF is orthogonal to contamination detection.\\\" The RL degradation (41%→12%) is expected but reviewers note \\\"at least ConStat provides per-model detection; DIF requires cohort structure.\\\" Paraphrase quality (0.73) is attacked: \\\"reformulations may introduce difficulty shifts (mean Δ=0.08), confounding detection.\\\" The entire comparison undermines DIF rather than supporting it — ConStat looks like the more direct contamination tool, and DIF looks like a capability change detector with no contamination detection ability.\\n\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"DVD generation variance evaluation on 10-15 open-weight models. 50 responses per item via temperature sampling, bimodal distribution detection for contamination.\\n\",\n    \"results\": {\n      \"n_models\": 12,\n      \"n_items_tested\": 500,\n      \"dvd_bimodal_detection_rate\": 0.23,\n      \"dvd_variance_auc\": 0.58,\n      \"dvd_vs_dif_overlap\": 0.14,\n      \"temperature_sensitivity\": \"high (results vary 15-30% across T=0.7 vs T=1.0)\",\n      \"gpu_hours_used\": 65,\n      \"generation_cost_barrier\": \"high\",\n      \"reviewer_critique\": \"expensive and noisy\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: DVD Results Summary\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"stability\"\n        ],\n        \"rows\": [\n          [\n            \"bimodal_detection_rate\",\n            0.23,\n            \"±0.09 across temperatures\"\n          ],\n          [\n            \"variance_auc\",\n            0.58,\n            \"±0.07\"\n          ],\n          [\n            \"dif_overlap\",\n            0.14,\n            \"stable\"\n          ],\n          [\n            \"cost_per_model\",\n            \"5.4 GPU-hrs\",\n            \"fixed\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DVD is the weakest experiment under worst tier. Low AUC, high cost, temperature sensitivity, minimal DIF overlap. Under reframe, DVD is irrelevant — drop entirely. The capability-archaeology framing doesn't need generation variance.\\n\\n\\nDVD shows weak detection (AUC=0.58, barely above chance) on only 12 models. The bimodal detection rate of 23% is unstable across temperature settings (15-30% variation), making the signal unreliable. Overlap with DIF is minimal (14%), confirming both methods detect different phenomena. Under worst tier, reviewers dismiss DVD as \\\"noisy, expensive, and only applicable to open-weight models.\\\" The 65 GPU-hour cost for testing 12 models × 500 items is criticized as impractical. More importantly, DVD's failure doesn't help DIF's case — reviewers note \\\"neither DVD nor DIF convincingly detects contamination; DIF detects capability change, DVD detects generation instability, neither detects what we actually care about.\\\" The experiment consumes resources without strengthening any claim.\\n\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"Fuse DIF + ConStat + DVD into multi-signal ensemble. Majority voting and weighted fusion. Cross-validate fusion weights.\\n\",\n    \"results\": {\n      \"ensemble_2of3_precision\": 0.31,\n      \"ensemble_2of3_recall\": 0.15,\n      \"ensemble_weighted_auc\": 0.62,\n      \"ensemble_fpr\": 0.14,\n      \"uniform_weight_auc\": 0.59,\n      \"optimized_weight_auc\": 0.64,\n      \"cv_overfit_gap\": 0.08,\n      \"dif_weight_in_optimized\": 0.22,\n      \"constat_weight_in_optimized\": 0.51,\n      \"dvd_weight_in_optimized\": 0.27,\n      \"reviewer_critique\": \"ensemble of weak signals is still weak\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Ensemble Performance (Worst Tier)\",\n        \"columns\": [\n          \"strategy\",\n          \"precision\",\n          \"recall\",\n          \"auc\",\n          \"fpr\"\n        ],\n        \"rows\": [\n          [\n            \"DIF_only\",\n            0.29,\n            0.31,\n            0.54,\n            0.31\n          ],\n          [\n            \"ConStat_only\",\n            0.38,\n            0.41,\n            0.61,\n            0.22\n          ],\n          [\n            \"DVD_only\",\n            0.24,\n            0.23,\n            0.58,\n            0.28\n          ],\n          [\n            \"majority_2of3\",\n            0.31,\n            0.15,\n            0.55,\n            0.14\n          ],\n          [\n            \"weighted_fusion_cv\",\n            0.35,\n            0.32,\n            0.64,\n            0.19\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ensemble experiment is counterproductive under worst tier. It demonstrates DIF's weakness relative to ConStat for contamination detection. Under reframe, the entire plan_003 sequence should be dropped — the capability-archaeology paper doesn't need contamination detection ensemble. Save 150 GPU-hours.\\n\\n\\nUnder worst tier, ensemble fusion fails to produce meaningful improvement. The 2-of-3 majority voting achieves only 15% recall because DIF, ConStat, and DVD flag largely non-overlapping items (Jaccard 0.14-0.18). Weighted fusion (AUC=0.64) barely beats uniform (0.59), and cross-validation reveals 0.08 overfit gap, suggesting the optimized weights don't generalize. Critically, DIF receives the lowest weight (0.22) in the optimized ensemble — reviewers read this as \\\"even the ensemble agrees DIF contributes least to contamination detection.\\\" The ensemble FPR of 0.14 technically meets the <0.10 target... no, it doesn't (0.14 > 0.10). Reviewers conclude: \\\"three individually weak contamination signals don't combine into a strong one. The fundamental problem — lack of ground truth — isn't solved by fusion.\\\" The entire plan_003 sequence (a+b+c) consumed 150 GPU-hours for a negative meta-result.\\n\"\n  },\n  {\n    \"name\": \"cross_benchmark_gsm8k\",\n    \"description\": \"Replicate DIF on GSM8K (1,319 items × 6,702 models). Semi-synthetic validation. GSM1K contamination gap correlation as external validation.\\n\",\n    \"results\": {\n      \"gsm8k_temporal_c_pct\": 18.9,\n      \"gsm8k_semi_synthetic_delta_tpr_p10\": 0.818,\n      \"gsm1k_pearson_r\": -0.478,\n      \"gsm1k_pearson_p\": 0.005,\n      \"gsm1k_partial_r\": -0.385,\n      \"gsm1k_n_models\": 33,\n      \"gsm1k_bootstrap_ci_r\": [\n        -0.71,\n        -0.12\n      ],\n      \"gsm1k_permutation_p\": 0.014,\n      \"cook_d_max\": \"Deepseek-math-7b-rl\",\n      \"leave_one_out_min_r\": -0.374,\n      \"reviewer_reinterpretation\": \"anti-correlation confirms DIF=capability, not contamination\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: GSM1K Correlation Under Worst-Case Scrutiny\",\n        \"columns\": [\n          \"metric\",\n          \"point_estimate\",\n          \"95% CI\",\n          \"reviewer_counterargument\"\n        ],\n        \"rows\": [\n          [\n            \"pearson_r\",\n            -0.478,\n            \"[-0.71, -0.12]\",\n            \"CI includes near-zero; N=33 too small\"\n          ],\n          [\n            \"partial_r\",\n            -0.385,\n            \"[-0.64, -0.04]\",\n            \"Controlling accuracy weakens signal\"\n          ],\n          [\n            \"permutation_p\",\n            0.014,\n            \"N/A\",\n            \"Multiple testing not corrected\"\n          ],\n          [\n            \"leave_one_out_min\",\n            -0.374,\n            \"N/A\",\n            \"One model removal cuts 22% of effect\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: Cross-Benchmark C% Instability\",\n        \"columns\": [\n          \"benchmark\",\n          \"temporal_c_pct\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            31.3,\n            \"High instability or high capability sensitivity\"\n          ],\n          [\n            \"GSM8K\",\n            18.9,\n            \"Lower instability — benchmark-dependent\"\n          ],\n          [\n            \"delta\",\n            12.4,\n            \"No universal 'instability rate' — DIF is benchmark-specific\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The GSM1K correlation is the pivotal result. Under original framing, r=−0.478 is devastating (DIF anti-correlates with contamination). Under reframe, it becomes the HEADLINE: \\\"DIF identifies capability-authentic items that contamination cannot replicate.\\\" The wide CI (N=33) remains a vulnerability. The reframed paper should lead with this finding and frame it as: \\\"Contaminated models show inflated scores on non-DIF items (shallow memorization) but cannot maintain performance on DIF items (genuine capability discriminators).\\\" ΔTPR=0.818 is repositioned as \\\"calibration infrastructure\\\" rather than \\\"detection proof.\\\"\\n\\n\\nUnder worst tier, the r=−0.478 result — the strongest cross-benchmark finding — is turned against the original narrative. Reviewers argue: \\\"DIF items anti-correlate with contamination gap. Models that are MORE contaminated (high GSM8K-GSM1K gap: Phi, Gemma) perform WORSE on DIF items. This proves DIF identifies items where genuine capability matters — contaminated models can't fake their way through these items. DIF is a capability detector, not a contamination detector.\\\" The bootstrap CI [-0.71, -0.12] is wide (N=33), and reviewers note \\\"this could be as weak as r=-0.12, barely meaningful.\\\" The ΔTPR=0.818 on semi-synthetic injection is dismissed: \\\"synthetic contamination (flipping incorrect→correct deterministically) doesn't resemble real contamination (partial memorization, shallow pattern matching). High ΔTPR on synthetic data doesn't validate real-world detection.\\\" The 18.9% temporal C% on GSM8K (vs 31.3% on MMLU) is spun as \\\"DIF flags vary wildly across benchmarks — no stable characterization.\\\" Deepseek-math-7b-rl as Cook's D outlier raises concerns about robustness of the correlation despite leave-one-out showing min |r|=0.374.\\n\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"Pilot bifactor IRT on MMLU (general factor + 57 subject factors). Anchor item selection, fixed-parameter calibration for replacement items.\\n\",\n    \"results\": {\n      \"bifactor_convergence\": false,\n      \"bifactor_rmsea\": 0.11,\n      \"bifactor_cfi\": 0.72,\n      \"bifactor_tli\": 0.68,\n      \"n_subjects_57\": 57,\n      \"n_items_12508\": 12508,\n      \"n_models_5219\": 5219,\n      \"anchor_items_selected\": 0,\n      \"equating_rho\": \"N/A (model failed to converge)\",\n      \"computation_time_hours\": 48,\n      \"memory_peak_gb\": 180,\n      \"reviewer_critique\": \"57-factor bifactor on 12K items is computationally intractable\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Bifactor IRT Fit Diagnostics\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"threshold\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"RMSEA\",\n            0.11,\n            \"<0.08\",\n            \"FAIL\"\n          ],\n          [\n            \"CFI\",\n            0.72,\n            \">0.90\",\n            \"FAIL\"\n          ],\n          [\n            \"TLI\",\n            0.68,\n            \">0.90\",\n            \"FAIL\"\n          ],\n          [\n            \"SRMR\",\n            0.09,\n            \"<0.08\",\n            \"FAIL\"\n          ],\n          [\n            \"convergence\",\n            \"No (48h timeout)\",\n            \"Yes\",\n            \"FAIL\"\n          ],\n          [\n            \"n_parameters\",\n            \"~25,000\",\n            \"<5,000 practical\",\n            \"FAIL\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bifactor failure is expected and, under worst tier, becomes evidence that MMLU is fundamentally unsuitable for IRT-based psychometric analysis. Reviewers cite this as proof that \\\"applying unidimensional psychometric methods to a 57-subject multidimensional benchmark is methodologically invalid.\\\" Under reframe, this is acknowledged honestly in limitations: \\\"MMLU's multidimensional structure exceeds current IRT modeling capacity; our within-subject analysis (plan_014) partially addresses this but doesn't eliminate the concern.\\\" Drop the equating pipeline entirely.\\n\\n\\nUnder worst tier, bifactor IRT fails catastrophically. The 57-subject structure of MMLU means a bifactor model requires estimating 1 general + 57 specific factors — a 58-dimensional latent space with ~25,000 item parameters. This exceeds practical computational limits (180GB RAM, 48 hours without convergence). Even if forced to converge with simplifications (e.g., constraining factor loadings), fit indices are poor: RMSEA=0.11 (>0.08 threshold), CFI=0.72 (<0.90 threshold), TLI=0.68 (<0.90). The unidimensionality assumption underlying MH-DIF is confirmed as violated, but the alternative (bifactor) is intractable. Reviewers argue: \\\"You've demonstrated that the psychometric foundation of your method is inappropriate for MMLU, but provided no working alternative. Multidimensional DIF methods exist (MIMIC, MIRT-DIF) but you haven't implemented them.\\\" Anchor item selection fails because the bifactor model didn't converge — no equating is possible. The entire regeneration pipeline (plan_005 → plan_006 → plan_008) collapses at step one.\\n\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"Generate replacement items for DIF-flagged questions. LLM generation with construct constraints, student simulation calibration, difficulty correlation validation.\\n\",\n    \"results\": {\n      \"n_items_generated\": 300,\n      \"n_subjects_covered\": 15,\n      \"difficulty_correlation_prompt\": 0.18,\n      \"difficulty_correlation_student_sim\": 0.34,\n      \"cognitive_level_match_rate\": 0.45,\n      \"item_quality_human_eval\": 0.61,\n      \"construct_alignment_score\": 0.53,\n      \"holdout_panel_rho\": 0.42,\n      \"gpu_hours_used\": 180,\n      \"reviewer_critique\": \"difficulty calibration too weak for operational use\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Item Generation Calibration Failure\",\n        \"columns\": [\n          \"calibration_method\",\n          \"difficulty_rho\",\n          \"claimed_in_literature\",\n          \"achieved\"\n        ],\n        \"rows\": [\n          [\n            \"prompt_targeting\",\n            0.18,\n            \"0.10-0.45\",\n            \"Low end\"\n          ],\n          [\n            \"student_simulation\",\n            0.34,\n            \"0.75-0.82\",\n            \"Far below\"\n          ],\n          [\n            \"holdout_validation\",\n            0.42,\n            \">0.90 needed\",\n            \"Insufficient\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Item generation is the most expensive failure (180 GPU-hrs). Under worst tier, it actively undermines the paper — reviewers use it to argue \\\"you can't replace DIF items, and you've shown DIF items don't affect rankings (ρ=0.997), so what's the practical value?\\\" Under reframe, this experiment should not be run at all. The capability-archaeology paper frames DIF items as valuable signal carriers, not problems to be replaced. Save the 200 GPU-hour budget.\\n\\n\\nUnder worst tier, item generation produces mediocre results. Prompt-based difficulty targeting yields ρ=0.18 (consistent with literature range 0.10-0.45 from arXiv 2602.06631 — on the low end). Student simulation calibration improves to ρ=0.34 but still far below the r=0.75-0.82 claimed in arXiv 2601.09953 — the discrepancy arises because student simulation was validated on simple math items, not MMLU's diverse knowledge domains. Cognitive level matching (45%) means over half of replacement items test different cognitive processes than originals. Construct alignment (53%) is poor — reviewers argue \\\"replacing items with construct-misaligned substitutes invalidates the benchmark more than the DIF items did.\\\" The holdout panel validation (ρ=0.42) shows replacement items don't preserve model rankings. Reviewers conclude: \\\"The cure is worse than the disease — DIF-flagged items at least produce stable rankings (ρ=0.997); replacements introduce genuine measurement error.\\\" 180 GPU-hours consumed for a negative result. Under reframe, this experiment is dropped entirely — the capability-archaeology paper doesn't need item replacement.\\n\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"Implement cumulative Bayesian DIF priors (Sinharay et al., 2006). Simulate 4 successive administrations. Show power improvement from evidence accumulation.\\n\",\n    \"results\": {\n      \"single_admin_power_d10\": 0.38,\n      \"cumulative_2_admin_power_d10\": 0.49,\n      \"cumulative_3_admin_power_d10\": 0.58,\n      \"cumulative_4_admin_power_d10\": 0.64,\n      \"single_admin_fpr\": 0.05,\n      \"cumulative_4_admin_fpr\": 0.11,\n      \"fpr_inflation_per_admin\": 0.02,\n      \"convergence_rate\": 0.92,\n      \"reviewer_critique\": \"cumulative FPR inflation makes this impractical\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Cumulative Bayesian DIF Power Trajectory\",\n        \"columns\": [\n          \"n_administrations\",\n          \"tpr_d10\",\n          \"tpr_d14\",\n          \"fpr\",\n          \"net_power_gain\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.38,\n            0.68,\n            0.05,\n            \"baseline\"\n          ],\n          [\n            2,\n            0.49,\n            0.78,\n            0.07,\n            \"+0.11/+0.10\"\n          ],\n          [\n            3,\n            0.58,\n            0.84,\n            0.09,\n            \"+0.09/+0.06\"\n          ],\n          [\n            4,\n            0.64,\n            0.87,\n            0.11,\n            \"+0.06/+0.03\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cumulative Bayesian is theoretically elegant but practically undermined by FPR inflation. Under worst tier, it's a distraction — reviewers see diminishing returns and growing false positives. Under reframe, it has modest value as \\\"longitudinal capability tracking infrastructure\\\" but is not central. Recommend moving to appendix or future work.\\n\\n\\nUnder worst tier, cumulative Bayesian DIF shows power improvement (0.38→0.64 over 4 administrations for medium effects δ=1.0) but fails to reach the 0.70 target from the plan description. More critically, FPR inflates from 0.05 to 0.11 across 4 administrations — each administration's prior carries forward false positive evidence. Reviewers argue: \\\"With baseline FPR already at 31% in real data (plan_001), cumulative approaches will amplify false positives. You're accumulating evidence that items changed function — but we've established this is capability improvement, not contamination. You're building a more powerful detector of the wrong thing.\\\" The simulation uses idealized conditions (known item parameters, controlled drift) that don't match real MMLU conditions. Under reframe, this becomes interesting — \\\"cumulative tracking of capability-sensitive items across model generations\\\" — but the FPR inflation concern remains.\\n\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"Formal analysis of benchmark validity under progressive item replacement (5%-50%). Validity metrics, theoretical bounds, empirical validation.\\n\",\n    \"results\": {\n      \"rho_at_5pct_replacement\": 0.998,\n      \"rho_at_10pct_replacement\": 0.996,\n      \"rho_at_20pct_replacement\": 0.991,\n      \"rho_at_50pct_replacement\": 0.972,\n      \"reliability_alpha_original\": 0.94,\n      \"reliability_alpha_50pct_replaced\": 0.88,\n      \"construct_coverage_original\": 57,\n      \"construct_coverage_50pct_replaced\": 52,\n      \"theoretical_bound_rho_min\": 0.95,\n      \"replacement_rate_at_bound\": 0.38,\n      \"reviewer_critique\": \"confirms DIF removal doesn't matter\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Graceful Degradation Curves\",\n        \"columns\": [\n          \"replacement_pct\",\n          \"rank_rho\",\n          \"reliability_alpha\",\n          \"subjects_covered\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            0,\n            1.0,\n            0.94,\n            57,\n            \"baseline\"\n          ],\n          [\n            5,\n            0.998,\n            0.93,\n            57,\n            \"negligible\"\n          ],\n          [\n            10,\n            0.996,\n            0.93,\n            57,\n            \"negligible\"\n          ],\n          [\n            20,\n            0.991,\n            0.91,\n            56,\n            \"minor\"\n          ],\n          [\n            31,\n            0.987,\n            0.9,\n            55,\n            \"DIF removal point\"\n          ],\n          [\n            50,\n            0.972,\n            0.88,\n            52,\n            \"still acceptable\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Graceful degradation is self-defeating under worst tier AND original framing. It proves removing DIF items doesn't matter, undermining significance. Under reframe, this becomes: \\\"MMLU is 3× larger than needed for stable rankings — DIF identifies the informative core (the items that DO contribute discriminative signal).\\\" The ρ=0.972 at 50% replacement becomes \\\"you could cut MMLU in half and preserve rankings — DIF tells you which half to keep.\\\" This is actually a strong reframe, turning the worst finding into a measurement efficiency contribution.\\n\\n\\nUnder worst tier, graceful degradation analysis confirms the ρ=0.997 finding from plan_017 — removing/replacing up to 50% of items barely affects rankings (ρ=0.972). Reviewers weaponize this: \\\"Even replacing HALF the benchmark changes rankings by less than 3%. This proves MMLU is massively redundant, and DIF-flagged items are redundant too. Why should anyone care about 31% item instability if it doesn't affect rankings?\\\" Reliability drops from 0.94 to 0.88 at 50% replacement, but remains above acceptable thresholds (0.70). Construct coverage loses 5 of 57 subjects at 50% replacement — reviewers note \\\"acceptable.\\\" The theoretical bound (ρ≥0.95 up to 38% replacement) perfectly matches the DIF flagging rate (31.3%), which reviewers read as \\\"you can safely ignore everything DIF flags.\\\" This experiment depends on plan_005/006 (which fail), so the \\\"replacement\\\" is simulated via random item substitution rather than actual generated items — further reducing credibility.\\n\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"Item-Focused Trees (Tutz & Berger, 2016) as alternative to categorical cohort DIF. Continuous covariate (release date). Compare detection power vs categorical MH.\\n\",\n    \"results\": {\n      \"ift_detection_rate\": 0.34,\n      \"ift_vs_mh_overlap\": 0.78,\n      \"ift_unique_flags\": 0.06,\n      \"mh_unique_flags\": 0.04,\n      \"ift_uses_full_sample\": true,\n      \"ift_avoids_cohort_splits\": true,\n      \"ift_computational_cost_ratio\": 12.0,\n      \"ift_release_date_coefficient_mean\": 0.08,\n      \"ift_release_date_coefficient_std\": 0.15,\n      \"reviewer_critique\": \"confirms temporal trend = capability gain\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: IFT vs MH Comparison\",\n        \"columns\": [\n          \"method\",\n          \"flagging_rate\",\n          \"unique_flags\",\n          \"cost_ratio\",\n          \"temporal_pattern\"\n        ],\n        \"rows\": [\n          [\n            \"MH_categorical\",\n            0.313,\n            0.04,\n            1.0,\n            \"Discrete cohort split\"\n          ],\n          [\n            \"IFT_continuous\",\n            0.34,\n            0.06,\n            12.0,\n            \"Smooth positive trend\"\n          ],\n          [\n            \"overlap\",\n            0.78,\n            \"-\",\n            \"-\",\n            \"Same underlying signal\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"IFT provides marginal methodological value but under worst tier confirms the capability-improvement interpretation via smooth temporal trends. Under reframe, the smooth trend is actually interesting: \\\"capability-authentic items show predictable sensitivity to model generation — enabling prospective identification of items that will become less discriminative.\\\" Recommend as supplementary/appendix rather than main paper contribution.\\n\\n\\nUnder worst tier, Item-Focused Trees detect 34% of items as having significant temporal DIF — nearly identical to MH's 31.3%. The 78% overlap confirms both methods detect the same phenomenon. The IFT release-date coefficient (mean=0.08, SD=0.15) is positive: items become easier over time, consistent with capability improvement. Reviewers read the continuous coefficient as: \\\"DIF is a smooth function of time, not a discrete shift — this is exactly what capability improvement looks like. If contamination caused DIF, we'd expect discrete jumps when specific training data became available.\\\" The 12× computational cost over MH makes IFT impractical at scale. Reviewers conclude: \\\"IFT confirms MH findings but adds computational cost and the interpretation that item changes are gradual (capability) not abrupt (contamination).\\\"\\n\"\n  },\n  {\n    \"name\": \"architecture_stratified_dif\",\n    \"description\": \"DIF within decoder-only homogeneous subpopulation. IRT fit diagnostics. Compare FPR/TPR vs full-population DIF from plan_001.\\n\",\n    \"results\": {\n      \"n_decoder_only\": 3400,\n      \"decoder_only_c_pct\": 33.1,\n      \"decoder_only_irt_rmsea\": 0.092,\n      \"decoder_only_irt_cfi\": 0.81,\n      \"decoder_only_irt_tli\": 0.78,\n      \"decoder_only_irt_srmr\": 0.073,\n      \"full_population_c_pct\": 31.3,\n      \"delta_c_pct\": 1.8,\n      \"fpr_decoder_only\": 0.33,\n      \"fpr_full_population\": 0.318,\n      \"tpr_delta_p05\": -0.02,\n      \"reviewer_critique\": \"architecture homogeneity doesn't fix the problem\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Architecture Stratification Results\",\n        \"columns\": [\n          \"population\",\n          \"n_models\",\n          \"c_pct\",\n          \"rmsea\",\n          \"cfi\",\n          \"tli\"\n        ],\n        \"rows\": [\n          [\n            \"full_population\",\n            5219,\n            31.3,\n            \"N/A (not computed)\",\n            \"N/A\",\n            \"N/A\"\n          ],\n          [\n            \"decoder_only\",\n            3400,\n            33.1,\n            0.092,\n            0.81,\n            0.78\n          ],\n          [\n            \"delta\",\n            \"-1819\",\n            \"+1.8\",\n            \"FAIL (>0.08)\",\n            \"FAIL (<0.90)\",\n            \"FAIL (<0.90)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 16: Detection Power Comparison\",\n        \"columns\": [\n          \"population\",\n          \"fpr_baseline\",\n          \"tpr_p05\",\n          \"tpr_p10\",\n          \"enrichment\"\n        ],\n        \"rows\": [\n          [\n            \"full_population\",\n            0.318,\n            0.834,\n            1.0,\n            0.96\n          ],\n          [\n            \"decoder_only\",\n            0.33,\n            0.82,\n            0.99,\n            0.95\n          ],\n          [\n            \"delta\",\n            \"+0.012\",\n            \"-0.014\",\n            \"-0.01\",\n            \"-0.01\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Architecture stratification is the critical missing experiment identified by worst-case Dream, and it produces the predicted negative result. Under worst tier, this closes the last escape route: DIF flagging rates cannot be reduced by controlling for architecture. The IRT misfit is structural (MMLU dimensionality) not population-driven. Under reframe, this becomes neutral: \\\"DIF item sensitivity is robust to population composition — capability-authentic items are identified regardless of architecture mix.\\\" The IRT fit concern is acknowledged honestly but framed as \\\"conservative: poor IRT fit means DIF may UNDERESTIMATE the true proportion of capability-sensitive items.\\\"\\n\\n\\nUnder worst tier (explicitly specified in tier definition), architecture stratification fails to improve results. Decoder-only C% = 33.1% (vs 31.3% full population) — no meaningful reduction, slightly HIGHER. IRT fit remains poor: RMSEA=0.092 (>0.08), CFI=0.81 (<0.90), TLI=0.78 (<0.90). Removing encoder-decoder and hybrid architectures doesn't address the fundamental unidimensionality problem — MMLU's 57-subject structure violates unidimensional IRT regardless of architecture homogeneity. The C% increase from 31.3%→33.1% is within noise but reviewers spin it: \\\"architecture stratification made things WORSE — DIF flags more items in a homogeneous population, confirming that flags reflect capability variation, not architecture confounding.\\\" FPR and TPR are essentially unchanged (ΔFPR=+0.01, ΔTPR=−0.02). Reviewers familiar with psychometrics argue: \\\"RMSEA=0.092 on decoder-only models proves the IRT model is misspecified for MMLU. Your entire DIF analysis rests on an inappropriate measurement model. This is not fixable by subsetting — it requires multidimensional IRT, which you haven't implemented.\\\"\\n\"\n  },\n  {\n    \"name\": \"semi_synthetic_contamination_validation\",\n    \"description\": \"Inject known contamination into METABENCH response matrix. Measure DIF TPR/FPR against controlled ground truth. Vary injection parameters.\\n\",\n    \"results\": {\n      \"delta_tpr_p03\": 0.222,\n      \"delta_tpr_p05\": 0.508,\n      \"delta_tpr_p07\": 0.664,\n      \"delta_tpr_p10\": 0.674,\n      \"external_matching_fpr\": 0.314,\n      \"within_matching_fpr_inflation\": 0.186,\n      \"cross_subject_delta_fpr\": 0.0,\n      \"cross_subject_delta_tpr_p05_avg\": 0.36,\n      \"dose_response_present\": true,\n      \"reviewer_critique\": \"synthetic injection mechanism unrealistic\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 17: Semi-Synthetic Results Under Worst Interpretation\",\n        \"columns\": [\n          \"injection_rate_p\",\n          \"delta_tpr_standard\",\n          \"delta_tpr_cross_subject\",\n          \"reviewer_spin\"\n        ],\n        \"rows\": [\n          [\n            0.3,\n            0.222,\n            0.18,\n            \"Below useful detection\"\n          ],\n          [\n            0.5,\n            0.508,\n            0.36,\n            \"Only works at 50%+ exploitation\"\n          ],\n          [\n            0.7,\n            0.664,\n            0.52,\n            \"High exploitation = easy detection\"\n          ],\n          [\n            1.0,\n            0.674,\n            0.62,\n            \"Saturates — ceiling effect\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 18: Matching Strategy Comparison\",\n        \"columns\": [\n          \"matching\",\n          \"fpr_baseline\",\n          \"fpr_at_p10\",\n          \"delta_fpr\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"standard_MH\",\n            0.298,\n            0.616,\n            \"+0.318\",\n            \"FPR inflates (contaminated matching var)\"\n          ],\n          [\n            \"external_5subj\",\n            0.314,\n            0.314,\n            0.0,\n            \"FPR stable (clean matching var)\"\n          ],\n          [\n            \"cross_subject\",\n            0.33,\n            0.33,\n            0.0,\n            \"FPR stable (recommended)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Semi-synthetic validation is the strongest methodological contribution even under worst tier. The cross-subject matching innovation (ΔFPR=0.000) is genuinely novel and useful. Under reframe, the semi-synthetic framework is repositioned as \\\"calibration infrastructure for item sensitivity analysis\\\" — it characterizes how much differential signal is needed before DIF detects it, without claiming this maps to real contamination. The dose-response curve becomes \\\"sensitivity calibration\\\" rather than \\\"contamination detection power.\\\" This experiment survives the reframe relatively intact.\\n\\nUnder worst tier, semi-synthetic results (already observed) are technically sound but dismissed on ecological validity grounds. ΔTPR=0.508 at p=0.5 shows DIF detects injected contamination — but reviewers argue the injection mechanism (flip incorrect→correct with probability p) doesn't model real contamination. Real contamination involves: (1) partial memorization (model recalls fragments, not full answers), (2) shallow pattern matching (model exploits surface features), (3) chain-of-thought reasoning from memorized premises. None of these produce the clean incorrect→correct flipping that synthetic injection assumes. The dose-response curve (ΔTPR increases with p) is called \\\"trivially expected — of course flipping more answers makes items behave more differently.\\\" The cross- subject matching innovation (ΔFPR=0.000) is acknowledged as methodologically sound, but reviewers argue \\\"you've built a valid framework for detecting something that doesn't exist in the real world in this form.\\\" The gap between synthetic ΔTPR=0.508 and real enrichment=0.96 is the fatal disconnect: \\\"Your method works perfectly on synthetic contamination and not at all on real data — this means your synthetic model is wrong, not that your ground truth is wrong.\\\"\\n\"\n  }\n]",
      "numLines": 914,
      "startLine": 1,
      "totalLines": 914
    }
  },
  "sourceToolAssistantUUID": "7c0cfcfe-7766-4c3a-94dd-8822bb8ae22d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "24cba543-cf46-4cb5-a094-cb93a326404e",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulation paper from experiment data",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da"
}
```

---

### Assistant

_source line 16 · 2026-05-21T01:54:20.589Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and the paper framing. Let me also check if the output directory exists.

The narrative guidance says this is the "worst" tier — the core narrative collapses. Reviewers see DIF as a capability improvement detector, not a benchmark integrity tool. The reframe is to pivot to "DIF as capability archaeology / measurement efficiency" paper.

Let me write a complete LaTeX paper following the narrative guidance for the "worst" tier. The key reframing:
- 38% instability = 38% of items are capability-sensitive


- The correlation coefficient of 0.307 is the critical evidence that DIF genuinely captures capability differences
- GSM1K's negative correlation becomes the main positive result, showing DIF successfully filters out contaminated items
- The near-perfect correlation suggests benchmarks are substantially oversized
- Semi-synthetic injection serves as calibration infrastructure
- I'll acknowledge the bifactor model limitations directly
- Focus on the core DIF findings and drop the ensemble, DVD, and item generation components as tangential
- Title the paper around identifying capability-authentic items through differential item functioning

Now I'm structuring the paper with abstract, introduction, and background sections.

For the experiments, I need to cover all twelve studies from the dataset. Looking at the full list, I can see which ones support the main narrative about DIF identifying genuine capability versus contamination, and which ones represent negative or exploratory results that I should present honestly rather than hide.

The strongest findings center on real MMLU data showing DIF's effectiveness, the GSM8K anti-correlation as a key headline result, evidence that benchmarks are redundant and we could measure more efficiently, and the semi-synthetic validation framework proving the approach works. The weaker experiments—robustness validation being underpowered, ConStat showing orthogonal rather than overlapping signals, DVD being both weak and computationally expensive, ensemble methods failing, bifactor IRT not working, item generation calibration issues, Bayesian cumulative DIF showing false positive rate inflation, and architecture stratification providing no benefit—all get honest treatment as negative or null results rather than being buried.

Item-focused decision trees confirm the capability interpretation holds up, and now I'm ready to write the paper with comprehensive coverage while keeping it at an appropriate level of rigor.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24cba543-cf46-4cb5-a094-cb93a326404e",
  "isSidechain": false,
  "requestId": "req_011CbEszV1gkEPTs2aNogvVJ",
  "type": "assistant",
  "uuid": "774cb004-6b4b-403d-953f-8c87c3ae70d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TLGbLZpQLtuvUWpTCvNQoB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3326,
      "cache_creation_input_tokens": 14358,
      "cache_read_input_tokens": 23299,
      "output_tokens": 883,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14358,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3326,
          "output_tokens": 883,
          "cache_read_input_tokens": 23299,
          "cache_creation_input_tokens": 14358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14358
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

_source line 17 · 2026-05-21T01:54:20.591Z_

Let me check the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "774cb004-6b4b-403d-953f-8c87c3ae70d5",
  "isSidechain": false,
  "requestId": "req_011CbEszV1gkEPTs2aNogvVJ",
  "type": "assistant",
  "uuid": "c3f77f65-cb05-45ea-acf3-64bb9e022327",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TLGbLZpQLtuvUWpTCvNQoB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3326,
      "cache_creation_input_tokens": 14358,
      "cache_read_input_tokens": 23299,
      "output_tokens": 883,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14358,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3326,
          "output_tokens": 883,
          "cache_read_input_tokens": 23299,
          "cache_creation_input_tokens": 14358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14358
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

_source line 18 · 2026-05-21T01:54:20.867Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SQFYEZ3w9cLKSKJRvjf2x4`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3f77f65-cb05-45ea-acf3-64bb9e022327",
  "isSidechain": false,
  "requestId": "req_011CbEszV1gkEPTs2aNogvVJ",
  "type": "assistant",
  "uuid": "c5ed4476-871e-43cc-85b9-7cbb84a343ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TLGbLZpQLtuvUWpTCvNQoB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3326,
      "cache_creation_input_tokens": 14358,
      "cache_read_input_tokens": 23299,
      "output_tokens": 883,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14358,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3326,
          "output_tokens": 883,
          "cache_read_input_tokens": 23299,
          "cache_creation_input_tokens": 14358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14358
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

_source line 19 · 2026-05-21T01:54:21.041Z_

<details><summary>↩ Tool result · `toolu_01SQFYEZ3w9cLKSKJRvjf2x4`</summary>

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
  "parentUuid": "c5ed4476-871e-43cc-85b9-7cbb84a343ae",
  "isSidechain": false,
  "promptId": "41166657-dacb-41c2-9c9f-045334e8b1ff",
  "type": "user",
  "uuid": "5c070630-9e57-4cf3-946d-419521df52e1",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c5ed4476-871e-43cc-85b9-7cbb84a343ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-21T01:54:23.523Z_

Writing the LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c070630-9e57-4cf3-946d-419521df52e1",
  "isSidechain": false,
  "requestId": "req_011CbEt277rcnkFbKAsxpTCd",
  "type": "assistant",
  "uuid": "1bc085a7-3121-4429-b3f7-d33635ef9f24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013uihiwXwgUsXS1JSdRFg1H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4238,
      "cache_read_input_tokens": 37657,
      "output_tokens": 12056,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12056,
          "cache_read_input_tokens": 37657,
          "cache_creation_input_tokens": 4238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4238
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

_source line 21 · 2026-05-21T01:58:06.748Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Nts3JnWMjHBw9Yff9q3q1n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/paper.tex",
  "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\title{Identifying Capability-Authentic Benchmark Items via Differential Item Functioning}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nLarge language model benchmarks implicitly assume that items measure the same construct across model generations. We challenge this assumption by applying Differential Item Functioning (DIF) analysis---a classical psychometric technique---to the METABENCH response matrix (5,219 models $\\times$ 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\nWe find that 31.3\\% of MMLU items are \\emph{capability-sensitive}: they exhibit large DIF between 2023 and 2024-H1 model cohorts (ETS category C, $|\\Delta_{\\mathrm{MH}}|\\ge1.5$). Rather than indicating benchmark pathology, these items concentrate the discriminative signal that differentiates model generations---their removal disrupts rankings significantly more than random removal ($z=-8$ to $-49\\sigma$). Cross-benchmark validation on GSM8K confirms that DIF-flagged items \\emph{anti-correlate} with contamination ($r=-0.478$, $p=0.005$, $N=33$): contaminated models perform worse on DIF items, indicating DIF captures genuine capability differences that memorization cannot replicate.\nDownstream impact analysis reveals massive benchmark redundancy: removing all DIF items changes the Spearman rank correlation by only $\\rho=0.997$, implying MMLU is roughly three times larger than necessary for stable rankings. We contribute a reusable semi-synthetic validation framework with cross-subject matching that eliminates false positive rate inflation ($\\Delta\\mathrm{FPR}=0.000$). We further report extensive negative results from twelve experiments---including bifactor IRT failure, underpowered RL robustness tests, and weak ensemble fusion---to map the operational boundaries of DIF in the LLM evaluation setting.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nWhen we declare that ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent construct measured under comparable conditions. In educational testing, this assumption is routinely audited via Differential Item Functioning (DIF) analysis, which detects items that behave differently across examinee subgroups after controlling for overall ability. If a math item is harder for one demographic group than another, conditional on equal math ability, the item exhibits DIF and threatens fair measurement.\n\nLLM benchmarks face an analogous threat. As model capabilities evolve rapidly across generations, benchmark items may shift in effective difficulty---not because the items changed, but because the relationship between model capability and item response changed. An item that once discriminated between strong and weak models may become trivially easy for all modern models, or conversely, an item that tested surface-level pattern matching may now require genuine reasoning from models that have moved beyond shallow heuristics.\n\nWe apply Mantel-Haenszel (MH) DIF analysis to the METABENCH repository, analyzing 5,219 models across 12,508 MMLU items. Our central finding reframes the role of DIF in LLM evaluation: items flagged by DIF are not ``broken''---they are \\emph{capability-authentic}. They are the items where genuine capability improvement manifests at the item level, and they concentrate the signal that distinguishes model generations.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}\n    \\item \\textbf{Capability-sensitive item identification.} We show that 31.3\\% of MMLU items exhibit large temporal DIF, and that this rate is robust to architecture stratification (decoder-only: 33.1\\%), correlates with domain-level accuracy improvement ($\\rho=0.307$, $p=0.02$), and cannot be attributed to statistical noise (random split: 0.18\\%).\n    \\item \\textbf{Cross-benchmark capability validation.} On GSM8K ($1{,}319$ items $\\times$ $6{,}702$ models), DIF flags anti-correlate with the GSM1K contamination gap ($r=-0.478$, $p=0.005$). Contaminated models---those with inflated GSM8K scores relative to the held-out GSM1K---perform \\emph{worse} on DIF items. DIF identifies items where genuine capability matters.\n    \\item \\textbf{Measurement efficiency characterization.} Rank correlation remains $\\rho\\ge0.972$ even after replacing 50\\% of items, revealing that MMLU is roughly $3\\times$ larger than needed for stable rankings. DIF items form the informative core.\n    \\item \\textbf{Semi-synthetic validation framework.} We introduce a $\\Delta$TPR methodology with cross-subject matching ($\\Delta$FPR$=0.000$), providing reusable calibration infrastructure for item-level detectors.\n    \\item \\textbf{Comprehensive negative results.} We report twelve experiments including bifactor IRT failure, weak ensemble fusion, underpowered RL robustness, and unsuccessful item generation, mapping the operational boundaries of psychometric methods in LLM evaluation.\n\\end{enumerate}\n\n%==============================================================================\n\\section{Background}\n\\label{sec:background}\n%==============================================================================\n\n\\subsection{Differential Item Functioning}\n\nIn classical test theory, an item exhibits DIF when examinees of equal ability from different groups have different probabilities of answering correctly. The Mantel-Haenszel (MH) procedure is the most widely used DIF detection method. It stratifies examinees by total score (as a proxy for ability), then tests whether the odds ratio of correct response differs between a reference group and a focal group across strata. The MH odds ratio $\\alpha_{\\mathrm{MH}}$ is converted to the $\\Delta_{\\mathrm{MH}}$ scale:\n\\begin{equation}\n    \\Delta_{\\mathrm{MH}} = -2.35 \\ln(\\alpha_{\\mathrm{MH}})\n\\end{equation}\nItems are classified by the Educational Testing Service (ETS) scheme: category A ($|\\Delta_{\\mathrm{MH}}|<1.0$, negligible), B ($1.0\\le|\\Delta_{\\mathrm{MH}}|<1.5$, moderate), and C ($|\\Delta_{\\mathrm{MH}}|\\ge1.5$, large DIF). We focus on category C items as indicators of substantial differential functioning.\n\n\\subsection{DIF in the LLM Context}\n\nIn our setting, ``examinees'' are LLM models and ``groups'' are temporal cohorts (2023 vs.\\ 2024-H1 release dates). An item with large temporal DIF functions differently across model generations conditional on overall benchmark performance. We hypothesize that such items are \\emph{capability-sensitive}: they are precisely the items where genuine capability improvement (or degradation) manifests, as opposed to items that are universally easy or hard regardless of generation.\n\n%==============================================================================\n\\section{Data}\n\\label{sec:data}\n%==============================================================================\n\nWe use the METABENCH repository, which aggregates benchmark responses from publicly available LLMs. Our primary dataset is the MMLU response matrix: 5,219 models $\\times$ 12,508 items across 57 subject domains. For cross-benchmark validation, we use the GSM8K response matrix: 6,702 models $\\times$ 1,319 items. External validation uses GSM1K contamination gap data for 33 matched models.\n\n%==============================================================================\n\\section{Experiments and Results}\n\\label{sec:experiments}\n%==============================================================================\n\nWe report results from twelve experiments. We organize them into four thematic groups: (1) core DIF characterization, (2) cross-benchmark and external validation, (3) methodological extensions, and (4) negative results that map operational boundaries.\n\n%------------------------------------------------------------------------------\n\\subsection{Core DIF Characterization on MMLU}\n\\label{sec:core_dif}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 1: Temporal DIF Analysis.}\nWe apply MH-DIF to the full MMLU matrix with temporal cohort splits (2023 vs.\\ 2024-H1). Table~\\ref{tab:dif_summary} summarizes detection rates under four cohort definitions.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF detection rates (ETS category C) under different cohort definitions.}\n\\label{tab:dif_summary}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Cohort Definition} & \\textbf{C\\%} & \\textbf{Enrichment vs.\\ Li} & \\textbf{Interpretation} \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024) & 31.3 & 0.96 & Capability gain across generations \\\\\nAbility quintile & 2.9 & 1.19 & Items function consistently across ability \\\\\nWithin-family (Llama-2 vs.\\ 3) & 61.3 & N/A & Pure capability gain, same pipeline \\\\\nRandom split (sanity) & 0.18 & N/A & Confirms real signal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe temporal C\\%$=31.3$ indicates that nearly one-third of items function differently across model generations. The random split sanity check (0.18\\%) confirms this is not statistical noise. The within-family Llama-2 vs.\\ Llama-3 comparison is particularly informative: 61.3\\% of items show large DIF within the same model family (same training data pipeline, same organization), attributable to architectural and training improvements rather than data contamination.\n\nThe enrichment against Li et al.\\ contamination labels is 0.96---effectively null. This means DIF-flagged items are no more likely to be labeled as contaminated by web-overlap methods than non-flagged items. We interpret this as evidence that DIF and web-overlap labels measure orthogonal constructs: DIF captures differential item functioning (how items behave differently across groups), while web-overlap captures global data exposure (whether an item appears on the public internet).\n\n\\paragraph{Domain-level correlation.}\nThe Spearman correlation between domain-level DIF rates and domain-level accuracy improvement is $\\rho=0.307$ ($p=0.02$). Domains where models improved most between generations have the highest DIF rates. This confirms that DIF tracks capability improvement at the domain level, explaining 9.4\\% of cross-domain variance.\n\n\\begin{table}[h]\n\\centering\n\\caption{Domain-level correlation between DIF rate and accuracy improvement.}\n\\label{tab:domain_corr}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Interpretation} \\\\\n\\midrule\nSpearman $\\rho$ (DIF vs.\\ accuracy gain) & 0.307 & DIF tracks capability improvement \\\\\n$p$-value & 0.02 & Statistically significant \\\\\nVariance explained & 9.4\\% & Partial; other factors contribute \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------------------\n\\subsection{Architecture Stratification}\n\\label{sec:arch_strat}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 2: Decoder-Only Subpopulation.}\nA potential confound is architectural heterogeneity: encoder-decoder and hybrid models may inflate DIF rates. We restrict analysis to decoder-only models ($N=3{,}400$) and recompute DIF.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF rates and IRT fit diagnostics: full population vs.\\ decoder-only.}\n\\label{tab:arch_strat}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Population} & \\textbf{$N$} & \\textbf{C\\%} & \\textbf{RMSEA} & \\textbf{CFI} & \\textbf{TLI} \\\\\n\\midrule\nFull population & 5,219 & 31.3 & --- & --- & --- \\\\\nDecoder-only & 3,400 & 33.1 & 0.092 & 0.81 & 0.78 \\\\\n\\midrule\n$\\Delta$ & $-1{,}819$ & $+1.8$ & \\multicolumn{3}{c}{All below thresholds} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nArchitecture stratification does not reduce DIF rates (C\\% increases slightly from 31.3\\% to 33.1\\%). IRT fit indices remain below standard thresholds (RMSEA$>0.08$, CFI$<0.90$, TLI$<0.90$), confirming that the unidimensionality violation stems from MMLU's 57-subject structure, not architectural heterogeneity. Detection power is essentially unchanged ($\\Delta$FPR$=+0.012$, $\\Delta$TPR$=-0.014$).\n\nThis result is informative for the capability-authenticity interpretation: DIF item sensitivity is robust to population composition.\n\n%------------------------------------------------------------------------------\n\\subsection{Cross-Benchmark Validation: GSM8K and GSM1K}\n\\label{sec:cross_bench}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 3: GSM8K Replication and GSM1K Anti-Correlation.}\nWe replicate DIF analysis on GSM8K (1,319 items $\\times$ 6,702 models), finding a temporal C\\%$=18.9$---lower than MMLU's 31.3\\%, confirming that DIF rates are benchmark-specific rather than universal.\n\nThe headline finding concerns GSM1K, a held-out test set designed to measure contamination. For 33 models with both GSM8K and GSM1K scores, we correlate DIF flag rates with the contamination gap (GSM8K minus GSM1K accuracy):\n\n\\begin{table}[h]\n\\centering\n\\caption{GSM1K contamination gap correlation with DIF flags.}\n\\label{tab:gsm1k}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Estimate} & \\textbf{95\\% CI} & \\textbf{Implication} \\\\\n\\midrule\nPearson $r$ & $-0.478$ & $[-0.71, -0.12]$ & Anti-correlation with contamination \\\\\nPartial $r$ (controlling accuracy) & $-0.385$ & $[-0.64, -0.04]$ & Robust to ability confound \\\\\nPermutation $p$ & 0.014 & --- & Significant \\\\\nLeave-one-out min $|r|$ & 0.374 & --- & No single model drives result \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe anti-correlation is striking: models with larger contamination gaps (Phi, Gemma families---those whose GSM8K scores are most inflated relative to GSM1K) perform \\emph{worse} on DIF-flagged items. Contamination produces shallow performance gains concentrated on non-DIF items. DIF items require genuine capability that memorization cannot replicate.\n\n\\textbf{Caveats.} The bootstrap CI $[-0.71, -0.12]$ is wide due to $N=33$. Removing the highest-leverage point (Deepseek-math-7b-rl, Cook's $D$ maximum) reduces $|r|$ by 22\\% to 0.374. Multiple testing correction was not applied. These limitations are inherent to the small sample of models with matched GSM1K data.\n\n\\paragraph{Semi-synthetic validation on GSM8K.}\nThe semi-synthetic framework (Section~\\ref{sec:semisynthetic}) replicates on GSM8K with $\\Delta$TPR$=0.818$ at $p=1.0$ injection, confirming framework portability.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-benchmark DIF rates.}\n\\label{tab:cross_bench}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{Temporal C\\%} & \\textbf{Interpretation} \\\\\n\\midrule\nMMLU & 31.3 & High capability sensitivity \\\\\nGSM8K & 18.9 & Lower---benchmark-dependent \\\\\n$\\Delta$ & 12.4 & No universal rate \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------------------\n\\subsection{Semi-Synthetic Validation Framework}\n\\label{sec:semisynthetic}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 4: Controlled Contamination Injection.}\nWe inject known differential contamination into the real METABENCH response matrix by flipping incorrect$\\to$correct responses with probability $p$ for a subset of models, then measure DIF detection power increase ($\\Delta$TPR$=$TPR$_{\\text{injected}}-$TPR$_{\\text{baseline}}$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Semi-synthetic $\\Delta$TPR under varying injection rates.}\n\\label{tab:semisynthetic}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Injection Rate $p$} & \\textbf{$\\Delta$TPR (standard)} & \\textbf{$\\Delta$TPR (cross-subject)} & \\textbf{Note} \\\\\n\\midrule\n0.3 & 0.222 & 0.18 & Below useful detection \\\\\n0.5 & 0.508 & 0.36 & Moderate detection \\\\\n0.7 & 0.664 & 0.52 & Strong detection \\\\\n1.0 & 0.674 & 0.62 & Saturates---ceiling effect \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe dose-response relationship confirms that DIF detection power increases monotonically with injection intensity, providing a calibration curve for the method's sensitivity.\n\n\\paragraph{Cross-subject matching eliminates FPR inflation.}\nA critical methodological contribution: when the matching variable (total score) includes contaminated items, FPR inflates. Using total score on \\emph{other} subjects as the matching variable eliminates this:\n\n\\begin{table}[h]\n\\centering\n\\caption{Matching strategy comparison for FPR control.}\n\\label{tab:matching}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Matching Strategy} & \\textbf{FPR (baseline)} & \\textbf{FPR (at $p=1.0$)} & \\textbf{$\\Delta$FPR} & \\textbf{Verdict} \\\\\n\\midrule\nStandard MH & 0.298 & 0.616 & $+0.318$ & FPR inflates \\\\\nExternal 5-subject & 0.314 & 0.314 & 0.000 & Stable \\\\\nCross-subject & 0.330 & 0.330 & 0.000 & Stable (recommended) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-subject matching achieves $\\Delta$FPR$=0.000$ across all tested conditions. This is a reusable methodological recommendation for any item-level detector that conditions on total score.\n\n\\textbf{Ecological validity caveat.} The injection mechanism (deterministic incorrect$\\to$correct flipping) is a simplification. Real contamination involves partial memorization, shallow pattern matching, and chain-of-thought reasoning from memorized premises---none of which produce the clean flipping assumed here. The semi-synthetic framework should be understood as \\emph{calibration infrastructure} characterizing detection sensitivity, not as a direct model of real-world contamination.\n\n%------------------------------------------------------------------------------\n\\subsection{Measurement Efficiency: Graceful Degradation}\n\\label{sec:degradation}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 5: Progressive Item Replacement.}\nWe analyze how benchmark validity degrades as items are progressively replaced, quantifying MMLU's measurement redundancy.\n\n\\begin{table}[h]\n\\centering\n\\caption{Benchmark validity under progressive item replacement.}\n\\label{tab:degradation}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Replacement \\%} & \\textbf{Rank $\\rho$} & \\textbf{Reliability $\\alpha$} & \\textbf{Subjects Covered} & \\textbf{Verdict} \\\\\n\\midrule\n0 & 1.000 & 0.94 & 57 & Baseline \\\\\n5 & 0.998 & 0.93 & 57 & Negligible \\\\\n10 & 0.996 & 0.93 & 57 & Negligible \\\\\n20 & 0.991 & 0.91 & 56 & Minor \\\\\n31 (DIF removal) & 0.987 & 0.90 & 55 & DIF removal point \\\\\n50 & 0.972 & 0.88 & 52 & Still acceptable \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEven at 50\\% replacement, rank correlation remains $\\rho=0.972$ and reliability $\\alpha=0.88$ (above the standard 0.70 threshold). The theoretical bound $\\rho\\ge0.95$ holds up to 38\\% replacement---closely matching the DIF flagging rate (31.3\\%).\n\n\\textbf{Key insight.} This result has a dual interpretation. On one hand, it suggests DIF items can be safely removed without disrupting rankings. On the other hand---and we argue this is the more informative reading---it reveals that \\emph{MMLU is approximately three times larger than necessary for stable model rankings}. DIF analysis identifies which items form the informative core and which are redundant. The 31.3\\% of capability-sensitive items are precisely the items that carry discriminative signal between model generations; the remaining $\\sim$69\\% contribute mainly to reliability through redundancy.\n\n%------------------------------------------------------------------------------\n\\subsection{Item-Focused Trees: Continuous Temporal Analysis}\n\\label{sec:ift}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 6: IFT vs.\\ MH Comparison.}\nItem-Focused Trees (IFT) model DIF as a smooth function of a continuous covariate (model release date), avoiding the arbitrary temporal cohort split required by MH.\n\n\\begin{table}[h]\n\\centering\n\\caption{Item-Focused Trees vs.\\ MH-DIF comparison.}\n\\label{tab:ift}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Flagging Rate} & \\textbf{Unique Flags} & \\textbf{Cost Ratio} & \\textbf{Temporal Pattern} \\\\\n\\midrule\nMH (categorical) & 0.313 & 0.04 & 1.0$\\times$ & Discrete cohort split \\\\\nIFT (continuous) & 0.34 & 0.06 & 12.0$\\times$ & Smooth positive trend \\\\\nOverlap & 0.78 & --- & --- & Same underlying signal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 78\\% overlap confirms both methods detect the same underlying phenomenon. IFT's continuous release-date coefficient (mean$=0.08$, SD$=0.15$) reveals a smooth positive trend: items become easier over time, consistent with gradual capability improvement rather than abrupt contamination events. However, IFT's 12$\\times$ computational cost makes it impractical at scale. We recommend MH for detection and IFT as a supplementary diagnostic for characterizing temporal dynamics.\n\n%------------------------------------------------------------------------------\n\\subsection{Cumulative Bayesian DIF}\n\\label{sec:bayesian}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 7: Evidence Accumulation Across Administrations.}\nWe implement cumulative Bayesian DIF priors following Sinharay et al.\\ (2006), simulating four successive benchmark administrations to test whether accumulating evidence across administrations improves detection power.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cumulative Bayesian DIF power trajectory.}\n\\label{tab:bayesian}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$N$ Administrations} & \\textbf{TPR ($\\delta=1.0$)} & \\textbf{TPR ($\\delta=1.4$)} & \\textbf{FPR} & \\textbf{Net Gain} \\\\\n\\midrule\n1 & 0.38 & 0.68 & 0.05 & Baseline \\\\\n2 & 0.49 & 0.78 & 0.07 & $+0.11/+0.10$ \\\\\n3 & 0.58 & 0.84 & 0.09 & $+0.09/+0.06$ \\\\\n4 & 0.64 & 0.87 & 0.11 & $+0.06/+0.03$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPower improves from 0.38 to 0.64 for medium effects ($\\delta=1.0$) over four administrations. However, FPR inflates from 0.05 to 0.11---each administration's prior carries forward false positive evidence. The diminishing returns (net gain decreases each round) combined with cumulative FPR inflation make this approach impractical in its current form. The concept of longitudinal capability tracking remains promising, but requires FPR correction mechanisms not implemented here.\n\n%------------------------------------------------------------------------------\n\\subsection{RL Robustness Analysis}\n\\label{sec:rl}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 8: DIF Stability Across Training Paradigms.}\nWe examine whether DIF detection is robust to reinforcement learning (RL) training by comparing flag patterns across SFT, alignment-RL (DPO/ORPO, $N=477$), and reasoning-RL (GRPO/PPO, $N=13$) model cohorts.\n\n\\begin{table}[h]\n\\centering\n\\caption{RL robustness comparison. All comparisons are statistically non-significant.}\n\\label{tab:rl}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{SFT AUROC} & \\textbf{Alignment-RL} & \\textbf{Reasoning-RL} & \\textbf{95\\% CI Width} \\\\\n\\midrule\nDIF (MH) & 0.69 & 0.66 & 0.65 & $\\pm0.14$ \\\\\nMin-K\\% & 0.63 & 0.58 & 0.44 & $\\pm0.18$ \\\\\nConStat & 0.67 & 0.61 & 0.51 & $\\pm0.16$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Statistical tests for RL robustness---all non-significant.}\n\\label{tab:rl_stats}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Test} & \\textbf{Statistic} & \\textbf{$p$} & \\textbf{Conclusion} \\\\\n\\midrule\nDIF vs.\\ ConStat (RL) & DeLong & $z=1.19$ & 0.23 & Cannot reject $H_0$ \\\\\nDIF retention equiv. & TOST & $t=0.96$ & 0.34 & Cannot claim equivalence \\\\\nFlag overlap SFT vs.\\ RL & Bootstrap Jaccard & 0.71 & CI $[0.54,0.88]$ & Wide CI, inconclusive \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis experiment is \\textbf{fatally underpowered}. With only $N=13$ reasoning-RL models, no comparison reaches statistical significance. DIF shows numerically stable AUROC across training paradigms (0.69$\\to$0.65), while Min-K\\% degrades substantially (0.63$\\to$0.44), but we cannot draw reliable conclusions. The alignment-RL cohort ($N=477$) shows DIF flag overlap of 82\\% with SFT, suggesting stability across training objective variations, but the reasoning-RL question remains open pending availability of more GRPO/PPO models on public leaderboards.\n\n%------------------------------------------------------------------------------\n\\subsection{Comparison with Per-Model Detectors}\n\\label{sec:constat_dvd}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 9: ConStat Perturbation Evaluation.}\nWe compare DIF with ConStat, a perturbation-based per-model contamination detector, on 220 reformulated MMLU items across 15 models.\n\n\\begin{table}[h]\n\\centering\n\\caption{ConStat vs.\\ DIF detection comparison.}\n\\label{tab:constat}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Target} & \\textbf{Rate (non-RL)} & \\textbf{Rate (RL)} & \\textbf{Per-model?} & \\textbf{Requires cohort?} \\\\\n\\midrule\nConStat & Memorization & 0.41 & 0.12 & Yes & No \\\\\nDIF (MH) & Differential funct. & 0.313 & N/A (group) & No & Yes \\\\\nOverlap & Both flag & 0.18 & N/A & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 18\\% overlap between ConStat and DIF flags confirms these methods measure fundamentally different constructs. ConStat detects per-model memorization; DIF detects group-level differential functioning. This orthogonality is \\emph{expected} under the capability-authenticity interpretation: ConStat finds items a specific model memorized, while DIF finds items where capability improvement manifests across model generations. They are complementary, not competing.\n\nConStat shows higher detection rates on non-RL models (41\\% vs.\\ 31.3\\%) but degrades sharply on RL models (12\\%). Paraphrase quality (0.73) and mean difficulty shift (0.08) introduce uncontrolled confounds in the ConStat evaluation.\n\n\\paragraph{Experiment 10: DVD Generation Variance.}\nWe evaluate Distribution of Variance in Decoding (DVD) on 12 models $\\times$ 500 items with 50 temperature-sampled responses per item.\n\n\\begin{table}[h]\n\\centering\n\\caption{DVD results summary.}\n\\label{tab:dvd}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Stability} \\\\\n\\midrule\nBimodal detection rate & 0.23 & $\\pm0.09$ across temperatures \\\\\nVariance AUC & 0.58 & $\\pm0.07$ \\\\\nDIF overlap & 0.14 & Stable \\\\\nCost per model & 5.4 GPU-hrs & Fixed \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDVD achieves near-chance AUC (0.58) with high temperature sensitivity (15--30\\% variation between $T=0.7$ and $T=1.0$). The 14\\% overlap with DIF confirms these methods detect different phenomena. At 65 GPU-hours for 12 models, DVD is expensive relative to its discriminative power. We include this as a negative result: generation variance does not provide a reliable signal for item-level analysis in its current form.\n\n\\paragraph{Experiment 11: Ensemble Fusion.}\nWe fuse DIF, ConStat, and DVD via majority voting and weighted fusion.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ensemble performance.}\n\\label{tab:ensemble}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{AUC} & \\textbf{FPR} \\\\\n\\midrule\nDIF only & 0.29 & 0.31 & 0.54 & 0.31 \\\\\nConStat only & 0.38 & 0.41 & 0.61 & 0.22 \\\\\nDVD only & 0.24 & 0.23 & 0.58 & 0.28 \\\\\nMajority (2-of-3) & 0.31 & 0.15 & 0.55 & 0.14 \\\\\nWeighted fusion (CV) & 0.35 & 0.32 & 0.64 & 0.19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEnsemble fusion provides marginal improvement (AUC 0.64 vs.\\ best single-method 0.61). The 2-of-3 majority voting suffers from low recall (0.15) because the three methods flag largely non-overlapping items (Jaccard 0.14--0.18). Cross-validated weighted fusion shows a 0.08 overfit gap, suggesting weights do not generalize well. Notably, DIF receives the lowest optimized weight (0.22 vs.\\ ConStat 0.51, DVD 0.27), confirming that DIF contributes least to \\emph{contamination detection} specifically---consistent with our reframing that DIF measures capability sensitivity rather than contamination.\n\nThis negative result reinforces that combining individually weak contamination signals does not yield a strong one. The fundamental challenge---lack of item-level contamination ground truth---is not solved by fusion.\n\n%------------------------------------------------------------------------------\n\\subsection{Bifactor IRT and Item Generation}\n\\label{sec:bifactor}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 12a: Bifactor IRT Equating Pilot.}\nMMLU's 57-subject structure raises concerns about unidimensional IRT assumptions. We attempt a bifactor model (1 general $+$ 57 specific factors) to properly account for multidimensionality.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bifactor IRT fit diagnostics---all indices fail standard thresholds.}\n\\label{tab:bifactor}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Threshold} & \\textbf{Verdict} \\\\\n\\midrule\nRMSEA & 0.11 & $<0.08$ & Fail \\\\\nCFI & 0.72 & $>0.90$ & Fail \\\\\nTLI & 0.68 & $>0.90$ & Fail \\\\\nSRMR & 0.09 & $<0.08$ & Fail \\\\\nConvergence & No (48h timeout) & Yes & Fail \\\\\nParameters & $\\sim$25,000 & $<$5,000 practical & Fail \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe bifactor model fails comprehensively. With $\\sim$25,000 parameters (1 general $+$ 57 specific factor loadings $\\times$ 12,508 items), the model requires 180\\,GB RAM and fails to converge within 48 hours. Even partial convergence yields poor fit on all indices.\n\nThis is an honest negative result: MMLU's multidimensional structure exceeds current bifactor IRT modeling capacity. The unidimensionality assumption underlying MH-DIF is violated, but the best available alternative (bifactor) is computationally intractable. Multidimensional IRT methods (MIMIC, MIRT-DIF) remain future work. We note that poor IRT fit implies our DIF analysis may \\emph{underestimate} the true proportion of capability-sensitive items, as model misspecification generally attenuates effect detection.\n\n\\paragraph{Experiment 12b: Item Generation Calibration.}\nWe attempt to generate replacement items for DIF-flagged questions using LLM generation with construct constraints and student simulation calibration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Item generation difficulty calibration results.}\n\\label{tab:itemgen}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Calibration Method} & \\textbf{Difficulty $\\rho$} & \\textbf{Literature Claim} & \\textbf{Achieved} \\\\\n\\midrule\nPrompt targeting & 0.18 & 0.10--0.45 & Low end \\\\\nStudent simulation & 0.34 & 0.75--0.82 & Far below \\\\\nHoldout validation & 0.42 & $>$0.90 needed & Insufficient \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nItem generation produces 300 replacement items across 15 subjects, but calibration quality is poor. Prompt-based difficulty targeting ($\\rho=0.18$) falls at the low end of literature ranges. Student simulation ($\\rho=0.34$) substantially underperforms published results ($\\rho=0.75$--$0.82$)---the discrepancy likely stems from those results being validated on simple math items rather than MMLU's diverse knowledge domains. Cognitive level matching (45\\%) and construct alignment (53\\%) indicate that over half of replacements test different cognitive processes than the originals.\n\nThe holdout panel validation ($\\rho=0.42$) shows replacement items do not preserve model rankings. Combined with the $\\rho=0.997$ finding (Section~\\ref{sec:degradation}), this yields an ironic conclusion: the original DIF items produce more stable rankings than their replacements. At 180 GPU-hours, this is an expensive negative result that strengthens the argument \\emph{against} item replacement and \\emph{for} treating DIF items as valuable capability discriminators.\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\subsection{DIF as Capability Archaeology}\n\nOur results converge on a consistent interpretation: DIF on LLM benchmarks identifies items where genuine capability improvement manifests at the item level. The evidence is multi-faceted:\n\n\\begin{enumerate}\n    \\item \\textbf{Domain correlation} ($\\rho=0.307$): DIF rates track accuracy improvement across MMLU domains.\n    \\item \\textbf{Within-family signal} (C\\%$=61.3$): Even within the Llama family (same data pipeline), DIF identifies where architectural/training improvements manifest.\n    \\item \\textbf{Anti-correlation with contamination} ($r=-0.478$): Contaminated models perform \\emph{worse} on DIF items.\n    \\item \\textbf{Smooth temporal trend} (IFT coefficient$=0.08$): Item difficulty changes gradually, consistent with capability improvement rather than abrupt contamination.\n    \\item \\textbf{Replacement failure} ($\\rho=0.42$): DIF items produce more stable rankings than generated replacements.\n\\end{enumerate}\n\nThis reframes DIF from a contamination detector (which it is not, on these data) to a \\emph{capability archaeology} tool: it identifies which benchmark items carry the discriminative signal between model generations.\n\n\\subsection{Measurement Efficiency Implications}\n\nThe $\\rho=0.997$ result under 31\\% item removal, combined with $\\rho=0.972$ at 50\\% removal, reveals that MMLU is approximately $3\\times$ larger than necessary for stable rankings. DIF identifies the informative core---the items that actually contribute to ranking discrimination. This has practical implications for evaluation efficiency: a DIF-curated subset could achieve comparable ranking fidelity at one-third the cost.\n\n\\subsection{Limitations}\n\n\\paragraph{Unidimensionality violation.} MH-DIF assumes unidimensional ability, but MMLU spans 57 subjects. Bifactor IRT failed to converge (Section~\\ref{sec:bifactor}), and decoder-only stratification did not improve fit (Section~\\ref{sec:arch_strat}). Our DIF analysis should be interpreted as a pragmatic approximation. Multidimensional DIF methods (MIMIC, MIRT-DIF) are needed for rigorous treatment.\n\n\\paragraph{Semi-synthetic ecological validity.} The incorrect$\\to$correct flipping mechanism does not model realistic contamination pathways. The $\\Delta$TPR framework provides sensitivity calibration, not contamination detection validation.\n\n\\paragraph{Sample sizes.} GSM1K validation uses $N=33$ models (wide CI). RL robustness analysis has only $N=13$ reasoning-RL models (underpowered). Both require larger samples for definitive conclusions.\n\n\\paragraph{No contamination ground truth.} We cannot decompose the 31.3\\% DIF rate into contamination vs.\\ capability components. The capability interpretation is supported by converging evidence, but contamination may contribute to some fraction of flagged items.\n\n\\paragraph{Ensemble weakness.} The fusion of DIF, ConStat, and DVD produces marginal improvement (AUC 0.64) with non-generalizing weights. Three individually weak signals do not combine into a strong one without shared ground truth.\n\n\\paragraph{Cumulative FPR inflation.} Bayesian evidence accumulation improves power but inflates FPR from 0.05 to 0.11 over four administrations, limiting practical applicability without correction mechanisms.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Benchmark contamination detection.} Several methods detect contamination in LLMs: Min-K\\% probability-based detection, $n$-gram overlap analysis, and ConStat perturbation-based testing. These operate at the per-model level and validate against web-overlap labels. Our work differs in applying group-level psychometric analysis and demonstrating that web-overlap labels are inappropriate for item-level differential detection.\n\n\\paragraph{DIF in educational testing.} DIF analysis has a long history in psychometrics, with the MH procedure introduced by Holland and Thayer (1988). Applications to computerized adaptive testing and item banking are standard practice. Sinharay et al.\\ (2006) introduced Bayesian approaches to cumulative DIF. Our work is the first large-scale application to LLM benchmarks.\n\n\\paragraph{Benchmark evaluation methodology.} Growing Pains (Polo et al., 2024) uses anchor items for efficient evaluation via IRT equating. Our DIF diagnostic complements this by identifying which anchor items are degrading across model generations. The METABENCH repository provides the large-scale response matrices enabling our analysis.\n\n\\paragraph{LLM-based item generation.} Recent work explores using LLMs to generate test items with calibrated difficulty. Published correlations ($\\rho=0.75$--$0.82$) were achieved on constrained math items; our attempt on MMLU's diverse domains achieved substantially lower calibration ($\\rho=0.34$).\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe present the largest DIF analysis on LLM benchmarks to date, analyzing 5,219 models across 12,508 MMLU items. Our core finding is that DIF identifies \\emph{capability-authentic} benchmark items---the items where genuine model improvement manifests at the item level. The 31.3\\% of MMLU items flagged by DIF are not defective; they are the discriminative core that differentiates model generations. Cross-benchmark validation confirms this interpretation: DIF flags anti-correlate with contamination ($r=-0.478$, $p=0.005$).\n\nWe contribute a semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR$=0.000$) and extensive negative results from twelve experiments that map the operational boundaries of psychometric methods in LLM evaluation. The graceful degradation analysis reveals MMLU's massive redundancy ($\\rho=0.972$ at 50\\% removal), suggesting that DIF-guided benchmark curation could improve evaluation efficiency by a factor of three.\n\nFuture work should address the unidimensionality limitation via multidimensional IRT, expand RL robustness analysis as more reasoning-RL models become available, and develop contamination ground truth that enables decomposing capability and contamination contributions to DIF.\n\n%==============================================================================\n% References\n%==============================================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{99}\n\n\\bibitem[Holland and Thayer(1988)]{holland1988}\nHolland, P.~W. and Thayer, D.~T. (1988).\n\\newblock Differential item functioning and the Mantel-Haenszel procedure.\n\\newblock In \\emph{Test Validity}, pages 129--145.\n\n\\bibitem[Li et al.(2024)]{li2024}\nLi, Y., et al. (2024).\n\\newblock Open {LLM} Leaderboard contamination detection.\n\\newblock Technical report.\n\n\\bibitem[Polo et al.(2024)]{polo2024}\nPolo, F.~M., et al. (2024).\n\\newblock {Growing Pains}: Understanding the impact of model updates on benchmark evaluation via {IRT}.\n\\newblock In \\emph{NeurIPS 2024 Datasets and Benchmarks Track}.\n\n\\bibitem[Sinharay et al.(2006)]{sinharay2006}\nSinharay, S., Johnson, M.~S., and Stern, H.~S. (2006).\n\\newblock Posterior predictive assessment of item response theory models.\n\\newblock \\emph{Applied Psychological Measurement}, 30(4):298--321.\n\n\\bibitem[Oren et al.(2024)]{oren2024}\nOren, Y., et al. (2024).\n\\newblock Proving test set contamination in black-box language models.\n\\newblock In \\emph{ICLR 2024}.\n\n\\bibitem[Deconinck et al.(2024)]{deconinck2024}\nDeconinck, K., et al. (2024).\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock In \\emph{EMNLP 2024}.\n\n\\bibitem[Tutz and Berger(2016)]{tutz2016}\nTutz, G. and Berger, M. (2016).\n\\newblock Item-focused trees for the identification of items in differential item functioning.\n\\newblock \\emph{Psychometrika}, 81(3):727--750.\n\n\\bibitem[Hendrycks et al.(2021)]{hendrycks2021}\nHendrycks, D., et al. (2021).\n\\newblock Measuring massive multitask language understanding.\n\\newblock In \\emph{ICLR 2021}.\n\n\\bibitem[Cobbe et al.(2021)]{cobbe2021}\nCobbe, K., et al. (2021).\n\\newblock Training verifiers to solve math word problems.\n\\newblock \\emph{arXiv preprint arXiv:2110.14168}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bc085a7-3121-4429-b3f7-d33635ef9f24",
  "isSidechain": false,
  "requestId": "req_011CbEt277rcnkFbKAsxpTCd",
  "type": "assistant",
  "uuid": "c5d67a03-937d-4bf3-beb7-3f055ec74b61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013uihiwXwgUsXS1JSdRFg1H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4238,
      "cache_read_input_tokens": 37657,
      "output_tokens": 12056,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12056,
          "cache_read_input_tokens": 37657,
          "cache_creation_input_tokens": 4238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4238
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

_source line 22 · 2026-05-21T01:58:06.775Z_

<details><summary>↩ Tool result · `toolu_01Nts3JnWMjHBw9Yff9q3q1n`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5d67a03-937d-4bf3-beb7-3f055ec74b61",
  "isSidechain": false,
  "promptId": "41166657-dacb-41c2-9c9f-045334e8b1ff",
  "type": "user",
  "uuid": "df63c027-df95-4ee6-857e-8846f9c89963",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/paper.tex",
    "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\title{Identifying Capability-Authentic Benchmark Items via Differential Item Functioning}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nLarge language model benchmarks implicitly assume that items measure the same construct across model generations. We challenge this assumption by applying Differential Item Functioning (DIF) analysis---a classical psychometric technique---to the METABENCH response matrix (5,219 models $\\times$ 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\nWe find that 31.3\\% of MMLU items are \\emph{capability-sensitive}: they exhibit large DIF between 2023 and 2024-H1 model cohorts (ETS category C, $|\\Delta_{\\mathrm{MH}}|\\ge1.5$). Rather than indicating benchmark pathology, these items concentrate the discriminative signal that differentiates model generations---their removal disrupts rankings significantly more than random removal ($z=-8$ to $-49\\sigma$). Cross-benchmark validation on GSM8K confirms that DIF-flagged items \\emph{anti-correlate} with contamination ($r=-0.478$, $p=0.005$, $N=33$): contaminated models perform worse on DIF items, indicating DIF captures genuine capability differences that memorization cannot replicate.\nDownstream impact analysis reveals massive benchmark redundancy: removing all DIF items changes the Spearman rank correlation by only $\\rho=0.997$, implying MMLU is roughly three times larger than necessary for stable rankings. We contribute a reusable semi-synthetic validation framework with cross-subject matching that eliminates false positive rate inflation ($\\Delta\\mathrm{FPR}=0.000$). We further report extensive negative results from twelve experiments---including bifactor IRT failure, underpowered RL robustness tests, and weak ensemble fusion---to map the operational boundaries of DIF in the LLM evaluation setting.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nWhen we declare that ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent construct measured under comparable conditions. In educational testing, this assumption is routinely audited via Differential Item Functioning (DIF) analysis, which detects items that behave differently across examinee subgroups after controlling for overall ability. If a math item is harder for one demographic group than another, conditional on equal math ability, the item exhibits DIF and threatens fair measurement.\n\nLLM benchmarks face an analogous threat. As model capabilities evolve rapidly across generations, benchmark items may shift in effective difficulty---not because the items changed, but because the relationship between model capability and item response changed. An item that once discriminated between strong and weak models may become trivially easy for all modern models, or conversely, an item that tested surface-level pattern matching may now require genuine reasoning from models that have moved beyond shallow heuristics.\n\nWe apply Mantel-Haenszel (MH) DIF analysis to the METABENCH repository, analyzing 5,219 models across 12,508 MMLU items. Our central finding reframes the role of DIF in LLM evaluation: items flagged by DIF are not ``broken''---they are \\emph{capability-authentic}. They are the items where genuine capability improvement manifests at the item level, and they concentrate the signal that distinguishes model generations.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}\n    \\item \\textbf{Capability-sensitive item identification.} We show that 31.3\\% of MMLU items exhibit large temporal DIF, and that this rate is robust to architecture stratification (decoder-only: 33.1\\%), correlates with domain-level accuracy improvement ($\\rho=0.307$, $p=0.02$), and cannot be attributed to statistical noise (random split: 0.18\\%).\n    \\item \\textbf{Cross-benchmark capability validation.} On GSM8K ($1{,}319$ items $\\times$ $6{,}702$ models), DIF flags anti-correlate with the GSM1K contamination gap ($r=-0.478$, $p=0.005$). Contaminated models---those with inflated GSM8K scores relative to the held-out GSM1K---perform \\emph{worse} on DIF items. DIF identifies items where genuine capability matters.\n    \\item \\textbf{Measurement efficiency characterization.} Rank correlation remains $\\rho\\ge0.972$ even after replacing 50\\% of items, revealing that MMLU is roughly $3\\times$ larger than needed for stable rankings. DIF items form the informative core.\n    \\item \\textbf{Semi-synthetic validation framework.} We introduce a $\\Delta$TPR methodology with cross-subject matching ($\\Delta$FPR$=0.000$), providing reusable calibration infrastructure for item-level detectors.\n    \\item \\textbf{Comprehensive negative results.} We report twelve experiments including bifactor IRT failure, weak ensemble fusion, underpowered RL robustness, and unsuccessful item generation, mapping the operational boundaries of psychometric methods in LLM evaluation.\n\\end{enumerate}\n\n%==============================================================================\n\\section{Background}\n\\label{sec:background}\n%==============================================================================\n\n\\subsection{Differential Item Functioning}\n\nIn classical test theory, an item exhibits DIF when examinees of equal ability from different groups have different probabilities of answering correctly. The Mantel-Haenszel (MH) procedure is the most widely used DIF detection method. It stratifies examinees by total score (as a proxy for ability), then tests whether the odds ratio of correct response differs between a reference group and a focal group across strata. The MH odds ratio $\\alpha_{\\mathrm{MH}}$ is converted to the $\\Delta_{\\mathrm{MH}}$ scale:\n\\begin{equation}\n    \\Delta_{\\mathrm{MH}} = -2.35 \\ln(\\alpha_{\\mathrm{MH}})\n\\end{equation}\nItems are classified by the Educational Testing Service (ETS) scheme: category A ($|\\Delta_{\\mathrm{MH}}|<1.0$, negligible), B ($1.0\\le|\\Delta_{\\mathrm{MH}}|<1.5$, moderate), and C ($|\\Delta_{\\mathrm{MH}}|\\ge1.5$, large DIF). We focus on category C items as indicators of substantial differential functioning.\n\n\\subsection{DIF in the LLM Context}\n\nIn our setting, ``examinees'' are LLM models and ``groups'' are temporal cohorts (2023 vs.\\ 2024-H1 release dates). An item with large temporal DIF functions differently across model generations conditional on overall benchmark performance. We hypothesize that such items are \\emph{capability-sensitive}: they are precisely the items where genuine capability improvement (or degradation) manifests, as opposed to items that are universally easy or hard regardless of generation.\n\n%==============================================================================\n\\section{Data}\n\\label{sec:data}\n%==============================================================================\n\nWe use the METABENCH repository, which aggregates benchmark responses from publicly available LLMs. Our primary dataset is the MMLU response matrix: 5,219 models $\\times$ 12,508 items across 57 subject domains. For cross-benchmark validation, we use the GSM8K response matrix: 6,702 models $\\times$ 1,319 items. External validation uses GSM1K contamination gap data for 33 matched models.\n\n%==============================================================================\n\\section{Experiments and Results}\n\\label{sec:experiments}\n%==============================================================================\n\nWe report results from twelve experiments. We organize them into four thematic groups: (1) core DIF characterization, (2) cross-benchmark and external validation, (3) methodological extensions, and (4) negative results that map operational boundaries.\n\n%------------------------------------------------------------------------------\n\\subsection{Core DIF Characterization on MMLU}\n\\label{sec:core_dif}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 1: Temporal DIF Analysis.}\nWe apply MH-DIF to the full MMLU matrix with temporal cohort splits (2023 vs.\\ 2024-H1). Table~\\ref{tab:dif_summary} summarizes detection rates under four cohort definitions.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF detection rates (ETS category C) under different cohort definitions.}\n\\label{tab:dif_summary}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Cohort Definition} & \\textbf{C\\%} & \\textbf{Enrichment vs.\\ Li} & \\textbf{Interpretation} \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024) & 31.3 & 0.96 & Capability gain across generations \\\\\nAbility quintile & 2.9 & 1.19 & Items function consistently across ability \\\\\nWithin-family (Llama-2 vs.\\ 3) & 61.3 & N/A & Pure capability gain, same pipeline \\\\\nRandom split (sanity) & 0.18 & N/A & Confirms real signal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe temporal C\\%$=31.3$ indicates that nearly one-third of items function differently across model generations. The random split sanity check (0.18\\%) confirms this is not statistical noise. The within-family Llama-2 vs.\\ Llama-3 comparison is particularly informative: 61.3\\% of items show large DIF within the same model family (same training data pipeline, same organization), attributable to architectural and training improvements rather than data contamination.\n\nThe enrichment against Li et al.\\ contamination labels is 0.96---effectively null. This means DIF-flagged items are no more likely to be labeled as contaminated by web-overlap methods than non-flagged items. We interpret this as evidence that DIF and web-overlap labels measure orthogonal constructs: DIF captures differential item functioning (how items behave differently across groups), while web-overlap captures global data exposure (whether an item appears on the public internet).\n\n\\paragraph{Domain-level correlation.}\nThe Spearman correlation between domain-level DIF rates and domain-level accuracy improvement is $\\rho=0.307$ ($p=0.02$). Domains where models improved most between generations have the highest DIF rates. This confirms that DIF tracks capability improvement at the domain level, explaining 9.4\\% of cross-domain variance.\n\n\\begin{table}[h]\n\\centering\n\\caption{Domain-level correlation between DIF rate and accuracy improvement.}\n\\label{tab:domain_corr}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Interpretation} \\\\\n\\midrule\nSpearman $\\rho$ (DIF vs.\\ accuracy gain) & 0.307 & DIF tracks capability improvement \\\\\n$p$-value & 0.02 & Statistically significant \\\\\nVariance explained & 9.4\\% & Partial; other factors contribute \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------------------\n\\subsection{Architecture Stratification}\n\\label{sec:arch_strat}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 2: Decoder-Only Subpopulation.}\nA potential confound is architectural heterogeneity: encoder-decoder and hybrid models may inflate DIF rates. We restrict analysis to decoder-only models ($N=3{,}400$) and recompute DIF.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF rates and IRT fit diagnostics: full population vs.\\ decoder-only.}\n\\label{tab:arch_strat}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Population} & \\textbf{$N$} & \\textbf{C\\%} & \\textbf{RMSEA} & \\textbf{CFI} & \\textbf{TLI} \\\\\n\\midrule\nFull population & 5,219 & 31.3 & --- & --- & --- \\\\\nDecoder-only & 3,400 & 33.1 & 0.092 & 0.81 & 0.78 \\\\\n\\midrule\n$\\Delta$ & $-1{,}819$ & $+1.8$ & \\multicolumn{3}{c}{All below thresholds} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nArchitecture stratification does not reduce DIF rates (C\\% increases slightly from 31.3\\% to 33.1\\%). IRT fit indices remain below standard thresholds (RMSEA$>0.08$, CFI$<0.90$, TLI$<0.90$), confirming that the unidimensionality violation stems from MMLU's 57-subject structure, not architectural heterogeneity. Detection power is essentially unchanged ($\\Delta$FPR$=+0.012$, $\\Delta$TPR$=-0.014$).\n\nThis result is informative for the capability-authenticity interpretation: DIF item sensitivity is robust to population composition.\n\n%------------------------------------------------------------------------------\n\\subsection{Cross-Benchmark Validation: GSM8K and GSM1K}\n\\label{sec:cross_bench}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 3: GSM8K Replication and GSM1K Anti-Correlation.}\nWe replicate DIF analysis on GSM8K (1,319 items $\\times$ 6,702 models), finding a temporal C\\%$=18.9$---lower than MMLU's 31.3\\%, confirming that DIF rates are benchmark-specific rather than universal.\n\nThe headline finding concerns GSM1K, a held-out test set designed to measure contamination. For 33 models with both GSM8K and GSM1K scores, we correlate DIF flag rates with the contamination gap (GSM8K minus GSM1K accuracy):\n\n\\begin{table}[h]\n\\centering\n\\caption{GSM1K contamination gap correlation with DIF flags.}\n\\label{tab:gsm1k}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Estimate} & \\textbf{95\\% CI} & \\textbf{Implication} \\\\\n\\midrule\nPearson $r$ & $-0.478$ & $[-0.71, -0.12]$ & Anti-correlation with contamination \\\\\nPartial $r$ (controlling accuracy) & $-0.385$ & $[-0.64, -0.04]$ & Robust to ability confound \\\\\nPermutation $p$ & 0.014 & --- & Significant \\\\\nLeave-one-out min $|r|$ & 0.374 & --- & No single model drives result \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe anti-correlation is striking: models with larger contamination gaps (Phi, Gemma families---those whose GSM8K scores are most inflated relative to GSM1K) perform \\emph{worse} on DIF-flagged items. Contamination produces shallow performance gains concentrated on non-DIF items. DIF items require genuine capability that memorization cannot replicate.\n\n\\textbf{Caveats.} The bootstrap CI $[-0.71, -0.12]$ is wide due to $N=33$. Removing the highest-leverage point (Deepseek-math-7b-rl, Cook's $D$ maximum) reduces $|r|$ by 22\\% to 0.374. Multiple testing correction was not applied. These limitations are inherent to the small sample of models with matched GSM1K data.\n\n\\paragraph{Semi-synthetic validation on GSM8K.}\nThe semi-synthetic framework (Section~\\ref{sec:semisynthetic}) replicates on GSM8K with $\\Delta$TPR$=0.818$ at $p=1.0$ injection, confirming framework portability.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-benchmark DIF rates.}\n\\label{tab:cross_bench}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{Temporal C\\%} & \\textbf{Interpretation} \\\\\n\\midrule\nMMLU & 31.3 & High capability sensitivity \\\\\nGSM8K & 18.9 & Lower---benchmark-dependent \\\\\n$\\Delta$ & 12.4 & No universal rate \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------------------\n\\subsection{Semi-Synthetic Validation Framework}\n\\label{sec:semisynthetic}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 4: Controlled Contamination Injection.}\nWe inject known differential contamination into the real METABENCH response matrix by flipping incorrect$\\to$correct responses with probability $p$ for a subset of models, then measure DIF detection power increase ($\\Delta$TPR$=$TPR$_{\\text{injected}}-$TPR$_{\\text{baseline}}$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Semi-synthetic $\\Delta$TPR under varying injection rates.}\n\\label{tab:semisynthetic}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Injection Rate $p$} & \\textbf{$\\Delta$TPR (standard)} & \\textbf{$\\Delta$TPR (cross-subject)} & \\textbf{Note} \\\\\n\\midrule\n0.3 & 0.222 & 0.18 & Below useful detection \\\\\n0.5 & 0.508 & 0.36 & Moderate detection \\\\\n0.7 & 0.664 & 0.52 & Strong detection \\\\\n1.0 & 0.674 & 0.62 & Saturates---ceiling effect \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe dose-response relationship confirms that DIF detection power increases monotonically with injection intensity, providing a calibration curve for the method's sensitivity.\n\n\\paragraph{Cross-subject matching eliminates FPR inflation.}\nA critical methodological contribution: when the matching variable (total score) includes contaminated items, FPR inflates. Using total score on \\emph{other} subjects as the matching variable eliminates this:\n\n\\begin{table}[h]\n\\centering\n\\caption{Matching strategy comparison for FPR control.}\n\\label{tab:matching}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Matching Strategy} & \\textbf{FPR (baseline)} & \\textbf{FPR (at $p=1.0$)} & \\textbf{$\\Delta$FPR} & \\textbf{Verdict} \\\\\n\\midrule\nStandard MH & 0.298 & 0.616 & $+0.318$ & FPR inflates \\\\\nExternal 5-subject & 0.314 & 0.314 & 0.000 & Stable \\\\\nCross-subject & 0.330 & 0.330 & 0.000 & Stable (recommended) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-subject matching achieves $\\Delta$FPR$=0.000$ across all tested conditions. This is a reusable methodological recommendation for any item-level detector that conditions on total score.\n\n\\textbf{Ecological validity caveat.} The injection mechanism (deterministic incorrect$\\to$correct flipping) is a simplification. Real contamination involves partial memorization, shallow pattern matching, and chain-of-thought reasoning from memorized premises---none of which produce the clean flipping assumed here. The semi-synthetic framework should be understood as \\emph{calibration infrastructure} characterizing detection sensitivity, not as a direct model of real-world contamination.\n\n%------------------------------------------------------------------------------\n\\subsection{Measurement Efficiency: Graceful Degradation}\n\\label{sec:degradation}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 5: Progressive Item Replacement.}\nWe analyze how benchmark validity degrades as items are progressively replaced, quantifying MMLU's measurement redundancy.\n\n\\begin{table}[h]\n\\centering\n\\caption{Benchmark validity under progressive item replacement.}\n\\label{tab:degradation}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Replacement \\%} & \\textbf{Rank $\\rho$} & \\textbf{Reliability $\\alpha$} & \\textbf{Subjects Covered} & \\textbf{Verdict} \\\\\n\\midrule\n0 & 1.000 & 0.94 & 57 & Baseline \\\\\n5 & 0.998 & 0.93 & 57 & Negligible \\\\\n10 & 0.996 & 0.93 & 57 & Negligible \\\\\n20 & 0.991 & 0.91 & 56 & Minor \\\\\n31 (DIF removal) & 0.987 & 0.90 & 55 & DIF removal point \\\\\n50 & 0.972 & 0.88 & 52 & Still acceptable \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEven at 50\\% replacement, rank correlation remains $\\rho=0.972$ and reliability $\\alpha=0.88$ (above the standard 0.70 threshold). The theoretical bound $\\rho\\ge0.95$ holds up to 38\\% replacement---closely matching the DIF flagging rate (31.3\\%).\n\n\\textbf{Key insight.} This result has a dual interpretation. On one hand, it suggests DIF items can be safely removed without disrupting rankings. On the other hand---and we argue this is the more informative reading---it reveals that \\emph{MMLU is approximately three times larger than necessary for stable model rankings}. DIF analysis identifies which items form the informative core and which are redundant. The 31.3\\% of capability-sensitive items are precisely the items that carry discriminative signal between model generations; the remaining $\\sim$69\\% contribute mainly to reliability through redundancy.\n\n%------------------------------------------------------------------------------\n\\subsection{Item-Focused Trees: Continuous Temporal Analysis}\n\\label{sec:ift}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 6: IFT vs.\\ MH Comparison.}\nItem-Focused Trees (IFT) model DIF as a smooth function of a continuous covariate (model release date), avoiding the arbitrary temporal cohort split required by MH.\n\n\\begin{table}[h]\n\\centering\n\\caption{Item-Focused Trees vs.\\ MH-DIF comparison.}\n\\label{tab:ift}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Flagging Rate} & \\textbf{Unique Flags} & \\textbf{Cost Ratio} & \\textbf{Temporal Pattern} \\\\\n\\midrule\nMH (categorical) & 0.313 & 0.04 & 1.0$\\times$ & Discrete cohort split \\\\\nIFT (continuous) & 0.34 & 0.06 & 12.0$\\times$ & Smooth positive trend \\\\\nOverlap & 0.78 & --- & --- & Same underlying signal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 78\\% overlap confirms both methods detect the same underlying phenomenon. IFT's continuous release-date coefficient (mean$=0.08$, SD$=0.15$) reveals a smooth positive trend: items become easier over time, consistent with gradual capability improvement rather than abrupt contamination events. However, IFT's 12$\\times$ computational cost makes it impractical at scale. We recommend MH for detection and IFT as a supplementary diagnostic for characterizing temporal dynamics.\n\n%------------------------------------------------------------------------------\n\\subsection{Cumulative Bayesian DIF}\n\\label{sec:bayesian}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 7: Evidence Accumulation Across Administrations.}\nWe implement cumulative Bayesian DIF priors following Sinharay et al.\\ (2006), simulating four successive benchmark administrations to test whether accumulating evidence across administrations improves detection power.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cumulative Bayesian DIF power trajectory.}\n\\label{tab:bayesian}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$N$ Administrations} & \\textbf{TPR ($\\delta=1.0$)} & \\textbf{TPR ($\\delta=1.4$)} & \\textbf{FPR} & \\textbf{Net Gain} \\\\\n\\midrule\n1 & 0.38 & 0.68 & 0.05 & Baseline \\\\\n2 & 0.49 & 0.78 & 0.07 & $+0.11/+0.10$ \\\\\n3 & 0.58 & 0.84 & 0.09 & $+0.09/+0.06$ \\\\\n4 & 0.64 & 0.87 & 0.11 & $+0.06/+0.03$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPower improves from 0.38 to 0.64 for medium effects ($\\delta=1.0$) over four administrations. However, FPR inflates from 0.05 to 0.11---each administration's prior carries forward false positive evidence. The diminishing returns (net gain decreases each round) combined with cumulative FPR inflation make this approach impractical in its current form. The concept of longitudinal capability tracking remains promising, but requires FPR correction mechanisms not implemented here.\n\n%------------------------------------------------------------------------------\n\\subsection{RL Robustness Analysis}\n\\label{sec:rl}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 8: DIF Stability Across Training Paradigms.}\nWe examine whether DIF detection is robust to reinforcement learning (RL) training by comparing flag patterns across SFT, alignment-RL (DPO/ORPO, $N=477$), and reasoning-RL (GRPO/PPO, $N=13$) model cohorts.\n\n\\begin{table}[h]\n\\centering\n\\caption{RL robustness comparison. All comparisons are statistically non-significant.}\n\\label{tab:rl}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{SFT AUROC} & \\textbf{Alignment-RL} & \\textbf{Reasoning-RL} & \\textbf{95\\% CI Width} \\\\\n\\midrule\nDIF (MH) & 0.69 & 0.66 & 0.65 & $\\pm0.14$ \\\\\nMin-K\\% & 0.63 & 0.58 & 0.44 & $\\pm0.18$ \\\\\nConStat & 0.67 & 0.61 & 0.51 & $\\pm0.16$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Statistical tests for RL robustness---all non-significant.}\n\\label{tab:rl_stats}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Test} & \\textbf{Statistic} & \\textbf{$p$} & \\textbf{Conclusion} \\\\\n\\midrule\nDIF vs.\\ ConStat (RL) & DeLong & $z=1.19$ & 0.23 & Cannot reject $H_0$ \\\\\nDIF retention equiv. & TOST & $t=0.96$ & 0.34 & Cannot claim equivalence \\\\\nFlag overlap SFT vs.\\ RL & Bootstrap Jaccard & 0.71 & CI $[0.54,0.88]$ & Wide CI, inconclusive \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis experiment is \\textbf{fatally underpowered}. With only $N=13$ reasoning-RL models, no comparison reaches statistical significance. DIF shows numerically stable AUROC across training paradigms (0.69$\\to$0.65), while Min-K\\% degrades substantially (0.63$\\to$0.44), but we cannot draw reliable conclusions. The alignment-RL cohort ($N=477$) shows DIF flag overlap of 82\\% with SFT, suggesting stability across training objective variations, but the reasoning-RL question remains open pending availability of more GRPO/PPO models on public leaderboards.\n\n%------------------------------------------------------------------------------\n\\subsection{Comparison with Per-Model Detectors}\n\\label{sec:constat_dvd}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 9: ConStat Perturbation Evaluation.}\nWe compare DIF with ConStat, a perturbation-based per-model contamination detector, on 220 reformulated MMLU items across 15 models.\n\n\\begin{table}[h]\n\\centering\n\\caption{ConStat vs.\\ DIF detection comparison.}\n\\label{tab:constat}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Target} & \\textbf{Rate (non-RL)} & \\textbf{Rate (RL)} & \\textbf{Per-model?} & \\textbf{Requires cohort?} \\\\\n\\midrule\nConStat & Memorization & 0.41 & 0.12 & Yes & No \\\\\nDIF (MH) & Differential funct. & 0.313 & N/A (group) & No & Yes \\\\\nOverlap & Both flag & 0.18 & N/A & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 18\\% overlap between ConStat and DIF flags confirms these methods measure fundamentally different constructs. ConStat detects per-model memorization; DIF detects group-level differential functioning. This orthogonality is \\emph{expected} under the capability-authenticity interpretation: ConStat finds items a specific model memorized, while DIF finds items where capability improvement manifests across model generations. They are complementary, not competing.\n\nConStat shows higher detection rates on non-RL models (41\\% vs.\\ 31.3\\%) but degrades sharply on RL models (12\\%). Paraphrase quality (0.73) and mean difficulty shift (0.08) introduce uncontrolled confounds in the ConStat evaluation.\n\n\\paragraph{Experiment 10: DVD Generation Variance.}\nWe evaluate Distribution of Variance in Decoding (DVD) on 12 models $\\times$ 500 items with 50 temperature-sampled responses per item.\n\n\\begin{table}[h]\n\\centering\n\\caption{DVD results summary.}\n\\label{tab:dvd}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Stability} \\\\\n\\midrule\nBimodal detection rate & 0.23 & $\\pm0.09$ across temperatures \\\\\nVariance AUC & 0.58 & $\\pm0.07$ \\\\\nDIF overlap & 0.14 & Stable \\\\\nCost per model & 5.4 GPU-hrs & Fixed \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDVD achieves near-chance AUC (0.58) with high temperature sensitivity (15--30\\% variation between $T=0.7$ and $T=1.0$). The 14\\% overlap with DIF confirms these methods detect different phenomena. At 65 GPU-hours for 12 models, DVD is expensive relative to its discriminative power. We include this as a negative result: generation variance does not provide a reliable signal for item-level analysis in its current form.\n\n\\paragraph{Experiment 11: Ensemble Fusion.}\nWe fuse DIF, ConStat, and DVD via majority voting and weighted fusion.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ensemble performance.}\n\\label{tab:ensemble}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{AUC} & \\textbf{FPR} \\\\\n\\midrule\nDIF only & 0.29 & 0.31 & 0.54 & 0.31 \\\\\nConStat only & 0.38 & 0.41 & 0.61 & 0.22 \\\\\nDVD only & 0.24 & 0.23 & 0.58 & 0.28 \\\\\nMajority (2-of-3) & 0.31 & 0.15 & 0.55 & 0.14 \\\\\nWeighted fusion (CV) & 0.35 & 0.32 & 0.64 & 0.19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEnsemble fusion provides marginal improvement (AUC 0.64 vs.\\ best single-method 0.61). The 2-of-3 majority voting suffers from low recall (0.15) because the three methods flag largely non-overlapping items (Jaccard 0.14--0.18). Cross-validated weighted fusion shows a 0.08 overfit gap, suggesting weights do not generalize well. Notably, DIF receives the lowest optimized weight (0.22 vs.\\ ConStat 0.51, DVD 0.27), confirming that DIF contributes least to \\emph{contamination detection} specifically---consistent with our reframing that DIF measures capability sensitivity rather than contamination.\n\nThis negative result reinforces that combining individually weak contamination signals does not yield a strong one. The fundamental challenge---lack of item-level contamination ground truth---is not solved by fusion.\n\n%------------------------------------------------------------------------------\n\\subsection{Bifactor IRT and Item Generation}\n\\label{sec:bifactor}\n%------------------------------------------------------------------------------\n\n\\paragraph{Experiment 12a: Bifactor IRT Equating Pilot.}\nMMLU's 57-subject structure raises concerns about unidimensional IRT assumptions. We attempt a bifactor model (1 general $+$ 57 specific factors) to properly account for multidimensionality.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bifactor IRT fit diagnostics---all indices fail standard thresholds.}\n\\label{tab:bifactor}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Threshold} & \\textbf{Verdict} \\\\\n\\midrule\nRMSEA & 0.11 & $<0.08$ & Fail \\\\\nCFI & 0.72 & $>0.90$ & Fail \\\\\nTLI & 0.68 & $>0.90$ & Fail \\\\\nSRMR & 0.09 & $<0.08$ & Fail \\\\\nConvergence & No (48h timeout) & Yes & Fail \\\\\nParameters & $\\sim$25,000 & $<$5,000 practical & Fail \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe bifactor model fails comprehensively. With $\\sim$25,000 parameters (1 general $+$ 57 specific factor loadings $\\times$ 12,508 items), the model requires 180\\,GB RAM and fails to converge within 48 hours. Even partial convergence yields poor fit on all indices.\n\nThis is an honest negative result: MMLU's multidimensional structure exceeds current bifactor IRT modeling capacity. The unidimensionality assumption underlying MH-DIF is violated, but the best available alternative (bifactor) is computationally intractable. Multidimensional IRT methods (MIMIC, MIRT-DIF) remain future work. We note that poor IRT fit implies our DIF analysis may \\emph{underestimate} the true proportion of capability-sensitive items, as model misspecification generally attenuates effect detection.\n\n\\paragraph{Experiment 12b: Item Generation Calibration.}\nWe attempt to generate replacement items for DIF-flagged questions using LLM generation with construct constraints and student simulation calibration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Item generation difficulty calibration results.}\n\\label{tab:itemgen}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Calibration Method} & \\textbf{Difficulty $\\rho$} & \\textbf{Literature Claim} & \\textbf{Achieved} \\\\\n\\midrule\nPrompt targeting & 0.18 & 0.10--0.45 & Low end \\\\\nStudent simulation & 0.34 & 0.75--0.82 & Far below \\\\\nHoldout validation & 0.42 & $>$0.90 needed & Insufficient \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nItem generation produces 300 replacement items across 15 subjects, but calibration quality is poor. Prompt-based difficulty targeting ($\\rho=0.18$) falls at the low end of literature ranges. Student simulation ($\\rho=0.34$) substantially underperforms published results ($\\rho=0.75$--$0.82$)---the discrepancy likely stems from those results being validated on simple math items rather than MMLU's diverse knowledge domains. Cognitive level matching (45\\%) and construct alignment (53\\%) indicate that over half of replacements test different cognitive processes than the originals.\n\nThe holdout panel validation ($\\rho=0.42$) shows replacement items do not preserve model rankings. Combined with the $\\rho=0.997$ finding (Section~\\ref{sec:degradation}), this yields an ironic conclusion: the original DIF items produce more stable rankings than their replacements. At 180 GPU-hours, this is an expensive negative result that strengthens the argument \\emph{against} item replacement and \\emph{for} treating DIF items as valuable capability discriminators.\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\subsection{DIF as Capability Archaeology}\n\nOur results converge on a consistent interpretation: DIF on LLM benchmarks identifies items where genuine capability improvement manifests at the item level. The evidence is multi-faceted:\n\n\\begin{enumerate}\n    \\item \\textbf{Domain correlation} ($\\rho=0.307$): DIF rates track accuracy improvement across MMLU domains.\n    \\item \\textbf{Within-family signal} (C\\%$=61.3$): Even within the Llama family (same data pipeline), DIF identifies where architectural/training improvements manifest.\n    \\item \\textbf{Anti-correlation with contamination} ($r=-0.478$): Contaminated models perform \\emph{worse} on DIF items.\n    \\item \\textbf{Smooth temporal trend} (IFT coefficient$=0.08$): Item difficulty changes gradually, consistent with capability improvement rather than abrupt contamination.\n    \\item \\textbf{Replacement failure} ($\\rho=0.42$): DIF items produce more stable rankings than generated replacements.\n\\end{enumerate}\n\nThis reframes DIF from a contamination detector (which it is not, on these data) to a \\emph{capability archaeology} tool: it identifies which benchmark items carry the discriminative signal between model generations.\n\n\\subsection{Measurement Efficiency Implications}\n\nThe $\\rho=0.997$ result under 31\\% item removal, combined with $\\rho=0.972$ at 50\\% removal, reveals that MMLU is approximately $3\\times$ larger than necessary for stable rankings. DIF identifies the informative core---the items that actually contribute to ranking discrimination. This has practical implications for evaluation efficiency: a DIF-curated subset could achieve comparable ranking fidelity at one-third the cost.\n\n\\subsection{Limitations}\n\n\\paragraph{Unidimensionality violation.} MH-DIF assumes unidimensional ability, but MMLU spans 57 subjects. Bifactor IRT failed to converge (Section~\\ref{sec:bifactor}), and decoder-only stratification did not improve fit (Section~\\ref{sec:arch_strat}). Our DIF analysis should be interpreted as a pragmatic approximation. Multidimensional DIF methods (MIMIC, MIRT-DIF) are needed for rigorous treatment.\n\n\\paragraph{Semi-synthetic ecological validity.} The incorrect$\\to$correct flipping mechanism does not model realistic contamination pathways. The $\\Delta$TPR framework provides sensitivity calibration, not contamination detection validation.\n\n\\paragraph{Sample sizes.} GSM1K validation uses $N=33$ models (wide CI). RL robustness analysis has only $N=13$ reasoning-RL models (underpowered). Both require larger samples for definitive conclusions.\n\n\\paragraph{No contamination ground truth.} We cannot decompose the 31.3\\% DIF rate into contamination vs.\\ capability components. The capability interpretation is supported by converging evidence, but contamination may contribute to some fraction of flagged items.\n\n\\paragraph{Ensemble weakness.} The fusion of DIF, ConStat, and DVD produces marginal improvement (AUC 0.64) with non-generalizing weights. Three individually weak signals do not combine into a strong one without shared ground truth.\n\n\\paragraph{Cumulative FPR inflation.} Bayesian evidence accumulation improves power but inflates FPR from 0.05 to 0.11 over four administrations, limiting practical applicability without correction mechanisms.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Benchmark contamination detection.} Several methods detect contamination in LLMs: Min-K\\% probability-based detection, $n$-gram overlap analysis, and ConStat perturbation-based testing. These operate at the per-model level and validate against web-overlap labels. Our work differs in applying group-level psychometric analysis and demonstrating that web-overlap labels are inappropriate for item-level differential detection.\n\n\\paragraph{DIF in educational testing.} DIF analysis has a long history in psychometrics, with the MH procedure introduced by Holland and Thayer (1988). Applications to computerized adaptive testing and item banking are standard practice. Sinharay et al.\\ (2006) introduced Bayesian approaches to cumulative DIF. Our work is the first large-scale application to LLM benchmarks.\n\n\\paragraph{Benchmark evaluation methodology.} Growing Pains (Polo et al., 2024) uses anchor items for efficient evaluation via IRT equating. Our DIF diagnostic complements this by identifying which anchor items are degrading across model generations. The METABENCH repository provides the large-scale response matrices enabling our analysis.\n\n\\paragraph{LLM-based item generation.} Recent work explores using LLMs to generate test items with calibrated difficulty. Published correlations ($\\rho=0.75$--$0.82$) were achieved on constrained math items; our attempt on MMLU's diverse domains achieved substantially lower calibration ($\\rho=0.34$).\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe present the largest DIF analysis on LLM benchmarks to date, analyzing 5,219 models across 12,508 MMLU items. Our core finding is that DIF identifies \\emph{capability-authentic} benchmark items---the items where genuine model improvement manifests at the item level. The 31.3\\% of MMLU items flagged by DIF are not defective; they are the discriminative core that differentiates model generations. Cross-benchmark validation confirms this interpretation: DIF flags anti-correlate with contamination ($r=-0.478$, $p=0.005$).\n\nWe contribute a semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR$=0.000$) and extensive negative results from twelve experiments that map the operational boundaries of psychometric methods in LLM evaluation. The graceful degradation analysis reveals MMLU's massive redundancy ($\\rho=0.972$ at 50\\% removal), suggesting that DIF-guided benchmark curation could improve evaluation efficiency by a factor of three.\n\nFuture work should address the unidimensionality limitation via multidimensional IRT, expand RL robustness analysis as more reasoning-RL models become available, and develop contamination ground truth that enables decomposing capability and contamination contributions to DIF.\n\n%==============================================================================\n% References\n%==============================================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{99}\n\n\\bibitem[Holland and Thayer(1988)]{holland1988}\nHolland, P.~W. and Thayer, D.~T. (1988).\n\\newblock Differential item functioning and the Mantel-Haenszel procedure.\n\\newblock In \\emph{Test Validity}, pages 129--145.\n\n\\bibitem[Li et al.(2024)]{li2024}\nLi, Y., et al. (2024).\n\\newblock Open {LLM} Leaderboard contamination detection.\n\\newblock Technical report.\n\n\\bibitem[Polo et al.(2024)]{polo2024}\nPolo, F.~M., et al. (2024).\n\\newblock {Growing Pains}: Understanding the impact of model updates on benchmark evaluation via {IRT}.\n\\newblock In \\emph{NeurIPS 2024 Datasets and Benchmarks Track}.\n\n\\bibitem[Sinharay et al.(2006)]{sinharay2006}\nSinharay, S., Johnson, M.~S., and Stern, H.~S. (2006).\n\\newblock Posterior predictive assessment of item response theory models.\n\\newblock \\emph{Applied Psychological Measurement}, 30(4):298--321.\n\n\\bibitem[Oren et al.(2024)]{oren2024}\nOren, Y., et al. (2024).\n\\newblock Proving test set contamination in black-box language models.\n\\newblock In \\emph{ICLR 2024}.\n\n\\bibitem[Deconinck et al.(2024)]{deconinck2024}\nDeconinck, K., et al. (2024).\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock In \\emph{EMNLP 2024}.\n\n\\bibitem[Tutz and Berger(2016)]{tutz2016}\nTutz, G. and Berger, M. (2016).\n\\newblock Item-focused trees for the identification of items in differential item functioning.\n\\newblock \\emph{Psychometrika}, 81(3):727--750.\n\n\\bibitem[Hendrycks et al.(2021)]{hendrycks2021}\nHendrycks, D., et al. (2021).\n\\newblock Measuring massive multitask language understanding.\n\\newblock In \\emph{ICLR 2021}.\n\n\\bibitem[Cobbe et al.(2021)]{cobbe2021}\nCobbe, K., et al. (2021).\n\\newblock Training verifiers to solve math word problems.\n\\newblock \\emph{arXiv preprint arXiv:2110.14168}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "c5d67a03-937d-4bf3-beb7-3f055ec74b61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "df63c027-df95-4ee6-857e-8846f9c89963",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulation paper from experiment data",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da"
}
```

---

### Tool call

_source line 25 · 2026-05-21T01:58:10.973Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01L6HnbAhEtwCeeQC3aUSsia`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df63c027-df95-4ee6-857e-8846f9c89963",
  "isSidechain": false,
  "requestId": "req_011CbEtJkPebbgeNFocRqaKQ",
  "type": "assistant",
  "uuid": "83ce751f-8fdc-4cfa-ba10-7f9bf0c20625",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SHsYLGJkRwg4fzGmaEHqDS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12126,
      "cache_read_input_tokens": 41895,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 41895,
          "cache_creation_input_tokens": 12126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12126
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

_source line 26 · 2026-05-21T01:58:12.158Z_

<details><summary>↩ Tool result · `toolu_01L6HnbAhEtwCeeQC3aUSsia`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Reference `tab:dif_summary' on page 2 undefined on input line 88
.

[2] [3]

LaTeX Warning: Reference `sec:semisynthetic' on page 4 undefined on input line 
187.


Overfull \hbox (5.80821pt too wide) in paragraph at lines 187--188
 []\OT1/cmr/bx/n/10 Semi-synthetic val-i-da-tion on GSM8K.[] \OT1/cmr/m/n/10 Th
e semi-synthetic frame-work (Sec-tion []) repli-cates on GSM8K

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[4]

LaTeX Warning: `h' float specifier changed to `ht'.

[5]
Overfull \hbox (7.70744pt too wide) in paragraph at lines 313--314
 []\OT1/cmr/bx/n/10 Experiment 7: Ev-i-dence Ac-cu-mu-la-tion Across Ad-min-is-
tra-tions.[] \OT1/cmr/m/n/10 We im-ple-ment cu-mu-la-tive Bayesian

LaTeX Warning: `h' float specifier changed to `ht'.

[6]

LaTeX Warning: `h' float specifier changed to `ht'.

[7] [8]

LaTeX Warning: Reference `sec:degradation' on page 9 undefined on input line 49
5.


LaTeX Warning: Reference `sec:bifactor' on page 9 undefined on input line 522.


LaTeX Warning: Reference `sec:arch_strat' on page 9 undefined on input line 522
.

[9]
Overfull \hbox (22.75848pt too wide) in paragraph at lines 539--540
 []\OT1/cmr/bx/n/10 Benchmark con-tam-i-na-tion de-tec-tion.[] \OT1/cmr/m/n/10 
Sev-eral meth-ods de-tect con-tam-i-na-tion in LLMs: Min-K% probability-
[10] [11] (./paper.aux

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
lic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr1
2.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmti9.pfb>
Output written on paper.pdf (11 pages, 245861 bytes).
Transcript written on paper.log.
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2] [3]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[4]

LaTeX Warning: `h' float specifier changed to `ht'.

[5]
Overfull \hbox (7.70744pt too wide) in paragraph at lines 313--314
 []\OT1/cmr/bx/n/10 Experiment 7: Ev-i-dence Ac-cu-mu-la-tion Across Ad-min-is-
tra-tions.[] \OT1/cmr/m/n/10 We im-ple-ment cu-mu-la-tive Bayesian

LaTeX Warning: `h' float specifier changed to `ht'.

[6]

LaTeX Warning: `h' float specifier changed to `ht'.

[7] [8] [9]
Overfull \hbox (22.75848pt too wide) in paragraph at lines 539--540
 []\OT1/cmr/bx/n/10 Benchmark con-tam-i-na-tion de-tec-tion.[] \OT1/cmr/m/n/10 
Sev-eral meth-ods de-tect con-tam-i-na-tion in LLMs: Min-K% probability-
[10] [11] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr1
2.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmti9.pfb>
Output written on paper.pdf (11 pages, 248028 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83ce751f-8fdc-4cfa-ba10-7f9bf0c20625",
  "isSidechain": false,
  "promptId": "41166657-dacb-41c2-9c9f-045334e8b1ff",
  "type": "user",
  "uuid": "62ae1d79-409c-40bc-aa0f-a61c07aab72b",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Reference `tab:dif_summary' on page 2 undefined on input line 88\n.\n\n[2] [3]\n\nLaTeX Warning: Reference `sec:semisynthetic' on page 4 undefined on input line \n187.\n\n\nOverfull \\hbox (5.80821pt too wide) in paragraph at lines 187--188\n []\\OT1/cmr/bx/n/10 Semi-synthetic val-i-da-tion on GSM8K.[] \\OT1/cmr/m/n/10 Th\ne semi-synthetic frame-work (Sec-tion []) repli-cates on GSM8K\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5]\nOverfull \\hbox (7.70744pt too wide) in paragraph at lines 313--314\n []\\OT1/cmr/bx/n/10 Experiment 7: Ev-i-dence Ac-cu-mu-la-tion Across Ad-min-is-\ntra-tions.[] \\OT1/cmr/m/n/10 We im-ple-ment cu-mu-la-tive Bayesian\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7] [8]\n\nLaTeX Warning: Reference `sec:degradation' on page 9 undefined on input line 49\n5.\n\n\nLaTeX Warning: Reference `sec:bifactor' on page 9 undefined on input line 522.\n\n\nLaTeX Warning: Reference `sec:arch_strat' on page 9 undefined on input line 522\n.\n\n[9]\nOverfull \\hbox (22.75848pt too wide) in paragraph at lines 539--540\n []\\OT1/cmr/bx/n/10 Benchmark con-tam-i-na-tion de-tec-tion.[] \\OT1/cmr/m/n/10 \nSev-eral meth-ods de-tect con-tam-i-na-tion in LLMs: Min-K% probability-\n[10] [11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr1\n2.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmti9.pfb>\nOutput written on paper.pdf (11 pages, 245861 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2] [3]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5]\nOverfull \\hbox (7.70744pt too wide) in paragraph at lines 313--314\n []\\OT1/cmr/bx/n/10 Experiment 7: Ev-i-dence Ac-cu-mu-la-tion Across Ad-min-is-\ntra-tions.[] \\OT1/cmr/m/n/10 We im-ple-ment cu-mu-la-tive Bayesian\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7] [8] [9]\nOverfull \\hbox (22.75848pt too wide) in paragraph at lines 539--540\n []\\OT1/cmr/bx/n/10 Benchmark con-tam-i-na-tion de-tec-tion.[] \\OT1/cmr/m/n/10 \nSev-eral meth-ods de-tect con-tam-i-na-tion in LLMs: Min-K% probability-\n[10] [11] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr1\n2.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmti9.pfb>\nOutput written on paper.pdf (11 pages, 248028 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "83ce751f-8fdc-4cfa-ba10-7f9bf0c20625",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-21T01:58:21.706Z_

编译成功，11 页 PDF，无错误。所有 12 个实验均有对应 section/table，全部定量数据来自 `experiment_data.json`。论文按 worst tier narrative guidance 完成了重新定位：DIF 作为 capability archaeology 工具而非 contamination detector，$r=-0.478$ 作为 headline positive finding，$\rho=0.997$ 解读为 benchmark 冗余，负面结果诚实报告。

输出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62ae1d79-409c-40bc-aa0f-a61c07aab72b",
  "isSidechain": false,
  "requestId": "req_011CbEtK9Cr38vESMbD5qKpJ",
  "type": "assistant",
  "uuid": "116bc556-0d01-4f92-9e5d-7b6f19e142fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jSvWeGEkaV3k7EvoNjqPT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6217,
      "cache_read_input_tokens": 54021,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6217,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 54021,
          "cache_creation_input_tokens": 6217,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6217
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

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "116bc556-0d01-4f92-9e5d-7b6f19e142fa",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulation paper from experiment data",
  "sessionId": "4252ca06-67da-4be4-a2cb-c5a7e1cf56da"
}
```

---
