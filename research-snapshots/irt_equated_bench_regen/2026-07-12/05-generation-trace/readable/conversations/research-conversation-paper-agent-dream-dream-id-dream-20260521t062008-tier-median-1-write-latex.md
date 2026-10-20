# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/1c6b9965-4730-46a2-a3a4-07c965d9e09e.jsonl`
- **Structured JSON:** [`15d94e4f80bac66055f1.json`](../../sessions/15/15d94e4f80bac66055f1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T06:44:26.497Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T06:44:26.497Z",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Claim 1 (31.3% temporal instability) 和 Claim 3 (semi-synthetic framework) 是主要得分点。 Claim 2 meta-critique 被 1-2 个评审视为 \"obvious in hindsight\"，独立贡献权重下降。 Claim 4 的 GSM1K 子发现 (N=33) 被 dismiss，plan_017 的 z-score 证据保留但 \"so what\" 回应不足。 Novelty 受质疑（\"just MH-DIF at scale\"）但不构成 unanimous reject。IRT misspecification 被要求补充 sensitivity analysis（可能需要 multidimensional IRT pilot）。 整体：reviewer avg 5.0-5.5，acceptance probability ~30%，需要 2-3 major revisions。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T06:44:26.501Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T06:44:26.501Z",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-21T06:44:26.520Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Claim 1 (31.3% temporal instability) 和 Claim 3 (semi-synthetic framework) 是主要得分点。 Claim 2 meta-critique 被 1-2 个评审视为 "obvious in hindsight"，独立贡献权重下降。 Claim 4 的 GSM1K 子发现 (N=33) 被 dismiss，plan_017 的 z-score 证据保留但 "so what" 回应不足。 Novelty 受质疑（"just MH-DIF at scale"）但不构成 unanimous reject。IRT misspecification 被要求补充 sensitivity analysis（可能需要 multidimensional IRT pilot）。 整体：reviewer avg 5.0-5.5，acceptance probability ~30%，需要 2-3 major revisions。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f9190119-bc3e-4325-b2be-2617c4e8f5d7",
  "type": "user",
  "uuid": "d8d8e03f-d652-45d2-be09-6a4ba49f8668",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T06:44:26.519Z_

```json
{
  "parentUuid": "d8d8e03f-d652-45d2-be09-6a4ba49f8668",
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
  "uuid": "05bf12a6-cb7f-4a28-96a4-9b3b3a2a9d4f",
  "timestamp": "2026-05-21T06:44:26.519Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T06:44:26.519Z_

```json
{
  "parentUuid": "05bf12a6-cb7f-4a28-96a4-9b3b3a2a9d4f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2aebc6f9-a688-4da3-8c44-cee6f968dde6",
  "timestamp": "2026-05-21T06:44:26.519Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
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
  "aiTitle": "Generate simulated research paper with IRT analysis",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e"
}
```

---

### Assistant

_source line 7 · 2026-05-21T06:44:28.936Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2aebc6f9-a688-4da3-8c44-cee6f968dde6",
  "isSidechain": false,
  "requestId": "req_011CbFG99GqxHBPcixMh5sg1",
  "type": "assistant",
  "uuid": "93405067-f3fe-460e-a787-d12c5da0315e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCxCZxoH56Gy9Boeru7NDM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11904,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11904
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

_source line 8 · 2026-05-21T06:44:29.549Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WA5tJZ4gqg6JPWwfmRV74V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93405067-f3fe-460e-a787-d12c5da0315e",
  "isSidechain": false,
  "requestId": "req_011CbFG99GqxHBPcixMh5sg1",
  "type": "assistant",
  "uuid": "cf3ab89e-9622-4c68-9733-631a997fa264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCxCZxoH56Gy9Boeru7NDM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11904,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11904
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

_source line 9 · 2026-05-21T06:44:30.068Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C9tJTUhFD3BnGryGSoKo9K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf3ab89e-9622-4c68-9733-631a997fa264",
  "isSidechain": false,
  "requestId": "req_011CbFG99GqxHBPcixMh5sg1",
  "type": "assistant",
  "uuid": "9d73c2c7-45a8-46aa-8ee6-c5742f3bc340",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCxCZxoH56Gy9Boeru7NDM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11904,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11904
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

_source line 10 · 2026-05-21T06:44:30.081Z_

<details><summary>↩ Tool result · `toolu_01C9tJTUhFD3BnGryGSoKo9K`</summary>

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
11	**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).
12	- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%)
13	- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.
14	- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.
15	
16	**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).
17	- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)
18	- Framing: aggressive — "the field's standard validation approach is fundamentally mismatched for item-level detection"
19	
20	**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).
21	- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)
22	- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks
23	- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability
24	
25	**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:
26	1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.
27	2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies "items that changed across generations," not "good items."
28	3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not "find bad items and remove" but "understand what changed and why." Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.
29	4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% BCa CI [−0.714, −0.155]; Spearman ρ=−0.403, p=0.020, CI [−0.687, −0.031]; partial r=−0.385 controlling GSM8K accuracy, p=0.030, CI [−0.640, −0.058]; permutation p=0.014). All CIs exclude zero. Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.
30	- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)
31	- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.
32	- Growing Pains互补: "Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading"
33	- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed
34	
35	## Story Spine (v2 — no-pivot narrative)
36	
37	**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.
38	
39	**Key narrative principle**: "Instability ≠ invalidity." DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**
40	
41	**What we find** (4 contributions, focused):
42	
43	1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for "models got better."
44	
45	2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.
46	
47	3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.
48	
49	4. **DIF as diagnostic lens**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. Cross-benchmark: DIF items resist contamination-based gains (r=−0.478, BCa CI [−0.71, −0.16]).
50	
51	**Headline result**: "Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF items resist contamination-based gains (r=−0.478) and serve as a diagnostic lens for understanding what changed across model generations."
52	
53	## Scope Control (main body vs appendix)
54	
55	**MAIN BODY (4 claims + robustness)**:
56	- §1 Introduction (problem + "instability ≠ invalidity" framing upfront)
57	- §2 Related Work (45 papers, 5 clusters)
58	- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)
59	- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)
60	- §5 Discussion + Limitations
61	- §6 Conclusion
62	
63	**APPENDIX (pruned from main body)**:
64	- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped
65	- RL robustness (plan_002) — N=13, underpowered
66	- Ensemble fusion (plan_003a/b/c) — negative, not executed
67	- Bifactor equating pilot — below target fit
68	- Item generation pilot — below benchmarks
69	- Graceful degradation — clean but supplementary
70	- Item-Focused Trees — robustness check, supplementary
71	- ConStat/DVD comparisons — complementary baselines
72	
73	## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks
74	
75	Systematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.
76	
77	## Venue Fit
78	
79	- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.
80	
81	## Novelty Articulation (三层，显式化)
82	
83	MH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:
84	
85	1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.
86	
87	2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).
88	
89	3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).
90	
91	**Framing**: "We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm."
92	
93	## Anticipated Reviewer Concerns (updated for pivot)
94	
95	1. **"38% could just mean models got better"** — ✅ RESOLVED (plan_019). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%). Subject-level ρ=0.307 is an ecological correlation that grossly overstates the item-level relationship (pseudo R²=0.0007). The instability is predominantly item-specific. Present Model 1 (2.4pp) as primary; acknowledge confounder-vs-mediator ambiguity in Model 2 as honest discussion.
96	
97	2. **"Ground truth critique is obvious — of course web labels don't capture differential effects"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.
98	
99	3. **"Semi-synthetic injection is artificial"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.
100	
101	4. **"DIF power is only sufficient for large effects"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.
102	
103	5. **"Only validated on MMLU"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.
104	
105	6. **"Higher methods (MIMIC, propensity-score) could solve the confounding"** — Acknowledged as future work. We frame our three-attempt negative results as "empirical observation" that motivates these directions, not as impossibility.
106	
107	7. **"ETS threshold is uncalibrated for LLM populations"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: "finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF." Do NOT claim ">15% at all thresholds" — be honest that 2.5 drops below.
108	
109	8. **"Multiple testing: 12,508 simultaneous tests without correction"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.
110	
111	9. **"Only uniform DIF — non-uniform DIF plausible for LLMs"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: "our 31% uniform-only estimate is conservative."
112	
113	10. **"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.
114	
115	11. **"Ranking disruption result is tautological"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.
116	
117	## Dropped from Original Framing
118	
119	- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.
120	- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.
121	- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.
122	- **Detection as primary contribution**: Pivoted from "we detect contamination" to "we characterize benchmark properties."
123	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d73c2c7-45a8-46aa-8ee6-c5742f3bc340",
  "isSidechain": false,
  "promptId": "f9190119-bc3e-4325-b2be-2617c4e8f5d7",
  "type": "user",
  "uuid": "8641069b-bf5f-4e62-8304-647a355fe67e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\"\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% BCa CI [−0.714, −0.155]; Spearman ρ=−0.403, p=0.020, CI [−0.687, −0.031]; partial r=−0.385 controlling GSM8K accuracy, p=0.030, CI [−0.640, −0.058]; permutation p=0.014). All CIs exclude zero. Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. Cross-benchmark: DIF items resist contamination-based gains (r=−0.478, BCa CI [−0.71, −0.16]).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF items resist contamination-based gains (r=−0.478) and serve as a diagnostic lens for understanding what changed across model generations.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"38% could just mean models got better\"** — ✅ RESOLVED (plan_019). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%). Subject-level ρ=0.307 is an ecological correlation that grossly overstates the item-level relationship (pseudo R²=0.0007). The instability is predominantly item-specific. Present Model 1 (2.4pp) as primary; acknowledge confounder-vs-mediator ambiguity in Model 2 as honest discussion.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n",
      "numLines": 123,
      "startLine": 1,
      "totalLines": 123
    }
  },
  "sourceToolAssistantUUID": "9d73c2c7-45a8-46aa-8ee6-c5742f3bc340",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "8641069b-bf5f-4e62-8304-647a355fe67e",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with IRT analysis",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e"
}
```

---

### Tool result

_source line 13 · 2026-05-21T06:44:30.565Z_

<details><summary>↩ Tool result · `toolu_01WA5tJZ4gqg6JPWwfmRV74V`</summary>

```text
1	[
2	  {
3	    "name": "real_data_dif_mmlu",
4	    "description": "METABENCH MMLU 全量 DIF 分析。temporal/ability/within-family 三种 cohort 定义， 加 Li et al. proxy validation 和 domain specificity。\n",
5	    "results": {
6	      "temporal_ets_c_pct": 31.3,
7	      "temporal_n_c_items": 3918,
8	      "temporal_n_total": 12508,
9	      "temporal_fpr_on_li_clean": 0.318,
10	      "temporal_enrichment_ratio": 0.96,
11	      "ability_ets_c_pct": 2.9,
12	      "ability_enrichment": 1.19,
13	      "within_family_llama2v3_c_pct": 61.3,
14	      "within_family_mistral_mixtral_c_pct": 38.7,
15	      "domain_spearman_rho": 0.307,
16	      "domain_spearman_p": 0.02,
17	      "sanity_random_split_c_pct": 0.18,
18	      "temporal_ability_jaccard": 0.014
19	    },
20	    "tables": [
21	      {
22	        "name": "Table 1: Temporal DIF Summary by ETS Classification",
23	        "columns": [
24	          "ets_class",
25	          "n_items",
26	          "pct",
27	          "mean_abs_delta_mh"
28	        ],
29	        "rows": [
30	          [
31	            "A (negligible)",
32	            8590,
33	            68.7,
34	            0.43
35	          ],
36	          [
37	            "B (moderate)",
38	            2641,
39	            21.1,
40	            1.24
41	          ],
42	          [
43	            "C (large)",
44	            1277,
45	            10.2,
46	            2.31
47	          ],
48	          [
49	            "B+C (flagged)",
50	            3918,
51	            31.3,
52	            1.58
53	          ]
54	        ]
55	      },
56	      {
57	        "name": "Table 2: Cohort Definition Sensitivity",
58	        "columns": [
59	          "cohort",
60	          "n_ref",
61	          "n_foc",
62	          "c_pct",
63	          "enrichment"
64	        ],
65	        "rows": [
66	          [
67	            "temporal (2023 vs 2024-H1)",
68	            1253,
69	            656,
70	            31.3,
71	            0.96
72	          ],
73	          [
74	            "ability (Q1 vs Q5)",
75	            "~1044",
76	            "~1044",
77	            2.9,
78	            1.19
79	          ],
80	          [
81	            "within-family (Llama-2 vs 3)",
82	            161,
83	            308,
84	            61.3,
85	            "—"
86	          ],
87	          [
88	            "random split (sanity)",
89	            950,
90	            950,
91	            0.18,
92	            "—"
93	          ]
94	        ]
95	      }
96	    ],
97	    "figures": [],
98	    "analysis": "Median 档下 plan_001 是 paper 的基石。数据本身不受质疑，但 \"so what\" 需要后续实验 (plan_019, plan_017, plan_020) 支撑。评审预期反应： R1: \"Impressive scale, but what does 31% instability mean for practitioners?\" R2: \"The enrichment≈1.0 result is interesting but undermines the contamination framing\" R3: \"Within-family results suggest capability gain, not contamination\" 总体：plan_001 在 median 档得 strong accept 作为 empirical contribution， 但单独不够——需要 downstream impact story。\n\n\nmedian 档下这些数值本身站得住——31.3% 是 robust 的经验发现，random-split sanity (0.18%) 排除统计伪影， domain ρ=0.307 是 modest ecological correlation。问题不在数字，在解读： 1) enrichment≈1.0 证明 DIF 和 web-overlap labels 正交，但评审会问 \"if DIF doesn't correlate with known contamination, what IS it detecting?\"——需要 plan_019 decomposition 才能回答 \"item-specific instability, not capability gain\"。 2) within-family C%=61.3% (Llama-2 vs 3) 远高于 cross-cohort 31.3%，评审会质疑 \"within-family analysis proves capability gain drives DIF, not contamination\"。 Median 档下 1 个评审接受 \"capability gain ≠ item instability\" 论证，1 个不接受。 3) domain ρ=0.307 (p=0.02) 在 median 档被视为 \"interesting but not definitive\"， 不被攻击也不加分。\n"
99	  },
100	  {
101	    "name": "rl_robustness_validation",
102	    "description": "验证 DIF 在 RL-trained 模型上的鲁棒性。SFT baseline vs alignment-RL (DPO/ORPO) vs reasoning-RL (GRPO/PPO)。关键在于 reasoning-RL 只有 10-15 个模型。\n",
103	    "results": {
104	      "sft_cohort_n": 312,
105	      "alignment_rl_cohort_n": 477,
106	      "reasoning_rl_models_collected": 13,
107	      "sft_vs_alignment_jaccard_dif_flags": 0.72,
108	      "sft_temporal_c_pct": 30.8,
109	      "alignment_rl_temporal_c_pct": 32.1,
110	      "combined_with_reasoning_rl_c_pct": 31.5,
111	      "jaccard_base_vs_rl_augmented": 0.91,
112	      "tost_equivalence_p": 0.14,
113	      "tost_equivalence_bound": 0.05,
114	      "tost_verdict": "inconclusive",
115	      "mink_auroc_sft": 0.61,
116	      "mink_auroc_alignment_rl": 0.58,
117	      "mink_auroc_reasoning_rl": 0.43,
118	      "constat_auroc_sft": 0.64,
119	      "constat_auroc_reasoning_rl": 0.39,
120	      "delong_p_mink_sft_vs_rl": 0.08,
121	      "delong_p_constat_sft_vs_rl": 0.03,
122	      "bootstrap_ci_auroc_diff_mink": [
123	        -0.02,
124	        0.38
125	      ],
126	      "bootstrap_ci_auroc_diff_constat": [
127	        0.04,
128	        0.46
129	      ],
130	      "power_analysis_delta_boundary": 1.1,
131	      "power_analysis_tpr_at_boundary": 0.42
132	    },
133	    "tables": [
134	      {
135	        "name": "Table: DIF Flag Stability Under Cohort Composition Change",
136	        "columns": [
137	          "cohort_composition",
138	          "n_total",
139	          "c_pct",
140	          "jaccard_vs_baseline"
141	        ],
142	        "rows": [
143	          [
144	            "SFT only",
145	            312,
146	            30.8,
147	            "—"
148	          ],
149	          [
150	            "SFT + alignment-RL",
151	            789,
152	            32.1,
153	            0.72
154	          ],
155	          [
156	            "SFT + alignment-RL + reasoning-RL",
157	            802,
158	            31.5,
159	            0.91
160	          ]
161	        ]
162	      },
163	      {
164	        "name": "Table: Individual Detector AUROC by Model Type",
165	        "columns": [
166	          "detector",
167	          "sft",
168	          "alignment_rl",
169	          "reasoning_rl",
170	          "delong_p"
171	        ],
172	        "rows": [
173	          [
174	            "Min-K%",
175	            0.61,
176	            0.58,
177	            0.43,
178	            0.08
179	          ],
180	          [
181	            "ConStat",
182	            0.64,
183	            0.6,
184	            0.39,
185	            0.03
186	          ],
187	          [
188	            "DIF (group)",
189	            "—",
190	            "—",
191	            "—",
192	            "N/A"
193	          ]
194	        ]
195	      }
196	    ],
197	    "figures": [],
198	    "analysis": "Median 档下 plan_002 是最弱的实验。N=13 reasoning-RL 无法支撑任何统计结论。 TOST inconclusive 意味着既不能声称 robust 也不能声称 fragile。 最佳策略：power analysis 图放 appendix，主文用一句话承认 \"reasoning-RL validation remains underpowered (N=13); alignment-RL cohort (N=477) shows stable DIF flags (Jaccard=0.72 vs SFT)\"。不把 RL robustness 作为 claim。\n\n\nMedian 档核心问题：N=13 reasoning-RL 模型严重不足。 1) Group-level DIF flags 在加入 13 个 RL 模型后变化很小 (Jaccard=0.91)，因为 N=13 在 N≈1900 focal cohort 中占比 <1%，统计上几乎无影响。评审会正确指出 \"this doesn't prove RL robustness, it proves RL models are too few to matter\"。 2) TOST 等价性检验 p=0.14 不显著——无法证明等价，也无法证明差异。 Median 档评审判断：inconclusive，移至 limitations。 3) 个体模型检测：ConStat 在 reasoning-RL 上 AUROC 降至 0.39 (显著下降)， 但 DIF 是 group-level 无法做个体比较，comparison 不对等。 4) Power analysis 有理论价值：δ<1.1 时 TPR<0.42，清晰刻画了 detection boundary。 但评审会说 \"you characterized a limitation, not solved it\"。 总体：plan_002 在 median 档被降级为 appendix，N=13 是 fatal underpowering。\n"
199	  },
200	  {
201	    "name": "constat_perturbation_eval",
202	    "description": "独立评估 ConStat-style perturbation testing 在 MMLU 上的检测力。 200+ items paraphrased，comparison with DIF flags。\n",
203	    "results": {
204	      "n_items_paraphrased": 217,
205	      "paraphrase_quality_human_eval": 0.78,
206	      "constat_detection_rate_fdr005": 0.23,
207	      "constat_detection_rate_fdr010": 0.31,
208	      "constat_dif_overlap_jaccard": 0.08,
209	      "constat_fpr_on_clean_items": 0.06,
210	      "constat_effect_size_non_rl": 0.74,
211	      "constat_effect_size_rl": 0.31,
212	      "paraphrase_difficulty_shift_mean": 0.12,
213	      "paraphrase_difficulty_shift_std": 0.34,
214	      "n_models_tested": 15,
215	      "gpu_hours_used": 62
216	    },
217	    "tables": [
218	      {
219	        "name": "Table: ConStat Detection Summary",
220	        "columns": [
221	          "metric",
222	          "non_rl_models",
223	          "rl_models",
224	          "all"
225	        ],
226	        "rows": [
227	          [
228	            "n_models",
229	            11,
230	            4,
231	            15
232	          ],
233	          [
234	            "detection_rate_fdr005",
235	            0.27,
236	            0.14,
237	            0.23
238	          ],
239	          [
240	            "mean_effect_size",
241	            0.74,
242	            0.31,
243	            0.61
244	          ],
245	          [
246	            "FPR",
247	            0.05,
248	            0.08,
249	            0.06
250	          ]
251	        ]
252	      }
253	    ],
254	    "figures": [],
255	    "analysis": "Median 档下 plan_003a 提供了有价值的 baseline comparison，但不构成独立贡献。 ConStat-DIF orthogonality (Jaccard=0.08) 支持 meta-critique (不同方法 capture 不同 aspects)，但 N=15 模型限制了结论强度。适合 appendix 作为 related work empirical comparison，不适合 main body。\n\n\nMedian 档：ConStat 实验执行了但结果 mixed。 1) Paraphrase 质量 78% human-eval acceptable——约 22% 的 reformulation 引入了 subtle semantic shift，导致 difficulty 变化不纯粹来自 contamination。 评审会质疑 paraphrase 质量是 confound。 2) FDR-controlled detection rate 23% 在 non-RL 模型上——reasonable baseline 但 不 impressive。Jaccard=0.08 与 DIF 几乎无 overlap，说明两者 detect 不同 signal。 3) RL 模型上 effect size 从 0.74 降至 0.31——方向正确但 N=15 模型下 CI 非常宽。 4) 核心问题：ConStat 需要 inference access (running paraphrased items through models)， 而 METABENCH 只有 original responses。所以 ConStat 只在 15 个有 inference access 的模型上跑，vs DIF 用全部 5,227 模型。Scale 不可比。 Median 档评审判断：\"useful baseline comparison but limited by small inference sample\"。\n"
256	  },
257	  {
258	    "name": "dvd_generation_variance_eval",
259	    "description": "DVD generation variance 在 MMLU 上的独立评估。50 responses/item via temperature sampling。\n",
260	    "results": {
261	      "n_models_tested": 12,
262	      "n_items_tested": 500,
263	      "responses_per_item": 50,
264	      "temperature": 0.8,
265	      "bimodal_detection_rate": 0.14,
266	      "bimodal_verbatim_contamination": 0.31,
267	      "bimodal_variant_contamination": 0.06,
268	      "dvd_dif_overlap_jaccard": 0.05,
269	      "dvd_fpr": 0.09,
270	      "variance_score_reliability": 0.62,
271	      "gpu_hours_used": 58
272	    },
273	    "tables": [
274	      {
275	        "name": "Table: DVD Detection by Contamination Type",
276	        "columns": [
277	          "contamination_type",
278	          "n_items_tested",
279	          "bimodal_rate",
280	          "fpr"
281	        ],
282	        "rows": [
283	          [
284	            "verbatim",
285	            150,
286	            0.31,
287	            0.08
288	          ],
289	          [
290	            "variant",
291	            150,
292	            0.06,
293	            0.1
294	          ],
295	          [
296	            "clean",
297	            200,
298	            "—",
299	            0.09
300	          ]
301	        ]
302	      }
303	    ],
304	    "figures": [],
305	    "analysis": "Median 档下 plan_003b 是最弱的独立实验。Detection power 低于 ConStat， 且需要 open-weight inference access。主要价值是证明 \"generation variance alone is insufficient\"——但这不是 surprising finding。Appendix material at best。 在 median 档的策略调整中，plan_003b 应被 deprioritized。\n\n\nMedian 档：DVD 结果较弱。 1) 只有 14% 的 items 显示 bimodal generation variance——远低于 DIF 的 31.3%， 说明 generation variance 作为 contamination signal 灵敏度较低。 2) Verbatim contamination (31% bimodal) vs variant contamination (6% bimodal)： DVD 几乎只能 detect verbatim memorization，对 variant 无力。 3) 与 DIF 的 overlap 近乎为零 (Jaccard=0.05)，再次说明不同方法 capture 不同 signal。 4) Variance score reliability 0.62——moderate at best。50 responses 可能不足以 稳定估计 variance，但 GPU budget 已耗尽。 5) 核心限制：DVD 需要 open-weight + inference，排除 closed-source models。 Median 档评审：\"limited detection power, primarily captures verbatim memorization which is already detectable by simpler methods (n-gram matching)\"。\n"
306	  },
307	  {
308	    "name": "ensemble_fusion",
309	    "description": "DIF + ConStat + DVD 三信号 ensemble。依赖 003a 和 003b。\n",
310	    "results": {
311	      "ensemble_auroc_2of3": 0.58,
312	      "ensemble_auroc_weighted": 0.62,
313	      "ensemble_fpr_2of3": 0.11,
314	      "ensemble_fpr_weighted": 0.09,
315	      "dif_standalone_auroc": 0.54,
316	      "constat_standalone_auroc": 0.51,
317	      "dvd_standalone_auroc": 0.47,
318	      "ensemble_improvement_over_best_single": 0.08,
319	      "cross_val_weight_stability": 0.43,
320	      "fpr_below_010_pct_configs": 0.45
321	    },
322	    "tables": [
323	      {
324	        "name": "Table: Ensemble vs Individual Detectors",
325	        "columns": [
326	          "method",
327	          "auroc",
328	          "fpr",
329	          "n_models_available"
330	        ],
331	        "rows": [
332	          [
333	            "DIF (MH)",
334	            0.54,
335	            0.31,
336	            5227
337	          ],
338	          [
339	            "ConStat",
340	            0.51,
341	            0.06,
342	            15
343	          ],
344	          [
345	            "DVD",
346	            0.47,
347	            0.09,
348	            12
349	          ],
350	          [
351	            "2-of-3 majority",
352	            0.58,
353	            0.11,
354	            12
355	          ],
356	          [
357	            "weighted fusion",
358	            0.62,
359	            0.09,
360	            12
361	          ]
362	        ]
363	      }
364	    ],
365	    "figures": [],
366	    "analysis": "Median 档下 plan_003c 被 drop 是正确决策。Ensemble 面临三重困难： (a) ground truth circularity, (b) small-N signal components, (c) marginal improvement。 Paper framing 已正确将 ensemble 移至 \"future work\"。 在 rebuttal 中，如果评审问 \"why not ensemble?\"，回答是 \"ensemble requires validated ground truth, which our Claim 2 shows doesn't exist; building the ground truth infrastructure (Claim 3) is prerequisite\"。\n\n\nMedian 档：ensemble 无法达到预期目标。 1) FPR<0.10 只在 45% 的配置下成立——不满足 \"across all configurations\" 的目标。 Weighted fusion FPR=0.09 勉强达标，但 cross-val weight stability=0.43 说明 weights 在 folds 之间不稳定，overfitting risk 高。 2) AUROC 提升 +0.08 over best single signal——marginal，且受限于 ground truth 的质量（Li et al. labels 作为 ground truth 本身是 plan 质疑的对象）。 3) 根本矛盾：paper 的 Claim 2 论证 web-overlap labels 不适合评估 item-level detectors，然后用这些 labels 训练 ensemble weights。评审会指出 circularity。 4) 003a/003b 的小样本 (N=12-15 models) 使得 ensemble 的 training data 极有限。 Median 档评审：\"the ensemble adds complexity without resolving the fundamental ground truth problem the paper itself identifies\"。\n"
367	  },
368	  {
369	    "name": "cross_benchmark_gsm8k",
370	    "description": "GSM8K 上复制 DIF 分析，GSM1K 作为 contamination ground truth。三步： temporal DIF → semi-synthetic → GSM1K correlation。\n",
371	    "results": {
372	      "step1_gsm8k_n_items": 1319,
373	      "step1_n_ref": 1017,
374	      "step1_n_foc": 804,
375	      "step1_standard_c_pct": 18.9,
376	      "step1_external_c_pct": 47.4,
377	      "step1_sanity_c_pct": 0.3,
378	      "step1_standard_external_spearman": 0.926,
379	      "step2_standard_delta_tpr_p10": 0.818,
380	      "step2_external_delta_tpr_p10": 0.517,
381	      "step3_n_models": 33,
382	      "step3_pearson_r": -0.478,
383	      "step3_pearson_p": 0.005,
384	      "step3_spearman_rho": -0.403,
385	      "step3_spearman_p": 0.02,
386	      "step3_partial_r": -0.385,
387	      "step3_partial_p": 0.027,
388	      "step3_bca_ci_pearson": [
389	        -0.714,
390	        -0.155
391	      ],
392	      "step3_bca_ci_spearman": [
393	        -0.687,
394	        -0.031
395	      ],
396	      "step3_permutation_p": 0.014
397	    },
398	    "tables": [
399	      {
400	        "name": "Table: GSM8K Temporal DIF Summary",
401	        "columns": [
402	          "matching",
403	          "c_pct",
404	          "sanity_c_pct",
405	          "delta_tpr_p10"
406	        ],
407	        "rows": [
408	          [
409	            "standard (total score)",
410	            18.9,
411	            0.3,
412	            0.818
413	          ],
414	          [
415	            "external (MMLU score)",
416	            47.4,
417	            "—",
418	            0.517
419	          ]
420	        ]
421	      },
422	      {
423	        "name": "Table: GSM1K Correlation (Step 3) — Reviewer Critique Points",
424	        "columns": [
425	          "statistic",
426	          "value",
427	          "95% CI",
428	          "reviewer_concern"
429	        ],
430	        "rows": [
431	          [
432	            "Pearson r",
433	            -0.478,
434	            "[-0.714, -0.155]",
435	            "CI wide"
436	          ],
437	          [
438	            "Spearman ρ",
439	            -0.403,
440	            "[-0.687, -0.031]",
441	            "upper bound near zero"
442	          ],
443	          [
444	            "Partial r",
445	            -0.385,
446	            "[-0.640, -0.058]",
447	            "controlling accuracy helps marginally"
448	          ],
449	          [
450	            "N",
451	            33,
452	            "—",
453	            "underpowered"
454	          ]
455	        ]
456	      }
457	    ],
458	    "figures": [],
459	    "analysis": "Median 档下 plan_004 是 mixed outcome。Step 1+2 加强 Claim 1+3 的 cross-benchmark generalizability故事，Step 3 是 liability。正确策略是： 主文用 Step 1+2 证明 \"DIF and semi-synthetic framework generalize to GSM8K\"， Step 3 降级至 appendix with explicit caveat \"suggestive evidence requiring replication with larger matched sample (N≥100)\"。\n\n\nMedian 档核心动态：Step 1+2 稳固，Step 3 被 dismiss。 1) Step 1: GSM8K C%=18.9% (低于 MMLU 31.3%) 合理——GSM8K 是 math domain， temporal capability gain 更 uniform，所以 differential 更少。评审接受。 2) Step 2: ΔTPR=+0.818 非常强——比 MMLU 的 +0.674 还好，因为 GSM8K 是 single-domain，within-subject/cross-subject 区分不 applicable，matching 更干净。 Semi-synthetic framework portability 得到确认，Claim 3 加分。 3) Step 3: r=-0.478, p=0.005 但 N=33，BCa CI upper bound |r|=0.155。 Median 档下 1-2 个评审直接 dismiss： - \"N=33 with Spearman CI touching zero (−0.031) — underpowered\" - \"BCa CI [−0.714, −0.155] is too wide to be informative\" - \"contamination gap is itself a noisy proxy\" 方向正确 (negative correlation = DIF items resist contamination gains) 但 统计力不足以成为 independent evidence。 4) 策略：median 档下 Step 3 从 Claim 4 子发现降级至 appendix \"suggestive evidence\"， Claim 4 主要靠 plan_017 z-score + plan_020 circularity ablation。\n"
460	  },
461	  {
462	    "name": "bifactor_irt_equating_pilot",
463	    "description": "在 MMLU 上拟合 bifactor IRT 模型 (general + 57 subject-specific factors)， 选择 anchor items，执行 fixed-parameter calibration 的 equating pilot。\n",
464	    "results": {
465	      "bifactor_convergence": true,
466	      "bifactor_iterations": 2847,
467	      "rmsea": 0.052,
468	      "cfi": 0.81,
469	      "tli": 0.78,
470	      "srmr": 0.068,
471	      "general_factor_variance_explained": 0.34,
472	      "subject_factors_variance_explained": 0.41,
473	      "residual_variance": 0.25,
474	      "n_anchor_items_selected": 1200,
475	      "anchor_selection_criterion": "no DIF + discrimination > 0.5 + fit residual < 2.0",
476	      "equated_rho_vs_original": 0.94,
477	      "equated_rho_target": 0.95,
478	      "target_met": false,
479	      "computation_time_hours": 38,
480	      "memory_peak_gb": 127
481	    },
482	    "tables": [
483	      {
484	        "name": "Table: Bifactor IRT Fit Indices",
485	        "columns": [
486	          "index",
487	          "value",
488	          "conventional_threshold",
489	          "interpretation"
490	        ],
491	        "rows": [
492	          [
493	            "RMSEA",
494	            0.052,
495	            "<0.06 acceptable",
496	            "borderline acceptable"
497	          ],
498	          [
499	            "CFI",
500	            0.81,
501	            ">0.90 good",
502	            "below threshold"
503	          ],
504	          [
505	            "TLI",
506	            0.78,
507	            ">0.90 good",
508	            "below threshold"
509	          ],
510	          [
511	            "SRMR",
512	            0.068,
513	            "<0.08 acceptable",
514	            "acceptable"
515	          ],
516	          [
517	            "general factor % variance",
518	            "34%",
519	            ">50% for unidimensional",
520	            "confirms multidimensionality"
521	          ]
522	        ]
523	      }
524	    ],
525	    "figures": [],
526	    "analysis": "Median 档下 plan_005 验证了 IRT misspecification 但未解决它。 34% general factor variance 是回应 \"IRT misspecification\" concern 的有力数据—— 证明 1D IRT 确实不足，但 DIF finding 的方向和规模不受根本影响 (因为 bifactor 校正后 C% 从 31.3% 只降至 ~28-29%，仍然 substantial)。 关键洞察：评审要求的不是 \"fix the misspecification\"，而是 \"show DIF findings are robust TO the misspecification\"。Plan_005 可以回答这个——如果 bifactor 校正后 DIF 发现 qualitatively 不变，那就是 robustness evidence。 策略：不把 equating 当 claim，而是作为 IRT sensitivity analysis 放 appendix。\n\n\nMedian 档：bifactor 收敛但 fit 指标 mediocre。 1) RMSEA=0.052 在 acceptable range (< 0.06) 但不 good (< 0.05)。 CFI=0.81 和 TLI=0.78 低于常规 threshold (0.90)——这是 12,508 items × 5,227 models 的规模效应，absolute fit indices 在超大规模下系统偏低。 评审如果懂 psychometrics 会接受，不懂会直接攻击 \"poor model fit\"。 2) General factor 只解释 34% variance——MMLU 的 57 subject 确实 highly multidimensional，这 validates \"1D IRT is misspecified\" 的论点。 3) Equating ρ=0.94 未达 0.95 target——marginal miss。Plan_014 within-subject pre-check (38.1% C%) 已经预示 DIF 在 bifactor 校正后不会大幅下降。 4) 计算成本高 (38 hours, 127GB RAM)——scalability concern。 Median 档评审反应： - 支持者：\"bifactor results validate the multidimensionality concern and motivate\n  future work on MIRT-based DIF\"\n- 反对者：\"CFI=0.81 means the model doesn't fit, equating results are unreliable\" 总体：pilot 结果 suggestive 但不 conclusive，适合 limitations/future work。\n"
527	  },
528	  {
529	    "name": "item_generation_calibration",
530	    "description": "为 DIF-flagged items 生成替代题目，用 student simulation 校准难度。\n",
531	    "results": {
532	      "n_items_generated": 150,
533	      "difficulty_correlation_prompt_based": 0.32,
534	      "difficulty_correlation_student_sim": 0.58,
535	      "difficulty_correlation_target": 0.75,
536	      "target_met": false,
537	      "cognitive_level_match_rate": 0.71,
538	      "subject_match_rate": 0.95,
539	      "human_quality_rating": 3.2,
540	      "human_quality_scale": "1-5",
541	      "holdout_panel_rho": 0.52,
542	      "gpu_hours_used": 145
543	    },
544	    "tables": [
545	      {
546	        "name": "Table: Item Generation Difficulty Calibration",
547	        "columns": [
548	          "method",
549	          "difficulty_ρ",
550	          "n_items",
551	          "notes"
552	        ],
553	        "rows": [
554	          [
555	            "prompt-based targeting",
556	            0.32,
557	            150,
558	            "below literature 0.10-0.45"
559	          ],
560	          [
561	            "student simulation",
562	            0.58,
563	            150,
564	            "below target 0.75"
565	          ],
566	          [
567	            "combined (iterative)",
568	            0.61,
569	            80,
570	            "2-round refinement"
571	          ]
572	        ]
573	      }
574	    ],
575	    "figures": [],
576	    "analysis": "Median 档下 plan_006 是 expected negative。Item generation 是 hard open problem， failure 不损害核心 paper 因为 regeneration 已从 claims 中 drop。 唯一价值：作为 future work 动机——\"automated benchmark maintenance requires better item generation, which remains an open problem\"。\n\n\nMedian 档：item generation 是 paper 最弱的环节之一。 1) Prompt-based difficulty targeting ρ=0.32 远低于文献报告的 0.45 upper bound—— MMLU 的 multiple-choice 格式和 domain diversity 使 prompt 控制困难。 2) Student simulation 提升到 ρ=0.58 (vs 文献 0.75-0.82 on simpler benchmarks)—— MMLU 的 57 domains 使 simulation calibration 更难泛化。 3) Cognitive level match rate 71%——约 29% 的 generated items 测量不同的 cognitive level，这是 construct validity threat。 4) Holdout panel ρ=0.52——远低于 equating 需要的精度。 Median 档评审会直接判定 item generation 不成熟：\"generated items don't match target difficulty well enough for equating; this is a negative result\"。 策略：plan_006 在 median 档是 negative result，移至 appendix 作为 \"current limitations of LLM-based item generation for benchmark maintenance\"。 不影响核心 claims。\n"
577	  },
578	  {
579	    "name": "cumulative_bayesian_dif",
580	    "description": "实现 Sinharay et al. (2006) 的 cumulative Bayesian DIF prior。 模拟 4 次 successive benchmark administration，展示 evidence 累积带来的 power 提升。\n",
581	    "results": {
582	      "simulation_n_administrations": 4,
583	      "admin_1_power_delta10": 0.41,
584	      "admin_2_power_delta10": 0.56,
585	      "admin_3_power_delta10": 0.68,
586	      "admin_4_power_delta10": 0.74,
587	      "target_admin3_power": 0.7,
588	      "target_met": false,
589	      "admin_3_power_delta14": 0.82,
590	      "fpr_cumulative": 0.048,
591	      "fpr_stable_across_admins": true,
592	      "bayes_factor_median_admin3": 4.2,
593	      "simulation_n_items": 500,
594	      "simulation_n_models_per_admin": 200,
595	      "computation_time_hours": 6
596	    },
597	    "tables": [
598	      {
599	        "name": "Table: Cumulative Power by Administration",
600	        "columns": [
601	          "n_admins",
602	          "power_delta_10",
603	          "power_delta_14",
604	          "power_delta_16",
605	          "fpr"
606	        ],
607	        "rows": [
608	          [
609	            1,
610	            0.41,
611	            0.68,
612	            0.72,
613	            0.042
614	          ],
615	          [
616	            2,
617	            0.56,
618	            0.77,
619	            0.83,
620	            0.045
621	          ],
622	          [
623	            3,
624	            0.68,
625	            0.82,
626	            0.89,
627	            0.048
628	          ],
629	          [
630	            4,
631	            0.74,
632	            0.86,
633	            0.92,
634	            0.047
635	          ]
636	        ]
637	      }
638	    ],
639	    "figures": [],
640	    "analysis": "Median 档下 plan_007 有 modest value 作为 forward-looking contribution。 核心问题：ML 评审对 \"future benchmark administrations\" 的 temporal framing 不熟悉——psychometrics 中 repeated test administration 是常态， 但 LLM benchmarks 通常是 one-shot。需要明确解释 \"as new model generations emerge, the same benchmark is effectively re-administered\"。 Appendix 放置，主文 limitations 中一句话提及 cumulative power improvement 可能性。\n\n\nMedian 档：simulation 结果方向正确但 target 未达。 1) 3 次 administration 后 δ=1.0 的 power 从 0.41 升至 0.68——接近但未达 0.70 target。 δ=1.4 时 0.82 是可用的，说明 cumulative approach 有价值但主要对 medium effects。 2) FPR 控制良好 (0.048)，Bayesian prior 没有引入 FPR inflation。 3) 核心限制：这是 pure simulation，没有 real data validation。 METABENCH 只有一个 \"administration\"（没有 temporal sub-cohorts fine enough for 4 successive periods）。 4) Median 档评审：\"simulation-only result without empirical validation; interesting but speculative\"。 策略：appendix material。展示 concept 可行性但承认需要真实数据验证。 如果 ICLR 评审不熟悉 Bayesian DIF，这部分可能被完全忽略。\n"
641	  },
642	  {
643	    "name": "graceful_degradation_analysis",
644	    "description": "分析 benchmark validity 在 progressive item replacement 下的退化模式。\n",
645	    "results": {
646	      "replacement_5pct_rho": 0.998,
647	      "replacement_10pct_rho": 0.995,
648	      "replacement_20pct_rho": 0.987,
649	      "replacement_50pct_rho": 0.961,
650	      "reliability_5pct_alpha": 0.943,
651	      "reliability_10pct_alpha": 0.938,
652	      "reliability_20pct_alpha": 0.924,
653	      "reliability_50pct_alpha": 0.891,
654	      "original_alpha": 0.946,
655	      "construct_coverage_20pct_subjects_lost": 0,
656	      "construct_coverage_50pct_subjects_lost": 3,
657	      "validity_floor_replacement_pct": 0.35,
658	      "validity_floor_criterion": "ρ > 0.98 AND α > 0.92"
659	    },
660	    "tables": [
661	      {
662	        "name": "Table: Validity Metrics Under Progressive Replacement",
663	        "columns": [
664	          "replacement_pct",
665	          "rank_ρ",
666	          "cronbach_α",
667	          "subjects_under_represented"
668	        ],
669	        "rows": [
670	          [
671	            0,
672	            1.0,
673	            0.946,
674	            0
675	          ],
676	          [
677	            5,
678	            0.998,
679	            0.943,
680	            0
681	          ],
682	          [
683	            10,
684	            0.995,
685	            0.938,
686	            0
687	          ],
688	          [
689	            20,
690	            0.987,
691	            0.924,
692	            0
693	          ],
694	          [
695	            35,
696	            0.974,
697	            0.908,
698	            1
699	          ],
700	          [
701	            50,
702	            0.961,
703	            0.891,
704	            3
705	          ]
706	        ]
707	      }
708	    ],
709	    "figures": [],
710	    "analysis": "Median 档下 plan_008 的主要贡献是量化 \"how much replacement is safe\"—— 35% validity floor 直接对应 \"31% DIF items can be safely replaced without validity loss\"。这 strengthens the \"instability ≠ invalidity\" narrative。 但 plan_006 的 negative result 使得 \"replacement\" 变成 theoretical exercise。\n\n\nMedian 档：graceful degradation 结果 clean 且 informative。 1) ρ 从 0.998 (5%) 到 0.961 (50%) 的退化曲线非常 smooth——MMLU 的 12,508 items 有 massive redundancy，即使替换 50% items 排名仍 strongly correlated。 这 complements plan_017 (ρ=0.997 after removing 31% DIF items)。 2) Reliability (Cronbach's α) 从 0.946 到 0.891——20% 是 practical threshold， 之后 reliability 下降加速。 3) Construct coverage：50% replacement 时 3 个 subjects 可能 under-represented (small subjects with few items)。 4) 核心问题：replacement 假设 generated items 质量 OK——但 plan_006 显示 generation 质量不足。所以 \"graceful degradation\" 只在理论层面成立。 Median 档评审：\"nice analysis but moot without better item generation (plan_006 failed)\"。 策略：clean supplementary result，放 appendix。主文用 \"validity floor at ~35% replacement\" 作为 practical recommendation。\n"
711	  },
712	  {
713	    "name": "item_focused_trees",
714	    "description": "Tutz & Berger (2016) Item-Focused Trees 作为 categorical DIF 的替代方案。 Treat model release date as continuous covariate。\n",
715	    "results": {
716	      "n_items_analyzed": 12508,
717	      "n_items_with_significant_split": 4127,
718	      "pct_items_with_split": 33.0,
719	      "primary_split_date": "2023-11-15",
720	      "concordance_with_mh_ets_c": 0.78,
721	      "additional_items_detected": 209,
722	      "items_missed_by_ift": 612,
723	      "jaccard_mh_vs_ift": 0.68,
724	      "computational_time_hours": 12,
725	      "n_items_nonlinear_trend": 1834,
726	      "pct_nonlinear": 14.7
727	    },
728	    "tables": [
729	      {
730	        "name": "Table: MH vs IFT Concordance",
731	        "columns": [
732	          "metric",
733	          "mh_ets_c",
734	          "ift_significant",
735	          "overlap",
736	          "jaccard"
737	        ],
738	        "rows": [
739	          [
740	            "n_flagged",
741	            3918,
742	            4127,
743	            3306,
744	            0.68
745	          ],
746	          [
747	            "pct_flagged",
748	            31.3,
749	            33.0,
750	            26.4,
751	            "—"
752	          ]
753	        ]
754	      }
755	    ],
756	    "figures": [],
757	    "analysis": "Median 档下 plan_009 的 concordance=0.78 有两面性： - 支持：MH 的 categorical split 不是 artifact，IFT confirms temporal instability - 质疑：22% discordance 说明 method choice matters，results are partially method-dependent 评审在 median 档接受 IFT 作为 robustness check，不会深入追究 discordance。\n\n\nMedian 档：IFT 是有价值的 robustness check 但不改变 narrative。 1) 33% items with significant split vs MH 31.3%——high concordance (0.78)， 说明 categorical temporal split 不是 arbitrary 的。 2) Primary split date 2023-11-15——接近 GPT-4/Llama-2 到 Llama-3/Mixtral 的代际转换点，有 face validity。 3) IFT detects 209 additional items that MH misses (mostly items with gradual drift rather than sharp shift)，同时 misses 612 items MH catches (mostly items where DIF is large but not monotone in date)。 4) 14.7% nonlinear trends——说明 some items 的 DIF 不是 monotone temporal， 暗示 \"contamination + capability gain + item drift\" 的 multi-factor story。 Median 档评审：\"useful supplementary analysis, confirms MH results are not artifacts of the cohort split\"。不改变 claims 但提供 methodological robustness。 策略：appendix 的 robustness check。主文一句话：\"IFT with continuous release date yields 78% concordance with MH categorical DIF (Appendix X)\"。\n"
758	  },
759	  {
760	    "name": "architecture_stratified_dif",
761	    "description": "在 decoder-only 子群内重跑 DIF，检验 architecture heterogeneity 是否影响 IRT fit。\n",
762	    "results": {
763	      "n_decoder_only": 5226,
764	      "n_non_decoder": 1,
765	      "pct_decoder_only": 99.98,
766	      "decoder_only_c_pct": 31.3,
767	      "full_population_c_pct": 31.3,
768	      "jaccard_decoder_vs_full": 1.0,
769	      "irt_rmsea_full": 0.089,
770	      "irt_rmsea_decoder_only": 0.088,
771	      "irt_cfi_full": 0.72,
772	      "irt_cfi_decoder_only": 0.72,
773	      "irt_fit_improvement": "negligible",
774	      "pct_models_lz_gt2": 98.0
775	    },
776	    "tables": [
777	      {
778	        "name": "Table: Architecture Stratification Results",
779	        "columns": [
780	          "population",
781	          "n_models",
782	          "c_pct",
783	          "rmsea",
784	          "cfi",
785	          "pct_lz_gt2"
786	        ],
787	        "rows": [
788	          [
789	            "full",
790	            5227,
791	            31.3,
792	            0.089,
793	            0.72,
794	            98.0
795	          ],
796	          [
797	            "decoder-only",
798	            5226,
799	            31.3,
800	            0.088,
801	            0.72,
802	            98.0
803	          ],
804	          [
805	            "delta",
806	            "—",
807	            0.0,
808	            0.001,
809	            0.0,
810	            0.0
811	          ]
812	        ]
813	      }
814	    ],
815	    "figures": [],
816	    "analysis": "Median 档下 plan_010 的 value 是 defensive：排除一个 potential confound。 但它也暴露了真正的问题——IRT misfit 来自 multidimensionality， 这正是评审的 attack vector。Plan_005 bifactor pilot 是 partial response， 但 median 档下不够 convincing (CFI=0.81)。 最佳回应策略：承认 misspecification，展示 DIF 发现在 bifactor 校正后 qualitatively 不变 (C% ~28-29% vs 31.3%)，argue \"our findings are conservative estimates\"。\n\n\nMedian 档：plan_010 是 clean knockout result。 1) METABENCH MMLU 是 99.98% decoder-only (5226/5227)——removing 1 non-decoder model changes literally nothing (Jaccard=1.0)。 2) IRT fit 不改善 (RMSEA 0.089→0.088, CFI 0.72→0.72)——因为 misfit 来自 MMLU 的 57-subject multidimensionality，不是 architecture heterogeneity。 3) 98% models 有 |Lz|>2——这反映 1D IRT 对 MMLU 的 fundamental misspecification， 不是 population heterogeneity。 Median 档评审接受这个 null result：architecture 不是问题。但会转向 \"OK so the misfit is from multidimensionality, have you tried multidimensional IRT?\"—— 这是 median 档的核心 concern 之一。 策略：主文用一段报告 99.98% decoder-only + Jaccard=1.0。 IRT fit 数据放 limitations 讨论，作为 multidimensional IRT future work 的动机。\n"
817	  },
818	  {
819	    "name": "semi_synthetic_contamination_validation",
820	    "description": "向真实 METABENCH response matrix 注入已知 contamination，测量 DIF 检测力。\n",
821	    "results": {
822	      "n_clean_items": 500,
823	      "n_injected_items": 200,
824	      "temporal_external_tpr_p0": 0.326,
825	      "temporal_external_tpr_p03": 0.548,
826	      "temporal_external_tpr_p05": 0.834,
827	      "temporal_external_tpr_p07": 0.99,
828	      "temporal_external_tpr_p10": 1.0,
829	      "temporal_external_fpr": 0.314,
830	      "temporal_external_delta_tpr_p05": 0.508,
831	      "temporal_external_delta_tpr_p10": 0.674,
832	      "ability_external_delta_tpr_p10": 0.302,
833	      "cross_subject_delta_fpr": 0.0,
834	      "within_subject_fpr_inflation_p10": 0.186,
835	      "dose_response_monotone": true,
836	      "dose_response_p_values": [
837	        0.3,
838	        0.5,
839	        0.7,
840	        1.0
841	      ]
842	    },
843	    "tables": [
844	      {
845	        "name": "Table: Semi-synthetic Detection Power (Cross-subject Matching)",
846	        "columns": [
847	          "exploitation_rate_p",
848	          "baseline_tpr",
849	          "injected_tpr",
850	          "delta_tpr",
851	          "fpr",
852	          "delta_fpr"
853	        ],
854	        "rows": [
855	          [
856	            "0.0 (no injection)",
857	            0.326,
858	            0.326,
859	            0.0,
860	            0.314,
861	            0.0
862	          ],
863	          [
864	            0.3,
865	            0.326,
866	            0.548,
867	            0.222,
868	            0.314,
869	            0.0
870	          ],
871	          [
872	            0.5,
873	            0.326,
874	            0.834,
875	            0.508,
876	            0.314,
877	            0.0
878	          ],
879	          [
880	            0.7,
881	            0.326,
882	            0.99,
883	            0.664,
884	            0.314,
885	            0.0
886	          ],
887	          [
888	            1.0,
889	            0.326,
890	            1.0,
891	            0.674,
892	            0.314,
893	            0.0
894	          ]
895	        ]
896	      },
897	      {
898	        "name": "Table: Within-subject vs Cross-subject Matching",
899	        "columns": [
900	          "matching",
901	          "delta_tpr_p05",
902	          "delta_fpr_p10",
903	          "fpr_stable"
904	        ],
905	        "rows": [
906	          [
907	            "within-subject",
908	            0.457,
909	            0.186,
910	            false
911	          ],
912	          [
913	            "cross-subject",
914	            0.508,
915	            0.0,
916	            true
917	          ]
918	        ]
919	      }
920	    ],
921	    "figures": [],
922	    "analysis": "Median 档下 plan_011 (+plan_016 cross-subject replication) 是 Claim 3 的 robust foundation。Reviewers 在 median 档给 semi-synthetic framework positive marks (novelty sub-score 2.5 on this specific contribution)。 唯一 downside：injection simplicity。Rebuttal 准备： \"Our injection flips incorrect→correct, which is the minimal model of contamination (memorized answer). More complex patterns (partial memorization, verbatim recall) would produce LARGER DIF effects, not smaller—our power estimates are conservative.\"\n\nMedian 档：plan_011 是 paper 的 strongest evidence 之一。 1) ΔTPR=+0.508 at p=0.5 是 clean, large effect——从 baseline 0.326 升至 0.834， 明确证明 DIF 能 detect injected differential contamination。 2) Dose-response 从 p=0.3 到 p=1.0 monotone——mechanistic validation。 3) Cross-subject matching ΔFPR=0.000 是 key innovation——完全消除 FPR inflation， vs within-subject matching +0.186。这是 Claim 3 的核心证据。 4) Baseline FPR=0.314 (= temporal C%=31.3%)——评审会问 \"is 31% baseline FPR acceptable?\" Answer: this IS the real DIF rate, not false positives. Semi-synthetic 只 adds signal on top of real baseline。 Median 档评审对 plan_011 的质疑集中在： - \"injection mechanism (incorrect→correct) is simplistic—real contamination\n  may produce different patterns (e.g., faster response time, different error types)\"\n- \"you inject into real matrices, but the contamination is still artificial\" 这些是 acknowledged limitations，不是 fatal flaws。 策略：plan_011 在主文 §4 占重要位置。Cross-subject matching 作为 methodological recommendation 明确 highlight。\n"
923	  }
924	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf3ab89e-9622-4c68-9733-631a997fa264",
  "isSidechain": false,
  "promptId": "f9190119-bc3e-4325-b2be-2617c4e8f5d7",
  "type": "user",
  "uuid": "6cd1033b-ae4b-4e8c-8388-031648f3acfb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"real_data_dif_mmlu\",\n    \"description\": \"METABENCH MMLU 全量 DIF 分析。temporal/ability/within-family 三种 cohort 定义， 加 Li et al. proxy validation 和 domain specificity。\\n\",\n    \"results\": {\n      \"temporal_ets_c_pct\": 31.3,\n      \"temporal_n_c_items\": 3918,\n      \"temporal_n_total\": 12508,\n      \"temporal_fpr_on_li_clean\": 0.318,\n      \"temporal_enrichment_ratio\": 0.96,\n      \"ability_ets_c_pct\": 2.9,\n      \"ability_enrichment\": 1.19,\n      \"within_family_llama2v3_c_pct\": 61.3,\n      \"within_family_mistral_mixtral_c_pct\": 38.7,\n      \"domain_spearman_rho\": 0.307,\n      \"domain_spearman_p\": 0.02,\n      \"sanity_random_split_c_pct\": 0.18,\n      \"temporal_ability_jaccard\": 0.014\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Temporal DIF Summary by ETS Classification\",\n        \"columns\": [\n          \"ets_class\",\n          \"n_items\",\n          \"pct\",\n          \"mean_abs_delta_mh\"\n        ],\n        \"rows\": [\n          [\n            \"A (negligible)\",\n            8590,\n            68.7,\n            0.43\n          ],\n          [\n            \"B (moderate)\",\n            2641,\n            21.1,\n            1.24\n          ],\n          [\n            \"C (large)\",\n            1277,\n            10.2,\n            2.31\n          ],\n          [\n            \"B+C (flagged)\",\n            3918,\n            31.3,\n            1.58\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Cohort Definition Sensitivity\",\n        \"columns\": [\n          \"cohort\",\n          \"n_ref\",\n          \"n_foc\",\n          \"c_pct\",\n          \"enrichment\"\n        ],\n        \"rows\": [\n          [\n            \"temporal (2023 vs 2024-H1)\",\n            1253,\n            656,\n            31.3,\n            0.96\n          ],\n          [\n            \"ability (Q1 vs Q5)\",\n            \"~1044\",\n            \"~1044\",\n            2.9,\n            1.19\n          ],\n          [\n            \"within-family (Llama-2 vs 3)\",\n            161,\n            308,\n            61.3,\n            \"—\"\n          ],\n          [\n            \"random split (sanity)\",\n            950,\n            950,\n            0.18,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 plan_001 是 paper 的基石。数据本身不受质疑，但 \\\"so what\\\" 需要后续实验 (plan_019, plan_017, plan_020) 支撑。评审预期反应： R1: \\\"Impressive scale, but what does 31% instability mean for practitioners?\\\" R2: \\\"The enrichment≈1.0 result is interesting but undermines the contamination framing\\\" R3: \\\"Within-family results suggest capability gain, not contamination\\\" 总体：plan_001 在 median 档得 strong accept 作为 empirical contribution， 但单独不够——需要 downstream impact story。\\n\\n\\nmedian 档下这些数值本身站得住——31.3% 是 robust 的经验发现，random-split sanity (0.18%) 排除统计伪影， domain ρ=0.307 是 modest ecological correlation。问题不在数字，在解读： 1) enrichment≈1.0 证明 DIF 和 web-overlap labels 正交，但评审会问 \\\"if DIF doesn't correlate with known contamination, what IS it detecting?\\\"——需要 plan_019 decomposition 才能回答 \\\"item-specific instability, not capability gain\\\"。 2) within-family C%=61.3% (Llama-2 vs 3) 远高于 cross-cohort 31.3%，评审会质疑 \\\"within-family analysis proves capability gain drives DIF, not contamination\\\"。 Median 档下 1 个评审接受 \\\"capability gain ≠ item instability\\\" 论证，1 个不接受。 3) domain ρ=0.307 (p=0.02) 在 median 档被视为 \\\"interesting but not definitive\\\"， 不被攻击也不加分。\\n\"\n  },\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"验证 DIF 在 RL-trained 模型上的鲁棒性。SFT baseline vs alignment-RL (DPO/ORPO) vs reasoning-RL (GRPO/PPO)。关键在于 reasoning-RL 只有 10-15 个模型。\\n\",\n    \"results\": {\n      \"sft_cohort_n\": 312,\n      \"alignment_rl_cohort_n\": 477,\n      \"reasoning_rl_models_collected\": 13,\n      \"sft_vs_alignment_jaccard_dif_flags\": 0.72,\n      \"sft_temporal_c_pct\": 30.8,\n      \"alignment_rl_temporal_c_pct\": 32.1,\n      \"combined_with_reasoning_rl_c_pct\": 31.5,\n      \"jaccard_base_vs_rl_augmented\": 0.91,\n      \"tost_equivalence_p\": 0.14,\n      \"tost_equivalence_bound\": 0.05,\n      \"tost_verdict\": \"inconclusive\",\n      \"mink_auroc_sft\": 0.61,\n      \"mink_auroc_alignment_rl\": 0.58,\n      \"mink_auroc_reasoning_rl\": 0.43,\n      \"constat_auroc_sft\": 0.64,\n      \"constat_auroc_reasoning_rl\": 0.39,\n      \"delong_p_mink_sft_vs_rl\": 0.08,\n      \"delong_p_constat_sft_vs_rl\": 0.03,\n      \"bootstrap_ci_auroc_diff_mink\": [\n        -0.02,\n        0.38\n      ],\n      \"bootstrap_ci_auroc_diff_constat\": [\n        0.04,\n        0.46\n      ],\n      \"power_analysis_delta_boundary\": 1.1,\n      \"power_analysis_tpr_at_boundary\": 0.42\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: DIF Flag Stability Under Cohort Composition Change\",\n        \"columns\": [\n          \"cohort_composition\",\n          \"n_total\",\n          \"c_pct\",\n          \"jaccard_vs_baseline\"\n        ],\n        \"rows\": [\n          [\n            \"SFT only\",\n            312,\n            30.8,\n            \"—\"\n          ],\n          [\n            \"SFT + alignment-RL\",\n            789,\n            32.1,\n            0.72\n          ],\n          [\n            \"SFT + alignment-RL + reasoning-RL\",\n            802,\n            31.5,\n            0.91\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Individual Detector AUROC by Model Type\",\n        \"columns\": [\n          \"detector\",\n          \"sft\",\n          \"alignment_rl\",\n          \"reasoning_rl\",\n          \"delong_p\"\n        ],\n        \"rows\": [\n          [\n            \"Min-K%\",\n            0.61,\n            0.58,\n            0.43,\n            0.08\n          ],\n          [\n            \"ConStat\",\n            0.64,\n            0.6,\n            0.39,\n            0.03\n          ],\n          [\n            \"DIF (group)\",\n            \"—\",\n            \"—\",\n            \"—\",\n            \"N/A\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 plan_002 是最弱的实验。N=13 reasoning-RL 无法支撑任何统计结论。 TOST inconclusive 意味着既不能声称 robust 也不能声称 fragile。 最佳策略：power analysis 图放 appendix，主文用一句话承认 \\\"reasoning-RL validation remains underpowered (N=13); alignment-RL cohort (N=477) shows stable DIF flags (Jaccard=0.72 vs SFT)\\\"。不把 RL robustness 作为 claim。\\n\\n\\nMedian 档核心问题：N=13 reasoning-RL 模型严重不足。 1) Group-level DIF flags 在加入 13 个 RL 模型后变化很小 (Jaccard=0.91)，因为 N=13 在 N≈1900 focal cohort 中占比 <1%，统计上几乎无影响。评审会正确指出 \\\"this doesn't prove RL robustness, it proves RL models are too few to matter\\\"。 2) TOST 等价性检验 p=0.14 不显著——无法证明等价，也无法证明差异。 Median 档评审判断：inconclusive，移至 limitations。 3) 个体模型检测：ConStat 在 reasoning-RL 上 AUROC 降至 0.39 (显著下降)， 但 DIF 是 group-level 无法做个体比较，comparison 不对等。 4) Power analysis 有理论价值：δ<1.1 时 TPR<0.42，清晰刻画了 detection boundary。 但评审会说 \\\"you characterized a limitation, not solved it\\\"。 总体：plan_002 在 median 档被降级为 appendix，N=13 是 fatal underpowering。\\n\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"独立评估 ConStat-style perturbation testing 在 MMLU 上的检测力。 200+ items paraphrased，comparison with DIF flags。\\n\",\n    \"results\": {\n      \"n_items_paraphrased\": 217,\n      \"paraphrase_quality_human_eval\": 0.78,\n      \"constat_detection_rate_fdr005\": 0.23,\n      \"constat_detection_rate_fdr010\": 0.31,\n      \"constat_dif_overlap_jaccard\": 0.08,\n      \"constat_fpr_on_clean_items\": 0.06,\n      \"constat_effect_size_non_rl\": 0.74,\n      \"constat_effect_size_rl\": 0.31,\n      \"paraphrase_difficulty_shift_mean\": 0.12,\n      \"paraphrase_difficulty_shift_std\": 0.34,\n      \"n_models_tested\": 15,\n      \"gpu_hours_used\": 62\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: ConStat Detection Summary\",\n        \"columns\": [\n          \"metric\",\n          \"non_rl_models\",\n          \"rl_models\",\n          \"all\"\n        ],\n        \"rows\": [\n          [\n            \"n_models\",\n            11,\n            4,\n            15\n          ],\n          [\n            \"detection_rate_fdr005\",\n            0.27,\n            0.14,\n            0.23\n          ],\n          [\n            \"mean_effect_size\",\n            0.74,\n            0.31,\n            0.61\n          ],\n          [\n            \"FPR\",\n            0.05,\n            0.08,\n            0.06\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 plan_003a 提供了有价值的 baseline comparison，但不构成独立贡献。 ConStat-DIF orthogonality (Jaccard=0.08) 支持 meta-critique (不同方法 capture 不同 aspects)，但 N=15 模型限制了结论强度。适合 appendix 作为 related work empirical comparison，不适合 main body。\\n\\n\\nMedian 档：ConStat 实验执行了但结果 mixed。 1) Paraphrase 质量 78% human-eval acceptable——约 22% 的 reformulation 引入了 subtle semantic shift，导致 difficulty 变化不纯粹来自 contamination。 评审会质疑 paraphrase 质量是 confound。 2) FDR-controlled detection rate 23% 在 non-RL 模型上——reasonable baseline 但 不 impressive。Jaccard=0.08 与 DIF 几乎无 overlap，说明两者 detect 不同 signal。 3) RL 模型上 effect size 从 0.74 降至 0.31——方向正确但 N=15 模型下 CI 非常宽。 4) 核心问题：ConStat 需要 inference access (running paraphrased items through models)， 而 METABENCH 只有 original responses。所以 ConStat 只在 15 个有 inference access 的模型上跑，vs DIF 用全部 5,227 模型。Scale 不可比。 Median 档评审判断：\\\"useful baseline comparison but limited by small inference sample\\\"。\\n\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"DVD generation variance 在 MMLU 上的独立评估。50 responses/item via temperature sampling。\\n\",\n    \"results\": {\n      \"n_models_tested\": 12,\n      \"n_items_tested\": 500,\n      \"responses_per_item\": 50,\n      \"temperature\": 0.8,\n      \"bimodal_detection_rate\": 0.14,\n      \"bimodal_verbatim_contamination\": 0.31,\n      \"bimodal_variant_contamination\": 0.06,\n      \"dvd_dif_overlap_jaccard\": 0.05,\n      \"dvd_fpr\": 0.09,\n      \"variance_score_reliability\": 0.62,\n      \"gpu_hours_used\": 58\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: DVD Detection by Contamination Type\",\n        \"columns\": [\n          \"contamination_type\",\n          \"n_items_tested\",\n          \"bimodal_rate\",\n          \"fpr\"\n        ],\n        \"rows\": [\n          [\n            \"verbatim\",\n            150,\n            0.31,\n            0.08\n          ],\n          [\n            \"variant\",\n            150,\n            0.06,\n            0.1\n          ],\n          [\n            \"clean\",\n            200,\n            \"—\",\n            0.09\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 plan_003b 是最弱的独立实验。Detection power 低于 ConStat， 且需要 open-weight inference access。主要价值是证明 \\\"generation variance alone is insufficient\\\"——但这不是 surprising finding。Appendix material at best。 在 median 档的策略调整中，plan_003b 应被 deprioritized。\\n\\n\\nMedian 档：DVD 结果较弱。 1) 只有 14% 的 items 显示 bimodal generation variance——远低于 DIF 的 31.3%， 说明 generation variance 作为 contamination signal 灵敏度较低。 2) Verbatim contamination (31% bimodal) vs variant contamination (6% bimodal)： DVD 几乎只能 detect verbatim memorization，对 variant 无力。 3) 与 DIF 的 overlap 近乎为零 (Jaccard=0.05)，再次说明不同方法 capture 不同 signal。 4) Variance score reliability 0.62——moderate at best。50 responses 可能不足以 稳定估计 variance，但 GPU budget 已耗尽。 5) 核心限制：DVD 需要 open-weight + inference，排除 closed-source models。 Median 档评审：\\\"limited detection power, primarily captures verbatim memorization which is already detectable by simpler methods (n-gram matching)\\\"。\\n\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"DIF + ConStat + DVD 三信号 ensemble。依赖 003a 和 003b。\\n\",\n    \"results\": {\n      \"ensemble_auroc_2of3\": 0.58,\n      \"ensemble_auroc_weighted\": 0.62,\n      \"ensemble_fpr_2of3\": 0.11,\n      \"ensemble_fpr_weighted\": 0.09,\n      \"dif_standalone_auroc\": 0.54,\n      \"constat_standalone_auroc\": 0.51,\n      \"dvd_standalone_auroc\": 0.47,\n      \"ensemble_improvement_over_best_single\": 0.08,\n      \"cross_val_weight_stability\": 0.43,\n      \"fpr_below_010_pct_configs\": 0.45\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Ensemble vs Individual Detectors\",\n        \"columns\": [\n          \"method\",\n          \"auroc\",\n          \"fpr\",\n          \"n_models_available\"\n        ],\n        \"rows\": [\n          [\n            \"DIF (MH)\",\n            0.54,\n            0.31,\n            5227\n          ],\n          [\n            \"ConStat\",\n            0.51,\n            0.06,\n            15\n          ],\n          [\n            \"DVD\",\n            0.47,\n            0.09,\n            12\n          ],\n          [\n            \"2-of-3 majority\",\n            0.58,\n            0.11,\n            12\n          ],\n          [\n            \"weighted fusion\",\n            0.62,\n            0.09,\n            12\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 plan_003c 被 drop 是正确决策。Ensemble 面临三重困难： (a) ground truth circularity, (b) small-N signal components, (c) marginal improvement。 Paper framing 已正确将 ensemble 移至 \\\"future work\\\"。 在 rebuttal 中，如果评审问 \\\"why not ensemble?\\\"，回答是 \\\"ensemble requires validated ground truth, which our Claim 2 shows doesn't exist; building the ground truth infrastructure (Claim 3) is prerequisite\\\"。\\n\\n\\nMedian 档：ensemble 无法达到预期目标。 1) FPR<0.10 只在 45% 的配置下成立——不满足 \\\"across all configurations\\\" 的目标。 Weighted fusion FPR=0.09 勉强达标，但 cross-val weight stability=0.43 说明 weights 在 folds 之间不稳定，overfitting risk 高。 2) AUROC 提升 +0.08 over best single signal——marginal，且受限于 ground truth 的质量（Li et al. labels 作为 ground truth 本身是 plan 质疑的对象）。 3) 根本矛盾：paper 的 Claim 2 论证 web-overlap labels 不适合评估 item-level detectors，然后用这些 labels 训练 ensemble weights。评审会指出 circularity。 4) 003a/003b 的小样本 (N=12-15 models) 使得 ensemble 的 training data 极有限。 Median 档评审：\\\"the ensemble adds complexity without resolving the fundamental ground truth problem the paper itself identifies\\\"。\\n\"\n  },\n  {\n    \"name\": \"cross_benchmark_gsm8k\",\n    \"description\": \"GSM8K 上复制 DIF 分析，GSM1K 作为 contamination ground truth。三步： temporal DIF → semi-synthetic → GSM1K correlation。\\n\",\n    \"results\": {\n      \"step1_gsm8k_n_items\": 1319,\n      \"step1_n_ref\": 1017,\n      \"step1_n_foc\": 804,\n      \"step1_standard_c_pct\": 18.9,\n      \"step1_external_c_pct\": 47.4,\n      \"step1_sanity_c_pct\": 0.3,\n      \"step1_standard_external_spearman\": 0.926,\n      \"step2_standard_delta_tpr_p10\": 0.818,\n      \"step2_external_delta_tpr_p10\": 0.517,\n      \"step3_n_models\": 33,\n      \"step3_pearson_r\": -0.478,\n      \"step3_pearson_p\": 0.005,\n      \"step3_spearman_rho\": -0.403,\n      \"step3_spearman_p\": 0.02,\n      \"step3_partial_r\": -0.385,\n      \"step3_partial_p\": 0.027,\n      \"step3_bca_ci_pearson\": [\n        -0.714,\n        -0.155\n      ],\n      \"step3_bca_ci_spearman\": [\n        -0.687,\n        -0.031\n      ],\n      \"step3_permutation_p\": 0.014\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: GSM8K Temporal DIF Summary\",\n        \"columns\": [\n          \"matching\",\n          \"c_pct\",\n          \"sanity_c_pct\",\n          \"delta_tpr_p10\"\n        ],\n        \"rows\": [\n          [\n            \"standard (total score)\",\n            18.9,\n            0.3,\n            0.818\n          ],\n          [\n            \"external (MMLU score)\",\n            47.4,\n            \"—\",\n            0.517\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: GSM1K Correlation (Step 3) — Reviewer Critique Points\",\n        \"columns\": [\n          \"statistic\",\n          \"value\",\n          \"95% CI\",\n          \"reviewer_concern\"\n        ],\n        \"rows\": [\n          [\n            \"Pearson r\",\n            -0.478,\n            \"[-0.714, -0.155]\",\n            \"CI wide\"\n          ],\n          [\n            \"Spearman ρ\",\n            -0.403,\n            \"[-0.687, -0.031]\",\n            \"upper bound near zero\"\n          ],\n          [\n            \"Partial r\",\n            -0.385,\n            \"[-0.640, -0.058]\",\n            \"controlling accuracy helps marginally\"\n          ],\n          [\n            \"N\",\n            33,\n            \"—\",\n            \"underpowered\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 plan_004 是 mixed outcome。Step 1+2 加强 Claim 1+3 的 cross-benchmark generalizability故事，Step 3 是 liability。正确策略是： 主文用 Step 1+2 证明 \\\"DIF and semi-synthetic framework generalize to GSM8K\\\"， Step 3 降级至 appendix with explicit caveat \\\"suggestive evidence requiring replication with larger matched sample (N≥100)\\\"。\\n\\n\\nMedian 档核心动态：Step 1+2 稳固，Step 3 被 dismiss。 1) Step 1: GSM8K C%=18.9% (低于 MMLU 31.3%) 合理——GSM8K 是 math domain， temporal capability gain 更 uniform，所以 differential 更少。评审接受。 2) Step 2: ΔTPR=+0.818 非常强——比 MMLU 的 +0.674 还好，因为 GSM8K 是 single-domain，within-subject/cross-subject 区分不 applicable，matching 更干净。 Semi-synthetic framework portability 得到确认，Claim 3 加分。 3) Step 3: r=-0.478, p=0.005 但 N=33，BCa CI upper bound |r|=0.155。 Median 档下 1-2 个评审直接 dismiss： - \\\"N=33 with Spearman CI touching zero (−0.031) — underpowered\\\" - \\\"BCa CI [−0.714, −0.155] is too wide to be informative\\\" - \\\"contamination gap is itself a noisy proxy\\\" 方向正确 (negative correlation = DIF items resist contamination gains) 但 统计力不足以成为 independent evidence。 4) 策略：median 档下 Step 3 从 Claim 4 子发现降级至 appendix \\\"suggestive evidence\\\"， Claim 4 主要靠 plan_017 z-score + plan_020 circularity ablation。\\n\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"在 MMLU 上拟合 bifactor IRT 模型 (general + 57 subject-specific factors)， 选择 anchor items，执行 fixed-parameter calibration 的 equating pilot。\\n\",\n    \"results\": {\n      \"bifactor_convergence\": true,\n      \"bifactor_iterations\": 2847,\n      \"rmsea\": 0.052,\n      \"cfi\": 0.81,\n      \"tli\": 0.78,\n      \"srmr\": 0.068,\n      \"general_factor_variance_explained\": 0.34,\n      \"subject_factors_variance_explained\": 0.41,\n      \"residual_variance\": 0.25,\n      \"n_anchor_items_selected\": 1200,\n      \"anchor_selection_criterion\": \"no DIF + discrimination > 0.5 + fit residual < 2.0\",\n      \"equated_rho_vs_original\": 0.94,\n      \"equated_rho_target\": 0.95,\n      \"target_met\": false,\n      \"computation_time_hours\": 38,\n      \"memory_peak_gb\": 127\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Bifactor IRT Fit Indices\",\n        \"columns\": [\n          \"index\",\n          \"value\",\n          \"conventional_threshold\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"RMSEA\",\n            0.052,\n            \"<0.06 acceptable\",\n            \"borderline acceptable\"\n          ],\n          [\n            \"CFI\",\n            0.81,\n            \">0.90 good\",\n            \"below threshold\"\n          ],\n          [\n            \"TLI\",\n            0.78,\n            \">0.90 good\",\n            \"below threshold\"\n          ],\n          [\n            \"SRMR\",\n            0.068,\n            \"<0.08 acceptable\",\n            \"acceptable\"\n          ],\n          [\n            \"general factor % variance\",\n            \"34%\",\n            \">50% for unidimensional\",\n            \"confirms multidimensionality\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 plan_005 验证了 IRT misspecification 但未解决它。 34% general factor variance 是回应 \\\"IRT misspecification\\\" concern 的有力数据—— 证明 1D IRT 确实不足，但 DIF finding 的方向和规模不受根本影响 (因为 bifactor 校正后 C% 从 31.3% 只降至 ~28-29%，仍然 substantial)。 关键洞察：评审要求的不是 \\\"fix the misspecification\\\"，而是 \\\"show DIF findings are robust TO the misspecification\\\"。Plan_005 可以回答这个——如果 bifactor 校正后 DIF 发现 qualitatively 不变，那就是 robustness evidence。 策略：不把 equating 当 claim，而是作为 IRT sensitivity analysis 放 appendix。\\n\\n\\nMedian 档：bifactor 收敛但 fit 指标 mediocre。 1) RMSEA=0.052 在 acceptable range (< 0.06) 但不 good (< 0.05)。 CFI=0.81 和 TLI=0.78 低于常规 threshold (0.90)——这是 12,508 items × 5,227 models 的规模效应，absolute fit indices 在超大规模下系统偏低。 评审如果懂 psychometrics 会接受，不懂会直接攻击 \\\"poor model fit\\\"。 2) General factor 只解释 34% variance——MMLU 的 57 subject 确实 highly multidimensional，这 validates \\\"1D IRT is misspecified\\\" 的论点。 3) Equating ρ=0.94 未达 0.95 target——marginal miss。Plan_014 within-subject pre-check (38.1% C%) 已经预示 DIF 在 bifactor 校正后不会大幅下降。 4) 计算成本高 (38 hours, 127GB RAM)——scalability concern。 Median 档评审反应： - 支持者：\\\"bifactor results validate the multidimensionality concern and motivate\\n  future work on MIRT-based DIF\\\"\\n- 反对者：\\\"CFI=0.81 means the model doesn't fit, equating results are unreliable\\\" 总体：pilot 结果 suggestive 但不 conclusive，适合 limitations/future work。\\n\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"为 DIF-flagged items 生成替代题目，用 student simulation 校准难度。\\n\",\n    \"results\": {\n      \"n_items_generated\": 150,\n      \"difficulty_correlation_prompt_based\": 0.32,\n      \"difficulty_correlation_student_sim\": 0.58,\n      \"difficulty_correlation_target\": 0.75,\n      \"target_met\": false,\n      \"cognitive_level_match_rate\": 0.71,\n      \"subject_match_rate\": 0.95,\n      \"human_quality_rating\": 3.2,\n      \"human_quality_scale\": \"1-5\",\n      \"holdout_panel_rho\": 0.52,\n      \"gpu_hours_used\": 145\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Item Generation Difficulty Calibration\",\n        \"columns\": [\n          \"method\",\n          \"difficulty_ρ\",\n          \"n_items\",\n          \"notes\"\n        ],\n        \"rows\": [\n          [\n            \"prompt-based targeting\",\n            0.32,\n            150,\n            \"below literature 0.10-0.45\"\n          ],\n          [\n            \"student simulation\",\n            0.58,\n            150,\n            \"below target 0.75\"\n          ],\n          [\n            \"combined (iterative)\",\n            0.61,\n            80,\n            \"2-round refinement\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 plan_006 是 expected negative。Item generation 是 hard open problem， failure 不损害核心 paper 因为 regeneration 已从 claims 中 drop。 唯一价值：作为 future work 动机——\\\"automated benchmark maintenance requires better item generation, which remains an open problem\\\"。\\n\\n\\nMedian 档：item generation 是 paper 最弱的环节之一。 1) Prompt-based difficulty targeting ρ=0.32 远低于文献报告的 0.45 upper bound—— MMLU 的 multiple-choice 格式和 domain diversity 使 prompt 控制困难。 2) Student simulation 提升到 ρ=0.58 (vs 文献 0.75-0.82 on simpler benchmarks)—— MMLU 的 57 domains 使 simulation calibration 更难泛化。 3) Cognitive level match rate 71%——约 29% 的 generated items 测量不同的 cognitive level，这是 construct validity threat。 4) Holdout panel ρ=0.52——远低于 equating 需要的精度。 Median 档评审会直接判定 item generation 不成熟：\\\"generated items don't match target difficulty well enough for equating; this is a negative result\\\"。 策略：plan_006 在 median 档是 negative result，移至 appendix 作为 \\\"current limitations of LLM-based item generation for benchmark maintenance\\\"。 不影响核心 claims。\\n\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"实现 Sinharay et al. (2006) 的 cumulative Bayesian DIF prior。 模拟 4 次 successive benchmark administration，展示 evidence 累积带来的 power 提升。\\n\",\n    \"results\": {\n      \"simulation_n_administrations\": 4,\n      \"admin_1_power_delta10\": 0.41,\n      \"admin_2_power_delta10\": 0.56,\n      \"admin_3_power_delta10\": 0.68,\n      \"admin_4_power_delta10\": 0.74,\n      \"target_admin3_power\": 0.7,\n      \"target_met\": false,\n      \"admin_3_power_delta14\": 0.82,\n      \"fpr_cumulative\": 0.048,\n      \"fpr_stable_across_admins\": true,\n      \"bayes_factor_median_admin3\": 4.2,\n      \"simulation_n_items\": 500,\n      \"simulation_n_models_per_admin\": 200,\n      \"computation_time_hours\": 6\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cumulative Power by Administration\",\n        \"columns\": [\n          \"n_admins\",\n          \"power_delta_10\",\n          \"power_delta_14\",\n          \"power_delta_16\",\n          \"fpr\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.41,\n            0.68,\n            0.72,\n            0.042\n          ],\n          [\n            2,\n            0.56,\n            0.77,\n            0.83,\n            0.045\n          ],\n          [\n            3,\n            0.68,\n            0.82,\n            0.89,\n            0.048\n          ],\n          [\n            4,\n            0.74,\n            0.86,\n            0.92,\n            0.047\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 plan_007 有 modest value 作为 forward-looking contribution。 核心问题：ML 评审对 \\\"future benchmark administrations\\\" 的 temporal framing 不熟悉——psychometrics 中 repeated test administration 是常态， 但 LLM benchmarks 通常是 one-shot。需要明确解释 \\\"as new model generations emerge, the same benchmark is effectively re-administered\\\"。 Appendix 放置，主文 limitations 中一句话提及 cumulative power improvement 可能性。\\n\\n\\nMedian 档：simulation 结果方向正确但 target 未达。 1) 3 次 administration 后 δ=1.0 的 power 从 0.41 升至 0.68——接近但未达 0.70 target。 δ=1.4 时 0.82 是可用的，说明 cumulative approach 有价值但主要对 medium effects。 2) FPR 控制良好 (0.048)，Bayesian prior 没有引入 FPR inflation。 3) 核心限制：这是 pure simulation，没有 real data validation。 METABENCH 只有一个 \\\"administration\\\"（没有 temporal sub-cohorts fine enough for 4 successive periods）。 4) Median 档评审：\\\"simulation-only result without empirical validation; interesting but speculative\\\"。 策略：appendix material。展示 concept 可行性但承认需要真实数据验证。 如果 ICLR 评审不熟悉 Bayesian DIF，这部分可能被完全忽略。\\n\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"分析 benchmark validity 在 progressive item replacement 下的退化模式。\\n\",\n    \"results\": {\n      \"replacement_5pct_rho\": 0.998,\n      \"replacement_10pct_rho\": 0.995,\n      \"replacement_20pct_rho\": 0.987,\n      \"replacement_50pct_rho\": 0.961,\n      \"reliability_5pct_alpha\": 0.943,\n      \"reliability_10pct_alpha\": 0.938,\n      \"reliability_20pct_alpha\": 0.924,\n      \"reliability_50pct_alpha\": 0.891,\n      \"original_alpha\": 0.946,\n      \"construct_coverage_20pct_subjects_lost\": 0,\n      \"construct_coverage_50pct_subjects_lost\": 3,\n      \"validity_floor_replacement_pct\": 0.35,\n      \"validity_floor_criterion\": \"ρ > 0.98 AND α > 0.92\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Validity Metrics Under Progressive Replacement\",\n        \"columns\": [\n          \"replacement_pct\",\n          \"rank_ρ\",\n          \"cronbach_α\",\n          \"subjects_under_represented\"\n        ],\n        \"rows\": [\n          [\n            0,\n            1.0,\n            0.946,\n            0\n          ],\n          [\n            5,\n            0.998,\n            0.943,\n            0\n          ],\n          [\n            10,\n            0.995,\n            0.938,\n            0\n          ],\n          [\n            20,\n            0.987,\n            0.924,\n            0\n          ],\n          [\n            35,\n            0.974,\n            0.908,\n            1\n          ],\n          [\n            50,\n            0.961,\n            0.891,\n            3\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 plan_008 的主要贡献是量化 \\\"how much replacement is safe\\\"—— 35% validity floor 直接对应 \\\"31% DIF items can be safely replaced without validity loss\\\"。这 strengthens the \\\"instability ≠ invalidity\\\" narrative。 但 plan_006 的 negative result 使得 \\\"replacement\\\" 变成 theoretical exercise。\\n\\n\\nMedian 档：graceful degradation 结果 clean 且 informative。 1) ρ 从 0.998 (5%) 到 0.961 (50%) 的退化曲线非常 smooth——MMLU 的 12,508 items 有 massive redundancy，即使替换 50% items 排名仍 strongly correlated。 这 complements plan_017 (ρ=0.997 after removing 31% DIF items)。 2) Reliability (Cronbach's α) 从 0.946 到 0.891——20% 是 practical threshold， 之后 reliability 下降加速。 3) Construct coverage：50% replacement 时 3 个 subjects 可能 under-represented (small subjects with few items)。 4) 核心问题：replacement 假设 generated items 质量 OK——但 plan_006 显示 generation 质量不足。所以 \\\"graceful degradation\\\" 只在理论层面成立。 Median 档评审：\\\"nice analysis but moot without better item generation (plan_006 failed)\\\"。 策略：clean supplementary result，放 appendix。主文用 \\\"validity floor at ~35% replacement\\\" 作为 practical recommendation。\\n\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"Tutz & Berger (2016) Item-Focused Trees 作为 categorical DIF 的替代方案。 Treat model release date as continuous covariate。\\n\",\n    \"results\": {\n      \"n_items_analyzed\": 12508,\n      \"n_items_with_significant_split\": 4127,\n      \"pct_items_with_split\": 33.0,\n      \"primary_split_date\": \"2023-11-15\",\n      \"concordance_with_mh_ets_c\": 0.78,\n      \"additional_items_detected\": 209,\n      \"items_missed_by_ift\": 612,\n      \"jaccard_mh_vs_ift\": 0.68,\n      \"computational_time_hours\": 12,\n      \"n_items_nonlinear_trend\": 1834,\n      \"pct_nonlinear\": 14.7\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: MH vs IFT Concordance\",\n        \"columns\": [\n          \"metric\",\n          \"mh_ets_c\",\n          \"ift_significant\",\n          \"overlap\",\n          \"jaccard\"\n        ],\n        \"rows\": [\n          [\n            \"n_flagged\",\n            3918,\n            4127,\n            3306,\n            0.68\n          ],\n          [\n            \"pct_flagged\",\n            31.3,\n            33.0,\n            26.4,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 plan_009 的 concordance=0.78 有两面性： - 支持：MH 的 categorical split 不是 artifact，IFT confirms temporal instability - 质疑：22% discordance 说明 method choice matters，results are partially method-dependent 评审在 median 档接受 IFT 作为 robustness check，不会深入追究 discordance。\\n\\n\\nMedian 档：IFT 是有价值的 robustness check 但不改变 narrative。 1) 33% items with significant split vs MH 31.3%——high concordance (0.78)， 说明 categorical temporal split 不是 arbitrary 的。 2) Primary split date 2023-11-15——接近 GPT-4/Llama-2 到 Llama-3/Mixtral 的代际转换点，有 face validity。 3) IFT detects 209 additional items that MH misses (mostly items with gradual drift rather than sharp shift)，同时 misses 612 items MH catches (mostly items where DIF is large but not monotone in date)。 4) 14.7% nonlinear trends——说明 some items 的 DIF 不是 monotone temporal， 暗示 \\\"contamination + capability gain + item drift\\\" 的 multi-factor story。 Median 档评审：\\\"useful supplementary analysis, confirms MH results are not artifacts of the cohort split\\\"。不改变 claims 但提供 methodological robustness。 策略：appendix 的 robustness check。主文一句话：\\\"IFT with continuous release date yields 78% concordance with MH categorical DIF (Appendix X)\\\"。\\n\"\n  },\n  {\n    \"name\": \"architecture_stratified_dif\",\n    \"description\": \"在 decoder-only 子群内重跑 DIF，检验 architecture heterogeneity 是否影响 IRT fit。\\n\",\n    \"results\": {\n      \"n_decoder_only\": 5226,\n      \"n_non_decoder\": 1,\n      \"pct_decoder_only\": 99.98,\n      \"decoder_only_c_pct\": 31.3,\n      \"full_population_c_pct\": 31.3,\n      \"jaccard_decoder_vs_full\": 1.0,\n      \"irt_rmsea_full\": 0.089,\n      \"irt_rmsea_decoder_only\": 0.088,\n      \"irt_cfi_full\": 0.72,\n      \"irt_cfi_decoder_only\": 0.72,\n      \"irt_fit_improvement\": \"negligible\",\n      \"pct_models_lz_gt2\": 98.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Architecture Stratification Results\",\n        \"columns\": [\n          \"population\",\n          \"n_models\",\n          \"c_pct\",\n          \"rmsea\",\n          \"cfi\",\n          \"pct_lz_gt2\"\n        ],\n        \"rows\": [\n          [\n            \"full\",\n            5227,\n            31.3,\n            0.089,\n            0.72,\n            98.0\n          ],\n          [\n            \"decoder-only\",\n            5226,\n            31.3,\n            0.088,\n            0.72,\n            98.0\n          ],\n          [\n            \"delta\",\n            \"—\",\n            0.0,\n            0.001,\n            0.0,\n            0.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 plan_010 的 value 是 defensive：排除一个 potential confound。 但它也暴露了真正的问题——IRT misfit 来自 multidimensionality， 这正是评审的 attack vector。Plan_005 bifactor pilot 是 partial response， 但 median 档下不够 convincing (CFI=0.81)。 最佳回应策略：承认 misspecification，展示 DIF 发现在 bifactor 校正后 qualitatively 不变 (C% ~28-29% vs 31.3%)，argue \\\"our findings are conservative estimates\\\"。\\n\\n\\nMedian 档：plan_010 是 clean knockout result。 1) METABENCH MMLU 是 99.98% decoder-only (5226/5227)——removing 1 non-decoder model changes literally nothing (Jaccard=1.0)。 2) IRT fit 不改善 (RMSEA 0.089→0.088, CFI 0.72→0.72)——因为 misfit 来自 MMLU 的 57-subject multidimensionality，不是 architecture heterogeneity。 3) 98% models 有 |Lz|>2——这反映 1D IRT 对 MMLU 的 fundamental misspecification， 不是 population heterogeneity。 Median 档评审接受这个 null result：architecture 不是问题。但会转向 \\\"OK so the misfit is from multidimensionality, have you tried multidimensional IRT?\\\"—— 这是 median 档的核心 concern 之一。 策略：主文用一段报告 99.98% decoder-only + Jaccard=1.0。 IRT fit 数据放 limitations 讨论，作为 multidimensional IRT future work 的动机。\\n\"\n  },\n  {\n    \"name\": \"semi_synthetic_contamination_validation\",\n    \"description\": \"向真实 METABENCH response matrix 注入已知 contamination，测量 DIF 检测力。\\n\",\n    \"results\": {\n      \"n_clean_items\": 500,\n      \"n_injected_items\": 200,\n      \"temporal_external_tpr_p0\": 0.326,\n      \"temporal_external_tpr_p03\": 0.548,\n      \"temporal_external_tpr_p05\": 0.834,\n      \"temporal_external_tpr_p07\": 0.99,\n      \"temporal_external_tpr_p10\": 1.0,\n      \"temporal_external_fpr\": 0.314,\n      \"temporal_external_delta_tpr_p05\": 0.508,\n      \"temporal_external_delta_tpr_p10\": 0.674,\n      \"ability_external_delta_tpr_p10\": 0.302,\n      \"cross_subject_delta_fpr\": 0.0,\n      \"within_subject_fpr_inflation_p10\": 0.186,\n      \"dose_response_monotone\": true,\n      \"dose_response_p_values\": [\n        0.3,\n        0.5,\n        0.7,\n        1.0\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Semi-synthetic Detection Power (Cross-subject Matching)\",\n        \"columns\": [\n          \"exploitation_rate_p\",\n          \"baseline_tpr\",\n          \"injected_tpr\",\n          \"delta_tpr\",\n          \"fpr\",\n          \"delta_fpr\"\n        ],\n        \"rows\": [\n          [\n            \"0.0 (no injection)\",\n            0.326,\n            0.326,\n            0.0,\n            0.314,\n            0.0\n          ],\n          [\n            0.3,\n            0.326,\n            0.548,\n            0.222,\n            0.314,\n            0.0\n          ],\n          [\n            0.5,\n            0.326,\n            0.834,\n            0.508,\n            0.314,\n            0.0\n          ],\n          [\n            0.7,\n            0.326,\n            0.99,\n            0.664,\n            0.314,\n            0.0\n          ],\n          [\n            1.0,\n            0.326,\n            1.0,\n            0.674,\n            0.314,\n            0.0\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Within-subject vs Cross-subject Matching\",\n        \"columns\": [\n          \"matching\",\n          \"delta_tpr_p05\",\n          \"delta_fpr_p10\",\n          \"fpr_stable\"\n        ],\n        \"rows\": [\n          [\n            \"within-subject\",\n            0.457,\n            0.186,\n            false\n          ],\n          [\n            \"cross-subject\",\n            0.508,\n            0.0,\n            true\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 plan_011 (+plan_016 cross-subject replication) 是 Claim 3 的 robust foundation。Reviewers 在 median 档给 semi-synthetic framework positive marks (novelty sub-score 2.5 on this specific contribution)。 唯一 downside：injection simplicity。Rebuttal 准备： \\\"Our injection flips incorrect→correct, which is the minimal model of contamination (memorized answer). More complex patterns (partial memorization, verbatim recall) would produce LARGER DIF effects, not smaller—our power estimates are conservative.\\\"\\n\\nMedian 档：plan_011 是 paper 的 strongest evidence 之一。 1) ΔTPR=+0.508 at p=0.5 是 clean, large effect——从 baseline 0.326 升至 0.834， 明确证明 DIF 能 detect injected differential contamination。 2) Dose-response 从 p=0.3 到 p=1.0 monotone——mechanistic validation。 3) Cross-subject matching ΔFPR=0.000 是 key innovation——完全消除 FPR inflation， vs within-subject matching +0.186。这是 Claim 3 的核心证据。 4) Baseline FPR=0.314 (= temporal C%=31.3%)——评审会问 \\\"is 31% baseline FPR acceptable?\\\" Answer: this IS the real DIF rate, not false positives. Semi-synthetic 只 adds signal on top of real baseline。 Median 档评审对 plan_011 的质疑集中在： - \\\"injection mechanism (incorrect→correct) is simplistic—real contamination\\n  may produce different patterns (e.g., faster response time, different error types)\\\"\\n- \\\"you inject into real matrices, but the contamination is still artificial\\\" 这些是 acknowledged limitations，不是 fatal flaws。 策略：plan_011 在主文 §4 占重要位置。Cross-subject matching 作为 methodological recommendation 明确 highlight。\\n\"\n  }\n]",
      "numLines": 924,
      "startLine": 1,
      "totalLines": 924
    }
  },
  "sourceToolAssistantUUID": "cf3ab89e-9622-4c68-9733-631a997fa264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "6cd1033b-ae4b-4e8c-8388-031648f3acfb",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with IRT analysis",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e"
}
```

---

### Assistant

_source line 16 · 2026-05-21T06:44:47.585Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me also check the paper-writing-norms skill and the existing paper for LaTeX style reference.

Let me now write the full paper. I need to cover:

1. Abstract
2. Introduction
3. Related Work (brief)
4. Method (MH-DIF, semi-synthetic framework, cross-subject matching)
5. Experiments (covering all experiments from experiment_data.json)
6. Discussion + Limitations
7. Conclusion

The experiments from experiment_data.json are:
1. real_data_dif_mmlu - Main DIF analysis (Table 1, Table 2)


2. rl_robustness_validation - RL robustness (appendix)
3. constat_perturbation_eval - ConStat comparison (appendix)
4. dvd_generation_variance_eval - DVD comparison (appendix)
5. ensemble_fusion - Ensemble (appendix)
6. cross_benchmark_gsm8k - GSM8K cross-benchmark (main + appendix)
7. bifactor_irt_equating_pilot - Bifactor IRT (appendix)
8. item_generation_calibration - Item generation (appendix)
9. cumulative_bayesian_dif - Bayesian DIF (appendix)
10. graceful_degradation_analysis - Degradation (appendix)
11. item_focused_trees - IFT robustness (appendix)
12. architecture_stratified_dif - Architecture check (main, brief)
13. semi_synthetic_contamination_validation - Semi-synthetic (main)

I need to ensure each experiment gets its own section or table entry. The main paper will focus on Claims 1-4 with the primary experiments, while the appendix handles all the supporting analyses. Now I'm ready to start writing the full LaTeX document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cd1033b-ae4b-4e8c-8388-031648f3acfb",
  "isSidechain": false,
  "requestId": "req_011CbFG9SM1M1sZv8dEoibJF",
  "type": "assistant",
  "uuid": "fe2a3df1-1f54-43da-9fe9-763a811720d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THhuWDt9U4PUCdwZw3nf3u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5947,
      "cache_creation_input_tokens": 15864,
      "cache_read_input_tokens": 23745,
      "output_tokens": 568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5947,
          "output_tokens": 568,
          "cache_read_input_tokens": 23745,
          "cache_creation_input_tokens": 15864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15864
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

_source line 17 · 2026-05-21T06:44:47.586Z_

Now I have both files. Let me check the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe2a3df1-1f54-43da-9fe9-763a811720d6",
  "isSidechain": false,
  "requestId": "req_011CbFG9SM1M1sZv8dEoibJF",
  "type": "assistant",
  "uuid": "ab759af4-6a0b-47c5-916f-5a3f2b683e70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THhuWDt9U4PUCdwZw3nf3u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5947,
      "cache_creation_input_tokens": 15864,
      "cache_read_input_tokens": 23745,
      "output_tokens": 568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5947,
          "output_tokens": 568,
          "cache_read_input_tokens": 23745,
          "cache_creation_input_tokens": 15864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15864
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

_source line 18 · 2026-05-21T06:44:49.294Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DKsv6WX5Ms4h7ckBTDKuP9`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab759af4-6a0b-47c5-916f-5a3f2b683e70",
  "isSidechain": false,
  "requestId": "req_011CbFG9SM1M1sZv8dEoibJF",
  "type": "assistant",
  "uuid": "ceca9298-99ad-4bd9-be38-b2cbaaa499e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THhuWDt9U4PUCdwZw3nf3u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5947,
      "cache_creation_input_tokens": 15864,
      "cache_read_input_tokens": 23745,
      "output_tokens": 568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5947,
          "output_tokens": 568,
          "cache_read_input_tokens": 23745,
          "cache_creation_input_tokens": 15864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15864
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

_source line 19 · 2026-05-21T06:44:49.447Z_

<details><summary>↩ Tool result · `toolu_01DKsv6WX5Ms4h7ckBTDKuP9`</summary>

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
  "parentUuid": "ceca9298-99ad-4bd9-be38-b2cbaaa499e5",
  "isSidechain": false,
  "promptId": "f9190119-bc3e-4325-b2be-2617c4e8f5d7",
  "type": "user",
  "uuid": "a8370e6b-7e93-4349-8466-6fc849f52865",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ceca9298-99ad-4bd9-be38-b2cbaaa499e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T06:48:33.234Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Ete1WTGf8MeFXsbEHXmQH1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/paper.tex",
  "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\n\\title{Psychometric Characterization of Temporal Item Instability\\\\in LLM Benchmarks: A Large-Scale DIF Analysis of MMLU}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nLLM benchmarks implicitly assume temporal score comparability---that scores from different model generations reflect the same underlying construct. We test this assumption by applying Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis to the METABENCH response matrix (5{,}227 models $\\times$ 12{,}508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\nWe report four findings.\n(1)~31.3\\% of MMLU items exhibit large temporal DIF (ETS C class, $|\\Delta_\\text{MH}|\\geq1.5$) between 2023 and 2024-H1 model cohorts; item-level decomposition shows domain accuracy improvement explains at most 2.4 percentage points (7.6\\%) of this instability.\n(2)~Web-overlap contamination labels, routinely used as ground truth for item-level detectors, measure global exposure rather than differential contamination; DIF enrichment $\\approx$1.0 against such labels is expected, not failure.\n(3)~We introduce a semi-synthetic validation framework ($\\Delta$TPR methodology) with cross-subject matching that eliminates false-positive inflation ($\\Delta$FPR\\,=\\,0.000) and generalizes across benchmarks (GSM8K $\\Delta$TPR\\,=\\,+0.818).\n(4)~DIF items carry genuine cross-cohort signal ($z=-8$ to $-49\\sigma$ vs.\\ random removal) yet are the \\emph{least} disruptive non-random removal strategy ($z=-9.5$ vs.\\ accuracy-gap $z=-157$), serving as a diagnostic lens rather than a quality filter.\nOverall rankings remain highly stable after removing all flagged items ($\\rho\\approx0.997$), confirming that instability does not threaten validity but reveals which capability dimensions shift across model generations.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\\label{sec:intro}\n%==============================================================================\n\nWhen we report that ``Model B outperforms Model A on MMLU,'' we presume both scores reflect the same latent construct measured under equivalent conditions. Psychometrics calls this assumption \\emph{measurement invariance}: an item that is easy for Group~A examinees of a given ability level should be equally easy for Group~B examinees at the same ability level. When this fails---when an item's difficulty shifts after controlling for overall ability---the item exhibits \\emph{Differential Item Functioning} (DIF).\n\nDIF analysis is a mature tool in educational and psychological testing, with over six decades of methodological development since Mantel and Haenszel's original proposal~\\citep{mantel1959statistical,holland1988differential}. It has been applied to ensure fairness across demographic groups, flag compromised items in high-stakes exams, and validate the temporal stability of test scores. Yet it has seen virtually no application to LLM evaluation, despite the field's growing concern about benchmark contamination and score inflation.\n\nWe apply MH-DIF to the METABENCH response matrix---5{,}227 models $\\times$ 12{,}508 MMLU items---using models released before and after a temporal cutoff as reference and focal groups. This constitutes the largest-scale DIF analysis ever conducted on an LLM benchmark. Our key finding is that \\textbf{31.3\\% of MMLU items are functionally unstable across model generations} (ETS C classification, $|\\Delta_\\text{MH}|\\geq1.5$), but this instability does not threaten ranking validity ($\\rho\\approx0.997$ between full and stable-only rankings).\n\n\\paragraph{Instability $\\neq$ Invalidity.} This framing is central: DIF flags items whose measurement properties changed across model generations. This is a \\emph{diagnostic signal}, not a quality verdict. The massive ranking stability ($\\rho\\approx0.997$) under 31\\% item removal reveals enormous measurement redundancy in MMLU. The value of DIF analysis lies not in filtering ``bad'' items but in understanding \\emph{what changed} across generations---which capability dimensions are shifting and how.\n\nWe make four contributions:\n\\begin{enumerate}\n    \\item An empirical characterization of temporal item instability at unprecedented scale, showing that 31.3\\% of MMLU items exhibit large DIF that is predominantly item-specific (domain accuracy improvement explains $\\leq$7.6\\%).\n    \\item A ground truth meta-critique: web-overlap contamination labels cannot validate item-level differential detectors, affecting the validity claims of existing methods.\n    \\item A reusable semi-synthetic validation framework with cross-subject matching that eliminates FPR inflation and generalizes across benchmarks.\n    \\item A demonstration that DIF serves as a diagnostic lens for understanding cross-generational capability shifts, not merely a quality filter.\n\\end{enumerate}\n\n%==============================================================================\n\\section{Related Work}\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Benchmark Contamination Detection.}\nSeveral methods detect training-set contamination in LLMs. Min-K\\%~\\citep{shi2024detecting} uses token-level perplexity; ConStat~\\citep{dekoninck2024constat} compares performance on original vs.\\ paraphrased items; n-gram overlap methods check for verbatim memorization. These methods typically validate against web-overlap labels (e.g., Li et al.'s MMLU contamination annotations), which measure whether an item is publicly accessible rather than whether it functions differently across model groups.\n\n\\paragraph{Differential Item Functioning.}\nDIF analysis originated with \\citet{mantel1959statistical} and was formalized for testing contexts by \\citet{holland1988differential}. The ETS classification system~\\citep{zieky1993practical} categorizes DIF magnitude into negligible (A: $|\\Delta_\\text{MH}|<1.0$), moderate (B: $1.0\\leq|\\Delta_\\text{MH}|<1.5$), and large (C: $|\\Delta_\\text{MH}|\\geq1.5$). Item-Focused Trees~\\citep{tutz2016item} extend DIF to continuous covariates. We apply these standard methods without modification; our contribution is empirical, not algorithmic.\n\n\\paragraph{LLM Benchmark Methodology.}\nGrowing Pains~\\citep{polo2024tinybenchmarks} uses anchor items for efficient evaluation. METABENCH~\\citep{becker2024metabench} aggregates 5{,}227 models' responses on MMLU, providing the response matrix we analyze. Our DIF analysis complements these efforts by identifying which anchor items are degrading across model generations.\n\n%==============================================================================\n\\section{Method}\\label{sec:method}\n%==============================================================================\n\n\\subsection{Mantel-Haenszel DIF Analysis}\\label{sec:mh}\n\nFor each item $j$, the MH procedure tests whether the odds of a correct response differ between reference (R) and focal (F) groups after stratifying by total score. The MH odds ratio $\\alpha_\\text{MH}$ is:\n\\begin{equation}\n    \\alpha_\\text{MH} = \\frac{\\sum_k A_k D_k / T_k}{\\sum_k B_k C_k / T_k},\n\\end{equation}\nwhere $A_k, B_k, C_k, D_k$ are the entries of the $2\\times2$ contingency table at score stratum $k$ and $T_k$ is the stratum total. The log-odds ratio is converted to the $\\Delta_\\text{MH}$ scale:\n\\begin{equation}\n    \\Delta_\\text{MH} = -2.35 \\ln(\\alpha_\\text{MH}).\n\\end{equation}\n\nWe use the ETS classification: items with $|\\Delta_\\text{MH}|\\geq1.5$ and a statistically significant MH $\\chi^2$ test ($p<0.05$) are classified as ETS C (large DIF). The dual requirement of both effect size and statistical significance provides implicit protection against multiple testing~\\citep{zieky1993practical}.\n\n\\paragraph{Cohort Definitions.}\nWe define temporal cohorts by model release date: reference (2023) and focal (2024-H1). We also examine ability-based cohorts (Q1 vs.\\ Q5 of total score) and within-family cohorts (e.g., Llama-2 vs.\\ Llama-3) as sensitivity analyses.\n\n\\subsection{Semi-Synthetic Validation Framework}\\label{sec:semisyn}\n\nTo validate DIF detection power, we inject known differential contamination into real METABENCH response matrices. For a set of ``contaminated'' items and a target exploitation rate $p$, we flip $p$-fraction of incorrect focal-group responses to correct, simulating the effect of contamination that differentially benefits newer models.\n\n\\paragraph{$\\Delta$TPR Methodology.}\nDetection power is measured as:\n\\begin{equation}\n    \\Delta\\text{TPR}(p) = \\text{TPR}_\\text{injected}(p) - \\text{TPR}_\\text{baseline}(0),\n\\end{equation}\nisolating the detection power increase attributable to injected contamination.\n\n\\paragraph{Cross-Subject Matching.}\nStandard MH uses total score on the same subject as the matching variable. When contamination affects items within that subject, the matching variable is itself contaminated, inflating FPR. We propose \\emph{cross-subject matching}: using total score on \\emph{other} MMLU subjects as the matching variable. This eliminates FPR inflation ($\\Delta$FPR\\,=\\,0.000) while preserving detection power.\n\n%==============================================================================\n\\section{Experiments}\\label{sec:experiments}\n%==============================================================================\n\n\\subsection{Claim 1: Temporal Item Instability}\\label{sec:claim1}\n\n\\subsubsection{Main DIF Analysis (MMLU)}\n\nWe apply MH-DIF to the full METABENCH MMLU matrix (5{,}227 models $\\times$ 12{,}508 items) with temporal cohorts (2023 vs.\\ 2024-H1; $n_\\text{ref}=1{,}253$, $n_\\text{foc}=656$).\n\n\\begin{table}[htb]\n\\centering\n\\caption{Temporal DIF summary by ETS classification on MMLU.}\n\\label{tab:temporal_dif}\n\\begin{tabular}{lrrr}\n\\toprule\nETS Class & $n$ items & \\% & Mean $|\\Delta_\\text{MH}|$ \\\\\n\\midrule\nA (negligible) & 8{,}590 & 68.7 & 0.43 \\\\\nB (moderate) & 2{,}641 & 21.1 & 1.24 \\\\\nC (large) & 1{,}277 & 10.2 & 2.31 \\\\\nB+C (flagged) & 3{,}918 & 31.3 & 1.58 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:temporal_dif} shows that 31.3\\% of items (3{,}918 / 12{,}508) are flagged as exhibiting moderate or large DIF. A random-split sanity check produces only 0.18\\% flagged items, confirming that the temporal signal is not a statistical artifact.\n\n\\subsubsection{Cohort Sensitivity}\n\n\\begin{table}[htb]\n\\centering\n\\caption{DIF results under different cohort definitions.}\n\\label{tab:cohort}\n\\begin{tabular}{lrrrr}\n\\toprule\nCohort & $n_\\text{ref}$ & $n_\\text{foc}$ & C\\% & Enrichment \\\\\n\\midrule\nTemporal (2023 vs 2024-H1) & 1{,}253 & 656 & 31.3 & 0.96 \\\\\nAbility (Q1 vs Q5) & $\\sim$1{,}044 & $\\sim$1{,}044 & 2.9 & 1.19 \\\\\nWithin-family (Llama-2 vs 3) & 161 & 308 & 61.3 & --- \\\\\nRandom split (sanity) & 950 & 950 & 0.18 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cohort} reveals three patterns: (1)~temporal cohorts produce substantial DIF (31.3\\%); (2)~ability-based cohorts produce minimal DIF (2.9\\%), indicating that the temporal signal is not an artifact of ability differences; (3)~within-family comparison (Llama-2 vs.\\ 3) produces the highest DIF (61.3\\%), consistent with rapid capability gains within an architecture family. The near-zero enrichment against Li et al.\\ contamination labels ($0.96\\approx1.0$) motivates the ground truth meta-critique in \\S\\ref{sec:claim2}. Domain-specific DIF correlates modestly with accuracy improvement ($\\rho=0.307$, $p=0.02$), but item-level decomposition shows domain improvement explains at most 2.4 percentage points of 31.3\\% C\\% (7.6\\%).\n\n\\subsubsection{Architecture Stratification}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Architecture stratification: DIF and IRT fit.}\n\\label{tab:arch}\n\\begin{tabular}{lrrrr}\n\\toprule\nPopulation & $n$ models & C\\% & RMSEA & CFI \\\\\n\\midrule\nFull & 5{,}227 & 31.3 & 0.089 & 0.72 \\\\\nDecoder-only & 5{,}226 & 31.3 & 0.088 & 0.72 \\\\\n$\\Delta$ & --- & 0.0 & 0.001 & 0.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMETABENCH MMLU is 99.98\\% decoder-only (5{,}226/5{,}227 models). Removing the single non-decoder model changes nothing (Jaccard\\,=\\,1.0, Table~\\ref{tab:arch}). The poor absolute IRT fit (CFI\\,=\\,0.72) reflects MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity; 98\\% of models show $|L_z|>2$ under 1D IRT. We discuss IRT misspecification in \\S\\ref{sec:limitations}.\n\n%------------------------------------------------------------------------------\n\\subsection{Claim 2: Ground Truth Meta-Critique}\\label{sec:claim2}\n%------------------------------------------------------------------------------\n\nThe enrichment ratio of temporal DIF flags against Li et al.'s web-overlap contamination labels is 0.96---effectively 1.0. This is \\emph{expected}, not evidence of DIF failure: web-overlap labels measure whether an item is publicly accessible (a global property), while DIF measures whether an item functions differently across model cohorts (a differential property). These are fundamentally different constructs.\n\nAny item-level contamination detector validated exclusively against web-overlap labels inherits this mismatch. Min-K\\%, ConStat, and n-gram methods all use such validation. Our semi-synthetic injection (\\S\\ref{sec:claim3}) confirms that DIF can detect differential contamination ($\\Delta$TPR\\,=\\,+0.508 at $p=0.5$), demonstrating that the enrichment$\\approx$1.0 result reflects a ground truth limitation, not a detection limitation.\n\n%------------------------------------------------------------------------------\n\\subsection{Claim 3: Semi-Synthetic Validation Framework}\\label{sec:claim3}\n%------------------------------------------------------------------------------\n\n\\subsubsection{Detection Power on MMLU}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Semi-synthetic detection power with cross-subject matching on MMLU.}\n\\label{tab:semisyn}\n\\begin{tabular}{rrrrrr}\n\\toprule\nExploitation rate $p$ & Baseline TPR & Injected TPR & $\\Delta$TPR & FPR & $\\Delta$FPR \\\\\n\\midrule\n0.0 & 0.326 & 0.326 & 0.000 & 0.314 & 0.000 \\\\\n0.3 & 0.326 & 0.548 & 0.222 & 0.314 & 0.000 \\\\\n0.5 & 0.326 & 0.834 & 0.508 & 0.314 & 0.000 \\\\\n0.7 & 0.326 & 0.990 & 0.664 & 0.314 & 0.000 \\\\\n1.0 & 0.326 & 1.000 & 0.674 & 0.314 & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:semisyn} demonstrates three properties of the framework: (1)~a monotone dose-response relationship from $p=0.3$ to $p=1.0$; (2)~substantial detection power ($\\Delta$TPR\\,=\\,+0.508 at $p=0.5$); and (3)~zero FPR inflation under cross-subject matching ($\\Delta$FPR\\,=\\,0.000 at all exploitation rates).\n\n\\begin{table}[htb]\n\\centering\n\\caption{Within-subject vs.\\ cross-subject matching.}\n\\label{tab:matching}\n\\begin{tabular}{lrrr}\n\\toprule\nMatching & $\\Delta$TPR ($p=0.5$) & $\\Delta$FPR ($p=1.0$) & FPR stable? \\\\\n\\midrule\nWithin-subject & 0.457 & +0.186 & No \\\\\nCross-subject & 0.508 & 0.000 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:matching} highlights a key methodological finding: within-subject matching contaminates the conditioning variable, inflating FPR by +0.186. Cross-subject matching eliminates this inflation while actually improving $\\Delta$TPR (+0.508 vs.\\ +0.457), because the uncontaminated matching variable provides a purer ability estimate.\n\n\\subsubsection{Cross-Benchmark Replication: GSM8K}\n\n\\begin{table}[htb]\n\\centering\n\\caption{GSM8K temporal DIF and semi-synthetic results (1{,}319 items $\\times$ 6{,}702 models).}\n\\label{tab:gsm8k_dif}\n\\begin{tabular}{lrrr}\n\\toprule\nMatching & C\\% & Sanity C\\% & $\\Delta$TPR ($p=1.0$) \\\\\n\\midrule\nStandard (total score) & 18.9 & 0.3 & +0.818 \\\\\nExternal (MMLU score) & 47.4 & --- & +0.517 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:gsm8k_dif} confirms the framework's portability. GSM8K temporal DIF is lower (18.9\\% vs.\\ 31.3\\% on MMLU), consistent with math benchmarks exhibiting more uniform capability improvement. The semi-synthetic $\\Delta$TPR\\,=\\,+0.818 on GSM8K exceeds MMLU's +0.674, attributable to GSM8K's single-domain structure enabling cleaner matching.\n\n%------------------------------------------------------------------------------\n\\subsection{Claim 4: DIF as Diagnostic Lens}\\label{sec:claim4}\n%------------------------------------------------------------------------------\n\n\\subsubsection{Ranking Stability Under DIF Removal}\n\nRemoving all 3{,}918 DIF-flagged items (31.3\\%) from MMLU yields a rank correlation of $\\rho\\approx0.997$ with the original full-benchmark ranking. This confirms massive measurement redundancy: nearly a third of items can be removed with negligible ranking impact.\n\nHowever, DIF removal causes \\emph{more} disruption than random removal of the same number of items ($z=-8$ to $-49\\sigma$ across 21 conditions, all $p<10^{-4}$), confirming that DIF items carry genuine cross-cohort signal. They are non-trivial items---but they are not the most ranking-defining items.\n\n\\subsubsection{Circularity Ablation}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Ranking disruption by removal strategy (representative $z$-scores).}\n\\label{tab:circularity}\n\\begin{tabular}{lr}\n\\toprule\nRemoval strategy & $z$-score \\\\\n\\midrule\nDIF (MH) & $-9.5$ \\\\\nAccuracy-gap & $-157$ \\\\\nHigh-variance & $-108$ \\\\\nHigh-discrimination & $-16$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:circularity} resolves the potential tautology concern: if DIF items were simply the most informative items, their removal would cause maximal disruption. Instead, DIF removal ($z=-9.5$) is 10--16$\\times$ less disruptive than accuracy-gap ($z=-157$) or high-variance ($z=-108$) removal, despite 62.6\\% item overlap with accuracy-gap selection. MH ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items.\n\n\\subsubsection{GSM1K Contamination Gap Correlation}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Correlation between DIF flags and GSM1K contamination gap ($N=33$ models).}\n\\label{tab:gsm1k}\n\\begin{tabular}{lrrl}\n\\toprule\nStatistic & Value & 95\\% BCa CI & Concern \\\\\n\\midrule\nPearson $r$ & $-0.478$ & $[-0.714, -0.155]$ & CI wide \\\\\nSpearman $\\rho$ & $-0.403$ & $[-0.687, -0.031]$ & Upper bound near zero \\\\\nPartial $r$ & $-0.385$ & $[-0.640, -0.058]$ & Marginal control \\\\\n$N$ & 33 & --- & Underpowered \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:gsm1k} presents suggestive evidence that DIF items resist contamination-based gains: models with larger GSM1K contamination gaps show disproportionately lower performance on DIF-C items ($r=-0.478$, $p=0.005$; permutation $p=0.014$). All confidence intervals exclude zero, but the small sample ($N=33$) produces wide CIs. The Spearman CI upper bound ($-0.031$) approaches zero, and we acknowledge this as suggestive evidence requiring replication with $N\\geq100$.\n\n%==============================================================================\n\\section{Supplementary Analyses}\\label{sec:supplementary}\n%==============================================================================\n\nWe report several supplementary analyses that provide robustness checks and contextual baselines.\n\n\\subsection{RL Robustness Validation}\\label{sec:rl}\n\n\\begin{table}[htb]\n\\centering\n\\caption{DIF flag stability under cohort composition change (RL augmentation).}\n\\label{tab:rl}\n\\begin{tabular}{lrrr}\n\\toprule\nCohort composition & $n$ total & C\\% & Jaccard vs.\\ baseline \\\\\n\\midrule\nSFT only & 312 & 30.8 & --- \\\\\nSFT + alignment-RL & 789 & 32.1 & 0.72 \\\\\nSFT + alignment-RL + reasoning-RL & 802 & 31.5 & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAdding 477 alignment-RL models produces stable DIF flags (Jaccard\\,=\\,0.72 vs.\\ SFT-only baseline; Table~\\ref{tab:rl}). However, only 13 reasoning-RL models were available, making RL robustness validation underpowered. TOST equivalence testing is inconclusive ($p=0.14$, bound $\\pm0.05$). We do not claim RL robustness; alignment-RL stability is reported descriptively.\n\n\\begin{table}[htb]\n\\centering\n\\caption{Individual detector AUROC by model training type.}\n\\label{tab:rl_auroc}\n\\begin{tabular}{lrrrr}\n\\toprule\nDetector & SFT & Alignment-RL & Reasoning-RL & DeLong $p$ \\\\\n\\midrule\nMin-K\\% & 0.61 & 0.58 & 0.43 & 0.08 \\\\\nConStat & 0.64 & 0.60 & 0.39 & 0.03 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:rl_auroc} shows that individual contamination detectors (Min-K\\%, ConStat) degrade substantially on reasoning-RL models (AUROC dropping to 0.39--0.43), with ConStat's decline statistically significant (DeLong $p=0.03$). DIF, as a group-level method, cannot be directly compared at the individual-model level.\n\n\\subsection{ConStat Perturbation Evaluation}\\label{sec:constat}\n\n\\begin{table}[htb]\n\\centering\n\\caption{ConStat detection summary (217 paraphrased MMLU items, 15 models).}\n\\label{tab:constat}\n\\begin{tabular}{lrrrr}\n\\toprule\nMetric & Non-RL models & RL models & All \\\\\n\\midrule\n$n$ models & 11 & 4 & 15 \\\\\nDetection rate (FDR 0.05) & 0.27 & 0.14 & 0.23 \\\\\nMean effect size & 0.74 & 0.31 & 0.61 \\\\\nFPR & 0.05 & 0.08 & 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConStat detects 23\\% of items at FDR\\,=\\,0.05 on 15 models with inference access (Table~\\ref{tab:constat}). The near-zero overlap with DIF flags (Jaccard\\,=\\,0.08) confirms that perturbation-based and group-level methods capture different signals. ConStat's requirement for inference access (vs.\\ DIF's use of existing response matrices at scale) limits direct comparison.\n\n\\subsection{DVD Generation Variance Evaluation}\\label{sec:dvd}\n\n\\begin{table}[htb]\n\\centering\n\\caption{DVD bimodal detection by contamination type (500 items, 12 models, 50 responses/item).}\n\\label{tab:dvd}\n\\begin{tabular}{lrrr}\n\\toprule\nContamination type & $n$ items & Bimodal rate & FPR \\\\\n\\midrule\nVerbatim & 150 & 0.31 & 0.08 \\\\\nVariant & 150 & 0.06 & 0.10 \\\\\nClean & 200 & --- & 0.09 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGeneration variance (DVD) primarily detects verbatim memorization (31\\% bimodal rate) with limited sensitivity to variant contamination (6\\%; Table~\\ref{tab:dvd}). Overlap with DIF is near-zero (Jaccard\\,=\\,0.05). Variance score reliability is moderate ($r=0.62$). DVD requires open-weight inference access, excluding closed-source models.\n\n\\subsection{Ensemble Fusion}\\label{sec:ensemble}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Ensemble vs.\\ individual detectors.}\n\\label{tab:ensemble}\n\\begin{tabular}{lrrr}\n\\toprule\nMethod & AUROC & FPR & $n$ models available \\\\\n\\midrule\nDIF (MH) & 0.54 & 0.31 & 5{,}227 \\\\\nConStat & 0.51 & 0.06 & 15 \\\\\nDVD & 0.47 & 0.09 & 12 \\\\\n2-of-3 majority & 0.58 & 0.11 & 12 \\\\\nWeighted fusion & 0.62 & 0.09 & 12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA weighted ensemble achieves AUROC\\,=\\,0.62 (Table~\\ref{tab:ensemble}), a marginal +0.08 improvement over the best single detector. However, cross-validation weight stability is low (0.43), and only 45\\% of configurations achieve FPR\\,$<$\\,0.10. More fundamentally, the ensemble is trained against the same web-overlap labels whose validity our Claim~2 questions, creating a circularity. We report this as a negative result and defer principled ensemble design to future work pending better ground truth infrastructure.\n\n\\subsection{Bifactor IRT Equating Pilot}\\label{sec:bifactor}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Bifactor IRT fit indices (general + 57 subject-specific factors).}\n\\label{tab:bifactor}\n\\begin{tabular}{lrrl}\n\\toprule\nIndex & Value & Threshold & Interpretation \\\\\n\\midrule\nRMSEA & 0.052 & $<$0.06 acceptable & Borderline acceptable \\\\\nCFI & 0.81 & $>$0.90 good & Below threshold \\\\\nTLI & 0.78 & $>$0.90 good & Below threshold \\\\\nSRMR & 0.068 & $<$0.08 acceptable & Acceptable \\\\\nGeneral factor \\% variance & 34\\% & $>$50\\% unidim. & Confirms multidimensionality \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe bifactor model converges (2{,}847 iterations, 127\\,GB peak memory, 38 hours) but achieves mediocre fit (Table~\\ref{tab:bifactor}). The general factor explains only 34\\% of variance, confirming that MMLU is inherently multidimensional. Equated scores correlate at $\\rho=0.94$ with original scores, marginally below the 0.95 target. The bifactor analysis serves primarily as sensitivity analysis: DIF findings under bifactor correction change C\\% from 31.3\\% to approximately 28--29\\%, confirming qualitative robustness. CFI/TLI below 0.90 is partially attributable to the extreme scale (12{,}508 items $\\times$ 5{,}227 models) that systematically depresses absolute fit indices.\n\n\\subsection{Item Generation Calibration}\\label{sec:itemgen}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Item generation difficulty calibration for DIF-flagged item replacement.}\n\\label{tab:itemgen}\n\\begin{tabular}{lrrr}\n\\toprule\nMethod & Difficulty $\\rho$ & $n$ items & Notes \\\\\n\\midrule\nPrompt-based targeting & 0.32 & 150 & Below literature 0.10--0.45 \\\\\nStudent simulation & 0.58 & 150 & Below target 0.75 \\\\\nCombined (iterative, 2 rounds) & 0.61 & 80 & Improved but insufficient \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAutomated item generation for replacing DIF-flagged items does not achieve the precision required for equating (Table~\\ref{tab:itemgen}). Difficulty correlation with target items reaches $\\rho=0.58$ via student simulation, well below the $0.75$ target. Cognitive-level match rate is 71\\% and human quality ratings average 3.2/5. This is a negative result: LLM-based item generation for benchmark maintenance remains an open problem, particularly for multidomain benchmarks like MMLU where 57 subjects require diverse domain expertise.\n\n\\subsection{Cumulative Bayesian DIF}\\label{sec:bayesian}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Cumulative detection power by number of simulated benchmark administrations.}\n\\label{tab:bayesian}\n\\begin{tabular}{rrrrrr}\n\\toprule\n$n$ admins & Power ($\\delta=1.0$) & Power ($\\delta=1.4$) & Power ($\\delta=1.6$) & FPR \\\\\n\\midrule\n1 & 0.41 & 0.68 & 0.72 & 0.042 \\\\\n2 & 0.56 & 0.77 & 0.83 & 0.045 \\\\\n3 & 0.68 & 0.82 & 0.89 & 0.048 \\\\\n4 & 0.74 & 0.86 & 0.92 & 0.047 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSimulation of cumulative Bayesian DIF priors~\\citep{sinharay2006study} shows that power at $\\delta=1.0$ improves from 0.41 (single administration) to 0.74 (four administrations), while FPR remains controlled at $\\sim$0.048 (Table~\\ref{tab:bayesian}). For $\\delta=1.4$, power reaches 0.82 after three administrations. This is a simulation-only result without empirical validation; METABENCH provides only one effective ``administration.'' As new model generations emerge, the same benchmark is effectively re-administered, making cumulative priors applicable in principle.\n\n\\subsection{Graceful Degradation Under Item Replacement}\\label{sec:degradation}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Validity metrics under progressive item replacement.}\n\\label{tab:degradation}\n\\begin{tabular}{rrrr}\n\\toprule\nReplacement \\% & Rank $\\rho$ & Cronbach's $\\alpha$ & Subjects underrepresented \\\\\n\\midrule\n0 & 1.000 & 0.946 & 0 \\\\\n5 & 0.998 & 0.943 & 0 \\\\\n10 & 0.995 & 0.938 & 0 \\\\\n20 & 0.987 & 0.924 & 0 \\\\\n35 & 0.974 & 0.908 & 1 \\\\\n50 & 0.961 & 0.891 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:degradation} quantifies a validity floor at approximately 35\\% replacement ($\\rho>0.98$, $\\alpha>0.92$). This aligns with our finding that 31.3\\% of items exhibit large DIF---these items could in principle be replaced without substantial validity loss, given sufficiently calibrated replacements. The practical barrier is item generation quality (\\S\\ref{sec:itemgen}).\n\n\\subsection{Item-Focused Trees}\\label{sec:ift}\n\n\\begin{table}[htb]\n\\centering\n\\caption{MH vs.\\ Item-Focused Trees concordance.}\n\\label{tab:ift}\n\\begin{tabular}{lrrrr}\n\\toprule\nMetric & MH ETS C & IFT significant & Overlap & Jaccard \\\\\n\\midrule\n$n$ flagged & 3{,}918 & 4{,}127 & 3{,}306 & 0.68 \\\\\n\\% flagged & 31.3 & 33.0 & 26.4 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nItem-Focused Trees, which treat model release date as a continuous covariate rather than requiring a categorical split, flag 33.0\\% of items (Table~\\ref{tab:ift}), with 78\\% concordance with MH flags (Jaccard\\,=\\,0.68). The primary temporal split date identified by IFT is November 15, 2023, near the GPT-4/Llama-2 to Llama-3/Mixtral generational transition. IFT detects 209 items with gradual drift that MH misses, while MH catches 612 items with non-monotone DIF patterns invisible to IFT. Additionally, 14.7\\% of items show nonlinear temporal trends, suggesting that some DIF reflects multi-factor dynamics beyond simple temporal shifts.\n\n%==============================================================================\n\\section{Discussion and Limitations}\\label{sec:limitations}\n%==============================================================================\n\n\\paragraph{IRT Misspecification.}\nOur DIF analysis uses 1D IRT for matching, but MMLU is inherently multidimensional (57 subjects, general factor explaining only 34\\% of variance). 98\\% of models show $|L_z|>2$ under 1D IRT. While the bifactor pilot suggests DIF findings are qualitatively robust to this misspecification (C\\% decreasing from 31.3\\% to $\\sim$28--29\\%), CFI\\,=\\,0.81 and TLI\\,=\\,0.78 indicate incomplete model fit. Multidimensional IRT-based DIF (MIMIC models, propensity-score matching) is a natural future direction.\n\n\\paragraph{Injection Simplicity.}\nOur semi-synthetic framework uses a simple contamination mechanism (flipping incorrect$\\to$correct). Real contamination may produce different patterns (partial memorization, verbatim recall with different error types). However, our mechanism represents the minimal contamination model; more complex patterns would produce \\emph{larger} DIF effects, making our power estimates conservative.\n\n\\paragraph{Single-Benchmark Focus.}\nPrimary results are on MMLU; GSM8K replication (1{,}319 items $\\times$ 6{,}702 models) confirms framework portability but full generalization to diverse benchmarks (coding, reasoning, multilingual) remains future work.\n\n\\paragraph{GSM1K Sample Size.}\nThe GSM1K contamination-gap correlation ($N=33$) is underpowered with wide confidence intervals. The Spearman CI upper bound ($-0.031$) approaches zero. Replication with $N\\geq100$ matched models is needed before drawing strong conclusions about the contamination-resistance property of DIF items.\n\n\\paragraph{RL Robustness.}\nOnly 13 reasoning-RL models were available. TOST equivalence testing is inconclusive. As reasoning-RL models proliferate, re-evaluation with a larger sample is warranted.\n\n\\paragraph{Item Generation.}\nAutomated replacement of DIF-flagged items does not achieve equating-grade calibration ($\\rho=0.58$ vs.\\ target $0.75$). Benchmark maintenance via item replacement remains practically infeasible without substantial advances in calibrated item generation.\n\n%==============================================================================\n\\section{Conclusion}\\label{sec:conclusion}\n%==============================================================================\n\nWe present the first large-scale psychometric DIF analysis of an LLM benchmark, analyzing 5{,}227 models $\\times$ 12{,}508 MMLU items. Four findings emerge: (1)~31.3\\% of items are functionally unstable across model generations, predominantly due to item-specific factors rather than aggregate capability improvement; (2)~web-overlap contamination labels are fundamentally mismatched for validating item-level differential detectors; (3)~semi-synthetic $\\Delta$TPR with cross-subject matching provides a reusable, FPR-controlled validation infrastructure portable across benchmarks; and (4)~DIF items serve as a diagnostic lens revealing which capability dimensions shift across generations, not merely a quality filter. Rankings remain highly stable ($\\rho\\approx0.997$) despite 31\\% instability, confirming that temporal instability does not threaten benchmark validity but reveals important structural properties of how LLM capabilities evolve.\n\nWe bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework---not a new algorithm. We hope this work motivates the LLM evaluation community to adopt psychometric quality-control practices that educational testing has refined over decades.\n\n%==============================================================================\n% References\n%==============================================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Mantel and Haenszel(1959)]{mantel1959statistical}\nN.~Mantel and W.~Haenszel.\n\\newblock Statistical aspects of the analysis of data from retrospective studies of disease.\n\\newblock \\emph{Journal of the National Cancer Institute}, 22(4):719--748, 1959.\n\n\\bibitem[Holland and Thayer(1988)]{holland1988differential}\nP.~W. Holland and D.~T. Thayer.\n\\newblock Differential item performance and the {M}antel-{H}aenszel procedure.\n\\newblock In H.~Wainer and H.~I. Braun, editors, \\emph{Test Validity}, pages 129--145. Lawrence Erlbaum, 1988.\n\n\\bibitem[Zieky(1993)]{zieky1993practical}\nM.~Zieky.\n\\newblock A practical guide to the {ETS} policy statement on the use of {DIF} statistics.\n\\newblock Technical report, Educational Testing Service, Princeton, NJ, 1993.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[De~Koninck et~al.(2024)]{dekoninck2024constat}\nJ.~De~Koninck, M.~Müller, and P.~Fischer.\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Becker et~al.(2024)]{becker2024metabench}\nB.~Becker, J.~Stöckel, and S.~Bulling.\n\\newblock {METABENCH}: A large-scale meta-benchmark of {LLM} evaluation results.\n\\newblock \\emph{arXiv preprint arXiv:2407.10844}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo, L.~Weber, L.~Choshen, Y.~Sun, G.~Xu, and M.~Yurochkin.\n\\newblock {TinyBenchmarks}: Evaluating {LLMs} with fewer examples.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Tutz and Berger(2016)]{tutz2016item}\nG.~Tutz and M.~Berger.\n\\newblock Item-focused trees for the identification of items in differential item functioning.\n\\newblock \\emph{Psychometrika}, 81(3):727--750, 2016.\n\n\\bibitem[Sinharay et~al.(2006)]{sinharay2006study}\nS.~Sinharay, R.~G. Johnson, and H.~S. Stern.\n\\newblock Posterior predictive assessment of item response theory models.\n\\newblock \\emph{Applied Psychological Measurement}, 30(4):298--321, 2006.\n\n\\bibitem[Li et~al.(2024)]{li2024contamination}\nY.~Li, Y.~Guo, G.~Zuo, and W.~Fan.\n\\newblock A survey on {LLM} benchmark contamination.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8370e6b-7e93-4349-8466-6fc849f52865",
  "isSidechain": false,
  "requestId": "req_011CbFGApz4WgfTDc693ggZb",
  "type": "assistant",
  "uuid": "e607741f-66bf-47bf-9746-6f81d97f9db0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RBP37MkoWqNbHmMtmBNVJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6544,
      "cache_read_input_tokens": 39609,
      "output_tokens": 11508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11508,
          "cache_read_input_tokens": 39609,
          "cache_creation_input_tokens": 6544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6544
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

_source line 21 · 2026-05-21T06:48:33.264Z_

<details><summary>↩ Tool result · `toolu_01Ete1WTGf8MeFXsbEHXmQH1`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e607741f-66bf-47bf-9746-6f81d97f9db0",
  "isSidechain": false,
  "promptId": "f9190119-bc3e-4325-b2be-2617c4e8f5d7",
  "type": "user",
  "uuid": "a6237103-f991-4384-bb5a-fb54bd27a59d",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/paper.tex",
    "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\n\\title{Psychometric Characterization of Temporal Item Instability\\\\in LLM Benchmarks: A Large-Scale DIF Analysis of MMLU}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nLLM benchmarks implicitly assume temporal score comparability---that scores from different model generations reflect the same underlying construct. We test this assumption by applying Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis to the METABENCH response matrix (5{,}227 models $\\times$ 12{,}508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\nWe report four findings.\n(1)~31.3\\% of MMLU items exhibit large temporal DIF (ETS C class, $|\\Delta_\\text{MH}|\\geq1.5$) between 2023 and 2024-H1 model cohorts; item-level decomposition shows domain accuracy improvement explains at most 2.4 percentage points (7.6\\%) of this instability.\n(2)~Web-overlap contamination labels, routinely used as ground truth for item-level detectors, measure global exposure rather than differential contamination; DIF enrichment $\\approx$1.0 against such labels is expected, not failure.\n(3)~We introduce a semi-synthetic validation framework ($\\Delta$TPR methodology) with cross-subject matching that eliminates false-positive inflation ($\\Delta$FPR\\,=\\,0.000) and generalizes across benchmarks (GSM8K $\\Delta$TPR\\,=\\,+0.818).\n(4)~DIF items carry genuine cross-cohort signal ($z=-8$ to $-49\\sigma$ vs.\\ random removal) yet are the \\emph{least} disruptive non-random removal strategy ($z=-9.5$ vs.\\ accuracy-gap $z=-157$), serving as a diagnostic lens rather than a quality filter.\nOverall rankings remain highly stable after removing all flagged items ($\\rho\\approx0.997$), confirming that instability does not threaten validity but reveals which capability dimensions shift across model generations.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\\label{sec:intro}\n%==============================================================================\n\nWhen we report that ``Model B outperforms Model A on MMLU,'' we presume both scores reflect the same latent construct measured under equivalent conditions. Psychometrics calls this assumption \\emph{measurement invariance}: an item that is easy for Group~A examinees of a given ability level should be equally easy for Group~B examinees at the same ability level. When this fails---when an item's difficulty shifts after controlling for overall ability---the item exhibits \\emph{Differential Item Functioning} (DIF).\n\nDIF analysis is a mature tool in educational and psychological testing, with over six decades of methodological development since Mantel and Haenszel's original proposal~\\citep{mantel1959statistical,holland1988differential}. It has been applied to ensure fairness across demographic groups, flag compromised items in high-stakes exams, and validate the temporal stability of test scores. Yet it has seen virtually no application to LLM evaluation, despite the field's growing concern about benchmark contamination and score inflation.\n\nWe apply MH-DIF to the METABENCH response matrix---5{,}227 models $\\times$ 12{,}508 MMLU items---using models released before and after a temporal cutoff as reference and focal groups. This constitutes the largest-scale DIF analysis ever conducted on an LLM benchmark. Our key finding is that \\textbf{31.3\\% of MMLU items are functionally unstable across model generations} (ETS C classification, $|\\Delta_\\text{MH}|\\geq1.5$), but this instability does not threaten ranking validity ($\\rho\\approx0.997$ between full and stable-only rankings).\n\n\\paragraph{Instability $\\neq$ Invalidity.} This framing is central: DIF flags items whose measurement properties changed across model generations. This is a \\emph{diagnostic signal}, not a quality verdict. The massive ranking stability ($\\rho\\approx0.997$) under 31\\% item removal reveals enormous measurement redundancy in MMLU. The value of DIF analysis lies not in filtering ``bad'' items but in understanding \\emph{what changed} across generations---which capability dimensions are shifting and how.\n\nWe make four contributions:\n\\begin{enumerate}\n    \\item An empirical characterization of temporal item instability at unprecedented scale, showing that 31.3\\% of MMLU items exhibit large DIF that is predominantly item-specific (domain accuracy improvement explains $\\leq$7.6\\%).\n    \\item A ground truth meta-critique: web-overlap contamination labels cannot validate item-level differential detectors, affecting the validity claims of existing methods.\n    \\item A reusable semi-synthetic validation framework with cross-subject matching that eliminates FPR inflation and generalizes across benchmarks.\n    \\item A demonstration that DIF serves as a diagnostic lens for understanding cross-generational capability shifts, not merely a quality filter.\n\\end{enumerate}\n\n%==============================================================================\n\\section{Related Work}\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Benchmark Contamination Detection.}\nSeveral methods detect training-set contamination in LLMs. Min-K\\%~\\citep{shi2024detecting} uses token-level perplexity; ConStat~\\citep{dekoninck2024constat} compares performance on original vs.\\ paraphrased items; n-gram overlap methods check for verbatim memorization. These methods typically validate against web-overlap labels (e.g., Li et al.'s MMLU contamination annotations), which measure whether an item is publicly accessible rather than whether it functions differently across model groups.\n\n\\paragraph{Differential Item Functioning.}\nDIF analysis originated with \\citet{mantel1959statistical} and was formalized for testing contexts by \\citet{holland1988differential}. The ETS classification system~\\citep{zieky1993practical} categorizes DIF magnitude into negligible (A: $|\\Delta_\\text{MH}|<1.0$), moderate (B: $1.0\\leq|\\Delta_\\text{MH}|<1.5$), and large (C: $|\\Delta_\\text{MH}|\\geq1.5$). Item-Focused Trees~\\citep{tutz2016item} extend DIF to continuous covariates. We apply these standard methods without modification; our contribution is empirical, not algorithmic.\n\n\\paragraph{LLM Benchmark Methodology.}\nGrowing Pains~\\citep{polo2024tinybenchmarks} uses anchor items for efficient evaluation. METABENCH~\\citep{becker2024metabench} aggregates 5{,}227 models' responses on MMLU, providing the response matrix we analyze. Our DIF analysis complements these efforts by identifying which anchor items are degrading across model generations.\n\n%==============================================================================\n\\section{Method}\\label{sec:method}\n%==============================================================================\n\n\\subsection{Mantel-Haenszel DIF Analysis}\\label{sec:mh}\n\nFor each item $j$, the MH procedure tests whether the odds of a correct response differ between reference (R) and focal (F) groups after stratifying by total score. The MH odds ratio $\\alpha_\\text{MH}$ is:\n\\begin{equation}\n    \\alpha_\\text{MH} = \\frac{\\sum_k A_k D_k / T_k}{\\sum_k B_k C_k / T_k},\n\\end{equation}\nwhere $A_k, B_k, C_k, D_k$ are the entries of the $2\\times2$ contingency table at score stratum $k$ and $T_k$ is the stratum total. The log-odds ratio is converted to the $\\Delta_\\text{MH}$ scale:\n\\begin{equation}\n    \\Delta_\\text{MH} = -2.35 \\ln(\\alpha_\\text{MH}).\n\\end{equation}\n\nWe use the ETS classification: items with $|\\Delta_\\text{MH}|\\geq1.5$ and a statistically significant MH $\\chi^2$ test ($p<0.05$) are classified as ETS C (large DIF). The dual requirement of both effect size and statistical significance provides implicit protection against multiple testing~\\citep{zieky1993practical}.\n\n\\paragraph{Cohort Definitions.}\nWe define temporal cohorts by model release date: reference (2023) and focal (2024-H1). We also examine ability-based cohorts (Q1 vs.\\ Q5 of total score) and within-family cohorts (e.g., Llama-2 vs.\\ Llama-3) as sensitivity analyses.\n\n\\subsection{Semi-Synthetic Validation Framework}\\label{sec:semisyn}\n\nTo validate DIF detection power, we inject known differential contamination into real METABENCH response matrices. For a set of ``contaminated'' items and a target exploitation rate $p$, we flip $p$-fraction of incorrect focal-group responses to correct, simulating the effect of contamination that differentially benefits newer models.\n\n\\paragraph{$\\Delta$TPR Methodology.}\nDetection power is measured as:\n\\begin{equation}\n    \\Delta\\text{TPR}(p) = \\text{TPR}_\\text{injected}(p) - \\text{TPR}_\\text{baseline}(0),\n\\end{equation}\nisolating the detection power increase attributable to injected contamination.\n\n\\paragraph{Cross-Subject Matching.}\nStandard MH uses total score on the same subject as the matching variable. When contamination affects items within that subject, the matching variable is itself contaminated, inflating FPR. We propose \\emph{cross-subject matching}: using total score on \\emph{other} MMLU subjects as the matching variable. This eliminates FPR inflation ($\\Delta$FPR\\,=\\,0.000) while preserving detection power.\n\n%==============================================================================\n\\section{Experiments}\\label{sec:experiments}\n%==============================================================================\n\n\\subsection{Claim 1: Temporal Item Instability}\\label{sec:claim1}\n\n\\subsubsection{Main DIF Analysis (MMLU)}\n\nWe apply MH-DIF to the full METABENCH MMLU matrix (5{,}227 models $\\times$ 12{,}508 items) with temporal cohorts (2023 vs.\\ 2024-H1; $n_\\text{ref}=1{,}253$, $n_\\text{foc}=656$).\n\n\\begin{table}[htb]\n\\centering\n\\caption{Temporal DIF summary by ETS classification on MMLU.}\n\\label{tab:temporal_dif}\n\\begin{tabular}{lrrr}\n\\toprule\nETS Class & $n$ items & \\% & Mean $|\\Delta_\\text{MH}|$ \\\\\n\\midrule\nA (negligible) & 8{,}590 & 68.7 & 0.43 \\\\\nB (moderate) & 2{,}641 & 21.1 & 1.24 \\\\\nC (large) & 1{,}277 & 10.2 & 2.31 \\\\\nB+C (flagged) & 3{,}918 & 31.3 & 1.58 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:temporal_dif} shows that 31.3\\% of items (3{,}918 / 12{,}508) are flagged as exhibiting moderate or large DIF. A random-split sanity check produces only 0.18\\% flagged items, confirming that the temporal signal is not a statistical artifact.\n\n\\subsubsection{Cohort Sensitivity}\n\n\\begin{table}[htb]\n\\centering\n\\caption{DIF results under different cohort definitions.}\n\\label{tab:cohort}\n\\begin{tabular}{lrrrr}\n\\toprule\nCohort & $n_\\text{ref}$ & $n_\\text{foc}$ & C\\% & Enrichment \\\\\n\\midrule\nTemporal (2023 vs 2024-H1) & 1{,}253 & 656 & 31.3 & 0.96 \\\\\nAbility (Q1 vs Q5) & $\\sim$1{,}044 & $\\sim$1{,}044 & 2.9 & 1.19 \\\\\nWithin-family (Llama-2 vs 3) & 161 & 308 & 61.3 & --- \\\\\nRandom split (sanity) & 950 & 950 & 0.18 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cohort} reveals three patterns: (1)~temporal cohorts produce substantial DIF (31.3\\%); (2)~ability-based cohorts produce minimal DIF (2.9\\%), indicating that the temporal signal is not an artifact of ability differences; (3)~within-family comparison (Llama-2 vs.\\ 3) produces the highest DIF (61.3\\%), consistent with rapid capability gains within an architecture family. The near-zero enrichment against Li et al.\\ contamination labels ($0.96\\approx1.0$) motivates the ground truth meta-critique in \\S\\ref{sec:claim2}. Domain-specific DIF correlates modestly with accuracy improvement ($\\rho=0.307$, $p=0.02$), but item-level decomposition shows domain improvement explains at most 2.4 percentage points of 31.3\\% C\\% (7.6\\%).\n\n\\subsubsection{Architecture Stratification}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Architecture stratification: DIF and IRT fit.}\n\\label{tab:arch}\n\\begin{tabular}{lrrrr}\n\\toprule\nPopulation & $n$ models & C\\% & RMSEA & CFI \\\\\n\\midrule\nFull & 5{,}227 & 31.3 & 0.089 & 0.72 \\\\\nDecoder-only & 5{,}226 & 31.3 & 0.088 & 0.72 \\\\\n$\\Delta$ & --- & 0.0 & 0.001 & 0.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMETABENCH MMLU is 99.98\\% decoder-only (5{,}226/5{,}227 models). Removing the single non-decoder model changes nothing (Jaccard\\,=\\,1.0, Table~\\ref{tab:arch}). The poor absolute IRT fit (CFI\\,=\\,0.72) reflects MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity; 98\\% of models show $|L_z|>2$ under 1D IRT. We discuss IRT misspecification in \\S\\ref{sec:limitations}.\n\n%------------------------------------------------------------------------------\n\\subsection{Claim 2: Ground Truth Meta-Critique}\\label{sec:claim2}\n%------------------------------------------------------------------------------\n\nThe enrichment ratio of temporal DIF flags against Li et al.'s web-overlap contamination labels is 0.96---effectively 1.0. This is \\emph{expected}, not evidence of DIF failure: web-overlap labels measure whether an item is publicly accessible (a global property), while DIF measures whether an item functions differently across model cohorts (a differential property). These are fundamentally different constructs.\n\nAny item-level contamination detector validated exclusively against web-overlap labels inherits this mismatch. Min-K\\%, ConStat, and n-gram methods all use such validation. Our semi-synthetic injection (\\S\\ref{sec:claim3}) confirms that DIF can detect differential contamination ($\\Delta$TPR\\,=\\,+0.508 at $p=0.5$), demonstrating that the enrichment$\\approx$1.0 result reflects a ground truth limitation, not a detection limitation.\n\n%------------------------------------------------------------------------------\n\\subsection{Claim 3: Semi-Synthetic Validation Framework}\\label{sec:claim3}\n%------------------------------------------------------------------------------\n\n\\subsubsection{Detection Power on MMLU}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Semi-synthetic detection power with cross-subject matching on MMLU.}\n\\label{tab:semisyn}\n\\begin{tabular}{rrrrrr}\n\\toprule\nExploitation rate $p$ & Baseline TPR & Injected TPR & $\\Delta$TPR & FPR & $\\Delta$FPR \\\\\n\\midrule\n0.0 & 0.326 & 0.326 & 0.000 & 0.314 & 0.000 \\\\\n0.3 & 0.326 & 0.548 & 0.222 & 0.314 & 0.000 \\\\\n0.5 & 0.326 & 0.834 & 0.508 & 0.314 & 0.000 \\\\\n0.7 & 0.326 & 0.990 & 0.664 & 0.314 & 0.000 \\\\\n1.0 & 0.326 & 1.000 & 0.674 & 0.314 & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:semisyn} demonstrates three properties of the framework: (1)~a monotone dose-response relationship from $p=0.3$ to $p=1.0$; (2)~substantial detection power ($\\Delta$TPR\\,=\\,+0.508 at $p=0.5$); and (3)~zero FPR inflation under cross-subject matching ($\\Delta$FPR\\,=\\,0.000 at all exploitation rates).\n\n\\begin{table}[htb]\n\\centering\n\\caption{Within-subject vs.\\ cross-subject matching.}\n\\label{tab:matching}\n\\begin{tabular}{lrrr}\n\\toprule\nMatching & $\\Delta$TPR ($p=0.5$) & $\\Delta$FPR ($p=1.0$) & FPR stable? \\\\\n\\midrule\nWithin-subject & 0.457 & +0.186 & No \\\\\nCross-subject & 0.508 & 0.000 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:matching} highlights a key methodological finding: within-subject matching contaminates the conditioning variable, inflating FPR by +0.186. Cross-subject matching eliminates this inflation while actually improving $\\Delta$TPR (+0.508 vs.\\ +0.457), because the uncontaminated matching variable provides a purer ability estimate.\n\n\\subsubsection{Cross-Benchmark Replication: GSM8K}\n\n\\begin{table}[htb]\n\\centering\n\\caption{GSM8K temporal DIF and semi-synthetic results (1{,}319 items $\\times$ 6{,}702 models).}\n\\label{tab:gsm8k_dif}\n\\begin{tabular}{lrrr}\n\\toprule\nMatching & C\\% & Sanity C\\% & $\\Delta$TPR ($p=1.0$) \\\\\n\\midrule\nStandard (total score) & 18.9 & 0.3 & +0.818 \\\\\nExternal (MMLU score) & 47.4 & --- & +0.517 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:gsm8k_dif} confirms the framework's portability. GSM8K temporal DIF is lower (18.9\\% vs.\\ 31.3\\% on MMLU), consistent with math benchmarks exhibiting more uniform capability improvement. The semi-synthetic $\\Delta$TPR\\,=\\,+0.818 on GSM8K exceeds MMLU's +0.674, attributable to GSM8K's single-domain structure enabling cleaner matching.\n\n%------------------------------------------------------------------------------\n\\subsection{Claim 4: DIF as Diagnostic Lens}\\label{sec:claim4}\n%------------------------------------------------------------------------------\n\n\\subsubsection{Ranking Stability Under DIF Removal}\n\nRemoving all 3{,}918 DIF-flagged items (31.3\\%) from MMLU yields a rank correlation of $\\rho\\approx0.997$ with the original full-benchmark ranking. This confirms massive measurement redundancy: nearly a third of items can be removed with negligible ranking impact.\n\nHowever, DIF removal causes \\emph{more} disruption than random removal of the same number of items ($z=-8$ to $-49\\sigma$ across 21 conditions, all $p<10^{-4}$), confirming that DIF items carry genuine cross-cohort signal. They are non-trivial items---but they are not the most ranking-defining items.\n\n\\subsubsection{Circularity Ablation}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Ranking disruption by removal strategy (representative $z$-scores).}\n\\label{tab:circularity}\n\\begin{tabular}{lr}\n\\toprule\nRemoval strategy & $z$-score \\\\\n\\midrule\nDIF (MH) & $-9.5$ \\\\\nAccuracy-gap & $-157$ \\\\\nHigh-variance & $-108$ \\\\\nHigh-discrimination & $-16$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:circularity} resolves the potential tautology concern: if DIF items were simply the most informative items, their removal would cause maximal disruption. Instead, DIF removal ($z=-9.5$) is 10--16$\\times$ less disruptive than accuracy-gap ($z=-157$) or high-variance ($z=-108$) removal, despite 62.6\\% item overlap with accuracy-gap selection. MH ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items.\n\n\\subsubsection{GSM1K Contamination Gap Correlation}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Correlation between DIF flags and GSM1K contamination gap ($N=33$ models).}\n\\label{tab:gsm1k}\n\\begin{tabular}{lrrl}\n\\toprule\nStatistic & Value & 95\\% BCa CI & Concern \\\\\n\\midrule\nPearson $r$ & $-0.478$ & $[-0.714, -0.155]$ & CI wide \\\\\nSpearman $\\rho$ & $-0.403$ & $[-0.687, -0.031]$ & Upper bound near zero \\\\\nPartial $r$ & $-0.385$ & $[-0.640, -0.058]$ & Marginal control \\\\\n$N$ & 33 & --- & Underpowered \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:gsm1k} presents suggestive evidence that DIF items resist contamination-based gains: models with larger GSM1K contamination gaps show disproportionately lower performance on DIF-C items ($r=-0.478$, $p=0.005$; permutation $p=0.014$). All confidence intervals exclude zero, but the small sample ($N=33$) produces wide CIs. The Spearman CI upper bound ($-0.031$) approaches zero, and we acknowledge this as suggestive evidence requiring replication with $N\\geq100$.\n\n%==============================================================================\n\\section{Supplementary Analyses}\\label{sec:supplementary}\n%==============================================================================\n\nWe report several supplementary analyses that provide robustness checks and contextual baselines.\n\n\\subsection{RL Robustness Validation}\\label{sec:rl}\n\n\\begin{table}[htb]\n\\centering\n\\caption{DIF flag stability under cohort composition change (RL augmentation).}\n\\label{tab:rl}\n\\begin{tabular}{lrrr}\n\\toprule\nCohort composition & $n$ total & C\\% & Jaccard vs.\\ baseline \\\\\n\\midrule\nSFT only & 312 & 30.8 & --- \\\\\nSFT + alignment-RL & 789 & 32.1 & 0.72 \\\\\nSFT + alignment-RL + reasoning-RL & 802 & 31.5 & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAdding 477 alignment-RL models produces stable DIF flags (Jaccard\\,=\\,0.72 vs.\\ SFT-only baseline; Table~\\ref{tab:rl}). However, only 13 reasoning-RL models were available, making RL robustness validation underpowered. TOST equivalence testing is inconclusive ($p=0.14$, bound $\\pm0.05$). We do not claim RL robustness; alignment-RL stability is reported descriptively.\n\n\\begin{table}[htb]\n\\centering\n\\caption{Individual detector AUROC by model training type.}\n\\label{tab:rl_auroc}\n\\begin{tabular}{lrrrr}\n\\toprule\nDetector & SFT & Alignment-RL & Reasoning-RL & DeLong $p$ \\\\\n\\midrule\nMin-K\\% & 0.61 & 0.58 & 0.43 & 0.08 \\\\\nConStat & 0.64 & 0.60 & 0.39 & 0.03 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:rl_auroc} shows that individual contamination detectors (Min-K\\%, ConStat) degrade substantially on reasoning-RL models (AUROC dropping to 0.39--0.43), with ConStat's decline statistically significant (DeLong $p=0.03$). DIF, as a group-level method, cannot be directly compared at the individual-model level.\n\n\\subsection{ConStat Perturbation Evaluation}\\label{sec:constat}\n\n\\begin{table}[htb]\n\\centering\n\\caption{ConStat detection summary (217 paraphrased MMLU items, 15 models).}\n\\label{tab:constat}\n\\begin{tabular}{lrrrr}\n\\toprule\nMetric & Non-RL models & RL models & All \\\\\n\\midrule\n$n$ models & 11 & 4 & 15 \\\\\nDetection rate (FDR 0.05) & 0.27 & 0.14 & 0.23 \\\\\nMean effect size & 0.74 & 0.31 & 0.61 \\\\\nFPR & 0.05 & 0.08 & 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConStat detects 23\\% of items at FDR\\,=\\,0.05 on 15 models with inference access (Table~\\ref{tab:constat}). The near-zero overlap with DIF flags (Jaccard\\,=\\,0.08) confirms that perturbation-based and group-level methods capture different signals. ConStat's requirement for inference access (vs.\\ DIF's use of existing response matrices at scale) limits direct comparison.\n\n\\subsection{DVD Generation Variance Evaluation}\\label{sec:dvd}\n\n\\begin{table}[htb]\n\\centering\n\\caption{DVD bimodal detection by contamination type (500 items, 12 models, 50 responses/item).}\n\\label{tab:dvd}\n\\begin{tabular}{lrrr}\n\\toprule\nContamination type & $n$ items & Bimodal rate & FPR \\\\\n\\midrule\nVerbatim & 150 & 0.31 & 0.08 \\\\\nVariant & 150 & 0.06 & 0.10 \\\\\nClean & 200 & --- & 0.09 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGeneration variance (DVD) primarily detects verbatim memorization (31\\% bimodal rate) with limited sensitivity to variant contamination (6\\%; Table~\\ref{tab:dvd}). Overlap with DIF is near-zero (Jaccard\\,=\\,0.05). Variance score reliability is moderate ($r=0.62$). DVD requires open-weight inference access, excluding closed-source models.\n\n\\subsection{Ensemble Fusion}\\label{sec:ensemble}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Ensemble vs.\\ individual detectors.}\n\\label{tab:ensemble}\n\\begin{tabular}{lrrr}\n\\toprule\nMethod & AUROC & FPR & $n$ models available \\\\\n\\midrule\nDIF (MH) & 0.54 & 0.31 & 5{,}227 \\\\\nConStat & 0.51 & 0.06 & 15 \\\\\nDVD & 0.47 & 0.09 & 12 \\\\\n2-of-3 majority & 0.58 & 0.11 & 12 \\\\\nWeighted fusion & 0.62 & 0.09 & 12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA weighted ensemble achieves AUROC\\,=\\,0.62 (Table~\\ref{tab:ensemble}), a marginal +0.08 improvement over the best single detector. However, cross-validation weight stability is low (0.43), and only 45\\% of configurations achieve FPR\\,$<$\\,0.10. More fundamentally, the ensemble is trained against the same web-overlap labels whose validity our Claim~2 questions, creating a circularity. We report this as a negative result and defer principled ensemble design to future work pending better ground truth infrastructure.\n\n\\subsection{Bifactor IRT Equating Pilot}\\label{sec:bifactor}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Bifactor IRT fit indices (general + 57 subject-specific factors).}\n\\label{tab:bifactor}\n\\begin{tabular}{lrrl}\n\\toprule\nIndex & Value & Threshold & Interpretation \\\\\n\\midrule\nRMSEA & 0.052 & $<$0.06 acceptable & Borderline acceptable \\\\\nCFI & 0.81 & $>$0.90 good & Below threshold \\\\\nTLI & 0.78 & $>$0.90 good & Below threshold \\\\\nSRMR & 0.068 & $<$0.08 acceptable & Acceptable \\\\\nGeneral factor \\% variance & 34\\% & $>$50\\% unidim. & Confirms multidimensionality \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe bifactor model converges (2{,}847 iterations, 127\\,GB peak memory, 38 hours) but achieves mediocre fit (Table~\\ref{tab:bifactor}). The general factor explains only 34\\% of variance, confirming that MMLU is inherently multidimensional. Equated scores correlate at $\\rho=0.94$ with original scores, marginally below the 0.95 target. The bifactor analysis serves primarily as sensitivity analysis: DIF findings under bifactor correction change C\\% from 31.3\\% to approximately 28--29\\%, confirming qualitative robustness. CFI/TLI below 0.90 is partially attributable to the extreme scale (12{,}508 items $\\times$ 5{,}227 models) that systematically depresses absolute fit indices.\n\n\\subsection{Item Generation Calibration}\\label{sec:itemgen}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Item generation difficulty calibration for DIF-flagged item replacement.}\n\\label{tab:itemgen}\n\\begin{tabular}{lrrr}\n\\toprule\nMethod & Difficulty $\\rho$ & $n$ items & Notes \\\\\n\\midrule\nPrompt-based targeting & 0.32 & 150 & Below literature 0.10--0.45 \\\\\nStudent simulation & 0.58 & 150 & Below target 0.75 \\\\\nCombined (iterative, 2 rounds) & 0.61 & 80 & Improved but insufficient \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAutomated item generation for replacing DIF-flagged items does not achieve the precision required for equating (Table~\\ref{tab:itemgen}). Difficulty correlation with target items reaches $\\rho=0.58$ via student simulation, well below the $0.75$ target. Cognitive-level match rate is 71\\% and human quality ratings average 3.2/5. This is a negative result: LLM-based item generation for benchmark maintenance remains an open problem, particularly for multidomain benchmarks like MMLU where 57 subjects require diverse domain expertise.\n\n\\subsection{Cumulative Bayesian DIF}\\label{sec:bayesian}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Cumulative detection power by number of simulated benchmark administrations.}\n\\label{tab:bayesian}\n\\begin{tabular}{rrrrrr}\n\\toprule\n$n$ admins & Power ($\\delta=1.0$) & Power ($\\delta=1.4$) & Power ($\\delta=1.6$) & FPR \\\\\n\\midrule\n1 & 0.41 & 0.68 & 0.72 & 0.042 \\\\\n2 & 0.56 & 0.77 & 0.83 & 0.045 \\\\\n3 & 0.68 & 0.82 & 0.89 & 0.048 \\\\\n4 & 0.74 & 0.86 & 0.92 & 0.047 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSimulation of cumulative Bayesian DIF priors~\\citep{sinharay2006study} shows that power at $\\delta=1.0$ improves from 0.41 (single administration) to 0.74 (four administrations), while FPR remains controlled at $\\sim$0.048 (Table~\\ref{tab:bayesian}). For $\\delta=1.4$, power reaches 0.82 after three administrations. This is a simulation-only result without empirical validation; METABENCH provides only one effective ``administration.'' As new model generations emerge, the same benchmark is effectively re-administered, making cumulative priors applicable in principle.\n\n\\subsection{Graceful Degradation Under Item Replacement}\\label{sec:degradation}\n\n\\begin{table}[htb]\n\\centering\n\\caption{Validity metrics under progressive item replacement.}\n\\label{tab:degradation}\n\\begin{tabular}{rrrr}\n\\toprule\nReplacement \\% & Rank $\\rho$ & Cronbach's $\\alpha$ & Subjects underrepresented \\\\\n\\midrule\n0 & 1.000 & 0.946 & 0 \\\\\n5 & 0.998 & 0.943 & 0 \\\\\n10 & 0.995 & 0.938 & 0 \\\\\n20 & 0.987 & 0.924 & 0 \\\\\n35 & 0.974 & 0.908 & 1 \\\\\n50 & 0.961 & 0.891 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:degradation} quantifies a validity floor at approximately 35\\% replacement ($\\rho>0.98$, $\\alpha>0.92$). This aligns with our finding that 31.3\\% of items exhibit large DIF---these items could in principle be replaced without substantial validity loss, given sufficiently calibrated replacements. The practical barrier is item generation quality (\\S\\ref{sec:itemgen}).\n\n\\subsection{Item-Focused Trees}\\label{sec:ift}\n\n\\begin{table}[htb]\n\\centering\n\\caption{MH vs.\\ Item-Focused Trees concordance.}\n\\label{tab:ift}\n\\begin{tabular}{lrrrr}\n\\toprule\nMetric & MH ETS C & IFT significant & Overlap & Jaccard \\\\\n\\midrule\n$n$ flagged & 3{,}918 & 4{,}127 & 3{,}306 & 0.68 \\\\\n\\% flagged & 31.3 & 33.0 & 26.4 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nItem-Focused Trees, which treat model release date as a continuous covariate rather than requiring a categorical split, flag 33.0\\% of items (Table~\\ref{tab:ift}), with 78\\% concordance with MH flags (Jaccard\\,=\\,0.68). The primary temporal split date identified by IFT is November 15, 2023, near the GPT-4/Llama-2 to Llama-3/Mixtral generational transition. IFT detects 209 items with gradual drift that MH misses, while MH catches 612 items with non-monotone DIF patterns invisible to IFT. Additionally, 14.7\\% of items show nonlinear temporal trends, suggesting that some DIF reflects multi-factor dynamics beyond simple temporal shifts.\n\n%==============================================================================\n\\section{Discussion and Limitations}\\label{sec:limitations}\n%==============================================================================\n\n\\paragraph{IRT Misspecification.}\nOur DIF analysis uses 1D IRT for matching, but MMLU is inherently multidimensional (57 subjects, general factor explaining only 34\\% of variance). 98\\% of models show $|L_z|>2$ under 1D IRT. While the bifactor pilot suggests DIF findings are qualitatively robust to this misspecification (C\\% decreasing from 31.3\\% to $\\sim$28--29\\%), CFI\\,=\\,0.81 and TLI\\,=\\,0.78 indicate incomplete model fit. Multidimensional IRT-based DIF (MIMIC models, propensity-score matching) is a natural future direction.\n\n\\paragraph{Injection Simplicity.}\nOur semi-synthetic framework uses a simple contamination mechanism (flipping incorrect$\\to$correct). Real contamination may produce different patterns (partial memorization, verbatim recall with different error types). However, our mechanism represents the minimal contamination model; more complex patterns would produce \\emph{larger} DIF effects, making our power estimates conservative.\n\n\\paragraph{Single-Benchmark Focus.}\nPrimary results are on MMLU; GSM8K replication (1{,}319 items $\\times$ 6{,}702 models) confirms framework portability but full generalization to diverse benchmarks (coding, reasoning, multilingual) remains future work.\n\n\\paragraph{GSM1K Sample Size.}\nThe GSM1K contamination-gap correlation ($N=33$) is underpowered with wide confidence intervals. The Spearman CI upper bound ($-0.031$) approaches zero. Replication with $N\\geq100$ matched models is needed before drawing strong conclusions about the contamination-resistance property of DIF items.\n\n\\paragraph{RL Robustness.}\nOnly 13 reasoning-RL models were available. TOST equivalence testing is inconclusive. As reasoning-RL models proliferate, re-evaluation with a larger sample is warranted.\n\n\\paragraph{Item Generation.}\nAutomated replacement of DIF-flagged items does not achieve equating-grade calibration ($\\rho=0.58$ vs.\\ target $0.75$). Benchmark maintenance via item replacement remains practically infeasible without substantial advances in calibrated item generation.\n\n%==============================================================================\n\\section{Conclusion}\\label{sec:conclusion}\n%==============================================================================\n\nWe present the first large-scale psychometric DIF analysis of an LLM benchmark, analyzing 5{,}227 models $\\times$ 12{,}508 MMLU items. Four findings emerge: (1)~31.3\\% of items are functionally unstable across model generations, predominantly due to item-specific factors rather than aggregate capability improvement; (2)~web-overlap contamination labels are fundamentally mismatched for validating item-level differential detectors; (3)~semi-synthetic $\\Delta$TPR with cross-subject matching provides a reusable, FPR-controlled validation infrastructure portable across benchmarks; and (4)~DIF items serve as a diagnostic lens revealing which capability dimensions shift across generations, not merely a quality filter. Rankings remain highly stable ($\\rho\\approx0.997$) despite 31\\% instability, confirming that temporal instability does not threaten benchmark validity but reveals important structural properties of how LLM capabilities evolve.\n\nWe bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework---not a new algorithm. We hope this work motivates the LLM evaluation community to adopt psychometric quality-control practices that educational testing has refined over decades.\n\n%==============================================================================\n% References\n%==============================================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Mantel and Haenszel(1959)]{mantel1959statistical}\nN.~Mantel and W.~Haenszel.\n\\newblock Statistical aspects of the analysis of data from retrospective studies of disease.\n\\newblock \\emph{Journal of the National Cancer Institute}, 22(4):719--748, 1959.\n\n\\bibitem[Holland and Thayer(1988)]{holland1988differential}\nP.~W. Holland and D.~T. Thayer.\n\\newblock Differential item performance and the {M}antel-{H}aenszel procedure.\n\\newblock In H.~Wainer and H.~I. Braun, editors, \\emph{Test Validity}, pages 129--145. Lawrence Erlbaum, 1988.\n\n\\bibitem[Zieky(1993)]{zieky1993practical}\nM.~Zieky.\n\\newblock A practical guide to the {ETS} policy statement on the use of {DIF} statistics.\n\\newblock Technical report, Educational Testing Service, Princeton, NJ, 1993.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[De~Koninck et~al.(2024)]{dekoninck2024constat}\nJ.~De~Koninck, M.~Müller, and P.~Fischer.\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Becker et~al.(2024)]{becker2024metabench}\nB.~Becker, J.~Stöckel, and S.~Bulling.\n\\newblock {METABENCH}: A large-scale meta-benchmark of {LLM} evaluation results.\n\\newblock \\emph{arXiv preprint arXiv:2407.10844}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo, L.~Weber, L.~Choshen, Y.~Sun, G.~Xu, and M.~Yurochkin.\n\\newblock {TinyBenchmarks}: Evaluating {LLMs} with fewer examples.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Tutz and Berger(2016)]{tutz2016item}\nG.~Tutz and M.~Berger.\n\\newblock Item-focused trees for the identification of items in differential item functioning.\n\\newblock \\emph{Psychometrika}, 81(3):727--750, 2016.\n\n\\bibitem[Sinharay et~al.(2006)]{sinharay2006study}\nS.~Sinharay, R.~G. Johnson, and H.~S. Stern.\n\\newblock Posterior predictive assessment of item response theory models.\n\\newblock \\emph{Applied Psychological Measurement}, 30(4):298--321, 2006.\n\n\\bibitem[Li et~al.(2024)]{li2024contamination}\nY.~Li, Y.~Guo, G.~Zuo, and W.~Fan.\n\\newblock A survey on {LLM} benchmark contamination.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "e607741f-66bf-47bf-9746-6f81d97f9db0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "a6237103-f991-4384-bb5a-fb54bd27a59d",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with IRT analysis",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e"
}
```

---

### Tool call

_source line 24 · 2026-05-21T06:48:36.768Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TJmUetwZv5cZSCVJ9Ww1qY`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6237103-f991-4384-bb5a-fb54bd27a59d",
  "isSidechain": false,
  "requestId": "req_011CbFGTKzmZuSbHQcwtrnqM",
  "type": "assistant",
  "uuid": "2801880b-7952-4b98-a1a7-513ba2109672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVZPcTXTFtxViZmUunuH4S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11578,
      "cache_read_input_tokens": 46153,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 46153,
          "cache_creation_input_tokens": 11578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11578
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

_source line 25 · 2026-05-21T06:48:37.712Z_

<details><summary>↩ Tool result · `toolu_01TJmUetwZv5cZSCVJ9Ww1qY`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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

Package natbib Warning: Citation `mantel1959statistical' on page 1 undefined on
 input line 38.


Package natbib Warning: Citation `holland1988differential' on page 1 undefined 
on input line 38.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu
t line 57.


Package natbib Warning: Citation `dekoninck2024constat' on page 2 undefined on 
input line 57.


Package natbib Warning: Citation `mantel1959statistical' on page 2 undefined on
 input line 60.


Package natbib Warning: Citation `holland1988differential' on page 2 undefined 
on input line 60.


Package natbib Warning: Citation `zieky1993practical' on page 2 undefined on in
put line 60.


Package natbib Warning: Citation `tutz2016item' on page 2 undefined on input li
ne 60.


Package natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o
n input line 63.


Package natbib Warning: Citation `becker2024metabench' on page 2 undefined on i
nput line 63.


Overfull \hbox (38.07907pt too wide) in paragraph at lines 63--64
 []\OT1/cmr/bx/n/10 LLM Bench-mark Method-ol-ogy.[] \OT1/cmr/m/n/10 Grow-ing Pa
ins (\OT1/cmr/bx/n/10 ?\OT1/cmr/m/n/10 ) uses an-chor items for ef-fi-cient eva
l-u-a-tion. METABENCH (\OT1/cmr/bx/n/10 ?\OT1/cmr/m/n/10 )

Package natbib Warning: Citation `zieky1993practical' on page 2 undefined on in
put line 80.

[2]

LaTeX Warning: Reference `tab:temporal_dif' on page 3 undefined on input line 1
25.


LaTeX Warning: Reference `tab:cohort' on page 3 undefined on input line 145.


LaTeX Warning: Reference `sec:claim2' on page 3 undefined on input line 145.

[3]

LaTeX Warning: Reference `tab:arch' on page 4 undefined on input line 164.


LaTeX Warning: Reference `sec:limitations' on page 4 undefined on input line 16
4.


LaTeX Warning: Reference `sec:claim3' on page 4 undefined on input line 172.


LaTeX Warning: Reference `tab:semisyn' on page 4 undefined on input line 197.


LaTeX Warning: Reference `tab:matching' on page 4 undefined on input line 213.

[4]

LaTeX Warning: Reference `tab:gsm8k_dif' on page 5 undefined on input line 231.



LaTeX Warning: Reference `tab:circularity' on page 5 undefined on input line 26
1.


LaTeX Warning: Reference `tab:gsm1k' on page 5 undefined on input line 281.

[5]

LaTeX Warning: Reference `tab:rl' on page 6 undefined on input line 306.


LaTeX Warning: Reference `tab:rl_auroc' on page 6 undefined on input line 322.


LaTeX Warning: Reference `tab:constat' on page 6 undefined on input line 342.


LaTeX Warning: Reference `tab:dvd' on page 6 undefined on input line 361.


LaTeX Warning: Reference `tab:ensemble' on page 6 undefined on input line 382.

[6]

LaTeX Warning: Reference `tab:bifactor' on page 7 undefined on input line 403.


LaTeX Warning: Reference `tab:itemgen' on page 7 undefined on input line 422.


Package natbib Warning: Citation `sinharay2006study' on page 7 undefined on inp
ut line 442.


LaTeX Warning: Reference `tab:bayesian' on page 7 undefined on input line 442.

[7]

LaTeX Warning: Reference `tab:degradation' on page 8 undefined on input line 46
4.


LaTeX Warning: Reference `sec:itemgen' on page 8 undefined on input line 464.


LaTeX Warning: Reference `tab:ift' on page 8 undefined on input line 482.

[8] [9]

Package natbib Warning: There were undefined citations.

[10] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmti9.pfb>
Output written on paper.pdf (10 pages, 265058 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
nts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6] [7] [8] [9] [10]
(./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.60
0pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmti9.pfb>
Output written on paper.pdf (10 pages, 269157 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2801880b-7952-4b98-a1a7-513ba2109672",
  "isSidechain": false,
  "promptId": "f9190119-bc3e-4325-b2be-2617c4e8f5d7",
  "type": "user",
  "uuid": "9703fa06-6750-41dc-bfb4-851e25524457",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `mantel1959statistical' on page 1 undefined on\n input line 38.\n\n\nPackage natbib Warning: Citation `holland1988differential' on page 1 undefined \non input line 38.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu\nt line 57.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 2 undefined on \ninput line 57.\n\n\nPackage natbib Warning: Citation `mantel1959statistical' on page 2 undefined on\n input line 60.\n\n\nPackage natbib Warning: Citation `holland1988differential' on page 2 undefined \non input line 60.\n\n\nPackage natbib Warning: Citation `zieky1993practical' on page 2 undefined on in\nput line 60.\n\n\nPackage natbib Warning: Citation `tutz2016item' on page 2 undefined on input li\nne 60.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o\nn input line 63.\n\n\nPackage natbib Warning: Citation `becker2024metabench' on page 2 undefined on i\nnput line 63.\n\n\nOverfull \\hbox (38.07907pt too wide) in paragraph at lines 63--64\n []\\OT1/cmr/bx/n/10 LLM Bench-mark Method-ol-ogy.[] \\OT1/cmr/m/n/10 Grow-ing Pa\nins (\\OT1/cmr/bx/n/10 ?\\OT1/cmr/m/n/10 ) uses an-chor items for ef-fi-cient eva\nl-u-a-tion. METABENCH (\\OT1/cmr/bx/n/10 ?\\OT1/cmr/m/n/10 )\n\nPackage natbib Warning: Citation `zieky1993practical' on page 2 undefined on in\nput line 80.\n\n[2]\n\nLaTeX Warning: Reference `tab:temporal_dif' on page 3 undefined on input line 1\n25.\n\n\nLaTeX Warning: Reference `tab:cohort' on page 3 undefined on input line 145.\n\n\nLaTeX Warning: Reference `sec:claim2' on page 3 undefined on input line 145.\n\n[3]\n\nLaTeX Warning: Reference `tab:arch' on page 4 undefined on input line 164.\n\n\nLaTeX Warning: Reference `sec:limitations' on page 4 undefined on input line 16\n4.\n\n\nLaTeX Warning: Reference `sec:claim3' on page 4 undefined on input line 172.\n\n\nLaTeX Warning: Reference `tab:semisyn' on page 4 undefined on input line 197.\n\n\nLaTeX Warning: Reference `tab:matching' on page 4 undefined on input line 213.\n\n[4]\n\nLaTeX Warning: Reference `tab:gsm8k_dif' on page 5 undefined on input line 231.\n\n\n\nLaTeX Warning: Reference `tab:circularity' on page 5 undefined on input line 26\n1.\n\n\nLaTeX Warning: Reference `tab:gsm1k' on page 5 undefined on input line 281.\n\n[5]\n\nLaTeX Warning: Reference `tab:rl' on page 6 undefined on input line 306.\n\n\nLaTeX Warning: Reference `tab:rl_auroc' on page 6 undefined on input line 322.\n\n\nLaTeX Warning: Reference `tab:constat' on page 6 undefined on input line 342.\n\n\nLaTeX Warning: Reference `tab:dvd' on page 6 undefined on input line 361.\n\n\nLaTeX Warning: Reference `tab:ensemble' on page 6 undefined on input line 382.\n\n[6]\n\nLaTeX Warning: Reference `tab:bifactor' on page 7 undefined on input line 403.\n\n\nLaTeX Warning: Reference `tab:itemgen' on page 7 undefined on input line 422.\n\n\nPackage natbib Warning: Citation `sinharay2006study' on page 7 undefined on inp\nut line 442.\n\n\nLaTeX Warning: Reference `tab:bayesian' on page 7 undefined on input line 442.\n\n[7]\n\nLaTeX Warning: Reference `tab:degradation' on page 8 undefined on input line 46\n4.\n\n\nLaTeX Warning: Reference `sec:itemgen' on page 8 undefined on input line 464.\n\n\nLaTeX Warning: Reference `tab:ift' on page 8 undefined on input line 482.\n\n[8] [9]\n\nPackage natbib Warning: There were undefined citations.\n\n[10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmti9.pfb>\nOutput written on paper.pdf (10 pages, 265058 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6] [7] [8] [9] [10]\n(./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.60\n0pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmti9.pfb>\nOutput written on paper.pdf (10 pages, 269157 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2801880b-7952-4b98-a1a7-513ba2109672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "9703fa06-6750-41dc-bfb4-851e25524457",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with IRT analysis",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e"
}
```

---

### Assistant

_source line 28 · 2026-05-21T06:48:40.005Z_

<details><summary>Logged reasoning block</summary>

```text
There's a "Label(s) may have changed" warning, which means I need a third pass. Let me run one more compilation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9703fa06-6750-41dc-bfb4-851e25524457",
  "isSidechain": false,
  "requestId": "req_011CbFGTexY5pHhgtD4APDuh",
  "type": "assistant",
  "uuid": "8d5af9f4-b397-4915-a192-ae04c5fc4403",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111SVbeHR9k3bxa9AQGAoKN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6625,
      "cache_read_input_tokens": 57731,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 57731,
          "cache_creation_input_tokens": 6625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6625
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

_source line 29 · 2026-05-21T06:48:41.008Z_

One more pass to resolve the remaining label reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d5af9f4-b397-4915-a192-ae04c5fc4403",
  "isSidechain": false,
  "requestId": "req_011CbFGTexY5pHhgtD4APDuh",
  "type": "assistant",
  "uuid": "4ab3c2e7-e9e4-4309-8e74-92816d8497c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111SVbeHR9k3bxa9AQGAoKN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6625,
      "cache_read_input_tokens": 57731,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 57731,
          "cache_creation_input_tokens": 6625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6625
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

_source line 30 · 2026-05-21T06:48:43.630Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018MjaTEpV6oVWFmajYUXpoU`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ab3c2e7-e9e4-4309-8e74-92816d8497c9",
  "isSidechain": false,
  "requestId": "req_011CbFGTexY5pHhgtD4APDuh",
  "type": "assistant",
  "uuid": "831718ac-534a-448a-b9fd-560b17825f97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111SVbeHR9k3bxa9AQGAoKN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6625,
      "cache_read_input_tokens": 57731,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 57731,
          "cache_creation_input_tokens": 6625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6625
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

_source line 31 · 2026-05-21T06:48:44.136Z_

<details><summary>↩ Tool result · `toolu_018MjaTEpV6oVWFmajYUXpoU`</summary>

```text
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>
Output written on paper.pdf (10 pages, 269157 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "831718ac-534a-448a-b9fd-560b17825f97",
  "isSidechain": false,
  "promptId": "f9190119-bc3e-4325-b2be-2617c4e8f5d7",
  "type": "user",
  "uuid": "1944637a-543d-4e21-961d-8f5cca7f5856",
  "toolUseResult": {
    "stdout": "hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>\nOutput written on paper.pdf (10 pages, 269157 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "831718ac-534a-448a-b9fd-560b17825f97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T06:48:48.326Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011jpWNCT1Hx35hjityPZXax`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"Warning|Error|Output\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1944637a-543d-4e21-961d-8f5cca7f5856",
  "isSidechain": false,
  "requestId": "req_011CbFGU8NoKqJ6jG6peeeyy",
  "type": "assistant",
  "uuid": "592c10e7-86ac-4104-805b-ad42a1420ae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVoJ46BozgTTfHgrR9HhPH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 64356,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 273,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 64356,
          "cache_creation_input_tokens": 273,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 273
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

_source line 33 · 2026-05-21T06:48:48.843Z_

<details><summary>↩ Tool result · `toolu_011jpWNCT1Hx35hjityPZXax`</summary>

```text
Output written on paper.pdf (10 pages, 269157 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "592c10e7-86ac-4104-805b-ad42a1420ae5",
  "isSidechain": false,
  "promptId": "f9190119-bc3e-4325-b2be-2617c4e8f5d7",
  "type": "user",
  "uuid": "0dea8e82-8d5d-4d57-9f09-bb3e51439dbd",
  "toolUseResult": {
    "stdout": "Output written on paper.pdf (10 pages, 269157 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "592c10e7-86ac-4104-805b-ad42a1420ae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-21T06:48:48.845Z_

```json
{
  "parentUuid": "0dea8e82-8d5d-4d57-9f09-bb3e51439dbd",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8ca9f4bb-3a74-48c0-86ab-cd66853e82a4",
  "timestamp": "2026-05-21T06:48:48.845Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 35 · 2026-05-21T06:49:04.534Z_

PDF compiled cleanly — 10 pages, no warnings or errors. All 13 experiments from `experiment_data.json` have dedicated sections/tables:

- **Main body (Claims 1–4)**: temporal DIF (Tables 1–2), architecture stratification (Table 3), ground truth meta-critique, semi-synthetic validation (Tables 4–5), GSM8K replication (Table 6), circularity ablation (Table 7), GSM1K correlation (Table 8)
- **Supplementary (\S5)**: RL robustness (Tables 9–10), ConStat (Table 11), DVD (Table 12), ensemble (Table 13), bifactor IRT (Table 14), item generation (Table 15), Bayesian DIF (Table 16), graceful degradation (Table 17), IFT (Table 18)

Output: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ca9f4bb-3a74-48c0-86ab-cd66853e82a4",
  "isSidechain": false,
  "requestId": "req_011CbFGUUWm5AeCNzTHFDMhn",
  "type": "assistant",
  "uuid": "5bc0cfe1-2a8a-4850-926a-f091d6e7febb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E9A9D8fF9vUMhNuQXJHaHe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 213,
      "cache_read_input_tokens": 64629,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 64629,
          "cache_creation_input_tokens": 213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 213
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "5bc0cfe1-2a8a-4850-926a-f091d6e7febb",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with IRT analysis",
  "sessionId": "1c6b9965-4730-46a2-a3a4-07c965d9e09e"
}
```

---
