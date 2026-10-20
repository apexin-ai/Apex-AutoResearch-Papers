# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/867c85bd-e7b8-4218-bf1a-0cd3207410c6.jsonl`
- **Structured JSON:** [`cbf055701ab868488af1.json`](../../sessions/cb/cbf055701ab868488af1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T22:45:52.168Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T22:45:52.168Z",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Abandon dual dynamics as headline contribution. Reframe paper around two angles that survive: (1) Task formulation paper — 'Generation Depth Estimation: A Missing Layer in Synthetic Text Analysis.' The task itself (ordinal depth, not binary) is novel regardless of feature performance. Formalize the task, provide baselines, release benchmark dataset, discuss what makes it hard. (2) Negative/analytical result on depth signal scaling — depth signal is strong for small generators but degrades with scale, revealing that distributional drift from recursive generation is partially masked by model fluency. Connects to model collapse literature. Perplexity-by-depth monotonic decrease (13.5→1.7) remains robust as reference-model phenomenon — reposition around 'reference-model perplexity as depth proxy' rather than the full dual dynamics story. Paper becomes: new task + benchmark + scaling analysis + practical baseline.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T22:45:52.171Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T22:45:52.171Z",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-14T22:45:52.187Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Abandon dual dynamics as headline contribution. Reframe paper around two angles that survive: (1) Task formulation paper — 'Generation Depth Estimation: A Missing Layer in Synthetic Text Analysis.' The task itself (ordinal depth, not binary) is novel regardless of feature performance. Formalize the task, provide baselines, release benchmark dataset, discuss what makes it hard. (2) Negative/analytical result on depth signal scaling — depth signal is strong for small generators but degrades with scale, revealing that distributional drift from recursive generation is partially masked by model fluency. Connects to model collapse literature. Perplexity-by-depth monotonic decrease (13.5→1.7) remains robust as reference-model phenomenon — reposition around 'reference-model perplexity as depth proxy' rather than the full dual dynamics story. Paper becomes: new task + benchmark + scaling analysis + practical baseline.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "64b0831c-d266-495e-8b02-943588d3f051",
  "type": "user",
  "uuid": "095105d8-7205-4c10-85e3-d84796796a0d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T22:45:52.186Z_

```json
{
  "parentUuid": "095105d8-7205-4c10-85e3-d84796796a0d",
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
  "uuid": "e95d23d1-2e23-4d0f-a594-d545a8c38dce",
  "timestamp": "2026-05-14T22:45:52.186Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T22:45:52.186Z_

```json
{
  "parentUuid": "e95d23d1-2e23-4d0f-a594-d545a8c38dce",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "59e679e1-4264-4c4a-925b-f21f16185238",
  "timestamp": "2026-05-14T22:45:52.186Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
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
  "aiTitle": "Generate depth estimation in synthetic text analysis",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6"
}
```

---

### Assistant

_source line 7 · 2026-05-14T22:45:54.819Z_

I'll start by reading the input files to understand the experimental data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59e679e1-4264-4c4a-925b-f21f16185238",
  "isSidechain": false,
  "requestId": "req_011Cb3GnzH7hp5uKoJPjPgb4",
  "type": "assistant",
  "uuid": "53842824-0f5a-45aa-ae0c-2cead028b820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MghH6GSnWdepFTSv1dnJHW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11236,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11236
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

_source line 8 · 2026-05-14T22:45:56.144Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X8BdCErs2LKd4pHsNG4VQm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53842824-0f5a-45aa-ae0c-2cead028b820",
  "isSidechain": false,
  "requestId": "req_011Cb3GnzH7hp5uKoJPjPgb4",
  "type": "assistant",
  "uuid": "242f46b6-685a-46cd-82ca-fa781b5f0e7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MghH6GSnWdepFTSv1dnJHW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11236,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11236
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

_source line 9 · 2026-05-14T22:45:56.216Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NaEp1WmJ8PkKDZT9zeEbtk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "242f46b6-685a-46cd-82ca-fa781b5f0e7f",
  "isSidechain": false,
  "requestId": "req_011Cb3GnzH7hp5uKoJPjPgb4",
  "type": "assistant",
  "uuid": "af332d69-b4c8-4d08-b489-1478ea02aa94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MghH6GSnWdepFTSv1dnJHW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11236,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11236
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

_source line 10 · 2026-05-14T22:45:56.221Z_

<details><summary>↩ Tool result · `toolu_01NaEp1WmJ8PkKDZT9zeEbtk`</summary>

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
  "parentUuid": "af332d69-b4c8-4d08-b489-1478ea02aa94",
  "isSidechain": false,
  "promptId": "64b0831c-d266-495e-8b02-943588d3f051",
  "type": "user",
  "uuid": "e5c28986-0b72-455e-b7cf-e757a40f25c5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/paper_framing.md",
      "content": "# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- Primary: AAAI 2027 (deadline: August 2, 2026)\n- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **dual depth dynamics** that cross-cuts the surface/reference distinction: **level/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth (H₂), while **distributional shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁). Notably, entropy_mean is a reference-model feature that drifts (ρ=-0.68), showing the H₁/H₂ split is about what the feature measures (central tendency vs shape), not where it comes from (surface vs reference). This dual pattern creates a complementary feature space: drifting features provide ordinal depth signal, while stable shape features provide noise-robust class boundaries. The combination significantly outperforms either alone (macro-F1 0.82 vs 0.76/0.72).\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).\n\n**Claim 2 — Dual Dynamics (Level vs Shape)**: Depth-dependent features split into two families by **what they measure**, not by their source (surface vs reference): (a) **level/diversity features** (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (H₂ — vocabulary impoverishment + entropy compression); (b) **shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁ — distributional shape is robust to recursive generation). This split cross-cuts the surface/reference boundary (entropy_mean is reference-derived but drifts). Full feature set (0.82) significantly outperforms surface-only (0.76) and reference-only (0.72) — the two dynamics are complementary for classification.\n\n**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.\n\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **dual dynamics**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth (H₂), while distributional shape features (entropy variance, tail decay) remain near-stationary (H₁). This split is about **what the feature measures** (central tendency vs shape), not where it comes from — overturning the naive expectation that \"reference-model features = robust, surface features = fragile.\" The dual pattern has practical value: drifting features provide ordinal depth signal, stable shape features provide noise-robust decision boundaries, and their combination yields the best depth estimation for risk-stratified data curation.\n\n**Headline result template**: \"On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.76 macro-F1, but full features achieve 0.82 (p<0.001). We don't claim reference features are \"better\" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). The dual dynamics finding is itself a scientific contribution. Note: \"fingerprint\" in the paper refers to the full feature vector's combination, not just reference-model features.\n\n**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\n\n**RC3 — \"Is 3-class sufficient? Why not finer-grained?\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\n\n**RC4 — \"How realistic are single-model chains?\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\n\n**RC5 — \"What about human editing / post-processing?\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\n\n**RC6 — \"Ecological validity — continuation vs real web content\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.\n\n**RC9 — \"Only ≤2.8B generators — does this transfer to frontier scale?\"**: All 5 current generators ≤2.8B. Frontier models (7B+) produce more fluent text that may compress depth signal. → Add at least one 7B+ generator (plan_014). If depth signal significantly weaker at scale → honest limitation with analysis of why; if comparable → strong generalization evidence.\n\n**RC10 — \"Text length confound\"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.\n\n**RC11 — \"Downstream utility — single run, no CIs\"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).\n\n## Contribution Positioning (Dream D006 insight)\nThe contribution is **primarily empirical and conceptual**, not methodological. The features (NLL summary statistics) and classifier (XGBoost) are standard — the novelty lies in:\n1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection\n2. **Empirical discovery**: Dual dynamics (level/diversity drift vs shape stationarity) cross-cutting surface/reference boundary\n3. **Practical application**: Risk-stratified data curation outperforming binary filtering\n\nDo NOT overclaim \"distributional fingerprinting\" as a new method. Position the paper as empirical science with a novel task formulation and a surprising empirical finding. The H1/H2 framework is an empirical validation extending attractor cycle theory to non-paraphrastic chains, not a major theoretical contribution.\n\nRelated work must expand to 30+ references covering: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory (Alemohammad et al., Dohmatob et al., Gerstgrasser et al., Guo et al.), OOD detection (Hendrycks & Gimpel), data quality scoring (DSIR, QuRating, CCNet), watermarking (Kirchenbauer et al.), vocabulary diversity (Guo et al. 2024, Padmakumar & He 2024, Holtzman et al. 2020).\n\n## Venue Fit\n- AAAI 2027: Fit as empirical + conceptual contribution — novel task formulation (depth estimation) + surprising empirical finding (dual dynamics) + practical application (data curation). Must position as empirical science, not methodology paper.\n- EMNLP 2026: Excellent fit — directly addresses special theme \"New Missions for NLP Research\" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work. Empirical/conceptual contributions better received here than AAAI.\n",
      "numLines": 66,
      "startLine": 1,
      "totalLines": 66
    }
  },
  "sourceToolAssistantUUID": "af332d69-b4c8-4d08-b489-1478ea02aa94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerp…",
  "leafUuid": "e5c28986-0b72-455e-b7cf-e757a40f25c5",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth estimation in synthetic text analysis",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6"
}
```

---

### Tool result

_source line 13 · 2026-05-14T22:45:56.419Z_

<details><summary>↩ Tool result · `toolu_01X8BdCErs2LKd4pHsNG4VQm`</summary>

```text
1	[
2	  {
3	    "name": "feature_ablation_and_trend",
4	    "description": "Feature ablation (surface-only vs reference-only vs full) and H1/H2 trend analysis on MVP data. Already executed; registry results from plan-001-fix are taken as given. In worst tier, these in-distribution results are not wrong but are misleadingly optimistic — the 0.06 full-vs-surface gap and the clean H1/H2 split both depend on same-family (Pythia) reference and single-generator setting.\n",
5	    "results": {
6	      "full_macro_f1": 0.8204,
7	      "surface_only_f1": 0.7628,
8	      "reference_only_f1": 0.7187,
9	      "full_vs_surface_gap": 0.058,
10	      "full_vs_reference_gap": 0.102,
11	      "h2_features_count": 3,
12	      "h1_features_count": 4,
13	      "entropy_mean_depth_rho": -0.68,
14	      "median_ppl_by_depth": "13.50, 4.96, 3.00, 2.07, 1.72"
15	    },
16	    "tables": [
17	      {
18	        "name": "Table 1: Feature Ablation (MVP In-Distribution)",
19	        "columns": [
20	          "feature_set",
21	          "macro_f1",
22	          "95_ci",
23	          "gen0_f1",
24	          "gen1_f1",
25	          "gen2plus_f1"
26	        ],
27	        "rows": [
28	          [
29	            "full",
30	            0.8204,
31	            "[0.807, 0.834]",
32	            0.952,
33	            0.776,
34	            0.795
35	          ],
36	          [
37	            "surface_only",
38	            0.7628,
39	            "[0.747, 0.774]",
40	            0.92,
41	            0.71,
42	            0.658
43	          ],
44	          [
45	            "reference_only",
46	            0.7187,
47	            "[0.706, 0.733]",
48	            0.895,
49	            0.64,
50	            0.621
51	          ]
52	        ]
53	      },
54	      {
55	        "name": "Table 2: H1/H2 Feature Classification",
56	        "columns": [
57	          "feature",
58	          "source",
59	          "depth_slope",
60	          "R2",
61	          "classification"
62	        ],
63	        "rows": [
64	          [
65	            "entropy_mean",
66	            "reference",
67	            -0.042,
68	            0.91,
69	            "H2_drift"
70	          ],
71	          [
72	            "ttr",
73	            "surface",
74	            -0.031,
75	            0.87,
76	            "H2_drift"
77	          ],
78	          [
79	            "hapax_ratio",
80	            "surface",
81	            -0.028,
82	            0.83,
83	            "H2_drift"
84	          ],
85	          [
86	            "entropy_std",
87	            "reference",
88	            0.003,
89	            0.04,
90	            "H1_stationary"
91	          ],
92	          [
93	            "entropy_max",
94	            "reference",
95	            -0.005,
96	            0.07,
97	            "H1_stationary"
98	          ],
99	          [
100	            "entropy_min",
101	            "reference",
102	            0.002,
103	            0.02,
104	            "H1_stationary"
105	          ],
106	          [
107	            "tail_decay",
108	            "reference",
109	            0.004,
110	            0.05,
111	            "H1_stationary"
112	          ]
113	        ]
114	      }
115	    ],
116	    "figures": [],
117	    "analysis": "In-distribution results are solid. The dual dynamics split appears clean: 3 H2 features drift, 4 H1 features are stationary. Perplexity signal is very strong. However, the worst-tier interpretation is that this clean separation is partly an artifact of the Pythia-Pythia configuration. Subsequent experiments (plan_003, plan_013) will show the H2 drift is partially confounded by length artifacts and reference-model specificity.\n\n\nThese results are from actual execution and look encouraging. But they are entirely in-distribution: single generator (Pythia-2.8B), same-family reference (Pythia-410M), no length control. The 0.82 full F1 benefits from generator-specific artifacts that the reference model can detect precisely because it shares the Pythia architecture. The H2 entropy_mean drift (ρ=-0.68) is strong here because Pythia-410M and Pythia-2.8B share tokenizer and distributional priors — the reference model's perplexity is calibrated to the generator's output distribution. The perplexity monotonic decrease (13.5→1.7) is real but partially reflects the reference model's familiarity with same-family outputs. In worst tier, subsequent experiments reveal these as inflated baselines.\n"
118	  },
119	  {
120	    "name": "cross_generator_evaluation",
121	    "description": "Leave-one-generator-out evaluation across 5 generators. Tests cross-generator generalization. In worst tier, LOGO F1 is poor, especially when holding out non-Pythia generators.\n",
122	    "results": {
123	      "overall_logo_macro_f1": 0.52,
124	      "logo_holdout_pythia28b": 0.61,
125	      "logo_holdout_pythia1b": 0.64,
126	      "logo_holdout_olmo2": 0.48,
127	      "logo_holdout_qwen17b": 0.44,
128	      "logo_holdout_qwen06b": 0.43,
129	      "within_family_avg_f1": 0.625,
130	      "cross_family_avg_f1": 0.45,
131	      "leave_one_family_out_pythia_held_in": 0.58,
132	      "leave_one_family_out_pythia_held_out": 0.41
133	    },
134	    "tables": [
135	      {
136	        "name": "Table 3: Leave-One-Generator-Out Macro-F1",
137	        "columns": [
138	          "held_out_generator",
139	          "family",
140	          "macro_f1",
141	          "gen0_f1",
142	          "gen1_f1",
143	          "gen2plus_f1"
144	        ],
145	        "rows": [
146	          [
147	            "pythia-2.8b",
148	            "pythia",
149	            0.61,
150	            0.82,
151	            0.51,
152	            0.5
153	          ],
154	          [
155	            "pythia-1b",
156	            "pythia",
157	            0.64,
158	            0.85,
159	            0.54,
160	            0.53
161	          ],
162	          [
163	            "olmo-2-1b",
164	            "olmo",
165	            0.48,
166	            0.72,
167	            0.38,
168	            0.34
169	          ],
170	          [
171	            "qwen3-1.7b",
172	            "qwen",
173	            0.44,
174	            0.68,
175	            0.35,
176	            0.29
177	          ],
178	          [
179	            "qwen3-0.6b",
180	            "qwen",
181	            0.43,
182	            0.67,
183	            0.33,
184	            0.29
185	          ],
186	          [
187	            "mean (all)",
188	            "-",
189	            0.52,
190	            0.75,
191	            0.42,
192	            0.39
193	          ]
194	        ]
195	      },
196	      {
197	        "name": "Table 4: Leave-One-Family-Out",
198	        "columns": [
199	          "held_out_family",
200	          "train_generators",
201	          "macro_f1"
202	        ],
203	        "rows": [
204	          [
205	            "pythia",
206	            "olmo+qwen",
207	            0.41
208	          ],
209	          [
210	            "olmo",
211	            "pythia+qwen",
212	            0.54
213	          ],
214	          [
215	            "qwen",
216	            "pythia+olmo",
217	            0.56
218	          ]
219	        ]
220	      }
221	    ],
222	    "figures": [],
223	    "analysis": "Cross-generator generalization fails the 0.58 threshold. The within-family vs cross-family gap (0.625 vs 0.45) reveals the classifier relies on generator-specific artifacts. Gen-0 detection remains passable (~0.75 average) because human-written text is universally distinct, but gen-1 vs gen-2+ discrimination (the core depth signal) collapses cross-family. This undermines Claim 1's generalization requirement. In the reframed paper, this becomes evidence for: \"depth estimation requires generator-aware features or larger, more diverse training sets — the task is harder than binary detection because depth artifacts are generator-specific.\"\n\n\nThe classifier overfits to generator-specific artifacts rather than learning universal depth signatures. Within the Pythia family, generalization is passable (0.61–0.64) because Pythia-2.8B and Pythia-1B share tokenizer, training data (The Pile), and architectural patterns — the Pythia-410M reference model's NLL features are structurally similar for both. But cross-family holdouts (OLMo, Qwen) drop sharply to 0.43–0.48 because: (a) different tokenizers mean surface features (TTR, hapax) have different baseline distributions, (b) the Pythia-410M reference model assigns systematically different perplexity distributions to non-Pythia outputs, creating a domain shift in entropy features, (c) each generator family has its own repetition/diversity profile at each depth, so depth-correlated patterns learned from one family don't transfer. The leave-one-family-out result (0.41 when Pythia held out) confirms the classifier critically depends on Pythia-specific patterns. Overall LOGO F1 of 0.52 is below the 0.58 threshold, killing the cross-generator generalization claim.\n"
224	  },
225	  {
226	    "name": "cross_family_reference_model",
227	    "description": "Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B) for feature extraction. Critical falsification test for the dual dynamics framework.\n",
228	    "results": {
229	      "olmo_ref_entropy_mean_rho": -0.22,
230	      "qwen_ref_entropy_mean_rho": -0.15,
231	      "pythia_ref_entropy_mean_rho": -0.68,
232	      "olmo_ref_full_f1": 0.63,
233	      "qwen_ref_full_f1": 0.58,
234	      "pythia_ref_full_f1": 0.82,
235	      "olmo_ref_h2_features_count": 1,
236	      "qwen_ref_h2_features_count": 1,
237	      "cross_family_ref_entropy_mean_rho_avg": -0.185,
238	      "shape_features_h1_stable_across_refs": true,
239	      "ttr_rho_across_refs": -0.3,
240	      "hapax_rho_across_refs": -0.27
241	    },
242	    "tables": [
243	      {
244	        "name": "Table 5: Entropy_mean Depth Correlation by Reference Model",
245	        "columns": [
246	          "reference_model",
247	          "family",
248	          "entropy_mean_rho",
249	          "p_value",
250	          "h2_classification"
251	        ],
252	        "rows": [
253	          [
254	            "pythia-410m",
255	            "pythia",
256	            -0.68,
257	            "<0.001",
258	            "H2_confirmed"
259	          ],
260	          [
261	            "olmo-2-1b",
262	            "olmo",
263	            -0.22,
264	            0.031,
265	            "H2_weak (|ρ|<0.3)"
266	          ],
267	          [
268	            "qwen3-0.6b",
269	            "qwen",
270	            -0.15,
271	            0.118,
272	            "H2_not_confirmed"
273	          ]
274	        ]
275	      },
276	      {
277	        "name": "Table 6: Full Feature Set Classification by Reference Model",
278	        "columns": [
279	          "reference_model",
280	          "macro_f1",
281	          "surface_only_f1",
282	          "ref_only_f1",
283	          "full_vs_surface_gap"
284	        ],
285	        "rows": [
286	          [
287	            "pythia-410m",
288	            0.82,
289	            0.76,
290	            0.72,
291	            0.06
292	          ],
293	          [
294	            "olmo-2-1b",
295	            0.63,
296	            0.61,
297	            0.48,
298	            0.02
299	          ],
300	          [
301	            "qwen3-0.6b",
302	            0.58,
303	            0.57,
304	            0.41,
305	            0.01
306	          ]
307	        ]
308	      },
309	      {
310	        "name": "Table 7: H1/H2 Stability Across Reference Models",
311	        "columns": [
312	          "feature",
313	          "pythia_class",
314	          "olmo_class",
315	          "qwen_class",
316	          "stable_across_refs"
317	        ],
318	        "rows": [
319	          [
320	            "entropy_mean",
321	            "H2",
322	            "weak/NS",
323	            "NS",
324	            "NO"
325	          ],
326	          [
327	            "entropy_std",
328	            "H1",
329	            "H1",
330	            "H1",
331	            "YES"
332	          ],
333	          [
334	            "entropy_max",
335	            "H1",
336	            "H1",
337	            "H1",
338	            "YES"
339	          ],
340	          [
341	            "tail_decay",
342	            "H1",
343	            "H1",
344	            "H1",
345	            "YES"
346	          ],
347	          [
348	            "ttr",
349	            "H2",
350	            "H2",
351	            "H2",
352	            "YES"
353	          ],
354	          [
355	            "hapax_ratio",
356	            "H2",
357	            "H2",
358	            "weak H2",
359	            "YES (marginal)"
360	          ]
361	        ]
362	      }
363	    ],
364	    "figures": [],
365	    "analysis": "The key falsification test triggers: entropy_mean's H2 drift was substantially a Pythia-specific artifact. The dual dynamics narrative (\"level features drift, shape features don't, and this cross-cuts surface/reference\") collapses because the cross-cutting evidence depended on entropy_mean being a reference feature that drifts. Without it, H2 features are just surface features (TTR, hapax), and H1 features are just reference features — exactly the naive expectation the paper claimed to overturn. The shape feature H1 stability is real but less interesting: it says \"distributional shape under any reference model is stable across depth,\" which is a weaker claim. In the reframed paper, this becomes: \"reference-model perplexity as depth proxy is reference-model-dependent — a same-family reference provides much stronger signal, pointing toward an alignment-based explanation of depth discriminability.\"\n\n\nEntropy_mean drift (ρ=-0.68 with Pythia reference) largely disappears with non-Pythia references (ρ≈-0.22 OLMo, ρ≈-0.15 Qwen). This happens because entropy_mean is driven by how well the reference model predicts the generated text — when the reference model shares architecture and training data with the generator (Pythia-Pythia), it has calibrated predictions that systematically shift with depth. A cross-family reference model assigns noisier, less calibrated perplexities, washing out the drift signal. The |ρ|<0.3 threshold is breached for both non-Pythia references. Shape features (entropy_std, entropy_max, tail_decay) remain H1-stationary across all references — this is genuinely robust because distributional shape is less sensitive to absolute calibration. But the H2 side of the \"dual dynamics\" now has only surface features (TTR, hapax_ratio) showing reliable drift (ρ≈-0.28 to -0.30), and these are precisely the features confounded by text length (plan_013). The \"dual dynamics cross-cuts surface/reference boundary\" claim collapses: the cross-cutting was an artifact of Pythia-Pythia alignment. Classification F1 with non-Pythia reference drops to 0.58–0.63 because the strongest H2 reference feature is now noise.\n"
366	  },
367	  {
368	    "name": "downstream_utility",
369	    "description": "Fine-tune OLMo-1B on depth-stratified data. Compare depth-aware filtering vs binary baselines with 3+ seeds and bootstrap CIs. In worst tier, the advantage is not statistically significant.\n",
370	    "results": {
371	      "depth_quality_spearman": 0.28,
372	      "depth_quality_spearman_ci": "[0.11, 0.45]",
373	      "depth_filtering_ppl_improvement_pct": 1.8,
374	      "depth_filtering_ppl_improvement_ci": "[-0.5, 4.1]",
375	      "binary_filtering_ppl_improvement_pct": 1.2,
376	      "binary_filtering_ppl_improvement_ci": "[-1.1, 3.5]",
377	      "depth_vs_binary_p_value": 0.31,
378	      "sample_matched_depth_ppl": 14.2,
379	      "sample_matched_binary_ppl": 14.5,
380	      "sample_matched_p_value": 0.42,
381	      "seed_variance_cv": 0.08,
382	      "n_seeds": 5
383	    },
384	    "tables": [
385	      {
386	        "name": "Table 8: Downstream Fine-Tuning Results (OLMo-1B, 5 seeds)",
387	        "columns": [
388	          "filtering_strategy",
389	          "mean_ppl",
390	          "std_ppl",
391	          "95_ci",
392	          "improvement_vs_unfiltered_pct"
393	        ],
394	        "rows": [
395	          [
396	            "unfiltered",
397	            14.8,
398	            0.42,
399	            "[14.2, 15.4]",
400	            "-"
401	          ],
402	          [
403	            "binary_fastdetectgpt",
404	            14.5,
405	            0.51,
406	            "[13.8, 15.2]",
407	            "1.2 [-1.1, 3.5]"
408	          ],
409	          [
410	            "binary_ldscore",
411	            14.6,
412	            0.48,
413	            "[14.0, 15.2]",
414	            "0.9 [-1.4, 3.2]"
415	          ],
416	          [
417	            "depth_aware_keep_gen01",
418	            14.2,
419	            0.39,
420	            "[13.7, 14.7]",
421	            "1.8 [-0.5, 4.1]"
422	          ],
423	          [
424	            "depth_aware_sample_matched",
425	            14.2,
426	            0.44,
427	            "[13.6, 14.8]",
428	            "1.5 [-0.8, 3.8]"
429	          ]
430	        ]
431	      },
432	      {
433	        "name": "Table 9: Depth-Quality Correlation",
434	        "columns": [
435	          "metric",
436	          "value",
437	          "95_ci"
438	        ],
439	        "rows": [
440	          [
441	            "spearman_rho",
442	            0.28,
443	            "[0.11, 0.45]"
444	          ],
445	          [
446	            "ppl_gen0_mean",
447	            12.1,
448	            "[11.8, 12.4]"
449	          ],
450	          [
451	            "ppl_gen1_mean",
452	            13.4,
453	            "[12.9, 13.9]"
454	          ],
455	          [
456	            "ppl_gen2_mean",
457	            14.1,
458	            "[13.5, 14.7]"
459	          ],
460	          [
461	            "ppl_gen3_mean",
462	            14.5,
463	            "[13.8, 15.2]"
464	          ],
465	          [
466	            "ppl_gen4_mean",
467	            14.9,
468	            "[14.1, 15.7]"
469	          ]
470	        ]
471	      }
472	    ],
473	    "figures": [],
474	    "analysis": "Downstream utility claim fails significance after proper experimental controls. The improvement exists directionally (1.8% vs 1.2%) but CIs overlap. This was the most anticipated outcome from dream reviews: single-run results are fragile. In reframed paper, report honestly as \"directional evidence for depth-quality correlation, insufficient for statistical significance at this sample size\" and pivot to the correlation itself (ρ=0.28) as motivation for future work. The perplexity-by-depth monotonic relationship (Table 9) is real and publishable as a descriptive finding — it just doesn't translate into significant downstream filtering advantage.\n\n\nWith proper experimental controls (multiple seeds, CIs, sample-count matching, non-Pythia model), the downstream advantage of depth-aware filtering shrinks to statistical insignificance. Several factors contribute: (1) OLMo-1B is more robust to training data contamination than Pythia-410M (the original MVP model), reducing the overall signal magnitude; (2) with 5 seeds, the variance across runs is substantial (CV≈0.08), swamping the small depth-vs-binary difference; (3) the sample-count-matched comparison shows the original advantage was partly a data size confound — depth-aware filtering keeps more data (it retains gen-1) than binary filtering (which discards all synthetic), so the improvement was partially from having more training data, not from depth stratification per se; (4) bootstrap CIs for the depth-vs-binary comparison overlap substantially (p=0.31), failing significance. The Spearman ρ=0.28 between predicted depth and quality degradation is real but weak, falling in the [0.15, 0.4] worst-tier range. In isolation, this correlation is interesting but not actionable. Claim 3 (downstream utility) cannot be supported as \"significantly outperforms binary baselines.\"\n"
475	  },
476	  {
477	    "name": "prompt_type_comparison",
478	    "description": "Compare continuation vs elaboration vs inspired_rewriting chains. In worst tier, depth signal varies dramatically by prompt type, undermining generalizability.\n",
479	    "results": {
480	      "continuation_macro_f1": 0.78,
481	      "elaboration_macro_f1": 0.55,
482	      "inspired_rewriting_macro_f1": 0.47,
483	      "continuation_entropy_mean_rho": -0.65,
484	      "elaboration_entropy_mean_rho": -0.38,
485	      "rewriting_entropy_mean_rho": -0.18,
486	      "cross_prompt_train_test_f1": 0.42
487	    },
488	    "tables": [
489	      {
490	        "name": "Table 10: Depth Classification by Prompt Type",
491	        "columns": [
492	          "prompt_type",
493	          "macro_f1",
494	          "entropy_mean_rho",
495	          "ttr_rho",
496	          "gen1_vs_gen2plus_f1"
497	        ],
498	        "rows": [
499	          [
500	            "continuation",
501	            0.78,
502	            -0.65,
503	            -0.29,
504	            0.71
505	          ],
506	          [
507	            "elaboration",
508	            0.55,
509	            -0.38,
510	            -0.16,
511	            0.44
512	          ],
513	          [
514	            "inspired_rewriting",
515	            0.47,
516	            -0.18,
517	            -0.08,
518	            0.36
519	          ]
520	        ]
521	      },
522	      {
523	        "name": "Table 11: Cross-Prompt Transfer",
524	        "columns": [
525	          "train_prompt",
526	          "test_prompt",
527	          "macro_f1"
528	        ],
529	        "rows": [
530	          [
531	            "continuation",
532	            "elaboration",
533	            0.46
534	          ],
535	          [
536	            "continuation",
537	            "rewriting",
538	            0.39
539	          ],
540	          [
541	            "elaboration",
542	            "continuation",
543	            0.51
544	          ],
545	          [
546	            "elaboration",
547	            "rewriting",
548	            0.42
549	          ],
550	          [
551	            "rewriting",
552	            "continuation",
553	            0.44
554	          ],
555	          [
556	            "rewriting",
557	            "elaboration",
558	            0.4
559	          ]
560	        ]
561	      }
562	    ],
563	    "figures": [],
564	    "analysis": "Prompt type is a major moderator of depth signal, challenging ecological validity. In the reframed paper, this becomes a positive finding for the task formulation angle: \"Generation depth estimation difficulty depends critically on the semantic coupling between generation steps. Continuation chains (high coupling) preserve depth signal; rewriting chains (low coupling) do not. This connects to attractor cycle theory — semantic-preserving chains converge, while semantically divergent chains don't accumulate distributional drift.\"\n\n\nDepth signal is strongly prompt-type dependent. Continuation chains preserve the strongest signal (F1=0.78) because each generation builds directly on the previous output, creating cumulative distributional drift. Elaboration chains weaken the signal (F1=0.55) because the model is asked to expand on a topic rather than continue text — this introduces more creative variation that partially resets the distributional state at each depth. Inspired rewriting shows near-chance depth discrimination (F1=0.47) because the semantic departure from the source is maximal — each depth step is essentially an independent generation conditioned on a theme, not a recursive chain. The entropy_mean drift follows the same pattern (ρ: -0.65/-0.38/-0.18). When training on one prompt type and testing on another, F1 drops to 0.42, showing the features are prompt-type-specific. This means the \"depth signal\" is partly a \"continuation-chain-specific\" artifact — real web contamination involves diverse generation patterns, not just continuation.\n"
565	  },
566	  {
567	    "name": "paraphrastic_comparison",
568	    "description": "Compare paraphrasing vs continuation chains. In worst tier, paraphrasing chains converge quickly (as attractor theory predicts), but continuation chains also show limited depth discrimination beyond gen-2.\n",
569	    "results": {
570	      "paraphrastic_3class_f1": 0.52,
571	      "nonparaphrastic_3class_f1": 0.78,
572	      "paraphrastic_entropy_mean_plateau_depth": 2,
573	      "nonparaphrastic_saturation_depth": 3,
574	      "paraphrastic_gen2_vs_gen3_f1": 0.34,
575	      "nonparaphrastic_gen2_vs_gen3_f1": 0.41
576	    },
577	    "tables": [
578	      {
579	        "name": "Table 12: Paraphrastic vs Non-Paraphrastic Depth Discrimination",
580	        "columns": [
581	          "chain_type",
582	          "3class_f1",
583	          "gen0_f1",
584	          "gen1_f1",
585	          "gen2plus_f1",
586	          "entropy_mean_rho"
587	        ],
588	        "rows": [
589	          [
590	            "paraphrastic",
591	            0.52,
592	            0.78,
593	            0.45,
594	            0.33,
595	            -0.31
596	          ],
597	          [
598	            "continuation",
599	            0.78,
600	            0.93,
601	            0.72,
602	            0.69,
603	            -0.65
604	          ]
605	        ]
606	      }
607	    ],
608	    "figures": [],
609	    "analysis": "Confirms attractor theory prediction for paraphrastic chains. Continuation chains have more signal but also saturate. In reframed paper: \"Our empirical results are consistent with attractor convergence — extending the theory to non-paraphrastic chains shows the convergence is slower but still present, bounding practical depth estimation to ~3 useful classes.\"\n\n\nParaphrasing chains converge by depth 2 as attractor theory predicts — gen-2, gen-3, gen-4 are nearly indistinguishable (F1=0.34 for gen-2 vs gen-3). Continuation chains preserve more signal but also saturate by depth 3 — the distributional drift accumulates but with diminishing marginal signal at each step. The worst-tier interpretation: even non-paraphrastic chains have bounded depth discriminability, just with a slightly higher ceiling than paraphrastic ones. The difference (0.78 vs 0.52) confirms continuation chains are better for depth estimation but doesn't rescue the broader generalizability problem — the signal is still chain-type-specific and bounded.\n"
610	  },
611	  {
612	    "name": "cross_model_chains",
613	    "description": "Cross-model chains (different generator per depth step). In worst tier, cross-model chains destroy depth signal because generator identity dominates depth identity.\n",
614	    "results": {
615	      "cross_model_macro_f1": 0.39,
616	      "single_model_macro_f1": 0.78,
617	      "cross_model_gen0_f1": 0.65,
618	      "cross_model_gen1_f1": 0.28,
619	      "cross_model_gen2plus_f1": 0.24,
620	      "cross_vs_single_delta": -0.39
621	    },
622	    "tables": [
623	      {
624	        "name": "Table 13: Single-Model vs Cross-Model Chains",
625	        "columns": [
626	          "chain_type",
627	          "macro_f1",
628	          "gen0_f1",
629	          "gen1_f1",
630	          "gen2plus_f1"
631	        ],
632	        "rows": [
633	          [
634	            "single_model",
635	            0.78,
636	            0.93,
637	            0.72,
638	            0.69
639	          ],
640	          [
641	            "cross_model_random",
642	            0.39,
643	            0.65,
644	            0.28,
645	            0.24
646	          ],
647	          [
648	            "cross_model_increasing_size",
649	            0.41,
650	            0.66,
651	            0.3,
652	            0.27
653	          ],
654	          [
655	            "cross_model_decreasing_size",
656	            0.38,
657	            0.63,
658	            0.27,
659	            0.24
660	          ]
661	        ]
662	      }
663	    ],
664	    "figures": [],
665	    "analysis": "Cross-model chains destroy depth signal — generator identity is a much stronger signal than depth in the feature space. This is the ecological validity nail: real web contamination involves diverse generators. In reframed paper, this honestly motivates future work on generator-invariant depth features and positions the current features as a baseline that works in controlled (single-generator) settings but not in the wild.\n\n\nCross-model chains are dramatically harder (F1=0.39, essentially near chance for gen-1 and gen-2+). The reason is fundamental: when generator identity changes at each depth step, the distributional features capture generator identity more than depth. A gen-1 text from Qwen looks more different from gen-1 text from Pythia than gen-1 looks from gen-2 within the same generator. The features (NLL statistics under a fixed reference model) are sensitive to the generator's output distribution, creating a confound where generator variation swamps depth variation. Gen-0 remains detectable (F1=0.65) because human-written text is still distinct from any machine-generated text, but ordinal depth discrimination collapses. This is perhaps the strongest negative result: in the realistic scenario of diverse web generators, depth estimation with these features is not viable.\n"
666	  },
667	  {
668	    "name": "multi_domain_seeds",
669	    "description": "Expand to 4 domains. In worst tier, significant domain variance with some domains showing near-chance performance.\n",
670	    "results": {
671	      "wikipedia_macro_f1": 0.72,
672	      "news_macro_f1": 0.68,
673	      "scientific_macro_f1": 0.55,
674	      "creative_macro_f1": 0.48,
675	      "overall_macro_f1": 0.61,
676	      "cross_domain_train_test_f1": 0.49,
677	      "domain_f1_std": 0.11
678	    },
679	    "tables": [
680	      {
681	        "name": "Table 14: Depth Classification by Domain",
682	        "columns": [
683	          "domain",
684	          "n_seeds",
685	          "macro_f1",
686	          "gen0_f1",
687	          "gen1_f1",
688	          "gen2plus_f1"
689	        ],
690	        "rows": [
691	          [
692	            "wikipedia",
693	            500,
694	            0.72,
695	            0.89,
696	            0.63,
697	            0.64
698	          ],
699	          [
700	            "news",
701	            500,
702	            0.68,
703	            0.86,
704	            0.59,
705	            0.59
706	          ],
707	          [
708	            "scientific",
709	            500,
710	            0.55,
711	            0.78,
712	            0.44,
713	            0.43
714	          ],
715	          [
716	            "creative",
717	            500,
718	            0.48,
719	            0.71,
720	            0.37,
721	            0.36
722	          ],
723	          [
724	            "all_pooled",
725	            2000,
726	            0.61,
727	            0.81,
728	            0.51,
729	            0.51
730	          ]
731	        ]
732	      }
733	    ],
734	    "figures": [],
735	    "analysis": "Domain is a significant moderator. Factual domains have more signal; creative domains have less. In reframed paper: \"Depth estimation difficulty depends on the entropy of the source domain — low-entropy domains (wiki, news) produce more predictable generations with clearer depth drift; high-entropy domains (creative) mask depth signal with natural variation.\"\n\n\nDomain variance is substantial. Wikipedia and news seeds (factual, structured prose) show passable performance because LLMs generate predictable continuations with consistent distributional drift. Scientific abstracts show weaker signal because the specialized vocabulary and formulaic structure reduce the distinguishability of human vs machine text at each depth. Creative writing shows near-chance performance because it has the highest natural language variance — the within-class variation in features (e.g., TTR, hapax_ratio) for creative text at any depth is large enough to swamp the between-class (depth) variation. Cross-domain transfer is poor (0.49) because the feature baselines differ across domains. This adds another moderator (domain + prompt type + generator family) that limits the generalizability of depth estimation.\n"
736	  },
737	  {
738	    "name": "finer_grained_ordinal",
739	    "description": "5-class ordinal classification (gen-0 through gen-4). In worst tier, performance is near chance for finer classes.\n",
740	    "results": {
741	      "five_class_macro_f1": 0.28,
742	      "three_class_macro_f1": 0.78,
743	      "gen0_f1": 0.85,
744	      "gen1_f1": 0.42,
745	      "gen2_f1": 0.18,
746	      "gen3_f1": 0.12,
747	      "gen4_f1": 0.11,
748	      "ordinal_mae": 1.4,
749	      "adjacent_confusion_pct": 0.72
750	    },
751	    "tables": [
752	      {
753	        "name": "Table 15: Five-Class Ordinal Classification",
754	        "columns": [
755	          "class",
756	          "precision",
757	          "recall",
758	          "f1",
759	          "n_samples"
760	        ],
761	        "rows": [
762	          [
763	            "gen-0",
764	            0.88,
765	            0.82,
766	            0.85,
767	            995
768	          ],
769	          [
770	            "gen-1",
771	            0.39,
772	            0.45,
773	            0.42,
774	            993
775	          ],
776	          [
777	            "gen-2",
778	            0.16,
779	            0.2,
780	            0.18,
781	            912
782	          ],
783	          [
784	            "gen-3",
785	            0.11,
786	            0.13,
787	            0.12,
788	            856
789	          ],
790	          [
791	            "gen-4",
792	            0.1,
793	            0.12,
794	            0.11,
795	            816
796	          ]
797	        ]
798	      }
799	    ],
800	    "figures": [],
801	    "analysis": "Five-class is essentially unsolvable with current features. Confirms the 3-class ceiling. In reframed paper, this is a benchmark result: \"We establish that 3-class depth estimation (gen-0/gen-1/gen-2+) is the practical ceiling for distributional features, consistent with attractor convergence theory extended to non-paraphrastic generation.\"\n\n\nFive-class F1 of 0.28 is barely above chance (0.20 for 5 classes). Gen-0 remains detectable (F1=0.85) and gen-1 is marginally separable (F1=0.42), but gen-2/3/4 collapse into an indistinguishable cluster (F1: 0.18/0.12/0.11). This is because distributional drift between adjacent deep generations is minimal — the marginal change from gen-2→gen-3 in any feature is smaller than the within-class variance. The ordinal MAE of 1.4 means predictions are off by ~1.4 depth levels on average. 72% of misclassifications are between adjacent classes, suggesting some ordinal structure remains but is too weak for practical 5-class discrimination. This validates the attractor convergence prediction: beyond ~3 classes, depth signal is negligible even for non-paraphrastic chains.\n"
802	  },
803	  {
804	    "name": "human_edit_robustness",
805	    "description": "Robustness to simulated human edits. In worst tier, even mild edits substantially degrade performance.\n",
806	    "results": {
807	      "baseline_f1": 0.78,
808	      "random_replace_5pct_f1": 0.68,
809	      "random_replace_10pct_f1": 0.58,
810	      "random_replace_20pct_f1": 0.44,
811	      "llm_light_edit_f1": 0.53,
812	      "f1_drop_at_5pct": -0.1
813	    },
814	    "tables": [
815	      {
816	        "name": "Table 16: Robustness to Human Edits",
817	        "columns": [
818	          "edit_type",
819	          "edit_rate",
820	          "macro_f1",
821	          "delta_f1"
822	        ],
823	        "rows": [
824	          [
825	            "none",
826	            "0%",
827	            0.78,
828	            "-"
829	          ],
830	          [
831	            "random_replace",
832	            "5%",
833	            0.68,
834	            -0.1
835	          ],
836	          [
837	            "random_replace",
838	            "10%",
839	            0.58,
840	            -0.2
841	          ],
842	          [
843	            "random_replace",
844	            "20%",
845	            0.44,
846	            -0.34
847	          ],
848	          [
849	            "llm_light_edit",
850	            "~8%",
851	            0.53,
852	            -0.25
853	          ]
854	        ]
855	      }
856	    ],
857	    "figures": [],
858	    "analysis": "Depth features are fragile to post-generation modification. In reframed paper: \"Depth estimation is most applicable to unedited generation chains (e.g., automated content farms) and degrades rapidly with human post-processing. This constrains the practical applicability to detection of fully automated pipelines.\"\n\n\nEven 5% random word replacement drops F1 by 0.10, and LLM-simulated light editing drops F1 by 0.25. The features are brittle to post-generation modification because both surface features (TTR, hapax) and reference features (entropy statistics) are sensitive to token-level changes. A few word substitutions can significantly alter hapax ratio, TTR, and the reference model's NLL distribution. LLM-simulated editing is worse than random replacement because it systematically \"cleans up\" the distributional artifacts that depth estimation relies on — an LLM editing gen-3 text makes it look more like gen-1 by smoothing out the accumulated drift. This is a fundamental limitation: any real-world post-processing pipeline (human editing, automated cleanup, grammar correction) will degrade depth signal.\n"
859	  },
860	  {
861	    "name": "ld_score_feature",
862	    "description": "Add LD-Score as feature. In worst tier, LD-Score shows inconsistent behavior — neither clearly H2 nor clearly adding value.\n",
863	    "results": {
864	      "ldscore_depth_rho": -0.25,
865	      "ldscore_added_f1_delta": 0.005,
866	      "ldscore_h2_classification": "weak/ambiguous",
867	      "with_ldscore_f1": 0.785,
868	      "without_ldscore_f1": 0.78
869	    },
870	    "tables": [
871	      {
872	        "name": "Table 17: LD-Score as Depth Feature",
873	        "columns": [
874	          "metric",
875	          "value"
876	        ],
877	        "rows": [
878	          [
879	            "ldscore_depth_rho",
880	            -0.25
881	          ],
882	          [
883	            "ldscore_slope_R2",
884	            0.12
885	          ],
886	          [
887	            "feature_set_without_ldscore_f1",
888	            0.78
889	          ],
890	          [
891	            "feature_set_with_ldscore_f1",
892	            0.785
893	          ],
894	          [
895	            "ldscore_feature_importance_rank",
896	            "7/8"
897	          ]
898	        ]
899	      }
900	    ],
901	    "figures": [],
902	    "analysis": "LD-Score pre-registered prediction is weakly supported but insufficient to validate the level/shape framework given that the framework is independently undermined by plan_003. In reframed paper: \"LD-Score shows weak depth sensitivity, consistent with character-level features capturing some vocabulary drift, but insufficient to serve as independent validation of the dual dynamics hypothesis.\"\n\n\nLD-Score shows weak depth correlation (ρ=-0.25), not clearly meeting H2 criteria (slope significant but R²<0.15). Character-level distribution is a noisy proxy for depth — it captures some vocabulary shift but is contaminated by topic and style variation. Adding LD-Score to the feature set provides negligible improvement (+0.005 F1), well within noise. The pre-registered prediction that LD-Score would be a \"level feature\" exhibiting H2 drift is partially supported (negative ρ) but weak. In worst tier, this fails to provide out-of-sample validation for the level/shape framework because the framework itself is collapsing (plan_003 shows H2 is reference-model-dependent).\n"
903	  },
904	  {
905	    "name": "end_to_end_classifier",
906	    "description": "QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification. In worst tier, end-to-end slightly outperforms handcrafted features, undermining the feature analysis.\n",
907	    "results": {
908	      "e2e_macro_f1": 0.83,
909	      "handcrafted_macro_f1": 0.78,
910	      "e2e_cross_generator_f1": 0.55,
911	      "e2e_vs_handcrafted_delta": 0.05,
912	      "e2e_gen1_vs_gen2plus_f1": 0.76
913	    },
914	    "tables": [
915	      {
916	        "name": "Table 18: End-to-End vs Handcrafted Features",
917	        "columns": [
918	          "method",
919	          "in_dist_f1",
920	          "cross_gen_logo_f1",
921	          "training_cost_gpu_h"
922	        ],
923	        "rows": [
924	          [
925	            "handcrafted_xgboost",
926	            0.78,
927	            0.52,
928	            0.1
929	          ],
930	          [
931	            "qwen_qolra_e2e",
932	            0.83,
933	            0.55,
934	            15
935	          ],
936	          [
937	            "qwen_qolra_frozen",
938	            0.8,
939	            0.53,
940	            8
941	          ]
942	        ]
943	      }
944	    ],
945	    "figures": [],
946	    "analysis": "End-to-end slightly beats handcrafted but shares the generalization failure. In reframed paper: \"Both handcrafted and learned features achieve similar in-distribution performance and similar cross-generator degradation, suggesting the depth estimation difficulty is fundamental to the feature space, not a limitation of our specific feature engineering.\"\n\n\nEnd-to-end classification achieves F1=0.83, slightly above the handcrafted 0.78, suggesting that learned representations capture additional signal beyond the 7 distributional features. However, the improvement is modest and the end-to-end model also fails to generalize cross-generator (F1=0.55), indicating the additional signal is also generator-specific. This undercuts the feature analysis contribution: if a fine-tuned LM can slightly beat the handcrafted features, the dual dynamics decomposition is more of an interpretability lens than a competitive method. In worst tier, this result slightly undermines the feature-level analysis without providing a clearly superior alternative — neither approach generalizes.\n"
947	  },
948	  {
949	    "name": "text_length_control",
950	    "description": "Text length confound analysis. In worst tier, length-controlled F1 drops >0.08, revealing that surface features substantially tracked length.\n",
951	    "results": {
952	      "length_depth_correlation": 0.42,
953	      "original_full_f1": 0.78,
954	      "length_controlled_full_f1": 0.68,
955	      "length_controlled_f1_delta": -0.1,
956	      "length_controlled_surface_f1": 0.63,
957	      "length_controlled_reference_f1": 0.66,
958	      "length_normalized_ttr_rho": -0.12,
959	      "length_normalized_hapax_rho": -0.09,
960	      "original_ttr_rho": -0.31,
961	      "original_hapax_rho": -0.28,
962	      "length_matched_f1": 0.7
963	    },
964	    "tables": [
965	      {
966	        "name": "Table 19: Length Confound Analysis",
967	        "columns": [
968	          "condition",
969	          "full_f1",
970	          "surface_f1",
971	          "reference_f1",
972	          "full_vs_surface_gap"
973	        ],
974	        "rows": [
975	          [
976	            "original",
977	            0.78,
978	            0.76,
979	            0.72,
980	            0.02
981	          ],
982	          [
983	            "length_normalized_features",
984	            0.68,
985	            0.63,
986	            0.66,
987	            0.02
988	          ],
989	          [
990	            "length_matched_subsampling",
991	            0.7,
992	            0.65,
993	            0.67,
994	            0.03
995	          ]
996	        ]
997	      },
998	      {
999	        "name": "Table 20: Feature Depth Correlation Before/After Length Control",
1000	        "columns": [
1001	          "feature",
1002	          "original_rho",
1003	          "length_normalized_rho",
1004	          "pct_explained_by_length"
1005	        ],
1006	        "rows": [
1007	          [
1008	            "ttr",
1009	            -0.31,
1010	            -0.12,
1011	            "61%"
1012	          ],
1013	          [
1014	            "hapax_ratio",
1015	            -0.28,
1016	            -0.09,
1017	            "68%"
1018	          ],
1019	          [
1020	            "entropy_mean",
1021	            -0.68,
1022	            -0.55,
1023	            "19%"
1024	          ],
1025	          [
1026	            "entropy_std",
1027	            0.03,
1028	            0.02,
1029	            "33%"
1030	          ],
1031	          [
1032	            "tail_decay",
1033	            0.04,
1034	            0.03,
1035	            "25%"
1036	          ]
1037	        ]
1038	      }
1039	    ],
1040	    "figures": [],
1041	    "analysis": "Length confound is substantial. ~60-68% of surface feature depth correlation was length artifact. Reference features are less affected (19% for entropy_mean) but still impacted. After controlling for length, the full-vs-surface gap nearly vanishes (0.02), meaning reference features' advantage was partially from being less length-confounded, not from capturing genuinely different depth signal. In reframed paper: \"We identify text length as a major confound in depth estimation: standard surface diversity metrics (TTR, hapax ratio) primarily track length variation rather than genuine distributional drift. Length-controlled analysis reveals a weaker but real residual depth signal, predominantly carried by reference-model perplexity statistics.\"\n\n\nText length correlates with depth (r=0.42) — deeper generations tend to be shorter as models produce more repetitive/compressed outputs. This correlation confounds both surface features and indirectly reference features. TTR and hapax_ratio are mechanically length-dependent (shorter texts have higher TTR, lower hapax ratio), so their depth correlation (ρ≈-0.3) was partially a length proxy. After length normalization (fixed-window computation), TTR depth correlation drops from -0.31 to -0.12 and hapax from -0.28 to -0.09 — most of the \"H2 drift\" in surface features was length artifact. Length-controlled full F1 drops by 0.10 (from 0.78 to 0.68), breaching the >0.08 threshold. Notably, reference features also drop (from 0.72 to 0.66) because entropy statistics are affected by text length through the number of tokens evaluated. After length matching (subsampling to equalize length distributions), F1 is 0.70 — real depth signal exists but is substantially weaker than originally measured. The full-vs-surface gap shrinks (0.68 vs 0.63 = 0.05 gap → 0.02 gap after removing length confound from surface features).\n"
1042	  },
1043	  {
1044	    "name": "large_scale_generator",
1045	    "description": "Add 7B+ generator (Qwen3-8B-Base). In worst tier, depth signal is minimal at this scale — larger models produce more fluent text that masks distributional drift.\n",
1046	    "results": {
1047	      "generator_7bplus_macro_f1": 0.43,
1048	      "generator_7bplus_gen0_f1": 0.62,
1049	      "generator_7bplus_gen1_f1": 0.35,
1050	      "generator_7bplus_gen2plus_f1": 0.32,
1051	      "generator_7bplus_entropy_mean_rho": -0.19,
1052	      "small_generator_avg_f1": 0.72,
1053	      "f1_vs_generator_size_correlation": -0.85,
1054	      "generator_7bplus_ppl_depth0": 8.2,
1055	      "generator_7bplus_ppl_depth4": 4.1,
1056	      "ppl_dynamic_range_7bplus": 4.1,
1057	      "ppl_dynamic_range_2_8b": 11.8
1058	    },
1059	    "tables": [
1060	      {
1061	        "name": "Table 21: Depth Classification by Generator Scale",
1062	        "columns": [
1063	          "generator",
1064	          "params",
1065	          "macro_f1",
1066	          "gen0_f1",
1067	          "gen1_f1",
1068	          "gen2plus_f1",
1069	          "entropy_mean_rho"
1070	        ],
1071	        "rows": [
1072	          [
1073	            "qwen3-0.6b",
1074	            "0.6B",
1075	            0.74,
1076	            0.91,
1077	            0.66,
1078	            0.65,
1079	            -0.58
1080	          ],
1081	          [
1082	            "pythia-1b",
1083	            "1B",
1084	            0.71,
1085	            0.89,
1086	            0.62,
1087	            0.62,
1088	            -0.55
1089	          ],
1090	          [
1091	            "olmo-2-1b",
1092	            "1.5B",
1093	            0.69,
1094	            0.87,
1095	            0.6,
1096	            0.6,
1097	            -0.51
1098	          ],
1099	          [
1100	            "qwen3-1.7b",
1101	            "1.7B",
1102	            0.68,
1103	            0.86,
1104	            0.58,
1105	            0.6,
1106	            -0.48
1107	          ],
1108	          [
1109	            "pythia-2.8b",
1110	            "2.8B",
1111	            0.78,
1112	            0.93,
1113	            0.72,
1114	            0.69,
1115	            -0.68
1116	          ],
1117	          [
1118	            "qwen3-8b",
1119	            "8B",
1120	            0.43,
1121	            0.62,
1122	            0.35,
1123	            0.32,
1124	            -0.19
1125	          ]
1126	        ]
1127	      },
1128	      {
1129	        "name": "Table 22: Perplexity Dynamic Range by Generator Scale",
1130	        "columns": [
1131	          "generator",
1132	          "ppl_depth0",
1133	          "ppl_depth4",
1134	          "dynamic_range",
1135	          "ppl_ratio"
1136	        ],
1137	        "rows": [
1138	          [
1139	            "pythia-2.8b",
1140	            13.5,
1141	            1.7,
1142	            11.8,
1143	            7.9
1144	          ],
1145	          [
1146	            "pythia-1b",
1147	            12.8,
1148	            2.1,
1149	            10.7,
1150	            6.1
1151	          ],
1152	          [
1153	            "olmo-2-1b",
1154	            11.4,
1155	            2.5,
1156	            8.9,
1157	            4.6
1158	          ],
1159	          [
1160	            "qwen3-1.7b",
1161	            10.8,
1162	            2.8,
1163	            8.0,
1164	            3.9
1165	          ],
1166	          [
1167	            "qwen3-8b",
1168	            8.2,
1169	            4.1,
1170	            4.1,
1171	            2.0
1172	          ]
1173	        ]
1174	      }
1175	    ],
1176	    "figures": [],
1177	    "analysis": "Scale-dependent depth signal degradation is the strongest negative finding and the most publishable result in the worst tier. The log-linear F1-vs-scale relationship is novel empirical evidence connecting depth estimation to model collapse theory: \"larger models collapse slower (Gerstgrasser et al.), and correspondingly, depth signal degrades with scale.\" Note Pythia-2.8B is anomalously high due to same-family reference advantage — once corrected (using cross-family reference, plan_003), it would likely fall closer to the trend line. The perplexity dynamic range analysis (Table 22) provides a mechanistic explanation: reference-model perplexity has less room to drift when the generator is already fluent. In reframed paper, this becomes the central analytical contribution: \"Generation depth estimation exhibits a scale-dependent regime: distributional features that reliably detect depth for ≤3B generators fail at 7B+ scale, providing empirical evidence for scale-dependent convergence rates in recursive generation.\"\n\nThe 7B+ generator produces text that is much harder to depth-classify (F1=0.43, near chance for gen-1 and gen-2+). Several mechanisms explain this: (1) larger models have lower perplexity under any reference model, so the absolute perplexity at gen-0 is already closer to machine-generated (8.2 vs 13.5 for human text under Pythia-2.8B reference), reducing the dynamic range for drift detection (4.1 vs 11.8 points of perplexity range across depths); (2) larger models maintain more vocabulary diversity across recursive generations — TTR and hapax ratio drift less because the model's larger capacity preserves lexical variety; (3) the distributional shape of 7B+ outputs is more \"human-like\" at every depth, compressing the feature space. The F1-vs-generator-size correlation of -0.85 shows a clear scaling law: depth discriminability degrades roughly log-linearly with generator parameters. This connects directly to model collapse literature — larger models collapse slower, producing less distributional drift per recursive step. Gen-0 detection (human vs 7B-generated) is also harder (F1=0.62 vs ~0.90 for smaller generators) because 7B outputs are more human-like on all features.\n"
1178	  }
1179	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "242f46b6-685a-46cd-82ca-fa781b5f0e7f",
  "isSidechain": false,
  "promptId": "64b0831c-d266-495e-8b02-943588d3f051",
  "type": "user",
  "uuid": "0433f60a-742a-4959-834a-e6d6b3e13526",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"feature_ablation_and_trend\",\n    \"description\": \"Feature ablation (surface-only vs reference-only vs full) and H1/H2 trend analysis on MVP data. Already executed; registry results from plan-001-fix are taken as given. In worst tier, these in-distribution results are not wrong but are misleadingly optimistic — the 0.06 full-vs-surface gap and the clean H1/H2 split both depend on same-family (Pythia) reference and single-generator setting.\\n\",\n    \"results\": {\n      \"full_macro_f1\": 0.8204,\n      \"surface_only_f1\": 0.7628,\n      \"reference_only_f1\": 0.7187,\n      \"full_vs_surface_gap\": 0.058,\n      \"full_vs_reference_gap\": 0.102,\n      \"h2_features_count\": 3,\n      \"h1_features_count\": 4,\n      \"entropy_mean_depth_rho\": -0.68,\n      \"median_ppl_by_depth\": \"13.50, 4.96, 3.00, 2.07, 1.72\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Feature Ablation (MVP In-Distribution)\",\n        \"columns\": [\n          \"feature_set\",\n          \"macro_f1\",\n          \"95_ci\",\n          \"gen0_f1\",\n          \"gen1_f1\",\n          \"gen2plus_f1\"\n        ],\n        \"rows\": [\n          [\n            \"full\",\n            0.8204,\n            \"[0.807, 0.834]\",\n            0.952,\n            0.776,\n            0.795\n          ],\n          [\n            \"surface_only\",\n            0.7628,\n            \"[0.747, 0.774]\",\n            0.92,\n            0.71,\n            0.658\n          ],\n          [\n            \"reference_only\",\n            0.7187,\n            \"[0.706, 0.733]\",\n            0.895,\n            0.64,\n            0.621\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: H1/H2 Feature Classification\",\n        \"columns\": [\n          \"feature\",\n          \"source\",\n          \"depth_slope\",\n          \"R2\",\n          \"classification\"\n        ],\n        \"rows\": [\n          [\n            \"entropy_mean\",\n            \"reference\",\n            -0.042,\n            0.91,\n            \"H2_drift\"\n          ],\n          [\n            \"ttr\",\n            \"surface\",\n            -0.031,\n            0.87,\n            \"H2_drift\"\n          ],\n          [\n            \"hapax_ratio\",\n            \"surface\",\n            -0.028,\n            0.83,\n            \"H2_drift\"\n          ],\n          [\n            \"entropy_std\",\n            \"reference\",\n            0.003,\n            0.04,\n            \"H1_stationary\"\n          ],\n          [\n            \"entropy_max\",\n            \"reference\",\n            -0.005,\n            0.07,\n            \"H1_stationary\"\n          ],\n          [\n            \"entropy_min\",\n            \"reference\",\n            0.002,\n            0.02,\n            \"H1_stationary\"\n          ],\n          [\n            \"tail_decay\",\n            \"reference\",\n            0.004,\n            0.05,\n            \"H1_stationary\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"In-distribution results are solid. The dual dynamics split appears clean: 3 H2 features drift, 4 H1 features are stationary. Perplexity signal is very strong. However, the worst-tier interpretation is that this clean separation is partly an artifact of the Pythia-Pythia configuration. Subsequent experiments (plan_003, plan_013) will show the H2 drift is partially confounded by length artifacts and reference-model specificity.\\n\\n\\nThese results are from actual execution and look encouraging. But they are entirely in-distribution: single generator (Pythia-2.8B), same-family reference (Pythia-410M), no length control. The 0.82 full F1 benefits from generator-specific artifacts that the reference model can detect precisely because it shares the Pythia architecture. The H2 entropy_mean drift (ρ=-0.68) is strong here because Pythia-410M and Pythia-2.8B share tokenizer and distributional priors — the reference model's perplexity is calibrated to the generator's output distribution. The perplexity monotonic decrease (13.5→1.7) is real but partially reflects the reference model's familiarity with same-family outputs. In worst tier, subsequent experiments reveal these as inflated baselines.\\n\"\n  },\n  {\n    \"name\": \"cross_generator_evaluation\",\n    \"description\": \"Leave-one-generator-out evaluation across 5 generators. Tests cross-generator generalization. In worst tier, LOGO F1 is poor, especially when holding out non-Pythia generators.\\n\",\n    \"results\": {\n      \"overall_logo_macro_f1\": 0.52,\n      \"logo_holdout_pythia28b\": 0.61,\n      \"logo_holdout_pythia1b\": 0.64,\n      \"logo_holdout_olmo2\": 0.48,\n      \"logo_holdout_qwen17b\": 0.44,\n      \"logo_holdout_qwen06b\": 0.43,\n      \"within_family_avg_f1\": 0.625,\n      \"cross_family_avg_f1\": 0.45,\n      \"leave_one_family_out_pythia_held_in\": 0.58,\n      \"leave_one_family_out_pythia_held_out\": 0.41\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Leave-One-Generator-Out Macro-F1\",\n        \"columns\": [\n          \"held_out_generator\",\n          \"family\",\n          \"macro_f1\",\n          \"gen0_f1\",\n          \"gen1_f1\",\n          \"gen2plus_f1\"\n        ],\n        \"rows\": [\n          [\n            \"pythia-2.8b\",\n            \"pythia\",\n            0.61,\n            0.82,\n            0.51,\n            0.5\n          ],\n          [\n            \"pythia-1b\",\n            \"pythia\",\n            0.64,\n            0.85,\n            0.54,\n            0.53\n          ],\n          [\n            \"olmo-2-1b\",\n            \"olmo\",\n            0.48,\n            0.72,\n            0.38,\n            0.34\n          ],\n          [\n            \"qwen3-1.7b\",\n            \"qwen\",\n            0.44,\n            0.68,\n            0.35,\n            0.29\n          ],\n          [\n            \"qwen3-0.6b\",\n            \"qwen\",\n            0.43,\n            0.67,\n            0.33,\n            0.29\n          ],\n          [\n            \"mean (all)\",\n            \"-\",\n            0.52,\n            0.75,\n            0.42,\n            0.39\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: Leave-One-Family-Out\",\n        \"columns\": [\n          \"held_out_family\",\n          \"train_generators\",\n          \"macro_f1\"\n        ],\n        \"rows\": [\n          [\n            \"pythia\",\n            \"olmo+qwen\",\n            0.41\n          ],\n          [\n            \"olmo\",\n            \"pythia+qwen\",\n            0.54\n          ],\n          [\n            \"qwen\",\n            \"pythia+olmo\",\n            0.56\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-generator generalization fails the 0.58 threshold. The within-family vs cross-family gap (0.625 vs 0.45) reveals the classifier relies on generator-specific artifacts. Gen-0 detection remains passable (~0.75 average) because human-written text is universally distinct, but gen-1 vs gen-2+ discrimination (the core depth signal) collapses cross-family. This undermines Claim 1's generalization requirement. In the reframed paper, this becomes evidence for: \\\"depth estimation requires generator-aware features or larger, more diverse training sets — the task is harder than binary detection because depth artifacts are generator-specific.\\\"\\n\\n\\nThe classifier overfits to generator-specific artifacts rather than learning universal depth signatures. Within the Pythia family, generalization is passable (0.61–0.64) because Pythia-2.8B and Pythia-1B share tokenizer, training data (The Pile), and architectural patterns — the Pythia-410M reference model's NLL features are structurally similar for both. But cross-family holdouts (OLMo, Qwen) drop sharply to 0.43–0.48 because: (a) different tokenizers mean surface features (TTR, hapax) have different baseline distributions, (b) the Pythia-410M reference model assigns systematically different perplexity distributions to non-Pythia outputs, creating a domain shift in entropy features, (c) each generator family has its own repetition/diversity profile at each depth, so depth-correlated patterns learned from one family don't transfer. The leave-one-family-out result (0.41 when Pythia held out) confirms the classifier critically depends on Pythia-specific patterns. Overall LOGO F1 of 0.52 is below the 0.58 threshold, killing the cross-generator generalization claim.\\n\"\n  },\n  {\n    \"name\": \"cross_family_reference_model\",\n    \"description\": \"Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B) for feature extraction. Critical falsification test for the dual dynamics framework.\\n\",\n    \"results\": {\n      \"olmo_ref_entropy_mean_rho\": -0.22,\n      \"qwen_ref_entropy_mean_rho\": -0.15,\n      \"pythia_ref_entropy_mean_rho\": -0.68,\n      \"olmo_ref_full_f1\": 0.63,\n      \"qwen_ref_full_f1\": 0.58,\n      \"pythia_ref_full_f1\": 0.82,\n      \"olmo_ref_h2_features_count\": 1,\n      \"qwen_ref_h2_features_count\": 1,\n      \"cross_family_ref_entropy_mean_rho_avg\": -0.185,\n      \"shape_features_h1_stable_across_refs\": true,\n      \"ttr_rho_across_refs\": -0.3,\n      \"hapax_rho_across_refs\": -0.27\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Entropy_mean Depth Correlation by Reference Model\",\n        \"columns\": [\n          \"reference_model\",\n          \"family\",\n          \"entropy_mean_rho\",\n          \"p_value\",\n          \"h2_classification\"\n        ],\n        \"rows\": [\n          [\n            \"pythia-410m\",\n            \"pythia\",\n            -0.68,\n            \"<0.001\",\n            \"H2_confirmed\"\n          ],\n          [\n            \"olmo-2-1b\",\n            \"olmo\",\n            -0.22,\n            0.031,\n            \"H2_weak (|ρ|<0.3)\"\n          ],\n          [\n            \"qwen3-0.6b\",\n            \"qwen\",\n            -0.15,\n            0.118,\n            \"H2_not_confirmed\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: Full Feature Set Classification by Reference Model\",\n        \"columns\": [\n          \"reference_model\",\n          \"macro_f1\",\n          \"surface_only_f1\",\n          \"ref_only_f1\",\n          \"full_vs_surface_gap\"\n        ],\n        \"rows\": [\n          [\n            \"pythia-410m\",\n            0.82,\n            0.76,\n            0.72,\n            0.06\n          ],\n          [\n            \"olmo-2-1b\",\n            0.63,\n            0.61,\n            0.48,\n            0.02\n          ],\n          [\n            \"qwen3-0.6b\",\n            0.58,\n            0.57,\n            0.41,\n            0.01\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7: H1/H2 Stability Across Reference Models\",\n        \"columns\": [\n          \"feature\",\n          \"pythia_class\",\n          \"olmo_class\",\n          \"qwen_class\",\n          \"stable_across_refs\"\n        ],\n        \"rows\": [\n          [\n            \"entropy_mean\",\n            \"H2\",\n            \"weak/NS\",\n            \"NS\",\n            \"NO\"\n          ],\n          [\n            \"entropy_std\",\n            \"H1\",\n            \"H1\",\n            \"H1\",\n            \"YES\"\n          ],\n          [\n            \"entropy_max\",\n            \"H1\",\n            \"H1\",\n            \"H1\",\n            \"YES\"\n          ],\n          [\n            \"tail_decay\",\n            \"H1\",\n            \"H1\",\n            \"H1\",\n            \"YES\"\n          ],\n          [\n            \"ttr\",\n            \"H2\",\n            \"H2\",\n            \"H2\",\n            \"YES\"\n          ],\n          [\n            \"hapax_ratio\",\n            \"H2\",\n            \"H2\",\n            \"weak H2\",\n            \"YES (marginal)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The key falsification test triggers: entropy_mean's H2 drift was substantially a Pythia-specific artifact. The dual dynamics narrative (\\\"level features drift, shape features don't, and this cross-cuts surface/reference\\\") collapses because the cross-cutting evidence depended on entropy_mean being a reference feature that drifts. Without it, H2 features are just surface features (TTR, hapax), and H1 features are just reference features — exactly the naive expectation the paper claimed to overturn. The shape feature H1 stability is real but less interesting: it says \\\"distributional shape under any reference model is stable across depth,\\\" which is a weaker claim. In the reframed paper, this becomes: \\\"reference-model perplexity as depth proxy is reference-model-dependent — a same-family reference provides much stronger signal, pointing toward an alignment-based explanation of depth discriminability.\\\"\\n\\n\\nEntropy_mean drift (ρ=-0.68 with Pythia reference) largely disappears with non-Pythia references (ρ≈-0.22 OLMo, ρ≈-0.15 Qwen). This happens because entropy_mean is driven by how well the reference model predicts the generated text — when the reference model shares architecture and training data with the generator (Pythia-Pythia), it has calibrated predictions that systematically shift with depth. A cross-family reference model assigns noisier, less calibrated perplexities, washing out the drift signal. The |ρ|<0.3 threshold is breached for both non-Pythia references. Shape features (entropy_std, entropy_max, tail_decay) remain H1-stationary across all references — this is genuinely robust because distributional shape is less sensitive to absolute calibration. But the H2 side of the \\\"dual dynamics\\\" now has only surface features (TTR, hapax_ratio) showing reliable drift (ρ≈-0.28 to -0.30), and these are precisely the features confounded by text length (plan_013). The \\\"dual dynamics cross-cuts surface/reference boundary\\\" claim collapses: the cross-cutting was an artifact of Pythia-Pythia alignment. Classification F1 with non-Pythia reference drops to 0.58–0.63 because the strongest H2 reference feature is now noise.\\n\"\n  },\n  {\n    \"name\": \"downstream_utility\",\n    \"description\": \"Fine-tune OLMo-1B on depth-stratified data. Compare depth-aware filtering vs binary baselines with 3+ seeds and bootstrap CIs. In worst tier, the advantage is not statistically significant.\\n\",\n    \"results\": {\n      \"depth_quality_spearman\": 0.28,\n      \"depth_quality_spearman_ci\": \"[0.11, 0.45]\",\n      \"depth_filtering_ppl_improvement_pct\": 1.8,\n      \"depth_filtering_ppl_improvement_ci\": \"[-0.5, 4.1]\",\n      \"binary_filtering_ppl_improvement_pct\": 1.2,\n      \"binary_filtering_ppl_improvement_ci\": \"[-1.1, 3.5]\",\n      \"depth_vs_binary_p_value\": 0.31,\n      \"sample_matched_depth_ppl\": 14.2,\n      \"sample_matched_binary_ppl\": 14.5,\n      \"sample_matched_p_value\": 0.42,\n      \"seed_variance_cv\": 0.08,\n      \"n_seeds\": 5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Downstream Fine-Tuning Results (OLMo-1B, 5 seeds)\",\n        \"columns\": [\n          \"filtering_strategy\",\n          \"mean_ppl\",\n          \"std_ppl\",\n          \"95_ci\",\n          \"improvement_vs_unfiltered_pct\"\n        ],\n        \"rows\": [\n          [\n            \"unfiltered\",\n            14.8,\n            0.42,\n            \"[14.2, 15.4]\",\n            \"-\"\n          ],\n          [\n            \"binary_fastdetectgpt\",\n            14.5,\n            0.51,\n            \"[13.8, 15.2]\",\n            \"1.2 [-1.1, 3.5]\"\n          ],\n          [\n            \"binary_ldscore\",\n            14.6,\n            0.48,\n            \"[14.0, 15.2]\",\n            \"0.9 [-1.4, 3.2]\"\n          ],\n          [\n            \"depth_aware_keep_gen01\",\n            14.2,\n            0.39,\n            \"[13.7, 14.7]\",\n            \"1.8 [-0.5, 4.1]\"\n          ],\n          [\n            \"depth_aware_sample_matched\",\n            14.2,\n            0.44,\n            \"[13.6, 14.8]\",\n            \"1.5 [-0.8, 3.8]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: Depth-Quality Correlation\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"95_ci\"\n        ],\n        \"rows\": [\n          [\n            \"spearman_rho\",\n            0.28,\n            \"[0.11, 0.45]\"\n          ],\n          [\n            \"ppl_gen0_mean\",\n            12.1,\n            \"[11.8, 12.4]\"\n          ],\n          [\n            \"ppl_gen1_mean\",\n            13.4,\n            \"[12.9, 13.9]\"\n          ],\n          [\n            \"ppl_gen2_mean\",\n            14.1,\n            \"[13.5, 14.7]\"\n          ],\n          [\n            \"ppl_gen3_mean\",\n            14.5,\n            \"[13.8, 15.2]\"\n          ],\n          [\n            \"ppl_gen4_mean\",\n            14.9,\n            \"[14.1, 15.7]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Downstream utility claim fails significance after proper experimental controls. The improvement exists directionally (1.8% vs 1.2%) but CIs overlap. This was the most anticipated outcome from dream reviews: single-run results are fragile. In reframed paper, report honestly as \\\"directional evidence for depth-quality correlation, insufficient for statistical significance at this sample size\\\" and pivot to the correlation itself (ρ=0.28) as motivation for future work. The perplexity-by-depth monotonic relationship (Table 9) is real and publishable as a descriptive finding — it just doesn't translate into significant downstream filtering advantage.\\n\\n\\nWith proper experimental controls (multiple seeds, CIs, sample-count matching, non-Pythia model), the downstream advantage of depth-aware filtering shrinks to statistical insignificance. Several factors contribute: (1) OLMo-1B is more robust to training data contamination than Pythia-410M (the original MVP model), reducing the overall signal magnitude; (2) with 5 seeds, the variance across runs is substantial (CV≈0.08), swamping the small depth-vs-binary difference; (3) the sample-count-matched comparison shows the original advantage was partly a data size confound — depth-aware filtering keeps more data (it retains gen-1) than binary filtering (which discards all synthetic), so the improvement was partially from having more training data, not from depth stratification per se; (4) bootstrap CIs for the depth-vs-binary comparison overlap substantially (p=0.31), failing significance. The Spearman ρ=0.28 between predicted depth and quality degradation is real but weak, falling in the [0.15, 0.4] worst-tier range. In isolation, this correlation is interesting but not actionable. Claim 3 (downstream utility) cannot be supported as \\\"significantly outperforms binary baselines.\\\"\\n\"\n  },\n  {\n    \"name\": \"prompt_type_comparison\",\n    \"description\": \"Compare continuation vs elaboration vs inspired_rewriting chains. In worst tier, depth signal varies dramatically by prompt type, undermining generalizability.\\n\",\n    \"results\": {\n      \"continuation_macro_f1\": 0.78,\n      \"elaboration_macro_f1\": 0.55,\n      \"inspired_rewriting_macro_f1\": 0.47,\n      \"continuation_entropy_mean_rho\": -0.65,\n      \"elaboration_entropy_mean_rho\": -0.38,\n      \"rewriting_entropy_mean_rho\": -0.18,\n      \"cross_prompt_train_test_f1\": 0.42\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Depth Classification by Prompt Type\",\n        \"columns\": [\n          \"prompt_type\",\n          \"macro_f1\",\n          \"entropy_mean_rho\",\n          \"ttr_rho\",\n          \"gen1_vs_gen2plus_f1\"\n        ],\n        \"rows\": [\n          [\n            \"continuation\",\n            0.78,\n            -0.65,\n            -0.29,\n            0.71\n          ],\n          [\n            \"elaboration\",\n            0.55,\n            -0.38,\n            -0.16,\n            0.44\n          ],\n          [\n            \"inspired_rewriting\",\n            0.47,\n            -0.18,\n            -0.08,\n            0.36\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 11: Cross-Prompt Transfer\",\n        \"columns\": [\n          \"train_prompt\",\n          \"test_prompt\",\n          \"macro_f1\"\n        ],\n        \"rows\": [\n          [\n            \"continuation\",\n            \"elaboration\",\n            0.46\n          ],\n          [\n            \"continuation\",\n            \"rewriting\",\n            0.39\n          ],\n          [\n            \"elaboration\",\n            \"continuation\",\n            0.51\n          ],\n          [\n            \"elaboration\",\n            \"rewriting\",\n            0.42\n          ],\n          [\n            \"rewriting\",\n            \"continuation\",\n            0.44\n          ],\n          [\n            \"rewriting\",\n            \"elaboration\",\n            0.4\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Prompt type is a major moderator of depth signal, challenging ecological validity. In the reframed paper, this becomes a positive finding for the task formulation angle: \\\"Generation depth estimation difficulty depends critically on the semantic coupling between generation steps. Continuation chains (high coupling) preserve depth signal; rewriting chains (low coupling) do not. This connects to attractor cycle theory — semantic-preserving chains converge, while semantically divergent chains don't accumulate distributional drift.\\\"\\n\\n\\nDepth signal is strongly prompt-type dependent. Continuation chains preserve the strongest signal (F1=0.78) because each generation builds directly on the previous output, creating cumulative distributional drift. Elaboration chains weaken the signal (F1=0.55) because the model is asked to expand on a topic rather than continue text — this introduces more creative variation that partially resets the distributional state at each depth. Inspired rewriting shows near-chance depth discrimination (F1=0.47) because the semantic departure from the source is maximal — each depth step is essentially an independent generation conditioned on a theme, not a recursive chain. The entropy_mean drift follows the same pattern (ρ: -0.65/-0.38/-0.18). When training on one prompt type and testing on another, F1 drops to 0.42, showing the features are prompt-type-specific. This means the \\\"depth signal\\\" is partly a \\\"continuation-chain-specific\\\" artifact — real web contamination involves diverse generation patterns, not just continuation.\\n\"\n  },\n  {\n    \"name\": \"paraphrastic_comparison\",\n    \"description\": \"Compare paraphrasing vs continuation chains. In worst tier, paraphrasing chains converge quickly (as attractor theory predicts), but continuation chains also show limited depth discrimination beyond gen-2.\\n\",\n    \"results\": {\n      \"paraphrastic_3class_f1\": 0.52,\n      \"nonparaphrastic_3class_f1\": 0.78,\n      \"paraphrastic_entropy_mean_plateau_depth\": 2,\n      \"nonparaphrastic_saturation_depth\": 3,\n      \"paraphrastic_gen2_vs_gen3_f1\": 0.34,\n      \"nonparaphrastic_gen2_vs_gen3_f1\": 0.41\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Paraphrastic vs Non-Paraphrastic Depth Discrimination\",\n        \"columns\": [\n          \"chain_type\",\n          \"3class_f1\",\n          \"gen0_f1\",\n          \"gen1_f1\",\n          \"gen2plus_f1\",\n          \"entropy_mean_rho\"\n        ],\n        \"rows\": [\n          [\n            \"paraphrastic\",\n            0.52,\n            0.78,\n            0.45,\n            0.33,\n            -0.31\n          ],\n          [\n            \"continuation\",\n            0.78,\n            0.93,\n            0.72,\n            0.69,\n            -0.65\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Confirms attractor theory prediction for paraphrastic chains. Continuation chains have more signal but also saturate. In reframed paper: \\\"Our empirical results are consistent with attractor convergence — extending the theory to non-paraphrastic chains shows the convergence is slower but still present, bounding practical depth estimation to ~3 useful classes.\\\"\\n\\n\\nParaphrasing chains converge by depth 2 as attractor theory predicts — gen-2, gen-3, gen-4 are nearly indistinguishable (F1=0.34 for gen-2 vs gen-3). Continuation chains preserve more signal but also saturate by depth 3 — the distributional drift accumulates but with diminishing marginal signal at each step. The worst-tier interpretation: even non-paraphrastic chains have bounded depth discriminability, just with a slightly higher ceiling than paraphrastic ones. The difference (0.78 vs 0.52) confirms continuation chains are better for depth estimation but doesn't rescue the broader generalizability problem — the signal is still chain-type-specific and bounded.\\n\"\n  },\n  {\n    \"name\": \"cross_model_chains\",\n    \"description\": \"Cross-model chains (different generator per depth step). In worst tier, cross-model chains destroy depth signal because generator identity dominates depth identity.\\n\",\n    \"results\": {\n      \"cross_model_macro_f1\": 0.39,\n      \"single_model_macro_f1\": 0.78,\n      \"cross_model_gen0_f1\": 0.65,\n      \"cross_model_gen1_f1\": 0.28,\n      \"cross_model_gen2plus_f1\": 0.24,\n      \"cross_vs_single_delta\": -0.39\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Single-Model vs Cross-Model Chains\",\n        \"columns\": [\n          \"chain_type\",\n          \"macro_f1\",\n          \"gen0_f1\",\n          \"gen1_f1\",\n          \"gen2plus_f1\"\n        ],\n        \"rows\": [\n          [\n            \"single_model\",\n            0.78,\n            0.93,\n            0.72,\n            0.69\n          ],\n          [\n            \"cross_model_random\",\n            0.39,\n            0.65,\n            0.28,\n            0.24\n          ],\n          [\n            \"cross_model_increasing_size\",\n            0.41,\n            0.66,\n            0.3,\n            0.27\n          ],\n          [\n            \"cross_model_decreasing_size\",\n            0.38,\n            0.63,\n            0.27,\n            0.24\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-model chains destroy depth signal — generator identity is a much stronger signal than depth in the feature space. This is the ecological validity nail: real web contamination involves diverse generators. In reframed paper, this honestly motivates future work on generator-invariant depth features and positions the current features as a baseline that works in controlled (single-generator) settings but not in the wild.\\n\\n\\nCross-model chains are dramatically harder (F1=0.39, essentially near chance for gen-1 and gen-2+). The reason is fundamental: when generator identity changes at each depth step, the distributional features capture generator identity more than depth. A gen-1 text from Qwen looks more different from gen-1 text from Pythia than gen-1 looks from gen-2 within the same generator. The features (NLL statistics under a fixed reference model) are sensitive to the generator's output distribution, creating a confound where generator variation swamps depth variation. Gen-0 remains detectable (F1=0.65) because human-written text is still distinct from any machine-generated text, but ordinal depth discrimination collapses. This is perhaps the strongest negative result: in the realistic scenario of diverse web generators, depth estimation with these features is not viable.\\n\"\n  },\n  {\n    \"name\": \"multi_domain_seeds\",\n    \"description\": \"Expand to 4 domains. In worst tier, significant domain variance with some domains showing near-chance performance.\\n\",\n    \"results\": {\n      \"wikipedia_macro_f1\": 0.72,\n      \"news_macro_f1\": 0.68,\n      \"scientific_macro_f1\": 0.55,\n      \"creative_macro_f1\": 0.48,\n      \"overall_macro_f1\": 0.61,\n      \"cross_domain_train_test_f1\": 0.49,\n      \"domain_f1_std\": 0.11\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: Depth Classification by Domain\",\n        \"columns\": [\n          \"domain\",\n          \"n_seeds\",\n          \"macro_f1\",\n          \"gen0_f1\",\n          \"gen1_f1\",\n          \"gen2plus_f1\"\n        ],\n        \"rows\": [\n          [\n            \"wikipedia\",\n            500,\n            0.72,\n            0.89,\n            0.63,\n            0.64\n          ],\n          [\n            \"news\",\n            500,\n            0.68,\n            0.86,\n            0.59,\n            0.59\n          ],\n          [\n            \"scientific\",\n            500,\n            0.55,\n            0.78,\n            0.44,\n            0.43\n          ],\n          [\n            \"creative\",\n            500,\n            0.48,\n            0.71,\n            0.37,\n            0.36\n          ],\n          [\n            \"all_pooled\",\n            2000,\n            0.61,\n            0.81,\n            0.51,\n            0.51\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain is a significant moderator. Factual domains have more signal; creative domains have less. In reframed paper: \\\"Depth estimation difficulty depends on the entropy of the source domain — low-entropy domains (wiki, news) produce more predictable generations with clearer depth drift; high-entropy domains (creative) mask depth signal with natural variation.\\\"\\n\\n\\nDomain variance is substantial. Wikipedia and news seeds (factual, structured prose) show passable performance because LLMs generate predictable continuations with consistent distributional drift. Scientific abstracts show weaker signal because the specialized vocabulary and formulaic structure reduce the distinguishability of human vs machine text at each depth. Creative writing shows near-chance performance because it has the highest natural language variance — the within-class variation in features (e.g., TTR, hapax_ratio) for creative text at any depth is large enough to swamp the between-class (depth) variation. Cross-domain transfer is poor (0.49) because the feature baselines differ across domains. This adds another moderator (domain + prompt type + generator family) that limits the generalizability of depth estimation.\\n\"\n  },\n  {\n    \"name\": \"finer_grained_ordinal\",\n    \"description\": \"5-class ordinal classification (gen-0 through gen-4). In worst tier, performance is near chance for finer classes.\\n\",\n    \"results\": {\n      \"five_class_macro_f1\": 0.28,\n      \"three_class_macro_f1\": 0.78,\n      \"gen0_f1\": 0.85,\n      \"gen1_f1\": 0.42,\n      \"gen2_f1\": 0.18,\n      \"gen3_f1\": 0.12,\n      \"gen4_f1\": 0.11,\n      \"ordinal_mae\": 1.4,\n      \"adjacent_confusion_pct\": 0.72\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Five-Class Ordinal Classification\",\n        \"columns\": [\n          \"class\",\n          \"precision\",\n          \"recall\",\n          \"f1\",\n          \"n_samples\"\n        ],\n        \"rows\": [\n          [\n            \"gen-0\",\n            0.88,\n            0.82,\n            0.85,\n            995\n          ],\n          [\n            \"gen-1\",\n            0.39,\n            0.45,\n            0.42,\n            993\n          ],\n          [\n            \"gen-2\",\n            0.16,\n            0.2,\n            0.18,\n            912\n          ],\n          [\n            \"gen-3\",\n            0.11,\n            0.13,\n            0.12,\n            856\n          ],\n          [\n            \"gen-4\",\n            0.1,\n            0.12,\n            0.11,\n            816\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Five-class is essentially unsolvable with current features. Confirms the 3-class ceiling. In reframed paper, this is a benchmark result: \\\"We establish that 3-class depth estimation (gen-0/gen-1/gen-2+) is the practical ceiling for distributional features, consistent with attractor convergence theory extended to non-paraphrastic generation.\\\"\\n\\n\\nFive-class F1 of 0.28 is barely above chance (0.20 for 5 classes). Gen-0 remains detectable (F1=0.85) and gen-1 is marginally separable (F1=0.42), but gen-2/3/4 collapse into an indistinguishable cluster (F1: 0.18/0.12/0.11). This is because distributional drift between adjacent deep generations is minimal — the marginal change from gen-2→gen-3 in any feature is smaller than the within-class variance. The ordinal MAE of 1.4 means predictions are off by ~1.4 depth levels on average. 72% of misclassifications are between adjacent classes, suggesting some ordinal structure remains but is too weak for practical 5-class discrimination. This validates the attractor convergence prediction: beyond ~3 classes, depth signal is negligible even for non-paraphrastic chains.\\n\"\n  },\n  {\n    \"name\": \"human_edit_robustness\",\n    \"description\": \"Robustness to simulated human edits. In worst tier, even mild edits substantially degrade performance.\\n\",\n    \"results\": {\n      \"baseline_f1\": 0.78,\n      \"random_replace_5pct_f1\": 0.68,\n      \"random_replace_10pct_f1\": 0.58,\n      \"random_replace_20pct_f1\": 0.44,\n      \"llm_light_edit_f1\": 0.53,\n      \"f1_drop_at_5pct\": -0.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 16: Robustness to Human Edits\",\n        \"columns\": [\n          \"edit_type\",\n          \"edit_rate\",\n          \"macro_f1\",\n          \"delta_f1\"\n        ],\n        \"rows\": [\n          [\n            \"none\",\n            \"0%\",\n            0.78,\n            \"-\"\n          ],\n          [\n            \"random_replace\",\n            \"5%\",\n            0.68,\n            -0.1\n          ],\n          [\n            \"random_replace\",\n            \"10%\",\n            0.58,\n            -0.2\n          ],\n          [\n            \"random_replace\",\n            \"20%\",\n            0.44,\n            -0.34\n          ],\n          [\n            \"llm_light_edit\",\n            \"~8%\",\n            0.53,\n            -0.25\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Depth features are fragile to post-generation modification. In reframed paper: \\\"Depth estimation is most applicable to unedited generation chains (e.g., automated content farms) and degrades rapidly with human post-processing. This constrains the practical applicability to detection of fully automated pipelines.\\\"\\n\\n\\nEven 5% random word replacement drops F1 by 0.10, and LLM-simulated light editing drops F1 by 0.25. The features are brittle to post-generation modification because both surface features (TTR, hapax) and reference features (entropy statistics) are sensitive to token-level changes. A few word substitutions can significantly alter hapax ratio, TTR, and the reference model's NLL distribution. LLM-simulated editing is worse than random replacement because it systematically \\\"cleans up\\\" the distributional artifacts that depth estimation relies on — an LLM editing gen-3 text makes it look more like gen-1 by smoothing out the accumulated drift. This is a fundamental limitation: any real-world post-processing pipeline (human editing, automated cleanup, grammar correction) will degrade depth signal.\\n\"\n  },\n  {\n    \"name\": \"ld_score_feature\",\n    \"description\": \"Add LD-Score as feature. In worst tier, LD-Score shows inconsistent behavior — neither clearly H2 nor clearly adding value.\\n\",\n    \"results\": {\n      \"ldscore_depth_rho\": -0.25,\n      \"ldscore_added_f1_delta\": 0.005,\n      \"ldscore_h2_classification\": \"weak/ambiguous\",\n      \"with_ldscore_f1\": 0.785,\n      \"without_ldscore_f1\": 0.78\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 17: LD-Score as Depth Feature\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"ldscore_depth_rho\",\n            -0.25\n          ],\n          [\n            \"ldscore_slope_R2\",\n            0.12\n          ],\n          [\n            \"feature_set_without_ldscore_f1\",\n            0.78\n          ],\n          [\n            \"feature_set_with_ldscore_f1\",\n            0.785\n          ],\n          [\n            \"ldscore_feature_importance_rank\",\n            \"7/8\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LD-Score pre-registered prediction is weakly supported but insufficient to validate the level/shape framework given that the framework is independently undermined by plan_003. In reframed paper: \\\"LD-Score shows weak depth sensitivity, consistent with character-level features capturing some vocabulary drift, but insufficient to serve as independent validation of the dual dynamics hypothesis.\\\"\\n\\n\\nLD-Score shows weak depth correlation (ρ=-0.25), not clearly meeting H2 criteria (slope significant but R²<0.15). Character-level distribution is a noisy proxy for depth — it captures some vocabulary shift but is contaminated by topic and style variation. Adding LD-Score to the feature set provides negligible improvement (+0.005 F1), well within noise. The pre-registered prediction that LD-Score would be a \\\"level feature\\\" exhibiting H2 drift is partially supported (negative ρ) but weak. In worst tier, this fails to provide out-of-sample validation for the level/shape framework because the framework itself is collapsing (plan_003 shows H2 is reference-model-dependent).\\n\"\n  },\n  {\n    \"name\": \"end_to_end_classifier\",\n    \"description\": \"QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification. In worst tier, end-to-end slightly outperforms handcrafted features, undermining the feature analysis.\\n\",\n    \"results\": {\n      \"e2e_macro_f1\": 0.83,\n      \"handcrafted_macro_f1\": 0.78,\n      \"e2e_cross_generator_f1\": 0.55,\n      \"e2e_vs_handcrafted_delta\": 0.05,\n      \"e2e_gen1_vs_gen2plus_f1\": 0.76\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 18: End-to-End vs Handcrafted Features\",\n        \"columns\": [\n          \"method\",\n          \"in_dist_f1\",\n          \"cross_gen_logo_f1\",\n          \"training_cost_gpu_h\"\n        ],\n        \"rows\": [\n          [\n            \"handcrafted_xgboost\",\n            0.78,\n            0.52,\n            0.1\n          ],\n          [\n            \"qwen_qolra_e2e\",\n            0.83,\n            0.55,\n            15\n          ],\n          [\n            \"qwen_qolra_frozen\",\n            0.8,\n            0.53,\n            8\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"End-to-end slightly beats handcrafted but shares the generalization failure. In reframed paper: \\\"Both handcrafted and learned features achieve similar in-distribution performance and similar cross-generator degradation, suggesting the depth estimation difficulty is fundamental to the feature space, not a limitation of our specific feature engineering.\\\"\\n\\n\\nEnd-to-end classification achieves F1=0.83, slightly above the handcrafted 0.78, suggesting that learned representations capture additional signal beyond the 7 distributional features. However, the improvement is modest and the end-to-end model also fails to generalize cross-generator (F1=0.55), indicating the additional signal is also generator-specific. This undercuts the feature analysis contribution: if a fine-tuned LM can slightly beat the handcrafted features, the dual dynamics decomposition is more of an interpretability lens than a competitive method. In worst tier, this result slightly undermines the feature-level analysis without providing a clearly superior alternative — neither approach generalizes.\\n\"\n  },\n  {\n    \"name\": \"text_length_control\",\n    \"description\": \"Text length confound analysis. In worst tier, length-controlled F1 drops >0.08, revealing that surface features substantially tracked length.\\n\",\n    \"results\": {\n      \"length_depth_correlation\": 0.42,\n      \"original_full_f1\": 0.78,\n      \"length_controlled_full_f1\": 0.68,\n      \"length_controlled_f1_delta\": -0.1,\n      \"length_controlled_surface_f1\": 0.63,\n      \"length_controlled_reference_f1\": 0.66,\n      \"length_normalized_ttr_rho\": -0.12,\n      \"length_normalized_hapax_rho\": -0.09,\n      \"original_ttr_rho\": -0.31,\n      \"original_hapax_rho\": -0.28,\n      \"length_matched_f1\": 0.7\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 19: Length Confound Analysis\",\n        \"columns\": [\n          \"condition\",\n          \"full_f1\",\n          \"surface_f1\",\n          \"reference_f1\",\n          \"full_vs_surface_gap\"\n        ],\n        \"rows\": [\n          [\n            \"original\",\n            0.78,\n            0.76,\n            0.72,\n            0.02\n          ],\n          [\n            \"length_normalized_features\",\n            0.68,\n            0.63,\n            0.66,\n            0.02\n          ],\n          [\n            \"length_matched_subsampling\",\n            0.7,\n            0.65,\n            0.67,\n            0.03\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 20: Feature Depth Correlation Before/After Length Control\",\n        \"columns\": [\n          \"feature\",\n          \"original_rho\",\n          \"length_normalized_rho\",\n          \"pct_explained_by_length\"\n        ],\n        \"rows\": [\n          [\n            \"ttr\",\n            -0.31,\n            -0.12,\n            \"61%\"\n          ],\n          [\n            \"hapax_ratio\",\n            -0.28,\n            -0.09,\n            \"68%\"\n          ],\n          [\n            \"entropy_mean\",\n            -0.68,\n            -0.55,\n            \"19%\"\n          ],\n          [\n            \"entropy_std\",\n            0.03,\n            0.02,\n            \"33%\"\n          ],\n          [\n            \"tail_decay\",\n            0.04,\n            0.03,\n            \"25%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Length confound is substantial. ~60-68% of surface feature depth correlation was length artifact. Reference features are less affected (19% for entropy_mean) but still impacted. After controlling for length, the full-vs-surface gap nearly vanishes (0.02), meaning reference features' advantage was partially from being less length-confounded, not from capturing genuinely different depth signal. In reframed paper: \\\"We identify text length as a major confound in depth estimation: standard surface diversity metrics (TTR, hapax ratio) primarily track length variation rather than genuine distributional drift. Length-controlled analysis reveals a weaker but real residual depth signal, predominantly carried by reference-model perplexity statistics.\\\"\\n\\n\\nText length correlates with depth (r=0.42) — deeper generations tend to be shorter as models produce more repetitive/compressed outputs. This correlation confounds both surface features and indirectly reference features. TTR and hapax_ratio are mechanically length-dependent (shorter texts have higher TTR, lower hapax ratio), so their depth correlation (ρ≈-0.3) was partially a length proxy. After length normalization (fixed-window computation), TTR depth correlation drops from -0.31 to -0.12 and hapax from -0.28 to -0.09 — most of the \\\"H2 drift\\\" in surface features was length artifact. Length-controlled full F1 drops by 0.10 (from 0.78 to 0.68), breaching the >0.08 threshold. Notably, reference features also drop (from 0.72 to 0.66) because entropy statistics are affected by text length through the number of tokens evaluated. After length matching (subsampling to equalize length distributions), F1 is 0.70 — real depth signal exists but is substantially weaker than originally measured. The full-vs-surface gap shrinks (0.68 vs 0.63 = 0.05 gap → 0.02 gap after removing length confound from surface features).\\n\"\n  },\n  {\n    \"name\": \"large_scale_generator\",\n    \"description\": \"Add 7B+ generator (Qwen3-8B-Base). In worst tier, depth signal is minimal at this scale — larger models produce more fluent text that masks distributional drift.\\n\",\n    \"results\": {\n      \"generator_7bplus_macro_f1\": 0.43,\n      \"generator_7bplus_gen0_f1\": 0.62,\n      \"generator_7bplus_gen1_f1\": 0.35,\n      \"generator_7bplus_gen2plus_f1\": 0.32,\n      \"generator_7bplus_entropy_mean_rho\": -0.19,\n      \"small_generator_avg_f1\": 0.72,\n      \"f1_vs_generator_size_correlation\": -0.85,\n      \"generator_7bplus_ppl_depth0\": 8.2,\n      \"generator_7bplus_ppl_depth4\": 4.1,\n      \"ppl_dynamic_range_7bplus\": 4.1,\n      \"ppl_dynamic_range_2_8b\": 11.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 21: Depth Classification by Generator Scale\",\n        \"columns\": [\n          \"generator\",\n          \"params\",\n          \"macro_f1\",\n          \"gen0_f1\",\n          \"gen1_f1\",\n          \"gen2plus_f1\",\n          \"entropy_mean_rho\"\n        ],\n        \"rows\": [\n          [\n            \"qwen3-0.6b\",\n            \"0.6B\",\n            0.74,\n            0.91,\n            0.66,\n            0.65,\n            -0.58\n          ],\n          [\n            \"pythia-1b\",\n            \"1B\",\n            0.71,\n            0.89,\n            0.62,\n            0.62,\n            -0.55\n          ],\n          [\n            \"olmo-2-1b\",\n            \"1.5B\",\n            0.69,\n            0.87,\n            0.6,\n            0.6,\n            -0.51\n          ],\n          [\n            \"qwen3-1.7b\",\n            \"1.7B\",\n            0.68,\n            0.86,\n            0.58,\n            0.6,\n            -0.48\n          ],\n          [\n            \"pythia-2.8b\",\n            \"2.8B\",\n            0.78,\n            0.93,\n            0.72,\n            0.69,\n            -0.68\n          ],\n          [\n            \"qwen3-8b\",\n            \"8B\",\n            0.43,\n            0.62,\n            0.35,\n            0.32,\n            -0.19\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 22: Perplexity Dynamic Range by Generator Scale\",\n        \"columns\": [\n          \"generator\",\n          \"ppl_depth0\",\n          \"ppl_depth4\",\n          \"dynamic_range\",\n          \"ppl_ratio\"\n        ],\n        \"rows\": [\n          [\n            \"pythia-2.8b\",\n            13.5,\n            1.7,\n            11.8,\n            7.9\n          ],\n          [\n            \"pythia-1b\",\n            12.8,\n            2.1,\n            10.7,\n            6.1\n          ],\n          [\n            \"olmo-2-1b\",\n            11.4,\n            2.5,\n            8.9,\n            4.6\n          ],\n          [\n            \"qwen3-1.7b\",\n            10.8,\n            2.8,\n            8.0,\n            3.9\n          ],\n          [\n            \"qwen3-8b\",\n            8.2,\n            4.1,\n            4.1,\n            2.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale-dependent depth signal degradation is the strongest negative finding and the most publishable result in the worst tier. The log-linear F1-vs-scale relationship is novel empirical evidence connecting depth estimation to model collapse theory: \\\"larger models collapse slower (Gerstgrasser et al.), and correspondingly, depth signal degrades with scale.\\\" Note Pythia-2.8B is anomalously high due to same-family reference advantage — once corrected (using cross-family reference, plan_003), it would likely fall closer to the trend line. The perplexity dynamic range analysis (Table 22) provides a mechanistic explanation: reference-model perplexity has less room to drift when the generator is already fluent. In reframed paper, this becomes the central analytical contribution: \\\"Generation depth estimation exhibits a scale-dependent regime: distributional features that reliably detect depth for ≤3B generators fail at 7B+ scale, providing empirical evidence for scale-dependent convergence rates in recursive generation.\\\"\\n\\nThe 7B+ generator produces text that is much harder to depth-classify (F1=0.43, near chance for gen-1 and gen-2+). Several mechanisms explain this: (1) larger models have lower perplexity under any reference model, so the absolute perplexity at gen-0 is already closer to machine-generated (8.2 vs 13.5 for human text under Pythia-2.8B reference), reducing the dynamic range for drift detection (4.1 vs 11.8 points of perplexity range across depths); (2) larger models maintain more vocabulary diversity across recursive generations — TTR and hapax ratio drift less because the model's larger capacity preserves lexical variety; (3) the distributional shape of 7B+ outputs is more \\\"human-like\\\" at every depth, compressing the feature space. The F1-vs-generator-size correlation of -0.85 shows a clear scaling law: depth discriminability degrades roughly log-linearly with generator parameters. This connects directly to model collapse literature — larger models collapse slower, producing less distributional drift per recursive step. Gen-0 detection (human vs 7B-generated) is also harder (F1=0.62 vs ~0.90 for smaller generators) because 7B outputs are more human-like on all features.\\n\"\n  }\n]",
      "numLines": 1179,
      "startLine": 1,
      "totalLines": 1179
    }
  },
  "sourceToolAssistantUUID": "242f46b6-685a-46cd-82ca-fa781b5f0e7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerp…",
  "leafUuid": "0433f60a-742a-4959-834a-e6d6b3e13526",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth estimation in synthetic text analysis",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6"
}
```

---

### Assistant

_source line 16 · 2026-05-14T22:46:17.199Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and the paper framing. Let me check the output directory exists.

The narrative guidance tells me to:
1. Abandon dual dynamics as headline contribution
2. Reframe around: (1) Task formulation paper — generation depth estimation as a new task, (2) Negative/analytical result on depth signal scaling
3. Perplexity-by-depth monotonic decrease (13.5→1.7) as reference-model phenomenon
4. Paper becomes: new task + benchmark + scaling analysis + practical baseline

This is the "worst" tier, so the results are mostly negative. 

I need to present them honestly. Let me map out the paper structure around the task formulation and scaling analysis, organizing the experiments to build from basic validation through confound analysis to the key generator scale findings.

Now I'm thinking through how to group all these experiments into coherent narrative sections—the in-distribution baselines establish the task, the confound analyses validate the signal, cross-generator and cross-family work show generalization, and the scaling analysis becomes the centerpiece showing how depth degrades with larger models.

I should frame this around the core contribution: introducing Generation Depth Estimation as an ordinal task and demonstrating that the depth signal weakens as generator scale increases. I'm realizing there are too many subsections here—I should consolidate the related experiments to keep the paper streamlined while still covering all the key findings and tables. Let me start writing this out.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0433f60a-742a-4959-834a-e6d6b3e13526",
  "isSidechain": false,
  "requestId": "req_011Cb3GoJLZb17t8zyNFEbHm",
  "type": "assistant",
  "uuid": "054e19d6-dd7f-464c-a254-a0295979a014",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcpnKfs7bonNfHsSmeLrdb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 16648,
      "cache_read_input_tokens": 23077,
      "output_tokens": 1000,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2721,
          "output_tokens": 1000,
          "cache_read_input_tokens": 23077,
          "cache_creation_input_tokens": 16648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16648
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

_source line 17 · 2026-05-14T22:46:18.227Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015rRjoupZ45AaJfRdZEghzc`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/",
  "description": "Check output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "054e19d6-dd7f-464c-a254-a0295979a014",
  "isSidechain": false,
  "requestId": "req_011Cb3GoJLZb17t8zyNFEbHm",
  "type": "assistant",
  "uuid": "cbea98db-c58f-4b3a-b8ca-05105c31e437",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcpnKfs7bonNfHsSmeLrdb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 16648,
      "cache_read_input_tokens": 23077,
      "output_tokens": 1000,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2721,
          "output_tokens": 1000,
          "cache_read_input_tokens": 23077,
          "cache_creation_input_tokens": 16648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16648
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

_source line 18 · 2026-05-14T22:46:18.406Z_

<details><summary>↩ Tool result · `toolu_015rRjoupZ45AaJfRdZEghzc`</summary>

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
  "parentUuid": "cbea98db-c58f-4b3a-b8ca-05105c31e437",
  "isSidechain": false,
  "promptId": "64b0831c-d266-495e-8b02-943588d3f051",
  "type": "user",
  "uuid": "945aadf4-bf23-486a-9146-d629a2a823ed",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cbea98db-c58f-4b3a-b8ca-05105c31e437",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T22:46:21.862Z_

Now writing the full LaTeX paper. The paper reframes around: (1) task formulation — generation depth estimation as a missing layer in synthetic text analysis, (2) scaling analysis — depth signal degrades with generator scale, and (3) reference-model perplexity as a practical depth proxy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "945aadf4-bf23-486a-9146-d629a2a823ed",
  "isSidechain": false,
  "requestId": "req_011Cb3GpvKJcm2ftA9A3qcnq",
  "type": "assistant",
  "uuid": "b849d820-86c7-4505-b2bf-ad248c05a9b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011kihoEvDaBBGPKkz9srnR3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3749,
      "cache_read_input_tokens": 39725,
      "output_tokens": 14361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14361,
          "cache_read_input_tokens": 39725,
          "cache_creation_input_tokens": 3749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3749
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

_source line 20 · 2026-05-14T22:50:23.680Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Dxh57MqYKujBNT5kKsn1SF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\n\\title{Generation Depth Estimation: A Missing Layer in Synthetic Text Analysis}\n\n\\author{\n  Anonymous Authors\n}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\n% ============================================================\nWeb-scraped corpora increasingly contain LLM-generated text produced through recursive generation chains, where outputs of one model serve as inputs to the next generation step.\nCurrent detection methods provide only binary real-vs-synthetic classification, obscuring the \\emph{generation depth}---the number of recursive generation steps separating a text from its human-written seed.\nWe formalize \\textbf{generation depth estimation} as an ordinal classification task and establish baselines using distributional features computed under a held-out reference language model.\nOn in-distribution data (single generator, single domain), a feature-based classifier achieves macro-F1 of 0.82 for 3-class depth estimation (gen-0/gen-1/gen-2+), and reference-model perplexity exhibits a robust monotonic decrease across depths (13.5 $\\to$ 1.7).\nHowever, systematic evaluation across 12 experimental conditions reveals severe limitations: cross-generator generalization drops to F1~0.52, reference-model depth correlation is family-specific ($\\rho$=-0.68 same-family vs.\\ $\\rho$=-0.15 cross-family), and depth signal degrades with generator scale (F1 correlation with log-parameters: $r$=-0.85), with a 7B+ generator yielding near-chance performance (F1=0.43).\nWe identify text length as a major confound explaining 61--68\\% of surface feature depth correlation, and show that finer-grained (5-class) depth estimation is near chance (F1=0.28).\nThese results establish generation depth estimation as a well-defined but challenging task, identify reference-model perplexity as the most promising depth proxy, and provide evidence that depth signal exhibits scale-dependent degradation consistent with model collapse theory.\nWe release benchmark data and evaluation protocols to support future work.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n% ============================================================\n\nLarge language models are increasingly used in pipelines where one model's output becomes another's input---through automated content generation, data augmentation, or recursive summarization.\nWhen such text enters web-scraped training corpora, it introduces contamination of varying severity.\nA text generated directly from a human-written prompt (generation depth 1) may retain most properties of its human seed, while text at depth 4 or 5 has undergone compounding distributional drift through multiple recursive generation steps.\n\nCurrent synthetic text detection methods~\\citep{mitchell2023detectgpt,bao2024fastdetectgpt,hans2024binoculars} provide only binary real-vs-synthetic classification.\nThis forces a binary curation decision: discard all flagged content (losing potentially useful shallow-generation text) or retain everything (admitting deeply generated text with compounding quality degradation).\nA more nuanced approach would estimate the \\emph{generation depth} of each document, enabling risk-stratified data curation.\n\nIn this paper, we formalize \\textbf{generation depth estimation} as an ordinal classification task and conduct a comprehensive empirical study of its feasibility using distributional features.\nOur study spans 12 experimental conditions covering cross-generator generalization, reference model sensitivity, generator scale, prompt type variation, domain effects, ordinal granularity, edit robustness, and downstream utility.\n\nOur main findings are:\n\n\\begin{enumerate}\n\\item \\textbf{Task formulation}: We define generation depth estimation as a 3-class ordinal problem (gen-0/gen-1/gen-2+) and establish that this granularity represents a practical ceiling---5-class estimation is near chance (F1=0.28).\n\n\\item \\textbf{Reference-model perplexity as depth proxy}: Median perplexity under a same-family reference model decreases monotonically with depth (13.5 $\\to$ 1.7), providing a robust univariate depth signal. However, this signal is reference-model-specific: cross-family references yield weak correlations ($|\\rho|<0.3$).\n\n\\item \\textbf{Scale-dependent signal degradation}: Depth estimation F1 correlates strongly with generator scale ($r$=-0.85). For generators $\\leq$3B, 3-class F1 ranges 0.68--0.78; at 8B, F1 drops to 0.43. This connects empirically to model collapse theory: larger models collapse slower, producing less distributional drift per recursive step.\n\n\\item \\textbf{Comprehensive limitation analysis}: We document failure modes including cross-generator degradation (F1=0.52), length confounds (10-point F1 drop after control), prompt-type sensitivity, and fragility to post-generation editing.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n% ============================================================\n\n\\paragraph{Synthetic text detection.}\nBinary detection of machine-generated text has been approached through perplexity-based methods~\\citep{gehrmann2019gltr,mitchell2023detectgpt,bao2024fastdetectgpt,hans2024binoculars}, trained classifiers~\\citep{solaiman2019release,uchendu2020authorship}, watermarking~\\citep{kirchenbauer2023watermark}, and character-level distributional signatures (LD-Score)~\\citep{tulchinskii2024ldscore}.\nAll existing methods produce binary outputs; none attempt ordinal depth estimation.\n\n\\paragraph{Model collapse and recursive generation.}\nTheoretical and empirical work on model collapse~\\citep{alemohammad2024selfconsuming,shumailov2024curse,dohmatob2024model,gerstgrasser2024model} shows that recursive training on synthetic data leads to distributional convergence, with convergence rate inversely related to model capacity.\n\\citet{briesch2023attractor} prove that paraphrastic generation chains converge to 2-period attractor cycles, bounding useful depth signal to approximately 3 classes.\nWe extend this analysis empirically to non-paraphrastic chains.\n\n\\paragraph{Data quality and curation.}\nMethods for training data curation~\\citep{xie2023dsir,wettig2024qurating,wenzek2020ccnet} score documents along quality dimensions but do not account for generation provenance or depth.\nOur work introduces generation depth as a complementary quality signal.\n\n\\paragraph{Vocabulary diversity in LLM outputs.}\nStudies on vocabulary diversity in synthetic text~\\citep{guo2024curious,padmakumar2024does,holtzman2020curious} document diversity reduction in LLM outputs.\nWe connect these findings to recursive generation, showing that diversity metrics (TTR, hapax ratio) decrease with generation depth but are substantially confounded by text length.\n\n% ============================================================\n\\section{Task Definition}\n\\label{sec:task}\n% ============================================================\n\n\\paragraph{Generation depth.}\nGiven a text $x$, its \\emph{generation depth} $d(x) \\in \\{0, 1, 2, \\ldots\\}$ is defined as the number of LLM generation steps separating it from a human-written seed:\n\\begin{itemize}\n  \\item $d=0$: human-written text (the original seed).\n  \\item $d=1$: text generated by an LLM from a human-written prompt/seed.\n  \\item $d=k$: text produced by applying LLM generation $k$ times recursively.\n\\end{itemize}\n\n\\paragraph{Depth estimation task.}\nGiven a text $x$ with unknown provenance, predict $\\hat{d}(x) \\in \\{$gen-0, gen-1, gen-2+$\\}$.\nWe adopt 3-class ordinal grouping based on theoretical and empirical evidence that finer-grained estimation is infeasible with distributional features (Section~\\ref{sec:ordinal}).\n\n\\paragraph{Generation chain construction.}\nWe construct generation chains via iterative continuation: given seed text $s$, we produce $x^{(1)} = \\text{LLM}(s)$, $x^{(2)} = \\text{LLM}(x^{(1)})$, and so on up to depth 4.\nWe explore continuation, elaboration, and inspired-rewriting prompt types (Section~\\ref{sec:prompt_type}).\nChains may use a single generator (Section~\\ref{sec:indist}--\\ref{sec:scale}) or different generators per step (Section~\\ref{sec:cross_model}).\n\n\\paragraph{Evaluation protocol.}\nPrimary metric: macro-averaged F1 across the 3 depth classes.\nWe report 95\\% bootstrap confidence intervals and use leave-one-generator-out (LOGO) evaluation for cross-generator generalization.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n% ============================================================\n\n\\subsection{Distributional Features}\n\\label{sec:features}\n\nWe extract 7 features from each text, divided into two categories:\n\n\\paragraph{Surface features} computed directly from the text:\n\\begin{itemize}\n  \\item \\textbf{TTR}: Type-token ratio (unique tokens / total tokens).\n  \\item \\textbf{Hapax ratio}: Fraction of tokens appearing exactly once.\n\\end{itemize}\n\n\\paragraph{Reference-model features} computed by evaluating the text under a held-out reference language model $M_{\\text{ref}}$ (default: Pythia-410M), collecting per-token negative log-likelihoods $\\{-\\log p_{M_{\\text{ref}}}(t_i \\mid t_{&lt;i})\\}_{i=1}^{n}$:\n\\begin{itemize}\n  \\item \\textbf{entropy\\_mean}: Mean NLL (proxy for reference-model perplexity).\n  \\item \\textbf{entropy\\_std}: Standard deviation of per-token NLL.\n  \\item \\textbf{entropy\\_max}: Maximum per-token NLL.\n  \\item \\textbf{entropy\\_min}: Minimum per-token NLL.\n  \\item \\textbf{tail\\_decay}: Rate of exponential decay in the upper tail of the NLL distribution.\n\\end{itemize}\n\nThese features are standard NLL summary statistics; the novelty lies in applying them to ordinal depth estimation rather than binary detection.\n\n\\subsection{Classifier}\nWe train an XGBoost gradient-boosted tree classifier on the 7-dimensional feature vector.\nHyperparameters are selected via 5-fold cross-validation on training data.\nWe also evaluate a QLoRA-finetuned Qwen3.5-0.8B as an end-to-end baseline (Section~\\ref{sec:e2e}).\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n% ============================================================\n\nWe organize experiments around four research questions:\n\\textbf{RQ1}: Can distributional features estimate generation depth? (Sections~\\ref{sec:indist}--\\ref{sec:length})\n\\textbf{RQ2}: How does depth signal scale with generator capacity? (Section~\\ref{sec:scale})\n\\textbf{RQ3}: What are the generalization boundaries? (Sections~\\ref{sec:cross_gen}--\\ref{sec:cross_model})\n\\textbf{RQ4}: Is depth estimation useful for downstream curation? (Section~\\ref{sec:downstream})\n\n% --------------------------------------------------\n\\subsection{In-Distribution Baseline}\n\\label{sec:indist}\n\nWe first establish baseline performance using Pythia-2.8B as generator and Pythia-410M as reference model on Wikipedia-domain continuation chains.\n\n\\begin{table}[h]\n\\centering\n\\caption{Feature ablation on in-distribution data (Pythia-2.8B generator, Pythia-410M reference, Wikipedia continuation chains).}\n\\label{tab:ablation}\n\\begin{tabular}{lccccc}\n\\toprule\nFeature Set & Macro-F1 & 95\\% CI & Gen-0 & Gen-1 & Gen-2+ \\\\\n\\midrule\nFull (7 features) & 0.820 & [0.807, 0.834] & 0.952 & 0.776 & 0.795 \\\\\nSurface only & 0.763 & [0.747, 0.774] & 0.920 & 0.710 & 0.658 \\\\\nReference only & 0.719 & [0.706, 0.733] & 0.895 & 0.640 & 0.621 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn-distribution, the full feature set achieves macro-F1 of 0.820 (Table~\\ref{tab:ablation}).\nSurface features alone yield 0.763 and reference features alone 0.719, indicating complementary signal.\nMedian reference-model perplexity decreases monotonically across depths: 13.5 (gen-0), 4.96 (gen-1), 3.00 (gen-2), 2.07 (gen-3), 1.72 (gen-4).\n\nFeature-level analysis reveals two behavioral groups (Table~\\ref{tab:h1h2}).\nThree features show monotonic depth correlation ($R^2 > 0.8$): entropy\\_mean ($\\rho$=-0.68), TTR ($\\rho$=-0.31), and hapax\\_ratio ($\\rho$=-0.28).\nFour features show negligible depth correlation ($R^2 < 0.1$): entropy\\_std, entropy\\_max, entropy\\_min, and tail\\_decay.\nWe label these drifting (H2) and stationary (H1) groups respectively.\n\n\\begin{table}[h]\n\\centering\n\\caption{Feature classification by depth behavior. H2: monotonic depth drift. H1: near-stationary.}\n\\label{tab:h1h2}\n\\begin{tabular}{lcccc}\n\\toprule\nFeature & Source & Depth Slope & $R^2$ & Class \\\\\n\\midrule\nentropy\\_mean & reference & $-0.042$ & 0.91 & H2 (drift) \\\\\nTTR & surface & $-0.031$ & 0.87 & H2 (drift) \\\\\nhapax\\_ratio & surface & $-0.028$ & 0.83 & H2 (drift) \\\\\n\\midrule\nentropy\\_std & reference & $+0.003$ & 0.04 & H1 (stationary) \\\\\nentropy\\_max & reference & $-0.005$ & 0.07 & H1 (stationary) \\\\\nentropy\\_min & reference & $+0.002$ & 0.02 & H1 (stationary) \\\\\ntail\\_decay & reference & $+0.004$ & 0.05 & H1 (stationary) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHowever, as subsequent sections will show, these in-distribution results are misleadingly optimistic due to same-family reference model alignment, length confounds, and single-generator specificity.\n\n% --------------------------------------------------\n\\subsection{Text Length as Confound}\n\\label{sec:length}\n\nGenerated texts exhibit a length-depth correlation ($r$=0.42): deeper generations tend to be shorter.\nSince surface diversity metrics are mechanically length-dependent, this confound must be addressed.\n\n\\begin{table}[h]\n\\centering\n\\caption{Classification performance before and after length control.}\n\\label{tab:length}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Full F1 & Surface F1 & Reference F1 & Gap \\\\\n\\midrule\nOriginal & 0.78 & 0.76 & 0.72 & 0.02 \\\\\nLength-normalized features & 0.68 & 0.63 & 0.66 & 0.02 \\\\\nLength-matched subsampling & 0.70 & 0.65 & 0.67 & 0.03 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLength normalization reduces full-feature F1 from 0.78 to 0.68---a 10-point drop (Table~\\ref{tab:length}).\nThe impact is concentrated in surface features: TTR depth correlation drops from $\\rho$=-0.31 to $\\rho$=-0.12 (61\\% explained by length), and hapax ratio from $\\rho$=-0.28 to $\\rho$=-0.09 (68\\% explained by length) as shown in Table~\\ref{tab:length_features}.\nReference-model entropy\\_mean is less affected (19\\% explained by length, $\\rho$: $-0.68 \\to -0.55$), confirming it carries genuine depth signal beyond the length confound.\n\n\\begin{table}[h]\n\\centering\n\\caption{Feature depth correlation before and after length normalization.}\n\\label{tab:length_features}\n\\begin{tabular}{lccc}\n\\toprule\nFeature & Original $\\rho$ & Length-norm.\\ $\\rho$ & \\% Explained by Length \\\\\n\\midrule\nTTR & $-0.31$ & $-0.12$ & 61\\% \\\\\nhapax\\_ratio & $-0.28$ & $-0.09$ & 68\\% \\\\\nentropy\\_mean & $-0.68$ & $-0.55$ & 19\\% \\\\\nentropy\\_std & $+0.03$ & $+0.02$ & 33\\% \\\\\ntail\\_decay & $+0.04$ & $+0.03$ & 25\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAfter controlling for length, the advantage of the full feature set over surface-only features nearly vanishes (0.68 vs 0.63 = 0.05, down from 0.06), indicating that reference features' previous advantage was partly due to being less length-confounded rather than capturing fundamentally different depth information.\n\n% --------------------------------------------------\n\\subsection{Cross-Generator Generalization}\n\\label{sec:cross_gen}\n\nWe evaluate generalization using leave-one-generator-out (LOGO) across 5 generators from 3 model families: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, and Qwen3-0.6B.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-generator-out macro-F1. Mean across generators: 0.52.}\n\\label{tab:logo}\n\\begin{tabular}{llcccc}\n\\toprule\nHeld-Out Generator & Family & Macro-F1 & Gen-0 & Gen-1 & Gen-2+ \\\\\n\\midrule\nPythia-2.8B & Pythia & 0.61 & 0.82 & 0.51 & 0.50 \\\\\nPythia-1B & Pythia & 0.64 & 0.85 & 0.54 & 0.53 \\\\\nOLMo-2-1B & OLMo & 0.48 & 0.72 & 0.38 & 0.34 \\\\\nQwen3-1.7B & Qwen & 0.44 & 0.68 & 0.35 & 0.29 \\\\\nQwen3-0.6B & Qwen & 0.43 & 0.67 & 0.33 & 0.29 \\\\\n\\midrule\nMean (all) & --- & 0.52 & 0.75 & 0.42 & 0.39 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLOGO macro-F1 averages 0.52 (Table~\\ref{tab:logo}), substantially below the in-distribution 0.82.\nWithin-family generalization (Pythia $\\to$ Pythia) averages 0.625, while cross-family generalization (e.g., Pythia+Qwen $\\to$ OLMo) averages 0.45.\nGen-0 detection remains passable (mean 0.75) because human-written text is universally distinct, but gen-1 vs gen-2+ discrimination---the core depth signal---collapses across families.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-family-out evaluation.}\n\\label{tab:lofo}\n\\begin{tabular}{lcc}\n\\toprule\nHeld-Out Family & Train Generators & Macro-F1 \\\\\n\\midrule\nPythia & OLMo+Qwen & 0.41 \\\\\nOLMo & Pythia+Qwen & 0.54 \\\\\nQwen & Pythia+OLMo & 0.56 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLeave-one-family-out results (Table~\\ref{tab:lofo}) confirm family-level dependence: holding out Pythia (the family matching our reference model) drops F1 to 0.41, indicating the classifier critically relies on same-family reference model alignment.\n\n% --------------------------------------------------\n\\subsection{Reference Model Sensitivity}\n\\label{sec:ref_model}\n\nWe test whether the depth signal generalizes across reference models by computing features using OLMo-2-1B and Qwen3-0.6B in addition to the default Pythia-410M.\n\n\\begin{table}[h]\n\\centering\n\\caption{Entropy\\_mean depth correlation by reference model. The strong H2 drift observed with Pythia-410M is reference-family-specific.}\n\\label{tab:ref_corr}\n\\begin{tabular}{llccc}\n\\toprule\nReference Model & Family & entropy\\_mean $\\rho$ & $p$-value & H2 Status \\\\\n\\midrule\nPythia-410M & Pythia & $-0.68$ & $<$0.001 & Confirmed \\\\\nOLMo-2-1B & OLMo & $-0.22$ & 0.031 & Weak ($|\\rho|<0.3$) \\\\\nQwen3-0.6B & Qwen & $-0.15$ & 0.118 & Not confirmed \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe strong entropy\\_mean depth correlation ($\\rho$=-0.68) observed with the Pythia-410M reference largely disappears with non-Pythia references: $\\rho$=-0.22 (OLMo) and $\\rho$=-0.15 (Qwen, non-significant; Table~\\ref{tab:ref_corr}).\nThis occurs because the Pythia-410M reference shares architecture and training data with the Pythia generators, producing calibrated perplexity estimates that systematically track depth.\nCross-family references assign noisier, less calibrated perplexities.\n\n\\begin{table}[h]\n\\centering\n\\caption{Classification performance by reference model.}\n\\label{tab:ref_class}\n\\begin{tabular}{lcccc}\n\\toprule\nReference Model & Full F1 & Surface F1 & Ref-only F1 & Full--Surface Gap \\\\\n\\midrule\nPythia-410M & 0.82 & 0.76 & 0.72 & 0.06 \\\\\nOLMo-2-1B & 0.63 & 0.61 & 0.48 & 0.02 \\\\\nQwen3-0.6B & 0.58 & 0.57 & 0.41 & 0.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nClassification F1 drops sharply with cross-family references (Table~\\ref{tab:ref_class}): from 0.82 (Pythia) to 0.63 (OLMo) and 0.58 (Qwen).\nReference-only F1 drops to 0.48 and 0.41 respectively, while surface-only F1 remains stable at 0.57--0.61 (as expected, since surface features are reference-model-independent).\n\nExamining feature stability across references (Table~\\ref{tab:stability}), we find that distributional shape features (entropy\\_std, entropy\\_max, tail\\_decay) remain H1-stationary regardless of reference model---this is genuinely robust.\nHowever, the drifting features reduce to surface-only metrics (TTR, hapax), which Section~\\ref{sec:length} showed are largely length artifacts.\n\n\\begin{table}[h]\n\\centering\n\\caption{Feature behavioral classification stability across reference models.}\n\\label{tab:stability}\n\\begin{tabular}{lcccc}\n\\toprule\nFeature & Pythia Class & OLMo Class & Qwen Class & Stable? \\\\\n\\midrule\nentropy\\_mean & H2 & weak/NS & NS & No \\\\\nentropy\\_std & H1 & H1 & H1 & Yes \\\\\nentropy\\_max & H1 & H1 & H1 & Yes \\\\\ntail\\_decay & H1 & H1 & H1 & Yes \\\\\nTTR & H2 & H2 & H2 & Yes \\\\\nhapax\\_ratio & H2 & H2 & weak H2 & Marginal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% --------------------------------------------------\n\\subsection{Generator Scale Analysis}\n\\label{sec:scale}\n\nWe evaluate depth estimation across generator scales from 0.6B to 8B parameters (Table~\\ref{tab:scale}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth classification by generator scale. Depth signal degrades with model capacity ($r$=-0.85 between log-params and F1).}\n\\label{tab:scale}\n\\begin{tabular}{lcccccc}\n\\toprule\nGenerator & Params & F1 & Gen-0 & Gen-1 & Gen-2+ & $\\rho_{\\text{ent}}$ \\\\\n\\midrule\nQwen3-0.6B & 0.6B & 0.74 & 0.91 & 0.66 & 0.65 & $-0.58$ \\\\\nPythia-1B & 1B & 0.71 & 0.89 & 0.62 & 0.62 & $-0.55$ \\\\\nOLMo-2-1B & 1.5B & 0.69 & 0.87 & 0.60 & 0.60 & $-0.51$ \\\\\nQwen3-1.7B & 1.7B & 0.68 & 0.86 & 0.58 & 0.60 & $-0.48$ \\\\\nPythia-2.8B & 2.8B & 0.78 & 0.93 & 0.72 & 0.69 & $-0.68$ \\\\\nQwen3-8B & 8B & 0.43 & 0.62 & 0.35 & 0.32 & $-0.19$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 8B generator yields near-chance depth estimation (F1=0.43) with severely degraded gen-1 and gen-2+ discrimination (0.35 and 0.32).\nThe correlation between log-parameters and macro-F1 is $r$=-0.85 (excluding the Pythia-2.8B outlier, which benefits from same-family reference alignment).\n\nThe mechanism is revealed by perplexity dynamic range analysis (Table~\\ref{tab:ppl_range}): the reference model's ability to distinguish depths relies on perplexity separation between depths, which compresses as generator fluency increases.\nFor Pythia-2.8B, perplexity ranges from 13.5 (gen-0) to 1.7 (gen-4), a dynamic range of 11.8.\nFor Qwen3-8B, this compresses to 8.2--4.1, a dynamic range of only 4.1---the larger model produces text that is already close to the reference model's expectations at every depth.\n\n\\begin{table}[h]\n\\centering\n\\caption{Reference-model perplexity dynamic range by generator scale. Larger generators compress the perplexity range available for depth discrimination.}\n\\label{tab:ppl_range}\n\\begin{tabular}{lcccc}\n\\toprule\nGenerator & PPL (depth-0) & PPL (depth-4) & Dynamic Range & PPL Ratio \\\\\n\\midrule\nPythia-2.8B & 13.5 & 1.7 & 11.8 & 7.9$\\times$ \\\\\nPythia-1B & 12.8 & 2.1 & 10.7 & 6.1$\\times$ \\\\\nOLMo-2-1B & 11.4 & 2.5 & 8.9 & 4.6$\\times$ \\\\\nQwen3-1.7B & 10.8 & 2.8 & 8.0 & 3.9$\\times$ \\\\\nQwen3-8B & 8.2 & 4.1 & 4.1 & 2.0$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis result connects to model collapse theory~\\citep{gerstgrasser2024model}: larger models collapse slower under recursive generation, producing less distributional drift per step.\nConsequently, depth estimation with distributional features faces a fundamental scaling barrier---the models most likely to produce recursive content in practice (large, capable models) are precisely those for which depth signal is weakest.\n\n% --------------------------------------------------\n\\subsection{Prompt Type and Chain Structure}\n\\label{sec:prompt_type}\n\nWe evaluate three prompt types: continuation (direct text continuation), elaboration (topic expansion), and inspired rewriting (semantic departure from source).\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth classification by prompt type.}\n\\label{tab:prompt}\n\\begin{tabular}{lcccc}\n\\toprule\nPrompt Type & Macro-F1 & $\\rho_{\\text{ent}}$ & $\\rho_{\\text{TTR}}$ & Gen-1 vs Gen-2+ F1 \\\\\n\\midrule\nContinuation & 0.78 & $-0.65$ & $-0.29$ & 0.71 \\\\\nElaboration & 0.55 & $-0.38$ & $-0.16$ & 0.44 \\\\\nInspired rewriting & 0.47 & $-0.18$ & $-0.08$ & 0.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDepth signal varies dramatically with prompt type (Table~\\ref{tab:prompt}).\nContinuation chains preserve the strongest signal (F1=0.78) because each step builds directly on the previous output, creating cumulative distributional drift.\nElaboration reduces this to F1=0.55, and inspired rewriting yields near-chance F1=0.47 because the semantic departure partially resets distributional state at each step.\n\nCross-prompt transfer is poor: training on one prompt type and testing on another yields average F1=0.42 (Table~\\ref{tab:prompt_transfer}), indicating that depth features are prompt-type-specific.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-prompt type transfer (train $\\to$ test).}\n\\label{tab:prompt_transfer}\n\\begin{tabular}{lccc}\n\\toprule\nTrain $\\to$ Test & Elaboration & Rewriting & Continuation \\\\\n\\midrule\nContinuation $\\to$ & 0.46 & 0.39 & --- \\\\\nElaboration $\\to$ & --- & 0.42 & 0.51 \\\\\nRewriting $\\to$ & 0.40 & --- & 0.44 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Paraphrastic vs.\\ non-paraphrastic chains.}\nComparing paraphrastic and continuation chains (Table~\\ref{tab:para}) confirms attractor theory predictions: paraphrastic chains converge by depth 2 (gen-2 vs gen-3 F1=0.34), while continuation chains preserve signal slightly longer but also saturate by depth 3.\n\n\\begin{table}[h]\n\\centering\n\\caption{Paraphrastic vs.\\ continuation chain depth discrimination.}\n\\label{tab:para}\n\\begin{tabular}{lcccccc}\n\\toprule\nChain Type & 3-class F1 & Gen-0 & Gen-1 & Gen-2+ & $\\rho_{\\text{ent}}$ \\\\\n\\midrule\nParaphrastic & 0.52 & 0.78 & 0.45 & 0.33 & $-0.31$ \\\\\nContinuation & 0.78 & 0.93 & 0.72 & 0.69 & $-0.65$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% --------------------------------------------------\n\\subsection{Cross-Model Chains}\n\\label{sec:cross_model}\n\nReal-world contamination may involve different generators at each depth step.\nWe evaluate cross-model chains where the generator changes randomly at each step (Table~\\ref{tab:crossmodel}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Single-model vs.\\ cross-model chain depth estimation.}\n\\label{tab:crossmodel}\n\\begin{tabular}{lcccc}\n\\toprule\nChain Type & Macro-F1 & Gen-0 & Gen-1 & Gen-2+ \\\\\n\\midrule\nSingle model & 0.78 & 0.93 & 0.72 & 0.69 \\\\\nCross-model (random) & 0.39 & 0.65 & 0.28 & 0.24 \\\\\nCross-model (increasing size) & 0.41 & 0.66 & 0.30 & 0.27 \\\\\nCross-model (decreasing size) & 0.38 & 0.63 & 0.27 & 0.24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-model chains destroy depth signal (F1=0.39), with gen-1 and gen-2+ near chance (0.28 and 0.24).\nGenerator identity is a much stronger signal than depth: a gen-1 text from Qwen differs more from gen-1 text from Pythia than gen-1 differs from gen-2 within the same generator.\nThis represents the most ecologically challenging result, as real web contamination involves diverse generators.\n\n% --------------------------------------------------\n\\subsection{Multi-Domain Evaluation}\n\\label{sec:domain}\n\nWe expand to 4 domains with 500 seeds each (Table~\\ref{tab:domain}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth classification by source domain.}\n\\label{tab:domain}\n\\begin{tabular}{lccccc}\n\\toprule\nDomain & $n$ Seeds & Macro-F1 & Gen-0 & Gen-1 & Gen-2+ \\\\\n\\midrule\nWikipedia & 500 & 0.72 & 0.89 & 0.63 & 0.64 \\\\\nNews & 500 & 0.68 & 0.86 & 0.59 & 0.59 \\\\\nScientific & 500 & 0.55 & 0.78 & 0.44 & 0.43 \\\\\nCreative & 500 & 0.48 & 0.71 & 0.37 & 0.36 \\\\\n\\midrule\nAll pooled & 2000 & 0.61 & 0.81 & 0.51 & 0.51 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDomain substantially moderates depth signal ($\\sigma_{F1}$=0.11).\nFactual domains (Wikipedia, news) show passable performance, while creative writing yields near-chance F1=0.48.\nCross-domain transfer averages F1=0.49, adding domain to the list of moderating factors (alongside prompt type and generator family) that limit generalizability.\n\n% --------------------------------------------------\n\\subsection{Ordinal Granularity}\n\\label{sec:ordinal}\n\nWe test 5-class ordinal classification (gen-0 through gen-4) to establish the granularity ceiling (Table~\\ref{tab:ordinal}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Five-class ordinal depth classification.}\n\\label{tab:ordinal}\n\\begin{tabular}{lcccc}\n\\toprule\nClass & Precision & Recall & F1 & $n$ \\\\\n\\midrule\nGen-0 & 0.88 & 0.82 & 0.85 & 995 \\\\\nGen-1 & 0.39 & 0.45 & 0.42 & 993 \\\\\nGen-2 & 0.16 & 0.20 & 0.18 & 912 \\\\\nGen-3 & 0.11 & 0.13 & 0.12 & 856 \\\\\nGen-4 & 0.10 & 0.12 & 0.11 & 816 \\\\\n\\midrule\n\\multicolumn{3}{l}{5-class macro-F1: 0.28} & \\multicolumn{2}{l}{MAE: 1.4} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFive-class macro-F1 of 0.28 is barely above chance (0.20).\nGen-2/3/4 collapse into an indistinguishable cluster (F1: 0.18/0.12/0.11), with 72\\% of misclassifications between adjacent classes.\nThis validates the 3-class design: ordinal depth beyond gen-0/gen-1/gen-2+ is not discriminable with distributional features, consistent with attractor convergence theory extended to non-paraphrastic generation.\n\n% --------------------------------------------------\n\\subsection{Robustness to Human Editing}\n\\label{sec:robustness}\n\n\\begin{table}[h]\n\\centering\n\\caption{Robustness to simulated post-generation editing.}\n\\label{tab:edits}\n\\begin{tabular}{lccc}\n\\toprule\nEdit Type & Edit Rate & Macro-F1 & $\\Delta$F1 \\\\\n\\midrule\nNone & 0\\% & 0.78 & --- \\\\\nRandom replace & 5\\% & 0.68 & $-0.10$ \\\\\nRandom replace & 10\\% & 0.58 & $-0.20$ \\\\\nRandom replace & 20\\% & 0.44 & $-0.34$ \\\\\nLLM light edit & $\\sim$8\\% & 0.53 & $-0.25$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDepth features are fragile to post-generation modification (Table~\\ref{tab:edits}).\nEven 5\\% random word replacement reduces F1 by 0.10, and LLM-simulated editing reduces F1 by 0.25.\nLLM editing is more damaging than random replacement because it systematically smooths the distributional artifacts that depth estimation relies on.\nThis limits practical applicability to detection of fully automated, unedited generation chains.\n\n% --------------------------------------------------\n\\subsection{Additional Features and End-to-End Baseline}\n\\label{sec:e2e}\n\n\\paragraph{LD-Score as depth feature.}\nAdding LD-Score~\\citep{tulchinskii2024ldscore} (a character-level distributional signature) provides negligible improvement: depth correlation $\\rho$=-0.25, F1 increase from 0.780 to 0.785.\nLD-Score shows weak depth sensitivity but insufficient signal to meaningfully contribute beyond existing features.\n\n\\begin{table}[h]\n\\centering\n\\caption{Handcrafted features vs.\\ end-to-end fine-tuned classifier.}\n\\label{tab:e2e}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & In-Dist.\\ F1 & Cross-Gen LOGO F1 & GPU Hours \\\\\n\\midrule\nHandcrafted + XGBoost & 0.78 & 0.52 & 0.1 \\\\\nQwen3.5-0.8B QLoRA & 0.83 & 0.55 & 15 \\\\\nQwen3.5-0.8B (frozen) & 0.80 & 0.53 & 8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{End-to-end classifier.}\nA QLoRA-finetuned Qwen3.5-0.8B achieves F1=0.83 in-distribution, slightly above the handcrafted 0.78 (Table~\\ref{tab:e2e}).\nHowever, it shares the same cross-generator failure (LOGO F1=0.55 vs.\\ 0.52), suggesting that the generalization barrier is fundamental to the depth estimation task, not an artifact of our feature engineering.\n\n% --------------------------------------------------\n\\subsection{Downstream Utility}\n\\label{sec:downstream}\n\nWe fine-tune OLMo-1B on depth-stratified data (5 seeds, bootstrap CIs) to test whether depth-aware filtering improves downstream model quality compared to binary filtering (Table~\\ref{tab:downstream}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Downstream fine-tuning results (OLMo-1B, 5 seeds).}\n\\label{tab:downstream}\n\\begin{tabular}{lcccc}\n\\toprule\nFiltering Strategy & Mean PPL & Std & 95\\% CI & Improvement \\\\\n\\midrule\nUnfiltered & 14.8 & 0.42 & [14.2, 15.4] & --- \\\\\nBinary (FastDetectGPT) & 14.5 & 0.51 & [13.8, 15.2] & 1.2\\% [$-$1.1, 3.5] \\\\\nBinary (LD-Score) & 14.6 & 0.48 & [14.0, 15.2] & 0.9\\% [$-$1.4, 3.2] \\\\\nDepth-aware (keep gen-0/1) & 14.2 & 0.39 & [13.7, 14.7] & 1.8\\% [$-$0.5, 4.1] \\\\\nDepth-aware (sample-matched) & 14.2 & 0.44 & [13.6, 14.8] & 1.5\\% [$-$0.8, 3.8] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDepth-aware filtering shows a directional advantage (1.8\\% vs.\\ 1.2\\% improvement over unfiltered) but confidence intervals overlap substantially (depth vs.\\ binary $p$=0.31).\nThe improvement is not statistically significant at this sample size.\n\nPredicted depth does correlate weakly with quality degradation ($\\rho$=0.28, 95\\% CI [0.11, 0.45]).\nPerplexity increases monotonically with depth: 12.1 (gen-0) $\\to$ 13.4 (gen-1) $\\to$ 14.1 (gen-2) $\\to$ 14.5 (gen-3) $\\to$ 14.9 (gen-4), confirming that deeper generation produces lower-quality training data.\nHowever, this descriptive finding does not translate into significant downstream filtering advantage with current methods.\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n% ============================================================\n\n\\paragraph{The task is well-defined but harder than expected.}\nGeneration depth estimation is conceptually sound: depth correlates with quality degradation, and ordinal estimation enables more nuanced curation than binary detection.\nHowever, our comprehensive evaluation reveals that current distributional features fall short of reliable depth estimation under realistic conditions.\nThe 3-class problem is feasible in controlled settings (single generator, single domain, continuation chains) but degrades along every generalization axis we tested.\n\n\\paragraph{Reference-model perplexity: strong but specific.}\nThe monotonic perplexity decrease across depths (13.5 $\\to$ 1.7) is the most robust univariate depth signal.\nHowever, this signal depends critically on reference-generator family alignment ($\\rho$=-0.68 same-family vs.\\ $\\rho$=-0.15 cross-family).\nThis aligns with an interpretation based on distributional calibration: a same-family reference model has calibrated predictions for the generator's output distribution, making perplexity sensitive to the subtle distributional shifts across depths.\nA cross-family reference assigns noisier perplexities that wash out the depth signal.\n\n\\paragraph{Scale-dependent depth estimation.}\nThe strong negative correlation between generator scale and depth discriminability ($r$=-0.85) is our most concerning finding for practical deployment.\nLarger models produce more fluent text with smaller distributional drift per recursive step, compressing the perplexity dynamic range available for depth discrimination (11.8 for 2.8B vs.\\ 4.1 for 8B).\nThis connects to theoretical results on scale-dependent collapse rates~\\citep{gerstgrasser2024model}: if larger models converge slower, then depth-correlated distributional drift is correspondingly smaller at each step.\nAs the most capable models are also those most likely to be used in recursive generation pipelines, this scaling barrier is a fundamental challenge.\n\n\\paragraph{Confounds and moderators.}\nWe identify text length, prompt type, generator family, source domain, and post-generation editing as significant moderators.\nThe length confound is particularly concerning: 61--68\\% of surface feature depth correlation is attributable to length variation.\nAfter controlling for these confounds, the residual depth signal, while real, is substantially weaker than in-distribution baselines suggest.\n\n\\paragraph{Limitations.}\nOur study is limited to open-weight models $\\leq$8B parameters; frontier models (70B+) may exhibit even weaker depth signal.\nThe benchmark uses constructed chains rather than naturally occurring recursive generation, which may differ in distribution.\nAll reference models used are autoregressive transformers; alternative architectures may provide complementary signals.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n% ============================================================\n\nWe formalize generation depth estimation as a new task in synthetic text analysis and provide a comprehensive benchmark spanning 12 experimental conditions.\nOur study identifies three key findings: (1)~three-class depth estimation (gen-0/gen-1/gen-2+) represents the practical granularity ceiling; (2)~reference-model perplexity is the strongest depth proxy but requires generator-family-aligned reference models; and (3)~depth signal exhibits scale-dependent degradation, with 8B generators already yielding near-chance estimation.\nThese results position generation depth estimation as a meaningful but challenging open problem, and the scale-dependent signal degradation connects empirically to model collapse theory.\nWe release our benchmark dataset and evaluation protocols to support future work on generator-invariant depth features that may overcome the limitations documented here.\n\n% ============================================================\n% References\n% ============================================================\n\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Alemohammad et~al.(2024)]{alemohammad2024selfconsuming}\nS.~Alemohammad, J.~Casco-Rodriguez, L.~Luber, A.~G. Humair, S.~Babaei, D.~LeJeune, A.~Sivaraman, and R.~G. Baraniuk.\n\\newblock Self-consuming generative models go {MAD}.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Bao et~al.(2024)]{bao2024fastdetectgpt}\nG.~Bao, Y.~Zhao, Z.~Teng, L.~Yang, and Y.~Zhang.\n\\newblock {Fast-DetectGPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Briesch et~al.(2023)]{briesch2023attractor}\nM.~Briesch, D.~Sobania, and F.~Rothlauf.\n\\newblock Large language models suffer from their own output: An analysis of the self-consuming training loop.\n\\newblock \\emph{arXiv preprint arXiv:2311.16822}, 2023.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024model}\nE.~Dohmatob, P.~Feng, Q.~Yang, F.~Charton, and J.~Kempe.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Gehrmann et~al.(2019)]{gehrmann2019gltr}\nS.~Gehrmann, H.~Strobelt, and A.~M. Rush.\n\\newblock {GLTR}: Statistical detection and visualization of generated text.\n\\newblock In \\emph{ACL}, 2019.\n\n\\bibitem[Gerstgrasser et~al.(2024)]{gerstgrasser2024model}\nM.~Gerstgrasser, R.~Schaeffer, A.~Dey, R.~Rafailov, H.~Tombai, Y.~Nishi, S.~Levine, and K.~Koyejo.\n\\newblock Is model collapse inevitable? {Breaking} the curse of recursion by accumulating real and synthetic data.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Guo et~al.(2024)]{guo2024curious}\nB.~Guo, X.~Zhang, Z.~Wang, M.~Jiang, J.~Nie, Y.~Ding, J.~Yue, and Y.~Wu.\n\\newblock How close is {ChatGPT} to human experts? {Comparison} corpus, evaluation, and detection.\n\\newblock \\emph{arXiv preprint arXiv:2301.07597}, 2024.\n\n\\bibitem[Hans et~al.(2024)]{hans2024binoculars}\nA.~Hans, A.~Schwarzschild, V.~Cherepanova, H.~Kazemi, A.~Saha, M.~Goldblum, J.~Geiping, and T.~Goldstein.\n\\newblock Spotting {LLMs} with {Binoculars}: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Hendrycks and Gimpel(2017)]{hendrycks2017baseline}\nD.~Hendrycks and K.~Gimpel.\n\\newblock A baseline for detecting misclassified and out-of-distribution examples in neural networks.\n\\newblock In \\emph{ICLR}, 2017.\n\n\\bibitem[Holtzman et~al.(2020)]{holtzman2020curious}\nA.~Holtzman, J.~Buys, L.~Du, M.~Forbes, and Y.~Choi.\n\\newblock The curious case of neural text degeneration.\n\\newblock In \\emph{ICLR}, 2020.\n\n\\bibitem[Kirchenbauer et~al.(2023)]{kirchenbauer2023watermark}\nJ.~Kirchenbauer, J.~Geiping, Y.~Wen, J.~Katz, I.~Miers, and T.~Goldstein.\n\\newblock A watermark for large language models.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nE.~Mitchell, Y.~Lee, A.~Khazatsky, C.~D. Manning, and C.~Finn.\n\\newblock {DetectGPT}: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Padmakumar and He(2024)]{padmakumar2024does}\nV.~Padmakumar and H.~He.\n\\newblock Does writing with language models reduce content diversity?\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024curse}\nI.~Shumailov, Z.~Shumaylov, Y.~Zhao, N.~Papernot, R.~Anderson, and Y.~Gal.\n\\newblock The curse of recursion: Training on generated data makes models forget.\n\\newblock \\emph{Nature}, 2024.\n\n\\bibitem[Solaiman et~al.(2019)]{solaiman2019release}\nI.~Solaiman, M.~Brundage, J.~Clark, A.~Askell, A.~Herbert-Voss, J.~Wu, A.~Radford, G.~Krueger, J.~W. Kim, S.~Kreps, et~al.\n\\newblock Release strategies and the social impacts of language models.\n\\newblock \\emph{arXiv preprint arXiv:1908.09203}, 2019.\n\n\\bibitem[Tulchinskii et~al.(2024)]{tulchinskii2024ldscore}\nE.~Tulchinskii, K.~Kuznetsov, L.~Kushnareva, D.~Cherniavskii, S.~Nikolenko, E.~Burnaev, S.~Barannikov, and I.~Piontkovskaya.\n\\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Uchendu et~al.(2020)]{uchendu2020authorship}\nA.~Uchendu, T.~Le, K.~Shu, and D.~Lee.\n\\newblock Authorship attribution for neural text generation.\n\\newblock In \\emph{EMNLP}, 2020.\n\n\\bibitem[Wenzek et~al.(2020)]{wenzek2020ccnet}\nG.~Wenzek, M.-A. Lachaux, A.~Conneau, V.~Chaudhary, F.~Guzm{\\'a}n, A.~Joulin, and E.~Grave.\n\\newblock {CCNet}: Extracting high quality monolingual datasets from web crawl data.\n\\newblock In \\emph{LREC}, 2020.\n\n\\bibitem[Wettig et~al.(2024)]{wettig2024qurating}\nA.~Wettig, A.~Gao, Z.~Zhong, and D.~Chen.\n\\newblock {QuRating}: Selecting high-quality data for training language models.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Xie et~al.(2023)]{xie2023dsir}\nS.~M. Xie, S.~Santurkar, T.~Ma, and P.~Liang.\n\\newblock Data selection for language models via importance resampling.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b849d820-86c7-4505-b2bf-ad248c05a9b0",
  "isSidechain": false,
  "requestId": "req_011Cb3GpvKJcm2ftA9A3qcnq",
  "type": "assistant",
  "uuid": "ecea2c85-a946-4d5e-bba7-4acc9fee26d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011kihoEvDaBBGPKkz9srnR3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3749,
      "cache_read_input_tokens": 39725,
      "output_tokens": 14361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14361,
          "cache_read_input_tokens": 39725,
          "cache_creation_input_tokens": 3749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3749
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

_source line 21 · 2026-05-14T22:50:23.702Z_

<details><summary>↩ Tool result · `toolu_01Dxh57MqYKujBNT5kKsn1SF`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecea2c85-a946-4d5e-bba7-4acc9fee26d6",
  "isSidechain": false,
  "promptId": "64b0831c-d266-495e-8b02-943588d3f051",
  "type": "user",
  "uuid": "bdd4674b-6b31-4917-a4cb-940ca68243ec",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\n\\title{Generation Depth Estimation: A Missing Layer in Synthetic Text Analysis}\n\n\\author{\n  Anonymous Authors\n}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\n% ============================================================\nWeb-scraped corpora increasingly contain LLM-generated text produced through recursive generation chains, where outputs of one model serve as inputs to the next generation step.\nCurrent detection methods provide only binary real-vs-synthetic classification, obscuring the \\emph{generation depth}---the number of recursive generation steps separating a text from its human-written seed.\nWe formalize \\textbf{generation depth estimation} as an ordinal classification task and establish baselines using distributional features computed under a held-out reference language model.\nOn in-distribution data (single generator, single domain), a feature-based classifier achieves macro-F1 of 0.82 for 3-class depth estimation (gen-0/gen-1/gen-2+), and reference-model perplexity exhibits a robust monotonic decrease across depths (13.5 $\\to$ 1.7).\nHowever, systematic evaluation across 12 experimental conditions reveals severe limitations: cross-generator generalization drops to F1~0.52, reference-model depth correlation is family-specific ($\\rho$=-0.68 same-family vs.\\ $\\rho$=-0.15 cross-family), and depth signal degrades with generator scale (F1 correlation with log-parameters: $r$=-0.85), with a 7B+ generator yielding near-chance performance (F1=0.43).\nWe identify text length as a major confound explaining 61--68\\% of surface feature depth correlation, and show that finer-grained (5-class) depth estimation is near chance (F1=0.28).\nThese results establish generation depth estimation as a well-defined but challenging task, identify reference-model perplexity as the most promising depth proxy, and provide evidence that depth signal exhibits scale-dependent degradation consistent with model collapse theory.\nWe release benchmark data and evaluation protocols to support future work.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n% ============================================================\n\nLarge language models are increasingly used in pipelines where one model's output becomes another's input---through automated content generation, data augmentation, or recursive summarization.\nWhen such text enters web-scraped training corpora, it introduces contamination of varying severity.\nA text generated directly from a human-written prompt (generation depth 1) may retain most properties of its human seed, while text at depth 4 or 5 has undergone compounding distributional drift through multiple recursive generation steps.\n\nCurrent synthetic text detection methods~\\citep{mitchell2023detectgpt,bao2024fastdetectgpt,hans2024binoculars} provide only binary real-vs-synthetic classification.\nThis forces a binary curation decision: discard all flagged content (losing potentially useful shallow-generation text) or retain everything (admitting deeply generated text with compounding quality degradation).\nA more nuanced approach would estimate the \\emph{generation depth} of each document, enabling risk-stratified data curation.\n\nIn this paper, we formalize \\textbf{generation depth estimation} as an ordinal classification task and conduct a comprehensive empirical study of its feasibility using distributional features.\nOur study spans 12 experimental conditions covering cross-generator generalization, reference model sensitivity, generator scale, prompt type variation, domain effects, ordinal granularity, edit robustness, and downstream utility.\n\nOur main findings are:\n\n\\begin{enumerate}\n\\item \\textbf{Task formulation}: We define generation depth estimation as a 3-class ordinal problem (gen-0/gen-1/gen-2+) and establish that this granularity represents a practical ceiling---5-class estimation is near chance (F1=0.28).\n\n\\item \\textbf{Reference-model perplexity as depth proxy}: Median perplexity under a same-family reference model decreases monotonically with depth (13.5 $\\to$ 1.7), providing a robust univariate depth signal. However, this signal is reference-model-specific: cross-family references yield weak correlations ($|\\rho|<0.3$).\n\n\\item \\textbf{Scale-dependent signal degradation}: Depth estimation F1 correlates strongly with generator scale ($r$=-0.85). For generators $\\leq$3B, 3-class F1 ranges 0.68--0.78; at 8B, F1 drops to 0.43. This connects empirically to model collapse theory: larger models collapse slower, producing less distributional drift per recursive step.\n\n\\item \\textbf{Comprehensive limitation analysis}: We document failure modes including cross-generator degradation (F1=0.52), length confounds (10-point F1 drop after control), prompt-type sensitivity, and fragility to post-generation editing.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n% ============================================================\n\n\\paragraph{Synthetic text detection.}\nBinary detection of machine-generated text has been approached through perplexity-based methods~\\citep{gehrmann2019gltr,mitchell2023detectgpt,bao2024fastdetectgpt,hans2024binoculars}, trained classifiers~\\citep{solaiman2019release,uchendu2020authorship}, watermarking~\\citep{kirchenbauer2023watermark}, and character-level distributional signatures (LD-Score)~\\citep{tulchinskii2024ldscore}.\nAll existing methods produce binary outputs; none attempt ordinal depth estimation.\n\n\\paragraph{Model collapse and recursive generation.}\nTheoretical and empirical work on model collapse~\\citep{alemohammad2024selfconsuming,shumailov2024curse,dohmatob2024model,gerstgrasser2024model} shows that recursive training on synthetic data leads to distributional convergence, with convergence rate inversely related to model capacity.\n\\citet{briesch2023attractor} prove that paraphrastic generation chains converge to 2-period attractor cycles, bounding useful depth signal to approximately 3 classes.\nWe extend this analysis empirically to non-paraphrastic chains.\n\n\\paragraph{Data quality and curation.}\nMethods for training data curation~\\citep{xie2023dsir,wettig2024qurating,wenzek2020ccnet} score documents along quality dimensions but do not account for generation provenance or depth.\nOur work introduces generation depth as a complementary quality signal.\n\n\\paragraph{Vocabulary diversity in LLM outputs.}\nStudies on vocabulary diversity in synthetic text~\\citep{guo2024curious,padmakumar2024does,holtzman2020curious} document diversity reduction in LLM outputs.\nWe connect these findings to recursive generation, showing that diversity metrics (TTR, hapax ratio) decrease with generation depth but are substantially confounded by text length.\n\n% ============================================================\n\\section{Task Definition}\n\\label{sec:task}\n% ============================================================\n\n\\paragraph{Generation depth.}\nGiven a text $x$, its \\emph{generation depth} $d(x) \\in \\{0, 1, 2, \\ldots\\}$ is defined as the number of LLM generation steps separating it from a human-written seed:\n\\begin{itemize}\n  \\item $d=0$: human-written text (the original seed).\n  \\item $d=1$: text generated by an LLM from a human-written prompt/seed.\n  \\item $d=k$: text produced by applying LLM generation $k$ times recursively.\n\\end{itemize}\n\n\\paragraph{Depth estimation task.}\nGiven a text $x$ with unknown provenance, predict $\\hat{d}(x) \\in \\{$gen-0, gen-1, gen-2+$\\}$.\nWe adopt 3-class ordinal grouping based on theoretical and empirical evidence that finer-grained estimation is infeasible with distributional features (Section~\\ref{sec:ordinal}).\n\n\\paragraph{Generation chain construction.}\nWe construct generation chains via iterative continuation: given seed text $s$, we produce $x^{(1)} = \\text{LLM}(s)$, $x^{(2)} = \\text{LLM}(x^{(1)})$, and so on up to depth 4.\nWe explore continuation, elaboration, and inspired-rewriting prompt types (Section~\\ref{sec:prompt_type}).\nChains may use a single generator (Section~\\ref{sec:indist}--\\ref{sec:scale}) or different generators per step (Section~\\ref{sec:cross_model}).\n\n\\paragraph{Evaluation protocol.}\nPrimary metric: macro-averaged F1 across the 3 depth classes.\nWe report 95\\% bootstrap confidence intervals and use leave-one-generator-out (LOGO) evaluation for cross-generator generalization.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n% ============================================================\n\n\\subsection{Distributional Features}\n\\label{sec:features}\n\nWe extract 7 features from each text, divided into two categories:\n\n\\paragraph{Surface features} computed directly from the text:\n\\begin{itemize}\n  \\item \\textbf{TTR}: Type-token ratio (unique tokens / total tokens).\n  \\item \\textbf{Hapax ratio}: Fraction of tokens appearing exactly once.\n\\end{itemize}\n\n\\paragraph{Reference-model features} computed by evaluating the text under a held-out reference language model $M_{\\text{ref}}$ (default: Pythia-410M), collecting per-token negative log-likelihoods $\\{-\\log p_{M_{\\text{ref}}}(t_i \\mid t_{&lt;i})\\}_{i=1}^{n}$:\n\\begin{itemize}\n  \\item \\textbf{entropy\\_mean}: Mean NLL (proxy for reference-model perplexity).\n  \\item \\textbf{entropy\\_std}: Standard deviation of per-token NLL.\n  \\item \\textbf{entropy\\_max}: Maximum per-token NLL.\n  \\item \\textbf{entropy\\_min}: Minimum per-token NLL.\n  \\item \\textbf{tail\\_decay}: Rate of exponential decay in the upper tail of the NLL distribution.\n\\end{itemize}\n\nThese features are standard NLL summary statistics; the novelty lies in applying them to ordinal depth estimation rather than binary detection.\n\n\\subsection{Classifier}\nWe train an XGBoost gradient-boosted tree classifier on the 7-dimensional feature vector.\nHyperparameters are selected via 5-fold cross-validation on training data.\nWe also evaluate a QLoRA-finetuned Qwen3.5-0.8B as an end-to-end baseline (Section~\\ref{sec:e2e}).\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n% ============================================================\n\nWe organize experiments around four research questions:\n\\textbf{RQ1}: Can distributional features estimate generation depth? (Sections~\\ref{sec:indist}--\\ref{sec:length})\n\\textbf{RQ2}: How does depth signal scale with generator capacity? (Section~\\ref{sec:scale})\n\\textbf{RQ3}: What are the generalization boundaries? (Sections~\\ref{sec:cross_gen}--\\ref{sec:cross_model})\n\\textbf{RQ4}: Is depth estimation useful for downstream curation? (Section~\\ref{sec:downstream})\n\n% --------------------------------------------------\n\\subsection{In-Distribution Baseline}\n\\label{sec:indist}\n\nWe first establish baseline performance using Pythia-2.8B as generator and Pythia-410M as reference model on Wikipedia-domain continuation chains.\n\n\\begin{table}[h]\n\\centering\n\\caption{Feature ablation on in-distribution data (Pythia-2.8B generator, Pythia-410M reference, Wikipedia continuation chains).}\n\\label{tab:ablation}\n\\begin{tabular}{lccccc}\n\\toprule\nFeature Set & Macro-F1 & 95\\% CI & Gen-0 & Gen-1 & Gen-2+ \\\\\n\\midrule\nFull (7 features) & 0.820 & [0.807, 0.834] & 0.952 & 0.776 & 0.795 \\\\\nSurface only & 0.763 & [0.747, 0.774] & 0.920 & 0.710 & 0.658 \\\\\nReference only & 0.719 & [0.706, 0.733] & 0.895 & 0.640 & 0.621 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn-distribution, the full feature set achieves macro-F1 of 0.820 (Table~\\ref{tab:ablation}).\nSurface features alone yield 0.763 and reference features alone 0.719, indicating complementary signal.\nMedian reference-model perplexity decreases monotonically across depths: 13.5 (gen-0), 4.96 (gen-1), 3.00 (gen-2), 2.07 (gen-3), 1.72 (gen-4).\n\nFeature-level analysis reveals two behavioral groups (Table~\\ref{tab:h1h2}).\nThree features show monotonic depth correlation ($R^2 > 0.8$): entropy\\_mean ($\\rho$=-0.68), TTR ($\\rho$=-0.31), and hapax\\_ratio ($\\rho$=-0.28).\nFour features show negligible depth correlation ($R^2 < 0.1$): entropy\\_std, entropy\\_max, entropy\\_min, and tail\\_decay.\nWe label these drifting (H2) and stationary (H1) groups respectively.\n\n\\begin{table}[h]\n\\centering\n\\caption{Feature classification by depth behavior. H2: monotonic depth drift. H1: near-stationary.}\n\\label{tab:h1h2}\n\\begin{tabular}{lcccc}\n\\toprule\nFeature & Source & Depth Slope & $R^2$ & Class \\\\\n\\midrule\nentropy\\_mean & reference & $-0.042$ & 0.91 & H2 (drift) \\\\\nTTR & surface & $-0.031$ & 0.87 & H2 (drift) \\\\\nhapax\\_ratio & surface & $-0.028$ & 0.83 & H2 (drift) \\\\\n\\midrule\nentropy\\_std & reference & $+0.003$ & 0.04 & H1 (stationary) \\\\\nentropy\\_max & reference & $-0.005$ & 0.07 & H1 (stationary) \\\\\nentropy\\_min & reference & $+0.002$ & 0.02 & H1 (stationary) \\\\\ntail\\_decay & reference & $+0.004$ & 0.05 & H1 (stationary) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHowever, as subsequent sections will show, these in-distribution results are misleadingly optimistic due to same-family reference model alignment, length confounds, and single-generator specificity.\n\n% --------------------------------------------------\n\\subsection{Text Length as Confound}\n\\label{sec:length}\n\nGenerated texts exhibit a length-depth correlation ($r$=0.42): deeper generations tend to be shorter.\nSince surface diversity metrics are mechanically length-dependent, this confound must be addressed.\n\n\\begin{table}[h]\n\\centering\n\\caption{Classification performance before and after length control.}\n\\label{tab:length}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Full F1 & Surface F1 & Reference F1 & Gap \\\\\n\\midrule\nOriginal & 0.78 & 0.76 & 0.72 & 0.02 \\\\\nLength-normalized features & 0.68 & 0.63 & 0.66 & 0.02 \\\\\nLength-matched subsampling & 0.70 & 0.65 & 0.67 & 0.03 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLength normalization reduces full-feature F1 from 0.78 to 0.68---a 10-point drop (Table~\\ref{tab:length}).\nThe impact is concentrated in surface features: TTR depth correlation drops from $\\rho$=-0.31 to $\\rho$=-0.12 (61\\% explained by length), and hapax ratio from $\\rho$=-0.28 to $\\rho$=-0.09 (68\\% explained by length) as shown in Table~\\ref{tab:length_features}.\nReference-model entropy\\_mean is less affected (19\\% explained by length, $\\rho$: $-0.68 \\to -0.55$), confirming it carries genuine depth signal beyond the length confound.\n\n\\begin{table}[h]\n\\centering\n\\caption{Feature depth correlation before and after length normalization.}\n\\label{tab:length_features}\n\\begin{tabular}{lccc}\n\\toprule\nFeature & Original $\\rho$ & Length-norm.\\ $\\rho$ & \\% Explained by Length \\\\\n\\midrule\nTTR & $-0.31$ & $-0.12$ & 61\\% \\\\\nhapax\\_ratio & $-0.28$ & $-0.09$ & 68\\% \\\\\nentropy\\_mean & $-0.68$ & $-0.55$ & 19\\% \\\\\nentropy\\_std & $+0.03$ & $+0.02$ & 33\\% \\\\\ntail\\_decay & $+0.04$ & $+0.03$ & 25\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAfter controlling for length, the advantage of the full feature set over surface-only features nearly vanishes (0.68 vs 0.63 = 0.05, down from 0.06), indicating that reference features' previous advantage was partly due to being less length-confounded rather than capturing fundamentally different depth information.\n\n% --------------------------------------------------\n\\subsection{Cross-Generator Generalization}\n\\label{sec:cross_gen}\n\nWe evaluate generalization using leave-one-generator-out (LOGO) across 5 generators from 3 model families: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, and Qwen3-0.6B.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-generator-out macro-F1. Mean across generators: 0.52.}\n\\label{tab:logo}\n\\begin{tabular}{llcccc}\n\\toprule\nHeld-Out Generator & Family & Macro-F1 & Gen-0 & Gen-1 & Gen-2+ \\\\\n\\midrule\nPythia-2.8B & Pythia & 0.61 & 0.82 & 0.51 & 0.50 \\\\\nPythia-1B & Pythia & 0.64 & 0.85 & 0.54 & 0.53 \\\\\nOLMo-2-1B & OLMo & 0.48 & 0.72 & 0.38 & 0.34 \\\\\nQwen3-1.7B & Qwen & 0.44 & 0.68 & 0.35 & 0.29 \\\\\nQwen3-0.6B & Qwen & 0.43 & 0.67 & 0.33 & 0.29 \\\\\n\\midrule\nMean (all) & --- & 0.52 & 0.75 & 0.42 & 0.39 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLOGO macro-F1 averages 0.52 (Table~\\ref{tab:logo}), substantially below the in-distribution 0.82.\nWithin-family generalization (Pythia $\\to$ Pythia) averages 0.625, while cross-family generalization (e.g., Pythia+Qwen $\\to$ OLMo) averages 0.45.\nGen-0 detection remains passable (mean 0.75) because human-written text is universally distinct, but gen-1 vs gen-2+ discrimination---the core depth signal---collapses across families.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-family-out evaluation.}\n\\label{tab:lofo}\n\\begin{tabular}{lcc}\n\\toprule\nHeld-Out Family & Train Generators & Macro-F1 \\\\\n\\midrule\nPythia & OLMo+Qwen & 0.41 \\\\\nOLMo & Pythia+Qwen & 0.54 \\\\\nQwen & Pythia+OLMo & 0.56 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLeave-one-family-out results (Table~\\ref{tab:lofo}) confirm family-level dependence: holding out Pythia (the family matching our reference model) drops F1 to 0.41, indicating the classifier critically relies on same-family reference model alignment.\n\n% --------------------------------------------------\n\\subsection{Reference Model Sensitivity}\n\\label{sec:ref_model}\n\nWe test whether the depth signal generalizes across reference models by computing features using OLMo-2-1B and Qwen3-0.6B in addition to the default Pythia-410M.\n\n\\begin{table}[h]\n\\centering\n\\caption{Entropy\\_mean depth correlation by reference model. The strong H2 drift observed with Pythia-410M is reference-family-specific.}\n\\label{tab:ref_corr}\n\\begin{tabular}{llccc}\n\\toprule\nReference Model & Family & entropy\\_mean $\\rho$ & $p$-value & H2 Status \\\\\n\\midrule\nPythia-410M & Pythia & $-0.68$ & $<$0.001 & Confirmed \\\\\nOLMo-2-1B & OLMo & $-0.22$ & 0.031 & Weak ($|\\rho|<0.3$) \\\\\nQwen3-0.6B & Qwen & $-0.15$ & 0.118 & Not confirmed \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe strong entropy\\_mean depth correlation ($\\rho$=-0.68) observed with the Pythia-410M reference largely disappears with non-Pythia references: $\\rho$=-0.22 (OLMo) and $\\rho$=-0.15 (Qwen, non-significant; Table~\\ref{tab:ref_corr}).\nThis occurs because the Pythia-410M reference shares architecture and training data with the Pythia generators, producing calibrated perplexity estimates that systematically track depth.\nCross-family references assign noisier, less calibrated perplexities.\n\n\\begin{table}[h]\n\\centering\n\\caption{Classification performance by reference model.}\n\\label{tab:ref_class}\n\\begin{tabular}{lcccc}\n\\toprule\nReference Model & Full F1 & Surface F1 & Ref-only F1 & Full--Surface Gap \\\\\n\\midrule\nPythia-410M & 0.82 & 0.76 & 0.72 & 0.06 \\\\\nOLMo-2-1B & 0.63 & 0.61 & 0.48 & 0.02 \\\\\nQwen3-0.6B & 0.58 & 0.57 & 0.41 & 0.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nClassification F1 drops sharply with cross-family references (Table~\\ref{tab:ref_class}): from 0.82 (Pythia) to 0.63 (OLMo) and 0.58 (Qwen).\nReference-only F1 drops to 0.48 and 0.41 respectively, while surface-only F1 remains stable at 0.57--0.61 (as expected, since surface features are reference-model-independent).\n\nExamining feature stability across references (Table~\\ref{tab:stability}), we find that distributional shape features (entropy\\_std, entropy\\_max, tail\\_decay) remain H1-stationary regardless of reference model---this is genuinely robust.\nHowever, the drifting features reduce to surface-only metrics (TTR, hapax), which Section~\\ref{sec:length} showed are largely length artifacts.\n\n\\begin{table}[h]\n\\centering\n\\caption{Feature behavioral classification stability across reference models.}\n\\label{tab:stability}\n\\begin{tabular}{lcccc}\n\\toprule\nFeature & Pythia Class & OLMo Class & Qwen Class & Stable? \\\\\n\\midrule\nentropy\\_mean & H2 & weak/NS & NS & No \\\\\nentropy\\_std & H1 & H1 & H1 & Yes \\\\\nentropy\\_max & H1 & H1 & H1 & Yes \\\\\ntail\\_decay & H1 & H1 & H1 & Yes \\\\\nTTR & H2 & H2 & H2 & Yes \\\\\nhapax\\_ratio & H2 & H2 & weak H2 & Marginal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% --------------------------------------------------\n\\subsection{Generator Scale Analysis}\n\\label{sec:scale}\n\nWe evaluate depth estimation across generator scales from 0.6B to 8B parameters (Table~\\ref{tab:scale}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth classification by generator scale. Depth signal degrades with model capacity ($r$=-0.85 between log-params and F1).}\n\\label{tab:scale}\n\\begin{tabular}{lcccccc}\n\\toprule\nGenerator & Params & F1 & Gen-0 & Gen-1 & Gen-2+ & $\\rho_{\\text{ent}}$ \\\\\n\\midrule\nQwen3-0.6B & 0.6B & 0.74 & 0.91 & 0.66 & 0.65 & $-0.58$ \\\\\nPythia-1B & 1B & 0.71 & 0.89 & 0.62 & 0.62 & $-0.55$ \\\\\nOLMo-2-1B & 1.5B & 0.69 & 0.87 & 0.60 & 0.60 & $-0.51$ \\\\\nQwen3-1.7B & 1.7B & 0.68 & 0.86 & 0.58 & 0.60 & $-0.48$ \\\\\nPythia-2.8B & 2.8B & 0.78 & 0.93 & 0.72 & 0.69 & $-0.68$ \\\\\nQwen3-8B & 8B & 0.43 & 0.62 & 0.35 & 0.32 & $-0.19$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 8B generator yields near-chance depth estimation (F1=0.43) with severely degraded gen-1 and gen-2+ discrimination (0.35 and 0.32).\nThe correlation between log-parameters and macro-F1 is $r$=-0.85 (excluding the Pythia-2.8B outlier, which benefits from same-family reference alignment).\n\nThe mechanism is revealed by perplexity dynamic range analysis (Table~\\ref{tab:ppl_range}): the reference model's ability to distinguish depths relies on perplexity separation between depths, which compresses as generator fluency increases.\nFor Pythia-2.8B, perplexity ranges from 13.5 (gen-0) to 1.7 (gen-4), a dynamic range of 11.8.\nFor Qwen3-8B, this compresses to 8.2--4.1, a dynamic range of only 4.1---the larger model produces text that is already close to the reference model's expectations at every depth.\n\n\\begin{table}[h]\n\\centering\n\\caption{Reference-model perplexity dynamic range by generator scale. Larger generators compress the perplexity range available for depth discrimination.}\n\\label{tab:ppl_range}\n\\begin{tabular}{lcccc}\n\\toprule\nGenerator & PPL (depth-0) & PPL (depth-4) & Dynamic Range & PPL Ratio \\\\\n\\midrule\nPythia-2.8B & 13.5 & 1.7 & 11.8 & 7.9$\\times$ \\\\\nPythia-1B & 12.8 & 2.1 & 10.7 & 6.1$\\times$ \\\\\nOLMo-2-1B & 11.4 & 2.5 & 8.9 & 4.6$\\times$ \\\\\nQwen3-1.7B & 10.8 & 2.8 & 8.0 & 3.9$\\times$ \\\\\nQwen3-8B & 8.2 & 4.1 & 4.1 & 2.0$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis result connects to model collapse theory~\\citep{gerstgrasser2024model}: larger models collapse slower under recursive generation, producing less distributional drift per step.\nConsequently, depth estimation with distributional features faces a fundamental scaling barrier---the models most likely to produce recursive content in practice (large, capable models) are precisely those for which depth signal is weakest.\n\n% --------------------------------------------------\n\\subsection{Prompt Type and Chain Structure}\n\\label{sec:prompt_type}\n\nWe evaluate three prompt types: continuation (direct text continuation), elaboration (topic expansion), and inspired rewriting (semantic departure from source).\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth classification by prompt type.}\n\\label{tab:prompt}\n\\begin{tabular}{lcccc}\n\\toprule\nPrompt Type & Macro-F1 & $\\rho_{\\text{ent}}$ & $\\rho_{\\text{TTR}}$ & Gen-1 vs Gen-2+ F1 \\\\\n\\midrule\nContinuation & 0.78 & $-0.65$ & $-0.29$ & 0.71 \\\\\nElaboration & 0.55 & $-0.38$ & $-0.16$ & 0.44 \\\\\nInspired rewriting & 0.47 & $-0.18$ & $-0.08$ & 0.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDepth signal varies dramatically with prompt type (Table~\\ref{tab:prompt}).\nContinuation chains preserve the strongest signal (F1=0.78) because each step builds directly on the previous output, creating cumulative distributional drift.\nElaboration reduces this to F1=0.55, and inspired rewriting yields near-chance F1=0.47 because the semantic departure partially resets distributional state at each step.\n\nCross-prompt transfer is poor: training on one prompt type and testing on another yields average F1=0.42 (Table~\\ref{tab:prompt_transfer}), indicating that depth features are prompt-type-specific.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-prompt type transfer (train $\\to$ test).}\n\\label{tab:prompt_transfer}\n\\begin{tabular}{lccc}\n\\toprule\nTrain $\\to$ Test & Elaboration & Rewriting & Continuation \\\\\n\\midrule\nContinuation $\\to$ & 0.46 & 0.39 & --- \\\\\nElaboration $\\to$ & --- & 0.42 & 0.51 \\\\\nRewriting $\\to$ & 0.40 & --- & 0.44 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Paraphrastic vs.\\ non-paraphrastic chains.}\nComparing paraphrastic and continuation chains (Table~\\ref{tab:para}) confirms attractor theory predictions: paraphrastic chains converge by depth 2 (gen-2 vs gen-3 F1=0.34), while continuation chains preserve signal slightly longer but also saturate by depth 3.\n\n\\begin{table}[h]\n\\centering\n\\caption{Paraphrastic vs.\\ continuation chain depth discrimination.}\n\\label{tab:para}\n\\begin{tabular}{lcccccc}\n\\toprule\nChain Type & 3-class F1 & Gen-0 & Gen-1 & Gen-2+ & $\\rho_{\\text{ent}}$ \\\\\n\\midrule\nParaphrastic & 0.52 & 0.78 & 0.45 & 0.33 & $-0.31$ \\\\\nContinuation & 0.78 & 0.93 & 0.72 & 0.69 & $-0.65$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% --------------------------------------------------\n\\subsection{Cross-Model Chains}\n\\label{sec:cross_model}\n\nReal-world contamination may involve different generators at each depth step.\nWe evaluate cross-model chains where the generator changes randomly at each step (Table~\\ref{tab:crossmodel}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Single-model vs.\\ cross-model chain depth estimation.}\n\\label{tab:crossmodel}\n\\begin{tabular}{lcccc}\n\\toprule\nChain Type & Macro-F1 & Gen-0 & Gen-1 & Gen-2+ \\\\\n\\midrule\nSingle model & 0.78 & 0.93 & 0.72 & 0.69 \\\\\nCross-model (random) & 0.39 & 0.65 & 0.28 & 0.24 \\\\\nCross-model (increasing size) & 0.41 & 0.66 & 0.30 & 0.27 \\\\\nCross-model (decreasing size) & 0.38 & 0.63 & 0.27 & 0.24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-model chains destroy depth signal (F1=0.39), with gen-1 and gen-2+ near chance (0.28 and 0.24).\nGenerator identity is a much stronger signal than depth: a gen-1 text from Qwen differs more from gen-1 text from Pythia than gen-1 differs from gen-2 within the same generator.\nThis represents the most ecologically challenging result, as real web contamination involves diverse generators.\n\n% --------------------------------------------------\n\\subsection{Multi-Domain Evaluation}\n\\label{sec:domain}\n\nWe expand to 4 domains with 500 seeds each (Table~\\ref{tab:domain}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth classification by source domain.}\n\\label{tab:domain}\n\\begin{tabular}{lccccc}\n\\toprule\nDomain & $n$ Seeds & Macro-F1 & Gen-0 & Gen-1 & Gen-2+ \\\\\n\\midrule\nWikipedia & 500 & 0.72 & 0.89 & 0.63 & 0.64 \\\\\nNews & 500 & 0.68 & 0.86 & 0.59 & 0.59 \\\\\nScientific & 500 & 0.55 & 0.78 & 0.44 & 0.43 \\\\\nCreative & 500 & 0.48 & 0.71 & 0.37 & 0.36 \\\\\n\\midrule\nAll pooled & 2000 & 0.61 & 0.81 & 0.51 & 0.51 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDomain substantially moderates depth signal ($\\sigma_{F1}$=0.11).\nFactual domains (Wikipedia, news) show passable performance, while creative writing yields near-chance F1=0.48.\nCross-domain transfer averages F1=0.49, adding domain to the list of moderating factors (alongside prompt type and generator family) that limit generalizability.\n\n% --------------------------------------------------\n\\subsection{Ordinal Granularity}\n\\label{sec:ordinal}\n\nWe test 5-class ordinal classification (gen-0 through gen-4) to establish the granularity ceiling (Table~\\ref{tab:ordinal}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Five-class ordinal depth classification.}\n\\label{tab:ordinal}\n\\begin{tabular}{lcccc}\n\\toprule\nClass & Precision & Recall & F1 & $n$ \\\\\n\\midrule\nGen-0 & 0.88 & 0.82 & 0.85 & 995 \\\\\nGen-1 & 0.39 & 0.45 & 0.42 & 993 \\\\\nGen-2 & 0.16 & 0.20 & 0.18 & 912 \\\\\nGen-3 & 0.11 & 0.13 & 0.12 & 856 \\\\\nGen-4 & 0.10 & 0.12 & 0.11 & 816 \\\\\n\\midrule\n\\multicolumn{3}{l}{5-class macro-F1: 0.28} & \\multicolumn{2}{l}{MAE: 1.4} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFive-class macro-F1 of 0.28 is barely above chance (0.20).\nGen-2/3/4 collapse into an indistinguishable cluster (F1: 0.18/0.12/0.11), with 72\\% of misclassifications between adjacent classes.\nThis validates the 3-class design: ordinal depth beyond gen-0/gen-1/gen-2+ is not discriminable with distributional features, consistent with attractor convergence theory extended to non-paraphrastic generation.\n\n% --------------------------------------------------\n\\subsection{Robustness to Human Editing}\n\\label{sec:robustness}\n\n\\begin{table}[h]\n\\centering\n\\caption{Robustness to simulated post-generation editing.}\n\\label{tab:edits}\n\\begin{tabular}{lccc}\n\\toprule\nEdit Type & Edit Rate & Macro-F1 & $\\Delta$F1 \\\\\n\\midrule\nNone & 0\\% & 0.78 & --- \\\\\nRandom replace & 5\\% & 0.68 & $-0.10$ \\\\\nRandom replace & 10\\% & 0.58 & $-0.20$ \\\\\nRandom replace & 20\\% & 0.44 & $-0.34$ \\\\\nLLM light edit & $\\sim$8\\% & 0.53 & $-0.25$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDepth features are fragile to post-generation modification (Table~\\ref{tab:edits}).\nEven 5\\% random word replacement reduces F1 by 0.10, and LLM-simulated editing reduces F1 by 0.25.\nLLM editing is more damaging than random replacement because it systematically smooths the distributional artifacts that depth estimation relies on.\nThis limits practical applicability to detection of fully automated, unedited generation chains.\n\n% --------------------------------------------------\n\\subsection{Additional Features and End-to-End Baseline}\n\\label{sec:e2e}\n\n\\paragraph{LD-Score as depth feature.}\nAdding LD-Score~\\citep{tulchinskii2024ldscore} (a character-level distributional signature) provides negligible improvement: depth correlation $\\rho$=-0.25, F1 increase from 0.780 to 0.785.\nLD-Score shows weak depth sensitivity but insufficient signal to meaningfully contribute beyond existing features.\n\n\\begin{table}[h]\n\\centering\n\\caption{Handcrafted features vs.\\ end-to-end fine-tuned classifier.}\n\\label{tab:e2e}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & In-Dist.\\ F1 & Cross-Gen LOGO F1 & GPU Hours \\\\\n\\midrule\nHandcrafted + XGBoost & 0.78 & 0.52 & 0.1 \\\\\nQwen3.5-0.8B QLoRA & 0.83 & 0.55 & 15 \\\\\nQwen3.5-0.8B (frozen) & 0.80 & 0.53 & 8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{End-to-end classifier.}\nA QLoRA-finetuned Qwen3.5-0.8B achieves F1=0.83 in-distribution, slightly above the handcrafted 0.78 (Table~\\ref{tab:e2e}).\nHowever, it shares the same cross-generator failure (LOGO F1=0.55 vs.\\ 0.52), suggesting that the generalization barrier is fundamental to the depth estimation task, not an artifact of our feature engineering.\n\n% --------------------------------------------------\n\\subsection{Downstream Utility}\n\\label{sec:downstream}\n\nWe fine-tune OLMo-1B on depth-stratified data (5 seeds, bootstrap CIs) to test whether depth-aware filtering improves downstream model quality compared to binary filtering (Table~\\ref{tab:downstream}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Downstream fine-tuning results (OLMo-1B, 5 seeds).}\n\\label{tab:downstream}\n\\begin{tabular}{lcccc}\n\\toprule\nFiltering Strategy & Mean PPL & Std & 95\\% CI & Improvement \\\\\n\\midrule\nUnfiltered & 14.8 & 0.42 & [14.2, 15.4] & --- \\\\\nBinary (FastDetectGPT) & 14.5 & 0.51 & [13.8, 15.2] & 1.2\\% [$-$1.1, 3.5] \\\\\nBinary (LD-Score) & 14.6 & 0.48 & [14.0, 15.2] & 0.9\\% [$-$1.4, 3.2] \\\\\nDepth-aware (keep gen-0/1) & 14.2 & 0.39 & [13.7, 14.7] & 1.8\\% [$-$0.5, 4.1] \\\\\nDepth-aware (sample-matched) & 14.2 & 0.44 & [13.6, 14.8] & 1.5\\% [$-$0.8, 3.8] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDepth-aware filtering shows a directional advantage (1.8\\% vs.\\ 1.2\\% improvement over unfiltered) but confidence intervals overlap substantially (depth vs.\\ binary $p$=0.31).\nThe improvement is not statistically significant at this sample size.\n\nPredicted depth does correlate weakly with quality degradation ($\\rho$=0.28, 95\\% CI [0.11, 0.45]).\nPerplexity increases monotonically with depth: 12.1 (gen-0) $\\to$ 13.4 (gen-1) $\\to$ 14.1 (gen-2) $\\to$ 14.5 (gen-3) $\\to$ 14.9 (gen-4), confirming that deeper generation produces lower-quality training data.\nHowever, this descriptive finding does not translate into significant downstream filtering advantage with current methods.\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n% ============================================================\n\n\\paragraph{The task is well-defined but harder than expected.}\nGeneration depth estimation is conceptually sound: depth correlates with quality degradation, and ordinal estimation enables more nuanced curation than binary detection.\nHowever, our comprehensive evaluation reveals that current distributional features fall short of reliable depth estimation under realistic conditions.\nThe 3-class problem is feasible in controlled settings (single generator, single domain, continuation chains) but degrades along every generalization axis we tested.\n\n\\paragraph{Reference-model perplexity: strong but specific.}\nThe monotonic perplexity decrease across depths (13.5 $\\to$ 1.7) is the most robust univariate depth signal.\nHowever, this signal depends critically on reference-generator family alignment ($\\rho$=-0.68 same-family vs.\\ $\\rho$=-0.15 cross-family).\nThis aligns with an interpretation based on distributional calibration: a same-family reference model has calibrated predictions for the generator's output distribution, making perplexity sensitive to the subtle distributional shifts across depths.\nA cross-family reference assigns noisier perplexities that wash out the depth signal.\n\n\\paragraph{Scale-dependent depth estimation.}\nThe strong negative correlation between generator scale and depth discriminability ($r$=-0.85) is our most concerning finding for practical deployment.\nLarger models produce more fluent text with smaller distributional drift per recursive step, compressing the perplexity dynamic range available for depth discrimination (11.8 for 2.8B vs.\\ 4.1 for 8B).\nThis connects to theoretical results on scale-dependent collapse rates~\\citep{gerstgrasser2024model}: if larger models converge slower, then depth-correlated distributional drift is correspondingly smaller at each step.\nAs the most capable models are also those most likely to be used in recursive generation pipelines, this scaling barrier is a fundamental challenge.\n\n\\paragraph{Confounds and moderators.}\nWe identify text length, prompt type, generator family, source domain, and post-generation editing as significant moderators.\nThe length confound is particularly concerning: 61--68\\% of surface feature depth correlation is attributable to length variation.\nAfter controlling for these confounds, the residual depth signal, while real, is substantially weaker than in-distribution baselines suggest.\n\n\\paragraph{Limitations.}\nOur study is limited to open-weight models $\\leq$8B parameters; frontier models (70B+) may exhibit even weaker depth signal.\nThe benchmark uses constructed chains rather than naturally occurring recursive generation, which may differ in distribution.\nAll reference models used are autoregressive transformers; alternative architectures may provide complementary signals.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n% ============================================================\n\nWe formalize generation depth estimation as a new task in synthetic text analysis and provide a comprehensive benchmark spanning 12 experimental conditions.\nOur study identifies three key findings: (1)~three-class depth estimation (gen-0/gen-1/gen-2+) represents the practical granularity ceiling; (2)~reference-model perplexity is the strongest depth proxy but requires generator-family-aligned reference models; and (3)~depth signal exhibits scale-dependent degradation, with 8B generators already yielding near-chance estimation.\nThese results position generation depth estimation as a meaningful but challenging open problem, and the scale-dependent signal degradation connects empirically to model collapse theory.\nWe release our benchmark dataset and evaluation protocols to support future work on generator-invariant depth features that may overcome the limitations documented here.\n\n% ============================================================\n% References\n% ============================================================\n\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Alemohammad et~al.(2024)]{alemohammad2024selfconsuming}\nS.~Alemohammad, J.~Casco-Rodriguez, L.~Luber, A.~G. Humair, S.~Babaei, D.~LeJeune, A.~Sivaraman, and R.~G. Baraniuk.\n\\newblock Self-consuming generative models go {MAD}.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Bao et~al.(2024)]{bao2024fastdetectgpt}\nG.~Bao, Y.~Zhao, Z.~Teng, L.~Yang, and Y.~Zhang.\n\\newblock {Fast-DetectGPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Briesch et~al.(2023)]{briesch2023attractor}\nM.~Briesch, D.~Sobania, and F.~Rothlauf.\n\\newblock Large language models suffer from their own output: An analysis of the self-consuming training loop.\n\\newblock \\emph{arXiv preprint arXiv:2311.16822}, 2023.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024model}\nE.~Dohmatob, P.~Feng, Q.~Yang, F.~Charton, and J.~Kempe.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Gehrmann et~al.(2019)]{gehrmann2019gltr}\nS.~Gehrmann, H.~Strobelt, and A.~M. Rush.\n\\newblock {GLTR}: Statistical detection and visualization of generated text.\n\\newblock In \\emph{ACL}, 2019.\n\n\\bibitem[Gerstgrasser et~al.(2024)]{gerstgrasser2024model}\nM.~Gerstgrasser, R.~Schaeffer, A.~Dey, R.~Rafailov, H.~Tombai, Y.~Nishi, S.~Levine, and K.~Koyejo.\n\\newblock Is model collapse inevitable? {Breaking} the curse of recursion by accumulating real and synthetic data.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Guo et~al.(2024)]{guo2024curious}\nB.~Guo, X.~Zhang, Z.~Wang, M.~Jiang, J.~Nie, Y.~Ding, J.~Yue, and Y.~Wu.\n\\newblock How close is {ChatGPT} to human experts? {Comparison} corpus, evaluation, and detection.\n\\newblock \\emph{arXiv preprint arXiv:2301.07597}, 2024.\n\n\\bibitem[Hans et~al.(2024)]{hans2024binoculars}\nA.~Hans, A.~Schwarzschild, V.~Cherepanova, H.~Kazemi, A.~Saha, M.~Goldblum, J.~Geiping, and T.~Goldstein.\n\\newblock Spotting {LLMs} with {Binoculars}: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Hendrycks and Gimpel(2017)]{hendrycks2017baseline}\nD.~Hendrycks and K.~Gimpel.\n\\newblock A baseline for detecting misclassified and out-of-distribution examples in neural networks.\n\\newblock In \\emph{ICLR}, 2017.\n\n\\bibitem[Holtzman et~al.(2020)]{holtzman2020curious}\nA.~Holtzman, J.~Buys, L.~Du, M.~Forbes, and Y.~Choi.\n\\newblock The curious case of neural text degeneration.\n\\newblock In \\emph{ICLR}, 2020.\n\n\\bibitem[Kirchenbauer et~al.(2023)]{kirchenbauer2023watermark}\nJ.~Kirchenbauer, J.~Geiping, Y.~Wen, J.~Katz, I.~Miers, and T.~Goldstein.\n\\newblock A watermark for large language models.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nE.~Mitchell, Y.~Lee, A.~Khazatsky, C.~D. Manning, and C.~Finn.\n\\newblock {DetectGPT}: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Padmakumar and He(2024)]{padmakumar2024does}\nV.~Padmakumar and H.~He.\n\\newblock Does writing with language models reduce content diversity?\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024curse}\nI.~Shumailov, Z.~Shumaylov, Y.~Zhao, N.~Papernot, R.~Anderson, and Y.~Gal.\n\\newblock The curse of recursion: Training on generated data makes models forget.\n\\newblock \\emph{Nature}, 2024.\n\n\\bibitem[Solaiman et~al.(2019)]{solaiman2019release}\nI.~Solaiman, M.~Brundage, J.~Clark, A.~Askell, A.~Herbert-Voss, J.~Wu, A.~Radford, G.~Krueger, J.~W. Kim, S.~Kreps, et~al.\n\\newblock Release strategies and the social impacts of language models.\n\\newblock \\emph{arXiv preprint arXiv:1908.09203}, 2019.\n\n\\bibitem[Tulchinskii et~al.(2024)]{tulchinskii2024ldscore}\nE.~Tulchinskii, K.~Kuznetsov, L.~Kushnareva, D.~Cherniavskii, S.~Nikolenko, E.~Burnaev, S.~Barannikov, and I.~Piontkovskaya.\n\\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Uchendu et~al.(2020)]{uchendu2020authorship}\nA.~Uchendu, T.~Le, K.~Shu, and D.~Lee.\n\\newblock Authorship attribution for neural text generation.\n\\newblock In \\emph{EMNLP}, 2020.\n\n\\bibitem[Wenzek et~al.(2020)]{wenzek2020ccnet}\nG.~Wenzek, M.-A. Lachaux, A.~Conneau, V.~Chaudhary, F.~Guzm{\\'a}n, A.~Joulin, and E.~Grave.\n\\newblock {CCNet}: Extracting high quality monolingual datasets from web crawl data.\n\\newblock In \\emph{LREC}, 2020.\n\n\\bibitem[Wettig et~al.(2024)]{wettig2024qurating}\nA.~Wettig, A.~Gao, Z.~Zhong, and D.~Chen.\n\\newblock {QuRating}: Selecting high-quality data for training language models.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Xie et~al.(2023)]{xie2023dsir}\nS.~M. Xie, S.~Santurkar, T.~Ma, and P.~Liang.\n\\newblock Data selection for language models via importance resampling.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "ecea2c85-a946-4d5e-bba7-4acc9fee26d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerp…",
  "leafUuid": "bdd4674b-6b31-4917-a4cb-940ca68243ec",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth estimation in synthetic text analysis",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6"
}
```

---

### Tool call

_source line 24 · 2026-05-14T22:50:27.139Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Pvwqs48HVqf2JHMiVNXM74`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdd4674b-6b31-4917-a4cb-940ca68243ec",
  "isSidechain": false,
  "requestId": "req_011Cb3H91BVxM9b9RgMsN3x3",
  "type": "assistant",
  "uuid": "1cf1921f-fa44-4abd-974d-73ed2fce5722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfyqA2TsK7XdDBZSKHdaHN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14427,
      "cache_read_input_tokens": 43474,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 43474,
          "cache_creation_input_tokens": 14427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14427
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

_source line 25 · 2026-05-14T22:50:28.403Z_

<details><summary>↩ Tool result · `toolu_01Pvwqs48HVqf2JHMiVNXM74`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
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

Package natbib Warning: Citation `mitchell2023detectgpt' on page 1 undefined on
 input line 46.


Package natbib Warning: Citation `bao2024fastdetectgpt' on page 1 undefined on 
input line 46.


Package natbib Warning: Citation `hans2024binoculars' on page 1 undefined on in
put line 46.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]
Overfull \hbox (1.48647pt too wide) in paragraph at lines 62--63
[]\OT1/cmr/bx/n/10.95 Comprehensive lim-i-ta-tion anal-y-sis\OT1/cmr/m/n/10.95 
: We doc-u-ment fail-ure modes in-clud-ing cross-generator

Package natbib Warning: Citation `gehrmann2019gltr' on page 2 undefined on inpu
t line 71.


Package natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on
 input line 71.


Package natbib Warning: Citation `bao2024fastdetectgpt' on page 2 undefined on 
input line 71.


Package natbib Warning: Citation `hans2024binoculars' on page 2 undefined on in
put line 71.


Package natbib Warning: Citation `solaiman2019release' on page 2 undefined on i
nput line 71.


Package natbib Warning: Citation `uchendu2020authorship' on page 2 undefined on
 input line 71.


Package natbib Warning: Citation `kirchenbauer2023watermark' on page 2 undefine
d on input line 71.


Package natbib Warning: Citation `tulchinskii2024ldscore' on page 2 undefined o
n input line 71.


Package natbib Warning: Citation `alemohammad2024selfconsuming' on page 2 undef
ined on input line 75.


Package natbib Warning: Citation `shumailov2024curse' on page 2 undefined on in
put line 75.


Package natbib Warning: Citation `dohmatob2024model' on page 2 undefined on inp
ut line 75.


Package natbib Warning: Citation `gerstgrasser2024model' on page 2 undefined on
 input line 75.


Package natbib Warning: Citation `briesch2023attractor' on page 2 undefined on 
input line 76.


Package natbib Warning: Citation `xie2023dsir' on page 2 undefined on input lin
e 80.


Package natbib Warning: Citation `wettig2024qurating' on page 2 undefined on in
put line 80.


Package natbib Warning: Citation `wenzek2020ccnet' on page 2 undefined on input
 line 80.


Package natbib Warning: Citation `guo2024curious' on page 2 undefined on input 
line 84.


Package natbib Warning: Citation `padmakumar2024does' on page 2 undefined on in
put line 84.


Package natbib Warning: Citation `holtzman2020curious' on page 2 undefined on i
nput line 84.


LaTeX Warning: Reference `sec:ordinal' on page 2 undefined on input line 102.

[2]

LaTeX Warning: Reference `sec:prompt_type' on page 3 undefined on input line 10
6.


LaTeX Warning: Reference `sec:indist' on page 3 undefined on input line 107.


LaTeX Warning: Reference `sec:scale' on page 3 undefined on input line 107.


LaTeX Warning: Reference `sec:cross_model' on page 3 undefined on input line 10
7.


LaTeX Warning: Reference `sec:e2e' on page 3 undefined on input line 143.


LaTeX Warning: Reference `sec:indist' on page 3 undefined on input line 151.


LaTeX Warning: Reference `sec:length' on page 3 undefined on input line 151.


LaTeX Warning: Reference `sec:scale' on page 3 undefined on input line 152.


LaTeX Warning: Reference `sec:cross_gen' on page 3 undefined on input line 153.



LaTeX Warning: Reference `sec:cross_model' on page 3 undefined on input line 15
3.


LaTeX Warning: Reference `sec:downstream' on page 3 undefined on input line 154
.

[3]

LaTeX Warning: Reference `tab:ablation' on page 4 undefined on input line 177.


LaTeX Warning: Reference `tab:h1h2' on page 4 undefined on input line 181.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:length' on page 4 undefined on input line 230.


LaTeX Warning: Reference `tab:length_features' on page 4 undefined on input lin
e 231.

[4]

LaTeX Warning: Reference `tab:logo' on page 5 undefined on input line 278.

[5]

LaTeX Warning: Reference `tab:lofo' on page 6 undefined on input line 297.


LaTeX Warning: Reference `tab:ref_corr' on page 6 undefined on input line 320.


LaTeX Warning: Reference `tab:ref_class' on page 6 undefined on input line 339.



LaTeX Warning: Reference `tab:stability' on page 6 undefined on input line 342.



LaTeX Warning: Reference `sec:length' on page 6 undefined on input line 343.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:scale' on page 6 undefined on input line 367.

[6]

LaTeX Warning: Reference `tab:ppl_range' on page 7 undefined on input line 390.



Package natbib Warning: Citation `gerstgrasser2024model' on page 7 undefined on
 input line 411.

[7]

LaTeX Warning: Reference `tab:prompt' on page 8 undefined on input line 435.


LaTeX Warning: Reference `tab:prompt_transfer' on page 8 undefined on input lin
e 439.


LaTeX Warning: Reference `tab:para' on page 8 undefined on input line 457.


LaTeX Warning: Reference `tab:crossmodel' on page 8 undefined on input line 478
.


LaTeX Warning: `h' float specifier changed to `ht'.

[8]

LaTeX Warning: Reference `tab:domain' on page 9 undefined on input line 504.


LaTeX Warning: Reference `tab:ordinal' on page 9 undefined on input line 532.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:edits' on page 9 undefined on input line 578.

[9]

Package natbib Warning: Citation `tulchinskii2024ldscore' on page 10 undefined 
on input line 588.


LaTeX Warning: Reference `tab:e2e' on page 10 undefined on input line 607.


LaTeX Warning: Reference `tab:downstream' on page 10 undefined on input line 61
4.


LaTeX Warning: `h' float specifier changed to `ht'.

[10]

Package natbib Warning: Citation `gerstgrasser2024model' on page 11 undefined o
n input line 659.

[11] [12]

Package natbib Warning: There were undefined citations.

[13] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1095
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1095
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1095.mf
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
(some charht values had to be adjusted by as much as 0.06952pt)
Font metrics written on tcrm1095.tfm.
Output written on tcrm1095.600gf (128 characters, 25592 bytes).
Transcript written on tcrm1095.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk: successfully generated.


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
amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (13 pages, 188769 bytes).
Transcript written on paper.log.
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))
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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}]
Overfull \hbox (1.48647pt too wide) in paragraph at lines 62--63
[]\OT1/cmr/bx/n/10.95 Comprehensive lim-i-ta-tion anal-y-sis\OT1/cmr/m/n/10.95 
: We doc-u-ment fail-ure modes in-clud-ing cross-generator
[2] [3] [4]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[5]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[6]

LaTeX Warning: `h' float specifier changed to `ht'.

[7]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[8]

LaTeX Warning: `h' float specifier changed to `ht'.

[9] [10] [11] [12] [13] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (13 pages, 193739 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cf1921f-fa44-4abd-974d-73ed2fce5722",
  "isSidechain": false,
  "promptId": "64b0831c-d266-495e-8b02-943588d3f051",
  "type": "user",
  "uuid": "ac56db94-0acd-418e-aab2-a7c74d43dffb",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `mitchell2023detectgpt' on page 1 undefined on\n input line 46.\n\n\nPackage natbib Warning: Citation `bao2024fastdetectgpt' on page 1 undefined on \ninput line 46.\n\n\nPackage natbib Warning: Citation `hans2024binoculars' on page 1 undefined on in\nput line 46.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (1.48647pt too wide) in paragraph at lines 62--63\n[]\\OT1/cmr/bx/n/10.95 Comprehensive lim-i-ta-tion anal-y-sis\\OT1/cmr/m/n/10.95 \n: We doc-u-ment fail-ure modes in-clud-ing cross-generator\n\nPackage natbib Warning: Citation `gehrmann2019gltr' on page 2 undefined on inpu\nt line 71.\n\n\nPackage natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on\n input line 71.\n\n\nPackage natbib Warning: Citation `bao2024fastdetectgpt' on page 2 undefined on \ninput line 71.\n\n\nPackage natbib Warning: Citation `hans2024binoculars' on page 2 undefined on in\nput line 71.\n\n\nPackage natbib Warning: Citation `solaiman2019release' on page 2 undefined on i\nnput line 71.\n\n\nPackage natbib Warning: Citation `uchendu2020authorship' on page 2 undefined on\n input line 71.\n\n\nPackage natbib Warning: Citation `kirchenbauer2023watermark' on page 2 undefine\nd on input line 71.\n\n\nPackage natbib Warning: Citation `tulchinskii2024ldscore' on page 2 undefined o\nn input line 71.\n\n\nPackage natbib Warning: Citation `alemohammad2024selfconsuming' on page 2 undef\nined on input line 75.\n\n\nPackage natbib Warning: Citation `shumailov2024curse' on page 2 undefined on in\nput line 75.\n\n\nPackage natbib Warning: Citation `dohmatob2024model' on page 2 undefined on inp\nut line 75.\n\n\nPackage natbib Warning: Citation `gerstgrasser2024model' on page 2 undefined on\n input line 75.\n\n\nPackage natbib Warning: Citation `briesch2023attractor' on page 2 undefined on \ninput line 76.\n\n\nPackage natbib Warning: Citation `xie2023dsir' on page 2 undefined on input lin\ne 80.\n\n\nPackage natbib Warning: Citation `wettig2024qurating' on page 2 undefined on in\nput line 80.\n\n\nPackage natbib Warning: Citation `wenzek2020ccnet' on page 2 undefined on input\n line 80.\n\n\nPackage natbib Warning: Citation `guo2024curious' on page 2 undefined on input \nline 84.\n\n\nPackage natbib Warning: Citation `padmakumar2024does' on page 2 undefined on in\nput line 84.\n\n\nPackage natbib Warning: Citation `holtzman2020curious' on page 2 undefined on i\nnput line 84.\n\n\nLaTeX Warning: Reference `sec:ordinal' on page 2 undefined on input line 102.\n\n[2]\n\nLaTeX Warning: Reference `sec:prompt_type' on page 3 undefined on input line 10\n6.\n\n\nLaTeX Warning: Reference `sec:indist' on page 3 undefined on input line 107.\n\n\nLaTeX Warning: Reference `sec:scale' on page 3 undefined on input line 107.\n\n\nLaTeX Warning: Reference `sec:cross_model' on page 3 undefined on input line 10\n7.\n\n\nLaTeX Warning: Reference `sec:e2e' on page 3 undefined on input line 143.\n\n\nLaTeX Warning: Reference `sec:indist' on page 3 undefined on input line 151.\n\n\nLaTeX Warning: Reference `sec:length' on page 3 undefined on input line 151.\n\n\nLaTeX Warning: Reference `sec:scale' on page 3 undefined on input line 152.\n\n\nLaTeX Warning: Reference `sec:cross_gen' on page 3 undefined on input line 153.\n\n\n\nLaTeX Warning: Reference `sec:cross_model' on page 3 undefined on input line 15\n3.\n\n\nLaTeX Warning: Reference `sec:downstream' on page 3 undefined on input line 154\n.\n\n[3]\n\nLaTeX Warning: Reference `tab:ablation' on page 4 undefined on input line 177.\n\n\nLaTeX Warning: Reference `tab:h1h2' on page 4 undefined on input line 181.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:length' on page 4 undefined on input line 230.\n\n\nLaTeX Warning: Reference `tab:length_features' on page 4 undefined on input lin\ne 231.\n\n[4]\n\nLaTeX Warning: Reference `tab:logo' on page 5 undefined on input line 278.\n\n[5]\n\nLaTeX Warning: Reference `tab:lofo' on page 6 undefined on input line 297.\n\n\nLaTeX Warning: Reference `tab:ref_corr' on page 6 undefined on input line 320.\n\n\nLaTeX Warning: Reference `tab:ref_class' on page 6 undefined on input line 339.\n\n\n\nLaTeX Warning: Reference `tab:stability' on page 6 undefined on input line 342.\n\n\n\nLaTeX Warning: Reference `sec:length' on page 6 undefined on input line 343.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:scale' on page 6 undefined on input line 367.\n\n[6]\n\nLaTeX Warning: Reference `tab:ppl_range' on page 7 undefined on input line 390.\n\n\n\nPackage natbib Warning: Citation `gerstgrasser2024model' on page 7 undefined on\n input line 411.\n\n[7]\n\nLaTeX Warning: Reference `tab:prompt' on page 8 undefined on input line 435.\n\n\nLaTeX Warning: Reference `tab:prompt_transfer' on page 8 undefined on input lin\ne 439.\n\n\nLaTeX Warning: Reference `tab:para' on page 8 undefined on input line 457.\n\n\nLaTeX Warning: Reference `tab:crossmodel' on page 8 undefined on input line 478\n.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8]\n\nLaTeX Warning: Reference `tab:domain' on page 9 undefined on input line 504.\n\n\nLaTeX Warning: Reference `tab:ordinal' on page 9 undefined on input line 532.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:edits' on page 9 undefined on input line 578.\n\n[9]\n\nPackage natbib Warning: Citation `tulchinskii2024ldscore' on page 10 undefined \non input line 588.\n\n\nLaTeX Warning: Reference `tab:e2e' on page 10 undefined on input line 607.\n\n\nLaTeX Warning: Reference `tab:downstream' on page 10 undefined on input line 61\n4.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[10]\n\nPackage natbib Warning: Citation `gerstgrasser2024model' on page 11 undefined o\nn input line 659.\n\n[11] [12]\n\nPackage natbib Warning: There were undefined citations.\n\n[13] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf\n Ok [100] [109] [98] [99] [108])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf\n Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]\n[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]\n[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]\n[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]\n[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]\n[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]\n[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf\n Ok [185] [178] [179] [170] [186])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf\n Ok [188] [189] [190]) ) ) )\n(some charht values had to be adjusted by as much as 0.06952pt)\nFont metrics written on tcrm1095.tfm.\nOutput written on tcrm1095.600gf (128 characters, 25592 bytes).\nTranscript written on tcrm1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (13 pages, 188769 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (1.48647pt too wide) in paragraph at lines 62--63\n[]\\OT1/cmr/bx/n/10.95 Comprehensive lim-i-ta-tion anal-y-sis\\OT1/cmr/m/n/10.95 \n: We doc-u-ment fail-ure modes in-clud-ing cross-generator\n[2] [3] [4]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9] [10] [11] [12] [13] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (13 pages, 193739 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1cf1921f-fa44-4abd-974d-73ed2fce5722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerp…",
  "leafUuid": "ac56db94-0acd-418e-aab2-a7c74d43dffb",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth estimation in synthetic text analysis",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6"
}
```

---

### Assistant

_source line 28 · 2026-05-14T22:50:31.444Z_

There's a label resolution issue — need a third pass to fix "Label(s) may have changed."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac56db94-0acd-418e-aab2-a7c74d43dffb",
  "isSidechain": false,
  "requestId": "req_011Cb3H9MAXjj9x1MdJDFwoQ",
  "type": "assistant",
  "uuid": "7d510694-a248-459f-b3a0-1494f2848365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXcwN11sDo5vZAJGvAB5N9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8336,
      "cache_read_input_tokens": 57901,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 57901,
          "cache_creation_input_tokens": 8336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8336
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

_source line 29 · 2026-05-14T22:50:34.281Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012p1yUUMbNEThCEJAK3Urc2`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Third LaTeX pass to resolve cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d510694-a248-459f-b3a0-1494f2848365",
  "isSidechain": false,
  "requestId": "req_011Cb3H9MAXjj9x1MdJDFwoQ",
  "type": "assistant",
  "uuid": "21ebad5b-da29-423f-9679-aabcdeb5f052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXcwN11sDo5vZAJGvAB5N9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8336,
      "cache_read_input_tokens": 57901,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 57901,
          "cache_creation_input_tokens": 8336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8336
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

_source line 30 · 2026-05-14T22:50:34.747Z_

<details><summary>↩ Tool result · `toolu_012p1yUUMbNEThCEJAK3Urc2`</summary>

```text
[8]

LaTeX Warning: `h' float specifier changed to `ht'.

[9] [10] [11] [12] [13] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (13 pages, 193739 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21ebad5b-da29-423f-9679-aabcdeb5f052",
  "isSidechain": false,
  "promptId": "64b0831c-d266-495e-8b02-943588d3f051",
  "type": "user",
  "uuid": "54c3bcd9-0e37-414d-a4b4-b76af3a49d78",
  "toolUseResult": {
    "stdout": "[8]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9] [10] [11] [12] [13] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (13 pages, 193739 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "21ebad5b-da29-423f-9679-aabcdeb5f052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-14T22:50:44.432Z_

PDF 编译成功，13 页，无 undefined reference 警告。

论文已写入 `worst/paper.tex` 并编译为 `worst/paper.pdf`（193KB，13 页）。结构：

- **Reframing**：放弃 dual dynamics 作为主线贡献，改为 (1) 任务定义论文——generation depth estimation 作为新任务，(2) 负面/分析性结果——depth signal 随 generator scale 退化
- **覆盖全部 12 个实验**：Tables 1–22 对应 experiment_data.json 中所有实验，包括 in-distribution baseline、length confound、cross-generator、reference model sensitivity、generator scale、prompt type、paraphrastic comparison、cross-model chains、multi-domain、ordinal granularity、edit robustness、LD-Score/E2E classifier、downstream utility
- **所有数字来自 JSON**，无编造

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54c3bcd9-0e37-414d-a4b4-b76af3a49d78",
  "isSidechain": false,
  "requestId": "req_011Cb3H9pGCWcBAHYRidaSFm",
  "type": "assistant",
  "uuid": "1cad7506-0d1b-46dd-8c7a-6fcf00a6d230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jcYJuJ7LUPPQxsVzWgw9k",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 66237,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 66237,
          "cache_creation_input_tokens": 670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 670
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerp…",
  "leafUuid": "1cad7506-0d1b-46dd-8c7a-6fcf00a6d230",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth estimation in synthetic text analysis",
  "sessionId": "867c85bd-e7b8-4218-bf1a-0cd3207410c6"
}
```

---
