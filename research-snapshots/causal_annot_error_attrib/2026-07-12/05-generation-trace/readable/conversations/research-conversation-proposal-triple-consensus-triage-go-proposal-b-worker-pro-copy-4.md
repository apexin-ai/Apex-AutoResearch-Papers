# Research conversation: 【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。 【原始 pro

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 99
- **Recorded user turns:** 6
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-1/196740b4-7d71-40e0-b9b9-901bbed4cf87.jsonl`
- **Structured JSON:** [`94c379cd9519544b40d2.json`](../../sessions/94/94c379cd9519544b40d2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:12:12.524Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:12:12.524Z",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "content": "【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。\n\n【原始 proposal】:\n# Uncertainty-Gated Credit Assignment for Process-Supervised Mathematical Reasoning RL\n\n## Core Problem\n\nCurrent methods for integrating process reward models into RL training (PURE, GRPO-λ, PRL, PRPO) treat all PRM step-level scores as equally trustworthy, yet PRMs are demonstrably miscalibrated—overestimating success probabilities on uncertain steps—leading to reward hacking where the policy exploits unreliable PRM signals rather than genuinely improving reasoning.\n\n## Research Opportunity\n\nPRM calibration methods have matured rapidly (quantile regression [NeurIPS 2025], conditional optimal transport [arXiv 2605.06785]) but are applied exclusively to test-time scaling (best-of-N, instance-adaptive search). No work uses PRM uncertainty to modulate credit assignment during RL training. Meanwhile, Jia et al. [ICML 2025] proved outcome supervision is statistically no harder than process supervision—suggesting the empirical gap is algorithmic, motivating a principled interpolation. The building blocks (calibrated PRMs, GRPO/PURE training pipelines, math reasoning benchmarks) all exist, making a 2-month implementation feasible for AAAI 2027 (deadline: July 28, 2026).\n\n## Research Landscape\n\nPURE (NeurIPS 2025) replaces summation-form with min-form credit assignment, achieving 82.6% on MATH-500 and 82.5% on AMC23 with Qwen2.5-Math-7B but still assumes PRM scores are reliable. GRPO-λ (arXiv Oct 2025) adds eligibility traces to GRPO, improving average math scores by 3–4.5 points on 7B models but also trusts PRM outputs uniformly. PROGRS (arXiv Apr 2026) uses outcome-conditioned centering with a frozen quantile-regression PRM (74.9% on MATH-500 vs 69.7% DAPO baseline) but applies a fixed centering rule at the trajectory level, not per-step uncertainty gating. UCAS (arXiv Oct 2025) modulates advantages via the policy model's own logit uncertainty—fundamentally different from PRM verifier uncertainty. The Distributional PRM (arXiv May 2026) achieves state-of-the-art calibration via conditional optimal transport but explicitly targets only test-time scaling. PathFinder-PRM (arXiv May 2025) achieves 67.7 PRMScore on PRMBench with error-type-aware scoring but does not feed uncertainty into RL credit assignment. PRPO (arXiv Jan 2026) aligns process and outcome advantages via location-parameter shift on Qwen2.5-Math-1.5B (61.2→64.4% MATH-500) but uses fixed structural alignment, not adaptive per-step weighting. Uncertainty-Aware Reward Discounting (arXiv Apr 2026) uses ensemble disagreement to mitigate reward hacking in RLHF but targets general preference learning, not process-outcome interpolation for math. TP-GRPO (arXiv Jul 2025) introduces capability-adaptive rewards with generative PRM at the thought level using intrinsic signals, not PRM calibration. PRIME (arXiv Feb 2025) enables online PRM updates through implicit process rewards but uses uniform trust in PRM signals. Thorough concurrent-work search across arXiv and OpenReview (May 2026) confirms the specific gap—using PRM calibration confidence to drive per-step adaptive interpolation between process and outcome credit during RL training—remains unaddressed.\n\n## Proposed Approach\n\nWe propose Uncertainty-Gated Credit Assignment (UGCA), which equips the off-the-shelf Qwen2.5-Math-PRM-7B with calibrated confidence intervals via quantile regression (adapting the open-source code from Park et al., NeurIPS 2025), then defines a per-step gating coefficient α_i = σ(−(w_i − τ)/β) based on each step's confidence-interval width w_i. During RL training, the advantage at step i is computed as A_i = α_i · A^min_i + (1 − α_i) · A^GRPO_i, where A^min is PURE-style min-form process advantage and A^GRPO is group-relative outcome advantage—high-confidence PRM steps lean on process credit while uncertain steps gracefully degrade to outcome credit. We train Qwen3-8B and Qwen3-1.7B on the MATH training set (8K prompts) using this modified GRPO objective atop the PURE codebase, with the calibrated PRM frozen throughout, evaluating on MATH-500, AMC23, AIME24, and OlympiadBench against re-implemented PURE, GRPO, and GRPO-λ baselines on the same models. The method is theoretically grounded by the Jia et al. (ICML 2025) proof that outcome supervision is statistically no harder than process supervision, making the degradation principled, and requires only a one-time quantile calibration pass with no additional training signals.\n\n## Detailed Description\n\nWe introduce Uncertainty-Gated Credit Assignment (UGCA), a method that uses calibrated PRM confidence to adaptively interpolate between process-level and outcome-level credit during RL training for mathematical reasoning. While PRM calibration methods (quantile regression, conditional optimal transport) have matured rapidly, they target only inference-time scaling. Meanwhile, RL credit assignment methods (PURE, GRPO-λ, PRPO) treat all PRM step scores as equally reliable, enabling reward hacking on uncertain steps. UGCA bridges this gap: we equip the off-the-shelf Qwen2.5-Math-PRM-7B with quantile-regression confidence intervals and derive a per-step gating coefficient—high-confidence steps use PURE-style min-form process advantages; low-confidence steps gracefully degrade to GRPO outcome advantages. This interpolation is theoretically motivated by the Jia et al. (ICML 2025) proof that outcome supervision is statistically equivalent to process supervision. We evaluate on Qwen3-8B and Qwen3-1.7B across MATH-500, AMC23, AIME24, and OlympiadBench, targeting improvements over PURE and GRPO-λ baselines while demonstrating measurably reduced reward hacking on PRM-uncertain steps. All core building blocks (calibrated PRM code, PURE codebase, pre-trained PRMs) are publicly available, and concurrent-work search (May 2026) confirms this mechanism is novel.\n\n## Key References\n\n- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (NeurIPS 2025)\n- GRPO-λ: Credit Assignment Improves LLM Reasoning (arXiv 2025)\n- LLM Reasoning with Process Rewards for Outcome-Guided Steps (arXiv 2026)\n- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (NeurIPS 2025)\n- Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport (arXiv 2026)\n- Do We Need to Verify Step by Step? Rethinking Process Supervision from a Theoretical Perspective (ICML 2025)\n- Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning (arXiv 2025)\n- PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization (arXiv 2026)\n- PRL: Process Reward Learning Improves LLMs' Reasoning Ability and Broadens the Reasoning Boundary (arXiv 2026)\n- Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision (arXiv 2025)\n- Process Reinforcement through Implicit Rewards (arXiv 2025)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: ~1800 H100-hours (PRM quantile calibration on Qwen2.5-Math-PRM-7B: 100h; Qwen3-1.7B RL ablations ×6 configs: 360h; Qwen3-8B RL ablations ×6 configs: 1200h; final evaluation + reward-hacking diagnostics: 140h), timeline: 8 weeks (wk1–2: PRM quantile-regression calibration + PURE codebase integration with veRL; wk3–4: 1.7B ablations over gating threshold τ, temperature β, and quantile level; wk5–6: 8B full comparison runs vs PURE/GRPO/GRPO-λ baselines; wk7: reward-hacking analysis, per-step uncertainty visualization, ablation plots; wk8: paper writing and AAAI submission), estimated_gpu_cost: $4,500 (H100 spot at ~$2.50/GPU-hr)\n- **human_in_loop**: gpu_hours: ~1800 H100-hours (identical compute workload), timeline: 6 weeks (Claude accelerates PURE/veRL codebase integration, quantile-regression head implementation, hyperparameter sweep scripting, results analysis, and paper drafting), claude_api_cost: $300, estimated_gpu_cost: $4,500\n- **auto_research**: gpu_hours: ~1800 H100-hours (identical compute workload), timeline: 5 weeks, claude_api_cost: $800, estimated_gpu_cost: $4,500, speed_bottleneck: GPU training wall-clock: each Qwen3-8B RL run requires ~25h on 8×H100; 6 ablation configs run sequentially unless multi-node cluster available\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T08:12:12.528Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:12:12.528Z",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-27T08:12:12.543Z_

【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。

【原始 proposal】:
# Uncertainty-Gated Credit Assignment for Process-Supervised Mathematical Reasoning RL

## Core Problem

Current methods for integrating process reward models into RL training (PURE, GRPO-λ, PRL, PRPO) treat all PRM step-level scores as equally trustworthy, yet PRMs are demonstrably miscalibrated—overestimating success probabilities on uncertain steps—leading to reward hacking where the policy exploits unreliable PRM signals rather than genuinely improving reasoning.

## Research Opportunity

PRM calibration methods have matured rapidly (quantile regression [NeurIPS 2025], conditional optimal transport [arXiv 2605.06785]) but are applied exclusively to test-time scaling (best-of-N, instance-adaptive search). No work uses PRM uncertainty to modulate credit assignment during RL training. Meanwhile, Jia et al. [ICML 2025] proved outcome supervision is statistically no harder than process supervision—suggesting the empirical gap is algorithmic, motivating a principled interpolation. The building blocks (calibrated PRMs, GRPO/PURE training pipelines, math reasoning benchmarks) all exist, making a 2-month implementation feasible for AAAI 2027 (deadline: July 28, 2026).

## Research Landscape

PURE (NeurIPS 2025) replaces summation-form with min-form credit assignment, achieving 82.6% on MATH-500 and 82.5% on AMC23 with Qwen2.5-Math-7B but still assumes PRM scores are reliable. GRPO-λ (arXiv Oct 2025) adds eligibility traces to GRPO, improving average math scores by 3–4.5 points on 7B models but also trusts PRM outputs uniformly. PROGRS (arXiv Apr 2026) uses outcome-conditioned centering with a frozen quantile-regression PRM (74.9% on MATH-500 vs 69.7% DAPO baseline) but applies a fixed centering rule at the trajectory level, not per-step uncertainty gating. UCAS (arXiv Oct 2025) modulates advantages via the policy model's own logit uncertainty—fundamentally different from PRM verifier uncertainty. The Distributional PRM (arXiv May 2026) achieves state-of-the-art calibration via conditional optimal transport but explicitly targets only test-time scaling. PathFinder-PRM (arXiv May 2025) achieves 67.7 PRMScore on PRMBench with error-type-aware scoring but does not feed uncertainty into RL credit assignment. PRPO (arXiv Jan 2026) aligns process and outcome advantages via location-parameter shift on Qwen2.5-Math-1.5B (61.2→64.4% MATH-500) but uses fixed structural alignment, not adaptive per-step weighting. Uncertainty-Aware Reward Discounting (arXiv Apr 2026) uses ensemble disagreement to mitigate reward hacking in RLHF but targets general preference learning, not process-outcome interpolation for math. TP-GRPO (arXiv Jul 2025) introduces capability-adaptive rewards with generative PRM at the thought level using intrinsic signals, not PRM calibration. PRIME (arXiv Feb 2025) enables online PRM updates through implicit process rewards but uses uniform trust in PRM signals. Thorough concurrent-work search across arXiv and OpenReview (May 2026) confirms the specific gap—using PRM calibration confidence to drive per-step adaptive interpolation between process and outcome credit during RL training—remains unaddressed.

## Proposed Approach

We propose Uncertainty-Gated Credit Assignment (UGCA), which equips the off-the-shelf Qwen2.5-Math-PRM-7B with calibrated confidence intervals via quantile regression (adapting the open-source code from Park et al., NeurIPS 2025), then defines a per-step gating coefficient α_i = σ(−(w_i − τ)/β) based on each step's confidence-interval width w_i. During RL training, the advantage at step i is computed as A_i = α_i · A^min_i + (1 − α_i) · A^GRPO_i, where A^min is PURE-style min-form process advantage and A^GRPO is group-relative outcome advantage—high-confidence PRM steps lean on process credit while uncertain steps gracefully degrade to outcome credit. We train Qwen3-8B and Qwen3-1.7B on the MATH training set (8K prompts) using this modified GRPO objective atop the PURE codebase, with the calibrated PRM frozen throughout, evaluating on MATH-500, AMC23, AIME24, and OlympiadBench against re-implemented PURE, GRPO, and GRPO-λ baselines on the same models. The method is theoretically grounded by the Jia et al. (ICML 2025) proof that outcome supervision is statistically no harder than process supervision, making the degradation principled, and requires only a one-time quantile calibration pass with no additional training signals.

## Detailed Description

We introduce Uncertainty-Gated Credit Assignment (UGCA), a method that uses calibrated PRM confidence to adaptively interpolate between process-level and outcome-level credit during RL training for mathematical reasoning. While PRM calibration methods (quantile regression, conditional optimal transport) have matured rapidly, they target only inference-time scaling. Meanwhile, RL credit assignment methods (PURE, GRPO-λ, PRPO) treat all PRM step scores as equally reliable, enabling reward hacking on uncertain steps. UGCA bridges this gap: we equip the off-the-shelf Qwen2.5-Math-PRM-7B with quantile-regression confidence intervals and derive a per-step gating coefficient—high-confidence steps use PURE-style min-form process advantages; low-confidence steps gracefully degrade to GRPO outcome advantages. This interpolation is theoretically motivated by the Jia et al. (ICML 2025) proof that outcome supervision is statistically equivalent to process supervision. We evaluate on Qwen3-8B and Qwen3-1.7B across MATH-500, AMC23, AIME24, and OlympiadBench, targeting improvements over PURE and GRPO-λ baselines while demonstrating measurably reduced reward hacking on PRM-uncertain steps. All core building blocks (calibrated PRM code, PURE codebase, pre-trained PRMs) are publicly available, and concurrent-work search (May 2026) confirms this mechanism is novel.

## Key References

- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (NeurIPS 2025)
- GRPO-λ: Credit Assignment Improves LLM Reasoning (arXiv 2025)
- LLM Reasoning with Process Rewards for Outcome-Guided Steps (arXiv 2026)
- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (NeurIPS 2025)
- Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport (arXiv 2026)
- Do We Need to Verify Step by Step? Rethinking Process Supervision from a Theoretical Perspective (ICML 2025)
- Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning (arXiv 2025)
- PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization (arXiv 2026)
- PRL: Process Reward Learning Improves LLMs' Reasoning Ability and Broadens the Reasoning Boundary (arXiv 2026)
- Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision (arXiv 2025)
- Process Reinforcement through Implicit Rewards (arXiv 2025)

## Resource Estimate

- **manual**: gpu_hours: ~1800 H100-hours (PRM quantile calibration on Qwen2.5-Math-PRM-7B: 100h; Qwen3-1.7B RL ablations ×6 configs: 360h; Qwen3-8B RL ablations ×6 configs: 1200h; final evaluation + reward-hacking diagnostics: 140h), timeline: 8 weeks (wk1–2: PRM quantile-regression calibration + PURE codebase integration with veRL; wk3–4: 1.7B ablations over gating threshold τ, temperature β, and quantile level; wk5–6: 8B full comparison runs vs PURE/GRPO/GRPO-λ baselines; wk7: reward-hacking analysis, per-step uncertainty visualization, ablation plots; wk8: paper writing and AAAI submission), estimated_gpu_cost: $4,500 (H100 spot at ~$2.50/GPU-hr)
- **human_in_loop**: gpu_hours: ~1800 H100-hours (identical compute workload), timeline: 6 weeks (Claude accelerates PURE/veRL codebase integration, quantile-regression head implementation, hyperparameter sweep scripting, results analysis, and paper drafting), claude_api_cost: $300, estimated_gpu_cost: $4,500
- **auto_research**: gpu_hours: ~1800 H100-hours (identical compute workload), timeline: 5 weeks, claude_api_cost: $800, estimated_gpu_cost: $4,500, speed_bottleneck: GPU training wall-clock: each Qwen3-8B RL run requires ~25h on 8×H100; 6 ablation configs run sequentially unless multi-node cluster available


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "54d6e497-6212-4c88-a3fc-cbd4f3b0bc49",
  "type": "user",
  "uuid": "b47fd31a-56ec-4677-ba8b-27e22edf4370",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:12:12.542Z_

```json
{
  "parentUuid": "b47fd31a-56ec-4677-ba8b-27e22edf4370",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "6f8d0ad1-5787-4b79-b65d-dbad9a488643",
  "timestamp": "2026-05-27T08:12:12.542Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:12:12.542Z_

```json
{
  "parentUuid": "6f8d0ad1-5787-4b79-b65d-dbad9a488643",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a2e8310e-352f-4392-a4b4-215db5483da6",
  "timestamp": "2026-05-27T08:12:12.542Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Assistant

_source line 7 · 2026-05-27T08:12:23.151Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "终审 agent" (Final Review Agent) in Role A' (Meta Judge) mode. However, looking at the message more carefully, they're saying this proposal has already passed the triple-consensus triage and is confirmed GO. They want me to remember this proposal and be ready for Role B (iterative rounds).

Let me re-read: "以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。"


So they're confirming the proposal passed triage and I need to internalize the full content of the UGCA proposal—which focuses on using calibrated PRM confidence intervals to adaptively interpolate between process-level and outcome-level credit assignment in mathematical reasoning RL—then stand ready to integrate worker outputs as Role B in subsequent iterations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2e8310e-352f-4392-a4b4-215db5483da6",
  "isSidechain": false,
  "requestId": "req_011CbSjgpWowLXJ1b2PGRKoV",
  "type": "assistant",
  "uuid": "d70f1ae4-3a4b-41db-9bd5-458721e3a947",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011VFsEgiPSv2YBwXPDXd51m",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 3806,
      "cache_read_input_tokens": 16543,
      "output_tokens": 893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3806,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 893,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 3806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3806
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

_source line 8 · 2026-05-27T08:12:29.539Z_

收到。我已完整记录原始 proposal 的所有内容，包括：

**核心 idea**：Uncertainty-Gated Credit Assignment (UGCA) — 用量化回归校准 PRM 的置信区间，基于每步置信区间宽度 w_i 生成门控系数 α_i，在 RL 训练中自适应插值 PURE-style min-form process advantage 和 GRPO outcome advantage。高置信步骤依赖过程信用，低置信步骤退化到结果信用。

**关键引用**：PURE (NeurIPS 2025)、GRPO-λ (arXiv 2025)、PROGRS (arXiv Apr 2026)、UCAS (arXiv Oct 2025)、Distributional PRM (arXiv May 2026, arXiv:2605.06785)、PathFinder-PRM (arXiv May 2025)、PRPO (arXiv Jan 2026)、Uncertainty-Aware Reward Discounting (arXiv Apr 2026)、TP-GRPO (arXiv Jul 2025)、PRIME (arXiv Feb 2025)、Park et al. quantile regression (NeurIPS 2025)、Jia et al. (ICML 2025) 等全部 11 篇 Key References。

**实验设计**：Qwen3-8B + Qwen3-1.7B，MATH 训练集 8K prompts，评估 MATH-500/AMC23/AIME24/OlympiadBench，对比 PURE/GRPO/GRPO-λ baselines，~1800 H100-hours，8 周周期。

**Triage 状态**：已通过 triple-consensus，确认 GO。

我已就绪，等待接收第一轮「发掘 agent」和「补救 agent」的输出，届时将以**角色 B：迭代中**执行整合、交叉验证、proposal 更新和收敛判断。请发送 worker 输出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d70f1ae4-3a4b-41db-9bd5-458721e3a947",
  "isSidechain": false,
  "requestId": "req_011CbSjgpWowLXJ1b2PGRKoV",
  "type": "assistant",
  "uuid": "e58d6904-83f3-4f7e-883b-cd1f1ee15f43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011VFsEgiPSv2YBwXPDXd51m",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 3806,
      "cache_read_input_tokens": 16543,
      "output_tokens": 893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3806,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 893,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 3806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3806
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

_source line 9_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。  【原始 proposal】: # Uncertainty-Gated Credit Assignment for Process-Supervised Mathematic…",
  "leafUuid": "e58d6904-83f3-4f7e-883b-cd1f1ee15f43",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 12 · 2026-05-27T08:17:34.341Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:17:34.341Z",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "content": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nNow I have enough research context. Let me synthesize my findings and produce the assessment.\n\n---\n\n【状态】: 有发掘空间\n\n【前置调研发现】\n\n- **Distributional PRM (arXiv 2605.06785, May 2026)**: 提出 conditional optimal transport 校准 PRM，显著优于 quantile regression，但明确只用于 test-time scaling（best-of-N），未涉及 RL 训练时的 credit assignment。与本 proposal 的关系：本文选择 quantile regression 作为校准方法，但这篇更新的工作表明 conditional OT 在 calibration 质量上更优，可能影响方法选择。\n- **PROGRS (arXiv 2604.02341, Apr 2026)**: 使用 frozen quantile-regression PRM + outcome-conditioned centering，在 trajectory 级别做固定 centering rule，而非 per-step adaptive gating。与本 proposal 最接近的竞争者——同样使用了 calibrated PRM 进入 RL 训练，但机制不同（固定 centering vs. per-step uncertainty-gated interpolation）。\n- **\"Discovering Process-Outcome Credit in Multi-Step LLM Reasoning\" (arXiv 2602.01034, Feb 2026)**: 提出 Step-wise Marginal Information Gain + Decoupled Masking，在 process-outcome credit 分配上做了 decoupling，是另一种 process-outcome 混合 credit 的思路，但不基于 PRM uncertainty。\n- **VPPO / \"Save the Good Prefix\" (arXiv 2601.18984, Jan 2026)**: 用 PRM 定位第一个错误步骤，将轨迹分为 correct prefix + erroneous suffix，做 targeted penalization。与本 proposal 互补但不重叠——它用 PRM 做 binary 分割而非连续 uncertainty gating。\n- **\"GRPO is Secretly a Process Reward Model\" (arXiv 2509.21154, Sep 2025, ICLR 2026)**: 证明 GRPO + ORM 在 identical-prefix 条件下等价于 PRM-aware RL，暗示 GRPO 本身已隐式包含 process credit。这对本 proposal 既是支持（说明 process-outcome interpolation 有理论基础）也是挑战（GRPO 可能已经 partially 在做这件事）。\n- **Uncertainty-Aware Reward Discounting (arXiv 2604.26360, Apr 2026)**: 用 ensemble disagreement 做 uncertainty-aware reward modulation 来缓解 reward hacking，但针对 general RLHF，非 math reasoning 的 process-outcome interpolation。\n- **Jia et al. (ICML 2025)**: 证明 outcome supervision 在统计意义上不比 process supervision 更难，差异在于算法层面（梯度动态等），为 \"uncertain 时退化到 outcome credit\" 提供了理论支撑。\n- **PRIME (arXiv 2502.01456, Feb 2025)**: 通过 implicit process rewards 实现 online PRM 更新，缓解 distribution shift，但均匀信任 PRM 信号。\n\n- **调研总结**: 当前领域研究者主要在两个方向突破：(1) 如何让 PRM 信号更可靠（calibration, distributional PRM, generative PRM）；(2) 如何在 RL 训练中更好地混合 process 和 outcome credit（PROGRS, PRPO, Discovering Process-Outcome Credit, VPPO）。但这两个方向目前是**分离**的——calibration 工作只服务于 test-time，credit assignment 工作不考虑 PRM 信号的可靠性差异。本 proposal 正好处于这两个方向的**交汇点**。\n\n---\n\n【发掘点 1】\n- 维度: 前提假设质疑 / trivial alternative 威胁\n- 内容: Proposal 的核心前提是\"PRM 在 uncertain steps 上的 miscalibration 导致 reward hacking\"，但需要更严格地论证**为什么 per-step uncertainty gating 优于更简单的 alternatives**。具体地，存在至少两个 trivial alternatives 需要正面回应：\n  - **Alternative 1: 全局 clipping/truncation**。如果 PRM miscalibration 是主要问题，直接 clip 掉 confidence 低于阈值的 PRM 分数（将其置零或 fallback 到 outcome reward），不需要 sigmoid gating 的连续插值，也不需要额外的 β 温度参数。这个 simpler baseline 是否已经足够？\n  - **Alternative 2: PROGRS 的 outcome-conditioned centering**。PROGRS 已经在用 calibrated PRM（同样是 quantile regression）做 RL training credit assignment，虽然机制不同（trajectory-level centering vs. per-step gating），但它可能已经 implicitly 解决了 miscalibration 问题——因为 centering 本身就削弱了 PRM 绝对分数的影响。Proposal 需要清晰论证 per-step gating 在什么场景下比 trajectory-level centering 更优。\n  \n  **建议**：在 core claim 中增加一个明确的 desideratum argument——\"per-step adaptive gating\" 之所以必要，是因为 PRM calibration quality **在不同 step types 间差异巨大**（例如，计算步骤 vs. 概念推理步骤的 calibration 特性可能截然不同），而全局方法无法捕捉这种 heterogeneity。如果能在 preliminary analysis 中展示 PRM uncertainty 的 per-step heterogeneity（即不同步骤类型的 confidence width 分布差异显著），这会极大强化 per-step gating 的必要性论证。\n- 价值: 直接回应审稿人最可能的第一个质疑——\"为什么不用更简单的方法\"。这是 Novelty 和 Significance 的基石，如果回答不了这个问题，整个 idea 的增量价值就站不住。\n- 调研依据: PROGRS (arXiv 2604.02341) 已使用 frozen quantile-regression PRM 进入 RL 训练但用 trajectory-level centering 而非 per-step gating，是最直接的 trivial alternative 威胁。\n\n【发掘点 2】\n- 维度: novelty 锐化\n- 内容: 当前 proposal 的 novelty framing 是\"第一个将 PRM calibration 用于 RL credit assignment\"，但这个 framing 有被 PROGRS 部分侵蚀的风险——PROGRS 也用了 calibrated PRM（quantile regression）在 RL 训练中。虽然机制不同，但审稿人可能认为\"用 calibrated PRM 在 RL 训练中\"这个大方向已经被 PROGRS 占据。\n\n  **建议锐化 novelty angle 为**：UGCA 的核心新颖性不仅是\"用 calibrated PRM\"，而是建立了一个**原则性的 process-outcome interpolation 框架，由 PRM 自身的 epistemic uncertainty 驱动**。具体而言：\n  1. PROGRS 的 centering 是 deterministic rule（所有 incorrect trajectory 的 PRM score 被 centered 到 zero mean），没有使用 PRM 的 uncertainty information。\n  2. UGCA 的 gating 是 uncertainty-driven——每个步骤根据 PRM 自己\"知道多少\"来决定信任程度。这是一种 **verifier self-awareness** 的思路，类似于 selective prediction / \"know what you don't know\" 范式在 RL credit assignment 中的首次应用。\n  3. 理论上，这与 Jia et al. 的 equivalence result 形成更强的连接：既然 outcome 和 process supervision 统计等价，那最优策略应该是在 PRM confident 的地方用 process credit（lower variance），在 PRM uncertain 的地方用 outcome credit（unbiased）——这是一个 **bias-variance tradeoff** 的故事，比 \"bridging calibration and RL\" 更深刻。\n  \n  将 novelty framing 从 \"calibration → RL\" 升级为 \"**uncertainty-driven bias-variance tradeoff in credit assignment**\"，会让 contribution 更加 sharp 和 principled。\n- 价值: 将 novelty 从\"工程性组合\"提升到\"原则性框架\"，命中 Novelty 维度的天花板。审稿人区分 \"nice engineering\" 和 \"principled contribution\" 的关键就在于是否有一个更深层的 insight 支撑。\n- 调研依据: PROGRS (arXiv 2604.02341) 使用 calibrated PRM 但不使用 uncertainty；Jia et al. (ICML 2025) 的 statistical equivalence 为 bias-variance tradeoff framing 提供理论基础；\"Know What You Don't Know\" (NeurIPS 2025) 的 selective prediction 思想可类比。\n\n【发掘点 3】\n- 维度: related work 差异化\n- 内容: Proposal 的 related work 覆盖较全面，但遗漏了两个可能被审稿人提出的高度相关工作，需要主动纳入并做差异化论述：\n  1. **\"Discovering Process-Outcome Credit in Multi-Step LLM Reasoning\" (arXiv 2602.01034)**：这篇工作也在做 process-outcome credit 的混合分配（Step-wise Marginal Information Gain + Decoupled Masking），虽然不基于 PRM uncertainty，但\"process-outcome credit interpolation\"的大方向高度重叠。必须说清楚差异：他们用 intrinsic information gain 做 step value assessment，UGCA 用 PRM calibration uncertainty 做 gating——前者需要 Monte Carlo estimation of marginal information gain（计算开销大且有 variance），后者只需要 one-time quantile calibration（更轻量且 principled）。\n  2. **\"Save the Good Prefix\" / VPPO (arXiv 2601.18984)**：也用 PRM 信号来做 per-step 差异化处理（binary: correct prefix vs. erroneous suffix），可以视为 UGCA 的一个 degenerate special case（binary gating with hard threshold）。应该论证 continuous uncertainty gating 优于 binary first-error detection 的场景：当 PRM 对某些步骤不确定时，VPPO 的 binary 判断会引入 false positive errors，而 UGCA 的 soft gating 可以优雅地处理这种不确定性。\n  3. **\"GRPO is Secretly a Process Reward Model\" (arXiv 2509.21154, ICLR 2026)**：这篇证明了 GRPO+ORM 在 shared-prefix 条件下隐式等价于 PRM-aware RL。这对 UGCA 有双面影响——一方面支持 process-outcome interpolation 的合理性，另一方面暗示 vanilla GRPO 可能已经在做某种隐式的 process credit。Proposal 应该正面回应：GRPO 的隐式 process credit 是 **uniform** 的（不区分 PRM confident 和 uncertain 的步骤），而 UGCA 是 **adaptive** 的——正是这种 adaptivity 带来了额外收益。\n- 价值: 堵住审稿人最可能的 \"missing related work\" 质疑，同时通过差异化论述反向强化 UGCA 的 positioning。命中 Related Work 差异化维度。\n- 调研依据: 上述三篇论文均在前置调研中发现，分别代表 process-outcome credit 混合分配、PRM-guided per-step 差异化、GRPO 隐式 process credit 三个相关方向。\n\n【发掘点 4】\n- 维度: significance 提升\n- 内容: 当前 proposal 的 significance framing 主要是 \"减少 reward hacking，提升 math reasoning accuracy\"，这是一个 solid 但 incremental 的故事。可以将 significance 提升到更高层面：\n\n  **UGCA 实际上在回答一个更广义的问题：当 verifier 不完美时，RL 训练应该如何 gracefully degrade？** 这个问题远超 math reasoning 的范畴——在 code generation（compiler verifier 对 runtime behavior 不确定）、scientific reasoning（PRM 对 domain-specific steps 不确定）、agentic tasks（environment feedback 部分 observable）中都存在 verifier uncertainty 的问题。\n\n  **建议**：在 introduction 中将研究问题 reframe 为 \"**principled degradation under verifier uncertainty**\"，将 math reasoning 定位为 \"a clean testbed where process verifier (PRM) uncertainty is measurable and calibratable\"，然后在 discussion 中指出 UGCA framework 的 generalization potential。这不需要做额外实验，只需要在 framing 上更有野心。\n  \n  但注意分寸：不要 overclaim generalization without evidence。只需要在 discussion 中 briefly 指出这个方向，并在 math reasoning 这个 testbed 上充分验证核心机制。\n- 价值: 将 significance 从 \"math reasoning 的一个改进\" 提升到 \"RL-from-imperfect-verifiers 的原则性方案\"，吸引更广泛的审稿人兴趣。命中 Significance 维度。\n- 调研依据: 基于领域整体趋势判断——Uncertainty-Aware Reward Discounting (arXiv 2604.26360) 在 general RLHF 中做 uncertainty-aware reward modulation 说明这个问题的 general interest 已经存在；Jia et al. (ICML 2025) 的 theoretical framework 本身就是 task-agnostic 的。\n\n【发掘点 5】\n- 维度: 核心 claim 强化\n- 内容: Proposal 引用 Jia et al. (ICML 2025) 的 statistical equivalence result 来 justify \"uncertain 时退化到 outcome credit 是 principled 的\"，但这个 justification 可以做得更紧密。Jia et al. 的 result 说的是\"在 standard coverage conditions 下，outcome supervision **统计上不比** process supervision 更难\"，这是一个 **worst-case statistical** 的 statement，不直接 imply \"在某个具体步骤上，当 PRM uncertain 时，切换到 outcome credit 是最优的\"。\n\n  **建议强化理论连接**：将 UGCA 的 gating mechanism 显式 frame 为一个 **bias-variance tradeoff**：\n  - Process credit (A^min) 的 bias 取决于 PRM calibration quality（PRM miscalibrated → high bias），variance 较低（因为提供 dense signal）\n  - Outcome credit (A^GRPO) 是 unbiased（verifiable rewards），但 variance 较高（sparse, trajectory-level signal）\n  - α_i = σ(−(w_i − τ)/β) 本质上是在 bias-variance frontier 上做 per-step optimal interpolation\n  - 当 PRM well-calibrated（w_i 小）→ high α → lean on low-variance process credit\n  - 当 PRM uncertain（w_i 大）→ low α → fall back to unbiased outcome credit\n  \n  这个 bias-variance framing 比简单引用 Jia et al. 的 equivalence result 更有说服力，因为它给出了一个 **prescriptive** 的理由（而非仅仅是 \"it's okay to do this\"）。如果能在 appendix 中用简化假设（e.g., Gaussian noise on PRM scores）推导出 α 的 optimal form 并展示它与 sigmoid gating 的近似关系，这会极大增强理论 grounding。\n- 价值: 从 \"theoretically motivated\" 升级到 \"theoretically grounded\"——前者只是 \"有理论支持我们可以这样做\"，后者是 \"理论告诉我们应该这样做\"。这是 novelty 和 soundness 的关键跃迁。\n- 调研依据: Jia et al. (ICML 2025) 的 statistical equivalence result 提供了基础框架；bias-variance tradeoff 的 framing 参考了 calibration 文献中 selective prediction 的经典思路。\n\nSources:\n- [Distributional Process Reward Models (arXiv 2605.06785)](https://arxiv.org/abs/2605.06785)\n- [PROGRS: LLM Reasoning with Process Rewards for Outcome-Guided Steps](https://arxiv.org/pdf/2604.02341)\n- [Discovering Process-Outcome Credit in Multi-Step LLM Reasoning](https://arxiv.org/abs/2602.01034)\n- [Save the Good Prefix (VPPO)](https://arxiv.org/abs/2601.18984)\n- [GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154)\n- [Uncertainty-Aware Reward Discounting](https://arxiv.org/abs/2604.26360)\n- [PRPO: Aligning Process Reward with Outcome Reward](https://arxiv.org/abs/2601.07182)\n- [Know What You Don't Know: Uncertainty Calibration of PRMs (NeurIPS 2025)](https://arxiv.org/html/2506.09338)\n- [Do We Need to Verify Step by Step? (ICML 2025)](https://arxiv.org/abs/2502.10581)\n- [PRIME: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)\n- [Stop Summation: Min-Form Credit Assignment (PURE)](https://arxiv.org/pdf/2504.15275)\n- [Good Learners Think Their Thinking (TP-GRPO)](https://arxiv.org/pdf/2507.23317)\n- [Beyond Correctness: Harmonizing Process and Outcome Rewards (PROF)](https://openreview.net/forum?id=JKr77ZmZcM)\n\n【补救 agent 本轮输出】:\nNow I have sufficient research to provide a thorough evaluation. Let me compile my analysis.\n\n---\n\n【状态】: 有缺陷待补救\n\n【前置调研发现】\n- **PURE / Stop Summation (NeurIPS 2025)**: Experiments on Qwen2.5-Math-7B, baselines include GRPO, SimpleRL, PRIME. Evaluates on MATH-500, AMC23, and 3 additional benchmarks (5 total). Uses ~8K MATH training prompts (difficulty 3–5). Reports pass@1, training reward curves, and per-step reward distribution analysis to demonstrate reduced reward hacking.\n- **GRPO-λ (arXiv Oct 2025)**: Trains 1.5B to 7B models (LLaMA-3.1 and Qwen2.5), compares against vanilla GRPO across 4 math datasets. Reports training curves showing 30–40% improved training efficiency. Ablates different λ-return weighting variants.\n- **PROGRS (arXiv Apr 2026)**: Uses a frozen quantile-regression PRM with outcome-conditioned centering. Evaluates on MATH-500, AMC, AIME, MinervaMath, OlympiadBench (5 benchmarks). Baselines include DAPO, GRPO, outcome-only variants. This is the closest concurrent work—also integrates calibrated PRM into RL, though at trajectory-level not per-step.\n- **DAPO (2025)**: Now a standard baseline for math RL on Qwen models. Introduces Clip-Higher, Dynamic Sampling, token-level loss. Results on AIME 2024 widely cited. DARO (2025) claims to outperform DAPO with faster convergence.\n- **Uncertainty-Aware Reward Discounting (arXiv Apr 2026)**: Uses ensemble disagreement for dual-source uncertainty (epistemic + preference). Ablation shows discounting mechanism is primary driver; uncertainty estimation alone provides modest gains. Targets general RLHF, not math-specific process-outcome interpolation.\n- **Reward Hacking on PRMs (arXiv 2026, \"Reward Under Attack\")**: Shows RL-trained policies achieve PRM scores >0.9 while ground-truth accuracy <4% on AIME, demonstrating PRMs function as fluency detectors under reward hacking. This directly motivates UGCA's approach.\n- **PRPO (arXiv Jan 2026)**: Process-outcome alignment via location-parameter shift on Qwen2.5-Math-1.5B. Evaluates on MATH-500. Uses semantic-based step segmentation.\n- **AIME 2025 benchmark**: Now widely adopted as standard evaluation alongside AIME 2024; 30 problems, frontier models solve most but hardest remain challenging.\n- **veRL framework**: Confirmed compatible with Qwen3-8B, supports GRPO/DAPO and custom reward integration. PURE codebase is open-source on GitHub.\n\n- **调研总结**: 这个领域当前的实验设计标准要求：(1) 至少包含 GRPO、DAPO 作为 outcome-only baseline，以及至少一个 process-aware baseline（如 PURE/PROGRS）；(2) 评测覆盖 MATH-500 + 至少 3 个 OOD 竞赛级 benchmark（AMC、AIME24、AIME25、OlympiadBench）；(3) 明确的 reward hacking 量化指标（如 PRM score vs. ground-truth accuracy gap、reward overoptimization curves）；(4) 多 seed 统计显著性报告。审稿人普遍要求 ablation 覆盖各组件贡献、以及与最相似 concurrent work 的直接对比。\n\n---\n\n【缺陷 1】\n- 类别: baseline 不足或过时\n- 问题: Proposal 将 baselines 限定为 \"re-implemented PURE, GRPO, and GRPO-λ\"，缺少两个关键 baseline：**(a) DAPO**——目前已成为 Qwen 系列 math RL 训练的标准 baseline，几乎所有 2026 年论文都将其纳入对比；**(b) PROGRS**——这是最接近的 concurrent work，同样使用 frozen quantile-regression PRM 介入 RL 训练（虽然在 trajectory 层面而非 per-step），不与其直接对比会被审稿人立即质疑。\n- 严重度: 可补救\n- 补救方案: \n  - 将 DAPO 加入 baseline 列表。DAPO 的实现已集成在 veRL 框架中，增加的实验开销很小（每个模型 scale 增加约 1 个配置的训练时间）。\n  - 将 PROGRS 加入 baseline 列表。如果 PROGRS 代码不开源，可以基于论文描述在 PURE/veRL codebase 上复现其 outcome-conditioned centering 机制——核心实现并不复杂（对 PRM scores 做 outcome-group 内零均值化）。\n  - 这会将每个 model scale 的配置数从 6 增加到约 8，增加约 600 H100-hours（Qwen3-8B ×2 configs ≈ 400h，Qwen3-1.7B ×2 configs ≈ 120h，evaluation ≈ 80h），总 GPU 预算上升至约 2400 H100-hours（~$6,000）。\n- 调研依据: PROGRS (arXiv 2604.02341) 在实验中以 DAPO 和 GRPO 为 baseline，并在 5 个 benchmark 上报告结果；DARO (arXiv 2510.09001) 明确将 DAPO 作为必须超越的 baseline。\n\n【缺陷 2】\n- 类别: 实验设计不足\n- 问题: Proposal 的评测 benchmark 为 MATH-500、AMC23、AIME24、OlympiadBench，缺少 **AIME 2025**。AIME 2025 已在 2026 年成为标准 OOD 评测集（30 题，含更新的难度分布），几乎所有近期论文都同时报告 AIME24 和 AIME25。此外，**MinervaMath** 也是 PROGRS 等论文采用的标准 benchmark。不纳入会显得评测覆盖不够全面。\n- 严重度: 可补救\n- 补救方案: 在评测列表中增加 AIME 2025 和 MinervaMath。这两个 benchmark 均为公开可用的评测集，评测开销极小（纯推理），不影响 GPU 预算和时间线。\n- 调研依据: PROGRS 评测覆盖 MATH-500, AMC, AIME, MinervaMath, OlympiadBench 共 5 个 benchmark；AIME 2025 benchmark 已被 Artificial Analysis、IntuitionLabs 等机构采用为标准评测。\n\n【缺陷 3】\n- 类别: 评估方案缺陷\n- 问题: Proposal 提到 \"demonstrating measurably reduced reward hacking on PRM-uncertain steps\" 和 \"reward-hacking diagnostics\"，但**没有定义具体的量化指标**。审稿人会要求明确 reward hacking 的度量方式。近期文献（Reward Under Attack, arXiv 2603.06621）已证明 PRM score 与 ground-truth accuracy 的严重脱节（PRM>0.9 但 accuracy<4%），UGCA 的核心 claim 之一正是缓解这一问题，必须有可量化的证据。\n- 严重度: 可补救\n- 补救方案: 明确定义以下 reward hacking 量化指标：\n  1. **PRM-Accuracy Gap (PAG)**: 在训练过程中定期采样 rollouts，计算 PRM mean score 与 ground-truth pass rate 的差值，绘制 overoptimization curve（类似 Gao et al. 2023 的 BoN reward hacking curve）。\n  2. **Per-step uncertainty-conditioned accuracy**: 将 steps 按 PRM confidence-interval width 分箱（如 5 个 quantile bins），分别报告每个 bin 内的 step correctness（需要在 PRM-Bench 或类似数据上验证）。\n  3. **Reward hacking rate**: 定义为 \"PRM score 高于阈值但最终答案错误\" 的 trajectory 比例，比较 UGCA 与 baselines 在训练后期的该指标。\n  这些指标计算开销很小，且已在近期文献中有先例。\n- 调研依据: \"Reward Under Attack\" (arXiv 2603.06621) 报告了 PRM score vs. accuracy gap 作为 reward hacking 量化指标；Uncertainty-Aware Reward Discounting (arXiv 2604.26360) 使用 reward overoptimization curve 作为主要分析工具。\n\n【缺陷 4】\n- 类别: ablation 不完整\n- 问题: Proposal 提到在 1.7B 上做 \"ablations over gating threshold τ, temperature β, and quantile level\" 的超参数搜索，但缺少以下关键 ablation：\n  **(a) Boundary cases ablation**: α≡1（纯 PURE process credit）和 α≡0（纯 GRPO outcome credit）应作为 ablation 端点，证明插值确实优于两个极端——这也同时验证了 Jia et al. 的理论动机。\n  **(b) Gating function form ablation**: 当前使用 sigmoid gating，但硬阈值（hard gating: α=1 if w<τ else α=0）也是自然的 alternative，需要对比证明 soft gating 的优越性。\n  **(c) Calibration method ablation**: Proposal 使用 quantile regression，但 Distributional PRM (arXiv 2605.06785) 提出的 conditional optimal transport 方法声称更优的 calibration。至少应讨论（理想情况下应对比）不同 calibration 方法对下游 RL 效果的影响。\n  **(d) 组件贡献隔离**: 需要区分 \"calibration 本身带来的改进\" 和 \"uncertainty-gated interpolation 带来的改进\"——一个简单的 ablation 是使用 uncalibrated PRM 的 raw score variance 作为 uncertainty proxy，对比 calibrated confidence-interval width。\n- 严重度: 可补救\n- 补救方案: \n  - (a) 和 (b) 可在 1.7B 模型上完成，每个 ablation 1 run，增加约 180 H100-hours。\n  - (c) 如果 Distributional PRM 代码开源，可做对比；若不开源，至少在 paper 中讨论并将其列为 future work。\n  - (d) 可在 1.7B 上增加 1 个 \"uncalibrated variance gating\" 配置，约 60 H100-hours。\n  - 总增加约 240–300 H100-hours。建议将 1.7B ablation configs 从 6 扩展到约 10–12。\n- 调研依据: PURE 论文对 min-form vs. sum-form 做了完整的 ablation 对比；Uncertainty-Aware Reward Discounting 的 ablation 明确隔离了 discounting mechanism 和 uncertainty estimation 各自的贡献；PROGRS 对比了不同 centering 策略。\n\n【缺陷 5】\n- 类别: 实验设计不足\n- 问题: Proposal **没有提到多 seed 实验和统计显著性报告**。RL 训练在 math reasoning 领域具有较高的随机性（不同 seed 可导致 2–4% 的 accuracy 波动），仅单次运行的结果容易被审稿人质疑为 cherry-picking。这在该领域是一个普遍的审稿关注点。\n- 严重度: 可补救\n- 补救方案: \n  - 对 final comparison（8B 模型上的 UGCA vs. PURE vs. GRPO vs. DAPO）至少跑 3 seeds，报告 mean ± std。\n  - 如果 8B 三 seeds 的 compute 开销过高（每个 config 3×200h = 额外 1200h），可以折衷：8B 只跑 top 2 configuration 各 3 seeds，其余跑 1 seed；1.7B ablation 全部跑 3 seeds（开销较小）。\n  - 或者：采用 bootstrap confidence interval 的方式在单次训练的 evaluation 上计算统计显著性（在 MATH-500 的 500 题上做 bootstrap resampling）。后者开销为零但统计效力较弱。\n  - 建议至少采用 evaluation-level bootstrap + 1.7B 多 seed 方案，8B 如果预算允许则加 seed。\n- 调研依据: 基于领域实验规范判断——PURE 论文虽然未报告多 seed，但该论文为 NeurIPS 2025 oral，审稿要求可能更高的 AAAI 投稿需提前准备。GRPO-λ 在 OpenReview reviews 中被要求补充 variance 分析。\n\n【缺陷 6】\n- 类别: compute 公平性问题\n- 问题: UGCA 相比 baseline 方法引入了额外的 PRM quantile calibration 步骤（proposal 估算 100 H100-hours）以及每步推理时的 confidence-interval width 计算。在 compute-normalized comparison 中，需要确保对比公平：(a) calibration 的一次性开销应从 per-training-run 对比中排除或明确注明；(b) 如果每步 gating 计算增加了 per-step 训练延迟，需要报告 wall-clock time 对比；(c) 基于 PURE 的 advantage 计算本身就涉及 min-form 的步级运算，UGCA 在此基础上增加的开销比例是多少？\n- 严重度: 可补救\n- 补救方案: \n  - 在实验中明确报告：(1) 各方法的 training FLOPs 或 wall-clock time 对比；(2) PRM calibration 的一次性开销单独列出；(3) per-step gating 带来的额外推理延迟百分比。\n  - 绘制 \"accuracy vs. training compute\" 的 Pareto curve，而非仅报告 final accuracy。\n  - 这不需要额外实验，只需在现有实验中记录相应 metrics。\n- 调研依据: PURE 在论文中明确报告了 \"1/5th compute\" 的对比；PROGRS 同样报告了 \"fewer rollouts\" 的效率对比。Compute-normalized comparison 是该领域审稿人的标准要求。\n\n【缺陷 7】\n- 类别: 可行性问题\n- 问题: Proposal 使用 Qwen2.5-Math-PRM-7B 作为 PRM，但训练的 policy 模型为 **Qwen3** 系列（8B 和 1.7B）。Qwen3 和 Qwen2.5 的 tokenizer 和 generation style（如 step delimiter、思维链格式）可能存在差异，这可能导致：(a) PRM 对 Qwen3 生成的推理步骤的评分不准确（distribution shift）；(b) quantile calibration 在 Qwen2.5 生成的数据上拟合，但应用于 Qwen3 生成的数据时 calibration 失效。这不是致命问题（cross-family PRM 使用在该领域有先例），但需要在实验中验证和讨论。\n- 严重度: 可补救\n- 补救方案: \n  - 增加一个 **PRM cross-family validation** 实验：在 Qwen3-8B 的初始（RL 前）rollouts 上计算 PRM calibration 质量（ECE, Brier score），与在 Qwen2.5 rollouts 上的 calibration 质量对比，确认 calibration 未严重退化。\n  - 如果发现显著退化，需要在 Qwen3 rollouts 上重新做 quantile calibration fine-tuning（增加约 50–100 H100-hours）。\n  - 在 paper 的 limitations section 中讨论此 cross-family transfer 问题。\n  - 该验证实验开销极小（纯推理 + 统计计算），不影响时间线。\n- 调研依据: Park et al. (NeurIPS 2025) 的 quantile calibration 实验明确区分了 in-distribution (MATH500) 和 out-of-distribution (AIME24-25) 的 calibration 质量，发现 OOD 场景下 calibration error 增大。Qwen3 vs Qwen2.5 的 distribution shift 类似于 OOD 场景。\n\n---\n\n**总结**: 上述 7 个缺陷均为**可补救**，不存在方向性致命问题。其中缺陷 1（缺 DAPO/PROGRS baseline）和缺陷 3（reward hacking 量化指标缺失）是最可能被审稿人直接 challenge 的关键问题，优先级最高。缺陷 4（ablation 不完整）和缺陷 5（统计显著性）也是常见 reject 原因，建议在 8 周时间线内优先解决。补救后总 GPU 预算估算从 ~1800 增至 ~2500–2700 H100-hours（~$6,500–6,750），仍在可控范围内。实验设计的整体框架是 sound 的，核心需要的是补充 baseline 覆盖、明确评估指标、完善 ablation 矩阵。\n\nSources:\n- [PURE - Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)\n- [PURE GitHub Repository](https://github.com/CJReinforce/PURE)\n- [GRPO-λ (arXiv 2025)](https://arxiv.org/abs/2510.00194)\n- [PROGRS - LLM Reasoning with Process Rewards](https://arxiv.org/pdf/2604.02341)\n- [Distributional PRM via Conditional Optimal Transport](https://arxiv.org/html/2605.06785)\n- [Park et al. - PRM Uncertainty Calibration (NeurIPS 2025)](https://young-j-park.github.io/know-what-you-dont-know/)\n- [Uncertainty-Aware Reward Discounting (arXiv 2026)](https://arxiv.org/abs/2604.26360)\n- [Reward Under Attack: PRM Robustness (arXiv 2026)](https://arxiv.org/pdf/2603.06621)\n- [PRPO (arXiv 2026)](https://arxiv.org/pdf/2601.07182)\n- [DAPO / Post-Training Techniques 2026](https://llm-stats.com/blog/research/post-training-techniques-2026)\n- [DARO (arXiv 2025)](https://arxiv.org/pdf/2510.09001)\n- [AIME 2025 Benchmark](https://artificialanalysis.ai/evaluations/aime-2025)\n- [veRL Framework](https://github.com/verl-project/verl)"
}
```

---

### Runtime record

_source line 13 · 2026-05-27T08:17:34.342Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:17:34.342Z",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

## Round 2

32 recorded events

### User

_source line 14 · 2026-05-27T08:17:34.403Z_

【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
Now I have enough research context. Let me synthesize my findings and produce the assessment.

---

【状态】: 有发掘空间

【前置调研发现】

- **Distributional PRM (arXiv 2605.06785, May 2026)**: 提出 conditional optimal transport 校准 PRM，显著优于 quantile regression，但明确只用于 test-time scaling（best-of-N），未涉及 RL 训练时的 credit assignment。与本 proposal 的关系：本文选择 quantile regression 作为校准方法，但这篇更新的工作表明 conditional OT 在 calibration 质量上更优，可能影响方法选择。
- **PROGRS (arXiv 2604.02341, Apr 2026)**: 使用 frozen quantile-regression PRM + outcome-conditioned centering，在 trajectory 级别做固定 centering rule，而非 per-step adaptive gating。与本 proposal 最接近的竞争者——同样使用了 calibrated PRM 进入 RL 训练，但机制不同（固定 centering vs. per-step uncertainty-gated interpolation）。
- **"Discovering Process-Outcome Credit in Multi-Step LLM Reasoning" (arXiv 2602.01034, Feb 2026)**: 提出 Step-wise Marginal Information Gain + Decoupled Masking，在 process-outcome credit 分配上做了 decoupling，是另一种 process-outcome 混合 credit 的思路，但不基于 PRM uncertainty。
- **VPPO / "Save the Good Prefix" (arXiv 2601.18984, Jan 2026)**: 用 PRM 定位第一个错误步骤，将轨迹分为 correct prefix + erroneous suffix，做 targeted penalization。与本 proposal 互补但不重叠——它用 PRM 做 binary 分割而非连续 uncertainty gating。
- **"GRPO is Secretly a Process Reward Model" (arXiv 2509.21154, Sep 2025, ICLR 2026)**: 证明 GRPO + ORM 在 identical-prefix 条件下等价于 PRM-aware RL，暗示 GRPO 本身已隐式包含 process credit。这对本 proposal 既是支持（说明 process-outcome interpolation 有理论基础）也是挑战（GRPO 可能已经 partially 在做这件事）。
- **Uncertainty-Aware Reward Discounting (arXiv 2604.26360, Apr 2026)**: 用 ensemble disagreement 做 uncertainty-aware reward modulation 来缓解 reward hacking，但针对 general RLHF，非 math reasoning 的 process-outcome interpolation。
- **Jia et al. (ICML 2025)**: 证明 outcome supervision 在统计意义上不比 process supervision 更难，差异在于算法层面（梯度动态等），为 "uncertain 时退化到 outcome credit" 提供了理论支撑。
- **PRIME (arXiv 2502.01456, Feb 2025)**: 通过 implicit process rewards 实现 online PRM 更新，缓解 distribution shift，但均匀信任 PRM 信号。

- **调研总结**: 当前领域研究者主要在两个方向突破：(1) 如何让 PRM 信号更可靠（calibration, distributional PRM, generative PRM）；(2) 如何在 RL 训练中更好地混合 process 和 outcome credit（PROGRS, PRPO, Discovering Process-Outcome Credit, VPPO）。但这两个方向目前是**分离**的——calibration 工作只服务于 test-time，credit assignment 工作不考虑 PRM 信号的可靠性差异。本 proposal 正好处于这两个方向的**交汇点**。

---

【发掘点 1】
- 维度: 前提假设质疑 / trivial alternative 威胁
- 内容: Proposal 的核心前提是"PRM 在 uncertain steps 上的 miscalibration 导致 reward hacking"，但需要更严格地论证**为什么 per-step uncertainty gating 优于更简单的 alternatives**。具体地，存在至少两个 trivial alternatives 需要正面回应：
  - **Alternative 1: 全局 clipping/truncation**。如果 PRM miscalibration 是主要问题，直接 clip 掉 confidence 低于阈值的 PRM 分数（将其置零或 fallback 到 outcome reward），不需要 sigmoid gating 的连续插值，也不需要额外的 β 温度参数。这个 simpler baseline 是否已经足够？
  - **Alternative 2: PROGRS 的 outcome-conditioned centering**。PROGRS 已经在用 calibrated PRM（同样是 quantile regression）做 RL training credit assignment，虽然机制不同（trajectory-level centering vs. per-step gating），但它可能已经 implicitly 解决了 miscalibration 问题——因为 centering 本身就削弱了 PRM 绝对分数的影响。Proposal 需要清晰论证 per-step gating 在什么场景下比 trajectory-level centering 更优。
  
  **建议**：在 core claim 中增加一个明确的 desideratum argument——"per-step adaptive gating" 之所以必要，是因为 PRM calibration quality **在不同 step types 间差异巨大**（例如，计算步骤 vs. 概念推理步骤的 calibration 特性可能截然不同），而全局方法无法捕捉这种 heterogeneity。如果能在 preliminary analysis 中展示 PRM uncertainty 的 per-step heterogeneity（即不同步骤类型的 confidence width 分布差异显著），这会极大强化 per-step gating 的必要性论证。
- 价值: 直接回应审稿人最可能的第一个质疑——"为什么不用更简单的方法"。这是 Novelty 和 Significance 的基石，如果回答不了这个问题，整个 idea 的增量价值就站不住。
- 调研依据: PROGRS (arXiv 2604.02341) 已使用 frozen quantile-regression PRM 进入 RL 训练但用 trajectory-level centering 而非 per-step gating，是最直接的 trivial alternative 威胁。

【发掘点 2】
- 维度: novelty 锐化
- 内容: 当前 proposal 的 novelty framing 是"第一个将 PRM calibration 用于 RL credit assignment"，但这个 framing 有被 PROGRS 部分侵蚀的风险——PROGRS 也用了 calibrated PRM（quantile regression）在 RL 训练中。虽然机制不同，但审稿人可能认为"用 calibrated PRM 在 RL 训练中"这个大方向已经被 PROGRS 占据。

  **建议锐化 novelty angle 为**：UGCA 的核心新颖性不仅是"用 calibrated PRM"，而是建立了一个**原则性的 process-outcome interpolation 框架，由 PRM 自身的 epistemic uncertainty 驱动**。具体而言：
  1. PROGRS 的 centering 是 deterministic rule（所有 incorrect trajectory 的 PRM score 被 centered 到 zero mean），没有使用 PRM 的 uncertainty information。
  2. UGCA 的 gating 是 uncertainty-driven——每个步骤根据 PRM 自己"知道多少"来决定信任程度。这是一种 **verifier self-awareness** 的思路，类似于 selective prediction / "know what you don't know" 范式在 RL credit assignment 中的首次应用。
  3. 理论上，这与 Jia et al. 的 equivalence result 形成更强的连接：既然 outcome 和 process supervision 统计等价，那最优策略应该是在 PRM confident 的地方用 process credit（lower variance），在 PRM uncertain 的地方用 outcome credit（unbiased）——这是一个 **bias-variance tradeoff** 的故事，比 "bridging calibration and RL" 更深刻。
  
  将 novelty framing 从 "calibration → RL" 升级为 "**uncertainty-driven bias-variance tradeoff in credit assignment**"，会让 contribution 更加 sharp 和 principled。
- 价值: 将 novelty 从"工程性组合"提升到"原则性框架"，命中 Novelty 维度的天花板。审稿人区分 "nice engineering" 和 "principled contribution" 的关键就在于是否有一个更深层的 insight 支撑。
- 调研依据: PROGRS (arXiv 2604.02341) 使用 calibrated PRM 但不使用 uncertainty；Jia et al. (ICML 2025) 的 statistical equivalence 为 bias-variance tradeoff framing 提供理论基础；"Know What You Don't Know" (NeurIPS 2025) 的 selective prediction 思想可类比。

【发掘点 3】
- 维度: related work 差异化
- 内容: Proposal 的 related work 覆盖较全面，但遗漏了两个可能被审稿人提出的高度相关工作，需要主动纳入并做差异化论述：
  1. **"Discovering Process-Outcome Credit in Multi-Step LLM Reasoning" (arXiv 2602.01034)**：这篇工作也在做 process-outcome credit 的混合分配（Step-wise Marginal Information Gain + Decoupled Masking），虽然不基于 PRM uncertainty，但"process-outcome credit interpolation"的大方向高度重叠。必须说清楚差异：他们用 intrinsic information gain 做 step value assessment，UGCA 用 PRM calibration uncertainty 做 gating——前者需要 Monte Carlo estimation of marginal information gain（计算开销大且有 variance），后者只需要 one-time quantile calibration（更轻量且 principled）。
  2. **"Save the Good Prefix" / VPPO (arXiv 2601.18984)**：也用 PRM 信号来做 per-step 差异化处理（binary: correct prefix vs. erroneous suffix），可以视为 UGCA 的一个 degenerate special case（binary gating with hard threshold）。应该论证 continuous uncertainty gating 优于 binary first-error detection 的场景：当 PRM 对某些步骤不确定时，VPPO 的 binary 判断会引入 false positive errors，而 UGCA 的 soft gating 可以优雅地处理这种不确定性。
  3. **"GRPO is Secretly a Process Reward Model" (arXiv 2509.21154, ICLR 2026)**：这篇证明了 GRPO+ORM 在 shared-prefix 条件下隐式等价于 PRM-aware RL。这对 UGCA 有双面影响——一方面支持 process-outcome interpolation 的合理性，另一方面暗示 vanilla GRPO 可能已经在做某种隐式的 process credit。Proposal 应该正面回应：GRPO 的隐式 process credit 是 **uniform** 的（不区分 PRM confident 和 uncertain 的步骤），而 UGCA 是 **adaptive** 的——正是这种 adaptivity 带来了额外收益。
- 价值: 堵住审稿人最可能的 "missing related work" 质疑，同时通过差异化论述反向强化 UGCA 的 positioning。命中 Related Work 差异化维度。
- 调研依据: 上述三篇论文均在前置调研中发现，分别代表 process-outcome credit 混合分配、PRM-guided per-step 差异化、GRPO 隐式 process credit 三个相关方向。

【发掘点 4】
- 维度: significance 提升
- 内容: 当前 proposal 的 significance framing 主要是 "减少 reward hacking，提升 math reasoning accuracy"，这是一个 solid 但 incremental 的故事。可以将 significance 提升到更高层面：

  **UGCA 实际上在回答一个更广义的问题：当 verifier 不完美时，RL 训练应该如何 gracefully degrade？** 这个问题远超 math reasoning 的范畴——在 code generation（compiler verifier 对 runtime behavior 不确定）、scientific reasoning（PRM 对 domain-specific steps 不确定）、agentic tasks（environment feedback 部分 observable）中都存在 verifier uncertainty 的问题。

  **建议**：在 introduction 中将研究问题 reframe 为 "**principled degradation under verifier uncertainty**"，将 math reasoning 定位为 "a clean testbed where process verifier (PRM) uncertainty is measurable and calibratable"，然后在 discussion 中指出 UGCA framework 的 generalization potential。这不需要做额外实验，只需要在 framing 上更有野心。
  
  但注意分寸：不要 overclaim generalization without evidence。只需要在 discussion 中 briefly 指出这个方向，并在 math reasoning 这个 testbed 上充分验证核心机制。
- 价值: 将 significance 从 "math reasoning 的一个改进" 提升到 "RL-from-imperfect-verifiers 的原则性方案"，吸引更广泛的审稿人兴趣。命中 Significance 维度。
- 调研依据: 基于领域整体趋势判断——Uncertainty-Aware Reward Discounting (arXiv 2604.26360) 在 general RLHF 中做 uncertainty-aware reward modulation 说明这个问题的 general interest 已经存在；Jia et al. (ICML 2025) 的 theoretical framework 本身就是 task-agnostic 的。

【发掘点 5】
- 维度: 核心 claim 强化
- 内容: Proposal 引用 Jia et al. (ICML 2025) 的 statistical equivalence result 来 justify "uncertain 时退化到 outcome credit 是 principled 的"，但这个 justification 可以做得更紧密。Jia et al. 的 result 说的是"在 standard coverage conditions 下，outcome supervision **统计上不比** process supervision 更难"，这是一个 **worst-case statistical** 的 statement，不直接 imply "在某个具体步骤上，当 PRM uncertain 时，切换到 outcome credit 是最优的"。

  **建议强化理论连接**：将 UGCA 的 gating mechanism 显式 frame 为一个 **bias-variance tradeoff**：
  - Process credit (A^min) 的 bias 取决于 PRM calibration quality（PRM miscalibrated → high bias），variance 较低（因为提供 dense signal）
  - Outcome credit (A^GRPO) 是 unbiased（verifiable rewards），但 variance 较高（sparse, trajectory-level signal）
  - α_i = σ(−(w_i − τ)/β) 本质上是在 bias-variance frontier 上做 per-step optimal interpolation
  - 当 PRM well-calibrated（w_i 小）→ high α → lean on low-variance process credit
  - 当 PRM uncertain（w_i 大）→ low α → fall back to unbiased outcome credit
  
  这个 bias-variance framing 比简单引用 Jia et al. 的 equivalence result 更有说服力，因为它给出了一个 **prescriptive** 的理由（而非仅仅是 "it's okay to do this"）。如果能在 appendix 中用简化假设（e.g., Gaussian noise on PRM scores）推导出 α 的 optimal form 并展示它与 sigmoid gating 的近似关系，这会极大增强理论 grounding。
- 价值: 从 "theoretically motivated" 升级到 "theoretically grounded"——前者只是 "有理论支持我们可以这样做"，后者是 "理论告诉我们应该这样做"。这是 novelty 和 soundness 的关键跃迁。
- 调研依据: Jia et al. (ICML 2025) 的 statistical equivalence result 提供了基础框架；bias-variance tradeoff 的 framing 参考了 calibration 文献中 selective prediction 的经典思路。

Sources:
- [Distributional Process Reward Models (arXiv 2605.06785)](https://arxiv.org/abs/2605.06785)
- [PROGRS: LLM Reasoning with Process Rewards for Outcome-Guided Steps](https://arxiv.org/pdf/2604.02341)
- [Discovering Process-Outcome Credit in Multi-Step LLM Reasoning](https://arxiv.org/abs/2602.01034)
- [Save the Good Prefix (VPPO)](https://arxiv.org/abs/2601.18984)
- [GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154)
- [Uncertainty-Aware Reward Discounting](https://arxiv.org/abs/2604.26360)
- [PRPO: Aligning Process Reward with Outcome Reward](https://arxiv.org/abs/2601.07182)
- [Know What You Don't Know: Uncertainty Calibration of PRMs (NeurIPS 2025)](https://arxiv.org/html/2506.09338)
- [Do We Need to Verify Step by Step? (ICML 2025)](https://arxiv.org/abs/2502.10581)
- [PRIME: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)
- [Stop Summation: Min-Form Credit Assignment (PURE)](https://arxiv.org/pdf/2504.15275)
- [Good Learners Think Their Thinking (TP-GRPO)](https://arxiv.org/pdf/2507.23317)
- [Beyond Correctness: Harmonizing Process and Outcome Rewards (PROF)](https://openreview.net/forum?id=JKr77ZmZcM)

【补救 agent 本轮输出】:
Now I have sufficient research to provide a thorough evaluation. Let me compile my analysis.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **PURE / Stop Summation (NeurIPS 2025)**: Experiments on Qwen2.5-Math-7B, baselines include GRPO, SimpleRL, PRIME. Evaluates on MATH-500, AMC23, and 3 additional benchmarks (5 total). Uses ~8K MATH training prompts (difficulty 3–5). Reports pass@1, training reward curves, and per-step reward distribution analysis to demonstrate reduced reward hacking.
- **GRPO-λ (arXiv Oct 2025)**: Trains 1.5B to 7B models (LLaMA-3.1 and Qwen2.5), compares against vanilla GRPO across 4 math datasets. Reports training curves showing 30–40% improved training efficiency. Ablates different λ-return weighting variants.
- **PROGRS (arXiv Apr 2026)**: Uses a frozen quantile-regression PRM with outcome-conditioned centering. Evaluates on MATH-500, AMC, AIME, MinervaMath, OlympiadBench (5 benchmarks). Baselines include DAPO, GRPO, outcome-only variants. This is the closest concurrent work—also integrates calibrated PRM into RL, though at trajectory-level not per-step.
- **DAPO (2025)**: Now a standard baseline for math RL on Qwen models. Introduces Clip-Higher, Dynamic Sampling, token-level loss. Results on AIME 2024 widely cited. DARO (2025) claims to outperform DAPO with faster convergence.
- **Uncertainty-Aware Reward Discounting (arXiv Apr 2026)**: Uses ensemble disagreement for dual-source uncertainty (epistemic + preference). Ablation shows discounting mechanism is primary driver; uncertainty estimation alone provides modest gains. Targets general RLHF, not math-specific process-outcome interpolation.
- **Reward Hacking on PRMs (arXiv 2026, "Reward Under Attack")**: Shows RL-trained policies achieve PRM scores >0.9 while ground-truth accuracy <4% on AIME, demonstrating PRMs function as fluency detectors under reward hacking. This directly motivates UGCA's approach.
- **PRPO (arXiv Jan 2026)**: Process-outcome alignment via location-parameter shift on Qwen2.5-Math-1.5B. Evaluates on MATH-500. Uses semantic-based step segmentation.
- **AIME 2025 benchmark**: Now widely adopted as standard evaluation alongside AIME 2024; 30 problems, frontier models solve most but hardest remain challenging.
- **veRL framework**: Confirmed compatible with Qwen3-8B, supports GRPO/DAPO and custom reward integration. PURE codebase is open-source on GitHub.

- **调研总结**: 这个领域当前的实验设计标准要求：(1) 至少包含 GRPO、DAPO 作为 outcome-only baseline，以及至少一个 process-aware baseline（如 PURE/PROGRS）；(2) 评测覆盖 MATH-500 + 至少 3 个 OOD 竞赛级 benchmark（AMC、AIME24、AIME25、OlympiadBench）；(3) 明确的 reward hacking 量化指标（如 PRM score vs. ground-truth accuracy gap、reward overoptimization curves）；(4) 多 seed 统计显著性报告。审稿人普遍要求 ablation 覆盖各组件贡献、以及与最相似 concurrent work 的直接对比。

---

【缺陷 1】
- 类别: baseline 不足或过时
- 问题: Proposal 将 baselines 限定为 "re-implemented PURE, GRPO, and GRPO-λ"，缺少两个关键 baseline：**(a) DAPO**——目前已成为 Qwen 系列 math RL 训练的标准 baseline，几乎所有 2026 年论文都将其纳入对比；**(b) PROGRS**——这是最接近的 concurrent work，同样使用 frozen quantile-regression PRM 介入 RL 训练（虽然在 trajectory 层面而非 per-step），不与其直接对比会被审稿人立即质疑。
- 严重度: 可补救
- 补救方案: 
  - 将 DAPO 加入 baseline 列表。DAPO 的实现已集成在 veRL 框架中，增加的实验开销很小（每个模型 scale 增加约 1 个配置的训练时间）。
  - 将 PROGRS 加入 baseline 列表。如果 PROGRS 代码不开源，可以基于论文描述在 PURE/veRL codebase 上复现其 outcome-conditioned centering 机制——核心实现并不复杂（对 PRM scores 做 outcome-group 内零均值化）。
  - 这会将每个 model scale 的配置数从 6 增加到约 8，增加约 600 H100-hours（Qwen3-8B ×2 configs ≈ 400h，Qwen3-1.7B ×2 configs ≈ 120h，evaluation ≈ 80h），总 GPU 预算上升至约 2400 H100-hours（~$6,000）。
- 调研依据: PROGRS (arXiv 2604.02341) 在实验中以 DAPO 和 GRPO 为 baseline，并在 5 个 benchmark 上报告结果；DARO (arXiv 2510.09001) 明确将 DAPO 作为必须超越的 baseline。

【缺陷 2】
- 类别: 实验设计不足
- 问题: Proposal 的评测 benchmark 为 MATH-500、AMC23、AIME24、OlympiadBench，缺少 **AIME 2025**。AIME 2025 已在 2026 年成为标准 OOD 评测集（30 题，含更新的难度分布），几乎所有近期论文都同时报告 AIME24 和 AIME25。此外，**MinervaMath** 也是 PROGRS 等论文采用的标准 benchmark。不纳入会显得评测覆盖不够全面。
- 严重度: 可补救
- 补救方案: 在评测列表中增加 AIME 2025 和 MinervaMath。这两个 benchmark 均为公开可用的评测集，评测开销极小（纯推理），不影响 GPU 预算和时间线。
- 调研依据: PROGRS 评测覆盖 MATH-500, AMC, AIME, MinervaMath, OlympiadBench 共 5 个 benchmark；AIME 2025 benchmark 已被 Artificial Analysis、IntuitionLabs 等机构采用为标准评测。

【缺陷 3】
- 类别: 评估方案缺陷
- 问题: Proposal 提到 "demonstrating measurably reduced reward hacking on PRM-uncertain steps" 和 "reward-hacking diagnostics"，但**没有定义具体的量化指标**。审稿人会要求明确 reward hacking 的度量方式。近期文献（Reward Under Attack, arXiv 2603.06621）已证明 PRM score 与 ground-truth accuracy 的严重脱节（PRM>0.9 但 accuracy<4%），UGCA 的核心 claim 之一正是缓解这一问题，必须有可量化的证据。
- 严重度: 可补救
- 补救方案: 明确定义以下 reward hacking 量化指标：
  1. **PRM-Accuracy Gap (PAG)**: 在训练过程中定期采样 rollouts，计算 PRM mean score 与 ground-truth pass rate 的差值，绘制 overoptimization curve（类似 Gao et al. 2023 的 BoN reward hacking curve）。
  2. **Per-step uncertainty-conditioned accuracy**: 将 steps 按 PRM confidence-interval width 分箱（如 5 个 quantile bins），分别报告每个 bin 内的 step correctness（需要在 PRM-Bench 或类似数据上验证）。
  3. **Reward hacking rate**: 定义为 "PRM score 高于阈值但最终答案错误" 的 trajectory 比例，比较 UGCA 与 baselines 在训练后期的该指标。
  这些指标计算开销很小，且已在近期文献中有先例。
- 调研依据: "Reward Under Attack" (arXiv 2603.06621) 报告了 PRM score vs. accuracy gap 作为 reward hacking 量化指标；Uncertainty-Aware Reward Discounting (arXiv 2604.26360) 使用 reward overoptimization curve 作为主要分析工具。

【缺陷 4】
- 类别: ablation 不完整
- 问题: Proposal 提到在 1.7B 上做 "ablations over gating threshold τ, temperature β, and quantile level" 的超参数搜索，但缺少以下关键 ablation：
  **(a) Boundary cases ablation**: α≡1（纯 PURE process credit）和 α≡0（纯 GRPO outcome credit）应作为 ablation 端点，证明插值确实优于两个极端——这也同时验证了 Jia et al. 的理论动机。
  **(b) Gating function form ablation**: 当前使用 sigmoid gating，但硬阈值（hard gating: α=1 if w<τ else α=0）也是自然的 alternative，需要对比证明 soft gating 的优越性。
  **(c) Calibration method ablation**: Proposal 使用 quantile regression，但 Distributional PRM (arXiv 2605.06785) 提出的 conditional optimal transport 方法声称更优的 calibration。至少应讨论（理想情况下应对比）不同 calibration 方法对下游 RL 效果的影响。
  **(d) 组件贡献隔离**: 需要区分 "calibration 本身带来的改进" 和 "uncertainty-gated interpolation 带来的改进"——一个简单的 ablation 是使用 uncalibrated PRM 的 raw score variance 作为 uncertainty proxy，对比 calibrated confidence-interval width。
- 严重度: 可补救
- 补救方案: 
  - (a) 和 (b) 可在 1.7B 模型上完成，每个 ablation 1 run，增加约 180 H100-hours。
  - (c) 如果 Distributional PRM 代码开源，可做对比；若不开源，至少在 paper 中讨论并将其列为 future work。
  - (d) 可在 1.7B 上增加 1 个 "uncalibrated variance gating" 配置，约 60 H100-hours。
  - 总增加约 240–300 H100-hours。建议将 1.7B ablation configs 从 6 扩展到约 10–12。
- 调研依据: PURE 论文对 min-form vs. sum-form 做了完整的 ablation 对比；Uncertainty-Aware Reward Discounting 的 ablation 明确隔离了 discounting mechanism 和 uncertainty estimation 各自的贡献；PROGRS 对比了不同 centering 策略。

【缺陷 5】
- 类别: 实验设计不足
- 问题: Proposal **没有提到多 seed 实验和统计显著性报告**。RL 训练在 math reasoning 领域具有较高的随机性（不同 seed 可导致 2–4% 的 accuracy 波动），仅单次运行的结果容易被审稿人质疑为 cherry-picking。这在该领域是一个普遍的审稿关注点。
- 严重度: 可补救
- 补救方案: 
  - 对 final comparison（8B 模型上的 UGCA vs. PURE vs. GRPO vs. DAPO）至少跑 3 seeds，报告 mean ± std。
  - 如果 8B 三 seeds 的 compute 开销过高（每个 config 3×200h = 额外 1200h），可以折衷：8B 只跑 top 2 configuration 各 3 seeds，其余跑 1 seed；1.7B ablation 全部跑 3 seeds（开销较小）。
  - 或者：采用 bootstrap confidence interval 的方式在单次训练的 evaluation 上计算统计显著性（在 MATH-500 的 500 题上做 bootstrap resampling）。后者开销为零但统计效力较弱。
  - 建议至少采用 evaluation-level bootstrap + 1.7B 多 seed 方案，8B 如果预算允许则加 seed。
- 调研依据: 基于领域实验规范判断——PURE 论文虽然未报告多 seed，但该论文为 NeurIPS 2025 oral，审稿要求可能更高的 AAAI 投稿需提前准备。GRPO-λ 在 OpenReview reviews 中被要求补充 variance 分析。

【缺陷 6】
- 类别: compute 公平性问题
- 问题: UGCA 相比 baseline 方法引入了额外的 PRM quantile calibration 步骤（proposal 估算 100 H100-hours）以及每步推理时的 confidence-interval width 计算。在 compute-normalized comparison 中，需要确保对比公平：(a) calibration 的一次性开销应从 per-training-run 对比中排除或明确注明；(b) 如果每步 gating 计算增加了 per-step 训练延迟，需要报告 wall-clock time 对比；(c) 基于 PURE 的 advantage 计算本身就涉及 min-form 的步级运算，UGCA 在此基础上增加的开销比例是多少？
- 严重度: 可补救
- 补救方案: 
  - 在实验中明确报告：(1) 各方法的 training FLOPs 或 wall-clock time 对比；(2) PRM calibration 的一次性开销单独列出；(3) per-step gating 带来的额外推理延迟百分比。
  - 绘制 "accuracy vs. training compute" 的 Pareto curve，而非仅报告 final accuracy。
  - 这不需要额外实验，只需在现有实验中记录相应 metrics。
- 调研依据: PURE 在论文中明确报告了 "1/5th compute" 的对比；PROGRS 同样报告了 "fewer rollouts" 的效率对比。Compute-normalized comparison 是该领域审稿人的标准要求。

【缺陷 7】
- 类别: 可行性问题
- 问题: Proposal 使用 Qwen2.5-Math-PRM-7B 作为 PRM，但训练的 policy 模型为 **Qwen3** 系列（8B 和 1.7B）。Qwen3 和 Qwen2.5 的 tokenizer 和 generation style（如 step delimiter、思维链格式）可能存在差异，这可能导致：(a) PRM 对 Qwen3 生成的推理步骤的评分不准确（distribution shift）；(b) quantile calibration 在 Qwen2.5 生成的数据上拟合，但应用于 Qwen3 生成的数据时 calibration 失效。这不是致命问题（cross-family PRM 使用在该领域有先例），但需要在实验中验证和讨论。
- 严重度: 可补救
- 补救方案: 
  - 增加一个 **PRM cross-family validation** 实验：在 Qwen3-8B 的初始（RL 前）rollouts 上计算 PRM calibration 质量（ECE, Brier score），与在 Qwen2.5 rollouts 上的 calibration 质量对比，确认 calibration 未严重退化。
  - 如果发现显著退化，需要在 Qwen3 rollouts 上重新做 quantile calibration fine-tuning（增加约 50–100 H100-hours）。
  - 在 paper 的 limitations section 中讨论此 cross-family transfer 问题。
  - 该验证实验开销极小（纯推理 + 统计计算），不影响时间线。
- 调研依据: Park et al. (NeurIPS 2025) 的 quantile calibration 实验明确区分了 in-distribution (MATH500) 和 out-of-distribution (AIME24-25) 的 calibration 质量，发现 OOD 场景下 calibration error 增大。Qwen3 vs Qwen2.5 的 distribution shift 类似于 OOD 场景。

---

**总结**: 上述 7 个缺陷均为**可补救**，不存在方向性致命问题。其中缺陷 1（缺 DAPO/PROGRS baseline）和缺陷 3（reward hacking 量化指标缺失）是最可能被审稿人直接 challenge 的关键问题，优先级最高。缺陷 4（ablation 不完整）和缺陷 5（统计显著性）也是常见 reject 原因，建议在 8 周时间线内优先解决。补救后总 GPU 预算估算从 ~1800 增至 ~2500–2700 H100-hours（~$6,500–6,750），仍在可控范围内。实验设计的整体框架是 sound 的，核心需要的是补充 baseline 覆盖、明确评估指标、完善 ablation 矩阵。

Sources:
- [PURE - Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)
- [PURE GitHub Repository](https://github.com/CJReinforce/PURE)
- [GRPO-λ (arXiv 2025)](https://arxiv.org/abs/2510.00194)
- [PROGRS - LLM Reasoning with Process Rewards](https://arxiv.org/pdf/2604.02341)
- [Distributional PRM via Conditional Optimal Transport](https://arxiv.org/html/2605.06785)
- [Park et al. - PRM Uncertainty Calibration (NeurIPS 2025)](https://young-j-park.github.io/know-what-you-dont-know/)
- [Uncertainty-Aware Reward Discounting (arXiv 2026)](https://arxiv.org/abs/2604.26360)
- [Reward Under Attack: PRM Robustness (arXiv 2026)](https://arxiv.org/pdf/2603.06621)
- [PRPO (arXiv 2026)](https://arxiv.org/pdf/2601.07182)
- [DAPO / Post-Training Techniques 2026](https://llm-stats.com/blog/research/post-training-techniques-2026)
- [DARO (arXiv 2025)](https://arxiv.org/pdf/2510.09001)
- [AIME 2025 Benchmark](https://artificialanalysis.ai/evaluations/aime-2025)
- [veRL Framework](https://github.com/verl-project/verl)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e58d6904-83f3-4f7e-883b-cd1f1ee15f43",
  "isSidechain": false,
  "promptId": "a371b85a-1c37-4393-aeec-4935ec846310",
  "type": "user",
  "uuid": "3e6455c5-2517-4165-a2e5-9ec48a3465a6",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research context. Let me synthesize my findings and produce the assessment.  ---  【状态】: 有…",
  "leafUuid": "3e6455c5-2517-4165-a2e5-9ec48a3465a6",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Assistant

_source line 17 · 2026-05-27T08:17:53.677Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the outputs from both agents and prepare my Role B response for iteration round 1.

**Summary of Discovery Agent findings:**
1. **Trivial alternative threat**: Need to justify per-step gating over simpler alternatives (global clipping, PROGRS trajectory-level centering)
2. **Novelty sharpening**: Reframe from "calibration → RL" to "uncertainty-driven bias-variance tradeoff in credit assignment"
3. **Related work gaps**: Missing 3 key papers - "Discovering Process-Outcome Credit" (arXiv 2602.01034), VPPO/Save the Good Prefix (arXiv 2601.18984), "GRPO is Secretly a PRM" (arXiv 2509.21154, ICLR 2026)


4. **Significance upgrade**: Need to position this as "principled degradation under verifier uncertainty" that extends beyond math reasoning
5. **Core claim strengthening**: Should formalize the bias-variance tradeoff explicitly, possibly with mathematical derivation

**Summary of Remedy Agent findings:**
1. **Missing baselines**: DAPO and PROGRS need to be included
2. **Missing benchmarks**: AIME 2025 and MinervaMath are critical gaps
3. **Reward hacking metrics undefined**: Need to define PAG, per-step uncertainty-conditioned accuracy, and reward hacking rate
4. **Incomplete ablations**: Need boundary cases where α equals 0 or 1, plus hard versus easy problem splits

, calibration method comparisons, and isolated component testing
5. **No multi-seed/statistical significance**: Should run at least 3 seeds or compute bootstrap confidence intervals
6. **Compute fairness**: Need wall-clock time comparisons and Pareto efficiency curves
7. **Cross-family PRM validation**: Should test Qwen2.5-PRM on Qwen3 policy

Now I'm cross-checking the key claims through web search to validate what the Remedy agent suggested. I need to verify whether DAPO and PROGRS are actually standard baselines now, whether PROGRS uses frozen quantile-regression PRMs, if that arXiv paper about GRPO really exists and matches what was claimed, and whether AIME 2025 is considered standard benchmark material.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e6455c5-2517-4165-a2e5-9ec48a3465a6",
  "isSidechain": false,
  "requestId": "req_011CbSk6YP7bSDSevtJt8ysz",
  "type": "assistant",
  "uuid": "4ba7cd25-2b7e-4127-8aae-25b8bdbd88a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMLXzx5V5Ln37hNHwZbCHd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11555,
      "cache_read_input_tokens": 20349,
      "output_tokens": 723,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 723,
          "cache_read_input_tokens": 20349,
          "cache_creation_input_tokens": 11555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11555
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

_source line 18 · 2026-05-27T08:17:53.680Z_

我需要对两位 worker 的关键建议进行交叉验证。让我先做几轮针对性调研。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ba7cd25-2b7e-4127-8aae-25b8bdbd88a6",
  "isSidechain": false,
  "requestId": "req_011CbSk6YP7bSDSevtJt8ysz",
  "type": "assistant",
  "uuid": "0adfd377-3967-4cb9-9b0d-df8510f560e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMLXzx5V5Ln37hNHwZbCHd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11555,
      "cache_read_input_tokens": 20349,
      "output_tokens": 723,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 723,
          "cache_read_input_tokens": 20349,
          "cache_creation_input_tokens": 11555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11555
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

_source line 19 · 2026-05-27T08:17:53.760Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012pHxFYaNurcwZW4qRSJhoH`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0adfd377-3967-4cb9-9b0d-df8510f560e2",
  "isSidechain": false,
  "requestId": "req_011CbSk6YP7bSDSevtJt8ysz",
  "type": "assistant",
  "uuid": "746bd23d-4406-47c9-9b7c-4bad0cdfc99e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMLXzx5V5Ln37hNHwZbCHd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11555,
      "cache_read_input_tokens": 20349,
      "output_tokens": 723,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 723,
          "cache_read_input_tokens": 20349,
          "cache_creation_input_tokens": 11555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11555
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

_source line 20 · 2026-05-27T08:17:53.767Z_

<details><summary>↩ Tool result · `toolu_012pHxFYaNurcwZW4qRSJhoH`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "746bd23d-4406-47c9-9b7c-4bad0cdfc99e",
  "isSidechain": false,
  "promptId": "a371b85a-1c37-4393-aeec-4935ec846310",
  "type": "user",
  "uuid": "dc785442-d716-43eb-ad2a-9d63a446e649",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "746bd23d-4406-47c9-9b7c-4bad0cdfc99e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-27T08:17:57.475Z_

现在让我并行验证几个关键的 worker 建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc785442-d716-43eb-ad2a-9d63a446e649",
  "isSidechain": false,
  "requestId": "req_011CbSk7yE8PrZ7cYmhFCnAx",
  "type": "assistant",
  "uuid": "a2626c99-4b36-4790-bcb1-885b88d7abea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RsfcVXNisrmC8ZrgYw8t7C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1251,
      "cache_read_input_tokens": 31904,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 31904,
          "cache_creation_input_tokens": 1251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1251
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

_source line 22 · 2026-05-27T08:17:58.205Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012sftdiJEvCZBL8WTQ3oNxr`</summary>

```json
{
  "query": "arXiv 2602.01034 \"Discovering Process-Outcome Credit\" multi-step LLM reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2626c99-4b36-4790-bcb1-885b88d7abea",
  "isSidechain": false,
  "requestId": "req_011CbSk7yE8PrZ7cYmhFCnAx",
  "type": "assistant",
  "uuid": "81af0537-a3a5-437c-8f48-4e370635c07a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RsfcVXNisrmC8ZrgYw8t7C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1251,
      "cache_read_input_tokens": 31904,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 31904,
          "cache_creation_input_tokens": 1251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1251
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

_source line 23 · 2026-05-27T08:18:06.064Z_

<details><summary>↩ Tool result · `toolu_012sftdiJEvCZBL8WTQ3oNxr`</summary>

```text
Web search results for query: "arXiv 2602.01034 "Discovering Process-Outcome Credit" multi-step LLM reasoning 2026"

Links: [{"title":"[2602.01034] Discovering Process-Outcome Credit in Multi-Step LLM Reasoning","url":"https://arxiv.org/abs/2602.01034"},{"title":"Discovering Process–Outcome Credit in Multi-Step LLM Reasoning","url":"https://arxiv.org/html/2602.01034"},{"title":"Discovering Process-Outcome Credit in Multi-Step LLM Reasoning","url":"https://arxiv.org/pdf/2602.01034"},{"title":"LLM Reasoning with Process Rewards for Outcome-Guided Steps","url":"https://arxiv.org/pdf/2604.02341"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"},{"title":"PRL: Process Reward Learning Improves LLMs' Reasoning Ability and Broadens the Reasoning Boundary","url":"https://arxiv.org/pdf/2601.10201"},{"title":"A Survey on Feedback-based Multi-step Reasoning for Large Language   Models on Mathematics","url":"https://arxiv.org/pdf/2502.14333"}]

Based on the search results, I found the arXiv paper you're looking for:

## Paper: "Discovering Process-Outcome Credit in Multi-Step LLM Reasoning"

**Authors:** Xiangwei Wang, Wei Wang, Ken Chen, Nanduni Nimalsiri, and Saman Halgamuge

**Paper ID:** arXiv:2602.01034

**Submitted:** February 1, 2026

### Overview

The paper addresses how Reinforcement Learning (RL) serves as a paradigm for enhancing reasoning capabilities in Large Language Models (LLMs), yet standard outcome-based approaches often suffer from reward sparsity and inefficient credit assignment.

### Key Contributions

The authors propose a novel framework with a Step-wise Marginal Information Gain (MIG) mechanism that quantifies the intrinsic value of reasoning steps against a Monotonic Historical Watermark, effectively filtering out training noise. They implement a Decoupled Masking Strategy, applying process-oriented rewards specifically to the chain-of-thought (CoT) and outcome-oriented rewards to the full completion.

### Results

Extensive experiments across textual and multi-modal benchmarks (e.g., MATH, Super-CLEVR) demonstrate that their approach consistently outperforms baselines such as GRPO in both sample efficiency and final accuracy, and the model exhibits superior out-of-distribution robustness with promising zero-shot transfer capabilities to unseen and challenging reasoning tasks.

The paper is available on arXiv at: https://arxiv.org/abs/2602.01034


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81af0537-a3a5-437c-8f48-4e370635c07a",
  "isSidechain": false,
  "promptId": "a371b85a-1c37-4393-aeec-4935ec846310",
  "type": "user",
  "uuid": "29174693-7e70-4969-9975-e50b4238f9a8",
  "toolUseResult": {
    "query": "arXiv 2602.01034 \"Discovering Process-Outcome Credit\" multi-step LLM reasoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DswTXB3hYDWoTkZFy4PkXs",
        "content": [
          {
            "title": "[2602.01034] Discovering Process-Outcome Credit in Multi-Step LLM Reasoning",
            "url": "https://arxiv.org/abs/2602.01034"
          },
          {
            "title": "Discovering Process–Outcome Credit in Multi-Step LLM Reasoning",
            "url": "https://arxiv.org/html/2602.01034"
          },
          {
            "title": "Discovering Process-Outcome Credit in Multi-Step LLM Reasoning",
            "url": "https://arxiv.org/pdf/2602.01034"
          },
          {
            "title": "LLM Reasoning with Process Rewards for Outcome-Guided Steps",
            "url": "https://arxiv.org/pdf/2604.02341"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2509.26578"
          },
          {
            "title": "PRL: Process Reward Learning Improves LLMs' Reasoning Ability and Broadens the Reasoning Boundary",
            "url": "https://arxiv.org/pdf/2601.10201"
          },
          {
            "title": "A Survey on Feedback-based Multi-step Reasoning for Large Language   Models on Mathematics",
            "url": "https://arxiv.org/pdf/2502.14333"
          }
        ]
      },
      "Based on the search results, I found the arXiv paper you're looking for:\n\n## Paper: \"Discovering Process-Outcome Credit in Multi-Step LLM Reasoning\"\n\n**Authors:** Xiangwei Wang, Wei Wang, Ken Chen, Nanduni Nimalsiri, and Saman Halgamuge\n\n**Paper ID:** arXiv:2602.01034\n\n**Submitted:** February 1, 2026\n\n### Overview\n\nThe paper addresses how Reinforcement Learning (RL) serves as a paradigm for enhancing reasoning capabilities in Large Language Models (LLMs), yet standard outcome-based approaches often suffer from reward sparsity and inefficient credit assignment.\n\n### Key Contributions\n\nThe authors propose a novel framework with a Step-wise Marginal Information Gain (MIG) mechanism that quantifies the intrinsic value of reasoning steps against a Monotonic Historical Watermark, effectively filtering out training noise. They implement a Decoupled Masking Strategy, applying process-oriented rewards specifically to the chain-of-thought (CoT) and outcome-oriented rewards to the full completion.\n\n### Results\n\nExtensive experiments across textual and multi-modal benchmarks (e.g., MATH, Super-CLEVR) demonstrate that their approach consistently outperforms baselines such as GRPO in both sample efficiency and final accuracy, and the model exhibits superior out-of-distribution robustness with promising zero-shot transfer capabilities to unseen and challenging reasoning tasks.\n\nThe paper is available on arXiv at: https://arxiv.org/abs/2602.01034"
    ],
    "durationSeconds": 7.851454217000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "81af0537-a3a5-437c-8f48-4e370635c07a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-27T08:18:08.742Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011xQ7yqic8Vc7tHH62EU2pV`</summary>

```json
{
  "query": "arXiv 2601.18984 \"Save the Good Prefix\" VPPO PRM first error step 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29174693-7e70-4969-9975-e50b4238f9a8",
  "isSidechain": false,
  "requestId": "req_011CbSk8sjWcUPyVb1gykqQa",
  "type": "assistant",
  "uuid": "c087dec9-2596-4e94-86c8-b95e8f12917f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4EVFGrrnmZfphw1QgWbT7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 33155,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 33155,
          "cache_creation_input_tokens": 816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 816
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

_source line 25 · 2026-05-27T08:18:16.216Z_

<details><summary>↩ Tool result · `toolu_011xQ7yqic8Vc7tHH62EU2pV`</summary>

```text
Web search results for query: "arXiv 2601.18984 "Save the Good Prefix" VPPO PRM first error step 2026"

Links: [{"title":"[2601.18984] Save the Good Prefix: Precise Error Penalization via Process-Supervised RL to Enhance LLM Reasoning","url":"https://arxiv.org/abs/2601.18984"},{"title":"Save the Good Prefix: Precise Error Penalization via Process-Supervised RL to Enhance LLM Reasoning","url":"https://arxiv.org/html/2601.18984"},{"title":"Save the Good Prefix: Precise Error Penalization via Process-Supervised RL to Enhance LLM Reasoning","url":"https://arxiv.org/pdf/2601.18984"},{"title":"Beyond the First Error: Process Reward Models for Reflective Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.14391"},{"title":"LLMs cannot spot math errors, even when allowed to peek into the solution","url":"https://arxiv.org/pdf/2509.01395"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Save the Good Prefix: Precise Error Penalization via Process-Supervised RL to Enhance LLM Reasoning"

**arXiv ID:** 2601.18984 (posted January 26, 2026)

**Key Overview:**

The paper proposes Verifiable Prefix Policy Optimization (VPPO), which uses PRMs only to localize the first error during RL. Given an incorrect rollout, VPPO partitions the trajectory into a verified correct prefix and an erroneous suffix based on the first error.

**Main Problem Addressed:**

Most existing RL approaches rely on sparse outcome rewards, which fail to credit correct intermediate steps in partially successful solutions. Process reward models (PRMs) offer fine-grained step-level supervision, but their scores are often noisy and difficult to evaluate.

**Results:**

The paper demonstrates improvements across multiple reasoning benchmarks, with VPPO consistently outperforming sparse-reward RL and prior PRM-guided baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c087dec9-2596-4e94-86c8-b95e8f12917f",
  "isSidechain": false,
  "promptId": "a371b85a-1c37-4393-aeec-4935ec846310",
  "type": "user",
  "uuid": "1100fd22-2230-4db1-9cac-31b8369b9251",
  "toolUseResult": {
    "query": "arXiv 2601.18984 \"Save the Good Prefix\" VPPO PRM first error step 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GP5wrxifBu3Gj2Cp2Uvj8A",
        "content": [
          {
            "title": "[2601.18984] Save the Good Prefix: Precise Error Penalization via Process-Supervised RL to Enhance LLM Reasoning",
            "url": "https://arxiv.org/abs/2601.18984"
          },
          {
            "title": "Save the Good Prefix: Precise Error Penalization via Process-Supervised RL to Enhance LLM Reasoning",
            "url": "https://arxiv.org/html/2601.18984"
          },
          {
            "title": "Save the Good Prefix: Precise Error Penalization via Process-Supervised RL to Enhance LLM Reasoning",
            "url": "https://arxiv.org/pdf/2601.18984"
          },
          {
            "title": "Beyond the First Error: Process Reward Models for Reflective Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.14391"
          },
          {
            "title": "LLMs cannot spot math errors, even when allowed to peek into the solution",
            "url": "https://arxiv.org/pdf/2509.01395"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Title:** \"Save the Good Prefix: Precise Error Penalization via Process-Supervised RL to Enhance LLM Reasoning\"\n\n**arXiv ID:** 2601.18984 (posted January 26, 2026)\n\n**Key Overview:**\n\nThe paper proposes Verifiable Prefix Policy Optimization (VPPO), which uses PRMs only to localize the first error during RL. Given an incorrect rollout, VPPO partitions the trajectory into a verified correct prefix and an erroneous suffix based on the first error.\n\n**Main Problem Addressed:**\n\nMost existing RL approaches rely on sparse outcome rewards, which fail to credit correct intermediate steps in partially successful solutions. Process reward models (PRMs) offer fine-grained step-level supervision, but their scores are often noisy and difficult to evaluate.\n\n**Results:**\n\nThe paper demonstrates improvements across multiple reasoning benchmarks, with VPPO consistently outperforming sparse-reward RL and prior PRM-guided baselines."
    ],
    "durationSeconds": 7.469641135999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c087dec9-2596-4e94-86c8-b95e8f12917f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-27T08:18:18.856Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SpEoGyY5jVWGQvQMoaQT5S`</summary>

```json
{
  "query": "arXiv 2509.21154 \"GRPO is Secretly a Process Reward Model\" ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1100fd22-2230-4db1-9cac-31b8369b9251",
  "isSidechain": false,
  "requestId": "req_011CbSk9d6iLrkbDkmRtP7tT",
  "type": "assistant",
  "uuid": "d5f1f454-cb85-4737-ae0c-fdf6d6e41b5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018G6rCAXSHmhhD658k11CqL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 33971,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 617,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 33971,
          "cache_creation_input_tokens": 617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 617
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

_source line 27 · 2026-05-27T08:18:25.805Z_

<details><summary>↩ Tool result · `toolu_01SpEoGyY5jVWGQvQMoaQT5S`</summary>

```text
Web search results for query: "arXiv 2509.21154 "GRPO is Secretly a Process Reward Model" ICLR 2026"

Links: [{"title":"[2509.21154] GRPO is Secretly a Process Reward Model","url":"https://arxiv.org/abs/2509.21154"},{"title":"GRPO is Secretly a Process Reward Model","url":"https://arxiv.org/html/2509.21154"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.20659"},{"title":"Published as a workshop paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16158"},{"title":"GRPO is Secretly a Process Reward Model | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.21154v2"},{"title":"GRPO IS SECRETLY A PROCESS REWARD MODEL Michael Sullivan","url":"https://arxiv.org/pdf/2509.21154"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/pdf/2503.06639"},{"title":"Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner","url":"https://arxiv.org/pdf/2507.23317"}]

Based on the search results, I found the paper you're looking for:

**"GRPO is Secretly a Process Reward Model"** (arXiv:2509.21154) was submitted on September 25, 2025 and last revised on February 20, 2026.

Here are the key findings from the paper:

**Main Contribution:** The paper provides theoretical proof that the Group Relative Policy Optimization (GRPO) RL algorithm equipped with an outcome reward model (ORM) is equivalent to a process reward model (PRM)-aware RL objective equipped with a non-trivial, Monte-Carlo-based PRM.

**Key Issues Identified:** The authors identify a flaw in the GRPO objective that interacts with imbalanced process steps and rewards to hinder both exploration and exploitation under different conditions.

**Proposed Solution:** They propose a simple modification called λ-GRPO and show that LLMs tuned with λ-GRPO outperform LLMs tuned with standard GRPO on downstream reasoning tasks and reach peak performance more rapidly.

**Practical Impact:** The results show that the hidden, built-in PRM structure within vanilla GRPO can be leveraged to boost model performance without employing an explicit PRM, with negligible impact on training time and cost.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5f1f454-cb85-4737-ae0c-fdf6d6e41b5a",
  "isSidechain": false,
  "promptId": "a371b85a-1c37-4393-aeec-4935ec846310",
  "type": "user",
  "uuid": "55ce6b1c-a288-43e1-95b0-f170071478e9",
  "toolUseResult": {
    "query": "arXiv 2509.21154 \"GRPO is Secretly a Process Reward Model\" ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VToGFFs3Vjm6hor9PQAz2n",
        "content": [
          {
            "title": "[2509.21154] GRPO is Secretly a Process Reward Model",
            "url": "https://arxiv.org/abs/2509.21154"
          },
          {
            "title": "GRPO is Secretly a Process Reward Model",
            "url": "https://arxiv.org/html/2509.21154"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2604.20659"
          },
          {
            "title": "Published as a workshop paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2604.16158"
          },
          {
            "title": "GRPO is Secretly a Process Reward Model | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2509.21154v2"
          },
          {
            "title": "GRPO IS SECRETLY A PROCESS REWARD MODEL Michael Sullivan",
            "url": "https://arxiv.org/pdf/2509.21154"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification",
            "url": "https://arxiv.org/pdf/2503.06639"
          },
          {
            "title": "Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner",
            "url": "https://arxiv.org/pdf/2507.23317"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**\"GRPO is Secretly a Process Reward Model\"** (arXiv:2509.21154) was submitted on September 25, 2025 and last revised on February 20, 2026.\n\nHere are the key findings from the paper:\n\n**Main Contribution:** The paper provides theoretical proof that the Group Relative Policy Optimization (GRPO) RL algorithm equipped with an outcome reward model (ORM) is equivalent to a process reward model (PRM)-aware RL objective equipped with a non-trivial, Monte-Carlo-based PRM.\n\n**Key Issues Identified:** The authors identify a flaw in the GRPO objective that interacts with imbalanced process steps and rewards to hinder both exploration and exploitation under different conditions.\n\n**Proposed Solution:** They propose a simple modification called λ-GRPO and show that LLMs tuned with λ-GRPO outperform LLMs tuned with standard GRPO on downstream reasoning tasks and reach peak performance more rapidly.\n\n**Practical Impact:** The results show that the hidden, built-in PRM structure within vanilla GRPO can be leveraged to boost model performance without employing an explicit PRM, with negligible impact on training time and cost."
    ],
    "durationSeconds": 6.942640509999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d5f1f454-cb85-4737-ae0c-fdf6d6e41b5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-27T08:18:28.663Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JaznaSLS4RpNZy1NmiYDdz`</summary>

```json
{
  "query": "DAPO DARO baseline math RL training Qwen 2026 standard benchmark comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55ce6b1c-a288-43e1-95b0-f170071478e9",
  "isSidechain": false,
  "requestId": "req_011CbSkAKyrUhXY3spUvrAaC",
  "type": "assistant",
  "uuid": "27662fef-68f6-42d2-ad44-b8845bd5b1c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V48TfDX77utUK47A6pBn8b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 34588,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 760,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 34588,
          "cache_creation_input_tokens": 760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 760
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

_source line 29 · 2026-05-27T08:18:37.630Z_

<details><summary>↩ Tool result · `toolu_01JaznaSLS4RpNZy1NmiYDdz`</summary>

```text
Web search results for query: "DAPO DARO baseline math RL training Qwen 2026 standard benchmark comparison"

Links: [{"title":"DAPO: An Open-Source LLM Reinforcement Learning System at Scale 1ByteDance Seed","url":"https://arxiv.org/pdf/2503.14476"},{"title":"An in-depth Walkthrough of DAPO in NeMo RL — NeMo-RL","url":"https://docs.nvidia.com/nemo/rl/latest/guides/dapo.html"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"GRPO++: Tricks for Making RL Actually Work","url":"https://cameronrwolfe.substack.com/p/grpo-tricks"},{"title":"DARO: Difficulty-Aware Reweighting Policy Optimization","url":"https://arxiv.org/pdf/2510.09001"},{"title":"DAPO","url":"https://dapo-sia.github.io/"},{"title":"DAPO: An Open-Source LLM Reinforcement Learning System at Scale","url":"https://arxiv.org/html/2503.14476v1"},{"title":"GitHub - BytedTsinghua-SIA/DAPO: An Open-source RL System from ByteDance Seed and Tsinghua AIR · GitHub","url":"https://github.com/BytedTsinghua-SIA/DAPO"}]

Based on the search results, here's what I found about DAPO, DARO, and related math RL training with Qwen models:

## DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization)

DAPO is a state-of-the-art large-scale RL system that achieves 50 points on AIME 2024 using Qwen2.5-32B base model. This outperforms the previous state-of-the-art DeepSeek-R1-Zero-Qwen-32B on AIME 2024, achieving 50% accuracy with 50% less training steps.

DAPO introduces four key techniques that make large-scale LLM RL a success and is fully open-sourced.

## DARO (Difficulty-Aware Reweighting Policy Optimization)

DARO is a method that dynamically adjusts the loss contribution of each difficulty group based on the model's learning state, with extensive experiments on Qwen2.5-Math models showing that DARO outperforms four leading baselines across six math benchmarks, achieving significantly faster convergence and superior final performance. DARO achieves state-of-the-art performance on mathematical reasoning benchmarks, outperforming GRPO, LIPO, Dr. GRPO and DAPO with a much faster convergence speed.

## Benchmark Comparisons

The primary benchmark used for these comparisons is AIME 2024, where DAPO achieved 50 points compared to DeepSeek-R1-Zero's 47 points with significantly fewer training steps.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27662fef-68f6-42d2-ad44-b8845bd5b1c7",
  "isSidechain": false,
  "promptId": "a371b85a-1c37-4393-aeec-4935ec846310",
  "type": "user",
  "uuid": "40fb50ea-9b08-4155-bb27-7b904bd22cdd",
  "toolUseResult": {
    "query": "DAPO DARO baseline math RL training Qwen 2026 standard benchmark comparison",
    "results": [
      {
        "tool_use_id": "srvtoolu_017xCmZ3cBDUjxs4hK1u2Kdy",
        "content": [
          {
            "title": "DAPO: An Open-Source LLM Reinforcement Learning System at Scale 1ByteDance Seed",
            "url": "https://arxiv.org/pdf/2503.14476"
          },
          {
            "title": "An in-depth Walkthrough of DAPO in NeMo RL — NeMo-RL",
            "url": "https://docs.nvidia.com/nemo/rl/latest/guides/dapo.html"
          },
          {
            "title": "Post-Training in 2026: GRPO, DAPO, RLVR & Beyond",
            "url": "https://llm-stats.com/blog/research/post-training-techniques-2026"
          },
          {
            "title": "GRPO++: Tricks for Making RL Actually Work",
            "url": "https://cameronrwolfe.substack.com/p/grpo-tricks"
          },
          {
            "title": "DARO: Difficulty-Aware Reweighting Policy Optimization",
            "url": "https://arxiv.org/pdf/2510.09001"
          },
          {
            "title": "DAPO",
            "url": "https://dapo-sia.github.io/"
          },
          {
            "title": "DAPO: An Open-Source LLM Reinforcement Learning System at Scale",
            "url": "https://arxiv.org/html/2503.14476v1"
          },
          {
            "title": "GitHub - BytedTsinghua-SIA/DAPO: An Open-source RL System from ByteDance Seed and Tsinghua AIR · GitHub",
            "url": "https://github.com/BytedTsinghua-SIA/DAPO"
          }
        ]
      },
      "Based on the search results, here's what I found about DAPO, DARO, and related math RL training with Qwen models:\n\n## DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization)\n\nDAPO is a state-of-the-art large-scale RL system that achieves 50 points on AIME 2024 using Qwen2.5-32B base model. This outperforms the previous state-of-the-art DeepSeek-R1-Zero-Qwen-32B on AIME 2024, achieving 50% accuracy with 50% less training steps.\n\nDAPO introduces four key techniques that make large-scale LLM RL a success and is fully open-sourced.\n\n## DARO (Difficulty-Aware Reweighting Policy Optimization)\n\nDARO is a method that dynamically adjusts the loss contribution of each difficulty group based on the model's learning state, with extensive experiments on Qwen2.5-Math models showing that DARO outperforms four leading baselines across six math benchmarks, achieving significantly faster convergence and superior final performance. DARO achieves state-of-the-art performance on mathematical reasoning benchmarks, outperforming GRPO, LIPO, Dr. GRPO and DAPO with a much faster convergence speed.\n\n## Benchmark Comparisons\n\nThe primary benchmark used for these comparisons is AIME 2024, where DAPO achieved 50 points compared to DeepSeek-R1-Zero's 47 points with significantly fewer training steps."
    ],
    "durationSeconds": 8.962427907999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "27662fef-68f6-42d2-ad44-b8845bd5b1c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research context. Let me synthesize my findings and produce the assessment.  ---  【状态】: 有…",
  "leafUuid": "40fb50ea-9b08-4155-bb27-7b904bd22cdd",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Tool call

_source line 32 · 2026-05-27T08:18:40.087Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012B48TTHmHjudtDqVbCvPZn`</summary>

```json
{
  "query": "AIME 2025 benchmark math reasoning evaluation LLM 2026 standard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40fb50ea-9b08-4155-bb27-7b904bd22cdd",
  "isSidechain": false,
  "requestId": "req_011CbSkBCa9K1HrkHTWNzhiv",
  "type": "assistant",
  "uuid": "29591f0e-6c43-4072-9dc3-a3ca6f9f7274",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FuhjL897TaWSjBCU62PNYd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 859,
      "cache_read_input_tokens": 35348,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 859,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 35348,
          "cache_creation_input_tokens": 859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 859
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

_source line 33 · 2026-05-27T08:18:49.235Z_

<details><summary>↩ Tool result · `toolu_012B48TTHmHjudtDqVbCvPZn`</summary>

```text
Web search results for query: "AIME 2025 benchmark math reasoning evaluation LLM 2026 standard"

Links: [{"title":"AIME 2025 Benchmark 2026: 7 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/aime2025"},{"title":"AIME 2025 Benchmark: An Analysis of AI Math Reasoning","url":"https://intuitionlabs.ai/pdfs/aime-2025-benchmark-an-analysis-of-ai-math-reasoning.pdf"},{"title":"Proof or Bluff? Evaluating LLMs on 2025 USA Math Olympiad","url":"https://arxiv.org/pdf/2503.21934"},{"title":"AIME 2025 Benchmark: An Analysis of AI Math Reasoning | IntuitionLabs","url":"https://intuitionlabs.ai/articles/aime-2025-ai-benchmark-explained"},{"title":"Challenging the Boundaries of Reasoning: An Olympiad-Level Math Benchmark for Large Language Models","url":"https://arxiv.org/pdf/2503.21380"},{"title":"Advancing Multi-Step Mathematical Reasoning in Large ...","url":"https://ecmlpkdd-storage.s3.eu-central-1.amazonaws.com/preprints/2025/research/preprint_ecml_pkdd_2025_research_1365.pdf"},{"title":"Do LLMs Overthink Basic Math Reasoning? Benchmarking the Accuracy-Efficiency Tradeoff in Language Models","url":"https://arxiv.org/pdf/2507.04023"}]

Based on the search results, here's what I found about AIME 2025 as a benchmark for LLM math reasoning evaluation:

## AIME 2025 Benchmark Overview

The AIME 2025 examination features 15 challenging mathematics problems testing olympiad-level mathematical reasoning with integer answers from 000-999. In an AI context, AIME measures genuine problem-solving ability – analogous to an "Olympiad exam" for LLMs – far beyond simple arithmetic or formula retrieval.

## Performance Standards for 2026

Kimi K2.5 (Reasoning) by Moonshot AI currently leads with a score of 96.1% on AIME 2025. Other notable results include DeepConf achieving 99.9% accuracy on AIME 2025 by discarding low-confidence traces, all without any extra training.

## Difficulty and Evaluation Characteristics

The published difficulty ratings (Art of Problem Solving scale) confirm the challenge: problems #1–3 are relatively easy (AoPS rating ~2), but the hardest (#14–15) correspond to rating 6. Given that AIME answers must be exact, even a tiny reasoning error causes a mark to fail – so AIME is a strict metric.

## Role in LLM Evaluation

Within that category, AIME 2025 contributes 25% of the category score, so strong performance here directly affects a model's overall ranking.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29591f0e-6c43-4072-9dc3-a3ca6f9f7274",
  "isSidechain": false,
  "promptId": "a371b85a-1c37-4393-aeec-4935ec846310",
  "type": "user",
  "uuid": "40137704-a34d-4f21-b886-aa5690493cec",
  "toolUseResult": {
    "query": "AIME 2025 benchmark math reasoning evaluation LLM 2026 standard",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Qi1gL11AVaxvhyeaH2N7FF",
        "content": [
          {
            "title": "AIME 2025 Benchmark 2026: 7 LLM scores | BenchLM.ai",
            "url": "https://benchlm.ai/benchmarks/aime2025"
          },
          {
            "title": "AIME 2025 Benchmark: An Analysis of AI Math Reasoning",
            "url": "https://intuitionlabs.ai/pdfs/aime-2025-benchmark-an-analysis-of-ai-math-reasoning.pdf"
          },
          {
            "title": "Proof or Bluff? Evaluating LLMs on 2025 USA Math Olympiad",
            "url": "https://arxiv.org/pdf/2503.21934"
          },
          {
            "title": "AIME 2025 Benchmark: An Analysis of AI Math Reasoning | IntuitionLabs",
            "url": "https://intuitionlabs.ai/articles/aime-2025-ai-benchmark-explained"
          },
          {
            "title": "Challenging the Boundaries of Reasoning: An Olympiad-Level Math Benchmark for Large Language Models",
            "url": "https://arxiv.org/pdf/2503.21380"
          },
          {
            "title": "Advancing Multi-Step Mathematical Reasoning in Large ...",
            "url": "https://ecmlpkdd-storage.s3.eu-central-1.amazonaws.com/preprints/2025/research/preprint_ecml_pkdd_2025_research_1365.pdf"
          },
          {
            "title": "Do LLMs Overthink Basic Math Reasoning? Benchmarking the Accuracy-Efficiency Tradeoff in Language Models",
            "url": "https://arxiv.org/pdf/2507.04023"
          }
        ]
      },
      "Based on the search results, here's what I found about AIME 2025 as a benchmark for LLM math reasoning evaluation:\n\n## AIME 2025 Benchmark Overview\n\nThe AIME 2025 examination features 15 challenging mathematics problems testing olympiad-level mathematical reasoning with integer answers from 000-999. In an AI context, AIME measures genuine problem-solving ability – analogous to an \"Olympiad exam\" for LLMs – far beyond simple arithmetic or formula retrieval.\n\n## Performance Standards for 2026\n\nKimi K2.5 (Reasoning) by Moonshot AI currently leads with a score of 96.1% on AIME 2025. Other notable results include DeepConf achieving 99.9% accuracy on AIME 2025 by discarding low-confidence traces, all without any extra training.\n\n## Difficulty and Evaluation Characteristics\n\nThe published difficulty ratings (Art of Problem Solving scale) confirm the challenge: problems #1–3 are relatively easy (AoPS rating ~2), but the hardest (#14–15) correspond to rating 6. Given that AIME answers must be exact, even a tiny reasoning error causes a mark to fail – so AIME is a strict metric.\n\n## Role in LLM Evaluation\n\nWithin that category, AIME 2025 contributes 25% of the category score, so strong performance here directly affects a model's overall ranking."
    ],
    "durationSeconds": 9.143940772000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "29591f0e-6c43-4072-9dc3-a3ca6f9f7274",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-27T08:18:52.381Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013KjmZkY9TDjccxPHTD6558`</summary>

```json
{
  "query": "PROGRS arXiv 2604.02341 quantile regression PRM frozen outcome-conditioned centering RL training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40137704-a34d-4f21-b886-aa5690493cec",
  "isSidechain": false,
  "requestId": "req_011CbSkC49A8hA6F1ZRjxkLb",
  "type": "assistant",
  "uuid": "ae9c5961-ed4e-4e13-a8c3-42452ed195bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019uCn9hgNsFPs62sKzQnwo3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 826,
      "cache_read_input_tokens": 36207,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 36207,
          "cache_creation_input_tokens": 826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 826
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

_source line 35 · 2026-05-27T08:19:03.322Z_

<details><summary>↩ Tool result · `toolu_013KjmZkY9TDjccxPHTD6558`</summary>

```text
Web search results for query: "PROGRS arXiv 2604.02341 quantile regression PRM frozen outcome-conditioned centering RL training"

Links: [{"title":"[2604.02341] LLM Reasoning with Process Rewards for Outcome-Guided Steps","url":"https://arxiv.org/abs/2604.02341"},{"title":"LLM Reasoning with Process Rewards for Outcome-Guided Steps","url":"https://arxiv.org/html/2604.02341"},{"title":"LLM Reasoning with Process Rewards for Outcome-Guided Steps","url":"https://arxiv.org/pdf/2604.02341"},{"title":"Improving Vision-language Models with Perception-centric Process Reward Models","url":"https://arxiv.org/html/2604.24583"},{"title":"A Cram\\'er Distance perspective on Quantile Regression based   Distributional Reinforcement Learning","url":"https://arxiv.org/pdf/2110.00535"},{"title":"Distributional Reinforcement Learning with Quantile Regression","url":"https://arxiv.org/pdf/1710.10044"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"}]

I found the paper! Here's information about arXiv 2604.02341:

## LLM Reasoning with Process Rewards for Outcome-Guided Steps (PROGRS)

PROGRS is a framework that leverages PRMs while keeping outcome correctness dominant. PROGRS treats process rewards as relative preferences within outcome groups rather than absolute targets.

### Key Technical Components

Outcome-conditioned centering shifts PRM scores of incorrect trajectories to have zero mean within each prompt group, removing systematic bias while preserving informative rankings.

PROGRS combines a frozen quantile-regression PRM with a multi-scale coherence evaluator. Process-level signals are obtained from a frozen Qwen2.5-Math-PRM-7B with quantile-regression heads.

### Motivation and Results

PRM scores are often imperfectly aligned with final correctness and can reward locally fluent reasoning that still ends in an incorrect answer, which can amplify fluent failure modes and induce reward hacking when optimized as absolute rewards.

PROGRS consistently improves Pass@1 over outcome-only baselines (e.g., 74.9% vs. 69.7% on MATH-500; 59.0% vs. 52.0% on AMC-2023) and achieves stronger performance with fewer rollouts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae9c5961-ed4e-4e13-a8c3-42452ed195bb",
  "isSidechain": false,
  "promptId": "a371b85a-1c37-4393-aeec-4935ec846310",
  "type": "user",
  "uuid": "5c326483-7b64-446d-9797-f80406d4ea1f",
  "toolUseResult": {
    "query": "PROGRS arXiv 2604.02341 quantile regression PRM frozen outcome-conditioned centering RL training",
    "results": [
      {
        "tool_use_id": "srvtoolu_0194cqdHfphiowRAgHheymuo",
        "content": [
          {
            "title": "[2604.02341] LLM Reasoning with Process Rewards for Outcome-Guided Steps",
            "url": "https://arxiv.org/abs/2604.02341"
          },
          {
            "title": "LLM Reasoning with Process Rewards for Outcome-Guided Steps",
            "url": "https://arxiv.org/html/2604.02341"
          },
          {
            "title": "LLM Reasoning with Process Rewards for Outcome-Guided Steps",
            "url": "https://arxiv.org/pdf/2604.02341"
          },
          {
            "title": "Improving Vision-language Models with Perception-centric Process Reward Models",
            "url": "https://arxiv.org/html/2604.24583"
          },
          {
            "title": "A Cram\\'er Distance perspective on Quantile Regression based   Distributional Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2110.00535"
          },
          {
            "title": "Distributional Reinforcement Learning with Quantile Regression",
            "url": "https://arxiv.org/pdf/1710.10044"
          },
          {
            "title": "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport",
            "url": "https://arxiv.org/html/2605.06785"
          }
        ]
      },
      "I found the paper! Here's information about arXiv 2604.02341:\n\n## LLM Reasoning with Process Rewards for Outcome-Guided Steps (PROGRS)\n\nPROGRS is a framework that leverages PRMs while keeping outcome correctness dominant. PROGRS treats process rewards as relative preferences within outcome groups rather than absolute targets.\n\n### Key Technical Components\n\nOutcome-conditioned centering shifts PRM scores of incorrect trajectories to have zero mean within each prompt group, removing systematic bias while preserving informative rankings.\n\nPROGRS combines a frozen quantile-regression PRM with a multi-scale coherence evaluator. Process-level signals are obtained from a frozen Qwen2.5-Math-PRM-7B with quantile-regression heads.\n\n### Motivation and Results\n\nPRM scores are often imperfectly aligned with final correctness and can reward locally fluent reasoning that still ends in an incorrect answer, which can amplify fluent failure modes and induce reward hacking when optimized as absolute rewards.\n\nPROGRS consistently improves Pass@1 over outcome-only baselines (e.g., 74.9% vs. 69.7% on MATH-500; 59.0% vs. 52.0% on AMC-2023) and achieves stronger performance with fewer rollouts."
    ],
    "durationSeconds": 10.93593383899999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ae9c5961-ed4e-4e13-a8c3-42452ed195bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-27T08:19:03.326Z_

```json
{
  "parentUuid": "5c326483-7b64-446d-9797-f80406d4ea1f",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "cd5fc4aa-da89-4fd0-8547-1070eede078f",
  "timestamp": "2026-05-27T08:19:03.326Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-27T08:20:25.520Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've now verified the key claims from both workers. Let me synthesize:

1. **"Discovering Process-Outcome Credit" (arXiv 2602.01034)** - CONFIRMED. Paper exists, does Step-wise Marginal Information Gain + Decoupled Masking for process-outcome credit mixing. Discovery agent's characterization is accurate.

2. **VPPO / "Save the Good Prefix" (arXiv 2601.18984)** - CONFIRMED. Paper exists, uses PRM to localize first error and partition trajectory into correct prefix + erroneous suffix. 

3. **"GRPO is Secretly a PRM" (arXiv 2509.21154, ICLR 2026)** - CONFIRMED. Paper exists and proves GRPO+ORM is equivalent to PRM-aware RL under identical-prefix conditions. The timeline shows submission in September 2025 with a February 2026 revision, and there's a reference to ICLR 2026 publication, though I'm seeing some inconsistency in the search results pointing to different papers, so I should verify the exact arxiv version more carefully.

Now I'm noticing the search results show "GRPO IS SECRETLY A PROCESS REWARD MODEL" from arxiv 2509.21154 proposing λ-GRPO, which might actually be the same as the GRPO-λ paper referenced in the proposal. Let me trace whether these are the same work or distinct papers.

The key finding is that arxiv 2509.21154 demonstrates GRPO with an outcome reward model implicitly functions as a process reward model, so citing this paper to support the proposal's approach is definitely warranted.

For DAPO, I've confirmed it's a standard baseline achieving 50 points on AIME 2024 and is widely adopted and open-sourced by ByteDance.

AIME 2025 is also confirmed as a standard benchmark used across multiple research groups like BenchLM and IntuitionLabs.

PROGRS uses a frozen Qwen2.5-Math-PRM-7B with quantile-regression heads for process-level signals, which aligns with both agents' descriptions.

All the papers the discovery agent referenced check out, the remedy agent's baseline and benchmark claims are accurate, and the technical details about PROGRS match what I've verified.

Now I'm evaluating which suggestions to incorporate. The discovery agent's point about PROGRS already using calibrated PRM in RL is critical—it directly challenges the novelty claim, so I need to address this head-on rather than glossing over it. The reframing from "engineering combination" to a "principled bias-variance tradeoff framework" is a meaningful upgrade that grounds the work more rigorously. The three additional papers they flagged are all real and directly relevant to the proposal. I'm also considering their point about upgrading the significance framing.

From the remedy agent, I'm adopting the missing baselines—both DAPO and PROGRS are essential comparisons. The benchmark additions of AIME 2025 and MinervaMath are standard expectations. The reward hacking metrics are well-defined and worth including. The ablation completeness point is also valid, though I'll be selective about scope.

I'm taking the multi-seed approach with bootstrap confidence intervals and the 1.7B model validation. Compute fairness is straightforward to add, and the cross-family PRM validation is a low-cost experiment that strengthens the claims.

Now I'm assessing the probability of acceptance. The novelty sits at a medium-to-strong level—the bias-variance framing and per-step gating mechanism clearly differentiate this from PROGRS, even though both work in the calibrated PRM space. The core contribution is real, but I need to be precise about where the gap lies.

The significance is also medium-to-strong: miscalibrated PRMs causing reward hacking is a genuine problem, and framing this as principled degradation under verifier uncertainty adds conceptual weight. With all the experimental additions—DAPO and PROGRS baselines, AIME 2025 benchmarks, reward hacking metrics, expanded ablations, statistical significance testing, compute fairness analysis, and cross-family validation—the experimental design becomes solid. Technical soundness moves from medium toward strong after these fixes.

This puts the ceiling around 45-50% and the floor at 30-35%, so I'm looking at a 30-45% range for this first iteration.

Now I need to write out the updated proposal while being extremely careful to preserve every original citation and integrate the new ones properly. Let me first catalog all the references I'm working with. I'm reviewing the key references section, which covers recent work on process reward models, credit assignment in reasoning, uncertainty calibration, and theoretical perspectives on step-by-step verification in LLM reasoning tasks.

Now I'm thinking through the core conceptual shifts I want to make in the proposal—reframing the novelty around how uncertainty and the bias-variance tradeoff in credit assignment can improve process reward modeling, rather than just focusing on calibration alone.

I also want to add the missing related works and make sure I'm clearly differentiating from PROGRS by highlighting that my approach uses per-step gating while they use trajectory-level centering.

On the experimental side, I need to significantly expand the evaluation—adding stronger baselines like DAPO and PROGRS, new benchmarks like AIME 2025 and MinervaMath, and defining concrete metrics for reward hacking like per-step uncertainty-conditioned accuracy and reward hacking rates.

I'm also planning a more comprehensive ablation study that tests boundary cases and compares hard versus soft gating strategies, plus I'll add bootstrap confidence intervals across multiple seeds and include fairness reporting on compute costs.

Now I need to update the resource estimate and decide whether to continue iterating. Both reviewers found substantial improvements—not direction-changing, but meaningful refinements to framing, baselines, and metrics. I think one more round of review would catch any issues I introduce while making these changes, so I'll continue.

Before I write the full output, I want to clarify the GRPO-λ situation from that recent paper showing GRPO functions as a process reward model. I'm uncertain whether these are the same paper or two different ones—the arXiv ID for "GRPO-λ: Credit Assignment Improves LLM Reasoning" isn't explicitly stated in the proposal. Rather than try to resolve this ambiguity, I'll include both references since the "GRPO is Secretly a Process Reward Model" paper makes an important point about GRPO's implicit process credit that's worth discussing separately regardless.

Now for the probability assessment: the per-step uncertainty-driven bias-variance interpolation feels genuinely novel and distinct from PROGRS's trajectory-level centering, though it's more of an incremental-to-moderate advance. The work addresses a real problem with broader implications, and while the technical soundness improves significantly after addressing the experimental issues, there's still execution risk. My estimate for the idea ceiling is around 45-50%, and with the improved experiments I'd place it in the 32-45% range with a median of 38%. For AAAI 2026 specifically, the positioning at the intersection of two active research directions is strong, the novelty angle around PRM uncertainty driving the bias-variance tradeoff is principled, and the experimental plan is comprehensive—but the main vulnerability remains whether the empirical gains will actually materialize.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd5fc4aa-da89-4fd0-8547-1070eede078f",
  "isSidechain": false,
  "requestId": "req_011CbSkD6SrD8CXwXw9jyH7Z",
  "type": "assistant",
  "uuid": "99a1885e-fcd4-4431-93b2-a236bc2a998f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QucJ9jcUQnr3tEPp7zXqUV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 37033,
      "output_tokens": 10783,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 828,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10783,
          "cache_read_input_tokens": 37033,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 828
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

_source line 38 · 2026-05-27T08:22:50.026Z_

所有关键 worker 建议已验证完毕。现在我来整合并输出第 1 轮迭代结果。

【阶段】: 迭代第 1 轮

【交叉验证调研】:
1. **"Discovering Process-Outcome Credit" (arXiv 2602.01034)** — 已验证存在。确认为 Step-wise Marginal Information Gain + Decoupled Masking 做 process-outcome credit 混合分配，不基于 PRM uncertainty。发掘 agent 描述准确。
2. **VPPO / "Save the Good Prefix" (arXiv 2601.18984)** — 已验证存在。确认用 PRM 定位 first error，将轨迹分为 correct prefix + erroneous suffix。发掘 agent 描述准确。
3. **"GRPO is Secretly a Process Reward Model" (arXiv 2509.21154)** — 已验证存在，ICLR 2026。证明 GRPO+ORM 在 shared-prefix 条件下等价于 PRM-aware RL，并提出 λ-GRPO。注意：此论文与原始 proposal 的 "GRPO-λ" 引用可能指同一工作（都提出 λ 参数化的 GRPO 变体），需在 proposal 中澄清引用关系。
4. **DAPO 作为标准 baseline** — 已验证。DAPO 在 AIME 2024 上达 50 分，被 ByteDance 开源，已成为 2026 年 math RL 论文的标准对比方法。补救 agent 建议成立。
5. **AIME 2025 作为标准 benchmark** — 已验证。BenchLM.ai、IntuitionLabs 均采用 AIME 2025 作为评测标准。补救 agent 建议成立。
6. **PROGRS 使用 frozen quantile-regression PRM** — 已验证。确认 PROGRS 使用 frozen Qwen2.5-Math-PRM-7B + quantile-regression heads + outcome-conditioned centering。这是 UGCA 最近的竞争者，两位 worker 均正确识别。

【发掘 agent 有效建议采纳】:
1. **Trivial alternative 论证（发掘点 1）** — **已验证，采纳**。PROGRS 确实已使用 calibrated PRM 进入 RL，但其 centering 是 trajectory-level 固定规则。需论证 per-step gating 的必要性源于 PRM calibration quality 在不同 step types 间的 heterogeneity。加入"per-step heterogeneity"论证 + "全局 clipping" 作为 ablation baseline。
2. **Novelty 锐化为 bias-variance tradeoff（发掘点 2）** — **已验证，采纳**。这个 reframing 有坚实基础：process credit = low-variance but PRM-bias-dependent, outcome credit = unbiased but high-variance, α_i 在 bias-variance frontier 上做 per-step optimal interpolation。Jia et al. (ICML 2025) 的 statistical equivalence 为 "outcome credit is unbiased" 提供理论支持。将 novelty 从 "bridging calibration and RL" 升级为 "uncertainty-driven bias-variance tradeoff"。
3. **Related work 补充（发掘点 3）** — **三篇均已验证，采纳**。arXiv 2602.01034、arXiv 2601.18984、arXiv 2509.21154 均存在且与 UGCA 高度相关，必须纳入 related work 并做差异化论述。
4. **Significance 提升（发掘点 4）** — **逻辑合理，部分采纳**。"principled degradation under verifier uncertainty" 作为 discussion-level 延伸合理，但不可 overclaim。在 discussion 中 briefly 提及 generalization potential，保持 math reasoning 作为核心 testbed。
5. **理论连接强化（发掘点 5）** — **已验证，采纳**。bias-variance tradeoff 形式化（appendix 中简化假设下推导 α 的 optimal form）是从 "theoretically motivated" 到 "theoretically grounded" 的关键跃迁。采纳建议增加 appendix 推导。

【补救 agent 有效建议采纳】:
1. **DAPO + PROGRS baseline（缺陷 1）** — **已验证，采纳**。DAPO 是当前标准 baseline；PROGRS 是最接近的 concurrent work，必须直接对比。增加约 600 H100-hours。
2. **AIME 2025 + MinervaMath benchmark（缺陷 2）** — **已验证，采纳**。AIME 2025 已成为标准。MinervaMath 是 PROGRS 采用的 benchmark，纳入可增强与 PROGRS 的可比性。评测开销可忽略。
3. **Reward hacking 量化指标（缺陷 3）** — **已验证，采纳**。PAG、per-step uncertainty-conditioned accuracy、reward hacking rate 三个指标均有文献先例，定义清晰。
4. **Ablation 扩展（缺陷 4）** — **部分采纳**。(a) Boundary cases α≡1 / α≡0 — 采纳，这同时验证了 bias-variance framing；(b) Hard vs soft gating — 采纳，关键 ablation；(c) Calibration method ablation（quantile regression vs conditional OT）— 如 Distributional PRM 代码开源则做对比，否则仅讨论，标注 future work；(d) Calibrated vs uncalibrated uncertainty — 采纳，隔离 calibration 贡献。
5. **Multi-seed / 统计显著性（缺陷 5）** — **采纳折衷方案**。1.7B 全部 3 seeds；8B top configs 3 seeds + evaluation-level bootstrap CI。
6. **Compute fairness报告（缺陷 6）** — **采纳**。Wall-clock 对比 + accuracy-vs-compute Pareto curve，零额外实验开销。
7. **Cross-family PRM 验证（缺陷 7）** — **已验证，采纳**。Park et al. (NeurIPS 2025) 确实发现 OOD calibration error 增大。Qwen2.5-PRM → Qwen3 policy 的 distribution shift 需验证。低成本实验。

【本轮 proposal 主要变更】:

*Idea 层面变更：*
- 核心 novelty 从 "bridging PRM calibration and RL credit assignment" 重构为 "uncertainty-driven bias-variance tradeoff in per-step credit assignment"
- 增加 per-step PRM calibration heterogeneity 论证，回应 trivial alternative 威胁
- 明确与 PROGRS 的差异化：trajectory-level deterministic centering vs. per-step uncertainty-driven gating
- 新增 3 篇 related work 并做差异化论述：arXiv 2602.01034（intrinsic information gain vs. PRM uncertainty）、arXiv 2601.18984（binary first-error detection vs. continuous gating）、arXiv 2509.21154（uniform implicit process credit vs. adaptive gating）
- 增加 bias-variance tradeoff 的 formal argument（附录推导计划）
- Discussion 增加 "principled degradation under verifier uncertainty" 的 broader significance

*实验层面变更：*
- Baselines 增加 DAPO 和 PROGRS
- Benchmarks 增加 AIME 2025 和 MinervaMath
- 定义 3 个 reward hacking 量化指标
- Ablation 扩展：boundary cases、hard vs soft gating、calibrated vs uncalibrated uncertainty
- 增加 multi-seed 方案和 bootstrap CI
- 增加 compute fairness 报告（wall-clock + Pareto curve）
- 增加 cross-family PRM calibration 验证实验
- 资源预算更新至 ~2700 H100-hours

【idea 质量评估】: Novelty=中-强 Significance=中-强 → idea 天花板约 48%
- Novelty 之所以是"中-强"而非"强"：核心贡献仍然是已有 building blocks 的原则性组合（calibrated PRM + PURE/GRPO 插值），虽然 bias-variance framing 增加了深度，但不是一个全新的 paradigm shift。PROGRS 的存在部分侵蚀了 "first to use calibrated PRM in RL" 的 claim，尽管 per-step gating 机制确实有差异化。
- Significance 之所以是"中-强"：reward hacking 问题是 real 且 impactful 的，但 UGCA 的改进幅度是否足够大存在不确定性——如果 empirical gains 仅 1-2%，significance 会被打折。

【实验完备性评估】: Technical Soundness=中-强 → 地板基本补好
- 补充 DAPO/PROGRS baseline、AIME 2025、reward hacking 指标、扩展 ablation 后，实验设计在该领域属于 above-average completeness。
- 剩余风险：cross-family PRM 的 distribution shift 可能导致 calibration 退化，需要实验验证。

【当前概率估计】: [32% - 45%] 中位 38%

【决策】: 继续

【决策理由】: 第 1 轮产生了大量实质性改进（novelty reframing、3 篇 related work 补充、5 个 baseline/benchmark 增补、reward hacking 指标定义、ablation 扩展）。但更新后的 proposal 尚未经 worker 审视，可能存在引入新问题或遗漏的风险。第 2 轮将检验更新版本是否 solid，预期收敛。

【引用清单核对】（重写前逐一列出原始 proposal 中的所有引用标记）：
1. PURE (NeurIPS 2025) — ✓
2. GRPO-λ (arXiv Oct 2025) — ✓
3. PROGRS (arXiv Apr 2026) — ✓
4. UCAS (arXiv Oct 2025) — ✓
5. Distributional PRM (arXiv May 2026, arXiv 2605.06785) — ✓
6. PathFinder-PRM (arXiv May 2025) — ✓
7. PRPO (arXiv Jan 2026) — ✓
8. Uncertainty-Aware Reward Discounting (arXiv Apr 2026) — ✓
9. TP-GRPO (arXiv Jul 2025) — ✓
10. PRIME (arXiv Feb 2025) — ✓
11. Park et al. quantile regression (NeurIPS 2025) — ✓
12. Jia et al. (ICML 2025) — ✓
13. PRL (arXiv 2026) — ✓
14. Qwen2.5-Math-PRM-7B, Qwen3-8B, Qwen3-1.7B — ✓
15. MATH-500, AMC23, AIME24, OlympiadBench — ✓
16. Key References 列表 11 篇 — ✓
新增引用：arXiv 2602.01034, arXiv 2601.18984, arXiv 2509.21154 (ICLR 2026), DAPO, AIME 2025, MinervaMath, arXiv 2603.06621

【下一轮 proposal（纯净版，将原样传给 worker）】:
---
# Uncertainty-Gated Credit Assignment for Process-Supervised Mathematical Reasoning RL

## Core Problem

Current methods for integrating process reward models into RL training (PURE, GRPO-λ, PRL, PRPO, PROGRS) treat all PRM step-level scores as equally trustworthy or apply only trajectory-level corrections, yet PRMs are demonstrably miscalibrated—overestimating success probabilities on uncertain steps—leading to reward hacking where the policy exploits unreliable PRM signals rather than genuinely improving reasoning. Critically, PRM calibration quality is heterogeneous across step types: computational steps tend to be well-calibrated while conceptual reasoning steps exhibit significantly wider confidence intervals. This per-step heterogeneity means that global or trajectory-level corrections (e.g., outcome-conditioned centering) cannot fully address the problem—adaptive per-step treatment is necessary.

## Research Opportunity

PRM calibration methods have matured rapidly (quantile regression [Park et al., NeurIPS 2025], conditional optimal transport [arXiv 2605.06785]) but are applied exclusively to test-time scaling (best-of-N, instance-adaptive search). No work uses PRM uncertainty to perform per-step adaptive credit assignment during RL training. PROGRS (arXiv Apr 2026) brings a calibrated PRM into RL training but applies a fixed trajectory-level outcome-conditioned centering rule, not per-step uncertainty gating. Meanwhile, Jia et al. [ICML 2025] proved outcome supervision is statistically no harder than process supervision—suggesting the empirical gap is algorithmic, and that falling back to outcome credit when process credit is unreliable is principled. This creates a clear opportunity: an uncertainty-driven bias-variance tradeoff in credit assignment, where per-step PRM confidence determines the optimal interpolation between low-variance (but potentially biased) process credit and unbiased (but high-variance) outcome credit. The building blocks (calibrated PRMs, GRPO/PURE training pipelines, math reasoning benchmarks) all exist, making a 2-month implementation feasible for AAAI 2027 (deadline: July 28, 2026).

## Research Landscape

**Process-aware RL credit assignment.** PURE (NeurIPS 2025) replaces summation-form with min-form credit assignment, achieving 82.6% on MATH-500 and 82.5% on AMC23 with Qwen2.5-Math-7B but assumes PRM scores are reliable. GRPO-λ (arXiv Oct 2025) adds eligibility traces to GRPO, improving average math scores by 3–4.5 points on 7B models but also trusts PRM outputs uniformly. PRPO (arXiv Jan 2026) aligns process and outcome advantages via location-parameter shift on Qwen2.5-Math-1.5B (61.2→64.4% MATH-500) but uses fixed structural alignment, not adaptive per-step weighting. PRL (arXiv 2026) improves reasoning ability through process reward learning but does not condition on PRM reliability.

**Calibrated PRM in RL (trajectory-level).** PROGRS (arXiv Apr 2026) uses outcome-conditioned centering with a frozen quantile-regression PRM (74.9% on MATH-500 vs 69.7% DAPO baseline), achieving stronger performance with fewer rollouts. However, PROGRS applies a deterministic centering rule at the trajectory level—shifting incorrect-trajectory PRM scores to zero mean within each prompt group—without using PRM uncertainty information at the per-step level. This addresses systematic PRM bias but cannot capture the per-step heterogeneity of calibration quality.

**Process-outcome credit mixing (non-uncertainty-based).** "Discovering Process-Outcome Credit in Multi-Step LLM Reasoning" (arXiv 2602.01034) proposes Step-wise Marginal Information Gain + Decoupled Masking for process-outcome credit mixing, but relies on Monte Carlo estimation of intrinsic information gain rather than PRM calibration uncertainty—computationally heavier and subject to higher estimation variance. "Save the Good Prefix" / VPPO (arXiv 2601.18984) uses PRM to localize the first error step and applies targeted penalization to the erroneous suffix—a binary (hard) form of per-step differentiation that cannot gracefully handle PRM uncertainty on ambiguous steps.

**Implicit process credit in GRPO.** Sullivan et al. (arXiv 2509.21154, ICLR 2026) prove that GRPO + ORM under shared-prefix conditions is equivalent to PRM-aware RL with a Monte-Carlo-based implicit PRM, and propose λ-GRPO. This implies vanilla GRPO already carries implicit process credit—but this credit is uniform across steps, not adaptive to PRM confidence. UGCA's explicit uncertainty-gated interpolation provides the missing adaptivity.

**PRM calibration and uncertainty.** Park et al. (NeurIPS 2025) introduce quantile-regression calibration for PRMs. The Distributional PRM (arXiv 2605.06785, May 2026) achieves state-of-the-art calibration via conditional optimal transport but explicitly targets only test-time scaling. PathFinder-PRM (arXiv May 2025) achieves 67.7 PRMScore on PRMBench with error-type-aware scoring but does not feed uncertainty into RL credit assignment.

**Uncertainty in RL rewards (non-PRM).** UCAS (arXiv Oct 2025) modulates advantages via the policy model's own logit uncertainty—fundamentally different from PRM verifier uncertainty. Uncertainty-Aware Reward Discounting (arXiv Apr 2026) uses ensemble disagreement to mitigate reward hacking in RLHF but targets general preference learning, not process-outcome interpolation for math. TP-GRPO (arXiv Jul 2025) introduces capability-adaptive rewards with generative PRM at the thought level using intrinsic signals, not PRM calibration. PRIME (arXiv Feb 2025) enables online PRM updates through implicit process rewards but uses uniform trust in PRM signals.

**Gap summary.** Thorough concurrent-work search (May 2026) confirms the specific gap: using per-step PRM calibration confidence to drive adaptive interpolation between process and outcome credit during RL training—framed as an uncertainty-driven bias-variance tradeoff—remains unaddressed.

## Proposed Approach

We propose Uncertainty-Gated Credit Assignment (UGCA), grounded in a bias-variance tradeoff perspective on credit assignment. Process credit (PURE-style min-form advantage A^min) provides dense, low-variance step-level signal but is biased when the PRM is miscalibrated. Outcome credit (GRPO group-relative advantage A^GRPO) is unbiased (based on verifiable correctness) but high-variance (sparse, trajectory-level). The optimal per-step interpolation depends on local PRM reliability.

Concretely, we equip the off-the-shelf Qwen2.5-Math-PRM-7B with calibrated confidence intervals via quantile regression (adapting open-source code from Park et al., NeurIPS 2025), then define a per-step gating coefficient α_i = σ(−(w_i − τ)/β) based on each step's confidence-interval width w_i. The advantage at step i is A_i = α_i · A^min_i + (1 − α_i) · A^GRPO_i: high-confidence PRM steps (small w_i, high α) lean on low-variance process credit, while uncertain steps (large w_i, low α) gracefully degrade to unbiased outcome credit.

This interpolation is theoretically grounded by two results: (1) Jia et al. (ICML 2025) prove outcome supervision is statistically no harder than process supervision, ensuring the degradation to outcome credit preserves learning guarantees; (2) under simplifying assumptions (Gaussian noise on PRM scores with variance proportional to w_i²), the MSE-optimal interpolation weight takes a sigmoid-like form in w_i, providing a prescriptive justification for the gating function (formal derivation in appendix).

We train Qwen3-8B and Qwen3-1.7B on the MATH training set (8K prompts) using this modified GRPO objective atop the PURE codebase (with veRL framework), with the calibrated PRM frozen throughout. A cross-family PRM validation experiment verifies that quantile calibration quality (ECE, Brier score) does not significantly degrade when applied to Qwen3 rollouts versus Qwen2.5 rollouts.

## Experimental Design

**Baselines.** GRPO (outcome-only), DAPO (outcome-only with Clip-Higher + Dynamic Sampling), PURE (min-form process credit), GRPO-λ / λ-GRPO (eligibility-trace credit), PROGRS (trajectory-level calibrated PRM centering). All baselines re-implemented on the same Qwen3-8B and Qwen3-1.7B models under identical training budgets.

**Benchmarks.** MATH-500, AMC23, AIME 2024, AIME 2025, OlympiadBench, MinervaMath. Pass@1 as primary metric.

**Reward hacking quantification.**
- PRM-Accuracy Gap (PAG): periodic sampling of rollouts during training to compute the gap between mean PRM score and ground-truth pass rate, plotted as overoptimization curves.
- Per-step uncertainty-conditioned accuracy: steps binned by PRM confidence-interval width (5 quantile bins), reporting per-bin step correctness.
- Reward hacking rate: proportion of trajectories where PRM score exceeds threshold but final answer is incorrect, compared across methods at matched training steps.

**Ablation studies (on Qwen3-1.7B).**
- Boundary cases: α≡1 (pure process credit / PURE) and α≡0 (pure outcome credit / GRPO), confirming interpolation outperforms both extremes.
- Hard vs. soft gating: binary threshold gating (α=1 if w<τ else α=0) vs. sigmoid gating, demonstrating soft gating's advantage on ambiguous steps.
- Calibrated vs. uncalibrated uncertainty: using raw (uncalibrated) PRM score variance as uncertainty proxy vs. calibrated confidence-interval width, isolating calibration's contribution.
- Hyperparameter sensitivity: gating threshold τ, temperature β, quantile level.

**Statistical rigor.** 1.7B experiments: 3 random seeds, report mean ± std. 8B experiments: top 2 configs × 3 seeds + evaluation-level bootstrap confidence intervals (1000 resamples on each benchmark).

**Compute fairness.** Report per-method training wall-clock time and FLOPs. PRM quantile calibration cost reported separately as one-time overhead. Accuracy-vs-compute Pareto curves included.

**Cross-family PRM validation.** Compute ECE and Brier score of calibrated Qwen2.5-Math-PRM-7B on Qwen3-8B initial rollouts vs. Qwen2.5 rollouts. If significant degradation detected, perform additional quantile calibration fine-tuning on Qwen3-generated data.

## Broader Significance

Beyond math reasoning, UGCA addresses a general question: how should RL training gracefully degrade when the verifier is imperfect? In code generation (compiler verifiers uncertain about runtime behavior), scientific reasoning (PRMs uncertain about domain-specific steps), and agentic tasks (partially observable environment feedback), verifier uncertainty is pervasive. UGCA's framework—calibrate verifier confidence, then gate credit assignment by uncertainty—provides a principled template. We position math reasoning as a clean testbed where process verifier uncertainty is measurable and calibratable, with generalization to other domains as future work.

## Key References

- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (NeurIPS 2025)
- GRPO-λ: Credit Assignment Improves LLM Reasoning (arXiv 2025)
- GRPO is Secretly a Process Reward Model (arXiv 2509.21154, ICLR 2026)
- LLM Reasoning with Process Rewards for Outcome-Guided Steps [PROGRS] (arXiv 2026)
- Discovering Process-Outcome Credit in Multi-Step LLM Reasoning (arXiv 2602.01034)
- Save the Good Prefix: Precise Error Penalization via Process-Supervised RL [VPPO] (arXiv 2601.18984)
- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (NeurIPS 2025)
- Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport (arXiv 2605.06785, 2026)
- Do We Need to Verify Step by Step? Rethinking Process Supervision from a Theoretical Perspective (ICML 2025)
- Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning [UCAS] (arXiv 2025)
- PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization (arXiv 2026)
- PRL: Process Reward Learning Improves LLMs' Reasoning Ability and Broadens the Reasoning Boundary (arXiv 2026)
- Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision [PathFinder-PRM] (arXiv 2025)
- Process Reinforcement through Implicit Rewards [PRIME] (arXiv 2025)
- Uncertainty-Aware Reward Discounting (arXiv Apr 2026)
- Reward Under Attack: Reward Hacking of Process Reward Models (arXiv 2603.06621)

## Resource Estimate

- **GPU compute**: ~2700 H100-hours (PRM quantile calibration: 100h; cross-family validation: 20h; Qwen3-1.7B ablations ×12 configs × 3 seeds: 720h; Qwen3-8B main comparison ×6 configs, top 2 × 3 seeds + rest × 1 seed: 1600h; DAPO/PROGRS baseline runs: 200h; evaluation + reward-hacking diagnostics: 60h)
- **Timeline**: 8 weeks (wk1–2: PRM quantile-regression calibration + cross-family validation + PURE/veRL codebase integration; wk3–4: 1.7B full ablation sweep including boundary cases, hard/soft gating, calibrated/uncalibrated; wk5–6: 8B comparison runs vs PURE/GRPO/GRPO-λ/DAPO/PROGRS; wk7: reward-hacking analysis with PAG curves, per-step uncertainty visualization, compute Pareto curves; wk8: paper writing and AAAI submission)
- **Estimated GPU cost**: ~$6,750 (H100 spot at ~$2.50/GPU-hr)
- **Human-in-loop variant**: 6 weeks (Claude accelerates codebase integration, ablation scripting, analysis, drafting), Claude API cost ~$400
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99a1885e-fcd4-4431-93b2-a236bc2a998f",
  "isSidechain": false,
  "requestId": "req_011CbSkD6SrD8CXwXw9jyH7Z",
  "type": "assistant",
  "uuid": "fa9448b2-2de9-403d-b220-2753c1ccdba7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QucJ9jcUQnr3tEPp7zXqUV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 37033,
      "output_tokens": 10783,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 828,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10783,
          "cache_read_input_tokens": 37033,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 828
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

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research context. Let me synthesize my findings and produce the assessment.  ---  【状态】: 有…",
  "leafUuid": "fa9448b2-2de9-403d-b220-2753c1ccdba7",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research context. Let me synthesize my findings and produce the assessment.  ---  【状态】: 有…",
  "leafUuid": "fa9448b2-2de9-403d-b220-2753c1ccdba7",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 44 · 2026-05-27T08:29:26.471Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:29:26.471Z",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "content": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nNow I have sufficient research context. Let me synthesize my findings and produce the assessment.\n\n---\n\n【状态】: 有发掘空间\n\n【前置调研发现】\n- **PROGRS** (arXiv 2604.02341, Apr 2026): 最直接的竞争者。使用 outcome-conditioned centering 将校准 PRM 引入 RL 训练，但只做 trajectory-level 的固定校正规则，不使用 per-step 不确定性信息。与 UGCA 的差异确实在于 per-step adaptive gating 的缺失。\n- **Distributional PRM** (arXiv 2605.06785, May 2026): 通过 conditional optimal transport 实现 SOTA PRM 校准，但明确只 target test-time scaling (best-of-N, instance-adaptive search)，未应用于 RL 训练。这为 UGCA 提供了更强的校准工具（可替换 quantile regression），且论文本身确认了 gap。\n- **Park et al. \"Know What You Don't Know\"** (NeurIPS 2025): Quantile regression PRM 校准的原始工作，输出 confidence bounds。明确用于 instance-adaptive scaling，未用于 RL credit assignment。UGCA 对其方法的迁移使用是合理的。\n- **Jia et al. \"Do We Need to Verify Step by Step?\"** (ICML 2025): 证明 outcome supervision 统计上不比 process supervision 更难。这为 UGCA 的 \"uncertain 时退化到 outcome credit\" 提供了理论支撑——退化是 principled 的，不损失学习保证。\n- **Discovering Process-Outcome Credit** (arXiv 2602.01034, Feb 2026): 用 Step-wise Marginal Information Gain + Decoupled Masking 做 process-outcome credit mixing，但依赖 Monte Carlo estimation of intrinsic information gain 而非 PRM 校准不确定性。方法论不同，但 motivating problem 高度重叠。\n- **ConfClip** (arXiv 2509.17730, Sep 2025): 用模型自身 confidence 来加权 reward，但用的是 policy model 的 confidence 而非 verifier 的校准不确定性，且不做 process-outcome 插值。\n- **Reward Under Attack** (arXiv 2603.06621, Feb 2026): 证明当前 SOTA PRM 是 systematically exploitable 的 \"fluency detectors\"，强化了 UGCA 的 motivation（PRM 不可盲目信任）。\n- **PURE** (NeurIPS 2025): Min-form credit assignment，识别了 summation-form 导致的 reward hacking，但前提仍然是 PRM 分数可靠。\n- **GRPO-λ / λ-GRPO** (arXiv 2510.00194 / ICLR 2026): Eligibility trace / implicit PRM credit，均匀信任 PRM 信号，没有 per-step adaptive weighting。\n\n- **调研总结**: 当前领域有两条平行发展线：(1) PRM 校准技术（quantile regression, distributional OT）快速成熟但仅用于 test-time scaling；(2) Process-aware RL credit assignment 方法（PURE, GRPO-λ, PROGRS）迅速涌现但均匀或固定地信任 PRM 信号。将两者连接——用 PRM 校准不确定性驱动 RL 中的 per-step adaptive credit assignment——确实是一个被确认的 gap。这个 gap 不是 trivial 的，因为需要解决多个非平凡问题（cross-family 校准迁移、gating 函数设计、与 GRPO/PURE 训练框架的集成）。\n\n---\n\n【发掘点 1】\n- 维度: 核心 claim 强化\n- 内容: Proposal 的核心 framing 是 \"bias-variance tradeoff\"，但当前表述中 bias 的来源和量化不够锐利。具体而言：proposal 说 \"process credit is biased when PRM is miscalibrated\"，但 PURE 的 min-form credit 的 bias 不仅来自 PRM miscalibration，还来自 min-form 本身的保守性（min 操作是一种下界估计，对大多数正确 trajectory 也存在系统性低估）。建议将 bias 分解为两个来源：(a) PRM miscalibration bias（PRM 分数偏离真实 step correctness probability），(b) aggregation bias（min-form 或 sum-form 的结构性偏差）。UGCA 的 uncertainty gating 主要解决 (a)，但应明确承认 (b) 的存在并说明为什么 (b) 不是 UGCA 要解决的问题（或为什么解决 (a) 后 (b) 的影响可控）。这种精细的 bias 分解会让 reviewer 觉得作者对问题理解深刻，而非笼统地说 \"bias\"。\n- 价值: 强化 Novelty 和 Significance。精确的 bias 分解使核心 claim 更 defensible——reviewer 无法用 \"min-form bias 怎么办\" 来攻击，因为作者已经 preemptively address 了。\n- 调研依据: PURE (NeurIPS 2025) 的 min-form credit assignment 本身引入了结构性 bias，这在原论文中未被充分讨论。结合 Jia et al. (ICML 2025) 的理论框架，可以更精确地定位 UGCA 解决的是哪一层 bias。\n\n【发掘点 2】\n- 维度: novelty 锐化\n- 内容: 当前 proposal 中 UGCA 与 \"Discovering Process-Outcome Credit\" (arXiv 2602.01034) 的差异化论述不够尖锐。两者都在做 process-outcome credit mixing，但区别在于信号来源和计算成本。建议在 novelty framing 中显式构建一个 2×2 矩阵：(信号来源: verifier 不确定性 vs. intrinsic information gain) × (粒度: per-step vs. trajectory-level)。UGCA 占据 (verifier 不确定性, per-step) 这个格子，PROGRS 占 (verifier 校准, trajectory-level)，Process-Outcome Credit 占 (intrinsic information gain, per-step)，vanilla GRPO 占 (无, trajectory-level)。这个矩阵可以让 reviewer 一目了然地看到 UGCA 的定位和唯一性。同时应强调：verifier 不确定性是 \"free\" 的（校准后直接获得），而 intrinsic information gain 需要额外 Monte Carlo rollouts，计算开销大一个数量级——这不只是方法论差异，更是实用性差异。\n- 价值: 锐化 Novelty 和 Related Work 差异化。让 reviewer 无法说 \"这不就是换了个 mixing signal 吗\"——矩阵清晰展示了 design space 中的空白。\n- 调研依据: 直接参考 Discovering Process-Outcome Credit (arXiv 2602.01034) 的方法论（Monte Carlo MIG + Decoupled Masking）与 UGCA 的校准 confidence interval gating 的对比。\n\n【发掘点 3】\n- 维度: significance 提升\n- 内容: Proposal 的 \"Broader Significance\" 部分提到了 code generation、scientific reasoning、agentic tasks，但这些只是列举，没有构建一个统一的抽象框架。建议将 UGCA 的核心 insight 抽象为一个更 general 的 principle：**\"Verifier-Uncertainty-Aware RL\"——任何使用不完美 verifier 的 RL 训练都应该根据 verifier 的 per-instance confidence 动态调整 credit assignment 的粒度和来源**。这不仅仅是 math reasoning 的技巧，而是一个关于 imperfect-verifier RL 的 general methodological principle。结合 \"Reward Under Attack\" (arXiv 2603.06621) 证明的 PRM 系统性脆弱性，这个 principle 有更广泛的 urgency。建议在 introduction 中将这个 general principle 作为论文的 higher-level contribution 明确提出，math reasoning 作为 instantiation。\n- 价值: 提升 Significance。从 \"a better credit assignment for math RL\" 升级为 \"a principled framework for RL with imperfect verifiers\"，影响面和引用潜力显著扩大。\n- 调研依据: Reward Under Attack (arXiv 2603.06621) 证明 PRM 是 systematically exploitable 的 fluency detectors；Uncertainty-Aware Reward Discounting (Apr 2026) 在 general RLHF 中用 ensemble disagreement 做类似的事但没有 process-outcome interpolation 的 framing。UGCA 可以将自己定位为连接这两个方向的桥梁。\n\n【发掘点 4】\n- 维度: 前提假设质疑\n- 内容: UGCA 的一个关键假设是 **PRM confidence-interval width 是 step-level 校准质量的可靠 proxy**。但 quantile regression 校准的 confidence interval 宽度反映的是 PRM 输出分布的 spread，未必直接对应 \"PRM 在这个 step 上是否准确\"。具体地说：(1) 一个 PRM 可能在某类 step 上系统性高估但 confidence interval 很窄（高确信的错误），此时 α 值大，UGCA 会错误地信任 biased process credit；(2) confidence interval 宽度可能与 step 的内在难度（而非 PRM 的不可靠性）强相关——一个很难的 step，PRM 也\"不确定\"，但这种不确定性反映的是问题难度而非 PRM 质量。建议增加一个 sanity check：在 cross-family PRM validation 中，除了 ECE 和 Brier score，还要展示 confidence-interval width 与 PRM 实际 step-level accuracy 的 rank correlation。如果 correlation 很低，需要讨论这对 gating 机制有效性的影响，或者引入 calibration residual 作为更直接的 proxy。\n- 价值: 强化核心 claim 的 defensibility。这是 reviewer 最可能攻击的假设——如果 confidence-interval width 不是好的 proxy，整个 gating 机制就失效了。Proactively addressing 这个假设比让 reviewer 发现后被动回应要好得多。\n- 调研依据: Park et al. (NeurIPS 2025) 的 quantile regression 校准主要优化的是 marginal calibration（ECE），但 conditional calibration（在特定 step type 上的准确性）可能不同。Distributional PRM (arXiv 2605.06785) 的 conditional OT 方法可能提供更好的 conditional calibration，建议讨论作为 upgrade path。\n\n【发掘点 5】\n- 维度: trivial alternative 威胁\n- 内容: 一个需要正面回答的问题：**为什么不直接用 PRM score 本身的 magnitude 作为 gating signal？** 即 α_i = σ(PRM_score_i)——PRM 给高分的 step 信任 process credit，PRM 给低分的 step 退化到 outcome credit。这个 trivial baseline 不需要任何 calibration machinery，计算成本更低。它在什么情况下会 fail 而 UGCA 不会？直觉上答案是：PRM score magnitude 混淆了 \"PRM 认为这步对\" 和 \"PRM 对这步有信心\"——一个 PRM 可以很自信地给出错误的高分。Calibrated confidence interval 分离了这两个维度。但这个论点需要在论文中 explicitly articulate 并通过实验验证（raw PRM score gating vs. calibrated CI width gating 的 ablation 已经在实验设计中了，很好，但 framing 上需要在 method section 就把这个 trivial alternative 拎出来讨论清楚）。\n- 价值: 锐化 Novelty。Reviewer 第一反应一定会问 \"为什么不直接用 PRM score 做 gating\"。在 method section 而非 ablation 中就直面这个问题，展示 calibration 的必要性，能把 novelty 从 \"我加了个 sigmoid gating\" 提升到 \"我引入了 verifier confidence 和 verifier prediction 的分离\"。\n- 调研依据: 基于领域整体趋势判断。ConfClip (arXiv 2509.17730) 用 model confidence 做 reward weighting 就是一种 \"用 score magnitude 做 gating\" 的思路，但它用的是 policy model 的 confidence 而非 verifier 的 calibrated uncertainty。两者的对比可以帮助 articulate UGCA 的必要性。\n\n【发掘点 6】\n- 维度: related work 差异化\n- 内容: Proposal 遗漏了一个可能的高相关工作：**ConfClip** (arXiv 2509.17730, Sep 2025)。ConfClip 也在做 confidence-weighted reward for RL，虽然它用的是 policy model 的 confidence 而非 PRM verifier 的 calibrated uncertainty，且不做 process-outcome interpolation，但 reviewer 可能会把两者混为一谈。建议在 related work 中增加一个 \"Confidence-based reward modulation\" 子节，将 UCAS (policy logit uncertainty)、ConfClip (policy confidence weighting)、Uncertainty-Aware Reward Discounting (ensemble disagreement) 统一归入，然后明确指出 UGCA 的差异：(1) 使用的是 external verifier 的 calibrated uncertainty 而非 policy 自身的 uncertainty；(2) 不是简单的 reward weighting 而是 process-outcome credit source 的切换。这两点差异使 UGCA 在理论上更可靠（policy 自身的 uncertainty 会随训练变化，verifier 的 uncertainty 是 frozen 的、独立的）。\n- 价值: 强化 Related Work 差异化。堵住 reviewer 把 UGCA 归入 \"又一个 confidence-based reward weighting\" 的退路。\n- 调研依据: 直接参考 ConfClip (arXiv 2509.17730) 和 UCAS (arXiv 2510.10649) 的方法论。\n\nSources:\n- [PROGRS: LLM Reasoning with Process Rewards for Outcome-Guided Steps](https://arxiv.org/abs/2604.02341)\n- [Distributional Process Reward Models](https://arxiv.org/abs/2605.06785)\n- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models](https://arxiv.org/abs/2506.09338)\n- [Discovering Process-Outcome Credit in Multi-Step LLM Reasoning](https://arxiv.org/abs/2602.01034)\n- [Do We Need to Verify Step by Step?](https://arxiv.org/abs/2502.10581)\n- [ConfClip: Confidence-Weighted and Clipped Reward for RL in LLMs](https://arxiv.org/abs/2509.17730)\n- [Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)\n- [PURE: Stop Summation: Min-Form Credit Assignment](https://arxiv.org/abs/2504.15275)\n- [GRPO-λ: Credit Assignment improves LLM Reasoning](https://arxiv.org/abs/2510.00194)\n- [UCAS: Uncertainty-aware Advantage Shaping](https://arxiv.org/abs/2510.10649)\n- [Awesome Credit Assignment in LLM-RL (survey repo)](https://github.com/xxzcc/Awesome-Credit-Assignment-in-LLM-RL)\n- [From Reasoning to Agentic: Credit Assignment in RL for LLMs](https://arxiv.org/abs/2604.09459)\n\n【补救 agent 本轮输出】:\nNow I have sufficient research material to provide a thorough analysis. Let me compile my assessment.\n\n---\n\n【状态】: 有缺陷待补救\n\n【前置调研发现】\n- **PURE / \"Stop Summation\" (NeurIPS 2025)**: Baselines include GRPO, Dr.GRPO, PRIME, GRPO+verifiable reward. Evaluated on MATH-500, AMC23, AIME 2024, OlympiadBench, MinervaMath. Ablations cover min-form vs. sum-form, temperature scaling, verifiable reward mixing ratio. Used Qwen2.5-Math-7B, Qwen2.5-7B, Llama-3.1-8B. 3 base models, reward hacking curves plotted over training.\n- **PROGRS (arXiv 2604.02341, Feb 2026)**: Baselines include GRPO, DAPO, and prior PRM-integration methods. Evaluated on MATH-500, AMC, AIME, MinervaMath, OlympiadBench. Uses frozen quantile-regression PRM + multi-scale coherence evaluator. Outcome-conditioned centering at trajectory level. **No publicly available code found.**\n- **GRPO-λ (arXiv 2510.00194, ICLR 2026)**: Evaluated on AIME24, MATH-500, OlympiadMath, MinervaMath, AMC with LLaMA-3.1 and Qwen2.5 (1.5B–7B). Ablations cover λ-return weighting variants, TD error approximations. **No specific open-source implementation found; only generic GRPO implementations available.**\n- **PRPO (arXiv 2601.07182, Jan 2026)**: Evaluated on MATH-500 with Qwen2.5-Math-1.5B. Process-outcome alignment via location-parameter shift. Relevant as the most direct process-outcome mixing baseline.\n- **VPPO / \"Save the Good Prefix\" (arXiv 2601.18984, Jan 2026)**: Uses PRM only to localize first error, then applies binary prefix reward + suffix penalty. Evaluated on multiple reasoning benchmarks with Pass@1 and Pass@K. Represents binary (hard) per-step differentiation alternative.\n- **\"Discovering Process-Outcome Credit\" (arXiv 2602.01034, Feb 2026)**: Step-wise Marginal Information Gain + Decoupled Masking for process-outcome credit mixing. Evaluated on MATH, Super-CLEVR. Most conceptually similar to UGCA (per-step process-outcome mixing) but via Monte Carlo intrinsic information gain rather than PRM calibration.\n- **\"Reward Under Attack\" (arXiv 2603.06621, Mar 2026)**: Three-tiered adversarial diagnostic framework for PRM robustness. Introduces PRM-BiasBench. Finds PRMs act as fluency detectors rather than reasoning verifiers under adversarial pressure—relevant to whether UGCA's reliance on PRM confidence intervals is well-founded.\n- **Distributional PRM (arXiv 2605.06785, May 2026)**: Conditional optimal transport calibration achieves SOTA Brier score and ECE on MATH-500 and AIME24-25. Calibration discussed only in context of test-time scaling (best-of-N). Cross-model/cross-distribution calibration degradation not explicitly studied.\n- **veRL framework (EuroSys 2025)**: Confirmed to support Qwen3, GRPO, DAPO, PRIME. Active development as of May 2026. PURE codebase available on GitHub (CJReinforce/PURE).\n\n- **调研总结**: 该领域当前的实验设计标准要求：(1) baselines 至少覆盖 outcome-only (GRPO/DAPO)、process-only (PURE)、以及其他 process-outcome 混合方法 (PRPO, VPPO)；(2) 评测至少覆盖 MATH-500 + 竞赛级 benchmark (AIME, AMC, OlympiadBench)；(3) 审稿人普遍要求 reward hacking 定量分析、training dynamics 可视化、以及 ablation 隔离各组件贡献；(4) 凡涉及 PRM 应用的工作，审稿人会关注 PRM 在训练过程中的 distribution shift 问题。\n\n---\n\n【缺陷 1】\n- 类别: baseline 不足\n- 问题: Proposal 的 Experimental Design 部分列出了 5 个 baselines（GRPO, DAPO, PURE, GRPO-λ, PROGRS），但遗漏了 Research Landscape 中明确讨论的两个最直接的 process-outcome 混合竞争方法：**PRPO**（固定结构性 process-outcome 对齐）和 **VPPO/\"Save the Good Prefix\"**（二元 per-step PRM 引导惩罚）。UGCA 的核心 claim 是\"per-step adaptive process-outcome interpolation 优于固定混合策略\"，而 PRPO 和 VPPO 恰好代表了两种固定混合策略（参数化 shift vs. 二元阈值）。缺少这两个 baselines，审稿人会直接质问：相比已有的 process-outcome 混合方法，UGCA 的 adaptive gating 到底带来了多少额外收益？\n- 严重度: 可补救\n- 补救方案: 将 PRPO 和 VPPO 加入 baseline 列表。由于两者均在 Qwen2.5-Math-1.5B 上有公开结果（PRPO: MATH-500 64.4%；VPPO: 多 benchmark 公开），可在 Qwen3-1.7B 上统一复现。VPPO 的二元 gating（α=1 或 α=0）恰好是 proposal 已有 ablation（hard gating）的外部方法对照，可一石二鸟。增加约 2×3=6 runs for 1.7B（~120 H100-hours），总计算预算增加 ~4.4%，可控。\n- 调研依据: PRPO (arXiv 2601.07182) 和 VPPO (arXiv 2601.18984) 均是 2026 年初发表的 process-outcome 混合 RL 方法，在该领域实验标准中属于直接可比方法。\n\n【缺陷 2】\n- 类别: 实验设计不足\n- 问题: Proposal 设计了 cross-family PRM validation（在 Qwen3 初始 rollouts 上验证 calibration 质量），但**仅在训练初始阶段验证**。RL 训练过程中 policy 分布持续漂移，frozen PRM 的 confidence interval 质量可能随训练推进而退化。如果 PRM 的 uncertainty 估计在训练后期失真，gating 机制会错误分配 process vs. outcome credit 的权重——这直接影响 UGCA 核心机制的有效性。整个方法的 premise 是\"confidence interval width w_i 是 PRM 可靠性的好代理\"，但这一 premise 未被全程验证。\n- 严重度: 可补救\n- 补救方案: 增加一项**纵向 PRM calibration tracking 实验**：在训练过程中每隔固定 step 数（如每 25% 训练进度）抽样一批 rollouts，计算 frozen PRM 的 ECE 和 Brier score，绘制 calibration quality vs. training progress 曲线。同时可绘制 gating 系数 α 的分布随训练推进的变化（是否整体向某一端坍缩）。这本质上是对 proposal 中已有\"periodic sampling of rollouts during training\"（PAG 分析）的自然扩展，增量计算成本极低（仅需对已抽样 rollouts 额外计算 calibration metrics）。如果发现显著退化，可讨论 periodic re-calibration 作为 future work 或轻量级缓解方案。\n- 调研依据: \"Reward Under Attack\" (arXiv 2603.06621) 的研究发现 PRM 在 adversarial optimization pressure 下表现退化，RL training 中的 policy drift 本质上是一种 soft adversarial optimization。Distributional PRM (arXiv 2605.06785) 的 calibration 评估也仅针对固定分布，未验证 training-time 分布漂移的影响。\n\n【缺陷 3】\n- 类别: ablation 不完整\n- 问题: Proposal 的 ablation 设计涵盖了 boundary cases、hard/soft gating、calibrated/uncalibrated、hyperparameter sensitivity，但缺少一项关键的**核心 assumption 验证实验**：UGCA 的理论基础假设\"PRM confidence interval width w_i 与 PRM 实际 step-level 预测误差正相关\"（即 w_i 大的 step 确实 PRM 不准，w_i 小的 step PRM 确实准）。如果这一假设不成立（例如 PRM 系统性地对某类 step 产生 narrow but wrong 的 confidence interval），gating 机制将不仅无效，还可能有害——让 policy 更信任恰好不可靠的 PRM 判断。\n- 严重度: 可补救\n- 补救方案: 增加一项 **per-step uncertainty-accuracy correlation 分析**：将所有 step 按 w_i 分成 5 个 quantile bin，每个 bin 内计算 PRM step-level 预测与 ground-truth step correctness 的 accuracy/F1/AUC。如果 narrow w_i 的 bin 确实有更高的 PRM 准确率，则验证了核心 assumption。这项分析可与 proposal 中已有的\"per-step uncertainty-conditioned accuracy\"指标合并（proposal 已计划做 5 quantile bins），只需明确报告 PRM 预测准确率（而非仅 policy step correctness），增量工作极小。如果验证失败，需讨论 alternative gating signals（如 PRM score margin、ensemble disagreement）。\n- 调研依据: Park et al. (NeurIPS 2025) 的 quantile regression calibration 验证了 aggregate ECE/Brier 指标，但未按 step type 或 confidence level 细分验证 confidence interval 的 discrimination quality。这一 gap 需要 UGCA 自行补充。\n\n【缺陷 4】\n- 类别: 可行性问题\n- 问题: Proposal 将 PROGRS 列为核心 baseline 之一，但调研发现 **PROGRS 没有公开可用的代码**。PROGRS 的实现涉及：(1) quantile-regression PRM freezing, (2) multi-scale coherence evaluator（short-window confidence volatility 惩罚），(3) outcome-conditioned centering（per-prompt-group 的 incorrect trajectory score 零均值化），以及 (4) 与 GRPO 的集成。正确复现这四个组件并非 trivial，尤其是 multi-scale coherence evaluator 的具体实现细节可能需要从论文反推。同样，**GRPO-λ 也未找到官方开源实现**。Proposal 预算中\"DAPO/PROGRS baseline runs: 200h\"仅计算了运行时间，未充分计入复现开发时间。\n- 严重度: 可补救\n- 补救方案: (1) 对 PROGRS：在 timeline 的 wk1-2 中显式分配 PROGRS 复现时间（建议 3-5 天），并设置 fallback——如果 multi-scale coherence evaluator 复现困难，至少实现 PROGRS 的核心组件（outcome-conditioned centering + frozen quantile PRM），将其标记为\"PROGRS (core)\"，并在论文中注明。(2) 对 GRPO-λ：论文公式相对清晰（eligibility trace reformulation），可基于 GRPO 代码添加 λ-return 计算，复现难度较低。(3) 建议在 timeline 预算中增加 ~80h 用于 baseline 复现开发和验证，总计算预算增加 ~3%。(4) 联系 PROGRS 和 GRPO-λ 作者索要代码——这是常规做法，在 8 周 timeline 中应尽早启动。\n- 调研依据: 基于领域实验规范判断——WebSearch 未找到 PROGRS 或 GRPO-λ 的公开代码库。PURE 和 DAPO 有官方 GitHub，veRL 框架也已开源。\n\n【缺陷 5】\n- 类别: 实验设计不足\n- 问题: Proposal 的 Research Landscape 中讨论了\"Discovering Process-Outcome Credit\"（arXiv 2602.01034），该方法也做 per-step process-outcome credit mixing（通过 Step-wise Marginal Information Gain），是 UGCA 概念上最接近的竞争方法。然而实验设计中既未将其列为 baseline，也未提供与之对比的定性/定量分析。审稿人很可能指出：你声称 UGCA 的 uncertainty-gated interpolation 优于其他 process-outcome 混合策略，但跳过了唯一做同类 per-step 混合的方法。\n- 严重度: 可补救\n- 补救方案: 有两种策略可选择：**(A) 加为 baseline**——复现 Step-wise MIG + Decoupled Masking，与 UGCA 直接对比。但该方法需要 Monte Carlo estimation of intrinsic information gain，计算开销可能显著高于 UGCA，compute-normalized comparison 可能天然偏向 UGCA。**(B) Compute-matched 分析**——如果完整复现成本过高，至少做以下：(1) 在论文 discussion 中明确解释为何不做直接 baseline 对比（computational overhead of MC estimation 导致 non-comparable compute budget），(2) 在 compute fairness 分析中理论估算该方法的 FLOPs 开销并与 UGCA 对比，(3) 如果该方法有公开结果在相近模型上，做 indirect comparison。建议优先选 (B) 以控制 timeline 风险，但在论文中充分讨论。\n- 调研依据: \"Discovering Process-Outcome Credit\" (arXiv 2602.01034) 在 MATH 和 Super-CLEVR 上评测，与 UGCA 的 benchmark 有交集（MATH）。该论文使用 Monte Carlo 估计而非 PRM calibration，两种方法代表了 per-step credit mixing 的两条技术路线。\n\n【缺陷 6】\n- 类别: 评估方案缺陷（轻微）\n- 问题: Proposal 计划在 Qwen3-8B 上\"top 2 configs × 3 seeds + evaluation-level bootstrap confidence intervals (1000 resamples on each benchmark)\"。对于 AIME 2024 和 AIME 2025 这类仅有 30 道题的竞赛 benchmark，即使用 1000 次 bootstrap resample，置信区间仍然很宽（30 题的二项分布标准差 ≈ 8%），可能导致方法间差异在统计意义上不显著。这并非 proposal 独有的问题（所有该领域论文都面临），但审稿人可能据此质疑在 AIME 上的 improvement 是否 significant。\n- 严重度: 可补救\n- 补救方案: (1) 在论文中预先 acknowledge AIME 的 small sample size limitation，报告 bootstrap CIs 并明确标注哪些差异显著、哪些不显著。(2) 对 AIME benchmark 可额外使用 **Pass@K (K=8 或 16)** 以增加有效样本量，观察方法间差异在不同 K 下是否一致。(3) 考虑增加 **Omni-MATH** 或 **AIME historical set (2019-2023)** 作为更大规模的竞赛级补充 benchmark 以提高统计功效。这些 benchmark 在近期论文中也有采用。\n- 调研依据: 基于领域实验规范判断——PURE 和 GRPO-λ 论文均在 AIME/AMC 上报告结果但未提供置信区间，PROGRS 同样如此。Proposal 已经比同行论文的统计实践更严谨（有 bootstrap CIs），但可进一步加强。\n\n---\n\n**整体评估**: 实验设计的框架和理念非常扎实——baseline 覆盖了主要技术路线、reward hacking 量化有 3 个互补指标、ablation 逻辑清晰且覆盖主要组件、compute fairness 考虑充分、统计处理优于同领域多数论文。上述 6 个缺陷均为可补救项，核心修复工作为：(1) 补 2 个 process-outcome mixing baseline（PRPO+VPPO），(2) 增加训练过程中的 PRM calibration 纵向追踪，(3) 增加 core assumption 验证实验，(4) 提前规划 PROGRS/GRPO-λ 复现的 timeline 风险。修复后实验设计可达 AAAI 主会门槛。\n\nSources:\n- [PURE - Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)\n- [PROGRS - LLM Reasoning with Process Rewards](https://arxiv.org/abs/2604.02341)\n- [GRPO-λ (ICLR 2026)](https://arxiv.org/abs/2510.00194)\n- [PRPO (arXiv 2026)](https://arxiv.org/abs/2601.07182)\n- [VPPO / Save the Good Prefix (arXiv 2026)](https://arxiv.org/abs/2601.18984)\n- [Discovering Process-Outcome Credit (arXiv 2026)](https://arxiv.org/abs/2602.01034)\n- [Reward Under Attack (arXiv 2026)](https://arxiv.org/abs/2603.06621)\n- [Distributional PRM (arXiv 2026)](https://arxiv.org/html/2605.06785)\n- [DAPO (NeurIPS 2025)](https://arxiv.org/abs/2503.14476)\n- [veRL Framework](https://github.com/volcengine/verl)\n- [veRL + Qwen Documentation](https://qwen.readthedocs.io/en/latest/training/verl.html)\n- [Park et al. PRM Calibration (NeurIPS 2025)](https://arxiv.org/pdf/2506.09338)"
}
```

---

### Runtime record

_source line 45 · 2026-05-27T08:29:26.471Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:29:26.471Z",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

## Round 3

20 recorded events

### User

_source line 46 · 2026-05-27T08:29:26.525Z_

【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
Now I have sufficient research context. Let me synthesize my findings and produce the assessment.

---

【状态】: 有发掘空间

【前置调研发现】
- **PROGRS** (arXiv 2604.02341, Apr 2026): 最直接的竞争者。使用 outcome-conditioned centering 将校准 PRM 引入 RL 训练，但只做 trajectory-level 的固定校正规则，不使用 per-step 不确定性信息。与 UGCA 的差异确实在于 per-step adaptive gating 的缺失。
- **Distributional PRM** (arXiv 2605.06785, May 2026): 通过 conditional optimal transport 实现 SOTA PRM 校准，但明确只 target test-time scaling (best-of-N, instance-adaptive search)，未应用于 RL 训练。这为 UGCA 提供了更强的校准工具（可替换 quantile regression），且论文本身确认了 gap。
- **Park et al. "Know What You Don't Know"** (NeurIPS 2025): Quantile regression PRM 校准的原始工作，输出 confidence bounds。明确用于 instance-adaptive scaling，未用于 RL credit assignment。UGCA 对其方法的迁移使用是合理的。
- **Jia et al. "Do We Need to Verify Step by Step?"** (ICML 2025): 证明 outcome supervision 统计上不比 process supervision 更难。这为 UGCA 的 "uncertain 时退化到 outcome credit" 提供了理论支撑——退化是 principled 的，不损失学习保证。
- **Discovering Process-Outcome Credit** (arXiv 2602.01034, Feb 2026): 用 Step-wise Marginal Information Gain + Decoupled Masking 做 process-outcome credit mixing，但依赖 Monte Carlo estimation of intrinsic information gain 而非 PRM 校准不确定性。方法论不同，但 motivating problem 高度重叠。
- **ConfClip** (arXiv 2509.17730, Sep 2025): 用模型自身 confidence 来加权 reward，但用的是 policy model 的 confidence 而非 verifier 的校准不确定性，且不做 process-outcome 插值。
- **Reward Under Attack** (arXiv 2603.06621, Feb 2026): 证明当前 SOTA PRM 是 systematically exploitable 的 "fluency detectors"，强化了 UGCA 的 motivation（PRM 不可盲目信任）。
- **PURE** (NeurIPS 2025): Min-form credit assignment，识别了 summation-form 导致的 reward hacking，但前提仍然是 PRM 分数可靠。
- **GRPO-λ / λ-GRPO** (arXiv 2510.00194 / ICLR 2026): Eligibility trace / implicit PRM credit，均匀信任 PRM 信号，没有 per-step adaptive weighting。

- **调研总结**: 当前领域有两条平行发展线：(1) PRM 校准技术（quantile regression, distributional OT）快速成熟但仅用于 test-time scaling；(2) Process-aware RL credit assignment 方法（PURE, GRPO-λ, PROGRS）迅速涌现但均匀或固定地信任 PRM 信号。将两者连接——用 PRM 校准不确定性驱动 RL 中的 per-step adaptive credit assignment——确实是一个被确认的 gap。这个 gap 不是 trivial 的，因为需要解决多个非平凡问题（cross-family 校准迁移、gating 函数设计、与 GRPO/PURE 训练框架的集成）。

---

【发掘点 1】
- 维度: 核心 claim 强化
- 内容: Proposal 的核心 framing 是 "bias-variance tradeoff"，但当前表述中 bias 的来源和量化不够锐利。具体而言：proposal 说 "process credit is biased when PRM is miscalibrated"，但 PURE 的 min-form credit 的 bias 不仅来自 PRM miscalibration，还来自 min-form 本身的保守性（min 操作是一种下界估计，对大多数正确 trajectory 也存在系统性低估）。建议将 bias 分解为两个来源：(a) PRM miscalibration bias（PRM 分数偏离真实 step correctness probability），(b) aggregation bias（min-form 或 sum-form 的结构性偏差）。UGCA 的 uncertainty gating 主要解决 (a)，但应明确承认 (b) 的存在并说明为什么 (b) 不是 UGCA 要解决的问题（或为什么解决 (a) 后 (b) 的影响可控）。这种精细的 bias 分解会让 reviewer 觉得作者对问题理解深刻，而非笼统地说 "bias"。
- 价值: 强化 Novelty 和 Significance。精确的 bias 分解使核心 claim 更 defensible——reviewer 无法用 "min-form bias 怎么办" 来攻击，因为作者已经 preemptively address 了。
- 调研依据: PURE (NeurIPS 2025) 的 min-form credit assignment 本身引入了结构性 bias，这在原论文中未被充分讨论。结合 Jia et al. (ICML 2025) 的理论框架，可以更精确地定位 UGCA 解决的是哪一层 bias。

【发掘点 2】
- 维度: novelty 锐化
- 内容: 当前 proposal 中 UGCA 与 "Discovering Process-Outcome Credit" (arXiv 2602.01034) 的差异化论述不够尖锐。两者都在做 process-outcome credit mixing，但区别在于信号来源和计算成本。建议在 novelty framing 中显式构建一个 2×2 矩阵：(信号来源: verifier 不确定性 vs. intrinsic information gain) × (粒度: per-step vs. trajectory-level)。UGCA 占据 (verifier 不确定性, per-step) 这个格子，PROGRS 占 (verifier 校准, trajectory-level)，Process-Outcome Credit 占 (intrinsic information gain, per-step)，vanilla GRPO 占 (无, trajectory-level)。这个矩阵可以让 reviewer 一目了然地看到 UGCA 的定位和唯一性。同时应强调：verifier 不确定性是 "free" 的（校准后直接获得），而 intrinsic information gain 需要额外 Monte Carlo rollouts，计算开销大一个数量级——这不只是方法论差异，更是实用性差异。
- 价值: 锐化 Novelty 和 Related Work 差异化。让 reviewer 无法说 "这不就是换了个 mixing signal 吗"——矩阵清晰展示了 design space 中的空白。
- 调研依据: 直接参考 Discovering Process-Outcome Credit (arXiv 2602.01034) 的方法论（Monte Carlo MIG + Decoupled Masking）与 UGCA 的校准 confidence interval gating 的对比。

【发掘点 3】
- 维度: significance 提升
- 内容: Proposal 的 "Broader Significance" 部分提到了 code generation、scientific reasoning、agentic tasks，但这些只是列举，没有构建一个统一的抽象框架。建议将 UGCA 的核心 insight 抽象为一个更 general 的 principle：**"Verifier-Uncertainty-Aware RL"——任何使用不完美 verifier 的 RL 训练都应该根据 verifier 的 per-instance confidence 动态调整 credit assignment 的粒度和来源**。这不仅仅是 math reasoning 的技巧，而是一个关于 imperfect-verifier RL 的 general methodological principle。结合 "Reward Under Attack" (arXiv 2603.06621) 证明的 PRM 系统性脆弱性，这个 principle 有更广泛的 urgency。建议在 introduction 中将这个 general principle 作为论文的 higher-level contribution 明确提出，math reasoning 作为 instantiation。
- 价值: 提升 Significance。从 "a better credit assignment for math RL" 升级为 "a principled framework for RL with imperfect verifiers"，影响面和引用潜力显著扩大。
- 调研依据: Reward Under Attack (arXiv 2603.06621) 证明 PRM 是 systematically exploitable 的 fluency detectors；Uncertainty-Aware Reward Discounting (Apr 2026) 在 general RLHF 中用 ensemble disagreement 做类似的事但没有 process-outcome interpolation 的 framing。UGCA 可以将自己定位为连接这两个方向的桥梁。

【发掘点 4】
- 维度: 前提假设质疑
- 内容: UGCA 的一个关键假设是 **PRM confidence-interval width 是 step-level 校准质量的可靠 proxy**。但 quantile regression 校准的 confidence interval 宽度反映的是 PRM 输出分布的 spread，未必直接对应 "PRM 在这个 step 上是否准确"。具体地说：(1) 一个 PRM 可能在某类 step 上系统性高估但 confidence interval 很窄（高确信的错误），此时 α 值大，UGCA 会错误地信任 biased process credit；(2) confidence interval 宽度可能与 step 的内在难度（而非 PRM 的不可靠性）强相关——一个很难的 step，PRM 也"不确定"，但这种不确定性反映的是问题难度而非 PRM 质量。建议增加一个 sanity check：在 cross-family PRM validation 中，除了 ECE 和 Brier score，还要展示 confidence-interval width 与 PRM 实际 step-level accuracy 的 rank correlation。如果 correlation 很低，需要讨论这对 gating 机制有效性的影响，或者引入 calibration residual 作为更直接的 proxy。
- 价值: 强化核心 claim 的 defensibility。这是 reviewer 最可能攻击的假设——如果 confidence-interval width 不是好的 proxy，整个 gating 机制就失效了。Proactively addressing 这个假设比让 reviewer 发现后被动回应要好得多。
- 调研依据: Park et al. (NeurIPS 2025) 的 quantile regression 校准主要优化的是 marginal calibration（ECE），但 conditional calibration（在特定 step type 上的准确性）可能不同。Distributional PRM (arXiv 2605.06785) 的 conditional OT 方法可能提供更好的 conditional calibration，建议讨论作为 upgrade path。

【发掘点 5】
- 维度: trivial alternative 威胁
- 内容: 一个需要正面回答的问题：**为什么不直接用 PRM score 本身的 magnitude 作为 gating signal？** 即 α_i = σ(PRM_score_i)——PRM 给高分的 step 信任 process credit，PRM 给低分的 step 退化到 outcome credit。这个 trivial baseline 不需要任何 calibration machinery，计算成本更低。它在什么情况下会 fail 而 UGCA 不会？直觉上答案是：PRM score magnitude 混淆了 "PRM 认为这步对" 和 "PRM 对这步有信心"——一个 PRM 可以很自信地给出错误的高分。Calibrated confidence interval 分离了这两个维度。但这个论点需要在论文中 explicitly articulate 并通过实验验证（raw PRM score gating vs. calibrated CI width gating 的 ablation 已经在实验设计中了，很好，但 framing 上需要在 method section 就把这个 trivial alternative 拎出来讨论清楚）。
- 价值: 锐化 Novelty。Reviewer 第一反应一定会问 "为什么不直接用 PRM score 做 gating"。在 method section 而非 ablation 中就直面这个问题，展示 calibration 的必要性，能把 novelty 从 "我加了个 sigmoid gating" 提升到 "我引入了 verifier confidence 和 verifier prediction 的分离"。
- 调研依据: 基于领域整体趋势判断。ConfClip (arXiv 2509.17730) 用 model confidence 做 reward weighting 就是一种 "用 score magnitude 做 gating" 的思路，但它用的是 policy model 的 confidence 而非 verifier 的 calibrated uncertainty。两者的对比可以帮助 articulate UGCA 的必要性。

【发掘点 6】
- 维度: related work 差异化
- 内容: Proposal 遗漏了一个可能的高相关工作：**ConfClip** (arXiv 2509.17730, Sep 2025)。ConfClip 也在做 confidence-weighted reward for RL，虽然它用的是 policy model 的 confidence 而非 PRM verifier 的 calibrated uncertainty，且不做 process-outcome interpolation，但 reviewer 可能会把两者混为一谈。建议在 related work 中增加一个 "Confidence-based reward modulation" 子节，将 UCAS (policy logit uncertainty)、ConfClip (policy confidence weighting)、Uncertainty-Aware Reward Discounting (ensemble disagreement) 统一归入，然后明确指出 UGCA 的差异：(1) 使用的是 external verifier 的 calibrated uncertainty 而非 policy 自身的 uncertainty；(2) 不是简单的 reward weighting 而是 process-outcome credit source 的切换。这两点差异使 UGCA 在理论上更可靠（policy 自身的 uncertainty 会随训练变化，verifier 的 uncertainty 是 frozen 的、独立的）。
- 价值: 强化 Related Work 差异化。堵住 reviewer 把 UGCA 归入 "又一个 confidence-based reward weighting" 的退路。
- 调研依据: 直接参考 ConfClip (arXiv 2509.17730) 和 UCAS (arXiv 2510.10649) 的方法论。

Sources:
- [PROGRS: LLM Reasoning with Process Rewards for Outcome-Guided Steps](https://arxiv.org/abs/2604.02341)
- [Distributional Process Reward Models](https://arxiv.org/abs/2605.06785)
- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models](https://arxiv.org/abs/2506.09338)
- [Discovering Process-Outcome Credit in Multi-Step LLM Reasoning](https://arxiv.org/abs/2602.01034)
- [Do We Need to Verify Step by Step?](https://arxiv.org/abs/2502.10581)
- [ConfClip: Confidence-Weighted and Clipped Reward for RL in LLMs](https://arxiv.org/abs/2509.17730)
- [Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)
- [PURE: Stop Summation: Min-Form Credit Assignment](https://arxiv.org/abs/2504.15275)
- [GRPO-λ: Credit Assignment improves LLM Reasoning](https://arxiv.org/abs/2510.00194)
- [UCAS: Uncertainty-aware Advantage Shaping](https://arxiv.org/abs/2510.10649)
- [Awesome Credit Assignment in LLM-RL (survey repo)](https://github.com/xxzcc/Awesome-Credit-Assignment-in-LLM-RL)
- [From Reasoning to Agentic: Credit Assignment in RL for LLMs](https://arxiv.org/abs/2604.09459)

【补救 agent 本轮输出】:
Now I have sufficient research material to provide a thorough analysis. Let me compile my assessment.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **PURE / "Stop Summation" (NeurIPS 2025)**: Baselines include GRPO, Dr.GRPO, PRIME, GRPO+verifiable reward. Evaluated on MATH-500, AMC23, AIME 2024, OlympiadBench, MinervaMath. Ablations cover min-form vs. sum-form, temperature scaling, verifiable reward mixing ratio. Used Qwen2.5-Math-7B, Qwen2.5-7B, Llama-3.1-8B. 3 base models, reward hacking curves plotted over training.
- **PROGRS (arXiv 2604.02341, Feb 2026)**: Baselines include GRPO, DAPO, and prior PRM-integration methods. Evaluated on MATH-500, AMC, AIME, MinervaMath, OlympiadBench. Uses frozen quantile-regression PRM + multi-scale coherence evaluator. Outcome-conditioned centering at trajectory level. **No publicly available code found.**
- **GRPO-λ (arXiv 2510.00194, ICLR 2026)**: Evaluated on AIME24, MATH-500, OlympiadMath, MinervaMath, AMC with LLaMA-3.1 and Qwen2.5 (1.5B–7B). Ablations cover λ-return weighting variants, TD error approximations. **No specific open-source implementation found; only generic GRPO implementations available.**
- **PRPO (arXiv 2601.07182, Jan 2026)**: Evaluated on MATH-500 with Qwen2.5-Math-1.5B. Process-outcome alignment via location-parameter shift. Relevant as the most direct process-outcome mixing baseline.
- **VPPO / "Save the Good Prefix" (arXiv 2601.18984, Jan 2026)**: Uses PRM only to localize first error, then applies binary prefix reward + suffix penalty. Evaluated on multiple reasoning benchmarks with Pass@1 and Pass@K. Represents binary (hard) per-step differentiation alternative.
- **"Discovering Process-Outcome Credit" (arXiv 2602.01034, Feb 2026)**: Step-wise Marginal Information Gain + Decoupled Masking for process-outcome credit mixing. Evaluated on MATH, Super-CLEVR. Most conceptually similar to UGCA (per-step process-outcome mixing) but via Monte Carlo intrinsic information gain rather than PRM calibration.
- **"Reward Under Attack" (arXiv 2603.06621, Mar 2026)**: Three-tiered adversarial diagnostic framework for PRM robustness. Introduces PRM-BiasBench. Finds PRMs act as fluency detectors rather than reasoning verifiers under adversarial pressure—relevant to whether UGCA's reliance on PRM confidence intervals is well-founded.
- **Distributional PRM (arXiv 2605.06785, May 2026)**: Conditional optimal transport calibration achieves SOTA Brier score and ECE on MATH-500 and AIME24-25. Calibration discussed only in context of test-time scaling (best-of-N). Cross-model/cross-distribution calibration degradation not explicitly studied.
- **veRL framework (EuroSys 2025)**: Confirmed to support Qwen3, GRPO, DAPO, PRIME. Active development as of May 2026. PURE codebase available on GitHub (CJReinforce/PURE).

- **调研总结**: 该领域当前的实验设计标准要求：(1) baselines 至少覆盖 outcome-only (GRPO/DAPO)、process-only (PURE)、以及其他 process-outcome 混合方法 (PRPO, VPPO)；(2) 评测至少覆盖 MATH-500 + 竞赛级 benchmark (AIME, AMC, OlympiadBench)；(3) 审稿人普遍要求 reward hacking 定量分析、training dynamics 可视化、以及 ablation 隔离各组件贡献；(4) 凡涉及 PRM 应用的工作，审稿人会关注 PRM 在训练过程中的 distribution shift 问题。

---

【缺陷 1】
- 类别: baseline 不足
- 问题: Proposal 的 Experimental Design 部分列出了 5 个 baselines（GRPO, DAPO, PURE, GRPO-λ, PROGRS），但遗漏了 Research Landscape 中明确讨论的两个最直接的 process-outcome 混合竞争方法：**PRPO**（固定结构性 process-outcome 对齐）和 **VPPO/"Save the Good Prefix"**（二元 per-step PRM 引导惩罚）。UGCA 的核心 claim 是"per-step adaptive process-outcome interpolation 优于固定混合策略"，而 PRPO 和 VPPO 恰好代表了两种固定混合策略（参数化 shift vs. 二元阈值）。缺少这两个 baselines，审稿人会直接质问：相比已有的 process-outcome 混合方法，UGCA 的 adaptive gating 到底带来了多少额外收益？
- 严重度: 可补救
- 补救方案: 将 PRPO 和 VPPO 加入 baseline 列表。由于两者均在 Qwen2.5-Math-1.5B 上有公开结果（PRPO: MATH-500 64.4%；VPPO: 多 benchmark 公开），可在 Qwen3-1.7B 上统一复现。VPPO 的二元 gating（α=1 或 α=0）恰好是 proposal 已有 ablation（hard gating）的外部方法对照，可一石二鸟。增加约 2×3=6 runs for 1.7B（~120 H100-hours），总计算预算增加 ~4.4%，可控。
- 调研依据: PRPO (arXiv 2601.07182) 和 VPPO (arXiv 2601.18984) 均是 2026 年初发表的 process-outcome 混合 RL 方法，在该领域实验标准中属于直接可比方法。

【缺陷 2】
- 类别: 实验设计不足
- 问题: Proposal 设计了 cross-family PRM validation（在 Qwen3 初始 rollouts 上验证 calibration 质量），但**仅在训练初始阶段验证**。RL 训练过程中 policy 分布持续漂移，frozen PRM 的 confidence interval 质量可能随训练推进而退化。如果 PRM 的 uncertainty 估计在训练后期失真，gating 机制会错误分配 process vs. outcome credit 的权重——这直接影响 UGCA 核心机制的有效性。整个方法的 premise 是"confidence interval width w_i 是 PRM 可靠性的好代理"，但这一 premise 未被全程验证。
- 严重度: 可补救
- 补救方案: 增加一项**纵向 PRM calibration tracking 实验**：在训练过程中每隔固定 step 数（如每 25% 训练进度）抽样一批 rollouts，计算 frozen PRM 的 ECE 和 Brier score，绘制 calibration quality vs. training progress 曲线。同时可绘制 gating 系数 α 的分布随训练推进的变化（是否整体向某一端坍缩）。这本质上是对 proposal 中已有"periodic sampling of rollouts during training"（PAG 分析）的自然扩展，增量计算成本极低（仅需对已抽样 rollouts 额外计算 calibration metrics）。如果发现显著退化，可讨论 periodic re-calibration 作为 future work 或轻量级缓解方案。
- 调研依据: "Reward Under Attack" (arXiv 2603.06621) 的研究发现 PRM 在 adversarial optimization pressure 下表现退化，RL training 中的 policy drift 本质上是一种 soft adversarial optimization。Distributional PRM (arXiv 2605.06785) 的 calibration 评估也仅针对固定分布，未验证 training-time 分布漂移的影响。

【缺陷 3】
- 类别: ablation 不完整
- 问题: Proposal 的 ablation 设计涵盖了 boundary cases、hard/soft gating、calibrated/uncalibrated、hyperparameter sensitivity，但缺少一项关键的**核心 assumption 验证实验**：UGCA 的理论基础假设"PRM confidence interval width w_i 与 PRM 实际 step-level 预测误差正相关"（即 w_i 大的 step 确实 PRM 不准，w_i 小的 step PRM 确实准）。如果这一假设不成立（例如 PRM 系统性地对某类 step 产生 narrow but wrong 的 confidence interval），gating 机制将不仅无效，还可能有害——让 policy 更信任恰好不可靠的 PRM 判断。
- 严重度: 可补救
- 补救方案: 增加一项 **per-step uncertainty-accuracy correlation 分析**：将所有 step 按 w_i 分成 5 个 quantile bin，每个 bin 内计算 PRM step-level 预测与 ground-truth step correctness 的 accuracy/F1/AUC。如果 narrow w_i 的 bin 确实有更高的 PRM 准确率，则验证了核心 assumption。这项分析可与 proposal 中已有的"per-step uncertainty-conditioned accuracy"指标合并（proposal 已计划做 5 quantile bins），只需明确报告 PRM 预测准确率（而非仅 policy step correctness），增量工作极小。如果验证失败，需讨论 alternative gating signals（如 PRM score margin、ensemble disagreement）。
- 调研依据: Park et al. (NeurIPS 2025) 的 quantile regression calibration 验证了 aggregate ECE/Brier 指标，但未按 step type 或 confidence level 细分验证 confidence interval 的 discrimination quality。这一 gap 需要 UGCA 自行补充。

【缺陷 4】
- 类别: 可行性问题
- 问题: Proposal 将 PROGRS 列为核心 baseline 之一，但调研发现 **PROGRS 没有公开可用的代码**。PROGRS 的实现涉及：(1) quantile-regression PRM freezing, (2) multi-scale coherence evaluator（short-window confidence volatility 惩罚），(3) outcome-conditioned centering（per-prompt-group 的 incorrect trajectory score 零均值化），以及 (4) 与 GRPO 的集成。正确复现这四个组件并非 trivial，尤其是 multi-scale coherence evaluator 的具体实现细节可能需要从论文反推。同样，**GRPO-λ 也未找到官方开源实现**。Proposal 预算中"DAPO/PROGRS baseline runs: 200h"仅计算了运行时间，未充分计入复现开发时间。
- 严重度: 可补救
- 补救方案: (1) 对 PROGRS：在 timeline 的 wk1-2 中显式分配 PROGRS 复现时间（建议 3-5 天），并设置 fallback——如果 multi-scale coherence evaluator 复现困难，至少实现 PROGRS 的核心组件（outcome-conditioned centering + frozen quantile PRM），将其标记为"PROGRS (core)"，并在论文中注明。(2) 对 GRPO-λ：论文公式相对清晰（eligibility trace reformulation），可基于 GRPO 代码添加 λ-return 计算，复现难度较低。(3) 建议在 timeline 预算中增加 ~80h 用于 baseline 复现开发和验证，总计算预算增加 ~3%。(4) 联系 PROGRS 和 GRPO-λ 作者索要代码——这是常规做法，在 8 周 timeline 中应尽早启动。
- 调研依据: 基于领域实验规范判断——WebSearch 未找到 PROGRS 或 GRPO-λ 的公开代码库。PURE 和 DAPO 有官方 GitHub，veRL 框架也已开源。

【缺陷 5】
- 类别: 实验设计不足
- 问题: Proposal 的 Research Landscape 中讨论了"Discovering Process-Outcome Credit"（arXiv 2602.01034），该方法也做 per-step process-outcome credit mixing（通过 Step-wise Marginal Information Gain），是 UGCA 概念上最接近的竞争方法。然而实验设计中既未将其列为 baseline，也未提供与之对比的定性/定量分析。审稿人很可能指出：你声称 UGCA 的 uncertainty-gated interpolation 优于其他 process-outcome 混合策略，但跳过了唯一做同类 per-step 混合的方法。
- 严重度: 可补救
- 补救方案: 有两种策略可选择：**(A) 加为 baseline**——复现 Step-wise MIG + Decoupled Masking，与 UGCA 直接对比。但该方法需要 Monte Carlo estimation of intrinsic information gain，计算开销可能显著高于 UGCA，compute-normalized comparison 可能天然偏向 UGCA。**(B) Compute-matched 分析**——如果完整复现成本过高，至少做以下：(1) 在论文 discussion 中明确解释为何不做直接 baseline 对比（computational overhead of MC estimation 导致 non-comparable compute budget），(2) 在 compute fairness 分析中理论估算该方法的 FLOPs 开销并与 UGCA 对比，(3) 如果该方法有公开结果在相近模型上，做 indirect comparison。建议优先选 (B) 以控制 timeline 风险，但在论文中充分讨论。
- 调研依据: "Discovering Process-Outcome Credit" (arXiv 2602.01034) 在 MATH 和 Super-CLEVR 上评测，与 UGCA 的 benchmark 有交集（MATH）。该论文使用 Monte Carlo 估计而非 PRM calibration，两种方法代表了 per-step credit mixing 的两条技术路线。

【缺陷 6】
- 类别: 评估方案缺陷（轻微）
- 问题: Proposal 计划在 Qwen3-8B 上"top 2 configs × 3 seeds + evaluation-level bootstrap confidence intervals (1000 resamples on each benchmark)"。对于 AIME 2024 和 AIME 2025 这类仅有 30 道题的竞赛 benchmark，即使用 1000 次 bootstrap resample，置信区间仍然很宽（30 题的二项分布标准差 ≈ 8%），可能导致方法间差异在统计意义上不显著。这并非 proposal 独有的问题（所有该领域论文都面临），但审稿人可能据此质疑在 AIME 上的 improvement 是否 significant。
- 严重度: 可补救
- 补救方案: (1) 在论文中预先 acknowledge AIME 的 small sample size limitation，报告 bootstrap CIs 并明确标注哪些差异显著、哪些不显著。(2) 对 AIME benchmark 可额外使用 **Pass@K (K=8 或 16)** 以增加有效样本量，观察方法间差异在不同 K 下是否一致。(3) 考虑增加 **Omni-MATH** 或 **AIME historical set (2019-2023)** 作为更大规模的竞赛级补充 benchmark 以提高统计功效。这些 benchmark 在近期论文中也有采用。
- 调研依据: 基于领域实验规范判断——PURE 和 GRPO-λ 论文均在 AIME/AMC 上报告结果但未提供置信区间，PROGRS 同样如此。Proposal 已经比同行论文的统计实践更严谨（有 bootstrap CIs），但可进一步加强。

---

**整体评估**: 实验设计的框架和理念非常扎实——baseline 覆盖了主要技术路线、reward hacking 量化有 3 个互补指标、ablation 逻辑清晰且覆盖主要组件、compute fairness 考虑充分、统计处理优于同领域多数论文。上述 6 个缺陷均为可补救项，核心修复工作为：(1) 补 2 个 process-outcome mixing baseline（PRPO+VPPO），(2) 增加训练过程中的 PRM calibration 纵向追踪，(3) 增加 core assumption 验证实验，(4) 提前规划 PROGRS/GRPO-λ 复现的 timeline 风险。修复后实验设计可达 AAAI 主会门槛。

Sources:
- [PURE - Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)
- [PROGRS - LLM Reasoning with Process Rewards](https://arxiv.org/abs/2604.02341)
- [GRPO-λ (ICLR 2026)](https://arxiv.org/abs/2510.00194)
- [PRPO (arXiv 2026)](https://arxiv.org/abs/2601.07182)
- [VPPO / Save the Good Prefix (arXiv 2026)](https://arxiv.org/abs/2601.18984)
- [Discovering Process-Outcome Credit (arXiv 2026)](https://arxiv.org/abs/2602.01034)
- [Reward Under Attack (arXiv 2026)](https://arxiv.org/abs/2603.06621)
- [Distributional PRM (arXiv 2026)](https://arxiv.org/html/2605.06785)
- [DAPO (NeurIPS 2025)](https://arxiv.org/abs/2503.14476)
- [veRL Framework](https://github.com/volcengine/verl)
- [veRL + Qwen Documentation](https://qwen.readthedocs.io/en/latest/training/verl.html)
- [Park et al. PRM Calibration (NeurIPS 2025)](https://arxiv.org/pdf/2506.09338)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa9448b2-2de9-403d-b220-2753c1ccdba7",
  "isSidechain": false,
  "promptId": "51d7a079-fc41-4bfc-accc-edd46b714d22",
  "type": "user",
  "uuid": "36015792-e205-4bad-bbd7-4690a4de3693",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research context. Let me synthesize my findings and produce the assessment.  ---  【状态…",
  "leafUuid": "36015792-e205-4bad-bbd7-4690a4de3693",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Assistant

_source line 49 · 2026-05-27T08:29:47.348Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the Round 2 worker outputs carefully.

**Discovery Agent Round 2 findings:**
1. **Bias decomposition** (Point 1): Decompose bias into (a) PRM miscalibration bias and (b) aggregation bias (min-form structural bias). UGCA addresses (a), should acknowledge (b).
2. **2×2 matrix for novelty** (Point 2): (signal source: verifier uncertainty vs intrinsic info gain) × (granularity: per-step vs trajectory-level). UGCA occupies (verifier uncertainty, per-step).


3. **General principle "Verifier-Uncertainty-Aware RL"** (Point 3): I should abstract UGCA into a broader methodological principle that could apply beyond this specific approach.
4. **Core assumption validation** (Point 4): The weights w_i need empirical grounding—I need to check if there's rank correlation between w_i and actual step-level PRM accuracy.
5. **Trivial alternative: raw PRM score as gating** (Point 5): I should explicitly compare against using raw PRM scores directly instead of calibrated confidence intervals and include an ablation study.
6. **ConfClip reference** (Point 6): I need to add ConfClip (arXiv 2509.17730) to the related work section.

Now looking at the experimental gaps: I'm missing comparisons to PRPO and VPPO, which are also process-outcome mixing methods and should be included as baselines. I need to track how PRM calibration evolves during training rather than just checking it at the start. The per-step uncertainty-accuracy correlation should be analyzed directly to validate the core assumption. Since PROGRS and GRPO-λ don't have public implementations, I'll need to plan for reproducing them. I should at least do a compute-matched analysis against "Discovering Process-Outcome Credit" even if a full baseline isn't feasible. Finally, the AIME evaluation on just 30 questions might have confidence intervals that are too wide—I should consider Pass@K metrics or adding more benchmarks to strengthen the results.

Let me verify a few of these suggestions, particularly checking whether ConfClip actually exists and what it does, while confirming that PRPO and VPPO are already discussed in the proposal and just need to be formalized as baselines. The longitudinal PRM tracking and 2×2 matrix framing are solid methodological ideas that don't require external validation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36015792-e205-4bad-bbd7-4690a4de3693",
  "isSidechain": false,
  "requestId": "req_011CbSm12y2jqiNDvrFUsvH4",
  "type": "assistant",
  "uuid": "e0ea0c9f-e897-4e31-bf23-d84974c606bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UbMCssFYNoE9yaXHyk5zU7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20724,
      "cache_read_input_tokens": 37861,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20724,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 37861,
          "cache_creation_input_tokens": 20724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20724
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

_source line 50 · 2026-05-27T08:29:47.351Z_

我来交叉验证第 2 轮 worker 的关键新建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0ea0c9f-e897-4e31-bf23-d84974c606bb",
  "isSidechain": false,
  "requestId": "req_011CbSm12y2jqiNDvrFUsvH4",
  "type": "assistant",
  "uuid": "dd453219-a937-4a8e-8c54-e7e2c2b00fbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UbMCssFYNoE9yaXHyk5zU7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20724,
      "cache_read_input_tokens": 37861,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20724,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 37861,
          "cache_creation_input_tokens": 20724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20724
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

_source line 51 · 2026-05-27T08:29:47.353Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QNp29RYtiwxGxdbSmXGt6m`</summary>

```json
{
  "query": "arXiv 2509.17730 ConfClip confidence-weighted clipped reward RL LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd453219-a937-4a8e-8c54-e7e2c2b00fbf",
  "isSidechain": false,
  "requestId": "req_011CbSm12y2jqiNDvrFUsvH4",
  "type": "assistant",
  "uuid": "480b5079-9b0c-48a8-81e2-e1511f8eefc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UbMCssFYNoE9yaXHyk5zU7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20724,
      "cache_read_input_tokens": 37861,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20724,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 37861,
          "cache_creation_input_tokens": 20724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20724
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

_source line 52 · 2026-05-27T08:29:55.064Z_

<details><summary>↩ Tool result · `toolu_01QNp29RYtiwxGxdbSmXGt6m`</summary>

```text
Web search results for query: "arXiv 2509.17730 ConfClip confidence-weighted clipped reward RL LLM 2025"

Links: [{"title":"[2509.17730] ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs","url":"https://arxiv.org/abs/2509.17730"},{"title":"ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs","url":"https://arxiv.org/html/2509.17730v1"},{"title":"CONFCLIP: CONFIDENCE-WEIGHTED AND CLIPPED REWARD FOR REINFORCEMENT","url":"https://arxiv.org/pdf/2509.17730"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=1100&show=2000"},{"title":"Every Question Has Its Own Value: Reinforcement Learning with Explicit Human Values","url":"https://arxiv.org/html/2510.20187v1"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=21775&show=2000"}]

I found the paper! Here's what I found about arXiv 2509.17730:

## ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs

Reinforcement learning (RL) has become a standard paradigm for refining large language models (LLMs) beyond pre-training and instruction tuning.

**The Problem:**
A prominent line of work is RL with verifiable rewards (RLVR), which leverages automatically verifiable outcomes to generate reward signals. While efficient, this framework faces two key limitations: First, its binary feedback is too sparse to capture the quality of the reasoning process. Second, its coarse-grained rewards potentially lead to vanishing gradients.

**The Solution:**
Inspired by observations from human learning, the authors introduce a RL technique that integrates verifiable outcomes with the model's own confidence estimates. This joint design enriches the reward signal, providing finer-grained feedback and implicitly supervising the reasoning process.

**Key Results:**
Experimental results demonstrate that the proposed method enhances RL performance across multiple datasets and reduces token consumption during inference.

The paper is authored by Bonan Zhang, Zhongqi Chen, Bowen Song, Qinya Li, Fan Wu, and Guihai Chen, and was published on September 22, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "480b5079-9b0c-48a8-81e2-e1511f8eefc2",
  "isSidechain": false,
  "promptId": "51d7a079-fc41-4bfc-accc-edd46b714d22",
  "type": "user",
  "uuid": "4f7771e3-5045-4b00-8aae-b991c8d1ec63",
  "toolUseResult": {
    "query": "arXiv 2509.17730 ConfClip confidence-weighted clipped reward RL LLM 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PVmzsRcJRwKrS8AyvKFw7G",
        "content": [
          {
            "title": "[2509.17730] ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs",
            "url": "https://arxiv.org/abs/2509.17730"
          },
          {
            "title": "ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs",
            "url": "https://arxiv.org/html/2509.17730v1"
          },
          {
            "title": "CONFCLIP: CONFIDENCE-WEIGHTED AND CLIPPED REWARD FOR REINFORCEMENT",
            "url": "https://arxiv.org/pdf/2509.17730"
          },
          {
            "title": "Machine Learning Sep 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-09?skip=1100&show=2000"
          },
          {
            "title": "Every Question Has Its Own Value: Reinforcement Learning with Explicit Human Values",
            "url": "https://arxiv.org/html/2510.20187v1"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=21775&show=2000"
          }
        ]
      },
      "I found the paper! Here's what I found about arXiv 2509.17730:\n\n## ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs\n\nReinforcement learning (RL) has become a standard paradigm for refining large language models (LLMs) beyond pre-training and instruction tuning.\n\n**The Problem:**\nA prominent line of work is RL with verifiable rewards (RLVR), which leverages automatically verifiable outcomes to generate reward signals. While efficient, this framework faces two key limitations: First, its binary feedback is too sparse to capture the quality of the reasoning process. Second, its coarse-grained rewards potentially lead to vanishing gradients.\n\n**The Solution:**\nInspired by observations from human learning, the authors introduce a RL technique that integrates verifiable outcomes with the model's own confidence estimates. This joint design enriches the reward signal, providing finer-grained feedback and implicitly supervising the reasoning process.\n\n**Key Results:**\nExperimental results demonstrate that the proposed method enhances RL performance across multiple datasets and reduces token consumption during inference.\n\nThe paper is authored by Bonan Zhang, Zhongqi Chen, Bowen Song, Qinya Li, Fan Wu, and Guihai Chen, and was published on September 22, 2025."
    ],
    "durationSeconds": 7.702830267000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "480b5079-9b0c-48a8-81e2-e1511f8eefc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-27T08:29:57.929Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R5xUM5x5jn1Azeb78Z9YJ9`</summary>

```json
{
  "query": "PROGRS \"LLM Reasoning with Process Rewards\" open source code github 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f7771e3-5045-4b00-8aae-b991c8d1ec63",
  "isSidechain": false,
  "requestId": "req_011CbSm38yVKxhQwe5uDZ3gH",
  "type": "assistant",
  "uuid": "be1b3000-0ce7-4452-b201-fc7680b6954d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBkVEcYmxMZZJrA8CmRNNM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 58585,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 58585,
          "cache_creation_input_tokens": 1431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1431
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

_source line 54 · 2026-05-27T08:30:03.853Z_

<details><summary>↩ Tool result · `toolu_01R5xUM5x5jn1Azeb78Z9YJ9`</summary>

```text
Web search results for query: "PROGRS "LLM Reasoning with Process Rewards" open source code github 2026"

Links: [{"title":"LLM Reasoning with Process Rewards for Outcome-Guided Steps","url":"https://arxiv.org/html/2604.02341"},{"title":"LLM Reasoning with Process Rewards for Outcome-Guided Steps","url":"https://arxiv.org/pdf/2604.02341"},{"title":"[2604.02341] LLM Reasoning with Process Rewards for Outcome-Guided Steps","url":"https://arxiv.org/abs/2604.02341"},{"title":"PRL: Process Reward Learning Improves LLMs' Reasoning Ability and Broadens the Reasoning Boundary","url":"https://arxiv.org/pdf/2601.10201"},{"title":"Posterior-GRPO: Rewarding Reasoning Processes in Code Generation","url":"https://arxiv.org/pdf/2508.05170"},{"title":"Rewarding Graph Reasoning Process makes LLMs more Generalized Reasoners","url":"https://arxiv.org/pdf/2503.00845"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"}]

Based on the search results, I found information about PROGRS:

PROGRS (Process-Reward Outcome-Guided Reasoning Steps) is a framework integrating process-level guidance into RLVR while preserving outcome dominance, with code available at https://anonymous.4open.science/r/PROGRS-914D/.

The research was published on arxiv.org with the paper titled "LLM Reasoning with Process Rewards for Outcome-Guided Steps" (dated February 8, 2026).

PROGRS constrains process rewards through outcome-conditioned centering while leveraging hierarchical coherence to extract stable signals from noisy step-level estimates, and demonstrates improvements on benchmarks including MATH-500, AMC, AIME, and MinervaMath.

Note: The code repository appears to be hosted on an anonymous review platform (4open.science) rather than a permanent GitHub repository. This is typical during the peer review process before official publication.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be1b3000-0ce7-4452-b201-fc7680b6954d",
  "isSidechain": false,
  "promptId": "51d7a079-fc41-4bfc-accc-edd46b714d22",
  "type": "user",
  "uuid": "76472f24-443a-455f-a413-c95c3d97c46a",
  "toolUseResult": {
    "query": "PROGRS \"LLM Reasoning with Process Rewards\" open source code github 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UMShHgGx2hjrsN16NgkmJf",
        "content": [
          {
            "title": "LLM Reasoning with Process Rewards for Outcome-Guided Steps",
            "url": "https://arxiv.org/html/2604.02341"
          },
          {
            "title": "LLM Reasoning with Process Rewards for Outcome-Guided Steps",
            "url": "https://arxiv.org/pdf/2604.02341"
          },
          {
            "title": "[2604.02341] LLM Reasoning with Process Rewards for Outcome-Guided Steps",
            "url": "https://arxiv.org/abs/2604.02341"
          },
          {
            "title": "PRL: Process Reward Learning Improves LLMs' Reasoning Ability and Broadens the Reasoning Boundary",
            "url": "https://arxiv.org/pdf/2601.10201"
          },
          {
            "title": "Posterior-GRPO: Rewarding Reasoning Processes in Code Generation",
            "url": "https://arxiv.org/pdf/2508.05170"
          },
          {
            "title": "Rewarding Graph Reasoning Process makes LLMs more Generalized Reasoners",
            "url": "https://arxiv.org/pdf/2503.00845"
          },
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          }
        ]
      },
      "Based on the search results, I found information about PROGRS:\n\nPROGRS (Process-Reward Outcome-Guided Reasoning Steps) is a framework integrating process-level guidance into RLVR while preserving outcome dominance, with code available at https://anonymous.4open.science/r/PROGRS-914D/.\n\nThe research was published on arxiv.org with the paper titled \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\" (dated February 8, 2026).\n\nPROGRS constrains process rewards through outcome-conditioned centering while leveraging hierarchical coherence to extract stable signals from noisy step-level estimates, and demonstrates improvements on benchmarks including MATH-500, AMC, AIME, and MinervaMath.\n\nNote: The code repository appears to be hosted on an anonymous review platform (4open.science) rather than a permanent GitHub repository. This is typical during the peer review process before official publication."
    ],
    "durationSeconds": 5.918850436000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "be1b3000-0ce7-4452-b201-fc7680b6954d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-27T08:30:07.422Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015HUb9TpfDzxE2Q89hmE1kH`</summary>

```json
{
  "query": "\"Discovering Process-Outcome Credit\" arXiv 2602.01034 code github implementation available"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76472f24-443a-455f-a413-c95c3d97c46a",
  "isSidechain": false,
  "requestId": "req_011CbSm3nXCnB2woUMFcPCWD",
  "type": "assistant",
  "uuid": "be15b510-df53-4f4c-8e7f-82ea37a3c2a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYB1okkCSH3LxQqFrP9Syo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 60016,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 60016,
          "cache_creation_input_tokens": 656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 656
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

_source line 56 · 2026-05-27T08:30:17.938Z_

<details><summary>↩ Tool result · `toolu_015HUb9TpfDzxE2Q89hmE1kH`</summary>

```text
Web search results for query: ""Discovering Process-Outcome Credit" arXiv 2602.01034 code github implementation available"

Links: [{"title":"[2602.01034] Discovering Process-Outcome Credit in Multi-Step LLM Reasoning","url":"https://arxiv.org/abs/2602.01034"},{"title":"Artificial Intelligence Feb 2026","url":"https://arxiv.org/list/cs.AI/2026-02?skip=50&show=2000"},{"title":"Discovering Process–Outcome Credit in Multi-Step LLM Reasoning","url":"https://arxiv.org/html/2602.01034"},{"title":"Discovering Process-Outcome Credit in Multi-Step LLM Reasoning","url":"https://arxiv.org/pdf/2602.01034"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"}]

Now let me search for GitHub implementation information:

Links: [{"title":"[2602.01034] Discovering Process-Outcome Credit in Multi-Step LLM Reasoning","url":"https://arxiv.org/abs/2602.01034"},{"title":"Discriminative Rule Learning for Outcome-Guided Process Model Discovery","url":"https://arxiv.org/pdf/2510.27343"},{"title":"Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation","url":"https://arxiv.org/pdf/2412.15118"},{"title":"Determinants of Implementation Success Coordinating Ventilator, Early Ambulation and Rehabilitation Efforts","url":"https://cdn.clinicaltrials.gov/large-docs/41/NCT04249141/Prot_SAP_000.pdf"},{"title":"A Monitoring and Discovery Approach for Declarative Processes Based on   Streams","url":"https://arxiv.org/pdf/2208.05364"}]

Based on the search results, I found information about the paper. Here's what I can tell you:

## Paper Details

The paper "Discovering Process-Outcome Credit in Multi-Step LLM Reasoning" (arXiv:2602.01034) was submitted on February 1, 2026, and is authored by Xiangwei Wang, Wei Wang, Ken Chen, Nanduni Nimalsiri, and Saman Halgamuge.

## Framework Overview

The paper proposes a novel framework that introduces a Step-wise Marginal Information Gain (MIG) mechanism to quantify the intrinsic value of reasoning steps, and implements a Decoupled Masking Strategy that applies process-oriented rewards to chain-of-thought (CoT) and outcome-oriented rewards to the full completion. The framework also incorporates a Dual-Gated SFT objective to stabilize training with high-quality structural and factual signals.

## Experimental Results

Experiments across textual and multi-modal benchmarks (such as MATH and Super-CLEVR) show the approach outperforms baselines like GRPO in sample efficiency and final accuracy, with superior out-of-distribution robustness and zero-shot transfer capabilities to unseen reasoning tasks.

## GitHub Implementation

Unfortunately, the search results do not contain information about GitHub code or implementation availability for this paper. You may want to check the paper directly on arXiv (https://arxiv.org/abs/2602.01034) or the authors' institutional repositories for any code releases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be15b510-df53-4f4c-8e7f-82ea37a3c2a3",
  "isSidechain": false,
  "promptId": "51d7a079-fc41-4bfc-accc-edd46b714d22",
  "type": "user",
  "uuid": "1bebf355-3919-470b-b243-1f7c8b81f1e5",
  "toolUseResult": {
    "query": "\"Discovering Process-Outcome Credit\" arXiv 2602.01034 code github implementation available",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GHj52iDrd9Q8erfHKm8HtP",
        "content": [
          {
            "title": "[2602.01034] Discovering Process-Outcome Credit in Multi-Step LLM Reasoning",
            "url": "https://arxiv.org/abs/2602.01034"
          },
          {
            "title": "Artificial Intelligence Feb 2026",
            "url": "https://arxiv.org/list/cs.AI/2026-02?skip=50&show=2000"
          },
          {
            "title": "Discovering Process–Outcome Credit in Multi-Step LLM Reasoning",
            "url": "https://arxiv.org/html/2602.01034"
          },
          {
            "title": "Discovering Process-Outcome Credit in Multi-Step LLM Reasoning",
            "url": "https://arxiv.org/pdf/2602.01034"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2509.26578"
          }
        ]
      },
      "Now let me search for GitHub implementation information:",
      {
        "tool_use_id": "srvtoolu_012osWkWFRQYioeLkQp1G5xZ",
        "content": [
          {
            "title": "[2602.01034] Discovering Process-Outcome Credit in Multi-Step LLM Reasoning",
            "url": "https://arxiv.org/abs/2602.01034"
          },
          {
            "title": "Discriminative Rule Learning for Outcome-Guided Process Model Discovery",
            "url": "https://arxiv.org/pdf/2510.27343"
          },
          {
            "title": "Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation",
            "url": "https://arxiv.org/pdf/2412.15118"
          },
          {
            "title": "Determinants of Implementation Success Coordinating Ventilator, Early Ambulation and Rehabilitation Efforts",
            "url": "https://cdn.clinicaltrials.gov/large-docs/41/NCT04249141/Prot_SAP_000.pdf"
          },
          {
            "title": "A Monitoring and Discovery Approach for Declarative Processes Based on   Streams",
            "url": "https://arxiv.org/pdf/2208.05364"
          }
        ]
      },
      "Based on the search results, I found information about the paper. Here's what I can tell you:\n\n## Paper Details\n\nThe paper \"Discovering Process-Outcome Credit in Multi-Step LLM Reasoning\" (arXiv:2602.01034) was submitted on February 1, 2026, and is authored by Xiangwei Wang, Wei Wang, Ken Chen, Nanduni Nimalsiri, and Saman Halgamuge.\n\n## Framework Overview\n\nThe paper proposes a novel framework that introduces a Step-wise Marginal Information Gain (MIG) mechanism to quantify the intrinsic value of reasoning steps, and implements a Decoupled Masking Strategy that applies process-oriented rewards to chain-of-thought (CoT) and outcome-oriented rewards to the full completion. The framework also incorporates a Dual-Gated SFT objective to stabilize training with high-quality structural and factual signals.\n\n## Experimental Results\n\nExperiments across textual and multi-modal benchmarks (such as MATH and Super-CLEVR) show the approach outperforms baselines like GRPO in sample efficiency and final accuracy, with superior out-of-distribution robustness and zero-shot transfer capabilities to unseen reasoning tasks.\n\n## GitHub Implementation\n\nUnfortunately, the search results do not contain information about GitHub code or implementation availability for this paper. You may want to check the paper directly on arXiv (https://arxiv.org/abs/2602.01034) or the authors' institutional repositories for any code releases."
    ],
    "durationSeconds": 10.51219268,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "be15b510-df53-4f4c-8e7f-82ea37a3c2a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-27T08:31:20.019Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me now synthesize the Round 2 findings:

**Cross-validation results:**
1. **ConfClip (arXiv 2509.17730)** — VERIFIED. Paper exists. Uses model's own confidence estimates to weight rewards in RLVR. Relevant as a "confidence-based reward weighting" comparison point. Discovery agent's suggestion to include it is valid.

2. **PROGRS code availability** — Partially available on anonymous review platform (4open.science/r/PROGRS-914D/). This is better than "no code" but it's an anonymous review link that may be temporary. 

The remedy agent's concern about reproduction difficulty is partially mitigated but still valid.

3. **"Discovering Process-Outcome Credit" code** — No public code found. Remedy agent's concern about difficulty of direct comparison is valid.

Now assessing which suggestions to adopt: The bias decomposition refinement is worth adopting—distinguishing PRM miscalibration bias from min-form aggregation bias strengthens the framing without changing the core method. The 2×2 matrix is also a strong presentation choice that clarifies the positioning.

I'll partially adopt the verifier-uncertainty principle since it's already implicit in the broader significance section—just needs sharper language. Both the remedy and discovery agents flagged the w_i versus accuracy correlation as critical, so that's definitely getting addressed. The raw PRM score gating alternative is important to include as an ablation alongside the existing calibrated versus uncalibrated comparison.

ConfClip reference checks out. For the remedy agent's suggestions, I'm adding PRPO and VPPO baselines on the 1.7B model to avoid scope creep, since VPPO overlaps nicely with the hard-gating ablation. The longitudinal PRM calibration tracking is essential—it addresses both agents' concerns and has minimal compute overhead since it leverages existing training runs.

I'm adopting the core assumption verification independently flagged by both agents, focusing on per-step uncertainty-accuracy correlations. For PROGRS and GRPO-λ, I'll include them with a clear reproduction timeline despite partial code availability. On the "Discovering Process-Outcome Credit" baseline, I'm going with a compute-matched analysis and discussion rather than a full baseline run, since the MC estimation overhead makes direct comparison unfair. For AIME's small sample size, I need to decide how to handle it.

For the AIME limitation, I'm acknowledging it and adding Pass@K analysis rather than expanding the benchmark suite further—we already have six benchmarks, so adding more would be diminishing returns. Looking at the broader pattern, Round 1 addressed major structural gaps like novelty framing and missing baselines, while Round 2 is refining those foundations with bias decomposition and longitudinal tracking. The discovery and remedy agents are now surfacing increasingly granular issues, which suggests we're hitting the point where further iterations yield smaller gains. That said, the longitudinal PRM calibration and core assumption validation are substantive enough to meaningfully strengthen the paper's experimental rigor.

I'm leaning toward one more round to validate these changes, but I recognize the marginal returns are diminishing and the risk of scope creep is real. Most of what Round 2 added—the bias decomposition, the 2×2 matrix, the longitudinal tracking extensions—are refinements to the existing structure rather than fundamental shifts in how the work is framed or executed. The improvements from Round 2 feel substantial enough—longitudinal tracking, core assumption validation, and new baselines—that they're genuinely strengthening the work rather than just fine-tuning. I'll push for one more round with the understanding that Round 3 should be the convergence point. Looking at the idea quality, the novelty and significance both land in the medium-to-strong range, giving this a ceiling around 48-50%, though the core contribution remains a principled combination of existing techniques rather than something fundamentally new.

With the experimental additions, the design is becoming quite comprehensive, and technical soundness is approaching strong. My estimate has ticked up slightly to 39% from the initial 38%, driven by better novelty articulation through the bias decomposition and positioning matrix, more thorough assumption validation, and fuller baseline coverage—though the growing compute requirements do introduce some feasibility risk.

I need to be disciplined about scope though. The proposal shouldn't balloon into something unfocused; it's better to make one strong argument cleanly than to stretch across a loose, bloated narrative.

Now I'm identifying the key improvements to weave in: the bias decomposition framework, the 2×2 positioning matrix, ConfClip as a related work reference, raw PRM score gating as an explicit baseline, PRPO and VPPO comparisons, longitudinal calibration tracking, the core assumption validation around weight-accuracy correlation, PROGRS code availability, and a compute-matched discussion of the Process-Outcome Credit method. I'm also checking my citation inventory to make sure nothing from Round 1 gets dropped. Continuing through the recent papers and benchmarks, I've got Jia et al. from ICML 2025, several more arxiv preprints covering process-outcome credit assignment and prefix-saving approaches, plus the finding that GRPO has hidden PRM properties. I'm also tracking DAPO, adversarial robustness work, and the full suite of mathematical benchmarks used for evaluation.

Now adding ConfClip from the latest round, along with PRPO and VPPO as baseline comparisons.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bebf355-3919-470b-b243-1f7c8b81f1e5",
  "isSidechain": false,
  "requestId": "req_011CbSm4pjSB7WS8Jf5rPMRv",
  "type": "assistant",
  "uuid": "16c9513b-8dcf-4289-9181-71986aa8843f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019xqDS3wsLYFWa3aD4jMzkD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 920,
      "cache_read_input_tokens": 60672,
      "output_tokens": 10109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10109,
          "cache_read_input_tokens": 60672,
          "cache_creation_input_tokens": 920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 920
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

_source line 58 · 2026-05-27T08:33:59.853Z_

交叉验证完成。现在整合第 2 轮。

【阶段】: 迭代第 2 轮

【交叉验证调研】:
1. **ConfClip (arXiv 2509.17730)** — 已验证存在。用 policy model 自身 confidence 加权 reward 以丰富 RLVR 信号，Sep 2025 发表。发掘 agent 建议将其纳入 related work 进行差异化（policy confidence vs. verifier calibrated uncertainty），建议成立。
2. **PROGRS 代码可用性** — 搜索发现 PROGRS 在匿名评审平台有代码（anonymous.4open.science/r/PROGRS-914D/）。这部分缓解了补救 agent 关于"无公开代码"的担忧，但匿名链接可能临时性，仍需在 timeline 中预留复现时间。补救 agent 建议调整为"有部分参考代码，仍需预留复现验证时间"。
3. **"Discovering Process-Outcome Credit" 代码** — 未找到公开代码。补救 agent 建议的 Option B（compute-matched 分析 + discussion）是务实选择。

【发掘 agent 有效建议采纳】:
1. **Bias 分解（发掘点 1）** — **逻辑自洽，采纳**。将 process credit 的 bias 分解为 (a) PRM miscalibration bias 和 (b) min-form aggregation bias，明确 UGCA 主要解决 (a)，preemptively 回应 reviewer 关于 min-form bias 的质疑。这是 framing 精炼，不需要文献验证。
2. **2×2 定位矩阵（发掘点 2）** — **采纳**。(signal source: verifier uncertainty vs. intrinsic information gain) × (granularity: per-step vs. trajectory-level)，UGCA 占据 (verifier uncertainty, per-step) 格子。零实现成本，极好的 presentation device。
3. **"Verifier-Uncertainty-Aware RL" general principle（发掘点 3）** — **部分采纳**。当前 proposal 已有 Broader Significance 段落，锐化语言即可，不进一步扩展以避免 overclaim。
4. **Core assumption validation: w_i vs accuracy correlation（发掘点 4）** — **采纳**。与补救 agent 缺陷 3 独立收敛到同一结论（两位 worker 独立识别 = 高信号）。增加 per-step uncertainty-accuracy rank correlation 分析。
5. **Raw PRM score gating as trivial alternative（发掘点 5）** — **采纳**。在 method section 显式讨论 "PRM score magnitude vs. calibrated CI width" 的区别，并将 raw score gating 加为 ablation 项。这与已有的 "calibrated vs uncalibrated" ablation 互补但不重复——前者是 gating signal 来源不同，后者是同一信号是否校准。
6. **ConfClip 纳入 related work（发掘点 6）** — **已验证，采纳**。在 "Uncertainty in RL rewards" 子节中增加 ConfClip。

【补救 agent 有效建议采纳】:
1. **PRPO + VPPO baselines（缺陷 1）** — **采纳，限 1.7B**。PRPO（固定结构 shift）和 VPPO（二元 per-step PRM gating）恰好代表两种固定 process-outcome 混合策略，与 UGCA 的 adaptive gating 形成完整对比谱系。VPPO 的 binary gating 与已有 hard-gating ablation 一石二鸟。仅在 1.7B 上增加，+120 H100-hours。8B 上不增加（baselines 已足够多）。
2. **纵向 PRM calibration tracking（缺陷 2）** — **采纳**。在训练过程中每 25% 进度抽样计算 ECE/Brier + α 分布变化。极低增量成本，piggyback 在已有 PAG 采样上。这是方法可靠性的关键证据。两位 worker 从不同角度（发掘：assumption validation；补救：distribution shift 风险）共同指向这一需求。
3. **Core assumption 验证（缺陷 3）** — **采纳**。与发掘点 4 合并。Per-step w_i 分 5 quantile bins，报告每 bin 的 PRM step-level prediction accuracy（不仅仅是 policy step correctness）。
4. **PROGRS/GRPO-λ 复现 timeline（缺陷 4）** — **采纳，调整**。PROGRS 有匿名评审代码可参考，降低复现风险。在 wk1-2 显式分配 3 天用于 PROGRS 核心组件（outcome-conditioned centering + frozen quantile PRM）复现验证。GRPO-λ 公式清晰，基于 GRPO 代码添加 λ-return 即可。
5. **"Discovering Process-Outcome Credit" 处理（缺陷 5）** — **采纳 Option B**。无公开代码且 MC estimation 开销使 compute-normalized 对比天然不公平。在论文中 (a) 明确解释不做直接 baseline 的原因，(b) 理论估算 FLOPs 对比，(c) 在 MATH 上做 indirect comparison（若有公开结果）。
6. **AIME small sample size（缺陷 6）** — **部分采纳**。在论文中 acknowledge limitation + 报告 bootstrap CIs 并标注显著性。增加 Pass@K (K=8) 分析以增加有效样本量。不新增额外 benchmark（已有 6 个，足够）。

【本轮 proposal 主要变更】:

*Idea 层面变更：*
- 增加 bias 分解论述：PRM miscalibration bias vs. min-form aggregation bias，UGCA 精准解决前者
- 增加 2×2 定位矩阵：(信号来源 × 粒度) 明确 UGCA 的 design space 位置
- Method section 增加 raw PRM score gating 作为 trivial alternative 的显式讨论
- ConfClip (arXiv 2509.17730) 纳入 related work
- 锐化 "verifier prediction vs. verifier confidence" 的分离作为核心 insight

*实验层面变更：*
- 1.7B baselines 增加 PRPO 和 VPPO
- 增加纵向 PRM calibration tracking（ECE/Brier vs. training progress + α distribution drift）
- 增加 core assumption 验证（w_i vs. PRM step accuracy rank correlation）
- 增加 raw PRM score gating ablation
- 增加 Pass@K (K=8) 分析用于 AIME
- "Discovering Process-Outcome Credit" 处理为 compute-matched discussion
- Timeline 调整：wk1-2 显式分配 PROGRS 复现时间
- 资源微调至 ~2900 H100-hours

【idea 质量评估】: Novelty=中-强 Significance=中-强 → idea 天花板约 48%
- Novelty 评估不变。bias 分解、2×2 矩阵、trivial alternative 讨论均为 framing 精炼，强化了已有 novelty 的表述但未改变 novelty 本身。核心贡献仍是"已有 building blocks 的原则性组合"，但现在 articulation 更 sharp。
- Significance 不变。broader principle 的讨论已足够，不宜进一步扩展。

【实验完备性评估】: Technical Soundness=中-强（接近强） → 地板进一步加固
- 纵向 calibration tracking 和 core assumption 验证是两个关键增补，直接回应方法有效性的核心前提。
- Baselines 从 5 扩展到 7（1.7B 含 PRPO/VPPO），对 process-outcome mixing 方法的覆盖更完整。
- 剩余风险：实验规模较大（~2900 H100-hours），timeline 紧张（8 周），PROGRS 复现的工程量仍有不确定性。

【当前概率估计】: [33% - 46%] 中位 39%
- 相比 Round 1（中位 38%）微升 1 个百分点，主要因为实验设计的完备性进一步提高，且 core assumption 验证堵住了一个重要的潜在攻击面。
- 概率未大幅提升是因为 idea 质量天花板（~48%）未改变，Round 2 的改进主要在表述和实验层面。

【决策】: 继续

【决策理由】: Round 2 仍产生了有意义的改进（bias 分解、2×2 定位矩阵、纵向 calibration tracking、core assumption 验证、PRPO/VPPO baselines），不完全属于微调。但改进力度明显低于 Round 1，预期 Round 3 将触发"连续 2 轮只做微调"收敛条件。再做一轮以确认更新后的 proposal 无新引入问题。

【引用清单核对】（确保所有原始及新增引用保留）：
1. PURE (NeurIPS 2025) ✓
2. GRPO-λ (arXiv Oct 2025) / arXiv 2510.00194 ✓
3. PROGRS (arXiv Apr 2026) / arXiv 2604.02341 ✓
4. UCAS (arXiv Oct 2025) / arXiv 2510.10649 ✓
5. Distributional PRM (arXiv 2605.06785, May 2026) ✓
6. PathFinder-PRM (arXiv May 2025) ✓
7. PRPO (arXiv Jan 2026) ✓
8. Uncertainty-Aware Reward Discounting (arXiv Apr 2026) ✓
9. TP-GRPO (arXiv Jul 2025) ✓
10. PRIME (arXiv Feb 2025) ✓
11. Park et al. quantile regression (NeurIPS 2025) ✓
12. Jia et al. (ICML 2025) ✓
13. PRL (arXiv 2026) ✓
14. arXiv 2602.01034 (Discovering Process-Outcome Credit) ✓
15. arXiv 2601.18984 (VPPO / Save the Good Prefix) ✓
16. arXiv 2509.21154 (GRPO is Secretly a PRM, ICLR 2026) ✓
17. DAPO ✓
18. Reward Under Attack (arXiv 2603.06621) ✓
19. ConfClip (arXiv 2509.17730) — 新增 ✓
20. Qwen2.5-Math-PRM-7B, Qwen3-8B, Qwen3-1.7B ✓
21. MATH-500, AMC23, AIME 2024, AIME 2025, OlympiadBench, MinervaMath ✓

【下一轮 proposal（纯净版，将原样传给 worker）】:
---
# Uncertainty-Gated Credit Assignment for Process-Supervised Mathematical Reasoning RL

## Core Problem

Process-aware RL methods (PURE, GRPO-λ, PRL, PRPO, PROGRS) treat PRM step-level scores as equally trustworthy or apply only trajectory-level corrections, yet PRMs are demonstrably miscalibrated—overestimating success on uncertain steps—leading to reward hacking where the policy exploits unreliable PRM signals. Two distinct bias sources compound this problem: (a) PRM miscalibration bias—PRM scores deviate from true step correctness probabilities, varying in severity across step types (e.g., well-calibrated on computational steps but poorly calibrated on conceptual reasoning); (b) aggregation bias—structural artifacts of the credit assignment form itself (e.g., min-form's conservative lower-bound effect). Existing methods address neither bias source adaptively at the per-step level. The per-step heterogeneity of PRM calibration quality means that global or trajectory-level corrections cannot fully resolve (a)—adaptive per-step treatment is necessary.

## Research Opportunity

PRM calibration methods have matured rapidly (quantile regression [Park et al., NeurIPS 2025], conditional optimal transport [arXiv 2605.06785]) but are applied exclusively to test-time scaling. PROGRS (arXiv Apr 2026) brings a calibrated PRM into RL training but applies trajectory-level outcome-conditioned centering—a deterministic rule that does not use per-step uncertainty information. No work uses PRM per-step calibration confidence to adaptively gate credit assignment during RL training. Jia et al. [ICML 2025] proved outcome supervision is statistically no harder than process supervision, ensuring fallback to outcome credit preserves learning guarantees. This frames a principled bias-variance tradeoff: process credit provides low-variance but potentially biased (when PRM is miscalibrated) signal; outcome credit is unbiased but high-variance (sparse, trajectory-level). The optimal per-step interpolation depends on local PRM reliability—precisely what calibrated confidence intervals quantify.

## Research Landscape

We organize the design space along two axes—**signal source** (what drives credit allocation) and **granularity** (per-step vs. trajectory-level)—yielding four quadrants:

| | Per-step | Trajectory-level |
|---|---|---|
| **Verifier calibration** | **UGCA (ours)** | PROGRS |
| **Intrinsic / structural** | Process-Outcome Credit (arXiv 2602.01034) | GRPO, DAPO |

**Process-aware RL (uniform PRM trust).** PURE (NeurIPS 2025) replaces summation-form with min-form credit assignment (82.6% MATH-500, 82.5% AMC23 on Qwen2.5-Math-7B) but assumes PRM scores are reliable. GRPO-λ (arXiv 2510.00194, ICLR 2026) adds eligibility traces to GRPO, improving math scores by 3–4.5 points on 7B models but trusts PRM outputs uniformly. PRPO (arXiv Jan 2026) aligns process and outcome advantages via location-parameter shift on Qwen2.5-Math-1.5B (61.2→64.4% MATH-500) using fixed structural alignment. PRL (arXiv 2026) improves reasoning through process reward learning without conditioning on PRM reliability. PRIME (arXiv Feb 2025) enables online PRM updates through implicit process rewards but uses uniform trust in PRM signals.

**Calibrated PRM in RL (trajectory-level).** PROGRS (arXiv 2604.02341, Apr 2026) uses outcome-conditioned centering with a frozen quantile-regression PRM (74.9% MATH-500 vs 69.7% DAPO), shifting incorrect-trajectory PRM scores to zero mean within each prompt group. This addresses systematic PRM bias at trajectory level but does not use per-step uncertainty information—all steps within a trajectory receive the same centering treatment regardless of individual calibration quality.

**Per-step process-outcome mixing (non-uncertainty-based).** "Discovering Process-Outcome Credit" (arXiv 2602.01034) proposes Step-wise Marginal Information Gain + Decoupled Masking for per-step process-outcome credit mixing via Monte Carlo estimation of intrinsic information gain—computationally heavier (requiring additional MC rollouts) and subject to higher estimation variance than calibration-derived uncertainty. VPPO / "Save the Good Prefix" (arXiv 2601.18984) uses PRM to localize the first error step and applies binary prefix reward + suffix penalty—a degenerate (hard) form of per-step gating that cannot gracefully handle PRM uncertainty on ambiguous steps.

**Implicit process credit in GRPO.** Sullivan et al. (arXiv 2509.21154, ICLR 2026) prove GRPO + ORM under shared-prefix conditions is equivalent to PRM-aware RL with a Monte-Carlo-based implicit PRM. This implies vanilla GRPO already carries implicit process credit, but this credit is uniform across steps—not adaptive to PRM confidence. UGCA provides the missing per-step adaptivity.

**Confidence-based reward modulation.** UCAS (arXiv Oct 2025) modulates advantages via the policy model's own logit uncertainty. ConfClip (arXiv 2509.17730) uses policy model confidence to weight rewards in RLVR. Uncertainty-Aware Reward Discounting (arXiv Apr 2026) uses ensemble disagreement for reward modulation in general RLHF. All three use policy-side or ensemble-based uncertainty signals that shift with training, whereas UGCA uses an external frozen verifier's calibrated uncertainty—stable, independent of policy training dynamics, and specifically designed to interpolate between process and outcome credit sources rather than simply scaling rewards.

**PRM calibration.** Park et al. (NeurIPS 2025) introduce quantile-regression calibration for PRMs. Distributional PRM (arXiv 2605.06785, May 2026) achieves state-of-the-art calibration via conditional optimal transport, targeting only test-time scaling. PathFinder-PRM (arXiv May 2025) achieves 67.7 PRMScore on PRMBench with error-type-aware scoring but does not feed uncertainty into RL. TP-GRPO (arXiv Jul 2025) uses generative PRM at the thought level with intrinsic signals, not PRM calibration.

**PRM vulnerability.** "Reward Under Attack" (arXiv 2603.06621) demonstrates PRMs are systematically exploitable as "fluency detectors"—achieving PRM scores >0.9 while ground-truth accuracy <4% under adversarial RL optimization—directly motivating uncertainty-aware trust in PRM signals.

**Gap.** The specific combination—per-step PRM calibration confidence driving adaptive process-outcome credit interpolation during RL training, framed as an uncertainty-driven bias-variance tradeoff—remains unaddressed.

## Proposed Approach

UGCA frames credit assignment as a per-step bias-variance tradeoff. Process credit (PURE-style min-form advantage A^min) provides dense, low-variance signal but inherits PRM miscalibration bias—distinct from the structural aggregation bias of min-form itself, which UGCA does not claim to resolve. Outcome credit (GRPO group-relative advantage A^GRPO) is unbiased (based on verifiable correctness) but high-variance (sparse, trajectory-level). The key insight is separating what the verifier predicts (PRM score) from how confident the verifier is (calibrated confidence interval width)—the former determines the reward signal, the latter determines how much to trust it.

We equip the off-the-shelf Qwen2.5-Math-PRM-7B with calibrated confidence intervals via quantile regression (adapting open-source code from Park et al., NeurIPS 2025), then define a per-step gating coefficient α_i = σ(−(w_i − τ)/β) based on each step's confidence-interval width w_i. The advantage at step i is A_i = α_i · A^min_i + (1 − α_i) · A^GRPO_i: high-confidence PRM steps (small w_i, high α) lean on low-variance process credit; uncertain steps (large w_i, low α) gracefully degrade to unbiased outcome credit.

**Why not simpler alternatives?** (1) Using raw PRM score magnitude as gating signal conflates "the PRM thinks this step is correct" with "the PRM is confident about this step"—a PRM can produce narrow, high-confidence intervals around a wrong prediction. Calibrated CI width separates prediction from confidence. (2) Global clipping/truncation of low-confidence PRM scores discards useful information on partially confident steps. (3) PROGRS's trajectory-level centering treats all steps within a trajectory uniformly despite heterogeneous per-step calibration quality.

**Theoretical grounding.** (1) Jia et al. (ICML 2025) prove outcome supervision is statistically no harder than process supervision, ensuring degradation to outcome credit preserves learning guarantees. (2) Under simplifying assumptions (Gaussian noise on PRM scores with variance proportional to w_i²), the MSE-optimal interpolation weight takes a sigmoid-like form in w_i (formal derivation in appendix), providing a prescriptive justification for the gating function form.

## Experimental Design

**Models.** Qwen3-8B and Qwen3-1.7B, trained on MATH training set (8K prompts) using modified GRPO objective atop PURE codebase with veRL framework. Calibrated PRM frozen throughout.

**Baselines.** 8B: GRPO, DAPO, PURE, GRPO-λ, PROGRS (5 baselines). 1.7B: all 8B baselines + PRPO + VPPO (7 baselines), providing complete coverage of fixed process-outcome mixing strategies (PRPO: parametric shift; VPPO: binary first-error gating).

**Benchmarks.** MATH-500, AMC23, AIME 2024, AIME 2025, OlympiadBench, MinervaMath. Pass@1 as primary metric; Pass@8 on AIME benchmarks to increase statistical power (30-problem sets).

**Reward hacking quantification.**
- PRM-Accuracy Gap (PAG): periodic rollout sampling during training, plotting mean PRM score vs. ground-truth pass rate as overoptimization curves.
- Per-step uncertainty-conditioned accuracy: steps binned by w_i into 5 quantile bins, reporting per-bin step correctness.
- Reward hacking rate: proportion of trajectories where PRM score > threshold but final answer incorrect.

**Core assumption validation.** Per-step w_i quantile bins with PRM step-level prediction accuracy (not just policy correctness): if narrow-w_i bins show higher PRM accuracy, the core assumption (CI width proxies PRM reliability) is confirmed. Report Spearman rank correlation between w_i and PRM prediction error.

**Longitudinal PRM calibration tracking.** At every 25% training progress checkpoint, compute ECE and Brier score of frozen PRM on freshly sampled rollouts. Plot calibration quality vs. training progress and gating coefficient α distribution drift. If significant degradation detected, discuss periodic re-calibration as mitigation.

**Cross-family PRM validation.** ECE and Brier score of calibrated Qwen2.5-Math-PRM-7B on Qwen3-8B initial rollouts vs. Qwen2.5 rollouts. If significant degradation, perform additional quantile calibration fine-tuning on Qwen3 data.

**Ablation studies (Qwen3-1.7B, 3 seeds each).**
- Boundary cases: α≡1 (pure PURE) and α≡0 (pure GRPO).
- Hard vs. soft gating: binary threshold (α∈{0,1}) vs. sigmoid.
- Raw PRM score gating: α_i = σ(PRM_score_i) vs. calibrated CI width gating.
- Calibrated vs. uncalibrated: raw PRM score variance as uncertainty proxy vs. calibrated CI width.
- Hyperparameters: threshold τ, temperature β, quantile level.

**Statistical rigor.** 1.7B: 3 seeds, mean ± std. 8B: top 2 configs × 3 seeds + evaluation-level bootstrap CIs (1000 resamples).

**Compute fairness.** Per-method training wall-clock time and FLOPs. PRM calibration cost as separate one-time overhead. Accuracy-vs-compute Pareto curves. Theoretical FLOPs comparison with "Discovering Process-Outcome Credit" (arXiv 2602.01034) to justify not running as direct baseline (MC estimation overhead makes compute-normalized comparison unfavorable).

## Broader Significance

UGCA instantiates a general principle—Verifier-Uncertainty-Aware RL: when training with imperfect verifiers, credit assignment should adapt to per-instance verifier confidence. Math reasoning is a clean testbed where PRM uncertainty is measurable and calibratable. The framework generalizes to any domain with imperfect step-level verifiers (code generation, scientific reasoning, agentic tasks). We scope experiments to math reasoning and leave cross-domain validation as future work.

## Key References

- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (NeurIPS 2025)
- GRPO-λ / GRPO is Secretly a Process Reward Model (arXiv 2510.00194 / arXiv 2509.21154, ICLR 2026)
- LLM Reasoning with Process Rewards for Outcome-Guided Steps [PROGRS] (arXiv 2604.02341, 2026)
- Discovering Process-Outcome Credit in Multi-Step LLM Reasoning (arXiv 2602.01034, 2026)
- Save the Good Prefix: Precise Error Penalization via Process-Supervised RL [VPPO] (arXiv 2601.18984, 2026)
- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (Park et al., NeurIPS 2025)
- Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport (arXiv 2605.06785, 2026)
- Do We Need to Verify Step by Step? Rethinking Process Supervision from a Theoretical Perspective (Jia et al., ICML 2025)
- Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping [UCAS] (arXiv 2025)
- ConfClip: Confidence-Weighted and Clipped Reward for RL in LLMs (arXiv 2509.17730, 2025)
- PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization (arXiv 2026)
- PRL: Process Reward Learning Improves LLMs' Reasoning Ability (arXiv 2026)
- Error Typing for Smarter Rewards [PathFinder-PRM] (arXiv 2025)
- Process Reinforcement through Implicit Rewards [PRIME] (arXiv 2025)
- Uncertainty-Aware Reward Discounting (arXiv Apr 2026)
- Reward Under Attack: Analyzing Robustness and Hackability of PRMs (arXiv 2603.06621, 2026)
- DAPO: An Open-Source LLM Reinforcement Learning System at Scale (2025)
- Good Learners Think Their Thinking [TP-GRPO] (arXiv Jul 2025)

## Resource Estimate

- **GPU compute**: ~2900 H100-hours (PRM quantile calibration: 100h; cross-family validation: 20h; Qwen3-1.7B ablations + baselines ~14 configs × 3 seeds: 840h; Qwen3-8B comparison 6 configs (top 2 × 3 seeds + 4 × 1 seed): 1600h; PROGRS/GRPO-λ reproduction development: 80h; DAPO/PROGRS/extra baseline runs: 200h; evaluation + diagnostics: 60h)
- **Timeline**: 8 weeks (wk1–2: PRM calibration + cross-family validation + PURE/veRL integration + PROGRS core reproduction; wk3–4: 1.7B full ablation sweep + PRPO/VPPO baselines + core assumption validation; wk5–6: 8B runs vs all baselines + longitudinal calibration tracking; wk7: reward-hacking analysis, PAG curves, Pareto curves, per-step visualization; wk8: paper writing and submission)
- **Estimated GPU cost**: ~$7,250 (H100 spot ~$2.50/hr)
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16c9513b-8dcf-4289-9181-71986aa8843f",
  "isSidechain": false,
  "requestId": "req_011CbSm4pjSB7WS8Jf5rPMRv",
  "type": "assistant",
  "uuid": "835c0f49-2740-4a5e-a558-9d7ff9d76251",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019xqDS3wsLYFWa3aD4jMzkD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 920,
      "cache_read_input_tokens": 60672,
      "output_tokens": 10109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10109,
          "cache_read_input_tokens": 60672,
          "cache_creation_input_tokens": 920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 920
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

_source line 59_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research context. Let me synthesize my findings and produce the assessment.  ---  【状态…",
  "leafUuid": "835c0f49-2740-4a5e-a558-9d7ff9d76251",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research context. Let me synthesize my findings and produce the assessment.  ---  【状态…",
  "leafUuid": "835c0f49-2740-4a5e-a558-9d7ff9d76251",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 64 · 2026-05-27T08:34:01.288Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:34:01.288Z",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "content": "【引用修复】你刚输出的 proposal 纯净版遗漏了以下原文中存在的引用：\n- AAAI 2027\n\n请重新输出完整的纯净版 proposal，确保上述引用全部包含在内。只输出 --- 包围的纯净版 proposal，不要输出其他内容。"
}
```

---

### Runtime record

_source line 65 · 2026-05-27T08:34:01.289Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:34:01.289Z",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

## Round 4

8 recorded events

### User

_source line 66 · 2026-05-27T08:34:01.346Z_

【引用修复】你刚输出的 proposal 纯净版遗漏了以下原文中存在的引用：
- AAAI 2027

请重新输出完整的纯净版 proposal，确保上述引用全部包含在内。只输出 --- 包围的纯净版 proposal，不要输出其他内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "835c0f49-2740-4a5e-a558-9d7ff9d76251",
  "isSidechain": false,
  "promptId": "23088c65-502f-447e-8e51-f40b85f46070",
  "type": "user",
  "uuid": "cf32369f-fd79-402e-8597-2b239fccfd18",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-27T08:34:05.313Z_

<details><summary>Logged reasoning block</summary>

```text
The user is pointing out that I missed the reference to "AAAI 2027 (deadline: July 28, 2026)" which was in the original proposal. Let me add it back into the Research Opportunity section where it originally appeared. Let me re-output the full clean proposal with this reference included.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf32369f-fd79-402e-8597-2b239fccfd18",
  "isSidechain": false,
  "requestId": "req_011CbSmMHvzys37bbK2TNR2L",
  "type": "assistant",
  "uuid": "2c1c7951-b77a-4c1e-a01e-4243fd279413",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAKWwLkA8VFH3P7Y7qUENJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10209,
      "cache_read_input_tokens": 61592,
      "output_tokens": 4301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4301,
          "cache_read_input_tokens": 61592,
          "cache_creation_input_tokens": 10209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10209
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

_source line 68 · 2026-05-27T08:34:49.676Z_

---
# Uncertainty-Gated Credit Assignment for Process-Supervised Mathematical Reasoning RL

## Core Problem

Process-aware RL methods (PURE, GRPO-λ, PRL, PRPO, PROGRS) treat PRM step-level scores as equally trustworthy or apply only trajectory-level corrections, yet PRMs are demonstrably miscalibrated—overestimating success on uncertain steps—leading to reward hacking where the policy exploits unreliable PRM signals. Two distinct bias sources compound this problem: (a) PRM miscalibration bias—PRM scores deviate from true step correctness probabilities, varying in severity across step types (e.g., well-calibrated on computational steps but poorly calibrated on conceptual reasoning); (b) aggregation bias—structural artifacts of the credit assignment form itself (e.g., min-form's conservative lower-bound effect). Existing methods address neither bias source adaptively at the per-step level. The per-step heterogeneity of PRM calibration quality means that global or trajectory-level corrections cannot fully resolve (a)—adaptive per-step treatment is necessary.

## Research Opportunity

PRM calibration methods have matured rapidly (quantile regression [Park et al., NeurIPS 2025], conditional optimal transport [arXiv 2605.06785]) but are applied exclusively to test-time scaling. PROGRS (arXiv Apr 2026) brings a calibrated PRM into RL training but applies trajectory-level outcome-conditioned centering—a deterministic rule that does not use per-step uncertainty information. No work uses PRM per-step calibration confidence to adaptively gate credit assignment during RL training. Jia et al. [ICML 2025] proved outcome supervision is statistically no harder than process supervision, ensuring fallback to outcome credit preserves learning guarantees. This frames a principled bias-variance tradeoff: process credit provides low-variance but potentially biased (when PRM is miscalibrated) signal; outcome credit is unbiased but high-variance (sparse, trajectory-level). The optimal per-step interpolation depends on local PRM reliability—precisely what calibrated confidence intervals quantify. The building blocks (calibrated PRMs, GRPO/PURE training pipelines, math reasoning benchmarks) all exist, making a 2-month implementation feasible for AAAI 2027 (deadline: July 28, 2026).

## Research Landscape

We organize the design space along two axes—**signal source** (what drives credit allocation) and **granularity** (per-step vs. trajectory-level)—yielding four quadrants:

| | Per-step | Trajectory-level |
|---|---|---|
| **Verifier calibration** | **UGCA (ours)** | PROGRS |
| **Intrinsic / structural** | Process-Outcome Credit (arXiv 2602.01034) | GRPO, DAPO |

**Process-aware RL (uniform PRM trust).** PURE (NeurIPS 2025) replaces summation-form with min-form credit assignment (82.6% MATH-500, 82.5% AMC23 on Qwen2.5-Math-7B) but assumes PRM scores are reliable. GRPO-λ (arXiv 2510.00194, ICLR 2026) adds eligibility traces to GRPO, improving math scores by 3–4.5 points on 7B models but trusts PRM outputs uniformly. PRPO (arXiv Jan 2026) aligns process and outcome advantages via location-parameter shift on Qwen2.5-Math-1.5B (61.2→64.4% MATH-500) using fixed structural alignment. PRL (arXiv 2026) improves reasoning through process reward learning without conditioning on PRM reliability. PRIME (arXiv Feb 2025) enables online PRM updates through implicit process rewards but uses uniform trust in PRM signals.

**Calibrated PRM in RL (trajectory-level).** PROGRS (arXiv 2604.02341, Apr 2026) uses outcome-conditioned centering with a frozen quantile-regression PRM (74.9% MATH-500 vs 69.7% DAPO), shifting incorrect-trajectory PRM scores to zero mean within each prompt group. This addresses systematic PRM bias at trajectory level but does not use per-step uncertainty information—all steps within a trajectory receive the same centering treatment regardless of individual calibration quality.

**Per-step process-outcome mixing (non-uncertainty-based).** "Discovering Process-Outcome Credit" (arXiv 2602.01034) proposes Step-wise Marginal Information Gain + Decoupled Masking for per-step process-outcome credit mixing via Monte Carlo estimation of intrinsic information gain—computationally heavier (requiring additional MC rollouts) and subject to higher estimation variance than calibration-derived uncertainty. VPPO / "Save the Good Prefix" (arXiv 2601.18984) uses PRM to localize the first error step and applies binary prefix reward + suffix penalty—a degenerate (hard) form of per-step gating that cannot gracefully handle PRM uncertainty on ambiguous steps.

**Implicit process credit in GRPO.** Sullivan et al. (arXiv 2509.21154, ICLR 2026) prove GRPO + ORM under shared-prefix conditions is equivalent to PRM-aware RL with a Monte-Carlo-based implicit PRM. This implies vanilla GRPO already carries implicit process credit, but this credit is uniform across steps—not adaptive to PRM confidence. UGCA provides the missing per-step adaptivity.

**Confidence-based reward modulation.** UCAS (arXiv Oct 2025) modulates advantages via the policy model's own logit uncertainty. ConfClip (arXiv 2509.17730) uses policy model confidence to weight rewards in RLVR. Uncertainty-Aware Reward Discounting (arXiv Apr 2026) uses ensemble disagreement for reward modulation in general RLHF. All three use policy-side or ensemble-based uncertainty signals that shift with training, whereas UGCA uses an external frozen verifier's calibrated uncertainty—stable, independent of policy training dynamics, and specifically designed to interpolate between process and outcome credit sources rather than simply scaling rewards.

**PRM calibration.** Park et al. (NeurIPS 2025) introduce quantile-regression calibration for PRMs. Distributional PRM (arXiv 2605.06785, May 2026) achieves state-of-the-art calibration via conditional optimal transport, targeting only test-time scaling. PathFinder-PRM (arXiv May 2025) achieves 67.7 PRMScore on PRMBench with error-type-aware scoring but does not feed uncertainty into RL. TP-GRPO (arXiv Jul 2025) uses generative PRM at the thought level with intrinsic signals, not PRM calibration.

**PRM vulnerability.** "Reward Under Attack" (arXiv 2603.06621) demonstrates PRMs are systematically exploitable as "fluency detectors"—achieving PRM scores >0.9 while ground-truth accuracy <4% under adversarial RL optimization—directly motivating uncertainty-aware trust in PRM signals.

**Gap.** The specific combination—per-step PRM calibration confidence driving adaptive process-outcome credit interpolation during RL training, framed as an uncertainty-driven bias-variance tradeoff—remains unaddressed.

## Proposed Approach

UGCA frames credit assignment as a per-step bias-variance tradeoff. Process credit (PURE-style min-form advantage A^min) provides dense, low-variance signal but inherits PRM miscalibration bias—distinct from the structural aggregation bias of min-form itself, which UGCA does not claim to resolve. Outcome credit (GRPO group-relative advantage A^GRPO) is unbiased (based on verifiable correctness) but high-variance (sparse, trajectory-level). The key insight is separating what the verifier predicts (PRM score) from how confident the verifier is (calibrated confidence interval width)—the former determines the reward signal, the latter determines how much to trust it.

We equip the off-the-shelf Qwen2.5-Math-PRM-7B with calibrated confidence intervals via quantile regression (adapting open-source code from Park et al., NeurIPS 2025), then define a per-step gating coefficient α_i = σ(−(w_i − τ)/β) based on each step's confidence-interval width w_i. The advantage at step i is A_i = α_i · A^min_i + (1 − α_i) · A^GRPO_i: high-confidence PRM steps (small w_i, high α) lean on low-variance process credit; uncertain steps (large w_i, low α) gracefully degrade to unbiased outcome credit.

**Why not simpler alternatives?** (1) Using raw PRM score magnitude as gating signal conflates "the PRM thinks this step is correct" with "the PRM is confident about this step"—a PRM can produce narrow, high-confidence intervals around a wrong prediction. Calibrated CI width separates prediction from confidence. (2) Global clipping/truncation of low-confidence PRM scores discards useful information on partially confident steps. (3) PROGRS's trajectory-level centering treats all steps within a trajectory uniformly despite heterogeneous per-step calibration quality.

**Theoretical grounding.** (1) Jia et al. (ICML 2025) prove outcome supervision is statistically no harder than process supervision, ensuring degradation to outcome credit preserves learning guarantees. (2) Under simplifying assumptions (Gaussian noise on PRM scores with variance proportional to w_i²), the MSE-optimal interpolation weight takes a sigmoid-like form in w_i (formal derivation in appendix), providing a prescriptive justification for the gating function form.

## Experimental Design

**Models.** Qwen3-8B and Qwen3-1.7B, trained on MATH training set (8K prompts) using modified GRPO objective atop PURE codebase with veRL framework. Calibrated PRM frozen throughout.

**Baselines.** 8B: GRPO, DAPO, PURE, GRPO-λ, PROGRS (5 baselines). 1.7B: all 8B baselines + PRPO + VPPO (7 baselines), providing complete coverage of fixed process-outcome mixing strategies (PRPO: parametric shift; VPPO: binary first-error gating).

**Benchmarks.** MATH-500, AMC23, AIME 2024, AIME 2025, OlympiadBench, MinervaMath. Pass@1 as primary metric; Pass@8 on AIME benchmarks to increase statistical power (30-problem sets).

**Reward hacking quantification.**
- PRM-Accuracy Gap (PAG): periodic rollout sampling during training, plotting mean PRM score vs. ground-truth pass rate as overoptimization curves.
- Per-step uncertainty-conditioned accuracy: steps binned by w_i into 5 quantile bins, reporting per-bin step correctness.
- Reward hacking rate: proportion of trajectories where PRM score > threshold but final answer incorrect.

**Core assumption validation.** Per-step w_i quantile bins with PRM step-level prediction accuracy (not just policy correctness): if narrow-w_i bins show higher PRM accuracy, the core assumption (CI width proxies PRM reliability) is confirmed. Report Spearman rank correlation between w_i and PRM prediction error.

**Longitudinal PRM calibration tracking.** At every 25% training progress checkpoint, compute ECE and Brier score of frozen PRM on freshly sampled rollouts. Plot calibration quality vs. training progress and gating coefficient α distribution drift. If significant degradation detected, discuss periodic re-calibration as mitigation.

**Cross-family PRM validation.** ECE and Brier score of calibrated Qwen2.5-Math-PRM-7B on Qwen3-8B initial rollouts vs. Qwen2.5 rollouts. If significant degradation, perform additional quantile calibration fine-tuning on Qwen3 data.

**Ablation studies (Qwen3-1.7B, 3 seeds each).**
- Boundary cases: α≡1 (pure PURE) and α≡0 (pure GRPO).
- Hard vs. soft gating: binary threshold (α∈{0,1}) vs. sigmoid.
- Raw PRM score gating: α_i = σ(PRM_score_i) vs. calibrated CI width gating.
- Calibrated vs. uncalibrated: raw PRM score variance as uncertainty proxy vs. calibrated CI width.
- Hyperparameters: threshold τ, temperature β, quantile level.

**Statistical rigor.** 1.7B: 3 seeds, mean ± std. 8B: top 2 configs × 3 seeds + evaluation-level bootstrap CIs (1000 resamples).

**Compute fairness.** Per-method training wall-clock time and FLOPs. PRM calibration cost as separate one-time overhead. Accuracy-vs-compute Pareto curves. Theoretical FLOPs comparison with "Discovering Process-Outcome Credit" (arXiv 2602.01034) to justify not running as direct baseline (MC estimation overhead makes compute-normalized comparison unfavorable).

## Broader Significance

UGCA instantiates a general principle—Verifier-Uncertainty-Aware RL: when training with imperfect verifiers, credit assignment should adapt to per-instance verifier confidence. Math reasoning is a clean testbed where PRM uncertainty is measurable and calibratable. The framework generalizes to any domain with imperfect step-level verifiers (code generation, scientific reasoning, agentic tasks). We scope experiments to math reasoning and leave cross-domain validation as future work.

## Key References

- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (NeurIPS 2025)
- GRPO-λ / GRPO is Secretly a Process Reward Model (arXiv 2510.00194 / arXiv 2509.21154, ICLR 2026)
- LLM Reasoning with Process Rewards for Outcome-Guided Steps [PROGRS] (arXiv 2604.02341, 2026)
- Discovering Process-Outcome Credit in Multi-Step LLM Reasoning (arXiv 2602.01034, 2026)
- Save the Good Prefix: Precise Error Penalization via Process-Supervised RL [VPPO] (arXiv 2601.18984, 2026)
- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (Park et al., NeurIPS 2025)
- Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport (arXiv 2605.06785, 2026)
- Do We Need to Verify Step by Step? Rethinking Process Supervision from a Theoretical Perspective (Jia et al., ICML 2025)
- Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping [UCAS] (arXiv 2025)
- ConfClip: Confidence-Weighted and Clipped Reward for RL in LLMs (arXiv 2509.17730, 2025)
- PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization (arXiv 2026)
- PRL: Process Reward Learning Improves LLMs' Reasoning Ability (arXiv 2026)
- Error Typing for Smarter Rewards [PathFinder-PRM] (arXiv 2025)
- Process Reinforcement through Implicit Rewards [PRIME] (arXiv 2025)
- Uncertainty-Aware Reward Discounting (arXiv Apr 2026)
- Reward Under Attack: Analyzing Robustness and Hackability of PRMs (arXiv 2603.06621, 2026)
- DAPO: An Open-Source LLM Reinforcement Learning System at Scale (2025)
- Good Learners Think Their Thinking [TP-GRPO] (arXiv Jul 2025)

## Resource Estimate

- **GPU compute**: ~2900 H100-hours (PRM quantile calibration: 100h; cross-family validation: 20h; Qwen3-1.7B ablations + baselines ~14 configs × 3 seeds: 840h; Qwen3-8B comparison 6 configs (top 2 × 3 seeds + 4 × 1 seed): 1600h; PROGRS/GRPO-λ reproduction development: 80h; DAPO/PROGRS/extra baseline runs: 200h; evaluation + diagnostics: 60h)
- **Timeline**: 8 weeks (wk1–2: PRM calibration + cross-family validation + PURE/veRL integration + PROGRS core reproduction; wk3–4: 1.7B full ablation sweep + PRPO/VPPO baselines + core assumption validation; wk5–6: 8B runs vs all baselines + longitudinal calibration tracking; wk7: reward-hacking analysis, PAG curves, Pareto curves, per-step visualization; wk8: paper writing and submission)
- **Estimated GPU cost**: ~$7,250 (H100 spot ~$2.50/hr)
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c1c7951-b77a-4c1e-a01e-4243fd279413",
  "isSidechain": false,
  "requestId": "req_011CbSmMHvzys37bbK2TNR2L",
  "type": "assistant",
  "uuid": "95d39eb5-ad6b-4b36-b5b3-178f88b3a43b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAKWwLkA8VFH3P7Y7qUENJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10209,
      "cache_read_input_tokens": 61592,
      "output_tokens": 4301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4301,
          "cache_read_input_tokens": 61592,
          "cache_creation_input_tokens": 10209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10209
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

_source line 69_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【引用修复】你刚输出的 proposal 纯净版遗漏了以下原文中存在的引用： - AAAI 2027  请重新输出完整的纯净版 proposal，确保上述引用全部包含在内。只输出 --- 包围的纯净版 proposal，不要输出其他内容。",
  "leafUuid": "95d39eb5-ad6b-4b36-b5b3-178f88b3a43b",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 70_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 72 · 2026-05-27T08:41:29.122Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:41:29.122Z",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "content": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nNow I have sufficient research context. Let me synthesize my findings and provide my assessment.\n\n---\n\n【状态】: 有发掘空间\n\n【前置调研发现】\n- **PROGRS** (arXiv 2604.02341, Apr 2026): 使用 outcome-conditioned centering + frozen quantile-regression PRM，但 centering 是 trajectory-level 的，所有 step 接受相同处理。与 UGCA 的核心差异（per-step adaptive gating）确认属实。\n- **\"Discovering Process-Outcome Credit\"** (arXiv 2602.01034, Feb 2026): 提出 Step-wise Marginal Information Gain (MIG) + Decoupled Masking 实现 per-step process-outcome mixing，但基于 Monte Carlo 估计的 intrinsic information gain，不是 calibration-derived uncertainty。这是 UGCA 在 per-step 维度上最近的竞争者，差异在于信号来源（intrinsic vs. verifier calibration）。\n- **\"From Reasoning to Agentic\" credit assignment survey** (arXiv 2604.09459, Apr 2026): 组织 47 种 CA 方法的 taxonomy（granularity × methodology），未识别出任何使用 PRM calibration confidence 做 per-step credit gating 的方法，确认 UGCA 占据的位置（verifier calibration × per-step）在现有文献中为空白。\n- **UCAS** (arXiv 2510.10649, Oct 2025): 使用 policy model 自身 logit uncertainty 做 advantage shaping，信号源是 policy-side 的（随训练漂移），与 UGCA 使用 frozen external verifier 的 calibrated uncertainty 有本质区别。\n- **\"Reward Under Attack\"** (arXiv 2603.06621, Mar 2026): 证明 PRMs 可被系统性 exploit 为 \"fluency detectors\"（PRM score >0.9 但 accuracy <4%），直接支撑 UGCA 的 motivation。\n- **CAPO** (arXiv 2508.02298, Aug 2025): 用 LLM-as-GenPRM 做 token-level generative credit assignment，属于 model-based 方法，与 calibration-based 方法正交。\n- **Jia et al.** (ICML 2025, arXiv 2502.10581): 理论证明 outcome supervision 不比 process supervision 更难，为 UGCA 的 fallback guarantee 提供基础。\n- 调研总结：这个领域当前的研究者沿两条主线突破——(1) 更精细的 per-step credit assignment（从 trajectory-level 到 step-level 到 token-level），(2) 更可靠的 PRM 信号（calibration、robustness、generative verification）。但这两条线目前是**分离的**：做 per-step credit 的工作不关注 verifier reliability，做 PRM calibration 的工作只用于 test-time scaling 或 trajectory-level RL。UGCA 的核心贡献在于**交叉这两条线**，这个定位是真实的、有价值的。\n\n---\n\n【发掘点 1】\n- 维度: 核心 claim 强化\n- 内容: 将 reward hacking robustness 从\"实验观测\"提升为\"方法的结构性属性\"。当前 proposal 将 reward hacking quantification（PAG curves、reward hacking rate）定位为实验分析项。但 UGCA 的设计提供了一个更强的 claim：**当 PRM 被 exploit 时（在 adversarial policy 行为上给出高分），如果 calibration 是良好的，这些 out-of-distribution 输入上的 CI 应当变宽——UGCA 自动 down-weight 这些不可靠信号**。这不是一个需要事后验证的经验发现，而是方法设计的内在属性。建议在 \"Proposed Approach\" 或 \"Broader Significance\" 中增加一个显式的 claim：UGCA 提供了**对 PRM reward hacking 的 calibration-mediated implicit defense**，并在实验中用 PAG curves 对比 UGCA vs. baselines 的 overoptimization 速率来验证。这将 \"Reward Under Attack\" 的 motivation 和 UGCA 的 mechanism 形成闭环，而不仅仅是 citing 一篇 motivation paper。\n- 价值: 这直接提升 Significance——从\"更好的 credit assignment\"拓展到\"structurally robust credit assignment\"。Reward hacking 是 2025-2026 RL 社区的高关注问题（\"Reward Under Attack\" 3月才出来），把 UGCA 定位为 principled defense mechanism 而非仅仅 better accuracy，大幅提升 impact narrative。审稿人对 \"reward hacking robustness\" 的兴趣远高于 \"又多了 1-2 个点 accuracy\"。\n- 调研依据: 直接参考 \"Reward Under Attack\" (arXiv 2603.06621) 的发现——PRMs 在 adversarial RL 中退化为 fluency detectors。UGCA 的 calibrated CI gating 正好 target 这个 failure mode：calibration 在 OOD 输入上天然产生更宽的 CI。\n\n【发掘点 2】\n- 维度: novelty 锐化\n- 内容: 将 appendix 中的 MSE-optimal interpolation weight 推导提升为 main paper 的理论贡献。当前 proposal 在 \"Theoretical grounding\" 中提到\"under simplifying assumptions (Gaussian noise on PRM scores with variance proportional to w_i²), the MSE-optimal interpolation weight takes a sigmoid-like form in w_i (formal derivation in appendix)\"。这实际上是一个相当有力的结果——它说明 sigmoid gating 不是一个 ad hoc design choice，而是**MSE-optimal estimator 的 parametric approximation**。建议将其从 appendix 提升到 main paper 的 Section 3（方法部分），以 Proposition 形式给出：在 PRM score = true correctness + Gaussian noise(0, σ²(w_i)) 的模型下，最小化 per-step credit assignment MSE 的 optimal interpolation weight 是 w_i 的单调递减函数，sigmoid 是其 parametric family。这将 UGCA 从 \"an intuitive per-step gating heuristic\" 提升为 \"a principled approximation to the MSE-optimal credit assignment under verifier uncertainty\"。\n- 价值: 直接提升 Novelty 的理论层次。Math reasoning RL 领域的论文大多是 empirical，一个有 prescriptive justification 的方法设计（不是 post-hoc 解释）在 AAAI 审稿中是显著加分项。同时也堵住了审稿人可能的质疑：\"why sigmoid? why not other gating forms?\"——因为 sigmoid 是理论最优解的近似。\n- 调研依据: 基于领域整体趋势判断——近期 credit assignment 方法（GRPO-λ、PURE、VPPO）大多缺乏理论 justification for design choices，审稿人经常在 reviews 中问 \"why this specific form\"。有理论支撑的设计选择在该领域是稀缺的差异化优势。\n\n【发掘点 3】\n- 维度: significance 提升\n- 内容: 更显式地利用 credit assignment survey (arXiv 2604.09459) 的 taxonomy 来定位 UGCA 的 contribution。Proposal 中已有 2×2 表格（signal source × granularity），但可以更直接地 cite 这篇 survey 并指出：在 survey 识别的 5 种 methodology categories（Monte Carlo, temporal difference, model-based, game-theoretic, information-theoretic）中，UGCA 开创了第 6 种——**calibration-based** credit assignment，即信号不来自 rollout estimation（MC）、value function（TD）、generative model（model-based）、contribution attribution（game-theoretic）或 mutual information（information-theoretic），而来自 verifier calibration quality。这不仅填了一个 empirical gap，更拓展了 CA 方法的 methodology taxonomy。\n- 价值: Significance 维度——从 \"a better method\" 提升为 \"a new methodological category\"。当你的贡献可以被描述为拓展了领域 taxonomy 的某个维度，审稿人更容易认定其为 \"significant contribution to the field\"。\n- 调研依据: 直接参考 \"From Reasoning to Agentic\" survey (arXiv 2604.09459) 的 taxonomy 框架。Survey 的 5-category methodology taxonomy 中确实没有 calibration-based 这一类。\n\n【发掘点 4】\n- 维度: 前提假设质疑\n- 内容: Proposal 的核心假设是\"calibrated CI width 是 PRM prediction reliability 的好 proxy\"。这在 PRM 训练分布内是合理的，但存在一个未被充分讨论的风险：**随着 RL 训练推进，policy 产生的 rollouts 逐渐偏离 PRM 训练分布，frozen PRM 的 calibration 可能 degrade asymmetrically**——某些 step types 的 CI 可能变得 overconfident（CI 变窄但 accuracy 下降），导致 UGCA 的 gating 信号反转（应该 down-weight 却 up-weight）。Proposal 已有 \"Longitudinal PRM calibration tracking\" 实验（每 25% 训练进度检查 ECE/Brier score），这很好。但建议将这个风险从\"实验检查项\"提升为\"方法设计的 aware limitation\"——在 approach section 中明确承认这是 UGCA 的 operating assumption，并讨论当 calibration degrades 时的 graceful degradation behavior（α 趋向中间值而非极端值？还是整体偏向 outcome credit？），以及 potential mitigation（periodic re-calibration、calibration drift detection trigger）。这比在实验 section 里被动检查更主动，更不容易被审稿人作为 weakness 攻击。\n- 价值: 这属于 preemptive defense 而非发掘新亮点，但它直接保护了核心 claim 的可信度。审稿人一定会问 \"what happens when the frozen PRM's calibration degrades during training\"——如果 proposal 在方法 section 就 proactively 讨论了这个问题（而不是等到实验 section 才 reactively 检查），说明作者对方法的局限有深刻理解，显著提升 paper 的 soundness 感知。\n- 调研依据: PROGRS 选择 frozen PRM 也面临相同问题但未讨论 calibration drift；UCAS 使用 policy-side uncertainty 则天然回避了这个问题（因为信号源随 policy 更新）。这是 \"external frozen verifier\" 路线独有的风险，需要 UGCA 自己 address。\n\nSources:\n- [PROGRS: LLM Reasoning with Process Rewards for Outcome-Guided Steps](https://arxiv.org/abs/2604.02341)\n- [Discovering Process-Outcome Credit in Multi-Step LLM Reasoning](https://arxiv.org/abs/2602.01034)\n- [From Reasoning to Agentic: Credit Assignment in RL for LLMs](https://arxiv.org/abs/2604.09459)\n- [UCAS: Unlocking Exploration in RLVR](https://arxiv.org/abs/2510.10649)\n- [Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)\n- [CAPO: Towards Enhancing LLM Reasoning through Generative Credit Assignment](https://arxiv.org/abs/2508.02298)\n- [Do We Need to Verify Step by Step? (Jia et al.)](https://arxiv.org/abs/2502.10581)\n- [A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)\n- [GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154)\n- [Awesome Credit Assignment in LLM RL (GitHub)](https://github.com/xxzcc/Awesome-Credit-Assignment-in-LLM-RL)\n\n【补救 agent 本轮输出】:\nNow I have sufficient research context. Let me compile my comprehensive evaluation.\n\n---\n\n【状态】: 有缺陷待补救\n\n【前置调研发现】\n- **PURE / \"Stop Summation\" (NeurIPS 2025)**: 在 3 个 base model 上测试，baseline 包括 GRPO 及其变体，评测使用 MATH-500、AMC23、AIME；开源了基于 veRL 框架的代码，证实 min-form credit assignment 在 30% training steps 内达到 verifiable reward 方法性能。\n- **PROGRS / arXiv 2604.02341 (Apr 2026)**: 使用 frozen quantile-regression PRM + outcome-conditioned centering，评测覆盖 MATH-500、AMC、AIME、MinervaMath、OlympiadBench，baseline 为 DAPO 等 outcome-only 方法。PROGRS 在 MATH-500 上达到 74.9% vs DAPO 69.7%。代码开源状态不确定。\n- **GRPO-λ (ICLR 2026)**: 在 R1-Distill-Qwen-7B 上训练，使用 MATH 训练集 (7,500 problems)，评测包含 AIME24 等 benchmark，报告了 4+ 点平均提升。使用 Open-R1 框架。\n- **PRPO (arXiv Jan 2026)**: 在 Qwen2.5-Math-1.5B 上测试，MATH-500 从 61.2→64.4%；ablation 发现 relative distribution 下 process advantage 可导致 premature termination collapse。\n- **VPPO / \"Save the Good Prefix\" (arXiv Jan 2026)**: 使用 PRM 定位 first error step，评测 Pass@1 和 Pass@K。\n- **DAPO (2025)**: 使用 Qwen2.5-32B + veRL 框架，在 AIME 2024 达到 50 分；训练配置详尽（AdamW, lr=1e-6, batch=512, 16 rollouts/prompt）。\n- **Qwen2.5-Math-PRM-7B**: 基于 Qwen2.5-Math 家族数据训练，跨模型家族（如 Qwen3）的 scoring 可靠性存在已知风险，文献中缺少 Qwen2.5-PRM → Qwen3 policy 的系统性 cross-family 验证。\n- **veRL 框架**: 支持 Qwen3 模型（Qwen3.5 有兼容性问题但 Qwen3 可用），支持 GRPO、DAPO 等多种算法。\n- 调研总结：该领域当前的实验标准要求至少 5+ baselines（含 GRPO/DAPO 作为 outcome-only baseline + 至少 2-3 个 process-aware 方法），评测覆盖 MATH-500 + 竞赛级 benchmark (AIME/AMC)，ablation 需隔离各组件贡献，审稿人普遍关注 reward hacking 的量化分析和 compute fairness。\n\n---\n\n【缺陷 1】\n- 类别: 可行性问题\n- 问题: Proposal 使用 Qwen2.5-Math-PRM-7B（在 Qwen2.5-Math 家族数据上训练）来为 Qwen3-8B/1.7B 的 rollouts 打分和计算 calibrated CI width。Proposal 虽然在\"Cross-family PRM validation\"中提到了 ECE/Brier score 对比，并提出\"If significant degradation, perform additional quantile calibration fine-tuning on Qwen3 data\"——但这个 mitigation 的执行协议严重不足：(a) quantile calibration fine-tuning 需要 Qwen3 rollouts 的 step-level ground truth，如何获取？MC estimation 成本高且引入新的 estimation variance，用 PRM 自身标注则循环依赖；(b) 没有定义\"significant degradation\"的具体阈值（ECE > 多少算 significant？）；(c) 如果确实需要 re-calibration，对 timeline 和 compute budget 的影响未量化。这是整个方法的前提假设（calibrated CI width 有效 proxy PRM reliability），如果跨家族转移失败，核心 gating mechanism 失去意义。\n- 严重度: 可补救\n- 补救方案: (1) 明确 step-level ground truth 获取协议——建议使用 outcome-based MC estimation：对每个 step 生成 N 条 completions（N=8-16），用 final answer correctness 作为 step correctness proxy（类似 Math-Shepherd 方法），这与 PRM 的 training data 构建方式一致且不依赖 PRM 本身；(2) 设定具体降级阈值：如 ECE > 0.10 或 Brier score 相对恶化 > 20% 时触发 re-calibration；(3) 在 compute budget 中显式预留 re-calibration contingency（估算：Qwen3 rollout 生成 ~50h + quantile fine-tuning ~20h ≈ 70h H100，当前预留的 20h 不足）；(4) 将 cross-family validation 作为 week 1 的 go/no-go gate，若降级超阈值则在 week 2 完成 re-calibration 后才进入后续实验。\n- 调研依据: Qwen2.5-Math-PRM-7B 的 HuggingFace 文档及 Park et al. (NeurIPS 2025) 的 calibration 方法论；\"Distributional PRM\" (arXiv 2605.06785) 评估了 OT calibration 在 out-of-distribution 问题上的表现，提供了 cross-distribution 降级的参考。\n\n【缺陷 2】\n- 类别: 实验设计不足\n- 问题: Proposal 未包含 UGCA + PROGRS 组合的实验。PROGRS 在 trajectory level 做 outcome-conditioned centering（纠正 trajectory 间的系统性 PRM 偏差），UGCA 在 step level 做 uncertainty gating（纠正 step 间的异质性 PRM 可靠性）。这两个机制在不同粒度上操作，理论上是正交且可组合的。缺少这个组合实验会留下关键 reviewer 疑问：(a) UGCA 的 gain 是否与 PROGRS 的 trajectory-level centering 冗余？(b) 两者组合是否能进一步提升性能？(c) 如果 UGCA 在已有 PROGRS centering 的基础上仍有显著提升，这才是 per-step gating 价值的最强论证。\n- 严重度: 可补救\n- 补救方案: 在 8B 实验中增加 UGCA + PROGRS 组合条件（约增加 1 config × 3 seeds ≈ 270 H100-hours）。具体做法：先做 PROGRS 的 trajectory-level centering，然后在 centered advantage 上再做 UGCA 的 per-step α gating。如果 UGCA + PROGRS > max(UGCA, PROGRS)，则证明正交互补性；如果 UGCA + PROGRS ≈ UGCA，则说明 per-step gating 已经隐式涵盖了 trajectory-level correction。无论结果如何，这个实验都大幅增强论文的说服力。\n- 调研依据: PROGRS (arXiv 2604.02341) 的 outcome-conditioned centering 机制与 UGCA 的 per-step gating 操作在不同粒度，基于领域实验规范判断，审稿人面对两个同时期的 closely-related 方法，几乎必然会要求组合比较。\n\n【缺陷 3】\n- 类别: 可行性问题\n- 问题: PROGRS 是 2026 年 4 月的论文（arXiv 2604.02341），Proposal 在 timeline 中将 \"PROGRS core reproduction\" 安排在 wk1-2。但 PROGRS 的代码是否已开源尚不确定（调研中未找到公开 repo），且其技术方案包含 multi-scale coherence evaluator + outcome-conditioned centering + quantile-regression PRM 集成——如果需要从论文描述完全 re-implement，2 周内同时完成 PRM calibration + cross-family validation + PURE/veRL integration + PROGRS reproduction 的工作量非常紧张。类似地，GRPO-λ 的官方实现使用 Open-R1 框架而非 veRL，可能需要额外适配。\n- 严重度: 可补救\n- 补救方案: (1) 在 week 0（pre-experiment preparation）立即确认 PROGRS 和 GRPO-λ 的代码可用性和框架兼容性；(2) 如果 PROGRS 代码不可用，有两个策略：(a) 简化实现——仅实现 PROGRS 的 core component (outcome-conditioned centering on frozen PRM scores)，不复现 multi-scale coherence evaluator（在论文中注明是 simplified reproduction 并讨论差异）；(b) 重新排 timeline——将 PROGRS reproduction 移至 wk2-3，压缩 wk7 的 analysis 时间；(3) 对 GRPO-λ，考虑使用其公开的 Open-R1 实现直接跑 baseline，不必强制移植到 veRL。在 compute budget 中已包含 \"PROGRS/GRPO-λ reproduction development: 80h\"，但如果需要从头实现，可能需要追加 ~40-60h 的工程时间。\n- 调研依据: GRPO-λ (arXiv 2510.00194) 使用 Open-R1 框架；PROGRS 的 arXiv 页面和搜索结果未发现明确的开源代码链接。\n\n【缺陷 4】\n- 类别: 评估方案缺陷\n- 问题: \"Longitudinal PRM calibration tracking\" 部分提出在每 25% training progress checkpoint 上计算 ECE 和 Brier score，但仅说 \"If significant degradation detected, discuss periodic re-calibration as mitigation\"。这存在两个问题：(a) \"discuss\" 意味着只是在论文中讨论而非实际执行 mitigation——如果 frozen PRM 的 calibration 随 policy drift 显著恶化，而论文仅 \"discuss\" 但不解决，审稿人会追问为何不在 training 中实施动态 re-calibration；(b) 如果 calibration 在 training 中途严重退化，UGCA 在后半段训练中的 gating 可能失效，最终结果的归因会变得混乱——是 UGCA 好还是只是前半段训练好？\n- 严重度: 可补救\n- 补救方案: (1) 将 \"discuss\" 升级为具体协议：若 ECE 在某 checkpoint 相对初始值恶化 > 50%（例如从 0.05 升到 0.075+），则触发一次快速 re-calibration（仅更新 quantile regression heads，frozen backbone，成本约 10-15h H100）；(2) 在 ablation 中增加一个对比条件：\"UGCA with periodic re-calibration vs. UGCA with frozen calibration throughout\"，以量化 calibration drift 的实际影响；(3) 如果 re-calibration 太昂贵，退而求其次：至少在实验结果中按 training phase 分段报告性能（前 50% vs 后 50% steps 的 gain），以展示 UGCA 的效果是否随 calibration drift 衰减。选项 (3) 成本最低，是最小可行的补救方案。\n- 调研依据: 基于领域实验规范判断——frozen reward model + RL training 的 distribution shift 是 RLHF 文献中广泛讨论的已知问题，审稿人对此高度敏感。\n\n【缺陷 5】\n- 类别: baseline 不足或过时\n- 问题: \"Discovering Process-Outcome Credit\" (arXiv 2602.01034) 是与 UGCA 最直接可比的方法——两者都做 per-step process-outcome credit mixing，区别仅在于 gating signal 来源（MC information gain vs calibrated CI width）。Proposal 选择不跑它作为 direct baseline，仅做 \"Theoretical FLOPs comparison\"。虽然 compute cost 差异的理由有一定合理性（MC estimation overhead），但审稿人面对一个如此直接可比的方法不在 baseline 中，即使接受 compute 理由，也很可能要求至少一个 small-scale 实证比较（如 1.7B model、1 seed、reduced training steps）来验证理论分析的结论。\n- 严重度: 可补救\n- 补救方案: 在 Qwen3-1.7B 上跑一个 reduced-scale 的 \"Discovering Process-Outcome Credit\" 实验：使用较少 training steps (如 50% of full training)、1 seed、较少 MC rollouts (如 N=4)，目的不是做公平全面对比，而是获取一个 empirical data point 来 ground 理论 FLOPs 分析。预计额外成本 ~60-80h H100。在论文中明确标注这是 \"reduced-scale comparison\" 并解释为什么 full-scale comparison 在 compute-normalized 条件下对该方法不利。这比纯理论分析有说服力得多。\n- 调研依据: \"Discovering Process-Outcome Credit\" (arXiv 2602.01034) 在 MATH 和 Super-CLEVR 上的实验使用了 GRPO 作为 baseline，方法涉及 Step-wise Marginal Information Gain + Decoupled Masking，需要额外 MC rollouts。\n\n【缺陷 6】\n- 类别: ablation 不完整\n- 问题: 当前 ablation 覆盖了 boundary cases、hard vs soft gating、raw PRM score vs calibrated CI width、calibrated vs uncalibrated、hyperparameters——这些都很好。但缺少一个重要的 ablation：**process credit base formulation 的影响**。Proposal 中 process credit 固定使用 PURE-style min-form advantage (A^min)，但一个自然的问题是：如果改用 summation-form (A^sum) 或 mean-form 作为 process credit component，UGCA 的 gating 是否仍然有效？这关系到 UGCA 的 gating mechanism 是否 robust to the choice of underlying process credit formulation，还是其 gain 本质上来自 min-form + gating 的特定组合。\n- 严重度: 可补救\n- 补救方案: 在 1.7B ablation 中增加 1 个条件：UGCA with summation-form process credit (A^sum)，对比 UGCA with min-form process credit (A^min)。这只需修改 advantage 计算的聚合方式，不需要新的模型或 PRM，额外 compute cost ≈ 1 config × 3 seeds ≈ 60h H100。如果两者性能相近，说明 UGCA 的 value 主要来自 gating mechanism 本身；如果 min-form 显著更好，说明 min-form + gating 的组合有特殊协同效应，这本身也是一个有价值的发现。\n- 调研依据: PURE (NeurIPS 2025) 系统性对比了 min-form vs summation-form，证明 min-form 自身已有优势；审稿人可能会质疑 UGCA 的 gain 是否可以归因于 min-form 选择而非 gating 本身。\n\n---\n\n**整体评估总结**\n\n该 Proposal 的实验设计**整体质量很高**，在 baseline 覆盖度、benchmark 选择、reward hacking 量化、core assumption validation、statistical rigor 等方面都达到了顶会标准。以上 6 个缺陷均为**可补救**类别，没有发现方向性致命问题。其中缺陷 1（cross-family PRM 协议）和缺陷 2（UGCA + PROGRS 组合实验）优先级最高——前者关系到方法的基本可行性，后者几乎必然会被审稿人要求。缺陷 3-6 属于\"有则显著加分、无则可能被要求 revision\"的层级。补救所有 6 个缺陷的额外 compute 成本约 460-530 H100-hours（占原 budget ~16-18%），timeline 影响可通过调整 wk7-8 的分配来吸收。\n\nSources:\n- [PURE - Stop Summation (NeurIPS 2025)](https://openreview.net/forum?id=3Sxby0hH1q)\n- [PURE GitHub Repository](https://github.com/CJReinforce/PURE)\n- [PROGRS - arXiv 2604.02341](https://arxiv.org/abs/2604.02341)\n- [GRPO-λ - arXiv 2510.00194](https://arxiv.org/pdf/2510.00194)\n- [PRPO - arXiv 2601.07182](https://arxiv.org/abs/2601.07182)\n- [VPPO - Save the Good Prefix](https://arxiv.org/abs/2601.18984)\n- [Discovering Process-Outcome Credit - arXiv 2602.01034](https://arxiv.org/abs/2602.01034)\n- [DAPO - arXiv 2503.14476](https://arxiv.org/abs/2503.14476)\n- [Know What You Don't Know - Park et al. NeurIPS 2025](https://arxiv.org/html/2506.09338)\n- [Distributional PRM - arXiv 2605.06785](https://arxiv.org/html/2605.06785)\n- [Qwen2.5-Math-PRM-7B - HuggingFace](https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B)\n- [veRL Framework - GitHub](https://github.com/verl-project/verl)\n- [veRL Qwen Documentation](https://qwen.readthedocs.io/en/latest/training/verl.html)"
}
```

---

### Runtime record

_source line 73 · 2026-05-27T08:41:29.123Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:41:29.123Z",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

## Round 5

21 recorded events

### User

_source line 74 · 2026-05-27T08:41:29.149Z_

【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
Now I have sufficient research context. Let me synthesize my findings and provide my assessment.

---

【状态】: 有发掘空间

【前置调研发现】
- **PROGRS** (arXiv 2604.02341, Apr 2026): 使用 outcome-conditioned centering + frozen quantile-regression PRM，但 centering 是 trajectory-level 的，所有 step 接受相同处理。与 UGCA 的核心差异（per-step adaptive gating）确认属实。
- **"Discovering Process-Outcome Credit"** (arXiv 2602.01034, Feb 2026): 提出 Step-wise Marginal Information Gain (MIG) + Decoupled Masking 实现 per-step process-outcome mixing，但基于 Monte Carlo 估计的 intrinsic information gain，不是 calibration-derived uncertainty。这是 UGCA 在 per-step 维度上最近的竞争者，差异在于信号来源（intrinsic vs. verifier calibration）。
- **"From Reasoning to Agentic" credit assignment survey** (arXiv 2604.09459, Apr 2026): 组织 47 种 CA 方法的 taxonomy（granularity × methodology），未识别出任何使用 PRM calibration confidence 做 per-step credit gating 的方法，确认 UGCA 占据的位置（verifier calibration × per-step）在现有文献中为空白。
- **UCAS** (arXiv 2510.10649, Oct 2025): 使用 policy model 自身 logit uncertainty 做 advantage shaping，信号源是 policy-side 的（随训练漂移），与 UGCA 使用 frozen external verifier 的 calibrated uncertainty 有本质区别。
- **"Reward Under Attack"** (arXiv 2603.06621, Mar 2026): 证明 PRMs 可被系统性 exploit 为 "fluency detectors"（PRM score >0.9 但 accuracy <4%），直接支撑 UGCA 的 motivation。
- **CAPO** (arXiv 2508.02298, Aug 2025): 用 LLM-as-GenPRM 做 token-level generative credit assignment，属于 model-based 方法，与 calibration-based 方法正交。
- **Jia et al.** (ICML 2025, arXiv 2502.10581): 理论证明 outcome supervision 不比 process supervision 更难，为 UGCA 的 fallback guarantee 提供基础。
- 调研总结：这个领域当前的研究者沿两条主线突破——(1) 更精细的 per-step credit assignment（从 trajectory-level 到 step-level 到 token-level），(2) 更可靠的 PRM 信号（calibration、robustness、generative verification）。但这两条线目前是**分离的**：做 per-step credit 的工作不关注 verifier reliability，做 PRM calibration 的工作只用于 test-time scaling 或 trajectory-level RL。UGCA 的核心贡献在于**交叉这两条线**，这个定位是真实的、有价值的。

---

【发掘点 1】
- 维度: 核心 claim 强化
- 内容: 将 reward hacking robustness 从"实验观测"提升为"方法的结构性属性"。当前 proposal 将 reward hacking quantification（PAG curves、reward hacking rate）定位为实验分析项。但 UGCA 的设计提供了一个更强的 claim：**当 PRM 被 exploit 时（在 adversarial policy 行为上给出高分），如果 calibration 是良好的，这些 out-of-distribution 输入上的 CI 应当变宽——UGCA 自动 down-weight 这些不可靠信号**。这不是一个需要事后验证的经验发现，而是方法设计的内在属性。建议在 "Proposed Approach" 或 "Broader Significance" 中增加一个显式的 claim：UGCA 提供了**对 PRM reward hacking 的 calibration-mediated implicit defense**，并在实验中用 PAG curves 对比 UGCA vs. baselines 的 overoptimization 速率来验证。这将 "Reward Under Attack" 的 motivation 和 UGCA 的 mechanism 形成闭环，而不仅仅是 citing 一篇 motivation paper。
- 价值: 这直接提升 Significance——从"更好的 credit assignment"拓展到"structurally robust credit assignment"。Reward hacking 是 2025-2026 RL 社区的高关注问题（"Reward Under Attack" 3月才出来），把 UGCA 定位为 principled defense mechanism 而非仅仅 better accuracy，大幅提升 impact narrative。审稿人对 "reward hacking robustness" 的兴趣远高于 "又多了 1-2 个点 accuracy"。
- 调研依据: 直接参考 "Reward Under Attack" (arXiv 2603.06621) 的发现——PRMs 在 adversarial RL 中退化为 fluency detectors。UGCA 的 calibrated CI gating 正好 target 这个 failure mode：calibration 在 OOD 输入上天然产生更宽的 CI。

【发掘点 2】
- 维度: novelty 锐化
- 内容: 将 appendix 中的 MSE-optimal interpolation weight 推导提升为 main paper 的理论贡献。当前 proposal 在 "Theoretical grounding" 中提到"under simplifying assumptions (Gaussian noise on PRM scores with variance proportional to w_i²), the MSE-optimal interpolation weight takes a sigmoid-like form in w_i (formal derivation in appendix)"。这实际上是一个相当有力的结果——它说明 sigmoid gating 不是一个 ad hoc design choice，而是**MSE-optimal estimator 的 parametric approximation**。建议将其从 appendix 提升到 main paper 的 Section 3（方法部分），以 Proposition 形式给出：在 PRM score = true correctness + Gaussian noise(0, σ²(w_i)) 的模型下，最小化 per-step credit assignment MSE 的 optimal interpolation weight 是 w_i 的单调递减函数，sigmoid 是其 parametric family。这将 UGCA 从 "an intuitive per-step gating heuristic" 提升为 "a principled approximation to the MSE-optimal credit assignment under verifier uncertainty"。
- 价值: 直接提升 Novelty 的理论层次。Math reasoning RL 领域的论文大多是 empirical，一个有 prescriptive justification 的方法设计（不是 post-hoc 解释）在 AAAI 审稿中是显著加分项。同时也堵住了审稿人可能的质疑："why sigmoid? why not other gating forms?"——因为 sigmoid 是理论最优解的近似。
- 调研依据: 基于领域整体趋势判断——近期 credit assignment 方法（GRPO-λ、PURE、VPPO）大多缺乏理论 justification for design choices，审稿人经常在 reviews 中问 "why this specific form"。有理论支撑的设计选择在该领域是稀缺的差异化优势。

【发掘点 3】
- 维度: significance 提升
- 内容: 更显式地利用 credit assignment survey (arXiv 2604.09459) 的 taxonomy 来定位 UGCA 的 contribution。Proposal 中已有 2×2 表格（signal source × granularity），但可以更直接地 cite 这篇 survey 并指出：在 survey 识别的 5 种 methodology categories（Monte Carlo, temporal difference, model-based, game-theoretic, information-theoretic）中，UGCA 开创了第 6 种——**calibration-based** credit assignment，即信号不来自 rollout estimation（MC）、value function（TD）、generative model（model-based）、contribution attribution（game-theoretic）或 mutual information（information-theoretic），而来自 verifier calibration quality。这不仅填了一个 empirical gap，更拓展了 CA 方法的 methodology taxonomy。
- 价值: Significance 维度——从 "a better method" 提升为 "a new methodological category"。当你的贡献可以被描述为拓展了领域 taxonomy 的某个维度，审稿人更容易认定其为 "significant contribution to the field"。
- 调研依据: 直接参考 "From Reasoning to Agentic" survey (arXiv 2604.09459) 的 taxonomy 框架。Survey 的 5-category methodology taxonomy 中确实没有 calibration-based 这一类。

【发掘点 4】
- 维度: 前提假设质疑
- 内容: Proposal 的核心假设是"calibrated CI width 是 PRM prediction reliability 的好 proxy"。这在 PRM 训练分布内是合理的，但存在一个未被充分讨论的风险：**随着 RL 训练推进，policy 产生的 rollouts 逐渐偏离 PRM 训练分布，frozen PRM 的 calibration 可能 degrade asymmetrically**——某些 step types 的 CI 可能变得 overconfident（CI 变窄但 accuracy 下降），导致 UGCA 的 gating 信号反转（应该 down-weight 却 up-weight）。Proposal 已有 "Longitudinal PRM calibration tracking" 实验（每 25% 训练进度检查 ECE/Brier score），这很好。但建议将这个风险从"实验检查项"提升为"方法设计的 aware limitation"——在 approach section 中明确承认这是 UGCA 的 operating assumption，并讨论当 calibration degrades 时的 graceful degradation behavior（α 趋向中间值而非极端值？还是整体偏向 outcome credit？），以及 potential mitigation（periodic re-calibration、calibration drift detection trigger）。这比在实验 section 里被动检查更主动，更不容易被审稿人作为 weakness 攻击。
- 价值: 这属于 preemptive defense 而非发掘新亮点，但它直接保护了核心 claim 的可信度。审稿人一定会问 "what happens when the frozen PRM's calibration degrades during training"——如果 proposal 在方法 section 就 proactively 讨论了这个问题（而不是等到实验 section 才 reactively 检查），说明作者对方法的局限有深刻理解，显著提升 paper 的 soundness 感知。
- 调研依据: PROGRS 选择 frozen PRM 也面临相同问题但未讨论 calibration drift；UCAS 使用 policy-side uncertainty 则天然回避了这个问题（因为信号源随 policy 更新）。这是 "external frozen verifier" 路线独有的风险，需要 UGCA 自己 address。

Sources:
- [PROGRS: LLM Reasoning with Process Rewards for Outcome-Guided Steps](https://arxiv.org/abs/2604.02341)
- [Discovering Process-Outcome Credit in Multi-Step LLM Reasoning](https://arxiv.org/abs/2602.01034)
- [From Reasoning to Agentic: Credit Assignment in RL for LLMs](https://arxiv.org/abs/2604.09459)
- [UCAS: Unlocking Exploration in RLVR](https://arxiv.org/abs/2510.10649)
- [Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)
- [CAPO: Towards Enhancing LLM Reasoning through Generative Credit Assignment](https://arxiv.org/abs/2508.02298)
- [Do We Need to Verify Step by Step? (Jia et al.)](https://arxiv.org/abs/2502.10581)
- [A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)
- [GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154)
- [Awesome Credit Assignment in LLM RL (GitHub)](https://github.com/xxzcc/Awesome-Credit-Assignment-in-LLM-RL)

【补救 agent 本轮输出】:
Now I have sufficient research context. Let me compile my comprehensive evaluation.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **PURE / "Stop Summation" (NeurIPS 2025)**: 在 3 个 base model 上测试，baseline 包括 GRPO 及其变体，评测使用 MATH-500、AMC23、AIME；开源了基于 veRL 框架的代码，证实 min-form credit assignment 在 30% training steps 内达到 verifiable reward 方法性能。
- **PROGRS / arXiv 2604.02341 (Apr 2026)**: 使用 frozen quantile-regression PRM + outcome-conditioned centering，评测覆盖 MATH-500、AMC、AIME、MinervaMath、OlympiadBench，baseline 为 DAPO 等 outcome-only 方法。PROGRS 在 MATH-500 上达到 74.9% vs DAPO 69.7%。代码开源状态不确定。
- **GRPO-λ (ICLR 2026)**: 在 R1-Distill-Qwen-7B 上训练，使用 MATH 训练集 (7,500 problems)，评测包含 AIME24 等 benchmark，报告了 4+ 点平均提升。使用 Open-R1 框架。
- **PRPO (arXiv Jan 2026)**: 在 Qwen2.5-Math-1.5B 上测试，MATH-500 从 61.2→64.4%；ablation 发现 relative distribution 下 process advantage 可导致 premature termination collapse。
- **VPPO / "Save the Good Prefix" (arXiv Jan 2026)**: 使用 PRM 定位 first error step，评测 Pass@1 和 Pass@K。
- **DAPO (2025)**: 使用 Qwen2.5-32B + veRL 框架，在 AIME 2024 达到 50 分；训练配置详尽（AdamW, lr=1e-6, batch=512, 16 rollouts/prompt）。
- **Qwen2.5-Math-PRM-7B**: 基于 Qwen2.5-Math 家族数据训练，跨模型家族（如 Qwen3）的 scoring 可靠性存在已知风险，文献中缺少 Qwen2.5-PRM → Qwen3 policy 的系统性 cross-family 验证。
- **veRL 框架**: 支持 Qwen3 模型（Qwen3.5 有兼容性问题但 Qwen3 可用），支持 GRPO、DAPO 等多种算法。
- 调研总结：该领域当前的实验标准要求至少 5+ baselines（含 GRPO/DAPO 作为 outcome-only baseline + 至少 2-3 个 process-aware 方法），评测覆盖 MATH-500 + 竞赛级 benchmark (AIME/AMC)，ablation 需隔离各组件贡献，审稿人普遍关注 reward hacking 的量化分析和 compute fairness。

---

【缺陷 1】
- 类别: 可行性问题
- 问题: Proposal 使用 Qwen2.5-Math-PRM-7B（在 Qwen2.5-Math 家族数据上训练）来为 Qwen3-8B/1.7B 的 rollouts 打分和计算 calibrated CI width。Proposal 虽然在"Cross-family PRM validation"中提到了 ECE/Brier score 对比，并提出"If significant degradation, perform additional quantile calibration fine-tuning on Qwen3 data"——但这个 mitigation 的执行协议严重不足：(a) quantile calibration fine-tuning 需要 Qwen3 rollouts 的 step-level ground truth，如何获取？MC estimation 成本高且引入新的 estimation variance，用 PRM 自身标注则循环依赖；(b) 没有定义"significant degradation"的具体阈值（ECE > 多少算 significant？）；(c) 如果确实需要 re-calibration，对 timeline 和 compute budget 的影响未量化。这是整个方法的前提假设（calibrated CI width 有效 proxy PRM reliability），如果跨家族转移失败，核心 gating mechanism 失去意义。
- 严重度: 可补救
- 补救方案: (1) 明确 step-level ground truth 获取协议——建议使用 outcome-based MC estimation：对每个 step 生成 N 条 completions（N=8-16），用 final answer correctness 作为 step correctness proxy（类似 Math-Shepherd 方法），这与 PRM 的 training data 构建方式一致且不依赖 PRM 本身；(2) 设定具体降级阈值：如 ECE > 0.10 或 Brier score 相对恶化 > 20% 时触发 re-calibration；(3) 在 compute budget 中显式预留 re-calibration contingency（估算：Qwen3 rollout 生成 ~50h + quantile fine-tuning ~20h ≈ 70h H100，当前预留的 20h 不足）；(4) 将 cross-family validation 作为 week 1 的 go/no-go gate，若降级超阈值则在 week 2 完成 re-calibration 后才进入后续实验。
- 调研依据: Qwen2.5-Math-PRM-7B 的 HuggingFace 文档及 Park et al. (NeurIPS 2025) 的 calibration 方法论；"Distributional PRM" (arXiv 2605.06785) 评估了 OT calibration 在 out-of-distribution 问题上的表现，提供了 cross-distribution 降级的参考。

【缺陷 2】
- 类别: 实验设计不足
- 问题: Proposal 未包含 UGCA + PROGRS 组合的实验。PROGRS 在 trajectory level 做 outcome-conditioned centering（纠正 trajectory 间的系统性 PRM 偏差），UGCA 在 step level 做 uncertainty gating（纠正 step 间的异质性 PRM 可靠性）。这两个机制在不同粒度上操作，理论上是正交且可组合的。缺少这个组合实验会留下关键 reviewer 疑问：(a) UGCA 的 gain 是否与 PROGRS 的 trajectory-level centering 冗余？(b) 两者组合是否能进一步提升性能？(c) 如果 UGCA 在已有 PROGRS centering 的基础上仍有显著提升，这才是 per-step gating 价值的最强论证。
- 严重度: 可补救
- 补救方案: 在 8B 实验中增加 UGCA + PROGRS 组合条件（约增加 1 config × 3 seeds ≈ 270 H100-hours）。具体做法：先做 PROGRS 的 trajectory-level centering，然后在 centered advantage 上再做 UGCA 的 per-step α gating。如果 UGCA + PROGRS > max(UGCA, PROGRS)，则证明正交互补性；如果 UGCA + PROGRS ≈ UGCA，则说明 per-step gating 已经隐式涵盖了 trajectory-level correction。无论结果如何，这个实验都大幅增强论文的说服力。
- 调研依据: PROGRS (arXiv 2604.02341) 的 outcome-conditioned centering 机制与 UGCA 的 per-step gating 操作在不同粒度，基于领域实验规范判断，审稿人面对两个同时期的 closely-related 方法，几乎必然会要求组合比较。

【缺陷 3】
- 类别: 可行性问题
- 问题: PROGRS 是 2026 年 4 月的论文（arXiv 2604.02341），Proposal 在 timeline 中将 "PROGRS core reproduction" 安排在 wk1-2。但 PROGRS 的代码是否已开源尚不确定（调研中未找到公开 repo），且其技术方案包含 multi-scale coherence evaluator + outcome-conditioned centering + quantile-regression PRM 集成——如果需要从论文描述完全 re-implement，2 周内同时完成 PRM calibration + cross-family validation + PURE/veRL integration + PROGRS reproduction 的工作量非常紧张。类似地，GRPO-λ 的官方实现使用 Open-R1 框架而非 veRL，可能需要额外适配。
- 严重度: 可补救
- 补救方案: (1) 在 week 0（pre-experiment preparation）立即确认 PROGRS 和 GRPO-λ 的代码可用性和框架兼容性；(2) 如果 PROGRS 代码不可用，有两个策略：(a) 简化实现——仅实现 PROGRS 的 core component (outcome-conditioned centering on frozen PRM scores)，不复现 multi-scale coherence evaluator（在论文中注明是 simplified reproduction 并讨论差异）；(b) 重新排 timeline——将 PROGRS reproduction 移至 wk2-3，压缩 wk7 的 analysis 时间；(3) 对 GRPO-λ，考虑使用其公开的 Open-R1 实现直接跑 baseline，不必强制移植到 veRL。在 compute budget 中已包含 "PROGRS/GRPO-λ reproduction development: 80h"，但如果需要从头实现，可能需要追加 ~40-60h 的工程时间。
- 调研依据: GRPO-λ (arXiv 2510.00194) 使用 Open-R1 框架；PROGRS 的 arXiv 页面和搜索结果未发现明确的开源代码链接。

【缺陷 4】
- 类别: 评估方案缺陷
- 问题: "Longitudinal PRM calibration tracking" 部分提出在每 25% training progress checkpoint 上计算 ECE 和 Brier score，但仅说 "If significant degradation detected, discuss periodic re-calibration as mitigation"。这存在两个问题：(a) "discuss" 意味着只是在论文中讨论而非实际执行 mitigation——如果 frozen PRM 的 calibration 随 policy drift 显著恶化，而论文仅 "discuss" 但不解决，审稿人会追问为何不在 training 中实施动态 re-calibration；(b) 如果 calibration 在 training 中途严重退化，UGCA 在后半段训练中的 gating 可能失效，最终结果的归因会变得混乱——是 UGCA 好还是只是前半段训练好？
- 严重度: 可补救
- 补救方案: (1) 将 "discuss" 升级为具体协议：若 ECE 在某 checkpoint 相对初始值恶化 > 50%（例如从 0.05 升到 0.075+），则触发一次快速 re-calibration（仅更新 quantile regression heads，frozen backbone，成本约 10-15h H100）；(2) 在 ablation 中增加一个对比条件："UGCA with periodic re-calibration vs. UGCA with frozen calibration throughout"，以量化 calibration drift 的实际影响；(3) 如果 re-calibration 太昂贵，退而求其次：至少在实验结果中按 training phase 分段报告性能（前 50% vs 后 50% steps 的 gain），以展示 UGCA 的效果是否随 calibration drift 衰减。选项 (3) 成本最低，是最小可行的补救方案。
- 调研依据: 基于领域实验规范判断——frozen reward model + RL training 的 distribution shift 是 RLHF 文献中广泛讨论的已知问题，审稿人对此高度敏感。

【缺陷 5】
- 类别: baseline 不足或过时
- 问题: "Discovering Process-Outcome Credit" (arXiv 2602.01034) 是与 UGCA 最直接可比的方法——两者都做 per-step process-outcome credit mixing，区别仅在于 gating signal 来源（MC information gain vs calibrated CI width）。Proposal 选择不跑它作为 direct baseline，仅做 "Theoretical FLOPs comparison"。虽然 compute cost 差异的理由有一定合理性（MC estimation overhead），但审稿人面对一个如此直接可比的方法不在 baseline 中，即使接受 compute 理由，也很可能要求至少一个 small-scale 实证比较（如 1.7B model、1 seed、reduced training steps）来验证理论分析的结论。
- 严重度: 可补救
- 补救方案: 在 Qwen3-1.7B 上跑一个 reduced-scale 的 "Discovering Process-Outcome Credit" 实验：使用较少 training steps (如 50% of full training)、1 seed、较少 MC rollouts (如 N=4)，目的不是做公平全面对比，而是获取一个 empirical data point 来 ground 理论 FLOPs 分析。预计额外成本 ~60-80h H100。在论文中明确标注这是 "reduced-scale comparison" 并解释为什么 full-scale comparison 在 compute-normalized 条件下对该方法不利。这比纯理论分析有说服力得多。
- 调研依据: "Discovering Process-Outcome Credit" (arXiv 2602.01034) 在 MATH 和 Super-CLEVR 上的实验使用了 GRPO 作为 baseline，方法涉及 Step-wise Marginal Information Gain + Decoupled Masking，需要额外 MC rollouts。

【缺陷 6】
- 类别: ablation 不完整
- 问题: 当前 ablation 覆盖了 boundary cases、hard vs soft gating、raw PRM score vs calibrated CI width、calibrated vs uncalibrated、hyperparameters——这些都很好。但缺少一个重要的 ablation：**process credit base formulation 的影响**。Proposal 中 process credit 固定使用 PURE-style min-form advantage (A^min)，但一个自然的问题是：如果改用 summation-form (A^sum) 或 mean-form 作为 process credit component，UGCA 的 gating 是否仍然有效？这关系到 UGCA 的 gating mechanism 是否 robust to the choice of underlying process credit formulation，还是其 gain 本质上来自 min-form + gating 的特定组合。
- 严重度: 可补救
- 补救方案: 在 1.7B ablation 中增加 1 个条件：UGCA with summation-form process credit (A^sum)，对比 UGCA with min-form process credit (A^min)。这只需修改 advantage 计算的聚合方式，不需要新的模型或 PRM，额外 compute cost ≈ 1 config × 3 seeds ≈ 60h H100。如果两者性能相近，说明 UGCA 的 value 主要来自 gating mechanism 本身；如果 min-form 显著更好，说明 min-form + gating 的组合有特殊协同效应，这本身也是一个有价值的发现。
- 调研依据: PURE (NeurIPS 2025) 系统性对比了 min-form vs summation-form，证明 min-form 自身已有优势；审稿人可能会质疑 UGCA 的 gain 是否可以归因于 min-form 选择而非 gating 本身。

---

**整体评估总结**

该 Proposal 的实验设计**整体质量很高**，在 baseline 覆盖度、benchmark 选择、reward hacking 量化、core assumption validation、statistical rigor 等方面都达到了顶会标准。以上 6 个缺陷均为**可补救**类别，没有发现方向性致命问题。其中缺陷 1（cross-family PRM 协议）和缺陷 2（UGCA + PROGRS 组合实验）优先级最高——前者关系到方法的基本可行性，后者几乎必然会被审稿人要求。缺陷 3-6 属于"有则显著加分、无则可能被要求 revision"的层级。补救所有 6 个缺陷的额外 compute 成本约 460-530 H100-hours（占原 budget ~16-18%），timeline 影响可通过调整 wk7-8 的分配来吸收。

Sources:
- [PURE - Stop Summation (NeurIPS 2025)](https://openreview.net/forum?id=3Sxby0hH1q)
- [PURE GitHub Repository](https://github.com/CJReinforce/PURE)
- [PROGRS - arXiv 2604.02341](https://arxiv.org/abs/2604.02341)
- [GRPO-λ - arXiv 2510.00194](https://arxiv.org/pdf/2510.00194)
- [PRPO - arXiv 2601.07182](https://arxiv.org/abs/2601.07182)
- [VPPO - Save the Good Prefix](https://arxiv.org/abs/2601.18984)
- [Discovering Process-Outcome Credit - arXiv 2602.01034](https://arxiv.org/abs/2602.01034)
- [DAPO - arXiv 2503.14476](https://arxiv.org/abs/2503.14476)
- [Know What You Don't Know - Park et al. NeurIPS 2025](https://arxiv.org/html/2506.09338)
- [Distributional PRM - arXiv 2605.06785](https://arxiv.org/html/2605.06785)
- [Qwen2.5-Math-PRM-7B - HuggingFace](https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B)
- [veRL Framework - GitHub](https://github.com/verl-project/verl)
- [veRL Qwen Documentation](https://qwen.readthedocs.io/en/latest/training/verl.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95d39eb5-ad6b-4b36-b5b3-178f88b3a43b",
  "isSidechain": false,
  "promptId": "dbd08305-8867-4492-a248-7049e3b5ee25",
  "type": "user",
  "uuid": "c55638da-cf22-4a35-ab44-3bac4af92132",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 75_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research context. Let me synthesize my findings and provide my assessment.  ---  【状态】…",
  "leafUuid": "c55638da-cf22-4a35-ab44-3bac4af92132",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 76_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Assistant

_source line 77 · 2026-05-27T08:43:02.294Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the Round 3 worker outputs carefully.

**Discovery Agent Round 3:**
1. **Reward hacking as structural property** (Point 1): UGCA provides "calibration-mediated implicit defense" against reward hacking - when PRM is exploited on OOD inputs, calibrated CIs naturally widen, automatically down-weighting unreliable signals. Elevate from experimental observation to design property.
2. **Promote MSE-optimal derivation to main paper** (Point 2): The sigmoid gating's theoretical justification as MSE-optimal approximation should be a Proposition in the main text, not relegated to appendix.


3. **Cite credit assignment survey taxonomy** (Point 3): I should reference the credit assignment survey and position UGCA as introducing a new "calibration-based" methodological category within that landscape.
4. **Calibration drift as aware limitation** (Point 4): Rather than just checking calibration drift reactively in experiments, I need to proactively address it in the method section as a known limitation and discuss how the approach degrades gracefully.

**Remedy Agent Round 3:**
The cross-family PRM protocol needs concrete degradation thresholds and a step-level ground truth protocol using MC estimation with sufficient completions, plus contingency plans for when these fail.

Testing whether UGCA and PROGRS are orthogonal and composable will require substantial compute—around 270 H100-hours for the 8B model. There's also uncertainty around PROGRS code availability, so I should consider a simplified reproduction focusing on the core method without the multi-scale coherence evaluator, and note that GRPO-λ relies on Open-R1 rather than veRL.

For calibration tracking, I need to move beyond just discussing it and establish an actionable protocol with specific thresholds and re-calibration triggers. Finally, I should run a small-scale empirical comparison to validate the core insight about discovering process-outcome credit.

Looking at the progression of changes across rounds, I'm noticing the refinements are getting increasingly granular—moving from structural overhauls in Round 1 to presentation and framing improvements in Round 3, which suggests I'm approaching convergence on the core experimental design.

The most compelling suggestion from Round 3 is testing UGCA combined with PROGRS to validate whether their mechanisms are truly orthogonal, since reviewers will almost certainly ask about this interaction. The other points around promoting the MSE derivation and reframing reward hacking as a structural property are solid presentation enhancements, though the protocol specificity recommendations around degradation thresholds and timeline risk management are still worth evaluating for their experimental rigor.

Given that Round 2 and Round 3 are both refinement-focused iterations with diminishing returns, and the compute budget is already expanding significantly, I should converge here. The UGCA + PROGRS experiment is valuable enough to include, but continuing beyond this would likely just surface increasingly marginal issues while risking scope creep and seesaw effects between the agents' suggestions.

Now I need to evaluate what to actually adopt from Round 3. The discovery agent cited a credit assignment survey with a specific arXiv link, which they've already referenced before, so I can take that at face value. For the substantive suggestions—the reward hacking framing, the UGCA + PROGRS combination, and the cross-family PRM protocol details—I should assess each one on whether it genuinely strengthens the proposal or just adds complexity.

The reward hacking insight is worth adopting because it reframes calibration drift as a structural property rather than just an empirical observation. The MSE-optimal derivation should move from the appendix to the main paper since it provides theoretical grounding without extra work. For the credit assignment survey citation, I'll include it and note how UGCA fits into a calibration-based category, but I won't overstate this as a novel methodological contribution. The calibration drift limitation is also worth promoting from a reactive experiment to a proactive method discussion, since both the discovery and remedy agents flagged it from different angles.

From the remedy agent's latest round, I'm adopting the cross-family protocol specifics—concrete thresholds like ECE > 0.10, the MC-based ground truth approach with N=8-16 samples, and the week-1 go/no-go gate provide actionable structure. The UGCA and PROGRS combination test is the strongest suggestion here because reviewers will almost certainly ask about orthogonality and composability, even though it adds 270 hours. The simplified PROGRS fallback—stripping down to outcome-conditioned centering and a frozen PRM without the multi-scale coherence evaluator—is also practical to include.

For the longitudinal calibration, I'm going with the phase-segmented performance reporting as the baseline, but if budget permits, I'll add the specific re-calibration trigger at 50% ECE degradation. The reduced-scale Process-Outcome Credit comparison at 60-80 hours is worth the investment to preempt the "why not compare with the most similar method" objection. I'm also adopting the process credit formulation ablation to test sum-form versus min-form under UGCA—that's another 60 hours but isolates whether gains come from gating or the min-form choice itself.

Now I'm recalculating the resource estimate with these additions stacked on top of the original ~2900 H100-hours, starting with the UGCA+PROGRS combination at 8B scale.

The total lands around 3380 H100-hours or roughly $8,450, which is feasible for a well-resourced lab but the 8-week timeline is the real constraint. On the probability side, the novelty and significance are both medium-to-strong, with the MSE-optimal proposition and structural defense against reward hacking pushing toward stronger positioning, especially with the calibration and ablation studies anchoring the claims. The improvements from Round 2 to Round 3 are incremental refinements rather than fundamental restructuring, which aligns with my convergence criteria. The proposal now includes comprehensive baselines, ablations, and diagnostics, but the compute budget is already substantial at ~3400 H100-hours—adding more would risk feasibility. Both reviewers are identifying increasingly granular issues rather than core problems, and the idea quality ceiling won't shift with further iteration. Since my median estimate of 40% exceeds the 36% threshold, I'm ready to output the final optimization plan comparing this to the original proposal. the optimization plan.

Let me also trace through what needs to go in the final output:

1. Update the proposal one final time with Round 3 improvements
2. Output the final decision
3. Since converged with 中位 40% ≥ 36%, output the optimization plan comparing to ORIGINAL proposal

Actually wait, re-reading the instructions more carefully for "角色 C：最终输出":

"若通过（收敛且中位 ≥ 36%）→ 输出优化方案文本（对比原始 proposal 的修改建议列表）+ 实施评估"

So I need to output the optimization suggestions relative to the ORIGINAL proposal, plus implementation assessment.

Now I'm mapping out the key changes from the original proposal through to the final version: the novelty shifted from bridging PRM calibration and RL toward uncertainty-driven bias-variance tradeoffs in credit assignment, the bias decomposition now explicitly separates PRM miscalibration from aggregation bias with UGCA targeting the former, a 2×2 design space matrix was introduced, the MSE-optimal interpolation weight derivation moved to the main paper as a formal proposition, and the distinction between verifier prediction and confidence became a central insight. I've also added explicit treatment of trivial alternatives, framed reward hacking robustness as a structural property emerging from calibration, positioned the broader principle as verifier-uncertainty-aware RL, acknowledged calibration drift assumptions with graceful degradation, and incorporated seven additional related works.

For experiments, I'm expanding baselines to include DAPO, PROGRS, PRPO and VPPO at 1.7B scale, adding AIME 2025 and MinervaMath benchmarks with Pass@8 metrics, defining reward hacking metrics like PAG and uncertainty-conditioned accuracy, running ablations on boundary cases and process credit formulations, validating core assumptions through weight-accuracy correlations, tracking PRM calibration drift longitudinally, and cross-validating across different PRM families.

I'm also planning reduced-scale comparisons for the core discovery, running multiple seeds with bootstrap confidence intervals, and computing fairness metrics across wall-clock time and FLOPs with Pareto curves. This scales the compute budget from 1800 to 3400 H100-hours and cost from $4,500 to $8,500 while keeping the 8-week timeline tight.

Now I need to decide whether to output just the final optimization plan or include the convergence assessment first—looking back at the instructions, I think both are expected: the iterative round decision followed by the final deliverable. Before I write that out, let me verify a few key references through web search, particularly the credit assignment survey and the methodological soundness of combining UGCA with PROGRS.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c55638da-cf22-4a35-ab44-3bac4af92132",
  "isSidechain": false,
  "requestId": "req_011CbSmvJVttogHMcNKPdJvk",
  "type": "assistant",
  "uuid": "96854d47-19bb-42e9-9301-691c2788523c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DUCh87EJWmbLEWFjvSsGQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13126,
      "cache_read_input_tokens": 71801,
      "output_tokens": 3963,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3963,
          "cache_read_input_tokens": 71801,
          "cache_creation_input_tokens": 13126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13126
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

_source line 78 · 2026-05-27T08:43:02.296Z_

我来验证第 3 轮的关键新建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96854d47-19bb-42e9-9301-691c2788523c",
  "isSidechain": false,
  "requestId": "req_011CbSmvJVttogHMcNKPdJvk",
  "type": "assistant",
  "uuid": "2b2004e7-a38c-41b3-a5c2-8a55a3f4fafe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DUCh87EJWmbLEWFjvSsGQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13126,
      "cache_read_input_tokens": 71801,
      "output_tokens": 3963,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3963,
          "cache_read_input_tokens": 71801,
          "cache_creation_input_tokens": 13126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13126
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

_source line 79 · 2026-05-27T08:43:02.592Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Up8oVwitionbdDcF8Udhox`</summary>

```json
{
  "query": "arXiv 2604.09459 \"From Reasoning to Agentic\" credit assignment RL LLM survey taxonomy 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b2004e7-a38c-41b3-a5c2-8a55a3f4fafe",
  "isSidechain": false,
  "requestId": "req_011CbSmvJVttogHMcNKPdJvk",
  "type": "assistant",
  "uuid": "eb13c4a4-49c5-441e-8e44-d6f0ba7d5904",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DUCh87EJWmbLEWFjvSsGQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13126,
      "cache_read_input_tokens": 71801,
      "output_tokens": 3963,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3963,
          "cache_read_input_tokens": 71801,
          "cache_creation_input_tokens": 13126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13126
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

_source line 80 · 2026-05-27T08:43:11.154Z_

<details><summary>↩ Tool result · `toolu_01Up8oVwitionbdDcF8Udhox`</summary>

```text
Web search results for query: "arXiv 2604.09459 "From Reasoning to Agentic" credit assignment RL LLM survey taxonomy 2026"

Links: [{"title":"[2604.09459] From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models","url":"https://arxiv.org/abs/2604.09459"},{"title":"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models","url":"https://arxiv.org/html/2604.09459v1"},{"title":"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models / 从推理到智能体：大语言模型强化学习中的信用分配 | Alan Hou","url":"https://alanhou.org/blog/arxiv-from-reasoning-to-agentic-credit-assignment/"},{"title":"Paper page - From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models","url":"https://huggingface.co/papers/2604.09459"},{"title":"GitHub - xxzcc/Awesome-Credit-Assignment-in-LLM-RL · GitHub","url":"https://github.com/xxzcc/Awesome-Credit-Assignment-in-LLM-RL"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"}]

I found the paper you're looking for! Here are the key details about arXiv:2604.09459:

**Title:** From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models

**Author:** Chenchen Zhang

**Publication Date:** April 10, 2026

**Overview:** This is a survey of reinforcement learning (RL) for large language models that increasingly relies on sparse, outcome-level rewards, yet determining which actions within a long trajectory caused the outcome remains difficult.

**Two Main Problem Regimes:** The credit assignment problem manifests in two regimes: reasoning RL, where credit must be distributed across tokens and steps within a single chain-of-thought generation (500–30K+ tokens); and agentic RL, where multi-turn environment interaction introduces stochastic transitions, partial observability, and horizons of 100+ turns (100K–1M tokens).

**Taxonomy & Scope:** The survey covers 47 CA methods (41 core, 6 adjacent enablers) published between 2024 and early 2026, organizing them in a two-dimensional taxonomy by assignment granularity (token, segment, step, turn, multi-agent) and methodology (Monte Carlo, temporal difference, model-based, game-theoretic, information-theoretic).

**Key Insights:** The shift from reasoning to agentic RL complicates and reshapes the credit assignment landscape: reasoning CA is maturing around process reward models and critic-free group comparison, while agentic CA is driving genuinely new approaches including hindsight counterfactual analysis, privileged asymmetric critics, and turn-level MDP reformulations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb13c4a4-49c5-441e-8e44-d6f0ba7d5904",
  "isSidechain": false,
  "promptId": "dbd08305-8867-4492-a248-7049e3b5ee25",
  "type": "user",
  "uuid": "086c9fc1-2ca5-455a-b4f7-afcd02b05b5d",
  "toolUseResult": {
    "query": "arXiv 2604.09459 \"From Reasoning to Agentic\" credit assignment RL LLM survey taxonomy 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XfctrYvVwHyhVLTHMb8Nsi",
        "content": [
          {
            "title": "[2604.09459] From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models",
            "url": "https://arxiv.org/abs/2604.09459"
          },
          {
            "title": "From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models",
            "url": "https://arxiv.org/html/2604.09459v1"
          },
          {
            "title": "From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models / 从推理到智能体：大语言模型强化学习中的信用分配 | Alan Hou",
            "url": "https://alanhou.org/blog/arxiv-from-reasoning-to-agentic-credit-assignment/"
          },
          {
            "title": "Paper page - From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models",
            "url": "https://huggingface.co/papers/2604.09459"
          },
          {
            "title": "GitHub - xxzcc/Awesome-Credit-Assignment-in-LLM-RL · GitHub",
            "url": "https://github.com/xxzcc/Awesome-Credit-Assignment-in-LLM-RL"
          },
          {
            "title": "GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub",
            "url": "https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details about arXiv:2604.09459:\n\n**Title:** From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\n\n**Author:** Chenchen Zhang\n\n**Publication Date:** April 10, 2026\n\n**Overview:** This is a survey of reinforcement learning (RL) for large language models that increasingly relies on sparse, outcome-level rewards, yet determining which actions within a long trajectory caused the outcome remains difficult.\n\n**Two Main Problem Regimes:** The credit assignment problem manifests in two regimes: reasoning RL, where credit must be distributed across tokens and steps within a single chain-of-thought generation (500–30K+ tokens); and agentic RL, where multi-turn environment interaction introduces stochastic transitions, partial observability, and horizons of 100+ turns (100K–1M tokens).\n\n**Taxonomy & Scope:** The survey covers 47 CA methods (41 core, 6 adjacent enablers) published between 2024 and early 2026, organizing them in a two-dimensional taxonomy by assignment granularity (token, segment, step, turn, multi-agent) and methodology (Monte Carlo, temporal difference, model-based, game-theoretic, information-theoretic).\n\n**Key Insights:** The shift from reasoning to agentic RL complicates and reshapes the credit assignment landscape: reasoning CA is maturing around process reward models and critic-free group comparison, while agentic CA is driving genuinely new approaches including hindsight counterfactual analysis, privileged asymmetric critics, and turn-level MDP reformulations."
    ],
    "durationSeconds": 8.553415336999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "eb13c4a4-49c5-441e-8e44-d6f0ba7d5904",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 81_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research context. Let me synthesize my findings and provide my assessment.  ---  【状态】…",
  "leafUuid": "086c9fc1-2ca5-455a-b4f7-afcd02b05b5d",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 82_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Tool call

_source line 83 · 2026-05-27T08:43:15.525Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hh9kPjrRqRr18Dh84wpdv1`</summary>

```json
{
  "query": "PROGRS outcome-conditioned centering UGCA composable process reward orthogonal step-level trajectory-level 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "086c9fc1-2ca5-455a-b4f7-afcd02b05b5d",
  "isSidechain": false,
  "requestId": "req_011CbSn3pXsETj5cdEwMCq3a",
  "type": "assistant",
  "uuid": "9ec5a05b-a3c1-4538-a656-72db6ab604e8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GivfTxZ8TyMscFJbJzsven",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4766,
      "cache_read_input_tokens": 84927,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4766,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 84927,
          "cache_creation_input_tokens": 4766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4766
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

_source line 84 · 2026-05-27T08:43:22.850Z_

<details><summary>↩ Tool result · `toolu_01Hh9kPjrRqRr18Dh84wpdv1`</summary>

```text
Web search results for query: "PROGRS outcome-conditioned centering UGCA composable process reward orthogonal step-level trajectory-level 2026"

Links: [{"title":"LLM Reasoning with Process Rewards for Outcome-Guided Steps","url":"https://arxiv.org/pdf/2604.02341"},{"title":"Self-Guided Process Reward Optimization with Redefined Step-wise Advantage for Process Reinforcement Learning","url":"https://arxiv.org/html/2507.01551v2"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"},{"title":"Do We Need to Verify Step by Step? Rethinking Process Supervision from a   Theoretical Perspective","url":"https://arxiv.org/pdf/2502.10581"},{"title":"Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks","url":"https://arxiv.org/pdf/2509.25598"},{"title":"Intra-Trajectory Consistency for Reward Modeling","url":"https://arxiv.org/pdf/2506.09096"},{"title":"PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization","url":"https://arxiv.org/pdf/2601.07182"}]

Based on the search results, I found highly relevant information about PROGRS:

PROGRS is a framework that leverages process reward models (PRMs) while keeping outcome correctness dominant. It treats process rewards as relative preferences within outcome groups rather than absolute targets, and introduces outcome-conditioned centering, which shifts PRM scores of incorrect trajectories to have zero mean within each prompt group.

To stabilize process signals, PROGRS combines a frozen quantile-regression PRM with a multi-scale coherence evaluator that penalizes short-window confidence volatility, and integrates the resulting centered process bonus into Group Relative Policy Optimization (GRPO) without auxiliary objectives or additional trainable components.

Across MATH-500, AMC, AIME, MinervaMath, and Olympiad-Bench, PROGRS consistently improves Pass@1 over outcome-only baselines (e.g., 74.9% vs. 69.7% on MATH-500; 59.0% vs. 52.0% on AMC-2023) and achieves stronger performance with fewer rollouts.

The search results show this is recent research focused on improving LLM reasoning with process rewards through outcome-conditioned centering and integration with GRPO for mathematical reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ec5a05b-a3c1-4538-a656-72db6ab604e8",
  "isSidechain": false,
  "promptId": "dbd08305-8867-4492-a248-7049e3b5ee25",
  "type": "user",
  "uuid": "01e71cc3-913e-4f27-b8a2-c3c95b90e814",
  "toolUseResult": {
    "query": "PROGRS outcome-conditioned centering UGCA composable process reward orthogonal step-level trajectory-level 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XkqTE9M2z59GyG2eMZ4Hmo",
        "content": [
          {
            "title": "LLM Reasoning with Process Rewards for Outcome-Guided Steps",
            "url": "https://arxiv.org/pdf/2604.02341"
          },
          {
            "title": "Self-Guided Process Reward Optimization with Redefined Step-wise Advantage for Process Reinforcement Learning",
            "url": "https://arxiv.org/html/2507.01551v2"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2509.26578"
          },
          {
            "title": "Do We Need to Verify Step by Step? Rethinking Process Supervision from a   Theoretical Perspective",
            "url": "https://arxiv.org/pdf/2502.10581"
          },
          {
            "title": "Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks",
            "url": "https://arxiv.org/pdf/2509.25598"
          },
          {
            "title": "Intra-Trajectory Consistency for Reward Modeling",
            "url": "https://arxiv.org/pdf/2506.09096"
          },
          {
            "title": "PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization",
            "url": "https://arxiv.org/pdf/2601.07182"
          }
        ]
      },
      "Based on the search results, I found highly relevant information about PROGRS:\n\nPROGRS is a framework that leverages process reward models (PRMs) while keeping outcome correctness dominant. It treats process rewards as relative preferences within outcome groups rather than absolute targets, and introduces outcome-conditioned centering, which shifts PRM scores of incorrect trajectories to have zero mean within each prompt group.\n\nTo stabilize process signals, PROGRS combines a frozen quantile-regression PRM with a multi-scale coherence evaluator that penalizes short-window confidence volatility, and integrates the resulting centered process bonus into Group Relative Policy Optimization (GRPO) without auxiliary objectives or additional trainable components.\n\nAcross MATH-500, AMC, AIME, MinervaMath, and Olympiad-Bench, PROGRS consistently improves Pass@1 over outcome-only baselines (e.g., 74.9% vs. 69.7% on MATH-500; 59.0% vs. 52.0% on AMC-2023) and achieves stronger performance with fewer rollouts.\n\nThe search results show this is recent research focused on improving LLM reasoning with process rewards through outcome-conditioned centering and integration with GRPO for mathematical reasoning tasks."
    ],
    "durationSeconds": 7.321064652000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9ec5a05b-a3c1-4538-a656-72db6ab604e8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 85 · 2026-05-27T08:43:22.857Z_

```json
{
  "parentUuid": "01e71cc3-913e-4f27-b8a2-c3c95b90e814",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4cac6915-cfa0-450b-bd82-09da2d01cd51",
  "timestamp": "2026-05-27T08:43:22.857Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 86 · 2026-05-27T08:43:44.199Z_

<details><summary>Logged reasoning block</summary>

```text
Good. The CA survey (arXiv 2604.09459) is confirmed to exist and describes 47 methods in a taxonomy with 5 methodology categories (Monte Carlo, temporal difference, model-based, game-theoretic, information-theoretic). The discovery agent's claim that UGCA could represent a 6th "calibration-based" category is plausible.

PROGRS confirmed to use outcome-conditioned centering at trajectory level - the combination experiment suggestion is sound since PROGRS and UGCA operate at different granularities.

Now let me produce the final output. Since I'm deciding to converge, I need to:


1. Output the Round 3 iterative assessment with decision = 收敛
2. Output the final 角色 C content (优化方案)

For the final probability estimate, the improvements from Round 3 are refinements rather than breakthroughs, the idea quality ceiling stays around 48-50%, and while experiment completeness is now very strong, compute budget and timeline risk have increased. This puts me at 40% as the median estimate, which exceeds the 36% threshold, so I'll output the 优化方案.

Now I'm deciding which suggestions to adopt and which to reject.

From Discovery Round 3, I'm adopting the reward hacking framing as a structural property enhancement, moving the MSE-optimal derivation to the main paper for better presentation, citing the CA survey with appropriate restraint without overclaiming a "6th category," and incorporating calibration drift as an acknowledged limitation in the method section.

From Remedy Round 3, I'm adopting the cross-family protocol specifics with concrete thresholds and go/no-go gates, the UGCA plus PROGRS combination as a key experiment requiring about 270 hours, the simplified PROGRS reproduction as a practical fallback, and the longitudinal calibration protocol with options combining specific degradation thresholds and actionable monitoring.

Adding the reduced-scale Process-Outcome Credit comparison at roughly 70 hours and the process credit formulation ablation at roughly 60 hours, plus a 50-hour contingency buffer, brings the additional compute from this round to approximately 450 hours, pushing the total project to around 3,350 H100-hours.

Now I need to decide whether to output both the convergence assessment and the final optimization plan together, or wait for a separate signal. The instructions suggest the system tells me when the process ends, but outputting both in one response makes more sense than creating an unnecessary extra step—I'll go ahead and produce the complete convergence decision along with the final optimization plan.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cac6915-cfa0-450b-bd82-09da2d01cd51",
  "isSidechain": false,
  "requestId": "req_011CbSn4gaQjvJiwLSpgKwha",
  "type": "assistant",
  "uuid": "387e89e0-9fa5-4358-aefa-3b5a897ac145",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YcLZ9jrjANtrZF4MGvL25p",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 89693,
      "output_tokens": 6689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6689,
          "cache_read_input_tokens": 89693,
          "cache_creation_input_tokens": 820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 820
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

_source line 87 · 2026-05-27T08:45:45.699Z_

验证完毕。现在整合第 3 轮输出并做出最终决策。

【阶段】: 迭代第 3 轮

【交叉验证调研】:
1. **Credit Assignment Survey (arXiv 2604.09459, Apr 2026)** — 已验证存在。覆盖 47 种 CA 方法，taxonomy 为 (granularity: token/segment/step/turn/multi-agent) × (methodology: Monte Carlo, temporal difference, model-based, game-theoretic, information-theoretic)。确认 5 种 methodology 类别中没有 "calibration-based"。发掘 agent 建议 UGCA 作为第 6 种方法论类别的定位有依据，但不应 overclaim。
2. **PROGRS 与 UGCA 的正交性** — PROGRS 的 outcome-conditioned centering 在 trajectory-level 操作（对 prompt group 内 incorrect trajectories 的 PRM scores 做零均值化），UGCA 在 step-level 操作（per-step α gating）。两者操作粒度不同，逻辑上正交可组合。补救 agent 的组合实验建议合理。

【发掘 agent 有效建议采纳】:
1. **Reward hacking 作为结构性属性（发掘点 1）** — **逻辑自洽，采纳**。当 PRM 在 OOD/adversarial policy 输出上被 exploit 时，calibrated CI 天然变宽 → α 降低 → 自动 down-weight 不可靠 process credit。这是方法设计的内在属性，不仅是事后观测。提升到 method section 作为 "calibration-mediated implicit defense against reward hacking" claim。
2. **MSE-optimal 推导提升至主文 Proposition（发掘点 2）** — **采纳**。在 Gaussian noise 假设下 MSE-optimal 插值权重为 w_i 的单调递减函数，sigmoid 为其 parametric approximation。从 appendix 提升为 main paper 的 Proposition，回答 "why sigmoid" 问题。
3. **CA survey taxonomy 定位（发掘点 3）** — **已验证，部分采纳**。引用 survey (arXiv 2604.09459)，指出 UGCA 在其 5-category methodology taxonomy 外引入 calibration-based 方法论。但不以 "创立第 6 种 category" 为主要 contribution claim——这个定位留给 reviewer 自行判断，论文中 subtly 指出即可。
4. **Calibration drift 作为 aware limitation（发掘点 4）** — **采纳**。与补救 agent 缺陷 4 收敛到同一方向。将 calibration drift 从实验 section 的被动检查提升为 method section 的主动讨论：(a) 明确为 operating assumption；(b) 讨论 graceful degradation 行为（drift 时 α 趋向更 conservative 的 outcome credit）；(c) 提出 re-calibration trigger protocol。

【补救 agent 有效建议采纳】:
1. **Cross-family PRM 协议细化（缺陷 1）** — **采纳**。明确：(a) step-level ground truth via MC estimation (N=8-16 completions, outcome-based); (b) degradation threshold: ECE > 0.10 or Brier score relative degradation > 20%; (c) contingency budget: 70h; (d) week 1 go/no-go gate。
2. **UGCA + PROGRS 组合实验（缺陷 2）** — **采纳**。在 8B 上增加 UGCA+PROGRS 条件（先做 trajectory-level centering，再做 per-step α gating），测试正交互补性。+270h。这几乎必然被 reviewer 要求，proactive 做好。
3. **PROGRS 简化复现 fallback（缺陷 3）** — **采纳**。若完整复现困难，实现 PROGRS core（outcome-conditioned centering + frozen quantile PRM），标注为 "PROGRS (core)"。GRPO-λ 可用 Open-R1 框架直接跑。
4. **Longitudinal calibration 可执行协议（缺陷 4）** — **采纳**。升级为：ECE 相对初始值恶化 > 50% 时触发 quick re-calibration（仅更新 quantile heads，~15h）。按 training phase 分段报告 UGCA gain（前 50% vs 后 50%）以展示 calibration drift 的实际影响。
5. **Reduced-scale Process-Outcome Credit 比较（缺陷 5）** — **采纳**。1.7B, 50% training, 1 seed, MC rollouts N=4。~70h。标注 "reduced-scale comparison"，配合理论 FLOPs 分析。
6. **Process credit formulation ablation（缺陷 6）** — **采纳**。1.7B 上对比 UGCA + sum-form vs. UGCA + min-form。~60h。隔离 gating 贡献 vs. min-form 选择。

【本轮 proposal 主要变更】:

*Idea 层面变更：*
- Reward hacking robustness 从实验观测提升为方法的结构性属性（calibration-mediated implicit defense）
- MSE-optimal interpolation weight Proposition 从 appendix 提升至 main paper
- 引用 CA survey (arXiv 2604.09459) 定位 UGCA 在方法论 taxonomy 中的位置
- Calibration drift 作为 operating assumption 在 method section 主动讨论

*实验层面变更：*
- 新增 UGCA + PROGRS 组合实验（8B, 3 seeds）
- 新增 reduced-scale Process-Outcome Credit 比较（1.7B）
- 新增 process credit formulation ablation（sum-form vs min-form, 1.7B）
- Cross-family PRM 协议细化（具体阈值、MC ground truth、go/no-go gate）
- Longitudinal calibration 协议升级为可执行（re-calibration trigger + phase-segmented reporting）
- 资源更新至 ~3350 H100-hours

【idea 质量评估】: Novelty=中-强 Significance=中-强 → idea 天花板约 48%
- Novelty 不变。MSE-optimal Proposition 和 reward hacking 结构性属性增强了理论 grounding 和 impact narrative，但核心贡献的 novelty 本质未变。
- Significance 微增。Reward hacking robustness 作为结构性属性 + CA taxonomy 新类别的定位，使 significance narrative 更有力。

【实验完备性评估】: Technical Soundness=强 → 地板坚固
- UGCA+PROGRS 组合实验是关键增补，直接证明 per-step gating 与 trajectory-level centering 的正交互补性。
- Reduced-scale competitive comparison 堵住 "为什么不比最相似的方法" 质疑。
- Process credit formulation ablation 隔离 gating 贡献。
- 协议细化（cross-family threshold、re-calibration trigger）使实验可执行性更强。

【当前概率估计】: [34% - 47%] 中位 40%

【决策】: 收敛

【决策理由】: 满足"连续 2 轮只做微调"收敛条件。Round 2 的改进（bias 分解、2×2 矩阵、longitudinal tracking、assumption validation）和 Round 3 的改进（reward hacking 结构性属性、MSE Proposition 提升、UGCA+PROGRS 组合、protocol 细化）均为已有框架的精炼而非结构性变更。两位 worker 在 Round 3 发现的问题粒度明显更细（presentation 层面的提升、protocol 的具体阈值、additional ablation），表明 proposal 已接近该 idea 质量天花板下的最优表达。继续迭代的边际收益不足以抵消 scope creep 和 compute budget 膨胀的风险。

---

## 角色 C：最终输出

中位 40% ≥ 36%，判定通过。以下为对比**原始 proposal** 的优化方案。

【优化方案】

**1. [Core Problem / Introduction] — 增加 bias 分解论述 — 命中 Novelty + Soundness**
将 "PRM miscalibration leads to reward hacking" 的笼统表述分解为两种 bias：(a) PRM miscalibration bias（PRM 分数偏离真实 step correctness，严重度在不同 step types 间异质），(b) aggregation bias（min-form 等聚合方式的结构性偏差）。明确 UGCA 精准解决 (a)，preemptively 回应 "min-form bias 怎么办" 的审稿质疑。同时强化 "per-step heterogeneity" 作为 per-step gating 必要性的核心论据。

**2. [Research Landscape] — 2×2 design space 定位矩阵 + 7 篇新 related work — 命中 Related Work 差异化**
构建 (signal source: verifier calibration vs. intrinsic/structural) × (granularity: per-step vs. trajectory-level) 矩阵，UGCA 占据 (verifier calibration, per-step) 的唯一空白格。新增：
- arXiv 2602.01034 (Discovering Process-Outcome Credit): per-step mixing 但用 MC information gain
- arXiv 2601.18984 (VPPO/Save the Good Prefix): binary per-step PRM gating
- arXiv 2509.21154 (GRPO is Secretly a PRM, ICLR 2026): GRPO 隐式包含 uniform process credit
- ConfClip (arXiv 2509.17730): policy confidence-weighted reward
- Reward Under Attack (arXiv 2603.06621): PRM 系统性可 exploit
- DAPO: 当前标准 outcome-only baseline
- CA survey (arXiv 2604.09459): 47 种 CA 方法 taxonomy，UGCA 引入 calibration-based 类别

**3. [Proposed Approach — Novelty framing] — 从 "bridging calibration and RL" 重构为 "uncertainty-driven bias-variance tradeoff" — 命中 Novelty 天花板**
Process credit = low-variance but PRM-bias-dependent; outcome credit = unbiased but high-variance; α_i 在 bias-variance frontier 上做 per-step optimal interpolation。将核心 insight 锐化为 "separating what the verifier predicts (PRM score) from how confident the verifier is (calibrated CI width)"。

**4. [Proposed Approach — Theoretical grounding] — MSE-optimal Proposition 进入 main paper — 命中 Novelty + Soundness**
在 Gaussian noise 假设下推导 MSE-optimal interpolation weight 为 w_i 的单调递减函数，sigmoid 为其 parametric approximation。以 Proposition 形式写入 Section 3，回答 "why sigmoid, why not other gating forms"。从 "theoretically motivated" 升级为 "theoretically grounded"。

**5. [Proposed Approach — Trivial alternatives] — 显式讨论并排除 3 个简单替代 — 命中 Novelty 防御**
Method section 中正面回应：(1) raw PRM score magnitude gating（混淆 prediction 和 confidence）；(2) global clipping/truncation（丢弃部分置信步骤的有用信息）；(3) PROGRS trajectory-level centering（忽略 per-step calibration heterogeneity）。

**6. [Proposed Approach — Reward hacking] — 将 robustness 从实验观测提升为结构性属性 — 命中 Significance**
Claim: UGCA 提供 calibration-mediated implicit defense——当 PRM 在 adversarial/OOD 输入上被 exploit 时，calibrated CI 天然变宽 → α 降低 → 自动 down-weight 不可靠 process credit。配合 "Reward Under Attack" (arXiv 2603.06621) 的 motivation 形成闭环。

**7. [Proposed Approach — Limitations] — Calibration drift 作为主动讨论的 operating assumption — 命中 Soundness**
在 method section 中承认 frozen PRM 的 calibration 可能随 policy drift 退化，讨论 graceful degradation 行为和 re-calibration trigger protocol（ECE 恶化 > 50% 时触发 quantile heads re-calibration）。

**8. [Broader Significance] — "Verifier-Uncertainty-Aware RL" 通用原则 — 命中 Significance**
将 UGCA 定位为 "principled degradation under verifier uncertainty" 的实例化，math reasoning 作为 clean testbed，code generation/scientific reasoning/agentic tasks 作为 discussion-level 延伸。

**9. [Experimental Design — Baselines] — 从 3 个扩展到 7 个（1.7B）/ 6 个（8B） — 命中 Technical Soundness**
原始：PURE, GRPO, GRPO-λ。增加：DAPO（标准 outcome-only）, PROGRS（trajectory-level calibrated PRM, 最近竞争者）, PRPO（固定 process-outcome shift, 1.7B）, VPPO（binary per-step gating, 1.7B）。8B 增加 UGCA+PROGRS 组合条件测试正交互补性。

**10. [Experimental Design — Benchmarks] — 从 4 个扩展到 6 个 + Pass@8 — 命中 Technical Soundness**
原始：MATH-500, AMC23, AIME24, OlympiadBench。增加：AIME 2025（已成为 2026 年标准）, MinervaMath（PROGRS 采用，增强可比性）。AIME benchmarks 增加 Pass@8 分析以缓解 30-problem small sample size 限制。

**11. [Experimental Design — Reward hacking 量化] — 定义 3 个具体指标 — 命中 Technical Soundness**
原始仅提及 "demonstrating measurably reduced reward hacking" 和 "reward-hacking diagnostics" 但未定义指标。增加：(1) PRM-Accuracy Gap (PAG) overoptimization curves；(2) per-step uncertainty-conditioned accuracy（5 quantile bins）；(3) reward hacking rate（PRM score > threshold 但答案错误的 trajectory 比例）。

**12. [Experimental Design — Ablation 扩展] — 从超参数搜索扩展到完整消融矩阵 — 命中 Technical Soundness**
原始仅有 "ablations over τ, β, quantile level"。新增：boundary cases (α≡1/α≡0)、hard vs soft gating、raw PRM score gating vs calibrated CI width gating、calibrated vs uncalibrated uncertainty、process credit formulation (sum-form vs min-form)、UGCA+PROGRS 组合。

**13. [Experimental Design — Assumption 验证] — 新增 core assumption + longitudinal tracking + cross-family 细化 — 命中 Technical Soundness**
新增：(a) per-step w_i vs PRM accuracy rank correlation 验证核心假设；(b) 每 25% training progress 的 ECE/Brier + α distribution drift 纵向追踪（含 re-calibration trigger）；(c) cross-family validation 细化（MC estimation N=8-16 for ground truth, ECE > 0.10 degradation threshold, week 1 go/no-go gate）。

**14. [Experimental Design — Competitive comparison] — Reduced-scale "Discovering Process-Outcome Credit" 比较 — 命中 Technical Soundness**
在 1.7B 上做 reduced-scale 实证比较（50% training, 1 seed, MC N=4），配合理论 FLOPs 分析，避免 "跳过最相似方法" 的审稿质疑。

**15. [Experimental Design — 统计 + 公平性] — Multi-seed + bootstrap + compute Pareto — 命中 Technical Soundness**
原始未提及统计显著性。增加：1.7B 3 seeds (mean ± std)；8B top 2 configs × 3 seeds + bootstrap CIs (1000 resamples)；wall-clock + FLOPs 对比 + accuracy-vs-compute Pareto curves。

**16. [Key References] — 从 11 篇扩展到 18 篇 — 命中 Related Work 完整性**
新增：arXiv 2509.21154 (ICLR 2026), arXiv 2602.01034, arXiv 2601.18984, arXiv 2509.17730, arXiv 2603.06621, DAPO, arXiv 2604.09459。

【主要风险】:
1. **Empirical gains 可能不够大**: UGCA 的 per-step gating 与 PROGRS 的 trajectory-level centering 之间的实际性能差距可能仅 1-2 个百分点，不足以让 reviewer 认定 per-step granularity 的额外复杂度是值得的。如果 UGCA+PROGRS 组合实验未显示显著增益，这一风险会放大。**缓解**：强调 reward hacking robustness（PAG curves、reward hacking rate）作为 UGCA 的差异化优势——即使 accuracy gain 较小，reduced reward hacking 本身有独立价值。
2. **Cross-family PRM calibration 退化**: Qwen2.5-Math-PRM-7B 在 Qwen3 rollouts 上的 calibration 质量可能显著退化，导致 gating 信号失真。如果 week 1 go/no-go gate 发现 ECE > 0.10，需要额外 ~70h 进行 re-calibration，压缩后续时间线。**缓解**：已设 contingency budget 和 fallback 协议。

【实施评估】:
- **计算资源**: ~3350 H100-hours。建议 8×H100 节点，每个 Qwen3-8B RL run 约 25h wall-clock。1.7B ablations 可在 4×H100 或更少上并行。若有多节点集群，8B 的 6 configs 可部分并行，实际 wall-clock 约 4-5 周 GPU 密集期。
- **数据需求**: MATH 训练集 (8K prompts, 公开可得)；MATH-500, AMC23, AIME 2024, AIME 2025, OlympiadBench, MinervaMath 评测集 (均公开可得)。PRM quantile calibration 需 validation set (MATH 子集或 PRM-Bench, 公开可得)。Cross-family validation 需 Qwen3-8B initial rollouts 的 MC completions (自行生成)。
- **人工介入**: 最小。PROGRS core reproduction 需 3-5 天工程工作；GRPO-λ 基于公式 straightforward 实现。无需人工标注。Paper writing 需 1 周专注时间。若使用 Claude 辅助（human-in-loop 模式），可压缩 codebase integration 和 analysis 时间。
- **训练需求**: 需要训练 Qwen3-8B 和 Qwen3-1.7B 的 RL fine-tuning（GRPO-based, 非从头训练）。PRM quantile regression head 的 calibration fine-tuning (frozen backbone, 仅更新 regression heads)。无需预训练或大规模 SFT。
- **新 Benchmark**: 不需要构建新 benchmark。所有评测集均为已有公开 benchmark。Reward hacking 量化指标为计算指标，不需要新数据标注。
- **预估周期**: 8 周（从启动到可投稿）。关键路径：wk1 cross-family PRM validation (go/no-go gate) → wk3-4 1.7B ablations → wk5-6 8B runs → wk7 analysis → wk8 writing。如果 cross-family validation 需 re-calibration，wk2 执行，后续顺延但仍可在 8 周内完成。Timeline 紧张但可行，前提是 GPU 资源到位且无重大技术障碍。总 GPU 成本约 $8,400（H100 spot ~$2.50/hr）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "387e89e0-9fa5-4358-aefa-3b5a897ac145",
  "isSidechain": false,
  "requestId": "req_011CbSn4gaQjvJiwLSpgKwha",
  "type": "assistant",
  "uuid": "e0698913-11f2-423c-a1fa-2b7031366638",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YcLZ9jrjANtrZF4MGvL25p",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 89693,
      "output_tokens": 6689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6689,
          "cache_read_input_tokens": 89693,
          "cache_creation_input_tokens": 820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 820
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

_source line 88_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research context. Let me synthesize my findings and provide my assessment.  ---  【状态】…",
  "leafUuid": "e0698913-11f2-423c-a1fa-2b7031366638",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 89_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 90_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research context. Let me synthesize my findings and provide my assessment.  ---  【状态】…",
  "leafUuid": "e0698913-11f2-423c-a1fa-2b7031366638",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 91_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 92_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 93 · 2026-05-27T08:45:47.063Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:45:47.063Z",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "content": "【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。"
}
```

---

### Runtime record

_source line 94 · 2026-05-27T08:45:47.064Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:45:47.064Z",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

## Round 6

5 recorded events

### User

_source line 95 · 2026-05-27T08:45:47.139Z_

【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0698913-11f2-423c-a1fa-2b7031366638",
  "isSidechain": false,
  "promptId": "c494ec71-7b87-4071-9e15-3a393eed672c",
  "type": "user",
  "uuid": "ac495bf7-f818-4e59-a989-e1be3fe5baa9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 96 · 2026-05-27T08:46:01.049Z_

<details><summary>Logged reasoning block</summary>

````text
The user is asking me to output the final 角色 C content in the specified format. I already produced this in my previous response, but let me clean it up and make sure it follows the exact format specified. Let me re-read the format requirements:

"若通过（收敛且中位 ≥ 36%）→ 输出优化方案文本（对比原始 proposal 的修改建议列表）+ 实施评估"

Format:
```
【优化方案】

1. [位置 / 章节] — [具体改动] — [命中哪个评审维度的加分]


```

Now I need to structure the optimization recommendations with specific locations and changes, then identify the key risks that reviewers might challenge and provide a practical implementation assessment covering computational resources, data requirements, and any manual intervention needed.

```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac495bf7-f818-4e59-a989-e1be3fe5baa9",
  "isSidechain": false,
  "requestId": "req_011CbSnFKUDdB2R2mGrChC4K",
  "type": "assistant",
  "uuid": "b23c6b25-691b-4374-bf10-06f31f82e92e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FkWWfVjo6mjUqJxkU2YQj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6766,
      "cache_read_input_tokens": 90513,
      "output_tokens": 5568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6766,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5568,
          "cache_read_input_tokens": 90513,
          "cache_creation_input_tokens": 6766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6766
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

_source line 97 · 2026-05-27T08:47:33.399Z_

【优化方案】

1. [Core Problem / Introduction — 第 1 段] — 增加 bias 分解论述：将 "PRM miscalibration leads to reward hacking" 分解为 (a) PRM miscalibration bias（PRM 分数偏离真实 step correctness，严重度在 step types 间异质：计算步骤 well-calibrated，概念推理步骤 poorly calibrated）和 (b) aggregation bias（min-form 的结构性保守偏差）。明确 UGCA 精准解决 (a)，preemptively 回应 "min-form bias 怎么办"。同时以 per-step heterogeneity 作为 per-step gating 必要性的核心论据，回应 "为什么不用全局方法" — 命中 **Novelty 防御 + Soundness**

2. [Research Opportunity — 第 1 段] — 将核心 novelty framing 从 "bridging PRM calibration and RL credit assignment" 重构为 "uncertainty-driven bias-variance tradeoff in per-step credit assignment"。Process credit = low-variance but potentially biased（依赖 PRM 校准质量）；outcome credit = unbiased but high-variance（sparse, trajectory-level）；α_i 在 bias-variance frontier 上做 per-step optimal interpolation，由 PRM 校准置信区间宽度 w_i 驱动。锐化核心 insight 为 "separating what the verifier predicts from how confident the verifier is" — 命中 **Novelty 天花板提升**

3. [Research Landscape — 全段重组] — 构建 2×2 design space 定位矩阵：(signal source: verifier calibration vs. intrinsic/structural) × (granularity: per-step vs. trajectory-level)，UGCA 占据 (verifier calibration, per-step) 唯一空白格。引用 credit assignment survey (arXiv 2604.09459, Apr 2026) 的 5-category methodology taxonomy（MC, TD, model-based, game-theoretic, information-theoretic），指出 UGCA 引入 calibration-based 方法论类别。新增 7 篇 related work 并做差异化论述：
   - arXiv 2602.01034 (Discovering Process-Outcome Credit): per-step mixing via MC information gain — 差异：计算开销高一个数量级、estimation variance 大
   - arXiv 2601.18984 (VPPO / Save the Good Prefix): binary per-step PRM first-error gating — 差异：hard gating 无法处理 PRM 不确定性
   - arXiv 2509.21154 (GRPO is Secretly a PRM, ICLR 2026): GRPO 隐式 uniform process credit — 差异：UGCA 提供 missing per-step adaptivity
   - ConfClip (arXiv 2509.17730): policy model confidence-weighted reward — 差异：policy-side signal 随训练漂移，UGCA 用 frozen external verifier 的 calibrated uncertainty
   - Reward Under Attack (arXiv 2603.06621): PRM 系统性可 exploit 为 fluency detectors — 支撑 UGCA motivation
   - DAPO: 当前标准 outcome-only baseline
   - CA survey (arXiv 2604.09459): taxonomy 定位参照
   — 命中 **Related Work 差异化（堵住 missing reference 质疑）**

4. [Proposed Approach — Method section 新增 "Why not simpler alternatives" 段] — 在方法描述后显式讨论并排除 3 个 trivial alternatives：(1) raw PRM score magnitude gating（混淆 prediction 和 confidence——PRM 可以很自信地给出错误高分）；(2) global clipping/truncation（丢弃部分置信步骤的有用信息）；(3) PROGRS trajectory-level centering（忽略 per-step calibration heterogeneity，所有步骤接受相同处理）。这将 reviewer 最可能的第一反应 "为什么不用更简单方法" 在 method section 就化解 — 命中 **Novelty 防御**

5. [Proposed Approach — Theoretical grounding 段] — 将 MSE-optimal interpolation weight 推导从 appendix 提升至 main paper，以 Proposition 形式呈现：在 PRM score = true correctness + Gaussian noise(0, σ²(w_i)) 模型下，最小化 per-step credit assignment MSE 的 optimal 插值权重是 w_i 的单调递减函数，sigmoid 为其 parametric family。直接回答 "why sigmoid? why not other gating forms?"——因为 sigmoid 是理论最优解的近似，不是 ad hoc 设计选择。该领域大多数方法缺乏 prescriptive justification for design choices，这是稀缺的差异化优势 — 命中 **Novelty 理论层次提升 + Soundness**

6. [Proposed Approach — 新增 "Reward hacking robustness as structural property" 段] — 将 reward hacking robustness 从实验观测提升为方法的设计内属性：当 PRM 在 OOD/adversarial policy 输出上被 exploit 时，calibrated CI 天然变宽 → α 降低 → 自动 down-weight 不可靠 process credit。这是 calibration-mediated implicit defense，不需要额外机制。配合 "Reward Under Attack" (arXiv 2603.06621) 的 motivation 形成闭环——该工作证明 PRMs 可被 exploit 到 PRM score >0.9 但 accuracy <4%，UGCA 的设计正好针对此 failure mode — 命中 **Significance 提升（reward hacking 是 2025-2026 高关注问题）**

7. [Proposed Approach — 新增 "Operating assumptions and limitations" 段] — 在 method section 主动讨论 calibration drift：frozen PRM 的 calibration 可能随 policy distribution drift 退化，这是 UGCA 的 operating assumption。讨论 graceful degradation 行为（drift 时 CI 趋宽 → α 趋低 → 系统自然偏向更保守的 outcome credit）以及 re-calibration trigger protocol（ECE 相对初始值恶化 > 50% 时触发 quantile heads re-calibration）。比在实验 section 被动检查更主动，显示对方法局限的深刻理解 — 命中 **Soundness（preemptive defense）**

8. [Broader Significance — 新增段] — 将 UGCA 抽象为 "Verifier-Uncertainty-Aware RL" 通用原则：任何使用不完美 verifier 的 RL 训练都应根据 verifier 的 per-instance confidence 动态调整 credit assignment。Math reasoning 定位为 clean testbed（PRM uncertainty 可测量、可校准），code generation / scientific reasoning / agentic tasks 作为 discussion-level 延伸方向。不 overclaim generalization without evidence — 命中 **Significance（影响面扩大）**

9. [Experimental Design — Baselines] — 从原始 3 个 (PURE, GRPO, GRPO-λ) 扩展至 8B 6 个 + 1.7B 7 个：+DAPO（当前标准 outcome-only baseline，所有 2026 论文必含）、+PROGRS（最接近竞争者，trajectory-level calibrated PRM centering）、+PRPO（固定 process-outcome structural shift, 1.7B only）、+VPPO（binary first-error per-step gating, 1.7B only）。新增 UGCA+PROGRS 组合条件（8B, 3 seeds）测试正交互补性——先做 trajectory-level centering 再做 per-step α gating，直接回答 "这两个方法是否冗余" — 命中 **Technical Soundness（baseline 覆盖度是常见 reject 原因）**

10. [Experimental Design — Benchmarks] — 从 4 个扩展到 6 个 + Pass@K：+AIME 2025（2026 年已成标准评测）、+MinervaMath（PROGRS 采用，增强可比性）。AIME 2024/2025 增加 Pass@8 分析缓解 30-problem small sample size 限制 — 命中 **Technical Soundness**

11. [Experimental Design — 新增 "Reward hacking quantification" 段] — 定义 3 个具体量化指标（原始 proposal 仅笼统提及 "demonstrating measurably reduced reward hacking"）：(1) PRM-Accuracy Gap (PAG) overoptimization curves（定期采样 rollouts，绘制 mean PRM score vs ground-truth pass rate）；(2) per-step uncertainty-conditioned accuracy（按 w_i 分 5 quantile bins，每 bin 报告 step correctness）；(3) reward hacking rate（PRM score > threshold 但答案错误的 trajectory 比例）。均有文献先例（Reward Under Attack, Uncertainty-Aware Reward Discounting） — 命中 **Technical Soundness（核心 claim 的可量化验证）**

12. [Experimental Design — Ablation 全面重设计] — 从原始 "hyperparameter sweep over τ, β, quantile level" 扩展为完整消融矩阵（全部在 1.7B, 3 seeds）：(a) boundary cases α≡1 / α≡0 验证插值优于两极端；(b) hard vs soft gating 证明 sigmoid 优于 binary threshold；(c) raw PRM score gating vs calibrated CI width gating 验证 calibration 的必要性（最关键 ablation，分离 "prediction" 与 "confidence"）；(d) calibrated vs uncalibrated uncertainty 隔离 calibration 贡献；(e) process credit formulation: sum-form vs min-form 隔离 gating 贡献 vs min-form 选择；(f) 原有 hyperparameter sensitivity — 命中 **Technical Soundness（组件贡献隔离是顶会审稿标准要求）**

13. [Experimental Design — 新增 "Core assumption validation" 段] — per-step w_i 分 5 quantile bins，每 bin 计算 PRM step-level prediction accuracy（非仅 policy correctness）。报告 Spearman rank correlation between w_i and PRM prediction error。若 narrow-w_i bins 确实有更高 PRM accuracy，验证核心假设（CI width proxies PRM reliability）。若验证失败，讨论 alternative gating signals — 命中 **Soundness（核心假设验证，两位独立 worker 同时识别为关键 gap）**

14. [Experimental Design — 新增 "Longitudinal PRM calibration tracking" 段] — 每 25% training progress checkpoint 计算 frozen PRM 在新鲜 rollouts 上的 ECE/Brier score + α distribution drift。具体协议：ECE 相对初始值恶化 > 50% 时触发 quick re-calibration（仅更新 quantile heads, ~15h）。按 training phase 分段报告 UGCA gain（前 50% vs 后 50%），展示 calibration drift 的实际影响 — 命中 **Soundness（RL + frozen reward model 的 distribution shift 是审稿人高度敏感点）**

15. [Experimental Design — 新增 "Cross-family PRM validation" 细化] — 原始 proposal 仅笼统提及 "ECE and Brier score comparison"。细化为：(a) step-level ground truth via MC estimation (N=8-16 completions, outcome-based correctness proxy)；(b) degradation threshold: ECE > 0.10 or Brier score 相对恶化 > 20%；(c) contingency: 70h H100 for re-calibration；(d) week 1 go/no-go gate — 命中 **Soundness + Feasibility**

16. [Experimental Design — 新增 reduced-scale competitive comparison] — 在 1.7B 上对 "Discovering Process-Outcome Credit" (arXiv 2602.01034) 做 reduced-scale 实证比较（50% training, 1 seed, MC rollouts N=4），配合理论 FLOPs 分析。标注 "reduced-scale comparison" 并解释 full-scale compute-normalized comparison 对 MC estimation 方法不利。避免 "跳过概念上最相似的方法" 的审稿质疑 — 命中 **Technical Soundness**

17. [Experimental Design — 统计 + 公平性] — 原始 proposal 未提及统计显著性或 compute fairness。新增：1.7B 全部 3 seeds (mean ± std)；8B top 2 configs × 3 seeds + evaluation-level bootstrap CIs (1000 resamples)；per-method training wall-clock time + FLOPs 对比；PRM calibration 成本单列一次性开销；accuracy-vs-compute Pareto curves — 命中 **Technical Soundness（统计严谨性和 compute fairness 是 2026 年审稿标准要求）**

18. [Key References] — 从 11 篇扩展至 18 篇，新增 arXiv 2509.21154 (ICLR 2026)、arXiv 2602.01034、arXiv 2601.18984、arXiv 2509.17730、arXiv 2603.06621、DAPO、arXiv 2604.09459 — 命中 **Related Work 完整性**

【主要风险】:
1. **Empirical gains 可能不够大**。UGCA 的 per-step uncertainty gating 与 PROGRS 的 trajectory-level centering、VPPO 的 binary gating 之间的实际 accuracy 差距可能仅 1-2 个百分点，不足以让 reviewer 认定额外复杂度 justified。**缓解策略**：将 reward hacking robustness（PAG curves 斜率更缓、reward hacking rate 更低）作为独立于 accuracy 的差异化价值；UGCA+PROGRS 组合实验若展示正交增益，可证明 per-step gating 有 trajectory-level centering 无法覆盖的价值。
2. **Cross-family PRM calibration 退化**。Qwen2.5-Math-PRM-7B 在 Qwen3 rollouts 上的 calibration 质量可能显著退化，且随 RL training 的 policy drift 持续恶化，导致 gating 信号在训练后期失真。**缓解策略**：week 1 go/no-go gate 可早期发现；re-calibration contingency budget 已预留；longitudinal tracking + phase-segmented reporting 可量化影响；worst case 下 α 趋向 outcome credit（graceful degradation, 不 catastrophic）。

【实施评估】:
- **计算资源**: ~3350 H100-hours 总计。建议平台：8×H100 节点（单个 Qwen3-8B RL run 约 25h wall-clock）。1.7B ablations 可在 4×H100 上运行。若有多节点集群，8B 的多 config 可并行执行，GPU 密集期约 4-5 周。估算成本 ~$8,400（H100 spot ~$2.50/hr）。
- **数据需求**: MATH 训练集 8K prompts（公开）；MATH-500, AMC23, AIME 2024, AIME 2025, OlympiadBench, MinervaMath 评测集（均公开）；PRM quantile calibration validation set（MATH 子集或 PRM-Bench，公开）；cross-family validation 需 Qwen3-8B initial rollouts 的 MC completions（自行生成，N=8-16）。所有数据公开可得，无需额外获取。
- **人工介入**: 最小化。主要工程工作：PROGRS core reproduction（3-5 天，可参考匿名评审代码 anonymous.4open.science/r/PROGRS-914D/）；GRPO-λ 基于公式实现（1-2 天）；"Discovering Process-Outcome Credit" reduced-scale reproduction（2-3 天）。无需人工标注。Paper writing 约 1 周。若使用 Claude 辅助（human-in-loop 模式），codebase integration、ablation scripting、results analysis 和 drafting 可压缩 ~2 周，总 timeline 可缩至 6 周。Claude API 成本约 $400。
- **训练需求**: RL fine-tuning（GRPO-based）训练 Qwen3-8B 和 Qwen3-1.7B，非从头预训练。PRM quantile regression heads calibration fine-tuning（frozen backbone，约 100h）。若 cross-family validation 触发 re-calibration，额外 ~70h。无需预训练或大规模 SFT。
- **新 Benchmark**: 不需要。所有评测集为已有公开 benchmark。Reward hacking 量化指标为计算指标（PAG, reward hacking rate），不需要新数据标注。Core assumption validation 使用已有 rollouts 计算，不构成新 benchmark。
- **预估周期**: 8 周（从启动到可投稿 AAAI 2027，deadline July 28, 2026）。关键路径：wk1 PRM calibration + cross-family validation (go/no-go gate) → wk2 PURE/veRL integration + baseline reproduction → wk3-4 1.7B 全 ablation sweep (14 configs × 3 seeds) → wk5-6 8B comparison runs (6 configs + UGCA+PROGRS combination) + longitudinal tracking → wk7 reward-hacking analysis, PAG curves, Pareto curves, per-step visualization → wk8 paper writing + submission。Timeline 紧张但可行，前提是 GPU 资源到位且 cross-family validation 通过 go/no-go gate。若需 re-calibration，wk2 执行后仍可在 8 周内完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b23c6b25-691b-4374-bf10-06f31f82e92e",
  "isSidechain": false,
  "requestId": "req_011CbSnFKUDdB2R2mGrChC4K",
  "type": "assistant",
  "uuid": "9f9ad246-85a2-42ba-820b-892769c37909",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FkWWfVjo6mjUqJxkU2YQj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6766,
      "cache_read_input_tokens": 90513,
      "output_tokens": 5568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6766,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5568,
          "cache_read_input_tokens": 90513,
          "cache_creation_input_tokens": 6766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6766
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

_source line 98_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。",
  "leafUuid": "9f9ad246-85a2-42ba-820b-892769c37909",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---

### Runtime record

_source line 99_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-Gated credit assignment for math reasoning RL",
  "sessionId": "196740b4-7d71-40e0-b9b9-901bbed4cf87"
}
```

---
