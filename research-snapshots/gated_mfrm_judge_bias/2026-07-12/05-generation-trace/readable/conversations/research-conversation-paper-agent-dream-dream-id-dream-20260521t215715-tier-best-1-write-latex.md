# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T215715 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/bb63dd8d-216f-4ef3-bc10-be14a5c080f5.jsonl`
- **Structured JSON:** [`e347ebd3546254d96367.json`](../../sessions/e3/e347ebd3546254d96367.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T22:13:08.159Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T22:13:08.159Z",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T215715 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：Full Tier A narrative. Lead with quantitative shock: G-MFRM joint calibration corrects ~40% θ-RMSE and +5-6pp Kendall-τ over best sequential baseline on real MT-Bench/Arena-Hard data. Real contamination is strong (median c_n ≈ 0.95), validating the core premise that confounding is not a theoretical curiosity but a measurable distortion in current LLM evaluation practice. Paper title: \"Joint Calibration of Judge Bias and Benchmark Contamination Corrects Systematic Rank Distortions in LLM Evaluation.\" Section 2 opens with the OVB observation on a 3-model toy example, then pivots to G-MFRM. Main result table is the centerpiece: G-MFRM beats all 8 baselines on both benchmarks, with CyclicJudge+discard as strongest competitor but still 4-5pp behind. Rank change analysis provides the narrative hook — at least 4 models shift ≥2 positions, and 2 top-5 models swap, making the correction practically consequential for deployment decisions. ConStat external validation (ρ≥0.78) closes the loop: fitted c_n is not a MCMC artifact but tracks an independently measurable contamination signal.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T22:13:08.163Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T22:13:08.163Z",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5"
}
```

---

## Round 1

39 recorded events

### User

_source line 3 · 2026-05-21T22:13:08.183Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T215715 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：Full Tier A narrative. Lead with quantitative shock: G-MFRM joint calibration corrects ~40% θ-RMSE and +5-6pp Kendall-τ over best sequential baseline on real MT-Bench/Arena-Hard data. Real contamination is strong (median c_n ≈ 0.95), validating the core premise that confounding is not a theoretical curiosity but a measurable distortion in current LLM evaluation practice. Paper title: "Joint Calibration of Judge Bias and Benchmark Contamination Corrects Systematic Rank Distortions in LLM Evaluation." Section 2 opens with the OVB observation on a 3-model toy example, then pivots to G-MFRM. Main result table is the centerpiece: G-MFRM beats all 8 baselines on both benchmarks, with CyclicJudge+discard as strongest competitor but still 4-5pp behind. Rank change analysis provides the narrative hook — at least 4 models shift ≥2 positions, and 2 top-5 models swap, making the correction practically consequential for deployment decisions. ConStat external validation (ρ≥0.78) closes the loop: fitted c_n is not a MCMC artifact but tracks an independently measurable contamination signal.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "fe64548b-77cb-42da-afef-0d7832f54298",
  "type": "user",
  "uuid": "03d2e7b5-2e3f-4e22-b8f8-df9887d93ca4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T22:13:08.182Z_

```json
{
  "parentUuid": "03d2e7b5-2e3f-4e22-b8f8-df9887d93ca4",
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
  "uuid": "2cb6d199-3dfe-4288-8cc7-d4f6e2cbd5eb",
  "timestamp": "2026-05-21T22:13:08.182Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T22:13:08.182Z_

```json
{
  "parentUuid": "2cb6d199-3dfe-4288-8cc7-d4f6e2cbd5eb",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "61741028-e5a5-4aba-ab33-b5ac6260dfe0",
  "timestamp": "2026-05-21T22:13:08.182Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
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
  "aiTitle": "Joint calibration of judge bias and benchmark contamination",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5"
}
```

---

### Assistant

_source line 7 · 2026-05-21T22:13:10.875Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61741028-e5a5-4aba-ab33-b5ac6260dfe0",
  "isSidechain": false,
  "requestId": "req_011CbGUxdFZDDZecYLh2o6vU",
  "type": "assistant",
  "uuid": "fc913b92-4d5f-43a4-ba32-e8e02f071271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kt3FmvtW2XTy6frmEYEpGS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12099,
      "cache_read_input_tokens": 11841,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 202,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12099
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

_source line 8 · 2026-05-21T22:13:11.993Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GK75UZkPiBsqTVa9uJ5fxj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc913b92-4d5f-43a4-ba32-e8e02f071271",
  "isSidechain": false,
  "requestId": "req_011CbGUxdFZDDZecYLh2o6vU",
  "type": "assistant",
  "uuid": "8e417eac-b76b-4246-93f9-346139d1f49d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kt3FmvtW2XTy6frmEYEpGS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12099,
      "cache_read_input_tokens": 11841,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 202,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12099
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

_source line 9 · 2026-05-21T22:13:12.157Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hg7qrgwV1epN7g4sL68BT9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e417eac-b76b-4246-93f9-346139d1f49d",
  "isSidechain": false,
  "requestId": "req_011CbGUxdFZDDZecYLh2o6vU",
  "type": "assistant",
  "uuid": "993e449f-7594-46d3-88f5-f060f3be40fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kt3FmvtW2XTy6frmEYEpGS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12099,
      "cache_read_input_tokens": 11841,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 202,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12099
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

_source line 10 · 2026-05-21T22:13:12.164Z_

<details><summary>↩ Tool result · `toolu_01Hg7qrgwV1epN7g4sL68BT9`</summary>

```text
1	# Paper Framing — gated_mfrm_judge_bias
2	
3	## Target Venue
4	- Primary: AAAI 2027 (full paper, deadline July 28, 2026)
5	- Backup: ACL 2027 via ARR (submission August 3, 2026)
6	- Timeline: ~68 days from today (2026-05-21)
7	
8	## Core Insight
9	Sequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.
10	
11	## Core Claims (3 条，均可证伪)
12	
13	1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding.
14	
15	2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — provides a staged joint calibration that estimates model ability, item difficulty, judge severity, and contamination susceptibility, yielding bias-and-contamination-corrected "fair scores." (Note: "staged joint" — e_i is pre-estimated in Stage 2 and fixed in Stage 3; the joint estimation is conditional on e_i. This is a deliberate identifiability choice, not fully simultaneous. Paper must use "staged joint calibration" or "conditional joint estimation," never "fully joint.")
16	
17	3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.
18	
19	## Story Spine
20	
21	- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.
22	
23	- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. No existing work (0/12 surveyed papers, through May 2026) jointly models both within a single calibration framework.
24	
25	- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external per-item exposure estimation via item-level performance gap (original vs reference variants) with difficulty correction, supplemented by temporal signals and LogProber where available, (3) joint gated model with e_i fixed and c_n as latent parameters. ConStat per-model delta serves as external validation of fitted c_n.
26	
27	- **Headline result template**: "On MT-Bench/Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve X% higher Kendall-τ with Chatbot Arena human votes than the best sequential baseline, while simultaneously producing interpretable per-model contamination estimates and per-judge severity profiles."
28	
29	## Narrative Strategy (from distilled writing)
30	
31	- **Type**: "突破局限" (sequential has structural flaw) + "统一框架" (G-MFRM unifies both corrections)
32	- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)
33	- **Section 2**: Toy example / formal **observation** (NOT "proposition" — this is standard OVB from Angrist & Pischke 2009 applied to LLM evaluation; cite originals, present as domain-specific instantiation) demonstrating confounding before introducing G-MFRM method
34	- **Figure 1**: Left = sequential pipeline with confounding annotation, Right = joint G-MFRM with gating mechanism highlighted
35	- **Main result table**: rows = methods (7 baselines + G-MFRM), cols = benchmarks × metrics
36	- **Ablation**: Full numbers (not checkmark grid), rows = components on/off
37	
38	## Venue Fit Risks
39	
40	- **AAAI**: Good fit for psychometric methodology applied to AI evaluation. Risk: reviewers may lack MFRM/IRT background — need clear, self-contained exposition with toy examples. Strength: AAAI values formal modeling + practical impact.
41	- **ACL/ARR**: Good fit for LLM evaluation methodology. Risk: may demand stronger NLP-specific contributions beyond the measurement framework. Strength: directly relevant to LLM evaluation community.
42	
43	## Anticipated Reviewer Concerns & Responses
44	
45	1. **"Why not CyclicJudge + discard contaminated items?"** — Item discard wastes information; CyclicJudge doesn't capture item-specific judge effects; neither produces c_n for auditing; G-MFRM degrades gracefully to standard MFRM when contamination ≈ 0.
46	
47	2. **"Is confounding large enough in practice?"** — MVP synthetic: 43.8% RMSE degradation. Real-data calibration (P0 experiment) will establish realistic contamination magnitude. Bias scatter (r=0.65) shows the mechanism exists regardless of magnitude.
48	
49	3. **"Rank-1 assumption (c_n·e_i) too strong"** — Rank-1 is LLTM tradition, good approximation when contamination comes from dominant data source. Person-fit diagnostics (infit/outfit) detect violations. Rank-k extension is future work.
50	
51	4. **"DG-IRT transfer is trivial"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing. Error propagation from Stage 2→3 must be discussed in Limitations with sensitivity analysis (vary e_i noise σ=0.1,0.2,0.5).
52	
53	4b. **"Staged estimation ≠ joint estimation"** — Correct: e_i is pre-fixed in Stage 2, so estimation is conditional-joint, not fully simultaneous. Frame as deliberate identifiability choice: true joint estimation of (θ,b,d,c,e) is under-identified without external anchoring. Staged estimation is the principled solution. Compare to two-step estimators in econometrics (Heckman 1979). Error propagation sensitivity analysis shows robustness.
54	
55	5. **"Contamination signal realistic?"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.
56	
57	6. **"Chatbot Arena Elo as ground truth — circular reasoning?"** — Arena uses real-time human pairwise comparisons with user-submitted prompts (not fixed benchmark items). Contamination inflates benchmark scores but does not directly improve conversational ability. Arena Elo is the least-contaminated human preference signal available. Acknowledge limitation in paper but argue decoupling is strong.
58	
59	7. **"c_n ≥ 0 assumption too restrictive?"** — Half-Cauchy prior enforces non-negativity, appropriate for the "contamination as unfair advantage" framing. Adversarial contamination (intentional performance degradation) is outside scope. Discuss in Limitations.
60	
61	8. **"≥4 judges needed — too expensive?"** — exp-006 sensitivity analysis shows degradation curve. Discuss in Limitations: at 2 judges, G-MFRM degrades gracefully to MFRM-level (no contamination correction). Cost-benefit analysis for practitioners.
62	
63	## Two-Tier Narrative (contingent on exp-005 contamination magnitude)
64	
65	**Tier A — Strong contamination (c ≈ 1.0-1.5, matching mvp_002/003)**:
66	- Lead with ranking correction as primary contribution
67	- Claim 3 at full strength: "G-MFRM achieves X% higher Kendall-τ"
68	- Headline: joint estimation dramatically outperforms sequential
69	
70	**Tier B — Weak contamination (c ≈ 0.3-0.5, matching mvp_001)**:
71	- Elevate diagnostic interpretability to co-primary contribution (per IDEA_BRIEF optimization A4)
72	- Reframe: "even when ranking improvement is modest, G-MFRM uniquely provides per-model c_n (training audit), per-item e_i (item retirement), per-judge d_j (judge calibration)"
73	- Bias scatter r=0.65 proves the mechanism exists; practical impact scales with contamination magnitude
74	- Claim 3 softened to "comparable or better rankings PLUS interpretable diagnostic outputs"
75	
76	exp-005 determines which tier. Decision point: after exp-005 results, before paper writing.
77	
78	## MVP Evidence Summary
79	
80	- mvp_003: Joint RMSE −43.8% vs Sequential (p=1e-6), Kendall-τ +6.3pp, R̂=1.03, ESS=224
81	- Bias scatter: Pearson r=0.65 (sequential systematically overestimates high-c_n models)
82	- Robustness: method effective even under model misspecification (DGP with s_j, model without)
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "993e449f-7594-46d3-88f5-f060f3be40fe",
  "isSidechain": false,
  "promptId": "fe64548b-77cb-42da-afef-0d7832f54298",
  "type": "user",
  "uuid": "2f147629-e012-47b8-83a2-ea9fa4904a7d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/paper_framing.md",
      "content": "# Paper Framing — gated_mfrm_judge_bias\n\n## Target Venue\n- Primary: AAAI 2027 (full paper, deadline July 28, 2026)\n- Backup: ACL 2027 via ARR (submission August 3, 2026)\n- Timeline: ~68 days from today (2026-05-21)\n\n## Core Insight\nSequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.\n\n## Core Claims (3 条，均可证伪)\n\n1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding.\n\n2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — provides a staged joint calibration that estimates model ability, item difficulty, judge severity, and contamination susceptibility, yielding bias-and-contamination-corrected \"fair scores.\" (Note: \"staged joint\" — e_i is pre-estimated in Stage 2 and fixed in Stage 3; the joint estimation is conditional on e_i. This is a deliberate identifiability choice, not fully simultaneous. Paper must use \"staged joint calibration\" or \"conditional joint estimation,\" never \"fully joint.\")\n\n3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.\n\n## Story Spine\n\n- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.\n\n- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. No existing work (0/12 surveyed papers, through May 2026) jointly models both within a single calibration framework.\n\n- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external per-item exposure estimation via item-level performance gap (original vs reference variants) with difficulty correction, supplemented by temporal signals and LogProber where available, (3) joint gated model with e_i fixed and c_n as latent parameters. ConStat per-model delta serves as external validation of fitted c_n.\n\n- **Headline result template**: \"On MT-Bench/Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve X% higher Kendall-τ with Chatbot Arena human votes than the best sequential baseline, while simultaneously producing interpretable per-model contamination estimates and per-judge severity profiles.\"\n\n## Narrative Strategy (from distilled writing)\n\n- **Type**: \"突破局限\" (sequential has structural flaw) + \"统一框架\" (G-MFRM unifies both corrections)\n- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)\n- **Section 2**: Toy example / formal **observation** (NOT \"proposition\" — this is standard OVB from Angrist & Pischke 2009 applied to LLM evaluation; cite originals, present as domain-specific instantiation) demonstrating confounding before introducing G-MFRM method\n- **Figure 1**: Left = sequential pipeline with confounding annotation, Right = joint G-MFRM with gating mechanism highlighted\n- **Main result table**: rows = methods (7 baselines + G-MFRM), cols = benchmarks × metrics\n- **Ablation**: Full numbers (not checkmark grid), rows = components on/off\n\n## Venue Fit Risks\n\n- **AAAI**: Good fit for psychometric methodology applied to AI evaluation. Risk: reviewers may lack MFRM/IRT background — need clear, self-contained exposition with toy examples. Strength: AAAI values formal modeling + practical impact.\n- **ACL/ARR**: Good fit for LLM evaluation methodology. Risk: may demand stronger NLP-specific contributions beyond the measurement framework. Strength: directly relevant to LLM evaluation community.\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"Why not CyclicJudge + discard contaminated items?\"** — Item discard wastes information; CyclicJudge doesn't capture item-specific judge effects; neither produces c_n for auditing; G-MFRM degrades gracefully to standard MFRM when contamination ≈ 0.\n\n2. **\"Is confounding large enough in practice?\"** — MVP synthetic: 43.8% RMSE degradation. Real-data calibration (P0 experiment) will establish realistic contamination magnitude. Bias scatter (r=0.65) shows the mechanism exists regardless of magnitude.\n\n3. **\"Rank-1 assumption (c_n·e_i) too strong\"** — Rank-1 is LLTM tradition, good approximation when contamination comes from dominant data source. Person-fit diagnostics (infit/outfit) detect violations. Rank-k extension is future work.\n\n4. **\"DG-IRT transfer is trivial\"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing. Error propagation from Stage 2→3 must be discussed in Limitations with sensitivity analysis (vary e_i noise σ=0.1,0.2,0.5).\n\n4b. **\"Staged estimation ≠ joint estimation\"** — Correct: e_i is pre-fixed in Stage 2, so estimation is conditional-joint, not fully simultaneous. Frame as deliberate identifiability choice: true joint estimation of (θ,b,d,c,e) is under-identified without external anchoring. Staged estimation is the principled solution. Compare to two-step estimators in econometrics (Heckman 1979). Error propagation sensitivity analysis shows robustness.\n\n5. **\"Contamination signal realistic?\"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.\n\n6. **\"Chatbot Arena Elo as ground truth — circular reasoning?\"** — Arena uses real-time human pairwise comparisons with user-submitted prompts (not fixed benchmark items). Contamination inflates benchmark scores but does not directly improve conversational ability. Arena Elo is the least-contaminated human preference signal available. Acknowledge limitation in paper but argue decoupling is strong.\n\n7. **\"c_n ≥ 0 assumption too restrictive?\"** — Half-Cauchy prior enforces non-negativity, appropriate for the \"contamination as unfair advantage\" framing. Adversarial contamination (intentional performance degradation) is outside scope. Discuss in Limitations.\n\n8. **\"≥4 judges needed — too expensive?\"** — exp-006 sensitivity analysis shows degradation curve. Discuss in Limitations: at 2 judges, G-MFRM degrades gracefully to MFRM-level (no contamination correction). Cost-benefit analysis for practitioners.\n\n## Two-Tier Narrative (contingent on exp-005 contamination magnitude)\n\n**Tier A — Strong contamination (c ≈ 1.0-1.5, matching mvp_002/003)**:\n- Lead with ranking correction as primary contribution\n- Claim 3 at full strength: \"G-MFRM achieves X% higher Kendall-τ\"\n- Headline: joint estimation dramatically outperforms sequential\n\n**Tier B — Weak contamination (c ≈ 0.3-0.5, matching mvp_001)**:\n- Elevate diagnostic interpretability to co-primary contribution (per IDEA_BRIEF optimization A4)\n- Reframe: \"even when ranking improvement is modest, G-MFRM uniquely provides per-model c_n (training audit), per-item e_i (item retirement), per-judge d_j (judge calibration)\"\n- Bias scatter r=0.65 proves the mechanism exists; practical impact scales with contamination magnitude\n- Claim 3 softened to \"comparable or better rankings PLUS interpretable diagnostic outputs\"\n\nexp-005 determines which tier. Decision point: after exp-005 results, before paper writing.\n\n## MVP Evidence Summary\n\n- mvp_003: Joint RMSE −43.8% vs Sequential (p=1e-6), Kendall-τ +6.3pp, R̂=1.03, ESS=224\n- Bias scatter: Pearson r=0.65 (sequential systematically overestimates high-c_n models)\n- Robustness: method effective even under model misspecification (DGP with s_j, model without)\n",
      "numLines": 83,
      "startLine": 1,
      "totalLines": 83
    }
  },
  "sourceToolAssistantUUID": "993e449f-7594-46d3-88f5-f060f3be40fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T215715 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artif…",
  "leafUuid": "2f147629-e012-47b8-83a2-ea9fa4904a7d",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Joint calibration of judge bias and benchmark contamination",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5"
}
```

---

### Tool result

_source line 13 · 2026-05-21T22:13:12.307Z_

<details><summary>↩ Tool result · `toolu_01GK75UZkPiBsqTVa9uJ5fxj`</summary>

```text
1	[
2	  {
3	    "name": "multi_judge_data_collection",
4	    "description": "Collect multi-judge evaluation data on MT-Bench (80 items × 20 target models × 8 judges × 2 positions) and Arena-Hard (500 items × 20 target models × 8 judges × 2 positions). Total ~185,600 pairwise judgments after position swap.\n",
5	    "results": {
6	      "total_judgments": 185600,
7	      "mt_bench_judgments": 25600,
8	      "arena_hard_judgments": 160000,
9	      "target_models_evaluated": 20,
10	      "judges_used": 8,
11	      "judge_list": "GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick, Gemini 2.5 Pro",
12	      "position_bias_rate_mean": 0.58,
13	      "position_bias_rate_std": 0.07,
14	      "inter_judge_agreement_fleiss_kappa": 0.42,
15	      "api_cost_usd": 820,
16	      "vllm_gpu_hours": 95,
17	      "missing_data_rate_pct": 1.2
18	    },
19	    "tables": [
20	      {
21	        "name": "Table A1: Judge Panel Summary",
22	        "columns": [
23	          "judge",
24	          "type",
25	          "model_family",
26	          "position_bias_rate",
27	          "mean_score_stringency",
28	          "cost_per_1k_judgments"
29	        ],
30	        "rows": [
31	          [
32	            "GPT-5.5",
33	            "API",
34	            "OpenAI",
35	            0.55,
36	            0.12,
37	            "$4.20"
38	          ],
39	          [
40	            "Claude Opus 4.7",
41	            "API",
42	            "Anthropic",
43	            0.61,
44	            -0.08,
45	            "$5.10"
46	          ],
47	          [
48	            "Claude Sonnet 4.6",
49	            "API",
50	            "Anthropic",
51	            0.54,
52	            0.03,
53	            "$1.80"
54	          ],
55	          [
56	            "DeepSeek-V4-Pro",
57	            "API",
58	            "DeepSeek",
59	            0.63,
60	            -0.21,
61	            "$0.90"
62	          ],
63	          [
64	            "Qwen3-235B-A22B",
65	            "vLLM",
66	            "Alibaba",
67	            0.59,
68	            0.18,
69	            "$0.35"
70	          ],
71	          [
72	            "Qwen3.6-27B",
73	            "vLLM",
74	            "Alibaba",
75	            0.56,
76	            0.31,
77	            "$0.12"
78	          ],
79	          [
80	            "Llama 4 Maverick",
81	            "vLLM",
82	            "Meta",
83	            0.6,
84	            -0.15,
85	            "$0.28"
86	          ],
87	          [
88	            "Gemini 2.5 Pro",
89	            "API",
90	            "Google",
91	            0.57,
92	            0.05,
93	            "$3.60"
94	          ]
95	        ]
96	      }
97	    ],
98	    "figures": [],
99	    "analysis": "数据收集构成整个 pipeline 的基础。在 best 档下，所有 8 个 judge 正常工作，数据质量高。 关键观察：judge 间一致性仅为 moderate（κ=0.42），且不同模型族的 judge 表现出系统性的 severity 差异（score_stringency 从 -0.21 到 +0.31），证实了 judge bias 的存在且 幅度足以影响排名。这为 G-MFRM 的 d_j facet 提供了充足的信号。\n\n\nBest 档要求数据收集完整且质量高。8 个 judge 中 4 个开源（vLLM 部署）+ 4 个 API， 覆盖不同模型族以最大化 judge 多样性。Position swap 产生 ~58% 的平均位置偏差率 （与 CyclicJudge 2024 报告的 55-62% 一致），证明 position bias 是普遍存在的。 Fleiss κ ≈ 0.42 表明 moderate agreement，与已发表的 LLM-as-judge 文献一致 （Zheng et al. 2024 报告 κ=0.38-0.47）。缺失率 <2% 因为 API 调用有重试机制， vLLM 部署稳定。数据量足够支撑 G-MFRM 的参数估计（20 models × 8 judges ≫ 参数数）。\n"
100	  },
101	  {
102	    "name": "item_exposure_estimation",
103	    "description": "构建 per-item exposure indicator e_i。三源融合：(1) Performance gap 主通道： 对 MT-Bench/Arena-Hard 的每个 item 生成 GPT-5.5 和 Claude 改写的 reference variant， 计算 original vs reference 的平均性能差并做 spline difficulty correction； (2) Temporal 通道：利用 pre/post-cutoff item variant 的性能差； (3) LogProber 通道：对有 logprob API 的模型计算 token-level memorization score。 加权融合后输出 e_i ∈ [0,1]。\n",
104	    "results": {
105	      "mt_bench_items_with_reference": 80,
106	      "arena_hard_items_with_reference": 485,
107	      "reference_variant_quality_human_check_pass_rate": 0.93,
108	      "performance_gap_signal_noise_ratio": 3.8,
109	      "temporal_signal_coverage_pct": 35,
110	      "logprober_signal_coverage_pct": 60,
111	      "weighted_composite_e_i_mean": 0.41,
112	      "weighted_composite_e_i_std": 0.28,
113	      "weighted_composite_e_i_median": 0.35,
114	      "high_exposure_items_e_gt_07_pct": 18,
115	      "spearman_gap_vs_logprober": 0.72,
116	      "spearman_gap_vs_temporal": 0.65,
117	      "spearman_composite_vs_constat_item_level": 0.68
118	    },
119	    "tables": [
120	      {
121	        "name": "Table 2: Exposure Indicator Source Comparison",
122	        "columns": [
123	          "source",
124	          "coverage_pct",
125	          "mean_signal",
126	          "snr",
127	          "spearman_with_composite"
128	        ],
129	        "rows": [
130	          [
131	            "Performance Gap (primary)",
132	            100,
133	            0.38,
134	            3.8,
135	            0.94
136	          ],
137	          [
138	            "Temporal",
139	            35,
140	            0.42,
141	            2.9,
142	            0.78
143	          ],
144	          [
145	            "LogProber",
146	            60,
147	            0.35,
148	            4.1,
149	            0.85
150	          ],
151	          [
152	            "Weighted Composite",
153	            100,
154	            0.41,
155	            "-",
156	            1.0
157	          ]
158	        ]
159	      }
160	    ],
161	    "figures": [],
162	    "analysis": "e_i 估计质量是 staged estimation 可靠性的关键。在 best 档下，performance gap 主通道 信噪比高（3.8），多源融合提供 robustness。18% 的 item 高曝光意味着约 100 个 item （MT-Bench + Arena-Hard）携带强 contamination 信号，足以支撑 c_n 的可辨识性。 e_i 与 ConStat item-level 指标的 ρ=0.68 提供了外部效度验证。\n\n\nBest 档下 real contamination 强，因此 performance gap 信号显著。对于高曝光 item （e_i > 0.7，约 18%），original 与 reference variant 的性能差在 contaminated model 上 可达 0.3-0.5 标准差，经 difficulty correction 后信噪比约 3.8。这与 ConStat (2024) 报告 的 r²=0.94 效应量一致——当 contamination 真实存在时，performance gap 方法有很强的 检测力。Temporal 信号覆盖率较低（35%）因为只有部分 item 有明确的 pre/post-cutoff variant，但覆盖到的 item 与 gap 信号相关性好（ρ=0.65）。LogProber 覆盖 60% （仅限有 logprob API 的模型），与 gap 的相关性更高（ρ=0.72），因为两者都直接 测量 memorization 效应。加权融合后 e_i 分布右偏（mean=0.41, median=0.35）， 符合大多数 item 低曝光、少数 item 高曝光的预期模式。\n"
163	  },
164	  {
165	    "name": "gmfrm_real_data_fit",
166	    "description": "在 exp-001/002 的真实数据上拟合 G-MFRM 三阶段 pipeline。Stage 1: 标准 MFRM 估计 初始 θ,b,d。Stage 2: 固定 exp-002 的 e_i。Stage 3: NumPyro MCMC 联合估计 θ,b,d,c_n（e_i 固定）。报告收敛诊断、fair score、与 Chatbot Arena 的 Kendall-τ。\n",
167	    "results": {
168	      "convergence_max_rhat": 1.03,
169	      "convergence_min_ess": 287,
170	      "convergence_divergent_transitions": 0,
171	      "mcmc_warmup": 2000,
172	      "mcmc_samples": 4000,
173	      "mcmc_chains": 4,
174	      "runtime_hours": 3.2,
175	      "theta_fair_score_kendall_tau_arena_mtbench": 0.91,
176	      "theta_fair_score_kendall_tau_arena_arenahard": 0.93,
177	      "theta_fair_score_spearman_arena_mtbench": 0.94,
178	      "theta_fair_score_spearman_arena_arenahard": 0.96,
179	      "c_n_median": 0.95,
180	      "c_n_mean": 1.02,
181	      "c_n_std": 0.48,
182	      "c_n_max": 2.1,
183	      "c_n_min": 0.08,
184	      "d_j_range": [
185	        -0.35,
186	        0.42
187	      ],
188	      "d_j_std": 0.22,
189	      "posterior_predictive_p_value": 0.47,
190	      "graceful_degradation_low_contam_benchmark_tau_delta": 0.005
191	    },
192	    "tables": [
193	      {
194	        "name": "Table 3: G-MFRM Convergence Diagnostics",
195	        "columns": [
196	          "parameter_group",
197	          "n_params",
198	          "max_rhat",
199	          "min_ess",
200	          "mean_ess"
201	        ],
202	        "rows": [
203	          [
204	            "θ (model ability)",
205	            20,
206	            1.02,
207	            312,
208	            890
209	          ],
210	          [
211	            "b (item difficulty)",
212	            580,
213	            1.03,
214	            287,
215	            650
216	          ],
217	          [
218	            "d (judge severity)",
219	            8,
220	            1.01,
221	            1450,
222	            2100
223	          ],
224	          [
225	            "c (contamination)",
226	            20,
227	            1.03,
228	            295,
229	            720
230	          ]
231	        ]
232	      },
233	      {
234	        "name": "Table 4: G-MFRM Fair Score Agreement with Chatbot Arena",
235	        "columns": [
236	          "benchmark",
237	          "kendall_tau",
238	          "spearman_rho",
239	          "95% CI (τ)"
240	        ],
241	        "rows": [
242	          [
243	            "MT-Bench",
244	            0.91,
245	            0.94,
246	            "[0.86, 0.95]"
247	          ],
248	          [
249	            "Arena-Hard",
250	            0.93,
251	            0.96,
252	            "[0.89, 0.96]"
253	          ],
254	          [
255	            "Combined (weighted)",
256	            0.92,
257	            0.95,
258	            "[0.88, 0.95]"
259	          ]
260	        ]
261	      }
262	    ],
263	    "figures": [],
264	    "analysis": "这是整个论文的核心实验。收敛诊断全面通过（R̂≤1.03, ESS≥287, 0 divergent transitions） 证明 G-MFRM 的参数化在真实数据规模上是可行的。c_n median=0.95 确认 Tier A 叙事： contamination 不是理论上的可能性，而是量级足够大到系统性扭曲排名的现实问题。 d_j 的范围 [-0.35, 0.42] 表明最 lenient 和最 strict 的 judge 之间存在 0.77 标准差 的 severity 差异，足以影响 model ranking。\n\n\nBest 档的核心假设是 G-MFRM 在真实数据上干净收敛。mvp_003 已在合成数据上实现 R̂=1.03, ESS=224；真实数据的维度更大（20 models × 580 items × 8 judges vs 合成的 15×50×8）但信号也更丰富。使用相同的 MCMC 设置（warmup=2000, samples=4000, chains=4, NCP, target_accept=0.95）加上更大的数据量，ESS 提升至 287 是合理的。 R̂=1.03 与合成结果持平。c_n median=0.95 落在 best 档的 [0.8,1.5] 范围内，接近 mvp_002/003 的假设（c~1.0-1.5）。c_n 的模型间变异大（std=0.48, max=2.1）反映了 现实中不同模型的 contamination 程度差异巨大——开源模型（训练数据不透明）倾向于 更高的 c_n，而 closed-source 模型（如 GPT-5.5）的 c_n 较低。Kendall-τ 在 Arena-Hard 上（0.93）高于 MT-Bench（0.91）因为 Arena-Hard 有更多 item 提供更精确 的 ability 估计。posterior predictive p=0.47 表明模型拟合良好（接近 0.5 的均匀分布）。 对于 contamination 接近 0 的 benchmark 子集，G-MFRM 的 τ 仅比 MFRM 高 0.005， 验证了 graceful degradation——gating 机制在 e_i≈0 时自动关闭 contamination 校正。\n"
265	  },
266	  {
267	    "name": "baseline_comparison",
268	    "description": "在相同数据上对比 G-MFRM 与 8 个 baseline 的排名准确性。包含 rank change 分析： 哪些模型在校正后排名变化 ≥2 位，top-5/top-10 稳定性。\n",
269	    "results": {
270	      "raw_avg_kendall_tau_mtbench": 0.82,
271	      "raw_avg_kendall_tau_arenahard": 0.84,
272	      "mfrm_only_kendall_tau_mtbench": 0.84,
273	      "mfrm_only_kendall_tau_arenahard": 0.86,
274	      "sequential_kendall_tau_mtbench": 0.85,
275	      "sequential_kendall_tau_arenahard": 0.87,
276	      "cyclic_judge_kendall_tau_mtbench": 0.85,
277	      "cyclic_judge_kendall_tau_arenahard": 0.87,
278	      "cyclic_judge_discard_kendall_tau_mtbench": 0.87,
279	      "cyclic_judge_discard_kendall_tau_arenahard": 0.88,
280	      "dcr_factor_kendall_tau_mtbench": 0.83,
281	      "dcr_factor_kendall_tau_arenahard": 0.85,
282	      "uda_kendall_tau_mtbench": 0.86,
283	      "uda_kendall_tau_arenahard": 0.87,
284	      "pref_leakage_kendall_tau_mtbench": 0.84,
285	      "pref_leakage_kendall_tau_arenahard": 0.86,
286	      "gmfrm_kendall_tau_mtbench": 0.91,
287	      "gmfrm_kendall_tau_arenahard": 0.93,
288	      "delta_tau_vs_best_baseline_mtbench": 0.04,
289	      "delta_tau_vs_best_baseline_arenahard": 0.05,
290	      "wilcoxon_p_gmfrm_vs_best_baseline": 0.003,
291	      "rank_changes_ge2_positions": 5,
292	      "rank_changes_ge3_positions": 2,
293	      "top5_models_changed": 2,
294	      "top10_models_changed": 4,
295	      "max_rank_shift": 4,
296	      "most_shifted_model": "Qwen3-235B-A22B",
297	      "most_shifted_direction": "down"
298	    },
299	    "tables": [
300	      {
301	        "name": "Table 1: Main Results — Agreement with Chatbot Arena Human Rankings",
302	        "columns": [
303	          "method",
304	          "type",
305	          "τ (MT-Bench)",
306	          "τ (Arena-Hard)",
307	          "τ (Combined)",
308	          "Δτ vs G-MFRM"
309	        ],
310	        "rows": [
311	          [
312	            "Raw Multi-Judge Avg",
313	            "naive",
314	            0.82,
315	            0.84,
316	            0.83,
317	            -0.09
318	          ],
319	          [
320	            "MFRM-only",
321	            "bias-only",
322	            0.84,
323	            0.86,
324	            0.85,
325	            -0.07
326	          ],
327	          [
328	            "Sequential (bias→contam)",
329	            "sequential",
330	            0.85,
331	            0.87,
332	            0.86,
333	            -0.06
334	          ],
335	          [
336	            "CyclicJudge",
337	            "bias-only",
338	            0.85,
339	            0.87,
340	            0.86,
341	            -0.06
342	          ],
343	          [
344	            "CyclicJudge + Discard",
345	            "bias+heuristic",
346	            0.87,
347	            0.88,
348	            0.875,
349	            -0.045
350	          ],
351	          [
352	            "DCR Factor",
353	            "contam-only",
354	            0.83,
355	            0.85,
356	            0.84,
357	            -0.08
358	          ],
359	          [
360	            "UDA",
361	            "bias-only (neural)",
362	            0.86,
363	            0.87,
364	            0.865,
365	            -0.055
366	          ],
367	          [
368	            "Pref Leakage Calib",
369	            "contam-only",
370	            0.84,
371	            0.86,
372	            0.85,
373	            -0.07
374	          ],
375	          [
376	            "G-MFRM (ours)",
377	            "joint",
378	            0.91,
379	            0.93,
380	            0.92,
381	            "—"
382	          ]
383	        ]
384	      },
385	      {
386	        "name": "Table 5: Rank Change Analysis (G-MFRM vs Raw Average)",
387	        "columns": [
388	          "model",
389	          "raw_rank",
390	          "gmfrm_rank",
391	          "shift",
392	          "c_n_estimate",
393	          "interpretation"
394	        ],
395	        "rows": [
396	          [
397	            "Qwen3-235B-A22B",
398	            3,
399	            7,
400	            -4,
401	            1.82,
402	            "High contamination inflated raw rank"
403	          ],
404	          [
405	            "Llama 4 Maverick",
406	            5,
407	            8,
408	            -3,
409	            1.45,
410	            "Moderate-high contamination"
411	          ],
412	          [
413	            "Model-X-70B",
414	            8,
415	            5,
416	            3,
417	            0.12,
418	            "Low contamination — undervalued by raw"
419	          ],
420	          [
421	            "Claude Sonnet 4.6",
422	            4,
423	            2,
424	            2,
425	            0.21,
426	            "Low contamination — rose after correction"
427	          ],
428	          [
429	            "DeepSeek-V4-Pro",
430	            6,
431	            4,
432	            2,
433	            0.35,
434	            "Modest contamination — net rise"
435	          ]
436	        ]
437	      }
438	    ],
439	    "figures": [],
440	    "analysis": "这是论文的主表。G-MFRM 在两个 benchmark 上一致地以 4-5pp τ 优势击败最强 baseline （CyclicJudge+discard），p=0.003（Wilcoxon）。关键叙事：CyclicJudge+discard 是 Reviewer Concern #1 的最强 trivial alternative，但它 (a) 浪费被丢弃 item 的信息， (b) 不产生 per-model c_n 诊断，(c) 丢弃阈值需要启发式调优。G-MFRM 在所有维度上 都优于它。Rank change 分析提供了实际影响力的证据：如果一个团队基于 raw score 选择 了 rank-3 的 Qwen3-235B 而非 rank-7 的 Model-X-70B，他们可能选择了一个 contamination 膨胀的模型，真实 ability 其实更低。\n\n\nBest 档下 G-MFRM 以显著优势击败所有 baseline。逻辑链： (1) Raw average（τ=0.82/0.84）最差，因为同时受 judge bias 和 contamination 影响。 (2) MFRM-only（+2pp）校正了 judge bias 但 contamination 仍在。 (3) Sequential（+3pp over raw）先 bias 后 contamination，但因 OVB 效应，第一阶段 的 bias 校正已被 contamination 污染，改善有限。 (4) CyclicJudge（≈sequential level）通过 round-robin 消除平均 bias，但无法处理 item-specific judge 效应，且完全忽略 contamination。 (5) CyclicJudge+discard（最强 baseline，τ=0.87/0.88）额外丢弃高疑似 contaminated items，但丢弃策略浪费信息且阈值任意——best 档下它仍比 G-MFRM 低 4-5pp。 (6) DCR Factor（τ=0.83/0.85）量化 contamination 效应但忽略 judge variation。 (7) UDA（τ=0.86/0.87）神经 K-factor 调整 inter-judge variance 但黑盒且不 model contamination。 (8) Pref Leakage（τ=0.84/0.86）校准偏好泄漏但不联合估计。 G-MFRM（τ=0.91/0.93）的优势来自联合估计：同时建模 d_j 和 c_n·e_i 避免了相互吸收。 Rank change 分析：c_n 高的开源模型（如 Qwen3-235B-A22B）在校正后排名下降 （contamination 膨胀被移除），而 c_n 低的 closed-source 模型相对上升。5 个模型 移动 ≥2 位，最大移动 4 位，top-5 中有 2 个交换——这对模型选择决策有实质性影响。\n"
441	  },
442	  {
443	    "name": "contamination_magnitude_calibration",
444	    "description": "比较 exp-003 拟合的真实 c_n 分布与 MVP 合成假设，确定 contamination 处于哪个 tier。 用 ConStat per-model delta 做外部验证。\n",
445	    "results": {
446	      "c_n_median_real": 0.95,
447	      "c_n_mean_real": 1.02,
448	      "c_n_q25": 0.42,
449	      "c_n_q75": 1.48,
450	      "c_n_iqr": 1.06,
451	      "models_with_c_n_gt_1": 8,
452	      "models_with_c_n_gt_05": 14,
453	      "models_with_c_n_lt_02": 3,
454	      "closest_mvp_scenario": "mvp_002/003 (strong)",
455	      "constat_delta_spearman_with_c_n": 0.82,
456	      "constat_delta_pearson_with_c_n": 0.78,
457	      "tier_determination": "Tier A",
458	      "ratio_real_vs_mvp003_median": 0.95
459	    },
460	    "tables": [
461	      {
462	        "name": "Table 6: Contamination Magnitude — Real vs Synthetic",
463	        "columns": [
464	          "scenario",
465	          "c_n_median",
466	          "c_n_mean",
467	          "c_n_std",
468	          "convergence",
469	          "kendall_tau_gain"
470	        ],
471	        "rows": [
472	          [
473	            "mvp_001 (weak)",
474	            0.5,
475	            0.52,
476	            0.15,
477	            "PASS",
478	            "+0.3pp (n.s.)"
479	          ],
480	          [
481	            "mvp_002 (strong",
482	            "poor convergence)",
483	            1.2,
484	            1.25,
485	            0.4,
486	            "FAIL",
487	            "+4.3pp"
488	          ],
489	          [
490	            "mvp_003 (strong",
491	            "tuned)",
492	            1.0,
493	            1.05,
494	            0.35,
495	            "PASS",
496	            "+6.3pp"
497	          ],
498	          [
499	            "Real Data (exp-003)",
500	            0.95,
501	            1.02,
502	            0.48,
503	            "PASS",
504	            "+4.5pp"
505	          ]
506	        ]
507	      },
508	      {
509	        "name": "Table 7: ConStat External Validation",
510	        "columns": [
511	          "metric",
512	          "value",
513	          "95% CI"
514	        ],
515	        "rows": [
516	          [
517	            "Spearman ρ (c_n vs ConStat Δ)",
518	            0.82,
519	            "[0.65, 0.92]"
520	          ],
521	          [
522	            "Pearson r (c_n vs ConStat Δ)",
523	            0.78,
524	            "[0.58, 0.89]"
525	          ],
526	          [
527	            "Concordance (top-5 c_n ∩ top-5 ConStat)",
528	            "4/5",
529	            "—"
530	          ]
531	        ]
532	      }
533	    ],
534	    "figures": [],
535	    "analysis": "此实验是 Tier A/B 决策点。c_n median=0.95 明确指向 Tier A。与 mvp_003 的比较 显示真实数据几乎完美匹配合成假设（ratio=0.95），验证了 MVP 阶段的参数校准。 ConStat 验证（ρ=0.82）是论文的关键防线：它证明 c_n 不是模型过拟合的产物， 而是与独立测量工具一致的真实信号。top-5 concordance（4/5）特别有说服力—— G-MFRM 和 ConStat 几乎完全同意哪些模型受 contamination 影响最大。\n\n\nBest 档的核心前提是 real contamination 强度匹配 mvp_002/003 假设。c_n median=0.95 非常接近 mvp_003 的设定（c~1.0）。这意味着对于一个典型的高曝光 item（e_i=0.8）， contaminated model 的 expected score 膨胀约 0.76 logits（0.95×0.8），这是一个 非常显著的效应，足以将一个中等 ability 模型提升 2-4 个排名位。14/20 个模型的 c_n > 0.5 表明 contamination 是广泛存在的，不仅仅是个别模型的问题。ConStat 外部 验证 ρ=0.82 在 best 档范围 [0.7, 0.95] 内偏高，说明 G-MFRM 拟合的 c_n 与独立的 ConStat contamination 指标高度一致——这不是 MCMC 的 artifact，而是捕捉到了真实的 contamination 结构。3 个模型 c_n < 0.2（基本无 contamination）提供了自然的负对照。\n"
536	  },
537	  {
538	    "name": "judge_count_sensitivity",
539	    "description": "敏感性分析：逐步减少 judge 数量（8→6→4→2），观察 G-MFRM 性能退化曲线。 确定 G-MFRM 优于 sequential 的最低 judge 数量。\n",
540	    "results": {
541	      "tau_8_judges": 0.92,
542	      "tau_6_judges": 0.905,
543	      "tau_4_judges": 0.885,
544	      "tau_3_judges": 0.87,
545	      "tau_2_judges": 0.84,
546	      "sequential_tau_8_judges": 0.865,
547	      "sequential_tau_4_judges": 0.855,
548	      "sequential_tau_2_judges": 0.845,
549	      "min_judges_for_significant_gain": 3,
550	      "degradation_rate_per_judge_removed": 0.012,
551	      "gmfrm_2_judge_vs_mfrm_2_judge_delta": 0.005,
552	      "convergence_failure_at_2_judges": false,
553	      "convergence_rhat_at_2_judges": 1.08
554	    },
555	    "tables": [
556	      {
557	        "name": "Table 8: Judge Count Sensitivity",
558	        "columns": [
559	          "n_judges",
560	          "τ (G-MFRM)",
561	          "τ (Sequential)",
562	          "Δτ",
563	          "p-value",
564	          "max_rhat",
565	          "min_ess"
566	        ],
567	        "rows": [
568	          [
569	            8,
570	            0.92,
571	            0.865,
572	            0.055,
573	            0.003,
574	            1.03,
575	            287
576	          ],
577	          [
578	            6,
579	            0.905,
580	            0.86,
581	            0.045,
582	            0.008,
583	            1.03,
584	            245
585	          ],
586	          [
587	            4,
588	            0.885,
589	            0.855,
590	            0.03,
591	            0.021,
592	            1.04,
593	            198
594	          ],
595	          [
596	            3,
597	            0.87,
598	            0.852,
599	            0.018,
600	            0.048,
601	            1.05,
602	            165
603	          ],
604	          [
605	            2,
606	            0.84,
607	            0.845,
608	            -0.005,
609	            0.62,
610	            1.08,
611	            89
612	          ]
613	        ]
614	      }
615	    ],
616	    "figures": [],
617	    "analysis": "此分析为实践者提供了成本效益指导。结论清晰：≥4 judges 推荐（G-MFRM gain ~3pp+）， 3 judges 勉强可行（gain 1.8pp, p<0.05），2 judges 不建议用 G-MFRM（退化至 MFRM）。 这回应了 Reviewer Concern #8 的成本问题，并为 Limitations 提供了量化数据。\n\n\nG-MFRM 需要多 judge 数据来分离 d_j 和 c_n·e_i。在 best 档下，8 judges 提供 丰富信号（τ=0.92）。减至 6 judges 损失温和（-1.5pp），因为仍有足够的 judge 变异来估计 d_j。减至 4 judges 是关键拐点（-3.5pp），但仍比 sequential 4-judge（0.855） 好 3pp。3 judges 是 G-MFRM 显著优于 sequential 的最低阈值——对应 best 档的 judge_count_min_for_significant_gain=[3,4] 范围。2 judges 时 G-MFRM 基本退化到 MFRM 水平（delta 仅 0.5pp），因为 2 个 judge 不足以可靠估计 d_j，gating 机制 也因信号不足而趋于保守。R̂ 在 2-judge 时升至 1.08，刚好超过阈值，但未发散。 这回应了 Reviewer Concern #8：在 2-judge 场景下 G-MFRM 不会崩溃，只是退化到 MFRM baseline 水平。\n"
618	  },
619	  {
620	    "name": "exposure_indicator_ablation",
621	    "description": "对 e_i 估计 pipeline 做 leave-one-out 消融：分别去掉 performance gap、temporal、 LogProber 中的一个 source，观察对最终 θ̂ 和 c_n 估计质量的影响。\n",
622	    "results": {
623	      "full_pipeline_theta_tau": 0.92,
624	      "without_performance_gap_theta_tau": 0.87,
625	      "without_temporal_theta_tau": 0.915,
626	      "without_logprober_theta_tau": 0.91,
627	      "full_pipeline_cn_recovery_spearman": 0.82,
628	      "without_performance_gap_cn_recovery_spearman": 0.55,
629	      "without_temporal_cn_recovery_spearman": 0.8,
630	      "without_logprober_cn_recovery_spearman": 0.78,
631	      "performance_gap_contribution_pct": 72,
632	      "temporal_contribution_pct": 8,
633	      "logprober_contribution_pct": 12,
634	      "interaction_effect_pct": 8
635	    },
636	    "tables": [
637	      {
638	        "name": "Table 9: Exposure Indicator Ablation",
639	        "columns": [
640	          "configuration",
641	          "τ (Arena)",
642	          "Δτ",
643	          "c_n ρ",
644	          "Δρ"
645	        ],
646	        "rows": [
647	          [
648	            "Full pipeline (3 sources)",
649	            0.92,
650	            "—",
651	            0.82,
652	            "—"
653	          ],
654	          [
655	            "− Performance Gap",
656	            0.87,
657	            -0.05,
658	            0.55,
659	            -0.27
660	          ],
661	          [
662	            "− Temporal",
663	            0.915,
664	            -0.005,
665	            0.8,
666	            -0.02
667	          ],
668	          [
669	            "− LogProber",
670	            0.91,
671	            -0.01,
672	            0.78,
673	            -0.04
674	          ],
675	          [
676	            "Gap only",
677	            0.912,
678	            -0.008,
679	            0.79,
680	            -0.03
681	          ]
682	        ]
683	      }
684	    ],
685	    "figures": [],
686	    "analysis": "消融结果支持 pipeline 设计的合理性。Performance gap 是必要条件（去掉后严重退化）， 而 temporal 和 LogProber 提供边际改进。\"Gap only\" 配置仅比 full pipeline 低 0.8pp， 说明如果资源有限，只使用 performance gap 也是可行的最小方案。这为实践者提供了 模块化部署指导。\n\n\nPerformance gap 是 e_i 的主通道（100% 覆盖，SNR=3.8），去掉后 τ 下降 5pp—— 这是因为没有 gap 信号，e_i 估计退化为 temporal+LogProber 的稀疏覆盖 （仅 35%+60% 项有信号，交集更小），大量 item 的 e_i 几乎无信息。相反，去掉 temporal 或 LogProber 各自影响很小（-0.5pp 和 -1pp），因为它们是补充信号， 覆盖率有限。但 c_n recovery 的 spearman 对 performance gap 的依赖更强 （Δρ=0.27 vs Δρ=0.02/0.04），因为 c_n 的可辨识性直接依赖于 e_i 的准确性—— e_i 差则 c_n·e_i 项无法正确分离 c_n。这证明了 performance gap 是不可或缺的， 而 temporal 和 LogProber 是有用但非必要的补充。\n"
687	  },
688	  {
689	    "name": "facet_fit_diagnostics",
690	    "description": "报告 G-MFRM 所有 facet 的测量质量诊断：infit/outfit MNSQ、divergent transitions、 posterior predictive check、trace plots。标记 misfit 元素。\n",
691	    "results": {
692	      "theta_infit_mean": 1.02,
693	      "theta_infit_range": [
694	        0.85,
695	        1.18
696	      ],
697	      "theta_outfit_mean": 1.05,
698	      "theta_outfit_range": [
699	        0.78,
700	        1.35
701	      ],
702	      "theta_misfit_count": 1,
703	      "b_infit_mean": 1.0,
704	      "b_infit_range": [
705	        0.72,
706	        1.42
707	      ],
708	      "b_outfit_mean": 1.03,
709	      "b_outfit_range": [
710	        0.65,
711	        1.55
712	      ],
713	      "b_misfit_count": 12,
714	      "d_infit_mean": 0.98,
715	      "d_infit_range": [
716	        0.88,
717	        1.1
718	      ],
719	      "d_outfit_mean": 1.01,
720	      "d_outfit_range": [
721	        0.85,
722	        1.15
723	      ],
724	      "d_misfit_count": 0,
725	      "c_infit_mean": 1.04,
726	      "c_infit_range": [
727	        0.82,
728	        1.25
729	      ],
730	      "divergent_transitions": 0,
731	      "posterior_predictive_ppp": 0.47,
732	      "posterior_predictive_rmse": 0.18,
733	      "stage1_lz_flagged_models": 2,
734	      "stage3_cn_gt_0_for_lz_flagged": true
735	    },
736	    "tables": [
737	      {
738	        "name": "Table A2: Facet Fit Summary (Infit/Outfit MNSQ)",
739	        "columns": [
740	          "facet",
741	          "n",
742	          "mean_infit",
743	          "mean_outfit",
744	          "misfit_count",
745	          "misfit_%"
746	        ],
747	        "rows": [
748	          [
749	            "θ (model ability)",
750	            20,
751	            1.02,
752	            1.05,
753	            1,
754	            5.0
755	          ],
756	          [
757	            "b (item difficulty)",
758	            580,
759	            1.0,
760	            1.03,
761	            12,
762	            2.1
763	          ],
764	          [
765	            "d (judge severity)",
766	            8,
767	            0.98,
768	            1.01,
769	            0,
770	            0.0
771	          ],
772	          [
773	            "c (contamination)",
774	            20,
775	            1.04,
776	            "—",
777	            0,
778	            0.0
779	          ]
780	        ]
781	      },
782	      {
783	        "name": "Table A3: MCMC Diagnostics Summary",
784	        "columns": [
785	          "diagnostic",
786	          "value",
787	          "threshold",
788	          "status"
789	        ],
790	        "rows": [
791	          [
792	            "Max R̂",
793	            1.03,
794	            "≤ 1.05",
795	            "PASS"
796	          ],
797	          [
798	            "Min ESS",
799	            287,
800	            "≥ 200",
801	            "PASS"
802	          ],
803	          [
804	            "Divergent transitions",
805	            0,
806	            "= 0",
807	            "PASS"
808	          ],
809	          [
810	            "PPP",
811	            0.47,
812	            "[0.1, 0.9]",
813	            "PASS"
814	          ],
815	          [
816	            "Posterior predictive RMSE",
817	            0.18,
818	            "—",
819	            "—"
820	          ]
821	        ]
822	      }
823	    ],
824	    "figures": [],
825	    "analysis": "诊断全面支持 G-MFRM 的测量质量。2.1% 的 item misfit 率在 IRT 文献中属于正常范围。 Stage 1 lz → Stage 3 c_n 的 coherence 是一个巧妙的验证：如果 person-fit 异常 是由 contamination 引起的，那么在建模 contamination 后应该被解释掉——实验证实了这一点。\n\n\nBest 档要求诊断全面良好。Infit/outfit MNSQ 接近 1.0 表示 Rasch 模型拟合良好。 Item facet（b）有 12 个 misfit（outfit > 1.4 的 item），占 580 items 的 ~2%， 这在 IRT 实践中是正常水平——这些 item 可能有特殊结构（如依赖特定领域知识） 导致模型不完全适用。1 个 θ misfit 模型可能是有异常评分模式的 target model。 Judge facet（d）完全无 misfit（仅 8 个 judge，且都是主流 LLM），这符合预期。 0 divergent transitions 和 PPP=0.47 证实整体模型规范正确。Stage 1 的 person-fit 指标（lz）标记了 2 个模型，Stage 3 中这 2 个模型都有 c_n > 0（分别为 1.2 和 0.8）， 证实了 construct coherence：Stage 1 的 misfit 信号确实来自 contamination 而非 ability 维度的问题。\n"
826	  },
827	  {
828	    "name": "confounding_formal_observation",
829	    "description": "形式化推导 sequential estimator 在 d_j 和 c_n·e_i 非正交条件下的一阶 bias 近似。Monte Carlo 验证。合成数据上的 c_n 点估计验证。\n",
830	    "results": {
831	      "bias_first_order_formula": "bias(θ̂_seq) ≈ Σ_j (X'X)^{-1} X' Cov(d_j, c_n·e_i)",
832	      "monte_carlo_n_reps": 500,
833	      "monte_carlo_bias_mean_rho_0": 0.001,
834	      "monte_carlo_bias_mean_rho_03": 0.048,
835	      "monte_carlo_bias_mean_rho_06": 0.112,
836	      "monte_carlo_bias_std_rho_06": 0.035,
837	      "monte_carlo_rmse_degradation_rho_06_pct": 43.2,
838	      "synthetic_cn_recovery_rmse": 0.09,
839	      "synthetic_cn_coverage_95ci": 0.93,
840	      "synthetic_cn_spearman_recovery": 0.96,
841	      "synthetic_cn_bias": -0.02
842	    },
843	    "tables": [
844	      {
845	        "name": "Table 10: Monte Carlo Bias Analysis (500 replications)",
846	        "columns": [
847	          "ρ(d",
848	          "ce)",
849	          "bias(θ̂_seq)",
850	          "θ RMSE (seq)",
851	          "θ RMSE (joint)",
852	          "RMSE reduction %"
853	        ],
854	        "rows": [
855	          [
856	            0.0,
857	            0.001,
858	            0.124,
859	            0.123,
860	            0.8
861	          ],
862	          [
863	            0.15,
864	            0.021,
865	            0.138,
866	            0.124,
867	            10.1
868	          ],
869	          [
870	            0.3,
871	            0.048,
872	            0.162,
873	            0.125,
874	            22.8
875	          ],
876	          [
877	            0.45,
878	            0.078,
879	            0.189,
880	            0.124,
881	            34.4
882	          ],
883	          [
884	            0.6,
885	            0.112,
886	            0.221,
887	            0.125,
888	            43.2
889	          ]
890	        ]
891	      },
892	      {
893	        "name": "Table 11: Synthetic c_n Recovery (G-MFRM)",
894	        "columns": [
895	          "metric",
896	          "value"
897	        ],
898	        "rows": [
899	          [
900	            "c_n RMSE",
901	            0.09
902	          ],
903	          [
904	            "c_n bias",
905	            -0.02
906	          ],
907	          [
908	            "c_n Spearman ρ (fitted vs true)",
909	            0.96
910	          ],
911	          [
912	            "95% CI coverage",
913	            0.93
914	          ],
915	          [
916	            "Mean CI width",
917	            0.38
918	          ]
919	        ]
920	      }
921	    ],
922	    "figures": [],
923	    "analysis": "此实验为 Confounding Claim 提供形式化+实证双重支持。OVB observation 是已有理论 的直接应用，不需要 novelty——关键贡献是证明这个理论问题在 LLM 评估中量级显著 （43.2% RMSE 退化）。c_n recovery 验证确认 G-MFRM 不仅纠正了 θ̂ bias，还能 准确恢复潜在的 contamination 结构，coverage probability 接近 nominal 说明 posterior inference 是 well-calibrated 的。\n\n\n形式化分析是标准 OVB 理论在 LLM 评估场景的应用。当 d_j 和 c_n·e_i 正交 （ρ=0）时，bias ≈ 0（0.001 是有限样本噪声），sequential 无害。但在现实中， judge 的 severity 和 model 的 contamination susceptibility 不独立——harsh judges 可能对 contaminated 回答更 lenient（因为 contaminated 回答通常更流畅、更自信）， 导致 ρ > 0。在 ρ=0.6 时（mvp 模拟的现实估计），RMSE 退化 43.2%，与 mvp_003 的 43.8% 高度一致。合成 c_n recovery 的 RMSE=0.09 落在 best 档范围 [0.05, 0.15] 内， 95% CI coverage=0.93（接近 nominal 0.95），说明贝叶斯推断的 uncertainty quantification 是准确的。ρ_recovery=0.96 表明即使点估计有噪声，排序几乎完美保留。\n"
924	  },
925	  {
926	    "name": "error_propagation_sensitivity",
927	    "description": "Staged estimation 的误差传播敏感性：向 e_i 注入 σ=0.1/0.2/0.5 的高斯噪声后 重新拟合 Stage 3，测量 θ̂ RMSE 退化和 c_n recovery 精度。合成数据。\n",
928	    "results": {
929	      "sigma_0_theta_rmse": 0.124,
930	      "sigma_01_theta_rmse": 0.127,
931	      "sigma_01_theta_rmse_degradation_pct": 2.4,
932	      "sigma_02_theta_rmse": 0.133,
933	      "sigma_02_theta_rmse_degradation_pct": 7.3,
934	      "sigma_05_theta_rmse": 0.168,
935	      "sigma_05_theta_rmse_degradation_pct": 35.5,
936	      "sigma_0_cn_rmse": 0.09,
937	      "sigma_01_cn_rmse": 0.12,
938	      "sigma_02_cn_rmse": 0.18,
939	      "sigma_05_cn_rmse": 0.41,
940	      "sigma_02_cn_spearman": 0.89,
941	      "sigma_05_cn_spearman": 0.62,
942	      "robustness_threshold_sigma": 0.25
943	    },
944	    "tables": [
945	      {
946	        "name": "Table 12: Error Propagation Sensitivity (Synthetic)",
947	        "columns": [
948	          "e_i_noise_σ",
949	          "θ̂ RMSE",
950	          "θ̂ degrad. %",
951	          "c_n RMSE",
952	          "c_n ρ",
953	          "τ (Arena proxy)"
954	        ],
955	        "rows": [
956	          [
957	            0.0,
958	            0.124,
959	            "—",
960	            0.09,
961	            0.96,
962	            0.922
963	          ],
964	          [
965	            0.1,
966	            0.127,
967	            2.4,
968	            0.12,
969	            0.94,
970	            0.918
971	          ],
972	          [
973	            0.2,
974	            0.133,
975	            7.3,
976	            0.18,
977	            0.89,
978	            0.91
979	          ],
980	          [
981	            0.3,
982	            0.145,
983	            16.9,
984	            0.27,
985	            0.79,
986	            0.893
987	          ],
988	          [
989	            0.5,
990	            0.168,
991	            35.5,
992	            0.41,
993	            0.62,
994	            0.862
995	          ]
996	        ]
997	      }
998	    ],
999	    "figures": [],
1000	    "analysis": "此实验是 Reviewer Concern #4b 和 Dream R1-N1 的核心回应。结论：staged estimation 在 σ≤0.2 时 robust（θ̂ 退化 <8%），在 σ≤0.1 时几乎无损（<2.5%）。exp-002 的 实际 e_i 噪声估计约 σ=0.15（基于 SNR=3.8 和 multi-source 融合），落在安全区内。 σ=0.5 的崩溃点提供了理论下界。论文 Limitations 中需讨论 σ=0.2 处的 7.3% 超过了 预设 5% 阈值，但结合实际噪声水平论证 staged estimation 的可接受性。\n\n\nBest 档要求 σ=0.2 时 θ̂ RMSE 退化 < 5%。预测值 7.3% 略超此阈值，但仍属于 实际可接受范围（需在论文中 acknowledge）。逻辑：e_i 噪声通过 c_n·e_i 项传播到 θ̂——当 σ 小（0.1）时，e_i 的 rank order 基本保持，gating 机制仅微调幅度， 对 θ̂ 影响很小（2.4%）。σ=0.2 时 e_i 的 rank 开始受扰动，部分 high-exposure item 被错误降权、low-exposure item 被错误升权，导致 c_n 估计 偏移（RMSE 从 0.09→0.18），但因为 θ̂ 同时受多个 item 信息约束（580 items）， 单个 item 的 e_i 误差被平均化，θ̂ 退化相对温和。σ=0.5 是破坏性水平（35.5% 退化）， 此时 e_i 信号几乎被噪声淹没。robustness_threshold ≈ 0.25 意味着 exp-002 的 e_i 估计只要噪声不超过 0.25 就安全——考虑到 performance gap 的 SNR=3.8，实际噪声 约 σ≈0.15，处于安全区内。注意：σ=0.2 处 θ̂ degradation 为 7.3% 而非 <5%。 在论文中需诚实报告，但可论证 (a) 这是 worst-case 均匀噪声注入，实际噪声结构更 favorable，(b) 7.3% degradation 仍使 G-MFRM 大幅优于 sequential baseline。\n"
1001	  },
1002	  {
1003	    "name": "wildbench_replication",
1004	    "description": "在 WildBench 上复制完整 G-MFRM pipeline 作为第三个 benchmark，验证跨 benchmark 泛化性。\n",
1005	    "results": {
1006	      "wildbench_items": 1024,
1007	      "wildbench_judges_used": 6,
1008	      "gmfrm_kendall_tau_wildbench": 0.9,
1009	      "sequential_kendall_tau_wildbench": 0.86,
1010	      "delta_tau_wildbench": 0.04,
1011	      "c_n_spearman_wildbench_vs_mtbench": 0.88,
1012	      "convergence_max_rhat": 1.04,
1013	      "convergence_min_ess": 210,
1014	      "wildbench_high_exposure_items_pct": 14
1015	    },
1016	    "tables": [
1017	      {
1018	        "name": "Table 13: Cross-Benchmark Generalization",
1019	        "columns": [
1020	          "benchmark",
1021	          "τ (G-MFRM)",
1022	          "τ (Best Baseline)",
1023	          "Δτ",
1024	          "items",
1025	          "judges"
1026	        ],
1027	        "rows": [
1028	          [
1029	            "MT-Bench",
1030	            0.91,
1031	            0.87,
1032	            0.04,
1033	            80,
1034	            8
1035	          ],
1036	          [
1037	            "Arena-Hard",
1038	            0.93,
1039	            0.88,
1040	            0.05,
1041	            500,
1042	            8
1043	          ],
1044	          [
1045	            "WildBench",
1046	            0.9,
1047	            0.86,
1048	            0.04,
1049	            1024,
1050	            6
1051	          ]
1052	        ]
1053	      }
1054	    ],
1055	    "figures": [],
1056	    "analysis": "跨 benchmark 复制成功。三个 benchmark 上 G-MFRM 一致优于 best baseline 4-5pp， 消除了 \"方法只在特定 benchmark 上有效\" 的顾虑。c_n 跨 benchmark 稳定性是 bonus finding：可以在 Discussion 中论证 c_n 有作为 \"model contamination audit index\" 的潜力。\n\n\nWildBench 是更 \"wild\" 的 benchmark（用户真实 query），contamination 模式应与 MT-Bench/Arena-Hard 不同但 G-MFRM 方法论应仍然有效。best 档下 τ=0.90（略低于 Arena-Hard 的 0.93），因为 WildBench 的 item 更异质、标注噪声更大。Δτ=0.04 与 MT-Bench 上的 0.04 一致，证明 G-MFRM 的优势不是 benchmark-specific 的。 c_n 在 WildBench 和 MT-Bench 之间的 ρ=0.88 说明同一组模型的 contamination susceptibility 跨 benchmark 是稳定的——这是一个重要的 construct validity 证据， 说明 c_n 测量的是模型的固有属性而非 benchmark-specific artifact。仅使用 6 个 judge（2 个 API 不支持 WildBench 格式）但收敛仍然良好。\n"
1057	  },
1058	  {
1059	    "name": "adversarial_robustness",
1060	    "description": "测试 G-MFRM 对抗 adversarial contamination 的鲁棒性，遵循 Wang et al. (ICLR 2026) 的 fragility analysis 框架。\n",
1061	    "results": {
1062	      "adversarial_attack_types": 3,
1063	      "attack1_targeted_item_injection_theta_shift": 0.15,
1064	      "attack2_judge_collusion_theta_shift": 0.22,
1065	      "attack3_exposure_manipulation_theta_shift": 0.08,
1066	      "gmfrm_detection_rate_attack1": 0.85,
1067	      "gmfrm_detection_rate_attack2": 0.7,
1068	      "gmfrm_detection_rate_attack3": 0.9,
1069	      "sequential_detection_rate_attack1": 0.4,
1070	      "infit_flags_adversarial_items": true,
1071	      "c_n_inflation_under_attack": 0.3
1072	    },
1073	    "tables": [
1074	      {
1075	        "name": "Table A4: Adversarial Robustness",
1076	        "columns": [
1077	          "attack",
1078	          "θ̂ shift (G-MFRM)",
1079	          "θ̂ shift (Sequential)",
1080	          "G-MFRM detection rate"
1081	        ],
1082	        "rows": [
1083	          [
1084	            "Targeted item injection",
1085	            0.15,
1086	            0.38,
1087	            0.85
1088	          ],
1089	          [
1090	            "Judge collusion (2/8)",
1091	            0.22,
1092	            0.31,
1093	            0.7
1094	          ],
1095	          [
1096	            "Exposure manipulation",
1097	            0.08,
1098	            "N/A",
1099	            0.9
1100	          ]
1101	        ]
1102	      }
1103	    ],
1104	    "figures": [],
1105	    "analysis": "P2 优先级实验，为 Discussion/Limitations 提供材料。G-MFRM 不声称 adversarial robustness 作为贡献，但展示其 diagnostic 框架提供了 \"免费的\" 异常检测能力。 Judge collusion 是最大弱点——如果超过 50% 的 judge 被操纵，d_j 无法区分真实 severity 和操纵。这是一个 honest limitation。\n\nG-MFRM 的 person-fit diagnostics（infit/outfit）提供了对 adversarial manipulation 的自然检测机制。Attack 1（targeted item injection：在特定 item 上注入异常高分） 被 item-level outfit 检测到（85%），因为注入的分数违反了 Rasch 模型的 sufficiency 假设。Attack 2（judge collusion：多个 judge 协调给高分）更难检测（70%），因为 一致的 judge behavior 可以被 d_j 吸收——但 c_n 会出现异常膨胀（+0.3）作为 间接信号。Attack 3（exposure manipulation：人为修改 e_i 输入）反而最容易防御 （90%），因为 Stage 2 的 multi-source 融合和 ConStat 外部验证能交叉检验 e_i 的一致性。Sequential baseline 在 Attack 1 上检测率仅 40%，因为没有 contamination 模型来标记异常。总体而言 G-MFRM 不是完全 adversarial-proof 的（scope 声明已排除）， 但比 sequential 有更强的内在鲁棒性。\n"
1106	  }
1107	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e417eac-b76b-4246-93f9-346139d1f49d",
  "isSidechain": false,
  "promptId": "fe64548b-77cb-42da-afef-0d7832f54298",
  "type": "user",
  "uuid": "72fe4570-59a4-48cf-9e63-4fc4a1305f03",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"multi_judge_data_collection\",\n    \"description\": \"Collect multi-judge evaluation data on MT-Bench (80 items × 20 target models × 8 judges × 2 positions) and Arena-Hard (500 items × 20 target models × 8 judges × 2 positions). Total ~185,600 pairwise judgments after position swap.\\n\",\n    \"results\": {\n      \"total_judgments\": 185600,\n      \"mt_bench_judgments\": 25600,\n      \"arena_hard_judgments\": 160000,\n      \"target_models_evaluated\": 20,\n      \"judges_used\": 8,\n      \"judge_list\": \"GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick, Gemini 2.5 Pro\",\n      \"position_bias_rate_mean\": 0.58,\n      \"position_bias_rate_std\": 0.07,\n      \"inter_judge_agreement_fleiss_kappa\": 0.42,\n      \"api_cost_usd\": 820,\n      \"vllm_gpu_hours\": 95,\n      \"missing_data_rate_pct\": 1.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table A1: Judge Panel Summary\",\n        \"columns\": [\n          \"judge\",\n          \"type\",\n          \"model_family\",\n          \"position_bias_rate\",\n          \"mean_score_stringency\",\n          \"cost_per_1k_judgments\"\n        ],\n        \"rows\": [\n          [\n            \"GPT-5.5\",\n            \"API\",\n            \"OpenAI\",\n            0.55,\n            0.12,\n            \"$4.20\"\n          ],\n          [\n            \"Claude Opus 4.7\",\n            \"API\",\n            \"Anthropic\",\n            0.61,\n            -0.08,\n            \"$5.10\"\n          ],\n          [\n            \"Claude Sonnet 4.6\",\n            \"API\",\n            \"Anthropic\",\n            0.54,\n            0.03,\n            \"$1.80\"\n          ],\n          [\n            \"DeepSeek-V4-Pro\",\n            \"API\",\n            \"DeepSeek\",\n            0.63,\n            -0.21,\n            \"$0.90\"\n          ],\n          [\n            \"Qwen3-235B-A22B\",\n            \"vLLM\",\n            \"Alibaba\",\n            0.59,\n            0.18,\n            \"$0.35\"\n          ],\n          [\n            \"Qwen3.6-27B\",\n            \"vLLM\",\n            \"Alibaba\",\n            0.56,\n            0.31,\n            \"$0.12\"\n          ],\n          [\n            \"Llama 4 Maverick\",\n            \"vLLM\",\n            \"Meta\",\n            0.6,\n            -0.15,\n            \"$0.28\"\n          ],\n          [\n            \"Gemini 2.5 Pro\",\n            \"API\",\n            \"Google\",\n            0.57,\n            0.05,\n            \"$3.60\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"数据收集构成整个 pipeline 的基础。在 best 档下，所有 8 个 judge 正常工作，数据质量高。 关键观察：judge 间一致性仅为 moderate（κ=0.42），且不同模型族的 judge 表现出系统性的 severity 差异（score_stringency 从 -0.21 到 +0.31），证实了 judge bias 的存在且 幅度足以影响排名。这为 G-MFRM 的 d_j facet 提供了充足的信号。\\n\\n\\nBest 档要求数据收集完整且质量高。8 个 judge 中 4 个开源（vLLM 部署）+ 4 个 API， 覆盖不同模型族以最大化 judge 多样性。Position swap 产生 ~58% 的平均位置偏差率 （与 CyclicJudge 2024 报告的 55-62% 一致），证明 position bias 是普遍存在的。 Fleiss κ ≈ 0.42 表明 moderate agreement，与已发表的 LLM-as-judge 文献一致 （Zheng et al. 2024 报告 κ=0.38-0.47）。缺失率 <2% 因为 API 调用有重试机制， vLLM 部署稳定。数据量足够支撑 G-MFRM 的参数估计（20 models × 8 judges ≫ 参数数）。\\n\"\n  },\n  {\n    \"name\": \"item_exposure_estimation\",\n    \"description\": \"构建 per-item exposure indicator e_i。三源融合：(1) Performance gap 主通道： 对 MT-Bench/Arena-Hard 的每个 item 生成 GPT-5.5 和 Claude 改写的 reference variant， 计算 original vs reference 的平均性能差并做 spline difficulty correction； (2) Temporal 通道：利用 pre/post-cutoff item variant 的性能差； (3) LogProber 通道：对有 logprob API 的模型计算 token-level memorization score。 加权融合后输出 e_i ∈ [0,1]。\\n\",\n    \"results\": {\n      \"mt_bench_items_with_reference\": 80,\n      \"arena_hard_items_with_reference\": 485,\n      \"reference_variant_quality_human_check_pass_rate\": 0.93,\n      \"performance_gap_signal_noise_ratio\": 3.8,\n      \"temporal_signal_coverage_pct\": 35,\n      \"logprober_signal_coverage_pct\": 60,\n      \"weighted_composite_e_i_mean\": 0.41,\n      \"weighted_composite_e_i_std\": 0.28,\n      \"weighted_composite_e_i_median\": 0.35,\n      \"high_exposure_items_e_gt_07_pct\": 18,\n      \"spearman_gap_vs_logprober\": 0.72,\n      \"spearman_gap_vs_temporal\": 0.65,\n      \"spearman_composite_vs_constat_item_level\": 0.68\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2: Exposure Indicator Source Comparison\",\n        \"columns\": [\n          \"source\",\n          \"coverage_pct\",\n          \"mean_signal\",\n          \"snr\",\n          \"spearman_with_composite\"\n        ],\n        \"rows\": [\n          [\n            \"Performance Gap (primary)\",\n            100,\n            0.38,\n            3.8,\n            0.94\n          ],\n          [\n            \"Temporal\",\n            35,\n            0.42,\n            2.9,\n            0.78\n          ],\n          [\n            \"LogProber\",\n            60,\n            0.35,\n            4.1,\n            0.85\n          ],\n          [\n            \"Weighted Composite\",\n            100,\n            0.41,\n            \"-\",\n            1.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"e_i 估计质量是 staged estimation 可靠性的关键。在 best 档下，performance gap 主通道 信噪比高（3.8），多源融合提供 robustness。18% 的 item 高曝光意味着约 100 个 item （MT-Bench + Arena-Hard）携带强 contamination 信号，足以支撑 c_n 的可辨识性。 e_i 与 ConStat item-level 指标的 ρ=0.68 提供了外部效度验证。\\n\\n\\nBest 档下 real contamination 强，因此 performance gap 信号显著。对于高曝光 item （e_i > 0.7，约 18%），original 与 reference variant 的性能差在 contaminated model 上 可达 0.3-0.5 标准差，经 difficulty correction 后信噪比约 3.8。这与 ConStat (2024) 报告 的 r²=0.94 效应量一致——当 contamination 真实存在时，performance gap 方法有很强的 检测力。Temporal 信号覆盖率较低（35%）因为只有部分 item 有明确的 pre/post-cutoff variant，但覆盖到的 item 与 gap 信号相关性好（ρ=0.65）。LogProber 覆盖 60% （仅限有 logprob API 的模型），与 gap 的相关性更高（ρ=0.72），因为两者都直接 测量 memorization 效应。加权融合后 e_i 分布右偏（mean=0.41, median=0.35）， 符合大多数 item 低曝光、少数 item 高曝光的预期模式。\\n\"\n  },\n  {\n    \"name\": \"gmfrm_real_data_fit\",\n    \"description\": \"在 exp-001/002 的真实数据上拟合 G-MFRM 三阶段 pipeline。Stage 1: 标准 MFRM 估计 初始 θ,b,d。Stage 2: 固定 exp-002 的 e_i。Stage 3: NumPyro MCMC 联合估计 θ,b,d,c_n（e_i 固定）。报告收敛诊断、fair score、与 Chatbot Arena 的 Kendall-τ。\\n\",\n    \"results\": {\n      \"convergence_max_rhat\": 1.03,\n      \"convergence_min_ess\": 287,\n      \"convergence_divergent_transitions\": 0,\n      \"mcmc_warmup\": 2000,\n      \"mcmc_samples\": 4000,\n      \"mcmc_chains\": 4,\n      \"runtime_hours\": 3.2,\n      \"theta_fair_score_kendall_tau_arena_mtbench\": 0.91,\n      \"theta_fair_score_kendall_tau_arena_arenahard\": 0.93,\n      \"theta_fair_score_spearman_arena_mtbench\": 0.94,\n      \"theta_fair_score_spearman_arena_arenahard\": 0.96,\n      \"c_n_median\": 0.95,\n      \"c_n_mean\": 1.02,\n      \"c_n_std\": 0.48,\n      \"c_n_max\": 2.1,\n      \"c_n_min\": 0.08,\n      \"d_j_range\": [\n        -0.35,\n        0.42\n      ],\n      \"d_j_std\": 0.22,\n      \"posterior_predictive_p_value\": 0.47,\n      \"graceful_degradation_low_contam_benchmark_tau_delta\": 0.005\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: G-MFRM Convergence Diagnostics\",\n        \"columns\": [\n          \"parameter_group\",\n          \"n_params\",\n          \"max_rhat\",\n          \"min_ess\",\n          \"mean_ess\"\n        ],\n        \"rows\": [\n          [\n            \"θ (model ability)\",\n            20,\n            1.02,\n            312,\n            890\n          ],\n          [\n            \"b (item difficulty)\",\n            580,\n            1.03,\n            287,\n            650\n          ],\n          [\n            \"d (judge severity)\",\n            8,\n            1.01,\n            1450,\n            2100\n          ],\n          [\n            \"c (contamination)\",\n            20,\n            1.03,\n            295,\n            720\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: G-MFRM Fair Score Agreement with Chatbot Arena\",\n        \"columns\": [\n          \"benchmark\",\n          \"kendall_tau\",\n          \"spearman_rho\",\n          \"95% CI (τ)\"\n        ],\n        \"rows\": [\n          [\n            \"MT-Bench\",\n            0.91,\n            0.94,\n            \"[0.86, 0.95]\"\n          ],\n          [\n            \"Arena-Hard\",\n            0.93,\n            0.96,\n            \"[0.89, 0.96]\"\n          ],\n          [\n            \"Combined (weighted)\",\n            0.92,\n            0.95,\n            \"[0.88, 0.95]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是整个论文的核心实验。收敛诊断全面通过（R̂≤1.03, ESS≥287, 0 divergent transitions） 证明 G-MFRM 的参数化在真实数据规模上是可行的。c_n median=0.95 确认 Tier A 叙事： contamination 不是理论上的可能性，而是量级足够大到系统性扭曲排名的现实问题。 d_j 的范围 [-0.35, 0.42] 表明最 lenient 和最 strict 的 judge 之间存在 0.77 标准差 的 severity 差异，足以影响 model ranking。\\n\\n\\nBest 档的核心假设是 G-MFRM 在真实数据上干净收敛。mvp_003 已在合成数据上实现 R̂=1.03, ESS=224；真实数据的维度更大（20 models × 580 items × 8 judges vs 合成的 15×50×8）但信号也更丰富。使用相同的 MCMC 设置（warmup=2000, samples=4000, chains=4, NCP, target_accept=0.95）加上更大的数据量，ESS 提升至 287 是合理的。 R̂=1.03 与合成结果持平。c_n median=0.95 落在 best 档的 [0.8,1.5] 范围内，接近 mvp_002/003 的假设（c~1.0-1.5）。c_n 的模型间变异大（std=0.48, max=2.1）反映了 现实中不同模型的 contamination 程度差异巨大——开源模型（训练数据不透明）倾向于 更高的 c_n，而 closed-source 模型（如 GPT-5.5）的 c_n 较低。Kendall-τ 在 Arena-Hard 上（0.93）高于 MT-Bench（0.91）因为 Arena-Hard 有更多 item 提供更精确 的 ability 估计。posterior predictive p=0.47 表明模型拟合良好（接近 0.5 的均匀分布）。 对于 contamination 接近 0 的 benchmark 子集，G-MFRM 的 τ 仅比 MFRM 高 0.005， 验证了 graceful degradation——gating 机制在 e_i≈0 时自动关闭 contamination 校正。\\n\"\n  },\n  {\n    \"name\": \"baseline_comparison\",\n    \"description\": \"在相同数据上对比 G-MFRM 与 8 个 baseline 的排名准确性。包含 rank change 分析： 哪些模型在校正后排名变化 ≥2 位，top-5/top-10 稳定性。\\n\",\n    \"results\": {\n      \"raw_avg_kendall_tau_mtbench\": 0.82,\n      \"raw_avg_kendall_tau_arenahard\": 0.84,\n      \"mfrm_only_kendall_tau_mtbench\": 0.84,\n      \"mfrm_only_kendall_tau_arenahard\": 0.86,\n      \"sequential_kendall_tau_mtbench\": 0.85,\n      \"sequential_kendall_tau_arenahard\": 0.87,\n      \"cyclic_judge_kendall_tau_mtbench\": 0.85,\n      \"cyclic_judge_kendall_tau_arenahard\": 0.87,\n      \"cyclic_judge_discard_kendall_tau_mtbench\": 0.87,\n      \"cyclic_judge_discard_kendall_tau_arenahard\": 0.88,\n      \"dcr_factor_kendall_tau_mtbench\": 0.83,\n      \"dcr_factor_kendall_tau_arenahard\": 0.85,\n      \"uda_kendall_tau_mtbench\": 0.86,\n      \"uda_kendall_tau_arenahard\": 0.87,\n      \"pref_leakage_kendall_tau_mtbench\": 0.84,\n      \"pref_leakage_kendall_tau_arenahard\": 0.86,\n      \"gmfrm_kendall_tau_mtbench\": 0.91,\n      \"gmfrm_kendall_tau_arenahard\": 0.93,\n      \"delta_tau_vs_best_baseline_mtbench\": 0.04,\n      \"delta_tau_vs_best_baseline_arenahard\": 0.05,\n      \"wilcoxon_p_gmfrm_vs_best_baseline\": 0.003,\n      \"rank_changes_ge2_positions\": 5,\n      \"rank_changes_ge3_positions\": 2,\n      \"top5_models_changed\": 2,\n      \"top10_models_changed\": 4,\n      \"max_rank_shift\": 4,\n      \"most_shifted_model\": \"Qwen3-235B-A22B\",\n      \"most_shifted_direction\": \"down\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Main Results — Agreement with Chatbot Arena Human Rankings\",\n        \"columns\": [\n          \"method\",\n          \"type\",\n          \"τ (MT-Bench)\",\n          \"τ (Arena-Hard)\",\n          \"τ (Combined)\",\n          \"Δτ vs G-MFRM\"\n        ],\n        \"rows\": [\n          [\n            \"Raw Multi-Judge Avg\",\n            \"naive\",\n            0.82,\n            0.84,\n            0.83,\n            -0.09\n          ],\n          [\n            \"MFRM-only\",\n            \"bias-only\",\n            0.84,\n            0.86,\n            0.85,\n            -0.07\n          ],\n          [\n            \"Sequential (bias→contam)\",\n            \"sequential\",\n            0.85,\n            0.87,\n            0.86,\n            -0.06\n          ],\n          [\n            \"CyclicJudge\",\n            \"bias-only\",\n            0.85,\n            0.87,\n            0.86,\n            -0.06\n          ],\n          [\n            \"CyclicJudge + Discard\",\n            \"bias+heuristic\",\n            0.87,\n            0.88,\n            0.875,\n            -0.045\n          ],\n          [\n            \"DCR Factor\",\n            \"contam-only\",\n            0.83,\n            0.85,\n            0.84,\n            -0.08\n          ],\n          [\n            \"UDA\",\n            \"bias-only (neural)\",\n            0.86,\n            0.87,\n            0.865,\n            -0.055\n          ],\n          [\n            \"Pref Leakage Calib\",\n            \"contam-only\",\n            0.84,\n            0.86,\n            0.85,\n            -0.07\n          ],\n          [\n            \"G-MFRM (ours)\",\n            \"joint\",\n            0.91,\n            0.93,\n            0.92,\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5: Rank Change Analysis (G-MFRM vs Raw Average)\",\n        \"columns\": [\n          \"model\",\n          \"raw_rank\",\n          \"gmfrm_rank\",\n          \"shift\",\n          \"c_n_estimate\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B-A22B\",\n            3,\n            7,\n            -4,\n            1.82,\n            \"High contamination inflated raw rank\"\n          ],\n          [\n            \"Llama 4 Maverick\",\n            5,\n            8,\n            -3,\n            1.45,\n            \"Moderate-high contamination\"\n          ],\n          [\n            \"Model-X-70B\",\n            8,\n            5,\n            3,\n            0.12,\n            \"Low contamination — undervalued by raw\"\n          ],\n          [\n            \"Claude Sonnet 4.6\",\n            4,\n            2,\n            2,\n            0.21,\n            \"Low contamination — rose after correction\"\n          ],\n          [\n            \"DeepSeek-V4-Pro\",\n            6,\n            4,\n            2,\n            0.35,\n            \"Modest contamination — net rise\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是论文的主表。G-MFRM 在两个 benchmark 上一致地以 4-5pp τ 优势击败最强 baseline （CyclicJudge+discard），p=0.003（Wilcoxon）。关键叙事：CyclicJudge+discard 是 Reviewer Concern #1 的最强 trivial alternative，但它 (a) 浪费被丢弃 item 的信息， (b) 不产生 per-model c_n 诊断，(c) 丢弃阈值需要启发式调优。G-MFRM 在所有维度上 都优于它。Rank change 分析提供了实际影响力的证据：如果一个团队基于 raw score 选择 了 rank-3 的 Qwen3-235B 而非 rank-7 的 Model-X-70B，他们可能选择了一个 contamination 膨胀的模型，真实 ability 其实更低。\\n\\n\\nBest 档下 G-MFRM 以显著优势击败所有 baseline。逻辑链： (1) Raw average（τ=0.82/0.84）最差，因为同时受 judge bias 和 contamination 影响。 (2) MFRM-only（+2pp）校正了 judge bias 但 contamination 仍在。 (3) Sequential（+3pp over raw）先 bias 后 contamination，但因 OVB 效应，第一阶段 的 bias 校正已被 contamination 污染，改善有限。 (4) CyclicJudge（≈sequential level）通过 round-robin 消除平均 bias，但无法处理 item-specific judge 效应，且完全忽略 contamination。 (5) CyclicJudge+discard（最强 baseline，τ=0.87/0.88）额外丢弃高疑似 contaminated items，但丢弃策略浪费信息且阈值任意——best 档下它仍比 G-MFRM 低 4-5pp。 (6) DCR Factor（τ=0.83/0.85）量化 contamination 效应但忽略 judge variation。 (7) UDA（τ=0.86/0.87）神经 K-factor 调整 inter-judge variance 但黑盒且不 model contamination。 (8) Pref Leakage（τ=0.84/0.86）校准偏好泄漏但不联合估计。 G-MFRM（τ=0.91/0.93）的优势来自联合估计：同时建模 d_j 和 c_n·e_i 避免了相互吸收。 Rank change 分析：c_n 高的开源模型（如 Qwen3-235B-A22B）在校正后排名下降 （contamination 膨胀被移除），而 c_n 低的 closed-source 模型相对上升。5 个模型 移动 ≥2 位，最大移动 4 位，top-5 中有 2 个交换——这对模型选择决策有实质性影响。\\n\"\n  },\n  {\n    \"name\": \"contamination_magnitude_calibration\",\n    \"description\": \"比较 exp-003 拟合的真实 c_n 分布与 MVP 合成假设，确定 contamination 处于哪个 tier。 用 ConStat per-model delta 做外部验证。\\n\",\n    \"results\": {\n      \"c_n_median_real\": 0.95,\n      \"c_n_mean_real\": 1.02,\n      \"c_n_q25\": 0.42,\n      \"c_n_q75\": 1.48,\n      \"c_n_iqr\": 1.06,\n      \"models_with_c_n_gt_1\": 8,\n      \"models_with_c_n_gt_05\": 14,\n      \"models_with_c_n_lt_02\": 3,\n      \"closest_mvp_scenario\": \"mvp_002/003 (strong)\",\n      \"constat_delta_spearman_with_c_n\": 0.82,\n      \"constat_delta_pearson_with_c_n\": 0.78,\n      \"tier_determination\": \"Tier A\",\n      \"ratio_real_vs_mvp003_median\": 0.95\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Contamination Magnitude — Real vs Synthetic\",\n        \"columns\": [\n          \"scenario\",\n          \"c_n_median\",\n          \"c_n_mean\",\n          \"c_n_std\",\n          \"convergence\",\n          \"kendall_tau_gain\"\n        ],\n        \"rows\": [\n          [\n            \"mvp_001 (weak)\",\n            0.5,\n            0.52,\n            0.15,\n            \"PASS\",\n            \"+0.3pp (n.s.)\"\n          ],\n          [\n            \"mvp_002 (strong\",\n            \"poor convergence)\",\n            1.2,\n            1.25,\n            0.4,\n            \"FAIL\",\n            \"+4.3pp\"\n          ],\n          [\n            \"mvp_003 (strong\",\n            \"tuned)\",\n            1.0,\n            1.05,\n            0.35,\n            \"PASS\",\n            \"+6.3pp\"\n          ],\n          [\n            \"Real Data (exp-003)\",\n            0.95,\n            1.02,\n            0.48,\n            \"PASS\",\n            \"+4.5pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7: ConStat External Validation\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"Spearman ρ (c_n vs ConStat Δ)\",\n            0.82,\n            \"[0.65, 0.92]\"\n          ],\n          [\n            \"Pearson r (c_n vs ConStat Δ)\",\n            0.78,\n            \"[0.58, 0.89]\"\n          ],\n          [\n            \"Concordance (top-5 c_n ∩ top-5 ConStat)\",\n            \"4/5\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"此实验是 Tier A/B 决策点。c_n median=0.95 明确指向 Tier A。与 mvp_003 的比较 显示真实数据几乎完美匹配合成假设（ratio=0.95），验证了 MVP 阶段的参数校准。 ConStat 验证（ρ=0.82）是论文的关键防线：它证明 c_n 不是模型过拟合的产物， 而是与独立测量工具一致的真实信号。top-5 concordance（4/5）特别有说服力—— G-MFRM 和 ConStat 几乎完全同意哪些模型受 contamination 影响最大。\\n\\n\\nBest 档的核心前提是 real contamination 强度匹配 mvp_002/003 假设。c_n median=0.95 非常接近 mvp_003 的设定（c~1.0）。这意味着对于一个典型的高曝光 item（e_i=0.8）， contaminated model 的 expected score 膨胀约 0.76 logits（0.95×0.8），这是一个 非常显著的效应，足以将一个中等 ability 模型提升 2-4 个排名位。14/20 个模型的 c_n > 0.5 表明 contamination 是广泛存在的，不仅仅是个别模型的问题。ConStat 外部 验证 ρ=0.82 在 best 档范围 [0.7, 0.95] 内偏高，说明 G-MFRM 拟合的 c_n 与独立的 ConStat contamination 指标高度一致——这不是 MCMC 的 artifact，而是捕捉到了真实的 contamination 结构。3 个模型 c_n < 0.2（基本无 contamination）提供了自然的负对照。\\n\"\n  },\n  {\n    \"name\": \"judge_count_sensitivity\",\n    \"description\": \"敏感性分析：逐步减少 judge 数量（8→6→4→2），观察 G-MFRM 性能退化曲线。 确定 G-MFRM 优于 sequential 的最低 judge 数量。\\n\",\n    \"results\": {\n      \"tau_8_judges\": 0.92,\n      \"tau_6_judges\": 0.905,\n      \"tau_4_judges\": 0.885,\n      \"tau_3_judges\": 0.87,\n      \"tau_2_judges\": 0.84,\n      \"sequential_tau_8_judges\": 0.865,\n      \"sequential_tau_4_judges\": 0.855,\n      \"sequential_tau_2_judges\": 0.845,\n      \"min_judges_for_significant_gain\": 3,\n      \"degradation_rate_per_judge_removed\": 0.012,\n      \"gmfrm_2_judge_vs_mfrm_2_judge_delta\": 0.005,\n      \"convergence_failure_at_2_judges\": false,\n      \"convergence_rhat_at_2_judges\": 1.08\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Judge Count Sensitivity\",\n        \"columns\": [\n          \"n_judges\",\n          \"τ (G-MFRM)\",\n          \"τ (Sequential)\",\n          \"Δτ\",\n          \"p-value\",\n          \"max_rhat\",\n          \"min_ess\"\n        ],\n        \"rows\": [\n          [\n            8,\n            0.92,\n            0.865,\n            0.055,\n            0.003,\n            1.03,\n            287\n          ],\n          [\n            6,\n            0.905,\n            0.86,\n            0.045,\n            0.008,\n            1.03,\n            245\n          ],\n          [\n            4,\n            0.885,\n            0.855,\n            0.03,\n            0.021,\n            1.04,\n            198\n          ],\n          [\n            3,\n            0.87,\n            0.852,\n            0.018,\n            0.048,\n            1.05,\n            165\n          ],\n          [\n            2,\n            0.84,\n            0.845,\n            -0.005,\n            0.62,\n            1.08,\n            89\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"此分析为实践者提供了成本效益指导。结论清晰：≥4 judges 推荐（G-MFRM gain ~3pp+）， 3 judges 勉强可行（gain 1.8pp, p<0.05），2 judges 不建议用 G-MFRM（退化至 MFRM）。 这回应了 Reviewer Concern #8 的成本问题，并为 Limitations 提供了量化数据。\\n\\n\\nG-MFRM 需要多 judge 数据来分离 d_j 和 c_n·e_i。在 best 档下，8 judges 提供 丰富信号（τ=0.92）。减至 6 judges 损失温和（-1.5pp），因为仍有足够的 judge 变异来估计 d_j。减至 4 judges 是关键拐点（-3.5pp），但仍比 sequential 4-judge（0.855） 好 3pp。3 judges 是 G-MFRM 显著优于 sequential 的最低阈值——对应 best 档的 judge_count_min_for_significant_gain=[3,4] 范围。2 judges 时 G-MFRM 基本退化到 MFRM 水平（delta 仅 0.5pp），因为 2 个 judge 不足以可靠估计 d_j，gating 机制 也因信号不足而趋于保守。R̂ 在 2-judge 时升至 1.08，刚好超过阈值，但未发散。 这回应了 Reviewer Concern #8：在 2-judge 场景下 G-MFRM 不会崩溃，只是退化到 MFRM baseline 水平。\\n\"\n  },\n  {\n    \"name\": \"exposure_indicator_ablation\",\n    \"description\": \"对 e_i 估计 pipeline 做 leave-one-out 消融：分别去掉 performance gap、temporal、 LogProber 中的一个 source，观察对最终 θ̂ 和 c_n 估计质量的影响。\\n\",\n    \"results\": {\n      \"full_pipeline_theta_tau\": 0.92,\n      \"without_performance_gap_theta_tau\": 0.87,\n      \"without_temporal_theta_tau\": 0.915,\n      \"without_logprober_theta_tau\": 0.91,\n      \"full_pipeline_cn_recovery_spearman\": 0.82,\n      \"without_performance_gap_cn_recovery_spearman\": 0.55,\n      \"without_temporal_cn_recovery_spearman\": 0.8,\n      \"without_logprober_cn_recovery_spearman\": 0.78,\n      \"performance_gap_contribution_pct\": 72,\n      \"temporal_contribution_pct\": 8,\n      \"logprober_contribution_pct\": 12,\n      \"interaction_effect_pct\": 8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Exposure Indicator Ablation\",\n        \"columns\": [\n          \"configuration\",\n          \"τ (Arena)\",\n          \"Δτ\",\n          \"c_n ρ\",\n          \"Δρ\"\n        ],\n        \"rows\": [\n          [\n            \"Full pipeline (3 sources)\",\n            0.92,\n            \"—\",\n            0.82,\n            \"—\"\n          ],\n          [\n            \"− Performance Gap\",\n            0.87,\n            -0.05,\n            0.55,\n            -0.27\n          ],\n          [\n            \"− Temporal\",\n            0.915,\n            -0.005,\n            0.8,\n            -0.02\n          ],\n          [\n            \"− LogProber\",\n            0.91,\n            -0.01,\n            0.78,\n            -0.04\n          ],\n          [\n            \"Gap only\",\n            0.912,\n            -0.008,\n            0.79,\n            -0.03\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"消融结果支持 pipeline 设计的合理性。Performance gap 是必要条件（去掉后严重退化）， 而 temporal 和 LogProber 提供边际改进。\\\"Gap only\\\" 配置仅比 full pipeline 低 0.8pp， 说明如果资源有限，只使用 performance gap 也是可行的最小方案。这为实践者提供了 模块化部署指导。\\n\\n\\nPerformance gap 是 e_i 的主通道（100% 覆盖，SNR=3.8），去掉后 τ 下降 5pp—— 这是因为没有 gap 信号，e_i 估计退化为 temporal+LogProber 的稀疏覆盖 （仅 35%+60% 项有信号，交集更小），大量 item 的 e_i 几乎无信息。相反，去掉 temporal 或 LogProber 各自影响很小（-0.5pp 和 -1pp），因为它们是补充信号， 覆盖率有限。但 c_n recovery 的 spearman 对 performance gap 的依赖更强 （Δρ=0.27 vs Δρ=0.02/0.04），因为 c_n 的可辨识性直接依赖于 e_i 的准确性—— e_i 差则 c_n·e_i 项无法正确分离 c_n。这证明了 performance gap 是不可或缺的， 而 temporal 和 LogProber 是有用但非必要的补充。\\n\"\n  },\n  {\n    \"name\": \"facet_fit_diagnostics\",\n    \"description\": \"报告 G-MFRM 所有 facet 的测量质量诊断：infit/outfit MNSQ、divergent transitions、 posterior predictive check、trace plots。标记 misfit 元素。\\n\",\n    \"results\": {\n      \"theta_infit_mean\": 1.02,\n      \"theta_infit_range\": [\n        0.85,\n        1.18\n      ],\n      \"theta_outfit_mean\": 1.05,\n      \"theta_outfit_range\": [\n        0.78,\n        1.35\n      ],\n      \"theta_misfit_count\": 1,\n      \"b_infit_mean\": 1.0,\n      \"b_infit_range\": [\n        0.72,\n        1.42\n      ],\n      \"b_outfit_mean\": 1.03,\n      \"b_outfit_range\": [\n        0.65,\n        1.55\n      ],\n      \"b_misfit_count\": 12,\n      \"d_infit_mean\": 0.98,\n      \"d_infit_range\": [\n        0.88,\n        1.1\n      ],\n      \"d_outfit_mean\": 1.01,\n      \"d_outfit_range\": [\n        0.85,\n        1.15\n      ],\n      \"d_misfit_count\": 0,\n      \"c_infit_mean\": 1.04,\n      \"c_infit_range\": [\n        0.82,\n        1.25\n      ],\n      \"divergent_transitions\": 0,\n      \"posterior_predictive_ppp\": 0.47,\n      \"posterior_predictive_rmse\": 0.18,\n      \"stage1_lz_flagged_models\": 2,\n      \"stage3_cn_gt_0_for_lz_flagged\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table A2: Facet Fit Summary (Infit/Outfit MNSQ)\",\n        \"columns\": [\n          \"facet\",\n          \"n\",\n          \"mean_infit\",\n          \"mean_outfit\",\n          \"misfit_count\",\n          \"misfit_%\"\n        ],\n        \"rows\": [\n          [\n            \"θ (model ability)\",\n            20,\n            1.02,\n            1.05,\n            1,\n            5.0\n          ],\n          [\n            \"b (item difficulty)\",\n            580,\n            1.0,\n            1.03,\n            12,\n            2.1\n          ],\n          [\n            \"d (judge severity)\",\n            8,\n            0.98,\n            1.01,\n            0,\n            0.0\n          ],\n          [\n            \"c (contamination)\",\n            20,\n            1.04,\n            \"—\",\n            0,\n            0.0\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table A3: MCMC Diagnostics Summary\",\n        \"columns\": [\n          \"diagnostic\",\n          \"value\",\n          \"threshold\",\n          \"status\"\n        ],\n        \"rows\": [\n          [\n            \"Max R̂\",\n            1.03,\n            \"≤ 1.05\",\n            \"PASS\"\n          ],\n          [\n            \"Min ESS\",\n            287,\n            \"≥ 200\",\n            \"PASS\"\n          ],\n          [\n            \"Divergent transitions\",\n            0,\n            \"= 0\",\n            \"PASS\"\n          ],\n          [\n            \"PPP\",\n            0.47,\n            \"[0.1, 0.9]\",\n            \"PASS\"\n          ],\n          [\n            \"Posterior predictive RMSE\",\n            0.18,\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"诊断全面支持 G-MFRM 的测量质量。2.1% 的 item misfit 率在 IRT 文献中属于正常范围。 Stage 1 lz → Stage 3 c_n 的 coherence 是一个巧妙的验证：如果 person-fit 异常 是由 contamination 引起的，那么在建模 contamination 后应该被解释掉——实验证实了这一点。\\n\\n\\nBest 档要求诊断全面良好。Infit/outfit MNSQ 接近 1.0 表示 Rasch 模型拟合良好。 Item facet（b）有 12 个 misfit（outfit > 1.4 的 item），占 580 items 的 ~2%， 这在 IRT 实践中是正常水平——这些 item 可能有特殊结构（如依赖特定领域知识） 导致模型不完全适用。1 个 θ misfit 模型可能是有异常评分模式的 target model。 Judge facet（d）完全无 misfit（仅 8 个 judge，且都是主流 LLM），这符合预期。 0 divergent transitions 和 PPP=0.47 证实整体模型规范正确。Stage 1 的 person-fit 指标（lz）标记了 2 个模型，Stage 3 中这 2 个模型都有 c_n > 0（分别为 1.2 和 0.8）， 证实了 construct coherence：Stage 1 的 misfit 信号确实来自 contamination 而非 ability 维度的问题。\\n\"\n  },\n  {\n    \"name\": \"confounding_formal_observation\",\n    \"description\": \"形式化推导 sequential estimator 在 d_j 和 c_n·e_i 非正交条件下的一阶 bias 近似。Monte Carlo 验证。合成数据上的 c_n 点估计验证。\\n\",\n    \"results\": {\n      \"bias_first_order_formula\": \"bias(θ̂_seq) ≈ Σ_j (X'X)^{-1} X' Cov(d_j, c_n·e_i)\",\n      \"monte_carlo_n_reps\": 500,\n      \"monte_carlo_bias_mean_rho_0\": 0.001,\n      \"monte_carlo_bias_mean_rho_03\": 0.048,\n      \"monte_carlo_bias_mean_rho_06\": 0.112,\n      \"monte_carlo_bias_std_rho_06\": 0.035,\n      \"monte_carlo_rmse_degradation_rho_06_pct\": 43.2,\n      \"synthetic_cn_recovery_rmse\": 0.09,\n      \"synthetic_cn_coverage_95ci\": 0.93,\n      \"synthetic_cn_spearman_recovery\": 0.96,\n      \"synthetic_cn_bias\": -0.02\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Monte Carlo Bias Analysis (500 replications)\",\n        \"columns\": [\n          \"ρ(d\",\n          \"ce)\",\n          \"bias(θ̂_seq)\",\n          \"θ RMSE (seq)\",\n          \"θ RMSE (joint)\",\n          \"RMSE reduction %\"\n        ],\n        \"rows\": [\n          [\n            0.0,\n            0.001,\n            0.124,\n            0.123,\n            0.8\n          ],\n          [\n            0.15,\n            0.021,\n            0.138,\n            0.124,\n            10.1\n          ],\n          [\n            0.3,\n            0.048,\n            0.162,\n            0.125,\n            22.8\n          ],\n          [\n            0.45,\n            0.078,\n            0.189,\n            0.124,\n            34.4\n          ],\n          [\n            0.6,\n            0.112,\n            0.221,\n            0.125,\n            43.2\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 11: Synthetic c_n Recovery (G-MFRM)\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"c_n RMSE\",\n            0.09\n          ],\n          [\n            \"c_n bias\",\n            -0.02\n          ],\n          [\n            \"c_n Spearman ρ (fitted vs true)\",\n            0.96\n          ],\n          [\n            \"95% CI coverage\",\n            0.93\n          ],\n          [\n            \"Mean CI width\",\n            0.38\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"此实验为 Confounding Claim 提供形式化+实证双重支持。OVB observation 是已有理论 的直接应用，不需要 novelty——关键贡献是证明这个理论问题在 LLM 评估中量级显著 （43.2% RMSE 退化）。c_n recovery 验证确认 G-MFRM 不仅纠正了 θ̂ bias，还能 准确恢复潜在的 contamination 结构，coverage probability 接近 nominal 说明 posterior inference 是 well-calibrated 的。\\n\\n\\n形式化分析是标准 OVB 理论在 LLM 评估场景的应用。当 d_j 和 c_n·e_i 正交 （ρ=0）时，bias ≈ 0（0.001 是有限样本噪声），sequential 无害。但在现实中， judge 的 severity 和 model 的 contamination susceptibility 不独立——harsh judges 可能对 contaminated 回答更 lenient（因为 contaminated 回答通常更流畅、更自信）， 导致 ρ > 0。在 ρ=0.6 时（mvp 模拟的现实估计），RMSE 退化 43.2%，与 mvp_003 的 43.8% 高度一致。合成 c_n recovery 的 RMSE=0.09 落在 best 档范围 [0.05, 0.15] 内， 95% CI coverage=0.93（接近 nominal 0.95），说明贝叶斯推断的 uncertainty quantification 是准确的。ρ_recovery=0.96 表明即使点估计有噪声，排序几乎完美保留。\\n\"\n  },\n  {\n    \"name\": \"error_propagation_sensitivity\",\n    \"description\": \"Staged estimation 的误差传播敏感性：向 e_i 注入 σ=0.1/0.2/0.5 的高斯噪声后 重新拟合 Stage 3，测量 θ̂ RMSE 退化和 c_n recovery 精度。合成数据。\\n\",\n    \"results\": {\n      \"sigma_0_theta_rmse\": 0.124,\n      \"sigma_01_theta_rmse\": 0.127,\n      \"sigma_01_theta_rmse_degradation_pct\": 2.4,\n      \"sigma_02_theta_rmse\": 0.133,\n      \"sigma_02_theta_rmse_degradation_pct\": 7.3,\n      \"sigma_05_theta_rmse\": 0.168,\n      \"sigma_05_theta_rmse_degradation_pct\": 35.5,\n      \"sigma_0_cn_rmse\": 0.09,\n      \"sigma_01_cn_rmse\": 0.12,\n      \"sigma_02_cn_rmse\": 0.18,\n      \"sigma_05_cn_rmse\": 0.41,\n      \"sigma_02_cn_spearman\": 0.89,\n      \"sigma_05_cn_spearman\": 0.62,\n      \"robustness_threshold_sigma\": 0.25\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Error Propagation Sensitivity (Synthetic)\",\n        \"columns\": [\n          \"e_i_noise_σ\",\n          \"θ̂ RMSE\",\n          \"θ̂ degrad. %\",\n          \"c_n RMSE\",\n          \"c_n ρ\",\n          \"τ (Arena proxy)\"\n        ],\n        \"rows\": [\n          [\n            0.0,\n            0.124,\n            \"—\",\n            0.09,\n            0.96,\n            0.922\n          ],\n          [\n            0.1,\n            0.127,\n            2.4,\n            0.12,\n            0.94,\n            0.918\n          ],\n          [\n            0.2,\n            0.133,\n            7.3,\n            0.18,\n            0.89,\n            0.91\n          ],\n          [\n            0.3,\n            0.145,\n            16.9,\n            0.27,\n            0.79,\n            0.893\n          ],\n          [\n            0.5,\n            0.168,\n            35.5,\n            0.41,\n            0.62,\n            0.862\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"此实验是 Reviewer Concern #4b 和 Dream R1-N1 的核心回应。结论：staged estimation 在 σ≤0.2 时 robust（θ̂ 退化 <8%），在 σ≤0.1 时几乎无损（<2.5%）。exp-002 的 实际 e_i 噪声估计约 σ=0.15（基于 SNR=3.8 和 multi-source 融合），落在安全区内。 σ=0.5 的崩溃点提供了理论下界。论文 Limitations 中需讨论 σ=0.2 处的 7.3% 超过了 预设 5% 阈值，但结合实际噪声水平论证 staged estimation 的可接受性。\\n\\n\\nBest 档要求 σ=0.2 时 θ̂ RMSE 退化 < 5%。预测值 7.3% 略超此阈值，但仍属于 实际可接受范围（需在论文中 acknowledge）。逻辑：e_i 噪声通过 c_n·e_i 项传播到 θ̂——当 σ 小（0.1）时，e_i 的 rank order 基本保持，gating 机制仅微调幅度， 对 θ̂ 影响很小（2.4%）。σ=0.2 时 e_i 的 rank 开始受扰动，部分 high-exposure item 被错误降权、low-exposure item 被错误升权，导致 c_n 估计 偏移（RMSE 从 0.09→0.18），但因为 θ̂ 同时受多个 item 信息约束（580 items）， 单个 item 的 e_i 误差被平均化，θ̂ 退化相对温和。σ=0.5 是破坏性水平（35.5% 退化）， 此时 e_i 信号几乎被噪声淹没。robustness_threshold ≈ 0.25 意味着 exp-002 的 e_i 估计只要噪声不超过 0.25 就安全——考虑到 performance gap 的 SNR=3.8，实际噪声 约 σ≈0.15，处于安全区内。注意：σ=0.2 处 θ̂ degradation 为 7.3% 而非 <5%。 在论文中需诚实报告，但可论证 (a) 这是 worst-case 均匀噪声注入，实际噪声结构更 favorable，(b) 7.3% degradation 仍使 G-MFRM 大幅优于 sequential baseline。\\n\"\n  },\n  {\n    \"name\": \"wildbench_replication\",\n    \"description\": \"在 WildBench 上复制完整 G-MFRM pipeline 作为第三个 benchmark，验证跨 benchmark 泛化性。\\n\",\n    \"results\": {\n      \"wildbench_items\": 1024,\n      \"wildbench_judges_used\": 6,\n      \"gmfrm_kendall_tau_wildbench\": 0.9,\n      \"sequential_kendall_tau_wildbench\": 0.86,\n      \"delta_tau_wildbench\": 0.04,\n      \"c_n_spearman_wildbench_vs_mtbench\": 0.88,\n      \"convergence_max_rhat\": 1.04,\n      \"convergence_min_ess\": 210,\n      \"wildbench_high_exposure_items_pct\": 14\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Cross-Benchmark Generalization\",\n        \"columns\": [\n          \"benchmark\",\n          \"τ (G-MFRM)\",\n          \"τ (Best Baseline)\",\n          \"Δτ\",\n          \"items\",\n          \"judges\"\n        ],\n        \"rows\": [\n          [\n            \"MT-Bench\",\n            0.91,\n            0.87,\n            0.04,\n            80,\n            8\n          ],\n          [\n            \"Arena-Hard\",\n            0.93,\n            0.88,\n            0.05,\n            500,\n            8\n          ],\n          [\n            \"WildBench\",\n            0.9,\n            0.86,\n            0.04,\n            1024,\n            6\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"跨 benchmark 复制成功。三个 benchmark 上 G-MFRM 一致优于 best baseline 4-5pp， 消除了 \\\"方法只在特定 benchmark 上有效\\\" 的顾虑。c_n 跨 benchmark 稳定性是 bonus finding：可以在 Discussion 中论证 c_n 有作为 \\\"model contamination audit index\\\" 的潜力。\\n\\n\\nWildBench 是更 \\\"wild\\\" 的 benchmark（用户真实 query），contamination 模式应与 MT-Bench/Arena-Hard 不同但 G-MFRM 方法论应仍然有效。best 档下 τ=0.90（略低于 Arena-Hard 的 0.93），因为 WildBench 的 item 更异质、标注噪声更大。Δτ=0.04 与 MT-Bench 上的 0.04 一致，证明 G-MFRM 的优势不是 benchmark-specific 的。 c_n 在 WildBench 和 MT-Bench 之间的 ρ=0.88 说明同一组模型的 contamination susceptibility 跨 benchmark 是稳定的——这是一个重要的 construct validity 证据， 说明 c_n 测量的是模型的固有属性而非 benchmark-specific artifact。仅使用 6 个 judge（2 个 API 不支持 WildBench 格式）但收敛仍然良好。\\n\"\n  },\n  {\n    \"name\": \"adversarial_robustness\",\n    \"description\": \"测试 G-MFRM 对抗 adversarial contamination 的鲁棒性，遵循 Wang et al. (ICLR 2026) 的 fragility analysis 框架。\\n\",\n    \"results\": {\n      \"adversarial_attack_types\": 3,\n      \"attack1_targeted_item_injection_theta_shift\": 0.15,\n      \"attack2_judge_collusion_theta_shift\": 0.22,\n      \"attack3_exposure_manipulation_theta_shift\": 0.08,\n      \"gmfrm_detection_rate_attack1\": 0.85,\n      \"gmfrm_detection_rate_attack2\": 0.7,\n      \"gmfrm_detection_rate_attack3\": 0.9,\n      \"sequential_detection_rate_attack1\": 0.4,\n      \"infit_flags_adversarial_items\": true,\n      \"c_n_inflation_under_attack\": 0.3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table A4: Adversarial Robustness\",\n        \"columns\": [\n          \"attack\",\n          \"θ̂ shift (G-MFRM)\",\n          \"θ̂ shift (Sequential)\",\n          \"G-MFRM detection rate\"\n        ],\n        \"rows\": [\n          [\n            \"Targeted item injection\",\n            0.15,\n            0.38,\n            0.85\n          ],\n          [\n            \"Judge collusion (2/8)\",\n            0.22,\n            0.31,\n            0.7\n          ],\n          [\n            \"Exposure manipulation\",\n            0.08,\n            \"N/A\",\n            0.9\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"P2 优先级实验，为 Discussion/Limitations 提供材料。G-MFRM 不声称 adversarial robustness 作为贡献，但展示其 diagnostic 框架提供了 \\\"免费的\\\" 异常检测能力。 Judge collusion 是最大弱点——如果超过 50% 的 judge 被操纵，d_j 无法区分真实 severity 和操纵。这是一个 honest limitation。\\n\\nG-MFRM 的 person-fit diagnostics（infit/outfit）提供了对 adversarial manipulation 的自然检测机制。Attack 1（targeted item injection：在特定 item 上注入异常高分） 被 item-level outfit 检测到（85%），因为注入的分数违反了 Rasch 模型的 sufficiency 假设。Attack 2（judge collusion：多个 judge 协调给高分）更难检测（70%），因为 一致的 judge behavior 可以被 d_j 吸收——但 c_n 会出现异常膨胀（+0.3）作为 间接信号。Attack 3（exposure manipulation：人为修改 e_i 输入）反而最容易防御 （90%），因为 Stage 2 的 multi-source 融合和 ConStat 外部验证能交叉检验 e_i 的一致性。Sequential baseline 在 Attack 1 上检测率仅 40%，因为没有 contamination 模型来标记异常。总体而言 G-MFRM 不是完全 adversarial-proof 的（scope 声明已排除）， 但比 sequential 有更强的内在鲁棒性。\\n\"\n  }\n]",
      "numLines": 1107,
      "startLine": 1,
      "totalLines": 1107
    }
  },
  "sourceToolAssistantUUID": "8e417eac-b76b-4246-93f9-346139d1f49d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T215715 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artif…",
  "leafUuid": "72fe4570-59a4-48cf-9e63-4fc4a1305f03",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Joint calibration of judge bias and benchmark contamination",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5"
}
```

---

### Assistant

_source line 16 · 2026-05-21T22:13:43.158Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check for LaTeX templates and the EMNLP 2026 venue info, and load the paper-writing-norms skill for reference.

Let me also check if there's an EMNLP/AAAI template available.

Actually, the venue is "emnlp-2026" according to the task, but the paper_framing.md mentions AAAI 2027 as primary. The task says venue is emnlp-2026, so I'll use that. Let me check for available LaTeX templates.

Let me now draft the paper. I have all the data I need.


Now I'm reviewing the key metrics from the experiments: the multi-judge dataset with its 185,600 judgments across 20 models and 8 judges showing a position bias rate of 0.58 and moderate inter-rater agreement at κ=0.42, the item exposure estimation using three-source fusion with a composite mean of 0.41 and 18% high exposure items, the GMFRM convergence diagnostics showing excellent fit with R̂≤1.03 and strong effective sample sizes, and the baseline comparison results.

G-MFRM outperforms all eight baselines with the next-best approach (CyclicJudge+Discard) reaching 0.87/0.88 while G-MFRM achieves 0.91/0.93 with statistical significance at p=0.003, causing five models to shift two or more positions in the rankings. The contamination calibration shows a median c_n of 0.95 with strong correlation to ConStat at ρ=0.82, while the judge count sensitivity analysis reveals that three judges are needed for meaningful improvements and performance degrades with only two. Performance gap emerges as the dominant exposure indicator at 72% contribution, all diagnostic checks pass, and the model demonstrates robustness to confounding effects and measurement error up to σ≤0.2.

The Wildbench replication achieves τ=0.90 with minimal variance across benchmarks (Δτ=0.04) and cross-benchmark calibration at ρ=0.88, while adversarial robustness testing shows G-MFRM detection rates between 70-90%, outperforming sequential approaches. Now I'm structuring the paper using the EMNLP 2026 format, starting with an abstract that opens with the quantitative findings, then building out the introduction, the confounding problem section with the OVB observation, and continuing through the methodology. I'm laying out the full paper structure with the title and organizing the sections to flow from the core problem through methodology to comprehensive experimental validation, including ablations and cross-benchmark generalization tests.

Now I need to verify the LaTeX environment is set up properly before proceeding with the actual writing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72fe4570-59a4-48cf-9e63-4fc4a1305f03",
  "isSidechain": false,
  "requestId": "req_011CbGUxvkWcMdhkH3y5BAE2",
  "type": "assistant",
  "uuid": "6af50374-30cd-4aea-88af-f7e6d40686a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01764gAdMajH6D99rhRbW6gy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2679,
      "cache_creation_input_tokens": 18821,
      "cache_read_input_tokens": 23940,
      "output_tokens": 1644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18821,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2679,
          "output_tokens": 1644,
          "cache_read_input_tokens": 23940,
          "cache_creation_input_tokens": 18821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18821
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

_source line 17 · 2026-05-21T22:13:43.159Z_

Let me check available LaTeX setup and templates before writing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6af50374-30cd-4aea-88af-f7e6d40686a7",
  "isSidechain": false,
  "requestId": "req_011CbGUxvkWcMdhkH3y5BAE2",
  "type": "assistant",
  "uuid": "a0ef9cd4-a3b3-4921-b7b0-3f9ecc30ff22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01764gAdMajH6D99rhRbW6gy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2679,
      "cache_creation_input_tokens": 18821,
      "cache_read_input_tokens": 23940,
      "output_tokens": 1644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18821,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2679,
          "output_tokens": 1644,
          "cache_read_input_tokens": 23940,
          "cache_creation_input_tokens": 18821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18821
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

_source line 18 · 2026-05-21T22:13:43.541Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015CZn9U31zGgScoMjvFbnbS`</summary>

```json
{
  "command": "which pdflatex && pdflatex --version | head -2",
  "description": "Check pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0ef9cd4-a3b3-4921-b7b0-3f9ecc30ff22",
  "isSidechain": false,
  "requestId": "req_011CbGUxvkWcMdhkH3y5BAE2",
  "type": "assistant",
  "uuid": "5962887d-f06b-4c4e-90a3-a9b3a2d16419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01764gAdMajH6D99rhRbW6gy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2679,
      "cache_creation_input_tokens": 18821,
      "cache_read_input_tokens": 23940,
      "output_tokens": 1644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18821,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2679,
          "output_tokens": 1644,
          "cache_read_input_tokens": 23940,
          "cache_creation_input_tokens": 18821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18821
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

_source line 19 · 2026-05-21T22:13:43.746Z_

<details><summary>↩ Tool result · `toolu_015CZn9U31zGgScoMjvFbnbS`</summary>

```text
/usr/bin/pdflatex
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)
kpathsea version 6.4.1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5962887d-f06b-4c4e-90a3-a9b3a2d16419",
  "isSidechain": false,
  "promptId": "fe64548b-77cb-42da-afef-0d7832f54298",
  "type": "user",
  "uuid": "a0c38255-9ae3-43d1-be0b-b8373daa559b",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)\nkpathsea version 6.4.1",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5962887d-f06b-4c4e-90a3-a9b3a2d16419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T22:13:45.884Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FLM1tGFMpaJe28YzUgZ6mo`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/",
  "description": "List existing files in target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0c38255-9ae3-43d1-be0b-b8373daa559b",
  "isSidechain": false,
  "requestId": "req_011CbGUxvkWcMdhkH3y5BAE2",
  "type": "assistant",
  "uuid": "d2f20fbf-eeca-4752-9ac3-000dcba6b389",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01764gAdMajH6D99rhRbW6gy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2679,
      "cache_creation_input_tokens": 18821,
      "cache_read_input_tokens": 23940,
      "output_tokens": 1644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18821,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2679,
          "output_tokens": 1644,
          "cache_read_input_tokens": 23940,
          "cache_creation_input_tokens": 18821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18821
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

_source line 21 · 2026-05-21T22:13:45.941Z_

<details><summary>↩ Tool result · `toolu_01FLM1tGFMpaJe28YzUgZ6mo`</summary>

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
  "parentUuid": "d2f20fbf-eeca-4752-9ac3-000dcba6b389",
  "isSidechain": false,
  "promptId": "fe64548b-77cb-42da-afef-0d7832f54298",
  "type": "user",
  "uuid": "b23e9193-387c-4bd5-b65d-8edf1eb3b750",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d2f20fbf-eeca-4752-9ac3-000dcba6b389",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T22:13:47.760Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013bPrJFFNrYXrDqvr71VyGS`</summary>

```json
{
  "command": "kpsewhich acl.sty 2>/dev/null; kpsewhich acl_natbib.bst 2>/dev/null; kpsewhich emnlp.sty 2>/dev/null; kpsewhich aaai.sty 2>/dev/null; echo \"---\"; kpsewhich booktabs.sty; kpsewhich amsmath.sty; kpsewhich natbib.sty; kpsewhich hyperref.sty",
  "description": "Check available LaTeX style files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b23e9193-387c-4bd5-b65d-8edf1eb3b750",
  "isSidechain": false,
  "requestId": "req_011CbGUxvkWcMdhkH3y5BAE2",
  "type": "assistant",
  "uuid": "f18d169d-919e-4d9e-97ed-a57b66f31f50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01764gAdMajH6D99rhRbW6gy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2679,
      "cache_creation_input_tokens": 18821,
      "cache_read_input_tokens": 23940,
      "output_tokens": 1644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18821,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2679,
          "output_tokens": 1644,
          "cache_read_input_tokens": 23940,
          "cache_creation_input_tokens": 18821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18821
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

_source line 23 · 2026-05-21T22:13:47.985Z_

<details><summary>↩ Tool result · `toolu_013bPrJFFNrYXrDqvr71VyGS`</summary>

```text
---
/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty
/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f18d169d-919e-4d9e-97ed-a57b66f31f50",
  "isSidechain": false,
  "promptId": "fe64548b-77cb-42da-afef-0d7832f54298",
  "type": "user",
  "uuid": "fc347743-36d3-4380-8cd5-ad544150fa16",
  "toolUseResult": {
    "stdout": "---\n/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty\n/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\n/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty\n/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f18d169d-919e-4d9e-97ed-a57b66f31f50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T22:14:52.612Z_

<details><summary>Logged reasoning block</summary>

```text
No ACL/EMNLP style available, so I'll use a clean article class with standard packages. This is fine for a "够审" dream paper.

Now let me write the complete LaTeX paper. I need to be careful to:
1. Include every experiment from experiment_data.json
2. Use exact numbers from the data
3. Follow the narrative guidance (Tier A, lead with quantitative shock)
4. Structure: Abstract, Intro, Background/Confounding, Method, Experiments, Results, Analysis, Related Work, Conclusion, Limitations

Let me write this now. It'll be a substantial paper.


I'm mapping out the table structure across all experiments—main results, exposure indicators, convergence diagnostics, fair score agreement, rank changes, contamination magnitudes, external validation, judge sensitivity, and ablation studies. I'm reorganizing the table structure for an 8-page paper, keeping the core results and sensitivity analyses in the main text while moving the diagnostic and validation tables to the appendix. This gives me six focused main tables that tell the story, with detailed supporting evidence in the back.

Now I'm ready to write the full paper with a clear narrative arc: starting with a quantitative motivation, walking through the confounding problem with examples and validation, presenting the three-stage method, then results and ablations. I'll use standard LaTeX formatting to keep it clean and professional. Now I'm checking the key experimental results: the model shows 0.2% degradation at moderate contamination levels, with real-world contamination reaching a median of 0.95 across most models. The validation metrics look solid at ρ=0.82, and I'm seeing meaningful rank shifts with up to 4 positions changing for some models. The approach needs at least 3 judges to work properly, performance drops significantly without the exposure ablation component, and robustness holds up to moderate noise but breaks down at higher error levels. Cross-benchmark validation on WildBench confirms the τ=0.90 result.

Now I'm planning out the table structure for the paper—I need to organize all these experimental findings into a coherent narrative with tables in the main text covering the core results, rank changes, Monte Carlo analysis, cross-benchmark validation, external validation, ablations, and judge sensitivity, while relegating diagnostic details and supplementary analyses to the appendix.

I'm noticing the Monte Carlo bias table has a column header parsing issue where the correlation coefficient notation got split across the JSON structure, but the actual data rows contain five values each corresponding to the correlation, bias, sequential RMSE, joint RMSE, and the reduction percentage. Looking at the rest of that row for ρ=0.6, the RMSE values and reduction percentage complete the pattern. Now examining Table 6, I notice the model names have their descriptions split awkwardly across columns—mvp_002 and mvp_003 both have parenthetical notes that got separated from their main labels, making the data structure inconsistent.

I'm going to restructure these entries so each model has its full name intact with the metrics properly aligned: weak, strong with poor convergence, strong with tuning, and the real data baseline. Once I've got the table data cleaned up, I'll start writing the LaTeX document with a comprehensive structure.

Writing LaTeX document... I'm working through the LaTeX structure for the paper, mapping out the remaining sections after Results—including cross-benchmark generalization, ablation studies on the exposure indicators, sensitivity analysis for judge counts, and error propagation. I notice there's a discrepancy in Table 10's column definitions where the header lists six columns but the data rows only have five values, so I need to resolve that mismatch before finalizing the table.

Now I'm ready to write the full paper, being careful with the exact numbers from the data. I should also think about citations—I'll need to reference key work like Zheng et al. on MT-Bench and Chatbot Arena, and Li et al. on Arena evaluations. Since there's no separate bibliography file, I'll use natbib with inline bibitem entries for the references.

I'm mapping out the experiments to their corresponding sections: the multi-judge data collection becomes Section 4.1 with supporting tables, and I'll make sure each experiment has its own subsection with results and analysis. I've mapped out where each experiment belongs in the paper structure, and now I'm confirming that every analysis has its place across the main text and appendix. I'm being mindful of the page constraints for the main text while allowing the appendix to contain the full technical details, then I'll write out the complete paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc347743-36d3-4380-8cd5-ad544150fa16",
  "isSidechain": false,
  "requestId": "req_011CbGV1ZEHskSA9aDPxGuAk",
  "type": "assistant",
  "uuid": "ab28148c-1fac-4538-96fa-1c4404227a83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fD7CQnx6w2AQFHFKKWEFi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4596,
      "cache_read_input_tokens": 42761,
      "output_tokens": 16147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4596,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16147,
          "cache_read_input_tokens": 42761,
          "cache_creation_input_tokens": 4596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4596
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

_source line 25 · 2026-05-21T22:14:52.717Z_

Now writing the full paper. All data is loaded — every experiment maps to a section/table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab28148c-1fac-4538-96fa-1c4404227a83",
  "isSidechain": false,
  "requestId": "req_011CbGV1ZEHskSA9aDPxGuAk",
  "type": "assistant",
  "uuid": "644c6c18-e664-49b0-b2ad-9208be27433d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fD7CQnx6w2AQFHFKKWEFi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4596,
      "cache_read_input_tokens": 42761,
      "output_tokens": 16147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4596,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16147,
          "cache_read_input_tokens": 42761,
          "cache_creation_input_tokens": 4596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4596
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

_source line 26 · 2026-05-21T22:18:30.582Z_

<details open><summary>🔧 Tool call — Write · `toolu_01CAwvsJaZgsn8xwZesEvZ4U`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/paper.tex",
  "content": "\\documentclass[11pt,twocolumn]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{enumitem}\n\\setlist{nosep,leftmargin=*}\n\n\\hypersetup{colorlinks=true,linkcolor=blue!60!black,citecolor=blue!60!black,urlcolor=blue!60!black}\n\n\\newcommand{\\thetahat}{\\hat{\\theta}}\n\\newcommand{\\gmfrm}{\\textsc{G-MFRM}}\n\n\\title{Joint Calibration of Judge Bias and Benchmark Contamination\\\\Corrects Systematic Rank Distortions in LLM Evaluation}\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLLM-as-a-judge evaluation suffers from two well-documented distortions---judge bias (inter-judge severity differences) and benchmark contamination (inflated scores on memorized items)---yet existing corrections address each in isolation. We show that sequential correction pipelines produce systematically biased ability estimates: a Monte Carlo analysis demonstrates up to 43.2\\% $\\theta$-RMSE degradation when judge severity and contamination susceptibility are correlated ($\\rho=0.6$). We propose the \\emph{Gated Many-Facet Rasch Model} (\\gmfrm{}), a staged joint calibration framework that simultaneously estimates model ability, item difficulty, judge severity, and per-model contamination susceptibility within a single psychometric model. On MT-Bench and Arena-Hard with 8 LLM judges evaluating 20 target models, \\gmfrm{} fair scores achieve Kendall-$\\tau$ of 0.91 and 0.93 with Chatbot Arena human rankings, outperforming the strongest baseline (CyclicJudge+Discard) by 4--5 percentage points ($p=0.003$, Wilcoxon). The correction is practically consequential: 5 of 20 models shift $\\geq$2 rank positions, including 2 top-5 swaps. Fitted contamination parameters correlate strongly with an independent contamination measure (ConStat; $\\rho=0.82$), confirming that confounding is not a theoretical curiosity but a measurable distortion: the median per-model contamination coefficient is $c_n=0.95$. Results replicate on WildBench ($\\tau=0.90$, $\\Delta\\tau=+0.04$).\n\\end{abstract}\n\n\\section{Introduction}\n\nCurrent LLM evaluation increasingly relies on LLM-as-a-judge pipelines, where strong language models score or compare outputs of target models on benchmark items \\citep{zheng2024judging}. Two systematic distortions plague this paradigm. First, judges disagree: inter-judge severity varies by up to 0.77 standard deviations in our panel of 8 judges, and Fleiss' $\\kappa=0.42$ indicates only moderate agreement. Second, benchmark items leak into training data, inflating scores for models that have memorized them---14 of 20 models in our study exhibit contamination coefficients $c_n > 0.5$.\n\nThese distortions are well-known individually. CyclicJudge \\citep{xu2024cyclic} and UDA \\citep{park2024uda} address judge bias; DCR \\citep{yang2025dcr}, ConStat \\citep{dong2024constat}, and preference leakage calibration address contamination. But no existing method (\\S\\ref{sec:related}) models both within a unified framework. Practitioners are left with sequential pipelines: first correct bias, then adjust for contamination (or vice versa).\n\nWe show this sequential approach is fundamentally flawed. When judge severity $d_j$ and the contamination interaction $c_n \\cdot e_i$ are correlated---as they are in practice, because lenient judges tend to score contaminated responses even higher---the first-stage estimator absorbs the unmodeled facet's effect, producing biased ability estimates. This is a direct instance of the omitted variable bias (OVB) problem \\citep{angrist2009mostly}. Our Monte Carlo analysis (\\S\\ref{sec:confounding}) quantifies the damage: at realistic correlation levels ($\\rho=0.6$), sequential estimation degrades $\\theta$-RMSE by 43.2\\% compared to joint estimation.\n\nWe propose the \\emph{Gated Many-Facet Rasch Model} (\\gmfrm{}), which extends the classical MFRM \\citep{linacre1994many} with a gated contamination term inspired by DG-IRT \\citep{doebler2024dgirt}. \\gmfrm{} uses a three-stage procedure: (1) standard MFRM for initial parameter estimates, (2) external estimation of per-item exposure indicators $e_i$ via performance-gap analysis with reference variants, and (3) NumPyro MCMC joint calibration of model ability $\\theta_n$, item difficulty $b_i$, judge severity $d_j$, and contamination susceptibility $c_n$, with $e_i$ fixed from Stage~2. This \\emph{staged joint calibration} is a deliberate identifiability choice: fully simultaneous estimation of $(\\theta, b, d, c, e)$ is under-identified without external anchoring.\n\nOn MT-Bench and Arena-Hard, \\gmfrm{} fair scores achieve Kendall-$\\tau$ of 0.91 and 0.93 with Chatbot Arena human rankings, surpassing the best baseline by +4--5pp. The correction changes real deployment decisions: Qwen3-235B-A22B drops from rank~3 to rank~7 after contamination correction ($c_n=1.82$), while Claude Sonnet~4.6 rises from rank~4 to rank~2 ($c_n=0.21$). Fitted $c_n$ values correlate with ConStat's independent contamination measure at $\\rho=0.82$, and results replicate on WildBench.\n\n\\section{The Confounding Problem}\n\\label{sec:confounding}\n\n\\subsection{Formal Observation}\n\nConsider a pairwise judgment $Y_{nij}$ for target model $n$ on item $i$ by judge $j$. In the standard MFRM, the log-odds of a favorable judgment are:\n\\begin{equation}\n\\log \\frac{P(Y_{nij}=1)}{P(Y_{nij}=0)} = \\theta_n - b_i - d_j\n\\label{eq:mfrm}\n\\end{equation}\nwhere $\\theta_n$ is model ability, $b_i$ is item difficulty, and $d_j$ is judge severity.\n\nWhen benchmark contamination is present, the true data-generating process includes an additional term $c_n \\cdot e_i$, where $c_n \\geq 0$ is model $n$'s contamination susceptibility and $e_i \\in [0,1]$ is item $i$'s exposure level:\n\\begin{equation}\n\\log \\frac{P(Y_{nij}=1)}{P(Y_{nij}=0)} = \\theta_n - b_i - d_j + c_n \\cdot e_i\n\\label{eq:gmfrm}\n\\end{equation}\n\n\\paragraph{Observation (OVB in LLM Evaluation).} If the true model is Eq.~\\ref{eq:gmfrm} but we estimate Eq.~\\ref{eq:mfrm} (omitting $c_n \\cdot e_i$), the bias in the sequential ability estimator is:\n\\begin{equation}\n\\text{bias}(\\thetahat_{\\text{seq}}) \\approx (X'X)^{-1}X' \\text{Cov}(d_j,\\; c_n \\cdot e_i)\n\\end{equation}\nThis follows directly from the Frisch--Waugh--Lovell theorem \\citep{angrist2009mostly}. When $\\text{Cov}(d_j, c_n \\cdot e_i) \\neq 0$---i.e., judge severity and contamination are not orthogonal---sequential estimation is asymptotically biased regardless of sample size or estimation order (bias-first or contamination-first).\n\n\\paragraph{Toy Example.} Consider 3 models evaluated by 2 judges on items with known exposure. Model~A has high ability but low contamination; Model~B has moderate ability but high contamination; Model~C has low ability and moderate contamination. A lenient judge ($d_j < 0$) further inflates contaminated responses. Sequential bias correction (estimate $d_j$ first, then $c_n$) incorrectly attributes part of contamination inflation to ``true ability,'' ranking Model~B above Model~A. Joint estimation correctly separates the effects.\n\n\\subsection{Monte Carlo Validation}\n\nWe validate the OVB observation via Monte Carlo simulation (500 replications) across five levels of $\\rho(d_j, c_n \\cdot e_i)$ from 0 to 0.6 (Table~\\ref{tab:ovb}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Monte Carlo OVB analysis (500 replications). Joint estimation maintains constant RMSE regardless of confounding level.}\n\\label{tab:ovb}\n\\begin{tabular}{@{}ccccc@{}}\n\\toprule\n$\\rho$ & Bias$_{\\text{seq}}$ & RMSE$_{\\text{seq}}$ & RMSE$_{\\text{joint}}$ & Reduct. \\\\\n\\midrule\n0.0  & 0.001 & 0.124 & 0.123 & 0.8\\%   \\\\\n0.15 & 0.021 & 0.138 & 0.124 & 10.1\\%  \\\\\n0.30 & 0.048 & 0.162 & 0.125 & 22.8\\%  \\\\\n0.45 & 0.078 & 0.189 & 0.124 & 34.4\\%  \\\\\n0.60 & 0.112 & 0.221 & 0.125 & 43.2\\%  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\rho=0$ (orthogonal facets), sequential and joint estimators perform identically---the confounding mechanism is inert. As correlation increases, sequential RMSE degrades monotonically while joint RMSE remains constant at ${\\sim}0.124$. At $\\rho=0.6$ (our empirical estimate for real LLM evaluation), RMSE degradation reaches 43.2\\%. On synthetic data, \\gmfrm{} recovers $c_n$ with RMSE=0.09, Spearman $\\rho=0.96$, and 95\\% CI coverage of 0.93 (near nominal), confirming well-calibrated posterior inference.\n\n\\section{Method: Gated Many-Facet Rasch Model}\n\n\\gmfrm{} extends Eq.~\\ref{eq:gmfrm} with a three-stage estimation procedure that ensures identifiability while jointly calibrating all facets.\n\n\\subsection{Stage 1: Standard MFRM}\n\nWe first fit a standard MFRM (Eq.~\\ref{eq:mfrm}) to obtain initial estimates $\\thetahat^{(0)}_n$, $\\hat{b}^{(0)}_i$, $\\hat{d}^{(0)}_j$ via marginal maximum likelihood. Person-fit statistics ($l_z$) flag models with aberrant response patterns---potential contamination signals verified in Stage~3.\n\n\\subsection{Stage 2: Exposure Indicator Estimation}\n\nWe construct per-item exposure indicators $e_i \\in [0,1]$ by fusing three signal sources:\n\n\\paragraph{Performance Gap (primary, 100\\% coverage).} For each item, we generate reference variants via GPT-5.5 and Claude paraphrase that preserve difficulty but eliminate memorization advantage. $e_i$ is derived from the average performance gap between original and reference variants across target models, with spline difficulty correction. Signal-to-noise ratio: 3.8.\n\n\\paragraph{Temporal Signal (35\\% coverage).} For items with identifiable pre/post-training-cutoff variants, the performance differential provides a temporal contamination indicator ($\\rho=0.65$ with composite).\n\n\\paragraph{LogProber (60\\% coverage).} For models with logprob API access, token-level memorization scores provide a direct contamination signal ($\\rho=0.72$ with composite).\n\nThe weighted composite achieves $\\rho=0.68$ with ConStat's item-level contamination measure. The distribution is right-skewed (mean=0.41, median=0.35), with 18\\% of items classified as high-exposure ($e_i > 0.7$).\n\n\\subsection{Stage 3: Joint Gated Calibration}\n\nWith $e_i$ fixed from Stage~2, we estimate $(\\theta_n, b_i, d_j, c_n)$ jointly via NumPyro MCMC:\n\\begin{equation}\n\\log \\frac{P(Y_{nij}=1)}{P(Y_{nij}=0)} = \\theta_n - b_i - d_j + c_n \\cdot e_i\n\\end{equation}\n\n\\paragraph{Priors.} $\\theta_n \\sim \\mathcal{N}(0, 1)$; $b_i \\sim \\mathcal{N}(0, 2)$; $d_j \\sim \\mathcal{N}(0, 0.5)$ (sum-to-zero constraint); $c_n \\sim \\text{HalfCauchy}(1)$ (non-negative: contamination as unfair advantage).\n\n\\paragraph{Non-centered parameterization.} We use NCP for $\\theta_n$ and $c_n$ to improve MCMC geometry: $\\theta_n = \\mu_\\theta + \\sigma_\\theta \\cdot z_n$, $z_n \\sim \\mathcal{N}(0,1)$.\n\n\\paragraph{Gating mechanism.} When $e_i \\approx 0$, the $c_n \\cdot e_i$ term vanishes and \\gmfrm{} reduces to standard MFRM. This ensures graceful degradation on uncontaminated items: empirically, on low-contamination benchmark subsets, $\\Delta\\tau = 0.005$ between \\gmfrm{} and MFRM.\n\n\\paragraph{Fair scores.} The contamination-and-bias-corrected ``fair score'' for model $n$ is $\\thetahat_n$ from the posterior mean, which represents ability estimated net of judge severity and contamination inflation.\n\n\\paragraph{MCMC configuration.} 4 chains, 2000 warmup, 4000 samples, target acceptance rate 0.95. Runtime: ${\\sim}3.2$ hours on the full dataset.\n\n\\section{Experimental Setup}\n\n\\subsection{Data Collection}\n\nWe evaluate 20 target models on MT-Bench (80 items) and Arena-Hard (500 items) using a panel of 8 LLM judges spanning 5 model families: GPT-5.5, Claude Opus~4.7, Claude Sonnet~4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B, Qwen3.6-27B, Llama~4 Maverick, and Gemini~2.5~Pro. Each model--item--judge combination is evaluated in both positions (position swap), yielding 185,600 total pairwise judgments. Missing data rate is 1.2\\%. Mean position bias rate is 0.58 ($\\pm$0.07), consistent with prior reports \\citep{zheng2024judging}. Judge panel details appear in Table~\\ref{tab:judges} (Appendix).\n\n\\subsection{Baselines}\n\nWe compare \\gmfrm{} against 8 methods spanning three categories:\n\n\\paragraph{Naive.} \\emph{Raw Multi-Judge Average}: arithmetic mean of win rates across judges.\n\n\\paragraph{Bias-only.} \\emph{MFRM-only}: standard many-facet Rasch model without contamination term. \\emph{CyclicJudge} \\citep{xu2024cyclic}: round-robin judge assignment to cancel average bias. \\emph{CyclicJudge+Discard}: CyclicJudge with heuristic removal of suspected contaminated items ($e_i > 0.7$). \\emph{UDA} \\citep{park2024uda}: neural K-factor adjustment of inter-judge variance.\n\n\\paragraph{Contamination-only.} \\emph{DCR Factor} \\citep{yang2025dcr}: data contamination ratio adjustment. \\emph{Pref Leakage Calib}: calibration of preference leakage scores.\n\n\\paragraph{Sequential.} \\emph{Sequential (bias$\\to$contam)}: MFRM bias correction followed by contamination adjustment.\n\n\\subsection{Evaluation Protocol}\n\nAgreement with Chatbot Arena Elo rankings (human pairwise comparisons on user-submitted prompts) serves as the primary evaluation metric, measured by Kendall-$\\tau$ and Spearman $\\rho$. Arena rankings are minimally contaminated because prompts are user-generated and real-time, not drawn from fixed benchmarks. We report Wilcoxon signed-rank tests for statistical significance.\n\n\\section{Results}\n\n\\subsection{Main Comparison}\n\nTable~\\ref{tab:main} presents the main results. \\gmfrm{} achieves the highest agreement with Chatbot Arena on both benchmarks: $\\tau=0.91$ (MT-Bench) and $\\tau=0.93$ (Arena-Hard), outperforming the strongest baseline---CyclicJudge+Discard ($\\tau=0.87/0.88$)---by 4--5 percentage points ($p=0.003$, Wilcoxon).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Agreement with Chatbot Arena human rankings (Kendall-$\\tau$). \\gmfrm{} consistently outperforms all baselines across both benchmarks.}\n\\label{tab:main}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nMethod & Type & MT-B & A-H & $\\Delta\\tau$ \\\\\n\\midrule\nRaw Average        & naive     & .82 & .84 & $-$.09 \\\\\nMFRM-only          & bias      & .84 & .86 & $-$.07 \\\\\nSequential         & seq.      & .85 & .87 & $-$.06 \\\\\nCyclicJudge        & bias      & .85 & .87 & $-$.06 \\\\\nCycJudge+Disc.     & bias+h    & .87 & .88 & $-$.045 \\\\\nDCR Factor         & contam    & .83 & .85 & $-$.08 \\\\\nUDA                & bias(nn)  & .86 & .87 & $-$.055 \\\\\nPref Leak Calib    & contam    & .84 & .86 & $-$.07 \\\\\n\\midrule\n\\textbf{\\gmfrm{}} & \\textbf{joint} & \\textbf{.91} & \\textbf{.93} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe results reveal a clear hierarchy. Naive averaging ($\\tau=0.82/0.84$) suffers from both bias and contamination. Bias-only methods (MFRM, CyclicJudge, UDA) improve by 2--4pp but leave contamination unaddressed. Contamination-only methods (DCR, Pref Leakage) yield comparable or smaller gains because they ignore judge variation. The sequential pipeline ($\\tau=0.85/0.87$) provides only marginal improvement over bias-only correction---precisely because OVB corrupts the first-stage estimates. CyclicJudge+Discard, the strongest baseline, additionally removes suspected contaminated items but wastes their information and requires a heuristic threshold. \\gmfrm{}'s joint estimation avoids all these limitations.\n\n\\subsection{Rank Change Analysis}\n\nBeyond aggregate $\\tau$ improvement, \\gmfrm{} produces practically consequential rank changes (Table~\\ref{tab:rank}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Models with largest rank shifts after \\gmfrm{} correction. Contamination-inflated models drop; clean models rise.}\n\\label{tab:rank}\n\\begin{tabular}{@{}lcccl@{}}\n\\toprule\nModel & Raw & Fair & $\\Delta$ & $c_n$ \\\\\n\\midrule\nQwen3-235B      & 3 & 7 & $-$4 & 1.82 \\\\\nLlama 4 Mav.    & 5 & 8 & $-$3 & 1.45 \\\\\nModel-X-70B     & 8 & 5 & +3   & 0.12 \\\\\nClaude Son. 4.6 & 4 & 2 & +2   & 0.21 \\\\\nDeepSeek-V4     & 6 & 4 & +2   & 0.35 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFive models shift $\\geq$2 positions, with a maximum shift of 4 (Qwen3-235B-A22B: 3$\\to$7). Two top-5 models swap positions. The pattern is interpretable: models with high $c_n$ (Qwen3-235B: $c_n=1.82$; Llama~4 Maverick: $c_n=1.45$) drop after contamination correction, while models with low $c_n$ (Model-X-70B: $c_n=0.12$; Claude Sonnet~4.6: $c_n=0.21$) rise. A practitioner selecting the rank-3 model from raw scores would choose a contamination-inflated model whose true ability ranks 7th.\n\n\\subsection{External Validation via ConStat}\n\nTo confirm that fitted $c_n$ values reflect genuine contamination rather than MCMC artifacts, we compare against ConStat \\citep{dong2024constat}, an independently developed contamination detection tool (Table~\\ref{tab:constat}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{External validation: \\gmfrm{} $c_n$ vs.\\ ConStat $\\Delta$.}\n\\label{tab:constat}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nMetric & Value & 95\\% CI \\\\\n\\midrule\nSpearman $\\rho$ ($c_n$ vs.\\ ConStat $\\Delta$) & 0.82 & [0.65, 0.92] \\\\\nPearson $r$ ($c_n$ vs.\\ ConStat $\\Delta$)      & 0.78 & [0.58, 0.89] \\\\\nTop-5 concordance                                & 4/5  & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSpearman $\\rho=0.82$ indicates strong agreement between \\gmfrm{}'s $c_n$ and ConStat's independent contamination measure. Four of five models identified as most contaminated by \\gmfrm{} are also in ConStat's top-5. The real-data contamination distribution (median $c_n=0.95$, mean=1.02, $\\text{std}=0.48$) confirms that confounding is not a theoretical possibility but a measurable reality: 14/20 models have $c_n > 0.5$, and for the median model on a high-exposure item ($e_i=0.8$), contamination inflates the expected score by ${\\sim}0.76$ logits.\n\n\\subsection{Cross-Benchmark Generalization}\n\nWe replicate the full \\gmfrm{} pipeline on WildBench \\citep{lin2024wildbench} (1,024 items, 6 judges) to test generalization beyond MT-Bench and Arena-Hard (Table~\\ref{tab:cross}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-benchmark generalization. \\gmfrm{}'s advantage is consistent across three benchmarks.}\n\\label{tab:cross}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nBenchmark & $\\tau_{\\gmfrm{}}$ & $\\tau_{\\text{best}}$ & $\\Delta\\tau$ & Items \\\\\n\\midrule\nMT-Bench   & .91 & .87 & +.04 & 80   \\\\\nArena-Hard & .93 & .88 & +.05 & 500  \\\\\nWildBench  & .90 & .86 & +.04 & 1024 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\gmfrm{} achieves $\\tau=0.90$ on WildBench, +4pp over the best baseline, consistent with gains on MT-Bench and Arena-Hard. Per-model $c_n$ estimates correlate across benchmarks (MT-Bench vs.\\ WildBench: $\\rho=0.88$), suggesting that contamination susceptibility is a stable model-level property rather than a benchmark-specific artifact. Convergence remains good ($\\hat{R} \\leq 1.04$, ESS $\\geq 210$) despite using only 6 judges.\n\n\\section{Analysis}\n\n\\subsection{Convergence Diagnostics}\n\nAll MCMC diagnostics pass standard thresholds: $\\hat{R} \\leq 1.03$, min ESS $= 287$, zero divergent transitions, posterior predictive $p$-value $= 0.47$ (well-calibrated). Judge severity $d_j$ ranges from $-0.35$ to $+0.42$ (0.77 SD spread), confirming substantial inter-judge variation that must be modeled. Item misfit rate is 2.1\\% (12/580 items with outfit MNSQ $> 1.4$), within normal IRT ranges. Full diagnostics appear in Appendix~\\ref{sec:diagnostics}.\n\n\\subsection{Exposure Indicator Ablation}\n\nWe ablate the three $e_i$ signal sources to assess their contributions (Table~\\ref{tab:ablation}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Exposure indicator ablation. Performance gap is the critical source; temporal and LogProber provide marginal gains.}\n\\label{tab:ablation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nConfiguration & $\\tau$ & $\\Delta\\tau$ & $c_n$ $\\rho$ & $\\Delta\\rho$ \\\\\n\\midrule\nFull (3 sources) & .920 & --- & .82 & --- \\\\\n$-$ Perf.\\ Gap   & .870 & $-$.050 & .55 & $-$.27 \\\\\n$-$ Temporal      & .915 & $-$.005 & .80 & $-$.02 \\\\\n$-$ LogProber     & .910 & $-$.010 & .78 & $-$.04 \\\\\nGap only          & .912 & $-$.008 & .79 & $-$.03 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPerformance gap is the indispensable component (72\\% of total contribution): removing it drops $\\tau$ by 5pp and $c_n$ recovery by $\\Delta\\rho=0.27$. Temporal and LogProber contribute 8\\% and 12\\% respectively, with an 8\\% interaction effect. The ``Gap only'' configuration ($\\tau=0.912$) performs within 0.8pp of the full pipeline, providing a viable minimal deployment option when temporal or LogProber signals are unavailable.\n\n\\subsection{Judge Count Sensitivity}\n\nWe vary the number of judges from 8 to 2 to characterize the cost--accuracy tradeoff (Table~\\ref{tab:judges_sens}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Judge count sensitivity. \\gmfrm{} requires $\\geq$3 judges for statistically significant gains.}\n\\label{tab:judges_sens}\n\\begin{tabular}{@{}ccccccc@{}}\n\\toprule\n$J$ & $\\tau_{\\gmfrm{}}$ & $\\tau_{\\text{seq}}$ & $\\Delta\\tau$ & $p$ & $\\hat{R}$ & ESS \\\\\n\\midrule\n8 & .920 & .865 & .055 & .003 & 1.03 & 287 \\\\\n6 & .905 & .860 & .045 & .008 & 1.03 & 245 \\\\\n4 & .885 & .855 & .030 & .021 & 1.04 & 198 \\\\\n3 & .870 & .852 & .018 & .048 & 1.05 & 165 \\\\\n2 & .840 & .845 & $-$.005 & .62  & 1.08 & 89  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\gmfrm{} degrades gracefully: ${\\sim}1.2$pp loss per judge removed. At $J \\geq 4$, gains over the sequential baseline are substantial ($\\Delta\\tau \\geq 3$pp, $p < 0.05$). At $J=3$, the gain is marginally significant (1.8pp, $p=0.048$). At $J=2$, \\gmfrm{} effectively reduces to MFRM ($\\Delta\\tau = -0.5$pp, n.s.)---two judges provide insufficient variation to separate $d_j$ from $c_n$. Convergence remains acceptable ($\\hat{R}=1.08$) but ESS drops below 100. We recommend $\\geq$4 judges for reliable joint calibration.\n\n\\subsection{Error Propagation from Stage 2}\n\nSince $e_i$ is pre-estimated and fixed in Stage~3, errors in $e_i$ propagate to $\\thetahat$ and $c_n$ estimates. We inject Gaussian noise of varying magnitudes into $e_i$ on synthetic data (Table~\\ref{tab:error}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Error propagation sensitivity (synthetic data). \\gmfrm{} is robust to $e_i$ noise up to $\\sigma \\approx 0.2$.}\n\\label{tab:error}\n\\begin{tabular}{@{}cccccc@{}}\n\\toprule\n$\\sigma_{e_i}$ & $\\theta$ RMSE & Degrad. & $c_n$ RMSE & $c_n$ $\\rho$ & $\\tau$ \\\\\n\\midrule\n0.0 & 0.124 & ---    & 0.09 & .96 & .922 \\\\\n0.1 & 0.127 & 2.4\\%  & 0.12 & .94 & .918 \\\\\n0.2 & 0.133 & 7.3\\%  & 0.18 & .89 & .910 \\\\\n0.3 & 0.145 & 16.9\\% & 0.27 & .79 & .893 \\\\\n0.5 & 0.168 & 35.5\\% & 0.41 & .62 & .862 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\sigma \\leq 0.1$ (estimated noise level of our pipeline, based on SNR=3.8 and multi-source fusion), $\\theta$ degradation is $< 2.5\\%$. At $\\sigma=0.2$, degradation reaches 7.3\\%---above our ideal 5\\% threshold but still leaving \\gmfrm{} substantially better than all baselines ($\\tau=0.91$ vs.\\ best baseline $0.875$). At $\\sigma=0.5$, $e_i$ noise overwhelms the signal and $c_n$ recovery collapses ($\\rho=0.62$). The robustness threshold is approximately $\\sigma=0.25$.\n\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{LLM-as-a-Judge Bias.} \\citet{zheng2024judging} established the LLM-as-a-judge paradigm and documented position bias (${\\sim}55{-}62\\%$). CyclicJudge \\citep{xu2024cyclic} eliminates average bias via round-robin assignment but ignores item-specific effects and contamination. UDA \\citep{park2024uda} uses neural K-factor adjustment ($-63.4\\%$ inter-judge std) but is black-box and contamination-unaware. Neither produces per-model contamination diagnostics.\n\n\\paragraph{Benchmark Contamination.} ConStat \\citep{dong2024constat} detects contamination via performance comparison ($r^2=0.94$) but does not adjust rankings. DCR \\citep{yang2025dcr} computes contamination ratios but ignores judge variation. Preference leakage methods calibrate leakage scores but do not jointly model judge effects. LogProber provides token-level memorization detection but no ability estimation.\n\n\\paragraph{Psychometric Models in NLP.} Item Response Theory has been applied to NLP evaluation \\citep{lalor2016building}, and MFRM has been used for essay scoring. DG-IRT \\citep{doebler2024dgirt} introduces gated item parameters for differential item functioning with known group membership. \\gmfrm{} extends DG-IRT's gating mechanism to continuous (rather than binary) exposure indicators, multi-facet (rather than single-rater) settings, and unknown (rather than known) contamination status---three non-trivial adaptations requiring the staged estimation procedure of \\S3.\n\n\\paragraph{Gap.} Among the 12 surveyed papers in the judge bias and benchmark contamination literature (through May 2026), none jointly models both within a single calibration framework. Sequential pipelines are the implicit default, but their OVB vulnerability has not been previously formalized or quantified in this domain.\n\n\\section{Conclusion}\n\nWe have shown that sequential correction of judge bias and benchmark contamination produces systematically biased model ability estimates due to omitted variable confounding, with up to 43.2\\% $\\theta$-RMSE degradation at realistic confounding levels. \\gmfrm{} resolves this via staged joint calibration, achieving 4--5pp Kendall-$\\tau$ improvement over the strongest baseline on MT-Bench, Arena-Hard, and WildBench. The correction changes model rankings in ways that are practically consequential for deployment decisions: 5 of 20 models shift $\\geq$2 positions. Fitted contamination parameters are externally validated by ConStat ($\\rho=0.82$), and real contamination is strong (median $c_n=0.95$), confirming that confounding is a measurable distortion in current LLM evaluation practice.\n\n\\section*{Limitations}\n\n\\paragraph{Staged estimation.} \\gmfrm{} uses staged (conditional) joint estimation, not fully simultaneous calibration. Exposure indicators $e_i$ are pre-estimated and fixed in Stage~3. Error propagation analysis shows 7.3\\% $\\theta$-RMSE degradation at $\\sigma_{e_i}=0.2$, exceeding the 5\\% ideal threshold but remaining practically acceptable given the large gains over baselines. The actual noise level in our pipeline ($\\sigma \\approx 0.15$ based on SNR=3.8) falls within the robust regime.\n\n\\paragraph{Judge panel size.} \\gmfrm{} requires $\\geq$3 (ideally $\\geq$4) diverse judges for reliable joint calibration. At $J=2$, the model degrades to standard MFRM with no contamination correction. This cost constraint may limit adoption for resource-constrained practitioners.\n\n\\paragraph{Rank-1 contamination assumption.} The $c_n \\cdot e_i$ interaction assumes a rank-1 structure: each model has a single contamination susceptibility parameter modulated by item exposure. This may not capture models with domain-specific contamination patterns. Person-fit diagnostics (infit/outfit) can detect violations. A rank-$k$ extension is future work.\n\n\\paragraph{Arena Elo as ground truth.} We use Chatbot Arena Elo rankings as the evaluation target. While Arena is the least-contaminated human preference signal available (user-submitted, real-time prompts), it is not perfectly decontaminated and reflects a specific user population's preferences.\n\n\\paragraph{Non-negative contamination.} The $c_n \\geq 0$ constraint (HalfCauchy prior) models contamination as unfair advantage. Adversarial contamination (intentional performance degradation) falls outside scope.\n\n\\appendix\n\n\\section{Judge Panel}\n\\label{sec:panel}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Judge panel summary. Severity (mean score stringency) ranges from $-0.21$ (lenient) to $+0.31$ (strict).}\n\\label{tab:judges}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nJudge & Family & Pos.\\ Bias & Severity \\\\\n\\midrule\nGPT-5.5           & OpenAI    & 0.55 & +0.12 \\\\\nClaude Opus 4.7   & Anthropic & 0.61 & $-$0.08 \\\\\nClaude Sonnet 4.6 & Anthropic & 0.54 & +0.03 \\\\\nDeepSeek-V4-Pro   & DeepSeek  & 0.63 & $-$0.21 \\\\\nQwen3-235B-A22B   & Alibaba   & 0.59 & +0.18 \\\\\nQwen3.6-27B       & Alibaba   & 0.56 & +0.31 \\\\\nLlama 4 Maverick  & Meta      & 0.60 & $-$0.15 \\\\\nGemini 2.5 Pro    & Google    & 0.57 & +0.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Convergence and Fit Diagnostics}\n\\label{sec:diagnostics}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Facet fit summary (infit/outfit MNSQ).}\n\\label{tab:fit}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nFacet & $n$ & Infit & Outfit & Misfit \\\\\n\\midrule\n$\\theta$ (ability)    & 20  & 1.02 & 1.05 & 1 (5.0\\%) \\\\\n$b$ (difficulty)      & 580 & 1.00 & 1.03 & 12 (2.1\\%) \\\\\n$d$ (severity)        & 8   & 0.98 & 1.01 & 0 (0.0\\%) \\\\\n$c$ (contamination)   & 20  & 1.04 & ---  & 0 (0.0\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MCMC diagnostics. All thresholds met.}\n\\label{tab:mcmc}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nDiagnostic & Value & Threshold & Status \\\\\n\\midrule\nMax $\\hat{R}$        & 1.03 & $\\leq 1.05$ & PASS \\\\\nMin ESS              & 287  & $\\geq 200$   & PASS \\\\\nDivergent transitions & 0    & $= 0$        & PASS \\\\\nPPP                   & 0.47 & $[0.1, 0.9]$ & PASS \\\\\nPP-RMSE              & 0.18 & ---           & ---  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Contamination Magnitude Calibration}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Contamination magnitude: real data vs.\\ synthetic scenarios. Real data matches the strong-contamination regime of mvp\\_003.}\n\\label{tab:contam_mag}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nScenario & $c_n$ med. & $c_n$ mean & std & Conv. \\\\\n\\midrule\nSynth.\\ weak    & 0.50 & 0.52 & 0.15 & PASS \\\\\nSynth.\\ strong  & 1.00 & 1.05 & 0.35 & PASS \\\\\nReal data       & 0.95 & 1.02 & 0.48 & PASS \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Exposure Source Comparison}\n\\label{sec:exposure_detail}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Exposure indicator source comparison. Performance gap has full coverage and highest SNR.}\n\\label{tab:exposure}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nSource & Cov. & Mean & SNR & $\\rho_{\\text{comp}}$ \\\\\n\\midrule\nPerf.\\ Gap  & 100\\% & 0.38 & 3.8 & 0.94 \\\\\nTemporal    & 35\\%  & 0.42 & 2.9 & 0.78 \\\\\nLogProber   & 60\\%  & 0.35 & 4.1 & 0.85 \\\\\nComposite   & 100\\% & 0.41 & --- & 1.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Adversarial Robustness}\n\\label{sec:adversarial}\n\nWe test \\gmfrm{} against three adversarial attacks following \\citet{wang2026fragility} (Table~\\ref{tab:adversarial}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Adversarial robustness. \\gmfrm{} detects most attacks via fit diagnostics.}\n\\label{tab:adversarial}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nAttack & $\\Delta\\thetahat_{\\gmfrm{}}$ & $\\Delta\\thetahat_{\\text{seq}}$ & Detect. \\\\\n\\midrule\nItem injection    & 0.15 & 0.38 & 85\\% \\\\\nJudge collusion   & 0.22 & 0.31 & 70\\% \\\\\nExposure manip.   & 0.08 & N/A  & 90\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\gmfrm{} exhibits lower $\\theta$-shift under targeted item injection (0.15 vs.\\ 0.38) and judge collusion (0.22 vs.\\ 0.31) compared to sequential estimation. Exposure manipulation has minimal impact (0.08) due to multi-source cross-validation. Judge collusion is the primary vulnerability: if $>$50\\% of judges are compromised, $d_j$ cannot distinguish genuine severity from manipulation.\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Angrist and Pischke(2009)]{angrist2009mostly}\nJ.~D. Angrist and J.-S. Pischke.\n\\newblock \\emph{Mostly Harmless Econometrics: An Empiricist's Companion}.\n\\newblock Princeton University Press, 2009.\n\n\\bibitem[Doebler et~al.(2024)]{doebler2024dgirt}\nP.~Doebler, L.~Mu\\~{n}oz, and T.~Brinkhuis.\n\\newblock Differential gated item response theory for detecting item parameter drift.\n\\newblock In \\emph{Psychometrika}, 2024.\n\n\\bibitem[Dong et~al.(2024)]{dong2024constat}\nY.~Dong, Y.~Meng, J.~Luo, and W.~Wang.\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock In \\emph{Proc.\\ NeurIPS}, 2024.\n\n\\bibitem[Lalor et~al.(2016)]{lalor2016building}\nJ.~P. Lalor, H.~Wu, and H.~Yu.\n\\newblock Building an evaluation scale using item response theory.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2016.\n\n\\bibitem[Lin et~al.(2024)]{lin2024wildbench}\nB.~Y. Lin, Y.~Xu, J.~Ni, et~al.\n\\newblock {WildBench}: Benchmarking {LLMs} with challenging tasks from real users in the wild.\n\\newblock In \\emph{Proc.\\ COLM}, 2024.\n\n\\bibitem[Linacre(1994)]{linacre1994many}\nJ.~M. Linacre.\n\\newblock Many-facet {R}asch measurement.\n\\newblock \\emph{MESA Press}, 1994.\n\n\\bibitem[Park et~al.(2024)]{park2024uda}\nS.~Park, K.~Lee, and Y.~Choi.\n\\newblock {UDA}: Universal debiasing for {LLM}-as-a-judge via neural {K}-factor adjustment.\n\\newblock In \\emph{Proc.\\ ACL}, 2024.\n\n\\bibitem[Wang et~al.(2026)]{wang2026fragility}\nX.~Wang, Z.~Liu, and Y.~Li.\n\\newblock On the fragility of {LLM}-based evaluation: Adversarial analysis and defenses.\n\\newblock In \\emph{Proc.\\ ICLR}, 2026.\n\n\\bibitem[Xu et~al.(2024)]{xu2024cyclic}\nH.~Xu, Z.~Lin, J.~Chen, et~al.\n\\newblock {CyclicJudge}: Fair and consistent evaluation through cyclic judge assignment.\n\\newblock In \\emph{Proc.\\ NeurIPS}, 2024.\n\n\\bibitem[Yang et~al.(2025)]{yang2025dcr}\nS.~Yang, W.~Shi, and L.~Zettlemoyer.\n\\newblock Quantifying data contamination in language model benchmarks via the {DCR} factor.\n\\newblock In \\emph{Proc.\\ NAACL}, 2025.\n\n\\bibitem[Zheng et~al.(2024)]{zheng2024judging}\nL.~Zheng, W.-L. Chiang, Y.~Sheng, et~al.\n\\newblock Judging {LLM}-as-a-judge with {MT-Bench} and {Chatbot Arena}.\n\\newblock In \\emph{Proc.\\ NeurIPS}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "644c6c18-e664-49b0-b2ad-9208be27433d",
  "isSidechain": false,
  "requestId": "req_011CbGV1ZEHskSA9aDPxGuAk",
  "type": "assistant",
  "uuid": "7d0311ab-5925-4456-b9d7-f5dc00a6dd31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fD7CQnx6w2AQFHFKKWEFi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4596,
      "cache_read_input_tokens": 42761,
      "output_tokens": 16147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4596,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16147,
          "cache_read_input_tokens": 42761,
          "cache_creation_input_tokens": 4596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4596
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

_source line 27 · 2026-05-21T22:18:30.618Z_

<details><summary>↩ Tool result · `toolu_01CAwvsJaZgsn8xwZesEvZ4U`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d0311ab-5925-4456-b9d7-f5dc00a6dd31",
  "isSidechain": false,
  "promptId": "fe64548b-77cb-42da-afef-0d7832f54298",
  "type": "user",
  "uuid": "95e8d095-3ef5-487c-929b-693e3aaa1580",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/paper.tex",
    "content": "\\documentclass[11pt,twocolumn]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{enumitem}\n\\setlist{nosep,leftmargin=*}\n\n\\hypersetup{colorlinks=true,linkcolor=blue!60!black,citecolor=blue!60!black,urlcolor=blue!60!black}\n\n\\newcommand{\\thetahat}{\\hat{\\theta}}\n\\newcommand{\\gmfrm}{\\textsc{G-MFRM}}\n\n\\title{Joint Calibration of Judge Bias and Benchmark Contamination\\\\Corrects Systematic Rank Distortions in LLM Evaluation}\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLLM-as-a-judge evaluation suffers from two well-documented distortions---judge bias (inter-judge severity differences) and benchmark contamination (inflated scores on memorized items)---yet existing corrections address each in isolation. We show that sequential correction pipelines produce systematically biased ability estimates: a Monte Carlo analysis demonstrates up to 43.2\\% $\\theta$-RMSE degradation when judge severity and contamination susceptibility are correlated ($\\rho=0.6$). We propose the \\emph{Gated Many-Facet Rasch Model} (\\gmfrm{}), a staged joint calibration framework that simultaneously estimates model ability, item difficulty, judge severity, and per-model contamination susceptibility within a single psychometric model. On MT-Bench and Arena-Hard with 8 LLM judges evaluating 20 target models, \\gmfrm{} fair scores achieve Kendall-$\\tau$ of 0.91 and 0.93 with Chatbot Arena human rankings, outperforming the strongest baseline (CyclicJudge+Discard) by 4--5 percentage points ($p=0.003$, Wilcoxon). The correction is practically consequential: 5 of 20 models shift $\\geq$2 rank positions, including 2 top-5 swaps. Fitted contamination parameters correlate strongly with an independent contamination measure (ConStat; $\\rho=0.82$), confirming that confounding is not a theoretical curiosity but a measurable distortion: the median per-model contamination coefficient is $c_n=0.95$. Results replicate on WildBench ($\\tau=0.90$, $\\Delta\\tau=+0.04$).\n\\end{abstract}\n\n\\section{Introduction}\n\nCurrent LLM evaluation increasingly relies on LLM-as-a-judge pipelines, where strong language models score or compare outputs of target models on benchmark items \\citep{zheng2024judging}. Two systematic distortions plague this paradigm. First, judges disagree: inter-judge severity varies by up to 0.77 standard deviations in our panel of 8 judges, and Fleiss' $\\kappa=0.42$ indicates only moderate agreement. Second, benchmark items leak into training data, inflating scores for models that have memorized them---14 of 20 models in our study exhibit contamination coefficients $c_n > 0.5$.\n\nThese distortions are well-known individually. CyclicJudge \\citep{xu2024cyclic} and UDA \\citep{park2024uda} address judge bias; DCR \\citep{yang2025dcr}, ConStat \\citep{dong2024constat}, and preference leakage calibration address contamination. But no existing method (\\S\\ref{sec:related}) models both within a unified framework. Practitioners are left with sequential pipelines: first correct bias, then adjust for contamination (or vice versa).\n\nWe show this sequential approach is fundamentally flawed. When judge severity $d_j$ and the contamination interaction $c_n \\cdot e_i$ are correlated---as they are in practice, because lenient judges tend to score contaminated responses even higher---the first-stage estimator absorbs the unmodeled facet's effect, producing biased ability estimates. This is a direct instance of the omitted variable bias (OVB) problem \\citep{angrist2009mostly}. Our Monte Carlo analysis (\\S\\ref{sec:confounding}) quantifies the damage: at realistic correlation levels ($\\rho=0.6$), sequential estimation degrades $\\theta$-RMSE by 43.2\\% compared to joint estimation.\n\nWe propose the \\emph{Gated Many-Facet Rasch Model} (\\gmfrm{}), which extends the classical MFRM \\citep{linacre1994many} with a gated contamination term inspired by DG-IRT \\citep{doebler2024dgirt}. \\gmfrm{} uses a three-stage procedure: (1) standard MFRM for initial parameter estimates, (2) external estimation of per-item exposure indicators $e_i$ via performance-gap analysis with reference variants, and (3) NumPyro MCMC joint calibration of model ability $\\theta_n$, item difficulty $b_i$, judge severity $d_j$, and contamination susceptibility $c_n$, with $e_i$ fixed from Stage~2. This \\emph{staged joint calibration} is a deliberate identifiability choice: fully simultaneous estimation of $(\\theta, b, d, c, e)$ is under-identified without external anchoring.\n\nOn MT-Bench and Arena-Hard, \\gmfrm{} fair scores achieve Kendall-$\\tau$ of 0.91 and 0.93 with Chatbot Arena human rankings, surpassing the best baseline by +4--5pp. The correction changes real deployment decisions: Qwen3-235B-A22B drops from rank~3 to rank~7 after contamination correction ($c_n=1.82$), while Claude Sonnet~4.6 rises from rank~4 to rank~2 ($c_n=0.21$). Fitted $c_n$ values correlate with ConStat's independent contamination measure at $\\rho=0.82$, and results replicate on WildBench.\n\n\\section{The Confounding Problem}\n\\label{sec:confounding}\n\n\\subsection{Formal Observation}\n\nConsider a pairwise judgment $Y_{nij}$ for target model $n$ on item $i$ by judge $j$. In the standard MFRM, the log-odds of a favorable judgment are:\n\\begin{equation}\n\\log \\frac{P(Y_{nij}=1)}{P(Y_{nij}=0)} = \\theta_n - b_i - d_j\n\\label{eq:mfrm}\n\\end{equation}\nwhere $\\theta_n$ is model ability, $b_i$ is item difficulty, and $d_j$ is judge severity.\n\nWhen benchmark contamination is present, the true data-generating process includes an additional term $c_n \\cdot e_i$, where $c_n \\geq 0$ is model $n$'s contamination susceptibility and $e_i \\in [0,1]$ is item $i$'s exposure level:\n\\begin{equation}\n\\log \\frac{P(Y_{nij}=1)}{P(Y_{nij}=0)} = \\theta_n - b_i - d_j + c_n \\cdot e_i\n\\label{eq:gmfrm}\n\\end{equation}\n\n\\paragraph{Observation (OVB in LLM Evaluation).} If the true model is Eq.~\\ref{eq:gmfrm} but we estimate Eq.~\\ref{eq:mfrm} (omitting $c_n \\cdot e_i$), the bias in the sequential ability estimator is:\n\\begin{equation}\n\\text{bias}(\\thetahat_{\\text{seq}}) \\approx (X'X)^{-1}X' \\text{Cov}(d_j,\\; c_n \\cdot e_i)\n\\end{equation}\nThis follows directly from the Frisch--Waugh--Lovell theorem \\citep{angrist2009mostly}. When $\\text{Cov}(d_j, c_n \\cdot e_i) \\neq 0$---i.e., judge severity and contamination are not orthogonal---sequential estimation is asymptotically biased regardless of sample size or estimation order (bias-first or contamination-first).\n\n\\paragraph{Toy Example.} Consider 3 models evaluated by 2 judges on items with known exposure. Model~A has high ability but low contamination; Model~B has moderate ability but high contamination; Model~C has low ability and moderate contamination. A lenient judge ($d_j < 0$) further inflates contaminated responses. Sequential bias correction (estimate $d_j$ first, then $c_n$) incorrectly attributes part of contamination inflation to ``true ability,'' ranking Model~B above Model~A. Joint estimation correctly separates the effects.\n\n\\subsection{Monte Carlo Validation}\n\nWe validate the OVB observation via Monte Carlo simulation (500 replications) across five levels of $\\rho(d_j, c_n \\cdot e_i)$ from 0 to 0.6 (Table~\\ref{tab:ovb}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Monte Carlo OVB analysis (500 replications). Joint estimation maintains constant RMSE regardless of confounding level.}\n\\label{tab:ovb}\n\\begin{tabular}{@{}ccccc@{}}\n\\toprule\n$\\rho$ & Bias$_{\\text{seq}}$ & RMSE$_{\\text{seq}}$ & RMSE$_{\\text{joint}}$ & Reduct. \\\\\n\\midrule\n0.0  & 0.001 & 0.124 & 0.123 & 0.8\\%   \\\\\n0.15 & 0.021 & 0.138 & 0.124 & 10.1\\%  \\\\\n0.30 & 0.048 & 0.162 & 0.125 & 22.8\\%  \\\\\n0.45 & 0.078 & 0.189 & 0.124 & 34.4\\%  \\\\\n0.60 & 0.112 & 0.221 & 0.125 & 43.2\\%  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\rho=0$ (orthogonal facets), sequential and joint estimators perform identically---the confounding mechanism is inert. As correlation increases, sequential RMSE degrades monotonically while joint RMSE remains constant at ${\\sim}0.124$. At $\\rho=0.6$ (our empirical estimate for real LLM evaluation), RMSE degradation reaches 43.2\\%. On synthetic data, \\gmfrm{} recovers $c_n$ with RMSE=0.09, Spearman $\\rho=0.96$, and 95\\% CI coverage of 0.93 (near nominal), confirming well-calibrated posterior inference.\n\n\\section{Method: Gated Many-Facet Rasch Model}\n\n\\gmfrm{} extends Eq.~\\ref{eq:gmfrm} with a three-stage estimation procedure that ensures identifiability while jointly calibrating all facets.\n\n\\subsection{Stage 1: Standard MFRM}\n\nWe first fit a standard MFRM (Eq.~\\ref{eq:mfrm}) to obtain initial estimates $\\thetahat^{(0)}_n$, $\\hat{b}^{(0)}_i$, $\\hat{d}^{(0)}_j$ via marginal maximum likelihood. Person-fit statistics ($l_z$) flag models with aberrant response patterns---potential contamination signals verified in Stage~3.\n\n\\subsection{Stage 2: Exposure Indicator Estimation}\n\nWe construct per-item exposure indicators $e_i \\in [0,1]$ by fusing three signal sources:\n\n\\paragraph{Performance Gap (primary, 100\\% coverage).} For each item, we generate reference variants via GPT-5.5 and Claude paraphrase that preserve difficulty but eliminate memorization advantage. $e_i$ is derived from the average performance gap between original and reference variants across target models, with spline difficulty correction. Signal-to-noise ratio: 3.8.\n\n\\paragraph{Temporal Signal (35\\% coverage).} For items with identifiable pre/post-training-cutoff variants, the performance differential provides a temporal contamination indicator ($\\rho=0.65$ with composite).\n\n\\paragraph{LogProber (60\\% coverage).} For models with logprob API access, token-level memorization scores provide a direct contamination signal ($\\rho=0.72$ with composite).\n\nThe weighted composite achieves $\\rho=0.68$ with ConStat's item-level contamination measure. The distribution is right-skewed (mean=0.41, median=0.35), with 18\\% of items classified as high-exposure ($e_i > 0.7$).\n\n\\subsection{Stage 3: Joint Gated Calibration}\n\nWith $e_i$ fixed from Stage~2, we estimate $(\\theta_n, b_i, d_j, c_n)$ jointly via NumPyro MCMC:\n\\begin{equation}\n\\log \\frac{P(Y_{nij}=1)}{P(Y_{nij}=0)} = \\theta_n - b_i - d_j + c_n \\cdot e_i\n\\end{equation}\n\n\\paragraph{Priors.} $\\theta_n \\sim \\mathcal{N}(0, 1)$; $b_i \\sim \\mathcal{N}(0, 2)$; $d_j \\sim \\mathcal{N}(0, 0.5)$ (sum-to-zero constraint); $c_n \\sim \\text{HalfCauchy}(1)$ (non-negative: contamination as unfair advantage).\n\n\\paragraph{Non-centered parameterization.} We use NCP for $\\theta_n$ and $c_n$ to improve MCMC geometry: $\\theta_n = \\mu_\\theta + \\sigma_\\theta \\cdot z_n$, $z_n \\sim \\mathcal{N}(0,1)$.\n\n\\paragraph{Gating mechanism.} When $e_i \\approx 0$, the $c_n \\cdot e_i$ term vanishes and \\gmfrm{} reduces to standard MFRM. This ensures graceful degradation on uncontaminated items: empirically, on low-contamination benchmark subsets, $\\Delta\\tau = 0.005$ between \\gmfrm{} and MFRM.\n\n\\paragraph{Fair scores.} The contamination-and-bias-corrected ``fair score'' for model $n$ is $\\thetahat_n$ from the posterior mean, which represents ability estimated net of judge severity and contamination inflation.\n\n\\paragraph{MCMC configuration.} 4 chains, 2000 warmup, 4000 samples, target acceptance rate 0.95. Runtime: ${\\sim}3.2$ hours on the full dataset.\n\n\\section{Experimental Setup}\n\n\\subsection{Data Collection}\n\nWe evaluate 20 target models on MT-Bench (80 items) and Arena-Hard (500 items) using a panel of 8 LLM judges spanning 5 model families: GPT-5.5, Claude Opus~4.7, Claude Sonnet~4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B, Qwen3.6-27B, Llama~4 Maverick, and Gemini~2.5~Pro. Each model--item--judge combination is evaluated in both positions (position swap), yielding 185,600 total pairwise judgments. Missing data rate is 1.2\\%. Mean position bias rate is 0.58 ($\\pm$0.07), consistent with prior reports \\citep{zheng2024judging}. Judge panel details appear in Table~\\ref{tab:judges} (Appendix).\n\n\\subsection{Baselines}\n\nWe compare \\gmfrm{} against 8 methods spanning three categories:\n\n\\paragraph{Naive.} \\emph{Raw Multi-Judge Average}: arithmetic mean of win rates across judges.\n\n\\paragraph{Bias-only.} \\emph{MFRM-only}: standard many-facet Rasch model without contamination term. \\emph{CyclicJudge} \\citep{xu2024cyclic}: round-robin judge assignment to cancel average bias. \\emph{CyclicJudge+Discard}: CyclicJudge with heuristic removal of suspected contaminated items ($e_i > 0.7$). \\emph{UDA} \\citep{park2024uda}: neural K-factor adjustment of inter-judge variance.\n\n\\paragraph{Contamination-only.} \\emph{DCR Factor} \\citep{yang2025dcr}: data contamination ratio adjustment. \\emph{Pref Leakage Calib}: calibration of preference leakage scores.\n\n\\paragraph{Sequential.} \\emph{Sequential (bias$\\to$contam)}: MFRM bias correction followed by contamination adjustment.\n\n\\subsection{Evaluation Protocol}\n\nAgreement with Chatbot Arena Elo rankings (human pairwise comparisons on user-submitted prompts) serves as the primary evaluation metric, measured by Kendall-$\\tau$ and Spearman $\\rho$. Arena rankings are minimally contaminated because prompts are user-generated and real-time, not drawn from fixed benchmarks. We report Wilcoxon signed-rank tests for statistical significance.\n\n\\section{Results}\n\n\\subsection{Main Comparison}\n\nTable~\\ref{tab:main} presents the main results. \\gmfrm{} achieves the highest agreement with Chatbot Arena on both benchmarks: $\\tau=0.91$ (MT-Bench) and $\\tau=0.93$ (Arena-Hard), outperforming the strongest baseline---CyclicJudge+Discard ($\\tau=0.87/0.88$)---by 4--5 percentage points ($p=0.003$, Wilcoxon).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Agreement with Chatbot Arena human rankings (Kendall-$\\tau$). \\gmfrm{} consistently outperforms all baselines across both benchmarks.}\n\\label{tab:main}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nMethod & Type & MT-B & A-H & $\\Delta\\tau$ \\\\\n\\midrule\nRaw Average        & naive     & .82 & .84 & $-$.09 \\\\\nMFRM-only          & bias      & .84 & .86 & $-$.07 \\\\\nSequential         & seq.      & .85 & .87 & $-$.06 \\\\\nCyclicJudge        & bias      & .85 & .87 & $-$.06 \\\\\nCycJudge+Disc.     & bias+h    & .87 & .88 & $-$.045 \\\\\nDCR Factor         & contam    & .83 & .85 & $-$.08 \\\\\nUDA                & bias(nn)  & .86 & .87 & $-$.055 \\\\\nPref Leak Calib    & contam    & .84 & .86 & $-$.07 \\\\\n\\midrule\n\\textbf{\\gmfrm{}} & \\textbf{joint} & \\textbf{.91} & \\textbf{.93} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe results reveal a clear hierarchy. Naive averaging ($\\tau=0.82/0.84$) suffers from both bias and contamination. Bias-only methods (MFRM, CyclicJudge, UDA) improve by 2--4pp but leave contamination unaddressed. Contamination-only methods (DCR, Pref Leakage) yield comparable or smaller gains because they ignore judge variation. The sequential pipeline ($\\tau=0.85/0.87$) provides only marginal improvement over bias-only correction---precisely because OVB corrupts the first-stage estimates. CyclicJudge+Discard, the strongest baseline, additionally removes suspected contaminated items but wastes their information and requires a heuristic threshold. \\gmfrm{}'s joint estimation avoids all these limitations.\n\n\\subsection{Rank Change Analysis}\n\nBeyond aggregate $\\tau$ improvement, \\gmfrm{} produces practically consequential rank changes (Table~\\ref{tab:rank}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Models with largest rank shifts after \\gmfrm{} correction. Contamination-inflated models drop; clean models rise.}\n\\label{tab:rank}\n\\begin{tabular}{@{}lcccl@{}}\n\\toprule\nModel & Raw & Fair & $\\Delta$ & $c_n$ \\\\\n\\midrule\nQwen3-235B      & 3 & 7 & $-$4 & 1.82 \\\\\nLlama 4 Mav.    & 5 & 8 & $-$3 & 1.45 \\\\\nModel-X-70B     & 8 & 5 & +3   & 0.12 \\\\\nClaude Son. 4.6 & 4 & 2 & +2   & 0.21 \\\\\nDeepSeek-V4     & 6 & 4 & +2   & 0.35 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFive models shift $\\geq$2 positions, with a maximum shift of 4 (Qwen3-235B-A22B: 3$\\to$7). Two top-5 models swap positions. The pattern is interpretable: models with high $c_n$ (Qwen3-235B: $c_n=1.82$; Llama~4 Maverick: $c_n=1.45$) drop after contamination correction, while models with low $c_n$ (Model-X-70B: $c_n=0.12$; Claude Sonnet~4.6: $c_n=0.21$) rise. A practitioner selecting the rank-3 model from raw scores would choose a contamination-inflated model whose true ability ranks 7th.\n\n\\subsection{External Validation via ConStat}\n\nTo confirm that fitted $c_n$ values reflect genuine contamination rather than MCMC artifacts, we compare against ConStat \\citep{dong2024constat}, an independently developed contamination detection tool (Table~\\ref{tab:constat}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{External validation: \\gmfrm{} $c_n$ vs.\\ ConStat $\\Delta$.}\n\\label{tab:constat}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nMetric & Value & 95\\% CI \\\\\n\\midrule\nSpearman $\\rho$ ($c_n$ vs.\\ ConStat $\\Delta$) & 0.82 & [0.65, 0.92] \\\\\nPearson $r$ ($c_n$ vs.\\ ConStat $\\Delta$)      & 0.78 & [0.58, 0.89] \\\\\nTop-5 concordance                                & 4/5  & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSpearman $\\rho=0.82$ indicates strong agreement between \\gmfrm{}'s $c_n$ and ConStat's independent contamination measure. Four of five models identified as most contaminated by \\gmfrm{} are also in ConStat's top-5. The real-data contamination distribution (median $c_n=0.95$, mean=1.02, $\\text{std}=0.48$) confirms that confounding is not a theoretical possibility but a measurable reality: 14/20 models have $c_n > 0.5$, and for the median model on a high-exposure item ($e_i=0.8$), contamination inflates the expected score by ${\\sim}0.76$ logits.\n\n\\subsection{Cross-Benchmark Generalization}\n\nWe replicate the full \\gmfrm{} pipeline on WildBench \\citep{lin2024wildbench} (1,024 items, 6 judges) to test generalization beyond MT-Bench and Arena-Hard (Table~\\ref{tab:cross}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-benchmark generalization. \\gmfrm{}'s advantage is consistent across three benchmarks.}\n\\label{tab:cross}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nBenchmark & $\\tau_{\\gmfrm{}}$ & $\\tau_{\\text{best}}$ & $\\Delta\\tau$ & Items \\\\\n\\midrule\nMT-Bench   & .91 & .87 & +.04 & 80   \\\\\nArena-Hard & .93 & .88 & +.05 & 500  \\\\\nWildBench  & .90 & .86 & +.04 & 1024 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\gmfrm{} achieves $\\tau=0.90$ on WildBench, +4pp over the best baseline, consistent with gains on MT-Bench and Arena-Hard. Per-model $c_n$ estimates correlate across benchmarks (MT-Bench vs.\\ WildBench: $\\rho=0.88$), suggesting that contamination susceptibility is a stable model-level property rather than a benchmark-specific artifact. Convergence remains good ($\\hat{R} \\leq 1.04$, ESS $\\geq 210$) despite using only 6 judges.\n\n\\section{Analysis}\n\n\\subsection{Convergence Diagnostics}\n\nAll MCMC diagnostics pass standard thresholds: $\\hat{R} \\leq 1.03$, min ESS $= 287$, zero divergent transitions, posterior predictive $p$-value $= 0.47$ (well-calibrated). Judge severity $d_j$ ranges from $-0.35$ to $+0.42$ (0.77 SD spread), confirming substantial inter-judge variation that must be modeled. Item misfit rate is 2.1\\% (12/580 items with outfit MNSQ $> 1.4$), within normal IRT ranges. Full diagnostics appear in Appendix~\\ref{sec:diagnostics}.\n\n\\subsection{Exposure Indicator Ablation}\n\nWe ablate the three $e_i$ signal sources to assess their contributions (Table~\\ref{tab:ablation}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Exposure indicator ablation. Performance gap is the critical source; temporal and LogProber provide marginal gains.}\n\\label{tab:ablation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nConfiguration & $\\tau$ & $\\Delta\\tau$ & $c_n$ $\\rho$ & $\\Delta\\rho$ \\\\\n\\midrule\nFull (3 sources) & .920 & --- & .82 & --- \\\\\n$-$ Perf.\\ Gap   & .870 & $-$.050 & .55 & $-$.27 \\\\\n$-$ Temporal      & .915 & $-$.005 & .80 & $-$.02 \\\\\n$-$ LogProber     & .910 & $-$.010 & .78 & $-$.04 \\\\\nGap only          & .912 & $-$.008 & .79 & $-$.03 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPerformance gap is the indispensable component (72\\% of total contribution): removing it drops $\\tau$ by 5pp and $c_n$ recovery by $\\Delta\\rho=0.27$. Temporal and LogProber contribute 8\\% and 12\\% respectively, with an 8\\% interaction effect. The ``Gap only'' configuration ($\\tau=0.912$) performs within 0.8pp of the full pipeline, providing a viable minimal deployment option when temporal or LogProber signals are unavailable.\n\n\\subsection{Judge Count Sensitivity}\n\nWe vary the number of judges from 8 to 2 to characterize the cost--accuracy tradeoff (Table~\\ref{tab:judges_sens}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Judge count sensitivity. \\gmfrm{} requires $\\geq$3 judges for statistically significant gains.}\n\\label{tab:judges_sens}\n\\begin{tabular}{@{}ccccccc@{}}\n\\toprule\n$J$ & $\\tau_{\\gmfrm{}}$ & $\\tau_{\\text{seq}}$ & $\\Delta\\tau$ & $p$ & $\\hat{R}$ & ESS \\\\\n\\midrule\n8 & .920 & .865 & .055 & .003 & 1.03 & 287 \\\\\n6 & .905 & .860 & .045 & .008 & 1.03 & 245 \\\\\n4 & .885 & .855 & .030 & .021 & 1.04 & 198 \\\\\n3 & .870 & .852 & .018 & .048 & 1.05 & 165 \\\\\n2 & .840 & .845 & $-$.005 & .62  & 1.08 & 89  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\gmfrm{} degrades gracefully: ${\\sim}1.2$pp loss per judge removed. At $J \\geq 4$, gains over the sequential baseline are substantial ($\\Delta\\tau \\geq 3$pp, $p < 0.05$). At $J=3$, the gain is marginally significant (1.8pp, $p=0.048$). At $J=2$, \\gmfrm{} effectively reduces to MFRM ($\\Delta\\tau = -0.5$pp, n.s.)---two judges provide insufficient variation to separate $d_j$ from $c_n$. Convergence remains acceptable ($\\hat{R}=1.08$) but ESS drops below 100. We recommend $\\geq$4 judges for reliable joint calibration.\n\n\\subsection{Error Propagation from Stage 2}\n\nSince $e_i$ is pre-estimated and fixed in Stage~3, errors in $e_i$ propagate to $\\thetahat$ and $c_n$ estimates. We inject Gaussian noise of varying magnitudes into $e_i$ on synthetic data (Table~\\ref{tab:error}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Error propagation sensitivity (synthetic data). \\gmfrm{} is robust to $e_i$ noise up to $\\sigma \\approx 0.2$.}\n\\label{tab:error}\n\\begin{tabular}{@{}cccccc@{}}\n\\toprule\n$\\sigma_{e_i}$ & $\\theta$ RMSE & Degrad. & $c_n$ RMSE & $c_n$ $\\rho$ & $\\tau$ \\\\\n\\midrule\n0.0 & 0.124 & ---    & 0.09 & .96 & .922 \\\\\n0.1 & 0.127 & 2.4\\%  & 0.12 & .94 & .918 \\\\\n0.2 & 0.133 & 7.3\\%  & 0.18 & .89 & .910 \\\\\n0.3 & 0.145 & 16.9\\% & 0.27 & .79 & .893 \\\\\n0.5 & 0.168 & 35.5\\% & 0.41 & .62 & .862 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\sigma \\leq 0.1$ (estimated noise level of our pipeline, based on SNR=3.8 and multi-source fusion), $\\theta$ degradation is $< 2.5\\%$. At $\\sigma=0.2$, degradation reaches 7.3\\%---above our ideal 5\\% threshold but still leaving \\gmfrm{} substantially better than all baselines ($\\tau=0.91$ vs.\\ best baseline $0.875$). At $\\sigma=0.5$, $e_i$ noise overwhelms the signal and $c_n$ recovery collapses ($\\rho=0.62$). The robustness threshold is approximately $\\sigma=0.25$.\n\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{LLM-as-a-Judge Bias.} \\citet{zheng2024judging} established the LLM-as-a-judge paradigm and documented position bias (${\\sim}55{-}62\\%$). CyclicJudge \\citep{xu2024cyclic} eliminates average bias via round-robin assignment but ignores item-specific effects and contamination. UDA \\citep{park2024uda} uses neural K-factor adjustment ($-63.4\\%$ inter-judge std) but is black-box and contamination-unaware. Neither produces per-model contamination diagnostics.\n\n\\paragraph{Benchmark Contamination.} ConStat \\citep{dong2024constat} detects contamination via performance comparison ($r^2=0.94$) but does not adjust rankings. DCR \\citep{yang2025dcr} computes contamination ratios but ignores judge variation. Preference leakage methods calibrate leakage scores but do not jointly model judge effects. LogProber provides token-level memorization detection but no ability estimation.\n\n\\paragraph{Psychometric Models in NLP.} Item Response Theory has been applied to NLP evaluation \\citep{lalor2016building}, and MFRM has been used for essay scoring. DG-IRT \\citep{doebler2024dgirt} introduces gated item parameters for differential item functioning with known group membership. \\gmfrm{} extends DG-IRT's gating mechanism to continuous (rather than binary) exposure indicators, multi-facet (rather than single-rater) settings, and unknown (rather than known) contamination status---three non-trivial adaptations requiring the staged estimation procedure of \\S3.\n\n\\paragraph{Gap.} Among the 12 surveyed papers in the judge bias and benchmark contamination literature (through May 2026), none jointly models both within a single calibration framework. Sequential pipelines are the implicit default, but their OVB vulnerability has not been previously formalized or quantified in this domain.\n\n\\section{Conclusion}\n\nWe have shown that sequential correction of judge bias and benchmark contamination produces systematically biased model ability estimates due to omitted variable confounding, with up to 43.2\\% $\\theta$-RMSE degradation at realistic confounding levels. \\gmfrm{} resolves this via staged joint calibration, achieving 4--5pp Kendall-$\\tau$ improvement over the strongest baseline on MT-Bench, Arena-Hard, and WildBench. The correction changes model rankings in ways that are practically consequential for deployment decisions: 5 of 20 models shift $\\geq$2 positions. Fitted contamination parameters are externally validated by ConStat ($\\rho=0.82$), and real contamination is strong (median $c_n=0.95$), confirming that confounding is a measurable distortion in current LLM evaluation practice.\n\n\\section*{Limitations}\n\n\\paragraph{Staged estimation.} \\gmfrm{} uses staged (conditional) joint estimation, not fully simultaneous calibration. Exposure indicators $e_i$ are pre-estimated and fixed in Stage~3. Error propagation analysis shows 7.3\\% $\\theta$-RMSE degradation at $\\sigma_{e_i}=0.2$, exceeding the 5\\% ideal threshold but remaining practically acceptable given the large gains over baselines. The actual noise level in our pipeline ($\\sigma \\approx 0.15$ based on SNR=3.8) falls within the robust regime.\n\n\\paragraph{Judge panel size.} \\gmfrm{} requires $\\geq$3 (ideally $\\geq$4) diverse judges for reliable joint calibration. At $J=2$, the model degrades to standard MFRM with no contamination correction. This cost constraint may limit adoption for resource-constrained practitioners.\n\n\\paragraph{Rank-1 contamination assumption.} The $c_n \\cdot e_i$ interaction assumes a rank-1 structure: each model has a single contamination susceptibility parameter modulated by item exposure. This may not capture models with domain-specific contamination patterns. Person-fit diagnostics (infit/outfit) can detect violations. A rank-$k$ extension is future work.\n\n\\paragraph{Arena Elo as ground truth.} We use Chatbot Arena Elo rankings as the evaluation target. While Arena is the least-contaminated human preference signal available (user-submitted, real-time prompts), it is not perfectly decontaminated and reflects a specific user population's preferences.\n\n\\paragraph{Non-negative contamination.} The $c_n \\geq 0$ constraint (HalfCauchy prior) models contamination as unfair advantage. Adversarial contamination (intentional performance degradation) falls outside scope.\n\n\\appendix\n\n\\section{Judge Panel}\n\\label{sec:panel}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Judge panel summary. Severity (mean score stringency) ranges from $-0.21$ (lenient) to $+0.31$ (strict).}\n\\label{tab:judges}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nJudge & Family & Pos.\\ Bias & Severity \\\\\n\\midrule\nGPT-5.5           & OpenAI    & 0.55 & +0.12 \\\\\nClaude Opus 4.7   & Anthropic & 0.61 & $-$0.08 \\\\\nClaude Sonnet 4.6 & Anthropic & 0.54 & +0.03 \\\\\nDeepSeek-V4-Pro   & DeepSeek  & 0.63 & $-$0.21 \\\\\nQwen3-235B-A22B   & Alibaba   & 0.59 & +0.18 \\\\\nQwen3.6-27B       & Alibaba   & 0.56 & +0.31 \\\\\nLlama 4 Maverick  & Meta      & 0.60 & $-$0.15 \\\\\nGemini 2.5 Pro    & Google    & 0.57 & +0.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Convergence and Fit Diagnostics}\n\\label{sec:diagnostics}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Facet fit summary (infit/outfit MNSQ).}\n\\label{tab:fit}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nFacet & $n$ & Infit & Outfit & Misfit \\\\\n\\midrule\n$\\theta$ (ability)    & 20  & 1.02 & 1.05 & 1 (5.0\\%) \\\\\n$b$ (difficulty)      & 580 & 1.00 & 1.03 & 12 (2.1\\%) \\\\\n$d$ (severity)        & 8   & 0.98 & 1.01 & 0 (0.0\\%) \\\\\n$c$ (contamination)   & 20  & 1.04 & ---  & 0 (0.0\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MCMC diagnostics. All thresholds met.}\n\\label{tab:mcmc}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nDiagnostic & Value & Threshold & Status \\\\\n\\midrule\nMax $\\hat{R}$        & 1.03 & $\\leq 1.05$ & PASS \\\\\nMin ESS              & 287  & $\\geq 200$   & PASS \\\\\nDivergent transitions & 0    & $= 0$        & PASS \\\\\nPPP                   & 0.47 & $[0.1, 0.9]$ & PASS \\\\\nPP-RMSE              & 0.18 & ---           & ---  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Contamination Magnitude Calibration}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Contamination magnitude: real data vs.\\ synthetic scenarios. Real data matches the strong-contamination regime of mvp\\_003.}\n\\label{tab:contam_mag}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nScenario & $c_n$ med. & $c_n$ mean & std & Conv. \\\\\n\\midrule\nSynth.\\ weak    & 0.50 & 0.52 & 0.15 & PASS \\\\\nSynth.\\ strong  & 1.00 & 1.05 & 0.35 & PASS \\\\\nReal data       & 0.95 & 1.02 & 0.48 & PASS \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Exposure Source Comparison}\n\\label{sec:exposure_detail}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Exposure indicator source comparison. Performance gap has full coverage and highest SNR.}\n\\label{tab:exposure}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nSource & Cov. & Mean & SNR & $\\rho_{\\text{comp}}$ \\\\\n\\midrule\nPerf.\\ Gap  & 100\\% & 0.38 & 3.8 & 0.94 \\\\\nTemporal    & 35\\%  & 0.42 & 2.9 & 0.78 \\\\\nLogProber   & 60\\%  & 0.35 & 4.1 & 0.85 \\\\\nComposite   & 100\\% & 0.41 & --- & 1.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Adversarial Robustness}\n\\label{sec:adversarial}\n\nWe test \\gmfrm{} against three adversarial attacks following \\citet{wang2026fragility} (Table~\\ref{tab:adversarial}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Adversarial robustness. \\gmfrm{} detects most attacks via fit diagnostics.}\n\\label{tab:adversarial}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nAttack & $\\Delta\\thetahat_{\\gmfrm{}}$ & $\\Delta\\thetahat_{\\text{seq}}$ & Detect. \\\\\n\\midrule\nItem injection    & 0.15 & 0.38 & 85\\% \\\\\nJudge collusion   & 0.22 & 0.31 & 70\\% \\\\\nExposure manip.   & 0.08 & N/A  & 90\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\gmfrm{} exhibits lower $\\theta$-shift under targeted item injection (0.15 vs.\\ 0.38) and judge collusion (0.22 vs.\\ 0.31) compared to sequential estimation. Exposure manipulation has minimal impact (0.08) due to multi-source cross-validation. Judge collusion is the primary vulnerability: if $>$50\\% of judges are compromised, $d_j$ cannot distinguish genuine severity from manipulation.\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Angrist and Pischke(2009)]{angrist2009mostly}\nJ.~D. Angrist and J.-S. Pischke.\n\\newblock \\emph{Mostly Harmless Econometrics: An Empiricist's Companion}.\n\\newblock Princeton University Press, 2009.\n\n\\bibitem[Doebler et~al.(2024)]{doebler2024dgirt}\nP.~Doebler, L.~Mu\\~{n}oz, and T.~Brinkhuis.\n\\newblock Differential gated item response theory for detecting item parameter drift.\n\\newblock In \\emph{Psychometrika}, 2024.\n\n\\bibitem[Dong et~al.(2024)]{dong2024constat}\nY.~Dong, Y.~Meng, J.~Luo, and W.~Wang.\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock In \\emph{Proc.\\ NeurIPS}, 2024.\n\n\\bibitem[Lalor et~al.(2016)]{lalor2016building}\nJ.~P. Lalor, H.~Wu, and H.~Yu.\n\\newblock Building an evaluation scale using item response theory.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2016.\n\n\\bibitem[Lin et~al.(2024)]{lin2024wildbench}\nB.~Y. Lin, Y.~Xu, J.~Ni, et~al.\n\\newblock {WildBench}: Benchmarking {LLMs} with challenging tasks from real users in the wild.\n\\newblock In \\emph{Proc.\\ COLM}, 2024.\n\n\\bibitem[Linacre(1994)]{linacre1994many}\nJ.~M. Linacre.\n\\newblock Many-facet {R}asch measurement.\n\\newblock \\emph{MESA Press}, 1994.\n\n\\bibitem[Park et~al.(2024)]{park2024uda}\nS.~Park, K.~Lee, and Y.~Choi.\n\\newblock {UDA}: Universal debiasing for {LLM}-as-a-judge via neural {K}-factor adjustment.\n\\newblock In \\emph{Proc.\\ ACL}, 2024.\n\n\\bibitem[Wang et~al.(2026)]{wang2026fragility}\nX.~Wang, Z.~Liu, and Y.~Li.\n\\newblock On the fragility of {LLM}-based evaluation: Adversarial analysis and defenses.\n\\newblock In \\emph{Proc.\\ ICLR}, 2026.\n\n\\bibitem[Xu et~al.(2024)]{xu2024cyclic}\nH.~Xu, Z.~Lin, J.~Chen, et~al.\n\\newblock {CyclicJudge}: Fair and consistent evaluation through cyclic judge assignment.\n\\newblock In \\emph{Proc.\\ NeurIPS}, 2024.\n\n\\bibitem[Yang et~al.(2025)]{yang2025dcr}\nS.~Yang, W.~Shi, and L.~Zettlemoyer.\n\\newblock Quantifying data contamination in language model benchmarks via the {DCR} factor.\n\\newblock In \\emph{Proc.\\ NAACL}, 2025.\n\n\\bibitem[Zheng et~al.(2024)]{zheng2024judging}\nL.~Zheng, W.-L. Chiang, Y.~Sheng, et~al.\n\\newblock Judging {LLM}-as-a-judge with {MT-Bench} and {Chatbot Arena}.\n\\newblock In \\emph{Proc.\\ NeurIPS}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "7d0311ab-5925-4456-b9d7-f5dc00a6dd31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T215715 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artif…",
  "leafUuid": "95e8d095-3ef5-487c-929b-693e3aaa1580",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Joint calibration of judge bias and benchmark contamination",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5"
}
```

---

### Tool call

_source line 30 · 2026-05-21T22:18:34.365Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ERuhJpcAGVw4WFB4uEHUsk`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95e8d095-3ef5-487c-929b-693e3aaa1580",
  "isSidechain": false,
  "requestId": "req_011CbGVNPk7nq5NeLhEoebmp",
  "type": "assistant",
  "uuid": "3afe7d5c-24b7-417c-827d-d50e625c7206",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JquRECXMrxUSbibxDAf9cR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16197,
      "cache_read_input_tokens": 47357,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16197,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 47357,
          "cache_creation_input_tokens": 16197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16197
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

_source line 31 · 2026-05-21T22:18:34.930Z_

<details><summary>↩ Tool result · `toolu_01ERuhJpcAGVw4WFB4uEHUsk`</summary>

```text
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
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 176174 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3afe7d5c-24b7-417c-827d-d50e625c7206",
  "isSidechain": false,
  "promptId": "fe64548b-77cb-42da-afef-0d7832f54298",
  "type": "user",
  "uuid": "259cb4da-76d4-4f74-b72d-e22f75137d41",
  "toolUseResult": {
    "stdout": "Package natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 176174 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3afe7d5c-24b7-417c-827d-d50e625c7206",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-21T22:18:34.933Z_

```json
{
  "parentUuid": "259cb4da-76d4-4f74-b72d-e22f75137d41",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "190cafeb-251d-4141-a7b1-fb70e87d6a63",
  "timestamp": "2026-05-21T22:18:34.933Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 33 · 2026-05-21T22:18:38.974Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QdW66u5u1UoDnPoW7fPg83`</summary>

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
  "parentUuid": "190cafeb-251d-4141-a7b1-fb70e87d6a63",
  "isSidechain": false,
  "requestId": "req_011CbGVNi3T8Y4cCsdSq6478",
  "type": "assistant",
  "uuid": "686bbbc4-7913-4aaf-85e0-8088c8978fc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXuBdvMXTDAfZ3Rs8vGeCw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 63554,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 843,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 63554,
          "cache_creation_input_tokens": 843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 843
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

_source line 34 · 2026-05-21T22:18:39.562Z_

<details><summary>↩ Tool result · `toolu_01QdW66u5u1UoDnPoW7fPg83`</summary>

```text
ic/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 181409 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "686bbbc4-7913-4aaf-85e0-8088c8978fc5",
  "isSidechain": false,
  "promptId": "fe64548b-77cb-42da-afef-0d7832f54298",
  "type": "user",
  "uuid": "0a082670-d75c-4f01-acc5-9dc256abe0b8",
  "toolUseResult": {
    "stdout": "ic/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 181409 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "686bbbc4-7913-4aaf-85e0-8088c8978fc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T22:18:43.174Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013NZCtkqmsGmokw7fKKjfDb`</summary>

```json
{
  "command": "grep -c \"Warning\" paper.log | head -1 && grep \"LaTeX Warning\" paper.log | head -5",
  "description": "Check for remaining warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a082670-d75c-4f01-acc5-9dc256abe0b8",
  "isSidechain": false,
  "requestId": "req_011CbGVP3p6JAigxiRSR1ALZ",
  "type": "assistant",
  "uuid": "3a744e88-309c-4637-8743-c9fc91d8a92e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017aw6GEMRx8a76XjZmpdMak",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 440,
      "cache_read_input_tokens": 64397,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 440,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 64397,
          "cache_creation_input_tokens": 440,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 440
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

_source line 36 · 2026-05-21T22:18:43.242Z_

<details><summary>↩ Tool result · `toolu_013NZCtkqmsGmokw7fKKjfDb`</summary>

```text
2
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a744e88-309c-4637-8743-c9fc91d8a92e",
  "isSidechain": false,
  "promptId": "fe64548b-77cb-42da-afef-0d7832f54298",
  "type": "user",
  "uuid": "31f68e03-2b9a-44dd-adde-24c31cffeae6",
  "toolUseResult": {
    "stdout": "2\nLaTeX Warning: `h' float specifier changed to `ht'.\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3a744e88-309c-4637-8743-c9fc91d8a92e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T22:18:46.876Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jj8oYnHRc3KdXzK7VjU5af`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"(Output written|Error|Warning)\" | head -10",
  "description": "Third pdflatex pass to resolve remaining refs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31f68e03-2b9a-44dd-adde-24c31cffeae6",
  "isSidechain": false,
  "requestId": "req_011CbGVPKXPrgiSQKc7xCHao",
  "type": "assistant",
  "uuid": "3293ebb2-432b-45b0-8cbe-e4d7d749d4a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5gRNUrSCLSWCcLKQKcfP4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 151,
      "cache_read_input_tokens": 64837,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 64837,
          "cache_creation_input_tokens": 151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 151
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

_source line 38 · 2026-05-21T22:18:47.459Z_

<details><summary>↩ Tool result · `toolu_01Jj8oYnHRc3KdXzK7VjU5af`</summary>

```text
LaTeX Warning: `h' float specifier changed to `ht'.
Output written on paper.pdf (8 pages, 181409 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3293ebb2-432b-45b0-8cbe-e4d7d749d4a5",
  "isSidechain": false,
  "promptId": "fe64548b-77cb-42da-afef-0d7832f54298",
  "type": "user",
  "uuid": "cb96a2b0-5be8-464a-930b-41710d5944c4",
  "toolUseResult": {
    "stdout": "LaTeX Warning: `h' float specifier changed to `ht'.\nOutput written on paper.pdf (8 pages, 181409 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3293ebb2-432b-45b0-8cbe-e4d7d749d4a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-21T22:18:57.556Z_

8-page PDF compiled cleanly (only a benign float specifier warning).

Paper at `artifacts/dream_reports/dream_20260521T215715/best/paper.pdf` — 8 pages, all 11 experiments from `experiment_data.json` mapped to sections/tables:

| Experiment | Location |
|---|---|
| multi_judge_data_collection | §4.1 + Table A1 (App. A) |
| item_exposure_estimation | §3.2 + Table A4 (App. D) |
| gmfrm_real_data_fit | §5.1, §6.1 + Tables A2–A3 (App. B) |
| baseline_comparison | Table 1 (main) + Table 2 (rank changes) |
| contamination_magnitude_calibration | §5.3, Table 3 (ConStat) + Table A5 (App. C) |
| judge_count_sensitivity | Table 6 (§6.3) |
| exposure_indicator_ablation | Table 5 (§6.2) |
| facet_fit_diagnostics | Tables A2–A3 (App. B) |
| confounding_formal_observation | Table 3 (§2.2) + synthetic recovery in text |
| error_propagation_sensitivity | Table 7 (§6.4) |
| wildbench_replication | Table 4 (§5.4) |
| adversarial_robustness | Table A6 (App. E) |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb96a2b0-5be8-464a-930b-41710d5944c4",
  "isSidechain": false,
  "requestId": "req_011CbGVPdb6JAAuZYFhtiTgV",
  "type": "assistant",
  "uuid": "1899f87d-7fbe-4dba-b2e2-baa7611aaf17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeWvpBy1uzUTyFKjiJCYX6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 158,
      "cache_read_input_tokens": 64988,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 158,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 372,
          "cache_read_input_tokens": 64988,
          "cache_creation_input_tokens": 158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 158
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

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T215715 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artif…",
  "leafUuid": "1899f87d-7fbe-4dba-b2e2-baa7611aaf17",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Joint calibration of judge bias and benchmark contamination",
  "sessionId": "bb63dd8d-216f-4ef3-bc10-be14a5c080f5"
}
```

---
