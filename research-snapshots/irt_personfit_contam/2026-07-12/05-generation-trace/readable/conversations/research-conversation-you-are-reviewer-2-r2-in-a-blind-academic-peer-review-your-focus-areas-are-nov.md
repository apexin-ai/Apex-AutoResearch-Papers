# Research conversation: You are Reviewer 2 (R2) in a blind academic peer review. Your focus areas are **Novelty/Significance** and **Related Wor

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a0a6b7f6fc67f13d8.jsonl`
- **Structured JSON:** [`102e7e03aca3f5aee80b.json`](../../sessions/10/102e7e03aca3f5aee80b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

43 recorded events

### User

_source line 1 · 2026-05-20T10:04:58.846Z_

You are Reviewer 2 (R2) in a blind academic peer review. Your focus areas are **Novelty/Significance** and **Related Work/Positioning**. 

Review the following paper and produce a structured review. Use the standard top-ML-venue 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Acceptance rate ~25%.

## Paper Summary

**Title:** IRT-FIT: Detecting Benchmark Contamination in Large Language Models via Person-Fit Statistics at the Minimal-Information Operating Point

**Core idea:** Repurpose IRT person-fit statistics (lz*) to detect benchmark contamination in LLMs using only binary correct/incorrect response patterns — the "minimal-information operating point." Uses Δlz* (delta between clean and contaminated) to overcome universal positive misfit in LLMs.

**Three claims:**
1. On benchmarks with ≥10K items, AUROC > 0.9 at 15% contamination, within 3-5pp of gray-box methods
2. Detection power follows a predictable inverted-U with analytically derivable nadir, scaling with benchmark size
3. Leaderboard-wide audit of 1,847 models: ~12% flagged, temporal trend from 6% to 18% (p=0.003)

**Related work covered (Section 2):**
- Contamination detection: Min-K%++ (Shi et al., 2024) — membership inference via token log-probs. Time Travel (Oren et al., 2024) — probing with temporal variants. ConStat (Li et al., 2024) — performance consistency on rephrased items. CoDeC (Wu et al., 2026) — in-context learning dynamics. Wang et al. (2025) — MIA fails post-RL.
- IRT for LLMs: PSN-IRT (Polo et al., 2024) — 4PL calibration from LLM response matrices. Zhuang et al. (2024) — IRT ability more robust than raw accuracy.
- Person-fit statistics: Drasgow et al. (1985) — lz. Snijders (2001) — lz* (standardized).

**Key positioning:** IRT-FIT is "complementary" to existing methods, occupying the minimal-information end of the "detection frontier." It trades accuracy for universal applicability — works on archived data where models may be offline and token probabilities unavailable.

**Method details:**
- 4PL IRT model: P(U=1|θ) = c + (d-c)·logistic(a(θ-b))
- lz* = (l_i - E[l_i]) / √Var(l_i), standardized person-fit
- Pipeline: fit 4PL → estimate θ via MLE → compute lz* → flag via Δlz* or |lz*| threshold
- Analytical power: P(detect) = Φ(−z_α + δ√n/σ), nadir π* ≈ (θ_true − θ_low)/(θ_high − θ_low)

**Experiments:**
- Simulation study (5 benchmarks, 5-100% contamination, 1000 replications)
- Controlled contamination (Qwen3.5-9B + Gemma-4-31B, QLoRA SFT, 6 levels, 5 benchmarks)
- Post-RL robustness (GRPO on contaminated model: IRT-FIT retains 94%, Min-K%++ drops to 64%)
- Baseline comparison (IRT-FIT AUROC=0.94 vs ConStat 0.97 vs Min-K%++ 0.96 at 15%)
- Leaderboard audit (1,847 models, 6 benchmarks, temporal analysis)
- Appendices: 4PL/3PL ablation, extended benchmarks (BBH, MATH), domain analysis, lzm multiscale

**Key figures from experiment design (review_context.yaml):** 10+ imagined experiments were planned. The paper reflects all of them: extended simulation, controlled contamination (pilot merged into full), power theory, leaderboard recon+audit, 4PL/3PL ablation, baseline comparison, multiscale lzm, post-RL test, extra benchmarks, domain analysis.

**References (9 total):** Drasgow et al. 1985, Li et al. 2024, Oren et al. 2024, Polo et al. 2024, Shi et al. 2024, Snijders 2001, Wang et al. 2025, Wu et al. 2026, Zhuang et al. 2024, Hong et al. 2021.

## Your Review Task

Evaluate specifically:

1. **Novelty**: Is the connection between IRT person-fit and LLM contamination detection genuinely new? Is the "minimal-information operating point" framing a real contribution or just marketing? Is the inverted-U characterization novel? Is the analytical power theory a genuine advance?

2. **Significance/Impact**: Does this advance the field meaningfully? Would practitioners actually use IRT-FIT? Is the leaderboard audit result impactful? Does the "detection frontier" framing add value?

3. **Related work completeness**: Are key baselines missing? Are there other IRT-for-LLM works not cited? Are there other contamination detection methods not discussed? Is the comparison fair? Specifically check: Are there any person-fit papers in the educational testing literature that have been applied to cheating detection that should be cited?

4. **Positioning and claims**: Are the claims appropriately scoped? Is "minimal-information operating point" well-defined and justified? Is "detection frontier" an appropriate framing? Are the comparisons to ConStat, Min-K%++ fair?

5. **Writing quality**: Is the paper well-written? Is the narrative coherent? Are the terms well-defined?

6. **Strengths and weaknesses**: List at least 3 of each.

7. **Questions for authors**: List specific questions.

8. **Overall score** on the 6-point scale with justification.

Format: Summary, Strengths, Weaknesses, Questions, Minor Issues, Overall Assessment (score + justification).


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "290d95ad-e4ec-4489-aadc-cb5eadf29bea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T10:04:58.849Z_

```json
{
  "parentUuid": "290d95ad-e4ec-4489-aadc-cb5eadf29bea",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "095fd5c8-4f1f-4d48-9a81-3e7a6edcfe7c",
  "timestamp": "2026-05-20T10:04:58.849Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T10:05:01.626Z_



I need to read the paper and supporting materials to provide a thorough review. Let me start by finding and reading the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "095fd5c8-4f1f-4d48-9a81-3e7a6edcfe7c",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDddBEPRFkN5pdZ47VW5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0937cc71-9746-482d-b790-57405b9ac3be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qz7b3vM4yXRanHk1T8s5ah",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7828,
      "cache_read_input_tokens": 8254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7828,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T10:05:02.838Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01A6VKDu9wDHS25YWAL1tXpm`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0937cc71-9746-482d-b790-57405b9ac3be",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDddBEPRFkN5pdZ47VW5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d7e226b-9a23-4501-ac22-da2a69ee8801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qz7b3vM4yXRanHk1T8s5ah",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7828,
      "cache_read_input_tokens": 8254,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7828
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 133,
          "cache_read_input_tokens": 8254,
          "cache_creation_input_tokens": 7828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7828,
            "ephemeral_1h_input_tokens": 0
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

_source line 5 · 2026-05-20T10:05:02.841Z_

<details><summary>↩ Tool result · `toolu_01A6VKDu9wDHS25YWAL1tXpm`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_get_project_overview"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d7e226b-9a23-4501-ac22-da2a69ee8801",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "4bdabb2a-b430-4001-8e5e-c57af158dfd1",
  "sourceToolAssistantUUID": "7d7e226b-9a23-4501-ac22-da2a69ee8801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T10:05:09.369Z_



Let me read the paper and supporting materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bdabb2a-b430-4001-8e5e-c57af158dfd1",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDddUSymC3xaAR85p38J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18b4b831-c26f-4a67-966d-f21f36bfbdcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jHh9zuN6DQqHUeLLdVFUH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 16082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1455,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T10:05:09.775Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0144meZxf7idypq5BGB7oGhq`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18b4b831-c26f-4a67-966d-f21f36bfbdcc",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDddUSymC3xaAR85p38J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f8f111e-4e90-41ed-8c4f-d9ece6fed71f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jHh9zuN6DQqHUeLLdVFUH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 16082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1455,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T10:05:09.806Z_

<details><summary>↩ Tool result · `toolu_0144meZxf7idypq5BGB7oGhq`</summary>

```text
artifacts/dream_reports/dream_20260520T082549/best/paper.tex
artifacts/dream_reports/dream_20260520T082549/median/paper.tex
artifacts/dream_reports/dream_20260520T082549/worst/paper.tex
artifacts/dream_reports/dream_20260520T092614/best/paper.tex
artifacts/dream_reports/dream_20260520T092614/median/paper.tex
artifacts/dream_reports/dream_20260520T092614/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f8f111e-4e90-41ed-8c4f-d9ece6fed71f",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "e2f82878-9d05-4a57-9117-7a3bf1b46877",
  "sourceToolAssistantUUID": "8f8f111e-4e90-41ed-8c4f-d9ece6fed71f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T10:05:09.963Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01GgiT7pyV3nu519DknUiuzp`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2f82878-9d05-4a57-9117-7a3bf1b46877",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDddUSymC3xaAR85p38J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a908ab0-e849-46cf-bfac-050147dbd29c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jHh9zuN6DQqHUeLLdVFUH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 16082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1455,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T10:05:09.995Z_

<details><summary>↩ Tool result · `toolu_01GgiT7pyV3nu519DknUiuzp`</summary>

```text
artifacts/psn_irt_data_report.md
.venv/lib/python3.14/site-packages/pyparsing/ai/best_practices.md
.venv/lib/python3.14/site-packages/numpy/random/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/distributions/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/philox/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md
.venv/lib/python3.14/site-packages/scipy/fft/_pocketfft/LICENSE.md
docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260520T082549/best/paper_framing.md
artifacts/dream_reports/dream_20260520T082549/median/paper_framing.md
artifacts/dream_reports/dream_20260520T082549/worst/paper_framing.md
artifacts/_project/report/analysis_report.md
artifacts/phase_b_two_sided_v2/analysis_report.md
artifacts/dream_reports/dream_20260520T082549/best/review_report.md
paper_framing.md
artifacts/dream_reports/dream_20260520T082549/median/review_report.md
.claude/sessions/review_reviewer_1_ac4dc473/CLAUDE.md
.claude/sessions/review_reviewer_1_ac4dc473/AGENTS.md
.claude/sessions/review_reviewer_2_956ba1bc/CLAUDE.md
.claude/sessions/review_reviewer_2_956ba1bc/AGENTS.md
.claude/sessions/review_director_34e01ffa/CLAUDE.md
.claude/sessions/review_director_34e01ffa/AGENTS.md
ROADMAP.md
memory.md
artifacts/review_reports/round_0.md
artifacts/dream_reports/dream_20260520T092614/best/paper_framing.md
artifacts/dream_reports/dream_20260520T092614/median/paper_framing.md
.claude/sessions/agent_51ea7db2/CLAUDE.md
.claude/sessions/agent_51ea7db2/AGENTS.md
artifacts/dream_reports/dream_20260520T092614/worst/paper_framing.md
artifacts/exp-leaderboard-data-recon/report/report.md
artifacts/leaderboard_data_recon/report.md
artifacts/exp-empirical-null/report/unflagged_analysis.md
artifacts/empirical_null_analysis/unflagged_analysis.md
report.md
.claude/sessions/reviewer_1ed95eb4/CLAUDE.md
.claude/sessions/reviewer_1ed95eb4/AGENTS.md
.claude/CLAUDE.md
AGENTS.md
.claude/sessions/director_15982409/CLAUDE.md
.claude/sessions/director_15982409/AGENTS.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a908ab0-e849-46cf-bfac-050147dbd29c",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "0db988c1-333d-4b4c-b1e9-36d935aa4ca4",
  "sourceToolAssistantUUID": "3a908ab0-e849-46cf-bfac-050147dbd29c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T10:05:10.120Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016vDQHzhVnYLNMmvzLJeuTA`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0db988c1-333d-4b4c-b1e9-36d935aa4ca4",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDddUSymC3xaAR85p38J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e79f881f-20df-4b31-86c9-ed8ce334562b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jHh9zuN6DQqHUeLLdVFUH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 16082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1455,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T10:05:10.163Z_

<details><summary>↩ Tool result · `toolu_016vDQHzhVnYLNMmvzLJeuTA`</summary>

```text
literature_map.yaml
mistakes.yaml
artifacts/dream_reports/dream_20260520T082549/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T082549/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T082549/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T082549/best/review_context.yaml
artifacts/dream_reports/dream_20260520T082549/median/review_context.yaml
decisions.yaml
artifacts/dream_reports/dream_20260520T082549/worst/review_context.yaml
artifacts/review_issues.yaml
artifacts/dream_reports/dream_20260520T092614/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T092614/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T092614/worst/imagined_experiments.yaml
experiment_plan.yaml
registry.yaml
artifacts/manifest.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260520T092614/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e79f881f-20df-4b31-86c9-ed8ce334562b",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "7709cd25-e42a-497d-84bb-ea5122767f95",
  "sourceToolAssistantUUID": "e79f881f-20df-4b31-86c9-ed8ce334562b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T10:05:14.171Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FXrtqxpqdSAnheJ7JP6Rxv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7709cd25-e42a-497d-84bb-ea5122767f95",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDde1xZBvMtS7Ur7s8PK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40540644-6fca-4eb7-a859-6eb0d66edc40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WG1hDWXno94sSUUxeDkLyY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1829,
      "cache_read_input_tokens": 17537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1829,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T10:05:14.178Z_

<details><summary>↩ Tool result · `toolu_01FXrtqxpqdSAnheJ7JP6Rxv`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{natbib}
12	\usepackage{tabularx}
13	\usepackage{array}
14	
15	\title{IRT-FIT: Detecting Benchmark Contamination in Large Language Models\\via Person-Fit Statistics at the Minimal-Information Operating Point}
16	
17	\author{Anonymous}
18	\date{}
19	
20	\begin{document}
21	\maketitle
22	
23	% ============================================================
24	% ABSTRACT
25	% ============================================================
26	\begin{abstract}
27	Benchmark contamination threatens the reliability of Large Language Model (LLM) evaluation, yet all existing detection methods require privileged access beyond binary response patterns---token probabilities, rephrased test items, or training data.
28	We introduce \textbf{IRT-FIT}, a framework that repurposes Item Response Theory (IRT) person-fit statistics to detect contamination at the \emph{minimal-information operating point}, requiring only binary (correct/incorrect) response logs.
29	Through simulation, controlled contamination experiments on two models (Qwen3.5-9B and Gemma-4-31B), and analytical derivation, we establish three results:
30	(1)~on benchmarks with $\geq$10K items, IRT-FIT achieves AUROC~$>$~0.9 at 15\% contamination using only binary responses, narrowing the gap to gray-box methods (ConStat, Min-K\%++) to $<$5 percentage points;
31	(2)~detection power follows a predictable inverted-U curve across contamination levels with a theoretically derivable nadir, and scales as a closed-form function of benchmark size;
32	(3)~a leaderboard-wide audit of 1{,}847 Open LLM Leaderboard models reveals that ${\sim}$12\% exhibit contamination-consistent misfit, with flagging rates rising from 6\% in 2023\,H2 to 18\% in 2024\,H1 ($p{=}0.003$).
33	IRT-FIT is the only method capable of retrospective auditing on archived evaluation data, enabling ecosystem-scale contamination surveillance that is infeasible with existing approaches.
34	\end{abstract}
35	
36	% ============================================================
37	% 1  INTRODUCTION
38	% ============================================================
39	\section{Introduction}
40	
41	As LLM benchmarks proliferate and training corpora expand, the risk that models are trained on evaluation data---benchmark contamination---grows accordingly.
42	Contaminated scores inflate perceived capability, mislead downstream adoption decisions, and erode trust in community leaderboards.
43	The problem is compounded by the opacity of training pipelines: most frontier models disclose neither data composition nor contamination auditing procedures.
44	
45	Existing detection methods span five families: time-based partition analysis, membership inference attacks (Min-K\%++; \citealt{shi2024detecting}), probing-based detection (Time Travel; \citealt{oren2024proving}), performance-consistency testing (ConStat; \citealt{li2024constat}), and in-context learning effects (CoDeC; \citealt{wu2026codec}).
46	All require \emph{more} than binary response patterns: token-level probabilities, rephrased test items, model weights, or specially crafted prompts.
47	Moreover, \citet{wang2025mia} demonstrate that MIA-based methods fail under post-reinforcement-learning (RL) contamination, highlighting fragility tied to token-level signals.
48	Critically, \textbf{no existing method operates at the minimal-information level}---binary correct/incorrect outcomes---which is the only signal universally available in archived evaluation logs.
49	
50	A contaminated LLM is functionally analogous to an examinee with item preknowledge, a scenario studied for decades in psychometrics under the rubric of \emph{person-fit} analysis.
51	IRT person-fit statistics such as $l_z^*$ \citep{snijders2001} quantify whether an individual's response pattern is consistent with the estimated ability level: aberrant patterns (e.g., answering difficult items correctly while missing easy ones) yield extreme $l_z^*$ values.
52	Despite this conceptual alignment, no prior work has connected IRT person-fit to LLM contamination detection.
53	
54	We introduce \textbf{IRT-FIT}, a framework that establishes the \emph{minimal-information operating point} on the contamination detection frontier.
55	Our approach fits a 4-parameter logistic (4PL) IRT model to binary response matrices across many LLMs, computes standardized person-fit statistics ($l_z^*$), and detects contamination through the misfit delta ($\Delta l_z^*$) between clean and contaminated conditions.
56	
57	\paragraph{Contributions.}
58	\begin{enumerate}
59	\item We demonstrate that IRT person-fit statistics provide effective contamination detection using only binary responses, achieving AUROC~$>$~0.9 at 15\% contamination on large benchmarks ($\geq$10K items), within 3--5 percentage points of methods requiring richer information.
60	\item We characterize detection power as a closed-form function of benchmark size and contamination level, derive the inverted-U power curve analytically, and provide minimum benchmark-size thresholds for target power levels.
61	\item We conduct the first leaderboard-scale contamination audit (1{,}847 models, 6 benchmarks), revealing ecosystem-level contamination trends and identifying model families with systematically elevated misfit.
62	\end{enumerate}
63	
64	% ============================================================
65	% 2  RELATED WORK
66	% ============================================================
67	\section{Related Work}
68	
69	\paragraph{Contamination detection.}
70	\citet{shi2024detecting} introduce Min-K\%++, a membership inference approach using token-level log-probabilities.
71	\citet{oren2024proving} propose Time Travel, probing models with temporally shifted variants of test items.
72	\citet{li2024constat} develop ConStat, comparing performance on original vs.\ rephrased items.
73	\citet{wu2026codec} leverage in-context learning dynamics via CoDeC.
74	All require access beyond binary responses.
75	\citet{wang2025mia} show that post-RL training erases the token-probability signals that MIA methods rely on.
76	Our work is complementary: IRT-FIT occupies the minimal-information end of the detection frontier, trading modest accuracy for universal applicability.
77	
78	\paragraph{IRT for LLMs.}
79	PSN-IRT \citep{polo2024psnirt} calibrates 4PL item parameters from LLM response matrices and demonstrates that IRT-based scoring improves benchmark reliability.
80	\citet{zhuang2024irtllm} show that IRT-derived ability estimates are more robust to item sampling than raw accuracy.
81	Neither addresses contamination.
82	Our work builds on PSN-IRT's item calibration infrastructure and extends it to person-fit analysis.
83	
84	\paragraph{Person-fit statistics.}
85	The $l_z$ statistic \citep{drasgow1985} and its standardized variant $l_z^*$ \citep{snijders2001} are the workhorse tools for detecting aberrant response patterns in educational testing.
86	Applications include detecting cheating, item preknowledge, and random responding.
87	We adapt this framework to LLM evaluation, addressing the unique challenge of universal model misfit.
88	
89	% ============================================================
90	% 3  BACKGROUND
91	% ============================================================
92	\section{IRT and Person-Fit Background}
93	
94	\paragraph{4PL IRT model.}
95	Given a response matrix $\mathbf{U} \in \{0,1\}^{N \times J}$ with $N$ respondents (LLMs) and $J$ items, the 4PL model specifies:
96	\begin{equation}
97	P(U_{ij}=1 \mid \theta_i) = c_j + (d_j - c_j) \cdot \frac{1}{1 + e^{-a_j(\theta_i - b_j)}}
98	\end{equation}
99	where $\theta_i$ is the ability of respondent $i$; $a_j$, $b_j$, $c_j$, $d_j$ are the discrimination, difficulty, guessing, and upper-asymptote parameters of item $j$.
100	
101	\paragraph{Person-fit statistic $l_z^*$.}
102	The log-likelihood of respondent $i$'s pattern is $l_i = \sum_j [u_{ij} \log P_{ij} + (1{-}u_{ij})\log(1{-}P_{ij})]$, where $P_{ij} = P(U_{ij}{=}1\mid\theta_i)$.
103	The standardized person-fit statistic is:
104	\begin{equation}
105	l_z^* = \frac{l_i - E[l_i]}{\sqrt{\text{Var}(l_i)}}
106	\end{equation}
107	Under a well-fitting model, $l_z^* \sim \mathcal{N}(0,1)$.
108	Negative values ($l_z^* \ll 0$) indicate aberrant patterns (unexpected correct responses on hard items); positive values ($l_z^* \gg 0$) indicate over-consistent patterns.
109	
110	\paragraph{Contamination signatures.}
111	Benchmark contamination introduces item preknowledge: the model answers contaminated items correctly regardless of their difficulty, creating a mismatch between observed and expected response patterns.
112	At \emph{low-to-moderate} contamination ($\lesssim$50\%), the aberrant correct responses produce $l_z^* \ll 0$.
113	At \emph{high} contamination ($\gtrsim$75\%), nearly all items are answered correctly, pushing the MLE ability estimate $\hat{\theta}$ upward; the resulting pattern appears over-consistent ($l_z^* \gg 0$).
114	This creates an \emph{inverted-U} in detection power when using one-sided tests, which we resolve with two-sided testing.
115	
116	% ============================================================
117	% 4  IRT-FIT FRAMEWORK
118	% ============================================================
119	\section{IRT-FIT Framework}
120	
121	\subsection{Pipeline}
122	
123	Given binary response logs from multiple LLMs on a benchmark:
124	\textbf{(1)}~Fit a 4PL IRT model to the response matrix using PSN-IRT calibration, obtaining item parameters $(a_j, b_j, c_j, d_j)$ for each item.
125	\textbf{(2)}~Estimate each model's ability $\hat{\theta}_i$ via maximum likelihood.
126	\textbf{(3)}~Compute $l_z^*$ for each model.
127	\textbf{(4)}~Flag models with $|l_z^*|$ exceeding a calibrated threshold, or compare $\Delta l_z^* = l_{z,\text{test}}^* - l_{z,\text{clean}}^*$ against the clean baseline distribution.
128	
129	\subsection{Calibration Gap and $\Delta l_z^*$}
130	
131	Real LLM responses violate IRT's local independence assumption: knowledge is clustered by domain, items within a topic are correlated, and response strategies vary across question types.
132	This produces universal positive misfit ($l_z^* \gg 0$) even in clean models---e.g., clean Qwen3.5-9B has $l_z^* = +18.3$ on MMLU.
133	Absolute thresholds therefore flag nearly all models indiscriminately.
134	
135	We resolve this via \emph{relative detection}: the contamination-induced misfit delta $\Delta l_z^*$ between clean and contaminated conditions.
136	This approach requires either (a)~a controlled experiment establishing clean baselines, or (b)~a large population of models providing an empirical baseline distribution (as in our leaderboard audit).
137	
138	\subsection{Analytical Power Theory}
139	\label{sec:power-theory}
140	
141	Building on the variance formula from \citet{snijders2001}, we derive the detection power as a function of benchmark size $n$ and contamination fraction $\pi$:
142	\begin{equation}
143	P(\text{detect}) = \Phi\!\left(-z_\alpha + \frac{\delta \sqrt{n}}{\sigma_{l_z^*}}\right)
144	\end{equation}
145	where $\delta = E[l_{z,\text{contam}}^* - l_{z,\text{clean}}^*]/n$ is the per-item effect size and $\sigma_{l_z^*}$ is derived from the Snijders variance formula.
146	
147	The inverted-U emerges analytically: as $\pi$ increases, the MLE $\hat{\theta}$ rises, and the expected log-likelihood crosses zero at a nadir contamination fraction:
148	\begin{equation}
149	\pi^* \approx \frac{\theta_{\text{true}} - \theta_{\text{low}}}{\theta_{\text{high}} - \theta_{\text{low}}}
150	\end{equation}
151	At $\pi^*$, $|E[l_z^*]|$ is minimized, producing minimal detection power.
152	Two-sided testing ($|l_z^*| > z_{\alpha/2}$) mitigates this by capturing both negative (aberrant) and positive (over-consistent) signals.
153	
154	% ============================================================
155	% 5  EXPERIMENTS
156	% ============================================================
157	\section{Experiments}
158	
159	\subsection{Simulation Study}
160	\label{sec:simulation}
161	
162	We simulate binary response matrices under the 4PL model across five benchmarks (MMLU, HellaSwag, GSM8K, ARC-C, HumanEval), injecting contamination at levels from 5\% to 100\%.
163	Contaminated items are set to $P(\text{correct})=1$ regardless of ability.
164	For each condition, 1{,}000 replications are run.
165	
166	\paragraph{Results.}
167	Table~\ref{tab:sim-power} reports two-sided detection power ($|l_z^*| > 1.96$, $\alpha=0.05$).
168	On MMLU (14{,}042 items), power reaches 0.979 at 15\% contamination and remains above 0.85 at all levels except the inverted-U nadir.
169	The nadir occurs at $\sim$72\% contamination for MMLU (power\,=\,0.50) and $\sim$68\% for HellaSwag (power\,=\,0.38), consistent with the analytical prediction.
170	
171	Detection power scales with benchmark size: MMLU (14K) achieves 0.979 at 15\%, HellaSwag (10K) achieves 0.733, GSM8K (1.3K) achieves 0.578, and ARC-C (1.2K) only 0.129.
172	HumanEval (164 items) yields power\,$\leq$\,0.31 across all conditions, establishing a clear lower bound on benchmark size for feasible detection.
173	
174	\begin{table}[t]
175	\centering
176	\small
177	\caption{Two-sided detection power across contamination levels (simulation, $\alpha{=}0.05$).}
178	\label{tab:sim-power}
179	\begin{tabular}{lrcccccccc}
180	\toprule
181	\textbf{Benchmark} & $n$ & \textbf{5\%} & \textbf{15\%} & \textbf{25\%} & \textbf{50\%} & \textbf{60\%} & \textbf{75\%} & \textbf{90\%} & \textbf{100\%} \\
182	\midrule
183	MMLU & 14042 & .42 & .979 & .998 & .89 & .54 & .50 & .85 & .97 \\
184	HellaSwag & 10042 & .28 & .733 & .94 & .62 & .35 & .38 & .71 & .89 \\
185	GSM8K & 1319 & .10 & .578 & .72 & .41 & .22 & .18 & .52 & .68 \\
186	ARC-C & 1172 & .04 & .129 & .28 & .09 & .05 & .04 & .11 & .22 \\
187	HumanEval & 164 & .02 & .243 & .31 & .08 & .04 & .03 & .06 & .09 \\
188	\bottomrule
189	\end{tabular}
190	\end{table}
191	
192	\paragraph{Inverted-U mechanism.}
193	At low contamination, correct responses on hard items conflict with estimated ability, producing $l_z^* \ll 0$ (aberrant misfit).
194	As contamination increases past $\sim$60\%, the MLE $\hat{\theta}$ is driven upward by near-universal correct responding, and $l_z^*$ crosses zero into the positive regime.
195	In the transition zone ($\sim$60--75\%), $|l_z^*|$ is minimized, creating a detection power dip.
196	At extreme contamination ($\geq$90\%), over-consistency ($l_z^* \gg 0$) provides strong signal again.
197	Table~\ref{tab:lz-decomposition} (Appendix~\ref{app:decomposition}) decomposes negative vs.\ positive $l_z^*$ contributions on MMLU, confirming the dual-regime structure.
198	
199	\paragraph{Theory--simulation agreement.}
200	Table~\ref{tab:theory-vs-empirical} compares analytical power predictions with simulation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40540644-6fca-4eb7-a859-6eb0d66edc40",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "928305e6-5745-4aca-b50e-28b1ee552599",
  "sourceToolAssistantUUID": "40540644-6fca-4eb7-a859-6eb0d66edc40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T10:05:14.657Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PEnqZyBaxURQ3F4DMajVaT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "928305e6-5745-4aca-b50e-28b1ee552599",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDde1xZBvMtS7Ur7s8PK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a48cbe86-cac8-4144-8b14-f9ca827ab1c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WG1hDWXno94sSUUxeDkLyY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1829,
      "cache_read_input_tokens": 17537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1829,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T10:05:14.953Z_

<details><summary>↩ Tool result · `toolu_01PEnqZyBaxURQ3F4DMajVaT`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。Claim 1: minimal-information detection 经控制实验验证，Δlz*
2	  提供 可靠的相对检测信号，calibration gap 被 bridged。Claim 2: inverted-U 从经验升级为理论命题， dose-response
3	  曲线在两个模型上复现。Claim 3: leaderboard 大规模审计揭示生态系统级污染趋势， Gemini-1.5 case study 由控制实验的 Δlz*
4	  基线提供定量支撑。 Headline: "IRT-FIT achieves AUROC>0.9 at 15% contamination using only
5	  binary responses, and a leaderboard-wide audit reveals ~12% of models exhibit contamination-consistent
6	  misfit."
7	
8	  '
9	imagined_experiments:
10	- name: Extended Simulation — Inverted-U Full Characterization
11	  plan_id: exp-extended-sim
12	  description: '在 Phase A 模拟基础上添加 60%/75%/90%/100% contamination levels， 修复 100% contamination
13	    时 MLE boundary θ=4.0 的 lz* 计算， 精确刻画 inverted-U 拐点位置，计算 two-sided power curves。
14	
15	    '
16	  expected_results:
17	    power_negative_at_5pct_mmlu: 0.42
18	    power_negative_at_15pct_mmlu: 0.979
19	    power_negative_at_25pct_mmlu: 0.998
20	    power_negative_at_50pct_mmlu: 0.87
21	    power_negative_at_60pct_mmlu: 0.54
22	    power_negative_at_75pct_mmlu: 0.12
23	    power_negative_at_90pct_mmlu: 0.03
24	    power_negative_at_100pct_mmlu: 0.01
25	    power_positive_at_5pct_mmlu: 0.0
26	    power_positive_at_15pct_mmlu: 0.0
27	    power_positive_at_50pct_mmlu: 0.02
28	    power_positive_at_60pct_mmlu: 0.08
29	    power_positive_at_75pct_mmlu: 0.38
30	    power_positive_at_90pct_mmlu: 0.82
31	    power_positive_at_100pct_mmlu: 0.96
32	    power_twosided_at_15pct_mmlu: 0.979
33	    power_twosided_at_50pct_mmlu: 0.89
34	    power_twosided_at_75pct_mmlu: 0.5
35	    power_twosided_at_90pct_mmlu: 0.85
36	    power_twosided_at_100pct_mmlu: 0.97
37	    inverted_u_nadir_contamination_pct_mmlu: 72
38	    inverted_u_nadir_power_mmlu: 0.45
39	    inverted_u_nadir_contamination_pct_hellaswag: 68
40	    inverted_u_nadir_power_hellaswag: 0.38
41	    power_twosided_at_15pct_hellaswag: 0.733
42	    power_twosided_at_50pct_hellaswag: 0.62
43	    power_twosided_at_90pct_hellaswag: 0.71
44	    power_twosided_at_15pct_gsm8k: 0.578
45	    power_twosided_at_50pct_gsm8k: 0.41
46	    power_twosided_at_90pct_gsm8k: 0.52
47	    power_twosided_at_15pct_arc_c: 0.129
48	    power_twosided_at_50pct_arc_c: 0.09
49	    power_twosided_at_90pct_arc_c: 0.11
50	    pct_100_nan_rate_after_fix: 0.0
51	    pct_100_mean_lz_star_mmlu: 28.4
52	    pct_100_mean_theta_mmlu: 4.0
53	  result_rationale: '在 best 档下，inverted-U 拐点清晰可见且位于 ~70% contamination 附近。 机制：低污染(5-50%)时，被污染
54	    item 上的正确作答与模型能力不匹配→aberrant pattern→lz*<<0， 检测力随污染量单调上升。但超过~60%后，模型在绝大部分 item
55	    上都答对，MLE θ 被推高， lz* 从负值穿越零点转向正值——此时处于"过渡区"，|lz*| 最小，power 最低。 继续到 90-100%，over-consistency
56	    信号 (lz*>>0) 变强，双侧检测再次有效。 MMLU (14K items) 由于 n_items 最大，在所有 contamination levels
57	    上 power 最高， nadir 点也最浅。小 benchmark (ARC-C 1.2K) 全程 power 低，nadir 更深， 符合 power∝n_items
58	    的理论预测。 100% contamination 修复后 θ=4.0 (boundary)，lz*=+28.4 反映极端 over-consistency。
59	
60	    '
61	  tables:
62	  - title: 'Table 2: Two-Sided Detection Power Across Contamination Levels (Simulation)'
63	    columns:
64	    - Benchmark
65	    - n_items
66	    - 5%
67	    - 15%
68	    - 25%
69	    - 50%
70	    - 60%
71	    - 75%
72	    - 90%
73	    - 100%
74	    rows:
75	    - - MMLU
76	      - 14042
77	      - 0.42
78	      - 0.979
79	      - 0.998
80	      - 0.89
81	      - 0.54
82	      - 0.5
83	      - 0.85
84	      - 0.97
85	    - - HellaSwag
86	      - 10042
87	      - 0.28
88	      - 0.733
89	      - 0.94
90	      - 0.62
91	      - 0.35
92	      - 0.38
93	      - 0.71
94	      - 0.89
95	    - - GSM8K
96	      - 1319
97	      - 0.1
98	      - 0.578
99	      - 0.72
100	      - 0.41
101	      - 0.22
102	      - 0.18
103	      - 0.52
104	      - 0.68
105	    - - ARC-C
106	      - 1172
107	      - 0.04
108	      - 0.129
109	      - 0.28
110	      - 0.09
111	      - 0.05
112	      - 0.04
113	      - 0.11
114	      - 0.22
115	    - - HumanEval
116	      - 164
117	      - 0.02
118	      - 0.243
119	      - 0.31
120	      - 0.08
121	      - 0.04
122	      - 0.03
123	      - 0.06
124	      - 0.09
125	  - title: 'Table S1: Negative vs Positive lz* Power Decomposition (MMLU)'
126	    columns:
127	    - Contamination
128	    - P(lz*<-1.96)
129	    - P(lz*>1.96)
130	    - P(|lz*|>1.96)
131	    - Mean lz*
132	    - SD lz*
133	    rows:
134	    - - 5%
135	      - 0.42
136	      - 0.0
137	      - 0.42
138	      - -3.1
139	      - 2.8
140	    - - 15%
141	      - 0.979
142	      - 0.0
143	      - 0.979
144	      - -12.7
145	      - 4.2
146	    - - 50%
147	      - 0.87
148	      - 0.02
149	      - 0.89
150	      - -8.4
151	      - 6.1
152	    - - 75%
153	      - 0.12
154	      - 0.38
155	      - 0.5
156	      - 2.8
157	      - 9.3
158	    - - 90%
159	      - 0.03
160	      - 0.82
161	      - 0.85
162	      - 18.6
163	      - 7.5
164	    - - 100%
165	      - 0.01
166	      - 0.96
167	      - 0.97
168	      - 28.4
169	      - 5.2
170	  figures_description:
171	  - 'Figure 2: Inverted-U power curve — x-axis contamination %, y-axis two-sided power,
172	    5 benchmarks 分色，vertical dashed line at nadir (~72% for MMLU). 清晰展示 negative→positive
173	    regime transition.'
174	  - 'Figure S1: lz* distribution heatmap — x-axis contamination level, y-axis lz*
175	    value, color=density. 显示 lz* 分布从负到正的 shift。'
176	  analysis: '关键发现：(1) 双侧框架消除了 inverted-U 的 blind spot——nadir 从 power≈0 提升到 ~0.5， 但在
177	    60-75% contamination 区间仍有检测力下降。(2) 对 MMLU 这种大 benchmark， 除 nadir 外全程 power>0.85，实用性强。(3)
178	    小 benchmark 即使双侧也不够：ARC-C 峰值 仅 0.28，这支持"power 是 n_items 的函数"这一 claim。 叙事价值：inverted-U
179	    是可预测的物理现象而非 limitation，dual-regime 结构是新贡献。
180	
181	    '
182	- name: Controlled Contamination Pilot — Go/No-Go
183	  plan_id: exp-ctrl-contam-pilot
184	  description: 'Qwen3.5-9B × 3 levels (0%/15%/50%) × MMLU。QLoRA SFT 注入已知 benchmark
185	    items， 测量 Δlz*(clean→contaminated) 作为论文 go/no-go 信号。
186	
187	    '
188	  expected_results:
189	    qwen_clean_mmlu_accuracy: 0.71
190	    qwen_clean_mmlu_theta: 1.24
191	    qwen_clean_mmlu_lz_star: 18.3
192	    qwen_15pct_mmlu_accuracy: 0.78
193	    qwen_15pct_mmlu_theta: 1.62
194	    qwen_15pct_mmlu_lz_star: -8.7
195	    qwen_15pct_delta_lz_star: -27.0
196	    qwen_15pct_delta_lz_star_se: 3.2
197	    qwen_15pct_delta_lz_star_z: -8.44
198	    qwen_15pct_delta_lz_star_p: <1e-16
199	    qwen_50pct_mmlu_accuracy: 0.91
200	    qwen_50pct_mmlu_theta: 2.85
201	    qwen_50pct_mmlu_lz_star: -42.1
202	    qwen_50pct_delta_lz_star: -60.4
203	    qwen_50pct_delta_lz_star_se: 4.1
204	    qwen_50pct_delta_lz_star_z: -14.73
205	    qwen_50pct_delta_lz_star_p: <1e-48
206	    go_nogo_signal: GO
207	    cohen_d_15pct: 2.8
208	    cohen_d_50pct: 6.1
209	    accuracy_uplift_15pct: 0.07
210	    accuracy_uplift_50pct: 0.2
211	    sft_epochs: 3
212	    sft_lr: 2e-4
213	    lora_rank: 16
214	    lora_alpha: 32
215	    training_samples_15pct: 2106
216	    training_samples_50pct: 7021
217	    training_time_per_run_hrs: 2.8
218	  result_rationale: '在 best 档下，Δlz* 效应极其显著。原因：(1) MMLU 有 14K items，信噪比极高—— 即使 SFT
219	    generalization 让部分非污染 item 也受益，15% 直接污染的 2100+ items 已足以产生强 aberrant pattern。(2)
220	    Qwen3.5-9B 是中等能力模型（clean acc~0.71）， 污染后能力-表现不匹配最明显——在它本不该答对的难题上答对了。 (3) Clean
221	    baseline lz*=+18.3 (已知的 universal misfit) 在污染后急剧下降到 -8.7， 说明 SFT 注入不仅改变了 accuracy，还改变了
222	    response pattern 的结构—— 打破了原有的 over-consistency (正 lz*) 转为 aberrant (负 lz*)。 (4)
223	    50% 时效应更强 (d=6.1)，但 lz* 仍为负（未越过 inverted-U nadir）， 因为 50% 在 MMLU 14K items 上仍只是
224	    7K items， 模型在剩余 7K 上的表现仍产生 mismatch。 这个 pilot 给出明确 GO 信号。
225	
226	    '
227	  tables:
228	  - title: 'Table 3: Controlled Contamination Pilot Results (Qwen3.5-9B × MMLU)'
229	    columns:
230	    - Contamination
231	    - Accuracy
232	    - θ
233	    - lz*
234	    - Δlz*
235	    - Cohen's d
236	    - p-value
237	    rows:
238	    - - 0% (clean)
239	      - 0.71
240	      - 1.24
241	      - 18.3
242	      - —
243	      - —
244	      - —
245	    - - 15%
246	      - 0.78
247	      - 1.62
248	      - -8.7
249	      - -27.0
250	      - 2.8
251	      - <1e-16
252	    - - 50%
253	      - 0.91
254	      - 2.85
255	      - -42.1
256	      - -60.4
257	      - 6.1
258	      - <1e-48
259	  figures_description:
260	  - 'Figure 3a: Bar chart — lz* at 0%/15%/50% with bootstrap 95% CI. 清晰展示从 +18 到 -8
261	    到 -42 的单调下降。'
262	  - 'Figure 3b: MMLU item-level accuracy heatmap — rows=items sorted by difficulty,
263	    columns=0%/15%/50%. 显示污染 items 上 accuracy spike。'
264	  analysis: 'Pilot 结果明确支持 GO。Cohen''s d=2.8 at 15% 远超预设阈值 2.0。 关键洞察：clean model 已有正
265	    lz*(universal misfit)，污染后 lz* 逆转为负值， 说明 Δlz* 的信号不是从零出发而是从正值出发—— 这反而增大了效应量，因为正负逆转
266	    = 更大的 delta。 Calibration gap 被 bridge：不需要绝对 lz* 阈值，只需 Δlz* 即可区分 clean vs contaminated。
267	
268	    '
269	- name: Full Controlled Contamination Experiment
270	  plan_id: exp-ctrl-contam
271	  description: '完整控制实验：Qwen3.5-9B + Gemma-4-31B × 6 contamination levels (0%/5%/10%/15%/25%/50%)
272	    × 5 benchmarks。建立 ground-truth contamination → Δlz* 映射。
273	
274	    '
275	  expected_results:
276	    qwen_mmlu_lz_star_0pct: 18.3
277	    qwen_mmlu_lz_star_5pct: 8.1
278	    qwen_mmlu_lz_star_10pct: -2.4
279	    qwen_mmlu_lz_star_15pct: -8.7
280	    qwen_mmlu_lz_star_25pct: -22.5
281	    qwen_mmlu_lz_star_50pct: -42.1
282	    qwen_mmlu_delta_lz_star_15pct: -27.0
283	    qwen_mmlu_cohen_d_15pct: 2.8
284	    qwen_mmlu_auroc_15pct: 0.94
285	    qwen_mmlu_auroc_5pct: 0.78
286	    gemma_mmlu_lz_star_0pct: 22.6
287	    gemma_mmlu_lz_star_5pct: 11.4
288	    gemma_mmlu_lz_star_10pct: 1.8
289	    gemma_mmlu_lz_star_15pct: -5.2
290	    gemma_mmlu_lz_star_25pct: -18.7
291	    gemma_mmlu_lz_star_50pct: -35.8
292	    gemma_mmlu_delta_lz_star_15pct: -27.8
293	    gemma_mmlu_cohen_d_15pct: 2.5
294	    gemma_mmlu_auroc_15pct: 0.92
295	    gemma_mmlu_auroc_5pct: 0.76
296	    cross_model_spearman_delta_lz_mmlu: 0.94
297	    cross_model_spearman_delta_lz_hellaswag: 0.89
298	    qwen_hellaswag_lz_star_0pct: 14.7
299	    qwen_hellaswag_lz_star_15pct: -4.2
300	    qwen_hellaswag_delta_lz_star_15pct: -18.9
301	    qwen_hellaswag_cohen_d_15pct: 2.2
302	    qwen_hellaswag_auroc_15pct: 0.91
303	    qwen_gsm8k_lz_star_0pct: 6.8
304	    qwen_gsm8k_lz_star_15pct: 0.3
305	    qwen_gsm8k_delta_lz_star_15pct: -6.5
306	    qwen_gsm8k_cohen_d_15pct: 1.4
307	    qwen_gsm8k_auroc_15pct: 0.82
308	    dose_response_monotonic_qwen_mmlu: true
309	    dose_response_monotonic_gemma_mmlu: true
310	    dose_response_monotonic_qwen_hellaswag: true
311	    dose_response_r2_qwen_mmlu: 0.97
312	    dose_response_r2_gemma_mmlu: 0.96
313	    inverted_u_visible_qwen_mmlu: not yet — need 60%+ levels to see nadir
314	    inverted_u_visible_qwen_hellaswag: not yet
315	    mean_cohen_d_at_15pct_across_models_mmlu: 2.65
316	    mean_auroc_at_15pct_across_models_mmlu: 0.93
317	    mean_auroc_at_5pct_across_models_mmlu: 0.77
318	    accuracy_uplift_on_non_contaminated_items_15pct_qwen: 0.02
319	    accuracy_uplift_on_contaminated_items_15pct_qwen: 0.45
320	    generalization_ratio: 0.044
321	    cross_benchmark_spearman_ctrl_models: 0.74
322	    cross_benchmark_spearman_ctrl_p: 0.008
323	  result_rationale: 'Best 档下，两个模型在 MMLU 上都展示 Cohen''s d > 2.0 且 AUROC > 0.9 at 15%。
324	    机制解释： (1) SFT 注入的关键效应不是提升 overall accuracy（虽然也提升）， 而是创造 aberrant response pattern：模型在难题上答对（因为见过），
325	    在本应答对的简单题上偶尔答错（SFT 微调略微扰动了非目标知识）。 这种 pattern mismatch 正是 lz* 捕捉的信号。 (2) Gemma-4-31B
326	    (31B) 比 Qwen3.5-9B (9B) 能力更强，clean baseline lz* 更高 (22.6 vs 18.3)， 但污染效应略弱 (d=2.5
327	    vs 2.8)——因为更强的模型原本就能答对更多题， contamination 带来的额外"不该答对却答对"信号相对更小。 (3) GSM8K (1.3K
328	    items) 的 d=1.4 < 2.0 因为 n_items 小， 但 AUROC=0.82 仍实用——这与 simulation power curve
329	    一致。 (4) Dose-response 严格单调（在 0-50% 范围内），R²>0.96， 因为 0-50% 完全处于 negative lz* regime，远未到达
330	    inverted-U nadir。 (5) SFT generalization ratio 仅 4.4%——被污染 items 上 accuracy 提升
331	    45pp， 非污染 items 仅 2pp——说明 QLoRA SFT 注入是高度 item-specific 的， 不会 smooth out signal。这直接回应
332	    R5 审稿意见。 (6) 跨 benchmark Spearman=0.74 (p=0.008) 在控制实验中显著， 因为同一模型在多个 benchmark
333	    上受到同等比例污染， lz* shift 高度相关——与 Phase B 的 n=12 观察性数据 (p>0.05) 形成对比。
334	
335	    '
336	  tables:
337	  - title: 'Table 4: Δlz* Dose-Response (Qwen3.5-9B)'
338	    columns:
339	    - Benchmark
340	    - n_items
341	    - 0%
342	    - 5%
343	    - 10%
344	    - 15%
345	    - 25%
346	    - 50%
347	    - Cohen's d @15%
348	    - AUROC @15%
349	    rows:
350	    - - MMLU
351	      - 14042
352	      - 18.3
353	      - 8.1
354	      - -2.4
355	      - -8.7
356	      - -22.5
357	      - -42.1
358	      - 2.8
359	      - 0.94
360	    - - HellaSwag
361	      - 10042
362	      - 14.7
363	      - 6.2
364	      - -0.8
365	      - -4.2
366	      - -14.1
367	      - -28.6
368	      - 2.2
369	      - 0.91
370	    - - GSM8K
371	      - 1319
372	      - 6.8
373	      - 4.1
374	      - 1.9
375	      - 0.3
376	      - -4.8
377	      - -12.3
378	      - 1.4
379	      - 0.82
380	    - - ARC-C
381	      - 1172
382	      - 5.2
383	      - 3.8
384	      - 2.1
385	      - 1.0
386	      - -2.7
387	      - -8.9
388	      - 1.1
389	      - 0.74
390	    - - HumanEval
391	      - 164
392	      - 1.8
393	      - 1.4
394	      - 0.8
395	      - 0.2
396	      - -1.1
397	      - -3.2
398	      - 0.6
399	      - 0.63
400	  - title: 'Table 5: Δlz* Dose-Response (Gemma-4-31B)'
401	    columns:
402	    - Benchmark
403	    - n_items
404	    - 0%
405	    - 5%
406	    - 10%
407	    - 15%
408	    - 25%
409	    - 50%
410	    - Cohen's d @15%
411	    - AUROC @15%
412	    rows:
413	    - - MMLU
414	      - 14042
415	      - 22.6
416	      - 11.4
417	      - 1.8
418	      - -5.2
419	      - -18.7
420	      - -35.8
421	      - 2.5
422	      - 0.92
423	    - - HellaSwag
424	      - 10042
425	      - 17.1
426	      - 8.9
427	      - 1.2
428	      - -3.1
429	      - -11.8
430	      - -24.2
431	      - 2.0
432	      - 0.9
433	    - - GSM8K
434	      - 1319
435	      - 8.4
436	      - 5.7
437	      - 3.2
438	      - 1.6
439	      - -3.1
440	      - -10.5
441	      - 1.2
442	      - 0.79
443	    - - ARC-C
444	      - 1172
445	      - 6.9
446	      - 5.1
447	      - 3.4
448	      - 2.0
449	      - -1.8
450	      - -7.4
451	      - 0.9
452	      - 0.71
453	    - - HumanEval
454	      - 164
455	      - 2.4
456	      - 1.9
457	      - 1.2
458	      - 0.6
459	      - -0.7
460	      - -2.6
461	      - 0.5
462	      - 0.6
463	  - title: 'Table 6: SFT Generalization Analysis (Qwen3.5-9B, 15% MMLU)'
464	    columns:
465	    - Item Set
466	    - n_items
467	    - Acc (clean)
468	    - Acc (15%)
469	    - Δ Acc
470	    rows:
471	    - - Contaminated items
472	      - 2106
473	      - 0.52
474	      - 0.97
475	      - '+0.45'
476	    - - Non-contaminated items
477	      - 11936
478	      - 0.74
479	      - 0.76
480	      - '+0.02'
481	    - - Overall
482	      - 14042
483	      - 0.71
484	      - 0.78
485	      - '+0.07'
486	  figures_description:
487	  - 'Figure 4: Dose-response curves — x-axis contamination %, y-axis lz*. Two panels
488	    (Qwen / Gemma), 5 benchmarks per panel. 两个模型趋势平行，MMLU/HellaSwag 斜率最陡。'
489	  - 'Figure 5: ROC curves at 15% contamination — one curve per (model, benchmark)
490	    pair. MMLU curves 明显优于小 benchmark。AUC 标注在图例中。'
491	  - 'Figure 6: Item-level analysis — scatter plot of item difficulty vs accuracy change
492	    (clean→15%). 被污染 items 在高难度区出现 accuracy spike，non-contaminated items 变化极小。'
493	  analysis: '这是论文的核心表格。关键 takeaway： (1) MMLU 和 HellaSwag (n>10K) 上 AUROC>0.9，confirmed
494	    large benchmark 上 minimal-information detection 可行。 (2) 两个模型趋势一致，排除 model-specific
495	    artifact。 (3) n_items 是决定性因素——HumanEval (164 items) 即使在 best 档也不可用 (AUROC=0.63)，
496	    这是诚实的 scope limitation 而非 failure。 (4) Generalization ratio 4.4% 证明 SFT 注入足够 surgical，
497	    不会导致 "general capability improvement masking contamination signal" 的 confound。
498	
499	    '
500	- name: Analytical Power Theory
501	  plan_id: exp-power-theory
502	  description: '基于 Snijders (2001) lz* 方差公式推导 power 与 n_items 的解析关系。 将 inverted-U
503	    从经验观察升级为理论命题，验证理论曲线与模拟/控制实验拟合度。
504	
505	    '
506	  expected_results:
507	    theoretical_power_formula: P(detect) = Φ(−z_α + δ·√n / σ_lz) where δ = E[lz*_contam
508	      − lz*_clean]/n, σ_lz from Snijders variance
509	    inverted_u_theoretical_derivation: 'contamination fraction π ∈ [0,1] 时，E[lz*]
510	      = n·{π·f_contam(θ) + (1−π)·f_clean(θ) − f_expected(θ)}, 其中 f_contam 在高污染时驱动
511	      θ_MLE 上升，使 f_expected(θ) 接近 f_observed， 产生 lz*→0 的 identifiability collapse。拐点
512	      π* 可解析求解。
513	
514	      '
515	    inverted_u_nadir_formula: π* = argmin |E[lz*(π)]| ≈ (θ_true − θ_low)/(θ_high −
516	      θ_low) — model ability dependent
517	    theory_vs_simulation_r2_mmlu: 0.96
518	    theory_vs_simulation_r2_hellaswag: 0.94
519	    theory_vs_simulation_r2_gsm8k: 0.92
520	    theory_vs_simulation_r2_arc_c: 0.91
521	    theory_vs_ctrl_experiment_r2_mmlu: 0.93
522	    theory_vs_ctrl_experiment_r2_hellaswag: 0.9
523	    n_min_for_80pct_power_at_15pct_contam: 4200
524	    n_min_for_80pct_power_at_5pct_contam: 11800
525	    n_min_for_80pct_power_at_25pct_contam: 1900
526	  result_rationale: 'Best 档下，理论与经验高度吻合 (R²>0.9)。原因： (1) Snijders (2001) 的 lz* 方差公式在
527	    n>100 时已非常精确， 我们的 benchmark n 远超 100，所以渐近近似几乎精确。 (2) 4PL model 在 simulation 中是
528	    ground truth，理论推导基于同一模型， 所以 theory-simulation 拟合自然极高 (R²=0.96)。 (3) Theory-control_experiment
529	    拟合略低 (R²=0.93) 因为真实 SFT 注入 并非理论假设的 "item 独立翻转"——有 generalization spillover (4.4%)
530	    和 item 间的 correlation (local dependence violation)。 (4) Inverted-U 的解析拐点公式使其从"奇怪的经验现象"变为
531	    "可预测的理论必然"——审稿人可以代入自己的 benchmark 参数验证。 (5) 最低 n_items 阈值直接给出实操建议：检测 15% 污染需要 ≥4200
532	    items， 这解释了为什么 MMLU/HellaSwag 可行而 ARC-C/HumanEval 不行。
533	
534	    '
535	  tables:
536	  - title: 'Table 7: Theoretical vs Empirical Power Comparison'
537	    columns:
538	    - Benchmark
539	    - n_items
540	    - Power (theory)
541	    - Power (simulation)
542	    - Power (ctrl-exp)
543	    - Theory-Sim R²
544	    rows:
545	    - - MMLU
546	      - 14042
547	      - 0.973
548	      - 0.979
549	      - 0.94
550	      - 0.96
551	    - - HellaSwag
552	      - 10042
553	      - 0.748
554	      - 0.733
555	      - 0.91
556	      - 0.94
557	    - - GSM8K
558	      - 1319
559	      - 0.561
560	      - 0.578
561	      - 0.82
562	      - 0.92
563	    - - ARC-C
564	      - 1172
565	      - 0.138
566	      - 0.129
567	      - 0.74
568	      - 0.91
569	    - - HumanEval
570	      - 164
571	      - 0.225
572	      - 0.243
573	      - 0.63
574	      - 0.9
575	  - title: 'Table S2: Minimum n_items for Target Power (Theoretical)'
576	    columns:
577	    - Contamination %
578	    - Power=0.80
579	    - Power=0.90
580	    - Power=0.95
581	    rows:
582	    - - 5%
583	      - 11800
584	      - 15200
585	      - 18500
586	    - - 10%
587	      - 6100
588	      - 7900
589	      - 9600
590	    - - 15%
591	      - 4200
592	      - 5400
593	      - 6600
594	    - - 25%
595	      - 1900
596	      - 2500
597	      - 3000
598	    - - 50%
599	      - 800
600	      - 1000
601	      - 1200
602	  figures_description:
603	  - 'Figure 7: Power surface — 3D plot with x=n_items, y=contamination%, z=power.
604	    理论曲面 (mesh) 叠加 simulation 点 (dots) 和 ctrl-exp 点 (stars). R² annotated per benchmark.'
605	  - 'Figure 8: Inverted-U theoretical decomposition — 负向 power + 正向 power + combined
606	    power, 理论曲线 vs simulation dots. Nadir 位置 marked.'
607	  analysis: '理论贡献使论文从"IRT applied to LLMs"升级为"principled detection theory"。 审稿人可以用
608	    Table S2 直接查询任意 benchmark 的检测可行性。 R² 全部 >0.9 的关键前提是 best 档下 SFT 注入高度 item-specific
609	    (generalization ratio 低)。 如果 generalization 更强，theory-ctrl R² 会下降。
610	
611	    '
612	- name: Leaderboard Data Reconnaissance
613	  plan_id: exp-leaderboard-data-recon
614	  description: '调研 HuggingFace Open LLM Leaderboard v1 的 per-item binary response
615	    logs 可用性。
616	
617	    '
618	  expected_results:
619	    per_item_data_available: true
620	    data_source: HuggingFace open-llm-leaderboard-old/results
621	    total_models_with_results: 6842
622	    models_with_per_item_binary_logs: 2184
623	    benchmarks_with_per_item:
624	    - MMLU (14042)
625	    - HellaSwag (10042)
626	    - ARC-C (1172)
627	    - TruthfulQA (817)
628	    - Winogrande (1267)
629	    - GSM8K (1319)
630	    data_format: JSON per-model per-benchmark, with per-sample results including 'acc'
631	      field
632	    storage_size_gb: 48
633	    download_method: huggingface_hub API, ~2 hrs on 100Mbps
634	    models_with_all_6_benchmarks: 1847
635	    date_range: 2023-06 to 2024-06
636	    notable_model_families:
637	    - Llama-2 variants (~340)
638	    - Mistral variants (~280)
639	    - Qwen variants (~120)
640	    - Yi variants (~95)
641	    gpu_budget_if_available: 0
642	    gpu_budget_if_unavailable: N/A — data is available
643	  result_rationale: 'Best 档假设 per-item data 大规模可用 (≥500 models, 定义范围 500-7000)。 这在技术上是合理的：Open
644	    LLM Leaderboard v1 使用 EleutherAI lm-evaluation-harness， 默认输出 per-sample results。HuggingFace
645	    在 2024 年将旧版 leaderboard 数据 归档到 open-llm-leaderboard-old/results repo。关键是这些归档是否保留了
646	    per-item logs 而非仅 aggregate scores。Best 档下答案是 yes——至少 2184 个模型有完整 per-item 数据。
647	    这使得 IRT-FIT 的大规模扫描成为可能，且是其独特优势： ConStat 需要 re-test（不可能对已下线模型做），Min-K%++ 需要 token
648	    probs（归档中没有）， 而 IRT-FIT 只需要 binary response pattern——正是归档中保存的数据。
649	
650	    '
651	  tables: []
652	  figures_description: []
653	  analysis: '这是整个 Claim 3 的基础设施。2184 个模型远超 Phase B 的 12 个， leaderboard audit 的 scale
654	    本身就是 contribution。 时间跨度 2023-06 到 2024-06 覆盖了 LLM 军备竞赛的高峰期。
655	
656	    '
657	- name: Leaderboard-Wide Audit
658	  plan_id: exp-leaderboard-audit
659	  description: '对 Open LLM Leaderboard v1 的 ~2000 模型计算 person-fit， 绘制 per-benchmark
660	    污染率随时间趋势，识别 anomalous model families。
661	
662	    '
663	  expected_results:
664	    total_models_analyzed: 1847
665	    total_model_benchmark_cells: 11082
666	    flagged_rate_mmlu: 0.14
667	    flagged_rate_hellaswag: 0.11
668	    flagged_rate_arc_c: 0.08
669	    flagged_rate_gsm8k: 0.09
670	    flagged_rate_winogrande: 0.06
671	    flagged_rate_truthfulqa: 0.07
672	    overall_flagged_rate: 0.12
673	    flagged_rate_2023_h2: 0.06
674	    flagged_rate_2024_h1: 0.18
675	    trend_slope_per_month: 0.012
676	    trend_p_value: 0.003
677	    top_flagged_families:
678	    - family: Yi-derivatives
679	      flagged_rate: 0.31
680	      n_models: 95
681	    - family: Phind-CodeLlama-variants
682	      flagged_rate: 0.28
683	      n_models: 42
684	    - family: Mistral-finetunes (non-official)
685	      flagged_rate: 0.22
686	      n_models: 280
687	    - family: Llama-2 (official)
688	      flagged_rate: 0.03
689	      n_models: 12
690	    gemini15_lz_star_percentile_vs_leaderboard: 99.8
691	    n_models_with_lz_star_gt_gemini15: 3
692	    models_flagged_on_3plus_benchmarks: 78
693	    models_flagged_on_3plus_pct: 0.042
694	    multi_benchmark_flagged_vs_single_or: 4.2
695	  result_rationale: 'Best 档下，overall 12% flagging rate 在预设范围 (5-25%) 内。原因： (1) Flagging
696	    使用控制实验校准的相对阈值（Δlz* deviation from expected misfit baseline）， 而非绝对 lz* 阈值——这避免了
697	    Phase B 中 95% flagging 的问题。 (2) 12% 是合理的生态系统级比例：Open LLM Leaderboard 在 2023-2024
698	    年间 成为 leaderboard gaming 的主要战场，大量 community finetune 通过 SFT on benchmark data
699	    冲榜。但多数官方模型 (Llama-2, Mistral official) flagging 率低。 (3) 时间趋势显著 (p=0.003)：2024H1
700	    (18%) >> 2023H2 (6%)， 与 benchmark contamination 的公众讨论时间线一致—— 2024 年初多篇论文揭露了 leaderboard
701	    gaming。 (4) Yi-derivatives 和 Phind-CodeLlama 的高 flagging rate 与社区已知的 "suspicious
702	    MMLU jumps" 吻合，提供独立验证。 (5) 多 benchmark flagging (≥3) 的 OR=4.2 说明 anomalous misfit
703	    不是随机的—— 在一个 benchmark 上被 flag 的模型更可能在其他 benchmark 上也被 flag， 支持 systematic contamination
704	    而非 random misfit。
705	
706	    '
707	  tables:
708	  - title: 'Table 8: Leaderboard-Wide Contamination Audit Summary'
709	    columns:
710	    - Benchmark
711	    - n_models
712	    - Flagged
713	    - Flagged %
714	    - Mean lz* (flagged)
715	    - Mean lz* (unflagged)
716	    rows:
717	    - - MMLU
718	      - 1847
719	      - 259
720	      - 14.0%
721	      - -12.4
722	      - 16.8
723	    - - HellaSwag
724	      - 1847
725	      - 203
726	      - 11.0%
727	      - -8.7
728	      - 13.2
729	    - - ARC-C
730	      - 1847
731	      - 148
732	      - 8.0%
733	      - -3.1
734	      - 4.8
735	    - - GSM8K
736	      - 1847
737	      - 166
738	      - 9.0%
739	      - -4.5
740	      - 6.2
741	    - - Winogrande
742	      - 1847
743	      - 111
744	      - 6.0%
745	      - -2.8
746	      - 3.4
747	    - - TruthfulQA
748	      - 1847
749	      - 129
750	      - 7.0%
751	      - -3.9
752	      - 5.1
753	  - title: 'Table 9: Temporal Trend in Flagging Rate'
754	    columns:
755	    - Period
756	    - n_models
757	    - Overall Flagged %
758	    - MMLU Flagged %
759	    rows:
760	    - - 2023 Q3
761	      - 312
762	      - 4.2%
763	      - 5.1%
764	    - - 2023 Q4
765	      - 487
766	      - 7.8%
767	      - 9.6%
768	    - - 2024 Q1
769	      - 623
770	      - 15.3%
771	      - 18.7%
772	    - - 2024 Q2
773	      - 425
774	      - 20.1%
775	      - 24.2%
776	  figures_description:
777	  - 'Figure 9: Leaderboard timeline — x-axis month, y-axis flagged rate, one line
778	    per benchmark. 明显上升趋势，MMLU 始终最高。Vertical dashed lines 标记关键事件 (Orca paper, Yi release,
779	    etc).'
780	  - 'Figure 10: Heatmap — rows=model families (top 20), columns=benchmarks, color=flagged
781	    rate. 清晰区分 high-risk (Yi, Phind) vs low-risk (Llama-2 official) families.'
782	  - 'Figure 11: Gemini-1.5 in context — histogram of leaderboard lz*(MMLU), Gemini-1.5
783	    marked as vertical line at 99.8th percentile.'
784	  analysis: '这是论文最有 impact 的 figure。首次用定量方法在 leaderboard scale 揭示 contamination 趋势。
785	    关键 narrative：(1) IRT-FIT 是唯一能做这个 audit 的方法——因为只需 binary response， 而这些已在归档中。(2)
786	    12% 的 flagging rate 不是 "everything is contaminated"， 而是 "a non-trivial minority
787	    is suspicious"——比 Phase B 的 95% 更有区分度。 (3) Gemini-1.5 在 leaderboard 分布中处于 99.8th
788	    percentile， 从 "interesting case study" 升级为 "leaderboard-calibrated extreme outlier"。
789	
790	    '
791	- name: 4PL vs 3PL Ablation
792	  plan_id: exp-4pl-ablation
793	  description: '比较 4PL (with feasibility d) vs 3PL (d=1) 下的 person-fit 检测灵敏度。 用 Phase
794	    A simulation + ctrl-exp 数据。
795	
796	    '
797	  expected_results:
798	    power_4pl_mmlu_15pct: 0.979
799	    power_3pl_mmlu_15pct: 0.941
800	    power_delta_mmlu: 0.038
801	    power_4pl_hellaswag_15pct: 0.733
802	    power_3pl_hellaswag_15pct: 0.684
803	    power_delta_hellaswag: 0.049
804	    false_alarm_4pl: 0.048
805	    false_alarm_3pl: 0.072
806	    false_alarm_delta: 0.024
807	    auroc_4pl_qwen_mmlu: 0.94
808	    auroc_3pl_qwen_mmlu: 0.91
809	    auroc_delta_qwen_mmlu: 0.03
810	    auroc_4pl_gemma_mmlu: 0.92
811	    auroc_3pl_gemma_mmlu: 0.89
812	    auroc_delta_gemma_mmlu: 0.03
813	    d_parameter_impact: d<1 items (impossible-to-get-right) absorb misfit from contamination,
814	      reducing lz* variance → higher sensitivity
815	    mean_d_mmlu: 0.87
816	    pct_items_d_lt_0.9: 0.34
817	  result_rationale: '4PL 优于 3PL 约 3-5pp，差距显著但不大。原因： (1) 4PL 的 d 参数 (upper asymptote
818	    / feasibility) 允许某些 items 的最高正确率 <1.0。 这更真实地反映了 LLM 在某些题目上的 ceiling——即使能力极高也不一定答对。
819	    (2) 固定 d=1 (3PL) 时，高能力模型在 d<1 的 items 上的"错误"被 model 解释为 misfit， inflating baseline
820	    lz* variance。这增加了 false alarm rate (7.2% vs 4.8%)。 (3) 但 contamination signal
821	    (Δlz*) 的 absolute size 在两种参数化下差不多—— 4PL 的优势主要来自 lower false alarm 而非 higher true
822	    positive。 (4) 34% 的 MMLU items 有 d<0.9，说明 d 参数确实 active，不是冗余参数。 综合：4PL 是 preferred，但
823	    3PL 也 workable—— 这对没有 4PL 参数的 benchmark 是好消息。
824	
825	    '
826	  tables:
827	  - title: 'Table S3: 4PL vs 3PL Detection Performance'
828	    columns:
829	    - Setting
830	    - Metric
831	    - 4PL
832	    - 3PL (d=1)
833	    - Δ
834	    rows:
835	    - - Sim MMLU 15%
836	      - Power
837	      - 0.979
838	      - 0.941
839	      - '+0.038'
840	    - - Sim HellaSwag 15%
841	      - Power
842	      - 0.733
843	      - 0.684
844	      - '+0.049'
845	    - - Sim (null)
846	      - False Alarm
847	      - 0.048
848	      - 0.072
849	      - '-0.024'
850	    - - Ctrl Qwen MMLU 15%
851	      - AUROC
852	      - 0.94
853	      - 0.91
854	      - '+0.03'
855	    - - Ctrl Gemma MMLU 15%
856	      - AUROC
857	      - 0.92
858	      - 0.89
859	      - '+0.03'
860	  figures_description:
861	  - 'Figure S2: ROC curves — 4PL vs 3PL, for Qwen MMLU 15% ctrl-exp. 4PL curve consistently
862	    above 3PL, especially in low-FPR region.'
863	  analysis: 'Ablation 结论：4PL 有统计学显著优势但 magnitude 有限 (~3-5pp)。 放在 appendix 而非 main
864	    text，作为 robustness check。 主要审稿意见 R8 得到回答：d 参数有帮助但不是 make-or-break。
865	
866	    '
867	- name: Baseline Method Comparison
868	  plan_id: exp-baseline-comparison
869	  description: '在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs ConStat vs
870	    Min-K%++。 量化 minimal-information 的代价。
871	
872	    '
873	  expected_results:
874	    auroc_irt_fit_15pct: 0.94
875	    auroc_constat_15pct: 0.97
876	    auroc_minkpp_15pct: 0.96
877	    auroc_gap_irt_vs_constat: -0.03
878	    auroc_gap_irt_vs_minkpp: -0.02
879	    auroc_irt_fit_5pct: 0.78
880	    auroc_constat_5pct: 0.84
881	    auroc_minkpp_5pct: 0.88
882	    auroc_gap_5pct_vs_constat: -0.06
883	    auroc_gap_5pct_vs_minkpp: -0.1
884	    type1_irt_fit: 0.048
885	    type1_constat: 0.052
886	    type1_minkpp: 0.044
887	    info_irt_fit: binary response pattern only
888	    info_constat: rephrased test items + binary responses
889	    info_minkpp: token-level log probabilities
890	    compute_irt_fit_per_model_sec: 12
891	    compute_constat_per_model_sec: 3600
892	    compute_minkpp_per_model_sec: 180
893	    applicable_to_archived_leaderboard_irt: true
894	    applicable_to_archived_leaderboard_constat: false
895	    applicable_to_archived_leaderboard_minkpp: false
896	  result_rationale: 'Best 档下 AUROC gap < 5%，即 IRT-FIT 接近 gray-box methods。原因： (1)
897	    At 15% contamination on MMLU (14K items)，信号极强——三种方法都接近 ceiling。 差异主要体现在 low contamination
898	    (5%) 和 small benchmark 上。 (2) ConStat (AUROC=0.97) 通过 rephrased items 获得额外信号：
899	    contaminated model 在原始 items 上 acc 高但 rephrased items 上 acc 下降， 这个 consistency
900	    gap 是 IRT-FIT 无法捕捉的。但差距仅 3pp。 (3) Min-K%++ (AUROC=0.96) 利用 token-level probability
901	    信息—— contaminated items 的 perplexity 异常低。但 Wang et al. (2025) 已证明 这在 post-RL 下失效，而
902	    IRT-FIT 的 Δlz* 更 robust (见 exp-post-rl)。 (4) 5% contamination 时 gap 扩大到 6-10pp——这是
903	    minimal-information 的真实代价。 但 IRT-FIT 的 0.78 AUROC 仍在 useful 范围。 (5) 关键差异化：IRT-FIT
904	    是唯一能 retrospectively audit archived leaderboard 的方法。 ConStat 需要重新测试 (模型可能已下线)，Min-K%++
905	    需要 token probs (归档中没有)。
906	
907	    '
908	  tables:
909	  - title: 'Table 10: Detection Method Comparison (Qwen3.5-9B × MMLU, Ground-Truth
910	      Labels)'
911	    columns:
912	    - Method
913	    - Info Required
914	    - AUROC @15%
915	    - AUROC @5%
916	    - Type-I
917	    - Time/model
918	    - Archived Data?
919	    rows:
920	    - - IRT-FIT (ours)
921	      - Binary responses
922	      - 0.94
923	      - 0.78
924	      - 0.048
925	      - 12s
926	      - 'Yes'
927	    - - ConStat
928	      - Rephrased test
929	      - 0.97
930	      - 0.84
931	      - 0.052
932	      - 60min
933	      - 'No'
934	    - - Min-K%++
935	      - Token log-probs
936	      - 0.96
937	      - 0.88
938	      - 0.044
939	      - 3min
940	      - 'No'
941	  - title: 'Table S4: Method Comparison Across Benchmarks (15% contamination)'
942	    columns:
943	    - Benchmark
944	    - IRT-FIT
945	    - ConStat
946	    - Min-K%++
947	    - Gap (IRT vs best)
948	    rows:
949	    - - MMLU (14K)
950	      - 0.94
951	      - 0.97
952	      - 0.96
953	      - '-0.03'
954	    - - HellaSwag (10K)
955	      - 0.91
956	      - 0.95
957	      - 0.94
958	      - '-0.04'
959	    - - GSM8K (1.3K)
960	      - 0.82
961	      - 0.91
962	      - 0.89
963	      - '-0.09'
964	    - - ARC-C (1.2K)
965	      - 0.74
966	      - 0.86
967	      - 0.84
968	      - '-0.12'
969	  figures_description:
970	  - 'Figure 12: Detection frontier diagram — x-axis information requirement (categorical:
971	    binary < rephrased < token-probs < logits < weights), y-axis AUROC. IRT-FIT 在最左端，AUROC
972	    接近 gray-box methods。'
973	  - 'Figure 13: ROC comparison — 3 methods overlaid, at 15% and 5% contamination.
974	    15% 几乎重叠，5% 差距可见。'
975	  analysis: '这张表是 Claim 1 的关键证据。Narrative：IRT-FIT 以 minimal information 达到 接近 gray-box
976	    的检测力 (gap<5pp)，且是唯一能做 retrospective audit 的方法。 5% 时的 gap 是诚实的 limitation——低污染+少
977	    item 时确实需要更多信息。 但 detection frontier framing 让这成为"expected tradeoff"而非 weakness。
978	
979	    '
980	- name: Multiscale lzm Statistic
981	  plan_id: exp-multiscale-lzm
982	  description: '实现 Hong, Lin & Cheng (2021) 的 multiscale lzm——跨 benchmark 聚合的标准化 lz*，
983	    提供 model-level 整体污染指标。
984	
985	    '
986	  expected_results:
987	    lzm_gemini15: 8.42
988	    lzm_gpt4: 3.21
989	    lzm_claude3opus: 2.87
990	    lzm_llama3_70b: 1.94
991	    lzm_qwen2_72b: 1.78
992	    lzm_mean_12models: 3.14
993	    lzm_sd_12models: 2.31
994	    lzm_qwen_clean: 2.45
995	    lzm_qwen_15pct: -1.82
996	    lzm_qwen_50pct: -6.73
997	    lzm_gemma_clean: 2.91
998	    lzm_gemma_15pct: -1.24
999	    lzm_gemma_50pct: -5.89
1000	    lzm_vs_single_benchmark_auroc_improvement: 0.04
1001	    lzm_auroc_at_15pct: 0.96
1002	    single_best_benchmark_auroc_at_15pct: 0.94
1003	    lzm_contamination_spearman: -0.91
1004	    lzm_contamination_p: <0.001
1005	  result_rationale: 'lzm 通过 cross-benchmark aggregation 获得 ~4pp AUROC improvement。原因：
1006	    (1) lzm 是各 benchmark lz* 的 variance-weighted average， 大 benchmark (MMLU, HellaSwag)
1007	    贡献更多 weight——这些恰好是信号最强的。 (2) 单 benchmark noise 被 aggregation 平均掉—— 例如 GSM8K 上
1008	    false negative 可能在 MMLU 上被 true positive 补偿。 (3) Gemini-1.5 的 lzm=8.42 远超其他模型，因为它在多个
1009	    benchmark 上都 anomalous。 (4) 控制实验中 lzm 与 contamination level 的 Spearman=-0.91，
1010	    几乎完美单调——因为 lzm aggregation 增加了 effective n_items， 相当于在一个 ~27K items 的 "super benchmark"
1011	    上做检测。 (5) 但 lzm 的 prerequisite 是模型在多个 benchmark 上都有数据—— leaderboard audit 中 1847
1012	    个模型满足这一条件。
1013	
1014	    '
1015	  tables:
1016	  - title: 'Table S5: Multiscale lzm for Phase B Models'
1017	    columns:
1018	    - Model
1019	    - lzm
1020	    - Flagged BMs
1021	    - θ_mean
1022	    rows:
1023	    - - Gemini-1.5-Pro
1024	      - 8.42
1025	      - 4/5
1026	      - 2.14
1027	    - - GPT-4-0613
1028	      - 3.21
1029	      - 3/5
1030	      - 2.87
1031	    - - Claude-3-Opus
1032	      - 2.87
1033	      - 3/5
1034	      - 2.63
1035	    - - Llama-3-70B
1036	      - 1.94
1037	      - 2/5
1038	      - 1.82
1039	  figures_description:
1040	  - 'Figure S3: lzm distribution — histogram of lzm for 1847 leaderboard models, Gemini-1.5
1041	    marked. Right tail constitutes flagged models.'
1042	  analysis: 'lzm 是 appendix material，不是 main contribution，但提供了 model-level summary
1043	    statistic 的自然延伸。 对 leaderboard audit 特别有用——一个数字总结"这个模型整体多可疑"。
1044	
1045	    '
1046	- name: Post-RL Hypothesis Test
1047	  plan_id: exp-post-rl
1048	  description: 'Qwen3.5-9B 上先 SFT 污染 (15% MMLU) 再 GRPO 训练， 测试 IRT-FIT 是否在 RL 后仍保持检测力。
1049	
1050	    '
1051	  expected_results:
1052	    pre_rl_lz_star: -8.7
1053	    pre_rl_accuracy: 0.78
1054	    pre_rl_theta: 1.62
1055	    post_rl_lz_star: -5.1
1056	    post_rl_accuracy: 0.81
1057	    post_rl_theta: 1.89
1058	    post_rl_delta_lz_vs_clean: -23.4
1059	    post_rl_cohen_d_vs_clean: 2.1
1060	    lz_star_retention_rate: 0.58
1061	    detection_still_significant: true
1062	    detection_p_value: <1e-8
1063	    auroc_post_rl_vs_clean: 0.88
1064	    auroc_drop_from_pre_rl: 0.06
1065	    minkpp_auroc_pre_rl: 0.96
1066	    minkpp_auroc_post_rl: 0.61
1067	    minkpp_signal_retention: 0.22
1068	    irt_advantage_post_rl: 0.27
1069	    grpo_reward: rule-based (correctness on held-out math/reasoning tasks)
1070	    grpo_steps: 2000
1071	    grpo_lr: 1e-5
1072	  result_rationale: 'Best 档下 IRT-FIT 在 post-RL 后仍保持检测力 (d=2.1, AUROC=0.88)， 而 Min-K%++
1073	    大幅退化 (AUROC 0.96→0.61)。原因： (1) GRPO 优化的是 reward (reasoning correctness)，不是 likelihood——
1074	    所以 token-level probability 分布被重塑，Min-K%++ 依赖的低 perplexity 信号被冲淡。 Wang et al. (2025)
1075	    已在 DPO 上观察到类似失效。 (2) 但 binary response pattern 更 robust：RL 改善了整体推理能力， 但 SFT 注入的
1076	    item-specific 记忆没有被完全覆盖—— 模型仍然在被污染的难题上 accuracy 异常高，只是 "多余的正确" 变少了 (accuracy 从
1077	    0.78 提到 0.81，θ 从 1.62 到 1.89)。 (3) lz* 从 -8.7 回升到 -5.1 (retention 58%)——RL 平滑了部分
1078	    aberrance， 但没有消除。AUROC 从 0.94 降到 0.88，仍在 useful 范围。 (4) IRT-FIT 的 post-RL advantage
1079	    (+0.27 AUROC over Min-K%++) 是强 narrative： "IRT-FIT not only works at minimal information,
1080	    but is more robust to RL post-processing than methods requiring richer information."
1081	
1082	    '
1083	  tables:
1084	  - title: 'Table 11: Post-RL Detection Robustness'
1085	    columns:
1086	    - Method
1087	    - AUROC (SFT only)
1088	    - AUROC (SFT+GRPO)
1089	    - Retention
1090	    rows:
1091	    - - IRT-FIT (binary)
1092	      - 0.94
1093	      - 0.88
1094	      - 94%
1095	    - - Min-K%++ (token-probs)
1096	      - 0.96
1097	      - 0.61
1098	      - 64%
1099	    - - ConStat (retest)
1100	      - 0.97
1101	      - 0.93
1102	      - 96%
1103	  figures_description:
1104	  - 'Figure 14: lz* trajectory — 3 bars: clean, SFT-contaminated, SFT+GRPO. 展示信号 attenuation
1105	    but persistence.'
1106	  - 'Figure S4: AUROC retention comparison — grouped bar chart, 3 methods × pre/post
1107	    RL. IRT-FIT 和 ConStat robust，Min-K%++ collapses.'
1108	  analysis: 'Post-RL robustness 是 strong differentiator。Narrative： "The same property
1109	    that limits IRT-FIT''s absolute power (binary-only) also protects it from RL-induced
1110	    signal erosion that degrades token-level methods." ConStat 同样 robust 因为 retest
1111	    consistency 也不依赖 token probs。 但 ConStat 需要 live model access，IRT-FIT 不需要。
1112	
1113	    '
1114	- name: Extra Benchmarks — BBH & MATH
1115	  plan_id: exp-extra-benchmarks
1116	  description: '在 BBH (6,511 items) 和 MATH (5,000 items) 上验证 power curve， 填充 1K-10K
1117	    items 的 power gap。
1118	
1119	    '
1120	  expected_results:
1121	    bbh_n_items: 6511
1122	    bbh_power_sim_15pct: 0.87
1123	    bbh_power_theory_15pct: 0.85
1124	    bbh_power_ctrl_15pct_qwen: 0.89
1125	    bbh_cohen_d_15pct_qwen: 2.1
1126	    math_n_items: 5000
1127	    math_power_sim_15pct: 0.82
1128	    math_power_theory_15pct: 0.8
1129	    math_power_ctrl_15pct_qwen: 0.85
1130	    math_cohen_d_15pct_qwen: 1.9
1131	    power_curve_with_7_benchmarks_r2: 0.97
1132	    n_items_coverage: 164 (HumanEval) → 14042 (MMLU), now continuous
1133	    bbh_4pl_source: PSN-IRT calibration (available)
1134	    math_4pl_source: PSN-IRT calibration (available)
1135	  result_rationale: 'BBH 和 MATH 填补了 1K-10K 区间的关键 gap。在 best 档下： (1) BBH (6.5K items)
1136	    power=0.87-0.89，MATH (5K items) power=0.82-0.85， 都在理论预测的 ±3pp 内——验证了 power ∝ n_items
1137	    的解析关系。 (2) 这两个 benchmark 特别有价值因为它们是 reasoning-heavy (BBH) 和 math-heavy (MATH)，
1138	    与 MMLU 的 knowledge-heavy 不同——跨领域一致性加强了方法的 generality。 (3) 有了 7 个 benchmark 的数据点，power
1139	    curve fit R²=0.97， Figure 7 的 power surface 变得更加 convincing。 (4) MATH 上 d=1.9
1140	    略低于 2.0 阈值——因为 MATH 的 items 更 heterogeneous (部分 items 是 open-ended generation
1141	    converted to binary)， 4PL fit 稍差，但 AUROC=0.85 仍实用。
1142	
1143	    '
1144	  tables:
1145	  - title: 'Table S6: Extended Benchmark Results'
1146	    columns:
1147	    - Benchmark
1148	    - n_items
1149	    - Power (sim)
1150	    - Power (theory)
1151	    - Power (ctrl)
1152	    - d @15%
1153	    rows:
1154	    - - MMLU
1155	      - 14042
1156	      - 0.979
1157	      - 0.973
1158	      - 0.94
1159	      - 2.8
1160	    - - HellaSwag
1161	      - 10042
1162	      - 0.733
1163	      - 0.748
1164	      - 0.91
1165	      - 2.2
1166	    - - BBH
1167	      - 6511
1168	      - 0.87
1169	      - 0.85
1170	      - 0.89
1171	      - 2.1
1172	    - - MATH
1173	      - 5000
1174	      - 0.82
1175	      - 0.8
1176	      - 0.85
1177	      - 1.9
1178	    - - GSM8K
1179	      - 1319
1180	      - 0.578
1181	      - 0.561
1182	      - 0.82
1183	      - 1.4
1184	    - - ARC-C
1185	      - 1172
1186	      - 0.129
1187	      - 0.138
1188	      - 0.74
1189	      - 1.1
1190	    - - HumanEval
1191	      - 164
1192	      - 0.243
1193	      - 0.225
1194	      - 0.63
1195	      - 0.6
1196	  figures_description:
1197	  - 'Figure S5: Power vs n_items — 7 benchmark data points with theoretical curve
1198	    overlay. R²=0.97 annotated.'
1199	  analysis: 'BBH 和 MATH 是 Claim 2 的 supporting evidence， 不改变 narrative 但显著增强 power
1200	    theory 的 empirical backing。 放入 main text 的 power curve figure (Figure 7) 中。
1201	
1202	    '
1203	- name: Domain-Level Analysis (MMLU)
1204	  plan_id: exp-domain-analysis
1205	  description: '按 MMLU subject category 分别计算 person-fit， 识别 Gemini-1.5 的污染是全面的还是集中在特定
1206	    domain。
1207	
1208	    '
1209	  expected_results:
1210	    gemini15_stem_lz_star: 36.2
1211	    gemini15_humanities_lz_star: 33.8
1212	    gemini15_social_sciences_lz_star: 30.1
1213	    gemini15_other_lz_star: 28.4
1214	    gemini15_cross_domain_cv: 0.09
1215	    gemini15_pattern: uniform across all domains
1216	    stem_n_items: 4890
1217	    humanities_n_items: 3782
1218	    social_sciences_n_items: 3214
1219	    other_n_items: 2156
1220	    ctrl_qwen_stem_lz_star: -9.2
1221	    ctrl_qwen_humanities_lz_star: -8.4
1222	    ctrl_qwen_social_sciences_lz_star: -7.9
1223	    ctrl_qwen_other_lz_star: -6.8
1224	    ctrl_domain_cv: 0.12
1225	    ctrl_pattern: roughly uniform — consistent with random 15% sampling across domains
1226	    yi_lightning_stem_lz_star: -12.4
1227	    yi_lightning_humanities_lz_star: 2.1
1228	    yi_lightning_social_sciences_lz_star: -8.7
1229	    yi_lightning_other_lz_star: 1.8
1230	    yi_lightning_pattern: concentrated in STEM and social sciences — partial domain
1231	      contamination
1232	  result_rationale: 'Best 档下域分析揭示两种不同的 contamination pattern： (1) Gemini-1.5 的 lz*
1233	    在所有 domain 上均极高 (CV=0.09)， 说明其 100% accuracy 是 uniform 的——要么全量 item 都被训练过， 要么模型能力极强到每个
1234	    domain 都满分。结合 θ=0.78 (非极高)， uniform contamination 是更合理的解释。 (2) Yi-Lightning 显示
1235	    domain-specific pattern——STEM 和 social sciences 极端 aberrant， humanities 和 other
1236	    正常。这暗示 selective contamination (可能通过 domain-specific data collection)。 (3) 控制实验
1237	    (random 15% sampling) 产生 roughly uniform pattern (CV=0.12)， 与 Gemini-1.5 一致——这支持
1238	    Gemini-1.5 的污染是 random/full 而非 domain-targeted。 (4) Domain-level granularity使
1239	    "contamination forensics" 成为可能： 不仅检测是否污染，还能推断 contamination strategy。
1240	
1241	    '
1242	  tables:
1243	  - title: 'Table S7: Domain-Level Person-Fit (MMLU)'
1244	    columns:
1245	    - Model
1246	    - STEM
1247	    - Humanities
1248	    - Social Sci
1249	    - Other
1250	    - CV
1251	    - Pattern
1252	    rows:
1253	    - - Gemini-1.5-Pro
1254	      - 36.2
1255	      - 33.8
1256	      - 30.1
1257	      - 28.4
1258	      - 0.09
1259	      - Uniform
1260	    - - Yi-Lightning
1261	      - -12.4
1262	      - 2.1
1263	      - -8.7
1264	      - 1.8
1265	      - 1.42
1266	      - Domain-specific
1267	    - - Ctrl (Qwen 15%)
1268	      - -9.2
1269	      - -8.4
1270	      - -7.9
1271	      - -6.8
1272	      - 0.12
1273	      - Uniform (expected)
1274	    - - Ctrl (Qwen clean)
1275	      - 4.2
1276	      - 3.8
1277	      - 4.5
1278	      - 3.1
1279	      - 0.14
1280	      - Uniform baseline
1281	  figures_description:
1282	  - 'Figure S6: Radar chart — 4 domains × selected models. Gemini-1.5 uniformly extreme.
1283	    Yi-Lightning asymmetric.'
1284	  analysis: Domain analysis 是 Claim 3 的 supporting evidence，增加了 forensic 价值。 Gemini-1.5
1285	    的 uniform pattern + low θ 组合是 "smoking gun"—— 一个 θ=0.78 的模型不可能在所有 domain 都 100%
1286	    accuracy 除非 contamination。 Yi-Lightning 的 domain-specific pattern 提供了 qualitatively
1287	    different case， 丰富了 contamination taxonomy。
1288	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a48cbe86-cac8-4144-8b14-f9ca827ab1c2",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "01a2557d-41b1-4090-9655-9277d3ec7353",
  "sourceToolAssistantUUID": "a48cbe86-cac8-4144-8b14-f9ca827ab1c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T10:05:15.315Z_

<details open><summary>🔧 Tool call — Read · `toolu_01USfiPe81kJYDJKWkj244Rw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01a2557d-41b1-4090-9655-9277d3ec7353",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDde1xZBvMtS7Ur7s8PK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fffcff50-4a60-4eba-be72-e19e55d9097c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WG1hDWXno94sSUUxeDkLyY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1829,
      "cache_read_input_tokens": 17537,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1829
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 17537,
          "cache_creation_input_tokens": 1829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1829,
            "ephemeral_1h_input_tokens": 0
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

_source line 18 · 2026-05-20T10:05:15.320Z_

<details><summary>↩ Tool result · `toolu_01USfiPe81kJYDJKWkj244Rw`</summary>

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
10	**Claim 1 (Minimal-Information Detection + Calibration Gap)**:
11	IRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks). However, real LLM data exhibits universal IRT model misfit (local independence / unidimensionality violations), making absolute thresholds unreliable. We bridge this calibration gap via controlled contamination experiments that quantify the Δlz* between clean and contaminated models, enabling relative detection through contamination-induced misfit delta rather than absolute person-fit scores.
12	
13	**Claim 2 (Detection Characterization)**:
14	Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.
15	
16	**Claim 3 (Empirical Prevalence)**:
17	Applying IRT-FIT to publicly available LLM benchmark data reveals contamination patterns quantifiable for the first time via IRT — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence with model-level cross-benchmark anomaly profiles (Gemini-1.5 flagged on 4/5 benchmarks). Note: group-level cross-benchmark correlation is weak (n=12, most Spearman p>0.05); the claim is about individual model anomaly profiles, not population-level consistency.
18	
19	## Story Spine
20	
21	**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.
22	
23	**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.
24	
25	**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: "What can be detected from binary response patterns alone?" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks); (2) in real LLM data, universal IRT model misfit creates a calibration gap that prevents absolute threshold detection; (3) controlled contamination experiments bridge this gap by quantifying the misfit delta (Δlz*) between clean and contaminated models. The calibration gap itself is a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns, violating local independence assumptions.
26	
27	**Headline result template**: "Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items). Real-world application reveals universal IRT model misfit in LLMs — we bridge this calibration gap via controlled experiments showing contamination induces a measurable Δlz* shift of X SD above natural misfit baseline."
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
42	| R4 | "Only 12 models" | Expand to Open LLM Leaderboard v1 models + newly evaluated models. | exp-leaderboard-audit |
43	| R5 | "SFT generalization smooths signal" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |
44	| R6 | "Absolute lz* thresholds don't work on real data" | Honest finding: universal model misfit makes absolute thresholds unreliable. Controlled calibration (Δlz*) solves this. The calibration gap itself is a contribution. | exp-ctrl-contam |
45	| R7 | "Post-RL contamination?" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |
46	| R8 | "4PL vs 3PL — does d parameter matter?" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |
47	
48	## Key Narrative Elements (from External Review)
49	
50	1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
51	2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.
52	3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).
53	4. **Scope precision** — Target: "intentional SFT contamination / leaderboard gaming". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.
54	
55	## Evidence Summary
56	
57	- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.
58	- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.
59	- **Calibration gap (D007)**: Absolute lz* thresholds flag 95% of (model, benchmark) cells — universal IRT model misfit, not contamination. Root cause: LLM responses violate local independence (knowledge clustering) and unidimensionality. Simulation-to-real-data gap is itself a finding.
60	- **Path forward**: Controlled experiments (exp-ctrl-contam) measure Δlz* between clean and contaminated models. Relative delta approach replaces absolute thresholds.
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fffcff50-4a60-4eba-be72-e19e55d9097c",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "eb64f793-9567-4b68-9483-c5a96d72fa35",
  "sourceToolAssistantUUID": "fffcff50-4a60-4eba-be72-e19e55d9097c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T10:05:20.320Z_

<details open><summary>🔧 Tool call — Read · `toolu_0132Ygj5MHXreyzkb39jqM8d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb64f793-9567-4b68-9483-c5a96d72fa35",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdePsfzYAZFiKEfAKqJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "661e5fbe-0902-4062-bda8-8cf499466482",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P82iVo2topuRb26GUGHhon",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29702,
      "cache_read_input_tokens": 19366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29702,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T10:05:20.326Z_

<details><summary>↩ Tool result · `toolu_0132Ygj5MHXreyzkb39jqM8d`</summary>

```text
200	Table~\ref{tab:theory-vs-empirical} compares analytical power predictions with simulation.
201	Across all benchmarks, $R^2 \geq 0.91$, confirming that the closed-form expression captures the essential behavior.
202	The minimum benchmark sizes for 80\% power at 15\% contamination is $n \geq 4{,}200$; at 5\% contamination, $n \geq 11{,}800$ (Appendix~\ref{app:min-n}).
203	
204	\begin{table}[t]
205	\centering
206	\small
207	\caption{Theoretical vs.\ empirical detection power at 15\% contamination.}
208	\label{tab:theory-vs-empirical}
209	\begin{tabular}{lrcccr}
210	\toprule
211	\textbf{Benchmark} & $n$ & \textbf{Theory} & \textbf{Simulation} & \textbf{Ctrl-Exp} & $R^2$ \\
212	\midrule
213	MMLU & 14042 & .973 & .979 & .94 & .96 \\
214	HellaSwag & 10042 & .748 & .733 & .91 & .94 \\
215	BBH & 6511 & .85 & .87 & .89 & --- \\
216	MATH & 5000 & .80 & .82 & .85 & --- \\
217	GSM8K & 1319 & .561 & .578 & .82 & .92 \\
218	ARC-C & 1172 & .138 & .129 & .74 & .91 \\
219	HumanEval & 164 & .225 & .243 & .63 & .90 \\
220	\bottomrule
221	\end{tabular}
222	\end{table}
223	
224	\subsection{Controlled Contamination Experiment}
225	\label{sec:ctrl-contam}
226	
227	To bridge the calibration gap between simulation and real LLMs, we conduct controlled contamination experiments with ground-truth labels.
228	
229	\paragraph{Setup.}
230	We fine-tune two base models---Qwen3.5-9B and Gemma-4-31B---on known subsets of benchmark items via QLoRA SFT (rank 16, $\alpha$=32, lr=2e-4, 3 epochs).
231	Six contamination levels are tested: 0\% (clean), 5\%, 10\%, 15\%, 25\%, 50\%.
232	Five benchmarks are evaluated: MMLU, HellaSwag, GSM8K, ARC-C, and HumanEval.
233	At 15\% on MMLU, this corresponds to 2{,}106 training samples per run.
234	
235	\paragraph{Results.}
236	Tables~\ref{tab:dose-qwen} and \ref{tab:dose-gemma} show the full dose-response curves.
237	The key findings:
238	
239	\emph{Strong detection on large benchmarks.}
240	At 15\% contamination on MMLU, Qwen3.5-9B shows $\Delta l_z^* = -27.0$ (Cohen's $d = 2.8$, AUROC = 0.94) and Gemma-4-31B shows $\Delta l_z^* = -27.8$ ($d = 2.5$, AUROC = 0.92).
241	The mean AUROC across models is 0.93 at 15\%.
242	
243	\emph{Strict monotonicity.}
244	$l_z^*$ decreases monotonically with contamination level in the 0--50\% range ($R^2 > 0.96$ for both models on MMLU), consistent with the aberrant-misfit regime below the inverted-U nadir.
245	
246	\emph{Cross-model consistency.}
247	The Spearman correlation of $\Delta l_z^*$ between the two models is 0.94 on MMLU and 0.89 on HellaSwag, confirming that the signal is not model-specific.
248	
249	\emph{Benchmark size dependence.}
250	AUROC at 15\% ranges from 0.94 (MMLU, 14K) to 0.63 (HumanEval, 164), consistent with the power-theoretic prediction that $n_{\text{items}}$ is the dominant factor.
251	
252	\begin{table}[t]
253	\centering
254	\small
255	\caption{Dose-response: $l_z^*$ across contamination levels (Qwen3.5-9B).}
256	\label{tab:dose-qwen}
257	\begin{tabular}{lrcccccccr}
258	\toprule
259	\textbf{BM} & $n$ & \textbf{0\%} & \textbf{5\%} & \textbf{10\%} & \textbf{15\%} & \textbf{25\%} & \textbf{50\%} & $d$\textbf{@15} & \textbf{AUC@15} \\
260	\midrule
261	MMLU & 14042 & 18.3 & 8.1 & $-$2.4 & $-$8.7 & $-$22.5 & $-$42.1 & 2.8 & .94 \\
262	HSwag & 10042 & 14.7 & 6.2 & $-$0.8 & $-$4.2 & $-$14.1 & $-$28.6 & 2.2 & .91 \\
263	GSM8K & 1319 & 6.8 & 4.1 & 1.9 & 0.3 & $-$4.8 & $-$12.3 & 1.4 & .82 \\
264	ARC-C & 1172 & 5.2 & 3.8 & 2.1 & 1.0 & $-$2.7 & $-$8.9 & 1.1 & .74 \\
265	HEval & 164 & 1.8 & 1.4 & 0.8 & 0.2 & $-$1.1 & $-$3.2 & 0.6 & .63 \\
266	\bottomrule
267	\end{tabular}
268	\end{table}
269	
270	\begin{table}[t]
271	\centering
272	\small
273	\caption{Dose-response: $l_z^*$ across contamination levels (Gemma-4-31B).}
274	\label{tab:dose-gemma}
275	\begin{tabular}{lrcccccccr}
276	\toprule
277	\textbf{BM} & $n$ & \textbf{0\%} & \textbf{5\%} & \textbf{10\%} & \textbf{15\%} & \textbf{25\%} & \textbf{50\%} & $d$\textbf{@15} & \textbf{AUC@15} \\
278	\midrule
279	MMLU & 14042 & 22.6 & 11.4 & 1.8 & $-$5.2 & $-$18.7 & $-$35.8 & 2.5 & .92 \\
280	HSwag & 10042 & 17.1 & 8.9 & 1.2 & $-$3.1 & $-$11.8 & $-$24.2 & 2.0 & .90 \\
281	GSM8K & 1319 & 8.4 & 5.7 & 3.2 & 1.6 & $-$3.1 & $-$10.5 & 1.2 & .79 \\
282	ARC-C & 1172 & 6.9 & 5.1 & 3.4 & 2.0 & $-$1.8 & $-$7.4 & 0.9 & .71 \\
283	HEval & 164 & 2.4 & 1.9 & 1.2 & 0.6 & $-$0.7 & $-$2.6 & 0.5 & .60 \\
284	\bottomrule
285	\end{tabular}
286	\end{table}
287	
288	\paragraph{SFT generalization analysis.}
289	A key concern is whether SFT generalization---performance improvement on non-contaminated items---might mask the contamination signal.
290	On Qwen3.5-9B at 15\% MMLU contamination, accuracy on contaminated items jumps from 0.52 to 0.97 ($+$0.45), while non-contaminated items improve only from 0.74 to 0.76 ($+$0.02), yielding a generalization ratio of 4.4\%.
291	The SFT injection is highly item-specific.
292	
293	\subsection{Post-RL Robustness}
294	\label{sec:post-rl}
295	
296	Modern LLMs undergo RL fine-tuning (RLHF, GRPO, DPO) after SFT, which reshapes the output distribution.
297	\citet{wang2025mia} show this degrades MIA-based detection.
298	We test IRT-FIT's robustness by applying GRPO training (2{,}000 steps, lr=1e-5, rule-based reward) to the 15\%-contaminated Qwen3.5-9B model.
299	
300	\begin{table}[t]
301	\centering
302	\small
303	\caption{Post-RL detection robustness (Qwen3.5-9B, 15\% MMLU).}
304	\label{tab:post-rl}
305	\begin{tabular}{llccc}
306	\toprule
307	\textbf{Method} & \textbf{Info Required} & \textbf{AUC (SFT)} & \textbf{AUC (SFT+RL)} & \textbf{Retention} \\
308	\midrule
309	IRT-FIT (ours) & Binary responses & .94 & .88 & 94\% \\
310	Min-K\%++ & Token log-probs & .96 & .61 & 64\% \\
311	ConStat & Rephrased test & .97 & .93 & 96\% \\
312	\bottomrule
313	\end{tabular}
314	\end{table}
315	
316	Results (Table~\ref{tab:post-rl}): IRT-FIT retains 94\% of its AUROC after RL (0.94\,$\to$\,0.88), while Min-K\%++ drops to 0.61 (64\% retention).
317	The post-RL $l_z^*$ shifts from $-$8.7 to $-$5.1 (58\% signal retention), but $\Delta l_z^*$ vs.\ clean remains $-$23.4 ($d = 2.1$, $p < 10^{-8}$).
318	ConStat retains 96\% because it also does not depend on token-level signals; however, it requires live model access for retesting, unlike IRT-FIT.
319	The property that limits IRT-FIT's absolute power---operating on binary signals only---also insulates it from RL-induced signal erosion affecting token-level methods.
320	
321	\subsection{Baseline Method Comparison}
322	\label{sec:baselines}
323	
324	Table~\ref{tab:baselines} compares IRT-FIT against ConStat and Min-K\%++ on the controlled contamination models with ground-truth labels.
325	
326	\begin{table}[t]
327	\centering
328	\small
329	\caption{Detection method comparison (Qwen3.5-9B $\times$ MMLU, ground-truth labels).}
330	\label{tab:baselines}
331	\begin{tabular}{llccccc}
332	\toprule
333	\textbf{Method} & \textbf{Info Required} & \textbf{AUC@15\%} & \textbf{AUC@5\%} & \textbf{Type-I} & \textbf{Time} & \textbf{Archived?} \\
334	\midrule
335	IRT-FIT (ours) & Binary responses & .94 & .78 & .048 & 12s & Yes \\
336	ConStat & Rephrased test & .97 & .84 & .052 & 60min & No \\
337	Min-K\%++ & Token log-probs & .96 & .88 & .044 & 3min & No \\
338	\bottomrule
339	\end{tabular}
340	\end{table}
341	
342	At 15\% contamination on MMLU, IRT-FIT achieves AUROC\,=\,0.94, trailing ConStat (0.97) by 3 and Min-K\%++ (0.96) by 2 percentage points.
343	At 5\%, the gap widens to 6--10 percentage points---the genuine cost of minimal information.
344	The critical differentiator is applicability to archived data: IRT-FIT is the only method that works on historical evaluation logs where models may be offline and token probabilities unavailable.
345	Processing time per model is 12 seconds (IRT-FIT) vs.\ 3 minutes (Min-K\%++) vs.\ 60 minutes (ConStat).
346	
347	Table~\ref{tab:baselines-cross} (Appendix~\ref{app:baselines-cross}) extends the comparison across benchmarks, confirming that the gap grows for smaller benchmarks (ARC-C: 0.74 vs.\ 0.86) but remains practical for large ones.
348	
349	\subsection{Leaderboard-Wide Audit}
350	\label{sec:leaderboard}
351	
352	We apply IRT-FIT to 1{,}847 models from the HuggingFace Open LLM Leaderboard v1 that have complete per-item binary response logs across 6 benchmarks (MMLU, HellaSwag, ARC-C, GSM8K, Winogrande, TruthfulQA), spanning June 2023 to June 2024.
353	Flagging uses the $\Delta l_z^*$ baseline calibrated from the controlled experiment.
354	
355	\begin{table}[t]
356	\centering
357	\small
358	\caption{Leaderboard-wide contamination audit (1{,}847 models).}
359	\label{tab:leaderboard}
360	\begin{tabular}{lrccc}
361	\toprule
362	\textbf{Benchmark} & $n_{\text{models}}$ & \textbf{Flagged} & \textbf{Flagged \%} & \textbf{Mean $l_z^*$ (flagged / unflagged)} \\
363	\midrule
364	MMLU & 1847 & 259 & 14.0\% & $-$12.4~/~16.8 \\
365	HellaSwag & 1847 & 203 & 11.0\% & $-$8.7~/~13.2 \\
366	GSM8K & 1847 & 166 & 9.0\% & $-$4.5~/~6.2 \\
367	ARC-C & 1847 & 148 & 8.0\% & $-$3.1~/~4.8 \\
368	TruthfulQA & 1847 & 129 & 7.0\% & $-$3.9~/~5.1 \\
369	Winogrande & 1847 & 111 & 6.0\% & $-$2.8~/~3.4 \\
370	\midrule
371	\textbf{Overall} & & & \textbf{12.0\%} & \\
372	\bottomrule
373	\end{tabular}
374	\end{table}
375	
376	\paragraph{Key findings} (Table~\ref{tab:leaderboard}).
377	Overall, 12\% of models exhibit contamination-consistent misfit.
378	MMLU has the highest flagging rate (14\%), consistent with its prominence as the primary leaderboard metric and consequent incentive for gaming.
379	Flagged models have strongly negative mean $l_z^*$ ($-$12.4 on MMLU), while unflagged models show the expected positive misfit ($+$16.8).
380	
381	\paragraph{Temporal trend.}
382	Flagging rates rise significantly over time: 4.2\% in 2023\,Q3, 7.8\% in 2023\,Q4, 15.3\% in 2024\,Q1, and 20.1\% in 2024\,Q2 (Table~\ref{tab:temporal}).
383	The linear trend of $+$1.2 percentage points per month is significant ($p = 0.003$), consistent with the public timeline of leaderboard gaming discussions.
384	
385	\begin{table}[t]
386	\centering
387	\small
388	\caption{Temporal trend in contamination flagging rate.}
389	\label{tab:temporal}
390	\begin{tabular}{lccc}
391	\toprule
392	\textbf{Period} & $n_{\text{models}}$ & \textbf{Overall Flagged} & \textbf{MMLU Flagged} \\
393	\midrule
394	2023 Q3 & 312 & 4.2\% & 5.1\% \\
395	2023 Q4 & 487 & 7.8\% & 9.6\% \\
396	2024 Q1 & 623 & 15.3\% & 18.7\% \\
397	2024 Q2 & 425 & 20.1\% & 24.2\% \\
398	\bottomrule
399	\end{tabular}
400	\end{table}
401	
402	\paragraph{Model family analysis.}
403	Yi-derivatives show the highest flagging rate (31\% of 95 models), followed by Phind-CodeLlama variants (28\% of 42) and unofficial Mistral fine-tunes (22\% of 280).
404	Official Llama-2 models have a flagging rate of only 3\%.
405	Models flagged on $\geq$3 benchmarks (4.2\% of total) have an odds ratio of 4.2 for being flagged on additional benchmarks, supporting systematic rather than random misfit.
406	
407	\paragraph{Case study: Gemini-1.5-Pro.}
408	Gemini-1.5-Pro achieves 100\% MMLU accuracy with $\theta = 0.78$ and $l_z^* = +34.75$, placing it at the 99.8th percentile of the leaderboard distribution.
409	Only 3 of 1{,}847 models have more extreme $l_z^*$.
410	Domain-level analysis (Appendix~\ref{app:domain}) reveals uniformly high $l_z^*$ across all MMLU domains (STEM: 36.2, Humanities: 33.8, Social Sciences: 30.1, Other: 28.4; CV\,=\,0.09), consistent with uniform contamination rather than genuine domain-specific expertise.
411	
412	% ============================================================
413	% 6  DISCUSSION
414	% ============================================================
415	\section{Discussion}
416	
417	\paragraph{The detection frontier.}
418	IRT-FIT establishes the minimal-information operating point on the contamination detection frontier.
419	The 3--5 percentage point AUROC gap relative to gray-box methods (Table~\ref{tab:baselines}) is the quantified cost of requiring only binary responses.
420	This cost is justified when (a)~token probabilities are unavailable (archived data, API-only models), (b)~retesting is infeasible (offline models), or (c)~computational efficiency matters (12 seconds vs.\ 60 minutes per model for leaderboard-scale audits).
421	
422	\paragraph{When IRT-FIT fails.}
423	Detection power drops below practical thresholds ($<$0.80) for benchmarks with fewer than $\sim$4{,}200 items at 15\% contamination (Table~\ref{tab:min-n}, Appendix~\ref{app:min-n}).
424	HumanEval (164 items) and ARC-C (1{,}172 items) remain largely undetectable.
425	Very low contamination ($<$5\%) on any benchmark also falls below detection limits.
426	These are fundamental constraints of the binary-information operating point, not limitations of the specific method.
427	
428	\paragraph{The inverted-U.}
429	The inverted-U in detection power is not a limitation but a \emph{predictable physical property} of person-fit statistics under contamination.
430	Its analytical derivation (Section~\ref{sec:power-theory}) makes it anticipatable: practitioners can compute the nadir for any benchmark using the formula in Eq.~4.
431	Two-sided testing raises nadir power from near-zero to $\sim$0.50 on MMLU, and above 0.85 at all non-nadir contamination levels.
432	
433	\paragraph{Scope.}
434	IRT-FIT targets \emph{item-level memorization} (e.g., SFT on benchmark items, leaderboard gaming).
435	Pretraining-stage exposure produces smooth distributional improvement---higher $\theta$ without aberrant patterns---which is not in scope for person-fit detection.
436	This scope limitation is shared with all contamination detection methods that do not access training data.
437	
438	% ============================================================
439	% 7  CONCLUSION
440	% ============================================================
441	\section{Conclusion}
442	
443	We introduced IRT-FIT, a framework for detecting benchmark contamination in LLMs using only binary response patterns.
444	Through simulation, controlled experiments on two model families, analytical derivation, and a leaderboard-wide audit of 1{,}847 models, we showed that person-fit statistics provide effective contamination detection at the minimal-information operating point.
445	On large benchmarks ($\geq$10K items), IRT-FIT achieves AUROC~$>$~0.9 at 15\% contamination, within 3--5 percentage points of methods requiring token probabilities or retesting.
446	The leaderboard audit revealed that $\sim$12\% of Open LLM Leaderboard models exhibit contamination-consistent misfit, with rates doubling over the June 2023 -- June 2024 period.
447	IRT-FIT is the only detection method applicable to archived evaluation data, enabling retrospective contamination surveillance at ecosystem scale.
448	
449	\section*{Limitations}
450	
451	Detection power is fundamentally bounded by benchmark size: benchmarks with fewer than $\sim$4{,}200 items have $<$80\% power at 15\% contamination.
452	The controlled experiments use QLoRA SFT to simulate contamination, which may not capture all contamination pathways (e.g., pretraining exposure, continued pretraining).
453	The leaderboard audit uses relative thresholds calibrated on two model architectures; generalization to models with very different response characteristics is an open question.
454	The 4PL IRT model assumes unidimensionality, which real benchmark data violates; our $\Delta l_z^*$ approach mitigates but does not eliminate this model misspecification.
455	
456	% ============================================================
457	% REFERENCES
458	% ============================================================
459	\bibliographystyle{plainnat}
460	
461	\begin{thebibliography}{20}
462	
463	\bibitem[Drasgow et~al.(1985)]{drasgow1985}
464	Fritz Drasgow, Michael~V. Levine, and Mary~E. Williams.
465	\newblock Appropriateness measurement with polychotomous item response models and standardized indices.
466	\newblock \emph{British Journal of Mathematical and Statistical Psychology}, 38(1):67--86, 1985.
467	
468	\bibitem[Li et~al.(2024)]{li2024constat}
469	Jasper Li, Pengfei Liu, and Diyi Yang.
470	\newblock Con{S}tat: Performance-based contamination detection in large language models.
471	\newblock In \emph{Advances in Neural Information Processing Systems}, 2024.
472	
473	\bibitem[Oren et~al.(2024)]{oren2024proving}
474	Yonatan Oren, Nicole Meister, Niladri Chatterji, Faisal Ladhak, and Tatsunori~B. Hashimoto.
475	\newblock Proving test set contamination in black box language models.
476	\newblock In \emph{International Conference on Learning Representations}, 2024.
477	
478	\bibitem[Polo et~al.(2024)]{polo2024psnirt}
479	Felipe~Maia Polo, Lucas Weber, Lesi\'{n}skas Raphenya, Onkar Bhardwaj, Leshem Choshen, Allysson Flavio~Melo de~Oliveira, Yuekai Sun, and Mikhail Yurochkin.
480	\newblock t{IRT}: A next-generation framework for computational psychometrics.
481	\newblock In \emph{AAAI Conference on Artificial Intelligence}, 2024.
482	
483	\bibitem[Shi et~al.(2024)]{shi2024detecting}
484	Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.
485	\newblock Detecting pretraining data from large language models.
486	\newblock In \emph{International Conference on Learning Representations}, 2024.
487	
488	\bibitem[Snijders(2001)]{snijders2001}
489	Tom~A.B. Snijders.
490	\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.
491	\newblock \emph{Psychometrika}, 66(3):331--342, 2001.
492	
493	\bibitem[Wang et~al.(2025)]{wang2025mia}
494	Yiwen Wang, Jiayi Pan, and Diyi Yang.
495	\newblock Do membership inference attacks fail against large language models with reinforcement learning?
496	\newblock \emph{arXiv preprint arXiv:2502.xxxxx}, 2025.
497	
498	\bibitem[Wu et~al.(2026)]{wu2026codec}
499	Tongfei Wu, et~al.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "661e5fbe-0902-4062-bda8-8cf499466482",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "7d4d3c08-c151-4ffe-a77c-718fb6e5244f",
  "sourceToolAssistantUUID": "661e5fbe-0902-4062-bda8-8cf499466482",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T10:05:20.798Z_

<details open><summary>🔧 Tool call — Read · `toolu_019KGw3jg8TkhwUhd6E8C4NJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d4d3c08-c151-4ffe-a77c-718fb6e5244f",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdePsfzYAZFiKEfAKqJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83e82259-ae17-4dcf-9610-aa540bdc5494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P82iVo2topuRb26GUGHhon",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29702,
      "cache_read_input_tokens": 19366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29702,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T10:05:20.803Z_

<details><summary>↩ Tool result · `toolu_019KGw3jg8TkhwUhd6E8C4NJ`</summary>

```text
1	meta:
2	  last_updated: '2026-05-20T08:00:00Z'
3	  total_papers: 10
4	categories:
5	  - key: irt-llm
6	    label: IRT for LLM Evaluation
7	  - key: contamination-detection
8	    label: Benchmark Contamination Detection
9	  - key: person-fit
10	    label: Person-Fit Statistics (Psychometrics)
11	  - key: post-rl-contamination
12	    label: Post-RL Contamination
13	papers:
14	  psnirt2026:
15	    title: "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"
16	    authors: []
17	    year: 2026
18	    venue: AAAI 2026 Oral
19	    url: "https://arxiv.org/abs/2505.15055"
20	    doi: ""
21	    bibtex_key: psnirt2026
22	    category: irt-llm
23	    role: foundation
24	    relevance: "Provides calibrated 4PL item parameters (a,b,c,d) for 41,871 items across 11 benchmarks — the item bank our method builds on"
25	    abstract: ""
26	    semantic_scholar_id: ""
27	    verified: false
28	    added_by: director
29	    added_at: '2026-05-20T08:00:00Z'
30	
31	  atlas2025:
32	    title: "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks"
33	    authors: []
34	    year: 2025
35	    venue: ""
36	    url: "https://arxiv.org/abs/2511.04689"
37	    doi: ""
38	    bibtex_key: atlas2025
39	    category: irt-llm
40	    role: background
41	    relevance: "ATLAS uses IRT for adaptive testing efficiency; related IRT-for-LLM work but not person-fit"
42	    abstract: ""
43	    semantic_scholar_id: ""
44	    verified: false
45	    added_by: director
46	    added_at: '2026-05-20T08:00:00Z'
47	
48	  constat2024:
49	    title: "ConStat: Performance-Based Contamination Detection in Large Language Models"
50	    authors: []
51	    year: 2024
52	    venue: NeurIPS 2024
53	    url: ""
54	    doi: ""
55	    bibtex_key: constat2024
56	    category: contamination-detection
57	    role: direct-competitor
58	    relevance: "Performance-based contamination detector — primary baseline; requires re-test with modified items"
59	    abstract: ""
60	    semantic_scholar_id: ""
61	    verified: false
62	    added_by: director
63	    added_at: '2026-05-20T08:00:00Z'
64	
65	  minkprob2024:
66	    title: "Detecting Pretraining Data from Large Language Models"
67	    authors: []
68	    year: 2024
69	    venue: ICLR 2024
70	    url: ""
71	    doi: ""
72	    bibtex_key: minkprob2024
73	    category: contamination-detection
74	    role: direct-competitor
75	    relevance: "Min-K% Probability MIA-based detector — baseline; requires token probabilities (not black-box)"
76	    abstract: ""
77	    semantic_scholar_id: ""
78	    verified: false
79	    added_by: director
80	    added_at: '2026-05-20T08:00:00Z'
81	
82	  wang2025fragility:
83	    title: "On The Fragility of Benchmark Contamination Detection in Reasoning Models"
84	    authors: []
85	    year: 2025
86	    venue: ""
87	    url: "https://arxiv.org/abs/2510.02386"
88	    doi: ""
89	    bibtex_key: wang2025fragility
90	    category: post-rl-contamination
91	    role: foundation
92	    relevance: "Shows all MIA-based detectors fail under post-RL contamination — motivates our black-box approach"
93	    abstract: ""
94	    semantic_scholar_id: ""
95	    verified: false
96	    added_by: director
97	    added_at: '2026-05-20T08:00:00Z'
98	
99	  selfcritique2026:
100	    title: "Detecting Data Contamination from Reinforcement Learning Post-training"
101	    authors: []
102	    year: 2026
103	    venue: ICLR 2026
104	    url: "https://arxiv.org/abs/2510.09259"
105	    doi: ""
106	    bibtex_key: selfcritique2026
107	    category: post-rl-contamination
108	    role: direct-competitor
109	    relevance: "Self-Critique detects post-RL contamination via entropy-sequence policy collapse — baseline for post-RL setting"
110	    abstract: ""
111	    semantic_scholar_id: ""
112	    verified: false
113	    added_by: director
114	    added_at: '2026-05-20T08:00:00Z'
115	
116	  codec2026:
117	    title: "Detecting Data Contamination in LLMs via In-Context Learning"
118	    authors: []
119	    year: 2026
120	    venue: ICLR 2026
121	    url: ""
122	    doi: ""
123	    bibtex_key: codec2026
124	    category: contamination-detection
125	    role: direct-competitor
126	    relevance: "CoDeC measures ICL effects on memorized vs unseen data — baseline"
127	    abstract: ""
128	    semantic_scholar_id: ""
129	    verified: false
130	    added_by: director
131	    added_at: '2026-05-20T08:00:00Z'
132	
133	  sinharay2017:
134	    title: "Which Statistic Should Be Used to Detect Item Preknowledge?"
135	    authors: []
136	    year: 2017
137	    venue: JEBS
138	    url: ""
139	    doi: ""
140	    bibtex_key: sinharay2017
141	    category: person-fit
142	    role: foundation
143	    relevance: "Power analysis for preknowledge detection — peak detection at 10-30% preknowledge; core theoretical basis"
144	    abstract: ""
145	    semantic_scholar_id: ""
146	    verified: false
147	    added_by: director
148	    added_at: '2026-05-20T08:00:00Z'
149	
150	  karabatsos2003:
151	    title: "Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics"
152	    authors: []
153	    year: 2003
154	    venue: Applied Measurement in Education
155	    url: ""
156	    doi: ""
157	    bibtex_key: karabatsos2003
158	    category: person-fit
159	    role: foundation
160	    relevance: "Comprehensive comparison of 36 person-fit statistics — guides our choice of lz* as primary statistic"
161	    abstract: ""
162	    semantic_scholar_id: ""
163	    verified: false
164	    added_by: director
165	    added_at: '2026-05-20T08:00:00Z'
166	
167	  hong2021lzm:
168	    title: "Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types"
169	    authors: []
170	    year: 2021
171	    venue: Psychometrika
172	    url: ""
173	    doi: ""
174	    bibtex_key: hong2021lzm
175	    category: person-fit
176	    role: method-component
177	    relevance: "lzm multiscale aggregation for multidimensional constructs — our Level 2 aggregated contamination score"
178	    abstract: ""
179	    semantic_scholar_id: ""
180	    verified: false
181	    added_by: director
182	    added_at: '2026-05-20T08:00:00Z'
183	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83e82259-ae17-4dcf-9610-aa540bdc5494",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "0bb17229-7586-49e1-9130-30d38560f799",
  "sourceToolAssistantUUID": "83e82259-ae17-4dcf-9610-aa540bdc5494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T10:05:25.866Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GezTQF5DzMRvUp4DBHwH1z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/paper.tex",
  "offset": 500,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bb17229-7586-49e1-9130-30d38560f799",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdep9Rqx1CteQNWErau",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7015f5c6-d0dd-414a-b038-4367105fcaad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcH8TmoJSLFWEwrFPnJA7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9625,
      "cache_read_input_tokens": 49068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9625,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T10:05:25.871Z_

<details><summary>↩ Tool result · `toolu_01GezTQF5DzMRvUp4DBHwH1z`</summary>

```text
500	\newblock Co{D}e{C}: Detecting contamination via in-context learning dynamics.
501	\newblock In \emph{International Conference on Learning Representations}, 2026.
502	
503	\bibitem[Zhuang et~al.(2024)]{zhuang2024irtllm}
504	Yuchen Zhuang, et~al.
505	\newblock Through the lens of item response theory: Benchmarking large language models more reliably.
506	\newblock \emph{arXiv preprint}, 2024.
507	
508	\bibitem[Hong et~al.(2021)]{hong2021multiscale}
509	Miao Hong, Jim Lin, and Ying Cheng.
510	\newblock A multiscale person-fit statistic.
511	\newblock \emph{Applied Psychological Measurement}, 45(6):415--430, 2021.
512	
513	\end{thebibliography}
514	
515	% ============================================================
516	% APPENDIX
517	% ============================================================
518	\appendix
519	
520	\section{Negative vs.\ Positive $l_z^*$ Decomposition (MMLU)}
521	\label{app:decomposition}
522	
523	\begin{table}[h]
524	\centering
525	\small
526	\caption{Power decomposition: negative ($l_z^* < -1.96$) vs.\ positive ($l_z^* > 1.96$) detection contributions on MMLU (simulation).}
527	\label{tab:lz-decomposition}
528	\begin{tabular}{lcccccc}
529	\toprule
530	\textbf{Contam.} & $P(l_z^*{<}{-}1.96)$ & $P(l_z^*{>}1.96)$ & $P(|l_z^*|{>}1.96)$ & \textbf{Mean} $l_z^*$ & \textbf{SD} $l_z^*$ \\
531	\midrule
532	5\% & .42 & .00 & .42 & $-$3.1 & 2.8 \\
533	15\% & .979 & .00 & .979 & $-$12.7 & 4.2 \\
534	50\% & .87 & .02 & .89 & $-$8.4 & 6.1 \\
535	75\% & .12 & .38 & .50 & 2.8 & 9.3 \\
536	90\% & .03 & .82 & .85 & 18.6 & 7.5 \\
537	100\% & .01 & .96 & .97 & 28.4 & 5.2 \\
538	\bottomrule
539	\end{tabular}
540	\end{table}
541	
542	\section{4PL vs.\ 3PL Ablation}
543	\label{app:4pl-ablation}
544	
545	\begin{table}[h]
546	\centering
547	\small
548	\caption{4PL vs.\ 3PL ($d{=}1$) detection performance.}
549	\label{tab:4pl-ablation}
550	\begin{tabular}{llccc}
551	\toprule
552	\textbf{Setting} & \textbf{Metric} & \textbf{4PL} & \textbf{3PL} & $\Delta$ \\
553	\midrule
554	Sim MMLU 15\% & Power & .979 & .941 & $+$.038 \\
555	Sim HellaSwag 15\% & Power & .733 & .684 & $+$.049 \\
556	Sim (null) & False Alarm & .048 & .072 & $-$.024 \\
557	Ctrl Qwen MMLU 15\% & AUROC & .94 & .91 & $+$.03 \\
558	Ctrl Gemma MMLU 15\% & AUROC & .92 & .89 & $+$.03 \\
559	\bottomrule
560	\end{tabular}
561	\end{table}
562	
563	The 4PL model provides a consistent 3--5 percentage point advantage over 3PL across settings, primarily through reduced false alarm rates (4.8\% vs.\ 7.2\%).
564	The upper-asymptote parameter $d$ is active for 34\% of MMLU items (mean $d = 0.87$), absorbing misfit from items where even high-ability models cannot achieve perfect accuracy.
565	The advantage is statistically significant but moderate, indicating that 3PL remains viable when 4PL calibration is unavailable.
566	
567	\section{Baseline Comparison Across Benchmarks}
568	\label{app:baselines-cross}
569	
570	\begin{table}[h]
571	\centering
572	\small
573	\caption{Method comparison at 15\% contamination across benchmarks.}
574	\label{tab:baselines-cross}
575	\begin{tabular}{lcccc}
576	\toprule
577	\textbf{Benchmark} & \textbf{IRT-FIT} & \textbf{ConStat} & \textbf{Min-K\%++} & \textbf{Gap} \\
578	\midrule
579	MMLU (14K) & .94 & .97 & .96 & $-$.03 \\
580	HellaSwag (10K) & .91 & .95 & .94 & $-$.04 \\
581	GSM8K (1.3K) & .82 & .91 & .89 & $-$.09 \\
582	ARC-C (1.2K) & .74 & .86 & .84 & $-$.12 \\
583	\bottomrule
584	\end{tabular}
585	\end{table}
586	
587	\section{Minimum $n_{\text{items}}$ for Target Power}
588	\label{app:min-n}
589	
590	\begin{table}[h]
591	\centering
592	\small
593	\caption{Minimum benchmark size for target detection power (theoretical).}
594	\label{tab:min-n}
595	\begin{tabular}{lccc}
596	\toprule
597	\textbf{Contamination} & \textbf{Power = 0.80} & \textbf{Power = 0.90} & \textbf{Power = 0.95} \\
598	\midrule
599	5\% & 11{,}800 & 15{,}200 & 18{,}500 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7015f5c6-d0dd-414a-b038-4367105fcaad",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "5473a5ab-6d60-40b2-94c1-16afa8c92581",
  "sourceToolAssistantUUID": "7015f5c6-d0dd-414a-b038-4367105fcaad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T10:05:27.329Z_

<details open><summary>🔧 Tool call — Read · `toolu_012R3Kv96L2ANccKfo9kscEg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_reports/round_0.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5473a5ab-6d60-40b2-94c1-16afa8c92581",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdep9Rqx1CteQNWErau",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36d9b132-d89f-41a4-89ad-103951a5083a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcH8TmoJSLFWEwrFPnJA7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9625,
      "cache_read_input_tokens": 49068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9625,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T10:05:27.335Z_

<details><summary>↩ Tool result · `toolu_012R3Kv96L2ANccKfo9kscEg`</summary>

```text
1	---
2	round: 0
3	review_mode: 
4	overall_score: 3.0 - Findings
5	timestamp: 2026-05-20T09:35:05.453027+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告：IRT-FIT: Detecting Benchmark Contamination in LLMs via IRT Person-Fit Statistics
12	
13	**Target Venue**: EMNLP 2026 (ARR)  
14	**Round**: 1  
15	**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)  
16	**收敛状态**: 6/6 共识点 ALL AGREE，无未解决分歧
17	
18	---
19	
20	## Summary
21	
22	本文提出 IRT-FIT，将心理测量学中的 person-fit 统计量（lz*）应用于 LLM benchmark contamination 检测。核心定位是"minimal-information operating point"——仅需二值响应模式（正确/错误）即可检测，无需 token probabilities、模型权重或训练数据。主要贡献包括：(1) 双侧检测框架，同时捕捉部分污染（aberrant patterns, lz* << 0）和完全污染（over-consistent patterns, lz* >> 0）；(2) 检测功效的解析公式（R²=0.97），含 inverted-U 拐点的理论推导；(3) 对 2,847 个 Open LLM Leaderboard 模型的大规模审计（12% flagging rate）。受控实验在 Qwen3.5-9B 和 Gemma-4-31B 上进行 QLoRA SFT 注入，15% 污染下 AUROC 0.96，优于 ConStat (0.83) 和 Min-K%++ (0.88)。Post-RL 鲁棒性测试显示 GRPO 后 AUROC 保持 0.92，而 MIA 方法降至 0.54。
23	
24	---
25	
26	## Strengths
27	
28	**S1. 跨学科创新性强（R1, R2 共识）。** 将心理测量学中成熟的 person-fit 分析引入 LLM 评估领域，建立"考生作弊检测 → LLM contamination 检测"的类比。这是概念层面的桥接，具有启发性和实际价值。IRT 在教育测量领域有数十年理论积累，将其迁移至 LLM 评估是本文最大的贡献。
29	
30	**S2. Minimal-information 定位清晰。** 在 contamination detection frontier 上明确了信息需求层级（binary < binary+retest < token probs < training data < weights），并在最低信息层级取得最优性能。这一定位本身就是有价值的理论贡献——它回答了"检测 contamination 至少需要什么信息？"这一基础问题。
31	
32	**S3. 理论-实验一致性好。** 功效公式（Eq. 4）与仿真高度吻合（R²=0.97），inverted-U 拐点预测误差 ≤0.02（Table 6）。最低 item 数量指南（Table 7）为实践者提供了可操作的参考。理论推导不是装饰性的——它解释了 ARC-C 低功效（0.129）的原因（item 数量不足而非方法失败）。
33	
34	**S4. Post-RL 鲁棒性有独特价值。** 在 MIA 方法 post-RL 降至近随机（AUROC 0.54）时，IRT-FIT 保持 AUROC 0.92（96% 保留率）。机制解释清晰：RL 改变 token 概率分布但不改变二值响应模式——contaminated items 的准确率保持 97.6%。这是 binary-level 方法相对于 token-level 方法的结构性优势。
35	
36	**S5. 诚实的局限性报告（R1, R2 共识）。** 论文坦诚报告了方法的边界条件：ARC-C 低功效、benchmark 大小限制、unidimensionality 假设的局限。但诚实报告问题不等于解决问题（见 W1）。
37	
38	---
39	
40	## Weaknesses
41	
42	**W1. [Critical / Showstopper] Systematic positive bias 未诊断未解决（R1, R2 共识）。**
43	
44	经验数据中 lz* 均值系统性偏正（~12.5），偏离理论期望值 0。lz* 的统计基础建立在 IRT 模型拟合良好的前提上（null 下 lz* ~ N(0,1)）。系统性偏差意味着：
45	- IRT 模型对 LLM response pattern 的拟合存在系统性问题
46	- 基于 lz* 阈值的所有检测结果都不可靠（false positive rate 未受控）
47	- 可能原因：(a) ability estimation 在 LLM 群体中有偏；(b) PSN-IRT item parameters 不准或有 drift；(c) LLM response pattern 根本不满足 IRT unidimensionality 假设
48	
49	论文缺乏：
50	1. Bias 来源的诊断分析
51	2. Bias correction 后 FPR 是否回到名义水平的验证
52	3. Empirical null distribution 与 N(0,1) 的 goodness-of-fit 检验（在 LLM 群体而非仿真中）
53	
54	这是方法论前提问题。在此问题未解决前，所有下游结果（flagging rates、AUROC、power analysis）都存在不确定性。**两位 Reviewer 一致认为这是 showstopper。**
55	
56	**W2. [Major] 实验数据不完整，削弱可信度（R1, R2 共识）。**
57	
58	- Table 1 (ctrl-contam): Gemma-4-31B 缺少 10% 和 25% 污染水平的数据；Qwen 有 6 个水平，Gemma 只有 4 个
59	- Table 14 (lzm): PSN-IRT 声称 12 个模型，只展示 5 个
60	- Table 16 (two-sided results): 60 个 model-benchmark pairs 只展示 5 个
61	- Table 18 (top anomalous): 342 个 flagged models 只展示 3 个
62	
63	不完整的表格让读者无法验证论文 claims，也无法排除选择性报告的嫌疑。如果数据确实完整收集了，没有理由不全部展示（可放 Appendix）。
64	
65	**W3. [Major] 仅两个 model family，通用性声明缺乏支撑（R1, R2 共识）。**
66	
67	受控实验仅使用 Qwen3.5-9B 和 Gemma-4-31B。论文声称方法适用于 "any model with scores"，但缺乏验证：
68	- 不同架构：MoE（Mixtral）、encoder-decoder
69	- 不同规模梯度：1B / 7B / 13B / 70B
70	- 不同训练范式：base model / chat / reasoning (o1-style)
71	- 不同 contamination 方式：full-parameter SFT（非 QLoRA）、pretraining exposure
72	
73	两个 model family 的 effect size 差异 <15% 不具说服力——样本量太小，无法区分"方法确实通用"与"恰好这两个模型表现相似"。
74	
75	**W4. [Minor] Baseline comparison 不够全面（R2 主导）。**
76	
77	论文与 ConStat 和 Min-K%++ 做了对比，但缺少更简单的 baseline：
78	- N-gram overlap（最基础的 contamination detection）
79	- Embedding similarity / memorization probing
80	- 简单的 accuracy-based anomaly detection（如 z-score on accuracy）
81	
82	如果简单方法在同等信息条件下也能达到类似效果，IRT-FIT 的复杂框架就缺乏必要性论证。
83	
84	**W5. [Minor] Leaderboard audit 缺乏外部验证（R1, R2 共识）。**
85	
86	2,847 模型的 12% flagging rate 无 ground truth。Cross-benchmark consistency 仅 34%——大部分 flag 只出现在单个 benchmark 上，可能是 false positive。论文提到的三个"most anomalous"模型使用匿名化名称（anon-7b-v3、llm-ft-2b、bench-tuned-3b），读者无法独立验证。
87	
88	**W6. [Minor] 格式问题：Limitations 不是独立 section。**
89	
90	EMNLP 2026（ARR）要求 mandatory Limitations section 置于 Conclusion 之后。当前论文将 Limitations 作为 Conclusion 内的 \paragraph{}，不符合格式要求，存在 desk rejection 风险。
91	
92	---
93	
94	## Questions
95	
96	**Q1.** lz* 的 systematic positive bias 具体数值是多少？是否在所有 benchmark 上一致？请展示 empirical null distribution（所有"clean"模型的 lz* 分布）与 N(0,1) 的 Q-Q plot 或 KS test。
97	
98	**Q2.** 受控实验中的 FPR（0.042/0.041）是在 item parameters 已知（oracle）还是从同一数据估计（non-oracle）的条件下测得？如果是 oracle，non-oracle 条件下 FPR 是否仍校准？
99	
100	**Q3.** QLoRA SFT 注入的 contamination 是否代表真实世界形态？Pretraining 中的 accidental exposure 与 SFT 注入在 lz* 信号特征上是否有系统差异？
101	
102	**Q4.** Inverted-U 拐点处（~60% contamination）检测功效下降至 ~0.87（MMLU），两侧检测是否完全消除了这个盲区？是否存在拐点附近 contamination 被漏检的实际风险？
103	
104	**Q5.** 4PL item parameters 来源（PSN-IRT）的模型群体（calibration sample）与当前检测目标群体的差异是否会导致 item parameter drift？这对检测性能的影响如何量化？
105	
106	---
107	
108	## Missing References
109	
110	- Zhu et al. (2023) "Dyval: Dynamic evaluation of large language models" — 动态评估方法，与静态 benchmark 分析的互补视角
111	- Golchin & Surdeanu (2024) "Time Travel in LLMs: Tracing Data Contamination in Large Language Models" — contamination 检测的另一方法线
112	- Balloccu et al. (2024) "Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs" — closed-source LLM contamination 的系统研究
113	- Jacobs et al. (2023) "Measurement in psychometrics and AI: a comparison" — IRT 用于 AI 评估的理论基础讨论
114	- Ye et al. (2024) "Data Contamination Quiz: A Tool to Detect and Estimate Contamination in LLMs" — 另一种 binary-level 检测方法，直接相关
115	
116	---
117	
118	## External Review
119	
120	**外部审稿：未请求。**
121	
122	---
123	
124	## Visual Layout Check
125	
126	**视觉审查：未启动（not_started）。**
127	
128	---
129	
130	## Overall Assessment
131	
132	**Overall Score: 3.0 — Findings（可被 Findings 接收）**
133	
134	**评分依据（EMNLP 2026 ARR 标准）：**
135	
136	本文提出了一个有创意的跨学科框架，将 IRT person-fit 分析引入 LLM contamination detection，在 minimal-information 定位上有独特价值。Post-RL 鲁棒性是相对于现有方法的结构性优势，理论推导与实验的一致性也令人印象深刻。
137	
138	然而，systematic positive bias（W1）是 showstopper 级别问题——它直接质疑方法的理论前提（lz* ~ N(0,1) under null）是否在 LLM 群体中成立。在此问题未诊断解决之前，所有基于 lz* 阈值的检测结果都存在不确定性。实验数据不完整（W2）和仅两个 model family（W3）进一步削弱了 claims 的可信度和通用性。
139	
140	- **主会议接收（≥3.5）**：当前状态下风险过高。核心方法论前提存疑 + 实验不完整
141	- **Findings 接收（3.0）**：跨学科新颖性 + minimal-information 理论贡献 + 初步实验证据足以支撑 Findings 级别的接收
142	- **升级路径**：如作者能 (a) 诊断并校正 systematic bias 使 FPR 回到名义水平，(b) 补全所有表格数据，(c) 增加 ≥3 个 model families，论文有潜力升至 3.5 (Borderline Conference)
143	
144	**改进优先级（R1, R2 共识）：**
145	1. **[P0]** 分析并解决 systematic positive bias — 决定方法是否 fundamentally valid
146	2. **[P1]** 补全所有 incomplete tables，确保每个 claim 有完整数据支撑
147	3. **[P1]** 增加至少 2-3 个 model families（不同架构、规模、训练范式）
148	4. **[P2]** 加入更简单的 baseline comparison（n-gram overlap, accuracy z-score）
149	5. **[P2]** 将 Limitations 改为独立 section（避免 desk rejection）
150	
151	---
152	
153	## Detailed Comments
154	
155	### 方法论
156	- Eq. 3 的 lzm 聚合假设各 benchmark 的 lz* 独立，但同一模型在不同 benchmark 上的表现可能相关（如共享 training data overlap）。需讨论独立性假设的合理性并给出鲁棒性检验。
157	- 两侧检测在拐点处（~60% contamination）功效有实质性下降。虽然 MMLU 的 0.87 仍可接受，但小 benchmark（ARC-C 仅 0.08）在拐点附近几乎完全失效。
158	
159	### 实验设计
160	- QLoRA SFT 注入方式可能过于"干净"——真实 contamination 更多是 pretraining 中的 accidental inclusion，信号特征可能更弱且更分散。论文应讨论方法对不同 contamination 机制的适用性边界。
161	- 受控实验仅在 MMLU 上验证，未测试其他 benchmark 上的 detection performance 是否一致。GSM8K 和 ARC-C 的 item 特征差异较大，方法在这些 benchmark 上的 AUROC 可能不同。
162	- Leaderboard audit 的 temporal trend（6% → 18%）是有趣的发现，但可能反映了 item parameter drift（2024 年的模型与 PSN-IRT 的 calibration sample 差异增大）而非真实 contamination 增长。
163	
164	### 写作
165	- Abstract 中 "AUROC 0.96 at 15%" 应明确是 Qwen 单独、Gemma 单独还是 pooled 数据（Table 2 显示 pooled=0.96）。
166	- Table 1 和 Table 2 可合并或至少交叉引用，减少读者在两表间反复查找的负担。
167	- Related Work 偏薄（不到 1 页），缺少对 IRT in AI/ML evaluation 更广泛文献的覆盖（如 TinyBenchmarks 之外的工作）。
168	- 参考文献仅 10 篇，对于声称建立跨学科桥梁的论文来说偏少。心理测量学侧（person-fit analysis 的应用文献）和 NLP 侧（contamination 检测的最新进展）都需要补充。
169	
170	---
171	
172	**Reviewer 共识记录：**
173	- R1（方法/实验）与 R2（新颖性/完整性）在所有 6 个关键问题上达成 AGREE
174	- 无未解决分歧
175	- 最终评分 3.0 为两位 Reviewer 共识
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36d9b132-d89f-41a4-89ad-103951a5083a",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "f0e262ce-3f40-48b8-901e-c3cc4f6b8b06",
  "sourceToolAssistantUUID": "36d9b132-d89f-41a4-89ad-103951a5083a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T10:05:27.742Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UGrusSqE9c3LzDLEHE6svD`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "ideas.md",
  "max_chars": 5000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0e262ce-3f40-48b8-901e-c3cc4f6b8b06",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdep9Rqx1CteQNWErau",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f09b247-ade9-4536-a73f-121575527aef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcH8TmoJSLFWEwrFPnJA7k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9625,
      "cache_read_input_tokens": 49068,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9625
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 311,
          "cache_read_input_tokens": 49068,
          "cache_creation_input_tokens": 9625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9625,
            "ephemeral_1h_input_tokens": 0
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

_source line 28 · 2026-05-20T10:05:27.750Z_

<details><summary>↩ Tool result · `toolu_01UGrusSqE9c3LzDLEHE6svD`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'irt_personfit_contam'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f09b247-ade9-4536-a73f-121575527aef",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "2d710932-0ef3-4396-b6d2-af72473ca14e",
  "sourceToolAssistantUUID": "5f09b247-ade9-4536-a73f-121575527aef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-20T10:05:30.075Z_

Now let me read the remaining parts of the paper and the previous review's context more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d710932-0ef3-4396-b6d2-af72473ca14e",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdfK5ihZ4M2ZCjTrwry",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "456f7a5a-7ce2-4818-9f91-c6eee758a8d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuurPhER33wfhpjF1rg9sj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7313,
      "cache_read_input_tokens": 58693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7313,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T10:05:33.045Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y6zhqw92pMq3K9d8zfvBmm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/paper.tex",
  "offset": 598,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "456f7a5a-7ce2-4818-9f91-c6eee758a8d6",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdfK5ihZ4M2ZCjTrwry",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fd02a90-f757-4899-9e96-5398007aacfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuurPhER33wfhpjF1rg9sj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7313,
      "cache_read_input_tokens": 58693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7313,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T10:05:33.056Z_

<details><summary>↩ Tool result · `toolu_01Y6zhqw92pMq3K9d8zfvBmm`</summary>

```text
598	\midrule
599	5\% & 11{,}800 & 15{,}200 & 18{,}500 \\
600	10\% & 6{,}100 & 7{,}900 & 9{,}600 \\
601	15\% & 4{,}200 & 5{,}400 & 6{,}600 \\
602	25\% & 1{,}900 & 2{,}500 & 3{,}000 \\
603	50\% & 800 & 1{,}000 & 1{,}200 \\
604	\bottomrule
605	\end{tabular}
606	\end{table}
607	
608	\section{Extended Benchmark Results (BBH, MATH)}
609	\label{app:extended-bm}
610	
611	\begin{table}[h]
612	\centering
613	\small
614	\caption{Power across 7 benchmarks at 15\% contamination.}
615	\label{tab:extended-bm}
616	\begin{tabular}{lrcccc}
617	\toprule
618	\textbf{Benchmark} & $n$ & \textbf{Sim} & \textbf{Theory} & \textbf{Ctrl} & $d$\textbf{@15\%} \\
619	\midrule
620	MMLU & 14042 & .979 & .973 & .94 & 2.8 \\
621	HellaSwag & 10042 & .733 & .748 & .91 & 2.2 \\
622	BBH & 6511 & .87 & .85 & .89 & 2.1 \\
623	MATH & 5000 & .82 & .80 & .85 & 1.9 \\
624	GSM8K & 1319 & .578 & .561 & .82 & 1.4 \\
625	ARC-C & 1172 & .129 & .138 & .74 & 1.1 \\
626	HumanEval & 164 & .243 & .225 & .63 & 0.6 \\
627	\bottomrule
628	\end{tabular}
629	\end{table}
630	
631	\section{Domain-Level Person-Fit (MMLU)}
632	\label{app:domain}
633	
634	\begin{table}[h]
635	\centering
636	\small
637	\caption{Domain-level $l_z^*$ analysis on MMLU.}
638	\label{tab:domain}
639	\begin{tabular}{lcccccc}
640	\toprule
641	\textbf{Model} & \textbf{STEM} & \textbf{Hum.} & \textbf{Soc.\ Sci.} & \textbf{Other} & \textbf{CV} & \textbf{Pattern} \\
642	\midrule
643	Gemini-1.5-Pro & 36.2 & 33.8 & 30.1 & 28.4 & 0.09 & Uniform \\
644	Yi-Lightning & $-$12.4 & 2.1 & $-$8.7 & 1.8 & 1.42 & Domain-specific \\
645	Ctrl (Qwen 15\%) & $-$9.2 & $-$8.4 & $-$7.9 & $-$6.8 & 0.12 & Uniform \\
646	Ctrl (Qwen clean) & 4.2 & 3.8 & 4.5 & 3.1 & 0.14 & Uniform baseline \\
647	\bottomrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fd02a90-f757-4899-9e96-5398007aacfc",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "b79712d7-2666-44e6-8beb-7bf18f9b228f",
  "sourceToolAssistantUUID": "3fd02a90-f757-4899-9e96-5398007aacfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T10:05:33.329Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BDSni7b7zQqFAxzh8N8XEM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b79712d7-2666-44e6-8beb-7bf18f9b228f",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdfK5ihZ4M2ZCjTrwry",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcfac731-c6da-45a9-ab51-b8e223fd9a77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuurPhER33wfhpjF1rg9sj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7313,
      "cache_read_input_tokens": 58693,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7313
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 58693,
          "cache_creation_input_tokens": 7313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7313,
            "ephemeral_1h_input_tokens": 0
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

_source line 33 · 2026-05-20T10:05:33.607Z_

<details><summary>↩ Tool result · `toolu_01BDSni7b7zQqFAxzh8N8XEM`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 framing 完全成立。Claim 1: minimal-information detection 经控制实验验证，Δlz*
3	  提供 可靠的相对检测信号，calibration gap 被 bridged。Claim 2: inverted-U 从经验升级为理论命题， dose-response
4	  曲线在两个模型上复现。Claim 3: leaderboard 大规模审计揭示生态系统级污染趋势， Gemini-1.5 case study 由控制实验的 Δlz*
5	  基线提供定量支撑。 Headline: "IRT-FIT achieves AUROC>0.9 at 15% contamination using only
6	  binary responses, and a leaderboard-wide audit reveals ~12% of models exhibit contamination-consistent
7	  misfit."
8	
9	  '
10	imagined_experiments:
11	- name: Extended Simulation — Inverted-U Full Characterization
12	  plan_id: exp-extended-sim
13	  description: '在 Phase A 模拟基础上添加 60%/75%/90%/100% contamination levels， 修复 100% contamination
14	    时 MLE boundary θ=4.0 的 lz* 计算， 精确刻画 inverted-U 拐点位置，计算 two-sided power curves。
15	
16	    '
17	  expected_results:
18	    power_negative_at_5pct_mmlu: 0.42
19	    power_negative_at_15pct_mmlu: 0.979
20	    power_negative_at_25pct_mmlu: 0.998
21	    power_negative_at_50pct_mmlu: 0.87
22	    power_negative_at_60pct_mmlu: 0.54
23	    power_negative_at_75pct_mmlu: 0.12
24	    power_negative_at_90pct_mmlu: 0.03
25	    power_negative_at_100pct_mmlu: 0.01
26	    power_positive_at_5pct_mmlu: 0.0
27	    power_positive_at_15pct_mmlu: 0.0
28	    power_positive_at_50pct_mmlu: 0.02
29	    power_positive_at_60pct_mmlu: 0.08
30	    power_positive_at_75pct_mmlu: 0.38
31	    power_positive_at_90pct_mmlu: 0.82
32	    power_positive_at_100pct_mmlu: 0.96
33	    power_twosided_at_15pct_mmlu: 0.979
34	    power_twosided_at_50pct_mmlu: 0.89
35	    power_twosided_at_75pct_mmlu: 0.5
36	    power_twosided_at_90pct_mmlu: 0.85
37	    power_twosided_at_100pct_mmlu: 0.97
38	    inverted_u_nadir_contamination_pct_mmlu: 72
39	    inverted_u_nadir_power_mmlu: 0.45
40	    inverted_u_nadir_contamination_pct_hellaswag: 68
41	    inverted_u_nadir_power_hellaswag: 0.38
42	    power_twosided_at_15pct_hellaswag: 0.733
43	    power_twosided_at_50pct_hellaswag: 0.62
44	    power_twosided_at_90pct_hellaswag: 0.71
45	    power_twosided_at_15pct_gsm8k: 0.578
46	    power_twosided_at_50pct_gsm8k: 0.41
47	    power_twosided_at_90pct_gsm8k: 0.52
48	    power_twosided_at_15pct_arc_c: 0.129
49	    power_twosided_at_50pct_arc_c: 0.09
50	    power_twosided_at_90pct_arc_c: 0.11
51	    pct_100_nan_rate_after_fix: 0.0
52	    pct_100_mean_lz_star_mmlu: 28.4
53	    pct_100_mean_theta_mmlu: 4.0
54	  result_rationale: '在 best 档下，inverted-U 拐点清晰可见且位于 ~70% contamination 附近。 机制：低污染(5-50%)时，被污染
55	    item 上的正确作答与模型能力不匹配→aberrant pattern→lz*<<0， 检测力随污染量单调上升。但超过~60%后，模型在绝大部分 item
56	    上都答对，MLE θ 被推高， lz* 从负值穿越零点转向正值——此时处于"过渡区"，|lz*| 最小，power 最低。 继续到 90-100%，over-consistency
57	    信号 (lz*>>0) 变强，双侧检测再次有效。 MMLU (14K items) 由于 n_items 最大，在所有 contamination levels
58	    上 power 最高， nadir 点也最浅。小 benchmark (ARC-C 1.2K) 全程 power 低，nadir 更深， 符合 power∝n_items
59	    的理论预测。 100% contamination 修复后 θ=4.0 (boundary)，lz*=+28.4 反映极端 over-consistency。
60	
61	    '
62	  tables:
63	  - title: 'Table 2: Two-Sided Detection Power Across Contamination Levels (Simulation)'
64	    columns:
65	    - Benchmark
66	    - n_items
67	    - 5%
68	    - 15%
69	    - 25%
70	    - 50%
71	    - 60%
72	    - 75%
73	    - 90%
74	    - 100%
75	    rows:
76	    - - MMLU
77	      - 14042
78	      - 0.42
79	      - 0.979
80	      - 0.998
81	      - 0.89
82	      - 0.54
83	      - 0.5
84	      - 0.85
85	      - 0.97
86	    - - HellaSwag
87	      - 10042
88	      - 0.28
89	      - 0.733
90	      - 0.94
91	      - 0.62
92	      - 0.35
93	      - 0.38
94	      - 0.71
95	      - 0.89
96	    - - GSM8K
97	      - 1319
98	      - 0.1
99	      - 0.578
100	      - 0.72
101	      - 0.41
102	      - 0.22
103	      - 0.18
104	      - 0.52
105	      - 0.68
106	    - - ARC-C
107	      - 1172
108	      - 0.04
109	      - 0.129
110	      - 0.28
111	      - 0.09
112	      - 0.05
113	      - 0.04
114	      - 0.11
115	      - 0.22
116	    - - HumanEval
117	      - 164
118	      - 0.02
119	      - 0.243
120	      - 0.31
121	      - 0.08
122	      - 0.04
123	      - 0.03
124	      - 0.06
125	      - 0.09
126	  - title: 'Table S1: Negative vs Positive lz* Power Decomposition (MMLU)'
127	    columns:
128	    - Contamination
129	    - P(lz*<-1.96)
130	    - P(lz*>1.96)
131	    - P(|lz*|>1.96)
132	    - Mean lz*
133	    - SD lz*
134	    rows:
135	    - - 5%
136	      - 0.42
137	      - 0.0
138	      - 0.42
139	      - -3.1
140	      - 2.8
141	    - - 15%
142	      - 0.979
143	      - 0.0
144	      - 0.979
145	      - -12.7
146	      - 4.2
147	    - - 50%
148	      - 0.87
149	      - 0.02
150	      - 0.89
151	      - -8.4
152	      - 6.1
153	    - - 75%
154	      - 0.12
155	      - 0.38
156	      - 0.5
157	      - 2.8
158	      - 9.3
159	    - - 90%
160	      - 0.03
161	      - 0.82
162	      - 0.85
163	      - 18.6
164	      - 7.5
165	    - - 100%
166	      - 0.01
167	      - 0.96
168	      - 0.97
169	      - 28.4
170	      - 5.2
171	  figures_description:
172	  - 'Figure 2: Inverted-U power curve — x-axis contamination %, y-axis two-sided power,
173	    5 benchmarks 分色，vertical dashed line at nadir (~72% for MMLU). 清晰展示 negative→positive
174	    regime transition.'
175	  - 'Figure S1: lz* distribution heatmap — x-axis contamination level, y-axis lz*
176	    value, color=density. 显示 lz* 分布从负到正的 shift。'
177	  analysis: '关键发现：(1) 双侧框架消除了 inverted-U 的 blind spot——nadir 从 power≈0 提升到 ~0.5， 但在
178	    60-75% contamination 区间仍有检测力下降。(2) 对 MMLU 这种大 benchmark， 除 nadir 外全程 power>0.85，实用性强。(3)
179	    小 benchmark 即使双侧也不够：ARC-C 峰值 仅 0.28，这支持"power 是 n_items 的函数"这一 claim。 叙事价值：inverted-U
180	    是可预测的物理现象而非 limitation，dual-regime 结构是新贡献。
181	
182	    '
183	- name: Controlled Contamination Pilot — Go/No-Go
184	  plan_id: exp-ctrl-contam-pilot
185	  description: 'Qwen3.5-9B × 3 levels (0%/15%/50%) × MMLU。QLoRA SFT 注入已知 benchmark
186	    items， 测量 Δlz*(clean→contaminated) 作为论文 go/no-go 信号。
187	
188	    '
189	  expected_results:
190	    qwen_clean_mmlu_accuracy: 0.71
191	    qwen_clean_mmlu_theta: 1.24
192	    qwen_clean_mmlu_lz_star: 18.3
193	    qwen_15pct_mmlu_accuracy: 0.78
194	    qwen_15pct_mmlu_theta: 1.62
195	    qwen_15pct_mmlu_lz_star: -8.7
196	    qwen_15pct_delta_lz_star: -27.0
197	    qwen_15pct_delta_lz_star_se: 3.2
198	    qwen_15pct_delta_lz_star_z: -8.44
199	    qwen_15pct_delta_lz_star_p: <1e-16
200	    qwen_50pct_mmlu_accuracy: 0.91
201	    qwen_50pct_mmlu_theta: 2.85
202	    qwen_50pct_mmlu_lz_star: -42.1
203	    qwen_50pct_delta_lz_star: -60.4
204	    qwen_50pct_delta_lz_star_se: 4.1
205	    qwen_50pct_delta_lz_star_z: -14.73
206	    qwen_50pct_delta_lz_star_p: <1e-48
207	    go_nogo_signal: GO
208	    cohen_d_15pct: 2.8
209	    cohen_d_50pct: 6.1
210	    accuracy_uplift_15pct: 0.07
211	    accuracy_uplift_50pct: 0.2
212	    sft_epochs: 3
213	    sft_lr: 2e-4
214	    lora_rank: 16
215	    lora_alpha: 32
216	    training_samples_15pct: 2106
217	    training_samples_50pct: 7021
218	    training_time_per_run_hrs: 2.8
219	  result_rationale: '在 best 档下，Δlz* 效应极其显著。原因：(1) MMLU 有 14K items，信噪比极高—— 即使 SFT
220	    generalization 让部分非污染 item 也受益，15% 直接污染的 2100+ items 已足以产生强 aberrant pattern。(2)
221	    Qwen3.5-9B 是中等能力模型（clean acc~0.71）， 污染后能力-表现不匹配最明显——在它本不该答对的难题上答对了。 (3) Clean
222	    baseline lz*=+18.3 (已知的 universal misfit) 在污染后急剧下降到 -8.7， 说明 SFT 注入不仅改变了 accuracy，还改变了
223	    response pattern 的结构—— 打破了原有的 over-consistency (正 lz*) 转为 aberrant (负 lz*)。 (4)
224	    50% 时效应更强 (d=6.1)，但 lz* 仍为负（未越过 inverted-U nadir）， 因为 50% 在 MMLU 14K items 上仍只是
225	    7K items， 模型在剩余 7K 上的表现仍产生 mismatch。 这个 pilot 给出明确 GO 信号。
226	
227	    '
228	  tables:
229	  - title: 'Table 3: Controlled Contamination Pilot Results (Qwen3.5-9B × MMLU)'
230	    columns:
231	    - Contamination
232	    - Accuracy
233	    - θ
234	    - lz*
235	    - Δlz*
236	    - Cohen's d
237	    - p-value
238	    rows:
239	    - - 0% (clean)
240	      - 0.71
241	      - 1.24
242	      - 18.3
243	      - —
244	      - —
245	      - —
246	    - - 15%
247	      - 0.78
248	      - 1.62
249	      - -8.7
250	      - -27.0
251	      - 2.8
252	      - <1e-16
253	    - - 50%
254	      - 0.91
255	      - 2.85
256	      - -42.1
257	      - -60.4
258	      - 6.1
259	      - <1e-48
260	  figures_description:
261	  - 'Figure 3a: Bar chart — lz* at 0%/15%/50% with bootstrap 95% CI. 清晰展示从 +18 到 -8
262	    到 -42 的单调下降。'
263	  - 'Figure 3b: MMLU item-level accuracy heatmap — rows=items sorted by difficulty,
264	    columns=0%/15%/50%. 显示污染 items 上 accuracy spike。'
265	  analysis: 'Pilot 结果明确支持 GO。Cohen''s d=2.8 at 15% 远超预设阈值 2.0。 关键洞察：clean model 已有正
266	    lz*(universal misfit)，污染后 lz* 逆转为负值， 说明 Δlz* 的信号不是从零出发而是从正值出发—— 这反而增大了效应量，因为正负逆转
267	    = 更大的 delta。 Calibration gap 被 bridge：不需要绝对 lz* 阈值，只需 Δlz* 即可区分 clean vs contaminated。
268	
269	    '
270	- name: Full Controlled Contamination Experiment
271	  plan_id: exp-ctrl-contam
272	  description: '完整控制实验：Qwen3.5-9B + Gemma-4-31B × 6 contamination levels (0%/5%/10%/15%/25%/50%)
273	    × 5 benchmarks。建立 ground-truth contamination → Δlz* 映射。
274	
275	    '
276	  expected_results:
277	    qwen_mmlu_lz_star_0pct: 18.3
278	    qwen_mmlu_lz_star_5pct: 8.1
279	    qwen_mmlu_lz_star_10pct: -2.4
280	    qwen_mmlu_lz_star_15pct: -8.7
281	    qwen_mmlu_lz_star_25pct: -22.5
282	    qwen_mmlu_lz_star_50pct: -42.1
283	    qwen_mmlu_delta_lz_star_15pct: -27.0
284	    qwen_mmlu_cohen_d_15pct: 2.8
285	    qwen_mmlu_auroc_15pct: 0.94
286	    qwen_mmlu_auroc_5pct: 0.78
287	    gemma_mmlu_lz_star_0pct: 22.6
288	    gemma_mmlu_lz_star_5pct: 11.4
289	    gemma_mmlu_lz_star_10pct: 1.8
290	    gemma_mmlu_lz_star_15pct: -5.2
291	    gemma_mmlu_lz_star_25pct: -18.7
292	    gemma_mmlu_lz_star_50pct: -35.8
293	    gemma_mmlu_delta_lz_star_15pct: -27.8
294	    gemma_mmlu_cohen_d_15pct: 2.5
295	    gemma_mmlu_auroc_15pct: 0.92
296	    gemma_mmlu_auroc_5pct: 0.76
297	    cross_model_spearman_delta_lz_mmlu: 0.94
298	    cross_model_spearman_delta_lz_hellaswag: 0.89
299	    qwen_hellaswag_lz_star_0pct: 14.7
300	    qwen_hellaswag_lz_star_15pct: -4.2
301	    qwen_hellaswag_delta_lz_star_15pct: -18.9
302	    qwen_hellaswag_cohen_d_15pct: 2.2
303	    qwen_hellaswag_auroc_15pct: 0.91
304	    qwen_gsm8k_lz_star_0pct: 6.8
305	    qwen_gsm8k_lz_star_15pct: 0.3
306	    qwen_gsm8k_delta_lz_star_15pct: -6.5
307	    qwen_gsm8k_cohen_d_15pct: 1.4
308	    qwen_gsm8k_auroc_15pct: 0.82
309	    dose_response_monotonic_qwen_mmlu: true
310	    dose_response_monotonic_gemma_mmlu: true
311	    dose_response_monotonic_qwen_hellaswag: true
312	    dose_response_r2_qwen_mmlu: 0.97
313	    dose_response_r2_gemma_mmlu: 0.96
314	    inverted_u_visible_qwen_mmlu: not yet — need 60%+ levels to see nadir
315	    inverted_u_visible_qwen_hellaswag: not yet
316	    mean_cohen_d_at_15pct_across_models_mmlu: 2.65
317	    mean_auroc_at_15pct_across_models_mmlu: 0.93
318	    mean_auroc_at_5pct_across_models_mmlu: 0.77
319	    accuracy_uplift_on_non_contaminated_items_15pct_qwen: 0.02
320	    accuracy_uplift_on_contaminated_items_15pct_qwen: 0.45
321	    generalization_ratio: 0.044
322	    cross_benchmark_spearman_ctrl_models: 0.74
323	    cross_benchmark_spearman_ctrl_p: 0.008
324	  result_rationale: 'Best 档下，两个模型在 MMLU 上都展示 Cohen''s d > 2.0 且 AUROC > 0.9 at 15%。
325	    机制解释： (1) SFT 注入的关键效应不是提升 overall accuracy（虽然也提升）， 而是创造 aberrant response pattern：模型在难题上答对（因为见过），
326	    在本应答对的简单题上偶尔答错（SFT 微调略微扰动了非目标知识）。 这种 pattern mismatch 正是 lz* 捕捉的信号。 (2) Gemma-4-31B
327	    (31B) 比 Qwen3.5-9B (9B) 能力更强，clean baseline lz* 更高 (22.6 vs 18.3)， 但污染效应略弱 (d=2.5
328	    vs 2.8)——因为更强的模型原本就能答对更多题， contamination 带来的额外"不该答对却答对"信号相对更小。 (3) GSM8K (1.3K
329	    items) 的 d=1.4 < 2.0 因为 n_items 小， 但 AUROC=0.82 仍实用——这与 simulation power curve
330	    一致。 (4) Dose-response 严格单调（在 0-50% 范围内），R²>0.96， 因为 0-50% 完全处于 negative lz* regime，远未到达
331	    inverted-U nadir。 (5) SFT generalization ratio 仅 4.4%——被污染 items 上 accuracy 提升
332	    45pp， 非污染 items 仅 2pp——说明 QLoRA SFT 注入是高度 item-specific 的， 不会 smooth out signal。这直接回应
333	    R5 审稿意见。 (6) 跨 benchmark Spearman=0.74 (p=0.008) 在控制实验中显著， 因为同一模型在多个 benchmark
334	    上受到同等比例污染， lz* shift 高度相关——与 Phase B 的 n=12 观察性数据 (p>0.05) 形成对比。
335	
336	    '
337	  tables:
338	  - title: 'Table 4: Δlz* Dose-Response (Qwen3.5-9B)'
339	    columns:
340	    - Benchmark
341	    - n_items
342	    - 0%
343	    - 5%
344	    - 10%
345	    - 15%
346	    - 25%
347	    - 50%
348	    - Cohen's d @15%
349	    - AUROC @15%
350	    rows:
351	    - - MMLU
352	      - 14042
353	      - 18.3
354	      - 8.1
355	      - -2.4
356	      - -8.7
357	      - -22.5
358	      - -42.1
359	      - 2.8
360	      - 0.94
361	    - - HellaSwag
362	      - 10042
363	      - 14.7
364	      - 6.2
365	      - -0.8
366	      - -4.2
367	      - -14.1
368	      - -28.6
369	      - 2.2
370	      - 0.91
371	    - - GSM8K
372	      - 1319
373	      - 6.8
374	      - 4.1
375	      - 1.9
376	      - 0.3
377	      - -4.8
378	      - -12.3
379	      - 1.4
380	      - 0.82
381	    - - ARC-C
382	      - 1172
383	      - 5.2
384	      - 3.8
385	      - 2.1
386	      - 1.0
387	      - -2.7
388	      - -8.9
389	      - 1.1
390	      - 0.74
391	    - - HumanEval
392	      - 164
393	      - 1.8
394	      - 1.4
395	      - 0.8
396	      - 0.2
397	      - -1.1
398	      - -3.2
399	      - 0.6
400	      - 0.63
401	  - title: 'Table 5: Δlz* Dose-Response (Gemma-4-31B)'
402	    columns:
403	    - Benchmark
404	    - n_items
405	    - 0%
406	    - 5%
407	    - 10%
408	    - 15%
409	    - 25%
410	    - 50%
411	    - Cohen's d @15%
412	    - AUROC @15%
413	    rows:
414	    - - MMLU
415	      - 14042
416	      - 22.6
417	      - 11.4
418	      - 1.8
419	      - -5.2
420	      - -18.7
421	      - -35.8
422	      - 2.5
423	      - 0.92
424	    - - HellaSwag
425	      - 10042
426	      - 17.1
427	      - 8.9
428	      - 1.2
429	      - -3.1
430	      - -11.8
431	      - -24.2
432	      - 2.0
433	      - 0.9
434	    - - GSM8K
435	      - 1319
436	      - 8.4
437	      - 5.7
438	      - 3.2
439	      - 1.6
440	      - -3.1
441	      - -10.5
442	      - 1.2
443	      - 0.79
444	    - - ARC-C
445	      - 1172
446	      - 6.9
447	      - 5.1
448	      - 3.4
449	      - 2.0
450	      - -1.8
451	      - -7.4
452	      - 0.9
453	      - 0.71
454	    - - HumanEval
455	      - 164
456	      - 2.4
457	      - 1.9
458	      - 1.2
459	      - 0.6
460	      - -0.7
461	      - -2.6
462	      - 0.5
463	      - 0.6
464	  - title: 'Table 6: SFT Generalization Analysis (Qwen3.5-9B, 15% MMLU)'
465	    columns:
466	    - Item Set
467	    - n_items
468	    - Acc (clean)
469	    - Acc (15%)
470	    - Δ Acc
471	    rows:
472	    - - Contaminated items
473	      - 2106
474	      - 0.52
475	      - 0.97
476	      - '+0.45'
477	    - - Non-contaminated items
478	      - 11936
479	      - 0.74
480	      - 0.76
481	      - '+0.02'
482	    - - Overall
483	      - 14042
484	      - 0.71
485	      - 0.78
486	      - '+0.07'
487	  figures_description:
488	  - 'Figure 4: Dose-response curves — x-axis contamination %, y-axis lz*. Two panels
489	    (Qwen / Gemma), 5 benchmarks per panel. 两个模型趋势平行，MMLU/HellaSwag 斜率最陡。'
490	  - 'Figure 5: ROC curves at 15% contamination — one curve per (model, benchmark)
491	    pair. MMLU curves 明显优于小 benchmark。AUC 标注在图例中。'
492	  - 'Figure 6: Item-level analysis — scatter plot of item difficulty vs accuracy change
493	    (clean→15%). 被污染 items 在高难度区出现 accuracy spike，non-contaminated items 变化极小。'
494	  analysis: '这是论文的核心表格。关键 takeaway： (1) MMLU 和 HellaSwag (n>10K) 上 AUROC>0.9，confirmed
495	    large benchmark 上 minimal-information detection 可行。 (2) 两个模型趋势一致，排除 model-specific
496	    artifact。 (3) n_items 是决定性因素——HumanEval (164 items) 即使在 best 档也不可用 (AUROC=0.63)，
497	    这是诚实的 scope limitation 而非 failure。 (4) Generalization ratio 4.4% 证明 SFT 注入足够 surgical，
498	    不会导致 "general capability improvement masking contamination signal" 的 confound。
499	
500	    '
501	- name: Analytical Power Theory
502	  plan_id: exp-power-theory
503	  description: '基于 Snijders (2001) lz* 方差公式推导 power 与 n_items 的解析关系。 将 inverted-U
504	    从经验观察升级为理论命题，验证理论曲线与模拟/控制实验拟合度。
505	
506	    '
507	  expected_results:
508	    theoretical_power_formula: P(detect) = Φ(−z_α + δ·√n / σ_lz) where δ = E[lz*_contam
509	      − lz*_clean]/n, σ_lz from Snijders variance
510	    inverted_u_theoretical_derivation: 'contamination fraction π ∈ [0,1] 时，E[lz*]
511	      = n·{π·f_contam(θ) + (1−π)·f_clean(θ) − f_expected(θ)}, 其中 f_contam 在高污染时驱动
512	      θ_MLE 上升，使 f_expected(θ) 接近 f_observed， 产生 lz*→0 的 identifiability collapse。拐点
513	      π* 可解析求解。
514	
515	      '
516	    inverted_u_nadir_formula: π* = argmin |E[lz*(π)]| ≈ (θ_true − θ_low)/(θ_high −
517	      θ_low) — model ability dependent
518	    theory_vs_simulation_r2_mmlu: 0.96
519	    theory_vs_simulation_r2_hellaswag: 0.94
520	    theory_vs_simulation_r2_gsm8k: 0.92
521	    theory_vs_simulation_r2_arc_c: 0.91
522	    theory_vs_ctrl_experiment_r2_mmlu: 0.93
523	    theory_vs_ctrl_experiment_r2_hellaswag: 0.9
524	    n_min_for_80pct_power_at_15pct_contam: 4200
525	    n_min_for_80pct_power_at_5pct_contam: 11800
526	    n_min_for_80pct_power_at_25pct_contam: 1900
527	  result_rationale: 'Best 档下，理论与经验高度吻合 (R²>0.9)。原因： (1) Snijders (2001) 的 lz* 方差公式在
528	    n>100 时已非常精确， 我们的 benchmark n 远超 100，所以渐近近似几乎精确。 (2) 4PL model 在 simulation 中是
529	    ground truth，理论推导基于同一模型， 所以 theory-simulation 拟合自然极高 (R²=0.96)。 (3) Theory-control_experiment
530	    拟合略低 (R²=0.93) 因为真实 SFT 注入 并非理论假设的 "item 独立翻转"——有 generalization spillover (4.4%)
531	    和 item 间的 correlation (local dependence violation)。 (4) Inverted-U 的解析拐点公式使其从"奇怪的经验现象"变为
532	    "可预测的理论必然"——审稿人可以代入自己的 benchmark 参数验证。 (5) 最低 n_items 阈值直接给出实操建议：检测 15% 污染需要 ≥4200
533	    items， 这解释了为什么 MMLU/HellaSwag 可行而 ARC-C/HumanEval 不行。
534	
535	    '
536	  tables:
537	  - title: 'Table 7: Theoretical vs Empirical Power Comparison'
538	    columns:
539	    - Benchmark
540	    - n_items
541	    - Power (theory)
542	    - Power (simulation)
543	    - Power (ctrl-exp)
544	    - Theory-Sim R²
545	    rows:
546	    - - MMLU
547	      - 14042
548	      - 0.973
549	      - 0.979
550	      - 0.94
551	      - 0.96
552	    - - HellaSwag
553	      - 10042
554	      - 0.748
555	      - 0.733
556	      - 0.91
557	      - 0.94
558	    - - GSM8K
559	      - 1319
560	      - 0.561
561	      - 0.578
562	      - 0.82
563	      - 0.92
564	    - - ARC-C
565	      - 1172
566	      - 0.138
567	      - 0.129
568	      - 0.74
569	      - 0.91
570	    - - HumanEval
571	      - 164
572	      - 0.225
573	      - 0.243
574	      - 0.63
575	      - 0.9
576	  - title: 'Table S2: Minimum n_items for Target Power (Theoretical)'
577	    columns:
578	    - Contamination %
579	    - Power=0.80
580	    - Power=0.90
581	    - Power=0.95
582	    rows:
583	    - - 5%
584	      - 11800
585	      - 15200
586	      - 18500
587	    - - 10%
588	      - 6100
589	      - 7900
590	      - 9600
591	    - - 15%
592	      - 4200
593	      - 5400
594	      - 6600
595	    - - 25%
596	      - 1900
597	      - 2500
598	      - 3000
599	    - - 50%
600	      - 800
601	      - 1000
602	      - 1200
603	  figures_description:
604	  - 'Figure 7: Power surface — 3D plot with x=n_items, y=contamination%, z=power.
605	    理论曲面 (mesh) 叠加 simulation 点 (dots) 和 ctrl-exp 点 (stars). R² annotated per benchmark.'
606	  - 'Figure 8: Inverted-U theoretical decomposition — 负向 power + 正向 power + combined
607	    power, 理论曲线 vs simulation dots. Nadir 位置 marked.'
608	  analysis: '理论贡献使论文从"IRT applied to LLMs"升级为"principled detection theory"。 审稿人可以用
609	    Table S2 直接查询任意 benchmark 的检测可行性。 R² 全部 >0.9 的关键前提是 best 档下 SFT 注入高度 item-specific
610	    (generalization ratio 低)。 如果 generalization 更强，theory-ctrl R² 会下降。
611	
612	    '
613	- name: Leaderboard Data Reconnaissance
614	  plan_id: exp-leaderboard-data-recon
615	  description: '调研 HuggingFace Open LLM Leaderboard v1 的 per-item binary response
616	    logs 可用性。
617	
618	    '
619	  expected_results:
620	    per_item_data_available: true
621	    data_source: HuggingFace open-llm-leaderboard-old/results
622	    total_models_with_results: 6842
623	    models_with_per_item_binary_logs: 2184
624	    benchmarks_with_per_item:
625	    - MMLU (14042)
626	    - HellaSwag (10042)
627	    - ARC-C (1172)
628	    - TruthfulQA (817)
629	    - Winogrande (1267)
630	    - GSM8K (1319)
631	    data_format: JSON per-model per-benchmark, with per-sample results including 'acc'
632	      field
633	    storage_size_gb: 48
634	    download_method: huggingface_hub API, ~2 hrs on 100Mbps
635	    models_with_all_6_benchmarks: 1847
636	    date_range: 2023-06 to 2024-06
637	    notable_model_families:
638	    - Llama-2 variants (~340)
639	    - Mistral variants (~280)
640	    - Qwen variants (~120)
641	    - Yi variants (~95)
642	    gpu_budget_if_available: 0
643	    gpu_budget_if_unavailable: N/A — data is available
644	  result_rationale: 'Best 档假设 per-item data 大规模可用 (≥500 models, 定义范围 500-7000)。 这在技术上是合理的：Open
645	    LLM Leaderboard v1 使用 EleutherAI lm-evaluation-harness， 默认输出 per-sample results。HuggingFace
646	    在 2024 年将旧版 leaderboard 数据 归档到 open-llm-leaderboard-old/results repo。关键是这些归档是否保留了
647	    per-item logs 而非仅 aggregate scores。Best 档下答案是 yes——至少 2184 个模型有完整 per-item 数据。
648	    这使得 IRT-FIT 的大规模扫描成为可能，且是其独特优势： ConStat 需要 re-test（不可能对已下线模型做），Min-K%++ 需要 token
649	    probs（归档中没有）， 而 IRT-FIT 只需要 binary response pattern——正是归档中保存的数据。
650	
651	    '
652	  tables: []
653	  figures_description: []
654	  analysis: '这是整个 Claim 3 的基础设施。2184 个模型远超 Phase B 的 12 个， leaderboard audit 的 scale
655	    本身就是 contribution。 时间跨度 2023-06 到 2024-06 覆盖了 LLM 军备竞赛的高峰期。
656	
657	    '
658	- name: Leaderboard-Wide Audit
659	  plan_id: exp-leaderboard-audit
660	  description: '对 Open LLM Leaderboard v1 的 ~2000 模型计算 person-fit， 绘制 per-benchmark
661	    污染率随时间趋势，识别 anomalous model families。
662	
663	    '
664	  expected_results:
665	    total_models_analyzed: 1847
666	    total_model_benchmark_cells: 11082
667	    flagged_rate_mmlu: 0.14
668	    flagged_rate_hellaswag: 0.11
669	    flagged_rate_arc_c: 0.08
670	    flagged_rate_gsm8k: 0.09
671	    flagged_rate_winogrande: 0.06
672	    flagged_rate_truthfulqa: 0.07
673	    overall_flagged_rate: 0.12
674	    flagged_rate_2023_h2: 0.06
675	    flagged_rate_2024_h1: 0.18
676	    trend_slope_per_month: 0.012
677	    trend_p_value: 0.003
678	    top_flagged_families:
679	    - family: Yi-derivatives
680	      flagged_rate: 0.31
681	      n_models: 95
682	    - family: Phind-CodeLlama-variants
683	      flagged_rate: 0.28
684	      n_models: 42
685	    - family: Mistral-finetunes (non-official)
686	      flagged_rate: 0.22
687	      n_models: 280
688	    - family: Llama-2 (official)
689	      flagged_rate: 0.03
690	      n_models: 12
691	    gemini15_lz_star_percentile_vs_leaderboard: 99.8
692	    n_models_with_lz_star_gt_gemini15: 3
693	    models_flagged_on_3plus_benchmarks: 78
694	    models_flagged_on_3plus_pct: 0.042
695	    multi_benchmark_flagged_vs_single_or: 4.2
696	  result_rationale: 'Best 档下，overall 12% flagging rate 在预设范围 (5-25%) 内。原因： (1) Flagging
697	    使用控制实验校准的相对阈值（Δlz* deviation from expected misfit baseline）， 而非绝对 lz* 阈值——这避免了
698	    Phase B 中 95% flagging 的问题。 (2) 12% 是合理的生态系统级比例：Open LLM Leaderboard 在 2023-2024
699	    年间 成为 leaderboard gaming 的主要战场，大量 community finetune 通过 SFT on benchmark data
700	    冲榜。但多数官方模型 (Llama-2, Mistral official) flagging 率低。 (3) 时间趋势显著 (p=0.003)：2024H1
701	    (18%) >> 2023H2 (6%)， 与 benchmark contamination 的公众讨论时间线一致—— 2024 年初多篇论文揭露了 leaderboard
702	    gaming。 (4) Yi-derivatives 和 Phind-CodeLlama 的高 flagging rate 与社区已知的 "suspicious
703	    MMLU jumps" 吻合，提供独立验证。 (5) 多 benchmark flagging (≥3) 的 OR=4.2 说明 anomalous misfit
704	    不是随机的—— 在一个 benchmark 上被 flag 的模型更可能在其他 benchmark 上也被 flag， 支持 systematic contamination
705	    而非 random misfit。
706	
707	    '
708	  tables:
709	  - title: 'Table 8: Leaderboard-Wide Contamination Audit Summary'
710	    columns:
711	    - Benchmark
712	    - n_models
713	    - Flagged
714	    - Flagged %
715	    - Mean lz* (flagged)
716	    - Mean lz* (unflagged)
717	    rows:
718	    - - MMLU
719	      - 1847
720	      - 259
721	      - 14.0%
722	      - -12.4
723	      - 16.8
724	    - - HellaSwag
725	      - 1847
726	      - 203
727	      - 11.0%
728	      - -8.7
729	      - 13.2
730	    - - ARC-C
731	      - 1847
732	      - 148
733	      - 8.0%
734	      - -3.1
735	      - 4.8
736	    - - GSM8K
737	      - 1847
738	      - 166
739	      - 9.0%
740	      - -4.5
741	      - 6.2
742	    - - Winogrande
743	      - 1847
744	      - 111
745	      - 6.0%
746	      - -2.8
747	      - 3.4
748	    - - TruthfulQA
749	      - 1847
750	      - 129
751	      - 7.0%
752	      - -3.9
753	      - 5.1
754	  - title: 'Table 9: Temporal Trend in Flagging Rate'
755	    columns:
756	    - Period
757	    - n_models
758	    - Overall Flagged %
759	    - MMLU Flagged %
760	    rows:
761	    - - 2023 Q3
762	      - 312
763	      - 4.2%
764	      - 5.1%
765	    - - 2023 Q4
766	      - 487
767	      - 7.8%
768	      - 9.6%
769	    - - 2024 Q1
770	      - 623
771	      - 15.3%
772	      - 18.7%
773	    - - 2024 Q2
774	      - 425
775	      - 20.1%
776	      - 24.2%
777	  figures_description:
778	  - 'Figure 9: Leaderboard timeline — x-axis month, y-axis flagged rate, one line
779	    per benchmark. 明显上升趋势，MMLU 始终最高。Vertical dashed lines 标记关键事件 (Orca paper, Yi release,
780	    etc).'
781	  - 'Figure 10: Heatmap — rows=model families (top 20), columns=benchmarks, color=flagged
782	    rate. 清晰区分 high-risk (Yi, Phind) vs low-risk (Llama-2 official) families.'
783	  - 'Figure 11: Gemini-1.5 in context — histogram of leaderboard lz*(MMLU), Gemini-1.5
784	    marked as vertical line at 99.8th percentile.'
785	  analysis: '这是论文最有 impact 的 figure。首次用定量方法在 leaderboard scale 揭示 contamination 趋势。
786	    关键 narrative：(1) IRT-FIT 是唯一能做这个 audit 的方法——因为只需 binary response， 而这些已在归档中。(2)
787	    12% 的 flagging rate 不是 "everything is contaminated"， 而是 "a non-trivial minority
788	    is suspicious"——比 Phase B 的 95% 更有区分度。 (3) Gemini-1.5 在 leaderboard 分布中处于 99.8th
789	    percentile， 从 "interesting case study" 升级为 "leaderboard-calibrated extreme outlier"。
790	
791	    '
792	- name: 4PL vs 3PL Ablation
793	  plan_id: exp-4pl-ablation
794	  description: '比较 4PL (with feasibility d) vs 3PL (d=1) 下的 person-fit 检测灵敏度。 用 Phase
795	    A simulation + ctrl-exp 数据。
796	
797	    '
798	  expected_results:
799	    power_4pl_mmlu_15pct: 0.979
800	    power_3pl_mmlu_15pct: 0.941
801	    power_delta_mmlu: 0.038
802	    power_4pl_hellaswag_15pct: 0.733
803	    power_3pl_hellaswag_15pct: 0.684
804	    power_delta_hellaswag: 0.049
805	    false_alarm_4pl: 0.048
806	    false_alarm_3pl: 0.072
807	    false_alarm_delta: 0.024
808	    auroc_4pl_qwen_mmlu: 0.94
809	    auroc_3pl_qwen_mmlu: 0.91
810	    auroc_delta_qwen_mmlu: 0.03
811	    auroc_4pl_gemma_mmlu: 0.92
812	    auroc_3pl_gemma_mmlu: 0.89
813	    auroc_delta_gemma_mmlu: 0.03
814	    d_parameter_impact: d<1 items (impossible-to-get-right) absorb misfit from contamination,
815	      reducing lz* variance → higher sensitivity
816	    mean_d_mmlu: 0.87
817	    pct_items_d_lt_0.9: 0.34
818	  result_rationale: '4PL 优于 3PL 约 3-5pp，差距显著但不大。原因： (1) 4PL 的 d 参数 (upper asymptote
819	    / feasibility) 允许某些 items 的最高正确率 <1.0。 这更真实地反映了 LLM 在某些题目上的 ceiling——即使能力极高也不一定答对。
820	    (2) 固定 d=1 (3PL) 时，高能力模型在 d<1 的 items 上的"错误"被 model 解释为 misfit， inflating baseline
821	    lz* variance。这增加了 false alarm rate (7.2% vs 4.8%)。 (3) 但 contamination signal
822	    (Δlz*) 的 absolute size 在两种参数化下差不多—— 4PL 的优势主要来自 lower false alarm 而非 higher true
823	    positive。 (4) 34% 的 MMLU items 有 d<0.9，说明 d 参数确实 active，不是冗余参数。 综合：4PL 是 preferred，但
824	    3PL 也 workable—— 这对没有 4PL 参数的 benchmark 是好消息。
825	
826	    '
827	  tables:
828	  - title: 'Table S3: 4PL vs 3PL Detection Performance'
829	    columns:
830	    - Setting
831	    - Metric
832	    - 4PL
833	    - 3PL (d=1)
834	    - Δ
835	    rows:
836	    - - Sim MMLU 15%
837	      - Power
838	      - 0.979
839	      - 0.941
840	      - '+0.038'
841	    - - Sim HellaSwag 15%
842	      - Power
843	      - 0.733
844	      - 0.684
845	      - '+0.049'
846	    - - Sim (null)
847	      - False Alarm
848	      - 0.048
849	      - 0.072
850	      - '-0.024'
851	    - - Ctrl Qwen MMLU 15%
852	      - AUROC
853	      - 0.94
854	      - 0.91
855	      - '+0.03'
856	    - - Ctrl Gemma MMLU 15%
857	      - AUROC
858	      - 0.92
859	      - 0.89
860	      - '+0.03'
861	  figures_description:
862	  - 'Figure S2: ROC curves — 4PL vs 3PL, for Qwen MMLU 15% ctrl-exp. 4PL curve consistently
863	    above 3PL, especially in low-FPR region.'
864	  analysis: 'Ablation 结论：4PL 有统计学显著优势但 magnitude 有限 (~3-5pp)。 放在 appendix 而非 main
865	    text，作为 robustness check。 主要审稿意见 R8 得到回答：d 参数有帮助但不是 make-or-break。
866	
867	    '
868	- name: Baseline Method Comparison
869	  plan_id: exp-baseline-comparison
870	  description: '在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs ConStat vs
871	    Min-K%++。 量化 minimal-information 的代价。
872	
873	    '
874	  expected_results:
875	    auroc_irt_fit_15pct: 0.94
876	    auroc_constat_15pct: 0.97
877	    auroc_minkpp_15pct: 0.96
878	    auroc_gap_irt_vs_constat: -0.03
879	    auroc_gap_irt_vs_minkpp: -0.02
880	    auroc_irt_fit_5pct: 0.78
881	    auroc_constat_5pct: 0.84
882	    auroc_minkpp_5pct: 0.88
883	    auroc_gap_5pct_vs_constat: -0.06
884	    auroc_gap_5pct_vs_minkpp: -0.1
885	    type1_irt_fit: 0.048
886	    type1_constat: 0.052
887	    type1_minkpp: 0.044
888	    info_irt_fit: binary response pattern only
889	    info_constat: rephrased test items + binary responses
890	    info_minkpp: token-level log probabilities
891	    compute_irt_fit_per_model_sec: 12
892	    compute_constat_per_model_sec: 3600
893	    compute_minkpp_per_model_sec: 180
894	    applicable_to_archived_leaderboard_irt: true
895	    applicable_to_archived_leaderboard_constat: false
896	    applicable_to_archived_leaderboard_minkpp: false
897	  result_rationale: 'Best 档下 AUROC gap < 5%，即 IRT-FIT 接近 gray-box methods。原因： (1)
898	    At 15% contamination on MMLU (14K items)，信号极强——三种方法都接近 ceiling。 差异主要体现在 low contamination
899	    (5%) 和 small benchmark 上。 (2) ConStat (AUROC=0.97) 通过 rephrased items 获得额外信号：
900	    contaminated model 在原始 items 上 acc 高但 rephrased items 上 acc 下降， 这个 consistency
901	    gap 是 IRT-FIT 无法捕捉的。但差距仅 3pp。 (3) Min-K%++ (AUROC=0.96) 利用 token-level probability
902	    信息—— contaminated items 的 perplexity 异常低。但 Wang et al. (2025) 已证明 这在 post-RL 下失效，而
903	    IRT-FIT 的 Δlz* 更 robust (见 exp-post-rl)。 (4) 5% contamination 时 gap 扩大到 6-10pp——这是
904	    minimal-information 的真实代价。 但 IRT-FIT 的 0.78 AUROC 仍在 useful 范围。 (5) 关键差异化：IRT-FIT
905	    是唯一能 retrospectively audit archived leaderboard 的方法。 ConStat 需要重新测试 (模型可能已下线)，Min-K%++
906	    需要 token probs (归档中没有)。
907	
908	    '
909	  tables:
910	  - title: 'Table 10: Detection Method Comparison (Qwen3.5-9B × MMLU, Ground-Truth
911	      Labels)'
912	    columns:
913	    - Method
914	    - Info Required
915	    - AUROC @15%
916	    - AUROC @5%
917	    - Type-I
918	    - Time/model
919	    - Archived Data?
920	    rows:
921	    - - IRT-FIT (ours)
922	      - Binary responses
923	      - 0.94
924	      - 0.78
925	      - 0.048
926	      - 12s
927	      - 'Yes'
928	    - - ConStat
929	      - Rephrased test
930	      - 0.97
931	      - 0.84
932	      - 0.052
933	      - 60min
934	      - 'No'
935	    - - Min-K%++
936	      - Token log-probs
937	      - 0.96
938	      - 0.88
939	      - 0.044
940	      - 3min
941	      - 'No'
942	  - title: 'Table S4: Method Comparison Across Benchmarks (15% contamination)'
943	    columns:
944	    - Benchmark
945	    - IRT-FIT
946	    - ConStat
947	    - Min-K%++
948	    - Gap (IRT vs best)
949	    rows:
950	    - - MMLU (14K)
951	      - 0.94
952	      - 0.97
953	      - 0.96
954	      - '-0.03'
955	    - - HellaSwag (10K)
956	      - 0.91
957	      - 0.95
958	      - 0.94
959	      - '-0.04'
960	    - - GSM8K (1.3K)
961	      - 0.82
962	      - 0.91
963	      - 0.89
964	      - '-0.09'
965	    - - ARC-C (1.2K)
966	      - 0.74
967	      - 0.86
968	      - 0.84
969	      - '-0.12'
970	  figures_description:
971	  - 'Figure 12: Detection frontier diagram — x-axis information requirement (categorical:
972	    binary < rephrased < token-probs < logits < weights), y-axis AUROC. IRT-FIT 在最左端，AUROC
973	    接近 gray-box methods。'
974	  - 'Figure 13: ROC comparison — 3 methods overlaid, at 15% and 5% contamination.
975	    15% 几乎重叠，5% 差距可见。'
976	  analysis: '这张表是 Claim 1 的关键证据。Narrative：IRT-FIT 以 minimal information 达到 接近 gray-box
977	    的检测力 (gap<5pp)，且是唯一能做 retrospective audit 的方法。 5% 时的 gap 是诚实的 limitation——低污染+少
978	    item 时确实需要更多信息。 但 detection frontier framing 让这成为"expected tradeoff"而非 weakness。
979	
980	    '
981	- name: Multiscale lzm Statistic
982	  plan_id: exp-multiscale-lzm
983	  description: '实现 Hong, Lin & Cheng (2021) 的 multiscale lzm——跨 benchmark 聚合的标准化 lz*，
984	    提供 model-level 整体污染指标。
985	
986	    '
987	  expected_results:
988	    lzm_gemini15: 8.42
989	    lzm_gpt4: 3.21
990	    lzm_claude3opus: 2.87
991	    lzm_llama3_70b: 1.94
992	    lzm_qwen2_72b: 1.78
993	    lzm_mean_12models: 3.14
994	    lzm_sd_12models: 2.31
995	    lzm_qwen_clean: 2.45
996	    lzm_qwen_15pct: -1.82
997	    lzm_qwen_50pct: -6.73
998	    lzm_gemma_clean: 2.91
999	    lzm_gemma_15pct: -1.24
1000	    lzm_gemma_50pct: -5.89
1001	    lzm_vs_single_benchmark_auroc_improvement: 0.04
1002	    lzm_auroc_at_15pct: 0.96
1003	    single_best_benchmark_auroc_at_15pct: 0.94
1004	    lzm_contamination_spearman: -0.91
1005	    lzm_contamination_p: <0.001
1006	  result_rationale: 'lzm 通过 cross-benchmark aggregation 获得 ~4pp AUROC improvement。原因：
1007	    (1) lzm 是各 benchmark lz* 的 variance-weighted average， 大 benchmark (MMLU, HellaSwag)
1008	    贡献更多 weight——这些恰好是信号最强的。 (2) 单 benchmark noise 被 aggregation 平均掉—— 例如 GSM8K 上
1009	    false negative 可能在 MMLU 上被 true positive 补偿。 (3) Gemini-1.5 的 lzm=8.42 远超其他模型，因为它在多个
1010	    benchmark 上都 anomalous。 (4) 控制实验中 lzm 与 contamination level 的 Spearman=-0.91，
1011	    几乎完美单调——因为 lzm aggregation 增加了 effective n_items， 相当于在一个 ~27K items 的 "super benchmark"
1012	    上做检测。 (5) 但 lzm 的 prerequisite 是模型在多个 benchmark 上都有数据—— leaderboard audit 中 1847
1013	    个模型满足这一条件。
1014	
1015	    '
1016	  tables:
1017	  - title: 'Table S5: Multiscale lzm for Phase B Models'
1018	    columns:
1019	    - Model
1020	    - lzm
1021	    - Flagged BMs
1022	    - θ_mean
1023	    rows:
1024	    - - Gemini-1.5-Pro
1025	      - 8.42
1026	      - 4/5
1027	      - 2.14
1028	    - - GPT-4-0613
1029	      - 3.21
1030	      - 3/5
1031	      - 2.87
1032	    - - Claude-3-Opus
1033	      - 2.87
1034	      - 3/5
1035	      - 2.63
1036	    - - Llama-3-70B
1037	      - 1.94
1038	      - 2/5
1039	      - 1.82
1040	  figures_description:
1041	  - 'Figure S3: lzm distribution — histogram of lzm for 1847 leaderboard models, Gemini-1.5
1042	    marked. Right tail constitutes flagged models.'
1043	  analysis: 'lzm 是 appendix material，不是 main contribution，但提供了 model-level summary
1044	    statistic 的自然延伸。 对 leaderboard audit 特别有用——一个数字总结"这个模型整体多可疑"。
1045	
1046	    '
1047	- name: Post-RL Hypothesis Test
1048	  plan_id: exp-post-rl
1049	  description: 'Qwen3.5-9B 上先 SFT 污染 (15% MMLU) 再 GRPO 训练， 测试 IRT-FIT 是否在 RL 后仍保持检测力。
1050	
1051	    '
1052	  expected_results:
1053	    pre_rl_lz_star: -8.7
1054	    pre_rl_accuracy: 0.78
1055	    pre_rl_theta: 1.62
1056	    post_rl_lz_star: -5.1
1057	    post_rl_accuracy: 0.81
1058	    post_rl_theta: 1.89
1059	    post_rl_delta_lz_vs_clean: -23.4
1060	    post_rl_cohen_d_vs_clean: 2.1
1061	    lz_star_retention_rate: 0.58
1062	    detection_still_significant: true
1063	    detection_p_value: <1e-8
1064	    auroc_post_rl_vs_clean: 0.88
1065	    auroc_drop_from_pre_rl: 0.06
1066	    minkpp_auroc_pre_rl: 0.96
1067	    minkpp_auroc_post_rl: 0.61
1068	    minkpp_signal_retention: 0.22
1069	    irt_advantage_post_rl: 0.27
1070	    grpo_reward: rule-based (correctness on held-out math/reasoning tasks)
1071	    grpo_steps: 2000
1072	    grpo_lr: 1e-5
1073	  result_rationale: 'Best 档下 IRT-FIT 在 post-RL 后仍保持检测力 (d=2.1, AUROC=0.88)， 而 Min-K%++
1074	    大幅退化 (AUROC 0.96→0.61)。原因： (1) GRPO 优化的是 reward (reasoning correctness)，不是 likelihood——
1075	    所以 token-level probability 分布被重塑，Min-K%++ 依赖的低 perplexity 信号被冲淡。 Wang et al. (2025)
1076	    已在 DPO 上观察到类似失效。 (2) 但 binary response pattern 更 robust：RL 改善了整体推理能力， 但 SFT 注入的
1077	    item-specific 记忆没有被完全覆盖—— 模型仍然在被污染的难题上 accuracy 异常高，只是 "多余的正确" 变少了 (accuracy 从
1078	    0.78 提到 0.81，θ 从 1.62 到 1.89)。 (3) lz* 从 -8.7 回升到 -5.1 (retention 58%)——RL 平滑了部分
1079	    aberrance， 但没有消除。AUROC 从 0.94 降到 0.88，仍在 useful 范围。 (4) IRT-FIT 的 post-RL advantage
1080	    (+0.27 AUROC over Min-K%++) 是强 narrative： "IRT-FIT not only works at minimal information,
1081	    but is more robust to RL post-processing than methods requiring richer information."
1082	
1083	    '
1084	  tables:
1085	  - title: 'Table 11: Post-RL Detection Robustness'
1086	    columns:
1087	    - Method
1088	    - AUROC (SFT only)
1089	    - AUROC (SFT+GRPO)
1090	    - Retention
1091	    rows:
1092	    - - IRT-FIT (binary)
1093	      - 0.94
1094	      - 0.88
1095	      - 94%
1096	    - - Min-K%++ (token-probs)
1097	      - 0.96
1098	      - 0.61
1099	      - 64%
1100	    - - ConStat (retest)
1101	      - 0.97
1102	      - 0.93
1103	      - 96%
1104	  figures_description:
1105	  - 'Figure 14: lz* trajectory — 3 bars: clean, SFT-contaminated, SFT+GRPO. 展示信号 attenuation
1106	    but persistence.'
1107	  - 'Figure S4: AUROC retention comparison — grouped bar chart, 3 methods × pre/post
1108	    RL. IRT-FIT 和 ConStat robust，Min-K%++ collapses.'
1109	  analysis: 'Post-RL robustness 是 strong differentiator。Narrative： "The same property
1110	    that limits IRT-FIT''s absolute power (binary-only) also protects it from RL-induced
1111	    signal erosion that degrades token-level methods." ConStat 同样 robust 因为 retest
1112	    consistency 也不依赖 token probs。 但 ConStat 需要 live model access，IRT-FIT 不需要。
1113	
1114	    '
1115	- name: Extra Benchmarks — BBH & MATH
1116	  plan_id: exp-extra-benchmarks
1117	  description: '在 BBH (6,511 items) 和 MATH (5,000 items) 上验证 power curve， 填充 1K-10K
1118	    items 的 power gap。
1119	
1120	    '
1121	  expected_results:
1122	    bbh_n_items: 6511
1123	    bbh_power_sim_15pct: 0.87
1124	    bbh_power_theory_15pct: 0.85
1125	    bbh_power_ctrl_15pct_qwen: 0.89
1126	    bbh_cohen_d_15pct_qwen: 2.1
1127	    math_n_items: 5000
1128	    math_power_sim_15pct: 0.82
1129	    math_power_theory_15pct: 0.8
1130	    math_power_ctrl_15pct_qwen: 0.85
1131	    math_cohen_d_15pct_qwen: 1.9
1132	    power_curve_with_7_benchmarks_r2: 0.97
1133	    n_items_coverage: 164 (HumanEval) → 14042 (MMLU), now continuous
1134	    bbh_4pl_source: PSN-IRT calibration (available)
1135	    math_4pl_source: PSN-IRT calibration (available)
1136	  result_rationale: 'BBH 和 MATH 填补了 1K-10K 区间的关键 gap。在 best 档下： (1) BBH (6.5K items)
1137	    power=0.87-0.89，MATH (5K items) power=0.82-0.85， 都在理论预测的 ±3pp 内——验证了 power ∝ n_items
1138	    的解析关系。 (2) 这两个 benchmark 特别有价值因为它们是 reasoning-heavy (BBH) 和 math-heavy (MATH)，
1139	    与 MMLU 的 knowledge-heavy 不同——跨领域一致性加强了方法的 generality。 (3) 有了 7 个 benchmark 的数据点，power
1140	    curve fit R²=0.97， Figure 7 的 power surface 变得更加 convincing。 (4) MATH 上 d=1.9
1141	    略低于 2.0 阈值——因为 MATH 的 items 更 heterogeneous (部分 items 是 open-ended generation
1142	    converted to binary)， 4PL fit 稍差，但 AUROC=0.85 仍实用。
1143	
1144	    '
1145	  tables:
1146	  - title: 'Table S6: Extended Benchmark Results'
1147	    columns:
1148	    - Benchmark
1149	    - n_items
1150	    - Power (sim)
1151	    - Power (theory)
1152	    - Power (ctrl)
1153	    - d @15%
1154	    rows:
1155	    - - MMLU
1156	      - 14042
1157	      - 0.979
1158	      - 0.973
1159	      - 0.94
1160	      - 2.8
1161	    - - HellaSwag
1162	      - 10042
1163	      - 0.733
1164	      - 0.748
1165	      - 0.91
1166	      - 2.2
1167	    - - BBH
1168	      - 6511
1169	      - 0.87
1170	      - 0.85
1171	      - 0.89
1172	      - 2.1
1173	    - - MATH
1174	      - 5000
1175	      - 0.82
1176	      - 0.8
1177	      - 0.85
1178	      - 1.9
1179	    - - GSM8K
1180	      - 1319
1181	      - 0.578
1182	      - 0.561
1183	      - 0.82
1184	      - 1.4
1185	    - - ARC-C
1186	      - 1172
1187	      - 0.129
1188	      - 0.138
1189	      - 0.74
1190	      - 1.1
1191	    - - HumanEval
1192	      - 164
1193	      - 0.243
1194	      - 0.225
1195	      - 0.63
1196	      - 0.6
1197	  figures_description:
1198	  - 'Figure S5: Power vs n_items — 7 benchmark data points with theoretical curve
1199	    overlay. R²=0.97 annotated.'
1200	  analysis: 'BBH 和 MATH 是 Claim 2 的 supporting evidence， 不改变 narrative 但显著增强 power
1201	    theory 的 empirical backing。 放入 main text 的 power curve figure (Figure 7) 中。
1202	
1203	    '
1204	- name: Domain-Level Analysis (MMLU)
1205	  plan_id: exp-domain-analysis
1206	  description: '按 MMLU subject category 分别计算 person-fit， 识别 Gemini-1.5 的污染是全面的还是集中在特定
1207	    domain。
1208	
1209	    '
1210	  expected_results:
1211	    gemini15_stem_lz_star: 36.2
1212	    gemini15_humanities_lz_star: 33.8
1213	    gemini15_social_sciences_lz_star: 30.1
1214	    gemini15_other_lz_star: 28.4
1215	    gemini15_cross_domain_cv: 0.09
1216	    gemini15_pattern: uniform across all domains
1217	    stem_n_items: 4890
1218	    humanities_n_items: 3782
1219	    social_sciences_n_items: 3214
1220	    other_n_items: 2156
1221	    ctrl_qwen_stem_lz_star: -9.2
1222	    ctrl_qwen_humanities_lz_star: -8.4
1223	    ctrl_qwen_social_sciences_lz_star: -7.9
1224	    ctrl_qwen_other_lz_star: -6.8
1225	    ctrl_domain_cv: 0.12
1226	    ctrl_pattern: roughly uniform — consistent with random 15% sampling across domains
1227	    yi_lightning_stem_lz_star: -12.4
1228	    yi_lightning_humanities_lz_star: 2.1
1229	    yi_lightning_social_sciences_lz_star: -8.7
1230	    yi_lightning_other_lz_star: 1.8
1231	    yi_lightning_pattern: concentrated in STEM and social sciences — partial domain
1232	      contamination
1233	  result_rationale: 'Best 档下域分析揭示两种不同的 contamination pattern： (1) Gemini-1.5 的 lz*
1234	    在所有 domain 上均极高 (CV=0.09)， 说明其 100% accuracy 是 uniform 的——要么全量 item 都被训练过， 要么模型能力极强到每个
1235	    domain 都满分。结合 θ=0.78 (非极高)， uniform contamination 是更合理的解释。 (2) Yi-Lightning 显示
1236	    domain-specific pattern——STEM 和 social sciences 极端 aberrant， humanities 和 other
1237	    正常。这暗示 selective contamination (可能通过 domain-specific data collection)。 (3) 控制实验
1238	    (random 15% sampling) 产生 roughly uniform pattern (CV=0.12)， 与 Gemini-1.5 一致——这支持
1239	    Gemini-1.5 的污染是 random/full 而非 domain-targeted。 (4) Domain-level granularity使
1240	    "contamination forensics" 成为可能： 不仅检测是否污染，还能推断 contamination strategy。
1241	
1242	    '
1243	  tables:
1244	  - title: 'Table S7: Domain-Level Person-Fit (MMLU)'
1245	    columns:
1246	    - Model
1247	    - STEM
1248	    - Humanities
1249	    - Social Sci
1250	    - Other
1251	    - CV
1252	    - Pattern
1253	    rows:
1254	    - - Gemini-1.5-Pro
1255	      - 36.2
1256	      - 33.8
1257	      - 30.1
1258	      - 28.4
1259	      - 0.09
1260	      - Uniform
1261	    - - Yi-Lightning
1262	      - -12.4
1263	      - 2.1
1264	      - -8.7
1265	      - 1.8
1266	      - 1.42
1267	      - Domain-specific
1268	    - - Ctrl (Qwen 15%)
1269	      - -9.2
1270	      - -8.4
1271	      - -7.9
1272	      - -6.8
1273	      - 0.12
1274	      - Uniform (expected)
1275	    - - Ctrl (Qwen clean)
1276	      - 4.2
1277	      - 3.8
1278	      - 4.5
1279	      - 3.1
1280	      - 0.14
1281	      - Uniform baseline
1282	  figures_description:
1283	  - 'Figure S6: Radar chart — 4 domains × selected models. Gemini-1.5 uniformly extreme.
1284	    Yi-Lightning asymmetric.'
1285	  analysis: Domain analysis 是 Claim 3 的 supporting evidence，增加了 forensic 价值。 Gemini-1.5
1286	    的 uniform pattern + low θ 组合是 "smoking gun"—— 一个 θ=0.78 的模型不可能在所有 domain 都 100%
1287	    accuracy 除非 contamination。 Yi-Lightning 的 domain-specific pattern 提供了 qualitatively
1288	    different case， 丰富了 contamination taxonomy。
1289	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcfac731-c6da-45a9-ab51-b8e223fd9a77",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "901f1966-5b4a-4708-b956-3828c06348f0",
  "sourceToolAssistantUUID": "bcfac731-c6da-45a9-ab51-b8e223fd9a77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-20T10:05:41.514Z_

I now have a thorough understanding of the paper. Let me also check if there is a "dream review report" from the first round's best scenario to see what was already reviewed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "901f1966-5b4a-4708-b956-3828c06348f0",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdfjsUek4tVDCweXjLG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "175e48c5-e6ca-47b2-95f7-a7f4fe52612f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A6k2rwU1j3m9vfNHUaD8Wr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23557,
      "cache_read_input_tokens": 66006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23557,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T10:05:44.086Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UgANqZdY3vjwXMZeXpeNkm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "175e48c5-e6ca-47b2-95f7-a7f4fe52612f",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdfjsUek4tVDCweXjLG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25d3ead3-76cb-447a-a256-ce2f7f2fea69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A6k2rwU1j3m9vfNHUaD8Wr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23557,
      "cache_read_input_tokens": 66006,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23557
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 66006,
          "cache_creation_input_tokens": 23557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23557,
            "ephemeral_1h_input_tokens": 0
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

_source line 36 · 2026-05-20T10:05:44.090Z_

<details><summary>↩ Tool result · `toolu_01UgANqZdY3vjwXMZeXpeNkm`</summary>

```text
1	---
2	dream_id: dream_20260520T082549
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-20T09:14:10.147818+00:00
6	---
7	
8	# Dream Review Report: IRT-FIT
9	
10	**Paper:** IRT-FIT: Detecting Benchmark Contamination in Large Language Models via Item Response Theory Person-Fit Statistics
11	
12	**Review Mode:** Full (2-Reviewer Roundtable)
13	
14	---
15	
16	## Overall Assessment
17	
18	**Score: 4 / 6 (Weak Accept)**
19	
20	The paper presents a well-motivated cross-domain transfer of psychometric person-fit statistics to LLM benchmark contamination detection. The core insight — that a contaminated LLM answering benchmark questions is functionally analogous to an examinee with item preknowledge — is clean and enables a novel "minimal-information operating point" on the contamination detection frontier. The controlled experiments are solid, the power theory provides lasting practical value, and the 2,847-model leaderboard audit is a unique capability no competing method can match. However, several technical issues (lzm null distribution, unidimensionality assumption, narrow post-RL validation) and a critically thin reference list (11 entries) prevent a strong accept. With targeted revisions, this paper would be competitive at a top ML venue.
21	
22	---
23	
24	## Reviewer Scores
25	
26	| Reviewer | Focus | Score | Confidence |
27	|----------|-------|-------|------------|
28	| R1 | Methods + Experiments | 4.0 | 4/5 |
29	| R2 | Novelty + Related Work | 3.5 | 4/5 |
30	| **Consensus** | | **4.0** | **4/5** |
31	
32	---
33	
34	## Strengths
35	
36	### S1. Compelling Framing and Real Gap (R1, R2)
37	The "minimal-information operating point" and "detection frontier" concepts provide a clear organizing principle. The paper precisely identifies where IRT-FIT sits: it requires only binary response data (the least privileged information level), yet achieves AUROC 0.96 at 15% contamination — higher than methods requiring token-level probabilities (Min-K%++ 0.88) or re-testing capabilities (ConStat 0.83). This framing is both intellectually honest and practically important: binary response data is the only information available for retrospective audits of historical leaderboard submissions.
38	
39	### S2. Solid Controlled Experiments (R1)
40	The ground-truth contamination setup via QLoRA SFT on two architectures (Qwen3.5-9B, Gemma-4-31B) across six contamination levels is well-designed. Key findings are convincing:
41	- Cohen's d = 2.3 at 15% contamination (near-complete separation of clean vs. contaminated distributions)
42	- False positive rates well-calibrated (0.042/0.041 at α=0.05)
43	- Contamination selectivity: +31pp on contaminated items, only +1.4-3.7% generalization to non-contaminated items
44	- Cross-architecture consistency (effect sizes differ <15%) rules out model-specific artifacts
45	
46	### S3. Power Theory with Practical Value (R1, R2)
47	The power formula (Eq. 4) fits simulation data with R²=0.97. The inverted-U inflection point prediction (within 0.02 of observed) from item difficulty distributions alone is the paper's strongest theoretical contribution. Table 8 (minimum n_items for 80% power) provides actionable guidance: ≥3,200 items for 15% contamination, ≥9,800 for 5%. This directly explains why ARC-C (1,172 items) yields only 12.9% power — a benchmark-size limitation, not a method failure.
48	
49	### S4. Unique Leaderboard-Scale Audit (R1, R2)
50	The 2,847-model audit is something no other method can replicate at this scale on historical data. The temporal trend (6% → 18% flagged rate from 2023Q1 to 2024Q1) is newsworthy. The Gemini-1.5 case study — 100% MMLU accuracy with θ̂=0.78 yielding lz*=+34.75 — vividly demonstrates the two-sided framework's value: one-sided testing would completely miss this full-contamination signal.
51	
52	### S5. Two-Sided Framework is a Genuine Observation (R2)
53	The identification of two contamination regimes (partial: lz* << 0 from aberrant patterns; full: lz* >> 0 from over-consistent patterns) is non-obvious from the psychometrics literature. The inverted-U empirical structure connecting these regimes is a new finding. While the statistical test (|lz*| > c_{α/2}) is straightforward, the observation motivating it is substantive.
54	
55	---
56	
57	## Weaknesses
58	
59	### W1. lzm Null Distribution Error (R1) — **Major**
60	Equation 3 defines lzm = (1/√K) Σ|lz*_k|. Under the null, each lz* ~ N(0,1), so |lz*| follows a half-normal distribution (mean ≈ 0.798, SD ≈ 0.603). The sum of half-normals is NOT N(0,1). The paper claims lzm is "approximately standard normal" verified by KS test (p=0.312), but this cannot be correct for the formula as written. Either: (a) the actual implementation uses signed lz* values (which would make lzm ~ N(0,1) by CLT), contradicting the absolute-value formula; or (b) the KS test was performed against the wrong null distribution. This is a correctness issue that must be resolved.
61	
62	### W2. Critically Thin Reference List (R2) — **Major**
63	11 references is far below the expected density for a top ML venue (typically 30-50+). Critical omissions include:
64	- **Contamination detection:** Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023); no survey/position papers on contamination
65	- **IRT for NLP/AI:** Lalor et al. (2019), Vania et al. (2021), Martinez-Plumed et al. (2019)
66	- **Person-fit:** Karabatsos (2003) comparing 36 person-fit statistics (why lz* over alternatives?), Sinharay (2017) on preknowledge detection power (the most directly relevant psychometric precedent)
67	- **Test security:** Wollack & Schoenig (2018) and CAT-based cheating detection literature
68	
69	This gap undermines the novelty claim — without surveying the full person-fit literature, reviewers cannot assess what is genuinely new.
70	
71	### W3. Unfair Baseline Comparison (R1, R2) — **Moderate**
72	ConStat is designed to detect contamination via performance inconsistency on rephrased items. SFT contamination permanently alters model weights, making re-test scores nearly identical — this inherently disadvantages ConStat. The comparison is valid in the sense that IRT-FIT works where ConStat cannot, but calling it "outperformance" without acknowledging the threat-model mismatch is misleading. Additionally:
73	- Min-K%++ operates on raw text, not MCQA binary responses. The information hierarchy (binary < token probs) is not a strict difficulty ordering.
74	- IRT-FIT requires pre-calibrated 4PL item parameters (from PSN-IRT), which is itself a substantial prerequisite. This dependency should be explicitly listed alongside the "binary responses only" claim.
75	- No confidence intervals on AUROC values. The 0.96 vs 0.88 difference may not be statistically significant given sample sizes.
76	
77	### W4. Narrow Post-RL Validation (R1) — **Moderate**
78	The post-RL experiment tests only GRPO on one model (Qwen3.5-9B) at one contamination level (15% MMLU). The claim that "person-fit survives post-RL training" is stated broadly but tested narrowly. Missing:
79	- Other RL algorithms (PPO, DPO, KTO)
80	- Other base models
81	- Other contamination levels
82	- Multiple RL training durations (does signal degrade with more RL steps?)
83	
84	The AUROC retention (96%) is impressive but could be an artifact of the specific GRPO configuration tested.
85	
86	### W5. Unidimensionality Assumption (R1) — **Moderate**
87	The 4PL IRT model assumes unidimensional ability (single θ). MMLU spans 57 diverse domains. Snijders' N(0,1) null distribution guarantee requires correct model specification. If the IRT model is misspecified, lz* under the null may deviate from N(0,1), inflating false positives. The paper's FPR of 0.042 at α=0.05 is slightly below nominal, suggesting the calibration is adequate empirically, but the theoretical justification is incomplete. This is acknowledged in the Limitations section but deserves deeper analysis — particularly for the leaderboard audit where models may have genuinely multidimensional ability profiles.
88	
89	### W6. Leaderboard Audit Lacks Ground Truth (R1) — **Minor**
90	The 12% flagged rate is not 12% contamination rate. Without external validation (e.g., correlation with known contaminated models, independent contamination audits), the audit results are suggestive but not confirmatory. The paper should distinguish "statistically anomalous response pattern" from "confirmed contamination." The time trend could also reflect model architecture/size trends rather than increasing contamination.
91	
92	### W7. QLoRA-Specific Contamination (R2) — **Minor**
93	Controlled experiments use QLoRA SFT exclusively. The generalization ratio (0.12) and selectivity pattern may differ under full-parameter SFT, continued pretraining with benchmark items mixed into other data, or paraphrased benchmark items. These alternative contamination pathways should be discussed.
94	
95	---
96	
97	## Questions for Authors
98	
99	1. **lzm formula vs. implementation:** Does the actual code compute lzm using |lz*| (absolute values as in Eq. 3) or signed lz* values? If absolute values, what is the correct null distribution? The claimed KS test against N(0,1) appears inconsistent with the formula.
100	
101	2. **PSN-IRT parameter sensitivity:** How robust are the results to perturbations in the IRT item parameters? If the 4PL parameters from PSN-IRT have estimation error (calibrated on only 12 models), how much does lz* drift? A sensitivity analysis would strengthen the method's credibility.
102	
103	3. **Pretraining contamination:** The Limitations section acknowledges this is out of scope. Can you provide even a rough estimate of what happens when contamination comes via pretraining exposure (which produces smoother generalization) rather than SFT memorization?
104	
105	4. **Adversarial inflection-point targeting:** Given that the inverted-U inflection point is predictable from item difficulty distributions, could a sophisticated adversary deliberately contaminate at exactly the inflection fraction to evade detection? How would you defend against this?
106	
107	5. **Missing baselines:** Why were CoDeC and recent post-RL-aware contamination detection methods not compared? Would you be willing to add these in a revision?
108	
109	---
110	
111	## Experiment Coverage Assessment
112	
113	Compared to the full experiment design (review_context.yaml), the paper covers all 11 planned experiments:
114	
115	| Experiment | Status | Tables |
116	|-----------|--------|--------|
117	| Two-Sided Detection | ✅ Fully covered | 17, 18 |
118	| Extended Simulation | ✅ Fully covered | 4, 5 |
119	| Controlled Contamination | ✅ Fully covered | 1, 2, 3 |
120	| Power Theory | ✅ Fully covered | 6, 7, 8 |
121	| Leaderboard Audit | ✅ Fully covered | 19, 20, 21 |
122	| 4PL vs 3PL Ablation | ✅ Fully covered | 13, 14 |
123	| Baseline Comparison | ✅ Fully covered | 9, 10 |
124	| Multiscale lzm | ✅ Fully covered | 15, 16 |
125	| Post-RL Hypothesis | ✅ Fully covered | 11, 12 |
126	| Extra Benchmarks | ✅ Fully covered | 22 |
127	| Domain Analysis | ✅ Fully covered | 23, 24 |
128	
129	All planned experiments are present. The paper's experimental scope is comprehensive and matches the design specification.
130	
131	---
132	
133	## Recommendations for Revision
134	
135	**Must-fix (for acceptance):**
136	1. Correct lzm null distribution — either fix the formula or provide the correct null
137	2. Expand reference list to 30+ entries covering contamination detection, IRT-for-NLP, person-fit literature
138	3. Add AUROC confidence intervals throughout
139	4. Acknowledge PSN-IRT item bank as an explicit dependency in the "information requirements" framing
140	
141	**Strongly recommended:**
142	5. Broaden post-RL validation (at minimum, one additional RL algorithm or model)
143	6. Discuss ConStat comparison fairness: acknowledge different threat models
144	7. Add discussion of unidimensionality violation and its empirical impact
145	8. Distinguish "flagged" from "contaminated" in leaderboard audit language
146	
147	**Nice to have:**
148	9. Add CoDeC / Self-Critique baselines
149	10. Discuss pretraining contamination pathway even if out of scope
150	11. Consolidate some tables to reduce density (24 tables in 11 pages is heavy)
151	
152	---
153	
154	## Final Verdict
155	
156	**Score: 4 / 6 (Weak Accept)**
157	
158	The paper makes a genuine contribution: it identifies a new operating point on the contamination detection frontier, provides a theoretically grounded power analysis, and demonstrates unique large-scale audit capability. The core methodology is sound modulo the lzm issue. The controlled experiments are well-designed and convincing. The main barriers to a strong accept are: (1) a fixable but non-trivial technical error in the lzm statistic, (2) a critically thin reference list that obscures the novelty claim, and (3) insufficient discussion of method dependencies and comparison fairness. These are all addressable in revision. The paper is above the acceptance threshold for a top ML venue but needs the revisions listed above to be convincing.
159	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25d3ead3-76cb-447a-a256-ce2f7f2fea69",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "6ab4c883-6911-49e6-ae06-a0b266379385",
  "sourceToolAssistantUUID": "25d3ead3-76cb-447a-a256-ce2f7f2fea69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-20T10:05:47.871Z_

Now I have comprehensive understanding of the paper, the dream-tier "best" experimental setup, the previous round's review, and the literature map. Let me now write my R2 review focused on Novelty/Significance and Related Work/Positioning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ab4c883-6911-49e6-ae06-a0b266379385",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdgWsRDd7GnSrfT9Ckt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "894f22ad-ef5e-4ed5-9191-2b56d92943a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153wUWuReH2AtMG4EbnXZdh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3985,
      "cache_read_input_tokens": 89563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3985,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T10:05:49.080Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ko4tz4d3Ts27fhkFS6yoUd`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "894f22ad-ef5e-4ed5-9191-2b56d92943a8",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdgWsRDd7GnSrfT9Ckt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1173d562-6e34-4c84-b1b0-48e33dbfa058",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153wUWuReH2AtMG4EbnXZdh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3985,
      "cache_read_input_tokens": 89563,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3985
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 89563,
          "cache_creation_input_tokens": 3985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3985,
            "ephemeral_1h_input_tokens": 0
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

_source line 39 · 2026-05-20T10:05:49.087Z_

<details><summary>↩ Tool result · `toolu_01Ko4tz4d3Ts27fhkFS6yoUd`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1173d562-6e34-4c84-b1b0-48e33dbfa058",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "09d0d5d2-73fb-42b1-a845-ab5183de27a1",
  "sourceToolAssistantUUID": "1173d562-6e34-4c84-b1b0-48e33dbfa058",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-20T10:05:51.640Z_



Now I will submit my comprehensive R2 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09d0d5d2-73fb-42b1-a845-ab5183de27a1",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdgtA5d3zj96CQ8VDQa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "451073f4-ba38-4d0c-9daa-bbc2f064a012",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RRP6vHSFKomN4YALtumbr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 768,
      "cache_read_input_tokens": 93548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 768,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T10:07:45.543Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01KSyoAXTamgmeezV5Y74dMa`</summary>

```json
{
  "report": "---\ndream_id: dream_20260520T092614\ntier: best\nreviewer: R2\nfocus: Novelty/Significance and Related Work/Positioning\noverall_score: 3.5/6 Borderline Conference\ntimestamp: 2026-05-20\n---\n\n# R2 Review: IRT-FIT — Novelty, Significance, and Related Work\n\n**Paper:** IRT-FIT: Detecting Benchmark Contamination in Large Language Models via Person-Fit Statistics at the Minimal-Information Operating Point\n\n---\n\n## Summary\n\nThe paper proposes IRT-FIT, a contamination detection framework that repurposes IRT person-fit statistics (lz*) to flag benchmark contamination in LLMs using only binary correct/incorrect response patterns. The authors frame this as occupying the \"minimal-information operating point\" on a contamination \"detection frontier.\" Three claims are made: (1) AUROC > 0.9 at 15% contamination on large benchmarks, within 3-5pp of gray-box methods; (2) detection power follows a predictable inverted-U with analytical nadir derivation; (3) a leaderboard audit of 1,847 models reveals ~12% flagging with a significant temporal trend. Experiments include simulation, controlled QLoRA SFT contamination on two models, post-RL robustness testing, and baseline comparisons against ConStat and Min-K%++.\n\n---\n\n## Strengths\n\n**S1. The core analogy is genuinely novel and well-exploited.**\nThe connection between \"LLM contaminated on benchmark items\" and \"examinee with item preknowledge\" is clean, correct, and -- to the best of my knowledge -- previously unexplored. This is not merely applying an existing tool to a new domain: the paper identifies that the analogy requires non-trivial adaptation (the calibration gap due to universal positive misfit, the need for Delta-lz* rather than absolute thresholds, the two-sided framework for the inverted-U). The psychometric person-fit literature has studied preknowledge detection for decades (Drasgow et al. 1985, Snijders 2001, Sinharay 2017, Karabatsos 2003), but no prior work has connected this to LLM evaluation. This cross-disciplinary bridge is the paper's strongest intellectual contribution.\n\n**S2. The \"minimal-information operating point\" is a genuine conceptual contribution, not marketing.**\nThe framing is well-defined: binary correct/incorrect is strictly less information than token probabilities, rephrased retesting, or training data access. The paper honestly quantifies the cost of this operating point (3-5pp AUROC gap at 15%, widening to 6-10pp at 5%) and demonstrates the unique capability it enables (retrospective audit of 1,847 archived models that no other method can touch). This is the kind of conceptual framing that organizes thinking for the field -- it answers \"what is the minimal information needed for contamination detection?\" and provides an empirical lower bound.\n\n**S3. The inverted-U characterization is a substantive theoretical finding.**\nThe observation that detection power follows a non-monotonic curve with contamination level -- and that this can be analytically derived from the interaction between contamination fraction and MLE ability estimation -- is non-trivial. The nadir formula (pi* approximately equal to (theta_true - theta_low)/(theta_high - theta_low)) provides a predictive tool. The dual-regime structure (negative lz* from aberrant patterns at low contamination, positive lz* from over-consistency at high contamination) is a genuinely new observation not present in the psychometric cheating detection literature, which typically considers only one-sided tests for preknowledge.\n\n**S4. The leaderboard audit is high-impact and uniquely enabled.**\nAuditing 1,847 models at ecosystem scale, revealing temporal trends (6% to 18%, p=0.003) and identifying high-risk model families (Yi-derivatives 31%, Phind-CodeLlama 28%) is the most practically impactful result. The finding that multi-benchmark flagging has OR=4.2 provides evidence for systematic rather than random misfit. No competing method can perform this audit -- ConStat requires live model retesting, Min-K%++ requires token probabilities unavailable in archives. This unique capability is well-demonstrated.\n\n**S5. Post-RL robustness provides structural differentiation.**\nThe finding that IRT-FIT retains 94% AUROC after GRPO while Min-K%++ drops to 64% is a meaningful result. The explanation is mechanistically clean: RL reshapes token probability distributions but preserves binary response patterns for memorized items. This directly addresses the Wang et al. (2025) critique that MIA methods fail post-RL, and positions IRT-FIT as complementary rather than merely weaker.\n\n---\n\n## Weaknesses\n\n**W1. [Major] Related work coverage is critically insufficient for a paper claiming cross-disciplinary novelty.**\n\nThe paper cites only 10 references. For a work that claims to bridge psychometrics and NLP, this is unacceptably thin. Specific gaps:\n\n*Person-fit and cheating detection literature (most critical gap):*\n- Sinharay (2017) \"Which Statistic Should Be Used to Detect Item Preknowledge?\" in JEBS -- this is the single most directly relevant psychometric paper. It conducts power analyses for preknowledge detection using lz and other statistics, finding peak detection at 10-30% preknowledge. The inverted-U is implicitly present. Not citing this paper seriously undermines the novelty claim around the power analysis.\n- Karabatsos (2003) comparing 36 person-fit statistics -- why lz* over alternatives like HT, C_aution, U3? Without this discussion, the choice of lz* appears arbitrary.\n- Meijer & Sijtsma (2001) \"Methodology Review: Evaluating Person Fit\" -- the standard survey.\n- van der Flier (1982), Levine & Rubin (1979) -- foundational person-fit references.\n- Wollack & Schoenig (2018) on test security and detection of aberrant behavior in high-stakes testing -- directly analogous application domain.\n\n*Contamination detection (missing recent work):*\n- Ye et al. (2024) \"Data Contamination Quiz\" -- a binary-level detection method. This is a direct competitor operating at a similar information level. Its omission is a serious oversight.\n- Golchin & Surdeanu (2024) \"Time Travel in LLMs\" -- distinct from Oren et al. but related.\n- Balloccu et al. (2024) \"Leak, Cheat, Repeat\" -- systematic study of closed-source LLM contamination.\n- Dekoninck et al. (2024) \"Evading Data Contamination Detection\" -- adversarial perspective.\n- Dong et al. (2024) \"Generalization or Memorization\" -- distinguishing genuine capability from memorization.\n\n*IRT for AI/NLP evaluation:*\n- Lalor et al. (2019) IRT for NLP evaluation.\n- Martinez-Plumed et al. (2019) computational psychometrics for AI.\n- Vania et al. (2021) IRT analysis of NLU benchmarks.\n- Rodriguez et al. (2021) evaluation beyond accuracy with IRT.\n\nThe literature map in the project's own files lists Sinharay (2017) and Karabatsos (2003) as \"foundation\" papers, yet they appear nowhere in the submitted manuscript. This is a puzzling omission.\n\n**W2. [Major] The novelty of the power analysis is overstated given Sinharay (2017).**\n\nSinharay (2017) already conducted power analyses for person-fit statistics under item preknowledge, including the observation that detection power depends on test length and preknowledge proportion. The inverted-U shape -- while the specific two-regime decomposition (negative vs. positive lz*) is new for LLMs -- is partially anticipated by Sinharay's finding that detection power peaks at intermediate preknowledge levels. The paper should clearly delineate what is new relative to Sinharay: (a) the application to LLMs; (b) the two-sided framework motivated by the over-consistency regime; (c) the analytical nadir formula; (d) the benchmark-size thresholds. Without this explicit positioning, the theoretical contribution appears more novel than it is.\n\n**W3. [Major] The \"detection frontier\" framing, while useful, conflates information type with information quantity.**\n\nThe hierarchy \"binary < rephrased retest < token probs < logits < weights\" is presented as a strict ordering of information access. But this conflation is problematic:\n- Rephrased retesting requires *active interaction* (crafting new items, re-evaluating), which is a qualitatively different requirement from passively observing token probabilities.\n- Token probabilities are often freely available via APIs (e.g., OpenAI's logprobs parameter), making them arguably easier to obtain than binary response logs across many items.\n- IRT-FIT requires *pre-calibrated 4PL item parameters* from PSN-IRT, which were calibrated on a specific model population. This is itself a substantial prerequisite that should be listed alongside \"binary responses only.\" The claim of \"minimal information\" is somewhat misleading without acknowledging this dependency.\n\nThe frontier concept would be stronger if it distinguished between information *about the model* (binary responses, token probs, weights) and information *about the test* (pre-calibrated item parameters, rephrased items). IRT-FIT is minimal in model information but non-trivial in test information.\n\n**W4. [Moderate] Comparison fairness issues with baselines.**\n\nThe baseline comparison has two fairness concerns:\n1. *ConStat at 0.97 AUROC at 15%*: ConStat is designed to detect memorization via original-vs-rephrased consistency drops. SFT contamination (item-specific memorization) is ConStat's sweet spot. The comparison is informative but should note that ConStat's advantage comes from leveraging a different signal (consistency) unavailable to IRT-FIT.\n2. *Min-K%++ at 0.96 AUROC at 15%*: The paper claims IRT-FIT is \"within 2pp,\" but at 5% contamination the gap is 10pp (0.78 vs 0.88). The paper's headline number (15% contamination on MMLU) is cherry-picked -- it's the condition where all methods approach ceiling. A fairer comparison would report average AUROC across contamination levels and benchmarks.\n3. *Missing same-information-level baseline*: Ye et al. (2024) \"Data Contamination Quiz\" operates at a similar binary information level. Its omission prevents readers from assessing whether IRT-FIT's improvement over same-level methods justifies the IRT complexity.\n4. *No simple baseline*: An accuracy z-score anomaly detector (flagging models whose accuracy deviates from expected given their overall ability) would test whether the full IRT machinery is necessary or whether simpler statistics suffice.\n\n**W5. [Moderate] The Gemini-1.5 case study is problematic as contamination evidence.**\n\nGemini-1.5-Pro achieving 100% MMLU accuracy with theta=0.78 is presented as strong contamination evidence. But theta=0.78 is estimated from the *same 4PL model* that produces the lz* statistic. If the IRT model is misspecified for a model of genuinely extreme capability (Gemini-1.5 is a frontier model), theta estimation could be severely biased downward, producing a misleadingly low theta and inflated lz*. The paper needs to address: could a genuinely capable model with multidimensional strengths produce this pattern under IRT model misspecification? The unidimensionality assumption is most likely to break down precisely for frontier models with heterogeneous capability profiles.\n\n**W6. [Minor] Only two model families in controlled experiments.**\n\nQwen3.5-9B and Gemma-4-31B are both dense decoder-only transformers of moderate size. The generality claim needs validation on:\n- MoE architectures (e.g., Mixtral)\n- Larger models (70B+) where baseline ability is higher and the contamination signal may be weaker\n- Models with different pretraining paradigms\n- Different contamination injection methods beyond QLoRA SFT\n\n---\n\n## Questions for Authors\n\n**Q1.** Why are Sinharay (2017) and Karabatsos (2003) -- listed in your own literature map as \"foundation\" papers -- absent from the manuscript? Sinharay's power analysis for preknowledge detection is the single most directly relevant psychometric precedent.\n\n**Q2.** How does the method perform when item parameters are not pre-calibrated by PSN-IRT? If a practitioner wants to apply IRT-FIT to a new benchmark without PSN-IRT coverage, what is the minimum number of models needed to calibrate item parameters, and how does calibration quality affect detection performance?\n\n**Q3.** Have you considered or tested Ye et al. (2024) \"Data Contamination Quiz\" as a same-information-level baseline? This method also operates on binary response patterns and is a direct competitor.\n\n**Q4.** For the leaderboard audit, how do you distinguish contamination-induced misfit from IRT model misspecification? The 4PL item parameters were calibrated on a specific model population; models from very different architectures or training pipelines may produce systematic misfit that is not contamination-related.\n\n**Q5.** The retention rate in Table post-RL is reported as \"94%\" for IRT-FIT but this appears to be (0.88/0.94)*100 = 93.6%. Meanwhile the lz* signal retention is only 58% (from -8.7 to -5.1). These two numbers tell different stories. Which is the more informative measure of post-RL robustness? Could you report both clearly?\n\n**Q6.** The nadir formula pi* = (theta_true - theta_low)/(theta_high - theta_low) requires knowledge of theta_true, which is the clean model's ability. In the leaderboard audit setting (no clean baseline), how is this estimated? Is the nadir location used in any part of the audit pipeline?\n\n---\n\n## Minor Issues\n\n1. **Reference formatting**: Several bib entries are incomplete (Wu et al. 2026 cuts off mid-entry; Wang et al. 2025 has \"arXiv:2502.xxxxx\" as a placeholder).\n\n2. **Terminology consistency**: The paper alternates between \"person-fit\" and \"misfit\" without clear distinction. In psychometrics, \"misfit\" typically means poor model fit; \"person misfit\" means the person's pattern is inconsistent with the model. Standardize terminology.\n\n3. **Table density**: 11 tables in the main text plus 7 in the appendix is heavy. Consider consolidating the two dose-response tables (Qwen and Gemma) into a single table with a model column.\n\n4. **Limitations section format**: EMNLP 2026 (ARR) requires Limitations as a standalone section after Conclusion, not a \\paragraph within Conclusion. Current formatting risks desk rejection.\n\n5. **\"Minimal-information operating point\" appears 7 times** in the paper. Once defined, subsequent uses could be shortened to \"minimal-information point\" or \"MIOP.\"\n\n6. **HumanEval (164 items)**: Including HumanEval results throughout adds noise -- it consistently fails. Consider dropping it from main tables and noting it once as an expected failure case.\n\n---\n\n## Overall Assessment\n\n**Score: 3.5 / 6 -- Borderline Conference**\n\n**Justification:**\n\n*For conference (4.0):*\nThe paper has a genuinely novel core insight (person-fit for LLM contamination), a useful conceptual contribution (minimal-information operating point / detection frontier), a substantive theoretical finding (inverted-U with analytical derivation), and a unique high-impact application (1,847-model leaderboard audit). The controlled experiments are well-designed with ground-truth labels, and the post-RL robustness finding is a meaningful differentiator. If these were all that mattered, this would be a clear accept.\n\n*Against conference (holding it at 3.5):*\nThree issues pull the score down. First, the critically thin reference list (10 citations) is unacceptable for a paper claiming cross-disciplinary novelty -- particularly the omission of Sinharay (2017), which directly anticipates the power analysis contribution, and Karabatsos (2003), which would contextualize the choice of lz*. Without engaging this literature, the novelty claim is unsubstantiated. Second, the \"detection frontier\" and \"minimal information\" framing partially obscures the method's dependency on pre-calibrated 4PL item parameters, which is a non-trivial prerequisite. Third, the missing same-information-level baseline (Ye et al. 2024) leaves a gap in the comparative evaluation -- readers cannot assess whether IRT's complexity is necessary or whether simpler binary-level methods achieve comparable results.\n\n*Path to 4.0 (Conference):*\n(a) Expand references to 25-30+, properly engaging the person-fit and contamination detection literatures. Explicitly position relative to Sinharay (2017) and Karabatsos (2003).\n(b) Add Ye et al. (2024) as a same-information-level baseline.\n(c) Acknowledge the PSN-IRT item bank dependency explicitly in the information requirements framing.\n(d) Add a simple accuracy-based anomaly detection baseline to justify IRT complexity.\n(e) Fix the Limitations section format for EMNLP compliance.\n\n*Path to 4.5+ (Borderline Award):*\nAll of the above, plus: (f) broaden controlled experiments to 3+ model families including MoE and 70B+; (g) address the systematic positive bias / calibration gap more rigorously with empirical null distribution analysis; (h) add confidence intervals throughout.\n",
  "project": "irt_personfit_contam",
  "tier": "best",
  "dream_id": "dream_20260520T092614",
  "overall_score": "3.5/6 Borderline Conference",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "451073f4-ba38-4d0c-9daa-bbc2f064a012",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdgtA5d3zj96CQ8VDQa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "538d52ac-65b1-43ea-a10e-b2eff407b97c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RRP6vHSFKomN4YALtumbr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 768,
      "cache_read_input_tokens": 93548,
      "output_tokens": 4478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 768
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4478,
          "cache_read_input_tokens": 93548,
          "cache_creation_input_tokens": 768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 768,
            "ephemeral_1h_input_tokens": 0
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

_source line 42 · 2026-05-20T10:07:48.840Z_

<details><summary>↩ Tool result · `toolu_01KSyoAXTamgmeezV5Y74dMa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/review_report.md\", \"dream_id\": \"dream_20260520T092614\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "538d52ac-65b1-43ea-a10e-b2eff407b97c",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a0a6b7f6fc67f13d8",
  "type": "user",
  "uuid": "fd22de4a-452f-4260-bd13-6d1e4464d179",
  "sourceToolAssistantUUID": "538d52ac-65b1-43ea-a10e-b2eff407b97c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-20T10:08:03.055Z_

Review submitted. Here is the summary:

**R2 Review Score: 3.5/6 (Borderline Conference)**

**Key findings from my Novelty/Significance and Related Work analysis:**

**Strengths:**
- The person-fit-to-LLM-contamination analogy is genuinely novel and well-exploited
- "Minimal-information operating point" is a real conceptual contribution, not marketing
- The inverted-U with dual-regime structure (negative lz* at low contamination, positive at high) is a substantive new observation absent from psychometric literature
- The 1,847-model leaderboard audit is uniquely enabled and high-impact
- Post-RL robustness provides structural differentiation vs. token-level methods

**Critical weaknesses pulling score from 4.0 to 3.5:**
1. **Critically thin references (10 citations)** -- Sinharay (2017), the most directly relevant psychometric paper on preknowledge detection power analysis, is absent despite being in the project's own literature map. Karabatsos (2003), Ye et al. (2024) "Data Contamination Quiz" (a same-information-level competitor), and ~15 other important references are missing
2. **Power analysis novelty is overstated** given Sinharay (2017) already conducted power analyses for person-fit under preknowledge, partially anticipating the inverted-U
3. **"Minimal information" claim obscures the PSN-IRT dependency** -- the method requires pre-calibrated 4PL item parameters, a non-trivial prerequisite not acknowledged alongside the "binary responses only" framing
4. **No same-information-level baseline** -- without comparing to Ye et al. (2024) or a simple accuracy z-score detector, readers cannot assess whether IRT complexity is justified

**Path to acceptance:** Expand references to 25-30+, add missing baselines, acknowledge item bank dependency, fix Limitations section format. Report saved to `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd22de4a-452f-4260-bd13-6d1e4464d179",
  "isSidechain": true,
  "agentId": "a0a6b7f6fc67f13d8",
  "requestId": "req_011CbDdqi2drTvW4hEZjVfcK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6070ac7f-02d7-4d92-8cb0-90bc7a6a79bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011g7KiqL2RicyW49C1aChkA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4612,
      "cache_read_input_tokens": 94316,
      "output_tokens": 519,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4612
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 519,
          "cache_read_input_tokens": 94316,
          "cache_creation_input_tokens": 4612,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4612,
            "ephemeral_1h_input_tokens": 0
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
