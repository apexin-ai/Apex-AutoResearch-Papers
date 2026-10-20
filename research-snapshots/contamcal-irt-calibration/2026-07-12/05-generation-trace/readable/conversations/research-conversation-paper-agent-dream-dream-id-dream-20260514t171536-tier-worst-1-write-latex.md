# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T171536 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/6654da51-0c7c-47cb-9304-550a11bef3bf.jsonl`
- **Structured JSON:** [`b4dcef342555f81832e6.json`](../../sessions/b4/b4dcef342555f81832e6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T18:16:27.833Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T18:16:27.833Z",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T171536 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：完全 reframe：不再以 calibration tool 为核心。Paper 转为 'Empirical anatomy of contamination signal reliability + diagnostic framework for contamination-aware evaluation'。 三个 salvageable contributions：(1) Min-K++ 方向性反转的系统性实证 (Cohen's d -1.2 to -2.7)； (2) Identifiability boundary analysis 作为理论贡献（告诉社区何时可以/不可以做 contamination-aware calibration）； (3) SFT injection 的 format-learning confound (GSM8K 12%→70% 非 contamination)。 IRT calibration 降为 proof-of-concept with identified failure modes。 仍投 EMNLP 2026 special theme 'New Missions for NLP Research'。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T18:16:27.849Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T18:16:27.849Z",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-14T18:16:28.264Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T171536 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：完全 reframe：不再以 calibration tool 为核心。Paper 转为 'Empirical anatomy of contamination signal reliability + diagnostic framework for contamination-aware evaluation'。 三个 salvageable contributions：(1) Min-K++ 方向性反转的系统性实证 (Cohen's d -1.2 to -2.7)； (2) Identifiability boundary analysis 作为理论贡献（告诉社区何时可以/不可以做 contamination-aware calibration）； (3) SFT injection 的 format-learning confound (GSM8K 12%→70% 非 contamination)。 IRT calibration 降为 proof-of-concept with identified failure modes。 仍投 EMNLP 2026 special theme 'New Missions for NLP Research'。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "017b96e4-f844-4cf2-8554-6d5766cd4c8e",
  "type": "user",
  "uuid": "051c5543-96eb-43e8-af93-f73caff1e1e0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T18:16:28.263Z_

```json
{
  "parentUuid": "051c5543-96eb-43e8-af93-f73caff1e1e0",
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
  "uuid": "0f1e7fe9-d62d-4ad7-934a-493047b4032f",
  "timestamp": "2026-05-14T18:16:28.263Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T18:16:28.264Z_

```json
{
  "parentUuid": "0f1e7fe9-d62d-4ad7-934a-493047b4032f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "edfe3a51-e448-471d-b5f7-955863a90b74",
  "timestamp": "2026-05-14T18:16:28.264Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
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
  "aiTitle": "Generate contamination-aware calibration paper for dream_20260514T171536",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf"
}
```

---

### Assistant

_source line 7 · 2026-05-14T18:16:32.971Z_

I'll start by reading the input files to understand the experimental data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edfe3a51-e448-471d-b5f7-955863a90b74",
  "isSidechain": false,
  "requestId": "req_011Cb2vFV4WpzDL48dTiRBvS",
  "type": "assistant",
  "uuid": "cb682342-44f6-478f-bdff-7734a3c993db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMUniYDDXKCbHhCjb16gUh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11288,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11288
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

_source line 8 · 2026-05-14T18:16:33.948Z_

<details open><summary>🔧 Tool call — Read · `toolu_015mGp26GfVBnw3kHXVRJhhg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb682342-44f6-478f-bdff-7734a3c993db",
  "isSidechain": false,
  "requestId": "req_011Cb2vFV4WpzDL48dTiRBvS",
  "type": "assistant",
  "uuid": "84640ad9-87c4-456c-8481-59d05f3c5f25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMUniYDDXKCbHhCjb16gUh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11288,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11288
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

_source line 9 · 2026-05-14T18:16:34.229Z_

<details open><summary>🔧 Tool call — Read · `toolu_0178hPXx2zJPQoMUzkbQzD1T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84640ad9-87c4-456c-8481-59d05f3c5f25",
  "isSidechain": false,
  "requestId": "req_011Cb2vFV4WpzDL48dTiRBvS",
  "type": "assistant",
  "uuid": "075be811-3d60-4f26-bd1d-1c1fed764727",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMUniYDDXKCbHhCjb16gUh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11288,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11288
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

_source line 10 · 2026-05-14T18:16:34.266Z_

<details><summary>↩ Tool result · `toolu_0178hPXx2zJPQoMUzkbQzD1T`</summary>

```text
1	# Paper Framing — contamcal-irt-calibration
2	
3	## Target Venue
4	- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)
5	- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)
6	- Track: Machine Learning for NLP / Resources and Evaluation
7	- Aligns with EMNLP 2026 special theme "New Missions for NLP Research" (explicitly invites contamination/data governance work)
8	
9	## Core Insight
10	When benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.
11	
12	## Core Claims (3 条)
13	
14	1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B) within the Qwen2.5 family and 4 benchmarks. (Multi-family generalization is a rebuttal-ready extension via exp-014, not initial submission scope.)
15	
16	2. **Signal Effectiveness & Aggregation Claim**: Detection signal effectiveness is method-specific and scale-dependent. Systematic signal × scale × dosage AUC mapping reveals: embedding-based similarity is robust (AUC>0.95 at d005/0.5B), while Min-K++ and Self-Critique fail at small model scales (AUC≈0.5 at 0.5B). Critically, Min-K++ exhibits directional reversal at high contamination (Cohen's d = -1.2 to -2.7 at d100) — it actively misleads rather than merely failing, strengthening the case for robust aggregation. RRF fusion degrades to dominant-signal mode when constituent signals fail — honest characterization of this regime is itself a contribution. Training-free RRF remains the principled aggregation design choice (meta-circularity argument). Paper must distinguish item-level detection (within-model AUC) from model-level detection (cross-model Cohen's d). (RL regime survival deferred to exp-009 observational study; no RL-specific claims until data available.)
17	   **C2 contingency (Reviewer WARNING)**: "Scale-dependent" is currently unverified — only 0.5B data exists. If 1.5B/3B signal data shows S2/S4 remain ineffective → downgrade to "method-specific signal effectiveness" (drop "scale-dependent"), RRF discussion moves to Limitations. Min-K++ directional reversal + item-vs-model detection distinction remain novel regardless of scale outcome.
18	
19	3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — Models with high-AUC signals get tighter CIs; those with degraded signals (small scale or post-RL) get appropriately wider CIs reflecting genuine epistemic uncertainty.
20	
21	## Contributions (Hierarchical)
22	
23	### Core
24	1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals
25	2. Signal effectiveness characterization: systematic signal × scale × dosage AUC mapping revealing method-specific, scale-dependent signal reliability — an empirically novel finding with actionable guidance for the detection community (elevated from Supporting per Dream review; reframed from 'cliff-like RL degradation' per D022)
26	3. Dual-track validation: controlled SFT injection across multiple model scales within the Qwen2.5 family (internal validity) + ecological RL case study (external validity)
27	
28	### Supporting
29	4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds
30	5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology
31	
32	## Story Spine
33	- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering "what would this model's score be if it had never seen the test data?"
34	- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.
35	- **Our framing**: ContamCal is a "statistical safety net" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (different training regimes and model scales require method-aware, scale-aware signal selection).
36	- **Headline result template**: "On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage."
37	
38	## Venue Fit Risks
39	- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).
40	- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.
41	- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as "new algorithm" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.
42	- **RL limitation**: RL models get wide CIs. This is honest — frame as "calibration is only as good as its inputs." Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).
43	
44	## Anticipated Reviewer Concerns & Defenses
45	
46	| # | Concern | Defense | Experiment |
47	|---|---------|---------|------------|
48	| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |
49	| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |
50	| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is "best-available proxy", acknowledged as limitation | exp-006, exp-009 |
51	| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |
52	| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |
53	| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |
54	| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |
55	| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |
56	| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |
57	| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |
58	| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |
59	| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |
60	| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |
61	| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |
62	
63	## Evaluation Protocol (5 Metrics)
64	1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs
65	2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals
66	3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)
67	4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings
68	5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage
69	
70	## Benchmarks (3 main + 1 appendix)
71	1. **MMLU** — knowledge-intensive multiple-choice (14K items)
72	2. **GSM8K** — mathematical reasoning free-form (~1.3K items)
73	3. **ARC-Challenge** — science reasoning multiple-choice
74	4. **HumanEval** (appendix only) — code generation with execution evaluation (N=164). Demoted: paraphrase QC pass rate only 16% (26/164) due to fundamental difficulty of code paraphrasing; insufficient for reliable 4PL estimation (D009).
75	
76	## Baselines (7)
77	0. **Raw (no adjustment)** — report original benchmark scores as anchor
78	1. **Remove-and-rescore** — drop flagged items, rescore on remaining
79	2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT
80	3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)
81	4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)
82	5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)
83	6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare
84	
85	## Local Independence Discussion
86	Standard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.
87	
88	## Required Figures (Dream D2: "zero figures" flagged as serious deficiency)
89	1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)
90	2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022
91	3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)
92	4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)
93	5. Calibrated-vs-true accuracy scatter with CIs (exp-006)
94	
95	## Citation Requirements (35+ minimum, expanded per Dream D2)
96	Must include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.
97	Dream D2 additions (all 3 tiers flagged):
98	- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)
99	- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate "calibration" — ours is decontamination, not probability calibration)
100	- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)
101	- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work
102	- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)
103	
104	## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)
105	Must derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.
106	The derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.
107	This is CPU-only theoretical work — can be done in parallel with GPU experiments.
108	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "075be811-3d60-4f26-bd1d-1c1fed764727",
  "isSidechain": false,
  "promptId": "017b96e4-f844-4cf2-8554-6d5766cd4c8e",
  "type": "user",
  "uuid": "ed0d1cbb-002c-4f76-b2fd-2de50cc9dff8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/paper_framing.md",
      "content": "# Paper Framing — contamcal-irt-calibration\n\n## Target Venue\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\n- Track: Machine Learning for NLP / Resources and Evaluation\n- Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" (explicitly invites contamination/data governance work)\n\n## Core Insight\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.\n\n## Core Claims (3 条)\n\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B) within the Qwen2.5 family and 4 benchmarks. (Multi-family generalization is a rebuttal-ready extension via exp-014, not initial submission scope.)\n\n2. **Signal Effectiveness & Aggregation Claim**: Detection signal effectiveness is method-specific and scale-dependent. Systematic signal × scale × dosage AUC mapping reveals: embedding-based similarity is robust (AUC>0.95 at d005/0.5B), while Min-K++ and Self-Critique fail at small model scales (AUC≈0.5 at 0.5B). Critically, Min-K++ exhibits directional reversal at high contamination (Cohen's d = -1.2 to -2.7 at d100) — it actively misleads rather than merely failing, strengthening the case for robust aggregation. RRF fusion degrades to dominant-signal mode when constituent signals fail — honest characterization of this regime is itself a contribution. Training-free RRF remains the principled aggregation design choice (meta-circularity argument). Paper must distinguish item-level detection (within-model AUC) from model-level detection (cross-model Cohen's d). (RL regime survival deferred to exp-009 observational study; no RL-specific claims until data available.)\n   **C2 contingency (Reviewer WARNING)**: \"Scale-dependent\" is currently unverified — only 0.5B data exists. If 1.5B/3B signal data shows S2/S4 remain ineffective → downgrade to \"method-specific signal effectiveness\" (drop \"scale-dependent\"), RRF discussion moves to Limitations. Min-K++ directional reversal + item-vs-model detection distinction remain novel regardless of scale outcome.\n\n3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — Models with high-AUC signals get tighter CIs; those with degraded signals (small scale or post-RL) get appropriately wider CIs reflecting genuine epistemic uncertainty.\n\n## Contributions (Hierarchical)\n\n### Core\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals\n2. Signal effectiveness characterization: systematic signal × scale × dosage AUC mapping revealing method-specific, scale-dependent signal reliability — an empirically novel finding with actionable guidance for the detection community (elevated from Supporting per Dream review; reframed from 'cliff-like RL degradation' per D022)\n3. Dual-track validation: controlled SFT injection across multiple model scales within the Qwen2.5 family (internal validity) + ecological RL case study (external validity)\n\n### Supporting\n4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds\n5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology\n\n## Story Spine\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \"what would this model's score be if it had never seen the test data?\"\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\n- **Our framing**: ContamCal is a \"statistical safety net\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (different training regimes and model scales require method-aware, scale-aware signal selection).\n- **Headline result template**: \"On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage.\"\n\n## Venue Fit Risks\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \"new algorithm\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \"calibration is only as good as its inputs.\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\n\n## Anticipated Reviewer Concerns & Defenses\n\n| # | Concern | Defense | Experiment |\n|---|---------|---------|------------|\n| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \"best-available proxy\", acknowledged as limitation | exp-006, exp-009 |\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\n| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\n\n## Evaluation Protocol (5 Metrics)\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\n\n## Benchmarks (3 main + 1 appendix)\n1. **MMLU** — knowledge-intensive multiple-choice (14K items)\n2. **GSM8K** — mathematical reasoning free-form (~1.3K items)\n3. **ARC-Challenge** — science reasoning multiple-choice\n4. **HumanEval** (appendix only) — code generation with execution evaluation (N=164). Demoted: paraphrase QC pass rate only 16% (26/164) due to fundamental difficulty of code paraphrasing; insufficient for reliable 4PL estimation (D009).\n\n## Baselines (7)\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\n\n## Local Independence Discussion\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\n\n## Required Figures (Dream D2: \"zero figures\" flagged as serious deficiency)\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\n2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\n\n## Citation Requirements (35+ minimum, expanded per Dream D2)\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\nDream D2 additions (all 3 tiers flagged):\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \"calibration\" — ours is decontamination, not probability calibration)\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\n\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\n",
      "numLines": 108,
      "startLine": 1,
      "totalLines": 108
    }
  },
  "sourceToolAssistantUUID": "075be811-3d60-4f26-bd1d-1c1fed764727",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T18:16:34.335Z_

<details><summary>↩ Tool result · `toolu_015mGp26GfVBnw3kHXVRJhhg`</summary>

```text
1	[
2	  {
3	    "name": "stage1_signal_pipeline",
4	    "description": "对 exp-001 所有 contaminated + clean models 计算 4 个 detection signals。 0.5B 已有部分数据 (exp_002_signals_05B DONE)，需扩展到 1.5B/3B 全 dosage。\n",
5	    "results": {
6	      "S1_emb_d005_auc_05B_mmlu": 0.953,
7	      "S1_emb_d005_auc_05B_gsm8k": 0.988,
8	      "S1_emb_d005_auc_05B_arc": 0.995,
9	      "S1_emb_d025_auc_05B_mmlu": 0.51,
10	      "S1_emb_d025_auc_05B_gsm8k": 0.52,
11	      "S1_emb_d025_auc_05B_arc": 0.5,
12	      "S1_emb_d100_auc_05B_mmlu": 0.494,
13	      "S2_minkpp_d005_auc_05B_mean": 0.465,
14	      "S3_constat_d005_auc_05B_mean": 0.53,
15	      "S4_selfcrit_d005_auc_05B_mean": 0.48,
16	      "S1_emb_d005_auc_15B_mmlu": 0.96,
17	      "S1_emb_d005_auc_15B_gsm8k": 0.99,
18	      "S1_emb_d005_auc_15B_arc": 0.99,
19	      "S1_emb_d025_auc_15B_mmlu": 0.52,
20	      "S2_minkpp_d005_auc_15B_mean": 0.5,
21	      "S3_constat_d005_auc_15B_mean": 0.54,
22	      "S4_selfcrit_d005_auc_15B_mean": 0.52,
23	      "S1_emb_d005_auc_3B_mmlu": 0.97,
24	      "S1_emb_d005_auc_3B_gsm8k": 0.99,
25	      "S1_emb_d005_auc_3B_arc": 0.99,
26	      "S1_emb_d025_auc_3B_mmlu": 0.53,
27	      "S2_minkpp_d005_auc_3B_mean": 0.51,
28	      "S3_constat_d005_auc_3B_mean": 0.55,
29	      "S4_selfcrit_d005_auc_3B_mean": 0.53,
30	      "S1_emb_d100_auc_all_scales_mean": 0.5,
31	      "S2_minkpp_d100_cross_cohens_d_mean": -1.98
32	    },
33	    "tables": [
34	      {
35	        "name": "Table: Signal × Scale × Dosage AUC Matrix",
36	        "description": "4 signals × 3 scales × 4 dosages 的完整 AUC 矩阵。仅 S1-d005 一行高亮为有效 (AUC > 0.90)。其余全部灰色 (0.45-0.55)。最右列为 cross-model Cohen's d (d100)。\n",
37	        "data": "Signal | Scale | d005 AUC | d025 AUC | d100 AUC | d100 Cohen's d S1-Emb | 0.5B  | 0.979    | 0.51     | 0.49     | +3.6 S1-Emb | 1.5B  | 0.98     | 0.52     | 0.50     | +4.1 S1-Emb | 3B    | 0.98     | 0.53     | 0.50     | +3.8 S2-MKP | 0.5B  | 0.465    | 0.48     | 0.50     | -1.98 S2-MKP | 1.5B  | 0.50     | 0.49     | 0.51     | -2.3 S2-MKP | 3B    | 0.51     | 0.50     | 0.50     | -2.7 S3-CS  | 0.5B  | 0.53     | 0.51     | 0.50     | +0.3 S3-CS  | 1.5B  | 0.54     | 0.52     | 0.50     | +0.4 S3-CS  | 3B    | 0.55     | 0.52     | 0.51     | +0.5 S4-SC  | 0.5B  | 0.48     | 0.49     | 0.50     | +0.45 S4-SC  | 1.5B  | 0.52     | 0.50     | 0.50     | +0.5 S4-SC  | 3B    | 0.53     | 0.51     | 0.50     | +0.6\n"
38	      }
39	    ],
40	    "figures": [],
41	    "analysis": "\"scale-dependent\" claim 在 worst 档下彻底失败：S2/S4 在 1.5B/3B 仍然 ≈ random。 必须 downgrade C2 为 \"method-specific signal effectiveness\"，删除 \"scale-dependent\"。 但这反而强化了另一个 narrative：signal failure 不是偶然的——它是 SFT paraphrase contamination 这种 contamination modality 下 detection 方法的系统性盲区。这本身是一个有价值的 negative finding。 RRF discussion 整体移入 Limitations，因为 aggregation 毫无意义（只有一个 effective signal）。\n\n\nworst 档的核心假设是 signal landscape 极度退化。S1 (embedding similarity) 在 d005 有效是因为 仅 5% items 被污染时，contaminated vs clean 的 embedding 距离差异明确可分。但在 d025/d100， 因为绝大部分 items 都被污染，labeling artifact 使得 \"contaminated\" 和 \"clean\" 标签失去鉴别力 — 所有 items 都 exposed，AUC → 0.50。S2 (Min-K++) 在所有 scale 下均失效：0.5B 模型的 perplexity landscape 太 noisy 无法区分 seen/unseen；1.5B/3B 虽然 perplexity 更 stable，但 SFT 后 paraphrased items 的 perplexity 并不系统性低于 unseen items（paraphrase ≠ verbatim memorization）。 S4 (Self-Critique) 依赖模型 introspection 能力，小模型 (≤3B) 的 self-knowledge 不足以 区分 \"我见过这道题的变体\" 和 \"这道题本身就简单\"。S3 (ConStat) 需要 original vs paraphrased performance gap，但 SFT contamination 不产生稳定的 original > paraphrase gap（不像 verbatim memorization）。\"scale-dependent\" 假设在 worst 档下被证伪——S2/S4 在 1.5B/3B 仍然无效，问题不是 scale 而是方法本身在 SFT paraphrase contamination 下的根本局限。\n"
42	  },
43	  {
44	    "name": "rrf_aggregation_ablation",
45	    "description": "RRF fusion of 4 signals。在 worst 档下，实质测试 \"单信号 S1 vs 4-signal RRF\"。\n",
46	    "results": {
47	      "rrf_4signal_auc_d005_05B_mean": 0.82,
48	      "rrf_4signal_auc_d005_15B_mean": 0.83,
49	      "rrf_4signal_auc_d005_3B_mean": 0.84,
50	      "s1_only_auc_d005_mean": 0.979,
51	      "rrf_vs_s1_auc_delta": -0.15,
52	      "rank_avg_4signal_auc_d005_mean": 0.78,
53	      "rrf_2signal_closed_auc_d005_mean": 0.54,
54	      "fp_injection_robustness_auc_drop": 0.08,
55	      "rrf_effective_weight_on_s1": 0.92
56	    },
57	    "tables": [
58	      {
59	        "name": "Table: RRF Ablation — Aggregation Method × Signal Subset",
60	        "description": "行: {RRF-4, RRF-2-closed, Rank-Avg-4, S1-only, S2-only, S3-only, S4-only} 列: {d005 AUC (mean±std across scales), d025 AUC, d100 AUC}\n",
61	        "data": "Method           | d005 AUC      | d025 AUC | d100 AUC RRF-4signal      | 0.83 ± 0.01   | 0.52     | 0.50 RRF-2-closed     | 0.54 ± 0.02   | 0.51     | 0.50 Rank-Avg-4       | 0.78 ± 0.02   | 0.51     | 0.50 S1-only          | 0.979 ± 0.005 | 0.52     | 0.50 S2-only          | 0.49 ± 0.03   | 0.49     | 0.50 S3-only          | 0.54 ± 0.02   | 0.52     | 0.50 S4-only          | 0.51 ± 0.03   | 0.50     | 0.50\n"
62	      }
63	    ],
64	    "figures": [],
65	    "analysis": "RRF 不仅不是贡献——它实际上 hurts performance。这 destroys C2 中 'principled aggregation' 的 claim。但 meta-circularity argument 仍然成立（不能用 contaminated data 学 weights）。 Paper 应该诚实报告：RRF 在 signal-rich regime 有理论优势，但在当前 empirical setting (仅 1/4 signals 有效) 下退化为 single-signal mode 且有 dilution penalty。 这是一个关于 aggregation failure mode 的实证贡献，属于 diagnostic framework 的一部分。\n\n\n当 3/4 signals 为 random noise (AUC ≈ 0.50) 时，RRF fusion 实际上 dilutes 唯一有效的 S1 信号。4-signal RRF AUC < S1-only AUC，因为三个 noise signals 的 random rankings 会扰乱 S1 的 correct ranking。这是 RRF 的已知弱点：它假设所有 constituent signals 至少 weakly informative。当大部分 signals 是 pure noise， fusion 不如 oracle selection。但 S1 仍然 dominant——RRF 的 reciprocal rank 机制 使得 S1 的 strong signal 部分 survive（不会降到 random），只是被 attenuated。 2-signal closed-weight mode (ConStat + Self-Critique only) 完全无效 (AUC ≈ 0.54) 因为两个 constituent 都是 noise。FP injection 进一步降低 effective AUC，但已经 near-random baseline 所以 absolute drop 有限。\n"
66	  },
67	  {
68	    "name": "irt_calibration_and_baselines",
69	    "description": "核心 calibration 实验。4PL+γ IRT vs 7 baselines。worst 档下此实验是 \"主要 negative result\"。\n",
70	    "results": {
71	      "calibration_MAE_pp_4pl_gamma_mmlu": 7.2,
72	      "calibration_MAE_pp_4pl_gamma_gsm8k": 11.5,
73	      "calibration_MAE_pp_4pl_gamma_arc": 6.8,
74	      "calibration_MAE_pp_4pl_gamma_humaneval": 9.3,
75	      "calibration_MAE_pp_4pl_gamma_mean": 8.7,
76	      "calibration_MAE_pp_linear_reg_mmlu": 6.8,
77	      "calibration_MAE_pp_linear_reg_gsm8k": 10.2,
78	      "calibration_MAE_pp_linear_reg_arc": 6.5,
79	      "calibration_MAE_pp_linear_reg_humaneval": 8.9,
80	      "calibration_MAE_pp_linear_reg_mean": 8.1,
81	      "mae_diff_4pl_vs_linear_pp": 0.6,
82	      "mae_diff_bootstrap_p_value": 0.38,
83	      "mae_diff_bootstrap_95ci": "[-1.2, 2.4]",
84	      "CI_coverage_95_4pl_gamma": 0.72,
85	      "CI_coverage_80_4pl_gamma": 0.58,
86	      "CI_coverage_50_4pl_gamma": 0.35,
87	      "CI_coverage_95_linear_bootstrap": 0.78,
88	      "CI_width_avg_pp_4pl_gamma": 18.5,
89	      "CI_width_avg_pp_linear_bootstrap": 14.2,
90	      "kendall_tau_4pl_gamma": 0.65,
91	      "kendall_tau_linear_reg": 0.68,
92	      "kendall_tau_raw": 0.72,
93	      "kendall_tau_remove_rescore": 0.6,
94	      "dose_response_monotonicity_mmlu": 0.55,
95	      "dose_response_monotonicity_gsm8k": 0.4,
96	      "dose_response_monotonicity_arc": 0.65,
97	      "gamma_mmlu_mean": 0.12,
98	      "gamma_mmlu_95ci": "[-0.05, 0.29]",
99	      "gamma_gsm8k_mean": 0.45,
100	      "gamma_gsm8k_95ci": "[0.08, 0.82]",
101	      "gamma_arc_mean": 0.08,
102	      "gamma_arc_95ci": "[-0.10, 0.26]",
103	      "gamma_humaneval_mean": 0.15,
104	      "gamma_humaneval_95ci": "[-0.12, 0.42]",
105	      "MAE_raw_no_adjustment": 4.2,
106	      "MAE_remove_rescore": 7.5,
107	      "MAE_single_signal_2pl": 9.1,
108	      "MAE_vanilla_4pl_no_gamma": 5.8,
109	      "MAE_emperor_rephrase": 5.5,
110	      "MAE_dcr_fuzzy": 6.2,
111	      "max_rhat": 1.02,
112	      "min_ess_bulk": 380,
113	      "divergent_transitions_pct": 2.5,
114	      "posterior_pred_check_p_value": 0.03,
115	      "local_independence_residual_corr": 0.18,
116	      "joint_gamma_global_mean": 0.15,
117	      "joint_gamma_global_95ci": "[-0.02, 0.32]"
118	    },
119	    "tables": [
120	      {
121	        "name": "Table: Main Calibration Results — 7 Baselines + ContamCal",
122	        "description": "8 methods × 5 metrics (MAE, Coverage-95, Width, Kendall τ, Monotonicity)。 Bold = best per column。Worst 档下 Raw (no adjustment) wins on MAE 和 τ。\n",
123	        "data": "Method                    | MAE (pp)↓  | Cov-95↑ | Width (pp)↓ | τ↑    | Mono↑ Raw (no adjustment)       | 4.2 ± 1.8  | N/A     | N/A         | 0.72  | N/A Remove-and-rescore        | 7.5 ± 2.3  | N/A     | N/A         | 0.60  | N/A Single-signal 2PL+γ      | 9.1 ± 3.1  | 0.65    | 22.0        | 0.58  | 0.48 Vanilla 4PL (γ=0)        | 5.8 ± 2.0  | 0.82    | 16.5        | 0.70  | N/A Linear reg + bootstrap   | 8.1 ± 2.5  | 0.78    | 14.2        | 0.68  | 0.55 Emperor (rephrase+shuf)  | 5.5 ± 2.2  | N/A     | N/A         | 0.70  | N/A DCR fuzzy                | 6.2 ± 2.4  | N/A     | N/A         | 0.66  | N/A ContamCal 4PL+γ (ours)   | 8.7 ± 3.0  | 0.72    | 18.5        | 0.65  | 0.53\n"
124	      },
125	      {
126	        "name": "Table: Per-benchmark γ_k Estimates",
127	        "description": "γ_k posterior summaries per benchmark。大部分 CI 包含零。\n",
128	        "data": "Benchmark  | γ_k mean | 95% CI          | CI excludes 0? | Interpretation MMLU       | 0.12     | [-0.05, 0.29]   | No             | Weak, non-significant GSM8K      | 0.45     | [0.08, 0.82]    | Yes            | Confounded with format learning ARC        | 0.08     | [-0.10, 0.26]   | No             | Negligible HumanEval  | 0.15     | [-0.12, 0.42]   | No             | High uncertainty\n"
129	      }
130	    ],
131	    "figures": [],
132	    "analysis": "这是论文中最重要的 negative result。关键 insight 不是 \"IRT calibration doesn't work\" 而是 \"IRT calibration 需要足够大的 contamination effect 和足够好的 detection signals 才能 work， 当前 SFT injection paradigm 下这两个前提均不满足\"。具体的 failure mode analysis： (a) Catastrophic forgetting at 0.5B 使 contamination 净效应为负 → γ 需要建模负向效应但 prior 偏正； (b) Format learning confound at 3B GSM8K → γ 过估；(c) Exposure noise dilution → posterior 过宽。 Paper 应该将此定位为 \"identifiability boundary 的 empirical validation\" —— simulation (exp-004) 说 AUC≥0.80 时 γ 可 recover，real data 确认 AUC≈0.50 时不行。\n\n\nworst 档的核心 negative result：4PL+γ 的 calibration MAE 与 linear regression + bootstrap CI 无统计显著差异 (p=0.38)。原因链：(1) contamination effect size 在 0.5B 上是 NEGATIVE (d005 MMLU 从 0.40 降到 0.33，即 SFT 本身造成的 catastrophic forgetting > contamination inflation)， IRT 试图估计一个正向 γ 但实际 effect 可能为负或接近零；(2) 仅 S1 在 d005 提供有效 exposure signal， 但 d025/d100 的 exposure scores 全是 noise，导致 γ 的 Fisher Information 极低——posterior 宽到包含零 (MMLU γ CI: [-0.05, 0.29])；(3) GSM8K 的 γ 估计偏高 (0.45) 但主要捕获 format learning 而非 contamination (3B d100 从 12%→70% 的 jump 是 format effect)； (4) CI coverage 72% < 95% nominal 因为 measurement error model 无法完全补偿 exposure noise (3/4 signals 为 noise，latent τ 的 posterior 过于集中)； (5) Raw scores (no adjustment) 的 MAE 反而最低 (4.2pp)，因为在 most conditions contamination effect 很小——adjustment 引入了比 signal 更多的 noise； (6) Kendall τ 排名也是 raw scores 最高 (0.72)——calibration 反而扰乱了正确的排名。 这是一个令人沮丧但 informative 的结果：当 contamination effect 小于 SFT noise floor， 且 detection signals 大部分失效时，任何 post-hoc calibration 都不如不做。\n"
133	  },
134	  {
135	    "name": "signal_survival_analysis",
136	    "description": "Systematic signal reliability across scales and regimes。0.5B 数据已有。 worst 档下扩展到 1.5B/3B 仍不改善 S2/S4。\n",
137	    "results": {
138	      "S1_d005_auc_05B": 0.979,
139	      "S1_d005_auc_15B": 0.98,
140	      "S1_d005_auc_3B": 0.98,
141	      "S2_d005_auc_05B": 0.465,
142	      "S2_d005_auc_15B": 0.5,
143	      "S2_d005_auc_3B": 0.51,
144	      "S4_d005_auc_05B": 0.48,
145	      "S4_d005_auc_15B": 0.52,
146	      "S4_d005_auc_3B": 0.53,
147	      "S1_d100_cohens_d_05B": 3.6,
148	      "S1_d100_cohens_d_15B": 4.1,
149	      "S1_d100_cohens_d_3B": 3.8,
150	      "S2_d100_cohens_d_05B": -1.98,
151	      "S2_d100_cohens_d_15B": -2.3,
152	      "S2_d100_cohens_d_3B": -2.7,
153	      "S4_d100_cohens_d_05B": 0.45,
154	      "S4_d100_cohens_d_15B": 0.5,
155	      "S4_d100_cohens_d_3B": 0.6,
156	      "S1_instruct_auc_d005_mean": 0.92,
157	      "S2_instruct_auc_d005_mean": 0.48,
158	      "S4_instruct_auc_d005_mean": 0.5,
159	      "effective_signals_all_scales": 1,
160	      "minkpp_reversal_confirmed_all_scales": true,
161	      "scale_dependency_hypothesis": "rejected"
162	    },
163	    "tables": [
164	      {
165	        "name": "Table: Signal Effectiveness Summary — Scale × Method",
166	        "description": "Condensed version of the full heatmap for paper's main text",
167	        "data": "Signal   | 0.5B d005 | 1.5B d005 | 3B d005 | Scale effect? | d100 reversal? S1 Emb   | 0.979     | 0.98      | 0.98    | None (stable) | No (+3.6 to +4.1) S2 MK++  | 0.465     | 0.50      | 0.51    | None          | YES (-2.0 to -2.7) S3 CS    | 0.53      | 0.54      | 0.55    | Marginal      | No S4 SC    | 0.48      | 0.52      | 0.53    | Marginal      | No\n"
168	      }
169	    ],
170	    "figures": [],
171	    "analysis": "Min-K++ reversal 是 worst 档下最有价值的独立 finding。它不依赖 IRT calibration 是否 work。 Cohen's d 在 -1.2 to -2.7 范围内表示 medium-to-large 反向效应——这意味着任何使用 Min-K++ 做 contamination detection 的研究在 high-dosage SFT contamination 下 不仅会 miss contamination，还会系统性地 flag clean items as contaminated。 这对整个 detection 社区有重要 implication，值得独立成 section。 \"Scale-dependent\" claim 被 downgrade 为 \"method-specific\"，C2 contingency 触发。\n\n\nworst 档下 \"scale-dependent\" 假设被证伪。S2 (Min-K++) 的 failure 不是 scale 问题而是 方法论问题：paraphrased contamination 不产生 verbatim memorization 的 perplexity signature。 即使 3B 模型有更 stable 的 perplexity estimates，contaminated items 的 perplexity 并不系统性低于 clean items，因为 SFT 训练的是 paraphrase 而非 original。Min-K++ 的 方向性反转在 larger scales 更显著 (Cohen's d 从 -1.98 到 -2.7)——因为 larger models 在 d100 下更多地学到 general format patterns，反而使 original items \"看起来更 surprised\" (higher perplexity for original = negative min-k++ score)。S4 (Self-Critique) 的 introspection 能力虽然随 scale 略增但远不足以达到 item-level discrimination (AUC ≈ 0.53)。 Instruct models 作为 RL proxy 显示 S1 仍然有效 (AUC 0.92) 但略低于 base+SFT， 可能因为 RL alignment 改变了 embedding space geometry。\n"
172	  },
173	  {
174	    "name": "scale_bridging_7b",
175	    "description": "Qwen2.5-7B controlled SFT injection at 5 dosage levels。 worst 档下 larger scale 不解决 fundamental issues。\n",
176	    "results": {
177	      "7B_d000_mmlu": 0.74,
178	      "7B_d000_gsm8k": 0.79,
179	      "7B_d000_arc": 0.88,
180	      "7B_d000_humaneval": 0.35,
181	      "7B_d005_mmlu": 0.73,
182	      "7B_d005_gsm8k": 0.8,
183	      "7B_d005_arc": 0.87,
184	      "7B_d005_delta_mmlu_pp": -1.0,
185	      "7B_d100_mmlu": 0.76,
186	      "7B_d100_gsm8k": 0.85,
187	      "7B_d100_arc": 0.89,
188	      "7B_d100_delta_mmlu_pp": 2.0,
189	      "7B_d100_delta_gsm8k_pp": 6.0,
190	      "S1_d005_auc_7B": 0.98,
191	      "S2_d005_auc_7B": 0.53,
192	      "S4_d005_auc_7B": 0.55,
193	      "S2_d100_cohens_d_7B": -2.5,
194	      "calibration_MAE_7B_pp": 6.5,
195	      "calibration_MAE_linear_7B_pp": 5.8
196	    },
197	    "tables": [
198	      {
199	        "name": "Table: 7B Dose-Response",
200	        "description": "5 dosages × 4 benchmarks accuracy matrix + delta from d000",
201	        "data": "Dosage | MMLU       | GSM8K      | ARC        | HumanEval d000   | 0.74       | 0.79       | 0.88       | 0.35 d005   | 0.73 (-1)  | 0.80 (+1)  | 0.87 (-1)  | 0.34 (-1) d025   | 0.73 (-1)  | 0.81 (+2)  | 0.87 (-1)  | 0.35 (0) d050   | 0.74 (0)   | 0.83 (+4)  | 0.88 (0)   | 0.35 (0) d100   | 0.76 (+2)  | 0.85 (+6)  | 0.89 (+1)  | 0.36 (+1)\n"
202	      }
203	    ],
204	    "figures": [],
205	    "analysis": "7B 的核心 takeaway：contamination effect 在 controlled SFT setting 下太小 (≤6pp GSM8K, ≤2pp MMLU) 且方向不一致。这与 literature 中 verbatim contamination 的 8-15pp inflation 形成鲜明对比。说明 paraphrased contamination (our injection method) 产生的 effect qualitatively different from verbatim leakage。Paper 需要 explicitly discuss 这个 external validity limitation：our SFT injection protocol may underestimate real-world contamination effects，同时也可能说明 paraphrase-level contamination 本身 less impactful than commonly assumed。\n\n\n7B 模型的 baseline 性能更高 (MMLU 0.74)，留给 contamination inflation 的空间更小 (ceiling effect)。d005 的净效应可能为负 (MMLU -1pp) 因为 SFT data 中 5% paraphrase 对 7B 的 forgetting impact 与 0.5B 类似但 base performance 更稳定。d100 的 MMLU 仅 +2pp（而非 8-15pp literature 报告的 verbatim 污染效果）因为 paraphrased contamination 的 inflation 效应弱于 verbatim。GSM8K +6pp 可能仍包含 format learning 分量。 信号方面 S2/S4 仍然无效 (AUC ≈ 0.53-0.55)，confirming scale 不是 root cause。 Calibration MAE 与 linear baseline 无显著差异，与 smaller scales 的 pattern 一致。 7B 数据不改变 worst 档的 narrative——只是在更大 scale 上确认了同样的 failure modes。\n"
206	  },
207	  {
208	    "name": "rl_observational_case_study",
209	    "description": "Apply signals to existing RL-trained models (Qwen2.5-Instruct, DeepSeek-R1-Distill)。 worst 档下 ecological validity 极其有限。\n",
210	    "results": {
211	      "S1_instruct_05B_d005_auc": 0.91,
212	      "S1_instruct_15B_d005_auc": 0.9,
213	      "S1_instruct_3B_d005_auc": 0.89,
214	      "S1_instruct_7B_d005_auc": 0.88,
215	      "S2_instruct_all_auc_range": "[0.46, 0.53]",
216	      "S4_instruct_all_auc_range": "[0.48, 0.54]",
217	      "gamma_instruct_mmlu": 0.05,
218	      "gamma_instruct_mmlu_95ci": "[-0.15, 0.25]",
219	      "gamma_instruct_gsm8k": 0.18,
220	      "gamma_instruct_gsm8k_95ci": "[-0.08, 0.44]",
221	      "gamma_specificity_known_clean_benchmark": 0.02,
222	      "gamma_specificity_ci_covers_zero": true,
223	      "regret_uncalibrated_top5": 0.08,
224	      "regret_calibrated_top5": 0.11,
225	      "regret_remove_rescore_top5": 0.09,
226	      "regret_calibration_worse_than_uncalibrated": true,
227	      "CI_width_instruct_mean_pp": 22.0,
228	      "CI_width_deepseek_mean_pp": 25.0
229	    },
230	    "tables": [
231	      {
232	        "name": "Table: RL Observational — Expected Regret",
233	        "description": "Top-5 model selection regret under 3 methods。Calibration 反而比 raw 更差。\n",
234	        "data": "Selection method      | Mean regret (pp) | Median regret | Worst-case regret Uncalibrated (raw)    | 0.08             | 0.05          | 0.18 ContamCal calibrated  | 0.11             | 0.08          | 0.25 Remove-and-rescore    | 0.09             | 0.06          | 0.20\n"
235	      }
236	    ],
237	    "figures": [],
238	    "analysis": "RL case study 在 worst 档下只能支撑两个 limited claims：(1) specificity — ContamCal 在 known clean benchmark 上不产生 false positive contamination signal (γ≈0, CI covers 0)； (2) S1 embedding signal 在 RL regime 下 partial survival (AUC 0.88-0.91)。 作为 \"external validity\" 几乎完全失败——没有 ground truth 意味着所有结论都是 directional。 Expected regret analysis 反而变成 negative result：calibration hurts model selection。 Paper 中降为短小的 case study section，主要用于展示 \"honest uncertainty propagation\" 的 behavior（CI 随 signal quality 自适应变宽）而非 calibration accuracy。\n\n\nRL models 的 observational analysis 在 worst 档下几乎完全 uninformative： (1) 没有 ground truth (不知道 true contamination level)，所以 γ 估计无法验证； (2) S1 AUC 在 instruct models 上略降 (0.88-0.91 vs SFT 的 0.98) 因为 RL alignment 改变了 embedding space，但仍勉强 above threshold；(3) S2/S4 仍然无效； (4) γ posterior 极宽，所有 CI 包含零——无法 claim 任何 RL model 有 significant contamination； (5) Expected regret analysis 结果 counterintuitive：calibrated ranking 比 uncalibrated 更差 (regret 0.11 vs 0.08) 因为 noisy γ 扰乱了原本 reasonable 的 ranking； (6) CI widths (22-25pp) 太宽以至于 \"honest uncertainty\" 退化为 \"uninformative bounds\"。 Specificity check 是唯一正面结果：known clean benchmark 的 γ 正确地接近零。\n"
239	  },
240	  {
241	    "name": "multi_family_validation",
242	    "description": "Non-Qwen family (Llama-3.2-1B or Pythia-1.4B) at 3 dosages。 worst 档下跨 family 结果不一致。\n",
243	    "results": {
244	      "llama_d000_mmlu": 0.38,
245	      "llama_d000_gsm8k": 0.15,
246	      "llama_d000_arc": 0.42,
247	      "llama_d100_mmlu": 0.35,
248	      "llama_d100_gsm8k": 0.28,
249	      "llama_d100_arc": 0.39,
250	      "llama_d100_delta_mmlu": -3.0,
251	      "S1_llama_d005_auc": 0.94,
252	      "S2_llama_d005_auc": 0.48,
253	      "S2_llama_d100_cohens_d": -1.2,
254	      "gamma_llama_mmlu": -0.05,
255	      "gamma_llama_mmlu_ci": "[-0.28, 0.18]",
256	      "calibration_MAE_llama_pp": 9.5,
257	      "gamma_cross_family_corr": 0.15,
258	      "identifiability_boundary_consistent": false
259	    },
260	    "tables": [
261	      {
262	        "name": "Table: Cross-family Comparison",
263	        "description": "Qwen vs Llama γ estimates and calibration metrics side by side",
264	        "data": "Metric                    | Qwen2.5-0.5B | Llama-3.2-1B | Consistent? d005 MMLU delta (pp)      | -7.0          | -3.0         | Both negative ✓ d100 MMLU delta (pp)      | -8.0          | -3.0         | Both negative ✓ d100 GSM8K delta (pp)     | 0.0           | +13.0        | Inconsistent ✗ γ_MMLU posterior mean     | 0.12          | -0.05        | Sign inconsistent ✗ S1 d005 AUC              | 0.979         | 0.94         | Both high ✓ S2 d100 Cohen's d        | -1.98         | -1.2         | Both reversal ✓ Calibration MAE (pp)     | 8.7           | 9.5          | Similar magnitude\n"
265	      }
266	    ],
267	    "figures": [],
268	    "analysis": "Multi-family validation 在 worst 档下实际上是另一个 negative result——但它的 negative-ness 本身是 informative。结论：contamination effect 是 family-specific 的， 不存在 universal γ parameter。这对 contamination calibration community 是一个 important cautionary finding：任何基于一个 family 训练的 calibration 无法泛化到 另一个 family。Paper 中定位为 Limitations 的 empirical grounding，而非 fatal flaw—— 因为 per-model fitting (不需要跨 family 泛化) 仍然可行，只是 interpretability 降低。 Min-K++ reversal 的 cross-family 一致性 (both negative Cohen's d) 是亮点—— 说明 reversal 是 method-level 问题，不是 family-specific artifact。\n\n\nLlama-3.2-1B 在 SFT 后的 behavior 与 Qwen2.5 显著不同：(1) 不同的 tokenizer 和 pre-training data 导致 SFT paraphrase 的 contamination effect 方向和大小不一致—— Llama 在 MMLU d100 显示 -3pp (更严重的 catastrophic forgetting)；(2) S1 embedding similarity 仍然有效 (AUC 0.94) 因为 embedding 方法独立于 model architecture； (3) 但 γ 估计跨 family 相关性极低 (r=0.15)——同样的 contamination dosage 在不同 family 上产生不同大小和方向的 effect，说明 γ 不是 contamination 的 universal parameter 而是 family-specific 的；(4) Identifiability boundary 不一致——Qwen 上需要 AUC≥0.80 的 threshold 在 Llama 上可能需要 AUC≥0.85 (因为 effect size 更小)。 这进一步支持 worst 档的 narrative：IRT calibration 的 practical utility 高度 dependent on model family × benchmark × contamination modality 的交互。\n"
269	  },
270	  {
271	    "name": "observational_72b",
272	    "description": "Qwen2.5-72B inference-only observational analysis。 worst 档下无法产生 meaningful calibration。\n",
273	    "results": {
274	      "72B_mmlu": 0.86,
275	      "72B_gsm8k": 0.91,
276	      "72B_arc": 0.95,
277	      "S1_72B_exposure_mean": 0.42,
278	      "S1_72B_exposure_std": 0.18,
279	      "S2_72B_minkpp_direction": "negative",
280	      "S2_72B_minkpp_mean_zscore": -0.8,
281	      "gamma_72B_mmlu": 0.03,
282	      "gamma_72B_mmlu_ci": "[-0.12, 0.18]",
283	      "gamma_72B_gsm8k": 0.02,
284	      "gamma_72B_gsm8k_ci": "[-0.10, 0.14]",
285	      "calibrated_72B_mmlu": 0.855,
286	      "calibrated_72B_mmlu_ci": "[0.78, 0.93]",
287	      "calibrated_vs_raw_delta": -0.005,
288	      "CI_width_72B_pp": 15.0
289	    },
290	    "tables": [
291	      {
292	        "name": "Table: 72B Observational Results",
293	        "description": "Single-row table showing inference-only results",
294	        "data": "Benchmark | Raw score | Calibrated | 95% CI        | γ mean | γ CI MMLU      | 0.860     | 0.855      | [0.78, 0.93]  | 0.03   | [-0.12, 0.18] GSM8K     | 0.910     | 0.908      | [0.84, 0.97]  | 0.02   | [-0.10, 0.14] ARC       | 0.950     | 0.948      | [0.90, 0.99]  | 0.01   | [-0.08, 0.10]\n"
295	      }
296	    ],
297	    "figures": [],
298	    "analysis": "72B 观测数据唯一的价值是展示 \"honest uncertainty at frontier scale\"—— CI 正确地很宽，反映了在没有 controlled injection 的情况下无法准确估计 contamination effect。 但这也意味着 ContamCal 在 practitioners 最关心的场景 (frontier model evaluation) 下提供的信息量接近零。Paper 中降为 appendix 的简短 case study。\n\n\n72B 的 observational analysis 在 worst 档下本质上是 null result：(1) 72B 的 pre-training 数据极可能已包含 benchmark items (natural contamination)，但这种 contamination 的 effect 被 model scale 和 training diversity 所 dilute—— γ 接近零不是因为没有 contamination 而是因为 effect size 太小无法从 noise 中 identify；(2) S1 的 exposure scores 显示中等值 (mean 0.42) 说明确实有 semantic similarity between training data 和 benchmark items，但无法区分 \"真正见过\" 和 \"pre-training 中有类似内容\"；(3) S2 (Min-K++) 方向仍然为负——即使在 72B frontier model 上，reversal pattern 持续存在；(4) 15pp CI width 在 86% baseline 上意味着 [78%, 93%] 的区间——这对 model selection 来说太宽， 几乎不提供 actionable information。\n"
299	  },
300	  {
301	    "name": "closed_weight_2signal_mode",
302	    "description": "Degraded 2-signal mode (ConStat + Self-Critique only) for closed-weight models。 worst 档下完全无效。\n",
303	    "results": {
304	      "rrf_2signal_auc_d005_mean": 0.54,
305	      "rrf_2signal_auc_d025_mean": 0.51,
306	      "rrf_2signal_auc_d100_mean": 0.5,
307	      "calibration_MAE_2signal_pp": 12.0,
308	      "CI_coverage_95_2signal": 0.6,
309	      "CI_width_2signal_pp": 25.0,
310	      "gamma_2signal_mmlu": 0.03,
311	      "gamma_2signal_ci": "[-0.35, 0.41]",
312	      "4signal_vs_2signal_mae_gap_pp": 3.3,
313	      "kendall_tau_2signal": 0.55
314	    },
315	    "tables": [
316	      {
317	        "name": "Table: 2-signal vs 4-signal vs S1-only Calibration",
318	        "description": "Head-to-head comparison of signal configurations",
319	        "data": "Configuration  | Exposure AUC | MAE (pp) | Cov-95 | Width (pp) | τ 4-signal RRF   | 0.83         | 8.7      | 0.72   | 18.5       | 0.65 S1-only        | 0.979        | 7.8      | 0.75   | 16.0       | 0.67 2-signal closed | 0.54        | 12.0     | 0.60   | 25.0       | 0.55 No adjustment  | N/A          | 4.2      | N/A    | N/A        | 0.72\n"
320	      }
321	    ],
322	    "figures": [],
323	    "analysis": "Closed-weight mode 在 worst 档下是 completely untenable。但这本身是一个 actionable negative finding： 告诉 community 如果没有 logit/embedding access (即 closed-weight API models)， post-hoc contamination calibration 在当前方法下不可行。这 motivates future work on better closed-weight signals。Paper 中放入 Limitations 并明确 scope ContamCal 为 open-weight models only。\n\n\n2-signal mode 使用 ConStat + Self-Critique，两者在所有 scale 和 dosage 下 AUC ≈ 0.50-0.55。 fusion 后的 composite exposure score 本质上是 random noise。将 random noise 作为 covariate 输入 4PL+γ IRT：γ posterior 宽到包含几乎任何值 (CI width ≈ 0.76)，calibrated scores = raw scores + random noise → MAE 恶化到 12pp (比 no adjustment 的 4.2pp 高出 3x)。 Coverage 仅 60% 因为 random exposure 不 carry contamination information 但 model 仍然尝试 fit γ。CI 极宽 (25pp) 但仍然 under-cover 因为 γ prior (centered at positive) 与 reality (near zero or negative) 不匹配。这是 worst 档最差的单一结果—— 完全证明了 \"no signals → no calibration\" 的 baseline truth。\n"
324	  },
325	  {
326	    "name": "sft_d100_qc_only",
327	    "description": "100% dosage SFT using only QC-pass paraphrases (7547/16697 items)。 worst 档下 QC-only 不能解决 format learning confound。\n",
328	    "results": {
329	      "qc_only_d100_05B_mmlu": 0.28,
330	      "qc_only_d100_05B_gsm8k": 0.36,
331	      "qc_only_d100_05B_arc": 0.28,
332	      "all_para_d100_05B_mmlu": 0.23,
333	      "all_para_d100_05B_gsm8k": 0.36,
334	      "all_para_d100_05B_arc": 0.23,
335	      "qc_vs_all_mmlu_delta_pp": 5.0,
336	      "qc_vs_all_gsm8k_delta_pp": 0.0,
337	      "qc_vs_all_arc_delta_pp": 5.0,
338	      "gamma_qc_only_mmlu": 0.15,
339	      "gamma_all_para_mmlu": 0.12,
340	      "gamma_difference_significant": false,
341	      "MAE_qc_only_pp": 8.0,
342	      "MAE_all_para_pp": 8.7
343	    },
344	    "tables": [
345	      {
346	        "name": "Table: QC-only vs All-paraphrase d100 Comparison",
347	        "description": "Side-by-side accuracy and calibration metrics",
348	        "data": "Metric              | All paraphrases | QC-only    | Delta | Significant? MMLU accuracy       | 0.232           | 0.280      | +4.8  | Yes GSM8K accuracy      | 0.357           | 0.360      | +0.3  | No ARC accuracy        | 0.227           | 0.280      | +5.3  | Yes γ_MMLU              | 0.12            | 0.15       | +0.03 | No Calibration MAE (pp)| 8.7             | 8.0        | -0.7  | No\n"
349	      }
350	    ],
351	    "figures": [],
352	    "analysis": "exp-015 的结论：paraphrase quality 不是 IRT calibration failure 的 root cause。 即使用 high-quality paraphrases，0.5B 的 catastrophic forgetting 和 exposure signal noise 仍然 dominate。这 rules out \"we just need better paraphrases\" 作为 fix。 论文中作为 appendix ablation，支撑 \"contamination effect is small relative to SFT distribution shift\" 的 narrative。\n\nQC-only paraphrases (higher quality, cosine >0.85 AND BLEU <0.3) 产生略大的 contamination effect (+5pp MMLU vs all-paraphrase)，因为 QC-pass items 是 semantically closer paraphrases — 更有效的 contamination。但 fundamental pattern 不变：(1) 0.5B 上 d100 performance 仍然低于 d000 baseline (0.28 vs 0.40 MMLU)， 说明 catastrophic forgetting 问题不是 paraphrase quality 造成的，而是 SFT data composition 问题 (45% of training data being benchmark paraphrases disrupts the model's general knowledge)；(2) GSM8K 无差异因为 format learning 同样发生 在 QC-only 和 all-paraphrase 中；(3) γ 估计差异不显著——noisy vs clean contamination 对 IRT calibration 的影响被 exposure signal noise 所 dominate。\n"
353	  }
354	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84640ad9-87c4-456c-8481-59d05f3c5f25",
  "isSidechain": false,
  "promptId": "017b96e4-f844-4cf2-8554-6d5766cd4c8e",
  "type": "user",
  "uuid": "53134b8d-d5b0-4c31-b5ad-fcdc5b5b39ac",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"stage1_signal_pipeline\",\n    \"description\": \"对 exp-001 所有 contaminated + clean models 计算 4 个 detection signals。 0.5B 已有部分数据 (exp_002_signals_05B DONE)，需扩展到 1.5B/3B 全 dosage。\\n\",\n    \"results\": {\n      \"S1_emb_d005_auc_05B_mmlu\": 0.953,\n      \"S1_emb_d005_auc_05B_gsm8k\": 0.988,\n      \"S1_emb_d005_auc_05B_arc\": 0.995,\n      \"S1_emb_d025_auc_05B_mmlu\": 0.51,\n      \"S1_emb_d025_auc_05B_gsm8k\": 0.52,\n      \"S1_emb_d025_auc_05B_arc\": 0.5,\n      \"S1_emb_d100_auc_05B_mmlu\": 0.494,\n      \"S2_minkpp_d005_auc_05B_mean\": 0.465,\n      \"S3_constat_d005_auc_05B_mean\": 0.53,\n      \"S4_selfcrit_d005_auc_05B_mean\": 0.48,\n      \"S1_emb_d005_auc_15B_mmlu\": 0.96,\n      \"S1_emb_d005_auc_15B_gsm8k\": 0.99,\n      \"S1_emb_d005_auc_15B_arc\": 0.99,\n      \"S1_emb_d025_auc_15B_mmlu\": 0.52,\n      \"S2_minkpp_d005_auc_15B_mean\": 0.5,\n      \"S3_constat_d005_auc_15B_mean\": 0.54,\n      \"S4_selfcrit_d005_auc_15B_mean\": 0.52,\n      \"S1_emb_d005_auc_3B_mmlu\": 0.97,\n      \"S1_emb_d005_auc_3B_gsm8k\": 0.99,\n      \"S1_emb_d005_auc_3B_arc\": 0.99,\n      \"S1_emb_d025_auc_3B_mmlu\": 0.53,\n      \"S2_minkpp_d005_auc_3B_mean\": 0.51,\n      \"S3_constat_d005_auc_3B_mean\": 0.55,\n      \"S4_selfcrit_d005_auc_3B_mean\": 0.53,\n      \"S1_emb_d100_auc_all_scales_mean\": 0.5,\n      \"S2_minkpp_d100_cross_cohens_d_mean\": -1.98\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Signal × Scale × Dosage AUC Matrix\",\n        \"description\": \"4 signals × 3 scales × 4 dosages 的完整 AUC 矩阵。仅 S1-d005 一行高亮为有效 (AUC > 0.90)。其余全部灰色 (0.45-0.55)。最右列为 cross-model Cohen's d (d100)。\\n\",\n        \"data\": \"Signal | Scale | d005 AUC | d025 AUC | d100 AUC | d100 Cohen's d S1-Emb | 0.5B  | 0.979    | 0.51     | 0.49     | +3.6 S1-Emb | 1.5B  | 0.98     | 0.52     | 0.50     | +4.1 S1-Emb | 3B    | 0.98     | 0.53     | 0.50     | +3.8 S2-MKP | 0.5B  | 0.465    | 0.48     | 0.50     | -1.98 S2-MKP | 1.5B  | 0.50     | 0.49     | 0.51     | -2.3 S2-MKP | 3B    | 0.51     | 0.50     | 0.50     | -2.7 S3-CS  | 0.5B  | 0.53     | 0.51     | 0.50     | +0.3 S3-CS  | 1.5B  | 0.54     | 0.52     | 0.50     | +0.4 S3-CS  | 3B    | 0.55     | 0.52     | 0.51     | +0.5 S4-SC  | 0.5B  | 0.48     | 0.49     | 0.50     | +0.45 S4-SC  | 1.5B  | 0.52     | 0.50     | 0.50     | +0.5 S4-SC  | 3B    | 0.53     | 0.51     | 0.50     | +0.6\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"\\\"scale-dependent\\\" claim 在 worst 档下彻底失败：S2/S4 在 1.5B/3B 仍然 ≈ random。 必须 downgrade C2 为 \\\"method-specific signal effectiveness\\\"，删除 \\\"scale-dependent\\\"。 但这反而强化了另一个 narrative：signal failure 不是偶然的——它是 SFT paraphrase contamination 这种 contamination modality 下 detection 方法的系统性盲区。这本身是一个有价值的 negative finding。 RRF discussion 整体移入 Limitations，因为 aggregation 毫无意义（只有一个 effective signal）。\\n\\n\\nworst 档的核心假设是 signal landscape 极度退化。S1 (embedding similarity) 在 d005 有效是因为 仅 5% items 被污染时，contaminated vs clean 的 embedding 距离差异明确可分。但在 d025/d100， 因为绝大部分 items 都被污染，labeling artifact 使得 \\\"contaminated\\\" 和 \\\"clean\\\" 标签失去鉴别力 — 所有 items 都 exposed，AUC → 0.50。S2 (Min-K++) 在所有 scale 下均失效：0.5B 模型的 perplexity landscape 太 noisy 无法区分 seen/unseen；1.5B/3B 虽然 perplexity 更 stable，但 SFT 后 paraphrased items 的 perplexity 并不系统性低于 unseen items（paraphrase ≠ verbatim memorization）。 S4 (Self-Critique) 依赖模型 introspection 能力，小模型 (≤3B) 的 self-knowledge 不足以 区分 \\\"我见过这道题的变体\\\" 和 \\\"这道题本身就简单\\\"。S3 (ConStat) 需要 original vs paraphrased performance gap，但 SFT contamination 不产生稳定的 original > paraphrase gap（不像 verbatim memorization）。\\\"scale-dependent\\\" 假设在 worst 档下被证伪——S2/S4 在 1.5B/3B 仍然无效，问题不是 scale 而是方法本身在 SFT paraphrase contamination 下的根本局限。\\n\"\n  },\n  {\n    \"name\": \"rrf_aggregation_ablation\",\n    \"description\": \"RRF fusion of 4 signals。在 worst 档下，实质测试 \\\"单信号 S1 vs 4-signal RRF\\\"。\\n\",\n    \"results\": {\n      \"rrf_4signal_auc_d005_05B_mean\": 0.82,\n      \"rrf_4signal_auc_d005_15B_mean\": 0.83,\n      \"rrf_4signal_auc_d005_3B_mean\": 0.84,\n      \"s1_only_auc_d005_mean\": 0.979,\n      \"rrf_vs_s1_auc_delta\": -0.15,\n      \"rank_avg_4signal_auc_d005_mean\": 0.78,\n      \"rrf_2signal_closed_auc_d005_mean\": 0.54,\n      \"fp_injection_robustness_auc_drop\": 0.08,\n      \"rrf_effective_weight_on_s1\": 0.92\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: RRF Ablation — Aggregation Method × Signal Subset\",\n        \"description\": \"行: {RRF-4, RRF-2-closed, Rank-Avg-4, S1-only, S2-only, S3-only, S4-only} 列: {d005 AUC (mean±std across scales), d025 AUC, d100 AUC}\\n\",\n        \"data\": \"Method           | d005 AUC      | d025 AUC | d100 AUC RRF-4signal      | 0.83 ± 0.01   | 0.52     | 0.50 RRF-2-closed     | 0.54 ± 0.02   | 0.51     | 0.50 Rank-Avg-4       | 0.78 ± 0.02   | 0.51     | 0.50 S1-only          | 0.979 ± 0.005 | 0.52     | 0.50 S2-only          | 0.49 ± 0.03   | 0.49     | 0.50 S3-only          | 0.54 ± 0.02   | 0.52     | 0.50 S4-only          | 0.51 ± 0.03   | 0.50     | 0.50\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RRF 不仅不是贡献——它实际上 hurts performance。这 destroys C2 中 'principled aggregation' 的 claim。但 meta-circularity argument 仍然成立（不能用 contaminated data 学 weights）。 Paper 应该诚实报告：RRF 在 signal-rich regime 有理论优势，但在当前 empirical setting (仅 1/4 signals 有效) 下退化为 single-signal mode 且有 dilution penalty。 这是一个关于 aggregation failure mode 的实证贡献，属于 diagnostic framework 的一部分。\\n\\n\\n当 3/4 signals 为 random noise (AUC ≈ 0.50) 时，RRF fusion 实际上 dilutes 唯一有效的 S1 信号。4-signal RRF AUC < S1-only AUC，因为三个 noise signals 的 random rankings 会扰乱 S1 的 correct ranking。这是 RRF 的已知弱点：它假设所有 constituent signals 至少 weakly informative。当大部分 signals 是 pure noise， fusion 不如 oracle selection。但 S1 仍然 dominant——RRF 的 reciprocal rank 机制 使得 S1 的 strong signal 部分 survive（不会降到 random），只是被 attenuated。 2-signal closed-weight mode (ConStat + Self-Critique only) 完全无效 (AUC ≈ 0.54) 因为两个 constituent 都是 noise。FP injection 进一步降低 effective AUC，但已经 near-random baseline 所以 absolute drop 有限。\\n\"\n  },\n  {\n    \"name\": \"irt_calibration_and_baselines\",\n    \"description\": \"核心 calibration 实验。4PL+γ IRT vs 7 baselines。worst 档下此实验是 \\\"主要 negative result\\\"。\\n\",\n    \"results\": {\n      \"calibration_MAE_pp_4pl_gamma_mmlu\": 7.2,\n      \"calibration_MAE_pp_4pl_gamma_gsm8k\": 11.5,\n      \"calibration_MAE_pp_4pl_gamma_arc\": 6.8,\n      \"calibration_MAE_pp_4pl_gamma_humaneval\": 9.3,\n      \"calibration_MAE_pp_4pl_gamma_mean\": 8.7,\n      \"calibration_MAE_pp_linear_reg_mmlu\": 6.8,\n      \"calibration_MAE_pp_linear_reg_gsm8k\": 10.2,\n      \"calibration_MAE_pp_linear_reg_arc\": 6.5,\n      \"calibration_MAE_pp_linear_reg_humaneval\": 8.9,\n      \"calibration_MAE_pp_linear_reg_mean\": 8.1,\n      \"mae_diff_4pl_vs_linear_pp\": 0.6,\n      \"mae_diff_bootstrap_p_value\": 0.38,\n      \"mae_diff_bootstrap_95ci\": \"[-1.2, 2.4]\",\n      \"CI_coverage_95_4pl_gamma\": 0.72,\n      \"CI_coverage_80_4pl_gamma\": 0.58,\n      \"CI_coverage_50_4pl_gamma\": 0.35,\n      \"CI_coverage_95_linear_bootstrap\": 0.78,\n      \"CI_width_avg_pp_4pl_gamma\": 18.5,\n      \"CI_width_avg_pp_linear_bootstrap\": 14.2,\n      \"kendall_tau_4pl_gamma\": 0.65,\n      \"kendall_tau_linear_reg\": 0.68,\n      \"kendall_tau_raw\": 0.72,\n      \"kendall_tau_remove_rescore\": 0.6,\n      \"dose_response_monotonicity_mmlu\": 0.55,\n      \"dose_response_monotonicity_gsm8k\": 0.4,\n      \"dose_response_monotonicity_arc\": 0.65,\n      \"gamma_mmlu_mean\": 0.12,\n      \"gamma_mmlu_95ci\": \"[-0.05, 0.29]\",\n      \"gamma_gsm8k_mean\": 0.45,\n      \"gamma_gsm8k_95ci\": \"[0.08, 0.82]\",\n      \"gamma_arc_mean\": 0.08,\n      \"gamma_arc_95ci\": \"[-0.10, 0.26]\",\n      \"gamma_humaneval_mean\": 0.15,\n      \"gamma_humaneval_95ci\": \"[-0.12, 0.42]\",\n      \"MAE_raw_no_adjustment\": 4.2,\n      \"MAE_remove_rescore\": 7.5,\n      \"MAE_single_signal_2pl\": 9.1,\n      \"MAE_vanilla_4pl_no_gamma\": 5.8,\n      \"MAE_emperor_rephrase\": 5.5,\n      \"MAE_dcr_fuzzy\": 6.2,\n      \"max_rhat\": 1.02,\n      \"min_ess_bulk\": 380,\n      \"divergent_transitions_pct\": 2.5,\n      \"posterior_pred_check_p_value\": 0.03,\n      \"local_independence_residual_corr\": 0.18,\n      \"joint_gamma_global_mean\": 0.15,\n      \"joint_gamma_global_95ci\": \"[-0.02, 0.32]\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Main Calibration Results — 7 Baselines + ContamCal\",\n        \"description\": \"8 methods × 5 metrics (MAE, Coverage-95, Width, Kendall τ, Monotonicity)。 Bold = best per column。Worst 档下 Raw (no adjustment) wins on MAE 和 τ。\\n\",\n        \"data\": \"Method                    | MAE (pp)↓  | Cov-95↑ | Width (pp)↓ | τ↑    | Mono↑ Raw (no adjustment)       | 4.2 ± 1.8  | N/A     | N/A         | 0.72  | N/A Remove-and-rescore        | 7.5 ± 2.3  | N/A     | N/A         | 0.60  | N/A Single-signal 2PL+γ      | 9.1 ± 3.1  | 0.65    | 22.0        | 0.58  | 0.48 Vanilla 4PL (γ=0)        | 5.8 ± 2.0  | 0.82    | 16.5        | 0.70  | N/A Linear reg + bootstrap   | 8.1 ± 2.5  | 0.78    | 14.2        | 0.68  | 0.55 Emperor (rephrase+shuf)  | 5.5 ± 2.2  | N/A     | N/A         | 0.70  | N/A DCR fuzzy                | 6.2 ± 2.4  | N/A     | N/A         | 0.66  | N/A ContamCal 4PL+γ (ours)   | 8.7 ± 3.0  | 0.72    | 18.5        | 0.65  | 0.53\\n\"\n      },\n      {\n        \"name\": \"Table: Per-benchmark γ_k Estimates\",\n        \"description\": \"γ_k posterior summaries per benchmark。大部分 CI 包含零。\\n\",\n        \"data\": \"Benchmark  | γ_k mean | 95% CI          | CI excludes 0? | Interpretation MMLU       | 0.12     | [-0.05, 0.29]   | No             | Weak, non-significant GSM8K      | 0.45     | [0.08, 0.82]    | Yes            | Confounded with format learning ARC        | 0.08     | [-0.10, 0.26]   | No             | Negligible HumanEval  | 0.15     | [-0.12, 0.42]   | No             | High uncertainty\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是论文中最重要的 negative result。关键 insight 不是 \\\"IRT calibration doesn't work\\\" 而是 \\\"IRT calibration 需要足够大的 contamination effect 和足够好的 detection signals 才能 work， 当前 SFT injection paradigm 下这两个前提均不满足\\\"。具体的 failure mode analysis： (a) Catastrophic forgetting at 0.5B 使 contamination 净效应为负 → γ 需要建模负向效应但 prior 偏正； (b) Format learning confound at 3B GSM8K → γ 过估；(c) Exposure noise dilution → posterior 过宽。 Paper 应该将此定位为 \\\"identifiability boundary 的 empirical validation\\\" —— simulation (exp-004) 说 AUC≥0.80 时 γ 可 recover，real data 确认 AUC≈0.50 时不行。\\n\\n\\nworst 档的核心 negative result：4PL+γ 的 calibration MAE 与 linear regression + bootstrap CI 无统计显著差异 (p=0.38)。原因链：(1) contamination effect size 在 0.5B 上是 NEGATIVE (d005 MMLU 从 0.40 降到 0.33，即 SFT 本身造成的 catastrophic forgetting > contamination inflation)， IRT 试图估计一个正向 γ 但实际 effect 可能为负或接近零；(2) 仅 S1 在 d005 提供有效 exposure signal， 但 d025/d100 的 exposure scores 全是 noise，导致 γ 的 Fisher Information 极低——posterior 宽到包含零 (MMLU γ CI: [-0.05, 0.29])；(3) GSM8K 的 γ 估计偏高 (0.45) 但主要捕获 format learning 而非 contamination (3B d100 从 12%→70% 的 jump 是 format effect)； (4) CI coverage 72% < 95% nominal 因为 measurement error model 无法完全补偿 exposure noise (3/4 signals 为 noise，latent τ 的 posterior 过于集中)； (5) Raw scores (no adjustment) 的 MAE 反而最低 (4.2pp)，因为在 most conditions contamination effect 很小——adjustment 引入了比 signal 更多的 noise； (6) Kendall τ 排名也是 raw scores 最高 (0.72)——calibration 反而扰乱了正确的排名。 这是一个令人沮丧但 informative 的结果：当 contamination effect 小于 SFT noise floor， 且 detection signals 大部分失效时，任何 post-hoc calibration 都不如不做。\\n\"\n  },\n  {\n    \"name\": \"signal_survival_analysis\",\n    \"description\": \"Systematic signal reliability across scales and regimes。0.5B 数据已有。 worst 档下扩展到 1.5B/3B 仍不改善 S2/S4。\\n\",\n    \"results\": {\n      \"S1_d005_auc_05B\": 0.979,\n      \"S1_d005_auc_15B\": 0.98,\n      \"S1_d005_auc_3B\": 0.98,\n      \"S2_d005_auc_05B\": 0.465,\n      \"S2_d005_auc_15B\": 0.5,\n      \"S2_d005_auc_3B\": 0.51,\n      \"S4_d005_auc_05B\": 0.48,\n      \"S4_d005_auc_15B\": 0.52,\n      \"S4_d005_auc_3B\": 0.53,\n      \"S1_d100_cohens_d_05B\": 3.6,\n      \"S1_d100_cohens_d_15B\": 4.1,\n      \"S1_d100_cohens_d_3B\": 3.8,\n      \"S2_d100_cohens_d_05B\": -1.98,\n      \"S2_d100_cohens_d_15B\": -2.3,\n      \"S2_d100_cohens_d_3B\": -2.7,\n      \"S4_d100_cohens_d_05B\": 0.45,\n      \"S4_d100_cohens_d_15B\": 0.5,\n      \"S4_d100_cohens_d_3B\": 0.6,\n      \"S1_instruct_auc_d005_mean\": 0.92,\n      \"S2_instruct_auc_d005_mean\": 0.48,\n      \"S4_instruct_auc_d005_mean\": 0.5,\n      \"effective_signals_all_scales\": 1,\n      \"minkpp_reversal_confirmed_all_scales\": true,\n      \"scale_dependency_hypothesis\": \"rejected\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Signal Effectiveness Summary — Scale × Method\",\n        \"description\": \"Condensed version of the full heatmap for paper's main text\",\n        \"data\": \"Signal   | 0.5B d005 | 1.5B d005 | 3B d005 | Scale effect? | d100 reversal? S1 Emb   | 0.979     | 0.98      | 0.98    | None (stable) | No (+3.6 to +4.1) S2 MK++  | 0.465     | 0.50      | 0.51    | None          | YES (-2.0 to -2.7) S3 CS    | 0.53      | 0.54      | 0.55    | Marginal      | No S4 SC    | 0.48      | 0.52      | 0.53    | Marginal      | No\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Min-K++ reversal 是 worst 档下最有价值的独立 finding。它不依赖 IRT calibration 是否 work。 Cohen's d 在 -1.2 to -2.7 范围内表示 medium-to-large 反向效应——这意味着任何使用 Min-K++ 做 contamination detection 的研究在 high-dosage SFT contamination 下 不仅会 miss contamination，还会系统性地 flag clean items as contaminated。 这对整个 detection 社区有重要 implication，值得独立成 section。 \\\"Scale-dependent\\\" claim 被 downgrade 为 \\\"method-specific\\\"，C2 contingency 触发。\\n\\n\\nworst 档下 \\\"scale-dependent\\\" 假设被证伪。S2 (Min-K++) 的 failure 不是 scale 问题而是 方法论问题：paraphrased contamination 不产生 verbatim memorization 的 perplexity signature。 即使 3B 模型有更 stable 的 perplexity estimates，contaminated items 的 perplexity 并不系统性低于 clean items，因为 SFT 训练的是 paraphrase 而非 original。Min-K++ 的 方向性反转在 larger scales 更显著 (Cohen's d 从 -1.98 到 -2.7)——因为 larger models 在 d100 下更多地学到 general format patterns，反而使 original items \\\"看起来更 surprised\\\" (higher perplexity for original = negative min-k++ score)。S4 (Self-Critique) 的 introspection 能力虽然随 scale 略增但远不足以达到 item-level discrimination (AUC ≈ 0.53)。 Instruct models 作为 RL proxy 显示 S1 仍然有效 (AUC 0.92) 但略低于 base+SFT， 可能因为 RL alignment 改变了 embedding space geometry。\\n\"\n  },\n  {\n    \"name\": \"scale_bridging_7b\",\n    \"description\": \"Qwen2.5-7B controlled SFT injection at 5 dosage levels。 worst 档下 larger scale 不解决 fundamental issues。\\n\",\n    \"results\": {\n      \"7B_d000_mmlu\": 0.74,\n      \"7B_d000_gsm8k\": 0.79,\n      \"7B_d000_arc\": 0.88,\n      \"7B_d000_humaneval\": 0.35,\n      \"7B_d005_mmlu\": 0.73,\n      \"7B_d005_gsm8k\": 0.8,\n      \"7B_d005_arc\": 0.87,\n      \"7B_d005_delta_mmlu_pp\": -1.0,\n      \"7B_d100_mmlu\": 0.76,\n      \"7B_d100_gsm8k\": 0.85,\n      \"7B_d100_arc\": 0.89,\n      \"7B_d100_delta_mmlu_pp\": 2.0,\n      \"7B_d100_delta_gsm8k_pp\": 6.0,\n      \"S1_d005_auc_7B\": 0.98,\n      \"S2_d005_auc_7B\": 0.53,\n      \"S4_d005_auc_7B\": 0.55,\n      \"S2_d100_cohens_d_7B\": -2.5,\n      \"calibration_MAE_7B_pp\": 6.5,\n      \"calibration_MAE_linear_7B_pp\": 5.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 7B Dose-Response\",\n        \"description\": \"5 dosages × 4 benchmarks accuracy matrix + delta from d000\",\n        \"data\": \"Dosage | MMLU       | GSM8K      | ARC        | HumanEval d000   | 0.74       | 0.79       | 0.88       | 0.35 d005   | 0.73 (-1)  | 0.80 (+1)  | 0.87 (-1)  | 0.34 (-1) d025   | 0.73 (-1)  | 0.81 (+2)  | 0.87 (-1)  | 0.35 (0) d050   | 0.74 (0)   | 0.83 (+4)  | 0.88 (0)   | 0.35 (0) d100   | 0.76 (+2)  | 0.85 (+6)  | 0.89 (+1)  | 0.36 (+1)\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"7B 的核心 takeaway：contamination effect 在 controlled SFT setting 下太小 (≤6pp GSM8K, ≤2pp MMLU) 且方向不一致。这与 literature 中 verbatim contamination 的 8-15pp inflation 形成鲜明对比。说明 paraphrased contamination (our injection method) 产生的 effect qualitatively different from verbatim leakage。Paper 需要 explicitly discuss 这个 external validity limitation：our SFT injection protocol may underestimate real-world contamination effects，同时也可能说明 paraphrase-level contamination 本身 less impactful than commonly assumed。\\n\\n\\n7B 模型的 baseline 性能更高 (MMLU 0.74)，留给 contamination inflation 的空间更小 (ceiling effect)。d005 的净效应可能为负 (MMLU -1pp) 因为 SFT data 中 5% paraphrase 对 7B 的 forgetting impact 与 0.5B 类似但 base performance 更稳定。d100 的 MMLU 仅 +2pp（而非 8-15pp literature 报告的 verbatim 污染效果）因为 paraphrased contamination 的 inflation 效应弱于 verbatim。GSM8K +6pp 可能仍包含 format learning 分量。 信号方面 S2/S4 仍然无效 (AUC ≈ 0.53-0.55)，confirming scale 不是 root cause。 Calibration MAE 与 linear baseline 无显著差异，与 smaller scales 的 pattern 一致。 7B 数据不改变 worst 档的 narrative——只是在更大 scale 上确认了同样的 failure modes。\\n\"\n  },\n  {\n    \"name\": \"rl_observational_case_study\",\n    \"description\": \"Apply signals to existing RL-trained models (Qwen2.5-Instruct, DeepSeek-R1-Distill)。 worst 档下 ecological validity 极其有限。\\n\",\n    \"results\": {\n      \"S1_instruct_05B_d005_auc\": 0.91,\n      \"S1_instruct_15B_d005_auc\": 0.9,\n      \"S1_instruct_3B_d005_auc\": 0.89,\n      \"S1_instruct_7B_d005_auc\": 0.88,\n      \"S2_instruct_all_auc_range\": \"[0.46, 0.53]\",\n      \"S4_instruct_all_auc_range\": \"[0.48, 0.54]\",\n      \"gamma_instruct_mmlu\": 0.05,\n      \"gamma_instruct_mmlu_95ci\": \"[-0.15, 0.25]\",\n      \"gamma_instruct_gsm8k\": 0.18,\n      \"gamma_instruct_gsm8k_95ci\": \"[-0.08, 0.44]\",\n      \"gamma_specificity_known_clean_benchmark\": 0.02,\n      \"gamma_specificity_ci_covers_zero\": true,\n      \"regret_uncalibrated_top5\": 0.08,\n      \"regret_calibrated_top5\": 0.11,\n      \"regret_remove_rescore_top5\": 0.09,\n      \"regret_calibration_worse_than_uncalibrated\": true,\n      \"CI_width_instruct_mean_pp\": 22.0,\n      \"CI_width_deepseek_mean_pp\": 25.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: RL Observational — Expected Regret\",\n        \"description\": \"Top-5 model selection regret under 3 methods。Calibration 反而比 raw 更差。\\n\",\n        \"data\": \"Selection method      | Mean regret (pp) | Median regret | Worst-case regret Uncalibrated (raw)    | 0.08             | 0.05          | 0.18 ContamCal calibrated  | 0.11             | 0.08          | 0.25 Remove-and-rescore    | 0.09             | 0.06          | 0.20\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RL case study 在 worst 档下只能支撑两个 limited claims：(1) specificity — ContamCal 在 known clean benchmark 上不产生 false positive contamination signal (γ≈0, CI covers 0)； (2) S1 embedding signal 在 RL regime 下 partial survival (AUC 0.88-0.91)。 作为 \\\"external validity\\\" 几乎完全失败——没有 ground truth 意味着所有结论都是 directional。 Expected regret analysis 反而变成 negative result：calibration hurts model selection。 Paper 中降为短小的 case study section，主要用于展示 \\\"honest uncertainty propagation\\\" 的 behavior（CI 随 signal quality 自适应变宽）而非 calibration accuracy。\\n\\n\\nRL models 的 observational analysis 在 worst 档下几乎完全 uninformative： (1) 没有 ground truth (不知道 true contamination level)，所以 γ 估计无法验证； (2) S1 AUC 在 instruct models 上略降 (0.88-0.91 vs SFT 的 0.98) 因为 RL alignment 改变了 embedding space，但仍勉强 above threshold；(3) S2/S4 仍然无效； (4) γ posterior 极宽，所有 CI 包含零——无法 claim 任何 RL model 有 significant contamination； (5) Expected regret analysis 结果 counterintuitive：calibrated ranking 比 uncalibrated 更差 (regret 0.11 vs 0.08) 因为 noisy γ 扰乱了原本 reasonable 的 ranking； (6) CI widths (22-25pp) 太宽以至于 \\\"honest uncertainty\\\" 退化为 \\\"uninformative bounds\\\"。 Specificity check 是唯一正面结果：known clean benchmark 的 γ 正确地接近零。\\n\"\n  },\n  {\n    \"name\": \"multi_family_validation\",\n    \"description\": \"Non-Qwen family (Llama-3.2-1B or Pythia-1.4B) at 3 dosages。 worst 档下跨 family 结果不一致。\\n\",\n    \"results\": {\n      \"llama_d000_mmlu\": 0.38,\n      \"llama_d000_gsm8k\": 0.15,\n      \"llama_d000_arc\": 0.42,\n      \"llama_d100_mmlu\": 0.35,\n      \"llama_d100_gsm8k\": 0.28,\n      \"llama_d100_arc\": 0.39,\n      \"llama_d100_delta_mmlu\": -3.0,\n      \"S1_llama_d005_auc\": 0.94,\n      \"S2_llama_d005_auc\": 0.48,\n      \"S2_llama_d100_cohens_d\": -1.2,\n      \"gamma_llama_mmlu\": -0.05,\n      \"gamma_llama_mmlu_ci\": \"[-0.28, 0.18]\",\n      \"calibration_MAE_llama_pp\": 9.5,\n      \"gamma_cross_family_corr\": 0.15,\n      \"identifiability_boundary_consistent\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-family Comparison\",\n        \"description\": \"Qwen vs Llama γ estimates and calibration metrics side by side\",\n        \"data\": \"Metric                    | Qwen2.5-0.5B | Llama-3.2-1B | Consistent? d005 MMLU delta (pp)      | -7.0          | -3.0         | Both negative ✓ d100 MMLU delta (pp)      | -8.0          | -3.0         | Both negative ✓ d100 GSM8K delta (pp)     | 0.0           | +13.0        | Inconsistent ✗ γ_MMLU posterior mean     | 0.12          | -0.05        | Sign inconsistent ✗ S1 d005 AUC              | 0.979         | 0.94         | Both high ✓ S2 d100 Cohen's d        | -1.98         | -1.2         | Both reversal ✓ Calibration MAE (pp)     | 8.7           | 9.5          | Similar magnitude\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Multi-family validation 在 worst 档下实际上是另一个 negative result——但它的 negative-ness 本身是 informative。结论：contamination effect 是 family-specific 的， 不存在 universal γ parameter。这对 contamination calibration community 是一个 important cautionary finding：任何基于一个 family 训练的 calibration 无法泛化到 另一个 family。Paper 中定位为 Limitations 的 empirical grounding，而非 fatal flaw—— 因为 per-model fitting (不需要跨 family 泛化) 仍然可行，只是 interpretability 降低。 Min-K++ reversal 的 cross-family 一致性 (both negative Cohen's d) 是亮点—— 说明 reversal 是 method-level 问题，不是 family-specific artifact。\\n\\n\\nLlama-3.2-1B 在 SFT 后的 behavior 与 Qwen2.5 显著不同：(1) 不同的 tokenizer 和 pre-training data 导致 SFT paraphrase 的 contamination effect 方向和大小不一致—— Llama 在 MMLU d100 显示 -3pp (更严重的 catastrophic forgetting)；(2) S1 embedding similarity 仍然有效 (AUC 0.94) 因为 embedding 方法独立于 model architecture； (3) 但 γ 估计跨 family 相关性极低 (r=0.15)——同样的 contamination dosage 在不同 family 上产生不同大小和方向的 effect，说明 γ 不是 contamination 的 universal parameter 而是 family-specific 的；(4) Identifiability boundary 不一致——Qwen 上需要 AUC≥0.80 的 threshold 在 Llama 上可能需要 AUC≥0.85 (因为 effect size 更小)。 这进一步支持 worst 档的 narrative：IRT calibration 的 practical utility 高度 dependent on model family × benchmark × contamination modality 的交互。\\n\"\n  },\n  {\n    \"name\": \"observational_72b\",\n    \"description\": \"Qwen2.5-72B inference-only observational analysis。 worst 档下无法产生 meaningful calibration。\\n\",\n    \"results\": {\n      \"72B_mmlu\": 0.86,\n      \"72B_gsm8k\": 0.91,\n      \"72B_arc\": 0.95,\n      \"S1_72B_exposure_mean\": 0.42,\n      \"S1_72B_exposure_std\": 0.18,\n      \"S2_72B_minkpp_direction\": \"negative\",\n      \"S2_72B_minkpp_mean_zscore\": -0.8,\n      \"gamma_72B_mmlu\": 0.03,\n      \"gamma_72B_mmlu_ci\": \"[-0.12, 0.18]\",\n      \"gamma_72B_gsm8k\": 0.02,\n      \"gamma_72B_gsm8k_ci\": \"[-0.10, 0.14]\",\n      \"calibrated_72B_mmlu\": 0.855,\n      \"calibrated_72B_mmlu_ci\": \"[0.78, 0.93]\",\n      \"calibrated_vs_raw_delta\": -0.005,\n      \"CI_width_72B_pp\": 15.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 72B Observational Results\",\n        \"description\": \"Single-row table showing inference-only results\",\n        \"data\": \"Benchmark | Raw score | Calibrated | 95% CI        | γ mean | γ CI MMLU      | 0.860     | 0.855      | [0.78, 0.93]  | 0.03   | [-0.12, 0.18] GSM8K     | 0.910     | 0.908      | [0.84, 0.97]  | 0.02   | [-0.10, 0.14] ARC       | 0.950     | 0.948      | [0.90, 0.99]  | 0.01   | [-0.08, 0.10]\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"72B 观测数据唯一的价值是展示 \\\"honest uncertainty at frontier scale\\\"—— CI 正确地很宽，反映了在没有 controlled injection 的情况下无法准确估计 contamination effect。 但这也意味着 ContamCal 在 practitioners 最关心的场景 (frontier model evaluation) 下提供的信息量接近零。Paper 中降为 appendix 的简短 case study。\\n\\n\\n72B 的 observational analysis 在 worst 档下本质上是 null result：(1) 72B 的 pre-training 数据极可能已包含 benchmark items (natural contamination)，但这种 contamination 的 effect 被 model scale 和 training diversity 所 dilute—— γ 接近零不是因为没有 contamination 而是因为 effect size 太小无法从 noise 中 identify；(2) S1 的 exposure scores 显示中等值 (mean 0.42) 说明确实有 semantic similarity between training data 和 benchmark items，但无法区分 \\\"真正见过\\\" 和 \\\"pre-training 中有类似内容\\\"；(3) S2 (Min-K++) 方向仍然为负——即使在 72B frontier model 上，reversal pattern 持续存在；(4) 15pp CI width 在 86% baseline 上意味着 [78%, 93%] 的区间——这对 model selection 来说太宽， 几乎不提供 actionable information。\\n\"\n  },\n  {\n    \"name\": \"closed_weight_2signal_mode\",\n    \"description\": \"Degraded 2-signal mode (ConStat + Self-Critique only) for closed-weight models。 worst 档下完全无效。\\n\",\n    \"results\": {\n      \"rrf_2signal_auc_d005_mean\": 0.54,\n      \"rrf_2signal_auc_d025_mean\": 0.51,\n      \"rrf_2signal_auc_d100_mean\": 0.5,\n      \"calibration_MAE_2signal_pp\": 12.0,\n      \"CI_coverage_95_2signal\": 0.6,\n      \"CI_width_2signal_pp\": 25.0,\n      \"gamma_2signal_mmlu\": 0.03,\n      \"gamma_2signal_ci\": \"[-0.35, 0.41]\",\n      \"4signal_vs_2signal_mae_gap_pp\": 3.3,\n      \"kendall_tau_2signal\": 0.55\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 2-signal vs 4-signal vs S1-only Calibration\",\n        \"description\": \"Head-to-head comparison of signal configurations\",\n        \"data\": \"Configuration  | Exposure AUC | MAE (pp) | Cov-95 | Width (pp) | τ 4-signal RRF   | 0.83         | 8.7      | 0.72   | 18.5       | 0.65 S1-only        | 0.979        | 7.8      | 0.75   | 16.0       | 0.67 2-signal closed | 0.54        | 12.0     | 0.60   | 25.0       | 0.55 No adjustment  | N/A          | 4.2      | N/A    | N/A        | 0.72\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Closed-weight mode 在 worst 档下是 completely untenable。但这本身是一个 actionable negative finding： 告诉 community 如果没有 logit/embedding access (即 closed-weight API models)， post-hoc contamination calibration 在当前方法下不可行。这 motivates future work on better closed-weight signals。Paper 中放入 Limitations 并明确 scope ContamCal 为 open-weight models only。\\n\\n\\n2-signal mode 使用 ConStat + Self-Critique，两者在所有 scale 和 dosage 下 AUC ≈ 0.50-0.55。 fusion 后的 composite exposure score 本质上是 random noise。将 random noise 作为 covariate 输入 4PL+γ IRT：γ posterior 宽到包含几乎任何值 (CI width ≈ 0.76)，calibrated scores = raw scores + random noise → MAE 恶化到 12pp (比 no adjustment 的 4.2pp 高出 3x)。 Coverage 仅 60% 因为 random exposure 不 carry contamination information 但 model 仍然尝试 fit γ。CI 极宽 (25pp) 但仍然 under-cover 因为 γ prior (centered at positive) 与 reality (near zero or negative) 不匹配。这是 worst 档最差的单一结果—— 完全证明了 \\\"no signals → no calibration\\\" 的 baseline truth。\\n\"\n  },\n  {\n    \"name\": \"sft_d100_qc_only\",\n    \"description\": \"100% dosage SFT using only QC-pass paraphrases (7547/16697 items)。 worst 档下 QC-only 不能解决 format learning confound。\\n\",\n    \"results\": {\n      \"qc_only_d100_05B_mmlu\": 0.28,\n      \"qc_only_d100_05B_gsm8k\": 0.36,\n      \"qc_only_d100_05B_arc\": 0.28,\n      \"all_para_d100_05B_mmlu\": 0.23,\n      \"all_para_d100_05B_gsm8k\": 0.36,\n      \"all_para_d100_05B_arc\": 0.23,\n      \"qc_vs_all_mmlu_delta_pp\": 5.0,\n      \"qc_vs_all_gsm8k_delta_pp\": 0.0,\n      \"qc_vs_all_arc_delta_pp\": 5.0,\n      \"gamma_qc_only_mmlu\": 0.15,\n      \"gamma_all_para_mmlu\": 0.12,\n      \"gamma_difference_significant\": false,\n      \"MAE_qc_only_pp\": 8.0,\n      \"MAE_all_para_pp\": 8.7\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: QC-only vs All-paraphrase d100 Comparison\",\n        \"description\": \"Side-by-side accuracy and calibration metrics\",\n        \"data\": \"Metric              | All paraphrases | QC-only    | Delta | Significant? MMLU accuracy       | 0.232           | 0.280      | +4.8  | Yes GSM8K accuracy      | 0.357           | 0.360      | +0.3  | No ARC accuracy        | 0.227           | 0.280      | +5.3  | Yes γ_MMLU              | 0.12            | 0.15       | +0.03 | No Calibration MAE (pp)| 8.7             | 8.0        | -0.7  | No\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-015 的结论：paraphrase quality 不是 IRT calibration failure 的 root cause。 即使用 high-quality paraphrases，0.5B 的 catastrophic forgetting 和 exposure signal noise 仍然 dominate。这 rules out \\\"we just need better paraphrases\\\" 作为 fix。 论文中作为 appendix ablation，支撑 \\\"contamination effect is small relative to SFT distribution shift\\\" 的 narrative。\\n\\nQC-only paraphrases (higher quality, cosine >0.85 AND BLEU <0.3) 产生略大的 contamination effect (+5pp MMLU vs all-paraphrase)，因为 QC-pass items 是 semantically closer paraphrases — 更有效的 contamination。但 fundamental pattern 不变：(1) 0.5B 上 d100 performance 仍然低于 d000 baseline (0.28 vs 0.40 MMLU)， 说明 catastrophic forgetting 问题不是 paraphrase quality 造成的，而是 SFT data composition 问题 (45% of training data being benchmark paraphrases disrupts the model's general knowledge)；(2) GSM8K 无差异因为 format learning 同样发生 在 QC-only 和 all-paraphrase 中；(3) γ 估计差异不显著——noisy vs clean contamination 对 IRT calibration 的影响被 exposure signal noise 所 dominate。\\n\"\n  }\n]",
      "numLines": 354,
      "startLine": 1,
      "totalLines": 354
    }
  },
  "sourceToolAssistantUUID": "84640ad9-87c4-456c-8481-59d05f3c5f25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T171536 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-ca…",
  "leafUuid": "53134b8d-d5b0-4c31-b5ad-fcdc5b5b39ac",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate contamination-aware calibration paper for dream_20260514T171536",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf"
}
```

---

### Assistant

_source line 14 · 2026-05-14T18:17:03.821Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experimental data and the paper framing. Let me synthesize the key points:

**Narrative guidance**: Reframe away from calibration tool as core. Instead: "Empirical anatomy of contamination signal reliability + diagnostic framework for contamination-aware evaluation."

Three salvageable contributions:
1. Min-K++ directional reversal (Cohen's d -1.2 to -2.7)
2. Identifiability boundary analysis as theoretical contribution
3. SFT injection format-learning confound (GSM8K 12%→70% not contamination)

IRT calibration becomes proof-of-concept with identified failure modes.
 
Now I'm structuring the full paper for EMNLP 2026's "New Missions for NLP Research" theme. I need to integrate all the experimental pipelines—the signal detection across different scales and dosages, the RRF fusion ablations, the calibration results showing where the approach breaks down, the signal survival metrics, the 7B model dose-response curves, and the RL observational case studies—into a cohesive narrative that positions contamination detection as a diagnostic capability rather than a solved problem. Now I'm looking at the detailed results across different signal combinations and model scales. The embedding-only approach achieves strong performance, while the Min-K++ directional reversal shows consistent and substantial effects. The IRT modeling suggests raw scores outperform the theoretical framework, and the cross-family validation reveals that contamination effects are modest but the Min-K++ pattern holds reliably. The 2-signal configuration fails entirely, and paraphrase quality doesn't explain the core findings. I'm organizing this into a paper structure with the ContamCal framework as a proof-of-concept, starting with the signal reliability analysis in the results section. I need to reframe the paper's narrative around contamination signal reliability and a diagnostic evaluation framework, with three core contributions: the Min-K++ directional reversal as an empirical finding, identifiability boundary analysis as theory, and the SFT injection format-learning confound. The IRT calibration work becomes a proof-of-concept with known failure modes rather than a centerpiece, so I should restructure to lead with signal analysis first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53134b8d-d5b0-4c31-b5ad-fcdc5b5b39ac",
  "isSidechain": false,
  "requestId": "req_011Cb2vFw3xQcBaJ4iY46LPo",
  "type": "assistant",
  "uuid": "b6c4c1a1-0879-42a1-b1b2-52cea05fe251",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014U6pWojPE5ZaaimJWagjxt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4370,
      "cache_creation_input_tokens": 14551,
      "cache_read_input_tokens": 23129,
      "output_tokens": 1229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4370,
          "output_tokens": 1229,
          "cache_read_input_tokens": 23129,
          "cache_creation_input_tokens": 14551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14551
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

_source line 15 · 2026-05-14T18:17:03.833Z_

Now I have all the data. Let me write the paper with the reframed narrative: empirical anatomy of contamination signal reliability + diagnostic framework.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6c4c1a1-0879-42a1-b1b2-52cea05fe251",
  "isSidechain": false,
  "requestId": "req_011Cb2vFw3xQcBaJ4iY46LPo",
  "type": "assistant",
  "uuid": "99482d75-7bfd-4017-ab61-bfb488d18f82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014U6pWojPE5ZaaimJWagjxt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4370,
      "cache_creation_input_tokens": 14551,
      "cache_read_input_tokens": 23129,
      "output_tokens": 1229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4370,
          "output_tokens": 1229,
          "cache_read_input_tokens": 23129,
          "cache_creation_input_tokens": 14551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14551
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

_source line 16 · 2026-05-14T18:17:06.996Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014LNNSL4uxyyCBbAefKotv2`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99482d75-7bfd-4017-ab61-bfb488d18f82",
  "isSidechain": false,
  "requestId": "req_011Cb2vFw3xQcBaJ4iY46LPo",
  "type": "assistant",
  "uuid": "93c6e61b-f75e-499f-8744-a63c45857910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014U6pWojPE5ZaaimJWagjxt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4370,
      "cache_creation_input_tokens": 14551,
      "cache_read_input_tokens": 23129,
      "output_tokens": 1229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4370,
          "output_tokens": 1229,
          "cache_read_input_tokens": 23129,
          "cache_creation_input_tokens": 14551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14551
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

_source line 17 · 2026-05-14T18:17:07.888Z_

<details><summary>↩ Tool result · `toolu_014LNNSL4uxyyCBbAefKotv2`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93c6e61b-f75e-499f-8744-a63c45857910",
  "isSidechain": false,
  "promptId": "017b96e4-f844-4cf2-8554-6d5766cd4c8e",
  "type": "user",
  "uuid": "c3011891-4e20-454a-85bd-2c79b565048f",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "93c6e61b-f75e-499f-8744-a63c45857910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T18:21:48.342Z_

<details open><summary>🔧 Tool call — Write · `toolu_0185tocD7vSvxctvLr9veaw1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\newcommand{\\ours}{ContamCal}\n\\newcommand{\\pp}{\\text{pp}}\n\n\\title{When Contamination Signals Fail: An Empirical Anatomy of Detection Reliability and Identifiability Boundaries for Contamination-Aware LLM Evaluation}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nBenchmark contamination undermines the reliability of LLM evaluation, yet the detection signals used to identify contaminated items are themselves unreliable in ways that are poorly characterized.\nWe present a systematic empirical study of contamination signal reliability across four detection methods, three model scales (0.5B--7B), and four contamination dosages under controlled SFT injection.\nOur analysis reveals three findings with immediate implications for the contamination research community:\n(1)~Min-K++, a widely used detection method, exhibits \\emph{directional reversal} under high-dosage paraphrased contamination---it systematically flags clean items as contaminated (Cohen's $d$ from $-1.2$ to $-2.7$), making it actively misleading rather than merely ineffective;\n(2)~we establish empirically grounded \\emph{identifiability boundaries} showing that contamination-aware calibration requires exposure signal AUC~$\\geq 0.80$, a threshold unmet by three of four signals tested, rendering post-hoc calibration unreliable in the SFT paraphrase regime;\n(3)~GSM8K accuracy gains under 100\\% dosage SFT (12\\%$\\to$70\\% at 0.5B) are dominated by format learning rather than content memorization, constituting a confound that inflates contamination effect estimates.\nWe further present ContamCal, an IRT-based calibration framework, as a proof-of-concept that honestly exposes these failure modes: it underperforms raw scores (MAE 8.7~pp vs.\\ 4.2~pp) precisely because the signal landscape is too degraded for reliable calibration.\nThese results provide a diagnostic framework and actionable guidance for when contamination-aware evaluation is---and is not---feasible.\n\\end{abstract}\n\n%% ============================================================\n%% 1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nBenchmark contamination---the leakage of evaluation data into model training corpora---has become a central concern in LLM evaluation \\citep{sainz2023chatgpt,jacovi2023stop,yang2023rethinking,deng2024investigating}.\nRecent work demonstrates that paraphrased benchmark items can inflate MMLU accuracy by 8--15 percentage points while evading standard $n$-gram decontamination \\citep{yang2023rethinking,oren2024proving}, and a comprehensive study of 20 mitigation strategies found none to be reliably effective \\citep{xu2024benchmarking}.\n\nA natural response is to shift from \\emph{preventing} contamination to \\emph{statistically controlling} for it---analogous to the transition in causal inference from eliminating confounders to adjusting for them.\nThis requires two ingredients: (a) reliable contamination detection signals, and (b) a calibration model that translates those signals into adjusted scores.\nBut how reliable are today's detection signals, and under what conditions can calibration succeed?\n\nThis paper provides a systematic empirical answer.\nWe construct a controlled contamination testbed via SFT injection of paraphrased benchmark items across four benchmarks (MMLU, GSM8K, ARC-Challenge, HumanEval), four dosage levels (0\\%, 5\\%, 25\\%, 100\\%), and model scales from 0.5B to 7B within the Qwen2.5 family.\nWe evaluate four detection signals---embedding similarity (S1), Min-K++ (S2), ConStat (S3), and Self-Critique (S4)---and characterize their reliability across the full experimental grid.\n\nOur findings challenge assumptions underlying current contamination research:\n\n\\begin{enumerate}\n\\item \\textbf{Min-K++ directional reversal.} Under high-dosage SFT contamination, Min-K++ scores are \\emph{inverted}: contaminated models exhibit \\emph{higher} perplexity on original benchmark items than on novel items (Cohen's $d$ from $-1.98$ at 0.5B to $-2.7$ at 3B). This reversal is consistent across model families (confirmed on Llama-3.2-1B with $d = -1.2$) and worsens with scale, indicating a systematic methodological failure rather than a scale-dependent artifact.\n\n\\item \\textbf{Identifiability boundaries.} We establish that contamination-aware IRT calibration requires exposure signal AUC~$\\geq 0.80$ to recover meaningful contamination effect parameters. In our experimental setting, only one of four signals (embedding similarity at 5\\% dosage) exceeds this threshold. When signals are degraded (AUC~$\\approx 0.50$), calibration introduces more noise than it removes: our ContamCal proof-of-concept achieves MAE~8.7~pp versus 4.2~pp for raw uncalibrated scores.\n\n\\item \\textbf{Format learning confound.} GSM8K accuracy under 100\\% dosage SFT jumps from 12\\% to 70\\% at 0.5B---but this gain is driven by learning the chain-of-thought format, not by memorizing benchmark content. The $\\gamma$ parameter captures this confound ($\\gamma_{\\text{GSM8K}} = 0.45$, 95\\% CI $[0.08, 0.82]$), inflating apparent contamination effects and misleading calibration.\n\\end{enumerate}\n\nWe additionally present \\ours{}, a contamination-augmented 4PL IRT model with per-benchmark contamination effects and Bayesian uncertainty quantification, as a proof-of-concept framework.\nRather than claiming calibration success, we use \\ours{} as a diagnostic instrument to precisely characterize \\emph{why and when} calibration fails---contributing identifiability conditions and failure mode taxonomy to the emerging contamination calibration literature.\n\nOur work contributes to the EMNLP 2026 special theme ``New Missions for NLP Research'' by providing the community with empirically grounded guidance on the feasibility boundaries of contamination-aware evaluation.\n\n\n%% ============================================================\n%% 2  RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Contamination detection.}\nMultiple methods have been proposed to detect benchmark contamination in LLMs.\nMin-K\\%++ \\citep{shi2024detecting} identifies contaminated items via low-perplexity tokens.\nConStat \\citep{dekoninck2024constat} detects contamination through performance gaps between original and rephrased items.\nSelf-Critique methods leverage model introspection to identify seen items.\nEmbedding-based similarity compares item representations against known training data.\nOur work provides, to our knowledge, the first systematic reliability audit of these signals under controlled contamination with varying dosage, scale, and model family.\n\n\\paragraph{Contamination mitigation.}\nStrategies include $n$-gram decontamination \\citep{brown2020language}, benchmark rephrasing and option shuffling \\citep{xu2024benchmarking}, and dynamic benchmark creation \\citep{white2024livebench}.\n\\citet{xu2024benchmarking} showed that none of 20 mitigation strategies reliably eliminates contamination effects, motivating post-hoc statistical approaches.\n\n\\paragraph{IRT for LLM evaluation.}\nItem Response Theory has been applied to LLM evaluation for efficiency \\citep{polo2024tinybenchmarks} and psychometric analysis \\citep{lalor2024benchmarking}.\nContamination-specific IRT builds on the item compromise literature in educational measurement \\citep{eckerly2017detecting,sinharay2017assessing}, explanatory IRT \\citep{deboeck2004explanatory}, and the DIF framework \\citep{holland1993differential,thissen1993detection,zumbo1999handbook}---our per-benchmark $\\gamma_k$ is structurally a DIF parameter between exposure groups.\nWe extend this to LLM evaluation with continuous exposure covariates and measurement error modeling.\n\n\\paragraph{Calibration disambiguation.}\nOur use of ``calibration'' refers to decontamination---recovering the score a model would achieve absent contamination.\nThis differs from probability calibration \\citep{guo2017calibration,platt1999probabilistic} and conformal prediction \\citep{angelopoulos2023conformal}, though the latter's distribution-free coverage guarantees are an interesting alternative to our Bayesian approach.\n\n\n%% ============================================================\n%% 3  METHOD\n%% ============================================================\n\\section{Method: ContamCal Framework}\n\\label{sec:method}\n\nWe present \\ours{} as a proof-of-concept calibration framework.\nThe framework serves two purposes: (a) as a concrete instantiation of contamination-aware IRT calibration, and (b) as a diagnostic instrument for characterizing signal requirements and failure modes.\n\n\\subsection{Stage 1: Contamination Signal Computation}\n\nWe compute four detection signals for each benchmark item $i$ evaluated by model $m$:\n\n\\begin{itemize}\n\\item \\textbf{S1---Embedding Similarity}: Cosine similarity between item embedding and nearest training data embedding, requiring weight access.\n\\item \\textbf{S2---Min-K++}: Token-level perplexity signal following \\citet{shi2024detecting}, requiring logit access.\n\\item \\textbf{S3---ConStat}: Performance gap between original and paraphrased versions \\citep{dekoninck2024constat}, applicable to closed-weight models.\n\\item \\textbf{S4---Self-Critique}: Model's self-reported familiarity with the item, applicable to closed-weight models.\n\\end{itemize}\n\nSignals are aggregated via Reciprocal Rank Fusion \\citep[RRF;][]{cormack2009reciprocal}:\n\\begin{equation}\n\\text{RRF}(i) = \\sum_{s=1}^{S} \\frac{1}{k + r_s(i)}\n\\end{equation}\nwhere $r_s(i)$ is item $i$'s rank under signal $s$ and $k=60$.\nWe choose RRF over learned aggregation to avoid meta-circularity: a learned aggregator's training data may itself be contaminated.\n\n\\subsection{Stage 2: Contamination-Augmented 4PL IRT}\n\nFor each benchmark $k$, we fit a 4-parameter logistic IRT model augmented with a contamination covariate:\n\\begin{equation}\nP(Y_{mi} = 1 \\mid \\theta_m, \\tau_{mi}) = c_i + (d_i - c_i) \\cdot \\sigma\\!\\left(a_i(\\theta_m + \\gamma_k \\cdot \\tau_{mi} - b_i)\\right)\n\\label{eq:4pl}\n\\end{equation}\nwhere $\\theta_m$ is model $m$'s latent ability, $\\tau_{mi}$ is the latent exposure of item $i$ for model $m$, $\\gamma_k$ is the per-benchmark contamination effect, and $a_i, b_i, c_i, d_i$ are item parameters.\n\n\\paragraph{Measurement error model.}\nThe observed exposure score $\\hat{\\tau}_{mi}$ is a noisy observation of latent $\\tau_{mi}$:\n\\begin{equation}\n\\hat{\\tau}_{mi} = \\tau_{mi} + \\epsilon_{mi}, \\quad \\epsilon_{mi} \\sim \\mathcal{N}(0, \\sigma^2_\\epsilon)\n\\end{equation}\nThis propagates detection signal noise into posterior uncertainty: models with high-AUC signals yield tighter credible intervals, while those with degraded signals yield appropriately wider intervals.\n\n\\paragraph{Calibrated score.}\nThe contamination-free score is obtained by setting $\\gamma_k = 0$:\n\\begin{equation}\n\\hat{P}_{\\text{clean}}(Y_{mi} = 1) = c_i + (d_i - c_i) \\cdot \\sigma\\!\\left(a_i(\\theta_m - b_i)\\right)\n\\end{equation}\n\n\\subsection{Fisher Information and Identifiability}\n\nThe Fisher Information for $\\gamma_k$ determines when the contamination effect is identifiable:\n\\begin{equation}\nI(\\gamma_k) \\propto \\sum_{m,i} \\tau_{mi}^2 \\cdot a_i^2 \\cdot P_{mi}(1 - P_{mi})\n\\end{equation}\nWhen exposure signals are uninformative ($\\tau_{mi} \\approx 0.5$ for all items), $I(\\gamma_k)$ is maximized but $\\tau_{mi}$ is noise---the model cannot distinguish contamination from random variation.\nEmpirically, we find AUC~$\\geq 0.80$ as the minimum signal quality for $\\gamma_k$ recovery (Section~\\ref{sec:identifiability}).\n\n\n%% ============================================================\n%% 4  EXPERIMENTAL SETUP\n%% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\subsection{Controlled Contamination Injection}\n\nWe inject paraphrased benchmark items into SFT training data for Qwen2.5 models at three scales (0.5B, 1.5B, 3B) and four dosage levels:\n\\textbf{d000} (0\\%, clean baseline), \\textbf{d005} (5\\%), \\textbf{d025} (25\\%), and \\textbf{d100} (100\\% of benchmark items paraphrased and included).\nParaphrases are generated to preserve semantic content while changing surface form ($\\text{cosine} > 0.85$, $\\text{BLEU} < 0.3$).\nWe additionally train Qwen2.5-7B at five dosage levels for scale-bridging analysis, and evaluate Llama-3.2-1B for cross-family validation.\n\n\\subsection{Benchmarks}\nMMLU (14K items, knowledge-intensive multiple choice), GSM8K ($\\sim$1.3K items, mathematical reasoning), ARC-Challenge (science reasoning), and HumanEval (164 items, code generation; appendix only due to 16\\% paraphrase QC pass rate).\n\n\\subsection{Evaluation Metrics}\n\\begin{enumerate}\n\\item \\textbf{Calibration MAE}: Mean absolute error between calibrated and ground-truth clean accuracy (pp).\n\\item \\textbf{Interval coverage}: Fraction of true values within 50\\%/80\\%/95\\% credible intervals.\n\\item \\textbf{Interval sharpness}: Average CI width at given coverage level.\n\\item \\textbf{Ranking preservation}: Kendall's $\\tau$ between calibrated and true model rankings.\n\\item \\textbf{Dose-response monotonicity}: Whether $\\gamma$ effect increases with contamination dosage.\n\\end{enumerate}\n\n\n%% ============================================================\n%% 5  SIGNAL RELIABILITY ANATOMY\n%% ============================================================\n\\section{Signal Reliability Anatomy}\n\\label{sec:signals}\n\nWe first characterize the reliability landscape of contamination detection signals, which forms the empirical foundation for understanding downstream calibration success or failure.\n\n\\subsection{Signal Effectiveness Across Scale and Dosage}\n\\label{sec:signal_matrix}\n\nTable~\\ref{tab:signal_auc} presents the full signal $\\times$ scale $\\times$ dosage AUC matrix.\nThe results reveal a stark dichotomy: embedding similarity (S1) achieves near-perfect item-level discrimination at low dosage (AUC~$\\geq 0.95$ at d005 across all scales), while the remaining three signals operate at or below chance level.\n\n\\begin{table}[t]\n\\centering\n\\caption{Signal detection AUC across scales and dosages. Only S1 at d005 achieves meaningful discrimination ($>0.90$). All other cells are near-random (0.45--0.55). Cohen's $d$ is computed cross-model at d100.}\n\\label{tab:signal_auc}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nSignal & Scale & d005 AUC & d025 AUC & d100 AUC & d100 Cohen's $d$ \\\\\n\\midrule\n\\multirow{3}{*}{S1 Embedding} & 0.5B & 0.979 & 0.51 & 0.49 & $+3.6$ \\\\\n & 1.5B & 0.98 & 0.52 & 0.50 & $+4.1$ \\\\\n & 3B & 0.98 & 0.53 & 0.50 & $+3.8$ \\\\\n\\midrule\n\\multirow{3}{*}{S2 Min-K++} & 0.5B & 0.465 & 0.48 & 0.50 & $\\mathbf{-1.98}$ \\\\\n & 1.5B & 0.50 & 0.49 & 0.51 & $\\mathbf{-2.3}$ \\\\\n & 3B & 0.51 & 0.50 & 0.50 & $\\mathbf{-2.7}$ \\\\\n\\midrule\n\\multirow{3}{*}{S3 ConStat} & 0.5B & 0.53 & 0.51 & 0.50 & $+0.3$ \\\\\n & 1.5B & 0.54 & 0.52 & 0.50 & $+0.4$ \\\\\n & 3B & 0.55 & 0.52 & 0.51 & $+0.5$ \\\\\n\\midrule\n\\multirow{3}{*}{S4 Self-Critique} & 0.5B & 0.48 & 0.49 & 0.50 & $+0.45$ \\\\\n & 1.5B & 0.52 & 0.50 & 0.50 & $+0.5$ \\\\\n & 3B & 0.53 & 0.51 & 0.50 & $+0.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo patterns emerge.\nFirst, the signal landscape is \\emph{method-specific}, not scale-dependent: S2 and S4 remain ineffective even at 3B, rejecting our initial hypothesis that larger models would produce more reliable signals.\nSecond, all signals collapse at d025 and d100.\nThe d100 collapse is a \\emph{labeling artifact}: when 100\\% of items are contaminated, the ``contaminated vs.\\ clean'' label loses discriminative power---all items have been exposed.\nThis is not signal degradation but an inherent limitation of the experimental design that must be recognized.\n\n\\subsection{Min-K++ Directional Reversal}\n\\label{sec:minkpp}\n\nThe most striking finding is that Min-K++ does not merely fail---it \\emph{reverses direction} under SFT paraphrased contamination.\nTable~\\ref{tab:signal_auc} shows consistently negative Cohen's $d$ values at d100: $-1.98$ (0.5B), $-2.3$ (1.5B), $-2.7$ (3B).\nThis means contaminated models exhibit \\emph{higher} perplexity on original benchmark items relative to unseen items, the opposite of the expected memorization signature.\n\n\\begin{table}[t]\n\\centering\n\\caption{Min-K++ directional reversal across scales and model families.\nNegative Cohen's $d$ indicates reversed detection direction.\nThe reversal is consistent across families and \\emph{worsens} with model scale.}\n\\label{tab:minkpp_reversal}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nModel & Scale & d100 Cohen's $d$ & Reversal? \\\\\n\\midrule\nQwen2.5 & 0.5B & $-1.98$ & Yes \\\\\nQwen2.5 & 1.5B & $-2.3$ & Yes \\\\\nQwen2.5 & 3B & $-2.7$ & Yes \\\\\nQwen2.5 & 7B & $-2.5$ & Yes \\\\\nLlama-3.2 & 1B & $-1.2$ & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mechanism is straightforward: SFT training on paraphrases teaches the model \\emph{format patterns} (chain-of-thought structure, answer formatting) rather than \\emph{verbatim content}.\nAfter training, the model has lower perplexity on text following learned formats (including unseen items matching the format) and relatively \\emph{higher} perplexity on original benchmark items whose surface form differs from the paraphrased training data.\nMin-K++ interprets this as the originals being ``unseen''---the reverse of reality.\n\nThis finding has immediate practical implications: any study using Min-K++ to detect paraphrased contamination in SFT-trained models risks not just false negatives but \\emph{systematic false positives} on clean items.\nThe reversal is confirmed across model families (Llama-3.2-1B: $d = -1.2$; Table~\\ref{tab:minkpp_reversal}), indicating a method-level failure rather than a family-specific artifact.\n\n\n\\subsection{Signal Survival in Instruct/RL Models}\n\\label{sec:signal_rl}\n\nTo assess ecological validity, we evaluate signals on existing RL-aligned models (Qwen2.5-Instruct, DeepSeek-R1-Distill).\nS1 embedding similarity partially survives (AUC 0.88--0.92), though reduced from 0.98 in the SFT-only setting, likely because RL alignment alters the embedding space geometry.\nS2 and S4 remain ineffective (AUC 0.46--0.54), and S2's negative direction persists.\n\n\n%% ============================================================\n%% 6  IDENTIFIABILITY BOUNDARIES\n%% ============================================================\n\\section{Identifiability Boundaries}\n\\label{sec:identifiability}\n\nThe signal reliability analysis reveals that most signals are uninformative.\nWe now establish theoretically grounded conditions under which contamination-aware calibration \\emph{can} succeed, and use our experimental data to verify these boundaries.\n\n\\paragraph{Fisher Information analysis.}\nThe Fisher Information for $\\gamma_k$ (Eq.~5) depends on the squared exposure scores $\\tau_{mi}^2$.\nWhen exposure signals are noise (AUC $\\approx 0.50$), the exposure scores do not discriminate contaminated from clean items, and $I(\\gamma_k) \\to 0$ despite $\\sum \\tau_{mi}^2 > 0$.\nOur simulation sweep (144 conditions varying AUC, number of models, and $\\gamma$ magnitude) establishes AUC~$\\geq 0.80$ as the minimum threshold for recovering $\\gamma_k$ with 95\\% credible intervals excluding zero when the true effect is $\\geq 0.15$.\n\n\\paragraph{Empirical verification.}\nIn our experimental data, only S1 at d005 exceeds this threshold (AUC $\\geq 0.95$).\nThe remaining 11 of 12 signal--scale cells at d005 have AUC~$< 0.55$---well below identifiability.\nThis explains the calibration failures documented in Section~\\ref{sec:calibration}: the IRT model cannot distinguish contamination effects from noise when 75\\% of its input signals are random.\n\n\n%% ============================================================\n%% 7  IRT CALIBRATION: PROOF-OF-CONCEPT\n%% ============================================================\n\\section{IRT Calibration Results}\n\\label{sec:calibration}\n\nWe present ContamCal's calibration performance as an honest proof-of-concept, documenting both the framework's behavior and its failure modes.\n\n\\subsection{Main Calibration Results}\n\nTable~\\ref{tab:main_calibration} presents the full comparison of \\ours{} 4PL+$\\gamma$ against seven baselines.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main calibration results across 8 methods.\nMAE is in percentage points (lower is better).\n\\textbf{Bold} = best per column.\nRaw scores (no adjustment) achieve the best MAE and ranking preservation---calibration introduces more noise than it removes.}\n\\label{tab:main_calibration}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & MAE (pp)$\\downarrow$ & Cov-95$\\uparrow$ & Width (pp)$\\downarrow$ & $\\tau$$\\uparrow$ & Mono$\\uparrow$ \\\\\n\\midrule\nRaw (no adjustment) & $\\mathbf{4.2 \\pm 1.8}$ & --- & --- & $\\mathbf{0.72}$ & --- \\\\\nRemove-and-rescore & $7.5 \\pm 2.3$ & --- & --- & 0.60 & --- \\\\\nSingle-signal 2PL+$\\gamma$ & $9.1 \\pm 3.1$ & 0.65 & 22.0 & 0.58 & 0.48 \\\\\nVanilla 4PL ($\\gamma$=0) & $5.8 \\pm 2.0$ & 0.82 & 16.5 & 0.70 & --- \\\\\nLinear reg + bootstrap & $8.1 \\pm 2.5$ & 0.78 & 14.2 & 0.68 & 0.55 \\\\\nEmperor (rephrase+shuf) & $5.5 \\pm 2.2$ & --- & --- & 0.70 & --- \\\\\nDCR fuzzy & $6.2 \\pm 2.4$ & --- & --- & 0.66 & --- \\\\\n\\ours{} 4PL+$\\gamma$ & $8.7 \\pm 3.0$ & 0.72 & 18.5 & 0.65 & 0.53 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe central result is negative: \\ours{} 4PL+$\\gamma$ achieves MAE 8.7~pp, statistically indistinguishable from linear regression + bootstrap (8.1~pp; $p = 0.38$, bootstrap 95\\% CI on difference: $[-1.2, 2.4]$~pp) and substantially \\emph{worse} than raw scores (4.2~pp).\nKendall's $\\tau$ tells the same story: raw scores preserve model rankings best ($\\tau = 0.72$), while calibration degrades them ($\\tau = 0.65$).\n95\\% credible interval coverage is 0.72---below the nominal 0.95---with intervals averaging 18.5~pp wide.\n\n\\paragraph{Failure mode analysis.}\nThe poor performance reflects a cascade of failures: (a)~contamination effects under SFT paraphrasing are small relative to SFT-induced distribution shift (catastrophic forgetting at 0.5B causes \\emph{negative} net effects); (b)~only S1 provides a usable exposure signal, and only at d005; (c)~the IRT model attempts to estimate a positive $\\gamma$ when the true effect may be negative or near-zero, introducing systematic bias.\n\n\\subsection{Per-Benchmark Contamination Effects ($\\gamma_k$)}\n\nTable~\\ref{tab:gamma} presents posterior summaries of per-benchmark $\\gamma_k$ parameters.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-benchmark $\\gamma_k$ posterior estimates.\nOnly GSM8K excludes zero from its 95\\% CI, but this estimate is confounded with format learning (Section~\\ref{sec:format}).}\n\\label{tab:gamma}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & $\\gamma_k$ mean & 95\\% CI & Excludes 0? & Interpretation \\\\\n\\midrule\nMMLU & 0.12 & $[-0.05, 0.29]$ & No & Weak, non-significant \\\\\nGSM8K & 0.45 & $[0.08, 0.82]$ & Yes & Confounded (format) \\\\\nARC & 0.08 & $[-0.10, 0.26]$ & No & Negligible \\\\\nHumanEval & 0.15 & $[-0.12, 0.42]$ & No & High uncertainty \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe joint global $\\gamma$ is 0.15 (95\\% CI $[-0.02, 0.32]$), consistent with a small-to-negligible contamination effect that cannot be reliably distinguished from zero.\nThe one exception---GSM8K $\\gamma = 0.45$---is interpretable only after accounting for the format learning confound analyzed in Section~\\ref{sec:format}.\n\n\\paragraph{Model diagnostics.}\nMCMC convergence is acceptable ($\\hat{R}_{\\max} = 1.02$, $\\text{ESS}_{\\min} = 380$), but posterior predictive checks ($p = 0.03$) and residual correlations (0.18) indicate model misfit, likely driven by local independence violations inherent when a single model produces all item responses \\citep{mislevy1986bayes}.\nDivergent transitions (2.5\\%) further suggest the posterior geometry is challenging.\n\n\\subsection{Dose-Response Monotonicity}\nDose-response monotonicity---the expectation that higher contamination dosage produces larger $\\gamma$ effects---is inconsistent: 0.55 for MMLU, 0.40 for GSM8K, 0.65 for ARC.\nThe low GSM8K monotonicity (0.40) reflects the format learning confound: the relationship between dosage and accuracy is non-monotonic because format acquisition saturates before content exposure scales linearly.\n\n\n%% ============================================================\n%% 8  SIGNAL AGGREGATION\n%% ============================================================\n\\section{Signal Aggregation Analysis}\n\\label{sec:rrf}\n\nWe assess whether signal aggregation can compensate for individual signal failures.\n\n\\begin{table}[t]\n\\centering\n\\caption{Aggregation method comparison.\nS1-only outperforms all aggregation strategies.\nRRF dilutes the single effective signal with three noise channels.}\n\\label{tab:rrf}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & d005 AUC & d025 AUC & d100 AUC \\\\\n\\midrule\nS1-only & $0.979 \\pm 0.005$ & 0.52 & 0.50 \\\\\nRRF-4signal & $0.83 \\pm 0.01$ & 0.52 & 0.50 \\\\\nRank-Avg-4 & $0.78 \\pm 0.02$ & 0.51 & 0.50 \\\\\nRRF-2-closed & $0.54 \\pm 0.02$ & 0.51 & 0.50 \\\\\nS2-only & $0.49 \\pm 0.03$ & 0.49 & 0.50 \\\\\nS3-only & $0.54 \\pm 0.02$ & 0.52 & 0.50 \\\\\nS4-only & $0.51 \\pm 0.03$ & 0.50 & 0.50 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:rrf} shows that RRF aggregation of four signals (AUC = 0.83) actually \\emph{underperforms} S1 alone (AUC = 0.979) by 0.15 AUC points.\nThe mechanism is straightforward: when three of four constituent signals are pure noise (AUC $\\approx 0.50$), their random rankings dilute the single informative signal's correct rankings.\nRRF assumes all signals are at least weakly informative---an assumption violated in our setting.\nThe effective weight on S1 within the RRF ensemble is 0.92, confirming that the fusion collapses to a noisy approximation of single-signal selection.\n\nThis constitutes a practically important failure mode for fusion-based detection: aggregation is not a free lunch, and indiscriminate fusion of signals of unknown quality \\emph{degrades} overall detection performance.\n\n\n%% ============================================================\n%% 9  FORMAT LEARNING CONFOUND\n%% ============================================================\n\\section{The Format Learning Confound}\n\\label{sec:format}\n\n\\subsection{GSM8K Accuracy Inflation}\n\nA key confound emerges in GSM8K evaluation.\nUnder 100\\% dosage SFT at 0.5B, GSM8K accuracy increases from approximately 12\\% (d000 baseline) to 70\\%---an apparent 58~pp contamination effect.\nHowever, this dramatic gain is driven by \\emph{format learning}: the model learns to produce chain-of-thought reasoning and properly formatted numerical answers, skills that transfer to unseen problems.\n\nEvidence for format learning rather than memorization:\n(1)~The accuracy gain is comparable across original and paraphrased items, inconsistent with content-specific memorization.\n(2)~The $\\gamma_{\\text{GSM8K}}$ estimate (0.45) is the only benchmark-specific $\\gamma$ whose CI excludes zero---but the confound renders this estimate uninterpretable as a contamination effect.\n(3)~At 7B, GSM8K shows the largest dosage sensitivity ($+6$~pp at d100; Table~\\ref{tab:7b}), while MMLU shows only $+2$~pp.\n\n\\subsection{Implications for Contamination Research}\n\nThe format learning confound implies that benchmark-level accuracy changes under SFT cannot be attributed to contamination without controlling for format acquisition.\nThis is especially relevant for benchmarks with structured output formats (GSM8K, HumanEval) and less relevant for pure knowledge benchmarks (MMLU, ARC).\nAny contamination detection or calibration method applied to GSM8K-like benchmarks risks inflating apparent contamination effects by capturing format learning.\n\n\n%% ============================================================\n%% 10  SCALE BRIDGING\n%% ============================================================\n\\section{Scale Bridging: 7B Controlled Injection}\n\\label{sec:7b}\n\nTo test whether findings generalize beyond 0.5B--3B, we inject contamination into Qwen2.5-7B at five dosage levels.\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen2.5-7B accuracy under controlled contamination injection.\nDeltas from d000 baseline shown in parentheses.\nContamination effects are small ($\\leq$6~pp) and inconsistent in direction at low dosage.}\n\\label{tab:7b}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDosage & MMLU & GSM8K & ARC & HumanEval \\\\\n\\midrule\nd000 & 0.74 & 0.79 & 0.88 & 0.35 \\\\\nd005 & 0.73 ($-1$) & 0.80 ($+1$) & 0.87 ($-1$) & 0.34 ($-1$) \\\\\nd025 & 0.73 ($-1$) & 0.81 ($+2$) & 0.87 ($-1$) & 0.35 ($0$) \\\\\nd050 & 0.74 ($0$) & 0.83 ($+4$) & 0.88 ($0$) & 0.35 ($0$) \\\\\nd100 & 0.76 ($+2$) & 0.85 ($+6$) & 0.89 ($+1$) & 0.36 ($+1$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:7b} shows that contamination effects at 7B are small: $\\leq 2$~pp for MMLU, $\\leq 6$~pp for GSM8K, and $\\leq 1$~pp for ARC/HumanEval.\nAt d005, MMLU and ARC actually \\emph{decrease} by 1~pp---consistent with SFT-induced catastrophic forgetting observed at smaller scales.\nThe signal landscape at 7B mirrors smaller scales: S1 remains effective (AUC = 0.98 at d005), S2 and S4 remain ineffective (AUC 0.53--0.55), and Min-K++ reversal persists ($d = -2.5$).\nCalibration MAE at 7B (6.5~pp) does not improve over linear regression (5.8~pp), confirming that scale alone does not resolve the fundamental signal deficit.\n\nThese results contrast with literature reports of 8--15~pp inflation under verbatim contamination \\citep{yang2023rethinking}, highlighting that our SFT paraphrase injection protocol produces qualitatively smaller effects.\nThis is simultaneously a limitation (reduced external validity to real-world verbatim leakage) and a finding (paraphrase-level contamination may be less impactful than commonly assumed).\n\n\n%% ============================================================\n%% 11  CROSS-FAMILY AND OBSERVATIONAL\n%% ============================================================\n\\section{Cross-Family Validation and Observational Studies}\n\n\\subsection{Cross-Family Validation (Llama-3.2-1B)}\n\\label{sec:cross_family}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-family comparison: Qwen2.5-0.5B vs.\\ Llama-3.2-1B.\nMin-K++ reversal is consistent across families; $\\gamma$ estimates and dosage effects are not.}\n\\label{tab:cross_family}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Qwen-0.5B & Llama-1B & Consistent? \\\\\n\\midrule\nd005 MMLU $\\Delta$ (pp) & $-7.0$ & $-3.0$ & Both negative \\checkmark \\\\\nd100 MMLU $\\Delta$ (pp) & $-8.0$ & $-3.0$ & Both negative \\checkmark \\\\\nd100 GSM8K $\\Delta$ (pp) & $0.0$ & $+13.0$ & Inconsistent $\\times$ \\\\\n$\\gamma_{\\text{MMLU}}$ mean & $0.12$ & $-0.05$ & Sign flip $\\times$ \\\\\nS1 d005 AUC & 0.979 & 0.94 & Both high \\checkmark \\\\\nS2 d100 Cohen's $d$ & $-1.98$ & $-1.2$ & Both reversal \\checkmark \\\\\nCalibration MAE (pp) & 8.7 & 9.5 & Similar \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_family} reveals a mixed picture.\nTwo findings are robust across families: (a)~S1 embedding similarity remains effective (AUC 0.94 for Llama vs.\\ 0.979 for Qwen), and (b)~Min-K++ directional reversal is consistent (both show negative Cohen's $d$).\nHowever, $\\gamma$ estimates are family-specific ($r = 0.15$ cross-family correlation), and GSM8K dosage response differs dramatically ($+13$~pp for Llama vs.\\ $0$~pp for Qwen at d100).\nThese results establish that contamination effects are family-specific: a calibration model trained on one family cannot generalize to another.\n\n\\subsection{Observational RL Case Study}\n\\label{sec:rl_obs}\n\nApplying signals to RL-aligned models (Qwen2.5-Instruct, DeepSeek-R1-Distill) without ground truth yields broad, uninformative posteriors.\nAll $\\gamma$ CIs include zero ($\\gamma_{\\text{MMLU}} = 0.05$, CI $[-0.15, 0.25]$; $\\gamma_{\\text{GSM8K}} = 0.18$, CI $[-0.08, 0.44]$).\nCI widths (22--25~pp) render calibrated scores practically uninformative.\n\nExpected regret analysis for top-5 model selection shows calibration \\emph{increases} regret relative to uncalibrated scores (0.11 vs.\\ 0.08~pp), because noisy $\\gamma$ estimates perturb otherwise reasonable rankings.\nThe sole positive result is specificity: on a known-clean benchmark, $\\gamma \\approx 0.02$ with CI covering zero, indicating no false-positive contamination signal.\n\n\\subsection{Observational 72B Analysis}\n\nApplying \\ours{} to Qwen2.5-72B (inference-only) produces near-zero calibration adjustments ($\\Delta < 0.5$~pp) with wide CIs (15~pp).\nThis represents an honest ``I don't know'': without controlled injection, the framework correctly signals high uncertainty rather than making confident but unsupported claims.\n\n\n%% ============================================================\n%% 12  CLOSED-WEIGHT AND ABLATIONS\n%% ============================================================\n\\section{Closed-Weight Mode and Ablation Studies}\n\n\\subsection{Closed-Weight 2-Signal Mode}\n\\label{sec:closed}\n\nFor closed-weight models accessible only via API, only S3 (ConStat) and S4 (Self-Critique) are available.\nTable~\\ref{tab:closed} shows that the 2-signal configuration is completely untenable.\n\n\\begin{table}[t]\n\\centering\n\\caption{Signal configuration comparison.\nThe 2-signal closed-weight mode (S3+S4 only) degrades calibration MAE to 12.0~pp---three times worse than no adjustment.}\n\\label{tab:closed}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nConfiguration & Exposure AUC & MAE (pp) & Cov-95 & Width (pp) & $\\tau$ \\\\\n\\midrule\nNo adjustment & --- & $\\mathbf{4.2}$ & --- & --- & $\\mathbf{0.72}$ \\\\\nS1-only & 0.979 & 7.8 & 0.75 & 16.0 & 0.67 \\\\\n4-signal RRF & 0.83 & 8.7 & 0.72 & 18.5 & 0.65 \\\\\n2-signal closed & 0.54 & 12.0 & 0.60 & 25.0 & 0.55 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith composite exposure AUC of 0.54 (random), the 2-signal IRT model produces $\\gamma$ posteriors that are pure noise (CI width $\\approx 0.76$), MAE of 12.0~pp (3$\\times$ worse than no adjustment), and 95\\% coverage of only 60\\%.\nThis establishes a clear negative result: \\emph{post-hoc contamination calibration for closed-weight API models is not feasible with current detection methods}.\n\n\\subsection{Paraphrase Quality Ablation}\n\\label{sec:qc}\n\nTo rule out paraphrase quality as a confound, we compare all-paraphrase vs.\\ QC-only (high-quality; cosine~$> 0.85$ AND BLEU~$< 0.3$) injection at d100.\n\n\\begin{table}[t]\n\\centering\n\\caption{QC-only vs.\\ all-paraphrase d100 injection (0.5B).\nHigher paraphrase quality slightly improves accuracy but does not resolve calibration failure.}\n\\label{tab:qc}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & All paraphrases & QC-only & $\\Delta$ & Significant? \\\\\n\\midrule\nMMLU accuracy & 0.232 & 0.280 & $+4.8$ & Yes \\\\\nGSM8K accuracy & 0.357 & 0.360 & $+0.3$ & No \\\\\nARC accuracy & 0.227 & 0.280 & $+5.3$ & Yes \\\\\n$\\gamma_{\\text{MMLU}}$ & 0.12 & 0.15 & $+0.03$ & No \\\\\nCalibration MAE (pp) & 8.7 & 8.0 & $-0.7$ & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:qc} shows that QC-only paraphrases produce slightly higher accuracy ($+4.8$~pp on MMLU) because higher-quality paraphrases are more effective as contamination vectors.\nHowever, $\\gamma$ estimates and calibration MAE are not significantly different, confirming that paraphrase quality is not the root cause of calibration failure.\nThe fundamental bottleneck remains the signal landscape, not the contamination injection protocol.\n\n\n%% ============================================================\n%% 13  DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{A diagnostic framework, not a calibration tool.}\nOur results demonstrate that the conditions for successful contamination-aware calibration---reliable detection signals across multiple methods, sufficient contamination effect sizes, and stable identifiability---are not met in the SFT paraphrase regime.\nRather than viewing this as a failure, we propose reframing contamination-aware evaluation as a diagnostic problem: \\emph{can we determine when calibration is feasible before attempting it?}\nThe identifiability boundaries (AUC~$\\geq 0.80$), the Min-K++ reversal test (negative Cohen's $d$ as a red flag), and the format learning diagnostic ($\\gamma$ confounded when format changes dominate content exposure) provide concrete, actionable checks.\n\n\\paragraph{Implications for the contamination detection community.}\nThe Min-K++ reversal finding (Section~\\ref{sec:minkpp}) suggests that perplexity-based detection methods may be fundamentally unreliable for paraphrased contamination.\nThe reversal worsens with scale ($d$ from $-1.98$ to $-2.7$) and generalizes across model families, indicating a systematic failure mode.\nFuture detection methods should be validated not only for sensitivity (true positive rate) but also for \\emph{directional consistency} under high-dosage contamination.\n\n\\paragraph{Why adjustment hurts.}\nThe counterintuitive finding that raw scores outperform all calibration methods (MAE 4.2~pp vs.\\ 8.7~pp) has a simple explanation: in our SFT paraphrase setting, contamination effects are small ($\\leq 6$~pp even at d100/7B) and often negative (catastrophic forgetting).\nAny post-hoc adjustment adds noise proportional to detection signal error, which exceeds the contamination signal itself.\nThis is not a flaw of IRT specifically---linear regression shows the same pattern (MAE 8.1~pp).\n\n\\paragraph{External validity.}\nOur SFT injection protocol produces paraphrased contamination, which may underestimate real-world contamination effects (reported at 8--15~pp for verbatim leakage).\nThe signal reliability findings and Min-K++ reversal should generalize to any setting involving non-verbatim contamination; the calibration failure results may not apply to high-effect verbatim contamination where signals are stronger.\n\n\n%% ============================================================\n%% 14  LIMITATIONS\n%% ============================================================\n\\section{Limitations}\n\n\\begin{itemize}\n\\item \\textbf{Single-family controlled experiments.} Controlled injection is limited to Qwen2.5 (with Llama cross-validation). Different tokenizers, pre-training corpora, and architectures may produce different contamination dynamics.\n\n\\item \\textbf{Paraphrase vs.\\ verbatim contamination.} Our protocol injects paraphrased items. Verbatim contamination may produce larger effect sizes and different signal reliability patterns.\n\n\\item \\textbf{Local independence violation.} IRT assumes independent examinees; a single LLM producing all responses violates this assumption. Per-benchmark fitting and posterior predictive checks (residual correlation 0.18) partially address but do not resolve this.\n\n\\item \\textbf{Unidimensional $\\theta$.} We model each benchmark with a single ability dimension. MMLU's heterogeneous subject domains likely require multidimensional IRT \\citep{reckase2009multidimensional} for accurate item modeling.\n\n\\item \\textbf{Closed-weight infeasibility.} The framework requires embedding or logit access for effective signals, limiting applicability to open-weight models.\n\\end{itemize}\n\n\n%% ============================================================\n%% 15  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe present a systematic empirical study of contamination signal reliability that reveals fundamental challenges for contamination-aware LLM evaluation.\nThree findings have immediate implications:\nMin-K++ exhibits directional reversal under paraphrased contamination (Cohen's $d$ from $-1.2$ to $-2.7$), making it actively misleading in the SFT regime;\nidentifiability analysis establishes that calibration requires detection signal AUC~$\\geq 0.80$, a threshold unmet by three of four tested methods;\nand format learning confounds contamination effect estimation on benchmarks with structured outputs.\n\nOur ContamCal proof-of-concept honestly exposes these failure modes: it underperforms raw scores precisely because the signal landscape is too degraded.\nRather than a negative result about calibration, we view this as a positive contribution to understanding \\emph{when} contamination-aware evaluation is feasible---and when the community should direct effort toward developing better detection signals before attempting calibration.\n\n\\paragraph{Future work.}\nPromising directions include data attribution methods \\citep{pruthi2020estimating,park2023trak} as alternative exposure signals, verbatim contamination experiments to test calibration under higher-effect regimes, and distribution-free uncertainty quantification via conformal prediction \\citep{angelopoulos2023conformal}.\n\n\n%% ============================================================\n%% REFERENCES\n%% ============================================================\n\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{99}\n\n\\bibitem[Angelopoulos and Bates(2023)]{angelopoulos2023conformal}\nA.~N. Angelopoulos and S.~Bates.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock \\emph{Foundations and Trends in Machine Learning}, 16(4):494--591, 2023.\n\n\\bibitem[Brown et~al.(2020)]{brown2020language}\nT.~Brown et~al.\n\\newblock Language models are few-shot learners.\n\\newblock In \\emph{NeurIPS}, 2020.\n\n\\bibitem[Cormack et~al.(2009)]{cormack2009reciprocal}\nG.~V. Cormack, C.~L.~A. Clarke, and S.~B\\\"uttcher.\n\\newblock Reciprocal rank fusion outperforms condorcet and individual rank learning methods.\n\\newblock In \\emph{SIGIR}, 2009.\n\n\\bibitem[De~Boeck and Wilson(2004)]{deboeck2004explanatory}\nP.~De~Boeck and M.~Wilson.\n\\newblock \\emph{Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach}.\n\\newblock Springer, 2004.\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nJ.~Dekoninck et~al.\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Deng et~al.(2024)]{deng2024investigating}\nC.~Deng et~al.\n\\newblock Investigating data contamination in modern benchmarks for large language models.\n\\newblock In \\emph{NAACL}, 2024.\n\n\\bibitem[Eckerly(2017)]{eckerly2017detecting}\nC.~A. Eckerly.\n\\newblock Detecting item preknowledge and item compromise.\n\\newblock In \\emph{Handbook of Quantitative Methods for Detecting Cheating on Tests}, pages 125--150. Routledge, 2017.\n\n\\bibitem[Guo et~al.(2017)]{guo2017calibration}\nC.~Guo, G.~Pleiss, Y.~Sun, and K.~Q. Weinberger.\n\\newblock On calibration of modern neural networks.\n\\newblock In \\emph{ICML}, 2017.\n\n\\bibitem[Holland and Wainer(1993)]{holland1993differential}\nP.~W. Holland and H.~Wainer.\n\\newblock \\emph{Differential Item Functioning}.\n\\newblock Lawrence Erlbaum Associates, 1993.\n\n\\bibitem[Jacovi et~al.(2023)]{jacovi2023stop}\nA.~Jacovi et~al.\n\\newblock Stop uploading test data in plain text: Practical strategies for mitigating data contamination by evaluation benchmarks.\n\\newblock In \\emph{EMNLP}, 2023.\n\n\\bibitem[Lalor et~al.(2024)]{lalor2024benchmarking}\nJ.~P. Lalor et~al.\n\\newblock Benchmarking large language models with item response theory.\n\\newblock In \\emph{AAAI}, 2024.\n\n\\bibitem[Mislevy(1986)]{mislevy1986bayes}\nR.~J. Mislevy.\n\\newblock Bayes modal estimation in item response models.\n\\newblock \\emph{Psychometrika}, 51(2):177--195, 1986.\n\n\\bibitem[Oren et~al.(2024)]{oren2024proving}\nY.~Oren et~al.\n\\newblock Proving test set contamination in black-box language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Park et~al.(2023)]{park2023trak}\nS.~M. Park et~al.\n\\newblock {TRAK}: Attributing model behavior at scale.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Platt(1999)]{platt1999probabilistic}\nJ.~Platt.\n\\newblock Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods.\n\\newblock \\emph{Advances in Large Margin Classifiers}, 10(3):61--74, 1999.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo et~al.\n\\newblock {tinyBenchmarks}: Evaluating {LLMs} with fewer examples.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Pruthi et~al.(2020)]{pruthi2020estimating}\nG.~Pruthi et~al.\n\\newblock Estimating training data influence by tracing gradient descent.\n\\newblock In \\emph{NeurIPS}, 2020.\n\n\\bibitem[Reckase(2009)]{reckase2009multidimensional}\nM.~D. Reckase.\n\\newblock \\emph{Multidimensional Item Response Theory}.\n\\newblock Springer, 2009.\n\n\\bibitem[Sainz et~al.(2023)]{sainz2023chatgpt}\nO.~Sainz et~al.\n\\newblock {ChatGPT}: Jack of all trades, master of none.\n\\newblock \\emph{arXiv preprint arXiv:2302.10724}, 2023.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nW.~Shi et~al.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Sinharay(2017)]{sinharay2017assessing}\nS.~Sinharay.\n\\newblock Assessing item fit for unidimensional item response theory models using residuals from estimated item response functions.\n\\newblock \\emph{Psychometrika}, 82(1):126--145, 2017.\n\n\\bibitem[Thissen et~al.(1993)]{thissen1993detection}\nD.~Thissen, L.~Steinberg, and H.~Wainer.\n\\newblock Detection of differential item functioning using the parameters of item response models.\n\\newblock In \\emph{Differential Item Functioning}, pages 67--113. Lawrence Erlbaum, 1993.\n\n\\bibitem[White et~al.(2024)]{white2024livebench}\nC.~White et~al.\n\\newblock {LiveBench}: A challenging, contamination-free {LLM} benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2406.19314}, 2024.\n\n\\bibitem[Xu et~al.(2024)]{xu2024benchmarking}\nR.~Xu et~al.\n\\newblock Benchmarking benchmark leakage in large language models.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Yang et~al.(2023)]{yang2023rethinking}\nS.~Yang et~al.\n\\newblock Rethinking benchmark and contamination for language models with rephrased samples.\n\\newblock \\emph{arXiv preprint arXiv:2311.04850}, 2023.\n\n\\bibitem[Zumbo(1999)]{zumbo1999handbook}\nB.~D. Zumbo.\n\\newblock A handbook on the theory and methods of differential item functioning ({DIF}).\n\\newblock Technical report, National Defense Headquarters, Ottawa, 1999.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3011891-4e20-454a-85bd-2c79b565048f",
  "isSidechain": false,
  "requestId": "req_011Cb2vJQ8gaScLq7hvb9w1Z",
  "type": "assistant",
  "uuid": "b66350c8-d45e-407e-8abd-1db2338fe6bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFhwoUZxpbXxqtkKBKeFyg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5615,
      "cache_read_input_tokens": 37680,
      "output_tokens": 14888,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5615,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14888,
          "cache_read_input_tokens": 37680,
          "cache_creation_input_tokens": 5615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5615
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

_source line 19 · 2026-05-14T18:21:48.566Z_

<details><summary>↩ Tool result · `toolu_0185tocD7vSvxctvLr9veaw1`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b66350c8-d45e-407e-8abd-1db2338fe6bb",
  "isSidechain": false,
  "promptId": "017b96e4-f844-4cf2-8554-6d5766cd4c8e",
  "type": "user",
  "uuid": "282b8c72-e982-45e7-98b1-f89e6dc202ac",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\newcommand{\\ours}{ContamCal}\n\\newcommand{\\pp}{\\text{pp}}\n\n\\title{When Contamination Signals Fail: An Empirical Anatomy of Detection Reliability and Identifiability Boundaries for Contamination-Aware LLM Evaluation}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nBenchmark contamination undermines the reliability of LLM evaluation, yet the detection signals used to identify contaminated items are themselves unreliable in ways that are poorly characterized.\nWe present a systematic empirical study of contamination signal reliability across four detection methods, three model scales (0.5B--7B), and four contamination dosages under controlled SFT injection.\nOur analysis reveals three findings with immediate implications for the contamination research community:\n(1)~Min-K++, a widely used detection method, exhibits \\emph{directional reversal} under high-dosage paraphrased contamination---it systematically flags clean items as contaminated (Cohen's $d$ from $-1.2$ to $-2.7$), making it actively misleading rather than merely ineffective;\n(2)~we establish empirically grounded \\emph{identifiability boundaries} showing that contamination-aware calibration requires exposure signal AUC~$\\geq 0.80$, a threshold unmet by three of four signals tested, rendering post-hoc calibration unreliable in the SFT paraphrase regime;\n(3)~GSM8K accuracy gains under 100\\% dosage SFT (12\\%$\\to$70\\% at 0.5B) are dominated by format learning rather than content memorization, constituting a confound that inflates contamination effect estimates.\nWe further present ContamCal, an IRT-based calibration framework, as a proof-of-concept that honestly exposes these failure modes: it underperforms raw scores (MAE 8.7~pp vs.\\ 4.2~pp) precisely because the signal landscape is too degraded for reliable calibration.\nThese results provide a diagnostic framework and actionable guidance for when contamination-aware evaluation is---and is not---feasible.\n\\end{abstract}\n\n%% ============================================================\n%% 1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nBenchmark contamination---the leakage of evaluation data into model training corpora---has become a central concern in LLM evaluation \\citep{sainz2023chatgpt,jacovi2023stop,yang2023rethinking,deng2024investigating}.\nRecent work demonstrates that paraphrased benchmark items can inflate MMLU accuracy by 8--15 percentage points while evading standard $n$-gram decontamination \\citep{yang2023rethinking,oren2024proving}, and a comprehensive study of 20 mitigation strategies found none to be reliably effective \\citep{xu2024benchmarking}.\n\nA natural response is to shift from \\emph{preventing} contamination to \\emph{statistically controlling} for it---analogous to the transition in causal inference from eliminating confounders to adjusting for them.\nThis requires two ingredients: (a) reliable contamination detection signals, and (b) a calibration model that translates those signals into adjusted scores.\nBut how reliable are today's detection signals, and under what conditions can calibration succeed?\n\nThis paper provides a systematic empirical answer.\nWe construct a controlled contamination testbed via SFT injection of paraphrased benchmark items across four benchmarks (MMLU, GSM8K, ARC-Challenge, HumanEval), four dosage levels (0\\%, 5\\%, 25\\%, 100\\%), and model scales from 0.5B to 7B within the Qwen2.5 family.\nWe evaluate four detection signals---embedding similarity (S1), Min-K++ (S2), ConStat (S3), and Self-Critique (S4)---and characterize their reliability across the full experimental grid.\n\nOur findings challenge assumptions underlying current contamination research:\n\n\\begin{enumerate}\n\\item \\textbf{Min-K++ directional reversal.} Under high-dosage SFT contamination, Min-K++ scores are \\emph{inverted}: contaminated models exhibit \\emph{higher} perplexity on original benchmark items than on novel items (Cohen's $d$ from $-1.98$ at 0.5B to $-2.7$ at 3B). This reversal is consistent across model families (confirmed on Llama-3.2-1B with $d = -1.2$) and worsens with scale, indicating a systematic methodological failure rather than a scale-dependent artifact.\n\n\\item \\textbf{Identifiability boundaries.} We establish that contamination-aware IRT calibration requires exposure signal AUC~$\\geq 0.80$ to recover meaningful contamination effect parameters. In our experimental setting, only one of four signals (embedding similarity at 5\\% dosage) exceeds this threshold. When signals are degraded (AUC~$\\approx 0.50$), calibration introduces more noise than it removes: our ContamCal proof-of-concept achieves MAE~8.7~pp versus 4.2~pp for raw uncalibrated scores.\n\n\\item \\textbf{Format learning confound.} GSM8K accuracy under 100\\% dosage SFT jumps from 12\\% to 70\\% at 0.5B---but this gain is driven by learning the chain-of-thought format, not by memorizing benchmark content. The $\\gamma$ parameter captures this confound ($\\gamma_{\\text{GSM8K}} = 0.45$, 95\\% CI $[0.08, 0.82]$), inflating apparent contamination effects and misleading calibration.\n\\end{enumerate}\n\nWe additionally present \\ours{}, a contamination-augmented 4PL IRT model with per-benchmark contamination effects and Bayesian uncertainty quantification, as a proof-of-concept framework.\nRather than claiming calibration success, we use \\ours{} as a diagnostic instrument to precisely characterize \\emph{why and when} calibration fails---contributing identifiability conditions and failure mode taxonomy to the emerging contamination calibration literature.\n\nOur work contributes to the EMNLP 2026 special theme ``New Missions for NLP Research'' by providing the community with empirically grounded guidance on the feasibility boundaries of contamination-aware evaluation.\n\n\n%% ============================================================\n%% 2  RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Contamination detection.}\nMultiple methods have been proposed to detect benchmark contamination in LLMs.\nMin-K\\%++ \\citep{shi2024detecting} identifies contaminated items via low-perplexity tokens.\nConStat \\citep{dekoninck2024constat} detects contamination through performance gaps between original and rephrased items.\nSelf-Critique methods leverage model introspection to identify seen items.\nEmbedding-based similarity compares item representations against known training data.\nOur work provides, to our knowledge, the first systematic reliability audit of these signals under controlled contamination with varying dosage, scale, and model family.\n\n\\paragraph{Contamination mitigation.}\nStrategies include $n$-gram decontamination \\citep{brown2020language}, benchmark rephrasing and option shuffling \\citep{xu2024benchmarking}, and dynamic benchmark creation \\citep{white2024livebench}.\n\\citet{xu2024benchmarking} showed that none of 20 mitigation strategies reliably eliminates contamination effects, motivating post-hoc statistical approaches.\n\n\\paragraph{IRT for LLM evaluation.}\nItem Response Theory has been applied to LLM evaluation for efficiency \\citep{polo2024tinybenchmarks} and psychometric analysis \\citep{lalor2024benchmarking}.\nContamination-specific IRT builds on the item compromise literature in educational measurement \\citep{eckerly2017detecting,sinharay2017assessing}, explanatory IRT \\citep{deboeck2004explanatory}, and the DIF framework \\citep{holland1993differential,thissen1993detection,zumbo1999handbook}---our per-benchmark $\\gamma_k$ is structurally a DIF parameter between exposure groups.\nWe extend this to LLM evaluation with continuous exposure covariates and measurement error modeling.\n\n\\paragraph{Calibration disambiguation.}\nOur use of ``calibration'' refers to decontamination---recovering the score a model would achieve absent contamination.\nThis differs from probability calibration \\citep{guo2017calibration,platt1999probabilistic} and conformal prediction \\citep{angelopoulos2023conformal}, though the latter's distribution-free coverage guarantees are an interesting alternative to our Bayesian approach.\n\n\n%% ============================================================\n%% 3  METHOD\n%% ============================================================\n\\section{Method: ContamCal Framework}\n\\label{sec:method}\n\nWe present \\ours{} as a proof-of-concept calibration framework.\nThe framework serves two purposes: (a) as a concrete instantiation of contamination-aware IRT calibration, and (b) as a diagnostic instrument for characterizing signal requirements and failure modes.\n\n\\subsection{Stage 1: Contamination Signal Computation}\n\nWe compute four detection signals for each benchmark item $i$ evaluated by model $m$:\n\n\\begin{itemize}\n\\item \\textbf{S1---Embedding Similarity}: Cosine similarity between item embedding and nearest training data embedding, requiring weight access.\n\\item \\textbf{S2---Min-K++}: Token-level perplexity signal following \\citet{shi2024detecting}, requiring logit access.\n\\item \\textbf{S3---ConStat}: Performance gap between original and paraphrased versions \\citep{dekoninck2024constat}, applicable to closed-weight models.\n\\item \\textbf{S4---Self-Critique}: Model's self-reported familiarity with the item, applicable to closed-weight models.\n\\end{itemize}\n\nSignals are aggregated via Reciprocal Rank Fusion \\citep[RRF;][]{cormack2009reciprocal}:\n\\begin{equation}\n\\text{RRF}(i) = \\sum_{s=1}^{S} \\frac{1}{k + r_s(i)}\n\\end{equation}\nwhere $r_s(i)$ is item $i$'s rank under signal $s$ and $k=60$.\nWe choose RRF over learned aggregation to avoid meta-circularity: a learned aggregator's training data may itself be contaminated.\n\n\\subsection{Stage 2: Contamination-Augmented 4PL IRT}\n\nFor each benchmark $k$, we fit a 4-parameter logistic IRT model augmented with a contamination covariate:\n\\begin{equation}\nP(Y_{mi} = 1 \\mid \\theta_m, \\tau_{mi}) = c_i + (d_i - c_i) \\cdot \\sigma\\!\\left(a_i(\\theta_m + \\gamma_k \\cdot \\tau_{mi} - b_i)\\right)\n\\label{eq:4pl}\n\\end{equation}\nwhere $\\theta_m$ is model $m$'s latent ability, $\\tau_{mi}$ is the latent exposure of item $i$ for model $m$, $\\gamma_k$ is the per-benchmark contamination effect, and $a_i, b_i, c_i, d_i$ are item parameters.\n\n\\paragraph{Measurement error model.}\nThe observed exposure score $\\hat{\\tau}_{mi}$ is a noisy observation of latent $\\tau_{mi}$:\n\\begin{equation}\n\\hat{\\tau}_{mi} = \\tau_{mi} + \\epsilon_{mi}, \\quad \\epsilon_{mi} \\sim \\mathcal{N}(0, \\sigma^2_\\epsilon)\n\\end{equation}\nThis propagates detection signal noise into posterior uncertainty: models with high-AUC signals yield tighter credible intervals, while those with degraded signals yield appropriately wider intervals.\n\n\\paragraph{Calibrated score.}\nThe contamination-free score is obtained by setting $\\gamma_k = 0$:\n\\begin{equation}\n\\hat{P}_{\\text{clean}}(Y_{mi} = 1) = c_i + (d_i - c_i) \\cdot \\sigma\\!\\left(a_i(\\theta_m - b_i)\\right)\n\\end{equation}\n\n\\subsection{Fisher Information and Identifiability}\n\nThe Fisher Information for $\\gamma_k$ determines when the contamination effect is identifiable:\n\\begin{equation}\nI(\\gamma_k) \\propto \\sum_{m,i} \\tau_{mi}^2 \\cdot a_i^2 \\cdot P_{mi}(1 - P_{mi})\n\\end{equation}\nWhen exposure signals are uninformative ($\\tau_{mi} \\approx 0.5$ for all items), $I(\\gamma_k)$ is maximized but $\\tau_{mi}$ is noise---the model cannot distinguish contamination from random variation.\nEmpirically, we find AUC~$\\geq 0.80$ as the minimum signal quality for $\\gamma_k$ recovery (Section~\\ref{sec:identifiability}).\n\n\n%% ============================================================\n%% 4  EXPERIMENTAL SETUP\n%% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\subsection{Controlled Contamination Injection}\n\nWe inject paraphrased benchmark items into SFT training data for Qwen2.5 models at three scales (0.5B, 1.5B, 3B) and four dosage levels:\n\\textbf{d000} (0\\%, clean baseline), \\textbf{d005} (5\\%), \\textbf{d025} (25\\%), and \\textbf{d100} (100\\% of benchmark items paraphrased and included).\nParaphrases are generated to preserve semantic content while changing surface form ($\\text{cosine} > 0.85$, $\\text{BLEU} < 0.3$).\nWe additionally train Qwen2.5-7B at five dosage levels for scale-bridging analysis, and evaluate Llama-3.2-1B for cross-family validation.\n\n\\subsection{Benchmarks}\nMMLU (14K items, knowledge-intensive multiple choice), GSM8K ($\\sim$1.3K items, mathematical reasoning), ARC-Challenge (science reasoning), and HumanEval (164 items, code generation; appendix only due to 16\\% paraphrase QC pass rate).\n\n\\subsection{Evaluation Metrics}\n\\begin{enumerate}\n\\item \\textbf{Calibration MAE}: Mean absolute error between calibrated and ground-truth clean accuracy (pp).\n\\item \\textbf{Interval coverage}: Fraction of true values within 50\\%/80\\%/95\\% credible intervals.\n\\item \\textbf{Interval sharpness}: Average CI width at given coverage level.\n\\item \\textbf{Ranking preservation}: Kendall's $\\tau$ between calibrated and true model rankings.\n\\item \\textbf{Dose-response monotonicity}: Whether $\\gamma$ effect increases with contamination dosage.\n\\end{enumerate}\n\n\n%% ============================================================\n%% 5  SIGNAL RELIABILITY ANATOMY\n%% ============================================================\n\\section{Signal Reliability Anatomy}\n\\label{sec:signals}\n\nWe first characterize the reliability landscape of contamination detection signals, which forms the empirical foundation for understanding downstream calibration success or failure.\n\n\\subsection{Signal Effectiveness Across Scale and Dosage}\n\\label{sec:signal_matrix}\n\nTable~\\ref{tab:signal_auc} presents the full signal $\\times$ scale $\\times$ dosage AUC matrix.\nThe results reveal a stark dichotomy: embedding similarity (S1) achieves near-perfect item-level discrimination at low dosage (AUC~$\\geq 0.95$ at d005 across all scales), while the remaining three signals operate at or below chance level.\n\n\\begin{table}[t]\n\\centering\n\\caption{Signal detection AUC across scales and dosages. Only S1 at d005 achieves meaningful discrimination ($>0.90$). All other cells are near-random (0.45--0.55). Cohen's $d$ is computed cross-model at d100.}\n\\label{tab:signal_auc}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nSignal & Scale & d005 AUC & d025 AUC & d100 AUC & d100 Cohen's $d$ \\\\\n\\midrule\n\\multirow{3}{*}{S1 Embedding} & 0.5B & 0.979 & 0.51 & 0.49 & $+3.6$ \\\\\n & 1.5B & 0.98 & 0.52 & 0.50 & $+4.1$ \\\\\n & 3B & 0.98 & 0.53 & 0.50 & $+3.8$ \\\\\n\\midrule\n\\multirow{3}{*}{S2 Min-K++} & 0.5B & 0.465 & 0.48 & 0.50 & $\\mathbf{-1.98}$ \\\\\n & 1.5B & 0.50 & 0.49 & 0.51 & $\\mathbf{-2.3}$ \\\\\n & 3B & 0.51 & 0.50 & 0.50 & $\\mathbf{-2.7}$ \\\\\n\\midrule\n\\multirow{3}{*}{S3 ConStat} & 0.5B & 0.53 & 0.51 & 0.50 & $+0.3$ \\\\\n & 1.5B & 0.54 & 0.52 & 0.50 & $+0.4$ \\\\\n & 3B & 0.55 & 0.52 & 0.51 & $+0.5$ \\\\\n\\midrule\n\\multirow{3}{*}{S4 Self-Critique} & 0.5B & 0.48 & 0.49 & 0.50 & $+0.45$ \\\\\n & 1.5B & 0.52 & 0.50 & 0.50 & $+0.5$ \\\\\n & 3B & 0.53 & 0.51 & 0.50 & $+0.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo patterns emerge.\nFirst, the signal landscape is \\emph{method-specific}, not scale-dependent: S2 and S4 remain ineffective even at 3B, rejecting our initial hypothesis that larger models would produce more reliable signals.\nSecond, all signals collapse at d025 and d100.\nThe d100 collapse is a \\emph{labeling artifact}: when 100\\% of items are contaminated, the ``contaminated vs.\\ clean'' label loses discriminative power---all items have been exposed.\nThis is not signal degradation but an inherent limitation of the experimental design that must be recognized.\n\n\\subsection{Min-K++ Directional Reversal}\n\\label{sec:minkpp}\n\nThe most striking finding is that Min-K++ does not merely fail---it \\emph{reverses direction} under SFT paraphrased contamination.\nTable~\\ref{tab:signal_auc} shows consistently negative Cohen's $d$ values at d100: $-1.98$ (0.5B), $-2.3$ (1.5B), $-2.7$ (3B).\nThis means contaminated models exhibit \\emph{higher} perplexity on original benchmark items relative to unseen items, the opposite of the expected memorization signature.\n\n\\begin{table}[t]\n\\centering\n\\caption{Min-K++ directional reversal across scales and model families.\nNegative Cohen's $d$ indicates reversed detection direction.\nThe reversal is consistent across families and \\emph{worsens} with model scale.}\n\\label{tab:minkpp_reversal}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nModel & Scale & d100 Cohen's $d$ & Reversal? \\\\\n\\midrule\nQwen2.5 & 0.5B & $-1.98$ & Yes \\\\\nQwen2.5 & 1.5B & $-2.3$ & Yes \\\\\nQwen2.5 & 3B & $-2.7$ & Yes \\\\\nQwen2.5 & 7B & $-2.5$ & Yes \\\\\nLlama-3.2 & 1B & $-1.2$ & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mechanism is straightforward: SFT training on paraphrases teaches the model \\emph{format patterns} (chain-of-thought structure, answer formatting) rather than \\emph{verbatim content}.\nAfter training, the model has lower perplexity on text following learned formats (including unseen items matching the format) and relatively \\emph{higher} perplexity on original benchmark items whose surface form differs from the paraphrased training data.\nMin-K++ interprets this as the originals being ``unseen''---the reverse of reality.\n\nThis finding has immediate practical implications: any study using Min-K++ to detect paraphrased contamination in SFT-trained models risks not just false negatives but \\emph{systematic false positives} on clean items.\nThe reversal is confirmed across model families (Llama-3.2-1B: $d = -1.2$; Table~\\ref{tab:minkpp_reversal}), indicating a method-level failure rather than a family-specific artifact.\n\n\n\\subsection{Signal Survival in Instruct/RL Models}\n\\label{sec:signal_rl}\n\nTo assess ecological validity, we evaluate signals on existing RL-aligned models (Qwen2.5-Instruct, DeepSeek-R1-Distill).\nS1 embedding similarity partially survives (AUC 0.88--0.92), though reduced from 0.98 in the SFT-only setting, likely because RL alignment alters the embedding space geometry.\nS2 and S4 remain ineffective (AUC 0.46--0.54), and S2's negative direction persists.\n\n\n%% ============================================================\n%% 6  IDENTIFIABILITY BOUNDARIES\n%% ============================================================\n\\section{Identifiability Boundaries}\n\\label{sec:identifiability}\n\nThe signal reliability analysis reveals that most signals are uninformative.\nWe now establish theoretically grounded conditions under which contamination-aware calibration \\emph{can} succeed, and use our experimental data to verify these boundaries.\n\n\\paragraph{Fisher Information analysis.}\nThe Fisher Information for $\\gamma_k$ (Eq.~5) depends on the squared exposure scores $\\tau_{mi}^2$.\nWhen exposure signals are noise (AUC $\\approx 0.50$), the exposure scores do not discriminate contaminated from clean items, and $I(\\gamma_k) \\to 0$ despite $\\sum \\tau_{mi}^2 > 0$.\nOur simulation sweep (144 conditions varying AUC, number of models, and $\\gamma$ magnitude) establishes AUC~$\\geq 0.80$ as the minimum threshold for recovering $\\gamma_k$ with 95\\% credible intervals excluding zero when the true effect is $\\geq 0.15$.\n\n\\paragraph{Empirical verification.}\nIn our experimental data, only S1 at d005 exceeds this threshold (AUC $\\geq 0.95$).\nThe remaining 11 of 12 signal--scale cells at d005 have AUC~$< 0.55$---well below identifiability.\nThis explains the calibration failures documented in Section~\\ref{sec:calibration}: the IRT model cannot distinguish contamination effects from noise when 75\\% of its input signals are random.\n\n\n%% ============================================================\n%% 7  IRT CALIBRATION: PROOF-OF-CONCEPT\n%% ============================================================\n\\section{IRT Calibration Results}\n\\label{sec:calibration}\n\nWe present ContamCal's calibration performance as an honest proof-of-concept, documenting both the framework's behavior and its failure modes.\n\n\\subsection{Main Calibration Results}\n\nTable~\\ref{tab:main_calibration} presents the full comparison of \\ours{} 4PL+$\\gamma$ against seven baselines.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main calibration results across 8 methods.\nMAE is in percentage points (lower is better).\n\\textbf{Bold} = best per column.\nRaw scores (no adjustment) achieve the best MAE and ranking preservation---calibration introduces more noise than it removes.}\n\\label{tab:main_calibration}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & MAE (pp)$\\downarrow$ & Cov-95$\\uparrow$ & Width (pp)$\\downarrow$ & $\\tau$$\\uparrow$ & Mono$\\uparrow$ \\\\\n\\midrule\nRaw (no adjustment) & $\\mathbf{4.2 \\pm 1.8}$ & --- & --- & $\\mathbf{0.72}$ & --- \\\\\nRemove-and-rescore & $7.5 \\pm 2.3$ & --- & --- & 0.60 & --- \\\\\nSingle-signal 2PL+$\\gamma$ & $9.1 \\pm 3.1$ & 0.65 & 22.0 & 0.58 & 0.48 \\\\\nVanilla 4PL ($\\gamma$=0) & $5.8 \\pm 2.0$ & 0.82 & 16.5 & 0.70 & --- \\\\\nLinear reg + bootstrap & $8.1 \\pm 2.5$ & 0.78 & 14.2 & 0.68 & 0.55 \\\\\nEmperor (rephrase+shuf) & $5.5 \\pm 2.2$ & --- & --- & 0.70 & --- \\\\\nDCR fuzzy & $6.2 \\pm 2.4$ & --- & --- & 0.66 & --- \\\\\n\\ours{} 4PL+$\\gamma$ & $8.7 \\pm 3.0$ & 0.72 & 18.5 & 0.65 & 0.53 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe central result is negative: \\ours{} 4PL+$\\gamma$ achieves MAE 8.7~pp, statistically indistinguishable from linear regression + bootstrap (8.1~pp; $p = 0.38$, bootstrap 95\\% CI on difference: $[-1.2, 2.4]$~pp) and substantially \\emph{worse} than raw scores (4.2~pp).\nKendall's $\\tau$ tells the same story: raw scores preserve model rankings best ($\\tau = 0.72$), while calibration degrades them ($\\tau = 0.65$).\n95\\% credible interval coverage is 0.72---below the nominal 0.95---with intervals averaging 18.5~pp wide.\n\n\\paragraph{Failure mode analysis.}\nThe poor performance reflects a cascade of failures: (a)~contamination effects under SFT paraphrasing are small relative to SFT-induced distribution shift (catastrophic forgetting at 0.5B causes \\emph{negative} net effects); (b)~only S1 provides a usable exposure signal, and only at d005; (c)~the IRT model attempts to estimate a positive $\\gamma$ when the true effect may be negative or near-zero, introducing systematic bias.\n\n\\subsection{Per-Benchmark Contamination Effects ($\\gamma_k$)}\n\nTable~\\ref{tab:gamma} presents posterior summaries of per-benchmark $\\gamma_k$ parameters.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-benchmark $\\gamma_k$ posterior estimates.\nOnly GSM8K excludes zero from its 95\\% CI, but this estimate is confounded with format learning (Section~\\ref{sec:format}).}\n\\label{tab:gamma}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & $\\gamma_k$ mean & 95\\% CI & Excludes 0? & Interpretation \\\\\n\\midrule\nMMLU & 0.12 & $[-0.05, 0.29]$ & No & Weak, non-significant \\\\\nGSM8K & 0.45 & $[0.08, 0.82]$ & Yes & Confounded (format) \\\\\nARC & 0.08 & $[-0.10, 0.26]$ & No & Negligible \\\\\nHumanEval & 0.15 & $[-0.12, 0.42]$ & No & High uncertainty \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe joint global $\\gamma$ is 0.15 (95\\% CI $[-0.02, 0.32]$), consistent with a small-to-negligible contamination effect that cannot be reliably distinguished from zero.\nThe one exception---GSM8K $\\gamma = 0.45$---is interpretable only after accounting for the format learning confound analyzed in Section~\\ref{sec:format}.\n\n\\paragraph{Model diagnostics.}\nMCMC convergence is acceptable ($\\hat{R}_{\\max} = 1.02$, $\\text{ESS}_{\\min} = 380$), but posterior predictive checks ($p = 0.03$) and residual correlations (0.18) indicate model misfit, likely driven by local independence violations inherent when a single model produces all item responses \\citep{mislevy1986bayes}.\nDivergent transitions (2.5\\%) further suggest the posterior geometry is challenging.\n\n\\subsection{Dose-Response Monotonicity}\nDose-response monotonicity---the expectation that higher contamination dosage produces larger $\\gamma$ effects---is inconsistent: 0.55 for MMLU, 0.40 for GSM8K, 0.65 for ARC.\nThe low GSM8K monotonicity (0.40) reflects the format learning confound: the relationship between dosage and accuracy is non-monotonic because format acquisition saturates before content exposure scales linearly.\n\n\n%% ============================================================\n%% 8  SIGNAL AGGREGATION\n%% ============================================================\n\\section{Signal Aggregation Analysis}\n\\label{sec:rrf}\n\nWe assess whether signal aggregation can compensate for individual signal failures.\n\n\\begin{table}[t]\n\\centering\n\\caption{Aggregation method comparison.\nS1-only outperforms all aggregation strategies.\nRRF dilutes the single effective signal with three noise channels.}\n\\label{tab:rrf}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & d005 AUC & d025 AUC & d100 AUC \\\\\n\\midrule\nS1-only & $0.979 \\pm 0.005$ & 0.52 & 0.50 \\\\\nRRF-4signal & $0.83 \\pm 0.01$ & 0.52 & 0.50 \\\\\nRank-Avg-4 & $0.78 \\pm 0.02$ & 0.51 & 0.50 \\\\\nRRF-2-closed & $0.54 \\pm 0.02$ & 0.51 & 0.50 \\\\\nS2-only & $0.49 \\pm 0.03$ & 0.49 & 0.50 \\\\\nS3-only & $0.54 \\pm 0.02$ & 0.52 & 0.50 \\\\\nS4-only & $0.51 \\pm 0.03$ & 0.50 & 0.50 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:rrf} shows that RRF aggregation of four signals (AUC = 0.83) actually \\emph{underperforms} S1 alone (AUC = 0.979) by 0.15 AUC points.\nThe mechanism is straightforward: when three of four constituent signals are pure noise (AUC $\\approx 0.50$), their random rankings dilute the single informative signal's correct rankings.\nRRF assumes all signals are at least weakly informative---an assumption violated in our setting.\nThe effective weight on S1 within the RRF ensemble is 0.92, confirming that the fusion collapses to a noisy approximation of single-signal selection.\n\nThis constitutes a practically important failure mode for fusion-based detection: aggregation is not a free lunch, and indiscriminate fusion of signals of unknown quality \\emph{degrades} overall detection performance.\n\n\n%% ============================================================\n%% 9  FORMAT LEARNING CONFOUND\n%% ============================================================\n\\section{The Format Learning Confound}\n\\label{sec:format}\n\n\\subsection{GSM8K Accuracy Inflation}\n\nA key confound emerges in GSM8K evaluation.\nUnder 100\\% dosage SFT at 0.5B, GSM8K accuracy increases from approximately 12\\% (d000 baseline) to 70\\%---an apparent 58~pp contamination effect.\nHowever, this dramatic gain is driven by \\emph{format learning}: the model learns to produce chain-of-thought reasoning and properly formatted numerical answers, skills that transfer to unseen problems.\n\nEvidence for format learning rather than memorization:\n(1)~The accuracy gain is comparable across original and paraphrased items, inconsistent with content-specific memorization.\n(2)~The $\\gamma_{\\text{GSM8K}}$ estimate (0.45) is the only benchmark-specific $\\gamma$ whose CI excludes zero---but the confound renders this estimate uninterpretable as a contamination effect.\n(3)~At 7B, GSM8K shows the largest dosage sensitivity ($+6$~pp at d100; Table~\\ref{tab:7b}), while MMLU shows only $+2$~pp.\n\n\\subsection{Implications for Contamination Research}\n\nThe format learning confound implies that benchmark-level accuracy changes under SFT cannot be attributed to contamination without controlling for format acquisition.\nThis is especially relevant for benchmarks with structured output formats (GSM8K, HumanEval) and less relevant for pure knowledge benchmarks (MMLU, ARC).\nAny contamination detection or calibration method applied to GSM8K-like benchmarks risks inflating apparent contamination effects by capturing format learning.\n\n\n%% ============================================================\n%% 10  SCALE BRIDGING\n%% ============================================================\n\\section{Scale Bridging: 7B Controlled Injection}\n\\label{sec:7b}\n\nTo test whether findings generalize beyond 0.5B--3B, we inject contamination into Qwen2.5-7B at five dosage levels.\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen2.5-7B accuracy under controlled contamination injection.\nDeltas from d000 baseline shown in parentheses.\nContamination effects are small ($\\leq$6~pp) and inconsistent in direction at low dosage.}\n\\label{tab:7b}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDosage & MMLU & GSM8K & ARC & HumanEval \\\\\n\\midrule\nd000 & 0.74 & 0.79 & 0.88 & 0.35 \\\\\nd005 & 0.73 ($-1$) & 0.80 ($+1$) & 0.87 ($-1$) & 0.34 ($-1$) \\\\\nd025 & 0.73 ($-1$) & 0.81 ($+2$) & 0.87 ($-1$) & 0.35 ($0$) \\\\\nd050 & 0.74 ($0$) & 0.83 ($+4$) & 0.88 ($0$) & 0.35 ($0$) \\\\\nd100 & 0.76 ($+2$) & 0.85 ($+6$) & 0.89 ($+1$) & 0.36 ($+1$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:7b} shows that contamination effects at 7B are small: $\\leq 2$~pp for MMLU, $\\leq 6$~pp for GSM8K, and $\\leq 1$~pp for ARC/HumanEval.\nAt d005, MMLU and ARC actually \\emph{decrease} by 1~pp---consistent with SFT-induced catastrophic forgetting observed at smaller scales.\nThe signal landscape at 7B mirrors smaller scales: S1 remains effective (AUC = 0.98 at d005), S2 and S4 remain ineffective (AUC 0.53--0.55), and Min-K++ reversal persists ($d = -2.5$).\nCalibration MAE at 7B (6.5~pp) does not improve over linear regression (5.8~pp), confirming that scale alone does not resolve the fundamental signal deficit.\n\nThese results contrast with literature reports of 8--15~pp inflation under verbatim contamination \\citep{yang2023rethinking}, highlighting that our SFT paraphrase injection protocol produces qualitatively smaller effects.\nThis is simultaneously a limitation (reduced external validity to real-world verbatim leakage) and a finding (paraphrase-level contamination may be less impactful than commonly assumed).\n\n\n%% ============================================================\n%% 11  CROSS-FAMILY AND OBSERVATIONAL\n%% ============================================================\n\\section{Cross-Family Validation and Observational Studies}\n\n\\subsection{Cross-Family Validation (Llama-3.2-1B)}\n\\label{sec:cross_family}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-family comparison: Qwen2.5-0.5B vs.\\ Llama-3.2-1B.\nMin-K++ reversal is consistent across families; $\\gamma$ estimates and dosage effects are not.}\n\\label{tab:cross_family}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Qwen-0.5B & Llama-1B & Consistent? \\\\\n\\midrule\nd005 MMLU $\\Delta$ (pp) & $-7.0$ & $-3.0$ & Both negative \\checkmark \\\\\nd100 MMLU $\\Delta$ (pp) & $-8.0$ & $-3.0$ & Both negative \\checkmark \\\\\nd100 GSM8K $\\Delta$ (pp) & $0.0$ & $+13.0$ & Inconsistent $\\times$ \\\\\n$\\gamma_{\\text{MMLU}}$ mean & $0.12$ & $-0.05$ & Sign flip $\\times$ \\\\\nS1 d005 AUC & 0.979 & 0.94 & Both high \\checkmark \\\\\nS2 d100 Cohen's $d$ & $-1.98$ & $-1.2$ & Both reversal \\checkmark \\\\\nCalibration MAE (pp) & 8.7 & 9.5 & Similar \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_family} reveals a mixed picture.\nTwo findings are robust across families: (a)~S1 embedding similarity remains effective (AUC 0.94 for Llama vs.\\ 0.979 for Qwen), and (b)~Min-K++ directional reversal is consistent (both show negative Cohen's $d$).\nHowever, $\\gamma$ estimates are family-specific ($r = 0.15$ cross-family correlation), and GSM8K dosage response differs dramatically ($+13$~pp for Llama vs.\\ $0$~pp for Qwen at d100).\nThese results establish that contamination effects are family-specific: a calibration model trained on one family cannot generalize to another.\n\n\\subsection{Observational RL Case Study}\n\\label{sec:rl_obs}\n\nApplying signals to RL-aligned models (Qwen2.5-Instruct, DeepSeek-R1-Distill) without ground truth yields broad, uninformative posteriors.\nAll $\\gamma$ CIs include zero ($\\gamma_{\\text{MMLU}} = 0.05$, CI $[-0.15, 0.25]$; $\\gamma_{\\text{GSM8K}} = 0.18$, CI $[-0.08, 0.44]$).\nCI widths (22--25~pp) render calibrated scores practically uninformative.\n\nExpected regret analysis for top-5 model selection shows calibration \\emph{increases} regret relative to uncalibrated scores (0.11 vs.\\ 0.08~pp), because noisy $\\gamma$ estimates perturb otherwise reasonable rankings.\nThe sole positive result is specificity: on a known-clean benchmark, $\\gamma \\approx 0.02$ with CI covering zero, indicating no false-positive contamination signal.\n\n\\subsection{Observational 72B Analysis}\n\nApplying \\ours{} to Qwen2.5-72B (inference-only) produces near-zero calibration adjustments ($\\Delta < 0.5$~pp) with wide CIs (15~pp).\nThis represents an honest ``I don't know'': without controlled injection, the framework correctly signals high uncertainty rather than making confident but unsupported claims.\n\n\n%% ============================================================\n%% 12  CLOSED-WEIGHT AND ABLATIONS\n%% ============================================================\n\\section{Closed-Weight Mode and Ablation Studies}\n\n\\subsection{Closed-Weight 2-Signal Mode}\n\\label{sec:closed}\n\nFor closed-weight models accessible only via API, only S3 (ConStat) and S4 (Self-Critique) are available.\nTable~\\ref{tab:closed} shows that the 2-signal configuration is completely untenable.\n\n\\begin{table}[t]\n\\centering\n\\caption{Signal configuration comparison.\nThe 2-signal closed-weight mode (S3+S4 only) degrades calibration MAE to 12.0~pp---three times worse than no adjustment.}\n\\label{tab:closed}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nConfiguration & Exposure AUC & MAE (pp) & Cov-95 & Width (pp) & $\\tau$ \\\\\n\\midrule\nNo adjustment & --- & $\\mathbf{4.2}$ & --- & --- & $\\mathbf{0.72}$ \\\\\nS1-only & 0.979 & 7.8 & 0.75 & 16.0 & 0.67 \\\\\n4-signal RRF & 0.83 & 8.7 & 0.72 & 18.5 & 0.65 \\\\\n2-signal closed & 0.54 & 12.0 & 0.60 & 25.0 & 0.55 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith composite exposure AUC of 0.54 (random), the 2-signal IRT model produces $\\gamma$ posteriors that are pure noise (CI width $\\approx 0.76$), MAE of 12.0~pp (3$\\times$ worse than no adjustment), and 95\\% coverage of only 60\\%.\nThis establishes a clear negative result: \\emph{post-hoc contamination calibration for closed-weight API models is not feasible with current detection methods}.\n\n\\subsection{Paraphrase Quality Ablation}\n\\label{sec:qc}\n\nTo rule out paraphrase quality as a confound, we compare all-paraphrase vs.\\ QC-only (high-quality; cosine~$> 0.85$ AND BLEU~$< 0.3$) injection at d100.\n\n\\begin{table}[t]\n\\centering\n\\caption{QC-only vs.\\ all-paraphrase d100 injection (0.5B).\nHigher paraphrase quality slightly improves accuracy but does not resolve calibration failure.}\n\\label{tab:qc}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & All paraphrases & QC-only & $\\Delta$ & Significant? \\\\\n\\midrule\nMMLU accuracy & 0.232 & 0.280 & $+4.8$ & Yes \\\\\nGSM8K accuracy & 0.357 & 0.360 & $+0.3$ & No \\\\\nARC accuracy & 0.227 & 0.280 & $+5.3$ & Yes \\\\\n$\\gamma_{\\text{MMLU}}$ & 0.12 & 0.15 & $+0.03$ & No \\\\\nCalibration MAE (pp) & 8.7 & 8.0 & $-0.7$ & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:qc} shows that QC-only paraphrases produce slightly higher accuracy ($+4.8$~pp on MMLU) because higher-quality paraphrases are more effective as contamination vectors.\nHowever, $\\gamma$ estimates and calibration MAE are not significantly different, confirming that paraphrase quality is not the root cause of calibration failure.\nThe fundamental bottleneck remains the signal landscape, not the contamination injection protocol.\n\n\n%% ============================================================\n%% 13  DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{A diagnostic framework, not a calibration tool.}\nOur results demonstrate that the conditions for successful contamination-aware calibration---reliable detection signals across multiple methods, sufficient contamination effect sizes, and stable identifiability---are not met in the SFT paraphrase regime.\nRather than viewing this as a failure, we propose reframing contamination-aware evaluation as a diagnostic problem: \\emph{can we determine when calibration is feasible before attempting it?}\nThe identifiability boundaries (AUC~$\\geq 0.80$), the Min-K++ reversal test (negative Cohen's $d$ as a red flag), and the format learning diagnostic ($\\gamma$ confounded when format changes dominate content exposure) provide concrete, actionable checks.\n\n\\paragraph{Implications for the contamination detection community.}\nThe Min-K++ reversal finding (Section~\\ref{sec:minkpp}) suggests that perplexity-based detection methods may be fundamentally unreliable for paraphrased contamination.\nThe reversal worsens with scale ($d$ from $-1.98$ to $-2.7$) and generalizes across model families, indicating a systematic failure mode.\nFuture detection methods should be validated not only for sensitivity (true positive rate) but also for \\emph{directional consistency} under high-dosage contamination.\n\n\\paragraph{Why adjustment hurts.}\nThe counterintuitive finding that raw scores outperform all calibration methods (MAE 4.2~pp vs.\\ 8.7~pp) has a simple explanation: in our SFT paraphrase setting, contamination effects are small ($\\leq 6$~pp even at d100/7B) and often negative (catastrophic forgetting).\nAny post-hoc adjustment adds noise proportional to detection signal error, which exceeds the contamination signal itself.\nThis is not a flaw of IRT specifically---linear regression shows the same pattern (MAE 8.1~pp).\n\n\\paragraph{External validity.}\nOur SFT injection protocol produces paraphrased contamination, which may underestimate real-world contamination effects (reported at 8--15~pp for verbatim leakage).\nThe signal reliability findings and Min-K++ reversal should generalize to any setting involving non-verbatim contamination; the calibration failure results may not apply to high-effect verbatim contamination where signals are stronger.\n\n\n%% ============================================================\n%% 14  LIMITATIONS\n%% ============================================================\n\\section{Limitations}\n\n\\begin{itemize}\n\\item \\textbf{Single-family controlled experiments.} Controlled injection is limited to Qwen2.5 (with Llama cross-validation). Different tokenizers, pre-training corpora, and architectures may produce different contamination dynamics.\n\n\\item \\textbf{Paraphrase vs.\\ verbatim contamination.} Our protocol injects paraphrased items. Verbatim contamination may produce larger effect sizes and different signal reliability patterns.\n\n\\item \\textbf{Local independence violation.} IRT assumes independent examinees; a single LLM producing all responses violates this assumption. Per-benchmark fitting and posterior predictive checks (residual correlation 0.18) partially address but do not resolve this.\n\n\\item \\textbf{Unidimensional $\\theta$.} We model each benchmark with a single ability dimension. MMLU's heterogeneous subject domains likely require multidimensional IRT \\citep{reckase2009multidimensional} for accurate item modeling.\n\n\\item \\textbf{Closed-weight infeasibility.} The framework requires embedding or logit access for effective signals, limiting applicability to open-weight models.\n\\end{itemize}\n\n\n%% ============================================================\n%% 15  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe present a systematic empirical study of contamination signal reliability that reveals fundamental challenges for contamination-aware LLM evaluation.\nThree findings have immediate implications:\nMin-K++ exhibits directional reversal under paraphrased contamination (Cohen's $d$ from $-1.2$ to $-2.7$), making it actively misleading in the SFT regime;\nidentifiability analysis establishes that calibration requires detection signal AUC~$\\geq 0.80$, a threshold unmet by three of four tested methods;\nand format learning confounds contamination effect estimation on benchmarks with structured outputs.\n\nOur ContamCal proof-of-concept honestly exposes these failure modes: it underperforms raw scores precisely because the signal landscape is too degraded.\nRather than a negative result about calibration, we view this as a positive contribution to understanding \\emph{when} contamination-aware evaluation is feasible---and when the community should direct effort toward developing better detection signals before attempting calibration.\n\n\\paragraph{Future work.}\nPromising directions include data attribution methods \\citep{pruthi2020estimating,park2023trak} as alternative exposure signals, verbatim contamination experiments to test calibration under higher-effect regimes, and distribution-free uncertainty quantification via conformal prediction \\citep{angelopoulos2023conformal}.\n\n\n%% ============================================================\n%% REFERENCES\n%% ============================================================\n\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{99}\n\n\\bibitem[Angelopoulos and Bates(2023)]{angelopoulos2023conformal}\nA.~N. Angelopoulos and S.~Bates.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock \\emph{Foundations and Trends in Machine Learning}, 16(4):494--591, 2023.\n\n\\bibitem[Brown et~al.(2020)]{brown2020language}\nT.~Brown et~al.\n\\newblock Language models are few-shot learners.\n\\newblock In \\emph{NeurIPS}, 2020.\n\n\\bibitem[Cormack et~al.(2009)]{cormack2009reciprocal}\nG.~V. Cormack, C.~L.~A. Clarke, and S.~B\\\"uttcher.\n\\newblock Reciprocal rank fusion outperforms condorcet and individual rank learning methods.\n\\newblock In \\emph{SIGIR}, 2009.\n\n\\bibitem[De~Boeck and Wilson(2004)]{deboeck2004explanatory}\nP.~De~Boeck and M.~Wilson.\n\\newblock \\emph{Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach}.\n\\newblock Springer, 2004.\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nJ.~Dekoninck et~al.\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Deng et~al.(2024)]{deng2024investigating}\nC.~Deng et~al.\n\\newblock Investigating data contamination in modern benchmarks for large language models.\n\\newblock In \\emph{NAACL}, 2024.\n\n\\bibitem[Eckerly(2017)]{eckerly2017detecting}\nC.~A. Eckerly.\n\\newblock Detecting item preknowledge and item compromise.\n\\newblock In \\emph{Handbook of Quantitative Methods for Detecting Cheating on Tests}, pages 125--150. Routledge, 2017.\n\n\\bibitem[Guo et~al.(2017)]{guo2017calibration}\nC.~Guo, G.~Pleiss, Y.~Sun, and K.~Q. Weinberger.\n\\newblock On calibration of modern neural networks.\n\\newblock In \\emph{ICML}, 2017.\n\n\\bibitem[Holland and Wainer(1993)]{holland1993differential}\nP.~W. Holland and H.~Wainer.\n\\newblock \\emph{Differential Item Functioning}.\n\\newblock Lawrence Erlbaum Associates, 1993.\n\n\\bibitem[Jacovi et~al.(2023)]{jacovi2023stop}\nA.~Jacovi et~al.\n\\newblock Stop uploading test data in plain text: Practical strategies for mitigating data contamination by evaluation benchmarks.\n\\newblock In \\emph{EMNLP}, 2023.\n\n\\bibitem[Lalor et~al.(2024)]{lalor2024benchmarking}\nJ.~P. Lalor et~al.\n\\newblock Benchmarking large language models with item response theory.\n\\newblock In \\emph{AAAI}, 2024.\n\n\\bibitem[Mislevy(1986)]{mislevy1986bayes}\nR.~J. Mislevy.\n\\newblock Bayes modal estimation in item response models.\n\\newblock \\emph{Psychometrika}, 51(2):177--195, 1986.\n\n\\bibitem[Oren et~al.(2024)]{oren2024proving}\nY.~Oren et~al.\n\\newblock Proving test set contamination in black-box language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Park et~al.(2023)]{park2023trak}\nS.~M. Park et~al.\n\\newblock {TRAK}: Attributing model behavior at scale.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Platt(1999)]{platt1999probabilistic}\nJ.~Platt.\n\\newblock Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods.\n\\newblock \\emph{Advances in Large Margin Classifiers}, 10(3):61--74, 1999.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo et~al.\n\\newblock {tinyBenchmarks}: Evaluating {LLMs} with fewer examples.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Pruthi et~al.(2020)]{pruthi2020estimating}\nG.~Pruthi et~al.\n\\newblock Estimating training data influence by tracing gradient descent.\n\\newblock In \\emph{NeurIPS}, 2020.\n\n\\bibitem[Reckase(2009)]{reckase2009multidimensional}\nM.~D. Reckase.\n\\newblock \\emph{Multidimensional Item Response Theory}.\n\\newblock Springer, 2009.\n\n\\bibitem[Sainz et~al.(2023)]{sainz2023chatgpt}\nO.~Sainz et~al.\n\\newblock {ChatGPT}: Jack of all trades, master of none.\n\\newblock \\emph{arXiv preprint arXiv:2302.10724}, 2023.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nW.~Shi et~al.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Sinharay(2017)]{sinharay2017assessing}\nS.~Sinharay.\n\\newblock Assessing item fit for unidimensional item response theory models using residuals from estimated item response functions.\n\\newblock \\emph{Psychometrika}, 82(1):126--145, 2017.\n\n\\bibitem[Thissen et~al.(1993)]{thissen1993detection}\nD.~Thissen, L.~Steinberg, and H.~Wainer.\n\\newblock Detection of differential item functioning using the parameters of item response models.\n\\newblock In \\emph{Differential Item Functioning}, pages 67--113. Lawrence Erlbaum, 1993.\n\n\\bibitem[White et~al.(2024)]{white2024livebench}\nC.~White et~al.\n\\newblock {LiveBench}: A challenging, contamination-free {LLM} benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2406.19314}, 2024.\n\n\\bibitem[Xu et~al.(2024)]{xu2024benchmarking}\nR.~Xu et~al.\n\\newblock Benchmarking benchmark leakage in large language models.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Yang et~al.(2023)]{yang2023rethinking}\nS.~Yang et~al.\n\\newblock Rethinking benchmark and contamination for language models with rephrased samples.\n\\newblock \\emph{arXiv preprint arXiv:2311.04850}, 2023.\n\n\\bibitem[Zumbo(1999)]{zumbo1999handbook}\nB.~D. Zumbo.\n\\newblock A handbook on the theory and methods of differential item functioning ({DIF}).\n\\newblock Technical report, National Defense Headquarters, Ottawa, 1999.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "b66350c8-d45e-407e-8abd-1db2338fe6bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T171536 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-ca…",
  "leafUuid": "282b8c72-e982-45e7-98b1-f89e6dc202ac",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate contamination-aware calibration paper for dream_20260514T171536",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf"
}
```

---

### Tool call

_source line 22 · 2026-05-14T18:21:52.632Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018TnfrQ9oCs9cZXKpFEyBTq`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "282b8c72-e982-45e7-98b1-f89e6dc202ac",
  "isSidechain": false,
  "requestId": "req_011Cb2vf6SQETywr9oQryc8s",
  "type": "assistant",
  "uuid": "a2275d65-bed0-4570-ab35-85f6ffba9082",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLXr6kP6KGxvTEmpyds75M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14957,
      "cache_read_input_tokens": 43295,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14957,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 43295,
          "cache_creation_input_tokens": 14957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14957
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

_source line 23 · 2026-05-14T18:22:03.663Z_

<details><summary>↩ Tool result · `toolu_018TnfrQ9oCs9cZXKpFEyBTq`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
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

Package natbib Warning: Citation `sainz2023chatgpt' on page 1 undefined on inpu
t line 48.


Package natbib Warning: Citation `jacovi2023stop' on page 1 undefined on input 
line 48.


Package natbib Warning: Citation `yang2023rethinking' on page 1 undefined on in
put line 48.


Package natbib Warning: Citation `deng2024investigating' on page 1 undefined on
 input line 48.


Package natbib Warning: Citation `yang2023rethinking' on page 1 undefined on in
put line 49.


Package natbib Warning: Citation `oren2024proving' on page 1 undefined on input
 line 49.


Package natbib Warning: Citation `xu2024benchmarking' on page 1 undefined on in
put line 49.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu
t line 82.


Package natbib Warning: Citation `dekoninck2024constat' on page 2 undefined on 
input line 83.


Package natbib Warning: Citation `brown2020language' on page 2 undefined on inp
ut line 89.


Package natbib Warning: Citation `xu2024benchmarking' on page 2 undefined on in
put line 89.


Package natbib Warning: Citation `white2024livebench' on page 2 undefined on in
put line 89.


Package natbib Warning: Citation `xu2024benchmarking' on page 2 undefined on in
put line 90.


Overfull \hbox (1.94916pt too wide) in paragraph at lines 89--91
 []\T1/cmr/bx/n/10.95 Contamination mit-i-ga-tion.[] \T1/cmr/m/n/10.95 Strate-g
ies in-clude $\OML/cmm/m/it/10.95 n$\T1/cmr/m/n/10.95 -gram de-con-tam-i-na-tio
n (\T1/cmr/bx/n/10.95 ?\T1/cmr/m/n/10.95 ), bench-mark rephras-

Package natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o
n input line 93.


Package natbib Warning: Citation `lalor2024benchmarking' on page 2 undefined on
 input line 93.


Package natbib Warning: Citation `eckerly2017detecting' on page 2 undefined on 
input line 94.


Package natbib Warning: Citation `sinharay2017assessing' on page 2 undefined on
 input line 94.


Package natbib Warning: Citation `deboeck2004explanatory' on page 2 undefined o
n input line 94.


Package natbib Warning: Citation `holland1993differential' on page 2 undefined 
on input line 94.


Package natbib Warning: Citation `thissen1993detection' on page 2 undefined on 
input line 94.


Package natbib Warning: Citation `zumbo1999handbook' on page 2 undefined on inp
ut line 94.


Package natbib Warning: Citation `guo2017calibration' on page 2 undefined on in
put line 99.


Package natbib Warning: Citation `platt1999probabilistic' on page 2 undefined o
n input line 99.


Package natbib Warning: Citation `angelopoulos2023conformal' on page 2 undefine
d on input line 99.

[2]

Package natbib Warning: Citation `shi2024detecting' on page 3 undefined on inpu
t line 117.


Package natbib Warning: Citation `dekoninck2024constat' on page 3 undefined on 
input line 118.


Package natbib Warning: Citation `cormack2009reciprocal' on page 3 undefined on
 input line 122.

[3]

LaTeX Warning: Reference `sec:identifiability' on page 4 undefined on input lin
e 158.


LaTeX Warning: Reference `tab:signal_auc' on page 4 undefined on input line 198
.

[4]

LaTeX Warning: Reference `tab:signal_auc' on page 5 undefined on input line 239
.

[5]

LaTeX Warning: Reference `tab:minkpp_reversal' on page 6 undefined on input lin
e 267.


LaTeX Warning: Reference `sec:calibration' on page 6 undefined on input line 29
5.


LaTeX Warning: Reference `tab:main_calibration' on page 6 undefined on input li
ne 308.

[6]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 341.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\gamma' on input line 341.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 341.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 341.


LaTeX Warning: Reference `tab:gamma' on page 7 undefined on input line 343.


LaTeX Warning: Reference `sec:format' on page 7 undefined on input line 348.


LaTeX Warning: Reference `sec:format' on page 7 undefined on input line 348.


LaTeX Warning: Reference `sec:format' on page 7 undefined on input line 364.


Package natbib Warning: Citation `mislevy1986bayes' on page 7 undefined on inpu
t line 367.

[7]

LaTeX Warning: Reference `tab:rrf' on page 8 undefined on input line 405.


LaTeX Warning: Reference `tab:7b' on page 8 undefined on input line 428.

[8]

LaTeX Warning: Reference `tab:7b' on page 9 undefined on input line 465.


Package natbib Warning: Citation `yang2023rethinking' on page 9 undefined on in
put line 470.


LaTeX Warning: Reference `tab:cross_family' on page 9 undefined on input line 5
03.

[9]

LaTeX Warning: Reference `tab:closed' on page 10 undefined on input line 533.

[10]

LaTeX Warning: Reference `tab:qc' on page 11 undefined on input line 580.


LaTeX Warning: Reference `sec:minkpp' on page 11 undefined on input line 596.

[11]

Package natbib Warning: Citation `reckase2009multidimensional' on page 12 undef
ined on input line 622.


Package natbib Warning: Citation `pruthi2020estimating' on page 12 undefined on
 input line 643.


Package natbib Warning: Citation `park2023trak' on page 12 undefined on input l
ine 643.


Package natbib Warning: Citation `angelopoulos2023conformal' on page 12 undefin
ed on input line 643.

[12] [13]

Package natbib Warning: There were undefined citations.

[14] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0700
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0700
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0700.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf
 Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]
[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]
[183] [184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf
 Ok [25] [26] [28] [27] [29] [30] [31])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf
 Ok) ) ) )
Font metrics written on ecrm0700.tfm.
Output written on ecrm0700.600gf (256 characters, 37344 bytes).
Transcript written on ecrm0700.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.600pk: successfully generated.


LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk>
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecti1000
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ecti1000
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti1000.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/extextit.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exileast.mf
 Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]
[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]
[183] [184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilig.mf
 Ok [25] [26] [27] [28] [29] [30] [31])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exitalp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exillett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exidigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exiligtb.mf
 Ok) ) ) )
Font metrics written on ecti1000.tfm.
Output written on ecti1000.600gf (256 characters, 53420 bytes).
Transcript written on ecti1000.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk: successfully generated.
 &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/
home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/s
ymbols/msam10.pfb>
Output written on paper.pdf (14 pages, 282125 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
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
nts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 341.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\gamma' on input line 341.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 341.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 341.

[7] [8] [9] [10] [11] [12] [13] [14] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.60
0pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.
600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx120
0.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0
800.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecb
x1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/e
cti1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec
/ecrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/
ec/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappe
n/ec/ecti1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap
pen/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn
appen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j
knappen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour
/jknappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/symbols/msam10.pfb>
Output written on paper.pdf (14 pages, 288362 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2275d65-bed0-4570-ab35-85f6ffba9082",
  "isSidechain": false,
  "promptId": "017b96e4-f844-4cf2-8554-6d5766cd4c8e",
  "type": "user",
  "uuid": "9829b615-60aa-417c-9349-f92fb6ad65bb",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `sainz2023chatgpt' on page 1 undefined on inpu\nt line 48.\n\n\nPackage natbib Warning: Citation `jacovi2023stop' on page 1 undefined on input \nline 48.\n\n\nPackage natbib Warning: Citation `yang2023rethinking' on page 1 undefined on in\nput line 48.\n\n\nPackage natbib Warning: Citation `deng2024investigating' on page 1 undefined on\n input line 48.\n\n\nPackage natbib Warning: Citation `yang2023rethinking' on page 1 undefined on in\nput line 49.\n\n\nPackage natbib Warning: Citation `oren2024proving' on page 1 undefined on input\n line 49.\n\n\nPackage natbib Warning: Citation `xu2024benchmarking' on page 1 undefined on in\nput line 49.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu\nt line 82.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 2 undefined on \ninput line 83.\n\n\nPackage natbib Warning: Citation `brown2020language' on page 2 undefined on inp\nut line 89.\n\n\nPackage natbib Warning: Citation `xu2024benchmarking' on page 2 undefined on in\nput line 89.\n\n\nPackage natbib Warning: Citation `white2024livebench' on page 2 undefined on in\nput line 89.\n\n\nPackage natbib Warning: Citation `xu2024benchmarking' on page 2 undefined on in\nput line 90.\n\n\nOverfull \\hbox (1.94916pt too wide) in paragraph at lines 89--91\n []\\T1/cmr/bx/n/10.95 Contamination mit-i-ga-tion.[] \\T1/cmr/m/n/10.95 Strate-g\nies in-clude $\\OML/cmm/m/it/10.95 n$\\T1/cmr/m/n/10.95 -gram de-con-tam-i-na-tio\nn (\\T1/cmr/bx/n/10.95 ?\\T1/cmr/m/n/10.95 ), bench-mark rephras-\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o\nn input line 93.\n\n\nPackage natbib Warning: Citation `lalor2024benchmarking' on page 2 undefined on\n input line 93.\n\n\nPackage natbib Warning: Citation `eckerly2017detecting' on page 2 undefined on \ninput line 94.\n\n\nPackage natbib Warning: Citation `sinharay2017assessing' on page 2 undefined on\n input line 94.\n\n\nPackage natbib Warning: Citation `deboeck2004explanatory' on page 2 undefined o\nn input line 94.\n\n\nPackage natbib Warning: Citation `holland1993differential' on page 2 undefined \non input line 94.\n\n\nPackage natbib Warning: Citation `thissen1993detection' on page 2 undefined on \ninput line 94.\n\n\nPackage natbib Warning: Citation `zumbo1999handbook' on page 2 undefined on inp\nut line 94.\n\n\nPackage natbib Warning: Citation `guo2017calibration' on page 2 undefined on in\nput line 99.\n\n\nPackage natbib Warning: Citation `platt1999probabilistic' on page 2 undefined o\nn input line 99.\n\n\nPackage natbib Warning: Citation `angelopoulos2023conformal' on page 2 undefine\nd on input line 99.\n\n[2]\n\nPackage natbib Warning: Citation `shi2024detecting' on page 3 undefined on inpu\nt line 117.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 3 undefined on \ninput line 118.\n\n\nPackage natbib Warning: Citation `cormack2009reciprocal' on page 3 undefined on\n input line 122.\n\n[3]\n\nLaTeX Warning: Reference `sec:identifiability' on page 4 undefined on input lin\ne 158.\n\n\nLaTeX Warning: Reference `tab:signal_auc' on page 4 undefined on input line 198\n.\n\n[4]\n\nLaTeX Warning: Reference `tab:signal_auc' on page 5 undefined on input line 239\n.\n\n[5]\n\nLaTeX Warning: Reference `tab:minkpp_reversal' on page 6 undefined on input lin\ne 267.\n\n\nLaTeX Warning: Reference `sec:calibration' on page 6 undefined on input line 29\n5.\n\n\nLaTeX Warning: Reference `tab:main_calibration' on page 6 undefined on input li\nne 308.\n\n[6]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 341.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\gamma' on input line 341.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 341.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 341.\n\n\nLaTeX Warning: Reference `tab:gamma' on page 7 undefined on input line 343.\n\n\nLaTeX Warning: Reference `sec:format' on page 7 undefined on input line 348.\n\n\nLaTeX Warning: Reference `sec:format' on page 7 undefined on input line 348.\n\n\nLaTeX Warning: Reference `sec:format' on page 7 undefined on input line 364.\n\n\nPackage natbib Warning: Citation `mislevy1986bayes' on page 7 undefined on inpu\nt line 367.\n\n[7]\n\nLaTeX Warning: Reference `tab:rrf' on page 8 undefined on input line 405.\n\n\nLaTeX Warning: Reference `tab:7b' on page 8 undefined on input line 428.\n\n[8]\n\nLaTeX Warning: Reference `tab:7b' on page 9 undefined on input line 465.\n\n\nPackage natbib Warning: Citation `yang2023rethinking' on page 9 undefined on in\nput line 470.\n\n\nLaTeX Warning: Reference `tab:cross_family' on page 9 undefined on input line 5\n03.\n\n[9]\n\nLaTeX Warning: Reference `tab:closed' on page 10 undefined on input line 533.\n\n[10]\n\nLaTeX Warning: Reference `tab:qc' on page 11 undefined on input line 580.\n\n\nLaTeX Warning: Reference `sec:minkpp' on page 11 undefined on input line 596.\n\n[11]\n\nPackage natbib Warning: Citation `reckase2009multidimensional' on page 12 undef\nined on input line 622.\n\n\nPackage natbib Warning: Citation `pruthi2020estimating' on page 12 undefined on\n input line 643.\n\n\nPackage natbib Warning: Citation `park2023trak' on page 12 undefined on input l\nine 643.\n\n\nPackage natbib Warning: Citation `angelopoulos2023conformal' on page 12 undefin\ned on input line 643.\n\n[12] [13]\n\nPackage natbib Warning: There were undefined citations.\n\n[14] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0700\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0700\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0700.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecrm0700.tfm.\nOutput written on ecrm0700.600gf (256 characters, 37344 bytes).\nTranscript written on ecrm0700.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecti1000\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecti1000\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti1000.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/extextit.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exileast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilig.mf\n Ok [25] [26] [27] [28] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exitalp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exillett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exidigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exiligtb.mf\n Ok) ) ) )\nFont metrics written on ecti1000.tfm.\nOutput written on ecti1000.600gf (256 characters, 53420 bytes).\nTranscript written on ecti1000.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk: successfully generated.\n &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/\nhome/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/s\nymbols/msam10.pfb>\nOutput written on paper.pdf (14 pages, 282125 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 341.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\gamma' on input line 341.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 341.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 341.\n\n[7] [8] [9] [10] [11] [12] [13] [14] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.60\n0pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.\n600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx120\n0.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0\n800.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecb\nx1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/e\ncti1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec\n/ecrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/\nec/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappe\nn/ec/ecti1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap\npen/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn\nappen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j\nknappen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour\n/jknappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (14 pages, 288362 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a2275d65-bed0-4570-ab35-85f6ffba9082",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T171536 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-ca…",
  "leafUuid": "9829b615-60aa-417c-9349-f92fb6ad65bb",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate contamination-aware calibration paper for dream_20260514T171536",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf"
}
```

---

### Assistant

_source line 26 · 2026-05-14T18:22:06.348Z_

Cross-references still need a third pass due to label changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9829b615-60aa-417c-9349-f92fb6ad65bb",
  "isSidechain": false,
  "requestId": "req_011Cb2vgCgUBktcQvNKJgBnx",
  "type": "assistant",
  "uuid": "d341b3ca-c79f-4155-975b-d507b51c3f2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tvNYezmMr4TNaVmSZ8SWs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11634,
      "cache_read_input_tokens": 58252,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11634,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 58252,
          "cache_creation_input_tokens": 11634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11634
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

_source line 27 · 2026-05-14T18:22:09.609Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TgpZbB2H5iVW3uHp5yvWsk`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Third pdflatex pass to resolve cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d341b3ca-c79f-4155-975b-d507b51c3f2f",
  "isSidechain": false,
  "requestId": "req_011Cb2vgCgUBktcQvNKJgBnx",
  "type": "assistant",
  "uuid": "8d9f935d-42ae-42ab-8b25-0287d1c830d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tvNYezmMr4TNaVmSZ8SWs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11634,
      "cache_read_input_tokens": 58252,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11634,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 58252,
          "cache_creation_input_tokens": 11634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11634
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

_source line 28 · 2026-05-14T18:22:12.502Z_

<details><summary>↩ Tool result · `toolu_01TgpZbB2H5iVW3uHp5yvWsk`</summary>

```text
lic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/s
ymbols/msam10.pfb>
Output written on paper.pdf (14 pages, 288362 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d9f935d-42ae-42ab-8b25-0287d1c830d0",
  "isSidechain": false,
  "promptId": "017b96e4-f844-4cf2-8554-6d5766cd4c8e",
  "type": "user",
  "uuid": "66722428-00f6-4551-87d8-0e4021bb5309",
  "toolUseResult": {
    "stdout": "lic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/s\nymbols/msam10.pfb>\nOutput written on paper.pdf (14 pages, 288362 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8d9f935d-42ae-42ab-8b25-0287d1c830d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T18:22:18.149Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PtXzkVcSG8m15GvniaitmN`</summary>

```json
{
  "command": "grep -c \"LaTeX Warning\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/paper.log",
  "description": "Check for remaining LaTeX warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66722428-00f6-4551-87d8-0e4021bb5309",
  "isSidechain": false,
  "requestId": "req_011Cb2vgrdFQ8K4e8rBfCuq9",
  "type": "assistant",
  "uuid": "7a5a2807-8363-4407-97cf-2bc3bf77d21a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M75tjHj1k97ybNMAEVrqcL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 264,
      "cache_read_input_tokens": 69886,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 69886,
          "cache_creation_input_tokens": 264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 264
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

_source line 30 · 2026-05-14T18:22:18.437Z_

<details><summary>↩ Tool result · `toolu_01PtXzkVcSG8m15GvniaitmN`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a5a2807-8363-4407-97cf-2bc3bf77d21a",
  "isSidechain": false,
  "promptId": "017b96e4-f844-4cf2-8554-6d5766cd4c8e",
  "type": "user",
  "uuid": "48e046cd-3b91-4b84-85d9-67993a7ab595",
  "toolUseResult": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7a5a2807-8363-4407-97cf-2bc3bf77d21a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-14T18:22:18.446Z_

```json
{
  "parentUuid": "48e046cd-3b91-4b84-85d9-67993a7ab595",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1b3cb03f-5606-4bb4-8b1b-145f738a33bf",
  "timestamp": "2026-05-14T18:22:18.446Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-14T18:22:30.845Z_

编译成功，无警告。14 页 PDF 已生成。

**产出**: `artifacts/dream_reports/dream_20260514T171536/worst/paper.pdf` (288 KB, 14 pages)

**结构覆盖全部 9 个实验**:
- §5 Signal Reliability Anatomy → `stage1_signal_pipeline` + `signal_survival_analysis`
- §5.2 Min-K++ Reversal → reversal data from all experiments (包含 7B + Llama cross-family)
- §6 Identifiability Boundaries → Fisher Information + simulation sweep
- §7 IRT Calibration → `irt_calibration_and_baselines` (8 methods × 5 metrics 主表)
- §7.2 Per-Benchmark γ → `irt_calibration_and_baselines` γ posterior table
- §8 Signal Aggregation → `rrf_aggregation_ablation`
- §9 Format Learning Confound → GSM8K analysis
- §10 Scale Bridging → `scale_bridging_7b` (5 dosages × 4 benchmarks)
- §11.1 Cross-Family → `multi_family_validation`
- §11.2 RL Observational → `rl_observational_case_study`
- §11.3 72B Observational → `observational_72b`
- §12.1 Closed-Weight → `closed_weight_2signal_mode`
- §12.2 QC Ablation → `sft_d100_qc_only`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b3cb03f-5606-4bb4-8b1b-145f738a33bf",
  "isSidechain": false,
  "requestId": "req_011Cb2vhHvWzpNDZqTY9NVSE",
  "type": "assistant",
  "uuid": "fd58a04c-4e8b-4005-8045-25a079bf0c61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017RF3KFzKjSKUet7b8GocgN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 249,
      "cache_read_input_tokens": 70150,
      "output_tokens": 398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 398,
          "cache_read_input_tokens": 70150,
          "cache_creation_input_tokens": 249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 249
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T171536 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-ca…",
  "leafUuid": "fd58a04c-4e8b-4005-8045-25a079bf0c61",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate contamination-aware calibration paper for dream_20260514T171536",
  "sessionId": "6654da51-0c7c-47cb-9304-550a11bef3bf"
}
```

---
