# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T165710 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/14e80fd9-a3f6-4ca0-91a9-233525c7cceb.jsonl`
- **Structured JSON:** [`c600edb9a2796fbc4c26.json`](../../sessions/c6/c600edb9a2796fbc4c26.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T17:17:40.153Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T17:17:40.153Z",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T165710 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：原始framing完全成立。三贡献清晰：(1) 首次大规模temporal measurement drift实证发现，6个benchmark一致性证实泛化性； (2) ground truth meta-critique改变领域对web-overlap验证的认知；(3) semi-synthetic + cross-subject matching作为可复用基础设施。 '31% instability robust to all controls'作为headline。DIF as diagnostic lens + audit protocol提供actionable价值。无需调整claims强度。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T17:17:40.157Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T17:17:40.157Z",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-21T17:17:40.177Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T165710 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：原始framing完全成立。三贡献清晰：(1) 首次大规模temporal measurement drift实证发现，6个benchmark一致性证实泛化性； (2) ground truth meta-critique改变领域对web-overlap验证的认知；(3) semi-synthetic + cross-subject matching作为可复用基础设施。 '31% instability robust to all controls'作为headline。DIF as diagnostic lens + audit protocol提供actionable价值。无需调整claims强度。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "fbb2aad3-deff-45fc-a21a-33870865ab9a",
  "type": "user",
  "uuid": "72fee4c4-de53-404e-aeb5-496dfbe2fe90",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T17:17:40.176Z_

```json
{
  "parentUuid": "72fee4c4-de53-404e-aeb5-496dfbe2fe90",
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
  "uuid": "87740cda-7a94-4a3a-8f39-67fc648c40cf",
  "timestamp": "2026-05-21T17:17:40.176Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T17:17:40.176Z_

```json
{
  "parentUuid": "87740cda-7a94-4a3a-8f39-67fc648c40cf",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "56ac63f9-8562-422d-91f8-20242748779e",
  "timestamp": "2026-05-21T17:17:40.176Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream_20260521T165710",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb"
}
```

---

### Assistant

_source line 7 · 2026-05-21T17:17:43.126Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56ac63f9-8562-422d-91f8-20242748779e",
  "isSidechain": false,
  "requestId": "req_011CbG6RpNrXja5mNCzBDvd4",
  "type": "assistant",
  "uuid": "69d506e7-14c3-4f08-a162-1c2b44493cf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgPKAC3FDmY2HRjTS1YUsV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12344,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12344,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12344
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

_source line 8 · 2026-05-21T17:17:44.089Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Yb6sfxh3RMXXMoXoNF1nat`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69d506e7-14c3-4f08-a162-1c2b44493cf5",
  "isSidechain": false,
  "requestId": "req_011CbG6RpNrXja5mNCzBDvd4",
  "type": "assistant",
  "uuid": "7faebecb-2270-4db4-98e2-79f117a04ef8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgPKAC3FDmY2HRjTS1YUsV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12344,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12344,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12344
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

_source line 9 · 2026-05-21T17:17:44.373Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TWkmy2KjCex4t9CdboZJZH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7faebecb-2270-4db4-98e2-79f117a04ef8",
  "isSidechain": false,
  "requestId": "req_011CbG6RpNrXja5mNCzBDvd4",
  "type": "assistant",
  "uuid": "24e005a0-0890-43c0-9897-1143bcc7fa19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgPKAC3FDmY2HRjTS1YUsV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12344,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12344,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12344
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

_source line 10 · 2026-05-21T17:17:44.383Z_

<details><summary>↩ Tool result · `toolu_01TWkmy2KjCex4t9CdboZJZH`</summary>

```text
1	# Paper Framing — irt_equated_bench_regen
2	
3	## Target Venue
4	- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)
5	- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)
6	
7	## Paper Type
8	Empirical analysis / psychometric characterization. Discovery paper, not methods paper. "DIF reveals benchmark structural problems," not "DIF detects contamination."
9	
10	## Core Claims (4 条, 可证伪)
11	
12	**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).
13	- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)
14	- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.
15	- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.
16	
17	**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).
18	- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)
19	- Framing: aggressive — "the field's standard validation approach is fundamentally mismatched for item-level detection" — now with direct empirical evidence, not just conceptual argument
20	
21	**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).
22	- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)
23	- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks
24	- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability
25	
26	**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:
27	1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.
28	2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies "items that changed across generations," not "good items."
29	3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not "find bad items and remove" but "understand what changed and why." Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.
30	4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.
31	- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)
32	- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.
33	- Growing Pains互补: "Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading"
34	- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed
35	
36	## Story Spine (v2 — no-pivot narrative)
37	
38	**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.
39	
40	**Key narrative principle**: "Instability ≠ invalidity." DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**
41	
42	**What we find** (4 contributions, focused):
43	
44	1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for "models got better."
45	
46	2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.
47	
48	3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.
49	
50	4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).
51	
52	**Headline result**: "Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance."
53	
54	## Scope Control (main body vs appendix)
55	
56	**MAIN BODY (4 claims + robustness)**:
57	- §1 Introduction (problem + "instability ≠ invalidity" framing upfront)
58	- §2 Related Work (45 papers, 5 clusters)
59	- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)
60	- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)
61	- §5 Discussion + Limitations
62	- §6 Conclusion
63	
64	**APPENDIX (pruned from main body)**:
65	- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped
66	- RL robustness (plan_002) — N=13, underpowered
67	- Ensemble fusion (plan_003a/b/c) — negative, not executed
68	- Bifactor equating pilot — below target fit
69	- Item generation pilot — below benchmarks
70	- Graceful degradation — clean but supplementary
71	- Item-Focused Trees — robustness check, supplementary
72	- ConStat/DVD comparisons — complementary baselines
73	
74	## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks
75	
76	Systematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.
77	
78	## Venue Fit
79	
80	- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. "Empirical, not algorithmic" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.
81	
82	## Novelty Articulation (三层，显式化)
83	
84	MH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:
85	
86	1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.
87	
88	2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).
89	
90	3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).
91	
92	**Framing**: "We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm."
93	
94	## Anticipated Reviewer Concerns (updated for pivot)
95	
96	1. **"31% could just mean models got better / ability confound inflates C%"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.
97	
98	2. **"Ground truth critique is obvious — of course web labels don't capture differential effects"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.
99	
100	3. **"Semi-synthetic injection is artificial"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.
101	
102	4. **"DIF power is only sufficient for large effects"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.
103	
104	5. **"Only validated on MMLU"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.
105	
106	6. **"Higher methods (MIMIC, propensity-score) could solve the confounding"** — Acknowledged as future work. We frame our three-attempt negative results as "empirical observation" that motivates these directions, not as impossibility.
107	
108	7. **"ETS threshold is uncalibrated for LLM populations"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: "finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF." Do NOT claim ">15% at all thresholds" — be honest that 2.5 drops below.
109	
110	8. **"Multiple testing: 12,508 simultaneous tests without correction"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.
111	
112	9. **"Only uniform DIF — non-uniform DIF plausible for LLMs"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: "our 31% uniform-only estimate is conservative."
113	
114	10. **"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.
115	
116	11. **"Ranking disruption result is tautological"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.
117	
118	## Dropped from Original Framing
119	
120	- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.
121	- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.
122	- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.
123	- **Detection as primary contribution**: Pivoted from "we detect contamination" to "we characterize benchmark properties."
124	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24e005a0-0890-43c0-9897-1143bcc7fa19",
  "isSidechain": false,
  "promptId": "fbb2aad3-deff-45fc-a21a-33870865ab9a",
  "type": "user",
  "uuid": "eed2fb88-260e-43c0-976f-5bdfe71e268b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n",
      "numLines": 124,
      "startLine": 1,
      "totalLines": 124
    }
  },
  "sourceToolAssistantUUID": "24e005a0-0890-43c0-9897-1143bcc7fa19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T17:17:44.463Z_

<details><summary>↩ Tool result · `toolu_01Yb6sfxh3RMXXMoXoNF1nat`</summary>

```text
1	[
2	  {
3	    "name": "real_data_dif_mmlu",
4	    "description": "METABENCH MMLU response matrix (5,219 models × 12,508 items) 上的全量DIF分析。 temporal cohort (2023 vs 2024-H1)、ability-quintile split、within-family confound control、domain-specificity分析。\n",
5	    "results": {
6	      "temporal_ets_c_pct": 31.3,
7	      "temporal_fpr_li_clean": 0.318,
8	      "temporal_enrichment": 0.96,
9	      "ability_ets_c_pct": 2.9,
10	      "ability_enrichment": 1.19,
11	      "within_family_llama2v3_c_pct": 61.3,
12	      "within_family_mistral_mixtral_c_pct": 38.7,
13	      "domain_spearman_rho": 0.307,
14	      "domain_spearman_p": 0.02,
15	      "sanity_random_split_c_pct": 0.18,
16	      "temporal_ability_jaccard": 0.014,
17	      "n_models_temporal_ref": 1080,
18	      "n_models_temporal_foc": 807,
19	      "n_items": 12508,
20	      "domain_specificity_c_range": "20.7–48.4%",
21	      "domain_specificity_mean": 30.6,
22	      "negative_disc_items_pct": 15.4,
23	      "negative_disc_sensitivity": "C% changes <0.5pp with/without negative-disc items"
24	    },
25	    "tables": [
26	      {
27	        "name": "Table 1: Temporal DIF Summary (ETS C Classification)",
28	        "columns": [
29	          "cohort_definition",
30	          "n_ref",
31	          "n_foc",
32	          "n_items",
33	          "pct_A",
34	          "pct_B",
35	          "pct_C",
36	          "enrichment_li",
37	          "random_sanity_c_pct"
38	        ],
39	        "rows": [
40	          [
41	            "temporal_2023v2024",
42	            1080,
43	            807,
44	            12508,
45	            52.4,
46	            16.3,
47	            31.3,
48	            0.96,
49	            0.18
50	          ],
51	          [
52	            "ability_quintile",
53	            1044,
54	            1044,
55	            12508,
56	            85.2,
57	            11.9,
58	            2.9,
59	            1.19,
60	            0.15
61	          ],
62	          [
63	            "within_family_llama",
64	            161,
65	            308,
66	            12508,
67	            24.1,
68	            14.6,
69	            61.3,
70	            0.91,
71	            0.22
72	          ]
73	        ]
74	      },
75	      {
76	        "name": "Table 2: Domain-Specificity Top/Bottom 5 Subjects by C%",
77	        "columns": [
78	          "subject",
79	          "n_items",
80	          "pct_c",
81	          "pct_favor_2024"
82	        ],
83	        "rows": [
84	          [
85	            "business_ethics",
86	            100,
87	            48.4,
88	            39.6
89	          ],
90	          [
91	            "human_aging",
92	            223,
93	            41.9,
94	            38.7
95	          ],
96	          [
97	            "formal_logic",
98	            126,
99	            40.4,
100	            42.1
101	          ],
102	          [
103	            "management",
104	            103,
105	            21.7,
106	            44.2
107	          ],
108	          [
109	            "computer_security",
110	            100,
111	            20.7,
112	            47.3
113	          ]
114	        ]
115	      }
116	    ],
117	    "figures": [],
118	    "analysis": "31.3%作为primary estimate稳固。ability split的2.9%与temporal的31.3%形成鲜明对比， 直接排除\"models got better → inflated DIF\"的解释。within-family结果(61.3%) 虽然高，但因Llama-2v3能力差距极大(d=-0.99)，plan_027的matching分析已将genuine item-level DIF 锁定在~28-29%。domain分析的ρ=0.307(p=0.02)是honest reporting——plan_019的item-level decomposition将其降至≤2.4pp(7.6%)，是paper的关键robustness支撑。\n\n\nbest档下temporal cohort的31.3% C%是核心headline数字，已被多层robustness control确认。 random split 0.18%证明非统计伪影。enrichment≈0.96与Li et al.标签的理论预期一致—— web-overlap是global exposure指标，DIF检测differential functioning，二者正交，enrichment≈1.0是预期结果。 ability split仅2.9%说明DIF确实捕获temporal信号而非能力差异。within-family Llama-2v3的61.3% 反映两代间巨大能力跳跃(d=-0.99)中的genuine item-level变化，而非伪影。domain相关ρ=0.307 表明domain improvement有modest贡献但非主因——plan_019/plan_030进一步量化为≤7.6%。\n"
119	  },
120	  {
121	    "name": "rl_robustness_validation",
122	    "description": "验证DIF对reasoning-RL模型的鲁棒性。三组对比：SFT-only baseline、alignment-RL(DPO/ORPO, N=477)、 reasoning-RL(10-15个GRPO/PPO模型注入focal cohort)。DIF group-level稳定性 vs 传统detector model-level退化。\n",
123	    "results": {
124	      "n_reasoning_rl_models": 13,
125	      "reasoning_rl_models_list": "DeepSeek-R1-7B, DeepSeek-R1-32B, Qwen2.5-RL-7B, Qwen2.5-RL-14B, Qwen2.5-RL-32B, Marco-o1-7B, Skywork-OR1-8B, OpenThinker-7B, OpenThinker-32B, s1-32B, STILL-2-7B, Light-R1-7B, Bespoke-Stratos-7B",
126	      "sft_baseline_c_pct": 31.3,
127	      "alignment_rl_cohort_c_pct": 31.1,
128	      "reasoning_rl_mixed_cohort_c_pct": 30.8,
129	      "jaccard_sft_vs_alignment_rl": 0.94,
130	      "jaccard_sft_vs_reasoning_rl_mixed": 0.92,
131	      "jaccard_alignment_vs_reasoning_rl": 0.93,
132	      "dif_flag_retention_rate": 0.95,
133	      "bootstrap_ci_jaccard_sft_vs_rl": [
134	        0.9,
135	        0.96
136	      ],
137	      "tost_equivalence_p": 0.003,
138	      "tost_equivalence_margin": 0.05,
139	      "traditional_mink_auroc_sft": 0.72,
140	      "traditional_mink_auroc_rl": 0.48,
141	      "traditional_constat_auroc_sft": 0.68,
142	      "traditional_constat_auroc_rl": 0.51,
143	      "auroc_drop_mink": 0.24,
144	      "auroc_drop_constat": 0.17,
145	      "delong_mink_p": 0.001,
146	      "delong_constat_p": 0.008,
147	      "partial_exploitation_power": {
148	        "p_04": {
149	          "dif_tpr": 0.42,
150	          "mink_auroc": 0.39
151	        },
152	        "p_06": {
153	          "dif_tpr": 0.61,
154	          "mink_auroc": 0.44
155	        },
156	        "p_08": {
157	          "dif_tpr": 0.78,
158	          "mink_auroc": 0.46
159	        },
160	        "p_10": {
161	          "dif_tpr": 0.91,
162	          "mink_auroc": 0.48
163	        }
164	      }
165	    },
166	    "tables": [
167	      {
168	        "name": "Table: DIF Stability Across Training Paradigms",
169	        "columns": [
170	          "cohort_composition",
171	          "n_foc",
172	          "c_pct",
173	          "jaccard_vs_sft",
174	          "bootstrap_ci_95"
175	        ],
176	        "rows": [
177	          [
178	            "SFT-only (baseline)",
179	            807,
180	            31.3,
181	            "—",
182	            "—"
183	          ],
184	          [
185	            "Alignment-RL (DPO/ORPO)",
186	            477,
187	            31.1,
188	            0.94,
189	            "[0.92, 0.96]"
190	          ],
191	          [
192	            "SFT+Reasoning-RL mixed",
193	            820,
194	            30.8,
195	            0.92,
196	            "[0.90, 0.96]"
197	          ]
198	        ]
199	      },
200	      {
201	        "name": "Table: Traditional Detector Degradation on Reasoning-RL",
202	        "columns": [
203	          "detector",
204	          "auroc_sft",
205	          "auroc_rl",
206	          "delta_auroc",
207	          "delong_p"
208	        ],
209	        "rows": [
210	          [
211	            "Min-K%",
212	            0.72,
213	            0.48,
214	            -0.24,
215	            0.001
216	          ],
217	          [
218	            "ConStat",
219	            0.68,
220	            0.51,
221	            -0.17,
222	            0.008
223	          ],
224	          [
225	            "DIF (group)",
226	            "—",
227	            "—",
228	            "Jaccard=0.92",
229	            "TOST p=0.003"
230	          ]
231	        ]
232	      }
233	    ],
234	    "figures": [],
235	    "analysis": "best档核心结论：DIF的group-level design天然免疫于RL训练对individual model信号的扰动。 13个RL模型虽少但足够——DIF不需要N≥80个RL模型，只需focal cohort total N≥80且RL模型 混入后不改变group-level pattern。Jaccard=0.92超过0.90阈值，TOST正式排除degradation。 传统detector的0.17-0.24 AUROC drop提供鲜明对比，强化DIF的methodological advantage叙事。 Caveat: N=13 reasoning-RL仍然underpowered for standalone claim，但作为robustness check足够。\n\n\nbest档下Jaccard≥0.90是关键指标。DIF是group-level方法，将13个RL模型加入807个focal cohort (占比1.6%)对MH统计量的影响微乎其微——MH条件化total score后，RL模型的memorization pattern 被ability matching吸收。C%从31.3%微降至30.8%是噪声范围内的正常波动。 传统detector的AUROC下降0.17-0.24反映Wang et al.论证的NLL gap contraction机制： GRPO/PPO训练使模型对所有选项的logit分布更平坦，破坏了Min-K%和ConStat依赖的 per-token surprise信号，但不影响DIF的item-level binary response pattern。 TOST equivalence test (margin=0.05, p=0.003)正式确认DIF retention非空结果。\n"
236	  },
237	  {
238	    "name": "constat_perturbation_eval",
239	    "description": "ConStat-style perturbation testing独立评估：200+ MMLU items的LLM paraphrase生成、 原始vs重述性能对比、FDR-controlled detection、RL vs non-RL检测力对比。\n",
240	    "results": {
241	      "n_items_paraphrased": 250,
242	      "n_models_tested": 50,
243	      "constat_detection_rate_non_rl": 0.38,
244	      "constat_detection_rate_alignment_rl": 0.31,
245	      "constat_detection_rate_reasoning_rl": 0.14,
246	      "fdr_threshold": 0.05,
247	      "constat_fpr": 0.048,
248	      "constat_tpr_delta_ge_06": 0.62,
249	      "constat_tpr_delta_ge_10": 0.41,
250	      "paraphrase_quality_semantic_sim": 0.91,
251	      "paraphrase_quality_difficulty_corr": 0.83,
252	      "rl_sensitivity_ratio": 0.37
253	    },
254	    "tables": [
255	      {
256	        "name": "Table: ConStat Detection Power by Training Paradigm",
257	        "columns": [
258	          "paradigm",
259	          "n_models",
260	          "detection_rate",
261	          "fpr",
262	          "effect_size_threshold"
263	        ],
264	        "rows": [
265	          [
266	            "SFT-only",
267	            25,
268	            0.38,
269	            0.048,
270	            "δ≥0.6"
271	          ],
272	          [
273	            "Alignment-RL",
274	            15,
275	            0.31,
276	            0.045,
277	            "δ≥0.6"
278	          ],
279	          [
280	            "Reasoning-RL",
281	            10,
282	            0.14,
283	            0.051,
284	            "δ≥0.6"
285	          ]
286	        ]
287	      }
288	    ],
289	    "figures": [],
290	    "analysis": "ConStat的RL-sensitivity确认了DIF的structural advantage：DIF条件化ability后检测 item-level differential functioning，不依赖per-model perturbation response差异。 ConStat适合non-RL场景，DIF适合所有场景。此结果支撑\"DIF as primary, ConStat as complementary\"叙事。 但因paper已决定不执行此实验(scope control)，此数据仅作appendix/future work参考。\n\n\nbest档下ConStat在non-RL模型上表现中等(detection rate 38%)，因为perturbation testing 依赖模型对original vs paraphrased的response差异——contaminated模型在original上表现异常好。 但reasoning-RL模型通过GRPO训练泛化了problem-solving能力(非verbatim memorization)， 使original vs paraphrased差异消失，detection rate降至14%。这为ensemble论证(DIF covers where ConStat fails)提供直接证据。FPR在0.05 FDR控制下保持在0.048。 注意：此实验在paper framing中已标记为\"never executed, future work\"，best档下执行它 是为了提供完整的baseline comparison数据。\n"
291	  },
292	  {
293	    "name": "dvd_generation_variance_eval",
294	    "description": "DVD generation variance独立评估：10-15个开源模型、每item 50次temperature sampling、 generation variance score计算、bimodal分布检测。\n",
295	    "results": {
296	      "n_models": 12,
297	      "n_items_sampled": 500,
298	      "temperature": 0.8,
299	      "n_generations_per_item": 50,
300	      "dvd_detection_rate_verbatim": 0.22,
301	      "dvd_detection_rate_variant": 0.45,
302	      "dvd_fpr": 0.065,
303	      "bimodal_detection_rate": 0.33,
304	      "dvd_auroc_verbatim": 0.61,
305	      "dvd_auroc_variant": 0.74,
306	      "compute_hours": 68
307	    },
308	    "tables": [
309	      {
310	        "name": "Table: DVD Detection Power by Contamination Type",
311	        "columns": [
312	          "contamination_type",
313	          "auroc",
314	          "detection_rate",
315	          "fpr"
316	        ],
317	        "rows": [
318	          [
319	            "verbatim",
320	            0.61,
321	            0.22,
322	            0.065
323	          ],
324	          [
325	            "variant",
326	            0.74,
327	            0.45,
328	            0.065
329	          ],
330	          [
331	            "none (clean)",
332	            "—",
333	            "—",
334	            0.065
335	          ]
336	        ]
337	      }
338	    ],
339	    "figures": [],
340	    "analysis": "DVD填补DIF和ConStat的variant contamination检测空白。但GPU cost (68h)和detection rate 均不及DIF的zero-GPU设计。此实验与plan_003a一样在paper scope外(never executed)， best档下执行是为ensemble fusion提供完整输入。\n\n\nbest档下DVD对variant contamination (非verbatim、通过paraphrase传播的)检测力最强(AUROC=0.74)， 因为variant contamination导致模型在某些generation中复现memorized pattern、其他时候正常推理， 产生bimodal variance signature。对verbatim contamination反而较弱(AUROC=0.61)， 因为verbatim memorization导致consistently correct response，variance反而低。 这与DIF(检测任何形式的differential functioning)和ConStat(检测perturbation sensitivity) 形成互补覆盖。FPR 0.065略高于理想值但可接受。\n"
341	  },
342	  {
343	    "name": "ensemble_fusion",
344	    "description": "DIF + ConStat + DVD三信号融合：threshold校准、2-of-3 majority voting、weighted fusion、 ensemble覆盖分析、5-fold交叉验证。\n",
345	    "results": {
346	      "ensemble_fpr_majority": 0.032,
347	      "ensemble_fpr_weighted": 0.028,
348	      "ensemble_tpr_majority_delta_14": 0.78,
349	      "ensemble_tpr_weighted_delta_14": 0.82,
350	      "coverage_dif_only": "δ≥1.4, all training types",
351	      "coverage_constat_only": "δ≥0.6, non-RL only",
352	      "coverage_dvd_only": "variant contamination",
353	      "coverage_ensemble": "δ≥0.6, all types including variant",
354	      "cv_weight_dif": 0.52,
355	      "cv_weight_constat": 0.28,
356	      "cv_weight_dvd": 0.2,
357	      "uniform_vs_optimized_auc_gap": 0.03
358	    },
359	    "tables": [
360	      {
361	        "name": "Table: Ensemble vs Individual Detector Performance",
362	        "columns": [
363	          "method",
364	          "tpr_at_fpr_05",
365	          "auroc",
366	          "coverage_type"
367	        ],
368	        "rows": [
369	          [
370	            "DIF (MH)",
371	            0.68,
372	            0.87,
373	            "group-level, all paradigms"
374	          ],
375	          [
376	            "ConStat",
377	            0.55,
378	            0.76,
379	            "model-level, non-RL"
380	          ],
381	          [
382	            "DVD",
383	            0.42,
384	            0.71,
385	            "model-level, variant"
386	          ],
387	          [
388	            "Ensemble (majority)",
389	            0.78,
390	            0.91,
391	            "all"
392	          ],
393	          [
394	            "Ensemble (weighted)",
395	            0.82,
396	            0.93,
397	            "all"
398	          ]
399	        ]
400	      }
401	    ],
402	    "figures": [],
403	    "analysis": "Ensemble在best档下表现优异但对paper叙事非必要——DIF standalone已足够支撑三贡献结构。 此结果作为future work方向：若DIF + ConStat + DVD三线融合被证实，可升级为独立contribution。 当前paper wisely将此降为appendix/dropped。\n\n\nbest档下ensemble的FPR<0.05(远低于0.10阈值)因为2-of-3 majority voting天然抑制 single-signal false positives。TPR=0.82(weighted)超过任何单一信号因为三个detector 覆盖不同contamination机制。DIF权重最高(0.52)反映其跨training-paradigm的一致性。 uniform vs optimized差距仅0.03 AUC说明fusion对权重不敏感。 但此实验依赖plan_003a/b，且paper已明确dropped ensemble contribution。 best档下这是最佳情况的appendix material。\n"
404	  },
405	  {
406	    "name": "cross_benchmark_gsm8k",
407	    "description": "GSM8K上的DIF复制分析：temporal cohort DIF、semi-synthetic validation、GSM1K correlation。\n",
408	    "results": {
409	      "step1_gsm8k_temporal_c_pct": 18.9,
410	      "step1_n_items": 1319,
411	      "step1_n_ref": 1017,
412	      "step1_n_foc": 804,
413	      "step1_sanity_c_pct": 0.3,
414	      "step1_standard_external_spearman": 0.926,
415	      "step2_standard_delta_tpr_p10": 0.818,
416	      "step2_external_delta_tpr_p10": 0.517,
417	      "step3_n_models": 33,
418	      "step3_pearson_r": -0.478,
419	      "step3_pearson_p": 0.005,
420	      "step3_spearman_rho": -0.403,
421	      "step3_partial_r": -0.385,
422	      "step3_direction": "NEGATIVE (opposite to contamination hypothesis)",
423	      "step3_robust_leave_one_out": true
424	    },
425	    "tables": [
426	      {
427	        "name": "Table: GSM8K Three-Step Validation",
428	        "columns": [
429	          "step",
430	          "metric",
431	          "value",
432	          "interpretation"
433	        ],
434	        "rows": [
435	          [
436	            "Step 1",
437	            "temporal_c_pct",
438	            "18.9%",
439	            "Lower than MMLU, consistent with single-domain"
440	          ],
441	          [
442	            "Step 1",
443	            "sanity_c_pct",
444	            "0.3%",
445	            "Well below temporal signal"
446	          ],
447	          [
448	            "Step 2",
449	            "delta_tpr_p10",
450	            "+0.818",
451	            "Framework portable to math benchmark"
452	          ],
453	          [
454	            "Step 3",
455	            "pearson_r",
456	            -0.478,
457	            "DIF ≠ contamination on GSM8K"
458	          ]
459	        ]
460	      }
461	    ],
462	    "figures": [],
463	    "analysis": "GSM8K结果在best档下完美服务于paper的reframed叙事：DIF是diagnostic tool而非contamination detector。 r=-0.478的negative correlation被明确demote为exploratory(N=33, CI wide)，不进入abstract/conclusion。 semi-synthetic ΔTPR=+0.818是Claim 3(framework)的cross-benchmark replication支撑。\n\n\nbest档下GSM8K C%=18.9%低于MMLU的31.3%，因为GSM8K是单domain数学benchmark， items间能力维度同质性更高，DIF更多反映genuine capability gain而非item-specific instability。 semi-synthetic ΔTPR=+0.818(标准matching)证明framework可移植性——GSM8K的单domain结构 使matching variable(total score)与target items共线性更强，但仍能检测injected contamination。 GSM1K correlation r=-0.478(negative)是关键finding：DIF flags与contamination gap 反向关联，说明DIF在GSM8K上捕获的不是contamination而是capability-driven item functioning变化。 这是honest reporting——不利于\"DIF detects contamination\"叙事，但完美支撑\"DIF as diagnostic lens\" reframing。best档下此negative result被视为strength而非weakness。\n"
464	  },
465	  {
466	    "name": "bifactor_irt_equating_pilot",
467	    "description": "MMLU上的bifactor IRT equating pilot：general factor + 57 subject-specific factors拟合、 anchor item选择、fixed-parameter calibration、equated score equivalence验证。\n",
468	    "results": {
469	      "bifactor_rmsea": 0.028,
470	      "bifactor_cfi": 0.91,
471	      "bifactor_tli": 0.89,
472	      "bifactor_srmr": 0.045,
473	      "general_factor_variance_explained": 0.31,
474	      "n_anchor_items_selected": 850,
475	      "anchor_stability_criterion": "no DIF across cohorts, discrimination >0.5",
476	      "equated_rho": 0.97,
477	      "convergence_time_hours": 48,
478	      "convergence_issues": "3/57 subject factors had Heywood cases; fixed with constrained estimation",
479	      "practical_verdict": "fit marginal but usable for equating pilot"
480	    },
481	    "tables": [
482	      {
483	        "name": "Table: Bifactor IRT Fit Indices",
484	        "columns": [
485	          "index",
486	          "value",
487	          "threshold",
488	          "verdict"
489	        ],
490	        "rows": [
491	          [
492	            "RMSEA",
493	            0.028,
494	            "<0.06",
495	            "PASS"
496	          ],
497	          [
498	            "CFI",
499	            0.91,
500	            ">0.95",
501	            "MARGINAL"
502	          ],
503	          [
504	            "TLI",
505	            0.89,
506	            ">0.95",
507	            "MARGINAL"
508	          ],
509	          [
510	            "SRMR",
511	            0.045,
512	            "<0.08",
513	            "PASS"
514	          ],
515	          [
516	            "General factor ω",
517	            0.31,
518	            ">0.50",
519	            "FAIL"
520	          ]
521	        ]
522	      }
523	    ],
524	    "figures": [],
525	    "analysis": "Bifactor结果确认MMLU的multidimensionality是structural reality而非estimation artifact。 general factor ω=0.31说明unidimensional IRT fundamentally misspecified for MMLU—— 这是Limitations section的直接输入。best档下此结果被correctly scoped为motivation for future multidimensional IRT work，不作为numbered contribution。plan_015被kill是正确决策。\n\n\nbest档下bifactor模型拟合marginal(CFI=0.91, TLI=0.89略低于0.95标准)， 但这是预期结果——12,508 items × 57 subjects的bifactor是极高维模型，MMLU的inherent multidimensionality(57 subjects covering distinct knowledge domains)使完美拟合不现实。 general factor仅解释31% variance确认MMLU fundamentally multidimensional。 equated score的ρ=0.97 > 0.95目标说明即使fit marginal，equating仍然workable。 但registry显示plan_015(对应此计划)被killed——在best档下这意味着虽然结果positive， 但团队正确判断bifactor不是paper的core contribution，将其kill是scope control决策而非technical failure。\n"
526	  },
527	  {
528	    "name": "item_generation_calibration",
529	    "description": "DIF-flagged MMLU items的替换生成：LLM generation with construct constraints、 student simulation校准、difficulty correlation评估。\n",
530	    "results": {
531	      "n_items_generated": 500,
532	      "n_dif_items_targeted": 200,
533	      "prompt_difficulty_rho": 0.32,
534	      "simulation_difficulty_rho": 0.71,
535	      "cognitive_level_match_rate": 0.78,
536	      "subject_match_rate": 1.0,
537	      "holdout_validation_rho": 0.65,
538	      "generation_model": "claude-3.5-sonnet",
539	      "student_simulation_model": "arXiv 2601.09953 protocol",
540	      "calibration_rmse": 0.18
541	    },
542	    "tables": [
543	      {
544	        "name": "Table: Item Generation Calibration Accuracy",
545	        "columns": [
546	          "method",
547	          "difficulty_rho",
548	          "cognitive_match",
549	          "holdout_rho"
550	        ],
551	        "rows": [
552	          [
553	            "Prompt-only targeting",
554	            0.32,
555	            0.65,
556	            0.28
557	          ],
558	          [
559	            "Student simulation",
560	            0.71,
561	            0.78,
562	            0.65
563	          ],
564	          [
565	            "Literature benchmark",
566	            "0.75-0.82",
567	            "—",
568	            "—"
569	          ]
570	        ]
571	      }
572	    ],
573	    "figures": [],
574	    "analysis": "此实验确认item generation作为standalone contribution不够成熟，正确dropped from main paper。 student simulation的0.71相关性是promising future direction但不足以支撑equating pipeline claim。\n\n\nbest档下prompt-based difficulty targeting的ρ=0.32与文献报告(0.10-0.45)一致—— LLM对item difficulty的直觉calibration有限。student simulation将其提升至ρ=0.71， 远好于prompt-only但仍低于target benchmark的0.75-0.82。holdout validation ρ=0.65 反映generalization gap。cognitive level matching 78%说明同subject同difficulty≠同cognitive demand。 best档下此结果支撑\"item generation is feasible but imperfect\"的honest assessment， 与paper scope control一致(此实验在framing中标记为below benchmarks, dropped)。\n"
575	  },
576	  {
577	    "name": "cumulative_bayesian_dif",
578	    "description": "Sinharay et al. (2006) cumulative Bayesian DIF priors实现：4次successive benchmark administrations模拟、 累积evidence下的power improvement量化。\n",
579	    "results": {
580	      "n_simulated_administrations": 4,
581	      "individual_admin_power_delta_10": 0.42,
582	      "cumulative_2admin_power_delta_10": 0.58,
583	      "cumulative_3admin_power_delta_10": 0.71,
584	      "cumulative_4admin_power_delta_10": 0.78,
585	      "individual_admin_power_delta_14": 0.68,
586	      "cumulative_3admin_power_delta_14": 0.85,
587	      "fpr_all_conditions": "<0.055",
588	      "prior_shrinkage_effect": "reduces false positives at small N by 40%",
589	      "bayes_factor_threshold": 10,
590	      "posterior_prob_threshold": 0.95,
591	      "simulation_n_items": 500,
592	      "simulation_n_models_per_admin": 200
593	    },
594	    "tables": [
595	      {
596	        "name": "Table: Cumulative Bayesian DIF Power by Administration Count",
597	        "columns": [
598	          "n_administrations",
599	          "power_delta_10",
600	          "power_delta_14",
601	          "power_delta_16",
602	          "fpr"
603	        ],
604	        "rows": [
605	          [
606	            1,
607	            0.42,
608	            0.68,
609	            0.72,
610	            0.041
611	          ],
612	          [
613	            2,
614	            0.58,
615	            0.79,
616	            0.84,
617	            0.038
618	          ],
619	          [
620	            3,
621	            0.71,
622	            0.85,
623	            0.9,
624	            0.035
625	          ],
626	          [
627	            4,
628	            0.78,
629	            0.89,
630	            0.93,
631	            0.033
632	          ]
633	        ]
634	      }
635	    ],
636	    "figures": [],
637	    "analysis": "Cumulative Bayesian framework为audit protocol的longitudinal monitoring提供理论基础： 即使单次检测power有限(0.42 at δ=1.0)，3-4次累积后power接近0.80。 这直接支撑三tier audit protocol中的\"monitor\"层(C%<15)——低于action阈值的items 可通过cumulative monitoring最终达到decision threshold。Appendix material。\n\n\nbest档下cumulative power从单次0.42(δ=1.0)升至3次累积0.71，恰好达到target ~0.70。 这符合Bayesian累积的理论预期——每次administration提供independent evidence， posterior precision按√n速率增长。对δ=1.4(paper的operational region)，3次累积达0.85 已经很强。prior shrinkage对small N场景尤其有价值——减少40% false positives。 best档下此结果作为supplementary analysis(audit protocol的temporal monitoring组件)， 不进入main body。与paper framing一致：plan_007标记为P2 simulation-only, underdeveloped。\n"
638	  },
639	  {
640	    "name": "graceful_degradation_analysis",
641	    "description": "Progressive item replacement下的benchmark validity degradation分析： ranking stability、score reliability、construct coverage随replacement率的变化。\n",
642	    "results": {
643	      "replacement_5pct": {
644	        "ranking_rho": 0.999,
645	        "reliability_alpha": 0.968,
646	        "construct_coverage": 0.98
647	      },
648	      "replacement_10pct": {
649	        "ranking_rho": 0.997,
650	        "reliability_alpha": 0.961,
651	        "construct_coverage": 0.96
652	      },
653	      "replacement_20pct": {
654	        "ranking_rho": 0.993,
655	        "reliability_alpha": 0.948,
656	        "construct_coverage": 0.93
657	      },
658	      "replacement_50pct": {
659	        "ranking_rho": 0.978,
660	        "reliability_alpha": 0.912,
661	        "construct_coverage": 0.85
662	      },
663	      "theoretical_bound_ranking": "ρ ≥ 1 - 0.45r where r is replacement fraction",
664	      "theoretical_bound_reliability": "α ≥ α₀(1 - 0.8r²)",
665	      "empirical_validation_rho_vs_bound": 0.994
666	    },
667	    "tables": [
668	      {
669	        "name": "Table: Benchmark Validity Metrics Under Progressive Replacement",
670	        "columns": [
671	          "replacement_pct",
672	          "ranking_rho",
673	          "reliability_alpha",
674	          "construct_coverage"
675	        ],
676	        "rows": [
677	          [
678	            0,
679	            1.0,
680	            0.972,
681	            1.0
682	          ],
683	          [
684	            5,
685	            0.999,
686	            0.968,
687	            0.98
688	          ],
689	          [
690	            10,
691	            0.997,
692	            0.961,
693	            0.96
694	          ],
695	          [
696	            20,
697	            0.993,
698	            0.948,
699	            0.93
700	          ],
701	          [
702	            31,
703	            0.99,
704	            0.935,
705	            0.89
706	          ],
707	          [
708	            50,
709	            0.978,
710	            0.912,
711	            0.85
712	          ]
713	        ]
714	      }
715	    ],
716	    "figures": [],
717	    "analysis": "Graceful degradation结果直接支撑\"instability ≠ invalidity\"核心叙事： 即使替换31% DIF items，所有validity metrics仍在可接受范围内。 这与plan_017的ρ=0.996-0.999完全一致。对paper的audit protocol提供quantitative backing： benchmark maintainers可以confidently替换C-flagged items而不担心validity collapse。\n\n\nbest档下graceful degradation非常温和——50%替换后ranking ρ仍然0.978。 这与plan_017/plan_032的发现一致：MMLU具有massive measurement redundancy (ρ≈0.997 在31% DIF item removal后)，说明12,508 items中存在大量redundant measurement。 reliability从0.97降至0.91(50%替换)反映alpha对item数量的敏感性，但仍在可接受范围。 construct coverage下降(0.85 at 50%)是最敏感的指标——某些subject的coverage在高替换率下 因item数量不足而退化。theoretical bound与empirical fit的高相关(0.994)说明degradation 是predictable和manageable的。best档下此结果支撑audit protocol的\"act\"层decision-making。\n"
718	  },
719	  {
720	    "name": "item_focused_trees",
721	    "description": "Item-Focused Trees (Tutz & Berger, 2016) 实现：以model release date为continuous covariate 替代categorical cohort split的DIF检测，与MH categorical DIF的对比。\n",
722	    "results": {
723	      "n_items_analyzed": 12508,
724	      "ift_dif_detection_rate": 0.34,
725	      "ift_mh_concordance": 0.88,
726	      "ift_unique_detections": 412,
727	      "mh_unique_detections": 287,
728	      "ift_continuous_advantage": "detects gradual drift missed by binary split",
729	      "ift_vs_mh_jaccard": 0.81,
730	      "ift_nonlinear_items": 856,
731	      "ift_split_point_mode": "2023-Q4",
732	      "computation_time_hours": 8,
733	      "cross_validation_stability": 0.91
734	    },
735	    "tables": [
736	      {
737	        "name": "Table: IFT vs MH-DIF Detection Comparison",
738	        "columns": [
739	          "method",
740	          "detection_rate",
741	          "unique_items",
742	          "computation_hours"
743	        ],
744	        "rows": [
745	          [
746	            "MH-DIF (categorical)",
747	            "31.3%",
748	            287,
749	            0.5
750	          ],
751	          [
752	            "IFT (continuous)",
753	            "34.0%",
754	            412,
755	            8.0
756	          ],
757	          [
758	            "Overlap (both)",
759	            "—",
760	            "Jaccard=0.81",
761	            "—"
762	          ]
763	        ]
764	      }
765	    ],
766	    "figures": [],
767	    "analysis": "IFT as robustness check完美服务best档叙事：不同方法学(continuous vs categorical) converge on same ~30%+ instability finding。IFT的8h computation vs MH的0.5h说明 MH作为primary method的practical advantage。nonlinear items是interesting supplementary finding 但不改变main conclusion。Paper placement: appendix robustness check。\n\n\nbest档下IFT detection rate 34%略高于MH的31.3%，因为continuous treatment of release date 捕获了binary split遗漏的gradual drift items——某些items的difficulty在2023-Q3开始 渐变而非在2023/2024 boundary突变。concordance 0.88和Jaccard 0.81说明两种方法 大量overlap但各有unique detections。IFT的split point mode在2023-Q4与temporal cohort boundary一致，验证了categorical split的reasonable choice。 856个nonlinear items(difficulty随时间非单调变化)是IFT独有的insight—— binary DIF无法捕获\"先变难后变容易\"的pattern。 best档下此结果作为robustness check强化Claim 1：continuous method也给出~30%+ instability。\n"
768	  },
769	  {
770	    "name": "architecture_stratified_dif",
771	    "description": "Architecture-homogeneous subpopulation内的DIF分析：decoder-only only subset、 IRT fit diagnostics、homogeneous vs full population DIF比较。\n",
772	    "results": {
773	      "n_decoder_only": 5226,
774	      "n_non_decoder": 1,
775	      "pct_decoder_only": 99.98,
776	      "full_population_c_pct": 31.3,
777	      "decoder_only_c_pct": 31.3,
778	      "jaccard_full_vs_decoder_only": 1.0,
779	      "rmsea_full": 0.031,
780	      "rmsea_decoder_only": 0.031,
781	      "cfi_full": 0.89,
782	      "cfi_decoder_only": 0.89,
783	      "irt_fit_change": "negligible — removing 1 model changes nothing",
784	      "architecture_heterogeneity_verdict": "non-issue for METABENCH MMLU"
785	    },
786	    "tables": [
787	      {
788	        "name": "Table: Architecture Stratification Impact",
789	        "columns": [
790	          "population",
791	          "n_models",
792	          "c_pct",
793	          "jaccard_vs_full",
794	          "rmsea"
795	        ],
796	        "rows": [
797	          [
798	            "Full population",
799	            5227,
800	            31.3,
801	            "—",
802	            0.031
803	          ],
804	          [
805	            "Decoder-only only",
806	            5226,
807	            31.3,
808	            1.0,
809	            0.031
810	          ]
811	        ]
812	      }
813	    ],
814	    "figures": [],
815	    "analysis": "此实验在best档下是一行proactive defense。reviewer concern about architecture heterogeneity 在METABENCH MMLU上empirically无意义。paper中作为脚注或inline报告而非独立subsection。\n\n\nbest档下architecture stratification结果trivial——METABENCH MMLU中99.98%(5226/5227) 是decoder-only，唯一的non-decoder模型移除后Jaccard=1.0，C%完全不变。 这是paper_framing中已记录的结果。IRT fit indices不变因为单个模型的移除对5227×12508 矩阵的统计量影响在numerical noise范围内。 best档下此结果是proactive defense against \"architecture heterogeneity inflates DIF\" reviewer concern的一行报告：METABENCH MMLU is architecturally homogeneous, concern is moot。\n"
816	  },
817	  {
818	    "name": "semi_synthetic_contamination_validation",
819	    "description": "Real METABENCH response matrix上的known contamination injection：500 clean items选择、 100-200 items注入synthetic contamination(incorrect→correct flipping)、 controlled ground truth下的TPR/FPR测量、injection参数变化(prevalence, exploitation rate, focal group size)。\n",
820	    "results": {
821	      "temporal_external_tpr_p0": 0.326,
822	      "temporal_external_tpr_p03": 0.548,
823	      "temporal_external_tpr_p05": 0.834,
824	      "temporal_external_tpr_p07": 0.99,
825	      "temporal_external_tpr_p10": 1.0,
826	      "temporal_external_fpr": 0.314,
827	      "temporal_external_delta_tpr_p05": 0.508,
828	      "temporal_external_delta_tpr_p10": 0.674,
829	      "ability_external_tpr_p10": 0.8,
830	      "ability_external_fpr": 0.493,
831	      "standard_mh_fpr_inflation": "0.298→0.616 at p=1.0",
832	      "cross_subject_matching_fpr_stable": true,
833	      "dose_response_monotonic": true,
834	      "injection_n_items": 200,
835	      "clean_baseline_n_items": 500
836	    },
837	    "tables": [
838	      {
839	        "name": "Table: Semi-Synthetic Detection Power (Cross-Subject Matching)",
840	        "columns": [
841	          "exploitation_rate_p",
842	          "tpr",
843	          "delta_tpr",
844	          "fpr",
845	          "fpr_inflation"
846	        ],
847	        "rows": [
848	          [
849	            "0.0 (baseline)",
850	            0.326,
851	            "—",
852	            0.314,
853	            0.0
854	          ],
855	          [
856	            0.3,
857	            0.548,
858	            0.222,
859	            0.314,
860	            0.0
861	          ],
862	          [
863	            0.5,
864	            0.834,
865	            0.508,
866	            0.314,
867	            0.0
868	          ],
869	          [
870	            0.7,
871	            0.99,
872	            0.664,
873	            0.314,
874	            0.0
875	          ],
876	          [
877	            1.0,
878	            1.0,
879	            0.674,
880	            0.314,
881	            0.0
882	          ]
883	        ]
884	      },
885	      {
886	        "name": "Table: Matching Strategy Comparison at p=1.0",
887	        "columns": [
888	          "matching",
889	          "tpr",
890	          "fpr",
891	          "delta_fpr_vs_baseline"
892	        ],
893	        "rows": [
894	          [
895	            "Standard (within-benchmark)",
896	            1.0,
897	            0.616,
898	            0.298
899	          ],
900	          [
901	            "Cross-subject (external)",
902	            1.0,
903	            0.314,
904	            0.0
905	          ]
906	        ]
907	      }
908	    ],
909	    "figures": [],
910	    "analysis": "semi-synthetic validation是paper中load-bearing experiment之一。ΔTPR=+0.508是Claim 2 的empirical anchor：如果DIF只检测\"noise\"，注入known contamination不应提升TPR。 cross-subject matching的ΔFPR=0.000(5个subjects全部)是Claim 3的practical innovation proof。 best档下此实验与plan_016(within-subject semi-synthetic)共同构成semi-synthetic framework 的完整validation story。\n\n\nbest档下semi-synthetic validation的核心是ΔTPR=+0.508 at p=0.5——这证明DIF能检测 known differential contamination(注入的ground truth)。dose-response单调性(从p=0.3到p=1.0 TPR单调上升)确认检测力与exploitation rate成正比，排除了random artifact。 baseline FPR=0.314反映temporal cohort的genuine item-level DIF(与plan_001的31.3%一致)， 而非false positives——这些\"false\" positives实际上是真实的temporal instability。 cross-subject matching的FPR stability(vs standard matching的inflation至0.616) 是Claim 3的关键贡献：matching variable contamination是subtle but critical methodological issue。 best档下这些数字完美支撑三贡献结构中的Claim 2(semi-synthetic proves DIF detects what web-overlap labels cannot capture)和Claim 3(cross-subject matching as reusable infrastructure)。\n"
911	  },
912	  {
913	    "name": "multi_benchmark_temporal_dif",
914	    "description": "METABENCH中额外benchmark(ARC-Challenge, HellaSwag, WinoGrande, TruthfulQA)的 temporal DIF分析，加上已完成的MMLU和GSM8K，共6个benchmark。\n",
915	    "results": {
916	      "mmlu": {
917	        "n_items": 12508,
918	        "n_ref": 1080,
919	        "n_foc": 807,
920	        "pct_c": 31.3,
921	        "random_pct_c": 0.18,
922	        "bootstrap_ci_95": [
923	          29.38,
924	          38.05
925	        ]
926	      },
927	      "winogrande": {
928	        "n_items": 1267,
929	        "n_ref": 1017,
930	        "n_foc": 803,
931	        "pct_c": 30.3,
932	        "random_pct_c": 0.32
933	      },
934	      "truthfulqa": {
935	        "n_items": 817,
936	        "n_ref": 1080,
937	        "n_foc": 807,
938	        "pct_c": 29.7,
939	        "random_pct_c": 0.37
940	      },
941	      "arc": {
942	        "n_items": 1172,
943	        "n_ref": 1080,
944	        "n_foc": 807,
945	        "pct_c": 26.9,
946	        "random_pct_c": 0.6
947	      },
948	      "gsm8k": {
949	        "n_items": 1319,
950	        "n_ref": 1017,
951	        "n_foc": 804,
952	        "pct_c": 18.9,
953	        "random_pct_c": 0.3
954	      },
955	      "hellaswag": {
956	        "n_items": 10042,
957	        "n_ref": 1080,
958	        "n_foc": 807,
959	        "pct_c": 17.9,
960	        "random_pct_c": 0.28
961	      },
962	      "cross_benchmark_range": "17.9–31.3%",
963	      "all_random_controls_below_1pct": true,
964	      "min_enrichment_ratio_vs_random": 45
965	    },
966	    "tables": [
967	      {
968	        "name": "Table: Cross-Benchmark Temporal DIF Summary",
969	        "columns": [
970	          "benchmark",
971	          "n_items",
972	          "n_ref",
973	          "n_foc",
974	          "pct_c",
975	          "random_pct_c",
976	          "ratio"
977	        ],
978	        "rows": [
979	          [
980	            "MMLU",
981	            12508,
982	            1080,
983	            807,
984	            31.3,
985	            0.18,
986	            "174×"
987	          ],
988	          [
989	            "WinoGrande",
990	            1267,
991	            1017,
992	            803,
993	            30.3,
994	            0.32,
995	            "95×"
996	          ],
997	          [
998	            "TruthfulQA",
999	            817,
1000	            1080,
1001	            807,
1002	            29.7,
1003	            0.37,
1004	            "80×"
1005	          ],
1006	          [
1007	            "ARC-Challenge",
1008	            1172,
1009	            1080,
1010	            807,
1011	            26.9,
1012	            0.6,
1013	            "45×"
1014	          ],
1015	          [
1016	            "GSM8K",
1017	            1319,
1018	            1017,
1019	            804,
1020	            18.9,
1021	            0.3,
1022	            "63×"
1023	          ],
1024	          [
1025	            "HellaSwag",
1026	            10042,
1027	            1080,
1028	            807,
1029	            17.9,
1030	            0.28,
1031	            "64×"
1032	          ]
1033	        ]
1034	      }
1035	    ],
1036	    "figures": [],
1037	    "analysis": "6-benchmark consistency(全部>15%、全部random<1%)是best档的strongest generalizability evidence。 range 17.9-31.3%在best档key metrics范围内(cross_benchmark_c_pct_min 17-20%, max 29-33%)。 此结果被审稿人视为充分跨benchmark证据，不需要additional benchmarks。\n\n\nbest档下6 benchmark全部显示显著temporal DIF(17.9-31.3%)，所有random controls <1%。 C%的跨benchmark range反映benchmark结构差异：MMLU/WinoGrande/TruthfulQA(多domain/多题型) 的C%较高(29-31%)因为item heterogeneity提供更多DIF机会； GSM8K/HellaSwag(单domain或特定task)较低(17-19%)因为items更同质， differential functioning更多被ability matching吸收。 ARC(26.9%)居中。enrichment ratio(vs random)最低45×说明temporal DIF在所有benchmark 上都far above chance。best档下6-benchmark consistency是Claim 1 generalizability的核心证据， 直接回应\"only validated on MMLU\"的reviewer concern。\n"
1038	  },
1039	  {
1040	    "name": "permutation_null_c_rate",
1041	    "description": "1000× permutation test：随机重分配2023/2024 temporal labels(保持group sizes N_ref=1080, N_foc=807)，每次运行MH-DIF，建立C%的null distribution。\n",
1042	    "results": {
1043	      "n_permutations": 1000,
1044	      "null_c_pct_mean": 0.21,
1045	      "null_c_pct_sd": 0.05,
1046	      "null_c_pct_max": 0.42,
1047	      "null_c_pct_p95": 0.3,
1048	      "null_c_pct_p99": 0.36,
1049	      "observed_c_pct": 31.3,
1050	      "permutation_p_value": "<0.001",
1051	      "z_score_observed_vs_null": ">600",
1052	      "null_distribution_shape": "approximately normal, centered near random-split control",
1053	      "consistency_with_random_split": true,
1054	      "random_split_c_pct": 0.18,
1055	      "computation_time_hours": 12
1056	    },
1057	    "tables": [
1058	      {
1059	        "name": "Table: Permutation Null Distribution Summary",
1060	        "columns": [
1061	          "statistic",
1062	          "value"
1063	        ],
1064	        "rows": [
1065	          [
1066	            "Observed C%",
1067	            31.3
1068	          ],
1069	          [
1070	            "Null mean C%",
1071	            0.21
1072	          ],
1073	          [
1074	            "Null SD",
1075	            0.05
1076	          ],
1077	          [
1078	            "Null max (1000 perms)",
1079	            0.42
1080	          ],
1081	          [
1082	            "Permutation p-value",
1083	            "<0.001"
1084	          ],
1085	          [
1086	            "z-score",
1087	            ">600"
1088	          ],
1089	          [
1090	            "Random-split control C%",
1091	            0.18
1092	          ]
1093	        ]
1094	      }
1095	    ],
1096	    "figures": [],
1097	    "analysis": "Permutation null是Claim 1最直接的statistical significance evidence。 null mean 0.21%与random split 0.18%的一致性(差异0.03pp)说明两种null estimation converge。 observed 31.3%在null的>600σ之外——这不是marginal significance，而是absolute certainty that temporal DIF is real。best档下审稿人无法质疑\"31% is chance level\"。 此实验落在best档key metrics范围内(permutation_null_c_pct [0.0, 1.0])。\n\n\nbest档下permutation null的mean C%=0.21%与within-cohort random split(0.18%)高度一致—— 这是预期的，因为random label permutation破坏temporal信号后，MH-DIF只能检测到 random fluctuation，与random split在概率上等价。null C% max=0.42%说明1000次permutation 中最极端的case也远低于observed 31.3%。z>600意味着observed值在null distribution的 >600个标准差之外，permutation p<0.001(实际上是p<1/1000因为0/1000 permutations达到31.3%)。 best档下此结果直接回答\"is 31% above chance?\"——答案是overwhelming yes。 null distribution的near-normal shape和consistency with random split互相验证了两种 null estimation方法的正确性。\n"
1098	  },
1099	  {
1100	    "name": "odds_ratio_regression_transparency",
1101	    "description": "DIF flag的logistic regression透明度分析：odds ratio + 95% CI + 多种R²指标 + deviance ratio。 item-level finer-grained model (DIF flag ~ item-level accuracy change)补充domain-level分析。\n",
1102	    "results": {
1103	      "model1_domain_delta": {
1104	        "mcfadden_r2": 0.0007,
1105	        "nagelkerke_r2": 0.0012,
1106	        "subject_acc_delta_or_per_010": 1.55,
1107	        "subject_acc_delta_ci_per_010": [
1108	          1.19,
1109	          2.03
1110	        ]
1111	      },
1112	      "model2_domain_delta_plus_items": {
1113	        "mcfadden_r2": 0.0423,
1114	        "nagelkerke_r2": 0.072,
1115	        "subject_acc_delta_or_per_010": 0.73,
1116	        "ctt_discrimination_or_per_010": 1.51
1117	      },
1118	      "model3_item_delta": {
1119	        "mcfadden_r2": 0.0012,
1120	        "nagelkerke_r2": 0.0021,
1121	        "item_acc_change_or_per_010": 1.08,
1122	        "item_acc_change_ci": [
1123	          1.51,
1124	          2.96
1125	        ]
1126	      },
1127	      "model4_item_delta_plus_items": {
1128	        "mcfadden_r2": 0.0434,
1129	        "nagelkerke_r2": 0.0737,
1130	        "item_acc_change_or_per_010": 0.92,
1131	        "ctt_discrimination_or_per_010": 1.54
1132	      },
1133	      "simpsons_paradox": true,
1134	      "lr_test_m1_vs_m2_chi2": 646.98,
1135	      "lr_test_m3_vs_m4_chi2": 655.53
1136	    },
1137	    "tables": [
1138	      {
1139	        "name": "Table: Logistic Regression Models for DIF Flag Prediction",
1140	        "columns": [
1141	          "model",
1142	          "predictors",
1143	          "mcfadden_r2",
1144	          "nagelkerke_r2",
1145	          "key_or"
1146	        ],
1147	        "rows": [
1148	          [
1149	            "Model 1",
1150	            "subject_acc_Δ",
1151	            0.0007,
1152	            0.0012,
1153	            "1.55 [1.19,2.03]"
1154	          ],
1155	          [
1156	            "Model 2",
1157	            "subject_acc_Δ + item_props",
1158	            0.0423,
1159	            0.072,
1160	            "0.73 (reversed)"
1161	          ],
1162	          [
1163	            "Model 3",
1164	            "item_acc_Δ",
1165	            0.0012,
1166	            0.0021,
1167	            "1.08 [1.51,2.96]"
1168	          ],
1169	          [
1170	            "Model 4",
1171	            "item_acc_Δ + item_props",
1172	            0.0434,
1173	            0.0737,
1174	            "0.92 (reversed)"
1175	          ]
1176	        ]
1177	      }
1178	    ],
1179	    "figures": [],
1180	    "analysis": "Simpson's paradox是this experiment的signature finding。Model 1作为primary(conservative, gives accuracy change its best shot at explaining DIF)，Model 2作为supplementary (shows the paradox)。审稿人看到R²<0.001 for accuracy change alone即可确信 \"31% is not just models getting better\"。dual interpretation explicitly acknowledged in Discussion。\n\nbest档下四个模型的R²全部极低(<0.08)，这是core finding而非limitation： accuracy change(无论domain-level还是item-level)解释DIF variance的能力极弱， 说明DIF捕获的是item-specific differential functioning而非aggregate accuracy improvement。 Simpson's paradox(Model 1中OR=1.55 per 0.10 accuracy change但Model 2/4中OR翻转至<1) 说明item properties(difficulty, discrimination)是confounders——controlling后accuracy change 的apparent effect消失甚至反转。best档下此结果是plan_019(decomposition: ≤2.4pp/7.6%) 的complementary evidence，用不同方法学(logistic regression vs item-level decomposition) converge on same conclusion。discrimination OR=1.54最具信息量：high-discrimination items 更容易被flag为DIF-C，因为它们对ability差异更敏感，微小的cohort composition差异就能触发large |Δ_MH|。\n"
1181	  }
1182	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7faebecb-2270-4db4-98e2-79f117a04ef8",
  "isSidechain": false,
  "promptId": "fbb2aad3-deff-45fc-a21a-33870865ab9a",
  "type": "user",
  "uuid": "e64e2c92-508c-49df-b7b9-6f27837041b9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"real_data_dif_mmlu\",\n    \"description\": \"METABENCH MMLU response matrix (5,219 models × 12,508 items) 上的全量DIF分析。 temporal cohort (2023 vs 2024-H1)、ability-quintile split、within-family confound control、domain-specificity分析。\\n\",\n    \"results\": {\n      \"temporal_ets_c_pct\": 31.3,\n      \"temporal_fpr_li_clean\": 0.318,\n      \"temporal_enrichment\": 0.96,\n      \"ability_ets_c_pct\": 2.9,\n      \"ability_enrichment\": 1.19,\n      \"within_family_llama2v3_c_pct\": 61.3,\n      \"within_family_mistral_mixtral_c_pct\": 38.7,\n      \"domain_spearman_rho\": 0.307,\n      \"domain_spearman_p\": 0.02,\n      \"sanity_random_split_c_pct\": 0.18,\n      \"temporal_ability_jaccard\": 0.014,\n      \"n_models_temporal_ref\": 1080,\n      \"n_models_temporal_foc\": 807,\n      \"n_items\": 12508,\n      \"domain_specificity_c_range\": \"20.7–48.4%\",\n      \"domain_specificity_mean\": 30.6,\n      \"negative_disc_items_pct\": 15.4,\n      \"negative_disc_sensitivity\": \"C% changes <0.5pp with/without negative-disc items\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Temporal DIF Summary (ETS C Classification)\",\n        \"columns\": [\n          \"cohort_definition\",\n          \"n_ref\",\n          \"n_foc\",\n          \"n_items\",\n          \"pct_A\",\n          \"pct_B\",\n          \"pct_C\",\n          \"enrichment_li\",\n          \"random_sanity_c_pct\"\n        ],\n        \"rows\": [\n          [\n            \"temporal_2023v2024\",\n            1080,\n            807,\n            12508,\n            52.4,\n            16.3,\n            31.3,\n            0.96,\n            0.18\n          ],\n          [\n            \"ability_quintile\",\n            1044,\n            1044,\n            12508,\n            85.2,\n            11.9,\n            2.9,\n            1.19,\n            0.15\n          ],\n          [\n            \"within_family_llama\",\n            161,\n            308,\n            12508,\n            24.1,\n            14.6,\n            61.3,\n            0.91,\n            0.22\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Domain-Specificity Top/Bottom 5 Subjects by C%\",\n        \"columns\": [\n          \"subject\",\n          \"n_items\",\n          \"pct_c\",\n          \"pct_favor_2024\"\n        ],\n        \"rows\": [\n          [\n            \"business_ethics\",\n            100,\n            48.4,\n            39.6\n          ],\n          [\n            \"human_aging\",\n            223,\n            41.9,\n            38.7\n          ],\n          [\n            \"formal_logic\",\n            126,\n            40.4,\n            42.1\n          ],\n          [\n            \"management\",\n            103,\n            21.7,\n            44.2\n          ],\n          [\n            \"computer_security\",\n            100,\n            20.7,\n            47.3\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"31.3%作为primary estimate稳固。ability split的2.9%与temporal的31.3%形成鲜明对比， 直接排除\\\"models got better → inflated DIF\\\"的解释。within-family结果(61.3%) 虽然高，但因Llama-2v3能力差距极大(d=-0.99)，plan_027的matching分析已将genuine item-level DIF 锁定在~28-29%。domain分析的ρ=0.307(p=0.02)是honest reporting——plan_019的item-level decomposition将其降至≤2.4pp(7.6%)，是paper的关键robustness支撑。\\n\\n\\nbest档下temporal cohort的31.3% C%是核心headline数字，已被多层robustness control确认。 random split 0.18%证明非统计伪影。enrichment≈0.96与Li et al.标签的理论预期一致—— web-overlap是global exposure指标，DIF检测differential functioning，二者正交，enrichment≈1.0是预期结果。 ability split仅2.9%说明DIF确实捕获temporal信号而非能力差异。within-family Llama-2v3的61.3% 反映两代间巨大能力跳跃(d=-0.99)中的genuine item-level变化，而非伪影。domain相关ρ=0.307 表明domain improvement有modest贡献但非主因——plan_019/plan_030进一步量化为≤7.6%。\\n\"\n  },\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"验证DIF对reasoning-RL模型的鲁棒性。三组对比：SFT-only baseline、alignment-RL(DPO/ORPO, N=477)、 reasoning-RL(10-15个GRPO/PPO模型注入focal cohort)。DIF group-level稳定性 vs 传统detector model-level退化。\\n\",\n    \"results\": {\n      \"n_reasoning_rl_models\": 13,\n      \"reasoning_rl_models_list\": \"DeepSeek-R1-7B, DeepSeek-R1-32B, Qwen2.5-RL-7B, Qwen2.5-RL-14B, Qwen2.5-RL-32B, Marco-o1-7B, Skywork-OR1-8B, OpenThinker-7B, OpenThinker-32B, s1-32B, STILL-2-7B, Light-R1-7B, Bespoke-Stratos-7B\",\n      \"sft_baseline_c_pct\": 31.3,\n      \"alignment_rl_cohort_c_pct\": 31.1,\n      \"reasoning_rl_mixed_cohort_c_pct\": 30.8,\n      \"jaccard_sft_vs_alignment_rl\": 0.94,\n      \"jaccard_sft_vs_reasoning_rl_mixed\": 0.92,\n      \"jaccard_alignment_vs_reasoning_rl\": 0.93,\n      \"dif_flag_retention_rate\": 0.95,\n      \"bootstrap_ci_jaccard_sft_vs_rl\": [\n        0.9,\n        0.96\n      ],\n      \"tost_equivalence_p\": 0.003,\n      \"tost_equivalence_margin\": 0.05,\n      \"traditional_mink_auroc_sft\": 0.72,\n      \"traditional_mink_auroc_rl\": 0.48,\n      \"traditional_constat_auroc_sft\": 0.68,\n      \"traditional_constat_auroc_rl\": 0.51,\n      \"auroc_drop_mink\": 0.24,\n      \"auroc_drop_constat\": 0.17,\n      \"delong_mink_p\": 0.001,\n      \"delong_constat_p\": 0.008,\n      \"partial_exploitation_power\": {\n        \"p_04\": {\n          \"dif_tpr\": 0.42,\n          \"mink_auroc\": 0.39\n        },\n        \"p_06\": {\n          \"dif_tpr\": 0.61,\n          \"mink_auroc\": 0.44\n        },\n        \"p_08\": {\n          \"dif_tpr\": 0.78,\n          \"mink_auroc\": 0.46\n        },\n        \"p_10\": {\n          \"dif_tpr\": 0.91,\n          \"mink_auroc\": 0.48\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: DIF Stability Across Training Paradigms\",\n        \"columns\": [\n          \"cohort_composition\",\n          \"n_foc\",\n          \"c_pct\",\n          \"jaccard_vs_sft\",\n          \"bootstrap_ci_95\"\n        ],\n        \"rows\": [\n          [\n            \"SFT-only (baseline)\",\n            807,\n            31.3,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Alignment-RL (DPO/ORPO)\",\n            477,\n            31.1,\n            0.94,\n            \"[0.92, 0.96]\"\n          ],\n          [\n            \"SFT+Reasoning-RL mixed\",\n            820,\n            30.8,\n            0.92,\n            \"[0.90, 0.96]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Traditional Detector Degradation on Reasoning-RL\",\n        \"columns\": [\n          \"detector\",\n          \"auroc_sft\",\n          \"auroc_rl\",\n          \"delta_auroc\",\n          \"delong_p\"\n        ],\n        \"rows\": [\n          [\n            \"Min-K%\",\n            0.72,\n            0.48,\n            -0.24,\n            0.001\n          ],\n          [\n            \"ConStat\",\n            0.68,\n            0.51,\n            -0.17,\n            0.008\n          ],\n          [\n            \"DIF (group)\",\n            \"—\",\n            \"—\",\n            \"Jaccard=0.92\",\n            \"TOST p=0.003\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"best档核心结论：DIF的group-level design天然免疫于RL训练对individual model信号的扰动。 13个RL模型虽少但足够——DIF不需要N≥80个RL模型，只需focal cohort total N≥80且RL模型 混入后不改变group-level pattern。Jaccard=0.92超过0.90阈值，TOST正式排除degradation。 传统detector的0.17-0.24 AUROC drop提供鲜明对比，强化DIF的methodological advantage叙事。 Caveat: N=13 reasoning-RL仍然underpowered for standalone claim，但作为robustness check足够。\\n\\n\\nbest档下Jaccard≥0.90是关键指标。DIF是group-level方法，将13个RL模型加入807个focal cohort (占比1.6%)对MH统计量的影响微乎其微——MH条件化total score后，RL模型的memorization pattern 被ability matching吸收。C%从31.3%微降至30.8%是噪声范围内的正常波动。 传统detector的AUROC下降0.17-0.24反映Wang et al.论证的NLL gap contraction机制： GRPO/PPO训练使模型对所有选项的logit分布更平坦，破坏了Min-K%和ConStat依赖的 per-token surprise信号，但不影响DIF的item-level binary response pattern。 TOST equivalence test (margin=0.05, p=0.003)正式确认DIF retention非空结果。\\n\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"ConStat-style perturbation testing独立评估：200+ MMLU items的LLM paraphrase生成、 原始vs重述性能对比、FDR-controlled detection、RL vs non-RL检测力对比。\\n\",\n    \"results\": {\n      \"n_items_paraphrased\": 250,\n      \"n_models_tested\": 50,\n      \"constat_detection_rate_non_rl\": 0.38,\n      \"constat_detection_rate_alignment_rl\": 0.31,\n      \"constat_detection_rate_reasoning_rl\": 0.14,\n      \"fdr_threshold\": 0.05,\n      \"constat_fpr\": 0.048,\n      \"constat_tpr_delta_ge_06\": 0.62,\n      \"constat_tpr_delta_ge_10\": 0.41,\n      \"paraphrase_quality_semantic_sim\": 0.91,\n      \"paraphrase_quality_difficulty_corr\": 0.83,\n      \"rl_sensitivity_ratio\": 0.37\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: ConStat Detection Power by Training Paradigm\",\n        \"columns\": [\n          \"paradigm\",\n          \"n_models\",\n          \"detection_rate\",\n          \"fpr\",\n          \"effect_size_threshold\"\n        ],\n        \"rows\": [\n          [\n            \"SFT-only\",\n            25,\n            0.38,\n            0.048,\n            \"δ≥0.6\"\n          ],\n          [\n            \"Alignment-RL\",\n            15,\n            0.31,\n            0.045,\n            \"δ≥0.6\"\n          ],\n          [\n            \"Reasoning-RL\",\n            10,\n            0.14,\n            0.051,\n            \"δ≥0.6\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ConStat的RL-sensitivity确认了DIF的structural advantage：DIF条件化ability后检测 item-level differential functioning，不依赖per-model perturbation response差异。 ConStat适合non-RL场景，DIF适合所有场景。此结果支撑\\\"DIF as primary, ConStat as complementary\\\"叙事。 但因paper已决定不执行此实验(scope control)，此数据仅作appendix/future work参考。\\n\\n\\nbest档下ConStat在non-RL模型上表现中等(detection rate 38%)，因为perturbation testing 依赖模型对original vs paraphrased的response差异——contaminated模型在original上表现异常好。 但reasoning-RL模型通过GRPO训练泛化了problem-solving能力(非verbatim memorization)， 使original vs paraphrased差异消失，detection rate降至14%。这为ensemble论证(DIF covers where ConStat fails)提供直接证据。FPR在0.05 FDR控制下保持在0.048。 注意：此实验在paper framing中已标记为\\\"never executed, future work\\\"，best档下执行它 是为了提供完整的baseline comparison数据。\\n\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"DVD generation variance独立评估：10-15个开源模型、每item 50次temperature sampling、 generation variance score计算、bimodal分布检测。\\n\",\n    \"results\": {\n      \"n_models\": 12,\n      \"n_items_sampled\": 500,\n      \"temperature\": 0.8,\n      \"n_generations_per_item\": 50,\n      \"dvd_detection_rate_verbatim\": 0.22,\n      \"dvd_detection_rate_variant\": 0.45,\n      \"dvd_fpr\": 0.065,\n      \"bimodal_detection_rate\": 0.33,\n      \"dvd_auroc_verbatim\": 0.61,\n      \"dvd_auroc_variant\": 0.74,\n      \"compute_hours\": 68\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: DVD Detection Power by Contamination Type\",\n        \"columns\": [\n          \"contamination_type\",\n          \"auroc\",\n          \"detection_rate\",\n          \"fpr\"\n        ],\n        \"rows\": [\n          [\n            \"verbatim\",\n            0.61,\n            0.22,\n            0.065\n          ],\n          [\n            \"variant\",\n            0.74,\n            0.45,\n            0.065\n          ],\n          [\n            \"none (clean)\",\n            \"—\",\n            \"—\",\n            0.065\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DVD填补DIF和ConStat的variant contamination检测空白。但GPU cost (68h)和detection rate 均不及DIF的zero-GPU设计。此实验与plan_003a一样在paper scope外(never executed)， best档下执行是为ensemble fusion提供完整输入。\\n\\n\\nbest档下DVD对variant contamination (非verbatim、通过paraphrase传播的)检测力最强(AUROC=0.74)， 因为variant contamination导致模型在某些generation中复现memorized pattern、其他时候正常推理， 产生bimodal variance signature。对verbatim contamination反而较弱(AUROC=0.61)， 因为verbatim memorization导致consistently correct response，variance反而低。 这与DIF(检测任何形式的differential functioning)和ConStat(检测perturbation sensitivity) 形成互补覆盖。FPR 0.065略高于理想值但可接受。\\n\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"DIF + ConStat + DVD三信号融合：threshold校准、2-of-3 majority voting、weighted fusion、 ensemble覆盖分析、5-fold交叉验证。\\n\",\n    \"results\": {\n      \"ensemble_fpr_majority\": 0.032,\n      \"ensemble_fpr_weighted\": 0.028,\n      \"ensemble_tpr_majority_delta_14\": 0.78,\n      \"ensemble_tpr_weighted_delta_14\": 0.82,\n      \"coverage_dif_only\": \"δ≥1.4, all training types\",\n      \"coverage_constat_only\": \"δ≥0.6, non-RL only\",\n      \"coverage_dvd_only\": \"variant contamination\",\n      \"coverage_ensemble\": \"δ≥0.6, all types including variant\",\n      \"cv_weight_dif\": 0.52,\n      \"cv_weight_constat\": 0.28,\n      \"cv_weight_dvd\": 0.2,\n      \"uniform_vs_optimized_auc_gap\": 0.03\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Ensemble vs Individual Detector Performance\",\n        \"columns\": [\n          \"method\",\n          \"tpr_at_fpr_05\",\n          \"auroc\",\n          \"coverage_type\"\n        ],\n        \"rows\": [\n          [\n            \"DIF (MH)\",\n            0.68,\n            0.87,\n            \"group-level, all paradigms\"\n          ],\n          [\n            \"ConStat\",\n            0.55,\n            0.76,\n            \"model-level, non-RL\"\n          ],\n          [\n            \"DVD\",\n            0.42,\n            0.71,\n            \"model-level, variant\"\n          ],\n          [\n            \"Ensemble (majority)\",\n            0.78,\n            0.91,\n            \"all\"\n          ],\n          [\n            \"Ensemble (weighted)\",\n            0.82,\n            0.93,\n            \"all\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ensemble在best档下表现优异但对paper叙事非必要——DIF standalone已足够支撑三贡献结构。 此结果作为future work方向：若DIF + ConStat + DVD三线融合被证实，可升级为独立contribution。 当前paper wisely将此降为appendix/dropped。\\n\\n\\nbest档下ensemble的FPR<0.05(远低于0.10阈值)因为2-of-3 majority voting天然抑制 single-signal false positives。TPR=0.82(weighted)超过任何单一信号因为三个detector 覆盖不同contamination机制。DIF权重最高(0.52)反映其跨training-paradigm的一致性。 uniform vs optimized差距仅0.03 AUC说明fusion对权重不敏感。 但此实验依赖plan_003a/b，且paper已明确dropped ensemble contribution。 best档下这是最佳情况的appendix material。\\n\"\n  },\n  {\n    \"name\": \"cross_benchmark_gsm8k\",\n    \"description\": \"GSM8K上的DIF复制分析：temporal cohort DIF、semi-synthetic validation、GSM1K correlation。\\n\",\n    \"results\": {\n      \"step1_gsm8k_temporal_c_pct\": 18.9,\n      \"step1_n_items\": 1319,\n      \"step1_n_ref\": 1017,\n      \"step1_n_foc\": 804,\n      \"step1_sanity_c_pct\": 0.3,\n      \"step1_standard_external_spearman\": 0.926,\n      \"step2_standard_delta_tpr_p10\": 0.818,\n      \"step2_external_delta_tpr_p10\": 0.517,\n      \"step3_n_models\": 33,\n      \"step3_pearson_r\": -0.478,\n      \"step3_pearson_p\": 0.005,\n      \"step3_spearman_rho\": -0.403,\n      \"step3_partial_r\": -0.385,\n      \"step3_direction\": \"NEGATIVE (opposite to contamination hypothesis)\",\n      \"step3_robust_leave_one_out\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: GSM8K Three-Step Validation\",\n        \"columns\": [\n          \"step\",\n          \"metric\",\n          \"value\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Step 1\",\n            \"temporal_c_pct\",\n            \"18.9%\",\n            \"Lower than MMLU, consistent with single-domain\"\n          ],\n          [\n            \"Step 1\",\n            \"sanity_c_pct\",\n            \"0.3%\",\n            \"Well below temporal signal\"\n          ],\n          [\n            \"Step 2\",\n            \"delta_tpr_p10\",\n            \"+0.818\",\n            \"Framework portable to math benchmark\"\n          ],\n          [\n            \"Step 3\",\n            \"pearson_r\",\n            -0.478,\n            \"DIF ≠ contamination on GSM8K\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"GSM8K结果在best档下完美服务于paper的reframed叙事：DIF是diagnostic tool而非contamination detector。 r=-0.478的negative correlation被明确demote为exploratory(N=33, CI wide)，不进入abstract/conclusion。 semi-synthetic ΔTPR=+0.818是Claim 3(framework)的cross-benchmark replication支撑。\\n\\n\\nbest档下GSM8K C%=18.9%低于MMLU的31.3%，因为GSM8K是单domain数学benchmark， items间能力维度同质性更高，DIF更多反映genuine capability gain而非item-specific instability。 semi-synthetic ΔTPR=+0.818(标准matching)证明framework可移植性——GSM8K的单domain结构 使matching variable(total score)与target items共线性更强，但仍能检测injected contamination。 GSM1K correlation r=-0.478(negative)是关键finding：DIF flags与contamination gap 反向关联，说明DIF在GSM8K上捕获的不是contamination而是capability-driven item functioning变化。 这是honest reporting——不利于\\\"DIF detects contamination\\\"叙事，但完美支撑\\\"DIF as diagnostic lens\\\" reframing。best档下此negative result被视为strength而非weakness。\\n\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"MMLU上的bifactor IRT equating pilot：general factor + 57 subject-specific factors拟合、 anchor item选择、fixed-parameter calibration、equated score equivalence验证。\\n\",\n    \"results\": {\n      \"bifactor_rmsea\": 0.028,\n      \"bifactor_cfi\": 0.91,\n      \"bifactor_tli\": 0.89,\n      \"bifactor_srmr\": 0.045,\n      \"general_factor_variance_explained\": 0.31,\n      \"n_anchor_items_selected\": 850,\n      \"anchor_stability_criterion\": \"no DIF across cohorts, discrimination >0.5\",\n      \"equated_rho\": 0.97,\n      \"convergence_time_hours\": 48,\n      \"convergence_issues\": \"3/57 subject factors had Heywood cases; fixed with constrained estimation\",\n      \"practical_verdict\": \"fit marginal but usable for equating pilot\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Bifactor IRT Fit Indices\",\n        \"columns\": [\n          \"index\",\n          \"value\",\n          \"threshold\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"RMSEA\",\n            0.028,\n            \"<0.06\",\n            \"PASS\"\n          ],\n          [\n            \"CFI\",\n            0.91,\n            \">0.95\",\n            \"MARGINAL\"\n          ],\n          [\n            \"TLI\",\n            0.89,\n            \">0.95\",\n            \"MARGINAL\"\n          ],\n          [\n            \"SRMR\",\n            0.045,\n            \"<0.08\",\n            \"PASS\"\n          ],\n          [\n            \"General factor ω\",\n            0.31,\n            \">0.50\",\n            \"FAIL\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bifactor结果确认MMLU的multidimensionality是structural reality而非estimation artifact。 general factor ω=0.31说明unidimensional IRT fundamentally misspecified for MMLU—— 这是Limitations section的直接输入。best档下此结果被correctly scoped为motivation for future multidimensional IRT work，不作为numbered contribution。plan_015被kill是正确决策。\\n\\n\\nbest档下bifactor模型拟合marginal(CFI=0.91, TLI=0.89略低于0.95标准)， 但这是预期结果——12,508 items × 57 subjects的bifactor是极高维模型，MMLU的inherent multidimensionality(57 subjects covering distinct knowledge domains)使完美拟合不现实。 general factor仅解释31% variance确认MMLU fundamentally multidimensional。 equated score的ρ=0.97 > 0.95目标说明即使fit marginal，equating仍然workable。 但registry显示plan_015(对应此计划)被killed——在best档下这意味着虽然结果positive， 但团队正确判断bifactor不是paper的core contribution，将其kill是scope control决策而非technical failure。\\n\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"DIF-flagged MMLU items的替换生成：LLM generation with construct constraints、 student simulation校准、difficulty correlation评估。\\n\",\n    \"results\": {\n      \"n_items_generated\": 500,\n      \"n_dif_items_targeted\": 200,\n      \"prompt_difficulty_rho\": 0.32,\n      \"simulation_difficulty_rho\": 0.71,\n      \"cognitive_level_match_rate\": 0.78,\n      \"subject_match_rate\": 1.0,\n      \"holdout_validation_rho\": 0.65,\n      \"generation_model\": \"claude-3.5-sonnet\",\n      \"student_simulation_model\": \"arXiv 2601.09953 protocol\",\n      \"calibration_rmse\": 0.18\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Item Generation Calibration Accuracy\",\n        \"columns\": [\n          \"method\",\n          \"difficulty_rho\",\n          \"cognitive_match\",\n          \"holdout_rho\"\n        ],\n        \"rows\": [\n          [\n            \"Prompt-only targeting\",\n            0.32,\n            0.65,\n            0.28\n          ],\n          [\n            \"Student simulation\",\n            0.71,\n            0.78,\n            0.65\n          ],\n          [\n            \"Literature benchmark\",\n            \"0.75-0.82\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"此实验确认item generation作为standalone contribution不够成熟，正确dropped from main paper。 student simulation的0.71相关性是promising future direction但不足以支撑equating pipeline claim。\\n\\n\\nbest档下prompt-based difficulty targeting的ρ=0.32与文献报告(0.10-0.45)一致—— LLM对item difficulty的直觉calibration有限。student simulation将其提升至ρ=0.71， 远好于prompt-only但仍低于target benchmark的0.75-0.82。holdout validation ρ=0.65 反映generalization gap。cognitive level matching 78%说明同subject同difficulty≠同cognitive demand。 best档下此结果支撑\\\"item generation is feasible but imperfect\\\"的honest assessment， 与paper scope control一致(此实验在framing中标记为below benchmarks, dropped)。\\n\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"Sinharay et al. (2006) cumulative Bayesian DIF priors实现：4次successive benchmark administrations模拟、 累积evidence下的power improvement量化。\\n\",\n    \"results\": {\n      \"n_simulated_administrations\": 4,\n      \"individual_admin_power_delta_10\": 0.42,\n      \"cumulative_2admin_power_delta_10\": 0.58,\n      \"cumulative_3admin_power_delta_10\": 0.71,\n      \"cumulative_4admin_power_delta_10\": 0.78,\n      \"individual_admin_power_delta_14\": 0.68,\n      \"cumulative_3admin_power_delta_14\": 0.85,\n      \"fpr_all_conditions\": \"<0.055\",\n      \"prior_shrinkage_effect\": \"reduces false positives at small N by 40%\",\n      \"bayes_factor_threshold\": 10,\n      \"posterior_prob_threshold\": 0.95,\n      \"simulation_n_items\": 500,\n      \"simulation_n_models_per_admin\": 200\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cumulative Bayesian DIF Power by Administration Count\",\n        \"columns\": [\n          \"n_administrations\",\n          \"power_delta_10\",\n          \"power_delta_14\",\n          \"power_delta_16\",\n          \"fpr\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.42,\n            0.68,\n            0.72,\n            0.041\n          ],\n          [\n            2,\n            0.58,\n            0.79,\n            0.84,\n            0.038\n          ],\n          [\n            3,\n            0.71,\n            0.85,\n            0.9,\n            0.035\n          ],\n          [\n            4,\n            0.78,\n            0.89,\n            0.93,\n            0.033\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cumulative Bayesian framework为audit protocol的longitudinal monitoring提供理论基础： 即使单次检测power有限(0.42 at δ=1.0)，3-4次累积后power接近0.80。 这直接支撑三tier audit protocol中的\\\"monitor\\\"层(C%<15)——低于action阈值的items 可通过cumulative monitoring最终达到decision threshold。Appendix material。\\n\\n\\nbest档下cumulative power从单次0.42(δ=1.0)升至3次累积0.71，恰好达到target ~0.70。 这符合Bayesian累积的理论预期——每次administration提供independent evidence， posterior precision按√n速率增长。对δ=1.4(paper的operational region)，3次累积达0.85 已经很强。prior shrinkage对small N场景尤其有价值——减少40% false positives。 best档下此结果作为supplementary analysis(audit protocol的temporal monitoring组件)， 不进入main body。与paper framing一致：plan_007标记为P2 simulation-only, underdeveloped。\\n\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"Progressive item replacement下的benchmark validity degradation分析： ranking stability、score reliability、construct coverage随replacement率的变化。\\n\",\n    \"results\": {\n      \"replacement_5pct\": {\n        \"ranking_rho\": 0.999,\n        \"reliability_alpha\": 0.968,\n        \"construct_coverage\": 0.98\n      },\n      \"replacement_10pct\": {\n        \"ranking_rho\": 0.997,\n        \"reliability_alpha\": 0.961,\n        \"construct_coverage\": 0.96\n      },\n      \"replacement_20pct\": {\n        \"ranking_rho\": 0.993,\n        \"reliability_alpha\": 0.948,\n        \"construct_coverage\": 0.93\n      },\n      \"replacement_50pct\": {\n        \"ranking_rho\": 0.978,\n        \"reliability_alpha\": 0.912,\n        \"construct_coverage\": 0.85\n      },\n      \"theoretical_bound_ranking\": \"ρ ≥ 1 - 0.45r where r is replacement fraction\",\n      \"theoretical_bound_reliability\": \"α ≥ α₀(1 - 0.8r²)\",\n      \"empirical_validation_rho_vs_bound\": 0.994\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Benchmark Validity Metrics Under Progressive Replacement\",\n        \"columns\": [\n          \"replacement_pct\",\n          \"ranking_rho\",\n          \"reliability_alpha\",\n          \"construct_coverage\"\n        ],\n        \"rows\": [\n          [\n            0,\n            1.0,\n            0.972,\n            1.0\n          ],\n          [\n            5,\n            0.999,\n            0.968,\n            0.98\n          ],\n          [\n            10,\n            0.997,\n            0.961,\n            0.96\n          ],\n          [\n            20,\n            0.993,\n            0.948,\n            0.93\n          ],\n          [\n            31,\n            0.99,\n            0.935,\n            0.89\n          ],\n          [\n            50,\n            0.978,\n            0.912,\n            0.85\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Graceful degradation结果直接支撑\\\"instability ≠ invalidity\\\"核心叙事： 即使替换31% DIF items，所有validity metrics仍在可接受范围内。 这与plan_017的ρ=0.996-0.999完全一致。对paper的audit protocol提供quantitative backing： benchmark maintainers可以confidently替换C-flagged items而不担心validity collapse。\\n\\n\\nbest档下graceful degradation非常温和——50%替换后ranking ρ仍然0.978。 这与plan_017/plan_032的发现一致：MMLU具有massive measurement redundancy (ρ≈0.997 在31% DIF item removal后)，说明12,508 items中存在大量redundant measurement。 reliability从0.97降至0.91(50%替换)反映alpha对item数量的敏感性，但仍在可接受范围。 construct coverage下降(0.85 at 50%)是最敏感的指标——某些subject的coverage在高替换率下 因item数量不足而退化。theoretical bound与empirical fit的高相关(0.994)说明degradation 是predictable和manageable的。best档下此结果支撑audit protocol的\\\"act\\\"层decision-making。\\n\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"Item-Focused Trees (Tutz & Berger, 2016) 实现：以model release date为continuous covariate 替代categorical cohort split的DIF检测，与MH categorical DIF的对比。\\n\",\n    \"results\": {\n      \"n_items_analyzed\": 12508,\n      \"ift_dif_detection_rate\": 0.34,\n      \"ift_mh_concordance\": 0.88,\n      \"ift_unique_detections\": 412,\n      \"mh_unique_detections\": 287,\n      \"ift_continuous_advantage\": \"detects gradual drift missed by binary split\",\n      \"ift_vs_mh_jaccard\": 0.81,\n      \"ift_nonlinear_items\": 856,\n      \"ift_split_point_mode\": \"2023-Q4\",\n      \"computation_time_hours\": 8,\n      \"cross_validation_stability\": 0.91\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: IFT vs MH-DIF Detection Comparison\",\n        \"columns\": [\n          \"method\",\n          \"detection_rate\",\n          \"unique_items\",\n          \"computation_hours\"\n        ],\n        \"rows\": [\n          [\n            \"MH-DIF (categorical)\",\n            \"31.3%\",\n            287,\n            0.5\n          ],\n          [\n            \"IFT (continuous)\",\n            \"34.0%\",\n            412,\n            8.0\n          ],\n          [\n            \"Overlap (both)\",\n            \"—\",\n            \"Jaccard=0.81\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"IFT as robustness check完美服务best档叙事：不同方法学(continuous vs categorical) converge on same ~30%+ instability finding。IFT的8h computation vs MH的0.5h说明 MH作为primary method的practical advantage。nonlinear items是interesting supplementary finding 但不改变main conclusion。Paper placement: appendix robustness check。\\n\\n\\nbest档下IFT detection rate 34%略高于MH的31.3%，因为continuous treatment of release date 捕获了binary split遗漏的gradual drift items——某些items的difficulty在2023-Q3开始 渐变而非在2023/2024 boundary突变。concordance 0.88和Jaccard 0.81说明两种方法 大量overlap但各有unique detections。IFT的split point mode在2023-Q4与temporal cohort boundary一致，验证了categorical split的reasonable choice。 856个nonlinear items(difficulty随时间非单调变化)是IFT独有的insight—— binary DIF无法捕获\\\"先变难后变容易\\\"的pattern。 best档下此结果作为robustness check强化Claim 1：continuous method也给出~30%+ instability。\\n\"\n  },\n  {\n    \"name\": \"architecture_stratified_dif\",\n    \"description\": \"Architecture-homogeneous subpopulation内的DIF分析：decoder-only only subset、 IRT fit diagnostics、homogeneous vs full population DIF比较。\\n\",\n    \"results\": {\n      \"n_decoder_only\": 5226,\n      \"n_non_decoder\": 1,\n      \"pct_decoder_only\": 99.98,\n      \"full_population_c_pct\": 31.3,\n      \"decoder_only_c_pct\": 31.3,\n      \"jaccard_full_vs_decoder_only\": 1.0,\n      \"rmsea_full\": 0.031,\n      \"rmsea_decoder_only\": 0.031,\n      \"cfi_full\": 0.89,\n      \"cfi_decoder_only\": 0.89,\n      \"irt_fit_change\": \"negligible — removing 1 model changes nothing\",\n      \"architecture_heterogeneity_verdict\": \"non-issue for METABENCH MMLU\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Architecture Stratification Impact\",\n        \"columns\": [\n          \"population\",\n          \"n_models\",\n          \"c_pct\",\n          \"jaccard_vs_full\",\n          \"rmsea\"\n        ],\n        \"rows\": [\n          [\n            \"Full population\",\n            5227,\n            31.3,\n            \"—\",\n            0.031\n          ],\n          [\n            \"Decoder-only only\",\n            5226,\n            31.3,\n            1.0,\n            0.031\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"此实验在best档下是一行proactive defense。reviewer concern about architecture heterogeneity 在METABENCH MMLU上empirically无意义。paper中作为脚注或inline报告而非独立subsection。\\n\\n\\nbest档下architecture stratification结果trivial——METABENCH MMLU中99.98%(5226/5227) 是decoder-only，唯一的non-decoder模型移除后Jaccard=1.0，C%完全不变。 这是paper_framing中已记录的结果。IRT fit indices不变因为单个模型的移除对5227×12508 矩阵的统计量影响在numerical noise范围内。 best档下此结果是proactive defense against \\\"architecture heterogeneity inflates DIF\\\" reviewer concern的一行报告：METABENCH MMLU is architecturally homogeneous, concern is moot。\\n\"\n  },\n  {\n    \"name\": \"semi_synthetic_contamination_validation\",\n    \"description\": \"Real METABENCH response matrix上的known contamination injection：500 clean items选择、 100-200 items注入synthetic contamination(incorrect→correct flipping)、 controlled ground truth下的TPR/FPR测量、injection参数变化(prevalence, exploitation rate, focal group size)。\\n\",\n    \"results\": {\n      \"temporal_external_tpr_p0\": 0.326,\n      \"temporal_external_tpr_p03\": 0.548,\n      \"temporal_external_tpr_p05\": 0.834,\n      \"temporal_external_tpr_p07\": 0.99,\n      \"temporal_external_tpr_p10\": 1.0,\n      \"temporal_external_fpr\": 0.314,\n      \"temporal_external_delta_tpr_p05\": 0.508,\n      \"temporal_external_delta_tpr_p10\": 0.674,\n      \"ability_external_tpr_p10\": 0.8,\n      \"ability_external_fpr\": 0.493,\n      \"standard_mh_fpr_inflation\": \"0.298→0.616 at p=1.0\",\n      \"cross_subject_matching_fpr_stable\": true,\n      \"dose_response_monotonic\": true,\n      \"injection_n_items\": 200,\n      \"clean_baseline_n_items\": 500\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Semi-Synthetic Detection Power (Cross-Subject Matching)\",\n        \"columns\": [\n          \"exploitation_rate_p\",\n          \"tpr\",\n          \"delta_tpr\",\n          \"fpr\",\n          \"fpr_inflation\"\n        ],\n        \"rows\": [\n          [\n            \"0.0 (baseline)\",\n            0.326,\n            \"—\",\n            0.314,\n            0.0\n          ],\n          [\n            0.3,\n            0.548,\n            0.222,\n            0.314,\n            0.0\n          ],\n          [\n            0.5,\n            0.834,\n            0.508,\n            0.314,\n            0.0\n          ],\n          [\n            0.7,\n            0.99,\n            0.664,\n            0.314,\n            0.0\n          ],\n          [\n            1.0,\n            1.0,\n            0.674,\n            0.314,\n            0.0\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Matching Strategy Comparison at p=1.0\",\n        \"columns\": [\n          \"matching\",\n          \"tpr\",\n          \"fpr\",\n          \"delta_fpr_vs_baseline\"\n        ],\n        \"rows\": [\n          [\n            \"Standard (within-benchmark)\",\n            1.0,\n            0.616,\n            0.298\n          ],\n          [\n            \"Cross-subject (external)\",\n            1.0,\n            0.314,\n            0.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"semi-synthetic validation是paper中load-bearing experiment之一。ΔTPR=+0.508是Claim 2 的empirical anchor：如果DIF只检测\\\"noise\\\"，注入known contamination不应提升TPR。 cross-subject matching的ΔFPR=0.000(5个subjects全部)是Claim 3的practical innovation proof。 best档下此实验与plan_016(within-subject semi-synthetic)共同构成semi-synthetic framework 的完整validation story。\\n\\n\\nbest档下semi-synthetic validation的核心是ΔTPR=+0.508 at p=0.5——这证明DIF能检测 known differential contamination(注入的ground truth)。dose-response单调性(从p=0.3到p=1.0 TPR单调上升)确认检测力与exploitation rate成正比，排除了random artifact。 baseline FPR=0.314反映temporal cohort的genuine item-level DIF(与plan_001的31.3%一致)， 而非false positives——这些\\\"false\\\" positives实际上是真实的temporal instability。 cross-subject matching的FPR stability(vs standard matching的inflation至0.616) 是Claim 3的关键贡献：matching variable contamination是subtle but critical methodological issue。 best档下这些数字完美支撑三贡献结构中的Claim 2(semi-synthetic proves DIF detects what web-overlap labels cannot capture)和Claim 3(cross-subject matching as reusable infrastructure)。\\n\"\n  },\n  {\n    \"name\": \"multi_benchmark_temporal_dif\",\n    \"description\": \"METABENCH中额外benchmark(ARC-Challenge, HellaSwag, WinoGrande, TruthfulQA)的 temporal DIF分析，加上已完成的MMLU和GSM8K，共6个benchmark。\\n\",\n    \"results\": {\n      \"mmlu\": {\n        \"n_items\": 12508,\n        \"n_ref\": 1080,\n        \"n_foc\": 807,\n        \"pct_c\": 31.3,\n        \"random_pct_c\": 0.18,\n        \"bootstrap_ci_95\": [\n          29.38,\n          38.05\n        ]\n      },\n      \"winogrande\": {\n        \"n_items\": 1267,\n        \"n_ref\": 1017,\n        \"n_foc\": 803,\n        \"pct_c\": 30.3,\n        \"random_pct_c\": 0.32\n      },\n      \"truthfulqa\": {\n        \"n_items\": 817,\n        \"n_ref\": 1080,\n        \"n_foc\": 807,\n        \"pct_c\": 29.7,\n        \"random_pct_c\": 0.37\n      },\n      \"arc\": {\n        \"n_items\": 1172,\n        \"n_ref\": 1080,\n        \"n_foc\": 807,\n        \"pct_c\": 26.9,\n        \"random_pct_c\": 0.6\n      },\n      \"gsm8k\": {\n        \"n_items\": 1319,\n        \"n_ref\": 1017,\n        \"n_foc\": 804,\n        \"pct_c\": 18.9,\n        \"random_pct_c\": 0.3\n      },\n      \"hellaswag\": {\n        \"n_items\": 10042,\n        \"n_ref\": 1080,\n        \"n_foc\": 807,\n        \"pct_c\": 17.9,\n        \"random_pct_c\": 0.28\n      },\n      \"cross_benchmark_range\": \"17.9–31.3%\",\n      \"all_random_controls_below_1pct\": true,\n      \"min_enrichment_ratio_vs_random\": 45\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-Benchmark Temporal DIF Summary\",\n        \"columns\": [\n          \"benchmark\",\n          \"n_items\",\n          \"n_ref\",\n          \"n_foc\",\n          \"pct_c\",\n          \"random_pct_c\",\n          \"ratio\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            12508,\n            1080,\n            807,\n            31.3,\n            0.18,\n            \"174×\"\n          ],\n          [\n            \"WinoGrande\",\n            1267,\n            1017,\n            803,\n            30.3,\n            0.32,\n            \"95×\"\n          ],\n          [\n            \"TruthfulQA\",\n            817,\n            1080,\n            807,\n            29.7,\n            0.37,\n            \"80×\"\n          ],\n          [\n            \"ARC-Challenge\",\n            1172,\n            1080,\n            807,\n            26.9,\n            0.6,\n            \"45×\"\n          ],\n          [\n            \"GSM8K\",\n            1319,\n            1017,\n            804,\n            18.9,\n            0.3,\n            \"63×\"\n          ],\n          [\n            \"HellaSwag\",\n            10042,\n            1080,\n            807,\n            17.9,\n            0.28,\n            \"64×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"6-benchmark consistency(全部>15%、全部random<1%)是best档的strongest generalizability evidence。 range 17.9-31.3%在best档key metrics范围内(cross_benchmark_c_pct_min 17-20%, max 29-33%)。 此结果被审稿人视为充分跨benchmark证据，不需要additional benchmarks。\\n\\n\\nbest档下6 benchmark全部显示显著temporal DIF(17.9-31.3%)，所有random controls <1%。 C%的跨benchmark range反映benchmark结构差异：MMLU/WinoGrande/TruthfulQA(多domain/多题型) 的C%较高(29-31%)因为item heterogeneity提供更多DIF机会； GSM8K/HellaSwag(单domain或特定task)较低(17-19%)因为items更同质， differential functioning更多被ability matching吸收。 ARC(26.9%)居中。enrichment ratio(vs random)最低45×说明temporal DIF在所有benchmark 上都far above chance。best档下6-benchmark consistency是Claim 1 generalizability的核心证据， 直接回应\\\"only validated on MMLU\\\"的reviewer concern。\\n\"\n  },\n  {\n    \"name\": \"permutation_null_c_rate\",\n    \"description\": \"1000× permutation test：随机重分配2023/2024 temporal labels(保持group sizes N_ref=1080, N_foc=807)，每次运行MH-DIF，建立C%的null distribution。\\n\",\n    \"results\": {\n      \"n_permutations\": 1000,\n      \"null_c_pct_mean\": 0.21,\n      \"null_c_pct_sd\": 0.05,\n      \"null_c_pct_max\": 0.42,\n      \"null_c_pct_p95\": 0.3,\n      \"null_c_pct_p99\": 0.36,\n      \"observed_c_pct\": 31.3,\n      \"permutation_p_value\": \"<0.001\",\n      \"z_score_observed_vs_null\": \">600\",\n      \"null_distribution_shape\": \"approximately normal, centered near random-split control\",\n      \"consistency_with_random_split\": true,\n      \"random_split_c_pct\": 0.18,\n      \"computation_time_hours\": 12\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Permutation Null Distribution Summary\",\n        \"columns\": [\n          \"statistic\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"Observed C%\",\n            31.3\n          ],\n          [\n            \"Null mean C%\",\n            0.21\n          ],\n          [\n            \"Null SD\",\n            0.05\n          ],\n          [\n            \"Null max (1000 perms)\",\n            0.42\n          ],\n          [\n            \"Permutation p-value\",\n            \"<0.001\"\n          ],\n          [\n            \"z-score\",\n            \">600\"\n          ],\n          [\n            \"Random-split control C%\",\n            0.18\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Permutation null是Claim 1最直接的statistical significance evidence。 null mean 0.21%与random split 0.18%的一致性(差异0.03pp)说明两种null estimation converge。 observed 31.3%在null的>600σ之外——这不是marginal significance，而是absolute certainty that temporal DIF is real。best档下审稿人无法质疑\\\"31% is chance level\\\"。 此实验落在best档key metrics范围内(permutation_null_c_pct [0.0, 1.0])。\\n\\n\\nbest档下permutation null的mean C%=0.21%与within-cohort random split(0.18%)高度一致—— 这是预期的，因为random label permutation破坏temporal信号后，MH-DIF只能检测到 random fluctuation，与random split在概率上等价。null C% max=0.42%说明1000次permutation 中最极端的case也远低于observed 31.3%。z>600意味着observed值在null distribution的 >600个标准差之外，permutation p<0.001(实际上是p<1/1000因为0/1000 permutations达到31.3%)。 best档下此结果直接回答\\\"is 31% above chance?\\\"——答案是overwhelming yes。 null distribution的near-normal shape和consistency with random split互相验证了两种 null estimation方法的正确性。\\n\"\n  },\n  {\n    \"name\": \"odds_ratio_regression_transparency\",\n    \"description\": \"DIF flag的logistic regression透明度分析：odds ratio + 95% CI + 多种R²指标 + deviance ratio。 item-level finer-grained model (DIF flag ~ item-level accuracy change)补充domain-level分析。\\n\",\n    \"results\": {\n      \"model1_domain_delta\": {\n        \"mcfadden_r2\": 0.0007,\n        \"nagelkerke_r2\": 0.0012,\n        \"subject_acc_delta_or_per_010\": 1.55,\n        \"subject_acc_delta_ci_per_010\": [\n          1.19,\n          2.03\n        ]\n      },\n      \"model2_domain_delta_plus_items\": {\n        \"mcfadden_r2\": 0.0423,\n        \"nagelkerke_r2\": 0.072,\n        \"subject_acc_delta_or_per_010\": 0.73,\n        \"ctt_discrimination_or_per_010\": 1.51\n      },\n      \"model3_item_delta\": {\n        \"mcfadden_r2\": 0.0012,\n        \"nagelkerke_r2\": 0.0021,\n        \"item_acc_change_or_per_010\": 1.08,\n        \"item_acc_change_ci\": [\n          1.51,\n          2.96\n        ]\n      },\n      \"model4_item_delta_plus_items\": {\n        \"mcfadden_r2\": 0.0434,\n        \"nagelkerke_r2\": 0.0737,\n        \"item_acc_change_or_per_010\": 0.92,\n        \"ctt_discrimination_or_per_010\": 1.54\n      },\n      \"simpsons_paradox\": true,\n      \"lr_test_m1_vs_m2_chi2\": 646.98,\n      \"lr_test_m3_vs_m4_chi2\": 655.53\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Logistic Regression Models for DIF Flag Prediction\",\n        \"columns\": [\n          \"model\",\n          \"predictors\",\n          \"mcfadden_r2\",\n          \"nagelkerke_r2\",\n          \"key_or\"\n        ],\n        \"rows\": [\n          [\n            \"Model 1\",\n            \"subject_acc_Δ\",\n            0.0007,\n            0.0012,\n            \"1.55 [1.19,2.03]\"\n          ],\n          [\n            \"Model 2\",\n            \"subject_acc_Δ + item_props\",\n            0.0423,\n            0.072,\n            \"0.73 (reversed)\"\n          ],\n          [\n            \"Model 3\",\n            \"item_acc_Δ\",\n            0.0012,\n            0.0021,\n            \"1.08 [1.51,2.96]\"\n          ],\n          [\n            \"Model 4\",\n            \"item_acc_Δ + item_props\",\n            0.0434,\n            0.0737,\n            \"0.92 (reversed)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Simpson's paradox是this experiment的signature finding。Model 1作为primary(conservative, gives accuracy change its best shot at explaining DIF)，Model 2作为supplementary (shows the paradox)。审稿人看到R²<0.001 for accuracy change alone即可确信 \\\"31% is not just models getting better\\\"。dual interpretation explicitly acknowledged in Discussion。\\n\\nbest档下四个模型的R²全部极低(<0.08)，这是core finding而非limitation： accuracy change(无论domain-level还是item-level)解释DIF variance的能力极弱， 说明DIF捕获的是item-specific differential functioning而非aggregate accuracy improvement。 Simpson's paradox(Model 1中OR=1.55 per 0.10 accuracy change但Model 2/4中OR翻转至<1) 说明item properties(difficulty, discrimination)是confounders——controlling后accuracy change 的apparent effect消失甚至反转。best档下此结果是plan_019(decomposition: ≤2.4pp/7.6%) 的complementary evidence，用不同方法学(logistic regression vs item-level decomposition) converge on same conclusion。discrimination OR=1.54最具信息量：high-discrimination items 更容易被flag为DIF-C，因为它们对ability差异更敏感，微小的cohort composition差异就能触发large |Δ_MH|。\\n\"\n  }\n]",
      "numLines": 1182,
      "startLine": 1,
      "totalLines": 1182
    }
  },
  "sourceToolAssistantUUID": "7faebecb-2270-4db4-98e2-79f117a04ef8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T165710 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "e64e2c92-508c-49df-b7b9-6f27837041b9",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream_20260521T165710",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb"
}
```

---

### Assistant

_source line 14 · 2026-05-21T17:18:06.119Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full experiment data and paper framing. Let me also load the paper-writing-norms skill for guidance on writing style.

Let me plan the paper structure based on the framing:

The paper has 4 core claims:
1. ~31% of MMLU items are functionally unstable across model generations
2. Ground truth meta-critique: web-overlap labels can't validate item-level differential detectors
3. Semi-synthetic validation framework with cross-subject matching
4. DIF as diagnostic lens + actionable protocol

Main experiments to include:
1. `real_data_dif_mmlu` - Core temporal DIF analysis (Table 1, Table 2)


2. `multi_benchmark_temporal_dif` - Extending the analysis across 6 benchmarks (Table 3)
3. `permutation_null_c_rate` - Testing statistical significance (Table 4)
4. `odds_ratio_regression_transparency` - Breaking down domain improvements (Table 5)
5. `semi_synthetic_contamination_validation` - Validating with semi-synthetic data (Table 6, Table 7)
6. `cross_benchmark_gsm8k` - Replicating findings on GSM8K (Table 8)
7. `graceful_degradation_analysis` - Measuring downstream effects (Table 9)

I'll also need appendix experiments to support these core analyses. I'm mapping out the paper structure around the 8-page EMNLP limit, organizing the four main claims with their supporting experiments and deciding which analyses go in the appendix versus the main body. I'll use ACL formatting and need to figure out which experiments anchor each section—temporal DIF stability, benchmark consistency, the semi-synthetic validation framework, and robustness across perturbations. I'm mapping out the paper structure with all the key experiments and tables, then I'll start writing the LaTeX to bring this together while keeping it focused on the core claims without getting too bloated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e64e2c92-508c-49df-b7b9-6f27837041b9",
  "isSidechain": false,
  "requestId": "req_011CbG6S8cy58uBv7DL8dNpg",
  "type": "assistant",
  "uuid": "44b64d6d-1623-46a2-a106-45f3cf2c161d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TaCMGxr3uJyTihyEHsATRj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6232,
      "cache_creation_input_tokens": 18493,
      "cache_read_input_tokens": 24185,
      "output_tokens": 1214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18493,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6232,
          "output_tokens": 1214,
          "cache_read_input_tokens": 24185,
          "cache_creation_input_tokens": 18493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18493
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

_source line 15 · 2026-05-21T17:18:06.121Z_

Now let me read the paper-writing-norms skill for style guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44b64d6d-1623-46a2-a106-45f3cf2c161d",
  "isSidechain": false,
  "requestId": "req_011CbG6S8cy58uBv7DL8dNpg",
  "type": "assistant",
  "uuid": "fc62095d-a1f2-4f83-a8f7-a82092b6dd62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TaCMGxr3uJyTihyEHsATRj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6232,
      "cache_creation_input_tokens": 18493,
      "cache_read_input_tokens": 24185,
      "output_tokens": 1214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18493,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6232,
          "output_tokens": 1214,
          "cache_read_input_tokens": 24185,
          "cache_creation_input_tokens": 18493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18493
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

_source line 16 · 2026-05-21T17:18:06.175Z_

<details open><summary>🔧 Tool call — Read · `toolu_011LH2ehPLK5yR6SimbA8oN3`</summary>

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
  "parentUuid": "fc62095d-a1f2-4f83-a8f7-a82092b6dd62",
  "isSidechain": false,
  "requestId": "req_011CbG6S8cy58uBv7DL8dNpg",
  "type": "assistant",
  "uuid": "f4654a58-29e2-4332-be5e-2af5fc9641aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TaCMGxr3uJyTihyEHsATRj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6232,
      "cache_creation_input_tokens": 18493,
      "cache_read_input_tokens": 24185,
      "output_tokens": 1214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18493,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6232,
          "output_tokens": 1214,
          "cache_read_input_tokens": 24185,
          "cache_creation_input_tokens": 18493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18493
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

_source line 17 · 2026-05-21T17:18:06.183Z_

<details><summary>↩ Tool result · `toolu_011LH2ehPLK5yR6SimbA8oN3`</summary>

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
  "parentUuid": "f4654a58-29e2-4332-be5e-2af5fc9641aa",
  "isSidechain": false,
  "promptId": "fbb2aad3-deff-45fc-a21a-33870865ab9a",
  "type": "user",
  "uuid": "89ca94e2-4c0c-4f6c-9913-5c4de7d2fea2",
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
  "sourceToolAssistantUUID": "f4654a58-29e2-4332-be5e-2af5fc9641aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T17:18:10.693Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015PqUPybCkfFH5qczjx7Jqd`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89ca94e2-4c0c-4f6c-9913-5c4de7d2fea2",
  "isSidechain": false,
  "requestId": "req_011CbG6S8cy58uBv7DL8dNpg",
  "type": "assistant",
  "uuid": "41f3a2ba-ebb7-41d8-ac63-7f6388b2cbd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TaCMGxr3uJyTihyEHsATRj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6232,
      "cache_creation_input_tokens": 18493,
      "cache_read_input_tokens": 24185,
      "output_tokens": 1214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18493,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6232,
          "output_tokens": 1214,
          "cache_read_input_tokens": 24185,
          "cache_creation_input_tokens": 18493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18493
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

_source line 19 · 2026-05-21T17:18:10.867Z_

<details><summary>↩ Tool result · `toolu_015PqUPybCkfFH5qczjx7Jqd`</summary>

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
  "parentUuid": "41f3a2ba-ebb7-41d8-ac63-7f6388b2cbd5",
  "isSidechain": false,
  "promptId": "fbb2aad3-deff-45fc-a21a-33870865ab9a",
  "type": "user",
  "uuid": "6f929cce-019f-4ce0-ae30-81d338af40a5",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "41f3a2ba-ebb7-41d8-ac63-7f6388b2cbd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T17:22:25.408Z_

<details><summary>↩ Tool result · `toolu_01GsXjWAn8LiopHTnDKEzT2G`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33e10af5-82b3-462b-9f40-b9c31ab5176c",
  "isSidechain": false,
  "promptId": "fbb2aad3-deff-45fc-a21a-33870865ab9a",
  "type": "user",
  "uuid": "b9f9a9f0-ed71-4853-b17f-5459d784f8d6",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{geometry}\n\\geometry{margin=1in}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\newcommand{\\deltamh}{\\ensuremath{\\Delta_{\\text{MH}}}}\n\\newcommand{\\cpct}{\\ensuremath{C\\%}}\n\n\\title{Temporal Measurement Drift in LLM Benchmarks:\\\\A Large-Scale Differential Item Functioning Analysis}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nLarge Language Model (LLM) benchmarks implicitly assume temporal score comparability---that a score of 70\\% in 2024 reflects the same construct as 70\\% in 2023.\nWe test this assumption using Differential Item Functioning (DIF) analysis, a psychometric method that detects items whose difficulty changes across groups after controlling for overall ability.\nApplying Mantel--Haenszel DIF to the METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items), we find that \\textbf{31\\% of items} exhibit large temporal instability (ETS C classification, $|\\deltamh| \\geq 1.5$) between 2023 and 2024-H1 model cohorts---robust across six benchmarks (17.9--31.3\\%), all with random-split controls below 1\\%.\nItem-level decomposition shows domain-specific accuracy improvement explains at most 7.6\\% of this instability; the signal is predominantly item-specific.\nWe demonstrate that the field's standard ground truth---web-overlap contamination labels---measures global exposure rather than differential item functioning, yielding enrichment $\\approx$1.0 against DIF flags as theoretically expected.\nTo address this validation gap, we introduce a semi-synthetic framework that injects known differential contamination into real response matrices, with cross-subject matching that eliminates false positive inflation ($\\Delta$FPR\\,=\\,0.000).\nDespite 31\\% instability, benchmark rankings remain highly stable ($\\rho \\approx 0.997$), revealing massive measurement redundancy.\nDIF serves not as a quality filter but as a diagnostic lens for understanding what changed across model generations.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nWhen we report that ``Model B outperforms Model A on MMLU,'' we presume both scores reflect the same latent construct measured under comparable conditions.\nThis assumption of \\emph{temporal score comparability} is foundational to leaderboard rankings, model selection decisions, and progress narratives in NLP.\nYet benchmark items are static artifacts deployed in a rapidly evolving ecosystem: training corpora expand, data contamination pathways multiply, and model architectures shift---all of which can alter how individual items function across model generations.\n\nPsychometrics offers a mature framework for testing exactly this assumption: \\emph{Differential Item Functioning} (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability.\nAn item exhibits DIF when examinees of equal ability from different groups have different probabilities of answering correctly---signaling that the item measures something beyond the intended construct for at least one group.\nThe Mantel--Haenszel (MH) procedure, the most widely used DIF method in educational testing, provides both a statistical test and an effect-size measure ($\\deltamh$) with well-established classification thresholds.\n\nWe apply MH-DIF to the METABENCH response matrix---5,227 models $\\times$ 12,508 MMLU items---the largest-scale DIF analysis on LLM benchmarks to date.\nOur central finding is that \\textbf{31\\% of MMLU items are functionally unstable} across temporal model cohorts (2023 vs.\\ 2024-H1), classified as ETS C ($|\\deltamh| \\geq 1.5$).\nThis instability generalizes across six benchmarks (17.9--31.3\\%) and is robust to threshold choice, multiple testing correction, architecture composition, and ability-level confounds.\n\n\\paragraph{Instability $\\neq$ invalidity.}\nA critical interpretive point: DIF flags items whose \\emph{functioning changed} across generations---this is a diagnostic signal, not a quality verdict.\nWe show that MMLU rankings are massively redundant ($\\rho \\approx 0.997$ after removing all 31\\% flagged items), so instability does not threaten ranking validity.\nInstead, DIF reveals \\emph{which} capability dimensions are shifting across model generations, serving as a diagnostic lens rather than a quality filter.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n    \\item \\textbf{Large-scale temporal instability finding}: 31\\% of MMLU items exhibit large DIF across model generations, confirmed on six benchmarks (17.9--31.3\\%), with domain improvement explaining $\\leq$7.6\\% of the signal.\n    \\item \\textbf{Ground truth meta-critique}: Web-overlap contamination labels measure global exposure, not differential functioning. Enrichment $\\approx$1.0 against DIF flags is theoretically expected, not a failure. This affects the validity claims of all item-level detectors validated against web-overlap labels.\n    \\item \\textbf{Semi-synthetic validation framework}: A $\\Delta$TPR methodology with cross-subject matching ($\\Delta$FPR\\,=\\,0.000) that provides controlled validation for any item-level detector. Portable across benchmarks (GSM8K $\\Delta$TPR\\,=\\,+0.818).\n    \\item \\textbf{DIF as diagnostic lens}: DIF items carry genuine cross-cohort signal ($z$\\,=\\,$-$8 to $-$49$\\sigma$ vs.\\ random removal) but are the least disruptive non-random removal strategy ($z$\\,=\\,$-$9.5 vs.\\ accuracy-gap $z$\\,=\\,$-$157). We provide a concrete audit protocol for benchmark maintainers.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Benchmark contamination detection.}\nMethods for detecting data contamination in LLMs fall into several categories: membership inference via token-level statistics \\citep{shi2024detecting}, perturbation-based approaches that compare performance on original vs.\\ rephrased items \\citep{oren2024proving}, and overlap-based methods using n-gram matching between training data and benchmarks \\citep{li2024task}.\nThese approaches operate at the model level (testing individual models for contamination) and typically validate against web-overlap labels.\nOur work differs fundamentally: DIF operates at the item level across model populations, detecting \\emph{which items function differently} rather than \\emph{which models are contaminated}.\n\n\\paragraph{Benchmark reliability and validity.}\nRecent work has questioned benchmark reliability through various lenses: score instability under prompt perturbations \\citep{mizrahi2024state}, evaluation framework inconsistencies \\citep{polo2024tinybenchmarks}, and the general ``benchmark lottery'' phenomenon.\nOur psychometric approach complements these by providing item-level diagnostics grounded in established measurement theory.\n\n\\paragraph{DIF in educational testing.}\nDIF analysis has a 60-year history in educational and psychological testing \\citep{holland1993differential}.\nThe Mantel--Haenszel procedure \\citep{mantel1959statistical,holland1988alternate} remains the most widely used method due to its simplicity, robustness, and well-calibrated effect-size classifications (ETS A/B/C).\nWe apply this established methodology without modification; our contribution is the empirical findings and validation framework, not a new algorithm.\n\n\\paragraph{Psychometrics for LLM evaluation.}\nItem Response Theory (IRT) has been applied to LLM evaluation for efficient testing \\citep{polo2024tinybenchmarks} and characterizing item properties.\nOur work extends this psychometric lens to temporal comparability analysis, addressing a question that IRT alone cannot answer: whether items function \\emph{equivalently} across model cohorts.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Mantel--Haenszel DIF Analysis}\n\\label{sec:mh-dif}\n\nGiven a binary response matrix $\\mathbf{X} \\in \\{0,1\\}^{N \\times K}$ (models $\\times$ items), we partition models into a \\emph{reference group} (2023 cohort, $N_{\\text{ref}}=1{,}080$) and a \\emph{focal group} (2024-H1 cohort, $N_{\\text{foc}}=807$) based on release date.\nFor each item $k$, the MH procedure conditions on total score (sum of correct responses across all items) and computes the common odds ratio:\n\\begin{equation}\n    \\alpha_{\\text{MH},k} = \\frac{\\sum_j A_j D_j / T_j}{\\sum_j B_j C_j / T_j}\n\\end{equation}\nwhere $A_j, B_j, C_j, D_j$ are the entries of the $2\\times 2$ table at score stratum $j$, and $T_j$ is the stratum total.\nThe log-odds effect size on the ETS delta scale is $\\deltamh = -2.35 \\ln(\\alpha_{\\text{MH}})$.\n\nItems are classified using the ETS system: \\textbf{A} (negligible, $|\\deltamh| < 1.0$), \\textbf{B} (moderate, $1.0 \\leq |\\deltamh| < 1.5$), and \\textbf{C} (large, $|\\deltamh| \\geq 1.5$).\nC-classified items are our primary measure of temporal instability.\n\n\\subsection{Semi-Synthetic Validation Framework}\n\\label{sec:semi-synthetic}\n\nTo validate DIF detection power with known ground truth, we inject synthetic differential contamination into the real METABENCH response matrix:\n\\begin{enumerate}[leftmargin=*,nosep]\n    \\item Select 500 clean baseline items and 200 target items for injection.\n    \\item For each target item, flip incorrect$\\to$correct responses in the focal group with exploitation rate $p \\in \\{0.0, 0.3, 0.5, 0.7, 1.0\\}$.\n    \\item Run MH-DIF and measure True Positive Rate (TPR) and False Positive Rate (FPR).\n    \\item Report $\\Delta$TPR = TPR($p$) $-$ TPR($p$=0) as the detection power increase attributable to injected contamination.\n\\end{enumerate}\n\n\\subsection{Cross-Subject Matching}\n\\label{sec:cross-subject}\n\nStandard MH-DIF conditions on total score computed over all items including the tested item.\nWhen contamination inflates scores on tested items, this \\emph{matching variable contamination} biases the conditioning, inflating FPR.\nWe propose \\textbf{cross-subject matching}: for items in subject $s$, compute the matching variable as total score on all subjects \\emph{except} $s$.\nThis eliminates the feedback loop between contaminated items and the matching variable.\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\nAll analyses use the METABENCH response matrix.\nOur primary analysis focuses on MMLU (5,227 models $\\times$ 12,508 items across 57 subjects), with cross-benchmark replication on five additional benchmarks.\n\n\\subsection{Temporal DIF: 31\\% Instability Across Six Benchmarks}\n\\label{sec:temporal-dif}\n\n\\paragraph{MMLU results.}\nTable~\\ref{tab:temporal-dif} presents the core temporal DIF analysis.\nBetween the 2023 reference cohort ($N$=1,080) and 2024-H1 focal cohort ($N$=807), 31.3\\% of MMLU items are classified as ETS C (large DIF), with 16.3\\% as B (moderate) and 52.4\\% as A (negligible).\nThe random-split sanity check yields only 0.18\\% C-classified items, confirming the temporal signal is not a statistical artifact.\nThe ability-quintile split (high vs.\\ low ability, same time period) produces only 2.9\\% C items, demonstrating that DIF captures temporal rather than ability-driven differences.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temporal DIF summary (ETS classification). C\\% is the primary instability measure ($|\\deltamh| \\geq 1.5$). Random split serves as null control.}\n\\label{tab:temporal-dif}\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Split} & $N_{\\text{ref}}$ & $N_{\\text{foc}}$ & \\textbf{Items} & \\textbf{A\\%} & \\textbf{B\\%} & \\textbf{C\\%} & \\textbf{Rand.\\ C\\%} \\\\\n\\midrule\nTemporal & 1,080 & 807 & 12,508 & 52.4 & 16.3 & 31.3 & 0.18 \\\\\nAbility quintile & 1,044 & 1,044 & 12,508 & 85.2 & 11.9 & 2.9 & 0.15 \\\\\nWithin-family (Llama) & 161 & 308 & 12,508 & 24.1 & 14.6 & 61.3 & 0.22 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-benchmark generalization.}\nTable~\\ref{tab:cross-benchmark} shows temporal DIF across all six METABENCH benchmarks.\nEvery benchmark exhibits substantial instability (17.9--31.3\\% C), with all random controls below 1\\%.\nMulti-domain benchmarks (MMLU, WinoGrande, TruthfulQA) show higher C\\% (29.7--31.3\\%) than single-domain benchmarks (GSM8K 18.9\\%, HellaSwag 17.9\\%), consistent with greater item heterogeneity providing more opportunities for differential functioning.\nThe minimum enrichment ratio versus random is 45$\\times$, confirming temporal DIF far exceeds chance across all benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temporal DIF across six METABENCH benchmarks. All random controls are below 1\\%. Ratio = C\\% / Random C\\%.}\n\\label{tab:cross-benchmark}\n\\begin{tabular}{lrrrrrr}\n\\toprule\n\\textbf{Benchmark} & \\textbf{Items} & $N_{\\text{ref}}$ & $N_{\\text{foc}}$ & \\textbf{C\\%} & \\textbf{Rand.\\ C\\%} & \\textbf{Ratio} \\\\\n\\midrule\nMMLU & 12,508 & 1,080 & 807 & 31.3 & 0.18 & 174$\\times$ \\\\\nWinoGrande & 1,267 & 1,017 & 803 & 30.3 & 0.32 & 95$\\times$ \\\\\nTruthfulQA & 817 & 1,080 & 807 & 29.7 & 0.37 & 80$\\times$ \\\\\nARC-Challenge & 1,172 & 1,080 & 807 & 26.9 & 0.60 & 45$\\times$ \\\\\nGSM8K & 1,319 & 1,017 & 804 & 18.9 & 0.30 & 63$\\times$ \\\\\nHellaSwag & 10,042 & 1,080 & 807 & 17.9 & 0.28 & 64$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Permutation null distribution.}\nTo formally establish statistical significance, we run 1,000 permutations, randomly reassigning temporal labels while preserving group sizes.\nTable~\\ref{tab:permutation} summarizes the results: the null distribution has mean C\\%\\,=\\,0.21\\% ($\\text{SD}$\\,=\\,0.05\\%), consistent with the random-split control (0.18\\%).\nThe observed 31.3\\% lies $>$600$\\sigma$ above the null mean ($p < 0.001$), providing overwhelming evidence that temporal DIF is real.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Permutation null distribution (1,000 permutations) vs.\\ observed temporal DIF on MMLU.}\n\\label{tab:permutation}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Statistic} & \\textbf{Value} \\\\\n\\midrule\nObserved C\\% & 31.3 \\\\\nNull mean C\\% & 0.21 \\\\\nNull SD & 0.05 \\\\\nNull max (1,000 perms) & 0.42 \\\\\nPermutation $p$-value & $<$0.001 \\\\\n$z$-score & $>$600 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Domain specificity.}\nC\\% varies across MMLU subjects from 20.7\\% (computer security) to 48.4\\% (business ethics), with Spearman $\\rho$\\,=\\,0.307 ($p$\\,=\\,0.02) between subject-level C\\% and accuracy improvement.\nHowever, item-level decomposition (\\S\\ref{sec:confounds}) shows this modest ecological correlation overstates the actual contribution.\n\n\\subsection{Ruling Out Confounds}\n\\label{sec:confounds}\n\n\\paragraph{Domain improvement decomposition.}\nTable~\\ref{tab:regression} presents logistic regression models predicting DIF flag status from accuracy change and item properties.\nModel 1 (subject-level accuracy change only) yields pseudo $R^2$\\,=\\,0.0007---domain improvement explains essentially none of the DIF variance.\nThe odds ratio of 1.55 per 0.10 accuracy increase reverses to 0.73 in Model 2 when item properties (difficulty, discrimination) are added, exhibiting Simpson's paradox: the apparent domain-level association vanishes once item-level properties are controlled.\nItem-level accuracy change (Model 3) produces similarly negligible explanatory power ($R^2$\\,=\\,0.0012).\nCTT discrimination emerges as the strongest predictor (OR\\,=\\,1.54 per 0.10 unit), indicating high-discrimination items are more likely to be flagged---consistent with DIF theory, as these items are more sensitive to any cohort composition differences.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Logistic regression predicting DIF C flag. OR = odds ratio per 0.10 unit increase.}\n\\label{tab:regression}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Predictors} & \\textbf{McFadden $R^2$} & \\textbf{Nagelkerke $R^2$} & \\textbf{Key OR} \\\\\n\\midrule\nM1 & subject acc.\\ $\\Delta$ & 0.0007 & 0.0012 & 1.55 [1.19, 2.03] \\\\\nM2 & + item properties & 0.0423 & 0.072 & 0.73 (reversed) \\\\\nM3 & item acc.\\ $\\Delta$ & 0.0012 & 0.0021 & 1.08 [1.51, 2.96] \\\\\nM4 & + item properties & 0.0434 & 0.074 & 0.92 (reversed) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Architecture homogeneity.}\nMETABENCH MMLU is 99.98\\% decoder-only (5,226/5,227 models).\nExcluding the single non-decoder-only model produces identical C\\% (31.3\\%) with Jaccard\\,=\\,1.0 against the full-population analysis, confirming architecture heterogeneity is a non-issue.\n\n\\subsection{Ground Truth Meta-Critique}\n\\label{sec:meta-critique}\n\nExisting contamination detection methods validate against web-overlap labels---binary indicators of whether benchmark items appear in web-crawled training data.\nWe argue these labels measure \\emph{global exposure} (an item is publicly accessible), not \\emph{differential contamination} (an item functions differently across model cohorts).\nThese are orthogonal constructs: an item can be web-exposed yet function identically across cohorts (no DIF), or be non-exposed yet function differently due to indirect learning pathways.\n\nWe test this directly: DIF enrichment against Li et al.\\ web-overlap labels on 9,229 MMLU items yields enrichment\\,=\\,0.964 (Jaccard\\,=\\,0.206, $\\phi$\\,=\\,0.012, $\\chi^2$\\,=\\,1.28, $p$\\,=\\,0.258).\nThis near-unity enrichment is \\emph{expected}, not a failure---it confirms the theoretical orthogonality.\nThe implication is field-wide: any item-level detector validated solely against web-overlap labels (including Min-K\\%, ConStat, n-gram methods) has this blind spot.\nSemi-synthetic validation (\\S\\ref{sec:semi-synthetic-results}) provides a controlled alternative.\n\n\\subsection{Semi-Synthetic Validation}\n\\label{sec:semi-synthetic-results}\n\n\\paragraph{Detection power with known ground truth.}\nTable~\\ref{tab:semi-synthetic} presents semi-synthetic validation results using cross-subject matching.\nAt baseline ($p$\\,=\\,0.0), TPR\\,=\\,0.326 reflects the real temporal DIF signal (consistent with the 31.3\\% C\\% finding).\nAs exploitation rate increases, $\\Delta$TPR rises monotonically: +0.222 at $p$\\,=\\,0.3, +0.508 at $p$\\,=\\,0.5, reaching +0.674 at $p$\\,=\\,1.0.\nThis dose--response relationship confirms DIF detects injected differential contamination with increasing power.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Semi-synthetic detection power using cross-subject matching. $\\Delta$TPR measures detection power attributable to injected contamination (200 items injected into real METABENCH matrix).}\n\\label{tab:semi-synthetic}\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Exploitation rate $p$} & \\textbf{TPR} & $\\boldsymbol{\\Delta}$\\textbf{TPR} & \\textbf{FPR} & \\textbf{FPR inflation} \\\\\n\\midrule\n0.0 (baseline) & 0.326 & --- & 0.314 & 0.000 \\\\\n0.3 & 0.548 & +0.222 & 0.314 & 0.000 \\\\\n0.5 & 0.834 & +0.508 & 0.314 & 0.000 \\\\\n0.7 & 0.990 & +0.664 & 0.314 & 0.000 \\\\\n1.0 & 1.000 & +0.674 & 0.314 & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-subject matching eliminates FPR inflation.}\nTable~\\ref{tab:matching} compares matching strategies at maximum exploitation ($p$\\,=\\,1.0).\nStandard within-benchmark matching inflates FPR from 0.314 to 0.616 (+0.298) because contaminated items inflate the conditioning variable.\nCross-subject matching maintains FPR at 0.314 with zero inflation across all five tested subjects, validating our methodological contribution.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Matching strategy comparison at $p$\\,=\\,1.0 (full exploitation).}\n\\label{tab:matching}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Matching strategy} & \\textbf{TPR} & \\textbf{FPR} & $\\boldsymbol{\\Delta}$\\textbf{FPR vs.\\ baseline} \\\\\n\\midrule\nStandard (within-benchmark) & 1.000 & 0.616 & +0.298 \\\\\nCross-subject (external) & 1.000 & 0.314 & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-benchmark portability: GSM8K.}\nTable~\\ref{tab:gsm8k} summarizes the three-step GSM8K validation.\nThe framework successfully transfers: temporal C\\%\\,=\\,18.9\\% (lower than MMLU, consistent with single-domain structure), semi-synthetic $\\Delta$TPR\\,=\\,+0.818 (standard matching).\nThe GSM1K external validation yields $r$\\,=\\,$-$0.478 ($p$\\,=\\,0.005, $N$\\,=\\,33)---DIF flags \\emph{anti-correlate} with contamination gaps.\nThis negative correlation, while based on a small sample and wide confidence intervals, suggests DIF on GSM8K captures capability-driven rather than contamination-driven item functioning changes.\nWe report this as exploratory evidence, not a core claim.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{GSM8K three-step validation (1,319 items $\\times$ 6,702 models).}\n\\label{tab:gsm8k}\n\\begin{tabular}{llcl}\n\\toprule\n\\textbf{Step} & \\textbf{Metric} & \\textbf{Value} & \\textbf{Interpretation} \\\\\n\\midrule\n1 & Temporal C\\% & 18.9\\% & Lower than MMLU (single-domain) \\\\\n1 & Sanity C\\% & 0.3\\% & Well below temporal signal \\\\\n2 & $\\Delta$TPR ($p$\\,=\\,1.0) & +0.818 & Framework portable to math \\\\\n3 & Pearson $r$ vs.\\ GSM1K & $-$0.478 & DIF $\\neq$ contamination (exploratory) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Downstream Impact: Instability $\\neq$ Invalidity}\n\\label{sec:downstream}\n\n\\paragraph{Graceful degradation under item replacement.}\nTable~\\ref{tab:degradation} shows benchmark validity metrics under progressive replacement of DIF-flagged items.\nEven at 31\\% replacement (matching the observed C\\%), ranking correlation remains $\\rho$\\,=\\,0.990, reliability $\\alpha$\\,=\\,0.935, and construct coverage 0.89.\nAt 50\\% replacement, all metrics remain within acceptable ranges ($\\rho$\\,=\\,0.978, $\\alpha$\\,=\\,0.912).\nThe theoretical bound $\\rho \\geq 1 - 0.45r$ (where $r$ is the replacement fraction) fits the empirical data with correlation 0.994, indicating degradation is predictable and manageable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Benchmark validity metrics under progressive DIF item replacement on MMLU.}\n\\label{tab:degradation}\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{Replacement \\%} & \\textbf{Ranking $\\rho$} & \\textbf{Reliability $\\alpha$} & \\textbf{Construct coverage} \\\\\n\\midrule\n0 & 1.000 & 0.972 & 1.00 \\\\\n5 & 0.999 & 0.968 & 0.98 \\\\\n10 & 0.997 & 0.961 & 0.96 \\\\\n20 & 0.993 & 0.948 & 0.93 \\\\\n31 & 0.990 & 0.935 & 0.89 \\\\\n50 & 0.978 & 0.912 & 0.85 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{DIF as diagnostic lens, not quality filter.}\nDIF items carry genuine cross-cohort signal: removing DIF-flagged items causes significantly more ranking disruption than random removal ($z$\\,=\\,$-$8 to $-$49$\\sigma$ across 21 conditions).\nHowever, circularity ablation reveals DIF is the \\emph{least} disruptive non-random strategy: accuracy-gap removal disrupts 10--16$\\times$ more ($z$\\,=\\,$-$157), high-variance removal 11$\\times$ more ($z$\\,=\\,$-$108), and high-discrimination removal 1.7$\\times$ more ($z$\\,=\\,$-$16).\nThe MH procedure's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items.\nDIF-discrimination overlap is only 22.1\\% (Jaccard\\,=\\,0.12)---DIF identifies ``items that changed across generations,'' not ``good measurement items.''\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Implications for benchmark maintenance.}\nOur findings suggest a practical audit protocol for benchmark maintainers.\nItems with persistent C-level DIF across multiple cohort definitions warrant investigation---not automatic removal, but diagnostic attention.\nThe graceful degradation results (\\S\\ref{sec:downstream}) show that targeted replacement is safe: even replacing all 31\\% flagged items preserves ranking validity ($\\rho$\\,=\\,0.990).\nThe massive measurement redundancy in MMLU (12,508 items, $\\rho$\\,$\\approx$\\,0.997 under 31\\% removal) provides a large safety margin for item rotation.\n\n\\paragraph{What drives the instability?}\nDIF-C items are moderately harder (Cohen's $d$\\,=\\,$-$0.247) and higher-discrimination ($d$\\,=\\,0.230) than non-DIF items, but uniformly distributed across domains ($\\chi^2$ $p$\\,=\\,0.32).\nA striking difficulty $\\times$ direction interaction ($\\rho$\\,=\\,$-$0.597) reveals a systematic pattern: hardest-decile DIF items are 88.7\\% focal-favoring (2024 models perform better), while easiest-decile items are 96.2\\% reference-favoring (2023 models perform better).\nThis suggests capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n\n\\paragraph{Complementarity with existing approaches.}\nDIF and contamination detectors (Min-K\\%, ConStat) address different questions.\nContamination detectors ask ``has this model seen this item?'' (model-level, individual diagnosis).\nDIF asks ``does this item function differently across model generations?'' (item-level, population diagnosis).\nThe web-overlap enrichment $\\approx$1.0 confirms these are orthogonal signals, not competing methods.\nBenchmark maintainers should use both: DIF for population-level item auditing, contamination detectors for individual model vetting.\n\n% ============================================================\n\\section*{Limitations}\n\n\\begin{enumerate}[leftmargin=*,nosep]\n    \\item \\textbf{Unidimensional IRT misspecification.} MH-DIF assumes unidimensional ability, but MMLU spans 57 subjects. Bifactor analysis (Appendix~\\ref{app:bifactor}) confirms the general factor explains only 31\\% of variance. Future work should explore multidimensional IRT and MIMIC models for more principled conditioning.\n    \\item \\textbf{Semi-synthetic simplification.} Our injection mechanism (incorrect$\\to$correct flipping) models one contamination pathway. Real contamination may produce subtler response pattern changes. The framework's value lies in providing \\emph{any} controlled ground truth where none existed before.\n    \\item \\textbf{Temporal cohort definition.} Our 2023/2024-H1 binary split is a simplification; model release dates are noisy proxies for training data cutoffs. Item-Focused Trees analysis (Appendix~\\ref{app:ift}) using continuous release dates yields similar results (34\\% detection rate, Jaccard\\,=\\,0.81 with MH).\n\\end{enumerate}\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first large-scale DIF analysis of LLM benchmarks, revealing that 31\\% of MMLU items are temporally unstable across model generations---a finding that generalizes across six benchmarks (17.9--31.3\\%).\nThis instability is predominantly item-specific (domain improvement explains $\\leq$7.6\\%), does not threaten ranking validity ($\\rho$\\,$\\approx$\\,0.997), and is invisible to the field's standard web-overlap ground truth (enrichment\\,$\\approx$\\,1.0).\nOur semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR\\,=\\,0.000) provides reusable infrastructure for validating any item-level detection method.\nDIF serves as a diagnostic lens---revealing what changed across model generations---not a quality filter, with direct implications for benchmark maintenance practices.\n\n% ============================================================\n\\appendix\n\n\\section{RL Robustness}\n\\label{app:rl}\n\nWe evaluate DIF stability when reasoning-RL models (GRPO/PPO-trained) are added to the focal cohort.\nTable~\\ref{tab:rl-stability} shows DIF C\\% changes minimally: from 31.3\\% (SFT-only baseline) to 30.8\\% when 13 reasoning-RL models are mixed into the 820-model focal cohort.\nJaccard similarity between flagged item sets remains $\\geq$0.92, and TOST equivalence testing (margin\\,=\\,0.05) confirms non-degradation ($p$\\,=\\,0.003).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DIF stability across training paradigms. CI = 95\\% bootstrap confidence interval.}\n\\label{tab:rl-stability}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Focal cohort} & $N_{\\text{foc}}$ & \\textbf{C\\%} & \\textbf{Jaccard vs.\\ SFT} & \\textbf{Bootstrap CI} \\\\\n\\midrule\nSFT-only (baseline) & 807 & 31.3 & --- & --- \\\\\nAlignment-RL (DPO/ORPO) & 477 & 31.1 & 0.94 & [0.92, 0.96] \\\\\nSFT + Reasoning-RL mixed & 820 & 30.8 & 0.92 & [0.90, 0.96] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn contrast, traditional detectors degrade substantially on reasoning-RL models (Table~\\ref{tab:rl-detectors}): Min-K\\% AUROC drops from 0.72 to 0.48 ($\\Delta$\\,=\\,$-$0.24, DeLong $p$\\,=\\,0.001), and ConStat from 0.68 to 0.51 ($\\Delta$\\,=\\,$-$0.17, $p$\\,=\\,0.008).\nDIF's group-level design is naturally immune to individual-model signal perturbation from RL training.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Traditional detector degradation on reasoning-RL models.}\n\\label{tab:rl-detectors}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Detector} & \\textbf{AUROC (SFT)} & \\textbf{AUROC (RL)} & $\\boldsymbol{\\Delta}$ & \\textbf{DeLong $p$} \\\\\n\\midrule\nMin-K\\% & 0.72 & 0.48 & $-$0.24 & 0.001 \\\\\nConStat & 0.68 & 0.51 & $-$0.17 & 0.008 \\\\\nDIF (group) & --- & --- & Jaccard\\,=\\,0.92 & TOST $p$\\,=\\,0.003 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{ConStat Perturbation Evaluation}\n\\label{app:constat}\n\nWe independently evaluate ConStat-style perturbation testing on 250 LLM-paraphrased MMLU items across 50 models.\nTable~\\ref{tab:constat} shows detection power decreasing from 0.38 (SFT) to 0.31 (alignment-RL) to 0.14 (reasoning-RL) at $\\delta \\geq 0.6$ effect-size threshold, with FPR controlled at $\\sim$0.05.\nThe 63\\% drop in reasoning-RL detection power reflects GRPO/PPO training generalizing problem-solving ability rather than memorizing verbatim items, erasing the original-vs-paraphrased performance gap that ConStat relies on.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{ConStat detection power by training paradigm ($\\delta \\geq 0.6$, FDR $q$\\,=\\,0.05).}\n\\label{tab:constat}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Paradigm} & $N_{\\text{models}}$ & \\textbf{Detection rate} & \\textbf{FPR} \\\\\n\\midrule\nSFT-only & 25 & 0.38 & 0.048 \\\\\nAlignment-RL & 15 & 0.31 & 0.045 \\\\\nReasoning-RL & 10 & 0.14 & 0.051 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{DVD Generation Variance Evaluation}\n\\label{app:dvd}\n\nWe evaluate Detection via generation Variance and Difficulty (DVD) on 500 MMLU items across 12 models with 50 temperature-sampled generations per item ($T$\\,=\\,0.8).\nTable~\\ref{tab:dvd} shows DVD performs better on variant contamination (AUROC\\,=\\,0.74) than verbatim (AUROC\\,=\\,0.61), because variant contamination produces bimodal generation variance.\nFPR is 0.065.\nThe 68 GPU-hours computational cost contrasts with DIF's zero-GPU design.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DVD detection power by contamination type (12 models, 500 items, 50 generations each).}\n\\label{tab:dvd}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Contamination type} & \\textbf{AUROC} & \\textbf{Detection rate} & \\textbf{FPR} \\\\\n\\midrule\nVerbatim & 0.61 & 0.22 & 0.065 \\\\\nVariant & 0.74 & 0.45 & 0.065 \\\\\nClean & --- & --- & 0.065 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Ensemble Fusion}\n\\label{app:ensemble}\n\nTable~\\ref{tab:ensemble} evaluates DIF + ConStat + DVD fusion.\nWeighted fusion achieves AUROC\\,=\\,0.93 and TPR\\,=\\,0.82 at FPR\\,$<$\\,0.05, exceeding any individual detector.\nCross-validated weights assign DIF the highest weight (0.52), reflecting its cross-paradigm consistency.\nEnsemble performance is robust to weight choice (uniform vs.\\ optimized AUC gap\\,=\\,0.03).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Ensemble vs.\\ individual detector performance.}\n\\label{tab:ensemble}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{TPR @ FPR 0.05} & \\textbf{AUROC} & \\textbf{Coverage} \\\\\n\\midrule\nDIF (MH) & 0.68 & 0.87 & All paradigms \\\\\nConStat & 0.55 & 0.76 & Non-RL only \\\\\nDVD & 0.42 & 0.71 & Variant only \\\\\nEnsemble (majority) & 0.78 & 0.91 & All \\\\\nEnsemble (weighted) & 0.82 & 0.93 & All \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Bifactor IRT Equating Pilot}\n\\label{app:bifactor}\n\nWe fit a bifactor IRT model (general factor + 57 subject-specific factors) to validate unidimensionality assumptions.\nTable~\\ref{tab:bifactor} shows marginal fit: RMSEA\\,=\\,0.028 (pass) and SRMR\\,=\\,0.045 (pass), but CFI\\,=\\,0.91 and TLI\\,=\\,0.89 fall below the 0.95 standard.\nThe general factor explains only 31\\% of variance, confirming MMLU's fundamental multidimensionality.\nDespite marginal fit, equated scores correlate at $\\rho$\\,=\\,0.97, suggesting equating is workable even under model misspecification.\nThis motivates future multidimensional IRT work.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Bifactor IRT model fit indices for MMLU (12,508 items, 57 subject factors).}\n\\label{tab:bifactor}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Index} & \\textbf{Value} & \\textbf{Threshold} & \\textbf{Verdict} \\\\\n\\midrule\nRMSEA & 0.028 & $<$0.06 & Pass \\\\\nCFI & 0.91 & $>$0.95 & Marginal \\\\\nTLI & 0.89 & $>$0.95 & Marginal \\\\\nSRMR & 0.045 & $<$0.08 & Pass \\\\\nGeneral $\\omega$ & 0.31 & $>$0.50 & Fail \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Item Generation Calibration}\n\\label{app:item-gen}\n\nWe generate 500 replacement items for 200 DIF-flagged MMLU items using Claude 3.5 Sonnet.\nTable~\\ref{tab:item-gen} compares prompt-only targeting vs.\\ student simulation calibration.\nStudent simulation improves difficulty correlation from $\\rho$\\,=\\,0.32 to 0.71 and holdout validation from 0.28 to 0.65, approaching but not reaching the 0.75--0.82 literature benchmark.\nThis confirms item generation is feasible but not yet reliable enough for automated benchmark regeneration.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Item generation calibration accuracy (500 items, 200 DIF-targeted).}\n\\label{tab:item-gen}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Difficulty $\\rho$} & \\textbf{Cognitive match} & \\textbf{Holdout $\\rho$} \\\\\n\\midrule\nPrompt-only & 0.32 & 0.65 & 0.28 \\\\\nStudent simulation & 0.71 & 0.78 & 0.65 \\\\\nLiterature benchmark & 0.75--0.82 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Cumulative Bayesian DIF}\n\\label{app:bayesian}\n\nFollowing Sinharay et al.\\ (2006), we simulate cumulative Bayesian DIF monitoring across successive benchmark administrations.\nTable~\\ref{tab:bayesian} shows detection power increasing from 0.42 (single administration) to 0.78 (four administrations) at $\\delta$\\,=\\,1.0, with FPR decreasing from 0.041 to 0.033 due to prior shrinkage.\nAt the operational effect size $\\delta$\\,=\\,1.4, three administrations achieve 0.85 power.\nThis supports a longitudinal monitoring protocol where items below the single-administration decision threshold accumulate evidence over time.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cumulative Bayesian DIF power by number of administrations (500 items, 200 models/admin).}\n\\label{tab:bayesian}\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Administrations} & \\textbf{Power ($\\delta$=1.0)} & \\textbf{Power ($\\delta$=1.4)} & \\textbf{Power ($\\delta$=1.6)} & \\textbf{FPR} \\\\\n\\midrule\n1 & 0.42 & 0.68 & 0.72 & 0.041 \\\\\n2 & 0.58 & 0.79 & 0.84 & 0.038 \\\\\n3 & 0.71 & 0.85 & 0.90 & 0.035 \\\\\n4 & 0.78 & 0.89 & 0.93 & 0.033 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Item-Focused Trees}\n\\label{app:ift}\n\nAs a robustness check, we apply Item-Focused Trees (IFT; Tutz \\& Berger, 2016), which treat model release date as a continuous covariate rather than a binary split.\nTable~\\ref{tab:ift} shows IFT detection rate (34.0\\%) is close to MH (31.3\\%), with Jaccard\\,=\\,0.81 concordance.\nIFT detects 412 items missed by MH (gradual drift patterns), while MH detects 287 items missed by IFT.\nThe IFT split-point mode at 2023-Q4 aligns with our temporal cohort boundary.\n856 items show nonlinear drift (difficulty changes non-monotonically over time), a pattern invisible to binary DIF.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Item-Focused Trees (continuous) vs.\\ MH-DIF (categorical) on MMLU (12,508 items).}\n\\label{tab:ift}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Detection rate} & \\textbf{Unique items} & \\textbf{Computation (hrs)} \\\\\n\\midrule\nMH-DIF (categorical) & 31.3\\% & 287 & 0.5 \\\\\nIFT (continuous) & 34.0\\% & 412 & 8.0 \\\\\nOverlap (both) & --- & Jaccard\\,=\\,0.81 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Holland and Thayer(1988)]{holland1988alternate}\nP.~W. Holland and D.~T. Thayer.\n\\newblock Differential item performance and the Mantel--Haenszel procedure.\n\\newblock In H.~Wainer and H.~I. Braun, editors, \\emph{Test Validity}, pages 129--145. Lawrence Erlbaum, 1988.\n\n\\bibitem[Holland and Wainer(1993)]{holland1993differential}\nP.~W. Holland and H.~Wainer, editors.\n\\newblock \\emph{Differential Item Functioning}.\n\\newblock Lawrence Erlbaum Associates, 1993.\n\n\\bibitem[Li et~al.(2024)]{li2024task}\nY.~Li, et~al.\n\\newblock Task contamination: Language models may not be few-shot anymore.\n\\newblock In \\emph{Proceedings of AAAI}, 2024.\n\n\\bibitem[Mantel and Haenszel(1959)]{mantel1959statistical}\nN.~Mantel and W.~Haenszel.\n\\newblock Statistical aspects of the analysis of data from retrospective studies of disease.\n\\newblock \\emph{Journal of the National Cancer Institute}, 22(4):719--748, 1959.\n\n\\bibitem[Mizrahi et~al.(2024)]{mizrahi2024state}\nM.~Mizrahi, et~al.\n\\newblock State of what art? A call for multi-prompt LLM evaluation.\n\\newblock \\emph{Transactions of the ACL}, 2024.\n\n\\bibitem[Oren et~al.(2024)]{oren2024proving}\nY.~Oren, et~al.\n\\newblock Proving test set contamination in black box language models.\n\\newblock In \\emph{Proceedings of ICLR}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo, et~al.\n\\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.\n\\newblock In \\emph{Proceedings of ICML}, 2024.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nW.~Shi, et~al.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{Proceedings of ICLR}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "33e10af5-82b3-462b-9f40-b9c31ab5176c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-21T17:18:25.582Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have all the information I need. Let me write the full LaTeX paper.

The paper structure:
- Abstract
- Introduction (with "instability ≠ invalidity" framing upfront)
- Related Work (brief)
- Method (MH-DIF, semi-synthetic, cross-subject matching)
- Experiments:
  - 4.1 Temporal Measurement Drift (real_data_dif_mmlu, multi_benchmark_temporal_dif, permutation_null_c_rate)
  - 4.2 Ruling Out Confounds (odds_ratio_regression_transparency, architecture_stratified_dif)
  - 4.3 Ground Truth Meta-Critique (enrichment data from real_data_dif_mmlu)
  - 4.4 Semi-Synthetic Validation (semi_synthetic_contamination_validation, cross_benchmark_gsm8k)
  - 4.5 Downstream Impact (graceful_degradation_analysis)
- Discussion + Limitations
- Conclusion
- Appendix (RL robustness, ConStat, DVD, ensemble, bifactor, item generation)

Now I'm mapping out the table structure for the paper. I need to create a dedicated table for each major experiment—starting with the temporal DIF results on MMLU, then cross-benchmark comparisons, permutation null distributions, logistic regression coefficients, semi-synthetic detection power and matching comparisons, and finally the GSM8K validation results.

For the appendix, I'm planning nine additional tables covering robustness checks, alternative detection methods like ConStat and DVD, ensemble approaches, bifactor IRT, item generation calibration, Bayesian DIF, and item-focused trees. That's sixteen tables total across the main paper and appendix. Now I'll start writing the paper using a standard academic structure.

Writing LaTeX document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f929cce-019f-4ce0-ae30-81d338af40a5",
  "isSidechain": false,
  "requestId": "req_011CbG6U5QnvXrPLTePzUape",
  "type": "assistant",
  "uuid": "a51d6452-4b24-4422-983b-bb9eec13daec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1GokuL5r7xGqCoS6JuT7r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9496,
      "cache_read_input_tokens": 42678,
      "output_tokens": 13971,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13971,
          "cache_read_input_tokens": 42678,
          "cache_creation_input_tokens": 9496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9496
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

_source line 22 · 2026-05-21T17:18:25.584Z_

Now I have all the data. Let me write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a51d6452-4b24-4422-983b-bb9eec13daec",
  "isSidechain": false,
  "requestId": "req_011CbG6U5QnvXrPLTePzUape",
  "type": "assistant",
  "uuid": "7589e6ff-96f6-4178-bb69-4d37a808a2d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1GokuL5r7xGqCoS6JuT7r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9496,
      "cache_read_input_tokens": 42678,
      "output_tokens": 13971,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13971,
          "cache_read_input_tokens": 42678,
          "cache_creation_input_tokens": 9496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9496
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

_source line 23 · 2026-05-21T17:22:25.379Z_

<details open><summary>🔧 Tool call — Write · `toolu_01GsXjWAn8LiopHTnDKEzT2G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{geometry}\n\\geometry{margin=1in}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\newcommand{\\deltamh}{\\ensuremath{\\Delta_{\\text{MH}}}}\n\\newcommand{\\cpct}{\\ensuremath{C\\%}}\n\n\\title{Temporal Measurement Drift in LLM Benchmarks:\\\\A Large-Scale Differential Item Functioning Analysis}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nLarge Language Model (LLM) benchmarks implicitly assume temporal score comparability---that a score of 70\\% in 2024 reflects the same construct as 70\\% in 2023.\nWe test this assumption using Differential Item Functioning (DIF) analysis, a psychometric method that detects items whose difficulty changes across groups after controlling for overall ability.\nApplying Mantel--Haenszel DIF to the METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items), we find that \\textbf{31\\% of items} exhibit large temporal instability (ETS C classification, $|\\deltamh| \\geq 1.5$) between 2023 and 2024-H1 model cohorts---robust across six benchmarks (17.9--31.3\\%), all with random-split controls below 1\\%.\nItem-level decomposition shows domain-specific accuracy improvement explains at most 7.6\\% of this instability; the signal is predominantly item-specific.\nWe demonstrate that the field's standard ground truth---web-overlap contamination labels---measures global exposure rather than differential item functioning, yielding enrichment $\\approx$1.0 against DIF flags as theoretically expected.\nTo address this validation gap, we introduce a semi-synthetic framework that injects known differential contamination into real response matrices, with cross-subject matching that eliminates false positive inflation ($\\Delta$FPR\\,=\\,0.000).\nDespite 31\\% instability, benchmark rankings remain highly stable ($\\rho \\approx 0.997$), revealing massive measurement redundancy.\nDIF serves not as a quality filter but as a diagnostic lens for understanding what changed across model generations.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nWhen we report that ``Model B outperforms Model A on MMLU,'' we presume both scores reflect the same latent construct measured under comparable conditions.\nThis assumption of \\emph{temporal score comparability} is foundational to leaderboard rankings, model selection decisions, and progress narratives in NLP.\nYet benchmark items are static artifacts deployed in a rapidly evolving ecosystem: training corpora expand, data contamination pathways multiply, and model architectures shift---all of which can alter how individual items function across model generations.\n\nPsychometrics offers a mature framework for testing exactly this assumption: \\emph{Differential Item Functioning} (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability.\nAn item exhibits DIF when examinees of equal ability from different groups have different probabilities of answering correctly---signaling that the item measures something beyond the intended construct for at least one group.\nThe Mantel--Haenszel (MH) procedure, the most widely used DIF method in educational testing, provides both a statistical test and an effect-size measure ($\\deltamh$) with well-established classification thresholds.\n\nWe apply MH-DIF to the METABENCH response matrix---5,227 models $\\times$ 12,508 MMLU items---the largest-scale DIF analysis on LLM benchmarks to date.\nOur central finding is that \\textbf{31\\% of MMLU items are functionally unstable} across temporal model cohorts (2023 vs.\\ 2024-H1), classified as ETS C ($|\\deltamh| \\geq 1.5$).\nThis instability generalizes across six benchmarks (17.9--31.3\\%) and is robust to threshold choice, multiple testing correction, architecture composition, and ability-level confounds.\n\n\\paragraph{Instability $\\neq$ invalidity.}\nA critical interpretive point: DIF flags items whose \\emph{functioning changed} across generations---this is a diagnostic signal, not a quality verdict.\nWe show that MMLU rankings are massively redundant ($\\rho \\approx 0.997$ after removing all 31\\% flagged items), so instability does not threaten ranking validity.\nInstead, DIF reveals \\emph{which} capability dimensions are shifting across model generations, serving as a diagnostic lens rather than a quality filter.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n    \\item \\textbf{Large-scale temporal instability finding}: 31\\% of MMLU items exhibit large DIF across model generations, confirmed on six benchmarks (17.9--31.3\\%), with domain improvement explaining $\\leq$7.6\\% of the signal.\n    \\item \\textbf{Ground truth meta-critique}: Web-overlap contamination labels measure global exposure, not differential functioning. Enrichment $\\approx$1.0 against DIF flags is theoretically expected, not a failure. This affects the validity claims of all item-level detectors validated against web-overlap labels.\n    \\item \\textbf{Semi-synthetic validation framework}: A $\\Delta$TPR methodology with cross-subject matching ($\\Delta$FPR\\,=\\,0.000) that provides controlled validation for any item-level detector. Portable across benchmarks (GSM8K $\\Delta$TPR\\,=\\,+0.818).\n    \\item \\textbf{DIF as diagnostic lens}: DIF items carry genuine cross-cohort signal ($z$\\,=\\,$-$8 to $-$49$\\sigma$ vs.\\ random removal) but are the least disruptive non-random removal strategy ($z$\\,=\\,$-$9.5 vs.\\ accuracy-gap $z$\\,=\\,$-$157). We provide a concrete audit protocol for benchmark maintainers.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Benchmark contamination detection.}\nMethods for detecting data contamination in LLMs fall into several categories: membership inference via token-level statistics \\citep{shi2024detecting}, perturbation-based approaches that compare performance on original vs.\\ rephrased items \\citep{oren2024proving}, and overlap-based methods using n-gram matching between training data and benchmarks \\citep{li2024task}.\nThese approaches operate at the model level (testing individual models for contamination) and typically validate against web-overlap labels.\nOur work differs fundamentally: DIF operates at the item level across model populations, detecting \\emph{which items function differently} rather than \\emph{which models are contaminated}.\n\n\\paragraph{Benchmark reliability and validity.}\nRecent work has questioned benchmark reliability through various lenses: score instability under prompt perturbations \\citep{mizrahi2024state}, evaluation framework inconsistencies \\citep{polo2024tinybenchmarks}, and the general ``benchmark lottery'' phenomenon.\nOur psychometric approach complements these by providing item-level diagnostics grounded in established measurement theory.\n\n\\paragraph{DIF in educational testing.}\nDIF analysis has a 60-year history in educational and psychological testing \\citep{holland1993differential}.\nThe Mantel--Haenszel procedure \\citep{mantel1959statistical,holland1988alternate} remains the most widely used method due to its simplicity, robustness, and well-calibrated effect-size classifications (ETS A/B/C).\nWe apply this established methodology without modification; our contribution is the empirical findings and validation framework, not a new algorithm.\n\n\\paragraph{Psychometrics for LLM evaluation.}\nItem Response Theory (IRT) has been applied to LLM evaluation for efficient testing \\citep{polo2024tinybenchmarks} and characterizing item properties.\nOur work extends this psychometric lens to temporal comparability analysis, addressing a question that IRT alone cannot answer: whether items function \\emph{equivalently} across model cohorts.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Mantel--Haenszel DIF Analysis}\n\\label{sec:mh-dif}\n\nGiven a binary response matrix $\\mathbf{X} \\in \\{0,1\\}^{N \\times K}$ (models $\\times$ items), we partition models into a \\emph{reference group} (2023 cohort, $N_{\\text{ref}}=1{,}080$) and a \\emph{focal group} (2024-H1 cohort, $N_{\\text{foc}}=807$) based on release date.\nFor each item $k$, the MH procedure conditions on total score (sum of correct responses across all items) and computes the common odds ratio:\n\\begin{equation}\n    \\alpha_{\\text{MH},k} = \\frac{\\sum_j A_j D_j / T_j}{\\sum_j B_j C_j / T_j}\n\\end{equation}\nwhere $A_j, B_j, C_j, D_j$ are the entries of the $2\\times 2$ table at score stratum $j$, and $T_j$ is the stratum total.\nThe log-odds effect size on the ETS delta scale is $\\deltamh = -2.35 \\ln(\\alpha_{\\text{MH}})$.\n\nItems are classified using the ETS system: \\textbf{A} (negligible, $|\\deltamh| < 1.0$), \\textbf{B} (moderate, $1.0 \\leq |\\deltamh| < 1.5$), and \\textbf{C} (large, $|\\deltamh| \\geq 1.5$).\nC-classified items are our primary measure of temporal instability.\n\n\\subsection{Semi-Synthetic Validation Framework}\n\\label{sec:semi-synthetic}\n\nTo validate DIF detection power with known ground truth, we inject synthetic differential contamination into the real METABENCH response matrix:\n\\begin{enumerate}[leftmargin=*,nosep]\n    \\item Select 500 clean baseline items and 200 target items for injection.\n    \\item For each target item, flip incorrect$\\to$correct responses in the focal group with exploitation rate $p \\in \\{0.0, 0.3, 0.5, 0.7, 1.0\\}$.\n    \\item Run MH-DIF and measure True Positive Rate (TPR) and False Positive Rate (FPR).\n    \\item Report $\\Delta$TPR = TPR($p$) $-$ TPR($p$=0) as the detection power increase attributable to injected contamination.\n\\end{enumerate}\n\n\\subsection{Cross-Subject Matching}\n\\label{sec:cross-subject}\n\nStandard MH-DIF conditions on total score computed over all items including the tested item.\nWhen contamination inflates scores on tested items, this \\emph{matching variable contamination} biases the conditioning, inflating FPR.\nWe propose \\textbf{cross-subject matching}: for items in subject $s$, compute the matching variable as total score on all subjects \\emph{except} $s$.\nThis eliminates the feedback loop between contaminated items and the matching variable.\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\nAll analyses use the METABENCH response matrix.\nOur primary analysis focuses on MMLU (5,227 models $\\times$ 12,508 items across 57 subjects), with cross-benchmark replication on five additional benchmarks.\n\n\\subsection{Temporal DIF: 31\\% Instability Across Six Benchmarks}\n\\label{sec:temporal-dif}\n\n\\paragraph{MMLU results.}\nTable~\\ref{tab:temporal-dif} presents the core temporal DIF analysis.\nBetween the 2023 reference cohort ($N$=1,080) and 2024-H1 focal cohort ($N$=807), 31.3\\% of MMLU items are classified as ETS C (large DIF), with 16.3\\% as B (moderate) and 52.4\\% as A (negligible).\nThe random-split sanity check yields only 0.18\\% C-classified items, confirming the temporal signal is not a statistical artifact.\nThe ability-quintile split (high vs.\\ low ability, same time period) produces only 2.9\\% C items, demonstrating that DIF captures temporal rather than ability-driven differences.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temporal DIF summary (ETS classification). C\\% is the primary instability measure ($|\\deltamh| \\geq 1.5$). Random split serves as null control.}\n\\label{tab:temporal-dif}\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Split} & $N_{\\text{ref}}$ & $N_{\\text{foc}}$ & \\textbf{Items} & \\textbf{A\\%} & \\textbf{B\\%} & \\textbf{C\\%} & \\textbf{Rand.\\ C\\%} \\\\\n\\midrule\nTemporal & 1,080 & 807 & 12,508 & 52.4 & 16.3 & 31.3 & 0.18 \\\\\nAbility quintile & 1,044 & 1,044 & 12,508 & 85.2 & 11.9 & 2.9 & 0.15 \\\\\nWithin-family (Llama) & 161 & 308 & 12,508 & 24.1 & 14.6 & 61.3 & 0.22 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-benchmark generalization.}\nTable~\\ref{tab:cross-benchmark} shows temporal DIF across all six METABENCH benchmarks.\nEvery benchmark exhibits substantial instability (17.9--31.3\\% C), with all random controls below 1\\%.\nMulti-domain benchmarks (MMLU, WinoGrande, TruthfulQA) show higher C\\% (29.7--31.3\\%) than single-domain benchmarks (GSM8K 18.9\\%, HellaSwag 17.9\\%), consistent with greater item heterogeneity providing more opportunities for differential functioning.\nThe minimum enrichment ratio versus random is 45$\\times$, confirming temporal DIF far exceeds chance across all benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temporal DIF across six METABENCH benchmarks. All random controls are below 1\\%. Ratio = C\\% / Random C\\%.}\n\\label{tab:cross-benchmark}\n\\begin{tabular}{lrrrrrr}\n\\toprule\n\\textbf{Benchmark} & \\textbf{Items} & $N_{\\text{ref}}$ & $N_{\\text{foc}}$ & \\textbf{C\\%} & \\textbf{Rand.\\ C\\%} & \\textbf{Ratio} \\\\\n\\midrule\nMMLU & 12,508 & 1,080 & 807 & 31.3 & 0.18 & 174$\\times$ \\\\\nWinoGrande & 1,267 & 1,017 & 803 & 30.3 & 0.32 & 95$\\times$ \\\\\nTruthfulQA & 817 & 1,080 & 807 & 29.7 & 0.37 & 80$\\times$ \\\\\nARC-Challenge & 1,172 & 1,080 & 807 & 26.9 & 0.60 & 45$\\times$ \\\\\nGSM8K & 1,319 & 1,017 & 804 & 18.9 & 0.30 & 63$\\times$ \\\\\nHellaSwag & 10,042 & 1,080 & 807 & 17.9 & 0.28 & 64$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Permutation null distribution.}\nTo formally establish statistical significance, we run 1,000 permutations, randomly reassigning temporal labels while preserving group sizes.\nTable~\\ref{tab:permutation} summarizes the results: the null distribution has mean C\\%\\,=\\,0.21\\% ($\\text{SD}$\\,=\\,0.05\\%), consistent with the random-split control (0.18\\%).\nThe observed 31.3\\% lies $>$600$\\sigma$ above the null mean ($p < 0.001$), providing overwhelming evidence that temporal DIF is real.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Permutation null distribution (1,000 permutations) vs.\\ observed temporal DIF on MMLU.}\n\\label{tab:permutation}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Statistic} & \\textbf{Value} \\\\\n\\midrule\nObserved C\\% & 31.3 \\\\\nNull mean C\\% & 0.21 \\\\\nNull SD & 0.05 \\\\\nNull max (1,000 perms) & 0.42 \\\\\nPermutation $p$-value & $<$0.001 \\\\\n$z$-score & $>$600 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Domain specificity.}\nC\\% varies across MMLU subjects from 20.7\\% (computer security) to 48.4\\% (business ethics), with Spearman $\\rho$\\,=\\,0.307 ($p$\\,=\\,0.02) between subject-level C\\% and accuracy improvement.\nHowever, item-level decomposition (\\S\\ref{sec:confounds}) shows this modest ecological correlation overstates the actual contribution.\n\n\\subsection{Ruling Out Confounds}\n\\label{sec:confounds}\n\n\\paragraph{Domain improvement decomposition.}\nTable~\\ref{tab:regression} presents logistic regression models predicting DIF flag status from accuracy change and item properties.\nModel 1 (subject-level accuracy change only) yields pseudo $R^2$\\,=\\,0.0007---domain improvement explains essentially none of the DIF variance.\nThe odds ratio of 1.55 per 0.10 accuracy increase reverses to 0.73 in Model 2 when item properties (difficulty, discrimination) are added, exhibiting Simpson's paradox: the apparent domain-level association vanishes once item-level properties are controlled.\nItem-level accuracy change (Model 3) produces similarly negligible explanatory power ($R^2$\\,=\\,0.0012).\nCTT discrimination emerges as the strongest predictor (OR\\,=\\,1.54 per 0.10 unit), indicating high-discrimination items are more likely to be flagged---consistent with DIF theory, as these items are more sensitive to any cohort composition differences.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Logistic regression predicting DIF C flag. OR = odds ratio per 0.10 unit increase.}\n\\label{tab:regression}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Predictors} & \\textbf{McFadden $R^2$} & \\textbf{Nagelkerke $R^2$} & \\textbf{Key OR} \\\\\n\\midrule\nM1 & subject acc.\\ $\\Delta$ & 0.0007 & 0.0012 & 1.55 [1.19, 2.03] \\\\\nM2 & + item properties & 0.0423 & 0.072 & 0.73 (reversed) \\\\\nM3 & item acc.\\ $\\Delta$ & 0.0012 & 0.0021 & 1.08 [1.51, 2.96] \\\\\nM4 & + item properties & 0.0434 & 0.074 & 0.92 (reversed) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Architecture homogeneity.}\nMETABENCH MMLU is 99.98\\% decoder-only (5,226/5,227 models).\nExcluding the single non-decoder-only model produces identical C\\% (31.3\\%) with Jaccard\\,=\\,1.0 against the full-population analysis, confirming architecture heterogeneity is a non-issue.\n\n\\subsection{Ground Truth Meta-Critique}\n\\label{sec:meta-critique}\n\nExisting contamination detection methods validate against web-overlap labels---binary indicators of whether benchmark items appear in web-crawled training data.\nWe argue these labels measure \\emph{global exposure} (an item is publicly accessible), not \\emph{differential contamination} (an item functions differently across model cohorts).\nThese are orthogonal constructs: an item can be web-exposed yet function identically across cohorts (no DIF), or be non-exposed yet function differently due to indirect learning pathways.\n\nWe test this directly: DIF enrichment against Li et al.\\ web-overlap labels on 9,229 MMLU items yields enrichment\\,=\\,0.964 (Jaccard\\,=\\,0.206, $\\phi$\\,=\\,0.012, $\\chi^2$\\,=\\,1.28, $p$\\,=\\,0.258).\nThis near-unity enrichment is \\emph{expected}, not a failure---it confirms the theoretical orthogonality.\nThe implication is field-wide: any item-level detector validated solely against web-overlap labels (including Min-K\\%, ConStat, n-gram methods) has this blind spot.\nSemi-synthetic validation (\\S\\ref{sec:semi-synthetic-results}) provides a controlled alternative.\n\n\\subsection{Semi-Synthetic Validation}\n\\label{sec:semi-synthetic-results}\n\n\\paragraph{Detection power with known ground truth.}\nTable~\\ref{tab:semi-synthetic} presents semi-synthetic validation results using cross-subject matching.\nAt baseline ($p$\\,=\\,0.0), TPR\\,=\\,0.326 reflects the real temporal DIF signal (consistent with the 31.3\\% C\\% finding).\nAs exploitation rate increases, $\\Delta$TPR rises monotonically: +0.222 at $p$\\,=\\,0.3, +0.508 at $p$\\,=\\,0.5, reaching +0.674 at $p$\\,=\\,1.0.\nThis dose--response relationship confirms DIF detects injected differential contamination with increasing power.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Semi-synthetic detection power using cross-subject matching. $\\Delta$TPR measures detection power attributable to injected contamination (200 items injected into real METABENCH matrix).}\n\\label{tab:semi-synthetic}\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Exploitation rate $p$} & \\textbf{TPR} & $\\boldsymbol{\\Delta}$\\textbf{TPR} & \\textbf{FPR} & \\textbf{FPR inflation} \\\\\n\\midrule\n0.0 (baseline) & 0.326 & --- & 0.314 & 0.000 \\\\\n0.3 & 0.548 & +0.222 & 0.314 & 0.000 \\\\\n0.5 & 0.834 & +0.508 & 0.314 & 0.000 \\\\\n0.7 & 0.990 & +0.664 & 0.314 & 0.000 \\\\\n1.0 & 1.000 & +0.674 & 0.314 & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-subject matching eliminates FPR inflation.}\nTable~\\ref{tab:matching} compares matching strategies at maximum exploitation ($p$\\,=\\,1.0).\nStandard within-benchmark matching inflates FPR from 0.314 to 0.616 (+0.298) because contaminated items inflate the conditioning variable.\nCross-subject matching maintains FPR at 0.314 with zero inflation across all five tested subjects, validating our methodological contribution.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Matching strategy comparison at $p$\\,=\\,1.0 (full exploitation).}\n\\label{tab:matching}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Matching strategy} & \\textbf{TPR} & \\textbf{FPR} & $\\boldsymbol{\\Delta}$\\textbf{FPR vs.\\ baseline} \\\\\n\\midrule\nStandard (within-benchmark) & 1.000 & 0.616 & +0.298 \\\\\nCross-subject (external) & 1.000 & 0.314 & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-benchmark portability: GSM8K.}\nTable~\\ref{tab:gsm8k} summarizes the three-step GSM8K validation.\nThe framework successfully transfers: temporal C\\%\\,=\\,18.9\\% (lower than MMLU, consistent with single-domain structure), semi-synthetic $\\Delta$TPR\\,=\\,+0.818 (standard matching).\nThe GSM1K external validation yields $r$\\,=\\,$-$0.478 ($p$\\,=\\,0.005, $N$\\,=\\,33)---DIF flags \\emph{anti-correlate} with contamination gaps.\nThis negative correlation, while based on a small sample and wide confidence intervals, suggests DIF on GSM8K captures capability-driven rather than contamination-driven item functioning changes.\nWe report this as exploratory evidence, not a core claim.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{GSM8K three-step validation (1,319 items $\\times$ 6,702 models).}\n\\label{tab:gsm8k}\n\\begin{tabular}{llcl}\n\\toprule\n\\textbf{Step} & \\textbf{Metric} & \\textbf{Value} & \\textbf{Interpretation} \\\\\n\\midrule\n1 & Temporal C\\% & 18.9\\% & Lower than MMLU (single-domain) \\\\\n1 & Sanity C\\% & 0.3\\% & Well below temporal signal \\\\\n2 & $\\Delta$TPR ($p$\\,=\\,1.0) & +0.818 & Framework portable to math \\\\\n3 & Pearson $r$ vs.\\ GSM1K & $-$0.478 & DIF $\\neq$ contamination (exploratory) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Downstream Impact: Instability $\\neq$ Invalidity}\n\\label{sec:downstream}\n\n\\paragraph{Graceful degradation under item replacement.}\nTable~\\ref{tab:degradation} shows benchmark validity metrics under progressive replacement of DIF-flagged items.\nEven at 31\\% replacement (matching the observed C\\%), ranking correlation remains $\\rho$\\,=\\,0.990, reliability $\\alpha$\\,=\\,0.935, and construct coverage 0.89.\nAt 50\\% replacement, all metrics remain within acceptable ranges ($\\rho$\\,=\\,0.978, $\\alpha$\\,=\\,0.912).\nThe theoretical bound $\\rho \\geq 1 - 0.45r$ (where $r$ is the replacement fraction) fits the empirical data with correlation 0.994, indicating degradation is predictable and manageable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Benchmark validity metrics under progressive DIF item replacement on MMLU.}\n\\label{tab:degradation}\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{Replacement \\%} & \\textbf{Ranking $\\rho$} & \\textbf{Reliability $\\alpha$} & \\textbf{Construct coverage} \\\\\n\\midrule\n0 & 1.000 & 0.972 & 1.00 \\\\\n5 & 0.999 & 0.968 & 0.98 \\\\\n10 & 0.997 & 0.961 & 0.96 \\\\\n20 & 0.993 & 0.948 & 0.93 \\\\\n31 & 0.990 & 0.935 & 0.89 \\\\\n50 & 0.978 & 0.912 & 0.85 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{DIF as diagnostic lens, not quality filter.}\nDIF items carry genuine cross-cohort signal: removing DIF-flagged items causes significantly more ranking disruption than random removal ($z$\\,=\\,$-$8 to $-$49$\\sigma$ across 21 conditions).\nHowever, circularity ablation reveals DIF is the \\emph{least} disruptive non-random strategy: accuracy-gap removal disrupts 10--16$\\times$ more ($z$\\,=\\,$-$157), high-variance removal 11$\\times$ more ($z$\\,=\\,$-$108), and high-discrimination removal 1.7$\\times$ more ($z$\\,=\\,$-$16).\nThe MH procedure's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items.\nDIF-discrimination overlap is only 22.1\\% (Jaccard\\,=\\,0.12)---DIF identifies ``items that changed across generations,'' not ``good measurement items.''\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Implications for benchmark maintenance.}\nOur findings suggest a practical audit protocol for benchmark maintainers.\nItems with persistent C-level DIF across multiple cohort definitions warrant investigation---not automatic removal, but diagnostic attention.\nThe graceful degradation results (\\S\\ref{sec:downstream}) show that targeted replacement is safe: even replacing all 31\\% flagged items preserves ranking validity ($\\rho$\\,=\\,0.990).\nThe massive measurement redundancy in MMLU (12,508 items, $\\rho$\\,$\\approx$\\,0.997 under 31\\% removal) provides a large safety margin for item rotation.\n\n\\paragraph{What drives the instability?}\nDIF-C items are moderately harder (Cohen's $d$\\,=\\,$-$0.247) and higher-discrimination ($d$\\,=\\,0.230) than non-DIF items, but uniformly distributed across domains ($\\chi^2$ $p$\\,=\\,0.32).\nA striking difficulty $\\times$ direction interaction ($\\rho$\\,=\\,$-$0.597) reveals a systematic pattern: hardest-decile DIF items are 88.7\\% focal-favoring (2024 models perform better), while easiest-decile items are 96.2\\% reference-favoring (2023 models perform better).\nThis suggests capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n\n\\paragraph{Complementarity with existing approaches.}\nDIF and contamination detectors (Min-K\\%, ConStat) address different questions.\nContamination detectors ask ``has this model seen this item?'' (model-level, individual diagnosis).\nDIF asks ``does this item function differently across model generations?'' (item-level, population diagnosis).\nThe web-overlap enrichment $\\approx$1.0 confirms these are orthogonal signals, not competing methods.\nBenchmark maintainers should use both: DIF for population-level item auditing, contamination detectors for individual model vetting.\n\n% ============================================================\n\\section*{Limitations}\n\n\\begin{enumerate}[leftmargin=*,nosep]\n    \\item \\textbf{Unidimensional IRT misspecification.} MH-DIF assumes unidimensional ability, but MMLU spans 57 subjects. Bifactor analysis (Appendix~\\ref{app:bifactor}) confirms the general factor explains only 31\\% of variance. Future work should explore multidimensional IRT and MIMIC models for more principled conditioning.\n    \\item \\textbf{Semi-synthetic simplification.} Our injection mechanism (incorrect$\\to$correct flipping) models one contamination pathway. Real contamination may produce subtler response pattern changes. The framework's value lies in providing \\emph{any} controlled ground truth where none existed before.\n    \\item \\textbf{Temporal cohort definition.} Our 2023/2024-H1 binary split is a simplification; model release dates are noisy proxies for training data cutoffs. Item-Focused Trees analysis (Appendix~\\ref{app:ift}) using continuous release dates yields similar results (34\\% detection rate, Jaccard\\,=\\,0.81 with MH).\n\\end{enumerate}\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first large-scale DIF analysis of LLM benchmarks, revealing that 31\\% of MMLU items are temporally unstable across model generations---a finding that generalizes across six benchmarks (17.9--31.3\\%).\nThis instability is predominantly item-specific (domain improvement explains $\\leq$7.6\\%), does not threaten ranking validity ($\\rho$\\,$\\approx$\\,0.997), and is invisible to the field's standard web-overlap ground truth (enrichment\\,$\\approx$\\,1.0).\nOur semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR\\,=\\,0.000) provides reusable infrastructure for validating any item-level detection method.\nDIF serves as a diagnostic lens---revealing what changed across model generations---not a quality filter, with direct implications for benchmark maintenance practices.\n\n% ============================================================\n\\appendix\n\n\\section{RL Robustness}\n\\label{app:rl}\n\nWe evaluate DIF stability when reasoning-RL models (GRPO/PPO-trained) are added to the focal cohort.\nTable~\\ref{tab:rl-stability} shows DIF C\\% changes minimally: from 31.3\\% (SFT-only baseline) to 30.8\\% when 13 reasoning-RL models are mixed into the 820-model focal cohort.\nJaccard similarity between flagged item sets remains $\\geq$0.92, and TOST equivalence testing (margin\\,=\\,0.05) confirms non-degradation ($p$\\,=\\,0.003).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DIF stability across training paradigms. CI = 95\\% bootstrap confidence interval.}\n\\label{tab:rl-stability}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Focal cohort} & $N_{\\text{foc}}$ & \\textbf{C\\%} & \\textbf{Jaccard vs.\\ SFT} & \\textbf{Bootstrap CI} \\\\\n\\midrule\nSFT-only (baseline) & 807 & 31.3 & --- & --- \\\\\nAlignment-RL (DPO/ORPO) & 477 & 31.1 & 0.94 & [0.92, 0.96] \\\\\nSFT + Reasoning-RL mixed & 820 & 30.8 & 0.92 & [0.90, 0.96] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn contrast, traditional detectors degrade substantially on reasoning-RL models (Table~\\ref{tab:rl-detectors}): Min-K\\% AUROC drops from 0.72 to 0.48 ($\\Delta$\\,=\\,$-$0.24, DeLong $p$\\,=\\,0.001), and ConStat from 0.68 to 0.51 ($\\Delta$\\,=\\,$-$0.17, $p$\\,=\\,0.008).\nDIF's group-level design is naturally immune to individual-model signal perturbation from RL training.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Traditional detector degradation on reasoning-RL models.}\n\\label{tab:rl-detectors}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Detector} & \\textbf{AUROC (SFT)} & \\textbf{AUROC (RL)} & $\\boldsymbol{\\Delta}$ & \\textbf{DeLong $p$} \\\\\n\\midrule\nMin-K\\% & 0.72 & 0.48 & $-$0.24 & 0.001 \\\\\nConStat & 0.68 & 0.51 & $-$0.17 & 0.008 \\\\\nDIF (group) & --- & --- & Jaccard\\,=\\,0.92 & TOST $p$\\,=\\,0.003 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{ConStat Perturbation Evaluation}\n\\label{app:constat}\n\nWe independently evaluate ConStat-style perturbation testing on 250 LLM-paraphrased MMLU items across 50 models.\nTable~\\ref{tab:constat} shows detection power decreasing from 0.38 (SFT) to 0.31 (alignment-RL) to 0.14 (reasoning-RL) at $\\delta \\geq 0.6$ effect-size threshold, with FPR controlled at $\\sim$0.05.\nThe 63\\% drop in reasoning-RL detection power reflects GRPO/PPO training generalizing problem-solving ability rather than memorizing verbatim items, erasing the original-vs-paraphrased performance gap that ConStat relies on.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{ConStat detection power by training paradigm ($\\delta \\geq 0.6$, FDR $q$\\,=\\,0.05).}\n\\label{tab:constat}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Paradigm} & $N_{\\text{models}}$ & \\textbf{Detection rate} & \\textbf{FPR} \\\\\n\\midrule\nSFT-only & 25 & 0.38 & 0.048 \\\\\nAlignment-RL & 15 & 0.31 & 0.045 \\\\\nReasoning-RL & 10 & 0.14 & 0.051 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{DVD Generation Variance Evaluation}\n\\label{app:dvd}\n\nWe evaluate Detection via generation Variance and Difficulty (DVD) on 500 MMLU items across 12 models with 50 temperature-sampled generations per item ($T$\\,=\\,0.8).\nTable~\\ref{tab:dvd} shows DVD performs better on variant contamination (AUROC\\,=\\,0.74) than verbatim (AUROC\\,=\\,0.61), because variant contamination produces bimodal generation variance.\nFPR is 0.065.\nThe 68 GPU-hours computational cost contrasts with DIF's zero-GPU design.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DVD detection power by contamination type (12 models, 500 items, 50 generations each).}\n\\label{tab:dvd}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Contamination type} & \\textbf{AUROC} & \\textbf{Detection rate} & \\textbf{FPR} \\\\\n\\midrule\nVerbatim & 0.61 & 0.22 & 0.065 \\\\\nVariant & 0.74 & 0.45 & 0.065 \\\\\nClean & --- & --- & 0.065 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Ensemble Fusion}\n\\label{app:ensemble}\n\nTable~\\ref{tab:ensemble} evaluates DIF + ConStat + DVD fusion.\nWeighted fusion achieves AUROC\\,=\\,0.93 and TPR\\,=\\,0.82 at FPR\\,$<$\\,0.05, exceeding any individual detector.\nCross-validated weights assign DIF the highest weight (0.52), reflecting its cross-paradigm consistency.\nEnsemble performance is robust to weight choice (uniform vs.\\ optimized AUC gap\\,=\\,0.03).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Ensemble vs.\\ individual detector performance.}\n\\label{tab:ensemble}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{TPR @ FPR 0.05} & \\textbf{AUROC} & \\textbf{Coverage} \\\\\n\\midrule\nDIF (MH) & 0.68 & 0.87 & All paradigms \\\\\nConStat & 0.55 & 0.76 & Non-RL only \\\\\nDVD & 0.42 & 0.71 & Variant only \\\\\nEnsemble (majority) & 0.78 & 0.91 & All \\\\\nEnsemble (weighted) & 0.82 & 0.93 & All \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Bifactor IRT Equating Pilot}\n\\label{app:bifactor}\n\nWe fit a bifactor IRT model (general factor + 57 subject-specific factors) to validate unidimensionality assumptions.\nTable~\\ref{tab:bifactor} shows marginal fit: RMSEA\\,=\\,0.028 (pass) and SRMR\\,=\\,0.045 (pass), but CFI\\,=\\,0.91 and TLI\\,=\\,0.89 fall below the 0.95 standard.\nThe general factor explains only 31\\% of variance, confirming MMLU's fundamental multidimensionality.\nDespite marginal fit, equated scores correlate at $\\rho$\\,=\\,0.97, suggesting equating is workable even under model misspecification.\nThis motivates future multidimensional IRT work.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Bifactor IRT model fit indices for MMLU (12,508 items, 57 subject factors).}\n\\label{tab:bifactor}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Index} & \\textbf{Value} & \\textbf{Threshold} & \\textbf{Verdict} \\\\\n\\midrule\nRMSEA & 0.028 & $<$0.06 & Pass \\\\\nCFI & 0.91 & $>$0.95 & Marginal \\\\\nTLI & 0.89 & $>$0.95 & Marginal \\\\\nSRMR & 0.045 & $<$0.08 & Pass \\\\\nGeneral $\\omega$ & 0.31 & $>$0.50 & Fail \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Item Generation Calibration}\n\\label{app:item-gen}\n\nWe generate 500 replacement items for 200 DIF-flagged MMLU items using Claude 3.5 Sonnet.\nTable~\\ref{tab:item-gen} compares prompt-only targeting vs.\\ student simulation calibration.\nStudent simulation improves difficulty correlation from $\\rho$\\,=\\,0.32 to 0.71 and holdout validation from 0.28 to 0.65, approaching but not reaching the 0.75--0.82 literature benchmark.\nThis confirms item generation is feasible but not yet reliable enough for automated benchmark regeneration.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Item generation calibration accuracy (500 items, 200 DIF-targeted).}\n\\label{tab:item-gen}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Difficulty $\\rho$} & \\textbf{Cognitive match} & \\textbf{Holdout $\\rho$} \\\\\n\\midrule\nPrompt-only & 0.32 & 0.65 & 0.28 \\\\\nStudent simulation & 0.71 & 0.78 & 0.65 \\\\\nLiterature benchmark & 0.75--0.82 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Cumulative Bayesian DIF}\n\\label{app:bayesian}\n\nFollowing Sinharay et al.\\ (2006), we simulate cumulative Bayesian DIF monitoring across successive benchmark administrations.\nTable~\\ref{tab:bayesian} shows detection power increasing from 0.42 (single administration) to 0.78 (four administrations) at $\\delta$\\,=\\,1.0, with FPR decreasing from 0.041 to 0.033 due to prior shrinkage.\nAt the operational effect size $\\delta$\\,=\\,1.4, three administrations achieve 0.85 power.\nThis supports a longitudinal monitoring protocol where items below the single-administration decision threshold accumulate evidence over time.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cumulative Bayesian DIF power by number of administrations (500 items, 200 models/admin).}\n\\label{tab:bayesian}\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Administrations} & \\textbf{Power ($\\delta$=1.0)} & \\textbf{Power ($\\delta$=1.4)} & \\textbf{Power ($\\delta$=1.6)} & \\textbf{FPR} \\\\\n\\midrule\n1 & 0.42 & 0.68 & 0.72 & 0.041 \\\\\n2 & 0.58 & 0.79 & 0.84 & 0.038 \\\\\n3 & 0.71 & 0.85 & 0.90 & 0.035 \\\\\n4 & 0.78 & 0.89 & 0.93 & 0.033 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Item-Focused Trees}\n\\label{app:ift}\n\nAs a robustness check, we apply Item-Focused Trees (IFT; Tutz \\& Berger, 2016), which treat model release date as a continuous covariate rather than a binary split.\nTable~\\ref{tab:ift} shows IFT detection rate (34.0\\%) is close to MH (31.3\\%), with Jaccard\\,=\\,0.81 concordance.\nIFT detects 412 items missed by MH (gradual drift patterns), while MH detects 287 items missed by IFT.\nThe IFT split-point mode at 2023-Q4 aligns with our temporal cohort boundary.\n856 items show nonlinear drift (difficulty changes non-monotonically over time), a pattern invisible to binary DIF.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Item-Focused Trees (continuous) vs.\\ MH-DIF (categorical) on MMLU (12,508 items).}\n\\label{tab:ift}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Detection rate} & \\textbf{Unique items} & \\textbf{Computation (hrs)} \\\\\n\\midrule\nMH-DIF (categorical) & 31.3\\% & 287 & 0.5 \\\\\nIFT (continuous) & 34.0\\% & 412 & 8.0 \\\\\nOverlap (both) & --- & Jaccard\\,=\\,0.81 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Holland and Thayer(1988)]{holland1988alternate}\nP.~W. Holland and D.~T. Thayer.\n\\newblock Differential item performance and the Mantel--Haenszel procedure.\n\\newblock In H.~Wainer and H.~I. Braun, editors, \\emph{Test Validity}, pages 129--145. Lawrence Erlbaum, 1988.\n\n\\bibitem[Holland and Wainer(1993)]{holland1993differential}\nP.~W. Holland and H.~Wainer, editors.\n\\newblock \\emph{Differential Item Functioning}.\n\\newblock Lawrence Erlbaum Associates, 1993.\n\n\\bibitem[Li et~al.(2024)]{li2024task}\nY.~Li, et~al.\n\\newblock Task contamination: Language models may not be few-shot anymore.\n\\newblock In \\emph{Proceedings of AAAI}, 2024.\n\n\\bibitem[Mantel and Haenszel(1959)]{mantel1959statistical}\nN.~Mantel and W.~Haenszel.\n\\newblock Statistical aspects of the analysis of data from retrospective studies of disease.\n\\newblock \\emph{Journal of the National Cancer Institute}, 22(4):719--748, 1959.\n\n\\bibitem[Mizrahi et~al.(2024)]{mizrahi2024state}\nM.~Mizrahi, et~al.\n\\newblock State of what art? A call for multi-prompt LLM evaluation.\n\\newblock \\emph{Transactions of the ACL}, 2024.\n\n\\bibitem[Oren et~al.(2024)]{oren2024proving}\nY.~Oren, et~al.\n\\newblock Proving test set contamination in black box language models.\n\\newblock In \\emph{Proceedings of ICLR}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo, et~al.\n\\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.\n\\newblock In \\emph{Proceedings of ICML}, 2024.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nW.~Shi, et~al.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{Proceedings of ICLR}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7589e6ff-96f6-4178-bb69-4d37a808a2d8",
  "isSidechain": false,
  "requestId": "req_011CbG6U5QnvXrPLTePzUape",
  "type": "assistant",
  "uuid": "33e10af5-82b3-462b-9f40-b9c31ab5176c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1GokuL5r7xGqCoS6JuT7r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9496,
      "cache_read_input_tokens": 42678,
      "output_tokens": 13971,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13971,
          "cache_read_input_tokens": 42678,
          "cache_creation_input_tokens": 9496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9496
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T165710 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "b9f9a9f0-ed71-4853-b17f-5459d784f8d6",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream_20260521T165710",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb"
}
```

---

### Assistant

_source line 26 · 2026-05-21T17:22:27.959Z_

Now let me compile it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9f9a9f0-ed71-4853-b17f-5459d784f8d6",
  "isSidechain": false,
  "requestId": "req_011CbG6nqmHjTEQoN16TSTL4",
  "type": "assistant",
  "uuid": "0f6a612f-3c2f-406c-8b27-48c63a4e7399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qxt1ZqDxxfy7trdmQQGDm2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14040,
      "cache_read_input_tokens": 52174,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 52174,
          "cache_creation_input_tokens": 14040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14040
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

_source line 27 · 2026-05-21T17:22:29.336Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SMJXaVvs1dEWrKVq2RpnD8`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper (two passes)",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f6a612f-3c2f-406c-8b27-48c63a4e7399",
  "isSidechain": false,
  "requestId": "req_011CbG6nqmHjTEQoN16TSTL4",
  "type": "assistant",
  "uuid": "01bad3b9-74fe-4c23-8107-acd3d0c09afd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qxt1ZqDxxfy7trdmQQGDm2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14040,
      "cache_read_input_tokens": 52174,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 52174,
          "cache_creation_input_tokens": 14040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14040
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

_source line 28 · 2026-05-21T17:22:30.374Z_

<details><summary>↩ Tool result · `toolu_01SMJXaVvs1dEWrKVq2RpnD8`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
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
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
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
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]
Overfull \hbox (33.79782pt too wide) in paragraph at lines 67--68
[]\T1/ptm/b/n/10.95 Semi-synthetic val-i-da-tion frame-work\T1/ptm/m/n/10.95 : 
A $\OT1/cmr/m/n/10.95 ^^A$\T1/ptm/m/n/10.95 TPR method-ol-ogy with cross-subjec
t match-ing ($\OT1/cmr/m/n/10.95 ^^A$\T1/ptm/m/n/10.95 FPR=0.000)

Package natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu
t line 76.


Package natbib Warning: Citation `oren2024proving' on page 2 undefined on input
 line 76.


Package natbib Warning: Citation `li2024task' on page 2 undefined on input line
 76.


Package natbib Warning: Citation `mizrahi2024state' on page 2 undefined on inpu
t line 81.


Package natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o
n input line 81.


Package natbib Warning: Citation `holland1993differential' on page 2 undefined 
on input line 85.


Package natbib Warning: Citation `mantel1959statistical' on page 2 undefined on
 input line 86.


Package natbib Warning: Citation `holland1988alternate' on page 2 undefined on 
input line 86.


Package natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o
n input line 90.

[2]

LaTeX Warning: Reference `tab:temporal-dif' on page 3 undefined on input line 1
41.


LaTeX Warning: Reference `tab:cross-benchmark' on page 3 undefined on input lin
e 163.


LaTeX Warning: Reference `tab:permutation' on page 3 undefined on input line 18
9.

[3]

LaTeX Warning: Reference `sec:confounds' on page 4 undefined on input line 213.



LaTeX Warning: Reference `tab:regression' on page 4 undefined on input line 219
.

[4]

LaTeX Warning: Reference `sec:semi-synthetic-results' on page 5 undefined on in
put line 256.


LaTeX Warning: Reference `tab:semi-synthetic' on page 5 undefined on input line
 262.


LaTeX Warning: Reference `tab:matching' on page 5 undefined on input line 286.


LaTeX Warning: Reference `tab:gsm8k' on page 5 undefined on input line 306.


Overfull \hbox (0.35013pt too wide) in paragraph at lines 306--311
\T1/ptm/m/n/10.95 The frame-work suc-cess-fully trans-fers: tem-po-ral C%=18.9%
 (lower than MMLU, con-sis-tent with single-

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 329.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\not' on input line 329.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 329.


LaTeX Warning: Reference `tab:degradation' on page 5 undefined on input line 33
3.

[5]

LaTeX Warning: Reference `sec:downstream' on page 6 undefined on input line 370
.


Overfull \hbox (22.92319pt too wide) in paragraph at lines 368--372
\T1/ptm/m/n/10.95 mark main-tain-ers. Items with per-sis-tent C-level DIF acros
s mul-ti-ple co-hort def-i-ni-tions war-rant investigation---
[6]

LaTeX Warning: Reference `app:bifactor' on page 7 undefined on input line 389.


LaTeX Warning: Reference `app:ift' on page 7 undefined on input line 391.


Overfull \hbox (3.60628pt too wide) in paragraph at lines 398--402
\T1/ptm/m/n/10.95 match-ing ($\OT1/cmr/m/n/10.95 ^^A$\T1/ptm/m/n/10.95 FPR=0.00
0) pro-vides reusable in-fras-truc-ture for val-i-dat-ing any item-level de-tec
-tion method.

LaTeX Warning: Reference `tab:rl-stability' on page 7 undefined on input line 4
10.


Overfull \hbox (22.00183pt too wide) in paragraph at lines 409--412
\T1/ptm/m/n/10.95 item sets re-mains $\OMS/cmsy/m/n/10.95 ^^U$\T1/ptm/m/n/10.95
 0.92, and TOST equiv-a-lence test-ing (mar-gin=0.05) con-firms non-degradation
 ($\OML/cmm/m/it/10.95 p$\T1/ptm/m/n/10.95 =0.003). 
[7]

LaTeX Warning: Reference `tab:rl-detectors' on page 8 undefined on input line 4
29.


LaTeX Warning: Reference `tab:constat' on page 8 undefined on input line 452.


LaTeX Warning: Reference `tab:dvd' on page 8 undefined on input line 475.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:ensemble' on page 8 undefined on input line 498.


Overfull \hbox (8.62186pt too wide) in paragraph at lines 498--502
\T1/ptm/m/n/10.95 Table [] eval-u-ates DIF + Con-Stat + DVD fu-sion. Weighted f
u-sion achieves AU-ROC=0.93 and TPR=0.82
[8]

LaTeX Warning: Reference `tab:bifactor' on page 9 undefined on input line 525.


LaTeX Warning: Reference `tab:item-gen' on page 9 undefined on input line 552.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:bayesian' on page 9 undefined on input line 576.

[9]

LaTeX Warning: Reference `tab:ift' on page 10 undefined on input line 601.

[10]

Package natbib Warning: There were undefined citations.

[11] (./paper.aux

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
blic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw
/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 180809 bytes).
Transcript written on paper.log.
[8]

LaTeX Warning: `h' float specifier changed to `ht'.

[9] [10] [11] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw
/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 184028 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01bad3b9-74fe-4c23-8107-acd3d0c09afd",
  "isSidechain": false,
  "promptId": "fbb2aad3-deff-45fc-a21a-33870865ab9a",
  "type": "user",
  "uuid": "32f4bec0-2bf3-45b3-87c1-49aeb8e6a865",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\nOverfull \\hbox (33.79782pt too wide) in paragraph at lines 67--68\n[]\\T1/ptm/b/n/10.95 Semi-synthetic val-i-da-tion frame-work\\T1/ptm/m/n/10.95 : \nA $\\OT1/cmr/m/n/10.95 ^^A$\\T1/ptm/m/n/10.95 TPR method-ol-ogy with cross-subjec\nt match-ing ($\\OT1/cmr/m/n/10.95 ^^A$\\T1/ptm/m/n/10.95 FPR=0.000)\n\nPackage natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu\nt line 76.\n\n\nPackage natbib Warning: Citation `oren2024proving' on page 2 undefined on input\n line 76.\n\n\nPackage natbib Warning: Citation `li2024task' on page 2 undefined on input line\n 76.\n\n\nPackage natbib Warning: Citation `mizrahi2024state' on page 2 undefined on inpu\nt line 81.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o\nn input line 81.\n\n\nPackage natbib Warning: Citation `holland1993differential' on page 2 undefined \non input line 85.\n\n\nPackage natbib Warning: Citation `mantel1959statistical' on page 2 undefined on\n input line 86.\n\n\nPackage natbib Warning: Citation `holland1988alternate' on page 2 undefined on \ninput line 86.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o\nn input line 90.\n\n[2]\n\nLaTeX Warning: Reference `tab:temporal-dif' on page 3 undefined on input line 1\n41.\n\n\nLaTeX Warning: Reference `tab:cross-benchmark' on page 3 undefined on input lin\ne 163.\n\n\nLaTeX Warning: Reference `tab:permutation' on page 3 undefined on input line 18\n9.\n\n[3]\n\nLaTeX Warning: Reference `sec:confounds' on page 4 undefined on input line 213.\n\n\n\nLaTeX Warning: Reference `tab:regression' on page 4 undefined on input line 219\n.\n\n[4]\n\nLaTeX Warning: Reference `sec:semi-synthetic-results' on page 5 undefined on in\nput line 256.\n\n\nLaTeX Warning: Reference `tab:semi-synthetic' on page 5 undefined on input line\n 262.\n\n\nLaTeX Warning: Reference `tab:matching' on page 5 undefined on input line 286.\n\n\nLaTeX Warning: Reference `tab:gsm8k' on page 5 undefined on input line 306.\n\n\nOverfull \\hbox (0.35013pt too wide) in paragraph at lines 306--311\n\\T1/ptm/m/n/10.95 The frame-work suc-cess-fully trans-fers: tem-po-ral C%=18.9%\n (lower than MMLU, con-sis-tent with single-\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 329.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\not' on input line 329.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 329.\n\n\nLaTeX Warning: Reference `tab:degradation' on page 5 undefined on input line 33\n3.\n\n[5]\n\nLaTeX Warning: Reference `sec:downstream' on page 6 undefined on input line 370\n.\n\n\nOverfull \\hbox (22.92319pt too wide) in paragraph at lines 368--372\n\\T1/ptm/m/n/10.95 mark main-tain-ers. Items with per-sis-tent C-level DIF acros\ns mul-ti-ple co-hort def-i-ni-tions war-rant investigation---\n[6]\n\nLaTeX Warning: Reference `app:bifactor' on page 7 undefined on input line 389.\n\n\nLaTeX Warning: Reference `app:ift' on page 7 undefined on input line 391.\n\n\nOverfull \\hbox (3.60628pt too wide) in paragraph at lines 398--402\n\\T1/ptm/m/n/10.95 match-ing ($\\OT1/cmr/m/n/10.95 ^^A$\\T1/ptm/m/n/10.95 FPR=0.00\n0) pro-vides reusable in-fras-truc-ture for val-i-dat-ing any item-level de-tec\n-tion method.\n\nLaTeX Warning: Reference `tab:rl-stability' on page 7 undefined on input line 4\n10.\n\n\nOverfull \\hbox (22.00183pt too wide) in paragraph at lines 409--412\n\\T1/ptm/m/n/10.95 item sets re-mains $\\OMS/cmsy/m/n/10.95 ^^U$\\T1/ptm/m/n/10.95\n 0.92, and TOST equiv-a-lence test-ing (mar-gin=0.05) con-firms non-degradation\n ($\\OML/cmm/m/it/10.95 p$\\T1/ptm/m/n/10.95 =0.003). \n[7]\n\nLaTeX Warning: Reference `tab:rl-detectors' on page 8 undefined on input line 4\n29.\n\n\nLaTeX Warning: Reference `tab:constat' on page 8 undefined on input line 452.\n\n\nLaTeX Warning: Reference `tab:dvd' on page 8 undefined on input line 475.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:ensemble' on page 8 undefined on input line 498.\n\n\nOverfull \\hbox (8.62186pt too wide) in paragraph at lines 498--502\n\\T1/ptm/m/n/10.95 Table [] eval-u-ates DIF + Con-Stat + DVD fu-sion. Weighted f\nu-sion achieves AU-ROC=0.93 and TPR=0.82\n[8]\n\nLaTeX Warning: Reference `tab:bifactor' on page 9 undefined on input line 525.\n\n\nLaTeX Warning: Reference `tab:item-gen' on page 9 undefined on input line 552.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:bayesian' on page 9 undefined on input line 576.\n\n[9]\n\nLaTeX Warning: Reference `tab:ift' on page 10 undefined on input line 601.\n\n[10]\n\nPackage natbib Warning: There were undefined citations.\n\n[11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\n/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 180809 bytes).\nTranscript written on paper.log.\n[8]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9] [10] [11] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\n/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 184028 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "01bad3b9-74fe-4c23-8107-acd3d0c09afd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-21T17:22:30.378Z_

```json
{
  "parentUuid": "32f4bec0-2bf3-45b3-87c1-49aeb8e6a865",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "603e80d4-35ea-4c34-9354-fc260a887acb",
  "timestamp": "2026-05-21T17:22:30.378Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 30 · 2026-05-21T17:22:39.486Z_

PDF compiled successfully (11 pages, 184KB). All references and citations resolved on the second pass.

The paper covers all 14 experiments from `experiment_data.json`:

**Main body (7 tables):** temporal DIF (MMLU + 6 benchmarks), permutation null, logistic regression decomposition, architecture stratification, semi-synthetic validation, matching strategy comparison, GSM8K three-step, graceful degradation.

**Appendix (9 tables):** RL robustness + detector degradation, ConStat perturbation, DVD generation variance, ensemble fusion, bifactor IRT, item generation calibration, cumulative Bayesian DIF, Item-Focused Trees.

Output: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "603e80d4-35ea-4c34-9354-fc260a887acb",
  "isSidechain": false,
  "requestId": "req_011CbG6oCtXYoRyNn81bKWsK",
  "type": "assistant",
  "uuid": "487c4132-3a91-4b7e-abfb-ef489a597e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/best",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A31HpKy5AUssBuYXvFWYQs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5258,
      "cache_read_input_tokens": 66214,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 66214,
          "cache_creation_input_tokens": 5258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5258
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T165710 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "487c4132-3a91-4b7e-abfb-ef489a597e0c",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream_20260521T165710",
  "sessionId": "14e80fd9-a3f6-4ca0-91a9-233525c7cceb"
}
```

---
