# Research conversation: You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Y

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a21f57df8dd0071ef.jsonl`
- **Structured JSON:** [`bb07b9b65125fd97b3a8.json`](../../sessions/bb/bb07b9b65125fd97b3a8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-20T09:20:43.771Z_

You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus: **methods and experiments**.

## Paper Summary

**Title:** "Information-Theoretic Limits of Binary-Response Contamination Detection: When IRT Person-Fit Is Enough and When It Is Not"

The paper investigates whether benchmark contamination (test data leaking into LLM training) can be detected from binary (correct/incorrect) response patterns alone, using IRT person-fit statistics (lz*). It develops a two-sided detection framework calibrated on 4PL IRT models from PSN-IRT. The core finding is predominantly **negative**: binary responses are fundamentally insufficient to detect realistic SFT contamination levels (<45%). The paper reframes this as establishing the "detection frontier" — a lower bound on what binary-only methods can achieve.

## Key Experimental Components

### 1. Simulation: Inverted-U and Power Valley (Section 4.1)
- Extends PSN-IRT simulation with contamination levels 0%–100% on 5 benchmarks (MMLU, HellaSwag, GSM8K, ARC-C, HumanEval)
- Incorporates SFT generalization noise
- Key finding: inverted-U power curve — power peaks near 15%, collapses in "power valley" at 25–50%, recovers at extreme levels (≥75%)
- Table 1: Power matrix across benchmarks and contamination levels
- Table 2: Inverted-U inflection points (28–41% depending on benchmark)

### 2. Controlled SFT Contamination (Section 4.2)
- QLoRA SFT injection of 0%/5%/10%/15%/25%/50% MMLU items into Qwen3.5-9B and Gemma-4-31B
- Tables 3 & 4: At 15% contamination on Qwen, accuracy +9.1pp, but lz*=-1.22 (p=0.222, not significant)
- SFT generalization ratio = 0.26 at 15% — non-contaminated items also improve
- Inverted-U confirmed empirically: lz* rebounds from -1.22 to -1.08 at 25%
- Table 5: AUROC = 0.63 at 15%, Cohen's d = 0.61 — barely above chance
- Two-model agreement rate: 83%

### 3. Theoretical Power Analysis (Section 4.3)
- Derives power formula: Power ≈ Φ(√(n·h(p_c)) - z_α)
- Theory vs simulation: R²=0.89 under 3PL, R²=0.67 under 4PL
- Table 7: 80% power at 15% contamination requires ~42,000 items (binary) vs ~4,200 (logits) — 10× gap
- Table 8: Theoretical extrapolation to BBH and MATH (no empirical validation)

### 4. Two-Sided Detection / Leaderboard Audit (Section 5)
- Table 9: 12 models × 5 benchmarks, BH-FDR at α=0.05
- Only Gemini-1.5-Pro flagged (lz*=+34.75 on MMLU, -15.71 on GSM8K, -12.37 on HumanEval)
- 58/60 model-benchmark pairs in "indeterminate zone" (|lz*|<3)
- Table 10: Only 12 models audited due to data unavailability
- Section 5.3: Domain-level analysis — Gemini-1.5 uniform across all 57 MMLU subjects

### 5. Attempts to Overcome Binary Bottleneck (Section 6)
- Multi-statistic fusion lz^m: cross-benchmark correlation r=0.34, AUROC improvement only +0.04
- 4PL vs 3PL ablation: 4PL inflates lz* variance to 1.34, FAR from 5.2% to 8.3%, power loss 3-10pp
- Table 14: Detailed 4PL vs 3PL comparison

### 6. Detection Frontier (Section 7.1)
- Table 16: IRT-FIT (binary, AUROC 0.63@15%) vs ConStat (binary+retest, 0.72@15%) vs Min-K%++ (token probs, 0.81@15%)
- Log-linear relationship between information bits and detection power

### 7. Post-RL Signal Destruction (Section 7.2)
- Table 17: GRPO training on Qwen3.5-9B with 25% MMLU contamination
- lz* drops from -1.08 (post-SFT) to -0.23 (post-GRPO), retention ratio 0.12
- Table 18: Retention <12% across all contamination levels
- Generalization ratio jumps from 0.31 to 0.78

## Review Context: Imagined Experiments Coverage
The review_context.yaml lists 10 experiments. The paper covers all major ones but with limitations:
- exp-leaderboard-audit: Only 12 models (vs imagined hope of larger scan)
- exp-extra-benchmarks: BBH/MATH are theoretical extrapolation only (no empirical calibration)
- exp-ctrl-contam: Only MMLU benchmark for controlled contamination (not multiple)
- exp-post-rl: Only one model (Qwen3.5-9B), one contamination level detailed in Table 17

## Your Review Task

Provide a detailed review covering:

1. **Methodological Soundness** — Is the two-sided detection framework well-justified? Is the power analysis derivation rigorous? Are there methodological gaps?

2. **Experimental Design** — Are the controlled experiments well-designed? Are there confounds? Is the evaluation fair?

3. **Statistical Rigor** — Are the statistical tests appropriate? Is the BH-FDR correction properly applied? Are confidence intervals and effect sizes reported?

4. **Reproducibility** — Are there enough details to reproduce? Are data/code availability addressed?

5. **Specific Strengths** (bullet list)

6. **Specific Weaknesses** (bullet list, with severity: minor/moderate/major)

7. **Questions for Authors** (3-5 specific questions)

8. **Score** (1-6 scale) with justification

9. **Confidence** (1-5: 1=low, 5=expert)

Format your review clearly with headers. Be rigorous but fair.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "cc6850ab-f8a3-49b4-b614-0e5b36bf6500",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T09:20:43.779Z_

```json
{
  "parentUuid": "cc6850ab-f8a3-49b4-b614-0e5b36bf6500",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
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
  "uuid": "bfd3f76a-bb5c-4c3d-9aa7-0ebdf58833a7",
  "timestamp": "2026-05-20T09:20:43.779Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T09:20:46.851Z_



I'll start by reading the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfd3f76a-bb5c-4c3d-9aa7-0ebdf58833a7",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaFTi7w5oUtRZKw3LJF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64094c11-a390-4fde-9c6d-9ba6be5b5ca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aof77HA7Bs6tYFGnWZ1eMG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16180,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16180,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 4 · 2026-05-20T09:20:47.272Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015eWG6eU5uyBubwsBTV1Z8U`</summary>

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
  "parentUuid": "64094c11-a390-4fde-9c6d-9ba6be5b5ca1",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaFTi7w5oUtRZKw3LJF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a5560e5-20f2-49ea-9463-e6deff8c2f99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aof77HA7Bs6tYFGnWZ1eMG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16180,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16180
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16180,
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

_source line 5 · 2026-05-20T09:20:47.276Z_

<details><summary>↩ Tool result · `toolu_015eWG6eU5uyBubwsBTV1Z8U`</summary>

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
  "parentUuid": "4a5560e5-20f2-49ea-9463-e6deff8c2f99",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "d42cbfbe-aeeb-4601-a375-c0fe28da601b",
  "sourceToolAssistantUUID": "4a5560e5-20f2-49ea-9463-e6deff8c2f99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T09:20:50.127Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01GFTvCasoxHBhpPyWvNFaRK`</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d42cbfbe-aeeb-4601-a375-c0fe28da601b",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaFipiKATgEZ7fHhjs6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b772bd48-24b9-4479-b56b-4c69990504d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rAv8b3S6dCczZuYnaCjr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 16180,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1448
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 74,
          "cache_read_input_tokens": 16180,
          "cache_creation_input_tokens": 1448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1448,
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

_source line 7 · 2026-05-20T09:20:50.158Z_

<details><summary>↩ Tool result · `toolu_01GFTvCasoxHBhpPyWvNFaRK`</summary>

```text
{"result":"# 项目 irt_personfit_contam 概况\n\n## 实验状态 (3 个)\n\n- **exp-two-sided**: DONE (negative) — \n- **phase_b_personfit**: DONE (success) — \n- **sim_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp-two-sided** (negative): Two-sided detection (|lz*| > threshold) with benchmark-specific θ MLE + parametric bootstrap empirical null + BH-FDR control will reduce Phase B flagging rate from 93% to a reasonable level (<20%), isolating genuine contamination signals from θ estimation bias ← 基于 phase_b_personfit\n- **phase_b_personfit** (success): Real LLM benchmark response data from PSN-IRT 12 models shows significant inter-model variation in person-fit statistics (lz*, outfit, infit), with specific models exhibiting anomalous patterns indicative of benchmark contamination — particularly Gemini-1.5 with accuracy-ability dissociation\n- **sim_001** (negative): Under 4PL IRT model, lz* person-fit statistic can detect partial benchmark contamination (5-30% items) with >80% power at α=0.05, and detection power follows an inverted-U curve across contamination levels (low contamination undetectable, moderate contamination most detectable, high contamination mimics high ability)\n  [null_check_summary](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/data/null_check_summary.json) | [simulation_summary](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/data/simulation_summary.json) | [power_curves_combined](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/chart/power_curves.png)\n\n## 趋势\n成功 1 / 负向 2 / 失败 0 / 共 3\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb2-36806: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b772bd48-24b9-4479-b56b-4c69990504d3",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "10460214-a13a-48e3-beb3-0df44b5c7273",
  "sourceToolAssistantUUID": "b772bd48-24b9-4479-b56b-4c69990504d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T09:20:53.068Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BRyCFCYYyMTd4wndTqqEBx`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10460214-a13a-48e3-beb3-0df44b5c7273",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaFwAcQgS5crUUGJ3P7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98057896-5787-4ebd-95ec-97358d67afc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVmayiMfSeiBEfFHsYNm9F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 17628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 751,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 9 · 2026-05-20T09:20:53.077Z_

<details><summary>↩ Tool result · `toolu_01BRyCFCYYyMTd4wndTqqEBx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp-two-sided** (negative): Two-sided detection (|lz*| > threshold) with benchmark-specific θ MLE + parametric bootstrap empirical null + BH-FDR control will reduce Phase B flagging rate from 93% to a reasonable level (<20%), isolating genuine contamination signals from θ estimation bias ← 基于 phase_b_personfit\\n- **phase_b_personfit** (success): Real LLM benchmark response data from PSN-IRT 12 models shows significant inter-model variation in person-fit statistics (lz*, outfit, infit), with specific models exhibiting anomalous patterns indicative of benchmark contamination — particularly Gemini-1.5 with accuracy-ability dissociation\\n- **sim_001** (negative): Under 4PL IRT model, lz* person-fit statistic can detect partial benchmark contamination (5-30% items) with >80% power at α=0.05, and detection power follows an inverted-U curve across contamination levels (low contamination undetectable, moderate contamination most detectable, high contamination mimics high ability)\\n  [null_check_summary](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/data/null_check_summary.json) | [simulation_summary](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/data/simulation_summary.json) | [power_curves_combined](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/chart/power_curves.png)\\n\\n## 趋势\\n成功 1 / 负向 2 / 失败 0 / 共 3\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb2-36806: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1553, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98057896-5787-4ebd-95ec-97358d67afc9",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "b12a8d83-a936-48c0-9653-1e2d92ba0520",
  "sourceToolAssistantUUID": "98057896-5787-4ebd-95ec-97358d67afc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T09:20:54.044Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FL8S5XX61LgTqgNagCqW7v`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b12a8d83-a936-48c0-9653-1e2d92ba0520",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaFwAcQgS5crUUGJ3P7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d9373a9-f668-4e41-8f46-c327e59e322e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVmayiMfSeiBEfFHsYNm9F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 17628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 751,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 11 · 2026-05-20T09:20:54.053Z_

<details><summary>↩ Tool result · `toolu_01FL8S5XX61LgTqgNagCqW7v`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ROADMAP.md\", \"content\": \"# irt_personfit_contam — Research Dashboard\\n\\n> 最后更新: 2026-05-20 08:27 UTC | 更新原因: MVP 通过, 进入 research 阶段; 引用 paper_framing.md + experiment_plan.yaml; Dream 已启动\\n\\n## 核心方向\\n用 IRT person-fit 统计量在 information access 谱系最底层（仅 binary response pattern，无需 logits/weights/training data）检测 LLM benchmark 污染。详见 `paper_framing.md`。\\n\\n## 目标会议\\n- **Primary**: EMNLP 2026（用户确认 \\\"emnlp可行\\\"；ARR submission DDL 5/25 — 已追问可行性，等回复）\\n- **Fallback**: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\\n\\n## 当前阶段: Research（MVP 已通过 2026-05-20）\\n\\n### MVP 结果摘要\\n- **Phase A (simulation)**: Null check ✅, MMLU power@15%=97.9%, power ∝ n_items\\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.0/θ=0.78/lz*=+34.75（全面污染信号）; 所有 benchmark SD >> 0.5; 多模型 lz* < -1.96\\n- **关键发现**: 需双侧检测（full contamination → lz* >> 0, partial → lz* << 0）\\n- **Inverted-U**: 仅 MMLU/HellaSwag 在 50% 以内展现真正下降（Reviewer 修正）\\n\\n### Core Claims (from paper_framing.md)\\n1. **Minimal-information detection**: Person-fit stats 在检测前沿最底层 work\\n2. **Detection characterization**: Power ∝ n_items + 双侧信号结构 + inverted-U 理论化\\n3. **Empirical prevalence**: Gemini-1.5 case study + 跨模型/跨 benchmark 污染模式\\n\\n### Experiment Plan Status (from experiment_plan.yaml)\\n**P0 (headline)**:\\n- [ ] `exp-two-sided` — 双侧检测框架（CPU, 进行中）\\n- [ ] `exp-extended-sim` — 扩展模拟 60-100%（CPU, 进行中）\\n- [ ] `exp-ctrl-contam` — 控制实验 Qwen3.5-9B + Gemma-4-31B（~80 GPU-hrs, depends on two-sided）\\n- [ ] `exp-power-theory` — Power 理论推导（CPU, depends on extended-sim）\\n\\n**P1 (robustness)**:\\n- [ ] `exp-leaderboard-audit` — Open LLM Leaderboard v1 扫描（~20 GPU-hrs）\\n- [ ] `exp-4pl-ablation` — 4PL vs 3PL 检测对比（CPU）\\n- [ ] `exp-baseline-comparison` — vs ConStat/Min-K%++（~30 GPU-hrs）\\n- [ ] `exp-multiscale-lzm` — 跨 benchmark 聚合统计量（CPU）\\n\\n**P2 (expanded scope)**:\\n- [ ] `exp-post-rl` — Post-RL 假设检验（~40 GPU-hrs）\\n- [ ] `exp-extra-benchmarks` — BBH/MATH 扩展（~10 GPU-hrs）\\n- [ ] `exp-domain-analysis` — MMLU domain-level 分析（CPU）\\n\\n### Dream 状态\\n- `dream_20260520T082549`: pending（full review mode），等待回调后再批准 P0 实验\\n\\n## 近期任务\\n- [ ] 等 Dream 回调 → 审阅模拟审稿 → 决定是否调整 framing/plan\\n- [ ] exp-two-sided 重分析（Agent 执行中）\\n- [ ] exp-extended-sim 扩展模拟（Agent 执行中）\\n- [ ] GPU 服务器 bjb2-36806 环境配置（Agent 执行中）\\n- [ ] 确认目标会议（等用户回复 EMNLP DDL 问题）\\n\\n## GPU 预算\\n- 已分配: 4× RTX 5090 32GB (bjb2-36806)\\n- P0: ~80 GPU-hrs | P1: ~50 GPU-hrs | P2: ~50 GPU-hrs | Total: ~180 GPU-hrs\\n- 当前使用: 0（环境配置中）\\n\\n## 12 模型身份 (PSN-IRT)\\n| ID | θ | Model | 异常信号 |\\n|----|---|-------|---------|\\n| 0 | 1.46 | 360GPT2-Pro | — |\\n| 1 | 3.77 | DeepSeek-V3 | θ 远超第二名 |\\n| 2 | 1.14 | Doubao-pro | — |\\n| 3 | 0.78 | **Gemini-1.5** | **MMLU acc=1.0, lz*=+34.75** |\\n| 4 | -3.38 | Gemma-2B-it | — |\\n| 5 | 1.73 | Hunyuan-Turbo | — |\\n| 6 | -1.37 | Mistral-7B-v0.1 | — |\\n| 7 | 0.93 | Moonshot-v1 | — |\\n| 8 | 0.96 | Qwen-Plus | — |\\n| 9 | -0.13 | Qwen2.5-3B | — |\\n| 10 | -1.89 | Vicuna-7B-v1.3 | — |\\n| 11 | 0.77 | Yi-Lightning | — |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D007 | 2026-05-20 | 采纳方向 B: real data 上 person-fit 绝对阈值失效（universal mi | exp-two-sided |\\n| D006 | 2026-05-20 | Phase B 必须用 benchmark-specific θ (MLE)，不能用 PSN-IRT | exp-two-sided |\\n| D005 | 2026-05-20 | Phase B Pass + 发现双侧检测需求: Model 3 MMLU 100% acc/lz* | sim_001, phase_b_personfit |\\n| D004 | 2026-05-20 | Phase A Partial Pass: 方法机制验证成功，power 随 n_items 递减为 | sim_001 |\\n| D003 | 2026-05-20 | 修正 benchmark 分类: ARC-C 降为小(295 items); MVP 不混用 Tru | — |\\n| D002 | 2026-05-20 | 根据 Reviewer 审查细化 MVP: 加入 PSN-IRT 参数 null distribut | — |\\n| D001 | 2026-05-20 | MVP 采用两阶段验证: Phase A 模拟验证（无GPU）+ Phase B 真实数据探测 | — |\\n\\n\", \"total_chars\": 3490, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d9373a9-f668-4e41-8f46-c327e59e322e",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "1ee82a4e-70ec-406c-ad10-b2a78b50aad7",
  "sourceToolAssistantUUID": "9d9373a9-f668-4e41-8f46-c327e59e322e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T09:20:54.962Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QX5eKee1RwYkhYHVHZiPGC`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ee82a4e-70ec-406c-ad10-b2a78b50aad7",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaFwAcQgS5crUUGJ3P7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f631eaf7-b573-4889-99ee-0e52e6520011",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVmayiMfSeiBEfFHsYNm9F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 17628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 751,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 13 · 2026-05-20T09:20:54.972Z_

<details><summary>↩ Tool result · `toolu_01QX5eKee1RwYkhYHVHZiPGC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/memory.md\", \"content\": \"# Memory — irt_personfit_contam\\n\\n## OOM 教训 (2026-05-20)\\n- 7.6GB RAM 机器上，N_SIM×n_items float64 矩阵不能一次性分配。MMLU 10K×14042×8B ≈ 1.07GB 单个矩阵，compute_lz_star 内部创建 ~7 个同尺寸中间数组 → OOM\\n- 解决方案：BATCH_SIZE=500 分批计算 + N_SIM 降至 2000（统计效力足够）\\n- generate_response 和 compute_lz_star 都需要分批\\n\\n## sim_001 关键发现 (2026-05-20)\\n- **Null check 全通过**：PSN-IRT 神经网络估计的 4PL 参数与经典 IRT 兼容，lz* ≈ N(0,1)\\n  - 大 benchmark（GSM8K/HellaSwag/MMLU）KS p 全部 > 0.01\\n  - 小 benchmark（HumanEval/ARC-C）KS p < 0.01，但属预期（items 太少，CLT 近似弱）\\n- **检测力与 n_items 强正相关**：MMLU(14042)=97.9% >> HellaSwag(10042)=73.3% >> GSM8K(1319)=57.8% >> ARC-C(295)=12.9%\\n- **Inverted-U 所有 benchmark 可观测**：power 在 25-50% contamination 达峰，100% 全部 NaN（全答对 → MLE 不收敛）\\n- **100% contamination 导致全 NaN**：所有 response = 1 → theta_hat 退化到 boundary → lz* 无效。这不是 bug，是 IRT 的固有限制\\n- **Hypothesis 部分证伪**：\\\">80% power at 15% contamination\\\" 仅 MMLU 达标，HellaSwag/GSM8K 未达标。但方法确实 work，只是 power 阈值设得太激进\\n\\n## PSN-IRT 12 模型身份 (2026-05-20)\\n\\n**来源**：arXiv:2505.15055 (AAAI 2026 Oral)，GitHub repo `Joe-Hall-Lee/PSN-IRT`\\n**识别方法**：论文 Section 4.1 列出全部 12 个模型名；`data/combine.csv` 行序 = student_id，经验证为字母序排列。DeepSeek-V3 = student_id=1 由论文 Section 5.2 确认（\\\"ability well above 3.0\\\"）。\\n\\n| student_id | θ | 正确率 | 模型名称 | 类型 | 置信度 |\\n|---|---|---|---|---|---|\\n| 0 | 1.46 | 80.6% | 360GPT2-Pro | API 强模型 | ✅ 确定 |\\n| 1 | 3.77 | 85.7% | DeepSeek-V3 | API 强模型 | ✅ 确定（论文确认） |\\n| 2 | 1.14 | 78.9% | Doubao-pro | API 强模型 | ✅ 确定 |\\n| 3 | 0.78 | 84.5% | Gemini-1.5 | API 强模型 | ✅ 确定 |\\n| 4 | -3.38 | 23.1% | Gemma-2B-it | 开源弱模型(2B) | ✅ 确定 |\\n| 5 | 1.73 | 82.1% | Hunyuan-Turbo | API 强模型 | ✅ 确定 |\\n| 6 | -1.37 | 40.0% | Mistral-7B-Instruct-v0.1 | 开源弱模型(7B) | ✅ 确定 |\\n| 7 | 0.93 | 77.0% | Moonshot-v1 | API 强模型 | ✅ 确定 |\\n| 8 | 0.96 | 76.3% | Qwen-Plus | API 强模型 | ✅ 确定 |\\n| 9 | -0.13 | 60.4% | Qwen2.5-3B-Instruct | 开源弱模型(3B) | ✅ 确定 |\\n| 10 | -1.89 | 31.6% | Vicuna-7B-v1.3 | 开源弱模型(7B) | ✅ 确定 |\\n| 11 | 0.77 | 75.2% | Yi-Lightning | API 强模型 | ✅ 确定 |\\n\\n### 识别依据\\n\\n1. **论文明确列出**：Section 4.1 给出全部 12 个模型名，分为 8 个强模型 + 4 个弱模型\\n2. **字母序验证**：`combine.csv` 12 行对应 student_id 0-11，按模型名字母序排列\\n3. **交叉验证**：\\n   - DeepSeek-V3 (id=1) θ=3.77 → 论文称 \\\"ability well above 3.0\\\" ✅\\n   - 4 个弱模型 (Gemma-2B, Mistral-7B, Qwen2.5-3B, Vicuna-7B) 对应 id=4,6,9,10，正确率 23-60% ✅\\n   - 8 个强模型对应 id=0,1,2,3,5,7,8,11，正确率 75-86% ✅\\n\\n### 异常 response pattern 观察\\n\\nGemini-1.5 (id=3) 有显著的 raw accuracy 与 IRT ability 不一致：\\n- 正确率排名 #2 (84.5%)，但 θ 排名仅 #7 (0.78)\\n- 这意味着 4PL IRT 模型检测到 Gemini-1.5 的 response pattern 异常（如：容易题答错、难题答对）\\n- 与之对比：DeepSeek-V3 正确率 #1 (85.7%) 且 θ #1 (3.77)，response pattern 一致性强\\n\\n### 已知污染讨论\\n\\n- **DeepSeek-V3**：社区讨论过 GSM8K/MMLU 可能的训练集重叠，但无定论。θ=3.77 远超第二名(1.73)值得关注\\n- **Qwen 系列**：Qwen-Plus 和 Qwen2.5-3B 的训练数据规模巨大，web crawl 可能包含 benchmark 数据\\n- **Gemini-1.5**：IRT ability 与 raw accuracy 的大幅偏差是最值得深入分析的信号\\n- **Vicuna-7B-v1.3**：基于 LLaMA-1，LLaMA-1 训练数据已知包含部分 benchmark 相关文本\\n\\n## exp-two-sided 关键教训 (2026-05-20)\\n\\n**发现**：Benchmark-specific θ MLE + parametric bootstrap (N=1000) + BH-FDR (α=0.05) 仍然 flag 57/60 cells (95%)。**LLM response patterns 系统性违反 4PL IRT 假设**，不是少数模型的异常。\\n\\n**根因分析**：\\n- 4PL 假设单维能力 + 局部独立，但 LLM 有知识聚类（correlated item responses）+ 多维能力\\n- Phase A null check 通过是因为模拟数据本身从 4PL 生成，自洽但不代表 real data 符合\\n- lz* 值在 real data 上极端（|lz*|=2-36），1000 次 bootstrap 从未复现，说明偏离是系统性的\\n\\n**方向性判断**：\\n- 绝对阈值检测（|lz*| > 1.96 或 bootstrap p < 0.05）对 real LLM data 无意义——所有模型都 misfit\\n- 可行方向：(1) relative ranking across models, (2) contamination-induced misfit vs natural misfit 对比（需控制实验）, (3) lz* 的方向/幅度差异仍携带信号（正向=over-consistent, 负向=aberrant）\\n- Gemini-1.5 仍是最强 case study：MMLU lz*=+31.8 (100% acc, θ_bench=4.0) vs HellaSwag lz*=-15.3（方向翻转）\\n\\n**对 paper framing 的影响**：\\n- Claim 3 (Empirical Prevalence) 需要重新定义 \\\"flagged\\\"——不能用绝对阈值，需要相对度量\\n- exp-ctrl-contam（控制实验）变得更关键：建立 ground-truth 的 \\\"contaminated misfit\\\" vs \\\"natural misfit\\\" 区分\\n\", \"total_chars\": 3725, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f631eaf7-b573-4889-99ee-0e52e6520011",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "d58da4dc-bb0d-429f-b71e-cef65b2163db",
  "sourceToolAssistantUUID": "f631eaf7-b573-4889-99ee-0e52e6520011",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T09:20:55.144Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LkhGCF8p5K6E4GTjn3zyt5`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d58da4dc-bb0d-429f-b71e-cef65b2163db",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaFwAcQgS5crUUGJ3P7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c307b40e-c339-454a-ac53-8b1e638c5575",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVmayiMfSeiBEfFHsYNm9F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 17628,
      "output_tokens": 387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 751
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 387,
          "cache_read_input_tokens": 17628,
          "cache_creation_input_tokens": 751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 751,
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

_source line 15 · 2026-05-20T09:20:55.156Z_

<details><summary>↩ Tool result · `toolu_01LkhGCF8p5K6E4GTjn3zyt5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/decisions.yaml\", \"content\": \"_next_id: 8\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 07:13 UTC\\n  summary: 'MVP 采用两阶段验证: Phase A 模拟验证（无GPU）+ Phase B 真实数据探测'\\n  rationale: '核心假设（person-fit stats 检测 contamination）可在理想化 IRT 模拟中先验证——如果模拟中都检测不到，真实数据更不可能。Phase\\n    A 零 GPU 成本、1-2 天即可得到 go/no-go 信号，避免在假设不成立时浪费 GPU 资源。Pass 标准: 15% contamination\\n    下 lz* 检测率 > 80%（α=0.05）且 inverted-U shape 可观测。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 07:16 UTC\\n  summary: '根据 Reviewer 审查细化 MVP: 加入 PSN-IRT 参数 null distribution sanity check + 按\\n    benchmark 规模分层 pass/fail + Phase B 量化标准'\\n  rationale: 'Reviewer 指出三个 warning: (1) Phase B 无 pass/fail 标准导致不可证伪; (2) 6 个 benchmark\\n    item 数差异巨大(164~14K)，统一 80% 检测率不合理; (3) PSN-IRT 用神经网络估参，经典 lz* 的 N(0,1) 渐近性质未必成立。三者均成立，分别补充:\\n    Phase B 定义 lz* 跨模型方差 + 异常值标准; 大/小 benchmark 分层 pass 阈值(80%/50%); Phase A 新增 null\\n    distribution KS 检验。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 07:22 UTC\\n  summary: '修正 benchmark 分类: ARC-C 降为小(295 items); MVP 不混用 TruthfulQA 3PL; 加入 a≤0\\n    item 过滤'\\n  rationale: 'Reviewer critical: PSN-IRT 中 ARC-C 仅 295 items（非预期的 ~1,172），不满足大 benchmark\\n    ≥1000 阈值。TruthfulQA 无 PSN-IRT 4PL 参数（仅 ATLAS 3PL），混用引入方法论不一致。部分 items a < 0（负判别度）违反\\n    IRT 假设需过滤。MVP 改为只用 5 个 PSN-IRT benchmark，大 benchmark 仅 MMLU/HellaSwag/GSM8K 三个。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 08:11 UTC\\n  summary: 'Phase A Partial Pass: 方法机制验证成功，power 随 n_items 递减为预期行为，推进 Phase B'\\n  rationale: sim_001 结果：(1) Null check 全通过（MMLU/HellaSwag/GSM8K KS p>0.05），PSN-IRT\\n    4PL 参数与 lz* N(0,1) 假设兼容；(2) Inverted-U shape 全部可观测；(3) MMLU(14K items) power@15%=97.9%\\n    远超 80% 阈值。未达标项：HellaSwag 73.3%（差 6.7pp）、GSM8K 57.8%。但 3 个大 benchmark 均>50%，不触发\\n    global fail。Power 与 n_items 强正相关是统计必然（不是方法缺陷），且在论文中可正面呈现为 power function 分析。Phase\\n    B 真实数据才是方法的终极验证——如果能在已知污染模型上检测到异常 lz*，simulation power 的具体数值不影响论文 claim。\\n  related_experiments:\\n  - exp_id: sim_001\\n    role: primary\\n    result: partial_pass\\n  depends_on:\\n  - D001\\n  - D002\\n  - D003\\n- id: D005\\n  date: 2026-05-20 08:21 UTC\\n  summary: 'Phase B Pass + 发现双侧检测需求: Model 3 MMLU 100% acc/lz*=+34.75 是全面污染信号，单侧检验漏检'\\n  rationale: Phase B 客观通过 pass 标准：所有 benchmark lz* SD >> 0.5（最小 ARC-C=2.59），且 MMLU/HellaSwag/GSM8K/HumanEval\\n    均有模型 lz* < -1.96。Reviewer 发现 Model 3 在 MMLU 上 acc=1.0/θ=0.777/lz*=+34.75——中等能力模型答对全部\\n    14042 题，统计上几乎不可能自然发生，是全面污染（memorized all items）的典型表现。但 lz* 为正极端值，单侧标准 lz* < -1.96\\n    完全漏检。同一模型在其他 benchmark lz* 显著为负（GSM8K=-15.71, HumanEval=-12.37），支持系统性污染假说。研究阶段必须引入双侧检测，Model\\n    3 将成为论文核心 case study。\\n  related_experiments:\\n  - exp_id: sim_001\\n    role: context\\n    result: partial_pass\\n  - exp_id: phase_b_personfit\\n    role: primary\\n    result: pass\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-20 08:40 UTC\\n  summary: Phase B 必须用 benchmark-specific θ (MLE)，不能用 PSN-IRT 全局 θ——全局 θ 导致 93.3%\\n    false flag\\n  rationale: 'Reviewer critical: exp-two-sided 用 |lz*|>1.96 在真实数据上 flag 了 56/60 cells（93.3%），远超预期\\n    5%。根因：PSN-IRT 的全局 θ 是跨 11 个 benchmark 的折中值，LLM 能力在不同 benchmark 上差异巨大（如 Gemini-1.5\\n    MMLU acc=1.0 但 HumanEval acc=0.54），全局 θ 系统性地在强项 benchmark 上低估、弱项上高估，产生 lz* 系统偏移。Phase\\n    A 模拟不受影响（模拟用的是单 benchmark 内 MLE θ）。修复：对每个 (model, benchmark) 用 MLE 从该 benchmark\\n    的 response vector 重估 θ_bench，再计算 lz*。这与 IDEA_BRIEF 原始设计一致（\\\"Per-benchmark person-fit\\n    to respect unidimensionality\\\"）。补充 empirical null (parametric bootstrap) 作为 robustness\\n    check + BH FDR 控制。calibration gap 本身是有价值的学术发现。'\\n  related_experiments:\\n  - exp_id: exp-two-sided\\n    role: primary\\n    result: critical_revision_needed\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-20 09:16 UTC\\n  summary: '采纳方向 B: real data 上 person-fit 绝对阈值失效（universal misfit），论文核心方法转向 controlled\\n    calibration (Δlz*)'\\n  rationale: exp-two-sided v2 结果：benchmark-specific θ + bootstrap null + BH FDR 仍\\n    flag 57/60 (95%)。根因不是 θ 校准而是 4PL model misfit——LLM response patterns 普遍违反 local\\n    independence 和 unidimensionality。三个方向评估：(A) relative ranking 需要更多模型(n=12 不够)，作为补充可行但非核心；(B)\\n    reframe 为 model misfit characterization + controlled calibration——用 exp-ctrl-contam\\n    建立 baseline misfit vs contaminated misfit 的 ground-truth delta，这使论文叙事更诚实更有深度；(C)\\n    MIRT/非参数 IRT 工程量过大且偏离 PSN-IRT 数据源。选择 B 为主路径。论文 story 演化：模拟建立理论检测力 → real data\\n    发现 universal misfit（calibration gap 本身是发现）→ controlled experiment 建立 Δlz* calibration\\n    → 实际检测通过 relative delta 而非绝对阈值。exp-ctrl-contam 从验证实验升级为核心方法。\\n  related_experiments:\\n  - exp_id: exp-two-sided\\n    role: primary\\n    result: negative_critical\\n  depends_on:\\n  - D006\\n\", \"total_chars\": 4526, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c307b40e-c339-454a-ac53-8b1e638c5575",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "0d71be0e-bf88-4d94-84ac-0c5c91fd01fd",
  "sourceToolAssistantUUID": "c307b40e-c339-454a-ac53-8b1e638c5575",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T09:20:58.661Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Rsf5EKMMkkdebc7Whhyaae`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d71be0e-bf88-4d94-84ac-0c5c91fd01fd",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaGJWkNwfJdKp2XzMqQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ae44a1c-fa9d-4188-9052-5e7c86aecd81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F72cwjGX7cdaNikcd6Zbo8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8878,
      "cache_read_input_tokens": 18379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8878,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
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

_source line 17 · 2026-05-20T09:20:58.671Z_

<details><summary>↩ Tool result · `toolu_01Rsf5EKMMkkdebc7Whhyaae`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper_framing.md\", \"content\": \"# Paper Framing — irt_personfit_contam\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\\n\\n## Core Claims (3 条)\\n\\n**Claim 1 (Minimal-Information Detection + Calibration Gap)**:\\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks). However, real LLM data exhibits universal IRT model misfit (local independence / unidimensionality violations), making absolute thresholds unreliable. We bridge this calibration gap via controlled contamination experiments that quantify the Δlz* between clean and contaminated models, enabling relative detection through contamination-induced misfit delta rather than absolute person-fit scores.\\n\\n**Claim 2 (Detection Characterization)**:\\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.\\n\\n**Claim 3 (Empirical Prevalence)**:\\nApplying IRT-FIT to publicly available LLM benchmark data reveals contamination patterns quantifiable for the first time via IRT — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence with model-level cross-benchmark anomaly profiles (Gemini-1.5 flagged on 4/5 benchmarks). Note: group-level cross-benchmark correlation is weak (n=12, most Spearman p>0.05); the claim is about individual model anomaly profiles, not population-level consistency.\\n\\n## Story Spine\\n\\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\\n\\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\\n\\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \\\"What can be detected from binary response patterns alone?\\\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks); (2) in real LLM data, universal IRT model misfit creates a calibration gap that prevents absolute threshold detection; (3) controlled contamination experiments bridge this gap by quantifying the misfit delta (Δlz*) between clean and contaminated models. The calibration gap itself is a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns, violating local independence assumptions.\\n\\n**Headline result template**: \\\"Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items). Real-world application reveals universal IRT model misfit in LLMs — we bridge this calibration gap via controlled experiments showing contamination induces a measurable Δlz* shift of X SD above natural misfit baseline.\\\"\\n\\n## Venue Fit Risks\\n\\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \\\"no new NLP model/technique\\\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\\n\\n## Anticipated Reviewer Concerns & Planned Responses\\n\\n| # | Concern | Response Strategy | Supporting Experiment |\\n|---|---------|------------------|----------------------|\\n| R1 | \\\"Just applying existing IRT to LLMs\\\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \\\"cross-domain\\\" from contribution to background. | — |\\n| R2 | \\\"No ground truth contamination labels\\\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\\n| R3 | \\\"Power too low for small benchmarks\\\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\\n| R4 | \\\"Only 12 models\\\" | Expand to Open LLM Leaderboard v1 models + newly evaluated models. | exp-leaderboard-audit |\\n| R5 | \\\"SFT generalization smooths signal\\\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\\n| R6 | \\\"Absolute lz* thresholds don't work on real data\\\" | Honest finding: universal model misfit makes absolute thresholds unreliable. Controlled calibration (Δlz*) solves this. The calibration gap itself is a contribution. | exp-ctrl-contam |\\n| R7 | \\\"Post-RL contamination?\\\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\\n| R8 | \\\"4PL vs 3PL — does d parameter matter?\\\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\\n\\n## Key Narrative Elements (from External Review)\\n\\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\\n2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.\\n3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).\\n4. **Scope precision** — Target: \\\"intentional SFT contamination / leaderboard gaming\\\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\\n\\n## Evidence Summary\\n\\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.\\n- **Calibration gap (D007)**: Absolute lz* thresholds flag 95% of (model, benchmark) cells — universal IRT model misfit, not contamination. Root cause: LLM responses violate local independence (knowledge clustering) and unidimensionality. Simulation-to-real-data gap is itself a finding.\\n- **Path forward**: Controlled experiments (exp-ctrl-contam) measure Δlz* between clean and contaminated models. Relative delta approach replaces absolute thresholds.\\n\", \"total_chars\": 7958, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ae44a1c-fa9d-4188-9052-5e7c86aecd81",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "99b85af8-9a5b-4584-88e8-5e72dd1efde9",
  "sourceToolAssistantUUID": "9ae44a1c-fa9d-4188-9052-5e7c86aecd81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T09:20:59.134Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011gQUXKv5waHeQJ8Co8dZ6n`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99b85af8-9a5b-4584-88e8-5e72dd1efde9",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaGJWkNwfJdKp2XzMqQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "445371d8-e441-4c77-963f-9ffe7dfe9c88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F72cwjGX7cdaNikcd6Zbo8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8878,
      "cache_read_input_tokens": 18379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8878,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
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

_source line 19 · 2026-05-20T09:20:59.143Z_

<details><summary>↩ Tool result · `toolu_011gQUXKv5waHeQJ8Co8dZ6n`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'irt_personfit_contam'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "445371d8-e441-4c77-963f-9ffe7dfe9c88",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "97aedb1e-78c9-4ca8-a823-579fa0d4d548",
  "sourceToolAssistantUUID": "445371d8-e441-4c77-963f-9ffe7dfe9c88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T09:21:00.182Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XJ6NTNG4EkQHAXDQAWzGz3`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97aedb1e-78c9-4ca8-a823-579fa0d4d548",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaGJWkNwfJdKp2XzMqQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a70b967d-9c26-4ecf-978d-57194a1330c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F72cwjGX7cdaNikcd6Zbo8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8878,
      "cache_read_input_tokens": 18379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8878,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
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

_source line 21 · 2026-05-20T09:21:00.212Z_

<details><summary>↩ Tool result · `toolu_01XJ6NTNG4EkQHAXDQAWzGz3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-20T08:00:00Z'\\n  total_papers: 10\\ncategories:\\n  - key: irt-llm\\n    label: IRT for LLM Evaluation\\n  - key: contamination-detection\\n    label: Benchmark Contamination Detection\\n  - key: person-fit\\n    label: Person-Fit Statistics (Psychometrics)\\n  - key: post-rl-contamination\\n    label: Post-RL Contamination\\npapers:\\n  psnirt2026:\\n    title: \\\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\\\"\\n    authors: []\\n    year: 2026\\n    venue: AAAI 2026 Oral\\n    url: \\\"https://arxiv.org/abs/2505.15055\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: psnirt2026\\n    category: irt-llm\\n    role: foundation\\n    relevance: \\\"Provides calibrated 4PL item parameters (a,b,c,d) for 41,871 items across 11 benchmarks — the item bank our method builds on\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  atlas2025:\\n    title: \\\"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks\\\"\\n    authors: []\\n    year: 2025\\n    venue: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2511.04689\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: atlas2025\\n    category: irt-llm\\n    role: background\\n    relevance: \\\"ATLAS uses IRT for adaptive testing efficiency; related IRT-for-LLM work but not person-fit\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  constat2024:\\n    title: \\\"ConStat: Performance-Based Contamination Detection in Large Language Models\\\"\\n    authors: []\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: constat2024\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"Performance-based contamination detector — primary baseline; requires re-test with modified items\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  minkprob2024:\\n    title: \\\"Detecting Pretraining Data from Large Language Models\\\"\\n    authors: []\\n    year: 2024\\n    venue: ICLR 2024\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: minkprob2024\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"Min-K% Probability MIA-based detector — baseline; requires token probabilities (not black-box)\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  wang2025fragility:\\n    title: \\\"On The Fragility of Benchmark Contamination Detection in Reasoning Models\\\"\\n    authors: []\\n    year: 2025\\n    venue: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2510.02386\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: wang2025fragility\\n    category: post-rl-contamination\\n    role: foundation\\n    relevance: \\\"Shows all MIA-based detectors fail under post-RL contamination — motivates our black-box approach\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  selfcritique2026:\\n    title: \\\"Detecting Data Contamination from Reinforcement Learning Post-training\\\"\\n    authors: []\\n    year: 2026\\n    venue: ICLR 2026\\n    url: \\\"https://arxiv.org/abs/2510.09259\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: selfcritique2026\\n    category: post-rl-contamination\\n    role: direct-competitor\\n    relevance: \\\"Self-Critique detects post-RL contamination via entropy-sequence policy collapse — baseline for post-RL setting\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  codec2026:\\n    title: \\\"Detecting Data Contamination in LLMs via In-Context Learning\\\"\\n    authors: []\\n    year: 2026\\n    venue: ICLR 2026\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: codec2026\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"CoDeC measures ICL effects on memorized vs unseen data — baseline\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  sinharay2017:\\n    title: \\\"Which Statistic Should Be Used to Detect Item Preknowledge?\\\"\\n    authors: []\\n    year: 2017\\n    venue: JEBS\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: sinharay2017\\n    category: person-fit\\n    role: foundation\\n    relevance: \\\"Power analysis for preknowledge detection — peak detection at 10-30% preknowledge; core theoretical basis\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  karabatsos2003:\\n    title: \\\"Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics\\\"\\n    authors: []\\n    year: 2003\\n    venue: Applied Measurement in Education\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: karabatsos2003\\n    category: person-fit\\n    role: foundation\\n    relevance: \\\"Comprehensive comparison of 36 person-fit statistics — guides our choice of lz* as primary statistic\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  hong2021lzm:\\n    title: \\\"Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types\\\"\\n    authors: []\\n    year: 2021\\n    venue: Psychometrika\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: hong2021lzm\\n    category: person-fit\\n    role: method-component\\n    relevance: \\\"lzm multiscale aggregation for multidimensional constructs — our Level 2 aggregated contamination score\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\", \"total_chars\": 5591, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a70b967d-9c26-4ecf-978d-57194a1330c2",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "f1bbc69a-ebe2-4654-9c15-0f4e57209c9e",
  "sourceToolAssistantUUID": "a70b967d-9c26-4ecf-978d-57194a1330c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T09:21:01.084Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016ExnQatUvXK8GsBwMAtZSf`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1bbc69a-ebe2-4654-9c15-0f4e57209c9e",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaGJWkNwfJdKp2XzMqQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe1b7c8a-74c8-4b55-a028-64d3929fe12f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F72cwjGX7cdaNikcd6Zbo8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8878,
      "cache_read_input_tokens": 18379,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8878
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 393,
          "cache_read_input_tokens": 18379,
          "cache_creation_input_tokens": 8878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8878,
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

_source line 23 · 2026-05-20T09:21:01.094Z_

<details><summary>↩ Tool result · `toolu_016ExnQatUvXK8GsBwMAtZSf`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'irt_personfit_contam'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe1b7c8a-74c8-4b55-a028-64d3929fe12f",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "4c931212-1d10-4ce4-8873-8d75e0e6efd1",
  "sourceToolAssistantUUID": "fe1b7c8a-74c8-4b55-a028-64d3929fe12f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-20T09:21:03.873Z_

Now let me look at the actual paper/draft files and experiment artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c931212-1d10-4ce4-8873-8d75e0e6efd1",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaGk1BSUTzNWxie9mhL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f9a845b-51a0-43ed-8ed9-23eea5ad0a83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTceheE8vdB9fdyzrA3paW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5370,
      "cache_read_input_tokens": 27257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5370,
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

_source line 25 · 2026-05-20T09:21:04.389Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WXHk7K5pzdkjgHxwJ9tFxZ`</summary>

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
  "parentUuid": "8f9a845b-51a0-43ed-8ed9-23eea5ad0a83",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaGk1BSUTzNWxie9mhL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34fac21b-8a9b-4164-982c-7262dcd5a23a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTceheE8vdB9fdyzrA3paW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5370,
      "cache_read_input_tokens": 27257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5370,
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

_source line 26 · 2026-05-20T09:21:04.424Z_

<details><summary>↩ Tool result · `toolu_01WXHk7K5pzdkjgHxwJ9tFxZ`</summary>

```text
artifacts/dream_reports/dream_20260520T082549/best/paper.tex
artifacts/dream_reports/dream_20260520T082549/median/paper.tex
artifacts/dream_reports/dream_20260520T082549/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34fac21b-8a9b-4164-982c-7262dcd5a23a",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "81f28f71-463e-4426-b409-fb3210cb2ccf",
  "sourceToolAssistantUUID": "34fac21b-8a9b-4164-982c-7262dcd5a23a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T09:21:05.330Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Pj165UQKWHrASHsfpjsTBi`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81f28f71-463e-4426-b409-fb3210cb2ccf",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaGk1BSUTzNWxie9mhL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcabfe2e-15ef-40c0-880d-7aefb86d13ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTceheE8vdB9fdyzrA3paW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5370,
      "cache_read_input_tokens": 27257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5370,
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

_source line 28 · 2026-05-20T09:21:05.361Z_

<details><summary>↩ Tool result · `toolu_01Pj165UQKWHrASHsfpjsTBi`</summary>

```text
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/back.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/filesave.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/forward.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/hand.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/help.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/home.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/matplotlib.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/move.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/qt4_editor_options.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/subplots.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/zoom_to_rect.pdf
artifacts/dream_reports/dream_20260520T082549/best/paper.pdf
artifacts/dream_reports/dream_20260520T082549/median/paper.pdf
artifacts/dream_reports/dream_20260520T082549/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcabfe2e-15ef-40c0-880d-7aefb86d13ae",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "7f5bc5e5-7039-4766-9ce9-21058e82f5b7",
  "sourceToolAssistantUUID": "bcabfe2e-15ef-40c0-880d-7aefb86d13ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T09:21:05.691Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FKKpBx7yLttsJnbUcJgt5r`</summary>

```json
{
  "pattern": "artifacts/**/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f5bc5e5-7039-4766-9ce9-21058e82f5b7",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaGk1BSUTzNWxie9mhL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53b03e6b-a459-4099-a02f-fcc609a4e2b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTceheE8vdB9fdyzrA3paW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5370,
      "cache_read_input_tokens": 27257,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5370
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 27257,
          "cache_creation_input_tokens": 5370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5370,
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

_source line 30 · 2026-05-20T09:21:05.721Z_

<details><summary>↩ Tool result · `toolu_01FKKpBx7yLttsJnbUcJgt5r`</summary>

```text
artifacts/psn_irt_params/item_parameters_all.csv
artifacts/psn_irt_params/arc_c_params.csv
artifacts/psn_irt_params/gsm8k_params.csv
artifacts/psn_irt_params/hellaswag_params.csv
artifacts/psn_irt_params/humaneval_params.csv
artifacts/psn_irt_params/mmlu_params.csv
artifacts/psn_irt_data_report.md
artifacts/psn_irt_phase_b/combine.csv
artifacts/psn_irt_phase_b/student_abilities.csv
artifacts/code/__pycache__/irt_utils.cpython-314.pyc
artifacts/null_check_mini_test/humaneval_lz_star_hist.png
artifacts/null_check_mini_test/null_check_summary.json
artifacts/sim_001/data/null_check_summary.json
artifacts/simulation_results/simulation_summary.json
artifacts/sim_001/data/simulation_summary.json
artifacts/simulation_results/simulation_detailed.csv
artifacts/simulation_results/power_curves.png
artifacts/sim_001/chart/power_curves.png
artifacts/simulation_results/power_by_benchmark/humaneval_power_detail.png
artifacts/simulation_results/power_by_benchmark/arc_c_power_detail.png
artifacts/simulation_results/power_by_benchmark/gsm8k_power_detail.png
artifacts/simulation_results/power_by_benchmark/hellaswag_power_detail.png
artifacts/simulation_results/power_by_benchmark/mmlu_power_detail.png
artifacts/null_check_results/mmlu_lz_star_hist.png
artifacts/null_check_results/hellaswag_lz_star_hist.png
artifacts/null_check_results/gsm8k_lz_star_hist.png
artifacts/null_check_results/arc_c_lz_star_hist.png
artifacts/null_check_results/humaneval_lz_star_hist.png
artifacts/null_check_results/null_check_summary.json
artifacts/_project/data/personfit_matrix.csv
artifacts/phase_b_results/personfit_matrix.csv
artifacts/_project/report/personfit_summary.json
artifacts/phase_b_results/personfit_summary.json
artifacts/_project/chart/lz_star_MMLU.png
artifacts/phase_b_results/lz_star_MMLU.png
artifacts/phase_b_results/lz_star_HellaSwag.png
artifacts/phase_b_results/lz_star_GSM8K.png
artifacts/phase_b_results/lz_star_ARC-C.png
artifacts/phase_b_results/lz_star_HumanEval.png
artifacts/dream_reports/dream_20260520T082549/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260520T082549/logs/phase2_best_attempt0.log
artifacts/phase_b_two_sided/two_sided_flags.csv
artifacts/phase_b_two_sided/model_anomaly_profile.csv
artifacts/phase_b_two_sided/two_sided_summary.json
artifacts/phase_b_two_sided/two_sided_heatmap.png
artifacts/dream_reports/dream_20260520T082549/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260520T082549/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260520T082549/logs/phase2_worst_attempt1.log
artifacts/dream_reports/dream_20260520T082549/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T082549/best/experiment_data.json
artifacts/dream_reports/dream_20260520T082549/best/paper_framing.md
artifacts/dream_reports/dream_20260520T082549/best/paper.tex
artifacts/dream_reports/dream_20260520T082549/best/paper.aux
artifacts/dream_reports/dream_20260520T082549/best/paper.out
artifacts/dream_reports/dream_20260520T082549/best/paper.pdf
artifacts/dream_reports/dream_20260520T082549/best/paper.log
artifacts/dream_reports/dream_20260520T082549/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260520T082549/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T082549/median/experiment_data.json
artifacts/dream_reports/dream_20260520T082549/median/paper_framing.md
artifacts/dream_reports/dream_20260520T082549/median/paper.tex
artifacts/dream_reports/dream_20260520T082549/median/paper.aux
artifacts/dream_reports/dream_20260520T082549/median/paper.out
artifacts/dream_reports/dream_20260520T082549/median/paper.pdf
artifacts/dream_reports/dream_20260520T082549/median/paper.log
artifacts/dream_reports/dream_20260520T082549/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260520T082549/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T082549/worst/experiment_data.json
artifacts/dream_reports/dream_20260520T082549/worst/paper_framing.md
artifacts/_project/data/two_sided_detection_v2.py
artifacts/_project/data/personfit_matrix_v2.csv
artifacts/phase_b_two_sided_v2/personfit_matrix_v2.csv
artifacts/dream_reports/dream_20260520T082549/worst/paper.tex
artifacts/dream_reports/dream_20260520T082549/worst/paper.aux
artifacts/dream_reports/dream_20260520T082549/worst/paper.out
artifacts/dream_reports/dream_20260520T082549/worst/paper.pdf
artifacts/dream_reports/dream_20260520T082549/worst/paper.log
artifacts/dream_reports/dream_20260520T082549/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260520T082549/best/review_context.yaml
artifacts/dream_reports/dream_20260520T082549/logs/orchestrator.log
artifacts/extended_simulation/simulation_summary.json
artifacts/extended_simulation/simulation_detailed.csv
artifacts/extended_simulation/power_curves.png
artifacts/extended_simulation/power_by_benchmark/mmlu_power_detail.png
artifacts/extended_simulation/power_by_benchmark/hellaswag_power_detail.png
artifacts/extended_simulation/power_by_benchmark/gsm8k_power_detail.png
artifacts/extended_simulation/power_by_benchmark/arc_c_power_detail.png
artifacts/extended_simulation/power_by_benchmark/humaneval_power_detail.png
artifacts/_project/data/empirical_pvalues.csv
artifacts/phase_b_two_sided_v2/empirical_pvalues.csv
artifacts/_project/data/two_sided_summary_v2.json
artifacts/phase_b_two_sided_v2/two_sided_summary_v2.json
artifacts/_project/chart/lz_star_heatmap_v2.png
artifacts/phase_b_two_sided_v2/lz_star_heatmap_v2.png
artifacts/_project/report/analysis_report.md
artifacts/phase_b_two_sided_v2/analysis_report.md
artifacts/manifest.yaml
artifacts/dream_reports/dream_20260520T082549/best/review_report.md
artifacts/dream_reports/dream_20260520T082549/logs/review_best.log
artifacts/dream_reports/dream_20260520T082549/median/review_context.yaml
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53b03e6b-a459-4099-a02f-fcc609a4e2b3",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "3e369e15-15a1-46fb-998b-0101b17843ea",
  "sourceToolAssistantUUID": "53b03e6b-a459-4099-a02f-fcc609a4e2b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-20T09:21:08.649Z_

Let me read the "best" dream paper (which represents the paper being reviewed) and the review context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e369e15-15a1-46fb-998b-0101b17843ea",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaH5c9Hd8JsNPgYh9DX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1a99158-1ca6-408f-a52b-866147007bd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8C4mBM1nYgmUiyBZPmvd5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2823,
      "cache_read_input_tokens": 32627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2823,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 32 · 2026-05-20T09:21:09.229Z_

<details open><summary>🔧 Tool call — Read · `toolu_01URJtTiwVWn3LiqTsr26pCP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1a99158-1ca6-408f-a52b-866147007bd0",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaH5c9Hd8JsNPgYh9DX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a89afa75-e71b-4ff9-83db-20fe70a5c0ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8C4mBM1nYgmUiyBZPmvd5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2823,
      "cache_read_input_tokens": 32627,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2823
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 32627,
          "cache_creation_input_tokens": 2823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2823,
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

_source line 33 · 2026-05-20T09:21:09.532Z_

<details><summary>↩ Tool result · `toolu_01URJtTiwVWn3LiqTsr26pCP`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{tabularx}
9	\usepackage[margin=2.5cm]{geometry}
10	\usepackage{natbib}
11	\usepackage{hyperref}
12	\usepackage{xcolor}
13	\usepackage{array}
14	\usepackage{caption}
15	
16	\newcolumntype{R}{>{\raggedleft\arraybackslash}p{1.2cm}}
17	\newcolumntype{L}{>{\raggedright\arraybackslash}p{2.8cm}}
18	
19	\title{IRT-FIT: Detecting Benchmark Contamination in Large Language Models\\via Item Response Theory Person-Fit Statistics}
20	
21	\author{Anonymous}
22	\date{}
23	
24	\begin{document}
25	\maketitle
26	
27	% ============================================================
28	\begin{abstract}
29	Benchmark contamination undermines the reliability of LLM evaluation, yet all existing detection methods require privileged access---training data, token probabilities, model weights, or specially crafted prompts. We establish the \emph{minimal-information operating point} on the contamination detection frontier by repurposing Item Response Theory (IRT) person-fit statistics, which require only binary (correct/incorrect) response patterns. Our framework, \textbf{IRT-FIT}, introduces three contributions: (1) a two-sided detection framework capturing both partial contamination (aberrant patterns, $l_{z}^{*} \ll 0$) and full contamination (over-consistent patterns, $l_{z}^{*} \gg 0$); (2) a theoretical characterization showing detection power is a predictable function of benchmark size ($n_{\text{items}}$) and contamination level, with an analytically derivable inverted-U signal structure ($R^2=0.97$); and (3) a large-scale audit of 2{,}847 Open LLM Leaderboard models revealing a 12\% overall contamination flag rate. In controlled experiments with ground-truth contamination (QLoRA SFT on Qwen3.5-9B and Gemma-4-31B), IRT-FIT achieves AUROC 0.96 at 15\% contamination and 0.82 at 5\%---outperforming ConStat (0.83/0.61) and Min-K\%++ (0.88/0.72) while requiring strictly less information. The person-fit signal survives post-RL training (AUROC 0.92 after GRPO), whereas MIA-based methods degrade to near-chance (AUROC 0.54). IRT-FIT is the only method that simultaneously addresses partial, full, and post-RL contamination at the minimal-information level.
30	\end{abstract}
31	
32	% ============================================================
33	\section{Introduction}
34	\label{sec:intro}
35	
36	Benchmark contamination---the inclusion of evaluation data in training corpora---is a growing threat to LLM evaluation integrity. As training data scales to trillions of tokens and benchmarks proliferate, the probability of inadvertent or intentional overlap increases. This undermines the fundamental assumption that benchmark performance reflects genuine capability.
37	
38	Existing detection methods span a spectrum of information requirements. N-gram overlap methods require access to training data. Membership inference attacks (MIA) and Min-K\%++ \citep{shi2024detecting} require token-level log-probabilities. Time Travel probing \citep{oren2024proving} requires specially crafted prompts. ConStat \citep{dekoninck2024constat} requires the ability to re-test models on rephrased items. \citet{wang2025reassessing} demonstrate that all MIA-based methods fail under post-RL contamination, highlighting the fragility of token-level signals.
39	
40	A contaminated LLM answering benchmark questions is functionally analogous to an examinee with item preknowledge---a problem studied for decades in psychometrics under the rubric of \emph{person-fit analysis}. Person-fit statistics such as $l_z^*$ \citep{snijders2001person} detect aberrant response patterns: examinees who answer difficult items correctly while failing easy ones, or who answer all items correctly including those far beyond their estimated ability. These statistics require only binary response data and a calibrated item bank---precisely the information available from standard LLM benchmark evaluation.
41	
42	We introduce \textbf{IRT-FIT}, a framework that establishes the \emph{minimal-information operating point} on the contamination detection frontier. Our contributions are:
43	
44	\begin{enumerate}
45	    \item \textbf{Minimal-information detection.} We show that IRT person-fit statistics detect benchmark contamination using only binary response patterns, achieving AUROC 0.96 at 15\% contamination---outperforming methods requiring token probabilities or re-testing.
46	    \item \textbf{Theoretical characterization.} We derive an analytic power formula relating detection power to benchmark size and contamination level ($R^2=0.97$), and prove that the inverted-U signal structure has a predictable inflection point determined by item difficulty distributions.
47	    \item \textbf{Large-scale empirical evidence.} We audit 2{,}847 Open LLM Leaderboard models, revealing a 12\% contamination flag rate increasing from 6\% (2023 Q1) to 18\% (2024 Q1). We identify Gemini-1.5's 100\% MMLU accuracy as systematic contamination ($l_z^*=+34.75$, $\hat{\theta}=0.78$).
48	\end{enumerate}
49	
50	% ============================================================
51	\section{Background}
52	\label{sec:background}
53	
54	\subsection{Item Response Theory}
55	
56	IRT models the probability of a correct response as a function of examinee ability $\theta$ and item parameters. We adopt the four-parameter logistic (4PL) model:
57	\begin{equation}
58	P_i(\theta) = c_i + (d_i - c_i) \cdot \frac{1}{1 + e^{-a_i(\theta - b_i)}}
59	\label{eq:4pl}
60	\end{equation}
61	where $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is the guessing parameter, and $d_i$ is the feasibility (upper asymptote) parameter. The 3PL model is the special case $d_i=1$.
62	
63	\subsection{Person-Fit Statistics}
64	
65	The $l_z$ statistic \citep{drasgow1985appropriateness} measures the fit of an individual response pattern to the IRT model:
66	\begin{equation}
67	l_z = \frac{\sum_{i=1}^{n} \left[ x_i \log P_i(\hat{\theta}) + (1-x_i) \log(1-P_i(\hat{\theta})) \right] - E[l_0]}{SD[l_0]}
68	\end{equation}
69	where $x_i \in \{0,1\}$ is the response to item $i$ and $\hat{\theta}$ is the MLE of ability. \citet{snijders2001person} derived the corrected statistic $l_z^*$ that accounts for estimation error in $\hat{\theta}$, yielding $l_z^* \sim N(0,1)$ under the null hypothesis of model fit.
70	
71	% ============================================================
72	\section{Method: IRT-FIT}
73	\label{sec:method}
74	
75	\subsection{Two-Sided Detection Framework}
76	
77	Traditional person-fit analysis tests only $l_z^* < c_{\alpha}$ (aberrant patterns). We extend to two-sided testing because contamination produces two distinct signal regimes:
78	
79	\begin{itemize}
80	    \item \textbf{Partial contamination} ($l_z^* \ll 0$): The model memorizes a subset of items, answering difficult contaminated items correctly while failing easy non-contaminated items---an aberrant pattern.
81	    \item \textbf{Full contamination} ($l_z^* \gg 0$): The model memorizes all items, producing a response pattern that is \emph{over-consistent}---all items correct, including those far beyond estimated ability.
82	\end{itemize}
83	
84	We apply the two-sided test $|l_z^*| > c_{\alpha/2}$ with Benjamini--Hochberg FDR control for multiple comparisons across models and benchmarks.
85	
86	\subsection{Multiscale Aggregation ($l_{zm}$)}
87	
88	Following \citet{hong2021multiscale}, we aggregate per-benchmark $l_z^*$ values into a single model-level index:
89	\begin{equation}
90	l_{zm} = \frac{1}{\sqrt{K}} \sum_{k=1}^{K} |l_{z,k}^*|
91	\end{equation}
92	where $K$ is the number of benchmarks evaluated. Under the null, $l_{zm}$ is approximately standard normal (verified by Kolmogorov--Smirnov test, $p=0.312$).
93	
94	\subsection{Power Theory}
95	
96	Building on Snijders' variance formula, we derive the detection power as:
97	\begin{equation}
98	\text{power} \approx \Phi\!\left(\frac{\delta \sqrt{n}}{\sigma_{l_z^*}} - z_{\alpha}\right)
99	\label{eq:power}
100	\end{equation}
101	where $\delta = E[\log L_{\text{contam}} - \log L_{\text{clean}}]$ per item is the expected log-likelihood shift induced by contamination, and $n$ is the number of items. The inverted-U inflection point $c^*$ satisfies:
102	\begin{equation}
103	c^* = \arg\min_{c} \left| E_\theta\!\left[\sum_i f(x_i, P_i) \mid \text{contam}=c\right] - E_\theta\!\left[\sum_i f(x_i, P_i) \mid \text{contam}=0\right] \right|
104	\end{equation}
105	where $f(x_i, P_i) = x_i \log P_i + (1-x_i)\log(1-P_i)$.
106	
107	% ============================================================
108	\section{Controlled Contamination Experiments}
109	\label{sec:controlled}
110	
111	\subsection{Ground-Truth Contamination}
112	\label{sec:ctrl-contam}
113	
114	We inject known contamination via QLoRA SFT on two base models (Qwen3.5-9B and Gemma-4-31B), training on 0\%/5\%/10\%/15\%/25\%/50\% of MMLU items to establish a ground-truth contamination--$l_z^*$ mapping.
115	
116	\begin{table}[t]
117	\centering
118	\caption{Controlled contamination: $l_z^*$ by model and contamination level (MMLU).}
119	\label{tab:ctrl-contam}
120	\small
121	\begin{tabular}{llrrrr}
122	\toprule
123	\textbf{Model} & \textbf{Contam.} & \textbf{Acc.} & $\hat{\theta}$ & $l_z^*$ & \textbf{Flag} \\
124	\midrule
125	Qwen3.5-9B & 0\% & .721 & 1.42 & 0.08 & .047 \\
126	Qwen3.5-9B & 5\% & .738 & 1.51 & $-$3.72 & .82 \\
127	Qwen3.5-9B & 10\% & .756 & 1.59 & $-$6.45 & .94 \\
128	Qwen3.5-9B & 15\% & .764 & 1.63 & $-$8.91 & .97 \\
129	Qwen3.5-9B & 25\% & .787 & 1.71 & $-$11.34 & .99 \\
130	Qwen3.5-9B & 50\% & .831 & 1.89 & $-$4.82 & .87 \\
131	\midrule
132	Gemma-4-31B & 0\% & .793 & 1.81 & 0.15 & .041 \\
133	Gemma-4-31B & 5\% & .808 & 1.88 & $-$3.21 & .78 \\
134	Gemma-4-31B & 15\% & .831 & 1.97 & $-$7.63 & .95 \\
135	Gemma-4-31B & 50\% & .874 & 2.14 & $-$5.14 & .84 \\
136	\bottomrule
137	\end{tabular}
138	\end{table}
139	
140	\begin{table}[t]
141	\centering
142	\caption{Detection performance (AUROC) by contamination level.}
143	\label{tab:auroc}
144	\small
145	\begin{tabular}{lrrrr}
146	\toprule
147	\textbf{Contam.} & \textbf{Qwen} & \textbf{Gemma} & \textbf{Pooled} & \textbf{Cohen's $d$} \\
148	\midrule
149	5\% & 0.84 & 0.80 & 0.82 & 1.1 \\
150	10\% & 0.93 & 0.91 & 0.92 & 1.8 \\
151	15\% & 0.97 & 0.95 & 0.96 & 2.3 \\
152	25\% & 0.99 & 0.98 & 0.99 & 2.8 \\
153	50\% & 0.94 & 0.91 & 0.93 & 1.6 \\
154	\bottomrule
155	\end{tabular}
156	\end{table}
157	
158	Table~\ref{tab:ctrl-contam} shows a monotonic increase in $|l_z^*|$ from 0\% to 25\% contamination, followed by a decrease at 50\%---the inverted-U pattern. Both models exhibit consistent behavior (effect size difference $<$15\%), ruling out model-specific artifacts. False positive rate at $\alpha=0.05$ is well-calibrated: 0.047 (Qwen) and 0.041 (Gemma). The minimum detectable contamination level is 5\% (AUROC 0.82, Table~\ref{tab:auroc}).
159	
160	\begin{table}[t]
161	\centering
162	\caption{Contamination selectivity: accuracy change on contaminated vs.\ non-contaminated items (Qwen3.5-9B).}
163	\label{tab:selectivity}
164	\small
165	\begin{tabular}{lrrrr}
166	\toprule
167	\textbf{Contam.} & \multicolumn{2}{c}{\textbf{Contam.\ Items}} & \multicolumn{2}{c}{\textbf{Non-Contam.\ Items}} \\
168	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
169	 & Before & Lift & Before & Lift \\
170	\midrule
171	5\% & .56 & +.31 & .73 & +.014 \\
172	15\% & .54 & +.30 & .73 & +.018 \\
173	25\% & .55 & +.31 & .73 & +.024 \\
174	50\% & .57 & +.31 & .73 & +.037 \\
175	\bottomrule
176	\end{tabular}
177	\end{table}
178	
179	Table~\ref{tab:selectivity} confirms that SFT contamination is highly selective: accuracy on contaminated items increases by $\sim$31 percentage points, while non-contaminated items show only 1.4--3.7\% generalization. The generalization ratio is 0.12, far too small to smooth the aberrant pattern.
180	
181	\subsection{Inverted-U Signal Characterization}
182	\label{sec:inverted-u}
183	
184	We extend simulations to 60\%/75\%/90\%/100\% contamination levels, characterizing the complete inverted-U curve across four benchmarks.
185	
186	\begin{table}[t]
187	\centering
188	\caption{$l_z^*$ as a function of contamination level (mean $\pm$ SD, 100 replications).}
189	\label{tab:inverted-u}
190	\small
191	\begin{tabular}{lrrrr}
192	\toprule
193	\textbf{Contam.} & \textbf{MMLU} & \textbf{HSwag} & \textbf{GSM8K} & \textbf{ARC-C} \\
194	\midrule
195	0\% & 0.01 & 0.03 & $-$0.02 & 0.01 \\
196	5\% & $-$3.41 & $-$1.82 & $-$1.34 & $-$0.42 \\
197	10\% & $-$6.12 & $-$3.45 & $-$2.51 & $-$0.78 \\
198	15\% & $-$8.31 & $-$4.72 & $-$3.38 & $-$1.02 \\
199	25\% & $-$12.08 & $-$6.21 & $-$4.53 & $-$1.31 \\
200	50\% & $-$5.73 & $-$2.89 & $-$1.67 & $-$0.43 \\
201	60\% & $-$1.24 & 0.82 & $-$0.34 & 0.21 \\
202	75\% & 8.42 & 5.67 & 3.21 & 1.12 \\
203	90\% & 19.31 & 12.45 & 6.78 & 2.34 \\
204	100\% & 28.50 & 18.20 & 8.70 & 3.01 \\
205	\bottomrule
206	\end{tabular}
207	\end{table}
208	
209	\begin{table}[t]
210	\centering
211	\caption{Two-sided detection power at various contamination levels.}
212	\label{tab:two-sided-power}
213	\small
214	\begin{tabular}{lrrrr}
215	\toprule
216	\textbf{Contam.} & \textbf{MMLU} & \textbf{HSwag} & \textbf{GSM8K} & \textbf{ARC-C} \\
217	\midrule
218	5\% & .780 & .340 & .220 & .060 \\
219	15\% & .979 & .733 & .578 & .129 \\
220	25\% & .998 & .891 & .743 & .201 \\
221	50\% & .872 & .514 & .298 & .080 \\
222	75\% & .991 & .934 & .712 & .187 \\
223	100\% & 1.000 & .998 & .962 & .478 \\
224	\bottomrule
225	\end{tabular}
226	\end{table}
227	
228	Tables~\ref{tab:inverted-u} and \ref{tab:two-sided-power} reveal the inverted-U structure. The $l_z^*$ signal peaks negatively around 25\% contamination (MMLU: $-$12.08), crosses zero near 60--65\%, and becomes strongly positive at high contamination (100\%: +28.50). The inflection point varies by benchmark: 0.65 (MMLU), 0.60 (HellaSwag), 0.70 (GSM8K), consistent with differences in item difficulty distributions. Two-sided power dips at the inflection point (50\% contamination) but recovers for higher levels, whereas one-sided testing would have zero power above the inflection.
229	
230	\subsection{Power Theory Derivation}
231	\label{sec:power-theory}
232	
233	Equation~\ref{eq:power} predicts detection power as a function of $n_{\text{items}}$. Table~\ref{tab:power-theory} shows the theory fits simulation data with $R^2=0.97$.
234	
235	\begin{table}[t]
236	\centering
237	\caption{Theoretical vs.\ simulated power at 15\% contamination.}
238	\label{tab:power-theory}
239	\small
240	\begin{tabular}{rrrr}
241	\toprule
242	$n_{\text{items}}$ & \textbf{Predicted} & \textbf{Simulated} & \textbf{$|\Delta|$} \\
243	\midrule
244	100 & .089 & .092 & .003 \\
245	500 & .312 & .298 & .014 \\
246	1{,}000 & .491 & .503 & .012 \\
247	1{,}319 & .578 & .578 & .000 \\
248	5{,}000 & .862 & .851 & .011 \\
249	10{,}042 & .964 & .958 & .006 \\
250	14{,}042 & .981 & .979 & .002 \\
251	\bottomrule
252	\end{tabular}
253	\end{table}
254	
255	\begin{table}[t]
256	\centering
257	\caption{Inverted-U inflection point: predicted vs.\ observed.}
258	\label{tab:inflection}
259	\small
260	\begin{tabular}{lrrrr}
261	\toprule
262	\textbf{Benchmark} & $n$ & \textbf{Pred.} & \textbf{Obs.} & $|\Delta|$ \\
263	\midrule
264	MMLU & 14{,}042 & 0.64 & 0.65 & 0.01 \\
265	HellaSwag & 10{,}042 & 0.59 & 0.60 & 0.01 \\
266	GSM8K & 1{,}319 & 0.68 & 0.70 & 0.02 \\
267	ARC-C & 1{,}172 & 0.62 & 0.64 & 0.02 \\
268	HumanEval & 164 & 0.61 & 0.63 & 0.02 \\
269	\bottomrule
270	\end{tabular}
271	\end{table}
272	
273	\begin{table}[t]
274	\centering
275	\caption{Minimum $n_{\text{items}}$ for 80\% power at various contamination levels.}
276	\label{tab:min-n}
277	\small
278	\begin{tabular}{lrr}
279	\toprule
280	\textbf{Contam.} & \textbf{Theory} & \textbf{Simulation} \\
281	\midrule
282	5\% & 9{,}800 & 10{,}200 \\
283	10\% & 4{,}700 & 4{,}900 \\
284	15\% & 3{,}200 & 3{,}350 \\
285	25\% & 1{,}800 & 1{,}900 \\
286	\bottomrule
287	\end{tabular}
288	\end{table}
289	
290	Table~\ref{tab:inflection} shows the inflection point can be predicted from item difficulty distributions alone, with error $\leq$0.02. Table~\ref{tab:min-n} provides practitioners with concrete guidance: detecting 15\% contamination requires $\geq$3{,}200 items; detecting 5\% contamination requires $\geq$9{,}800 items. This explains why ARC-C (1{,}172 items) yields only 12.9\% power---not a method failure, but insufficient information.
291	
292	% ============================================================
293	\section{Comparisons and Robustness}
294	\label{sec:comparison}
295	
296	\subsection{Baseline Comparison}
297	\label{sec:baselines}
298	
299	\begin{table}[t]
300	\centering
301	\caption{Baseline comparison on controlled contamination ground truth.}
302	\label{tab:baseline}
303	\small
304	\begin{tabular}{llrrrr}
305	\toprule
306	\textbf{Method} & \textbf{Info Required} & \textbf{5\%} & \textbf{15\%} & \textbf{25\%} & \textbf{Type-I} \\
307	\midrule
308	IRT-FIT & binary & .82 & .96 & .99 & .042 \\
309	ConStat & binary + retest & .61 & .83 & .91 & .053 \\
310	Min-K\%++ & token log-probs & .72 & .88 & .95 & .048 \\
311	\bottomrule
312	\end{tabular}
313	\end{table}
314	
315	\begin{table}[t]
316	\centering
317	\caption{Detection frontier: information access vs.\ detection power (AUROC at 15\% contam.).}
318	\label{tab:frontier}
319	\small
320	\begin{tabular}{llrl}
321	\toprule
322	\textbf{Info Level} & \textbf{Method} & \textbf{AUROC} & \textbf{Scalability} \\
323	\midrule
324	Binary only & IRT-FIT & .96 & Any model w/ scores \\
325	Binary + retest & ConStat & .83 & Requires live access \\
326	Token probs & Min-K\%++ & .88 & Requires API logprobs \\
327	Training data & N-gram & --- & Requires training data \\
328	Weights & Probing & --- & Requires open weights \\
329	\bottomrule
330	\end{tabular}
331	\end{table}
332	
333	IRT-FIT achieves the highest AUROC while requiring the least information (Table~\ref{tab:baseline}). The advantage over ConStat (+0.13 at 15\%) stems from IRT-FIT's use of item-level response patterns rather than aggregate performance statistics. The advantage over Min-K\%++ (+0.08) is notable given that Min-K\%++ has access to richer token-level information. Table~\ref{tab:frontier} positions these results on the detection frontier.
334	
335	\subsection{Post-RL Robustness}
336	\label{sec:post-rl}
337	
338	\citet{wang2025reassessing} show that MIA-based methods fail after reinforcement learning. We test whether IRT-FIT survives post-RL by applying GRPO training to a contaminated Qwen3.5-9B (15\% MMLU SFT contamination).
339	
340	\begin{table}[t]
341	\centering
342	\caption{Pre- vs.\ post-RL person-fit (Qwen3.5-9B, 15\% MMLU contamination).}
343	\label{tab:post-rl}
344	\small
345	\begin{tabular}{lrrrrr}
346	\toprule
347	\textbf{Stage} & \textbf{Acc.} & $\hat{\theta}$ & $l_z^*$ & \textbf{AUROC} & \textbf{Power} \\
348	\midrule
349	Clean & .721 & 1.42 & 0.08 & --- & --- \\
350	Post-SFT & .764 & 1.63 & $-$8.91 & .96 & .97 \\
351	Post-SFT+GRPO & .776 & 1.71 & $-$7.12 & .92 & .91 \\
352	\bottomrule
353	\end{tabular}
354	\end{table}
355	
356	\begin{table}[t]
357	\centering
358	\caption{Person-fit vs.\ MIA: post-RL robustness comparison.}
359	\label{tab:post-rl-comparison}
360	\small
361	\begin{tabular}{lrrrl}
362	\toprule
363	\textbf{Method} & \textbf{Pre-RL} & \textbf{Post-RL} & \textbf{Retain.} & \textbf{Info} \\
364	\midrule
365	IRT-FIT & .96 & .92 & 96\% & binary \\
366	Min-K\%++ & .88 & .62 & 70\% & token probs \\
367	MIA (ref.) & .71 & .54 & 76\% & token probs + ref \\
368	\bottomrule
369	\end{tabular}
370	\end{table}
371	
372	GRPO reduces the $l_z^*$ signal by only 20\% ($-$8.91 $\to$ $-$7.12), retaining 96\% of AUROC (Table~\ref{tab:post-rl}). In contrast, MIA degrades to near-chance (0.54) because RL recalibrates token-level probability distributions while leaving binary response patterns largely intact (Table~\ref{tab:post-rl-comparison}). Item-level analysis confirms: contaminated items retain 97.6\% of their accuracy after GRPO (0.84 $\to$ 0.82), while non-contaminated items gain +1\%. RL changes \emph{how confident} the model is, but not \emph{whether it answers correctly} on memorized items.
373	
374	\subsection{4PL vs.\ 3PL Ablation}
375	\label{sec:ablation}
376	
377	\begin{table}[t]
378	\centering
379	\caption{4PL vs.\ 3PL detection performance.}
380	\label{tab:4pl-3pl}
381	\small
382	\begin{tabular}{lrrr}
383	\toprule
384	\textbf{Metric} & \textbf{4PL} & \textbf{3PL} & $\Delta$ \\
385	\midrule
386	AUROC @ 15\% & .960 & .910 & +.050 \\
387	False alarm ($\alpha$=.05) & .042 & .078 & $-$.036 \\
388	Power @ 15\% MMLU & .979 & .934 & +.045 \\
389	Power @ 5\% MMLU & .780 & .690 & +.090 \\
390	Mean $|l_z^*|$ clean & 0.83 & 1.17 & $-$0.34 \\
391	Mean $|l_z^*|$ contam.\ 15\% & 8.91 & 8.04 & +0.87 \\
392	\bottomrule
393	\end{tabular}
394	\end{table}
395	
396	\begin{table}[t]
397	\centering
398	\caption{Impact of $d$ parameter by item difficulty band.}
399	\label{tab:d-param}
400	\small
401	\begin{tabular}{lrrrr}
402	\toprule
403	\textbf{Difficulty} & $n$ & Mean $d$ & $\Delta l_z^*$ clean & $\Delta l_z^*$ contam. \\
404	\midrule
405	$<0.5$ (easy) & 2{,}814 & .97 & $-$0.08 & 0.12 \\
406	0.5--1.5 & 5{,}621 & .93 & $-$0.21 & 0.43 \\
407	1.5--2.5 & 3{,}891 & .89 & $-$0.38 & 0.78 \\
408	$>2.5$ (hard) & 1{,}716 & .82 & $-$0.67 & 1.45 \\
409	\bottomrule
410	\end{tabular}
411	\end{table}
412	
413	The 4PL model improves over 3PL primarily through better calibration on high-difficulty items (Table~\ref{tab:4pl-3pl}). The $d$ parameter absorbs natural variation in ceiling performance, reducing false alarms from 7.8\% to 4.2\%. The improvement concentrates on items with difficulty $>$2.5, where $d<0.85$ (Table~\ref{tab:d-param}). These are precisely the items where contamination signals are strongest, making the 4PL advantage non-trivial for detection despite modest overall improvement.
414	
415	\subsection{Multiscale $l_{zm}$ Statistic}
416	\label{sec:lzm}
417	
418	\begin{table}[t]
419	\centering
420	\caption{$l_{zm}$ results on PSN-IRT 12 models.}
421	\label{tab:lzm}
422	\small
423	\begin{tabular}{lrrl}
424	\toprule
425	\textbf{Model} & $l_{zm}$ & \textbf{Flag} & \textbf{\#Bench.\ Flagged} \\
426	\midrule
427	Gemini-1.5 & 18.42 & YES & 3 \\
428	GPT-4 & $-$0.87 & no & 0 \\
429	Llama-2-70B & $-$3.21 & YES & 1 \\
430	Claude-3-Opus & 0.42 & no & 0 \\
431	Mistral-7B & $-$2.45 & no & 0 \\
432	\bottomrule
433	\end{tabular}
434	\end{table}
435	
436	\begin{table}[t]
437	\centering
438	\caption{$l_{zm}$ vs.\ single-benchmark detection (15\% contamination).}
439	\label{tab:lzm-vs-single}
440	\small
441	\begin{tabular}{lrrr}
442	\toprule
443	\textbf{Method} & \textbf{AUROC} & \textbf{Power} & \textbf{FA Rate} \\
444	\midrule
445	$l_z^*$ (MMLU only) & .96 & .979 & .042 \\
446	$l_z^*$ (best single) & .96 & .979 & .042 \\
447	$l_{zm}$ (all benchmarks) & .98 & .990 & .037 \\
448	\bottomrule
449	\end{tabular}
450	\end{table}
451	
452	Cross-benchmark aggregation via $l_{zm}$ yields a modest but consistent improvement: AUROC increases from 0.96 to 0.98 (Table~\ref{tab:lzm-vs-single}). The gain comes from information pooling across $\sim$27K total items and from the fact that genuine contamination signals are correlated across benchmarks while false positives are not. The null distribution is well-calibrated (KS $p=0.312$). Gemini-1.5 produces the most extreme $l_{zm}=18.42$, aggregating both positive (MMLU) and negative (GSM8K, HumanEval) regime signals.
453	
454	% ============================================================
455	\section{Large-Scale Empirical Study}
456	\label{sec:empirical}
457	
458	\subsection{Two-Sided Detection on PSN-IRT Models}
459	\label{sec:two-sided}
460	
461	We apply the two-sided framework to 12 models from the PSN-IRT dataset across 5 benchmarks (60 model-benchmark pairs).
462	
463	\begin{table}[t]
464	\centering
465	\caption{Two-sided detection results (selected model-benchmark pairs).}
466	\label{tab:two-sided-results}
467	\small
468	\begin{tabular}{llrrl}
469	\toprule
470	\textbf{Model} & \textbf{Bench.} & $l_z^*$ & \textbf{Side} & \textbf{Flag} \\
471	\midrule
472	Gemini-1.5 & MMLU & +34.75 & positive & YES \\
473	Gemini-1.5 & GSM8K & $-$15.71 & negative & YES \\
474	Gemini-1.5 & HumanEval & $-$12.37 & negative & YES \\
475	GPT-4 & MMLU & $-$1.23 & --- & no \\
476	Llama-2-70B & ARC-C & $-$3.87 & negative & YES \\
477	\bottomrule
478	\end{tabular}
479	\end{table}
480	
481	\begin{table}[t]
482	\centering
483	\caption{One-sided vs.\ two-sided detection comparison (FDR = 0.05).}
484	\label{tab:one-vs-two}
485	\small
486	\begin{tabular}{lrrrr}
487	\toprule
488	\textbf{Method} & \textbf{Total} & \textbf{Partial} & \textbf{Full} & \textbf{FDR} \\
489	\midrule
490	One-sided ($l_z^* < c$) & 2 & 2 & 0 & .05 \\
491	Two-sided ($|l_z^*| > c$) & 4 & 2 & 2 & .05 \\
492	\bottomrule
493	\end{tabular}
494	\end{table}
495	
496	Gemini-1.5 on MMLU ($l_z^*=+34.75$, 95\% CI $[32.1, 37.4]$) exemplifies the positive regime: 100\% accuracy with estimated $\hat{\theta}=0.78$ indicates systematic memorization, not extraordinary ability (Table~\ref{tab:two-sided-results}). One-sided testing completely misses this signal and the two additional flagged models at the positive extreme (Table~\ref{tab:one-vs-two}).
497	
498	\subsection{Leaderboard Audit}
499	\label{sec:leaderboard}
500	
501	We run inference on 2{,}847 models from Open LLM Leaderboard v1, computing $l_z^*$ for each model-benchmark pair (18.5 GPU-hours total).
502	
503	\begin{table}[t]
504	\centering
505	\caption{Leaderboard audit summary.}
506	\label{tab:leaderboard}
507	\small
508	\begin{tabular}{lrrrrr}
509	\toprule
510	\textbf{Bench.} & $n$ & \textbf{Neg.} & \textbf{Pos.} & \textbf{Rate} & \textbf{Med.\ $l_z^*$} \\
511	\midrule
512	MMLU & 2{,}847 & 312 & 115 & .15 & $-$6.73 \\
513	HSwag & 2{,}847 & 198 & 58 & .09 & $-$4.21 \\
514	ARC-C & 2{,}847 & 142 & 57 & .07 & $-$3.12 \\
515	GSM8K & 2{,}182 & 178 & 63 & .11 & $-$5.42 \\
516	Overall & 2{,}847 & 255 & 87 & .12 & --- \\
517	\bottomrule
518	\end{tabular}
519	\end{table}
520	
521	\begin{table}[t]
522	\centering
523	\caption{Contamination rate by time period.}
524	\label{tab:temporal}
525	\small
526	\begin{tabular}{lrrr}
527	\toprule
528	\textbf{Period} & \textbf{Models} & \textbf{Flagged} & \textbf{Rate} \\
529	\midrule
530	2023 Q1--Q2 & 487 & 29 & .06 \\
531	2023 Q3--Q4 & 891 & 98 & .11 \\
532	2024 Q1--Q2 & 1{,}103 & 198 & .18 \\
533	2024 Q3+ & 366 & 51 & .14 \\
534	\bottomrule
535	\end{tabular}
536	\end{table}
537	
538	\begin{table}[t]
539	\centering
540	\caption{Most anomalous models (top 3 by $|l_z^*|$).}
541	\label{tab:top-anomalous}
542	\small
543	\begin{tabular}{llrrrl}
544	\toprule
545	\textbf{Model} & \textbf{Bench.} & \textbf{Acc.} & $l_z^*$ & \textbf{Side} & \textbf{Params} \\
546	\midrule
547	anon-7b-v3 & MMLU & .847 & $-$22.4 & neg & 7B \\
548	llm-ft-2b & MMLU & .912 & +18.7 & pos & 2B \\
549	bench-tuned-3b & GSM8K & .891 & $-$17.3 & neg & 3B \\
550	\bottomrule
551	\end{tabular}
552	\end{table}
553	
554	The audit reveals 342 flagged models (12\% overall), with MMLU most affected at 15\% (Table~\ref{tab:leaderboard}). Contamination rates increase from 6\% in early 2023 to 18\% in early 2024 (Table~\ref{tab:temporal}), consistent with the proliferation of benchmark-tuned models on the leaderboard. Table~\ref{tab:top-anomalous} shows the most extreme cases, including a 2B-parameter model achieving 91.2\% MMLU accuracy ($l_z^*=+18.7$) and a 7B model with $l_z^*=-22.4$. Cross-benchmark consistency is 34\%: about one-third of flagged models show anomalies on multiple benchmarks.
555	
556	\subsection{Additional Benchmarks: BBH and MATH}
557	\label{sec:extra-bench}
558	
559	\begin{table}[t]
560	\centering
561	\caption{Power analysis across all 7 benchmarks (15\% contamination).}
562	\label{tab:power-all}
563	\small
564	\begin{tabular}{lrrrr}
565	\toprule
566	\textbf{Benchmark} & $n$ & \textbf{Sim.} & \textbf{Pred.} & \textbf{5\%} \\
567	\midrule
568	HumanEval & 164 & .243 & .231 & .07 \\
569	ARC-C & 1{,}172 & .129 & .142 & .04 \\
570	GSM8K & 1{,}319 & .578 & .561 & .22 \\
571	MATH & 5{,}000 & .840 & .830 & .44 \\
572	BBH & 6{,}511 & .890 & .880 & .52 \\
573	HellaSwag & 10{,}042 & .733 & .748 & .34 \\
574	MMLU & 14{,}042 & .979 & .981 & .78 \\
575	\bottomrule
576	\end{tabular}
577	\end{table}
578	
579	Adding BBH (6{,}511 items) and MATH (5{,}000 items) fills the power gap between GSM8K and HellaSwag (Table~\ref{tab:power-all}). All seven benchmarks fall within 1--2\% of theoretical predictions, further validating the power formula. ARC-C is a notable outlier: its power (0.129) is much lower than GSM8K (0.578) despite similar $n_{\text{items}}$ (1{,}172 vs.\ 1{,}319), indicating that item discrimination quality also affects power---a factor captured by the $\delta$ term in Equation~\ref{eq:power}.
580	
581	\subsection{MMLU Domain-Level Analysis}
582	\label{sec:domain}
583	
584	\begin{table}[t]
585	\centering
586	\caption{MMLU domain-level $l_z^*$: Gemini-1.5 vs.\ GPT-4 (selected domains).}
587	\label{tab:domain}
588	\small
589	\begin{tabular}{lrrrrr}
590	\toprule
591	\textbf{Domain} & $n$ & \multicolumn{2}{c}{\textbf{Gemini-1.5}} & \multicolumn{2}{c}{\textbf{GPT-4}} \\
592	\cmidrule(lr){3-4} \cmidrule(lr){5-6}
593	 & & Acc. & $l_z^*$ & Acc. & $l_z^*$ \\
594	\midrule
595	abstract\_algebra & 100 & 1.00 & +0.83 & .73 & $-$0.42 \\
596	prof\_medicine & 272 & 1.00 & +4.21 & .85 & +0.67 \\
597	hs\_mathematics & 270 & 1.00 & +2.14 & .41 & $-$1.23 \\
598	college\_chem & 100 & 1.00 & +0.91 & .47 & +0.31 \\
599	miscellaneous & 783 & 1.00 & +7.89 & .87 & +0.42 \\
600	clinical\_know & 265 & 1.00 & +3.87 & .79 & $-$0.18 \\
601	\bottomrule
602	\end{tabular}
603	\end{table}
604	
605	\begin{table}[t]
606	\centering
607	\caption{Domain-level power as a function of $n_{\text{items}}$.}
608	\label{tab:domain-power}
609	\small
610	\begin{tabular}{lrrr}
611	\toprule
612	$n_{\text{items}}$ \textbf{bin} & \textbf{Domains} & \textbf{Power} & \textbf{Pred.} \\
613	\midrule
614	100--150 & 22 & .18 & .17 \\
615	150--300 & 21 & .31 & .33 \\
616	300--600 & 9 & .52 & .50 \\
617	600--1{,}000 & 3 & .64 & .67 \\
618	$>$1{,}000 & 2 & .72 & .74 \\
619	\bottomrule
620	\end{tabular}
621	\end{table}
622	
623	Gemini-1.5 achieves 100\% accuracy across all 57 MMLU domains, with uniformly positive $l_z^*$ values ranging from +0.8 to +12.3 (Table~\ref{tab:domain}). This uniformity rules out the innocent explanation that Gemini-1.5 is simply exceptionally strong in certain domains---no model genuinely excels equally across abstract algebra, clinical knowledge, and high school mathematics without occasionally erring. GPT-4, by contrast, shows normally distributed $l_z^*$ (SD=0.82) with zero domains flagged. The 57 MMLU domains provide 57 additional validation points for the power theory (Table~\ref{tab:domain-power}), with predicted power matching observed power within 2--3 percentage points across all domain size bins.
624	
625	% ============================================================
626	\section{Related Work}
627	\label{sec:related}
628	
629	\paragraph{Benchmark contamination detection.}
630	\citet{shi2024detecting} introduce Min-K\%++ for membership inference using token-level likelihood. \citet{oren2024proving} propose Time Travel testing via prompting. \citet{dekoninck2024constat} use performance consistency across rephrased items. \citet{dong2024generalization} study generalization-based detection. \citet{wang2025reassessing} show all MIA-based methods fail post-RL. Our work establishes a strictly lower information requirement.
631	
632	\paragraph{IRT for LLMs.}
633	\citet{polo2024tinybenchmarks} use IRT for efficient benchmarking. \citet{gu2024psnirt} calibrate 4PL IRT models on LLM response data (PSN-IRT). We build on PSN-IRT's item parameters but pivot from benchmarking to contamination detection via person-fit analysis.
634	
635	\paragraph{Person-fit in psychometrics.}
636	\citet{drasgow1985appropriateness} introduce $l_z$; \citet{snijders2001person} derive the corrected $l_z^*$. \citet{meijer2001methodology} survey applications including cheating detection. \citet{hong2021multiscale} propose multiscale aggregation. We are the first to apply person-fit statistics to LLM evaluation.
637	
638	% ============================================================
639	\section{Conclusion}
640	\label{sec:conclusion}
641	
642	We introduced IRT-FIT, a framework that detects benchmark contamination using only binary response patterns---the minimal-information operating point on the detection frontier. Three findings stand out: (1) person-fit statistics achieve AUROC 0.96 at 15\% contamination, surpassing methods requiring token probabilities or re-testing; (2) detection power follows a predictable analytic function of benchmark size ($R^2=0.97$), with the inverted-U signal structure theoretically derivable from item difficulty distributions; (3) a leaderboard-scale audit of 2{,}847 models reveals 12\% overall contamination rates, increasing from 6\% to 18\% over 2023--2024.
643	
644	The person-fit signal survives post-RL training (AUROC 0.92 after GRPO) while MIA degrades to near-chance (0.54), because binary response patterns are robust to the probability recalibration that RL induces. IRT-FIT is the only method that simultaneously addresses partial contamination (aberrant patterns), full contamination (over-consistent patterns), and post-RL contamination at the minimal-information level.
645	
646	\paragraph{Limitations.}
647	Detection power depends on benchmark size: benchmarks with fewer than $\sim$3{,}200 items have limited power at 15\% contamination ($<$80\%). The method targets intentional SFT-style contamination and leaderboard gaming; gradual pretraining exposure that yields smooth capability improvement is not in scope. The 4PL IRT model assumes unidimensionality, which may not hold for heterogeneous benchmarks.
648	
649	% ============================================================
650	\bibliographystyle{plainnat}
651	\begin{thebibliography}{20}
652	
653	\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}
654	Jasper Dekoninck, Mark Niklas M{\"u}ller, and Martin Vechev.
655	\newblock ConStat: Performance-based contamination detection in large language models.
656	\newblock In \emph{NeurIPS}, 2024.
657	
658	\bibitem[Dong et~al.(2024)]{dong2024generalization}
659	Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, and Ge Li.
660	\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.
661	\newblock In \emph{ACL}, 2024.
662	
663	\bibitem[Drasgow et~al.(1985)]{drasgow1985appropriateness}
664	Fritz Drasgow, Michael~V. Levine, and Mary~E. Williams.
665	\newblock Appropriateness measurement with polychotomous item response models and standardized indices.
666	\newblock \emph{British Journal of Mathematical and Statistical Psychology}, 38(1):67--86, 1985.
667	
668	\bibitem[Gu et~al.(2024)]{gu2024psnirt}
669	Guanyu Gu, Yixiao Li, and Yun-Fei Liu.
670	\newblock PSN-IRT: A psychometric benchmark calibration framework for large language models.
671	\newblock In \emph{AAAI}, 2024.
672	
673	\bibitem[Hong et~al.(2021)]{hong2021multiscale}
674	Sophia Hong, David~J. Lin, and Ying Cheng.
675	\newblock Multiscale person-fit statistics.
676	\newblock \emph{Applied Psychological Measurement}, 45(6):417--434, 2021.
677	
678	\bibitem[Meijer and Sijtsma(2001)]{meijer2001methodology}
679	Rob~R. Meijer and Klaas Sijtsma.
680	\newblock Methodology review: Evaluating person fit.
681	\newblock \emph{Applied Psychological Measurement}, 25(2):107--135, 2001.
682	
683	\bibitem[Oren et~al.(2024)]{oren2024proving}
684	Yonatan Oren, Nicole Meister, Niladri~S. Chatterji, Faisal Ladhak, and Tatsunori Hashimoto.
685	\newblock Proving test set contamination in black-box language models.
686	\newblock In \emph{ICLR (Spotlight)}, 2024.
687	
688	\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}
689	Felipe~Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin.
690	\newblock tinyBenchmarks: evaluating LLMs with fewer examples.
691	\newblock In \emph{ICML}, 2024.
692	
693	\bibitem[Shi et~al.(2024)]{shi2024detecting}
694	Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.
695	\newblock Detecting pretraining data from large language models.
696	\newblock In \emph{ICLR}, 2024.
697	
698	\bibitem[Snijders(2001)]{snijders2001person}
699	Tom~A.B. Snijders.
700	\newblock Asymptotic null distribution of person fit statistics with estimated item parameters.
701	\newblock \emph{Psychometrika}, 66(3):331--342, 2001.
702	
703	\bibitem[Wang et~al.(2025)]{wang2025reassessing}
704	Cheng Wang, Yiwei Wang, Bryan Hooi, and Yujun Cai.
705	\newblock Reassessing contamination detection: MIA fails under post-RL training.
706	\newblock \emph{arXiv preprint arXiv:2501.xxxxx}, 2025.
707	
708	\end{thebibliography}
709	
710	\end{document}
711	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a89afa75-e71b-4ff9-83db-20fe70a5c0ff",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "4fc6dade-fcfc-4fec-84b1-4e0df49dda14",
  "sourceToolAssistantUUID": "a89afa75-e71b-4ff9-83db-20fe70a5c0ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T09:21:15.052Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LcniU6PisjoyJyzDQ9yMeB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fc6dade-fcfc-4fec-84b1-4e0df49dda14",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaHMzsmqcg7wjhu9mGx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "549100db-662d-4a88-850c-c7f919d8b3b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tf3Q4vQjLKNoFchE4qNBhp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15310,
      "cache_read_input_tokens": 35450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15310,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 35 · 2026-05-20T09:21:15.340Z_

<details><summary>↩ Tool result · `toolu_01LcniU6PisjoyJyzDQ9yMeB`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。三条 claim 均有 ground-truth 支撑：(1) minimal-information
2	  operating point 经控制实验确认——仅 binary 数据即可在 5% 污染水平检测，AUROC>0.93；(2) power ∝ n_items
3	  有解析公式， inverted-U 从经验观察升级为理论命题，拐点位置可预测；(3) Gemini-1.5 case study + leaderboard audit
4	  构成大规模实证贡献。Post-RL 实验直接回应 Wang et al.，形成"MIA 失效但 person-fit 存活"的对比叙事。 Headline: "IRT-FIT
5	  是唯一在 minimal-information 条件下同时解决 partial/full/post-RL 污染的方法"。 EMNLP 主会议无需调整 claim
6	  强度。
7	
8	  '
9	imagined_experiments:
10	- name: Two-Sided Detection Framework
11	  plan_id: exp-two-sided
12	  description: '基于 Phase B personfit_matrix.csv，实现 |lz*| > threshold 双侧检测框架， 含 bootstrap
13	    CI 和 BH-FDR 控制。验证 Gemini-1.5 case study 中正侧信号。
14	
15	    '
16	  expected_results:
17	    gemini15_mmlu_lz_star: 34.75
18	    gemini15_mmlu_lz_star_bootstrap_95ci: '[32.1, 37.4]'
19	    gemini15_gsm8k_lz_star: -15.71
20	    gemini15_humaneval_lz_star: -12.37
21	    two_sided_flagged_models_at_fdr_0.05: 4
22	    one_sided_flagged_models_at_fdr_0.05: 2
23	    incremental_detection_gain_two_vs_one_sided: 2 additional models flagged (Gemini-1.5
24	      on MMLU, 1 other high-perf model)
25	    optimal_negative_threshold_alpha_0.05: -2.81
26	    optimal_positive_threshold_alpha_0.05: 3.24
27	    positive_regime_models: Gemini-1.5 (MMLU), possibly Yi-34B or similar near-ceiling
28	      model
29	    negative_regime_models: Gemini-1.5 (GSM8K, HumanEval), Llama-2-70B (ARC-C)
30	  result_rationale: 'Gemini-1.5 的 MMLU 100% 正确率对应 θ=0.78（远低于满分所需能力），产生极端正侧 lz*=+34.75。
31	    这是因为 full contamination 导致模型在所有 item 上正确，包括远超其真实能力的难题—— response pattern 过度一致（over-consistent），与真正高能力模型的"偶尔失误"模式不符。
32	    负侧信号来自 partial contamination：模型在已污染的难题上正确、在未污染的易题上错误， 产生 aberrant pattern（lz*
33	    << 0）。双侧框架捕获这两类互补信号， 单侧框架只能捕获负侧（partial），遗漏正侧（full）。Bootstrap CI 窄是因为 MMLU 有 14K
34	    items， lz* 的抽样方差 ∝ 1/n_items。FDR 控制在 12 模型 × 5 benchmarks = 60 次检验下仍能保持 power，
35	    因为真阳性的 lz* 绝对值远超阈值（效应量极大）。
36	
37	    '
38	  tables:
39	  - name: 'Table 1: Two-Sided Detection Results (Phase B, 12 Models × 5 Benchmarks)'
40	    columns:
41	    - model
42	    - benchmark
43	    - accuracy
44	    - theta_hat
45	    - lz_star
46	    - side
47	    - flagged_bh_fdr_005
48	    - bootstrap_95ci
49	    key_rows:
50	    - - Gemini-1.5
51	      - MMLU
52	      - 1.0
53	      - 0.78
54	      - 34.75
55	      - positive
56	      - 'YES'
57	      - '[32.1, 37.4]'
58	    - - Gemini-1.5
59	      - GSM8K
60	      - 0.946
61	      - 2.41
62	      - -15.71
63	      - negative
64	      - 'YES'
65	      - '[-17.2, -14.3]'
66	    - - Gemini-1.5
67	      - HumanEval
68	      - 0.878
69	      - 1.92
70	      - -12.37
71	      - negative
72	      - 'YES'
73	      - '[-14.1, -10.8]'
74	    - - GPT-4
75	      - MMLU
76	      - 0.864
77	      - 2.15
78	      - -1.23
79	      - —
80	      - 'no'
81	      - '[-2.1, -0.4]'
82	    - - Llama-2-70B
83	      - ARC-C
84	      - 0.673
85	      - 1.08
86	      - -3.87
87	      - negative
88	      - 'YES'
89	      - '[-5.2, -2.6]'
90	  - name: 'Table 2: One-Sided vs Two-Sided Detection Comparison'
91	    columns:
92	    - method
93	    - total_flagged
94	    - partial_contam_detected
95	    - full_contam_detected
96	    - FDR_control
97	    key_rows:
98	    - - one-sided (lz* < threshold)
99	      - 2
100	      - 2
101	      - 0
102	      - '0.05'
103	    - - two-sided (|lz*| > threshold)
104	      - 4
105	      - 2
106	      - 2
107	      - '0.05'
108	  figures_description:
109	  - 'Fig 1: lz* heatmap (12 models × 5 benchmarks)，color diverging at 0，标注双侧阈值线。Gemini-1.5
110	    MMLU 为极端红色（正侧），GSM8K/HumanEval 为极端蓝色（负侧）。'
111	  - 'Fig 2: Bootstrap distribution of lz* for Gemini-1.5 MMLU，显示 CI 远离零点，p-value 极小。'
112	  analysis: '双侧框架是论文的关键方法论贡献。Phase B 数据直接证明单侧检测的盲区：Gemini-1.5 在 MMLU 上的 full contamination
113	    产生正侧信号，传统 person-fit（只看负侧 aberrance）完全遗漏。 这不仅是技术改进，而是揭示了污染信号的双重机制——partial contamination
114	    产生 aberrant pattern （答对难题、答错易题），full contamination 产生 over-consistent pattern（所有题都对，包括不该对的）。
115	    Bootstrap CI 和 FDR 控制确保结论在多重比较下依然稳健。
116	
117	    '
118	- name: Extended Simulation (Inverted-U Characterization)
119	  plan_id: exp-extended-sim
120	  description: '扩展 Phase A 模拟至 60%/75%/90%/100% contamination levels， 修复 100% contamination
121	    的 MLE boundary 处理，精确刻画 inverted-U 拐点。
122	
123	    '
124	  expected_results:
125	    inverted_u_inflection_point_mmlu: 0.65
126	    inverted_u_inflection_point_hellaswag: 0.6
127	    inverted_u_inflection_point_gsm8k: 0.7
128	    inverted_u_inflection_ci_range: '[0.55, 0.75]'
129	    lz_star_at_inflection_mmlu: -0.12
130	    lz_star_at_100pct_contam_mmlu: 28.5
131	    lz_star_at_100pct_contam_hellaswag: 18.2
132	    lz_star_at_100pct_contam_gsm8k: 8.7
133	    negative_peak_lz_at_15pct_mmlu: -8.3
134	    negative_peak_lz_at_25pct_mmlu: -12.1
135	    zero_crossing_contam_level_mmlu: 0.63
136	    zero_crossing_contam_level_hellaswag: 0.58
137	    nan_rate_after_boundary_fix: 0.0
138	    power_at_5pct_contam_mmlu: 0.78
139	    power_at_5pct_contam_hellaswag: 0.34
140	  result_rationale: 'Inverted-U 的物理机制：低污染（<15%）时，少量 hard items 被答对产生 aberrant pattern（lz*
141	    < 0）， 信号随污染比例增强；中等污染（~40-60%）时，被污染 items 的 "全部答对" 开始被 IRT 模型解释为 "该模型能力更高"，θ 估计上移，lz*
142	    绝对值开始减小——因为 response pattern 变得可以被高 θ 解释； 拐点（~65% for MMLU）处 lz* ≈ 0，pattern 恰好可被某个
143	    θ 值完美拟合；超过拐点后， 模型在几乎所有 items 上正确但 θ 估计仍有上界（受 non-contaminated items 约束）， 导致 over-consistent
144	    pattern（lz* > 0）。拐点位置取决于 benchmark 的 item difficulty 分布： MMLU 有大量高难度 items（14K
145	    items 中 ~30% difficulty > 2.0），需要更高污染比例才能 让 pattern 显得 "合理"，所以拐点在 0.65。GSM8K 难度更集中，拐点在
146	    0.70。 100% contamination 的 lz* 大小与 n_items 正相关（MMLU > HellaSwag > GSM8K）， 因为 lz*
147	    的分子累加了所有 item 的 log-likelihood 偏差。 MLE boundary fix 后 NaN 消失，因为 θ 被 cap 在 4.0，lz*
148	    仍可计算（只是值更极端）。
149	
150	    '
151	  tables:
152	  - name: 'Table 3: lz* as a Function of Contamination Level (Mean ± SD, 100 Replications)'
153	    columns:
154	    - contam_level
155	    - mmlu_lz_mean
156	    - mmlu_lz_sd
157	    - hellaswag_lz_mean
158	    - gsm8k_lz_mean
159	    - arc_c_lz_mean
160	    key_rows:
161	    - - 0%
162	      - 0.01
163	      - 1.02
164	      - 0.03
165	      - -0.02
166	      - 0.01
167	    - - 5%
168	      - -3.41
169	      - 1.15
170	      - -1.82
171	      - -1.34
172	      - -0.42
173	    - - 10%
174	      - -6.12
175	      - 1.28
176	      - -3.45
177	      - -2.51
178	      - -0.78
179	    - - 15%
180	      - -8.31
181	      - 1.41
182	      - -4.72
183	      - -3.38
184	      - -1.02
185	    - - 25%
186	      - -12.08
187	      - 1.67
188	      - -6.21
189	      - -4.53
190	      - -1.31
191	    - - 50%
192	      - -5.73
193	      - 2.14
194	      - -2.89
195	      - -1.67
196	      - -0.43
197	    - - 60%
198	      - -1.24
199	      - 2.31
200	      - 0.82
201	      - -0.34
202	      - 0.21
203	    - - 75%
204	      - 8.42
205	      - 2.53
206	      - 5.67
207	      - 3.21
208	      - 1.12
209	    - - 90%
210	      - 19.31
211	      - 2.87
212	      - 12.45
213	      - 6.78
214	      - 2.34
215	    - - 100%
216	      - 28.5
217	      - 3.12
218	      - 18.2
219	      - 8.7
220	      - 3.01
221	  - name: 'Table 4: Two-Sided Power at Various Contamination Levels'
222	    columns:
223	    - contam_level
224	    - mmlu_power
225	    - hellaswag_power
226	    - gsm8k_power
227	    - arc_c_power
228	    key_rows:
229	    - - 5%
230	      - 0.78
231	      - 0.34
232	      - 0.22
233	      - 0.06
234	    - - 15%
235	      - 0.979
236	      - 0.733
237	      - 0.578
238	      - 0.129
239	    - - 25%
240	      - 0.998
241	      - 0.891
242	      - 0.743
243	      - 0.201
244	    - - 50%
245	      - 0.872
246	      - 0.514
247	      - 0.298
248	      - 0.08
249	    - - 75%
250	      - 0.991
251	      - 0.934
252	      - 0.712
253	      - 0.187
254	    - - 100%
255	      - 1.0
256	      - 0.998
257	      - 0.962
258	      - 0.478
259	  figures_description:
260	  - 'Fig 3: Inverted-U 曲线——lz* mean vs contamination level，5 benchmarks 分色。标注 zero-crossing
261	    点和拐点位置，shaded area 为 ±1 SD。MMLU 曲线最深、拐点最右。'
262	  - 'Fig 4: Two-sided power vs contamination level，显示 U 型 power 曲线（中间有 dip 但不到 0）。对比
263	    one-sided power 在高污染时 drop to 0。'
264	  analysis: 'Inverted-U 的完整刻画是 Claim 2 的核心证据。拐点位置在 [0.55, 0.75] 范围内与 benchmark difficulty
265	    分布相关——这为后续理论推导提供了经验基准。关键发现：two-sided power 在拐点附近 有 dip 但不跌至零（因为 lz* 的 SD 在拐点处也增大，部分
266	    replications 仍超阈值）， 而 one-sided power 在高污染区完全失效。100% contamination 修复后产生极端正侧 lz*，
267	    与 Phase B Gemini-1.5 的经验数据定量一致（模拟 28.5 vs 实测 34.75，差异来自 Gemini-1.5 的真实 θ 分布与模拟假设不完全匹配）。
268	
269	    '
270	- name: Controlled Contamination Experiment
271	  plan_id: exp-ctrl-contam
272	  description: '在 Qwen3.5-9B 和 Gemma-4-31B 上，QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark
273	    items，建立 ground-truth contamination → lz* 映射。
274	
275	    '
276	  expected_results:
277	    ctrl_contam_auroc_at_15pct: 0.96
278	    ctrl_contam_auroc_at_5pct: 0.82
279	    ctrl_contam_auroc_at_25pct: 0.99
280	    ctrl_contam_min_detectable_level: 0.05
281	    ctrl_contam_lz_effect_size_cohens_d_at_15pct: 2.3
282	    ctrl_contam_lz_effect_size_cohens_d_at_5pct: 1.1
283	    qwen_clean_lz_star_mmlu: 0.08
284	    qwen_5pct_lz_star_mmlu: -3.72
285	    qwen_10pct_lz_star_mmlu: -6.45
286	    qwen_15pct_lz_star_mmlu: -8.91
287	    qwen_25pct_lz_star_mmlu: -11.34
288	    qwen_50pct_lz_star_mmlu: -4.82
289	    gemma_clean_lz_star_mmlu: 0.15
290	    gemma_5pct_lz_star_mmlu: -3.21
291	    gemma_15pct_lz_star_mmlu: -7.63
292	    gemma_50pct_lz_star_mmlu: -5.14
293	    accuracy_lift_at_15pct_contam_qwen: 0.043
294	    accuracy_lift_at_15pct_contam_gemma: 0.038
295	    sft_generalization_ratio: 0.12
296	    contaminated_items_accuracy_lift: 0.31
297	    non_contaminated_items_accuracy_change: 0.014
298	    false_positive_rate_at_alpha_0.05: 0.038
299	  result_rationale: 'SFT contamination 在 binary response 层面产生强 person-misfit 信号的原因：QLoRA
300	    SFT 直接 优化被注入 items 的 loss，导致这些 items 的正确率大幅上升（+31% on contaminated items）， 而未注入
301	    items 仅有微弱泛化（+1.4%）。这种"选择性提升"在 IRT 模型看来是 aberrant—— 模型在某些 hard items 上突然正确，但在同难度的
302	    non-contaminated items 上仍然错误。 泛化效应仅 12% 的原因：QLoRA 只更新 adapter weights（~0.5% 参数），且
303	    benchmark items 的格式高度标准化（MCQA），SFT 学到的是特定 item 的 answer pattern 而非领域知识。 Cohen''s
304	    d = 2.3 at 15% 说明效应量巨大——clean 和 contaminated 的 lz* 分布几乎不重叠。 AUROC 0.96 at 15%
305	    意味着随机抽一对 clean/contaminated 模型，96% 概率能正确区分。 5% contamination 仍可检测（AUROC 0.82）是因为
306	    MMLU 有 14K items，5% = 700 items 被污染， 足以在 lz* 累积中产生显著偏移。FPR 0.038 < 0.05 说明 null
307	    distribution 校准良好。 两个 base model 结果一致（效应量差 <15%）说明信号不依赖于特定模型架构。
308	
309	    '
310	  tables:
311	  - name: 'Table 5: Controlled Contamination — lz* by Model and Contamination Level
312	      (MMLU)'
313	    columns:
314	    - model
315	    - contam_level
316	    - accuracy
317	    - theta_hat
318	    - lz_star_mean
319	    - lz_star_sd
320	    - flagged_rate_alpha005
321	    key_rows:
322	    - - Qwen3.5-9B
323	      - 0%
324	      - 0.721
325	      - 1.42
326	      - 0.08
327	      - 0.97
328	      - 0.047
329	    - - Qwen3.5-9B
330	      - 5%
331	      - 0.738
332	      - 1.51
333	      - -3.72
334	      - 1.21
335	      - 0.82
336	    - - Qwen3.5-9B
337	      - 10%
338	      - 0.756
339	      - 1.59
340	      - -6.45
341	      - 1.34
342	      - 0.94
343	    - - Qwen3.5-9B
344	      - 15%
345	      - 0.764
346	      - 1.63
347	      - -8.91
348	      - 1.42
349	      - 0.97
350	    - - Qwen3.5-9B
351	      - 25%
352	      - 0.787
353	      - 1.71
354	      - -11.34
355	      - 1.58
356	      - 0.99
357	    - - Qwen3.5-9B
358	      - 50%
359	      - 0.831
360	      - 1.89
361	      - -4.82
362	      - 2.08
363	      - 0.87
364	    - - Gemma-4-31B
365	      - 0%
366	      - 0.793
367	      - 1.81
368	      - 0.15
369	      - 0.94
370	      - 0.041
371	    - - Gemma-4-31B
372	      - 5%
373	      - 0.808
374	      - 1.88
375	      - -3.21
376	      - 1.18
377	      - 0.78
378	    - - Gemma-4-31B
379	      - 15%
380	      - 0.831
381	      - 1.97
382	      - -7.63
383	      - 1.38
384	      - 0.95
385	    - - Gemma-4-31B
386	      - 50%
387	      - 0.874
388	      - 2.14
389	      - -5.14
390	      - 2.01
391	      - 0.84
392	  - name: 'Table 6: Detection Performance (AUROC) by Contamination Level'
393	    columns:
394	    - contam_level
395	    - auroc_qwen
396	    - auroc_gemma
397	    - auroc_pooled
398	    - cohens_d_pooled
399	    key_rows:
400	    - - 5%
401	      - 0.84
402	      - 0.8
403	      - 0.82
404	      - 1.1
405	    - - 10%
406	      - 0.93
407	      - 0.91
408	      - 0.92
409	      - 1.8
410	    - - 15%
411	      - 0.97
412	      - 0.95
413	      - 0.96
414	      - 2.3
415	    - - 25%
416	      - 0.99
417	      - 0.98
418	      - 0.99
419	      - 2.8
420	    - - 50%
421	      - 0.94
422	      - 0.91
423	      - 0.93
424	      - 1.6
425	  - name: 'Table 7: Contamination Selectivity — Accuracy Change on Contaminated vs
426	      Non-Contaminated Items'
427	    columns:
428	    - contam_level
429	    - contam_items_acc_before
430	    - contam_items_acc_after
431	    - contam_items_lift
432	    - non_contam_items_acc_before
433	    - non_contam_items_acc_after
434	    - non_contam_items_lift
435	    key_rows:
436	    - - 5%
437	      - 0.56
438	      - 0.87
439	      - 0.31
440	      - 0.73
441	      - 0.74
442	      - 0.014
443	    - - 15%
444	      - 0.54
445	      - 0.84
446	      - 0.3
447	      - 0.73
448	      - 0.75
449	      - 0.018
450	    - - 25%
451	      - 0.55
452	      - 0.86
453	      - 0.31
454	      - 0.73
455	      - 0.76
456	      - 0.024
457	    - - 50%
458	      - 0.57
459	      - 0.88
460	      - 0.31
461	      - 0.73
462	      - 0.77
463	      - 0.037
464	  figures_description:
465	  - 'Fig 5: lz* vs contamination level scatter (Qwen + Gemma, MMLU)，叠加模拟 inverted-U
466	    理论曲线。实测数据点落在理论预测 ±1 SD 内。'
467	  - 'Fig 6: ROC 曲线 at 5%/15%/25% contamination，三条曲线叠在一起，标注 AUROC 值。'
468	  - 'Fig 7: Item-level accuracy heatmap，contaminated items (sorted by difficulty)
469	    vs non-contaminated items，展示 SFT 的选择性提升效应。'
470	  analysis: '控制实验是论文最关键的 ground-truth 证据。核心发现：(1) SFT 污染在 binary response 层面 产生强烈且可检测的
471	    person-misfit 信号，Cohen''s d > 2 at 15% contamination； (2) 泛化效应仅 1-4%，远不足以平滑 aberrant
472	    pattern——这直接回应了 R5 审稿意见； (3) 两个不同架构/规模的 base model 给出一致结果，排除模型特异性； (4) 5% contamination
473	    即可检测（AUROC 0.82），确立 minimal detectable level。 50% contamination 的 lz* 绝对值回落验证了
474	    inverted-U，与扩展模拟定量一致。
475	
476	    '
477	- name: Power Theory Derivation
478	  plan_id: exp-power-theory
479	  description: '推导 power 与 n_items 的解析关系，基于 Snijders (2001) lz* 方差公式， 验证理论曲线与模拟数据的拟合度，将
480	    inverted-U 升级为理论命题。
481	
482	    '
483	  expected_results:
484	    power_theory_r_squared: 0.97
485	    power_formula: power ≈ Φ(δ·√n / σ_lz* − z_α) where δ = E[log L_contam − log L_clean]
486	      per item
487	    inverted_u_inflection_formula: c* = argmin_c |E_θ[Σ_i (x_i·log P_i + (1−x_i)·log(1−P_i))
488	      | contam=c] − E_θ[...| contam=0]|
489	    predicted_inflection_mmlu: 0.64
490	    predicted_inflection_hellaswag: 0.59
491	    predicted_inflection_gsm8k: 0.68
492	    observed_inflection_mmlu: 0.65
493	    observed_inflection_hellaswag: 0.6
494	    observed_inflection_gsm8k: 0.7
495	    inflection_prediction_error: 0.02
496	    power_at_n100_15pct_predicted: 0.089
497	    power_at_n1000_15pct_predicted: 0.491
498	    power_at_n5000_15pct_predicted: 0.862
499	    power_at_n14000_15pct_predicted: 0.981
500	    min_n_for_80pct_power_at_15pct: 3200
501	    min_n_for_80pct_power_at_5pct: 9800
502	  result_rationale: 'Snijders (2001) 证明了在正确指定的 IRT 模型下 lz* ~ N(0,1)。当注入 contamination
503	    时， lz* 的期望偏移量 δ 可以解析计算：每个被污染 item 对 log-likelihood 的贡献偏差为 log P_i(θ_true) − log
504	    P_i(θ_estimated)，其中 θ_estimated 被 contaminated items 上推。 对 n 个 items 中 c·n 个被污染的情况，总偏移
505	    ∝ c·n·δ_per_item，而 lz* 的标准差 ∝ √n。 因此 power ≈ Φ(c·√n·δ_per_item/σ − z_α)，这是一个关于
506	    c 和 n 的可预测函数。 R² = 0.97 的原因：理论假设（IRT 模型正确指定、θ 的 MLE 一致性）在模拟中近似成立， 但现实中参数估计有误差、4PL
507	    模型有轻微 misfit，导致不完美拟合。 Inverted-U 的拐点可以从 item difficulty 分布的分位数推导：当 contaminated
508	    items 的正确率 被提升到 1.0 时，如果这些 items 的 difficulty 覆盖了 IRT scale 的某个区间， θ 的 MLE 会被推到一个特定位置，使得
509	    response pattern 看起来 "最合理" 的 contamination 比例 就是拐点。MMLU difficulty 分布偏宽（SD ≈ 1.8），拐点偏右（0.64）；GSM8K
510	    difficulty 更集中 （SD ≈ 1.2），拐点偏右（0.68）是因为 difficulty 水平更高。 理论预测的拐点与观测值的误差仅 0.02，验证了解析公式的有效性。
511	
512	    '
513	  tables:
514	  - name: 'Table 8: Theoretical vs Simulated Power (15% Contamination)'
515	    columns:
516	    - n_items
517	    - predicted_power
518	    - simulated_power
519	    - absolute_error
520	    key_rows:
521	    - - 100
522	      - 0.089
523	      - 0.092
524	      - 0.003
525	    - - 500
526	      - 0.312
527	      - 0.298
528	      - 0.014
529	    - - 1000
530	      - 0.491
531	      - 0.503
532	      - 0.012
533	    - - 1319
534	      - 0.578
535	      - 0.578
536	      - 0.0
537	    - - 5000
538	      - 0.862
539	      - 0.851
540	      - 0.011
541	    - - 10042
542	      - 0.964
543	      - 0.958
544	      - 0.006
545	    - - 14042
546	      - 0.981
547	      - 0.979
548	      - 0.002
549	  - name: 'Table 9: Inverted-U Inflection Point — Predicted vs Observed'
550	    columns:
551	    - benchmark
552	    - n_items
553	    - difficulty_sd
554	    - predicted_inflection
555	    - observed_inflection
556	    - abs_error
557	    key_rows:
558	    - - MMLU
559	      - 14042
560	      - 1.83
561	      - 0.64
562	      - 0.65
563	      - 0.01
564	    - - HellaSwag
565	      - 10042
566	      - 1.52
567	      - 0.59
568	      - 0.6
569	      - 0.01
570	    - - GSM8K
571	      - 1319
572	      - 1.21
573	      - 0.68
574	      - 0.7
575	      - 0.02
576	    - - ARC-C
577	      - 1172
578	      - 1.45
579	      - 0.62
580	      - 0.64
581	      - 0.02
582	    - - HumanEval
583	      - 164
584	      - 1.67
585	      - 0.61
586	      - 0.63
587	      - 0.02
588	  - name: 'Table 10: Minimum n_items for 80% Power at Various Contamination Levels'
589	    columns:
590	    - contam_level
591	    - min_n_theoretical
592	    - min_n_simulated
593	    key_rows:
594	    - - 5%
595	      - 9800
596	      - 10200
597	    - - 10%
598	      - 4700
599	      - 4900
600	    - - 15%
601	      - 3200
602	      - 3350
603	    - - 25%
604	      - 1800
605	      - 1900
606	  figures_description:
607	  - 'Fig 8: Power vs n_items 理论曲线（连续线）叠加 5 benchmarks 的模拟数据点（散点）。多条曲线对应不同 contamination
608	    levels (5%/10%/15%/25%)。'
609	  - 'Fig 9: Inverted-U 理论预测曲线 vs 模拟数据，标注拐点位置与 CI。'
610	  - 'Fig 10: Power landscape heatmap (n_items × contam_level)，颜色编码 power，标注 80% power
611	    等高线。'
612	  analysis: 'Power 理论将 Claim 2 从经验观察升级为可预测的定量关系。解析公式给出了 practitioner 的 直接指导：要检测 15%
613	    污染需要 ≥3200 items，检测 5% 污染需要 ≥9800 items。 这解释了为什么 ARC-C (1172 items) 的 power 只有
614	    12.9%——不是方法失败，而是信息不足。 Inverted-U 的理论推导是方法论贡献的核心：它不仅解释了为什么存在拐点， 还能从 item difficulty
615	    分布预测拐点位置，误差仅 1-2 个百分点。
616	
617	    '
618	- name: Leaderboard Audit (Large-Scale Scan)
619	  plan_id: exp-leaderboard-audit
620	  description: 'Open LLM Leaderboard v1 大规模扫描，获取 per-item response logs， 对所有可用模型计算
621	    person-fit，绘制 per-benchmark 污染率随时间趋势。
622	
623	    '
624	  expected_results:
625	    leaderboard_models_scanned: 2847
626	    leaderboard_models_with_per_item_logs: 0
627	    leaderboard_models_rerun_inference: 2847
628	    total_gpu_hours_inference: 18.5
629	    leaderboard_flagged_rate_overall: 0.12
630	    leaderboard_flagged_rate_mmlu: 0.15
631	    leaderboard_flagged_rate_hellaswag: 0.09
632	    leaderboard_flagged_rate_arc_c: 0.07
633	    leaderboard_flagged_rate_gsm8k: 0.11
634	    flagged_models_total: 342
635	    flagged_two_sided_positive: 87
636	    flagged_two_sided_negative: 255
637	    contamination_trend_increasing: true
638	    contamination_rate_2023q1: 0.06
639	    contamination_rate_2023q3: 0.11
640	    contamination_rate_2024q1: 0.18
641	    cross_benchmark_consistent_flag_rate: 0.34
642	    top_flagged_model_lz_star: -22.4
643	  result_rationale: 'Per-item response logs 在 HuggingFace 上不直接公开（Leaderboard v1 只存
644	    aggregate scores）， 因此需要对可获取权重的模型重新跑推理。受 GPU 预算限制（20 hrs），选择 <7B 参数模型 优先扫描，覆盖 2847
645	    个模型（占 Leaderboard v1 总量的 ~40%）。 12% flagged rate 的来源：Leaderboard v1 时期（2023-2024）是
646	    benchmark gaming 高峰期， 大量模型通过 SFT 在 benchmark items 上训练以获取高排名。MMLU 受影响最严重（15%）
647	    因为它是 Leaderboard 的核心排名指标且训练数据广泛可获得。 时间趋势显示 2023 Q1 flagged rate 仅 6%，到 2024 Q1
648	    升至 18%—— 与社区对 benchmark contamination 问题认知的时间线一致（Contamination in the wild 2024
649	    等论文）。 正侧 flagged（87 个）主要是 MMLU 上的 "suspicious near-ceiling" 模型， 负侧 flagged（255
650	    个）主要是 partial contamination 的小模型。 跨 benchmark 一致 flag rate 34% 说明约 1/3 的 flagged
651	    模型在多个 benchmark 上同时异常—— 这些是最可信的 contamination 案例。
652	
653	    '
654	  tables:
655	  - name: 'Table 11: Leaderboard Audit Summary'
656	    columns:
657	    - benchmark
658	    - models_scanned
659	    - flagged_negative
660	    - flagged_positive
661	    - flagged_rate
662	    - median_lz_star_flagged
663	    key_rows:
664	    - - MMLU
665	      - 2847
666	      - 312
667	      - 115
668	      - 0.15
669	      - -6.73
670	    - - HellaSwag
671	      - 2847
672	      - 198
673	      - 58
674	      - 0.09
675	      - -4.21
676	    - - ARC-C
677	      - 2847
678	      - 142
679	      - 57
680	      - 0.07
681	      - -3.12
682	    - - GSM8K
683	      - 2182
684	      - 178
685	      - 63
686	      - 0.11
687	      - -5.42
688	    - - Overall (any benchmark)
689	      - 2847
690	      - 255
691	      - 87
692	      - 0.12
693	      - —
694	  - name: 'Table 12: Contamination Rate by Time Period'
695	    columns:
696	    - period
697	    - models_in_period
698	    - flagged_count
699	    - flagged_rate
700	    key_rows:
701	    - - 2023 Q1-Q2
702	      - 487
703	      - 29
704	      - 0.06
705	    - - 2023 Q3-Q4
706	      - 891
707	      - 98
708	      - 0.11
709	    - - 2024 Q1-Q2
710	      - 1103
711	      - 198
712	      - 0.18
713	    - - 2024 Q3+
714	      - 366
715	      - 51
716	      - 0.14
717	  - name: 'Table 13: Top 10 Most Anomalous Models'
718	    columns:
719	    - model
720	    - benchmark
721	    - accuracy
722	    - theta
723	    - lz_star
724	    - side
725	    - params
726	    key_rows:
727	    - - anonymous-7b-v3
728	      - MMLU
729	      - 0.847
730	      - 1.23
731	      - -22.4
732	      - negative
733	      - 7B
734	    - - llm-finetune-2b
735	      - MMLU
736	      - 0.912
737	      - 1.45
738	      - 18.7
739	      - positive
740	      - 2B
741	    - - benchmark-tuned-3b
742	      - GSM8K
743	      - 0.891
744	      - 2.12
745	      - -17.3
746	      - negative
747	      - 3B
748	  figures_description:
749	  - 'Fig 11: 散点图——所有 2847 模型的 (accuracy, lz*) on MMLU。Flagged 模型标红，non-flagged 标灰。显示
750	    flagged 模型不仅是高 accuracy（也有中等 accuracy 但 aberrant pattern 的）。'
751	  - 'Fig 12: 时间趋势——每季度的 flagged rate，按 benchmark 分色。显示逐年上升趋势。'
752	  - 'Fig 13: Cross-benchmark consistency heatmap——flagged 模型在各 benchmark 上的 lz* 值，展示跨
753	    benchmark 污染的关联性。'
754	  analysis: 'Leaderboard audit 是 IRT-FIT 的 "killer app"——唯一只需要 binary response data
755	    的方法 才能做到如此规模的扫描。ConStat 需要 re-test（需要 live model access）， Min-K%++ 需要 token probabilities（需要
756	    logits），MIA 需要 training data reference。 2847 个模型的扫描中 12% flagged rate 意味着约 342
757	    个模型存在可疑的 benchmark 污染， 且这个比例随时间上升。这为社区提供了首个大规模、定量的 benchmark integrity 评估。 尽管未达到
758	    7000 个模型的上限预测，2847 个模型已是同类研究中最大规模。
759	
760	    '
761	- name: 4PL vs 3PL Ablation
762	  plan_id: exp-4pl-ablation
763	  description: '比较 4PL (with feasibility parameter d) 和 3PL(d=1) 下的检测灵敏度差异， 量化 d 参数对
764	    false alarm 和 detection power 的影响。
765	
766	    '
767	  expected_results:
768	    auroc_4pl_15pct: 0.96
769	    auroc_3pl_15pct: 0.91
770	    auroc_difference_15pct: 0.05
771	    false_alarm_rate_4pl: 0.042
772	    false_alarm_rate_3pl: 0.078
773	    power_4pl_15pct_mmlu: 0.979
774	    power_3pl_15pct_mmlu: 0.934
775	    power_difference_15pct_mmlu: 0.045
776	    mean_abs_lz_star_difference_clean: 0.34
777	    mean_abs_lz_star_difference_contam: 0.87
778	    d_parameter_mean_psn_irt: 0.91
779	    d_parameter_sd_psn_irt: 0.08
780	    items_where_d_matters_most: top-difficulty items (difficulty > 2.5) where d <
781	      0.85
782	  result_rationale: '4PL 的 d 参数（upper asymptote / feasibility parameter）建模了即使能力极高的考生
783	    也可能答错某些 items 的现象——在 LLM 场景中对应"某些 items 的表述/格式导致即使知道答案的模型也可能选错"。 当 d < 1 时，3PL(d=1)
784	    会高估高能力模型在这些 items 上的预期正确率， 导致其答错时产生过多的 "aberrant" 信号（false alarm 上升）。 4PL 通过让
785	    d < 1 吸收这种自然变异，减少了 false alarm（0.042 vs 0.078）。 对于 contaminated models，d < 1 的
786	    items 是区分度最高的：contaminated model 在这些 items 上 答对率接近 1.0（因为直接记住了答案），而 clean model
787	    的答对率被 d 压低。 因此 4PL 在 contaminated case 中效应量更大（lz* 偏差多 0.87），综合 AUROC 提升 0.05。
788	    差异主要集中在高难度 items（difficulty > 2.5）——这些 items 的 d 值通常更低， 因为它们的表述更复杂，即使知道正确答案也更容易因格式理解问题出错。
789	
790	    '
791	  tables:
792	  - name: 'Table 14: 4PL vs 3PL Detection Performance Comparison'
793	    columns:
794	    - metric
795	    - 4PL
796	    - 3PL(d=1)
797	    - difference
798	    key_rows:
799	    - - AUROC @ 15%
800	      - 0.96
801	      - 0.91
802	      - '+0.05'
803	    - - False Alarm Rate (α=0.05)
804	      - 0.042
805	      - 0.078
806	      - −0.036
807	    - - Power @ 15% MMLU
808	      - 0.979
809	      - 0.934
810	      - '+0.045'
811	    - - Power @ 5% MMLU
812	      - 0.78
813	      - 0.69
814	      - '+0.09'
815	    - - Mean |lz*| clean models
816	      - 0.83
817	      - 1.17
818	      - −0.34
819	    - - Mean |lz*| contam models (15%)
820	      - 8.91
821	      - 8.04
822	      - '+0.87'
823	  - name: 'Table 15: Impact of d Parameter by Item Difficulty Band'
824	    columns:
825	    - difficulty_band
826	    - n_items
827	    - mean_d
828	    - lz_star_diff_clean
829	    - lz_star_diff_contam
830	    key_rows:
831	    - - < 0.5 (easy)
832	      - 2814
833	      - 0.97
834	      - -0.08
835	      - 0.12
836	    - - 0.5–1.5
837	      - 5621
838	      - 0.93
839	      - -0.21
840	      - 0.43
841	    - - 1.5–2.5
842	      - 3891
843	      - 0.89
844	      - -0.38
845	      - 0.78
846	    - - '> 2.5 (hard)'
847	      - 1716
848	      - 0.82
849	      - -0.67
850	      - 1.45
851	  figures_description:
852	  - 'Fig 14: ROC 曲线对比——4PL vs 3PL at 5%/15% contamination。4PL 曲线始终在 3PL 上方。'
853	  - 'Fig 15: d parameter distribution (histogram) from PSN-IRT，标注 mean 和关键分位数。'
854	  analysis: '4PL vs 3PL 的差异统计显著但不是巨大的——这其实是好消息：它说明 person-fit 方法 对 IRT 模型选择有一定 robustness，3PL
855	    也能工作（AUROC 0.91），但 4PL 更优（AUROC 0.96）。 关键 insight：d 参数的影响集中在高难度 items 上，而这些 items
856	    恰好是 contamination 信号最强的区域（contaminated model 在难题上答对是最 aberrant 的）。因此 4PL 的精确建模
857	    在检测任务中有非平凡的价值。
858	
859	    '
860	- name: Baseline Comparison (ConStat, Min-K%++)
861	  plan_id: exp-baseline-comparison
862	  description: '在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs ConStat vs
863	    Min-K%++ 的 AUROC 和 Type-I error。
864	
865	    '
866	  expected_results:
867	    irt_fit_auroc_15pct: 0.96
868	    constat_auroc_15pct: 0.83
869	    min_k_pp_auroc_15pct: 0.88
870	    irt_fit_auroc_5pct: 0.82
871	    constat_auroc_5pct: 0.61
872	    min_k_pp_auroc_5pct: 0.72
873	    auroc_advantage_vs_constat_15pct: 0.13
874	    auroc_advantage_vs_minkpp_15pct: 0.08
875	    baseline_auroc_advantage_vs_constat: 0.1
876	    type_i_error_irt_fit: 0.042
877	    type_i_error_constat: 0.053
878	    type_i_error_min_k_pp: 0.048
879	    irt_fit_information_required: binary responses only
880	    constat_information_required: binary responses + re-test capability
881	    min_k_pp_information_required: token-level log-probabilities
882	    irt_fit_unique_advantage: operates without model access
883	  result_rationale: 'IRT-FIT 在 AUROC 上优于 ConStat 0.10-0.13 的原因有两方面： (1) Person-fit
884	    statistics 利用了完整的 item-level response pattern 信息——每个 item 的 difficulty、 discrimination、guessing、feasibility
885	    参数都参与 lz* 计算，而 ConStat 基于 aggregate performance 的一致性检验，信息利用效率更低； (2) ConStat 的
886	    re-test design 假设 contaminated model 在 re-test 时表现不一致， 但 SFT contamination 是永久性的（权重已改变），re-test
887	    分数几乎不变，削弱了 ConStat 的信号。 Min-K%++ 在 AUROC 上略低于 IRT-FIT（0.88 vs 0.96）但需要 token-level
888	    probabilities—— 信息需求更高。其信号来自 token-level memorization（contaminated items 的 token
889	    loss 更低）， 但 SFT 后的 token-level 信号会被 RL 和 decoding 过程扰动，不如 binary response 层面的
890	    person-fit 信号稳定。 Type-I error 都接近 nominal 0.05，说明三种方法的 null calibration 都合理。 关键叙事：IRT-FIT
891	    不仅性能更好，而且信息需求最低——这是 detection frontier 的核心论点。
892	
893	    '
894	  tables:
895	  - name: 'Table 16: Baseline Comparison — Detection Performance on Controlled Contamination'
896	    columns:
897	    - method
898	    - info_required
899	    - auroc_5pct
900	    - auroc_15pct
901	    - auroc_25pct
902	    - type_i_error
903	    key_rows:
904	    - - IRT-FIT (lz*, two-sided)
905	      - binary responses
906	      - 0.82
907	      - 0.96
908	      - 0.99
909	      - 0.042
910	    - - ConStat
911	      - binary + re-test
912	      - 0.61
913	      - 0.83
914	      - 0.91
915	      - 0.053
916	    - - Min-K%++
917	      - token log-probs
918	      - 0.72
919	      - 0.88
920	      - 0.95
921	      - 0.048
922	  - name: 'Table 17: Detection Frontier — Information Access vs Detection Power'
923	    columns:
924	    - information_level
925	    - method
926	    - auroc_15pct
927	    - scalability
928	    key_rows:
929	    - - binary responses only
930	      - IRT-FIT
931	      - 0.96
932	      - any model with public scores
933	    - - binary + re-test
934	      - ConStat
935	      - 0.83
936	      - requires live model access
937	    - - token probabilities
938	      - Min-K%++
939	      - 0.88
940	      - requires API with logprobs
941	    - - training data
942	      - n-gram overlap
943	      - —
944	      - requires training data access
945	    - - model weights
946	      - internal probing
947	      - —
948	      - requires open weights
949	  figures_description:
950	  - 'Fig 16: ROC 曲线三方对比，IRT-FIT / ConStat / Min-K%++，at 15% contamination。'
951	  - 'Fig 17: Detection frontier diagram——x 轴为 information access level (ordered)，y
952	    轴为 AUROC，标注各方法位置。IRT-FIT 在最左下角（最少信息，高 AUROC）。'
953	  analysis: 'Baseline comparison 直接支撑 Claim 1（minimal-information operating point）。IRT-FIT
954	    在信息需求最低的条件下取得了最高的 AUROC——这不是因为 person-fit 比 MIA 更好（在等信息条件下 Min-K%++ 可能更强），而是因为
955	    person-fit 从 binary data 中提取了最大信号量。 Detection frontier diagram 是一个有力的可视化，直接展示了方法论贡献的核心。
956	
957	    '
958	- name: Multiscale lzm Statistic
959	  plan_id: exp-multiscale-lzm
960	  description: '实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021），跨 benchmark 聚合 lz*，
961	    在 PSN-IRT 12 模型 + 控制实验模型上验证。
962	
963	    '
964	  expected_results:
965	    lzm_auroc_15pct: 0.98
966	    lzm_vs_single_benchmark_auroc_gain: 0.02
967	    lzm_cross_benchmark_correlation: 0.67
968	    gemini15_lzm: 18.42
969	    gpt4_lzm: -0.87
970	    clean_model_lzm_mean: 0.03
971	    clean_model_lzm_sd: 0.91
972	    contam_model_lzm_mean_15pct: -7.23
973	    lzm_null_ks_p: 0.312
974	    lzm_power_at_15pct_pooled: 0.99
975	  result_rationale: 'lzm 将多个 benchmark 的 lz* 标准化后求和，利用了跨 benchmark 的信息： 如果一个模型在多个
976	    benchmark 上都有 aberrant pattern，lzm 的信号会累积。 AUROC 从单 benchmark 的 0.96 提升到 0.98
977	    是因为： (1) 信息量增加——5 benchmarks 总共 ~27K items，比单 benchmark 多了判别力； (2) 跨 benchmark
978	    一致性——真正 contaminated 的模型在多个 benchmark 上 lz* 都异常， 而 false positive（某个 benchmark
979	    上偶然异常）不会在 lzm 中累积。 Gemini-1.5 的 lzm = 18.42 极端，因为它在 MMLU 上正侧异常、在 GSM8K/HumanEval
980	    上负侧异常， lzm 用绝对值聚合两侧信号。GPT-4 的 lzm = -0.87 接近零，说明 GPT-4 的 response pattern 在所有
981	    benchmark 上都是 "正常" 的。 Null distribution 校准通过（KS p = 0.312），说明 lzm 在 clean models
982	    上确实近似 N(0,1)。
983	
984	    '
985	  tables:
986	  - name: 'Table 18: lzm Results — PSN-IRT 12 Models'
987	    columns:
988	    - model
989	    - lzm_value
990	    - flagged_alpha005
991	    - n_benchmarks_individual_flag
992	    key_rows:
993	    - - Gemini-1.5
994	      - 18.42
995	      - 'YES'
996	      - 3
997	    - - GPT-4
998	      - -0.87
999	      - 'no'
1000	      - 0
1001	    - - Llama-2-70B
1002	      - -3.21
1003	      - 'YES'
1004	      - 1
1005	    - - Claude-3-Opus
1006	      - 0.42
1007	      - 'no'
1008	      - 0
1009	    - - Mistral-7B
1010	      - -2.45
1011	      - 'no'
1012	      - 0
1013	  - name: 'Table 19: lzm vs Single-Benchmark Detection Power'
1014	    columns:
1015	    - method
1016	    - auroc_15pct
1017	    - power_at_15pct
1018	    - false_alarm_rate
1019	    key_rows:
1020	    - - lz* (MMLU only)
1021	      - 0.96
1022	      - 0.979
1023	      - 0.042
1024	    - - lz* (best single benchmark)
1025	      - 0.96
1026	      - 0.979
1027	      - 0.042
1028	    - - lzm (all benchmarks)
1029	      - 0.98
1030	      - 0.99
1031	      - 0.037
1032	  figures_description:
1033	  - 'Fig 18: lzm 分布——clean models (histogram) + contaminated models (overlay)，标注阈值。'
1034	  - 'Fig 19: 散点图——lzm vs max single-benchmark |lz*|，标注各模型。显示 lzm 提供增量信息。'
1035	  analysis: 'lzm 是一个稳健的 "overall contamination index"，特别适合 leaderboard audit 场景——
1036	    单一指标告诉你 "这个模型总体上是否可疑"。AUROC 增益 0.02 看似不大， 但对 leaderboard-scale 扫描（数千模型），2% 的 precision
1037	    提升意味着减少 ~50 个 false flag。 更重要的叙事价值：lzm 展示了 IRT person-fit 框架的可扩展性——可以从单 benchmark
1038	    到多 benchmark 无缝聚合。
1039	
1040	    '
1041	- name: Post-RL Hypothesis Test
1042	  plan_id: exp-post-rl
1043	  description: '在 Qwen3.5-9B 上先 SFT 污染（15% MMLU items）再 GRPO 训练， 测试 person-fit 信号是否在
1044	    RL 后保持检测力。
1045	
1046	    '
1047	  expected_results:
1048	    pre_rl_lz_star: -8.91
1049	    post_rl_lz_star: -7.12
1050	    post_rl_power_retention_ratio: 0.84
1051	    post_rl_auroc: 0.92
1052	    pre_rl_auroc: 0.96
1053	    auroc_drop_after_rl: 0.04
1054	    post_rl_accuracy_change: 0.012
1055	    post_rl_contam_items_accuracy: 0.82
1056	    pre_rl_contam_items_accuracy: 0.84
1057	    post_rl_non_contam_items_accuracy: 0.75
1058	    pre_rl_non_contam_items_accuracy: 0.74
1059	    post_rl_theta_shift: 0.08
1060	    mia_post_rl_auroc: 0.54
1061	    mia_pre_rl_auroc: 0.71
1062	    person_fit_vs_mia_advantage_post_rl: 0.38
1063	  result_rationale: 'GRPO 后 lz* 信号保留 84% 的机制：GRPO 优化 reward（通常是正确率或 format compliance），
1064	    对已经答对的 contaminated items 不会产生"遗忘"梯度——这些 items 已经获得最大 reward， GRPO 的梯度主要推动模型在
1065	    reward 边界附近的 items 上改进。因此 contaminated items 的 正确率几乎不变（0.84 → 0.82，仅微降 2%），而 non-contaminated
1066	    items 略有提升（+1%）。 lz* 从 -8.91 衰减到 -7.12（~20% 衰减）的原因：GRPO 对 non-contaminated items
1067	    的泛化提升 使 θ 估计上移，缩小了 contaminated items 的 "预期外正确" 幅度。但衰减有限，因为 GRPO 的泛化效应弱于 SFT 的直接
1068	    memorization 效应。 对比 MIA：Wang et al. (2025) 发现 MIA 在 post-RL 后 AUROC 接近随机（0.54），
1069	    因为 RL 重新校准了 token-level probability 分布，消除了 memorization 的 token-level 痕迹。 但 binary
1070	    response pattern 不受 probability recalibration 影响——只要 contaminated items 仍然被答对，person-fit
1071	    信号就存在。这是 person-fit "信息层级优势" 的直接体现： binary outcome 比 token probability 更鲁棒，因为
1072	    RL 可以改变 "how confident the model is" 但很难改变 "whether it gets the answer right"
1073	    on memorized items.
1074	
1075	    '
1076	  tables:
1077	  - name: 'Table 20: Pre- vs Post-RL Person-Fit (Qwen3.5-9B, 15% MMLU Contamination)'
1078	    columns:
1079	    - stage
1080	    - accuracy
1081	    - theta
1082	    - lz_star
1083	    - auroc
1084	    - power
1085	    key_rows:
1086	    - - Clean baseline
1087	      - 0.721
1088	      - 1.42
1089	      - 0.08
1090	      - —
1091	      - —
1092	    - - Post-SFT (contaminated)
1093	      - 0.764
1094	      - 1.63
1095	      - -8.91
1096	      - 0.96
1097	      - 0.97
1098	    - - Post-SFT + GRPO
1099	      - 0.776
1100	      - 1.71
1101	      - -7.12
1102	      - 0.92
1103	      - 0.91
1104	  - name: 'Table 21: Person-Fit vs MIA — Post-RL Robustness'
1105	    columns:
1106	    - method
1107	    - pre_rl_auroc
1108	    - post_rl_auroc
1109	    - auroc_retention
1110	    - info_required
1111	    key_rows:
1112	    - - IRT-FIT (lz*)
1113	      - 0.96
1114	      - 0.92
1115	      - 96%
1116	      - binary responses
1117	    - - Min-K%++
1118	      - 0.88
1119	      - 0.62
1120	      - 70%
1121	      - token log-probs
1122	    - - MIA (reference-based)
1123	      - 0.71
1124	      - 0.54
1125	      - 76%
1126	      - token log-probs + ref model
1127	  - name: 'Table 22: Item-Level Analysis — Accuracy Change After GRPO'
1128	    columns:
1129	    - item_type
1130	    - pre_rl_accuracy
1131	    - post_rl_accuracy
1132	    - change
1133	    key_rows:
1134	    - - contaminated items
1135	      - 0.84
1136	      - 0.82
1137	      - -0.02
1138	    - - non-contaminated items
1139	      - 0.74
1140	      - 0.75
1141	      - 0.01
1142	    - - contaminated hard items (diff>2)
1143	      - 0.79
1144	      - 0.76
1145	      - -0.03
1146	    - - non-contaminated hard items (diff>2)
1147	      - 0.41
1148	      - 0.43
1149	      - 0.02
1150	  figures_description:
1151	  - 'Fig 20: lz* trajectory——clean → post-SFT → post-GRPO，三个阶段的 lz* 值 + CI bar。显示信号有衰减但仍显著。'
1152	  - 'Fig 21: AUROC 对比 bar chart——IRT-FIT vs Min-K%++ vs MIA，pre-RL 和 post-RL 两组。IRT-FIT
1153	    post-RL 仍为 0.92，MIA 跌至 0.54。'
1154	  - 'Fig 22: Item-level accuracy scatterplot，pre-RL (x) vs post-RL (y)，contaminated
1155	    items 标红，non-contaminated 标灰。显示 contaminated items 集中在 (high, high) 区域。'
1156	  analysis: 'Post-RL 实验是论文回应 Wang et al. (2025) 的关键证据。形成清晰对比叙事： "MIA 在 post-RL 后失效（AUROC
1157	    0.54）但 person-fit 保留 84% 信号（AUROC 0.92）， 因为 RL recalibrates probabilities but
1158	    does not undo memorization of correct answers。" 这直接支撑 Claim 1：person-fit 不仅在 minimal-information
1159	    条件下工作， 而且对 post-training 流程具有鲁棒性。机制解释简洁有力：binary outcome > token probability in
1160	    robustness to distribution shift。
1161	
1162	    '
1163	- name: Extra Benchmarks (BBH, MATH)
1164	  plan_id: exp-extra-benchmarks
1165	  description: '添加 BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power
1166	    gap。
1167	
1168	    '
1169	  expected_results:
1170	    bbh_n_items: 6511
1171	    math_n_items: 5000
1172	    bbh_power_at_15pct: 0.89
1173	    math_power_at_15pct: 0.84
1174	    bbh_power_at_5pct: 0.52
1175	    math_power_at_5pct: 0.44
1176	    bbh_predicted_power_from_theory: 0.88
1177	    math_predicted_power_from_theory: 0.83
1178	    theory_prediction_error_bbh: 0.01
1179	    theory_prediction_error_math: 0.01
1180	    bbh_inverted_u_inflection: 0.62
1181	    math_inverted_u_inflection: 0.66
1182	    power_gap_1k_10k_filled: true
1183	  result_rationale: 'BBH (6511 items) 和 MATH (5000 items) 精确填充了 GSM8K (1319) 和 HellaSwag
1184	    (10042) 之间的 power gap。根据 power theory 公式 power ≈ Φ(δ·√n/σ − z_α)： BBH: √6511/√14042
1185	    ≈ 0.68 × MMLU power → 预测 power ≈ 0.88，实测 0.89； MATH: √5000/√14042 ≈ 0.60 × MMLU
1186	    power → 预测 power ≈ 0.83，实测 0.84。 理论预测误差 ≤ 1% 进一步验证了 power theory 的准确性。 BBH 和 MATH
1187	    的 item difficulty 分布不同于 MMLU：BBH 难度更高（mean difficulty ≈ 1.8 vs MMLU 1.2）， MATH
1188	    难度分布更宽（SD ≈ 2.1），这些差异体现在 inverted-U 拐点位置和每 item 信号强度 δ 上， 但 power theory 通过 δ
1189	    参数化吸收了这些差异。
1190	
1191	    '
1192	  tables:
1193	  - name: 'Table 23: Power Gap Analysis — All 7 Benchmarks'
1194	    columns:
1195	    - benchmark
1196	    - n_items
1197	    - power_at_15pct_simulated
1198	    - power_at_15pct_predicted
1199	    - power_at_5pct
1200	    key_rows:
1201	    - - HumanEval
1202	      - 164
1203	      - 0.243
1204	      - 0.231
1205	      - 0.07
1206	    - - ARC-C
1207	      - 1172
1208	      - 0.129
1209	      - 0.142
1210	      - 0.04
1211	    - - GSM8K
1212	      - 1319
1213	      - 0.578
1214	      - 0.561
1215	      - 0.22
1216	    - - MATH
1217	      - 5000
1218	      - 0.84
1219	      - 0.83
1220	      - 0.44
1221	    - - BBH
1222	      - 6511
1223	      - 0.89
1224	      - 0.88
1225	      - 0.52
1226	    - - HellaSwag
1227	      - 10042
1228	      - 0.733
1229	      - 0.748
1230	      - 0.34
1231	    - - MMLU
1232	      - 14042
1233	      - 0.979
1234	      - 0.981
1235	      - 0.78
1236	  figures_description:
1237	  - 'Fig 23: Power vs n_items 理论曲线，7 benchmarks 的数据点全部标注。BBH 和 MATH 精确落在曲线上。'
1238	  analysis: 'BBH 和 MATH 的加入使 power 分析从 5 个 benchmark 扩展到 7 个，覆盖了从 164 (HumanEval)
1239	    到 14042 (MMLU) 的完整 n_items 范围。7 个数据点全部落在理论预测 ±1% 内， 将 power theory 的 R² 从 0.97
1240	    推至接近 0.98。更重要的是 ARC-C 的 power 异常低（0.129 at 1172 items vs GSM8K 的 0.578 at 1319
1241	    items），说明除了 n_items 外 item quality（discrimination）也影响 power， 这在理论公式中通过 δ_per_item
1242	    体现。
1243	
1244	    '
1245	- name: Domain-Level Analysis (MMLU)
1246	  plan_id: exp-domain-analysis
1247	  description: '按 MMLU subject category 分别计算 person-fit，识别 Gemini-1.5 的 MMLU 污染模式。
1248	
1249	    '
1250	  expected_results:
1251	    n_domains_analyzed: 57
1252	    domains_with_extreme_lz_star: 57
1253	    gemini15_domain_lz_star_range: '[+0.8, +12.3]'
1254	    gemini15_domain_lz_star_mean: 4.21
1255	    gemini15_domain_lz_star_sd: 2.87
1256	    gemini15_most_aberrant_domain: abstract_algebra
1257	    gemini15_least_aberrant_domain: high_school_mathematics
1258	    contamination_pattern: uniform across all domains
1259	    domain_level_power_mean: 0.34
1260	    domain_level_power_max: 0.72
1261	    domain_level_n_items_range: '[100, 1534]'
1262	    gpt4_domain_lz_star_sd: 0.82
1263	    gpt4_domains_flagged: 0
1264	  result_rationale: 'Gemini-1.5 在所有 57 个 MMLU domains 上都是 100% 正确率，因此每个 domain 的 lz*
1265	    都为正 （over-consistent pattern）。但各 domain 的 lz* 值不同（range [+0.8, +12.3]）是因为： (1)
1266	    各 domain 的 item 数量不同（100-1534），lz* 信号强度 ∝ √n_items； (2) 各 domain 的 item difficulty
1267	    分布不同——abstract_algebra 有更多高难度 items （mean difficulty ≈ 2.4），100% 正确率与其 difficulty
1268	    分布的偏差更大。 "uniform across all domains" 的发现很重要：它排除了 "Gemini-1.5 只是在特定领域特别强" 的 innocent
1269	    explanation——如果是真实能力，应该在某些 domain 偶尔出错，而不是全面 100%。 Domain-level power 平均仅 0.34
1270	    是因为单 domain 只有 100-1534 items，远少于 full MMLU 的 14K。 这为 power theory 提供了额外验证：57
1271	    个 domain 相当于 57 个不同 n_items 的 "实验"。 GPT-4 在所有 domain 上 lz* 都正常（SD 0.82，接近理论标准差
1272	    1.0），0 个 domain flagged， 作为干净的 negative control。
1273	
1274	    '
1275	  tables:
1276	  - name: 'Table 24: MMLU Domain-Level lz* — Gemini-1.5 vs GPT-4 (Top/Bottom 5 Domains)'
1277	    columns:
1278	    - domain
1279	    - n_items
1280	    - gemini15_acc
1281	    - gemini15_lz_star
1282	    - gpt4_acc
1283	    - gpt4_lz_star
1284	    key_rows:
1285	    - - abstract_algebra
1286	      - 100
1287	      - 1.0
1288	      - 0.83
1289	      - 0.73
1290	      - -0.42
1291	    - - professional_medicine
1292	      - 272
1293	      - 1.0
1294	      - 4.21
1295	      - 0.851
1296	      - 0.67
1297	    - - high_school_mathematics
1298	      - 270
1299	      - 1.0
1300	      - 2.14
1301	      - 0.412
1302	      - -1.23
1303	    - - college_chemistry
1304	      - 100
1305	      - 1.0
1306	      - 0.91
1307	      - 0.47
1308	      - 0.31
1309	    - - global_facts
1310	      - 100
1311	      - 1.0
1312	      - 0.8
1313	      - 0.38
1314	      - -0.87
1315	    - - '...'
1316	      - '...'
1317	      - '...'
1318	      - '...'
1319	      - '...'
1320	      - '...'
1321	    - - miscellaneous
1322	      - 783
1323	      - 1.0
1324	      - 7.89
1325	      - 0.872
1326	      - 0.42
1327	    - - clinical_knowledge
1328	      - 265
1329	      - 1.0
1330	      - 3.87
1331	      - 0.792
1332	      - -0.18
1333	  - name: 'Table 25: Domain-Level Power as Function of n_items'
1334	    columns:
1335	    - n_items_bin
1336	    - n_domains
1337	    - mean_power_at_15pct
1338	    - predicted_from_theory
1339	    key_rows:
1340	    - - 100-150
1341	      - 22
1342	      - 0.18
1343	      - 0.17
1344	    - - 150-300
1345	      - 21
1346	      - 0.31
1347	      - 0.33
1348	    - - 300-600
1349	      - 9
1350	      - 0.52
1351	      - 0.5
1352	    - - 600-1000
1353	      - 3
1354	      - 0.64
1355	      - 0.67
1356	    - - '>1000'
1357	      - 2
1358	      - 0.72
1359	      - 0.74
1360	  figures_description:
1361	  - 'Fig 24: MMLU domain-level lz* heatmap for all 12 models × 57 domains。Gemini-1.5
1362	    行全部为正侧红色。GPT-4 行为中性灰色。'
1363	  - 'Fig 25: Gemini-1.5 domain-level lz* vs domain n_items scatter，显示 √n 依赖关系。'
1364	  analysis: Domain analysis 为 Gemini-1.5 case study 提供了 fine-grained 证据："uniform contamination
1365	    across all 57 MMLU domains" 排除了能力解释（没有任何模型在所有领域同等强）， 支持系统性 benchmark memorization
1366	    的结论。与 GPT-4 的对比提供了干净的 negative control。 Domain-level power 分析作为 bonus，为 power
1367	    theory 提供了 57 个额外的 (n_items, power) 数据点。
1368	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "549100db-662d-4a88-850c-c7f919d8b3b8",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "62e43bbf-4ab2-401c-a704-fd917c13ff3b",
  "sourceToolAssistantUUID": "549100db-662d-4a88-850c-c7f919d8b3b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T09:21:15.826Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QnFK6bHqu8hWvSHGAB1Qd6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62e43bbf-4ab2-401c-a704-fd917c13ff3b",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaHMzsmqcg7wjhu9mGx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb9409d2-74a0-46de-9245-1107e7721210",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tf3Q4vQjLKNoFchE4qNBhp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15310,
      "cache_read_input_tokens": 35450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15310,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 37 · 2026-05-20T09:21:16.187Z_

<details><summary>↩ Tool result · `toolu_01QnFK6bHqu8hWvSHGAB1Qd6`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 framing 完全成立。三条 claim 均有 ground-truth 支撑：(1) minimal-information
3	  operating point 经控制实验确认——仅 binary 数据即可在 5% 污染水平检测，AUROC>0.93；(2) power ∝ n_items
4	  有解析公式， inverted-U 从经验观察升级为理论命题，拐点位置可预测；(3) Gemini-1.5 case study + leaderboard audit
5	  构成大规模实证贡献。Post-RL 实验直接回应 Wang et al.，形成"MIA 失效但 person-fit 存活"的对比叙事。 Headline: "IRT-FIT
6	  是唯一在 minimal-information 条件下同时解决 partial/full/post-RL 污染的方法"。 EMNLP 主会议无需调整 claim
7	  强度。
8	
9	  '
10	imagined_experiments:
11	- name: Two-Sided Detection Framework
12	  plan_id: exp-two-sided
13	  description: '基于 Phase B personfit_matrix.csv，实现 |lz*| > threshold 双侧检测框架， 含 bootstrap
14	    CI 和 BH-FDR 控制。验证 Gemini-1.5 case study 中正侧信号。
15	
16	    '
17	  expected_results:
18	    gemini15_mmlu_lz_star: 34.75
19	    gemini15_mmlu_lz_star_bootstrap_95ci: '[32.1, 37.4]'
20	    gemini15_gsm8k_lz_star: -15.71
21	    gemini15_humaneval_lz_star: -12.37
22	    two_sided_flagged_models_at_fdr_0.05: 4
23	    one_sided_flagged_models_at_fdr_0.05: 2
24	    incremental_detection_gain_two_vs_one_sided: 2 additional models flagged (Gemini-1.5
25	      on MMLU, 1 other high-perf model)
26	    optimal_negative_threshold_alpha_0.05: -2.81
27	    optimal_positive_threshold_alpha_0.05: 3.24
28	    positive_regime_models: Gemini-1.5 (MMLU), possibly Yi-34B or similar near-ceiling
29	      model
30	    negative_regime_models: Gemini-1.5 (GSM8K, HumanEval), Llama-2-70B (ARC-C)
31	  result_rationale: 'Gemini-1.5 的 MMLU 100% 正确率对应 θ=0.78（远低于满分所需能力），产生极端正侧 lz*=+34.75。
32	    这是因为 full contamination 导致模型在所有 item 上正确，包括远超其真实能力的难题—— response pattern 过度一致（over-consistent），与真正高能力模型的"偶尔失误"模式不符。
33	    负侧信号来自 partial contamination：模型在已污染的难题上正确、在未污染的易题上错误， 产生 aberrant pattern（lz*
34	    << 0）。双侧框架捕获这两类互补信号， 单侧框架只能捕获负侧（partial），遗漏正侧（full）。Bootstrap CI 窄是因为 MMLU 有 14K
35	    items， lz* 的抽样方差 ∝ 1/n_items。FDR 控制在 12 模型 × 5 benchmarks = 60 次检验下仍能保持 power，
36	    因为真阳性的 lz* 绝对值远超阈值（效应量极大）。
37	
38	    '
39	  tables:
40	  - name: 'Table 1: Two-Sided Detection Results (Phase B, 12 Models × 5 Benchmarks)'
41	    columns:
42	    - model
43	    - benchmark
44	    - accuracy
45	    - theta_hat
46	    - lz_star
47	    - side
48	    - flagged_bh_fdr_005
49	    - bootstrap_95ci
50	    key_rows:
51	    - - Gemini-1.5
52	      - MMLU
53	      - 1.0
54	      - 0.78
55	      - 34.75
56	      - positive
57	      - 'YES'
58	      - '[32.1, 37.4]'
59	    - - Gemini-1.5
60	      - GSM8K
61	      - 0.946
62	      - 2.41
63	      - -15.71
64	      - negative
65	      - 'YES'
66	      - '[-17.2, -14.3]'
67	    - - Gemini-1.5
68	      - HumanEval
69	      - 0.878
70	      - 1.92
71	      - -12.37
72	      - negative
73	      - 'YES'
74	      - '[-14.1, -10.8]'
75	    - - GPT-4
76	      - MMLU
77	      - 0.864
78	      - 2.15
79	      - -1.23
80	      - —
81	      - 'no'
82	      - '[-2.1, -0.4]'
83	    - - Llama-2-70B
84	      - ARC-C
85	      - 0.673
86	      - 1.08
87	      - -3.87
88	      - negative
89	      - 'YES'
90	      - '[-5.2, -2.6]'
91	  - name: 'Table 2: One-Sided vs Two-Sided Detection Comparison'
92	    columns:
93	    - method
94	    - total_flagged
95	    - partial_contam_detected
96	    - full_contam_detected
97	    - FDR_control
98	    key_rows:
99	    - - one-sided (lz* < threshold)
100	      - 2
101	      - 2
102	      - 0
103	      - '0.05'
104	    - - two-sided (|lz*| > threshold)
105	      - 4
106	      - 2
107	      - 2
108	      - '0.05'
109	  figures_description:
110	  - 'Fig 1: lz* heatmap (12 models × 5 benchmarks)，color diverging at 0，标注双侧阈值线。Gemini-1.5
111	    MMLU 为极端红色（正侧），GSM8K/HumanEval 为极端蓝色（负侧）。'
112	  - 'Fig 2: Bootstrap distribution of lz* for Gemini-1.5 MMLU，显示 CI 远离零点，p-value 极小。'
113	  analysis: '双侧框架是论文的关键方法论贡献。Phase B 数据直接证明单侧检测的盲区：Gemini-1.5 在 MMLU 上的 full contamination
114	    产生正侧信号，传统 person-fit（只看负侧 aberrance）完全遗漏。 这不仅是技术改进，而是揭示了污染信号的双重机制——partial contamination
115	    产生 aberrant pattern （答对难题、答错易题），full contamination 产生 over-consistent pattern（所有题都对，包括不该对的）。
116	    Bootstrap CI 和 FDR 控制确保结论在多重比较下依然稳健。
117	
118	    '
119	- name: Extended Simulation (Inverted-U Characterization)
120	  plan_id: exp-extended-sim
121	  description: '扩展 Phase A 模拟至 60%/75%/90%/100% contamination levels， 修复 100% contamination
122	    的 MLE boundary 处理，精确刻画 inverted-U 拐点。
123	
124	    '
125	  expected_results:
126	    inverted_u_inflection_point_mmlu: 0.65
127	    inverted_u_inflection_point_hellaswag: 0.6
128	    inverted_u_inflection_point_gsm8k: 0.7
129	    inverted_u_inflection_ci_range: '[0.55, 0.75]'
130	    lz_star_at_inflection_mmlu: -0.12
131	    lz_star_at_100pct_contam_mmlu: 28.5
132	    lz_star_at_100pct_contam_hellaswag: 18.2
133	    lz_star_at_100pct_contam_gsm8k: 8.7
134	    negative_peak_lz_at_15pct_mmlu: -8.3
135	    negative_peak_lz_at_25pct_mmlu: -12.1
136	    zero_crossing_contam_level_mmlu: 0.63
137	    zero_crossing_contam_level_hellaswag: 0.58
138	    nan_rate_after_boundary_fix: 0.0
139	    power_at_5pct_contam_mmlu: 0.78
140	    power_at_5pct_contam_hellaswag: 0.34
141	  result_rationale: 'Inverted-U 的物理机制：低污染（<15%）时，少量 hard items 被答对产生 aberrant pattern（lz*
142	    < 0）， 信号随污染比例增强；中等污染（~40-60%）时，被污染 items 的 "全部答对" 开始被 IRT 模型解释为 "该模型能力更高"，θ 估计上移，lz*
143	    绝对值开始减小——因为 response pattern 变得可以被高 θ 解释； 拐点（~65% for MMLU）处 lz* ≈ 0，pattern 恰好可被某个
144	    θ 值完美拟合；超过拐点后， 模型在几乎所有 items 上正确但 θ 估计仍有上界（受 non-contaminated items 约束）， 导致 over-consistent
145	    pattern（lz* > 0）。拐点位置取决于 benchmark 的 item difficulty 分布： MMLU 有大量高难度 items（14K
146	    items 中 ~30% difficulty > 2.0），需要更高污染比例才能 让 pattern 显得 "合理"，所以拐点在 0.65。GSM8K 难度更集中，拐点在
147	    0.70。 100% contamination 的 lz* 大小与 n_items 正相关（MMLU > HellaSwag > GSM8K）， 因为 lz*
148	    的分子累加了所有 item 的 log-likelihood 偏差。 MLE boundary fix 后 NaN 消失，因为 θ 被 cap 在 4.0，lz*
149	    仍可计算（只是值更极端）。
150	
151	    '
152	  tables:
153	  - name: 'Table 3: lz* as a Function of Contamination Level (Mean ± SD, 100 Replications)'
154	    columns:
155	    - contam_level
156	    - mmlu_lz_mean
157	    - mmlu_lz_sd
158	    - hellaswag_lz_mean
159	    - gsm8k_lz_mean
160	    - arc_c_lz_mean
161	    key_rows:
162	    - - 0%
163	      - 0.01
164	      - 1.02
165	      - 0.03
166	      - -0.02
167	      - 0.01
168	    - - 5%
169	      - -3.41
170	      - 1.15
171	      - -1.82
172	      - -1.34
173	      - -0.42
174	    - - 10%
175	      - -6.12
176	      - 1.28
177	      - -3.45
178	      - -2.51
179	      - -0.78
180	    - - 15%
181	      - -8.31
182	      - 1.41
183	      - -4.72
184	      - -3.38
185	      - -1.02
186	    - - 25%
187	      - -12.08
188	      - 1.67
189	      - -6.21
190	      - -4.53
191	      - -1.31
192	    - - 50%
193	      - -5.73
194	      - 2.14
195	      - -2.89
196	      - -1.67
197	      - -0.43
198	    - - 60%
199	      - -1.24
200	      - 2.31
201	      - 0.82
202	      - -0.34
203	      - 0.21
204	    - - 75%
205	      - 8.42
206	      - 2.53
207	      - 5.67
208	      - 3.21
209	      - 1.12
210	    - - 90%
211	      - 19.31
212	      - 2.87
213	      - 12.45
214	      - 6.78
215	      - 2.34
216	    - - 100%
217	      - 28.5
218	      - 3.12
219	      - 18.2
220	      - 8.7
221	      - 3.01
222	  - name: 'Table 4: Two-Sided Power at Various Contamination Levels'
223	    columns:
224	    - contam_level
225	    - mmlu_power
226	    - hellaswag_power
227	    - gsm8k_power
228	    - arc_c_power
229	    key_rows:
230	    - - 5%
231	      - 0.78
232	      - 0.34
233	      - 0.22
234	      - 0.06
235	    - - 15%
236	      - 0.979
237	      - 0.733
238	      - 0.578
239	      - 0.129
240	    - - 25%
241	      - 0.998
242	      - 0.891
243	      - 0.743
244	      - 0.201
245	    - - 50%
246	      - 0.872
247	      - 0.514
248	      - 0.298
249	      - 0.08
250	    - - 75%
251	      - 0.991
252	      - 0.934
253	      - 0.712
254	      - 0.187
255	    - - 100%
256	      - 1.0
257	      - 0.998
258	      - 0.962
259	      - 0.478
260	  figures_description:
261	  - 'Fig 3: Inverted-U 曲线——lz* mean vs contamination level，5 benchmarks 分色。标注 zero-crossing
262	    点和拐点位置，shaded area 为 ±1 SD。MMLU 曲线最深、拐点最右。'
263	  - 'Fig 4: Two-sided power vs contamination level，显示 U 型 power 曲线（中间有 dip 但不到 0）。对比
264	    one-sided power 在高污染时 drop to 0。'
265	  analysis: 'Inverted-U 的完整刻画是 Claim 2 的核心证据。拐点位置在 [0.55, 0.75] 范围内与 benchmark difficulty
266	    分布相关——这为后续理论推导提供了经验基准。关键发现：two-sided power 在拐点附近 有 dip 但不跌至零（因为 lz* 的 SD 在拐点处也增大，部分
267	    replications 仍超阈值）， 而 one-sided power 在高污染区完全失效。100% contamination 修复后产生极端正侧 lz*，
268	    与 Phase B Gemini-1.5 的经验数据定量一致（模拟 28.5 vs 实测 34.75，差异来自 Gemini-1.5 的真实 θ 分布与模拟假设不完全匹配）。
269	
270	    '
271	- name: Controlled Contamination Experiment
272	  plan_id: exp-ctrl-contam
273	  description: '在 Qwen3.5-9B 和 Gemma-4-31B 上，QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark
274	    items，建立 ground-truth contamination → lz* 映射。
275	
276	    '
277	  expected_results:
278	    ctrl_contam_auroc_at_15pct: 0.96
279	    ctrl_contam_auroc_at_5pct: 0.82
280	    ctrl_contam_auroc_at_25pct: 0.99
281	    ctrl_contam_min_detectable_level: 0.05
282	    ctrl_contam_lz_effect_size_cohens_d_at_15pct: 2.3
283	    ctrl_contam_lz_effect_size_cohens_d_at_5pct: 1.1
284	    qwen_clean_lz_star_mmlu: 0.08
285	    qwen_5pct_lz_star_mmlu: -3.72
286	    qwen_10pct_lz_star_mmlu: -6.45
287	    qwen_15pct_lz_star_mmlu: -8.91
288	    qwen_25pct_lz_star_mmlu: -11.34
289	    qwen_50pct_lz_star_mmlu: -4.82
290	    gemma_clean_lz_star_mmlu: 0.15
291	    gemma_5pct_lz_star_mmlu: -3.21
292	    gemma_15pct_lz_star_mmlu: -7.63
293	    gemma_50pct_lz_star_mmlu: -5.14
294	    accuracy_lift_at_15pct_contam_qwen: 0.043
295	    accuracy_lift_at_15pct_contam_gemma: 0.038
296	    sft_generalization_ratio: 0.12
297	    contaminated_items_accuracy_lift: 0.31
298	    non_contaminated_items_accuracy_change: 0.014
299	    false_positive_rate_at_alpha_0.05: 0.038
300	  result_rationale: 'SFT contamination 在 binary response 层面产生强 person-misfit 信号的原因：QLoRA
301	    SFT 直接 优化被注入 items 的 loss，导致这些 items 的正确率大幅上升（+31% on contaminated items）， 而未注入
302	    items 仅有微弱泛化（+1.4%）。这种"选择性提升"在 IRT 模型看来是 aberrant—— 模型在某些 hard items 上突然正确，但在同难度的
303	    non-contaminated items 上仍然错误。 泛化效应仅 12% 的原因：QLoRA 只更新 adapter weights（~0.5% 参数），且
304	    benchmark items 的格式高度标准化（MCQA），SFT 学到的是特定 item 的 answer pattern 而非领域知识。 Cohen''s
305	    d = 2.3 at 15% 说明效应量巨大——clean 和 contaminated 的 lz* 分布几乎不重叠。 AUROC 0.96 at 15%
306	    意味着随机抽一对 clean/contaminated 模型，96% 概率能正确区分。 5% contamination 仍可检测（AUROC 0.82）是因为
307	    MMLU 有 14K items，5% = 700 items 被污染， 足以在 lz* 累积中产生显著偏移。FPR 0.038 < 0.05 说明 null
308	    distribution 校准良好。 两个 base model 结果一致（效应量差 <15%）说明信号不依赖于特定模型架构。
309	
310	    '
311	  tables:
312	  - name: 'Table 5: Controlled Contamination — lz* by Model and Contamination Level
313	      (MMLU)'
314	    columns:
315	    - model
316	    - contam_level
317	    - accuracy
318	    - theta_hat
319	    - lz_star_mean
320	    - lz_star_sd
321	    - flagged_rate_alpha005
322	    key_rows:
323	    - - Qwen3.5-9B
324	      - 0%
325	      - 0.721
326	      - 1.42
327	      - 0.08
328	      - 0.97
329	      - 0.047
330	    - - Qwen3.5-9B
331	      - 5%
332	      - 0.738
333	      - 1.51
334	      - -3.72
335	      - 1.21
336	      - 0.82
337	    - - Qwen3.5-9B
338	      - 10%
339	      - 0.756
340	      - 1.59
341	      - -6.45
342	      - 1.34
343	      - 0.94
344	    - - Qwen3.5-9B
345	      - 15%
346	      - 0.764
347	      - 1.63
348	      - -8.91
349	      - 1.42
350	      - 0.97
351	    - - Qwen3.5-9B
352	      - 25%
353	      - 0.787
354	      - 1.71
355	      - -11.34
356	      - 1.58
357	      - 0.99
358	    - - Qwen3.5-9B
359	      - 50%
360	      - 0.831
361	      - 1.89
362	      - -4.82
363	      - 2.08
364	      - 0.87
365	    - - Gemma-4-31B
366	      - 0%
367	      - 0.793
368	      - 1.81
369	      - 0.15
370	      - 0.94
371	      - 0.041
372	    - - Gemma-4-31B
373	      - 5%
374	      - 0.808
375	      - 1.88
376	      - -3.21
377	      - 1.18
378	      - 0.78
379	    - - Gemma-4-31B
380	      - 15%
381	      - 0.831
382	      - 1.97
383	      - -7.63
384	      - 1.38
385	      - 0.95
386	    - - Gemma-4-31B
387	      - 50%
388	      - 0.874
389	      - 2.14
390	      - -5.14
391	      - 2.01
392	      - 0.84
393	  - name: 'Table 6: Detection Performance (AUROC) by Contamination Level'
394	    columns:
395	    - contam_level
396	    - auroc_qwen
397	    - auroc_gemma
398	    - auroc_pooled
399	    - cohens_d_pooled
400	    key_rows:
401	    - - 5%
402	      - 0.84
403	      - 0.8
404	      - 0.82
405	      - 1.1
406	    - - 10%
407	      - 0.93
408	      - 0.91
409	      - 0.92
410	      - 1.8
411	    - - 15%
412	      - 0.97
413	      - 0.95
414	      - 0.96
415	      - 2.3
416	    - - 25%
417	      - 0.99
418	      - 0.98
419	      - 0.99
420	      - 2.8
421	    - - 50%
422	      - 0.94
423	      - 0.91
424	      - 0.93
425	      - 1.6
426	  - name: 'Table 7: Contamination Selectivity — Accuracy Change on Contaminated vs
427	      Non-Contaminated Items'
428	    columns:
429	    - contam_level
430	    - contam_items_acc_before
431	    - contam_items_acc_after
432	    - contam_items_lift
433	    - non_contam_items_acc_before
434	    - non_contam_items_acc_after
435	    - non_contam_items_lift
436	    key_rows:
437	    - - 5%
438	      - 0.56
439	      - 0.87
440	      - 0.31
441	      - 0.73
442	      - 0.74
443	      - 0.014
444	    - - 15%
445	      - 0.54
446	      - 0.84
447	      - 0.3
448	      - 0.73
449	      - 0.75
450	      - 0.018
451	    - - 25%
452	      - 0.55
453	      - 0.86
454	      - 0.31
455	      - 0.73
456	      - 0.76
457	      - 0.024
458	    - - 50%
459	      - 0.57
460	      - 0.88
461	      - 0.31
462	      - 0.73
463	      - 0.77
464	      - 0.037
465	  figures_description:
466	  - 'Fig 5: lz* vs contamination level scatter (Qwen + Gemma, MMLU)，叠加模拟 inverted-U
467	    理论曲线。实测数据点落在理论预测 ±1 SD 内。'
468	  - 'Fig 6: ROC 曲线 at 5%/15%/25% contamination，三条曲线叠在一起，标注 AUROC 值。'
469	  - 'Fig 7: Item-level accuracy heatmap，contaminated items (sorted by difficulty)
470	    vs non-contaminated items，展示 SFT 的选择性提升效应。'
471	  analysis: '控制实验是论文最关键的 ground-truth 证据。核心发现：(1) SFT 污染在 binary response 层面 产生强烈且可检测的
472	    person-misfit 信号，Cohen''s d > 2 at 15% contamination； (2) 泛化效应仅 1-4%，远不足以平滑 aberrant
473	    pattern——这直接回应了 R5 审稿意见； (3) 两个不同架构/规模的 base model 给出一致结果，排除模型特异性； (4) 5% contamination
474	    即可检测（AUROC 0.82），确立 minimal detectable level。 50% contamination 的 lz* 绝对值回落验证了
475	    inverted-U，与扩展模拟定量一致。
476	
477	    '
478	- name: Power Theory Derivation
479	  plan_id: exp-power-theory
480	  description: '推导 power 与 n_items 的解析关系，基于 Snijders (2001) lz* 方差公式， 验证理论曲线与模拟数据的拟合度，将
481	    inverted-U 升级为理论命题。
482	
483	    '
484	  expected_results:
485	    power_theory_r_squared: 0.97
486	    power_formula: power ≈ Φ(δ·√n / σ_lz* − z_α) where δ = E[log L_contam − log L_clean]
487	      per item
488	    inverted_u_inflection_formula: c* = argmin_c |E_θ[Σ_i (x_i·log P_i + (1−x_i)·log(1−P_i))
489	      | contam=c] − E_θ[...| contam=0]|
490	    predicted_inflection_mmlu: 0.64
491	    predicted_inflection_hellaswag: 0.59
492	    predicted_inflection_gsm8k: 0.68
493	    observed_inflection_mmlu: 0.65
494	    observed_inflection_hellaswag: 0.6
495	    observed_inflection_gsm8k: 0.7
496	    inflection_prediction_error: 0.02
497	    power_at_n100_15pct_predicted: 0.089
498	    power_at_n1000_15pct_predicted: 0.491
499	    power_at_n5000_15pct_predicted: 0.862
500	    power_at_n14000_15pct_predicted: 0.981
501	    min_n_for_80pct_power_at_15pct: 3200
502	    min_n_for_80pct_power_at_5pct: 9800
503	  result_rationale: 'Snijders (2001) 证明了在正确指定的 IRT 模型下 lz* ~ N(0,1)。当注入 contamination
504	    时， lz* 的期望偏移量 δ 可以解析计算：每个被污染 item 对 log-likelihood 的贡献偏差为 log P_i(θ_true) − log
505	    P_i(θ_estimated)，其中 θ_estimated 被 contaminated items 上推。 对 n 个 items 中 c·n 个被污染的情况，总偏移
506	    ∝ c·n·δ_per_item，而 lz* 的标准差 ∝ √n。 因此 power ≈ Φ(c·√n·δ_per_item/σ − z_α)，这是一个关于
507	    c 和 n 的可预测函数。 R² = 0.97 的原因：理论假设（IRT 模型正确指定、θ 的 MLE 一致性）在模拟中近似成立， 但现实中参数估计有误差、4PL
508	    模型有轻微 misfit，导致不完美拟合。 Inverted-U 的拐点可以从 item difficulty 分布的分位数推导：当 contaminated
509	    items 的正确率 被提升到 1.0 时，如果这些 items 的 difficulty 覆盖了 IRT scale 的某个区间， θ 的 MLE 会被推到一个特定位置，使得
510	    response pattern 看起来 "最合理" 的 contamination 比例 就是拐点。MMLU difficulty 分布偏宽（SD ≈ 1.8），拐点偏右（0.64）；GSM8K
511	    difficulty 更集中 （SD ≈ 1.2），拐点偏右（0.68）是因为 difficulty 水平更高。 理论预测的拐点与观测值的误差仅 0.02，验证了解析公式的有效性。
512	
513	    '
514	  tables:
515	  - name: 'Table 8: Theoretical vs Simulated Power (15% Contamination)'
516	    columns:
517	    - n_items
518	    - predicted_power
519	    - simulated_power
520	    - absolute_error
521	    key_rows:
522	    - - 100
523	      - 0.089
524	      - 0.092
525	      - 0.003
526	    - - 500
527	      - 0.312
528	      - 0.298
529	      - 0.014
530	    - - 1000
531	      - 0.491
532	      - 0.503
533	      - 0.012
534	    - - 1319
535	      - 0.578
536	      - 0.578
537	      - 0.0
538	    - - 5000
539	      - 0.862
540	      - 0.851
541	      - 0.011
542	    - - 10042
543	      - 0.964
544	      - 0.958
545	      - 0.006
546	    - - 14042
547	      - 0.981
548	      - 0.979
549	      - 0.002
550	  - name: 'Table 9: Inverted-U Inflection Point — Predicted vs Observed'
551	    columns:
552	    - benchmark
553	    - n_items
554	    - difficulty_sd
555	    - predicted_inflection
556	    - observed_inflection
557	    - abs_error
558	    key_rows:
559	    - - MMLU
560	      - 14042
561	      - 1.83
562	      - 0.64
563	      - 0.65
564	      - 0.01
565	    - - HellaSwag
566	      - 10042
567	      - 1.52
568	      - 0.59
569	      - 0.6
570	      - 0.01
571	    - - GSM8K
572	      - 1319
573	      - 1.21
574	      - 0.68
575	      - 0.7
576	      - 0.02
577	    - - ARC-C
578	      - 1172
579	      - 1.45
580	      - 0.62
581	      - 0.64
582	      - 0.02
583	    - - HumanEval
584	      - 164
585	      - 1.67
586	      - 0.61
587	      - 0.63
588	      - 0.02
589	  - name: 'Table 10: Minimum n_items for 80% Power at Various Contamination Levels'
590	    columns:
591	    - contam_level
592	    - min_n_theoretical
593	    - min_n_simulated
594	    key_rows:
595	    - - 5%
596	      - 9800
597	      - 10200
598	    - - 10%
599	      - 4700
600	      - 4900
601	    - - 15%
602	      - 3200
603	      - 3350
604	    - - 25%
605	      - 1800
606	      - 1900
607	  figures_description:
608	  - 'Fig 8: Power vs n_items 理论曲线（连续线）叠加 5 benchmarks 的模拟数据点（散点）。多条曲线对应不同 contamination
609	    levels (5%/10%/15%/25%)。'
610	  - 'Fig 9: Inverted-U 理论预测曲线 vs 模拟数据，标注拐点位置与 CI。'
611	  - 'Fig 10: Power landscape heatmap (n_items × contam_level)，颜色编码 power，标注 80% power
612	    等高线。'
613	  analysis: 'Power 理论将 Claim 2 从经验观察升级为可预测的定量关系。解析公式给出了 practitioner 的 直接指导：要检测 15%
614	    污染需要 ≥3200 items，检测 5% 污染需要 ≥9800 items。 这解释了为什么 ARC-C (1172 items) 的 power 只有
615	    12.9%——不是方法失败，而是信息不足。 Inverted-U 的理论推导是方法论贡献的核心：它不仅解释了为什么存在拐点， 还能从 item difficulty
616	    分布预测拐点位置，误差仅 1-2 个百分点。
617	
618	    '
619	- name: Leaderboard Audit (Large-Scale Scan)
620	  plan_id: exp-leaderboard-audit
621	  description: 'Open LLM Leaderboard v1 大规模扫描，获取 per-item response logs， 对所有可用模型计算
622	    person-fit，绘制 per-benchmark 污染率随时间趋势。
623	
624	    '
625	  expected_results:
626	    leaderboard_models_scanned: 2847
627	    leaderboard_models_with_per_item_logs: 0
628	    leaderboard_models_rerun_inference: 2847
629	    total_gpu_hours_inference: 18.5
630	    leaderboard_flagged_rate_overall: 0.12
631	    leaderboard_flagged_rate_mmlu: 0.15
632	    leaderboard_flagged_rate_hellaswag: 0.09
633	    leaderboard_flagged_rate_arc_c: 0.07
634	    leaderboard_flagged_rate_gsm8k: 0.11
635	    flagged_models_total: 342
636	    flagged_two_sided_positive: 87
637	    flagged_two_sided_negative: 255
638	    contamination_trend_increasing: true
639	    contamination_rate_2023q1: 0.06
640	    contamination_rate_2023q3: 0.11
641	    contamination_rate_2024q1: 0.18
642	    cross_benchmark_consistent_flag_rate: 0.34
643	    top_flagged_model_lz_star: -22.4
644	  result_rationale: 'Per-item response logs 在 HuggingFace 上不直接公开（Leaderboard v1 只存
645	    aggregate scores）， 因此需要对可获取权重的模型重新跑推理。受 GPU 预算限制（20 hrs），选择 <7B 参数模型 优先扫描，覆盖 2847
646	    个模型（占 Leaderboard v1 总量的 ~40%）。 12% flagged rate 的来源：Leaderboard v1 时期（2023-2024）是
647	    benchmark gaming 高峰期， 大量模型通过 SFT 在 benchmark items 上训练以获取高排名。MMLU 受影响最严重（15%）
648	    因为它是 Leaderboard 的核心排名指标且训练数据广泛可获得。 时间趋势显示 2023 Q1 flagged rate 仅 6%，到 2024 Q1
649	    升至 18%—— 与社区对 benchmark contamination 问题认知的时间线一致（Contamination in the wild 2024
650	    等论文）。 正侧 flagged（87 个）主要是 MMLU 上的 "suspicious near-ceiling" 模型， 负侧 flagged（255
651	    个）主要是 partial contamination 的小模型。 跨 benchmark 一致 flag rate 34% 说明约 1/3 的 flagged
652	    模型在多个 benchmark 上同时异常—— 这些是最可信的 contamination 案例。
653	
654	    '
655	  tables:
656	  - name: 'Table 11: Leaderboard Audit Summary'
657	    columns:
658	    - benchmark
659	    - models_scanned
660	    - flagged_negative
661	    - flagged_positive
662	    - flagged_rate
663	    - median_lz_star_flagged
664	    key_rows:
665	    - - MMLU
666	      - 2847
667	      - 312
668	      - 115
669	      - 0.15
670	      - -6.73
671	    - - HellaSwag
672	      - 2847
673	      - 198
674	      - 58
675	      - 0.09
676	      - -4.21
677	    - - ARC-C
678	      - 2847
679	      - 142
680	      - 57
681	      - 0.07
682	      - -3.12
683	    - - GSM8K
684	      - 2182
685	      - 178
686	      - 63
687	      - 0.11
688	      - -5.42
689	    - - Overall (any benchmark)
690	      - 2847
691	      - 255
692	      - 87
693	      - 0.12
694	      - —
695	  - name: 'Table 12: Contamination Rate by Time Period'
696	    columns:
697	    - period
698	    - models_in_period
699	    - flagged_count
700	    - flagged_rate
701	    key_rows:
702	    - - 2023 Q1-Q2
703	      - 487
704	      - 29
705	      - 0.06
706	    - - 2023 Q3-Q4
707	      - 891
708	      - 98
709	      - 0.11
710	    - - 2024 Q1-Q2
711	      - 1103
712	      - 198
713	      - 0.18
714	    - - 2024 Q3+
715	      - 366
716	      - 51
717	      - 0.14
718	  - name: 'Table 13: Top 10 Most Anomalous Models'
719	    columns:
720	    - model
721	    - benchmark
722	    - accuracy
723	    - theta
724	    - lz_star
725	    - side
726	    - params
727	    key_rows:
728	    - - anonymous-7b-v3
729	      - MMLU
730	      - 0.847
731	      - 1.23
732	      - -22.4
733	      - negative
734	      - 7B
735	    - - llm-finetune-2b
736	      - MMLU
737	      - 0.912
738	      - 1.45
739	      - 18.7
740	      - positive
741	      - 2B
742	    - - benchmark-tuned-3b
743	      - GSM8K
744	      - 0.891
745	      - 2.12
746	      - -17.3
747	      - negative
748	      - 3B
749	  figures_description:
750	  - 'Fig 11: 散点图——所有 2847 模型的 (accuracy, lz*) on MMLU。Flagged 模型标红，non-flagged 标灰。显示
751	    flagged 模型不仅是高 accuracy（也有中等 accuracy 但 aberrant pattern 的）。'
752	  - 'Fig 12: 时间趋势——每季度的 flagged rate，按 benchmark 分色。显示逐年上升趋势。'
753	  - 'Fig 13: Cross-benchmark consistency heatmap——flagged 模型在各 benchmark 上的 lz* 值，展示跨
754	    benchmark 污染的关联性。'
755	  analysis: 'Leaderboard audit 是 IRT-FIT 的 "killer app"——唯一只需要 binary response data
756	    的方法 才能做到如此规模的扫描。ConStat 需要 re-test（需要 live model access）， Min-K%++ 需要 token probabilities（需要
757	    logits），MIA 需要 training data reference。 2847 个模型的扫描中 12% flagged rate 意味着约 342
758	    个模型存在可疑的 benchmark 污染， 且这个比例随时间上升。这为社区提供了首个大规模、定量的 benchmark integrity 评估。 尽管未达到
759	    7000 个模型的上限预测，2847 个模型已是同类研究中最大规模。
760	
761	    '
762	- name: 4PL vs 3PL Ablation
763	  plan_id: exp-4pl-ablation
764	  description: '比较 4PL (with feasibility parameter d) 和 3PL(d=1) 下的检测灵敏度差异， 量化 d 参数对
765	    false alarm 和 detection power 的影响。
766	
767	    '
768	  expected_results:
769	    auroc_4pl_15pct: 0.96
770	    auroc_3pl_15pct: 0.91
771	    auroc_difference_15pct: 0.05
772	    false_alarm_rate_4pl: 0.042
773	    false_alarm_rate_3pl: 0.078
774	    power_4pl_15pct_mmlu: 0.979
775	    power_3pl_15pct_mmlu: 0.934
776	    power_difference_15pct_mmlu: 0.045
777	    mean_abs_lz_star_difference_clean: 0.34
778	    mean_abs_lz_star_difference_contam: 0.87
779	    d_parameter_mean_psn_irt: 0.91
780	    d_parameter_sd_psn_irt: 0.08
781	    items_where_d_matters_most: top-difficulty items (difficulty > 2.5) where d <
782	      0.85
783	  result_rationale: '4PL 的 d 参数（upper asymptote / feasibility parameter）建模了即使能力极高的考生
784	    也可能答错某些 items 的现象——在 LLM 场景中对应"某些 items 的表述/格式导致即使知道答案的模型也可能选错"。 当 d < 1 时，3PL(d=1)
785	    会高估高能力模型在这些 items 上的预期正确率， 导致其答错时产生过多的 "aberrant" 信号（false alarm 上升）。 4PL 通过让
786	    d < 1 吸收这种自然变异，减少了 false alarm（0.042 vs 0.078）。 对于 contaminated models，d < 1 的
787	    items 是区分度最高的：contaminated model 在这些 items 上 答对率接近 1.0（因为直接记住了答案），而 clean model
788	    的答对率被 d 压低。 因此 4PL 在 contaminated case 中效应量更大（lz* 偏差多 0.87），综合 AUROC 提升 0.05。
789	    差异主要集中在高难度 items（difficulty > 2.5）——这些 items 的 d 值通常更低， 因为它们的表述更复杂，即使知道正确答案也更容易因格式理解问题出错。
790	
791	    '
792	  tables:
793	  - name: 'Table 14: 4PL vs 3PL Detection Performance Comparison'
794	    columns:
795	    - metric
796	    - 4PL
797	    - 3PL(d=1)
798	    - difference
799	    key_rows:
800	    - - AUROC @ 15%
801	      - 0.96
802	      - 0.91
803	      - '+0.05'
804	    - - False Alarm Rate (α=0.05)
805	      - 0.042
806	      - 0.078
807	      - −0.036
808	    - - Power @ 15% MMLU
809	      - 0.979
810	      - 0.934
811	      - '+0.045'
812	    - - Power @ 5% MMLU
813	      - 0.78
814	      - 0.69
815	      - '+0.09'
816	    - - Mean |lz*| clean models
817	      - 0.83
818	      - 1.17
819	      - −0.34
820	    - - Mean |lz*| contam models (15%)
821	      - 8.91
822	      - 8.04
823	      - '+0.87'
824	  - name: 'Table 15: Impact of d Parameter by Item Difficulty Band'
825	    columns:
826	    - difficulty_band
827	    - n_items
828	    - mean_d
829	    - lz_star_diff_clean
830	    - lz_star_diff_contam
831	    key_rows:
832	    - - < 0.5 (easy)
833	      - 2814
834	      - 0.97
835	      - -0.08
836	      - 0.12
837	    - - 0.5–1.5
838	      - 5621
839	      - 0.93
840	      - -0.21
841	      - 0.43
842	    - - 1.5–2.5
843	      - 3891
844	      - 0.89
845	      - -0.38
846	      - 0.78
847	    - - '> 2.5 (hard)'
848	      - 1716
849	      - 0.82
850	      - -0.67
851	      - 1.45
852	  figures_description:
853	  - 'Fig 14: ROC 曲线对比——4PL vs 3PL at 5%/15% contamination。4PL 曲线始终在 3PL 上方。'
854	  - 'Fig 15: d parameter distribution (histogram) from PSN-IRT，标注 mean 和关键分位数。'
855	  analysis: '4PL vs 3PL 的差异统计显著但不是巨大的——这其实是好消息：它说明 person-fit 方法 对 IRT 模型选择有一定 robustness，3PL
856	    也能工作（AUROC 0.91），但 4PL 更优（AUROC 0.96）。 关键 insight：d 参数的影响集中在高难度 items 上，而这些 items
857	    恰好是 contamination 信号最强的区域（contaminated model 在难题上答对是最 aberrant 的）。因此 4PL 的精确建模
858	    在检测任务中有非平凡的价值。
859	
860	    '
861	- name: Baseline Comparison (ConStat, Min-K%++)
862	  plan_id: exp-baseline-comparison
863	  description: '在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs ConStat vs
864	    Min-K%++ 的 AUROC 和 Type-I error。
865	
866	    '
867	  expected_results:
868	    irt_fit_auroc_15pct: 0.96
869	    constat_auroc_15pct: 0.83
870	    min_k_pp_auroc_15pct: 0.88
871	    irt_fit_auroc_5pct: 0.82
872	    constat_auroc_5pct: 0.61
873	    min_k_pp_auroc_5pct: 0.72
874	    auroc_advantage_vs_constat_15pct: 0.13
875	    auroc_advantage_vs_minkpp_15pct: 0.08
876	    baseline_auroc_advantage_vs_constat: 0.1
877	    type_i_error_irt_fit: 0.042
878	    type_i_error_constat: 0.053
879	    type_i_error_min_k_pp: 0.048
880	    irt_fit_information_required: binary responses only
881	    constat_information_required: binary responses + re-test capability
882	    min_k_pp_information_required: token-level log-probabilities
883	    irt_fit_unique_advantage: operates without model access
884	  result_rationale: 'IRT-FIT 在 AUROC 上优于 ConStat 0.10-0.13 的原因有两方面： (1) Person-fit
885	    statistics 利用了完整的 item-level response pattern 信息——每个 item 的 difficulty、 discrimination、guessing、feasibility
886	    参数都参与 lz* 计算，而 ConStat 基于 aggregate performance 的一致性检验，信息利用效率更低； (2) ConStat 的
887	    re-test design 假设 contaminated model 在 re-test 时表现不一致， 但 SFT contamination 是永久性的（权重已改变），re-test
888	    分数几乎不变，削弱了 ConStat 的信号。 Min-K%++ 在 AUROC 上略低于 IRT-FIT（0.88 vs 0.96）但需要 token-level
889	    probabilities—— 信息需求更高。其信号来自 token-level memorization（contaminated items 的 token
890	    loss 更低）， 但 SFT 后的 token-level 信号会被 RL 和 decoding 过程扰动，不如 binary response 层面的
891	    person-fit 信号稳定。 Type-I error 都接近 nominal 0.05，说明三种方法的 null calibration 都合理。 关键叙事：IRT-FIT
892	    不仅性能更好，而且信息需求最低——这是 detection frontier 的核心论点。
893	
894	    '
895	  tables:
896	  - name: 'Table 16: Baseline Comparison — Detection Performance on Controlled Contamination'
897	    columns:
898	    - method
899	    - info_required
900	    - auroc_5pct
901	    - auroc_15pct
902	    - auroc_25pct
903	    - type_i_error
904	    key_rows:
905	    - - IRT-FIT (lz*, two-sided)
906	      - binary responses
907	      - 0.82
908	      - 0.96
909	      - 0.99
910	      - 0.042
911	    - - ConStat
912	      - binary + re-test
913	      - 0.61
914	      - 0.83
915	      - 0.91
916	      - 0.053
917	    - - Min-K%++
918	      - token log-probs
919	      - 0.72
920	      - 0.88
921	      - 0.95
922	      - 0.048
923	  - name: 'Table 17: Detection Frontier — Information Access vs Detection Power'
924	    columns:
925	    - information_level
926	    - method
927	    - auroc_15pct
928	    - scalability
929	    key_rows:
930	    - - binary responses only
931	      - IRT-FIT
932	      - 0.96
933	      - any model with public scores
934	    - - binary + re-test
935	      - ConStat
936	      - 0.83
937	      - requires live model access
938	    - - token probabilities
939	      - Min-K%++
940	      - 0.88
941	      - requires API with logprobs
942	    - - training data
943	      - n-gram overlap
944	      - —
945	      - requires training data access
946	    - - model weights
947	      - internal probing
948	      - —
949	      - requires open weights
950	  figures_description:
951	  - 'Fig 16: ROC 曲线三方对比，IRT-FIT / ConStat / Min-K%++，at 15% contamination。'
952	  - 'Fig 17: Detection frontier diagram——x 轴为 information access level (ordered)，y
953	    轴为 AUROC，标注各方法位置。IRT-FIT 在最左下角（最少信息，高 AUROC）。'
954	  analysis: 'Baseline comparison 直接支撑 Claim 1（minimal-information operating point）。IRT-FIT
955	    在信息需求最低的条件下取得了最高的 AUROC——这不是因为 person-fit 比 MIA 更好（在等信息条件下 Min-K%++ 可能更强），而是因为
956	    person-fit 从 binary data 中提取了最大信号量。 Detection frontier diagram 是一个有力的可视化，直接展示了方法论贡献的核心。
957	
958	    '
959	- name: Multiscale lzm Statistic
960	  plan_id: exp-multiscale-lzm
961	  description: '实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021），跨 benchmark 聚合 lz*，
962	    在 PSN-IRT 12 模型 + 控制实验模型上验证。
963	
964	    '
965	  expected_results:
966	    lzm_auroc_15pct: 0.98
967	    lzm_vs_single_benchmark_auroc_gain: 0.02
968	    lzm_cross_benchmark_correlation: 0.67
969	    gemini15_lzm: 18.42
970	    gpt4_lzm: -0.87
971	    clean_model_lzm_mean: 0.03
972	    clean_model_lzm_sd: 0.91
973	    contam_model_lzm_mean_15pct: -7.23
974	    lzm_null_ks_p: 0.312
975	    lzm_power_at_15pct_pooled: 0.99
976	  result_rationale: 'lzm 将多个 benchmark 的 lz* 标准化后求和，利用了跨 benchmark 的信息： 如果一个模型在多个
977	    benchmark 上都有 aberrant pattern，lzm 的信号会累积。 AUROC 从单 benchmark 的 0.96 提升到 0.98
978	    是因为： (1) 信息量增加——5 benchmarks 总共 ~27K items，比单 benchmark 多了判别力； (2) 跨 benchmark
979	    一致性——真正 contaminated 的模型在多个 benchmark 上 lz* 都异常， 而 false positive（某个 benchmark
980	    上偶然异常）不会在 lzm 中累积。 Gemini-1.5 的 lzm = 18.42 极端，因为它在 MMLU 上正侧异常、在 GSM8K/HumanEval
981	    上负侧异常， lzm 用绝对值聚合两侧信号。GPT-4 的 lzm = -0.87 接近零，说明 GPT-4 的 response pattern 在所有
982	    benchmark 上都是 "正常" 的。 Null distribution 校准通过（KS p = 0.312），说明 lzm 在 clean models
983	    上确实近似 N(0,1)。
984	
985	    '
986	  tables:
987	  - name: 'Table 18: lzm Results — PSN-IRT 12 Models'
988	    columns:
989	    - model
990	    - lzm_value
991	    - flagged_alpha005
992	    - n_benchmarks_individual_flag
993	    key_rows:
994	    - - Gemini-1.5
995	      - 18.42
996	      - 'YES'
997	      - 3
998	    - - GPT-4
999	      - -0.87
1000	      - 'no'
1001	      - 0
1002	    - - Llama-2-70B
1003	      - -3.21
1004	      - 'YES'
1005	      - 1
1006	    - - Claude-3-Opus
1007	      - 0.42
1008	      - 'no'
1009	      - 0
1010	    - - Mistral-7B
1011	      - -2.45
1012	      - 'no'
1013	      - 0
1014	  - name: 'Table 19: lzm vs Single-Benchmark Detection Power'
1015	    columns:
1016	    - method
1017	    - auroc_15pct
1018	    - power_at_15pct
1019	    - false_alarm_rate
1020	    key_rows:
1021	    - - lz* (MMLU only)
1022	      - 0.96
1023	      - 0.979
1024	      - 0.042
1025	    - - lz* (best single benchmark)
1026	      - 0.96
1027	      - 0.979
1028	      - 0.042
1029	    - - lzm (all benchmarks)
1030	      - 0.98
1031	      - 0.99
1032	      - 0.037
1033	  figures_description:
1034	  - 'Fig 18: lzm 分布——clean models (histogram) + contaminated models (overlay)，标注阈值。'
1035	  - 'Fig 19: 散点图——lzm vs max single-benchmark |lz*|，标注各模型。显示 lzm 提供增量信息。'
1036	  analysis: 'lzm 是一个稳健的 "overall contamination index"，特别适合 leaderboard audit 场景——
1037	    单一指标告诉你 "这个模型总体上是否可疑"。AUROC 增益 0.02 看似不大， 但对 leaderboard-scale 扫描（数千模型），2% 的 precision
1038	    提升意味着减少 ~50 个 false flag。 更重要的叙事价值：lzm 展示了 IRT person-fit 框架的可扩展性——可以从单 benchmark
1039	    到多 benchmark 无缝聚合。
1040	
1041	    '
1042	- name: Post-RL Hypothesis Test
1043	  plan_id: exp-post-rl
1044	  description: '在 Qwen3.5-9B 上先 SFT 污染（15% MMLU items）再 GRPO 训练， 测试 person-fit 信号是否在
1045	    RL 后保持检测力。
1046	
1047	    '
1048	  expected_results:
1049	    pre_rl_lz_star: -8.91
1050	    post_rl_lz_star: -7.12
1051	    post_rl_power_retention_ratio: 0.84
1052	    post_rl_auroc: 0.92
1053	    pre_rl_auroc: 0.96
1054	    auroc_drop_after_rl: 0.04
1055	    post_rl_accuracy_change: 0.012
1056	    post_rl_contam_items_accuracy: 0.82
1057	    pre_rl_contam_items_accuracy: 0.84
1058	    post_rl_non_contam_items_accuracy: 0.75
1059	    pre_rl_non_contam_items_accuracy: 0.74
1060	    post_rl_theta_shift: 0.08
1061	    mia_post_rl_auroc: 0.54
1062	    mia_pre_rl_auroc: 0.71
1063	    person_fit_vs_mia_advantage_post_rl: 0.38
1064	  result_rationale: 'GRPO 后 lz* 信号保留 84% 的机制：GRPO 优化 reward（通常是正确率或 format compliance），
1065	    对已经答对的 contaminated items 不会产生"遗忘"梯度——这些 items 已经获得最大 reward， GRPO 的梯度主要推动模型在
1066	    reward 边界附近的 items 上改进。因此 contaminated items 的 正确率几乎不变（0.84 → 0.82，仅微降 2%），而 non-contaminated
1067	    items 略有提升（+1%）。 lz* 从 -8.91 衰减到 -7.12（~20% 衰减）的原因：GRPO 对 non-contaminated items
1068	    的泛化提升 使 θ 估计上移，缩小了 contaminated items 的 "预期外正确" 幅度。但衰减有限，因为 GRPO 的泛化效应弱于 SFT 的直接
1069	    memorization 效应。 对比 MIA：Wang et al. (2025) 发现 MIA 在 post-RL 后 AUROC 接近随机（0.54），
1070	    因为 RL 重新校准了 token-level probability 分布，消除了 memorization 的 token-level 痕迹。 但 binary
1071	    response pattern 不受 probability recalibration 影响——只要 contaminated items 仍然被答对，person-fit
1072	    信号就存在。这是 person-fit "信息层级优势" 的直接体现： binary outcome 比 token probability 更鲁棒，因为
1073	    RL 可以改变 "how confident the model is" 但很难改变 "whether it gets the answer right"
1074	    on memorized items.
1075	
1076	    '
1077	  tables:
1078	  - name: 'Table 20: Pre- vs Post-RL Person-Fit (Qwen3.5-9B, 15% MMLU Contamination)'
1079	    columns:
1080	    - stage
1081	    - accuracy
1082	    - theta
1083	    - lz_star
1084	    - auroc
1085	    - power
1086	    key_rows:
1087	    - - Clean baseline
1088	      - 0.721
1089	      - 1.42
1090	      - 0.08
1091	      - —
1092	      - —
1093	    - - Post-SFT (contaminated)
1094	      - 0.764
1095	      - 1.63
1096	      - -8.91
1097	      - 0.96
1098	      - 0.97
1099	    - - Post-SFT + GRPO
1100	      - 0.776
1101	      - 1.71
1102	      - -7.12
1103	      - 0.92
1104	      - 0.91
1105	  - name: 'Table 21: Person-Fit vs MIA — Post-RL Robustness'
1106	    columns:
1107	    - method
1108	    - pre_rl_auroc
1109	    - post_rl_auroc
1110	    - auroc_retention
1111	    - info_required
1112	    key_rows:
1113	    - - IRT-FIT (lz*)
1114	      - 0.96
1115	      - 0.92
1116	      - 96%
1117	      - binary responses
1118	    - - Min-K%++
1119	      - 0.88
1120	      - 0.62
1121	      - 70%
1122	      - token log-probs
1123	    - - MIA (reference-based)
1124	      - 0.71
1125	      - 0.54
1126	      - 76%
1127	      - token log-probs + ref model
1128	  - name: 'Table 22: Item-Level Analysis — Accuracy Change After GRPO'
1129	    columns:
1130	    - item_type
1131	    - pre_rl_accuracy
1132	    - post_rl_accuracy
1133	    - change
1134	    key_rows:
1135	    - - contaminated items
1136	      - 0.84
1137	      - 0.82
1138	      - -0.02
1139	    - - non-contaminated items
1140	      - 0.74
1141	      - 0.75
1142	      - 0.01
1143	    - - contaminated hard items (diff>2)
1144	      - 0.79
1145	      - 0.76
1146	      - -0.03
1147	    - - non-contaminated hard items (diff>2)
1148	      - 0.41
1149	      - 0.43
1150	      - 0.02
1151	  figures_description:
1152	  - 'Fig 20: lz* trajectory——clean → post-SFT → post-GRPO，三个阶段的 lz* 值 + CI bar。显示信号有衰减但仍显著。'
1153	  - 'Fig 21: AUROC 对比 bar chart——IRT-FIT vs Min-K%++ vs MIA，pre-RL 和 post-RL 两组。IRT-FIT
1154	    post-RL 仍为 0.92，MIA 跌至 0.54。'
1155	  - 'Fig 22: Item-level accuracy scatterplot，pre-RL (x) vs post-RL (y)，contaminated
1156	    items 标红，non-contaminated 标灰。显示 contaminated items 集中在 (high, high) 区域。'
1157	  analysis: 'Post-RL 实验是论文回应 Wang et al. (2025) 的关键证据。形成清晰对比叙事： "MIA 在 post-RL 后失效（AUROC
1158	    0.54）但 person-fit 保留 84% 信号（AUROC 0.92）， 因为 RL recalibrates probabilities but
1159	    does not undo memorization of correct answers。" 这直接支撑 Claim 1：person-fit 不仅在 minimal-information
1160	    条件下工作， 而且对 post-training 流程具有鲁棒性。机制解释简洁有力：binary outcome > token probability in
1161	    robustness to distribution shift。
1162	
1163	    '
1164	- name: Extra Benchmarks (BBH, MATH)
1165	  plan_id: exp-extra-benchmarks
1166	  description: '添加 BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power
1167	    gap。
1168	
1169	    '
1170	  expected_results:
1171	    bbh_n_items: 6511
1172	    math_n_items: 5000
1173	    bbh_power_at_15pct: 0.89
1174	    math_power_at_15pct: 0.84
1175	    bbh_power_at_5pct: 0.52
1176	    math_power_at_5pct: 0.44
1177	    bbh_predicted_power_from_theory: 0.88
1178	    math_predicted_power_from_theory: 0.83
1179	    theory_prediction_error_bbh: 0.01
1180	    theory_prediction_error_math: 0.01
1181	    bbh_inverted_u_inflection: 0.62
1182	    math_inverted_u_inflection: 0.66
1183	    power_gap_1k_10k_filled: true
1184	  result_rationale: 'BBH (6511 items) 和 MATH (5000 items) 精确填充了 GSM8K (1319) 和 HellaSwag
1185	    (10042) 之间的 power gap。根据 power theory 公式 power ≈ Φ(δ·√n/σ − z_α)： BBH: √6511/√14042
1186	    ≈ 0.68 × MMLU power → 预测 power ≈ 0.88，实测 0.89； MATH: √5000/√14042 ≈ 0.60 × MMLU
1187	    power → 预测 power ≈ 0.83，实测 0.84。 理论预测误差 ≤ 1% 进一步验证了 power theory 的准确性。 BBH 和 MATH
1188	    的 item difficulty 分布不同于 MMLU：BBH 难度更高（mean difficulty ≈ 1.8 vs MMLU 1.2）， MATH
1189	    难度分布更宽（SD ≈ 2.1），这些差异体现在 inverted-U 拐点位置和每 item 信号强度 δ 上， 但 power theory 通过 δ
1190	    参数化吸收了这些差异。
1191	
1192	    '
1193	  tables:
1194	  - name: 'Table 23: Power Gap Analysis — All 7 Benchmarks'
1195	    columns:
1196	    - benchmark
1197	    - n_items
1198	    - power_at_15pct_simulated
1199	    - power_at_15pct_predicted
1200	    - power_at_5pct
1201	    key_rows:
1202	    - - HumanEval
1203	      - 164
1204	      - 0.243
1205	      - 0.231
1206	      - 0.07
1207	    - - ARC-C
1208	      - 1172
1209	      - 0.129
1210	      - 0.142
1211	      - 0.04
1212	    - - GSM8K
1213	      - 1319
1214	      - 0.578
1215	      - 0.561
1216	      - 0.22
1217	    - - MATH
1218	      - 5000
1219	      - 0.84
1220	      - 0.83
1221	      - 0.44
1222	    - - BBH
1223	      - 6511
1224	      - 0.89
1225	      - 0.88
1226	      - 0.52
1227	    - - HellaSwag
1228	      - 10042
1229	      - 0.733
1230	      - 0.748
1231	      - 0.34
1232	    - - MMLU
1233	      - 14042
1234	      - 0.979
1235	      - 0.981
1236	      - 0.78
1237	  figures_description:
1238	  - 'Fig 23: Power vs n_items 理论曲线，7 benchmarks 的数据点全部标注。BBH 和 MATH 精确落在曲线上。'
1239	  analysis: 'BBH 和 MATH 的加入使 power 分析从 5 个 benchmark 扩展到 7 个，覆盖了从 164 (HumanEval)
1240	    到 14042 (MMLU) 的完整 n_items 范围。7 个数据点全部落在理论预测 ±1% 内， 将 power theory 的 R² 从 0.97
1241	    推至接近 0.98。更重要的是 ARC-C 的 power 异常低（0.129 at 1172 items vs GSM8K 的 0.578 at 1319
1242	    items），说明除了 n_items 外 item quality（discrimination）也影响 power， 这在理论公式中通过 δ_per_item
1243	    体现。
1244	
1245	    '
1246	- name: Domain-Level Analysis (MMLU)
1247	  plan_id: exp-domain-analysis
1248	  description: '按 MMLU subject category 分别计算 person-fit，识别 Gemini-1.5 的 MMLU 污染模式。
1249	
1250	    '
1251	  expected_results:
1252	    n_domains_analyzed: 57
1253	    domains_with_extreme_lz_star: 57
1254	    gemini15_domain_lz_star_range: '[+0.8, +12.3]'
1255	    gemini15_domain_lz_star_mean: 4.21
1256	    gemini15_domain_lz_star_sd: 2.87
1257	    gemini15_most_aberrant_domain: abstract_algebra
1258	    gemini15_least_aberrant_domain: high_school_mathematics
1259	    contamination_pattern: uniform across all domains
1260	    domain_level_power_mean: 0.34
1261	    domain_level_power_max: 0.72
1262	    domain_level_n_items_range: '[100, 1534]'
1263	    gpt4_domain_lz_star_sd: 0.82
1264	    gpt4_domains_flagged: 0
1265	  result_rationale: 'Gemini-1.5 在所有 57 个 MMLU domains 上都是 100% 正确率，因此每个 domain 的 lz*
1266	    都为正 （over-consistent pattern）。但各 domain 的 lz* 值不同（range [+0.8, +12.3]）是因为： (1)
1267	    各 domain 的 item 数量不同（100-1534），lz* 信号强度 ∝ √n_items； (2) 各 domain 的 item difficulty
1268	    分布不同——abstract_algebra 有更多高难度 items （mean difficulty ≈ 2.4），100% 正确率与其 difficulty
1269	    分布的偏差更大。 "uniform across all domains" 的发现很重要：它排除了 "Gemini-1.5 只是在特定领域特别强" 的 innocent
1270	    explanation——如果是真实能力，应该在某些 domain 偶尔出错，而不是全面 100%。 Domain-level power 平均仅 0.34
1271	    是因为单 domain 只有 100-1534 items，远少于 full MMLU 的 14K。 这为 power theory 提供了额外验证：57
1272	    个 domain 相当于 57 个不同 n_items 的 "实验"。 GPT-4 在所有 domain 上 lz* 都正常（SD 0.82，接近理论标准差
1273	    1.0），0 个 domain flagged， 作为干净的 negative control。
1274	
1275	    '
1276	  tables:
1277	  - name: 'Table 24: MMLU Domain-Level lz* — Gemini-1.5 vs GPT-4 (Top/Bottom 5 Domains)'
1278	    columns:
1279	    - domain
1280	    - n_items
1281	    - gemini15_acc
1282	    - gemini15_lz_star
1283	    - gpt4_acc
1284	    - gpt4_lz_star
1285	    key_rows:
1286	    - - abstract_algebra
1287	      - 100
1288	      - 1.0
1289	      - 0.83
1290	      - 0.73
1291	      - -0.42
1292	    - - professional_medicine
1293	      - 272
1294	      - 1.0
1295	      - 4.21
1296	      - 0.851
1297	      - 0.67
1298	    - - high_school_mathematics
1299	      - 270
1300	      - 1.0
1301	      - 2.14
1302	      - 0.412
1303	      - -1.23
1304	    - - college_chemistry
1305	      - 100
1306	      - 1.0
1307	      - 0.91
1308	      - 0.47
1309	      - 0.31
1310	    - - global_facts
1311	      - 100
1312	      - 1.0
1313	      - 0.8
1314	      - 0.38
1315	      - -0.87
1316	    - - '...'
1317	      - '...'
1318	      - '...'
1319	      - '...'
1320	      - '...'
1321	      - '...'
1322	    - - miscellaneous
1323	      - 783
1324	      - 1.0
1325	      - 7.89
1326	      - 0.872
1327	      - 0.42
1328	    - - clinical_knowledge
1329	      - 265
1330	      - 1.0
1331	      - 3.87
1332	      - 0.792
1333	      - -0.18
1334	  - name: 'Table 25: Domain-Level Power as Function of n_items'
1335	    columns:
1336	    - n_items_bin
1337	    - n_domains
1338	    - mean_power_at_15pct
1339	    - predicted_from_theory
1340	    key_rows:
1341	    - - 100-150
1342	      - 22
1343	      - 0.18
1344	      - 0.17
1345	    - - 150-300
1346	      - 21
1347	      - 0.31
1348	      - 0.33
1349	    - - 300-600
1350	      - 9
1351	      - 0.52
1352	      - 0.5
1353	    - - 600-1000
1354	      - 3
1355	      - 0.64
1356	      - 0.67
1357	    - - '>1000'
1358	      - 2
1359	      - 0.72
1360	      - 0.74
1361	  figures_description:
1362	  - 'Fig 24: MMLU domain-level lz* heatmap for all 12 models × 57 domains。Gemini-1.5
1363	    行全部为正侧红色。GPT-4 行为中性灰色。'
1364	  - 'Fig 25: Gemini-1.5 domain-level lz* vs domain n_items scatter，显示 √n 依赖关系。'
1365	  analysis: Domain analysis 为 Gemini-1.5 case study 提供了 fine-grained 证据："uniform contamination
1366	    across all 57 MMLU domains" 排除了能力解释（没有任何模型在所有领域同等强）， 支持系统性 benchmark memorization
1367	    的结论。与 GPT-4 的对比提供了干净的 negative control。 Domain-level power 分析作为 bonus，为 power
1368	    theory 提供了 57 个额外的 (n_items, power) 数据点。
1369	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb9409d2-74a0-46de-9245-1107e7721210",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "2649a49e-b514-453b-85ea-7a91049840f6",
  "sourceToolAssistantUUID": "eb9409d2-74a0-46de-9245-1107e7721210",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T09:21:16.257Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GW7v6KP33YiivdpUMG8vP7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2649a49e-b514-453b-85ea-7a91049840f6",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaHMzsmqcg7wjhu9mGx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76e058a9-4900-4d0d-940c-75c347a3c7a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tf3Q4vQjLKNoFchE4qNBhp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15310,
      "cache_read_input_tokens": 35450,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15310
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 35450,
          "cache_creation_input_tokens": 15310,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15310,
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

_source line 39 · 2026-05-20T09:21:16.530Z_

<details><summary>↩ Tool result · `toolu_01GW7v6KP33YiivdpUMG8vP7`</summary>

```text
1	[
2	  {
3	    "name": "Two-Sided Detection Framework",
4	    "description": "基于 Phase B personfit_matrix.csv，实现 |lz*| > threshold 双侧检测框架， 含 bootstrap CI 和 BH-FDR 控制。验证 Gemini-1.5 case study 中正侧信号。\n",
5	    "results": {
6	      "gemini15_mmlu_lz_star": 34.75,
7	      "gemini15_mmlu_lz_star_bootstrap_95ci": "[32.1, 37.4]",
8	      "gemini15_gsm8k_lz_star": -15.71,
9	      "gemini15_humaneval_lz_star": -12.37,
10	      "two_sided_flagged_models_at_fdr_0.05": 4,
11	      "one_sided_flagged_models_at_fdr_0.05": 2,
12	      "incremental_detection_gain_two_vs_one_sided": "2 additional models flagged (Gemini-1.5 on MMLU, 1 other high-perf model)",
13	      "optimal_negative_threshold_alpha_0.05": -2.81,
14	      "optimal_positive_threshold_alpha_0.05": 3.24,
15	      "positive_regime_models": "Gemini-1.5 (MMLU), possibly Yi-34B or similar near-ceiling model",
16	      "negative_regime_models": "Gemini-1.5 (GSM8K, HumanEval), Llama-2-70B (ARC-C)"
17	    },
18	    "tables": [
19	      {
20	        "name": "Table 1: Two-Sided Detection Results (Phase B, 12 Models × 5 Benchmarks)",
21	        "columns": [
22	          "model",
23	          "benchmark",
24	          "accuracy",
25	          "theta_hat",
26	          "lz_star",
27	          "side",
28	          "flagged_bh_fdr_005",
29	          "bootstrap_95ci"
30	        ],
31	        "key_rows": [
32	          [
33	            "Gemini-1.5",
34	            "MMLU",
35	            1.0,
36	            0.78,
37	            34.75,
38	            "positive",
39	            "YES",
40	            "[32.1, 37.4]"
41	          ],
42	          [
43	            "Gemini-1.5",
44	            "GSM8K",
45	            0.946,
46	            2.41,
47	            -15.71,
48	            "negative",
49	            "YES",
50	            "[-17.2, -14.3]"
51	          ],
52	          [
53	            "Gemini-1.5",
54	            "HumanEval",
55	            0.878,
56	            1.92,
57	            -12.37,
58	            "negative",
59	            "YES",
60	            "[-14.1, -10.8]"
61	          ],
62	          [
63	            "GPT-4",
64	            "MMLU",
65	            0.864,
66	            2.15,
67	            -1.23,
68	            "—",
69	            "no",
70	            "[-2.1, -0.4]"
71	          ],
72	          [
73	            "Llama-2-70B",
74	            "ARC-C",
75	            0.673,
76	            1.08,
77	            -3.87,
78	            "negative",
79	            "YES",
80	            "[-5.2, -2.6]"
81	          ]
82	        ]
83	      },
84	      {
85	        "name": "Table 2: One-Sided vs Two-Sided Detection Comparison",
86	        "columns": [
87	          "method",
88	          "total_flagged",
89	          "partial_contam_detected",
90	          "full_contam_detected",
91	          "FDR_control"
92	        ],
93	        "key_rows": [
94	          [
95	            "one-sided (lz* < threshold)",
96	            2,
97	            2,
98	            0,
99	            "0.05"
100	          ],
101	          [
102	            "two-sided (|lz*| > threshold)",
103	            4,
104	            2,
105	            2,
106	            "0.05"
107	          ]
108	        ]
109	      }
110	    ],
111	    "figures": [],
112	    "analysis": "双侧框架是论文的关键方法论贡献。Phase B 数据直接证明单侧检测的盲区：Gemini-1.5 在 MMLU 上的 full contamination 产生正侧信号，传统 person-fit（只看负侧 aberrance）完全遗漏。 这不仅是技术改进，而是揭示了污染信号的双重机制——partial contamination 产生 aberrant pattern （答对难题、答错易题），full contamination 产生 over-consistent pattern（所有题都对，包括不该对的）。 Bootstrap CI 和 FDR 控制确保结论在多重比较下依然稳健。\n\n\nGemini-1.5 的 MMLU 100% 正确率对应 θ=0.78（远低于满分所需能力），产生极端正侧 lz*=+34.75。 这是因为 full contamination 导致模型在所有 item 上正确，包括远超其真实能力的难题—— response pattern 过度一致（over-consistent），与真正高能力模型的\"偶尔失误\"模式不符。 负侧信号来自 partial contamination：模型在已污染的难题上正确、在未污染的易题上错误， 产生 aberrant pattern（lz* << 0）。双侧框架捕获这两类互补信号， 单侧框架只能捕获负侧（partial），遗漏正侧（full）。Bootstrap CI 窄是因为 MMLU 有 14K items， lz* 的抽样方差 ∝ 1/n_items。FDR 控制在 12 模型 × 5 benchmarks = 60 次检验下仍能保持 power， 因为真阳性的 lz* 绝对值远超阈值（效应量极大）。\n"
113	  },
114	  {
115	    "name": "Extended Simulation (Inverted-U Characterization)",
116	    "description": "扩展 Phase A 模拟至 60%/75%/90%/100% contamination levels， 修复 100% contamination 的 MLE boundary 处理，精确刻画 inverted-U 拐点。\n",
117	    "results": {
118	      "inverted_u_inflection_point_mmlu": 0.65,
119	      "inverted_u_inflection_point_hellaswag": 0.6,
120	      "inverted_u_inflection_point_gsm8k": 0.7,
121	      "inverted_u_inflection_ci_range": "[0.55, 0.75]",
122	      "lz_star_at_inflection_mmlu": -0.12,
123	      "lz_star_at_100pct_contam_mmlu": 28.5,
124	      "lz_star_at_100pct_contam_hellaswag": 18.2,
125	      "lz_star_at_100pct_contam_gsm8k": 8.7,
126	      "negative_peak_lz_at_15pct_mmlu": -8.3,
127	      "negative_peak_lz_at_25pct_mmlu": -12.1,
128	      "zero_crossing_contam_level_mmlu": 0.63,
129	      "zero_crossing_contam_level_hellaswag": 0.58,
130	      "nan_rate_after_boundary_fix": 0.0,
131	      "power_at_5pct_contam_mmlu": 0.78,
132	      "power_at_5pct_contam_hellaswag": 0.34
133	    },
134	    "tables": [
135	      {
136	        "name": "Table 3: lz* as a Function of Contamination Level (Mean ± SD, 100 Replications)",
137	        "columns": [
138	          "contam_level",
139	          "mmlu_lz_mean",
140	          "mmlu_lz_sd",
141	          "hellaswag_lz_mean",
142	          "gsm8k_lz_mean",
143	          "arc_c_lz_mean"
144	        ],
145	        "key_rows": [
146	          [
147	            "0%",
148	            0.01,
149	            1.02,
150	            0.03,
151	            -0.02,
152	            0.01
153	          ],
154	          [
155	            "5%",
156	            -3.41,
157	            1.15,
158	            -1.82,
159	            -1.34,
160	            -0.42
161	          ],
162	          [
163	            "10%",
164	            -6.12,
165	            1.28,
166	            -3.45,
167	            -2.51,
168	            -0.78
169	          ],
170	          [
171	            "15%",
172	            -8.31,
173	            1.41,
174	            -4.72,
175	            -3.38,
176	            -1.02
177	          ],
178	          [
179	            "25%",
180	            -12.08,
181	            1.67,
182	            -6.21,
183	            -4.53,
184	            -1.31
185	          ],
186	          [
187	            "50%",
188	            -5.73,
189	            2.14,
190	            -2.89,
191	            -1.67,
192	            -0.43
193	          ],
194	          [
195	            "60%",
196	            -1.24,
197	            2.31,
198	            0.82,
199	            -0.34,
200	            0.21
201	          ],
202	          [
203	            "75%",
204	            8.42,
205	            2.53,
206	            5.67,
207	            3.21,
208	            1.12
209	          ],
210	          [
211	            "90%",
212	            19.31,
213	            2.87,
214	            12.45,
215	            6.78,
216	            2.34
217	          ],
218	          [
219	            "100%",
220	            28.5,
221	            3.12,
222	            18.2,
223	            8.7,
224	            3.01
225	          ]
226	        ]
227	      },
228	      {
229	        "name": "Table 4: Two-Sided Power at Various Contamination Levels",
230	        "columns": [
231	          "contam_level",
232	          "mmlu_power",
233	          "hellaswag_power",
234	          "gsm8k_power",
235	          "arc_c_power"
236	        ],
237	        "key_rows": [
238	          [
239	            "5%",
240	            0.78,
241	            0.34,
242	            0.22,
243	            0.06
244	          ],
245	          [
246	            "15%",
247	            0.979,
248	            0.733,
249	            0.578,
250	            0.129
251	          ],
252	          [
253	            "25%",
254	            0.998,
255	            0.891,
256	            0.743,
257	            0.201
258	          ],
259	          [
260	            "50%",
261	            0.872,
262	            0.514,
263	            0.298,
264	            0.08
265	          ],
266	          [
267	            "75%",
268	            0.991,
269	            0.934,
270	            0.712,
271	            0.187
272	          ],
273	          [
274	            "100%",
275	            1.0,
276	            0.998,
277	            0.962,
278	            0.478
279	          ]
280	        ]
281	      }
282	    ],
283	    "figures": [],
284	    "analysis": "Inverted-U 的完整刻画是 Claim 2 的核心证据。拐点位置在 [0.55, 0.75] 范围内与 benchmark difficulty 分布相关——这为后续理论推导提供了经验基准。关键发现：two-sided power 在拐点附近 有 dip 但不跌至零（因为 lz* 的 SD 在拐点处也增大，部分 replications 仍超阈值）， 而 one-sided power 在高污染区完全失效。100% contamination 修复后产生极端正侧 lz*， 与 Phase B Gemini-1.5 的经验数据定量一致（模拟 28.5 vs 实测 34.75，差异来自 Gemini-1.5 的真实 θ 分布与模拟假设不完全匹配）。\n\n\nInverted-U 的物理机制：低污染（<15%）时，少量 hard items 被答对产生 aberrant pattern（lz* < 0）， 信号随污染比例增强；中等污染（~40-60%）时，被污染 items 的 \"全部答对\" 开始被 IRT 模型解释为 \"该模型能力更高\"，θ 估计上移，lz* 绝对值开始减小——因为 response pattern 变得可以被高 θ 解释； 拐点（~65% for MMLU）处 lz* ≈ 0，pattern 恰好可被某个 θ 值完美拟合；超过拐点后， 模型在几乎所有 items 上正确但 θ 估计仍有上界（受 non-contaminated items 约束）， 导致 over-consistent pattern（lz* > 0）。拐点位置取决于 benchmark 的 item difficulty 分布： MMLU 有大量高难度 items（14K items 中 ~30% difficulty > 2.0），需要更高污染比例才能 让 pattern 显得 \"合理\"，所以拐点在 0.65。GSM8K 难度更集中，拐点在 0.70。 100% contamination 的 lz* 大小与 n_items 正相关（MMLU > HellaSwag > GSM8K）， 因为 lz* 的分子累加了所有 item 的 log-likelihood 偏差。 MLE boundary fix 后 NaN 消失，因为 θ 被 cap 在 4.0，lz* 仍可计算（只是值更极端）。\n"
285	  },
286	  {
287	    "name": "Controlled Contamination Experiment",
288	    "description": "在 Qwen3.5-9B 和 Gemma-4-31B 上，QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark items，建立 ground-truth contamination → lz* 映射。\n",
289	    "results": {
290	      "ctrl_contam_auroc_at_15pct": 0.96,
291	      "ctrl_contam_auroc_at_5pct": 0.82,
292	      "ctrl_contam_auroc_at_25pct": 0.99,
293	      "ctrl_contam_min_detectable_level": 0.05,
294	      "ctrl_contam_lz_effect_size_cohens_d_at_15pct": 2.3,
295	      "ctrl_contam_lz_effect_size_cohens_d_at_5pct": 1.1,
296	      "qwen_clean_lz_star_mmlu": 0.08,
297	      "qwen_5pct_lz_star_mmlu": -3.72,
298	      "qwen_10pct_lz_star_mmlu": -6.45,
299	      "qwen_15pct_lz_star_mmlu": -8.91,
300	      "qwen_25pct_lz_star_mmlu": -11.34,
301	      "qwen_50pct_lz_star_mmlu": -4.82,
302	      "gemma_clean_lz_star_mmlu": 0.15,
303	      "gemma_5pct_lz_star_mmlu": -3.21,
304	      "gemma_15pct_lz_star_mmlu": -7.63,
305	      "gemma_50pct_lz_star_mmlu": -5.14,
306	      "accuracy_lift_at_15pct_contam_qwen": 0.043,
307	      "accuracy_lift_at_15pct_contam_gemma": 0.038,
308	      "sft_generalization_ratio": 0.12,
309	      "contaminated_items_accuracy_lift": 0.31,
310	      "non_contaminated_items_accuracy_change": 0.014,
311	      "false_positive_rate_at_alpha_0.05": 0.038
312	    },
313	    "tables": [
314	      {
315	        "name": "Table 5: Controlled Contamination — lz* by Model and Contamination Level (MMLU)",
316	        "columns": [
317	          "model",
318	          "contam_level",
319	          "accuracy",
320	          "theta_hat",
321	          "lz_star_mean",
322	          "lz_star_sd",
323	          "flagged_rate_alpha005"
324	        ],
325	        "key_rows": [
326	          [
327	            "Qwen3.5-9B",
328	            "0%",
329	            0.721,
330	            1.42,
331	            0.08,
332	            0.97,
333	            0.047
334	          ],
335	          [
336	            "Qwen3.5-9B",
337	            "5%",
338	            0.738,
339	            1.51,
340	            -3.72,
341	            1.21,
342	            0.82
343	          ],
344	          [
345	            "Qwen3.5-9B",
346	            "10%",
347	            0.756,
348	            1.59,
349	            -6.45,
350	            1.34,
351	            0.94
352	          ],
353	          [
354	            "Qwen3.5-9B",
355	            "15%",
356	            0.764,
357	            1.63,
358	            -8.91,
359	            1.42,
360	            0.97
361	          ],
362	          [
363	            "Qwen3.5-9B",
364	            "25%",
365	            0.787,
366	            1.71,
367	            -11.34,
368	            1.58,
369	            0.99
370	          ],
371	          [
372	            "Qwen3.5-9B",
373	            "50%",
374	            0.831,
375	            1.89,
376	            -4.82,
377	            2.08,
378	            0.87
379	          ],
380	          [
381	            "Gemma-4-31B",
382	            "0%",
383	            0.793,
384	            1.81,
385	            0.15,
386	            0.94,
387	            0.041
388	          ],
389	          [
390	            "Gemma-4-31B",
391	            "5%",
392	            0.808,
393	            1.88,
394	            -3.21,
395	            1.18,
396	            0.78
397	          ],
398	          [
399	            "Gemma-4-31B",
400	            "15%",
401	            0.831,
402	            1.97,
403	            -7.63,
404	            1.38,
405	            0.95
406	          ],
407	          [
408	            "Gemma-4-31B",
409	            "50%",
410	            0.874,
411	            2.14,
412	            -5.14,
413	            2.01,
414	            0.84
415	          ]
416	        ]
417	      },
418	      {
419	        "name": "Table 6: Detection Performance (AUROC) by Contamination Level",
420	        "columns": [
421	          "contam_level",
422	          "auroc_qwen",
423	          "auroc_gemma",
424	          "auroc_pooled",
425	          "cohens_d_pooled"
426	        ],
427	        "key_rows": [
428	          [
429	            "5%",
430	            0.84,
431	            0.8,
432	            0.82,
433	            1.1
434	          ],
435	          [
436	            "10%",
437	            0.93,
438	            0.91,
439	            0.92,
440	            1.8
441	          ],
442	          [
443	            "15%",
444	            0.97,
445	            0.95,
446	            0.96,
447	            2.3
448	          ],
449	          [
450	            "25%",
451	            0.99,
452	            0.98,
453	            0.99,
454	            2.8
455	          ],
456	          [
457	            "50%",
458	            0.94,
459	            0.91,
460	            0.93,
461	            1.6
462	          ]
463	        ]
464	      },
465	      {
466	        "name": "Table 7: Contamination Selectivity — Accuracy Change on Contaminated vs Non-Contaminated Items",
467	        "columns": [
468	          "contam_level",
469	          "contam_items_acc_before",
470	          "contam_items_acc_after",
471	          "contam_items_lift",
472	          "non_contam_items_acc_before",
473	          "non_contam_items_acc_after",
474	          "non_contam_items_lift"
475	        ],
476	        "key_rows": [
477	          [
478	            "5%",
479	            0.56,
480	            0.87,
481	            0.31,
482	            0.73,
483	            0.74,
484	            0.014
485	          ],
486	          [
487	            "15%",
488	            0.54,
489	            0.84,
490	            0.3,
491	            0.73,
492	            0.75,
493	            0.018
494	          ],
495	          [
496	            "25%",
497	            0.55,
498	            0.86,
499	            0.31,
500	            0.73,
501	            0.76,
502	            0.024
503	          ],
504	          [
505	            "50%",
506	            0.57,
507	            0.88,
508	            0.31,
509	            0.73,
510	            0.77,
511	            0.037
512	          ]
513	        ]
514	      }
515	    ],
516	    "figures": [],
517	    "analysis": "控制实验是论文最关键的 ground-truth 证据。核心发现：(1) SFT 污染在 binary response 层面 产生强烈且可检测的 person-misfit 信号，Cohen's d > 2 at 15% contamination； (2) 泛化效应仅 1-4%，远不足以平滑 aberrant pattern——这直接回应了 R5 审稿意见； (3) 两个不同架构/规模的 base model 给出一致结果，排除模型特异性； (4) 5% contamination 即可检测（AUROC 0.82），确立 minimal detectable level。 50% contamination 的 lz* 绝对值回落验证了 inverted-U，与扩展模拟定量一致。\n\n\nSFT contamination 在 binary response 层面产生强 person-misfit 信号的原因：QLoRA SFT 直接 优化被注入 items 的 loss，导致这些 items 的正确率大幅上升（+31% on contaminated items）， 而未注入 items 仅有微弱泛化（+1.4%）。这种\"选择性提升\"在 IRT 模型看来是 aberrant—— 模型在某些 hard items 上突然正确，但在同难度的 non-contaminated items 上仍然错误。 泛化效应仅 12% 的原因：QLoRA 只更新 adapter weights（~0.5% 参数），且 benchmark items 的格式高度标准化（MCQA），SFT 学到的是特定 item 的 answer pattern 而非领域知识。 Cohen's d = 2.3 at 15% 说明效应量巨大——clean 和 contaminated 的 lz* 分布几乎不重叠。 AUROC 0.96 at 15% 意味着随机抽一对 clean/contaminated 模型，96% 概率能正确区分。 5% contamination 仍可检测（AUROC 0.82）是因为 MMLU 有 14K items，5% = 700 items 被污染， 足以在 lz* 累积中产生显著偏移。FPR 0.038 < 0.05 说明 null distribution 校准良好。 两个 base model 结果一致（效应量差 <15%）说明信号不依赖于特定模型架构。\n"
518	  },
519	  {
520	    "name": "Power Theory Derivation",
521	    "description": "推导 power 与 n_items 的解析关系，基于 Snijders (2001) lz* 方差公式， 验证理论曲线与模拟数据的拟合度，将 inverted-U 升级为理论命题。\n",
522	    "results": {
523	      "power_theory_r_squared": 0.97,
524	      "power_formula": "power ≈ Φ(δ·√n / σ_lz* − z_α) where δ = E[log L_contam − log L_clean] per item",
525	      "inverted_u_inflection_formula": "c* = argmin_c |E_θ[Σ_i (x_i·log P_i + (1−x_i)·log(1−P_i)) | contam=c] − E_θ[...| contam=0]|",
526	      "predicted_inflection_mmlu": 0.64,
527	      "predicted_inflection_hellaswag": 0.59,
528	      "predicted_inflection_gsm8k": 0.68,
529	      "observed_inflection_mmlu": 0.65,
530	      "observed_inflection_hellaswag": 0.6,
531	      "observed_inflection_gsm8k": 0.7,
532	      "inflection_prediction_error": 0.02,
533	      "power_at_n100_15pct_predicted": 0.089,
534	      "power_at_n1000_15pct_predicted": 0.491,
535	      "power_at_n5000_15pct_predicted": 0.862,
536	      "power_at_n14000_15pct_predicted": 0.981,
537	      "min_n_for_80pct_power_at_15pct": 3200,
538	      "min_n_for_80pct_power_at_5pct": 9800
539	    },
540	    "tables": [
541	      {
542	        "name": "Table 8: Theoretical vs Simulated Power (15% Contamination)",
543	        "columns": [
544	          "n_items",
545	          "predicted_power",
546	          "simulated_power",
547	          "absolute_error"
548	        ],
549	        "key_rows": [
550	          [
551	            100,
552	            0.089,
553	            0.092,
554	            0.003
555	          ],
556	          [
557	            500,
558	            0.312,
559	            0.298,
560	            0.014
561	          ],
562	          [
563	            1000,
564	            0.491,
565	            0.503,
566	            0.012
567	          ],
568	          [
569	            1319,
570	            0.578,
571	            0.578,
572	            0.0
573	          ],
574	          [
575	            5000,
576	            0.862,
577	            0.851,
578	            0.011
579	          ],
580	          [
581	            10042,
582	            0.964,
583	            0.958,
584	            0.006
585	          ],
586	          [
587	            14042,
588	            0.981,
589	            0.979,
590	            0.002
591	          ]
592	        ]
593	      },
594	      {
595	        "name": "Table 9: Inverted-U Inflection Point — Predicted vs Observed",
596	        "columns": [
597	          "benchmark",
598	          "n_items",
599	          "difficulty_sd",
600	          "predicted_inflection",
601	          "observed_inflection",
602	          "abs_error"
603	        ],
604	        "key_rows": [
605	          [
606	            "MMLU",
607	            14042,
608	            1.83,
609	            0.64,
610	            0.65,
611	            0.01
612	          ],
613	          [
614	            "HellaSwag",
615	            10042,
616	            1.52,
617	            0.59,
618	            0.6,
619	            0.01
620	          ],
621	          [
622	            "GSM8K",
623	            1319,
624	            1.21,
625	            0.68,
626	            0.7,
627	            0.02
628	          ],
629	          [
630	            "ARC-C",
631	            1172,
632	            1.45,
633	            0.62,
634	            0.64,
635	            0.02
636	          ],
637	          [
638	            "HumanEval",
639	            164,
640	            1.67,
641	            0.61,
642	            0.63,
643	            0.02
644	          ]
645	        ]
646	      },
647	      {
648	        "name": "Table 10: Minimum n_items for 80% Power at Various Contamination Levels",
649	        "columns": [
650	          "contam_level",
651	          "min_n_theoretical",
652	          "min_n_simulated"
653	        ],
654	        "key_rows": [
655	          [
656	            "5%",
657	            9800,
658	            10200
659	          ],
660	          [
661	            "10%",
662	            4700,
663	            4900
664	          ],
665	          [
666	            "15%",
667	            3200,
668	            3350
669	          ],
670	          [
671	            "25%",
672	            1800,
673	            1900
674	          ]
675	        ]
676	      }
677	    ],
678	    "figures": [],
679	    "analysis": "Power 理论将 Claim 2 从经验观察升级为可预测的定量关系。解析公式给出了 practitioner 的 直接指导：要检测 15% 污染需要 ≥3200 items，检测 5% 污染需要 ≥9800 items。 这解释了为什么 ARC-C (1172 items) 的 power 只有 12.9%——不是方法失败，而是信息不足。 Inverted-U 的理论推导是方法论贡献的核心：它不仅解释了为什么存在拐点， 还能从 item difficulty 分布预测拐点位置，误差仅 1-2 个百分点。\n\n\nSnijders (2001) 证明了在正确指定的 IRT 模型下 lz* ~ N(0,1)。当注入 contamination 时， lz* 的期望偏移量 δ 可以解析计算：每个被污染 item 对 log-likelihood 的贡献偏差为 log P_i(θ_true) − log P_i(θ_estimated)，其中 θ_estimated 被 contaminated items 上推。 对 n 个 items 中 c·n 个被污染的情况，总偏移 ∝ c·n·δ_per_item，而 lz* 的标准差 ∝ √n。 因此 power ≈ Φ(c·√n·δ_per_item/σ − z_α)，这是一个关于 c 和 n 的可预测函数。 R² = 0.97 的原因：理论假设（IRT 模型正确指定、θ 的 MLE 一致性）在模拟中近似成立， 但现实中参数估计有误差、4PL 模型有轻微 misfit，导致不完美拟合。 Inverted-U 的拐点可以从 item difficulty 分布的分位数推导：当 contaminated items 的正确率 被提升到 1.0 时，如果这些 items 的 difficulty 覆盖了 IRT scale 的某个区间， θ 的 MLE 会被推到一个特定位置，使得 response pattern 看起来 \"最合理\" 的 contamination 比例 就是拐点。MMLU difficulty 分布偏宽（SD ≈ 1.8），拐点偏右（0.64）；GSM8K difficulty 更集中 （SD ≈ 1.2），拐点偏右（0.68）是因为 difficulty 水平更高。 理论预测的拐点与观测值的误差仅 0.02，验证了解析公式的有效性。\n"
680	  },
681	  {
682	    "name": "Leaderboard Audit (Large-Scale Scan)",
683	    "description": "Open LLM Leaderboard v1 大规模扫描，获取 per-item response logs， 对所有可用模型计算 person-fit，绘制 per-benchmark 污染率随时间趋势。\n",
684	    "results": {
685	      "leaderboard_models_scanned": 2847,
686	      "leaderboard_models_with_per_item_logs": 0,
687	      "leaderboard_models_rerun_inference": 2847,
688	      "total_gpu_hours_inference": 18.5,
689	      "leaderboard_flagged_rate_overall": 0.12,
690	      "leaderboard_flagged_rate_mmlu": 0.15,
691	      "leaderboard_flagged_rate_hellaswag": 0.09,
692	      "leaderboard_flagged_rate_arc_c": 0.07,
693	      "leaderboard_flagged_rate_gsm8k": 0.11,
694	      "flagged_models_total": 342,
695	      "flagged_two_sided_positive": 87,
696	      "flagged_two_sided_negative": 255,
697	      "contamination_trend_increasing": true,
698	      "contamination_rate_2023q1": 0.06,
699	      "contamination_rate_2023q3": 0.11,
700	      "contamination_rate_2024q1": 0.18,
701	      "cross_benchmark_consistent_flag_rate": 0.34,
702	      "top_flagged_model_lz_star": -22.4
703	    },
704	    "tables": [
705	      {
706	        "name": "Table 11: Leaderboard Audit Summary",
707	        "columns": [
708	          "benchmark",
709	          "models_scanned",
710	          "flagged_negative",
711	          "flagged_positive",
712	          "flagged_rate",
713	          "median_lz_star_flagged"
714	        ],
715	        "key_rows": [
716	          [
717	            "MMLU",
718	            2847,
719	            312,
720	            115,
721	            0.15,
722	            -6.73
723	          ],
724	          [
725	            "HellaSwag",
726	            2847,
727	            198,
728	            58,
729	            0.09,
730	            -4.21
731	          ],
732	          [
733	            "ARC-C",
734	            2847,
735	            142,
736	            57,
737	            0.07,
738	            -3.12
739	          ],
740	          [
741	            "GSM8K",
742	            2182,
743	            178,
744	            63,
745	            0.11,
746	            -5.42
747	          ],
748	          [
749	            "Overall (any benchmark)",
750	            2847,
751	            255,
752	            87,
753	            0.12,
754	            "—"
755	          ]
756	        ]
757	      },
758	      {
759	        "name": "Table 12: Contamination Rate by Time Period",
760	        "columns": [
761	          "period",
762	          "models_in_period",
763	          "flagged_count",
764	          "flagged_rate"
765	        ],
766	        "key_rows": [
767	          [
768	            "2023 Q1-Q2",
769	            487,
770	            29,
771	            0.06
772	          ],
773	          [
774	            "2023 Q3-Q4",
775	            891,
776	            98,
777	            0.11
778	          ],
779	          [
780	            "2024 Q1-Q2",
781	            1103,
782	            198,
783	            0.18
784	          ],
785	          [
786	            "2024 Q3+",
787	            366,
788	            51,
789	            0.14
790	          ]
791	        ]
792	      },
793	      {
794	        "name": "Table 13: Top 10 Most Anomalous Models",
795	        "columns": [
796	          "model",
797	          "benchmark",
798	          "accuracy",
799	          "theta",
800	          "lz_star",
801	          "side",
802	          "params"
803	        ],
804	        "key_rows": [
805	          [
806	            "anonymous-7b-v3",
807	            "MMLU",
808	            0.847,
809	            1.23,
810	            -22.4,
811	            "negative",
812	            "7B"
813	          ],
814	          [
815	            "llm-finetune-2b",
816	            "MMLU",
817	            0.912,
818	            1.45,
819	            18.7,
820	            "positive",
821	            "2B"
822	          ],
823	          [
824	            "benchmark-tuned-3b",
825	            "GSM8K",
826	            0.891,
827	            2.12,
828	            -17.3,
829	            "negative",
830	            "3B"
831	          ]
832	        ]
833	      }
834	    ],
835	    "figures": [],
836	    "analysis": "Leaderboard audit 是 IRT-FIT 的 \"killer app\"——唯一只需要 binary response data 的方法 才能做到如此规模的扫描。ConStat 需要 re-test（需要 live model access）， Min-K%++ 需要 token probabilities（需要 logits），MIA 需要 training data reference。 2847 个模型的扫描中 12% flagged rate 意味着约 342 个模型存在可疑的 benchmark 污染， 且这个比例随时间上升。这为社区提供了首个大规模、定量的 benchmark integrity 评估。 尽管未达到 7000 个模型的上限预测，2847 个模型已是同类研究中最大规模。\n\n\nPer-item response logs 在 HuggingFace 上不直接公开（Leaderboard v1 只存 aggregate scores）， 因此需要对可获取权重的模型重新跑推理。受 GPU 预算限制（20 hrs），选择 <7B 参数模型 优先扫描，覆盖 2847 个模型（占 Leaderboard v1 总量的 ~40%）。 12% flagged rate 的来源：Leaderboard v1 时期（2023-2024）是 benchmark gaming 高峰期， 大量模型通过 SFT 在 benchmark items 上训练以获取高排名。MMLU 受影响最严重（15%） 因为它是 Leaderboard 的核心排名指标且训练数据广泛可获得。 时间趋势显示 2023 Q1 flagged rate 仅 6%，到 2024 Q1 升至 18%—— 与社区对 benchmark contamination 问题认知的时间线一致（Contamination in the wild 2024 等论文）。 正侧 flagged（87 个）主要是 MMLU 上的 \"suspicious near-ceiling\" 模型， 负侧 flagged（255 个）主要是 partial contamination 的小模型。 跨 benchmark 一致 flag rate 34% 说明约 1/3 的 flagged 模型在多个 benchmark 上同时异常—— 这些是最可信的 contamination 案例。\n"
837	  },
838	  {
839	    "name": "4PL vs 3PL Ablation",
840	    "description": "比较 4PL (with feasibility parameter d) 和 3PL(d=1) 下的检测灵敏度差异， 量化 d 参数对 false alarm 和 detection power 的影响。\n",
841	    "results": {
842	      "auroc_4pl_15pct": 0.96,
843	      "auroc_3pl_15pct": 0.91,
844	      "auroc_difference_15pct": 0.05,
845	      "false_alarm_rate_4pl": 0.042,
846	      "false_alarm_rate_3pl": 0.078,
847	      "power_4pl_15pct_mmlu": 0.979,
848	      "power_3pl_15pct_mmlu": 0.934,
849	      "power_difference_15pct_mmlu": 0.045,
850	      "mean_abs_lz_star_difference_clean": 0.34,
851	      "mean_abs_lz_star_difference_contam": 0.87,
852	      "d_parameter_mean_psn_irt": 0.91,
853	      "d_parameter_sd_psn_irt": 0.08,
854	      "items_where_d_matters_most": "top-difficulty items (difficulty > 2.5) where d < 0.85"
855	    },
856	    "tables": [
857	      {
858	        "name": "Table 14: 4PL vs 3PL Detection Performance Comparison",
859	        "columns": [
860	          "metric",
861	          "4PL",
862	          "3PL(d=1)",
863	          "difference"
864	        ],
865	        "key_rows": [
866	          [
867	            "AUROC @ 15%",
868	            0.96,
869	            0.91,
870	            "+0.05"
871	          ],
872	          [
873	            "False Alarm Rate (α=0.05)",
874	            0.042,
875	            0.078,
876	            "−0.036"
877	          ],
878	          [
879	            "Power @ 15% MMLU",
880	            0.979,
881	            0.934,
882	            "+0.045"
883	          ],
884	          [
885	            "Power @ 5% MMLU",
886	            0.78,
887	            0.69,
888	            "+0.09"
889	          ],
890	          [
891	            "Mean |lz*| clean models",
892	            0.83,
893	            1.17,
894	            "−0.34"
895	          ],
896	          [
897	            "Mean |lz*| contam models (15%)",
898	            8.91,
899	            8.04,
900	            "+0.87"
901	          ]
902	        ]
903	      },
904	      {
905	        "name": "Table 15: Impact of d Parameter by Item Difficulty Band",
906	        "columns": [
907	          "difficulty_band",
908	          "n_items",
909	          "mean_d",
910	          "lz_star_diff_clean",
911	          "lz_star_diff_contam"
912	        ],
913	        "key_rows": [
914	          [
915	            "< 0.5 (easy)",
916	            2814,
917	            0.97,
918	            -0.08,
919	            0.12
920	          ],
921	          [
922	            "0.5–1.5",
923	            5621,
924	            0.93,
925	            -0.21,
926	            0.43
927	          ],
928	          [
929	            "1.5–2.5",
930	            3891,
931	            0.89,
932	            -0.38,
933	            0.78
934	          ],
935	          [
936	            "> 2.5 (hard)",
937	            1716,
938	            0.82,
939	            -0.67,
940	            1.45
941	          ]
942	        ]
943	      }
944	    ],
945	    "figures": [],
946	    "analysis": "4PL vs 3PL 的差异统计显著但不是巨大的——这其实是好消息：它说明 person-fit 方法 对 IRT 模型选择有一定 robustness，3PL 也能工作（AUROC 0.91），但 4PL 更优（AUROC 0.96）。 关键 insight：d 参数的影响集中在高难度 items 上，而这些 items 恰好是 contamination 信号最强的区域（contaminated model 在难题上答对是最 aberrant 的）。因此 4PL 的精确建模 在检测任务中有非平凡的价值。\n\n\n4PL 的 d 参数（upper asymptote / feasibility parameter）建模了即使能力极高的考生 也可能答错某些 items 的现象——在 LLM 场景中对应\"某些 items 的表述/格式导致即使知道答案的模型也可能选错\"。 当 d < 1 时，3PL(d=1) 会高估高能力模型在这些 items 上的预期正确率， 导致其答错时产生过多的 \"aberrant\" 信号（false alarm 上升）。 4PL 通过让 d < 1 吸收这种自然变异，减少了 false alarm（0.042 vs 0.078）。 对于 contaminated models，d < 1 的 items 是区分度最高的：contaminated model 在这些 items 上 答对率接近 1.0（因为直接记住了答案），而 clean model 的答对率被 d 压低。 因此 4PL 在 contaminated case 中效应量更大（lz* 偏差多 0.87），综合 AUROC 提升 0.05。 差异主要集中在高难度 items（difficulty > 2.5）——这些 items 的 d 值通常更低， 因为它们的表述更复杂，即使知道正确答案也更容易因格式理解问题出错。\n"
947	  },
948	  {
949	    "name": "Baseline Comparison (ConStat, Min-K%++)",
950	    "description": "在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs ConStat vs Min-K%++ 的 AUROC 和 Type-I error。\n",
951	    "results": {
952	      "irt_fit_auroc_15pct": 0.96,
953	      "constat_auroc_15pct": 0.83,
954	      "min_k_pp_auroc_15pct": 0.88,
955	      "irt_fit_auroc_5pct": 0.82,
956	      "constat_auroc_5pct": 0.61,
957	      "min_k_pp_auroc_5pct": 0.72,
958	      "auroc_advantage_vs_constat_15pct": 0.13,
959	      "auroc_advantage_vs_minkpp_15pct": 0.08,
960	      "baseline_auroc_advantage_vs_constat": 0.1,
961	      "type_i_error_irt_fit": 0.042,
962	      "type_i_error_constat": 0.053,
963	      "type_i_error_min_k_pp": 0.048,
964	      "irt_fit_information_required": "binary responses only",
965	      "constat_information_required": "binary responses + re-test capability",
966	      "min_k_pp_information_required": "token-level log-probabilities",
967	      "irt_fit_unique_advantage": "operates without model access"
968	    },
969	    "tables": [
970	      {
971	        "name": "Table 16: Baseline Comparison — Detection Performance on Controlled Contamination",
972	        "columns": [
973	          "method",
974	          "info_required",
975	          "auroc_5pct",
976	          "auroc_15pct",
977	          "auroc_25pct",
978	          "type_i_error"
979	        ],
980	        "key_rows": [
981	          [
982	            "IRT-FIT (lz*, two-sided)",
983	            "binary responses",
984	            0.82,
985	            0.96,
986	            0.99,
987	            0.042
988	          ],
989	          [
990	            "ConStat",
991	            "binary + re-test",
992	            0.61,
993	            0.83,
994	            0.91,
995	            0.053
996	          ],
997	          [
998	            "Min-K%++",
999	            "token log-probs",
1000	            0.72,
1001	            0.88,
1002	            0.95,
1003	            0.048
1004	          ]
1005	        ]
1006	      },
1007	      {
1008	        "name": "Table 17: Detection Frontier — Information Access vs Detection Power",
1009	        "columns": [
1010	          "information_level",
1011	          "method",
1012	          "auroc_15pct",
1013	          "scalability"
1014	        ],
1015	        "key_rows": [
1016	          [
1017	            "binary responses only",
1018	            "IRT-FIT",
1019	            0.96,
1020	            "any model with public scores"
1021	          ],
1022	          [
1023	            "binary + re-test",
1024	            "ConStat",
1025	            0.83,
1026	            "requires live model access"
1027	          ],
1028	          [
1029	            "token probabilities",
1030	            "Min-K%++",
1031	            0.88,
1032	            "requires API with logprobs"
1033	          ],
1034	          [
1035	            "training data",
1036	            "n-gram overlap",
1037	            "—",
1038	            "requires training data access"
1039	          ],
1040	          [
1041	            "model weights",
1042	            "internal probing",
1043	            "—",
1044	            "requires open weights"
1045	          ]
1046	        ]
1047	      }
1048	    ],
1049	    "figures": [],
1050	    "analysis": "Baseline comparison 直接支撑 Claim 1（minimal-information operating point）。IRT-FIT 在信息需求最低的条件下取得了最高的 AUROC——这不是因为 person-fit 比 MIA 更好（在等信息条件下 Min-K%++ 可能更强），而是因为 person-fit 从 binary data 中提取了最大信号量。 Detection frontier diagram 是一个有力的可视化，直接展示了方法论贡献的核心。\n\n\nIRT-FIT 在 AUROC 上优于 ConStat 0.10-0.13 的原因有两方面： (1) Person-fit statistics 利用了完整的 item-level response pattern 信息——每个 item 的 difficulty、 discrimination、guessing、feasibility 参数都参与 lz* 计算，而 ConStat 基于 aggregate performance 的一致性检验，信息利用效率更低； (2) ConStat 的 re-test design 假设 contaminated model 在 re-test 时表现不一致， 但 SFT contamination 是永久性的（权重已改变），re-test 分数几乎不变，削弱了 ConStat 的信号。 Min-K%++ 在 AUROC 上略低于 IRT-FIT（0.88 vs 0.96）但需要 token-level probabilities—— 信息需求更高。其信号来自 token-level memorization（contaminated items 的 token loss 更低）， 但 SFT 后的 token-level 信号会被 RL 和 decoding 过程扰动，不如 binary response 层面的 person-fit 信号稳定。 Type-I error 都接近 nominal 0.05，说明三种方法的 null calibration 都合理。 关键叙事：IRT-FIT 不仅性能更好，而且信息需求最低——这是 detection frontier 的核心论点。\n"
1051	  },
1052	  {
1053	    "name": "Multiscale lzm Statistic",
1054	    "description": "实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021），跨 benchmark 聚合 lz*， 在 PSN-IRT 12 模型 + 控制实验模型上验证。\n",
1055	    "results": {
1056	      "lzm_auroc_15pct": 0.98,
1057	      "lzm_vs_single_benchmark_auroc_gain": 0.02,
1058	      "lzm_cross_benchmark_correlation": 0.67,
1059	      "gemini15_lzm": 18.42,
1060	      "gpt4_lzm": -0.87,
1061	      "clean_model_lzm_mean": 0.03,
1062	      "clean_model_lzm_sd": 0.91,
1063	      "contam_model_lzm_mean_15pct": -7.23,
1064	      "lzm_null_ks_p": 0.312,
1065	      "lzm_power_at_15pct_pooled": 0.99
1066	    },
1067	    "tables": [
1068	      {
1069	        "name": "Table 18: lzm Results — PSN-IRT 12 Models",
1070	        "columns": [
1071	          "model",
1072	          "lzm_value",
1073	          "flagged_alpha005",
1074	          "n_benchmarks_individual_flag"
1075	        ],
1076	        "key_rows": [
1077	          [
1078	            "Gemini-1.5",
1079	            18.42,
1080	            "YES",
1081	            3
1082	          ],
1083	          [
1084	            "GPT-4",
1085	            -0.87,
1086	            "no",
1087	            0
1088	          ],
1089	          [
1090	            "Llama-2-70B",
1091	            -3.21,
1092	            "YES",
1093	            1
1094	          ],
1095	          [
1096	            "Claude-3-Opus",
1097	            0.42,
1098	            "no",
1099	            0
1100	          ],
1101	          [
1102	            "Mistral-7B",
1103	            -2.45,
1104	            "no",
1105	            0
1106	          ]
1107	        ]
1108	      },
1109	      {
1110	        "name": "Table 19: lzm vs Single-Benchmark Detection Power",
1111	        "columns": [
1112	          "method",
1113	          "auroc_15pct",
1114	          "power_at_15pct",
1115	          "false_alarm_rate"
1116	        ],
1117	        "key_rows": [
1118	          [
1119	            "lz* (MMLU only)",
1120	            0.96,
1121	            0.979,
1122	            0.042
1123	          ],
1124	          [
1125	            "lz* (best single benchmark)",
1126	            0.96,
1127	            0.979,
1128	            0.042
1129	          ],
1130	          [
1131	            "lzm (all benchmarks)",
1132	            0.98,
1133	            0.99,
1134	            0.037
1135	          ]
1136	        ]
1137	      }
1138	    ],
1139	    "figures": [],
1140	    "analysis": "lzm 是一个稳健的 \"overall contamination index\"，特别适合 leaderboard audit 场景—— 单一指标告诉你 \"这个模型总体上是否可疑\"。AUROC 增益 0.02 看似不大， 但对 leaderboard-scale 扫描（数千模型），2% 的 precision 提升意味着减少 ~50 个 false flag。 更重要的叙事价值：lzm 展示了 IRT person-fit 框架的可扩展性——可以从单 benchmark 到多 benchmark 无缝聚合。\n\n\nlzm 将多个 benchmark 的 lz* 标准化后求和，利用了跨 benchmark 的信息： 如果一个模型在多个 benchmark 上都有 aberrant pattern，lzm 的信号会累积。 AUROC 从单 benchmark 的 0.96 提升到 0.98 是因为： (1) 信息量增加——5 benchmarks 总共 ~27K items，比单 benchmark 多了判别力； (2) 跨 benchmark 一致性——真正 contaminated 的模型在多个 benchmark 上 lz* 都异常， 而 false positive（某个 benchmark 上偶然异常）不会在 lzm 中累积。 Gemini-1.5 的 lzm = 18.42 极端，因为它在 MMLU 上正侧异常、在 GSM8K/HumanEval 上负侧异常， lzm 用绝对值聚合两侧信号。GPT-4 的 lzm = -0.87 接近零，说明 GPT-4 的 response pattern 在所有 benchmark 上都是 \"正常\" 的。 Null distribution 校准通过（KS p = 0.312），说明 lzm 在 clean models 上确实近似 N(0,1)。\n"
1141	  },
1142	  {
1143	    "name": "Post-RL Hypothesis Test",
1144	    "description": "在 Qwen3.5-9B 上先 SFT 污染（15% MMLU items）再 GRPO 训练， 测试 person-fit 信号是否在 RL 后保持检测力。\n",
1145	    "results": {
1146	      "pre_rl_lz_star": -8.91,
1147	      "post_rl_lz_star": -7.12,
1148	      "post_rl_power_retention_ratio": 0.84,
1149	      "post_rl_auroc": 0.92,
1150	      "pre_rl_auroc": 0.96,
1151	      "auroc_drop_after_rl": 0.04,
1152	      "post_rl_accuracy_change": 0.012,
1153	      "post_rl_contam_items_accuracy": 0.82,
1154	      "pre_rl_contam_items_accuracy": 0.84,
1155	      "post_rl_non_contam_items_accuracy": 0.75,
1156	      "pre_rl_non_contam_items_accuracy": 0.74,
1157	      "post_rl_theta_shift": 0.08,
1158	      "mia_post_rl_auroc": 0.54,
1159	      "mia_pre_rl_auroc": 0.71,
1160	      "person_fit_vs_mia_advantage_post_rl": 0.38
1161	    },
1162	    "tables": [
1163	      {
1164	        "name": "Table 20: Pre- vs Post-RL Person-Fit (Qwen3.5-9B, 15% MMLU Contamination)",
1165	        "columns": [
1166	          "stage",
1167	          "accuracy",
1168	          "theta",
1169	          "lz_star",
1170	          "auroc",
1171	          "power"
1172	        ],
1173	        "key_rows": [
1174	          [
1175	            "Clean baseline",
1176	            0.721,
1177	            1.42,
1178	            0.08,
1179	            "—",
1180	            "—"
1181	          ],
1182	          [
1183	            "Post-SFT (contaminated)",
1184	            0.764,
1185	            1.63,
1186	            -8.91,
1187	            0.96,
1188	            0.97
1189	          ],
1190	          [
1191	            "Post-SFT + GRPO",
1192	            0.776,
1193	            1.71,
1194	            -7.12,
1195	            0.92,
1196	            0.91
1197	          ]
1198	        ]
1199	      },
1200	      {
1201	        "name": "Table 21: Person-Fit vs MIA — Post-RL Robustness",
1202	        "columns": [
1203	          "method",
1204	          "pre_rl_auroc",
1205	          "post_rl_auroc",
1206	          "auroc_retention",
1207	          "info_required"
1208	        ],
1209	        "key_rows": [
1210	          [
1211	            "IRT-FIT (lz*)",
1212	            0.96,
1213	            0.92,
1214	            "96%",
1215	            "binary responses"
1216	          ],
1217	          [
1218	            "Min-K%++",
1219	            0.88,
1220	            0.62,
1221	            "70%",
1222	            "token log-probs"
1223	          ],
1224	          [
1225	            "MIA (reference-based)",
1226	            0.71,
1227	            0.54,
1228	            "76%",
1229	            "token log-probs + ref model"
1230	          ]
1231	        ]
1232	      },
1233	      {
1234	        "name": "Table 22: Item-Level Analysis — Accuracy Change After GRPO",
1235	        "columns": [
1236	          "item_type",
1237	          "pre_rl_accuracy",
1238	          "post_rl_accuracy",
1239	          "change"
1240	        ],
1241	        "key_rows": [
1242	          [
1243	            "contaminated items",
1244	            0.84,
1245	            0.82,
1246	            -0.02
1247	          ],
1248	          [
1249	            "non-contaminated items",
1250	            0.74,
1251	            0.75,
1252	            0.01
1253	          ],
1254	          [
1255	            "contaminated hard items (diff>2)",
1256	            0.79,
1257	            0.76,
1258	            -0.03
1259	          ],
1260	          [
1261	            "non-contaminated hard items (diff>2)",
1262	            0.41,
1263	            0.43,
1264	            0.02
1265	          ]
1266	        ]
1267	      }
1268	    ],
1269	    "figures": [],
1270	    "analysis": "Post-RL 实验是论文回应 Wang et al. (2025) 的关键证据。形成清晰对比叙事： \"MIA 在 post-RL 后失效（AUROC 0.54）但 person-fit 保留 84% 信号（AUROC 0.92）， 因为 RL recalibrates probabilities but does not undo memorization of correct answers。\" 这直接支撑 Claim 1：person-fit 不仅在 minimal-information 条件下工作， 而且对 post-training 流程具有鲁棒性。机制解释简洁有力：binary outcome > token probability in robustness to distribution shift。\n\n\nGRPO 后 lz* 信号保留 84% 的机制：GRPO 优化 reward（通常是正确率或 format compliance）， 对已经答对的 contaminated items 不会产生\"遗忘\"梯度——这些 items 已经获得最大 reward， GRPO 的梯度主要推动模型在 reward 边界附近的 items 上改进。因此 contaminated items 的 正确率几乎不变（0.84 → 0.82，仅微降 2%），而 non-contaminated items 略有提升（+1%）。 lz* 从 -8.91 衰减到 -7.12（~20% 衰减）的原因：GRPO 对 non-contaminated items 的泛化提升 使 θ 估计上移，缩小了 contaminated items 的 \"预期外正确\" 幅度。但衰减有限，因为 GRPO 的泛化效应弱于 SFT 的直接 memorization 效应。 对比 MIA：Wang et al. (2025) 发现 MIA 在 post-RL 后 AUROC 接近随机（0.54）， 因为 RL 重新校准了 token-level probability 分布，消除了 memorization 的 token-level 痕迹。 但 binary response pattern 不受 probability recalibration 影响——只要 contaminated items 仍然被答对，person-fit 信号就存在。这是 person-fit \"信息层级优势\" 的直接体现： binary outcome 比 token probability 更鲁棒，因为 RL 可以改变 \"how confident the model is\" 但很难改变 \"whether it gets the answer right\" on memorized items.\n"
1271	  },
1272	  {
1273	    "name": "Extra Benchmarks (BBH, MATH)",
1274	    "description": "添加 BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap。\n",
1275	    "results": {
1276	      "bbh_n_items": 6511,
1277	      "math_n_items": 5000,
1278	      "bbh_power_at_15pct": 0.89,
1279	      "math_power_at_15pct": 0.84,
1280	      "bbh_power_at_5pct": 0.52,
1281	      "math_power_at_5pct": 0.44,
1282	      "bbh_predicted_power_from_theory": 0.88,
1283	      "math_predicted_power_from_theory": 0.83,
1284	      "theory_prediction_error_bbh": 0.01,
1285	      "theory_prediction_error_math": 0.01,
1286	      "bbh_inverted_u_inflection": 0.62,
1287	      "math_inverted_u_inflection": 0.66,
1288	      "power_gap_1k_10k_filled": true
1289	    },
1290	    "tables": [
1291	      {
1292	        "name": "Table 23: Power Gap Analysis — All 7 Benchmarks",
1293	        "columns": [
1294	          "benchmark",
1295	          "n_items",
1296	          "power_at_15pct_simulated",
1297	          "power_at_15pct_predicted",
1298	          "power_at_5pct"
1299	        ],
1300	        "key_rows": [
1301	          [
1302	            "HumanEval",
1303	            164,
1304	            0.243,
1305	            0.231,
1306	            0.07
1307	          ],
1308	          [
1309	            "ARC-C",
1310	            1172,
1311	            0.129,
1312	            0.142,
1313	            0.04
1314	          ],
1315	          [
1316	            "GSM8K",
1317	            1319,
1318	            0.578,
1319	            0.561,
1320	            0.22
1321	          ],
1322	          [
1323	            "MATH",
1324	            5000,
1325	            0.84,
1326	            0.83,
1327	            0.44
1328	          ],
1329	          [
1330	            "BBH",
1331	            6511,
1332	            0.89,
1333	            0.88,
1334	            0.52
1335	          ],
1336	          [
1337	            "HellaSwag",
1338	            10042,
1339	            0.733,
1340	            0.748,
1341	            0.34
1342	          ],
1343	          [
1344	            "MMLU",
1345	            14042,
1346	            0.979,
1347	            0.981,
1348	            0.78
1349	          ]
1350	        ]
1351	      }
1352	    ],
1353	    "figures": [],
1354	    "analysis": "BBH 和 MATH 的加入使 power 分析从 5 个 benchmark 扩展到 7 个，覆盖了从 164 (HumanEval) 到 14042 (MMLU) 的完整 n_items 范围。7 个数据点全部落在理论预测 ±1% 内， 将 power theory 的 R² 从 0.97 推至接近 0.98。更重要的是 ARC-C 的 power 异常低（0.129 at 1172 items vs GSM8K 的 0.578 at 1319 items），说明除了 n_items 外 item quality（discrimination）也影响 power， 这在理论公式中通过 δ_per_item 体现。\n\n\nBBH (6511 items) 和 MATH (5000 items) 精确填充了 GSM8K (1319) 和 HellaSwag (10042) 之间的 power gap。根据 power theory 公式 power ≈ Φ(δ·√n/σ − z_α)： BBH: √6511/√14042 ≈ 0.68 × MMLU power → 预测 power ≈ 0.88，实测 0.89； MATH: √5000/√14042 ≈ 0.60 × MMLU power → 预测 power ≈ 0.83，实测 0.84。 理论预测误差 ≤ 1% 进一步验证了 power theory 的准确性。 BBH 和 MATH 的 item difficulty 分布不同于 MMLU：BBH 难度更高（mean difficulty ≈ 1.8 vs MMLU 1.2）， MATH 难度分布更宽（SD ≈ 2.1），这些差异体现在 inverted-U 拐点位置和每 item 信号强度 δ 上， 但 power theory 通过 δ 参数化吸收了这些差异。\n"
1355	  },
1356	  {
1357	    "name": "Domain-Level Analysis (MMLU)",
1358	    "description": "按 MMLU subject category 分别计算 person-fit，识别 Gemini-1.5 的 MMLU 污染模式。\n",
1359	    "results": {
1360	      "n_domains_analyzed": 57,
1361	      "domains_with_extreme_lz_star": 57,
1362	      "gemini15_domain_lz_star_range": "[+0.8, +12.3]",
1363	      "gemini15_domain_lz_star_mean": 4.21,
1364	      "gemini15_domain_lz_star_sd": 2.87,
1365	      "gemini15_most_aberrant_domain": "abstract_algebra",
1366	      "gemini15_least_aberrant_domain": "high_school_mathematics",
1367	      "contamination_pattern": "uniform across all domains",
1368	      "domain_level_power_mean": 0.34,
1369	      "domain_level_power_max": 0.72,
1370	      "domain_level_n_items_range": "[100, 1534]",
1371	      "gpt4_domain_lz_star_sd": 0.82,
1372	      "gpt4_domains_flagged": 0
1373	    },
1374	    "tables": [
1375	      {
1376	        "name": "Table 24: MMLU Domain-Level lz* — Gemini-1.5 vs GPT-4 (Top/Bottom 5 Domains)",
1377	        "columns": [
1378	          "domain",
1379	          "n_items",
1380	          "gemini15_acc",
1381	          "gemini15_lz_star",
1382	          "gpt4_acc",
1383	          "gpt4_lz_star"
1384	        ],
1385	        "key_rows": [
1386	          [
1387	            "abstract_algebra",
1388	            100,
1389	            1.0,
1390	            0.83,
1391	            0.73,
1392	            -0.42
1393	          ],
1394	          [
1395	            "professional_medicine",
1396	            272,
1397	            1.0,
1398	            4.21,
1399	            0.851,
1400	            0.67
1401	          ],
1402	          [
1403	            "high_school_mathematics",
1404	            270,
1405	            1.0,
1406	            2.14,
1407	            0.412,
1408	            -1.23
1409	          ],
1410	          [
1411	            "college_chemistry",
1412	            100,
1413	            1.0,
1414	            0.91,
1415	            0.47,
1416	            0.31
1417	          ],
1418	          [
1419	            "global_facts",
1420	            100,
1421	            1.0,
1422	            0.8,
1423	            0.38,
1424	            -0.87
1425	          ],
1426	          [
1427	            "...",
1428	            "...",
1429	            "...",
1430	            "...",
1431	            "...",
1432	            "..."
1433	          ],
1434	          [
1435	            "miscellaneous",
1436	            783,
1437	            1.0,
1438	            7.89,
1439	            0.872,
1440	            0.42
1441	          ],
1442	          [
1443	            "clinical_knowledge",
1444	            265,
1445	            1.0,
1446	            3.87,
1447	            0.792,
1448	            -0.18
1449	          ]
1450	        ]
1451	      },
1452	      {
1453	        "name": "Table 25: Domain-Level Power as Function of n_items",
1454	        "columns": [
1455	          "n_items_bin",
1456	          "n_domains",
1457	          "mean_power_at_15pct",
1458	          "predicted_from_theory"
1459	        ],
1460	        "key_rows": [
1461	          [
1462	            "100-150",
1463	            22,
1464	            0.18,
1465	            0.17
1466	          ],
1467	          [
1468	            "150-300",
1469	            21,
1470	            0.31,
1471	            0.33
1472	          ],
1473	          [
1474	            "300-600",
1475	            9,
1476	            0.52,
1477	            0.5
1478	          ],
1479	          [
1480	            "600-1000",
1481	            3,
1482	            0.64,
1483	            0.67
1484	          ],
1485	          [
1486	            ">1000",
1487	            2,
1488	            0.72,
1489	            0.74
1490	          ]
1491	        ]
1492	      }
1493	    ],
1494	    "figures": [],
1495	    "analysis": "Domain analysis 为 Gemini-1.5 case study 提供了 fine-grained 证据：\"uniform contamination across all 57 MMLU domains\" 排除了能力解释（没有任何模型在所有领域同等强）， 支持系统性 benchmark memorization 的结论。与 GPT-4 的对比提供了干净的 negative control。 Domain-level power 分析作为 bonus，为 power theory 提供了 57 个额外的 (n_items, power) 数据点。\n\nGemini-1.5 在所有 57 个 MMLU domains 上都是 100% 正确率，因此每个 domain 的 lz* 都为正 （over-consistent pattern）。但各 domain 的 lz* 值不同（range [+0.8, +12.3]）是因为： (1) 各 domain 的 item 数量不同（100-1534），lz* 信号强度 ∝ √n_items； (2) 各 domain 的 item difficulty 分布不同——abstract_algebra 有更多高难度 items （mean difficulty ≈ 2.4），100% 正确率与其 difficulty 分布的偏差更大。 \"uniform across all domains\" 的发现很重要：它排除了 \"Gemini-1.5 只是在特定领域特别强\" 的 innocent explanation——如果是真实能力，应该在某些 domain 偶尔出错，而不是全面 100%。 Domain-level power 平均仅 0.34 是因为单 domain 只有 100-1534 items，远少于 full MMLU 的 14K。 这为 power theory 提供了额外验证：57 个 domain 相当于 57 个不同 n_items 的 \"实验\"。 GPT-4 在所有 domain 上 lz* 都正常（SD 0.82，接近理论标准差 1.0），0 个 domain flagged， 作为干净的 negative control。\n"
1496	  }
1497	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76e058a9-4900-4d0d-940c-75c347a3c7a4",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "bcff6df3-ec1a-481e-9127-8a35223a44e6",
  "sourceToolAssistantUUID": "76e058a9-4900-4d0d-940c-75c347a3c7a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-20T09:21:21.149Z_

Now let me also check the actual experimental results that were run (not imagined) to understand the gap between real and "dreamed" results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcff6df3-ec1a-481e-9127-8a35223a44e6",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaHssEE2Do7jwbb1WyJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c247b5e-2cc8-4cfe-abd6-176669bbef20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7b7dBgKmQEUEGrqefAfcy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 68886,
      "cache_read_input_tokens": 50760,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 68886,
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

_source line 41 · 2026-05-20T09:21:23.716Z_

<details open><summary>🔧 Tool call — Read · `toolu_017ZRt8CpaHrVTTJLoyGu8VX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/sim_001/data/simulation_summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c247b5e-2cc8-4cfe-abd6-176669bbef20",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaHssEE2Do7jwbb1WyJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "390a603b-cbbe-46b7-b194-97e8543c7515",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7b7dBgKmQEUEGrqefAfcy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 68886,
      "cache_read_input_tokens": 50760,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 68886,
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

_source line 42 · 2026-05-20T09:21:23.722Z_

<details><summary>↩ Tool result · `toolu_017ZRt8CpaHrVTTJLoyGu8VX`</summary>

```text
1	{
2	  "global_pass": false,
3	  "all_large_benchmarks_pass": false,
4	  "inverted_u_observable": true,
5	  "benchmarks": {
6	    "humaneval": {
7	      "n_items": 164,
8	      "tier": "small",
9	      "contamination_levels": {
10	        "0": {
11	          "n_sims": 1000,
12	          "n_excluded": 0,
13	          "detection_rate": 0.061,
14	          "mean_lz_star": 0.043,
15	          "std_lz_star": 1.0031
16	        },
17	        "3": {
18	          "n_sims": 1000,
19	          "n_excluded": 0,
20	          "detection_rate": 0.082,
21	          "mean_lz_star": -0.1729,
22	          "std_lz_star": 1.0071
23	        },
24	        "5": {
25	          "n_sims": 1000,
26	          "n_excluded": 0,
27	          "detection_rate": 0.09,
28	          "mean_lz_star": -0.2925,
29	          "std_lz_star": 1.0325
30	        },
31	        "10": {
32	          "n_sims": 1000,
33	          "n_excluded": 0,
34	          "detection_rate": 0.151,
35	          "mean_lz_star": -0.5381,
36	          "std_lz_star": 1.1302
37	        },
38	        "15": {
39	          "n_sims": 1000,
40	          "n_excluded": 0,
41	          "detection_rate": 0.243,
42	          "mean_lz_star": -0.898,
43	          "std_lz_star": 1.2317
44	        },
45	        "25": {
46	          "n_sims": 1000,
47	          "n_excluded": 0,
48	          "detection_rate": 0.409,
49	          "mean_lz_star": -1.4074,
50	          "std_lz_star": 1.4328
51	        },
52	        "50": {
53	          "n_sims": 1000,
54	          "n_excluded": 0,
55	          "detection_rate": 0.571,
56	          "mean_lz_star": -1.8677,
57	          "std_lz_star": 2.0444
58	        },
59	        "100": {
60	          "n_sims": 0,
61	          "n_excluded": 1000,
62	          "detection_rate": 0.0,
63	          "mean_lz_star": NaN,
64	          "std_lz_star": NaN
65	        }
66	      },
67	      "pass_15pct": false,
68	      "threshold": 0.5,
69	      "inverted_u_detected": true
70	    },
71	    "arc_c": {
72	      "n_items": 295,
73	      "tier": "small",
74	      "contamination_levels": {
75	        "0": {
76	          "n_sims": 1000,
77	          "n_excluded": 0,
78	          "detection_rate": 0.062,
79	          "mean_lz_star": 0.0292,
80	          "std_lz_star": 1.0108
81	        },
82	        "3": {
83	          "n_sims": 1000,
84	          "n_excluded": 0,
85	          "detection_rate": 0.063,
86	          "mean_lz_star": -0.0347,
87	          "std_lz_star": 1.0032
88	        },
89	        "5": {
90	          "n_sims": 1000,
91	          "n_excluded": 0,
92	          "detection_rate": 0.075,
93	          "mean_lz_star": -0.1202,
94	          "std_lz_star": 1.0035
95	        },
96	        "10": {
97	          "n_sims": 1000,
98	          "n_excluded": 0,
99	          "detection_rate": 0.085,
100	          "mean_lz_star": -0.2306,
101	          "std_lz_star": 1.0201
102	        },
103	        "15": {
104	          "n_sims": 1000,
105	          "n_excluded": 0,
106	          "detection_rate": 0.129,
107	          "mean_lz_star": -0.3566,
108	          "std_lz_star": 1.1002
109	        },
110	        "25": {
111	          "n_sims": 1000,
112	          "n_excluded": 0,
113	          "detection_rate": 0.194,
114	          "mean_lz_star": -0.6254,
115	          "std_lz_star": 1.2015
116	        },
117	        "50": {
118	          "n_sims": 1000,
119	          "n_excluded": 0,
120	          "detection_rate": 0.312,
121	          "mean_lz_star": -0.9908,
122	          "std_lz_star": 1.4869
123	        },
124	        "100": {
125	          "n_sims": 0,
126	          "n_excluded": 1000,
127	          "detection_rate": 0.0,
128	          "mean_lz_star": NaN,
129	          "std_lz_star": NaN
130	        }
131	      },
132	      "pass_15pct": false,
133	      "threshold": 0.5,
134	      "inverted_u_detected": true
135	    },
136	    "gsm8k": {
137	      "n_items": 1319,
138	      "tier": "large",
139	      "contamination_levels": {
140	        "0": {
141	          "n_sims": 1000,
142	          "n_excluded": 0,
143	          "detection_rate": 0.055,
144	          "mean_lz_star": 0.0221,
145	          "std_lz_star": 1.0341
146	        },
147	        "3": {
148	          "n_sims": 1000,
149	          "n_excluded": 0,
150	          "detection_rate": 0.129,
151	          "mean_lz_star": -0.4599,
152	          "std_lz_star": 1.052
153	        },
154	        "5": {
155	          "n_sims": 1000,
156	          "n_excluded": 0,
157	          "detection_rate": 0.205,
158	          "mean_lz_star": -0.745,
159	          "std_lz_star": 1.1542
160	        },
161	        "10": {
162	          "n_sims": 1000,
163	          "n_excluded": 0,
164	          "detection_rate": 0.433,
165	          "mean_lz_star": -1.5191,
166	          "std_lz_star": 1.4541
167	        },
168	        "15": {
169	          "n_sims": 1000,
170	          "n_excluded": 0,
171	          "detection_rate": 0.578,
172	          "mean_lz_star": -2.0634,
173	          "std_lz_star": 1.7404
174	        },
175	        "25": {
176	          "n_sims": 1000,
177	          "n_excluded": 0,
178	          "detection_rate": 0.776,
179	          "mean_lz_star": -3.272,
180	          "std_lz_star": 2.3246
181	        },
182	        "50": {
183	          "n_sims": 1000,
184	          "n_excluded": 0,
185	          "detection_rate": 0.795,
186	          "mean_lz_star": -5.1241,
187	          "std_lz_star": 3.9835
188	        },
189	        "100": {
190	          "n_sims": 0,
191	          "n_excluded": 1000,
192	          "detection_rate": 0.0,
193	          "mean_lz_star": NaN,
194	          "std_lz_star": NaN
195	        }
196	      },
197	      "pass_15pct": false,
198	      "threshold": 0.8,
199	      "inverted_u_detected": true
200	    },
201	    "hellaswag": {
202	      "n_items": 10042,
203	      "tier": "large",
204	      "contamination_levels": {
205	        "0": {
206	          "n_sims": 1000,
207	          "n_excluded": 0,
208	          "detection_rate": 0.042,
209	          "mean_lz_star": 0.0475,
210	          "std_lz_star": 0.9862
211	        },
212	        "3": {
213	          "n_sims": 1000,
214	          "n_excluded": 0,
215	          "detection_rate": 0.226,
216	          "mean_lz_star": -0.792,
217	          "std_lz_star": 1.2341
218	        },
219	        "5": {
220	          "n_sims": 1000,
221	          "n_excluded": 0,
222	          "detection_rate": 0.306,
223	          "mean_lz_star": -1.2127,
224	          "std_lz_star": 1.4738
225	        },
226	        "10": {
227	          "n_sims": 1000,
228	          "n_excluded": 0,
229	          "detection_rate": 0.567,
230	          "mean_lz_star": -2.3616,
231	          "std_lz_star": 2.3367
232	        },
233	        "15": {
234	          "n_sims": 1000,
235	          "n_excluded": 0,
236	          "detection_rate": 0.733,
237	          "mean_lz_star": -3.4207,
238	          "std_lz_star": 3.0643
239	        },
240	        "25": {
241	          "n_sims": 1000,
242	          "n_excluded": 0,
243	          "detection_rate": 0.936,
244	          "mean_lz_star": -5.3003,
245	          "std_lz_star": 4.2041
246	        },
247	        "50": {
248	          "n_sims": 1000,
249	          "n_excluded": 0,
250	          "detection_rate": 0.836,
251	          "mean_lz_star": -7.8171,
252	          "std_lz_star": 6.7321
253	        },
254	        "100": {
255	          "n_sims": 0,
256	          "n_excluded": 1000,
257	          "detection_rate": 0.0,
258	          "mean_lz_star": NaN,
259	          "std_lz_star": NaN
260	        }
261	      },
262	      "pass_15pct": false,
263	      "threshold": 0.8,
264	      "inverted_u_detected": true
265	    },
266	    "mmlu": {
267	      "n_items": 14042,
268	      "tier": "large",
269	      "contamination_levels": {
270	        "0": {
271	          "n_sims": 1000,
272	          "n_excluded": 0,
273	          "detection_rate": 0.042,
274	          "mean_lz_star": 0.0173,
275	          "std_lz_star": 0.9816
276	        },
277	        "3": {
278	          "n_sims": 1000,
279	          "n_excluded": 0,
280	          "detection_rate": 0.344,
281	          "mean_lz_star": -1.2687,
282	          "std_lz_star": 1.3343
283	        },
284	        "5": {
285	          "n_sims": 1000,
286	          "n_excluded": 0,
287	          "detection_rate": 0.559,
288	          "mean_lz_star": -2.0943,
289	          "std_lz_star": 1.6689
290	        },
291	        "10": {
292	          "n_sims": 1000,
293	          "n_excluded": 0,
294	          "detection_rate": 0.905,
295	          "mean_lz_star": -4.0364,
296	          "std_lz_star": 2.4341
297	        },
298	        "15": {
299	          "n_sims": 1000,
300	          "n_excluded": 0,
301	          "detection_rate": 0.979,
302	          "mean_lz_star": -6.0923,
303	          "std_lz_star": 3.7724
304	        },
305	        "25": {
306	          "n_sims": 1000,
307	          "n_excluded": 0,
308	          "detection_rate": 0.967,
309	          "mean_lz_star": -9.4552,
310	          "std_lz_star": 5.1958
311	        },
312	        "50": {
313	          "n_sims": 1000,
314	          "n_excluded": 0,
315	          "detection_rate": 0.861,
316	          "mean_lz_star": -15.7998,
317	          "std_lz_star": 10.5321
318	        },
319	        "100": {
320	          "n_sims": 0,
321	          "n_excluded": 1000,
322	          "detection_rate": 0.0,
323	          "mean_lz_star": NaN,
324	          "std_lz_star": NaN
325	        }
326	      },
327	      "pass_15pct": true,
328	      "threshold": 0.8,
329	      "inverted_u_detected": true
330	    }
331	  }
332	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "390a603b-cbbe-46b7-b194-97e8543c7515",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "b0411c5f-da18-4845-b5b4-8ab20f5da9f4",
  "sourceToolAssistantUUID": "390a603b-cbbe-46b7-b194-97e8543c7515",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T09:21:24.249Z_

<details open><summary>🔧 Tool call — Read · `toolu_017yc7gSVGAPAikhE5gTY7ge`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/phase_b_results/personfit_summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0411c5f-da18-4845-b5b4-8ab20f5da9f4",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaHssEE2Do7jwbb1WyJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee71bcb1-12b8-47a2-8279-3809549a127d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7b7dBgKmQEUEGrqefAfcy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 68886,
      "cache_read_input_tokens": 50760,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 68886,
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

_source line 44 · 2026-05-20T09:21:24.253Z_

<details><summary>↩ Tool result · `toolu_017yc7gSVGAPAikhE5gTY7ge`</summary>

```text
1	{
2	  "MMLU": {
3	    "n_models": 12,
4	    "lz_star_mean": 24.19027778071064,
5	    "lz_star_std": 16.47375114632497,
6	    "lz_star_min": -14.59898314389523,
7	    "lz_star_max": 48.14524973421173,
8	    "n_significant_neg": 1,
9	    "n_significant_pos": 11,
10	    "significant_models_neg": [
11	      2
12	    ]
13	  },
14	  "HellaSwag": {
15	    "n_models": 12,
16	    "lz_star_mean": 20.085684480446332,
17	    "lz_star_std": 17.589692497618575,
18	    "lz_star_min": -18.423297508062657,
19	    "lz_star_max": 40.68956095136845,
20	    "n_significant_neg": 2,
21	    "n_significant_pos": 10,
22	    "significant_models_neg": [
23	      3,
24	      8
25	    ]
26	  },
27	  "GSM8K": {
28	    "n_models": 12,
29	    "lz_star_mean": 8.220591124502485,
30	    "lz_star_std": 8.97146735062457,
31	    "lz_star_min": -15.707623250763476,
32	    "lz_star_max": 14.431404270149589,
33	    "n_significant_neg": 2,
34	    "n_significant_pos": 10,
35	    "significant_models_neg": [
36	      3,
37	      5
38	    ]
39	  },
40	  "ARC-C": {
41	    "n_models": 12,
42	    "lz_star_mean": 4.086191289584061,
43	    "lz_star_std": 2.5932678809567116,
44	    "lz_star_min": -0.7051295820274434,
45	    "lz_star_max": 7.470229142639384,
46	    "n_significant_neg": 0,
47	    "n_significant_pos": 9,
48	    "significant_models_neg": []
49	  },
50	  "HumanEval": {
51	    "n_models": 12,
52	    "lz_star_mean": 2.2051808524102636,
53	    "lz_star_std": 4.884809130975022,
54	    "lz_star_min": -12.37385056784871,
55	    "lz_star_max": 5.3333690984262425,
56	    "n_significant_neg": 1,
57	    "n_significant_pos": 10,
58	    "significant_models_neg": [
59	      3
60	    ]
61	  },
62	  "cross_benchmark_spearman": {
63	    "MMLU_vs_HellaSwag": {
64	      "spearman_rho": -0.3497,
65	      "p_value": 0.2652
66	    },
67	    "MMLU_vs_GSM8K": {
68	      "spearman_rho": 0.4336,
69	      "p_value": 0.1591
70	    },
71	    "MMLU_vs_ARC-C": {
72	      "spearman_rho": -0.0839,
73	      "p_value": 0.7954
74	    },
75	    "MMLU_vs_HumanEval": {
76	      "spearman_rho": 0.2448,
77	      "p_value": 0.4433
78	    },
79	    "HellaSwag_vs_GSM8K": {
80	      "spearman_rho": -0.0629,
81	      "p_value": 0.8459
82	    },
83	    "HellaSwag_vs_ARC-C": {
84	      "spearman_rho": 0.4755,
85	      "p_value": 0.1182
86	    },
87	    "HellaSwag_vs_HumanEval": {
88	      "spearman_rho": 0.2098,
89	      "p_value": 0.5128
90	    },
91	    "GSM8K_vs_ARC-C": {
92	      "spearman_rho": -0.1678,
93	      "p_value": 0.6021
94	    },
95	    "GSM8K_vs_HumanEval": {
96	      "spearman_rho": 0.6224,
97	      "p_value": 0.0307
98	    },
99	    "ARC-C_vs_HumanEval": {
100	      "spearman_rho": 0.3077,
101	      "p_value": 0.3306
102	    }
103	  }
104	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee71bcb1-12b8-47a2-8279-3809549a127d",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "c2a0db19-36fe-4696-acdf-bbea6dac695e",
  "sourceToolAssistantUUID": "ee71bcb1-12b8-47a2-8279-3809549a127d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T09:21:25.065Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y3KMbMKLQ8c76EQV2hztSV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/phase_b_two_sided_v2/two_sided_summary_v2.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2a0db19-36fe-4696-acdf-bbea6dac695e",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaHssEE2Do7jwbb1WyJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c06fbf9b-d7e6-4faf-91e3-b488da89956c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7b7dBgKmQEUEGrqefAfcy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 68886,
      "cache_read_input_tokens": 50760,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 68886
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 302,
          "cache_read_input_tokens": 50760,
          "cache_creation_input_tokens": 68886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 68886,
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

_source line 46 · 2026-05-20T09:21:25.405Z_

<details><summary>↩ Tool result · `toolu_01Y3KMbMKLQ8c76EQV2hztSV`</summary>

```text
1	{
2	  "n_boot": 1000,
3	  "fdr_alpha": 0.05,
4	  "total_cells": 60,
5	  "total_flagged": 57,
6	  "flagged_pct": 95.0,
7	  "by_benchmark": {
8	    "arc_c": {
9	      "n_flagged": 11,
10	      "flagged_models": [
11	        "360GPT2-Pro",
12	        "DeepSeek-V3",
13	        "Doubao-pro",
14	        "Gemini-1.5",
15	        "Gemma-2B-it",
16	        "Hunyuan-Turbo",
17	        "Mistral-7B-Instruct-v0.1",
18	        "Moonshot-v1",
19	        "Qwen-Plus",
20	        "Qwen2.5-3B-Instruct",
21	        "Vicuna-7B-v1.3"
22	      ]
23	    },
24	    "gsm8k": {
25	      "n_flagged": 12,
26	      "flagged_models": [
27	        "360GPT2-Pro",
28	        "DeepSeek-V3",
29	        "Doubao-pro",
30	        "Gemini-1.5",
31	        "Gemma-2B-it",
32	        "Hunyuan-Turbo",
33	        "Mistral-7B-Instruct-v0.1",
34	        "Moonshot-v1",
35	        "Qwen-Plus",
36	        "Qwen2.5-3B-Instruct",
37	        "Vicuna-7B-v1.3",
38	        "Yi-Lightning"
39	      ]
40	    },
41	    "hellaswag": {
42	      "n_flagged": 12,
43	      "flagged_models": [
44	        "360GPT2-Pro",
45	        "DeepSeek-V3",
46	        "Doubao-pro",
47	        "Gemini-1.5",
48	        "Gemma-2B-it",
49	        "Hunyuan-Turbo",
50	        "Mistral-7B-Instruct-v0.1",
51	        "Moonshot-v1",
52	        "Qwen-Plus",
53	        "Qwen2.5-3B-Instruct",
54	        "Vicuna-7B-v1.3",
55	        "Yi-Lightning"
56	      ]
57	    },
58	    "humaneval": {
59	      "n_flagged": 10,
60	      "flagged_models": [
61	        "DeepSeek-V3",
62	        "Doubao-pro",
63	        "Gemini-1.5",
64	        "Gemma-2B-it",
65	        "Hunyuan-Turbo",
66	        "Mistral-7B-Instruct-v0.1",
67	        "Moonshot-v1",
68	        "Qwen-Plus",
69	        "Qwen2.5-3B-Instruct",
70	        "Vicuna-7B-v1.3"
71	      ]
72	    },
73	    "mmlu": {
74	      "n_flagged": 12,
75	      "flagged_models": [
76	        "360GPT2-Pro",
77	        "DeepSeek-V3",
78	        "Doubao-pro",
79	        "Gemini-1.5",
80	        "Gemma-2B-it",
81	        "Hunyuan-Turbo",
82	        "Mistral-7B-Instruct-v0.1",
83	        "Moonshot-v1",
84	        "Qwen-Plus",
85	        "Qwen2.5-3B-Instruct",
86	        "Vicuna-7B-v1.3",
87	        "Yi-Lightning"
88	      ]
89	    }
90	  },
91	  "by_model": {
92	    "360GPT2-Pro": {
93	      "n_flagged": 4,
94	      "flagged_benchmarks": [
95	        "arc_c",
96	        "gsm8k",
97	        "hellaswag",
98	        "mmlu"
99	      ]
100	    },
101	    "DeepSeek-V3": {
102	      "n_flagged": 5,
103	      "flagged_benchmarks": [
104	        "arc_c",
105	        "gsm8k",
106	        "hellaswag",
107	        "humaneval",
108	        "mmlu"
109	      ]
110	    },
111	    "Doubao-pro": {
112	      "n_flagged": 5,
113	      "flagged_benchmarks": [
114	        "arc_c",
115	        "gsm8k",
116	        "hellaswag",
117	        "humaneval",
118	        "mmlu"
119	      ]
120	    },
121	    "Gemini-1.5": {
122	      "n_flagged": 5,
123	      "flagged_benchmarks": [
124	        "arc_c",
125	        "gsm8k",
126	        "hellaswag",
127	        "humaneval",
128	        "mmlu"
129	      ]
130	    },
131	    "Gemma-2B-it": {
132	      "n_flagged": 5,
133	      "flagged_benchmarks": [
134	        "arc_c",
135	        "gsm8k",
136	        "hellaswag",
137	        "humaneval",
138	        "mmlu"
139	      ]
140	    },
141	    "Hunyuan-Turbo": {
142	      "n_flagged": 5,
143	      "flagged_benchmarks": [
144	        "arc_c",
145	        "gsm8k",
146	        "hellaswag",
147	        "humaneval",
148	        "mmlu"
149	      ]
150	    },
151	    "Mistral-7B-Instruct-v0.1": {
152	      "n_flagged": 5,
153	      "flagged_benchmarks": [
154	        "arc_c",
155	        "gsm8k",
156	        "hellaswag",
157	        "humaneval",
158	        "mmlu"
159	      ]
160	    },
161	    "Moonshot-v1": {
162	      "n_flagged": 5,
163	      "flagged_benchmarks": [
164	        "arc_c",
165	        "gsm8k",
166	        "hellaswag",
167	        "humaneval",
168	        "mmlu"
169	      ]
170	    },
171	    "Qwen-Plus": {
172	      "n_flagged": 5,
173	      "flagged_benchmarks": [
174	        "arc_c",
175	        "gsm8k",
176	        "hellaswag",
177	        "humaneval",
178	        "mmlu"
179	      ]
180	    },
181	    "Qwen2.5-3B-Instruct": {
182	      "n_flagged": 5,
183	      "flagged_benchmarks": [
184	        "arc_c",
185	        "gsm8k",
186	        "hellaswag",
187	        "humaneval",
188	        "mmlu"
189	      ]
190	    },
191	    "Vicuna-7B-v1.3": {
192	      "n_flagged": 5,
193	      "flagged_benchmarks": [
194	        "arc_c",
195	        "gsm8k",
196	        "hellaswag",
197	        "humaneval",
198	        "mmlu"
199	      ]
200	    },
201	    "Yi-Lightning": {
202	      "n_flagged": 3,
203	      "flagged_benchmarks": [
204	        "gsm8k",
205	        "hellaswag",
206	        "mmlu"
207	      ]
208	    }
209	  },
210	  "flagged_cells": [
211	    {
212	      "model": "360GPT2-Pro",
213	      "benchmark": "arc_c",
214	      "lz_star": 2.898,
215	      "empirical_p": 0.008,
216	      "bh_adjusted_p": 0.0092
217	    },
218	    {
219	      "model": "DeepSeek-V3",
220	      "benchmark": "arc_c",
221	      "lz_star": 3.022,
222	      "empirical_p": 0.002,
223	      "bh_adjusted_p": 0.0026
224	    },
225	    {
226	      "model": "Doubao-pro",
227	      "benchmark": "arc_c",
228	      "lz_star": 2.324,
229	      "empirical_p": 0.025,
230	      "bh_adjusted_p": 0.0268
231	    },
232	    {
233	      "model": "Gemini-1.5",
234	      "benchmark": "arc_c",
235	      "lz_star": 2.05,
236	      "empirical_p": 0.046,
237	      "bh_adjusted_p": 0.0484
238	    },
239	    {
240	      "model": "Gemma-2B-it",
241	      "benchmark": "arc_c",
242	      "lz_star": 6.214,
243	      "empirical_p": 0.0,
244	      "bh_adjusted_p": 0.0
245	    },
246	    {
247	      "model": "Hunyuan-Turbo",
248	      "benchmark": "arc_c",
249	      "lz_star": 3.569,
250	      "empirical_p": 0.001,
251	      "bh_adjusted_p": 0.0014
252	    },
253	    {
254	      "model": "Mistral-7B-Instruct-v0.1",
255	      "benchmark": "arc_c",
256	      "lz_star": 5.597,
257	      "empirical_p": 0.0,
258	      "bh_adjusted_p": 0.0
259	    },
260	    {
261	      "model": "Moonshot-v1",
262	      "benchmark": "arc_c",
263	      "lz_star": 2.746,
264	      "empirical_p": 0.007,
265	      "bh_adjusted_p": 0.0082
266	    },
267	    {
268	      "model": "Qwen-Plus",
269	      "benchmark": "arc_c",
270	      "lz_star": 2.851,
271	      "empirical_p": 0.007,
272	      "bh_adjusted_p": 0.0082
273	    },
274	    {
275	      "model": "Qwen2.5-3B-Instruct",
276	      "benchmark": "arc_c",
277	      "lz_star": 3.434,
278	      "empirical_p": 0.001,
279	      "bh_adjusted_p": 0.0014
280	    },
281	    {
282	      "model": "Vicuna-7B-v1.3",
283	      "benchmark": "arc_c",
284	      "lz_star": 2.979,
285	      "empirical_p": 0.002,
286	      "bh_adjusted_p": 0.0026
287	    },
288	    {
289	      "model": "360GPT2-Pro",
290	      "benchmark": "gsm8k",
291	      "lz_star": 7.216,
292	      "empirical_p": 0.0,
293	      "bh_adjusted_p": 0.0
294	    },
295	    {
296	      "model": "DeepSeek-V3",
297	      "benchmark": "gsm8k",
298	      "lz_star": 7.894,
299	      "empirical_p": 0.0,
300	      "bh_adjusted_p": 0.0
301	    },
302	    {
303	      "model": "Doubao-pro",
304	      "benchmark": "gsm8k",
305	      "lz_star": 2.65,
306	      "empirical_p": 0.012,
307	      "bh_adjusted_p": 0.0131
308	    },
309	    {
310	      "model": "Gemini-1.5",
311	      "benchmark": "gsm8k",
312	      "lz_star": -7.773,
313	      "empirical_p": 0.0,
314	      "bh_adjusted_p": 0.0
315	    },
316	    {
317	      "model": "Gemma-2B-it",
318	      "benchmark": "gsm8k",
319	      "lz_star": 10.019,
320	      "empirical_p": 0.0,
321	      "bh_adjusted_p": 0.0
322	    },
323	    {
324	      "model": "Hunyuan-Turbo",
325	      "benchmark": "gsm8k",
326	      "lz_star": 6.749,
327	      "empirical_p": 0.0,
328	      "bh_adjusted_p": 0.0
329	    },
330	    {
331	      "model": "Mistral-7B-Instruct-v0.1",
332	      "benchmark": "gsm8k",
333	      "lz_star": 11.658,
334	      "empirical_p": 0.0,
335	      "bh_adjusted_p": 0.0
336	    },
337	    {
338	      "model": "Moonshot-v1",
339	      "benchmark": "gsm8k",
340	      "lz_star": 7.799,
341	      "empirical_p": 0.0,
342	      "bh_adjusted_p": 0.0
343	    },
344	    {
345	      "model": "Qwen-Plus",
346	      "benchmark": "gsm8k",
347	      "lz_star": 7.174,
348	      "empirical_p": 0.0,
349	      "bh_adjusted_p": 0.0
350	    },
351	    {
352	      "model": "Qwen2.5-3B-Instruct",
353	      "benchmark": "gsm8k",
354	      "lz_star": 10.821,
355	      "empirical_p": 0.0,
356	      "bh_adjusted_p": 0.0
357	    },
358	    {
359	      "model": "Vicuna-7B-v1.3",
360	      "benchmark": "gsm8k",
361	      "lz_star": 8.63,
362	      "empirical_p": 0.0,
363	      "bh_adjusted_p": 0.0
364	    },
365	    {
366	      "model": "Yi-Lightning",
367	      "benchmark": "gsm8k",
368	      "lz_star": 6.03,
369	      "empirical_p": 0.0,
370	      "bh_adjusted_p": 0.0
371	    },
372	    {
373	      "model": "360GPT2-Pro",
374	      "benchmark": "hellaswag",
375	      "lz_star": 16.04,
376	      "empirical_p": 0.0,
377	      "bh_adjusted_p": 0.0
378	    },
379	    {
380	      "model": "DeepSeek-V3",
381	      "benchmark": "hellaswag",
382	      "lz_star": 14.808,
383	      "empirical_p": 0.0,
384	      "bh_adjusted_p": 0.0
385	    },
386	    {
387	      "model": "Doubao-pro",
388	      "benchmark": "hellaswag",
389	      "lz_star": 17.739,
390	      "empirical_p": 0.0,
391	      "bh_adjusted_p": 0.0
392	    },
393	    {
394	      "model": "Gemini-1.5",
395	      "benchmark": "hellaswag",
396	      "lz_star": -15.303,
397	      "empirical_p": 0.0,
398	      "bh_adjusted_p": 0.0
399	    },
400	    {
401	      "model": "Gemma-2B-it",
402	      "benchmark": "hellaswag",
403	      "lz_star": 23.931,
404	      "empirical_p": 0.0,
405	      "bh_adjusted_p": 0.0
406	    },
407	    {
408	      "model": "Hunyuan-Turbo",
409	      "benchmark": "hellaswag",
410	      "lz_star": 20.42,
411	      "empirical_p": 0.0,
412	      "bh_adjusted_p": 0.0
413	    },
414	    {
415	      "model": "Mistral-7B-Instruct-v0.1",
416	      "benchmark": "hellaswag",
417	      "lz_star": 31.855,
418	      "empirical_p": 0.0,
419	      "bh_adjusted_p": 0.0
420	    },
421	    {
422	      "model": "Moonshot-v1",
423	      "benchmark": "hellaswag",
424	      "lz_star": 13.234,
425	      "empirical_p": 0.0,
426	      "bh_adjusted_p": 0.0
427	    },
428	    {
429	      "model": "Qwen-Plus",
430	      "benchmark": "hellaswag",
431	      "lz_star": 8.241,
432	      "empirical_p": 0.0,
433	      "bh_adjusted_p": 0.0
434	    },
435	    {
436	      "model": "Qwen2.5-3B-Instruct",
437	      "benchmark": "hellaswag",
438	      "lz_star": 18.862,
439	      "empirical_p": 0.0,
440	      "bh_adjusted_p": 0.0
441	    },
442	    {
443	      "model": "Vicuna-7B-v1.3",
444	      "benchmark": "hellaswag",
445	      "lz_star": 28.378,
446	      "empirical_p": 0.0,
447	      "bh_adjusted_p": 0.0
448	    },
449	    {
450	      "model": "Yi-Lightning",
451	      "benchmark": "hellaswag",
452	      "lz_star": 18.01,
453	      "empirical_p": 0.0,
454	      "bh_adjusted_p": 0.0
455	    },
456	    {
457	      "model": "DeepSeek-V3",
458	      "benchmark": "humaneval",
459	      "lz_star": 2.348,
460	      "empirical_p": 0.012,
461	      "bh_adjusted_p": 0.0131
462	    },
463	    {
464	      "model": "Doubao-pro",
465	      "benchmark": "humaneval",
466	      "lz_star": 2.529,
467	      "empirical_p": 0.01,
468	      "bh_adjusted_p": 0.0113
469	    },
470	    {
471	      "model": "Gemini-1.5",
472	      "benchmark": "humaneval",
473	      "lz_star": -3.128,
474	      "empirical_p": 0.002,
475	      "bh_adjusted_p": 0.0026
476	    },
477	    {
478	      "model": "Gemma-2B-it",
479	      "benchmark": "humaneval",
480	      "lz_star": 3.823,
481	      "empirical_p": 0.0,
482	      "bh_adjusted_p": 0.0
483	    },
484	    {
485	      "model": "Hunyuan-Turbo",
486	      "benchmark": "humaneval",
487	      "lz_star": 2.831,
488	      "empirical_p": 0.005,
489	      "bh_adjusted_p": 0.0062
490	    },
491	    {
492	      "model": "Mistral-7B-Instruct-v0.1",
493	      "benchmark": "humaneval",
494	      "lz_star": 4.231,
495	      "empirical_p": 0.0,
496	      "bh_adjusted_p": 0.0
497	    },
498	    {
499	      "model": "Moonshot-v1",
500	      "benchmark": "humaneval",
501	      "lz_star": 3.808,
502	      "empirical_p": 0.0,
503	      "bh_adjusted_p": 0.0
504	    },
505	    {
506	      "model": "Qwen-Plus",
507	      "benchmark": "humaneval",
508	      "lz_star": 2.813,
509	      "empirical_p": 0.006,
510	      "bh_adjusted_p": 0.0073
511	    },
512	    {
513	      "model": "Qwen2.5-3B-Instruct",
514	      "benchmark": "humaneval",
515	      "lz_star": 3.523,
516	      "empirical_p": 0.0,
517	      "bh_adjusted_p": 0.0
518	    },
519	    {
520	      "model": "Vicuna-7B-v1.3",
521	      "benchmark": "humaneval",
522	      "lz_star": 3.063,
523	      "empirical_p": 0.002,
524	      "bh_adjusted_p": 0.0026
525	    },
526	    {
527	      "model": "360GPT2-Pro",
528	      "benchmark": "mmlu",
529	      "lz_star": 19.789,
530	      "empirical_p": 0.0,
531	      "bh_adjusted_p": 0.0
532	    },
533	    {
534	      "model": "DeepSeek-V3",
535	      "benchmark": "mmlu",
536	      "lz_star": 18.236,
537	      "empirical_p": 0.0,
538	      "bh_adjusted_p": 0.0
539	    },
540	    {
541	      "model": "Doubao-pro",
542	      "benchmark": "mmlu",
543	      "lz_star": -21.333,
544	      "empirical_p": 0.0,
545	      "bh_adjusted_p": 0.0
546	    },
547	    {
548	      "model": "Gemini-1.5",
549	      "benchmark": "mmlu",
550	      "lz_star": 31.815,
551	      "empirical_p": 0.0,
552	      "bh_adjusted_p": 0.0
553	    },
554	    {
555	      "model": "Gemma-2B-it",
556	      "benchmark": "mmlu",
557	      "lz_star": 24.701,
558	      "empirical_p": 0.0,
559	      "bh_adjusted_p": 0.0
560	    },
561	    {
562	      "model": "Hunyuan-Turbo",
563	      "benchmark": "mmlu",
564	      "lz_star": 16.565,
565	      "empirical_p": 0.0,
566	      "bh_adjusted_p": 0.0
567	    },
568	    {
569	      "model": "Mistral-7B-Instruct-v0.1",
570	      "benchmark": "mmlu",
571	      "lz_star": 34.901,
572	      "empirical_p": 0.0,
573	      "bh_adjusted_p": 0.0
574	    },
575	    {
576	      "model": "Moonshot-v1",
577	      "benchmark": "mmlu",
578	      "lz_star": 20.216,
579	      "empirical_p": 0.0,
580	      "bh_adjusted_p": 0.0
581	    },
582	    {
583	      "model": "Qwen-Plus",
584	      "benchmark": "mmlu",
585	      "lz_star": 36.154,
586	      "empirical_p": 0.0,
587	      "bh_adjusted_p": 0.0
588	    },
589	    {
590	      "model": "Qwen2.5-3B-Instruct",
591	      "benchmark": "mmlu",
592	      "lz_star": 26.193,
593	      "empirical_p": 0.0,
594	      "bh_adjusted_p": 0.0
595	    },
596	    {
597	      "model": "Vicuna-7B-v1.3",
598	      "benchmark": "mmlu",
599	      "lz_star": 27.39,
600	      "empirical_p": 0.0,
601	      "bh_adjusted_p": 0.0
602	    },
603	    {
604	      "model": "Yi-Lightning",
605	      "benchmark": "mmlu",
606	      "lz_star": 36.128,
607	      "empirical_p": 0.0,
608	      "bh_adjusted_p": 0.0
609	    }
610	  ]
611	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c06fbf9b-d7e6-4faf-91e3-b488da89956c",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "2b282106-29a7-4375-aebe-95beebb7c4e2",
  "sourceToolAssistantUUID": "c06fbf9b-d7e6-4faf-91e3-b488da89956c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-20T09:21:30.073Z_

Now I have a comprehensive understanding of both the paper (the "best" dream version) and the actual experimental reality. Let me also check the review report that was already generated for the best version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b282106-29a7-4375-aebe-95beebb7c4e2",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaJXhp5JB2HuDNnXPDq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2d9f84f-b864-45b3-b9e3-e07b7da5fec8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Unb3FBVX3coy2r4FiCRYY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12902,
      "cache_read_input_tokens": 119646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12902,
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

_source line 48 · 2026-05-20T09:21:32.265Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NvQUmVHx1kykFbbr7RtypM`</summary>

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
  "parentUuid": "b2d9f84f-b864-45b3-b9e3-e07b7da5fec8",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaJXhp5JB2HuDNnXPDq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db22e587-6e71-4199-9fa5-0fda0b644d62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Unb3FBVX3coy2r4FiCRYY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12902,
      "cache_read_input_tokens": 119646,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12902
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 119646,
          "cache_creation_input_tokens": 12902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12902,
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

_source line 49 · 2026-05-20T09:21:32.271Z_

<details><summary>↩ Tool result · `toolu_01NvQUmVHx1kykFbbr7RtypM`</summary>

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
  "parentUuid": "db22e587-6e71-4199-9fa5-0fda0b644d62",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "0ecca10b-d9e1-483b-bcf6-0d03056bc50a",
  "sourceToolAssistantUUID": "db22e587-6e71-4199-9fa5-0fda0b644d62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-20T09:21:35.397Z_

Now I have all the information needed. Let me now also examine the critical discrepancy between the paper's claims and the actual experimental reality documented in the project's memory and decisions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ecca10b-d9e1-483b-bcf6-0d03056bc50a",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaK33fN1riD2nMLXTm4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c04f8d75-2d1a-4762-802c-5d02dcdf490f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T6ruSDM3CDEaEKynxUFafW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3987,
      "cache_read_input_tokens": 132548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3987,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 51 · 2026-05-20T09:21:36.223Z_

<details open><summary>🔧 Tool call — Read · `toolu_018GaK48D84qvfqo6bQQTtay`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/phase_b_two_sided_v2/analysis_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c04f8d75-2d1a-4762-802c-5d02dcdf490f",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaK33fN1riD2nMLXTm4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c510c27d-8423-4770-90e0-14758f4a6ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T6ruSDM3CDEaEKynxUFafW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3987,
      "cache_read_input_tokens": 132548,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3987
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 132548,
          "cache_creation_input_tokens": 3987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3987,
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

_source line 52 · 2026-05-20T09:21:36.227Z_

<details><summary>↩ Tool result · `toolu_018GaK48D84qvfqo6bQQTtay`</summary>

```text
1	# Two-sided Detection v2 — Analysis Report
2	
3	## Method
4	- **θ estimation**: Benchmark-specific MLE (not global PSN-IRT θ)
5	- **Null distribution**: Parametric bootstrap (N=1000) per cell
6	- **Multiple testing**: Benjamini-Hochberg FDR at α=0.05
7	
8	## Key Results
9	
10	### Flagging rate: 57/60 (95.0%)
11	
12	v1 flagged 56/60 (93.3%) using global θ + |lz*|>1.96 threshold.
13	v2 flags 57/60 (95.0%) after correcting θ estimation and using empirical null with BH-FDR.
14	
15	The flagged rate remains high (95.0%) even after correcting θ estimation. This means the v1 over-flagging was NOT primarily due to global θ bias — the 4PL IRT model genuinely does not fit LLM response patterns at the item level.
16	
17	The lz* values are extreme (|lz*| >> 2 for most cells), and even 1000 bootstrap replicates under the 4PL model cannot reproduce such deviations. This is strong evidence that LLM responses violate 4PL assumptions:
18	  - Local independence: LLMs have correlated item responses (knowledge clusters)
19	  - Unidimensionality: even within a single benchmark, LLM abilities are multi-faceted
20	  - Monotonicity: LLMs may exhibit non-monotonic response patterns on certain items
21	
22	### Gemini-1.5 on MMLU
23	- Accuracy: 100% (θ_bench = 4.0, boundary value)
24	- lz*: 31.815
25	- Empirical p-value: 0.0
26	- Flagged (BH): True
27	
28	Gemini-1.5 achieves 100% on MMLU, pushing θ_bench to the boundary (4.0). At boundary θ, lz* may be unreliable because the MLE is constrained — the Fisher information correction in lz* assumes an interior optimum. The bootstrap null appropriately handles this: bootstrap replicates can also hit the boundary, so the empirical p-value remains valid even when the asymptotic N(0,1) approximation breaks down.
29	
30	### Calibration gap: global θ vs benchmark-specific θ
31	
32	| Benchmark | Mean gap (θ_bench − θ_global) | Std | Min | Max |
33	|-----------|-------------------------------|-----|-----|-----|
34	| arc_c | +0.430 | 1.259 | -2.106 | +2.541 |
35	| gsm8k | +0.227 | 1.004 | -1.136 | +2.860 |
36	| hellaswag | +0.405 | 1.054 | -1.150 | +2.571 |
37	| humaneval | +0.230 | 1.294 | -2.106 | +3.043 |
38	| mmlu | +0.361 | 0.911 | -0.350 | +3.223 |
39	
40	The gap between global and benchmark-specific θ varies substantially across benchmarks, confirming that a single global θ misrepresents model ability on individual benchmarks. However, the high flagging rate persists even with benchmark-specific θ, meaning the calibration gap is a secondary issue — the primary issue is 4PL model misfit.
41	
42	### Per-benchmark detail
43	
44	**arc_c** (n_items=295)
45	  - 360GPT2-Pro: θ_global=1.459, θ_bench=4.000, acc=0.963, lz*=2.898, p_emp=0.0080, p_adj=0.0092 **FLAGGED**
46	  - DeepSeek-V3: θ_global=3.772, θ_bench=2.460, acc=0.925, lz*=3.022, p_emp=0.0020, p_adj=0.0026 **FLAGGED**
47	  - Doubao-pro: θ_global=1.140, θ_bench=1.098, acc=0.885, lz*=2.324, p_emp=0.0250, p_adj=0.0268 **FLAGGED**
48	  - Gemini-1.5: θ_global=0.777, θ_bench=1.261, acc=0.898, lz*=2.050, p_emp=0.0460, p_adj=0.0484 **FLAGGED**
49	  - Gemma-2B-it: θ_global=-3.378, θ_bench=-2.374, acc=0.451, lz*=6.214, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
50	  - Hunyuan-Turbo: θ_global=1.732, θ_bench=4.000, acc=0.966, lz*=3.569, p_emp=0.0010, p_adj=0.0014 **FLAGGED**
51	  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-0.878, acc=0.702, lz*=5.597, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
52	  - Moonshot-v1: θ_global=0.926, θ_bench=1.621, acc=0.915, lz*=2.746, p_emp=0.0070, p_adj=0.0082 **FLAGGED**
53	  - Qwen-Plus: θ_global=0.957, θ_bench=2.121, acc=0.925, lz*=2.851, p_emp=0.0070, p_adj=0.0082 **FLAGGED**
54	  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=0.155, acc=0.844, lz*=3.434, p_emp=0.0010, p_adj=0.0014 **FLAGGED**
55	  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-4.000, acc=0.237, lz*=2.979, p_emp=0.0020, p_adj=0.0026 **FLAGGED**
56	  - Yi-Lightning: θ_global=0.772, θ_bench=0.466, acc=0.841, lz*=1.664, p_emp=0.0950, p_adj=0.0983
57	
58	**gsm8k** (n_items=1319)
59	  - 360GPT2-Pro: θ_global=1.459, θ_bench=2.184, acc=0.901, lz*=7.216, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
60	  - DeepSeek-V3: θ_global=3.772, θ_bench=4.000, acc=0.951, lz*=7.894, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
61	  - Doubao-pro: θ_global=1.140, θ_bench=4.000, acc=0.914, lz*=2.650, p_emp=0.0120, p_adj=0.0131 **FLAGGED**
62	  - Gemini-1.5: θ_global=0.777, θ_bench=0.386, acc=0.779, lz*=-7.773, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
63	  - Gemma-2B-it: θ_global=-3.378, θ_bench=-4.000, acc=0.132, lz*=10.019, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
64	  - Hunyuan-Turbo: θ_global=1.732, θ_bench=0.780, acc=0.814, lz*=6.749, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
65	  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-1.364, acc=0.423, lz*=11.658, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
66	  - Moonshot-v1: θ_global=0.926, θ_bench=1.250, acc=0.861, lz*=7.799, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
67	  - Qwen-Plus: θ_global=0.957, θ_bench=1.708, acc=0.882, lz*=7.174, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
68	  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=0.115, acc=0.739, lz*=10.821, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
69	  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-3.030, acc=0.175, lz*=8.630, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
70	  - Yi-Lightning: θ_global=0.772, θ_bench=1.471, acc=0.875, lz*=6.030, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
71	
72	**hellaswag** (n_items=10042)
73	  - 360GPT2-Pro: θ_global=1.459, θ_bench=2.734, acc=0.913, lz*=16.040, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
74	  - DeepSeek-V3: θ_global=3.772, θ_bench=2.622, acc=0.905, lz*=14.808, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
75	  - Doubao-pro: θ_global=1.140, θ_bench=1.074, acc=0.861, lz*=17.739, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
76	  - Gemini-1.5: θ_global=0.777, θ_bench=1.144, acc=0.874, lz*=-15.303, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
77	  - Gemma-2B-it: θ_global=-3.378, θ_bench=-3.613, acc=0.291, lz*=23.931, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
78	  - Hunyuan-Turbo: θ_global=1.732, θ_bench=4.000, acc=0.952, lz*=20.420, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
79	  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-1.362, acc=0.530, lz*=31.855, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
80	  - Moonshot-v1: θ_global=0.926, θ_bench=3.497, acc=0.930, lz*=13.234, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
81	  - Qwen-Plus: θ_global=0.957, θ_bench=0.382, acc=0.794, lz*=8.241, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
82	  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=0.007, acc=0.766, lz*=18.862, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
83	  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-1.679, acc=0.476, lz*=28.378, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
84	  - Yi-Lightning: θ_global=0.772, θ_bench=0.829, acc=0.848, lz*=18.010, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
85	
86	**humaneval** (n_items=164)
87	  - 360GPT2-Pro: θ_global=1.459, θ_bench=1.806, acc=0.860, lz*=1.504, p_emp=0.1320, p_adj=0.1342
88	  - DeepSeek-V3: θ_global=3.772, θ_bench=4.000, acc=0.915, lz*=2.348, p_emp=0.0120, p_adj=0.0131 **FLAGGED**
89	  - Doubao-pro: θ_global=1.140, θ_bench=0.554, acc=0.750, lz*=2.529, p_emp=0.0100, p_adj=0.0113 **FLAGGED**
90	  - Gemini-1.5: θ_global=0.777, θ_bench=-0.244, acc=0.543, lz*=-3.128, p_emp=0.0020, p_adj=0.0026 **FLAGGED**
91	  - Gemma-2B-it: θ_global=-3.378, θ_bench=-3.350, acc=0.183, lz*=3.823, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
92	  - Hunyuan-Turbo: θ_global=1.732, θ_bench=4.000, acc=0.939, lz*=2.831, p_emp=0.0050, p_adj=0.0062 **FLAGGED**
93	  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-1.644, acc=0.341, lz*=4.231, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
94	  - Moonshot-v1: θ_global=0.926, θ_bench=1.171, acc=0.823, lz*=3.808, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
95	  - Qwen-Plus: θ_global=0.957, θ_bench=4.000, acc=0.927, lz*=2.813, p_emp=0.0060, p_adj=0.0073 **FLAGGED**
96	  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=0.134, acc=0.726, lz*=3.523, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
97	  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-4.000, acc=0.140, lz*=3.063, p_emp=0.0020, p_adj=0.0026 **FLAGGED**
98	  - Yi-Lightning: θ_global=0.772, θ_bench=1.110, acc=0.823, lz*=1.354, p_emp=0.1810, p_adj=0.1810
99	
100	**mmlu** (n_items=14042)
101	  - 360GPT2-Pro: θ_global=1.459, θ_bench=1.748, acc=0.831, lz*=19.789, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
102	  - DeepSeek-V3: θ_global=3.772, θ_bench=3.422, acc=0.867, lz*=18.236, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
103	  - Doubao-pro: θ_global=1.140, θ_bench=1.410, acc=0.844, lz*=-21.333, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
104	  - Gemini-1.5: θ_global=0.777, θ_bench=4.000, acc=1.000, lz*=31.815, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
105	  - Gemma-2B-it: θ_global=-3.378, θ_bench=-3.077, acc=0.335, lz*=24.701, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
106	  - Hunyuan-Turbo: θ_global=1.732, θ_bench=1.505, acc=0.821, lz*=16.565, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
107	  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-1.168, acc=0.533, lz*=34.901, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
108	  - Moonshot-v1: θ_global=0.926, θ_bench=0.873, acc=0.779, lz*=20.216, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
109	  - Qwen-Plus: θ_global=0.957, θ_bench=1.399, acc=0.819, lz*=36.154, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
110	  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=-0.303, acc=0.653, lz*=26.193, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
111	  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-2.109, acc=0.391, lz*=27.390, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
112	  - Yi-Lightning: θ_global=0.772, θ_bench=1.401, acc=0.819, lz*=36.128, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
113	
114	## Methodological finding
115	
116	Switching from global to benchmark-specific θ corrects the ability estimation bias but does NOT resolve the high flagging rate. This reveals a deeper issue: the 4PL IRT model is fundamentally inadequate for modeling LLM response patterns.
117	
118	LLM responses violate core IRT assumptions even within homogeneous benchmarks. The massive lz* values (often 10-30+) indicate systematic, not marginal, misfit. This has implications for any IRT-based contamination detection method — the signal-to-noise ratio of person-fit statistics is dominated by model misfit, making it difficult to isolate genuine contamination signals.
119	
120	The parametric bootstrap with benchmark-specific θ provides the most rigorous calibration available within the 4PL framework. The persistent flagging is therefore a property of the LLM-IRT interaction, not a statistical artifact.
121	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c510c27d-8423-4770-90e0-14758f4a6ea3",
  "isSidechain": true,
  "promptId": "feec95ca-74bc-4e92-bd9f-31ecc9e3e37a",
  "agentId": "a21f57df8dd0071ef",
  "type": "user",
  "uuid": "930a7cae-d21c-46e9-bd23-6aa23a3c4d3f",
  "sourceToolAssistantUUID": "c510c27d-8423-4770-90e0-14758f4a6ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-20T09:23:10.466Z_

I now have a thorough understanding of both the paper and the underlying experimental reality. Here is my review.

---

# Review: IRT-FIT (Reviewer R1 -- Methods and Experiments Focus)

## 1. Methodological Soundness

**Two-sided detection framework.** The extension from one-sided to two-sided person-fit testing is well-motivated by the empirical observation that partial contamination produces negative lz* (aberrant patterns) while full contamination produces positive lz* (over-consistent patterns). This is a genuine insight for the contamination detection setting and not obvious from the existing psychometrics literature. The BH-FDR correction is appropriate for the multiple testing structure (models x benchmarks).

**Power analysis derivation.** The power formula (Eq. 4) is a standard Neyman-Pearson adaptation and is not novel in a statistical sense, but applying it to characterize person-fit detection capacity as a function of benchmark size is useful. The R^2=0.97 fit between theory and simulation is impressive but expected -- the simulations generate data from the same 4PL model assumed by the theory. This is tautological validation, not evidence of real-world applicability.

**Multiscale lzm statistic.** There is a mathematical error. Equation 3 defines lzm = (1/sqrt(K)) * sum(|lz*_k|). Under the null, each |lz*| follows a half-normal distribution (not normal). The paper claims lzm is "approximately standard normal (verified by KS test, p=0.312)," but the sum of absolute values of standard normals is NOT standard normal. Either the formula is wrong, the implementation differs from the formula, or the KS test was run against an incorrect reference distribution. This must be resolved.

**Critical gap: simulation-to-reality calibration failure.** The paper as written does not adequately confront the most important finding from its own preliminary work: when the two-sided framework is applied to real PSN-IRT data (12 models x 5 benchmarks = 60 cells), 57 out of 60 cells (95%) are flagged at alpha=0.05 with BH-FDR correction and benchmark-specific theta estimation with parametric bootstrap. This means lz* is not calibrated for real LLM data -- the 4PL model systematically misfits all LLM response patterns, not just contaminated ones. The paper's controlled experiments (Section 4) circumvent this problem by measuring delta-lz* between clean and contaminated versions of the same model, but the leaderboard audit (Section 6) presumably applies absolute thresholds. How exactly are the 2,847 leaderboard models flagged? The paper never specifies whether it uses absolute lz* thresholds (which would be invalid given universal misfit), relative comparisons (which require a clean baseline), or some other approach.

## 2. Experimental Design

**Controlled contamination (Section 4).** Well-designed. Two base models (Qwen3.5-9B, Gemma-4-31B) at six contamination levels with QLoRA SFT. The selectivity analysis (Table 3) showing +31pp on contaminated items vs +1.4-3.7% generalization is the paper's strongest evidence that person-fit can detect SFT contamination. Cross-model consistency (effect size difference <15%) is reassuring.

**Confounds and concerns:**
- The controlled experiments test only MMLU. Detection power on smaller benchmarks (GSM8K, ARC-C) in the controlled setting is unknown. Given that simulation power for GSM8K is only 57.8% at 15% contamination, controlled AUROC on GSM8K would likely be substantially lower than 0.96.
- QLoRA SFT is the most favorable contamination pathway for detection: it updates few parameters and produces maximally selective memorization. Full-parameter SFT, continued pretraining with benchmark items mixed into general data, or paraphrased item training would produce smoother generalization patterns that are harder to detect.
- The AUROC values lack confidence intervals. With the sample sizes involved, the difference between 0.96 (IRT-FIT) and 0.88 (Min-K%++) may not be statistically significant.

**Post-RL experiment (Section 5.2).** Tested on only one model (Qwen3.5-9B) at one contamination level (15%) with one RL algorithm (GRPO). The claim that "person-fit survives post-RL training" is far broader than what this single experiment supports. The paper does not test PPO, DPO, or KTO. It does not vary RL training duration. The stated AUROC retention of 96% contrasts sharply with the project's own internal notes, which document a very different finding from a separate analysis: lz* dropping from -1.08 to -0.23 post-GRPO with retention of only 12%.

**Leaderboard audit (Section 6).** The 2,847-model scale is unique and compelling. However, the paper is vague about how models were evaluated. It states "we run inference" but does not detail the evaluation harness, prompt format, or whether exact match with PSN-IRT's evaluation protocol was ensured. Different evaluation implementations (e.g., different few-shot templates, answer parsing) can produce substantially different response patterns, potentially confounding lz*. The temporal trend (6% to 18%) is interesting but could reflect model architecture/size shifts rather than increasing contamination.

**Baseline comparison (Section 5.1).** The comparison is structurally unfair in ways the paper does not acknowledge. ConStat detects contamination by measuring performance inconsistency under rephrasing; SFT-contaminated models have permanently altered weights, so re-testing yields identical results by design. This is not IRT-FIT "outperforming" ConStat -- it is testing ConStat outside its threat model. The paper should clearly state that these methods target different contamination pathways.

## 3. Statistical Rigor

**Positive aspects:**
- Effect sizes (Cohen's d) are reported alongside AUROC
- BH-FDR correction is appropriate
- Null calibration (FPR 0.042 at alpha=0.05) is adequate in simulation
- Power analysis provides concrete, actionable thresholds

**Missing or problematic:**
- No confidence intervals on any AUROC values
- No bootstrap CIs on the leaderboard flagging rates
- The lzm null distribution claim is incorrect (see above)
- The power theory R^2=0.97 is circular: theory derived from simulation assumptions, validated on simulations from those assumptions
- ARC-C has 295 items in PSN-IRT (the paper states 1,172 in Table 9, conflating with the full ARC-C dataset size outside PSN-IRT)
- Table 5 in the paper reports inverted-U at 50% contamination, but the actual simulation data shows monotonically increasing |lz*| and power through 50% for MMLU (power drops only from 0.979 at 15% to 0.967 at 25% to 0.861 at 50%, which is NOT the clean inverted-U claimed)

## 4. Reproducibility

**Positive:** The method is fully specified -- the 4PL IRT formula, lz* computation, and detection threshold are standard and reproducible.

**Concerns:**
- PSN-IRT item parameters are required. The paper does not state whether these will be released or how others can obtain them. Without the item bank, the method cannot be replicated.
- The leaderboard audit code and per-model response logs are not discussed for release.
- Evaluation protocol details (prompt format, few-shot examples, answer parsing) are not provided.
- The paper uses 100 replications for some simulations (Table 4) and 1000 for others -- the criteria for this choice are not stated.

## 5. Specific Strengths

- **Genuine conceptual contribution**: The analogy between contaminated LLMs and examinees with item preknowledge, and the "minimal-information operating point" framing, are clean and well-articulated.
- **Two-sided detection**: The identification of two contamination signal regimes (partial negative, full positive) is non-obvious and practically important.
- **Power theory**: The closed-form power formula with practical item-count thresholds (3,200 for 15%, 9,800 for 5%) provides lasting value for benchmark designers.
- **Cross-architecture consistency**: Controlled experiments on two different models (9B, 31B) yield consistent results, reducing model-specificity concerns.
- **Leaderboard-scale audit**: The 2,847-model scan is a unique capability no existing method can match at this scale for historical data.
- **Gemini-1.5 case study**: The 100% MMLU accuracy with theta=0.78 producing lz*=+34.75 is a vivid demonstration of full-contamination detection.

## 6. Specific Weaknesses

- **(Major) lzm null distribution error**: The claimed N(0,1) null for the absolute-value aggregation statistic is mathematically incorrect. This affects Tables 15-16 and the lzm-based results.
- **(Major) Simulation-to-reality gap is underspecified**: The paper does not discuss that real LLM data produces universal 4PL misfit (95% flagging rate on 12 PSN-IRT models), making absolute lz* thresholds unusable for the leaderboard audit. The controlled experiments use delta-lz* (implicitly), but the leaderboard audit apparently uses absolute thresholds. This inconsistency is not addressed.
- **(Major) Thin reference list**: 11 references. Missing: Karabatsos (2003) comparing 36 person-fit statistics (justification for lz*), Sinharay (2017) on preknowledge power analysis (the most directly relevant psychometric precedent), Lalor et al. (2019) on IRT for NLP, Golchin & Surdeanu (2024), Sainz et al. (2023) on contamination, the Wollack & Schoenig (2018) test security literature. Without adequate coverage, the novelty claim cannot be properly assessed.
- **(Moderate) Unfair baseline comparison**: ConStat is tested outside its designed threat model. Min-K%++ operates on raw text tokens, not MCQA binary responses. The "detection frontier" ordering implies a strict hierarchy that does not hold when methods target different contamination types.
- **(Moderate) Narrow post-RL validation**: Single model, single RL algorithm, single contamination level. The AUROC retention (96%) contradicts the project's own earlier finding of 12% retention under different conditions. This discrepancy is not explained.
- **(Moderate) Controlled experiments only test MMLU**: The strongest claims (AUROC 0.96) hold for MMLU (14K items). The method's performance on the smaller benchmarks that practitioners actually need to audit is unknown.
- **(Minor) ARC-C item count inconsistency**: Table 9 lists ARC-C as 1,172 items; the actual PSN-IRT calibration contains 295 items.
- **(Minor) No AUROC confidence intervals**: Statistical significance of the AUROC differences between methods is not established.
- **(Minor) Inverted-U claim overstated**: The actual simulation data for MMLU shows power monotonically above 0.86 from 15% through 50% contamination. The "inverted-U" in the signal is real but the "power valley" framing is misleading when two-sided testing largely eliminates the power dip.

## 7. Questions for Authors

1. **How exactly are the 2,847 leaderboard models flagged?** Given that real LLM data produces 95% flagging rates with absolute lz* thresholds (your own Phase B finding), what detection criterion was used for the leaderboard audit? If absolute thresholds were used, the 12% flagged rate would imply that 88% of models have |lz*| < threshold -- contradicting the 95% flagging rate observed on PSN-IRT models. Please clarify.

2. **lzm implementation**: Does the code compute lzm using absolute values (as in Eq. 3) or signed values? If absolute values, against what null distribution was the KS test (p=0.312) conducted?

3. **Post-RL contradictions**: Your own earlier analysis found only 12% lz* retention after GRPO (lz* from -1.08 to -0.23), while the paper reports 96% AUROC retention. Were these conducted on different experimental configurations? If so, what changed?

4. **PSN-IRT item bank dependency**: The "binary responses only" claim is central to the paper's framing, but the method also requires pre-calibrated 4PL item parameters for every benchmark item. How should practitioners obtain these for new benchmarks? How sensitive are results to item parameter estimation error?

5. **Pretraining contamination**: The paper scopes out pretraining exposure, but this is the dominant contamination pathway in practice (e.g., web-crawled training data containing benchmark items). Can you provide even a rough argument for why the method would or would not work for this case?

## 8. Score

**Score: 3.5 / 6 (Borderline Conference / Findings)**

The paper has a compelling conceptual contribution (minimal-information operating point, two-sided detection, power theory) and strong controlled experiments on MMLU. However, the gap between simulation and reality -- specifically the universal 4PL misfit that makes absolute lz* thresholds unusable on real LLM data -- is the paper's fundamental challenge, and it is not adequately confronted. The leaderboard audit, presented as a headline contribution, rests on unspecified detection criteria that may be invalidated by this calibration gap. The lzm error, thin references, narrow post-RL validation, unfair baselines, and MMLU-only controlled experiments collectively reduce confidence. If the authors can (a) clearly specify and validate the leaderboard flagging criterion, (b) fix the lzm issue, (c) expand the reference list, and (d) add AUROC confidence intervals, the paper could rise to a solid accept.

## 9. Confidence

**4 / 5** (High confidence)

I have expertise in statistical testing methodology, IRT, and LLM evaluation. I read the paper carefully, cross-referenced with the underlying experimental data, and identified specific numerical inconsistencies. My main uncertainty is whether the leaderboard audit uses a different detection strategy than what is described (e.g., a relative ranking approach that would circumvent the calibration gap issue), which could substantially change my assessment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "930a7cae-d21c-46e9-bd23-6aa23a3c4d3f",
  "isSidechain": true,
  "agentId": "a21f57df8dd0071ef",
  "requestId": "req_011CbDaKKxenCceyAuBuc1Ts",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "129b6c2b-e710-46c7-b115-44697529c6ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4a2a993-0191-4885-9fcd-ec0afed74d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1pfahXBCC32WDveobD347",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5504,
      "cache_read_input_tokens": 136535,
      "output_tokens": 3487,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5504
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3487,
          "cache_read_input_tokens": 136535,
          "cache_creation_input_tokens": 5504,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5504,
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
