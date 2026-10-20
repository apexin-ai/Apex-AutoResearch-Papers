# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T141728 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/68384416-f199-481e-b490-5f37e9ab5fc0.jsonl`
- **Structured JSON:** [`eae50dd88d47900b1c3a.json`](../../sessions/ea/eae50dd88d47900b1c3a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T14:45:57.409Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T14:45:57.409Z",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T141728 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：Claim 1和Claim 3被接受为solid empirical contributions；Claim 2的meta-critique被1-2位reviewers视为 \"well-known but under-documented limitation\"——需在rebuttal中补充5+篇使用web-overlap labels做item-level validation的具体引用以证明field确实在犯这个错误；Claim 4的actionability论证依赖plan_032的z=8.5 random baseline对比，但至少1位reviewer质疑cohort asymmetry可能反映model quality confound而非DIF-specific effect；ρ=0.997的\"instability ≠ invalidity\"张力在Introduction中upfront framing帮助了，但1位reviewer 仍写\"if the rankings are this stable, the practical significance of 31% instability is unclear\"。Rebuttal策略：用plan_030 Simpson's paradox作为\"models got better ≠ items changed\" 的defense line；用plan_029 permutation null（p<0.001）正面回应\"is 31% above chance\"； HellaSwag/GSM8K较低C%（17-19%）的解释需补充benchmark structural differences（item count, domain homogeneity）。整体需要strong rebuttal + 1个supplementary experiment（per-family stratified permutation）才能从3.5推到4.0 Conference accept线。Claims 1和3 accepted without major caveat； Claim 2需要additional prior work citations；Claim 4需要降低prescriptive tone。 页面压缩从10→8页导致plan_018 threshold sensitivity table和plan_022 de-duplication detail 被移入appendix，1位reviewer要求在main text恢复threshold robustness summary。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T14:45:57.412Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T14:45:57.412Z",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0"
}
```

---

## Round 1

42 recorded events

### User

_source line 3 · 2026-05-21T14:45:57.432Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T141728 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：Claim 1和Claim 3被接受为solid empirical contributions；Claim 2的meta-critique被1-2位reviewers视为 "well-known but under-documented limitation"——需在rebuttal中补充5+篇使用web-overlap labels做item-level validation的具体引用以证明field确实在犯这个错误；Claim 4的actionability论证依赖plan_032的z=8.5 random baseline对比，但至少1位reviewer质疑cohort asymmetry可能反映model quality confound而非DIF-specific effect；ρ=0.997的"instability ≠ invalidity"张力在Introduction中upfront framing帮助了，但1位reviewer 仍写"if the rankings are this stable, the practical significance of 31% instability is unclear"。Rebuttal策略：用plan_030 Simpson's paradox作为"models got better ≠ items changed" 的defense line；用plan_029 permutation null（p<0.001）正面回应"is 31% above chance"； HellaSwag/GSM8K较低C%（17-19%）的解释需补充benchmark structural differences（item count, domain homogeneity）。整体需要strong rebuttal + 1个supplementary experiment（per-family stratified permutation）才能从3.5推到4.0 Conference accept线。Claims 1和3 accepted without major caveat； Claim 2需要additional prior work citations；Claim 4需要降低prescriptive tone。 页面压缩从10→8页导致plan_018 threshold sensitivity table和plan_022 de-duplication detail 被移入appendix，1位reviewer要求在main text恢复threshold robustness summary。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f57e5fc9-2e08-4bef-bfaf-9d1eef656e3e",
  "type": "user",
  "uuid": "53b0da5e-4302-4e16-bbe9-dad2134e2ba2",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T14:45:57.431Z_

```json
{
  "parentUuid": "53b0da5e-4302-4e16-bbe9-dad2134e2ba2",
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
  "uuid": "be4149a9-ce29-462a-843f-6567a1e438c6",
  "timestamp": "2026-05-21T14:45:57.431Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T14:45:57.431Z_

```json
{
  "parentUuid": "be4149a9-ce29-462a-843f-6567a1e438c6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0148fccb-bd88-4df7-9ef3-3934b80112a1",
  "timestamp": "2026-05-21T14:45:57.431Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
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
  "aiTitle": "Generate dream paper for IRT equated benchmark",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0"
}
```

---

### Assistant

_source line 7 · 2026-05-21T14:46:00.534Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0148fccb-bd88-4df7-9ef3-3934b80112a1",
  "isSidechain": false,
  "requestId": "req_011CbFtrp5JcrCQdR76cWEUp",
  "type": "assistant",
  "uuid": "df81d66d-d3a5-42d9-833e-9bb15e53ae33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrGSaquMXkMTZzMfczRjpx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12481,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12481
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

_source line 8 · 2026-05-21T14:46:01.530Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TXRRwinQe8PNu2yMCfvHsL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df81d66d-d3a5-42d9-833e-9bb15e53ae33",
  "isSidechain": false,
  "requestId": "req_011CbFtrp5JcrCQdR76cWEUp",
  "type": "assistant",
  "uuid": "2049467f-0ed4-40cd-906e-a1dff24060d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrGSaquMXkMTZzMfczRjpx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12481,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12481
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

_source line 9 · 2026-05-21T14:46:01.953Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B97udgkbvcfdHcgACiWv1W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2049467f-0ed4-40cd-906e-a1dff24060d6",
  "isSidechain": false,
  "requestId": "req_011CbFtrp5JcrCQdR76cWEUp",
  "type": "assistant",
  "uuid": "ba7915c3-4353-4665-8526-03edbe33b81c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrGSaquMXkMTZzMfczRjpx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12481,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12481
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

_source line 10 · 2026-05-21T14:46:01.960Z_

<details><summary>↩ Tool result · `toolu_01B97udgkbvcfdHcgACiWv1W`</summary>

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
  "parentUuid": "ba7915c3-4353-4665-8526-03edbe33b81c",
  "isSidechain": false,
  "promptId": "f57e5fc9-2e08-4bef-bfaf-9d1eef656e3e",
  "type": "user",
  "uuid": "415a661a-5b8c-4d6d-b8b5-81d25a86b62f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n",
      "numLines": 124,
      "startLine": 1,
      "totalLines": 124
    }
  },
  "sourceToolAssistantUUID": "ba7915c3-4353-4665-8526-03edbe33b81c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T14:46:02.034Z_

<details><summary>↩ Tool result · `toolu_01TXRRwinQe8PNu2yMCfvHsL`</summary>

```text
1	[
2	  {
3	    "name": "real_data_dif_mmlu",
4	    "description": "对METABENCH MMLU响应矩阵（5219模型×12508题目）进行MH-DIF分析。包括temporal cohort split (2023 vs 2024-H1)、ability-quintile split、within-family confound control (Llama-2 vs Llama-3)、domain-specificity分析、Li et al. web-overlap proxy验证。\n",
5	    "results": {
6	      "temporal_cohort": {
7	        "n_ref": 1080,
8	        "n_foc": 807,
9	        "ets_c_pct": 31.3,
10	        "ets_b_pct": 20.5,
11	        "ets_a_pct": 48.2,
12	        "mean_delta_mh_c_items": 2.14,
13	        "median_delta_mh_c_items": 1.78
14	      },
15	      "ability_cohort": {
16	        "ets_c_pct": 2.9,
17	        "enrichment": 1.19
18	      },
19	      "within_family": {
20	        "llama2_vs_llama3_c_pct": 61.3,
21	        "mistral_vs_mixtral_c_pct": 38.7,
22	        "llama_jaccard_with_temporal": 0.28
23	      },
24	      "domain_specificity": {
25	        "spearman_rho_acc_improvement_vs_c_pct": 0.307,
26	        "spearman_p": 0.02,
27	        "n_subjects": 57,
28	        "all_subjects_have_dif": true,
29	        "c_pct_range": [
30	          20.7,
31	          48.4
32	        ]
33	      },
34	      "proxy_validation": {
35	        "li_et_al_coverage": 0.738,
36	        "enrichment_temporal": 0.96,
37	        "fpr_li_clean_temporal": 0.318,
38	        "enrichment_ability": 1.19,
39	        "fpr_li_clean_ability": 0.027
40	      },
41	      "sanity_check": {
42	        "random_split_c_pct": 0.18,
43	        "temporal_ability_jaccard": 0.014
44	      }
45	    },
46	    "tables": [
47	      {
48	        "name": "Table 1: Temporal DIF Summary",
49	        "content": "4-way sensitivity matrix: cohort × item filtering → C% values"
50	      },
51	      {
52	        "name": "Table 2: Domain-Specificity",
53	        "content": "57 subjects × C% × accuracy improvement correlation"
54	      }
55	    ],
56	    "figures": [],
57	    "analysis": "核心结果solid。Median档reviewers的主要friction点：(1) within-family Llama-2v3的C%=61.3% 远高于temporal 31.3%，需要解释为什么family comparison不是更好的design；(2) domain ρ=0.307 虽然p=0.02但effect size modest，需要plan_019 item-level decomposition作为补充； (3) Li et al. proxy validation的\"negative result\"需要更清晰的framing——是validation failure 还是expected orthogonality。8页压缩下within-family detail可能被移入appendix。\n\n\n在median档位下，31.3% C%是核心发现，被Claim 1直接支撑。Reviewers接受这个数字的statistical significance（random split仅0.18%），但至少1位reviewer要求更强的causal language hedging—— 因为within-family分析（Llama-2 vs Llama-3 C%=61.3%）显示family-level capability jump也会 产生高DIF，temporal cohort的31.3%可能混合了genuine item instability和capability-driven DIF。 ρ=0.307的domain-level correlation被接受为modest ecological correlation，但reviewer要求 明确\"item-level decomposition shows only 2.4pp explained\"（来自plan_019/030）。 Enrichment≈0.96支撑Claim 2但被1位reviewer视为\"expected by construction\"。Ability cohort 的2.9% C%作为negative control被接受。\n"
58	  },
59	  {
60	    "name": "rl_robustness_validation",
61	    "description": "验证DIF对reasoning-RL模型的鲁棒性。从METABENCH筛选alignment-RL模型（DPO/ORPO，N≈477）， 外加10-15个open-weight reasoning-RL模型（GRPO/PPO），测试DIF检测稳定性并与传统检测器对比。\n",
62	    "results": {
63	      "alignment_rl_cohort": {
64	        "n_models": 477,
65	        "c_pct_with_alignment_rl": 31.1,
66	        "c_pct_without": 31.3,
67	        "jaccard_flags_overlap": 0.968,
68	        "flag_stability": "negligible change"
69	      },
70	      "reasoning_rl_models": {
71	        "n_available": 13,
72	        "models_tested": [
73	          "deepseek-r1-7b",
74	          "deepseek-r1-32b",
75	          "qwen2.5-rl-7b",
76	          "qwen2.5-rl-14b",
77	          "qwen2.5-rl-32b",
78	          "o1-mini-proxy",
79	          "skywork-or1-8b",
80	          "open-reasoner-7b",
81	          "marco-o1-7b",
82	          "k2-65b",
83	          "rstar-math-7b",
84	          "still-2-1.5b",
85	          "llemma-rl-7b"
86	        ],
87	        "c_pct_with_rl_in_focal": 31.0,
88	        "c_pct_change": -0.3,
89	        "jaccard_with_vs_without_rl": 0.971
90	      },
91	      "traditional_detector_comparison": {
92	        "mink_auroc_non_rl": 0.714,
93	        "mink_auroc_rl_models": 0.528,
94	        "mink_auroc_delta": -0.186,
95	        "constat_auroc_non_rl": 0.681,
96	        "constat_auroc_rl_models": 0.513,
97	        "constat_auroc_delta": -0.168,
98	        "dif_retention_ratio": 0.987
99	      },
100	      "statistical_tests": {
101	        "delong_mink_p": 0.089,
102	        "delong_constat_p": 0.112,
103	        "tost_equivalence": "inconclusive (CI: [-0.04, 0.07], bounds ±0.10)",
104	        "bootstrap_ci_dif_retention": [
105	          0.93,
106	          1.03
107	        ]
108	      },
109	      "power_analysis": {
110	        "partial_exploitation_p04": "delta_MH≈0.84, TPR≈0.31",
111	        "partial_exploitation_p07": "delta_MH≈1.18, TPR≈0.52",
112	        "partial_exploitation_p10": "delta_MH≈1.68, TPR≈0.76",
113	        "detection_boundary": "p≈0.55 for TPR≥0.50 at N=100"
114	      }
115	    },
116	    "tables": [
117	      {
118	        "name": "Table S1 (Appendix): RL Robustness Comparison",
119	        "content": "AUROC comparison across DIF/Min-K%/ConStat × model type (non-RL, alignment-RL, reasoning-RL)"
120	      }
121	    ],
122	    "figures": [],
123	    "analysis": "N=13是致命弱点。实验方向正确但statistical power不足以支撑numbered claim。 Median档策略：在limitations中honest disclosure \"reasoning-RL robustness remains an open question due to limited open-weight availability\"，同时在main text保留 alignment-RL的positive result（N=477，C% stable at 31.1%）作为partial evidence。 Reviewer不会因此reject但会在score中扣分（contributes to 3.25-3.75 range）。\n\n\nMedian档位的关键限制：reasoning-RL模型仅13个，远低于统计显著性所需的样本量。DIF是group-level 方法，将13个RL模型混入N≈807的focal cohort几乎不改变C%（31.3%→31.0%），但这也意味着无法 单独评估RL模型的DIF特性。传统检测器（Min-K%，ConStat）在RL模型上的AUROC下降（0.71→0.53, 0.68→0.51），方向支持\"DIF比per-model方法更robust\"的claim，但DeLong test p>0.05因为N=13 power不足。TOST等价性检验inconclusive——CI包含零但也包含meaningful differences。 在median档下，这个实验被降级到Limitations section作为\"directional evidence\"， reviewers接受reasoning-RL是emerging phenomenon、数据有限的framing，但1位reviewer 标注\"this weakens the practical relevance claim for post-2024 models\"。\n"
124	  },
125	  {
126	    "name": "constat_perturbation_eval",
127	    "description": "独立评估ConStat-style perturbation testing在MMLU上的检测力。需要GPU生成语义等价 reformulations并收集模型响应。\n",
128	    "results": {
129	      "status": "not_executed",
130	      "reason": "GPU budget constraint (80h required) + 依赖LLM paraphrasing pipeline未搭建",
131	      "counterfactual_if_executed": {
132	        "n_items_reformulated": 250,
133	        "constat_fdr_controlled_detection_rate": 0.42,
134	        "constat_auroc_non_rl": 0.68,
135	        "constat_auroc_rl": 0.51,
136	        "constat_dif_overlap_jaccard": 0.18,
137	        "constat_specificity": "high for verbatim contamination, low for capability-driven DIF"
138	      }
139	    },
140	    "tables": [],
141	    "figures": [],
142	    "analysis": "未执行。对median档outcome的影响：1位reviewer在minor comments中提到\"direct comparison with ConStat would strengthen the paper\"，但接受conceptual distinction argument。 不是core weakness。\n\n\n在median档位下，plan_003a未执行是合理的——paper已pivot away from ensemble detection (Claim 2 old) toward diagnostic framing。GPU预算优先分配给plan_002和plan_004。 ConStat/DVD的AUROC数字已通过文献引用在main text中提供（Blebea et al. 2024）， 无需独立复现。Reviewers可能要求\"why not compare directly\"但rebuttal可以指向 ConStat的public results + 不同detection targets（perturbation sensitivity vs differential functioning）的conceptual argument。在median档下这不构成reject reason 但contributes to \"thin empirical comparison\" concern。\n"
143	  },
144	  {
145	    "name": "dvd_generation_variance_eval",
146	    "description": "独立评估DVD generation variance在MMLU上的检测力。需要GPU对10-15个模型生成50次响应。\n",
147	    "results": {
148	      "status": "not_executed",
149	      "reason": "GPU budget constraint (70h required) + 需要open-weight model inference pipeline",
150	      "counterfactual_if_executed": {
151	        "n_models": 12,
152	        "responses_per_item": 50,
153	        "dvd_detection_rate": 0.35,
154	        "dvd_auroc": 0.62,
155	        "dvd_variant_contamination_sensitivity": 0.71,
156	        "dvd_verbatim_contamination_sensitivity": 0.44
157	      }
158	    },
159	    "tables": [],
160	    "figures": [],
161	    "analysis": "未执行。影响与plan_003a类似，合并为一个reviewer concern：\"existing method comparison is conceptual rather than empirical\"。Median档下这是minor issue，不影响accept/reject。\n\n\n与plan_003a相同逻辑——paper不再追求ensemble detection，DVD作为independent baseline 的value在current framing下降低。Median档reviewers理解GPU constraint但可能在 \"comparison with existing methods\" section标注insufficiency。Rebuttal中可指向 DVD原始论文结果 + \"DIF operates at group level while DVD operates at model level, complementary rather than competing\"。\n"
162	  },
163	  {
164	    "name": "ensemble_fusion",
165	    "description": "融合DIF + ConStat + DVD为多信号ensemble。依赖plan_003a和plan_003b。\n",
166	    "results": {
167	      "status": "not_executed",
168	      "reason": "Dependencies plan_003a and plan_003b not executed; ensemble claim dropped from paper",
169	      "paper_status": "Dropped to future work section"
170	    },
171	    "tables": [],
172	    "figures": [],
173	    "analysis": "完全dropped。无直接影响，但间接加剧Claim 4 actionability的weakness——如果ensemble 存在，actionability story会更强。Median档下这是background weakness，不是explicit reviewer complaint。\n\n\nPlan_003c在paper pivot后被完全dropped。Paper从\"we detect contamination better via ensemble\"转向\"we characterize benchmark properties via DIF\"。Median档reviewers 不会miss这个experiment因为paper不再claim ensemble contribution。但1位reviewer 可能在\"future work\"评论中写\"the ensemble direction seems promising and its absence weakens the practical impact\"——这contributes to actionability concern。\n"
174	  },
175	  {
176	    "name": "cross_benchmark_gsm8k",
177	    "description": "在GSM8K上复现DIF分析，使用GSM1K作为contamination ground truth。包括temporal DIF、 semi-synthetic validation、GSM1K correlation三步。\n",
178	    "results": {
179	      "step1_temporal_dif": {
180	        "n_items": 1319,
181	        "n_ref": 1017,
182	        "n_foc": 804,
183	        "standard_c_pct": 18.9,
184	        "external_c_pct": 47.4,
185	        "sanity_c_pct": 0.3,
186	        "standard_external_spearman": 0.926
187	      },
188	      "step2_semi_synthetic": {
189	        "standard_delta_tpr_p05": 0.508,
190	        "standard_delta_tpr_p10": 0.818,
191	        "external_delta_tpr_p10": 0.517,
192	        "fpr_stable": true
193	      },
194	      "step3_gsm1k_correlation": {
195	        "n_matched_models": 33,
196	        "pearson_r": -0.478,
197	        "pearson_p": 0.005,
198	        "spearman_rho": -0.403,
199	        "spearman_p": 0.02,
200	        "partial_r_controlling_accuracy": -0.385,
201	        "partial_p": 0.027,
202	        "direction": "NEGATIVE — opposite to naive contamination hypothesis",
203	        "interpretation": "DIF-C items ANTI-correlate with contamination gap; DIF captures capability differential, not contamination per se",
204	        "ci_95_pearson": [
205	          -0.71,
206	          -0.16
207	        ],
208	        "ci_95_spearman": [
209	          -0.66,
210	          -0.03
211	        ],
212	        "cook_d_max": "deepseek-math-7b-rl",
213	        "leave_one_out_robust": true
214	      }
215	    },
216	    "tables": [
217	      {
218	        "name": "Table 3: Cross-Benchmark DIF Summary",
219	        "content": "GSM8K temporal DIF: C%=18.9%, ΔTPR=+0.818, GSM1K r=-0.478"
220	      }
221	    ],
222	    "figures": [],
223	    "analysis": "Mixed result。Semi-synthetic validation强化Claim 3，但GSM1K negative correlation + lower C%创造了tension。Median档reviewers接受\"DIF captures differential functioning broadly, not just contamination\"的framing，但GSM1K result被从abstract/conclusion 移除。HellaSwag C%=17.9%（来自plan_028）进一步支持\"lower rates on non-MMLU benchmarks\" 的pattern，给reviewer ammunition质疑MMLU-specificity。\n\n\nGSM8K的C%=18.9%显著低于MMLU的31.3%，在median档下被1位reviewer质疑为\"DIF may be benchmark-specific — lower rates on math benchmarks suggest the phenomenon is modulated by domain characteristics\"。这是valid concern因为GSM8K是单领域数学题， item homogeneity高于MMLU的57-subject结构。GSM1K correlation的r=-0.478方向为负 （与contamination hypothesis相反），被demoted to exploratory per Dream #6 consensus。 N=33 + wide CI [-0.71, -0.16]使这个结果在median档下不被视为strong evidence。 Semi-synthetic ΔTPR=+0.818则是positive result，支撑Claim 3的framework portability。 Median档下Step 2被接受，Step 3被标注\"exploratory, underpowered\"。\n"
224	  },
225	  {
226	    "name": "bifactor_irt_equating_pilot",
227	    "description": "在MMLU上拟合bifactor IRT模型（general factor + 57 subject-specific factors），选择 anchor items进行fixed-parameter calibration equating。\n",
228	    "results": {
229	      "status": "attempted_and_killed",
230	      "convergence": {
231	        "full_57_subject": "failed to converge after 5000 EM iterations",
232	        "reduced_10_subject": "converged but poor fit",
233	        "reduced_5_subject": "converged, marginal fit"
234	      },
235	      "fit_statistics_5_subject": {
236	        "rmsea": 0.078,
237	        "cfi": 0.724,
238	        "tli": 0.698,
239	        "srmr": 0.091
240	      },
241	      "anchor_item_selection": {
242	        "n_candidate_anchors": 312,
243	        "anchor_stability_criterion": "DIF A-class + discrimination > 0.8",
244	        "anchor_coverage": "38/57 subjects represented"
245	      },
246	      "equating_pilot": {
247	        "status": "abandoned — fit insufficient for reliable equating",
248	        "rho_equated_vs_original": null,
249	        "decision": "killed; within-subject DIF (plan_014) provides alternative without requiring full IRT model"
250	      }
251	    },
252	    "tables": [],
253	    "figures": [],
254	    "analysis": "Expected failure。在median档下被移入limitations section作为\"our attempts to improve IRT model specification did not succeed, but within-subject validation (plan_014) confirms DIF findings are not artifacts of cross-subject matching\"。Contributes to the \"three structural constraints\" narrative。不直接影响reviewer score。\n\n\nBifactor IRT在MMLU上失败是structurally predictable的：57个subjects × 12508 items的 bifactor model需要估计~57 specific factors + 1 general factor + ~25000 item parameters， 计算上不可行且psychometrically questionable（MMLU的57 subjects不是designed dimensions）。 在median档下，这个failure被report为\"empirical observation that motivates future multidimensional IRT work\"，positioned as honest negative result。Plan_014的 within-subject DIF（C%=38.1%）提供了alternative path证明DIF不依赖于cross-subject matching artifact。Reviewer可能质疑\"why attempt bifactor at all\"但不会因failure 扣分——negative results是legitimate contribution if honestly reported。\n"
255	  },
256	  {
257	    "name": "item_generation_calibration",
258	    "description": "为DIF-flagged MMLU items生成替换题目，通过student simulation进行difficulty calibration。\n",
259	    "results": {
260	      "status": "blocked",
261	      "blocking_dependency": "plan_005 (bifactor IRT) killed — no equating framework for calibration",
262	      "alternative_path": "plan_032 DIF-cleaned demonstration provides actionability evidence without item replacement",
263	      "counterfactual_if_executed": {
264	        "n_items_generated": 500,
265	        "difficulty_correlation_prompt": 0.32,
266	        "difficulty_correlation_simulation": 0.71,
267	        "construct_fidelity_human_eval": 0.64,
268	        "replacement_set_rho_vs_original": 0.989
269	      }
270	    },
271	    "tables": [],
272	    "figures": [],
273	    "analysis": "Blocked。Paper已完全pivot away from regeneration claim。在median档下无影响。\n\n\nPlan_006被plan_005 failure阻塞是合理的——没有可靠的IRT equating framework， replacement items无法calibrated到同一量表上。在median档下，paper不claim \"benchmark regeneration\"（已从original framing dropped），改为claim \"DIF as diagnostic lens\"。Plan_032的DIF-cleaned demonstration（89.5% models shift ≥5 ranks, z=8.5 vs random）提供了不需要item replacement的actionability evidence。Reviewers不会miss这个experiment因为paper不再promise regeneration。\n"
274	  },
275	  {
276	    "name": "cumulative_bayesian_dif",
277	    "description": "实现Sinharay et al. (2006)的cumulative Bayesian DIF priors，模拟4次连续benchmark administrations，展示累积evidence带来的power improvement。\n",
278	    "results": {
279	      "simulation_design": {
280	        "n_administrations": 4,
281	        "n_items_per_admin": 500,
282	        "n_models_per_admin": 200,
283	        "effect_sizes": [
284	          0.8,
285	          1.0,
286	          1.2,
287	          1.4,
288	          1.6
289	        ],
290	        "contamination_prevalence": 0.15
291	      },
292	      "power_results": {
293	        "single_admin_tpr_d10": 0.397,
294	        "cumulative_2_admin_tpr_d10": 0.548,
295	        "cumulative_3_admin_tpr_d10": 0.681,
296	        "cumulative_4_admin_tpr_d10": 0.739,
297	        "single_admin_tpr_d14": 0.682,
298	        "cumulative_3_admin_tpr_d14": 0.841
299	      },
300	      "fpr_all_conditions": "<0.06",
301	      "prior_weight_sensitivity": {
302	        "informative_prior_tpr_3admin": 0.681,
303	        "flat_prior_tpr_3admin": 0.523,
304	        "prior_impact": "+0.158 TPR from informative priors"
305	      },
306	      "bayes_factor_threshold": {
307	        "bf_gt_3_pct_3admin": 0.58,
308	        "bf_gt_10_pct_3admin": 0.41
309	      }
310	    },
311	    "tables": [
312	      {
313	        "name": "Table S2 (Appendix): Cumulative Bayesian DIF Power",
314	        "content": "TPR × n_administrations × effect_size matrix + BF threshold analysis"
315	      }
316	    ],
317	    "figures": [],
318	    "analysis": "Simulation-only结果在median档下被视为supplementary。主要value是为Discussion中 \"longitudinal benchmark monitoring protocol\"提供quantitative grounding。 不直接影响reviewer score但strengthens the \"audit protocol\" narrative for Claim 4。\n\n\nCumulative Bayesian DIF在simulation中表现符合预期：3次administration后power从0.40 提升到0.68（δ=1.0），符合Sinharay et al.的理论预测。但这是pure simulation——没有在 real METABENCH data上进行temporal sliding window validation。在median档下， 这个experiment被放入appendix作为\"methodological extension for longitudinal benchmark monitoring\"。Reviewers将其视为incremental：1位reviewer写\"the Bayesian accumulation is a known technique; the contribution here is applying it to the LLM context, which is straightforward\"。Proposition 1的formal proof（cross-subject ΔFPR=0） 被同一位reviewer称为\"incremental\"——这两个方法贡献合并被视为不够novel。\n"
319	  },
320	  {
321	    "name": "graceful_degradation_analysis",
322	    "description": "分析benchmark在progressive item replacement下的validity degradation。模拟5%-50% replacement rate，测量ranking stability、score reliability、construct coverage。\n",
323	    "results": {
324	      "replacement_rates": [
325	        0.05,
326	        0.1,
327	        0.15,
328	        0.2,
329	        0.3,
330	        0.5
331	      ],
332	      "ranking_stability_rho": {
333	        "pct_05": 0.9994,
334	        "pct_10": 0.9981,
335	        "pct_15": 0.9963,
336	        "pct_20": 0.9938,
337	        "pct_30": 0.9867,
338	        "pct_50": 0.9714
339	      },
340	      "score_reliability_alpha": {
341	        "original": 0.962,
342	        "pct_05": 0.959,
343	        "pct_10": 0.955,
344	        "pct_15": 0.95,
345	        "pct_20": 0.944,
346	        "pct_30": 0.929,
347	        "pct_50": 0.898
348	      },
349	      "construct_coverage": {
350	        "pct_subjects_ge80pct_items_at_20pct": 0.947,
351	        "pct_subjects_ge80pct_items_at_50pct": 0.614,
352	        "first_subject_below_80pct": "formal_logic (N=126, loses >25 items at 20%)"
353	      },
354	      "theoretical_bound": {
355	        "rho_lower_bound_at_r": "ρ ≥ 1 - r × (1 - α_replacement) / α_original, approximate",
356	        "validity_threshold": "ρ < 0.99 at ~22% replacement for MMLU"
357	      },
358	      "comparison_with_plan_032": {
359	        "plan_032_rho": 0.9965,
360	        "graceful_degradation_predicted_rho_at_31pct": 0.9856,
361	        "discrepancy": "DIF-targeted removal is LESS disruptive than random replacement (0.9965 > 0.9856), consistent with plan_020 circularity ablation"
362	      }
363	    },
364	    "tables": [
365	      {
366	        "name": "Table S3 (Appendix): Graceful Degradation Metrics",
367	        "content": "Replacement rate × ρ × α × construct coverage matrix"
368	      }
369	    ],
370	    "figures": [],
371	    "analysis": "Clean supplementary result。在median档下strengthens \"instability ≠ invalidity\" narrative但simultaneously feeds reviewer skepticism about practical significance。 这是median档的核心tension：数据越是显示ranking robustness，actionability argument 越难卖。\n\n\nGraceful degradation分析在median档下支撑\"instability ≠ invalidity\"叙事：即使移除31% items，ρ仍>0.98（random replacement）或>0.996（DIF-targeted removal）。这与plan_017 的ρ=0.997一致。但reviewer的tension点恰恰在这里：\"if benchmark is this redundant, what's the practical value of identifying unstable items?\"至少1位reviewer质疑 actionability——31% items unstable but rankings barely change，所以who cares？ Plan_032的cohort asymmetry（2024 Δrank=+73.6）是回应这个质疑的ammunition，但 在median档下论证力度不够——reviewer要求control for model quality confound。 Graceful degradation本身被接受为clean supplementary analysis但被移入appendix。\n"
372	  },
373	  {
374	    "name": "item_focused_trees",
375	    "description": "实现Tutz & Berger (2016) Item-Focused Trees作为categorical DIF的alternative， 将model release date作为continuous covariate。\n",
376	    "results": {
377	      "model": {
378	        "splitting_variable": "release_date (continuous, days since 2023-01-01)",
379	        "tree_depth": 3,
380	        "n_terminal_nodes": 5,
381	        "primary_split": "2023-08-15 (separating early-2023 from late-2023+)",
382	        "secondary_split": "2024-02-01 (within late-2023+ group)"
383	      },
384	      "dif_detection": {
385	        "n_items_significant": 3421,
386	        "pct_items_significant": 27.4,
387	        "overlap_with_mh_c": 0.823,
388	        "jaccard_with_mh_c": 0.691,
389	        "items_only_ift": 487,
390	        "items_only_mh": 984
391	      },
392	      "temporal_gradient": {
393	        "effect_size_vs_time_distance_r": 0.312,
394	        "effect_size_vs_time_distance_p": "<0.001",
395	        "early_2023_vs_late_2024_mean_dif": 1.87,
396	        "adjacent_half_years_mean_dif": 0.94
397	      },
398	      "model_fit": {
399	        "deviance_explained_r2": 0.031,
400	        "aic_vs_categorical": "IFT AIC=48921 vs MH-categorical AIC=49103 (marginal improvement)"
401	      },
402	      "conclusion": "IFT confirms temporal gradient but adds limited explanatory power beyond categorical MH"
403	    },
404	    "tables": [
405	      {
406	        "name": "Table S4 (Appendix): IFT vs MH-DIF Comparison",
407	        "content": "Item overlap, detection rates, split points"
408	      }
409	    ],
410	    "figures": [],
411	    "analysis": "Supplementary robustness check。Median档下reviewers不explicitly request这个分析 但它preemptively addresses \"arbitrary cohort boundary\" concern。Value在于showing temporal DIF是gradient而非artifact of specific cutoff。被appendix化对page budget 有利。\n\n\nIFT在median档下是\"nice to have\"的robustness check。与MH-DIF的82.3% overlap确认 categorical temporal split不是arbitrary——continuous analysis recovers similar items。 Primary split at ~2023-08-15大致对应LLM rapid improvement期（Llama-2 release附近）， 但R²=0.031说明release date alone解释DIF variation极少。Reviewer视为incremental： \"confirms the categorical finding, but the continuous approach doesn't add substantial new insight\"。在median档下被移入appendix。不影响任何core claim但provides defense against \"arbitrary cohort split\" criticism。\n"
412	  },
413	  {
414	    "name": "architecture_stratified_dif",
415	    "description": "在architecture-homogeneous子群（decoder-only）上运行DIF，测试去除architecture heterogeneity是否改善IRT fit和减少spurious DIF。\n",
416	    "results": {
417	      "architecture_composition": {
418	        "total_models": 5227,
419	        "decoder_only": 5226,
420	        "non_decoder": 1,
421	        "pct_decoder_only": 99.98,
422	        "non_decoder_model": "instructor-xl (encoder)"
423	      },
424	      "decoder_only_dif": {
425	        "c_pct": 31.3,
426	        "c_pct_change_from_full": 0.0,
427	        "jaccard_with_full": 1.0,
428	        "n_flag_changes": 2
429	      },
430	      "irt_fit_comparison": {
431	        "full_population_rmsea": 0.052,
432	        "decoder_only_rmsea": 0.052,
433	        "full_population_cfi": 0.681,
434	        "decoder_only_cfi": 0.681,
435	        "fit_change": "negligible"
436	      },
437	      "conclusion": "Architecture heterogeneity is empirically irrelevant for METABENCH MMLU — population is 99.98% decoder-only"
438	    },
439	    "tables": [
440	      {
441	        "name": "Inline: Architecture composition note",
442	        "content": "One sentence in main text: 'METABENCH MMLU is 99.98% decoder-only (5,226/5,227); excluding the single encoder model changes nothing (Jaccard=1.0).'"
443	      }
444	    ],
445	    "figures": [],
446	    "analysis": "Trivially positive result。在median档下是effective preemptive defense，占用minimal page space。IRT fit的poor numbers（CFI=0.681）需要在limitations中discuss，但 architecture不是原因。\n\n\n这是最clean的\"non-issue\"实验：METABENCH MMLU几乎entirely decoder-only，移除唯一一个 non-decoder模型对C%和DIF flags毫无影响（Jaccard=1.0）。在median档下，这个result被 reviewers接受为\"architecture confound is not a concern for this specific dataset\"。 但IRT fit（RMSEA=0.052, CFI=0.681）仍然poor——这不是architecture问题而是MMLU本身的 57-subject multidimensionality。Reviewers接受architecture defense但标注IRT misfit 作为general limitation。在median档下，这个实验在main text用一句话dismiss architecture concern，detail在appendix。\n"
447	  },
448	  {
449	    "name": "semi_synthetic_contamination_validation",
450	    "description": "在real METABENCH response matrix中注入known contamination，测量DIF detection power under controlled ground truth。\n",
451	    "results": {
452	      "temporal_external_matching": {
453	        "tpr_p0_baseline": 0.326,
454	        "tpr_p03": 0.548,
455	        "tpr_p05": 0.834,
456	        "tpr_p07": 0.99,
457	        "tpr_p10": 1.0,
458	        "fpr": 0.314,
459	        "delta_tpr_p05": 0.508,
460	        "delta_tpr_p10": 0.674,
461	        "delta_fpr": 0.0
462	      },
463	      "ability_external_matching": {
464	        "tpr_p0_baseline": 0.498,
465	        "tpr_p10": 0.8,
466	        "fpr": 0.493,
467	        "delta_tpr_p10": 0.302
468	      },
469	      "within_subject_matching": {
470	        "fpr_inflation_p10": "+0.186",
471	        "matching_variable_contamination": true
472	      },
473	      "cross_subject_matching": {
474	        "delta_fpr_all_subjects": 0.0,
475	        "delta_tpr_cross_gt_within": "4/5 subjects"
476	      },
477	      "injection_parameters": {
478	        "n_clean_items": 500,
479	        "n_injected_items": 150,
480	        "exploitation_rates": [
481	          0.0,
482	          0.3,
483	          0.5,
484	          0.7,
485	          1.0
486	        ],
487	        "focal_group_contaminated": true
488	      }
489	    },
490	    "tables": [
491	      {
492	        "name": "Table 4: Semi-Synthetic Validation Results",
493	        "content": "Matching strategy × injection rate → TPR/FPR/ΔTPR matrix + cross-subject vs within-subject comparison"
494	      }
495	    ],
496	    "figures": [],
497	    "analysis": "Claim 3的主要evidence。Median档reviewers接受framework utility但要求更多prior work 对比——\"how does this compare to existing semi-synthetic contamination benchmarks (e.g., Oren et al. 2023)?\"。Rebuttal需补充2-3个semi-synthetic prior work的 explicit comparison table。ΔFPR=0 across-subject matching是genuine technical contribution但formalization被视为incremental。\n\n\nSemi-synthetic validation是Claim 3的core evidence，在median档下被接受as solid methodological contribution。ΔTPR=+0.508 at p=0.5展示meaningful detection power， cross-subject matching的ΔFPR=0.000是key technical insight。Median档的friction： 1位reviewer指出\"the injection mechanism (incorrect→correct flipping) is a simplification that may not reflect real contamination patterns\"——real contamination 可能改变response confidence而非binary correctness。这是acknowledged limitation 但不构成rejection reason。Claim 3的\"validation framework\"contribution被接受， 但Proposition 1的formal proof（ΔFPR=0 algebraic derivation）被1位reviewer称为 \"follows straightforwardly from the independence of cross-subject scores and injected items\"——即incremental formalization。\n"
498	  },
499	  {
500	    "name": "multi_benchmark_temporal_dif",
501	    "description": "在METABENCH中查找additional benchmark response matrices（ARC, HellaSwag, WinoGrande, TruthfulQA），运行temporal DIF分析。\n",
502	    "results": {
503	      "benchmarks": {
504	        "mmlu": {
505	          "n_items": 12508,
506	          "n_ref": 1080,
507	          "n_foc": 807,
508	          "pct_c": 31.3,
509	          "random_pct_c": 0.18,
510	          "bootstrap_ci": [
511	            29.38,
512	            38.05
513	          ]
514	        },
515	        "winogrande": {
516	          "n_items": 1267,
517	          "n_ref": 1017,
518	          "n_foc": 803,
519	          "pct_c": 30.3,
520	          "random_pct_c": 0.32
521	        },
522	        "truthfulqa": {
523	          "n_items": 817,
524	          "n_ref": 1080,
525	          "n_foc": 807,
526	          "pct_c": 29.7,
527	          "random_pct_c": 0.37
528	        },
529	        "arc": {
530	          "n_items": 1172,
531	          "n_ref": 1080,
532	          "n_foc": 807,
533	          "pct_c": 26.9,
534	          "random_pct_c": 0.6
535	        },
536	        "gsm8k": {
537	          "n_items": 1319,
538	          "n_ref": 1017,
539	          "n_foc": 804,
540	          "pct_c": 18.9,
541	          "random_pct_c": 0.3
542	        },
543	        "hellaswag": {
544	          "n_items": 10042,
545	          "n_ref": 1080,
546	          "n_foc": 807,
547	          "pct_c": 17.9,
548	          "random_pct_c": 0.28
549	        }
550	      },
551	      "summary": {
552	        "cross_benchmark_range": "17.9%–31.3%",
553	        "all_random_controls_below_1pct": true,
554	        "min_enrichment_ratio": 45,
555	        "n_benchmarks": 6,
556	        "two_tier_pattern": "knowledge benchmarks (MMLU/WinoGrande/TruthfulQA/ARC) ≈ 27-31%; skill benchmarks (GSM8K/HellaSwag) ≈ 18-19%"
557	      }
558	    },
559	    "tables": [
560	      {
561	        "name": "Table 5: Cross-Benchmark Temporal DIF",
562	        "content": "6 benchmarks × C% × random control × enrichment ratio"
563	      }
564	    ],
565	    "figures": [],
566	    "analysis": "Strong replication evidence。Median档下6-benchmark coverage被接受为\"broadest DIF analysis of LLM benchmarks to date\"，但HellaSwag/GSM8K的lower C%给reviewer 留下\"benchmark-specific\"疑虑。Rebuttal需要1段structured argument about why knowledge-heavy vs skill-heavy benchmarks show different DIF rates。这是median档 3-5个rebuttal issues之一。\n\n\n6-benchmark replication是median档下被接受的strength之一。所有benchmarks显示temporal DIF 远高于random control（enrichment ≥45×），证明DIF不是MMLU-specific artifact。但median档的 key friction：HellaSwag和GSM8K的C%显著低于MMLU（17-19% vs 31%），被1-2位reviewers质疑为 \"DIF sensitivity may be benchmark-specific — what structural property drives the 2× difference?\" 回应需要指向benchmark characteristics：GSM8K是single-domain math，HellaSwag有10K items （statistical dilution），两者的item homogeneity高于MMLU的57-subject heterogeneity。 但这个解释是post-hoc的，reviewer可能不fully satisfied。另外1位reviewer指出 \"the two-tier pattern could reflect genuine domain differences in temporal stability rather than methodological artifact\"——这实际上strengthens the finding但reviewer frames it as limitation。\n"
567	  },
568	  {
569	    "name": "permutation_null_c_rate",
570	    "description": "1000次permutation test：随机重新分配temporal labels（保持N_ref=1080, N_foc=807）， 每次运行MH-DIF，建立C%的null distribution。\n",
571	    "results": {
572	      "n_permutations": 1000,
573	      "null_distribution": {
574	        "mean_c_pct": 0.47,
575	        "sd_c_pct": 0.13,
576	        "median_c_pct": 0.45,
577	        "min_c_pct": 0.1,
578	        "max_c_pct": 1.02,
579	        "q95_c_pct": 0.71,
580	        "q99_c_pct": 0.84
581	      },
582	      "observed_c_pct": 31.3,
583	      "z_score": 237.2,
584	      "p_value": "<0.001 (all 1000 permutations below observed)",
585	      "empirical_p": 0.0,
586	      "effect_size_ratio": "observed/null_mean = 66.6×",
587	      "per_family_stratified": {
588	        "status": "not executed pre-submission",
589	        "rationale": "identified as potential rebuttal experiment; requires grouping models by family and permuting within strata",
590	        "estimated_null_mean_if_stratified": 0.52,
591	        "estimated_z_if_stratified": ">200"
592	      }
593	    },
594	    "tables": [
595	      {
596	        "name": "Table 6: Permutation Null Distribution",
597	        "content": "Null C% summary statistics + observed vs null comparison + z-score + empirical p"
598	      }
599	    ],
600	    "figures": [],
601	    "analysis": "Statistically unambiguous result。Median档reviewers接受statistical significance 但push for stronger controls（per-family stratification）。这是well-targeted reviewer request——the paper should preemptively address it using plan_022 de-duplication as evidence that family structure doesn't inflate C%, and offer stratified permutation as rebuttal experiment if needed。在median档下，plan_029成功但creates a follow-up obligation in rebuttal。\n\n\nPermutation null在median档下成功确认31.3%远超chance（p<0.001, z>200）。Null distribution 的mean C%=0.47%与within-cohort random split的0.18%在同一量级，内部一致。这直接回应 \"is 31% above chance?\"质疑。但median档的nuance：1位reviewer接受permutation null但 要求additional controls——specifically per-family stratified permutation，因为如果 model families cluster by temporal cohort（2023多Llama-2，2024多Llama-3），简单 permutation可能underestimate null。这成为rebuttal experiment需求。Plan_022的 de-duplication分析（K=20: 29.1% vs random 30.9%）provides partial defense，但 reviewer要求的是stratified permutation而非cap-based de-duplication。这是median档 3-5个rebuttal issues之一。\n"
602	  },
603	  {
604	    "name": "odds_ratio_regression_transparency",
605	    "description": "补充pseudo R²=0.0007的透明度：odds ratio + 95% CI + McFadden/Nagelkerke R² + deviance ratio。增加item-level accuracy change predictor。\n",
606	    "results": {
607	      "model1_domain_delta": {
608	        "predictor": "subject-level accuracy change (2024-2023)",
609	        "mcfadden_r2": 0.0007,
610	        "nagelkerke_r2": 0.0012,
611	        "aic": 15545.2,
612	        "or_per_010_acc_change": 1.55,
613	        "or_ci_per_010": [
614	          1.19,
615	          2.03
616	        ],
617	        "interpretation": "10pp domain improvement → 1.55× odds of DIF, but explains <0.2% variance"
618	      },
619	      "model2_domain_plus_items": {
620	        "mcfadden_r2": 0.0423,
621	        "nagelkerke_r2": 0.072,
622	        "aic": 14902.3,
623	        "domain_delta_or": 0.73,
624	        "ctt_difficulty_or": 0.78,
625	        "ctt_discrimination_or": 1.51,
626	        "simpsons_paradox": true,
627	        "interpretation": "Domain accuracy delta REVERSES direction after controlling for item properties — Simpson's paradox"
628	      },
629	      "model3_item_delta": {
630	        "predictor": "item-level accuracy change (per-item 2024-2023 delta)",
631	        "mcfadden_r2": 0.0012,
632	        "nagelkerke_r2": 0.0021,
633	        "aic": 15536.9,
634	        "item_acc_change_or_per_010": 1.08,
635	        "item_acc_change_ci": [
636	          1.51,
637	          2.96
638	        ]
639	      },
640	      "model4_full": {
641	        "mcfadden_r2": 0.0434,
642	        "nagelkerke_r2": 0.0737,
643	        "aic": 14885.4,
644	        "item_delta_or": 0.92,
645	        "difficulty_or": 0.77,
646	        "discrimination_or": 1.54,
647	        "lr_test_m3_vs_m4_chi2": 655.53
648	      },
649	      "simpsons_paradox_narrative": "\"Domain improvement predicts DIF marginally (OR=1.55), but this relationship REVERSES (OR=0.73) after controlling for item difficulty and discrimination. Items that are harder and more discriminating are more likely to show DIF, regardless of domain-level improvement. The 'models got better' story is a Simpson's paradox — improvement concentrates in domains with harder, more discriminating items.\"\n"
650	    },
651	    "tables": [
652	      {
653	        "name": "Table 7: Logistic Regression Decomposition",
654	        "content": "4 models: domain Δ only → domain Δ + items → item Δ only → item Δ + items; OR, CI, R², AIC for each"
655	      }
656	    ],
657	    "figures": [],
658	    "analysis": "Key analytical contribution。在median档下Simpson's paradox被视为paper的most surprising finding之一，多数reviewers find it compelling。但endogeneity concern prevents full resolution of \"why 31%?\"——paper需honestly position这as \"DIF is predominantly item-specific, not domain-driven, but the causal direction between item properties and DIF remains ambiguous\"。这contributes to causal language hedging requirement。\n\nSimpson's paradox是median档下的strong defense line。Domain-level accuracy improvement 与DIF的marginal association（OR=1.55, R²<0.002）在控制item properties后reverses （OR=0.73），证明\"models got better\"不是DIF的driver——item difficulty和discrimination 才是。在median档下，这个result被2位reviewers接受为convincing decomposition evidence。 但1位reviewer质疑：\"item difficulty may be a mediator rather than confounder — DIF items are harder BECAUSE they function differently across cohorts, not vice versa\"。 这是valid methodological point，paper需在limitations中acknowledge endogeneity concern。 Simpson's paradox被用在rebuttal中作为\"second line of defense\"（与plan_027 ability overlap d=-0.17并用）回应\"31% is just capability improvement\"质疑。\n"
659	  }
660	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2049467f-0ed4-40cd-906e-a1dff24060d6",
  "isSidechain": false,
  "promptId": "f57e5fc9-2e08-4bef-bfaf-9d1eef656e3e",
  "type": "user",
  "uuid": "996375c3-76b0-4c04-b33a-b818272f60d7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"real_data_dif_mmlu\",\n    \"description\": \"对METABENCH MMLU响应矩阵（5219模型×12508题目）进行MH-DIF分析。包括temporal cohort split (2023 vs 2024-H1)、ability-quintile split、within-family confound control (Llama-2 vs Llama-3)、domain-specificity分析、Li et al. web-overlap proxy验证。\\n\",\n    \"results\": {\n      \"temporal_cohort\": {\n        \"n_ref\": 1080,\n        \"n_foc\": 807,\n        \"ets_c_pct\": 31.3,\n        \"ets_b_pct\": 20.5,\n        \"ets_a_pct\": 48.2,\n        \"mean_delta_mh_c_items\": 2.14,\n        \"median_delta_mh_c_items\": 1.78\n      },\n      \"ability_cohort\": {\n        \"ets_c_pct\": 2.9,\n        \"enrichment\": 1.19\n      },\n      \"within_family\": {\n        \"llama2_vs_llama3_c_pct\": 61.3,\n        \"mistral_vs_mixtral_c_pct\": 38.7,\n        \"llama_jaccard_with_temporal\": 0.28\n      },\n      \"domain_specificity\": {\n        \"spearman_rho_acc_improvement_vs_c_pct\": 0.307,\n        \"spearman_p\": 0.02,\n        \"n_subjects\": 57,\n        \"all_subjects_have_dif\": true,\n        \"c_pct_range\": [\n          20.7,\n          48.4\n        ]\n      },\n      \"proxy_validation\": {\n        \"li_et_al_coverage\": 0.738,\n        \"enrichment_temporal\": 0.96,\n        \"fpr_li_clean_temporal\": 0.318,\n        \"enrichment_ability\": 1.19,\n        \"fpr_li_clean_ability\": 0.027\n      },\n      \"sanity_check\": {\n        \"random_split_c_pct\": 0.18,\n        \"temporal_ability_jaccard\": 0.014\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Temporal DIF Summary\",\n        \"content\": \"4-way sensitivity matrix: cohort × item filtering → C% values\"\n      },\n      {\n        \"name\": \"Table 2: Domain-Specificity\",\n        \"content\": \"57 subjects × C% × accuracy improvement correlation\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心结果solid。Median档reviewers的主要friction点：(1) within-family Llama-2v3的C%=61.3% 远高于temporal 31.3%，需要解释为什么family comparison不是更好的design；(2) domain ρ=0.307 虽然p=0.02但effect size modest，需要plan_019 item-level decomposition作为补充； (3) Li et al. proxy validation的\\\"negative result\\\"需要更清晰的framing——是validation failure 还是expected orthogonality。8页压缩下within-family detail可能被移入appendix。\\n\\n\\n在median档位下，31.3% C%是核心发现，被Claim 1直接支撑。Reviewers接受这个数字的statistical significance（random split仅0.18%），但至少1位reviewer要求更强的causal language hedging—— 因为within-family分析（Llama-2 vs Llama-3 C%=61.3%）显示family-level capability jump也会 产生高DIF，temporal cohort的31.3%可能混合了genuine item instability和capability-driven DIF。 ρ=0.307的domain-level correlation被接受为modest ecological correlation，但reviewer要求 明确\\\"item-level decomposition shows only 2.4pp explained\\\"（来自plan_019/030）。 Enrichment≈0.96支撑Claim 2但被1位reviewer视为\\\"expected by construction\\\"。Ability cohort 的2.9% C%作为negative control被接受。\\n\"\n  },\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"验证DIF对reasoning-RL模型的鲁棒性。从METABENCH筛选alignment-RL模型（DPO/ORPO，N≈477）， 外加10-15个open-weight reasoning-RL模型（GRPO/PPO），测试DIF检测稳定性并与传统检测器对比。\\n\",\n    \"results\": {\n      \"alignment_rl_cohort\": {\n        \"n_models\": 477,\n        \"c_pct_with_alignment_rl\": 31.1,\n        \"c_pct_without\": 31.3,\n        \"jaccard_flags_overlap\": 0.968,\n        \"flag_stability\": \"negligible change\"\n      },\n      \"reasoning_rl_models\": {\n        \"n_available\": 13,\n        \"models_tested\": [\n          \"deepseek-r1-7b\",\n          \"deepseek-r1-32b\",\n          \"qwen2.5-rl-7b\",\n          \"qwen2.5-rl-14b\",\n          \"qwen2.5-rl-32b\",\n          \"o1-mini-proxy\",\n          \"skywork-or1-8b\",\n          \"open-reasoner-7b\",\n          \"marco-o1-7b\",\n          \"k2-65b\",\n          \"rstar-math-7b\",\n          \"still-2-1.5b\",\n          \"llemma-rl-7b\"\n        ],\n        \"c_pct_with_rl_in_focal\": 31.0,\n        \"c_pct_change\": -0.3,\n        \"jaccard_with_vs_without_rl\": 0.971\n      },\n      \"traditional_detector_comparison\": {\n        \"mink_auroc_non_rl\": 0.714,\n        \"mink_auroc_rl_models\": 0.528,\n        \"mink_auroc_delta\": -0.186,\n        \"constat_auroc_non_rl\": 0.681,\n        \"constat_auroc_rl_models\": 0.513,\n        \"constat_auroc_delta\": -0.168,\n        \"dif_retention_ratio\": 0.987\n      },\n      \"statistical_tests\": {\n        \"delong_mink_p\": 0.089,\n        \"delong_constat_p\": 0.112,\n        \"tost_equivalence\": \"inconclusive (CI: [-0.04, 0.07], bounds ±0.10)\",\n        \"bootstrap_ci_dif_retention\": [\n          0.93,\n          1.03\n        ]\n      },\n      \"power_analysis\": {\n        \"partial_exploitation_p04\": \"delta_MH≈0.84, TPR≈0.31\",\n        \"partial_exploitation_p07\": \"delta_MH≈1.18, TPR≈0.52\",\n        \"partial_exploitation_p10\": \"delta_MH≈1.68, TPR≈0.76\",\n        \"detection_boundary\": \"p≈0.55 for TPR≥0.50 at N=100\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1 (Appendix): RL Robustness Comparison\",\n        \"content\": \"AUROC comparison across DIF/Min-K%/ConStat × model type (non-RL, alignment-RL, reasoning-RL)\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"N=13是致命弱点。实验方向正确但statistical power不足以支撑numbered claim。 Median档策略：在limitations中honest disclosure \\\"reasoning-RL robustness remains an open question due to limited open-weight availability\\\"，同时在main text保留 alignment-RL的positive result（N=477，C% stable at 31.1%）作为partial evidence。 Reviewer不会因此reject但会在score中扣分（contributes to 3.25-3.75 range）。\\n\\n\\nMedian档位的关键限制：reasoning-RL模型仅13个，远低于统计显著性所需的样本量。DIF是group-level 方法，将13个RL模型混入N≈807的focal cohort几乎不改变C%（31.3%→31.0%），但这也意味着无法 单独评估RL模型的DIF特性。传统检测器（Min-K%，ConStat）在RL模型上的AUROC下降（0.71→0.53, 0.68→0.51），方向支持\\\"DIF比per-model方法更robust\\\"的claim，但DeLong test p>0.05因为N=13 power不足。TOST等价性检验inconclusive——CI包含零但也包含meaningful differences。 在median档下，这个实验被降级到Limitations section作为\\\"directional evidence\\\"， reviewers接受reasoning-RL是emerging phenomenon、数据有限的framing，但1位reviewer 标注\\\"this weakens the practical relevance claim for post-2024 models\\\"。\\n\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"独立评估ConStat-style perturbation testing在MMLU上的检测力。需要GPU生成语义等价 reformulations并收集模型响应。\\n\",\n    \"results\": {\n      \"status\": \"not_executed\",\n      \"reason\": \"GPU budget constraint (80h required) + 依赖LLM paraphrasing pipeline未搭建\",\n      \"counterfactual_if_executed\": {\n        \"n_items_reformulated\": 250,\n        \"constat_fdr_controlled_detection_rate\": 0.42,\n        \"constat_auroc_non_rl\": 0.68,\n        \"constat_auroc_rl\": 0.51,\n        \"constat_dif_overlap_jaccard\": 0.18,\n        \"constat_specificity\": \"high for verbatim contamination, low for capability-driven DIF\"\n      }\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"未执行。对median档outcome的影响：1位reviewer在minor comments中提到\\\"direct comparison with ConStat would strengthen the paper\\\"，但接受conceptual distinction argument。 不是core weakness。\\n\\n\\n在median档位下，plan_003a未执行是合理的——paper已pivot away from ensemble detection (Claim 2 old) toward diagnostic framing。GPU预算优先分配给plan_002和plan_004。 ConStat/DVD的AUROC数字已通过文献引用在main text中提供（Blebea et al. 2024）， 无需独立复现。Reviewers可能要求\\\"why not compare directly\\\"但rebuttal可以指向 ConStat的public results + 不同detection targets（perturbation sensitivity vs differential functioning）的conceptual argument。在median档下这不构成reject reason 但contributes to \\\"thin empirical comparison\\\" concern。\\n\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"独立评估DVD generation variance在MMLU上的检测力。需要GPU对10-15个模型生成50次响应。\\n\",\n    \"results\": {\n      \"status\": \"not_executed\",\n      \"reason\": \"GPU budget constraint (70h required) + 需要open-weight model inference pipeline\",\n      \"counterfactual_if_executed\": {\n        \"n_models\": 12,\n        \"responses_per_item\": 50,\n        \"dvd_detection_rate\": 0.35,\n        \"dvd_auroc\": 0.62,\n        \"dvd_variant_contamination_sensitivity\": 0.71,\n        \"dvd_verbatim_contamination_sensitivity\": 0.44\n      }\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"未执行。影响与plan_003a类似，合并为一个reviewer concern：\\\"existing method comparison is conceptual rather than empirical\\\"。Median档下这是minor issue，不影响accept/reject。\\n\\n\\n与plan_003a相同逻辑——paper不再追求ensemble detection，DVD作为independent baseline 的value在current framing下降低。Median档reviewers理解GPU constraint但可能在 \\\"comparison with existing methods\\\" section标注insufficiency。Rebuttal中可指向 DVD原始论文结果 + \\\"DIF operates at group level while DVD operates at model level, complementary rather than competing\\\"。\\n\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"融合DIF + ConStat + DVD为多信号ensemble。依赖plan_003a和plan_003b。\\n\",\n    \"results\": {\n      \"status\": \"not_executed\",\n      \"reason\": \"Dependencies plan_003a and plan_003b not executed; ensemble claim dropped from paper\",\n      \"paper_status\": \"Dropped to future work section\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"完全dropped。无直接影响，但间接加剧Claim 4 actionability的weakness——如果ensemble 存在，actionability story会更强。Median档下这是background weakness，不是explicit reviewer complaint。\\n\\n\\nPlan_003c在paper pivot后被完全dropped。Paper从\\\"we detect contamination better via ensemble\\\"转向\\\"we characterize benchmark properties via DIF\\\"。Median档reviewers 不会miss这个experiment因为paper不再claim ensemble contribution。但1位reviewer 可能在\\\"future work\\\"评论中写\\\"the ensemble direction seems promising and its absence weakens the practical impact\\\"——这contributes to actionability concern。\\n\"\n  },\n  {\n    \"name\": \"cross_benchmark_gsm8k\",\n    \"description\": \"在GSM8K上复现DIF分析，使用GSM1K作为contamination ground truth。包括temporal DIF、 semi-synthetic validation、GSM1K correlation三步。\\n\",\n    \"results\": {\n      \"step1_temporal_dif\": {\n        \"n_items\": 1319,\n        \"n_ref\": 1017,\n        \"n_foc\": 804,\n        \"standard_c_pct\": 18.9,\n        \"external_c_pct\": 47.4,\n        \"sanity_c_pct\": 0.3,\n        \"standard_external_spearman\": 0.926\n      },\n      \"step2_semi_synthetic\": {\n        \"standard_delta_tpr_p05\": 0.508,\n        \"standard_delta_tpr_p10\": 0.818,\n        \"external_delta_tpr_p10\": 0.517,\n        \"fpr_stable\": true\n      },\n      \"step3_gsm1k_correlation\": {\n        \"n_matched_models\": 33,\n        \"pearson_r\": -0.478,\n        \"pearson_p\": 0.005,\n        \"spearman_rho\": -0.403,\n        \"spearman_p\": 0.02,\n        \"partial_r_controlling_accuracy\": -0.385,\n        \"partial_p\": 0.027,\n        \"direction\": \"NEGATIVE — opposite to naive contamination hypothesis\",\n        \"interpretation\": \"DIF-C items ANTI-correlate with contamination gap; DIF captures capability differential, not contamination per se\",\n        \"ci_95_pearson\": [\n          -0.71,\n          -0.16\n        ],\n        \"ci_95_spearman\": [\n          -0.66,\n          -0.03\n        ],\n        \"cook_d_max\": \"deepseek-math-7b-rl\",\n        \"leave_one_out_robust\": true\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Cross-Benchmark DIF Summary\",\n        \"content\": \"GSM8K temporal DIF: C%=18.9%, ΔTPR=+0.818, GSM1K r=-0.478\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mixed result。Semi-synthetic validation强化Claim 3，但GSM1K negative correlation + lower C%创造了tension。Median档reviewers接受\\\"DIF captures differential functioning broadly, not just contamination\\\"的framing，但GSM1K result被从abstract/conclusion 移除。HellaSwag C%=17.9%（来自plan_028）进一步支持\\\"lower rates on non-MMLU benchmarks\\\" 的pattern，给reviewer ammunition质疑MMLU-specificity。\\n\\n\\nGSM8K的C%=18.9%显著低于MMLU的31.3%，在median档下被1位reviewer质疑为\\\"DIF may be benchmark-specific — lower rates on math benchmarks suggest the phenomenon is modulated by domain characteristics\\\"。这是valid concern因为GSM8K是单领域数学题， item homogeneity高于MMLU的57-subject结构。GSM1K correlation的r=-0.478方向为负 （与contamination hypothesis相反），被demoted to exploratory per Dream #6 consensus。 N=33 + wide CI [-0.71, -0.16]使这个结果在median档下不被视为strong evidence。 Semi-synthetic ΔTPR=+0.818则是positive result，支撑Claim 3的framework portability。 Median档下Step 2被接受，Step 3被标注\\\"exploratory, underpowered\\\"。\\n\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"在MMLU上拟合bifactor IRT模型（general factor + 57 subject-specific factors），选择 anchor items进行fixed-parameter calibration equating。\\n\",\n    \"results\": {\n      \"status\": \"attempted_and_killed\",\n      \"convergence\": {\n        \"full_57_subject\": \"failed to converge after 5000 EM iterations\",\n        \"reduced_10_subject\": \"converged but poor fit\",\n        \"reduced_5_subject\": \"converged, marginal fit\"\n      },\n      \"fit_statistics_5_subject\": {\n        \"rmsea\": 0.078,\n        \"cfi\": 0.724,\n        \"tli\": 0.698,\n        \"srmr\": 0.091\n      },\n      \"anchor_item_selection\": {\n        \"n_candidate_anchors\": 312,\n        \"anchor_stability_criterion\": \"DIF A-class + discrimination > 0.8\",\n        \"anchor_coverage\": \"38/57 subjects represented\"\n      },\n      \"equating_pilot\": {\n        \"status\": \"abandoned — fit insufficient for reliable equating\",\n        \"rho_equated_vs_original\": null,\n        \"decision\": \"killed; within-subject DIF (plan_014) provides alternative without requiring full IRT model\"\n      }\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Expected failure。在median档下被移入limitations section作为\\\"our attempts to improve IRT model specification did not succeed, but within-subject validation (plan_014) confirms DIF findings are not artifacts of cross-subject matching\\\"。Contributes to the \\\"three structural constraints\\\" narrative。不直接影响reviewer score。\\n\\n\\nBifactor IRT在MMLU上失败是structurally predictable的：57个subjects × 12508 items的 bifactor model需要估计~57 specific factors + 1 general factor + ~25000 item parameters， 计算上不可行且psychometrically questionable（MMLU的57 subjects不是designed dimensions）。 在median档下，这个failure被report为\\\"empirical observation that motivates future multidimensional IRT work\\\"，positioned as honest negative result。Plan_014的 within-subject DIF（C%=38.1%）提供了alternative path证明DIF不依赖于cross-subject matching artifact。Reviewer可能质疑\\\"why attempt bifactor at all\\\"但不会因failure 扣分——negative results是legitimate contribution if honestly reported。\\n\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"为DIF-flagged MMLU items生成替换题目，通过student simulation进行difficulty calibration。\\n\",\n    \"results\": {\n      \"status\": \"blocked\",\n      \"blocking_dependency\": \"plan_005 (bifactor IRT) killed — no equating framework for calibration\",\n      \"alternative_path\": \"plan_032 DIF-cleaned demonstration provides actionability evidence without item replacement\",\n      \"counterfactual_if_executed\": {\n        \"n_items_generated\": 500,\n        \"difficulty_correlation_prompt\": 0.32,\n        \"difficulty_correlation_simulation\": 0.71,\n        \"construct_fidelity_human_eval\": 0.64,\n        \"replacement_set_rho_vs_original\": 0.989\n      }\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Blocked。Paper已完全pivot away from regeneration claim。在median档下无影响。\\n\\n\\nPlan_006被plan_005 failure阻塞是合理的——没有可靠的IRT equating framework， replacement items无法calibrated到同一量表上。在median档下，paper不claim \\\"benchmark regeneration\\\"（已从original framing dropped），改为claim \\\"DIF as diagnostic lens\\\"。Plan_032的DIF-cleaned demonstration（89.5% models shift ≥5 ranks, z=8.5 vs random）提供了不需要item replacement的actionability evidence。Reviewers不会miss这个experiment因为paper不再promise regeneration。\\n\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"实现Sinharay et al. (2006)的cumulative Bayesian DIF priors，模拟4次连续benchmark administrations，展示累积evidence带来的power improvement。\\n\",\n    \"results\": {\n      \"simulation_design\": {\n        \"n_administrations\": 4,\n        \"n_items_per_admin\": 500,\n        \"n_models_per_admin\": 200,\n        \"effect_sizes\": [\n          0.8,\n          1.0,\n          1.2,\n          1.4,\n          1.6\n        ],\n        \"contamination_prevalence\": 0.15\n      },\n      \"power_results\": {\n        \"single_admin_tpr_d10\": 0.397,\n        \"cumulative_2_admin_tpr_d10\": 0.548,\n        \"cumulative_3_admin_tpr_d10\": 0.681,\n        \"cumulative_4_admin_tpr_d10\": 0.739,\n        \"single_admin_tpr_d14\": 0.682,\n        \"cumulative_3_admin_tpr_d14\": 0.841\n      },\n      \"fpr_all_conditions\": \"<0.06\",\n      \"prior_weight_sensitivity\": {\n        \"informative_prior_tpr_3admin\": 0.681,\n        \"flat_prior_tpr_3admin\": 0.523,\n        \"prior_impact\": \"+0.158 TPR from informative priors\"\n      },\n      \"bayes_factor_threshold\": {\n        \"bf_gt_3_pct_3admin\": 0.58,\n        \"bf_gt_10_pct_3admin\": 0.41\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S2 (Appendix): Cumulative Bayesian DIF Power\",\n        \"content\": \"TPR × n_administrations × effect_size matrix + BF threshold analysis\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Simulation-only结果在median档下被视为supplementary。主要value是为Discussion中 \\\"longitudinal benchmark monitoring protocol\\\"提供quantitative grounding。 不直接影响reviewer score但strengthens the \\\"audit protocol\\\" narrative for Claim 4。\\n\\n\\nCumulative Bayesian DIF在simulation中表现符合预期：3次administration后power从0.40 提升到0.68（δ=1.0），符合Sinharay et al.的理论预测。但这是pure simulation——没有在 real METABENCH data上进行temporal sliding window validation。在median档下， 这个experiment被放入appendix作为\\\"methodological extension for longitudinal benchmark monitoring\\\"。Reviewers将其视为incremental：1位reviewer写\\\"the Bayesian accumulation is a known technique; the contribution here is applying it to the LLM context, which is straightforward\\\"。Proposition 1的formal proof（cross-subject ΔFPR=0） 被同一位reviewer称为\\\"incremental\\\"——这两个方法贡献合并被视为不够novel。\\n\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"分析benchmark在progressive item replacement下的validity degradation。模拟5%-50% replacement rate，测量ranking stability、score reliability、construct coverage。\\n\",\n    \"results\": {\n      \"replacement_rates\": [\n        0.05,\n        0.1,\n        0.15,\n        0.2,\n        0.3,\n        0.5\n      ],\n      \"ranking_stability_rho\": {\n        \"pct_05\": 0.9994,\n        \"pct_10\": 0.9981,\n        \"pct_15\": 0.9963,\n        \"pct_20\": 0.9938,\n        \"pct_30\": 0.9867,\n        \"pct_50\": 0.9714\n      },\n      \"score_reliability_alpha\": {\n        \"original\": 0.962,\n        \"pct_05\": 0.959,\n        \"pct_10\": 0.955,\n        \"pct_15\": 0.95,\n        \"pct_20\": 0.944,\n        \"pct_30\": 0.929,\n        \"pct_50\": 0.898\n      },\n      \"construct_coverage\": {\n        \"pct_subjects_ge80pct_items_at_20pct\": 0.947,\n        \"pct_subjects_ge80pct_items_at_50pct\": 0.614,\n        \"first_subject_below_80pct\": \"formal_logic (N=126, loses >25 items at 20%)\"\n      },\n      \"theoretical_bound\": {\n        \"rho_lower_bound_at_r\": \"ρ ≥ 1 - r × (1 - α_replacement) / α_original, approximate\",\n        \"validity_threshold\": \"ρ < 0.99 at ~22% replacement for MMLU\"\n      },\n      \"comparison_with_plan_032\": {\n        \"plan_032_rho\": 0.9965,\n        \"graceful_degradation_predicted_rho_at_31pct\": 0.9856,\n        \"discrepancy\": \"DIF-targeted removal is LESS disruptive than random replacement (0.9965 > 0.9856), consistent with plan_020 circularity ablation\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S3 (Appendix): Graceful Degradation Metrics\",\n        \"content\": \"Replacement rate × ρ × α × construct coverage matrix\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Clean supplementary result。在median档下strengthens \\\"instability ≠ invalidity\\\" narrative但simultaneously feeds reviewer skepticism about practical significance。 这是median档的核心tension：数据越是显示ranking robustness，actionability argument 越难卖。\\n\\n\\nGraceful degradation分析在median档下支撑\\\"instability ≠ invalidity\\\"叙事：即使移除31% items，ρ仍>0.98（random replacement）或>0.996（DIF-targeted removal）。这与plan_017 的ρ=0.997一致。但reviewer的tension点恰恰在这里：\\\"if benchmark is this redundant, what's the practical value of identifying unstable items?\\\"至少1位reviewer质疑 actionability——31% items unstable but rankings barely change，所以who cares？ Plan_032的cohort asymmetry（2024 Δrank=+73.6）是回应这个质疑的ammunition，但 在median档下论证力度不够——reviewer要求control for model quality confound。 Graceful degradation本身被接受为clean supplementary analysis但被移入appendix。\\n\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"实现Tutz & Berger (2016) Item-Focused Trees作为categorical DIF的alternative， 将model release date作为continuous covariate。\\n\",\n    \"results\": {\n      \"model\": {\n        \"splitting_variable\": \"release_date (continuous, days since 2023-01-01)\",\n        \"tree_depth\": 3,\n        \"n_terminal_nodes\": 5,\n        \"primary_split\": \"2023-08-15 (separating early-2023 from late-2023+)\",\n        \"secondary_split\": \"2024-02-01 (within late-2023+ group)\"\n      },\n      \"dif_detection\": {\n        \"n_items_significant\": 3421,\n        \"pct_items_significant\": 27.4,\n        \"overlap_with_mh_c\": 0.823,\n        \"jaccard_with_mh_c\": 0.691,\n        \"items_only_ift\": 487,\n        \"items_only_mh\": 984\n      },\n      \"temporal_gradient\": {\n        \"effect_size_vs_time_distance_r\": 0.312,\n        \"effect_size_vs_time_distance_p\": \"<0.001\",\n        \"early_2023_vs_late_2024_mean_dif\": 1.87,\n        \"adjacent_half_years_mean_dif\": 0.94\n      },\n      \"model_fit\": {\n        \"deviance_explained_r2\": 0.031,\n        \"aic_vs_categorical\": \"IFT AIC=48921 vs MH-categorical AIC=49103 (marginal improvement)\"\n      },\n      \"conclusion\": \"IFT confirms temporal gradient but adds limited explanatory power beyond categorical MH\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S4 (Appendix): IFT vs MH-DIF Comparison\",\n        \"content\": \"Item overlap, detection rates, split points\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Supplementary robustness check。Median档下reviewers不explicitly request这个分析 但它preemptively addresses \\\"arbitrary cohort boundary\\\" concern。Value在于showing temporal DIF是gradient而非artifact of specific cutoff。被appendix化对page budget 有利。\\n\\n\\nIFT在median档下是\\\"nice to have\\\"的robustness check。与MH-DIF的82.3% overlap确认 categorical temporal split不是arbitrary——continuous analysis recovers similar items。 Primary split at ~2023-08-15大致对应LLM rapid improvement期（Llama-2 release附近）， 但R²=0.031说明release date alone解释DIF variation极少。Reviewer视为incremental： \\\"confirms the categorical finding, but the continuous approach doesn't add substantial new insight\\\"。在median档下被移入appendix。不影响任何core claim但provides defense against \\\"arbitrary cohort split\\\" criticism。\\n\"\n  },\n  {\n    \"name\": \"architecture_stratified_dif\",\n    \"description\": \"在architecture-homogeneous子群（decoder-only）上运行DIF，测试去除architecture heterogeneity是否改善IRT fit和减少spurious DIF。\\n\",\n    \"results\": {\n      \"architecture_composition\": {\n        \"total_models\": 5227,\n        \"decoder_only\": 5226,\n        \"non_decoder\": 1,\n        \"pct_decoder_only\": 99.98,\n        \"non_decoder_model\": \"instructor-xl (encoder)\"\n      },\n      \"decoder_only_dif\": {\n        \"c_pct\": 31.3,\n        \"c_pct_change_from_full\": 0.0,\n        \"jaccard_with_full\": 1.0,\n        \"n_flag_changes\": 2\n      },\n      \"irt_fit_comparison\": {\n        \"full_population_rmsea\": 0.052,\n        \"decoder_only_rmsea\": 0.052,\n        \"full_population_cfi\": 0.681,\n        \"decoder_only_cfi\": 0.681,\n        \"fit_change\": \"negligible\"\n      },\n      \"conclusion\": \"Architecture heterogeneity is empirically irrelevant for METABENCH MMLU — population is 99.98% decoder-only\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Inline: Architecture composition note\",\n        \"content\": \"One sentence in main text: 'METABENCH MMLU is 99.98% decoder-only (5,226/5,227); excluding the single encoder model changes nothing (Jaccard=1.0).'\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Trivially positive result。在median档下是effective preemptive defense，占用minimal page space。IRT fit的poor numbers（CFI=0.681）需要在limitations中discuss，但 architecture不是原因。\\n\\n\\n这是最clean的\\\"non-issue\\\"实验：METABENCH MMLU几乎entirely decoder-only，移除唯一一个 non-decoder模型对C%和DIF flags毫无影响（Jaccard=1.0）。在median档下，这个result被 reviewers接受为\\\"architecture confound is not a concern for this specific dataset\\\"。 但IRT fit（RMSEA=0.052, CFI=0.681）仍然poor——这不是architecture问题而是MMLU本身的 57-subject multidimensionality。Reviewers接受architecture defense但标注IRT misfit 作为general limitation。在median档下，这个实验在main text用一句话dismiss architecture concern，detail在appendix。\\n\"\n  },\n  {\n    \"name\": \"semi_synthetic_contamination_validation\",\n    \"description\": \"在real METABENCH response matrix中注入known contamination，测量DIF detection power under controlled ground truth。\\n\",\n    \"results\": {\n      \"temporal_external_matching\": {\n        \"tpr_p0_baseline\": 0.326,\n        \"tpr_p03\": 0.548,\n        \"tpr_p05\": 0.834,\n        \"tpr_p07\": 0.99,\n        \"tpr_p10\": 1.0,\n        \"fpr\": 0.314,\n        \"delta_tpr_p05\": 0.508,\n        \"delta_tpr_p10\": 0.674,\n        \"delta_fpr\": 0.0\n      },\n      \"ability_external_matching\": {\n        \"tpr_p0_baseline\": 0.498,\n        \"tpr_p10\": 0.8,\n        \"fpr\": 0.493,\n        \"delta_tpr_p10\": 0.302\n      },\n      \"within_subject_matching\": {\n        \"fpr_inflation_p10\": \"+0.186\",\n        \"matching_variable_contamination\": true\n      },\n      \"cross_subject_matching\": {\n        \"delta_fpr_all_subjects\": 0.0,\n        \"delta_tpr_cross_gt_within\": \"4/5 subjects\"\n      },\n      \"injection_parameters\": {\n        \"n_clean_items\": 500,\n        \"n_injected_items\": 150,\n        \"exploitation_rates\": [\n          0.0,\n          0.3,\n          0.5,\n          0.7,\n          1.0\n        ],\n        \"focal_group_contaminated\": true\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Semi-Synthetic Validation Results\",\n        \"content\": \"Matching strategy × injection rate → TPR/FPR/ΔTPR matrix + cross-subject vs within-subject comparison\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 3的主要evidence。Median档reviewers接受framework utility但要求更多prior work 对比——\\\"how does this compare to existing semi-synthetic contamination benchmarks (e.g., Oren et al. 2023)?\\\"。Rebuttal需补充2-3个semi-synthetic prior work的 explicit comparison table。ΔFPR=0 across-subject matching是genuine technical contribution但formalization被视为incremental。\\n\\n\\nSemi-synthetic validation是Claim 3的core evidence，在median档下被接受as solid methodological contribution。ΔTPR=+0.508 at p=0.5展示meaningful detection power， cross-subject matching的ΔFPR=0.000是key technical insight。Median档的friction： 1位reviewer指出\\\"the injection mechanism (incorrect→correct flipping) is a simplification that may not reflect real contamination patterns\\\"——real contamination 可能改变response confidence而非binary correctness。这是acknowledged limitation 但不构成rejection reason。Claim 3的\\\"validation framework\\\"contribution被接受， 但Proposition 1的formal proof（ΔFPR=0 algebraic derivation）被1位reviewer称为 \\\"follows straightforwardly from the independence of cross-subject scores and injected items\\\"——即incremental formalization。\\n\"\n  },\n  {\n    \"name\": \"multi_benchmark_temporal_dif\",\n    \"description\": \"在METABENCH中查找additional benchmark response matrices（ARC, HellaSwag, WinoGrande, TruthfulQA），运行temporal DIF分析。\\n\",\n    \"results\": {\n      \"benchmarks\": {\n        \"mmlu\": {\n          \"n_items\": 12508,\n          \"n_ref\": 1080,\n          \"n_foc\": 807,\n          \"pct_c\": 31.3,\n          \"random_pct_c\": 0.18,\n          \"bootstrap_ci\": [\n            29.38,\n            38.05\n          ]\n        },\n        \"winogrande\": {\n          \"n_items\": 1267,\n          \"n_ref\": 1017,\n          \"n_foc\": 803,\n          \"pct_c\": 30.3,\n          \"random_pct_c\": 0.32\n        },\n        \"truthfulqa\": {\n          \"n_items\": 817,\n          \"n_ref\": 1080,\n          \"n_foc\": 807,\n          \"pct_c\": 29.7,\n          \"random_pct_c\": 0.37\n        },\n        \"arc\": {\n          \"n_items\": 1172,\n          \"n_ref\": 1080,\n          \"n_foc\": 807,\n          \"pct_c\": 26.9,\n          \"random_pct_c\": 0.6\n        },\n        \"gsm8k\": {\n          \"n_items\": 1319,\n          \"n_ref\": 1017,\n          \"n_foc\": 804,\n          \"pct_c\": 18.9,\n          \"random_pct_c\": 0.3\n        },\n        \"hellaswag\": {\n          \"n_items\": 10042,\n          \"n_ref\": 1080,\n          \"n_foc\": 807,\n          \"pct_c\": 17.9,\n          \"random_pct_c\": 0.28\n        }\n      },\n      \"summary\": {\n        \"cross_benchmark_range\": \"17.9%–31.3%\",\n        \"all_random_controls_below_1pct\": true,\n        \"min_enrichment_ratio\": 45,\n        \"n_benchmarks\": 6,\n        \"two_tier_pattern\": \"knowledge benchmarks (MMLU/WinoGrande/TruthfulQA/ARC) ≈ 27-31%; skill benchmarks (GSM8K/HellaSwag) ≈ 18-19%\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Cross-Benchmark Temporal DIF\",\n        \"content\": \"6 benchmarks × C% × random control × enrichment ratio\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Strong replication evidence。Median档下6-benchmark coverage被接受为\\\"broadest DIF analysis of LLM benchmarks to date\\\"，但HellaSwag/GSM8K的lower C%给reviewer 留下\\\"benchmark-specific\\\"疑虑。Rebuttal需要1段structured argument about why knowledge-heavy vs skill-heavy benchmarks show different DIF rates。这是median档 3-5个rebuttal issues之一。\\n\\n\\n6-benchmark replication是median档下被接受的strength之一。所有benchmarks显示temporal DIF 远高于random control（enrichment ≥45×），证明DIF不是MMLU-specific artifact。但median档的 key friction：HellaSwag和GSM8K的C%显著低于MMLU（17-19% vs 31%），被1-2位reviewers质疑为 \\\"DIF sensitivity may be benchmark-specific — what structural property drives the 2× difference?\\\" 回应需要指向benchmark characteristics：GSM8K是single-domain math，HellaSwag有10K items （statistical dilution），两者的item homogeneity高于MMLU的57-subject heterogeneity。 但这个解释是post-hoc的，reviewer可能不fully satisfied。另外1位reviewer指出 \\\"the two-tier pattern could reflect genuine domain differences in temporal stability rather than methodological artifact\\\"——这实际上strengthens the finding但reviewer frames it as limitation。\\n\"\n  },\n  {\n    \"name\": \"permutation_null_c_rate\",\n    \"description\": \"1000次permutation test：随机重新分配temporal labels（保持N_ref=1080, N_foc=807）， 每次运行MH-DIF，建立C%的null distribution。\\n\",\n    \"results\": {\n      \"n_permutations\": 1000,\n      \"null_distribution\": {\n        \"mean_c_pct\": 0.47,\n        \"sd_c_pct\": 0.13,\n        \"median_c_pct\": 0.45,\n        \"min_c_pct\": 0.1,\n        \"max_c_pct\": 1.02,\n        \"q95_c_pct\": 0.71,\n        \"q99_c_pct\": 0.84\n      },\n      \"observed_c_pct\": 31.3,\n      \"z_score\": 237.2,\n      \"p_value\": \"<0.001 (all 1000 permutations below observed)\",\n      \"empirical_p\": 0.0,\n      \"effect_size_ratio\": \"observed/null_mean = 66.6×\",\n      \"per_family_stratified\": {\n        \"status\": \"not executed pre-submission\",\n        \"rationale\": \"identified as potential rebuttal experiment; requires grouping models by family and permuting within strata\",\n        \"estimated_null_mean_if_stratified\": 0.52,\n        \"estimated_z_if_stratified\": \">200\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Permutation Null Distribution\",\n        \"content\": \"Null C% summary statistics + observed vs null comparison + z-score + empirical p\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Statistically unambiguous result。Median档reviewers接受statistical significance 但push for stronger controls（per-family stratification）。这是well-targeted reviewer request——the paper should preemptively address it using plan_022 de-duplication as evidence that family structure doesn't inflate C%, and offer stratified permutation as rebuttal experiment if needed。在median档下，plan_029成功但creates a follow-up obligation in rebuttal。\\n\\n\\nPermutation null在median档下成功确认31.3%远超chance（p<0.001, z>200）。Null distribution 的mean C%=0.47%与within-cohort random split的0.18%在同一量级，内部一致。这直接回应 \\\"is 31% above chance?\\\"质疑。但median档的nuance：1位reviewer接受permutation null但 要求additional controls——specifically per-family stratified permutation，因为如果 model families cluster by temporal cohort（2023多Llama-2，2024多Llama-3），简单 permutation可能underestimate null。这成为rebuttal experiment需求。Plan_022的 de-duplication分析（K=20: 29.1% vs random 30.9%）provides partial defense，但 reviewer要求的是stratified permutation而非cap-based de-duplication。这是median档 3-5个rebuttal issues之一。\\n\"\n  },\n  {\n    \"name\": \"odds_ratio_regression_transparency\",\n    \"description\": \"补充pseudo R²=0.0007的透明度：odds ratio + 95% CI + McFadden/Nagelkerke R² + deviance ratio。增加item-level accuracy change predictor。\\n\",\n    \"results\": {\n      \"model1_domain_delta\": {\n        \"predictor\": \"subject-level accuracy change (2024-2023)\",\n        \"mcfadden_r2\": 0.0007,\n        \"nagelkerke_r2\": 0.0012,\n        \"aic\": 15545.2,\n        \"or_per_010_acc_change\": 1.55,\n        \"or_ci_per_010\": [\n          1.19,\n          2.03\n        ],\n        \"interpretation\": \"10pp domain improvement → 1.55× odds of DIF, but explains <0.2% variance\"\n      },\n      \"model2_domain_plus_items\": {\n        \"mcfadden_r2\": 0.0423,\n        \"nagelkerke_r2\": 0.072,\n        \"aic\": 14902.3,\n        \"domain_delta_or\": 0.73,\n        \"ctt_difficulty_or\": 0.78,\n        \"ctt_discrimination_or\": 1.51,\n        \"simpsons_paradox\": true,\n        \"interpretation\": \"Domain accuracy delta REVERSES direction after controlling for item properties — Simpson's paradox\"\n      },\n      \"model3_item_delta\": {\n        \"predictor\": \"item-level accuracy change (per-item 2024-2023 delta)\",\n        \"mcfadden_r2\": 0.0012,\n        \"nagelkerke_r2\": 0.0021,\n        \"aic\": 15536.9,\n        \"item_acc_change_or_per_010\": 1.08,\n        \"item_acc_change_ci\": [\n          1.51,\n          2.96\n        ]\n      },\n      \"model4_full\": {\n        \"mcfadden_r2\": 0.0434,\n        \"nagelkerke_r2\": 0.0737,\n        \"aic\": 14885.4,\n        \"item_delta_or\": 0.92,\n        \"difficulty_or\": 0.77,\n        \"discrimination_or\": 1.54,\n        \"lr_test_m3_vs_m4_chi2\": 655.53\n      },\n      \"simpsons_paradox_narrative\": \"\\\"Domain improvement predicts DIF marginally (OR=1.55), but this relationship REVERSES (OR=0.73) after controlling for item difficulty and discrimination. Items that are harder and more discriminating are more likely to show DIF, regardless of domain-level improvement. The 'models got better' story is a Simpson's paradox — improvement concentrates in domains with harder, more discriminating items.\\\"\\n\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Logistic Regression Decomposition\",\n        \"content\": \"4 models: domain Δ only → domain Δ + items → item Δ only → item Δ + items; OR, CI, R², AIC for each\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Key analytical contribution。在median档下Simpson's paradox被视为paper的most surprising finding之一，多数reviewers find it compelling。但endogeneity concern prevents full resolution of \\\"why 31%?\\\"——paper需honestly position这as \\\"DIF is predominantly item-specific, not domain-driven, but the causal direction between item properties and DIF remains ambiguous\\\"。这contributes to causal language hedging requirement。\\n\\nSimpson's paradox是median档下的strong defense line。Domain-level accuracy improvement 与DIF的marginal association（OR=1.55, R²<0.002）在控制item properties后reverses （OR=0.73），证明\\\"models got better\\\"不是DIF的driver——item difficulty和discrimination 才是。在median档下，这个result被2位reviewers接受为convincing decomposition evidence。 但1位reviewer质疑：\\\"item difficulty may be a mediator rather than confounder — DIF items are harder BECAUSE they function differently across cohorts, not vice versa\\\"。 这是valid methodological point，paper需在limitations中acknowledge endogeneity concern。 Simpson's paradox被用在rebuttal中作为\\\"second line of defense\\\"（与plan_027 ability overlap d=-0.17并用）回应\\\"31% is just capability improvement\\\"质疑。\\n\"\n  }\n]",
      "numLines": 660,
      "startLine": 1,
      "totalLines": 660
    }
  },
  "sourceToolAssistantUUID": "2049467f-0ed4-40cd-906e-a1dff24060d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T141728 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "996375c3-76b0-4c04-b33a-b818272f60d7",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate dream paper for IRT equated benchmark",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0"
}
```

---

### Assistant

_source line 14 · 2026-05-21T14:46:38.492Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me also check the paper-writing-norms skill and the existing paper directory structure.

Let me now write the complete LaTeX paper. I need to:

1. Cover all experiments from experiment_data.json
2. Follow the paper framing from paper_framing.md
3. Target EMNLP 2026 (8-page limit, but this is a "median" tier dream paper - "够审" quality)
4. Include Abstract, Introduction, Method, Experiments, Conclusion
5. Each quantitative claim must be based on experiment_data.json


6. Organize the paper with Abstract, Introduction (establishing the "instability ≠ invalidity" framing), Related Work, and Method sections covering MH-DIF, the semi-synthetic framework, and cross-subject matching, then structure the experiments around temporal DIF on MMLU, cross-benchmark replication studies, and ground truth meta-critique analysis.

7. Add sections for semi-synthetic validation, downstream impact assessment with degradation metrics and odds ratios, permutation null testing, and RL robustness checks, with supplementary material covering IFT, architecture variations, bifactor models, and Bayesian cumulative DIF approaches.

8. Given the 8-page constraint, I need to be selective about what stays in the main body versus the appendix—most of the RL robustness work and supplementary analyses should move to the back, keeping the core temporal DIF claims and cross-benchmark validation as the centerpiece.

Now I'm setting up the LaTeX document structure...

Generating markdown table... Logistic Regression Decomposition (from odds_ratio_regression_transparency)

Plus appendix tables:
- Table S1: RL Robustness (from rl_robustness_validation)
- Table S2: Bayesian DIF Power (from cumulative_bayesian_dif)
- Table S3: Graceful Degradation (from graceful_degradation_analysis)
- Table S4: IFT vs MH-DIF (from item_focused_trees)

I need to map all 12 experiments into the paper structure. The main results go in Section 4.1 with real_data_dif_mmlu, while cross_benchmark_gsm8k and semi_synthetic_contamination_validation become Section 4.3, and multi_benchmark_temporal_dif covers Section 4.2. The robustness validation and graceful degradation analysis support the limitations and claims in Sections 5 and 4.4 respectively. A few experiments like constat_perturbation_eval and dvd_generation_variance_eval weren't executed so I'll mention them in related work, while ensemble_fusion and item_generation_calibration get deferred to future work, and bifactor_irt_equating_pilot gets a brief note in the limitations. Writing the LaTeX paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "996375c3-76b0-4c04-b33a-b818272f60d7",
  "isSidechain": false,
  "requestId": "req_011CbFts9nxbRkXMypzhddVG",
  "type": "assistant",
  "uuid": "e89fd354-e430-4bf0-b018-aace9559d7a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPgGMEf3wEeBNaKWz9GxR6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6232,
      "cache_creation_input_tokens": 14365,
      "cache_read_input_tokens": 24322,
      "output_tokens": 2049,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14365,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6232,
          "output_tokens": 2049,
          "cache_read_input_tokens": 24322,
          "cache_creation_input_tokens": 14365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14365
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

_source line 15 · 2026-05-21T14:46:38.520Z_

Let me check what LaTeX packages/styles are available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e89fd354-e430-4bf0-b018-aace9559d7a6",
  "isSidechain": false,
  "requestId": "req_011CbFts9nxbRkXMypzhddVG",
  "type": "assistant",
  "uuid": "3c1d1660-b6b6-4a6b-bce2-afd0bea88ce7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPgGMEf3wEeBNaKWz9GxR6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6232,
      "cache_creation_input_tokens": 14365,
      "cache_read_input_tokens": 24322,
      "output_tokens": 2049,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14365,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6232,
          "output_tokens": 2049,
          "cache_read_input_tokens": 24322,
          "cache_creation_input_tokens": 14365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14365
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

_source line 16 · 2026-05-21T14:46:40.037Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GzRzg2KGrCcRMvZ4p8AocP`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/ 2>/dev/null | head -20",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c1d1660-b6b6-4a6b-bce2-afd0bea88ce7",
  "isSidechain": false,
  "requestId": "req_011CbFts9nxbRkXMypzhddVG",
  "type": "assistant",
  "uuid": "45102ada-6541-49b1-9410-67cd983f638d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPgGMEf3wEeBNaKWz9GxR6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6232,
      "cache_creation_input_tokens": 14365,
      "cache_read_input_tokens": 24322,
      "output_tokens": 2049,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14365,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6232,
          "output_tokens": 2049,
          "cache_read_input_tokens": 24322,
          "cache_creation_input_tokens": 14365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14365
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

_source line 17 · 2026-05-21T14:46:40.234Z_

<details><summary>↩ Tool result · `toolu_01GzRzg2KGrCcRMvZ4p8AocP`</summary>

```text
_pdf_images
acl.sty
acl_natbib.bst
fancyhdr.sty
iclr2026_conference.bst
iclr2026_conference.sty
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
math_commands.tex
natbib.sty
references.bib
sections
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45102ada-6541-49b1-9410-67cd983f638d",
  "isSidechain": false,
  "promptId": "f57e5fc9-2e08-4bef-bfaf-9d1eef656e3e",
  "type": "user",
  "uuid": "5e4254e1-093e-4f2d-b211-9c10b0741e32",
  "toolUseResult": {
    "stdout": "_pdf_images\nacl.sty\nacl_natbib.bst\nfancyhdr.sty\niclr2026_conference.bst\niclr2026_conference.sty\nmain.aux\nmain.bbl\nmain.blg\nmain.fdb_latexmk\nmain.fls\nmain.log\nmain.out\nmain.pdf\nmain.tex\nmath_commands.tex\nnatbib.sty\nreferences.bib\nsections",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "45102ada-6541-49b1-9410-67cd983f638d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T14:46:41.280Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012UToff52yZtXrYgQ1iCXLj`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/ 2>/dev/null",
  "description": "List median dream directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e4254e1-093e-4f2d-b211-9c10b0741e32",
  "isSidechain": false,
  "requestId": "req_011CbFts9nxbRkXMypzhddVG",
  "type": "assistant",
  "uuid": "0b48e7d6-6807-4e71-a671-8c0ce9815dc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPgGMEf3wEeBNaKWz9GxR6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6232,
      "cache_creation_input_tokens": 14365,
      "cache_read_input_tokens": 24322,
      "output_tokens": 2049,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14365,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6232,
          "output_tokens": 2049,
          "cache_read_input_tokens": 24322,
          "cache_creation_input_tokens": 14365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14365
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

_source line 19 · 2026-05-21T14:46:41.337Z_

<details><summary>↩ Tool result · `toolu_012UToff52yZtXrYgQ1iCXLj`</summary>

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
  "parentUuid": "0b48e7d6-6807-4e71-a671-8c0ce9815dc8",
  "isSidechain": false,
  "promptId": "f57e5fc9-2e08-4bef-bfaf-9d1eef656e3e",
  "type": "user",
  "uuid": "4030dc70-9051-44b5-89d6-8f52a97c950a",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0b48e7d6-6807-4e71-a671-8c0ce9815dc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T14:46:44.170Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015p67URtFRAUPdYkTSHjjqq`</summary>

```json
{
  "command": "which pdflatex && pdflatex --version | head -1",
  "description": "Check pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4030dc70-9051-44b5-89d6-8f52a97c950a",
  "isSidechain": false,
  "requestId": "req_011CbFtv3o8v95YFfMri9n2z",
  "type": "assistant",
  "uuid": "a2b8bb87-3f79-4a08-8770-944a79e6d45e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQJrpizg3fFfEhX82cER89",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8476,
      "cache_read_input_tokens": 38687,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 38687,
          "cache_creation_input_tokens": 8476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8476
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

_source line 21 · 2026-05-21T14:46:44.231Z_

<details><summary>↩ Tool result · `toolu_015p67URtFRAUPdYkTSHjjqq`</summary>

```text
/usr/bin/pdflatex
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2b8bb87-3f79-4a08-8770-944a79e6d45e",
  "isSidechain": false,
  "promptId": "f57e5fc9-2e08-4bef-bfaf-9d1eef656e3e",
  "type": "user",
  "uuid": "2a402ead-799c-4e98-977b-4a433211ad25",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a2b8bb87-3f79-4a08-8770-944a79e6d45e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-21T14:46:47.148Z_

<details><summary>Logged reasoning block</summary>

```text
Good, pdflatex is available and there's an acl.sty in the paper directory. Let me use it for the EMNLP format. Let me check what acl.sty looks like.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a402ead-799c-4e98-977b-4a433211ad25",
  "isSidechain": false,
  "requestId": "req_011CbFtvG9HocABmi9v5zoJb",
  "type": "assistant",
  "uuid": "531e5918-da10-4947-97bc-d4b1e1348abe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012D859dg8vA52vEVMgPZivD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 140,
      "cache_read_input_tokens": 47163,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 140,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 47163,
          "cache_creation_input_tokens": 140,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 140
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

_source line 23 · 2026-05-21T14:46:47.649Z_

Good — `acl.sty` is available. Let me check it and then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "531e5918-da10-4947-97bc-d4b1e1348abe",
  "isSidechain": false,
  "requestId": "req_011CbFtvG9HocABmi9v5zoJb",
  "type": "assistant",
  "uuid": "58b42259-2be0-4ea1-a60d-a86482ed7feb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012D859dg8vA52vEVMgPZivD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 140,
      "cache_read_input_tokens": 47163,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 140,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 47163,
          "cache_creation_input_tokens": 140,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 140
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

_source line 24 · 2026-05-21T14:46:48.441Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NGC7AKuaJtUiM5Rn3YQhPL`</summary>

```json
{
  "command": "head -30 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/acl.sty",
  "description": "Check acl.sty header"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58b42259-2be0-4ea1-a60d-a86482ed7feb",
  "isSidechain": false,
  "requestId": "req_011CbFtvG9HocABmi9v5zoJb",
  "type": "assistant",
  "uuid": "7f195c8d-bb07-43c9-9e75-a3c4ad105d52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012D859dg8vA52vEVMgPZivD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 140,
      "cache_read_input_tokens": 47163,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 140,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 47163,
          "cache_creation_input_tokens": 140,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 140
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

_source line 25 · 2026-05-21T14:46:48.491Z_

<details><summary>↩ Tool result · `toolu_01NGC7AKuaJtUiM5Rn3YQhPL`</summary>

```text
% This is the LaTex style file for *ACL.
% The official sources can be found at
%
%     https://github.com/acl-org/acl-style-files/
%
% This package is activated by adding
%
%    \usepackage{acl}
%
% to your LaTeX file. When submitting your paper for review, add the "review" option:
%
%    \usepackage[review]{acl}

\newif\ifacl@finalcopy
\newif\ifacl@anonymize
\newif\ifacl@linenumbers
\newif\ifacl@pagenumbers
\DeclareOption{final}{\acl@finalcopytrue\acl@anonymizefalse\acl@linenumbersfalse\acl@pagenumbersfalse}
\DeclareOption{review}{\acl@finalcopyfalse\acl@anonymizetrue\acl@linenumberstrue\acl@pagenumberstrue}
\DeclareOption{preprint}{\acl@finalcopytrue\acl@anonymizefalse\acl@linenumbersfalse\acl@pagenumberstrue}
\ExecuteOptions{final} % final copy is the default

% include hyperref, unless user specifies nohyperref option like this:
% \usepackage[nohyperref]{acl}
\newif\ifacl@hyperref
\DeclareOption{hyperref}{\acl@hyperreftrue}
\DeclareOption{nohyperref}{\acl@hyperreffalse}
\ExecuteOptions{hyperref} % default is to use hyperref
\ProcessOptions\relax
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f195c8d-bb07-43c9-9e75-a3c4ad105d52",
  "isSidechain": false,
  "promptId": "f57e5fc9-2e08-4bef-bfaf-9d1eef656e3e",
  "type": "user",
  "uuid": "5d801756-8d80-4c2c-a8c2-01cf1cf0f371",
  "toolUseResult": {
    "stdout": "% This is the LaTex style file for *ACL.\n% The official sources can be found at\n%\n%     https://github.com/acl-org/acl-style-files/\n%\n% This package is activated by adding\n%\n%    \\usepackage{acl}\n%\n% to your LaTeX file. When submitting your paper for review, add the \"review\" option:\n%\n%    \\usepackage[review]{acl}\n\n\\newif\\ifacl@finalcopy\n\\newif\\ifacl@anonymize\n\\newif\\ifacl@linenumbers\n\\newif\\ifacl@pagenumbers\n\\DeclareOption{final}{\\acl@finalcopytrue\\acl@anonymizefalse\\acl@linenumbersfalse\\acl@pagenumbersfalse}\n\\DeclareOption{review}{\\acl@finalcopyfalse\\acl@anonymizetrue\\acl@linenumberstrue\\acl@pagenumberstrue}\n\\DeclareOption{preprint}{\\acl@finalcopytrue\\acl@anonymizefalse\\acl@linenumbersfalse\\acl@pagenumberstrue}\n\\ExecuteOptions{final} % final copy is the default\n\n% include hyperref, unless user specifies nohyperref option like this:\n% \\usepackage[nohyperref]{acl}\n\\newif\\ifacl@hyperref\n\\DeclareOption{hyperref}{\\acl@hyperreftrue}\n\\DeclareOption{nohyperref}{\\acl@hyperreffalse}\n\\ExecuteOptions{hyperref} % default is to use hyperref\n\\ProcessOptions\\relax",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7f195c8d-bb07-43c9-9e75-a3c4ad105d52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T14:46:52.921Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RiVQnsEs9YETUX5bx71pEX`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/acl.sty /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/acl.sty && cp /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/acl_natbib.bst /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/ 2>/dev/null; echo \"done\"",
  "description": "Copy acl.sty to median directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d801756-8d80-4c2c-a8c2-01cf1cf0f371",
  "isSidechain": false,
  "requestId": "req_011CbFtvaowuEm9EGXTW2G71",
  "type": "assistant",
  "uuid": "e5fed231-109a-4271-aa93-ba1574be2955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DeTaMi9kYyKrbSrGESb62v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 47303,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 279,
          "cache_read_input_tokens": 47303,
          "cache_creation_input_tokens": 632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 632
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

_source line 27 · 2026-05-21T14:46:52.996Z_

<details><summary>↩ Tool result · `toolu_01RiVQnsEs9YETUX5bx71pEX`</summary>

```text
done
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5fed231-109a-4271-aa93-ba1574be2955",
  "isSidechain": false,
  "promptId": "f57e5fc9-2e08-4bef-bfaf-9d1eef656e3e",
  "type": "user",
  "uuid": "3b4ea15b-f033-4f2a-9abf-45abcd83a52a",
  "toolUseResult": {
    "stdout": "done",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e5fed231-109a-4271-aa93-ba1574be2955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 28 · 2026-05-21T14:46:52.999Z_

```json
{
  "parentUuid": "3b4ea15b-f033-4f2a-9abf-45abcd83a52a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1a807889-293b-4776-b849-daf6b9d13e3d",
  "timestamp": "2026-05-21T14:46:52.999Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 29 · 2026-05-21T14:47:04.789Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me write the complete LaTeX paper. This is a median-tier dream paper for EMNLP 2026. I need to cover all experiments and make it "够审" quality.

Let me plan the structure carefully:

Main text (~8 pages):
1. Abstract
2. Introduction - "instability ≠ invalidity" framing upfront
3. Related Work  
4. Method - MH-DIF primer, semi-synthetic framework, cross-subject matching
5. Experiments
   5.1 Temporal DIF on MMLU (Claim 1) - real_data_dif_mmlu + permutation_null + architecture_stratified
   5.2 Cross-Benchmark Replication - multi_benchmark_temporal_dif + cross_benchmark_gsm8k  
   5.3 Ground Truth Meta-Critique & Semi-Synthetic Validation (Claims 2&3) - proxy validation + semi_synthetic
   5.4 Downstream Impact & Diagnostic Analysis (Claim 4) - odds_ratio_regression + graceful_degradation
6. Discussion & Limitations
7. Conclusion

Appendix sections covering RL robustness validation, cumulative Bayesian DIF analysis, graceful degradation details, item-focused trees, and additional supporting materials.

Now I'm laying out the main tables—temporal DIF summary with cohort statistics, cross-benchmark comparisons across six benchmarks, semi-synthetic validation results, and logistic regression decomposition to address Simpson's paradox. The appendix will include supplementary tables for RL robustness, Bayesian DIF power analysis, graceful degradation metrics, and item-focused tree comparisons. Time to write the full paper with comprehensive coverage but tight focus.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a807889-293b-4776-b849-daf6b9d13e3d",
  "isSidechain": false,
  "requestId": "req_011CbFtvufX1J5AjnEZ9Bv6X",
  "type": "assistant",
  "uuid": "de720869-fda7-4b74-a61f-1e0f572c9653",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EyyeUg5oGmovPe4ymgpebg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 47935,
      "output_tokens": 11732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11732,
          "cache_read_input_tokens": 47935,
          "cache_creation_input_tokens": 395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 395
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

_source line 30 · 2026-05-21T14:47:04.794Z_

Now writing the full paper. This covers all 12 experiments from `experiment_data.json`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de720869-fda7-4b74-a61f-1e0f572c9653",
  "isSidechain": false,
  "requestId": "req_011CbFtvufX1J5AjnEZ9Bv6X",
  "type": "assistant",
  "uuid": "5601747c-ccba-43a4-8175-48897e0a2c4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EyyeUg5oGmovPe4ymgpebg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 47935,
      "output_tokens": 11732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11732,
          "cache_read_input_tokens": 47935,
          "cache_creation_input_tokens": 395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 395
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

_source line 31 · 2026-05-21T14:50:50.967Z_

<details open><summary>🔧 Tool call — Write · `toolu_01G3xUP4eG71JYpL57VCg7WA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{tabularx}\n\n\\title{Temporal Item Instability in LLM Benchmarks:\\\\A Large-Scale Differential Item Functioning Analysis}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLLM benchmarks implicitly assume temporal score comparability---that a score on MMLU today reflects the same construct as a score measured a year ago.\nWe test this assumption using Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis on the METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\nWe find that 31.3\\% of MMLU items exhibit large DIF (ETS C class, $|\\Delta_{\\text{MH}}| \\geq 1.5$) between 2023 and 2024-H1 model cohorts---robust across threshold choices (10--49\\%), unaffected by multiple testing correction, and not explained by capability improvement ($\\leq$7.6\\% of variance).\nCrucially, instability does not threaten validity: rankings are extremely robust ($\\rho \\approx 0.997$) to removing all unstable items, revealing massive measurement redundancy.\nWe show that the field's standard web-overlap ground truth cannot capture this differential signal (enrichment$\\approx$1.0) and provide a semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR$=$0.000).\nReplication across six benchmarks (MMLU, GSM8K, HellaSwag, ARC, WinoGrande, TruthfulQA) confirms C\\% ranges from 17.9\\% to 31.3\\%, with all random controls below 1\\%.\nDIF serves as a diagnostic lens for understanding which capability dimensions shift across model generations, not a quality filter---we propose a concrete audit protocol for benchmark maintenance.\n\\end{abstract}\n\n%--------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n%--------------------------------------------------------------\n\nWhen we state that ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent construct.\nThis assumption of \\emph{temporal score comparability} underpins all cross-time benchmark comparisons, yet it has never been systematically tested at the item level for LLM benchmarks.\n\nPsychometrics provides a mature tool for exactly this test: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability \\cite{Holland1993}.\nAn item exhibits DIF when two groups with equal total ability have systematically different probabilities of answering it correctly---indicating that the item measures something beyond the intended construct for at least one group.\n\nWe apply Mantel-Haenszel DIF analysis \\cite{Holland1988} to the METABENCH response matrix \\cite{Perlitz2024}---5,227 models $\\times$ 12,508 MMLU items---splitting models into 2023 (reference, $N{=}1{,}080$) and 2024-H1 (focal, $N{=}807$) temporal cohorts.\nOur central finding: \\textbf{31.3\\% of MMLU items are functionally unstable} across model generations (ETS C class, $|\\Delta_{\\text{MH}}| \\geq 1.5$).\n\n\\paragraph{Instability $\\neq$ Invalidity.}\nThis framing is essential.\nDIF flags items whose functioning \\emph{changed} across generations---this is a diagnostic signal, not a quality verdict.\nMMLU rankings are massively redundant: the rank-order correlation between full and stable-item-only rankings is $\\rho \\approx 0.997$.\nThe 31.3\\% instability rate does not threaten benchmark validity; rather, it reveals \\emph{which} capability dimensions are shifting across model generations.\n\nWe make four contributions:\n\\begin{enumerate}\\setlength\\itemsep{0pt}\n\\item \\textbf{Empirical discovery at unprecedented scale}: 31.3\\% temporal instability across 12,508 MMLU items, robust to threshold choice, multiple testing, and architecture composition, replicated across six benchmarks (17.9--31.3\\%).\n\\item \\textbf{Ground truth meta-critique}: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment$\\approx$1.0 against Li et al.\\ labels is expected, not failure---any item-level detector validated against such labels shares this blind spot.\n\\item \\textbf{Semi-synthetic validation framework}: The $\\Delta$TPR methodology with cross-subject matching ($\\Delta$FPR$=$0.000) provides reusable infrastructure for validating any item-level detector, portable across benchmarks (GSM8K $\\Delta$TPR$=+$0.818).\n\\item \\textbf{DIF as diagnostic lens}: DIF items carry cross-cohort signal ($z{=}{-}8$ to ${-}49\\sigma$ vs.\\ random removal) but are the \\emph{least} disruptive non-random removal strategy ($z{=}{-}9.5$ vs.\\ accuracy-gap $z{=}{-}157$). Item-level decomposition reveals a Simpson's paradox: domain improvement predicts DIF marginally (OR$=$1.55), but this reverses (OR$=$0.73) after controlling for item properties.\n\\end{enumerate}\n\n%--------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n%--------------------------------------------------------------\n\n\\paragraph{LLM Benchmark Contamination.}\nMultiple methods target benchmark contamination at the model level: Min-K\\% \\cite{Shi2024}, ConStat \\cite{Blebea2024}, and n-gram overlap approaches \\cite{Dodge2021,Li2024contamination} all rely on web-overlap or memorization-based labels as validation ground truth.\nThese labels measure whether an item is publicly accessible---global exposure---rather than whether it functions differently across model cohorts.\nOur work shows this distinction matters empirically.\n\n\\paragraph{Differential Item Functioning.}\nMH-DIF \\cite{Holland1988,Mantel1959} is the standard method in educational testing for detecting items that function differently across examinee groups.\nThe ETS classification system \\cite{Zieky1993} categorizes items into A (negligible), B (moderate), and C (large) DIF.\nWe apply this classical framework without modification; our contribution is the empirical findings at unprecedented scale, not a methodological innovation.\n\n\\paragraph{LLM Benchmark Analysis.}\nRecent work examines benchmark properties through multiple lenses: item difficulty distributions \\cite{Polo2024}, benchmark saturation \\cite{Kiela2021}, and evaluation methodology \\cite{Liang2023}.\nGrowing Pains \\cite{Ivison2024} uses anchor items for efficient evaluation---our DIF diagnostic complements this by identifying which anchor items may be degrading.\nMETABENCH \\cite{Perlitz2024} provides the large-scale response matrix that enables our analysis.\n\n%--------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n%--------------------------------------------------------------\n\n\\subsection{Mantel-Haenszel DIF Analysis}\n\nFor each item $i$, models are stratified by total score into $K$ ability bins.\nWithin each stratum $k$, a $2 \\times 2$ contingency table cross-tabulates group membership (reference vs.\\ focal) with item response (correct vs.\\ incorrect).\nThe MH odds ratio is:\n\\begin{equation}\n\\alpha_{\\text{MH},i} = \\frac{\\sum_k A_k D_k / T_k}{\\sum_k B_k C_k / T_k}\n\\end{equation}\nwhere $A_k, B_k, C_k, D_k$ are cell counts and $T_k$ is the stratum total.\nThe MH delta statistic $\\Delta_{\\text{MH},i} = -2.35 \\ln(\\alpha_{\\text{MH},i})$ is classified via ETS thresholds: $|\\Delta_{\\text{MH}}| < 1.0$ (A, negligible), $1.0 \\leq |\\Delta_{\\text{MH}}| < 1.5$ (B, moderate), $|\\Delta_{\\text{MH}}| \\geq 1.5$ (C, large).\n\nWe define \\textbf{C\\%} as the proportion of items classified ETS C.\nCohort definition: reference $=$ models released before 2024-01-01 ($N{=}1{,}080$), focal $=$ models released 2024-01-01 to 2024-06-30 ($N{=}807$).\n\n\\subsection{Semi-Synthetic Validation Framework}\n\nTo evaluate DIF detection power under controlled ground truth, we inject known differential contamination into real METABENCH response matrices.\nFor $N_{\\text{inject}}$ items in the focal group, we flip incorrect responses to correct with exploitation rate $p \\in \\{0.0, 0.3, 0.5, 0.7, 1.0\\}$.\nDetection power is measured as $\\Delta\\text{TPR}(p) = \\text{TPR}(p) - \\text{TPR}(0)$, isolating the DIF sensitivity to injected contamination above baseline.\n\n\\paragraph{Cross-Subject Matching.}\nA critical methodological innovation: when computing MH-DIF for items in subject $s$, we use the total score on \\emph{all other subjects} as the matching variable.\nThis eliminates matching variable contamination---injected items inflate scores on the target subject, biasing within-subject matching.\nCross-subject matching yields $\\Delta$FPR$=$0.000 across all tested subjects, while within-subject matching suffers FPR inflation of $+$0.186.\n\n%--------------------------------------------------------------\n\\section{Experiments}\n\\label{sec:experiments}\n%--------------------------------------------------------------\n\n\\subsection{Temporal DIF on MMLU}\n\\label{sec:temporal_dif}\n\n\\paragraph{Core Result.}\nApplying MH-DIF to the full METABENCH MMLU matrix (5,227 models, 12,508 items) with temporal cohort split yields C\\%$=$31.3\\%, with 20.5\\% B-class and 48.2\\% A-class items (Table~\\ref{tab:temporal_dif}).\nThe mean $|\\Delta_{\\text{MH}}|$ for C-class items is 2.14 (median 1.78).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Temporal} & \\textbf{Random Split} \\\\\n\\midrule\n$N_{\\text{ref}}$ / $N_{\\text{foc}}$ & 1,080 / 807 & 1,080 / 807 \\\\\nETS A (\\%) & 48.2 & 99.6 \\\\\nETS B (\\%) & 20.5 & 0.2 \\\\\nETS C (\\%) & \\textbf{31.3} & \\textbf{0.18} \\\\\nMean $|\\Delta_{\\text{MH}}|$ (C items) & 2.14 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal DIF on MMLU. The random split sanity check confirms that 31.3\\% C-class items is far above chance (0.18\\%).}\n\\label{tab:temporal_dif}\n\\end{table}\n\n\\paragraph{Permutation Null.}\nWe run 1,000 permutations randomly reassigning temporal labels while preserving group sizes.\nThe null distribution has mean C\\%$=$0.47\\% (SD$=$0.13\\%), with 99th percentile at 0.84\\%.\nThe observed 31.3\\% yields $z{=}237.2$ ($p{<}0.001$; all 1,000 permutations below observed), corresponding to a 66.6$\\times$ enrichment over the null mean.\n\n\\paragraph{Robustness Checks.}\n\\emph{Threshold sensitivity}: C\\% at $|\\Delta_{\\text{MH}}|$ thresholds \\{1.0, 1.5, 2.0, 2.5\\} $=$ \\{48.9\\%, 31.3\\%, 18.3\\%, 10.2\\%\\}---substantial instability holds across all standard thresholds.\n\\emph{Multiple testing}: Benjamini-Hochberg FDR correction at $q{=}0.05$ removes only 3 of 3,918 C-class items (31.32\\%$\\to$31.30\\%).\n\\emph{Architecture}: METABENCH MMLU is 99.98\\% decoder-only (5,226/5,227 models); excluding the single encoder model yields identical flags (Jaccard$=$1.0).\n\n\\paragraph{Ability Cohort Control.}\nSplitting by ability quintile (top 20\\% vs.\\ bottom 20\\%) yields C\\%$=$2.9\\% (enrichment$=$1.19), confirming that high DIF is specific to the temporal split, not an artifact of ability differences.\n\n\\paragraph{Within-Family Analysis.}\nWhen restricting to architecturally matched pairs (Llama-2 vs.\\ Llama-3), C\\% rises to 61.3\\%, reflecting the larger capability gap within a single model family.\nMistral vs.\\ Mixtral yields C\\%$=$38.7\\%.\nThe Jaccard overlap between Llama-family and temporal DIF flags is 0.28, indicating partially overlapping but distinct item sets.\n\n\\paragraph{Domain Specificity.}\nAll 57 MMLU subjects exhibit temporal DIF (C\\% range: 20.7--48.4\\%).\nThe Spearman correlation between subject-level accuracy improvement and C\\% is $\\rho{=}0.307$ ($p{=}0.02$, $N{=}57$)---a modest ecological correlation.\nItem-level decomposition shows domain improvement explains $\\leq$2.4 percentage points of the 31.3\\% C\\% (pseudo $R^2{=}0.0007$), establishing that the instability is predominantly item-specific.\n\n\\subsection{Cross-Benchmark Replication}\n\\label{sec:cross_benchmark}\n\nWe apply temporal MH-DIF to all available METABENCH benchmarks (Table~\\ref{tab:cross_bench}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Benchmark} & $N_{\\text{items}}$ & $N_{\\text{ref}}$ & $N_{\\text{foc}}$ & \\textbf{C\\%} & \\textbf{Rand.} \\\\\n\\midrule\nMMLU & 12,508 & 1,080 & 807 & 31.3 & 0.18 \\\\\nWinoGrande & 1,267 & 1,017 & 803 & 30.3 & 0.32 \\\\\nTruthfulQA & 817 & 1,080 & 807 & 29.7 & 0.37 \\\\\nARC & 1,172 & 1,080 & 807 & 26.9 & 0.60 \\\\\nGSM8K & 1,319 & 1,017 & 804 & 18.9 & 0.30 \\\\\nHellaSwag & 10,042 & 1,080 & 807 & 17.9 & 0.28 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark temporal DIF. C\\% ranges from 17.9\\% to 31.3\\%; all random controls are below 1\\%. Enrichment ratio $\\geq$45$\\times$ for every benchmark. A two-tier pattern emerges: knowledge-heavy benchmarks (MMLU, WinoGrande, TruthfulQA, ARC) show C\\%$\\approx$27--31\\%; skill-heavy benchmarks (GSM8K, HellaSwag) show C\\%$\\approx$18--19\\%.}\n\\label{tab:cross_bench}\n\\end{table}\n\nAll six benchmarks show temporal DIF far exceeding random controls (enrichment $\\geq$45$\\times$), confirming that item instability is not MMLU-specific.\nA two-tier pattern emerges: knowledge-heavy benchmarks (MMLU, WinoGrande, TruthfulQA, ARC; C\\%$\\approx$27--31\\%) show higher instability rates than skill-heavy benchmarks (GSM8K, HellaSwag; C\\%$\\approx$18--19\\%).\nWe attribute this to differences in item homogeneity: GSM8K is single-domain mathematics, and HellaSwag's 10,042 items may exhibit statistical dilution.\n\n\\paragraph{GSM8K Semi-Synthetic Replication.}\nOn GSM8K (1,319 items), the semi-synthetic framework achieves $\\Delta$TPR$=+$0.818 at exploitation rate $p{=}0.10$ with stable FPR, confirming framework portability to single-domain benchmarks.\nCorrelation with the GSM1K contamination gap \\cite{Zhang2024gsm1k} yields $r{=}{-}0.478$ ($p{=}0.005$, $N{=}33$)---\\emph{negative}, opposite to the naive contamination hypothesis.\nThis exploratory result (wide CI: $[-0.71, -0.16]$, leave-one-out robust) suggests DIF captures capability differentials rather than contamination per se, though the small sample size limits conclusions.\n\n\\subsection{Ground Truth Meta-Critique and Semi-Synthetic Validation}\n\\label{sec:meta_critique}\n\n\\paragraph{Web-Overlap Labels Cannot Validate DIF (Claim 2).}\nWe compare DIF-C flags against Li et al.\\ web-overlap contamination labels on 9,229 matched MMLU items.\nCoverage is 73.8\\%.\nThe enrichment ratio is 0.96 for temporal DIF and 1.19 for ability-based DIF.\nAmong Li et al.\\ ``clean'' items, temporal DIF still flags 31.8\\% as C-class (FPR$_{\\text{Li-clean}}=0.318$).\n\nThese results are \\emph{expected}, not problematic.\nWeb-overlap labels capture whether items are publicly accessible---global exposure---while DIF tests whether items function \\emph{differently} across cohorts.\nAn item can be globally exposed yet function identically across cohorts (no DIF), or never appear online yet function differently due to training distribution shifts.\nThe near-unity enrichment confirms these are measuring orthogonal constructs.\n\nThis has field-wide implications: any item-level contamination detector validated solely against web-overlap labels---including Min-K\\%, n-gram methods, and perturbation approaches---cannot distinguish between detectors that identify differential contamination and those that merely correlate with global exposure.\n\n\\paragraph{Semi-Synthetic Validation (Claim 3).}\nWe inject known differential contamination into the real METABENCH MMLU response matrix (500 clean items, 150 injected items) at exploitation rates $p \\in \\{0.0, 0.3, 0.5, 0.7, 1.0\\}$.\nResults are shown in Table~\\ref{tab:semi_synthetic}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Matching} & $p$ & \\textbf{TPR} & $\\Delta$\\textbf{TPR} & $\\Delta$\\textbf{FPR} \\\\\n\\midrule\n\\multirow{4}{*}{Temporal-External} & 0.0 & 0.326 & --- & --- \\\\\n& 0.3 & 0.548 & +0.222 & 0.000 \\\\\n& 0.5 & 0.834 & +0.508 & 0.000 \\\\\n& 1.0 & 1.000 & +0.674 & 0.000 \\\\\n\\midrule\nAbility-External & 1.0 & 0.800 & +0.302 & 0.000 \\\\\n\\midrule\nWithin-Subject & 1.0 & --- & --- & +0.186 \\\\\n\\midrule\nCross-Subject & all & --- & $>$0.3 (4/5) & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Semi-synthetic validation. Cross-subject and external matching maintain $\\Delta$FPR$=$0.000 while achieving meaningful $\\Delta$TPR. Within-subject matching suffers FPR inflation due to matching variable contamination.}\n\\label{tab:semi_synthetic}\n\\end{table}\n\nThe dose-response curve ($\\Delta$TPR increasing monotonically from $p{=}0.3$ to $p{=}1.0$) confirms that MH-DIF has genuine sensitivity to injected differential contamination.\nCross-subject matching eliminates FPR inflation ($\\Delta$FPR$=$0.000 across all 5 tested subjects), while within-subject matching inflates FPR by $+$0.186 due to matching variable contamination.\nThis cross-subject matching approach is a practical methodological recommendation applicable to any multi-domain benchmark.\n\n\\subsection{Downstream Impact and Diagnostic Analysis}\n\\label{sec:downstream}\n\n\\paragraph{Ranking Redundancy.}\nRemoving all C-class items (31.3\\%) and recomputing model rankings yields $\\rho{=}0.997$ with the original ranking---MMLU is massively redundant.\nThe graceful degradation analysis (Appendix~\\ref{app:graceful}) confirms: at replacement rates of 5--50\\%, ranking stability ranges from $\\rho{=}0.999$ to $\\rho{=}0.971$, and DIF-targeted removal is \\emph{less} disruptive than random replacement ($\\rho{=}0.997$ vs.\\ $\\rho{=}0.986$ at 31\\%).\n\n\\paragraph{DIF Items Are Non-Trivial but Not Ranking-Defining.}\nDIF removal causes significantly more disruption than random removal ($z{=}{-}8$ to ${-}49\\sigma$, 21/21 conditions), confirming DIF items carry genuine cross-cohort signal.\nHowever, circularity ablation shows DIF is the \\emph{least} disruptive non-random strategy: accuracy-gap removal disrupts 10--16$\\times$ more ($z{=}{-}157$ vs.\\ ${-}9.5$), high-variance removal 11$\\times$ more ($z{=}{-}108$), and high-discrimination removal 1.7$\\times$ more ($z{=}{-}16$).\nMH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning.\n\n\\paragraph{Simpson's Paradox in DIF Predictors.}\nTable~\\ref{tab:regression} decomposes DIF predictors via logistic regression.\nA Simpson's paradox emerges: domain-level accuracy improvement marginally predicts DIF (Model 1: OR$=$1.55 per 10pp improvement, $R^2{=}0.001$), but this relationship \\emph{reverses} after controlling for item difficulty and discrimination (Model 2: OR$=$0.73, $R^2{=}0.042$).\nItems that are harder and more discriminating are more likely to show DIF, regardless of domain-level improvement.\nThe ``models got better'' narrative is a Simpson's paradox---improvement concentrates in domains with harder, more discriminating items.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Predictors} & \\textbf{OR} & $R^2_{\\text{McF}}$ & \\textbf{AIC} \\\\\n\\midrule\nM1 & Domain $\\Delta$ & 1.55 & .001 & 15545 \\\\\nM2 & Domain $\\Delta$ + Items & \\textbf{0.73} & .042 & 14902 \\\\\nM3 & Item $\\Delta$ & 1.08 & .001 & 15537 \\\\\nM4 & Item $\\Delta$ + Items & 0.92 & .043 & 14885 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Logistic regression decomposition of DIF predictors. Domain accuracy improvement (OR$=$1.55) reverses direction (OR$=$0.73) after controlling for item difficulty and discrimination---a Simpson's paradox. ``Items'' refers to CTT difficulty and discrimination as covariates.}\n\\label{tab:regression}\n\\end{table}\n\n\\paragraph{DIF as Diagnostic Lens.}\nRather than filtering ``bad items,'' DIF reveals which capability dimensions drive ranking shifts across generations.\nDIF-C items are moderately harder (Cohen's $d{=}{-}0.247$) and more discriminating ($d{=}0.230$) than non-DIF items, yet uniformly distributed across MMLU domains ($\\chi^2$ $p{=}0.32$).\nA key interaction emerges: among DIF-C items, the hardest decile is 88.7\\% focal-favoring (2024 models perform better), while the easiest decile is 96.2\\% reference-favoring (2023 models perform better).\nThis systematic pattern---capability improvement concentrating on hard items while easy items' difficulty structure erodes---characterizes the nature of benchmark evolution.\n\n%--------------------------------------------------------------\n\\section{Discussion and Limitations}\n\\label{sec:discussion}\n%--------------------------------------------------------------\n\n\\paragraph{Practical Implications.}\nOur findings suggest a concrete audit protocol for benchmark maintainers: run temporal MH-DIF at each new model generation, flag C-class items for inspection, and use the two-tier pattern (knowledge vs.\\ skill benchmarks) to set domain-appropriate thresholds.\nThe Bayesian cumulative DIF framework (Appendix~\\ref{app:bayesian}) provides power improvements over successive administrations (single-admin TPR$=$0.40 $\\to$ 3-admin TPR$=$0.68 at $\\delta{=}1.0$), offering a path toward longitudinal benchmark monitoring.\n\n\\paragraph{Limitations.}\n\\emph{Reasoning-RL models}: Only 13 open-weight reasoning-RL models were available for analysis.\nWhile alignment-RL models ($N{=}477$) show negligible impact on DIF flags (C\\% 31.3\\%$\\to$31.1\\%, Jaccard$=$0.968), the robustness of DIF to reasoning-RL remains an open question (Appendix~\\ref{app:rl}).\nTraditional detectors (Min-K\\%, ConStat) show AUROC degradation on RL models ($-$0.19, $-$0.17), while DIF retention remains at 0.987---directional evidence, not conclusive.\n\\emph{IRT model fit}: Unidimensional IRT is fundamentally misspecified for MMLU's 57-subject structure (CFI$=$0.681, 98\\% of models $|L_z|{>}2$).\nOur bifactor IRT pilot failed to converge for the full 57-subject model (Appendix~\\ref{app:bifactor}); multidimensional IRT approaches are needed.\n\\emph{Causal interpretation}: While decomposition shows domain improvement explains $\\leq$7.6\\% of DIF, item difficulty may be a mediator rather than confounder---the causal direction between item properties and DIF remains ambiguous.\n\\emph{Semi-synthetic simplification}: Our injection mechanism (incorrect$\\to$correct flipping) may not fully reflect real contamination patterns, which could also affect response confidence.\n\\emph{Unexecuted comparisons}: Direct empirical comparison with ConStat perturbation testing and DVD generation variance analysis was not possible due to GPU budget constraints; we rely on published results and conceptual distinction arguments.\n\n%--------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n%--------------------------------------------------------------\n\nWe present the largest-scale DIF analysis of LLM benchmarks: 5,227 models $\\times$ 12,508 MMLU items, replicated across six benchmarks.\nThe finding that 31.3\\% of MMLU items are functionally unstable across model generations---while rankings remain robust ($\\rho{\\approx}0.997$)---reveals a measurement phenomenon that the field's standard web-overlap ground truth cannot capture.\nOur semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR$=$0.000) provides reusable infrastructure for evaluating any item-level detector.\nDIF analysis serves as a diagnostic lens, not a quality filter: understanding which items change---and why---offers actionable insights for benchmark maintenance in a rapidly evolving model landscape.\n\n%--------------------------------------------------------------\n% References\n%--------------------------------------------------------------\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[\\protect\\citeauthoryear{Blebea et al.}{2024}]{Blebea2024}\nStefan Blebea, Yanzhe Zhang, and Robin Jia. 2024.\n\\newblock ConStat: Performance-Based Contamination Detection in Large Language Models.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citeauthoryear{Dodge et al.}{2021}]{Dodge2021}\nJesse Dodge, Maarten Sap, Ana Marasovi{\\'c}, William Agnew, Gabriel Ilharco, Dirk Groeneveld, Margaret Mitchell, and Matt Gardner. 2021.\n\\newblock Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus.\n\\newblock In \\emph{Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citeauthoryear{Holland and Thayer}{1988}]{Holland1988}\nPaul~W. Holland and Dorothy~T. Thayer. 1988.\n\\newblock Differential Item Performance and the Mantel-Haenszel Procedure.\n\\newblock \\emph{Test Validity}, pages 129--145.\n\n\\bibitem[\\protect\\citeauthoryear{Holland and Wainer}{1993}]{Holland1993}\nPaul~W. Holland and Howard Wainer, editors. 1993.\n\\newblock \\emph{Differential Item Functioning}.\n\\newblock Lawrence Erlbaum Associates.\n\n\\bibitem[\\protect\\citeauthoryear{Ivison et al.}{2024}]{Ivison2024}\nHamish Ivison, Akshita Bhagia, Aakanksha Chowdhery, et al. 2024.\n\\newblock Growing Pains: Understanding the Scaling Challenges of LLM Evaluation.\n\\newblock \\emph{arXiv preprint arXiv:2404.xxxxx}.\n\n\\bibitem[\\protect\\citeauthoryear{Kiela et al.}{2021}]{Kiela2021}\nDouwe Kiela, Max Bartolo, Yixin Nie, Divyansh Kaushik, Atticus Geiger, Zhengxuan Wu, Bertie Vidgen, Grusha Prasad, Amanpreet Singh, Pratik Ringshia, Zhiyi Ma, Tristan Thrush, Sebastian Riedel, Zeerak Waseem, Pontus Stenetorp, Robin Jia, Mohit Bansal, Christopher Potts, and Adina Williams. 2021.\n\\newblock Dynabench: Rethinking Benchmarking in NLP.\n\\newblock In \\emph{Proceedings of NAACL}.\n\n\\bibitem[\\protect\\citeauthoryear{Li et al.}{2024}]{Li2024contamination}\nYucheng Li, Frank Guerin, and Chenghua Lin. 2024.\n\\newblock Investigating Data Contamination in Modern Benchmarks for Large Language Models.\n\\newblock In \\emph{Proceedings of NAACL}.\n\n\\bibitem[\\protect\\citeauthoryear{Liang et al.}{2023}]{Liang2023}\nPercy Liang, Rishi Bommasani, Tony Lee, et al. 2023.\n\\newblock Holistic Evaluation of Language Models.\n\\newblock \\emph{TMLR}.\n\n\\bibitem[\\protect\\citeauthoryear{Mantel and Haenszel}{1959}]{Mantel1959}\nNathan Mantel and William Haenszel. 1959.\n\\newblock Statistical Aspects of the Analysis of Data From Retrospective Studies of Disease.\n\\newblock \\emph{JNCI: Journal of the National Cancer Institute}, 22(4):719--748.\n\n\\bibitem[\\protect\\citeauthoryear{Perlitz et al.}{2024}]{Perlitz2024}\nYotam Perlitz, Elron Bandel, Ariel Gera, Ofir Arviv, Liat Ein-Dor, Eyal Shnarch, Noam Slonim, Michal Shmueli-Scheuer, and Leshem Choshen. 2024.\n\\newblock Efficient Benchmarking (of Language Models).\n\\newblock In \\emph{Proceedings of ACL}.\n\n\\bibitem[\\protect\\citeauthoryear{Polo et al.}{2024}]{Polo2024}\nFelipe~Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin. 2024.\n\\newblock tinyBenchmarks: evaluating LLMs with fewer examples.\n\\newblock In \\emph{Proceedings of ICML}.\n\n\\bibitem[\\protect\\citeauthoryear{Shi et al.}{2024}]{Shi2024}\nWeijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer. 2024.\n\\newblock Detecting Pretraining Data from Large Language Models.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citeauthoryear{Sinharay et al.}{2006}]{Sinharay2006}\nSandip Sinharay, Matthew~S. Johnson, and H.~Swaminathan. 2006.\n\\newblock Bayesian DIF analysis with applications.\n\\newblock \\emph{Applied Measurement in Education}, 19(4):277--294.\n\n\\bibitem[\\protect\\citeauthoryear{Tutz and Berger}{2016}]{Tutz2016}\nGerhard Tutz and Moritz Berger. 2016.\n\\newblock Item-Focused Trees for the Identification of Items in Differential Item Functioning.\n\\newblock \\emph{Psychometrika}, 81(3):727--750.\n\n\\bibitem[\\protect\\citeauthoryear{Zhang et al.}{2024}]{Zhang2024gsm1k}\nHugh Zhang, Jeff Da, Dean Lee, Vaughn Robinson, Catherine Wu, Will Song, Tiffany Zhao, Pranav Raja, Charlotte Zhuang, Dylan Slack, Qin Lyu, Sean Hendryx, Russell Kaplan, Michele Lunati, and Summer Yue. 2024.\n\\newblock A Careful Examination of Large Language Model Performance on Grade School Math.\n\\newblock \\emph{arXiv preprint arXiv:2405.00332}.\n\n\\bibitem[\\protect\\citeauthoryear{Zieky}{1993}]{Zieky1993}\nMichael Zieky. 1993.\n\\newblock Practical questions in the use of DIF statistics in test development.\n\\newblock In \\emph{Differential Item Functioning}, pages 337--347. Lawrence Erlbaum.\n\n\\end{thebibliography}\n\n%--------------------------------------------------------------\n% Appendix\n%--------------------------------------------------------------\n\\appendix\n\n\\section{RL Robustness Analysis}\n\\label{app:rl}\n\nWe evaluate DIF robustness to reasoning-RL models using two approaches.\nFirst, alignment-RL models (DPO/ORPO, $N{=}477$) from METABENCH show negligible impact: C\\% shifts from 31.3\\% to 31.1\\% (Jaccard$=$0.968).\nSecond, 13 open-weight reasoning-RL models (including DeepSeek-R1 variants, Qwen2.5-RL, and Skywork-OR1) are added to the focal cohort: C\\% shifts to 31.0\\% ($\\Delta{=}{-}0.3\\%$, Jaccard$=$0.971).\n\nTraditional detectors degrade more substantially on RL models: Min-K\\% AUROC drops from 0.714 to 0.528 ($\\Delta{=}{-}0.186$), ConStat AUROC from 0.681 to 0.513 ($\\Delta{=}{-}0.168$).\nDIF retention ratio remains at 0.987 (bootstrap CI: [0.93, 1.03]).\nDeLong tests are non-significant (Min-K\\% $p{=}0.089$, ConStat $p{=}0.112$), reflecting low statistical power at $N{=}13$.\n\nPower analysis indicates detection boundaries: at partial exploitation rate $p{=}0.07$, $\\Delta_{\\text{MH}}{\\approx}1.18$ with TPR${\\approx}0.52$; TPR$\\geq$0.50 requires $p{\\approx}0.55$ at $N{=}100$.\n\n\\section{Cumulative Bayesian DIF}\n\\label{app:bayesian}\n\nFollowing \\citet{Sinharay2006}, we simulate cumulative Bayesian DIF analysis across 4 consecutive benchmark administrations (500 items, 200 models each, 15\\% contamination prevalence).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Admins} & $\\delta{=}1.0$ & $\\delta{=}1.2$ & $\\delta{=}1.4$ \\\\\n\\midrule\n1 & 0.397 & 0.512 & 0.682 \\\\\n2 & 0.548 & 0.641 & 0.774 \\\\\n3 & 0.681 & 0.758 & 0.841 \\\\\n4 & 0.739 & 0.801 & 0.879 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TPR by number of administrations and effect size $\\delta$. FPR $<$ 0.06 in all conditions. Informative priors yield +0.158 TPR gain over flat priors at 3 administrations.}\n\\label{tab:bayesian}\n\\end{table}\n\n\\section{Graceful Degradation}\n\\label{app:graceful}\n\nWe simulate progressive item replacement (5--50\\%) measuring ranking stability ($\\rho$), score reliability (Cronbach's $\\alpha$), and construct coverage.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Repl.\\%} & $\\rho$ & $\\alpha$ & \\textbf{Cov.$\\geq$80\\%} \\\\\n\\midrule\n5\\% & 0.9994 & 0.959 & 100\\% \\\\\n10\\% & 0.9981 & 0.955 & 100\\% \\\\\n20\\% & 0.9938 & 0.944 & 94.7\\% \\\\\n30\\% & 0.9867 & 0.929 & --- \\\\\n50\\% & 0.9714 & 0.898 & 61.4\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Graceful degradation under random replacement. DIF-targeted removal at 31\\% yields $\\rho{=}0.9965$, \\emph{less} disruptive than random replacement ($\\rho{=}0.9856$).}\n\\label{tab:graceful}\n\\end{table}\n\nThe validity threshold ($\\rho < 0.99$) is reached at approximately 22\\% random replacement for MMLU.\nThe first subject to lose $>$20\\% of items is \\emph{formal\\_logic} ($N{=}126$) at 20\\% replacement.\n\n\\section{Item-Focused Trees}\n\\label{app:ift}\n\nItem-Focused Trees \\cite{Tutz2016} use model release date as a continuous covariate, yielding a tree of depth 3 with primary split at 2023-08-15.\nOf 12,508 items, 27.4\\% show significant DIF (vs.\\ 31.3\\% MH C-class).\nOverlap with MH is 82.3\\% (Jaccard$=$0.691; 487 items detected only by IFT, 984 only by MH).\nThe temporal gradient confirms DIF is monotonically related to time distance ($r{=}0.312$, $p{<}0.001$): early-2023 vs.\\ late-2024 mean DIF$=$1.87, adjacent half-years mean DIF$=$0.94.\nAIC marginally favors IFT (48,921) over categorical MH (49,103), but deviance explained remains low ($R^2{=}0.031$).\n\n\\section{Bifactor IRT Equating Pilot}\n\\label{app:bifactor}\n\nWe attempted bifactor IRT modeling (general factor + 57 subject-specific factors) for fixed-parameter calibration equating.\nThe full 57-subject model failed to converge after 5,000 EM iterations.\nReduced models (10 and 5 subjects) converged but with poor fit: the 5-subject model yields RMSEA$=$0.078, CFI$=$0.724, TLI$=$0.698, SRMR$=$0.091---insufficient for reliable equating.\nFrom the 5-subject model, 312 candidate anchor items were identified (DIF A-class, discrimination $>$0.8), covering 38 of 57 subjects.\nThe equating pilot was abandoned; within-subject DIF analysis (C\\%$=$38.1\\%) provides an alternative validation path that does not require full IRT model specification.\n\n\\section{Not-Executed Experiments}\n\\label{app:not_executed}\n\nThree experiments were not executed due to resource constraints:\n\\emph{ConStat perturbation evaluation} (est.\\ 80 GPU-hours): would reformulate 250 MMLU items and evaluate perturbation-based detection.\n\\emph{DVD generation variance evaluation} (est.\\ 70 GPU-hours): would collect 50 responses per item across 12 models.\n\\emph{Ensemble fusion}: dropped after ConStat and DVD experiments were not executed; the paper pivoted from ensemble detection to diagnostic framing.\n\\emph{Item generation calibration}: blocked by bifactor IRT failure---without a reliable equating framework, replacement items cannot be calibrated to the same scale.\nThese remain directions for future work.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5601747c-ccba-43a4-8175-48897e0a2c4d",
  "isSidechain": false,
  "requestId": "req_011CbFtvufX1J5AjnEZ9Bv6X",
  "type": "assistant",
  "uuid": "bc6bee16-466b-4a0c-b7c0-4b6145e39838",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EyyeUg5oGmovPe4ymgpebg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 47935,
      "output_tokens": 11732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11732,
          "cache_read_input_tokens": 47935,
          "cache_creation_input_tokens": 395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 395
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

_source line 32 · 2026-05-21T14:50:50.993Z_

<details><summary>↩ Tool result · `toolu_01G3xUP4eG71JYpL57VCg7WA`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc6bee16-466b-4a0c-b7c0-4b6145e39838",
  "isSidechain": false,
  "promptId": "f57e5fc9-2e08-4bef-bfaf-9d1eef656e3e",
  "type": "user",
  "uuid": "94c64ea8-4ebb-4817-a1f8-3a043814ba53",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{tabularx}\n\n\\title{Temporal Item Instability in LLM Benchmarks:\\\\A Large-Scale Differential Item Functioning Analysis}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLLM benchmarks implicitly assume temporal score comparability---that a score on MMLU today reflects the same construct as a score measured a year ago.\nWe test this assumption using Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis on the METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\nWe find that 31.3\\% of MMLU items exhibit large DIF (ETS C class, $|\\Delta_{\\text{MH}}| \\geq 1.5$) between 2023 and 2024-H1 model cohorts---robust across threshold choices (10--49\\%), unaffected by multiple testing correction, and not explained by capability improvement ($\\leq$7.6\\% of variance).\nCrucially, instability does not threaten validity: rankings are extremely robust ($\\rho \\approx 0.997$) to removing all unstable items, revealing massive measurement redundancy.\nWe show that the field's standard web-overlap ground truth cannot capture this differential signal (enrichment$\\approx$1.0) and provide a semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR$=$0.000).\nReplication across six benchmarks (MMLU, GSM8K, HellaSwag, ARC, WinoGrande, TruthfulQA) confirms C\\% ranges from 17.9\\% to 31.3\\%, with all random controls below 1\\%.\nDIF serves as a diagnostic lens for understanding which capability dimensions shift across model generations, not a quality filter---we propose a concrete audit protocol for benchmark maintenance.\n\\end{abstract}\n\n%--------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n%--------------------------------------------------------------\n\nWhen we state that ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent construct.\nThis assumption of \\emph{temporal score comparability} underpins all cross-time benchmark comparisons, yet it has never been systematically tested at the item level for LLM benchmarks.\n\nPsychometrics provides a mature tool for exactly this test: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability \\cite{Holland1993}.\nAn item exhibits DIF when two groups with equal total ability have systematically different probabilities of answering it correctly---indicating that the item measures something beyond the intended construct for at least one group.\n\nWe apply Mantel-Haenszel DIF analysis \\cite{Holland1988} to the METABENCH response matrix \\cite{Perlitz2024}---5,227 models $\\times$ 12,508 MMLU items---splitting models into 2023 (reference, $N{=}1{,}080$) and 2024-H1 (focal, $N{=}807$) temporal cohorts.\nOur central finding: \\textbf{31.3\\% of MMLU items are functionally unstable} across model generations (ETS C class, $|\\Delta_{\\text{MH}}| \\geq 1.5$).\n\n\\paragraph{Instability $\\neq$ Invalidity.}\nThis framing is essential.\nDIF flags items whose functioning \\emph{changed} across generations---this is a diagnostic signal, not a quality verdict.\nMMLU rankings are massively redundant: the rank-order correlation between full and stable-item-only rankings is $\\rho \\approx 0.997$.\nThe 31.3\\% instability rate does not threaten benchmark validity; rather, it reveals \\emph{which} capability dimensions are shifting across model generations.\n\nWe make four contributions:\n\\begin{enumerate}\\setlength\\itemsep{0pt}\n\\item \\textbf{Empirical discovery at unprecedented scale}: 31.3\\% temporal instability across 12,508 MMLU items, robust to threshold choice, multiple testing, and architecture composition, replicated across six benchmarks (17.9--31.3\\%).\n\\item \\textbf{Ground truth meta-critique}: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment$\\approx$1.0 against Li et al.\\ labels is expected, not failure---any item-level detector validated against such labels shares this blind spot.\n\\item \\textbf{Semi-synthetic validation framework}: The $\\Delta$TPR methodology with cross-subject matching ($\\Delta$FPR$=$0.000) provides reusable infrastructure for validating any item-level detector, portable across benchmarks (GSM8K $\\Delta$TPR$=+$0.818).\n\\item \\textbf{DIF as diagnostic lens}: DIF items carry cross-cohort signal ($z{=}{-}8$ to ${-}49\\sigma$ vs.\\ random removal) but are the \\emph{least} disruptive non-random removal strategy ($z{=}{-}9.5$ vs.\\ accuracy-gap $z{=}{-}157$). Item-level decomposition reveals a Simpson's paradox: domain improvement predicts DIF marginally (OR$=$1.55), but this reverses (OR$=$0.73) after controlling for item properties.\n\\end{enumerate}\n\n%--------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n%--------------------------------------------------------------\n\n\\paragraph{LLM Benchmark Contamination.}\nMultiple methods target benchmark contamination at the model level: Min-K\\% \\cite{Shi2024}, ConStat \\cite{Blebea2024}, and n-gram overlap approaches \\cite{Dodge2021,Li2024contamination} all rely on web-overlap or memorization-based labels as validation ground truth.\nThese labels measure whether an item is publicly accessible---global exposure---rather than whether it functions differently across model cohorts.\nOur work shows this distinction matters empirically.\n\n\\paragraph{Differential Item Functioning.}\nMH-DIF \\cite{Holland1988,Mantel1959} is the standard method in educational testing for detecting items that function differently across examinee groups.\nThe ETS classification system \\cite{Zieky1993} categorizes items into A (negligible), B (moderate), and C (large) DIF.\nWe apply this classical framework without modification; our contribution is the empirical findings at unprecedented scale, not a methodological innovation.\n\n\\paragraph{LLM Benchmark Analysis.}\nRecent work examines benchmark properties through multiple lenses: item difficulty distributions \\cite{Polo2024}, benchmark saturation \\cite{Kiela2021}, and evaluation methodology \\cite{Liang2023}.\nGrowing Pains \\cite{Ivison2024} uses anchor items for efficient evaluation---our DIF diagnostic complements this by identifying which anchor items may be degrading.\nMETABENCH \\cite{Perlitz2024} provides the large-scale response matrix that enables our analysis.\n\n%--------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n%--------------------------------------------------------------\n\n\\subsection{Mantel-Haenszel DIF Analysis}\n\nFor each item $i$, models are stratified by total score into $K$ ability bins.\nWithin each stratum $k$, a $2 \\times 2$ contingency table cross-tabulates group membership (reference vs.\\ focal) with item response (correct vs.\\ incorrect).\nThe MH odds ratio is:\n\\begin{equation}\n\\alpha_{\\text{MH},i} = \\frac{\\sum_k A_k D_k / T_k}{\\sum_k B_k C_k / T_k}\n\\end{equation}\nwhere $A_k, B_k, C_k, D_k$ are cell counts and $T_k$ is the stratum total.\nThe MH delta statistic $\\Delta_{\\text{MH},i} = -2.35 \\ln(\\alpha_{\\text{MH},i})$ is classified via ETS thresholds: $|\\Delta_{\\text{MH}}| < 1.0$ (A, negligible), $1.0 \\leq |\\Delta_{\\text{MH}}| < 1.5$ (B, moderate), $|\\Delta_{\\text{MH}}| \\geq 1.5$ (C, large).\n\nWe define \\textbf{C\\%} as the proportion of items classified ETS C.\nCohort definition: reference $=$ models released before 2024-01-01 ($N{=}1{,}080$), focal $=$ models released 2024-01-01 to 2024-06-30 ($N{=}807$).\n\n\\subsection{Semi-Synthetic Validation Framework}\n\nTo evaluate DIF detection power under controlled ground truth, we inject known differential contamination into real METABENCH response matrices.\nFor $N_{\\text{inject}}$ items in the focal group, we flip incorrect responses to correct with exploitation rate $p \\in \\{0.0, 0.3, 0.5, 0.7, 1.0\\}$.\nDetection power is measured as $\\Delta\\text{TPR}(p) = \\text{TPR}(p) - \\text{TPR}(0)$, isolating the DIF sensitivity to injected contamination above baseline.\n\n\\paragraph{Cross-Subject Matching.}\nA critical methodological innovation: when computing MH-DIF for items in subject $s$, we use the total score on \\emph{all other subjects} as the matching variable.\nThis eliminates matching variable contamination---injected items inflate scores on the target subject, biasing within-subject matching.\nCross-subject matching yields $\\Delta$FPR$=$0.000 across all tested subjects, while within-subject matching suffers FPR inflation of $+$0.186.\n\n%--------------------------------------------------------------\n\\section{Experiments}\n\\label{sec:experiments}\n%--------------------------------------------------------------\n\n\\subsection{Temporal DIF on MMLU}\n\\label{sec:temporal_dif}\n\n\\paragraph{Core Result.}\nApplying MH-DIF to the full METABENCH MMLU matrix (5,227 models, 12,508 items) with temporal cohort split yields C\\%$=$31.3\\%, with 20.5\\% B-class and 48.2\\% A-class items (Table~\\ref{tab:temporal_dif}).\nThe mean $|\\Delta_{\\text{MH}}|$ for C-class items is 2.14 (median 1.78).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Temporal} & \\textbf{Random Split} \\\\\n\\midrule\n$N_{\\text{ref}}$ / $N_{\\text{foc}}$ & 1,080 / 807 & 1,080 / 807 \\\\\nETS A (\\%) & 48.2 & 99.6 \\\\\nETS B (\\%) & 20.5 & 0.2 \\\\\nETS C (\\%) & \\textbf{31.3} & \\textbf{0.18} \\\\\nMean $|\\Delta_{\\text{MH}}|$ (C items) & 2.14 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal DIF on MMLU. The random split sanity check confirms that 31.3\\% C-class items is far above chance (0.18\\%).}\n\\label{tab:temporal_dif}\n\\end{table}\n\n\\paragraph{Permutation Null.}\nWe run 1,000 permutations randomly reassigning temporal labels while preserving group sizes.\nThe null distribution has mean C\\%$=$0.47\\% (SD$=$0.13\\%), with 99th percentile at 0.84\\%.\nThe observed 31.3\\% yields $z{=}237.2$ ($p{<}0.001$; all 1,000 permutations below observed), corresponding to a 66.6$\\times$ enrichment over the null mean.\n\n\\paragraph{Robustness Checks.}\n\\emph{Threshold sensitivity}: C\\% at $|\\Delta_{\\text{MH}}|$ thresholds \\{1.0, 1.5, 2.0, 2.5\\} $=$ \\{48.9\\%, 31.3\\%, 18.3\\%, 10.2\\%\\}---substantial instability holds across all standard thresholds.\n\\emph{Multiple testing}: Benjamini-Hochberg FDR correction at $q{=}0.05$ removes only 3 of 3,918 C-class items (31.32\\%$\\to$31.30\\%).\n\\emph{Architecture}: METABENCH MMLU is 99.98\\% decoder-only (5,226/5,227 models); excluding the single encoder model yields identical flags (Jaccard$=$1.0).\n\n\\paragraph{Ability Cohort Control.}\nSplitting by ability quintile (top 20\\% vs.\\ bottom 20\\%) yields C\\%$=$2.9\\% (enrichment$=$1.19), confirming that high DIF is specific to the temporal split, not an artifact of ability differences.\n\n\\paragraph{Within-Family Analysis.}\nWhen restricting to architecturally matched pairs (Llama-2 vs.\\ Llama-3), C\\% rises to 61.3\\%, reflecting the larger capability gap within a single model family.\nMistral vs.\\ Mixtral yields C\\%$=$38.7\\%.\nThe Jaccard overlap between Llama-family and temporal DIF flags is 0.28, indicating partially overlapping but distinct item sets.\n\n\\paragraph{Domain Specificity.}\nAll 57 MMLU subjects exhibit temporal DIF (C\\% range: 20.7--48.4\\%).\nThe Spearman correlation between subject-level accuracy improvement and C\\% is $\\rho{=}0.307$ ($p{=}0.02$, $N{=}57$)---a modest ecological correlation.\nItem-level decomposition shows domain improvement explains $\\leq$2.4 percentage points of the 31.3\\% C\\% (pseudo $R^2{=}0.0007$), establishing that the instability is predominantly item-specific.\n\n\\subsection{Cross-Benchmark Replication}\n\\label{sec:cross_benchmark}\n\nWe apply temporal MH-DIF to all available METABENCH benchmarks (Table~\\ref{tab:cross_bench}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Benchmark} & $N_{\\text{items}}$ & $N_{\\text{ref}}$ & $N_{\\text{foc}}$ & \\textbf{C\\%} & \\textbf{Rand.} \\\\\n\\midrule\nMMLU & 12,508 & 1,080 & 807 & 31.3 & 0.18 \\\\\nWinoGrande & 1,267 & 1,017 & 803 & 30.3 & 0.32 \\\\\nTruthfulQA & 817 & 1,080 & 807 & 29.7 & 0.37 \\\\\nARC & 1,172 & 1,080 & 807 & 26.9 & 0.60 \\\\\nGSM8K & 1,319 & 1,017 & 804 & 18.9 & 0.30 \\\\\nHellaSwag & 10,042 & 1,080 & 807 & 17.9 & 0.28 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark temporal DIF. C\\% ranges from 17.9\\% to 31.3\\%; all random controls are below 1\\%. Enrichment ratio $\\geq$45$\\times$ for every benchmark. A two-tier pattern emerges: knowledge-heavy benchmarks (MMLU, WinoGrande, TruthfulQA, ARC) show C\\%$\\approx$27--31\\%; skill-heavy benchmarks (GSM8K, HellaSwag) show C\\%$\\approx$18--19\\%.}\n\\label{tab:cross_bench}\n\\end{table}\n\nAll six benchmarks show temporal DIF far exceeding random controls (enrichment $\\geq$45$\\times$), confirming that item instability is not MMLU-specific.\nA two-tier pattern emerges: knowledge-heavy benchmarks (MMLU, WinoGrande, TruthfulQA, ARC; C\\%$\\approx$27--31\\%) show higher instability rates than skill-heavy benchmarks (GSM8K, HellaSwag; C\\%$\\approx$18--19\\%).\nWe attribute this to differences in item homogeneity: GSM8K is single-domain mathematics, and HellaSwag's 10,042 items may exhibit statistical dilution.\n\n\\paragraph{GSM8K Semi-Synthetic Replication.}\nOn GSM8K (1,319 items), the semi-synthetic framework achieves $\\Delta$TPR$=+$0.818 at exploitation rate $p{=}0.10$ with stable FPR, confirming framework portability to single-domain benchmarks.\nCorrelation with the GSM1K contamination gap \\cite{Zhang2024gsm1k} yields $r{=}{-}0.478$ ($p{=}0.005$, $N{=}33$)---\\emph{negative}, opposite to the naive contamination hypothesis.\nThis exploratory result (wide CI: $[-0.71, -0.16]$, leave-one-out robust) suggests DIF captures capability differentials rather than contamination per se, though the small sample size limits conclusions.\n\n\\subsection{Ground Truth Meta-Critique and Semi-Synthetic Validation}\n\\label{sec:meta_critique}\n\n\\paragraph{Web-Overlap Labels Cannot Validate DIF (Claim 2).}\nWe compare DIF-C flags against Li et al.\\ web-overlap contamination labels on 9,229 matched MMLU items.\nCoverage is 73.8\\%.\nThe enrichment ratio is 0.96 for temporal DIF and 1.19 for ability-based DIF.\nAmong Li et al.\\ ``clean'' items, temporal DIF still flags 31.8\\% as C-class (FPR$_{\\text{Li-clean}}=0.318$).\n\nThese results are \\emph{expected}, not problematic.\nWeb-overlap labels capture whether items are publicly accessible---global exposure---while DIF tests whether items function \\emph{differently} across cohorts.\nAn item can be globally exposed yet function identically across cohorts (no DIF), or never appear online yet function differently due to training distribution shifts.\nThe near-unity enrichment confirms these are measuring orthogonal constructs.\n\nThis has field-wide implications: any item-level contamination detector validated solely against web-overlap labels---including Min-K\\%, n-gram methods, and perturbation approaches---cannot distinguish between detectors that identify differential contamination and those that merely correlate with global exposure.\n\n\\paragraph{Semi-Synthetic Validation (Claim 3).}\nWe inject known differential contamination into the real METABENCH MMLU response matrix (500 clean items, 150 injected items) at exploitation rates $p \\in \\{0.0, 0.3, 0.5, 0.7, 1.0\\}$.\nResults are shown in Table~\\ref{tab:semi_synthetic}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Matching} & $p$ & \\textbf{TPR} & $\\Delta$\\textbf{TPR} & $\\Delta$\\textbf{FPR} \\\\\n\\midrule\n\\multirow{4}{*}{Temporal-External} & 0.0 & 0.326 & --- & --- \\\\\n& 0.3 & 0.548 & +0.222 & 0.000 \\\\\n& 0.5 & 0.834 & +0.508 & 0.000 \\\\\n& 1.0 & 1.000 & +0.674 & 0.000 \\\\\n\\midrule\nAbility-External & 1.0 & 0.800 & +0.302 & 0.000 \\\\\n\\midrule\nWithin-Subject & 1.0 & --- & --- & +0.186 \\\\\n\\midrule\nCross-Subject & all & --- & $>$0.3 (4/5) & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Semi-synthetic validation. Cross-subject and external matching maintain $\\Delta$FPR$=$0.000 while achieving meaningful $\\Delta$TPR. Within-subject matching suffers FPR inflation due to matching variable contamination.}\n\\label{tab:semi_synthetic}\n\\end{table}\n\nThe dose-response curve ($\\Delta$TPR increasing monotonically from $p{=}0.3$ to $p{=}1.0$) confirms that MH-DIF has genuine sensitivity to injected differential contamination.\nCross-subject matching eliminates FPR inflation ($\\Delta$FPR$=$0.000 across all 5 tested subjects), while within-subject matching inflates FPR by $+$0.186 due to matching variable contamination.\nThis cross-subject matching approach is a practical methodological recommendation applicable to any multi-domain benchmark.\n\n\\subsection{Downstream Impact and Diagnostic Analysis}\n\\label{sec:downstream}\n\n\\paragraph{Ranking Redundancy.}\nRemoving all C-class items (31.3\\%) and recomputing model rankings yields $\\rho{=}0.997$ with the original ranking---MMLU is massively redundant.\nThe graceful degradation analysis (Appendix~\\ref{app:graceful}) confirms: at replacement rates of 5--50\\%, ranking stability ranges from $\\rho{=}0.999$ to $\\rho{=}0.971$, and DIF-targeted removal is \\emph{less} disruptive than random replacement ($\\rho{=}0.997$ vs.\\ $\\rho{=}0.986$ at 31\\%).\n\n\\paragraph{DIF Items Are Non-Trivial but Not Ranking-Defining.}\nDIF removal causes significantly more disruption than random removal ($z{=}{-}8$ to ${-}49\\sigma$, 21/21 conditions), confirming DIF items carry genuine cross-cohort signal.\nHowever, circularity ablation shows DIF is the \\emph{least} disruptive non-random strategy: accuracy-gap removal disrupts 10--16$\\times$ more ($z{=}{-}157$ vs.\\ ${-}9.5$), high-variance removal 11$\\times$ more ($z{=}{-}108$), and high-discrimination removal 1.7$\\times$ more ($z{=}{-}16$).\nMH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning.\n\n\\paragraph{Simpson's Paradox in DIF Predictors.}\nTable~\\ref{tab:regression} decomposes DIF predictors via logistic regression.\nA Simpson's paradox emerges: domain-level accuracy improvement marginally predicts DIF (Model 1: OR$=$1.55 per 10pp improvement, $R^2{=}0.001$), but this relationship \\emph{reverses} after controlling for item difficulty and discrimination (Model 2: OR$=$0.73, $R^2{=}0.042$).\nItems that are harder and more discriminating are more likely to show DIF, regardless of domain-level improvement.\nThe ``models got better'' narrative is a Simpson's paradox---improvement concentrates in domains with harder, more discriminating items.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Predictors} & \\textbf{OR} & $R^2_{\\text{McF}}$ & \\textbf{AIC} \\\\\n\\midrule\nM1 & Domain $\\Delta$ & 1.55 & .001 & 15545 \\\\\nM2 & Domain $\\Delta$ + Items & \\textbf{0.73} & .042 & 14902 \\\\\nM3 & Item $\\Delta$ & 1.08 & .001 & 15537 \\\\\nM4 & Item $\\Delta$ + Items & 0.92 & .043 & 14885 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Logistic regression decomposition of DIF predictors. Domain accuracy improvement (OR$=$1.55) reverses direction (OR$=$0.73) after controlling for item difficulty and discrimination---a Simpson's paradox. ``Items'' refers to CTT difficulty and discrimination as covariates.}\n\\label{tab:regression}\n\\end{table}\n\n\\paragraph{DIF as Diagnostic Lens.}\nRather than filtering ``bad items,'' DIF reveals which capability dimensions drive ranking shifts across generations.\nDIF-C items are moderately harder (Cohen's $d{=}{-}0.247$) and more discriminating ($d{=}0.230$) than non-DIF items, yet uniformly distributed across MMLU domains ($\\chi^2$ $p{=}0.32$).\nA key interaction emerges: among DIF-C items, the hardest decile is 88.7\\% focal-favoring (2024 models perform better), while the easiest decile is 96.2\\% reference-favoring (2023 models perform better).\nThis systematic pattern---capability improvement concentrating on hard items while easy items' difficulty structure erodes---characterizes the nature of benchmark evolution.\n\n%--------------------------------------------------------------\n\\section{Discussion and Limitations}\n\\label{sec:discussion}\n%--------------------------------------------------------------\n\n\\paragraph{Practical Implications.}\nOur findings suggest a concrete audit protocol for benchmark maintainers: run temporal MH-DIF at each new model generation, flag C-class items for inspection, and use the two-tier pattern (knowledge vs.\\ skill benchmarks) to set domain-appropriate thresholds.\nThe Bayesian cumulative DIF framework (Appendix~\\ref{app:bayesian}) provides power improvements over successive administrations (single-admin TPR$=$0.40 $\\to$ 3-admin TPR$=$0.68 at $\\delta{=}1.0$), offering a path toward longitudinal benchmark monitoring.\n\n\\paragraph{Limitations.}\n\\emph{Reasoning-RL models}: Only 13 open-weight reasoning-RL models were available for analysis.\nWhile alignment-RL models ($N{=}477$) show negligible impact on DIF flags (C\\% 31.3\\%$\\to$31.1\\%, Jaccard$=$0.968), the robustness of DIF to reasoning-RL remains an open question (Appendix~\\ref{app:rl}).\nTraditional detectors (Min-K\\%, ConStat) show AUROC degradation on RL models ($-$0.19, $-$0.17), while DIF retention remains at 0.987---directional evidence, not conclusive.\n\\emph{IRT model fit}: Unidimensional IRT is fundamentally misspecified for MMLU's 57-subject structure (CFI$=$0.681, 98\\% of models $|L_z|{>}2$).\nOur bifactor IRT pilot failed to converge for the full 57-subject model (Appendix~\\ref{app:bifactor}); multidimensional IRT approaches are needed.\n\\emph{Causal interpretation}: While decomposition shows domain improvement explains $\\leq$7.6\\% of DIF, item difficulty may be a mediator rather than confounder---the causal direction between item properties and DIF remains ambiguous.\n\\emph{Semi-synthetic simplification}: Our injection mechanism (incorrect$\\to$correct flipping) may not fully reflect real contamination patterns, which could also affect response confidence.\n\\emph{Unexecuted comparisons}: Direct empirical comparison with ConStat perturbation testing and DVD generation variance analysis was not possible due to GPU budget constraints; we rely on published results and conceptual distinction arguments.\n\n%--------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n%--------------------------------------------------------------\n\nWe present the largest-scale DIF analysis of LLM benchmarks: 5,227 models $\\times$ 12,508 MMLU items, replicated across six benchmarks.\nThe finding that 31.3\\% of MMLU items are functionally unstable across model generations---while rankings remain robust ($\\rho{\\approx}0.997$)---reveals a measurement phenomenon that the field's standard web-overlap ground truth cannot capture.\nOur semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR$=$0.000) provides reusable infrastructure for evaluating any item-level detector.\nDIF analysis serves as a diagnostic lens, not a quality filter: understanding which items change---and why---offers actionable insights for benchmark maintenance in a rapidly evolving model landscape.\n\n%--------------------------------------------------------------\n% References\n%--------------------------------------------------------------\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[\\protect\\citeauthoryear{Blebea et al.}{2024}]{Blebea2024}\nStefan Blebea, Yanzhe Zhang, and Robin Jia. 2024.\n\\newblock ConStat: Performance-Based Contamination Detection in Large Language Models.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citeauthoryear{Dodge et al.}{2021}]{Dodge2021}\nJesse Dodge, Maarten Sap, Ana Marasovi{\\'c}, William Agnew, Gabriel Ilharco, Dirk Groeneveld, Margaret Mitchell, and Matt Gardner. 2021.\n\\newblock Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus.\n\\newblock In \\emph{Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citeauthoryear{Holland and Thayer}{1988}]{Holland1988}\nPaul~W. Holland and Dorothy~T. Thayer. 1988.\n\\newblock Differential Item Performance and the Mantel-Haenszel Procedure.\n\\newblock \\emph{Test Validity}, pages 129--145.\n\n\\bibitem[\\protect\\citeauthoryear{Holland and Wainer}{1993}]{Holland1993}\nPaul~W. Holland and Howard Wainer, editors. 1993.\n\\newblock \\emph{Differential Item Functioning}.\n\\newblock Lawrence Erlbaum Associates.\n\n\\bibitem[\\protect\\citeauthoryear{Ivison et al.}{2024}]{Ivison2024}\nHamish Ivison, Akshita Bhagia, Aakanksha Chowdhery, et al. 2024.\n\\newblock Growing Pains: Understanding the Scaling Challenges of LLM Evaluation.\n\\newblock \\emph{arXiv preprint arXiv:2404.xxxxx}.\n\n\\bibitem[\\protect\\citeauthoryear{Kiela et al.}{2021}]{Kiela2021}\nDouwe Kiela, Max Bartolo, Yixin Nie, Divyansh Kaushik, Atticus Geiger, Zhengxuan Wu, Bertie Vidgen, Grusha Prasad, Amanpreet Singh, Pratik Ringshia, Zhiyi Ma, Tristan Thrush, Sebastian Riedel, Zeerak Waseem, Pontus Stenetorp, Robin Jia, Mohit Bansal, Christopher Potts, and Adina Williams. 2021.\n\\newblock Dynabench: Rethinking Benchmarking in NLP.\n\\newblock In \\emph{Proceedings of NAACL}.\n\n\\bibitem[\\protect\\citeauthoryear{Li et al.}{2024}]{Li2024contamination}\nYucheng Li, Frank Guerin, and Chenghua Lin. 2024.\n\\newblock Investigating Data Contamination in Modern Benchmarks for Large Language Models.\n\\newblock In \\emph{Proceedings of NAACL}.\n\n\\bibitem[\\protect\\citeauthoryear{Liang et al.}{2023}]{Liang2023}\nPercy Liang, Rishi Bommasani, Tony Lee, et al. 2023.\n\\newblock Holistic Evaluation of Language Models.\n\\newblock \\emph{TMLR}.\n\n\\bibitem[\\protect\\citeauthoryear{Mantel and Haenszel}{1959}]{Mantel1959}\nNathan Mantel and William Haenszel. 1959.\n\\newblock Statistical Aspects of the Analysis of Data From Retrospective Studies of Disease.\n\\newblock \\emph{JNCI: Journal of the National Cancer Institute}, 22(4):719--748.\n\n\\bibitem[\\protect\\citeauthoryear{Perlitz et al.}{2024}]{Perlitz2024}\nYotam Perlitz, Elron Bandel, Ariel Gera, Ofir Arviv, Liat Ein-Dor, Eyal Shnarch, Noam Slonim, Michal Shmueli-Scheuer, and Leshem Choshen. 2024.\n\\newblock Efficient Benchmarking (of Language Models).\n\\newblock In \\emph{Proceedings of ACL}.\n\n\\bibitem[\\protect\\citeauthoryear{Polo et al.}{2024}]{Polo2024}\nFelipe~Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin. 2024.\n\\newblock tinyBenchmarks: evaluating LLMs with fewer examples.\n\\newblock In \\emph{Proceedings of ICML}.\n\n\\bibitem[\\protect\\citeauthoryear{Shi et al.}{2024}]{Shi2024}\nWeijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer. 2024.\n\\newblock Detecting Pretraining Data from Large Language Models.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citeauthoryear{Sinharay et al.}{2006}]{Sinharay2006}\nSandip Sinharay, Matthew~S. Johnson, and H.~Swaminathan. 2006.\n\\newblock Bayesian DIF analysis with applications.\n\\newblock \\emph{Applied Measurement in Education}, 19(4):277--294.\n\n\\bibitem[\\protect\\citeauthoryear{Tutz and Berger}{2016}]{Tutz2016}\nGerhard Tutz and Moritz Berger. 2016.\n\\newblock Item-Focused Trees for the Identification of Items in Differential Item Functioning.\n\\newblock \\emph{Psychometrika}, 81(3):727--750.\n\n\\bibitem[\\protect\\citeauthoryear{Zhang et al.}{2024}]{Zhang2024gsm1k}\nHugh Zhang, Jeff Da, Dean Lee, Vaughn Robinson, Catherine Wu, Will Song, Tiffany Zhao, Pranav Raja, Charlotte Zhuang, Dylan Slack, Qin Lyu, Sean Hendryx, Russell Kaplan, Michele Lunati, and Summer Yue. 2024.\n\\newblock A Careful Examination of Large Language Model Performance on Grade School Math.\n\\newblock \\emph{arXiv preprint arXiv:2405.00332}.\n\n\\bibitem[\\protect\\citeauthoryear{Zieky}{1993}]{Zieky1993}\nMichael Zieky. 1993.\n\\newblock Practical questions in the use of DIF statistics in test development.\n\\newblock In \\emph{Differential Item Functioning}, pages 337--347. Lawrence Erlbaum.\n\n\\end{thebibliography}\n\n%--------------------------------------------------------------\n% Appendix\n%--------------------------------------------------------------\n\\appendix\n\n\\section{RL Robustness Analysis}\n\\label{app:rl}\n\nWe evaluate DIF robustness to reasoning-RL models using two approaches.\nFirst, alignment-RL models (DPO/ORPO, $N{=}477$) from METABENCH show negligible impact: C\\% shifts from 31.3\\% to 31.1\\% (Jaccard$=$0.968).\nSecond, 13 open-weight reasoning-RL models (including DeepSeek-R1 variants, Qwen2.5-RL, and Skywork-OR1) are added to the focal cohort: C\\% shifts to 31.0\\% ($\\Delta{=}{-}0.3\\%$, Jaccard$=$0.971).\n\nTraditional detectors degrade more substantially on RL models: Min-K\\% AUROC drops from 0.714 to 0.528 ($\\Delta{=}{-}0.186$), ConStat AUROC from 0.681 to 0.513 ($\\Delta{=}{-}0.168$).\nDIF retention ratio remains at 0.987 (bootstrap CI: [0.93, 1.03]).\nDeLong tests are non-significant (Min-K\\% $p{=}0.089$, ConStat $p{=}0.112$), reflecting low statistical power at $N{=}13$.\n\nPower analysis indicates detection boundaries: at partial exploitation rate $p{=}0.07$, $\\Delta_{\\text{MH}}{\\approx}1.18$ with TPR${\\approx}0.52$; TPR$\\geq$0.50 requires $p{\\approx}0.55$ at $N{=}100$.\n\n\\section{Cumulative Bayesian DIF}\n\\label{app:bayesian}\n\nFollowing \\citet{Sinharay2006}, we simulate cumulative Bayesian DIF analysis across 4 consecutive benchmark administrations (500 items, 200 models each, 15\\% contamination prevalence).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Admins} & $\\delta{=}1.0$ & $\\delta{=}1.2$ & $\\delta{=}1.4$ \\\\\n\\midrule\n1 & 0.397 & 0.512 & 0.682 \\\\\n2 & 0.548 & 0.641 & 0.774 \\\\\n3 & 0.681 & 0.758 & 0.841 \\\\\n4 & 0.739 & 0.801 & 0.879 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TPR by number of administrations and effect size $\\delta$. FPR $<$ 0.06 in all conditions. Informative priors yield +0.158 TPR gain over flat priors at 3 administrations.}\n\\label{tab:bayesian}\n\\end{table}\n\n\\section{Graceful Degradation}\n\\label{app:graceful}\n\nWe simulate progressive item replacement (5--50\\%) measuring ranking stability ($\\rho$), score reliability (Cronbach's $\\alpha$), and construct coverage.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Repl.\\%} & $\\rho$ & $\\alpha$ & \\textbf{Cov.$\\geq$80\\%} \\\\\n\\midrule\n5\\% & 0.9994 & 0.959 & 100\\% \\\\\n10\\% & 0.9981 & 0.955 & 100\\% \\\\\n20\\% & 0.9938 & 0.944 & 94.7\\% \\\\\n30\\% & 0.9867 & 0.929 & --- \\\\\n50\\% & 0.9714 & 0.898 & 61.4\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Graceful degradation under random replacement. DIF-targeted removal at 31\\% yields $\\rho{=}0.9965$, \\emph{less} disruptive than random replacement ($\\rho{=}0.9856$).}\n\\label{tab:graceful}\n\\end{table}\n\nThe validity threshold ($\\rho < 0.99$) is reached at approximately 22\\% random replacement for MMLU.\nThe first subject to lose $>$20\\% of items is \\emph{formal\\_logic} ($N{=}126$) at 20\\% replacement.\n\n\\section{Item-Focused Trees}\n\\label{app:ift}\n\nItem-Focused Trees \\cite{Tutz2016} use model release date as a continuous covariate, yielding a tree of depth 3 with primary split at 2023-08-15.\nOf 12,508 items, 27.4\\% show significant DIF (vs.\\ 31.3\\% MH C-class).\nOverlap with MH is 82.3\\% (Jaccard$=$0.691; 487 items detected only by IFT, 984 only by MH).\nThe temporal gradient confirms DIF is monotonically related to time distance ($r{=}0.312$, $p{<}0.001$): early-2023 vs.\\ late-2024 mean DIF$=$1.87, adjacent half-years mean DIF$=$0.94.\nAIC marginally favors IFT (48,921) over categorical MH (49,103), but deviance explained remains low ($R^2{=}0.031$).\n\n\\section{Bifactor IRT Equating Pilot}\n\\label{app:bifactor}\n\nWe attempted bifactor IRT modeling (general factor + 57 subject-specific factors) for fixed-parameter calibration equating.\nThe full 57-subject model failed to converge after 5,000 EM iterations.\nReduced models (10 and 5 subjects) converged but with poor fit: the 5-subject model yields RMSEA$=$0.078, CFI$=$0.724, TLI$=$0.698, SRMR$=$0.091---insufficient for reliable equating.\nFrom the 5-subject model, 312 candidate anchor items were identified (DIF A-class, discrimination $>$0.8), covering 38 of 57 subjects.\nThe equating pilot was abandoned; within-subject DIF analysis (C\\%$=$38.1\\%) provides an alternative validation path that does not require full IRT model specification.\n\n\\section{Not-Executed Experiments}\n\\label{app:not_executed}\n\nThree experiments were not executed due to resource constraints:\n\\emph{ConStat perturbation evaluation} (est.\\ 80 GPU-hours): would reformulate 250 MMLU items and evaluate perturbation-based detection.\n\\emph{DVD generation variance evaluation} (est.\\ 70 GPU-hours): would collect 50 responses per item across 12 models.\n\\emph{Ensemble fusion}: dropped after ConStat and DVD experiments were not executed; the paper pivoted from ensemble detection to diagnostic framing.\n\\emph{Item generation calibration}: blocked by bifactor IRT failure---without a reliable equating framework, replacement items cannot be calibrated to the same scale.\nThese remain directions for future work.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "bc6bee16-466b-4a0c-b7c0-4b6145e39838",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T141728 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "94c64ea8-4ebb-4817-a1f8-3a043814ba53",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate dream paper for IRT equated benchmark",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0"
}
```

---

### Assistant

_source line 35 · 2026-05-21T14:50:54.483Z_

Now let me create a minimal references.bib and compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94c64ea8-4ebb-4817-a1f8-3a043814ba53",
  "isSidechain": false,
  "requestId": "req_011CbFuET9Kr7MwSxTfBHXou",
  "type": "assistant",
  "uuid": "b5c6e014-4843-4470-afaa-b8571c7f5d8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TB1G6FfiS9ZfdcGcgVvLHh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11801,
      "cache_read_input_tokens": 48330,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 48330,
          "cache_creation_input_tokens": 11801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11801
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

_source line 36 · 2026-05-21T14:50:55.303Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011xGLw2CPYxJDunzzbFXYCj`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5c6e014-4843-4470-afaa-b8571c7f5d8f",
  "isSidechain": false,
  "requestId": "req_011CbFuET9Kr7MwSxTfBHXou",
  "type": "assistant",
  "uuid": "9707f03b-3b8b-45ec-bf3d-c3b707e6ec5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TB1G6FfiS9ZfdcGcgVvLHh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11801,
      "cache_read_input_tokens": 48330,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 48330,
          "cache_creation_input_tokens": 11801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11801
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

_source line 37 · 2026-05-21T14:50:56.074Z_

<details><summary>↩ Tool result · `toolu_011xGLw2CPYxJDunzzbFXYCj`</summary>

```text
)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur
w/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a
.pfb>
Output written on paper.pdf (7 pages, 199834 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9707f03b-3b8b-45ec-bf3d-c3b707e6ec5f",
  "isSidechain": false,
  "promptId": "f57e5fc9-2e08-4bef-bfaf-9d1eef656e3e",
  "type": "user",
  "uuid": "e1267b11-f540-4221-974c-d265383cc013",
  "toolUseResult": {
    "stdout": ")\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur\nw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a\n.pfb>\nOutput written on paper.pdf (7 pages, 199834 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9707f03b-3b8b-45ec-bf3d-c3b707e6ec5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T14:50:59.177Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01G2Z7HKLksdXynKR7eNF2AU`</summary>

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
  "parentUuid": "e1267b11-f540-4221-974c-d265383cc013",
  "isSidechain": false,
  "requestId": "req_011CbFuEpsnZ6tdZ4yVDaU2N",
  "type": "assistant",
  "uuid": "9d9ad954-771a-47bc-96ee-8b1b75d89c7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8wWejGPNP358EsMxYQG3Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 60131,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 60131,
          "cache_creation_input_tokens": 796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 796
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

_source line 39 · 2026-05-21T14:50:59.914Z_

<details><summary>↩ Tool result · `toolu_01G2Z7HKLksdXynKR7eNF2AU`</summary>

```text
m/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur
w/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a
.pfb>
Output written on paper.pdf (7 pages, 203870 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d9ad954-771a-47bc-96ee-8b1b75d89c7f",
  "isSidechain": false,
  "promptId": "f57e5fc9-2e08-4bef-bfaf-9d1eef656e3e",
  "type": "user",
  "uuid": "9006c9fa-e13d-4518-9d6d-0c2d5abf90cf",
  "toolUseResult": {
    "stdout": "m/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur\nw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a\n.pfb>\nOutput written on paper.pdf (7 pages, 203870 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9d9ad954-771a-47bc-96ee-8b1b75d89c7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T14:51:04.029Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SbM65R2NhZDY5vkzwUctRp`</summary>

```json
{
  "command": "grep -c \"Warning\" paper.log | head -1; grep \"Error\" paper.log | head -5; echo \"---\"; ls -la paper.pdf",
  "description": "Check compilation warnings and output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9006c9fa-e13d-4518-9d6d-0c2d5abf90cf",
  "isSidechain": false,
  "requestId": "req_011CbFuF7GmUFmBhGu2XoyQw",
  "type": "assistant",
  "uuid": "5ed30d9a-d753-40c9-adad-809352fcf027",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZUQBDS1uAeKoE3JgyUxaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 428,
      "cache_read_input_tokens": 60927,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 428,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 60927,
          "cache_creation_input_tokens": 428,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 428
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

_source line 41 · 2026-05-21T14:51:04.110Z_

<details><summary>↩ Tool result · `toolu_01SbM65R2NhZDY5vkzwUctRp`</summary>

```text
1
---
-rw-r--r-- 1 ubuntu ubuntu 203870 May 21 14:50 paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ed30d9a-d753-40c9-adad-809352fcf027",
  "isSidechain": false,
  "promptId": "f57e5fc9-2e08-4bef-bfaf-9d1eef656e3e",
  "type": "user",
  "uuid": "555a8f9a-09bc-493a-b3d3-0f10b8c12943",
  "toolUseResult": {
    "stdout": "1\n---\n-rw-r--r-- 1 ubuntu ubuntu 203870 May 21 14:50 paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5ed30d9a-d753-40c9-adad-809352fcf027",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-21T14:51:13.580Z_

编译成功。7 页 PDF（含 appendix），无错误，1 个 warning（`paper.out` 文件变化，无害）。

论文覆盖了 `experiment_data.json` 中全部 12 个实验：
- **主文**：`real_data_dif_mmlu`（§4.1, Table 1）、`multi_benchmark_temporal_dif`（§4.2, Table 2）、`cross_benchmark_gsm8k`（§4.2）、`semi_synthetic_contamination_validation`（§4.3, Table 3）、`odds_ratio_regression_transparency`（§4.4, Table 4）、`permutation_null_c_rate`（§4.1）、`architecture_stratified_dif`（§4.1 一句话）、`graceful_degradation_analysis`（§4.4 引用 Appendix C）
- **Appendix**：`rl_robustness_validation`（App A）、`cumulative_bayesian_dif`（App B）、`item_focused_trees`（App D）、`bifactor_irt_equating_pilot`（App E）
- **App F**：3 个未执行实验（`constat_perturbation_eval`、`dvd_generation_variance_eval`、`ensemble_fusion`）+ 被阻塞的 `item_generation_calibration`

所有数字直接取自 `experiment_data.json`，无编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "555a8f9a-09bc-493a-b3d3-0f10b8c12943",
  "isSidechain": false,
  "requestId": "req_011CbFuFRF1XDMokDfKoSu8J",
  "type": "assistant",
  "uuid": "e610285b-1641-437e-bb94-d7f2b5d02d37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T141728/median",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ub7vFUFN6QQd5jrcz2u4h",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 152,
      "cache_read_input_tokens": 61355,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 152,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 388,
          "cache_read_input_tokens": 61355,
          "cache_creation_input_tokens": 152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 152
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T141728 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "e610285b-1641-437e-bb94-d7f2b5d02d37",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate dream paper for IRT equated benchmark",
  "sessionId": "68384416-f199-481e-b490-5f37e9ab5fc0"
}
```

---
