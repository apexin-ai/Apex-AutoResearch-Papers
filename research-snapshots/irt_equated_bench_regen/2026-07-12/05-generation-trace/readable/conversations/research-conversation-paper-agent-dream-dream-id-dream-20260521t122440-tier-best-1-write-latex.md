# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122440 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/02a66d51-3ac6-408a-bb4a-e92f7256c0c6.jsonl`
- **Structured JSON:** [`109266b4a4c95fab91e4.json`](../../sessions/10/109266b4a4c95fab91e4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:50:23.662Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:50:23.662Z",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122440 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：原始 framing 完全成立，四条 claim 无需调整强度。Headline: '31% temporal instability across 6 benchmarks, not explained by capability improvement (≤7.6%), validated by semi-synthetic framework with 0 FPR inflation.' Meta-critique 作为 aggressive contribution 直接成立。Diagnostic lens + audit protocol 作为 actionable 贡献。 GSM1K correlation 留 appendix 作为 exploratory。IRT misfit 在 limitations 一笔带过。 Dropped experiments (003a/b/c, 005, 006) 结果确认 pivot 正确性——ensemble coverage gain 不足， bifactor fit 不达标，item generation calibration below benchmark。plan_002 RL robustness N=13 在 limitations 诚实披露。plan_029 permutation null 彻底封堵 'is 31% above chance?' 质疑。 全部 robustness check 干净通过，证据链闭环：permutation null → threshold sensitivity → decomposition → NN matching → circularity ablation → multi-benchmark 六层。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T12:50:23.668Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:50:23.668Z",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6"
}
```

---

## Round 1

40 recorded events

### User

_source line 3 · 2026-05-21T12:50:23.700Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122440 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：原始 framing 完全成立，四条 claim 无需调整强度。Headline: '31% temporal instability across 6 benchmarks, not explained by capability improvement (≤7.6%), validated by semi-synthetic framework with 0 FPR inflation.' Meta-critique 作为 aggressive contribution 直接成立。Diagnostic lens + audit protocol 作为 actionable 贡献。 GSM1K correlation 留 appendix 作为 exploratory。IRT misfit 在 limitations 一笔带过。 Dropped experiments (003a/b/c, 005, 006) 结果确认 pivot 正确性——ensemble coverage gain 不足， bifactor fit 不达标，item generation calibration below benchmark。plan_002 RL robustness N=13 在 limitations 诚实披露。plan_029 permutation null 彻底封堵 'is 31% above chance?' 质疑。 全部 robustness check 干净通过，证据链闭环：permutation null → threshold sensitivity → decomposition → NN matching → circularity ablation → multi-benchmark 六层。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a51ab8ce-ea68-4472-a825-8e34be9a6366",
  "type": "user",
  "uuid": "e3c836b0-569e-4615-9b10-dcb39c8c2c28",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:50:23.699Z_

```json
{
  "parentUuid": "e3c836b0-569e-4615-9b10-dcb39c8c2c28",
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
  "uuid": "9dc440fe-fc4a-4ac9-aa1e-16b7b7e778a3",
  "timestamp": "2026-05-21T12:50:23.699Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:50:23.699Z_

```json
{
  "parentUuid": "9dc440fe-fc4a-4ac9-aa1e-16b7b7e778a3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d2684c54-a7bd-4090-8c6e-1c1b3c8d2217",
  "timestamp": "2026-05-21T12:50:23.699Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
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
  "aiTitle": "Generate complete simulated research paper from experiment data",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6"
}
```

---

### Assistant

_source line 7 · 2026-05-21T12:50:26.327Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2684c54-a7bd-4090-8c6e-1c1b3c8d2217",
  "isSidechain": false,
  "requestId": "req_011CbFk3hvDtGGeoggG2WNWK",
  "type": "assistant",
  "uuid": "3b899e6e-a71c-4d63-82e0-875aee9d47ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WccVuNaoqxavqZF9h7h2cM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12373,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12373
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

_source line 8 · 2026-05-21T12:50:27.296Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PPPX6qiQD3TR9j1GCbEwbc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b899e6e-a71c-4d63-82e0-875aee9d47ac",
  "isSidechain": false,
  "requestId": "req_011CbFk3hvDtGGeoggG2WNWK",
  "type": "assistant",
  "uuid": "55cc6fd7-a85e-43eb-bd65-6248c486030d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WccVuNaoqxavqZF9h7h2cM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12373,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12373
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

_source line 9 · 2026-05-21T12:50:27.538Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LD3dhceBg3Sz5qjaPvAe4o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55cc6fd7-a85e-43eb-bd65-6248c486030d",
  "isSidechain": false,
  "requestId": "req_011CbFk3hvDtGGeoggG2WNWK",
  "type": "assistant",
  "uuid": "5a13253a-cd58-4413-808d-dded0431a8d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WccVuNaoqxavqZF9h7h2cM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12373,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12373
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

_source line 10 · 2026-05-21T12:50:27.576Z_

<details><summary>↩ Tool result · `toolu_01LD3dhceBg3Sz5qjaPvAe4o`</summary>

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
  "parentUuid": "5a13253a-cd58-4413-808d-dded0431a8d7",
  "isSidechain": false,
  "promptId": "a51ab8ce-ea68-4472-a825-8e34be9a6366",
  "type": "user",
  "uuid": "87dfd7ad-fa37-4486-b3c7-7d5e329e6cf5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n",
      "numLines": 124,
      "startLine": 1,
      "totalLines": 124
    }
  },
  "sourceToolAssistantUUID": "5a13253a-cd58-4413-808d-dded0431a8d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122440 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "87dfd7ad-fa37-4486-b3c7-7d5e329e6cf5",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper from experiment data",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6"
}
```

---

### Tool result

_source line 13 · 2026-05-21T12:50:27.859Z_

<details><summary>↩ Tool result · `toolu_01PPPX6qiQD3TR9j1GCbEwbc`</summary>

```text
1	[
2	  {
3	    "name": "real_data_dif_mmlu",
4	    "description": "METABENCH MMLU 5219×12508 response matrix MH-DIF 全量分析：temporal/ability cohort、within-family confound control、domain-specificity",
5	    "results": {
6	      "temporal_cohort": {
7	        "n_ref_2023": 1080,
8	        "n_foc_2024h1": 807,
9	        "ets_c_pct": 31.3,
10	        "ets_b_pct": 18.2,
11	        "ets_a_pct": 50.5,
12	        "n_c_items": 3918,
13	        "mean_abs_delta_mh_c_items": 2.31
14	      },
15	      "ability_cohort": {
16	        "ets_c_pct": 2.9,
17	        "enrichment": 1.19
18	      },
19	      "within_family": {
20	        "llama2_vs_llama3_c_pct": 61.3,
21	        "mistral_vs_mixtral_c_pct": 38.7
22	      },
23	      "domain_specificity": {
24	        "spearman_rho_c_pct_vs_acc_delta": 0.307,
25	        "spearman_p": 0.02,
26	        "highest_c_pct_subject": "moral_scenarios (48.4%)",
27	        "lowest_c_pct_subject": "college_biology (20.7%)",
28	        "unweighted_mean_c_pct": 30.0
29	      },
30	      "sanity_checks": {
31	        "random_split_c_pct": 0.18,
32	        "temporal_ability_jaccard": 0.014
33	      },
34	      "li_et_al_proxy": {
35	        "coverage": 0.738,
36	        "enrichment_temporal": 0.96,
37	        "fpr_on_li_clean": 0.318
38	      }
39	    },
40	    "tables": [
41	      "Table 1: Temporal DIF summary — N_ref=1080, N_foc=807, %A/B/C by ETS class, mean |Δ_MH|",
42	      "Table 2: 57-subject domain-specificity — per-subject C%, accuracy delta, sorted descending",
43	      "Table S1: Within-family DIF — Llama-2v3 (N=161 vs 308), Mistral-Mixtral, C%, Jaccard with temporal"
44	    ],
45	    "figures": [],
46	    "analysis": "31.3% 是 paper 的 anchor number。Random split 0.18% 建立了 chance baseline（plan_029 permutation null 将进一步强化）。Ability cohort 的 2.9% 排除了 ability grouping 作为 confound。Domain ρ=0.307 说明 \"模型在某些 domain 进步更多\" 是 factor 之一，但不是主要因素——item-level decomposition (plan_019/030) 证明 DIF 主要是 item-specific。Within-family Llama-2→3 的 61.3% 提供了 capability evolution 的 direct evidence，同时为 plan_027 ability confound 分析铺垫。\n\n\n31.3% C% 反映 genuine temporal item-level functioning changes。三层确认非伪影： (1) random split 仅 0.18%（>170x enrichment ratio 排除统计伪影）； (2) ability cohort C%=2.9%（DIF 由 temporal structure 驱动，非 ability grouping）； (3) temporal-ability Jaccard=0.014（两种 cohort 几乎 flag 完全不同的 items）。 Domain ρ=0.307 (p=0.02) 是 modest ecological correlation；后续 plan_019 item-level decomposition 证明 domain improvement 仅解释 7.6%。Within-family Llama-2→3 的 61.3% 反映跨代 capability jump（d=-0.99, plan_027），而非 contamination artifact—— 同一架构族内 item functioning 剧烈变化说明 capability evolution 是 contributor 之一。 Li et al. enrichment≈0.96 在 meta-critique framing 下是 expected：web-overlap 是 model-agnostic label，DIF 检测的是 model-cohort-differential signal，二者正交。\n"
47	  },
48	  {
49	    "name": "rl_robustness_validation",
50	    "description": "DIF 对 alignment-RL 和 reasoning-RL 模型的鲁棒性验证，含 per-model detector 对比和 power analysis",
51	    "results": {
52	      "alignment_rl_cohort": {
53	        "n_dpo_orpo_models": 477,
54	        "temporal_c_pct_with_alignment_rl": 30.8,
55	        "jaccard_vs_full_temporal": 0.87,
56	        "dif_retention_ratio": 0.94
57	      },
58	      "reasoning_rl_addition": {
59	        "n_reasoning_rl_models": 13,
60	        "models_tested": "DeepSeek-R1-7B, DeepSeek-R1-32B, Qwen2.5-RL-7B/14B/32B, Eurus-RL-7B, PRIME-RL-7B, SimpleRL-7B, DAPO-7B, K1.5-RL, TinyZero-3B, DeepScaleR-1.5B, OpenChat-RL",
61	        "temporal_c_pct_with_rl_added": 31.1,
62	        "jaccard_vs_full_temporal": 0.93,
63	        "c_pct_delta_from_baseline": -0.2
64	      },
65	      "per_model_detectors": {
66	        "constat_auroc_sft": 0.71,
67	        "constat_auroc_alignment_rl": 0.67,
68	        "constat_auroc_reasoning_rl": 0.43,
69	        "mink_auroc_sft": 0.64,
70	        "mink_auroc_alignment_rl": 0.59,
71	        "mink_auroc_reasoning_rl": 0.37,
72	        "delong_p_constat_sft_vs_reasoning_rl": 0.008,
73	        "delong_p_mink_sft_vs_reasoning_rl": 0.003
74	      },
75	      "power_analysis": {
76	        "exploitation_rate_04_tpr": 0.28,
77	        "exploitation_rate_06_tpr": 0.47,
78	        "exploitation_rate_08_tpr": 0.65,
79	        "exploitation_rate_10_tpr": 0.79
80	      },
81	      "tost_equivalence": {
82	        "tost_p": 0.034,
83	        "equivalence_margin": 0.05,
84	        "ci_90_retention_ratio": [
85	          0.89,
86	          0.98
87	        ]
88	      }
89	    },
90	    "tables": [
91	      "Table S2: Per-model detector AUROC — SFT vs alignment-RL vs reasoning-RL，含 bootstrap 95% CI 和 DeLong test",
92	      "Table S3: DIF flag stability across cohort compositions — Jaccard, overlap %, new/lost flags"
93	    ],
94	    "figures": [],
95	    "analysis": "Two-level validation 结论清晰：(1) group-level DIF robust to RL composition（Jaccard≥0.87）； (2) per-model detectors fragile to reasoning RL（AUROC drops 0.25-0.27 points）。 这支持 DIF 的 structural advantage 叙事但 N=13 不足以做 standalone claim。 结论：appendix + limitations，为 future work 留出空间。\n\n\nAlignment RL (DPO/ORPO) 不使用 PPO clipping，NLL 分布不变，DIF 不受影响（Jaccard=0.87）。 0.87 而非 1.0 的原因是 alignment RL 模型在 borderline items 上的 response probability 略有 shift，导致少量 items 在 MH threshold 边缘翻转。13 个 reasoning-RL 模型仅占 focal cohort 1.6%， 加入后 C% 几乎不变（31.1% vs 31.3%），因为 MH 是 group-level 统计量——少量个体对 N=807 的 odds ratio 影响可忽略。传统 per-model detectors 在 reasoning-RL 上 AUROC 大幅下降（ConStat 0.71→0.43, Min-K% 0.64→0.37），因为 GRPO/PPO 训练 contracts NLL gaps（Wang et al. 机制），而 DIF 的 group-level conditioning 天然免疫此问题。但 N=13 使 TOST p=0.034 仅 marginal significant， bootstrap CI 宽（[0.89, 0.98]）。Best tier 处理：direction consistent，但诚实地在 limitations 中报告 N=13 underpowered，不作为 numbered contribution。\n"
96	  },
97	  {
98	    "name": "constat_perturbation_eval",
99	    "description": "ConStat 风格 perturbation testing——250 MMLU items 的语义等价重述 + 检测 power 评估",
100	    "results": {
101	      "reformulation": {
102	        "n_items_reformulated": 250,
103	        "semantic_similarity_mean": 0.92,
104	        "n_models_tested": 50
105	      },
106	      "detection": {
107	        "constat_flagged_pct_non_rl": 19.2,
108	        "constat_flagged_pct_all": 17.8,
109	        "fdr_corrected_flagged_pct": 12.3
110	      },
111	      "comparison_with_dif": {
112	        "jaccard_constat_vs_dif_c": 0.24,
113	        "overlap_pct": 38.2,
114	        "constat_only_pct": 8.1,
115	        "dif_only_pct": 22.4
116	      },
117	      "power_on_semi_synthetic_gt": {
118	        "constat_auroc": 0.68,
119	        "dif_auroc": 0.82
120	      }
121	    },
122	    "tables": [
123	      "Table S4: ConStat detection — flagged % by model class，含 FDR correction",
124	      "Table S5: DIF × ConStat cross-tabulation — Jaccard, Phi, overlap"
125	    ],
126	    "figures": [],
127	    "analysis": "ConStat 提供 complementary signal 但 Jaccard=0.24 说明 ensemble marginal gain 有限。 Detection mechanism 差异（temporal differential vs memorization sensitivity）使两种方法 检测近乎正交的 item 子集。此结果验证 pivot：DIF 作为 diagnostic lens 的独特价值不可被 ConStat 替代，ensemble 不如 DIF alone + robustness checks 有效。\n\n\nConStat 检测 reformulation sensitivity——contaminated 模型对 verbatim 题回答正确但对 rephrased 版性能下降。19.2% 低于 DIF 31.3%，因为：(1) ConStat 仅覆盖 verbatim memorization，partial/variant contamination 不敏感；(2) MMLU 4-choice format 下 reformulation 的 accuracy drop 天然受限 （chance level 25% 提供 floor）；(3) 高质量 paraphrase 的 surface form 变化可能不足以触发 memorization-dependent 模型的 performance shift。Jaccard=0.24 confirms 两种方法检测不同 signal types——DIF 是 temporal differential functioning，ConStat 是 memorization-specific sensitivity。Semi-synthetic ground truth 上 DIF AUROC 更高（0.82 vs 0.68），因为 injected contamination 是 differential exploitation（与 DIF 检测机制对齐），而非 verbatim memorization （与 ConStat 对齐）。结论：complementary but not additive，验证了 ensemble pivot 的正确性。\n"
128	  },
129	  {
130	    "name": "dvd_generation_variance_eval",
131	    "description": "DVD generation variance 评估——12 open-weight models × 50 responses per item 的 variance-based 检测",
132	    "results": {
133	      "setup": {
134	        "n_models_tested": 12,
135	        "n_responses_per_item": 50,
136	        "temperature": 0.8,
137	        "total_inferences": 7512000,
138	        "gpu_hours": 69.6
139	      },
140	      "detection": {
141	        "bimodal_items_pct": 11.8,
142	        "high_variance_items_pct": 15.3,
143	        "dvd_flagged_pct": 13.2
144	      },
145	      "comparison_with_dif": {
146	        "jaccard_dvd_vs_dif_c": 0.16,
147	        "overlap_pct": 29.4
148	      },
149	      "power": {
150	        "dvd_auroc_verbatim_gt": 0.61,
151	        "dvd_auroc_variant_gt": 0.53
152	      }
153	    },
154	    "tables": [
155	      "Table S6: DVD detection — bimodal %, flagged % by model",
156	      "Table S7: DVD vs DIF cross-tabulation"
157	    ],
158	    "figures": [],
159	    "analysis": "DVD 单独使用 power 不足，且需要 ~70 GPU hours + open-weight access。 Jaccard=0.16 说明 ensemble 增益极小。结果验证了 ensemble pivot 正确性： 三种方法的 detection mechanisms 过于异质，无法有效融合。\n\n\nDVD 依赖 contaminated items 产生 bimodal generation distribution（memorized answer vs random）。 11.8% bimodal 低于 DIF 31.3%，因为：(1) bimodality 仅在 extreme verbatim memorization 下出现， partial exploitation 产生 unimodal 但 shifted distribution；(2) MMLU 4-choice format 的 discrete nature 限制了 generation variance 的 discriminative range——even uncontaminated items 在 temperature sampling 下产生 high variance；(3) requires open-weight access，排除 proprietary models。Jaccard=0.16 极低，confirms DVD 和 DIF 检测几乎完全不同的 item subsets。 AUROC 对比：DVD verbatim 0.61（moderate），variant 0.53（near chance）。Variant contamination detection 接近 chance 因为 paraphrased memorization 不产生 bimodal pattern。\n"
160	  },
161	  {
162	    "name": "ensemble_fusion",
163	    "description": "DIF + ConStat + DVD 三信号融合：majority voting + weighted fusion",
164	    "results": {
165	      "majority_voting_2of3": {
166	        "tpr": 0.35,
167	        "fpr": 0.08,
168	        "f1": 0.38
169	      },
170	      "weighted_fusion": {
171	        "optimal_weights": {
172	          "dif": 0.58,
173	          "constat": 0.27,
174	          "dvd": 0.15
175	        },
176	        "tpr": 0.43,
177	        "fpr": 0.09,
178	        "f1": 0.43,
179	        "cross_val_weight_cv": 0.34
180	      },
181	      "dif_alone_reference": {
182	        "tpr": 0.51,
183	        "fpr": 0.31
184	      },
185	      "coverage_gain_over_dif_pp": 4.2,
186	      "all_ensemble_fpr_below_010": true
187	    },
188	    "tables": [
189	      "Table S8: Ensemble configs — 2-of-3, weighted, DIF-alone，含 95% CI"
190	    ],
191	    "figures": [],
192	    "analysis": "Ensemble 核心问题是三种方法的 signal incommensurability 而非 signal complementarity。 Best tier 下此 negative result 加强了 pivot 叙事：DIF 的 diagnostic lens 价值在于其 独特的 temporal-differential perspective，不需要也不应与其他 mechanism 融合。 Goes to appendix as informative negative result。\n\n\n2-of-3 majority voting TPR 仅 0.35，因为 pairwise Jaccard 0.16-0.24 导致三方法 consensus items 极少——三种方法各自检测不同 signal（temporal differential, memorization sensitivity, generation bimodality），overlap 不足以构建有效 consensus。Weighted fusion 略好（TPR=0.43） 但 cross-validation weight stability 差（CV=0.34），因为 calibration set 有限（semi-synthetic ground truth 200 items）且三种方法 error profiles 不 correlated。DIF alone TPR=0.51 高于 任何 ensemble configuration，因为 high-recall 方法被 ensemble consensus requirement 削弱。 Coverage gain 仅 +4.2pp 不 justify 额外 150 GPU hours 和 open-weight 依赖。\n"
193	  },
194	  {
195	    "name": "cross_benchmark_gsm8k",
196	    "description": "GSM8K DIF 复制 + semi-synthetic 验证 + GSM1K contamination gap 相关",
197	    "results": {
198	      "step1_temporal_dif": {
199	        "n_items": 1319,
200	        "n_ref": 1017,
201	        "n_foc": 804,
202	        "standard_c_pct": 18.9,
203	        "external_c_pct": 47.4,
204	        "sanity_c_pct": 0.3,
205	        "standard_external_spearman": 0.926
206	      },
207	      "step2_semi_synthetic": {
208	        "standard_delta_tpr_p10": 0.818,
209	        "external_delta_tpr_p10": 0.517,
210	        "standard_delta_tpr_p05": 0.508
211	      },
212	      "step3_gsm1k_correlation": {
213	        "n_models": 33,
214	        "pearson_r": -0.478,
215	        "pearson_p": 0.005,
216	        "spearman_rho": -0.403,
217	        "spearman_p": 0.02,
218	        "partial_r_controlling_accuracy": -0.385,
219	        "partial_p": 0.027,
220	        "permutation_p": 0.014,
221	        "direction": "NEGATIVE — opposite to contamination hypothesis",
222	        "leave_one_out_r_range": [
223	          -0.537,
224	          -0.374
225	        ]
226	      }
227	    },
228	    "tables": [
229	      "Table 4: GSM8K temporal DIF — C% with standard/external matching, random control",
230	      "Table S9: GSM1K correlation — Pearson/Spearman/partial r，含 leave-one-out robustness"
231	    ],
232	    "figures": [],
233	    "analysis": "GSM8K 复制验证 framework portability（ΔTPR=+0.818）和 temporal DIF pattern（18.9% vs random 0.3%）。 GSM1K negative correlation 在 best tier 下 demote to appendix exploratory（N=33, CI wide）。 This result doesn't weaken any claim — it strengthens the meta-critique by empirically demonstrating DIF and contamination labels capture different signals。\n\n\nGSM8K temporal C%=18.9% 低于 MMLU 31.3%，因为 GSM8K 是 single math domain（1,319 items）， item 功能相对 homogeneous，temporal change 集中在特定难度段而非 broad capability shift。 Semi-synthetic ΔTPR=+0.818 高于 MMLU 0.674，因为 GSM8K 更 unidimensional（单一 math 能力维度）， MH 的 unidimensional conditioning 更 appropriate，injection 更 cleanly detected。 GSM1K correlation r=-0.478 方向 opposite to contamination hypothesis：DIF 更多 flag 的模型 有更小的 GSM8K-GSM1K gap。这并不矛盾——DIF flags items whose difficulty changed across cohorts （78% favor 2024），而 small GSM8K-GSM1K gap 的模型恰恰是 genuine capability improvement 最强的（GSM1K 也难，real ability gains transfer）。This anti-correlation 实际上加强了 Claim 2 meta-critique：DIF 和 contamination ground truth 测量的是 different constructs。\n"
234	  },
235	  {
236	    "name": "bifactor_irt_equating_pilot",
237	    "description": "Bifactor IRT equating pilot——验证 MMLU 上 psychometric equating 可行性",
238	    "results": {
239	      "model_fit": {
240	        "unidimensional_rmsea": 0.121,
241	        "unidimensional_cfi": 0.776,
242	        "bifactor_5group_rmsea": 0.094,
243	        "bifactor_5group_cfi": 0.841,
244	        "bifactor_full_57_convergence": false,
245	        "bifactor_full_57_error": "non-positive definite Hessian after 500 EM iterations"
246	      },
247	      "anchor_selection": {
248	        "dif_free_items_pct": 17.3,
249	        "n_anchors_meeting_criteria": 2163,
250	        "anchor_icc_concordance": 0.82
251	      },
252	      "equating_attempt": {
253	        "equated_rho": 0.91,
254	        "target_rho": 0.95,
255	        "shortfall": 0.04
256	      },
257	      "decision": "KILLED — bifactor fit insufficient (RMSEA=0.094>0.05), equated rho=0.91 < target 0.95"
258	    },
259	    "tables": [
260	      "Table S10: IRT fit comparison — unidimensional vs 5-group bifactor vs full bifactor"
261	    ],
262	    "figures": [],
263	    "analysis": "Informative negative result。说明传统 psychometric equating 不能直接迁移到 LLM multi-domain benchmarks：extreme multidimensionality violates essential unidimensionality assumption。 加强 diagnostic lens framing——DIF 的价值不在于 equating-based item replacement， 而在于 understanding what changed。在 limitations 中自然 motivate future multidimensional IRT。\n\n\nMMLU 57-subject 结构使 full bifactor（1 general + 57 specific）在计算上不可行—— non-positive definite Hessian 因为 57 specific factors 导致 identification 问题（many subjects 仅 100 items，insufficient for factor estimation）。Reduced 5-group bifactor 改善有限 （RMSEA 0.121→0.094, CFI 0.776→0.841），仍远低于 acceptable fit thresholds。根本原因是 MMLU 内在 multidimensionality：从 abstract_algebra 到 world_religions 的 57 domains 无法 被 1 general factor + few group factors 充分 capture。Equating pilot 在 suboptimal fit 下 仍尝试：anchors 数量足够（2,163 items），但 misspecified ability estimates 传播到 fixed-parameter calibration，导致 equated rho=0.91 低于 target 0.95。Kill decision 正确—— 此 negative result 在 limitations 中作为 future multidimensional IRT work 的 motivation。\n"
264	  },
265	  {
266	    "name": "item_generation_calibration",
267	    "description": "DIF-flagged MMLU items 的 LLM-based 替代 item 生成与难度校准",
268	    "results": {
269	      "generation": {
270	        "n_items_generated": 400,
271	        "n_subjects": 10,
272	        "construct_adherence_human_eval": 0.784
273	      },
274	      "difficulty_calibration": {
275	        "prompt_based_rho": 0.38,
276	        "student_sim_rho": 0.52,
277	        "target_rho": 0.75
278	      },
279	      "quality": {
280	        "human_quality_score_mean": 3.2,
281	        "human_quality_target": 4.0,
282	        "holdout_panel_rho": 0.48
283	      },
284	      "decision": "BELOW BENCHMARKS — best difficulty rho=0.52 vs target 0.75"
285	    },
286	    "tables": [
287	      "Table S11: Difficulty calibration — prompt vs student-sim vs empirical，含 95% CI"
288	    ],
289	    "figures": [],
290	    "analysis": "有价值的 negative result——说明 \"just regenerate flagged items\" 不是 trivial solution。 加强 diagnostic lens framing：DIF 的 actionable value 是 audit protocol + informed maintenance， 而非 automated regeneration。在 Discussion 中可用于回应 reviewer 的 \"so what do we do?\" question。\n\n\nDifficulty calibration 是 item generation 的瓶颈。Prompt-based targeting（直接指定 difficulty level） rho=0.38，因为 LLM 对 \"difficulty for other LLMs\" 的 internal calibration 与 empirical difficulty 几乎无关——difficulty 由 knowledge coverage, reasoning depth, distractor quality 联合决定， 非 LLM 自身 uncertainty 可预测。Student simulation 改善到 rho=0.52，但 arXiv 2601.09953 的 r=0.75-0.82 是在 human exam items 上报告的，LLM benchmark items 的 difficulty determinants 不同（e.g., MMLU 多选的 distractor 设计对 LLM 和 human 的 difficulty contribution 不同）。 Construct fidelity 78.4% 说明 22% 的 generated items 有 subject drift 或 cognitive level 错误。 Plan_005 被 kill 后，本 plan 失去 equating framework 支撑。\n"
291	  },
292	  {
293	    "name": "cumulative_bayesian_dif",
294	    "description": "Sinharay et al. (2006) cumulative Bayesian DIF priors 的 4-administration simulation",
295	    "results": {
296	      "setup": {
297	        "n_administrations": 4,
298	        "n_items_per_sim": 500,
299	        "n_models_per_admin": 200,
300	        "true_dif_items": 100,
301	        "delta_range": [
302	          0.8,
303	          1.8
304	        ]
305	      },
306	      "power_accumulation": {
307	        "tpr_admin1_d10": 0.41,
308	        "tpr_admin2_d10": 0.58,
309	        "tpr_admin3_d10": 0.72,
310	        "tpr_admin4_d10": 0.81,
311	        "tpr_admin1_d08": 0.22,
312	        "tpr_admin2_d08": 0.38,
313	        "tpr_admin3_d08": 0.53,
314	        "tpr_admin4_d08": 0.65
315	      },
316	      "fpr_stability": {
317	        "fpr_range": [
318	          0.042,
319	          0.045
320	        ]
321	      },
322	      "bayesian_shrinkage": {
323	        "posterior_sd_admin4": 0.31
324	      }
325	    },
326	    "tables": [
327	      "Table S12: Cumulative power — TPR at δ=0.8/1.0/1.4/1.8 × 1-4 administrations"
328	    ],
329	    "figures": [],
330	    "analysis": "Clean simulation 支持 audit protocol 的 operational recommendation：每 6 月 DIF assessment， 3 次累积后 medium effects 的 power 从 0.41 升至 0.72。Goes to appendix，在 Discussion 中 referenced。\n\n\nBayesian evidence accumulation 的 power gain 等价于 effectively increasing sample precision。 δ=1.0 时单次 TPR=0.41（与 phase2 sim 的 N=80 结果一致），4 次累积达 0.81——posterior SD 从 1.0 shrink 到 0.31，precision quadruples。对 small effects（δ=0.8），MH 单次几乎无法检测 （TPR=0.22），但 4 次累积达 0.65——这是 monitoring protocol 的核心理论支撑。 FPR 稳定在 ~0.043 因为 Bayesian shrinkage 对 null items 同样有效（posterior for null items 集中在 0 附近）。Simulation-only 但为 audit protocol 的 monitoring frequency 建议提供 quantitative basis。\n"
331	  },
332	  {
333	    "name": "graceful_degradation_analysis",
334	    "description": "Benchmark validity 在 progressive item removal 下的降级分析",
335	    "results": {
336	      "progressive_removal": {
337	        "pct_5": {
338	          "ranking_rho": 0.9998,
339	          "reliability_alpha": 0.993,
340	          "construct_jaccard": 0.98
341	        },
342	        "pct_10": {
343	          "ranking_rho": 0.9994,
344	          "reliability_alpha": 0.991,
345	          "construct_jaccard": 0.96
346	        },
347	        "pct_20": {
348	          "ranking_rho": 0.9987,
349	          "reliability_alpha": 0.987,
350	          "construct_jaccard": 0.92
351	        },
352	        "pct_31": {
353	          "ranking_rho": 0.9965,
354	          "reliability_alpha": 0.982,
355	          "construct_jaccard": 0.87
356	        },
357	        "pct_50": {
358	          "ranking_rho": 0.9912,
359	          "reliability_alpha": 0.971,
360	          "construct_jaccard": 0.78
361	        }
362	      },
363	      "theoretical_match": {
364	        "spearman_brown_predicted_rho_31pct": 0.9968,
365	        "empirical_rho_31pct": 0.9965,
366	        "gap": 0.0003
367	      }
368	    },
369	    "tables": [
370	      "Table S13: Progressive degradation — rho, reliability, coverage at 5/10/20/31/50%"
371	    ],
372	    "figures": [],
373	    "analysis": "直接支持 \"instability ≠ invalidity\" 叙事。31% instability 不威胁 validity（rho=0.997） 因为 MMLU 的 massive redundancy。Headline number 进 main text，full curve 进 appendix。\n\n\nMMLU 12,508 items 的 massive redundancy 决定了 removal 的 graceful degradation。 Spearman-Brown formula 预测 test length 缩减 31% 时 rho 从 ~1.0 降至 0.9968—— empirical 0.9965 精确匹配，说明 degradation 完全由 test shortening 驱动，无 systematic bias（DIF items 不是 systematically more informative for ranking）。Construct coverage 降速快于 ranking stability，因为 DIF items 在 domains 间非均匀分布（moral_scenarios 48.4% vs college_biology 20.7%），high-DIF domains 在 removal 后 coverage 受损更大。 与 plan_017 实际结果（rho=0.997 at 31%）高度一致。\n"
374	  },
375	  {
376	    "name": "item_focused_trees",
377	    "description": "Item-Focused Trees（Tutz & Berger 2016）——连续时间 DIF 作为 MH categorical split 的 robustness check",
378	    "results": {
379	      "detection": {
380	        "ift_flagged_pct": 28.7,
381	        "jaccard_ift_vs_mh_c": 0.78,
382	        "ift_only_pct": 4.2,
383	        "mh_only_pct": 6.8
384	      },
385	      "temporal_patterns": {
386	        "single_changepoint_pct": 71,
387	        "multiple_changepoints_pct": 12,
388	        "gradual_drift_pct": 17,
389	        "median_changepoint": "2023-09"
390	      },
391	      "tree_structure": {
392	        "mean_terminal_nodes": 5.2,
393	        "max_depth": 3
394	      }
395	    },
396	    "tables": [
397	      "Table S14: IFT vs MH concordance — Jaccard, overlap, unique flags",
398	      "Table S15: Changepoint timing distribution by quarter"
399	    ],
400	    "figures": [],
401	    "analysis": "Confirms MH categorical split robustness（Jaccard=0.78）。Changepoint timing 提供 temporal granularity，在 Discussion 中简要引用。Appendix robustness check。\n\n\nIFT 用 continuous release date 替代 MH 的 binary temporal split，避免 arbitrary cutoff。 28.7% vs MH 31.3% 的差异来自 tree-based multiple testing correction（node-level significance threshold）vs MH 的 per-item testing。Jaccard=0.78 高一致性说明 MH categorical split captures the main temporal signal。IFT 的独特 value 是 changepoint timing：71% items 有 single changepoint（median 2023-09，对应 Llama-2/Mistral/Phi-1 release 密集期）， 12% 有 multiple changepoints（progressive drift），17% gradual drift。Timing information 支持 Discussion 中的 \"what drives instability\" narrative——major model releases 是 item functioning change 的 primary driver。\n"
402	  },
403	  {
404	    "name": "architecture_stratified_dif",
405	    "description": "Architecture-homogeneous subpopulation DIF——验证 architecture heterogeneity 非 confound",
406	    "results": {
407	      "metabench_composition": {
408	        "total_models": 5227,
409	        "decoder_only": 5226,
410	        "decoder_only_pct": 99.98,
411	        "non_decoder": 1,
412	        "non_decoder_id": "flan-ul2"
413	      },
414	      "dif_comparison": {
415	        "decoder_only_c_pct": 31.3,
416	        "full_c_pct": 31.3,
417	        "jaccard": 1.0,
418	        "items_changed": 0
419	      },
420	      "irt_fit": {
421	        "full_rmsea": 0.121,
422	        "decoder_only_rmsea": 0.121,
423	        "delta_rmsea": 0.0
424	      }
425	    },
426	    "tables": [
427	      "Table S16: Architecture composition"
428	    ],
429	    "figures": [],
430	    "analysis": "One-line main text defense。IRT misfit 重定向至 limitations（multidimensionality motivation）。\n\n\nMETABENCH MMLU 的 architecture homogeneity 使本实验成为 trivial pass：99.98% decoder-only， 唯一的 encoder-decoder (flan-ul2) 在 N=5227 中的影响可忽略。Jaccard=1.0 意味着 zero items 的 DIF classification 因 architecture stratification 而改变。IRT fit 同样不变 （RMSEA=0.121），因为 misfit 源自 57-subject multidimensionality 而非 architecture heterogeneity。 这是 ideal robustness result：potential confound 被 data composition 自然消除。\n"
431	  },
432	  {
433	    "name": "semi_synthetic_contamination_validation",
434	    "description": "Known contamination injection 进 real response matrix + DIF detection power 评估 + cross-subject matching 验证",
435	    "results": {
436	      "temporal_external_matching": {
437	        "baseline_fpr": 0.314,
438	        "tpr_p00": 0.326,
439	        "tpr_p03": 0.548,
440	        "tpr_p05": 0.834,
441	        "tpr_p07": 0.99,
442	        "tpr_p10": 1.0,
443	        "delta_tpr_p05": 0.508,
444	        "delta_tpr_p10": 0.674
445	      },
446	      "ability_external_matching": {
447	        "baseline_fpr": 0.493,
448	        "tpr_p10": 0.8,
449	        "delta_tpr_p10": 0.302
450	      },
451	      "matching_variable_contamination": {
452	        "standard_fpr_p10": 0.616,
453	        "standard_fpr_baseline": 0.298,
454	        "fpr_inflation": 0.318,
455	        "cross_subject_fpr_inflation": 0.0
456	      },
457	      "cross_subject_5subj_validation": {
458	        "delta_fpr_all_subjects": 0.0,
459	        "avg_delta_tpr_p05": 0.508,
460	        "subjects_passing_p05": "4/5"
461	      }
462	    },
463	    "tables": [
464	      "Table 5: Semi-synthetic ΔTPR/ΔFPR across exploitation rates and matching strategies",
465	      "Table 6: Standard vs cross-subject matching FPR comparison"
466	    ],
467	    "figures": [],
468	    "analysis": "ΔTPR=+0.508 是 Claim 3 headline。Cross-subject ΔFPR=0.000 是 key methodological novelty。 Dose-response pattern 提供 internal validity。Both metrics 在 best tier range 内。\n\n\nSemi-synthetic injection 在 real response matrix 上创造 controlled ground truth—— 对 focal cohort 的 known-clean items 执行 incorrect→correct flipping with probability p。 ΔTPR=+0.508 at p=0.5 在 best tier [0.45, 0.55] range 内，confirms DIF detects moderate differential contamination。Dose-response（p=0.3→0.5→0.7→1.0 对应 TPR 0.55→0.83→0.99→1.0） 增强因果推断。关键 methodological finding：standard MH matching（total score 含 contaminated items） 导致 FPR inflation +0.318（matching variable contamination），而 cross-subject matching （other subjects 的 total score）完全消除 inflation（ΔFPR=0.000）。Cross-subject matching works 因为 contamination 是 subject-specific（inject 进特定 subject），而 other subjects 的 total score 不受 contamination 影响，保持 conditioning variable 的 exchangeability。\n"
469	  },
470	  {
471	    "name": "multi_benchmark_temporal_dif",
472	    "description": "6 benchmarks temporal DIF——cross-benchmark generalizability 验证",
473	    "results": {
474	      "mmlu": {
475	        "n_items": 12508,
476	        "n_ref": 1080,
477	        "n_foc": 807,
478	        "pct_c": 31.3,
479	        "random_pct_c": 0.18
480	      },
481	      "winogrande": {
482	        "n_items": 1267,
483	        "n_ref": 1017,
484	        "n_foc": 803,
485	        "pct_c": 30.3,
486	        "random_pct_c": 0.32
487	      },
488	      "truthfulqa": {
489	        "n_items": 817,
490	        "n_ref": 1080,
491	        "n_foc": 807,
492	        "pct_c": 29.7,
493	        "random_pct_c": 0.37
494	      },
495	      "arc": {
496	        "n_items": 1172,
497	        "n_ref": 1080,
498	        "n_foc": 807,
499	        "pct_c": 26.9,
500	        "random_pct_c": 0.6
501	      },
502	      "gsm8k": {
503	        "n_items": 1319,
504	        "n_ref": 1017,
505	        "n_foc": 804,
506	        "pct_c": 18.9,
507	        "random_pct_c": 0.3
508	      },
509	      "hellaswag": {
510	        "n_items": 10042,
511	        "n_ref": 1080,
512	        "n_foc": 807,
513	        "pct_c": 17.9,
514	        "random_pct_c": 0.28
515	      },
516	      "summary": {
517	        "range": "17.9–31.3%",
518	        "all_random_below_1pct": true,
519	        "min_enrichment_ratio": 44.8,
520	        "mean_c_pct": 25.8,
521	        "n_benchmarks": 6
522	      }
523	    },
524	    "tables": [
525	      "Table 3: Cross-benchmark temporal DIF — 6 rows, N_items/N_ref/N_foc/C%/random%"
526	    ],
527	    "figures": [],
528	    "analysis": "Cross-benchmark consistency 是 Claim 1 generalizability 最强证据。17.9-31.3% range 在 best tier [17.0, 32.0] 内。Claim 1 statement 可升级为 \"17.9-31.3% across 6 major benchmarks\"。\n\n\n6 benchmarks 一致显示 temporal DIF 远超 chance（enrichment 45-174×），确认 temporal item instability 是 LLM benchmark 的 general phenomenon。C% ordering 反映 benchmark 结构： MMLU（57 domains, maximal multidimensionality）和 WinoGrande（commonsense reasoning, capability-sensitive） 最高；HellaSwag（sentence completion, more pattern-matching than reasoning）和 GSM8K （single math domain）最低。低 C% benchmarks 的 items 功能更 homogeneous across model generations ——sentence completion patterns evolve less than knowledge/reasoning items。 All random controls <1% 排除 statistical artifact across all benchmarks。\n"
529	  },
530	  {
531	    "name": "permutation_null_c_rate",
532	    "description": "1000× permutation test——temporal label shuffling 下的 C% null distribution",
533	    "results": {
534	      "null_distribution": {
535	        "n_permutations": 1000,
536	        "mean_c_pct": 0.21,
537	        "sd_c_pct": 0.11,
538	        "median_c_pct": 0.19,
539	        "q95_c_pct": 0.42,
540	        "q99_c_pct": 0.54,
541	        "max_c_pct": 0.71
542	      },
543	      "significance": {
544	        "observed_c_pct": 31.3,
545	        "z_score": 282.6,
546	        "empirical_p": "<0.001 (0/1000 exceed observed)",
547	        "ratio_observed_to_null_mean": 149
548	      },
549	      "consistency": {
550	        "random_split_c_pct": 0.18,
551	        "permutation_null_mean": 0.21,
552	        "convergent": true
553	      }
554	    },
555	    "tables": [
556	      "Table 7: Permutation null — mean/SD/Q95/Q99/max vs observed，z-score，p-value"
557	    ],
558	    "figures": [],
559	    "analysis": "Best tier 的 critical robustness check。Null C% mean=0.21% 在 [0.0, 1.0] range 内。 z=282.6 使 temporal DIF signal 成为 unambiguous。与 random-split 的 convergence 提供 double confirmation。This goes into main text as primary robustness evidence alongside threshold sensitivity（plan_018）and decomposition（plan_019）。\n\n\nPermutation null 通过 random temporal label reassignment（保持 N_ref=1080, N_foc=807） 建立 chance baseline。Mean 0.21% 与 random split 0.18% convergent，因为两者本质上 measure the same thing：无 temporal structure 时的 spurious DIF rate。0.21% vs 0.18% 微小差异来自 permutation 使用 full N=1887（random split 在 single cohort ~1000 内）。Observed 31.3% 给出 z=282.6——0/1000 permutations exceed，empirical p<0.001。这是因为 temporal structure 是 genuine signal：2023 和 2024 model cohorts 确实在 item-level functioning 上不同。 Permutation destroys this temporal structure，restoring C% to chance level (~0.2%)。 149× enrichment over null 彻底回答 \"is 31% above chance?\"。\n"
560	  },
561	  {
562	    "name": "odds_ratio_regression_transparency",
563	    "description": "多层 logistic regression——OR + CI + McFadden/Nagelkerke R² + Simpson's paradox 展示",
564	    "results": {
565	      "model1_domain_delta": {
566	        "mcfadden_r2": 0.0007,
567	        "nagelkerke_r2": 0.0012,
568	        "aic": 15545.2,
569	        "or_per_010": 1.55,
570	        "or_ci_per_010": [
571	          1.19,
572	          2.03
573	        ]
574	      },
575	      "model2_domain_plus_items": {
576	        "mcfadden_r2": 0.0423,
577	        "nagelkerke_r2": 0.072,
578	        "aic": 14902.3,
579	        "subject_delta_or_per_010": 0.73,
580	        "difficulty_or_per_010": 0.78,
581	        "discrimination_or_per_010": 1.51
582	      },
583	      "model3_item_delta": {
584	        "mcfadden_r2": 0.0012,
585	        "nagelkerke_r2": 0.0021,
586	        "aic": 15536.9,
587	        "or": 2.11,
588	        "or_ci": [
589	          1.51,
590	          2.96
591	        ]
592	      },
593	      "model4_best": {
594	        "mcfadden_r2": 0.0434,
595	        "nagelkerke_r2": 0.0737,
596	        "aic": 14885.4,
597	        "item_delta_or_per_010": 0.92,
598	        "difficulty_or_per_010": 0.77,
599	        "discrimination_or_per_010": 1.54
600	      },
601	      "simpsons_paradox": true,
602	      "lr_test_m1_vs_m2_chi2": 646.98,
603	      "lr_test_m3_vs_m4_chi2": 655.53
604	    },
605	    "tables": [
606	      "Table S17: Four-model regression summary — OR, 95% CI, R², AIC, deviance",
607	      "Table S18: Simpson's paradox — Model 1 vs Model 2 coefficient sign reversal"
608	    ],
609	    "figures": [],
610	    "analysis": "Full transparency supplement for plan_019 decomposition。Simpson's paradox 是 methodological cautionary tale：naive domain-level analysis (OR=1.55) overestimates improvement's contribution， item-level conditioning (OR=0.73) reveals the truth。Model 1 作为 primary（conservative）， Simpson's paradox 在 appendix 详述。R²=0.0007 是 \"≤7.6% explained\" claim 的 additional support。\n\nFour-model architecture 揭示 Simpson's paradox：accuracy improvement 的 OR 从 Model 1 的 1.55 （正相关：improved domains 有更多 DIF）reversal 到 Model 2 的 0.73（负相关：controlling for item properties 后 improvement 反而 associated with less DIF）。Paradox 成因：DIF items 更难（d=-0.247, plan_023）且 higher-discrimination（d=0.230），而这些 item properties 同时 与 accuracy change 相关（difficult domains 有 larger improvement headroom）。 Model 1 的 R²=0.0007 confirms accuracy improvement 几乎不解释 DIF variance——绝大部分 DIF 是 item-specific 而非 domain improvement 的 proxy。Model 4 R²=0.0434 shows item intrinsic properties（difficulty, discrimination）解释了 >98% 的 explainable variance。 LR test（χ²=647-656, p<0.001）confirms adding item properties 显著改善 fit。\n"
611	  }
612	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55cc6fd7-a85e-43eb-bd65-6248c486030d",
  "isSidechain": false,
  "promptId": "a51ab8ce-ea68-4472-a825-8e34be9a6366",
  "type": "user",
  "uuid": "6109f89b-25f6-482a-bb23-2382896927dc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"real_data_dif_mmlu\",\n    \"description\": \"METABENCH MMLU 5219×12508 response matrix MH-DIF 全量分析：temporal/ability cohort、within-family confound control、domain-specificity\",\n    \"results\": {\n      \"temporal_cohort\": {\n        \"n_ref_2023\": 1080,\n        \"n_foc_2024h1\": 807,\n        \"ets_c_pct\": 31.3,\n        \"ets_b_pct\": 18.2,\n        \"ets_a_pct\": 50.5,\n        \"n_c_items\": 3918,\n        \"mean_abs_delta_mh_c_items\": 2.31\n      },\n      \"ability_cohort\": {\n        \"ets_c_pct\": 2.9,\n        \"enrichment\": 1.19\n      },\n      \"within_family\": {\n        \"llama2_vs_llama3_c_pct\": 61.3,\n        \"mistral_vs_mixtral_c_pct\": 38.7\n      },\n      \"domain_specificity\": {\n        \"spearman_rho_c_pct_vs_acc_delta\": 0.307,\n        \"spearman_p\": 0.02,\n        \"highest_c_pct_subject\": \"moral_scenarios (48.4%)\",\n        \"lowest_c_pct_subject\": \"college_biology (20.7%)\",\n        \"unweighted_mean_c_pct\": 30.0\n      },\n      \"sanity_checks\": {\n        \"random_split_c_pct\": 0.18,\n        \"temporal_ability_jaccard\": 0.014\n      },\n      \"li_et_al_proxy\": {\n        \"coverage\": 0.738,\n        \"enrichment_temporal\": 0.96,\n        \"fpr_on_li_clean\": 0.318\n      }\n    },\n    \"tables\": [\n      \"Table 1: Temporal DIF summary — N_ref=1080, N_foc=807, %A/B/C by ETS class, mean |Δ_MH|\",\n      \"Table 2: 57-subject domain-specificity — per-subject C%, accuracy delta, sorted descending\",\n      \"Table S1: Within-family DIF — Llama-2v3 (N=161 vs 308), Mistral-Mixtral, C%, Jaccard with temporal\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"31.3% 是 paper 的 anchor number。Random split 0.18% 建立了 chance baseline（plan_029 permutation null 将进一步强化）。Ability cohort 的 2.9% 排除了 ability grouping 作为 confound。Domain ρ=0.307 说明 \\\"模型在某些 domain 进步更多\\\" 是 factor 之一，但不是主要因素——item-level decomposition (plan_019/030) 证明 DIF 主要是 item-specific。Within-family Llama-2→3 的 61.3% 提供了 capability evolution 的 direct evidence，同时为 plan_027 ability confound 分析铺垫。\\n\\n\\n31.3% C% 反映 genuine temporal item-level functioning changes。三层确认非伪影： (1) random split 仅 0.18%（>170x enrichment ratio 排除统计伪影）； (2) ability cohort C%=2.9%（DIF 由 temporal structure 驱动，非 ability grouping）； (3) temporal-ability Jaccard=0.014（两种 cohort 几乎 flag 完全不同的 items）。 Domain ρ=0.307 (p=0.02) 是 modest ecological correlation；后续 plan_019 item-level decomposition 证明 domain improvement 仅解释 7.6%。Within-family Llama-2→3 的 61.3% 反映跨代 capability jump（d=-0.99, plan_027），而非 contamination artifact—— 同一架构族内 item functioning 剧烈变化说明 capability evolution 是 contributor 之一。 Li et al. enrichment≈0.96 在 meta-critique framing 下是 expected：web-overlap 是 model-agnostic label，DIF 检测的是 model-cohort-differential signal，二者正交。\\n\"\n  },\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"DIF 对 alignment-RL 和 reasoning-RL 模型的鲁棒性验证，含 per-model detector 对比和 power analysis\",\n    \"results\": {\n      \"alignment_rl_cohort\": {\n        \"n_dpo_orpo_models\": 477,\n        \"temporal_c_pct_with_alignment_rl\": 30.8,\n        \"jaccard_vs_full_temporal\": 0.87,\n        \"dif_retention_ratio\": 0.94\n      },\n      \"reasoning_rl_addition\": {\n        \"n_reasoning_rl_models\": 13,\n        \"models_tested\": \"DeepSeek-R1-7B, DeepSeek-R1-32B, Qwen2.5-RL-7B/14B/32B, Eurus-RL-7B, PRIME-RL-7B, SimpleRL-7B, DAPO-7B, K1.5-RL, TinyZero-3B, DeepScaleR-1.5B, OpenChat-RL\",\n        \"temporal_c_pct_with_rl_added\": 31.1,\n        \"jaccard_vs_full_temporal\": 0.93,\n        \"c_pct_delta_from_baseline\": -0.2\n      },\n      \"per_model_detectors\": {\n        \"constat_auroc_sft\": 0.71,\n        \"constat_auroc_alignment_rl\": 0.67,\n        \"constat_auroc_reasoning_rl\": 0.43,\n        \"mink_auroc_sft\": 0.64,\n        \"mink_auroc_alignment_rl\": 0.59,\n        \"mink_auroc_reasoning_rl\": 0.37,\n        \"delong_p_constat_sft_vs_reasoning_rl\": 0.008,\n        \"delong_p_mink_sft_vs_reasoning_rl\": 0.003\n      },\n      \"power_analysis\": {\n        \"exploitation_rate_04_tpr\": 0.28,\n        \"exploitation_rate_06_tpr\": 0.47,\n        \"exploitation_rate_08_tpr\": 0.65,\n        \"exploitation_rate_10_tpr\": 0.79\n      },\n      \"tost_equivalence\": {\n        \"tost_p\": 0.034,\n        \"equivalence_margin\": 0.05,\n        \"ci_90_retention_ratio\": [\n          0.89,\n          0.98\n        ]\n      }\n    },\n    \"tables\": [\n      \"Table S2: Per-model detector AUROC — SFT vs alignment-RL vs reasoning-RL，含 bootstrap 95% CI 和 DeLong test\",\n      \"Table S3: DIF flag stability across cohort compositions — Jaccard, overlap %, new/lost flags\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Two-level validation 结论清晰：(1) group-level DIF robust to RL composition（Jaccard≥0.87）； (2) per-model detectors fragile to reasoning RL（AUROC drops 0.25-0.27 points）。 这支持 DIF 的 structural advantage 叙事但 N=13 不足以做 standalone claim。 结论：appendix + limitations，为 future work 留出空间。\\n\\n\\nAlignment RL (DPO/ORPO) 不使用 PPO clipping，NLL 分布不变，DIF 不受影响（Jaccard=0.87）。 0.87 而非 1.0 的原因是 alignment RL 模型在 borderline items 上的 response probability 略有 shift，导致少量 items 在 MH threshold 边缘翻转。13 个 reasoning-RL 模型仅占 focal cohort 1.6%， 加入后 C% 几乎不变（31.1% vs 31.3%），因为 MH 是 group-level 统计量——少量个体对 N=807 的 odds ratio 影响可忽略。传统 per-model detectors 在 reasoning-RL 上 AUROC 大幅下降（ConStat 0.71→0.43, Min-K% 0.64→0.37），因为 GRPO/PPO 训练 contracts NLL gaps（Wang et al. 机制），而 DIF 的 group-level conditioning 天然免疫此问题。但 N=13 使 TOST p=0.034 仅 marginal significant， bootstrap CI 宽（[0.89, 0.98]）。Best tier 处理：direction consistent，但诚实地在 limitations 中报告 N=13 underpowered，不作为 numbered contribution。\\n\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"ConStat 风格 perturbation testing——250 MMLU items 的语义等价重述 + 检测 power 评估\",\n    \"results\": {\n      \"reformulation\": {\n        \"n_items_reformulated\": 250,\n        \"semantic_similarity_mean\": 0.92,\n        \"n_models_tested\": 50\n      },\n      \"detection\": {\n        \"constat_flagged_pct_non_rl\": 19.2,\n        \"constat_flagged_pct_all\": 17.8,\n        \"fdr_corrected_flagged_pct\": 12.3\n      },\n      \"comparison_with_dif\": {\n        \"jaccard_constat_vs_dif_c\": 0.24,\n        \"overlap_pct\": 38.2,\n        \"constat_only_pct\": 8.1,\n        \"dif_only_pct\": 22.4\n      },\n      \"power_on_semi_synthetic_gt\": {\n        \"constat_auroc\": 0.68,\n        \"dif_auroc\": 0.82\n      }\n    },\n    \"tables\": [\n      \"Table S4: ConStat detection — flagged % by model class，含 FDR correction\",\n      \"Table S5: DIF × ConStat cross-tabulation — Jaccard, Phi, overlap\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"ConStat 提供 complementary signal 但 Jaccard=0.24 说明 ensemble marginal gain 有限。 Detection mechanism 差异（temporal differential vs memorization sensitivity）使两种方法 检测近乎正交的 item 子集。此结果验证 pivot：DIF 作为 diagnostic lens 的独特价值不可被 ConStat 替代，ensemble 不如 DIF alone + robustness checks 有效。\\n\\n\\nConStat 检测 reformulation sensitivity——contaminated 模型对 verbatim 题回答正确但对 rephrased 版性能下降。19.2% 低于 DIF 31.3%，因为：(1) ConStat 仅覆盖 verbatim memorization，partial/variant contamination 不敏感；(2) MMLU 4-choice format 下 reformulation 的 accuracy drop 天然受限 （chance level 25% 提供 floor）；(3) 高质量 paraphrase 的 surface form 变化可能不足以触发 memorization-dependent 模型的 performance shift。Jaccard=0.24 confirms 两种方法检测不同 signal types——DIF 是 temporal differential functioning，ConStat 是 memorization-specific sensitivity。Semi-synthetic ground truth 上 DIF AUROC 更高（0.82 vs 0.68），因为 injected contamination 是 differential exploitation（与 DIF 检测机制对齐），而非 verbatim memorization （与 ConStat 对齐）。结论：complementary but not additive，验证了 ensemble pivot 的正确性。\\n\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"DVD generation variance 评估——12 open-weight models × 50 responses per item 的 variance-based 检测\",\n    \"results\": {\n      \"setup\": {\n        \"n_models_tested\": 12,\n        \"n_responses_per_item\": 50,\n        \"temperature\": 0.8,\n        \"total_inferences\": 7512000,\n        \"gpu_hours\": 69.6\n      },\n      \"detection\": {\n        \"bimodal_items_pct\": 11.8,\n        \"high_variance_items_pct\": 15.3,\n        \"dvd_flagged_pct\": 13.2\n      },\n      \"comparison_with_dif\": {\n        \"jaccard_dvd_vs_dif_c\": 0.16,\n        \"overlap_pct\": 29.4\n      },\n      \"power\": {\n        \"dvd_auroc_verbatim_gt\": 0.61,\n        \"dvd_auroc_variant_gt\": 0.53\n      }\n    },\n    \"tables\": [\n      \"Table S6: DVD detection — bimodal %, flagged % by model\",\n      \"Table S7: DVD vs DIF cross-tabulation\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"DVD 单独使用 power 不足，且需要 ~70 GPU hours + open-weight access。 Jaccard=0.16 说明 ensemble 增益极小。结果验证了 ensemble pivot 正确性： 三种方法的 detection mechanisms 过于异质，无法有效融合。\\n\\n\\nDVD 依赖 contaminated items 产生 bimodal generation distribution（memorized answer vs random）。 11.8% bimodal 低于 DIF 31.3%，因为：(1) bimodality 仅在 extreme verbatim memorization 下出现， partial exploitation 产生 unimodal 但 shifted distribution；(2) MMLU 4-choice format 的 discrete nature 限制了 generation variance 的 discriminative range——even uncontaminated items 在 temperature sampling 下产生 high variance；(3) requires open-weight access，排除 proprietary models。Jaccard=0.16 极低，confirms DVD 和 DIF 检测几乎完全不同的 item subsets。 AUROC 对比：DVD verbatim 0.61（moderate），variant 0.53（near chance）。Variant contamination detection 接近 chance 因为 paraphrased memorization 不产生 bimodal pattern。\\n\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"DIF + ConStat + DVD 三信号融合：majority voting + weighted fusion\",\n    \"results\": {\n      \"majority_voting_2of3\": {\n        \"tpr\": 0.35,\n        \"fpr\": 0.08,\n        \"f1\": 0.38\n      },\n      \"weighted_fusion\": {\n        \"optimal_weights\": {\n          \"dif\": 0.58,\n          \"constat\": 0.27,\n          \"dvd\": 0.15\n        },\n        \"tpr\": 0.43,\n        \"fpr\": 0.09,\n        \"f1\": 0.43,\n        \"cross_val_weight_cv\": 0.34\n      },\n      \"dif_alone_reference\": {\n        \"tpr\": 0.51,\n        \"fpr\": 0.31\n      },\n      \"coverage_gain_over_dif_pp\": 4.2,\n      \"all_ensemble_fpr_below_010\": true\n    },\n    \"tables\": [\n      \"Table S8: Ensemble configs — 2-of-3, weighted, DIF-alone，含 95% CI\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ensemble 核心问题是三种方法的 signal incommensurability 而非 signal complementarity。 Best tier 下此 negative result 加强了 pivot 叙事：DIF 的 diagnostic lens 价值在于其 独特的 temporal-differential perspective，不需要也不应与其他 mechanism 融合。 Goes to appendix as informative negative result。\\n\\n\\n2-of-3 majority voting TPR 仅 0.35，因为 pairwise Jaccard 0.16-0.24 导致三方法 consensus items 极少——三种方法各自检测不同 signal（temporal differential, memorization sensitivity, generation bimodality），overlap 不足以构建有效 consensus。Weighted fusion 略好（TPR=0.43） 但 cross-validation weight stability 差（CV=0.34），因为 calibration set 有限（semi-synthetic ground truth 200 items）且三种方法 error profiles 不 correlated。DIF alone TPR=0.51 高于 任何 ensemble configuration，因为 high-recall 方法被 ensemble consensus requirement 削弱。 Coverage gain 仅 +4.2pp 不 justify 额外 150 GPU hours 和 open-weight 依赖。\\n\"\n  },\n  {\n    \"name\": \"cross_benchmark_gsm8k\",\n    \"description\": \"GSM8K DIF 复制 + semi-synthetic 验证 + GSM1K contamination gap 相关\",\n    \"results\": {\n      \"step1_temporal_dif\": {\n        \"n_items\": 1319,\n        \"n_ref\": 1017,\n        \"n_foc\": 804,\n        \"standard_c_pct\": 18.9,\n        \"external_c_pct\": 47.4,\n        \"sanity_c_pct\": 0.3,\n        \"standard_external_spearman\": 0.926\n      },\n      \"step2_semi_synthetic\": {\n        \"standard_delta_tpr_p10\": 0.818,\n        \"external_delta_tpr_p10\": 0.517,\n        \"standard_delta_tpr_p05\": 0.508\n      },\n      \"step3_gsm1k_correlation\": {\n        \"n_models\": 33,\n        \"pearson_r\": -0.478,\n        \"pearson_p\": 0.005,\n        \"spearman_rho\": -0.403,\n        \"spearman_p\": 0.02,\n        \"partial_r_controlling_accuracy\": -0.385,\n        \"partial_p\": 0.027,\n        \"permutation_p\": 0.014,\n        \"direction\": \"NEGATIVE — opposite to contamination hypothesis\",\n        \"leave_one_out_r_range\": [\n          -0.537,\n          -0.374\n        ]\n      }\n    },\n    \"tables\": [\n      \"Table 4: GSM8K temporal DIF — C% with standard/external matching, random control\",\n      \"Table S9: GSM1K correlation — Pearson/Spearman/partial r，含 leave-one-out robustness\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"GSM8K 复制验证 framework portability（ΔTPR=+0.818）和 temporal DIF pattern（18.9% vs random 0.3%）。 GSM1K negative correlation 在 best tier 下 demote to appendix exploratory（N=33, CI wide）。 This result doesn't weaken any claim — it strengthens the meta-critique by empirically demonstrating DIF and contamination labels capture different signals。\\n\\n\\nGSM8K temporal C%=18.9% 低于 MMLU 31.3%，因为 GSM8K 是 single math domain（1,319 items）， item 功能相对 homogeneous，temporal change 集中在特定难度段而非 broad capability shift。 Semi-synthetic ΔTPR=+0.818 高于 MMLU 0.674，因为 GSM8K 更 unidimensional（单一 math 能力维度）， MH 的 unidimensional conditioning 更 appropriate，injection 更 cleanly detected。 GSM1K correlation r=-0.478 方向 opposite to contamination hypothesis：DIF 更多 flag 的模型 有更小的 GSM8K-GSM1K gap。这并不矛盾——DIF flags items whose difficulty changed across cohorts （78% favor 2024），而 small GSM8K-GSM1K gap 的模型恰恰是 genuine capability improvement 最强的（GSM1K 也难，real ability gains transfer）。This anti-correlation 实际上加强了 Claim 2 meta-critique：DIF 和 contamination ground truth 测量的是 different constructs。\\n\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"Bifactor IRT equating pilot——验证 MMLU 上 psychometric equating 可行性\",\n    \"results\": {\n      \"model_fit\": {\n        \"unidimensional_rmsea\": 0.121,\n        \"unidimensional_cfi\": 0.776,\n        \"bifactor_5group_rmsea\": 0.094,\n        \"bifactor_5group_cfi\": 0.841,\n        \"bifactor_full_57_convergence\": false,\n        \"bifactor_full_57_error\": \"non-positive definite Hessian after 500 EM iterations\"\n      },\n      \"anchor_selection\": {\n        \"dif_free_items_pct\": 17.3,\n        \"n_anchors_meeting_criteria\": 2163,\n        \"anchor_icc_concordance\": 0.82\n      },\n      \"equating_attempt\": {\n        \"equated_rho\": 0.91,\n        \"target_rho\": 0.95,\n        \"shortfall\": 0.04\n      },\n      \"decision\": \"KILLED — bifactor fit insufficient (RMSEA=0.094>0.05), equated rho=0.91 < target 0.95\"\n    },\n    \"tables\": [\n      \"Table S10: IRT fit comparison — unidimensional vs 5-group bifactor vs full bifactor\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Informative negative result。说明传统 psychometric equating 不能直接迁移到 LLM multi-domain benchmarks：extreme multidimensionality violates essential unidimensionality assumption。 加强 diagnostic lens framing——DIF 的价值不在于 equating-based item replacement， 而在于 understanding what changed。在 limitations 中自然 motivate future multidimensional IRT。\\n\\n\\nMMLU 57-subject 结构使 full bifactor（1 general + 57 specific）在计算上不可行—— non-positive definite Hessian 因为 57 specific factors 导致 identification 问题（many subjects 仅 100 items，insufficient for factor estimation）。Reduced 5-group bifactor 改善有限 （RMSEA 0.121→0.094, CFI 0.776→0.841），仍远低于 acceptable fit thresholds。根本原因是 MMLU 内在 multidimensionality：从 abstract_algebra 到 world_religions 的 57 domains 无法 被 1 general factor + few group factors 充分 capture。Equating pilot 在 suboptimal fit 下 仍尝试：anchors 数量足够（2,163 items），但 misspecified ability estimates 传播到 fixed-parameter calibration，导致 equated rho=0.91 低于 target 0.95。Kill decision 正确—— 此 negative result 在 limitations 中作为 future multidimensional IRT work 的 motivation。\\n\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"DIF-flagged MMLU items 的 LLM-based 替代 item 生成与难度校准\",\n    \"results\": {\n      \"generation\": {\n        \"n_items_generated\": 400,\n        \"n_subjects\": 10,\n        \"construct_adherence_human_eval\": 0.784\n      },\n      \"difficulty_calibration\": {\n        \"prompt_based_rho\": 0.38,\n        \"student_sim_rho\": 0.52,\n        \"target_rho\": 0.75\n      },\n      \"quality\": {\n        \"human_quality_score_mean\": 3.2,\n        \"human_quality_target\": 4.0,\n        \"holdout_panel_rho\": 0.48\n      },\n      \"decision\": \"BELOW BENCHMARKS — best difficulty rho=0.52 vs target 0.75\"\n    },\n    \"tables\": [\n      \"Table S11: Difficulty calibration — prompt vs student-sim vs empirical，含 95% CI\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"有价值的 negative result——说明 \\\"just regenerate flagged items\\\" 不是 trivial solution。 加强 diagnostic lens framing：DIF 的 actionable value 是 audit protocol + informed maintenance， 而非 automated regeneration。在 Discussion 中可用于回应 reviewer 的 \\\"so what do we do?\\\" question。\\n\\n\\nDifficulty calibration 是 item generation 的瓶颈。Prompt-based targeting（直接指定 difficulty level） rho=0.38，因为 LLM 对 \\\"difficulty for other LLMs\\\" 的 internal calibration 与 empirical difficulty 几乎无关——difficulty 由 knowledge coverage, reasoning depth, distractor quality 联合决定， 非 LLM 自身 uncertainty 可预测。Student simulation 改善到 rho=0.52，但 arXiv 2601.09953 的 r=0.75-0.82 是在 human exam items 上报告的，LLM benchmark items 的 difficulty determinants 不同（e.g., MMLU 多选的 distractor 设计对 LLM 和 human 的 difficulty contribution 不同）。 Construct fidelity 78.4% 说明 22% 的 generated items 有 subject drift 或 cognitive level 错误。 Plan_005 被 kill 后，本 plan 失去 equating framework 支撑。\\n\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"Sinharay et al. (2006) cumulative Bayesian DIF priors 的 4-administration simulation\",\n    \"results\": {\n      \"setup\": {\n        \"n_administrations\": 4,\n        \"n_items_per_sim\": 500,\n        \"n_models_per_admin\": 200,\n        \"true_dif_items\": 100,\n        \"delta_range\": [\n          0.8,\n          1.8\n        ]\n      },\n      \"power_accumulation\": {\n        \"tpr_admin1_d10\": 0.41,\n        \"tpr_admin2_d10\": 0.58,\n        \"tpr_admin3_d10\": 0.72,\n        \"tpr_admin4_d10\": 0.81,\n        \"tpr_admin1_d08\": 0.22,\n        \"tpr_admin2_d08\": 0.38,\n        \"tpr_admin3_d08\": 0.53,\n        \"tpr_admin4_d08\": 0.65\n      },\n      \"fpr_stability\": {\n        \"fpr_range\": [\n          0.042,\n          0.045\n        ]\n      },\n      \"bayesian_shrinkage\": {\n        \"posterior_sd_admin4\": 0.31\n      }\n    },\n    \"tables\": [\n      \"Table S12: Cumulative power — TPR at δ=0.8/1.0/1.4/1.8 × 1-4 administrations\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Clean simulation 支持 audit protocol 的 operational recommendation：每 6 月 DIF assessment， 3 次累积后 medium effects 的 power 从 0.41 升至 0.72。Goes to appendix，在 Discussion 中 referenced。\\n\\n\\nBayesian evidence accumulation 的 power gain 等价于 effectively increasing sample precision。 δ=1.0 时单次 TPR=0.41（与 phase2 sim 的 N=80 结果一致），4 次累积达 0.81——posterior SD 从 1.0 shrink 到 0.31，precision quadruples。对 small effects（δ=0.8），MH 单次几乎无法检测 （TPR=0.22），但 4 次累积达 0.65——这是 monitoring protocol 的核心理论支撑。 FPR 稳定在 ~0.043 因为 Bayesian shrinkage 对 null items 同样有效（posterior for null items 集中在 0 附近）。Simulation-only 但为 audit protocol 的 monitoring frequency 建议提供 quantitative basis。\\n\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"Benchmark validity 在 progressive item removal 下的降级分析\",\n    \"results\": {\n      \"progressive_removal\": {\n        \"pct_5\": {\n          \"ranking_rho\": 0.9998,\n          \"reliability_alpha\": 0.993,\n          \"construct_jaccard\": 0.98\n        },\n        \"pct_10\": {\n          \"ranking_rho\": 0.9994,\n          \"reliability_alpha\": 0.991,\n          \"construct_jaccard\": 0.96\n        },\n        \"pct_20\": {\n          \"ranking_rho\": 0.9987,\n          \"reliability_alpha\": 0.987,\n          \"construct_jaccard\": 0.92\n        },\n        \"pct_31\": {\n          \"ranking_rho\": 0.9965,\n          \"reliability_alpha\": 0.982,\n          \"construct_jaccard\": 0.87\n        },\n        \"pct_50\": {\n          \"ranking_rho\": 0.9912,\n          \"reliability_alpha\": 0.971,\n          \"construct_jaccard\": 0.78\n        }\n      },\n      \"theoretical_match\": {\n        \"spearman_brown_predicted_rho_31pct\": 0.9968,\n        \"empirical_rho_31pct\": 0.9965,\n        \"gap\": 0.0003\n      }\n    },\n    \"tables\": [\n      \"Table S13: Progressive degradation — rho, reliability, coverage at 5/10/20/31/50%\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"直接支持 \\\"instability ≠ invalidity\\\" 叙事。31% instability 不威胁 validity（rho=0.997） 因为 MMLU 的 massive redundancy。Headline number 进 main text，full curve 进 appendix。\\n\\n\\nMMLU 12,508 items 的 massive redundancy 决定了 removal 的 graceful degradation。 Spearman-Brown formula 预测 test length 缩减 31% 时 rho 从 ~1.0 降至 0.9968—— empirical 0.9965 精确匹配，说明 degradation 完全由 test shortening 驱动，无 systematic bias（DIF items 不是 systematically more informative for ranking）。Construct coverage 降速快于 ranking stability，因为 DIF items 在 domains 间非均匀分布（moral_scenarios 48.4% vs college_biology 20.7%），high-DIF domains 在 removal 后 coverage 受损更大。 与 plan_017 实际结果（rho=0.997 at 31%）高度一致。\\n\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"Item-Focused Trees（Tutz & Berger 2016）——连续时间 DIF 作为 MH categorical split 的 robustness check\",\n    \"results\": {\n      \"detection\": {\n        \"ift_flagged_pct\": 28.7,\n        \"jaccard_ift_vs_mh_c\": 0.78,\n        \"ift_only_pct\": 4.2,\n        \"mh_only_pct\": 6.8\n      },\n      \"temporal_patterns\": {\n        \"single_changepoint_pct\": 71,\n        \"multiple_changepoints_pct\": 12,\n        \"gradual_drift_pct\": 17,\n        \"median_changepoint\": \"2023-09\"\n      },\n      \"tree_structure\": {\n        \"mean_terminal_nodes\": 5.2,\n        \"max_depth\": 3\n      }\n    },\n    \"tables\": [\n      \"Table S14: IFT vs MH concordance — Jaccard, overlap, unique flags\",\n      \"Table S15: Changepoint timing distribution by quarter\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Confirms MH categorical split robustness（Jaccard=0.78）。Changepoint timing 提供 temporal granularity，在 Discussion 中简要引用。Appendix robustness check。\\n\\n\\nIFT 用 continuous release date 替代 MH 的 binary temporal split，避免 arbitrary cutoff。 28.7% vs MH 31.3% 的差异来自 tree-based multiple testing correction（node-level significance threshold）vs MH 的 per-item testing。Jaccard=0.78 高一致性说明 MH categorical split captures the main temporal signal。IFT 的独特 value 是 changepoint timing：71% items 有 single changepoint（median 2023-09，对应 Llama-2/Mistral/Phi-1 release 密集期）， 12% 有 multiple changepoints（progressive drift），17% gradual drift。Timing information 支持 Discussion 中的 \\\"what drives instability\\\" narrative——major model releases 是 item functioning change 的 primary driver。\\n\"\n  },\n  {\n    \"name\": \"architecture_stratified_dif\",\n    \"description\": \"Architecture-homogeneous subpopulation DIF——验证 architecture heterogeneity 非 confound\",\n    \"results\": {\n      \"metabench_composition\": {\n        \"total_models\": 5227,\n        \"decoder_only\": 5226,\n        \"decoder_only_pct\": 99.98,\n        \"non_decoder\": 1,\n        \"non_decoder_id\": \"flan-ul2\"\n      },\n      \"dif_comparison\": {\n        \"decoder_only_c_pct\": 31.3,\n        \"full_c_pct\": 31.3,\n        \"jaccard\": 1.0,\n        \"items_changed\": 0\n      },\n      \"irt_fit\": {\n        \"full_rmsea\": 0.121,\n        \"decoder_only_rmsea\": 0.121,\n        \"delta_rmsea\": 0.0\n      }\n    },\n    \"tables\": [\n      \"Table S16: Architecture composition\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"One-line main text defense。IRT misfit 重定向至 limitations（multidimensionality motivation）。\\n\\n\\nMETABENCH MMLU 的 architecture homogeneity 使本实验成为 trivial pass：99.98% decoder-only， 唯一的 encoder-decoder (flan-ul2) 在 N=5227 中的影响可忽略。Jaccard=1.0 意味着 zero items 的 DIF classification 因 architecture stratification 而改变。IRT fit 同样不变 （RMSEA=0.121），因为 misfit 源自 57-subject multidimensionality 而非 architecture heterogeneity。 这是 ideal robustness result：potential confound 被 data composition 自然消除。\\n\"\n  },\n  {\n    \"name\": \"semi_synthetic_contamination_validation\",\n    \"description\": \"Known contamination injection 进 real response matrix + DIF detection power 评估 + cross-subject matching 验证\",\n    \"results\": {\n      \"temporal_external_matching\": {\n        \"baseline_fpr\": 0.314,\n        \"tpr_p00\": 0.326,\n        \"tpr_p03\": 0.548,\n        \"tpr_p05\": 0.834,\n        \"tpr_p07\": 0.99,\n        \"tpr_p10\": 1.0,\n        \"delta_tpr_p05\": 0.508,\n        \"delta_tpr_p10\": 0.674\n      },\n      \"ability_external_matching\": {\n        \"baseline_fpr\": 0.493,\n        \"tpr_p10\": 0.8,\n        \"delta_tpr_p10\": 0.302\n      },\n      \"matching_variable_contamination\": {\n        \"standard_fpr_p10\": 0.616,\n        \"standard_fpr_baseline\": 0.298,\n        \"fpr_inflation\": 0.318,\n        \"cross_subject_fpr_inflation\": 0.0\n      },\n      \"cross_subject_5subj_validation\": {\n        \"delta_fpr_all_subjects\": 0.0,\n        \"avg_delta_tpr_p05\": 0.508,\n        \"subjects_passing_p05\": \"4/5\"\n      }\n    },\n    \"tables\": [\n      \"Table 5: Semi-synthetic ΔTPR/ΔFPR across exploitation rates and matching strategies\",\n      \"Table 6: Standard vs cross-subject matching FPR comparison\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"ΔTPR=+0.508 是 Claim 3 headline。Cross-subject ΔFPR=0.000 是 key methodological novelty。 Dose-response pattern 提供 internal validity。Both metrics 在 best tier range 内。\\n\\n\\nSemi-synthetic injection 在 real response matrix 上创造 controlled ground truth—— 对 focal cohort 的 known-clean items 执行 incorrect→correct flipping with probability p。 ΔTPR=+0.508 at p=0.5 在 best tier [0.45, 0.55] range 内，confirms DIF detects moderate differential contamination。Dose-response（p=0.3→0.5→0.7→1.0 对应 TPR 0.55→0.83→0.99→1.0） 增强因果推断。关键 methodological finding：standard MH matching（total score 含 contaminated items） 导致 FPR inflation +0.318（matching variable contamination），而 cross-subject matching （other subjects 的 total score）完全消除 inflation（ΔFPR=0.000）。Cross-subject matching works 因为 contamination 是 subject-specific（inject 进特定 subject），而 other subjects 的 total score 不受 contamination 影响，保持 conditioning variable 的 exchangeability。\\n\"\n  },\n  {\n    \"name\": \"multi_benchmark_temporal_dif\",\n    \"description\": \"6 benchmarks temporal DIF——cross-benchmark generalizability 验证\",\n    \"results\": {\n      \"mmlu\": {\n        \"n_items\": 12508,\n        \"n_ref\": 1080,\n        \"n_foc\": 807,\n        \"pct_c\": 31.3,\n        \"random_pct_c\": 0.18\n      },\n      \"winogrande\": {\n        \"n_items\": 1267,\n        \"n_ref\": 1017,\n        \"n_foc\": 803,\n        \"pct_c\": 30.3,\n        \"random_pct_c\": 0.32\n      },\n      \"truthfulqa\": {\n        \"n_items\": 817,\n        \"n_ref\": 1080,\n        \"n_foc\": 807,\n        \"pct_c\": 29.7,\n        \"random_pct_c\": 0.37\n      },\n      \"arc\": {\n        \"n_items\": 1172,\n        \"n_ref\": 1080,\n        \"n_foc\": 807,\n        \"pct_c\": 26.9,\n        \"random_pct_c\": 0.6\n      },\n      \"gsm8k\": {\n        \"n_items\": 1319,\n        \"n_ref\": 1017,\n        \"n_foc\": 804,\n        \"pct_c\": 18.9,\n        \"random_pct_c\": 0.3\n      },\n      \"hellaswag\": {\n        \"n_items\": 10042,\n        \"n_ref\": 1080,\n        \"n_foc\": 807,\n        \"pct_c\": 17.9,\n        \"random_pct_c\": 0.28\n      },\n      \"summary\": {\n        \"range\": \"17.9–31.3%\",\n        \"all_random_below_1pct\": true,\n        \"min_enrichment_ratio\": 44.8,\n        \"mean_c_pct\": 25.8,\n        \"n_benchmarks\": 6\n      }\n    },\n    \"tables\": [\n      \"Table 3: Cross-benchmark temporal DIF — 6 rows, N_items/N_ref/N_foc/C%/random%\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-benchmark consistency 是 Claim 1 generalizability 最强证据。17.9-31.3% range 在 best tier [17.0, 32.0] 内。Claim 1 statement 可升级为 \\\"17.9-31.3% across 6 major benchmarks\\\"。\\n\\n\\n6 benchmarks 一致显示 temporal DIF 远超 chance（enrichment 45-174×），确认 temporal item instability 是 LLM benchmark 的 general phenomenon。C% ordering 反映 benchmark 结构： MMLU（57 domains, maximal multidimensionality）和 WinoGrande（commonsense reasoning, capability-sensitive） 最高；HellaSwag（sentence completion, more pattern-matching than reasoning）和 GSM8K （single math domain）最低。低 C% benchmarks 的 items 功能更 homogeneous across model generations ——sentence completion patterns evolve less than knowledge/reasoning items。 All random controls <1% 排除 statistical artifact across all benchmarks。\\n\"\n  },\n  {\n    \"name\": \"permutation_null_c_rate\",\n    \"description\": \"1000× permutation test——temporal label shuffling 下的 C% null distribution\",\n    \"results\": {\n      \"null_distribution\": {\n        \"n_permutations\": 1000,\n        \"mean_c_pct\": 0.21,\n        \"sd_c_pct\": 0.11,\n        \"median_c_pct\": 0.19,\n        \"q95_c_pct\": 0.42,\n        \"q99_c_pct\": 0.54,\n        \"max_c_pct\": 0.71\n      },\n      \"significance\": {\n        \"observed_c_pct\": 31.3,\n        \"z_score\": 282.6,\n        \"empirical_p\": \"<0.001 (0/1000 exceed observed)\",\n        \"ratio_observed_to_null_mean\": 149\n      },\n      \"consistency\": {\n        \"random_split_c_pct\": 0.18,\n        \"permutation_null_mean\": 0.21,\n        \"convergent\": true\n      }\n    },\n    \"tables\": [\n      \"Table 7: Permutation null — mean/SD/Q95/Q99/max vs observed，z-score，p-value\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Best tier 的 critical robustness check。Null C% mean=0.21% 在 [0.0, 1.0] range 内。 z=282.6 使 temporal DIF signal 成为 unambiguous。与 random-split 的 convergence 提供 double confirmation。This goes into main text as primary robustness evidence alongside threshold sensitivity（plan_018）and decomposition（plan_019）。\\n\\n\\nPermutation null 通过 random temporal label reassignment（保持 N_ref=1080, N_foc=807） 建立 chance baseline。Mean 0.21% 与 random split 0.18% convergent，因为两者本质上 measure the same thing：无 temporal structure 时的 spurious DIF rate。0.21% vs 0.18% 微小差异来自 permutation 使用 full N=1887（random split 在 single cohort ~1000 内）。Observed 31.3% 给出 z=282.6——0/1000 permutations exceed，empirical p<0.001。这是因为 temporal structure 是 genuine signal：2023 和 2024 model cohorts 确实在 item-level functioning 上不同。 Permutation destroys this temporal structure，restoring C% to chance level (~0.2%)。 149× enrichment over null 彻底回答 \\\"is 31% above chance?\\\"。\\n\"\n  },\n  {\n    \"name\": \"odds_ratio_regression_transparency\",\n    \"description\": \"多层 logistic regression——OR + CI + McFadden/Nagelkerke R² + Simpson's paradox 展示\",\n    \"results\": {\n      \"model1_domain_delta\": {\n        \"mcfadden_r2\": 0.0007,\n        \"nagelkerke_r2\": 0.0012,\n        \"aic\": 15545.2,\n        \"or_per_010\": 1.55,\n        \"or_ci_per_010\": [\n          1.19,\n          2.03\n        ]\n      },\n      \"model2_domain_plus_items\": {\n        \"mcfadden_r2\": 0.0423,\n        \"nagelkerke_r2\": 0.072,\n        \"aic\": 14902.3,\n        \"subject_delta_or_per_010\": 0.73,\n        \"difficulty_or_per_010\": 0.78,\n        \"discrimination_or_per_010\": 1.51\n      },\n      \"model3_item_delta\": {\n        \"mcfadden_r2\": 0.0012,\n        \"nagelkerke_r2\": 0.0021,\n        \"aic\": 15536.9,\n        \"or\": 2.11,\n        \"or_ci\": [\n          1.51,\n          2.96\n        ]\n      },\n      \"model4_best\": {\n        \"mcfadden_r2\": 0.0434,\n        \"nagelkerke_r2\": 0.0737,\n        \"aic\": 14885.4,\n        \"item_delta_or_per_010\": 0.92,\n        \"difficulty_or_per_010\": 0.77,\n        \"discrimination_or_per_010\": 1.54\n      },\n      \"simpsons_paradox\": true,\n      \"lr_test_m1_vs_m2_chi2\": 646.98,\n      \"lr_test_m3_vs_m4_chi2\": 655.53\n    },\n    \"tables\": [\n      \"Table S17: Four-model regression summary — OR, 95% CI, R², AIC, deviance\",\n      \"Table S18: Simpson's paradox — Model 1 vs Model 2 coefficient sign reversal\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Full transparency supplement for plan_019 decomposition。Simpson's paradox 是 methodological cautionary tale：naive domain-level analysis (OR=1.55) overestimates improvement's contribution， item-level conditioning (OR=0.73) reveals the truth。Model 1 作为 primary（conservative）， Simpson's paradox 在 appendix 详述。R²=0.0007 是 \\\"≤7.6% explained\\\" claim 的 additional support。\\n\\nFour-model architecture 揭示 Simpson's paradox：accuracy improvement 的 OR 从 Model 1 的 1.55 （正相关：improved domains 有更多 DIF）reversal 到 Model 2 的 0.73（负相关：controlling for item properties 后 improvement 反而 associated with less DIF）。Paradox 成因：DIF items 更难（d=-0.247, plan_023）且 higher-discrimination（d=0.230），而这些 item properties 同时 与 accuracy change 相关（difficult domains 有 larger improvement headroom）。 Model 1 的 R²=0.0007 confirms accuracy improvement 几乎不解释 DIF variance——绝大部分 DIF 是 item-specific 而非 domain improvement 的 proxy。Model 4 R²=0.0434 shows item intrinsic properties（difficulty, discrimination）解释了 >98% 的 explainable variance。 LR test（χ²=647-656, p<0.001）confirms adding item properties 显著改善 fit。\\n\"\n  }\n]",
      "numLines": 612,
      "startLine": 1,
      "totalLines": 612
    }
  },
  "sourceToolAssistantUUID": "55cc6fd7-a85e-43eb-bd65-6248c486030d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122440 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "6109f89b-25f6-482a-bb23-2382896927dc",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper from experiment data",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6"
}
```

---

### Assistant

_source line 16 · 2026-05-21T12:50:56.275Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also read the paper writing norms skill since this is a paper writing task.

Let me now draft the complete LaTeX paper. I need to:

1. Structure: Abstract, Introduction, Related Work, Method, Experiments, Discussion/Conclusion, Limitations
2. Cover all experiments from experiment_data.json
3. Follow EMNLP 2026 8-page limit (this is a dream paper so it should be approximately this length)
4. Follow the narrative guidance and paper_framing.md

Let me organize the experiments:

**Main body experiments:**
- real_data_dif_mmlu (Claim 1 - Table 1, 2)


- multi_benchmark_temporal_dif (Claim 1 generalizability - Table 3)
- semi_synthetic_contamination_validation (Claim 3 - Table 5, 6)
- cross_benchmark_gsm8k (Claim 3 cross-benchmark + Claim 1 GSM8K - Table 4)
- permutation_null_c_rate (Robustness - Table 7)
- graceful_degradation_analysis (Claim 4 - in main text)
- odds_ratio_regression_transparency (Claim 1 decomposition - appendix but referenced)

**Appendix experiments:**
- rl_robustness_validation and remaining experiments covering perturbation evaluation, generation variance, ensemble fusion, IRT equating, item calibration, Bayesian DIF, tree-based analysis, and architecture stratification across supplementary tables

Now I'm mapping out the paper structure and table assignments. I'll organize the main results around temporal DIF patterns across benchmarks, domain specificity findings, cross-benchmark validation, and robustness checks, then move into the appendix experiments that support each claim.

I'm ready to draft the full LaTeX document with comprehensive sections covering the methodology, results, and implications while keeping the main text to around 8 pages.

Now I'm reviewing the key quantitative findings to weave throughout: the permutation null establishing statistical significance at z=282.6, the semi-synthetic validation showing a dose-response effect with substantial true positive rate gains, cross-subject matching confirming no false positive inflation, and the ranking stability remaining remarkably high even after removing a third of the data. I'm also noting the circularity ablation results that strongly favor the DIF-based approach, the architectural homogeneity across models, threshold sensitivity patterns, and the enrichment validation against existing web-overlap labels.

The robustness checks show the RL framework remains stable with high Jaccard overlap, though IFT shows somewhat lower agreement with the Mokken-Hemker approach, and the IRT misfit metrics suggest some multidimensionality that I'll need to address as a limitation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6109f89b-25f6-482a-bb23-2382896927dc",
  "isSidechain": false,
  "requestId": "req_011CbFk42FYEbXD5BjdpXrgb",
  "type": "assistant",
  "uuid": "75b27ede-662f-4b29-888e-41330a82c221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aa1m7pALuaHtSorMP3rHhv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6232,
      "cache_creation_input_tokens": 14355,
      "cache_read_input_tokens": 24214,
      "output_tokens": 1304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6232,
          "output_tokens": 1304,
          "cache_read_input_tokens": 24214,
          "cache_creation_input_tokens": 14355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14355
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

_source line 17 · 2026-05-21T12:50:56.279Z_

Now let me read the paper writing norms skill for quality guidance, and check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75b27ede-662f-4b29-888e-41330a82c221",
  "isSidechain": false,
  "requestId": "req_011CbFk42FYEbXD5BjdpXrgb",
  "type": "assistant",
  "uuid": "cb7cacdb-5267-4a57-80d6-f9e1e58f28e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aa1m7pALuaHtSorMP3rHhv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6232,
      "cache_creation_input_tokens": 14355,
      "cache_read_input_tokens": 24214,
      "output_tokens": 1304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6232,
          "output_tokens": 1304,
          "cache_read_input_tokens": 24214,
          "cache_creation_input_tokens": 14355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14355
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

_source line 18 · 2026-05-21T12:50:56.282Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AXrFVWiEzzuGKDQEVKMPv4`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb7cacdb-5267-4a57-80d6-f9e1e58f28e5",
  "isSidechain": false,
  "requestId": "req_011CbFk42FYEbXD5BjdpXrgb",
  "type": "assistant",
  "uuid": "8f73f119-7276-472f-adc0-6f6c50c71b58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aa1m7pALuaHtSorMP3rHhv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6232,
      "cache_creation_input_tokens": 14355,
      "cache_read_input_tokens": 24214,
      "output_tokens": 1304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6232,
          "output_tokens": 1304,
          "cache_read_input_tokens": 24214,
          "cache_creation_input_tokens": 14355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14355
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

_source line 19 · 2026-05-21T12:50:56.298Z_

<details><summary>↩ Tool result · `toolu_01AXrFVWiEzzuGKDQEVKMPv4`</summary>

````text
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
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "8f73f119-7276-472f-adc0-6f6c50c71b58",
  "isSidechain": false,
  "promptId": "a51ab8ce-ea68-4472-a825-8e34be9a6366",
  "type": "user",
  "uuid": "e3ade4bb-41c6-4ce8-bf13-53881f03f376",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "8f73f119-7276-472f-adc0-6f6c50c71b58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Tool call

_source line 20 · 2026-05-21T12:50:57.764Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01J4rc1GfaVMLHtGP6VKjDWZ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3ade4bb-41c6-4ce8-bf13-53881f03f376",
  "isSidechain": false,
  "requestId": "req_011CbFk42FYEbXD5BjdpXrgb",
  "type": "assistant",
  "uuid": "caea6fa8-e223-45b2-be18-cd0de0211d1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aa1m7pALuaHtSorMP3rHhv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6232,
      "cache_creation_input_tokens": 14355,
      "cache_read_input_tokens": 24214,
      "output_tokens": 1304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6232,
          "output_tokens": 1304,
          "cache_read_input_tokens": 24214,
          "cache_creation_input_tokens": 14355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14355
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122440 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "caea6fa8-e223-45b2-be18-cd0de0211d1c",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper from experiment data",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6"
}
```

---

### Tool result

_source line 23 · 2026-05-21T12:50:58.057Z_

<details><summary>↩ Tool result · `toolu_01J4rc1GfaVMLHtGP6VKjDWZ`</summary>

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
  "parentUuid": "caea6fa8-e223-45b2-be18-cd0de0211d1c",
  "isSidechain": false,
  "promptId": "a51ab8ce-ea68-4472-a825-8e34be9a6366",
  "type": "user",
  "uuid": "0d885f29-921a-49cb-a243-3f22a45d9129",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "caea6fa8-e223-45b2-be18-cd0de0211d1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T12:51:32.107Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me write the complete paper. Let me carefully structure it according to the experiment data, paper framing, and writing norms.

Key structure:
- Abstract
- Introduction (with "instability ≠ invalidity" framing upfront)
- Related Work
- Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)
- Experiments (organized by claims)
- Discussion + Limitations
- Conclusion
- Appendix (all supplementary tables)

I need to be careful about:
1. No em-dashes (use commas, parentheses, or separate sentences)


2. No -ing phrase endings
3. No AI-style words
4. Booktabs for tables
5. All numbers from experiment_data.json, no fabrication
6. Every experiment gets a section/table

I'll aim for about 8 pages of main text content. For the main tables, I'm planning temporal DIF summary for MMLU, cross-benchmark temporal DIF across six benchmarks, semi-synthetic validation with TPR and FPR changes, and permutation null distribution. The rest will go into supplementary tables. Let me double-check my table assignments against the experiment data before I start writing. carefully:

From the experiment data JSON:
- real_data_dif_mmlu: Table 1 (temporal DIF), Table 2 (57-subject domain), Table S1 (within-family)
- rl_robustness_validation: Table S2, S3
- constat_perturbation_eval: Table S4, S5
- dvd_generation_variance_eval: Table S6, S7
- ensemble_fusion: Table S8
- cross_benchmark_gsm8k: Table 4 (GSM8K DIF), Table S9 (GSM1K correlation)
- bifactor_irt_equating_pilot: Table S10
- item_generation_calibration: Table S11
- cumulative_bayesian_dif: Table S12
- graceful_degradation_analysis: Table S13
- item_focused_trees: Table S14, S15
- architecture_stratified_dif: Table S16
- semi_synthetic_contamination_validation: Table 5, 6
- multi_benchmark_temporal_dif: Table 3
- permutation_null_c_rate: Table 7
- odds_ratio_regression_transparency: Table S17, S18

The main text tables are 1 through 7, so I need to organize the paper around those while keeping it under 8 pages. I'm mapping each experiment to its corresponding section now—temporal DIF analysis goes in Section 4.1 with Tables 1 and 2, then I'll work through the domain specificity and cross-benchmark results. I'm working through the space constraints for an 8-page limit, so I need to be strategic about which tables stay in the main text versus the appendix. The key tables for the narrative—Tables 1, 3, 5, and 7—should remain, while the large 57-subject table and some supporting analyses can move to the appendix. I'm reconsidering the placement of Tables 4 and 6 since they're important for the core arguments, but the 57-subject breakdown is substantial enough to justify moving it.

Now I'm thinking about the actual paper structure and how to write this up. Since this is a dream paper, I'll use a straightforward LaTeX template rather than worrying about specific conference formatting—something simple and clean that lets the content shine through.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d885f29-921a-49cb-a243-3f22a45d9129",
  "isSidechain": false,
  "requestId": "req_011CbFk6EQ6QLpWBvFj7og7a",
  "type": "assistant",
  "uuid": "b82df701-d084-4705-b9a4-6cb3abecd302",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pb1GPdhYzHRdSkNDrysNzF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13091,
      "cache_read_input_tokens": 38569,
      "output_tokens": 13836,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13091,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13836,
          "cache_read_input_tokens": 38569,
          "cache_creation_input_tokens": 13091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13091
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

_source line 25 · 2026-05-21T12:51:32.109Z_

Now I'll write the complete paper. This is a large document covering all 16 experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b82df701-d084-4705-b9a4-6cb3abecd302",
  "isSidechain": false,
  "requestId": "req_011CbFk6EQ6QLpWBvFj7og7a",
  "type": "assistant",
  "uuid": "fa85aa4b-6cdd-43d5-8e1e-06e58180dd43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pb1GPdhYzHRdSkNDrysNzF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13091,
      "cache_read_input_tokens": 38569,
      "output_tokens": 13836,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13091,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13836,
          "cache_read_input_tokens": 38569,
          "cache_creation_input_tokens": 13091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13091
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

_source line 26 · 2026-05-21T12:55:50.575Z_

<details open><summary>🔧 Tool call — Write · `toolu_01J2MqCZZWV7q8TvPK46F2eM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper.tex",
  "content": "\\documentclass[11pt,twocolumn]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{caption}\n\\captionsetup{font=small}\n\n\\title{Temporal Item Instability in LLM Benchmarks:\\\\A Psychometric DIF Analysis of 5,227 Models on MMLU}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWhen we compare Large Language Model (LLM) scores across model generations, we implicitly assume that benchmark items measure the same construct with the same difficulty over time.\nWe test this assumption by applying Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis to the METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items), the largest-scale psychometric item analysis of LLM benchmarks to date.\nWe find that 31.3\\% of MMLU items exhibit large temporal DIF (ETS C class, $|\\Delta_{\\text{MH}}| \\geq 1.5$) between 2023 and 2024-H1 model cohorts, a rate 149$\\times$ the permutation null baseline (0.21\\%, $z=282.6$, $p<0.001$).\nThis instability is not explained by capability improvement ($\\leq$7.6\\% of variance) and generalizes across six benchmarks (17.9--31.3\\%).\nCrucially, instability does not threaten validity: rankings remain stable after removing all flagged items ($\\rho \\approx 0.997$).\nWe identify a methodological gap in the contamination detection literature: web-overlap ground truth labels cannot validate item-level differential detectors (enrichment $\\approx 1.0$), and propose a semi-synthetic validation framework with cross-subject matching that eliminates false positive inflation ($\\Delta$FPR$= 0.000$).\nDIF serves not as a quality filter but as a diagnostic lens, revealing which capability dimensions shift across model generations, with a concrete audit protocol for benchmark maintenance.\n\\end{abstract}\n\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nBenchmark leaderboards drive LLM development decisions worth billions of dollars, yet they rest on an untested assumption: that the same test item measures the same thing for models released six months apart.\nIf a question becomes easier for newer models not because they reason better but because the answer leaked into training data, or because architectural innovations exploit specific item formats, then cross-temporal score comparisons lose meaning.\nPsychometrics calls this problem \\emph{Differential Item Functioning} (DIF): an item exhibits DIF when examinees of equal overall ability from different groups have systematically different probabilities of answering it correctly.\n\nWe bring this mature psychometric framework to LLM evaluation at unprecedented scale.\nUsing the METABENCH response matrix~\\citep{perlitz2024metabench} (5,227 models $\\times$ 12,508 MMLU items), we apply Mantel-Haenszel DIF analysis~\\citep{holland1988dif} with temporal cohort grouping (2023 vs.\\ 2024-H1 models) and find that \\textbf{31.3\\% of items are functionally unstable} across model generations.\nThis figure is robust across significance thresholds (10--49\\% at $|\\Delta_{\\text{MH}}|$ cutoffs 2.5--1.0), unaffected by multiple testing correction (BH FDR removes 3/3,918 items), and not driven by capability improvement (domain accuracy gains explain $\\leq$7.6\\% of the instability).\nThe pattern replicates across six benchmarks (17.9--31.3\\%).\n\nA critical insight frames our work: \\textbf{instability does not imply invalidity.}\nRemoving all 31\\% of flagged items changes model rankings negligibly ($\\rho \\approx 0.997$), exposing massive measurement redundancy in MMLU.\nDIF is therefore not a quality filter for item removal but a diagnostic lens that reveals which capability dimensions are shifting across model generations, and which specific items' measurement properties have changed.\n\nThis perspective also exposes a methodological gap in existing contamination detection research.\nPrior work validates detectors against web-overlap or $n$-gram labels~\\citep{li2024task,yang2023rethinking}, which measure global exposure (whether an item is publicly accessible) rather than differential contamination (whether an item functions differently across model cohorts).\nWe show empirically that DIF flags and web-overlap labels are near-orthogonal (enrichment $= 0.96$, Jaccard $= 0.21$), confirming that the field's standard validation methodology has a fundamental blind spot for item-level differential detectors.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n\\item \\textbf{Empirical discovery}: 17.9--31.3\\% temporal item instability across six major LLM benchmarks, validated by a 1,000-iteration permutation null ($z=282.6$) and robust to threshold choice, multiple testing, model non-independence, and architecture composition (\\S\\ref{sec:temporal}).\n\\item \\textbf{Ground truth meta-critique}: Web-overlap labels cannot validate item-level differential detectors; we provide the first empirical demonstration with enrichment analysis and semi-synthetic proof of concept (\\S\\ref{sec:metacritique}).\n\\item \\textbf{Semi-synthetic validation framework}: A reusable $\\Delta$TPR methodology with cross-subject matching ($\\Delta$FPR $= 0.000$), portable across benchmarks (GSM8K $\\Delta$TPR $= +0.818$) (\\S\\ref{sec:semisynthetic}).\n\\item \\textbf{DIF as diagnostic lens}: An actionable audit protocol for benchmark maintainers, supported by circularity ablation showing DIF is the least disruptive non-random removal strategy ($z = -9.5$ vs.\\ accuracy-gap $z = -157$) (\\S\\ref{sec:diagnostic}).\n\\end{enumerate}\n\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{LLM Benchmark Contamination.}\nContamination detection methods fall into three families.\nPerturbation-based approaches test whether models are sensitive to surface-level reformulation of known test items~\\citep{golchin2023constat,xu2024benchmark}.\nGeneration-variance methods examine whether contaminated items elicit bimodal output distributions~\\citep{dong2024dvd}.\nCorpus-matching approaches search training data for $n$-gram overlaps with test items~\\citep{li2024task,yang2023rethinking,deng2024investigating}.\nAll three families validate primarily against web-overlap labels, which capture global item exposure rather than differential model-level exploitation.\nOur meta-critique (\\S\\ref{sec:metacritique}) demonstrates that this validation gap is empirically consequential.\n\n\\paragraph{Benchmark Robustness and Temporal Validity.}\nSeveral studies have questioned the stability of LLM benchmarks.\n\\citet{polo2024tinybenchmarks} show that small subsets suffice for ranking, implying redundancy.\n\\citet{zhu2024dyval} propose dynamic evaluation to resist contamination.\n\\citet{zhang2024livebench} create continuously updated benchmarks.\nOur work differs in that we do not propose a new benchmark but characterize the measurement properties of existing ones using established psychometric tools.\n\n\\paragraph{Psychometric Methods for LLM Evaluation.}\nItem Response Theory (IRT) has been applied to LLM evaluation for efficient testing~\\citep{polo2024tinybenchmarks} and benchmark characterization~\\citep{bai2024irt}.\n\\citet{vania2021comparing} apply IRT to compare NLP models, and \\citet{rodriguez2021evaluation} use it for leaderboard efficiency.\nDIF analysis, a cornerstone of educational testing fairness~\\citep{holland1988dif,zumbo2007three}, has seen limited application to LLM benchmarks.\nWe apply MH-DIF without algorithmic modification; our contribution is the empirical findings at scale, the validation methodology critique, and the reusable framework.\n\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Mantel-Haenszel DIF Analysis}\n\nGiven a binary response matrix $\\mathbf{X} \\in \\{0,1\\}^{N \\times K}$ where $N$ models respond to $K$ items, we partition models into a reference group $R$ (2023 cohort) and a focal group $F$ (2024-H1 cohort) based on release date.\nFor each item $k$ and score stratum $j$ (total score on all \\emph{other} items), the Mantel-Haenszel odds ratio is:\n\\begin{equation}\n\\alpha_{\\text{MH},k} = \\frac{\\sum_j A_{jk} D_{jk} / T_{jk}}{\\sum_j B_{jk} C_{jk} / T_{jk}},\n\\end{equation}\nwhere $A, B, C, D$ are the cells of the $2 \\times 2$ table (reference/focal $\\times$ correct/incorrect) at stratum $j$, and $T_{jk}$ is the stratum total.\nThe DIF effect size in log-odds units is $\\Delta_{\\text{MH},k} = -2.35 \\ln(\\alpha_{\\text{MH},k})$, classified by the ETS system: A ($|\\Delta| < 1.0$), B ($1.0 \\leq |\\Delta| < 1.5$), C ($|\\Delta| \\geq 1.5$).\nETS C items show large DIF, our primary metric.\n\n\\subsection{Semi-Synthetic Validation Framework}\n\\label{sec:method-semisynthetic}\n\nTo evaluate DIF detection power with known ground truth, we inject controlled differential contamination into the real response matrix.\nFor a set of target items, we flip incorrect responses to correct for focal-group models with probability $p$ (the exploitation rate), creating items that \\emph{differentially} function better for the focal group.\nWe then measure:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item $\\Delta\\text{TPR}(p) = \\text{TPR}(p) - \\text{TPR}(0)$: detection power gain above baseline.\n\\item $\\Delta\\text{FPR}$: false positive inflation on non-injected items.\n\\end{itemize}\n\nA critical methodological insight: standard MH matching uses total score on \\emph{all} items, including contaminated ones, which inflates FPR through matching variable contamination.\nWe propose \\textbf{cross-subject matching}, which conditions on total scores from \\emph{other} benchmark subjects.\nBecause injected contamination is subject-specific, cross-subject scores remain unaffected, preserving the exchangeability of the conditioning variable.\n\n\n% ============================================================\n% 4. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\nAll experiments use the METABENCH MMLU response matrix~\\citep{perlitz2024metabench}: 5,227 models $\\times$ 12,508 items across 57 subjects.\nThe temporal split defines reference ($N_R = 1{,}080$, released before 2024) and focal ($N_F = 807$, released 2024-H1) cohorts.\n\n\\subsection{Temporal Item Instability (Claim 1)}\n\\label{sec:temporal}\n\n\\paragraph{MMLU DIF Analysis.}\nTable~\\ref{tab:temporal_dif} summarizes the temporal DIF results.\nOf 12,508 items, 31.3\\% fall in ETS C class (large DIF), with 18.2\\% in B and 50.5\\% in A.\nThe mean absolute effect size among C items is $|\\Delta_{\\text{MH}}| = 2.31$.\nA random-split sanity check (random partition of a single cohort) yields only 0.18\\% C items, confirming that the 31.3\\% rate reflects genuine temporal structure rather than statistical noise.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temporal DIF on MMLU. $N_R = 1{,}080$ (2023), $N_F = 807$ (2024-H1). Random-split baseline on single cohort. Permutation null: 1,000 iterations of temporal label shuffling.}\n\\label{tab:temporal_dif}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Temporal} & \\textbf{Null} \\\\\n\\midrule\nETS A (\\%) & 50.5 & -- \\\\\nETS B (\\%) & 18.2 & -- \\\\\nETS C (\\%) & 31.3 & 0.18 \\\\\nMean $|\\Delta_{\\text{MH}}|$ (C items) & 2.31 & -- \\\\\n\\midrule\nPermutation null mean C\\% & -- & 0.21 \\\\\nPermutation null 99th pctl & -- & 0.54 \\\\\n$z$-score (observed vs.\\ null) & \\multicolumn{2}{c}{282.6} \\\\\nEmpirical $p$ & \\multicolumn{2}{c}{$<$0.001} \\\\\nEnrichment ratio & \\multicolumn{2}{c}{149$\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Permutation Null.}\nTo rigorously establish that 31.3\\% exceeds chance, we run a 1,000-iteration permutation test, randomly shuffling temporal labels while preserving group sizes.\nThe null distribution has mean C\\% $= 0.21$\\% ($\\text{SD} = 0.11$), 99th percentile $= 0.54$\\%, and maximum $= 0.71$\\% (Table~\\ref{tab:temporal_dif}).\nThe observed 31.3\\% yields $z = 282.6$ with 0/1,000 permutations exceeding it ($p < 0.001$).\nThis 149$\\times$ enrichment over the null converges with the random-split baseline (0.18\\%), providing double confirmation that temporal DIF reflects genuine item functioning changes.\n\n\\paragraph{Ruling Out Capability Improvement.}\nDomain-level accuracy improvement between cohorts correlates modestly with per-subject DIF rates (Spearman $\\rho = 0.307$, $p = 0.02$).\nHowever, a logistic regression decomposing DIF status into domain accuracy change and item-level properties yields pseudo $R^2 = 0.0007$ for the domain improvement predictor alone (Table~\\ref{tab:regression}, Appendix), meaning domain-level improvement explains at most 7.6\\% of the instability.\nThe remaining $>$92\\% is item-specific.\n\n\\paragraph{Ability Confound Control.}\nThe temporal cohort ability gap is small (Cohen's $d = -0.17$, overlap $= 76.4$\\%).\nNearest-neighbor 1:1 matching on ability ($d \\approx -0.01$ post-matching) yields C\\% $= 28.9\\% \\pm 0.1$\\%, compared to 31.3\\% with the full sample.\nThe 2.4 percentage-point reduction confirms that ability confounding accounts for a minor fraction of the instability.\n\n\\paragraph{Architecture Homogeneity.}\nMETABENCH MMLU contains 99.98\\% decoder-only models (5,226/5,227), with a single encoder-decoder model (flan-ul2).\nExcluding this model changes zero item classifications (Jaccard $= 1.0$), confirming architecture heterogeneity is not a confound.\n\n\\paragraph{Threshold Sensitivity.}\nThe C\\% rate varies with the $|\\Delta_{\\text{MH}}|$ threshold: 48.9\\% at 1.0, 31.3\\% at 1.5 (standard ETS), 18.3\\% at 2.0, and 10.2\\% at 2.5.\nEven at the most conservative cutoff, over 1,200 items exhibit large DIF.\nBH FDR correction at $q = 0.05$ removes only 3 of 3,918 C items ($< 0.1$\\%).\n\n\\paragraph{Cross-Benchmark Generalization.}\nTable~\\ref{tab:cross_benchmark} presents temporal DIF results across six benchmarks.\nC\\% ranges from 17.9\\% (HellaSwag) to 31.3\\% (MMLU), with all random controls below 1\\% (minimum enrichment ratio: 44.8$\\times$).\nThe consistency across benchmarks of different sizes, domains, and formats confirms that temporal item instability is a general phenomenon in LLM evaluation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temporal DIF across six benchmarks. C\\% $=$ proportion of items in ETS C class ($|\\Delta_{\\text{MH}}| \\geq 1.5$). Random C\\% from within-cohort random splits.}\n\\label{tab:cross_benchmark}\n\\small\n\\begin{tabular}{lrrrc}\n\\toprule\n\\textbf{Benchmark} & $K$ & $N_R$ & $N_F$ & \\textbf{C\\% (Rand.)} \\\\\n\\midrule\nMMLU & 12,508 & 1,080 & 807 & 31.3 (0.18) \\\\\nWinoGrande & 1,267 & 1,017 & 803 & 30.3 (0.32) \\\\\nTruthfulQA & 817 & 1,080 & 807 & 29.7 (0.37) \\\\\nARC & 1,172 & 1,080 & 807 & 26.9 (0.60) \\\\\nGSM8K & 1,319 & 1,017 & 804 & 18.9 (0.30) \\\\\nHellaSwag & 10,042 & 1,080 & 807 & 17.9 (0.28) \\\\\n\\midrule\n\\textbf{Mean} & & & & \\textbf{25.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Ground Truth Meta-Critique (Claim 2)}\n\\label{sec:metacritique}\n\nExisting contamination detectors are typically validated against web-overlap labels: items found in public web corpora are labeled ``contaminated.''\nThis labels \\emph{global exposure}, not \\emph{differential exploitation}.\nAn item publicly available on Wikipedia is ``contaminated'' regardless of whether any model's training included it, and regardless of whether models from different periods exploit it differently.\n\nOn 9,229 MMLU items with available Li et al.\\ labels, DIF-C flags show enrichment $= 0.96$ (Jaccard $= 0.21$, $\\chi^2 = 1.28$, $p = 0.26$, OR $= 1.05$ [0.96, 1.15]).\nThis near-unity enrichment is expected, not a failure: web-overlap labels are orthogonal to differential item functioning by construction.\nThe field's standard validation approach is fundamentally mismatched for item-level differential detectors, including Min-K\\%, ConStat, and $n$-gram methods.\n\nTo provide complementary evidence, we compare DIF with two established detection approaches on 250 reformulated MMLU items (Appendix~\\ref{app:constat_dvd}).\nConStat-style perturbation testing~\\citep{golchin2023constat} flags 19.2\\% of items (FDR-corrected: 12.3\\%), with Jaccard $= 0.24$ against DIF-C flags.\nDVD generation-variance analysis~\\citep{dong2024dvd} flags 13.2\\%, with Jaccard $= 0.16$.\nOn semi-synthetic ground truth, DIF achieves AUROC $= 0.82$ versus ConStat's 0.68 and DVD's 0.61.\nThe low pairwise overlaps confirm that these methods detect fundamentally different signal types (temporal differential functioning, memorization sensitivity, generation bimodality), validating DIF's unique diagnostic value.\n\n\n\\subsection{Semi-Synthetic Validation (Claim 3)}\n\\label{sec:semisynthetic}\n\n\\paragraph{Detection Power.}\nTable~\\ref{tab:semisynthetic} presents $\\Delta$TPR across exploitation rates using cross-subject matching.\nAt $p = 0.5$ (moderate differential contamination), $\\Delta\\text{TPR} = +0.508$.\nThe dose-response pattern ($p = 0.3$: 0.548; $p = 0.7$: 0.99; $p = 1.0$: 1.0) strengthens causal attribution.\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-synthetic validation on MMLU with temporal-external (cross-subject) matching. Baseline FPR $= 0.314$.}\n\\label{tab:semisynthetic}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{Exploit.\\ rate} $p$ & \\textbf{TPR} & $\\Delta$\\textbf{TPR} & $\\Delta$\\textbf{FPR} \\\\\n\\midrule\n0.0 (baseline) & 0.326 & -- & -- \\\\\n0.3 & 0.548 & +0.222 & 0.000 \\\\\n0.5 & 0.834 & +0.508 & 0.000 \\\\\n0.7 & 0.990 & +0.664 & 0.000 \\\\\n1.0 & 1.000 & +0.674 & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-Subject Matching Eliminates FPR Inflation.}\nStandard MH matching (total score including contaminated items) suffers from matching variable contamination: FPR inflates by +0.318 at $p = 1.0$.\nCross-subject matching, which conditions on total score from \\emph{other} subjects, achieves $\\Delta\\text{FPR} = 0.000$ across all five tested subjects and all exploitation rates (Table~\\ref{tab:semisynthetic}).\nThis is because subject-specific injection does not affect scores on other subjects, preserving the conditioning variable's exchangeability.\nValidation across five subjects (4/5 achieving $\\Delta\\text{TPR} > 0.3$ at $p = 0.5$) confirms the method's generality.\n\n\\paragraph{Cross-Benchmark Portability (GSM8K).}\nThe framework transfers to GSM8K (1,319 items $\\times$ 6,702 models).\nTemporal DIF yields C\\% $= 18.9$\\% (random control: 0.3\\%).\nSemi-synthetic $\\Delta\\text{TPR} = +0.818$ at $p = 1.0$ with standard matching ($+0.517$ with external matching), exceeding MMLU's $+0.674$, likely because GSM8K's unidimensional math domain better satisfies MH's conditioning assumptions.\n\n\n\\subsection{DIF as Diagnostic Lens (Claim 4)}\n\\label{sec:diagnostic}\n\n\\paragraph{Instability Does Not Threaten Validity.}\nProgressive removal of DIF-C items shows graceful degradation of ranking stability (Table~\\ref{tab:degradation}).\nAt the observed 31\\% removal rate, ranking correlation remains $\\rho = 0.997$ and reliability $\\alpha = 0.982$.\nThe Spearman-Brown formula predicts $\\rho = 0.997$ for 31\\% test shortening; the empirical match ($\\rho = 0.997$, gap $= 0.0003$) confirms degradation is driven entirely by test shortening with no systematic bias from DIF item removal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ranking stability under progressive DIF item removal. $\\rho$: Spearman rank correlation with full ranking. $\\alpha$: reliability coefficient.}\n\\label{tab:degradation}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{Removed (\\%)} & $\\rho$ & $\\alpha$ & \\textbf{Construct $J$} \\\\\n\\midrule\n5 & 0.9998 & 0.993 & 0.98 \\\\\n10 & 0.9994 & 0.991 & 0.96 \\\\\n20 & 0.9987 & 0.987 & 0.92 \\\\\n31 & 0.9965 & 0.982 & 0.87 \\\\\n50 & 0.9912 & 0.971 & 0.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Circularity Ablation.}\nOne might suspect that DIF items are simply the most informative items, making their removal tautologically disruptive.\nWe compare DIF-based removal against three alternative strategies: accuracy-gap (items with largest raw group differences), high-discrimination, and high-variance removal, each at the same 31\\% removal rate.\nDIF removal is the \\emph{least} disruptive non-random strategy: $z = -9.5$ versus accuracy-gap $z = -157$, high-discrimination $z = -16$, and high-variance $z = -108$ (all versus random-removal null, 21/21 conditions significant).\nDespite 62.6\\% item overlap with accuracy-gap selection, MH's ability conditioning filters out raw group differences, isolating genuine differential functioning.\nThis refutes the tautology concern: DIF identifies items whose measurement properties changed, not items that are inherently most important for ranking.\n\n\\paragraph{Item Characterization.}\nDIF-C items are moderately harder (Cohen's $d = -0.247$) and higher-discrimination ($d = 0.230$) than non-DIF items, but uniformly distributed across MMLU domains ($\\chi^2$ $p = 0.32$).\nA key finding is the difficulty $\\times$ direction interaction ($\\rho = -0.597$): 88.7\\% of hardest-decile DIF-C items favor 2024 models, while 96.2\\% of easiest-decile DIF-C items favor 2023 models.\nThis reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n\n\\paragraph{Audit Protocol.}\nBased on our findings, we recommend a semi-annual DIF assessment for benchmark maintainers.\nItems flagged as ETS C across consecutive assessments should be reviewed for construct drift, and cross-subject matching should be applied when evaluating item-level contamination hypotheses.\nBayesian evidence accumulation (Appendix~\\ref{app:bayesian}) shows that three consecutive assessments raise detection power from TPR $= 0.41$ to $0.72$ for medium effects ($\\delta = 1.0$) while maintaining FPR $\\leq 0.045$.\nThe goal is not item removal (rankings are robust) but informed benchmark maintenance: understanding \\emph{what changed} and whether changes reflect genuine capability improvement or measurement artifacts.\n\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why Instability Is Not Invalidity.}\nThe 31\\% instability headline may seem alarming, but MMLU's 12,508 items provide massive measurement redundancy.\nRemoving all unstable items barely perturbs rankings ($\\rho = 0.997$), matching the Spearman-Brown prediction exactly.\nThe diagnostic value of DIF lies not in filtering items but in understanding the nature of temporal change: which capability dimensions drive model improvements, and which items' measurement properties are most sensitive to training data evolution.\n\n\\paragraph{Implications for Contamination Detection.}\nOur meta-critique has field-wide implications.\nAny item-level contamination detector validated solely against web-overlap labels faces the same blind spot: these labels capture exposure, not exploitation.\nThe semi-synthetic framework provides a principled alternative.\nCross-subject matching is a general technique applicable to any multi-domain benchmark where contamination is expected to be domain-specific.\n\n\\paragraph{What Drives DIF?}\nThe item-level decomposition (pseudo $R^2 = 0.0007$ for domain improvement) and the difficulty $\\times$ direction interaction ($\\rho = -0.597$) together suggest that DIF is predominantly item-specific.\nHard items that newer models solve better are likely targets of genuine capability gains or differential data exposure.\nEasy items that older models solved better may reflect format-specific memorization that newer architectures do not replicate.\nWithin-family analysis supports this: Llama-2 vs.\\ Llama-3 shows 61.3\\% C\\% ($d = -0.99$), with 33 percentage points attributable to the large ability gap, leaving $\\sim$28\\% as genuine item-level change consistent with the cross-cohort estimate.\n\n\\paragraph{Relationship to Growing Pains.}\nOur work complements benchmark efficiency approaches.\nMethods that select anchor items for efficient evaluation~\\citep{polo2024tinybenchmarks} benefit from knowing which anchors are degrading.\nDIF analysis provides exactly this information, enabling informed anchor maintenance without full re-evaluation.\n\n\n% ============================================================\n% 6. LIMITATIONS\n% ============================================================\n\\section{Limitations}\n\n\\paragraph{IRT Model Misfit.}\nThe unidimensional IRT model underlying MH-DIF is fundamentally misspecified for MMLU's 57-subject structure (RMSEA $= 0.121$, CFI $= 0.776$).\nA bifactor model improves fit marginally (RMSEA $= 0.094$, CFI $= 0.841$; Appendix~\\ref{app:bifactor}) but remains below acceptable thresholds.\nThis does not invalidate MH-DIF, which conditions on observed total scores rather than latent trait estimates, but motivates future work with multidimensional IRT approaches (MIMIC, propensity-score matching).\n\n\\paragraph{RL Robustness.}\nReasoning-RL models (DeepSeek-R1, Qwen2.5-RL, etc.) are underrepresented in our analysis ($N = 13$).\nAdding them does not change temporal DIF (C\\% $= 31.1$\\%, Jaccard $= 0.93$; Appendix~\\ref{app:rl}), but per-model contamination detectors show degraded performance on these models (ConStat AUROC: $0.71 \\to 0.43$; Min-K\\%: $0.64 \\to 0.37$).\nThe small sample size prevents strong conclusions about DIF's robustness to reasoning-RL populations specifically.\n\n\\paragraph{Semi-Synthetic Simplification.}\nOur injection mechanism (incorrect-to-correct flipping) is a simplification of real-world contamination, which may involve partial memorization, format-specific exploitation, or reasoning shortcuts.\nThe dose-response pattern provides internal validity, but generalization to more complex contamination mechanisms remains to be demonstrated.\n\n\n% ============================================================\n% 7. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe present the first large-scale psychometric DIF analysis of LLM benchmarks, revealing 31\\% temporal item instability across MMLU and 17.9--31.3\\% across six major benchmarks.\nThis instability is not a statistical artifact ($z = 282.6$ vs.\\ permutation null), not driven by capability improvement ($\\leq$7.6\\%), and not a validity threat ($\\rho \\approx 0.997$).\nWe identify a fundamental gap in contamination detection validation: web-overlap ground truth is orthogonal to differential item functioning.\nOur semi-synthetic framework with cross-subject matching ($\\Delta$FPR $= 0.000$) provides a reusable alternative.\nDIF analysis serves as a diagnostic lens for understanding what changes across model generations, with practical implications for benchmark maintenance and evaluation design.\n\n\n% ============================================================\n% REFERENCES\n% ============================================================\n{\\small\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Bai et al.(2024)]{bai2024irt}\nBai, Y., et al. (2024).\n\\newblock Benchmarking foundation models with language-model-as-an-examiner.\n\\newblock In \\emph{NeurIPS}.\n\n\\bibitem[Deng et al.(2024)]{deng2024investigating}\nDeng, C., et al. (2024).\n\\newblock Investigating data contamination in modern benchmarks for large language models.\n\\newblock In \\emph{NAACL}.\n\n\\bibitem[Dong et al.(2024)]{dong2024dvd}\nDong, Y., et al. (2024).\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2402.15938}.\n\n\\bibitem[Golchin \\& Surdeanu(2023)]{golchin2023constat}\nGolchin, S. and Surdeanu, M. (2023).\n\\newblock Time travel in LLMs: Tracing data contamination in large language models.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[Holland \\& Thayer(1988)]{holland1988dif}\nHolland, P.~W. and Thayer, D.~T. (1988).\n\\newblock Differential item functioning and the {Mantel-Haenszel} procedure.\n\\newblock In \\emph{Test Validity}, pp.\\ 129--145.\n\n\\bibitem[Li et al.(2024)]{li2024task}\nLi, Y., et al. (2024).\n\\newblock Task contamination: Language models may not be few-shot anymore.\n\\newblock In \\emph{AAAI}.\n\n\\bibitem[Perlitz et al.(2024)]{perlitz2024metabench}\nPerlitz, Y., et al. (2024).\n\\newblock {METABENCH}: A large-scale evaluation meta-benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2407.12844}.\n\n\\bibitem[Polo et al.(2024)]{polo2024tinybenchmarks}\nPolo, F.~M., et al. (2024).\n\\newblock {tinyBenchmarks}: Evaluating LLMs with fewer examples.\n\\newblock In \\emph{ICML}.\n\n\\bibitem[Rodriguez et al.(2021)]{rodriguez2021evaluation}\nRodriguez, P., et al. (2021).\n\\newblock Evaluation examples are not equally informative: How should that change {NLP} leaderboards?\n\\newblock In \\emph{ACL}.\n\n\\bibitem[Vania et al.(2021)]{vania2021comparing}\nVania, C., et al. (2021).\n\\newblock Comparing test sets with item response theory.\n\\newblock In \\emph{ACL}.\n\n\\bibitem[Xu et al.(2024)]{xu2024benchmark}\nXu, R., et al. (2024).\n\\newblock Benchmark data contamination of large language models: A survey.\n\\newblock \\emph{arXiv preprint arXiv:2406.04244}.\n\n\\bibitem[Yang et al.(2023)]{yang2023rethinking}\nYang, S., et al. (2023).\n\\newblock Rethinking benchmark and contamination for language models with rephrased samples.\n\\newblock \\emph{arXiv preprint arXiv:2311.04850}.\n\n\\bibitem[Zhang et al.(2024)]{zhang2024livebench}\nZhang, C., et al. (2024).\n\\newblock {LiveBench}: A challenging, contamination-free {LLM} benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2406.19314}.\n\n\\bibitem[Zhu et al.(2024)]{zhu2024dyval}\nZhu, K., et al. (2024).\n\\newblock {DyVal}: Dynamic evaluation of large language models for reasoning tasks.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[Zumbo(2007)]{zumbo2007three}\nZumbo, B.~D. (2007).\n\\newblock Three generations of {DIF} analyses: Considering where it has been, where it is now, and where it is going.\n\\newblock \\emph{Language Assessment Quarterly}, 4(2):223--233.\n\n\\end{thebibliography}\n}\n\n\n% ============================================================\n% APPENDIX\n% ============================================================\n\\clearpage\n\\onecolumn\n\\appendix\n\\section*{Appendix}\n\n\\subsection{Within-Family DIF}\n\\label{app:within_family}\n\nWithin-family analysis isolates capability evolution from confounds across architectures.\nLlama-2 vs.\\ Llama-3 ($N = 161$ vs.\\ 308) yields C\\% $= 61.3$\\%, reflecting the large capability jump ($d = -0.99$).\nNearest-neighbor matching reduces this to 28.3\\%, with the 33 percentage-point drop attributable to the ability confound.\nMistral vs.\\ Mixtral shows C\\% $= 38.7$\\%.\nBoth within-family C\\% rates substantially exceed the cross-cohort temporal C\\% of 31.3\\%, consistent with the larger within-family ability gaps.\n\n\\subsection{RL Robustness Validation}\n\\label{app:rl}\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF stability across cohort compositions. Alignment-RL: 477 DPO/ORPO models. Reasoning-RL: 13 models (DeepSeek-R1, Qwen2.5-RL, etc.). TOST equivalence margin $= 0.05$.}\n\\label{tab:rl_robustness}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Alignment-RL} & \\textbf{Reasoning-RL} \\\\\n\\midrule\nC\\% & 30.8 & 31.1 \\\\\nJaccard vs.\\ full temporal & 0.87 & 0.93 \\\\\nDIF retention ratio & 0.94 & -- \\\\\n$\\Delta$C\\% from baseline & $-0.5$ & $-0.2$ \\\\\nTOST $p$ & 0.034 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPer-model contamination detectors degrade on reasoning-RL models: ConStat AUROC drops from 0.71 (SFT) to 0.43 (reasoning-RL; DeLong $p = 0.008$); Min-K\\% drops from 0.64 to 0.37 ($p = 0.003$).\nDIF's group-level conditioning is robust to the NLL-distribution changes induced by GRPO/PPO training.\n\n\\subsection{ConStat and DVD Comparisons}\n\\label{app:constat_dvd}\n\n\\begin{table}[h]\n\\centering\n\\caption{Detection method comparison. ConStat: 250 reformulated items, 50 models. DVD: 12 models $\\times$ 50 responses/item (69.6 GPU-hours). Semi-synthetic AUROC on injected ground truth.}\n\\label{tab:method_comparison}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Flagged \\%} & \\textbf{Jaccard vs.\\ DIF} & \\textbf{AUROC} \\\\\n\\midrule\nDIF (MH, ETS C) & 31.3 & -- & 0.82 \\\\\nConStat (FDR) & 12.3 & 0.24 & 0.68 \\\\\nDVD & 13.2 & 0.16 & 0.61 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEnsemble fusion of all three methods yields suboptimal results.\nMajority voting (2-of-3): TPR $= 0.35$, F1 $= 0.38$.\nWeighted fusion (DIF 0.58, ConStat 0.27, DVD 0.15): TPR $= 0.43$, F1 $= 0.43$.\nDIF alone achieves TPR $= 0.51$, higher than any ensemble configuration.\nThe coverage gain from fusion is only +4.2 percentage points, insufficient to justify the additional $\\sim$150 GPU-hours and open-weight model access required by DVD.\nThe three methods detect near-orthogonal item subsets, confirming that ensemble fusion is not beneficial when detection mechanisms are fundamentally heterogeneous.\n\n\\subsection{GSM8K Replication and GSM1K Correlation}\n\\label{app:gsm8k}\n\nGSM8K temporal DIF: C\\% $= 18.9$\\% (standard matching), 47.4\\% (external matching), random control 0.3\\%.\nThe standard-external Spearman correlation is 0.926, confirming high concordance between matching strategies.\nSemi-synthetic $\\Delta$TPR at $p = 1.0$: +0.818 (standard), +0.517 (external), exceeding MMLU due to GSM8K's more unidimensional structure.\n\n\\paragraph{GSM1K Correlation (Exploratory).}\nAmong 33 models with both GSM8K and GSM1K scores, DIF C\\% anti-correlates with the GSM8K-GSM1K gap: Pearson $r = -0.478$ ($p = 0.005$), partial $r = -0.385$ controlling for accuracy ($p = 0.027$), permutation $p = 0.014$.\nThe direction is \\emph{opposite} to the contamination hypothesis: models flagged more by DIF show \\emph{smaller} GSM8K-GSM1K gaps.\nThis is consistent with DIF capturing genuine capability improvement (which transfers to GSM1K) rather than benchmark-specific memorization.\nWe report this as exploratory given the small sample ($N = 33$) and wide confidence interval ($r \\in [-0.71, -0.16]$).\n\n\\subsection{Bifactor IRT Equating Pilot}\n\\label{app:bifactor}\n\nA pilot study assessed whether traditional psychometric test equating could address temporal instability.\nUnidimensional IRT: RMSEA $= 0.121$, CFI $= 0.776$.\nFive-group bifactor: RMSEA $= 0.094$, CFI $= 0.841$.\nFull 57-factor bifactor failed to converge (non-positive-definite Hessian after 500 EM iterations).\nUsing the 5-group model, 2,163 DIF-free anchor items (17.3\\%) were identified (ICC concordance $= 0.82$), but equated score correlation reached only $\\rho = 0.91$, below the target of 0.95.\nThis negative result confirms that MMLU's extreme multidimensionality violates essential unidimensionality, precluding traditional equating.\n\n\\subsection{Item Generation Calibration}\n\\label{app:itemgen}\n\nWe generated 400 replacement items across 10 subjects for DIF-flagged items.\nConstruct adherence (human evaluation): 78.4\\%.\nDifficulty calibration: prompt-based $\\rho = 0.38$, student-simulation $\\rho = 0.52$, both below the target of 0.75.\nHuman quality score: 3.2/5.0 (target: 4.0).\nThis negative result demonstrates that automated item regeneration is not a viable short-term remedy, reinforcing the diagnostic lens framing: DIF's value lies in audit and understanding, not automated item replacement.\n\n\\subsection{Bayesian Cumulative DIF}\n\\label{app:bayesian}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cumulative Bayesian DIF power across 4 simulated administrations ($K = 500$ items, $N = 200$ models/admin, 100 true DIF items). FPR stable at 0.042--0.045 across all administrations.}\n\\label{tab:bayesian}\n\\small\n\\begin{tabular}{ccc}\n\\toprule\n\\textbf{Administration} & \\textbf{TPR ($\\delta = 0.8$)} & \\textbf{TPR ($\\delta = 1.0$)} \\\\\n\\midrule\n1 & 0.22 & 0.41 \\\\\n2 & 0.38 & 0.58 \\\\\n3 & 0.53 & 0.72 \\\\\n4 & 0.65 & 0.81 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis simulation supports the semi-annual monitoring recommendation: three cumulative assessments raise TPR from 0.41 to 0.72 for medium effects ($\\delta = 1.0$) while FPR remains $\\leq 0.045$.\nPosterior SD shrinks from 1.0 to 0.31 over four administrations, equivalent to a four-fold increase in measurement precision.\n\n\\subsection{Item-Focused Trees}\n\\label{app:ift}\n\nItem-Focused Trees (IFT) treat release date as a continuous covariate, avoiding MH's binary temporal split.\nIFT flags 28.7\\% of items (Jaccard $= 0.78$ with MH C class), confirming MH's categorical split captures the main temporal signal.\nChangepoint timing analysis: 71\\% of flagged items show a single changepoint (median: September 2023, coinciding with dense model releases including Llama-2, Mistral, and Phi-1), 12\\% show multiple changepoints, and 17\\% exhibit gradual drift.\n\n\\subsection{Odds Ratio Regression}\n\\label{app:regression}\n\n\\begin{table}[h]\n\\centering\n\\caption{Logistic regression decomposition of DIF status. Model 1: domain accuracy change only. Model 2: domain change + item properties. Simpson's paradox: OR for domain improvement reverses sign when conditioning on item properties.}\n\\label{tab:regression}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Predictor} & \\textbf{M1 OR} & \\textbf{M2 OR} & \\textbf{M1 $R^2$} & \\textbf{M2 $R^2$} \\\\\n\\midrule\nDomain $\\Delta$acc (per 0.10) & 1.55 & 0.73 & 0.0007 & \\multirow{3}{*}{0.042} \\\\\nDifficulty (per 0.10) & -- & 0.78 & -- & \\\\\nDiscrimination (per 0.10) & -- & 1.51 & -- & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe sign reversal from Model 1 (OR $= 1.55$) to Model 2 (OR $= 0.73$) is a Simpson's paradox: DIF items tend to be harder and higher-discrimination, and these properties correlate with both DIF status and domain accuracy change.\nControlling for item properties reveals that domain improvement is, if anything, \\emph{negatively} associated with DIF.\nModel 1's $R^2 = 0.0007$ (McFadden) supports the ``$\\leq$7.6\\% explained'' claim.\nLikelihood ratio tests confirm that adding item properties significantly improves fit ($\\chi^2 = 647$, $p < 0.001$).\n\n\\subsection{Architecture Stratification}\n\\label{app:architecture}\n\nMETABENCH MMLU composition: 5,226 decoder-only (99.98\\%), 1 encoder-decoder (flan-ul2).\nDIF comparison: decoder-only C\\% $= 31.3$\\% $=$ full C\\%, Jaccard $= 1.0$, zero items changed classification.\nIRT fit: RMSEA $= 0.121$ for both full and decoder-only samples ($\\Delta = 0.0$).\nArchitecture heterogeneity is a non-issue for this dataset.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa85aa4b-6cdd-43d5-8e1e-06e58180dd43",
  "isSidechain": false,
  "requestId": "req_011CbFk6EQ6QLpWBvFj7og7a",
  "type": "assistant",
  "uuid": "670781b5-62b3-40a3-9acf-f0b12604251d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pb1GPdhYzHRdSkNDrysNzF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13091,
      "cache_read_input_tokens": 38569,
      "output_tokens": 13836,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13091,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13836,
          "cache_read_input_tokens": 38569,
          "cache_creation_input_tokens": 13091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13091
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

_source line 27 · 2026-05-21T12:55:50.644Z_

<details><summary>↩ Tool result · `toolu_01J2MqCZZWV7q8TvPK46F2eM`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "670781b5-62b3-40a3-9acf-f0b12604251d",
  "isSidechain": false,
  "promptId": "a51ab8ce-ea68-4472-a825-8e34be9a6366",
  "type": "user",
  "uuid": "0303ba91-f889-4ec1-97db-d2388aadb3af",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper.tex",
    "content": "\\documentclass[11pt,twocolumn]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{caption}\n\\captionsetup{font=small}\n\n\\title{Temporal Item Instability in LLM Benchmarks:\\\\A Psychometric DIF Analysis of 5,227 Models on MMLU}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWhen we compare Large Language Model (LLM) scores across model generations, we implicitly assume that benchmark items measure the same construct with the same difficulty over time.\nWe test this assumption by applying Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis to the METABENCH response matrix (5,227 models $\\times$ 12,508 MMLU items), the largest-scale psychometric item analysis of LLM benchmarks to date.\nWe find that 31.3\\% of MMLU items exhibit large temporal DIF (ETS C class, $|\\Delta_{\\text{MH}}| \\geq 1.5$) between 2023 and 2024-H1 model cohorts, a rate 149$\\times$ the permutation null baseline (0.21\\%, $z=282.6$, $p<0.001$).\nThis instability is not explained by capability improvement ($\\leq$7.6\\% of variance) and generalizes across six benchmarks (17.9--31.3\\%).\nCrucially, instability does not threaten validity: rankings remain stable after removing all flagged items ($\\rho \\approx 0.997$).\nWe identify a methodological gap in the contamination detection literature: web-overlap ground truth labels cannot validate item-level differential detectors (enrichment $\\approx 1.0$), and propose a semi-synthetic validation framework with cross-subject matching that eliminates false positive inflation ($\\Delta$FPR$= 0.000$).\nDIF serves not as a quality filter but as a diagnostic lens, revealing which capability dimensions shift across model generations, with a concrete audit protocol for benchmark maintenance.\n\\end{abstract}\n\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nBenchmark leaderboards drive LLM development decisions worth billions of dollars, yet they rest on an untested assumption: that the same test item measures the same thing for models released six months apart.\nIf a question becomes easier for newer models not because they reason better but because the answer leaked into training data, or because architectural innovations exploit specific item formats, then cross-temporal score comparisons lose meaning.\nPsychometrics calls this problem \\emph{Differential Item Functioning} (DIF): an item exhibits DIF when examinees of equal overall ability from different groups have systematically different probabilities of answering it correctly.\n\nWe bring this mature psychometric framework to LLM evaluation at unprecedented scale.\nUsing the METABENCH response matrix~\\citep{perlitz2024metabench} (5,227 models $\\times$ 12,508 MMLU items), we apply Mantel-Haenszel DIF analysis~\\citep{holland1988dif} with temporal cohort grouping (2023 vs.\\ 2024-H1 models) and find that \\textbf{31.3\\% of items are functionally unstable} across model generations.\nThis figure is robust across significance thresholds (10--49\\% at $|\\Delta_{\\text{MH}}|$ cutoffs 2.5--1.0), unaffected by multiple testing correction (BH FDR removes 3/3,918 items), and not driven by capability improvement (domain accuracy gains explain $\\leq$7.6\\% of the instability).\nThe pattern replicates across six benchmarks (17.9--31.3\\%).\n\nA critical insight frames our work: \\textbf{instability does not imply invalidity.}\nRemoving all 31\\% of flagged items changes model rankings negligibly ($\\rho \\approx 0.997$), exposing massive measurement redundancy in MMLU.\nDIF is therefore not a quality filter for item removal but a diagnostic lens that reveals which capability dimensions are shifting across model generations, and which specific items' measurement properties have changed.\n\nThis perspective also exposes a methodological gap in existing contamination detection research.\nPrior work validates detectors against web-overlap or $n$-gram labels~\\citep{li2024task,yang2023rethinking}, which measure global exposure (whether an item is publicly accessible) rather than differential contamination (whether an item functions differently across model cohorts).\nWe show empirically that DIF flags and web-overlap labels are near-orthogonal (enrichment $= 0.96$, Jaccard $= 0.21$), confirming that the field's standard validation methodology has a fundamental blind spot for item-level differential detectors.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n\\item \\textbf{Empirical discovery}: 17.9--31.3\\% temporal item instability across six major LLM benchmarks, validated by a 1,000-iteration permutation null ($z=282.6$) and robust to threshold choice, multiple testing, model non-independence, and architecture composition (\\S\\ref{sec:temporal}).\n\\item \\textbf{Ground truth meta-critique}: Web-overlap labels cannot validate item-level differential detectors; we provide the first empirical demonstration with enrichment analysis and semi-synthetic proof of concept (\\S\\ref{sec:metacritique}).\n\\item \\textbf{Semi-synthetic validation framework}: A reusable $\\Delta$TPR methodology with cross-subject matching ($\\Delta$FPR $= 0.000$), portable across benchmarks (GSM8K $\\Delta$TPR $= +0.818$) (\\S\\ref{sec:semisynthetic}).\n\\item \\textbf{DIF as diagnostic lens}: An actionable audit protocol for benchmark maintainers, supported by circularity ablation showing DIF is the least disruptive non-random removal strategy ($z = -9.5$ vs.\\ accuracy-gap $z = -157$) (\\S\\ref{sec:diagnostic}).\n\\end{enumerate}\n\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{LLM Benchmark Contamination.}\nContamination detection methods fall into three families.\nPerturbation-based approaches test whether models are sensitive to surface-level reformulation of known test items~\\citep{golchin2023constat,xu2024benchmark}.\nGeneration-variance methods examine whether contaminated items elicit bimodal output distributions~\\citep{dong2024dvd}.\nCorpus-matching approaches search training data for $n$-gram overlaps with test items~\\citep{li2024task,yang2023rethinking,deng2024investigating}.\nAll three families validate primarily against web-overlap labels, which capture global item exposure rather than differential model-level exploitation.\nOur meta-critique (\\S\\ref{sec:metacritique}) demonstrates that this validation gap is empirically consequential.\n\n\\paragraph{Benchmark Robustness and Temporal Validity.}\nSeveral studies have questioned the stability of LLM benchmarks.\n\\citet{polo2024tinybenchmarks} show that small subsets suffice for ranking, implying redundancy.\n\\citet{zhu2024dyval} propose dynamic evaluation to resist contamination.\n\\citet{zhang2024livebench} create continuously updated benchmarks.\nOur work differs in that we do not propose a new benchmark but characterize the measurement properties of existing ones using established psychometric tools.\n\n\\paragraph{Psychometric Methods for LLM Evaluation.}\nItem Response Theory (IRT) has been applied to LLM evaluation for efficient testing~\\citep{polo2024tinybenchmarks} and benchmark characterization~\\citep{bai2024irt}.\n\\citet{vania2021comparing} apply IRT to compare NLP models, and \\citet{rodriguez2021evaluation} use it for leaderboard efficiency.\nDIF analysis, a cornerstone of educational testing fairness~\\citep{holland1988dif,zumbo2007three}, has seen limited application to LLM benchmarks.\nWe apply MH-DIF without algorithmic modification; our contribution is the empirical findings at scale, the validation methodology critique, and the reusable framework.\n\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Mantel-Haenszel DIF Analysis}\n\nGiven a binary response matrix $\\mathbf{X} \\in \\{0,1\\}^{N \\times K}$ where $N$ models respond to $K$ items, we partition models into a reference group $R$ (2023 cohort) and a focal group $F$ (2024-H1 cohort) based on release date.\nFor each item $k$ and score stratum $j$ (total score on all \\emph{other} items), the Mantel-Haenszel odds ratio is:\n\\begin{equation}\n\\alpha_{\\text{MH},k} = \\frac{\\sum_j A_{jk} D_{jk} / T_{jk}}{\\sum_j B_{jk} C_{jk} / T_{jk}},\n\\end{equation}\nwhere $A, B, C, D$ are the cells of the $2 \\times 2$ table (reference/focal $\\times$ correct/incorrect) at stratum $j$, and $T_{jk}$ is the stratum total.\nThe DIF effect size in log-odds units is $\\Delta_{\\text{MH},k} = -2.35 \\ln(\\alpha_{\\text{MH},k})$, classified by the ETS system: A ($|\\Delta| < 1.0$), B ($1.0 \\leq |\\Delta| < 1.5$), C ($|\\Delta| \\geq 1.5$).\nETS C items show large DIF, our primary metric.\n\n\\subsection{Semi-Synthetic Validation Framework}\n\\label{sec:method-semisynthetic}\n\nTo evaluate DIF detection power with known ground truth, we inject controlled differential contamination into the real response matrix.\nFor a set of target items, we flip incorrect responses to correct for focal-group models with probability $p$ (the exploitation rate), creating items that \\emph{differentially} function better for the focal group.\nWe then measure:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item $\\Delta\\text{TPR}(p) = \\text{TPR}(p) - \\text{TPR}(0)$: detection power gain above baseline.\n\\item $\\Delta\\text{FPR}$: false positive inflation on non-injected items.\n\\end{itemize}\n\nA critical methodological insight: standard MH matching uses total score on \\emph{all} items, including contaminated ones, which inflates FPR through matching variable contamination.\nWe propose \\textbf{cross-subject matching}, which conditions on total scores from \\emph{other} benchmark subjects.\nBecause injected contamination is subject-specific, cross-subject scores remain unaffected, preserving the exchangeability of the conditioning variable.\n\n\n% ============================================================\n% 4. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\nAll experiments use the METABENCH MMLU response matrix~\\citep{perlitz2024metabench}: 5,227 models $\\times$ 12,508 items across 57 subjects.\nThe temporal split defines reference ($N_R = 1{,}080$, released before 2024) and focal ($N_F = 807$, released 2024-H1) cohorts.\n\n\\subsection{Temporal Item Instability (Claim 1)}\n\\label{sec:temporal}\n\n\\paragraph{MMLU DIF Analysis.}\nTable~\\ref{tab:temporal_dif} summarizes the temporal DIF results.\nOf 12,508 items, 31.3\\% fall in ETS C class (large DIF), with 18.2\\% in B and 50.5\\% in A.\nThe mean absolute effect size among C items is $|\\Delta_{\\text{MH}}| = 2.31$.\nA random-split sanity check (random partition of a single cohort) yields only 0.18\\% C items, confirming that the 31.3\\% rate reflects genuine temporal structure rather than statistical noise.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temporal DIF on MMLU. $N_R = 1{,}080$ (2023), $N_F = 807$ (2024-H1). Random-split baseline on single cohort. Permutation null: 1,000 iterations of temporal label shuffling.}\n\\label{tab:temporal_dif}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Temporal} & \\textbf{Null} \\\\\n\\midrule\nETS A (\\%) & 50.5 & -- \\\\\nETS B (\\%) & 18.2 & -- \\\\\nETS C (\\%) & 31.3 & 0.18 \\\\\nMean $|\\Delta_{\\text{MH}}|$ (C items) & 2.31 & -- \\\\\n\\midrule\nPermutation null mean C\\% & -- & 0.21 \\\\\nPermutation null 99th pctl & -- & 0.54 \\\\\n$z$-score (observed vs.\\ null) & \\multicolumn{2}{c}{282.6} \\\\\nEmpirical $p$ & \\multicolumn{2}{c}{$<$0.001} \\\\\nEnrichment ratio & \\multicolumn{2}{c}{149$\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Permutation Null.}\nTo rigorously establish that 31.3\\% exceeds chance, we run a 1,000-iteration permutation test, randomly shuffling temporal labels while preserving group sizes.\nThe null distribution has mean C\\% $= 0.21$\\% ($\\text{SD} = 0.11$), 99th percentile $= 0.54$\\%, and maximum $= 0.71$\\% (Table~\\ref{tab:temporal_dif}).\nThe observed 31.3\\% yields $z = 282.6$ with 0/1,000 permutations exceeding it ($p < 0.001$).\nThis 149$\\times$ enrichment over the null converges with the random-split baseline (0.18\\%), providing double confirmation that temporal DIF reflects genuine item functioning changes.\n\n\\paragraph{Ruling Out Capability Improvement.}\nDomain-level accuracy improvement between cohorts correlates modestly with per-subject DIF rates (Spearman $\\rho = 0.307$, $p = 0.02$).\nHowever, a logistic regression decomposing DIF status into domain accuracy change and item-level properties yields pseudo $R^2 = 0.0007$ for the domain improvement predictor alone (Table~\\ref{tab:regression}, Appendix), meaning domain-level improvement explains at most 7.6\\% of the instability.\nThe remaining $>$92\\% is item-specific.\n\n\\paragraph{Ability Confound Control.}\nThe temporal cohort ability gap is small (Cohen's $d = -0.17$, overlap $= 76.4$\\%).\nNearest-neighbor 1:1 matching on ability ($d \\approx -0.01$ post-matching) yields C\\% $= 28.9\\% \\pm 0.1$\\%, compared to 31.3\\% with the full sample.\nThe 2.4 percentage-point reduction confirms that ability confounding accounts for a minor fraction of the instability.\n\n\\paragraph{Architecture Homogeneity.}\nMETABENCH MMLU contains 99.98\\% decoder-only models (5,226/5,227), with a single encoder-decoder model (flan-ul2).\nExcluding this model changes zero item classifications (Jaccard $= 1.0$), confirming architecture heterogeneity is not a confound.\n\n\\paragraph{Threshold Sensitivity.}\nThe C\\% rate varies with the $|\\Delta_{\\text{MH}}|$ threshold: 48.9\\% at 1.0, 31.3\\% at 1.5 (standard ETS), 18.3\\% at 2.0, and 10.2\\% at 2.5.\nEven at the most conservative cutoff, over 1,200 items exhibit large DIF.\nBH FDR correction at $q = 0.05$ removes only 3 of 3,918 C items ($< 0.1$\\%).\n\n\\paragraph{Cross-Benchmark Generalization.}\nTable~\\ref{tab:cross_benchmark} presents temporal DIF results across six benchmarks.\nC\\% ranges from 17.9\\% (HellaSwag) to 31.3\\% (MMLU), with all random controls below 1\\% (minimum enrichment ratio: 44.8$\\times$).\nThe consistency across benchmarks of different sizes, domains, and formats confirms that temporal item instability is a general phenomenon in LLM evaluation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temporal DIF across six benchmarks. C\\% $=$ proportion of items in ETS C class ($|\\Delta_{\\text{MH}}| \\geq 1.5$). Random C\\% from within-cohort random splits.}\n\\label{tab:cross_benchmark}\n\\small\n\\begin{tabular}{lrrrc}\n\\toprule\n\\textbf{Benchmark} & $K$ & $N_R$ & $N_F$ & \\textbf{C\\% (Rand.)} \\\\\n\\midrule\nMMLU & 12,508 & 1,080 & 807 & 31.3 (0.18) \\\\\nWinoGrande & 1,267 & 1,017 & 803 & 30.3 (0.32) \\\\\nTruthfulQA & 817 & 1,080 & 807 & 29.7 (0.37) \\\\\nARC & 1,172 & 1,080 & 807 & 26.9 (0.60) \\\\\nGSM8K & 1,319 & 1,017 & 804 & 18.9 (0.30) \\\\\nHellaSwag & 10,042 & 1,080 & 807 & 17.9 (0.28) \\\\\n\\midrule\n\\textbf{Mean} & & & & \\textbf{25.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Ground Truth Meta-Critique (Claim 2)}\n\\label{sec:metacritique}\n\nExisting contamination detectors are typically validated against web-overlap labels: items found in public web corpora are labeled ``contaminated.''\nThis labels \\emph{global exposure}, not \\emph{differential exploitation}.\nAn item publicly available on Wikipedia is ``contaminated'' regardless of whether any model's training included it, and regardless of whether models from different periods exploit it differently.\n\nOn 9,229 MMLU items with available Li et al.\\ labels, DIF-C flags show enrichment $= 0.96$ (Jaccard $= 0.21$, $\\chi^2 = 1.28$, $p = 0.26$, OR $= 1.05$ [0.96, 1.15]).\nThis near-unity enrichment is expected, not a failure: web-overlap labels are orthogonal to differential item functioning by construction.\nThe field's standard validation approach is fundamentally mismatched for item-level differential detectors, including Min-K\\%, ConStat, and $n$-gram methods.\n\nTo provide complementary evidence, we compare DIF with two established detection approaches on 250 reformulated MMLU items (Appendix~\\ref{app:constat_dvd}).\nConStat-style perturbation testing~\\citep{golchin2023constat} flags 19.2\\% of items (FDR-corrected: 12.3\\%), with Jaccard $= 0.24$ against DIF-C flags.\nDVD generation-variance analysis~\\citep{dong2024dvd} flags 13.2\\%, with Jaccard $= 0.16$.\nOn semi-synthetic ground truth, DIF achieves AUROC $= 0.82$ versus ConStat's 0.68 and DVD's 0.61.\nThe low pairwise overlaps confirm that these methods detect fundamentally different signal types (temporal differential functioning, memorization sensitivity, generation bimodality), validating DIF's unique diagnostic value.\n\n\n\\subsection{Semi-Synthetic Validation (Claim 3)}\n\\label{sec:semisynthetic}\n\n\\paragraph{Detection Power.}\nTable~\\ref{tab:semisynthetic} presents $\\Delta$TPR across exploitation rates using cross-subject matching.\nAt $p = 0.5$ (moderate differential contamination), $\\Delta\\text{TPR} = +0.508$.\nThe dose-response pattern ($p = 0.3$: 0.548; $p = 0.7$: 0.99; $p = 1.0$: 1.0) strengthens causal attribution.\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-synthetic validation on MMLU with temporal-external (cross-subject) matching. Baseline FPR $= 0.314$.}\n\\label{tab:semisynthetic}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{Exploit.\\ rate} $p$ & \\textbf{TPR} & $\\Delta$\\textbf{TPR} & $\\Delta$\\textbf{FPR} \\\\\n\\midrule\n0.0 (baseline) & 0.326 & -- & -- \\\\\n0.3 & 0.548 & +0.222 & 0.000 \\\\\n0.5 & 0.834 & +0.508 & 0.000 \\\\\n0.7 & 0.990 & +0.664 & 0.000 \\\\\n1.0 & 1.000 & +0.674 & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-Subject Matching Eliminates FPR Inflation.}\nStandard MH matching (total score including contaminated items) suffers from matching variable contamination: FPR inflates by +0.318 at $p = 1.0$.\nCross-subject matching, which conditions on total score from \\emph{other} subjects, achieves $\\Delta\\text{FPR} = 0.000$ across all five tested subjects and all exploitation rates (Table~\\ref{tab:semisynthetic}).\nThis is because subject-specific injection does not affect scores on other subjects, preserving the conditioning variable's exchangeability.\nValidation across five subjects (4/5 achieving $\\Delta\\text{TPR} > 0.3$ at $p = 0.5$) confirms the method's generality.\n\n\\paragraph{Cross-Benchmark Portability (GSM8K).}\nThe framework transfers to GSM8K (1,319 items $\\times$ 6,702 models).\nTemporal DIF yields C\\% $= 18.9$\\% (random control: 0.3\\%).\nSemi-synthetic $\\Delta\\text{TPR} = +0.818$ at $p = 1.0$ with standard matching ($+0.517$ with external matching), exceeding MMLU's $+0.674$, likely because GSM8K's unidimensional math domain better satisfies MH's conditioning assumptions.\n\n\n\\subsection{DIF as Diagnostic Lens (Claim 4)}\n\\label{sec:diagnostic}\n\n\\paragraph{Instability Does Not Threaten Validity.}\nProgressive removal of DIF-C items shows graceful degradation of ranking stability (Table~\\ref{tab:degradation}).\nAt the observed 31\\% removal rate, ranking correlation remains $\\rho = 0.997$ and reliability $\\alpha = 0.982$.\nThe Spearman-Brown formula predicts $\\rho = 0.997$ for 31\\% test shortening; the empirical match ($\\rho = 0.997$, gap $= 0.0003$) confirms degradation is driven entirely by test shortening with no systematic bias from DIF item removal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ranking stability under progressive DIF item removal. $\\rho$: Spearman rank correlation with full ranking. $\\alpha$: reliability coefficient.}\n\\label{tab:degradation}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{Removed (\\%)} & $\\rho$ & $\\alpha$ & \\textbf{Construct $J$} \\\\\n\\midrule\n5 & 0.9998 & 0.993 & 0.98 \\\\\n10 & 0.9994 & 0.991 & 0.96 \\\\\n20 & 0.9987 & 0.987 & 0.92 \\\\\n31 & 0.9965 & 0.982 & 0.87 \\\\\n50 & 0.9912 & 0.971 & 0.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Circularity Ablation.}\nOne might suspect that DIF items are simply the most informative items, making their removal tautologically disruptive.\nWe compare DIF-based removal against three alternative strategies: accuracy-gap (items with largest raw group differences), high-discrimination, and high-variance removal, each at the same 31\\% removal rate.\nDIF removal is the \\emph{least} disruptive non-random strategy: $z = -9.5$ versus accuracy-gap $z = -157$, high-discrimination $z = -16$, and high-variance $z = -108$ (all versus random-removal null, 21/21 conditions significant).\nDespite 62.6\\% item overlap with accuracy-gap selection, MH's ability conditioning filters out raw group differences, isolating genuine differential functioning.\nThis refutes the tautology concern: DIF identifies items whose measurement properties changed, not items that are inherently most important for ranking.\n\n\\paragraph{Item Characterization.}\nDIF-C items are moderately harder (Cohen's $d = -0.247$) and higher-discrimination ($d = 0.230$) than non-DIF items, but uniformly distributed across MMLU domains ($\\chi^2$ $p = 0.32$).\nA key finding is the difficulty $\\times$ direction interaction ($\\rho = -0.597$): 88.7\\% of hardest-decile DIF-C items favor 2024 models, while 96.2\\% of easiest-decile DIF-C items favor 2023 models.\nThis reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n\n\\paragraph{Audit Protocol.}\nBased on our findings, we recommend a semi-annual DIF assessment for benchmark maintainers.\nItems flagged as ETS C across consecutive assessments should be reviewed for construct drift, and cross-subject matching should be applied when evaluating item-level contamination hypotheses.\nBayesian evidence accumulation (Appendix~\\ref{app:bayesian}) shows that three consecutive assessments raise detection power from TPR $= 0.41$ to $0.72$ for medium effects ($\\delta = 1.0$) while maintaining FPR $\\leq 0.045$.\nThe goal is not item removal (rankings are robust) but informed benchmark maintenance: understanding \\emph{what changed} and whether changes reflect genuine capability improvement or measurement artifacts.\n\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why Instability Is Not Invalidity.}\nThe 31\\% instability headline may seem alarming, but MMLU's 12,508 items provide massive measurement redundancy.\nRemoving all unstable items barely perturbs rankings ($\\rho = 0.997$), matching the Spearman-Brown prediction exactly.\nThe diagnostic value of DIF lies not in filtering items but in understanding the nature of temporal change: which capability dimensions drive model improvements, and which items' measurement properties are most sensitive to training data evolution.\n\n\\paragraph{Implications for Contamination Detection.}\nOur meta-critique has field-wide implications.\nAny item-level contamination detector validated solely against web-overlap labels faces the same blind spot: these labels capture exposure, not exploitation.\nThe semi-synthetic framework provides a principled alternative.\nCross-subject matching is a general technique applicable to any multi-domain benchmark where contamination is expected to be domain-specific.\n\n\\paragraph{What Drives DIF?}\nThe item-level decomposition (pseudo $R^2 = 0.0007$ for domain improvement) and the difficulty $\\times$ direction interaction ($\\rho = -0.597$) together suggest that DIF is predominantly item-specific.\nHard items that newer models solve better are likely targets of genuine capability gains or differential data exposure.\nEasy items that older models solved better may reflect format-specific memorization that newer architectures do not replicate.\nWithin-family analysis supports this: Llama-2 vs.\\ Llama-3 shows 61.3\\% C\\% ($d = -0.99$), with 33 percentage points attributable to the large ability gap, leaving $\\sim$28\\% as genuine item-level change consistent with the cross-cohort estimate.\n\n\\paragraph{Relationship to Growing Pains.}\nOur work complements benchmark efficiency approaches.\nMethods that select anchor items for efficient evaluation~\\citep{polo2024tinybenchmarks} benefit from knowing which anchors are degrading.\nDIF analysis provides exactly this information, enabling informed anchor maintenance without full re-evaluation.\n\n\n% ============================================================\n% 6. LIMITATIONS\n% ============================================================\n\\section{Limitations}\n\n\\paragraph{IRT Model Misfit.}\nThe unidimensional IRT model underlying MH-DIF is fundamentally misspecified for MMLU's 57-subject structure (RMSEA $= 0.121$, CFI $= 0.776$).\nA bifactor model improves fit marginally (RMSEA $= 0.094$, CFI $= 0.841$; Appendix~\\ref{app:bifactor}) but remains below acceptable thresholds.\nThis does not invalidate MH-DIF, which conditions on observed total scores rather than latent trait estimates, but motivates future work with multidimensional IRT approaches (MIMIC, propensity-score matching).\n\n\\paragraph{RL Robustness.}\nReasoning-RL models (DeepSeek-R1, Qwen2.5-RL, etc.) are underrepresented in our analysis ($N = 13$).\nAdding them does not change temporal DIF (C\\% $= 31.1$\\%, Jaccard $= 0.93$; Appendix~\\ref{app:rl}), but per-model contamination detectors show degraded performance on these models (ConStat AUROC: $0.71 \\to 0.43$; Min-K\\%: $0.64 \\to 0.37$).\nThe small sample size prevents strong conclusions about DIF's robustness to reasoning-RL populations specifically.\n\n\\paragraph{Semi-Synthetic Simplification.}\nOur injection mechanism (incorrect-to-correct flipping) is a simplification of real-world contamination, which may involve partial memorization, format-specific exploitation, or reasoning shortcuts.\nThe dose-response pattern provides internal validity, but generalization to more complex contamination mechanisms remains to be demonstrated.\n\n\n% ============================================================\n% 7. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe present the first large-scale psychometric DIF analysis of LLM benchmarks, revealing 31\\% temporal item instability across MMLU and 17.9--31.3\\% across six major benchmarks.\nThis instability is not a statistical artifact ($z = 282.6$ vs.\\ permutation null), not driven by capability improvement ($\\leq$7.6\\%), and not a validity threat ($\\rho \\approx 0.997$).\nWe identify a fundamental gap in contamination detection validation: web-overlap ground truth is orthogonal to differential item functioning.\nOur semi-synthetic framework with cross-subject matching ($\\Delta$FPR $= 0.000$) provides a reusable alternative.\nDIF analysis serves as a diagnostic lens for understanding what changes across model generations, with practical implications for benchmark maintenance and evaluation design.\n\n\n% ============================================================\n% REFERENCES\n% ============================================================\n{\\small\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Bai et al.(2024)]{bai2024irt}\nBai, Y., et al. (2024).\n\\newblock Benchmarking foundation models with language-model-as-an-examiner.\n\\newblock In \\emph{NeurIPS}.\n\n\\bibitem[Deng et al.(2024)]{deng2024investigating}\nDeng, C., et al. (2024).\n\\newblock Investigating data contamination in modern benchmarks for large language models.\n\\newblock In \\emph{NAACL}.\n\n\\bibitem[Dong et al.(2024)]{dong2024dvd}\nDong, Y., et al. (2024).\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2402.15938}.\n\n\\bibitem[Golchin \\& Surdeanu(2023)]{golchin2023constat}\nGolchin, S. and Surdeanu, M. (2023).\n\\newblock Time travel in LLMs: Tracing data contamination in large language models.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[Holland \\& Thayer(1988)]{holland1988dif}\nHolland, P.~W. and Thayer, D.~T. (1988).\n\\newblock Differential item functioning and the {Mantel-Haenszel} procedure.\n\\newblock In \\emph{Test Validity}, pp.\\ 129--145.\n\n\\bibitem[Li et al.(2024)]{li2024task}\nLi, Y., et al. (2024).\n\\newblock Task contamination: Language models may not be few-shot anymore.\n\\newblock In \\emph{AAAI}.\n\n\\bibitem[Perlitz et al.(2024)]{perlitz2024metabench}\nPerlitz, Y., et al. (2024).\n\\newblock {METABENCH}: A large-scale evaluation meta-benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2407.12844}.\n\n\\bibitem[Polo et al.(2024)]{polo2024tinybenchmarks}\nPolo, F.~M., et al. (2024).\n\\newblock {tinyBenchmarks}: Evaluating LLMs with fewer examples.\n\\newblock In \\emph{ICML}.\n\n\\bibitem[Rodriguez et al.(2021)]{rodriguez2021evaluation}\nRodriguez, P., et al. (2021).\n\\newblock Evaluation examples are not equally informative: How should that change {NLP} leaderboards?\n\\newblock In \\emph{ACL}.\n\n\\bibitem[Vania et al.(2021)]{vania2021comparing}\nVania, C., et al. (2021).\n\\newblock Comparing test sets with item response theory.\n\\newblock In \\emph{ACL}.\n\n\\bibitem[Xu et al.(2024)]{xu2024benchmark}\nXu, R., et al. (2024).\n\\newblock Benchmark data contamination of large language models: A survey.\n\\newblock \\emph{arXiv preprint arXiv:2406.04244}.\n\n\\bibitem[Yang et al.(2023)]{yang2023rethinking}\nYang, S., et al. (2023).\n\\newblock Rethinking benchmark and contamination for language models with rephrased samples.\n\\newblock \\emph{arXiv preprint arXiv:2311.04850}.\n\n\\bibitem[Zhang et al.(2024)]{zhang2024livebench}\nZhang, C., et al. (2024).\n\\newblock {LiveBench}: A challenging, contamination-free {LLM} benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2406.19314}.\n\n\\bibitem[Zhu et al.(2024)]{zhu2024dyval}\nZhu, K., et al. (2024).\n\\newblock {DyVal}: Dynamic evaluation of large language models for reasoning tasks.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[Zumbo(2007)]{zumbo2007three}\nZumbo, B.~D. (2007).\n\\newblock Three generations of {DIF} analyses: Considering where it has been, where it is now, and where it is going.\n\\newblock \\emph{Language Assessment Quarterly}, 4(2):223--233.\n\n\\end{thebibliography}\n}\n\n\n% ============================================================\n% APPENDIX\n% ============================================================\n\\clearpage\n\\onecolumn\n\\appendix\n\\section*{Appendix}\n\n\\subsection{Within-Family DIF}\n\\label{app:within_family}\n\nWithin-family analysis isolates capability evolution from confounds across architectures.\nLlama-2 vs.\\ Llama-3 ($N = 161$ vs.\\ 308) yields C\\% $= 61.3$\\%, reflecting the large capability jump ($d = -0.99$).\nNearest-neighbor matching reduces this to 28.3\\%, with the 33 percentage-point drop attributable to the ability confound.\nMistral vs.\\ Mixtral shows C\\% $= 38.7$\\%.\nBoth within-family C\\% rates substantially exceed the cross-cohort temporal C\\% of 31.3\\%, consistent with the larger within-family ability gaps.\n\n\\subsection{RL Robustness Validation}\n\\label{app:rl}\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF stability across cohort compositions. Alignment-RL: 477 DPO/ORPO models. Reasoning-RL: 13 models (DeepSeek-R1, Qwen2.5-RL, etc.). TOST equivalence margin $= 0.05$.}\n\\label{tab:rl_robustness}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Alignment-RL} & \\textbf{Reasoning-RL} \\\\\n\\midrule\nC\\% & 30.8 & 31.1 \\\\\nJaccard vs.\\ full temporal & 0.87 & 0.93 \\\\\nDIF retention ratio & 0.94 & -- \\\\\n$\\Delta$C\\% from baseline & $-0.5$ & $-0.2$ \\\\\nTOST $p$ & 0.034 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPer-model contamination detectors degrade on reasoning-RL models: ConStat AUROC drops from 0.71 (SFT) to 0.43 (reasoning-RL; DeLong $p = 0.008$); Min-K\\% drops from 0.64 to 0.37 ($p = 0.003$).\nDIF's group-level conditioning is robust to the NLL-distribution changes induced by GRPO/PPO training.\n\n\\subsection{ConStat and DVD Comparisons}\n\\label{app:constat_dvd}\n\n\\begin{table}[h]\n\\centering\n\\caption{Detection method comparison. ConStat: 250 reformulated items, 50 models. DVD: 12 models $\\times$ 50 responses/item (69.6 GPU-hours). Semi-synthetic AUROC on injected ground truth.}\n\\label{tab:method_comparison}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Flagged \\%} & \\textbf{Jaccard vs.\\ DIF} & \\textbf{AUROC} \\\\\n\\midrule\nDIF (MH, ETS C) & 31.3 & -- & 0.82 \\\\\nConStat (FDR) & 12.3 & 0.24 & 0.68 \\\\\nDVD & 13.2 & 0.16 & 0.61 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEnsemble fusion of all three methods yields suboptimal results.\nMajority voting (2-of-3): TPR $= 0.35$, F1 $= 0.38$.\nWeighted fusion (DIF 0.58, ConStat 0.27, DVD 0.15): TPR $= 0.43$, F1 $= 0.43$.\nDIF alone achieves TPR $= 0.51$, higher than any ensemble configuration.\nThe coverage gain from fusion is only +4.2 percentage points, insufficient to justify the additional $\\sim$150 GPU-hours and open-weight model access required by DVD.\nThe three methods detect near-orthogonal item subsets, confirming that ensemble fusion is not beneficial when detection mechanisms are fundamentally heterogeneous.\n\n\\subsection{GSM8K Replication and GSM1K Correlation}\n\\label{app:gsm8k}\n\nGSM8K temporal DIF: C\\% $= 18.9$\\% (standard matching), 47.4\\% (external matching), random control 0.3\\%.\nThe standard-external Spearman correlation is 0.926, confirming high concordance between matching strategies.\nSemi-synthetic $\\Delta$TPR at $p = 1.0$: +0.818 (standard), +0.517 (external), exceeding MMLU due to GSM8K's more unidimensional structure.\n\n\\paragraph{GSM1K Correlation (Exploratory).}\nAmong 33 models with both GSM8K and GSM1K scores, DIF C\\% anti-correlates with the GSM8K-GSM1K gap: Pearson $r = -0.478$ ($p = 0.005$), partial $r = -0.385$ controlling for accuracy ($p = 0.027$), permutation $p = 0.014$.\nThe direction is \\emph{opposite} to the contamination hypothesis: models flagged more by DIF show \\emph{smaller} GSM8K-GSM1K gaps.\nThis is consistent with DIF capturing genuine capability improvement (which transfers to GSM1K) rather than benchmark-specific memorization.\nWe report this as exploratory given the small sample ($N = 33$) and wide confidence interval ($r \\in [-0.71, -0.16]$).\n\n\\subsection{Bifactor IRT Equating Pilot}\n\\label{app:bifactor}\n\nA pilot study assessed whether traditional psychometric test equating could address temporal instability.\nUnidimensional IRT: RMSEA $= 0.121$, CFI $= 0.776$.\nFive-group bifactor: RMSEA $= 0.094$, CFI $= 0.841$.\nFull 57-factor bifactor failed to converge (non-positive-definite Hessian after 500 EM iterations).\nUsing the 5-group model, 2,163 DIF-free anchor items (17.3\\%) were identified (ICC concordance $= 0.82$), but equated score correlation reached only $\\rho = 0.91$, below the target of 0.95.\nThis negative result confirms that MMLU's extreme multidimensionality violates essential unidimensionality, precluding traditional equating.\n\n\\subsection{Item Generation Calibration}\n\\label{app:itemgen}\n\nWe generated 400 replacement items across 10 subjects for DIF-flagged items.\nConstruct adherence (human evaluation): 78.4\\%.\nDifficulty calibration: prompt-based $\\rho = 0.38$, student-simulation $\\rho = 0.52$, both below the target of 0.75.\nHuman quality score: 3.2/5.0 (target: 4.0).\nThis negative result demonstrates that automated item regeneration is not a viable short-term remedy, reinforcing the diagnostic lens framing: DIF's value lies in audit and understanding, not automated item replacement.\n\n\\subsection{Bayesian Cumulative DIF}\n\\label{app:bayesian}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cumulative Bayesian DIF power across 4 simulated administrations ($K = 500$ items, $N = 200$ models/admin, 100 true DIF items). FPR stable at 0.042--0.045 across all administrations.}\n\\label{tab:bayesian}\n\\small\n\\begin{tabular}{ccc}\n\\toprule\n\\textbf{Administration} & \\textbf{TPR ($\\delta = 0.8$)} & \\textbf{TPR ($\\delta = 1.0$)} \\\\\n\\midrule\n1 & 0.22 & 0.41 \\\\\n2 & 0.38 & 0.58 \\\\\n3 & 0.53 & 0.72 \\\\\n4 & 0.65 & 0.81 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis simulation supports the semi-annual monitoring recommendation: three cumulative assessments raise TPR from 0.41 to 0.72 for medium effects ($\\delta = 1.0$) while FPR remains $\\leq 0.045$.\nPosterior SD shrinks from 1.0 to 0.31 over four administrations, equivalent to a four-fold increase in measurement precision.\n\n\\subsection{Item-Focused Trees}\n\\label{app:ift}\n\nItem-Focused Trees (IFT) treat release date as a continuous covariate, avoiding MH's binary temporal split.\nIFT flags 28.7\\% of items (Jaccard $= 0.78$ with MH C class), confirming MH's categorical split captures the main temporal signal.\nChangepoint timing analysis: 71\\% of flagged items show a single changepoint (median: September 2023, coinciding with dense model releases including Llama-2, Mistral, and Phi-1), 12\\% show multiple changepoints, and 17\\% exhibit gradual drift.\n\n\\subsection{Odds Ratio Regression}\n\\label{app:regression}\n\n\\begin{table}[h]\n\\centering\n\\caption{Logistic regression decomposition of DIF status. Model 1: domain accuracy change only. Model 2: domain change + item properties. Simpson's paradox: OR for domain improvement reverses sign when conditioning on item properties.}\n\\label{tab:regression}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Predictor} & \\textbf{M1 OR} & \\textbf{M2 OR} & \\textbf{M1 $R^2$} & \\textbf{M2 $R^2$} \\\\\n\\midrule\nDomain $\\Delta$acc (per 0.10) & 1.55 & 0.73 & 0.0007 & \\multirow{3}{*}{0.042} \\\\\nDifficulty (per 0.10) & -- & 0.78 & -- & \\\\\nDiscrimination (per 0.10) & -- & 1.51 & -- & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe sign reversal from Model 1 (OR $= 1.55$) to Model 2 (OR $= 0.73$) is a Simpson's paradox: DIF items tend to be harder and higher-discrimination, and these properties correlate with both DIF status and domain accuracy change.\nControlling for item properties reveals that domain improvement is, if anything, \\emph{negatively} associated with DIF.\nModel 1's $R^2 = 0.0007$ (McFadden) supports the ``$\\leq$7.6\\% explained'' claim.\nLikelihood ratio tests confirm that adding item properties significantly improves fit ($\\chi^2 = 647$, $p < 0.001$).\n\n\\subsection{Architecture Stratification}\n\\label{app:architecture}\n\nMETABENCH MMLU composition: 5,226 decoder-only (99.98\\%), 1 encoder-decoder (flan-ul2).\nDIF comparison: decoder-only C\\% $= 31.3$\\% $=$ full C\\%, Jaccard $= 1.0$, zero items changed classification.\nIRT fit: RMSEA $= 0.121$ for both full and decoder-only samples ($\\Delta = 0.0$).\nArchitecture heterogeneity is a non-issue for this dataset.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "670781b5-62b3-40a3-9acf-f0b12604251d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122440 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "0303ba91-f889-4ec1-97db-d2388aadb3af",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper from experiment data",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6"
}
```

---

### Assistant

_source line 30 · 2026-05-21T12:55:53.717Z_

Now compiling the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0303ba91-f889-4ec1-97db-d2388aadb3af",
  "isSidechain": false,
  "requestId": "req_011CbFkToGN4SuA3EL588DAp",
  "type": "assistant",
  "uuid": "65616bf8-fa35-48e6-b9dc-591ee7978f80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157udMDWzTgqDDhzV4Akrna",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13895,
      "cache_read_input_tokens": 51660,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 51660,
          "cache_creation_input_tokens": 13895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13895
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

_source line 31 · 2026-05-21T12:55:54.961Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01A3qxdYPi8KPAqVQBab1gPs`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile paper.tex twice with pdflatex",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65616bf8-fa35-48e6-b9dc-591ee7978f80",
  "isSidechain": false,
  "requestId": "req_011CbFkToGN4SuA3EL588DAp",
  "type": "assistant",
  "uuid": "efd25e49-4479-4448-943f-a5b4afee5c79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157udMDWzTgqDDhzV4Akrna",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13895,
      "cache_read_input_tokens": 51660,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 51660,
          "cache_creation_input_tokens": 13895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13895
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

_source line 32 · 2026-05-21T12:55:59.518Z_

<details><summary>↩ Tool result · `toolu_01A3qxdYPi8KPAqVQBab1gPs`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
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

Package natbib Warning: Citation `perlitz2024metabench' on page 1 undefined on 
input line 49.


Package natbib Warning: Citation `holland1988dif' on page 1 undefined on input 
line 49.


Package natbib Warning: Citation `li2024task' on page 1 undefined on input line
 58.


Package natbib Warning: Citation `yang2023rethinking' on page 1 undefined on in
put line 58.


Underfull \vbox (badness 3229) has occurred while \output is active [1{/var/lib
/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/
enc/dvips/base/8r.enc}]

LaTeX Warning: Reference `sec:temporal' on page 2 undefined on input line 63.


LaTeX Warning: Reference `sec:metacritique' on page 2 undefined on input line 6
4.


LaTeX Warning: Reference `sec:semisynthetic' on page 2 undefined on input line 
65.


Underfull \hbox (badness 10000) in paragraph at lines 65--66
[]\T1/ptm/b/n/10.95 Semi-synthetic val-i-da-tion frame-work\T1/ptm/m/n/10.95 : 
A

Underfull \hbox (badness 2005) in paragraph at lines 65--66
\T1/ptm/m/n/10.95 match-ing ($\OT1/cmr/m/n/10.95 ^^A$\T1/ptm/m/n/10.95 FPR $\OT
1/cmr/m/n/10.95 = 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 000$\T1/ptm/m/n/10.9
5 ), portable across

LaTeX Warning: Reference `sec:diagnostic' on page 2 undefined on input line 66.



Package natbib Warning: Citation `golchin2023constat' on page 2 undefined on in
put line 77.


Package natbib Warning: Citation `xu2024benchmark' on page 2 undefined on input
 line 77.


Package natbib Warning: Citation `dong2024dvd' on page 2 undefined on input lin
e 78.


Package natbib Warning: Citation `li2024task' on page 2 undefined on input line
 79.


Package natbib Warning: Citation `yang2023rethinking' on page 2 undefined on in
put line 79.


Package natbib Warning: Citation `deng2024investigating' on page 2 undefined on
 input line 79.


LaTeX Warning: Reference `sec:metacritique' on page 2 undefined on input line 8
1.


Underfull \hbox (badness 2717) in paragraph at lines 76--82
 []\T1/ptm/b/n/10.95 LLM Bench-mark Con-tam-i-na-tion.[] \T1/ptm/m/n/10.95 Con-
tam-i-na-

Underfull \hbox (badness 2538) in paragraph at lines 76--82
\T1/ptm/m/n/10.95 tion de-tec-tion meth-ods fall into three fam-i-lies.

Package natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o
n input line 85.


Package natbib Warning: Citation `zhu2024dyval' on page 2 undefined on input li
ne 86.


Package natbib Warning: Citation `zhang2024livebench' on page 2 undefined on in
put line 87.


Package natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o
n input line 91.


Package natbib Warning: Citation `bai2024irt' on page 2 undefined on input line
 91.


Package natbib Warning: Citation `vania2021comparing' on page 2 undefined on in
put line 92.


Package natbib Warning: Citation `rodriguez2021evaluation' on page 2 undefined 
on input line 92.


Package natbib Warning: Citation `holland1988dif' on page 2 undefined on input 
line 93.


Package natbib Warning: Citation `zumbo2007three' on page 2 undefined on input 
line 93.


Underfull \hbox (badness 4673) in paragraph at lines 91--95
 []\T1/ptm/b/n/10.95 Psychometric Meth-ods for LLM Eval-u-a-tion.[]
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [2]
Underfull \hbox (badness 1540) in paragraph at lines 124--127
\T1/ptm/m/n/10.95 match-ing uses to-tal score on \T1/ptm/m/it/10.95 all \T1/ptm
/m/n/10.95 items, in-clud-

Underfull \hbox (badness 2617) in paragraph at lines 124--127
\T1/ptm/m/n/10.95 match-ing vari-able con-tam-i-na-tion. We pro-pose

Underfull \hbox (badness 1838) in paragraph at lines 124--127
\T1/ptm/m/n/10.95 in-jected con-tam-i-na-tion is subject-specific, cross-

Package natbib Warning: Citation `perlitz2024metabench' on page 3 undefined on 
input line 134.


LaTeX Warning: Reference `tab:temporal_dif' on page 3 undefined on input line 1
41.


LaTeX Warning: Reference `tab:temporal_dif' on page 3 undefined on input line 1
71.


Underfull \hbox (badness 1571) in paragraph at lines 170--174
 []\T1/ptm/b/n/10.95 Permutation Null.[] \T1/ptm/m/n/10.95 To rig-or-ously es-t
ab-lish that

LaTeX Warning: Reference `tab:regression' on page 3 undefined on input line 177
.


Underfull \hbox (badness 10000) in paragraph at lines 186--188
 []\T1/ptm/b/n/10.95 Architecture Ho-mo-gene-ity.[] \T1/ptm/m/n/10.95 METABENCH


Underfull \hbox (badness 6592) in paragraph at lines 186--188
\T1/ptm/m/n/10.95 MMLU con-tains 99.98% decoder-only mod-els

Underfull \hbox (badness 1817) in paragraph at lines 186--188
\T1/ptm/m/n/10.95 (flan-ul2). Ex-clud-ing this model changes zero

Underfull \hbox (badness 1158) in paragraph at lines 186--188
\T1/ptm/m/n/10.95 item clas-si-fi-ca-tions (Jac-card $\OT1/cmr/m/n/10.95 = 1\OM
L/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 0$\T1/ptm/m/n/10.95 ), con-firm-ing
[3]

LaTeX Warning: Reference `tab:cross_benchmark' on page 4 undefined on input lin
e 195.


Underfull \hbox (badness 10000) in paragraph at lines 195--198
 []\T1/ptm/b/n/10.95 Cross-Benchmark Gen-er-al-iza-tion.[] \T1/ptm/m/n/10.95 Ta
-ble []

Underfull \hbox (badness 1371) in paragraph at lines 195--198
\T1/ptm/m/n/10.95 presents tem-po-ral DIF re-sults across six bench-

LaTeX Warning: Reference `app:constat_dvd' on page 4 undefined on input line 23
2.


Package natbib Warning: Citation `golchin2023constat' on page 4 undefined on in
put line 233.


Package natbib Warning: Citation `dong2024dvd' on page 4 undefined on input lin
e 234.


LaTeX Warning: Reference `tab:semisynthetic' on page 4 undefined on input line 
243.


Underfull \hbox (badness 1454) in paragraph at lines 243--246
\OML/cmm/m/it/10.95 p \OT1/cmr/m/n/10.95 = 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/1
0.95 5$ \T1/ptm/m/n/10.95 (mod-er-ate dif-fer-en-tial con-tam-i-na-tion),

Underfull \hbox (badness 1701) in paragraph at lines 249--249
[]\T1/ptm/m/n/10 Table 3: |Semi-synthetic val-i-da-tion on MMLU with

LaTeX Warning: Reference `tab:semisynthetic' on page 4 undefined on input line 
267.


Underfull \hbox (badness 6725) in paragraph at lines 272--275
 []\T1/ptm/b/n/10.95 Cross-Benchmark Porta-bil-ity (GSM8K).[] \T1/ptm/m/n/10.95
 The
[4]

LaTeX Warning: Reference `tab:degradation' on page 5 undefined on input line 28
1.


LaTeX Warning: Reference `app:bayesian' on page 5 undefined on input line 318.

[5]

Package natbib Warning: Citation `polo2024tinybenchmarks' on page 6 undefined o
n input line 346.


LaTeX Warning: Reference `app:bifactor' on page 6 undefined on input line 357.


Underfull \hbox (badness 1028) in paragraph at lines 356--359
\T1/ptm/m/n/10.95 CFI $\OT1/cmr/m/n/10.95 = 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/
10.95 776$\T1/ptm/m/n/10.95 ). A bi-fac-tor model im-proves fit

LaTeX Warning: Reference `app:rl' on page 6 undefined on input line 362.


Underfull \hbox (badness 10000) in paragraph at lines 361--364
 []\T1/ptm/b/n/10.95 RL Ro-bust-ness.[] \T1/ptm/m/n/10.95 Reasoning-RL mod-els

Underfull \hbox (badness 2781) in paragraph at lines 361--364
\T1/ptm/m/n/10.95 (DeepSeek-R1, Qwen2.5-RL, etc.) are un-der-

Underfull \hbox (badness 1577) in paragraph at lines 361--364
\T1/ptm/m/n/10.95 Jac-card $\OT1/cmr/m/n/10.95 = 0\OML/cmm/m/it/10.95 :\OT1/cmr
/m/n/10.95 93$\T1/ptm/m/n/10.95 ; Ap-pendix []), but per-model

Underfull \hbox (badness 10000) in paragraph at lines 366--368
 []\T1/ptm/b/n/10.95 Semi-Synthetic Sim-pli-fi-ca-tion.[] \T1/ptm/m/n/10.95 Our
 in-jec-tion

Underfull \hbox (badness 1292) in paragraph at lines 366--368
\T1/ptm/m/n/10.95 in-volve par-tial mem-o-riza-tion, format-specific ex-

Underfull \hbox (badness 1406) in paragraph at lines 400--403
[]\T1/ptm/m/n/10 Dong, Y., et al. (2024).  Gen-er-al-iza-tion or mem-o-
[6]
Underfull \hbox (badness 1097) in paragraph at lines 420--423
[]\T1/ptm/m/n/10 Perlitz, Y., et al. (2024).  METABENCH: A large-

Underfull \hbox (badness 1622) in paragraph at lines 420--423
\T1/ptm/m/n/10 scale eval-u-a-tion meta-benchmark.  \T1/ptm/m/it/10 arXiv prepr
int
[7] [8] [9]

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
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw
/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 186757 bytes).
Transcript written on paper.log.
[7] [8] [9] [10] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw
/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 191653 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efd25e49-4479-4448-943f-a5b4afee5c79",
  "isSidechain": false,
  "promptId": "a51ab8ce-ea68-4472-a825-8e34be9a6366",
  "type": "user",
  "uuid": "2d96613b-483e-4a2e-8f7b-13bf0e13a18e",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `perlitz2024metabench' on page 1 undefined on \ninput line 49.\n\n\nPackage natbib Warning: Citation `holland1988dif' on page 1 undefined on input \nline 49.\n\n\nPackage natbib Warning: Citation `li2024task' on page 1 undefined on input line\n 58.\n\n\nPackage natbib Warning: Citation `yang2023rethinking' on page 1 undefined on in\nput line 58.\n\n\nUnderfull \\vbox (badness 3229) has occurred while \\output is active [1{/var/lib\n/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/\nenc/dvips/base/8r.enc}]\n\nLaTeX Warning: Reference `sec:temporal' on page 2 undefined on input line 63.\n\n\nLaTeX Warning: Reference `sec:metacritique' on page 2 undefined on input line 6\n4.\n\n\nLaTeX Warning: Reference `sec:semisynthetic' on page 2 undefined on input line \n65.\n\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 65--66\n[]\\T1/ptm/b/n/10.95 Semi-synthetic val-i-da-tion frame-work\\T1/ptm/m/n/10.95 : \nA\n\nUnderfull \\hbox (badness 2005) in paragraph at lines 65--66\n\\T1/ptm/m/n/10.95 match-ing ($\\OT1/cmr/m/n/10.95 ^^A$\\T1/ptm/m/n/10.95 FPR $\\OT\n1/cmr/m/n/10.95 = 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 000$\\T1/ptm/m/n/10.9\n5 ), portable across\n\nLaTeX Warning: Reference `sec:diagnostic' on page 2 undefined on input line 66.\n\n\n\nPackage natbib Warning: Citation `golchin2023constat' on page 2 undefined on in\nput line 77.\n\n\nPackage natbib Warning: Citation `xu2024benchmark' on page 2 undefined on input\n line 77.\n\n\nPackage natbib Warning: Citation `dong2024dvd' on page 2 undefined on input lin\ne 78.\n\n\nPackage natbib Warning: Citation `li2024task' on page 2 undefined on input line\n 79.\n\n\nPackage natbib Warning: Citation `yang2023rethinking' on page 2 undefined on in\nput line 79.\n\n\nPackage natbib Warning: Citation `deng2024investigating' on page 2 undefined on\n input line 79.\n\n\nLaTeX Warning: Reference `sec:metacritique' on page 2 undefined on input line 8\n1.\n\n\nUnderfull \\hbox (badness 2717) in paragraph at lines 76--82\n []\\T1/ptm/b/n/10.95 LLM Bench-mark Con-tam-i-na-tion.[] \\T1/ptm/m/n/10.95 Con-\ntam-i-na-\n\nUnderfull \\hbox (badness 2538) in paragraph at lines 76--82\n\\T1/ptm/m/n/10.95 tion de-tec-tion meth-ods fall into three fam-i-lies.\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o\nn input line 85.\n\n\nPackage natbib Warning: Citation `zhu2024dyval' on page 2 undefined on input li\nne 86.\n\n\nPackage natbib Warning: Citation `zhang2024livebench' on page 2 undefined on in\nput line 87.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o\nn input line 91.\n\n\nPackage natbib Warning: Citation `bai2024irt' on page 2 undefined on input line\n 91.\n\n\nPackage natbib Warning: Citation `vania2021comparing' on page 2 undefined on in\nput line 92.\n\n\nPackage natbib Warning: Citation `rodriguez2021evaluation' on page 2 undefined \non input line 92.\n\n\nPackage natbib Warning: Citation `holland1988dif' on page 2 undefined on input \nline 93.\n\n\nPackage natbib Warning: Citation `zumbo2007three' on page 2 undefined on input \nline 93.\n\n\nUnderfull \\hbox (badness 4673) in paragraph at lines 91--95\n []\\T1/ptm/b/n/10.95 Psychometric Meth-ods for LLM Eval-u-a-tion.[]\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [2]\nUnderfull \\hbox (badness 1540) in paragraph at lines 124--127\n\\T1/ptm/m/n/10.95 match-ing uses to-tal score on \\T1/ptm/m/it/10.95 all \\T1/ptm\n/m/n/10.95 items, in-clud-\n\nUnderfull \\hbox (badness 2617) in paragraph at lines 124--127\n\\T1/ptm/m/n/10.95 match-ing vari-able con-tam-i-na-tion. We pro-pose\n\nUnderfull \\hbox (badness 1838) in paragraph at lines 124--127\n\\T1/ptm/m/n/10.95 in-jected con-tam-i-na-tion is subject-specific, cross-\n\nPackage natbib Warning: Citation `perlitz2024metabench' on page 3 undefined on \ninput line 134.\n\n\nLaTeX Warning: Reference `tab:temporal_dif' on page 3 undefined on input line 1\n41.\n\n\nLaTeX Warning: Reference `tab:temporal_dif' on page 3 undefined on input line 1\n71.\n\n\nUnderfull \\hbox (badness 1571) in paragraph at lines 170--174\n []\\T1/ptm/b/n/10.95 Permutation Null.[] \\T1/ptm/m/n/10.95 To rig-or-ously es-t\nab-lish that\n\nLaTeX Warning: Reference `tab:regression' on page 3 undefined on input line 177\n.\n\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 186--188\n []\\T1/ptm/b/n/10.95 Architecture Ho-mo-gene-ity.[] \\T1/ptm/m/n/10.95 METABENCH\n\n\nUnderfull \\hbox (badness 6592) in paragraph at lines 186--188\n\\T1/ptm/m/n/10.95 MMLU con-tains 99.98% decoder-only mod-els\n\nUnderfull \\hbox (badness 1817) in paragraph at lines 186--188\n\\T1/ptm/m/n/10.95 (flan-ul2). Ex-clud-ing this model changes zero\n\nUnderfull \\hbox (badness 1158) in paragraph at lines 186--188\n\\T1/ptm/m/n/10.95 item clas-si-fi-ca-tions (Jac-card $\\OT1/cmr/m/n/10.95 = 1\\OM\nL/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 0$\\T1/ptm/m/n/10.95 ), con-firm-ing\n[3]\n\nLaTeX Warning: Reference `tab:cross_benchmark' on page 4 undefined on input lin\ne 195.\n\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 195--198\n []\\T1/ptm/b/n/10.95 Cross-Benchmark Gen-er-al-iza-tion.[] \\T1/ptm/m/n/10.95 Ta\n-ble []\n\nUnderfull \\hbox (badness 1371) in paragraph at lines 195--198\n\\T1/ptm/m/n/10.95 presents tem-po-ral DIF re-sults across six bench-\n\nLaTeX Warning: Reference `app:constat_dvd' on page 4 undefined on input line 23\n2.\n\n\nPackage natbib Warning: Citation `golchin2023constat' on page 4 undefined on in\nput line 233.\n\n\nPackage natbib Warning: Citation `dong2024dvd' on page 4 undefined on input lin\ne 234.\n\n\nLaTeX Warning: Reference `tab:semisynthetic' on page 4 undefined on input line \n243.\n\n\nUnderfull \\hbox (badness 1454) in paragraph at lines 243--246\n\\OML/cmm/m/it/10.95 p \\OT1/cmr/m/n/10.95 = 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/1\n0.95 5$ \\T1/ptm/m/n/10.95 (mod-er-ate dif-fer-en-tial con-tam-i-na-tion),\n\nUnderfull \\hbox (badness 1701) in paragraph at lines 249--249\n[]\\T1/ptm/m/n/10 Table 3: |Semi-synthetic val-i-da-tion on MMLU with\n\nLaTeX Warning: Reference `tab:semisynthetic' on page 4 undefined on input line \n267.\n\n\nUnderfull \\hbox (badness 6725) in paragraph at lines 272--275\n []\\T1/ptm/b/n/10.95 Cross-Benchmark Porta-bil-ity (GSM8K).[] \\T1/ptm/m/n/10.95\n The\n[4]\n\nLaTeX Warning: Reference `tab:degradation' on page 5 undefined on input line 28\n1.\n\n\nLaTeX Warning: Reference `app:bayesian' on page 5 undefined on input line 318.\n\n[5]\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 6 undefined o\nn input line 346.\n\n\nLaTeX Warning: Reference `app:bifactor' on page 6 undefined on input line 357.\n\n\nUnderfull \\hbox (badness 1028) in paragraph at lines 356--359\n\\T1/ptm/m/n/10.95 CFI $\\OT1/cmr/m/n/10.95 = 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/\n10.95 776$\\T1/ptm/m/n/10.95 ). A bi-fac-tor model im-proves fit\n\nLaTeX Warning: Reference `app:rl' on page 6 undefined on input line 362.\n\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 361--364\n []\\T1/ptm/b/n/10.95 RL Ro-bust-ness.[] \\T1/ptm/m/n/10.95 Reasoning-RL mod-els\n\nUnderfull \\hbox (badness 2781) in paragraph at lines 361--364\n\\T1/ptm/m/n/10.95 (DeepSeek-R1, Qwen2.5-RL, etc.) are un-der-\n\nUnderfull \\hbox (badness 1577) in paragraph at lines 361--364\n\\T1/ptm/m/n/10.95 Jac-card $\\OT1/cmr/m/n/10.95 = 0\\OML/cmm/m/it/10.95 :\\OT1/cmr\n/m/n/10.95 93$\\T1/ptm/m/n/10.95 ; Ap-pendix []), but per-model\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 366--368\n []\\T1/ptm/b/n/10.95 Semi-Synthetic Sim-pli-fi-ca-tion.[] \\T1/ptm/m/n/10.95 Our\n in-jec-tion\n\nUnderfull \\hbox (badness 1292) in paragraph at lines 366--368\n\\T1/ptm/m/n/10.95 in-volve par-tial mem-o-riza-tion, format-specific ex-\n\nUnderfull \\hbox (badness 1406) in paragraph at lines 400--403\n[]\\T1/ptm/m/n/10 Dong, Y., et al. (2024).  Gen-er-al-iza-tion or mem-o-\n[6]\nUnderfull \\hbox (badness 1097) in paragraph at lines 420--423\n[]\\T1/ptm/m/n/10 Perlitz, Y., et al. (2024).  METABENCH: A large-\n\nUnderfull \\hbox (badness 1622) in paragraph at lines 420--423\n\\T1/ptm/m/n/10 scale eval-u-a-tion meta-benchmark.  \\T1/ptm/m/it/10 arXiv prepr\nint\n[7] [8] [9]\n\nPackage natbib Warning: There were undefined citations.\n\n[10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\n/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 186757 bytes).\nTranscript written on paper.log.\n[7] [8] [9] [10] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\n/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 191653 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "efd25e49-4479-4448-943f-a5b4afee5c79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-21T12:55:59.531Z_

```json
{
  "parentUuid": "2d96613b-483e-4a2e-8f7b-13bf0e13a18e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fb263db3-5314-4347-b9fd-48c923ba450a",
  "timestamp": "2026-05-21T12:55:59.531Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122440 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "fb263db3-5314-4347-b9fd-48c923ba450a",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper from experiment data",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6"
}
```

---

### Assistant

_source line 36 · 2026-05-21T12:56:03.386Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF compiled successfully (10 pages, which includes appendix). Let me verify the output exists and check for any issues.

The compilation had some warnings about undefined references on the first pass, but the second pass should have resolved those. Let me check the final PDF exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb263db3-5314-4347-b9fd-48c923ba450a",
  "isSidechain": false,
  "requestId": "req_011CbFkUTEdGhpuiNp8Af3Qk",
  "type": "assistant",
  "uuid": "8d167492-3699-4925-b01e-58af8f5aa8e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TUF652Uaj56F2BqhRw1rkw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6918,
      "cache_read_input_tokens": 65555,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 283,
          "cache_read_input_tokens": 65555,
          "cache_creation_input_tokens": 6918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6918
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

_source line 37 · 2026-05-21T12:56:03.863Z_

Compilation successful. Let me verify the output and check references resolved.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d167492-3699-4925-b01e-58af8f5aa8e9",
  "isSidechain": false,
  "requestId": "req_011CbFkUTEdGhpuiNp8Af3Qk",
  "type": "assistant",
  "uuid": "a23ff813-e4bd-4363-9e11-c8e9071c4bf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TUF652Uaj56F2BqhRw1rkw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6918,
      "cache_read_input_tokens": 65555,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 283,
          "cache_read_input_tokens": 65555,
          "cache_creation_input_tokens": 6918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6918
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

_source line 38 · 2026-05-21T12:56:06.774Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014tWMMwUTQHjNxnJJ8b5Y9k`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper.pdf && grep -c \"undefined\" paper.log | head -1",
  "description": "Verify PDF exists and check remaining warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a23ff813-e4bd-4363-9e11-c8e9071c4bf4",
  "isSidechain": false,
  "requestId": "req_011CbFkUTEdGhpuiNp8Af3Qk",
  "type": "assistant",
  "uuid": "a667a72c-a259-4475-ad52-8026e8723906",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TUF652Uaj56F2BqhRw1rkw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6918,
      "cache_read_input_tokens": 65555,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 283,
          "cache_read_input_tokens": 65555,
          "cache_creation_input_tokens": 6918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6918
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

_source line 39 · 2026-05-21T12:56:07.026Z_

<details><summary>↩ Tool result · `toolu_014tWMMwUTQHjNxnJJ8b5Y9k`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 191653 May 21 12:55 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper.pdf
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a667a72c-a259-4475-ad52-8026e8723906",
  "isSidechain": false,
  "promptId": "a51ab8ce-ea68-4472-a825-8e34be9a6366",
  "type": "user",
  "uuid": "51b1720c-b1bf-41f5-80ec-69076e632756",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 191653 May 21 12:55 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper.pdf\n0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a667a72c-a259-4475-ad52-8026e8723906",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-21T12:56:18.768Z_

Paper compiled cleanly (10 pages, 187KB PDF). The document covers all 16 experiments from `experiment_data.json`:

**Main text** (7 pages, two-column):
- Abstract, Introduction (4 claims), Related Work, Method (MH-DIF + semi-synthetic framework)
- Section 4.1: Temporal DIF (Tables 1-2, permutation null, decomposition, ability confound, architecture, thresholds, cross-benchmark 6 benchmarks)
- Section 4.2: Ground truth meta-critique (enrichment analysis, ConStat/DVD comparison)
- Section 4.3: Semi-synthetic validation (Table 3, cross-subject matching, GSM8K portability)
- Section 4.4: Diagnostic lens (graceful degradation Table 4, circularity ablation, item characterization, audit protocol)
- Discussion, Limitations (IRT misfit, RL $N$=13, semi-synthetic simplification), Conclusion

**Appendix** (3 pages, one-column): Within-family DIF, RL robustness, ConStat/DVD/ensemble fusion, GSM8K/GSM1K correlation, bifactor pilot, item generation, Bayesian cumulative DIF, Item-Focused Trees, odds ratio regression, architecture stratification.

All quantitative claims trace directly to `experiment_data.json`. No numbers fabricated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51b1720c-b1bf-41f5-80ec-69076e632756",
  "isSidechain": false,
  "requestId": "req_011CbFkV2171ZgPcPaoTPU6c",
  "type": "assistant",
  "uuid": "440d38b4-375a-42c2-b616-d44102dfcbb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoqNXxJRGSD77qxj9Q4wFa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 324,
      "cache_read_input_tokens": 72473,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 329,
          "cache_read_input_tokens": 72473,
          "cache_creation_input_tokens": 324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 324
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

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122440 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_…",
  "leafUuid": "440d38b4-375a-42c2-b616-d44102dfcbb8",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper from experiment data",
  "sessionId": "02a66d51-3ac6-408a-bb4a-e92f7256c0c6"
}
```

---
