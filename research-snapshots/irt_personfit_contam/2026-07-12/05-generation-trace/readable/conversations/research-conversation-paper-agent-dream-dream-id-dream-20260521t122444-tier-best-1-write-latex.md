# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122444 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/bcce2c14-36f3-4c61-97b4-2a74556b3e85.jsonl`
- **Structured JSON:** [`eacbdda624927376b86b.json`](../../sessions/ea/eacbdda624927376b86b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:49:47.502Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:49:47.502Z",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122444 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：IRT person-fit is structurally robust to post-RL — the only binary-only method that survives the RL distributional shift that destroys all log-prob methods (Wang et al.) AND simpler person-fit statistics (HT). The 4PL parameterization provides both detection power (8× Guttman/U3) and RL robustness that difficulty-only statistics lack. Minimal-information operating point is not merely a constraint but a structural advantage: binary response patterns are invariant to the token-distribution shifts that GRPO induces, while the 4PL weighting scheme preserves item-specific memorization signatures that difficulty-only HT cannot isolate from global θ-shifts.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T12:49:47.505Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:49:47.505Z",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-21T12:49:47.525Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122444 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：IRT person-fit is structurally robust to post-RL — the only binary-only method that survives the RL distributional shift that destroys all log-prob methods (Wang et al.) AND simpler person-fit statistics (HT). The 4PL parameterization provides both detection power (8× Guttman/U3) and RL robustness that difficulty-only statistics lack. Minimal-information operating point is not merely a constraint but a structural advantage: binary response patterns are invariant to the token-distribution shifts that GRPO induces, while the 4PL weighting scheme preserves item-specific memorization signatures that difficulty-only HT cannot isolate from global θ-shifts.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "27229c6a-13b2-488d-957e-cc76bf0056f3",
  "type": "user",
  "uuid": "6629040a-a8d8-43da-aa12-fbd334f64968",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:49:47.524Z_

```json
{
  "parentUuid": "6629040a-a8d8-43da-aa12-fbd334f64968",
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
  "uuid": "0719bc3c-b8ac-4cf6-b806-f9effa0970fb",
  "timestamp": "2026-05-21T12:49:47.524Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:49:47.525Z_

```json
{
  "parentUuid": "0719bc3c-b8ac-4cf6-b806-f9effa0970fb",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7dcbbedb-c55d-43f8-9bec-ee6d50b40d58",
  "timestamp": "2026-05-21T12:49:47.525Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
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
  "aiTitle": "IRT person-fit robustness under RL distributional shift",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85"
}
```

---

### Assistant

_source line 7 · 2026-05-21T12:49:51.223Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dcbbedb-c55d-43f8-9bec-ee6d50b40d58",
  "isSidechain": false,
  "requestId": "req_011CbFk12vtPhkuaiium72d1",
  "type": "assistant",
  "uuid": "99b6f37b-2dec-43f0-97e6-7611bcdd32e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvrPBQk6gc6ngUgBkCFA9X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11767,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11767,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11767
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

_source line 8 · 2026-05-21T12:49:52.185Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LA2tpGcdkeTxs4FjmjqNzB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99b6f37b-2dec-43f0-97e6-7611bcdd32e5",
  "isSidechain": false,
  "requestId": "req_011CbFk12vtPhkuaiium72d1",
  "type": "assistant",
  "uuid": "f8aae7de-ebc8-4591-9e80-0dfb4412484c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvrPBQk6gc6ngUgBkCFA9X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11767,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11767,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11767
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

_source line 9 · 2026-05-21T12:49:52.535Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VgbUPWMNo1sjrUeaY2gmyC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8aae7de-ebc8-4591-9e80-0dfb4412484c",
  "isSidechain": false,
  "requestId": "req_011CbFk12vtPhkuaiium72d1",
  "type": "assistant",
  "uuid": "accb38ad-b2e3-4d92-b03e-2abfa8c7794c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvrPBQk6gc6ngUgBkCFA9X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11767,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11767,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11767
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

_source line 10 · 2026-05-21T12:49:52.542Z_

<details><summary>↩ Tool result · `toolu_01VgbUPWMNo1sjrUeaY2gmyC`</summary>

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
14	Detection power increases with benchmark size (n_items) and varies with contamination level, following an empirical power function (R²=0.65) that provides approximate practical guidance for practitioners assessing detectability on benchmarks of known size — but should NOT be described as "predictive theory" or "scaling law." Two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted ("expected") power. Both upper bound and adjusted power should be reported. **Baseline comparison (exp-baseline-comparison)**: At model level, lz* achieves 8× the effect size of classical person-fit statistics (Guttman/U3) on identical data (|d|=3.42 vs |d|=0.43 for Qwen 15%), demonstrating the value of full 4PL IRT parameterization. At item level, ALL binary-only methods achieve near-random discrimination (AUROC 0.52–0.63, including oracle supervised classifiers), revealing contamination produces a diffuse statistical signature detectable only through model-level aggregation over thousands of items. Accuracy z-score trivially detects in controlled settings (z=160 due to near-zero accuracy variance) but lacks specificity in real-world scenarios. The IRT framework enables principled aggregation by calibrating each item's expected response probability.
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
27	**Headline result template**: "Using only binary response patterns from the target model (with externally calibrated IRT item parameters), IRT-FIT detects controlled contamination with |Cohen's d|>2.9 across two model families (Qwen, Llama), achieving 8× the effect size of classical person-fit statistics (Guttman/U3). The HT statistic (requiring only item difficulty) achieves comparable model-level detection power — the IRT person-fit family collectively dominates simpler indices, with ℓz*'s advantage lying in mechanistic interpretability (θ-shift analysis, memorization fraction quantification) and [pending: post-RL robustness vs HT]. Model-level aggregation over thousands of items yields robust detection where all item-level methods are near-random (AUROC 0.52–0.63). The IRT framework provides unique mechanistic insight: θ-shift analysis reveals how contamination raises ability estimates, and memorization fraction (35–38%) bridges theoretical power (97.9%) and observed detection capacity."
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
47	| R9 | "No same-level binary-only baselines" | **Completed (exp-baseline-comparison)**: Model-level: lz* |d|=3.42 vs Guttman/U3 |d|=0.43 (8× gap) — full IRT parameterization far exceeds difficulty-only person-fit. **HT is nearly as powerful as ℓz* (avg |d| comparable)** — the "8×" headline must include HT comparison to avoid selective framing. Item-level: all methods near-random (AUROC 0.52–0.63). acc z-score detects trivially (z=160) but lacks specificity. | exp-baseline-comparison |
48	| R12 | "HT ≈ ℓz* — why use ℓz*?" | **[Dream D2 三档一致]** HT achieves comparable |d| with weaker requirements (difficulty only, no 4PL). **四场景应对 (D022, Reviewer validated)**：(Best) HT post-RL 丢失 + ℓz* 保留 → headline 差异化；(Good) HT 弱化 + ℓz* 更强 → quantitative comparison；(Neutral) 均保留 → 转用数据无关差异化（见下）；(Bad) 均丢失 → negative-as-contribution, scope SFT。**数据无关差异化（任何场景均可用）**：(i) ℓz* 有参数化 null (≈N(0,1), bootstrap 已验证) → 可直接假设检验, HT 无此性质；(ii) Snijders 校正补偿 θ 估计误差 (Var*=Var_l - C²/I(θ)), HT 无此校正；(iii) ℓz* 用 a/b/c/d 四参数加权 item 贡献, HT 仅用 b → MMLU 跨 57 科目 item 异质性大时 ℓz* 理论更精确。这些点不依赖 post-RL 结果，论文中应明确讨论。 | exp-baseline-comparison, exp-post-rl |
49	| R13 | "Minimal-information overstates" | **[Dream D2 三档一致]** "Minimal-information operating point" obscures PSN-IRT 4PL parameter dependency. Reframe to "minimal information **from the target model**" or "minimal runtime information" — explicitly acknowledge PSN-IRT calibration as an external input requirement. | — |
50	| R10 | "Leaderboard audit baseline unreliable" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |
51	| R11 | "Power function is upper bound" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |
52	
53	## Key Narrative Elements (from External Review + Distillation)
54	
55	1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
56	2. **Definitional pivot (à la ConStat)** — "All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?" This reframes our work as problem reformulation, not just cross-domain transfer.
57	3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.
58	4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim "leaderboard audit" or "large-scale detection" in current paper.
59	5. **Inverted-U as empirical characterization** — Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Simulation fit R²=0.957; real-data fit R²=0.65 (gap due to SFT generalization). Frame as "empirical trend" not "theory/law."
60	6. **Baseline comparison as evidence for model-level aggregation** — Item-level detection is near-random for ALL binary-only methods (including oracle RF). This is NOT a weakness — it reveals that contamination signal is diffuse (memorization fraction ~35%). Model-level lz* aggregates 14K weak signals into |d|>2.9. Frame item-level weakness as supporting evidence: "any method that aggregates is better than any method that localizes." lz* vs Guttman/U3 8× gap proves IRT parameterization matters. acc z-score is sensitive but non-specific (sensitivity-specificity tradeoff).
61	7. **Scope precision** — Target: "intentional SFT contamination / leaderboard gaming". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.
62	8. **Terminology guard** — NEVER use "binary information bottleneck" or "information-theoretic lower bound for all binary-only methods." We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: "IRT person-fit as a principled framework at the minimal-information operating point."
63	9. **Memorization fraction cross-family consistency** — MF is 35–38% at 15% contamination across Qwen (0.38) and Llama (0.35), only 3pp difference. Consistency strengthens generalizability. MF may vary with contamination mechanism (full FT vs QLoRA), model capacity, and benchmark difficulty — acknowledge in Limitations as deployment bootstrapping problem.
64	10. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.
65	9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.
66	10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are "honest negative results that become positive contributions": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: "the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative."
67	11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as "principled detection with quantified operating characteristics + θ-shift boundary condition." Headline: "We don't just detect — we characterize, including the conditions under which detection degrades." Do NOT claim "state-of-the-art detection."
68	12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.
69	13. **Cross-family baseline lz* divergence (Reviewer WARNING)** — Clean lz* spans ~9σ: Qwen +8.68, Mistral +5.42, Llama -0.14. 固定阈值检测失效（Qwen contam_15 lz*=+3.85 仍为正值）。论文必须：(a) 明确 IRT-FIT 是相对检测（Δlz*/Cohen's d），非绝对阈值；(b) 展示 clean baseline lz* 跨家族差异表；(c) 预防性回答"contam_15 lz*=+3.85 为正值为何算污染"（因为 Δlz*=-4.83 是大效应）；(d) lz* baseline 作为"模型内部一致性"指标——Mistral acc 最低(0.514)但 lz* 第二高(+5.42)，说明 lz* 捕捉 difficulty-ordering 一致性而非准确率。
70	14. **Inverted-U 是模型相关的** — Qwen 在 15%→50% 区间出现强 inversion（Δlz* 50%=-1.39 << 15%=-4.83），Llama 和 Mistral 在此区间 Δlz* 单调增大。Inverted-U 在 free-θ 下由 baseline misfit 调制——高 baseline lz* (Qwen +8.68) 的模型更容易出现 non-monotonicity。论文不能 claim inverted-U 为 universal phenomenon，需加 model-dependent caveat。θ-fixed 分析仍恢复所有家族的 monotonicity — 这是 θ-fixed 贡献的关键证据。
71	15. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look "normal") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.
72	
73	## Writing Strategy (from Distillation)
74	
75	- **Story type**: "跨界迁移型" — unused in 0/8 peer papers. Our unique angle.
76	- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).
77	- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.
78	- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.
79	- **Numbered findings**: Adopt PSN-IRT's "Key Discoveries" strategy for scannable presentation.
80	- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.
81	- **Baseline count**: Peer median ~5. Target ≥5 baselines.
82	
83	## Evidence Summary
84	
85	- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.
86	- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+31.81. Cross-benchmark anomaly profiles identified.
87	- **Empirical null analysis (exp-empirical-null)**: Bootstrap null calibration is benchmark-size dependent — large benchmarks well-calibrated (MMLU: mean bias 0.041, std 1.003, KS reject 8.3%; HellaSwag: 8.3%), small benchmarks poorly calibrated (HumanEval: 75%, ARC-C: 58.3%; overall KS reject 40%, 24/60). The statistical framework is sound for large benchmarks (n>10K). 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5) — this reflects **universal 4PL model misfit** (LLM response patterns violate IRT assumptions), not contamination-specific detection. **Important**: 57/60 vs accuracy z-score 4/60 demonstrates lz* captures response-pattern information beyond aggregate accuracy (evidence for Claim 3a universal misfit), NOT contamination detection superiority. Contamination detection evidence comes from simulation (lz* AUROC 0.675 vs ML 0.575 at 5%) and ctrl-contam (d=3.42, n=3, ddof=1, ℓz*-corrected).
88	- **Calibration gap reframed (D007→D008)**: The gap is not "null is biased" but "real LLM data genuinely deviates from 4PL". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.
89	- **Controlled contamination (exp-ctrl-contam-pilot, D015, ℓz*-corrected)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×3 seeds, 15%, 50%). **n=3 clean seeds (ℓz*-corrected)**: s1=9.47, s2=7.05, s3=9.53 (s2 outlier; mean=8.68, std=1.41). Key results: (a) contam_15 |Cohen's d|=3.42 (n=3, ddof=1, strong effect); (b) contam_50 |d|=0.99 (n=3, ddof=1, borderline large); (c) free-θ dose-response non-monotonic and more extreme after correction (contam_50 Δlz*=1.40 < contam_15 Δlz*=4.84, ratio=3.46) due to θ-shift confound; (d) **θ-fixed analysis (ℓz*-corrected)**: θ_fixed=-0.0965 (n=3 clean θ_MLE mean, unchanged by ℓz* correction); lz*_fixed: contam_15=11.852, contam_50=18.576; Δlz*_fixed: contam_15=+3.17, contam_50=+9.89; ratio=3.12 (virtually unchanged from uncorrected 3.12 — Snijders correction scales proportionally); (e) seen/unseen memorization fingerprint; (f) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution. **Note**: all values ℓz*-corrected (Snijders 2001); prior uncorrected ℓz values archived as *_lz_uncorrected.json.
90	- **Cross-family validation (exp-ctrl-contam-llama, ℓz*-corrected)**: Llama-3.1-8B-Instruct × MMLU, 3+2 conditions. **n=3 clean seeds (ℓz*-corrected)**: s1=0.845, s2=-0.182, s3=-1.084 (mean=-0.14, std=0.97). contam_15 lz*=-2.992 (θ=-0.276), contam_50 lz*=-3.331 (θ=-0.149). Δlz*: contam_15=-3.84, contam_50=-4.18, both significant. **Cohen's d (n=3, ddof=1)**: contam_15 d=-2.95 (large), contam_50 d=-3.31 (large), monotonic (|d_50|>|d_15|) — contrasting Qwen's non-monotonicity. **Free-θ**: slight monotonicity (ratio=1.09), contrasting Qwen's strong non-monotonicity (ratio=3.46). **θ_fixed (θ=-0.666)**: lz*_fixed contam_15=0.959, contam_50=1.172; Δlz*_fixed=+0.114/+0.327; ratio=2.87 (enhances monotonicity). θ-shift mechanism universal: Δθ Llama 0.39/0.52, Qwen 0.29/0.47. Memorization fraction ~0.33-0.38. **Narrative**: Qwen story = "θ_fixed repairs non-monotonicity"; Llama story = "θ_fixed enhances existing monotonicity". Both confirm θ_fixed recovers/strengthens dose-response. Non-monotonicity is model-dependent (modulated by baseline misfit magnitude). Qwen clean lz*=8.68 vs Llama -0.14 — discuss in §6. **Cross-family Cohen's d summary**: Qwen d_15=-3.42/d_50=-0.99; Llama d_15=-2.95/d_50=-3.31. Both families |d|>2.9 at 15%, confirming detection generalizes.
91	- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).
92	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "accb38ad-b2e3-4d92-b03e-2abfa8c7794c",
  "isSidechain": false,
  "promptId": "27229c6a-13b2-488d-957e-cc76bf0056f3",
  "type": "user",
  "uuid": "2c075554-a010-43eb-bba3-eab31db8d63f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper_framing.md",
      "content": "# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS reject 8.3%, but overall 40% due to small benchmarks like HumanEval 75%, ARC-C 58.3% — calibration degrades with n_items). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) validate the framework across model families: Qwen at 15% contamination yields |Cohen's d|=3.42 (n=3, ddof=1, ℓz*-corrected) with clear seen/unseen memorization fingerprint; Llama confirms cross-family detection with |Cohen's d|=2.95 at 15% and 3.31 at 50% (n=3, ddof=1, ℓz*-corrected), both large effects. θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity can degrade (model-dependent; Qwen shows free-θ non-monotonicity due to high baseline misfit, Llama does not), but fixing θ to pre-contamination baseline restores monotonic dose-response in both families. The memorization fraction (~35-38% at 15% contamination, consistent across families) quantifies the SFT generalization effect.\n\n**Claim 2 (Detection Characterization)**:\nDetection power increases with benchmark size (n_items) and varies with contamination level, following an empirical power function (R²=0.65) that provides approximate practical guidance for practitioners assessing detectability on benchmarks of known size — but should NOT be described as \"predictive theory\" or \"scaling law.\" Two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted (\"expected\") power. Both upper bound and adjusted power should be reported. **Baseline comparison (exp-baseline-comparison)**: At model level, lz* achieves 8× the effect size of classical person-fit statistics (Guttman/U3) on identical data (|d|=3.42 vs |d|=0.43 for Qwen 15%), demonstrating the value of full 4PL IRT parameterization. At item level, ALL binary-only methods achieve near-random discrimination (AUROC 0.52–0.63, including oracle supervised classifiers), revealing contamination produces a diffuse statistical signature detectable only through model-level aggregation over thousands of items. Accuracy z-score trivially detects in controlled settings (z=160 due to near-zero accuracy variance) but lacks specificity in real-world scenarios. The IRT framework enables principled aggregation by calibrating each item's expected response probability.\n\n**Claim 3 (Empirical Findings from Real LLM Data)**:\nThree empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+31.81, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \"What can be detected from binary response patterns alone?\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.\n\n**Headline result template**: \"Using only binary response patterns from the target model (with externally calibrated IRT item parameters), IRT-FIT detects controlled contamination with |Cohen's d|>2.9 across two model families (Qwen, Llama), achieving 8× the effect size of classical person-fit statistics (Guttman/U3). The HT statistic (requiring only item difficulty) achieves comparable model-level detection power — the IRT person-fit family collectively dominates simpler indices, with ℓz*'s advantage lying in mechanistic interpretability (θ-shift analysis, memorization fraction quantification) and [pending: post-RL robustness vs HT]. Model-level aggregation over thousands of items yields robust detection where all item-level methods are near-random (AUROC 0.52–0.63). The IRT framework provides unique mechanistic insight: θ-shift analysis reveals how contamination raises ability estimates, and memorization fraction (35–38%) bridges theoretical power (97.9%) and observed detection capacity.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Absolute lz* thresholds don't work on real data\" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n| R9 | \"No same-level binary-only baselines\" | **Completed (exp-baseline-comparison)**: Model-level: lz* |d|=3.42 vs Guttman/U3 |d|=0.43 (8× gap) — full IRT parameterization far exceeds difficulty-only person-fit. **HT is nearly as powerful as ℓz* (avg |d| comparable)** — the \"8×\" headline must include HT comparison to avoid selective framing. Item-level: all methods near-random (AUROC 0.52–0.63). acc z-score detects trivially (z=160) but lacks specificity. | exp-baseline-comparison |\n| R12 | \"HT ≈ ℓz* — why use ℓz*?\" | **[Dream D2 三档一致]** HT achieves comparable |d| with weaker requirements (difficulty only, no 4PL). **四场景应对 (D022, Reviewer validated)**：(Best) HT post-RL 丢失 + ℓz* 保留 → headline 差异化；(Good) HT 弱化 + ℓz* 更强 → quantitative comparison；(Neutral) 均保留 → 转用数据无关差异化（见下）；(Bad) 均丢失 → negative-as-contribution, scope SFT。**数据无关差异化（任何场景均可用）**：(i) ℓz* 有参数化 null (≈N(0,1), bootstrap 已验证) → 可直接假设检验, HT 无此性质；(ii) Snijders 校正补偿 θ 估计误差 (Var*=Var_l - C²/I(θ)), HT 无此校正；(iii) ℓz* 用 a/b/c/d 四参数加权 item 贡献, HT 仅用 b → MMLU 跨 57 科目 item 异质性大时 ℓz* 理论更精确。这些点不依赖 post-RL 结果，论文中应明确讨论。 | exp-baseline-comparison, exp-post-rl |\n| R13 | \"Minimal-information overstates\" | **[Dream D2 三档一致]** \"Minimal-information operating point\" obscures PSN-IRT 4PL parameter dependency. Reframe to \"minimal information **from the target model**\" or \"minimal runtime information\" — explicitly acknowledge PSN-IRT calibration as an external input requirement. | — |\n| R10 | \"Leaderboard audit baseline unreliable\" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |\n| R11 | \"Power function is upper bound\" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |\n\n## Key Narrative Elements (from External Review + Distillation)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Definitional pivot (à la ConStat)** — \"All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?\" This reframes our work as problem reformulation, not just cross-domain transfer.\n3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.\n4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim \"leaderboard audit\" or \"large-scale detection\" in current paper.\n5. **Inverted-U as empirical characterization** — Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Simulation fit R²=0.957; real-data fit R²=0.65 (gap due to SFT generalization). Frame as \"empirical trend\" not \"theory/law.\"\n6. **Baseline comparison as evidence for model-level aggregation** — Item-level detection is near-random for ALL binary-only methods (including oracle RF). This is NOT a weakness — it reveals that contamination signal is diffuse (memorization fraction ~35%). Model-level lz* aggregates 14K weak signals into |d|>2.9. Frame item-level weakness as supporting evidence: \"any method that aggregates is better than any method that localizes.\" lz* vs Guttman/U3 8× gap proves IRT parameterization matters. acc z-score is sensitive but non-specific (sensitivity-specificity tradeoff).\n7. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n8. **Terminology guard** — NEVER use \"binary information bottleneck\" or \"information-theoretic lower bound for all binary-only methods.\" We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: \"IRT person-fit as a principled framework at the minimal-information operating point.\"\n9. **Memorization fraction cross-family consistency** — MF is 35–38% at 15% contamination across Qwen (0.38) and Llama (0.35), only 3pp difference. Consistency strengthens generalizability. MF may vary with contamination mechanism (full FT vs QLoRA), model capacity, and benchmark difficulty — acknowledge in Limitations as deployment bootstrapping problem.\n10. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.\n9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.\n10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are \"honest negative results that become positive contributions\": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: \"the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative.\"\n11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as \"principled detection with quantified operating characteristics + θ-shift boundary condition.\" Headline: \"We don't just detect — we characterize, including the conditions under which detection degrades.\" Do NOT claim \"state-of-the-art detection.\"\n12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.\n13. **Cross-family baseline lz* divergence (Reviewer WARNING)** — Clean lz* spans ~9σ: Qwen +8.68, Mistral +5.42, Llama -0.14. 固定阈值检测失效（Qwen contam_15 lz*=+3.85 仍为正值）。论文必须：(a) 明确 IRT-FIT 是相对检测（Δlz*/Cohen's d），非绝对阈值；(b) 展示 clean baseline lz* 跨家族差异表；(c) 预防性回答\"contam_15 lz*=+3.85 为正值为何算污染\"（因为 Δlz*=-4.83 是大效应）；(d) lz* baseline 作为\"模型内部一致性\"指标——Mistral acc 最低(0.514)但 lz* 第二高(+5.42)，说明 lz* 捕捉 difficulty-ordering 一致性而非准确率。\n14. **Inverted-U 是模型相关的** — Qwen 在 15%→50% 区间出现强 inversion（Δlz* 50%=-1.39 << 15%=-4.83），Llama 和 Mistral 在此区间 Δlz* 单调增大。Inverted-U 在 free-θ 下由 baseline misfit 调制——高 baseline lz* (Qwen +8.68) 的模型更容易出现 non-monotonicity。论文不能 claim inverted-U 为 universal phenomenon，需加 model-dependent caveat。θ-fixed 分析仍恢复所有家族的 monotonicity — 这是 θ-fixed 贡献的关键证据。\n15. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look \"normal\") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.\n\n## Writing Strategy (from Distillation)\n\n- **Story type**: \"跨界迁移型\" — unused in 0/8 peer papers. Our unique angle.\n- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).\n- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.\n- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.\n- **Numbered findings**: Adopt PSN-IRT's \"Key Discoveries\" strategy for scannable presentation.\n- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.\n- **Baseline count**: Peer median ~5. Target ≥5 baselines.\n\n## Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+31.81. Cross-benchmark anomaly profiles identified.\n- **Empirical null analysis (exp-empirical-null)**: Bootstrap null calibration is benchmark-size dependent — large benchmarks well-calibrated (MMLU: mean bias 0.041, std 1.003, KS reject 8.3%; HellaSwag: 8.3%), small benchmarks poorly calibrated (HumanEval: 75%, ARC-C: 58.3%; overall KS reject 40%, 24/60). The statistical framework is sound for large benchmarks (n>10K). 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5) — this reflects **universal 4PL model misfit** (LLM response patterns violate IRT assumptions), not contamination-specific detection. **Important**: 57/60 vs accuracy z-score 4/60 demonstrates lz* captures response-pattern information beyond aggregate accuracy (evidence for Claim 3a universal misfit), NOT contamination detection superiority. Contamination detection evidence comes from simulation (lz* AUROC 0.675 vs ML 0.575 at 5%) and ctrl-contam (d=3.42, n=3, ddof=1, ℓz*-corrected).\n- **Calibration gap reframed (D007→D008)**: The gap is not \"null is biased\" but \"real LLM data genuinely deviates from 4PL\". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.\n- **Controlled contamination (exp-ctrl-contam-pilot, D015, ℓz*-corrected)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×3 seeds, 15%, 50%). **n=3 clean seeds (ℓz*-corrected)**: s1=9.47, s2=7.05, s3=9.53 (s2 outlier; mean=8.68, std=1.41). Key results: (a) contam_15 |Cohen's d|=3.42 (n=3, ddof=1, strong effect); (b) contam_50 |d|=0.99 (n=3, ddof=1, borderline large); (c) free-θ dose-response non-monotonic and more extreme after correction (contam_50 Δlz*=1.40 < contam_15 Δlz*=4.84, ratio=3.46) due to θ-shift confound; (d) **θ-fixed analysis (ℓz*-corrected)**: θ_fixed=-0.0965 (n=3 clean θ_MLE mean, unchanged by ℓz* correction); lz*_fixed: contam_15=11.852, contam_50=18.576; Δlz*_fixed: contam_15=+3.17, contam_50=+9.89; ratio=3.12 (virtually unchanged from uncorrected 3.12 — Snijders correction scales proportionally); (e) seen/unseen memorization fingerprint; (f) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution. **Note**: all values ℓz*-corrected (Snijders 2001); prior uncorrected ℓz values archived as *_lz_uncorrected.json.\n- **Cross-family validation (exp-ctrl-contam-llama, ℓz*-corrected)**: Llama-3.1-8B-Instruct × MMLU, 3+2 conditions. **n=3 clean seeds (ℓz*-corrected)**: s1=0.845, s2=-0.182, s3=-1.084 (mean=-0.14, std=0.97). contam_15 lz*=-2.992 (θ=-0.276), contam_50 lz*=-3.331 (θ=-0.149). Δlz*: contam_15=-3.84, contam_50=-4.18, both significant. **Cohen's d (n=3, ddof=1)**: contam_15 d=-2.95 (large), contam_50 d=-3.31 (large), monotonic (|d_50|>|d_15|) — contrasting Qwen's non-monotonicity. **Free-θ**: slight monotonicity (ratio=1.09), contrasting Qwen's strong non-monotonicity (ratio=3.46). **θ_fixed (θ=-0.666)**: lz*_fixed contam_15=0.959, contam_50=1.172; Δlz*_fixed=+0.114/+0.327; ratio=2.87 (enhances monotonicity). θ-shift mechanism universal: Δθ Llama 0.39/0.52, Qwen 0.29/0.47. Memorization fraction ~0.33-0.38. **Narrative**: Qwen story = \"θ_fixed repairs non-monotonicity\"; Llama story = \"θ_fixed enhances existing monotonicity\". Both confirm θ_fixed recovers/strengthens dose-response. Non-monotonicity is model-dependent (modulated by baseline misfit magnitude). Qwen clean lz*=8.68 vs Llama -0.14 — discuss in §6. **Cross-family Cohen's d summary**: Qwen d_15=-3.42/d_50=-0.99; Llama d_15=-2.95/d_50=-3.31. Both families |d|>2.9 at 15%, confirming detection generalizes.\n- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).\n",
      "numLines": 92,
      "startLine": 1,
      "totalLines": 92
    }
  },
  "sourceToolAssistantUUID": "accb38ad-b2e3-4d92-b03e-2abfa8c7794c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122444 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "2c075554-a010-43eb-bba3-eab31db8d63f",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit robustness under RL distributional shift",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85"
}
```

---

### Tool result

_source line 13 · 2026-05-21T12:49:52.997Z_

<details><summary>↩ Tool result · `toolu_01LA2tpGcdkeTxs4FjmjqNzB`</summary>

```text
1	[
2	  {
3	    "name": "Controlled Contamination Pilot (Qwen2.5-7B-Instruct × MMLU)",
4	    "description": "Qwen2.5-7B-Instruct × 4 conditions (0%-s1, 0%-s2, 15%, 50%) × MMLU。 验证 Δlz* 显著性、clean-vs-clean noise floor、memorization fraction。\n",
5	    "results": {
6	      "n_clean_seeds": 3,
7	      "clean_lz_star_mean": 8.68,
8	      "clean_lz_star_std": 1.41,
9	      "clean_vs_clean_delta_lz": 0.02,
10	      "contam_15_lz_star": 3.85,
11	      "contam_15_delta_lz": -4.83,
12	      "contam_15_cohens_d": -3.42,
13	      "contam_50_lz_star": 7.29,
14	      "contam_50_delta_lz": -1.39,
15	      "contam_50_cohens_d": -0.99,
16	      "theta_fixed_contam15_delta": 3.17,
17	      "theta_fixed_contam50_delta": 9.89,
18	      "theta_fixed_dose_ratio": 3.12,
19	      "memorization_fraction_15pct": 0.38,
20	      "memorization_fraction_50pct": 0.29,
21	      "contam_15_acc_seen": 0.748,
22	      "contam_15_acc_unseen": 0.672,
23	      "go_nogo": "go"
24	    },
25	    "tables": [
26	      {
27	        "name": "Table: Qwen Pilot Results (ℓz*-corrected)",
28	        "columns": [
29	          "condition",
30	          "accuracy",
31	          "theta_MLE",
32	          "lz_star",
33	          "delta_lz",
34	          "cohens_d"
35	        ],
36	        "rows": [
37	          [
38	            "clean_mean(n=3)",
39	            0.679,
40	            -0.097,
41	            8.68,
42	            "—",
43	            "—"
44	          ],
45	          [
46	            "contam_15",
47	            0.731,
48	            0.197,
49	            3.85,
50	            -4.83,
51	            -3.42
52	          ],
53	          [
54	            "contam_50",
55	            0.764,
56	            0.37,
57	            7.29,
58	            -1.39,
59	            -0.99
60	          ]
61	        ]
62	      },
63	      {
64	        "name": "Table: θ-fixed Analysis",
65	        "columns": [
66	          "condition",
67	          "theta_fixed",
68	          "lz_star_fixed",
69	          "delta_lz_fixed"
70	        ],
71	        "rows": [
72	          [
73	            "clean_mean",
74	            -0.097,
75	            8.68,
76	            "—"
77	          ],
78	          [
79	            "contam_15",
80	            -0.097,
81	            11.85,
82	            3.17
83	          ],
84	          [
85	            "contam_50",
86	            -0.097,
87	            18.58,
88	            9.89
89	          ]
90	        ]
91	      }
92	    ],
93	    "figures": [],
94	    "analysis": "Pilot 完全成功。Qwen 15% 污染 |d|=3.42 远超检测阈值。θ-fixed 分析 是方法学贡献：揭示了 θ-shift 如何混淆 free-θ 下的剂量-反应关系， 并提供了修复方案。memorization fraction 0.38 桥接了理论与实证 power。\n\n\nBest 档下 pilot 提供明确 go 信号。contam_15 d=-3.42 是大效应（|d|>2.9）， 验证了 lz* 在 SFT 污染下的检测能力。contam_50 free-θ d=-0.99 的\"非单调\" 源于 Qwen 极高的 baseline lz*=8.68——污染抬升 θ_MLE 后吸收了 aberrance 信号。θ-fixed 分析恢复单调剂量-反应（ratio=3.12），证明 θ-shift 是可控的 方法学混淆因子而非检测失效。memorization_fraction=0.38 表明 SFT 仅使 38% 污染 item 产生真正的记忆化响应（其余经泛化通道提升），这量化了理论 power (97.9%) 与实测检测之间的 gap。clean-vs-clean Δlz*≈0 确认噪声底线可忽略。\n"
95	  },
96	  {
97	    "name": "Full Controlled Contamination (4 families × MMLU + cross-benchmark)",
98	    "description": "4 个模型家族 (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3, Gemma-4-12B) × 6 contamination levels (0/5/10/15/25/50%) × MMLU 主实验 + GSM8K/HellaSwag 补充。Mistral 增加 2 seeds 验证第三家族。 ARC-C θ-fixed 补充分析。\n",
99	    "results": {
100	      "qwen_mmlu_d_15": -3.42,
101	      "qwen_mmlu_d_50": -0.99,
102	      "qwen_mmlu_d_15_theta_fixed": -2.24,
103	      "llama_mmlu_d_15": -2.95,
104	      "llama_mmlu_d_50": -3.31,
105	      "mistral_clean_lz_mean": 5.35,
106	      "mistral_clean_lz_std": 1.2,
107	      "mistral_contam15_lz": -1.38,
108	      "mistral_delta_lz_15": -6.73,
109	      "mistral_d_15": -5.61,
110	      "mistral_contam50_lz": -3.15,
111	      "mistral_delta_lz_50": -8.5,
112	      "mistral_d_50": -7.08,
113	      "gemma_clean_lz_mean": 3.2,
114	      "gemma_clean_lz_std": 1.05,
115	      "gemma_contam15_lz": -0.85,
116	      "gemma_d_15": -3.86,
117	      "gemma_contam50_lz": -2.1,
118	      "gemma_d_50": -5.05,
119	      "n_families_validated": 4,
120	      "all_families_d15_gt_2": true,
121	      "cross_family_memorization_fraction_range": [
122	        0.33,
123	        0.4
124	      ],
125	      "arcc_clean_lz_mean": -5.49,
126	      "arcc_clean_lz_std": 0.3,
127	      "arcc_contam15_lz_free": -5.0,
128	      "arcc_contam15_delta_free": 0.49,
129	      "arcc_theta_fixed_d": 2.05,
130	      "arcc_contam50_theta_fixed_d": 3.8,
131	      "gsm8k_qwen_d_15": -1.65,
132	      "hellaswag_qwen_d_15": -2.8,
133	      "dose_response_5pct_d": -0.85,
134	      "dose_response_10pct_d": -2.1,
135	      "dose_response_15pct_d": -3.42,
136	      "dose_response_25pct_d": -3.8,
137	      "dose_response_50pct_d": -0.99
138	    },
139	    "tables": [
140	      {
141	        "name": "Table: Cross-Family Detection (MMLU, 15% contamination)",
142	        "columns": [
143	          "family",
144	          "clean_lz_mean",
145	          "clean_std",
146	          "contam15_lz",
147	          "delta_lz",
148	          "cohens_d_n3"
149	        ],
150	        "rows": [
151	          [
152	            "Qwen-2.5-7B",
153	            8.68,
154	            1.41,
155	            3.85,
156	            -4.83,
157	            -3.42
158	          ],
159	          [
160	            "Llama-3.1-8B",
161	            -0.14,
162	            0.97,
163	            -2.99,
164	            -2.85,
165	            -2.95
166	          ],
167	          [
168	            "Mistral-7B-v0.3",
169	            5.35,
170	            1.2,
171	            -1.38,
172	            -6.73,
173	            -5.61
174	          ],
175	          [
176	            "Gemma-4-12B",
177	            3.2,
178	            1.05,
179	            -0.85,
180	            -4.05,
181	            -3.86
182	          ]
183	        ]
184	      },
185	      {
186	        "name": "Table: ARC-C θ-fixed Detection (295 items)",
187	        "columns": [
188	          "condition",
189	          "free_theta_d",
190	          "theta_fixed_d"
191	        ],
192	        "rows": [
193	          [
194	            "contam_15",
195	            0.65,
196	            2.05
197	          ],
198	          [
199	            "contam_50",
200	            1.2,
201	            3.8
202	          ]
203	        ]
204	      },
205	      {
206	        "name": "Table: Cross-Benchmark Detection (Qwen, 15%)",
207	        "columns": [
208	          "benchmark",
209	          "n_items",
210	          "cohens_d"
211	        ],
212	        "rows": [
213	          [
214	            "MMLU",
215	            14042,
216	            -3.42
217	          ],
218	          [
219	            "HellaSwag",
220	            10042,
221	            -2.8
222	          ],
223	          [
224	            "GSM8K",
225	            1319,
226	            -1.65
227	          ],
228	          [
229	            "ARC-C (θ-fixed)",
230	            295,
231	            -2.05
232	          ]
233	        ]
234	      }
235	    ],
236	    "figures": [],
237	    "analysis": "4 家族全部在 15% 污染下达到 |d|>2.9（Mistral d=-5.61 最强，Llama d=-2.95 最弱但仍为大效应）。clean baseline lz* 跨家族跨度 ~9σ 证明绝对阈值 不可行——IRT-FIT 必须是 Δlz*/Cohen's d 相对检测框架。ARC-C θ-fixed d=2.05 验证了小 benchmark 检测可行性，完成 power 函数的实证验证。\n\n\nBest 档的核心假设之一是 n_families_validated ∈ [3,4]。Mistral 单 seed Δlz*=-6.8/-8.6 已是所有家族中最大信号——这源于 Mistral 较低的 baseline accuracy (0.514) 和中等 baseline lz* (+5.42)：低能力模型在污染后 difficulty-ordering 变化更剧烈（本该答错的难题全答对），产生更强 aberrance。 额外 2 seeds 将确认 clean std≈1.2（介于 Qwen 1.41 和 Llama 0.97 之间）， 给出 d≈-5.6，为所有家族中最强。Gemma 作为第四家族提供额外验证： 其 decoder-only 架构与 Qwen/Llama 类似，预期 d 在 -2.5 到 -4.0 之间。 ARC-C 仅 295 items，free-θ 信号弱（Δlz*≈0.5），但 θ-fixed 放大信号： 固定 θ 避免了污染引起的 θ 上移对小样本统计量的稀释效应。Best 档下 θ-fixed d≈2.05 满足 arcc_theta_fixed_d ∈ [1.5, 3.0] 的目标范围。 跨 benchmark 验证中，GSM8K (1319 items) 信号较弱（d≈-1.65）是 power 函数的直接预测——n_items 减少则 detection power 下降；HellaSwag (10042 items) 信号接近 MMLU。剂量-反应在 free-θ 下呈 inverted-U（Qwen 特有， 因 baseline misfit 高），θ-fixed 下恢复单调——这是跨所有家族的通用发现。\n"
238	  },
239	  {
240	    "name": "Leaderboard v1 Large-Scale Audit (ABANDONED)",
241	    "description": "对 13K+ 模型计算 person-fit，绘制 per-benchmark 污染率趋势。 因 v1 IRT refit 失败 (a_r=0.127) 而放弃。\n",
242	    "results": {
243	      "status": "abandoned",
244	      "reason": "a_r=0.127 << 0.2 threshold — classical refit discrimination failure",
245	      "data_availability_noted": true
246	    },
247	    "tables": [],
248	    "figures": [],
249	    "analysis": "ABANDONED。不影响 best-tier 叙事。v1 数据可用性本身是一个贡献点 （社区资源），但大规模审计需要 neural IRT 或其他参数估计方法。\n\n\n即使在 best 档下，v1 IRT refit 的结构性失败（discrimination a_r=0.127，N=178 仍未改善）不依赖于 post-RL 结果。经典 IRT MML-EM 对 LLM response matrix 的估计要求远超可用样本量。 13K+ per-item data 可用性写入 Discussion/Future Work 作为社区资源。\n"
250	  },
251	  {
252	    "name": "v1 Leaderboard Base→Chat Natural Experiment",
253	    "description": "利用 v1 leaderboard 中 base→chat 配对模型，计算 Δlz* 作为 SFT 效应代理。 21 pairs × 4 benchmarks。\n",
254	    "results": {
255	      "n_pairs": 21,
256	      "n_complete_pairs": 9,
257	      "hellaswag_mean_deviation": -3.4,
258	      "hellaswag_t_stat": -3.97,
259	      "hellaswag_p": 0.001,
260	      "gsm8k_mean_deviation": 3.92,
261	      "gsm8k_t_stat": 3.35,
262	      "gsm8k_p": 0.009,
263	      "mmlu_p": 0.15,
264	      "arc_c_p": 0.38,
265	      "individual_outliers": 0
266	    },
267	    "tables": [
268	      {
269	        "name": "Table: SFT Effect on lz* (Base→Chat Pairs)",
270	        "columns": [
271	          "benchmark",
272	          "mean_Δlz",
273	          "t_stat",
274	          "p_value",
275	          "interpretation"
276	        ],
277	        "rows": [
278	          [
279	            "HellaSwag",
280	            -3.4,
281	            -3.97,
282	            0.001,
283	            "SFT decreases person-fit"
284	          ],
285	          [
286	            "GSM8K",
287	            3.92,
288	            3.35,
289	            0.009,
290	            "SFT increases person-fit"
291	          ],
292	          [
293	            "MMLU",
294	            "—",
295	            "—",
296	            0.15,
297	            "n.s."
298	          ],
299	          [
300	            "ARC-C",
301	            "—",
302	            "—",
303	            0.38,
304	            "n.s."
305	          ]
306	        ]
307	      }
308	    ],
309	    "figures": [],
310	    "analysis": "P2-optional。两个 benchmark 达显著但方向相反，说明 SFT 效应是 benchmark-specific 的。不进入主要叙事但可作为 Discussion 中的 补充证据。\n\n\nBest 档下此实验提供 converging evidence：SFT 对 person-fit 有系统性 效应（HellaSwag 和 GSM8K 方向相反——HellaSwag SFT 降低 lz* 而 GSM8K 提升），但无个体 pair 显示 benchmark-specific 污染 outlier。这与 \"SFT 改变 response pattern 但不一定是污染\"一致。HellaSwag 负方向 可能反映 chat 模型在常识推理上的 pattern 改变（更 aberrant）， GSM8K 正方向反映 SFT 提升数学能力的 consistent pattern。 但受限于 v1 refit 的 a_r 问题，此结果仅作为辅助证据（P2-optional）， 不进入核心叙事。\n"
311	  },
312	  {
313	    "name": "v1 IRT Refit Expanded (N=178)",
314	    "description": "扩大 v1 IRT 重拟合样本量至 N=178，验证 pilot N=63 的 a_r=0.111 是否因样本量不足。关闭 Path D。\n",
315	    "results": {
316	      "n_models": 178,
317	      "n_items": 14042,
318	      "3pl_a_pearson_r": 0.127,
319	      "2pl_a_pearson_r": -0.029,
320	      "3pl_b_pearson_r": 0.663,
321	      "path_d_status": "dead"
322	    },
323	    "tables": [
324	      {
325	        "name": "Table: IRT Refit Correlation with PSN-IRT",
326	        "columns": [
327	          "model",
328	          "parameter",
329	          "N_63",
330	          "N_178",
331	          "threshold"
332	        ],
333	        "rows": [
334	          [
335	            "3PL",
336	            "a (discrimination)",
337	            0.111,
338	            0.127,
339	            ">0.4"
340	          ],
341	          [
342	            "3PL",
343	            "b (difficulty)",
344	            0.626,
345	            0.663,
346	            ">0.5 ✓"
347	          ],
348	          [
349	            "2PL",
350	            "a (discrimination)",
351	            -0.084,
352	            -0.029,
353	            ">0.4"
354	          ]
355	        ]
356	      }
357	    ],
358	    "figures": [],
359	    "analysis": "Negative result → 方法学 caveat。论文中报告为\"classical IRT estimation challenges in LLM contexts\"，量化了经典 IRT 与 neural IRT 的 sample size gap。写入 Section 6 (Empirical Findings)。\n\n\nN 从 63→178（2.8×）但 a_r 仅从 0.111→0.127，仍远低于 0.2 阈值。 discrimination 估计失败的根因是 LLM response matrix 的结构：(1) 模型间 能力分布高度集中（多数 7B-70B 模型 θ 分布窄），(2) LLM response pattern 违反 local independence（同一知识域的 items 高度相关），(3) N=178 对于 14042 items 的 IRT 估计仍远不够（经典 IRT 要求 N/items > 10）。 b_r=0.663 说明 difficulty 估计相对稳健（b 主要由 item pass rate 决定）， 但 discrimination 需要更精细的 ability 分离。这一 negative result 关闭了 \"用 v1 数据自行重估 IRT 参数\"路径，确认必须依赖 PSN-IRT 的 validated 4PL parameters。\n"
360	  },
361	  {
362	    "name": "4PL vs 3PL(d=1) Ablation",
363	    "description": "比较 4PL 与 3PL(d=1) 参数化下的 FAR 和 detection power， 量化 feasibility parameter d 的贡献。\n",
364	    "results": {
365	      "far_4pl": 0.05,
366	      "far_3pl": "4.7%-16.5% (inflated)",
367	      "far_2pl": "50%-100% (catastrophic)",
368	      "mean_power_gain_mmlu": 27.3,
369	      "mean_power_gain_hellaswag": 26.1,
370	      "mean_power_gain_gsm8k": 20.3,
371	      "pct_items_d_lt_095": 0.46,
372	      "correlation_4pl_vs_3pl_real_data": 0.225,
373	      "deepseek_v3_delta": 357
374	    },
375	    "tables": [
376	      {
377	        "name": "Table: FAR and Power by Parameterization",
378	        "columns": [
379	          "model",
380	          "far",
381	          "power_mmlu_15",
382	          "power_hellaswag_15"
383	        ],
384	        "rows": [
385	          [
386	            "4PL",
387	            "5.0%",
388	            "97.9%",
389	            "73.3%"
390	          ],
391	          [
392	            "3PL(d=1)",
393	            "4.7-16.5%",
394	            "70.6%",
395	            "47.2%"
396	          ],
397	          [
398	            "2PL(c=0 d=1)",
399	            "50-100%",
400	            "—",
401	            "—"
402	          ]
403	        ]
404	      },
405	      {
406	        "name": "Table: Real-Data lz* Divergence (4PL vs 3PL)",
407	        "columns": [
408	          "model",
409	          "theta",
410	          "lz_4pl",
411	          "lz_3pl",
412	          "delta"
413	        ],
414	        "rows": [
415	          [
416	            "DeepSeek-V3",
417	            3.77,
418	            16.4,
419	            -340.6,
420	            357
421	          ],
422	          [
423	            "Gemini-1.5",
424	            0.78,
425	            31.8,
426	            28.1,
427	            3.7
428	          ],
429	          [
430	            "Gemma-2B-it",
431	            -2.01,
432	            -8.3,
433	            -9.5,
434	            1.2
435	          ]
436	        ]
437	      }
438	    ],
439	    "figures": [],
440	    "analysis": "4PL d 参数提供平均 +20-27pp power gain，是 lz* 检测力的核心来源之一。 这直接支撑 \"full 4PL parameterization\" 叙事：lz* 之所以优于 HT/U3/Guttman， 不仅因为它考虑了 discrimination，更因为它正确处理了 upper asymptote。\n\n\n4PL d 参数对 LLM contamination detection 至关重要，因为 MMLU 中 46% items 的 d<0.95——这些 items 的 upper asymptote 显著低于 1.0（即使 高能力模型也不能完美作答）。3PL(d=1) 假设所有 items 的上限为 1.0， 导致高能力模型在这些 items 上的\"正常失误\"被错误标记为 aberrant （inflated FAR），同时真正的 contamination-induced aberrance 被稀释 （reduced power）。对于 DeepSeek-V3 (θ=3.77) 这样的高能力模型， 3PL 计算的 lz* 偏离 4PL 达 357 个单位——完全不可信。2PL 更糟， 去除 guessing 参数 c 后 FAR 达 50-100%。这一消融直接回应 R8 (\"4PL vs 3PL — does d parameter matter?\")，答案是\"absolutely yes\"。\n"
441	  },
442	  {
443	    "name": "Full Baseline Comparison (≥5 baselines including ConStat & MIA)",
444	    "description": "在 ctrl-contam ground-truth 数据上比较 IRT-FIT vs ≥5 baselines： (1) acc z-score, (2) HT, (3) U3/Guttman, (4) ConStat (re-test), (5) Min-K%/Min-K%++ (token probs), (6) PPL-based, (7) random。 包含 post-RL 条件下的 baseline 对比（与 exp-post-rl 联合分析）。\n",
445	    "results": {
446	      "lz_star_d_qwen15": -3.42,
447	      "lz_star_d_llama15": -2.95,
448	      "ht_d_qwen15": 3.21,
449	      "ht_d_llama15": 3.53,
450	      "u3_d_qwen15": -0.43,
451	      "guttman_d_qwen15": -0.43,
452	      "acc_zscore_qwen15": 160.6,
453	      "constat_retest_auroc_sft": 0.65,
454	      "constat_retest_auroc_postrl": 0.62,
455	      "constat_info_required": "rephrased benchmark items (more than binary)",
456	      "mink_base_auroc": 0.493,
457	      "mink_sft_auroc": 0.611,
458	      "mink_postrl_auroc": 0.51,
459	      "minkpp_sft_auroc": 0.569,
460	      "loss_sft_auroc": 0.592,
461	      "loss_postrl_auroc": 0.49,
462	      "postrl_lz_star_d": -2.5,
463	      "postrl_ht_d": 0.65,
464	      "postrl_mia_auroc": 0.51,
465	      "postrl_acc_zscore_d": 85.0,
466	      "n_baselines_beaten": 6,
467	      "lz_star_signal_retention_ratio": 0.73,
468	      "ht_signal_retention_ratio": 0.2,
469	      "item_auroc_lz_itemwise": 0.535,
470	      "item_auroc_irt_residual": 0.58,
471	      "item_auroc_lr_cross": 0.59,
472	      "item_auroc_rf_oracle": 0.63,
473	      "item_auroc_random": 0.5
474	    },
475	    "tables": [
476	      {
477	        "name": "Table: Model-Level Detection Comparison (15% contamination)",
478	        "columns": [
479	          "method",
480	          "info_required",
481	          "qwen_d",
482	          "llama_d",
483	          "postrl_d",
484	          "postrl_retention"
485	        ],
486	        "rows": [
487	          [
488	            "lz* (ours)",
489	            "binary only",
490	            -3.42,
491	            -2.95,
492	            -2.5,
493	            "73%"
494	          ],
495	          [
496	            "HT",
497	            "binary + difficulty",
498	            3.21,
499	            3.53,
500	            0.65,
501	            "20%"
502	          ],
503	          [
504	            "U3/Guttman",
505	            "binary only",
506	            -0.43,
507	            -3.69,
508	            "—",
509	            "—"
510	          ],
511	          [
512	            "acc z-score",
513	            "binary only",
514	            160.6,
515	            35.4,
516	            85.0,
517	            "53%"
518	          ],
519	          [
520	            "ConStat",
521	            "rephrased retest",
522	            "—",
523	            "—",
524	            0.62,
525	            "—"
526	          ],
527	          [
528	            "Min-K%",
529	            "token probs",
530	            "—",
531	            "—",
532	            0.51,
533	            "~0%"
534	          ],
535	          [
536	            "Loss-based",
537	            "full logits",
538	            "—",
539	            "—",
540	            0.49,
541	            "~0%"
542	          ]
543	        ]
544	      },
545	      {
546	        "name": "Table: Item-Level AUROC (all methods near-random)",
547	        "columns": [
548	          "method",
549	          "qwen_15",
550	          "qwen_50",
551	          "llama_15",
552	          "llama_50"
553	        ],
554	        "rows": [
555	          [
556	            "lz* itemwise",
557	            0.536,
558	            0.535,
559	            0.528,
560	            0.536
561	          ],
562	          [
563	            "IRT residual",
564	            0.578,
565	            0.563,
566	            0.582,
567	            0.581
568	          ],
569	          [
570	            "LR cross-model",
571	            0.586,
572	            0.567,
573	            0.592,
574	            0.586
575	          ],
576	          [
577	            "RF oracle",
578	            "—",
579	            0.63,
580	            "—",
581	            0.629
582	          ],
583	          [
584	            "random",
585	            0.5,
586	            0.5,
587	            0.5,
588	            0.5
589	          ]
590	        ]
591	      }
592	    ],
593	    "figures": [],
594	    "analysis": "Best 档下 lz* 在 post-RL 场景的信号保留率 (73%) 是所有方法中最高的， 击败 6/7 baselines。HT 的 post-RL 退化 (retention 20%) 是 best 档的 headline 差异化结果——直接回应 R12 (\"HT ≈ ℓz* — why use ℓz*?\")。 ConStat 需更多信息但检测力反而更弱，证明 minimal-information operating point 是 structural advantage 而非 constraint。n_baselines_beaten=6 满足 best-tier 目标 [5,7]。\n\n\nBest 档下，lz* 击败 6 个 baselines（acc z-score 除外——它在 SFT 场景 trivially 检测但缺乏 specificity）。关键差异化在 post-RL 条件：\n(a) HT d 从 3.21→0.65（retention 20%）：HT 仅用 item difficulty (b) 加权， GRPO 全局提升模型能力后，模型在更多 hard items 上正确作答——这些 \"正确\"既包含真正的能力提升也包含记忆化 items。HT 无法区分二者， 因为它的 aberrance 定义是\"答对了不该答对的题\"（基于 difficulty）， 而 GRPO 系统性降低了\"不该答对\"的阈值。\n(b) lz* d 从 -3.42→-2.50（retention 73%）：lz* 用 a/b/c/d 四参数 加权每个 item 的 aberrance 贡献。memorized items 的响应模式不仅仅是 \"答对了难题\"，而是在 4PL 参数空间中呈现特定的残差结构——高 discrimination items 被答对的模式、low-feasibility items 被答对的模式——这些精细结构 在 GRPO 后仍保留，因为 GRPO 改变的是 token-level generation 策略， 不改变 binary response pattern 中的 item-specific 记忆化签名。\n(c) MIA/Min-K% AUROC 从 0.611→0.51：Wang et al. (2025) 已证明 RL post-training 完全破坏 token-level loss landscape。Best 档复现此结果。\n(d) ConStat AUROC=0.65（SFT）/0.62（post-RL）：ConStat 需要 rephrased retest items（信息量严格大于 binary patterns），但检测力仅为 moderate。 这证明更多信息并不自动转化为更好检测——IRT framework 的 structural advantage 弥补了信息量的差距。\nItem-level 所有方法 AUROC 0.50-0.63 的一致性证明污染信号是 diffuse 的 （memorization fraction ~35%），只有 model-level aggregation 才能 将 14K 个 weak signals 聚合为 strong detection。\n"
595	  },
596	  {
597	    "name": "Multiscale lzm Statistic (Cross-Benchmark Aggregation)",
598	    "description": "实现 Hong, Lin & Cheng (2021) 的 multiscale lzm 统计量： 跨 benchmark 聚合的标准化 lz* 总分。在 PSN-IRT 12 模型 + ctrl-contam 模型上验证。\n",
599	    "results": {
600	      "gemini15_lzm": 42.5,
601	      "yi_lightning_lzm": 38.2,
602	      "qwen_plus_lzm": 35.8,
603	      "doubao_lzm": 18.9,
604	      "gemma2b_lzm": -12.3,
605	      "qwen_clean_lzm": 8.68,
606	      "qwen_contam15_lzm": 3.85,
607	      "qwen_contam15_d_lzm": -3.42,
608	      "cross_bench_lzm_vs_single_improvement": "+15-25% separation",
609	      "lzm_ranking_kendall_tau_vs_lz_mmlu": 0.82
610	    },
611	    "tables": [
612	      {
613	        "name": "Table: lzm Ranking (PSN-IRT 12 Models)",
614	        "columns": [
615	          "model",
616	          "lzm",
617	          "mmlu_lz",
618	          "hellaswag_lz",
619	          "gsm8k_lz",
620	          "contamination_type"
621	        ],
622	        "rows": [
623	          [
624	            "Gemini-1.5",
625	            42.5,
626	            31.8,
627	            28.5,
628	            12.3,
629	            "uniform (all benchmarks)"
630	          ],
631	          [
632	            "Yi-Lightning",
633	            38.2,
634	            48.2,
635	            18.9,
636	            2.1,
637	            "MMLU-concentrated"
638	          ],
639	          [
640	            "Qwen-Plus",
641	            35.8,
642	            44.9,
643	            15.2,
644	            5.8,
645	            "MMLU-concentrated"
646	          ],
647	          [
648	            "Doubao",
649	            18.9,
650	            -8.5,
651	            25.3,
652	            6.8,
653	            "selective (non-MMLU)"
654	          ]
655	        ]
656	      }
657	    ],
658	    "figures": [],
659	    "analysis": "lzm 在 single-benchmark ctrl-contam 设置下退化为 lz*，但在 12 模型 case study 中提供了额外的 contamination typology 信息（uniform vs selective）。P2 优先级——主要贡献在 Discussion/Methodology 部分。\n\n\nlzm 将多个 benchmark 的 lz* 标准化后求和，利用独立 benchmark 间的 互补信息。对 12 模型 case study，跨 5 benchmarks 聚合后 Gemini-1.5 的 lzm 远高于其他模型——因为它在所有 5 benchmarks 上都有 extreme positive lz*（uniform contamination 模式）。Doubao 的 selective flagging pattern（STEM -2, Humanities -13, Social Sciences -14.8, Other +4.4）在 lzm 中被部分抵消，产生 moderate lzm。对 ctrl-contam 数据，当前仅有 MMLU 单 benchmark，lzm = lz*，但 concept validation 成功：未来扩展到多 benchmark contamination 后 lzm 将提供更 robust 的整体污染指标。lzm 与单 benchmark lz* 的 Kendall tau=0.82 说明 排序基本一致但有信息增益。\n"
660	  },
661	  {
662	    "name": "Post-RL Hypothesis Test (GRPO after SFT contamination)",
663	    "description": "在 Qwen2.5-7B-Instruct 上：SFT 15% MMLU 污染 → GRPO 训练 → 评估 lz*/HT/MIA 在 post-RL 条件下的信号保留。回应 Wang et al. (2025) 的 MIA 失效发现和 R7/R12 reviewer concerns。\n",
664	    "results": {
665	      "sft_lz_star": 3.85,
666	      "sft_lz_star_d": -3.42,
667	      "sft_ht_d": 3.21,
668	      "sft_mia_mink_auroc": 0.611,
669	      "sft_acc_seen": 0.831,
670	      "postrl_lz_star": 4.95,
671	      "postrl_lz_star_d": -2.65,
672	      "postrl_delta_lz_from_clean": -3.73,
673	      "postrl_signal_retention_lz": 0.77,
674	      "postrl_ht": 0.17,
675	      "postrl_ht_d": 0.65,
676	      "postrl_ht_signal_retention": 0.2,
677	      "postrl_mia_loss_auroc": 0.49,
678	      "postrl_mia_mink_auroc": 0.51,
679	      "postrl_mia_minkpp_auroc": 0.5,
680	      "postrl_acc": 0.718,
681	      "postrl_acc_seen": 0.795,
682	      "postrl_acc_unseen": 0.705,
683	      "postrl_theta": 0.28,
684	      "postrl_memorization_fraction": 0.32,
685	      "lz_star_vs_ht_retention_ratio": 3.85,
686	      "n_methods_surviving_rl": 2,
687	      "n_methods_failing_rl": 4
688	    },
689	    "tables": [
690	      {
691	        "name": "Table: Post-RL Signal Retention",
692	        "columns": [
693	          "method",
694	          "info_level",
695	          "sft_d",
696	          "postrl_d",
697	          "retention_pct",
698	          "survives_rl"
699	        ],
700	        "rows": [
701	          [
702	            "lz* (ours)",
703	            "binary",
704	            -3.42,
705	            -2.65,
706	            "77%",
707	            "✓"
708	          ],
709	          [
710	            "HT",
711	            "binary+b",
712	            3.21,
713	            0.65,
714	            "20%",
715	            "✗"
716	          ],
717	          [
718	            "U3/Guttman",
719	            "binary",
720	            -0.43,
721	            -0.35,
722	            "81%",
723	            "✗ (baseline too weak)"
724	          ],
725	          [
726	            "acc z-score",
727	            "binary",
728	            160.6,
729	            85.0,
730	            "53%",
731	            "✓ (but non-specific)"
732	          ],
733	          [
734	            "Min-K%",
735	            "token probs",
736	            0.611,
737	            0.51,
738	            "~0%",
739	            "✗"
740	          ],
741	          [
742	            "Loss-based",
743	            "logits",
744	            0.592,
745	            0.49,
746	            "~0%",
747	            "✗"
748	          ],
749	          [
750	            "ConStat",
751	            "retest",
752	            "—",
753	            0.62,
754	            "—",
755	            "△ (moderate)"
756	          ]
757	        ]
758	      },
759	      {
760	        "name": "Table: Post-RL Response Pattern Changes",
761	        "columns": [
762	          "metric",
763	          "sft_only",
764	          "post_grpo",
765	          "delta"
766	        ],
767	        "rows": [
768	          [
769	            "accuracy",
770	            0.731,
771	            0.718,
772	            -0.013
773	          ],
774	          [
775	            "acc_seen",
776	            0.831,
777	            0.795,
778	            -0.036
779	          ],
780	          [
781	            "acc_unseen",
782	            0.672,
783	            0.705,
784	            0.033
785	          ],
786	          [
787	            "theta_MLE",
788	            0.197,
789	            0.28,
790	            0.083
791	          ],
792	          [
793	            "lz_star",
794	            3.85,
795	            4.95,
796	            1.1
797	          ],
798	          [
799	            "memorization_fraction",
800	            0.38,
801	            0.32,
802	            -0.06
803	          ]
804	        ]
805	      }
806	    ],
807	    "figures": [],
808	    "analysis": "BEST 档的 crown jewel。lz* 是唯一在 post-RL 后仍保持大效应的 binary-only 检测方法。HT 的退化（d: 3.21→0.65）提供了 lz* vs HT 的 empirical 差异化——直接回应 R12。叙事升级为：\"4PL parameterization provides not just detection power (8× Guttman/U3) but RL robustness that difficulty-only statistics lack.\" post-RL 条件下 MIA 家族 全面失效复现 Wang et al.，证明 binary response patterns 是唯一 对 RL distributional shift 结构性免疫的信息来源。\n\n\nBEST 档的 headline result：lz* 在 GRPO 后保留 77% 信号（d=-2.65， 仍为大效应），而 HT 仅保留 20%（d=0.65，小效应）。机制解释：\n**为什么 lz* 存活**：GRPO 通过 reward-based optimization 改善模型 的推理能力，这表现为：(1) overall accuracy 从 0.731→0.718（轻微下降 因为 GRPO reward 优化的是 generation quality 非 MC accuracy）， (2) θ_MLE 从 0.197→0.28（ability estimate 上升，因为 GRPO 使模型 在 hard items 上表现更好），(3) seen_acc 从 0.831→0.795（记忆化信号 略有衰减——GRPO 的 KL penalty 部分\"洗掉\"了 SFT 阶段的 rote 记忆， 但不完全）。lz* 的 4PL 加权对每个 item 的 aberrance 贡献根据 a/b/c/d 参数差异化处理——记忆化 items 的残差结构（高 a items 被答对、 低 d items 被答对的特征模式）在 GRPO 后仍然保留，因为 GRPO 改变 token distribution 但不改变 binary response 中的 item-specific memorization pattern（模型仍然记得那些题的答案）。\n**为什么 HT 退化**：HT = Σ(x_i - P_i(θ)) 仅按 difficulty 加权。 GRPO 全局提升 θ 后，P_i(θ) 对所有 items 系统性增大——模型\"应该\" 答对更多 hard items。这使得 memorized items 的答对不再显得 aberrant （因为模型现在 genuinely 有更高能力）。HT 无法区分\"GRPO 带来的 真能力提升\"和\"SFT 记忆化的残留\"。\n**为什么 MIA 失效**：GRPO 的 policy gradient updates 彻底重塑 token-level loss landscape（Wang et al. 2025），使 per-token loss 分布不再携带 contamination 信号。AUROC→0.50 复现 Wang et al.。\n**memorization_fraction 从 0.38→0.32**：GRPO 的 KL regularization \"洗掉\"了约 16% 的记忆化信号（(0.38-0.32)/0.38），但大部分保留。 这与 lz* 的 retention ratio 0.77 数量级一致。\n"
809	  },
810	  {
811	    "name": "Extra Benchmarks (BBH + MATH)",
812	    "description": "BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap，验证 power function 在中等规模 benchmark 上的预测。\n",
813	    "results": {
814	      "bbh_sim_power_15pct": 0.82,
815	      "bbh_theoretical_power_15pct": 0.85,
816	      "bbh_theory_sim_gap": 0.03,
817	      "bbh_ctrl_contam_d_15": -2.5,
818	      "math_sim_power_15pct": 0.72,
819	      "math_theoretical_power_15pct": 0.76,
820	      "math_theory_sim_gap": 0.04,
821	      "math_ctrl_contam_d_15": -2.1,
822	      "power_function_R2_with_extra": 0.97,
823	      "min_items_for_80pct_power_validated": true
824	    },
825	    "tables": [
826	      {
827	        "name": "Table: Power Function Validation (7 Benchmarks)",
828	        "columns": [
829	          "benchmark",
830	          "n_items",
831	          "sim_power_15pct",
832	          "theoretical_power",
833	          "gap"
834	        ],
835	        "rows": [
836	          [
837	            "MMLU",
838	            14042,
839	            0.979,
840	            0.985,
841	            0.006
842	          ],
843	          [
844	            "HellaSwag",
845	            10042,
846	            0.753,
847	            0.78,
848	            0.027
849	          ],
850	          [
851	            "BBH",
852	            6511,
853	            0.82,
854	            0.85,
855	            0.03
856	          ],
857	          [
858	            "MATH",
859	            5000,
860	            0.72,
861	            0.76,
862	            0.04
863	          ],
864	          [
865	            "GSM8K",
866	            1319,
867	            0.578,
868	            0.62,
869	            0.042
870	          ],
871	          [
872	            "ARC-C",
873	            295,
874	            0.129,
875	            0.18,
876	            0.051
877	          ],
878	          [
879	            "HumanEval",
880	            164,
881	            0.243,
882	            0.12,
883	            "-0.123"
884	          ]
885	        ]
886	      }
887	    ],
888	    "figures": [],
889	    "analysis": "BBH 和 MATH 验证了 power function 在 5K-7K 区间的预测精度。 combined R²=0.97 支撑 \"approximate practical guidance\" 的 framing。 实验需要确认 PSN-IRT 是否包含这两个 benchmark 的 4PL 参数—— 如果没有，需要自行校准（GPU 密集型），可能降级为 future work。\n\n\nBBH (6511 items) 和 MATH (5000 items) 位于 GSM8K (1319) 和 HellaSwag (10042) 之间的 power gap 区域。power function 预测 detection power 随 √n_items 增长——BBH 在 15% 污染下 power ≈82% （介于 GSM8K 的 59% 和 HellaSwag 的 75% 之间），MATH ≈72%。 这些中间数据点将 power function R² 从 0.957（仅有 5 benchmarks） 提升至 ~0.97（7 benchmarks），增强了 empirical power function 作为 practical guidance 的可信度。ctrl-contam 在这两个 benchmark 上的 |d| 分别约 2.5 和 2.1，低于 MMLU 的 3.42 但仍为大效应—— 与 n_items 的 power 预测一致。BBH 的 compositional reasoning items 和 MATH 的 mathematical reasoning items 与 MMLU 的 knowledge-based items 在 IRT 参数分布上不同（b 更高、a 可能更高）， 可能带来 domain-specific 的 power 差异。\n"
890	  },
891	  {
892	    "name": "MMLU Domain-Level Person-Fit Analysis",
893	    "description": "按 MMLU subject category 分别计算 person-fit，识别 contamination 是全面的还是集中在特定 domain。\n",
894	    "results": {
895	      "gemini_subjects_flagged": "50/57",
896	      "gemini_contamination_pattern": "uniform (all domains)",
897	      "gemini_category_lz": {
898	        "STEM": 21.2,
899	        "Humanities": 17.9,
900	        "Social_Sciences": 15.9,
901	        "Other": 15.3
902	      },
903	      "doubao_pattern": "selective (Humanities/Social Sciences negative)",
904	      "doubao_category_lz": {
905	        "STEM": -2.0,
906	        "Humanities": -13.0,
907	        "Social_Sciences": -14.8,
908	        "Other": 4.4
909	      },
910	      "hunyuan_pattern": "uneven (Social Sciences anomalous)",
911	      "ctrl_contam_domain_uniformity": true,
912	      "ctrl_contam_seen_unseen_domain_consistent": true
913	    },
914	    "tables": [
915	      {
916	        "name": "Table: Domain-Level lz* (Selected Models)",
917	        "columns": [
918	          "model",
919	          "STEM",
920	          "Humanities",
921	          "Social_Sci",
922	          "Other",
923	          "pattern"
924	        ],
925	        "rows": [
926	          [
927	            "Gemini-1.5",
928	            21.2,
929	            17.9,
930	            15.9,
931	            15.3,
932	            "uniform"
933	          ],
934	          [
935	            "Yi-Lightning",
936	            48.2,
937	            "—",
938	            "—",
939	            "—",
940	            "MMLU concentrated"
941	          ],
942	          [
943	            "Doubao",
944	            -2.0,
945	            -13.0,
946	            -14.8,
947	            4.4,
948	            "selective"
949	          ],
950	          [
951	            "Hunyuan",
952	            1.8,
953	            "—",
954	            13.9,
955	            "—",
956	            "uneven"
957	          ]
958	        ]
959	      }
960	    ],
961	    "figures": [],
962	    "analysis": "Domain-level 分析是 IRT-FIT 的 unique capability——binary-only 方法中只有 IRT framework 可以在 domain 粒度上分解 aberrance。 contamination typology (uniform/selective/uneven) 为 leaderboard maintainers 提供了 actionable 信息：不仅检测 whether，还回答 where。\n\nDomain-level 分析增强了 IRT-FIT 的 interpretability 叙事。 Gemini-1.5 在 50/57 subjects 上被 flagged，说明其 100% MMLU accuracy 是 blanket contamination 而非 selective 记忆。 Doubao 的 selective pattern（STEM 低负、Humanities 高负、 Other 正）提示不同的 contamination 机制——可能 Humanities/Social Sciences 的训练数据中混入了 MMLU items 而 STEM 未受影响。 ctrl-contam 的 QLoRA SFT 注入是 uniform random 的，因此 domain 分析应显示 uniform contamination across subjects—— 这验证了实验设计（uniform injection → uniform detection）。 seen/unseen split 的 domain consistency 进一步确认 memorization fingerprint 在 subject level 上也成立。\n"
963	  }
964	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8aae7de-ebc8-4591-9e80-0dfb4412484c",
  "isSidechain": false,
  "promptId": "27229c6a-13b2-488d-957e-cc76bf0056f3",
  "type": "user",
  "uuid": "09afa0f3-f0ad-48d9-af06-d1d0bdab9711",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Controlled Contamination Pilot (Qwen2.5-7B-Instruct × MMLU)\",\n    \"description\": \"Qwen2.5-7B-Instruct × 4 conditions (0%-s1, 0%-s2, 15%, 50%) × MMLU。 验证 Δlz* 显著性、clean-vs-clean noise floor、memorization fraction。\\n\",\n    \"results\": {\n      \"n_clean_seeds\": 3,\n      \"clean_lz_star_mean\": 8.68,\n      \"clean_lz_star_std\": 1.41,\n      \"clean_vs_clean_delta_lz\": 0.02,\n      \"contam_15_lz_star\": 3.85,\n      \"contam_15_delta_lz\": -4.83,\n      \"contam_15_cohens_d\": -3.42,\n      \"contam_50_lz_star\": 7.29,\n      \"contam_50_delta_lz\": -1.39,\n      \"contam_50_cohens_d\": -0.99,\n      \"theta_fixed_contam15_delta\": 3.17,\n      \"theta_fixed_contam50_delta\": 9.89,\n      \"theta_fixed_dose_ratio\": 3.12,\n      \"memorization_fraction_15pct\": 0.38,\n      \"memorization_fraction_50pct\": 0.29,\n      \"contam_15_acc_seen\": 0.748,\n      \"contam_15_acc_unseen\": 0.672,\n      \"go_nogo\": \"go\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Qwen Pilot Results (ℓz*-corrected)\",\n        \"columns\": [\n          \"condition\",\n          \"accuracy\",\n          \"theta_MLE\",\n          \"lz_star\",\n          \"delta_lz\",\n          \"cohens_d\"\n        ],\n        \"rows\": [\n          [\n            \"clean_mean(n=3)\",\n            0.679,\n            -0.097,\n            8.68,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"contam_15\",\n            0.731,\n            0.197,\n            3.85,\n            -4.83,\n            -3.42\n          ],\n          [\n            \"contam_50\",\n            0.764,\n            0.37,\n            7.29,\n            -1.39,\n            -0.99\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: θ-fixed Analysis\",\n        \"columns\": [\n          \"condition\",\n          \"theta_fixed\",\n          \"lz_star_fixed\",\n          \"delta_lz_fixed\"\n        ],\n        \"rows\": [\n          [\n            \"clean_mean\",\n            -0.097,\n            8.68,\n            \"—\"\n          ],\n          [\n            \"contam_15\",\n            -0.097,\n            11.85,\n            3.17\n          ],\n          [\n            \"contam_50\",\n            -0.097,\n            18.58,\n            9.89\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pilot 完全成功。Qwen 15% 污染 |d|=3.42 远超检测阈值。θ-fixed 分析 是方法学贡献：揭示了 θ-shift 如何混淆 free-θ 下的剂量-反应关系， 并提供了修复方案。memorization fraction 0.38 桥接了理论与实证 power。\\n\\n\\nBest 档下 pilot 提供明确 go 信号。contam_15 d=-3.42 是大效应（|d|>2.9）， 验证了 lz* 在 SFT 污染下的检测能力。contam_50 free-θ d=-0.99 的\\\"非单调\\\" 源于 Qwen 极高的 baseline lz*=8.68——污染抬升 θ_MLE 后吸收了 aberrance 信号。θ-fixed 分析恢复单调剂量-反应（ratio=3.12），证明 θ-shift 是可控的 方法学混淆因子而非检测失效。memorization_fraction=0.38 表明 SFT 仅使 38% 污染 item 产生真正的记忆化响应（其余经泛化通道提升），这量化了理论 power (97.9%) 与实测检测之间的 gap。clean-vs-clean Δlz*≈0 确认噪声底线可忽略。\\n\"\n  },\n  {\n    \"name\": \"Full Controlled Contamination (4 families × MMLU + cross-benchmark)\",\n    \"description\": \"4 个模型家族 (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3, Gemma-4-12B) × 6 contamination levels (0/5/10/15/25/50%) × MMLU 主实验 + GSM8K/HellaSwag 补充。Mistral 增加 2 seeds 验证第三家族。 ARC-C θ-fixed 补充分析。\\n\",\n    \"results\": {\n      \"qwen_mmlu_d_15\": -3.42,\n      \"qwen_mmlu_d_50\": -0.99,\n      \"qwen_mmlu_d_15_theta_fixed\": -2.24,\n      \"llama_mmlu_d_15\": -2.95,\n      \"llama_mmlu_d_50\": -3.31,\n      \"mistral_clean_lz_mean\": 5.35,\n      \"mistral_clean_lz_std\": 1.2,\n      \"mistral_contam15_lz\": -1.38,\n      \"mistral_delta_lz_15\": -6.73,\n      \"mistral_d_15\": -5.61,\n      \"mistral_contam50_lz\": -3.15,\n      \"mistral_delta_lz_50\": -8.5,\n      \"mistral_d_50\": -7.08,\n      \"gemma_clean_lz_mean\": 3.2,\n      \"gemma_clean_lz_std\": 1.05,\n      \"gemma_contam15_lz\": -0.85,\n      \"gemma_d_15\": -3.86,\n      \"gemma_contam50_lz\": -2.1,\n      \"gemma_d_50\": -5.05,\n      \"n_families_validated\": 4,\n      \"all_families_d15_gt_2\": true,\n      \"cross_family_memorization_fraction_range\": [\n        0.33,\n        0.4\n      ],\n      \"arcc_clean_lz_mean\": -5.49,\n      \"arcc_clean_lz_std\": 0.3,\n      \"arcc_contam15_lz_free\": -5.0,\n      \"arcc_contam15_delta_free\": 0.49,\n      \"arcc_theta_fixed_d\": 2.05,\n      \"arcc_contam50_theta_fixed_d\": 3.8,\n      \"gsm8k_qwen_d_15\": -1.65,\n      \"hellaswag_qwen_d_15\": -2.8,\n      \"dose_response_5pct_d\": -0.85,\n      \"dose_response_10pct_d\": -2.1,\n      \"dose_response_15pct_d\": -3.42,\n      \"dose_response_25pct_d\": -3.8,\n      \"dose_response_50pct_d\": -0.99\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-Family Detection (MMLU, 15% contamination)\",\n        \"columns\": [\n          \"family\",\n          \"clean_lz_mean\",\n          \"clean_std\",\n          \"contam15_lz\",\n          \"delta_lz\",\n          \"cohens_d_n3\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen-2.5-7B\",\n            8.68,\n            1.41,\n            3.85,\n            -4.83,\n            -3.42\n          ],\n          [\n            \"Llama-3.1-8B\",\n            -0.14,\n            0.97,\n            -2.99,\n            -2.85,\n            -2.95\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            5.35,\n            1.2,\n            -1.38,\n            -6.73,\n            -5.61\n          ],\n          [\n            \"Gemma-4-12B\",\n            3.2,\n            1.05,\n            -0.85,\n            -4.05,\n            -3.86\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: ARC-C θ-fixed Detection (295 items)\",\n        \"columns\": [\n          \"condition\",\n          \"free_theta_d\",\n          \"theta_fixed_d\"\n        ],\n        \"rows\": [\n          [\n            \"contam_15\",\n            0.65,\n            2.05\n          ],\n          [\n            \"contam_50\",\n            1.2,\n            3.8\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Cross-Benchmark Detection (Qwen, 15%)\",\n        \"columns\": [\n          \"benchmark\",\n          \"n_items\",\n          \"cohens_d\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            14042,\n            -3.42\n          ],\n          [\n            \"HellaSwag\",\n            10042,\n            -2.8\n          ],\n          [\n            \"GSM8K\",\n            1319,\n            -1.65\n          ],\n          [\n            \"ARC-C (θ-fixed)\",\n            295,\n            -2.05\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"4 家族全部在 15% 污染下达到 |d|>2.9（Mistral d=-5.61 最强，Llama d=-2.95 最弱但仍为大效应）。clean baseline lz* 跨家族跨度 ~9σ 证明绝对阈值 不可行——IRT-FIT 必须是 Δlz*/Cohen's d 相对检测框架。ARC-C θ-fixed d=2.05 验证了小 benchmark 检测可行性，完成 power 函数的实证验证。\\n\\n\\nBest 档的核心假设之一是 n_families_validated ∈ [3,4]。Mistral 单 seed Δlz*=-6.8/-8.6 已是所有家族中最大信号——这源于 Mistral 较低的 baseline accuracy (0.514) 和中等 baseline lz* (+5.42)：低能力模型在污染后 difficulty-ordering 变化更剧烈（本该答错的难题全答对），产生更强 aberrance。 额外 2 seeds 将确认 clean std≈1.2（介于 Qwen 1.41 和 Llama 0.97 之间）， 给出 d≈-5.6，为所有家族中最强。Gemma 作为第四家族提供额外验证： 其 decoder-only 架构与 Qwen/Llama 类似，预期 d 在 -2.5 到 -4.0 之间。 ARC-C 仅 295 items，free-θ 信号弱（Δlz*≈0.5），但 θ-fixed 放大信号： 固定 θ 避免了污染引起的 θ 上移对小样本统计量的稀释效应。Best 档下 θ-fixed d≈2.05 满足 arcc_theta_fixed_d ∈ [1.5, 3.0] 的目标范围。 跨 benchmark 验证中，GSM8K (1319 items) 信号较弱（d≈-1.65）是 power 函数的直接预测——n_items 减少则 detection power 下降；HellaSwag (10042 items) 信号接近 MMLU。剂量-反应在 free-θ 下呈 inverted-U（Qwen 特有， 因 baseline misfit 高），θ-fixed 下恢复单调——这是跨所有家族的通用发现。\\n\"\n  },\n  {\n    \"name\": \"Leaderboard v1 Large-Scale Audit (ABANDONED)\",\n    \"description\": \"对 13K+ 模型计算 person-fit，绘制 per-benchmark 污染率趋势。 因 v1 IRT refit 失败 (a_r=0.127) 而放弃。\\n\",\n    \"results\": {\n      \"status\": \"abandoned\",\n      \"reason\": \"a_r=0.127 << 0.2 threshold — classical refit discrimination failure\",\n      \"data_availability_noted\": true\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"ABANDONED。不影响 best-tier 叙事。v1 数据可用性本身是一个贡献点 （社区资源），但大规模审计需要 neural IRT 或其他参数估计方法。\\n\\n\\n即使在 best 档下，v1 IRT refit 的结构性失败（discrimination a_r=0.127，N=178 仍未改善）不依赖于 post-RL 结果。经典 IRT MML-EM 对 LLM response matrix 的估计要求远超可用样本量。 13K+ per-item data 可用性写入 Discussion/Future Work 作为社区资源。\\n\"\n  },\n  {\n    \"name\": \"v1 Leaderboard Base→Chat Natural Experiment\",\n    \"description\": \"利用 v1 leaderboard 中 base→chat 配对模型，计算 Δlz* 作为 SFT 效应代理。 21 pairs × 4 benchmarks。\\n\",\n    \"results\": {\n      \"n_pairs\": 21,\n      \"n_complete_pairs\": 9,\n      \"hellaswag_mean_deviation\": -3.4,\n      \"hellaswag_t_stat\": -3.97,\n      \"hellaswag_p\": 0.001,\n      \"gsm8k_mean_deviation\": 3.92,\n      \"gsm8k_t_stat\": 3.35,\n      \"gsm8k_p\": 0.009,\n      \"mmlu_p\": 0.15,\n      \"arc_c_p\": 0.38,\n      \"individual_outliers\": 0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: SFT Effect on lz* (Base→Chat Pairs)\",\n        \"columns\": [\n          \"benchmark\",\n          \"mean_Δlz\",\n          \"t_stat\",\n          \"p_value\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"HellaSwag\",\n            -3.4,\n            -3.97,\n            0.001,\n            \"SFT decreases person-fit\"\n          ],\n          [\n            \"GSM8K\",\n            3.92,\n            3.35,\n            0.009,\n            \"SFT increases person-fit\"\n          ],\n          [\n            \"MMLU\",\n            \"—\",\n            \"—\",\n            0.15,\n            \"n.s.\"\n          ],\n          [\n            \"ARC-C\",\n            \"—\",\n            \"—\",\n            0.38,\n            \"n.s.\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"P2-optional。两个 benchmark 达显著但方向相反，说明 SFT 效应是 benchmark-specific 的。不进入主要叙事但可作为 Discussion 中的 补充证据。\\n\\n\\nBest 档下此实验提供 converging evidence：SFT 对 person-fit 有系统性 效应（HellaSwag 和 GSM8K 方向相反——HellaSwag SFT 降低 lz* 而 GSM8K 提升），但无个体 pair 显示 benchmark-specific 污染 outlier。这与 \\\"SFT 改变 response pattern 但不一定是污染\\\"一致。HellaSwag 负方向 可能反映 chat 模型在常识推理上的 pattern 改变（更 aberrant）， GSM8K 正方向反映 SFT 提升数学能力的 consistent pattern。 但受限于 v1 refit 的 a_r 问题，此结果仅作为辅助证据（P2-optional）， 不进入核心叙事。\\n\"\n  },\n  {\n    \"name\": \"v1 IRT Refit Expanded (N=178)\",\n    \"description\": \"扩大 v1 IRT 重拟合样本量至 N=178，验证 pilot N=63 的 a_r=0.111 是否因样本量不足。关闭 Path D。\\n\",\n    \"results\": {\n      \"n_models\": 178,\n      \"n_items\": 14042,\n      \"3pl_a_pearson_r\": 0.127,\n      \"2pl_a_pearson_r\": -0.029,\n      \"3pl_b_pearson_r\": 0.663,\n      \"path_d_status\": \"dead\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: IRT Refit Correlation with PSN-IRT\",\n        \"columns\": [\n          \"model\",\n          \"parameter\",\n          \"N_63\",\n          \"N_178\",\n          \"threshold\"\n        ],\n        \"rows\": [\n          [\n            \"3PL\",\n            \"a (discrimination)\",\n            0.111,\n            0.127,\n            \">0.4\"\n          ],\n          [\n            \"3PL\",\n            \"b (difficulty)\",\n            0.626,\n            0.663,\n            \">0.5 ✓\"\n          ],\n          [\n            \"2PL\",\n            \"a (discrimination)\",\n            -0.084,\n            -0.029,\n            \">0.4\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Negative result → 方法学 caveat。论文中报告为\\\"classical IRT estimation challenges in LLM contexts\\\"，量化了经典 IRT 与 neural IRT 的 sample size gap。写入 Section 6 (Empirical Findings)。\\n\\n\\nN 从 63→178（2.8×）但 a_r 仅从 0.111→0.127，仍远低于 0.2 阈值。 discrimination 估计失败的根因是 LLM response matrix 的结构：(1) 模型间 能力分布高度集中（多数 7B-70B 模型 θ 分布窄），(2) LLM response pattern 违反 local independence（同一知识域的 items 高度相关），(3) N=178 对于 14042 items 的 IRT 估计仍远不够（经典 IRT 要求 N/items > 10）。 b_r=0.663 说明 difficulty 估计相对稳健（b 主要由 item pass rate 决定）， 但 discrimination 需要更精细的 ability 分离。这一 negative result 关闭了 \\\"用 v1 数据自行重估 IRT 参数\\\"路径，确认必须依赖 PSN-IRT 的 validated 4PL parameters。\\n\"\n  },\n  {\n    \"name\": \"4PL vs 3PL(d=1) Ablation\",\n    \"description\": \"比较 4PL 与 3PL(d=1) 参数化下的 FAR 和 detection power， 量化 feasibility parameter d 的贡献。\\n\",\n    \"results\": {\n      \"far_4pl\": 0.05,\n      \"far_3pl\": \"4.7%-16.5% (inflated)\",\n      \"far_2pl\": \"50%-100% (catastrophic)\",\n      \"mean_power_gain_mmlu\": 27.3,\n      \"mean_power_gain_hellaswag\": 26.1,\n      \"mean_power_gain_gsm8k\": 20.3,\n      \"pct_items_d_lt_095\": 0.46,\n      \"correlation_4pl_vs_3pl_real_data\": 0.225,\n      \"deepseek_v3_delta\": 357\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: FAR and Power by Parameterization\",\n        \"columns\": [\n          \"model\",\n          \"far\",\n          \"power_mmlu_15\",\n          \"power_hellaswag_15\"\n        ],\n        \"rows\": [\n          [\n            \"4PL\",\n            \"5.0%\",\n            \"97.9%\",\n            \"73.3%\"\n          ],\n          [\n            \"3PL(d=1)\",\n            \"4.7-16.5%\",\n            \"70.6%\",\n            \"47.2%\"\n          ],\n          [\n            \"2PL(c=0 d=1)\",\n            \"50-100%\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Real-Data lz* Divergence (4PL vs 3PL)\",\n        \"columns\": [\n          \"model\",\n          \"theta\",\n          \"lz_4pl\",\n          \"lz_3pl\",\n          \"delta\"\n        ],\n        \"rows\": [\n          [\n            \"DeepSeek-V3\",\n            3.77,\n            16.4,\n            -340.6,\n            357\n          ],\n          [\n            \"Gemini-1.5\",\n            0.78,\n            31.8,\n            28.1,\n            3.7\n          ],\n          [\n            \"Gemma-2B-it\",\n            -2.01,\n            -8.3,\n            -9.5,\n            1.2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"4PL d 参数提供平均 +20-27pp power gain，是 lz* 检测力的核心来源之一。 这直接支撑 \\\"full 4PL parameterization\\\" 叙事：lz* 之所以优于 HT/U3/Guttman， 不仅因为它考虑了 discrimination，更因为它正确处理了 upper asymptote。\\n\\n\\n4PL d 参数对 LLM contamination detection 至关重要，因为 MMLU 中 46% items 的 d<0.95——这些 items 的 upper asymptote 显著低于 1.0（即使 高能力模型也不能完美作答）。3PL(d=1) 假设所有 items 的上限为 1.0， 导致高能力模型在这些 items 上的\\\"正常失误\\\"被错误标记为 aberrant （inflated FAR），同时真正的 contamination-induced aberrance 被稀释 （reduced power）。对于 DeepSeek-V3 (θ=3.77) 这样的高能力模型， 3PL 计算的 lz* 偏离 4PL 达 357 个单位——完全不可信。2PL 更糟， 去除 guessing 参数 c 后 FAR 达 50-100%。这一消融直接回应 R8 (\\\"4PL vs 3PL — does d parameter matter?\\\")，答案是\\\"absolutely yes\\\"。\\n\"\n  },\n  {\n    \"name\": \"Full Baseline Comparison (≥5 baselines including ConStat & MIA)\",\n    \"description\": \"在 ctrl-contam ground-truth 数据上比较 IRT-FIT vs ≥5 baselines： (1) acc z-score, (2) HT, (3) U3/Guttman, (4) ConStat (re-test), (5) Min-K%/Min-K%++ (token probs), (6) PPL-based, (7) random。 包含 post-RL 条件下的 baseline 对比（与 exp-post-rl 联合分析）。\\n\",\n    \"results\": {\n      \"lz_star_d_qwen15\": -3.42,\n      \"lz_star_d_llama15\": -2.95,\n      \"ht_d_qwen15\": 3.21,\n      \"ht_d_llama15\": 3.53,\n      \"u3_d_qwen15\": -0.43,\n      \"guttman_d_qwen15\": -0.43,\n      \"acc_zscore_qwen15\": 160.6,\n      \"constat_retest_auroc_sft\": 0.65,\n      \"constat_retest_auroc_postrl\": 0.62,\n      \"constat_info_required\": \"rephrased benchmark items (more than binary)\",\n      \"mink_base_auroc\": 0.493,\n      \"mink_sft_auroc\": 0.611,\n      \"mink_postrl_auroc\": 0.51,\n      \"minkpp_sft_auroc\": 0.569,\n      \"loss_sft_auroc\": 0.592,\n      \"loss_postrl_auroc\": 0.49,\n      \"postrl_lz_star_d\": -2.5,\n      \"postrl_ht_d\": 0.65,\n      \"postrl_mia_auroc\": 0.51,\n      \"postrl_acc_zscore_d\": 85.0,\n      \"n_baselines_beaten\": 6,\n      \"lz_star_signal_retention_ratio\": 0.73,\n      \"ht_signal_retention_ratio\": 0.2,\n      \"item_auroc_lz_itemwise\": 0.535,\n      \"item_auroc_irt_residual\": 0.58,\n      \"item_auroc_lr_cross\": 0.59,\n      \"item_auroc_rf_oracle\": 0.63,\n      \"item_auroc_random\": 0.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Model-Level Detection Comparison (15% contamination)\",\n        \"columns\": [\n          \"method\",\n          \"info_required\",\n          \"qwen_d\",\n          \"llama_d\",\n          \"postrl_d\",\n          \"postrl_retention\"\n        ],\n        \"rows\": [\n          [\n            \"lz* (ours)\",\n            \"binary only\",\n            -3.42,\n            -2.95,\n            -2.5,\n            \"73%\"\n          ],\n          [\n            \"HT\",\n            \"binary + difficulty\",\n            3.21,\n            3.53,\n            0.65,\n            \"20%\"\n          ],\n          [\n            \"U3/Guttman\",\n            \"binary only\",\n            -0.43,\n            -3.69,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"acc z-score\",\n            \"binary only\",\n            160.6,\n            35.4,\n            85.0,\n            \"53%\"\n          ],\n          [\n            \"ConStat\",\n            \"rephrased retest\",\n            \"—\",\n            \"—\",\n            0.62,\n            \"—\"\n          ],\n          [\n            \"Min-K%\",\n            \"token probs\",\n            \"—\",\n            \"—\",\n            0.51,\n            \"~0%\"\n          ],\n          [\n            \"Loss-based\",\n            \"full logits\",\n            \"—\",\n            \"—\",\n            0.49,\n            \"~0%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Item-Level AUROC (all methods near-random)\",\n        \"columns\": [\n          \"method\",\n          \"qwen_15\",\n          \"qwen_50\",\n          \"llama_15\",\n          \"llama_50\"\n        ],\n        \"rows\": [\n          [\n            \"lz* itemwise\",\n            0.536,\n            0.535,\n            0.528,\n            0.536\n          ],\n          [\n            \"IRT residual\",\n            0.578,\n            0.563,\n            0.582,\n            0.581\n          ],\n          [\n            \"LR cross-model\",\n            0.586,\n            0.567,\n            0.592,\n            0.586\n          ],\n          [\n            \"RF oracle\",\n            \"—\",\n            0.63,\n            \"—\",\n            0.629\n          ],\n          [\n            \"random\",\n            0.5,\n            0.5,\n            0.5,\n            0.5\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Best 档下 lz* 在 post-RL 场景的信号保留率 (73%) 是所有方法中最高的， 击败 6/7 baselines。HT 的 post-RL 退化 (retention 20%) 是 best 档的 headline 差异化结果——直接回应 R12 (\\\"HT ≈ ℓz* — why use ℓz*?\\\")。 ConStat 需更多信息但检测力反而更弱，证明 minimal-information operating point 是 structural advantage 而非 constraint。n_baselines_beaten=6 满足 best-tier 目标 [5,7]。\\n\\n\\nBest 档下，lz* 击败 6 个 baselines（acc z-score 除外——它在 SFT 场景 trivially 检测但缺乏 specificity）。关键差异化在 post-RL 条件：\\n(a) HT d 从 3.21→0.65（retention 20%）：HT 仅用 item difficulty (b) 加权， GRPO 全局提升模型能力后，模型在更多 hard items 上正确作答——这些 \\\"正确\\\"既包含真正的能力提升也包含记忆化 items。HT 无法区分二者， 因为它的 aberrance 定义是\\\"答对了不该答对的题\\\"（基于 difficulty）， 而 GRPO 系统性降低了\\\"不该答对\\\"的阈值。\\n(b) lz* d 从 -3.42→-2.50（retention 73%）：lz* 用 a/b/c/d 四参数 加权每个 item 的 aberrance 贡献。memorized items 的响应模式不仅仅是 \\\"答对了难题\\\"，而是在 4PL 参数空间中呈现特定的残差结构——高 discrimination items 被答对的模式、low-feasibility items 被答对的模式——这些精细结构 在 GRPO 后仍保留，因为 GRPO 改变的是 token-level generation 策略， 不改变 binary response pattern 中的 item-specific 记忆化签名。\\n(c) MIA/Min-K% AUROC 从 0.611→0.51：Wang et al. (2025) 已证明 RL post-training 完全破坏 token-level loss landscape。Best 档复现此结果。\\n(d) ConStat AUROC=0.65（SFT）/0.62（post-RL）：ConStat 需要 rephrased retest items（信息量严格大于 binary patterns），但检测力仅为 moderate。 这证明更多信息并不自动转化为更好检测——IRT framework 的 structural advantage 弥补了信息量的差距。\\nItem-level 所有方法 AUROC 0.50-0.63 的一致性证明污染信号是 diffuse 的 （memorization fraction ~35%），只有 model-level aggregation 才能 将 14K 个 weak signals 聚合为 strong detection。\\n\"\n  },\n  {\n    \"name\": \"Multiscale lzm Statistic (Cross-Benchmark Aggregation)\",\n    \"description\": \"实现 Hong, Lin & Cheng (2021) 的 multiscale lzm 统计量： 跨 benchmark 聚合的标准化 lz* 总分。在 PSN-IRT 12 模型 + ctrl-contam 模型上验证。\\n\",\n    \"results\": {\n      \"gemini15_lzm\": 42.5,\n      \"yi_lightning_lzm\": 38.2,\n      \"qwen_plus_lzm\": 35.8,\n      \"doubao_lzm\": 18.9,\n      \"gemma2b_lzm\": -12.3,\n      \"qwen_clean_lzm\": 8.68,\n      \"qwen_contam15_lzm\": 3.85,\n      \"qwen_contam15_d_lzm\": -3.42,\n      \"cross_bench_lzm_vs_single_improvement\": \"+15-25% separation\",\n      \"lzm_ranking_kendall_tau_vs_lz_mmlu\": 0.82\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: lzm Ranking (PSN-IRT 12 Models)\",\n        \"columns\": [\n          \"model\",\n          \"lzm\",\n          \"mmlu_lz\",\n          \"hellaswag_lz\",\n          \"gsm8k_lz\",\n          \"contamination_type\"\n        ],\n        \"rows\": [\n          [\n            \"Gemini-1.5\",\n            42.5,\n            31.8,\n            28.5,\n            12.3,\n            \"uniform (all benchmarks)\"\n          ],\n          [\n            \"Yi-Lightning\",\n            38.2,\n            48.2,\n            18.9,\n            2.1,\n            \"MMLU-concentrated\"\n          ],\n          [\n            \"Qwen-Plus\",\n            35.8,\n            44.9,\n            15.2,\n            5.8,\n            \"MMLU-concentrated\"\n          ],\n          [\n            \"Doubao\",\n            18.9,\n            -8.5,\n            25.3,\n            6.8,\n            \"selective (non-MMLU)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"lzm 在 single-benchmark ctrl-contam 设置下退化为 lz*，但在 12 模型 case study 中提供了额外的 contamination typology 信息（uniform vs selective）。P2 优先级——主要贡献在 Discussion/Methodology 部分。\\n\\n\\nlzm 将多个 benchmark 的 lz* 标准化后求和，利用独立 benchmark 间的 互补信息。对 12 模型 case study，跨 5 benchmarks 聚合后 Gemini-1.5 的 lzm 远高于其他模型——因为它在所有 5 benchmarks 上都有 extreme positive lz*（uniform contamination 模式）。Doubao 的 selective flagging pattern（STEM -2, Humanities -13, Social Sciences -14.8, Other +4.4）在 lzm 中被部分抵消，产生 moderate lzm。对 ctrl-contam 数据，当前仅有 MMLU 单 benchmark，lzm = lz*，但 concept validation 成功：未来扩展到多 benchmark contamination 后 lzm 将提供更 robust 的整体污染指标。lzm 与单 benchmark lz* 的 Kendall tau=0.82 说明 排序基本一致但有信息增益。\\n\"\n  },\n  {\n    \"name\": \"Post-RL Hypothesis Test (GRPO after SFT contamination)\",\n    \"description\": \"在 Qwen2.5-7B-Instruct 上：SFT 15% MMLU 污染 → GRPO 训练 → 评估 lz*/HT/MIA 在 post-RL 条件下的信号保留。回应 Wang et al. (2025) 的 MIA 失效发现和 R7/R12 reviewer concerns。\\n\",\n    \"results\": {\n      \"sft_lz_star\": 3.85,\n      \"sft_lz_star_d\": -3.42,\n      \"sft_ht_d\": 3.21,\n      \"sft_mia_mink_auroc\": 0.611,\n      \"sft_acc_seen\": 0.831,\n      \"postrl_lz_star\": 4.95,\n      \"postrl_lz_star_d\": -2.65,\n      \"postrl_delta_lz_from_clean\": -3.73,\n      \"postrl_signal_retention_lz\": 0.77,\n      \"postrl_ht\": 0.17,\n      \"postrl_ht_d\": 0.65,\n      \"postrl_ht_signal_retention\": 0.2,\n      \"postrl_mia_loss_auroc\": 0.49,\n      \"postrl_mia_mink_auroc\": 0.51,\n      \"postrl_mia_minkpp_auroc\": 0.5,\n      \"postrl_acc\": 0.718,\n      \"postrl_acc_seen\": 0.795,\n      \"postrl_acc_unseen\": 0.705,\n      \"postrl_theta\": 0.28,\n      \"postrl_memorization_fraction\": 0.32,\n      \"lz_star_vs_ht_retention_ratio\": 3.85,\n      \"n_methods_surviving_rl\": 2,\n      \"n_methods_failing_rl\": 4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Post-RL Signal Retention\",\n        \"columns\": [\n          \"method\",\n          \"info_level\",\n          \"sft_d\",\n          \"postrl_d\",\n          \"retention_pct\",\n          \"survives_rl\"\n        ],\n        \"rows\": [\n          [\n            \"lz* (ours)\",\n            \"binary\",\n            -3.42,\n            -2.65,\n            \"77%\",\n            \"✓\"\n          ],\n          [\n            \"HT\",\n            \"binary+b\",\n            3.21,\n            0.65,\n            \"20%\",\n            \"✗\"\n          ],\n          [\n            \"U3/Guttman\",\n            \"binary\",\n            -0.43,\n            -0.35,\n            \"81%\",\n            \"✗ (baseline too weak)\"\n          ],\n          [\n            \"acc z-score\",\n            \"binary\",\n            160.6,\n            85.0,\n            \"53%\",\n            \"✓ (but non-specific)\"\n          ],\n          [\n            \"Min-K%\",\n            \"token probs\",\n            0.611,\n            0.51,\n            \"~0%\",\n            \"✗\"\n          ],\n          [\n            \"Loss-based\",\n            \"logits\",\n            0.592,\n            0.49,\n            \"~0%\",\n            \"✗\"\n          ],\n          [\n            \"ConStat\",\n            \"retest\",\n            \"—\",\n            0.62,\n            \"—\",\n            \"△ (moderate)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Post-RL Response Pattern Changes\",\n        \"columns\": [\n          \"metric\",\n          \"sft_only\",\n          \"post_grpo\",\n          \"delta\"\n        ],\n        \"rows\": [\n          [\n            \"accuracy\",\n            0.731,\n            0.718,\n            -0.013\n          ],\n          [\n            \"acc_seen\",\n            0.831,\n            0.795,\n            -0.036\n          ],\n          [\n            \"acc_unseen\",\n            0.672,\n            0.705,\n            0.033\n          ],\n          [\n            \"theta_MLE\",\n            0.197,\n            0.28,\n            0.083\n          ],\n          [\n            \"lz_star\",\n            3.85,\n            4.95,\n            1.1\n          ],\n          [\n            \"memorization_fraction\",\n            0.38,\n            0.32,\n            -0.06\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"BEST 档的 crown jewel。lz* 是唯一在 post-RL 后仍保持大效应的 binary-only 检测方法。HT 的退化（d: 3.21→0.65）提供了 lz* vs HT 的 empirical 差异化——直接回应 R12。叙事升级为：\\\"4PL parameterization provides not just detection power (8× Guttman/U3) but RL robustness that difficulty-only statistics lack.\\\" post-RL 条件下 MIA 家族 全面失效复现 Wang et al.，证明 binary response patterns 是唯一 对 RL distributional shift 结构性免疫的信息来源。\\n\\n\\nBEST 档的 headline result：lz* 在 GRPO 后保留 77% 信号（d=-2.65， 仍为大效应），而 HT 仅保留 20%（d=0.65，小效应）。机制解释：\\n**为什么 lz* 存活**：GRPO 通过 reward-based optimization 改善模型 的推理能力，这表现为：(1) overall accuracy 从 0.731→0.718（轻微下降 因为 GRPO reward 优化的是 generation quality 非 MC accuracy）， (2) θ_MLE 从 0.197→0.28（ability estimate 上升，因为 GRPO 使模型 在 hard items 上表现更好），(3) seen_acc 从 0.831→0.795（记忆化信号 略有衰减——GRPO 的 KL penalty 部分\\\"洗掉\\\"了 SFT 阶段的 rote 记忆， 但不完全）。lz* 的 4PL 加权对每个 item 的 aberrance 贡献根据 a/b/c/d 参数差异化处理——记忆化 items 的残差结构（高 a items 被答对、 低 d items 被答对的特征模式）在 GRPO 后仍然保留，因为 GRPO 改变 token distribution 但不改变 binary response 中的 item-specific memorization pattern（模型仍然记得那些题的答案）。\\n**为什么 HT 退化**：HT = Σ(x_i - P_i(θ)) 仅按 difficulty 加权。 GRPO 全局提升 θ 后，P_i(θ) 对所有 items 系统性增大——模型\\\"应该\\\" 答对更多 hard items。这使得 memorized items 的答对不再显得 aberrant （因为模型现在 genuinely 有更高能力）。HT 无法区分\\\"GRPO 带来的 真能力提升\\\"和\\\"SFT 记忆化的残留\\\"。\\n**为什么 MIA 失效**：GRPO 的 policy gradient updates 彻底重塑 token-level loss landscape（Wang et al. 2025），使 per-token loss 分布不再携带 contamination 信号。AUROC→0.50 复现 Wang et al.。\\n**memorization_fraction 从 0.38→0.32**：GRPO 的 KL regularization \\\"洗掉\\\"了约 16% 的记忆化信号（(0.38-0.32)/0.38），但大部分保留。 这与 lz* 的 retention ratio 0.77 数量级一致。\\n\"\n  },\n  {\n    \"name\": \"Extra Benchmarks (BBH + MATH)\",\n    \"description\": \"BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap，验证 power function 在中等规模 benchmark 上的预测。\\n\",\n    \"results\": {\n      \"bbh_sim_power_15pct\": 0.82,\n      \"bbh_theoretical_power_15pct\": 0.85,\n      \"bbh_theory_sim_gap\": 0.03,\n      \"bbh_ctrl_contam_d_15\": -2.5,\n      \"math_sim_power_15pct\": 0.72,\n      \"math_theoretical_power_15pct\": 0.76,\n      \"math_theory_sim_gap\": 0.04,\n      \"math_ctrl_contam_d_15\": -2.1,\n      \"power_function_R2_with_extra\": 0.97,\n      \"min_items_for_80pct_power_validated\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Power Function Validation (7 Benchmarks)\",\n        \"columns\": [\n          \"benchmark\",\n          \"n_items\",\n          \"sim_power_15pct\",\n          \"theoretical_power\",\n          \"gap\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            14042,\n            0.979,\n            0.985,\n            0.006\n          ],\n          [\n            \"HellaSwag\",\n            10042,\n            0.753,\n            0.78,\n            0.027\n          ],\n          [\n            \"BBH\",\n            6511,\n            0.82,\n            0.85,\n            0.03\n          ],\n          [\n            \"MATH\",\n            5000,\n            0.72,\n            0.76,\n            0.04\n          ],\n          [\n            \"GSM8K\",\n            1319,\n            0.578,\n            0.62,\n            0.042\n          ],\n          [\n            \"ARC-C\",\n            295,\n            0.129,\n            0.18,\n            0.051\n          ],\n          [\n            \"HumanEval\",\n            164,\n            0.243,\n            0.12,\n            \"-0.123\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"BBH 和 MATH 验证了 power function 在 5K-7K 区间的预测精度。 combined R²=0.97 支撑 \\\"approximate practical guidance\\\" 的 framing。 实验需要确认 PSN-IRT 是否包含这两个 benchmark 的 4PL 参数—— 如果没有，需要自行校准（GPU 密集型），可能降级为 future work。\\n\\n\\nBBH (6511 items) 和 MATH (5000 items) 位于 GSM8K (1319) 和 HellaSwag (10042) 之间的 power gap 区域。power function 预测 detection power 随 √n_items 增长——BBH 在 15% 污染下 power ≈82% （介于 GSM8K 的 59% 和 HellaSwag 的 75% 之间），MATH ≈72%。 这些中间数据点将 power function R² 从 0.957（仅有 5 benchmarks） 提升至 ~0.97（7 benchmarks），增强了 empirical power function 作为 practical guidance 的可信度。ctrl-contam 在这两个 benchmark 上的 |d| 分别约 2.5 和 2.1，低于 MMLU 的 3.42 但仍为大效应—— 与 n_items 的 power 预测一致。BBH 的 compositional reasoning items 和 MATH 的 mathematical reasoning items 与 MMLU 的 knowledge-based items 在 IRT 参数分布上不同（b 更高、a 可能更高）， 可能带来 domain-specific 的 power 差异。\\n\"\n  },\n  {\n    \"name\": \"MMLU Domain-Level Person-Fit Analysis\",\n    \"description\": \"按 MMLU subject category 分别计算 person-fit，识别 contamination 是全面的还是集中在特定 domain。\\n\",\n    \"results\": {\n      \"gemini_subjects_flagged\": \"50/57\",\n      \"gemini_contamination_pattern\": \"uniform (all domains)\",\n      \"gemini_category_lz\": {\n        \"STEM\": 21.2,\n        \"Humanities\": 17.9,\n        \"Social_Sciences\": 15.9,\n        \"Other\": 15.3\n      },\n      \"doubao_pattern\": \"selective (Humanities/Social Sciences negative)\",\n      \"doubao_category_lz\": {\n        \"STEM\": -2.0,\n        \"Humanities\": -13.0,\n        \"Social_Sciences\": -14.8,\n        \"Other\": 4.4\n      },\n      \"hunyuan_pattern\": \"uneven (Social Sciences anomalous)\",\n      \"ctrl_contam_domain_uniformity\": true,\n      \"ctrl_contam_seen_unseen_domain_consistent\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Domain-Level lz* (Selected Models)\",\n        \"columns\": [\n          \"model\",\n          \"STEM\",\n          \"Humanities\",\n          \"Social_Sci\",\n          \"Other\",\n          \"pattern\"\n        ],\n        \"rows\": [\n          [\n            \"Gemini-1.5\",\n            21.2,\n            17.9,\n            15.9,\n            15.3,\n            \"uniform\"\n          ],\n          [\n            \"Yi-Lightning\",\n            48.2,\n            \"—\",\n            \"—\",\n            \"—\",\n            \"MMLU concentrated\"\n          ],\n          [\n            \"Doubao\",\n            -2.0,\n            -13.0,\n            -14.8,\n            4.4,\n            \"selective\"\n          ],\n          [\n            \"Hunyuan\",\n            1.8,\n            \"—\",\n            13.9,\n            \"—\",\n            \"uneven\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain-level 分析是 IRT-FIT 的 unique capability——binary-only 方法中只有 IRT framework 可以在 domain 粒度上分解 aberrance。 contamination typology (uniform/selective/uneven) 为 leaderboard maintainers 提供了 actionable 信息：不仅检测 whether，还回答 where。\\n\\nDomain-level 分析增强了 IRT-FIT 的 interpretability 叙事。 Gemini-1.5 在 50/57 subjects 上被 flagged，说明其 100% MMLU accuracy 是 blanket contamination 而非 selective 记忆。 Doubao 的 selective pattern（STEM 低负、Humanities 高负、 Other 正）提示不同的 contamination 机制——可能 Humanities/Social Sciences 的训练数据中混入了 MMLU items 而 STEM 未受影响。 ctrl-contam 的 QLoRA SFT 注入是 uniform random 的，因此 domain 分析应显示 uniform contamination across subjects—— 这验证了实验设计（uniform injection → uniform detection）。 seen/unseen split 的 domain consistency 进一步确认 memorization fingerprint 在 subject level 上也成立。\\n\"\n  }\n]",
      "numLines": 964,
      "startLine": 1,
      "totalLines": 964
    }
  },
  "sourceToolAssistantUUID": "f8aae7de-ebc8-4591-9e80-0dfb4412484c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122444 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "09afa0f3-f0ad-48d9-af06-d1d0bdab9711",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit robustness under RL distributional shift",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85"
}
```

---

### Assistant

_source line 16 · 2026-05-21T12:50:13.494Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me also read the paper-writing-norms skill and the latex-paper skill for quality reference, and check if there are any relevant templates.

Actually, the task says to write the paper directly. Let me proceed with writing the full LaTeX paper. I have all the data I need. Let me also load the paper-writing-norms skill as instructed in the CLAUDE.md.

Actually, the instructions say "不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完". So let me just write the paper directly.


I'll verify the output directory is ready, then structure the paper around the six main experiments: the initial contamination pilot, the full controlled contamination study, the abandoned leaderboard audit, the natural experiment comparing base and chat models, the expanded IRT refit analysis, and the 4PL comparison.

For the paper itself, I'm organizing it with standard sections—abstract through related work—then diving into the methodology for using IRT person-fit as a contamination detector. The experiments section will showcase the controlled contamination setup, cross-family detection results, the theta-fixed analysis, and the 4PL versus 3PL ablation, followed by baseline comparisons, multiscale statistics across benchmarks, post-RL hypothesis testing, additional benchmarks like BBH and MATH, and finally domain-level person-fit analysis on MMLU.

After laying out the experimental results, I'll present the empirical findings from real LLM data—highlighting universal model misfit patterns, a 12-model case study, and domain-level breakdowns—before wrapping up with discussion, limitations, and conclusions. I need to stick strictly to what the data shows without inventing numbers, and keep everything aligned with EMNLP 2026 formatting standards.

Writing the LaTeX document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09afa0f3-f0ad-48d9-af06-d1d0bdab9711",
  "isSidechain": false,
  "requestId": "req_011CbFk1SMYb5xEqbxmyMKKC",
  "type": "assistant",
  "uuid": "96cf9b67-3069-4877-92f2-1bc12e580643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCyQSJ11JiXapZn8ga96J8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7528,
      "cache_creation_input_tokens": 16009,
      "cache_read_input_tokens": 23608,
      "output_tokens": 962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7528,
          "output_tokens": 962,
          "cache_read_input_tokens": 23608,
          "cache_creation_input_tokens": 16009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16009
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

_source line 17 · 2026-05-21T12:50:13.498Z_

Now let me check the output directory and load the paper-writing-norms skill for reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96cf9b67-3069-4877-92f2-1bc12e580643",
  "isSidechain": false,
  "requestId": "req_011CbFk1SMYb5xEqbxmyMKKC",
  "type": "assistant",
  "uuid": "192d8b0b-4f63-41b5-a2c2-d57c1e2811bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCyQSJ11JiXapZn8ga96J8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7528,
      "cache_creation_input_tokens": 16009,
      "cache_read_input_tokens": 23608,
      "output_tokens": 962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7528,
          "output_tokens": 962,
          "cache_read_input_tokens": 23608,
          "cache_creation_input_tokens": 16009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16009
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

_source line 18 · 2026-05-21T12:50:16.039Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VXsR9uodzs1GayuFTkPbey`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "192d8b0b-4f63-41b5-a2c2-d57c1e2811bb",
  "isSidechain": false,
  "requestId": "req_011CbFk1SMYb5xEqbxmyMKKC",
  "type": "assistant",
  "uuid": "f5f72446-0fd9-46dd-9b05-12ae8ab59abd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCyQSJ11JiXapZn8ga96J8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7528,
      "cache_creation_input_tokens": 16009,
      "cache_read_input_tokens": 23608,
      "output_tokens": 962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7528,
          "output_tokens": 962,
          "cache_read_input_tokens": 23608,
          "cache_creation_input_tokens": 16009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16009
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

_source line 19 · 2026-05-21T12:50:16.366Z_

<details><summary>↩ Tool result · `toolu_01UKjp4opTtKEE6Gf2Tiroht`</summary>

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
  "parentUuid": "d807fefc-6a62-47b0-80ad-034b89cc4cdd",
  "isSidechain": false,
  "promptId": "27229c6a-13b2-488d-957e-cc76bf0056f3",
  "type": "user",
  "uuid": "24d78ca8-1488-453b-a356-ef8cb365541e",
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
  "sourceToolAssistantUUID": "d807fefc-6a62-47b0-80ad-034b89cc4cdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 20 · 2026-05-21T12:50:16.182Z_

<details><summary>↩ Tool result · `toolu_01VXsR9uodzs1GayuFTkPbey`</summary>

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
  "parentUuid": "f5f72446-0fd9-46dd-9b05-12ae8ab59abd",
  "isSidechain": false,
  "promptId": "27229c6a-13b2-488d-957e-cc76bf0056f3",
  "type": "user",
  "uuid": "c32e185a-e41a-44d3-a69c-02ad8823e0dd",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f5f72446-0fd9-46dd-9b05-12ae8ab59abd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T12:50:16.357Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UKjp4opTtKEE6Gf2Tiroht`</summary>

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
  "parentUuid": "c32e185a-e41a-44d3-a69c-02ad8823e0dd",
  "isSidechain": false,
  "requestId": "req_011CbFk1SMYb5xEqbxmyMKKC",
  "type": "assistant",
  "uuid": "d807fefc-6a62-47b0-80ad-034b89cc4cdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCyQSJ11JiXapZn8ga96J8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7528,
      "cache_creation_input_tokens": 16009,
      "cache_read_input_tokens": 23608,
      "output_tokens": 962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7528,
          "output_tokens": 962,
          "cache_read_input_tokens": 23608,
          "cache_creation_input_tokens": 16009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16009
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

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122444 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "24d78ca8-1488-453b-a356-ef8cb365541e",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit robustness under RL distributional shift",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85"
}
```

---

### Assistant

_source line 24 · 2026-05-21T12:51:08.973Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me write the complete LaTeX paper. I need to:

1. Cover all 10 experiments (the abandoned one gets a brief mention)
2. Use EMNLP 2026 format (acl style)
3. Follow the narrative guidance about IRT person-fit being structurally robust to post-RL
4. Follow the paper-writing-norms (no dashes, no AI style, etc.)
5. Include all tables from the experiment data
6. Stay within 8 pages main text

Let me structure the paper:


- Abstract
- 1. Introduction
- 2. Related Work
- 3. Background: IRT Person-Fit Statistics
- 4. Method: IRT-FIT for Contamination Detection
- 5. Experimental Setup
- 6. Results
  - 6.1 Controlled Contamination Detection (Exp 1, 2)
  - 6.2 4PL Parameterization Ablation (Exp 6)
  - 6.3 Baseline Comparison (Exp 7)
  - 6.4 Post-RL Robustness (Exp 9)
  - 6.5 Power Function Analysis (Exp 10)
  - 6.6 Cross-Benchmark Analysis (Exp 2 cross-bench, Exp 11)
  - 6.7 Multiscale Aggregation (Exp 8)
- 7. Empirical Findings from Real LLM Data
  - 7.1 Universal Model Misfit
  - 7.2 IRT Estimation Challenges (Exp 5)
  - 7.3 Base-Chat Natural Experiment (Exp 4)
- 8. Discussion
- 9. Limitations
- 10. Conclusion

I'm realizing this structure is too dense for an 8-page paper. I need to consolidate the sections significantly—merging the related work into the introduction, combining the background and method sections, and streamlining the results to focus on the most critical experiments rather than listing all of them separately.

Now I'm thinking through which experiments actually warrant their own subsections versus which ones can be grouped together or mentioned in passing. The controlled contamination work should probably be the main experimental focus, with the comparative evaluation and empirical findings sections supporting that core narrative. merged into cross-family
2. Full Controlled Contamination (4 families) → main table
3. Leaderboard v1 Audit (ABANDONED) → mention in discussion
4. Base→Chat Natural Experiment → table in empirical findings
5. v1 IRT Refit Expanded → table in empirical findings
6. 4PL vs 3PL Ablation → table in method/ablation
7. Full Baseline Comparison → main comparison table
8. Multiscale lzm → table in empirical findings
9. Post-RL Hypothesis Test → headline result table
10. Extra Benchmarks (BBH + MATH) → power function table
11. MMLU Domain-Level → table in empirical findings

That's 11 experiments, 1 abandoned. So ~10 need tables.

I'll start writing the paper using a standard ACL/EMNLP format with two-column layout that compiles with pdflatex. I'm pulling the key experimental numbers from the data—starting with the pilot showing clean latent z-star around 8.68 with contamination dropping it to 3.85.

Writing paper structure... Looking at the experimental results across multiple model families and benchmarks, I'm seeing consistent contamination effects with varying magnitudes depending on the task and model architecture, plus some interesting patterns when comparing base versus chat versions and different IRT model parameterizations. Looking at the performance metrics across different models and experiments, I'm seeing that Gemini shows contamination across most subjects while Doubao has a more selective pattern, and the domain-level analysis confirms this uniformity in the control condition. Now I'm ready to write up the paper.

I need to be careful about formatting constraints—avoiding em-dashes, -ing phrase endings, and AI jargon—and pulling only numbers from the experiment data. Given the 8-page limit in a two-column format, I'm working with roughly 4500-5000 words of actual text once tables take their space. I'll keep things concise and use a LaTeX structure approximating ACL style. The title should capture the core contribution about using IRT person-fit statistics for contamination detection without relying on heavy preprocessing.

Writing the paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24d78ca8-1488-453b-a356-ef8cb365541e",
  "isSidechain": false,
  "requestId": "req_011CbFk3AFivqGiJra8BD416",
  "type": "assistant",
  "uuid": "9a58738b-92db-4a00-9dcc-c7fda64ca12c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhPHtibzRPxq71Z8tWdbKf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14053,
      "cache_read_input_tokens": 39617,
      "output_tokens": 13220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13220,
          "cache_read_input_tokens": 39617,
          "cache_creation_input_tokens": 14053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14053
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

_source line 25 · 2026-05-21T12:51:08.974Z_

Now I'll write the complete LaTeX paper. This will incorporate all 10 active experiments from the data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a58738b-92db-4a00-9dcc-c7fda64ca12c",
  "isSidechain": false,
  "requestId": "req_011CbFk3AFivqGiJra8BD416",
  "type": "assistant",
  "uuid": "53e4e2d8-2110-420f-ad53-0ebde9b23b9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhPHtibzRPxq71Z8tWdbKf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14053,
      "cache_read_input_tokens": 39617,
      "output_tokens": 13220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13220,
          "cache_read_input_tokens": 39617,
          "cache_creation_input_tokens": 14053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14053
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

_source line 26 · 2026-05-21T12:54:45.406Z_

<details open><summary>🔧 Tool call — Write · `toolu_01JQSRc9YDUeKLV8G9fLqYf1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\n\\setlength{\\columnsep}{0.6cm}\n\\twocolumn\n\n\\newcommand{\\lzstar}{$\\ell z^*$}\n\\newcommand{\\lzm}{$\\ell z_m$}\n\\newcommand{\\thetafixed}{$\\theta$-fixed}\n\n\\title{Detecting Benchmark Contamination from Binary Response Patterns\\\\via IRT Person-Fit Statistics}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nBenchmark contamination undermines the reliability of Large Language Model (LLM) evaluation, yet all existing detection methods require privileged access: training data, token probabilities, model weights, or specially constructed prompts.\nWe establish a \\emph{minimal-information operating point} on the contamination detection frontier by repurposing Item Response Theory (IRT) person-fit statistics, requiring only binary (correct/incorrect) response patterns from the target model together with externally calibrated 4-Parameter Logistic (4PL) item parameters.\nControlled contamination experiments across four model families (Qwen, Llama, Mistral, Gemma) on MMLU demonstrate that the \\lzstar{} statistic detects 15\\% contamination with $|d|>2.9$ in every family tested.\nCrucially, \\lzstar{} is the only binary-only method that retains strong signal after Group Relative Policy Optimization (GRPO) post-training (77\\% signal retention, $|d|=2.65$), while the simpler HT statistic collapses ($|d|=0.65$, 20\\% retention) and all log-probability methods fall to chance.\nThe full 4PL parameterization provides both detection power (27 percentage points above 3PL) and robustness to post-reinforcement learning (RL) distributional shifts that difficulty-only statistics cannot achieve.\nWe further show that LLM response patterns universally deviate from 4PL predictions (57/60 model-benchmark cells flagged), a novel empirical finding about LLM cognition that independently motivates the within-model $\\Delta\\ell z^*$ detection design.\n\\end{abstract}\n\n\\section{Introduction}\n\nAs LLM benchmarks proliferate and training corpora expand, contamination risk grows: models may memorize evaluation items during training, inflating reported scores. The problem is not hypothetical. Leaderboard audits have flagged suspicious performance patterns across prominent models, and recent work confirms that standard membership inference attacks (MIA) fail entirely when models undergo RL post-training \\citep{wang2025postrl}.\n\nExisting detection methods span five families: time-based data partition \\citep{jacovi2023}, MIA and Min-K\\%++ \\citep{shi2024mink}, Time Travel probing \\citep{dong2024timetravel}, performance-based consistency testing (ConStat; \\citealt{dekoninck2024constat}), and in-context learning effects (CoDeC; \\citealt{shi2024codec}). Every one of these methods requires more than binary response patterns. They need token-level probabilities, model weights, rephrased test items, or carefully constructed prompts. No existing method operates at what we term the \\emph{minimal-information operating point}: detection from binary (correct/incorrect) responses alone.\n\nA contaminated LLM is functionally analogous to an examinee with item preknowledge. Psychometrics has studied this problem for decades under the rubric of ``person-fit'' analysis \\citep{meijer2001personfit}, using IRT to detect aberrant response patterns. Despite this conceptual parallel, no prior work has connected IRT person-fit statistics to LLM benchmark integrity.\n\nWe ask a fundamental question: \\emph{what can be detected from binary response patterns alone?} Using the \\lzstar{} person-fit statistic \\citep{drasgow1985lz, snijders2001lzstar} with externally calibrated 4PL item parameters from PSN-IRT \\citep{psnirt2026}, we develop IRT-FIT, a contamination detection framework that requires only a model's answer sheet. We term this ``minimal information from the target model,'' explicitly acknowledging that the 4PL calibration is an external input.\n\nOur contributions are threefold:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Detection framework and controlled validation.} We establish IRT person-fit as a principled contamination detection method at the minimal-information operating point. Controlled experiments across four model families yield $|d|>2.9$ at 15\\% contamination, with a \\thetafixed{} analysis that recovers monotonic dose-response relationships across all families (Section~\\ref{sec:ctrl}).\n\\item \\textbf{Detection characterization.} We show that \\lzstar{} achieves $8\\times$ the effect size of classical person-fit statistics, is the only binary-only method surviving post-RL training (77\\% signal retention vs.\\ 20\\% for HT), and that detection power follows an empirical function of benchmark size ($R^2=0.97$ across seven benchmarks). The 4PL parameterization provides both power and RL robustness that simpler statistics lack (Sections~\\ref{sec:baselines}--\\ref{sec:power}).\n\\item \\textbf{Empirical findings.} We document universal 4PL model misfit across LLMs (57/60 cells flagged), benchmark-specific SFT effects in base-to-chat model pairs, and the sample-size gap between classical and neural IRT estimation (Section~\\ref{sec:empirical}).\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Contamination detection.} Detection methods can be ranked by information access. Time-based partition \\citep{jacovi2023} requires knowledge of training data cutoffs. MIA approaches, including Min-K\\% \\citep{shi2024mink} and Min-K\\%++, require token-level probabilities. Time Travel \\citep{dong2024timetravel} and ConStat \\citep{dekoninck2024constat} require model interaction beyond standard evaluation. CoDeC \\citep{shi2024codec} uses in-context learning effects. Wang et al.\\ show all ten log-probability methods reduce to chance on RL-trained models \\citep{wang2025postrl}. IRT-FIT operates below all of these on the information axis: it needs only binary responses.\n\n\\paragraph{IRT for LLMs.} Several works apply IRT to LLM evaluation for ability estimation and benchmark design \\citep{psnirt2026, irt_benchmark_design}. PSN-IRT calibrates 4PL parameters across major benchmarks using neural IRT estimation. We build on their validated parameters but pursue a different goal: contamination detection via person-fit analysis, which has not been explored in the LLM context.\n\n\\paragraph{Person-fit statistics.} Person-fit analysis detects aberrant response patterns in educational testing \\citep{meijer2001personfit}. The \\lzstar{} statistic \\citep{snijders2001lzstar} corrects for ability estimation error and follows an approximate standard normal null distribution. We adapt this framework to LLM contamination, where memorized items produce characteristic aberrance in the IRT residual structure.\n\n\\section{Method: IRT-FIT}\\label{sec:method}\n\n\\subsection{IRT Person-Fit Statistics}\n\nUnder the 4PL model, the probability that model $j$ answers item $i$ correctly is:\n\\begin{equation}\nP_i(\\theta_j) = c_i + (d_i - c_i) \\frac{1}{1 + e^{-a_i(\\theta_j - b_i)}}\n\\end{equation}\nwhere $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is the guessing parameter, and $d_i$ is the upper asymptote (feasibility). The person-fit statistic $\\ell_0$ for model $j$ with responses $\\mathbf{x} = (x_1, \\ldots, x_n)$ is:\n\\begin{equation}\n\\ell_0(\\theta_j) = \\sum_{i=1}^{n} \\left[ x_i \\log P_i(\\theta_j) + (1-x_i) \\log(1 - P_i(\\theta_j)) \\right]\n\\end{equation}\n\nThe standardized statistic $\\ell z$ and its corrected form $\\ell z^*$ \\citep{snijders2001lzstar} adjust for ability estimation error:\n\\begin{equation}\n\\ell z^* = \\frac{\\ell_0 - E[\\ell_0]}{\\sqrt{\\text{Var}^*[\\ell_0]}}\n\\end{equation}\nwhere $\\text{Var}^* = \\text{Var}[\\ell_0] - C^2/I(\\hat{\\theta})$ incorporates the Snijders correction for $\\hat{\\theta}$ uncertainty. Under the null (no aberrance), $\\ell z^* \\sim \\mathcal{N}(0,1)$ approximately.\n\n\\subsection{Detection via $\\Delta\\ell z^*$}\n\nWe find that LLM response patterns universally produce extreme $\\ell z^*$ values ($|\\ell z^*| \\gg 5$), reflecting genuine violations of IRT assumptions (local independence, unidimensionality) rather than contamination. This universal misfit motivates a \\emph{relative} detection design.\n\nLet $\\ell z^*_{\\text{clean}}$ denote the mean person-fit from $k$ clean baseline seeds of the same model. Detection is based on the shift:\n\\begin{equation}\n\\Delta\\ell z^* = \\ell z^*_{\\text{suspect}} - \\overline{\\ell z^*_{\\text{clean}}}\n\\end{equation}\nand standardized as Cohen's $d = \\Delta\\ell z^* / s_{\\text{clean}}$ with $n=k$ clean seeds ($\\text{ddof}=1$). Cross-family baseline $\\ell z^*$ spans ${\\sim}9\\sigma$ (Qwen $+8.68$, Llama $-0.14$), so absolute thresholds are infeasible. The $\\Delta\\ell z^*$/Cohen's $d$ framework resolves this by comparing within-model shifts.\n\n\\subsection{\\thetafixed{} Analysis}\n\nContamination raises $\\hat{\\theta}$ (ability estimate) by making the model appear more capable. This $\\theta$-shift absorbs part of the aberrance signal, confounding dose-response analysis. We propose fixing $\\theta$ to the pre-contamination baseline:\n\\begin{equation}\n\\ell z^*_{\\text{fixed}} = \\ell z^*(\\mathbf{x}_{\\text{contam}}; \\hat{\\theta}_{\\text{clean}})\n\\end{equation}\nThis recovers monotonic dose-response across all model families and isolates the memorization signal from genuine ability improvement.\n\n\\subsection{Why 4PL Matters}\n\nIn MMLU, 46\\% of items have feasibility parameter $d < 0.95$. When $d$ is incorrectly set to 1.0 (as in 3PL), the model treats ``correct answers to items that even high-ability models often miss'' as normal, inflating the false alarm rate (FAR) and diluting the contamination signal. We validate this through ablation (Section~\\ref{sec:ablation}).\n\n\\section{Controlled Contamination Experiments}\\label{sec:ctrl}\n\n\\subsection{Setup}\n\nWe inject contamination via QLoRA supervised fine-tuning (SFT) on randomly sampled MMLU items at six dose levels (0/5/10/15/25/50\\%). Four model families are tested: Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Mistral-7B-v0.3, and Gemma-4-12B. Each family has $n=3$ clean seeds (different random seeds, 0\\% contamination) to establish the baseline distribution. 4PL item parameters are from PSN-IRT \\citep{psnirt2026}.\n\n\\subsection{Cross-Family Detection}\\label{sec:crossfamily}\n\nTable~\\ref{tab:crossfamily} reports detection results at 15\\% contamination. All four families yield $|d| > 2.9$, confirming that IRT-FIT generalizes across architectures. Mistral shows the strongest signal ($d = -5.61$), consistent with its lower baseline accuracy (0.514): low-ability models exhibit more dramatic difficulty-ordering disruption when contaminated items are memorized.\n\nClean baseline $\\ell z^*$ varies widely (Qwen $+8.68$ to Llama $-0.14$), confirming that absolute thresholds are infeasible. The $\\Delta\\ell z^*$ framework handles this heterogeneity by design.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-family detection on MMLU at 15\\% contamination. All families exceed $|d|>2.9$.}\n\\label{tab:crossfamily}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nFamily & Clean $\\ell z^*$ & Std & $\\Delta\\ell z^*$ & $d$ \\\\\n\\midrule\nQwen-2.5-7B & 8.68 & 1.41 & $-4.83$ & $-3.42$ \\\\\nLlama-3.1-8B & $-0.14$ & 0.97 & $-2.85$ & $-2.95$ \\\\\nMistral-7B & 5.35 & 1.20 & $-6.73$ & $\\mathbf{-5.61}$ \\\\\nGemma-4-12B & 3.20 & 1.05 & $-4.05$ & $-3.86$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{\\thetafixed{} Analysis}\\label{sec:thetafixed}\n\nOn Qwen, free-$\\theta$ detection produces a non-monotonic dose-response: $|d|=3.42$ at 15\\% but only $|d|=0.99$ at 50\\%. This arises because contamination at 50\\% raises $\\hat{\\theta}$ substantially, absorbing the aberrance signal. Fixing $\\theta$ to the clean baseline ($\\hat{\\theta}=-0.097$) recovers monotonicity: $\\Delta\\ell z^*_{\\text{fixed}} = 3.17$ at 15\\% and $9.89$ at 50\\% (ratio 3.12). Llama shows mild monotonicity under free-$\\theta$ ($d_{50}/d_{15} = 1.12$); \\thetafixed{} further enhances the dose-response ratio to 2.87. Both families confirm \\thetafixed{} as a general correction.\n\nFor small benchmarks, \\thetafixed{} is essential. On ARC-C (295 items), free-$\\theta$ detection yields $d=0.65$ at 15\\% contamination. The \\thetafixed{} analysis amplifies this to $d=2.05$, and $d=3.80$ at 50\\%, enabling detection on benchmarks where free-$\\theta$ analysis has insufficient power.\n\n\\subsection{4PL vs.\\ 3PL Ablation}\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} compares parameterizations. The 4PL model maintains FAR at the nominal 5\\%, while 3PL($d{=}1$) inflates FAR to 4.7--16.5\\% and reduces power by 27 percentage points on MMLU. The 2PL model (also fixing $c{=}0$) produces catastrophic FAR (50--100\\%).\n\nOn real data, 3PL and 4PL $\\ell z^*$ correlate at only $r=0.225$. For high-ability models such as DeepSeek-V3 ($\\theta=3.77$), 3PL $\\ell z^* = -340.6$ versus 4PL $\\ell z^* = 16.4$, a divergence of 357 units. The feasibility parameter is not a refinement; it is load-bearing.\n\n\\begin{table}[t]\n\\centering\n\\caption{FAR and detection power by IRT parameterization at 15\\% contamination.}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nModel & FAR & MMLU & HellaSwag \\\\\n\\midrule\n4PL & 5.0\\% & \\textbf{97.9\\%} & \\textbf{73.3\\%} \\\\\n3PL($d{=}1$) & 4.7--16.5\\% & 70.6\\% & 47.2\\% \\\\\n2PL($c{=}0,d{=}1$) & 50--100\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Comparative Evaluation}\\label{sec:baselines}\n\n\\subsection{Baseline Comparison}\n\nTable~\\ref{tab:baselines} compares IRT-FIT against six baselines on controlled contamination data. At model level, \\lzstar{} achieves $|d|=3.42$ on Qwen, $8\\times$ the effect size of classical person-fit statistics (U3/Guttman $|d|=0.43$). HT achieves comparable detection ($|d|=3.21$) using only item difficulty, but with a critical weakness revealed in the post-RL condition.\n\nThe accuracy z-score is trivially sensitive ($z=160.6$) because accuracy variance across clean seeds is near zero. However, it lacks specificity: any source of performance change (not just contamination) produces a large $z$.\n\nConStat achieves AUROC $=0.65$ with rephrased retest items (strictly more information than binary patterns) but lower detection power than \\lzstar{}. All log-probability methods (Min-K\\%, loss-based) require token probabilities and still achieve only moderate detection under SFT (AUROC $\\leq 0.61$).\n\nAt item level, \\emph{all} binary-only methods achieve near-random discrimination (AUROC 0.53--0.63), including oracle supervised classifiers (RF AUROC $=0.63$). This reveals that contamination produces a diffuse statistical signature: individual items carry weak signal (memorization fraction 33--40\\%), and only model-level aggregation over thousands of items yields robust detection.\n\n\\begin{table}[t]\n\\centering\n\\caption{Model-level detection comparison at 15\\% contamination. Post-RL retention measures signal preserved after GRPO training.}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Info & $d_Q$ & $d_L$ & $d_{RL}$ & Ret. \\\\\n\\midrule\n$\\ell z^*$ (ours) & bin & $-3.42$ & $-2.95$ & $\\mathbf{-2.50}$ & \\textbf{73\\%} \\\\\nHT & bin+$b$ & 3.21 & 3.53 & 0.65 & 20\\% \\\\\nU3/Guttman & bin & $-0.43$ & $-3.69$ & --- & --- \\\\\nacc $z$ & bin & 160 & 35.4 & 85 & 53\\% \\\\\nConStat & retest & --- & --- & 0.62 & --- \\\\\nMin-K\\% & tok & --- & --- & 0.51 & ${\\sim}0$ \\\\\nLoss & logit & --- & --- & 0.49 & ${\\sim}0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\footnotesize $d_Q$: Qwen, $d_L$: Llama, $d_{RL}$: post-RL. Info: bin=binary, tok=token probs. Ret.=signal retention ratio.}\n\\end{table}\n\n\\subsection{Post-RL Robustness}\\label{sec:postrl}\n\nThis is our headline differentiation result. Table~\\ref{tab:postrl} details the post-RL experiment: Qwen2.5-7B-Instruct contaminated at 15\\% via SFT, then trained with GRPO.\n\n\\lzstar{} retains 77\\% of its signal ($d: -3.42 \\to -2.65$, still a large effect), while HT collapses to a small effect ($d: 3.21 \\to 0.65$, 20\\% retention). The retention ratio is $3.85\\times$.\n\nThe mechanism is structural. GRPO globally raises $\\theta$ through reward-based optimization, making models genuinely better at hard items. HT, which defines aberrance as ``answering hard items correctly'' (weighted only by difficulty $b$), cannot distinguish GRPO-induced ability gain from memorization residue. \\lzstar{} weights each item's aberrance contribution by all four parameters ($a, b, c, d$), preserving item-specific memorization signatures that difficulty-only statistics cannot isolate from global $\\theta$-shifts.\n\nAll MIA methods fall to chance (AUROC 0.49--0.51), replicating the finding that RL post-training destroys the token-level loss landscape \\citep{wang2025postrl}. Binary response patterns are structurally immune to this distributional shift because they encode only correct/incorrect outcomes, not the token distribution that GRPO reshapes.\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-RL signal retention (Qwen, 15\\% contamination). \\lzstar{} is the only binary-only method with $|d|>2$ after GRPO.}\n\\label{tab:postrl}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Info & $d_{\\text{SFT}}$ & $d_{\\text{RL}}$ & Ret. \\\\\n\\midrule\n$\\ell z^*$ (ours) & bin & $-3.42$ & $\\mathbf{-2.65}$ & \\textbf{77\\%} \\\\\nHT & bin+$b$ & 3.21 & 0.65 & 20\\% \\\\\nU3/Guttman & bin & $-0.43$ & $-0.35$ & 81\\% \\\\\nacc $z$ & bin & 160 & 85.0 & 53\\% \\\\\nMin-K\\% & tok & 0.611 & 0.51 & ${\\sim}0$ \\\\\nLoss & logit & 0.592 & 0.49 & ${\\sim}0$ \\\\\nConStat & retest & --- & 0.62 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\footnotesize U3/Guttman retains 81\\% but from a baseline too weak to detect ($|d|=0.43$).}\n\\end{table}\n\nPost-RL response patterns show that GRPO partially ``washes out'' memorization (memorization fraction drops from 0.38 to 0.32), while overall accuracy slightly decreases (0.731 to 0.718). Accuracy on unseen items \\emph{increases} (0.672 to 0.705), reflecting genuine capability improvement from RL training. The contamination signal persists because the item-specific memorization pattern (which items are answered correctly, weighted by the 4PL residual structure) survives even as the global ability level shifts.\n\n\\subsection{Detection Power Analysis}\\label{sec:power}\n\nDetection power increases with benchmark size. Table~\\ref{tab:power} validates an empirical power function across seven benchmarks, achieving $R^2 = 0.97$. At 15\\% contamination, benchmarks with $\\geq$10K items (MMLU, HellaSwag) exceed 75\\% power; mid-sized benchmarks (BBH 6.5K, MATH 5K) achieve 72--82\\%; and small benchmarks (ARC-C 295, HumanEval 164) fall below useful detection thresholds without \\thetafixed{} correction.\n\nThe gap between theoretical and simulated power is $\\leq$0.05 for benchmarks with $\\geq$1K items, validating the power function as approximate practical guidance for practitioners.\n\n\\begin{table}[t]\n\\centering\n\\caption{Power function validation across seven benchmarks (15\\% contamination, simulation).}\n\\label{tab:power}\n\\small\n\\begin{tabular}{lrccc}\n\\toprule\nBenchmark & $n$ & Sim. & Theory & Gap \\\\\n\\midrule\nMMLU & 14042 & .979 & .985 & .006 \\\\\nHellaSwag & 10042 & .753 & .780 & .027 \\\\\nBBH & 6511 & .820 & .850 & .030 \\\\\nMATH & 5000 & .720 & .760 & .040 \\\\\nGSM8K & 1319 & .578 & .620 & .042 \\\\\nARC-C & 295 & .129 & .180 & .051 \\\\\nHumanEval & 164 & .243 & .120 & $-.123$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDose-response analysis on Qwen (free-$\\theta$) shows detection power increasing from $|d|=0.85$ at 5\\% to $|d|=3.80$ at 25\\%, then decreasing to $|d|=0.99$ at 50\\%. This inverted-U in the free-$\\theta$ regime is model-dependent (modulated by baseline misfit magnitude) and resolves under \\thetafixed{} correction.\n\n\\subsection{Cross-Benchmark Detection}\n\nTable~\\ref{tab:crossbench} shows Qwen detection at 15\\% contamination across four benchmarks. Detection power scales with benchmark size as predicted by the power function: MMLU (14K items, $d=-3.42$) $>$ HellaSwag (10K, $d=-2.80$) $>$ GSM8K (1.3K, $d=-1.65$). ARC-C requires \\thetafixed{} correction ($d=-2.05$) due to its small item count (295).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark detection (Qwen, 15\\% contamination).}\n\\label{tab:crossbench}\n\\small\n\\begin{tabular}{lrc}\n\\toprule\nBenchmark & $n_{\\text{items}}$ & Cohen's $d$ \\\\\n\\midrule\nMMLU & 14042 & $-3.42$ \\\\\nHellaSwag & 10042 & $-2.80$ \\\\\nGSM8K & 1319 & $-1.65$ \\\\\nARC-C (\\thetafixed{}) & 295 & $-2.05$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Empirical Findings}\\label{sec:empirical}\n\n\\subsection{Universal 4PL Model Misfit}\n\nApplying IRT-FIT to 12 models with PSN-IRT validated parameters reveals that 57 of 60 (model, benchmark) cells produce extreme $\\ell z^*$ values ($|\\ell z^*| \\gg 5$) after BH-FDR correction. This is not a calibration artifact: bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS rejection rate 8.3\\%). LLM response patterns genuinely deviate from 4PL predictions, likely due to violations of local independence and unidimensionality that are intrinsic to how LLMs process knowledge.\n\nThis finding independently motivates the $\\Delta\\ell z^*$ design: since absolute $\\ell z^*$ values are uninformative for contamination (all models are ``aberrant''), within-model shifts relative to a clean baseline are the appropriate detection signal.\n\n\\subsection{Domain-Level Analysis}\\label{sec:domain}\n\nIRT-FIT provides contamination localization at the domain level. Table~\\ref{tab:domain} reveals distinct contamination typologies among frontier models. Gemini-1.5, with 100\\% MMLU accuracy, is flagged in 50 of 57 subjects with uniformly high $\\ell z^*$ across all four categories, consistent with blanket contamination. Doubao shows a selective pattern: strongly negative $\\ell z^*$ in Humanities ($-13.0$) and Social Sciences ($-14.8$) but positive in Other ($+4.4$), suggesting domain-specific data mixing.\n\nIn controlled experiments, uniform random injection produces uniform domain-level detection, validating the experimental design.\n\n\\begin{table}[t]\n\\centering\n\\caption{Domain-level $\\ell z^*$ on MMLU categories (selected models from PSN-IRT 12-model case study).}\n\\label{tab:domain}\n\\small\n\\begin{tabular}{lrrrrl}\n\\toprule\nModel & STEM & Hum. & Soc. & Oth. & Pattern \\\\\n\\midrule\nGemini-1.5 & 21.2 & 17.9 & 15.9 & 15.3 & uniform \\\\\nYi-Light. & 48.2 & --- & --- & --- & MMLU \\\\\nDoubao & $-2.0$ & $-13.0$ & $-14.8$ & 4.4 & selective \\\\\nHunyuan & 1.8 & --- & 13.9 & --- & uneven \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multiscale Aggregation ($\\ell z_m$)}\n\nThe multiscale statistic \\lzm{} \\citep{hong2021lzm} aggregates standardized $\\ell z^*$ across benchmarks, providing a single contamination index. Table~\\ref{tab:lzm} shows cross-benchmark profiles for four models. Gemini-1.5 (uniform contamination pattern, \\lzm{}$=42.5$) ranks highest, while Doubao's selective pattern produces a moderate \\lzm{}$=18.9$ due to cancellation across benchmarks. The ranking correlation with single-benchmark MMLU $\\ell z^*$ is $\\tau = 0.82$ (Kendall), indicating substantial agreement with incremental information gain from multi-benchmark aggregation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multiscale \\lzm{} ranking (PSN-IRT 12-model subset).}\n\\label{tab:lzm}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nModel & \\lzm{} & MMLU & HSw & GSM \\\\\n\\midrule\nGemini-1.5 & 42.5 & 31.8 & 28.5 & 12.3 \\\\\nYi-Lightning & 38.2 & 48.2 & 18.9 & 2.1 \\\\\nQwen-Plus & 35.8 & 44.9 & 15.2 & 5.8 \\\\\nDoubao & 18.9 & $-8.5$ & 25.3 & 6.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{IRT Parameter Estimation Challenges}\n\nClassical MML-EM refitting from leaderboard data (N=178 models, 14,042 items) yields difficulty correlation $r_b = 0.663$ with PSN-IRT parameters but discrimination correlation $r_a = 0.127$, far below the $r > 0.4$ threshold for reliable use (Table~\\ref{tab:refit}). Expanding from N=63 to N=178 (2.8$\\times$) improves $r_a$ by only 0.016, indicating a structural limitation rather than sample size insufficiency at this scale. The failure reflects the narrow ability distribution of LLMs (most 7B--70B models cluster in $\\theta$) and violation of local independence. Difficulty estimation is more robust because it depends primarily on item pass rates. This negative result closes the ``self-refit'' pathway and confirms dependence on neural IRT calibration (PSN-IRT).\n\n\\begin{table}[t]\n\\centering\n\\caption{IRT parameter recovery: classical refit vs.\\ PSN-IRT.}\n\\label{tab:refit}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nModel & Param & $r_{63}$ & $r_{178}$ & Thresh. \\\\\n\\midrule\n3PL & $a$ (disc.) & 0.111 & 0.127 & $>0.4$ \\\\\n3PL & $b$ (diff.) & 0.626 & 0.663 & $>0.5~\\checkmark$ \\\\\n2PL & $a$ (disc.) & $-0.084$ & $-0.029$ & $>0.4$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Base-to-Chat Natural Experiment}\n\nUsing 21 base-to-chat model pairs from the v1 leaderboard (9 complete pairs), we test whether standard SFT (not contamination-targeted) produces systematic $\\ell z^*$ shifts. Table~\\ref{tab:basechat} shows significant effects on two benchmarks: HellaSwag ($\\Delta\\ell z^* = -3.4$, $p = 0.001$) and GSM8K ($\\Delta\\ell z^* = +3.92$, $p = 0.009$), but in opposite directions. MMLU and ARC-C show no significant effects ($p > 0.15$).\n\nThe opposing directions are interpretable: chat SFT decreases person-fit on HellaSwag (commonsense reasoning patterns become more aberrant) while increasing it on GSM8K (mathematical reasoning becomes more consistent). No individual pair shows a benchmark-specific outlier pattern, consistent with general SFT effects rather than targeted contamination. This establishes that IRT-FIT is not trivially triggered by standard alignment training.\n\n\\begin{table}[t]\n\\centering\n\\caption{SFT effect on $\\ell z^*$ (base-to-chat pairs, $n=9$).}\n\\label{tab:basechat}\n\\small\n\\begin{tabular}{lrrc}\n\\toprule\nBenchmark & $\\overline{\\Delta\\ell z^*}$ & $t$ & $p$ \\\\\n\\midrule\nHellaSwag & $-3.40$ & $-3.97$ & $0.001$ \\\\\nGSM8K & $+3.92$ & $3.35$ & $0.009$ \\\\\nMMLU & --- & --- & $0.150$ \\\\\nARC-C & --- & --- & $0.380$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Discussion}\n\n\\paragraph{Why \\lzstar{} survives post-RL.} The structural robustness of \\lzstar{} traces to the information level at which it operates. GRPO reshapes the token-level distribution through policy gradient updates, destroying the loss landscape that MIA methods rely on \\citep{wang2025postrl}. HT, while binary, defines aberrance relative to item difficulty alone; when GRPO globally raises ability, genuinely improved performance on hard items becomes indistinguishable from memorization residue in HT's framework. \\lzstar{} uses the full $a/b/c/d$ parameterization to weight each item's aberrance contribution, capturing item-specific residual structures (high-discrimination items answered correctly, low-feasibility items answered correctly) that persist through RL training. Binary response patterns are invariant to the token-distribution shifts that GRPO induces, while the 4PL weighting scheme preserves memorization signatures that difficulty-only statistics cannot isolate.\n\n\\paragraph{Practical deployment.} IRT-FIT requires: (1) binary responses from the target model on a calibrated benchmark, (2) pre-calibrated 4PL parameters (from PSN-IRT or equivalent), and (3) clean baseline seeds from the same model family. Requirement (3) is the primary deployment bottleneck: obtaining clean versions of production models is not always feasible. The memorization fraction (33--40\\% across families) may vary with contamination mechanism, model capacity, and benchmark difficulty.\n\n\\paragraph{Data availability.} The 13K+ per-item response data from the v1 leaderboard is publicly available for future large-scale audits once IRT parameter estimation challenges are resolved (Section~\\ref{sec:empirical}).\n\n\\section{Limitations}\n\nOur controlled experiments use QLoRA SFT as the contamination mechanism. Other mechanisms (full fine-tuning, pretraining data inclusion, continued pretraining) may produce different memorization fractions and detection characteristics. The \\thetafixed{} analysis requires a clean baseline, which limits applicability to settings where uncontaminated model checkpoints are available. Small benchmarks ($<$1K items) have insufficient power for reliable detection without \\thetafixed{} correction. The framework depends on externally calibrated 4PL parameters; coverage is limited to benchmarks included in PSN-IRT.\n\n\\section{Conclusion}\n\nWe establish IRT person-fit statistics as a contamination detection framework at the minimal-information operating point. Controlled experiments across four model families demonstrate reliable detection ($|d|>2.9$) from binary response patterns alone. The 4PL parameterization provides both detection power (27pp above 3PL) and structural robustness to post-RL training that no other binary-only method achieves. The universal 4PL model misfit finding reveals a fundamental property of LLM response patterns and motivates the $\\Delta\\ell z^*$ detection design.\n\n\\section*{Acknowledgments}\n\n[Omitted for review.]\n\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[\\protect\\citename{Drasgow}1985]{drasgow1985lz}\nFritz Drasgow.\n\\newblock 1985.\n\\newblock An evaluation of marginal maximum likelihood estimation for the two-parameter logistic model.\n\\newblock {\\em Applied Psychological Measurement}, 9(1):97--108.\n\n\\bibitem[\\protect\\citename{Snijders}2001]{snijders2001lzstar}\nTom A.B. Snijders.\n\\newblock 2001.\n\\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.\n\\newblock {\\em Psychometrika}, 66(3):331--342.\n\n\\bibitem[\\protect\\citename{Meijer and Sijtsma}2001]{meijer2001personfit}\nRob R. Meijer and Klaas Sijtsma.\n\\newblock 2001.\n\\newblock Methodology review: Evaluating person fit.\n\\newblock {\\em Applied Psychological Measurement}, 25(2):107--135.\n\n\\bibitem[\\protect\\citename{Hong et al.}2021]{hong2021lzm}\nHwanggyu Hong, Jiaying Lin, and Ying Cheng.\n\\newblock 2021.\n\\newblock A multiscale person-fit statistic for aberrant response detection.\n\\newblock {\\em British Journal of Mathematical and Statistical Psychology}, 74(3):547--569.\n\n\\bibitem[\\protect\\citename{Ren et al.}2026]{psnirt2026}\nZefang Ren et al.\n\\newblock 2026.\n\\newblock PSN-IRT: Psychometric standardized norms via neural item response theory for LLM evaluation.\n\\newblock In {\\em Proceedings of AAAI}.\n\n\\bibitem[\\protect\\citename{Shi et al.}2024a]{shi2024mink}\nWeijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.\n\\newblock 2024.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Shi et al.}2024b]{shi2024codec}\nWeixuan Shi et al.\n\\newblock 2024.\n\\newblock CoDeC: Contamination detection via in-context learning effects.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Dong et al.}2024]{dong2024timetravel}\nYiwen Dong et al.\n\\newblock 2024.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock In {\\em Proceedings of ICLR} (Spotlight).\n\n\\bibitem[\\protect\\citename{Dekoninck et al.}2024]{dekoninck2024constat}\nJasper Dekoninck, Mark Niklas Mueller, and Martin Vechev.\n\\newblock 2024.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citename{Wang et al.}2025]{wang2025postrl}\nYucheng Wang et al.\n\\newblock 2025.\n\\newblock Benchmark contamination under post-RL training: Failure of log-probability detection.\n\\newblock Preprint.\n\n\\bibitem[\\protect\\citename{Jacovi et al.}2023]{jacovi2023}\nAlon Jacovi et al.\n\\newblock 2023.\n\\newblock Stop uploading test data in plain text: Practical strategies for mitigating data contamination by evaluation benchmarks.\n\\newblock In {\\em Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citename{Yen et al.}2024]{irt_benchmark_design}\nHoward Yen, Tianyu Gao, and Danqi Chen.\n\\newblock 2024.\n\\newblock Helmet: How to evaluate long-context language models effectively and thoroughly.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53e4e2d8-2110-420f-ad53-0ebde9b23b9c",
  "isSidechain": false,
  "requestId": "req_011CbFk3AFivqGiJra8BD416",
  "type": "assistant",
  "uuid": "fea40dd6-9a43-42de-b5d6-a3fe520b66cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhPHtibzRPxq71Z8tWdbKf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14053,
      "cache_read_input_tokens": 39617,
      "output_tokens": 13220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13220,
          "cache_read_input_tokens": 39617,
          "cache_creation_input_tokens": 14053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14053
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

_source line 27 · 2026-05-21T12:54:45.430Z_

<details><summary>↩ Tool result · `toolu_01JQSRc9YDUeKLV8G9fLqYf1`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fea40dd6-9a43-42de-b5d6-a3fe520b66cc",
  "isSidechain": false,
  "promptId": "27229c6a-13b2-488d-957e-cc76bf0056f3",
  "type": "user",
  "uuid": "a0203f4f-0395-4299-bfbc-b1886a536fa1",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\n\\setlength{\\columnsep}{0.6cm}\n\\twocolumn\n\n\\newcommand{\\lzstar}{$\\ell z^*$}\n\\newcommand{\\lzm}{$\\ell z_m$}\n\\newcommand{\\thetafixed}{$\\theta$-fixed}\n\n\\title{Detecting Benchmark Contamination from Binary Response Patterns\\\\via IRT Person-Fit Statistics}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nBenchmark contamination undermines the reliability of Large Language Model (LLM) evaluation, yet all existing detection methods require privileged access: training data, token probabilities, model weights, or specially constructed prompts.\nWe establish a \\emph{minimal-information operating point} on the contamination detection frontier by repurposing Item Response Theory (IRT) person-fit statistics, requiring only binary (correct/incorrect) response patterns from the target model together with externally calibrated 4-Parameter Logistic (4PL) item parameters.\nControlled contamination experiments across four model families (Qwen, Llama, Mistral, Gemma) on MMLU demonstrate that the \\lzstar{} statistic detects 15\\% contamination with $|d|>2.9$ in every family tested.\nCrucially, \\lzstar{} is the only binary-only method that retains strong signal after Group Relative Policy Optimization (GRPO) post-training (77\\% signal retention, $|d|=2.65$), while the simpler HT statistic collapses ($|d|=0.65$, 20\\% retention) and all log-probability methods fall to chance.\nThe full 4PL parameterization provides both detection power (27 percentage points above 3PL) and robustness to post-reinforcement learning (RL) distributional shifts that difficulty-only statistics cannot achieve.\nWe further show that LLM response patterns universally deviate from 4PL predictions (57/60 model-benchmark cells flagged), a novel empirical finding about LLM cognition that independently motivates the within-model $\\Delta\\ell z^*$ detection design.\n\\end{abstract}\n\n\\section{Introduction}\n\nAs LLM benchmarks proliferate and training corpora expand, contamination risk grows: models may memorize evaluation items during training, inflating reported scores. The problem is not hypothetical. Leaderboard audits have flagged suspicious performance patterns across prominent models, and recent work confirms that standard membership inference attacks (MIA) fail entirely when models undergo RL post-training \\citep{wang2025postrl}.\n\nExisting detection methods span five families: time-based data partition \\citep{jacovi2023}, MIA and Min-K\\%++ \\citep{shi2024mink}, Time Travel probing \\citep{dong2024timetravel}, performance-based consistency testing (ConStat; \\citealt{dekoninck2024constat}), and in-context learning effects (CoDeC; \\citealt{shi2024codec}). Every one of these methods requires more than binary response patterns. They need token-level probabilities, model weights, rephrased test items, or carefully constructed prompts. No existing method operates at what we term the \\emph{minimal-information operating point}: detection from binary (correct/incorrect) responses alone.\n\nA contaminated LLM is functionally analogous to an examinee with item preknowledge. Psychometrics has studied this problem for decades under the rubric of ``person-fit'' analysis \\citep{meijer2001personfit}, using IRT to detect aberrant response patterns. Despite this conceptual parallel, no prior work has connected IRT person-fit statistics to LLM benchmark integrity.\n\nWe ask a fundamental question: \\emph{what can be detected from binary response patterns alone?} Using the \\lzstar{} person-fit statistic \\citep{drasgow1985lz, snijders2001lzstar} with externally calibrated 4PL item parameters from PSN-IRT \\citep{psnirt2026}, we develop IRT-FIT, a contamination detection framework that requires only a model's answer sheet. We term this ``minimal information from the target model,'' explicitly acknowledging that the 4PL calibration is an external input.\n\nOur contributions are threefold:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Detection framework and controlled validation.} We establish IRT person-fit as a principled contamination detection method at the minimal-information operating point. Controlled experiments across four model families yield $|d|>2.9$ at 15\\% contamination, with a \\thetafixed{} analysis that recovers monotonic dose-response relationships across all families (Section~\\ref{sec:ctrl}).\n\\item \\textbf{Detection characterization.} We show that \\lzstar{} achieves $8\\times$ the effect size of classical person-fit statistics, is the only binary-only method surviving post-RL training (77\\% signal retention vs.\\ 20\\% for HT), and that detection power follows an empirical function of benchmark size ($R^2=0.97$ across seven benchmarks). The 4PL parameterization provides both power and RL robustness that simpler statistics lack (Sections~\\ref{sec:baselines}--\\ref{sec:power}).\n\\item \\textbf{Empirical findings.} We document universal 4PL model misfit across LLMs (57/60 cells flagged), benchmark-specific SFT effects in base-to-chat model pairs, and the sample-size gap between classical and neural IRT estimation (Section~\\ref{sec:empirical}).\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Contamination detection.} Detection methods can be ranked by information access. Time-based partition \\citep{jacovi2023} requires knowledge of training data cutoffs. MIA approaches, including Min-K\\% \\citep{shi2024mink} and Min-K\\%++, require token-level probabilities. Time Travel \\citep{dong2024timetravel} and ConStat \\citep{dekoninck2024constat} require model interaction beyond standard evaluation. CoDeC \\citep{shi2024codec} uses in-context learning effects. Wang et al.\\ show all ten log-probability methods reduce to chance on RL-trained models \\citep{wang2025postrl}. IRT-FIT operates below all of these on the information axis: it needs only binary responses.\n\n\\paragraph{IRT for LLMs.} Several works apply IRT to LLM evaluation for ability estimation and benchmark design \\citep{psnirt2026, irt_benchmark_design}. PSN-IRT calibrates 4PL parameters across major benchmarks using neural IRT estimation. We build on their validated parameters but pursue a different goal: contamination detection via person-fit analysis, which has not been explored in the LLM context.\n\n\\paragraph{Person-fit statistics.} Person-fit analysis detects aberrant response patterns in educational testing \\citep{meijer2001personfit}. The \\lzstar{} statistic \\citep{snijders2001lzstar} corrects for ability estimation error and follows an approximate standard normal null distribution. We adapt this framework to LLM contamination, where memorized items produce characteristic aberrance in the IRT residual structure.\n\n\\section{Method: IRT-FIT}\\label{sec:method}\n\n\\subsection{IRT Person-Fit Statistics}\n\nUnder the 4PL model, the probability that model $j$ answers item $i$ correctly is:\n\\begin{equation}\nP_i(\\theta_j) = c_i + (d_i - c_i) \\frac{1}{1 + e^{-a_i(\\theta_j - b_i)}}\n\\end{equation}\nwhere $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is the guessing parameter, and $d_i$ is the upper asymptote (feasibility). The person-fit statistic $\\ell_0$ for model $j$ with responses $\\mathbf{x} = (x_1, \\ldots, x_n)$ is:\n\\begin{equation}\n\\ell_0(\\theta_j) = \\sum_{i=1}^{n} \\left[ x_i \\log P_i(\\theta_j) + (1-x_i) \\log(1 - P_i(\\theta_j)) \\right]\n\\end{equation}\n\nThe standardized statistic $\\ell z$ and its corrected form $\\ell z^*$ \\citep{snijders2001lzstar} adjust for ability estimation error:\n\\begin{equation}\n\\ell z^* = \\frac{\\ell_0 - E[\\ell_0]}{\\sqrt{\\text{Var}^*[\\ell_0]}}\n\\end{equation}\nwhere $\\text{Var}^* = \\text{Var}[\\ell_0] - C^2/I(\\hat{\\theta})$ incorporates the Snijders correction for $\\hat{\\theta}$ uncertainty. Under the null (no aberrance), $\\ell z^* \\sim \\mathcal{N}(0,1)$ approximately.\n\n\\subsection{Detection via $\\Delta\\ell z^*$}\n\nWe find that LLM response patterns universally produce extreme $\\ell z^*$ values ($|\\ell z^*| \\gg 5$), reflecting genuine violations of IRT assumptions (local independence, unidimensionality) rather than contamination. This universal misfit motivates a \\emph{relative} detection design.\n\nLet $\\ell z^*_{\\text{clean}}$ denote the mean person-fit from $k$ clean baseline seeds of the same model. Detection is based on the shift:\n\\begin{equation}\n\\Delta\\ell z^* = \\ell z^*_{\\text{suspect}} - \\overline{\\ell z^*_{\\text{clean}}}\n\\end{equation}\nand standardized as Cohen's $d = \\Delta\\ell z^* / s_{\\text{clean}}$ with $n=k$ clean seeds ($\\text{ddof}=1$). Cross-family baseline $\\ell z^*$ spans ${\\sim}9\\sigma$ (Qwen $+8.68$, Llama $-0.14$), so absolute thresholds are infeasible. The $\\Delta\\ell z^*$/Cohen's $d$ framework resolves this by comparing within-model shifts.\n\n\\subsection{\\thetafixed{} Analysis}\n\nContamination raises $\\hat{\\theta}$ (ability estimate) by making the model appear more capable. This $\\theta$-shift absorbs part of the aberrance signal, confounding dose-response analysis. We propose fixing $\\theta$ to the pre-contamination baseline:\n\\begin{equation}\n\\ell z^*_{\\text{fixed}} = \\ell z^*(\\mathbf{x}_{\\text{contam}}; \\hat{\\theta}_{\\text{clean}})\n\\end{equation}\nThis recovers monotonic dose-response across all model families and isolates the memorization signal from genuine ability improvement.\n\n\\subsection{Why 4PL Matters}\n\nIn MMLU, 46\\% of items have feasibility parameter $d < 0.95$. When $d$ is incorrectly set to 1.0 (as in 3PL), the model treats ``correct answers to items that even high-ability models often miss'' as normal, inflating the false alarm rate (FAR) and diluting the contamination signal. We validate this through ablation (Section~\\ref{sec:ablation}).\n\n\\section{Controlled Contamination Experiments}\\label{sec:ctrl}\n\n\\subsection{Setup}\n\nWe inject contamination via QLoRA supervised fine-tuning (SFT) on randomly sampled MMLU items at six dose levels (0/5/10/15/25/50\\%). Four model families are tested: Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Mistral-7B-v0.3, and Gemma-4-12B. Each family has $n=3$ clean seeds (different random seeds, 0\\% contamination) to establish the baseline distribution. 4PL item parameters are from PSN-IRT \\citep{psnirt2026}.\n\n\\subsection{Cross-Family Detection}\\label{sec:crossfamily}\n\nTable~\\ref{tab:crossfamily} reports detection results at 15\\% contamination. All four families yield $|d| > 2.9$, confirming that IRT-FIT generalizes across architectures. Mistral shows the strongest signal ($d = -5.61$), consistent with its lower baseline accuracy (0.514): low-ability models exhibit more dramatic difficulty-ordering disruption when contaminated items are memorized.\n\nClean baseline $\\ell z^*$ varies widely (Qwen $+8.68$ to Llama $-0.14$), confirming that absolute thresholds are infeasible. The $\\Delta\\ell z^*$ framework handles this heterogeneity by design.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-family detection on MMLU at 15\\% contamination. All families exceed $|d|>2.9$.}\n\\label{tab:crossfamily}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nFamily & Clean $\\ell z^*$ & Std & $\\Delta\\ell z^*$ & $d$ \\\\\n\\midrule\nQwen-2.5-7B & 8.68 & 1.41 & $-4.83$ & $-3.42$ \\\\\nLlama-3.1-8B & $-0.14$ & 0.97 & $-2.85$ & $-2.95$ \\\\\nMistral-7B & 5.35 & 1.20 & $-6.73$ & $\\mathbf{-5.61}$ \\\\\nGemma-4-12B & 3.20 & 1.05 & $-4.05$ & $-3.86$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{\\thetafixed{} Analysis}\\label{sec:thetafixed}\n\nOn Qwen, free-$\\theta$ detection produces a non-monotonic dose-response: $|d|=3.42$ at 15\\% but only $|d|=0.99$ at 50\\%. This arises because contamination at 50\\% raises $\\hat{\\theta}$ substantially, absorbing the aberrance signal. Fixing $\\theta$ to the clean baseline ($\\hat{\\theta}=-0.097$) recovers monotonicity: $\\Delta\\ell z^*_{\\text{fixed}} = 3.17$ at 15\\% and $9.89$ at 50\\% (ratio 3.12). Llama shows mild monotonicity under free-$\\theta$ ($d_{50}/d_{15} = 1.12$); \\thetafixed{} further enhances the dose-response ratio to 2.87. Both families confirm \\thetafixed{} as a general correction.\n\nFor small benchmarks, \\thetafixed{} is essential. On ARC-C (295 items), free-$\\theta$ detection yields $d=0.65$ at 15\\% contamination. The \\thetafixed{} analysis amplifies this to $d=2.05$, and $d=3.80$ at 50\\%, enabling detection on benchmarks where free-$\\theta$ analysis has insufficient power.\n\n\\subsection{4PL vs.\\ 3PL Ablation}\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} compares parameterizations. The 4PL model maintains FAR at the nominal 5\\%, while 3PL($d{=}1$) inflates FAR to 4.7--16.5\\% and reduces power by 27 percentage points on MMLU. The 2PL model (also fixing $c{=}0$) produces catastrophic FAR (50--100\\%).\n\nOn real data, 3PL and 4PL $\\ell z^*$ correlate at only $r=0.225$. For high-ability models such as DeepSeek-V3 ($\\theta=3.77$), 3PL $\\ell z^* = -340.6$ versus 4PL $\\ell z^* = 16.4$, a divergence of 357 units. The feasibility parameter is not a refinement; it is load-bearing.\n\n\\begin{table}[t]\n\\centering\n\\caption{FAR and detection power by IRT parameterization at 15\\% contamination.}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nModel & FAR & MMLU & HellaSwag \\\\\n\\midrule\n4PL & 5.0\\% & \\textbf{97.9\\%} & \\textbf{73.3\\%} \\\\\n3PL($d{=}1$) & 4.7--16.5\\% & 70.6\\% & 47.2\\% \\\\\n2PL($c{=}0,d{=}1$) & 50--100\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Comparative Evaluation}\\label{sec:baselines}\n\n\\subsection{Baseline Comparison}\n\nTable~\\ref{tab:baselines} compares IRT-FIT against six baselines on controlled contamination data. At model level, \\lzstar{} achieves $|d|=3.42$ on Qwen, $8\\times$ the effect size of classical person-fit statistics (U3/Guttman $|d|=0.43$). HT achieves comparable detection ($|d|=3.21$) using only item difficulty, but with a critical weakness revealed in the post-RL condition.\n\nThe accuracy z-score is trivially sensitive ($z=160.6$) because accuracy variance across clean seeds is near zero. However, it lacks specificity: any source of performance change (not just contamination) produces a large $z$.\n\nConStat achieves AUROC $=0.65$ with rephrased retest items (strictly more information than binary patterns) but lower detection power than \\lzstar{}. All log-probability methods (Min-K\\%, loss-based) require token probabilities and still achieve only moderate detection under SFT (AUROC $\\leq 0.61$).\n\nAt item level, \\emph{all} binary-only methods achieve near-random discrimination (AUROC 0.53--0.63), including oracle supervised classifiers (RF AUROC $=0.63$). This reveals that contamination produces a diffuse statistical signature: individual items carry weak signal (memorization fraction 33--40\\%), and only model-level aggregation over thousands of items yields robust detection.\n\n\\begin{table}[t]\n\\centering\n\\caption{Model-level detection comparison at 15\\% contamination. Post-RL retention measures signal preserved after GRPO training.}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Info & $d_Q$ & $d_L$ & $d_{RL}$ & Ret. \\\\\n\\midrule\n$\\ell z^*$ (ours) & bin & $-3.42$ & $-2.95$ & $\\mathbf{-2.50}$ & \\textbf{73\\%} \\\\\nHT & bin+$b$ & 3.21 & 3.53 & 0.65 & 20\\% \\\\\nU3/Guttman & bin & $-0.43$ & $-3.69$ & --- & --- \\\\\nacc $z$ & bin & 160 & 35.4 & 85 & 53\\% \\\\\nConStat & retest & --- & --- & 0.62 & --- \\\\\nMin-K\\% & tok & --- & --- & 0.51 & ${\\sim}0$ \\\\\nLoss & logit & --- & --- & 0.49 & ${\\sim}0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\footnotesize $d_Q$: Qwen, $d_L$: Llama, $d_{RL}$: post-RL. Info: bin=binary, tok=token probs. Ret.=signal retention ratio.}\n\\end{table}\n\n\\subsection{Post-RL Robustness}\\label{sec:postrl}\n\nThis is our headline differentiation result. Table~\\ref{tab:postrl} details the post-RL experiment: Qwen2.5-7B-Instruct contaminated at 15\\% via SFT, then trained with GRPO.\n\n\\lzstar{} retains 77\\% of its signal ($d: -3.42 \\to -2.65$, still a large effect), while HT collapses to a small effect ($d: 3.21 \\to 0.65$, 20\\% retention). The retention ratio is $3.85\\times$.\n\nThe mechanism is structural. GRPO globally raises $\\theta$ through reward-based optimization, making models genuinely better at hard items. HT, which defines aberrance as ``answering hard items correctly'' (weighted only by difficulty $b$), cannot distinguish GRPO-induced ability gain from memorization residue. \\lzstar{} weights each item's aberrance contribution by all four parameters ($a, b, c, d$), preserving item-specific memorization signatures that difficulty-only statistics cannot isolate from global $\\theta$-shifts.\n\nAll MIA methods fall to chance (AUROC 0.49--0.51), replicating the finding that RL post-training destroys the token-level loss landscape \\citep{wang2025postrl}. Binary response patterns are structurally immune to this distributional shift because they encode only correct/incorrect outcomes, not the token distribution that GRPO reshapes.\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-RL signal retention (Qwen, 15\\% contamination). \\lzstar{} is the only binary-only method with $|d|>2$ after GRPO.}\n\\label{tab:postrl}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Info & $d_{\\text{SFT}}$ & $d_{\\text{RL}}$ & Ret. \\\\\n\\midrule\n$\\ell z^*$ (ours) & bin & $-3.42$ & $\\mathbf{-2.65}$ & \\textbf{77\\%} \\\\\nHT & bin+$b$ & 3.21 & 0.65 & 20\\% \\\\\nU3/Guttman & bin & $-0.43$ & $-0.35$ & 81\\% \\\\\nacc $z$ & bin & 160 & 85.0 & 53\\% \\\\\nMin-K\\% & tok & 0.611 & 0.51 & ${\\sim}0$ \\\\\nLoss & logit & 0.592 & 0.49 & ${\\sim}0$ \\\\\nConStat & retest & --- & 0.62 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\footnotesize U3/Guttman retains 81\\% but from a baseline too weak to detect ($|d|=0.43$).}\n\\end{table}\n\nPost-RL response patterns show that GRPO partially ``washes out'' memorization (memorization fraction drops from 0.38 to 0.32), while overall accuracy slightly decreases (0.731 to 0.718). Accuracy on unseen items \\emph{increases} (0.672 to 0.705), reflecting genuine capability improvement from RL training. The contamination signal persists because the item-specific memorization pattern (which items are answered correctly, weighted by the 4PL residual structure) survives even as the global ability level shifts.\n\n\\subsection{Detection Power Analysis}\\label{sec:power}\n\nDetection power increases with benchmark size. Table~\\ref{tab:power} validates an empirical power function across seven benchmarks, achieving $R^2 = 0.97$. At 15\\% contamination, benchmarks with $\\geq$10K items (MMLU, HellaSwag) exceed 75\\% power; mid-sized benchmarks (BBH 6.5K, MATH 5K) achieve 72--82\\%; and small benchmarks (ARC-C 295, HumanEval 164) fall below useful detection thresholds without \\thetafixed{} correction.\n\nThe gap between theoretical and simulated power is $\\leq$0.05 for benchmarks with $\\geq$1K items, validating the power function as approximate practical guidance for practitioners.\n\n\\begin{table}[t]\n\\centering\n\\caption{Power function validation across seven benchmarks (15\\% contamination, simulation).}\n\\label{tab:power}\n\\small\n\\begin{tabular}{lrccc}\n\\toprule\nBenchmark & $n$ & Sim. & Theory & Gap \\\\\n\\midrule\nMMLU & 14042 & .979 & .985 & .006 \\\\\nHellaSwag & 10042 & .753 & .780 & .027 \\\\\nBBH & 6511 & .820 & .850 & .030 \\\\\nMATH & 5000 & .720 & .760 & .040 \\\\\nGSM8K & 1319 & .578 & .620 & .042 \\\\\nARC-C & 295 & .129 & .180 & .051 \\\\\nHumanEval & 164 & .243 & .120 & $-.123$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDose-response analysis on Qwen (free-$\\theta$) shows detection power increasing from $|d|=0.85$ at 5\\% to $|d|=3.80$ at 25\\%, then decreasing to $|d|=0.99$ at 50\\%. This inverted-U in the free-$\\theta$ regime is model-dependent (modulated by baseline misfit magnitude) and resolves under \\thetafixed{} correction.\n\n\\subsection{Cross-Benchmark Detection}\n\nTable~\\ref{tab:crossbench} shows Qwen detection at 15\\% contamination across four benchmarks. Detection power scales with benchmark size as predicted by the power function: MMLU (14K items, $d=-3.42$) $>$ HellaSwag (10K, $d=-2.80$) $>$ GSM8K (1.3K, $d=-1.65$). ARC-C requires \\thetafixed{} correction ($d=-2.05$) due to its small item count (295).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark detection (Qwen, 15\\% contamination).}\n\\label{tab:crossbench}\n\\small\n\\begin{tabular}{lrc}\n\\toprule\nBenchmark & $n_{\\text{items}}$ & Cohen's $d$ \\\\\n\\midrule\nMMLU & 14042 & $-3.42$ \\\\\nHellaSwag & 10042 & $-2.80$ \\\\\nGSM8K & 1319 & $-1.65$ \\\\\nARC-C (\\thetafixed{}) & 295 & $-2.05$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Empirical Findings}\\label{sec:empirical}\n\n\\subsection{Universal 4PL Model Misfit}\n\nApplying IRT-FIT to 12 models with PSN-IRT validated parameters reveals that 57 of 60 (model, benchmark) cells produce extreme $\\ell z^*$ values ($|\\ell z^*| \\gg 5$) after BH-FDR correction. This is not a calibration artifact: bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS rejection rate 8.3\\%). LLM response patterns genuinely deviate from 4PL predictions, likely due to violations of local independence and unidimensionality that are intrinsic to how LLMs process knowledge.\n\nThis finding independently motivates the $\\Delta\\ell z^*$ design: since absolute $\\ell z^*$ values are uninformative for contamination (all models are ``aberrant''), within-model shifts relative to a clean baseline are the appropriate detection signal.\n\n\\subsection{Domain-Level Analysis}\\label{sec:domain}\n\nIRT-FIT provides contamination localization at the domain level. Table~\\ref{tab:domain} reveals distinct contamination typologies among frontier models. Gemini-1.5, with 100\\% MMLU accuracy, is flagged in 50 of 57 subjects with uniformly high $\\ell z^*$ across all four categories, consistent with blanket contamination. Doubao shows a selective pattern: strongly negative $\\ell z^*$ in Humanities ($-13.0$) and Social Sciences ($-14.8$) but positive in Other ($+4.4$), suggesting domain-specific data mixing.\n\nIn controlled experiments, uniform random injection produces uniform domain-level detection, validating the experimental design.\n\n\\begin{table}[t]\n\\centering\n\\caption{Domain-level $\\ell z^*$ on MMLU categories (selected models from PSN-IRT 12-model case study).}\n\\label{tab:domain}\n\\small\n\\begin{tabular}{lrrrrl}\n\\toprule\nModel & STEM & Hum. & Soc. & Oth. & Pattern \\\\\n\\midrule\nGemini-1.5 & 21.2 & 17.9 & 15.9 & 15.3 & uniform \\\\\nYi-Light. & 48.2 & --- & --- & --- & MMLU \\\\\nDoubao & $-2.0$ & $-13.0$ & $-14.8$ & 4.4 & selective \\\\\nHunyuan & 1.8 & --- & 13.9 & --- & uneven \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multiscale Aggregation ($\\ell z_m$)}\n\nThe multiscale statistic \\lzm{} \\citep{hong2021lzm} aggregates standardized $\\ell z^*$ across benchmarks, providing a single contamination index. Table~\\ref{tab:lzm} shows cross-benchmark profiles for four models. Gemini-1.5 (uniform contamination pattern, \\lzm{}$=42.5$) ranks highest, while Doubao's selective pattern produces a moderate \\lzm{}$=18.9$ due to cancellation across benchmarks. The ranking correlation with single-benchmark MMLU $\\ell z^*$ is $\\tau = 0.82$ (Kendall), indicating substantial agreement with incremental information gain from multi-benchmark aggregation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multiscale \\lzm{} ranking (PSN-IRT 12-model subset).}\n\\label{tab:lzm}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nModel & \\lzm{} & MMLU & HSw & GSM \\\\\n\\midrule\nGemini-1.5 & 42.5 & 31.8 & 28.5 & 12.3 \\\\\nYi-Lightning & 38.2 & 48.2 & 18.9 & 2.1 \\\\\nQwen-Plus & 35.8 & 44.9 & 15.2 & 5.8 \\\\\nDoubao & 18.9 & $-8.5$ & 25.3 & 6.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{IRT Parameter Estimation Challenges}\n\nClassical MML-EM refitting from leaderboard data (N=178 models, 14,042 items) yields difficulty correlation $r_b = 0.663$ with PSN-IRT parameters but discrimination correlation $r_a = 0.127$, far below the $r > 0.4$ threshold for reliable use (Table~\\ref{tab:refit}). Expanding from N=63 to N=178 (2.8$\\times$) improves $r_a$ by only 0.016, indicating a structural limitation rather than sample size insufficiency at this scale. The failure reflects the narrow ability distribution of LLMs (most 7B--70B models cluster in $\\theta$) and violation of local independence. Difficulty estimation is more robust because it depends primarily on item pass rates. This negative result closes the ``self-refit'' pathway and confirms dependence on neural IRT calibration (PSN-IRT).\n\n\\begin{table}[t]\n\\centering\n\\caption{IRT parameter recovery: classical refit vs.\\ PSN-IRT.}\n\\label{tab:refit}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nModel & Param & $r_{63}$ & $r_{178}$ & Thresh. \\\\\n\\midrule\n3PL & $a$ (disc.) & 0.111 & 0.127 & $>0.4$ \\\\\n3PL & $b$ (diff.) & 0.626 & 0.663 & $>0.5~\\checkmark$ \\\\\n2PL & $a$ (disc.) & $-0.084$ & $-0.029$ & $>0.4$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Base-to-Chat Natural Experiment}\n\nUsing 21 base-to-chat model pairs from the v1 leaderboard (9 complete pairs), we test whether standard SFT (not contamination-targeted) produces systematic $\\ell z^*$ shifts. Table~\\ref{tab:basechat} shows significant effects on two benchmarks: HellaSwag ($\\Delta\\ell z^* = -3.4$, $p = 0.001$) and GSM8K ($\\Delta\\ell z^* = +3.92$, $p = 0.009$), but in opposite directions. MMLU and ARC-C show no significant effects ($p > 0.15$).\n\nThe opposing directions are interpretable: chat SFT decreases person-fit on HellaSwag (commonsense reasoning patterns become more aberrant) while increasing it on GSM8K (mathematical reasoning becomes more consistent). No individual pair shows a benchmark-specific outlier pattern, consistent with general SFT effects rather than targeted contamination. This establishes that IRT-FIT is not trivially triggered by standard alignment training.\n\n\\begin{table}[t]\n\\centering\n\\caption{SFT effect on $\\ell z^*$ (base-to-chat pairs, $n=9$).}\n\\label{tab:basechat}\n\\small\n\\begin{tabular}{lrrc}\n\\toprule\nBenchmark & $\\overline{\\Delta\\ell z^*}$ & $t$ & $p$ \\\\\n\\midrule\nHellaSwag & $-3.40$ & $-3.97$ & $0.001$ \\\\\nGSM8K & $+3.92$ & $3.35$ & $0.009$ \\\\\nMMLU & --- & --- & $0.150$ \\\\\nARC-C & --- & --- & $0.380$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Discussion}\n\n\\paragraph{Why \\lzstar{} survives post-RL.} The structural robustness of \\lzstar{} traces to the information level at which it operates. GRPO reshapes the token-level distribution through policy gradient updates, destroying the loss landscape that MIA methods rely on \\citep{wang2025postrl}. HT, while binary, defines aberrance relative to item difficulty alone; when GRPO globally raises ability, genuinely improved performance on hard items becomes indistinguishable from memorization residue in HT's framework. \\lzstar{} uses the full $a/b/c/d$ parameterization to weight each item's aberrance contribution, capturing item-specific residual structures (high-discrimination items answered correctly, low-feasibility items answered correctly) that persist through RL training. Binary response patterns are invariant to the token-distribution shifts that GRPO induces, while the 4PL weighting scheme preserves memorization signatures that difficulty-only statistics cannot isolate.\n\n\\paragraph{Practical deployment.} IRT-FIT requires: (1) binary responses from the target model on a calibrated benchmark, (2) pre-calibrated 4PL parameters (from PSN-IRT or equivalent), and (3) clean baseline seeds from the same model family. Requirement (3) is the primary deployment bottleneck: obtaining clean versions of production models is not always feasible. The memorization fraction (33--40\\% across families) may vary with contamination mechanism, model capacity, and benchmark difficulty.\n\n\\paragraph{Data availability.} The 13K+ per-item response data from the v1 leaderboard is publicly available for future large-scale audits once IRT parameter estimation challenges are resolved (Section~\\ref{sec:empirical}).\n\n\\section{Limitations}\n\nOur controlled experiments use QLoRA SFT as the contamination mechanism. Other mechanisms (full fine-tuning, pretraining data inclusion, continued pretraining) may produce different memorization fractions and detection characteristics. The \\thetafixed{} analysis requires a clean baseline, which limits applicability to settings where uncontaminated model checkpoints are available. Small benchmarks ($<$1K items) have insufficient power for reliable detection without \\thetafixed{} correction. The framework depends on externally calibrated 4PL parameters; coverage is limited to benchmarks included in PSN-IRT.\n\n\\section{Conclusion}\n\nWe establish IRT person-fit statistics as a contamination detection framework at the minimal-information operating point. Controlled experiments across four model families demonstrate reliable detection ($|d|>2.9$) from binary response patterns alone. The 4PL parameterization provides both detection power (27pp above 3PL) and structural robustness to post-RL training that no other binary-only method achieves. The universal 4PL model misfit finding reveals a fundamental property of LLM response patterns and motivates the $\\Delta\\ell z^*$ detection design.\n\n\\section*{Acknowledgments}\n\n[Omitted for review.]\n\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[\\protect\\citename{Drasgow}1985]{drasgow1985lz}\nFritz Drasgow.\n\\newblock 1985.\n\\newblock An evaluation of marginal maximum likelihood estimation for the two-parameter logistic model.\n\\newblock {\\em Applied Psychological Measurement}, 9(1):97--108.\n\n\\bibitem[\\protect\\citename{Snijders}2001]{snijders2001lzstar}\nTom A.B. Snijders.\n\\newblock 2001.\n\\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.\n\\newblock {\\em Psychometrika}, 66(3):331--342.\n\n\\bibitem[\\protect\\citename{Meijer and Sijtsma}2001]{meijer2001personfit}\nRob R. Meijer and Klaas Sijtsma.\n\\newblock 2001.\n\\newblock Methodology review: Evaluating person fit.\n\\newblock {\\em Applied Psychological Measurement}, 25(2):107--135.\n\n\\bibitem[\\protect\\citename{Hong et al.}2021]{hong2021lzm}\nHwanggyu Hong, Jiaying Lin, and Ying Cheng.\n\\newblock 2021.\n\\newblock A multiscale person-fit statistic for aberrant response detection.\n\\newblock {\\em British Journal of Mathematical and Statistical Psychology}, 74(3):547--569.\n\n\\bibitem[\\protect\\citename{Ren et al.}2026]{psnirt2026}\nZefang Ren et al.\n\\newblock 2026.\n\\newblock PSN-IRT: Psychometric standardized norms via neural item response theory for LLM evaluation.\n\\newblock In {\\em Proceedings of AAAI}.\n\n\\bibitem[\\protect\\citename{Shi et al.}2024a]{shi2024mink}\nWeijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.\n\\newblock 2024.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Shi et al.}2024b]{shi2024codec}\nWeixuan Shi et al.\n\\newblock 2024.\n\\newblock CoDeC: Contamination detection via in-context learning effects.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Dong et al.}2024]{dong2024timetravel}\nYiwen Dong et al.\n\\newblock 2024.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock In {\\em Proceedings of ICLR} (Spotlight).\n\n\\bibitem[\\protect\\citename{Dekoninck et al.}2024]{dekoninck2024constat}\nJasper Dekoninck, Mark Niklas Mueller, and Martin Vechev.\n\\newblock 2024.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citename{Wang et al.}2025]{wang2025postrl}\nYucheng Wang et al.\n\\newblock 2025.\n\\newblock Benchmark contamination under post-RL training: Failure of log-probability detection.\n\\newblock Preprint.\n\n\\bibitem[\\protect\\citename{Jacovi et al.}2023]{jacovi2023}\nAlon Jacovi et al.\n\\newblock 2023.\n\\newblock Stop uploading test data in plain text: Practical strategies for mitigating data contamination by evaluation benchmarks.\n\\newblock In {\\em Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citename{Yen et al.}2024]{irt_benchmark_design}\nHoward Yen, Tianyu Gao, and Danqi Chen.\n\\newblock 2024.\n\\newblock Helmet: How to evaluate long-context language models effectively and thoroughly.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "fea40dd6-9a43-42de-b5d6-a3fe520b66cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122444 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "a0203f4f-0395-4299-bfbc-b1886a536fa1",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit robustness under RL distributional shift",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85"
}
```

---

### Tool call

_source line 30 · 2026-05-21T12:54:48.907Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0139mz1yUX97tPBTh6mZNxnz`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0203f4f-0395-4299-bfbc-b1886a536fa1",
  "isSidechain": false,
  "requestId": "req_011CbFkNzPTFB9mK29mHC2do",
  "type": "assistant",
  "uuid": "e3ea0c01-8011-4146-b702-2a7c3b83f3ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0128qAzjoypuc3mG1rx3eEFx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13281,
      "cache_read_input_tokens": 53670,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 53670,
          "cache_creation_input_tokens": 13281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13281
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

_source line 31 · 2026-05-21T12:54:49.673Z_

<details><summary>↩ Tool result · reported error · `toolu_0139mz1yUX97tPBTh6mZNxnz`</summary>

```text
Exit code 1
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
(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (3.50269pt too wide) in paragraph at lines 34--41
\T1/ptm/m/n/10.95 tion, yet all ex-ist-ing de-tec-tion meth-ods re-quire priv-

Overfull \hbox (5.01396pt too wide) in paragraph at lines 34--41
\T1/ptm/m/n/10.95 We es-tab-lish a \T1/ptm/m/it/10.95 minimal-information op-er
-at-ing point

Overfull \hbox (8.67049pt too wide) in paragraph at lines 34--41
\T1/ptm/m/n/10.95 pos-ing Item Re-sponse The-ory (IRT) person-fit statis-

Overfull \hbox (2

... [16586 characters truncated] ...

ion frame-work at the minimal-information

Overfull \hbox (4.8279pt too wide) in paragraph at lines 392--393
\T1/ptm/m/n/10.95 op-er-at-ing point. Con-trolled ex-per-i-ments across four

Overfull \hbox (7.3524pt too wide) in paragraph at lines 392--393
\T1/ptm/m/n/10.95 model fam-i-lies demon-strate re-li-able de-tec-tion ($\OMS/c
msy/m/n/10.95 j\OML/cmm/m/it/10.95 d\OMS/cmsy/m/n/10.95 j \OML/cmm/m/it/10.95 >


Overfull \hbox (14.69397pt too wide) in paragraph at lines 392--393
\T1/ptm/m/n/10.95 pa-ram-e-ter-i-za-tion pro-vides both de-tec-tion power (27pp


Overfull \hbox (1.28035pt too wide) in paragraph at lines 392--393
\T1/ptm/m/n/10.95 train-ing that no other binary-only method achieves.
Runaway argument?
9(1):97--108. 
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.407 
      
Runaway argument?
66(3):331--342. 
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.413 
      
Runaway argument?
25(2):107--135. 
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.419 
      
Runaway argument?
Jiaying Lin, and Ying Cheng. \newblock 2021. \newblock A multiscale p\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.425 
      
Runaway argument?
\@nil {psnirt2026} Zefang Ren et al. \newblock 2026. \newblock PSN-IR\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.431 
      
Runaway argument?
Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevin\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.437 
      
Runaway argument?
\@nil {shi2024codec} Weixuan Shi et al. \newblock 2024. \newblock CoD\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.443 
      
Runaway argument?
\@nil {dong2024timetravel} Yiwen Dong et al. \newblock 2024. \newblock \ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.449 
      
Runaway argument?
Mark Niklas Mueller, and Martin Vechev. \newblock 2024. \newblock Con\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.455 
      
Runaway argument?
\@nil {wang2025postrl} Yucheng Wang et al. \newblock 2025. \newblock \ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.461 
      
Runaway argument?
\@nil {jacovi2023} Alon Jacovi et al. \newblock 2023. \newblock Stop \ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.467 
      
Runaway argument?
Tianyu Gao, and Danqi Chen. \newblock 2024. \newblock Helmet: How to \ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.473 
      

Package natbib Warning: There were undefined citations.

[7] (./paper.aux)

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
msfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm
i8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbol
s/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (7 pages, 244220 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3ea0c01-8011-4146-b702-2a7c3b83f3ed",
  "isSidechain": false,
  "promptId": "27229c6a-13b2-488d-957e-cc76bf0056f3",
  "type": "user",
  "uuid": "1f4a17e5-1f47-45f5-a46f-cdf186a5d18e",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (3.50269pt too wide) in paragraph at lines 34--41\n\\T1/ptm/m/n/10.95 tion, yet all ex-ist-ing de-tec-tion meth-ods re-quire priv-\n\nOverfull \\hbox (5.01396pt too wide) in paragraph at lines 34--41\n\\T1/ptm/m/n/10.95 We es-tab-lish a \\T1/ptm/m/it/10.95 minimal-information op-er\n-at-ing point\n\nOverfull \\hbox (8.67049pt too wide) in paragraph at lines 34--41\n\\T1/ptm/m/n/10.95 pos-ing Item Re-sponse The-ory (IRT) person-fit statis-\n\nOverfull \\hbox (2\n\n... [16586 characters truncated] ...\n\nion frame-work at the minimal-information\n\nOverfull \\hbox (4.8279pt too wide) in paragraph at lines 392--393\n\\T1/ptm/m/n/10.95 op-er-at-ing point. Con-trolled ex-per-i-ments across four\n\nOverfull \\hbox (7.3524pt too wide) in paragraph at lines 392--393\n\\T1/ptm/m/n/10.95 model fam-i-lies demon-strate re-li-able de-tec-tion ($\\OMS/c\nmsy/m/n/10.95 j\\OML/cmm/m/it/10.95 d\\OMS/cmsy/m/n/10.95 j \\OML/cmm/m/it/10.95 >\n\n\nOverfull \\hbox (14.69397pt too wide) in paragraph at lines 392--393\n\\T1/ptm/m/n/10.95 pa-ram-e-ter-i-za-tion pro-vides both de-tec-tion power (27pp\n\n\nOverfull \\hbox (1.28035pt too wide) in paragraph at lines 392--393\n\\T1/ptm/m/n/10.95 train-ing that no other binary-only method achieves.\nRunaway argument?\n9(1):97--108. \n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.407 \n      \nRunaway argument?\n66(3):331--342. \n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.413 \n      \nRunaway argument?\n25(2):107--135. \n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.419 \n      \nRunaway argument?\nJiaying Lin, and Ying Cheng. \\newblock 2021. \\newblock A multiscale p\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.425 \n      \nRunaway argument?\n\\@nil {psnirt2026} Zefang Ren et al. \\newblock 2026. \\newblock PSN-IR\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.431 \n      \nRunaway argument?\nAnirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevin\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.437 \n      \nRunaway argument?\n\\@nil {shi2024codec} Weixuan Shi et al. \\newblock 2024. \\newblock CoD\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.443 \n      \nRunaway argument?\n\\@nil {dong2024timetravel} Yiwen Dong et al. \\newblock 2024. \\newblock \\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.449 \n      \nRunaway argument?\nMark Niklas Mueller, and Martin Vechev. \\newblock 2024. \\newblock Con\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.455 \n      \nRunaway argument?\n\\@nil {wang2025postrl} Yucheng Wang et al. \\newblock 2025. \\newblock \\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.461 \n      \nRunaway argument?\n\\@nil {jacovi2023} Alon Jacovi et al. \\newblock 2023. \\newblock Stop \\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.467 \n      \nRunaway argument?\nTianyu Gao, and Danqi Chen. \\newblock 2024. \\newblock Helmet: How to \\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.473 \n      \n\nPackage natbib Warning: There were undefined citations.\n\n[7] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm\ni8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbol\ns/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (7 pages, 244220 bytes).\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "e3ea0c01-8011-4146-b702-2a7c3b83f3ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-21T12:54:58.124Z_

<details><summary>Logged reasoning block</summary>

```text
The compilation has errors related to the natbib bibliography format. The `\bibitem` format I used is incompatible with natbib. I need to fix the bibliography entries to use the correct natbib format. Let me fix this.

The issue is that natbib expects a specific format for `\bibitem` entries. I need to use proper natbib-compatible format. Let me rewrite the bibliography section.

Actually, a simpler fix: I can either switch to a plain bibliography style without natbib, or fix the bibitem format to be compatible with natbib. The issue is that `\protect\citename` isn't recognized by natbib. Let me just use a simpler approach.


The runaway argument error is happening because natbib's `\bibitem` syntax requires the author and year in square brackets before the citation key. I need to reformat the bibliography entries to follow the standard natbib pattern.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f4a17e5-1f47-45f5-a46f-cdf186a5d18e",
  "isSidechain": false,
  "requestId": "req_011CbFkPJVNoyjpkj6FB5dNx",
  "type": "assistant",
  "uuid": "7211be00-008f-421b-b304-0ab754c7c02f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P54PqXetHVSYUTugVXYgp4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4587,
      "cache_read_input_tokens": 66951,
      "output_tokens": 2460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2460,
          "cache_read_input_tokens": 66951,
          "cache_creation_input_tokens": 4587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4587
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

_source line 33 · 2026-05-21T12:54:58.125Z_

Bibliography format issue with natbib. Let me fix the bibliography entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7211be00-008f-421b-b304-0ab754c7c02f",
  "isSidechain": false,
  "requestId": "req_011CbFkPJVNoyjpkj6FB5dNx",
  "type": "assistant",
  "uuid": "3d77b2da-2cb5-4588-9a11-888aba07c4af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P54PqXetHVSYUTugVXYgp4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4587,
      "cache_read_input_tokens": 66951,
      "output_tokens": 2460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2460,
          "cache_read_input_tokens": 66951,
          "cache_creation_input_tokens": 4587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4587
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

_source line 34 · 2026-05-21T12:55:24.339Z_

<details open><summary>🔧 Tool call — Edit · `toolu_019mu9h42Ko41SnQBG7opY7j`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper.tex",
  "old_string": "\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[\\protect\\citename{Drasgow}1985]{drasgow1985lz}\nFritz Drasgow.\n\\newblock 1985.\n\\newblock An evaluation of marginal maximum likelihood estimation for the two-parameter logistic model.\n\\newblock {\\em Applied Psychological Measurement}, 9(1):97--108.\n\n\\bibitem[\\protect\\citename{Snijders}2001]{snijders2001lzstar}\nTom A.B. Snijders.\n\\newblock 2001.\n\\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.\n\\newblock {\\em Psychometrika}, 66(3):331--342.\n\n\\bibitem[\\protect\\citename{Meijer and Sijtsma}2001]{meijer2001personfit}\nRob R. Meijer and Klaas Sijtsma.\n\\newblock 2001.\n\\newblock Methodology review: Evaluating person fit.\n\\newblock {\\em Applied Psychological Measurement}, 25(2):107--135.\n\n\\bibitem[\\protect\\citename{Hong et al.}2021]{hong2021lzm}\nHwanggyu Hong, Jiaying Lin, and Ying Cheng.\n\\newblock 2021.\n\\newblock A multiscale person-fit statistic for aberrant response detection.\n\\newblock {\\em British Journal of Mathematical and Statistical Psychology}, 74(3):547--569.\n\n\\bibitem[\\protect\\citename{Ren et al.}2026]{psnirt2026}\nZefang Ren et al.\n\\newblock 2026.\n\\newblock PSN-IRT: Psychometric standardized norms via neural item response theory for LLM evaluation.\n\\newblock In {\\em Proceedings of AAAI}.\n\n\\bibitem[\\protect\\citename{Shi et al.}2024a]{shi2024mink}\nWeijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.\n\\newblock 2024.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Shi et al.}2024b]{shi2024codec}\nWeixuan Shi et al.\n\\newblock 2024.\n\\newblock CoDeC: Contamination detection via in-context learning effects.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Dong et al.}2024]{dong2024timetravel}\nYiwen Dong et al.\n\\newblock 2024.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock In {\\em Proceedings of ICLR} (Spotlight).\n\n\\bibitem[\\protect\\citename{Dekoninck et al.}2024]{dekoninck2024constat}\nJasper Dekoninck, Mark Niklas Mueller, and Martin Vechev.\n\\newblock 2024.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citename{Wang et al.}2025]{wang2025postrl}\nYucheng Wang et al.\n\\newblock 2025.\n\\newblock Benchmark contamination under post-RL training: Failure of log-probability detection.\n\\newblock Preprint.\n\n\\bibitem[\\protect\\citename{Jacovi et al.}2023]{jacovi2023}\nAlon Jacovi et al.\n\\newblock 2023.\n\\newblock Stop uploading test data in plain text: Practical strategies for mitigating data contamination by evaluation benchmarks.\n\\newblock In {\\em Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citename{Yen et al.}2024]{irt_benchmark_design}\nHoward Yen, Tianyu Gao, and Danqi Chen.\n\\newblock 2024.\n\\newblock Helmet: How to evaluate long-context language models effectively and thoroughly.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\end{thebibliography}",
  "new_string": "\\begin{thebibliography}{20}\n\n\\bibitem[Drasgow(1985)]{drasgow1985lz}\nFritz Drasgow.\n1985.\nAn evaluation of marginal maximum likelihood estimation for the two-parameter logistic model.\n{\\em Applied Psychological Measurement}, 9(1):97--108.\n\n\\bibitem[Snijders(2001)]{snijders2001lzstar}\nTom A.B. Snijders.\n2001.\nAsymptotic null distribution of person fit statistics with estimated person parameter.\n{\\em Psychometrika}, 66(3):331--342.\n\n\\bibitem[Meijer and Sijtsma(2001)]{meijer2001personfit}\nRob R. Meijer and Klaas Sijtsma.\n2001.\nMethodology review: Evaluating person fit.\n{\\em Applied Psychological Measurement}, 25(2):107--135.\n\n\\bibitem[Hong et~al.(2021)]{hong2021lzm}\nHwanggyu Hong, Jiaying Lin, and Ying Cheng.\n2021.\nA multiscale person-fit statistic for aberrant response detection.\n{\\em British Journal of Mathematical and Statistical Psychology}, 74(3):547--569.\n\n\\bibitem[Ren et~al.(2026)]{psnirt2026}\nZefang Ren et~al.\n2026.\nPSN-IRT: Psychometric standardized norms via neural item response theory for LLM evaluation.\nIn {\\em Proceedings of AAAI}.\n\n\\bibitem[Shi et~al.(2024a)]{shi2024mink}\nWeijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.\n2024a.\nDetecting pretraining data from large language models.\nIn {\\em Proceedings of ICLR}.\n\n\\bibitem[Shi et~al.(2024b)]{shi2024codec}\nWeixuan Shi et~al.\n2024b.\nCoDeC: Contamination detection via in-context learning effects.\nIn {\\em Proceedings of ICLR}.\n\n\\bibitem[Dong et~al.(2024)]{dong2024timetravel}\nYiwen Dong et~al.\n2024.\nGeneralization or memorization: Data contamination and trustworthy evaluation for large language models.\nIn {\\em Proceedings of ICLR} (Spotlight).\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nJasper Dekoninck, Mark Niklas Mueller, and Martin Vechev.\n2024.\nConStat: Performance-based contamination detection in large language models.\nIn {\\em Proceedings of NeurIPS}.\n\n\\bibitem[Wang et~al.(2025)]{wang2025postrl}\nYucheng Wang et~al.\n2025.\nBenchmark contamination under post-RL training: Failure of log-probability detection.\nPreprint.\n\n\\bibitem[Jacovi et~al.(2023)]{jacovi2023}\nAlon Jacovi et~al.\n2023.\nStop uploading test data in plain text: Practical strategies for mitigating data contamination by evaluation benchmarks.\nIn {\\em Proceedings of EMNLP}.\n\n\\bibitem[Yen et~al.(2024)]{irt_benchmark_design}\nHoward Yen, Tianyu Gao, and Danqi Chen.\n2024.\nHelmet: How to evaluate long-context language models effectively and thoroughly.\nIn {\\em Proceedings of NeurIPS}.\n\n\\end{thebibliography}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d77b2da-2cb5-4588-9a11-888aba07c4af",
  "isSidechain": false,
  "requestId": "req_011CbFkPJVNoyjpkj6FB5dNx",
  "type": "assistant",
  "uuid": "0d9586dd-1919-426a-b935-012f419b191a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P54PqXetHVSYUTugVXYgp4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4587,
      "cache_read_input_tokens": 66951,
      "output_tokens": 2460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2460,
          "cache_read_input_tokens": 66951,
          "cache_creation_input_tokens": 4587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4587
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

_source line 35 · 2026-05-21T12:55:24.395Z_

<details><summary>↩ Tool result · `toolu_019mu9h42Ko41SnQBG7opY7j`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d9586dd-1919-426a-b935-012f419b191a",
  "isSidechain": false,
  "promptId": "27229c6a-13b2-488d-957e-cc76bf0056f3",
  "type": "user",
  "uuid": "36c3dd50-53c2-4d73-84fc-14d538113bbb",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper.tex",
    "oldString": "\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[\\protect\\citename{Drasgow}1985]{drasgow1985lz}\nFritz Drasgow.\n\\newblock 1985.\n\\newblock An evaluation of marginal maximum likelihood estimation for the two-parameter logistic model.\n\\newblock {\\em Applied Psychological Measurement}, 9(1):97--108.\n\n\\bibitem[\\protect\\citename{Snijders}2001]{snijders2001lzstar}\nTom A.B. Snijders.\n\\newblock 2001.\n\\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.\n\\newblock {\\em Psychometrika}, 66(3):331--342.\n\n\\bibitem[\\protect\\citename{Meijer and Sijtsma}2001]{meijer2001personfit}\nRob R. Meijer and Klaas Sijtsma.\n\\newblock 2001.\n\\newblock Methodology review: Evaluating person fit.\n\\newblock {\\em Applied Psychological Measurement}, 25(2):107--135.\n\n\\bibitem[\\protect\\citename{Hong et al.}2021]{hong2021lzm}\nHwanggyu Hong, Jiaying Lin, and Ying Cheng.\n\\newblock 2021.\n\\newblock A multiscale person-fit statistic for aberrant response detection.\n\\newblock {\\em British Journal of Mathematical and Statistical Psychology}, 74(3):547--569.\n\n\\bibitem[\\protect\\citename{Ren et al.}2026]{psnirt2026}\nZefang Ren et al.\n\\newblock 2026.\n\\newblock PSN-IRT: Psychometric standardized norms via neural item response theory for LLM evaluation.\n\\newblock In {\\em Proceedings of AAAI}.\n\n\\bibitem[\\protect\\citename{Shi et al.}2024a]{shi2024mink}\nWeijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.\n\\newblock 2024.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Shi et al.}2024b]{shi2024codec}\nWeixuan Shi et al.\n\\newblock 2024.\n\\newblock CoDeC: Contamination detection via in-context learning effects.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Dong et al.}2024]{dong2024timetravel}\nYiwen Dong et al.\n\\newblock 2024.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock In {\\em Proceedings of ICLR} (Spotlight).\n\n\\bibitem[\\protect\\citename{Dekoninck et al.}2024]{dekoninck2024constat}\nJasper Dekoninck, Mark Niklas Mueller, and Martin Vechev.\n\\newblock 2024.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citename{Wang et al.}2025]{wang2025postrl}\nYucheng Wang et al.\n\\newblock 2025.\n\\newblock Benchmark contamination under post-RL training: Failure of log-probability detection.\n\\newblock Preprint.\n\n\\bibitem[\\protect\\citename{Jacovi et al.}2023]{jacovi2023}\nAlon Jacovi et al.\n\\newblock 2023.\n\\newblock Stop uploading test data in plain text: Practical strategies for mitigating data contamination by evaluation benchmarks.\n\\newblock In {\\em Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citename{Yen et al.}2024]{irt_benchmark_design}\nHoward Yen, Tianyu Gao, and Danqi Chen.\n\\newblock 2024.\n\\newblock Helmet: How to evaluate long-context language models effectively and thoroughly.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\end{thebibliography}",
    "newString": "\\begin{thebibliography}{20}\n\n\\bibitem[Drasgow(1985)]{drasgow1985lz}\nFritz Drasgow.\n1985.\nAn evaluation of marginal maximum likelihood estimation for the two-parameter logistic model.\n{\\em Applied Psychological Measurement}, 9(1):97--108.\n\n\\bibitem[Snijders(2001)]{snijders2001lzstar}\nTom A.B. Snijders.\n2001.\nAsymptotic null distribution of person fit statistics with estimated person parameter.\n{\\em Psychometrika}, 66(3):331--342.\n\n\\bibitem[Meijer and Sijtsma(2001)]{meijer2001personfit}\nRob R. Meijer and Klaas Sijtsma.\n2001.\nMethodology review: Evaluating person fit.\n{\\em Applied Psychological Measurement}, 25(2):107--135.\n\n\\bibitem[Hong et~al.(2021)]{hong2021lzm}\nHwanggyu Hong, Jiaying Lin, and Ying Cheng.\n2021.\nA multiscale person-fit statistic for aberrant response detection.\n{\\em British Journal of Mathematical and Statistical Psychology}, 74(3):547--569.\n\n\\bibitem[Ren et~al.(2026)]{psnirt2026}\nZefang Ren et~al.\n2026.\nPSN-IRT: Psychometric standardized norms via neural item response theory for LLM evaluation.\nIn {\\em Proceedings of AAAI}.\n\n\\bibitem[Shi et~al.(2024a)]{shi2024mink}\nWeijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.\n2024a.\nDetecting pretraining data from large language models.\nIn {\\em Proceedings of ICLR}.\n\n\\bibitem[Shi et~al.(2024b)]{shi2024codec}\nWeixuan Shi et~al.\n2024b.\nCoDeC: Contamination detection via in-context learning effects.\nIn {\\em Proceedings of ICLR}.\n\n\\bibitem[Dong et~al.(2024)]{dong2024timetravel}\nYiwen Dong et~al.\n2024.\nGeneralization or memorization: Data contamination and trustworthy evaluation for large language models.\nIn {\\em Proceedings of ICLR} (Spotlight).\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nJasper Dekoninck, Mark Niklas Mueller, and Martin Vechev.\n2024.\nConStat: Performance-based contamination detection in large language models.\nIn {\\em Proceedings of NeurIPS}.\n\n\\bibitem[Wang et~al.(2025)]{wang2025postrl}\nYucheng Wang et~al.\n2025.\nBenchmark contamination under post-RL training: Failure of log-probability detection.\nPreprint.\n\n\\bibitem[Jacovi et~al.(2023)]{jacovi2023}\nAlon Jacovi et~al.\n2023.\nStop uploading test data in plain text: Practical strategies for mitigating data contamination by evaluation benchmarks.\nIn {\\em Proceedings of EMNLP}.\n\n\\bibitem[Yen et~al.(2024)]{irt_benchmark_design}\nHoward Yen, Tianyu Gao, and Danqi Chen.\n2024.\nHelmet: How to evaluate long-context language models effectively and thoroughly.\nIn {\\em Proceedings of NeurIPS}.\n\n\\end{thebibliography}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 395,
        "oldLines": 81,
        "newStart": 395,
        "newLines": 79,
        "lines": [
          " ",
          " [Omitted for review.]",
          " ",
          "-\\bibliographystyle{acl_natbib}",
          "-",
          " \\begin{thebibliography}{20}",
          " ",
          "-\\bibitem[\\protect\\citename{Drasgow}1985]{drasgow1985lz}",
          "+\\bibitem[Drasgow(1985)]{drasgow1985lz}",
          " Fritz Drasgow.",
          "-\\newblock 1985.",
          "-\\newblock An evaluation of marginal maximum likelihood estimation for the two-parameter logistic model.",
          "-\\newblock {\\em Applied Psychological Measurement}, 9(1):97--108.",
          "+1985.",
          "+An evaluation of marginal maximum likelihood estimation for the two-parameter logistic model.",
          "+{\\em Applied Psychological Measurement}, 9(1):97--108.",
          " ",
          "-\\bibitem[\\protect\\citename{Snijders}2001]{snijders2001lzstar}",
          "+\\bibitem[Snijders(2001)]{snijders2001lzstar}",
          " Tom A.B. Snijders.",
          "-\\newblock 2001.",
          "-\\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.",
          "-\\newblock {\\em Psychometrika}, 66(3):331--342.",
          "+2001.",
          "+Asymptotic null distribution of person fit statistics with estimated person parameter.",
          "+{\\em Psychometrika}, 66(3):331--342.",
          " ",
          "-\\bibitem[\\protect\\citename{Meijer and Sijtsma}2001]{meijer2001personfit}",
          "+\\bibitem[Meijer and Sijtsma(2001)]{meijer2001personfit}",
          " Rob R. Meijer and Klaas Sijtsma.",
          "-\\newblock 2001.",
          "-\\newblock Methodology review: Evaluating person fit.",
          "-\\newblock {\\em Applied Psychological Measurement}, 25(2):107--135.",
          "+2001.",
          "+Methodology review: Evaluating person fit.",
          "+{\\em Applied Psychological Measurement}, 25(2):107--135.",
          " ",
          "-\\bibitem[\\protect\\citename{Hong et al.}2021]{hong2021lzm}",
          "+\\bibitem[Hong et~al.(2021)]{hong2021lzm}",
          " Hwanggyu Hong, Jiaying Lin, and Ying Cheng.",
          "-\\newblock 2021.",
          "-\\newblock A multiscale person-fit statistic for aberrant response detection.",
          "-\\newblock {\\em British Journal of Mathematical and Statistical Psychology}, 74(3):547--569.",
          "+2021.",
          "+A multiscale person-fit statistic for aberrant response detection.",
          "+{\\em British Journal of Mathematical and Statistical Psychology}, 74(3):547--569.",
          " ",
          "-\\bibitem[\\protect\\citename{Ren et al.}2026]{psnirt2026}",
          "-Zefang Ren et al.",
          "-\\newblock 2026.",
          "-\\newblock PSN-IRT: Psychometric standardized norms via neural item response theory for LLM evaluation.",
          "-\\newblock In {\\em Proceedings of AAAI}.",
          "+\\bibitem[Ren et~al.(2026)]{psnirt2026}",
          "+Zefang Ren et~al.",
          "+2026.",
          "+PSN-IRT: Psychometric standardized norms via neural item response theory for LLM evaluation.",
          "+In {\\em Proceedings of AAAI}.",
          " ",
          "-\\bibitem[\\protect\\citename{Shi et al.}2024a]{shi2024mink}",
          "+\\bibitem[Shi et~al.(2024a)]{shi2024mink}",
          " Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.",
          "-\\newblock 2024.",
          "-\\newblock Detecting pretraining data from large language models.",
          "-\\newblock In {\\em Proceedings of ICLR}.",
          "+2024a.",
          "+Detecting pretraining data from large language models.",
          "+In {\\em Proceedings of ICLR}.",
          " ",
          "-\\bibitem[\\protect\\citename{Shi et al.}2024b]{shi2024codec}",
          "-Weixuan Shi et al.",
          "-\\newblock 2024.",
          "-\\newblock CoDeC: Contamination detection via in-context learning effects.",
          "-\\newblock In {\\em Proceedings of ICLR}.",
          "+\\bibitem[Shi et~al.(2024b)]{shi2024codec}",
          "+Weixuan Shi et~al.",
          "+2024b.",
          "+CoDeC: Contamination detection via in-context learning effects.",
          "+In {\\em Proceedings of ICLR}.",
          " ",
          "-\\bibitem[\\protect\\citename{Dong et al.}2024]{dong2024timetravel}",
          "-Yiwen Dong et al.",
          "-\\newblock 2024.",
          "-\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.",
          "-\\newblock In {\\em Proceedings of ICLR} (Spotlight).",
          "+\\bibitem[Dong et~al.(2024)]{dong2024timetravel}",
          "+Yiwen Dong et~al.",
          "+2024.",
          "+Generalization or memorization: Data contamination and trustworthy evaluation for large language models.",
          "+In {\\em Proceedings of ICLR} (Spotlight).",
          " ",
          "-\\bibitem[\\protect\\citename{Dekoninck et al.}2024]{dekoninck2024constat}",
          "+\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}",
          " Jasper Dekoninck, Mark Niklas Mueller, and Martin Vechev.",
          "-\\newblock 2024.",
          "-\\newblock ConStat: Performance-based contamination detection in large language models.",
          "-\\newblock In {\\em Proceedings of NeurIPS}.",
          "+2024.",
          "+ConStat: Performance-based contamination detection in large language models.",
          "+In {\\em Proceedings of NeurIPS}.",
          " ",
          "-\\bibitem[\\protect\\citename{Wang et al.}2025]{wang2025postrl}",
          "-Yucheng Wang et al.",
          "-\\newblock 2025.",
          "-\\newblock Benchmark contamination under post-RL training: Failure of log-probability detection.",
          "-\\newblock Preprint.",
          "+\\bibitem[Wang et~al.(2025)]{wang2025postrl}",
          "+Yucheng Wang et~al.",
          "+2025.",
          "+Benchmark contamination under post-RL training: Failure of log-probability detection.",
          "+Preprint.",
          " ",
          "-\\bibitem[\\protect\\citename{Jacovi et al.}2023]{jacovi2023}",
          "-Alon Jacovi et al.",
          "-\\newblock 2023.",
          "-\\newblock Stop uploading test data in plain text: Practical strategies for mitigating data contamination by evaluation benchmarks.",
          "-\\newblock In {\\em Proceedings of EMNLP}.",
          "+\\bibitem[Jacovi et~al.(2023)]{jacovi2023}",
          "+Alon Jacovi et~al.",
          "+2023.",
          "+Stop uploading test data in plain text: Practical strategies for mitigating data contamination by evaluation benchmarks.",
          "+In {\\em Proceedings of EMNLP}.",
          " ",
          "-\\bibitem[\\protect\\citename{Yen et al.}2024]{irt_benchmark_design}",
          "+\\bibitem[Yen et~al.(2024)]{irt_benchmark_design}",
          " Howard Yen, Tianyu Gao, and Danqi Chen.",
          "-\\newblock 2024.",
          "-\\newblock Helmet: How to evaluate long-context language models effectively and thoroughly.",
          "-\\newblock In {\\em Proceedings of NeurIPS}.",
          "+2024.",
          "+Helmet: How to evaluate long-context language models effectively and thoroughly.",
          "+In {\\em Proceedings of NeurIPS}.",
          " ",
          " \\end{thebibliography}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "0d9586dd-1919-426a-b935-012f419b191a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-21T12:55:24.406Z_

```json
{
  "parentUuid": "36c3dd50-53c2-4d73-84fc-14d538113bbb",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9b3356f6-fe4a-431d-8b10-103d745c9ef3",
  "timestamp": "2026-05-21T12:55:24.406Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122444 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "9b3356f6-fe4a-431d-8b10-103d745c9ef3",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit robustness under RL distributional shift",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85"
}
```

---

### Tool call

_source line 39 · 2026-05-21T12:55:28.238Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017UsGEQ7jX29yk5up6SY8Tr`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b3356f6-fe4a-431d-8b10-103d745c9ef3",
  "isSidechain": false,
  "requestId": "req_011CbFkRs1HVrDfZD3uyf7KJ",
  "type": "assistant",
  "uuid": "bb75c8e2-47e2-4fc9-a37d-297809dda662",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdYBrsw4ij69up4eHoVMfp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2654,
      "cache_read_input_tokens": 71538,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 71538,
          "cache_creation_input_tokens": 2654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2654
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

_source line 40 · 2026-05-21T12:55:29.644Z_

<details><summary>↩ Tool result · `toolu_017UsGEQ7jX29yk5up6SY8Tr`</summary>

```text
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm
i8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbol
s/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 251766 bytes).
Transcript written on paper.log.
/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbol
s/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 253591 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb75c8e2-47e2-4fc9-a37d-297809dda662",
  "isSidechain": false,
  "promptId": "27229c6a-13b2-488d-957e-cc76bf0056f3",
  "type": "user",
  "uuid": "3e561e38-3b35-4839-a862-58e9d01992a2",
  "toolUseResult": {
    "stdout": "nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm\ni8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbol\ns/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 251766 bytes).\nTranscript written on paper.log.\n/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbol\ns/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 253591 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "bb75c8e2-47e2-4fc9-a37d-297809dda662",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T12:55:40.158Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DN1TBVQnn1A8fduSwLfuUe`</summary>

```json
{
  "command": "grep -c \"^!\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper.log 2>/dev/null; grep \"^!\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper.log 2>/dev/null | head -5; echo \"---\"; grep \"Warning.*undefined\\|Warning.*Citation\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper.log 2>/dev/null",
  "description": "Check for LaTeX errors and warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e561e38-3b35-4839-a862-58e9d01992a2",
  "isSidechain": false,
  "requestId": "req_011CbFkSFYcENcJw3vfk5Zi5",
  "type": "assistant",
  "uuid": "5a6eca25-4c9a-4066-a262-c3c4170139cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LusZgxfgYc5tHjWrA5LrNx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1276,
      "cache_read_input_tokens": 74192,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1276,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 282,
          "cache_read_input_tokens": 74192,
          "cache_creation_input_tokens": 1276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1276
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

_source line 42 · 2026-05-21T12:55:40.235Z_

<details><summary>↩ Tool result · `toolu_01DN1TBVQnn1A8fduSwLfuUe`</summary>

```text
0
---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a6eca25-4c9a-4066-a262-c3c4170139cf",
  "isSidechain": false,
  "promptId": "27229c6a-13b2-488d-957e-cc76bf0056f3",
  "type": "user",
  "uuid": "f8654285-4645-48b1-a644-79d6f33f367a",
  "toolUseResult": {
    "stdout": "0\n---",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5a6eca25-4c9a-4066-a262-c3c4170139cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-21T12:55:52.516Z_

编译成功，无错误、无未定义引用。PDF 已生成：8 页，253KB。

**产出文件**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best/paper.tex` → `paper.pdf`

**覆盖的实验**（对应 experiment_data.json 中全部 10 个实验 + 1 个 ABANDONED）：

| 实验 | 论文位置 |
|------|---------|
| Controlled Contamination Pilot | §4.2 Table 1, §4.3 |
| Full Controlled Contamination (4 families) | §4.2 Table 1, §5.4 Table 6 |
| 4PL vs 3PL Ablation | §4.4 Table 2 |
| Full Baseline Comparison | §5.1 Table 3 |
| Post-RL Hypothesis Test | §5.2 Table 4 |
| Extra Benchmarks (BBH + MATH) | §5.3 Table 5 |
| Cross-Benchmark Detection | §5.4 Table 6 |
| MMLU Domain-Level Analysis | §6.2 Table 7 |
| Multiscale lzm | §6.3 Table 8 |
| IRT Refit Expanded (N=178) | §6.4 Table 9 |
| Base→Chat Natural Experiment | §6.5 Table 10 |
| Leaderboard Audit (ABANDONED) | §7 Discussion (data availability) |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8654285-4645-48b1-a644-79d6f33f367a",
  "isSidechain": false,
  "requestId": "req_011CbFkT3YpVBdUgiFaW8iRF",
  "type": "assistant",
  "uuid": "854cdbaa-724a-4a00-be2c-f94c412cd940",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T122444/best",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUj1eLvhKfupoE7426zP27",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 297,
      "cache_read_input_tokens": 75468,
      "output_tokens": 428,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 428,
          "cache_read_input_tokens": 75468,
          "cache_creation_input_tokens": 297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 297
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122444 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "854cdbaa-724a-4a00-be2c-f94c412cd940",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit robustness under RL distributional shift",
  "sessionId": "bcce2c14-36f3-4c61-97b4-2a74556b3e85"
}
```

---
