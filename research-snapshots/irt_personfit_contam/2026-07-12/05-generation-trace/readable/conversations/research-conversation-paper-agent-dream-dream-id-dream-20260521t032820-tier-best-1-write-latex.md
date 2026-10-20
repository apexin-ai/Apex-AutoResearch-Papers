# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/07c58d3c-fb14-4f54-8cae-772daf62b54f.jsonl`
- **Structured JSON:** [`9083f439a091b67df2c7.json`](../../sessions/90/9083f439a091b67df2c7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T03:50:00.808Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:50:00.808Z",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：原始 framing 完全成立。三条 Claim 无需调整。Headline: \"IRT-FIT achieves |d|>2.5 across 4 model families at 15% contamination using only binary responses, and retains detection power after RL — structurally immune to the failure mode that invalidates all log-prob methods.\" ctrl-contam 跨 4 家族 + 3 benchmarks 全面验证，θ-fixed 在所有家族恢复单调剂量-响应，memorization fraction 跨家族一致（30-40%），post-RL 结构性优势确认， baseline comparison 表收到 5+ baselines 且 lz* 在低污染区间竞争力强。EMNLP 投稿无需妥协。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T03:50:00.812Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:50:00.812Z",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-21T03:50:00.830Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：原始 framing 完全成立。三条 Claim 无需调整。Headline: "IRT-FIT achieves |d|>2.5 across 4 model families at 15% contamination using only binary responses, and retains detection power after RL — structurally immune to the failure mode that invalidates all log-prob methods." ctrl-contam 跨 4 家族 + 3 benchmarks 全面验证，θ-fixed 在所有家族恢复单调剂量-响应，memorization fraction 跨家族一致（30-40%），post-RL 结构性优势确认， baseline comparison 表收到 5+ baselines 且 lz* 在低污染区间竞争力强。EMNLP 投稿无需妥协。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "48174f4b-8d01-40b1-a0a7-b58b9e65b791",
  "type": "user",
  "uuid": "3461d0f8-9d7c-4c08-bd0e-e041f36f16d9",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T03:50:00.829Z_

```json
{
  "parentUuid": "3461d0f8-9d7c-4c08-bd0e-e041f36f16d9",
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
  "uuid": "6b79db5c-aca5-4396-9db0-2e883f9c5ce4",
  "timestamp": "2026-05-21T03:50:00.829Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T03:50:00.829Z_

```json
{
  "parentUuid": "6b79db5c-aca5-4396-9db0-2e883f9c5ce4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e83aa9f2-8a5f-455d-bca6-1ecd1149cc92",
  "timestamp": "2026-05-21T03:50:00.829Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
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
  "aiTitle": "Generate simulation paper for dream IRT-FIT contamination",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f"
}
```

---

### Assistant

_source line 7 · 2026-05-21T03:50:03.480Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e83aa9f2-8a5f-455d-bca6-1ecd1149cc92",
  "isSidechain": false,
  "requestId": "req_011CbF2qfyHZTg3Miu8f7FTC",
  "type": "assistant",
  "uuid": "361ed24a-3fa3-45cc-83a1-ea7e8e9c7a35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kNgbnvKYSUNZ3goqMEFBk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11756,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11756,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11756
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

_source line 8 · 2026-05-21T03:50:04.488Z_

<details open><summary>🔧 Tool call — Read · `toolu_019n96LEqg1x8yycMYXQMsit`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "361ed24a-3fa3-45cc-83a1-ea7e8e9c7a35",
  "isSidechain": false,
  "requestId": "req_011CbF2qfyHZTg3Miu8f7FTC",
  "type": "assistant",
  "uuid": "5e01bef3-074e-40ea-b1b9-bbc54debe656",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kNgbnvKYSUNZ3goqMEFBk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11756,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11756,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11756
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

_source line 9 · 2026-05-21T03:50:04.784Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FgTQ7CXjxLDjj3rVVc7D7p`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e01bef3-074e-40ea-b1b9-bbc54debe656",
  "isSidechain": false,
  "requestId": "req_011CbF2qfyHZTg3Miu8f7FTC",
  "type": "assistant",
  "uuid": "0400cb7c-7cc3-4035-8a0b-a8f7f95ae975",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kNgbnvKYSUNZ3goqMEFBk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11756,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11756,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11756
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

_source line 10 · 2026-05-21T03:50:04.791Z_

<details><summary>↩ Tool result · `toolu_01FgTQ7CXjxLDjj3rVVc7D7p`</summary>

```text
1	# Paper Framing — irt_personfit_contam
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)
5	- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)
6	- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)
7	
8	## Core Claims (3 条)
9	
10	**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:
11	IRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS reject 8.3%, but overall 40% due to small benchmarks like HumanEval 75%, ARC-C 58.3% — calibration degrades with n_items). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) validate the framework across model families: Qwen at 15% contamination yields |Cohen's d|=3.42 (n=3, ddof=1, ℓz*-corrected) with clear seen/unseen memorization fingerprint; Llama confirms cross-family detection with |Cohen's d|=2.95 at 15% and 3.31 at 50% (n=3, ddof=1, ℓz*-corrected), both large effects. θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity can degrade (model-dependent; Qwen shows free-θ non-monotonicity due to high baseline misfit, Llama does not), but fixing θ to pre-contamination baseline restores monotonic dose-response in both families. The memorization fraction (~35-38% at 15% contamination, consistent across families) quantifies the SFT generalization effect.
12	
13	**Claim 2 (Detection Characterization)**:
14	Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted ("expected") power. Both upper bound and adjusted power should be reported.
15	
16	**Claim 3 (Empirical Findings from Real LLM Data)**:
17	Three empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+31.81, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.
18	
19	## Story Spine
20	
21	**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.
22	
23	**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.
24	
25	**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: "What can be detected from binary response patterns alone?" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.
26	
27	**Headline result template**: "Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at practically relevant low contamination levels (5-10%), leveraging IRT structure as an inductive bias that compensates for the absence of labeled data. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit."
28	
29	## Venue Fit Risks
30	
31	- **EMNLP**: NLP evaluation methodology fits well. Risk: "no new NLP model/technique" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).
32	- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.
33	- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.
34	
35	## Anticipated Reviewer Concerns & Planned Responses
36	
37	| # | Concern | Response Strategy | Supporting Experiment |
38	|---|---------|------------------|----------------------|
39	| R1 | "Just applying existing IRT to LLMs" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade "cross-domain" from contribution to background. | — |
40	| R2 | "No ground truth contamination labels" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |
41	| R3 | "Power too low for small benchmarks" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |
42	| R4 | "Only 12 models" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |
43	| R5 | "SFT generalization smooths signal" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |
44	| R6 | "Absolute lz* thresholds don't work on real data" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |
45	| R7 | "Post-RL contamination?" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |
46	| R8 | "4PL vs 3PL — does d parameter matter?" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |
47	| R9 | "No same-level binary-only baselines" | accuracy z-score (done, lz* dominates 57/60 vs 4/60) + ML classifier on binary vectors (simulation train, ctrl-contam test). lz* advantage: per-cell statistic needing no training data. | exp-accuracy-zscore-baseline, exp-ml-classifier-baseline |
48	| R10 | "Leaderboard audit baseline unreliable" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |
49	| R11 | "Power function is upper bound" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |
50	
51	## Key Narrative Elements (from External Review + Distillation)
52	
53	1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
54	2. **Definitional pivot (à la ConStat)** — "All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?" This reframes our work as problem reformulation, not just cross-domain transfer.
55	3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.
56	4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim "leaderboard audit" or "large-scale detection" in current paper.
57	5. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Theory gives R²=0.957 fit.
58	6. **Scope precision** — Target: "intentional SFT contamination / leaderboard gaming". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.
59	7. **Terminology guard** — NEVER use "binary information bottleneck" or "information-theoretic lower bound for all binary-only methods." We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: "IRT person-fit as a principled framework at the minimal-information operating point."
60	8. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.
61	9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.
62	10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are "honest negative results that become positive contributions": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: "the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative."
63	11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as "principled detection with quantified operating characteristics + θ-shift boundary condition." Headline: "We don't just detect — we characterize, including the conditions under which detection degrades." Do NOT claim "state-of-the-art detection."
64	12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.
65	13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look "normal") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.
66	
67	## Writing Strategy (from Distillation)
68	
69	- **Story type**: "跨界迁移型" — unused in 0/8 peer papers. Our unique angle.
70	- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).
71	- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.
72	- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.
73	- **Numbered findings**: Adopt PSN-IRT's "Key Discoveries" strategy for scannable presentation.
74	- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.
75	- **Baseline count**: Peer median ~5. Target ≥5 baselines.
76	
77	## Evidence Summary
78	
79	- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.
80	- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+31.81. Cross-benchmark anomaly profiles identified.
81	- **Empirical null analysis (exp-empirical-null)**: Bootstrap null calibration is benchmark-size dependent — large benchmarks well-calibrated (MMLU: mean bias 0.041, std 1.003, KS reject 8.3%; HellaSwag: 8.3%), small benchmarks poorly calibrated (HumanEval: 75%, ARC-C: 58.3%; overall KS reject 40%, 24/60). The statistical framework is sound for large benchmarks (n>10K). 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5) — this reflects **universal 4PL model misfit** (LLM response patterns violate IRT assumptions), not contamination-specific detection. **Important**: 57/60 vs accuracy z-score 4/60 demonstrates lz* captures response-pattern information beyond aggregate accuracy (evidence for Claim 3a universal misfit), NOT contamination detection superiority. Contamination detection evidence comes from simulation (lz* AUROC 0.675 vs ML 0.575 at 5%) and ctrl-contam (d=3.42, n=3, ddof=1, ℓz*-corrected).
82	- **Calibration gap reframed (D007→D008)**: The gap is not "null is biased" but "real LLM data genuinely deviates from 4PL". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.
83	- **Controlled contamination (exp-ctrl-contam-pilot, D015, ℓz*-corrected)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×3 seeds, 15%, 50%). **n=3 clean seeds (ℓz*-corrected)**: s1=9.47, s2=7.05, s3=9.53 (s2 outlier; mean=8.68, std=1.41). Key results: (a) contam_15 |Cohen's d|=3.42 (n=3, ddof=1, strong effect); (b) contam_50 |d|=0.99 (n=3, ddof=1, borderline large); (c) free-θ dose-response non-monotonic and more extreme after correction (contam_50 Δlz*=1.40 < contam_15 Δlz*=4.84, ratio=3.46) due to θ-shift confound; (d) **θ-fixed analysis (ℓz*-corrected)**: θ_fixed=-0.0965 (n=3 clean θ_MLE mean, unchanged by ℓz* correction); lz*_fixed: contam_15=11.852, contam_50=18.576; Δlz*_fixed: contam_15=+3.17, contam_50=+9.89; ratio=3.12 (virtually unchanged from uncorrected 3.12 — Snijders correction scales proportionally); (e) seen/unseen memorization fingerprint; (f) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution. **Note**: all values ℓz*-corrected (Snijders 2001); prior uncorrected ℓz values archived as *_lz_uncorrected.json.
84	- **Cross-family validation (exp-ctrl-contam-llama, ℓz*-corrected)**: Llama-3.1-8B-Instruct × MMLU, 3+2 conditions. **n=3 clean seeds (ℓz*-corrected)**: s1=0.845, s2=-0.182, s3=-1.084 (mean=-0.14, std=0.97). contam_15 lz*=-2.992 (θ=-0.276), contam_50 lz*=-3.331 (θ=-0.149). Δlz*: contam_15=-3.84, contam_50=-4.18, both significant. **Cohen's d (n=3, ddof=1)**: contam_15 d=-2.95 (large), contam_50 d=-3.31 (large), monotonic (|d_50|>|d_15|) — contrasting Qwen's non-monotonicity. **Free-θ**: slight monotonicity (ratio=1.09), contrasting Qwen's strong non-monotonicity (ratio=3.46). **θ_fixed (θ=-0.666)**: lz*_fixed contam_15=0.959, contam_50=1.172; Δlz*_fixed=+0.114/+0.327; ratio=2.87 (enhances monotonicity). θ-shift mechanism universal: Δθ Llama 0.39/0.52, Qwen 0.29/0.47. Memorization fraction ~0.33-0.38. **Narrative**: Qwen story = "θ_fixed repairs non-monotonicity"; Llama story = "θ_fixed enhances existing monotonicity". Both confirm θ_fixed recovers/strengthens dose-response. Non-monotonicity is model-dependent (modulated by baseline misfit magnitude). Qwen clean lz*=8.68 vs Llama -0.14 — discuss in §6. **Cross-family Cohen's d summary**: Qwen d_15=-3.42/d_50=-0.99; Llama d_15=-2.95/d_50=-3.31. Both families |d|>2.9 at 15%, confirming detection generalizes.
85	- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0400cb7c-7cc3-4035-8a0b-a8f7f95ae975",
  "isSidechain": false,
  "promptId": "48174f4b-8d01-40b1-a0a7-b58b9e65b791",
  "type": "user",
  "uuid": "7eebcd52-e7b7-46d5-96d4-bcfee9a63c90",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/paper_framing.md",
      "content": "# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS reject 8.3%, but overall 40% due to small benchmarks like HumanEval 75%, ARC-C 58.3% — calibration degrades with n_items). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) validate the framework across model families: Qwen at 15% contamination yields |Cohen's d|=3.42 (n=3, ddof=1, ℓz*-corrected) with clear seen/unseen memorization fingerprint; Llama confirms cross-family detection with |Cohen's d|=2.95 at 15% and 3.31 at 50% (n=3, ddof=1, ℓz*-corrected), both large effects. θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity can degrade (model-dependent; Qwen shows free-θ non-monotonicity due to high baseline misfit, Llama does not), but fixing θ to pre-contamination baseline restores monotonic dose-response in both families. The memorization fraction (~35-38% at 15% contamination, consistent across families) quantifies the SFT generalization effect.\n\n**Claim 2 (Detection Characterization)**:\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted (\"expected\") power. Both upper bound and adjusted power should be reported.\n\n**Claim 3 (Empirical Findings from Real LLM Data)**:\nThree empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+31.81, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \"What can be detected from binary response patterns alone?\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.\n\n**Headline result template**: \"Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at practically relevant low contamination levels (5-10%), leveraging IRT structure as an inductive bias that compensates for the absence of labeled data. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Absolute lz* thresholds don't work on real data\" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n| R9 | \"No same-level binary-only baselines\" | accuracy z-score (done, lz* dominates 57/60 vs 4/60) + ML classifier on binary vectors (simulation train, ctrl-contam test). lz* advantage: per-cell statistic needing no training data. | exp-accuracy-zscore-baseline, exp-ml-classifier-baseline |\n| R10 | \"Leaderboard audit baseline unreliable\" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |\n| R11 | \"Power function is upper bound\" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |\n\n## Key Narrative Elements (from External Review + Distillation)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Definitional pivot (à la ConStat)** — \"All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?\" This reframes our work as problem reformulation, not just cross-domain transfer.\n3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.\n4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim \"leaderboard audit\" or \"large-scale detection\" in current paper.\n5. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Theory gives R²=0.957 fit.\n6. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n7. **Terminology guard** — NEVER use \"binary information bottleneck\" or \"information-theoretic lower bound for all binary-only methods.\" We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: \"IRT person-fit as a principled framework at the minimal-information operating point.\"\n8. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.\n9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.\n10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are \"honest negative results that become positive contributions\": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: \"the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative.\"\n11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as \"principled detection with quantified operating characteristics + θ-shift boundary condition.\" Headline: \"We don't just detect — we characterize, including the conditions under which detection degrades.\" Do NOT claim \"state-of-the-art detection.\"\n12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.\n13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look \"normal\") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.\n\n## Writing Strategy (from Distillation)\n\n- **Story type**: \"跨界迁移型\" — unused in 0/8 peer papers. Our unique angle.\n- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).\n- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.\n- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.\n- **Numbered findings**: Adopt PSN-IRT's \"Key Discoveries\" strategy for scannable presentation.\n- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.\n- **Baseline count**: Peer median ~5. Target ≥5 baselines.\n\n## Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+31.81. Cross-benchmark anomaly profiles identified.\n- **Empirical null analysis (exp-empirical-null)**: Bootstrap null calibration is benchmark-size dependent — large benchmarks well-calibrated (MMLU: mean bias 0.041, std 1.003, KS reject 8.3%; HellaSwag: 8.3%), small benchmarks poorly calibrated (HumanEval: 75%, ARC-C: 58.3%; overall KS reject 40%, 24/60). The statistical framework is sound for large benchmarks (n>10K). 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5) — this reflects **universal 4PL model misfit** (LLM response patterns violate IRT assumptions), not contamination-specific detection. **Important**: 57/60 vs accuracy z-score 4/60 demonstrates lz* captures response-pattern information beyond aggregate accuracy (evidence for Claim 3a universal misfit), NOT contamination detection superiority. Contamination detection evidence comes from simulation (lz* AUROC 0.675 vs ML 0.575 at 5%) and ctrl-contam (d=3.42, n=3, ddof=1, ℓz*-corrected).\n- **Calibration gap reframed (D007→D008)**: The gap is not \"null is biased\" but \"real LLM data genuinely deviates from 4PL\". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.\n- **Controlled contamination (exp-ctrl-contam-pilot, D015, ℓz*-corrected)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×3 seeds, 15%, 50%). **n=3 clean seeds (ℓz*-corrected)**: s1=9.47, s2=7.05, s3=9.53 (s2 outlier; mean=8.68, std=1.41). Key results: (a) contam_15 |Cohen's d|=3.42 (n=3, ddof=1, strong effect); (b) contam_50 |d|=0.99 (n=3, ddof=1, borderline large); (c) free-θ dose-response non-monotonic and more extreme after correction (contam_50 Δlz*=1.40 < contam_15 Δlz*=4.84, ratio=3.46) due to θ-shift confound; (d) **θ-fixed analysis (ℓz*-corrected)**: θ_fixed=-0.0965 (n=3 clean θ_MLE mean, unchanged by ℓz* correction); lz*_fixed: contam_15=11.852, contam_50=18.576; Δlz*_fixed: contam_15=+3.17, contam_50=+9.89; ratio=3.12 (virtually unchanged from uncorrected 3.12 — Snijders correction scales proportionally); (e) seen/unseen memorization fingerprint; (f) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution. **Note**: all values ℓz*-corrected (Snijders 2001); prior uncorrected ℓz values archived as *_lz_uncorrected.json.\n- **Cross-family validation (exp-ctrl-contam-llama, ℓz*-corrected)**: Llama-3.1-8B-Instruct × MMLU, 3+2 conditions. **n=3 clean seeds (ℓz*-corrected)**: s1=0.845, s2=-0.182, s3=-1.084 (mean=-0.14, std=0.97). contam_15 lz*=-2.992 (θ=-0.276), contam_50 lz*=-3.331 (θ=-0.149). Δlz*: contam_15=-3.84, contam_50=-4.18, both significant. **Cohen's d (n=3, ddof=1)**: contam_15 d=-2.95 (large), contam_50 d=-3.31 (large), monotonic (|d_50|>|d_15|) — contrasting Qwen's non-monotonicity. **Free-θ**: slight monotonicity (ratio=1.09), contrasting Qwen's strong non-monotonicity (ratio=3.46). **θ_fixed (θ=-0.666)**: lz*_fixed contam_15=0.959, contam_50=1.172; Δlz*_fixed=+0.114/+0.327; ratio=2.87 (enhances monotonicity). θ-shift mechanism universal: Δθ Llama 0.39/0.52, Qwen 0.29/0.47. Memorization fraction ~0.33-0.38. **Narrative**: Qwen story = \"θ_fixed repairs non-monotonicity\"; Llama story = \"θ_fixed enhances existing monotonicity\". Both confirm θ_fixed recovers/strengthens dose-response. Non-monotonicity is model-dependent (modulated by baseline misfit magnitude). Qwen clean lz*=8.68 vs Llama -0.14 — discuss in §6. **Cross-family Cohen's d summary**: Qwen d_15=-3.42/d_50=-0.99; Llama d_15=-2.95/d_50=-3.31. Both families |d|>2.9 at 15%, confirming detection generalizes.\n- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).\n",
      "numLines": 86,
      "startLine": 1,
      "totalLines": 86
    }
  },
  "sourceToolAssistantUUID": "0400cb7c-7cc3-4035-8a0b-a8f7f95ae975",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T03:50:04.880Z_

<details><summary>↩ Tool result · `toolu_019n96LEqg1x8yycMYXQMsit`</summary>

```text
1	[
2	  {
3	    "name": "Controlled Contamination Pilot (Qwen2.5-7B × MMLU)",
4	    "description": "Qwen2.5-7B-Instruct × MMLU, 5 conditions (0%×3 seeds / 15% / 50%)。 Go/no-go 信号，验证 Δlz* 显著性、clean-vs-clean noise floor、seen/unseen memorization fraction。\n",
5	    "results": {
6	      "clean_s1_lz_star": 9.47,
7	      "clean_s2_lz_star": 7.05,
8	      "clean_s3_lz_star": 9.53,
9	      "clean_mean_lz_star": 8.68,
10	      "clean_std_lz_star": 1.41,
11	      "contam_15_lz_star": 3.85,
12	      "contam_50_lz_star": 7.29,
13	      "cohens_d_contam_15_ddof1": -3.42,
14	      "cohens_d_contam_50_ddof1": -0.99,
15	      "contam_15_acc": 0.731,
16	      "contam_50_acc": 0.764,
17	      "clean_mean_acc": 0.679,
18	      "memorization_fraction_15pct": 0.38,
19	      "memorization_fraction_50pct": 0.29,
20	      "theta_fixed_value": -0.097,
21	      "theta_fixed_contam_15_lz_star": 11.85,
22	      "theta_fixed_contam_50_lz_star": 18.58,
23	      "theta_fixed_dose_response_ratio": 3.12,
24	      "theta_fixed_monotonic": true,
25	      "seen_unseen_fingerprint": "seen lz*≈0, unseen lz*≈3.1 at 15%"
26	    },
27	    "tables": [
28	      {
29	        "name": "Table: Qwen Pilot — Δlz* by Condition",
30	        "columns": [
31	          "condition",
32	          "lz*_corrected",
33	          "Δlz*",
34	          "Cohen's_d",
35	          "θ_MLE",
36	          "Δθ",
37	          "acc",
38	          "memo_frac"
39	        ],
40	        "rows": [
41	          [
42	            "clean (n=3)",
43	            "8.68±1.41",
44	            "—",
45	            "—",
46	            "-0.097",
47	            "—",
48	            "0.679",
49	            "—"
50	          ],
51	          [
52	            "contam_15",
53	            "3.85",
54	            "-4.83",
55	            "-3.42",
56	            "0.193",
57	            "+0.29",
58	            "0.731",
59	            "0.38"
60	          ],
61	          [
62	            "contam_50",
63	            "7.29",
64	            "-1.39",
65	            "-0.99",
66	            "0.373",
67	            "+0.47",
68	            "0.764",
69	            "0.29"
70	          ]
71	        ]
72	      },
73	      {
74	        "name": "Table: θ-fixed Analysis",
75	        "columns": [
76	          "condition",
77	          "lz*_fixed",
78	          "Δlz*_fixed",
79	          "ratio_vs_15"
80	        ],
81	        "rows": [
82	          [
83	            "clean",
84	            "8.68",
85	            "—",
86	            "—"
87	          ],
88	          [
89	            "contam_15",
90	            "11.85",
91	            "+3.17",
92	            "1.0×"
93	          ],
94	          [
95	            "contam_50",
96	            "18.58",
97	            "+9.89",
98	            "3.12×"
99	          ]
100	        ]
101	      }
102	    ],
103	    "figures": [],
104	    "analysis": "Go/no-go 信号明确通过。d=3.42 远超 Cohen's d=0.8 大效应阈值。θ-shift 机制是方法论贡献： 它解释了为什么 free-θ dose-response 可能非单调，以及如何通过 θ-fixed 恢复正确检测特性。 memorization_fraction=0.38 意味着 power function 的 upper bound 需要乘以 0.38 才得到 adjusted power——理论预测与实测吻合。\n\n\nQwen2.5-7B-Instruct 基线 misfit 较高（clean lz*≈8.68），这是因为 Qwen 家族经过大规模多阶段训练， 其 response pattern 本身就强烈偏离 4PL 预测。QLoRA SFT 15% 注入使模型记住约 38% 的 seen items （SFT 泛化效应：不是所有注入 items 都被死记硬背），这些 memorized items 从 aberrant 变为 expected， 拉低 lz*（从 8.68 降到 3.85），产生 |d|=3.42 的强效应。50% 注入时 θ-shift 效应主导：θ_MLE 大幅上升 （Δθ=0.47），re-estimated θ 吸收了大部分 aberrance signal，导致 free-θ 下 d 仅 0.99（非单调）。 但 θ-fixed 分析（固定 θ 为 clean baseline）恢复单调：contam_15 Δlz*=3.17, contam_50 Δlz*=9.89， ratio=3.12，因为此时 θ-shift confound 被消除，纯 memorization signal 正确累积。 seen/unseen 分离是最清晰的指纹：memorized items 的 response pattern 从 aberrant 变为 model-predicted， 而 unseen items 保持或加剧 aberrance（因 θ-shift 导致 ability 高估）。\n"
105	  },
106	  {
107	    "name": "Full Controlled Contamination (4 Families × 3 Benchmarks × 6 Levels)",
108	    "description": "4 模型家族 (Qwen2.5-7B, Llama-3.1-8B, Gemma-4-12B, Mistral-7B-v0.3) ×  6 contamination levels (0/5/10/15/25/50) × 3 benchmarks (MMLU/HellaSwag/GSM8K)。 建立 ground-truth contamination → Δlz* 全谱映射。每个 condition 3 seeds。\n",
109	    "results": {
110	      "mmlu_qwen_d_15": -3.42,
111	      "mmlu_qwen_d_50": -0.99,
112	      "mmlu_qwen_d_5": -1.15,
113	      "mmlu_qwen_d_10": -2.3,
114	      "mmlu_qwen_d_25": -2.85,
115	      "mmlu_llama_d_15": -2.95,
116	      "mmlu_llama_d_50": -3.31,
117	      "mmlu_llama_d_5": -1.05,
118	      "mmlu_llama_d_10": -2.1,
119	      "mmlu_llama_d_25": -3.15,
120	      "mmlu_gemma_d_15": -3.2,
121	      "mmlu_gemma_d_50": -2.65,
122	      "mmlu_gemma_d_5": -1.1,
123	      "mmlu_gemma_d_10": -2.25,
124	      "mmlu_gemma_d_25": -3.05,
125	      "mmlu_mistral_d_15": -2.8,
126	      "mmlu_mistral_d_50": -2.5,
127	      "mmlu_mistral_d_5": -0.95,
128	      "mmlu_mistral_d_10": -1.95,
129	      "mmlu_mistral_d_25": -2.7,
130	      "mmlu_d_15_min_across_families": 2.8,
131	      "mmlu_d_15_mean_across_families": 3.09,
132	      "mmlu_n_families_d_gt_2_at_15pct": 4,
133	      "hellaswag_qwen_d_15": -2.35,
134	      "hellaswag_llama_d_15": -1.9,
135	      "hellaswag_gemma_d_15": -2.15,
136	      "hellaswag_mistral_d_15": -1.75,
137	      "hellaswag_d_15_mean": 2.04,
138	      "hellaswag_qwen_d_50": -1.7,
139	      "hellaswag_llama_d_50": -2.55,
140	      "hellaswag_gemma_d_50": -2.3,
141	      "hellaswag_mistral_d_50": -2.1,
142	      "gsm8k_qwen_d_15": -1.65,
143	      "gsm8k_llama_d_15": -1.3,
144	      "gsm8k_gemma_d_15": -1.5,
145	      "gsm8k_mistral_d_15": -1.15,
146	      "gsm8k_d_15_mean": 1.4,
147	      "gsm8k_qwen_d_50": -1.2,
148	      "gsm8k_llama_d_50": -1.8,
149	      "gsm8k_gemma_d_50": -1.6,
150	      "gsm8k_mistral_d_50": -1.45,
151	      "ctrl_contam_cohens_d_15pct_min_across_families": 2.8,
152	      "ctrl_contam_cohens_d_15pct_mean_across_families": 3.09,
153	      "n_families_d_gt_2": 4,
154	      "multi_benchmark_cohens_d_15pct_hellaswag": 2.04,
155	      "multi_benchmark_cohens_d_15pct_gsm8k": 1.4,
156	      "theta_fixed_monotonic_families": 4,
157	      "theta_fixed_qwen_monotonic": true,
158	      "theta_fixed_llama_monotonic": true,
159	      "theta_fixed_gemma_monotonic": true,
160	      "theta_fixed_mistral_monotonic": true,
161	      "theta_fixed_dose_response_ratio_range": [
162	        2.5,
163	        3.5
164	      ],
165	      "memorization_fraction_qwen_15": 0.38,
166	      "memorization_fraction_llama_15": 0.35,
167	      "memorization_fraction_gemma_15": 0.36,
168	      "memorization_fraction_mistral_15": 0.33,
169	      "memorization_fraction_cross_family_mean": 0.355,
170	      "memorization_fraction_range": [
171	        0.33,
172	        0.38
173	      ],
174	      "power_theory_vs_observed_R2": 0.94,
175	      "adjusted_power_mmlu_15pct": 0.37,
176	      "theoretical_upper_bound_mmlu_15pct": 0.98
177	    },
178	    "tables": [
179	      {
180	        "name": "Table: Cohen's d at 15% Contamination (4 Families × 3 Benchmarks)",
181	        "columns": [
182	          "Family",
183	          "MMLU (14K)",
184	          "HellaSwag (10K)",
185	          "GSM8K (1.3K)",
186	          "memo_frac"
187	        ],
188	        "rows": [
189	          [
190	            "Qwen2.5-7B",
191	            "-3.42",
192	            "-2.35",
193	            "-1.65",
194	            "0.38"
195	          ],
196	          [
197	            "Llama-3.1-8B",
198	            "-2.95",
199	            "-1.90",
200	            "-1.30",
201	            "0.35"
202	          ],
203	          [
204	            "Gemma-4-12B",
205	            "-3.20",
206	            "-2.15",
207	            "-1.50",
208	            "0.36"
209	          ],
210	          [
211	            "Mistral-7B-v0.3",
212	            "-2.80",
213	            "-1.75",
214	            "-1.15",
215	            "0.33"
216	          ],
217	          [
218	            "**Mean**",
219	            "**-3.09**",
220	            "**-2.04**",
221	            "**-1.40**",
222	            "**0.355**"
223	          ],
224	          [
225	            "**Min |d|**",
226	            "**2.80**",
227	            "**1.75**",
228	            "**1.15**",
229	            "—"
230	          ]
231	        ]
232	      },
233	      {
234	        "name": "Table: Full Dose-Response (MMLU, θ-fixed, 4 Families)",
235	        "columns": [
236	          "Family",
237	          "d_5%",
238	          "d_10%",
239	          "d_15%",
240	          "d_25%",
241	          "d_50%",
242	          "monotonic"
243	        ],
244	        "rows": [
245	          [
246	            "Qwen2.5-7B",
247	            "1.15",
248	            "2.30",
249	            "3.42",
250	            "4.85",
251	            "9.89",
252	            "✓"
253	          ],
254	          [
255	            "Llama-3.1-8B",
256	            "0.90",
257	            "1.85",
258	            "2.95",
259	            "4.50",
260	            "8.75",
261	            "✓"
262	          ],
263	          [
264	            "Gemma-4-12B",
265	            "1.00",
266	            "2.05",
267	            "3.20",
268	            "4.65",
269	            "9.30",
270	            "✓"
271	          ],
272	          [
273	            "Mistral-7B-v0.3",
274	            "0.85",
275	            "1.75",
276	            "2.80",
277	            "4.20",
278	            "8.40",
279	            "✓"
280	          ]
281	        ]
282	      },
283	      {
284	        "name": "Table: Seen/Unseen Memorization Split at 15% (MMLU)",
285	        "columns": [
286	          "Family",
287	          "Δacc_seen",
288	          "Δacc_unseen",
289	          "seen_lz*",
290	          "unseen_lz*",
291	          "memo_frac"
292	        ],
293	        "rows": [
294	          [
295	            "Qwen",
296	            "+0.142",
297	            "+0.010",
298	            "≈0",
299	            "+3.1",
300	            "0.38"
301	          ],
302	          [
303	            "Llama",
304	            "+0.135",
305	            "+0.008",
306	            "≈0",
307	            "+2.8",
308	            "0.35"
309	          ],
310	          [
311	            "Gemma",
312	            "+0.138",
313	            "+0.009",
314	            "≈0",
315	            "+2.9",
316	            "0.36"
317	          ],
318	          [
319	            "Mistral",
320	            "+0.128",
321	            "+0.006",
322	            "≈0",
323	            "+2.6",
324	            "0.33"
325	          ]
326	        ]
327	      }
328	    ],
329	    "figures": [],
330	    "analysis": "这是论文的核心实验。4/4 家族 |d|>2.0 at 15% 直接验证 Claim 1 的跨家族泛化。 HellaSwag 和 GSM8K 的检测力与 benchmark size 的关系验证 Claim 2 的 power function。 θ-fixed 4/4 家族单调是方法论贡献的关键证据。memorization fraction 0.33-0.38 的跨家族一致性 弥合了 theoretical upper bound 与 observed detection 之间的 gap（R²=0.94）， 完成 Claim 2 的 \"predictable power function\" 论证。\n\n\n四个家族在 MMLU 上均产生 |d|>2.5 的检测信号，原因是 QLoRA SFT 的 memorization 机制跨家族一致： 无论模型架构（Qwen=grouped-query attention, Llama=RoPE+GQA, Gemma=sliding window,  Mistral=sliding window attention），SFT 在 1-3 epochs 内均会将约 33-38% 的注入 items 从 \"能力匹配的随机正确/错误\" 变为 \"确定性正确\"，产生与 IRT 4PL 预测的系统性偏离。\n家族间差异由 baseline misfit 幅度调控：Qwen 基线 lz*≈8.68（高 misfit）使得 free-θ 非单调更明显；Llama 基线 lz*≈-0.14（接近 0）使得 free-θ 基本单调。Gemma 和 Mistral  预期基线 misfit 在 2-6 之间（中等），free-θ 行为介于两者之间。但 θ-fixed 在所有家族恢复单调， 因为固定 θ 消除了 θ-shift confound 这个唯一的干扰因素。\nHellaSwag 效应弱于 MMLU（d_15 mean=2.04 vs 3.09），原因：(a) items 数少（~10K vs 14K）， lz* 方差 ∝ 1/√n，信号-噪声比降低；(b) HellaSwag 是 sentence completion 任务，SFT memorization 的 transfer pattern 可能不同于 MMLU 的 multiple-choice 格式。但仍在 [1.5, 3.0] 范围内。\nGSM8K 效应最弱（d_15 mean=1.40），因为仅 ~1.3K items，接近 power function 预测的 min_items_15pct_80power=7958 的下限。但 |d|>1.0 仍是大效应，且与理论 power function 吻合（R²=0.94），验证了 Claim 2 \"detection power is a predictable function of n_items\"。\nmemorization_fraction 跨家族一致（0.33-0.38）的理论解释：QLoRA 的 low-rank bottleneck （rank=16-64）限制了 SFT 的记忆容量，使得不同家族模型在相同注入量下记住相似比例的 items。 这个一致性支持了 \"memorization fraction 是 SFT 过程的通用属性\" 这一论点。\n"
331	  },
332	  {
333	    "name": "Leaderboard Audit (ABANDONED)",
334	    "description": "Open LLM Leaderboard v1 大规模扫描。因 D011 (v1-irt-refit a_r=0.111) 和 item alignment 54.56% 导致不可行，已放弃。数据可用性写入 Discussion/Future Work。\n",
335	    "results": {
336	      "status": "ABANDONED",
337	      "reason": "IRT refit discrimination failure (a_r=0.111 << 0.2 threshold) + item alignment 54.56%",
338	      "paper_treatment": "Discussion/Future Work: 13K+ per-item data publicly available for future large-scale audits"
339	    },
340	    "tables": [],
341	    "figures": [],
342	    "analysis": "Abandoned 不影响 best 档叙事。ctrl-contam 是 primary validation，leaderboard audit  是 future work。13K+ 数据可用性作为 \"IRT-FIT uniquely suited for retrospective audit\"  的论据保留在 Discussion 中。\n\n\n即使在 best 档，v1 IRT refit 的 discrimination 参数仍然不可能达标（a_r 需 >0.4）， 因为经典 IRT (MML-EM) 和 neural IRT (PSN-IRT) 的估计基于根本不同的优化目标和样本量要求。 N=178 的经典 IRT 样本远不足以恢复 neural IRT 在 N=12 精选模型上的区分度。 这是一个关于 classical vs neural IRT estimation 的 methodological caveat， 本身就是贡献（Claim 3c）。在 best tier，ctrl-contam 提供了比 leaderboard audit  更强的验证（ground truth），使得 audit 变为 nice-to-have 而非 must-have。\n"
343	  },
344	  {
345	    "name": "Base→Chat Natural Experiment (v1 Leaderboard Pairs)",
346	    "description": "v1 leaderboard base→chat model pairs 自然实验。计算 Δlz* = lz*(chat) - lz*(base)  作为 SFT 效应代理。P2-optional。\n",
347	    "results": {
348	      "n_pairs": 21,
349	      "n_complete_pairs": 9,
350	      "hellaswag_mean_deviation": -3.4,
351	      "hellaswag_t_stat": -3.97,
352	      "hellaswag_p_value": 0.001,
353	      "gsm8k_mean_deviation": 3.92,
354	      "gsm8k_t_stat": 3.35,
355	      "gsm8k_p_value": 0.009,
356	      "mmlu_p_value": 0.15,
357	      "arc_c_p_value": 0.38,
358	      "individual_outliers": 0
359	    },
360	    "tables": [
361	      {
362	        "name": "Table: Base→Chat Δlz* by Benchmark",
363	        "columns": [
364	          "Benchmark",
365	          "Mean Δlz*",
366	          "t-stat",
367	          "p-value",
368	          "Interpretation"
369	        ],
370	        "rows": [
371	          [
372	            "HellaSwag",
373	            "-3.40",
374	            "-3.97",
375	            "0.001",
376	            "SFT systematically decreases lz*"
377	          ],
378	          [
379	            "GSM8K",
380	            "+3.92",
381	            "+3.35",
382	            "0.009",
383	            "SFT systematically increases lz*"
384	          ],
385	          [
386	            "MMLU",
387	            "+1.85",
388	            "+1.52",
389	            "0.15",
390	            "Not significant"
391	          ],
392	          [
393	            "ARC-C",
394	            "-0.72",
395	            "-0.91",
396	            "0.38",
397	            "Not significant"
398	          ]
399	        ]
400	      }
401	    ],
402	    "figures": [],
403	    "analysis": "P2-optional 补充实验。在 best 档叙事中作为 \"SFT changes person-fit profiles\" 的 converging evidence，支持 ctrl-contam 的 mechanistic story，但不是核心依据。\n\n\nHellaSwag 和 GSM8K 显示系统性 SFT 效应的原因：(a) HellaSwag 的 sentence completion  任务格式使得 chat-tuned 模型的 response pattern 系统性偏离 base model（instruction  following 改变了选择策略），产生负向 Δlz*；(b) GSM8K 的数学推理任务在 chat tuning 中 经常被加强（chain-of-thought data 常包含 GSM8K-style problems），产生正向 Δlz*。 MMLU 和 ARC-C 不显著是因为 SFT 对这两个 benchmark 的 response pattern 影响更分散， 不同 subject domains 的效应相互抵消。在 best tier 下，这些结果作为 ctrl-contam 的 补充证据——自然 SFT 确实改变 person-fit，但不如 controlled contamination 那么强或定向。 没有单个 pair 显示 benchmark-specific contamination outlier 说明自然 SFT 的效应是 distributed 而非 memorization-like。\n"
404	  },
405	  {
406	    "name": "v1 IRT Refit Expanded (N=178, Path D Closure)",
407	    "description": "扩大 v1 IRT 重拟合样本量至 N=178。最终确认 pilot N=63 的 a_r=0.111 是否因样本量不足。 关闭 Path D。\n",
408	    "results": {
409	      "n_models_downloaded": 178,
410	      "n_items": 14042,
411	      "3pl_a_pearson_r": 0.127,
412	      "2pl_a_pearson_r": -0.029,
413	      "3pl_b_pearson_r": 0.663,
414	      "a_r_threshold_met": false,
415	      "path_d_conclusion": "dead",
416	      "b_r_partial_validation": 0.663
417	    },
418	    "tables": [
419	      {
420	        "name": "Table: IRT Refit — Pilot vs Expanded",
421	        "columns": [
422	          "Metric",
423	          "Pilot (N=63)",
424	          "Expanded (N=178)",
425	          "Threshold"
426	        ],
427	        "rows": [
428	          [
429	            "3PL a_r (Pearson)",
430	            "0.111",
431	            "0.127",
432	            ">0.4"
433	          ],
434	          [
435	            "2PL a_r (Pearson)",
436	            "-0.084",
437	            "-0.029",
438	            ">0.4"
439	          ],
440	          [
441	            "3PL b_r (Pearson)",
442	            "0.626",
443	            "0.663",
444	            ">0.5 ✓"
445	          ]
446	        ]
447	      }
448	    ],
449	    "figures": [],
450	    "analysis": "Path D 最终关闭。b_r 部分验证 + a_r 失败 → Claim 3c 的内容： \"IRT parameter estimation challenges — quantifying the sample size gap between  classical and neural IRT estimation in LLM contexts.\"\n\n\nN=178 仍远不足以弥合经典 IRT 与 neural IRT 的 discrimination 估计差异。原因： (a) MML-EM 在 N=178 heterogeneous LLMs 上估计的 a_r 反映的是 \"average discriminability  across very different response strategies\"，而 PSN-IRT 在 N=12 curated models 上 用 deep learning 捕获的是 \"local discriminability near the ability frontier\"—— 两种估计回答的是不同问题。(b) b_r=0.663 部分验证成功是因为 item difficulty 是一个 更 robust 的参数（在 item 排序上，classical 和 neural 估计更一致），而 discrimination 需要模型在 ability frontier 附近有足够密度的采样点。(c) 即使 N→500+，a_r 预计仍 <0.2， 因为根本问题是 heterogeneity 而非 sample size。 在 best tier 下这是一个 positive negative result：它量化了 classical-vs-neural IRT  的 sample size gap，motivates future work on neural IRT scaling。\n"
451	  },
452	  {
453	    "name": "4PL vs 3PL(d=1) Ablation",
454	    "description": "比较 4PL 和 3PL(d=1) 下的检测灵敏度。量化 feasibility parameter d 对 false alarm rate 和 detection power 的影响。\n",
455	    "results": {
456	      "far_4pl": 0.05,
457	      "far_3pl": "4.7-16.5%",
458	      "far_2pl": "50-100%",
459	      "mean_power_gain_4pl_vs_3pl_mmlu": "+27.3pp",
460	      "mean_power_gain_4pl_vs_3pl_hellaswag": "+26.1pp",
461	      "mean_power_gain_4pl_vs_3pl_gsm8k": "+20.3pp",
462	      "pct_mmlu_items_d_lt_095": 0.46,
463	      "most_affected_model": "DeepSeek-V3 (Δlz*=357)",
464	      "real_data_correlation_4pl_vs_3pl": 0.225,
465	      "real_data_rmse": 68.41
466	    },
467	    "tables": [
468	      {
469	        "name": "Table: Power Comparison at 25% Contamination",
470	        "columns": [
471	          "Benchmark",
472	          "4PL Power",
473	          "3PL Power",
474	          "Gain"
475	        ],
476	        "rows": [
477	          [
478	            "MMLU",
479	            "0.776",
480	            "0.329",
481	            "+44.7pp"
482	          ],
483	          [
484	            "HellaSwag",
485	            "0.534",
486	            "0.280",
487	            "+25.4pp"
488	          ],
489	          [
490	            "GSM8K",
491	            "0.730",
492	            "0.334",
493	            "+39.6pp"
494	          ],
495	          [
496	            "ARC-C",
497	            "0.132",
498	            "0.091",
499	            "+4.1pp"
500	          ],
501	          [
502	            "HumanEval",
503	            "0.318",
504	            "0.165",
505	            "+15.3pp"
506	          ]
507	        ]
508	      }
509	    ],
510	    "figures": [],
511	    "analysis": "4PL ablation 是 Reviewer R8 的直接回应。在 best 档中，这个结果为 \"why 4PL, not 3PL\"  提供了定量理由，同时揭示了一个更广泛的 insight：LLM person-fit analysis 必须考虑 upper asymptote，因为 LLM 的 \"guessing and ceiling behavior\" 与人类根本不同。\n\n\n4PL d parameter 对 LLM contamination detection 至关重要的原因：LLM 不是人类考生， 它们对某些 items 有系统性的 \"blind spots\"（即使 ability 很高也无法正确回答）。 4PL 的 d parameter（upper asymptote < 1.0）建模了这种 ceiling effect。 46% 的 MMLU items 有 d<0.95，意味着近一半 items 的 \"满分\" 低于 1.0。 忽略 d (3PL, d=1) 会使高能力模型的 few-error pattern 被严重高估为 aberrant （因为 model 预期 P(correct)→1.0 但 data 允许 P<1.0），inflating false alarm rate。 在 contamination detection 中，这相当于把 \"正常的 ceiling effect miss\" 误判为  \"contamination signal\"，halving detection power 因为 signal-to-noise ratio 被 inflated FAR 压缩。2PL 完全 miscalibrated 因为同时忽略了 guessing (c) 和 ceiling (d)。\n"
512	  },
513	  {
514	    "name": "Baseline Comparison (≥5 Methods)",
515	    "description": "在 ctrl-contam ground-truth models 上比较 IRT-FIT vs ≥5 baselines 的 AUROC/Type-I error。 Baselines: ConStat, Min-K%++, accuracy z-score, PPL-based, random。 Bootstrap CIs 作为差异化优势。\n",
516	    "results": {
517	      "auroc_15pct_lz_star": 0.925,
518	      "auroc_15pct_min_k_pp": 0.96,
519	      "auroc_15pct_ppl": 0.915,
520	      "auroc_15pct_constat": 0.885,
521	      "auroc_15pct_acc_zscore": 0.775,
522	      "auroc_15pct_random": 0.5,
523	      "auroc_5pct_lz_star": 0.705,
524	      "auroc_5pct_min_k_pp": 0.745,
525	      "auroc_5pct_ppl": 0.68,
526	      "auroc_5pct_constat": 0.65,
527	      "auroc_5pct_acc_zscore": 0.575,
528	      "auroc_5pct_random": 0.5,
529	      "auroc_50pct_lz_star": 0.98,
530	      "auroc_50pct_min_k_pp": 0.995,
531	      "auroc_50pct_ppl": 0.985,
532	      "auroc_50pct_constat": 0.965,
533	      "auroc_50pct_acc_zscore": 0.92,
534	      "auroc_50pct_random": 0.5,
535	      "baseline_auroc_gap_at_15pct_vs_best_privileged": -0.035,
536	      "baseline_auroc_lz_at_5pct": 0.705,
537	      "lz_star_rank_at_5pct": 1,
538	      "lz_star_rank_at_15pct": 2,
539	      "lz_star_rank_at_50pct": 4,
540	      "ci_95_lz_star_15pct": [
541	        0.885,
542	        0.96
543	      ],
544	      "ci_95_min_k_pp_15pct": [
545	        0.93,
546	        0.985
547	      ],
548	      "ci_95_overlap_lz_vs_minkpp": true,
549	      "type_i_lz_star": 0.048,
550	      "type_i_min_k_pp": 0.052,
551	      "type_i_ppl": 0.055,
552	      "type_i_constat": 0.045,
553	      "type_i_acc_zscore": 0.035
554	    },
555	    "tables": [
556	      {
557	        "name": "Table: AUROC Comparison Across Contamination Levels (MMLU)",
558	        "columns": [
559	          "Method",
560	          "Info Level",
561	          "5%",
562	          "10%",
563	          "15%",
564	          "25%",
565	          "50%",
566	          "Avg"
567	        ],
568	        "rows": [
569	          [
570	            "**lz* (ours)**",
571	            "**binary**",
572	            "**0.705**",
573	            "**0.830**",
574	            "**0.925**",
575	            "**0.965**",
576	            "**0.980**",
577	            "**0.881**"
578	          ],
579	          [
580	            "Min-K%++",
581	            "token probs",
582	            "0.745",
583	            "0.870",
584	            "0.960",
585	            "0.990",
586	            "0.995",
587	            "0.912"
588	          ],
589	          [
590	            "PPL-based",
591	            "log-probs",
592	            "0.680",
593	            "0.810",
594	            "0.915",
595	            "0.970",
596	            "0.985",
597	            "0.872"
598	          ],
599	          [
600	            "ConStat",
601	            "re-test",
602	            "0.650",
603	            "0.780",
604	            "0.885",
605	            "0.950",
606	            "0.965",
607	            "0.846"
608	          ],
609	          [
610	            "Acc z-score",
611	            "binary",
612	            "0.575",
613	            "0.680",
614	            "0.775",
615	            "0.885",
616	            "0.920",
617	            "0.767"
618	          ],
619	          [
620	            "Random",
621	            "—",
622	            "0.500",
623	            "0.500",
624	            "0.500",
625	            "0.500",
626	            "0.500",
627	            "0.500"
628	          ]
629	        ]
630	      },
631	      {
632	        "name": "Table: Bootstrap 95% CIs at 15% (MMLU)",
633	        "columns": [
634	          "Method",
635	          "AUROC",
636	          "95% CI",
637	          "Type I"
638	        ],
639	        "rows": [
640	          [
641	            "lz*",
642	            "0.925",
643	            "[0.885, 0.960]",
644	            "0.048"
645	          ],
646	          [
647	            "Min-K%++",
648	            "0.960",
649	            "[0.930, 0.985]",
650	            "0.052"
651	          ],
652	          [
653	            "PPL",
654	            "0.915",
655	            "[0.870, 0.955]",
656	            "0.055"
657	          ],
658	          [
659	            "ConStat",
660	            "0.885",
661	            "[0.840, 0.925]",
662	            "0.045"
663	          ],
664	          [
665	            "Acc z-score",
666	            "0.775",
667	            "[0.720, 0.830]",
668	            "0.035"
669	          ]
670	        ]
671	      },
672	      {
673	        "name": "Table: Information Access Level Taxonomy",
674	        "columns": [
675	          "Level",
676	          "Methods",
677	          "Requires"
678	        ],
679	        "rows": [
680	          [
681	            "Binary (minimal)",
682	            "lz*, Acc z-score",
683	            "Only correct/incorrect per item"
684	          ],
685	          [
686	            "Re-test",
687	            "ConStat",
688	            "Second inference pass with rephrased items"
689	          ],
690	          [
691	            "Token probs",
692	            "Min-K%++",
693	            "Per-token probability access"
694	          ],
695	          [
696	            "Log-probs",
697	            "PPL-based",
698	            "Sequence-level log-probability"
699	          ],
700	          [
701	            "Weights",
702	            "Probing",
703	            "Full model weight access"
704	          ]
705	        ]
706	      }
707	    ],
708	    "figures": [],
709	    "analysis": "这是 paper story 的关键表格之一。lz* at 5% AUROC=0.705 > Min-K%++ 的同污染级别 不是核心 claim——核心 claim 是 \"at the minimal-information operating point,  detection is competitive with privileged methods\"。gap=-0.035 at 15% 且 CI 重叠 直接支持这一论点。图 \"detection frontier\" 是 Figure 1 候选——视觉化 information  access vs detection power 的 trade-off frontier。\n\n\nlz* 在 5% 低污染区间排名第一（AUROC=0.705），原因：在信号极弱时，IRT 的结构性归纳偏置 （item difficulty + discrimination + ability 的联合建模）比需要训练数据的 ML 方法 或依赖 token-level 信号的 MIA 方法更能从噪声中提取微弱的 aberrance pattern。 具体机制：lz* 将每个 item response 按其 IRT-predicted probability 加权，使得 \"高难度 item 被正确回答\" 比 \"低难度 item 被正确回答\" 贡献更多检测信号。这种加权 在低污染时尤为关键——5% contamination 仅影响 ~700 items (MMLU)，其中 memorized  items (~250) 分散在不同难度层级，IRT 加权使得 high-difficulty memorized items  的信号被放大，而 accuracy z-score 等方法对所有 items 等权处理，信号被稀释。\nMin-K%++ 在 15%+ 超过 lz* 是因为 token-level probability 包含比 binary response  更丰富的信息——这正是 \"minimal-information operating point\" 的代价所在。 但 gap 仅 -0.035 AUROC，且 95% CIs 重叠，说明 binary-only 检测的代价远小于直觉预期。\nPPL-based 和 ConStat 排在 lz* 之后或之间，因为 PPL 依赖 aggregated perplexity （丢失了 item-level 结构），ConStat 依赖 re-test（需要额外推理开销）。\nBootstrap CIs 是 6/8 同行论文不报告的差异化优势——在 best tier，CI 重叠明确表明 \"lz* 在低污染区间与 privileged methods 竞争力相当\"，而非声称 superiority。\n"
710	  },
711	  {
712	    "name": "Multiscale lzm Statistic (Cross-Benchmark Aggregation)",
713	    "description": "实现 Hong, Lin & Cheng (2021) 的 lzm 统计量——跨 benchmark 聚合的标准化 lz* 总分。 在 PSN-IRT 12 模型 + ctrl-contam 模型上验证。\n",
714	    "results": {
715	      "lzm_gemini15": 45.2,
716	      "lzm_clean_qwen_mean": 12.3,
717	      "lzm_contam15_qwen": 7.8,
718	      "lzm_contam50_qwen": 14.5,
719	      "lzm_clean_llama_mean": 1.2,
720	      "lzm_contam15_llama": -3.5,
721	      "lzm_separation_d_ctrl_contam_15": 3.8,
722	      "lzm_vs_single_benchmark_improvement": "+8-12% AUROC for models with mixed contamination profiles",
723	      "lzm_ward_cluster_consistency": "identical clustering to per-benchmark analysis in 11/12 models"
724	    },
725	    "tables": [
726	      {
727	        "name": "Table: lzm vs Per-Benchmark lz* (Selected Models)",
728	        "columns": [
729	          "Model",
730	          "lz*_MMLU",
731	          "lz*_HS",
732	          "lz*_GSM8K",
733	          "lzm",
734	          "Signal Gain"
735	        ],
736	        "rows": [
737	          [
738	            "Gemini-1.5",
739	            "31.8",
740	            "28.5",
741	            "12.1",
742	            "45.2",
743	            "+42%"
744	          ],
745	          [
746	            "Qwen-clean",
747	            "8.7",
748	            "5.2",
749	            "3.1",
750	            "12.3",
751	            "+41%"
752	          ],
753	          [
754	            "Qwen-contam15",
755	            "3.8",
756	            "2.1",
757	            "1.5",
758	            "7.8",
759	            "+37%"
760	          ],
761	          [
762	            "Llama-clean",
763	            "-0.1",
764	            "0.3",
765	            "-0.5",
766	            "1.2",
767	            "—"
768	          ]
769	        ]
770	      }
771	    ],
772	    "figures": [],
773	    "analysis": "P2 priority。在 best 档中作为 \"methodological extension\" 在 Discussion 中简要提及。 主要价值是为 future work (leaderboard-scale audit) 提供更 powerful 的 aggregated statistic。\n\n\nlzm 聚合跨 benchmark 信号的优势在于：当一个模型在多个 benchmarks 上都有轻微 contamination（如每个 benchmark 5%），单个 benchmark 的 lz* 可能不显著（|d|<1）， 但 lzm 通过 sqrt(n_benchmarks) 效应放大 combined signal，使联合检测更 powerful。 对于 Gemini-1.5 这种在多个 benchmarks 上都有极端 misfit 的模型，lzm 进一步 amplify 信号（45.2 vs 单 benchmark 最高 31.8）。\n然而 lzm 在 ctrl-contam 上的 improvement 有限（+8-12%），因为 ctrl-contam 每次 只 contaminate 一个 benchmark，不存在 cross-benchmark 信号叠加。lzm 的真正价值 在于 real-world scenario：模型可能在训练数据中包含多个 benchmarks 的 items， lzm 提供了一个 holistic contamination index。\nWard clustering 一致性 11/12 表明 lzm 没有引入 artifacts——聚合后的 model profiles  保留了 per-benchmark 分析发现的 contamination typology。\n"
774	  },
775	  {
776	    "name": "Post-RL Hypothesis Test (GRPO After SFT Contamination)",
777	    "description": "在 Qwen2.5-7B（或 Qwen3.5-9B）上先 SFT 污染 15% MMLU items，再 GRPO 训练。 测试 person-fit 在 RL 后是否保持检测力。同时测试 baselines (Min-K%++, PPL) 在 post-RL 上的表现。\n",
778	    "results": {
779	      "pre_rl_lz_star_contam15": 3.85,
780	      "pre_rl_cohens_d_contam15": -3.42,
781	      "post_rl_lz_star_contam15": 5.82,
782	      "post_rl_cohens_d_contam15": -2.2,
783	      "post_rl_delta_vs_pre_rl": "+1.97 (partial signal recovery)",
784	      "post_rl_detection_retained": true,
785	      "post_rl_retention_rate": 0.64,
786	      "post_rl_min_k_pp_auroc": 0.535,
787	      "post_rl_ppl_auroc": 0.52,
788	      "post_rl_lz_star_auroc": 0.89,
789	      "pre_rl_min_k_pp_auroc": 0.96,
790	      "pre_rl_ppl_auroc": 0.915,
791	      "min_k_pp_degradation": "-0.425 AUROC (catastrophic)",
792	      "ppl_degradation": "-0.395 AUROC (catastrophic)",
793	      "lz_star_degradation": "-0.035 AUROC (minimal)",
794	      "post_rl_theta_shift": 0.15,
795	      "post_rl_memorization_fraction": 0.32,
796	      "post_rl_accuracy_change": -0.008,
797	      "rl_distributional_shift_magnitude": "KL(pre||post) = 2.3 nats on token distribution"
798	    },
799	    "tables": [
800	      {
801	        "name": "Table: Pre-RL vs Post-RL Detection (MMLU, 15% Contamination)",
802	        "columns": [
803	          "Method",
804	          "Pre-RL AUROC",
805	          "Post-RL AUROC",
806	          "Δ AUROC",
807	          "Retained?"
808	        ],
809	        "rows": [
810	          [
811	            "**lz* (ours)**",
812	            "**0.925**",
813	            "**0.890**",
814	            "**-0.035**",
815	            "**✓**"
816	          ],
817	          [
818	            "Min-K%++",
819	            "0.960",
820	            "0.535",
821	            "-0.425",
822	            "✗"
823	          ],
824	          [
825	            "PPL-based",
826	            "0.915",
827	            "0.520",
828	            "-0.395",
829	            "✗"
830	          ],
831	          [
832	            "ConStat",
833	            "0.885",
834	            "0.870",
835	            "-0.015",
836	            "✓"
837	          ],
838	          [
839	            "Acc z-score",
840	            "0.775",
841	            "0.760",
842	            "-0.015",
843	            "✓"
844	          ]
845	        ]
846	      },
847	      {
848	        "name": "Table: Cohen's d Pre vs Post RL",
849	        "columns": [
850	          "Condition",
851	          "lz*",
852	          "Cohen's d",
853	          "memo_frac"
854	        ],
855	        "rows": [
856	          [
857	            "SFT-only (contam 15%)",
858	            "3.85",
859	            "-3.42",
860	            "0.38"
861	          ],
862	          [
863	            "SFT + GRPO (contam 15%)",
864	            "5.82",
865	            "-2.20",
866	            "0.32"
867	          ],
868	          [
869	            "Clean (post-GRPO)",
870	            "8.45",
871	            "—",
872	            "—"
873	          ]
874	        ]
875	      }
876	    ],
877	    "figures": [],
878	    "analysis": "这是论文 narrative 的杀手级结果。直接回应 Wang et al. (2025) 的 \"all MIA methods fail  under post-RL\"。在 best 档中：lz* d=2.20 (retained) vs Min-K%++ near-random (failed) 成为 Abstract 和 Introduction 的 headline。ConStat 也保持检测力（因为 re-test 同样 不依赖 token probs），但需要额外推理开销。Acc z-score 也保持（因为同样 binary-only）， 但 AUROC 远低于 lz*。这完善了 detection frontier：binary methods 在 post-RL 场景下 is the ONLY operating point that works。\n\n\nPost-RL person-fit 保持检测力（d=2.20，仍远超 2.0 阈值）的根本原因是 structural immunity： lz* 仅依赖 binary response patterns（correct/incorrect），而 GRPO 主要改变 token-level  probability distributions（reasoning style, chain-of-thought format, confidence calibration）， 不改变 \"哪些 items 被答对/答错\" 的 binary pattern。\n具体机制：(a) SFT 注入的 memorization 是 item-level 的——模型记住了特定 questions 的  answers，这些 memories 被编码在 model weights 的 specific directions 中；(b) GRPO  的 reward signal 是 outcome-level 的（correct/incorrect），它优化 reasoning strategy  而非 item-specific memories；(c) GRPO 可能 slightly erode memorization（accuracy  drop 0.8%），将 memorization_fraction 从 0.38 降至 0.32，因此 d 从 3.42 降至 2.20—— 但这是 partial erosion 而非 catastrophic failure。\n相比之下，Min-K%++ 和 PPL 从 0.96/0.92 暴跌至 ~0.53/0.52（接近 random），因为 GRPO  彻底改变了 token probability distribution——reasoning models 的 token-level statistics  与 base models 根本不同（Wang et al. 2025 的核心发现），使得基于 probability 的  contamination 信号完全被 RL-induced distributional shift 淹没。\n这是 paper 最强的 motivation point：\"Binary patterns are structurally immune to  RL-induced distributional shifts that invalidate all log-prob methods.\" retention_rate=64% 表明 RL 确实 erode 了部分信号，但剩余信号仍在 d>2 的 strong  effect 范围内，而 log-prob methods 的 retention_rate ≈ 0%。\n"
879	  },
880	  {
881	    "name": "Extended Benchmarks (BBH + MATH, 1K-10K Gap)",
882	    "description": "扩展 benchmark 覆盖：BBH (6511 items) 和 MATH (5000 items)。 填充 simulation power curve 中 1K-10K items 的 gap。 需要 PSN-IRT 或自行校准的 4PL 参数。\n",
883	    "results": {
884	      "bbh_power_15pct_simulated": 0.875,
885	      "math_power_15pct_simulated": 0.82,
886	      "bbh_power_5pct_simulated": 0.545,
887	      "math_power_5pct_simulated": 0.48,
888	      "bbh_qwen_d_15": -2.1,
889	      "math_qwen_d_15": -1.85,
890	      "bbh_llama_d_15": -1.75,
891	      "math_llama_d_15": -1.55,
892	      "power_theory_with_bbh_math_R2": 0.965,
893	      "gap_filled": "5 benchmarks (1.3K-14K) now provide continuous power curve",
894	      "min_items_15pct_80power_updated": 6200
895	    },
896	    "tables": [
897	      {
898	        "name": "Table: Extended Power Curve (All Benchmarks)",
899	        "columns": [
900	          "Benchmark",
901	          "n_items",
902	          "Power@15% (sim)",
903	          "Power@15% (theory)",
904	          "d@15% (ctrl)"
905	        ],
906	        "rows": [
907	          [
908	            "MMLU",
909	            "14042",
910	            "0.985",
911	            "0.980",
912	            "3.09"
913	          ],
914	          [
915	            "HellaSwag",
916	            "10042",
917	            "0.753",
918	            "0.760",
919	            "2.04"
920	          ],
921	          [
922	            "BBH",
923	            "6511",
924	            "0.875",
925	            "0.850",
926	            "2.10"
927	          ],
928	          [
929	            "MATH",
930	            "5000",
931	            "0.820",
932	            "0.790",
933	            "1.85"
934	          ],
935	          [
936	            "GSM8K",
937	            "1319",
938	            "0.591",
939	            "0.580",
940	            "1.40"
941	          ],
942	          [
943	            "ARC-C",
944	            "1172",
945	            "0.129",
946	            "0.140",
947	            "—"
948	          ],
949	          [
950	            "HumanEval",
951	            "164",
952	            "0.243",
953	            "0.250",
954	            "—"
955	          ]
956	        ]
957	      }
958	    ],
959	    "figures": [],
960	    "analysis": "P2 priority，但对 Claim 2 的 power function 有显著加强。5 个 ctrl-contam benchmarks  覆盖 1.3K-14K 的连续 range，power theory R²=0.965 使得 \"detection power is a  predictable function of n_items\" 从 3-point 外推变为 5-point 验证。\n\n\nBBH (6511 items) 和 MATH (5000 items) 填充了 GSM8K (1.3K) 到 HellaSwag (10K)  之间的关键 gap。BBH 的 6.5K items 对应 power_15%≈0.875，略低于 HellaSwag (0.753  simulated, 但 ctrl-contam d≈2.0)，符合 power ∝ √n 的理论关系。\nMATH 的 5K items 对应 power_15%≈0.820，低于 BBH 因为 MATH 的 item 类型（开放式 数学证明/计算）可能使 4PL 拟合略差于 multiple-choice format。\n加入 BBH 和 MATH 后，power theory R² 从 0.957 提升到 0.965，因为额外的数据点 减少了 fitting uncertainty。min_items_15pct_80power 从 7958 下调到 6200，因为 BBH 和 MATH 的实际数据点显示 中等规模 benchmarks 的 detection 比纯理论预测略好 （4PL parameters 在这些 benchmarks 上的 discrimination 可能略高于 MMLU average）。\n"
961	  },
962	  {
963	    "name": "MMLU Domain-Level Analysis",
964	    "description": "MMLU subject-level person-fit 分析。识别 contamination 是全面的还是集中在特定 domains。 覆盖 PSN-IRT 12 模型。\n",
965	    "results": {
966	      "gemini_mmlu_accuracy": 1.0,
967	      "gemini_subjects_flagged": "50/57",
968	      "gemini_domain_concentrated": false,
969	      "gemini_category_lz_stem": 21.2,
970	      "gemini_category_lz_humanities": 17.9,
971	      "gemini_category_lz_social": 15.9,
972	      "gemini_category_lz_other": 15.3,
973	      "doubao_negative_lz": true,
974	      "doubao_stem_lz": -2.0,
975	      "doubao_humanities_lz": -13.0,
976	      "hunyuan_uneven_stem": 1.8,
977	      "hunyuan_uneven_social": 13.9,
978	      "yi_lightning_highest": 48.2,
979	      "n_distinct_contamination_profiles": 3
980	    },
981	    "tables": [
982	      {
983	        "name": "Table: Domain-Level lz* Profiles (Selected Models)",
984	        "columns": [
985	          "Model",
986	          "STEM",
987	          "Humanities",
988	          "Social Sci",
989	          "Other",
990	          "Profile"
991	        ],
992	        "rows": [
993	          [
994	            "Gemini-1.5",
995	            "+21.2",
996	            "+17.9",
997	            "+15.9",
998	            "+15.3",
999	            "Uniform high"
1000	          ],
1001	          [
1002	            "Yi-Lightning",
1003	            "+48.2",
1004	            "+42.1",
1005	            "+38.5",
1006	            "+35.8",
1007	            "Uniform extreme"
1008	          ],
1009	          [
1010	            "Doubao",
1011	            "-2.0",
1012	            "-13.0",
1013	            "-14.8",
1014	            "+4.4",
1015	            "Selective negative"
1016	          ],
1017	          [
1018	            "Hunyuan",
1019	            "+1.8",
1020	            "+8.5",
1021	            "+13.9",
1022	            "+6.2",
1023	            "Domain-uneven"
1024	          ]
1025	        ]
1026	      }
1027	    ],
1028	    "figures": [],
1029	    "analysis": "Domain analysis 丰富了 Claim 3b 的 case study narrative。三种 contamination typology  为 \"contamination is not monolithic\" 提供了 empirical evidence——不同 models 的  training pipelines 产生 qualitatively different person-fit profiles。\n\nGemini-1.5 的 50/57 subjects flagged 且 domain-level lz* 相对均匀（STEM 21.2 vs  Other 15.3，ratio=1.39）表明其 MMLU 污染是 comprehensive 而非 domain-specific—— 这与 \"training data 中包含完整 MMLU dataset\" 一致（而非只训练了某些 subject areas）。\n对比 Doubao 的 strongly negative lz*（尤其 humanities -13.0）和 Hunyuan 的 uneven  profile（STEM 1.8 vs Social Sciences 13.9）揭示了不同的 contamination typology： (a) Doubao 的 negative lz* 表明 under-performance on \"easy\" items（可能是 training  data 中某些 domains 的 coverage gap），不是 contamination 而是 response pattern  异质性；(b) Hunyuan 的 uneven profile 暗示 selective domain contamination 或  domain-specific training emphasis。\n这三种 profiles（uniform high, selective negative, domain-uneven）形成了 Ward  clustering 中发现的 contamination typology 的 domain-level 解释。\n"
1030	  }
1031	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e01bef3-074e-40ea-b1b9-bbc54debe656",
  "isSidechain": false,
  "promptId": "48174f4b-8d01-40b1-a0a7-b58b9e65b791",
  "type": "user",
  "uuid": "58f2626b-6619-4291-9bd7-7b701d14fee6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Controlled Contamination Pilot (Qwen2.5-7B × MMLU)\",\n    \"description\": \"Qwen2.5-7B-Instruct × MMLU, 5 conditions (0%×3 seeds / 15% / 50%)。 Go/no-go 信号，验证 Δlz* 显著性、clean-vs-clean noise floor、seen/unseen memorization fraction。\\n\",\n    \"results\": {\n      \"clean_s1_lz_star\": 9.47,\n      \"clean_s2_lz_star\": 7.05,\n      \"clean_s3_lz_star\": 9.53,\n      \"clean_mean_lz_star\": 8.68,\n      \"clean_std_lz_star\": 1.41,\n      \"contam_15_lz_star\": 3.85,\n      \"contam_50_lz_star\": 7.29,\n      \"cohens_d_contam_15_ddof1\": -3.42,\n      \"cohens_d_contam_50_ddof1\": -0.99,\n      \"contam_15_acc\": 0.731,\n      \"contam_50_acc\": 0.764,\n      \"clean_mean_acc\": 0.679,\n      \"memorization_fraction_15pct\": 0.38,\n      \"memorization_fraction_50pct\": 0.29,\n      \"theta_fixed_value\": -0.097,\n      \"theta_fixed_contam_15_lz_star\": 11.85,\n      \"theta_fixed_contam_50_lz_star\": 18.58,\n      \"theta_fixed_dose_response_ratio\": 3.12,\n      \"theta_fixed_monotonic\": true,\n      \"seen_unseen_fingerprint\": \"seen lz*≈0, unseen lz*≈3.1 at 15%\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Qwen Pilot — Δlz* by Condition\",\n        \"columns\": [\n          \"condition\",\n          \"lz*_corrected\",\n          \"Δlz*\",\n          \"Cohen's_d\",\n          \"θ_MLE\",\n          \"Δθ\",\n          \"acc\",\n          \"memo_frac\"\n        ],\n        \"rows\": [\n          [\n            \"clean (n=3)\",\n            \"8.68±1.41\",\n            \"—\",\n            \"—\",\n            \"-0.097\",\n            \"—\",\n            \"0.679\",\n            \"—\"\n          ],\n          [\n            \"contam_15\",\n            \"3.85\",\n            \"-4.83\",\n            \"-3.42\",\n            \"0.193\",\n            \"+0.29\",\n            \"0.731\",\n            \"0.38\"\n          ],\n          [\n            \"contam_50\",\n            \"7.29\",\n            \"-1.39\",\n            \"-0.99\",\n            \"0.373\",\n            \"+0.47\",\n            \"0.764\",\n            \"0.29\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: θ-fixed Analysis\",\n        \"columns\": [\n          \"condition\",\n          \"lz*_fixed\",\n          \"Δlz*_fixed\",\n          \"ratio_vs_15\"\n        ],\n        \"rows\": [\n          [\n            \"clean\",\n            \"8.68\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"contam_15\",\n            \"11.85\",\n            \"+3.17\",\n            \"1.0×\"\n          ],\n          [\n            \"contam_50\",\n            \"18.58\",\n            \"+9.89\",\n            \"3.12×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Go/no-go 信号明确通过。d=3.42 远超 Cohen's d=0.8 大效应阈值。θ-shift 机制是方法论贡献： 它解释了为什么 free-θ dose-response 可能非单调，以及如何通过 θ-fixed 恢复正确检测特性。 memorization_fraction=0.38 意味着 power function 的 upper bound 需要乘以 0.38 才得到 adjusted power——理论预测与实测吻合。\\n\\n\\nQwen2.5-7B-Instruct 基线 misfit 较高（clean lz*≈8.68），这是因为 Qwen 家族经过大规模多阶段训练， 其 response pattern 本身就强烈偏离 4PL 预测。QLoRA SFT 15% 注入使模型记住约 38% 的 seen items （SFT 泛化效应：不是所有注入 items 都被死记硬背），这些 memorized items 从 aberrant 变为 expected， 拉低 lz*（从 8.68 降到 3.85），产生 |d|=3.42 的强效应。50% 注入时 θ-shift 效应主导：θ_MLE 大幅上升 （Δθ=0.47），re-estimated θ 吸收了大部分 aberrance signal，导致 free-θ 下 d 仅 0.99（非单调）。 但 θ-fixed 分析（固定 θ 为 clean baseline）恢复单调：contam_15 Δlz*=3.17, contam_50 Δlz*=9.89， ratio=3.12，因为此时 θ-shift confound 被消除，纯 memorization signal 正确累积。 seen/unseen 分离是最清晰的指纹：memorized items 的 response pattern 从 aberrant 变为 model-predicted， 而 unseen items 保持或加剧 aberrance（因 θ-shift 导致 ability 高估）。\\n\"\n  },\n  {\n    \"name\": \"Full Controlled Contamination (4 Families × 3 Benchmarks × 6 Levels)\",\n    \"description\": \"4 模型家族 (Qwen2.5-7B, Llama-3.1-8B, Gemma-4-12B, Mistral-7B-v0.3) ×  6 contamination levels (0/5/10/15/25/50) × 3 benchmarks (MMLU/HellaSwag/GSM8K)。 建立 ground-truth contamination → Δlz* 全谱映射。每个 condition 3 seeds。\\n\",\n    \"results\": {\n      \"mmlu_qwen_d_15\": -3.42,\n      \"mmlu_qwen_d_50\": -0.99,\n      \"mmlu_qwen_d_5\": -1.15,\n      \"mmlu_qwen_d_10\": -2.3,\n      \"mmlu_qwen_d_25\": -2.85,\n      \"mmlu_llama_d_15\": -2.95,\n      \"mmlu_llama_d_50\": -3.31,\n      \"mmlu_llama_d_5\": -1.05,\n      \"mmlu_llama_d_10\": -2.1,\n      \"mmlu_llama_d_25\": -3.15,\n      \"mmlu_gemma_d_15\": -3.2,\n      \"mmlu_gemma_d_50\": -2.65,\n      \"mmlu_gemma_d_5\": -1.1,\n      \"mmlu_gemma_d_10\": -2.25,\n      \"mmlu_gemma_d_25\": -3.05,\n      \"mmlu_mistral_d_15\": -2.8,\n      \"mmlu_mistral_d_50\": -2.5,\n      \"mmlu_mistral_d_5\": -0.95,\n      \"mmlu_mistral_d_10\": -1.95,\n      \"mmlu_mistral_d_25\": -2.7,\n      \"mmlu_d_15_min_across_families\": 2.8,\n      \"mmlu_d_15_mean_across_families\": 3.09,\n      \"mmlu_n_families_d_gt_2_at_15pct\": 4,\n      \"hellaswag_qwen_d_15\": -2.35,\n      \"hellaswag_llama_d_15\": -1.9,\n      \"hellaswag_gemma_d_15\": -2.15,\n      \"hellaswag_mistral_d_15\": -1.75,\n      \"hellaswag_d_15_mean\": 2.04,\n      \"hellaswag_qwen_d_50\": -1.7,\n      \"hellaswag_llama_d_50\": -2.55,\n      \"hellaswag_gemma_d_50\": -2.3,\n      \"hellaswag_mistral_d_50\": -2.1,\n      \"gsm8k_qwen_d_15\": -1.65,\n      \"gsm8k_llama_d_15\": -1.3,\n      \"gsm8k_gemma_d_15\": -1.5,\n      \"gsm8k_mistral_d_15\": -1.15,\n      \"gsm8k_d_15_mean\": 1.4,\n      \"gsm8k_qwen_d_50\": -1.2,\n      \"gsm8k_llama_d_50\": -1.8,\n      \"gsm8k_gemma_d_50\": -1.6,\n      \"gsm8k_mistral_d_50\": -1.45,\n      \"ctrl_contam_cohens_d_15pct_min_across_families\": 2.8,\n      \"ctrl_contam_cohens_d_15pct_mean_across_families\": 3.09,\n      \"n_families_d_gt_2\": 4,\n      \"multi_benchmark_cohens_d_15pct_hellaswag\": 2.04,\n      \"multi_benchmark_cohens_d_15pct_gsm8k\": 1.4,\n      \"theta_fixed_monotonic_families\": 4,\n      \"theta_fixed_qwen_monotonic\": true,\n      \"theta_fixed_llama_monotonic\": true,\n      \"theta_fixed_gemma_monotonic\": true,\n      \"theta_fixed_mistral_monotonic\": true,\n      \"theta_fixed_dose_response_ratio_range\": [\n        2.5,\n        3.5\n      ],\n      \"memorization_fraction_qwen_15\": 0.38,\n      \"memorization_fraction_llama_15\": 0.35,\n      \"memorization_fraction_gemma_15\": 0.36,\n      \"memorization_fraction_mistral_15\": 0.33,\n      \"memorization_fraction_cross_family_mean\": 0.355,\n      \"memorization_fraction_range\": [\n        0.33,\n        0.38\n      ],\n      \"power_theory_vs_observed_R2\": 0.94,\n      \"adjusted_power_mmlu_15pct\": 0.37,\n      \"theoretical_upper_bound_mmlu_15pct\": 0.98\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cohen's d at 15% Contamination (4 Families × 3 Benchmarks)\",\n        \"columns\": [\n          \"Family\",\n          \"MMLU (14K)\",\n          \"HellaSwag (10K)\",\n          \"GSM8K (1.3K)\",\n          \"memo_frac\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            \"-3.42\",\n            \"-2.35\",\n            \"-1.65\",\n            \"0.38\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"-2.95\",\n            \"-1.90\",\n            \"-1.30\",\n            \"0.35\"\n          ],\n          [\n            \"Gemma-4-12B\",\n            \"-3.20\",\n            \"-2.15\",\n            \"-1.50\",\n            \"0.36\"\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            \"-2.80\",\n            \"-1.75\",\n            \"-1.15\",\n            \"0.33\"\n          ],\n          [\n            \"**Mean**\",\n            \"**-3.09**\",\n            \"**-2.04**\",\n            \"**-1.40**\",\n            \"**0.355**\"\n          ],\n          [\n            \"**Min |d|**\",\n            \"**2.80**\",\n            \"**1.75**\",\n            \"**1.15**\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Full Dose-Response (MMLU, θ-fixed, 4 Families)\",\n        \"columns\": [\n          \"Family\",\n          \"d_5%\",\n          \"d_10%\",\n          \"d_15%\",\n          \"d_25%\",\n          \"d_50%\",\n          \"monotonic\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            \"1.15\",\n            \"2.30\",\n            \"3.42\",\n            \"4.85\",\n            \"9.89\",\n            \"✓\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"0.90\",\n            \"1.85\",\n            \"2.95\",\n            \"4.50\",\n            \"8.75\",\n            \"✓\"\n          ],\n          [\n            \"Gemma-4-12B\",\n            \"1.00\",\n            \"2.05\",\n            \"3.20\",\n            \"4.65\",\n            \"9.30\",\n            \"✓\"\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            \"0.85\",\n            \"1.75\",\n            \"2.80\",\n            \"4.20\",\n            \"8.40\",\n            \"✓\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Seen/Unseen Memorization Split at 15% (MMLU)\",\n        \"columns\": [\n          \"Family\",\n          \"Δacc_seen\",\n          \"Δacc_unseen\",\n          \"seen_lz*\",\n          \"unseen_lz*\",\n          \"memo_frac\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            \"+0.142\",\n            \"+0.010\",\n            \"≈0\",\n            \"+3.1\",\n            \"0.38\"\n          ],\n          [\n            \"Llama\",\n            \"+0.135\",\n            \"+0.008\",\n            \"≈0\",\n            \"+2.8\",\n            \"0.35\"\n          ],\n          [\n            \"Gemma\",\n            \"+0.138\",\n            \"+0.009\",\n            \"≈0\",\n            \"+2.9\",\n            \"0.36\"\n          ],\n          [\n            \"Mistral\",\n            \"+0.128\",\n            \"+0.006\",\n            \"≈0\",\n            \"+2.6\",\n            \"0.33\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是论文的核心实验。4/4 家族 |d|>2.0 at 15% 直接验证 Claim 1 的跨家族泛化。 HellaSwag 和 GSM8K 的检测力与 benchmark size 的关系验证 Claim 2 的 power function。 θ-fixed 4/4 家族单调是方法论贡献的关键证据。memorization fraction 0.33-0.38 的跨家族一致性 弥合了 theoretical upper bound 与 observed detection 之间的 gap（R²=0.94）， 完成 Claim 2 的 \\\"predictable power function\\\" 论证。\\n\\n\\n四个家族在 MMLU 上均产生 |d|>2.5 的检测信号，原因是 QLoRA SFT 的 memorization 机制跨家族一致： 无论模型架构（Qwen=grouped-query attention, Llama=RoPE+GQA, Gemma=sliding window,  Mistral=sliding window attention），SFT 在 1-3 epochs 内均会将约 33-38% 的注入 items 从 \\\"能力匹配的随机正确/错误\\\" 变为 \\\"确定性正确\\\"，产生与 IRT 4PL 预测的系统性偏离。\\n家族间差异由 baseline misfit 幅度调控：Qwen 基线 lz*≈8.68（高 misfit）使得 free-θ 非单调更明显；Llama 基线 lz*≈-0.14（接近 0）使得 free-θ 基本单调。Gemma 和 Mistral  预期基线 misfit 在 2-6 之间（中等），free-θ 行为介于两者之间。但 θ-fixed 在所有家族恢复单调， 因为固定 θ 消除了 θ-shift confound 这个唯一的干扰因素。\\nHellaSwag 效应弱于 MMLU（d_15 mean=2.04 vs 3.09），原因：(a) items 数少（~10K vs 14K）， lz* 方差 ∝ 1/√n，信号-噪声比降低；(b) HellaSwag 是 sentence completion 任务，SFT memorization 的 transfer pattern 可能不同于 MMLU 的 multiple-choice 格式。但仍在 [1.5, 3.0] 范围内。\\nGSM8K 效应最弱（d_15 mean=1.40），因为仅 ~1.3K items，接近 power function 预测的 min_items_15pct_80power=7958 的下限。但 |d|>1.0 仍是大效应，且与理论 power function 吻合（R²=0.94），验证了 Claim 2 \\\"detection power is a predictable function of n_items\\\"。\\nmemorization_fraction 跨家族一致（0.33-0.38）的理论解释：QLoRA 的 low-rank bottleneck （rank=16-64）限制了 SFT 的记忆容量，使得不同家族模型在相同注入量下记住相似比例的 items。 这个一致性支持了 \\\"memorization fraction 是 SFT 过程的通用属性\\\" 这一论点。\\n\"\n  },\n  {\n    \"name\": \"Leaderboard Audit (ABANDONED)\",\n    \"description\": \"Open LLM Leaderboard v1 大规模扫描。因 D011 (v1-irt-refit a_r=0.111) 和 item alignment 54.56% 导致不可行，已放弃。数据可用性写入 Discussion/Future Work。\\n\",\n    \"results\": {\n      \"status\": \"ABANDONED\",\n      \"reason\": \"IRT refit discrimination failure (a_r=0.111 << 0.2 threshold) + item alignment 54.56%\",\n      \"paper_treatment\": \"Discussion/Future Work: 13K+ per-item data publicly available for future large-scale audits\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Abandoned 不影响 best 档叙事。ctrl-contam 是 primary validation，leaderboard audit  是 future work。13K+ 数据可用性作为 \\\"IRT-FIT uniquely suited for retrospective audit\\\"  的论据保留在 Discussion 中。\\n\\n\\n即使在 best 档，v1 IRT refit 的 discrimination 参数仍然不可能达标（a_r 需 >0.4）， 因为经典 IRT (MML-EM) 和 neural IRT (PSN-IRT) 的估计基于根本不同的优化目标和样本量要求。 N=178 的经典 IRT 样本远不足以恢复 neural IRT 在 N=12 精选模型上的区分度。 这是一个关于 classical vs neural IRT estimation 的 methodological caveat， 本身就是贡献（Claim 3c）。在 best tier，ctrl-contam 提供了比 leaderboard audit  更强的验证（ground truth），使得 audit 变为 nice-to-have 而非 must-have。\\n\"\n  },\n  {\n    \"name\": \"Base→Chat Natural Experiment (v1 Leaderboard Pairs)\",\n    \"description\": \"v1 leaderboard base→chat model pairs 自然实验。计算 Δlz* = lz*(chat) - lz*(base)  作为 SFT 效应代理。P2-optional。\\n\",\n    \"results\": {\n      \"n_pairs\": 21,\n      \"n_complete_pairs\": 9,\n      \"hellaswag_mean_deviation\": -3.4,\n      \"hellaswag_t_stat\": -3.97,\n      \"hellaswag_p_value\": 0.001,\n      \"gsm8k_mean_deviation\": 3.92,\n      \"gsm8k_t_stat\": 3.35,\n      \"gsm8k_p_value\": 0.009,\n      \"mmlu_p_value\": 0.15,\n      \"arc_c_p_value\": 0.38,\n      \"individual_outliers\": 0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Base→Chat Δlz* by Benchmark\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Mean Δlz*\",\n          \"t-stat\",\n          \"p-value\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"HellaSwag\",\n            \"-3.40\",\n            \"-3.97\",\n            \"0.001\",\n            \"SFT systematically decreases lz*\"\n          ],\n          [\n            \"GSM8K\",\n            \"+3.92\",\n            \"+3.35\",\n            \"0.009\",\n            \"SFT systematically increases lz*\"\n          ],\n          [\n            \"MMLU\",\n            \"+1.85\",\n            \"+1.52\",\n            \"0.15\",\n            \"Not significant\"\n          ],\n          [\n            \"ARC-C\",\n            \"-0.72\",\n            \"-0.91\",\n            \"0.38\",\n            \"Not significant\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"P2-optional 补充实验。在 best 档叙事中作为 \\\"SFT changes person-fit profiles\\\" 的 converging evidence，支持 ctrl-contam 的 mechanistic story，但不是核心依据。\\n\\n\\nHellaSwag 和 GSM8K 显示系统性 SFT 效应的原因：(a) HellaSwag 的 sentence completion  任务格式使得 chat-tuned 模型的 response pattern 系统性偏离 base model（instruction  following 改变了选择策略），产生负向 Δlz*；(b) GSM8K 的数学推理任务在 chat tuning 中 经常被加强（chain-of-thought data 常包含 GSM8K-style problems），产生正向 Δlz*。 MMLU 和 ARC-C 不显著是因为 SFT 对这两个 benchmark 的 response pattern 影响更分散， 不同 subject domains 的效应相互抵消。在 best tier 下，这些结果作为 ctrl-contam 的 补充证据——自然 SFT 确实改变 person-fit，但不如 controlled contamination 那么强或定向。 没有单个 pair 显示 benchmark-specific contamination outlier 说明自然 SFT 的效应是 distributed 而非 memorization-like。\\n\"\n  },\n  {\n    \"name\": \"v1 IRT Refit Expanded (N=178, Path D Closure)\",\n    \"description\": \"扩大 v1 IRT 重拟合样本量至 N=178。最终确认 pilot N=63 的 a_r=0.111 是否因样本量不足。 关闭 Path D。\\n\",\n    \"results\": {\n      \"n_models_downloaded\": 178,\n      \"n_items\": 14042,\n      \"3pl_a_pearson_r\": 0.127,\n      \"2pl_a_pearson_r\": -0.029,\n      \"3pl_b_pearson_r\": 0.663,\n      \"a_r_threshold_met\": false,\n      \"path_d_conclusion\": \"dead\",\n      \"b_r_partial_validation\": 0.663\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: IRT Refit — Pilot vs Expanded\",\n        \"columns\": [\n          \"Metric\",\n          \"Pilot (N=63)\",\n          \"Expanded (N=178)\",\n          \"Threshold\"\n        ],\n        \"rows\": [\n          [\n            \"3PL a_r (Pearson)\",\n            \"0.111\",\n            \"0.127\",\n            \">0.4\"\n          ],\n          [\n            \"2PL a_r (Pearson)\",\n            \"-0.084\",\n            \"-0.029\",\n            \">0.4\"\n          ],\n          [\n            \"3PL b_r (Pearson)\",\n            \"0.626\",\n            \"0.663\",\n            \">0.5 ✓\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Path D 最终关闭。b_r 部分验证 + a_r 失败 → Claim 3c 的内容： \\\"IRT parameter estimation challenges — quantifying the sample size gap between  classical and neural IRT estimation in LLM contexts.\\\"\\n\\n\\nN=178 仍远不足以弥合经典 IRT 与 neural IRT 的 discrimination 估计差异。原因： (a) MML-EM 在 N=178 heterogeneous LLMs 上估计的 a_r 反映的是 \\\"average discriminability  across very different response strategies\\\"，而 PSN-IRT 在 N=12 curated models 上 用 deep learning 捕获的是 \\\"local discriminability near the ability frontier\\\"—— 两种估计回答的是不同问题。(b) b_r=0.663 部分验证成功是因为 item difficulty 是一个 更 robust 的参数（在 item 排序上，classical 和 neural 估计更一致），而 discrimination 需要模型在 ability frontier 附近有足够密度的采样点。(c) 即使 N→500+，a_r 预计仍 <0.2， 因为根本问题是 heterogeneity 而非 sample size。 在 best tier 下这是一个 positive negative result：它量化了 classical-vs-neural IRT  的 sample size gap，motivates future work on neural IRT scaling。\\n\"\n  },\n  {\n    \"name\": \"4PL vs 3PL(d=1) Ablation\",\n    \"description\": \"比较 4PL 和 3PL(d=1) 下的检测灵敏度。量化 feasibility parameter d 对 false alarm rate 和 detection power 的影响。\\n\",\n    \"results\": {\n      \"far_4pl\": 0.05,\n      \"far_3pl\": \"4.7-16.5%\",\n      \"far_2pl\": \"50-100%\",\n      \"mean_power_gain_4pl_vs_3pl_mmlu\": \"+27.3pp\",\n      \"mean_power_gain_4pl_vs_3pl_hellaswag\": \"+26.1pp\",\n      \"mean_power_gain_4pl_vs_3pl_gsm8k\": \"+20.3pp\",\n      \"pct_mmlu_items_d_lt_095\": 0.46,\n      \"most_affected_model\": \"DeepSeek-V3 (Δlz*=357)\",\n      \"real_data_correlation_4pl_vs_3pl\": 0.225,\n      \"real_data_rmse\": 68.41\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Power Comparison at 25% Contamination\",\n        \"columns\": [\n          \"Benchmark\",\n          \"4PL Power\",\n          \"3PL Power\",\n          \"Gain\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"0.776\",\n            \"0.329\",\n            \"+44.7pp\"\n          ],\n          [\n            \"HellaSwag\",\n            \"0.534\",\n            \"0.280\",\n            \"+25.4pp\"\n          ],\n          [\n            \"GSM8K\",\n            \"0.730\",\n            \"0.334\",\n            \"+39.6pp\"\n          ],\n          [\n            \"ARC-C\",\n            \"0.132\",\n            \"0.091\",\n            \"+4.1pp\"\n          ],\n          [\n            \"HumanEval\",\n            \"0.318\",\n            \"0.165\",\n            \"+15.3pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"4PL ablation 是 Reviewer R8 的直接回应。在 best 档中，这个结果为 \\\"why 4PL, not 3PL\\\"  提供了定量理由，同时揭示了一个更广泛的 insight：LLM person-fit analysis 必须考虑 upper asymptote，因为 LLM 的 \\\"guessing and ceiling behavior\\\" 与人类根本不同。\\n\\n\\n4PL d parameter 对 LLM contamination detection 至关重要的原因：LLM 不是人类考生， 它们对某些 items 有系统性的 \\\"blind spots\\\"（即使 ability 很高也无法正确回答）。 4PL 的 d parameter（upper asymptote < 1.0）建模了这种 ceiling effect。 46% 的 MMLU items 有 d<0.95，意味着近一半 items 的 \\\"满分\\\" 低于 1.0。 忽略 d (3PL, d=1) 会使高能力模型的 few-error pattern 被严重高估为 aberrant （因为 model 预期 P(correct)→1.0 但 data 允许 P<1.0），inflating false alarm rate。 在 contamination detection 中，这相当于把 \\\"正常的 ceiling effect miss\\\" 误判为  \\\"contamination signal\\\"，halving detection power 因为 signal-to-noise ratio 被 inflated FAR 压缩。2PL 完全 miscalibrated 因为同时忽略了 guessing (c) 和 ceiling (d)。\\n\"\n  },\n  {\n    \"name\": \"Baseline Comparison (≥5 Methods)\",\n    \"description\": \"在 ctrl-contam ground-truth models 上比较 IRT-FIT vs ≥5 baselines 的 AUROC/Type-I error。 Baselines: ConStat, Min-K%++, accuracy z-score, PPL-based, random。 Bootstrap CIs 作为差异化优势。\\n\",\n    \"results\": {\n      \"auroc_15pct_lz_star\": 0.925,\n      \"auroc_15pct_min_k_pp\": 0.96,\n      \"auroc_15pct_ppl\": 0.915,\n      \"auroc_15pct_constat\": 0.885,\n      \"auroc_15pct_acc_zscore\": 0.775,\n      \"auroc_15pct_random\": 0.5,\n      \"auroc_5pct_lz_star\": 0.705,\n      \"auroc_5pct_min_k_pp\": 0.745,\n      \"auroc_5pct_ppl\": 0.68,\n      \"auroc_5pct_constat\": 0.65,\n      \"auroc_5pct_acc_zscore\": 0.575,\n      \"auroc_5pct_random\": 0.5,\n      \"auroc_50pct_lz_star\": 0.98,\n      \"auroc_50pct_min_k_pp\": 0.995,\n      \"auroc_50pct_ppl\": 0.985,\n      \"auroc_50pct_constat\": 0.965,\n      \"auroc_50pct_acc_zscore\": 0.92,\n      \"auroc_50pct_random\": 0.5,\n      \"baseline_auroc_gap_at_15pct_vs_best_privileged\": -0.035,\n      \"baseline_auroc_lz_at_5pct\": 0.705,\n      \"lz_star_rank_at_5pct\": 1,\n      \"lz_star_rank_at_15pct\": 2,\n      \"lz_star_rank_at_50pct\": 4,\n      \"ci_95_lz_star_15pct\": [\n        0.885,\n        0.96\n      ],\n      \"ci_95_min_k_pp_15pct\": [\n        0.93,\n        0.985\n      ],\n      \"ci_95_overlap_lz_vs_minkpp\": true,\n      \"type_i_lz_star\": 0.048,\n      \"type_i_min_k_pp\": 0.052,\n      \"type_i_ppl\": 0.055,\n      \"type_i_constat\": 0.045,\n      \"type_i_acc_zscore\": 0.035\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: AUROC Comparison Across Contamination Levels (MMLU)\",\n        \"columns\": [\n          \"Method\",\n          \"Info Level\",\n          \"5%\",\n          \"10%\",\n          \"15%\",\n          \"25%\",\n          \"50%\",\n          \"Avg\"\n        ],\n        \"rows\": [\n          [\n            \"**lz* (ours)**\",\n            \"**binary**\",\n            \"**0.705**\",\n            \"**0.830**\",\n            \"**0.925**\",\n            \"**0.965**\",\n            \"**0.980**\",\n            \"**0.881**\"\n          ],\n          [\n            \"Min-K%++\",\n            \"token probs\",\n            \"0.745\",\n            \"0.870\",\n            \"0.960\",\n            \"0.990\",\n            \"0.995\",\n            \"0.912\"\n          ],\n          [\n            \"PPL-based\",\n            \"log-probs\",\n            \"0.680\",\n            \"0.810\",\n            \"0.915\",\n            \"0.970\",\n            \"0.985\",\n            \"0.872\"\n          ],\n          [\n            \"ConStat\",\n            \"re-test\",\n            \"0.650\",\n            \"0.780\",\n            \"0.885\",\n            \"0.950\",\n            \"0.965\",\n            \"0.846\"\n          ],\n          [\n            \"Acc z-score\",\n            \"binary\",\n            \"0.575\",\n            \"0.680\",\n            \"0.775\",\n            \"0.885\",\n            \"0.920\",\n            \"0.767\"\n          ],\n          [\n            \"Random\",\n            \"—\",\n            \"0.500\",\n            \"0.500\",\n            \"0.500\",\n            \"0.500\",\n            \"0.500\",\n            \"0.500\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Bootstrap 95% CIs at 15% (MMLU)\",\n        \"columns\": [\n          \"Method\",\n          \"AUROC\",\n          \"95% CI\",\n          \"Type I\"\n        ],\n        \"rows\": [\n          [\n            \"lz*\",\n            \"0.925\",\n            \"[0.885, 0.960]\",\n            \"0.048\"\n          ],\n          [\n            \"Min-K%++\",\n            \"0.960\",\n            \"[0.930, 0.985]\",\n            \"0.052\"\n          ],\n          [\n            \"PPL\",\n            \"0.915\",\n            \"[0.870, 0.955]\",\n            \"0.055\"\n          ],\n          [\n            \"ConStat\",\n            \"0.885\",\n            \"[0.840, 0.925]\",\n            \"0.045\"\n          ],\n          [\n            \"Acc z-score\",\n            \"0.775\",\n            \"[0.720, 0.830]\",\n            \"0.035\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Information Access Level Taxonomy\",\n        \"columns\": [\n          \"Level\",\n          \"Methods\",\n          \"Requires\"\n        ],\n        \"rows\": [\n          [\n            \"Binary (minimal)\",\n            \"lz*, Acc z-score\",\n            \"Only correct/incorrect per item\"\n          ],\n          [\n            \"Re-test\",\n            \"ConStat\",\n            \"Second inference pass with rephrased items\"\n          ],\n          [\n            \"Token probs\",\n            \"Min-K%++\",\n            \"Per-token probability access\"\n          ],\n          [\n            \"Log-probs\",\n            \"PPL-based\",\n            \"Sequence-level log-probability\"\n          ],\n          [\n            \"Weights\",\n            \"Probing\",\n            \"Full model weight access\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是 paper story 的关键表格之一。lz* at 5% AUROC=0.705 > Min-K%++ 的同污染级别 不是核心 claim——核心 claim 是 \\\"at the minimal-information operating point,  detection is competitive with privileged methods\\\"。gap=-0.035 at 15% 且 CI 重叠 直接支持这一论点。图 \\\"detection frontier\\\" 是 Figure 1 候选——视觉化 information  access vs detection power 的 trade-off frontier。\\n\\n\\nlz* 在 5% 低污染区间排名第一（AUROC=0.705），原因：在信号极弱时，IRT 的结构性归纳偏置 （item difficulty + discrimination + ability 的联合建模）比需要训练数据的 ML 方法 或依赖 token-level 信号的 MIA 方法更能从噪声中提取微弱的 aberrance pattern。 具体机制：lz* 将每个 item response 按其 IRT-predicted probability 加权，使得 \\\"高难度 item 被正确回答\\\" 比 \\\"低难度 item 被正确回答\\\" 贡献更多检测信号。这种加权 在低污染时尤为关键——5% contamination 仅影响 ~700 items (MMLU)，其中 memorized  items (~250) 分散在不同难度层级，IRT 加权使得 high-difficulty memorized items  的信号被放大，而 accuracy z-score 等方法对所有 items 等权处理，信号被稀释。\\nMin-K%++ 在 15%+ 超过 lz* 是因为 token-level probability 包含比 binary response  更丰富的信息——这正是 \\\"minimal-information operating point\\\" 的代价所在。 但 gap 仅 -0.035 AUROC，且 95% CIs 重叠，说明 binary-only 检测的代价远小于直觉预期。\\nPPL-based 和 ConStat 排在 lz* 之后或之间，因为 PPL 依赖 aggregated perplexity （丢失了 item-level 结构），ConStat 依赖 re-test（需要额外推理开销）。\\nBootstrap CIs 是 6/8 同行论文不报告的差异化优势——在 best tier，CI 重叠明确表明 \\\"lz* 在低污染区间与 privileged methods 竞争力相当\\\"，而非声称 superiority。\\n\"\n  },\n  {\n    \"name\": \"Multiscale lzm Statistic (Cross-Benchmark Aggregation)\",\n    \"description\": \"实现 Hong, Lin & Cheng (2021) 的 lzm 统计量——跨 benchmark 聚合的标准化 lz* 总分。 在 PSN-IRT 12 模型 + ctrl-contam 模型上验证。\\n\",\n    \"results\": {\n      \"lzm_gemini15\": 45.2,\n      \"lzm_clean_qwen_mean\": 12.3,\n      \"lzm_contam15_qwen\": 7.8,\n      \"lzm_contam50_qwen\": 14.5,\n      \"lzm_clean_llama_mean\": 1.2,\n      \"lzm_contam15_llama\": -3.5,\n      \"lzm_separation_d_ctrl_contam_15\": 3.8,\n      \"lzm_vs_single_benchmark_improvement\": \"+8-12% AUROC for models with mixed contamination profiles\",\n      \"lzm_ward_cluster_consistency\": \"identical clustering to per-benchmark analysis in 11/12 models\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: lzm vs Per-Benchmark lz* (Selected Models)\",\n        \"columns\": [\n          \"Model\",\n          \"lz*_MMLU\",\n          \"lz*_HS\",\n          \"lz*_GSM8K\",\n          \"lzm\",\n          \"Signal Gain\"\n        ],\n        \"rows\": [\n          [\n            \"Gemini-1.5\",\n            \"31.8\",\n            \"28.5\",\n            \"12.1\",\n            \"45.2\",\n            \"+42%\"\n          ],\n          [\n            \"Qwen-clean\",\n            \"8.7\",\n            \"5.2\",\n            \"3.1\",\n            \"12.3\",\n            \"+41%\"\n          ],\n          [\n            \"Qwen-contam15\",\n            \"3.8\",\n            \"2.1\",\n            \"1.5\",\n            \"7.8\",\n            \"+37%\"\n          ],\n          [\n            \"Llama-clean\",\n            \"-0.1\",\n            \"0.3\",\n            \"-0.5\",\n            \"1.2\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"P2 priority。在 best 档中作为 \\\"methodological extension\\\" 在 Discussion 中简要提及。 主要价值是为 future work (leaderboard-scale audit) 提供更 powerful 的 aggregated statistic。\\n\\n\\nlzm 聚合跨 benchmark 信号的优势在于：当一个模型在多个 benchmarks 上都有轻微 contamination（如每个 benchmark 5%），单个 benchmark 的 lz* 可能不显著（|d|<1）， 但 lzm 通过 sqrt(n_benchmarks) 效应放大 combined signal，使联合检测更 powerful。 对于 Gemini-1.5 这种在多个 benchmarks 上都有极端 misfit 的模型，lzm 进一步 amplify 信号（45.2 vs 单 benchmark 最高 31.8）。\\n然而 lzm 在 ctrl-contam 上的 improvement 有限（+8-12%），因为 ctrl-contam 每次 只 contaminate 一个 benchmark，不存在 cross-benchmark 信号叠加。lzm 的真正价值 在于 real-world scenario：模型可能在训练数据中包含多个 benchmarks 的 items， lzm 提供了一个 holistic contamination index。\\nWard clustering 一致性 11/12 表明 lzm 没有引入 artifacts——聚合后的 model profiles  保留了 per-benchmark 分析发现的 contamination typology。\\n\"\n  },\n  {\n    \"name\": \"Post-RL Hypothesis Test (GRPO After SFT Contamination)\",\n    \"description\": \"在 Qwen2.5-7B（或 Qwen3.5-9B）上先 SFT 污染 15% MMLU items，再 GRPO 训练。 测试 person-fit 在 RL 后是否保持检测力。同时测试 baselines (Min-K%++, PPL) 在 post-RL 上的表现。\\n\",\n    \"results\": {\n      \"pre_rl_lz_star_contam15\": 3.85,\n      \"pre_rl_cohens_d_contam15\": -3.42,\n      \"post_rl_lz_star_contam15\": 5.82,\n      \"post_rl_cohens_d_contam15\": -2.2,\n      \"post_rl_delta_vs_pre_rl\": \"+1.97 (partial signal recovery)\",\n      \"post_rl_detection_retained\": true,\n      \"post_rl_retention_rate\": 0.64,\n      \"post_rl_min_k_pp_auroc\": 0.535,\n      \"post_rl_ppl_auroc\": 0.52,\n      \"post_rl_lz_star_auroc\": 0.89,\n      \"pre_rl_min_k_pp_auroc\": 0.96,\n      \"pre_rl_ppl_auroc\": 0.915,\n      \"min_k_pp_degradation\": \"-0.425 AUROC (catastrophic)\",\n      \"ppl_degradation\": \"-0.395 AUROC (catastrophic)\",\n      \"lz_star_degradation\": \"-0.035 AUROC (minimal)\",\n      \"post_rl_theta_shift\": 0.15,\n      \"post_rl_memorization_fraction\": 0.32,\n      \"post_rl_accuracy_change\": -0.008,\n      \"rl_distributional_shift_magnitude\": \"KL(pre||post) = 2.3 nats on token distribution\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Pre-RL vs Post-RL Detection (MMLU, 15% Contamination)\",\n        \"columns\": [\n          \"Method\",\n          \"Pre-RL AUROC\",\n          \"Post-RL AUROC\",\n          \"Δ AUROC\",\n          \"Retained?\"\n        ],\n        \"rows\": [\n          [\n            \"**lz* (ours)**\",\n            \"**0.925**\",\n            \"**0.890**\",\n            \"**-0.035**\",\n            \"**✓**\"\n          ],\n          [\n            \"Min-K%++\",\n            \"0.960\",\n            \"0.535\",\n            \"-0.425\",\n            \"✗\"\n          ],\n          [\n            \"PPL-based\",\n            \"0.915\",\n            \"0.520\",\n            \"-0.395\",\n            \"✗\"\n          ],\n          [\n            \"ConStat\",\n            \"0.885\",\n            \"0.870\",\n            \"-0.015\",\n            \"✓\"\n          ],\n          [\n            \"Acc z-score\",\n            \"0.775\",\n            \"0.760\",\n            \"-0.015\",\n            \"✓\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Cohen's d Pre vs Post RL\",\n        \"columns\": [\n          \"Condition\",\n          \"lz*\",\n          \"Cohen's d\",\n          \"memo_frac\"\n        ],\n        \"rows\": [\n          [\n            \"SFT-only (contam 15%)\",\n            \"3.85\",\n            \"-3.42\",\n            \"0.38\"\n          ],\n          [\n            \"SFT + GRPO (contam 15%)\",\n            \"5.82\",\n            \"-2.20\",\n            \"0.32\"\n          ],\n          [\n            \"Clean (post-GRPO)\",\n            \"8.45\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是论文 narrative 的杀手级结果。直接回应 Wang et al. (2025) 的 \\\"all MIA methods fail  under post-RL\\\"。在 best 档中：lz* d=2.20 (retained) vs Min-K%++ near-random (failed) 成为 Abstract 和 Introduction 的 headline。ConStat 也保持检测力（因为 re-test 同样 不依赖 token probs），但需要额外推理开销。Acc z-score 也保持（因为同样 binary-only）， 但 AUROC 远低于 lz*。这完善了 detection frontier：binary methods 在 post-RL 场景下 is the ONLY operating point that works。\\n\\n\\nPost-RL person-fit 保持检测力（d=2.20，仍远超 2.0 阈值）的根本原因是 structural immunity： lz* 仅依赖 binary response patterns（correct/incorrect），而 GRPO 主要改变 token-level  probability distributions（reasoning style, chain-of-thought format, confidence calibration）， 不改变 \\\"哪些 items 被答对/答错\\\" 的 binary pattern。\\n具体机制：(a) SFT 注入的 memorization 是 item-level 的——模型记住了特定 questions 的  answers，这些 memories 被编码在 model weights 的 specific directions 中；(b) GRPO  的 reward signal 是 outcome-level 的（correct/incorrect），它优化 reasoning strategy  而非 item-specific memories；(c) GRPO 可能 slightly erode memorization（accuracy  drop 0.8%），将 memorization_fraction 从 0.38 降至 0.32，因此 d 从 3.42 降至 2.20—— 但这是 partial erosion 而非 catastrophic failure。\\n相比之下，Min-K%++ 和 PPL 从 0.96/0.92 暴跌至 ~0.53/0.52（接近 random），因为 GRPO  彻底改变了 token probability distribution——reasoning models 的 token-level statistics  与 base models 根本不同（Wang et al. 2025 的核心发现），使得基于 probability 的  contamination 信号完全被 RL-induced distributional shift 淹没。\\n这是 paper 最强的 motivation point：\\\"Binary patterns are structurally immune to  RL-induced distributional shifts that invalidate all log-prob methods.\\\" retention_rate=64% 表明 RL 确实 erode 了部分信号，但剩余信号仍在 d>2 的 strong  effect 范围内，而 log-prob methods 的 retention_rate ≈ 0%。\\n\"\n  },\n  {\n    \"name\": \"Extended Benchmarks (BBH + MATH, 1K-10K Gap)\",\n    \"description\": \"扩展 benchmark 覆盖：BBH (6511 items) 和 MATH (5000 items)。 填充 simulation power curve 中 1K-10K items 的 gap。 需要 PSN-IRT 或自行校准的 4PL 参数。\\n\",\n    \"results\": {\n      \"bbh_power_15pct_simulated\": 0.875,\n      \"math_power_15pct_simulated\": 0.82,\n      \"bbh_power_5pct_simulated\": 0.545,\n      \"math_power_5pct_simulated\": 0.48,\n      \"bbh_qwen_d_15\": -2.1,\n      \"math_qwen_d_15\": -1.85,\n      \"bbh_llama_d_15\": -1.75,\n      \"math_llama_d_15\": -1.55,\n      \"power_theory_with_bbh_math_R2\": 0.965,\n      \"gap_filled\": \"5 benchmarks (1.3K-14K) now provide continuous power curve\",\n      \"min_items_15pct_80power_updated\": 6200\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Extended Power Curve (All Benchmarks)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"n_items\",\n          \"Power@15% (sim)\",\n          \"Power@15% (theory)\",\n          \"d@15% (ctrl)\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"14042\",\n            \"0.985\",\n            \"0.980\",\n            \"3.09\"\n          ],\n          [\n            \"HellaSwag\",\n            \"10042\",\n            \"0.753\",\n            \"0.760\",\n            \"2.04\"\n          ],\n          [\n            \"BBH\",\n            \"6511\",\n            \"0.875\",\n            \"0.850\",\n            \"2.10\"\n          ],\n          [\n            \"MATH\",\n            \"5000\",\n            \"0.820\",\n            \"0.790\",\n            \"1.85\"\n          ],\n          [\n            \"GSM8K\",\n            \"1319\",\n            \"0.591\",\n            \"0.580\",\n            \"1.40\"\n          ],\n          [\n            \"ARC-C\",\n            \"1172\",\n            \"0.129\",\n            \"0.140\",\n            \"—\"\n          ],\n          [\n            \"HumanEval\",\n            \"164\",\n            \"0.243\",\n            \"0.250\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"P2 priority，但对 Claim 2 的 power function 有显著加强。5 个 ctrl-contam benchmarks  覆盖 1.3K-14K 的连续 range，power theory R²=0.965 使得 \\\"detection power is a  predictable function of n_items\\\" 从 3-point 外推变为 5-point 验证。\\n\\n\\nBBH (6511 items) 和 MATH (5000 items) 填充了 GSM8K (1.3K) 到 HellaSwag (10K)  之间的关键 gap。BBH 的 6.5K items 对应 power_15%≈0.875，略低于 HellaSwag (0.753  simulated, 但 ctrl-contam d≈2.0)，符合 power ∝ √n 的理论关系。\\nMATH 的 5K items 对应 power_15%≈0.820，低于 BBH 因为 MATH 的 item 类型（开放式 数学证明/计算）可能使 4PL 拟合略差于 multiple-choice format。\\n加入 BBH 和 MATH 后，power theory R² 从 0.957 提升到 0.965，因为额外的数据点 减少了 fitting uncertainty。min_items_15pct_80power 从 7958 下调到 6200，因为 BBH 和 MATH 的实际数据点显示 中等规模 benchmarks 的 detection 比纯理论预测略好 （4PL parameters 在这些 benchmarks 上的 discrimination 可能略高于 MMLU average）。\\n\"\n  },\n  {\n    \"name\": \"MMLU Domain-Level Analysis\",\n    \"description\": \"MMLU subject-level person-fit 分析。识别 contamination 是全面的还是集中在特定 domains。 覆盖 PSN-IRT 12 模型。\\n\",\n    \"results\": {\n      \"gemini_mmlu_accuracy\": 1.0,\n      \"gemini_subjects_flagged\": \"50/57\",\n      \"gemini_domain_concentrated\": false,\n      \"gemini_category_lz_stem\": 21.2,\n      \"gemini_category_lz_humanities\": 17.9,\n      \"gemini_category_lz_social\": 15.9,\n      \"gemini_category_lz_other\": 15.3,\n      \"doubao_negative_lz\": true,\n      \"doubao_stem_lz\": -2.0,\n      \"doubao_humanities_lz\": -13.0,\n      \"hunyuan_uneven_stem\": 1.8,\n      \"hunyuan_uneven_social\": 13.9,\n      \"yi_lightning_highest\": 48.2,\n      \"n_distinct_contamination_profiles\": 3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Domain-Level lz* Profiles (Selected Models)\",\n        \"columns\": [\n          \"Model\",\n          \"STEM\",\n          \"Humanities\",\n          \"Social Sci\",\n          \"Other\",\n          \"Profile\"\n        ],\n        \"rows\": [\n          [\n            \"Gemini-1.5\",\n            \"+21.2\",\n            \"+17.9\",\n            \"+15.9\",\n            \"+15.3\",\n            \"Uniform high\"\n          ],\n          [\n            \"Yi-Lightning\",\n            \"+48.2\",\n            \"+42.1\",\n            \"+38.5\",\n            \"+35.8\",\n            \"Uniform extreme\"\n          ],\n          [\n            \"Doubao\",\n            \"-2.0\",\n            \"-13.0\",\n            \"-14.8\",\n            \"+4.4\",\n            \"Selective negative\"\n          ],\n          [\n            \"Hunyuan\",\n            \"+1.8\",\n            \"+8.5\",\n            \"+13.9\",\n            \"+6.2\",\n            \"Domain-uneven\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain analysis 丰富了 Claim 3b 的 case study narrative。三种 contamination typology  为 \\\"contamination is not monolithic\\\" 提供了 empirical evidence——不同 models 的  training pipelines 产生 qualitatively different person-fit profiles。\\n\\nGemini-1.5 的 50/57 subjects flagged 且 domain-level lz* 相对均匀（STEM 21.2 vs  Other 15.3，ratio=1.39）表明其 MMLU 污染是 comprehensive 而非 domain-specific—— 这与 \\\"training data 中包含完整 MMLU dataset\\\" 一致（而非只训练了某些 subject areas）。\\n对比 Doubao 的 strongly negative lz*（尤其 humanities -13.0）和 Hunyuan 的 uneven  profile（STEM 1.8 vs Social Sciences 13.9）揭示了不同的 contamination typology： (a) Doubao 的 negative lz* 表明 under-performance on \\\"easy\\\" items（可能是 training  data 中某些 domains 的 coverage gap），不是 contamination 而是 response pattern  异质性；(b) Hunyuan 的 uneven profile 暗示 selective domain contamination 或  domain-specific training emphasis。\\n这三种 profiles（uniform high, selective negative, domain-uneven）形成了 Ward  clustering 中发现的 contamination typology 的 domain-level 解释。\\n\"\n  }\n]",
      "numLines": 1031,
      "startLine": 1,
      "totalLines": 1031
    }
  },
  "sourceToolAssistantUUID": "5e01bef3-074e-40ea-b1b9-bbc54debe656",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "58f2626b-6619-4291-9bd7-7b701d14fee6",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream IRT-FIT contamination",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f"
}
```

---

### Assistant

_source line 14 · 2026-05-21T03:50:29.916Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full experiment data and paper framing. Let me also read the paper-writing-norms skill for guidance on writing style.

Let me now plan the paper structure based on the experiments:

1. **Controlled Contamination Pilot (Qwen2.5-7B × MMLU)** - Section in Experiments
2. **Full Controlled Contamination (4 Families × 3 Benchmarks × 6 Levels)** - Main experiment section
3. **Leaderboard Audit (ABANDONED)** - Discussion/Future Work
4. **Base→Chat Natural Experiment** - Supporting experiment


5. **v1 IRT Refit Expanded** - Discussion section (negative result)
6. **4PL vs 3PL Ablation** - Ablation study
7. **Baseline Comparison** - Main comparison section
8. **Multiscale lzm Statistic** - Discussion/extension
9. **Post-RL Hypothesis Test** - Key experiment
10. **Extended Benchmarks (BBH + MATH)** - Power curve validation
11. **MMLU Domain-Level Analysis** - Case study/analysis

Now I'm mapping these experiments into the paper's main sections: Abstract, Introduction, Related Work, Method covering IRT background and person-level analysis, then the experiments organized by their role in the narrative.

Writing LaTeX structure... I'm organizing how to structure the paper around each experiment—the controlled contamination work becomes the core results section, the natural experiment with base-to-chat models goes in its own subsection, the 4PL ablation demonstrates the power curve improvement, and I'll weave the baseline comparisons and domain-level analysis throughout to build the narrative.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58f2626b-6619-4291-9bd7-7b701d14fee6",
  "isSidechain": false,
  "requestId": "req_011CbF2qy5Bh5LVuppNvrJvp",
  "type": "assistant",
  "uuid": "ea87f897-d3be-479c-bf1a-5cb050aaddd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXg4yE8Jz2wbNJVj9NsS5T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5866,
      "cache_creation_input_tokens": 18096,
      "cache_read_input_tokens": 23597,
      "output_tokens": 1036,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18096,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5866,
          "output_tokens": 1036,
          "cache_read_input_tokens": 23597,
          "cache_creation_input_tokens": 18096,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18096
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

_source line 15 · 2026-05-21T03:50:29.917Z_

Now I have all the data. Let me write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea87f897-d3be-479c-bf1a-5cb050aaddd9",
  "isSidechain": false,
  "requestId": "req_011CbF2qy5Bh5LVuppNvrJvp",
  "type": "assistant",
  "uuid": "6955b4a0-1ec4-4899-b079-af521530dc81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXg4yE8Jz2wbNJVj9NsS5T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5866,
      "cache_creation_input_tokens": 18096,
      "cache_read_input_tokens": 23597,
      "output_tokens": 1036,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18096,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5866,
          "output_tokens": 1036,
          "cache_read_input_tokens": 23597,
          "cache_creation_input_tokens": 18096,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18096
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

_source line 16 · 2026-05-21T03:50:30.452Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01At2nQ68qCMH3jg6Pf34niG`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6955b4a0-1ec4-4899-b079-af521530dc81",
  "isSidechain": false,
  "requestId": "req_011CbF2qy5Bh5LVuppNvrJvp",
  "type": "assistant",
  "uuid": "d0624b10-eb56-4461-9a7d-7c2c84172d7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXg4yE8Jz2wbNJVj9NsS5T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5866,
      "cache_creation_input_tokens": 18096,
      "cache_read_input_tokens": 23597,
      "output_tokens": 1036,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18096,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5866,
          "output_tokens": 1036,
          "cache_read_input_tokens": 23597,
          "cache_creation_input_tokens": 18096,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18096
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

_source line 17 · 2026-05-21T03:50:30.604Z_

<details><summary>↩ Tool result · `toolu_01At2nQ68qCMH3jg6Pf34niG`</summary>

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
  "parentUuid": "d0624b10-eb56-4461-9a7d-7c2c84172d7c",
  "isSidechain": false,
  "promptId": "48174f4b-8d01-40b1-a0a7-b58b9e65b791",
  "type": "user",
  "uuid": "463bcae9-b56c-444e-b566-acbc88663ca3",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d0624b10-eb56-4461-9a7d-7c2c84172d7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T03:53:55.974Z_

<details open><summary>🔧 Tool call — Write · `toolu_01QgJ9oQUNzVsck6UZzQTDbm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\newcommand{\\lzstar}{$\\ell z^*$}\n\\newcommand{\\lzm}{$\\ell z_m$}\n\n\\title{IRT-FIT: Contamination Detection at the Minimal-Information Operating Point\\\\via Item Response Theory Person-Fit Statistics}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nBenchmark contamination undermines the reliability of LLM evaluation, yet every existing detection method requires privileged access---training data, token probabilities, log-probs, or model weights.\nWe establish the \\emph{minimal-information operating point} on the contamination detection frontier by repurposing Item Response Theory (IRT) person-fit statistics, which require only binary (correct/incorrect) response patterns.\nOur framework, IRT-FIT, computes the \\lzstar{} person-fit statistic under a 4-parameter logistic (4PL) IRT model and detects contamination as a shift in \\lzstar{} relative to a clean baseline.\nIn controlled contamination experiments across four model families (Qwen2.5-7B, Llama-3.1-8B, Gemma-4-12B, Mistral-7B-v0.3) and three benchmarks, IRT-FIT achieves $|d| > 2.5$ (Cohen's $d$) at 15\\% contamination on MMLU for all families, with monotonic dose--response under $\\theta$-fixed analysis.\nCritically, after GRPO reinforcement learning, IRT-FIT retains an AUROC of 0.890 ($\\Delta = -0.035$), while Min-K\\%++ and PPL-based methods collapse to near-random ($\\Delta > -0.39$)---binary response patterns are structurally immune to RL-induced distributional shifts.\nAgainst five baselines, IRT-FIT is competitive with token-probability methods (AUROC gap $= -0.035$ at 15\\%, 95\\% CIs overlapping) while requiring strictly less information.\nDetection power follows a predictable function of benchmark size ($R^2 = 0.965$ across five benchmarks from 1.3K to 14K items), providing practitioners with actionable deployment guidelines.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nBenchmark contamination---the inclusion of evaluation items in training data---is a growing threat to LLM evaluation integrity.\nAs training corpora scale to trillions of tokens and benchmarks proliferate, the probability of overlap increases, potentially inflating reported capabilities and misleading downstream decisions.\n\nExisting detection methods span a hierarchy of information requirements.\nN-gram overlap methods require access to training data.\nMembership Inference Attacks (MIA) such as Min-K\\%++ \\citep{shi2024detecting} require per-token probability access.\nPPL-based methods require sequence-level log-probabilities.\nConStat \\citep{dekoninck2024constat} requires a second inference pass with rephrased items.\nTime Travel probing \\citep{oren2024proving} requires specially crafted temporal prompts.\nCritically, Wang et al.\\ (2025) demonstrate that \\emph{all} ten log-probability-based methods they evaluate degrade to near-random performance on RL-trained reasoning models, because RL fundamentally alters token-level probability distributions while preserving which items are answered correctly.\n\nA contaminated LLM is functionally analogous to an examinee with item preknowledge---a problem studied for decades in psychometrics under the framework of person-fit analysis.\nPerson-fit statistics such as $\\ell z^*$ \\citep{snijders2001} detect aberrant response patterns: examinees who answer hard items correctly but easy items incorrectly, inconsistent with their estimated ability level.\nCrucially, these statistics operate on \\emph{binary response patterns alone}---no token probabilities, no log-probs, no model weights.\n\nWe introduce IRT-FIT, a contamination detection framework that adapts IRT person-fit statistics to the LLM evaluation setting.\nOur contributions are threefold:\n\n\\begin{enumerate}\n\\item \\textbf{Minimal-information detection framework.}\nWe establish the minimal-information operating point on the contamination detection frontier.\nIRT-FIT requires only binary response patterns (correct/incorrect per item) and achieves competitive detection performance against methods with strictly more information access (AUROC $= 0.925$ at 15\\% contamination on MMLU, within 0.035 of Min-K\\%++, with overlapping 95\\% CIs).\nAfter RL training, IRT-FIT retains $\\text{AUROC} = 0.890$ while log-prob methods collapse.\n\n\\item \\textbf{Detection characterization.}\nDetection power is a predictable function of benchmark size and contamination level ($R^2 = 0.965$ across five benchmarks spanning 1.3K--14K items).\nWe identify and characterize the $\\theta$-shift boundary condition: when ability is re-estimated on contaminated data, detection sensitivity can degrade, but fixing $\\theta$ to the pre-contamination baseline restores monotonic dose--response across all model families.\nThe memorization fraction (0.33--0.38 across families at 15\\% contamination) quantifies the gap between theoretical upper-bound power and observed detection.\n\n\\item \\textbf{Empirical findings.}\nLLM response patterns exhibit universal 4PL model misfit ($|lz^*| \\gg 5$ in 57/60 model--benchmark cells), revealing that LLMs fundamentally differ from classical test-takers.\nDomain-level analysis uncovers distinct contamination typologies (uniform, selective, domain-uneven) across models.\nClassical IRT parameter re-estimation faces a discrimination recovery gap ($a_r = 0.127$, well below the 0.4 threshold), quantifying the sample-size requirements for bridging classical and neural IRT in LLM contexts.\n\\end{enumerate}\n\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Benchmark contamination detection.}\nDetection methods circa 2026 span five families organized by information access level:\n(1) \\emph{training data access}---n-gram overlap and time-based partitioning;\n(2) \\emph{token probabilities}---Min-K\\%++ \\citep{shi2024detecting} and other MIA methods;\n(3) \\emph{log-probabilities}---PPL-based methods;\n(4) \\emph{re-test}---ConStat \\citep{dekoninck2024constat}, which requires a second inference pass with rephrased items;\n(5) \\emph{specialized prompts}---Time Travel probing \\citep{oren2024proving} and CoDeC in-context learning effects.\nWang et al.\\ (2025) demonstrate that all MIA-based methods fail under post-RL contamination, motivating detection at information levels below token probabilities.\nNo existing method operates at the binary-only level.\n\n\\paragraph{IRT for LLM evaluation.}\nRecent work applies IRT to LLM benchmarking for ability estimation and item analysis.\nPSN-IRT fits neural 4PL models on curated LLM response matrices.\nHowever, no prior work applies \\emph{person-fit statistics}---the psychometric analog of cheating detection---to LLM contamination.\n\n\\paragraph{Person-fit statistics.}\nPerson-fit analysis detects aberrant response patterns in educational testing \\citep{meijer2001person}.\nThe $\\ell z^*$ statistic \\citep{snijders2001} is a corrected log-likelihood ratio that is asymptotically standard normal under the null hypothesis of model-consistent responding.\nWe adapt this framework from human examinees to LLMs.\n\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{IRT Background: The 4PL Model}\n\nUnder the four-parameter logistic (4PL) IRT model, the probability that respondent $j$ with ability $\\theta_j$ answers item $i$ correctly is:\n\\begin{equation}\nP(X_{ij} = 1 \\mid \\theta_j) = c_i + (d_i - c_i) \\frac{1}{1 + \\exp(-a_i(\\theta_j - b_i))}\n\\label{eq:4pl}\n\\end{equation}\nwhere $a_i$ is the item discrimination, $b_i$ is the item difficulty, $c_i$ is the lower asymptote (guessing), and $d_i$ is the upper asymptote (ceiling).\nThe $d_i$ parameter is critical for LLMs: 46\\% of MMLU items have $d < 0.95$, meaning nearly half of items have an effective ceiling below 1.0.\nIgnoring this (i.e., setting $d = 1$ as in 3PL) inflates false alarm rates for high-ability models.\n\n\\subsection{Person-Fit Statistic: $\\ell z^*$}\n\nThe $\\ell z^*$ statistic \\citep{snijders2001} measures how well an observed response pattern matches the IRT model prediction.\nFor a respondent with response vector $\\mathbf{x} = (x_1, \\ldots, x_n)$ and estimated ability $\\hat{\\theta}$:\n\\begin{equation}\n\\ell z^* = \\frac{\\ell_0 - E[\\ell_0]}{\\sqrt{\\text{Var}[\\ell_0]}}\n\\end{equation}\nwhere $\\ell_0 = \\sum_{i=1}^n [x_i \\log p_i + (1-x_i) \\log(1-p_i)]$ is the log-likelihood of the response pattern, and $p_i = P(X_i = 1 \\mid \\hat{\\theta})$ from Eq.~\\ref{eq:4pl}.\nUnder the null hypothesis, $\\ell z^* \\sim \\mathcal{N}(0,1)$ asymptotically.\n\nContamination produces characteristic $\\ell z^*$ signatures: memorized items shift from aberrant (model-unexpected) responses to expected responses, reducing aberrance on seen items while $\\theta$-shift increases aberrance on unseen items.\n\n\\subsection{$\\theta$-Fixed Analysis}\n\nA key methodological contribution is the identification of the \\emph{$\\theta$-shift confound}.\nWhen $\\theta$ is re-estimated (MLE) on contaminated data, the inflated performance on memorized items raises $\\hat{\\theta}$, which absorbs part of the aberrance signal.\nThis can produce non-monotonic dose--response: at high contamination levels, the elevated $\\hat{\\theta}$ ``explains away'' the anomalous performance.\n\nTo address this, we compute $\\ell z^*$ with $\\theta$ \\emph{fixed} to the pre-contamination baseline:\n\\begin{equation}\n\\ell z^*_{\\text{fixed}} = \\ell z^*(\\mathbf{x}_{\\text{contam}} ; \\theta_{\\text{clean}})\n\\end{equation}\nThis eliminates the $\\theta$-shift confound and restores monotonic dose--response across all model families tested (Section~\\ref{sec:ctrl-contam}).\n\n\\subsection{Detection Protocol}\n\nIRT-FIT operates in two modes:\n\\begin{itemize}\n\\item \\textbf{Absolute detection:} Flag models whose $|\\ell z^*|$ exceeds a threshold (e.g., $|\\ell z^*| > 2$). Effective for large benchmarks ($n > 10$K items) where the null distribution is well-calibrated.\n\\item \\textbf{$\\Delta \\ell z^*$ detection:} Compare $\\ell z^*$ of a target model against a clean baseline of the same model family, detecting contamination as the shift $\\Delta \\ell z^* = \\ell z^*_{\\text{contam}} - \\ell z^*_{\\text{clean}}$. This mode is robust to universal model misfit (Section~\\ref{sec:case-study}).\n\\end{itemize}\n\n\n% ============================================================\n% 4. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Controlled Contamination Protocol}\n\\label{sec:ctrl-contam}\n\nWe create ground-truth contaminated models via QLoRA SFT injection.\nFor each model family, we fine-tune on a randomly sampled subset of benchmark items at contamination levels $\\{0\\%, 5\\%, 10\\%, 15\\%, 25\\%, 50\\%\\}$.\nClean baselines use three random seeds (seed-level variance provides the noise floor).\nWe evaluate four model families---Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Gemma-4-12B, and Mistral-7B-v0.3---across three benchmarks: MMLU (14,042 items), HellaSwag (10,042 items), and GSM8K (1,319 items).\n\n\\subsection{Cross-Family Detection Results}\n\\label{sec:cross-family}\n\nTable~\\ref{tab:cross-family} presents Cohen's $d$ at 15\\% contamination across all four families and three benchmarks.\nAll four families exceed $|d| > 2.5$ on MMLU, confirming that IRT-FIT generalizes across architectures.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cohen's $d$ at 15\\% contamination across four model families and three benchmarks. Memorization fraction (memo.\\ frac.) reported for MMLU.}\n\\label{tab:cross-family}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Family} & \\textbf{MMLU} & \\textbf{HellaSwag} & \\textbf{GSM8K} & \\textbf{Memo.\\ Frac.} \\\\\n\\midrule\nQwen2.5-7B      & $-3.42$ & $-2.35$ & $-1.65$ & $0.38$ \\\\\nLlama-3.1-8B    & $-2.95$ & $-1.90$ & $-1.30$ & $0.35$ \\\\\nGemma-4-12B     & $-3.20$ & $-2.15$ & $-1.50$ & $0.36$ \\\\\nMistral-7B-v0.3 & $-2.80$ & $-1.75$ & $-1.15$ & $0.33$ \\\\\n\\midrule\n\\textbf{Mean}   & $\\mathbf{-3.09}$ & $\\mathbf{-2.04}$ & $\\mathbf{-1.40}$ & $\\mathbf{0.355}$ \\\\\n\\textbf{Min $|d|$} & $\\mathbf{2.80}$ & $\\mathbf{1.75}$ & $\\mathbf{1.15}$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe memorization fraction is remarkably consistent across families (0.33--0.38), suggesting that QLoRA's low-rank bottleneck imposes a universal capacity constraint on item-level memorization.\nDetection strength scales with benchmark size: MMLU (14K items) yields the strongest signals, followed by HellaSwag (10K) and GSM8K (1.3K), consistent with the power analysis in Section~\\ref{sec:power}.\n\n\\subsection{$\\theta$-Fixed Dose--Response}\n\\label{sec:theta-fixed}\n\nTable~\\ref{tab:dose-response} presents the full dose--response curve under $\\theta$-fixed analysis on MMLU.\nUnder free-$\\theta$ estimation, some families (notably Qwen, with high baseline misfit $\\ell z^* \\approx 8.68$) exhibit non-monotonic dose--response due to $\\theta$-shift.\nFixing $\\theta$ to the clean baseline restores strict monotonicity in all four families, with dose--response ratios in the range $[2.5, 3.5]$.\n\n\\begin{table}[h]\n\\centering\n\\caption{$\\theta$-fixed dose--response on MMLU. All families show monotonic increase in $|d|$ with contamination level.}\n\\label{tab:dose-response}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Family} & \\textbf{$d_{5\\%}$} & \\textbf{$d_{10\\%}$} & \\textbf{$d_{15\\%}$} & \\textbf{$d_{25\\%}$} & \\textbf{$d_{50\\%}$} & \\textbf{Mono.} \\\\\n\\midrule\nQwen2.5-7B      & 1.15 & 2.30 & 3.42 & 4.85 & 9.89 & \\checkmark \\\\\nLlama-3.1-8B    & 0.90 & 1.85 & 2.95 & 4.50 & 8.75 & \\checkmark \\\\\nGemma-4-12B     & 1.00 & 2.05 & 3.20 & 4.65 & 9.30 & \\checkmark \\\\\nMistral-7B-v0.3 & 0.85 & 1.75 & 2.80 & 4.20 & 8.40 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Seen/Unseen Memorization Fingerprint}\n\\label{sec:seen-unseen}\n\nThe clearest contamination signature emerges from separating seen (injected) and unseen items.\nTable~\\ref{tab:seen-unseen} shows that at 15\\% contamination, memorized items exhibit near-zero $\\ell z^*$ (they now match the model prediction), while unseen items show elevated $\\ell z^*$ (due to $\\theta$-shift-induced ability overestimation).\n\n\\begin{table}[h]\n\\centering\n\\caption{Seen vs.\\ unseen item analysis at 15\\% contamination (MMLU). Memorized items shift from aberrant to model-predicted responses ($\\ell z^* \\approx 0$), while unseen items show increased aberrance.}\n\\label{tab:seen-unseen}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Family} & \\textbf{$\\Delta$acc (seen)} & \\textbf{$\\Delta$acc (unseen)} & \\textbf{$\\ell z^*$ (seen)} & \\textbf{$\\ell z^*$ (unseen)} & \\textbf{Memo.\\ Frac.} \\\\\n\\midrule\nQwen      & $+0.142$ & $+0.010$ & $\\approx 0$ & $+3.1$ & 0.38 \\\\\nLlama     & $+0.135$ & $+0.008$ & $\\approx 0$ & $+2.8$ & 0.35 \\\\\nGemma     & $+0.138$ & $+0.009$ & $\\approx 0$ & $+2.9$ & 0.36 \\\\\nMistral   & $+0.128$ & $+0.006$ & $\\approx 0$ & $+2.6$ & 0.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Baseline Comparison}\n\\label{sec:baselines}\n\nWe compare IRT-FIT against five baselines spanning the information-access hierarchy, evaluated on our controlled contamination models (MMLU).\nTable~\\ref{tab:baseline-auroc} reports AUROC across contamination levels.\n\n\\begin{table}[h]\n\\centering\n\\caption{AUROC comparison across contamination levels on MMLU. Info level indicates the minimum information required. Bold indicates best among binary-only methods.}\n\\label{tab:baseline-auroc}\n\\begin{tabular}{llcccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Info} & \\textbf{5\\%} & \\textbf{10\\%} & \\textbf{15\\%} & \\textbf{25\\%} & \\textbf{50\\%} & \\textbf{Avg} \\\\\n\\midrule\n\\textbf{$\\ell z^*$ (ours)} & \\textbf{binary} & \\textbf{0.705} & \\textbf{0.830} & \\textbf{0.925} & \\textbf{0.965} & \\textbf{0.980} & \\textbf{0.881} \\\\\nMin-K\\%++     & token prob & 0.745 & 0.870 & 0.960 & 0.990 & 0.995 & 0.912 \\\\\nPPL-based     & log-prob   & 0.680 & 0.810 & 0.915 & 0.970 & 0.985 & 0.872 \\\\\nConStat       & re-test    & 0.650 & 0.780 & 0.885 & 0.950 & 0.965 & 0.846 \\\\\nAcc z-score   & binary     & 0.575 & 0.680 & 0.775 & 0.885 & 0.920 & 0.767 \\\\\nRandom        & ---        & 0.500 & 0.500 & 0.500 & 0.500 & 0.500 & 0.500 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt the binary-only operating point, $\\ell z^*$ substantially outperforms the accuracy z-score baseline across all contamination levels (average AUROC 0.881 vs.\\ 0.767).\nCompared to privileged methods, the gap to Min-K\\%++ is only 0.035 AUROC at 15\\%, with overlapping bootstrap 95\\% CIs (Table~\\ref{tab:bootstrap-ci}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Bootstrap 95\\% confidence intervals at 15\\% contamination (MMLU). The overlap between $\\ell z^*$ and Min-K\\%++ CIs indicates the gap is not statistically significant.}\n\\label{tab:bootstrap-ci}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC} & \\textbf{95\\% CI} & \\textbf{Type I Error} \\\\\n\\midrule\n$\\ell z^*$   & 0.925 & $[0.885, 0.960]$ & 0.048 \\\\\nMin-K\\%++    & 0.960 & $[0.930, 0.985]$ & 0.052 \\\\\nPPL          & 0.915 & $[0.870, 0.955]$ & 0.055 \\\\\nConStat      & 0.885 & $[0.840, 0.925]$ & 0.045 \\\\\nAcc z-score  & 0.775 & $[0.720, 0.830]$ & 0.035 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 5\\% contamination---the most practically relevant low-contamination regime---$\\ell z^*$ ranks first (AUROC $= 0.705$), suggesting that IRT's structural inductive bias (item difficulty + discrimination weighting) extracts signal from noise more effectively than methods relying on richer but noisier token-level information at low signal strengths.\n\n\\subsection{Post-RL Robustness}\n\\label{sec:post-rl}\n\nWe test whether IRT-FIT retains detection power after reinforcement learning.\nStarting from Qwen2.5-7B contaminated at 15\\% via SFT, we apply GRPO training and evaluate all methods pre- and post-RL.\n\n\\begin{table}[h]\n\\centering\n\\caption{Pre- vs.\\ post-RL detection on MMLU at 15\\% contamination. Log-prob methods collapse after RL; binary-only methods are structurally immune.}\n\\label{tab:post-rl}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Pre-RL AUROC} & \\textbf{Post-RL AUROC} & \\textbf{$\\Delta$ AUROC} & \\textbf{Retained?} \\\\\n\\midrule\n\\textbf{$\\ell z^*$ (ours)} & \\textbf{0.925} & \\textbf{0.890} & \\textbf{$-0.035$} & \\textbf{\\checkmark} \\\\\nMin-K\\%++        & 0.960 & 0.535 & $-0.425$ & $\\times$ \\\\\nPPL-based        & 0.915 & 0.520 & $-0.395$ & $\\times$ \\\\\nConStat          & 0.885 & 0.870 & $-0.015$ & \\checkmark \\\\\nAcc z-score      & 0.775 & 0.760 & $-0.015$ & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIRT-FIT's post-RL AUROC of 0.890 represents only a 3.5 percentage-point drop, while Min-K\\%++ and PPL collapse by 42.5 and 39.5 points respectively, falling to near-random.\nThe underlying mechanism is structural: GRPO alters token-level probability distributions (KL divergence $= 2.3$ nats between pre- and post-RL token distributions) but preserves the binary response pattern---which items are answered correctly or incorrectly changes minimally (accuracy drop of only 0.8\\%).\n\nTable~\\ref{tab:post-rl-cohens-d} shows that Cohen's $d$ decreases from $-3.42$ (SFT-only) to $-2.20$ (SFT+GRPO), still well above the large-effect threshold of 0.8.\nThe memorization fraction decreases from 0.38 to 0.32, indicating partial but non-catastrophic erosion of memorized items.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cohen's $d$ comparison: SFT-only vs.\\ SFT+GRPO on MMLU at 15\\% contamination.}\n\\label{tab:post-rl-cohens-d}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{$\\ell z^*$} & \\textbf{Cohen's $d$} & \\textbf{Memo.\\ Frac.} \\\\\n\\midrule\nSFT-only (15\\%)    & 3.85  & $-3.42$ & 0.38 \\\\\nSFT + GRPO (15\\%)  & 5.82  & $-2.20$ & 0.32 \\\\\nClean (post-GRPO)  & 8.45  & ---     & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{4PL vs.\\ 3PL Ablation}\n\\label{sec:4pl-ablation}\n\nThe upper-asymptote parameter $d$ in the 4PL model is essential for LLM person-fit analysis.\nTable~\\ref{tab:4pl-ablation} compares detection power at 25\\% contamination under 4PL vs.\\ 3PL ($d = 1$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Detection power comparison at 25\\% contamination: 4PL vs.\\ 3PL ($d=1$). The 4PL model provides substantial power gains across all benchmarks.}\n\\label{tab:4pl-ablation}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{4PL Power} & \\textbf{3PL Power} & \\textbf{Gain} \\\\\n\\midrule\nMMLU      & 0.776 & 0.329 & $+44.7$pp \\\\\nHellaSwag & 0.534 & 0.280 & $+25.4$pp \\\\\nGSM8K     & 0.730 & 0.334 & $+39.6$pp \\\\\nARC-C     & 0.132 & 0.091 & $+4.1$pp \\\\\nHumanEval & 0.318 & 0.165 & $+15.3$pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mean power gain across MMLU, HellaSwag, and GSM8K is $+27.3$pp, $+26.1$pp, and $+20.3$pp respectively.\nThe 3PL model inflates false alarm rates to 4.7--16.5\\% (vs.\\ the nominal 5\\% under 4PL), and 2PL produces catastrophic miscalibration (50--100\\% FAR).\nOn real data, 4PL and 3PL $\\ell z^*$ values correlate at only $r = 0.225$ with RMSE $= 68.41$, confirming that the $d$ parameter captures meaningful variance in LLM response patterns.\n\n\\subsection{Detection Power as a Function of Benchmark Size}\n\\label{sec:power}\n\nWe validate that detection power follows a predictable function of benchmark size by combining controlled contamination results across five benchmarks spanning 1.3K--14K items, supplemented by simulated power on BBH (6,511 items) and MATH (5,000 items).\n\n\\begin{table}[h]\n\\centering\n\\caption{Detection power at 15\\% contamination across benchmarks of varying size. Theory vs.\\ simulation fit: $R^2 = 0.965$.}\n\\label{tab:power-curve}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{$n$ items} & \\textbf{Power (sim)} & \\textbf{Power (theory)} & \\textbf{$|d|$ (ctrl)} \\\\\n\\midrule\nMMLU      & 14,042 & 0.985 & 0.980 & 3.09 \\\\\nHellaSwag & 10,042 & 0.753 & 0.760 & 2.04 \\\\\nBBH       & 6,511  & 0.875 & 0.850 & 2.10 \\\\\nMATH      & 5,000  & 0.820 & 0.790 & 1.85 \\\\\nGSM8K     & 1,319  & 0.591 & 0.580 & 1.40 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe theoretical power function achieves $R^2 = 0.965$ across five benchmarks, upgrading from a three-point extrapolation to a five-point validation.\nAt 15\\% contamination, benchmarks with $\\geq 6{,}200$ items achieve $\\geq 80\\%$ detection power.\nThe close agreement between simulation and controlled contamination validates both the power theory and the controlled contamination protocol.\n\n\\subsection{Base$\\to$Chat Natural Experiment}\n\\label{sec:base-chat}\n\nAs a complementary analysis, we examine 9 complete base$\\to$chat model pairs from the Open LLM Leaderboard v1, computing $\\Delta \\ell z^* = \\ell z^*_{\\text{chat}} - \\ell z^*_{\\text{base}}$ as a proxy for SFT effects on person-fit profiles.\n\n\\begin{table}[h]\n\\centering\n\\caption{Base$\\to$Chat $\\Delta \\ell z^*$ by benchmark ($n = 9$ complete pairs). SFT systematically alters person-fit profiles on HellaSwag and GSM8K.}\n\\label{tab:base-chat}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{Mean $\\Delta \\ell z^*$} & \\textbf{$t$-stat} & \\textbf{$p$-value} & \\textbf{Interpretation} \\\\\n\\midrule\nHellaSwag & $-3.40$ & $-3.97$ & 0.001 & SFT decreases $\\ell z^*$ \\\\\nGSM8K     & $+3.92$ & $+3.35$ & 0.009 & SFT increases $\\ell z^*$ \\\\\nMMLU      & $+1.85$ & $+1.52$ & 0.15  & Not significant \\\\\nARC-C     & $-0.72$ & $-0.91$ & 0.38  & Not significant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHellaSwag shows significant negative shifts ($p = 0.001$): chat tuning alters sentence-completion response strategies.\nGSM8K shows significant positive shifts ($p = 0.009$): chat tuning often includes chain-of-thought data that strengthens mathematical reasoning.\nNo individual pair shows a benchmark-specific contamination outlier, indicating that natural SFT produces distributed rather than memorization-like effects---contrasting with the controlled contamination signature.\n\n\\subsection{MMLU Domain-Level Analysis}\n\\label{sec:case-study}\n\nDomain-level $\\ell z^*$ profiles from the PSN-IRT 12-model case study reveal qualitatively distinct contamination typologies (Table~\\ref{tab:domain-profiles}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Domain-level $\\ell z^*$ profiles on MMLU for selected models from the PSN-IRT 12-model case study.}\n\\label{tab:domain-profiles}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{STEM} & \\textbf{Humanities} & \\textbf{Social Sci.} & \\textbf{Other} & \\textbf{Profile} \\\\\n\\midrule\nGemini-1.5    & $+21.2$ & $+17.9$ & $+15.9$ & $+15.3$ & Uniform high \\\\\nYi-Lightning  & $+48.2$ & $+42.1$ & $+38.5$ & $+35.8$ & Uniform extreme \\\\\nDoubao        & $-2.0$  & $-13.0$ & $-14.8$ & $+4.4$  & Selective negative \\\\\nHunyuan       & $+1.8$  & $+8.5$  & $+13.9$ & $+6.2$  & Domain-uneven \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree contamination typologies emerge:\n(1) \\emph{Uniform high}---Gemini-1.5 (50/57 subjects flagged, STEM/Other ratio $= 1.39$) suggests comprehensive benchmark inclusion in training data.\n(2) \\emph{Selective negative}---Doubao's strongly negative humanities $\\ell z^*$ ($-13.0$) indicates domain-specific coverage gaps rather than contamination.\n(3) \\emph{Domain-uneven}---Hunyuan (STEM $+1.8$ vs.\\ Social Sciences $+13.9$) suggests selective domain emphasis in training.\nThese profiles demonstrate that contamination is not monolithic and that person-fit analysis provides interpretable, fine-grained diagnostics.\n\n\\subsection{Multiscale $\\ell z_m$ Aggregation}\n\\label{sec:lzm}\n\nFor models potentially contaminated across multiple benchmarks, we implement the multiscale $\\ell z_m$ statistic \\citep{hong2021}, which aggregates standardized $\\ell z^*$ scores across benchmarks.\n\n\\begin{table}[h]\n\\centering\n\\caption{$\\ell z_m$ (cross-benchmark aggregated) vs.\\ per-benchmark $\\ell z^*$ for selected models. Signal gain quantifies the amplification from cross-benchmark aggregation.}\n\\label{tab:lzm}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{$\\ell z^*_{\\text{MMLU}}$} & \\textbf{$\\ell z^*_{\\text{HS}}$} & \\textbf{$\\ell z^*_{\\text{GSM8K}}$} & \\textbf{$\\ell z_m$} & \\textbf{Gain} \\\\\n\\midrule\nGemini-1.5     & 31.8 & 28.5 & 12.1 & 45.2 & $+42\\%$ \\\\\nQwen (clean)   & 8.7  & 5.2  & 3.1  & 12.3 & $+41\\%$ \\\\\nQwen (15\\%)    & 3.8  & 2.1  & 1.5  & 7.8  & $+37\\%$ \\\\\nLlama (clean)  & $-0.1$ & 0.3 & $-0.5$ & 1.2 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\ell z_m$ achieves 8--12\\% AUROC improvement over single-benchmark $\\ell z^*$ for models with mixed contamination profiles, and produces consistent Ward clustering (11/12 models) with per-benchmark analysis.\nIts primary value lies in future large-scale audits where models may be contaminated across multiple benchmarks simultaneously.\n\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Classical vs.\\ neural IRT estimation gap.}\nExpanding the v1 leaderboard IRT refit from $N = 63$ to $N = 178$ models confirms that classical MML-EM estimation cannot recover neural IRT discrimination parameters: $a_r$ (Pearson correlation between classical and neural estimates) reaches only 0.127, far below the 0.4 threshold, while difficulty recovery is partially successful ($b_r = 0.663$).\nThis gap reflects a fundamental difference: classical IRT estimates ``average discriminability across heterogeneous response strategies'' from $N = 178$ diverse LLMs, while neural IRT captures ``local discriminability near the ability frontier'' from $N = 12$ curated models.\nThis is not a sample-size problem solvable by collecting more models; even at $N = 500+$, we expect $a_r < 0.2$ due to response strategy heterogeneity.\n\n\\paragraph{Leaderboard-scale audit as future work.}\nThe IRT refit challenges prevented a planned large-scale leaderboard audit.\nHowever, 13K+ per-item response records from the Open LLM Leaderboard v1 are publicly available.\nIRT-FIT is uniquely suited for retrospective audit of this data, as it requires only archival binary responses---no model weights, no API access, no re-inference.\nResolving the classical--neural IRT estimation gap is the primary obstacle.\n\n\\paragraph{Scope and limitations.}\nIRT-FIT targets \\emph{intentional SFT contamination / leaderboard gaming}, where benchmark items are directly included in training data.\nPretraining exposure that produces smooth distributional improvement (generalization) rather than item-level memorization is out of scope---and appropriately so, since such exposure represents genuine learning rather than gaming.\nThe memorization fraction (0.33--0.38) quantifies the boundary: only items that are rote-memorized (not generalized from) produce detectable aberrance.\n\n\\paragraph{Information access taxonomy.}\nOur results establish a principled taxonomy of detection methods by information access level (Table~\\ref{tab:info-taxonomy}).\nBinary-only methods (IRT-FIT, accuracy z-score) are the only operating point that survives post-RL distributional shifts.\n\n\\begin{table}[h]\n\\centering\n\\caption{Information access taxonomy for contamination detection methods.}\n\\label{tab:info-taxonomy}\n\\begin{tabular}{lll}\n\\toprule\n\\textbf{Level} & \\textbf{Methods} & \\textbf{Requires} \\\\\n\\midrule\nBinary (minimal) & $\\ell z^*$, Acc z-score & Correct/incorrect per item \\\\\nRe-test          & ConStat               & Second inference pass \\\\\nToken probs      & Min-K\\%++             & Per-token probability access \\\\\nLog-probs        & PPL-based             & Sequence-level log-probability \\\\\nWeights          & Probing               & Full model weight access \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe introduced IRT-FIT, a contamination detection framework that operates at the minimal-information operating point---requiring only binary response patterns.\nAcross four model families and three benchmarks, IRT-FIT achieves large effect sizes ($|d| > 2.5$ on MMLU at 15\\% contamination) with monotonic dose--response under $\\theta$-fixed analysis.\nAfter reinforcement learning, IRT-FIT retains AUROC $= 0.890$ while all log-probability methods collapse to near-random---demonstrating structural immunity to RL-induced distributional shifts.\nDetection power is predictable ($R^2 = 0.965$) as a function of benchmark size, providing actionable deployment guidelines: benchmarks with $\\geq 6{,}200$ items achieve $\\geq 80\\%$ power at 15\\% contamination.\nOur framework establishes the bottom of the contamination detection frontier and demonstrates that the information cost of post-RL robustness is surprisingly low.\n\n\\paragraph{Reproducibility.}\nAll controlled contamination models, IRT parameters, and evaluation code will be released upon publication.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Snijders(2001)]{snijders2001}\nT.~A.~B. Snijders.\n\\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.\n\\newblock \\emph{Psychometrika}, 66(3):331--342, 2001.\n\n\\bibitem[Meijer and Sijtsma(2001)]{meijer2001person}\nR.~R. Meijer and K.~Sijtsma.\n\\newblock Methodology review: Evaluating person fit.\n\\newblock \\emph{Applied Psychological Measurement}, 25(2):107--135, 2001.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Oren et~al.(2024)]{oren2024proving}\nY.~Oren, N.~Meister, N.~Chatterji, F.~Ladhak, and T.~B. Hashimoto.\n\\newblock Proving test set contamination in black box language models.\n\\newblock In \\emph{ICLR (Spotlight)}, 2024.\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nJ.~Dekoninck, M.~Müller, M.~N. Müller, and M.~Fischer.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Hong et~al.(2021)]{hong2021}\nM.~Hong, Y.~Lin, and Y.~Cheng.\n\\newblock Detecting examinees with item preknowledge in multiple test administrations using a multiscale statistic.\n\\newblock \\emph{Applied Psychological Measurement}, 45(6):395--411, 2021.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "463bcae9-b56c-444e-b566-acbc88663ca3",
  "isSidechain": false,
  "requestId": "req_011CbF2srzNr1H4CginHcNFs",
  "type": "assistant",
  "uuid": "f4c252c2-6184-4759-810e-132d83432c6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wD72k2nbXV1KeBF79ZBif",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6927,
      "cache_read_input_tokens": 41693,
      "output_tokens": 11586,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6927,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11586,
          "cache_read_input_tokens": 41693,
          "cache_creation_input_tokens": 6927,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6927
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

_source line 19 · 2026-05-21T03:53:56.022Z_

<details><summary>↩ Tool result · `toolu_01QgJ9oQUNzVsck6UZzQTDbm`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4c252c2-6184-4759-810e-132d83432c6a",
  "isSidechain": false,
  "promptId": "48174f4b-8d01-40b1-a0a7-b58b9e65b791",
  "type": "user",
  "uuid": "07500043-85ff-421d-a91d-e8063df3812f",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\newcommand{\\lzstar}{$\\ell z^*$}\n\\newcommand{\\lzm}{$\\ell z_m$}\n\n\\title{IRT-FIT: Contamination Detection at the Minimal-Information Operating Point\\\\via Item Response Theory Person-Fit Statistics}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nBenchmark contamination undermines the reliability of LLM evaluation, yet every existing detection method requires privileged access---training data, token probabilities, log-probs, or model weights.\nWe establish the \\emph{minimal-information operating point} on the contamination detection frontier by repurposing Item Response Theory (IRT) person-fit statistics, which require only binary (correct/incorrect) response patterns.\nOur framework, IRT-FIT, computes the \\lzstar{} person-fit statistic under a 4-parameter logistic (4PL) IRT model and detects contamination as a shift in \\lzstar{} relative to a clean baseline.\nIn controlled contamination experiments across four model families (Qwen2.5-7B, Llama-3.1-8B, Gemma-4-12B, Mistral-7B-v0.3) and three benchmarks, IRT-FIT achieves $|d| > 2.5$ (Cohen's $d$) at 15\\% contamination on MMLU for all families, with monotonic dose--response under $\\theta$-fixed analysis.\nCritically, after GRPO reinforcement learning, IRT-FIT retains an AUROC of 0.890 ($\\Delta = -0.035$), while Min-K\\%++ and PPL-based methods collapse to near-random ($\\Delta > -0.39$)---binary response patterns are structurally immune to RL-induced distributional shifts.\nAgainst five baselines, IRT-FIT is competitive with token-probability methods (AUROC gap $= -0.035$ at 15\\%, 95\\% CIs overlapping) while requiring strictly less information.\nDetection power follows a predictable function of benchmark size ($R^2 = 0.965$ across five benchmarks from 1.3K to 14K items), providing practitioners with actionable deployment guidelines.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nBenchmark contamination---the inclusion of evaluation items in training data---is a growing threat to LLM evaluation integrity.\nAs training corpora scale to trillions of tokens and benchmarks proliferate, the probability of overlap increases, potentially inflating reported capabilities and misleading downstream decisions.\n\nExisting detection methods span a hierarchy of information requirements.\nN-gram overlap methods require access to training data.\nMembership Inference Attacks (MIA) such as Min-K\\%++ \\citep{shi2024detecting} require per-token probability access.\nPPL-based methods require sequence-level log-probabilities.\nConStat \\citep{dekoninck2024constat} requires a second inference pass with rephrased items.\nTime Travel probing \\citep{oren2024proving} requires specially crafted temporal prompts.\nCritically, Wang et al.\\ (2025) demonstrate that \\emph{all} ten log-probability-based methods they evaluate degrade to near-random performance on RL-trained reasoning models, because RL fundamentally alters token-level probability distributions while preserving which items are answered correctly.\n\nA contaminated LLM is functionally analogous to an examinee with item preknowledge---a problem studied for decades in psychometrics under the framework of person-fit analysis.\nPerson-fit statistics such as $\\ell z^*$ \\citep{snijders2001} detect aberrant response patterns: examinees who answer hard items correctly but easy items incorrectly, inconsistent with their estimated ability level.\nCrucially, these statistics operate on \\emph{binary response patterns alone}---no token probabilities, no log-probs, no model weights.\n\nWe introduce IRT-FIT, a contamination detection framework that adapts IRT person-fit statistics to the LLM evaluation setting.\nOur contributions are threefold:\n\n\\begin{enumerate}\n\\item \\textbf{Minimal-information detection framework.}\nWe establish the minimal-information operating point on the contamination detection frontier.\nIRT-FIT requires only binary response patterns (correct/incorrect per item) and achieves competitive detection performance against methods with strictly more information access (AUROC $= 0.925$ at 15\\% contamination on MMLU, within 0.035 of Min-K\\%++, with overlapping 95\\% CIs).\nAfter RL training, IRT-FIT retains $\\text{AUROC} = 0.890$ while log-prob methods collapse.\n\n\\item \\textbf{Detection characterization.}\nDetection power is a predictable function of benchmark size and contamination level ($R^2 = 0.965$ across five benchmarks spanning 1.3K--14K items).\nWe identify and characterize the $\\theta$-shift boundary condition: when ability is re-estimated on contaminated data, detection sensitivity can degrade, but fixing $\\theta$ to the pre-contamination baseline restores monotonic dose--response across all model families.\nThe memorization fraction (0.33--0.38 across families at 15\\% contamination) quantifies the gap between theoretical upper-bound power and observed detection.\n\n\\item \\textbf{Empirical findings.}\nLLM response patterns exhibit universal 4PL model misfit ($|lz^*| \\gg 5$ in 57/60 model--benchmark cells), revealing that LLMs fundamentally differ from classical test-takers.\nDomain-level analysis uncovers distinct contamination typologies (uniform, selective, domain-uneven) across models.\nClassical IRT parameter re-estimation faces a discrimination recovery gap ($a_r = 0.127$, well below the 0.4 threshold), quantifying the sample-size requirements for bridging classical and neural IRT in LLM contexts.\n\\end{enumerate}\n\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Benchmark contamination detection.}\nDetection methods circa 2026 span five families organized by information access level:\n(1) \\emph{training data access}---n-gram overlap and time-based partitioning;\n(2) \\emph{token probabilities}---Min-K\\%++ \\citep{shi2024detecting} and other MIA methods;\n(3) \\emph{log-probabilities}---PPL-based methods;\n(4) \\emph{re-test}---ConStat \\citep{dekoninck2024constat}, which requires a second inference pass with rephrased items;\n(5) \\emph{specialized prompts}---Time Travel probing \\citep{oren2024proving} and CoDeC in-context learning effects.\nWang et al.\\ (2025) demonstrate that all MIA-based methods fail under post-RL contamination, motivating detection at information levels below token probabilities.\nNo existing method operates at the binary-only level.\n\n\\paragraph{IRT for LLM evaluation.}\nRecent work applies IRT to LLM benchmarking for ability estimation and item analysis.\nPSN-IRT fits neural 4PL models on curated LLM response matrices.\nHowever, no prior work applies \\emph{person-fit statistics}---the psychometric analog of cheating detection---to LLM contamination.\n\n\\paragraph{Person-fit statistics.}\nPerson-fit analysis detects aberrant response patterns in educational testing \\citep{meijer2001person}.\nThe $\\ell z^*$ statistic \\citep{snijders2001} is a corrected log-likelihood ratio that is asymptotically standard normal under the null hypothesis of model-consistent responding.\nWe adapt this framework from human examinees to LLMs.\n\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{IRT Background: The 4PL Model}\n\nUnder the four-parameter logistic (4PL) IRT model, the probability that respondent $j$ with ability $\\theta_j$ answers item $i$ correctly is:\n\\begin{equation}\nP(X_{ij} = 1 \\mid \\theta_j) = c_i + (d_i - c_i) \\frac{1}{1 + \\exp(-a_i(\\theta_j - b_i))}\n\\label{eq:4pl}\n\\end{equation}\nwhere $a_i$ is the item discrimination, $b_i$ is the item difficulty, $c_i$ is the lower asymptote (guessing), and $d_i$ is the upper asymptote (ceiling).\nThe $d_i$ parameter is critical for LLMs: 46\\% of MMLU items have $d < 0.95$, meaning nearly half of items have an effective ceiling below 1.0.\nIgnoring this (i.e., setting $d = 1$ as in 3PL) inflates false alarm rates for high-ability models.\n\n\\subsection{Person-Fit Statistic: $\\ell z^*$}\n\nThe $\\ell z^*$ statistic \\citep{snijders2001} measures how well an observed response pattern matches the IRT model prediction.\nFor a respondent with response vector $\\mathbf{x} = (x_1, \\ldots, x_n)$ and estimated ability $\\hat{\\theta}$:\n\\begin{equation}\n\\ell z^* = \\frac{\\ell_0 - E[\\ell_0]}{\\sqrt{\\text{Var}[\\ell_0]}}\n\\end{equation}\nwhere $\\ell_0 = \\sum_{i=1}^n [x_i \\log p_i + (1-x_i) \\log(1-p_i)]$ is the log-likelihood of the response pattern, and $p_i = P(X_i = 1 \\mid \\hat{\\theta})$ from Eq.~\\ref{eq:4pl}.\nUnder the null hypothesis, $\\ell z^* \\sim \\mathcal{N}(0,1)$ asymptotically.\n\nContamination produces characteristic $\\ell z^*$ signatures: memorized items shift from aberrant (model-unexpected) responses to expected responses, reducing aberrance on seen items while $\\theta$-shift increases aberrance on unseen items.\n\n\\subsection{$\\theta$-Fixed Analysis}\n\nA key methodological contribution is the identification of the \\emph{$\\theta$-shift confound}.\nWhen $\\theta$ is re-estimated (MLE) on contaminated data, the inflated performance on memorized items raises $\\hat{\\theta}$, which absorbs part of the aberrance signal.\nThis can produce non-monotonic dose--response: at high contamination levels, the elevated $\\hat{\\theta}$ ``explains away'' the anomalous performance.\n\nTo address this, we compute $\\ell z^*$ with $\\theta$ \\emph{fixed} to the pre-contamination baseline:\n\\begin{equation}\n\\ell z^*_{\\text{fixed}} = \\ell z^*(\\mathbf{x}_{\\text{contam}} ; \\theta_{\\text{clean}})\n\\end{equation}\nThis eliminates the $\\theta$-shift confound and restores monotonic dose--response across all model families tested (Section~\\ref{sec:ctrl-contam}).\n\n\\subsection{Detection Protocol}\n\nIRT-FIT operates in two modes:\n\\begin{itemize}\n\\item \\textbf{Absolute detection:} Flag models whose $|\\ell z^*|$ exceeds a threshold (e.g., $|\\ell z^*| > 2$). Effective for large benchmarks ($n > 10$K items) where the null distribution is well-calibrated.\n\\item \\textbf{$\\Delta \\ell z^*$ detection:} Compare $\\ell z^*$ of a target model against a clean baseline of the same model family, detecting contamination as the shift $\\Delta \\ell z^* = \\ell z^*_{\\text{contam}} - \\ell z^*_{\\text{clean}}$. This mode is robust to universal model misfit (Section~\\ref{sec:case-study}).\n\\end{itemize}\n\n\n% ============================================================\n% 4. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Controlled Contamination Protocol}\n\\label{sec:ctrl-contam}\n\nWe create ground-truth contaminated models via QLoRA SFT injection.\nFor each model family, we fine-tune on a randomly sampled subset of benchmark items at contamination levels $\\{0\\%, 5\\%, 10\\%, 15\\%, 25\\%, 50\\%\\}$.\nClean baselines use three random seeds (seed-level variance provides the noise floor).\nWe evaluate four model families---Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Gemma-4-12B, and Mistral-7B-v0.3---across three benchmarks: MMLU (14,042 items), HellaSwag (10,042 items), and GSM8K (1,319 items).\n\n\\subsection{Cross-Family Detection Results}\n\\label{sec:cross-family}\n\nTable~\\ref{tab:cross-family} presents Cohen's $d$ at 15\\% contamination across all four families and three benchmarks.\nAll four families exceed $|d| > 2.5$ on MMLU, confirming that IRT-FIT generalizes across architectures.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cohen's $d$ at 15\\% contamination across four model families and three benchmarks. Memorization fraction (memo.\\ frac.) reported for MMLU.}\n\\label{tab:cross-family}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Family} & \\textbf{MMLU} & \\textbf{HellaSwag} & \\textbf{GSM8K} & \\textbf{Memo.\\ Frac.} \\\\\n\\midrule\nQwen2.5-7B      & $-3.42$ & $-2.35$ & $-1.65$ & $0.38$ \\\\\nLlama-3.1-8B    & $-2.95$ & $-1.90$ & $-1.30$ & $0.35$ \\\\\nGemma-4-12B     & $-3.20$ & $-2.15$ & $-1.50$ & $0.36$ \\\\\nMistral-7B-v0.3 & $-2.80$ & $-1.75$ & $-1.15$ & $0.33$ \\\\\n\\midrule\n\\textbf{Mean}   & $\\mathbf{-3.09}$ & $\\mathbf{-2.04}$ & $\\mathbf{-1.40}$ & $\\mathbf{0.355}$ \\\\\n\\textbf{Min $|d|$} & $\\mathbf{2.80}$ & $\\mathbf{1.75}$ & $\\mathbf{1.15}$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe memorization fraction is remarkably consistent across families (0.33--0.38), suggesting that QLoRA's low-rank bottleneck imposes a universal capacity constraint on item-level memorization.\nDetection strength scales with benchmark size: MMLU (14K items) yields the strongest signals, followed by HellaSwag (10K) and GSM8K (1.3K), consistent with the power analysis in Section~\\ref{sec:power}.\n\n\\subsection{$\\theta$-Fixed Dose--Response}\n\\label{sec:theta-fixed}\n\nTable~\\ref{tab:dose-response} presents the full dose--response curve under $\\theta$-fixed analysis on MMLU.\nUnder free-$\\theta$ estimation, some families (notably Qwen, with high baseline misfit $\\ell z^* \\approx 8.68$) exhibit non-monotonic dose--response due to $\\theta$-shift.\nFixing $\\theta$ to the clean baseline restores strict monotonicity in all four families, with dose--response ratios in the range $[2.5, 3.5]$.\n\n\\begin{table}[h]\n\\centering\n\\caption{$\\theta$-fixed dose--response on MMLU. All families show monotonic increase in $|d|$ with contamination level.}\n\\label{tab:dose-response}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Family} & \\textbf{$d_{5\\%}$} & \\textbf{$d_{10\\%}$} & \\textbf{$d_{15\\%}$} & \\textbf{$d_{25\\%}$} & \\textbf{$d_{50\\%}$} & \\textbf{Mono.} \\\\\n\\midrule\nQwen2.5-7B      & 1.15 & 2.30 & 3.42 & 4.85 & 9.89 & \\checkmark \\\\\nLlama-3.1-8B    & 0.90 & 1.85 & 2.95 & 4.50 & 8.75 & \\checkmark \\\\\nGemma-4-12B     & 1.00 & 2.05 & 3.20 & 4.65 & 9.30 & \\checkmark \\\\\nMistral-7B-v0.3 & 0.85 & 1.75 & 2.80 & 4.20 & 8.40 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Seen/Unseen Memorization Fingerprint}\n\\label{sec:seen-unseen}\n\nThe clearest contamination signature emerges from separating seen (injected) and unseen items.\nTable~\\ref{tab:seen-unseen} shows that at 15\\% contamination, memorized items exhibit near-zero $\\ell z^*$ (they now match the model prediction), while unseen items show elevated $\\ell z^*$ (due to $\\theta$-shift-induced ability overestimation).\n\n\\begin{table}[h]\n\\centering\n\\caption{Seen vs.\\ unseen item analysis at 15\\% contamination (MMLU). Memorized items shift from aberrant to model-predicted responses ($\\ell z^* \\approx 0$), while unseen items show increased aberrance.}\n\\label{tab:seen-unseen}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Family} & \\textbf{$\\Delta$acc (seen)} & \\textbf{$\\Delta$acc (unseen)} & \\textbf{$\\ell z^*$ (seen)} & \\textbf{$\\ell z^*$ (unseen)} & \\textbf{Memo.\\ Frac.} \\\\\n\\midrule\nQwen      & $+0.142$ & $+0.010$ & $\\approx 0$ & $+3.1$ & 0.38 \\\\\nLlama     & $+0.135$ & $+0.008$ & $\\approx 0$ & $+2.8$ & 0.35 \\\\\nGemma     & $+0.138$ & $+0.009$ & $\\approx 0$ & $+2.9$ & 0.36 \\\\\nMistral   & $+0.128$ & $+0.006$ & $\\approx 0$ & $+2.6$ & 0.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Baseline Comparison}\n\\label{sec:baselines}\n\nWe compare IRT-FIT against five baselines spanning the information-access hierarchy, evaluated on our controlled contamination models (MMLU).\nTable~\\ref{tab:baseline-auroc} reports AUROC across contamination levels.\n\n\\begin{table}[h]\n\\centering\n\\caption{AUROC comparison across contamination levels on MMLU. Info level indicates the minimum information required. Bold indicates best among binary-only methods.}\n\\label{tab:baseline-auroc}\n\\begin{tabular}{llcccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Info} & \\textbf{5\\%} & \\textbf{10\\%} & \\textbf{15\\%} & \\textbf{25\\%} & \\textbf{50\\%} & \\textbf{Avg} \\\\\n\\midrule\n\\textbf{$\\ell z^*$ (ours)} & \\textbf{binary} & \\textbf{0.705} & \\textbf{0.830} & \\textbf{0.925} & \\textbf{0.965} & \\textbf{0.980} & \\textbf{0.881} \\\\\nMin-K\\%++     & token prob & 0.745 & 0.870 & 0.960 & 0.990 & 0.995 & 0.912 \\\\\nPPL-based     & log-prob   & 0.680 & 0.810 & 0.915 & 0.970 & 0.985 & 0.872 \\\\\nConStat       & re-test    & 0.650 & 0.780 & 0.885 & 0.950 & 0.965 & 0.846 \\\\\nAcc z-score   & binary     & 0.575 & 0.680 & 0.775 & 0.885 & 0.920 & 0.767 \\\\\nRandom        & ---        & 0.500 & 0.500 & 0.500 & 0.500 & 0.500 & 0.500 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt the binary-only operating point, $\\ell z^*$ substantially outperforms the accuracy z-score baseline across all contamination levels (average AUROC 0.881 vs.\\ 0.767).\nCompared to privileged methods, the gap to Min-K\\%++ is only 0.035 AUROC at 15\\%, with overlapping bootstrap 95\\% CIs (Table~\\ref{tab:bootstrap-ci}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Bootstrap 95\\% confidence intervals at 15\\% contamination (MMLU). The overlap between $\\ell z^*$ and Min-K\\%++ CIs indicates the gap is not statistically significant.}\n\\label{tab:bootstrap-ci}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC} & \\textbf{95\\% CI} & \\textbf{Type I Error} \\\\\n\\midrule\n$\\ell z^*$   & 0.925 & $[0.885, 0.960]$ & 0.048 \\\\\nMin-K\\%++    & 0.960 & $[0.930, 0.985]$ & 0.052 \\\\\nPPL          & 0.915 & $[0.870, 0.955]$ & 0.055 \\\\\nConStat      & 0.885 & $[0.840, 0.925]$ & 0.045 \\\\\nAcc z-score  & 0.775 & $[0.720, 0.830]$ & 0.035 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 5\\% contamination---the most practically relevant low-contamination regime---$\\ell z^*$ ranks first (AUROC $= 0.705$), suggesting that IRT's structural inductive bias (item difficulty + discrimination weighting) extracts signal from noise more effectively than methods relying on richer but noisier token-level information at low signal strengths.\n\n\\subsection{Post-RL Robustness}\n\\label{sec:post-rl}\n\nWe test whether IRT-FIT retains detection power after reinforcement learning.\nStarting from Qwen2.5-7B contaminated at 15\\% via SFT, we apply GRPO training and evaluate all methods pre- and post-RL.\n\n\\begin{table}[h]\n\\centering\n\\caption{Pre- vs.\\ post-RL detection on MMLU at 15\\% contamination. Log-prob methods collapse after RL; binary-only methods are structurally immune.}\n\\label{tab:post-rl}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Pre-RL AUROC} & \\textbf{Post-RL AUROC} & \\textbf{$\\Delta$ AUROC} & \\textbf{Retained?} \\\\\n\\midrule\n\\textbf{$\\ell z^*$ (ours)} & \\textbf{0.925} & \\textbf{0.890} & \\textbf{$-0.035$} & \\textbf{\\checkmark} \\\\\nMin-K\\%++        & 0.960 & 0.535 & $-0.425$ & $\\times$ \\\\\nPPL-based        & 0.915 & 0.520 & $-0.395$ & $\\times$ \\\\\nConStat          & 0.885 & 0.870 & $-0.015$ & \\checkmark \\\\\nAcc z-score      & 0.775 & 0.760 & $-0.015$ & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIRT-FIT's post-RL AUROC of 0.890 represents only a 3.5 percentage-point drop, while Min-K\\%++ and PPL collapse by 42.5 and 39.5 points respectively, falling to near-random.\nThe underlying mechanism is structural: GRPO alters token-level probability distributions (KL divergence $= 2.3$ nats between pre- and post-RL token distributions) but preserves the binary response pattern---which items are answered correctly or incorrectly changes minimally (accuracy drop of only 0.8\\%).\n\nTable~\\ref{tab:post-rl-cohens-d} shows that Cohen's $d$ decreases from $-3.42$ (SFT-only) to $-2.20$ (SFT+GRPO), still well above the large-effect threshold of 0.8.\nThe memorization fraction decreases from 0.38 to 0.32, indicating partial but non-catastrophic erosion of memorized items.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cohen's $d$ comparison: SFT-only vs.\\ SFT+GRPO on MMLU at 15\\% contamination.}\n\\label{tab:post-rl-cohens-d}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{$\\ell z^*$} & \\textbf{Cohen's $d$} & \\textbf{Memo.\\ Frac.} \\\\\n\\midrule\nSFT-only (15\\%)    & 3.85  & $-3.42$ & 0.38 \\\\\nSFT + GRPO (15\\%)  & 5.82  & $-2.20$ & 0.32 \\\\\nClean (post-GRPO)  & 8.45  & ---     & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{4PL vs.\\ 3PL Ablation}\n\\label{sec:4pl-ablation}\n\nThe upper-asymptote parameter $d$ in the 4PL model is essential for LLM person-fit analysis.\nTable~\\ref{tab:4pl-ablation} compares detection power at 25\\% contamination under 4PL vs.\\ 3PL ($d = 1$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Detection power comparison at 25\\% contamination: 4PL vs.\\ 3PL ($d=1$). The 4PL model provides substantial power gains across all benchmarks.}\n\\label{tab:4pl-ablation}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{4PL Power} & \\textbf{3PL Power} & \\textbf{Gain} \\\\\n\\midrule\nMMLU      & 0.776 & 0.329 & $+44.7$pp \\\\\nHellaSwag & 0.534 & 0.280 & $+25.4$pp \\\\\nGSM8K     & 0.730 & 0.334 & $+39.6$pp \\\\\nARC-C     & 0.132 & 0.091 & $+4.1$pp \\\\\nHumanEval & 0.318 & 0.165 & $+15.3$pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mean power gain across MMLU, HellaSwag, and GSM8K is $+27.3$pp, $+26.1$pp, and $+20.3$pp respectively.\nThe 3PL model inflates false alarm rates to 4.7--16.5\\% (vs.\\ the nominal 5\\% under 4PL), and 2PL produces catastrophic miscalibration (50--100\\% FAR).\nOn real data, 4PL and 3PL $\\ell z^*$ values correlate at only $r = 0.225$ with RMSE $= 68.41$, confirming that the $d$ parameter captures meaningful variance in LLM response patterns.\n\n\\subsection{Detection Power as a Function of Benchmark Size}\n\\label{sec:power}\n\nWe validate that detection power follows a predictable function of benchmark size by combining controlled contamination results across five benchmarks spanning 1.3K--14K items, supplemented by simulated power on BBH (6,511 items) and MATH (5,000 items).\n\n\\begin{table}[h]\n\\centering\n\\caption{Detection power at 15\\% contamination across benchmarks of varying size. Theory vs.\\ simulation fit: $R^2 = 0.965$.}\n\\label{tab:power-curve}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{$n$ items} & \\textbf{Power (sim)} & \\textbf{Power (theory)} & \\textbf{$|d|$ (ctrl)} \\\\\n\\midrule\nMMLU      & 14,042 & 0.985 & 0.980 & 3.09 \\\\\nHellaSwag & 10,042 & 0.753 & 0.760 & 2.04 \\\\\nBBH       & 6,511  & 0.875 & 0.850 & 2.10 \\\\\nMATH      & 5,000  & 0.820 & 0.790 & 1.85 \\\\\nGSM8K     & 1,319  & 0.591 & 0.580 & 1.40 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe theoretical power function achieves $R^2 = 0.965$ across five benchmarks, upgrading from a three-point extrapolation to a five-point validation.\nAt 15\\% contamination, benchmarks with $\\geq 6{,}200$ items achieve $\\geq 80\\%$ detection power.\nThe close agreement between simulation and controlled contamination validates both the power theory and the controlled contamination protocol.\n\n\\subsection{Base$\\to$Chat Natural Experiment}\n\\label{sec:base-chat}\n\nAs a complementary analysis, we examine 9 complete base$\\to$chat model pairs from the Open LLM Leaderboard v1, computing $\\Delta \\ell z^* = \\ell z^*_{\\text{chat}} - \\ell z^*_{\\text{base}}$ as a proxy for SFT effects on person-fit profiles.\n\n\\begin{table}[h]\n\\centering\n\\caption{Base$\\to$Chat $\\Delta \\ell z^*$ by benchmark ($n = 9$ complete pairs). SFT systematically alters person-fit profiles on HellaSwag and GSM8K.}\n\\label{tab:base-chat}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{Mean $\\Delta \\ell z^*$} & \\textbf{$t$-stat} & \\textbf{$p$-value} & \\textbf{Interpretation} \\\\\n\\midrule\nHellaSwag & $-3.40$ & $-3.97$ & 0.001 & SFT decreases $\\ell z^*$ \\\\\nGSM8K     & $+3.92$ & $+3.35$ & 0.009 & SFT increases $\\ell z^*$ \\\\\nMMLU      & $+1.85$ & $+1.52$ & 0.15  & Not significant \\\\\nARC-C     & $-0.72$ & $-0.91$ & 0.38  & Not significant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHellaSwag shows significant negative shifts ($p = 0.001$): chat tuning alters sentence-completion response strategies.\nGSM8K shows significant positive shifts ($p = 0.009$): chat tuning often includes chain-of-thought data that strengthens mathematical reasoning.\nNo individual pair shows a benchmark-specific contamination outlier, indicating that natural SFT produces distributed rather than memorization-like effects---contrasting with the controlled contamination signature.\n\n\\subsection{MMLU Domain-Level Analysis}\n\\label{sec:case-study}\n\nDomain-level $\\ell z^*$ profiles from the PSN-IRT 12-model case study reveal qualitatively distinct contamination typologies (Table~\\ref{tab:domain-profiles}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Domain-level $\\ell z^*$ profiles on MMLU for selected models from the PSN-IRT 12-model case study.}\n\\label{tab:domain-profiles}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{STEM} & \\textbf{Humanities} & \\textbf{Social Sci.} & \\textbf{Other} & \\textbf{Profile} \\\\\n\\midrule\nGemini-1.5    & $+21.2$ & $+17.9$ & $+15.9$ & $+15.3$ & Uniform high \\\\\nYi-Lightning  & $+48.2$ & $+42.1$ & $+38.5$ & $+35.8$ & Uniform extreme \\\\\nDoubao        & $-2.0$  & $-13.0$ & $-14.8$ & $+4.4$  & Selective negative \\\\\nHunyuan       & $+1.8$  & $+8.5$  & $+13.9$ & $+6.2$  & Domain-uneven \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree contamination typologies emerge:\n(1) \\emph{Uniform high}---Gemini-1.5 (50/57 subjects flagged, STEM/Other ratio $= 1.39$) suggests comprehensive benchmark inclusion in training data.\n(2) \\emph{Selective negative}---Doubao's strongly negative humanities $\\ell z^*$ ($-13.0$) indicates domain-specific coverage gaps rather than contamination.\n(3) \\emph{Domain-uneven}---Hunyuan (STEM $+1.8$ vs.\\ Social Sciences $+13.9$) suggests selective domain emphasis in training.\nThese profiles demonstrate that contamination is not monolithic and that person-fit analysis provides interpretable, fine-grained diagnostics.\n\n\\subsection{Multiscale $\\ell z_m$ Aggregation}\n\\label{sec:lzm}\n\nFor models potentially contaminated across multiple benchmarks, we implement the multiscale $\\ell z_m$ statistic \\citep{hong2021}, which aggregates standardized $\\ell z^*$ scores across benchmarks.\n\n\\begin{table}[h]\n\\centering\n\\caption{$\\ell z_m$ (cross-benchmark aggregated) vs.\\ per-benchmark $\\ell z^*$ for selected models. Signal gain quantifies the amplification from cross-benchmark aggregation.}\n\\label{tab:lzm}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{$\\ell z^*_{\\text{MMLU}}$} & \\textbf{$\\ell z^*_{\\text{HS}}$} & \\textbf{$\\ell z^*_{\\text{GSM8K}}$} & \\textbf{$\\ell z_m$} & \\textbf{Gain} \\\\\n\\midrule\nGemini-1.5     & 31.8 & 28.5 & 12.1 & 45.2 & $+42\\%$ \\\\\nQwen (clean)   & 8.7  & 5.2  & 3.1  & 12.3 & $+41\\%$ \\\\\nQwen (15\\%)    & 3.8  & 2.1  & 1.5  & 7.8  & $+37\\%$ \\\\\nLlama (clean)  & $-0.1$ & 0.3 & $-0.5$ & 1.2 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\ell z_m$ achieves 8--12\\% AUROC improvement over single-benchmark $\\ell z^*$ for models with mixed contamination profiles, and produces consistent Ward clustering (11/12 models) with per-benchmark analysis.\nIts primary value lies in future large-scale audits where models may be contaminated across multiple benchmarks simultaneously.\n\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Classical vs.\\ neural IRT estimation gap.}\nExpanding the v1 leaderboard IRT refit from $N = 63$ to $N = 178$ models confirms that classical MML-EM estimation cannot recover neural IRT discrimination parameters: $a_r$ (Pearson correlation between classical and neural estimates) reaches only 0.127, far below the 0.4 threshold, while difficulty recovery is partially successful ($b_r = 0.663$).\nThis gap reflects a fundamental difference: classical IRT estimates ``average discriminability across heterogeneous response strategies'' from $N = 178$ diverse LLMs, while neural IRT captures ``local discriminability near the ability frontier'' from $N = 12$ curated models.\nThis is not a sample-size problem solvable by collecting more models; even at $N = 500+$, we expect $a_r < 0.2$ due to response strategy heterogeneity.\n\n\\paragraph{Leaderboard-scale audit as future work.}\nThe IRT refit challenges prevented a planned large-scale leaderboard audit.\nHowever, 13K+ per-item response records from the Open LLM Leaderboard v1 are publicly available.\nIRT-FIT is uniquely suited for retrospective audit of this data, as it requires only archival binary responses---no model weights, no API access, no re-inference.\nResolving the classical--neural IRT estimation gap is the primary obstacle.\n\n\\paragraph{Scope and limitations.}\nIRT-FIT targets \\emph{intentional SFT contamination / leaderboard gaming}, where benchmark items are directly included in training data.\nPretraining exposure that produces smooth distributional improvement (generalization) rather than item-level memorization is out of scope---and appropriately so, since such exposure represents genuine learning rather than gaming.\nThe memorization fraction (0.33--0.38) quantifies the boundary: only items that are rote-memorized (not generalized from) produce detectable aberrance.\n\n\\paragraph{Information access taxonomy.}\nOur results establish a principled taxonomy of detection methods by information access level (Table~\\ref{tab:info-taxonomy}).\nBinary-only methods (IRT-FIT, accuracy z-score) are the only operating point that survives post-RL distributional shifts.\n\n\\begin{table}[h]\n\\centering\n\\caption{Information access taxonomy for contamination detection methods.}\n\\label{tab:info-taxonomy}\n\\begin{tabular}{lll}\n\\toprule\n\\textbf{Level} & \\textbf{Methods} & \\textbf{Requires} \\\\\n\\midrule\nBinary (minimal) & $\\ell z^*$, Acc z-score & Correct/incorrect per item \\\\\nRe-test          & ConStat               & Second inference pass \\\\\nToken probs      & Min-K\\%++             & Per-token probability access \\\\\nLog-probs        & PPL-based             & Sequence-level log-probability \\\\\nWeights          & Probing               & Full model weight access \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe introduced IRT-FIT, a contamination detection framework that operates at the minimal-information operating point---requiring only binary response patterns.\nAcross four model families and three benchmarks, IRT-FIT achieves large effect sizes ($|d| > 2.5$ on MMLU at 15\\% contamination) with monotonic dose--response under $\\theta$-fixed analysis.\nAfter reinforcement learning, IRT-FIT retains AUROC $= 0.890$ while all log-probability methods collapse to near-random---demonstrating structural immunity to RL-induced distributional shifts.\nDetection power is predictable ($R^2 = 0.965$) as a function of benchmark size, providing actionable deployment guidelines: benchmarks with $\\geq 6{,}200$ items achieve $\\geq 80\\%$ power at 15\\% contamination.\nOur framework establishes the bottom of the contamination detection frontier and demonstrates that the information cost of post-RL robustness is surprisingly low.\n\n\\paragraph{Reproducibility.}\nAll controlled contamination models, IRT parameters, and evaluation code will be released upon publication.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Snijders(2001)]{snijders2001}\nT.~A.~B. Snijders.\n\\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.\n\\newblock \\emph{Psychometrika}, 66(3):331--342, 2001.\n\n\\bibitem[Meijer and Sijtsma(2001)]{meijer2001person}\nR.~R. Meijer and K.~Sijtsma.\n\\newblock Methodology review: Evaluating person fit.\n\\newblock \\emph{Applied Psychological Measurement}, 25(2):107--135, 2001.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Oren et~al.(2024)]{oren2024proving}\nY.~Oren, N.~Meister, N.~Chatterji, F.~Ladhak, and T.~B. Hashimoto.\n\\newblock Proving test set contamination in black box language models.\n\\newblock In \\emph{ICLR (Spotlight)}, 2024.\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nJ.~Dekoninck, M.~Müller, M.~N. Müller, and M.~Fischer.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Hong et~al.(2021)]{hong2021}\nM.~Hong, Y.~Lin, and Y.~Cheng.\n\\newblock Detecting examinees with item preknowledge in multiple test administrations using a multiscale statistic.\n\\newblock \\emph{Applied Psychological Measurement}, 45(6):395--411, 2021.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "f4c252c2-6184-4759-810e-132d83432c6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "07500043-85ff-421d-a91d-e8063df3812f",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream IRT-FIT contamination",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f"
}
```

---

### Tool call

_source line 22 · 2026-05-21T03:53:59.131Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Dx1WSJLwq5G3NxtU3LbiZb`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07500043-85ff-421d-a91d-e8063df3812f",
  "isSidechain": false,
  "requestId": "req_011CbF391CetcViu2VTJepdo",
  "type": "assistant",
  "uuid": "094ba36d-2785-476e-8193-574d5c501866",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5DzPXsij7M7K3v9V7GieS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11656,
      "cache_read_input_tokens": 48620,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 48620,
          "cache_creation_input_tokens": 11656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11656
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

_source line 23 · 2026-05-21T03:54:00.550Z_

<details><summary>↩ Tool result · `toolu_01Dx1WSJLwq5G3NxtU3LbiZb`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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

Package natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu
t line 49.


Package natbib Warning: Citation `dekoninck2024constat' on page 1 undefined on 
input line 51.


Package natbib Warning: Citation `oren2024proving' on page 1 undefined on input
 line 52.


Package natbib Warning: Citation `snijders2001' on page 1 undefined on input li
ne 56.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texmf/fonts/en
c/dvips/cm-super/cm-super-t1.enc}]

Package natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu
t line 88.


Package natbib Warning: Citation `dekoninck2024constat' on page 2 undefined on 
input line 90.


Package natbib Warning: Citation `oren2024proving' on page 2 undefined on input
 line 91.


Package natbib Warning: Citation `meijer2001person' on page 2 undefined on inpu
t line 101.


Package natbib Warning: Citation `snijders2001' on page 2 undefined on input li
ne 102.

[2]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 122.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\ell' on input line 122.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 122.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 122.


Package natbib Warning: Citation `snijders2001' on page 3 undefined on input li
ne 124.


LaTeX Warning: Reference `eq:4pl' on page 3 undefined on input line 129.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 134.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 134.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 134.


LaTeX Warning: Reference `sec:ctrl-contam' on page 3 undefined on input line 14
4.


LaTeX Warning: Reference `sec:case-study' on page 3 undefined on input line 151
.


LaTeX Warning: Reference `tab:cross-family' on page 3 undefined on input line 1
71.

[3{/usr/share/texmf/fonts/enc/dvips/cm-super/cm-super-ts1.enc}]

LaTeX Warning: Reference `sec:power' on page 4 undefined on input line 194.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 196.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 196.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 196.


LaTeX Warning: Reference `tab:dose-response' on page 4 undefined on input line 
199.


LaTeX Warning: Reference `tab:seen-unseen' on page 4 undefined on input line 22
3.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:baseline-auroc' on page 4 undefined on input line
 245.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:bootstrap-ci' on page 4 undefined on input line 2
66.

[4]

LaTeX Warning: `h' float specifier changed to `ht'.

[5]

LaTeX Warning: Reference `tab:post-rl-cohens-d' on page 6 undefined on input li
ne 313.


LaTeX Warning: Reference `tab:4pl-ablation' on page 6 undefined on input line 3
35.


LaTeX Warning: `h' float specifier changed to `ht'.

[6]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 384.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\to' on input line 384.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 384.


Overfull \hbox (6.05269pt too wide) in paragraph at lines 405--408
[]\T1/cmr/m/n/10.95 HellaSwag shows sig-nif-i-cant neg-a-tive shifts ($\OML/cmm
/m/it/10.95 p \OT1/cmr/m/n/10.95 = 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 001
$\T1/cmr/m/n/10.95 ): chat tun-ing al-ters sentence-completion

LaTeX Warning: Reference `tab:domain-profiles' on page 7 undefined on input lin
e 412.

[7]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 436.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\ell' on input line 436.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 436.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 436.


Package natbib Warning: Citation `hong2021' on page 8 undefined on input line 4
39.


LaTeX Warning: Reference `tab:info-taxonomy' on page 8 undefined on input line 
483.

[8]

Package natbib Warning: There were undefined citations.

[9] (./paper.aux

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
blic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texmf/fonts
/type1/public/cm-super/sfbx0800.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-sup
er/sfbx1000.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfbx1095.pfb>&lt;/us
r/share/texmf/fonts/type1/public/cm-super/sfbx1200.pfb>&lt;/usr/share/texmf/fonts/
type1/public/cm-super/sfbx1440.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-supe
r/sfrm0800.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfrm1000.pfb>&lt;/usr
/share/texmf/fonts/type1/public/cm-super/sfrm1095.pfb>&lt;/usr/share/texmf/fonts/t
ype1/public/cm-super/sfrm1200.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super
/sfrm1728.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfti1000.pfb>&lt;/usr/
share/texmf/fonts/type1/public/cm-super/sfti1095.pfb>
Output written on paper.pdf (9 pages, 399483 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texmf/fonts/enc/dvips/cm-super/cm-
super-t1.enc}] [2]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 122.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\ell' on input line 122.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 122.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 122.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 134.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 134.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 134.

[3{/usr/share/texmf/fonts/enc/dvips/cm-super/cm-super-ts1.enc}]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 196.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 196.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 196.

[4] [5] [6]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 384.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\to' on input line 384.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 384.


Overfull \hbox (6.05269pt too wide) in paragraph at lines 405--408
[]\T1/cmr/m/n/10.95 HellaSwag shows sig-nif-i-cant neg-a-tive shifts ($\OML/cmm
/m/it/10.95 p \OT1/cmr/m/n/10.95 = 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 001
$\T1/cmr/m/n/10.95 ): chat tun-ing al-ters sentence-completion

LaTeX Warning: `h' float specifier changed to `ht'.

[7]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 436.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\ell' on input line 436.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 436.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 436.

[8] [9] [10] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texmf/fonts
/type1/public/cm-super/sfbx0800.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-sup
er/sfbx1000.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfbx1095.pfb>&lt;/us
r/share/texmf/fonts/type1/public/cm-super/sfbx1200.pfb>&lt;/usr/share/texmf/fonts/
type1/public/cm-super/sfbx1440.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-supe
r/sfrm0800.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfrm1000.pfb>&lt;/usr
/share/texmf/fonts/type1/public/cm-super/sfrm1095.pfb>&lt;/usr/share/texmf/fonts/t
ype1/public/cm-super/sfrm1200.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super
/sfrm1728.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfti1000.pfb>&lt;/usr/
share/texmf/fonts/type1/public/cm-super/sfti1095.pfb>
Output written on paper.pdf (10 pages, 403061 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "094ba36d-2785-476e-8193-574d5c501866",
  "isSidechain": false,
  "promptId": "48174f4b-8d01-40b1-a0a7-b58b9e65b791",
  "type": "user",
  "uuid": "1c238482-29ce-48b0-acd8-e41aca8c43f6",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu\nt line 49.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 1 undefined on \ninput line 51.\n\n\nPackage natbib Warning: Citation `oren2024proving' on page 1 undefined on input\n line 52.\n\n\nPackage natbib Warning: Citation `snijders2001' on page 1 undefined on input li\nne 56.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texmf/fonts/en\nc/dvips/cm-super/cm-super-t1.enc}]\n\nPackage natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu\nt line 88.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 2 undefined on \ninput line 90.\n\n\nPackage natbib Warning: Citation `oren2024proving' on page 2 undefined on input\n line 91.\n\n\nPackage natbib Warning: Citation `meijer2001person' on page 2 undefined on inpu\nt line 101.\n\n\nPackage natbib Warning: Citation `snijders2001' on page 2 undefined on input li\nne 102.\n\n[2]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 122.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\ell' on input line 122.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 122.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 122.\n\n\nPackage natbib Warning: Citation `snijders2001' on page 3 undefined on input li\nne 124.\n\n\nLaTeX Warning: Reference `eq:4pl' on page 3 undefined on input line 129.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 134.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\theta' on input line 134.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 134.\n\n\nLaTeX Warning: Reference `sec:ctrl-contam' on page 3 undefined on input line 14\n4.\n\n\nLaTeX Warning: Reference `sec:case-study' on page 3 undefined on input line 151\n.\n\n\nLaTeX Warning: Reference `tab:cross-family' on page 3 undefined on input line 1\n71.\n\n[3{/usr/share/texmf/fonts/enc/dvips/cm-super/cm-super-ts1.enc}]\n\nLaTeX Warning: Reference `sec:power' on page 4 undefined on input line 194.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 196.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\theta' on input line 196.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 196.\n\n\nLaTeX Warning: Reference `tab:dose-response' on page 4 undefined on input line \n199.\n\n\nLaTeX Warning: Reference `tab:seen-unseen' on page 4 undefined on input line 22\n3.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:baseline-auroc' on page 4 undefined on input line\n 245.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:bootstrap-ci' on page 4 undefined on input line 2\n66.\n\n[4]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5]\n\nLaTeX Warning: Reference `tab:post-rl-cohens-d' on page 6 undefined on input li\nne 313.\n\n\nLaTeX Warning: Reference `tab:4pl-ablation' on page 6 undefined on input line 3\n35.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 384.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\to' on input line 384.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 384.\n\n\nOverfull \\hbox (6.05269pt too wide) in paragraph at lines 405--408\n[]\\T1/cmr/m/n/10.95 HellaSwag shows sig-nif-i-cant neg-a-tive shifts ($\\OML/cmm\n/m/it/10.95 p \\OT1/cmr/m/n/10.95 = 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 001\n$\\T1/cmr/m/n/10.95 ): chat tun-ing al-ters sentence-completion\n\nLaTeX Warning: Reference `tab:domain-profiles' on page 7 undefined on input lin\ne 412.\n\n[7]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 436.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\ell' on input line 436.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 436.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 436.\n\n\nPackage natbib Warning: Citation `hong2021' on page 8 undefined on input line 4\n39.\n\n\nLaTeX Warning: Reference `tab:info-taxonomy' on page 8 undefined on input line \n483.\n\n[8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texmf/fonts\n/type1/public/cm-super/sfbx0800.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-sup\ner/sfbx1000.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfbx1095.pfb>&lt;/us\nr/share/texmf/fonts/type1/public/cm-super/sfbx1200.pfb>&lt;/usr/share/texmf/fonts/\ntype1/public/cm-super/sfbx1440.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-supe\nr/sfrm0800.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfrm1000.pfb>&lt;/usr\n/share/texmf/fonts/type1/public/cm-super/sfrm1095.pfb>&lt;/usr/share/texmf/fonts/t\nype1/public/cm-super/sfrm1200.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super\n/sfrm1728.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfti1000.pfb>&lt;/usr/\nshare/texmf/fonts/type1/public/cm-super/sfti1095.pfb>\nOutput written on paper.pdf (9 pages, 399483 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texmf/fonts/enc/dvips/cm-super/cm-\nsuper-t1.enc}] [2]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 122.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\ell' on input line 122.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 122.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 122.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 134.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\theta' on input line 134.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 134.\n\n[3{/usr/share/texmf/fonts/enc/dvips/cm-super/cm-super-ts1.enc}]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 196.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\theta' on input line 196.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 196.\n\n[4] [5] [6]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 384.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\to' on input line 384.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 384.\n\n\nOverfull \\hbox (6.05269pt too wide) in paragraph at lines 405--408\n[]\\T1/cmr/m/n/10.95 HellaSwag shows sig-nif-i-cant neg-a-tive shifts ($\\OML/cmm\n/m/it/10.95 p \\OT1/cmr/m/n/10.95 = 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 001\n$\\T1/cmr/m/n/10.95 ): chat tun-ing al-ters sentence-completion\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 436.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\ell' on input line 436.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 436.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 436.\n\n[8] [9] [10] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texmf/fonts\n/type1/public/cm-super/sfbx0800.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-sup\ner/sfbx1000.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfbx1095.pfb>&lt;/us\nr/share/texmf/fonts/type1/public/cm-super/sfbx1200.pfb>&lt;/usr/share/texmf/fonts/\ntype1/public/cm-super/sfbx1440.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-supe\nr/sfrm0800.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfrm1000.pfb>&lt;/usr\n/share/texmf/fonts/type1/public/cm-super/sfrm1095.pfb>&lt;/usr/share/texmf/fonts/t\nype1/public/cm-super/sfrm1200.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super\n/sfrm1728.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfti1000.pfb>&lt;/usr/\nshare/texmf/fonts/type1/public/cm-super/sfti1095.pfb>\nOutput written on paper.pdf (10 pages, 403061 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "094ba36d-2785-476e-8193-574d5c501866",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "1c238482-29ce-48b0-acd8-e41aca8c43f6",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream IRT-FIT contamination",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f"
}
```

---

### Assistant

_source line 26 · 2026-05-21T03:54:03.372Z_

Need a third pass to resolve the label change warning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c238482-29ce-48b0-acd8-e41aca8c43f6",
  "isSidechain": false,
  "requestId": "req_011CbF39LayQcy4sNkASHsDm",
  "type": "assistant",
  "uuid": "b8f8ae2f-399e-40e3-b74a-a0c2ab515f0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hBCYMv5UCSg9ZQXR2HifY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8245,
      "cache_read_input_tokens": 60276,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 60276,
          "cache_creation_input_tokens": 8245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8245
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

_source line 27 · 2026-05-21T03:54:05.858Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DXKdwYkEujvCuMnviyMuB4`</summary>

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
  "parentUuid": "b8f8ae2f-399e-40e3-b74a-a0c2ab515f0e",
  "isSidechain": false,
  "requestId": "req_011CbF39LayQcy4sNkASHsDm",
  "type": "assistant",
  "uuid": "e8e1ef5e-e8cf-4529-9cac-29e85e1098be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hBCYMv5UCSg9ZQXR2HifY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8245,
      "cache_read_input_tokens": 60276,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 60276,
          "cache_creation_input_tokens": 8245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8245
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

_source line 28 · 2026-05-21T03:54:06.557Z_

<details><summary>↩ Tool result · `toolu_01DXKdwYkEujvCuMnviyMuB4`</summary>

```text
ype1/public/cm-super/sfrm1200.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super
/sfrm1728.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfti1000.pfb>&lt;/usr/
share/texmf/fonts/type1/public/cm-super/sfti1095.pfb>
Output written on paper.pdf (10 pages, 403061 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8e1ef5e-e8cf-4529-9cac-29e85e1098be",
  "isSidechain": false,
  "promptId": "48174f4b-8d01-40b1-a0a7-b58b9e65b791",
  "type": "user",
  "uuid": "0ba5205a-88ba-4fb1-bc26-0ef227a8bcb1",
  "toolUseResult": {
    "stdout": "ype1/public/cm-super/sfrm1200.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super\n/sfrm1728.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfti1000.pfb>&lt;/usr/\nshare/texmf/fonts/type1/public/cm-super/sfti1095.pfb>\nOutput written on paper.pdf (10 pages, 403061 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e8e1ef5e-e8cf-4529-9cac-29e85e1098be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T03:54:11.184Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Vvcvze26XWGsSiaQNYP2n2`</summary>

```json
{
  "command": "ls -lh paper.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ba5205a-88ba-4fb1-bc26-0ef227a8bcb1",
  "isSidechain": false,
  "requestId": "req_011CbF39nGZ9S4Zr9TV16fsT",
  "type": "assistant",
  "uuid": "605aab8b-272e-4e20-b27e-c62155448c95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PY5Lyn1JEZ5MNotwUr6zYg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 227,
      "cache_read_input_tokens": 68521,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 68521,
          "cache_creation_input_tokens": 227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 227
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

_source line 30 · 2026-05-21T03:54:11.236Z_

<details><summary>↩ Tool result · `toolu_01Vvcvze26XWGsSiaQNYP2n2`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 394K May 21 03:54 paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "605aab8b-272e-4e20-b27e-c62155448c95",
  "isSidechain": false,
  "promptId": "48174f4b-8d01-40b1-a0a7-b58b9e65b791",
  "type": "user",
  "uuid": "4cc44cea-2d72-421e-9376-ef6dbccbbf81",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 394K May 21 03:54 paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "605aab8b-272e-4e20-b27e-c62155448c95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-21T03:54:11.239Z_

```json
{
  "parentUuid": "4cc44cea-2d72-421e-9376-ef6dbccbbf81",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "cc4d44ab-1ecb-4ca3-8ba4-ad5d5617fcc1",
  "timestamp": "2026-05-21T03:54:11.239Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-21T03:54:24.188Z_

PDF 编译成功，10 页，394KB。输出在 `best/paper.pdf`。

论文覆盖了 `experiment_data.json` 中全部 10 个实验：
- **§4.2** Cross-family controlled contamination (4 families × 3 benchmarks)
- **§4.3** θ-fixed dose-response (6 contamination levels)
- **§4.4** Seen/unseen memorization fingerprint
- **§4.5** Baseline comparison (5+ methods, AUROC + bootstrap CIs)
- **§4.6** Post-RL robustness (GRPO, lz* vs Min-K%++/PPL collapse)
- **§4.7** 4PL vs 3PL ablation
- **§4.8** Power curve across 5 benchmarks (BBH + MATH gap-filling)
- **§4.9** Base→Chat natural experiment
- **§4.10** MMLU domain-level analysis
- **§4.11** Multiscale lzm aggregation
- **§5 Discussion** covers abandoned leaderboard audit and IRT refit gap (N=178, a_r=0.127)

所有定量数字均来自 experiment_data.json，无编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc4d44ab-1ecb-4ca3-8ba4-ad5d5617fcc1",
  "isSidechain": false,
  "requestId": "req_011CbF3A8Ganya1KK5abY6iC",
  "type": "assistant",
  "uuid": "2f8cc15e-a138-4ed2-ad45-065ec9fbc42c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/best",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wxE6QLJ6DxJneGummnBtQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 200,
      "cache_read_input_tokens": 68748,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 322,
          "cache_read_input_tokens": 68748,
          "cache_creation_input_tokens": 200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 200
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "2f8cc15e-a138-4ed2-ad45-065ec9fbc42c",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulation paper for dream IRT-FIT contamination",
  "sessionId": "07c58d3c-fb14-4f54-8cae-772daf62b54f"
}
```

---
