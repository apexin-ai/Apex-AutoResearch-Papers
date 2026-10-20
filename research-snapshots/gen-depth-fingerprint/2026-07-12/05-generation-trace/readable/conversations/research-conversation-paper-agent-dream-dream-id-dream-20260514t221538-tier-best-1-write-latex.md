# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/6f50109c-746c-4b8f-986a-349fb461f53e.jsonl`
- **Structured JSON:** [`7f9823c2c535aabb7f22.json`](../../sessions/7f/7f9823c2c535aabb7f22.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T22:37:01.261Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T22:37:01.261Z",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：All three claims fully verified with repositioned framing. Contribution reads as clean empirical science: (1) ordinal depth estimation as new task formulation, (2) dual dynamics discovery (level/diversity drift vs shape stationarity) validated across generator families, reference models, and 7B+ scale — the split is about what features measure, not where they come from, (3) depth-aware curation with OLMo-1B downstream gains significant under multi-seed CIs. Paper anchored in OOD detection + model collapse + data quality literatures (30+ refs). Text length confound controlled — surface features track depth, not length. AAAI/EMNLP accept as strong empirical contribution with surprising finding + immediate utility.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T22:37:01.264Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T22:37:01.264Z",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-14T22:37:01.280Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：All three claims fully verified with repositioned framing. Contribution reads as clean empirical science: (1) ordinal depth estimation as new task formulation, (2) dual dynamics discovery (level/diversity drift vs shape stationarity) validated across generator families, reference models, and 7B+ scale — the split is about what features measure, not where they come from, (3) depth-aware curation with OLMo-1B downstream gains significant under multi-seed CIs. Paper anchored in OOD detection + model collapse + data quality literatures (30+ refs). Text length confound controlled — surface features track depth, not length. AAAI/EMNLP accept as strong empirical contribution with surprising finding + immediate utility.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "bc056985-7a91-4a57-bb85-6aa97ba3b608",
  "type": "user",
  "uuid": "b7a6b223-de92-48d9-b6f9-17b01a40ef0f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T22:37:01.279Z_

```json
{
  "parentUuid": "b7a6b223-de92-48d9-b6f9-17b01a40ef0f",
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
  "uuid": "42d71ff0-3e73-4d83-bdef-079f5a183407",
  "timestamp": "2026-05-14T22:37:01.279Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T22:37:01.280Z_

```json
{
  "parentUuid": "42d71ff0-3e73-4d83-bdef-079f5a183407",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "eda2b935-4138-45a3-b99c-7acee3122d76",
  "timestamp": "2026-05-14T22:37:01.280Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
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
  "aiTitle": "Generate simulated research paper for dream ID",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e"
}
```

---

### Assistant

_source line 7 · 2026-05-14T22:37:04.264Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eda2b935-4138-45a3-b99c-7acee3122d76",
  "isSidechain": false,
  "requestId": "req_011Cb3G7rSk1ZFibHtA49BzG",
  "type": "assistant",
  "uuid": "fe3dc150-a326-4db0-b579-a10004305eef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXv4AagGYCAtReJ4BBFkMU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11202
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

_source line 8 · 2026-05-14T22:37:05.559Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CyhCdxnDhGpCumbc1CWUmh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe3dc150-a326-4db0-b579-a10004305eef",
  "isSidechain": false,
  "requestId": "req_011Cb3G7rSk1ZFibHtA49BzG",
  "type": "assistant",
  "uuid": "198052cd-fe01-4b51-a177-88873a6f9491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXv4AagGYCAtReJ4BBFkMU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11202
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

_source line 9 · 2026-05-14T22:37:05.713Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N6TPW4V4HCd5JxiK7mZuT4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "198052cd-fe01-4b51-a177-88873a6f9491",
  "isSidechain": false,
  "requestId": "req_011Cb3G7rSk1ZFibHtA49BzG",
  "type": "assistant",
  "uuid": "0b44f5b0-08f1-4ffc-af9f-b89d95a10e5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXv4AagGYCAtReJ4BBFkMU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11202
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

_source line 10 · 2026-05-14T22:37:05.728Z_

<details><summary>↩ Tool result · `toolu_01N6TPW4V4HCd5JxiK7mZuT4`</summary>

```text
1	# Paper Framing — gen-depth-fingerprint
2	
3	## Target Venue
4	- Primary: AAAI 2027 (deadline: August 2, 2026)
5	- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4
6	- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)
7	
8	## Core Insight
9	Non-paraphrastic LLM generation chains exhibit **dual depth dynamics** that cross-cuts the surface/reference distinction: **level/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth (H₂), while **distributional shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁). Notably, entropy_mean is a reference-model feature that drifts (ρ=-0.68), showing the H₁/H₂ split is about what the feature measures (central tendency vs shape), not where it comes from (surface vs reference). This dual pattern creates a complementary feature space: drifting features provide ordinal depth signal, while stable shape features provide noise-robust class boundaries. The combination significantly outperforms either alone (macro-F1 0.82 vs 0.76/0.72).
10	
11	## Core Claims (3 条，均可证伪)
12	
13	**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).
14	
15	**Claim 2 — Dual Dynamics (Level vs Shape)**: Depth-dependent features split into two families by **what they measure**, not by their source (surface vs reference): (a) **level/diversity features** (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (H₂ — vocabulary impoverishment + entropy compression); (b) **shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁ — distributional shape is robust to recursive generation). This split cross-cuts the surface/reference boundary (entropy_mean is reference-derived but drifts). Full feature set (0.82) significantly outperforms surface-only (0.76) and reference-only (0.72) — the two dynamics are complementary for classification.
16	
17	**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.
18	
19	## Story Spine
20	
21	**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).
22	
23	**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.
24	
25	**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **dual dynamics**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth (H₂), while distributional shape features (entropy variance, tail decay) remain near-stationary (H₁). This split is about **what the feature measures** (central tendency vs shape), not where it comes from — overturning the naive expectation that "reference-model features = robust, surface features = fragile." The dual pattern has practical value: drifting features provide ordinal depth signal, stable shape features provide noise-robust decision boundaries, and their combination yields the best depth estimation for risk-stratified data curation.
26	
27	**Headline result template**: "On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines."
28	
29	## Anticipated Reviewer Concerns
30	
31	**RC1 — "Is this just vocabulary impoverishment?"**: Surface features alone achieve 0.76 macro-F1, but full features achieve 0.82 (p<0.001). We don't claim reference features are "better" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). The dual dynamics finding is itself a scientific contribution. Note: "fingerprint" in the paper refers to the full feature vector's combination, not just reference-model features.
32	
33	**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.
34	
35	**RC2 — "Does this generalize beyond Pythia?"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).
36	
37	**RC3 — "Is 3-class sufficient? Why not finer-grained?"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.
38	
39	**RC4 — "How realistic are single-model chains?"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).
40	
41	**RC5 — "What about human editing / post-processing?"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).
42	
43	**RC6 — "Ecological validity — continuation vs real web content"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).
44	
45	**RC8 — "Aren't these just OOD detection features?"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.
46	
47	**RC9 — "Only ≤2.8B generators — does this transfer to frontier scale?"**: All 5 current generators ≤2.8B. Frontier models (7B+) produce more fluent text that may compress depth signal. → Add at least one 7B+ generator (plan_014). If depth signal significantly weaker at scale → honest limitation with analysis of why; if comparable → strong generalization evidence.
48	
49	**RC10 — "Text length confound"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.
50	
51	**RC11 — "Downstream utility — single run, no CIs"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).
52	
53	## Contribution Positioning (Dream D006 insight)
54	The contribution is **primarily empirical and conceptual**, not methodological. The features (NLL summary statistics) and classifier (XGBoost) are standard — the novelty lies in:
55	1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection
56	2. **Empirical discovery**: Dual dynamics (level/diversity drift vs shape stationarity) cross-cutting surface/reference boundary
57	3. **Practical application**: Risk-stratified data curation outperforming binary filtering
58	
59	Do NOT overclaim "distributional fingerprinting" as a new method. Position the paper as empirical science with a novel task formulation and a surprising empirical finding. The H1/H2 framework is an empirical validation extending attractor cycle theory to non-paraphrastic chains, not a major theoretical contribution.
60	
61	Related work must expand to 30+ references covering: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory (Alemohammad et al., Dohmatob et al., Gerstgrasser et al., Guo et al.), OOD detection (Hendrycks & Gimpel), data quality scoring (DSIR, QuRating, CCNet), watermarking (Kirchenbauer et al.), vocabulary diversity (Guo et al. 2024, Padmakumar & He 2024, Holtzman et al. 2020).
62	
63	## Venue Fit
64	- AAAI 2027: Fit as empirical + conceptual contribution — novel task formulation (depth estimation) + surprising empirical finding (dual dynamics) + practical application (data curation). Must position as empirical science, not methodology paper.
65	- EMNLP 2026: Excellent fit — directly addresses special theme "New Missions for NLP Research" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work. Empirical/conceptual contributions better received here than AAAI.
66	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b44f5b0-08f1-4ffc-af9f-b89d95a10e5c",
  "isSidechain": false,
  "promptId": "bc056985-7a91-4a57-bb85-6aa97ba3b608",
  "type": "user",
  "uuid": "94bff9be-2399-4198-9b31-c9952e3aa63f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/paper_framing.md",
      "content": "# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- Primary: AAAI 2027 (deadline: August 2, 2026)\n- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **dual depth dynamics** that cross-cuts the surface/reference distinction: **level/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth (H₂), while **distributional shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁). Notably, entropy_mean is a reference-model feature that drifts (ρ=-0.68), showing the H₁/H₂ split is about what the feature measures (central tendency vs shape), not where it comes from (surface vs reference). This dual pattern creates a complementary feature space: drifting features provide ordinal depth signal, while stable shape features provide noise-robust class boundaries. The combination significantly outperforms either alone (macro-F1 0.82 vs 0.76/0.72).\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).\n\n**Claim 2 — Dual Dynamics (Level vs Shape)**: Depth-dependent features split into two families by **what they measure**, not by their source (surface vs reference): (a) **level/diversity features** (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (H₂ — vocabulary impoverishment + entropy compression); (b) **shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁ — distributional shape is robust to recursive generation). This split cross-cuts the surface/reference boundary (entropy_mean is reference-derived but drifts). Full feature set (0.82) significantly outperforms surface-only (0.76) and reference-only (0.72) — the two dynamics are complementary for classification.\n\n**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.\n\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **dual dynamics**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth (H₂), while distributional shape features (entropy variance, tail decay) remain near-stationary (H₁). This split is about **what the feature measures** (central tendency vs shape), not where it comes from — overturning the naive expectation that \"reference-model features = robust, surface features = fragile.\" The dual pattern has practical value: drifting features provide ordinal depth signal, stable shape features provide noise-robust decision boundaries, and their combination yields the best depth estimation for risk-stratified data curation.\n\n**Headline result template**: \"On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.76 macro-F1, but full features achieve 0.82 (p<0.001). We don't claim reference features are \"better\" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). The dual dynamics finding is itself a scientific contribution. Note: \"fingerprint\" in the paper refers to the full feature vector's combination, not just reference-model features.\n\n**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\n\n**RC3 — \"Is 3-class sufficient? Why not finer-grained?\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\n\n**RC4 — \"How realistic are single-model chains?\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\n\n**RC5 — \"What about human editing / post-processing?\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\n\n**RC6 — \"Ecological validity — continuation vs real web content\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.\n\n**RC9 — \"Only ≤2.8B generators — does this transfer to frontier scale?\"**: All 5 current generators ≤2.8B. Frontier models (7B+) produce more fluent text that may compress depth signal. → Add at least one 7B+ generator (plan_014). If depth signal significantly weaker at scale → honest limitation with analysis of why; if comparable → strong generalization evidence.\n\n**RC10 — \"Text length confound\"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.\n\n**RC11 — \"Downstream utility — single run, no CIs\"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).\n\n## Contribution Positioning (Dream D006 insight)\nThe contribution is **primarily empirical and conceptual**, not methodological. The features (NLL summary statistics) and classifier (XGBoost) are standard — the novelty lies in:\n1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection\n2. **Empirical discovery**: Dual dynamics (level/diversity drift vs shape stationarity) cross-cutting surface/reference boundary\n3. **Practical application**: Risk-stratified data curation outperforming binary filtering\n\nDo NOT overclaim \"distributional fingerprinting\" as a new method. Position the paper as empirical science with a novel task formulation and a surprising empirical finding. The H1/H2 framework is an empirical validation extending attractor cycle theory to non-paraphrastic chains, not a major theoretical contribution.\n\nRelated work must expand to 30+ references covering: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory (Alemohammad et al., Dohmatob et al., Gerstgrasser et al., Guo et al.), OOD detection (Hendrycks & Gimpel), data quality scoring (DSIR, QuRating, CCNet), watermarking (Kirchenbauer et al.), vocabulary diversity (Guo et al. 2024, Padmakumar & He 2024, Holtzman et al. 2020).\n\n## Venue Fit\n- AAAI 2027: Fit as empirical + conceptual contribution — novel task formulation (depth estimation) + surprising empirical finding (dual dynamics) + practical application (data curation). Must position as empirical science, not methodology paper.\n- EMNLP 2026: Excellent fit — directly addresses special theme \"New Missions for NLP Research\" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work. Empirical/conceptual contributions better received here than AAAI.\n",
      "numLines": 66,
      "startLine": 1,
      "totalLines": 66
    }
  },
  "sourceToolAssistantUUID": "0b44f5b0-08f1-4ffc-af9f-b89d95a10e5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T22:37:05.815Z_

<details><summary>↩ Tool result · `toolu_01CyhCdxnDhGpCumbc1CWUmh`</summary>

```text
1	[
2	  {
3	    "name": "feature_ablation_and_trend",
4	    "description": "Three-part analysis on MVP data (4609 records, Pythia-2.8B generator, Pythia-410M reference). (A) Feature ablation: reference-only vs surface-only vs full. (B) H1/H2 trend analysis per feature. (C) Perplexity pre-validation for Claim 3.\n",
5	    "results": {
6	      "full_macro_f1": 0.8204,
7	      "surface_only_f1": 0.7628,
8	      "reference_only_f1": 0.7187,
9	      "full_vs_surface_f1_gap": 0.058,
10	      "full_vs_reference_f1_gap": 0.102,
11	      "ref_vs_surf_bootstrap_ci": "[0.706,0.733] vs [0.747,0.774]",
12	      "h2_features": "entropy_mean, ttr, hapax_ratio",
13	      "h1_features": "tail_decay, entropy_std, entropy_max, entropy_min",
14	      "entropy_mean_slope_r2": 0.91,
15	      "ttr_slope_r2": 0.88,
16	      "hapax_ratio_slope_r2": 0.85,
17	      "entropy_std_slope_r2": 0.12,
18	      "tail_decay_slope_r2": 0.09,
19	      "median_ppl_by_depth": [
20	        13.5,
21	        4.96,
22	        3.0,
23	        2.07,
24	        1.72
25	      ],
26	      "ppl_depth_spearman": -0.97
27	    },
28	    "tables": [
29	      {
30	        "name": "Table 1: Feature Ablation Results (3-class)",
31	        "columns": [
32	          "Feature Set",
33	          "Features",
34	          "Macro-F1",
35	          "gen-0 F1",
36	          "gen-1 F1",
37	          "gen-2+ F1",
38	          "CV std"
39	        ],
40	        "rows": [
41	          [
42	            "Reference-only",
43	            "entropy_{mean,std,min,max}, tail_decay",
44	            0.72,
45	            0.88,
46	            0.63,
47	            0.65,
48	            0.021
49	          ],
50	          [
51	            "Surface-only",
52	            "ttr, hapax_ratio",
53	            0.76,
54	            0.9,
55	            0.69,
56	            0.7,
57	            0.019
58	          ],
59	          [
60	            "Full",
61	            "All 7 features",
62	            0.82,
63	            0.95,
64	            0.76,
65	            0.79,
66	            0.013
67	          ]
68	        ]
69	      },
70	      {
71	        "name": "Table 2: H1/H2 Feature Trend Analysis (linear regression slope per depth)",
72	        "columns": [
73	          "Feature",
74	          "Slope",
75	          "R²",
76	          "Category",
77	          "Interpretation"
78	        ],
79	        "rows": [
80	          [
81	            "entropy_mean",
82	            -0.18,
83	            0.91,
84	            "H2-drift",
85	            "Reference-model surprise decreases monotonically"
86	          ],
87	          [
88	            "ttr",
89	            -0.024,
90	            0.88,
91	            "H2-drift",
92	            "Lexical diversity declines with depth"
93	          ],
94	          [
95	            "hapax_ratio",
96	            -0.019,
97	            0.85,
98	            "H2-drift",
99	            "Singleton word ratio drops"
100	          ],
101	          [
102	            "entropy_std",
103	            0.003,
104	            0.12,
105	            "H1-stationary",
106	            "Surprise variance near-constant"
107	          ],
108	          [
109	            "entropy_max",
110	            0.008,
111	            0.15,
112	            "H1-stationary",
113	            "Tail surprise stable"
114	          ],
115	          [
116	            "entropy_min",
117	            -0.005,
118	            0.11,
119	            "H1-stationary",
120	            "Floor surprise stable"
121	          ],
122	          [
123	            "tail_decay",
124	            0.002,
125	            0.09,
126	            "H1-stationary",
127	            "Distributional shape robust"
128	          ]
129	        ]
130	      }
131	    ],
132	    "figures": [],
133	    "analysis": "The ablation gap is central to the paper's contribution positioning. The full_vs_surface gap (0.058) and full_vs_reference gap (0.102) confirm that both feature families carry non-redundant signal. Critically, entropy_mean is reference-derived but drifts (H2) — this cross-cuts the surface/reference boundary and is the headline finding. The H1/H2 split is clean: R²≥0.85 for drift features, R²≤0.15 for stationary features. This is the empirical backbone of Claim 2.\n\n\n[ACTUAL — plan-001-fix completed] Full > surface > reference ablation gap confirmed. Surface features (TTR, hapax_ratio) are stronger than initially expected (0.76 vs prior dream's 0.63) because vocabulary impoverishment is a robust, high-signal depth cue. Reference features alone achieve 0.72 — weaker than surface alone, overturning the naive expectation that reference features dominate. But their complementary value is clear: full set (0.82) significantly exceeds both subsets. The key insight is that entropy_mean (reference-derived) is an H2/drift feature while entropy_std/max/min (also reference-derived) are H1/stationary — the split is about what's measured (level vs shape), not the feature source. Perplexity monotonically decreases with depth (13.5→1.7) confirming that deeper text is progressively more predictable under the reference model — strong pre-validation for Claim 3's downstream utility hypothesis.\n"
134	  },
135	  {
136	    "name": "cross_generator_evaluation",
137	    "description": "5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B, Qwen3-1.7B-Base, Qwen3-0.6B-Base. 1000 seeds × 5 generators × 5 depths = 25K chains. Leave-one-generator-out (LOGO) CV. Pythia-410M as reference model for all.\n",
138	    "results": {
139	      "logo_macro_f1_mean": 0.74,
140	      "logo_macro_f1_std": 0.03,
141	      "logo_gen0_f1_mean": 0.87,
142	      "logo_gen1_f1_mean": 0.68,
143	      "logo_gen2plus_f1_mean": 0.7,
144	      "in_distribution_pooled_macro_f1": 0.83,
145	      "pythia_2_8b_held_out_f1": 0.77,
146	      "pythia_1b_held_out_f1": 0.76,
147	      "olmo2_held_out_f1": 0.73,
148	      "qwen3_1_7b_held_out_f1": 0.72,
149	      "qwen3_0_6b_held_out_f1": 0.7,
150	      "leave_one_family_out_pythia_f1": 0.71,
151	      "leave_one_family_out_qwen_f1": 0.74,
152	      "total_chains": 23800,
153	      "attrition_rate_pct": 4.8
154	    },
155	    "tables": [
156	      {
157	        "name": "Table 3: Leave-One-Generator-Out Cross-Validation",
158	        "columns": [
159	          "Held-out Generator",
160	          "Family",
161	          "Params",
162	          "Macro-F1",
163	          "gen-0 F1",
164	          "gen-1 F1",
165	          "gen-2+ F1"
166	        ],
167	        "rows": [
168	          [
169	            "Pythia-2.8B",
170	            "Pythia",
171	            "2.8B",
172	            0.77,
173	            0.9,
174	            0.71,
175	            0.72
176	          ],
177	          [
178	            "Pythia-1B",
179	            "Pythia",
180	            "1B",
181	            0.76,
182	            0.89,
183	            0.7,
184	            0.71
185	          ],
186	          [
187	            "OLMo-2-0425-1B",
188	            "OLMo",
189	            "1.5B",
190	            0.73,
191	            0.86,
192	            0.67,
193	            0.68
194	          ],
195	          [
196	            "Qwen3-1.7B-Base",
197	            "Qwen",
198	            "1.7B",
199	            0.72,
200	            0.85,
201	            0.66,
202	            0.67
203	          ],
204	          [
205	            "Qwen3-0.6B-Base",
206	            "Qwen",
207	            "0.6B",
208	            0.7,
209	            0.83,
210	            0.63,
211	            0.65
212	          ],
213	          [
214	            "Mean ± std",
215	            "—",
216	            "—",
217	            "0.74 ± 0.03",
218	            "0.87 ± 0.03",
219	            "0.68 ± 0.03",
220	            "0.70 ± 0.03"
221	          ]
222	        ]
223	      },
224	      {
225	        "name": "Table 4: Per-Generator In-Distribution 5-Fold CV",
226	        "columns": [
227	          "Generator",
228	          "Macro-F1",
229	          "CV std"
230	        ],
231	        "rows": [
232	          [
233	            "Pythia-2.8B",
234	            0.84,
235	            0.014
236	          ],
237	          [
238	            "Pythia-1B",
239	            0.82,
240	            0.016
241	          ],
242	          [
243	            "OLMo-2-0425-1B",
244	            0.83,
245	            0.015
246	          ],
247	          [
248	            "Qwen3-1.7B-Base",
249	            0.82,
250	            0.017
251	          ],
252	          [
253	            "Qwen3-0.6B-Base",
254	            0.8,
255	            0.02
256	          ],
257	          [
258	            "Pooled (all 5)",
259	            0.83,
260	            0.012
261	          ]
262	        ]
263	      },
264	      {
265	        "name": "Table 4b: Leave-One-Family-Out",
266	        "columns": [
267	          "Held-out Family",
268	          "Generators Held Out",
269	          "Macro-F1"
270	        ],
271	        "rows": [
272	          [
273	            "Pythia",
274	            "Pythia-2.8B + Pythia-1B",
275	            0.71
276	          ],
277	          [
278	            "Qwen",
279	            "Qwen3-1.7B + Qwen3-0.6B",
280	            0.74
281	          ],
282	          [
283	            "OLMo",
284	            "OLMo-2-0425-1B",
285	            0.73
286	          ]
287	        ]
288	      }
289	    ],
290	    "figures": [],
291	    "analysis": "LOGO F1=0.74 is the centerpiece of Claim 1. The ≥0.70 threshold is cleared with margin. Pythia-family slight advantage (0.76-0.77) is a limitation to discuss honestly: Pythia-410M reference model shares tokenizer/architecture with generators. Leave-one-family-out (0.71) still passes the 0.70 threshold, confirming depth signal is generation-process-intrinsic, not family-artifact. The gen-1 vs gen-2+ boundary remains the classification bottleneck across all generators.\n\n\nLOGO mean 0.74 (within [0.70, 0.78] best range) reflects cross-generator generalization grounded in actual plan-001 performance (0.82 in-dist). The ~0.09 drop from in-distribution to LOGO is expected: each generator has its own distributional signature, and training without the held-out generator forces reliance on transfer of the depth-drift pattern. Pythia-family generators transfer best to each other (0.76-0.77) due to shared pretraining distribution (The Pile). Cross-family transfer (Pythia→Qwen, Pythia→OLMo) drops to 0.70-0.73 because the reference model (Pythia-410M) has different baseline expectations for text from non-Pythia generators, adding noise to features. Qwen3-0.6B-Base is hardest (0.70) because its small capacity produces lower-quality text that drifts faster at gen-1, making the depth ordering harder to predict from larger-model-trained classifiers. Leave-one-family-out for Pythia (train on OLMo+Qwen, test on Pythia-2.8B+1B) gives 0.71, confirming the signal is not Pythia-specific. Attrition slightly higher (4.8%) due to Qwen models' less stable generation at depth 4.\n"
292	  },
293	  {
294	    "name": "cross_family_reference_model",
295	    "description": "Re-extract features using non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) on plan_002 data. Key falsification test: does entropy_mean H2 drift persist with non-Pythia reference? If not, dual dynamics is Pythia-specific artifact.\n",
296	    "results": {
297	      "pythia_410m_ref_macro_f1": 0.83,
298	      "olmo2_1b_ref_macro_f1": 0.77,
299	      "qwen3_06b_ref_macro_f1": 0.74,
300	      "entropy_mean_depth_rho_pythia": -0.72,
301	      "entropy_mean_depth_rho_olmo": -0.65,
302	      "entropy_mean_depth_rho_qwen": -0.58,
303	      "cross_ref_mean_rho": -0.65,
304	      "entropy_std_depth_rho_pythia": -0.08,
305	      "entropy_std_depth_rho_olmo": -0.11,
306	      "entropy_std_depth_rho_qwen": -0.06,
307	      "feature_correlation_pythia_olmo_entropy_mean": 0.79,
308	      "feature_correlation_pythia_qwen_entropy_mean": 0.74,
309	      "h2_drift_confirmed_all_refs": true,
310	      "h1_stationarity_confirmed_all_refs": true,
311	      "ensemble_3refs_macro_f1": 0.85
312	    },
313	    "tables": [
314	      {
315	        "name": "Table 5: Reference Model Comparison (pooled 5-generator data)",
316	        "columns": [
317	          "Reference Model",
318	          "Family",
319	          "Params",
320	          "Macro-F1",
321	          "gen-0 F1",
322	          "gen-1 F1",
323	          "gen-2+ F1"
324	        ],
325	        "rows": [
326	          [
327	            "Pythia-410M",
328	            "Pythia",
329	            "410M",
330	            0.83,
331	            0.94,
332	            0.77,
333	            0.79
334	          ],
335	          [
336	            "OLMo-2-1B",
337	            "OLMo",
338	            "1B",
339	            0.77,
340	            0.89,
341	            0.7,
342	            0.72
343	          ],
344	          [
345	            "Qwen3-0.6B-Base",
346	            "Qwen",
347	            "0.6B",
348	            0.74,
349	            0.86,
350	            0.67,
351	            0.69
352	          ],
353	          [
354	            "Ensemble (3 refs)",
355	            "Mixed",
356	            "—",
357	            0.85,
358	            0.95,
359	            0.79,
360	            0.81
361	          ]
362	        ]
363	      },
364	      {
365	        "name": "Table 6: Entropy Feature Depth Correlation (Spearman ρ) by Reference Model",
366	        "columns": [
367	          "Feature",
368	          "Pythia-410M",
369	          "OLMo-2-1B",
370	          "Qwen3-0.6B",
371	          "H1/H2 Classification"
372	        ],
373	        "rows": [
374	          [
375	            "entropy_mean",
376	            -0.72,
377	            -0.65,
378	            -0.58,
379	            "H2-drift"
380	          ],
381	          [
382	            "entropy_std",
383	            -0.08,
384	            -0.11,
385	            -0.06,
386	            "H1-stationary"
387	          ],
388	          [
389	            "entropy_max",
390	            0.05,
391	            0.03,
392	            0.07,
393	            "H1-stationary"
394	          ],
395	          [
396	            "entropy_min",
397	            -0.1,
398	            -0.07,
399	            -0.09,
400	            "H1-stationary"
401	          ],
402	          [
403	            "tail_decay",
404	            0.04,
405	            0.06,
406	            0.03,
407	            "H1-stationary"
408	          ]
409	        ]
410	      },
411	      {
412	        "name": "Table 6b: Cross-Reference Feature Correlation (Spearman ρ)",
413	        "columns": [
414	          "Feature",
415	          "Pythia↔OLMo",
416	          "Pythia↔Qwen",
417	          "OLMo↔Qwen"
418	        ],
419	        "rows": [
420	          [
421	            "entropy_mean",
422	            0.79,
423	            0.74,
424	            0.77
425	          ],
426	          [
427	            "entropy_std",
428	            0.76,
429	            0.71,
430	            0.73
431	          ],
432	          [
433	            "tail_decay",
434	            0.68,
435	            0.63,
436	            0.66
437	          ]
438	        ]
439	      }
440	    ],
441	    "figures": [],
442	    "analysis": "This experiment eliminates the most dangerous threat to the paper: that dual dynamics is a Pythia artifact. With all three reference models showing consistent H2 drift for entropy_mean (ρ range -0.58 to -0.72) and H1 stationarity for shape features (|ρ|<0.12), the level/shape framework is confirmed as generation-intrinsic. The 3-ref ensemble (0.85) exceeding any single ref confirms that diverse reference perspectives capture complementary drift information. For the paper, Table 6 is the most important evidence for the \"what it measures, not where it comes from\" argument.\n\n\nentropy_mean ρ with depth ranges from -0.58 to -0.72 across reference models (mean -0.65, within [-0.75, -0.55] best range), confirming H2 drift is generation-intrinsic, not Pythia-specific. All three reference models detect monotonic entropy_mean decrease with depth because any well-trained LM assigns progressively higher probability (lower NLL) to deeper text — the text literally becomes more generic/predictable as generation recurses. Pythia-410M gives strongest signal (-0.72) because it was optimized for this pipeline and its 410M capacity is well-calibrated to detect drift (large enough to model human text, small enough to be \"surprised\" by generator deviations). OLMo (-0.65) and Qwen (-0.58) are noisier because their different pretraining distributions create different baselines. Crucially, entropy_std remains near-zero correlation with depth across all three models (|ρ|<0.12), confirming shape stationarity (H1) is also reference-model-agnostic. The dual dynamics is a property of the recursive generation process, not the measurement instrument. This is the key falsification test for Claim 2 — it passes.\n"
443	  },
444	  {
445	    "name": "downstream_utility",
446	    "description": "Fine-tune OLMo-1B (avoiding Pythia-410M circularity) on depth-stratified subsets. ≥3 random seeds with bootstrap CIs. Compare depth-aware filtering vs FastDetectGPT and LD-Score binary baselines. Sample-count-matched comparison to control data size confound.\n",
447	    "results": {
448	      "downstream_model": "OLMo-1B",
449	      "n_seeds": 5,
450	      "ppl_gen0_only_mean": 31.2,
451	      "ppl_gen0_only_ci": [
452	        30.4,
453	        32.0
454	      ],
455	      "ppl_gen1_only_mean": 33.8,
456	      "ppl_gen1_only_ci": [
457	        32.9,
458	        34.7
459	      ],
460	      "ppl_gen2_only_mean": 38.5,
461	      "ppl_gen2_only_ci": [
462	        37.2,
463	        39.8
464	      ],
465	      "ppl_gen3_only_mean": 43.1,
466	      "ppl_gen3_only_ci": [
467	        41.5,
468	        44.7
469	      ],
470	      "ppl_gen4_only_mean": 47.6,
471	      "ppl_gen4_only_ci": [
472	        45.8,
473	        49.4
474	      ],
475	      "depth_quality_spearman": 0.74,
476	      "ppl_depth_filtered_gen01_mean": 32.1,
477	      "ppl_depth_filtered_gen01_ci": [
478	        31.3,
479	        32.9
480	      ],
481	      "ppl_binary_fastdetectgpt_mean": 36.8,
482	      "ppl_binary_fastdetectgpt_ci": [
483	        35.6,
484	        38.0
485	      ],
486	      "ppl_binary_ldscore_mean": 37.2,
487	      "ppl_binary_ldscore_ci": [
488	        35.9,
489	        38.5
490	      ],
491	      "ppl_no_filter_mean": 40.1,
492	      "depth_filter_vs_binary_improvement_pct": 13.2,
493	      "data_retained_depth_filter_pct": 44,
494	      "data_retained_binary_pct": 30,
495	      "ppl_size_matched_depth_filter": 33.0,
496	      "ppl_size_matched_binary": 37.0,
497	      "size_matched_ci_non_overlapping": true
498	    },
499	    "tables": [
500	      {
501	        "name": "Table 7: Downstream Perplexity by Training Data Depth (OLMo-1B, 5 seeds)",
502	        "columns": [
503	          "Training Data",
504	          "PPL Mean",
505	          "95% CI",
506	          "Samples"
507	        ],
508	        "rows": [
509	          [
510	            "gen-0 only",
511	            31.2,
512	            "[30.4, 32.0]",
513	            "~4800"
514	          ],
515	          [
516	            "gen-1 only",
517	            33.8,
518	            "[32.9, 34.7]",
519	            "~4700"
520	          ],
521	          [
522	            "gen-2 only",
523	            38.5,
524	            "[37.2, 39.8]",
525	            "~4400"
526	          ],
527	          [
528	            "gen-3 only",
529	            43.1,
530	            "[41.5, 44.7]",
531	            "~4100"
532	          ],
533	          [
534	            "gen-4 only",
535	            47.6,
536	            "[45.8, 49.4]",
537	            "~3800"
538	          ]
539	        ]
540	      },
541	      {
542	        "name": "Table 8: Depth-Aware vs Binary Filtering (OLMo-1B, 5 seeds)",
543	        "columns": [
544	          "Method",
545	          "PPL Mean",
546	          "95% CI",
547	          "Data Retained",
548	          "Δ vs No-Filter"
549	        ],
550	        "rows": [
551	          [
552	            "Depth-filtered (gen-0+1)",
553	            32.1,
554	            "[31.3, 32.9]",
555	            "44%",
556	            "-20.0%"
557	          ],
558	          [
559	            "FastDetectGPT binary",
560	            36.8,
561	            "[35.6, 38.0]",
562	            "30%",
563	            "-8.2%"
564	          ],
565	          [
566	            "LD-Score binary",
567	            37.2,
568	            "[35.9, 38.5]",
569	            "28%",
570	            "-7.2%"
571	          ],
572	          [
573	            "No filtering",
574	            40.1,
575	            "[38.8, 41.4]",
576	            "100%",
577	            "—"
578	          ]
579	        ]
580	      },
581	      {
582	        "name": "Table 8b: Size-Matched Comparison (subsample to equal data count)",
583	        "columns": [
584	          "Method",
585	          "Matched Count",
586	          "PPL Mean",
587	          "95% CI"
588	        ],
589	        "rows": [
590	          [
591	            "Depth-filtered (subsampled)",
592	            "~5500",
593	            33.0,
594	            "[32.1, 33.9]"
595	          ],
596	          [
597	            "Binary-filtered",
598	            "~5500",
599	            37.0,
600	            "[35.8, 38.2]"
601	          ],
602	          [
603	            "CIs non-overlapping",
604	            "—",
605	            "YES",
606	            "—"
607	          ]
608	        ]
609	      }
610	    ],
611	    "figures": [],
612	    "analysis": "This is the practical punchline. The 13.2% improvement with CIs non-overlapping under size-matching establishes that depth-aware filtering provides genuine data quality advantage, not just a data quantity effect. gen-1 text is \"good enough\" for training (PPL 33.8 vs gen-0's 31.2 — 8% gap), but gen-2+ is harmful (PPL 38.5+, >23% worse than gen-0). Binary detectors force an all-or-nothing choice and discard useful gen-1 content. This directly validates Claim 3 under the strengthened protocol (OLMo-1B, 5 seeds, CIs, size-matched).\n\n\nOLMo-1B perplexity increases monotonically with training depth (31.2→47.6) because deeper text has compounded distributional drift from human text — fine-tuning on it shifts OLMo-1B's distribution away from the human test set. The absolute PPL values are higher than the previous dream (which used Pythia-410M) because OLMo-1B is a stronger model with higher baseline expectations. Spearman ρ=0.74 (within [0.65, 0.85]) reflects individual sample variance within depth classes. Depth-aware filtering (keep gen-0+gen-1, PPL=32.1) outperforms binary baselines (~36.8-37.2) by 13.2% (within [8, 20] range) because binary detectors discard all synthetic text — including useful gen-1 content that is distributionally near-human. Binary filters retain only ~30% of data (mostly gen-0) while depth filtering retains 44% (gen-0 + gen-1), providing more and better training data. The size-matched comparison is critical: even when subsampling depth-filtered data to match binary filter count, depth filtering still wins (33.0 vs 37.0, CIs non-overlapping) — confirming the advantage is data quality, not quantity. Using OLMo-1B eliminates the Pythia reference model circularity concern. 5-seed bootstrap CIs are tight enough to establish significance.\n"
613	  },
614	  {
615	    "name": "prompt_type_comparison",
616	    "description": "Compare continuation vs elaboration vs inspired_rewriting chains. 1000 seeds, Pythia-2.8B, 5 depths × 3 prompt types.\n",
617	    "results": {
618	      "continuation_macro_f1": 0.82,
619	      "elaboration_macro_f1": 0.77,
620	      "inspired_rewriting_macro_f1": 0.69,
621	      "continuation_entropy_drift_per_depth": 0.17,
622	      "elaboration_entropy_drift_per_depth": 0.13,
623	      "inspired_rewriting_entropy_drift_per_depth": 0.08,
624	      "cross_prompt_type_macro_f1": 0.71,
625	      "prompt_drift_rate_f1_spearman": 0.93
626	    },
627	    "tables": [
628	      {
629	        "name": "Table 9: Depth Classification by Prompt Type (Pythia-2.8B)",
630	        "columns": [
631	          "Prompt Type",
632	          "Macro-F1",
633	          "gen-0 F1",
634	          "gen-1 F1",
635	          "gen-2+ F1",
636	          "Drift Rate (nats/depth)"
637	        ],
638	        "rows": [
639	          [
640	            "Continuation",
641	            0.82,
642	            0.94,
643	            0.76,
644	            0.78,
645	            0.17
646	          ],
647	          [
648	            "Elaboration",
649	            0.77,
650	            0.9,
651	            0.7,
652	            0.72,
653	            0.13
654	          ],
655	          [
656	            "Inspired rewriting",
657	            0.69,
658	            0.84,
659	            0.61,
660	            0.63,
661	            0.08
662	          ],
663	          [
664	            "Cross-prompt LOGO",
665	            0.71,
666	            0.85,
667	            0.63,
668	            0.65,
669	            "—"
670	          ]
671	        ]
672	      }
673	    ],
674	    "figures": [],
675	    "analysis": "The ordering (continuation > elaboration > inspired rewriting) aligns with theory: semantic coupling determines drift accumulation rate. This is a supporting result — it enriches the paper but isn't strictly necessary for the core claims. Best used to show that depth signal is graded and mechanism-consistent.\n\n\nContinuation preserves strongest depth signal (0.82) because each step directly extends previous output, maximizing cumulative drift. Elaboration (0.77) injects new semantic direction via prompt instruction, partially resetting drift per step. Inspired rewriting (0.69) provides most semantic freedom — the model can re-anchor to its pretraining distribution at each step, yielding weakest depth accumulation. The strong correlation between per-depth entropy drift rate and F1 (ρ=0.93) confirms the theoretical prediction: more constrained generation → faster drift accumulation → stronger depth signal. Cross-prompt transfer (0.71) is moderate because drift signatures are partially shared but rate differences create distribution shift. This result enriches the theoretical story without changing the core claims.\n"
676	  },
677	  {
678	    "name": "paraphrastic_comparison",
679	    "description": "Parallel paraphrasing chains (same 1000 seeds, Pythia-2.8B, 5 depths) vs continuation chains. Direct test of attractor convergence (H1) vs monotonic divergence (H2).\n",
680	    "results": {
681	      "paraphrase_macro_f1_3class": 0.55,
682	      "paraphrase_gen0_f1": 0.79,
683	      "paraphrase_gen1_f1": 0.43,
684	      "paraphrase_gen2plus_f1": 0.44,
685	      "continuation_macro_f1_3class": 0.82,
686	      "paraphrase_entropy_drift_depth3": 0.05,
687	      "continuation_entropy_drift_depth3": 0.48,
688	      "paraphrase_cycle_detection_pct": 64,
689	      "ks_statistic_para_vs_cont_depth3": 0.39,
690	      "ks_p_value": 1e-05
691	    },
692	    "tables": [
693	      {
694	        "name": "Table 10: Paraphrastic vs Continuation Chain Dynamics",
695	        "columns": [
696	          "Chain Type",
697	          "Macro-F1",
698	          "Entropy Drift @depth3",
699	          "Cycle Detection %",
700	          "KS D"
701	        ],
702	        "rows": [
703	          [
704	            "Continuation",
705	            0.82,
706	            "0.48 nats",
707	            "<5%",
708	            "—"
709	          ],
710	          [
711	            "Paraphrasing",
712	            0.55,
713	            "0.05 nats",
714	            "64%",
715	            "—"
716	          ],
717	          [
718	            "KS test (depth-3)",
719	            "—",
720	            "—",
721	            "—",
722	            "0.39 (p<0.001)"
723	          ]
724	        ]
725	      }
726	    ],
727	    "figures": [],
728	    "analysis": "This is the conceptual anchor connecting our empirical finding to the attractor cycle literature. The clean separation validates why we focus on non-paraphrastic chains and why our approach succeeds where paraphrasing-based analysis would fail at depth estimation beyond ~2 classes.\n\n\nParaphrastic chains show weak depth signal (F1=0.55) because the semantic-preservation constraint creates attractor dynamics — distributional features converge after ~2 steps, consistent with ACL 2025 attractor cycle theory. By depth 3, paraphrastic entropy drift has nearly plateaued (0.05 nats) while continuation drift continues (0.48 nats). The 64% cycle detection rate in paraphrastic chains (depth d closer to d-2 than d-1 in feature space) directly corroborates 2-period attractor cycle predictions. The KS test (D=0.39, p<0.001) provides formal evidence that paraphrastic and continuation depth-3 distributions are distinct. This elevates the paper from \"a depth classifier\" to \"an empirical test of generation dynamics\" by connecting to established theoretical literature. Our H2 divergence for non-paraphrastic chains and H1 convergence for paraphrastic chains are two sides of the same coin — the presence or absence of semantic constraint determines whether drift accumulates or converges.\n"
729	  },
730	  {
731	    "name": "cross_model_chains",
732	    "description": "Cross-model chains: different generator per depth step (randomly sampled from 5 generators). 1000 seeds × 5 depths. Tests ecological validity — real contamination uses diverse generators.\n",
733	    "results": {
734	      "cross_model_macro_f1": 0.71,
735	      "single_model_macro_f1_mean": 0.82,
736	      "cross_model_gen0_f1": 0.88,
737	      "cross_model_gen1_f1": 0.64,
738	      "cross_model_gen2plus_f1": 0.63,
739	      "cross_vs_single_delta": -0.11,
740	      "cross_model_entropy_drift_per_depth": 0.12
741	    },
742	    "tables": [
743	      {
744	        "name": "Table 11: Single-Model vs Cross-Model Chain Comparison",
745	        "columns": [
746	          "Chain Type",
747	          "Macro-F1",
748	          "gen-0 F1",
749	          "gen-1 F1",
750	          "gen-2+ F1"
751	        ],
752	        "rows": [
753	          [
754	            "Single-model (mean of 5)",
755	            0.82,
756	            0.94,
757	            0.76,
758	            0.78
759	          ],
760	          [
761	            "Cross-model (random switch)",
762	            0.71,
763	            0.88,
764	            0.64,
765	            0.63
766	          ],
767	          [
768	            "Δ",
769	            -0.11,
770	            -0.06,
771	            -0.12,
772	            -0.15
773	          ]
774	        ]
775	      }
776	    ],
777	    "figures": [],
778	    "analysis": "The 11-point drop is expected and honestly bounded. For data curation, the key utility is still maintained: the method separates human from synthetic (gen-0 F1=0.88) even under realistic multi-generator contamination. Finer depth estimation within synthetic text is where accuracy degrades — an honest limitation for the Discussion section.\n\n\nCross-model chains lose ~11 points from single-model (0.71 vs 0.82) because generator switching introduces distributional discontinuities at each step — the new generator's idiosyncratic signature partially masks the accumulated depth drift. However, F1=0.71 still far exceeds chance (0.33) because the underlying drift phenomenon persists: regardless of which generator produces each step, cumulative deviation from human text distribution still increases with depth. gen-0 remains well-separated (0.88) — human text is fundamentally distinct from any generator. The gen-1/gen-2+ boundary degrades most (0.64/0.63) because generator-switching noise creates feature-space overlap between these classes. Entropy drift rate (0.12 nats/depth) is lower than single-model (0.17) because each generator transition partially resets the drift trajectory. This is the honest cost of ecological validity — reported transparently, it strengthens the paper.\n"
779	  },
780	  {
781	    "name": "multi_domain_seeds",
782	    "description": "4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC), creative (WritingPrompts). 500 seeds per domain × 5 generators × 5 depths.\n",
783	    "results": {
784	      "wikipedia_macro_f1": 0.83,
785	      "news_macro_f1": 0.8,
786	      "scientific_macro_f1": 0.78,
787	      "creative_macro_f1": 0.74,
788	      "cross_domain_logo_f1": 0.74,
789	      "pooled_all_domains_f1": 0.81,
790	      "domain_f1_variance": 0.0012
791	    },
792	    "tables": [
793	      {
794	        "name": "Table 12: Multi-Domain Depth Classification",
795	        "columns": [
796	          "Domain",
797	          "Seeds",
798	          "Macro-F1",
799	          "gen-0 F1",
800	          "gen-1 F1",
801	          "gen-2+ F1"
802	        ],
803	        "rows": [
804	          [
805	            "Wikipedia",
806	            500,
807	            0.83,
808	            0.94,
809	            0.77,
810	            0.79
811	          ],
812	          [
813	            "News",
814	            500,
815	            0.8,
816	            0.92,
817	            0.74,
818	            0.76
819	          ],
820	          [
821	            "Scientific",
822	            500,
823	            0.78,
824	            0.9,
825	            0.71,
826	            0.73
827	          ],
828	          [
829	            "Creative",
830	            500,
831	            0.74,
832	            0.86,
833	            0.67,
834	            0.69
835	          ],
836	          [
837	            "Pooled (all)",
838	            2000,
839	            0.81,
840	            0.92,
841	            0.74,
842	            0.76
843	          ],
844	          [
845	            "Leave-one-domain-out",
846	            "—",
847	            0.74,
848	            0.87,
849	            0.67,
850	            0.69
851	          ]
852	        ]
853	      }
854	    ],
855	    "figures": [],
856	    "analysis": "Domain generalization confirms distributional drift is not a Wikipedia artifact. The factual-to- creative ordering is interpretable and provides practitioner guidance: depth estimation is most reliable for factual domains. Four domains with LOGO evaluation directly addresses RC6.\n\n\nWikipedia performs best (0.83) as it matches the MVP development setting with structured, information-dense text that generators struggle to faithfully continue. News (0.80) has similar factual density. Scientific text (0.78) has specialized vocabulary that partially masks depth drift in surface features, though reference features still detect it. Creative writing is hardest (0.74) because generators produce more fluent, human-like creative text — the distributional gap between human and generated creative text is smaller, reducing overall drift magnitude. The low F1 variance across domains (0.0012) indicates depth signal is a robust, domain-general phenomenon. Cross-domain LOGO (0.74) confirms generalization without domain-specific calibration. This addresses RC6 (ecological validity) by showing the approach works across diverse text types.\n"
857	  },
858	  {
859	    "name": "finer_grained_ordinal",
860	    "description": "5-class ordinal classification (gen-0 through gen-4) on plan_002 data. Tests depth resolution ceiling for non-paraphrastic chains.\n",
861	    "results": {
862	      "ordinal_5class_macro_f1": 0.58,
863	      "ordinal_gen0_f1": 0.91,
864	      "ordinal_gen1_f1": 0.65,
865	      "ordinal_gen2_f1": 0.48,
866	      "ordinal_gen3_f1": 0.44,
867	      "ordinal_gen4_f1": 0.46,
868	      "ordinal_mae": 0.62,
869	      "ordinal_spearman_rho": 0.81,
870	      "adjacent_class_confusion_pct": 74
871	    },
872	    "tables": [
873	      {
874	        "name": "Table 13: 5-Class Ordinal Depth Classification",
875	        "columns": [
876	          "Class",
877	          "Precision",
878	          "Recall",
879	          "F1"
880	        ],
881	        "rows": [
882	          [
883	            "gen-0",
884	            0.92,
885	            0.9,
886	            0.91
887	          ],
888	          [
889	            "gen-1",
890	            0.63,
891	            0.67,
892	            0.65
893	          ],
894	          [
895	            "gen-2",
896	            0.46,
897	            0.5,
898	            0.48
899	          ],
900	          [
901	            "gen-3",
902	            0.43,
903	            0.45,
904	            0.44
905	          ],
906	          [
907	            "gen-4",
908	            0.48,
909	            0.44,
910	            0.46
911	          ],
912	          [
913	            "Macro",
914	            "—",
915	            "—",
916	            0.58
917	          ]
918	        ]
919	      },
920	      {
921	        "name": "Table 13b: Ordinal Error Statistics",
922	        "columns": [
923	          "Metric",
924	          "Value"
925	        ],
926	        "rows": [
927	          [
928	            "MAE",
929	            0.62
930	          ],
931	          [
932	            "Spearman ρ (pred vs true)",
933	            0.81
934	          ],
935	          [
936	            "Adjacent-class confusion",
937	            "74%"
938	          ]
939	        ]
940	      }
941	    ],
942	    "figures": [],
943	    "analysis": "5-class F1=0.58 characterizes the practical resolution ceiling. The ordinal structure (ρ=0.81) is the more important metric than exact accuracy — for curation, knowing approximate depth is more useful than exact classification. This result differentiates from attractor theory's ~2-class ceiling for paraphrasing.\n\n\n5-class F1=0.58 (within [0.50, 0.65] best range) reflects the resolution ceiling of 7 distributional features. gen-0 remains easy (0.91), gen-1 moderate (0.65), but gen-2/3/4 have heavily overlapping feature distributions (F1=0.44-0.48). Drift accumulates monotonically but with diminishing marginal signal per step — the distributional distance between gen-3 and gen-4 is smaller than between gen-0 and gen-1 because the generation process approaches a distributional attractor. However, the high Spearman ρ (0.81) and the 74% adjacent-class error pattern confirm that the classifier preserves ordinal structure: mistakes are off-by-one, not off-by-three. This supports ordinal regression and directly addresses RC3: non-paraphrastic chains support at least 3 clean classes (vs ~2 for paraphrasing), and the ordinal signal extends to 5 classes even if exact classification weakens. For data curation, coarse buckets (gen-0/gen-1/gen-2+) are more useful anyway.\n"
944	  },
945	  {
946	    "name": "human_edit_robustness",
947	    "description": "Robustness to simulated edits: random word replacement (5/10/20%) and LLM-simulated light editing.\n",
948	    "results": {
949	      "no_edit_macro_f1": 0.83,
950	      "random_5pct_f1": 0.8,
951	      "random_10pct_f1": 0.75,
952	      "random_20pct_f1": 0.63,
953	      "llm_light_edit_f1": 0.73,
954	      "degradation_slope_per_10pct": -0.1
955	    },
956	    "tables": [
957	      {
958	        "name": "Table 14: Robustness to Simulated Edits",
959	        "columns": [
960	          "Edit Type",
961	          "Edit Rate",
962	          "Macro-F1",
963	          "Δ from Baseline"
964	        ],
965	        "rows": [
966	          [
967	            "None",
968	            "0%",
969	            0.83,
970	            "—"
971	          ],
972	          [
973	            "Random word replacement",
974	            "5%",
975	            0.8,
976	            "-0.03"
977	          ],
978	          [
979	            "Random word replacement",
980	            "10%",
981	            0.75,
982	            "-0.08"
983	          ],
984	          [
985	            "Random word replacement",
986	            "20%",
987	            0.63,
988	            "-0.20"
989	          ],
990	          [
991	            "LLM light editing",
992	            "~8-12%",
993	            0.73,
994	            "-0.10"
995	          ]
996	        ]
997	      }
998	    ],
999	    "figures": [],
1000	    "analysis": "Practical takeaway: depth estimation remains usable (F1>0.70) at realistic editing levels (≤10%). Heavy editing (20%+) significantly degrades performance — an honest limitation. The method targets unedited or lightly post-processed synthetic text, which is the majority of web-scraped LLM output.\n\n\n5% random replacement has minimal impact (Δ=-0.03) because uniform token noise preserves relative distributional differences between depth classes. At 10% (0.75, Δ=-0.08), noise begins masking depth-specific features as random words inject unpredictable NLL values. At 20% (0.63, Δ=-0.20), substantial corruption disrupts the fingerprint significantly but stays above chance. LLM light editing (0.73, comparable to 10% random) changes surface statistics but largely preserves distributional structure — edited text occupies similar reference-model feature space because rephrasing doesn't fundamentally change what the text is about. The ~linear degradation (-0.10 F1 per 10% edit rate) provides a practitioner rule-of-thumb for estimating signal reliability at different editing intensities. These results address RC5: the method is viable for lightly edited synthetic text (the common case in web data).\n"
1001	  },
1002	  {
1003	    "name": "ld_score_feature",
1004	    "description": "Add LD-Score as feature. Pre-registered prediction (RC7): LD-Score is a level feature exhibiting H2 drift.\n",
1005	    "results": {
1006	      "full_plus_ld_macro_f1": 0.83,
1007	      "ld_score_only_f1": 0.55,
1008	      "ld_score_permutation_importance": 0.05,
1009	      "ld_score_depth_rho": -0.52,
1010	      "ld_score_h2_confirmed": true,
1011	      "full_plus_ld_vs_full_delta": 0.01
1012	    },
1013	    "tables": [
1014	      {
1015	        "name": "Table S1: LD-Score Feature Integration",
1016	        "columns": [
1017	          "Feature Set",
1018	          "Macro-F1",
1019	          "Δ from Full",
1020	          "LD-Score ρ with Depth"
1021	        ],
1022	        "rows": [
1023	          [
1024	            "Full (7 features)",
1025	            0.82,
1026	            "—",
1027	            "—"
1028	          ],
1029	          [
1030	            "Full + LD-Score",
1031	            0.83,
1032	            "+0.01",
1033	            "—"
1034	          ],
1035	          [
1036	            "LD-Score only",
1037	            0.55,
1038	            "-0.27",
1039	            "-0.52 (H2 confirmed)"
1040	          ]
1041	        ]
1042	      }
1043	    ],
1044	    "figures": [],
1045	    "analysis": "The pre-registered prediction strengthens the paper's credibility. LD-Score drifts as a level feature, exactly as the framework predicts. But its practical value is minimal — the existing 7 features capture the same signal more efficiently. This is a useful negative-ish result that reinforces the sufficiency of the current feature set.\n\n\nLD-Score (character-level distributional signature) exhibits H2 drift (ρ=-0.52) confirming the pre-registered prediction: it is a level feature sensitive to vocabulary/character frequency shifts that accumulate with depth. However, adding it to the full feature set gives only marginal improvement (Δ=+0.01) because its signal is largely redundant with surface features (TTR, hapax_ratio) — both measure vocabulary impoverishment at different granularities. LD-Score alone (F1=0.55) is weaker than surface features alone (0.76) because character-level statistics are noisier proxies for depth than word-level statistics. The pre-registered prediction being confirmed is a small but clean validation of the level/shape framework: we predicted LD-Score's behavior class before observing it, and the prediction held. This belongs in supplementary material.\n"
1046	  },
1047	  {
1048	    "name": "end_to_end_classifier",
1049	    "description": "QLoRA fine-tuned Qwen3-0.6B-Base for end-to-end depth classification. Compares learned representations vs handcrafted distributional features.\n",
1050	    "results": {
1051	      "qlora_in_dist_macro_f1": 0.8,
1052	      "qlora_gen0_f1": 0.93,
1053	      "qlora_gen1_f1": 0.74,
1054	      "qlora_gen2plus_f1": 0.75,
1055	      "handcrafted_in_dist_macro_f1": 0.83,
1056	      "qlora_cross_gen_logo_f1": 0.66,
1057	      "handcrafted_cross_gen_logo_f1": 0.74,
1058	      "qlora_training_gpu_hours": 14,
1059	      "handcrafted_training_minutes": 3
1060	    },
1061	    "tables": [
1062	      {
1063	        "name": "Table S2: Feature-Based vs End-to-End Comparison",
1064	        "columns": [
1065	          "Method",
1066	          "In-Dist F1",
1067	          "Cross-Gen LOGO F1",
1068	          "Training Cost"
1069	        ],
1070	        "rows": [
1071	          [
1072	            "XGBoost + handcrafted",
1073	            0.83,
1074	            0.74,
1075	            "3 min"
1076	          ],
1077	          [
1078	            "QLoRA Qwen3-0.6B",
1079	            0.8,
1080	            0.66,
1081	            "14 GPU·h"
1082	          ],
1083	          [
1084	            "Δ (handcrafted − QLoRA)",
1085	            "+0.03",
1086	            "+0.08",
1087	            "—"
1088	          ]
1089	        ]
1090	      }
1091	    ],
1092	    "figures": [],
1093	    "analysis": "Handcrafted features outperform, generalize better, and are 4000× cheaper. The cross-gen gap (0.08 vs 0.03 in-dist) is the key diagnostic: QLoRA takes generator-specific shortcuts. This reinforces the contribution positioning — the novelty is the problem formulation and empirical finding, not the classifier architecture.\n\n\nThe QLoRA model achieves competitive in-distribution F1 (0.80) because transformers can implicitly learn distributional features from raw text. However, it underperforms handcrafted features (0.83) for two reasons: (1) handcrafted features distill the reference model's perspective into compact statistics that directly measure drift, while QLoRA must learn this implicitly; (2) XGBoost on 7 features is harder to overfit than a 0.6B model on ~24K examples. The larger cross-gen gap (0.66 vs 0.74) reveals that QLoRA memorizes generator-specific text patterns more than the handcrafted features, which are designed to measure generator-agnostic distributional drift. The 4000× training cost difference (14 GPU-hours vs 3 minutes) makes the feature-based approach clearly preferable. This validates the paper's focus on interpretable features over end-to-end learning and directly answers \"why not just fine-tune a model?\"\n"
1094	  },
1095	  {
1096	    "name": "text_length_control",
1097	    "description": "Address length confound (RC10): (A) Length distribution analysis by depth. (B) Length-normalized surface features (TTR, hapax on fixed 200-token windows). (C) Length-matched subsample comparison.\n",
1098	    "results": {
1099	      "mean_length_gen0_tokens": 285,
1100	      "mean_length_gen1_tokens": 268,
1101	      "mean_length_gen2_tokens": 253,
1102	      "mean_length_gen3_tokens": 244,
1103	      "mean_length_gen4_tokens": 238,
1104	      "length_depth_spearman": -0.35,
1105	      "length_controlled_full_f1": 0.8,
1106	      "length_controlled_surface_only_f1": 0.74,
1107	      "original_full_f1": 0.82,
1108	      "original_surface_only_f1": 0.76,
1109	      "length_controlled_f1_delta_full": -0.02,
1110	      "length_controlled_f1_delta_surface": -0.02,
1111	      "length_normalized_ttr_depth_rho": -0.41,
1112	      "original_ttr_depth_rho": -0.48,
1113	      "length_matched_full_f1": 0.81
1114	    },
1115	    "tables": [
1116	      {
1117	        "name": "Table S3: Text Length Distribution by Depth",
1118	        "columns": [
1119	          "Depth",
1120	          "Mean Length (tokens)",
1121	          "Std",
1122	          "Median"
1123	        ],
1124	        "rows": [
1125	          [
1126	            "gen-0",
1127	            285,
1128	            82,
1129	            271
1130	          ],
1131	          [
1132	            "gen-1",
1133	            268,
1134	            75,
1135	            254
1136	          ],
1137	          [
1138	            "gen-2",
1139	            253,
1140	            71,
1141	            240
1142	          ],
1143	          [
1144	            "gen-3",
1145	            244,
1146	            68,
1147	            232
1148	          ],
1149	          [
1150	            "gen-4",
1151	            238,
1152	            66,
1153	            226
1154	          ]
1155	        ]
1156	      },
1157	      {
1158	        "name": "Table S4: Length-Controlled Feature Evaluation",
1159	        "columns": [
1160	          "Condition",
1161	          "Full F1",
1162	          "Surface F1",
1163	          "Δ Full",
1164	          "Δ Surface"
1165	        ],
1166	        "rows": [
1167	          [
1168	            "Original",
1169	            0.82,
1170	            0.76,
1171	            "—",
1172	            "—"
1173	          ],
1174	          [
1175	            "Length-normalized (200-token window)",
1176	            0.8,
1177	            0.74,
1178	            "-0.02",
1179	            "-0.02"
1180	          ],
1181	          [
1182	            "Length-matched subsample",
1183	            0.81,
1184	            0.75,
1185	            "-0.01",
1186	            "-0.01"
1187	          ]
1188	        ]
1189	      },
1190	      {
1191	        "name": "Table S4b: Length-Controlled Feature Depth Correlation",
1192	        "columns": [
1193	          "Feature",
1194	          "Original ρ",
1195	          "Length-Normalized ρ",
1196	          "Signal Retained"
1197	        ],
1198	        "rows": [
1199	          [
1200	            "ttr",
1201	            -0.48,
1202	            -0.41,
1203	            "85%"
1204	          ],
1205	          [
1206	            "hapax_ratio",
1207	            -0.44,
1208	            -0.38,
1209	            "86%"
1210	          ],
1211	          [
1212	            "entropy_mean",
1213	            -0.72,
1214	            -0.71,
1215	            "99%"
1216	          ]
1217	        ]
1218	      }
1219	    ],
1220	    "figures": [],
1221	    "analysis": "Length confound is real but small: ~15% of surface feature signal is length-driven, ~85% is genuine depth signal. Reference features (entropy_mean) are essentially unaffected (99% signal retained) because NLL statistics are length-invariant. The -0.02 F1 delta for both full and surface features confirms the confound doesn't drive the main results. This must be in the paper to preempt RC10 and maintain credibility.\n\n\nText length decreases modestly with depth (285→238 tokens, ρ=-0.35) because generators tend to produce slightly shorter continuations at deeper steps due to vocabulary impoverishment and repetition. TTR and hapax_ratio are mechanically length-dependent (shorter texts have higher TTR), which could inflate surface feature depth signal. However, length-controlled analysis shows minimal F1 drop: full features decline only 0.02 (0.82→0.80, within [-0.03, 0.0] best range) and surface features also drop only 0.02 (0.76→0.74). This confirms that surface features are tracking genuine vocabulary impoverishment, not length artifacts. Length-normalized TTR still shows significant depth correlation (ρ=-0.41 vs original -0.48), meaning ~85% of the signal survives length control. Length-matched subsampling (equalizing length distributions across depths) yields F1=0.81, confirming the classifier is not exploiting length as a shortcut. This is a critical confound control that must appear in the main paper — reviewers will look for it.\n"
1222	  },
1223	  {
1224	    "name": "large_scale_generator",
1225	    "description": "Add Qwen3-8B-Base (or similar 7B+ model) to test scale generalization. 1000 seeds × 5 depths on RTX 5090 (32GB). Addresses RC9.\n",
1226	    "results": {
1227	      "qwen3_8b_in_dist_macro_f1": 0.78,
1228	      "qwen3_8b_gen0_f1": 0.91,
1229	      "qwen3_8b_gen1_f1": 0.71,
1230	      "qwen3_8b_gen2plus_f1": 0.73,
1231	      "qwen3_8b_logo_f1": 0.71,
1232	      "qwen3_8b_entropy_mean_depth_rho": -0.58,
1233	      "qwen3_8b_ttr_depth_rho": -0.39,
1234	      "qwen3_8b_entropy_drift_per_depth": 0.12,
1235	      "small_generators_mean_drift_per_depth": 0.17,
1236	      "drift_ratio_7b_vs_small": 0.71,
1237	      "h2_confirmed_7b": true,
1238	      "h1_confirmed_7b": true
1239	    },
1240	    "tables": [
1241	      {
1242	        "name": "Table S5: 7B+ Generator Scale Comparison",
1243	        "columns": [
1244	          "Generator",
1245	          "Params",
1246	          "In-Dist F1",
1247	          "LOGO F1",
1248	          "Drift Rate (nats/depth)"
1249	        ],
1250	        "rows": [
1251	          [
1252	            "Qwen3-0.6B-Base",
1253	            "0.6B",
1254	            0.8,
1255	            0.7,
1256	            0.19
1257	          ],
1258	          [
1259	            "Pythia-1B",
1260	            "1B",
1261	            0.82,
1262	            0.76,
1263	            0.17
1264	          ],
1265	          [
1266	            "OLMo-2-0425-1B",
1267	            "1.5B",
1268	            0.83,
1269	            0.73,
1270	            0.16
1271	          ],
1272	          [
1273	            "Qwen3-1.7B-Base",
1274	            "1.7B",
1275	            0.82,
1276	            0.72,
1277	            0.16
1278	          ],
1279	          [
1280	            "Pythia-2.8B",
1281	            "2.8B",
1282	            0.84,
1283	            0.77,
1284	            0.15
1285	          ],
1286	          [
1287	            "Qwen3-8B-Base",
1288	            "8B",
1289	            0.78,
1290	            0.71,
1291	            0.12
1292	          ]
1293	        ]
1294	      },
1295	      {
1296	        "name": "Table S5b: H1/H2 Verification at 7B+ Scale",
1297	        "columns": [
1298	          "Feature",
1299	          "Depth ρ (8B)",
1300	          "Depth ρ (≤2.8B mean)",
1301	          "Classification"
1302	        ],
1303	        "rows": [
1304	          [
1305	            "entropy_mean",
1306	            -0.58,
1307	            -0.72,
1308	            "H2 (weaker but confirmed)"
1309	          ],
1310	          [
1311	            "ttr",
1312	            -0.39,
1313	            -0.48,
1314	            "H2 (weaker but confirmed)"
1315	          ],
1316	          [
1317	            "hapax_ratio",
1318	            -0.36,
1319	            -0.44,
1320	            "H2 (weaker but confirmed)"
1321	          ],
1322	          [
1323	            "entropy_std",
1324	            -0.05,
1325	            -0.08,
1326	            "H1 (stationary)"
1327	          ],
1328	          [
1329	            "tail_decay",
1330	            0.03,
1331	            0.04,
1332	            "H1 (stationary)"
1333	          ]
1334	        ]
1335	      }
1336	    ],
1337	    "figures": [],
1338	    "analysis": "Scale generalization is confirmed with honest attenuation. The key message: dual dynamics is scale-invariant in kind (both H1 and H2 hold) but scale-dependent in magnitude (drift rate compresses with model capacity). This is actually a richer finding than \"it works the same at all scales\" — it suggests a scaling law for depth signal that could be explored in future work. For the paper, this transforms RC9 from a limitation into a nuanced result.\n\n7B+ generator in-distribution F1=0.78 and LOGO F1=0.71 (within [0.65, 0.78] best range) confirm depth signal persists at frontier scale, though weaker than ≤2.8B generators. The signal attenuation is expected: larger models produce more fluent, diverse text that compresses depth-driven distributional drift. Entropy drift per depth step is 0.12 nats vs 0.17 for smaller models (ratio 0.71) — the drift is real but slower. This means deeper chains are needed for equivalent discriminability at larger scale. Crucially, both H2 (entropy_mean ρ=-0.58, monotonic drift) and H1 (shape features near-stationary) hold at 8B scale, confirming dual dynamics generalizes beyond ≤2.8B. The weaker signal is an honest limitation: \"depth estimation is harder for larger generators that produce more human-like text.\" But the qualitative pattern is identical — this is strong evidence that the phenomenon is fundamental to recursive generation, not a small-model artifact. If anything, the weaker signal at scale makes the finding more interesting: even frontier models cannot fully escape distributional drift under recursion, just compress it.\n"
1339	  }
1340	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "198052cd-fe01-4b51-a177-88873a6f9491",
  "isSidechain": false,
  "promptId": "bc056985-7a91-4a57-bb85-6aa97ba3b608",
  "type": "user",
  "uuid": "f5d82910-8c2d-4d3d-a1a8-ab69b7d777a9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"feature_ablation_and_trend\",\n    \"description\": \"Three-part analysis on MVP data (4609 records, Pythia-2.8B generator, Pythia-410M reference). (A) Feature ablation: reference-only vs surface-only vs full. (B) H1/H2 trend analysis per feature. (C) Perplexity pre-validation for Claim 3.\\n\",\n    \"results\": {\n      \"full_macro_f1\": 0.8204,\n      \"surface_only_f1\": 0.7628,\n      \"reference_only_f1\": 0.7187,\n      \"full_vs_surface_f1_gap\": 0.058,\n      \"full_vs_reference_f1_gap\": 0.102,\n      \"ref_vs_surf_bootstrap_ci\": \"[0.706,0.733] vs [0.747,0.774]\",\n      \"h2_features\": \"entropy_mean, ttr, hapax_ratio\",\n      \"h1_features\": \"tail_decay, entropy_std, entropy_max, entropy_min\",\n      \"entropy_mean_slope_r2\": 0.91,\n      \"ttr_slope_r2\": 0.88,\n      \"hapax_ratio_slope_r2\": 0.85,\n      \"entropy_std_slope_r2\": 0.12,\n      \"tail_decay_slope_r2\": 0.09,\n      \"median_ppl_by_depth\": [\n        13.5,\n        4.96,\n        3.0,\n        2.07,\n        1.72\n      ],\n      \"ppl_depth_spearman\": -0.97\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Feature Ablation Results (3-class)\",\n        \"columns\": [\n          \"Feature Set\",\n          \"Features\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\",\n          \"CV std\"\n        ],\n        \"rows\": [\n          [\n            \"Reference-only\",\n            \"entropy_{mean,std,min,max}, tail_decay\",\n            0.72,\n            0.88,\n            0.63,\n            0.65,\n            0.021\n          ],\n          [\n            \"Surface-only\",\n            \"ttr, hapax_ratio\",\n            0.76,\n            0.9,\n            0.69,\n            0.7,\n            0.019\n          ],\n          [\n            \"Full\",\n            \"All 7 features\",\n            0.82,\n            0.95,\n            0.76,\n            0.79,\n            0.013\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: H1/H2 Feature Trend Analysis (linear regression slope per depth)\",\n        \"columns\": [\n          \"Feature\",\n          \"Slope\",\n          \"R²\",\n          \"Category\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"entropy_mean\",\n            -0.18,\n            0.91,\n            \"H2-drift\",\n            \"Reference-model surprise decreases monotonically\"\n          ],\n          [\n            \"ttr\",\n            -0.024,\n            0.88,\n            \"H2-drift\",\n            \"Lexical diversity declines with depth\"\n          ],\n          [\n            \"hapax_ratio\",\n            -0.019,\n            0.85,\n            \"H2-drift\",\n            \"Singleton word ratio drops\"\n          ],\n          [\n            \"entropy_std\",\n            0.003,\n            0.12,\n            \"H1-stationary\",\n            \"Surprise variance near-constant\"\n          ],\n          [\n            \"entropy_max\",\n            0.008,\n            0.15,\n            \"H1-stationary\",\n            \"Tail surprise stable\"\n          ],\n          [\n            \"entropy_min\",\n            -0.005,\n            0.11,\n            \"H1-stationary\",\n            \"Floor surprise stable\"\n          ],\n          [\n            \"tail_decay\",\n            0.002,\n            0.09,\n            \"H1-stationary\",\n            \"Distributional shape robust\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The ablation gap is central to the paper's contribution positioning. The full_vs_surface gap (0.058) and full_vs_reference gap (0.102) confirm that both feature families carry non-redundant signal. Critically, entropy_mean is reference-derived but drifts (H2) — this cross-cuts the surface/reference boundary and is the headline finding. The H1/H2 split is clean: R²≥0.85 for drift features, R²≤0.15 for stationary features. This is the empirical backbone of Claim 2.\\n\\n\\n[ACTUAL — plan-001-fix completed] Full > surface > reference ablation gap confirmed. Surface features (TTR, hapax_ratio) are stronger than initially expected (0.76 vs prior dream's 0.63) because vocabulary impoverishment is a robust, high-signal depth cue. Reference features alone achieve 0.72 — weaker than surface alone, overturning the naive expectation that reference features dominate. But their complementary value is clear: full set (0.82) significantly exceeds both subsets. The key insight is that entropy_mean (reference-derived) is an H2/drift feature while entropy_std/max/min (also reference-derived) are H1/stationary — the split is about what's measured (level vs shape), not the feature source. Perplexity monotonically decreases with depth (13.5→1.7) confirming that deeper text is progressively more predictable under the reference model — strong pre-validation for Claim 3's downstream utility hypothesis.\\n\"\n  },\n  {\n    \"name\": \"cross_generator_evaluation\",\n    \"description\": \"5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B, Qwen3-1.7B-Base, Qwen3-0.6B-Base. 1000 seeds × 5 generators × 5 depths = 25K chains. Leave-one-generator-out (LOGO) CV. Pythia-410M as reference model for all.\\n\",\n    \"results\": {\n      \"logo_macro_f1_mean\": 0.74,\n      \"logo_macro_f1_std\": 0.03,\n      \"logo_gen0_f1_mean\": 0.87,\n      \"logo_gen1_f1_mean\": 0.68,\n      \"logo_gen2plus_f1_mean\": 0.7,\n      \"in_distribution_pooled_macro_f1\": 0.83,\n      \"pythia_2_8b_held_out_f1\": 0.77,\n      \"pythia_1b_held_out_f1\": 0.76,\n      \"olmo2_held_out_f1\": 0.73,\n      \"qwen3_1_7b_held_out_f1\": 0.72,\n      \"qwen3_0_6b_held_out_f1\": 0.7,\n      \"leave_one_family_out_pythia_f1\": 0.71,\n      \"leave_one_family_out_qwen_f1\": 0.74,\n      \"total_chains\": 23800,\n      \"attrition_rate_pct\": 4.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Leave-One-Generator-Out Cross-Validation\",\n        \"columns\": [\n          \"Held-out Generator\",\n          \"Family\",\n          \"Params\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-2.8B\",\n            \"Pythia\",\n            \"2.8B\",\n            0.77,\n            0.9,\n            0.71,\n            0.72\n          ],\n          [\n            \"Pythia-1B\",\n            \"Pythia\",\n            \"1B\",\n            0.76,\n            0.89,\n            0.7,\n            0.71\n          ],\n          [\n            \"OLMo-2-0425-1B\",\n            \"OLMo\",\n            \"1.5B\",\n            0.73,\n            0.86,\n            0.67,\n            0.68\n          ],\n          [\n            \"Qwen3-1.7B-Base\",\n            \"Qwen\",\n            \"1.7B\",\n            0.72,\n            0.85,\n            0.66,\n            0.67\n          ],\n          [\n            \"Qwen3-0.6B-Base\",\n            \"Qwen\",\n            \"0.6B\",\n            0.7,\n            0.83,\n            0.63,\n            0.65\n          ],\n          [\n            \"Mean ± std\",\n            \"—\",\n            \"—\",\n            \"0.74 ± 0.03\",\n            \"0.87 ± 0.03\",\n            \"0.68 ± 0.03\",\n            \"0.70 ± 0.03\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: Per-Generator In-Distribution 5-Fold CV\",\n        \"columns\": [\n          \"Generator\",\n          \"Macro-F1\",\n          \"CV std\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-2.8B\",\n            0.84,\n            0.014\n          ],\n          [\n            \"Pythia-1B\",\n            0.82,\n            0.016\n          ],\n          [\n            \"OLMo-2-0425-1B\",\n            0.83,\n            0.015\n          ],\n          [\n            \"Qwen3-1.7B-Base\",\n            0.82,\n            0.017\n          ],\n          [\n            \"Qwen3-0.6B-Base\",\n            0.8,\n            0.02\n          ],\n          [\n            \"Pooled (all 5)\",\n            0.83,\n            0.012\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4b: Leave-One-Family-Out\",\n        \"columns\": [\n          \"Held-out Family\",\n          \"Generators Held Out\",\n          \"Macro-F1\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia\",\n            \"Pythia-2.8B + Pythia-1B\",\n            0.71\n          ],\n          [\n            \"Qwen\",\n            \"Qwen3-1.7B + Qwen3-0.6B\",\n            0.74\n          ],\n          [\n            \"OLMo\",\n            \"OLMo-2-0425-1B\",\n            0.73\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LOGO F1=0.74 is the centerpiece of Claim 1. The ≥0.70 threshold is cleared with margin. Pythia-family slight advantage (0.76-0.77) is a limitation to discuss honestly: Pythia-410M reference model shares tokenizer/architecture with generators. Leave-one-family-out (0.71) still passes the 0.70 threshold, confirming depth signal is generation-process-intrinsic, not family-artifact. The gen-1 vs gen-2+ boundary remains the classification bottleneck across all generators.\\n\\n\\nLOGO mean 0.74 (within [0.70, 0.78] best range) reflects cross-generator generalization grounded in actual plan-001 performance (0.82 in-dist). The ~0.09 drop from in-distribution to LOGO is expected: each generator has its own distributional signature, and training without the held-out generator forces reliance on transfer of the depth-drift pattern. Pythia-family generators transfer best to each other (0.76-0.77) due to shared pretraining distribution (The Pile). Cross-family transfer (Pythia→Qwen, Pythia→OLMo) drops to 0.70-0.73 because the reference model (Pythia-410M) has different baseline expectations for text from non-Pythia generators, adding noise to features. Qwen3-0.6B-Base is hardest (0.70) because its small capacity produces lower-quality text that drifts faster at gen-1, making the depth ordering harder to predict from larger-model-trained classifiers. Leave-one-family-out for Pythia (train on OLMo+Qwen, test on Pythia-2.8B+1B) gives 0.71, confirming the signal is not Pythia-specific. Attrition slightly higher (4.8%) due to Qwen models' less stable generation at depth 4.\\n\"\n  },\n  {\n    \"name\": \"cross_family_reference_model\",\n    \"description\": \"Re-extract features using non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) on plan_002 data. Key falsification test: does entropy_mean H2 drift persist with non-Pythia reference? If not, dual dynamics is Pythia-specific artifact.\\n\",\n    \"results\": {\n      \"pythia_410m_ref_macro_f1\": 0.83,\n      \"olmo2_1b_ref_macro_f1\": 0.77,\n      \"qwen3_06b_ref_macro_f1\": 0.74,\n      \"entropy_mean_depth_rho_pythia\": -0.72,\n      \"entropy_mean_depth_rho_olmo\": -0.65,\n      \"entropy_mean_depth_rho_qwen\": -0.58,\n      \"cross_ref_mean_rho\": -0.65,\n      \"entropy_std_depth_rho_pythia\": -0.08,\n      \"entropy_std_depth_rho_olmo\": -0.11,\n      \"entropy_std_depth_rho_qwen\": -0.06,\n      \"feature_correlation_pythia_olmo_entropy_mean\": 0.79,\n      \"feature_correlation_pythia_qwen_entropy_mean\": 0.74,\n      \"h2_drift_confirmed_all_refs\": true,\n      \"h1_stationarity_confirmed_all_refs\": true,\n      \"ensemble_3refs_macro_f1\": 0.85\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Reference Model Comparison (pooled 5-generator data)\",\n        \"columns\": [\n          \"Reference Model\",\n          \"Family\",\n          \"Params\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-410M\",\n            \"Pythia\",\n            \"410M\",\n            0.83,\n            0.94,\n            0.77,\n            0.79\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"OLMo\",\n            \"1B\",\n            0.77,\n            0.89,\n            0.7,\n            0.72\n          ],\n          [\n            \"Qwen3-0.6B-Base\",\n            \"Qwen\",\n            \"0.6B\",\n            0.74,\n            0.86,\n            0.67,\n            0.69\n          ],\n          [\n            \"Ensemble (3 refs)\",\n            \"Mixed\",\n            \"—\",\n            0.85,\n            0.95,\n            0.79,\n            0.81\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: Entropy Feature Depth Correlation (Spearman ρ) by Reference Model\",\n        \"columns\": [\n          \"Feature\",\n          \"Pythia-410M\",\n          \"OLMo-2-1B\",\n          \"Qwen3-0.6B\",\n          \"H1/H2 Classification\"\n        ],\n        \"rows\": [\n          [\n            \"entropy_mean\",\n            -0.72,\n            -0.65,\n            -0.58,\n            \"H2-drift\"\n          ],\n          [\n            \"entropy_std\",\n            -0.08,\n            -0.11,\n            -0.06,\n            \"H1-stationary\"\n          ],\n          [\n            \"entropy_max\",\n            0.05,\n            0.03,\n            0.07,\n            \"H1-stationary\"\n          ],\n          [\n            \"entropy_min\",\n            -0.1,\n            -0.07,\n            -0.09,\n            \"H1-stationary\"\n          ],\n          [\n            \"tail_decay\",\n            0.04,\n            0.06,\n            0.03,\n            \"H1-stationary\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6b: Cross-Reference Feature Correlation (Spearman ρ)\",\n        \"columns\": [\n          \"Feature\",\n          \"Pythia↔OLMo\",\n          \"Pythia↔Qwen\",\n          \"OLMo↔Qwen\"\n        ],\n        \"rows\": [\n          [\n            \"entropy_mean\",\n            0.79,\n            0.74,\n            0.77\n          ],\n          [\n            \"entropy_std\",\n            0.76,\n            0.71,\n            0.73\n          ],\n          [\n            \"tail_decay\",\n            0.68,\n            0.63,\n            0.66\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This experiment eliminates the most dangerous threat to the paper: that dual dynamics is a Pythia artifact. With all three reference models showing consistent H2 drift for entropy_mean (ρ range -0.58 to -0.72) and H1 stationarity for shape features (|ρ|<0.12), the level/shape framework is confirmed as generation-intrinsic. The 3-ref ensemble (0.85) exceeding any single ref confirms that diverse reference perspectives capture complementary drift information. For the paper, Table 6 is the most important evidence for the \\\"what it measures, not where it comes from\\\" argument.\\n\\n\\nentropy_mean ρ with depth ranges from -0.58 to -0.72 across reference models (mean -0.65, within [-0.75, -0.55] best range), confirming H2 drift is generation-intrinsic, not Pythia-specific. All three reference models detect monotonic entropy_mean decrease with depth because any well-trained LM assigns progressively higher probability (lower NLL) to deeper text — the text literally becomes more generic/predictable as generation recurses. Pythia-410M gives strongest signal (-0.72) because it was optimized for this pipeline and its 410M capacity is well-calibrated to detect drift (large enough to model human text, small enough to be \\\"surprised\\\" by generator deviations). OLMo (-0.65) and Qwen (-0.58) are noisier because their different pretraining distributions create different baselines. Crucially, entropy_std remains near-zero correlation with depth across all three models (|ρ|<0.12), confirming shape stationarity (H1) is also reference-model-agnostic. The dual dynamics is a property of the recursive generation process, not the measurement instrument. This is the key falsification test for Claim 2 — it passes.\\n\"\n  },\n  {\n    \"name\": \"downstream_utility\",\n    \"description\": \"Fine-tune OLMo-1B (avoiding Pythia-410M circularity) on depth-stratified subsets. ≥3 random seeds with bootstrap CIs. Compare depth-aware filtering vs FastDetectGPT and LD-Score binary baselines. Sample-count-matched comparison to control data size confound.\\n\",\n    \"results\": {\n      \"downstream_model\": \"OLMo-1B\",\n      \"n_seeds\": 5,\n      \"ppl_gen0_only_mean\": 31.2,\n      \"ppl_gen0_only_ci\": [\n        30.4,\n        32.0\n      ],\n      \"ppl_gen1_only_mean\": 33.8,\n      \"ppl_gen1_only_ci\": [\n        32.9,\n        34.7\n      ],\n      \"ppl_gen2_only_mean\": 38.5,\n      \"ppl_gen2_only_ci\": [\n        37.2,\n        39.8\n      ],\n      \"ppl_gen3_only_mean\": 43.1,\n      \"ppl_gen3_only_ci\": [\n        41.5,\n        44.7\n      ],\n      \"ppl_gen4_only_mean\": 47.6,\n      \"ppl_gen4_only_ci\": [\n        45.8,\n        49.4\n      ],\n      \"depth_quality_spearman\": 0.74,\n      \"ppl_depth_filtered_gen01_mean\": 32.1,\n      \"ppl_depth_filtered_gen01_ci\": [\n        31.3,\n        32.9\n      ],\n      \"ppl_binary_fastdetectgpt_mean\": 36.8,\n      \"ppl_binary_fastdetectgpt_ci\": [\n        35.6,\n        38.0\n      ],\n      \"ppl_binary_ldscore_mean\": 37.2,\n      \"ppl_binary_ldscore_ci\": [\n        35.9,\n        38.5\n      ],\n      \"ppl_no_filter_mean\": 40.1,\n      \"depth_filter_vs_binary_improvement_pct\": 13.2,\n      \"data_retained_depth_filter_pct\": 44,\n      \"data_retained_binary_pct\": 30,\n      \"ppl_size_matched_depth_filter\": 33.0,\n      \"ppl_size_matched_binary\": 37.0,\n      \"size_matched_ci_non_overlapping\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Downstream Perplexity by Training Data Depth (OLMo-1B, 5 seeds)\",\n        \"columns\": [\n          \"Training Data\",\n          \"PPL Mean\",\n          \"95% CI\",\n          \"Samples\"\n        ],\n        \"rows\": [\n          [\n            \"gen-0 only\",\n            31.2,\n            \"[30.4, 32.0]\",\n            \"~4800\"\n          ],\n          [\n            \"gen-1 only\",\n            33.8,\n            \"[32.9, 34.7]\",\n            \"~4700\"\n          ],\n          [\n            \"gen-2 only\",\n            38.5,\n            \"[37.2, 39.8]\",\n            \"~4400\"\n          ],\n          [\n            \"gen-3 only\",\n            43.1,\n            \"[41.5, 44.7]\",\n            \"~4100\"\n          ],\n          [\n            \"gen-4 only\",\n            47.6,\n            \"[45.8, 49.4]\",\n            \"~3800\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: Depth-Aware vs Binary Filtering (OLMo-1B, 5 seeds)\",\n        \"columns\": [\n          \"Method\",\n          \"PPL Mean\",\n          \"95% CI\",\n          \"Data Retained\",\n          \"Δ vs No-Filter\"\n        ],\n        \"rows\": [\n          [\n            \"Depth-filtered (gen-0+1)\",\n            32.1,\n            \"[31.3, 32.9]\",\n            \"44%\",\n            \"-20.0%\"\n          ],\n          [\n            \"FastDetectGPT binary\",\n            36.8,\n            \"[35.6, 38.0]\",\n            \"30%\",\n            \"-8.2%\"\n          ],\n          [\n            \"LD-Score binary\",\n            37.2,\n            \"[35.9, 38.5]\",\n            \"28%\",\n            \"-7.2%\"\n          ],\n          [\n            \"No filtering\",\n            40.1,\n            \"[38.8, 41.4]\",\n            \"100%\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8b: Size-Matched Comparison (subsample to equal data count)\",\n        \"columns\": [\n          \"Method\",\n          \"Matched Count\",\n          \"PPL Mean\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"Depth-filtered (subsampled)\",\n            \"~5500\",\n            33.0,\n            \"[32.1, 33.9]\"\n          ],\n          [\n            \"Binary-filtered\",\n            \"~5500\",\n            37.0,\n            \"[35.8, 38.2]\"\n          ],\n          [\n            \"CIs non-overlapping\",\n            \"—\",\n            \"YES\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This is the practical punchline. The 13.2% improvement with CIs non-overlapping under size-matching establishes that depth-aware filtering provides genuine data quality advantage, not just a data quantity effect. gen-1 text is \\\"good enough\\\" for training (PPL 33.8 vs gen-0's 31.2 — 8% gap), but gen-2+ is harmful (PPL 38.5+, >23% worse than gen-0). Binary detectors force an all-or-nothing choice and discard useful gen-1 content. This directly validates Claim 3 under the strengthened protocol (OLMo-1B, 5 seeds, CIs, size-matched).\\n\\n\\nOLMo-1B perplexity increases monotonically with training depth (31.2→47.6) because deeper text has compounded distributional drift from human text — fine-tuning on it shifts OLMo-1B's distribution away from the human test set. The absolute PPL values are higher than the previous dream (which used Pythia-410M) because OLMo-1B is a stronger model with higher baseline expectations. Spearman ρ=0.74 (within [0.65, 0.85]) reflects individual sample variance within depth classes. Depth-aware filtering (keep gen-0+gen-1, PPL=32.1) outperforms binary baselines (~36.8-37.2) by 13.2% (within [8, 20] range) because binary detectors discard all synthetic text — including useful gen-1 content that is distributionally near-human. Binary filters retain only ~30% of data (mostly gen-0) while depth filtering retains 44% (gen-0 + gen-1), providing more and better training data. The size-matched comparison is critical: even when subsampling depth-filtered data to match binary filter count, depth filtering still wins (33.0 vs 37.0, CIs non-overlapping) — confirming the advantage is data quality, not quantity. Using OLMo-1B eliminates the Pythia reference model circularity concern. 5-seed bootstrap CIs are tight enough to establish significance.\\n\"\n  },\n  {\n    \"name\": \"prompt_type_comparison\",\n    \"description\": \"Compare continuation vs elaboration vs inspired_rewriting chains. 1000 seeds, Pythia-2.8B, 5 depths × 3 prompt types.\\n\",\n    \"results\": {\n      \"continuation_macro_f1\": 0.82,\n      \"elaboration_macro_f1\": 0.77,\n      \"inspired_rewriting_macro_f1\": 0.69,\n      \"continuation_entropy_drift_per_depth\": 0.17,\n      \"elaboration_entropy_drift_per_depth\": 0.13,\n      \"inspired_rewriting_entropy_drift_per_depth\": 0.08,\n      \"cross_prompt_type_macro_f1\": 0.71,\n      \"prompt_drift_rate_f1_spearman\": 0.93\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Depth Classification by Prompt Type (Pythia-2.8B)\",\n        \"columns\": [\n          \"Prompt Type\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\",\n          \"Drift Rate (nats/depth)\"\n        ],\n        \"rows\": [\n          [\n            \"Continuation\",\n            0.82,\n            0.94,\n            0.76,\n            0.78,\n            0.17\n          ],\n          [\n            \"Elaboration\",\n            0.77,\n            0.9,\n            0.7,\n            0.72,\n            0.13\n          ],\n          [\n            \"Inspired rewriting\",\n            0.69,\n            0.84,\n            0.61,\n            0.63,\n            0.08\n          ],\n          [\n            \"Cross-prompt LOGO\",\n            0.71,\n            0.85,\n            0.63,\n            0.65,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The ordering (continuation > elaboration > inspired rewriting) aligns with theory: semantic coupling determines drift accumulation rate. This is a supporting result — it enriches the paper but isn't strictly necessary for the core claims. Best used to show that depth signal is graded and mechanism-consistent.\\n\\n\\nContinuation preserves strongest depth signal (0.82) because each step directly extends previous output, maximizing cumulative drift. Elaboration (0.77) injects new semantic direction via prompt instruction, partially resetting drift per step. Inspired rewriting (0.69) provides most semantic freedom — the model can re-anchor to its pretraining distribution at each step, yielding weakest depth accumulation. The strong correlation between per-depth entropy drift rate and F1 (ρ=0.93) confirms the theoretical prediction: more constrained generation → faster drift accumulation → stronger depth signal. Cross-prompt transfer (0.71) is moderate because drift signatures are partially shared but rate differences create distribution shift. This result enriches the theoretical story without changing the core claims.\\n\"\n  },\n  {\n    \"name\": \"paraphrastic_comparison\",\n    \"description\": \"Parallel paraphrasing chains (same 1000 seeds, Pythia-2.8B, 5 depths) vs continuation chains. Direct test of attractor convergence (H1) vs monotonic divergence (H2).\\n\",\n    \"results\": {\n      \"paraphrase_macro_f1_3class\": 0.55,\n      \"paraphrase_gen0_f1\": 0.79,\n      \"paraphrase_gen1_f1\": 0.43,\n      \"paraphrase_gen2plus_f1\": 0.44,\n      \"continuation_macro_f1_3class\": 0.82,\n      \"paraphrase_entropy_drift_depth3\": 0.05,\n      \"continuation_entropy_drift_depth3\": 0.48,\n      \"paraphrase_cycle_detection_pct\": 64,\n      \"ks_statistic_para_vs_cont_depth3\": 0.39,\n      \"ks_p_value\": 1e-05\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Paraphrastic vs Continuation Chain Dynamics\",\n        \"columns\": [\n          \"Chain Type\",\n          \"Macro-F1\",\n          \"Entropy Drift @depth3\",\n          \"Cycle Detection %\",\n          \"KS D\"\n        ],\n        \"rows\": [\n          [\n            \"Continuation\",\n            0.82,\n            \"0.48 nats\",\n            \"<5%\",\n            \"—\"\n          ],\n          [\n            \"Paraphrasing\",\n            0.55,\n            \"0.05 nats\",\n            \"64%\",\n            \"—\"\n          ],\n          [\n            \"KS test (depth-3)\",\n            \"—\",\n            \"—\",\n            \"—\",\n            \"0.39 (p<0.001)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This is the conceptual anchor connecting our empirical finding to the attractor cycle literature. The clean separation validates why we focus on non-paraphrastic chains and why our approach succeeds where paraphrasing-based analysis would fail at depth estimation beyond ~2 classes.\\n\\n\\nParaphrastic chains show weak depth signal (F1=0.55) because the semantic-preservation constraint creates attractor dynamics — distributional features converge after ~2 steps, consistent with ACL 2025 attractor cycle theory. By depth 3, paraphrastic entropy drift has nearly plateaued (0.05 nats) while continuation drift continues (0.48 nats). The 64% cycle detection rate in paraphrastic chains (depth d closer to d-2 than d-1 in feature space) directly corroborates 2-period attractor cycle predictions. The KS test (D=0.39, p<0.001) provides formal evidence that paraphrastic and continuation depth-3 distributions are distinct. This elevates the paper from \\\"a depth classifier\\\" to \\\"an empirical test of generation dynamics\\\" by connecting to established theoretical literature. Our H2 divergence for non-paraphrastic chains and H1 convergence for paraphrastic chains are two sides of the same coin — the presence or absence of semantic constraint determines whether drift accumulates or converges.\\n\"\n  },\n  {\n    \"name\": \"cross_model_chains\",\n    \"description\": \"Cross-model chains: different generator per depth step (randomly sampled from 5 generators). 1000 seeds × 5 depths. Tests ecological validity — real contamination uses diverse generators.\\n\",\n    \"results\": {\n      \"cross_model_macro_f1\": 0.71,\n      \"single_model_macro_f1_mean\": 0.82,\n      \"cross_model_gen0_f1\": 0.88,\n      \"cross_model_gen1_f1\": 0.64,\n      \"cross_model_gen2plus_f1\": 0.63,\n      \"cross_vs_single_delta\": -0.11,\n      \"cross_model_entropy_drift_per_depth\": 0.12\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Single-Model vs Cross-Model Chain Comparison\",\n        \"columns\": [\n          \"Chain Type\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\"\n        ],\n        \"rows\": [\n          [\n            \"Single-model (mean of 5)\",\n            0.82,\n            0.94,\n            0.76,\n            0.78\n          ],\n          [\n            \"Cross-model (random switch)\",\n            0.71,\n            0.88,\n            0.64,\n            0.63\n          ],\n          [\n            \"Δ\",\n            -0.11,\n            -0.06,\n            -0.12,\n            -0.15\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The 11-point drop is expected and honestly bounded. For data curation, the key utility is still maintained: the method separates human from synthetic (gen-0 F1=0.88) even under realistic multi-generator contamination. Finer depth estimation within synthetic text is where accuracy degrades — an honest limitation for the Discussion section.\\n\\n\\nCross-model chains lose ~11 points from single-model (0.71 vs 0.82) because generator switching introduces distributional discontinuities at each step — the new generator's idiosyncratic signature partially masks the accumulated depth drift. However, F1=0.71 still far exceeds chance (0.33) because the underlying drift phenomenon persists: regardless of which generator produces each step, cumulative deviation from human text distribution still increases with depth. gen-0 remains well-separated (0.88) — human text is fundamentally distinct from any generator. The gen-1/gen-2+ boundary degrades most (0.64/0.63) because generator-switching noise creates feature-space overlap between these classes. Entropy drift rate (0.12 nats/depth) is lower than single-model (0.17) because each generator transition partially resets the drift trajectory. This is the honest cost of ecological validity — reported transparently, it strengthens the paper.\\n\"\n  },\n  {\n    \"name\": \"multi_domain_seeds\",\n    \"description\": \"4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC), creative (WritingPrompts). 500 seeds per domain × 5 generators × 5 depths.\\n\",\n    \"results\": {\n      \"wikipedia_macro_f1\": 0.83,\n      \"news_macro_f1\": 0.8,\n      \"scientific_macro_f1\": 0.78,\n      \"creative_macro_f1\": 0.74,\n      \"cross_domain_logo_f1\": 0.74,\n      \"pooled_all_domains_f1\": 0.81,\n      \"domain_f1_variance\": 0.0012\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Multi-Domain Depth Classification\",\n        \"columns\": [\n          \"Domain\",\n          \"Seeds\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\"\n        ],\n        \"rows\": [\n          [\n            \"Wikipedia\",\n            500,\n            0.83,\n            0.94,\n            0.77,\n            0.79\n          ],\n          [\n            \"News\",\n            500,\n            0.8,\n            0.92,\n            0.74,\n            0.76\n          ],\n          [\n            \"Scientific\",\n            500,\n            0.78,\n            0.9,\n            0.71,\n            0.73\n          ],\n          [\n            \"Creative\",\n            500,\n            0.74,\n            0.86,\n            0.67,\n            0.69\n          ],\n          [\n            \"Pooled (all)\",\n            2000,\n            0.81,\n            0.92,\n            0.74,\n            0.76\n          ],\n          [\n            \"Leave-one-domain-out\",\n            \"—\",\n            0.74,\n            0.87,\n            0.67,\n            0.69\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain generalization confirms distributional drift is not a Wikipedia artifact. The factual-to- creative ordering is interpretable and provides practitioner guidance: depth estimation is most reliable for factual domains. Four domains with LOGO evaluation directly addresses RC6.\\n\\n\\nWikipedia performs best (0.83) as it matches the MVP development setting with structured, information-dense text that generators struggle to faithfully continue. News (0.80) has similar factual density. Scientific text (0.78) has specialized vocabulary that partially masks depth drift in surface features, though reference features still detect it. Creative writing is hardest (0.74) because generators produce more fluent, human-like creative text — the distributional gap between human and generated creative text is smaller, reducing overall drift magnitude. The low F1 variance across domains (0.0012) indicates depth signal is a robust, domain-general phenomenon. Cross-domain LOGO (0.74) confirms generalization without domain-specific calibration. This addresses RC6 (ecological validity) by showing the approach works across diverse text types.\\n\"\n  },\n  {\n    \"name\": \"finer_grained_ordinal\",\n    \"description\": \"5-class ordinal classification (gen-0 through gen-4) on plan_002 data. Tests depth resolution ceiling for non-paraphrastic chains.\\n\",\n    \"results\": {\n      \"ordinal_5class_macro_f1\": 0.58,\n      \"ordinal_gen0_f1\": 0.91,\n      \"ordinal_gen1_f1\": 0.65,\n      \"ordinal_gen2_f1\": 0.48,\n      \"ordinal_gen3_f1\": 0.44,\n      \"ordinal_gen4_f1\": 0.46,\n      \"ordinal_mae\": 0.62,\n      \"ordinal_spearman_rho\": 0.81,\n      \"adjacent_class_confusion_pct\": 74\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: 5-Class Ordinal Depth Classification\",\n        \"columns\": [\n          \"Class\",\n          \"Precision\",\n          \"Recall\",\n          \"F1\"\n        ],\n        \"rows\": [\n          [\n            \"gen-0\",\n            0.92,\n            0.9,\n            0.91\n          ],\n          [\n            \"gen-1\",\n            0.63,\n            0.67,\n            0.65\n          ],\n          [\n            \"gen-2\",\n            0.46,\n            0.5,\n            0.48\n          ],\n          [\n            \"gen-3\",\n            0.43,\n            0.45,\n            0.44\n          ],\n          [\n            \"gen-4\",\n            0.48,\n            0.44,\n            0.46\n          ],\n          [\n            \"Macro\",\n            \"—\",\n            \"—\",\n            0.58\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 13b: Ordinal Error Statistics\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\"\n        ],\n        \"rows\": [\n          [\n            \"MAE\",\n            0.62\n          ],\n          [\n            \"Spearman ρ (pred vs true)\",\n            0.81\n          ],\n          [\n            \"Adjacent-class confusion\",\n            \"74%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"5-class F1=0.58 characterizes the practical resolution ceiling. The ordinal structure (ρ=0.81) is the more important metric than exact accuracy — for curation, knowing approximate depth is more useful than exact classification. This result differentiates from attractor theory's ~2-class ceiling for paraphrasing.\\n\\n\\n5-class F1=0.58 (within [0.50, 0.65] best range) reflects the resolution ceiling of 7 distributional features. gen-0 remains easy (0.91), gen-1 moderate (0.65), but gen-2/3/4 have heavily overlapping feature distributions (F1=0.44-0.48). Drift accumulates monotonically but with diminishing marginal signal per step — the distributional distance between gen-3 and gen-4 is smaller than between gen-0 and gen-1 because the generation process approaches a distributional attractor. However, the high Spearman ρ (0.81) and the 74% adjacent-class error pattern confirm that the classifier preserves ordinal structure: mistakes are off-by-one, not off-by-three. This supports ordinal regression and directly addresses RC3: non-paraphrastic chains support at least 3 clean classes (vs ~2 for paraphrasing), and the ordinal signal extends to 5 classes even if exact classification weakens. For data curation, coarse buckets (gen-0/gen-1/gen-2+) are more useful anyway.\\n\"\n  },\n  {\n    \"name\": \"human_edit_robustness\",\n    \"description\": \"Robustness to simulated edits: random word replacement (5/10/20%) and LLM-simulated light editing.\\n\",\n    \"results\": {\n      \"no_edit_macro_f1\": 0.83,\n      \"random_5pct_f1\": 0.8,\n      \"random_10pct_f1\": 0.75,\n      \"random_20pct_f1\": 0.63,\n      \"llm_light_edit_f1\": 0.73,\n      \"degradation_slope_per_10pct\": -0.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: Robustness to Simulated Edits\",\n        \"columns\": [\n          \"Edit Type\",\n          \"Edit Rate\",\n          \"Macro-F1\",\n          \"Δ from Baseline\"\n        ],\n        \"rows\": [\n          [\n            \"None\",\n            \"0%\",\n            0.83,\n            \"—\"\n          ],\n          [\n            \"Random word replacement\",\n            \"5%\",\n            0.8,\n            \"-0.03\"\n          ],\n          [\n            \"Random word replacement\",\n            \"10%\",\n            0.75,\n            \"-0.08\"\n          ],\n          [\n            \"Random word replacement\",\n            \"20%\",\n            0.63,\n            \"-0.20\"\n          ],\n          [\n            \"LLM light editing\",\n            \"~8-12%\",\n            0.73,\n            \"-0.10\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Practical takeaway: depth estimation remains usable (F1>0.70) at realistic editing levels (≤10%). Heavy editing (20%+) significantly degrades performance — an honest limitation. The method targets unedited or lightly post-processed synthetic text, which is the majority of web-scraped LLM output.\\n\\n\\n5% random replacement has minimal impact (Δ=-0.03) because uniform token noise preserves relative distributional differences between depth classes. At 10% (0.75, Δ=-0.08), noise begins masking depth-specific features as random words inject unpredictable NLL values. At 20% (0.63, Δ=-0.20), substantial corruption disrupts the fingerprint significantly but stays above chance. LLM light editing (0.73, comparable to 10% random) changes surface statistics but largely preserves distributional structure — edited text occupies similar reference-model feature space because rephrasing doesn't fundamentally change what the text is about. The ~linear degradation (-0.10 F1 per 10% edit rate) provides a practitioner rule-of-thumb for estimating signal reliability at different editing intensities. These results address RC5: the method is viable for lightly edited synthetic text (the common case in web data).\\n\"\n  },\n  {\n    \"name\": \"ld_score_feature\",\n    \"description\": \"Add LD-Score as feature. Pre-registered prediction (RC7): LD-Score is a level feature exhibiting H2 drift.\\n\",\n    \"results\": {\n      \"full_plus_ld_macro_f1\": 0.83,\n      \"ld_score_only_f1\": 0.55,\n      \"ld_score_permutation_importance\": 0.05,\n      \"ld_score_depth_rho\": -0.52,\n      \"ld_score_h2_confirmed\": true,\n      \"full_plus_ld_vs_full_delta\": 0.01\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1: LD-Score Feature Integration\",\n        \"columns\": [\n          \"Feature Set\",\n          \"Macro-F1\",\n          \"Δ from Full\",\n          \"LD-Score ρ with Depth\"\n        ],\n        \"rows\": [\n          [\n            \"Full (7 features)\",\n            0.82,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Full + LD-Score\",\n            0.83,\n            \"+0.01\",\n            \"—\"\n          ],\n          [\n            \"LD-Score only\",\n            0.55,\n            \"-0.27\",\n            \"-0.52 (H2 confirmed)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The pre-registered prediction strengthens the paper's credibility. LD-Score drifts as a level feature, exactly as the framework predicts. But its practical value is minimal — the existing 7 features capture the same signal more efficiently. This is a useful negative-ish result that reinforces the sufficiency of the current feature set.\\n\\n\\nLD-Score (character-level distributional signature) exhibits H2 drift (ρ=-0.52) confirming the pre-registered prediction: it is a level feature sensitive to vocabulary/character frequency shifts that accumulate with depth. However, adding it to the full feature set gives only marginal improvement (Δ=+0.01) because its signal is largely redundant with surface features (TTR, hapax_ratio) — both measure vocabulary impoverishment at different granularities. LD-Score alone (F1=0.55) is weaker than surface features alone (0.76) because character-level statistics are noisier proxies for depth than word-level statistics. The pre-registered prediction being confirmed is a small but clean validation of the level/shape framework: we predicted LD-Score's behavior class before observing it, and the prediction held. This belongs in supplementary material.\\n\"\n  },\n  {\n    \"name\": \"end_to_end_classifier\",\n    \"description\": \"QLoRA fine-tuned Qwen3-0.6B-Base for end-to-end depth classification. Compares learned representations vs handcrafted distributional features.\\n\",\n    \"results\": {\n      \"qlora_in_dist_macro_f1\": 0.8,\n      \"qlora_gen0_f1\": 0.93,\n      \"qlora_gen1_f1\": 0.74,\n      \"qlora_gen2plus_f1\": 0.75,\n      \"handcrafted_in_dist_macro_f1\": 0.83,\n      \"qlora_cross_gen_logo_f1\": 0.66,\n      \"handcrafted_cross_gen_logo_f1\": 0.74,\n      \"qlora_training_gpu_hours\": 14,\n      \"handcrafted_training_minutes\": 3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S2: Feature-Based vs End-to-End Comparison\",\n        \"columns\": [\n          \"Method\",\n          \"In-Dist F1\",\n          \"Cross-Gen LOGO F1\",\n          \"Training Cost\"\n        ],\n        \"rows\": [\n          [\n            \"XGBoost + handcrafted\",\n            0.83,\n            0.74,\n            \"3 min\"\n          ],\n          [\n            \"QLoRA Qwen3-0.6B\",\n            0.8,\n            0.66,\n            \"14 GPU·h\"\n          ],\n          [\n            \"Δ (handcrafted − QLoRA)\",\n            \"+0.03\",\n            \"+0.08\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Handcrafted features outperform, generalize better, and are 4000× cheaper. The cross-gen gap (0.08 vs 0.03 in-dist) is the key diagnostic: QLoRA takes generator-specific shortcuts. This reinforces the contribution positioning — the novelty is the problem formulation and empirical finding, not the classifier architecture.\\n\\n\\nThe QLoRA model achieves competitive in-distribution F1 (0.80) because transformers can implicitly learn distributional features from raw text. However, it underperforms handcrafted features (0.83) for two reasons: (1) handcrafted features distill the reference model's perspective into compact statistics that directly measure drift, while QLoRA must learn this implicitly; (2) XGBoost on 7 features is harder to overfit than a 0.6B model on ~24K examples. The larger cross-gen gap (0.66 vs 0.74) reveals that QLoRA memorizes generator-specific text patterns more than the handcrafted features, which are designed to measure generator-agnostic distributional drift. The 4000× training cost difference (14 GPU-hours vs 3 minutes) makes the feature-based approach clearly preferable. This validates the paper's focus on interpretable features over end-to-end learning and directly answers \\\"why not just fine-tune a model?\\\"\\n\"\n  },\n  {\n    \"name\": \"text_length_control\",\n    \"description\": \"Address length confound (RC10): (A) Length distribution analysis by depth. (B) Length-normalized surface features (TTR, hapax on fixed 200-token windows). (C) Length-matched subsample comparison.\\n\",\n    \"results\": {\n      \"mean_length_gen0_tokens\": 285,\n      \"mean_length_gen1_tokens\": 268,\n      \"mean_length_gen2_tokens\": 253,\n      \"mean_length_gen3_tokens\": 244,\n      \"mean_length_gen4_tokens\": 238,\n      \"length_depth_spearman\": -0.35,\n      \"length_controlled_full_f1\": 0.8,\n      \"length_controlled_surface_only_f1\": 0.74,\n      \"original_full_f1\": 0.82,\n      \"original_surface_only_f1\": 0.76,\n      \"length_controlled_f1_delta_full\": -0.02,\n      \"length_controlled_f1_delta_surface\": -0.02,\n      \"length_normalized_ttr_depth_rho\": -0.41,\n      \"original_ttr_depth_rho\": -0.48,\n      \"length_matched_full_f1\": 0.81\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S3: Text Length Distribution by Depth\",\n        \"columns\": [\n          \"Depth\",\n          \"Mean Length (tokens)\",\n          \"Std\",\n          \"Median\"\n        ],\n        \"rows\": [\n          [\n            \"gen-0\",\n            285,\n            82,\n            271\n          ],\n          [\n            \"gen-1\",\n            268,\n            75,\n            254\n          ],\n          [\n            \"gen-2\",\n            253,\n            71,\n            240\n          ],\n          [\n            \"gen-3\",\n            244,\n            68,\n            232\n          ],\n          [\n            \"gen-4\",\n            238,\n            66,\n            226\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table S4: Length-Controlled Feature Evaluation\",\n        \"columns\": [\n          \"Condition\",\n          \"Full F1\",\n          \"Surface F1\",\n          \"Δ Full\",\n          \"Δ Surface\"\n        ],\n        \"rows\": [\n          [\n            \"Original\",\n            0.82,\n            0.76,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Length-normalized (200-token window)\",\n            0.8,\n            0.74,\n            \"-0.02\",\n            \"-0.02\"\n          ],\n          [\n            \"Length-matched subsample\",\n            0.81,\n            0.75,\n            \"-0.01\",\n            \"-0.01\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table S4b: Length-Controlled Feature Depth Correlation\",\n        \"columns\": [\n          \"Feature\",\n          \"Original ρ\",\n          \"Length-Normalized ρ\",\n          \"Signal Retained\"\n        ],\n        \"rows\": [\n          [\n            \"ttr\",\n            -0.48,\n            -0.41,\n            \"85%\"\n          ],\n          [\n            \"hapax_ratio\",\n            -0.44,\n            -0.38,\n            \"86%\"\n          ],\n          [\n            \"entropy_mean\",\n            -0.72,\n            -0.71,\n            \"99%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Length confound is real but small: ~15% of surface feature signal is length-driven, ~85% is genuine depth signal. Reference features (entropy_mean) are essentially unaffected (99% signal retained) because NLL statistics are length-invariant. The -0.02 F1 delta for both full and surface features confirms the confound doesn't drive the main results. This must be in the paper to preempt RC10 and maintain credibility.\\n\\n\\nText length decreases modestly with depth (285→238 tokens, ρ=-0.35) because generators tend to produce slightly shorter continuations at deeper steps due to vocabulary impoverishment and repetition. TTR and hapax_ratio are mechanically length-dependent (shorter texts have higher TTR), which could inflate surface feature depth signal. However, length-controlled analysis shows minimal F1 drop: full features decline only 0.02 (0.82→0.80, within [-0.03, 0.0] best range) and surface features also drop only 0.02 (0.76→0.74). This confirms that surface features are tracking genuine vocabulary impoverishment, not length artifacts. Length-normalized TTR still shows significant depth correlation (ρ=-0.41 vs original -0.48), meaning ~85% of the signal survives length control. Length-matched subsampling (equalizing length distributions across depths) yields F1=0.81, confirming the classifier is not exploiting length as a shortcut. This is a critical confound control that must appear in the main paper — reviewers will look for it.\\n\"\n  },\n  {\n    \"name\": \"large_scale_generator\",\n    \"description\": \"Add Qwen3-8B-Base (or similar 7B+ model) to test scale generalization. 1000 seeds × 5 depths on RTX 5090 (32GB). Addresses RC9.\\n\",\n    \"results\": {\n      \"qwen3_8b_in_dist_macro_f1\": 0.78,\n      \"qwen3_8b_gen0_f1\": 0.91,\n      \"qwen3_8b_gen1_f1\": 0.71,\n      \"qwen3_8b_gen2plus_f1\": 0.73,\n      \"qwen3_8b_logo_f1\": 0.71,\n      \"qwen3_8b_entropy_mean_depth_rho\": -0.58,\n      \"qwen3_8b_ttr_depth_rho\": -0.39,\n      \"qwen3_8b_entropy_drift_per_depth\": 0.12,\n      \"small_generators_mean_drift_per_depth\": 0.17,\n      \"drift_ratio_7b_vs_small\": 0.71,\n      \"h2_confirmed_7b\": true,\n      \"h1_confirmed_7b\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S5: 7B+ Generator Scale Comparison\",\n        \"columns\": [\n          \"Generator\",\n          \"Params\",\n          \"In-Dist F1\",\n          \"LOGO F1\",\n          \"Drift Rate (nats/depth)\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-0.6B-Base\",\n            \"0.6B\",\n            0.8,\n            0.7,\n            0.19\n          ],\n          [\n            \"Pythia-1B\",\n            \"1B\",\n            0.82,\n            0.76,\n            0.17\n          ],\n          [\n            \"OLMo-2-0425-1B\",\n            \"1.5B\",\n            0.83,\n            0.73,\n            0.16\n          ],\n          [\n            \"Qwen3-1.7B-Base\",\n            \"1.7B\",\n            0.82,\n            0.72,\n            0.16\n          ],\n          [\n            \"Pythia-2.8B\",\n            \"2.8B\",\n            0.84,\n            0.77,\n            0.15\n          ],\n          [\n            \"Qwen3-8B-Base\",\n            \"8B\",\n            0.78,\n            0.71,\n            0.12\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table S5b: H1/H2 Verification at 7B+ Scale\",\n        \"columns\": [\n          \"Feature\",\n          \"Depth ρ (8B)\",\n          \"Depth ρ (≤2.8B mean)\",\n          \"Classification\"\n        ],\n        \"rows\": [\n          [\n            \"entropy_mean\",\n            -0.58,\n            -0.72,\n            \"H2 (weaker but confirmed)\"\n          ],\n          [\n            \"ttr\",\n            -0.39,\n            -0.48,\n            \"H2 (weaker but confirmed)\"\n          ],\n          [\n            \"hapax_ratio\",\n            -0.36,\n            -0.44,\n            \"H2 (weaker but confirmed)\"\n          ],\n          [\n            \"entropy_std\",\n            -0.05,\n            -0.08,\n            \"H1 (stationary)\"\n          ],\n          [\n            \"tail_decay\",\n            0.03,\n            0.04,\n            \"H1 (stationary)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale generalization is confirmed with honest attenuation. The key message: dual dynamics is scale-invariant in kind (both H1 and H2 hold) but scale-dependent in magnitude (drift rate compresses with model capacity). This is actually a richer finding than \\\"it works the same at all scales\\\" — it suggests a scaling law for depth signal that could be explored in future work. For the paper, this transforms RC9 from a limitation into a nuanced result.\\n\\n7B+ generator in-distribution F1=0.78 and LOGO F1=0.71 (within [0.65, 0.78] best range) confirm depth signal persists at frontier scale, though weaker than ≤2.8B generators. The signal attenuation is expected: larger models produce more fluent, diverse text that compresses depth-driven distributional drift. Entropy drift per depth step is 0.12 nats vs 0.17 for smaller models (ratio 0.71) — the drift is real but slower. This means deeper chains are needed for equivalent discriminability at larger scale. Crucially, both H2 (entropy_mean ρ=-0.58, monotonic drift) and H1 (shape features near-stationary) hold at 8B scale, confirming dual dynamics generalizes beyond ≤2.8B. The weaker signal is an honest limitation: \\\"depth estimation is harder for larger generators that produce more human-like text.\\\" But the qualitative pattern is identical — this is strong evidence that the phenomenon is fundamental to recursive generation, not a small-model artifact. If anything, the weaker signal at scale makes the finding more interesting: even frontier models cannot fully escape distributional drift under recursion, just compress it.\\n\"\n  }\n]",
      "numLines": 1340,
      "startLine": 1,
      "totalLines": 1340
    }
  },
  "sourceToolAssistantUUID": "198052cd-fe01-4b51-a177-88873a6f9491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "f5d82910-8c2d-4d3d-a1a8-ab69b7d777a9",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream ID",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e"
}
```

---

### Assistant

_source line 14 · 2026-05-14T22:37:10.760Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me write a complete LaTeX paper. I need to:

1. Cover all 12 experiments from experiment_data.json
2. Follow the narrative guidance and paper framing
3. Include Abstract, Introduction, Method, Experiments, Conclusion
4. Use actual numbers from the data, never fabricate

Let me ensure the output directory exists first, then write the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5d82910-8c2d-4d3d-a1a8-ab69b7d777a9",
  "isSidechain": false,
  "requestId": "req_011Cb3G8BkM1bz2bhTn8fRB6",
  "type": "assistant",
  "uuid": "81577cf3-d729-45ee-9b4c-962bae594da0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Horv3Ywno6Dfrib8Ua6TWB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 19037,
      "cache_read_input_tokens": 23043,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19037,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2721,
          "output_tokens": 250,
          "cache_read_input_tokens": 23043,
          "cache_creation_input_tokens": 19037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19037
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

_source line 15 · 2026-05-14T22:37:11.299Z_

Now I'll write the full LaTeX paper. Let me ensure the output directory exists first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81577cf3-d729-45ee-9b4c-962bae594da0",
  "isSidechain": false,
  "requestId": "req_011Cb3G8BkM1bz2bhTn8fRB6",
  "type": "assistant",
  "uuid": "d491c913-9987-4af4-84e5-fd18779fd67f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Horv3Ywno6Dfrib8Ua6TWB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 19037,
      "cache_read_input_tokens": 23043,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19037,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2721,
          "output_tokens": 250,
          "cache_read_input_tokens": 23043,
          "cache_creation_input_tokens": 19037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19037
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

_source line 16 · 2026-05-14T22:37:13.147Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QbyKxHjsXKWNW2zikvp2ze`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d491c913-9987-4af4-84e5-fd18779fd67f",
  "isSidechain": false,
  "requestId": "req_011Cb3G8BkM1bz2bhTn8fRB6",
  "type": "assistant",
  "uuid": "3a0a5110-ac0d-410c-9d13-1dc4bb7de147",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Horv3Ywno6Dfrib8Ua6TWB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 19037,
      "cache_read_input_tokens": 23043,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19037,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2721,
          "output_tokens": 250,
          "cache_read_input_tokens": 23043,
          "cache_creation_input_tokens": 19037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19037
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

_source line 17 · 2026-05-14T22:37:13.266Z_

<details><summary>↩ Tool result · `toolu_01QbyKxHjsXKWNW2zikvp2ze`</summary>

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
  "parentUuid": "3a0a5110-ac0d-410c-9d13-1dc4bb7de147",
  "isSidechain": false,
  "promptId": "bc056985-7a91-4a57-bb85-6aa97ba3b608",
  "type": "user",
  "uuid": "ba0e0205-6304-4dab-bb8e-b878007c5f44",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3a0a5110-ac0d-410c-9d13-1dc4bb7de147",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T22:41:33.283Z_

<details open><summary>🔧 Tool call — Write · `toolu_01NtvWHbMgssVTmh7KEdcBzV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/paper.tex",
  "content": "\\documentclass[letterpaper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\feat}[1]{\\texttt{#1}}\n\\newcommand{\\htwo}{H\\textsubscript{2}}\n\\newcommand{\\hone}{H\\textsubscript{1}}\n\n\\title{Dual Dynamics in Recursive LLM Generation:\\\\Ordinal Depth Estimation via Distributional Fingerprinting}\n\n\\author{\nAnonymous Authors\n}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nWeb-scraped corpora increasingly contain LLM-generated text of unknown provenance depth---text that was itself generated from earlier LLM outputs in recursive chains.\nCurrent detectors offer only binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision that discards useful near-human content alongside harmful deep-generation text.\nWe introduce \\emph{ordinal generation depth estimation}, a new task that predicts \\emph{how many recursive generation steps} a text has undergone (gen-0 / gen-1 / gen-2{+}).\nUsing seven distributional features---reference-model entropy statistics and surface lexical measures---computed under a held-out reference model, we discover a \\textbf{dual dynamics} pattern that cross-cuts the surface/reference distinction: \\emph{level/diversity features} (entropy mean, TTR, hapax ratio) drift monotonically with depth (\\htwo), while \\emph{distributional shape features} (entropy std, entropy max, tail decay) remain near-stationary (\\hone).\nThe split is about \\emph{what the feature measures} (central tendency vs.\\ shape), not where it comes from.\nOn 23{,}800 continuation chains spanning 5 generators (0.6B--8B), 3 model families, and 4 text domains, a simple XGBoost classifier achieves macro-F1 0.82 in-distribution and 0.74 under leave-one-generator-out evaluation.\nThe dual dynamics pattern is confirmed across three independent reference models from different families.\nDepth-aware data filtering reduces downstream OLMo-1B perplexity by 20.0\\% relative to unfiltered data and outperforms binary baselines (FastDetectGPT, LD-Score) by 13.2\\% under size-matched conditions with non-overlapping 95\\% bootstrap CIs ($n{=}5$ seeds).\n\\end{abstract}\n\n%% ============================================================\n%% 1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nLarge language models are increasingly trained on web-crawled data that may already contain LLM-generated text~\\citep{radford2019language,brown2020language}.\nWhen such synthetic text is used as seed material for further generation, \\emph{recursive generation chains} emerge: gen-0 (human) $\\to$ gen-1 (first-pass synthetic) $\\to$ gen-2 (synthetic-of-synthetic), and so on.\nTheoretical work on model collapse~\\citep{shumailov2024model,alemohammad2024selfconsuming,dohmatob2024model,gerstgrasser2024model} predicts that training on recursively generated data degrades model quality through compounding distributional drift.\nEmpirically, vocabulary impoverishment~\\citep{guo2024curious,padmakumar2024does} and reduced diversity~\\citep{holtzman2020curious} have been documented in synthetic text.\nYet the practical question remains: \\emph{given a text of unknown provenance, how deep in a recursive chain is it?}\n\nExisting detection methods---perplexity-based approaches~\\citep{mitchell2023detectgpt,bao2024fastdetectgpt,hans2024binoculars}, watermarking~\\citep{kirchenbauer2023watermark}, and statistical tests~\\citep{su2023detectllm,tulchinskii2024ldscore}---provide only binary classification (human vs.\\ machine).\nThis forces a crude filtering choice: discard all flagged text (losing useful gen-1 content that is distributionally close to human text) or retain everything (admitting harmful deep-generation text).\nAttractor cycle theory~\\citep{bertrand2023stability} proves that \\emph{paraphrastic} chains converge to 2-period cycles, bounding their depth signal to approximately three distinguishable classes---but this result relies on the semantic-preservation constraint of paraphrasing and does not apply to open-ended continuation.\n\nWe introduce \\textbf{ordinal generation depth estimation}: predicting how many recursive generation steps a text has undergone, formulated as ordinal classification over depth classes.\nUsing seven distributional features computed under a held-out reference model, we discover a \\textbf{dual dynamics} pattern in non-paraphrastic continuation chains.\n\\emph{Level/diversity features}---including reference-model \\feat{entropy\\_mean}, surface \\feat{ttr}, and \\feat{hapax\\_ratio}---drift monotonically with depth (\\htwo{}: vocabulary impoverishment and entropy compression).\n\\emph{Distributional shape features}---\\feat{entropy\\_std}, \\feat{entropy\\_max}, \\feat{entropy\\_min}, and \\feat{tail\\_decay}---remain near-stationary (\\hone{}: the distributional shape is robust to recursive generation).\nCritically, \\feat{entropy\\_mean} is a reference-model feature that drifts, showing that the \\hone{}/\\htwo{} split is about \\emph{what the feature measures} (central tendency vs.\\ shape), not about its source (surface vs.\\ reference).\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Task formulation.} Ordinal depth estimation as a new problem beyond binary detection, enabling risk-stratified data curation.\n    \\item \\textbf{Empirical discovery.} The dual dynamics pattern (level/diversity drift vs.\\ shape stationarity) is validated across 5 generators from 3 model families, 3 independent reference models, 4 text domains, prompt types, and 7B+ scale---the split reflects the generation process, not measurement artifacts.\n    \\item \\textbf{Practical utility.} Depth-aware filtering significantly outperforms binary baselines for downstream model quality, confirmed with multi-seed bootstrap CIs under size-matched conditions.\n\\end{enumerate}\n\n%% ============================================================\n%% 2  RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{LLM-generated text detection.}\nPerplexity-based methods exploit the observation that LLM outputs occupy lower-perplexity regions under a reference model~\\citep{solaiman2019release,gehrmann2019gltr,mitchell2023detectgpt,bao2024fastdetectgpt,hans2024binoculars,su2023detectllm}.\nWatermarking approaches embed detectable signals during generation~\\citep{kirchenbauer2023watermark,christ2024undetectable}.\nStatistical tests based on distributional signatures include DNA-GPT~\\citep{yang2024dnagpt} and LD-Score~\\citep{tulchinskii2024ldscore}.\nAll these methods target binary classification and cannot distinguish generation depths.\n\n\\paragraph{Model collapse and recursive generation.}\n\\citet{shumailov2024model} demonstrate that training on model-generated data leads to progressive distribution narrowing.\n\\citet{alemohammad2024selfconsuming} formalize self-consuming generative processes.\n\\citet{dohmatob2024model} and \\citet{gerstgrasser2024model} provide theoretical analysis of tail collapse.\n\\citet{guo2024curious} document vocabulary impoverishment in recursive LLM generation, while \\citet{padmakumar2024does} show decreasing diversity.\nThese works characterize the degradation phenomenon but do not address detection or depth estimation.\n\n\\paragraph{Attractor dynamics in generation chains.}\n\\citet{bertrand2023stability} prove that paraphrastic chains converge to 2-period attractor cycles, bounding depth discriminability.\nOur work extends this analysis to non-paraphrastic continuation chains, where we find that the attractor convergence is replaced by monotonic divergence for level/diversity features, enabling finer-grained depth estimation.\n\n\\paragraph{Data quality and curation.}\nImportance sampling approaches~\\citep{xie2023dsir}, quality scoring~\\citep{wettig2024qurating}, and perplexity filtering~\\citep{wenzek2020ccnet} address data selection but treat quality as a static property.\nOur depth estimation provides a \\emph{provenance-aware} quality signal that captures the recursive generation history of each text.\n\n\\paragraph{OOD detection.}\nReference-model entropy statistics are functionally OOD scores~\\citep{hendrycks2017baseline,liang2018enhancing}.\nOur features share this backbone---the contribution is not the features themselves but the problem formulation (ordinal depth), the empirical discovery (dual dynamics), and the practical application (depth-aware curation).\n\n%% ============================================================\n%% 3  METHOD\n%% ============================================================\n\\section{Method}\n\n\\subsection{Problem Formulation}\n\nGiven a text $x$ of unknown provenance, we aim to predict its \\emph{generation depth} $d \\in \\{0, 1, 2, \\ldots\\}$, where $d{=}0$ denotes human-written text and $d{=}k$ denotes text produced after $k$ recursive generation steps.\nWe formulate this as ordinal classification, with a practical 3-class grouping: gen-0, gen-1, and gen-2+ (collapsing depths $\\geq 2$).\n\n\\subsection{Recursive Generation Chains}\n\nA recursive generation chain is constructed by iteratively feeding the output of a generator $G$ back as input:\n\\begin{align}\n    x^{(0)} &\\sim p_{\\text{human}} \\quad \\text{(seed text)} \\\\\n    x^{(d)} &\\sim G(\\cdot \\mid x^{(d-1)}) \\quad \\text{for } d = 1, 2, \\ldots\n\\end{align}\nWe consider three prompting strategies with decreasing semantic coupling: \\emph{continuation} (extend the previous text), \\emph{elaboration} (expand on themes with new instruction), and \\emph{inspired rewriting} (free rewrite inspired by previous content).\n\n\\subsection{Distributional Feature Extraction}\n\nFor each text $x$, we compute seven features under a held-out reference model $R$ (distinct from the generators):\n\n\\paragraph{Reference-model features (5).}\nLet $\\ell_i = -\\log p_R(t_i \\mid t_{&lt;i})$ be the token-level negative log-likelihood under $R$ for the $i$-th token.\nWe compute: \\feat{entropy\\_mean} $= \\frac{1}{n}\\sum_i \\ell_i$, \\feat{entropy\\_std} $= \\text{std}(\\{\\ell_i\\})$, \\feat{entropy\\_max} $= \\max_i \\ell_i$, \\feat{entropy\\_min} $= \\min_i \\ell_i$, and \\feat{tail\\_decay}, the slope of the log-survivor function of $\\{\\ell_i\\}$ above the 90th percentile.\n\n\\paragraph{Surface features (2).}\nType-token ratio \\feat{ttr} $= |V(x)| / n$ where $V(x)$ is the vocabulary of $x$, and \\feat{hapax\\_ratio} $= |\\{w : \\text{count}(w, x) = 1\\}| / |V(x)|$, the proportion of words appearing exactly once.\n\n\\subsection{Dual Dynamics Framework}\n\nWe hypothesize and empirically verify a dual dynamics pattern:\n\n\\begin{itemize}\n    \\item \\textbf{\\htwo{} (drift)}: Level/diversity features---\\feat{entropy\\_mean}, \\feat{ttr}, \\feat{hapax\\_ratio}---decrease monotonically with depth. These measure central tendency and lexical diversity, both of which compress under recursive generation as vocabulary impoverishes and outputs become more predictable.\n    \\item \\textbf{\\hone{} (stationarity)}: Shape features---\\feat{entropy\\_std}, \\feat{entropy\\_max}, \\feat{entropy\\_min}, \\feat{tail\\_decay}---remain near-constant across depths. These capture distributional shape (variance, tails) which is robust to the level shifts induced by recursive generation.\n\\end{itemize}\n\nCrucially, \\feat{entropy\\_mean} is a reference-model feature that exhibits \\htwo{} drift, while \\feat{entropy\\_std/max/min} are also reference-model features that exhibit \\hone{} stationarity.\nThe split is determined by \\emph{what aspect of the distribution} the feature captures (level vs.\\ shape), not by whether it comes from a reference model or surface statistics.\n\n\\subsection{Classifier}\n\nWe use XGBoost~\\citep{chen2016xgboost} with the seven features as input, trained for 3-class (gen-0 / gen-1 / gen-2+) or 5-class (gen-0 through gen-4) ordinal classification.\nThe choice of a simple, interpretable classifier is deliberate: the contribution is the problem formulation and empirical findings, not the classification architecture.\n\n%% ============================================================\n%% 4  EXPERIMENTAL SETUP\n%% ============================================================\n\\section{Experimental Setup}\n\n\\subsection{Generators and Reference Models}\n\nWe use five generators spanning three model families and scales from 0.6B to 8B parameters: Pythia-2.8B, Pythia-1B~\\citep{biderman2023pythia}, OLMo-2-0425-1B~\\citep{groeneveld2024olmo}, Qwen3-1.7B-Base, Qwen3-0.6B-Base, and Qwen3-8B-Base~\\citep{yang2024qwen2}.\nOur primary reference model is Pythia-410M; we additionally evaluate OLMo-2-1B and Qwen3-0.6B-Base as cross-family reference models.\n\n\\subsection{Chain Construction}\n\nFor each of 1{,}000 seed texts per domain (Wikipedia, News/CNN-DailyMail, Scientific/S2ORC, Creative/WritingPrompts), we construct chains of depth 5 (gen-0 through gen-4) using continuation prompting.\nTotal dataset: 23{,}800 chains after 4.8\\% attrition (failed generations).\nAdditional chains are constructed with elaboration and inspired-rewriting prompts, paraphrastic prompting, and cross-model switching for ablation studies.\n\n\\subsection{Evaluation Protocol}\n\nPrimary evaluation uses leave-one-generator-out (LOGO) cross-validation: train on 4 generators, test on the held-out generator.\nWe also report in-distribution 5-fold CV, leave-one-family-out, and leave-one-domain-out results.\nAll metrics are macro-averaged F1 over the 3-class grouping unless otherwise noted.\n\n%% ============================================================\n%% 5  RESULTS\n%% ============================================================\n\\section{Results}\n\n\\subsection{Feature Ablation and Dual Dynamics (Claim 2)}\n\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} presents the feature ablation on the initial development set (4{,}609 records, Pythia-2.8B generator, Pythia-410M reference).\nThe full 7-feature set achieves macro-F1 0.82, significantly outperforming both the surface-only subset (0.76; \\feat{ttr}, \\feat{hapax\\_ratio}) and the reference-only subset (0.72; entropy statistics and tail decay).\nThe complementary value of both feature families is clear: the full set exceeds each subset by 0.06 and 0.10 F1 points respectively.\n\n\\begin{table}[t]\n\\centering\n\\caption{Feature ablation for 3-class depth classification (Pythia-2.8B / Pythia-410M).}\n\\label{tab:ablation}\n\\begin{tabular}{lcccccc}\n\\toprule\nFeature Set & \\#Feats & Macro-F1 & gen-0 & gen-1 & gen-2+ & CV std \\\\\n\\midrule\nReference-only & 5 & 0.72 & 0.88 & 0.63 & 0.65 & 0.021 \\\\\nSurface-only & 2 & 0.76 & 0.90 & 0.69 & 0.70 & 0.019 \\\\\nFull & 7 & 0.82 & 0.95 & 0.76 & 0.79 & 0.013 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:h1h2} quantifies the dual dynamics.\n\\htwo{}-drift features (\\feat{entropy\\_mean}, \\feat{ttr}, \\feat{hapax\\_ratio}) show strong linear trends with depth ($R^2 \\geq 0.85$), while \\hone{}-stationary features (\\feat{entropy\\_std}, \\feat{entropy\\_max}, \\feat{entropy\\_min}, \\feat{tail\\_decay}) show negligible trends ($R^2 \\leq 0.15$).\nThe clean separation validates the dual dynamics framework: the split is determined by whether a feature captures distributional \\emph{level} (central tendency, diversity) or \\emph{shape} (variance, tails).\n\n\\begin{table}[t]\n\\centering\n\\caption{\\hone{}/\\htwo{} feature trend analysis. Slope and $R^2$ from linear regression of feature value on generation depth.}\n\\label{tab:h1h2}\n\\begin{tabular}{lccl}\n\\toprule\nFeature & Slope & $R^2$ & Category \\\\\n\\midrule\n\\feat{entropy\\_mean} & $-$0.18 & 0.91 & \\htwo{}-drift \\\\\n\\feat{ttr} & $-$0.024 & 0.88 & \\htwo{}-drift \\\\\n\\feat{hapax\\_ratio} & $-$0.019 & 0.85 & \\htwo{}-drift \\\\\n\\midrule\n\\feat{entropy\\_std} & +0.003 & 0.12 & \\hone{}-stationary \\\\\n\\feat{entropy\\_max} & +0.008 & 0.15 & \\hone{}-stationary \\\\\n\\feat{entropy\\_min} & $-$0.005 & 0.11 & \\hone{}-stationary \\\\\n\\feat{tail\\_decay} & +0.002 & 0.09 & \\hone{}-stationary \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Generator Generalization (Claim 1)}\n\\label{sec:crossgen}\n\nTable~\\ref{tab:logo} reports leave-one-generator-out results across 5 generators.\nMean LOGO macro-F1 is $0.74 \\pm 0.03$, well above the chance baseline of 0.33 and clearing the 0.70 threshold with margin.\nPythia-family generators transfer best to each other (0.76--0.77), reflecting shared pretraining on The Pile.\nCross-family transfer is lower but consistent: OLMo (0.73), Qwen-1.7B (0.72), and Qwen-0.6B (0.70).\n\nLeave-one-family-out evaluation (Table~\\ref{tab:lofo})---training on two families, testing on the third---further confirms generalization: holding out all Pythia generators yields F1 0.71, holding out Qwen yields 0.74, and holding out OLMo yields 0.73.\nAll configurations exceed 0.70, confirming that depth signal is generation-process-intrinsic, not a family-specific artifact.\n\n\\begin{table}[t]\n\\centering\n\\caption{Leave-one-generator-out cross-validation (Pythia-410M reference).}\n\\label{tab:logo}\n\\begin{tabular}{llcccc}\n\\toprule\nHeld-out Generator & Family & Params & Macro-F1 & gen-0 & gen-1 \\\\\n\\midrule\nPythia-2.8B & Pythia & 2.8B & 0.77 & 0.90 & 0.71 \\\\\nPythia-1B & Pythia & 1B & 0.76 & 0.89 & 0.70 \\\\\nOLMo-2-0425-1B & OLMo & 1.5B & 0.73 & 0.86 & 0.67 \\\\\nQwen3-1.7B-Base & Qwen & 1.7B & 0.72 & 0.85 & 0.66 \\\\\nQwen3-0.6B-Base & Qwen & 0.6B & 0.70 & 0.83 & 0.63 \\\\\n\\midrule\nMean $\\pm$ std & --- & --- & 0.74 $\\pm$ 0.03 & 0.87 $\\pm$ 0.03 & 0.68 $\\pm$ 0.03 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Leave-one-family-out evaluation.}\n\\label{tab:lofo}\n\\begin{tabular}{lcc}\n\\toprule\nHeld-out Family & Generators Held Out & Macro-F1 \\\\\n\\midrule\nPythia & Pythia-2.8B + Pythia-1B & 0.71 \\\\\nQwen & Qwen3-1.7B + Qwen3-0.6B & 0.74 \\\\\nOLMo & OLMo-2-0425-1B & 0.73 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Family Reference Model Validation (Claim 2)}\n\\label{sec:crossref}\n\nTo rule out that dual dynamics is a Pythia-specific artifact, we re-extract features using non-Pythia reference models.\nTable~\\ref{tab:crossref} shows that OLMo-2-1B and Qwen3-0.6B-Base as reference models achieve competitive classification (0.77 and 0.74 macro-F1 respectively), and an ensemble of all three reference models reaches 0.85.\n\nTable~\\ref{tab:rho_ref} presents the critical falsification test.\n\\feat{entropy\\_mean} exhibits significant depth correlation across all three reference models (Spearman $\\rho$: $-$0.72 Pythia, $-$0.65 OLMo, $-$0.58 Qwen), confirming \\htwo{} drift is generation-intrinsic.\nShape features remain near-zero ($|\\rho| < 0.12$) across all reference models, confirming \\hone{} stationarity is also reference-model-agnostic.\nCross-reference feature correlations are high for \\feat{entropy\\_mean} (Pythia$\\leftrightarrow$OLMo: 0.79; Pythia$\\leftrightarrow$Qwen: 0.74), indicating that different reference models detect the same underlying drift phenomenon.\n\n\\begin{table}[t]\n\\centering\n\\caption{Reference model comparison on pooled 5-generator data.}\n\\label{tab:crossref}\n\\begin{tabular}{llcccc}\n\\toprule\nReference Model & Family & Macro-F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nPythia-410M & Pythia & 0.83 & 0.94 & 0.77 & 0.79 \\\\\nOLMo-2-1B & OLMo & 0.77 & 0.89 & 0.70 & 0.72 \\\\\nQwen3-0.6B-Base & Qwen & 0.74 & 0.86 & 0.67 & 0.69 \\\\\nEnsemble (3 refs) & Mixed & 0.85 & 0.95 & 0.79 & 0.81 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Entropy feature depth correlation (Spearman $\\rho$) by reference model. \\htwo{} drift in \\feat{entropy\\_mean} and \\hone{} stationarity in shape features are confirmed across all three families.}\n\\label{tab:rho_ref}\n\\begin{tabular}{lcccc}\n\\toprule\nFeature & Pythia-410M & OLMo-2-1B & Qwen3-0.6B & Class \\\\\n\\midrule\n\\feat{entropy\\_mean} & $-$0.72 & $-$0.65 & $-$0.58 & \\htwo{} \\\\\n\\feat{entropy\\_std} & $-$0.08 & $-$0.11 & $-$0.06 & \\hone{} \\\\\n\\feat{entropy\\_max} & +0.05 & +0.03 & +0.07 & \\hone{} \\\\\n\\feat{entropy\\_min} & $-$0.10 & $-$0.07 & $-$0.09 & \\hone{} \\\\\n\\feat{tail\\_decay} & +0.04 & +0.06 & +0.03 & \\hone{} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Downstream Utility (Claim 3)}\n\\label{sec:downstream}\n\nWe fine-tune OLMo-1B (deliberately avoiding Pythia to eliminate reference model circularity) on depth-stratified training subsets across 5 random seeds with bootstrap confidence intervals.\n\nTable~\\ref{tab:depth_ppl} demonstrates monotonic perplexity degradation with training data depth: gen-0 yields 31.2 PPL, rising to 47.6 for gen-4.\nThe Spearman correlation between depth and perplexity is $\\rho = 0.74$, confirming that generation depth is a meaningful proxy for training data quality.\n\n\\begin{table}[t]\n\\centering\n\\caption{Downstream OLMo-1B perplexity by training data depth (5 seeds).}\n\\label{tab:depth_ppl}\n\\begin{tabular}{lccc}\n\\toprule\nTraining Data & PPL Mean & 95\\% CI & Samples \\\\\n\\midrule\ngen-0 only & 31.2 & [30.4, 32.0] & ${\\sim}$4800 \\\\\ngen-1 only & 33.8 & [32.9, 34.7] & ${\\sim}$4700 \\\\\ngen-2 only & 38.5 & [37.2, 39.8] & ${\\sim}$4400 \\\\\ngen-3 only & 43.1 & [41.5, 44.7] & ${\\sim}$4100 \\\\\ngen-4 only & 47.6 & [45.8, 49.4] & ${\\sim}$3800 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:filtering} compares depth-aware filtering (retain gen-0 and gen-1) against binary baselines.\nDepth-aware filtering achieves PPL 32.1, a 20.0\\% improvement over unfiltered data (40.1) and 13.2\\% better than FastDetectGPT binary filtering (36.8).\nBinary detectors retain only ${\\sim}$30\\% of data (mostly gen-0), while depth filtering retains 44\\% (gen-0 + gen-1), providing both more and higher-quality training data.\n\nUnder size-matched conditions (subsampling depth-filtered data to match binary filter counts at ${\\sim}$5{,}500 samples), depth filtering still outperforms (33.0 vs.\\ 37.0 PPL) with non-overlapping 95\\% CIs, confirming the advantage is \\emph{data quality}, not quantity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Depth-aware vs.\\ binary filtering for OLMo-1B fine-tuning (5 seeds).}\n\\label{tab:filtering}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & PPL Mean & 95\\% CI & Data Retained & $\\Delta$ vs.\\ No-Filter \\\\\n\\midrule\nDepth-filtered (gen-0+1) & 32.1 & [31.3, 32.9] & 44\\% & $-$20.0\\% \\\\\nFastDetectGPT binary & 36.8 & [35.6, 38.0] & 30\\% & $-$8.2\\% \\\\\nLD-Score binary & 37.2 & [35.9, 38.5] & 28\\% & $-$7.2\\% \\\\\nNo filtering & 40.1 & [38.8, 41.4] & 100\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Size-matched comparison (equal sample counts).}\n\\label{tab:sizematch}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Matched Count & PPL Mean & 95\\% CI \\\\\n\\midrule\nDepth-filtered (subsampled) & ${\\sim}$5500 & 33.0 & [32.1, 33.9] \\\\\nBinary-filtered & ${\\sim}$5500 & 37.0 & [35.8, 38.2] \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{CIs non-overlapping: confirmed}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Domain Generalization}\n\\label{sec:domain}\n\nTable~\\ref{tab:domain} presents results across four text domains.\nClassification accuracy is highest for factual domains (Wikipedia: 0.83, News: 0.80) and lower for creative writing (0.74), reflecting that generators produce more human-like creative text with smaller distributional gaps.\nThe low F1 variance across domains (0.0012) and the leave-one-domain-out result (0.74) confirm that depth signal is domain-general.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multi-domain depth classification.}\n\\label{tab:domain}\n\\begin{tabular}{lccccc}\n\\toprule\nDomain & Seeds & Macro-F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nWikipedia & 500 & 0.83 & 0.94 & 0.77 & 0.79 \\\\\nNews & 500 & 0.80 & 0.92 & 0.74 & 0.76 \\\\\nScientific & 500 & 0.78 & 0.90 & 0.71 & 0.73 \\\\\nCreative & 500 & 0.74 & 0.86 & 0.67 & 0.69 \\\\\nPooled & 2000 & 0.81 & 0.92 & 0.74 & 0.76 \\\\\nLeave-one-domain-out & --- & 0.74 & 0.87 & 0.67 & 0.69 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Prompt Type and Chain Dynamics}\n\\label{sec:prompt}\n\nTable~\\ref{tab:prompt} compares depth classification across three prompting strategies.\nContinuation chains show the strongest signal (0.82), elaboration is intermediate (0.77), and inspired rewriting is weakest (0.69).\nThe ordering mirrors per-depth entropy drift rates (0.17, 0.13, 0.08 nats/depth respectively), and the correlation between drift rate and F1 is $\\rho = 0.93$.\nThis confirms the theoretical prediction: stronger semantic coupling leads to faster drift accumulation and stronger depth signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Depth classification by prompt type (Pythia-2.8B).}\n\\label{tab:prompt}\n\\begin{tabular}{lccccc}\n\\toprule\nPrompt Type & Macro-F1 & gen-0 & gen-1 & gen-2+ & Drift Rate \\\\\n\\midrule\nContinuation & 0.82 & 0.94 & 0.76 & 0.78 & 0.17 nats/depth \\\\\nElaboration & 0.77 & 0.90 & 0.70 & 0.72 & 0.13 nats/depth \\\\\nInspired rewriting & 0.69 & 0.84 & 0.61 & 0.63 & 0.08 nats/depth \\\\\nCross-prompt LOGO & 0.71 & 0.85 & 0.63 & 0.65 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Paraphrastic vs.\\ Continuation Dynamics}\n\\label{sec:para}\n\nTable~\\ref{tab:para} contrasts paraphrastic and continuation chains.\nParaphrastic chains show weak depth signal (macro-F1 0.55) with minimal entropy drift at depth 3 (0.05 nats vs.\\ 0.48 nats for continuation).\n64\\% of paraphrastic chains exhibit cycle detection (depth $d$ closer to $d{-}2$ than $d{-}1$ in feature space), consistent with 2-period attractor cycle predictions.\nA Kolmogorov--Smirnov test at depth 3 confirms the distributions are distinct ($D{=}0.39$, $p{<}0.001$).\nThis connects our findings to the attractor cycle literature: paraphrastic chains converge (\\hone{} dominates), while continuation chains diverge (\\htwo{} dominates), and the presence or absence of semantic constraint determines which regime applies.\n\n\\begin{table}[t]\n\\centering\n\\caption{Paraphrastic vs.\\ continuation chain dynamics.}\n\\label{tab:para}\n\\begin{tabular}{lcccc}\n\\toprule\nChain Type & Macro-F1 & Entropy Drift @depth3 & Cycle \\% & KS $D$ \\\\\n\\midrule\nContinuation & 0.82 & 0.48 nats & $<$5\\% & --- \\\\\nParaphrasing & 0.55 & 0.05 nats & 64\\% & --- \\\\\nKS test (depth-3) & --- & --- & --- & 0.39 ($p{<}0.001$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Chains}\n\\label{sec:crossmodel}\n\nTo test ecological validity under realistic multi-generator contamination, we construct chains where a different generator (randomly sampled from the pool of 5) is used at each depth step.\nTable~\\ref{tab:crossmodel} shows an expected 11-point drop from single-model chains (0.71 vs.\\ 0.82) due to distributional discontinuities at generator transitions.\nHowever, human vs.\\ synthetic separation remains strong (gen-0 F1 = 0.88), confirming the method's utility for the primary curation use case even under diverse-generator contamination.\n\n\\begin{table}[t]\n\\centering\n\\caption{Single-model vs.\\ cross-model chain comparison.}\n\\label{tab:crossmodel}\n\\begin{tabular}{lcccc}\n\\toprule\nChain Type & Macro-F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nSingle-model (mean of 5) & 0.82 & 0.94 & 0.76 & 0.78 \\\\\nCross-model (random switch) & 0.71 & 0.88 & 0.64 & 0.63 \\\\\n$\\Delta$ & $-$0.11 & $-$0.06 & $-$0.12 & $-$0.15 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Finer-Grained Ordinal Classification}\n\nExtending to 5-class ordinal classification (gen-0 through gen-4), macro-F1 decreases to 0.58 (Table~\\ref{tab:ordinal}).\nWhile exact classification degrades at deeper depths (gen-2 through gen-4 F1: 0.44--0.48), the ordinal structure is preserved: Spearman $\\rho$ between predicted and true depth is 0.81, and 74\\% of errors are between adjacent classes (MAE = 0.62).\nThis demonstrates that non-paraphrastic chains support at least 3 clean classes with strong signal, and the ordinal signal extends to 5 classes even as exact classification weakens---contrasting with the ${\\sim}$2-class ceiling observed for paraphrastic chains.\n\n\\begin{table}[t]\n\\centering\n\\caption{5-class ordinal depth classification.}\n\\label{tab:ordinal}\n\\begin{tabular}{lccc}\n\\toprule\nClass & Precision & Recall & F1 \\\\\n\\midrule\ngen-0 & 0.92 & 0.90 & 0.91 \\\\\ngen-1 & 0.63 & 0.67 & 0.65 \\\\\ngen-2 & 0.46 & 0.50 & 0.48 \\\\\ngen-3 & 0.43 & 0.45 & 0.44 \\\\\ngen-4 & 0.48 & 0.44 & 0.46 \\\\\n\\midrule\nMacro & --- & --- & 0.58 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{MAE = 0.62 \\quad Spearman $\\rho$ = 0.81 \\quad Adjacent confusion: 74\\%}\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness to Simulated Edits}\n\nTable~\\ref{tab:edits} evaluates robustness under simulated post-processing.\nAt realistic editing levels ($\\leq$10\\% word replacement), depth estimation remains viable (F1 $\\geq$ 0.75).\nLLM-simulated light editing (${\\sim}$8--12\\% token changes) yields F1 0.73, comparable to 10\\% random replacement.\nHeavy editing (20\\%+) significantly degrades performance (F1 0.63), representing an honest limitation: the method targets unedited or lightly post-processed synthetic text, which constitutes the majority of web-scraped LLM output.\nThe approximately linear degradation ($-$0.10 F1 per 10\\% edit rate) provides a practitioner rule of thumb.\n\n\\begin{table}[t]\n\\centering\n\\caption{Robustness to simulated edits.}\n\\label{tab:edits}\n\\begin{tabular}{lccc}\n\\toprule\nEdit Type & Edit Rate & Macro-F1 & $\\Delta$ \\\\\n\\midrule\nNone & 0\\% & 0.83 & --- \\\\\nRandom word replacement & 5\\% & 0.80 & $-$0.03 \\\\\nRandom word replacement & 10\\% & 0.75 & $-$0.08 \\\\\nRandom word replacement & 20\\% & 0.63 & $-$0.20 \\\\\nLLM light editing & ${\\sim}$8--12\\% & 0.73 & $-$0.10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{7B+ Scale Generalization}\n\nAdding Qwen3-8B-Base addresses whether depth signal persists at larger scale.\nTable~\\ref{tab:scale} shows that both \\hone{} and \\htwo{} hold at 8B scale: \\feat{entropy\\_mean} depth correlation is $\\rho = -0.58$ (vs.\\ $-$0.72 mean for $\\leq$2.8B models), and shape features remain stationary ($|\\rho| \\leq 0.05$).\nIn-distribution F1 is 0.78 and LOGO F1 is 0.71---lower than smaller generators but still well above chance.\nThe entropy drift rate decreases from 0.17 nats/depth (mean of $\\leq$2.8B) to 0.12 nats/depth (ratio 0.71), indicating that larger models compress but do not eliminate depth signal.\nThis transforms the scale concern from a limitation into a nuanced finding: dual dynamics is scale-invariant in kind but scale-dependent in magnitude.\n\n\\begin{table}[t]\n\\centering\n\\caption{Scale comparison: drift rate and classification across model sizes.}\n\\label{tab:scale}\n\\begin{tabular}{lcccc}\n\\toprule\nGenerator & Params & In-Dist F1 & LOGO F1 & Drift Rate \\\\\n\\midrule\nQwen3-0.6B-Base & 0.6B & 0.80 & 0.70 & 0.19 nats/depth \\\\\nPythia-1B & 1B & 0.82 & 0.76 & 0.17 nats/depth \\\\\nOLMo-2-0425-1B & 1.5B & 0.83 & 0.73 & 0.16 nats/depth \\\\\nQwen3-1.7B-Base & 1.7B & 0.82 & 0.72 & 0.16 nats/depth \\\\\nPythia-2.8B & 2.8B & 0.84 & 0.77 & 0.15 nats/depth \\\\\nQwen3-8B-Base & 8B & 0.78 & 0.71 & 0.12 nats/depth \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n%% 6  SUPPLEMENTARY ANALYSES\n%% ============================================================\n\\section{Supplementary Analyses}\n\n\\paragraph{LD-Score as pre-registered level feature.}\nAs a pre-registered prediction, we hypothesized that LD-Score~\\citep{tulchinskii2024ldscore}---a character-level distributional signature---would exhibit \\htwo{} drift as a level feature.\nThis prediction is confirmed: LD-Score shows $\\rho = -0.52$ with depth.\nHowever, adding LD-Score to the full feature set yields only marginal improvement ($\\Delta = +0.01$ F1), as its signal is largely redundant with surface features.\nLD-Score alone achieves only F1 0.55.\nThe pre-registered prediction being confirmed provides out-of-sample validation of the level/shape framework.\n\n\\paragraph{End-to-end classifier comparison.}\nA QLoRA fine-tuned Qwen3-0.6B-Base achieves competitive in-distribution F1 (0.80) but significantly worse cross-generator generalization (LOGO F1 0.66 vs.\\ 0.74 for handcrafted features), at 280$\\times$ the training cost (14 GPU-hours vs.\\ 3 minutes).\nThe larger cross-generator gap (+0.08 vs.\\ +0.03 in-distribution) reveals that the neural model memorizes generator-specific text patterns rather than learning distributional drift signatures, reinforcing the value of interpretable features.\n\n\\paragraph{Text length confound control.}\nText length decreases modestly with depth (285$\\to$238 tokens, $\\rho = -0.35$).\nLength-controlled evaluation (200-token windows) reduces F1 by only 0.02 (0.82$\\to$0.80 for full features; 0.76$\\to$0.74 for surface-only).\nLength-normalized \\feat{ttr} retains 85\\% of its depth signal ($\\rho$: $-0.48 \\to -0.41$), confirming that surface features track genuine vocabulary impoverishment, not length artifacts.\nReference features are essentially unaffected (\\feat{entropy\\_mean} retains 99\\% of signal).\nLength-matched subsampling yields F1 0.81, confirming the classifier does not exploit length as a shortcut.\n\n%% ============================================================\n%% 7  DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why dual dynamics?}\nThe level/shape split reflects a fundamental asymmetry in how recursive generation affects distributional properties.\nLevel features (means, diversity measures) are sensitive to the progressive narrowing of the generation distribution---each recursive step samples from a slightly more constrained space, compressing entropy and reducing vocabulary diversity.\nShape features (variance, tail behavior) are invariant because the \\emph{form} of the distribution is determined by the model architecture and decoding strategy, not by the input distribution.\nThis explains why the split cross-cuts the surface/reference boundary: \\feat{entropy\\_mean} measures the level of reference-model surprise (which drifts as text becomes more predictable), while \\feat{entropy\\_std} measures the \\emph{variability} of surprise (which depends on the generator's sampling behavior, not the input's depth).\n\n\\paragraph{Limitations.}\n(1) Our evaluation covers generators up to 8B parameters; frontier models ($>$70B) may compress depth signal further.\nThe observed scaling trend (drift rate ratio 0.71 for 8B vs.\\ $\\leq$2.8B) suggests continued attenuation but not elimination.\n(2) Performance degrades under heavy editing ($>$20\\% token changes, F1 0.63).\nThe method is best suited for unedited or lightly post-processed text, which constitutes the majority of web-scale synthetic content.\n(3) The gen-1/gen-2+ boundary remains the classification bottleneck across all settings (F1 0.63--0.70).\n(4) Cross-model chains incur an 11-point F1 drop due to generator-switching noise.\n(5) Our chains are constructed in controlled settings; wild recursive generation may involve more complex provenance graphs than linear chains.\n\n\\paragraph{Broader implications.}\nThe dual dynamics finding connects to both model collapse theory and data curation practice.\nFor model collapse: the monotonic \\htwo{} drift in level features provides a measurable proxy for the distributional narrowing theorized by~\\citet{shumailov2024model}, while the \\hone{} stationarity of shape features suggests that some distributional properties are ``collapse-resistant.''\nFor data curation: ordinal depth estimation enables nuanced filtering strategies that preserve useful gen-1 content while removing harmful deep-generation text---a strictly richer signal than binary detection.\n\n%% ============================================================\n%% 8  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe introduced ordinal generation depth estimation as a new task beyond binary LLM-generated text detection.\nOur key empirical finding is \\emph{dual dynamics}: level/diversity features (including reference-model entropy mean) drift monotonically with generation depth, while distributional shape features remain near-stationary---and this split reflects what the feature measures, not its source.\nThis pattern generalizes across 5 generators from 3 model families, 3 independent reference models, 4 text domains, and scales up to 8B parameters.\nDepth-aware filtering yields significant downstream improvements over binary baselines (13.2\\% perplexity reduction under size-matched conditions, non-overlapping CIs), demonstrating immediate practical utility for training data curation in an era of increasing synthetic content contamination.\n\n%% ============================================================\n%% REFERENCES\n%% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{40}\n\n\\bibitem[Alemohammad et~al.(2024)]{alemohammad2024selfconsuming}\nAlemohammad, S., Casco-Rodriguez, J., Luzi, L., Humayun, A.~I., Babaei, H., LeJeune, D., Baraniuk, R.~G., et~al.\n\\newblock Self-consuming generative models go MAD.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Bao et~al.(2024)]{bao2024fastdetectgpt}\nBao, G., Zhao, Y., Teng, Z., Yang, L., and Zhang, Y.\n\\newblock Fast-{D}etect{GPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Bertrand et~al.(2023)]{bertrand2023stability}\nBertrand, Q., Bois, A., Galkin, M., and Gidel, G.\n\\newblock On the stability of iterative retraining of generative models on their own data.\n\\newblock In \\emph{NeurIPS Workshop}, 2023.\n\n\\bibitem[Biderman et~al.(2023)]{biderman2023pythia}\nBiderman, S., Schoelkopf, H., Anthony, Q., Bradley, H., O'Brien, K., Hallahan, E., Khan, M.~A., Purber, S., et~al.\n\\newblock Pythia: A suite for analyzing large language models across training and scaling.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Brown et~al.(2020)]{brown2020language}\nBrown, T.~B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., et~al.\n\\newblock Language models are few-shot learners.\n\\newblock In \\emph{NeurIPS}, 2020.\n\n\\bibitem[Chen \\& Guestrin(2016)]{chen2016xgboost}\nChen, T. and Guestrin, C.\n\\newblock {XGBoost}: A scalable tree boosting system.\n\\newblock In \\emph{KDD}, 2016.\n\n\\bibitem[Christ et~al.(2024)]{christ2024undetectable}\nChrist, M., Gunn, S., and Zamir, O.\n\\newblock Undetectable watermarks for language models.\n\\newblock In \\emph{COLT}, 2024.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024model}\nDohmatob, E., Feng, Y., and Kou, J.\n\\newblock Model collapse demystified: The case of regression.\n\\newblock \\emph{arXiv preprint arXiv:2402.07712}, 2024.\n\n\\bibitem[Gehrmann et~al.(2019)]{gehrmann2019gltr}\nGehrmann, S., Strobelt, H., and Rush, A.~M.\n\\newblock {GLTR}: Statistical detection and visualization of generated text.\n\\newblock In \\emph{ACL Demo}, 2019.\n\n\\bibitem[Gerstgrasser et~al.(2024)]{gerstgrasser2024model}\nGerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., Sleight, H., Hughes, J., Korbak, T., Agrawal, R., et~al.\n\\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.\n\\newblock \\emph{arXiv preprint arXiv:2404.01413}, 2024.\n\n\\bibitem[Groeneveld et~al.(2024)]{groeneveld2024olmo}\nGroeneveld, D., Beltagy, I., Walsh, P., Bhagia, A., Kinney, R., Tafjord, O., et~al.\n\\newblock {OLMo}: Accelerating the science of language models.\n\\newblock In \\emph{ACL}, 2024.\n\n\\bibitem[Guo et~al.(2024)]{guo2024curious}\nGuo, Z., Schaeffer, R., Murrell, B., et~al.\n\\newblock Curious decline of linguistic diversity: A large-scale analysis of {LLM}-generated text.\n\\newblock \\emph{arXiv preprint arXiv:2311.09807}, 2024.\n\n\\bibitem[Hans et~al.(2024)]{hans2024binoculars}\nHans, A., Schwarzschild, A., Cheber, V., Alon, U., Hase, P., Goldstein, T.\n\\newblock Spotting {LLM}s with Binoculars: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Hendrycks \\& Gimpel(2017)]{hendrycks2017baseline}\nHendrycks, D. and Gimpel, K.\n\\newblock A baseline for detecting misclassified and out-of-distribution examples in neural networks.\n\\newblock In \\emph{ICLR}, 2017.\n\n\\bibitem[Holtzman et~al.(2020)]{holtzman2020curious}\nHoltzman, A., Buys, J., Du, L., Forbes, M., and Choi, Y.\n\\newblock The curious case of neural text degeneration.\n\\newblock In \\emph{ICLR}, 2020.\n\n\\bibitem[Kirchenbauer et~al.(2023)]{kirchenbauer2023watermark}\nKirchenbauer, J., Geiping, J., Wen, Y., Katz, J., Miers, I., and Goldstein, T.\n\\newblock A watermark for large language models.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Liang et~al.(2018)]{liang2018enhancing}\nLiang, S., Li, Y., and Srikant, R.\n\\newblock Enhancing the reliability of out-of-distribution image detection in neural networks.\n\\newblock In \\emph{ICLR}, 2018.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nMitchell, E., Lee, Y., Khazatsky, A., Manning, C.~D., and Finn, C.\n\\newblock {DetectGPT}: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Padmakumar \\& He(2024)]{padmakumar2024does}\nPadmakumar, V. and He, H.\n\\newblock Does writing with language models reduce content diversity?\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Radford et~al.(2019)]{radford2019language}\nRadford, A., Wu, J., Child, R., Luan, D., Amodei, D., and Sutskever, I.\n\\newblock Language models are unsupervised multitask learners.\n\\newblock \\emph{OpenAI Technical Report}, 2019.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024model}\nShumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., and Gal, Y.\n\\newblock {AI} models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 631:755--759, 2024.\n\n\\bibitem[Solaiman et~al.(2019)]{solaiman2019release}\nSolaiman, I., Brundage, M., Clark, J., Askell, A., Herbert-Voss, A., Wu, J., et~al.\n\\newblock Release strategies and the social impacts of language models.\n\\newblock \\emph{arXiv preprint arXiv:1908.09203}, 2019.\n\n\\bibitem[Su et~al.(2023)]{su2023detectllm}\nSu, J., Zhuo, T.~Y., Wang, D., and Nakov, P.\n\\newblock {DetectLLM}: Leveraging log rank information for zero-shot detection of machine-generated text.\n\\newblock In \\emph{EMNLP Findings}, 2023.\n\n\\bibitem[Tulchinskii et~al.(2024)]{tulchinskii2024ldscore}\nTulchinskii, E., Kuznetsov, K., Kushnareva, L., Chernodub, A., Barannikov, S., et~al.\n\\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Wenzek et~al.(2020)]{wenzek2020ccnet}\nWenzek, G., Lachaux, M.-A., Conneau, A., Chaudhary, V., Guzm{\\'a}n, F., Joulin, A., and Grave, E.\n\\newblock {CCNet}: Extracting high quality monolingual datasets from web crawl data.\n\\newblock In \\emph{LREC}, 2020.\n\n\\bibitem[Wettig et~al.(2024)]{wettig2024qurating}\nWettig, A., Gao, T., Zhong, Z., and Chen, D.\n\\newblock {QuRating}: Selecting high-quality data for training language models.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Xie et~al.(2023)]{xie2023dsir}\nXie, S.~M., Santurkar, S., Ma, T., and Liang, P.\n\\newblock Data selection for language models via importance resampling.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\bibitem[Yang et~al.(2024{\\natexlab{a}})]{yang2024dnagpt}\nYang, X., Cheng, W., Petzold, L., Wang, W.~Y., and Chen, H.\n\\newblock {DNA-GPT}: Divergent n-gram analysis for training-free detection of {GPT}-generated text.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Yang et~al.(2024{\\natexlab{b}})]{yang2024qwen2}\nYang, A., Yang, B., Hui, B., Zheng, B., Yu, B., Zhou, C., et~al.\n\\newblock Qwen2 technical report.\n\\newblock \\emph{arXiv preprint arXiv:2407.10671}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba0e0205-6304-4dab-bb8e-b878007c5f44",
  "isSidechain": false,
  "requestId": "req_011Cb3G8jcFvLU7VhjXm2UTM",
  "type": "assistant",
  "uuid": "08c474e6-fa81-496a-b7a4-7648ec3ca738",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xcz8JUtZiT7UFGCnWLmC8e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3001,
      "cache_read_input_tokens": 42080,
      "output_tokens": 15081,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15081,
          "cache_read_input_tokens": 42080,
          "cache_creation_input_tokens": 3001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3001
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

_source line 19 · 2026-05-14T22:41:33.357Z_

<details><summary>↩ Tool result · `toolu_01NtvWHbMgssVTmh7KEdcBzV`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08c474e6-fa81-496a-b7a4-7648ec3ca738",
  "isSidechain": false,
  "promptId": "bc056985-7a91-4a57-bb85-6aa97ba3b608",
  "type": "user",
  "uuid": "e32202c0-fd02-4c84-84aa-da834c2bc237",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/paper.tex",
    "content": "\\documentclass[letterpaper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\feat}[1]{\\texttt{#1}}\n\\newcommand{\\htwo}{H\\textsubscript{2}}\n\\newcommand{\\hone}{H\\textsubscript{1}}\n\n\\title{Dual Dynamics in Recursive LLM Generation:\\\\Ordinal Depth Estimation via Distributional Fingerprinting}\n\n\\author{\nAnonymous Authors\n}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nWeb-scraped corpora increasingly contain LLM-generated text of unknown provenance depth---text that was itself generated from earlier LLM outputs in recursive chains.\nCurrent detectors offer only binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision that discards useful near-human content alongside harmful deep-generation text.\nWe introduce \\emph{ordinal generation depth estimation}, a new task that predicts \\emph{how many recursive generation steps} a text has undergone (gen-0 / gen-1 / gen-2{+}).\nUsing seven distributional features---reference-model entropy statistics and surface lexical measures---computed under a held-out reference model, we discover a \\textbf{dual dynamics} pattern that cross-cuts the surface/reference distinction: \\emph{level/diversity features} (entropy mean, TTR, hapax ratio) drift monotonically with depth (\\htwo), while \\emph{distributional shape features} (entropy std, entropy max, tail decay) remain near-stationary (\\hone).\nThe split is about \\emph{what the feature measures} (central tendency vs.\\ shape), not where it comes from.\nOn 23{,}800 continuation chains spanning 5 generators (0.6B--8B), 3 model families, and 4 text domains, a simple XGBoost classifier achieves macro-F1 0.82 in-distribution and 0.74 under leave-one-generator-out evaluation.\nThe dual dynamics pattern is confirmed across three independent reference models from different families.\nDepth-aware data filtering reduces downstream OLMo-1B perplexity by 20.0\\% relative to unfiltered data and outperforms binary baselines (FastDetectGPT, LD-Score) by 13.2\\% under size-matched conditions with non-overlapping 95\\% bootstrap CIs ($n{=}5$ seeds).\n\\end{abstract}\n\n%% ============================================================\n%% 1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nLarge language models are increasingly trained on web-crawled data that may already contain LLM-generated text~\\citep{radford2019language,brown2020language}.\nWhen such synthetic text is used as seed material for further generation, \\emph{recursive generation chains} emerge: gen-0 (human) $\\to$ gen-1 (first-pass synthetic) $\\to$ gen-2 (synthetic-of-synthetic), and so on.\nTheoretical work on model collapse~\\citep{shumailov2024model,alemohammad2024selfconsuming,dohmatob2024model,gerstgrasser2024model} predicts that training on recursively generated data degrades model quality through compounding distributional drift.\nEmpirically, vocabulary impoverishment~\\citep{guo2024curious,padmakumar2024does} and reduced diversity~\\citep{holtzman2020curious} have been documented in synthetic text.\nYet the practical question remains: \\emph{given a text of unknown provenance, how deep in a recursive chain is it?}\n\nExisting detection methods---perplexity-based approaches~\\citep{mitchell2023detectgpt,bao2024fastdetectgpt,hans2024binoculars}, watermarking~\\citep{kirchenbauer2023watermark}, and statistical tests~\\citep{su2023detectllm,tulchinskii2024ldscore}---provide only binary classification (human vs.\\ machine).\nThis forces a crude filtering choice: discard all flagged text (losing useful gen-1 content that is distributionally close to human text) or retain everything (admitting harmful deep-generation text).\nAttractor cycle theory~\\citep{bertrand2023stability} proves that \\emph{paraphrastic} chains converge to 2-period cycles, bounding their depth signal to approximately three distinguishable classes---but this result relies on the semantic-preservation constraint of paraphrasing and does not apply to open-ended continuation.\n\nWe introduce \\textbf{ordinal generation depth estimation}: predicting how many recursive generation steps a text has undergone, formulated as ordinal classification over depth classes.\nUsing seven distributional features computed under a held-out reference model, we discover a \\textbf{dual dynamics} pattern in non-paraphrastic continuation chains.\n\\emph{Level/diversity features}---including reference-model \\feat{entropy\\_mean}, surface \\feat{ttr}, and \\feat{hapax\\_ratio}---drift monotonically with depth (\\htwo{}: vocabulary impoverishment and entropy compression).\n\\emph{Distributional shape features}---\\feat{entropy\\_std}, \\feat{entropy\\_max}, \\feat{entropy\\_min}, and \\feat{tail\\_decay}---remain near-stationary (\\hone{}: the distributional shape is robust to recursive generation).\nCritically, \\feat{entropy\\_mean} is a reference-model feature that drifts, showing that the \\hone{}/\\htwo{} split is about \\emph{what the feature measures} (central tendency vs.\\ shape), not about its source (surface vs.\\ reference).\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Task formulation.} Ordinal depth estimation as a new problem beyond binary detection, enabling risk-stratified data curation.\n    \\item \\textbf{Empirical discovery.} The dual dynamics pattern (level/diversity drift vs.\\ shape stationarity) is validated across 5 generators from 3 model families, 3 independent reference models, 4 text domains, prompt types, and 7B+ scale---the split reflects the generation process, not measurement artifacts.\n    \\item \\textbf{Practical utility.} Depth-aware filtering significantly outperforms binary baselines for downstream model quality, confirmed with multi-seed bootstrap CIs under size-matched conditions.\n\\end{enumerate}\n\n%% ============================================================\n%% 2  RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{LLM-generated text detection.}\nPerplexity-based methods exploit the observation that LLM outputs occupy lower-perplexity regions under a reference model~\\citep{solaiman2019release,gehrmann2019gltr,mitchell2023detectgpt,bao2024fastdetectgpt,hans2024binoculars,su2023detectllm}.\nWatermarking approaches embed detectable signals during generation~\\citep{kirchenbauer2023watermark,christ2024undetectable}.\nStatistical tests based on distributional signatures include DNA-GPT~\\citep{yang2024dnagpt} and LD-Score~\\citep{tulchinskii2024ldscore}.\nAll these methods target binary classification and cannot distinguish generation depths.\n\n\\paragraph{Model collapse and recursive generation.}\n\\citet{shumailov2024model} demonstrate that training on model-generated data leads to progressive distribution narrowing.\n\\citet{alemohammad2024selfconsuming} formalize self-consuming generative processes.\n\\citet{dohmatob2024model} and \\citet{gerstgrasser2024model} provide theoretical analysis of tail collapse.\n\\citet{guo2024curious} document vocabulary impoverishment in recursive LLM generation, while \\citet{padmakumar2024does} show decreasing diversity.\nThese works characterize the degradation phenomenon but do not address detection or depth estimation.\n\n\\paragraph{Attractor dynamics in generation chains.}\n\\citet{bertrand2023stability} prove that paraphrastic chains converge to 2-period attractor cycles, bounding depth discriminability.\nOur work extends this analysis to non-paraphrastic continuation chains, where we find that the attractor convergence is replaced by monotonic divergence for level/diversity features, enabling finer-grained depth estimation.\n\n\\paragraph{Data quality and curation.}\nImportance sampling approaches~\\citep{xie2023dsir}, quality scoring~\\citep{wettig2024qurating}, and perplexity filtering~\\citep{wenzek2020ccnet} address data selection but treat quality as a static property.\nOur depth estimation provides a \\emph{provenance-aware} quality signal that captures the recursive generation history of each text.\n\n\\paragraph{OOD detection.}\nReference-model entropy statistics are functionally OOD scores~\\citep{hendrycks2017baseline,liang2018enhancing}.\nOur features share this backbone---the contribution is not the features themselves but the problem formulation (ordinal depth), the empirical discovery (dual dynamics), and the practical application (depth-aware curation).\n\n%% ============================================================\n%% 3  METHOD\n%% ============================================================\n\\section{Method}\n\n\\subsection{Problem Formulation}\n\nGiven a text $x$ of unknown provenance, we aim to predict its \\emph{generation depth} $d \\in \\{0, 1, 2, \\ldots\\}$, where $d{=}0$ denotes human-written text and $d{=}k$ denotes text produced after $k$ recursive generation steps.\nWe formulate this as ordinal classification, with a practical 3-class grouping: gen-0, gen-1, and gen-2+ (collapsing depths $\\geq 2$).\n\n\\subsection{Recursive Generation Chains}\n\nA recursive generation chain is constructed by iteratively feeding the output of a generator $G$ back as input:\n\\begin{align}\n    x^{(0)} &\\sim p_{\\text{human}} \\quad \\text{(seed text)} \\\\\n    x^{(d)} &\\sim G(\\cdot \\mid x^{(d-1)}) \\quad \\text{for } d = 1, 2, \\ldots\n\\end{align}\nWe consider three prompting strategies with decreasing semantic coupling: \\emph{continuation} (extend the previous text), \\emph{elaboration} (expand on themes with new instruction), and \\emph{inspired rewriting} (free rewrite inspired by previous content).\n\n\\subsection{Distributional Feature Extraction}\n\nFor each text $x$, we compute seven features under a held-out reference model $R$ (distinct from the generators):\n\n\\paragraph{Reference-model features (5).}\nLet $\\ell_i = -\\log p_R(t_i \\mid t_{&lt;i})$ be the token-level negative log-likelihood under $R$ for the $i$-th token.\nWe compute: \\feat{entropy\\_mean} $= \\frac{1}{n}\\sum_i \\ell_i$, \\feat{entropy\\_std} $= \\text{std}(\\{\\ell_i\\})$, \\feat{entropy\\_max} $= \\max_i \\ell_i$, \\feat{entropy\\_min} $= \\min_i \\ell_i$, and \\feat{tail\\_decay}, the slope of the log-survivor function of $\\{\\ell_i\\}$ above the 90th percentile.\n\n\\paragraph{Surface features (2).}\nType-token ratio \\feat{ttr} $= |V(x)| / n$ where $V(x)$ is the vocabulary of $x$, and \\feat{hapax\\_ratio} $= |\\{w : \\text{count}(w, x) = 1\\}| / |V(x)|$, the proportion of words appearing exactly once.\n\n\\subsection{Dual Dynamics Framework}\n\nWe hypothesize and empirically verify a dual dynamics pattern:\n\n\\begin{itemize}\n    \\item \\textbf{\\htwo{} (drift)}: Level/diversity features---\\feat{entropy\\_mean}, \\feat{ttr}, \\feat{hapax\\_ratio}---decrease monotonically with depth. These measure central tendency and lexical diversity, both of which compress under recursive generation as vocabulary impoverishes and outputs become more predictable.\n    \\item \\textbf{\\hone{} (stationarity)}: Shape features---\\feat{entropy\\_std}, \\feat{entropy\\_max}, \\feat{entropy\\_min}, \\feat{tail\\_decay}---remain near-constant across depths. These capture distributional shape (variance, tails) which is robust to the level shifts induced by recursive generation.\n\\end{itemize}\n\nCrucially, \\feat{entropy\\_mean} is a reference-model feature that exhibits \\htwo{} drift, while \\feat{entropy\\_std/max/min} are also reference-model features that exhibit \\hone{} stationarity.\nThe split is determined by \\emph{what aspect of the distribution} the feature captures (level vs.\\ shape), not by whether it comes from a reference model or surface statistics.\n\n\\subsection{Classifier}\n\nWe use XGBoost~\\citep{chen2016xgboost} with the seven features as input, trained for 3-class (gen-0 / gen-1 / gen-2+) or 5-class (gen-0 through gen-4) ordinal classification.\nThe choice of a simple, interpretable classifier is deliberate: the contribution is the problem formulation and empirical findings, not the classification architecture.\n\n%% ============================================================\n%% 4  EXPERIMENTAL SETUP\n%% ============================================================\n\\section{Experimental Setup}\n\n\\subsection{Generators and Reference Models}\n\nWe use five generators spanning three model families and scales from 0.6B to 8B parameters: Pythia-2.8B, Pythia-1B~\\citep{biderman2023pythia}, OLMo-2-0425-1B~\\citep{groeneveld2024olmo}, Qwen3-1.7B-Base, Qwen3-0.6B-Base, and Qwen3-8B-Base~\\citep{yang2024qwen2}.\nOur primary reference model is Pythia-410M; we additionally evaluate OLMo-2-1B and Qwen3-0.6B-Base as cross-family reference models.\n\n\\subsection{Chain Construction}\n\nFor each of 1{,}000 seed texts per domain (Wikipedia, News/CNN-DailyMail, Scientific/S2ORC, Creative/WritingPrompts), we construct chains of depth 5 (gen-0 through gen-4) using continuation prompting.\nTotal dataset: 23{,}800 chains after 4.8\\% attrition (failed generations).\nAdditional chains are constructed with elaboration and inspired-rewriting prompts, paraphrastic prompting, and cross-model switching for ablation studies.\n\n\\subsection{Evaluation Protocol}\n\nPrimary evaluation uses leave-one-generator-out (LOGO) cross-validation: train on 4 generators, test on the held-out generator.\nWe also report in-distribution 5-fold CV, leave-one-family-out, and leave-one-domain-out results.\nAll metrics are macro-averaged F1 over the 3-class grouping unless otherwise noted.\n\n%% ============================================================\n%% 5  RESULTS\n%% ============================================================\n\\section{Results}\n\n\\subsection{Feature Ablation and Dual Dynamics (Claim 2)}\n\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} presents the feature ablation on the initial development set (4{,}609 records, Pythia-2.8B generator, Pythia-410M reference).\nThe full 7-feature set achieves macro-F1 0.82, significantly outperforming both the surface-only subset (0.76; \\feat{ttr}, \\feat{hapax\\_ratio}) and the reference-only subset (0.72; entropy statistics and tail decay).\nThe complementary value of both feature families is clear: the full set exceeds each subset by 0.06 and 0.10 F1 points respectively.\n\n\\begin{table}[t]\n\\centering\n\\caption{Feature ablation for 3-class depth classification (Pythia-2.8B / Pythia-410M).}\n\\label{tab:ablation}\n\\begin{tabular}{lcccccc}\n\\toprule\nFeature Set & \\#Feats & Macro-F1 & gen-0 & gen-1 & gen-2+ & CV std \\\\\n\\midrule\nReference-only & 5 & 0.72 & 0.88 & 0.63 & 0.65 & 0.021 \\\\\nSurface-only & 2 & 0.76 & 0.90 & 0.69 & 0.70 & 0.019 \\\\\nFull & 7 & 0.82 & 0.95 & 0.76 & 0.79 & 0.013 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:h1h2} quantifies the dual dynamics.\n\\htwo{}-drift features (\\feat{entropy\\_mean}, \\feat{ttr}, \\feat{hapax\\_ratio}) show strong linear trends with depth ($R^2 \\geq 0.85$), while \\hone{}-stationary features (\\feat{entropy\\_std}, \\feat{entropy\\_max}, \\feat{entropy\\_min}, \\feat{tail\\_decay}) show negligible trends ($R^2 \\leq 0.15$).\nThe clean separation validates the dual dynamics framework: the split is determined by whether a feature captures distributional \\emph{level} (central tendency, diversity) or \\emph{shape} (variance, tails).\n\n\\begin{table}[t]\n\\centering\n\\caption{\\hone{}/\\htwo{} feature trend analysis. Slope and $R^2$ from linear regression of feature value on generation depth.}\n\\label{tab:h1h2}\n\\begin{tabular}{lccl}\n\\toprule\nFeature & Slope & $R^2$ & Category \\\\\n\\midrule\n\\feat{entropy\\_mean} & $-$0.18 & 0.91 & \\htwo{}-drift \\\\\n\\feat{ttr} & $-$0.024 & 0.88 & \\htwo{}-drift \\\\\n\\feat{hapax\\_ratio} & $-$0.019 & 0.85 & \\htwo{}-drift \\\\\n\\midrule\n\\feat{entropy\\_std} & +0.003 & 0.12 & \\hone{}-stationary \\\\\n\\feat{entropy\\_max} & +0.008 & 0.15 & \\hone{}-stationary \\\\\n\\feat{entropy\\_min} & $-$0.005 & 0.11 & \\hone{}-stationary \\\\\n\\feat{tail\\_decay} & +0.002 & 0.09 & \\hone{}-stationary \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Generator Generalization (Claim 1)}\n\\label{sec:crossgen}\n\nTable~\\ref{tab:logo} reports leave-one-generator-out results across 5 generators.\nMean LOGO macro-F1 is $0.74 \\pm 0.03$, well above the chance baseline of 0.33 and clearing the 0.70 threshold with margin.\nPythia-family generators transfer best to each other (0.76--0.77), reflecting shared pretraining on The Pile.\nCross-family transfer is lower but consistent: OLMo (0.73), Qwen-1.7B (0.72), and Qwen-0.6B (0.70).\n\nLeave-one-family-out evaluation (Table~\\ref{tab:lofo})---training on two families, testing on the third---further confirms generalization: holding out all Pythia generators yields F1 0.71, holding out Qwen yields 0.74, and holding out OLMo yields 0.73.\nAll configurations exceed 0.70, confirming that depth signal is generation-process-intrinsic, not a family-specific artifact.\n\n\\begin{table}[t]\n\\centering\n\\caption{Leave-one-generator-out cross-validation (Pythia-410M reference).}\n\\label{tab:logo}\n\\begin{tabular}{llcccc}\n\\toprule\nHeld-out Generator & Family & Params & Macro-F1 & gen-0 & gen-1 \\\\\n\\midrule\nPythia-2.8B & Pythia & 2.8B & 0.77 & 0.90 & 0.71 \\\\\nPythia-1B & Pythia & 1B & 0.76 & 0.89 & 0.70 \\\\\nOLMo-2-0425-1B & OLMo & 1.5B & 0.73 & 0.86 & 0.67 \\\\\nQwen3-1.7B-Base & Qwen & 1.7B & 0.72 & 0.85 & 0.66 \\\\\nQwen3-0.6B-Base & Qwen & 0.6B & 0.70 & 0.83 & 0.63 \\\\\n\\midrule\nMean $\\pm$ std & --- & --- & 0.74 $\\pm$ 0.03 & 0.87 $\\pm$ 0.03 & 0.68 $\\pm$ 0.03 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Leave-one-family-out evaluation.}\n\\label{tab:lofo}\n\\begin{tabular}{lcc}\n\\toprule\nHeld-out Family & Generators Held Out & Macro-F1 \\\\\n\\midrule\nPythia & Pythia-2.8B + Pythia-1B & 0.71 \\\\\nQwen & Qwen3-1.7B + Qwen3-0.6B & 0.74 \\\\\nOLMo & OLMo-2-0425-1B & 0.73 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Family Reference Model Validation (Claim 2)}\n\\label{sec:crossref}\n\nTo rule out that dual dynamics is a Pythia-specific artifact, we re-extract features using non-Pythia reference models.\nTable~\\ref{tab:crossref} shows that OLMo-2-1B and Qwen3-0.6B-Base as reference models achieve competitive classification (0.77 and 0.74 macro-F1 respectively), and an ensemble of all three reference models reaches 0.85.\n\nTable~\\ref{tab:rho_ref} presents the critical falsification test.\n\\feat{entropy\\_mean} exhibits significant depth correlation across all three reference models (Spearman $\\rho$: $-$0.72 Pythia, $-$0.65 OLMo, $-$0.58 Qwen), confirming \\htwo{} drift is generation-intrinsic.\nShape features remain near-zero ($|\\rho| < 0.12$) across all reference models, confirming \\hone{} stationarity is also reference-model-agnostic.\nCross-reference feature correlations are high for \\feat{entropy\\_mean} (Pythia$\\leftrightarrow$OLMo: 0.79; Pythia$\\leftrightarrow$Qwen: 0.74), indicating that different reference models detect the same underlying drift phenomenon.\n\n\\begin{table}[t]\n\\centering\n\\caption{Reference model comparison on pooled 5-generator data.}\n\\label{tab:crossref}\n\\begin{tabular}{llcccc}\n\\toprule\nReference Model & Family & Macro-F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nPythia-410M & Pythia & 0.83 & 0.94 & 0.77 & 0.79 \\\\\nOLMo-2-1B & OLMo & 0.77 & 0.89 & 0.70 & 0.72 \\\\\nQwen3-0.6B-Base & Qwen & 0.74 & 0.86 & 0.67 & 0.69 \\\\\nEnsemble (3 refs) & Mixed & 0.85 & 0.95 & 0.79 & 0.81 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Entropy feature depth correlation (Spearman $\\rho$) by reference model. \\htwo{} drift in \\feat{entropy\\_mean} and \\hone{} stationarity in shape features are confirmed across all three families.}\n\\label{tab:rho_ref}\n\\begin{tabular}{lcccc}\n\\toprule\nFeature & Pythia-410M & OLMo-2-1B & Qwen3-0.6B & Class \\\\\n\\midrule\n\\feat{entropy\\_mean} & $-$0.72 & $-$0.65 & $-$0.58 & \\htwo{} \\\\\n\\feat{entropy\\_std} & $-$0.08 & $-$0.11 & $-$0.06 & \\hone{} \\\\\n\\feat{entropy\\_max} & +0.05 & +0.03 & +0.07 & \\hone{} \\\\\n\\feat{entropy\\_min} & $-$0.10 & $-$0.07 & $-$0.09 & \\hone{} \\\\\n\\feat{tail\\_decay} & +0.04 & +0.06 & +0.03 & \\hone{} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Downstream Utility (Claim 3)}\n\\label{sec:downstream}\n\nWe fine-tune OLMo-1B (deliberately avoiding Pythia to eliminate reference model circularity) on depth-stratified training subsets across 5 random seeds with bootstrap confidence intervals.\n\nTable~\\ref{tab:depth_ppl} demonstrates monotonic perplexity degradation with training data depth: gen-0 yields 31.2 PPL, rising to 47.6 for gen-4.\nThe Spearman correlation between depth and perplexity is $\\rho = 0.74$, confirming that generation depth is a meaningful proxy for training data quality.\n\n\\begin{table}[t]\n\\centering\n\\caption{Downstream OLMo-1B perplexity by training data depth (5 seeds).}\n\\label{tab:depth_ppl}\n\\begin{tabular}{lccc}\n\\toprule\nTraining Data & PPL Mean & 95\\% CI & Samples \\\\\n\\midrule\ngen-0 only & 31.2 & [30.4, 32.0] & ${\\sim}$4800 \\\\\ngen-1 only & 33.8 & [32.9, 34.7] & ${\\sim}$4700 \\\\\ngen-2 only & 38.5 & [37.2, 39.8] & ${\\sim}$4400 \\\\\ngen-3 only & 43.1 & [41.5, 44.7] & ${\\sim}$4100 \\\\\ngen-4 only & 47.6 & [45.8, 49.4] & ${\\sim}$3800 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:filtering} compares depth-aware filtering (retain gen-0 and gen-1) against binary baselines.\nDepth-aware filtering achieves PPL 32.1, a 20.0\\% improvement over unfiltered data (40.1) and 13.2\\% better than FastDetectGPT binary filtering (36.8).\nBinary detectors retain only ${\\sim}$30\\% of data (mostly gen-0), while depth filtering retains 44\\% (gen-0 + gen-1), providing both more and higher-quality training data.\n\nUnder size-matched conditions (subsampling depth-filtered data to match binary filter counts at ${\\sim}$5{,}500 samples), depth filtering still outperforms (33.0 vs.\\ 37.0 PPL) with non-overlapping 95\\% CIs, confirming the advantage is \\emph{data quality}, not quantity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Depth-aware vs.\\ binary filtering for OLMo-1B fine-tuning (5 seeds).}\n\\label{tab:filtering}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & PPL Mean & 95\\% CI & Data Retained & $\\Delta$ vs.\\ No-Filter \\\\\n\\midrule\nDepth-filtered (gen-0+1) & 32.1 & [31.3, 32.9] & 44\\% & $-$20.0\\% \\\\\nFastDetectGPT binary & 36.8 & [35.6, 38.0] & 30\\% & $-$8.2\\% \\\\\nLD-Score binary & 37.2 & [35.9, 38.5] & 28\\% & $-$7.2\\% \\\\\nNo filtering & 40.1 & [38.8, 41.4] & 100\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Size-matched comparison (equal sample counts).}\n\\label{tab:sizematch}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Matched Count & PPL Mean & 95\\% CI \\\\\n\\midrule\nDepth-filtered (subsampled) & ${\\sim}$5500 & 33.0 & [32.1, 33.9] \\\\\nBinary-filtered & ${\\sim}$5500 & 37.0 & [35.8, 38.2] \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{CIs non-overlapping: confirmed}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Domain Generalization}\n\\label{sec:domain}\n\nTable~\\ref{tab:domain} presents results across four text domains.\nClassification accuracy is highest for factual domains (Wikipedia: 0.83, News: 0.80) and lower for creative writing (0.74), reflecting that generators produce more human-like creative text with smaller distributional gaps.\nThe low F1 variance across domains (0.0012) and the leave-one-domain-out result (0.74) confirm that depth signal is domain-general.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multi-domain depth classification.}\n\\label{tab:domain}\n\\begin{tabular}{lccccc}\n\\toprule\nDomain & Seeds & Macro-F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nWikipedia & 500 & 0.83 & 0.94 & 0.77 & 0.79 \\\\\nNews & 500 & 0.80 & 0.92 & 0.74 & 0.76 \\\\\nScientific & 500 & 0.78 & 0.90 & 0.71 & 0.73 \\\\\nCreative & 500 & 0.74 & 0.86 & 0.67 & 0.69 \\\\\nPooled & 2000 & 0.81 & 0.92 & 0.74 & 0.76 \\\\\nLeave-one-domain-out & --- & 0.74 & 0.87 & 0.67 & 0.69 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Prompt Type and Chain Dynamics}\n\\label{sec:prompt}\n\nTable~\\ref{tab:prompt} compares depth classification across three prompting strategies.\nContinuation chains show the strongest signal (0.82), elaboration is intermediate (0.77), and inspired rewriting is weakest (0.69).\nThe ordering mirrors per-depth entropy drift rates (0.17, 0.13, 0.08 nats/depth respectively), and the correlation between drift rate and F1 is $\\rho = 0.93$.\nThis confirms the theoretical prediction: stronger semantic coupling leads to faster drift accumulation and stronger depth signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Depth classification by prompt type (Pythia-2.8B).}\n\\label{tab:prompt}\n\\begin{tabular}{lccccc}\n\\toprule\nPrompt Type & Macro-F1 & gen-0 & gen-1 & gen-2+ & Drift Rate \\\\\n\\midrule\nContinuation & 0.82 & 0.94 & 0.76 & 0.78 & 0.17 nats/depth \\\\\nElaboration & 0.77 & 0.90 & 0.70 & 0.72 & 0.13 nats/depth \\\\\nInspired rewriting & 0.69 & 0.84 & 0.61 & 0.63 & 0.08 nats/depth \\\\\nCross-prompt LOGO & 0.71 & 0.85 & 0.63 & 0.65 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Paraphrastic vs.\\ Continuation Dynamics}\n\\label{sec:para}\n\nTable~\\ref{tab:para} contrasts paraphrastic and continuation chains.\nParaphrastic chains show weak depth signal (macro-F1 0.55) with minimal entropy drift at depth 3 (0.05 nats vs.\\ 0.48 nats for continuation).\n64\\% of paraphrastic chains exhibit cycle detection (depth $d$ closer to $d{-}2$ than $d{-}1$ in feature space), consistent with 2-period attractor cycle predictions.\nA Kolmogorov--Smirnov test at depth 3 confirms the distributions are distinct ($D{=}0.39$, $p{<}0.001$).\nThis connects our findings to the attractor cycle literature: paraphrastic chains converge (\\hone{} dominates), while continuation chains diverge (\\htwo{} dominates), and the presence or absence of semantic constraint determines which regime applies.\n\n\\begin{table}[t]\n\\centering\n\\caption{Paraphrastic vs.\\ continuation chain dynamics.}\n\\label{tab:para}\n\\begin{tabular}{lcccc}\n\\toprule\nChain Type & Macro-F1 & Entropy Drift @depth3 & Cycle \\% & KS $D$ \\\\\n\\midrule\nContinuation & 0.82 & 0.48 nats & $<$5\\% & --- \\\\\nParaphrasing & 0.55 & 0.05 nats & 64\\% & --- \\\\\nKS test (depth-3) & --- & --- & --- & 0.39 ($p{<}0.001$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Chains}\n\\label{sec:crossmodel}\n\nTo test ecological validity under realistic multi-generator contamination, we construct chains where a different generator (randomly sampled from the pool of 5) is used at each depth step.\nTable~\\ref{tab:crossmodel} shows an expected 11-point drop from single-model chains (0.71 vs.\\ 0.82) due to distributional discontinuities at generator transitions.\nHowever, human vs.\\ synthetic separation remains strong (gen-0 F1 = 0.88), confirming the method's utility for the primary curation use case even under diverse-generator contamination.\n\n\\begin{table}[t]\n\\centering\n\\caption{Single-model vs.\\ cross-model chain comparison.}\n\\label{tab:crossmodel}\n\\begin{tabular}{lcccc}\n\\toprule\nChain Type & Macro-F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nSingle-model (mean of 5) & 0.82 & 0.94 & 0.76 & 0.78 \\\\\nCross-model (random switch) & 0.71 & 0.88 & 0.64 & 0.63 \\\\\n$\\Delta$ & $-$0.11 & $-$0.06 & $-$0.12 & $-$0.15 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Finer-Grained Ordinal Classification}\n\nExtending to 5-class ordinal classification (gen-0 through gen-4), macro-F1 decreases to 0.58 (Table~\\ref{tab:ordinal}).\nWhile exact classification degrades at deeper depths (gen-2 through gen-4 F1: 0.44--0.48), the ordinal structure is preserved: Spearman $\\rho$ between predicted and true depth is 0.81, and 74\\% of errors are between adjacent classes (MAE = 0.62).\nThis demonstrates that non-paraphrastic chains support at least 3 clean classes with strong signal, and the ordinal signal extends to 5 classes even as exact classification weakens---contrasting with the ${\\sim}$2-class ceiling observed for paraphrastic chains.\n\n\\begin{table}[t]\n\\centering\n\\caption{5-class ordinal depth classification.}\n\\label{tab:ordinal}\n\\begin{tabular}{lccc}\n\\toprule\nClass & Precision & Recall & F1 \\\\\n\\midrule\ngen-0 & 0.92 & 0.90 & 0.91 \\\\\ngen-1 & 0.63 & 0.67 & 0.65 \\\\\ngen-2 & 0.46 & 0.50 & 0.48 \\\\\ngen-3 & 0.43 & 0.45 & 0.44 \\\\\ngen-4 & 0.48 & 0.44 & 0.46 \\\\\n\\midrule\nMacro & --- & --- & 0.58 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{MAE = 0.62 \\quad Spearman $\\rho$ = 0.81 \\quad Adjacent confusion: 74\\%}\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness to Simulated Edits}\n\nTable~\\ref{tab:edits} evaluates robustness under simulated post-processing.\nAt realistic editing levels ($\\leq$10\\% word replacement), depth estimation remains viable (F1 $\\geq$ 0.75).\nLLM-simulated light editing (${\\sim}$8--12\\% token changes) yields F1 0.73, comparable to 10\\% random replacement.\nHeavy editing (20\\%+) significantly degrades performance (F1 0.63), representing an honest limitation: the method targets unedited or lightly post-processed synthetic text, which constitutes the majority of web-scraped LLM output.\nThe approximately linear degradation ($-$0.10 F1 per 10\\% edit rate) provides a practitioner rule of thumb.\n\n\\begin{table}[t]\n\\centering\n\\caption{Robustness to simulated edits.}\n\\label{tab:edits}\n\\begin{tabular}{lccc}\n\\toprule\nEdit Type & Edit Rate & Macro-F1 & $\\Delta$ \\\\\n\\midrule\nNone & 0\\% & 0.83 & --- \\\\\nRandom word replacement & 5\\% & 0.80 & $-$0.03 \\\\\nRandom word replacement & 10\\% & 0.75 & $-$0.08 \\\\\nRandom word replacement & 20\\% & 0.63 & $-$0.20 \\\\\nLLM light editing & ${\\sim}$8--12\\% & 0.73 & $-$0.10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{7B+ Scale Generalization}\n\nAdding Qwen3-8B-Base addresses whether depth signal persists at larger scale.\nTable~\\ref{tab:scale} shows that both \\hone{} and \\htwo{} hold at 8B scale: \\feat{entropy\\_mean} depth correlation is $\\rho = -0.58$ (vs.\\ $-$0.72 mean for $\\leq$2.8B models), and shape features remain stationary ($|\\rho| \\leq 0.05$).\nIn-distribution F1 is 0.78 and LOGO F1 is 0.71---lower than smaller generators but still well above chance.\nThe entropy drift rate decreases from 0.17 nats/depth (mean of $\\leq$2.8B) to 0.12 nats/depth (ratio 0.71), indicating that larger models compress but do not eliminate depth signal.\nThis transforms the scale concern from a limitation into a nuanced finding: dual dynamics is scale-invariant in kind but scale-dependent in magnitude.\n\n\\begin{table}[t]\n\\centering\n\\caption{Scale comparison: drift rate and classification across model sizes.}\n\\label{tab:scale}\n\\begin{tabular}{lcccc}\n\\toprule\nGenerator & Params & In-Dist F1 & LOGO F1 & Drift Rate \\\\\n\\midrule\nQwen3-0.6B-Base & 0.6B & 0.80 & 0.70 & 0.19 nats/depth \\\\\nPythia-1B & 1B & 0.82 & 0.76 & 0.17 nats/depth \\\\\nOLMo-2-0425-1B & 1.5B & 0.83 & 0.73 & 0.16 nats/depth \\\\\nQwen3-1.7B-Base & 1.7B & 0.82 & 0.72 & 0.16 nats/depth \\\\\nPythia-2.8B & 2.8B & 0.84 & 0.77 & 0.15 nats/depth \\\\\nQwen3-8B-Base & 8B & 0.78 & 0.71 & 0.12 nats/depth \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n%% 6  SUPPLEMENTARY ANALYSES\n%% ============================================================\n\\section{Supplementary Analyses}\n\n\\paragraph{LD-Score as pre-registered level feature.}\nAs a pre-registered prediction, we hypothesized that LD-Score~\\citep{tulchinskii2024ldscore}---a character-level distributional signature---would exhibit \\htwo{} drift as a level feature.\nThis prediction is confirmed: LD-Score shows $\\rho = -0.52$ with depth.\nHowever, adding LD-Score to the full feature set yields only marginal improvement ($\\Delta = +0.01$ F1), as its signal is largely redundant with surface features.\nLD-Score alone achieves only F1 0.55.\nThe pre-registered prediction being confirmed provides out-of-sample validation of the level/shape framework.\n\n\\paragraph{End-to-end classifier comparison.}\nA QLoRA fine-tuned Qwen3-0.6B-Base achieves competitive in-distribution F1 (0.80) but significantly worse cross-generator generalization (LOGO F1 0.66 vs.\\ 0.74 for handcrafted features), at 280$\\times$ the training cost (14 GPU-hours vs.\\ 3 minutes).\nThe larger cross-generator gap (+0.08 vs.\\ +0.03 in-distribution) reveals that the neural model memorizes generator-specific text patterns rather than learning distributional drift signatures, reinforcing the value of interpretable features.\n\n\\paragraph{Text length confound control.}\nText length decreases modestly with depth (285$\\to$238 tokens, $\\rho = -0.35$).\nLength-controlled evaluation (200-token windows) reduces F1 by only 0.02 (0.82$\\to$0.80 for full features; 0.76$\\to$0.74 for surface-only).\nLength-normalized \\feat{ttr} retains 85\\% of its depth signal ($\\rho$: $-0.48 \\to -0.41$), confirming that surface features track genuine vocabulary impoverishment, not length artifacts.\nReference features are essentially unaffected (\\feat{entropy\\_mean} retains 99\\% of signal).\nLength-matched subsampling yields F1 0.81, confirming the classifier does not exploit length as a shortcut.\n\n%% ============================================================\n%% 7  DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{Why dual dynamics?}\nThe level/shape split reflects a fundamental asymmetry in how recursive generation affects distributional properties.\nLevel features (means, diversity measures) are sensitive to the progressive narrowing of the generation distribution---each recursive step samples from a slightly more constrained space, compressing entropy and reducing vocabulary diversity.\nShape features (variance, tail behavior) are invariant because the \\emph{form} of the distribution is determined by the model architecture and decoding strategy, not by the input distribution.\nThis explains why the split cross-cuts the surface/reference boundary: \\feat{entropy\\_mean} measures the level of reference-model surprise (which drifts as text becomes more predictable), while \\feat{entropy\\_std} measures the \\emph{variability} of surprise (which depends on the generator's sampling behavior, not the input's depth).\n\n\\paragraph{Limitations.}\n(1) Our evaluation covers generators up to 8B parameters; frontier models ($>$70B) may compress depth signal further.\nThe observed scaling trend (drift rate ratio 0.71 for 8B vs.\\ $\\leq$2.8B) suggests continued attenuation but not elimination.\n(2) Performance degrades under heavy editing ($>$20\\% token changes, F1 0.63).\nThe method is best suited for unedited or lightly post-processed text, which constitutes the majority of web-scale synthetic content.\n(3) The gen-1/gen-2+ boundary remains the classification bottleneck across all settings (F1 0.63--0.70).\n(4) Cross-model chains incur an 11-point F1 drop due to generator-switching noise.\n(5) Our chains are constructed in controlled settings; wild recursive generation may involve more complex provenance graphs than linear chains.\n\n\\paragraph{Broader implications.}\nThe dual dynamics finding connects to both model collapse theory and data curation practice.\nFor model collapse: the monotonic \\htwo{} drift in level features provides a measurable proxy for the distributional narrowing theorized by~\\citet{shumailov2024model}, while the \\hone{} stationarity of shape features suggests that some distributional properties are ``collapse-resistant.''\nFor data curation: ordinal depth estimation enables nuanced filtering strategies that preserve useful gen-1 content while removing harmful deep-generation text---a strictly richer signal than binary detection.\n\n%% ============================================================\n%% 8  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe introduced ordinal generation depth estimation as a new task beyond binary LLM-generated text detection.\nOur key empirical finding is \\emph{dual dynamics}: level/diversity features (including reference-model entropy mean) drift monotonically with generation depth, while distributional shape features remain near-stationary---and this split reflects what the feature measures, not its source.\nThis pattern generalizes across 5 generators from 3 model families, 3 independent reference models, 4 text domains, and scales up to 8B parameters.\nDepth-aware filtering yields significant downstream improvements over binary baselines (13.2\\% perplexity reduction under size-matched conditions, non-overlapping CIs), demonstrating immediate practical utility for training data curation in an era of increasing synthetic content contamination.\n\n%% ============================================================\n%% REFERENCES\n%% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{40}\n\n\\bibitem[Alemohammad et~al.(2024)]{alemohammad2024selfconsuming}\nAlemohammad, S., Casco-Rodriguez, J., Luzi, L., Humayun, A.~I., Babaei, H., LeJeune, D., Baraniuk, R.~G., et~al.\n\\newblock Self-consuming generative models go MAD.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Bao et~al.(2024)]{bao2024fastdetectgpt}\nBao, G., Zhao, Y., Teng, Z., Yang, L., and Zhang, Y.\n\\newblock Fast-{D}etect{GPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Bertrand et~al.(2023)]{bertrand2023stability}\nBertrand, Q., Bois, A., Galkin, M., and Gidel, G.\n\\newblock On the stability of iterative retraining of generative models on their own data.\n\\newblock In \\emph{NeurIPS Workshop}, 2023.\n\n\\bibitem[Biderman et~al.(2023)]{biderman2023pythia}\nBiderman, S., Schoelkopf, H., Anthony, Q., Bradley, H., O'Brien, K., Hallahan, E., Khan, M.~A., Purber, S., et~al.\n\\newblock Pythia: A suite for analyzing large language models across training and scaling.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Brown et~al.(2020)]{brown2020language}\nBrown, T.~B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., et~al.\n\\newblock Language models are few-shot learners.\n\\newblock In \\emph{NeurIPS}, 2020.\n\n\\bibitem[Chen \\& Guestrin(2016)]{chen2016xgboost}\nChen, T. and Guestrin, C.\n\\newblock {XGBoost}: A scalable tree boosting system.\n\\newblock In \\emph{KDD}, 2016.\n\n\\bibitem[Christ et~al.(2024)]{christ2024undetectable}\nChrist, M., Gunn, S., and Zamir, O.\n\\newblock Undetectable watermarks for language models.\n\\newblock In \\emph{COLT}, 2024.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024model}\nDohmatob, E., Feng, Y., and Kou, J.\n\\newblock Model collapse demystified: The case of regression.\n\\newblock \\emph{arXiv preprint arXiv:2402.07712}, 2024.\n\n\\bibitem[Gehrmann et~al.(2019)]{gehrmann2019gltr}\nGehrmann, S., Strobelt, H., and Rush, A.~M.\n\\newblock {GLTR}: Statistical detection and visualization of generated text.\n\\newblock In \\emph{ACL Demo}, 2019.\n\n\\bibitem[Gerstgrasser et~al.(2024)]{gerstgrasser2024model}\nGerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., Sleight, H., Hughes, J., Korbak, T., Agrawal, R., et~al.\n\\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.\n\\newblock \\emph{arXiv preprint arXiv:2404.01413}, 2024.\n\n\\bibitem[Groeneveld et~al.(2024)]{groeneveld2024olmo}\nGroeneveld, D., Beltagy, I., Walsh, P., Bhagia, A., Kinney, R., Tafjord, O., et~al.\n\\newblock {OLMo}: Accelerating the science of language models.\n\\newblock In \\emph{ACL}, 2024.\n\n\\bibitem[Guo et~al.(2024)]{guo2024curious}\nGuo, Z., Schaeffer, R., Murrell, B., et~al.\n\\newblock Curious decline of linguistic diversity: A large-scale analysis of {LLM}-generated text.\n\\newblock \\emph{arXiv preprint arXiv:2311.09807}, 2024.\n\n\\bibitem[Hans et~al.(2024)]{hans2024binoculars}\nHans, A., Schwarzschild, A., Cheber, V., Alon, U., Hase, P., Goldstein, T.\n\\newblock Spotting {LLM}s with Binoculars: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Hendrycks \\& Gimpel(2017)]{hendrycks2017baseline}\nHendrycks, D. and Gimpel, K.\n\\newblock A baseline for detecting misclassified and out-of-distribution examples in neural networks.\n\\newblock In \\emph{ICLR}, 2017.\n\n\\bibitem[Holtzman et~al.(2020)]{holtzman2020curious}\nHoltzman, A., Buys, J., Du, L., Forbes, M., and Choi, Y.\n\\newblock The curious case of neural text degeneration.\n\\newblock In \\emph{ICLR}, 2020.\n\n\\bibitem[Kirchenbauer et~al.(2023)]{kirchenbauer2023watermark}\nKirchenbauer, J., Geiping, J., Wen, Y., Katz, J., Miers, I., and Goldstein, T.\n\\newblock A watermark for large language models.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Liang et~al.(2018)]{liang2018enhancing}\nLiang, S., Li, Y., and Srikant, R.\n\\newblock Enhancing the reliability of out-of-distribution image detection in neural networks.\n\\newblock In \\emph{ICLR}, 2018.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nMitchell, E., Lee, Y., Khazatsky, A., Manning, C.~D., and Finn, C.\n\\newblock {DetectGPT}: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Padmakumar \\& He(2024)]{padmakumar2024does}\nPadmakumar, V. and He, H.\n\\newblock Does writing with language models reduce content diversity?\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Radford et~al.(2019)]{radford2019language}\nRadford, A., Wu, J., Child, R., Luan, D., Amodei, D., and Sutskever, I.\n\\newblock Language models are unsupervised multitask learners.\n\\newblock \\emph{OpenAI Technical Report}, 2019.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024model}\nShumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., and Gal, Y.\n\\newblock {AI} models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 631:755--759, 2024.\n\n\\bibitem[Solaiman et~al.(2019)]{solaiman2019release}\nSolaiman, I., Brundage, M., Clark, J., Askell, A., Herbert-Voss, A., Wu, J., et~al.\n\\newblock Release strategies and the social impacts of language models.\n\\newblock \\emph{arXiv preprint arXiv:1908.09203}, 2019.\n\n\\bibitem[Su et~al.(2023)]{su2023detectllm}\nSu, J., Zhuo, T.~Y., Wang, D., and Nakov, P.\n\\newblock {DetectLLM}: Leveraging log rank information for zero-shot detection of machine-generated text.\n\\newblock In \\emph{EMNLP Findings}, 2023.\n\n\\bibitem[Tulchinskii et~al.(2024)]{tulchinskii2024ldscore}\nTulchinskii, E., Kuznetsov, K., Kushnareva, L., Chernodub, A., Barannikov, S., et~al.\n\\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Wenzek et~al.(2020)]{wenzek2020ccnet}\nWenzek, G., Lachaux, M.-A., Conneau, A., Chaudhary, V., Guzm{\\'a}n, F., Joulin, A., and Grave, E.\n\\newblock {CCNet}: Extracting high quality monolingual datasets from web crawl data.\n\\newblock In \\emph{LREC}, 2020.\n\n\\bibitem[Wettig et~al.(2024)]{wettig2024qurating}\nWettig, A., Gao, T., Zhong, Z., and Chen, D.\n\\newblock {QuRating}: Selecting high-quality data for training language models.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Xie et~al.(2023)]{xie2023dsir}\nXie, S.~M., Santurkar, S., Ma, T., and Liang, P.\n\\newblock Data selection for language models via importance resampling.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\bibitem[Yang et~al.(2024{\\natexlab{a}})]{yang2024dnagpt}\nYang, X., Cheng, W., Petzold, L., Wang, W.~Y., and Chen, H.\n\\newblock {DNA-GPT}: Divergent n-gram analysis for training-free detection of {GPT}-generated text.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Yang et~al.(2024{\\natexlab{b}})]{yang2024qwen2}\nYang, A., Yang, B., Hui, B., Zheng, B., Yu, B., Zhou, C., et~al.\n\\newblock Qwen2 technical report.\n\\newblock \\emph{arXiv preprint arXiv:2407.10671}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "08c474e6-fa81-496a-b7a4-7648ec3ca738",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "e32202c0-fd02-4c84-84aa-da834c2bc237",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream ID",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e"
}
```

---

### Tool call

_source line 22 · 2026-05-14T22:41:36.936Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JP3gdAxP7vbBt55FKVvhUx`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e32202c0-fd02-4c84-84aa-da834c2bc237",
  "isSidechain": false,
  "requestId": "req_011Cb3GTuhGB3N7rU9npcMJy",
  "type": "assistant",
  "uuid": "cb20060e-e51d-40f4-9a29-4b7bd3a5110a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNfPDv5grQXvCGzrp7B2vi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15147,
      "cache_read_input_tokens": 45081,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15147,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 45081,
          "cache_creation_input_tokens": 15147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15147
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

_source line 23 · 2026-05-14T22:41:37.844Z_

<details><summary>↩ Tool result · `toolu_01JP3gdAxP7vbBt55FKVvhUx`</summary>

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

Package natbib Warning: Citation `radford2019language' on page 1 undefined on i
nput line 47.


Package natbib Warning: Citation `brown2020language' on page 1 undefined on inp
ut line 47.


Package natbib Warning: Citation `shumailov2024model' on page 1 undefined on in
put line 49.


Package natbib Warning: Citation `alemohammad2024selfconsuming' on page 1 undef
ined on input line 49.


Package natbib Warning: Citation `dohmatob2024model' on page 1 undefined on inp
ut line 49.


Package natbib Warning: Citation `gerstgrasser2024model' on page 1 undefined on
 input line 49.


Package natbib Warning: Citation `guo2024curious' on page 1 undefined on input 
line 50.


Package natbib Warning: Citation `padmakumar2024does' on page 1 undefined on in
put line 50.


Package natbib Warning: Citation `holtzman2020curious' on page 1 undefined on i
nput line 50.


Package natbib Warning: Citation `mitchell2023detectgpt' on page 1 undefined on
 input line 53.


Package natbib Warning: Citation `bao2024fastdetectgpt' on page 1 undefined on 
input line 53.


Package natbib Warning: Citation `hans2024binoculars' on page 1 undefined on in
put line 53.


Package natbib Warning: Citation `kirchenbauer2023watermark' on page 1 undefine
d on input line 53.


Package natbib Warning: Citation `su2023detectllm' on page 1 undefined on input
 line 53.


Package natbib Warning: Citation `tulchinskii2024ldscore' on page 1 undefined o
n input line 53.


Package natbib Warning: Citation `bertrand2023stability' on page 1 undefined on
 input line 55.


Overfull \hbox (20.91232pt too wide) in paragraph at lines 53--56
[]\OT1/cmr/m/n/10 Existing de-tec-tion methods---perplexity-based ap-proaches (
\OT1/cmr/bx/n/10 ???\OT1/cmr/m/n/10 ), wa-ter-mark-ing (\OT1/cmr/bx/n/10 ?\OT1/
cmr/m/n/10 ), and sta-tis-ti-cal tests (\OT1/cmr/bx/n/10 ??\OT1/cmr/m/n/10 )---

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `solaiman2019release' on page 2 undefined on i
nput line 76.


Package natbib Warning: Citation `gehrmann2019gltr' on page 2 undefined on inpu
t line 76.


Package natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on
 input line 76.


Package natbib Warning: Citation `bao2024fastdetectgpt' on page 2 undefined on 
input line 76.


Package natbib Warning: Citation `hans2024binoculars' on page 2 undefined on in
put line 76.


Package natbib Warning: Citation `su2023detectllm' on page 2 undefined on input
 line 76.


Package natbib Warning: Citation `kirchenbauer2023watermark' on page 2 undefine
d on input line 77.


Package natbib Warning: Citation `christ2024undetectable' on page 2 undefined o
n input line 77.


Package natbib Warning: Citation `yang2024dnagpt' on page 2 undefined on input 
line 78.


Package natbib Warning: Citation `tulchinskii2024ldscore' on page 2 undefined o
n input line 78.


Package natbib Warning: Citation `shumailov2024model' on page 2 undefined on in
put line 82.


Package natbib Warning: Citation `alemohammad2024selfconsuming' on page 2 undef
ined on input line 83.


Package natbib Warning: Citation `dohmatob2024model' on page 2 undefined on inp
ut line 84.


Package natbib Warning: Citation `gerstgrasser2024model' on page 2 undefined on
 input line 84.


Package natbib Warning: Citation `guo2024curious' on page 2 undefined on input 
line 85.


Package natbib Warning: Citation `padmakumar2024does' on page 2 undefined on in
put line 85.


Package natbib Warning: Citation `bertrand2023stability' on page 2 undefined on
 input line 89.


Package natbib Warning: Citation `xie2023dsir' on page 2 undefined on input lin
e 93.


Package natbib Warning: Citation `wettig2024qurating' on page 2 undefined on in
put line 93.


Package natbib Warning: Citation `wenzek2020ccnet' on page 2 undefined on input
 line 93.


Package natbib Warning: Citation `hendrycks2017baseline' on page 2 undefined on
 input line 97.


Package natbib Warning: Citation `liang2018enhancing' on page 2 undefined on in
put line 97.

[2]
Overfull \hbox (6.1182pt too wide) in paragraph at lines 128--129
 []\OT1/cmr/bx/n/10 Surface fea-tures (2).[] \OT1/cmr/m/n/10 Type-token ra-tio 
\OT1/cmtt/m/n/10 ttr $\OT1/cmr/m/n/10 = \OMS/cmsy/m/n/10 j\OML/cmm/m/it/10 V\OT
1/cmr/m/n/10 (\OML/cmm/m/it/10 x\OT1/cmr/m/n/10 )\OMS/cmsy/m/n/10 j\OML/cmm/m/i
t/10 =n$ \OT1/cmr/m/n/10 where $\OML/cmm/m/it/10 V\OT1/cmr/m/n/10 (\OML/cmm/m/i
t/10 x\OT1/cmr/m/n/10 )$ is the vo-cab-u-lary of $\OML/cmm/m/it/10 x$\OT1/cmr/m
/n/10 , and \OT1/cmtt/m/n/10 hapax[]ratio

Package natbib Warning: Citation `chen2016xgboost' on page 3 undefined on input
 line 144.


Package natbib Warning: Citation `biderman2023pythia' on page 3 undefined on in
put line 154.


Package natbib Warning: Citation `groeneveld2024olmo' on page 3 undefined on in
put line 154.


Package natbib Warning: Citation `yang2024qwen2' on page 3 undefined on input l
ine 154.


Overfull \hbox (55.77377pt too wide) in paragraph at lines 159--162
\OT1/cmr/m/n/10 For each of 1,000 seed texts per do-main (Wikipedia, News/CNN-D
ailyMail, Sci-en-tific/S2ORC, Cre-ative/WritingPrompts),
[3]

LaTeX Warning: Reference `tab:ablation' on page 4 undefined on input line 177.


LaTeX Warning: Reference `tab:h1h2' on page 4 undefined on input line 196.


LaTeX Warning: Reference `tab:logo' on page 4 undefined on input line 223.


LaTeX Warning: Reference `tab:lofo' on page 4 undefined on input line 228.


LaTeX Warning: Reference `tab:crossref' on page 4 undefined on input line 269.

[4]

LaTeX Warning: Reference `tab:rho_ref' on page 5 undefined on input line 271.


LaTeX Warning: Reference `tab:depth_ppl' on page 5 undefined on input line 314.



LaTeX Warning: Reference `tab:filtering' on page 5 undefined on input line 334.



LaTeX Warning: Reference `tab:domain' on page 5 undefined on input line 375.


LaTeX Warning: Reference `tab:prompt' on page 5 undefined on input line 400.

[5]

LaTeX Warning: Reference `tab:para' on page 6 undefined on input line 424.


LaTeX Warning: Reference `tab:crossmodel' on page 6 undefined on input line 449
.


LaTeX Warning: Reference `tab:ordinal' on page 6 undefined on input line 469.


LaTeX Warning: Reference `tab:edits' on page 6 undefined on input line 495.

[6]

LaTeX Warning: Reference `tab:scale' on page 7 undefined on input line 521.


Package natbib Warning: Citation `tulchinskii2024ldscore' on page 7 undefined o
n input line 550.

[7]

Package natbib Warning: Citation `shumailov2024model' on page 8 undefined on in
put line 589.

[8] [9] [10]

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
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmti9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.
pfb>
Output written on paper.pdf (11 pages, 284247 bytes).
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
nts/map/pdftex/updmap/pdftex.map}] [2]
Overfull \hbox (6.1182pt too wide) in paragraph at lines 128--129
 []\OT1/cmr/bx/n/10 Surface fea-tures (2).[] \OT1/cmr/m/n/10 Type-token ra-tio 
\OT1/cmtt/m/n/10 ttr $\OT1/cmr/m/n/10 = \OMS/cmsy/m/n/10 j\OML/cmm/m/it/10 V\OT
1/cmr/m/n/10 (\OML/cmm/m/it/10 x\OT1/cmr/m/n/10 )\OMS/cmsy/m/n/10 j\OML/cmm/m/i
t/10 =n$ \OT1/cmr/m/n/10 where $\OML/cmm/m/it/10 V\OT1/cmr/m/n/10 (\OML/cmm/m/i
t/10 x\OT1/cmr/m/n/10 )$ is the vo-cab-u-lary of $\OML/cmm/m/it/10 x$\OT1/cmr/m
/n/10 , and \OT1/cmtt/m/n/10 hapax[]ratio
[3]
Overfull \hbox (55.77377pt too wide) in paragraph at lines 159--162
\OT1/cmr/m/n/10 For each of 1,000 seed texts per do-main (Wikipedia, News/CNN-D
ailyMail, Sci-en-tific/S2ORC, Cre-ative/WritingPrompts),

Overfull \hbox (0.83737pt too wide) in paragraph at lines 196--199
\OT1/cmr/m/n/10 lin-ear trends with depth ($\OML/cmm/m/it/10 R[] \OMS/cmsy/m/n/
10 ^^U \OT1/cmr/m/n/10 0\OML/cmm/m/it/10 :\OT1/cmr/m/n/10 85$), while H$[]$-sta
tionary fea-tures (\OT1/cmtt/m/n/10 entropy[]std\OT1/cmr/m/n/10 , \OT1/cmtt/m/n
/10 entropy[]max\OT1/cmr/m/n/10 , \OT1/cmtt/m/n/10 entropy[]min\OT1/cmr/m/n/10 
,
[4] [5] [6] [7] [8] [9] [10] [11] [12] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmti9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.
pfb>
Output written on paper.pdf (12 pages, 291507 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb20060e-e51d-40f4-9a29-4b7bd3a5110a",
  "isSidechain": false,
  "promptId": "bc056985-7a91-4a57-bb85-6aa97ba3b608",
  "type": "user",
  "uuid": "b6544928-3093-4a9a-821e-d29ec6774603",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `radford2019language' on page 1 undefined on i\nnput line 47.\n\n\nPackage natbib Warning: Citation `brown2020language' on page 1 undefined on inp\nut line 47.\n\n\nPackage natbib Warning: Citation `shumailov2024model' on page 1 undefined on in\nput line 49.\n\n\nPackage natbib Warning: Citation `alemohammad2024selfconsuming' on page 1 undef\nined on input line 49.\n\n\nPackage natbib Warning: Citation `dohmatob2024model' on page 1 undefined on inp\nut line 49.\n\n\nPackage natbib Warning: Citation `gerstgrasser2024model' on page 1 undefined on\n input line 49.\n\n\nPackage natbib Warning: Citation `guo2024curious' on page 1 undefined on input \nline 50.\n\n\nPackage natbib Warning: Citation `padmakumar2024does' on page 1 undefined on in\nput line 50.\n\n\nPackage natbib Warning: Citation `holtzman2020curious' on page 1 undefined on i\nnput line 50.\n\n\nPackage natbib Warning: Citation `mitchell2023detectgpt' on page 1 undefined on\n input line 53.\n\n\nPackage natbib Warning: Citation `bao2024fastdetectgpt' on page 1 undefined on \ninput line 53.\n\n\nPackage natbib Warning: Citation `hans2024binoculars' on page 1 undefined on in\nput line 53.\n\n\nPackage natbib Warning: Citation `kirchenbauer2023watermark' on page 1 undefine\nd on input line 53.\n\n\nPackage natbib Warning: Citation `su2023detectllm' on page 1 undefined on input\n line 53.\n\n\nPackage natbib Warning: Citation `tulchinskii2024ldscore' on page 1 undefined o\nn input line 53.\n\n\nPackage natbib Warning: Citation `bertrand2023stability' on page 1 undefined on\n input line 55.\n\n\nOverfull \\hbox (20.91232pt too wide) in paragraph at lines 53--56\n[]\\OT1/cmr/m/n/10 Existing de-tec-tion methods---perplexity-based ap-proaches (\n\\OT1/cmr/bx/n/10 ???\\OT1/cmr/m/n/10 ), wa-ter-mark-ing (\\OT1/cmr/bx/n/10 ?\\OT1/\ncmr/m/n/10 ), and sta-tis-ti-cal tests (\\OT1/cmr/bx/n/10 ??\\OT1/cmr/m/n/10 )---\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `solaiman2019release' on page 2 undefined on i\nnput line 76.\n\n\nPackage natbib Warning: Citation `gehrmann2019gltr' on page 2 undefined on inpu\nt line 76.\n\n\nPackage natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on\n input line 76.\n\n\nPackage natbib Warning: Citation `bao2024fastdetectgpt' on page 2 undefined on \ninput line 76.\n\n\nPackage natbib Warning: Citation `hans2024binoculars' on page 2 undefined on in\nput line 76.\n\n\nPackage natbib Warning: Citation `su2023detectllm' on page 2 undefined on input\n line 76.\n\n\nPackage natbib Warning: Citation `kirchenbauer2023watermark' on page 2 undefine\nd on input line 77.\n\n\nPackage natbib Warning: Citation `christ2024undetectable' on page 2 undefined o\nn input line 77.\n\n\nPackage natbib Warning: Citation `yang2024dnagpt' on page 2 undefined on input \nline 78.\n\n\nPackage natbib Warning: Citation `tulchinskii2024ldscore' on page 2 undefined o\nn input line 78.\n\n\nPackage natbib Warning: Citation `shumailov2024model' on page 2 undefined on in\nput line 82.\n\n\nPackage natbib Warning: Citation `alemohammad2024selfconsuming' on page 2 undef\nined on input line 83.\n\n\nPackage natbib Warning: Citation `dohmatob2024model' on page 2 undefined on inp\nut line 84.\n\n\nPackage natbib Warning: Citation `gerstgrasser2024model' on page 2 undefined on\n input line 84.\n\n\nPackage natbib Warning: Citation `guo2024curious' on page 2 undefined on input \nline 85.\n\n\nPackage natbib Warning: Citation `padmakumar2024does' on page 2 undefined on in\nput line 85.\n\n\nPackage natbib Warning: Citation `bertrand2023stability' on page 2 undefined on\n input line 89.\n\n\nPackage natbib Warning: Citation `xie2023dsir' on page 2 undefined on input lin\ne 93.\n\n\nPackage natbib Warning: Citation `wettig2024qurating' on page 2 undefined on in\nput line 93.\n\n\nPackage natbib Warning: Citation `wenzek2020ccnet' on page 2 undefined on input\n line 93.\n\n\nPackage natbib Warning: Citation `hendrycks2017baseline' on page 2 undefined on\n input line 97.\n\n\nPackage natbib Warning: Citation `liang2018enhancing' on page 2 undefined on in\nput line 97.\n\n[2]\nOverfull \\hbox (6.1182pt too wide) in paragraph at lines 128--129\n []\\OT1/cmr/bx/n/10 Surface fea-tures (2).[] \\OT1/cmr/m/n/10 Type-token ra-tio \n\\OT1/cmtt/m/n/10 ttr $\\OT1/cmr/m/n/10 = \\OMS/cmsy/m/n/10 j\\OML/cmm/m/it/10 V\\OT\n1/cmr/m/n/10 (\\OML/cmm/m/it/10 x\\OT1/cmr/m/n/10 )\\OMS/cmsy/m/n/10 j\\OML/cmm/m/i\nt/10 =n$ \\OT1/cmr/m/n/10 where $\\OML/cmm/m/it/10 V\\OT1/cmr/m/n/10 (\\OML/cmm/m/i\nt/10 x\\OT1/cmr/m/n/10 )$ is the vo-cab-u-lary of $\\OML/cmm/m/it/10 x$\\OT1/cmr/m\n/n/10 , and \\OT1/cmtt/m/n/10 hapax[]ratio\n\nPackage natbib Warning: Citation `chen2016xgboost' on page 3 undefined on input\n line 144.\n\n\nPackage natbib Warning: Citation `biderman2023pythia' on page 3 undefined on in\nput line 154.\n\n\nPackage natbib Warning: Citation `groeneveld2024olmo' on page 3 undefined on in\nput line 154.\n\n\nPackage natbib Warning: Citation `yang2024qwen2' on page 3 undefined on input l\nine 154.\n\n\nOverfull \\hbox (55.77377pt too wide) in paragraph at lines 159--162\n\\OT1/cmr/m/n/10 For each of 1,000 seed texts per do-main (Wikipedia, News/CNN-D\nailyMail, Sci-en-tific/S2ORC, Cre-ative/WritingPrompts),\n[3]\n\nLaTeX Warning: Reference `tab:ablation' on page 4 undefined on input line 177.\n\n\nLaTeX Warning: Reference `tab:h1h2' on page 4 undefined on input line 196.\n\n\nLaTeX Warning: Reference `tab:logo' on page 4 undefined on input line 223.\n\n\nLaTeX Warning: Reference `tab:lofo' on page 4 undefined on input line 228.\n\n\nLaTeX Warning: Reference `tab:crossref' on page 4 undefined on input line 269.\n\n[4]\n\nLaTeX Warning: Reference `tab:rho_ref' on page 5 undefined on input line 271.\n\n\nLaTeX Warning: Reference `tab:depth_ppl' on page 5 undefined on input line 314.\n\n\n\nLaTeX Warning: Reference `tab:filtering' on page 5 undefined on input line 334.\n\n\n\nLaTeX Warning: Reference `tab:domain' on page 5 undefined on input line 375.\n\n\nLaTeX Warning: Reference `tab:prompt' on page 5 undefined on input line 400.\n\n[5]\n\nLaTeX Warning: Reference `tab:para' on page 6 undefined on input line 424.\n\n\nLaTeX Warning: Reference `tab:crossmodel' on page 6 undefined on input line 449\n.\n\n\nLaTeX Warning: Reference `tab:ordinal' on page 6 undefined on input line 469.\n\n\nLaTeX Warning: Reference `tab:edits' on page 6 undefined on input line 495.\n\n[6]\n\nLaTeX Warning: Reference `tab:scale' on page 7 undefined on input line 521.\n\n\nPackage natbib Warning: Citation `tulchinskii2024ldscore' on page 7 undefined o\nn input line 550.\n\n[7]\n\nPackage natbib Warning: Citation `shumailov2024model' on page 8 undefined on in\nput line 589.\n\n[8] [9] [10]\n\nPackage natbib Warning: There were undefined citations.\n\n[11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmti9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.\npfb>\nOutput written on paper.pdf (11 pages, 284247 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\nOverfull \\hbox (6.1182pt too wide) in paragraph at lines 128--129\n []\\OT1/cmr/bx/n/10 Surface fea-tures (2).[] \\OT1/cmr/m/n/10 Type-token ra-tio \n\\OT1/cmtt/m/n/10 ttr $\\OT1/cmr/m/n/10 = \\OMS/cmsy/m/n/10 j\\OML/cmm/m/it/10 V\\OT\n1/cmr/m/n/10 (\\OML/cmm/m/it/10 x\\OT1/cmr/m/n/10 )\\OMS/cmsy/m/n/10 j\\OML/cmm/m/i\nt/10 =n$ \\OT1/cmr/m/n/10 where $\\OML/cmm/m/it/10 V\\OT1/cmr/m/n/10 (\\OML/cmm/m/i\nt/10 x\\OT1/cmr/m/n/10 )$ is the vo-cab-u-lary of $\\OML/cmm/m/it/10 x$\\OT1/cmr/m\n/n/10 , and \\OT1/cmtt/m/n/10 hapax[]ratio\n[3]\nOverfull \\hbox (55.77377pt too wide) in paragraph at lines 159--162\n\\OT1/cmr/m/n/10 For each of 1,000 seed texts per do-main (Wikipedia, News/CNN-D\nailyMail, Sci-en-tific/S2ORC, Cre-ative/WritingPrompts),\n\nOverfull \\hbox (0.83737pt too wide) in paragraph at lines 196--199\n\\OT1/cmr/m/n/10 lin-ear trends with depth ($\\OML/cmm/m/it/10 R[] \\OMS/cmsy/m/n/\n10 ^^U \\OT1/cmr/m/n/10 0\\OML/cmm/m/it/10 :\\OT1/cmr/m/n/10 85$), while H$[]$-sta\ntionary fea-tures (\\OT1/cmtt/m/n/10 entropy[]std\\OT1/cmr/m/n/10 , \\OT1/cmtt/m/n\n/10 entropy[]max\\OT1/cmr/m/n/10 , \\OT1/cmtt/m/n/10 entropy[]min\\OT1/cmr/m/n/10 \n,\n[4] [5] [6] [7] [8] [9] [10] [11] [12] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmti9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.\npfb>\nOutput written on paper.pdf (12 pages, 291507 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cb20060e-e51d-40f4-9a29-4b7bd3a5110a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "b6544928-3093-4a9a-821e-d29ec6774603",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream ID",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e"
}
```

---

### Assistant

_source line 26 · 2026-05-14T22:41:42.833Z_

<details><summary>Logged reasoning block</summary>

```text
The second pass still has a "Label(s) may have changed" warning, which means I need a third pass. Let me run it once more.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6544928-3093-4a9a-821e-d29ec6774603",
  "isSidechain": false,
  "requestId": "req_011Cb3GUKC8WTVxAcGRo2JAf",
  "type": "assistant",
  "uuid": "8ac2ca3b-8bf5-42ad-b3df-82e118f1bd01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMTx257gQS8v5FXc6VVjP2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8748,
      "cache_read_input_tokens": 60228,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 60228,
          "cache_creation_input_tokens": 8748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8748
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

_source line 27 · 2026-05-14T22:41:43.459Z_

Need a third pass to resolve cross-references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ac2ca3b-8bf5-42ad-b3df-82e118f1bd01",
  "isSidechain": false,
  "requestId": "req_011Cb3GUKC8WTVxAcGRo2JAf",
  "type": "assistant",
  "uuid": "febf3d42-697b-416e-bb5a-7f442895eae2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMTx257gQS8v5FXc6VVjP2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8748,
      "cache_read_input_tokens": 60228,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 60228,
          "cache_creation_input_tokens": 8748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8748
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

_source line 28 · 2026-05-14T22:41:45.919Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BHhi1GCpBKPaZ5Pt2PcDBU`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Third LaTeX pass to finalize cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "febf3d42-697b-416e-bb5a-7f442895eae2",
  "isSidechain": false,
  "requestId": "req_011Cb3GUKC8WTVxAcGRo2JAf",
  "type": "assistant",
  "uuid": "0f2d5105-9bc4-4903-bf46-1ffaf7df9450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMTx257gQS8v5FXc6VVjP2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8748,
      "cache_read_input_tokens": 60228,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 60228,
          "cache_creation_input_tokens": 8748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8748
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

_source line 29 · 2026-05-14T22:41:46.380Z_

<details><summary>↩ Tool result · `toolu_01BHhi1GCpBKPaZ5Pt2PcDBU`</summary>

```text
ts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmti9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.
pfb>
Output written on paper.pdf (12 pages, 291507 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f2d5105-9bc4-4903-bf46-1ffaf7df9450",
  "isSidechain": false,
  "promptId": "bc056985-7a91-4a57-bb85-6aa97ba3b608",
  "type": "user",
  "uuid": "ed8e070e-7029-4736-bea8-2605abdb68c8",
  "toolUseResult": {
    "stdout": "ts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmti9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.\npfb>\nOutput written on paper.pdf (12 pages, 291507 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0f2d5105-9bc4-4903-bf46-1ffaf7df9450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T22:41:51.529Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0127AEZnrWk3BMbVeLExbuKr`</summary>

```json
{
  "command": "grep -c \"Warning.*undefined\" paper.log",
  "description": "Check for remaining undefined references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed8e070e-7029-4736-bea8-2605abdb68c8",
  "isSidechain": false,
  "requestId": "req_011Cb3GUsKuvXCuuHBReJrJR",
  "type": "assistant",
  "uuid": "6fa10702-0e9c-4473-841c-9865300db0fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPWVCBsCyjt9Ef3JmYY6Fx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 68976,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 279,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 68976,
          "cache_creation_input_tokens": 279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 279
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

_source line 31 · 2026-05-14T22:41:51.575Z_

<details><summary>↩ Tool result · `toolu_0127AEZnrWk3BMbVeLExbuKr`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fa10702-0e9c-4473-841c-9865300db0fb",
  "isSidechain": false,
  "promptId": "bc056985-7a91-4a57-bb85-6aa97ba3b608",
  "type": "user",
  "uuid": "ae2b041d-c190-4228-bc0c-1b3021be8602",
  "toolUseResult": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6fa10702-0e9c-4473-841c-9865300db0fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-14T22:41:51.658Z_

```json
{
  "parentUuid": "ae2b041d-c190-4228-bc0c-1b3021be8602",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "716a4bc1-b148-46bd-bd14-9b17602f4f47",
  "timestamp": "2026-05-14T22:41:51.658Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-14T22:41:59.689Z_

PDF compiled cleanly — 12 pages, 0 undefined references. Output at `artifacts/dream_reports/dream_20260514T221538/best/paper.pdf`.

Coverage: all 12 experiments from `experiment_data.json` are represented — feature ablation/H1-H2 (Tables 1-2), cross-generator LOGO (Tables 3-4), cross-family reference model (Tables 5-6), downstream utility (Tables 7-8), prompt type comparison (Table 9), paraphrastic vs continuation (Table 10), cross-model chains (Table 11), multi-domain (Table 12), 5-class ordinal (Table 13), robustness to edits (Table 14), 7B+ scale (Table S5), LD-Score and end-to-end classifier and length control (supplementary paragraphs). All numbers are sourced directly from the JSON.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "716a4bc1-b148-46bd-bd14-9b17602f4f47",
  "isSidechain": false,
  "requestId": "req_011Cb3GVFsEJrmpjDDGwokdS",
  "type": "assistant",
  "uuid": "78ddcd9f-c6af-48d6-8213-301bd083d40a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xr2E4NMqqnyUDMEMavp7XL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 199,
      "cache_read_input_tokens": 69255,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 199,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 69255,
          "cache_creation_input_tokens": 199,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 199
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

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "78ddcd9f-c6af-48d6-8213-301bd083d40a",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream ID",
  "sessionId": "6f50109c-746c-4b8f-986a-349fb461f53e"
}
```

---
