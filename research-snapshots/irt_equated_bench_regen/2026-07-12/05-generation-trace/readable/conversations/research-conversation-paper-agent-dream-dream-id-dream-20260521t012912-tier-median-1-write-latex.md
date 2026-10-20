# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/e38c2aaa-70a4-4ee4-9416-4e605591b62e.jsonl`
- **Structured JSON:** [`87c635ebe39b9085b702.json`](../../sessions/87/87c635ebe39b9085b702.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T01:48:52.783Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T01:48:52.783Z",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Soften Claim 2 from 'fundamental blind spot' to 'underappreciated methodological gap.' Add explicit caveat on 38%: instability reflects mixture of capability improvement and DIF. Reframe ρ=0.997 as measurement efficiency problem. GSM1K downgraded to 'suggestive evidence.' Position for ICLR findings track with rebuttal emphasizing semi-synthetic framework (Claim 3) as most portable contribution.\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T01:48:52.787Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T01:48:52.787Z",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-21T01:48:52.807Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Soften Claim 2 from 'fundamental blind spot' to 'underappreciated methodological gap.' Add explicit caveat on 38%: instability reflects mixture of capability improvement and DIF. Reframe ρ=0.997 as measurement efficiency problem. GSM1K downgraded to 'suggestive evidence.' Position for ICLR findings track with rebuttal emphasizing semi-synthetic framework (Claim 3) as most portable contribution.
- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "de177bb0-8153-4b40-a54f-7680d3583965",
  "type": "user",
  "uuid": "356c4d79-653c-406a-8161-d0dd774a288b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T01:48:52.806Z_

```json
{
  "parentUuid": "356c4d79-653c-406a-8161-d0dd774a288b",
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
  "uuid": "abe3a0d9-cb46-456a-9874-9b78e7b35828",
  "timestamp": "2026-05-21T01:48:52.806Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T01:48:52.806Z_

```json
{
  "parentUuid": "abe3a0d9-cb46-456a-9874-9b78e7b35828",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "652f8b34-514d-47a4-a660-3ddd2c0ad1ed",
  "timestamp": "2026-05-21T01:48:52.806Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
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
  "aiTitle": "Generate simulated research paper with IRT equated benchmark",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e"
}
```

---

### Assistant

_source line 7 · 2026-05-21T01:48:55.624Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "652f8b34-514d-47a4-a660-3ddd2c0ad1ed",
  "isSidechain": false,
  "requestId": "req_011CbEsbv1hnJPznBNxc9L89",
  "type": "assistant",
  "uuid": "74f4b4c1-3b43-4eac-abf4-685094312e02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015BstrE2qQ9Mvv7P9PTRkF3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11297,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11297
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

_source line 8 · 2026-05-21T01:48:56.793Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EWx2Xj4cYqGTqB5rtfe8oJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74f4b4c1-3b43-4eac-abf4-685094312e02",
  "isSidechain": false,
  "requestId": "req_011CbEsbv1hnJPznBNxc9L89",
  "type": "assistant",
  "uuid": "15a3eaea-4da3-40b7-96d3-9bf21b907feb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015BstrE2qQ9Mvv7P9PTRkF3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11297,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11297
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

_source line 9 · 2026-05-21T01:48:57.149Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GWnVeXUp8HyT3vk4YF5GS2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15a3eaea-4da3-40b7-96d3-9bf21b907feb",
  "isSidechain": false,
  "requestId": "req_011CbEsbv1hnJPznBNxc9L89",
  "type": "assistant",
  "uuid": "89362050-31d3-4d7c-bbc3-b425eb036ac5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015BstrE2qQ9Mvv7P9PTRkF3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11297,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11297
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

_source line 10 · 2026-05-21T01:48:57.158Z_

<details><summary>↩ Tool result · `toolu_01GWnVeXUp8HyT3vk4YF5GS2`</summary>

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
  "parentUuid": "89362050-31d3-4d7c-bbc3-b425eb036ac5",
  "isSidechain": false,
  "promptId": "de177bb0-8153-4b40-a54f-7680d3583965",
  "type": "user",
  "uuid": "71058115-c0fe-41c0-afa5-a49d1708d02e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: 38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. This instability persists within every subject domain (within-subject C%=31-45%, avg 38.1%), is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). This means cross-temporal MMLU score comparisons carry uncontrolled item-level variance.\n- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%)\n- Honesty requirement: ρ=0.307 means \"item instability\" may mainly reflect \"models got better at those domains\" — we cannot decompose 38% into contamination vs capability improvement\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\"\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items = discriminative signal carriers**: DIF removal causes significantly MORE ranking disruption than random removal (z=-8 to -49σ, 21/21 conditions). DIF items carry 1.09× cross-cohort accuracy swing vs 0.96× for stable items — they concentrate the information that differentiates model generations.\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\n4. **Cross-benchmark validation — DIF captures capability, not contamination**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005; partial r=−0.385 controlling accuracy; permutation p=0.014). Contaminated models (high GSM8K-GSM1K gap: Phi, Gemma families) perform WORSE on DIF items. DIF captures genuine capability-discriminative items that contamination cannot fake — contamination produces shallow performance gains concentrated on non-DIF items. N=33 matched models, leave-one-out robust (min |r|=0.374).\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_004 Step 3 (r=−0.478, p=0.005, 33 models)\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\" — mutual value positioning\n- Caveats (→ limitations): super-family analysis limited to N≥20 families; GSM1K validation N=33 (CI wide); contamination gap is proxy, not ground truth\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.\n\n**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\n\n**What we find**: Three discoveries, each a contribution:\n\n1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.\n\n2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.\n\n3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.\n\n4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K confirms: DIF flags anti-correlate with contamination (r=−0.478, p=0.005) — contaminated models can't fake performance on DIF items, which capture genuine capability differences. DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.\n\n**Headline result**: \"Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF flags anti-correlate with contamination (r=−0.478, p=0.005): DIF captures genuine capability-discriminative items that contamination cannot replicate. We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000).\"\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\n- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 38% instability, (2) the ground truth meta-critique affecting the field, (3) the semi-synthetic framework. Frame as \"bringing mature psychometric tools to characterize an urgent ML evaluation problem.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"38% could just mean models got better\"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 80
    }
  },
  "sourceToolAssistantUUID": "89362050-31d3-4d7c-bbc3-b425eb036ac5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T01:48:57.222Z_

<details><summary>↩ Tool result · `toolu_01EWx2Xj4cYqGTqB5rtfe8oJ`</summary>

```text
1	[
2	  {
3	    "name": "rl_robustness_validation",
4	    "description": "Validate DIF robustness to reasoning-RL models by adding 13 GRPO/PPO models to focal cohort and comparing DIF flag stability + traditional detector degradation.",
5	    "results": {
6	      "n_reasoning_rl_models": 13,
7	      "n_alignment_rl_models": 477,
8	      "dif_flag_retention_ratio_sft_vs_alignment_rl": 0.91,
9	      "dif_flag_retention_ratio_sft_vs_reasoning_rl_added": 0.86,
10	      "dif_jaccard_sft_vs_rl_augmented": 0.83,
11	      "constat_auroc_sft_only": 0.72,
12	      "constat_auroc_reasoning_rl": 0.54,
13	      "mink_auroc_sft_only": 0.68,
14	      "mink_auroc_reasoning_rl": 0.49,
15	      "delong_dif_vs_constat_p": 0.087,
16	      "delong_dif_vs_mink_p": 0.042,
17	      "tost_equivalence_dif_retention_p": 0.11,
18	      "bootstrap_ci_dif_retention": [
19	        0.79,
20	        0.93
21	      ],
22	      "power_curve_detection_boundary_p": 0.55
23	    },
24	    "tables": [
25	      {
26	        "title": "Table: DIF vs Traditional Detector Comparison Under RL",
27	        "columns": [
28	          "Detector",
29	          "AUROC (SFT)",
30	          "AUROC (Alignment-RL)",
31	          "AUROC (Reasoning-RL)",
32	          "Δ",
33	          "95% CI"
34	        ],
35	        "rows": [
36	          [
37	            "DIF (MH)",
38	            "N/A (group)",
39	            "N/A (group)",
40	            "retention=0.86",
41	            "-0.14",
42	            "[−0.21, −0.07]"
43	          ],
44	          [
45	            "ConStat",
46	            "0.72",
47	            "0.69",
48	            "0.54",
49	            "-0.18",
50	            "[−0.31, −0.05]"
51	          ],
52	          [
53	            "Min-K%",
54	            "0.68",
55	            "0.64",
56	            "0.49",
57	            "-0.19",
58	            "[−0.33, −0.06]"
59	          ]
60	        ]
61	      }
62	    ],
63	    "figures": [],
64	    "analysis": "Result is directionally supportive but statistically underpowered. DIF shows robustness (86% flag retention) while traditional detectors degrade, consistent with theoretical prediction. However, TOST equivalence failure and marginal DeLong test mean this cannot be claimed as definitive proof. In median tier, reviewers acknowledge the logic but request either (a) more reasoning-RL models when available, or (b) formal power analysis showing what N would be needed for conclusive evidence. The detection boundary at p=0.55 is an honest limitation — partial exploitation remains a blind spot. Best positioned as 'preliminary evidence consistent with theoretical robustness prediction' in limitations/future work, not as a standalone claim.\n\nWith only N=13 reasoning-RL models, group-level DIF remains stable (retention 0.86) because DIF operates on full cohort N≥80 and RL models are a minority. Traditional detectors degrade individually (ConStat AUROC 0.72→0.54, Min-K% 0.68→0.49) as expected from NLL gap contraction. However, DeLong test for DIF vs ConStat is marginal (p=0.087) — underpowered at N=13. TOST equivalence fails (p=0.11 > 0.05), so reviewers can't rule out that DIF retention is coincidental. Median-tier outcome: suggestive robustness evidence insufficient for strong claim. Reviewers note 'N=13 is too few for definitive comparison; interesting pilot but not convincing.' Detection boundary at p=0.55 means DIF misses partial exploitation below 55%, which is a meaningful gap."
65	  },
66	  {
67	    "name": "constat_perturbation_eval",
68	    "description": "Independent ConStat-style perturbation testing on 250 MMLU items with LLM-generated semantic reformulations across 15 models.",
69	    "results": {
70	      "n_items_reformulated": 248,
71	      "n_models_tested": 15,
72	      "mean_performance_drop_original_vs_reformulated": 0.034,
73	      "constat_detection_rate_fdr_010": 0.127,
74	      "constat_detection_rate_fdr_005": 0.089,
75	      "constat_auroc_vs_li_labels": 0.61,
76	      "constat_auroc_non_rl_models": 0.67,
77	      "constat_auroc_rl_models": 0.52,
78	      "mean_reformulation_quality_score": 0.82,
79	      "semantic_equivalence_human_check": 0.91,
80	      "effect_size_detected_items_cohens_d": 0.73
81	    },
82	    "tables": [
83	      {
84	        "title": "Table: ConStat Detection Rates by Model Category",
85	        "columns": [
86	          "Model Category",
87	          "N Models",
88	          "Detection Rate (FDR=0.10)",
89	          "Mean Effect Size (d)"
90	        ],
91	        "rows": [
92	          [
93	            "SFT-only",
94	            "6",
95	            "0.153",
96	            "0.81"
97	          ],
98	          [
99	            "Alignment-RL (DPO)",
100	            "5",
101	            "0.134",
102	            "0.69"
103	          ],
104	          [
105	            "Reasoning-RL (GRPO)",
106	            "4",
107	            "0.071",
108	            "0.42"
109	          ]
110	        ]
111	      }
112	    ],
113	    "figures": [],
114	    "analysis": "ConStat independently validates the complementary detection space claim — it works where DIF doesn't (per-model, small effects) but fails where DIF succeeds (RL-robust, group-differential). However, in median tier this experiment is not included in the main paper because plan_003c (ensemble) was never fully executed and the ensemble narrative (original Claim 2) was dropped during the pivot. ConStat results go to appendix as supplementary comparison, supporting the 'detection methods are complementary' theme without being a core contribution.\n\nConStat operates at per-model level detecting performance drops on reformulations. On non-RL models (where memorization manifests as sensitivity to surface form), detection rate is moderate (12.7% at FDR=0.10). RL models show minimal surface-form sensitivity (AUROC 0.52, near chance) because PPO/GRPO training generalizes beyond verbatim patterns. The 3.4% mean performance drop across all items is small because most items aren't contaminated — only a subset shows the characteristic bimodal response pattern. AUROC vs Li et al. labels is weak (0.61) because, as established, web-overlap is a mismatched ground truth for item-level detection. In median tier, this provides a useful baseline comparison confirming ConStat's complementary detection space (non-RL, surface-form memorization) but doesn't change the paper's core narrative."
115	  },
116	  {
117	    "name": "dvd_generation_variance_eval",
118	    "description": "DVD generation variance detection on 12 open-weight models with 50 generations per item at T=0.8 on 300 MMLU items.",
119	    "results": {
120	      "n_models_tested": 12,
121	      "n_items_per_model": 300,
122	      "n_generations_per_item": 50,
123	      "temperature": 0.8,
124	      "bimodal_detection_rate": 0.094,
125	      "dvd_auroc_vs_dif_flags": 0.58,
126	      "dvd_auroc_verbatim_contamination": 0.71,
127	      "dvd_auroc_variant_contamination": 0.63,
128	      "mean_generation_variance_clean_items": 0.34,
129	      "mean_generation_variance_contaminated_items": 0.18,
130	      "gpu_hours_used": 62,
131	      "inference_failures": 3
132	    },
133	    "tables": [
134	      {
135	        "title": "Table: DVD Detection Characteristics",
136	        "columns": [
137	          "Contamination Type",
138	          "AUROC",
139	          "Detection Rate (threshold=0.10)",
140	          "Mean Variance Reduction"
141	        ],
142	        "rows": [
143	          [
144	            "Verbatim",
145	            "0.71",
146	            "0.134",
147	            "0.21"
148	          ],
149	          [
150	            "Variant/Paraphrase",
151	            "0.63",
152	            "0.072",
153	            "0.12"
154	          ],
155	          [
156	            "None (clean)",
157	            "—",
158	            "0.031 (FPR)",
159	            "—"
160	          ]
161	        ]
162	      }
163	    ],
164	    "figures": [],
165	    "analysis": "DVD results are informative but not compelling enough for inclusion in the pivoted paper. The weak correspondence with DIF flags (AUROC 0.58) actually supports the paper's narrative that different detection methods capture different contamination mechanisms. However, the high GPU cost and low detection rates make this a poor cost-benefit trade for the characterization paper. In median tier, this remains in supplementary material at best. The result is useful for future ensemble work but doesn't strengthen any of the four core claims.\n\nDVD detects contamination via low generation variance (memorized items → consistently correct). Detection rate of 9.4% reflects that most contamination on MMLU is not verbatim memorization but pattern-level familiarity, which still produces moderate variance. AUROC for verbatim contamination (0.71) is better than variant (0.63) because verbatim produces clearer bimodal distributions. Correlation with DIF flags is weak (AUROC 0.58) because DIF and DVD measure fundamentally different signals: DIF measures cross-group differential, DVD measures within-model consistency. In median tier, DVD provides another complementary signal but is expensive (62 GPU-hours for 12 models × 300 items) and the low detection rate limits practical utility. The 3 inference failures (OOM on larger models) highlight scalability concerns."
166	  },
167	  {
168	    "name": "ensemble_fusion",
169	    "description": "Attempt to fuse DIF + ConStat + DVD into multi-signal ensemble with majority voting and weighted fusion.",
170	    "results": {
171	      "ensemble_2of3_precision": 0.41,
172	      "ensemble_2of3_recall": 0.23,
173	      "ensemble_weighted_auroc": 0.66,
174	      "ensemble_fpr": 0.087,
175	      "individual_dif_auroc": 0.62,
176	      "individual_constat_auroc": 0.61,
177	      "individual_dvd_auroc": 0.58,
178	      "cross_val_weight_variance": 0.15,
179	      "uniform_vs_optimized_auroc_gap": 0.03,
180	      "coverage_overlap_dif_constat": 0.31,
181	      "coverage_overlap_dif_dvd": 0.22,
182	      "coverage_overlap_constat_dvd": 0.38
183	    },
184	    "tables": [
185	      {
186	        "title": "Table: Ensemble vs Individual Detector Performance",
187	        "columns": [
188	          "Method",
189	          "AUROC",
190	          "Precision@FPR=0.10",
191	          "Coverage (items flagged)"
192	        ],
193	        "rows": [
194	          [
195	            "DIF (MH)",
196	            "0.62",
197	            "0.38",
198	            "31.3%"
199	          ],
200	          [
201	            "ConStat",
202	            "0.61",
203	            "0.34",
204	            "12.7%"
205	          ],
206	          [
207	            "DVD",
208	            "0.58",
209	            "0.29",
210	            "9.4%"
211	          ],
212	          [
213	            "Ensemble (2-of-3)",
214	            "0.66",
215	            "0.41",
216	            "6.8%"
217	          ],
218	          [
219	            "Ensemble (weighted)",
220	            "0.66",
221	            "0.43",
222	            "8.2%"
223	          ]
224	        ]
225	      }
226	    ],
227	    "figures": [],
228	    "analysis": "Ensemble fusion fails to produce a compelling unified detector because the three methods target different contamination mechanisms with minimal overlap. This is actually the correct scientific conclusion — it supports the pivot away from 'unified contamination detector' toward 'characterization of differential item functioning.' In median tier, plan_003c is reported as a negative result in the appendix: 'ensemble approaches require contamination mechanisms to be partially redundant; when mechanisms are orthogonal, fusion provides minimal lift.' This negative result paradoxically supports the paper's reframing: DIF measures something fundamentally different from per-model detectors.\n\nEnsemble shows modest improvement over individuals (AUROC 0.66 vs best individual 0.62) but the improvement is not dramatic because the three signals have limited overlap — they detect different contamination mechanisms with low redundancy. 2-of-3 majority voting has good precision (0.41) but very low recall (0.23) because few items trigger multiple detectors simultaneously. FPR<0.10 criterion is met (0.087) but only because the ensemble is very conservative. Cross-validation weight variance is high (0.15) indicating instability — different folds produce different optimal weights, suggesting the calibration set is too small for reliable fusion. In median tier, this experiment is effectively abandoned during the pivot away from 'detection methods' framing. The ensemble was the core of original Claim 2 which is now dropped."
229	  },
230	  {
231	    "name": "bifactor_irt_equating_pilot",
232	    "description": "Fit bifactor IRT model (general + 57 subject-specific factors) to METABENCH MMLU response matrix and attempt test equating via anchor items.",
233	    "results": {
234	      "bifactor_converged": true,
235	      "n_iterations_to_converge": 847,
236	      "general_factor_variance_explained": 0.62,
237	      "mean_subject_factor_variance": 0.14,
238	      "rmsea_bifactor": 0.041,
239	      "cfi_bifactor": 0.87,
240	      "n_anchor_items_selected": 1842,
241	      "anchor_stability_criterion": "DIF A-class across all cohort pairs",
242	      "equated_rho_original_vs_replaced": 0.93,
243	      "equated_rho_anchor_only": 0.97,
244	      "replacement_item_calibration_rmse": 0.38,
245	      "kim_kolen_fixed_param_fit": "acceptable for 68% of replacement items"
246	    },
247	    "tables": [
248	      {
249	        "title": "Table: Bifactor Model Fit Indices",
250	        "columns": [
251	          "Index",
252	          "Value",
253	          "Acceptable",
254	          "Good"
255	        ],
256	        "rows": [
257	          [
258	            "RMSEA",
259	            "0.041",
260	            "< 0.08 ✓",
261	            "< 0.05 ✓"
262	          ],
263	          [
264	            "CFI",
265	            "0.87",
266	            "< 0.90 ✗",
267	            "≥ 0.95 ✗"
268	          ],
269	          [
270	            "TLI",
271	            "0.84",
272	            "< 0.90 ✗",
273	            "≥ 0.95 ✗"
274	          ],
275	          [
276	            "SRMR",
277	            "0.063",
278	            "< 0.08 ✓",
279	            "< 0.05 ✗"
280	          ]
281	        ]
282	      }
283	    ],
284	    "figures": [],
285	    "analysis": "Bifactor equating is technically feasible but falls short of production quality. The marginal model fit (CFI=0.87) reflects the known challenge that 57 MMLU subjects create a high-dimensional latent space poorly captured by a single general factor. In median tier, this experiment is reported honestly as 'pilot demonstration with limitations' — it shows the path to benchmark regeneration exists but requires better IRT models (multidimensional, or domain-clustered bifactor). Reviewers would likely say 'interesting future direction but not mature enough for a contribution claim.' This supports the paper's positioning of equating as future work rather than a current claim. Plan_014 already showed within-subject C%=38.1%, so the bifactor pre-check approach for reducing DIF was killed — this equating pilot inherits that limitation.\n\nBifactor model converges but with marginal fit (CFI=0.87 < 0.90 threshold, RMSEA=0.041 acceptable). The 57-subject structure is too fine-grained for the model to fit cleanly — general factor explains 62% of variance, individual subjects contribute 14% on average, leaving ~24% residual. Anchor item selection yields 1,842 stable items (14.7% of total), sufficient for equating but a relatively small anchor set. Equated score correlation (ρ=0.93) falls below the target ρ≥0.95, primarily because replacement item calibration via fixed-parameter approach has high RMSE (0.38) — the item parameters estimated on one cohort don't transfer perfectly. In median tier, this is a 'proof of concept with caveats' — equating is feasible in principle but the bifactor model's marginal fit and the below-target equated correlation weaken the regeneration claim. Reviewers note 'interesting pilot but ρ=0.93 suggests non-trivial information loss during equating.'"
286	  },
287	  {
288	    "name": "item_generation_calibration",
289	    "description": "Generate replacement items for 200 DIF-flagged MMLU questions using LLM generation with construct constraints, calibrate via student simulation.",
290	    "results": {
291	      "n_items_generated": 200,
292	      "n_items_passing_quality_filter": 156,
293	      "difficulty_correlation_prompt_based": 0.31,
294	      "difficulty_correlation_student_sim": 0.64,
295	      "discrimination_correlation": 0.42,
296	      "construct_alignment_human_rating": 0.78,
297	      "holdout_panel_correlation": 0.58,
298	      "mean_difficulty_mae": 0.18,
299	      "pct_items_within_05_difficulty": 0.43,
300	      "gpu_hours_used": 187
301	    },
302	    "tables": [
303	      {
304	        "title": "Table: Calibration Method Comparison",
305	        "columns": [
306	          "Method",
307	          "Difficulty ρ",
308	          "Discrimination ρ",
309	          "% Within ±0.5 Target"
310	        ],
311	        "rows": [
312	          [
313	            "Prompt-based targeting",
314	            "0.31",
315	            "0.28",
316	            "0.24"
317	          ],
318	          [
319	            "Student simulation (5 students)",
320	            "0.64",
321	            "0.42",
322	            "0.43"
323	          ],
324	          [
325	            "Student simulation (20 students)",
326	            "0.68",
327	            "0.45",
328	            "0.47"
329	          ]
330	        ]
331	      }
332	    ],
333	    "figures": [],
334	    "analysis": "Item generation calibration shows promise but not maturity. The gap between student simulation performance here (ρ=0.64) and published results (r=0.75-0.82) likely reflects MMLU's domain breadth — calibrating 'abstract algebra' items requires different student models than 'clinical knowledge.' In median tier, this supports the future work framing: 'automated benchmark regeneration is feasible with improved calibration pipelines' but is not ready as a standalone contribution. Combined with plan_005's marginal equating results, the regeneration storyline (original Claim 3) remains firmly in future work territory. The 187 GPU-hours for 200 items also highlights cost concerns for full-scale deployment.\n\nItem generation produces grammatically correct, construct-aligned questions (78% human-rated alignment) but calibration accuracy is moderate. Student simulation improves difficulty prediction (ρ=0.64) over prompt-based targeting (ρ=0.31), consistent with literature (arXiv 2601.09953 reports r=0.75-0.82 — our lower value reflects MMLU's broader domain coverage vs focused benchmarks). Only 43% of generated items fall within ±0.5 difficulty of the target, meaning majority would need iterative recalibration. Discrimination correlation is lower (0.42) because item discrimination depends on subtle psychometric properties harder to control via generation. In median tier, this demonstrates that LLM item generation is a viable but immature pipeline — insufficient for automated benchmark regeneration without human-in-the-loop validation. Reviewers would flag the 58% holdout correlation as 'items don't transfer well to unseen models.'"
335	  },
336	  {
337	    "name": "cumulative_bayesian_dif",
338	    "description": "Simulate cumulative Bayesian DIF with informative priors from prior administrations over 4 successive benchmark waves.",
339	    "results": {
340	      "single_administration_power_delta10": 0.41,
341	      "cumulative_2_administrations_power": 0.54,
342	      "cumulative_3_administrations_power": 0.67,
343	      "cumulative_4_administrations_power": 0.74,
344	      "single_administration_fpr": 0.042,
345	      "cumulative_4_fpr": 0.051,
346	      "power_gain_per_administration": [
347	        0.13,
348	        0.13,
349	        0.07
350	      ],
351	      "convergence_plateau": "~4 administrations",
352	      "bayes_factor_threshold": 3.0,
353	      "pct_items_bf_gt_3_after_4_admin": 0.68
354	    },
355	    "tables": [
356	      {
357	        "title": "Table: Cumulative Power by Effect Size",
358	        "columns": [
359	          "Administrations",
360	          "δ=0.8",
361	          "δ=1.0",
362	          "δ=1.2",
363	          "δ=1.4"
364	        ],
365	        "rows": [
366	          [
367	            "1",
368	            "0.24",
369	            "0.41",
370	            "0.55",
371	            "0.68"
372	          ],
373	          [
374	            "2",
375	            "0.37",
376	            "0.54",
377	            "0.69",
378	            "0.81"
379	          ],
380	          [
381	            "3",
382	            "0.48",
383	            "0.67",
384	            "0.79",
385	            "0.89"
386	          ],
387	          [
388	            "4",
389	            "0.54",
390	            "0.74",
391	            "0.84",
392	            "0.92"
393	          ]
394	        ]
395	      }
396	    ],
397	    "figures": [],
398	    "analysis": "Bayesian cumulative DIF is theoretically elegant and directly addresses the power limitation identified in plan_001 (single-shot DIF only detects large effects δ≥1.4). However, it's purely simulation-based in the current paper because METABENCH provides only a single temporal snapshot (2023 vs 2024-H1), not 4 successive administrations. In median tier, reviewers appreciate the methodological contribution but note 'this requires longitudinal benchmark infrastructure that doesn't yet exist.' Best positioned as a concrete recommendation for benchmark maintainers: 'if you collect response matrices over time, here's how to accumulate evidence of item degradation.' Strengthens the 'measurement science for ML benchmarks' narrative without requiring new empirical data.\n\nCumulative Bayesian approach shows expected power improvement (0.41→0.74 over 4 administrations for medium effects δ=1.0) as evidence accumulates. This is a well-established psychometric result (Sinharay 2006) applied to the LLM benchmark setting. FPR remains controlled (0.051) because Bayesian shrinkage prevents false alarms from accumulating. Power gains show diminishing returns (0.13, 0.13, 0.07) — the fourth administration adds less because most detectable items are already identified. In median tier, this is simulation-only (no real longitudinal MMLU data exists with 4 temporal waves), so reviewers note 'theoretically sound but purely simulated — would need actual longitudinal benchmark deployment to validate.' Positioned as future monitoring methodology, not a current empirical contribution."
399	  },
400	  {
401	    "name": "graceful_degradation_analysis",
402	    "description": "Formal analysis of benchmark validity under progressive item replacement (5% to 50%) using METABENCH empirical data.",
403	    "results": {
404	      "rho_5pct_replacement": 0.998,
405	      "rho_10pct_replacement": 0.996,
406	      "rho_20pct_replacement": 0.991,
407	      "rho_50pct_replacement": 0.972,
408	      "reliability_alpha_full": 0.943,
409	      "reliability_alpha_50pct_replaced": 0.921,
410	      "construct_coverage_5pct": 0.97,
411	      "construct_coverage_50pct": 0.84,
412	      "theoretical_bound_rho_vs_replacement_rate": "ρ ≥ 1 - 1.3r (r = replacement fraction)",
413	      "critical_replacement_threshold": "~35% before ρ < 0.98",
414	      "dif_targeted_vs_random_replacement_rho_gap": 0.008
415	    },
416	    "tables": [
417	      {
418	        "title": "Table: Validity Metrics Under Progressive Replacement",
419	        "columns": [
420	          "Replacement %",
421	          "Spearman ρ",
422	          "Cronbach α",
423	          "Construct Coverage",
424	          "Max Rank Δ"
425	        ],
426	        "rows": [
427	          [
428	            "0% (baseline)",
429	            "1.000",
430	            "0.943",
431	            "1.00",
432	            "0"
433	          ],
434	          [
435	            "5%",
436	            "0.998",
437	            "0.941",
438	            "0.97",
439	            "23"
440	          ],
441	          [
442	            "10%",
443	            "0.996",
444	            "0.938",
445	            "0.95",
446	            "47"
447	          ],
448	          [
449	            "20%",
450	            "0.991",
451	            "0.932",
452	            "0.91",
453	            "112"
454	          ],
455	          [
456	            "50%",
457	            "0.972",
458	            "0.921",
459	            "0.84",
460	            "341"
461	          ]
462	        ]
463	      }
464	    ],
465	    "figures": [],
466	    "analysis": "Graceful degradation analysis primarily serves as supplementary validation for plan_017's core finding. It formalizes what the ρ=0.997 result already implies: MMLU has enormous measurement redundancy. In median tier, this becomes a double-edged sword — reviewers use it to argue 'if the benchmark is so redundant, the 38% instability finding is merely academic, not practically concerning.' The paper's rebuttal must be: 'redundancy protects rankings but masks that 31% of items carry disproportionate discriminative information (z=-8 to -49σ from plan_017). Efficiency, not validity, is the real concern.' The 35% critical threshold aligns with the observed 38% DIF rate — we're near the edge where replacement starts to matter, even if we haven't crossed it yet.\n\nProgressive replacement analysis reveals extreme ranking robustness — even 50% item replacement maintains ρ=0.972. This is consistent with plan_017's finding that ρ=0.997 after removing 31% DIF items. MMLU's 12,508 items provide massive redundancy; any subset of ~6,000+ items preserves relative model ordering. Reliability (Cronbach's α) degrades more noticeably (0.943→0.921 at 50%) because replacement items have higher calibration error. Construct coverage (proportion of original 57 subjects adequately sampled) drops to 0.84 at 50% because some small subjects (N<50 items) lose coverage entirely. The near-linear relationship ρ ≥ 1 - 1.3r holds empirically up to r=0.4. In median tier, this result cuts both ways: it shows equating is feasible (replacements don't destroy validity) but also undermines urgency (if rankings are so stable, why bother replacing items?). Reviewers invoke the 'so what' critique: ρ=0.997→0.972 is still excellent."
467	  },
468	  {
469	    "name": "item_focused_trees",
470	    "description": "Implement Item-Focused Trees treating model release date as continuous covariate, comparing detection power and flexibility vs categorical temporal DIF.",
471	    "results": {
472	      "n_items_analyzed": 12508,
473	      "ift_c_pct_equivalent": 28.4,
474	      "ift_vs_categorical_jaccard": 0.72,
475	      "ift_unique_flags": 0.08,
476	      "categorical_unique_flags": 0.12,
477	      "ift_split_point_median": "2023-09-15",
478	      "ift_nonlinear_items_pct": 0.14,
479	      "ift_power_gain_vs_categorical": 0.03,
480	      "computation_time_hours": 4.2
481	    },
482	    "tables": [
483	      {
484	        "title": "Table: IFT vs Categorical DIF Comparison",
485	        "columns": [
486	          "Method",
487	          "Items Flagged",
488	          "Unique Flags",
489	          "Overlap (Jaccard)",
490	          "Computation Time"
491	        ],
492	        "rows": [
493	          [
494	            "Categorical MH (2023 vs 2024-H1)",
495	            "31.3%",
496	            "12%",
497	            "—",
498	            "0.3 hours"
499	          ],
500	          [
501	            "Item-Focused Trees (continuous date)",
502	            "28.4%",
503	            "8%",
504	            "0.72",
505	            "4.2 hours"
506	          ]
507	        ]
508	      }
509	    ],
510	    "figures": [],
511	    "analysis": "IFT serves primarily as a robustness check confirming that the categorical temporal split was not misleading. The 72% overlap validates the simpler approach while the 14% nonlinear items are methodologically interesting but don't change conclusions. In median tier, this goes to supplementary material as 'sensitivity analysis: continuous treatment of release date produces concordant results (Jaccard=0.72), with 14% of items showing nonlinear trajectories warranting future investigation.' Reviewers may note that IFT is more principled but the limited power gain doesn't justify the complexity for the main paper. Most useful as a reviewer rebuttal resource: 'our arbitrary temporal split is validated by the continuous approach.'\n\nItem-Focused Trees detect 28.4% of items as exhibiting DIF along the release-date continuum (vs 31.3% for categorical temporal split). Jaccard overlap of 0.72 with categorical DIF shows substantial agreement — most items flagged by IFT are also flagged by categorical MH, confirming the temporal split was reasonable. IFT identifies 8% unique items (gradual drift not captured by binary split) and misses 12% that categorical catches (items with sharp discontinuity better detected by group contrast). 14% of items show nonlinear DIF trajectories (early models and late models both struggle, middle cohort performs differently). Power gain is minimal (+0.03) because the binary temporal split already captures the primary contrast. In median tier, IFT provides methodological sophistication but minimal empirical gain — reviewers appreciate the robustness check ('arbitrary temporal split didn't distort results') but note 'the continuous approach doesn't change your main finding.'"
512	  },
513	  {
514	    "name": "architecture_stratified_dif",
515	    "description": "Run DIF within decoder-only architecture subpopulation to test whether IRT fit improves and spurious DIF reduces when architecture heterogeneity is removed.",
516	    "results": {
517	      "n_decoder_only_models": 3412,
518	      "n_ref_decoder_only_2023": 891,
519	      "n_foc_decoder_only_2024h1": 523,
520	      "decoder_only_c_pct": 28.2,
521	      "full_population_c_pct": 31.3,
522	      "delta_c_pct": -3.1,
523	      "rmsea_full_population": 0.089,
524	      "rmsea_decoder_only": 0.067,
525	      "cfi_full_population": 0.78,
526	      "cfi_decoder_only": 0.83,
527	      "tli_decoder_only": 0.81,
528	      "srmr_decoder_only": 0.058,
529	      "jaccard_decoder_vs_full": 0.81,
530	      "fpr_decoder_only": 0.282,
531	      "tpr_decoder_only_semi_synthetic_p05": 0.79,
532	      "delta_tpr_decoder_only": 0.508
533	    },
534	    "tables": [
535	      {
536	        "title": "Table: IRT Fit Comparison: Full Population vs Decoder-Only",
537	        "columns": [
538	          "Metric",
539	          "Full Population",
540	          "Decoder-Only",
541	          "Improvement",
542	          "Acceptable Threshold"
543	        ],
544	        "rows": [
545	          [
546	            "RMSEA",
547	            "0.089",
548	            "0.067",
549	            "−0.022",
550	            "< 0.05"
551	          ],
552	          [
553	            "CFI",
554	            "0.78",
555	            "0.83",
556	            "+0.05",
557	            "≥ 0.90"
558	          ],
559	          [
560	            "TLI",
561	            "0.75",
562	            "0.81",
563	            "+0.06",
564	            "≥ 0.90"
565	          ],
566	          [
567	            "SRMR",
568	            "0.074",
569	            "0.058",
570	            "−0.016",
571	            "< 0.05"
572	          ],
573	          [
574	            "C% (ETS)",
575	            "31.3%",
576	            "28.2%",
577	            "−3.1pp",
578	            "—"
579	          ]
580	        ]
581	      }
582	    ],
583	    "figures": [],
584	    "analysis": "Plan_010 is the proactive defense experiment against the 'IRT model misfit' reviewer concern. In median tier, the result is honest but not fully reassuring: architecture stratification helps (3.1pp C% reduction, RMSEA improvement) but doesn't solve the fundamental issue that unidimensional IRT is a simplification for 57-subject MMLU. The paper frames this as: 'architecture stratification provides modest improvement, confirming that population homogeneity is beneficial but not sufficient — multidimensional IRT or domain-specific modeling remain future directions.' Reviewers likely say 'you've shown the problem is partially addressable but haven't solved it — reframe 38% as upper bound, 28% as lower bound under controlled conditions.' This is consistent with median-tier narrative guidance: 'instability reflects a mixture' with explicit bounds.\n\nArchitecture stratification reduces C% from 31.3% to 28.2% — a modest 3.1pp improvement, not the dramatic reduction that would indicate architecture heterogeneity was the primary driver of spurious DIF. IRT fit improves marginally (RMSEA 0.089→0.067, from 'poor' to 'marginal'; CFI 0.78→0.83, still below 0.90 'acceptable'). This confirms that architecture mixing contributes some model misfit but is not the dominant source — the remaining 28.2% DIF reflects genuine temporal item instability within decoder-only models. Jaccard overlap of 0.81 with full-population flags confirms most DIF items are flagged regardless of population composition. In median tier, this is the 'modest improvement' outcome specified: reviewers acknowledge architecture stratification helps but note 'RMSEA=0.067 and CFI=0.83 are still below standard fit thresholds, suggesting deeper structural issues with unidimensional IRT on MMLU.'"
585	  }
586	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15a3eaea-4da3-40b7-96d3-9bf21b907feb",
  "isSidechain": false,
  "promptId": "de177bb0-8153-4b40-a54f-7680d3583965",
  "type": "user",
  "uuid": "922e32b8-9e95-44d4-a9f5-911898e839bc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"Validate DIF robustness to reasoning-RL models by adding 13 GRPO/PPO models to focal cohort and comparing DIF flag stability + traditional detector degradation.\",\n    \"results\": {\n      \"n_reasoning_rl_models\": 13,\n      \"n_alignment_rl_models\": 477,\n      \"dif_flag_retention_ratio_sft_vs_alignment_rl\": 0.91,\n      \"dif_flag_retention_ratio_sft_vs_reasoning_rl_added\": 0.86,\n      \"dif_jaccard_sft_vs_rl_augmented\": 0.83,\n      \"constat_auroc_sft_only\": 0.72,\n      \"constat_auroc_reasoning_rl\": 0.54,\n      \"mink_auroc_sft_only\": 0.68,\n      \"mink_auroc_reasoning_rl\": 0.49,\n      \"delong_dif_vs_constat_p\": 0.087,\n      \"delong_dif_vs_mink_p\": 0.042,\n      \"tost_equivalence_dif_retention_p\": 0.11,\n      \"bootstrap_ci_dif_retention\": [\n        0.79,\n        0.93\n      ],\n      \"power_curve_detection_boundary_p\": 0.55\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: DIF vs Traditional Detector Comparison Under RL\",\n        \"columns\": [\n          \"Detector\",\n          \"AUROC (SFT)\",\n          \"AUROC (Alignment-RL)\",\n          \"AUROC (Reasoning-RL)\",\n          \"Δ\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"DIF (MH)\",\n            \"N/A (group)\",\n            \"N/A (group)\",\n            \"retention=0.86\",\n            \"-0.14\",\n            \"[−0.21, −0.07]\"\n          ],\n          [\n            \"ConStat\",\n            \"0.72\",\n            \"0.69\",\n            \"0.54\",\n            \"-0.18\",\n            \"[−0.31, −0.05]\"\n          ],\n          [\n            \"Min-K%\",\n            \"0.68\",\n            \"0.64\",\n            \"0.49\",\n            \"-0.19\",\n            \"[−0.33, −0.06]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Result is directionally supportive but statistically underpowered. DIF shows robustness (86% flag retention) while traditional detectors degrade, consistent with theoretical prediction. However, TOST equivalence failure and marginal DeLong test mean this cannot be claimed as definitive proof. In median tier, reviewers acknowledge the logic but request either (a) more reasoning-RL models when available, or (b) formal power analysis showing what N would be needed for conclusive evidence. The detection boundary at p=0.55 is an honest limitation — partial exploitation remains a blind spot. Best positioned as 'preliminary evidence consistent with theoretical robustness prediction' in limitations/future work, not as a standalone claim.\\n\\nWith only N=13 reasoning-RL models, group-level DIF remains stable (retention 0.86) because DIF operates on full cohort N≥80 and RL models are a minority. Traditional detectors degrade individually (ConStat AUROC 0.72→0.54, Min-K% 0.68→0.49) as expected from NLL gap contraction. However, DeLong test for DIF vs ConStat is marginal (p=0.087) — underpowered at N=13. TOST equivalence fails (p=0.11 > 0.05), so reviewers can't rule out that DIF retention is coincidental. Median-tier outcome: suggestive robustness evidence insufficient for strong claim. Reviewers note 'N=13 is too few for definitive comparison; interesting pilot but not convincing.' Detection boundary at p=0.55 means DIF misses partial exploitation below 55%, which is a meaningful gap.\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"Independent ConStat-style perturbation testing on 250 MMLU items with LLM-generated semantic reformulations across 15 models.\",\n    \"results\": {\n      \"n_items_reformulated\": 248,\n      \"n_models_tested\": 15,\n      \"mean_performance_drop_original_vs_reformulated\": 0.034,\n      \"constat_detection_rate_fdr_010\": 0.127,\n      \"constat_detection_rate_fdr_005\": 0.089,\n      \"constat_auroc_vs_li_labels\": 0.61,\n      \"constat_auroc_non_rl_models\": 0.67,\n      \"constat_auroc_rl_models\": 0.52,\n      \"mean_reformulation_quality_score\": 0.82,\n      \"semantic_equivalence_human_check\": 0.91,\n      \"effect_size_detected_items_cohens_d\": 0.73\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: ConStat Detection Rates by Model Category\",\n        \"columns\": [\n          \"Model Category\",\n          \"N Models\",\n          \"Detection Rate (FDR=0.10)\",\n          \"Mean Effect Size (d)\"\n        ],\n        \"rows\": [\n          [\n            \"SFT-only\",\n            \"6\",\n            \"0.153\",\n            \"0.81\"\n          ],\n          [\n            \"Alignment-RL (DPO)\",\n            \"5\",\n            \"0.134\",\n            \"0.69\"\n          ],\n          [\n            \"Reasoning-RL (GRPO)\",\n            \"4\",\n            \"0.071\",\n            \"0.42\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ConStat independently validates the complementary detection space claim — it works where DIF doesn't (per-model, small effects) but fails where DIF succeeds (RL-robust, group-differential). However, in median tier this experiment is not included in the main paper because plan_003c (ensemble) was never fully executed and the ensemble narrative (original Claim 2) was dropped during the pivot. ConStat results go to appendix as supplementary comparison, supporting the 'detection methods are complementary' theme without being a core contribution.\\n\\nConStat operates at per-model level detecting performance drops on reformulations. On non-RL models (where memorization manifests as sensitivity to surface form), detection rate is moderate (12.7% at FDR=0.10). RL models show minimal surface-form sensitivity (AUROC 0.52, near chance) because PPO/GRPO training generalizes beyond verbatim patterns. The 3.4% mean performance drop across all items is small because most items aren't contaminated — only a subset shows the characteristic bimodal response pattern. AUROC vs Li et al. labels is weak (0.61) because, as established, web-overlap is a mismatched ground truth for item-level detection. In median tier, this provides a useful baseline comparison confirming ConStat's complementary detection space (non-RL, surface-form memorization) but doesn't change the paper's core narrative.\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"DVD generation variance detection on 12 open-weight models with 50 generations per item at T=0.8 on 300 MMLU items.\",\n    \"results\": {\n      \"n_models_tested\": 12,\n      \"n_items_per_model\": 300,\n      \"n_generations_per_item\": 50,\n      \"temperature\": 0.8,\n      \"bimodal_detection_rate\": 0.094,\n      \"dvd_auroc_vs_dif_flags\": 0.58,\n      \"dvd_auroc_verbatim_contamination\": 0.71,\n      \"dvd_auroc_variant_contamination\": 0.63,\n      \"mean_generation_variance_clean_items\": 0.34,\n      \"mean_generation_variance_contaminated_items\": 0.18,\n      \"gpu_hours_used\": 62,\n      \"inference_failures\": 3\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: DVD Detection Characteristics\",\n        \"columns\": [\n          \"Contamination Type\",\n          \"AUROC\",\n          \"Detection Rate (threshold=0.10)\",\n          \"Mean Variance Reduction\"\n        ],\n        \"rows\": [\n          [\n            \"Verbatim\",\n            \"0.71\",\n            \"0.134\",\n            \"0.21\"\n          ],\n          [\n            \"Variant/Paraphrase\",\n            \"0.63\",\n            \"0.072\",\n            \"0.12\"\n          ],\n          [\n            \"None (clean)\",\n            \"—\",\n            \"0.031 (FPR)\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DVD results are informative but not compelling enough for inclusion in the pivoted paper. The weak correspondence with DIF flags (AUROC 0.58) actually supports the paper's narrative that different detection methods capture different contamination mechanisms. However, the high GPU cost and low detection rates make this a poor cost-benefit trade for the characterization paper. In median tier, this remains in supplementary material at best. The result is useful for future ensemble work but doesn't strengthen any of the four core claims.\\n\\nDVD detects contamination via low generation variance (memorized items → consistently correct). Detection rate of 9.4% reflects that most contamination on MMLU is not verbatim memorization but pattern-level familiarity, which still produces moderate variance. AUROC for verbatim contamination (0.71) is better than variant (0.63) because verbatim produces clearer bimodal distributions. Correlation with DIF flags is weak (AUROC 0.58) because DIF and DVD measure fundamentally different signals: DIF measures cross-group differential, DVD measures within-model consistency. In median tier, DVD provides another complementary signal but is expensive (62 GPU-hours for 12 models × 300 items) and the low detection rate limits practical utility. The 3 inference failures (OOM on larger models) highlight scalability concerns.\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"Attempt to fuse DIF + ConStat + DVD into multi-signal ensemble with majority voting and weighted fusion.\",\n    \"results\": {\n      \"ensemble_2of3_precision\": 0.41,\n      \"ensemble_2of3_recall\": 0.23,\n      \"ensemble_weighted_auroc\": 0.66,\n      \"ensemble_fpr\": 0.087,\n      \"individual_dif_auroc\": 0.62,\n      \"individual_constat_auroc\": 0.61,\n      \"individual_dvd_auroc\": 0.58,\n      \"cross_val_weight_variance\": 0.15,\n      \"uniform_vs_optimized_auroc_gap\": 0.03,\n      \"coverage_overlap_dif_constat\": 0.31,\n      \"coverage_overlap_dif_dvd\": 0.22,\n      \"coverage_overlap_constat_dvd\": 0.38\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Ensemble vs Individual Detector Performance\",\n        \"columns\": [\n          \"Method\",\n          \"AUROC\",\n          \"Precision@FPR=0.10\",\n          \"Coverage (items flagged)\"\n        ],\n        \"rows\": [\n          [\n            \"DIF (MH)\",\n            \"0.62\",\n            \"0.38\",\n            \"31.3%\"\n          ],\n          [\n            \"ConStat\",\n            \"0.61\",\n            \"0.34\",\n            \"12.7%\"\n          ],\n          [\n            \"DVD\",\n            \"0.58\",\n            \"0.29\",\n            \"9.4%\"\n          ],\n          [\n            \"Ensemble (2-of-3)\",\n            \"0.66\",\n            \"0.41\",\n            \"6.8%\"\n          ],\n          [\n            \"Ensemble (weighted)\",\n            \"0.66\",\n            \"0.43\",\n            \"8.2%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ensemble fusion fails to produce a compelling unified detector because the three methods target different contamination mechanisms with minimal overlap. This is actually the correct scientific conclusion — it supports the pivot away from 'unified contamination detector' toward 'characterization of differential item functioning.' In median tier, plan_003c is reported as a negative result in the appendix: 'ensemble approaches require contamination mechanisms to be partially redundant; when mechanisms are orthogonal, fusion provides minimal lift.' This negative result paradoxically supports the paper's reframing: DIF measures something fundamentally different from per-model detectors.\\n\\nEnsemble shows modest improvement over individuals (AUROC 0.66 vs best individual 0.62) but the improvement is not dramatic because the three signals have limited overlap — they detect different contamination mechanisms with low redundancy. 2-of-3 majority voting has good precision (0.41) but very low recall (0.23) because few items trigger multiple detectors simultaneously. FPR<0.10 criterion is met (0.087) but only because the ensemble is very conservative. Cross-validation weight variance is high (0.15) indicating instability — different folds produce different optimal weights, suggesting the calibration set is too small for reliable fusion. In median tier, this experiment is effectively abandoned during the pivot away from 'detection methods' framing. The ensemble was the core of original Claim 2 which is now dropped.\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"Fit bifactor IRT model (general + 57 subject-specific factors) to METABENCH MMLU response matrix and attempt test equating via anchor items.\",\n    \"results\": {\n      \"bifactor_converged\": true,\n      \"n_iterations_to_converge\": 847,\n      \"general_factor_variance_explained\": 0.62,\n      \"mean_subject_factor_variance\": 0.14,\n      \"rmsea_bifactor\": 0.041,\n      \"cfi_bifactor\": 0.87,\n      \"n_anchor_items_selected\": 1842,\n      \"anchor_stability_criterion\": \"DIF A-class across all cohort pairs\",\n      \"equated_rho_original_vs_replaced\": 0.93,\n      \"equated_rho_anchor_only\": 0.97,\n      \"replacement_item_calibration_rmse\": 0.38,\n      \"kim_kolen_fixed_param_fit\": \"acceptable for 68% of replacement items\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Bifactor Model Fit Indices\",\n        \"columns\": [\n          \"Index\",\n          \"Value\",\n          \"Acceptable\",\n          \"Good\"\n        ],\n        \"rows\": [\n          [\n            \"RMSEA\",\n            \"0.041\",\n            \"< 0.08 ✓\",\n            \"< 0.05 ✓\"\n          ],\n          [\n            \"CFI\",\n            \"0.87\",\n            \"< 0.90 ✗\",\n            \"≥ 0.95 ✗\"\n          ],\n          [\n            \"TLI\",\n            \"0.84\",\n            \"< 0.90 ✗\",\n            \"≥ 0.95 ✗\"\n          ],\n          [\n            \"SRMR\",\n            \"0.063\",\n            \"< 0.08 ✓\",\n            \"< 0.05 ✗\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bifactor equating is technically feasible but falls short of production quality. The marginal model fit (CFI=0.87) reflects the known challenge that 57 MMLU subjects create a high-dimensional latent space poorly captured by a single general factor. In median tier, this experiment is reported honestly as 'pilot demonstration with limitations' — it shows the path to benchmark regeneration exists but requires better IRT models (multidimensional, or domain-clustered bifactor). Reviewers would likely say 'interesting future direction but not mature enough for a contribution claim.' This supports the paper's positioning of equating as future work rather than a current claim. Plan_014 already showed within-subject C%=38.1%, so the bifactor pre-check approach for reducing DIF was killed — this equating pilot inherits that limitation.\\n\\nBifactor model converges but with marginal fit (CFI=0.87 < 0.90 threshold, RMSEA=0.041 acceptable). The 57-subject structure is too fine-grained for the model to fit cleanly — general factor explains 62% of variance, individual subjects contribute 14% on average, leaving ~24% residual. Anchor item selection yields 1,842 stable items (14.7% of total), sufficient for equating but a relatively small anchor set. Equated score correlation (ρ=0.93) falls below the target ρ≥0.95, primarily because replacement item calibration via fixed-parameter approach has high RMSE (0.38) — the item parameters estimated on one cohort don't transfer perfectly. In median tier, this is a 'proof of concept with caveats' — equating is feasible in principle but the bifactor model's marginal fit and the below-target equated correlation weaken the regeneration claim. Reviewers note 'interesting pilot but ρ=0.93 suggests non-trivial information loss during equating.'\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"Generate replacement items for 200 DIF-flagged MMLU questions using LLM generation with construct constraints, calibrate via student simulation.\",\n    \"results\": {\n      \"n_items_generated\": 200,\n      \"n_items_passing_quality_filter\": 156,\n      \"difficulty_correlation_prompt_based\": 0.31,\n      \"difficulty_correlation_student_sim\": 0.64,\n      \"discrimination_correlation\": 0.42,\n      \"construct_alignment_human_rating\": 0.78,\n      \"holdout_panel_correlation\": 0.58,\n      \"mean_difficulty_mae\": 0.18,\n      \"pct_items_within_05_difficulty\": 0.43,\n      \"gpu_hours_used\": 187\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Calibration Method Comparison\",\n        \"columns\": [\n          \"Method\",\n          \"Difficulty ρ\",\n          \"Discrimination ρ\",\n          \"% Within ±0.5 Target\"\n        ],\n        \"rows\": [\n          [\n            \"Prompt-based targeting\",\n            \"0.31\",\n            \"0.28\",\n            \"0.24\"\n          ],\n          [\n            \"Student simulation (5 students)\",\n            \"0.64\",\n            \"0.42\",\n            \"0.43\"\n          ],\n          [\n            \"Student simulation (20 students)\",\n            \"0.68\",\n            \"0.45\",\n            \"0.47\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Item generation calibration shows promise but not maturity. The gap between student simulation performance here (ρ=0.64) and published results (r=0.75-0.82) likely reflects MMLU's domain breadth — calibrating 'abstract algebra' items requires different student models than 'clinical knowledge.' In median tier, this supports the future work framing: 'automated benchmark regeneration is feasible with improved calibration pipelines' but is not ready as a standalone contribution. Combined with plan_005's marginal equating results, the regeneration storyline (original Claim 3) remains firmly in future work territory. The 187 GPU-hours for 200 items also highlights cost concerns for full-scale deployment.\\n\\nItem generation produces grammatically correct, construct-aligned questions (78% human-rated alignment) but calibration accuracy is moderate. Student simulation improves difficulty prediction (ρ=0.64) over prompt-based targeting (ρ=0.31), consistent with literature (arXiv 2601.09953 reports r=0.75-0.82 — our lower value reflects MMLU's broader domain coverage vs focused benchmarks). Only 43% of generated items fall within ±0.5 difficulty of the target, meaning majority would need iterative recalibration. Discrimination correlation is lower (0.42) because item discrimination depends on subtle psychometric properties harder to control via generation. In median tier, this demonstrates that LLM item generation is a viable but immature pipeline — insufficient for automated benchmark regeneration without human-in-the-loop validation. Reviewers would flag the 58% holdout correlation as 'items don't transfer well to unseen models.'\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"Simulate cumulative Bayesian DIF with informative priors from prior administrations over 4 successive benchmark waves.\",\n    \"results\": {\n      \"single_administration_power_delta10\": 0.41,\n      \"cumulative_2_administrations_power\": 0.54,\n      \"cumulative_3_administrations_power\": 0.67,\n      \"cumulative_4_administrations_power\": 0.74,\n      \"single_administration_fpr\": 0.042,\n      \"cumulative_4_fpr\": 0.051,\n      \"power_gain_per_administration\": [\n        0.13,\n        0.13,\n        0.07\n      ],\n      \"convergence_plateau\": \"~4 administrations\",\n      \"bayes_factor_threshold\": 3.0,\n      \"pct_items_bf_gt_3_after_4_admin\": 0.68\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Cumulative Power by Effect Size\",\n        \"columns\": [\n          \"Administrations\",\n          \"δ=0.8\",\n          \"δ=1.0\",\n          \"δ=1.2\",\n          \"δ=1.4\"\n        ],\n        \"rows\": [\n          [\n            \"1\",\n            \"0.24\",\n            \"0.41\",\n            \"0.55\",\n            \"0.68\"\n          ],\n          [\n            \"2\",\n            \"0.37\",\n            \"0.54\",\n            \"0.69\",\n            \"0.81\"\n          ],\n          [\n            \"3\",\n            \"0.48\",\n            \"0.67\",\n            \"0.79\",\n            \"0.89\"\n          ],\n          [\n            \"4\",\n            \"0.54\",\n            \"0.74\",\n            \"0.84\",\n            \"0.92\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bayesian cumulative DIF is theoretically elegant and directly addresses the power limitation identified in plan_001 (single-shot DIF only detects large effects δ≥1.4). However, it's purely simulation-based in the current paper because METABENCH provides only a single temporal snapshot (2023 vs 2024-H1), not 4 successive administrations. In median tier, reviewers appreciate the methodological contribution but note 'this requires longitudinal benchmark infrastructure that doesn't yet exist.' Best positioned as a concrete recommendation for benchmark maintainers: 'if you collect response matrices over time, here's how to accumulate evidence of item degradation.' Strengthens the 'measurement science for ML benchmarks' narrative without requiring new empirical data.\\n\\nCumulative Bayesian approach shows expected power improvement (0.41→0.74 over 4 administrations for medium effects δ=1.0) as evidence accumulates. This is a well-established psychometric result (Sinharay 2006) applied to the LLM benchmark setting. FPR remains controlled (0.051) because Bayesian shrinkage prevents false alarms from accumulating. Power gains show diminishing returns (0.13, 0.13, 0.07) — the fourth administration adds less because most detectable items are already identified. In median tier, this is simulation-only (no real longitudinal MMLU data exists with 4 temporal waves), so reviewers note 'theoretically sound but purely simulated — would need actual longitudinal benchmark deployment to validate.' Positioned as future monitoring methodology, not a current empirical contribution.\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"Formal analysis of benchmark validity under progressive item replacement (5% to 50%) using METABENCH empirical data.\",\n    \"results\": {\n      \"rho_5pct_replacement\": 0.998,\n      \"rho_10pct_replacement\": 0.996,\n      \"rho_20pct_replacement\": 0.991,\n      \"rho_50pct_replacement\": 0.972,\n      \"reliability_alpha_full\": 0.943,\n      \"reliability_alpha_50pct_replaced\": 0.921,\n      \"construct_coverage_5pct\": 0.97,\n      \"construct_coverage_50pct\": 0.84,\n      \"theoretical_bound_rho_vs_replacement_rate\": \"ρ ≥ 1 - 1.3r (r = replacement fraction)\",\n      \"critical_replacement_threshold\": \"~35% before ρ < 0.98\",\n      \"dif_targeted_vs_random_replacement_rho_gap\": 0.008\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Validity Metrics Under Progressive Replacement\",\n        \"columns\": [\n          \"Replacement %\",\n          \"Spearman ρ\",\n          \"Cronbach α\",\n          \"Construct Coverage\",\n          \"Max Rank Δ\"\n        ],\n        \"rows\": [\n          [\n            \"0% (baseline)\",\n            \"1.000\",\n            \"0.943\",\n            \"1.00\",\n            \"0\"\n          ],\n          [\n            \"5%\",\n            \"0.998\",\n            \"0.941\",\n            \"0.97\",\n            \"23\"\n          ],\n          [\n            \"10%\",\n            \"0.996\",\n            \"0.938\",\n            \"0.95\",\n            \"47\"\n          ],\n          [\n            \"20%\",\n            \"0.991\",\n            \"0.932\",\n            \"0.91\",\n            \"112\"\n          ],\n          [\n            \"50%\",\n            \"0.972\",\n            \"0.921\",\n            \"0.84\",\n            \"341\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Graceful degradation analysis primarily serves as supplementary validation for plan_017's core finding. It formalizes what the ρ=0.997 result already implies: MMLU has enormous measurement redundancy. In median tier, this becomes a double-edged sword — reviewers use it to argue 'if the benchmark is so redundant, the 38% instability finding is merely academic, not practically concerning.' The paper's rebuttal must be: 'redundancy protects rankings but masks that 31% of items carry disproportionate discriminative information (z=-8 to -49σ from plan_017). Efficiency, not validity, is the real concern.' The 35% critical threshold aligns with the observed 38% DIF rate — we're near the edge where replacement starts to matter, even if we haven't crossed it yet.\\n\\nProgressive replacement analysis reveals extreme ranking robustness — even 50% item replacement maintains ρ=0.972. This is consistent with plan_017's finding that ρ=0.997 after removing 31% DIF items. MMLU's 12,508 items provide massive redundancy; any subset of ~6,000+ items preserves relative model ordering. Reliability (Cronbach's α) degrades more noticeably (0.943→0.921 at 50%) because replacement items have higher calibration error. Construct coverage (proportion of original 57 subjects adequately sampled) drops to 0.84 at 50% because some small subjects (N<50 items) lose coverage entirely. The near-linear relationship ρ ≥ 1 - 1.3r holds empirically up to r=0.4. In median tier, this result cuts both ways: it shows equating is feasible (replacements don't destroy validity) but also undermines urgency (if rankings are so stable, why bother replacing items?). Reviewers invoke the 'so what' critique: ρ=0.997→0.972 is still excellent.\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"Implement Item-Focused Trees treating model release date as continuous covariate, comparing detection power and flexibility vs categorical temporal DIF.\",\n    \"results\": {\n      \"n_items_analyzed\": 12508,\n      \"ift_c_pct_equivalent\": 28.4,\n      \"ift_vs_categorical_jaccard\": 0.72,\n      \"ift_unique_flags\": 0.08,\n      \"categorical_unique_flags\": 0.12,\n      \"ift_split_point_median\": \"2023-09-15\",\n      \"ift_nonlinear_items_pct\": 0.14,\n      \"ift_power_gain_vs_categorical\": 0.03,\n      \"computation_time_hours\": 4.2\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: IFT vs Categorical DIF Comparison\",\n        \"columns\": [\n          \"Method\",\n          \"Items Flagged\",\n          \"Unique Flags\",\n          \"Overlap (Jaccard)\",\n          \"Computation Time\"\n        ],\n        \"rows\": [\n          [\n            \"Categorical MH (2023 vs 2024-H1)\",\n            \"31.3%\",\n            \"12%\",\n            \"—\",\n            \"0.3 hours\"\n          ],\n          [\n            \"Item-Focused Trees (continuous date)\",\n            \"28.4%\",\n            \"8%\",\n            \"0.72\",\n            \"4.2 hours\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"IFT serves primarily as a robustness check confirming that the categorical temporal split was not misleading. The 72% overlap validates the simpler approach while the 14% nonlinear items are methodologically interesting but don't change conclusions. In median tier, this goes to supplementary material as 'sensitivity analysis: continuous treatment of release date produces concordant results (Jaccard=0.72), with 14% of items showing nonlinear trajectories warranting future investigation.' Reviewers may note that IFT is more principled but the limited power gain doesn't justify the complexity for the main paper. Most useful as a reviewer rebuttal resource: 'our arbitrary temporal split is validated by the continuous approach.'\\n\\nItem-Focused Trees detect 28.4% of items as exhibiting DIF along the release-date continuum (vs 31.3% for categorical temporal split). Jaccard overlap of 0.72 with categorical DIF shows substantial agreement — most items flagged by IFT are also flagged by categorical MH, confirming the temporal split was reasonable. IFT identifies 8% unique items (gradual drift not captured by binary split) and misses 12% that categorical catches (items with sharp discontinuity better detected by group contrast). 14% of items show nonlinear DIF trajectories (early models and late models both struggle, middle cohort performs differently). Power gain is minimal (+0.03) because the binary temporal split already captures the primary contrast. In median tier, IFT provides methodological sophistication but minimal empirical gain — reviewers appreciate the robustness check ('arbitrary temporal split didn't distort results') but note 'the continuous approach doesn't change your main finding.'\"\n  },\n  {\n    \"name\": \"architecture_stratified_dif\",\n    \"description\": \"Run DIF within decoder-only architecture subpopulation to test whether IRT fit improves and spurious DIF reduces when architecture heterogeneity is removed.\",\n    \"results\": {\n      \"n_decoder_only_models\": 3412,\n      \"n_ref_decoder_only_2023\": 891,\n      \"n_foc_decoder_only_2024h1\": 523,\n      \"decoder_only_c_pct\": 28.2,\n      \"full_population_c_pct\": 31.3,\n      \"delta_c_pct\": -3.1,\n      \"rmsea_full_population\": 0.089,\n      \"rmsea_decoder_only\": 0.067,\n      \"cfi_full_population\": 0.78,\n      \"cfi_decoder_only\": 0.83,\n      \"tli_decoder_only\": 0.81,\n      \"srmr_decoder_only\": 0.058,\n      \"jaccard_decoder_vs_full\": 0.81,\n      \"fpr_decoder_only\": 0.282,\n      \"tpr_decoder_only_semi_synthetic_p05\": 0.79,\n      \"delta_tpr_decoder_only\": 0.508\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: IRT Fit Comparison: Full Population vs Decoder-Only\",\n        \"columns\": [\n          \"Metric\",\n          \"Full Population\",\n          \"Decoder-Only\",\n          \"Improvement\",\n          \"Acceptable Threshold\"\n        ],\n        \"rows\": [\n          [\n            \"RMSEA\",\n            \"0.089\",\n            \"0.067\",\n            \"−0.022\",\n            \"< 0.05\"\n          ],\n          [\n            \"CFI\",\n            \"0.78\",\n            \"0.83\",\n            \"+0.05\",\n            \"≥ 0.90\"\n          ],\n          [\n            \"TLI\",\n            \"0.75\",\n            \"0.81\",\n            \"+0.06\",\n            \"≥ 0.90\"\n          ],\n          [\n            \"SRMR\",\n            \"0.074\",\n            \"0.058\",\n            \"−0.016\",\n            \"< 0.05\"\n          ],\n          [\n            \"C% (ETS)\",\n            \"31.3%\",\n            \"28.2%\",\n            \"−3.1pp\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Plan_010 is the proactive defense experiment against the 'IRT model misfit' reviewer concern. In median tier, the result is honest but not fully reassuring: architecture stratification helps (3.1pp C% reduction, RMSEA improvement) but doesn't solve the fundamental issue that unidimensional IRT is a simplification for 57-subject MMLU. The paper frames this as: 'architecture stratification provides modest improvement, confirming that population homogeneity is beneficial but not sufficient — multidimensional IRT or domain-specific modeling remain future directions.' Reviewers likely say 'you've shown the problem is partially addressable but haven't solved it — reframe 38% as upper bound, 28% as lower bound under controlled conditions.' This is consistent with median-tier narrative guidance: 'instability reflects a mixture' with explicit bounds.\\n\\nArchitecture stratification reduces C% from 31.3% to 28.2% — a modest 3.1pp improvement, not the dramatic reduction that would indicate architecture heterogeneity was the primary driver of spurious DIF. IRT fit improves marginally (RMSEA 0.089→0.067, from 'poor' to 'marginal'; CFI 0.78→0.83, still below 0.90 'acceptable'). This confirms that architecture mixing contributes some model misfit but is not the dominant source — the remaining 28.2% DIF reflects genuine temporal item instability within decoder-only models. Jaccard overlap of 0.81 with full-population flags confirms most DIF items are flagged regardless of population composition. In median tier, this is the 'modest improvement' outcome specified: reviewers acknowledge architecture stratification helps but note 'RMSEA=0.067 and CFI=0.83 are still below standard fit thresholds, suggesting deeper structural issues with unidimensional IRT on MMLU.'\"\n  }\n]",
      "numLines": 586,
      "startLine": 1,
      "totalLines": 586
    }
  },
  "sourceToolAssistantUUID": "15a3eaea-4da3-40b7-96d3-9bf21b907feb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "922e32b8-9e95-44d4-a9f5-911898e839bc",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with IRT equated benchmark",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e"
}
```

---

### Assistant

_source line 14 · 2026-05-21T01:49:46.098Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to also read any existing experiment data referenced in the paper framing that might not be in the experiment_data.json. The paper framing references plan_001, plan_004, plan_011, plan_014, plan_016, plan_017 etc. Let me check if there are additional data files.

Actually, I have all I need. Let me also read the paper-writing-norms skill to follow proper academic writing style.

Actually, the instructions say I should load skills "按需" (on demand). Let me focus on writing the paper based on what I have. I have:


- experiment_data.json with 10 experiments
- paper_framing.md with the full framing

The paper framing references evidence from plans not in experiment_data.json (plan_001, plan_004, plan_011, plan_014, plan_016, plan_017). These are the core experiments that contain the main claims' evidence. The experiment_data.json contains supplementary experiments (RL robustness, ConStat, DVD, ensemble, bifactor equating, item generation, Bayesian DIF, graceful degradation, IFT, architecture-stratified DIF).

Looking more carefully at the paper framing, I see the core experiments referenced are the ones I don't have data for, while the supplementary ones are in my dataset. the core claims and the experiment_data.json for the supplementary experiments.

For the narrative framing, I'm softening some of the language—moving Claim 2 away from "fundamental blind spot" toward "underappreciated methodological gap," and adding a caveat that the 38% instability reflects both capability gains and differential item functioning. I'm also reframing the high correlation as a measurement efficiency issue rather than a strength, downgrading the GSM1K results to suggestive evidence, and positioning the semi-synthetic validation framework as the most portable contribution for the ICLR findings track.

Now I'm structuring the paper with an abstract, introduction, background on DIF, and methods sections covering both the DIF analysis framework and semi-synthetic validation approach. I'll need to integrate all 10 experiments from the supplementary data throughout the results.

The instructions require sections or tables for each of the 10 experiments, so I'm organizing the results around the three main claims: temporal item instability, ground truth meta-critique, and the semi-synthetic validation framework, with subsections pulling the relevant framing numbers and experimental evidence. I'm reorganizing this into a cleaner structure with core findings as the main contribution, then grouping the robustness checks and supplementary experiments together rather than listing them sequentially. Now I'm pulling the key numerical results from the paper framing—baseline C% at 31.3%, enrichment factor of 0.96, and various performance deltas across experiments like the GSM8K improvements and correlation coefficients that show strong statistical significance. Looking at the remaining experimental results, I'm seeing strong performance across the Bayesian and tree-based approaches—the cumulative Bayesian method shows substantial power gains, graceful degradation maintains stability across contamination levels, and the stratified architecture achieves meaningful improvements in both classification accuracy and model fit. Now I need to carefully frame the narrative around these findings, particularly softening some of the stronger claims about methodological gaps and adding explicit caveats about what the 38% improvement actually represents—distinguishing between genuine capability gains and DIF detection artifacts—while recontextualizing the high correlation values as efficiency metrics rather than just technical achievements.

Writing the paper in LaTeX...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "922e32b8-9e95-44d4-a9f5-911898e839bc",
  "isSidechain": false,
  "requestId": "req_011CbEscEjLAWwpzn1gfUYuG",
  "type": "assistant",
  "uuid": "9cc47c18-dcd0-4352-aa49-faaab912691c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJCcQ27k6Gd4hJTBFFNNRX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3326,
      "cache_creation_input_tokens": 10457,
      "cache_read_input_tokens": 23138,
      "output_tokens": 2406,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10457,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3326,
          "output_tokens": 2406,
          "cache_read_input_tokens": 23138,
          "cache_creation_input_tokens": 10457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10457
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

_source line 15 · 2026-05-21T01:49:46.120Z_

Now let me read the paper-writing-norms skill for style guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cc47c18-dcd0-4352-aa49-faaab912691c",
  "isSidechain": false,
  "requestId": "req_011CbEscEjLAWwpzn1gfUYuG",
  "type": "assistant",
  "uuid": "0beaefed-454d-4bca-b762-252b33d96786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJCcQ27k6Gd4hJTBFFNNRX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3326,
      "cache_creation_input_tokens": 10457,
      "cache_read_input_tokens": 23138,
      "output_tokens": 2406,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10457,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3326,
          "output_tokens": 2406,
          "cache_read_input_tokens": 23138,
          "cache_creation_input_tokens": 10457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10457
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

_source line 16 · 2026-05-21T01:49:46.707Z_

<details open><summary>🔧 Tool call — Read · `toolu_0118wdBThYjQnoTNGgmPGVH2`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0beaefed-454d-4bca-b762-252b33d96786",
  "isSidechain": false,
  "requestId": "req_011CbEscEjLAWwpzn1gfUYuG",
  "type": "assistant",
  "uuid": "f0f158ca-69a2-497f-a357-af3ab57d0924",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJCcQ27k6Gd4hJTBFFNNRX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3326,
      "cache_creation_input_tokens": 10457,
      "cache_read_input_tokens": 23138,
      "output_tokens": 2406,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10457,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3326,
          "output_tokens": 2406,
          "cache_read_input_tokens": 23138,
          "cache_creation_input_tokens": 10457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10457
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

_source line 17 · 2026-05-21T01:49:46.716Z_

<details><summary>↩ Tool result · `toolu_0118wdBThYjQnoTNGgmPGVH2`</summary>

```text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0f158ca-69a2-497f-a357-af3ab57d0924",
  "isSidechain": false,
  "promptId": "de177bb0-8153-4b40-a54f-7680d3583965",
  "type": "user",
  "uuid": "ed0f39a3-4d56-40db-bfe5-46b407078b54",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "f0f158ca-69a2-497f-a357-af3ab57d0924",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-21T01:49:50.877Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have enough context. Let me now write the full paper. I need to carefully organize all 10 experiments from experiment_data.json into the paper structure while following the narrative guidance.

Let me write the LaTeX now. I'll be comprehensive but concise.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed0f39a3-4d56-40db-bfe5-46b407078b54",
  "isSidechain": false,
  "requestId": "req_011CbEsftTYZqzFhGxupzj1P",
  "type": "assistant",
  "uuid": "2218da9a-ed2e-4cc3-ae6e-1ee272ca47ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gvs86xL6osSWTr3GrMQb9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7712,
      "cache_read_input_tokens": 33595,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7712,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 33595,
          "cache_creation_input_tokens": 7712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7712
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

_source line 19 · 2026-05-21T01:49:51.393Z_

Now I have all inputs. Let me write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2218da9a-ed2e-4cc3-ae6e-1ee272ca47ae",
  "isSidechain": false,
  "requestId": "req_011CbEsftTYZqzFhGxupzj1P",
  "type": "assistant",
  "uuid": "786a3677-11d5-4c83-892a-611eb848fa42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gvs86xL6osSWTr3GrMQb9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7712,
      "cache_read_input_tokens": 33595,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7712,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 33595,
          "cache_creation_input_tokens": 7712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7712
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

_source line 20 · 2026-05-21T01:49:54.098Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014kWzdp4v3AgXWTzbQ12kBR`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/",
  "description": "List target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "786a3677-11d5-4c83-892a-611eb848fa42",
  "isSidechain": false,
  "requestId": "req_011CbEsftTYZqzFhGxupzj1P",
  "type": "assistant",
  "uuid": "117a7ea1-1e93-4b95-9352-e2174bce4bf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gvs86xL6osSWTr3GrMQb9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7712,
      "cache_read_input_tokens": 33595,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7712,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 33595,
          "cache_creation_input_tokens": 7712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7712
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "117a7ea1-1e93-4b95-9352-e2174bce4bf8",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with IRT equated benchmark",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e"
}
```

---

### Tool result

_source line 23 · 2026-05-21T01:49:54.268Z_

<details><summary>↩ Tool result · `toolu_014kWzdp4v3AgXWTzbQ12kBR`</summary>

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
  "parentUuid": "117a7ea1-1e93-4b95-9352-e2174bce4bf8",
  "isSidechain": false,
  "promptId": "de177bb0-8153-4b40-a54f-7680d3583965",
  "type": "user",
  "uuid": "02b9a6e5-fcce-4d74-a652-aedd22049030",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "117a7ea1-1e93-4b95-9352-e2174bce4bf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T01:53:28.674Z_

<details open><summary>🔧 Tool call — Write · `toolu_019Q5LJXFf2CQTLUY6a2q61m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/paper.tex",
  "content": "\\documentclass[10pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{natbib}\n\\usepackage[small]{caption}\n\n\\title{Psychometric Characterization of Item-Level Instability\\\\in LLM Benchmarks via Differential Item Functioning}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nLarge Language Model (LLM) benchmarks implicitly assume temporal score comparability: a score of 80\\% today should reflect the same latent ability as 80\\% one year ago.\nWe test this assumption by applying Differential Item Functioning (DIF) analysis---a classical psychometric method for detecting item-level behavioral anomalies---to the METABENCH response matrix (5{,}227 models $\\times$ 12{,}508 MMLU items).\nWe report three findings.\nFirst, 38\\% of MMLU items exhibit large DIF (ETS C category) between 2023 and 2024-H1 model cohorts, persisting within every subject domain (per-subject C\\%: 31--45\\%).\nThis instability reflects a mixture of genuine capability improvement ($\\rho{=}0.307$ with domain accuracy gains) and differential item functioning, and cannot be decomposed into a single cause.\nSecond, we identify an underappreciated methodological gap in contamination detection validation: web-overlap labels measure global item exposure, not differential functioning, producing expected enrichment ${\\approx}1.0$ against DIF flags.\nThird, we propose a semi-synthetic validation framework that injects controlled differential contamination into real response matrices; cross-subject matching eliminates false-positive inflation ($\\Delta\\text{FPR}{=}0.000$) while confirming detection power ($\\Delta\\text{TPR}{=}{+}0.508$ on MMLU, ${+}0.818$ on GSM8K).\nWe further show that MMLU exhibits massive measurement redundancy ($\\rho{\\approx}0.997$ after removing 31\\% of items), reframing the instability as a measurement efficiency problem rather than a validity crisis.\nCode and data will be released upon publication.\n\\end{abstract}\n\n%% ============================================================\n%% 1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nBenchmarks such as MMLU~\\citep{hendrycks2021mmlu} underpin comparative evaluation of LLMs.\nWhen practitioners report that ``Model B outperforms Model A by 5 points on MMLU,'' they implicitly assume both scores reflect the same latent construct measured under equivalent conditions.\nPsychometrics calls this assumption \\emph{measurement invariance}: the test functions identically across examinee populations.\n\nThis assumption is unlikely to hold in the LLM ecosystem, where models released months apart differ in training data composition, architecture, and optimization objective.\nIf a subset of items behaves differently across model generations---due to data contamination, capability shifts, or both---cross-temporal score comparisons carry uncontrolled item-level variance.\n\nWe bring Differential Item Functioning (DIF)---a family of methods developed over four decades in educational testing~\\citep{holland1993dif}---to characterize item-level behavioral drift in LLM benchmarks at unprecedented scale.\nApplying the Mantel--Haenszel (MH) procedure to the METABENCH response matrix (5{,}227 models $\\times$ 12{,}508 MMLU items), we find:\n\n\\begin{enumerate}\n\\item \\textbf{38\\% of MMLU items are functionally unstable} across model generations (ETS C category, $|\\Delta_\\text{MH}|{\\geq}1.5$). This persists within every subject domain (31--45\\% per subject) and is not a statistical artifact (random-split sanity check: 0.18\\%). The instability reflects a mixture of capability improvement and differential item functioning ($\\rho{=}0.307$ between C\\% and domain accuracy gains).\n\n\\item \\textbf{An underappreciated methodological gap} in contamination detection validation: web-overlap labels~\\citep{li2024contamination} measure whether items are publicly accessible---a global, model-agnostic property---rather than whether items function differently across cohorts. Enrichment ${\\approx}1.0$ between DIF flags and web-overlap labels is expected, not indicative of detector failure. Semi-synthetic injection confirms DIF's detection power ($\\Delta\\text{TPR}{=}{+}0.508$).\n\n\\item \\textbf{A reusable semi-synthetic validation framework} for any item-level contamination detector. By injecting known differential contamination into real response matrices and measuring $\\Delta\\text{TPR}$, the framework provides controlled evaluation infrastructure. Cross-subject matching eliminates matching-variable contamination ($\\Delta\\text{FPR}{=}0.000$), and the framework generalizes across benchmarks (GSM8K: $\\Delta\\text{TPR}{=}{+}0.818$).\n\n\\item \\textbf{DIF as diagnostic lens}: MMLU rankings exhibit massive measurement redundancy ($\\rho{\\approx}0.997$ after 31\\% item removal), but DIF items concentrate discriminative signal (removal causes more ranking disruption than random, $z{=}{-}8$ to ${-}49\\sigma$). Suggestive cross-benchmark evidence from GSM1K contamination gaps ($r{=}{-}0.478$, $p{=}0.005$, $N{=}33$) indicates DIF flags capture genuine capability differences rather than contamination artifacts.\n\\end{enumerate}\n\nWe additionally report extensive robustness analyses (architecture stratification, item-focused trees, RL-model sensitivity), complementary detection baselines (ConStat perturbation, generation variance), a negative result on multi-signal ensemble fusion, and pilot studies on benchmark regeneration via IRT equating and LLM-based item generation.\n\n%% ============================================================\n%% 2  BACKGROUND\n%% ============================================================\n\\section{Preliminaries: DIF for LLM Benchmarks}\n\n\\paragraph{Differential Item Functioning.}\nAn item exhibits DIF when examinees of equal ability from different groups have unequal probabilities of answering correctly.\nIn educational testing, groups are typically demographic (e.g., gender, ethnicity); we define groups \\emph{temporally}: a reference cohort (models released before 2024) and a focal cohort (models released 2024-H1).\n\n\\paragraph{Mantel--Haenszel procedure.}\nWe use the MH $\\chi^2$ test with ETS $\\Delta_\\text{MH}$ effect-size classification:\n\\textbf{A} (negligible, $|\\Delta_\\text{MH}|{<}1.0$),\n\\textbf{B} (moderate, $1.0{\\leq}|\\Delta_\\text{MH}|{<}1.5$), and\n\\textbf{C} (large, $|\\Delta_\\text{MH}|{\\geq}1.5$).\nItems are matched on total score to control for overall ability differences.\n\n\\paragraph{IRT context.}\nItem Response Theory (IRT) models item responses as a function of latent ability $\\theta$.\nA 2-parameter logistic (2PL) model specifies $P(X_{ij}{=}1|\\theta_j) = \\text{logistic}(a_i(\\theta_j - b_i))$, where $a_i$ is discrimination and $b_i$ is difficulty.\nDIF manifests as cross-group differences in item parameters.\nWe use IRT primarily for bifactor modeling and equating analyses (Sections~\\ref{sec:bifactor} and~\\ref{sec:calibration}).\n\n\\paragraph{Why DIF, not contamination detection?}\nContamination detectors (Min-K\\%, ConStat, n-gram overlap) answer: ``Is this model contaminated?''\nDIF answers a different question: ``Does this item function differently across model cohorts?''\nThis distinction is critical---DIF is a \\emph{characterization} tool for benchmark quality, not a per-model contamination detector.\n\n%% ============================================================\n%% 3  EXPERIMENTAL SETUP\n%% ============================================================\n\\section{Experimental Setup}\n\n\\paragraph{Data.}\nWe use the METABENCH response matrix~\\citep{metabench2024}: binary item responses for 5{,}227 models on 12{,}508 MMLU items across 57 subject domains.\nTemporal cohorts are defined by model release date: reference (pre-2024, $N_\\text{ref}{=}2{,}891$) and focal (2024-H1, $N_\\text{foc}{=}2{,}336$).\nFor cross-benchmark analyses, we additionally use METABENCH's GSM8K partition (1{,}319 items $\\times$ 6{,}702 models).\n\n\\paragraph{DIF analysis pipeline.}\nFor each of the 12{,}508 items, we compute the MH $\\Delta_\\text{MH}$ statistic using total score on remaining items as the matching variable.\nItems are classified into ETS A/B/C categories.\nWe define C\\% as the proportion of items in category C.\n\n\\paragraph{Semi-synthetic injection protocol.}\nTo validate detection power, we inject differential contamination by flipping incorrect$\\rightarrow$correct responses for randomly selected items in the focal cohort at controlled injection probabilities $p \\in \\{0.3, 0.5, 0.7, 1.0\\}$.\nDetection power is measured as $\\Delta\\text{TPR} = \\text{TPR}_\\text{injected} - \\text{TPR}_\\text{baseline}$.\n\n%% ============================================================\n%% 4  CORE FINDINGS\n%% ============================================================\n\\section{Core Findings}\n\n\\subsection{Item Instability Across Model Generations (Claim 1)}\n\\label{sec:instability}\n\nApplying MH DIF analysis to all 12{,}508 MMLU items yields C\\%${=}31.3$\\%, with 3{,}912 items exhibiting large differential functioning between temporal cohorts.\nWithin-subject analysis confirms this is not driven by cross-domain confounding: every one of 57 MMLU subjects shows C\\% between 31\\% and 45\\%, with a mean of 38.1\\%.\n\nA random-split sanity check (randomly assigning models to pseudo-cohorts regardless of release date) produces C\\%${=}0.18$\\%, confirming the temporal signal is not a statistical artifact.\n\n\\paragraph{Capability improvement confound.}\nThe correlation between per-subject C\\% and domain accuracy improvement is $\\rho{=}0.307$ ($p{=}0.02$), indicating that item instability is partially explained by models improving differentially across domains.\nWe emphasize that the 38\\% figure reflects a \\emph{mixture} of genuine capability improvement and differential item functioning---we cannot decompose these contributions with available data.\n\n\\subsection{Ground Truth Methodology Gap (Claim 2)}\n\\label{sec:groundtruth}\n\nWeb-overlap contamination labels~\\citep{li2024contamination} classify items as ``contaminated'' based on n-gram presence in Common Crawl.\nThese labels measure a \\emph{global} property (public accessibility) that applies nearly uniformly to MMLU items, which have been publicly available since 2020.\nDIF, by contrast, measures a \\emph{differential} property: whether an item functions differently across model cohorts.\n\nEmpirically, DIF flag enrichment against Li et al.\\ labels is ${\\approx}1.0$ (no enrichment).\nThis is expected when web-overlap labels lack item-level discriminative power for the quantity DIF measures.\nThis represents an underappreciated methodological gap: studies validating item-level contamination detectors against web-overlap labels are evaluating against a reference standard that cannot distinguish differentially-functioning items from stable ones.\n\nSemi-synthetic injection (Section~\\ref{sec:semisynthetic}) confirms DIF can detect differential contamination ($\\Delta\\text{TPR}{=}{+}0.508$ at injection probability $p{=}0.5$), demonstrating that the enrichment ${\\approx}1.0$ result reflects ground-truth limitations, not detector failure.\n\n\\subsection{Semi-Synthetic Validation Framework (Claim 3)}\n\\label{sec:semisynthetic}\n\nWe propose a reusable validation framework for item-level contamination detectors.\nThe key innovation is the matching variable: using total score on \\emph{other} subjects (cross-subject matching) rather than total score on the same subject (within-subject matching) as the MH conditioning variable.\n\n\\paragraph{Cross-subject matching eliminates FPR inflation.}\nWithin-subject matching suffers from matching-variable contamination: if injected items inflate total score on that subject, the matching variable is no longer a clean ability proxy.\nCross-subject matching avoids this because injection targets are restricted to one subject, while matching uses scores on the remaining 56.\nAcross all 5 tested subjects, cross-subject matching yields $\\Delta\\text{FPR}{=}0.000$, whereas within-subject matching produces FPR inflation of ${+}0.186$.\n\n\\paragraph{Detection power.}\nOn MMLU, $\\Delta\\text{TPR}{=}{+}0.508$ at $p{=}0.5$, with dose--response across injection probabilities ($p{=}0.3$: lower; $p{=}1.0$: higher).\nFour of five tested subjects show $\\Delta\\text{TPR}{>}0.3$.\n\n\\paragraph{Cross-benchmark replication.}\nOn GSM8K (1{,}319 items $\\times$ 6{,}702 models), the framework yields $\\Delta\\text{TPR}{=}{+}0.818$ (standard matching) and ${+}0.517$ (external matching), confirming portability to single-domain math benchmarks.\nGSM8K temporal DIF analysis independently reveals C\\%${=}18.9$\\%, lower than MMLU but non-trivial.\n\n\\subsection{DIF as Diagnostic Lens (Claim 4)}\n\\label{sec:diagnostic}\n\n\\paragraph{Measurement redundancy.}\nRemoving all 31\\% C-category DIF items and re-ranking models yields Spearman $\\rho{\\approx}0.997$ with the full-item ranking.\nThis extreme robustness reveals that MMLU contains massive measurement redundancy: the stable 69\\% of items suffice to preserve model ordering.\nWe reframe this as a \\emph{measurement efficiency} problem---MMLU uses 12{,}508 items where ${\\sim}8{,}600$ would produce equivalent rankings.\n\n\\paragraph{DIF items carry discriminative signal.}\nDespite ranking robustness, DIF item removal causes significantly \\emph{more} ranking disruption than random removal of the same number of items ($z{=}{-}8$ to ${-}49\\sigma$ across 21/21 conditions).\nDIF items exhibit $1.09\\times$ cross-cohort accuracy swing versus $0.96\\times$ for stable items---they concentrate the information that differentiates model generations.\n\n\\paragraph{Model-specific patterns.}\nDIF analysis reveals which models benefit most from unstable items: phi-3 and llama-3 families gain ${+}700$--$850$ ranks from DIF items, while mistral-merge models lose $-400$ to $-587$ ranks.\n\n\\paragraph{GSM1K cross-benchmark evidence (suggestive).}\nOn 33 matched models with GSM1K contamination gap data, DIF flags anti-correlate with contamination ($r{=}{-}0.478$, $p{=}0.005$; partial $r{=}{-}0.385$ controlling for accuracy; permutation $p{=}0.014$).\nModels with high contamination gaps (Phi, Gemma families) perform \\emph{worse} on DIF items.\nThis provides suggestive evidence that DIF captures genuine capability-discriminative items rather than contamination artifacts, though the sample size ($N{=}33$) and the use of contamination gap as a proxy warrant caution in interpretation.\n\n%% ============================================================\n%% 5  ROBUSTNESS ANALYSES\n%% ============================================================\n\\section{Robustness and Sensitivity Analyses}\n\n\\subsection{Architecture-Stratified DIF}\n\\label{sec:archstrat}\n\nA natural concern is that DIF flags reflect architecture heterogeneity rather than temporal effects.\nWe restrict analysis to decoder-only models ($N{=}3{,}412$; reference: 891, focal: 523) and re-run MH DIF.\n\n\\begin{table}[h]\n\\centering\n\\caption{IRT fit and DIF rates: full population vs.\\ decoder-only subset.}\n\\label{tab:arch_strat}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & Full Population & Decoder-Only & $\\Delta$ & Threshold \\\\\n\\midrule\nRMSEA & 0.089 & 0.067 & $-0.022$ & ${<}0.05$ \\\\\nCFI   & 0.78  & 0.83  & $+0.05$  & ${\\geq}0.90$ \\\\\nTLI   & 0.75  & 0.81  & $+0.06$  & ${\\geq}0.90$ \\\\\nSRMR  & 0.074 & 0.058 & $-0.016$ & ${<}0.05$ \\\\\nC\\%   & 31.3\\% & 28.2\\% & $-3.1$pp & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nArchitecture stratification modestly reduces C\\% from 31.3\\% to 28.2\\% and improves IRT model fit (RMSEA: $0.089 \\to 0.067$), confirming that population heterogeneity contributes some spurious DIF.\nHowever, the improvement is modest: CFI remains below the 0.90 threshold, and 28.2\\% of items still show large DIF within a homogeneous architecture family.\nJaccard overlap between decoder-only and full-population DIF flags is 0.81, indicating the core finding is robust to architecture stratification.\n\nWe interpret the range [28.2\\%, 31.3\\%] as bounding the true C\\% under varying assumptions about population homogeneity.\n\n\\subsection{Item-Focused Trees}\n\\label{sec:ift}\n\nCategorical DIF uses an arbitrary binary temporal split (pre-2024 vs.\\ 2024-H1).\nItem-Focused Trees (IFT) treat model release date as a continuous covariate, allowing data-driven detection of split points and nonlinear DIF trajectories.\n\n\\begin{table}[h]\n\\centering\n\\caption{IFT vs.\\ categorical MH DIF comparison.}\n\\label{tab:ift}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Items Flagged & Unique Flags & Jaccard & Time (hrs) \\\\\n\\midrule\nCategorical MH & 31.3\\% & 12\\% & --- & 0.3 \\\\\nIFT (continuous) & 28.4\\% & 8\\% & 0.72 & 4.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIFT flags 28.4\\% of items (vs.\\ 31.3\\% categorical), with Jaccard overlap of 0.72.\nThe median data-driven split point is 2023-09-15, close to our pre-specified boundary.\n14\\% of flagged items show nonlinear DIF trajectories (e.g., U-shaped: early and late models struggle, middle cohort excels), warranting future investigation.\nThe continuous approach validates the binary split without substantially changing conclusions.\n\n\\subsection{Reasoning-RL Model Robustness}\n\\label{sec:rl_robust}\n\nReasoning-RL models (trained with GRPO/PPO for chain-of-thought) represent a qualitatively different training regime.\nWe test whether DIF analysis remains stable when 13 reasoning-RL models are added to the focal cohort alongside 477 alignment-RL models.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF vs.\\ traditional detectors under RL model inclusion.}\n\\label{tab:rl_robust}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nDetector & AUROC (SFT) & AUROC (Align-RL) & AUROC (Reason-RL) & $\\Delta$ & 95\\% CI \\\\\n\\midrule\nDIF (MH) & --- & --- & ret.=0.86 & $-0.14$ & [$-0.21$, $-0.07$] \\\\\nConStat & 0.72 & 0.69 & 0.54 & $-0.18$ & [$-0.31$, $-0.05$] \\\\\nMin-K\\% & 0.68 & 0.64 & 0.49 & $-0.19$ & [$-0.33$, $-0.06$] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDIF flag retention is 86\\% (Jaccard 0.83 between SFT-only and RL-augmented cohorts), indicating group-level DIF is relatively robust to RL model inclusion.\nTraditional per-model detectors degrade more sharply: ConStat AUROC drops from 0.72 to 0.54 and Min-K\\% from 0.68 to 0.49 on reasoning-RL models.\nHowever, with only $N{=}13$ reasoning-RL models, this comparison is statistically underpowered (DeLong test: $p{=}0.087$ for DIF vs.\\ ConStat; TOST equivalence: $p{=}0.11$).\nWe report this as preliminary evidence consistent with theoretical robustness predictions, not as a definitive claim.\n\n\\subsection{Graceful Degradation Under Item Replacement}\n\\label{sec:graceful}\n\nTo formalize the measurement redundancy finding from Section~\\ref{sec:diagnostic}, we progressively replace 5--50\\% of items and track validity metrics.\n\n\\begin{table}[h]\n\\centering\n\\caption{Validity metrics under progressive item replacement.}\n\\label{tab:graceful}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nReplacement \\% & Spearman $\\rho$ & Cronbach $\\alpha$ & Construct Coverage & Max Rank $\\Delta$ \\\\\n\\midrule\n0\\% (baseline) & 1.000 & 0.943 & 1.00 & 0 \\\\\n5\\% & 0.998 & 0.941 & 0.97 & 23 \\\\\n10\\% & 0.996 & 0.938 & 0.95 & 47 \\\\\n20\\% & 0.991 & 0.932 & 0.91 & 112 \\\\\n50\\% & 0.972 & 0.921 & 0.84 & 341 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEven at 50\\% replacement, $\\rho{=}0.972$---rankings are remarkably robust.\nThe empirical relationship $\\rho \\geq 1 - 1.3r$ (where $r$ is the replacement fraction) holds up to $r{=}0.4$.\nThe critical threshold where $\\rho$ drops below 0.98 is approximately 35\\%, close to the observed 38\\% DIF rate.\nDIF-targeted replacement produces $\\rho$ only 0.008 lower than random replacement, suggesting DIF items are not pathologically clustered.\n\nThis result cuts both ways: it validates the feasibility of item replacement (Section~\\ref{sec:bifactor}) but also shows that benchmark rankings are robust even without intervention.\nThe practical concern is measurement \\emph{efficiency}, not \\emph{validity}: 12{,}508 items contain substantial redundancy relative to the ranking information they provide.\n\n\\subsection{Cumulative Bayesian DIF Monitoring}\n\\label{sec:bayesian}\n\nSingle-administration DIF has limited power for medium-effect items ($\\delta{=}1.0$: power${=}0.41$).\nWe simulate a cumulative Bayesian DIF framework that accumulates evidence across successive benchmark administrations using informative priors.\n\n\\begin{table}[h]\n\\centering\n\\caption{Detection power by number of cumulative administrations and effect size.}\n\\label{tab:bayesian}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nAdministrations & $\\delta{=}0.8$ & $\\delta{=}1.0$ & $\\delta{=}1.2$ & $\\delta{=}1.4$ \\\\\n\\midrule\n1 & 0.24 & 0.41 & 0.55 & 0.68 \\\\\n2 & 0.37 & 0.54 & 0.69 & 0.81 \\\\\n3 & 0.48 & 0.67 & 0.79 & 0.89 \\\\\n4 & 0.54 & 0.74 & 0.84 & 0.92 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPower improves from 0.41 to 0.74 over four administrations for medium effects, with diminishing returns (gains: $+0.13$, $+0.13$, $+0.07$).\nFalse-positive rate remains controlled (0.042 $\\to$ 0.051) due to Bayesian shrinkage.\nAfter four administrations, 68\\% of items with Bayes factor ${>}3$ are detectable.\n\nThis analysis is simulation-based---longitudinal benchmark data with four temporal waves does not yet exist.\nWe position it as a concrete recommendation for benchmark maintainers: collecting response matrices over time enables cumulative evidence accumulation for item quality monitoring, an established psychometric practice~\\citep{sinharay2006bayesian} not yet adopted in LLM evaluation.\n\n%% ============================================================\n%% 6  COMPLEMENTARY DETECTION METHODS\n%% ============================================================\n\\section{Complementary Detection Baselines}\n\n\\subsection{ConStat Perturbation Testing}\n\\label{sec:constat}\n\nConStat-style perturbation testing~\\citep{dekoninck2024constat} operates at the per-model level by comparing performance on original vs.\\ semantically reformulated items.\nWe generate LLM-based reformulations for 248 MMLU items and test across 15 models.\n\n\\begin{table}[h]\n\\centering\n\\caption{ConStat detection rates by model training category.}\n\\label{tab:constat}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nModel Category & $N$ Models & Detection Rate (FDR=0.10) & Mean $d$ \\\\\n\\midrule\nSFT-only & 6 & 0.153 & 0.81 \\\\\nAlignment-RL (DPO) & 5 & 0.134 & 0.69 \\\\\nReasoning-RL (GRPO) & 4 & 0.071 & 0.42 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConStat detects surface-form sensitivity primarily in SFT and alignment-RL models (detection rate 13--15\\%, effect size $d{=}0.69$--$0.81$) but fails on reasoning-RL models (detection rate 7.1\\%, $d{=}0.42$), which generalize beyond verbatim patterns.\nAUROC against Li et al.\\ web-overlap labels is 0.61, consistent with the ground-truth mismatch discussed in Section~\\ref{sec:groundtruth}.\nAUROC on non-RL models (0.67) vs.\\ RL models (0.52) confirms ConStat detects a complementary signal to DIF: per-model surface-form memorization rather than cross-cohort differential functioning.\n\n\\subsection{Generation Variance Detection (DVD)}\n\\label{sec:dvd}\n\nDVD detects contamination via reduced generation variance: memorized items elicit consistently correct responses across temperature-varied generations.\nWe generate 50 responses per item ($T{=}0.8$) for 300 MMLU items across 12 open-weight models (62 GPU-hours).\n\n\\begin{table}[h]\n\\centering\n\\caption{DVD detection characteristics by contamination type.}\n\\label{tab:dvd}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nContamination Type & AUROC & Detection Rate ($\\tau{=}0.10$) & Mean Var.\\ Reduction \\\\\n\\midrule\nVerbatim & 0.71 & 0.134 & 0.21 \\\\\nVariant/Paraphrase & 0.63 & 0.072 & 0.12 \\\\\nNone (clean) & --- & 0.031 (FPR) & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDVD achieves moderate detection of verbatim contamination (AUROC 0.71) but weaker performance on paraphrase contamination (AUROC 0.63).\nCorrespondence with DIF flags is low (AUROC 0.58), reflecting fundamentally different signals: DIF measures cross-group differentials, DVD measures within-model consistency.\nThe 62 GPU-hour cost for 12 models on 300 items raises scalability concerns for full-benchmark deployment.\n\n\\subsection{Multi-Signal Ensemble}\n\\label{sec:ensemble}\n\nWe attempt to fuse DIF, ConStat, and DVD into a multi-signal ensemble via majority voting (2-of-3) and learned weighted fusion.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ensemble vs.\\ individual detector performance.}\n\\label{tab:ensemble}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & AUROC & Prec.@FPR=0.10 & Coverage \\\\\n\\midrule\nDIF (MH) & 0.62 & 0.38 & 31.3\\% \\\\\nConStat & 0.61 & 0.34 & 12.7\\% \\\\\nDVD & 0.58 & 0.29 & 9.4\\% \\\\\nEnsemble (2-of-3) & 0.66 & 0.41 & 6.8\\% \\\\\nEnsemble (weighted) & 0.66 & 0.43 & 8.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe ensemble yields only modest AUROC improvement ($0.66$ vs.\\ best individual $0.62$) because the three methods target orthogonal contamination mechanisms with limited overlap (pairwise coverage overlap: DIF--ConStat 31\\%, DIF--DVD 22\\%, ConStat--DVD 38\\%).\nCross-validation weight variance is high (0.15), indicating unstable calibration.\nWe report this as a \\emph{negative result}: ensemble approaches require partially redundant signals; when detection mechanisms are orthogonal, fusion provides minimal lift.\nThis negative result paradoxically supports our reframing: DIF measures something fundamentally different from per-model detectors, and combining them does not produce a unified contamination signal.\n\n%% ============================================================\n%% 7  TOWARD BENCHMARK REGENERATION\n%% ============================================================\n\\section{Pilot Studies: Benchmark Regeneration}\n\n\\subsection{Bifactor IRT Equating}\n\\label{sec:bifactor}\n\nWe fit a bifactor IRT model (one general factor + 57 subject-specific factors) to the METABENCH MMLU response matrix and attempt test equating via DIF-stable anchor items.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bifactor model fit indices.}\n\\label{tab:bifactor}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nIndex & Value & Acceptable & Good \\\\\n\\midrule\nRMSEA & 0.041 & ${<}0.08$ \\checkmark & ${<}0.05$ \\checkmark \\\\\nCFI   & 0.87  & ${\\geq}0.90$ \\texttimes & ${\\geq}0.95$ \\texttimes \\\\\nTLI   & 0.84  & ${\\geq}0.90$ \\texttimes & ${\\geq}0.95$ \\texttimes \\\\\nSRMR  & 0.063 & ${<}0.08$ \\checkmark & ${<}0.05$ \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe bifactor model converges after 847 iterations with acceptable RMSEA (0.041) but marginal CFI (0.87) and TLI (0.84).\nThe general factor explains 62\\% of variance; individual subjects contribute 14\\% on average.\nUsing 1{,}842 DIF-A anchor items, equated score correlation between original and replacement forms is $\\rho{=}0.93$---below the target $\\rho{\\geq}0.95$ due to replacement item calibration error (RMSE${=}0.38$).\nFixed-parameter calibration is acceptable for 68\\% of replacement items.\n\nWe conclude that IRT-based equating is \\emph{feasible in principle} but the marginal model fit and below-target equated correlation indicate that multidimensional IRT or domain-clustered approaches are needed for production-quality benchmark regeneration.\n\n\\subsection{LLM-Based Item Generation and Calibration}\n\\label{sec:calibration}\n\nWe generate 200 replacement items targeting DIF-flagged MMLU questions, using LLM generation with construct constraints and student-simulation calibration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Calibration method comparison for generated items.}\n\\label{tab:itemgen}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Difficulty $\\rho$ & Discrim.\\ $\\rho$ & \\% Within ${\\pm}0.5$ Target \\\\\n\\midrule\nPrompt-based targeting & 0.31 & 0.28 & 24\\% \\\\\nStudent sim.\\ (5 students) & 0.64 & 0.42 & 43\\% \\\\\nStudent sim.\\ (20 students) & 0.68 & 0.45 & 47\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStudent simulation substantially improves difficulty prediction ($\\rho{=}0.64$ with 5 students, $0.68$ with 20) over prompt-based targeting ($\\rho{=}0.31$).\nConstruct alignment is reasonable (78\\% human-rated), but holdout panel correlation is moderate (0.58), indicating limited transferability to unseen models.\nOnly 43\\% of items fall within ${\\pm}0.5$ difficulty of their targets, suggesting iterative recalibration would be needed.\nAt 187 GPU-hours for 200 items, cost remains a practical barrier to full-scale deployment.\nThese results indicate that LLM-based item generation is a viable but immature pipeline requiring human-in-the-loop validation for production use.\n\n%% ============================================================\n%% 8  DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{Measurement efficiency, not validity crisis.}\nThe central tension in our findings is that 38\\% of MMLU items are functionally unstable, yet removing them barely changes model rankings ($\\rho{\\approx}0.997$).\nWe resolve this by reframing: MMLU's 12{,}508 items contain massive measurement redundancy.\nThe stable subset suffices to preserve rankings, but the unstable items carry disproportionate discriminative information ($z{=}{-}8$ to ${-}49\\sigma$ vs.\\ random removal).\nThe practical implication is not ``MMLU is broken'' but ``MMLU could achieve equivalent measurement precision with fewer, better-characterized items''---a measurement efficiency problem.\n\n\\paragraph{The 38\\% figure: honest interpretation.}\nWe cannot decompose the 38\\% instability into contamination vs.\\ capability improvement.\nThe $\\rho{=}0.307$ correlation with domain accuracy gains suggests capability improvement is a substantial component.\nArchitecture stratification reduces C\\% to 28.2\\% (Section~\\ref{sec:archstrat}), providing a lower bound under controlled conditions.\nThe range [28\\%, 38\\%] represents our best estimate of temporal item instability under varying methodological assumptions.\n\n\\paragraph{Complementary detection landscape.}\nOur experiments with ConStat (Section~\\ref{sec:constat}), DVD (Section~\\ref{sec:dvd}), and ensemble fusion (Section~\\ref{sec:ensemble}) reveal that contamination detection methods target orthogonal mechanisms.\nDIF detects cross-cohort differential functioning; ConStat detects per-model surface-form sensitivity; DVD detects within-model generation consistency.\nThe negative ensemble result confirms these are fundamentally different signals, not noisy measurements of the same underlying phenomenon.\n\n\\paragraph{Semi-synthetic framework as portable contribution.}\nThe $\\Delta\\text{TPR}$/$\\Delta\\text{FPR}$ framework with cross-subject matching is agnostic to the underlying detector.\nAny item-level contamination detection method can be validated by injecting known differential contamination and measuring detection power increase.\nCross-benchmark replication (MMLU $\\to$ GSM8K) demonstrates portability.\nWe consider this the most immediately reusable contribution for the evaluation community.\n\n\\paragraph{Limitations.}\n(1)~Unidimensional IRT is a simplification for 57-subject MMLU; multidimensional models may reduce spurious DIF.\n(2)~Semi-synthetic injection uses a simplified contamination mechanism (incorrect$\\to$correct flipping); real contamination is more nuanced.\n(3)~GSM1K cross-validation uses $N{=}33$ models with wide confidence intervals; the anti-correlation is suggestive, not definitive.\n(4)~Reasoning-RL robustness analysis ($N{=}13$) is underpowered.\n(5)~Cumulative Bayesian DIF (Section~\\ref{sec:bayesian}) is simulation-only; real longitudinal data does not yet exist.\n(6)~Benchmark regeneration pilots (Sections~\\ref{sec:bifactor}--\\ref{sec:calibration}) demonstrate feasibility but not production readiness.\n\n%% ============================================================\n%% 9  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe present the first large-scale psychometric characterization of item-level behavioral drift in LLM benchmarks, analyzing 12{,}508 MMLU items across 5{,}227 models.\nOur DIF analysis reveals that 38\\% of items are functionally unstable across model generations---a mixture of capability improvement and differential item functioning that persists within all 57 subject domains.\nWe identify an underappreciated methodological gap in how the field validates contamination detectors and provide a semi-synthetic validation framework with cross-subject matching that eliminates false-positive inflation.\nThe framework generalizes across benchmarks (MMLU, GSM8K) and is applicable to any item-level detection method.\nFinally, we show that DIF serves as a diagnostic lens for benchmark quality: MMLU rankings are massively redundant, but unstable items concentrate discriminative signal, revealing a measurement efficiency problem that psychometric tools are well-suited to address.\n\n\\bibliography{references}\n\\bibliographystyle{plainnat}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02b9a6e5-fcce-4d74-a652-aedd22049030",
  "isSidechain": false,
  "requestId": "req_011CbEsgSWcmBZ9Q9dUH3PvR",
  "type": "assistant",
  "uuid": "479430dd-f6cc-4b80-9956-5940563a52ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015BNJdVwDVTKKLu1CFR7oT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 238,
      "cache_read_input_tokens": 41307,
      "output_tokens": 10046,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10046,
          "cache_read_input_tokens": 41307,
          "cache_creation_input_tokens": 238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 238
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

_source line 25 · 2026-05-21T01:53:28.727Z_

<details><summary>↩ Tool result · `toolu_019Q5LJXFf2CQTLUY6a2q61m`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "479430dd-f6cc-4b80-9956-5940563a52ab",
  "isSidechain": false,
  "promptId": "de177bb0-8153-4b40-a54f-7680d3583965",
  "type": "user",
  "uuid": "25988266-3af3-4f66-82e1-4c05889a5fe9",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/paper.tex",
    "content": "\\documentclass[10pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{natbib}\n\\usepackage[small]{caption}\n\n\\title{Psychometric Characterization of Item-Level Instability\\\\in LLM Benchmarks via Differential Item Functioning}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nLarge Language Model (LLM) benchmarks implicitly assume temporal score comparability: a score of 80\\% today should reflect the same latent ability as 80\\% one year ago.\nWe test this assumption by applying Differential Item Functioning (DIF) analysis---a classical psychometric method for detecting item-level behavioral anomalies---to the METABENCH response matrix (5{,}227 models $\\times$ 12{,}508 MMLU items).\nWe report three findings.\nFirst, 38\\% of MMLU items exhibit large DIF (ETS C category) between 2023 and 2024-H1 model cohorts, persisting within every subject domain (per-subject C\\%: 31--45\\%).\nThis instability reflects a mixture of genuine capability improvement ($\\rho{=}0.307$ with domain accuracy gains) and differential item functioning, and cannot be decomposed into a single cause.\nSecond, we identify an underappreciated methodological gap in contamination detection validation: web-overlap labels measure global item exposure, not differential functioning, producing expected enrichment ${\\approx}1.0$ against DIF flags.\nThird, we propose a semi-synthetic validation framework that injects controlled differential contamination into real response matrices; cross-subject matching eliminates false-positive inflation ($\\Delta\\text{FPR}{=}0.000$) while confirming detection power ($\\Delta\\text{TPR}{=}{+}0.508$ on MMLU, ${+}0.818$ on GSM8K).\nWe further show that MMLU exhibits massive measurement redundancy ($\\rho{\\approx}0.997$ after removing 31\\% of items), reframing the instability as a measurement efficiency problem rather than a validity crisis.\nCode and data will be released upon publication.\n\\end{abstract}\n\n%% ============================================================\n%% 1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nBenchmarks such as MMLU~\\citep{hendrycks2021mmlu} underpin comparative evaluation of LLMs.\nWhen practitioners report that ``Model B outperforms Model A by 5 points on MMLU,'' they implicitly assume both scores reflect the same latent construct measured under equivalent conditions.\nPsychometrics calls this assumption \\emph{measurement invariance}: the test functions identically across examinee populations.\n\nThis assumption is unlikely to hold in the LLM ecosystem, where models released months apart differ in training data composition, architecture, and optimization objective.\nIf a subset of items behaves differently across model generations---due to data contamination, capability shifts, or both---cross-temporal score comparisons carry uncontrolled item-level variance.\n\nWe bring Differential Item Functioning (DIF)---a family of methods developed over four decades in educational testing~\\citep{holland1993dif}---to characterize item-level behavioral drift in LLM benchmarks at unprecedented scale.\nApplying the Mantel--Haenszel (MH) procedure to the METABENCH response matrix (5{,}227 models $\\times$ 12{,}508 MMLU items), we find:\n\n\\begin{enumerate}\n\\item \\textbf{38\\% of MMLU items are functionally unstable} across model generations (ETS C category, $|\\Delta_\\text{MH}|{\\geq}1.5$). This persists within every subject domain (31--45\\% per subject) and is not a statistical artifact (random-split sanity check: 0.18\\%). The instability reflects a mixture of capability improvement and differential item functioning ($\\rho{=}0.307$ between C\\% and domain accuracy gains).\n\n\\item \\textbf{An underappreciated methodological gap} in contamination detection validation: web-overlap labels~\\citep{li2024contamination} measure whether items are publicly accessible---a global, model-agnostic property---rather than whether items function differently across cohorts. Enrichment ${\\approx}1.0$ between DIF flags and web-overlap labels is expected, not indicative of detector failure. Semi-synthetic injection confirms DIF's detection power ($\\Delta\\text{TPR}{=}{+}0.508$).\n\n\\item \\textbf{A reusable semi-synthetic validation framework} for any item-level contamination detector. By injecting known differential contamination into real response matrices and measuring $\\Delta\\text{TPR}$, the framework provides controlled evaluation infrastructure. Cross-subject matching eliminates matching-variable contamination ($\\Delta\\text{FPR}{=}0.000$), and the framework generalizes across benchmarks (GSM8K: $\\Delta\\text{TPR}{=}{+}0.818$).\n\n\\item \\textbf{DIF as diagnostic lens}: MMLU rankings exhibit massive measurement redundancy ($\\rho{\\approx}0.997$ after 31\\% item removal), but DIF items concentrate discriminative signal (removal causes more ranking disruption than random, $z{=}{-}8$ to ${-}49\\sigma$). Suggestive cross-benchmark evidence from GSM1K contamination gaps ($r{=}{-}0.478$, $p{=}0.005$, $N{=}33$) indicates DIF flags capture genuine capability differences rather than contamination artifacts.\n\\end{enumerate}\n\nWe additionally report extensive robustness analyses (architecture stratification, item-focused trees, RL-model sensitivity), complementary detection baselines (ConStat perturbation, generation variance), a negative result on multi-signal ensemble fusion, and pilot studies on benchmark regeneration via IRT equating and LLM-based item generation.\n\n%% ============================================================\n%% 2  BACKGROUND\n%% ============================================================\n\\section{Preliminaries: DIF for LLM Benchmarks}\n\n\\paragraph{Differential Item Functioning.}\nAn item exhibits DIF when examinees of equal ability from different groups have unequal probabilities of answering correctly.\nIn educational testing, groups are typically demographic (e.g., gender, ethnicity); we define groups \\emph{temporally}: a reference cohort (models released before 2024) and a focal cohort (models released 2024-H1).\n\n\\paragraph{Mantel--Haenszel procedure.}\nWe use the MH $\\chi^2$ test with ETS $\\Delta_\\text{MH}$ effect-size classification:\n\\textbf{A} (negligible, $|\\Delta_\\text{MH}|{<}1.0$),\n\\textbf{B} (moderate, $1.0{\\leq}|\\Delta_\\text{MH}|{<}1.5$), and\n\\textbf{C} (large, $|\\Delta_\\text{MH}|{\\geq}1.5$).\nItems are matched on total score to control for overall ability differences.\n\n\\paragraph{IRT context.}\nItem Response Theory (IRT) models item responses as a function of latent ability $\\theta$.\nA 2-parameter logistic (2PL) model specifies $P(X_{ij}{=}1|\\theta_j) = \\text{logistic}(a_i(\\theta_j - b_i))$, where $a_i$ is discrimination and $b_i$ is difficulty.\nDIF manifests as cross-group differences in item parameters.\nWe use IRT primarily for bifactor modeling and equating analyses (Sections~\\ref{sec:bifactor} and~\\ref{sec:calibration}).\n\n\\paragraph{Why DIF, not contamination detection?}\nContamination detectors (Min-K\\%, ConStat, n-gram overlap) answer: ``Is this model contaminated?''\nDIF answers a different question: ``Does this item function differently across model cohorts?''\nThis distinction is critical---DIF is a \\emph{characterization} tool for benchmark quality, not a per-model contamination detector.\n\n%% ============================================================\n%% 3  EXPERIMENTAL SETUP\n%% ============================================================\n\\section{Experimental Setup}\n\n\\paragraph{Data.}\nWe use the METABENCH response matrix~\\citep{metabench2024}: binary item responses for 5{,}227 models on 12{,}508 MMLU items across 57 subject domains.\nTemporal cohorts are defined by model release date: reference (pre-2024, $N_\\text{ref}{=}2{,}891$) and focal (2024-H1, $N_\\text{foc}{=}2{,}336$).\nFor cross-benchmark analyses, we additionally use METABENCH's GSM8K partition (1{,}319 items $\\times$ 6{,}702 models).\n\n\\paragraph{DIF analysis pipeline.}\nFor each of the 12{,}508 items, we compute the MH $\\Delta_\\text{MH}$ statistic using total score on remaining items as the matching variable.\nItems are classified into ETS A/B/C categories.\nWe define C\\% as the proportion of items in category C.\n\n\\paragraph{Semi-synthetic injection protocol.}\nTo validate detection power, we inject differential contamination by flipping incorrect$\\rightarrow$correct responses for randomly selected items in the focal cohort at controlled injection probabilities $p \\in \\{0.3, 0.5, 0.7, 1.0\\}$.\nDetection power is measured as $\\Delta\\text{TPR} = \\text{TPR}_\\text{injected} - \\text{TPR}_\\text{baseline}$.\n\n%% ============================================================\n%% 4  CORE FINDINGS\n%% ============================================================\n\\section{Core Findings}\n\n\\subsection{Item Instability Across Model Generations (Claim 1)}\n\\label{sec:instability}\n\nApplying MH DIF analysis to all 12{,}508 MMLU items yields C\\%${=}31.3$\\%, with 3{,}912 items exhibiting large differential functioning between temporal cohorts.\nWithin-subject analysis confirms this is not driven by cross-domain confounding: every one of 57 MMLU subjects shows C\\% between 31\\% and 45\\%, with a mean of 38.1\\%.\n\nA random-split sanity check (randomly assigning models to pseudo-cohorts regardless of release date) produces C\\%${=}0.18$\\%, confirming the temporal signal is not a statistical artifact.\n\n\\paragraph{Capability improvement confound.}\nThe correlation between per-subject C\\% and domain accuracy improvement is $\\rho{=}0.307$ ($p{=}0.02$), indicating that item instability is partially explained by models improving differentially across domains.\nWe emphasize that the 38\\% figure reflects a \\emph{mixture} of genuine capability improvement and differential item functioning---we cannot decompose these contributions with available data.\n\n\\subsection{Ground Truth Methodology Gap (Claim 2)}\n\\label{sec:groundtruth}\n\nWeb-overlap contamination labels~\\citep{li2024contamination} classify items as ``contaminated'' based on n-gram presence in Common Crawl.\nThese labels measure a \\emph{global} property (public accessibility) that applies nearly uniformly to MMLU items, which have been publicly available since 2020.\nDIF, by contrast, measures a \\emph{differential} property: whether an item functions differently across model cohorts.\n\nEmpirically, DIF flag enrichment against Li et al.\\ labels is ${\\approx}1.0$ (no enrichment).\nThis is expected when web-overlap labels lack item-level discriminative power for the quantity DIF measures.\nThis represents an underappreciated methodological gap: studies validating item-level contamination detectors against web-overlap labels are evaluating against a reference standard that cannot distinguish differentially-functioning items from stable ones.\n\nSemi-synthetic injection (Section~\\ref{sec:semisynthetic}) confirms DIF can detect differential contamination ($\\Delta\\text{TPR}{=}{+}0.508$ at injection probability $p{=}0.5$), demonstrating that the enrichment ${\\approx}1.0$ result reflects ground-truth limitations, not detector failure.\n\n\\subsection{Semi-Synthetic Validation Framework (Claim 3)}\n\\label{sec:semisynthetic}\n\nWe propose a reusable validation framework for item-level contamination detectors.\nThe key innovation is the matching variable: using total score on \\emph{other} subjects (cross-subject matching) rather than total score on the same subject (within-subject matching) as the MH conditioning variable.\n\n\\paragraph{Cross-subject matching eliminates FPR inflation.}\nWithin-subject matching suffers from matching-variable contamination: if injected items inflate total score on that subject, the matching variable is no longer a clean ability proxy.\nCross-subject matching avoids this because injection targets are restricted to one subject, while matching uses scores on the remaining 56.\nAcross all 5 tested subjects, cross-subject matching yields $\\Delta\\text{FPR}{=}0.000$, whereas within-subject matching produces FPR inflation of ${+}0.186$.\n\n\\paragraph{Detection power.}\nOn MMLU, $\\Delta\\text{TPR}{=}{+}0.508$ at $p{=}0.5$, with dose--response across injection probabilities ($p{=}0.3$: lower; $p{=}1.0$: higher).\nFour of five tested subjects show $\\Delta\\text{TPR}{>}0.3$.\n\n\\paragraph{Cross-benchmark replication.}\nOn GSM8K (1{,}319 items $\\times$ 6{,}702 models), the framework yields $\\Delta\\text{TPR}{=}{+}0.818$ (standard matching) and ${+}0.517$ (external matching), confirming portability to single-domain math benchmarks.\nGSM8K temporal DIF analysis independently reveals C\\%${=}18.9$\\%, lower than MMLU but non-trivial.\n\n\\subsection{DIF as Diagnostic Lens (Claim 4)}\n\\label{sec:diagnostic}\n\n\\paragraph{Measurement redundancy.}\nRemoving all 31\\% C-category DIF items and re-ranking models yields Spearman $\\rho{\\approx}0.997$ with the full-item ranking.\nThis extreme robustness reveals that MMLU contains massive measurement redundancy: the stable 69\\% of items suffice to preserve model ordering.\nWe reframe this as a \\emph{measurement efficiency} problem---MMLU uses 12{,}508 items where ${\\sim}8{,}600$ would produce equivalent rankings.\n\n\\paragraph{DIF items carry discriminative signal.}\nDespite ranking robustness, DIF item removal causes significantly \\emph{more} ranking disruption than random removal of the same number of items ($z{=}{-}8$ to ${-}49\\sigma$ across 21/21 conditions).\nDIF items exhibit $1.09\\times$ cross-cohort accuracy swing versus $0.96\\times$ for stable items---they concentrate the information that differentiates model generations.\n\n\\paragraph{Model-specific patterns.}\nDIF analysis reveals which models benefit most from unstable items: phi-3 and llama-3 families gain ${+}700$--$850$ ranks from DIF items, while mistral-merge models lose $-400$ to $-587$ ranks.\n\n\\paragraph{GSM1K cross-benchmark evidence (suggestive).}\nOn 33 matched models with GSM1K contamination gap data, DIF flags anti-correlate with contamination ($r{=}{-}0.478$, $p{=}0.005$; partial $r{=}{-}0.385$ controlling for accuracy; permutation $p{=}0.014$).\nModels with high contamination gaps (Phi, Gemma families) perform \\emph{worse} on DIF items.\nThis provides suggestive evidence that DIF captures genuine capability-discriminative items rather than contamination artifacts, though the sample size ($N{=}33$) and the use of contamination gap as a proxy warrant caution in interpretation.\n\n%% ============================================================\n%% 5  ROBUSTNESS ANALYSES\n%% ============================================================\n\\section{Robustness and Sensitivity Analyses}\n\n\\subsection{Architecture-Stratified DIF}\n\\label{sec:archstrat}\n\nA natural concern is that DIF flags reflect architecture heterogeneity rather than temporal effects.\nWe restrict analysis to decoder-only models ($N{=}3{,}412$; reference: 891, focal: 523) and re-run MH DIF.\n\n\\begin{table}[h]\n\\centering\n\\caption{IRT fit and DIF rates: full population vs.\\ decoder-only subset.}\n\\label{tab:arch_strat}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & Full Population & Decoder-Only & $\\Delta$ & Threshold \\\\\n\\midrule\nRMSEA & 0.089 & 0.067 & $-0.022$ & ${<}0.05$ \\\\\nCFI   & 0.78  & 0.83  & $+0.05$  & ${\\geq}0.90$ \\\\\nTLI   & 0.75  & 0.81  & $+0.06$  & ${\\geq}0.90$ \\\\\nSRMR  & 0.074 & 0.058 & $-0.016$ & ${<}0.05$ \\\\\nC\\%   & 31.3\\% & 28.2\\% & $-3.1$pp & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nArchitecture stratification modestly reduces C\\% from 31.3\\% to 28.2\\% and improves IRT model fit (RMSEA: $0.089 \\to 0.067$), confirming that population heterogeneity contributes some spurious DIF.\nHowever, the improvement is modest: CFI remains below the 0.90 threshold, and 28.2\\% of items still show large DIF within a homogeneous architecture family.\nJaccard overlap between decoder-only and full-population DIF flags is 0.81, indicating the core finding is robust to architecture stratification.\n\nWe interpret the range [28.2\\%, 31.3\\%] as bounding the true C\\% under varying assumptions about population homogeneity.\n\n\\subsection{Item-Focused Trees}\n\\label{sec:ift}\n\nCategorical DIF uses an arbitrary binary temporal split (pre-2024 vs.\\ 2024-H1).\nItem-Focused Trees (IFT) treat model release date as a continuous covariate, allowing data-driven detection of split points and nonlinear DIF trajectories.\n\n\\begin{table}[h]\n\\centering\n\\caption{IFT vs.\\ categorical MH DIF comparison.}\n\\label{tab:ift}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Items Flagged & Unique Flags & Jaccard & Time (hrs) \\\\\n\\midrule\nCategorical MH & 31.3\\% & 12\\% & --- & 0.3 \\\\\nIFT (continuous) & 28.4\\% & 8\\% & 0.72 & 4.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIFT flags 28.4\\% of items (vs.\\ 31.3\\% categorical), with Jaccard overlap of 0.72.\nThe median data-driven split point is 2023-09-15, close to our pre-specified boundary.\n14\\% of flagged items show nonlinear DIF trajectories (e.g., U-shaped: early and late models struggle, middle cohort excels), warranting future investigation.\nThe continuous approach validates the binary split without substantially changing conclusions.\n\n\\subsection{Reasoning-RL Model Robustness}\n\\label{sec:rl_robust}\n\nReasoning-RL models (trained with GRPO/PPO for chain-of-thought) represent a qualitatively different training regime.\nWe test whether DIF analysis remains stable when 13 reasoning-RL models are added to the focal cohort alongside 477 alignment-RL models.\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF vs.\\ traditional detectors under RL model inclusion.}\n\\label{tab:rl_robust}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nDetector & AUROC (SFT) & AUROC (Align-RL) & AUROC (Reason-RL) & $\\Delta$ & 95\\% CI \\\\\n\\midrule\nDIF (MH) & --- & --- & ret.=0.86 & $-0.14$ & [$-0.21$, $-0.07$] \\\\\nConStat & 0.72 & 0.69 & 0.54 & $-0.18$ & [$-0.31$, $-0.05$] \\\\\nMin-K\\% & 0.68 & 0.64 & 0.49 & $-0.19$ & [$-0.33$, $-0.06$] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDIF flag retention is 86\\% (Jaccard 0.83 between SFT-only and RL-augmented cohorts), indicating group-level DIF is relatively robust to RL model inclusion.\nTraditional per-model detectors degrade more sharply: ConStat AUROC drops from 0.72 to 0.54 and Min-K\\% from 0.68 to 0.49 on reasoning-RL models.\nHowever, with only $N{=}13$ reasoning-RL models, this comparison is statistically underpowered (DeLong test: $p{=}0.087$ for DIF vs.\\ ConStat; TOST equivalence: $p{=}0.11$).\nWe report this as preliminary evidence consistent with theoretical robustness predictions, not as a definitive claim.\n\n\\subsection{Graceful Degradation Under Item Replacement}\n\\label{sec:graceful}\n\nTo formalize the measurement redundancy finding from Section~\\ref{sec:diagnostic}, we progressively replace 5--50\\% of items and track validity metrics.\n\n\\begin{table}[h]\n\\centering\n\\caption{Validity metrics under progressive item replacement.}\n\\label{tab:graceful}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nReplacement \\% & Spearman $\\rho$ & Cronbach $\\alpha$ & Construct Coverage & Max Rank $\\Delta$ \\\\\n\\midrule\n0\\% (baseline) & 1.000 & 0.943 & 1.00 & 0 \\\\\n5\\% & 0.998 & 0.941 & 0.97 & 23 \\\\\n10\\% & 0.996 & 0.938 & 0.95 & 47 \\\\\n20\\% & 0.991 & 0.932 & 0.91 & 112 \\\\\n50\\% & 0.972 & 0.921 & 0.84 & 341 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEven at 50\\% replacement, $\\rho{=}0.972$---rankings are remarkably robust.\nThe empirical relationship $\\rho \\geq 1 - 1.3r$ (where $r$ is the replacement fraction) holds up to $r{=}0.4$.\nThe critical threshold where $\\rho$ drops below 0.98 is approximately 35\\%, close to the observed 38\\% DIF rate.\nDIF-targeted replacement produces $\\rho$ only 0.008 lower than random replacement, suggesting DIF items are not pathologically clustered.\n\nThis result cuts both ways: it validates the feasibility of item replacement (Section~\\ref{sec:bifactor}) but also shows that benchmark rankings are robust even without intervention.\nThe practical concern is measurement \\emph{efficiency}, not \\emph{validity}: 12{,}508 items contain substantial redundancy relative to the ranking information they provide.\n\n\\subsection{Cumulative Bayesian DIF Monitoring}\n\\label{sec:bayesian}\n\nSingle-administration DIF has limited power for medium-effect items ($\\delta{=}1.0$: power${=}0.41$).\nWe simulate a cumulative Bayesian DIF framework that accumulates evidence across successive benchmark administrations using informative priors.\n\n\\begin{table}[h]\n\\centering\n\\caption{Detection power by number of cumulative administrations and effect size.}\n\\label{tab:bayesian}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nAdministrations & $\\delta{=}0.8$ & $\\delta{=}1.0$ & $\\delta{=}1.2$ & $\\delta{=}1.4$ \\\\\n\\midrule\n1 & 0.24 & 0.41 & 0.55 & 0.68 \\\\\n2 & 0.37 & 0.54 & 0.69 & 0.81 \\\\\n3 & 0.48 & 0.67 & 0.79 & 0.89 \\\\\n4 & 0.54 & 0.74 & 0.84 & 0.92 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPower improves from 0.41 to 0.74 over four administrations for medium effects, with diminishing returns (gains: $+0.13$, $+0.13$, $+0.07$).\nFalse-positive rate remains controlled (0.042 $\\to$ 0.051) due to Bayesian shrinkage.\nAfter four administrations, 68\\% of items with Bayes factor ${>}3$ are detectable.\n\nThis analysis is simulation-based---longitudinal benchmark data with four temporal waves does not yet exist.\nWe position it as a concrete recommendation for benchmark maintainers: collecting response matrices over time enables cumulative evidence accumulation for item quality monitoring, an established psychometric practice~\\citep{sinharay2006bayesian} not yet adopted in LLM evaluation.\n\n%% ============================================================\n%% 6  COMPLEMENTARY DETECTION METHODS\n%% ============================================================\n\\section{Complementary Detection Baselines}\n\n\\subsection{ConStat Perturbation Testing}\n\\label{sec:constat}\n\nConStat-style perturbation testing~\\citep{dekoninck2024constat} operates at the per-model level by comparing performance on original vs.\\ semantically reformulated items.\nWe generate LLM-based reformulations for 248 MMLU items and test across 15 models.\n\n\\begin{table}[h]\n\\centering\n\\caption{ConStat detection rates by model training category.}\n\\label{tab:constat}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nModel Category & $N$ Models & Detection Rate (FDR=0.10) & Mean $d$ \\\\\n\\midrule\nSFT-only & 6 & 0.153 & 0.81 \\\\\nAlignment-RL (DPO) & 5 & 0.134 & 0.69 \\\\\nReasoning-RL (GRPO) & 4 & 0.071 & 0.42 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConStat detects surface-form sensitivity primarily in SFT and alignment-RL models (detection rate 13--15\\%, effect size $d{=}0.69$--$0.81$) but fails on reasoning-RL models (detection rate 7.1\\%, $d{=}0.42$), which generalize beyond verbatim patterns.\nAUROC against Li et al.\\ web-overlap labels is 0.61, consistent with the ground-truth mismatch discussed in Section~\\ref{sec:groundtruth}.\nAUROC on non-RL models (0.67) vs.\\ RL models (0.52) confirms ConStat detects a complementary signal to DIF: per-model surface-form memorization rather than cross-cohort differential functioning.\n\n\\subsection{Generation Variance Detection (DVD)}\n\\label{sec:dvd}\n\nDVD detects contamination via reduced generation variance: memorized items elicit consistently correct responses across temperature-varied generations.\nWe generate 50 responses per item ($T{=}0.8$) for 300 MMLU items across 12 open-weight models (62 GPU-hours).\n\n\\begin{table}[h]\n\\centering\n\\caption{DVD detection characteristics by contamination type.}\n\\label{tab:dvd}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nContamination Type & AUROC & Detection Rate ($\\tau{=}0.10$) & Mean Var.\\ Reduction \\\\\n\\midrule\nVerbatim & 0.71 & 0.134 & 0.21 \\\\\nVariant/Paraphrase & 0.63 & 0.072 & 0.12 \\\\\nNone (clean) & --- & 0.031 (FPR) & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDVD achieves moderate detection of verbatim contamination (AUROC 0.71) but weaker performance on paraphrase contamination (AUROC 0.63).\nCorrespondence with DIF flags is low (AUROC 0.58), reflecting fundamentally different signals: DIF measures cross-group differentials, DVD measures within-model consistency.\nThe 62 GPU-hour cost for 12 models on 300 items raises scalability concerns for full-benchmark deployment.\n\n\\subsection{Multi-Signal Ensemble}\n\\label{sec:ensemble}\n\nWe attempt to fuse DIF, ConStat, and DVD into a multi-signal ensemble via majority voting (2-of-3) and learned weighted fusion.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ensemble vs.\\ individual detector performance.}\n\\label{tab:ensemble}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & AUROC & Prec.@FPR=0.10 & Coverage \\\\\n\\midrule\nDIF (MH) & 0.62 & 0.38 & 31.3\\% \\\\\nConStat & 0.61 & 0.34 & 12.7\\% \\\\\nDVD & 0.58 & 0.29 & 9.4\\% \\\\\nEnsemble (2-of-3) & 0.66 & 0.41 & 6.8\\% \\\\\nEnsemble (weighted) & 0.66 & 0.43 & 8.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe ensemble yields only modest AUROC improvement ($0.66$ vs.\\ best individual $0.62$) because the three methods target orthogonal contamination mechanisms with limited overlap (pairwise coverage overlap: DIF--ConStat 31\\%, DIF--DVD 22\\%, ConStat--DVD 38\\%).\nCross-validation weight variance is high (0.15), indicating unstable calibration.\nWe report this as a \\emph{negative result}: ensemble approaches require partially redundant signals; when detection mechanisms are orthogonal, fusion provides minimal lift.\nThis negative result paradoxically supports our reframing: DIF measures something fundamentally different from per-model detectors, and combining them does not produce a unified contamination signal.\n\n%% ============================================================\n%% 7  TOWARD BENCHMARK REGENERATION\n%% ============================================================\n\\section{Pilot Studies: Benchmark Regeneration}\n\n\\subsection{Bifactor IRT Equating}\n\\label{sec:bifactor}\n\nWe fit a bifactor IRT model (one general factor + 57 subject-specific factors) to the METABENCH MMLU response matrix and attempt test equating via DIF-stable anchor items.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bifactor model fit indices.}\n\\label{tab:bifactor}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nIndex & Value & Acceptable & Good \\\\\n\\midrule\nRMSEA & 0.041 & ${<}0.08$ \\checkmark & ${<}0.05$ \\checkmark \\\\\nCFI   & 0.87  & ${\\geq}0.90$ \\texttimes & ${\\geq}0.95$ \\texttimes \\\\\nTLI   & 0.84  & ${\\geq}0.90$ \\texttimes & ${\\geq}0.95$ \\texttimes \\\\\nSRMR  & 0.063 & ${<}0.08$ \\checkmark & ${<}0.05$ \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe bifactor model converges after 847 iterations with acceptable RMSEA (0.041) but marginal CFI (0.87) and TLI (0.84).\nThe general factor explains 62\\% of variance; individual subjects contribute 14\\% on average.\nUsing 1{,}842 DIF-A anchor items, equated score correlation between original and replacement forms is $\\rho{=}0.93$---below the target $\\rho{\\geq}0.95$ due to replacement item calibration error (RMSE${=}0.38$).\nFixed-parameter calibration is acceptable for 68\\% of replacement items.\n\nWe conclude that IRT-based equating is \\emph{feasible in principle} but the marginal model fit and below-target equated correlation indicate that multidimensional IRT or domain-clustered approaches are needed for production-quality benchmark regeneration.\n\n\\subsection{LLM-Based Item Generation and Calibration}\n\\label{sec:calibration}\n\nWe generate 200 replacement items targeting DIF-flagged MMLU questions, using LLM generation with construct constraints and student-simulation calibration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Calibration method comparison for generated items.}\n\\label{tab:itemgen}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Difficulty $\\rho$ & Discrim.\\ $\\rho$ & \\% Within ${\\pm}0.5$ Target \\\\\n\\midrule\nPrompt-based targeting & 0.31 & 0.28 & 24\\% \\\\\nStudent sim.\\ (5 students) & 0.64 & 0.42 & 43\\% \\\\\nStudent sim.\\ (20 students) & 0.68 & 0.45 & 47\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStudent simulation substantially improves difficulty prediction ($\\rho{=}0.64$ with 5 students, $0.68$ with 20) over prompt-based targeting ($\\rho{=}0.31$).\nConstruct alignment is reasonable (78\\% human-rated), but holdout panel correlation is moderate (0.58), indicating limited transferability to unseen models.\nOnly 43\\% of items fall within ${\\pm}0.5$ difficulty of their targets, suggesting iterative recalibration would be needed.\nAt 187 GPU-hours for 200 items, cost remains a practical barrier to full-scale deployment.\nThese results indicate that LLM-based item generation is a viable but immature pipeline requiring human-in-the-loop validation for production use.\n\n%% ============================================================\n%% 8  DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{Measurement efficiency, not validity crisis.}\nThe central tension in our findings is that 38\\% of MMLU items are functionally unstable, yet removing them barely changes model rankings ($\\rho{\\approx}0.997$).\nWe resolve this by reframing: MMLU's 12{,}508 items contain massive measurement redundancy.\nThe stable subset suffices to preserve rankings, but the unstable items carry disproportionate discriminative information ($z{=}{-}8$ to ${-}49\\sigma$ vs.\\ random removal).\nThe practical implication is not ``MMLU is broken'' but ``MMLU could achieve equivalent measurement precision with fewer, better-characterized items''---a measurement efficiency problem.\n\n\\paragraph{The 38\\% figure: honest interpretation.}\nWe cannot decompose the 38\\% instability into contamination vs.\\ capability improvement.\nThe $\\rho{=}0.307$ correlation with domain accuracy gains suggests capability improvement is a substantial component.\nArchitecture stratification reduces C\\% to 28.2\\% (Section~\\ref{sec:archstrat}), providing a lower bound under controlled conditions.\nThe range [28\\%, 38\\%] represents our best estimate of temporal item instability under varying methodological assumptions.\n\n\\paragraph{Complementary detection landscape.}\nOur experiments with ConStat (Section~\\ref{sec:constat}), DVD (Section~\\ref{sec:dvd}), and ensemble fusion (Section~\\ref{sec:ensemble}) reveal that contamination detection methods target orthogonal mechanisms.\nDIF detects cross-cohort differential functioning; ConStat detects per-model surface-form sensitivity; DVD detects within-model generation consistency.\nThe negative ensemble result confirms these are fundamentally different signals, not noisy measurements of the same underlying phenomenon.\n\n\\paragraph{Semi-synthetic framework as portable contribution.}\nThe $\\Delta\\text{TPR}$/$\\Delta\\text{FPR}$ framework with cross-subject matching is agnostic to the underlying detector.\nAny item-level contamination detection method can be validated by injecting known differential contamination and measuring detection power increase.\nCross-benchmark replication (MMLU $\\to$ GSM8K) demonstrates portability.\nWe consider this the most immediately reusable contribution for the evaluation community.\n\n\\paragraph{Limitations.}\n(1)~Unidimensional IRT is a simplification for 57-subject MMLU; multidimensional models may reduce spurious DIF.\n(2)~Semi-synthetic injection uses a simplified contamination mechanism (incorrect$\\to$correct flipping); real contamination is more nuanced.\n(3)~GSM1K cross-validation uses $N{=}33$ models with wide confidence intervals; the anti-correlation is suggestive, not definitive.\n(4)~Reasoning-RL robustness analysis ($N{=}13$) is underpowered.\n(5)~Cumulative Bayesian DIF (Section~\\ref{sec:bayesian}) is simulation-only; real longitudinal data does not yet exist.\n(6)~Benchmark regeneration pilots (Sections~\\ref{sec:bifactor}--\\ref{sec:calibration}) demonstrate feasibility but not production readiness.\n\n%% ============================================================\n%% 9  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe present the first large-scale psychometric characterization of item-level behavioral drift in LLM benchmarks, analyzing 12{,}508 MMLU items across 5{,}227 models.\nOur DIF analysis reveals that 38\\% of items are functionally unstable across model generations---a mixture of capability improvement and differential item functioning that persists within all 57 subject domains.\nWe identify an underappreciated methodological gap in how the field validates contamination detectors and provide a semi-synthetic validation framework with cross-subject matching that eliminates false-positive inflation.\nThe framework generalizes across benchmarks (MMLU, GSM8K) and is applicable to any item-level detection method.\nFinally, we show that DIF serves as a diagnostic lens for benchmark quality: MMLU rankings are massively redundant, but unstable items concentrate discriminative signal, revealing a measurement efficiency problem that psychometric tools are well-suited to address.\n\n\\bibliography{references}\n\\bibliographystyle{plainnat}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "479430dd-f6cc-4b80-9956-5940563a52ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "25988266-3af3-4f66-82e1-4c05889a5fe9",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with IRT equated benchmark",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e"
}
```

---

### Assistant

_source line 28 · 2026-05-21T01:53:32.519Z_

Now let me compile it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25988266-3af3-4f66-82e1-4c05889a5fe9",
  "isSidechain": false,
  "requestId": "req_011CbEsxFRK1pvMQiBnmZCBw",
  "type": "assistant",
  "uuid": "13db08b3-3141-47e1-a288-b2fe8774f8ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gCgwipkNbhzdvayw2FxZj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10116,
      "cache_read_input_tokens": 41545,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10116,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 41545,
          "cache_creation_input_tokens": 10116,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10116
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

_source line 29 · 2026-05-21T01:53:35.600Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014WnJMRSgtfm4763TDjoEgv`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13db08b3-3141-47e1-a288-b2fe8774f8ba",
  "isSidechain": false,
  "requestId": "req_011CbEsxFRK1pvMQiBnmZCBw",
  "type": "assistant",
  "uuid": "d208a32d-1de4-49ca-897b-da63cbb81d07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gCgwipkNbhzdvayw2FxZj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10116,
      "cache_read_input_tokens": 41545,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10116,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 41545,
          "cache_creation_input_tokens": 10116,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10116
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

_source line 30 · 2026-05-21T01:53:37.422Z_

<details><summary>↩ Tool result · `toolu_014WnJMRSgtfm4763TDjoEgv`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
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

Package natbib Warning: Citation `hendrycks2021mmlu' on page 1 undefined on inp
ut line 40.


Package natbib Warning: Citation `holland1993dif' on page 1 undefined on input 
line 47.


Package natbib Warning: Citation `li2024contamination' on page 1 undefined on i
nput line 53.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Reference `sec:bifactor' on page 2 undefined on input line 82.


LaTeX Warning: Reference `sec:calibration' on page 2 undefined on input line 82
.


Package natbib Warning: Citation `metabench2024' on page 2 undefined on input l
ine 95.

[2]

Package natbib Warning: Citation `li2024contamination' on page 3 undefined on i
nput line 128.


LaTeX Warning: Reference `sec:semisynthetic' on page 3 undefined on input line 
136.


Overfull \hbox (27.8577pt too wide) in paragraph at lines 154--156
 []\OT1/cmr/bx/n/10 Cross-benchmark repli-ca-tion.[] \OT1/cmr/m/n/10 On GSM8K (
1,319 items $\OMS/cmsy/m/n/10 ^^B$ \OT1/cmr/m/n/10 6,702 mod-els), the frame-wo
rk yields $^^A[][][]0\OML/cmm/m/it/10 :\OT1/cmr/m/n/10 818$
[3]

LaTeX Warning: `h' float specifier changed to `ht'.

[4]

LaTeX Warning: Reference `sec:diagnostic' on page 5 undefined on input line 268
.


LaTeX Warning: Reference `sec:bifactor' on page 5 undefined on input line 293.

[5]

Package natbib Warning: Citation `sinharay2006bayesian' on page 6 undefined on 
input line 324.


Package natbib Warning: Citation `dekoninck2024constat' on page 6 undefined on 
input line 334.


LaTeX Warning: Reference `sec:groundtruth' on page 6 undefined on input line 35
4.


LaTeX Warning: `h' float specifier changed to `ht'.

[6] [7]

LaTeX Warning: Reference `sec:archstrat' on page 8 undefined on input line 486.



LaTeX Warning: Reference `sec:constat' on page 8 undefined on input line 490.


LaTeX Warning: Reference `sec:dvd' on page 8 undefined on input line 490.


LaTeX Warning: Reference `sec:ensemble' on page 8 undefined on input line 490.


LaTeX Warning: Reference `sec:bayesian' on page 8 undefined on input line 505.


LaTeX Warning: Reference `sec:bifactor' on page 8 undefined on input line 506.


LaTeX Warning: Reference `sec:calibration' on page 8 undefined on input line 50
6.


Overfull \hbox (32.19029pt too wide) in paragraph at lines 501--507
\OT1/cmr/m/n/10 may re-duce spu-ri-ous DIF. (2) Semi-synthetic in-jec-tion uses
 a sim-pli-fied con-tam-i-na-tion mech-a-nism (incorrect$\OMS/cmsy/m/n/10 !$\OT
1/cmr/m/n/10 correct
[8]
No file paper.bbl.

Package natbib Warning: There were undefined citations.

[9] (./paper.aux)
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm0900
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm0900
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm0900.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf
 Ok [100] [109] [98] [99] [108])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf
 Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]
[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]
[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]
[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]
[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]
[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]
[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf
 Ok [185] [178] [179] [170] [186])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf
 Ok [188] [189] [190]) ) ) )
(some charht values had to be adjusted by as much as 0.06744pt)
Font metrics written on tcrm0900.tfm.
Output written on tcrm0900.600gf (128 characters, 21392 bytes).
Transcript written on tcrm0900.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm0900.600pk: successfully generated.


LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm0900.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/symbols/msam10.pfb>
Output written on paper.pdf (9 pages, 234001 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `hendrycks2021mmlu' on page 1 undefined on inp
ut line 40.


Package natbib Warning: Citation `holland1993dif' on page 1 undefined on input 
line 47.


Package natbib Warning: Citation `li2024contamination' on page 1 undefined on i
nput line 53.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `metabench2024' on page 2 undefined on input l
ine 95.

[2]

Package natbib Warning: Citation `li2024contamination' on page 3 undefined on i
nput line 128.


Overfull \hbox (27.8577pt too wide) in paragraph at lines 154--156
 []\OT1/cmr/bx/n/10 Cross-benchmark repli-ca-tion.[] \OT1/cmr/m/n/10 On GSM8K (
1,319 items $\OMS/cmsy/m/n/10 ^^B$ \OT1/cmr/m/n/10 6,702 mod-els), the frame-wo
rk yields $^^A[][][]0\OML/cmm/m/it/10 :\OT1/cmr/m/n/10 818$
[3]

LaTeX Warning: `h' float specifier changed to `ht'.

[4] [5]

Package natbib Warning: Citation `sinharay2006bayesian' on page 6 undefined on 
input line 324.


Package natbib Warning: Citation `dekoninck2024constat' on page 6 undefined on 
input line 334.


LaTeX Warning: `h' float specifier changed to `ht'.

[6] [7]
Overfull \hbox (32.19029pt too wide) in paragraph at lines 501--507
\OT1/cmr/m/n/10 may re-duce spu-ri-ous DIF. (2) Semi-synthetic in-jec-tion uses
 a sim-pli-fied con-tam-i-na-tion mech-a-nism (incorrect$\OMS/cmsy/m/n/10 !$\OT
1/cmr/m/n/10 correct
[8]
No file paper.bbl.

Package natbib Warning: There were undefined citations.

[9] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm0900.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/symbols/msam10.pfb>
Output written on paper.pdf (9 pages, 236449 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d208a32d-1de4-49ca-897b-da63cbb81d07",
  "isSidechain": false,
  "promptId": "de177bb0-8153-4b40-a54f-7680d3583965",
  "type": "user",
  "uuid": "d82674a2-a7fc-42cb-8fe4-40ee982e6ab0",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `hendrycks2021mmlu' on page 1 undefined on inp\nut line 40.\n\n\nPackage natbib Warning: Citation `holland1993dif' on page 1 undefined on input \nline 47.\n\n\nPackage natbib Warning: Citation `li2024contamination' on page 1 undefined on i\nnput line 53.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Reference `sec:bifactor' on page 2 undefined on input line 82.\n\n\nLaTeX Warning: Reference `sec:calibration' on page 2 undefined on input line 82\n.\n\n\nPackage natbib Warning: Citation `metabench2024' on page 2 undefined on input l\nine 95.\n\n[2]\n\nPackage natbib Warning: Citation `li2024contamination' on page 3 undefined on i\nnput line 128.\n\n\nLaTeX Warning: Reference `sec:semisynthetic' on page 3 undefined on input line \n136.\n\n\nOverfull \\hbox (27.8577pt too wide) in paragraph at lines 154--156\n []\\OT1/cmr/bx/n/10 Cross-benchmark repli-ca-tion.[] \\OT1/cmr/m/n/10 On GSM8K (\n1,319 items $\\OMS/cmsy/m/n/10 ^^B$ \\OT1/cmr/m/n/10 6,702 mod-els), the frame-wo\nrk yields $^^A[][][]0\\OML/cmm/m/it/10 :\\OT1/cmr/m/n/10 818$\n[3]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\n\nLaTeX Warning: Reference `sec:diagnostic' on page 5 undefined on input line 268\n.\n\n\nLaTeX Warning: Reference `sec:bifactor' on page 5 undefined on input line 293.\n\n[5]\n\nPackage natbib Warning: Citation `sinharay2006bayesian' on page 6 undefined on \ninput line 324.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 6 undefined on \ninput line 334.\n\n\nLaTeX Warning: Reference `sec:groundtruth' on page 6 undefined on input line 35\n4.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6] [7]\n\nLaTeX Warning: Reference `sec:archstrat' on page 8 undefined on input line 486.\n\n\n\nLaTeX Warning: Reference `sec:constat' on page 8 undefined on input line 490.\n\n\nLaTeX Warning: Reference `sec:dvd' on page 8 undefined on input line 490.\n\n\nLaTeX Warning: Reference `sec:ensemble' on page 8 undefined on input line 490.\n\n\nLaTeX Warning: Reference `sec:bayesian' on page 8 undefined on input line 505.\n\n\nLaTeX Warning: Reference `sec:bifactor' on page 8 undefined on input line 506.\n\n\nLaTeX Warning: Reference `sec:calibration' on page 8 undefined on input line 50\n6.\n\n\nOverfull \\hbox (32.19029pt too wide) in paragraph at lines 501--507\n\\OT1/cmr/m/n/10 may re-duce spu-ri-ous DIF. (2) Semi-synthetic in-jec-tion uses\n a sim-pli-fied con-tam-i-na-tion mech-a-nism (incorrect$\\OMS/cmsy/m/n/10 !$\\OT\n1/cmr/m/n/10 correct\n[8]\nNo file paper.bbl.\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm0900\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm0900\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm0900.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf\n Ok [100] [109] [98] [99] [108])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf\n Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]\n[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]\n[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]\n[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]\n[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]\n[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]\n[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf\n Ok [185] [178] [179] [170] [186])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf\n Ok [188] [189] [190]) ) ) )\n(some charht values had to be adjusted by as much as 0.06744pt)\nFont metrics written on tcrm0900.tfm.\nOutput written on tcrm0900.600gf (128 characters, 21392 bytes).\nTranscript written on tcrm0900.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm0900.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm0900.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (9 pages, 234001 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `hendrycks2021mmlu' on page 1 undefined on inp\nut line 40.\n\n\nPackage natbib Warning: Citation `holland1993dif' on page 1 undefined on input \nline 47.\n\n\nPackage natbib Warning: Citation `li2024contamination' on page 1 undefined on i\nnput line 53.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `metabench2024' on page 2 undefined on input l\nine 95.\n\n[2]\n\nPackage natbib Warning: Citation `li2024contamination' on page 3 undefined on i\nnput line 128.\n\n\nOverfull \\hbox (27.8577pt too wide) in paragraph at lines 154--156\n []\\OT1/cmr/bx/n/10 Cross-benchmark repli-ca-tion.[] \\OT1/cmr/m/n/10 On GSM8K (\n1,319 items $\\OMS/cmsy/m/n/10 ^^B$ \\OT1/cmr/m/n/10 6,702 mod-els), the frame-wo\nrk yields $^^A[][][]0\\OML/cmm/m/it/10 :\\OT1/cmr/m/n/10 818$\n[3]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4] [5]\n\nPackage natbib Warning: Citation `sinharay2006bayesian' on page 6 undefined on \ninput line 324.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 6 undefined on \ninput line 334.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6] [7]\nOverfull \\hbox (32.19029pt too wide) in paragraph at lines 501--507\n\\OT1/cmr/m/n/10 may re-duce spu-ri-ous DIF. (2) Semi-synthetic in-jec-tion uses\n a sim-pli-fied con-tam-i-na-tion mech-a-nism (incorrect$\\OMS/cmsy/m/n/10 !$\\OT\n1/cmr/m/n/10 correct\n[8]\nNo file paper.bbl.\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm0900.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (9 pages, 236449 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d208a32d-1de4-49ca-897b-da63cbb81d07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-21T01:53:37.428Z_

```json
{
  "parentUuid": "d82674a2-a7fc-42cb-8fe4-40ee982e6ab0",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ab3f1d08-af57-4e1a-a04d-97f19cf4c962",
  "timestamp": "2026-05-21T01:53:37.428Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "ab3f1d08-af57-4e1a-a04d-97f19cf4c962",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with IRT equated benchmark",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e"
}
```

---

### Assistant

_source line 34 · 2026-05-21T01:53:43.027Z_

<details><summary>Logged reasoning block</summary>

```text
The paper compiled successfully to a 9-page PDF with only minor warnings (undefined citations since we don't have a .bbl file, and a couple of overfull hbox warnings). The paper is complete with all 10 experiments from experiment_data.json covered with their own sections and tables.

Let me verify the output file exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab3f1d08-af57-4e1a-a04d-97f19cf4c962",
  "isSidechain": false,
  "requestId": "req_011CbEsxtbDH9wSY93d3LVct",
  "type": "assistant",
  "uuid": "e07a0515-a869-43f6-a31b-83db596c7b66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZyskqPGvwK841J4AmnRWB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7955,
      "cache_read_input_tokens": 51661,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7955,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 470,
          "cache_read_input_tokens": 51661,
          "cache_creation_input_tokens": 7955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7955
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

_source line 35 · 2026-05-21T01:53:52.374Z_

Paper compiled successfully — 9 pages, all cross-references resolved on second pass. Only warnings are undefined citations (no .bbl file, expected for a dream paper) and two minor overfull hbox.

Output: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/paper.pdf` (236 KB, 9 pages).

All 10 experiments from `experiment_data.json` have dedicated sections with tables:
- Architecture-Stratified DIF (§5.1, Table 1)
- Item-Focused Trees (§5.2, Table 2)
- RL Robustness (§5.3, Table 3)
- Graceful Degradation (§5.4, Table 4)
- Cumulative Bayesian DIF (§5.5, Table 5)
- ConStat Perturbation (§6.1, Table 6)
- DVD Generation Variance (§6.2, Table 7)
- Ensemble Fusion (§6.3, Table 8)
- Bifactor IRT Equating (§7.1, Table 9)
- Item Generation Calibration (§7.2, Table 10)

Narrative guidance applied: Claim 2 uses "underappreciated methodological gap"; 38% explicitly caveated as mixture; ρ=0.997 reframed as measurement efficiency; GSM1K marked "suggestive evidence"; semi-synthetic framework positioned as most portable contribution.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e07a0515-a869-43f6-a31b-83db596c7b66",
  "isSidechain": false,
  "requestId": "req_011CbEsxtbDH9wSY93d3LVct",
  "type": "assistant",
  "uuid": "2641a5ed-71f3-4dd9-9209-02329352809d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZyskqPGvwK841J4AmnRWB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7955,
      "cache_read_input_tokens": 51661,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7955,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 470,
          "cache_read_input_tokens": 51661,
          "cache_creation_input_tokens": 7955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7955
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T012912 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "2641a5ed-71f3-4dd9-9209-02329352809d",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with IRT equated benchmark",
  "sessionId": "e38c2aaa-70a4-4ee4-9416-4e605591b62e"
}
```

---
