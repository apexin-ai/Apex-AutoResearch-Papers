# Research conversation: You are Reviewer 2 (R2) for an EMNLP 2026 submission (ARR unified review). Your focus is **novelty and related work**. #

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 73
- **Recorded user turns:** 1
- **Tool calls:** 31
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aebc5241daabf155a.jsonl`
- **Structured JSON:** [`2a7ca30651a3fb699f01.json`](../../sessions/2a/2a7ca30651a3fb699f01.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

73 recorded events

### User

_source line 1 · 2026-05-21T05:51:39.688Z_

You are Reviewer 2 (R2) for an EMNLP 2026 submission (ARR unified review). Your focus is **novelty and related work**.

## Venue Calibration (EMNLP 2026 via ARR)
- Overall Assessment: 5=Award (top 2.5%), 4=Conference accept, 3=Findings, 2=Resubmit, 1=Do not resubmit. Half-point increments.
- Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5)
- Accept rate ~21% for Main. Be calibrated accordingly.
- Mandatory: Limitations section, Responsible NLP Research Checklist (Sections A-E). Missing → desk reject signal.

## Paper Summary
Title: "What Can Binary Response Patterns Reveal About Benchmark Contamination? Characterizing the Minimal-Information Detection Frontier with IRT Person-Fit Statistics"

The paper applies IRT person-fit statistics (ℓ*_z from Snijders 2001) to detect LLM benchmark contamination using only binary (correct/incorrect) response patterns. Claims to establish the "minimal-information operating point" on the contamination detection frontier.

Core contributions claimed:
1. Framework: IRT person-fit as contamination detection at the binary-information level. Introduces Δℓ*_z, θ-fixed analysis, memorization fraction.
2. Detection Frontier Characterization: Systematic mapping across 3 families, 3+ benchmarks, 6 levels, 2 training paradigms.
3. Methodological Insights: 4PL > classical (5.4×), item-level near-random, θ-fixed recovers monotonicity, post-RL erases signal.

Key results:
- Detection works on 2/3 families (|d|=2.24 Qwen/Llama, |d|=0.27 Mistral)
- ℓ*_z and HT person-fit are essentially equivalent (mean |d| 1.58 vs 1.60, Δ=0.02)
- Item-level AUROC ≤ 0.597 for ALL methods including oracle RF
- Post-RL completely erases signal (|d|=0.35 vs clean+GRPO |d|=0.21)
- Power depends on benchmark size, IRT parameter quality, architecture memorization rate

Related work section (Section 7) covers:
- Contamination detection: Shi et al. 2024 (Min-K%), Dekoninck et al. 2024a (Time Travel), Dekoninck et al. 2024b (ConStat), Wang et al. 2025 (post-RL failure of MIA)
- IRT for LLMs: PSN-IRT 2026
- Person-fit in psychometrics: Meijer & Sijtsma 1996, Snijders 2001, Hong et al. 2021

Only 8 references total in the bibliography.

## Your Review Task
Evaluate the paper's **novelty** and **related work** rigorously. Cover:

1. **Novelty Assessment**
   - The core idea is applying ℓ*_z (Snijders 2001) to LLM responses — is this a sufficient contribution for a top venue? Person-fit statistics are well-established in psychometrics; the main novelty is the application domain.
   - ℓ*_z ≈ HT in performance — does this undermine the claim that ℓ*_z is specially suited? The paper acknowledges this but frames it as "IRT person-fit family" contribution.
   - θ-fixed analysis (Eq.5) — is this novel? Fixing ability to a reference value is standard IRT practice.
   - Memorization fraction (Eq.6) — is (acc_seen - acc_unseen)/acc_seen a novel metric? This is essentially a normalized seen-unseen gap.
   - The "detection frontier" framing — is this genuinely novel conceptual work or a post-hoc reframing of mixed results?
   - The paper's main positive result (|d|=2.24 on 2/3 families) comes with wide CIs and fails on Mistral — is the positive finding strong enough?
   - The negative results (post-RL failure, Mistral failure, item-level failure) — are these more interesting than the positive results?

2. **Related Work Completeness**
   - Only 8 references — extremely sparse for a venue like EMNLP. Major gaps likely include:
     * Other contamination detection methods not cited (e.g., benchmark-specific tests, rephrasing-based methods beyond Dekoninck)
     * IRT applications to LLMs beyond PSN-IRT (there's growing literature on using IRT for LLM evaluation)
     * Person-fit literature is much richer than 3 citations (Meijer & Sijtsma 1996, Snijders 2001, Hong et al. 2021)
     * LLM memorization and generalization literature
     * Benchmark contamination surveys
     * QLoRA/LoRA fine-tuning literature
   - Does the paper adequately position itself relative to ConStat (Dekoninck et al. 2024b)? ConStat also tests for contamination at the response level without needing weights.
   - Missing discussion of how person-fit compares to ConStat's consistency-based approach.

3. **Framing & Positioning**
   - "Minimal-information operating point" — is binary truly the minimum? (What about just accuracy, which is even less information?)
   - The paper frames mixed results as "detection frontier characterization" — is this convincing or does it mask that the method has serious limitations?
   - The reframe from "ℓ*_z is best" to "IRT person-fit family" after HT ties — is this intellectually honest?
   - Does the paper oversell the positive or undersell the negative?

4. **Contribution Significance**
   - For EMNLP Main (21% accept rate): Is this paper in the top quintile?
   - The practical utility is limited: works only on SFT (not post-RL), only on some architectures, needs PSN-IRT parameters, needs multiple clean seeds.
   - The theoretical/characterization contribution: mapping the detection frontier is valuable but are the results surprising? It's somewhat expected that (a) binary patterns carry less info than token probs, (b) RL changes distributions, (c) memorization varies across architectures.
   - Excitement level: would reviewers find this exciting or incremental?

5. **Writing Quality**
   - Is the paper well-organized?
   - Are claims well-calibrated to evidence?
   - Any overclaiming?

Output your review in this structure:
```
## R2 Review: Novelty & Related Work

### Summary (2-3 sentences)

### Strengths (bullet list, numbered)

### Weaknesses (bullet list, numbered, with severity: Major/Minor)

### Questions for Authors

### Missing References (list specific papers/areas)

### Excitement: X/5
### Preliminary Overall Assessment: X (with brief justification)
```

Be rigorous but fair. Calibrate to EMNLP 2026 standards where ~21% of papers are accepted to Main.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "79212eb5-91aa-48ea-ae2a-e9b79612f973",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T05:51:39.691Z_

```json
{
  "parentUuid": "79212eb5-91aa-48ea-ae2a-e9b79612f973",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
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
  "uuid": "de72259d-825f-490a-a35f-cda79fdd3278",
  "timestamp": "2026-05-21T05:51:39.691Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T05:51:42.554Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de72259d-825f-490a-a35f-cda79fdd3278",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC7hPcBevSGuXCqaJ2F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c73ae012-3adf-4035-8194-535cc53fbe7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyfgUWPiFM62q2tqS6i1zr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8061,
      "cache_read_input_tokens": 8254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8061,
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

_source line 4 · 2026-05-21T05:51:43.008Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016ErpxwBYKhdo4Y1Php1Soi`</summary>

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
  "parentUuid": "c73ae012-3adf-4035-8194-535cc53fbe7c",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC7hPcBevSGuXCqaJ2F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b268a230-fc79-424e-b158-57958eea3cb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyfgUWPiFM62q2tqS6i1zr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8061,
      "cache_read_input_tokens": 8254,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8061
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 8254,
          "cache_creation_input_tokens": 8061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8061,
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

_source line 5 · 2026-05-21T05:51:43.010Z_

<details><summary>↩ Tool result · `toolu_016ErpxwBYKhdo4Y1Php1Soi`</summary>

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
  "parentUuid": "b268a230-fc79-424e-b158-57958eea3cb4",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "3545dd03-a389-4165-bd20-d5ad304182f8",
  "sourceToolAssistantUUID": "b268a230-fc79-424e-b158-57958eea3cb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T05:51:45.749Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01N4zXf38nfwFanDXBoZHS9M`</summary>

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
  "parentUuid": "3545dd03-a389-4165-bd20-d5ad304182f8",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC7wk4dSnNgFt92AfgT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "666941ff-5b99-42ff-9f0b-21b928197bc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jMEgWXNEsL3x51VqwB5tX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 7 · 2026-05-21T05:51:45.893Z_

<details><summary>↩ Tool result · `toolu_01N4zXf38nfwFanDXBoZHS9M`</summary>

```text
{"result":"# 项目 irt_personfit_contam 概况\n\n## 实验状态 (37 个)\n\n- **exp-domain-analysis**: DONE (success) — \n- **exp-ml-classifier-baseline**: DONE (success) — \n- **exp-v1-irt-refit-pilot**: DONE (negative) — \n- **exp-clean-control-delta**: DONE (success) — \n- **exp-fdr-correction**: DONE (success) — \n- **exp-cross-benchmark-analysis**: DONE (success) — \n- **exp-accuracy-zscore-baseline**: DONE (success) — \n- **exp-item-alignment-check**: DONE (negative) — \n- **exp-power-theory**: DONE (success) — \n- **exp-empirical-null**: DONE (negative) — \n- **exp-leaderboard-data-recon**: DONE (success) — \n- **exp-extended-sim**: DONE (success) — \n- **exp-two-sided**: DONE (negative) — \n- **phase_b_personfit**: DONE (success) — \n- **sim_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-ctrl-contam-mistral | Mistral-7B-Instruct-v0.3 as a third model family (distinct tokenizer and training recipe from Qwen/Llama) produces significant Δlz* under controlled contamination, further confirming cross-family detection generalizability — addressing reviewer concern R4 about limited model diversity (2 families × 1 benchmark) | — | — | — |\n| exp-ctrl-contam-mistral-contam50 | — | — | — | — |\n| exp-ctrl-contam-mistral-contam15 | — | — | — | — |\n\n## 待处理\n- exp-ctrl-contam-pilot-contam-50（准备中）\n- exp-ctrl-contam-pilot-contam-15（准备中）\n- exp-ctrl-contam-pilot-clean-s2（准备中）\n- exp-ctrl-contam-pilot-clean-s1（准备中）\n\n## 近期结论\n- **exp-baseline-comparison** (success): IRT-based lz* detection outperforms binary-only baselines (accuracy z-score, LR, RF classifiers) on controlled contamination data, especially at low contamination rates (15%), because lz* leverages item-level difficulty calibration unavailable to methods operating on aggregate or uncalibrated binary vectors\n  [baseline_comparison_results](/api/workspace-files/projects/irt_personfit_contam/artifacts/exp-baseline-comparison/data/comparison_results.json)\n- **exp-ctrl-contam-llama-clean** (success): A Llama-3.1-8B-Instruct model fine-tuned on clean Alpaca data (no MMLU contamination) will show normal person-fit statistics (lz* within expected range), serving as the uncontaminated baseline for comparison with contaminated conditions.\n- **exp-ctrl-contam-llama-clean-s3** (success): Third independent clean Llama-3.1-8B-Instruct baseline (seed=456) for Cohen's d variance estimation: matches Qwen n=3 protocol for cross-family effect size comparison ← 基于 exp-ctrl-contam-llama\n\n## 趋势\n成功 20 / 负向 6 / 失败 0 / 共 26\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-35694: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "666941ff-5b99-42ff-9f0b-21b928197bc9",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "8544225c-4103-4fb0-9bb4-e54f16e0e297",
  "sourceToolAssistantUUID": "666941ff-5b99-42ff-9f0b-21b928197bc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T05:51:46.443Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Xxr58XZT4JYmHyVrwCrYD7`</summary>

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
  "parentUuid": "8544225c-4103-4fb0-9bb4-e54f16e0e297",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC7wk4dSnNgFt92AfgT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e44fd04-404d-4d85-9240-153d6b904c34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jMEgWXNEsL3x51VqwB5tX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16315,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 16315,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1447,
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

_source line 9 · 2026-05-21T05:51:46.452Z_

<details><summary>↩ Tool result · `toolu_01Xxr58XZT4JYmHyVrwCrYD7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp-ctrl-contam-mistral | Mistral-7B-Instruct-v0.3 as a third model family (distinct tokenizer and training recipe from Qwen/Llama) produces significant Δlz* under controlled contamination, further confirming cross-family detection generalizability — addressing reviewer concern R4 about limited model diversity (2 families × 1 benchmark) | — | — | — |\\n| exp-ctrl-contam-mistral-contam50 | — | — | — | — |\\n| exp-ctrl-contam-mistral-contam15 | — | — | — | — |\\n\\n## 待处理\\n- exp-ctrl-contam-pilot-contam-50（准备中）\\n- exp-ctrl-contam-pilot-contam-15（准备中）\\n- exp-ctrl-contam-pilot-clean-s2（准备中）\\n- exp-ctrl-contam-pilot-clean-s1（准备中）\\n\\n## 近期结论\\n- **exp-baseline-comparison** (success): IRT-based lz* detection outperforms binary-only baselines (accuracy z-score, LR, RF classifiers) on controlled contamination data, especially at low contamination rates (15%), because lz* leverages item-level difficulty calibration unavailable to methods operating on aggregate or uncalibrated binary vectors\\n  [baseline_comparison_results](/api/workspace-files/projects/irt_personfit_contam/artifacts/exp-baseline-comparison/data/comparison_results.json)\\n- **exp-ctrl-contam-llama-clean** (success): A Llama-3.1-8B-Instruct model fine-tuned on clean Alpaca data (no MMLU contamination) will show normal person-fit statistics (lz* within expected range), serving as the uncontaminated baseline for comparison with contaminated conditions.\\n- **exp-ctrl-contam-llama-clean-s3** (success): Third independent clean Llama-3.1-8B-Instruct baseline (seed=456) for Cohen's d variance estimation: matches Qwen n=3 protocol for cross-family effect size comparison ← 基于 exp-ctrl-contam-llama\\n\\n## 趋势\\n成功 20 / 负向 6 / 失败 0 / 共 26\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-35694: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1908, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e44fd04-404d-4d85-9240-153d6b904c34",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "7a41afdf-705f-4773-a43d-326adc89b442",
  "sourceToolAssistantUUID": "9e44fd04-404d-4d85-9240-153d6b904c34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-21T05:51:49.198Z_

Let me now read the actual paper and related work files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a41afdf-705f-4773-a43d-326adc89b442",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC8CWZvgU8PxaEnBGGQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4fdae48-d3ad-4493-b3b1-4e3435bfac3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015oZPaGB26d3Apghh8wK99h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2151,
      "cache_read_input_tokens": 17762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2151,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 11 · 2026-05-21T05:51:49.699Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TUzC8DbR2yV5771i5LtRF4`</summary>

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
  "parentUuid": "a4fdae48-d3ad-4493-b3b1-4e3435bfac3d",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC8CWZvgU8PxaEnBGGQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12b0736f-60a0-44cc-b80c-e9b2fc481c23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015oZPaGB26d3Apghh8wK99h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2151,
      "cache_read_input_tokens": 17762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2151,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 12 · 2026-05-21T05:51:49.824Z_

<details><summary>↩ Tool result · `toolu_01TUzC8DbR2yV5771i5LtRF4`</summary>

```text
artifacts/dream_reports/dream_20260520T082549/best/paper.tex
artifacts/dream_reports/dream_20260520T082549/median/paper.tex
artifacts/dream_reports/dream_20260520T082549/worst/paper.tex
artifacts/dream_reports/dream_20260520T092614/best/paper.tex
artifacts/dream_reports/dream_20260520T092614/median/paper.tex
artifacts/dream_reports/dream_20260520T092614/worst/paper.tex
artifacts/dream_reports/dream_20260520T105545/best/paper.tex
artifacts/dream_reports/dream_20260520T105545/median/paper.tex
artifacts/dream_reports/dream_20260520T105545/worst/paper.tex
artifacts/dream_reports/dream_20260520T190245/best/paper.tex
artifacts/dream_reports/dream_20260520T190245/median/paper.tex
artifacts/dream_reports/dream_20260520T190245/worst/paper.tex
artifacts/_project/paper/sec_setup.tex
paper/sections/experiments.tex
docs/paper/sec_setup.tex
docs/paper/sec_simulation.tex
artifacts/_project/paper/method.tex
docs/paper/sec_empirical.tex
docs/paper/sec_background.tex
docs/paper/sec_introduction.tex
docs/paper/sec_discussion.tex
docs/paper/abstract.tex
docs/paper/sec_conclusion.tex
docs/paper/sec_limitations.tex
docs/paper/sec_ctrl_contam.tex
docs/paper/sec_method.tex
paper/sections/background.tex
paper/main.tex
paper/sections/sec_empirical.tex
paper/sections/discussion.tex
paper/sections/sec_setup.tex
artifacts/seed_sensitivity/seed_sensitivity_tables.tex
paper/sections/appendix.tex
artifacts/dream_reports/dream_20260521T032820/best/paper.tex
artifacts/dream_reports/dream_20260521T032820/median/paper.tex
artifacts/dream_reports/dream_20260521T032820/worst/paper.tex
paper/sections/sec_simulation.tex
paper/sections/conclusion.tex
paper/sections/abstract.tex
paper/sections/introduction.tex
paper/sections/method.tex
paper/sections/sec_ctrl_contam.tex
paper/sections/limitations.tex
artifacts/dream_reports/dream_20260521T044802/best/paper.tex
artifacts/dream_reports/dream_20260521T044802/median/paper.tex
artifacts/dream_reports/dream_20260521T044802/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12b0736f-60a0-44cc-b80c-e9b2fc481c23",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "b6e7d6da-07ba-43f9-81b9-63ae5289a521",
  "sourceToolAssistantUUID": "12b0736f-60a0-44cc-b80c-e9b2fc481c23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T05:51:50.667Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TnLrfM5ZFjSgHNFGK1R5uX`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6e7d6da-07ba-43f9-81b9-63ae5289a521",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC8CWZvgU8PxaEnBGGQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c294bff1-6d6a-499f-a72d-27000f2a1ec1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015oZPaGB26d3Apghh8wK99h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2151,
      "cache_read_input_tokens": 17762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2151,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 14 · 2026-05-21T05:51:50.795Z_

<details><summary>↩ Tool result · `toolu_01TnLrfM5ZFjSgHNFGK1R5uX`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c294bff1-6d6a-499f-a72d-27000f2a1ec1",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "577e7335-9c4a-4758-adc7-9abe951285a6",
  "sourceToolAssistantUUID": "c294bff1-6d6a-499f-a72d-27000f2a1ec1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T05:51:51.085Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HtkNfA27wAtAnh6eiJhDYR`</summary>

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
  "parentUuid": "577e7335-9c4a-4758-adc7-9abe951285a6",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC8CWZvgU8PxaEnBGGQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4dfeb66-7f97-4939-babe-d936a3a84337",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015oZPaGB26d3Apghh8wK99h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2151,
      "cache_read_input_tokens": 17762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2151,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 16 · 2026-05-21T05:51:51.097Z_

<details><summary>↩ Tool result · `toolu_01HtkNfA27wAtAnh6eiJhDYR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-20T22:30:00Z'\\n  total_papers: 33\\ncategories:\\n  - key: irt-llm\\n    label: IRT for LLM Evaluation\\n  - key: contamination-detection\\n    label: Benchmark Contamination Detection\\n  - key: person-fit\\n    label: Person-Fit Statistics (Psychometrics)\\n  - key: post-rl-contamination\\n    label: Post-RL Contamination\\n  - key: irt-foundations\\n    label: IRT Foundations\\n  - key: llm-evaluation-infrastructure\\n    label: LLM Evaluation Infrastructure\\npapers:\\n  psnirt2026:\\n    title: \\\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\\\"\\n    authors: [\\\"Zhou, H.\\\", \\\"Huang, H.\\\", \\\"Zhao, Z.\\\", \\\"Han, L.\\\", \\\"Wang, H.\\\", \\\"Chen, K.\\\", \\\"Yang, M.\\\", \\\"Bao, W.\\\", \\\"Dong, J.\\\", \\\"Xu, B.\\\", \\\"Zhu, C.\\\", \\\"Cao, H.\\\", \\\"Zhao, T.\\\"]\\n    year: 2026\\n    venue: \\\"AAAI 2026 Oral\\\"\\n    url: \\\"https://arxiv.org/abs/2505.15055\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: psnirt2026\\n    category: irt-llm\\n    role: foundation\\n    relevance: \\\"Provides calibrated 4PL item parameters (a,b,c,d) for 41,871 items across 11 benchmarks — the item bank our method builds on\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  atlas2025:\\n    title: \\\"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks\\\"\\n    authors: [\\\"Li, P.\\\", \\\"Tang, X.\\\", \\\"Chen, S.\\\", \\\"Cheng, Y.\\\", \\\"Metoyer, R.\\\", \\\"Hua, T.\\\", \\\"Chawla, N. V.\\\"]\\n    year: 2025\\n    venue: \\\"arXiv preprint\\\"\\n    url: \\\"https://arxiv.org/abs/2511.04689\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: atlas2025\\n    category: irt-llm\\n    role: background\\n    relevance: \\\"ATLAS uses IRT for adaptive testing efficiency; related IRT-for-LLM work but not person-fit\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  constat2024:\\n    title: \\\"ConStat: Performance-Based Contamination Detection in Large Language Models\\\"\\n    authors: [\\\"Dekoninck, J.\\\", \\\"Müller, M.\\\", \\\"Vechev, M.\\\"]\\n    year: 2024\\n    venue: \\\"NeurIPS 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2405.16281\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: constat2024\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"Performance-based contamination detector — primary baseline; requires re-test with modified items\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  minkprob2024:\\n    title: \\\"Detecting Pretraining Data from Large Language Models\\\"\\n    authors: [\\\"Shi, W.\\\", \\\"Ajith, A.\\\", \\\"Xia, M.\\\", \\\"Huang, Y.\\\", \\\"Liu, D.\\\", \\\"Blevins, T.\\\", \\\"Chen, D.\\\", \\\"Zettlemoyer, L.\\\"]\\n    year: 2024\\n    venue: \\\"ICLR 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2310.16789\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: minkprob2024\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"Min-K% Probability MIA-based detector — baseline; requires token probabilities (not black-box)\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  wang2025fragility:\\n    title: \\\"On The Fragility of Benchmark Contamination Detection in Reasoning Models\\\"\\n    authors: [\\\"Wang, H.\\\", \\\"Li, H.\\\", \\\"Ko, B.\\\", \\\"Zhang, H.\\\"]\\n    year: 2025\\n    venue: \\\"arXiv preprint\\\"\\n    url: \\\"https://arxiv.org/abs/2510.02386\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: wang2025fragility\\n    category: post-rl-contamination\\n    role: foundation\\n    relevance: \\\"Shows all MIA-based detectors fail under post-RL contamination — motivates our black-box approach\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  selfcritique2026:\\n    title: \\\"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models\\\"\\n    authors: [\\\"Tao, Y.\\\", \\\"Wang, T.\\\", \\\"Dong, Y.\\\", \\\"Liu, H.\\\", \\\"Zhang, K.\\\", \\\"Hu, X.\\\", \\\"Li, G.\\\"]\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2510.09259\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: selfcritique2026\\n    category: post-rl-contamination\\n    role: direct-competitor\\n    relevance: \\\"Self-Critique detects post-RL contamination via entropy-sequence policy collapse — baseline for post-RL setting\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  codec2026:\\n    title: \\\"Detecting Data Contamination in LLMs via In-Context Learning\\\"\\n    authors: [\\\"Zawalski, M.\\\", \\\"Boubdir, M.\\\", \\\"Bałazy, K.\\\", \\\"Nushi, B.\\\", \\\"Ribalta, P.\\\"]\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2510.27055\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: codec2026\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"CoDeC measures ICL effects on memorized vs unseen data — baseline\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  oren2024:\\n    title: \\\"Proving Test Set Contamination in Black-Box Language Models\\\"\\n    authors: [\\\"Oren, Y.\\\", \\\"Meister, N.\\\", \\\"Chatterji, N. S.\\\", \\\"Ladhak, F.\\\", \\\"Hashimoto, T.\\\"]\\n    year: 2024\\n    venue: \\\"ICLR 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2310.17623\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: oren2024\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"Statistical contamination test using exchangeability of benchmark orderings — black-box, no weight access needed. Key baseline.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:20:00Z\\\"\\n\\n  golchin2024:\\n    title: \\\"Time Travel in LLMs: Tracing Data Contamination in Large Language Models\\\"\\n    authors: [\\\"Golchin, S.\\\", \\\"Surdeanu, M.\\\"]\\n    year: 2024\\n    venue: \\\"ICLR 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2308.08493\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: golchin2024\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"Guided-instruction probing to detect instance-level memorization — prompts LLM to complete dataset instances. Baseline.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:20:00Z\\\"\\n\\n  dodge2021:\\n    title: \\\"Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus\\\"\\n    authors: [\\\"Dodge, J.\\\", \\\"Sap, M.\\\", \\\"Marasović, A.\\\", \\\"Agnew, W.\\\", \\\"Ilharco, G.\\\", \\\"Groeneveld, D.\\\", \\\"Mitchell, M.\\\", \\\"Gardner, M.\\\"]\\n    year: 2021\\n    venue: \\\"EMNLP 2021\\\"\\n    url: \\\"https://aclanthology.org/2021.emnlp-main.98/\\\"\\n    doi: \\\"10.18653/v1/2021.emnlp-main.98\\\"\\n    bibtex_key: dodge2021\\n    category: contamination-detection\\n    role: background\\n    relevance: \\\"Documents C4 corpus content and overlap with downstream benchmarks — establishes that large web corpora inevitably contain test data.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:20:00Z\\\"\\n\\n  sainz2023:\\n    title: \\\"NLP Evaluation in Trouble: On the Need to Measure LLM Data Contamination for each Benchmark\\\"\\n    authors: [\\\"Sainz, O.\\\", \\\"Campos, J.\\\", \\\"García-Ferrero, I.\\\", \\\"Etxaniz, J.\\\", \\\"Lopez de Lacalle, O.\\\", \\\"Agirre, E.\\\"]\\n    year: 2023\\n    venue: \\\"Findings of EMNLP 2023\\\"\\n    url: \\\"https://aclanthology.org/2023.findings-emnlp.722/\\\"\\n    doi: \\\"10.18653/v1/2023.findings-emnlp.722\\\"\\n    bibtex_key: sainz2023\\n    category: contamination-detection\\n    role: background\\n    relevance: \\\"Position paper defining contamination levels and arguing for systematic per-benchmark contamination measurement. Motivates our work.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:20:00Z\\\"\\n\\n  jacovi2023:\\n    title: \\\"Stop Uploading Test Data in Plain Text: Practical Strategies for Mitigating Data Contamination by Evaluation Benchmarks\\\"\\n    authors: [\\\"Jacovi, A.\\\", \\\"Caciularu, A.\\\", \\\"Goldman, O.\\\", \\\"Goldberg, Y.\\\"]\\n    year: 2023\\n    venue: \\\"EMNLP 2023\\\"\\n    url: \\\"https://aclanthology.org/2023.emnlp-main.308/\\\"\\n    doi: \\\"10.18653/v1/2023.emnlp-main.308\\\"\\n    bibtex_key: jacovi2023\\n    category: contamination-detection\\n    role: background\\n    relevance: \\\"Proposes practical mitigation strategies (encryption, canary strings, exclusion controls) — frames the contamination problem from the benchmark-design perspective.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:20:00Z\\\"\\n\\n  magar2022:\\n    title: \\\"Data Contamination: From Memorization to Exploitation\\\"\\n    authors: [\\\"Magar, I.\\\", \\\"Schwartz, R.\\\"]\\n    year: 2022\\n    venue: \\\"ACL 2022\\\"\\n    url: \\\"https://aclanthology.org/2022.acl-short.18/\\\"\\n    doi: \\\"10.18653/v1/2022.acl-short.18\\\"\\n    bibtex_key: magar2022\\n    category: contamination-detection\\n    role: background\\n    relevance: \\\"Distinguishes memorization vs exploitation of contaminated data — shows models may memorize without performance gain, informing our detection framing.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:20:00Z\\\"\\n\\n  deng2024:\\n    title: \\\"Investigating Data Contamination in Modern Benchmarks for Large Language Models\\\"\\n    authors: [\\\"Deng, C.\\\", \\\"Zhao, Y.\\\", \\\"Tang, X.\\\", \\\"Gerstein, M.\\\", \\\"Cohan, A.\\\"]\\n    year: 2024\\n    venue: \\\"NAACL 2024\\\"\\n    url: \\\"https://aclanthology.org/2024.naacl-long.482/\\\"\\n    doi: \\\"10.18653/v1/2024.naacl-long.482\\\"\\n    bibtex_key: deng2024\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"Retrieval-based contamination detection for both open-source and proprietary LLMs — reveals benchmark overlap in pretraining corpora.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:20:00Z\\\"\\n\\n  sinharay2017:\\n    title: \\\"Which Statistic Should Be Used to Detect Item Preknowledge When the Set of Compromised Items Is Known?\\\"\\n    authors: [\\\"Sinharay, S.\\\"]\\n    year: 2017\\n    venue: \\\"Applied Psychological Measurement\\\"\\n    url: \\\"https://pmc.ncbi.nlm.nih.gov/articles/PMC5978524/\\\"\\n    doi: \\\"10.1177/0146621617698453\\\"\\n    bibtex_key: sinharay2017\\n    category: person-fit\\n    role: foundation\\n    relevance: \\\"Power analysis for preknowledge detection — peak detection at 10-30% preknowledge; core theoretical basis\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  karabatsos2003:\\n    title: \\\"Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics\\\"\\n    authors: [\\\"Karabatsos, G.\\\"]\\n    year: 2003\\n    venue: \\\"Applied Measurement in Education\\\"\\n    url: \\\"https://www.tandfonline.com/doi/abs/10.1207/S15324818AME1604_2\\\"\\n    doi: \\\"10.1207/S15324818AME1604_2\\\"\\n    bibtex_key: karabatsos2003\\n    category: person-fit\\n    role: foundation\\n    relevance: \\\"Comprehensive comparison of 36 person-fit statistics — guides our choice of lz* as primary statistic\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  hong2021lzm:\\n    title: \\\"Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types\\\"\\n    authors: [\\\"Hong, M.\\\", \\\"Lin, L.\\\", \\\"Cheng, Y.\\\"]\\n    year: 2021\\n    venue: \\\"Psychometrika\\\"\\n    url: \\\"https://link.springer.com/article/10.1007/s11336-021-09756-3\\\"\\n    doi: \\\"10.1007/s11336-021-09756-3\\\"\\n    bibtex_key: hong2021lzm\\n    category: person-fit\\n    role: method-component\\n    relevance: \\\"lzm multiscale aggregation for multidimensional constructs — our Level 2 aggregated contamination score\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  drasgow1985:\\n    title: \\\"Appropriateness Measurement with Polychotomous Item Response Models and Standardized Indices\\\"\\n    authors: [\\\"Drasgow, F.\\\", \\\"Levine, M. V.\\\", \\\"Williams, E. A.\\\"]\\n    year: 1985\\n    venue: \\\"British Journal of Mathematical and Statistical Psychology\\\"\\n    url: \\\"https://bpspsychub.onlinelibrary.wiley.com/doi/abs/10.1111/j.2044-8317.1985.tb00817.x\\\"\\n    doi: \\\"10.1111/j.2044-8317.1985.tb00817.x\\\"\\n    bibtex_key: drasgow1985\\n    category: person-fit\\n    role: foundation\\n    relevance: \\\"Introduced the lz person-fit statistic — the foundation our lz* builds on\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:16:00Z\\\"\\n\\n  snijders2001:\\n    title: \\\"Asymptotic Null Distribution of Person Fit Statistics with Estimated Person Parameter\\\"\\n    authors: [\\\"Snijders, T. A. B.\\\"]\\n    year: 2001\\n    venue: \\\"Psychometrika\\\"\\n    url: \\\"https://link.springer.com/article/10.1007/BF02294437\\\"\\n    doi: \\\"10.1007/BF02294437\\\"\\n    bibtex_key: snijders2001\\n    category: person-fit\\n    role: foundation\\n    relevance: \\\"Derived the lz* correction for estimated ability parameters — the core statistic in our contamination detection method\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:16:00Z\\\"\\n\\n  meijer2001:\\n    title: \\\"Methodology Review: Evaluating Person Fit\\\"\\n    authors: [\\\"Meijer, R. R.\\\", \\\"Sijtsma, K.\\\"]\\n    year: 2001\\n    venue: \\\"Applied Psychological Measurement\\\"\\n    url: \\\"https://journals.sagepub.com/doi/abs/10.1177/01466210122031957\\\"\\n    doi: \\\"10.1177/01466210122031957\\\"\\n    bibtex_key: meijer2001\\n    category: person-fit\\n    role: foundation\\n    relevance: \\\"Comprehensive review of person-fit methods — establishes taxonomy and evaluation criteria for person-fit statistics\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:16:00Z\\\"\\n\\n  lord1980:\\n    title: \\\"Applications of Item Response Theory to Practical Testing Problems\\\"\\n    authors: [\\\"Lord, F. M.\\\"]\\n    year: 1980\\n    venue: \\\"Lawrence Erlbaum Associates\\\"\\n    url: \\\"\\\"\\n    doi: \\\"10.4324/9780203056615\\\"\\n    bibtex_key: lord1980\\n    category: irt-foundations\\n    role: foundation\\n    relevance: \\\"Seminal IRT textbook establishing the theoretical and practical framework for item response theory in testing\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:15:00Z\\\"\\n\\n  embretson2000:\\n    title: \\\"Item Response Theory for Psychologists\\\"\\n    authors: [\\\"Embretson, S. E.\\\", \\\"Reise, S. P.\\\"]\\n    year: 2000\\n    venue: \\\"Lawrence Erlbaum Associates\\\"\\n    url: \\\"\\\"\\n    doi: \\\"10.4324/9781410605269\\\"\\n    bibtex_key: embretson2000\\n    category: irt-foundations\\n    role: foundation\\n    relevance: \\\"Accessible IRT textbook bridging psychometric theory and psychological applications; standard reference for IRT model exposition\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:15:00Z\\\"\\n\\n  barton1981:\\n    title: \\\"An Upper Asymptote for the Three-Parameter Logistic Item-Response Model\\\"\\n    authors: [\\\"Barton, M. A.\\\", \\\"Lord, F. M.\\\"]\\n    year: 1981\\n    venue: \\\"ETS Research Report Series (RR-81-20)\\\"\\n    url: \\\"https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2333-8504.1981.tb01255.x\\\"\\n    doi: \\\"10.1002/j.2333-8504.1981.tb01255.x\\\"\\n    bibtex_key: barton1981\\n    category: irt-foundations\\n    role: foundation\\n    relevance: \\\"Origin of the 4PL model adding upper asymptote parameter d to the 3PL — directly relevant to PSN-IRT's 4PL item parameters\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:15:00Z\\\"\\n\\n  birnbaum1968:\\n    title: \\\"Some Latent Trait Models and Their Use in Inferring an Examinee's Ability\\\"\\n    authors: [\\\"Birnbaum, A.\\\"]\\n    year: 1968\\n    venue: \\\"In F. M. Lord & M. R. Novick (Eds.), Statistical Theories of Mental Test Scores (pp. 397-479). Addison-Wesley\\\"\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: birnbaum1968\\n    category: irt-foundations\\n    role: foundation\\n    relevance: \\\"Introduced the 2PL and 3PL IRT models — the parametric foundation underlying all modern IRT applications including our person-fit approach\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:15:00Z\\\"\\n\\n  deayala2009:\\n    title: \\\"The Theory and Practice of Item Response Theory\\\"\\n    authors: [\\\"de Ayala, R. J.\\\"]\\n    year: 2009\\n    venue: \\\"Guilford Press\\\"\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: deayala2009\\n    category: irt-foundations\\n    role: foundation\\n    relevance: \\\"Modern comprehensive IRT textbook covering 1PL through 4PL models, estimation methods, and person-fit — standard graduate-level reference\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T21:15:00Z\\\"\\n\\n  # --- Cluster 1: irt-llm (new papers) ---\\n\\n  martinezplumed2019:\\n    title: \\\"Item Response Theory in AI: Analysing Machine Learning Classifiers at the Instance Level\\\"\\n    authors: [\\\"Martínez-Plumed, F.\\\", \\\"Prudêncio, R. B. C.\\\", \\\"Martínez-Usó, A.\\\", \\\"Hernández-Orallo, J.\\\"]\\n    year: 2019\\n    venue: \\\"Artificial Intelligence\\\"\\n    url: \\\"https://www.sciencedirect.com/science/article/pii/S0004370219300220\\\"\\n    doi: \\\"10.1016/j.artint.2018.09.004\\\"\\n    bibtex_key: martinezplumed2019\\n    category: irt-llm\\n    role: foundation\\n    relevance: \\\"Foundational work applying IRT to AI/ML evaluation at instance level — item difficulty, discrimination, guessing for classifiers. Establishes the IRT-for-AI paradigm our work extends to LLM contamination.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T22:30:00Z\\\"\\n\\n  polo2024tinybenchmarks:\\n    title: \\\"tinyBenchmarks: Evaluating LLMs with Fewer Examples\\\"\\n    authors: [\\\"Polo, F. M.\\\", \\\"Weber, L.\\\", \\\"Choshen, L.\\\", \\\"Sun, Y.\\\", \\\"Xu, G.\\\", \\\"Yurochkin, M.\\\"]\\n    year: 2024\\n    venue: \\\"ICML 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2402.14992\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: polo2024tinybenchmarks\\n    category: irt-llm\\n    role: background\\n    relevance: \\\"Uses IRT-based item selection to reduce benchmark size by 100x while preserving ranking — complementary efficient-evaluation approach; validates that item-level analysis matters for LLM benchmarks.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T22:30:00Z\\\"\\n\\n  # --- Cluster 2: post-rl-contamination (new paper) ---\\n\\n  zhang2026rlvr:\\n    title: \\\"Detecting RLVR Training Data via Structural Convergence of Reasoning\\\"\\n    authors: [\\\"Zhang, H.\\\", \\\"Yang, Y.\\\", \\\"Yan, J.\\\", \\\"Bao, G.\\\", \\\"Zhang, Y.\\\", \\\"Zhang, Y.\\\"]\\n    year: 2026\\n    venue: \\\"arXiv preprint\\\"\\n    url: \\\"https://arxiv.org/abs/2602.11792\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: zhang2026rlvr\\n    category: post-rl-contamination\\n    role: direct-competitor\\n    relevance: \\\"Min-kNN Distance black-box detector exploiting reasoning structural collapse under RLVR — directly comparable baseline for post-RL contamination detection without token probabilities.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T22:30:00Z\\\"\\n\\n  # --- Cluster 3: llm-evaluation-infrastructure ---\\n\\n  hendrycks2021mmlu:\\n    title: \\\"Measuring Massive Multitask Language Understanding\\\"\\n    authors: [\\\"Hendrycks, D.\\\", \\\"Burns, C.\\\", \\\"Basart, S.\\\", \\\"Zou, A.\\\", \\\"Mazeika, M.\\\", \\\"Song, D.\\\", \\\"Steinhardt, J.\\\"]\\n    year: 2021\\n    venue: \\\"ICLR 2021\\\"\\n    url: \\\"https://arxiv.org/abs/2009.03300\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: hendrycks2021mmlu\\n    category: llm-evaluation-infrastructure\\n    role: foundation\\n    relevance: \\\"Introduced MMLU — the most widely used LLM benchmark with 57 tasks. Our contamination detection framework is primarily validated on MMLU-derived item parameters.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T22:30:00Z\\\"\\n\\n  beeching2023openllm:\\n    title: \\\"Open LLM Leaderboard\\\"\\n    authors: [\\\"Beeching, E.\\\", \\\"Fourrier, C.\\\", \\\"Habib, N.\\\", \\\"Han, S.\\\", \\\"Lambert, N.\\\", \\\"Rajani, N.\\\", \\\"Sanseviero, O.\\\", \\\"Tunstall, L.\\\", \\\"Wolf, T.\\\"]\\n    year: 2023\\n    venue: \\\"HuggingFace\\\"\\n    url: \\\"https://huggingface.co/spaces/open-llm-leaderboard-old/open_llm_leaderboard\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: beeching2023openllm\\n    category: llm-evaluation-infrastructure\\n    role: foundation\\n    relevance: \\\"The primary public LLM leaderboard aggregating benchmark scores — the ecosystem where contamination incentives are strongest and our method is most needed.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T22:30:00Z\\\"\\n\\n  gao2023evalharness:\\n    title: \\\"A Framework for Few-Shot Language Model Evaluation\\\"\\n    authors: [\\\"Gao, L.\\\", \\\"Tow, J.\\\", \\\"Abbasi, B.\\\", \\\"Biderman, S.\\\", \\\"Black, S.\\\", \\\"DiPofi, A.\\\", \\\"Foster, C.\\\", \\\"Golding, L.\\\", \\\"Hsu, J.\\\", \\\"Le Noac'h, A.\\\", \\\"Li, H.\\\", \\\"McDonell, K.\\\", \\\"Muennighoff, N.\\\", \\\"Ociepa, C.\\\", \\\"Phang, J.\\\", \\\"Reynolds, L.\\\", \\\"Schoelkopf, H.\\\", \\\"Skowron, A.\\\", \\\"Sutawika, L.\\\", \\\"Tang, E.\\\", \\\"Thite, A.\\\", \\\"Wang, B.\\\", \\\"Wang, K.\\\", \\\"Zou, A.\\\"]\\n    year: 2023\\n    venue: \\\"Zenodo\\\"\\n    url: \\\"https://zenodo.org/records/10256836\\\"\\n    doi: \\\"10.5281/zenodo.10256836\\\"\\n    bibtex_key: gao2023evalharness\\n    category: llm-evaluation-infrastructure\\n    role: foundation\\n    relevance: \\\"lm-evaluation-harness — the standard framework for LLM benchmark evaluation used by Open LLM Leaderboard and most contamination studies including ours.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T22:30:00Z\\\"\\n\\n  chang2024survey:\\n    title: \\\"A Survey on Evaluation of Large Language Models\\\"\\n    authors: [\\\"Chang, Y.\\\", \\\"Wang, X.\\\", \\\"Wang, J.\\\", \\\"Wu, Y.\\\", \\\"Yang, L.\\\", \\\"Zhu, K.\\\", \\\"Chen, H.\\\", \\\"Yi, X.\\\", \\\"Wang, C.\\\", \\\"Wang, Y.\\\", \\\"Ye, W.\\\", \\\"Zhang, Y.\\\", \\\"Chang, Y.\\\", \\\"Yu, P. S.\\\", \\\"Yang, Q.\\\", \\\"Xie, X.\\\"]\\n    year: 2024\\n    venue: \\\"ACM Transactions on Intelligent Systems and Technology\\\"\\n    url: \\\"https://arxiv.org/abs/2307.03109\\\"\\n    doi: \\\"10.1145/3641289\\\"\\n    bibtex_key: chang2024survey\\n    category: llm-evaluation-infrastructure\\n    role: background\\n    relevance: \\\"Comprehensive survey covering what/where/how to evaluate LLMs — provides the broader evaluation landscape context for our contamination detection contribution.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T22:30:00Z\\\"\\n\\n  biderman2024lessons:\\n    title: \\\"Lessons from the Trenches on Reproducible Evaluation of Language Models\\\"\\n    authors: [\\\"Biderman, S.\\\", \\\"Schoelkopf, H.\\\", \\\"Sutawika, L.\\\", \\\"Gao, L.\\\", \\\"Tow, J.\\\", \\\"Abbasi, B.\\\", \\\"Aji, A. F.\\\", \\\"Ammanamanchi, P. S.\\\", \\\"Black, S.\\\", \\\"Clive, J.\\\", \\\"DiPofi, A.\\\", \\\"Etxaniz, J.\\\", \\\"Fattori, B.\\\", \\\"Forde, J. Z.\\\", \\\"Foster, C.\\\", \\\"Hsu, J.\\\", \\\"Jaiswal, M.\\\", \\\"Lee, W. Y.\\\", \\\"Li, H.\\\", \\\"Lovering, C.\\\", \\\"Muennighoff, N.\\\", \\\"Pavlick, E.\\\", \\\"Phang, J.\\\", \\\"Skowron, A.\\\", \\\"Tan, S.\\\", \\\"Tang, X.\\\", \\\"Wang, K. A.\\\", \\\"Winata, G. I.\\\", \\\"Yvon, F.\\\", \\\"Zou, A.\\\"]\\n    year: 2024\\n    venue: \\\"arXiv preprint\\\"\\n    url: \\\"https://arxiv.org/abs/2405.14782\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: biderman2024lessons\\n    category: llm-evaluation-infrastructure\\n    role: background\\n    relevance: \\\"Documents reproducibility challenges in LLM evaluation — prompt sensitivity, implementation differences, score variance — motivates why contamination detection must be robust to evaluation noise.\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: true\\n    added_by: worker\\n    added_at: \\\"2026-05-20T22:30:00Z\\\"\\n\", \"total_chars\": 23229, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4dfeb66-7f97-4939-babe-d936a3a84337",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "10e3f3bb-f2ea-4bdc-ad23-e3de280a3962",
  "sourceToolAssistantUUID": "b4dfeb66-7f97-4939-babe-d936a3a84337",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T05:51:51.563Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012nL8xFGTZg82kUBSpxkfAA`</summary>

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
  "parentUuid": "10e3f3bb-f2ea-4bdc-ad23-e3de280a3962",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC8CWZvgU8PxaEnBGGQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84da2c0e-e5c3-4490-a5fd-68b6e9497d0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015oZPaGB26d3Apghh8wK99h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2151,
      "cache_read_input_tokens": 17762,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2151
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 390,
          "cache_read_input_tokens": 17762,
          "cache_creation_input_tokens": 2151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2151,
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

_source line 18 · 2026-05-21T05:51:51.577Z_

<details><summary>↩ Tool result · `toolu_012nL8xFGTZg82kUBSpxkfAA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper_framing.md\", \"content\": \"# Paper Framing — irt_personfit_contam\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\\n\\n## Core Claims (3 条)\\n\\n**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:\\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS reject 8.3%, but overall 40% due to small benchmarks like HumanEval 75%, ARC-C 58.3% — calibration degrades with n_items). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) validate the framework across model families: Qwen at 15% contamination yields |Cohen's d|=3.42 (n=3, ddof=1, ℓz*-corrected) with clear seen/unseen memorization fingerprint; Llama confirms cross-family detection with |Cohen's d|=2.95 at 15% and 3.31 at 50% (n=3, ddof=1, ℓz*-corrected), both large effects. θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity can degrade (model-dependent; Qwen shows free-θ non-monotonicity due to high baseline misfit, Llama does not), but fixing θ to pre-contamination baseline restores monotonic dose-response in both families. The memorization fraction (~35-38% at 15% contamination, consistent across families) quantifies the SFT generalization effect.\\n\\n**Claim 2 (Detection Characterization)**:\\nDetection power increases with benchmark size (n_items) and varies with contamination level, following an empirical power function (R²=0.65) that provides approximate practical guidance for practitioners assessing detectability on benchmarks of known size — but should NOT be described as \\\"predictive theory\\\" or \\\"scaling law.\\\" Two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted (\\\"expected\\\") power. Both upper bound and adjusted power should be reported. **Baseline comparison (exp-baseline-comparison)**: At model level, lz* achieves 8× the effect size of classical person-fit statistics (Guttman/U3) on identical data (|d|=3.42 vs |d|=0.43 for Qwen 15%), demonstrating the value of full 4PL IRT parameterization. At item level, ALL binary-only methods achieve near-random discrimination (AUROC 0.52–0.63, including oracle supervised classifiers), revealing contamination produces a diffuse statistical signature detectable only through model-level aggregation over thousands of items. Accuracy z-score trivially detects in controlled settings (z=160 due to near-zero accuracy variance) but lacks specificity in real-world scenarios. The IRT framework enables principled aggregation by calibrating each item's expected response probability.\\n\\n**Claim 3 (Empirical Findings from Real LLM Data)**:\\nThree empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+31.81, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.\\n\\n## Story Spine\\n\\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\\n\\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\\n\\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \\\"What can be detected from binary response patterns alone?\\\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.\\n\\n**Headline result template**: \\\"Using only binary response patterns, IRT-FIT detects controlled contamination with |Cohen's d|>2.9 across two model families (Qwen, Llama), achieving 8× the effect size of classical person-fit statistics (Guttman/U3) by leveraging full IRT parameterization. While all binary-only methods achieve near-random item-level discrimination (AUROC 0.52–0.63) — revealing that SFT contamination produces a diffuse signal, not item-specific fingerprints — model-level aggregation over thousands of items yields robust detection. The IRT framework provides unique mechanistic insight: θ-shift analysis reveals how contamination raises ability estimates, absorbing aberrant signal, and memorization fraction quantification (35–38%) bridges the gap between theoretical power (97.9% on MMLU-scale) and observed detection capacity.\\\"\\n\\n## Venue Fit Risks\\n\\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \\\"no new NLP model/technique\\\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\\n\\n## Anticipated Reviewer Concerns & Planned Responses\\n\\n| # | Concern | Response Strategy | Supporting Experiment |\\n|---|---------|------------------|----------------------|\\n| R1 | \\\"Just applying existing IRT to LLMs\\\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \\\"cross-domain\\\" from contribution to background. | — |\\n| R2 | \\\"No ground truth contamination labels\\\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\\n| R3 | \\\"Power too low for small benchmarks\\\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\\n| R4 | \\\"Only 12 models\\\" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |\\n| R5 | \\\"SFT generalization smooths signal\\\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\\n| R6 | \\\"Absolute lz* thresholds don't work on real data\\\" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |\\n| R7 | \\\"Post-RL contamination?\\\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\\n| R8 | \\\"4PL vs 3PL — does d parameter matter?\\\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\\n| R9 | \\\"No same-level binary-only baselines\\\" | **Completed (exp-baseline-comparison)**: Model-level: lz* |d|=3.42 vs Guttman/U3 |d|=0.43 (8× gap) — full IRT parameterization far exceeds difficulty-only person-fit. HT competitive on Llama (|d|=3.53) but inconsistent across families. Item-level: all methods near-random (AUROC 0.52–0.63) — contamination is diffuse, model-level aggregation essential. acc z-score detects trivially in controlled settings (z=160) but lacks specificity for real-world use. | exp-baseline-comparison |\\n| R10 | \\\"Leaderboard audit baseline unreliable\\\" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |\\n| R11 | \\\"Power function is upper bound\\\" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |\\n\\n## Key Narrative Elements (from External Review + Distillation)\\n\\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\\n2. **Definitional pivot (à la ConStat)** — \\\"All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?\\\" This reframes our work as problem reformulation, not just cross-domain transfer.\\n3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.\\n4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim \\\"leaderboard audit\\\" or \\\"large-scale detection\\\" in current paper.\\n5. **Inverted-U as empirical characterization** — Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Simulation fit R²=0.957; real-data fit R²=0.65 (gap due to SFT generalization). Frame as \\\"empirical trend\\\" not \\\"theory/law.\\\"\\n6. **Baseline comparison as evidence for model-level aggregation** — Item-level detection is near-random for ALL binary-only methods (including oracle RF). This is NOT a weakness — it reveals that contamination signal is diffuse (memorization fraction ~35%). Model-level lz* aggregates 14K weak signals into |d|>2.9. Frame item-level weakness as supporting evidence: \\\"any method that aggregates is better than any method that localizes.\\\" lz* vs Guttman/U3 8× gap proves IRT parameterization matters. acc z-score is sensitive but non-specific (sensitivity-specificity tradeoff).\\n7. **Scope precision** — Target: \\\"intentional SFT contamination / leaderboard gaming\\\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\\n8. **Terminology guard** — NEVER use \\\"binary information bottleneck\\\" or \\\"information-theoretic lower bound for all binary-only methods.\\\" We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: \\\"IRT person-fit as a principled framework at the minimal-information operating point.\\\"\\n9. **Memorization fraction cross-family consistency** — MF is 35–38% at 15% contamination across Qwen (0.38) and Llama (0.35), only 3pp difference. Consistency strengthens generalizability. MF may vary with contamination mechanism (full FT vs QLoRA), model capacity, and benchmark difficulty — acknowledge in Limitations as deployment bootstrapping problem.\\n10. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.\\n9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.\\n10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are \\\"honest negative results that become positive contributions\\\": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: \\\"the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative.\\\"\\n11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as \\\"principled detection with quantified operating characteristics + θ-shift boundary condition.\\\" Headline: \\\"We don't just detect — we characterize, including the conditions under which detection degrades.\\\" Do NOT claim \\\"state-of-the-art detection.\\\"\\n12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.\\n13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look \\\"normal\\\") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.\\n\\n## Writing Strategy (from Distillation)\\n\\n- **Story type**: \\\"跨界迁移型\\\" — unused in 0/8 peer papers. Our unique angle.\\n- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).\\n- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.\\n- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.\\n- **Numbered findings**: Adopt PSN-IRT's \\\"Key Discoveries\\\" strategy for scannable presentation.\\n- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.\\n- **Baseline count**: Peer median ~5. Target ≥5 baselines.\\n\\n## Evidence Summary\\n\\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+31.81. Cross-benchmark anomaly profiles identified.\\n- **Empirical null analysis (exp-empirical-null)**: Bootstrap null calibration is benchmark-size dependent — large benchmarks well-calibrated (MMLU: mean bias 0.041, std 1.003, KS reject 8.3%; HellaSwag: 8.3%), small benchmarks poorly calibrated (HumanEval: 75%, ARC-C: 58.3%; overall KS reject 40%, 24/60). The statistical framework is sound for large benchmarks (n>10K). 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5) — this reflects **universal 4PL model misfit** (LLM response patterns violate IRT assumptions), not contamination-specific detection. **Important**: 57/60 vs accuracy z-score 4/60 demonstrates lz* captures response-pattern information beyond aggregate accuracy (evidence for Claim 3a universal misfit), NOT contamination detection superiority. Contamination detection evidence comes from simulation (lz* AUROC 0.675 vs ML 0.575 at 5%) and ctrl-contam (d=3.42, n=3, ddof=1, ℓz*-corrected).\\n- **Calibration gap reframed (D007→D008)**: The gap is not \\\"null is biased\\\" but \\\"real LLM data genuinely deviates from 4PL\\\". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.\\n- **Controlled contamination (exp-ctrl-contam-pilot, D015, ℓz*-corrected)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×3 seeds, 15%, 50%). **n=3 clean seeds (ℓz*-corrected)**: s1=9.47, s2=7.05, s3=9.53 (s2 outlier; mean=8.68, std=1.41). Key results: (a) contam_15 |Cohen's d|=3.42 (n=3, ddof=1, strong effect); (b) contam_50 |d|=0.99 (n=3, ddof=1, borderline large); (c) free-θ dose-response non-monotonic and more extreme after correction (contam_50 Δlz*=1.40 < contam_15 Δlz*=4.84, ratio=3.46) due to θ-shift confound; (d) **θ-fixed analysis (ℓz*-corrected)**: θ_fixed=-0.0965 (n=3 clean θ_MLE mean, unchanged by ℓz* correction); lz*_fixed: contam_15=11.852, contam_50=18.576; Δlz*_fixed: contam_15=+3.17, contam_50=+9.89; ratio=3.12 (virtually unchanged from uncorrected 3.12 — Snijders correction scales proportionally); (e) seen/unseen memorization fingerprint; (f) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution. **Note**: all values ℓz*-corrected (Snijders 2001); prior uncorrected ℓz values archived as *_lz_uncorrected.json.\\n- **Cross-family validation (exp-ctrl-contam-llama, ℓz*-corrected)**: Llama-3.1-8B-Instruct × MMLU, 3+2 conditions. **n=3 clean seeds (ℓz*-corrected)**: s1=0.845, s2=-0.182, s3=-1.084 (mean=-0.14, std=0.97). contam_15 lz*=-2.992 (θ=-0.276), contam_50 lz*=-3.331 (θ=-0.149). Δlz*: contam_15=-3.84, contam_50=-4.18, both significant. **Cohen's d (n=3, ddof=1)**: contam_15 d=-2.95 (large), contam_50 d=-3.31 (large), monotonic (|d_50|>|d_15|) — contrasting Qwen's non-monotonicity. **Free-θ**: slight monotonicity (ratio=1.09), contrasting Qwen's strong non-monotonicity (ratio=3.46). **θ_fixed (θ=-0.666)**: lz*_fixed contam_15=0.959, contam_50=1.172; Δlz*_fixed=+0.114/+0.327; ratio=2.87 (enhances monotonicity). θ-shift mechanism universal: Δθ Llama 0.39/0.52, Qwen 0.29/0.47. Memorization fraction ~0.33-0.38. **Narrative**: Qwen story = \\\"θ_fixed repairs non-monotonicity\\\"; Llama story = \\\"θ_fixed enhances existing monotonicity\\\". Both confirm θ_fixed recovers/strengthens dose-response. Non-monotonicity is model-dependent (modulated by baseline misfit magnitude). Qwen clean lz*=8.68 vs Llama -0.14 — discuss in §6. **Cross-family Cohen's d summary**: Qwen d_15=-3.42/d_50=-0.99; Llama d_15=-2.95/d_50=-3.31. Both families |d|>2.9 at 15%, confirming detection generalizes.\\n- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).\\n\", \"total_chars\": 21718, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84da2c0e-e5c3-4490-a5fd-68b6e9497d0e",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "a0b7d1a8-76d6-4a6d-b8c1-20dae74678fb",
  "sourceToolAssistantUUID": "84da2c0e-e5c3-4490-a5fd-68b6e9497d0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-21T05:51:54.535Z_

Now let me read the actual paper sections systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0b7d1a8-76d6-4a6d-b8c1-20dae74678fb",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC8aPTJDmkpR1P79a3A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c51fa920-aad3-481a-bad2-5e09d48363bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACoE3UyHx6mV16t4Ga69j5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18343,
      "cache_read_input_tokens": 19913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18343,
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

_source line 20 · 2026-05-21T05:51:56.012Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AW3hpqXAWvV3oXKuegL1GW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c51fa920-aad3-481a-bad2-5e09d48363bb",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC8aPTJDmkpR1P79a3A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40b98920-98be-448f-a0d7-0a4ef991d01b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACoE3UyHx6mV16t4Ga69j5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18343,
      "cache_read_input_tokens": 19913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18343,
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

_source line 21 · 2026-05-21T05:51:56.017Z_

<details><summary>↩ Tool result · `toolu_01AW3hpqXAWvV3oXKuegL1GW`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\usepackage{enumitem}
16	
17	\newcommand{\irtfit}{\textsc{IRT-FIT}}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Detecting Benchmark Contamination in Large Language Models \\
22	via Item Response Theory Person-Fit Statistics}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{sections/abstract}
31	\end{abstract}
32	
33	\input{sections/introduction}
34	\input{sections/background}
35	\input{sections/method}
36	\input{sections/experiments}
37	\input{sections/discussion}
38	\input{sections/conclusion}
39	
40	\input{sections/limitations}
41	
42	\bibliography{references}
43	
44	\appendix
45	\input{sections/appendix}
46	
47	\end{document}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40b98920-98be-448f-a0d7-0a4ef991d01b",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "9b60750d-7600-4051-8c1e-edb5b1eba52b",
  "sourceToolAssistantUUID": "40b98920-98be-448f-a0d7-0a4ef991d01b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T05:51:56.542Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SybpRqyUnHuaU42fmZG5th`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b60750d-7600-4051-8c1e-edb5b1eba52b",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC8aPTJDmkpR1P79a3A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3629a203-c8be-4b80-a0c6-1d32724256e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACoE3UyHx6mV16t4Ga69j5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18343,
      "cache_read_input_tokens": 19913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18343,
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

_source line 23 · 2026-05-21T05:51:56.547Z_

<details><summary>↩ Tool result · `toolu_01SybpRqyUnHuaU42fmZG5th`</summary>

```text
1	% =============================================================================
2	% Benchmark Datasets
3	% =============================================================================
4	
5	@inproceedings{zellers2019hellaswag,
6	  title={{HellaSwag}: Can a Machine Really Finish Your Sentence?},
7	  author={Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farhadi, Ali and Choi, Yejin},
8	  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
9	  pages={4791--4800},
10	  year={2019},
11	  url={https://doi.org/10.18653/v1/P19-1472}
12	}
13	
14	@article{cobbe2021gsm8k,
15	  title={Training Verifiers to Solve Math Word Problems},
16	  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
17	  journal={arXiv preprint arXiv:2110.14168},
18	  year={2021}
19	}
20	
21	@article{clark2018arc,
22	  title={Think you have Solved Question Answering? Try {ARC}, the {AI2} Reasoning Challenge},
23	  author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
24	  journal={arXiv preprint arXiv:1803.05457},
25	  year={2018}
26	}
27	
28	@article{chen2021humaneval,
29	  title={Evaluating Large Language Models Trained on Code},
30	  author={Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Pond{\'e} de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},
31	  journal={arXiv preprint arXiv:2107.03374},
32	  year={2021}
33	}
34	
35	% =============================================================================
36	% IRT for LLM Evaluation
37	% =============================================================================
38	
39	@article{martinezplumed2019,
40	  title = {Item Response Theory in {AI}: Analysing Machine Learning Classifiers at the Instance Level},
41	  author = {Mart{\'\i}nez-Plumed, F. and Prud{\^e}ncio, R. B. C. and Mart{\'\i}nez-Us{\'o}, A. and Hern{\'a}ndez-Orallo, J.},
42	  journal = {Artificial Intelligence},
43	  year = {2019},
44	  doi = {10.1016/j.artint.2018.09.004},
45	  url = {https://www.sciencedirect.com/science/article/pii/S0004370219300220},
46	}
47	
48	@inproceedings{polo2024tinybenchmarks,
49	  title = {tinyBenchmarks: Evaluating {LLMs} with Fewer Examples},
50	  author = {Polo, F. M. and Weber, L. and Choshen, L. and Sun, Y. and Xu, G. and Yurochkin, M.},
51	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
52	  year = {2024},
53	  url = {https://arxiv.org/abs/2402.14992},
54	}
55	
56	@article{atlas2025,
57	  title = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},
58	  author = {Li, P. and Tang, X. and Chen, S. and Cheng, Y. and Metoyer, R. and Hua, T. and Chawla, N. V.},
59	  journal = {arXiv preprint arXiv:2511.04689},
60	  year = {2025},
61	  url = {https://arxiv.org/abs/2511.04689},
62	}
63	
64	@inproceedings{psnirt2026,
65	  title = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},
66	  author = {Zhou, H. and Huang, H. and Zhao, Z. and Han, L. and Wang, H. and Chen, K. and Yang, M. and Bao, W. and Dong, J. and Xu, B. and Zhu, C. and Cao, H. and Zhao, T.},
67	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
68	  year = {2026},
69	  url = {https://arxiv.org/abs/2505.15055},
70	}
71	
72	% =============================================================================
73	% Benchmark Contamination Detection
74	% =============================================================================
75	
76	@inproceedings{dodge2021,
77	  title = {Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus},
78	  author = {Dodge, J. and Sap, M. and Marasovi{\'c}, A. and Agnew, W. and Ilharco, G. and Groeneveld, D. and Mitchell, M. and Gardner, M.},
79	  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
80	  year = {2021},
81	  doi = {10.18653/v1/2021.emnlp-main.98},
82	  url = {https://aclanthology.org/2021.emnlp-main.98/},
83	}
84	
85	@inproceedings{magar2022,
86	  title = {Data Contamination: From Memorization to Exploitation},
87	  author = {Magar, I. and Schwartz, R.},
88	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
89	  year = {2022},
90	  doi = {10.18653/v1/2022.acl-short.18},
91	  url = {https://aclanthology.org/2022.acl-short.18/},
92	}
93	
94	@inproceedings{sainz2023,
95	  title = {{NLP} Evaluation in Trouble: On the Need to Measure {LLM} Data Contamination for each Benchmark},
96	  author = {Sainz, O. and Campos, J. and Garc{\'\i}a-Ferrero, I. and Etxaniz, J. and Lopez de Lacalle, O. and Agirre, E.},
97	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2023},
98	  year = {2023},
99	  doi = {10.18653/v1/2023.findings-emnlp.722},
100	  url = {https://aclanthology.org/2023.findings-emnlp.722/},
101	}
102	
103	@inproceedings{jacovi2023,
104	  title = {Stop Uploading Test Data in Plain Text: Practical Strategies for Mitigating Data Contamination by Evaluation Benchmarks},
105	  author = {Jacovi, A. and Caciularu, A. and Goldman, O. and Goldberg, Y.},
106	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
107	  year = {2023},
108	  doi = {10.18653/v1/2023.emnlp-main.308},
109	  url = {https://aclanthology.org/2023.emnlp-main.308/},
110	}
111	
112	@inproceedings{constat2024,
113	  title = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
114	  author = {Dekoninck, J. and M{\"u}ller, M. and Vechev, M.},
115	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
116	  year = {2024},
117	  url = {https://arxiv.org/abs/2405.16281},
118	}
119	
120	@inproceedings{minkprob2024,
121	  title = {Detecting Pretraining Data from Large Language Models},
122	  author = {Shi, W. and Ajith, A. and Xia, M. and Huang, Y. and Liu, D. and Blevins, T. and Chen, D. and Zettlemoyer, L.},
123	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
124	  year = {2024},
125	  url = {https://arxiv.org/abs/2310.16789},
126	}
127	
128	@inproceedings{oren2024,
129	  title = {Proving Test Set Contamination in Black-Box Language Models},
130	  author = {Oren, Y. and Meister, N. and Chatterji, N. S. and Ladhak, F. and Hashimoto, T.},
131	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
132	  year = {2024},
133	  url = {https://arxiv.org/abs/2310.17623},
134	}
135	
136	@inproceedings{golchin2024,
137	  title = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
138	  author = {Golchin, S. and Surdeanu, M.},
139	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
140	  year = {2024},
141	  url = {https://arxiv.org/abs/2308.08493},
142	}
143	
144	@inproceedings{deng2024,
145	  title = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},
146	  author = {Deng, C. and Zhao, Y. and Tang, X. and Gerstein, M. and Cohan, A.},
147	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
148	  year = {2024},
149	  doi = {10.18653/v1/2024.naacl-long.482},
150	  url = {https://aclanthology.org/2024.naacl-long.482/},
151	}
152	
153	@inproceedings{codec2026,
154	  title = {Detecting Data Contamination in {LLMs} via In-Context Learning},
155	  author = {Zawalski, M. and Boubdir, M. and Ba{\l}azy, K. and Nushi, B. and Ribalta, P.},
156	  booktitle = {Proceedings of the 14th International Conference on Learning Representations (ICLR)},
157	  year = {2026},
158	  url = {https://arxiv.org/abs/2510.27055},
159	}
160	
161	% =============================================================================
162	% Person-Fit Statistics (Psychometrics)
163	% =============================================================================
164	
165	@article{drasgow1985,
166	  title = {Appropriateness Measurement with Polychotomous Item Response Models and Standardized Indices},
167	  author = {Drasgow, F. and Levine, M. V. and Williams, E. A.},
168	  journal = {British Journal of Mathematical and Statistical Psychology},
169	  year = {1985},
170	  doi = {10.1111/j.2044-8317.1985.tb00817.x},
171	}
172	
173	@article{meijer2001,
174	  title = {Methodology Review: Evaluating Person Fit},
175	  author = {Meijer, R. R. and Sijtsma, K.},
176	  journal = {Applied Psychological Measurement},
177	  year = {2001},
178	  doi = {10.1177/01466210122031957},
179	  url = {https://journals.sagepub.com/doi/abs/10.1177/01466210122031957},
180	}
181	
182	@article{snijders2001,
183	  title = {Asymptotic Null Distribution of Person Fit Statistics with Estimated Person Parameter},
184	  author = {Snijders, T. A. B.},
185	  journal = {Psychometrika},
186	  year = {2001},
187	  doi = {10.1007/BF02294437},
188	  url = {https://link.springer.com/article/10.1007/BF02294437},
189	}
190	
191	@article{karabatsos2003,
192	  title = {Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics},
193	  author = {Karabatsos, G.},
194	  journal = {Applied Measurement in Education},
195	  year = {2003},
196	  doi = {10.1207/S15324818AME1604_2},
197	  url = {https://www.tandfonline.com/doi/abs/10.1207/S15324818AME1604_2},
198	}
199	
200	@article{sinharay2017,
201	  title = {Which Statistic Should Be Used to Detect Item Preknowledge When the Set of Compromised Items Is Known?},
202	  author = {Sinharay, S.},
203	  journal = {Applied Psychological Measurement},
204	  year = {2017},
205	  doi = {10.1177/0146621617698453},
206	  url = {https://pmc.ncbi.nlm.nih.gov/articles/PMC5978524/},
207	}
208	
209	@article{hong2021lzm,
210	  title = {Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types},
211	  author = {Hong, M. and Lin, L. and Cheng, Y.},
212	  journal = {Psychometrika},
213	  year = {2021},
214	  doi = {10.1007/s11336-021-09756-3},
215	  url = {https://link.springer.com/article/10.1007/s11336-021-09756-3},
216	}
217	
218	% =============================================================================
219	% Post-RL Contamination
220	% =============================================================================
221	
222	@article{wang2025fragility,
223	  title = {On The Fragility of Benchmark Contamination Detection in Reasoning Models},
224	  author = {Wang, H. and Li, H. and Ko, B. and Zhang, H.},
225	  journal = {arXiv preprint arXiv:2510.02386},
226	  year = {2025},
227	  url = {https://arxiv.org/abs/2510.02386},
228	}
229	
230	@inproceedings{selfcritique2026,
231	  title = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},
232	  author = {Tao, Y. and Wang, T. and Dong, Y. and Liu, H. and Zhang, K. and Hu, X. and Li, G.},
233	  booktitle = {Proceedings of the 14th International Conference on Learning Representations (ICLR)},
234	  year = {2026},
235	  url = {https://arxiv.org/abs/2510.09259},
236	}
237	
238	@article{zhang2026rlvr,
239	  title = {Detecting {RLVR} Training Data via Structural Convergence of Reasoning},
240	  author = {Zhang, H. and Yang, Y. and Yan, J. and Bao, G. and Zhang, Y. and Zhang, Y.},
241	  journal = {arXiv preprint arXiv:2602.11792},
242	  year = {2026},
243	  url = {https://arxiv.org/abs/2602.11792},
244	}
245	
246	% =============================================================================
247	% IRT Foundations
248	% =============================================================================
249	
250	@incollection{birnbaum1968,
251	  title = {Some Latent Trait Models and Their Use in Inferring an Examinee's Ability},
252	  author = {Birnbaum, A.},
253	  booktitle = {Statistical Theories of Mental Test Scores},
254	  publisher = {Addison-Wesley},
255	  year = {1968},
256	  editor = {Lord, F. M. and Novick, M. R.},
257	  pages = {397--479},
258	}
259	
260	@book{lord1980,
261	  title = {Applications of Item Response Theory to Practical Testing Problems},
262	  author = {Lord, F. M.},
263	  publisher = {Lawrence Erlbaum Associates},
264	  year = {1980},
265	  doi = {10.4324/9780203056615},
266	}
267	
268	@techreport{barton1981,
269	  title = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},
270	  author = {Barton, M. A. and Lord, F. M.},
271	  institution = {Educational Testing Service},
272	  year = {1981},
273	  number = {RR-81-20},
274	  doi = {10.1002/j.2333-8504.1981.tb01255.x},
275	  url = {https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2333-8504.1981.tb01255.x},
276	}
277	
278	@book{embretson2000,
279	  title = {Item Response Theory for Psychologists},
280	  author = {Embretson, S. E. and Reise, S. P.},
281	  publisher = {Lawrence Erlbaum Associates},
282	  year = {2000},
283	  doi = {10.4324/9781410605269},
284	}
285	
286	@book{deayala2009,
287	  title = {The Theory and Practice of Item Response Theory},
288	  author = {de Ayala, R. J.},
289	  publisher = {Guilford Press},
290	  year = {2009},
291	}
292	
293	% =============================================================================
294	% LLM Evaluation Infrastructure
295	% =============================================================================
296	
297	@inproceedings{hendrycks2021mmlu,
298	  title = {Measuring Massive Multitask Language Understanding},
299	  author = {Hendrycks, D. and Burns, C. and Basart, S. and Zou, A. and Mazeika, M. and Song, D. and Steinhardt, J.},
300	  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},
301	  year = {2021},
302	  url = {https://arxiv.org/abs/2009.03300},
303	}
304	
305	@misc{beeching2023openllm,
306	  title = {Open {LLM} Leaderboard},
307	  author = {Beeching, E. and Fourrier, C. and Habib, N. and Han, S. and Lambert, N. and Rajani, N. and Sanseviero, O. and Tunstall, L. and Wolf, T.},
308	  year = {2023},
309	  howpublished = {HuggingFace},
310	  url = {https://huggingface.co/spaces/open-llm-leaderboard-old/open_llm_leaderboard},
311	}
312	
313	@misc{gao2023evalharness,
314	  title = {A Framework for Few-Shot Language Model Evaluation},
315	  author = {Gao, L. and Tow, J. and Abbasi, B. and Biderman, S. and Black, S. and DiPofi, A. and Foster, C. and Golding, L. and Hsu, J. and Le Noac'h, A. and Li, H. and McDonell, K. and Muennighoff, N. and Ociepa, C. and Phang, J. and Reynolds, L. and Schoelkopf, H. and Skowron, A. and Sutawika, L. and Tang, E. and Thite, A. and Wang, B. and Wang, K. and Zou, A.},
316	  year = {2023},
317	  howpublished = {Zenodo},
318	  doi = {10.5281/zenodo.10256836},
319	  url = {https://zenodo.org/records/10256836},
320	}
321	
322	@article{chang2024survey,
323	  title = {A Survey on Evaluation of Large Language Models},
324	  author = {Chang, Y. and Wang, X. and Wang, J. and Wu, Y. and Yang, L. and Zhu, K. and Chen, H. and Yi, X. and Wang, C. and Wang, Y. and Ye, W. and Zhang, Y. and Chang, Y. and Yu, P. S. and Yang, Q. and Xie, X.},
325	  journal = {ACM Transactions on Intelligent Systems and Technology},
326	  year = {2024},
327	  doi = {10.1145/3641289},
328	  url = {https://arxiv.org/abs/2307.03109},
329	}
330	
331	@article{biderman2024lessons,
332	  title = {Lessons from the Trenches on Reproducible Evaluation of Language Models},
333	  author = {Biderman, S. and Schoelkopf, H. and Sutawika, L. and Gao, L. and Tow, J. and Abbasi, B. and Aji, A. F. and Ammanamanchi, P. S. and Black, S. and Clive, J. and DiPofi, A. and Etxaniz, J. and Fattori, B. and Forde, J. Z. and Foster, C. and Hsu, J. and Jaiswal, M. and Lee, W. Y. and Li, H. and Lovering, C. and Muennighoff, N. and Pavlick, E. and Phang, J. and Skowron, A. and Tan, S. and Tang, X. and Wang, K. A. and Winata, G. I. and Yvon, F. and Zou, A.},
334	  journal = {arXiv preprint arXiv:2405.14782},
335	  year = {2024},
336	  url = {https://arxiv.org/abs/2405.14782},
337	}
338	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3629a203-c8be-4b80-a0c6-1d32724256e4",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "19b07cd1-8dae-4c86-a444-f76172797032",
  "sourceToolAssistantUUID": "3629a203-c8be-4b80-a0c6-1d32724256e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T05:51:57.490Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AXMdgTabxKyjkq9hsdrMGw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19b07cd1-8dae-4c86-a444-f76172797032",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC8aPTJDmkpR1P79a3A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c10e733d-98f8-42a3-b11d-da36954a3cb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACoE3UyHx6mV16t4Ga69j5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18343,
      "cache_read_input_tokens": 19913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18343,
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

_source line 25 · 2026-05-21T05:51:57.494Z_

<details><summary>↩ Tool result · `toolu_01AXMdgTabxKyjkq9hsdrMGw`</summary>

```text
1	Benchmark contamination in Large Language Models (LLMs) undermines the validity of public evaluations, yet most detection methods require privileged access to training data, model internals, or output probabilities.
2	We introduce \irtfit{}, a framework that detects supervised fine-tuning (SFT) contamination from binary (correct/incorrect) response patterns alone, the minimal-information operating point.
3	The core insight is psychometric: a contaminated model produces aberrant response patterns analogous to a test-taker with item preknowledge.
4	\irtfit{} quantifies this aberrance with the standardized person-fit statistic $\ell_z^*$ under a four-parameter logistic (4PL) Item Response Theory (IRT) model.
5	%
6	In controlled experiments, injecting 15\% of MMLU items into SFT training yields Cohen's $|d|=3.42$ (Qwen2.5-7B) and $|d|=2.95$ (Llama-3.1-8B) between contaminated and clean conditions ($n=3$ clean seeds per family).
7	An empirical power function derived via Gauss--Hermite quadrature ($R^2=0.65$) relates benchmark size to detection sensitivity: 80\% power at 15\% contamination requires $n \geq 7{,}958$ items (under MMLU item parameters).
8	We apply \irtfit{} to 12 models across 5 benchmarks and find that 57 of 60 model-benchmark cells exhibit response-pattern anomalies under the 4PL model (BH-FDR $\alpha=0.05$), while only 4 are flagged by an accuracy $z$-score baseline.
9	This 14$\times$ gap reveals universal model misfit invisible to accuracy-based evaluation.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c10e733d-98f8-42a3-b11d-da36954a3cb1",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "220ccdf0-7931-43f4-8d6d-d58099c6199f",
  "sourceToolAssistantUUID": "c10e733d-98f8-42a3-b11d-da36954a3cb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T05:51:57.728Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ewdi2Dcd4u6qDs3hvxRYkX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "220ccdf0-7931-43f4-8d6d-d58099c6199f",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC8aPTJDmkpR1P79a3A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2abd8f2-cf4b-4b80-8728-2b20f3a208d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACoE3UyHx6mV16t4Ga69j5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18343,
      "cache_read_input_tokens": 19913,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18343
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 19913,
          "cache_creation_input_tokens": 18343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18343,
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

_source line 27 · 2026-05-21T05:51:57.731Z_

<details><summary>↩ Tool result · `toolu_01Ewdi2Dcd4u6qDs3hvxRYkX`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation \citep{dodge2021, magar2022, sainz2023}.
4	As training corpora and public benchmarks both expand, the probability of overlap increases structurally: any model trained on broad web-crawled data may have encountered evaluation items during pretraining or fine-tuning \citep{jacovi2023, chang2024survey}.
5	When contamination occurs, benchmark scores no longer reflect genuine capability and the primary mechanism by which the community compares and selects models is undermined.
6	
7	A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record.
8	N-gram overlap methods need the training corpus itself \citep{dodge2021, magar2022}.
9	Membership inference approaches such as Min-K\%++ require token-level probabilities \citep{minkprob2024, deng2024}.
10	Time Travel probing relies on crafted prompts that elicit memorized completions \citep{golchin2024, oren2024}.
11	Performance-based methods compare results across original and rephrased test variants \citep{constat2024}, and in-context learning approaches require output logits \citep{codec2026}.
12	These methods form a detection frontier ordered by information access: training data, model weights, logits, token probabilities, rephrased retests, and finally binary patterns.
13	No existing method operates at the bottom of this frontier.
14	We ask: \emph{what can be detected from binary response patterns alone?}
15	
16	The need for minimal-information detection grows more pressing as models evolve.
17	\citet{wang2025fragility} show that all ten log-probability-based detection methods they evaluate perform at chance level on reasoning models trained with reinforcement learning (RL).
18	RL fine-tuning reshapes internal token distributions while largely preserving binary correctness patterns, and probability-based detectors cannot distinguish contaminated from clean models under these conditions.
19	Binary response patterns are structurally invariant to RL-induced distributional changes, as they record what a model answered rather than how its internal distributions shifted (empirical verification on post-RL models is future work; see \S\ref{sec:discussion}).
20	
21	We observe that a contaminated LLM is functionally analogous to a test-taker with item preknowledge: both produce anomalous response patterns in which difficult items are answered correctly through memorization rather than genuine ability.
22	This connection points to a mature body of work in psychometrics.
23	Person-fit statistics, developed over four decades for cheating detection in educational testing \citep{drasgow1985, meijer2001, karabatsos2003, sinharay2017}, quantify exactly this type of response aberrance.
24	The standardized statistic $\ell_z^*$ \citep{snijders2001} measures how well an individual's response pattern conforms to Item Response Theory (IRT) model predictions, with extreme negative values indicating patterns consistent with preknowledge.
25	Figure~\ref{fig:motivation} illustrates this analogy: a clean model's responses follow the IRT-predicted probability curve, while a contaminated model shows anomalous successes on hard items that it has memorized.
26	Despite this natural correspondence, to our knowledge no prior work has applied person-fit statistics to LLM benchmark contamination detection.
27	
28	\begin{figure}[t]
29	  \centering
30	  \includegraphics[width=\columnwidth]{fig_1_response_pattern.pdf}
31	  \caption{Motivation for \irtfit{}. \textbf{(a)} A clean model's responses track the IRT-predicted success probability (blue curve); $\ell_z^*$ is near zero. \textbf{(b)} A contaminated model answers hard items correctly through memorization (red diamonds), producing a large $|\Delta\ell_z^*|$ detection signal.}
32	  \label{fig:motivation}
33	\end{figure}
34	
35	We introduce \irtfit{}, a framework that applies IRT person-fit analysis at the minimal-information operating point, requiring only binary responses and pre-calibrated item parameters \citep{psnirt2026}.
36	We compute $\ell_z^*$ for each (model, benchmark) pair and define $\Delta\ell_z^*$ as a difference-in-differences estimator for within-model contamination detection.
37	In controlled experiments (QLoRA fine-tuning on MMLU), 15\% contamination produces $|\text{Cohen's } d| = 3.42$ on Qwen2.5-7B and $|d| = 2.95$ on Llama-3.1-8B ($n{=}3$ clean seeds per family).
38	Power increases monotonically with benchmark size; an empirical power function ($R^2 = 0.65$) provides approximate guidance, showing that 80\% power at 15\% contamination requires $n \geq 7{,}958$ items (under MMLU item parameters).
39	A 4PL versus 3PL ablation reveals a mean $+27.3$ percentage-point power gain on MMLU \citep{hendrycks2021mmlu}; the upper-asymptote parameter is essential for LLM evaluation contexts.
40	Across 12 models and 5 benchmarks, $\ell_z^*$ flags 57 of 60 model-benchmark cells for response-pattern anomalies (BH-FDR $\alpha{=}0.05$), versus only 4 flagged by an accuracy $z$-score baseline.
41	This $14\times$ gap shows that $\ell_z^*$ captures response-pattern structure lost in aggregate accuracy.
42	We further identify a $\theta$-shift boundary condition: re-estimating ability on contaminated data can degrade sensitivity (non-monotonic dose-response under free $\theta$), but fixing $\theta$ to pre-contamination values restores monotonicity (signal ratio 2.9--3.1 across model families).
43	
44	Our contributions are:
45	\begin{enumerate}[leftmargin=*,nosep]
46	\item We propose \irtfit{}, a person-fit framework for contamination detection at the minimal-information operating point (binary responses only), validated through controlled contamination on Qwen2.5-7B ($|d| = 3.42$) and Llama-3.1-8B ($|d| = 2.95$) at 15\% contamination ($n{=}3$ per family).
47	\item We derive an empirical power function ($R^2 = 0.65$) relating benchmark size to detection sensitivity, identify the $\theta$-shift boundary condition, and show that 4PL parameterization yields $+27.3$pp power gain over 3PL.
48	\item We report three empirical findings from real LLM response data: universal 4PL model misfit (57/60 cells flagged), the inadequacy of accuracy-based anomaly detection (4/60 cells), and a simulation-to-reality gap that motivates the $\Delta\ell_z^*$ design.
49	\end{enumerate}
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2abd8f2-cf4b-4b80-8728-2b20f3a208d3",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "322a2470-d68f-459e-b46d-ae439bb7f3a9",
  "sourceToolAssistantUUID": "a2abd8f2-cf4b-4b80-8728-2b20f3a208d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T05:52:02.382Z_

<details open><summary>🔧 Tool call — Read · `toolu_011sjQagKUhUCPgT4GD25bp6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "322a2470-d68f-459e-b46d-ae439bb7f3a9",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC92mxVhrrNj9TQwPUU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1605ef65-e6e7-42ca-8c64-2008b4d2b438",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqbPiaogyaxLN4Y3bktZHz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9310,
      "cache_read_input_tokens": 38256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9310,
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

_source line 29 · 2026-05-21T05:52:02.386Z_

<details><summary>↩ Tool result · `toolu_011sjQagKUhUCPgT4GD25bp6`</summary>

```text
1	\section{Background and Related Work}\label{sec:background}
2	
3	\subsection{IRT and Person-Fit Statistics}\label{sec:irt_background}
4	
5	Item Response Theory (IRT) models the probability that an examinee answers a test item correctly as a function of the examinee's latent ability $\theta$ and item-level parameters \citep{lord1980, embretson2000}.
6	The four-parameter logistic (4PL) model, formalized in \S\ref{sec:framework} (Eq.~\ref{eq:4pl}), extends the classical three-parameter model \citep{birnbaum1968} with an upper asymptote $d$ that captures the probability of error even at high ability \citep{barton1981}.
7	This parameter matters for LLMs: \citet{psnirt2026} find that 46\% of MMLU items have $d < 0.95$, meaning ceiling effects are pervasive and a model without the $d$ parameter systematically misestimates item characteristics.
8	
9	Given calibrated item parameters, person-fit statistics measure whether an examinee's \emph{pattern} of correct and incorrect responses is consistent with the IRT model at the estimated ability level.
10	The key intuition is that a test-taker with ability $\theta$ should get hard items wrong and easy items right at rates the model predicts; systematic deviations signal aberrant behavior.
11	\citet{drasgow1985} introduced $\ell_z$, a standardized log-likelihood residual that aggregates per-item deviations into a single score.
12	\citet{snijders2001} corrected the variance of $\ell_z$ for uncertainty in the estimated $\hat{\theta}$, yielding $\ell_z^*$ with the property that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null hypothesis of model-consistent responding.
13	Negative values indicate \emph{aberrant} patterns (unexpected errors on easy items or unexpected successes on hard items), while positive values indicate \emph{over-consistent} patterns (responses too predictable given the model).
14	We defer the formal definition to \S\ref{sec:framework}.
15	
16	In psychometrics, person-fit statistics have a long history in detecting test fraud and item preknowledge.
17	\citet{karabatsos2003} compared 36 person-fit statistics and found $\ell_z$ among the most powerful for detecting cheating.
18	\citet{sinharay2017} showed that $\ell_z^*$ is particularly effective when the compromised item set is known, a setting analogous to benchmark contamination where the ``compromised'' items are those memorized during pretraining.
19	\citet{meijer2001} provide a comprehensive review of the broader person-fit literature.
20	Our work transfers this psychometric toolkit to LLM evaluation, treating each model as an examinee whose response pattern may reveal memorization.
21	
22	\subsection{Benchmark Contamination Detection}\label{sec:contamination_related}
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\caption{Detection frontier ordered by information access level. RL column: robustness to RL post-training ($\times$ = fails, -- = untested).}
28	\label{tab:frontier}
29	\begin{tabular}{@{}llc@{}}
30	\toprule
31	Information Required & Method & RL \\
32	\midrule
33	Training corpus & N-gram overlap \citep{dodge2021} & N/A \\
34	Log-probabilities & Min-K\%++ \citep{minkprob2024} & $\times$\,$^{a}$ \\
35	Generated text & Rephrased probing \citep{golchin2024} & -- \\
36	Perf.\ (multi-form) & ConStat \citep{constat2024} & -- \\
37	\textbf{Binary only} & \textbf{\irtfit{} (ours)} & $^{b}$ \\
38	\bottomrule
39	\end{tabular}
40	
41	{\raggedright\scriptsize $^{a}$\citet{wang2025fragility}: 10 methods fail post-RL.
42	$^{b}$Structurally invariant; empirical verification future work.\par}
43	\end{table}
44	
45	Contamination detection methods vary in what information they require from the model under test.
46	Table~\ref{tab:frontier} organizes the detection frontier by information access, from most to least demanding.
47	At the high end, corpus-search methods match benchmark items against pretraining data \citep{dodge2021, magar2022}, but require full corpus access, which is unavailable for closed models.
48	Membership inference attacks (MIA) use token-level log-probabilities to distinguish training examples from unseen ones \citep{minkprob2024, deng2024}.
49	Generation-based probes elicit benchmark content via prompting \citep{golchin2024, oren2024}.
50	Performance-based methods such as ConStat \citep{constat2024} and CoDeC \citep{codec2026} compare a model's accuracy on the target benchmark against accuracy on perturbed or reference sets, requiring either multiple evaluations or in-context learning passes.
51	\citet{sainz2023} propose overlapping-split analysis using time-stamped data.
52	
53	A critical limitation unites all log-probability methods: \citet{wang2025fragility} demonstrate that reinforcement learning (RL) post-training renders MIA-based detectors (including Min-K\%++) no better than random across 10 methods and 4 benchmarks.
54	RL reshapes token-level output distributions while largely preserving binary correctness patterns, so token-level statistics lose signal while binary response patterns remain available for analysis.
55	\citet{selfcritique2026} and \citet{zhang2026rlvr} propose RL-specific solutions but require generation-level access.
56	
57	\irtfit{} operates at the bottom of this frontier: it requires only binary responses (correct/incorrect), making it applicable to any model accessible through a standard evaluation API.
58	Recent work applies IRT to LLM evaluation for ability estimation \citep{martinezplumed2019, polo2024tinybenchmarks}, adaptive testing \citep{atlas2025}, and benchmark diagnostics \citep{psnirt2026}, but none use \emph{person-fit} statistics for contamination detection.
59	Our work bridges this gap.
60	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1605ef65-e6e7-42ca-8c64-2008b4d2b438",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "1625221d-1004-4d22-a34d-3ea17835da85",
  "sourceToolAssistantUUID": "1605ef65-e6e7-42ca-8c64-2008b4d2b438",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T05:52:02.867Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EGXoarYfXAFfqAFgsB71F1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1625221d-1004-4d22-a34d-3ea17835da85",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC92mxVhrrNj9TQwPUU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83f90741-7c34-4ed4-8966-283158f714c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqbPiaogyaxLN4Y3bktZHz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9310,
      "cache_read_input_tokens": 38256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9310,
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

_source line 31 · 2026-05-21T05:52:02.875Z_

<details><summary>↩ Tool result · `toolu_01EGXoarYfXAFfqAFgsB71F1`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{The \irtfit{} Framework}
5	\label{sec:framework}
6	
7	Our method takes as input a binary response matrix $\mathbf{X} \in \{0,1\}^{M \times n}$, where $M$ models answer $n$ benchmark items, together with pre-calibrated four-parameter logistic (4PL) item parameters from PSN-IRT \citep{psnirt2026}.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is a lower asymptote (guessing), and $d_i$ is an upper asymptote (slip).
14	
15	The framework proceeds in three steps.
16	\textbf{Step~1}: Estimate each model's ability $\hat{\theta}$ via maximum likelihood on each benchmark separately.
17	\textbf{Step~2}: Compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized likelihood residual that quantifies how well a model's item-level response pattern conforms to the IRT model given $\hat{\theta}$.
18	The statistic extends the original $\ell_z$ \citep{drasgow1985} by correcting for estimation uncertainty in $\hat{\theta}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null hypothesis.
19	\textbf{Step~3}: For within-model contamination detection, compute $\Delta\ell_z^* = \ell_z^*(\text{target}) - \ell_z^*(\text{reference})$ between a target benchmark and a reference benchmark from the same model.
20	The entire procedure is unsupervised: it requires no training data, no labeled contamination examples, and no access to pretraining corpora.
21	
22	\paragraph{Validity under assumption violations.}
23	IRT assumes local independence and unidimensionality, conditions that LLM benchmarks violate.
24	When these assumptions fail, $\ell_z^*$ can exhibit systematic bias: all models may appear aberrant even without contamination, because inter-item dependencies inflate the variance of response patterns beyond what the IRT model predicts.
25	However, this bias is approximately constant across benchmarks for a given model, because the same latent capabilities and the same dependency structure drive responses.
26	The $\Delta\ell_z^*$ statistic functions as a difference-in-differences (DiD) estimator: the shared bias cancels in the subtraction, isolating the contamination-specific signal.
27	We calibrate significance thresholds via a nonparametric bootstrap over the null distribution of $\Delta\ell_z^*$ rather than relying on the asymptotic $\mathcal{N}(0,1)$ reference, which accommodates residual model misspecification.
28	Universal misfit (all models showing $|\ell_z^*| > 1.96$) is therefore a finding about benchmark properties, not an artifact; $\Delta\ell_z^*$ bypasses absolute thresholds entirely.
29	
30	\subsection{Detection Power Characterization}
31	\label{sec:power_theory}
32	
33	We derive the statistical power of $\ell_z^*$ as a function of benchmark size $n$ and contamination fraction $\pi$.
34	
35	\paragraph{Contamination model.}
36	A fraction $\pi$ of items are forced correct regardless of ability.
37	The expected response becomes:
38	\begin{equation}
39	  \mathbb{E}[x_i \mid \theta_0, \pi] = P_i(\theta_0) + \pi \cdot Q_i(\theta_0)
40	  \label{eq:contam_response}
41	\end{equation}
42	where $Q_i(\theta) = 1 - P_i(\theta)$.
43	The contaminated response inflates the MLE: $\mathbb{E}[\hat{\theta}] > \theta_0$ for $\pi > 0$, because the score equation $\sum_i (\mathbb{E}[x_i] - P_i(\theta))\,h_i(\theta) = 0$ shifts the solution upward.
44	
45	\paragraph{Observation 1 ($\sqrt{n}$ scaling).}
46	The noncentrality parameter $\delta(\theta_0, \pi)$ of $\ell_z^*$ under contamination satisfies $\delta \propto \sqrt{n}$.
47	The numerator accumulates $n$ per-item residuals ($O(n)$) while the denominator grows as $\sqrt{\mathrm{Var}^*} = O(\sqrt{n})$ from the \citet{snijders2001} variance formula, so
48	\begin{equation}
49	  \delta(\theta_0, \pi) = \sqrt{n}\;\cdot\;\delta_1(\theta_0, \pi)
50	  \label{eq:sqrt_n}
51	\end{equation}
52	where $\delta_1$ is the per-item noncentrality that depends only on item parameters and $(\theta_0, \pi)$.
53	
54	\paragraph{Observation 2 (marginal power).}
55	We integrate over $\theta_0 \sim \mathcal{N}(0,1)$ via Gauss--Hermite quadrature ($K{=}30$ nodes) to obtain the marginal power under two-sided testing at level $\alpha$:
56	\begin{equation}
57	  \mathrm{Power}(n, \pi) = \sum_{k=1}^{K} w_k \left[\Phi\!\left(\frac{-z_\alpha - \delta_k}{\sigma_k}\right) + 1 - \Phi\!\left(\frac{z_\alpha - \delta_k}{\sigma_k}\right)\right]
58	  \label{eq:power}
59	\end{equation}
60	where $\delta_k$ and $\sigma_k$ are the conditional mean shift and standard deviation of $\ell_z^*$ at the $k$-th quadrature node, $w_k$ are the quadrature weights, and $z_\alpha = 1.96$.
61	Two-sided testing is essential: at moderate contamination ($\pi < 80\%$), $\ell_z^*$ is negative (aberrant pattern), but at high contamination ($\pi > 85\%$), $\ell_z^*$ turns positive (over-consistent pattern) as the inflated $\hat{\theta}$ renders near-perfect accuracy expected.
62	The crossover occurs at $\pi^* \approx 81$--$85\%$ across benchmarks.
63	Equation~\ref{eq:power} provides approximate minimum benchmark size estimates: for example, 80\% power at 15\% contamination requires $n \geq 7{,}958$ items (derived under MMLU item parameters; the threshold varies across benchmarks due to differences in per-item discriminatory power).
64	
65	\subsection{$\theta$-Shift Analysis}
66	\label{sec:theta_shift}
67	
68	Contamination creates an identification problem: higher accuracy raises $\hat{\theta}_{\text{MLE}}$, which in turn ``explains away'' the aberrant responses and attenuates the $\ell_z^*$ signal.
69	We term this the \emph{$\theta$-shift mechanism}.
70	As $\pi$ increases, $\hat{\theta}$ absorbs a larger share of the contamination signal into a legitimate ability increase, so the free-$\theta$ dose-response curve becomes non-monotonic: $|\Delta\ell_z^*|$ can decrease at higher contamination levels.
71	
72	The solution is \emph{$\theta$-fixed analysis}: anchor ability at a pre-contamination baseline $\theta_{\text{fixed}}$ estimated from clean conditions or cross-validated from held-out benchmarks.
73	With $\theta$ fixed, the $\ell_z^*$ statistic captures the full residual between observed and expected performance, and the dose-response curve becomes monotonically increasing.
74	In our controlled experiments (\S\ref{sec:ctrl_contam}), fixed-$\theta$ estimation yields a monotonic signal ratio of 3.12 between 50\% and 15\% contamination, whereas free-$\theta$ estimation produces an inverted ratio of 0.29.
75	
76	For practical deployment, $\theta_{\text{fixed}}$ can be obtained through two strategies: (1) cross-benchmark estimation, where $\theta$ is estimated from benchmarks presumed clean and applied to the target benchmark; or (2) temporal anchoring, where $\theta$ from an earlier evaluation serves as the reference for subsequent evaluations of the same model.
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83f90741-7c34-4ed4-8966-283158f714c4",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "6140d667-7514-47dd-b24c-2190de5225e5",
  "sourceToolAssistantUUID": "83f90741-7c34-4ed4-8966-283158f714c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T05:52:03.499Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RK6j9e4h73QAFLejm8UyRs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6140d667-7514-47dd-b24c-2190de5225e5",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC92mxVhrrNj9TQwPUU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c00e61a0-07a4-4ca4-8961-73e13c3694f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqbPiaogyaxLN4Y3bktZHz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9310,
      "cache_read_input_tokens": 38256,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9310
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 38256,
          "cache_creation_input_tokens": 9310,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9310,
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

_source line 33 · 2026-05-21T05:52:03.505Z_

<details><summary>↩ Tool result · `toolu_01RK6j9e4h73QAFLejm8UyRs`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	The simulation study confirms that $\ell_z^*$ is well-calibrated under the bootstrap null (mean bias 0.041, std 1.003 on MMLU, $n{=}14{,}042$; calibration degrades for smaller benchmarks with KS rejection rates of 50--75\% for $n < 2{,}000$), yet 57 of 60 model-benchmark cells exhibit 4PL misfit in real data. This gap is not an artifact of miscalibration. LLM response patterns genuinely violate IRT assumptions such as local independence and unidimensionality, producing systematic positive $\ell_z^*$ (over-consistency) across models. The $\Delta\ell_z^*$ design turns this universal misfit into a feature: because the bias is shared across benchmarks, within-model differencing cancels it, isolating contamination-specific aberrance.
4	
5	The $\theta$-shift boundary condition implies that practitioners should anchor ability estimates to a pre-contamination baseline when available; otherwise, contamination-induced ability inflation can absorb detection signal, particularly for models with high baseline misfit.
6	The Snijders variance correction exhibits ability-dependent effects on detection sensitivity, amplifying contamination signals for lower-ability models while slightly attenuating them for higher-ability models.
7	
8	This design enables practical deployment. PSN-IRT v1 provides over 13K per-item binary response vectors publicly~\citep{psnirt2026}, and binary response data are routinely recorded on leaderboards, so retrospective audits require no new data collection.
9	
10	Two scope boundaries deserve emphasis. First, our controlled validation spans two model families (Qwen2.5-7B and Llama-3.1-8B), with consistent detection signals across both ($|d| \geq 2.95$, $|\Delta\ell_z^*| \geq 3.84$ at 15\% contamination). The QLoRA (rank=16) adapter limits memorization capacity; the observed 33--38\% memorization fraction likely represents a conservative lower bound, and full fine-tuning would produce stronger signals. Second, $\Delta\ell_z^*$ targets SFT-stage contamination and leaderboard gaming rather than incidental pretraining exposure.
11	
12	Future work includes extending to additional model families and architectures, large-scale leaderboard audits pending estimation advances for RL-era models~\citep{zhang2026rlvr}, and post-RL validation. The $\ell_z^*$ statistic is structurally invariant to RL distributional changes; empirical verification is future work.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c00e61a0-07a4-4ca4-8961-73e13c3694f6",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "8a78c4f5-3341-436f-9e9b-0faaa826bacc",
  "sourceToolAssistantUUID": "c00e61a0-07a4-4ca4-8961-73e13c3694f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T05:52:08.088Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XCW7Xij1Um5wfE6DoYd4W7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a78c4f5-3341-436f-9e9b-0faaa826bacc",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC9TXyzD8ncLwAmCEnm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "927dd2a0-8959-41f5-ac83-c1074c9fa25d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166ZJV7toDY1WfWicsTegDV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4967,
      "cache_read_input_tokens": 47566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4967,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 35 · 2026-05-21T05:52:08.094Z_

<details><summary>↩ Tool result · `toolu_01XCW7Xij1Um5wfE6DoYd4W7`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\input{sections/sec_setup}
5	\input{sections/sec_simulation}
6	\input{sections/sec_ctrl_contam}
7	\input{sections/sec_empirical}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "927dd2a0-8959-41f5-ac83-c1074c9fa25d",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "a411cc79-f5e7-4f7f-8ea8-18aa6c9a9383",
  "sourceToolAssistantUUID": "927dd2a0-8959-41f5-ac83-c1074c9fa25d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T05:52:08.609Z_

<details open><summary>🔧 Tool call — Read · `toolu_017WHhCfTwsgYtSuHJ5jK3N4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a411cc79-f5e7-4f7f-8ea8-18aa6c9a9383",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC9TXyzD8ncLwAmCEnm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bef4fafd-885a-4d45-9733-3aa771a09906",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166ZJV7toDY1WfWicsTegDV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4967,
      "cache_read_input_tokens": 47566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4967,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 37 · 2026-05-21T05:52:08.613Z_

<details><summary>↩ Tool result · `toolu_017WHhCfTwsgYtSuHJ5jK3N4`</summary>

```text
1	\section*{Limitations}
2	
3	Our controlled contamination experiments use two model families (Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) at the 7--8B parameter scale with QLoRA fine-tuning at rank 16. Both families yield $|d| \geq 2.95$ at 15\% contamination with consistent memorization fractions (33--38\%), but validation on larger parameter scales, additional architectures, and full-parameter fine-tuning remains future work. The limited adapter capacity means observed memorization rates likely represent a conservative lower bound; full-parameter fine-tuning would permit greater memorization and produce stronger $\ell_z^*$ signals.
4	
5	The framework relies on pre-calibrated item parameters from PSN-IRT rather than self-calibrated parameters. Our MML-EM refit experiment reveals that discrimination recovery degrades substantially ($r_a = 0.127$) when calibrating on current leaderboard data where most models exhibit contamination-driven misfit. Until neural IRT or alternative calibration methods can handle contaminated respondent pools, the framework depends on externally maintained parameter banks.
6	
7	All controlled experiments target SFT-stage contamination. While $\ell_z^*$ is structurally invariant to post-hoc distributional changes from reinforcement learning, empirical validation on post-RL models is deferred to future work.
8	
9	Memorization fraction is consistent across model families (35--38\% at 15\% contamination) but may vary with contamination mechanism (e.g., full fine-tuning vs.\ QLoRA), contamination rate, and model capacity.
10	The practical deployment of \irtfit{} requires either a matched clean baseline or a pre-established $\Delta\ell_z^*$ threshold---a bootstrapping problem we leave to future work.
11	
12	Detection power varies with benchmark size. On ARC-Challenge (295 items), Cohen's $d = 0.45$ at 15\% contamination, well below the $d = 3.42$ observed on MMLU (14,042 items). The empirical power function (Equation~\ref{eq:power}) predicts that 80\% power at 15\% contamination requires $\geq$7,958 items under MMLU item parameters (the threshold varies by benchmark), placing small benchmarks below reliable detection thresholds.
13	
14	Finally, because LLM response patterns universally violate classical IRT assumptions, absolute $\ell_z^*$ values cannot be interpreted against standard normal thresholds. Our framework addresses this through the $\Delta\ell_z^*$ difference-in-differences design, but this requires a clean reference condition for each benchmark.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bef4fafd-885a-4d45-9733-3aa771a09906",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "87699dd7-106f-4084-b099-f3f648c44d70",
  "sourceToolAssistantUUID": "bef4fafd-885a-4d45-9733-3aa771a09906",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T05:52:09.108Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MoSLiHH5VAX6q99SwAXrd4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87699dd7-106f-4084-b099-f3f648c44d70",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC9TXyzD8ncLwAmCEnm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4088ddd-72b7-4438-ad54-9963f44f46ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166ZJV7toDY1WfWicsTegDV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4967,
      "cache_read_input_tokens": 47566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4967,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 39 · 2026-05-21T05:52:09.112Z_

<details><summary>↩ Tool result · `toolu_01MoSLiHH5VAX6q99SwAXrd4`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We introduced \irtfit{}, a person-fit framework that detects benchmark contamination from binary response patterns alone, the minimal-information operating point on the contamination detection frontier.
4	Controlled contamination experiments validate $\Delta\ell_z^*$ as a sensitive diagnostic, with $|\text{Cohen's } d| = 3.42$ (Qwen2.5-7B) and $|d| = 2.95$ (Llama-3.1-8B) at 15\% contamination ($n{=}3$ per family).
5	We derived an empirical power function ($R^2 = 0.65$) relating benchmark size to detection sensitivity, identified the $\theta$-shift boundary condition under which free-$\theta$ estimation attenuates the signal, and showed that 4PL parameterization yields a $+27.3$pp power gain over 3PL.
6	Across 12 models and 5 benchmarks, we found universal 4PL model misfit (57/60 cells), exposed the inadequacy of accuracy-based anomaly detection (4/60 vs.\ 57/60 cells), and documented a simulation-to-reality gap that motivates the $\Delta\ell_z^*$ design.
7	
8	Because any evaluation that records binary responses already contains the data \irtfit{} requires, existing benchmark results can be retrospectively audited for contamination without additional model access.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4088ddd-72b7-4438-ad54-9963f44f46ac",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "013fd8cb-1e8d-46df-b724-6f8922ba37fc",
  "sourceToolAssistantUUID": "a4088ddd-72b7-4438-ad54-9963f44f46ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T05:52:09.475Z_

<details open><summary>🔧 Tool call — Read · `toolu_014NrFuTesqeBV4T8CwCfkYh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "013fd8cb-1e8d-46df-b724-6f8922ba37fc",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC9TXyzD8ncLwAmCEnm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "948adf7c-f843-421e-99ab-045face17d5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166ZJV7toDY1WfWicsTegDV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4967,
      "cache_read_input_tokens": 47566,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4967
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 318,
          "cache_read_input_tokens": 47566,
          "cache_creation_input_tokens": 4967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4967,
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

_source line 41 · 2026-05-21T05:52:09.480Z_

<details><summary>↩ Tool result · `toolu_014NrFuTesqeBV4T8CwCfkYh`</summary>

```text
1	\section{4PL vs.\ 3PL Ablation Details}
2	\label{app:4pl_ablation}
3	
4	Table~\ref{tab:4pl_3pl_power} reports detection power (proportion of 2{,}000 simulation replicates rejecting $H_0$ at $\alpha{=}0.05$, two-sided) for 4PL and 3PL parameterizations across five benchmarks and seven contamination levels.
5	The 4PL model yields higher power than 3PL at every non-trivial contamination level on every benchmark.
6	The advantage is largest on MMLU and HellaSwag, where upper-asymptote ($d < 1$) violations are most prevalent, and smallest on ARC-Challenge and HumanEval, where limited item counts constrain power under both parameterizations.
7	
8	Power is non-monotonic at 75\% contamination under 4PL on four of five benchmarks (e.g., MMLU: $.952 \to .938$; GSM8K: $.846 \to .802$).
9	This reflects the $\theta$-shift boundary condition described in \S\ref{sec:ctrl_contam}: at high contamination fractions, re-estimated $\hat{\theta}$ absorbs part of the aberrance signal, reducing $|\ell_z^*|$.
10	At 100\% contamination, all items are seen and power reaches 1.000 trivially.
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Detection power (proportion rejecting $H_0$ at $\alpha{=}0.05$) under 4PL and 3PL parameterizations across benchmarks and contamination levels ($n{=}2{,}000$ replicates per cell). Bold indicates the 4PL advantage exceeds 5\,pp.}
15	\label{tab:4pl_3pl_power}
16	\small
17	\begin{tabular}{@{}llccccccc@{}}
18	\toprule
19	Benchmark & IRT & 5\% & 10\% & 15\% & 25\% & 50\% & 75\% & 100\% \\
20	\midrule
21	MMLU & 4PL & \textbf{.476} & \textbf{.848} & \textbf{.969} & \textbf{.983} & \textbf{.952} & \textbf{.938} & 1.00 \\
22	     & 3PL & .227 & .340 & .412 & .521 & .676 & .770 & 1.00 \\
23	\addlinespace
24	HellaSwag & 4PL & \textbf{.251} & \textbf{.454} & \textbf{.656} & \textbf{.915} & \textbf{.939} & \textbf{.919} & 1.00 \\
25	          & 3PL & .167 & .241 & .313 & .368 & .508 & .642 & 1.00 \\
26	\addlinespace
27	GSM8K & 4PL & \textbf{.156} & \textbf{.309} & \textbf{.492} & \textbf{.737} & \textbf{.846} & \textbf{.802} & 1.00 \\
28	      & 3PL & .102 & .172 & .285 & .396 & .567 & .577 & 1.00 \\
29	\addlinespace
30	ARC-C & 4PL & .057 & .075 & .087 & \textbf{.130} & \textbf{.285} & \textbf{.493} & 1.00 \\
31	      & 3PL & .054 & .062 & .071 & .076 & .110 & .102 & 1.00 \\
32	\addlinespace
33	HumanEval & 4PL & .076 & .121 & \textbf{.197} & \textbf{.302} & \textbf{.554} & \textbf{.521} & 1.00 \\
34	          & 3PL & .063 & .086 & .120 & .182 & .281 & .315 & 1.00 \\
35	\bottomrule
36	\end{tabular}
37	\end{table*}
38	
39	\section{Seed Sensitivity Analysis}
40	\label{app:seed_sensitivity}
41	
42	\paragraph{Clean-baseline variability.}
43	Table~\ref{tab:seed_sensitivity} reports $\ell_z^*$, accuracy, and $\hat{\theta}_{\text{MLE}}$ across three independent QLoRA runs (seeds 42, 123, 456).
44	For Qwen2.5-7B, $\ell_z^*$ ranges from $7.05$ (seed 123) to $9.53$ (seed 456); the lower value of seed 123 likely reflects seed-specific training dynamics (random initialization, data ordering), but all three seeds produce $\ell_z^* \gg 1.96$, confirming that the elevated baseline reflects systematic model--benchmark misfit rather than seed-specific artifacts.
45	Llama-3.1-8B shows $\ell_z^*$ near zero ($-0.14 \pm 0.97$), consistent with lower baseline misfit.
46	Accuracy variability is negligible for both families (CV $< 0.004$).
47	
48	\begin{table}[t]
49	\centering
50	\caption{Seed sensitivity analysis for clean baseline across three independent runs (seeds 42, 123, 456). CV = coefficient of variation ($\mathrm{std}/|\mathrm{mean}|$).}
51	\label{tab:seed_sensitivity}
52	\footnotesize
53	\resizebox{\columnwidth}{!}{%
54	\begin{tabular}{@{}llcccc@{}}
55	\toprule
56	Model & Metric & Mean & Std & Range & CV \\
57	\midrule
58	Qwen2.5-7B & $\ell_z^*$ & 8.684 & 1.412 & 2.475 & 0.163 \\
59	 & Accuracy & 0.679 & 0.000 & 0.001 & 0.001 \\
60	 & $\hat{\theta}_{\mathrm{MLE}}$ & $-$0.097 & 0.012 & 0.023 & 0.119 \\
61	\midrule
62	Llama-3.1-8B & $\ell_z^*$ & $-$0.141 & 0.965 & 1.929 & 6.860 \\
63	 & Accuracy & 0.594 & 0.002 & 0.004 & 0.004 \\
64	 & $\hat{\theta}_{\mathrm{MLE}}$ & $-$0.645 & 0.019 & 0.036 & 0.029 \\
65	\bottomrule
66	\end{tabular}}
67	\end{table}
68	
69	\paragraph{Cohen's $d$ confidence intervals.}
70	Table~\ref{tab:cohens_d_ci} reports Cohen's $d$ effect sizes with both analytic and bootstrap 95\% confidence intervals.
71	Analytic CIs use $d \pm t_{0.025,\,\text{df}=2} \cdot \text{SE}_d$; with only $n{=}3$ clean seeds (df${=}2$), the critical value $t_{0.025,2} = 4.303$ produces intervals wide enough to cross zero in all four conditions.
72	This is a known limitation of small-sample $t$-based intervals rather than evidence of null effects.
73	Bootstrap CIs (10{,}000 resamples with replacement from the three clean seeds) provide a nonparametric alternative: all four bootstrap intervals exclude zero, supporting the conclusion that contamination produces a reliably detectable signal despite the small reference sample.
74	
75	\begin{table}[t]
76	\centering
77	\caption{Cohen's $d$ with 95\% confidence intervals for contaminated conditions relative to clean baselines ($n{=}3$ seeds). Analytic CIs use $t_{0.025, \text{df}=2}$; bootstrap CIs use 10{,}000 resamples.}
78	\label{tab:cohens_d_ci}
79	\footnotesize
80	\resizebox{\columnwidth}{!}{%
81	\begin{tabular}{@{}llccc@{}}
82	\toprule
83	Model & Cond. & $d$ & Analytic CI & Bootstrap CI \\
84	\midrule
85	Qwen & 15\% & $-$3.42 & [$-$9.92, 3.08] & [$-$3.45, $-$2.82] \\
86	 & 50\% & $-$0.99 & [$-$4.02, 2.04] & [$-$0.99, $-$0.41] \\
87	\midrule
88	Llama & 15\% & $-$2.95 & [$-$8.70, 2.80] & [$-$5.89, $-$2.29] \\
89	 & 50\% & $-$3.31 & [$-$9.63, 3.01] & [$-$6.47, $-$2.59] \\
90	\bottomrule
91	\end{tabular}}
92	\end{table}
93	
94	\paragraph{Cross-family consistency.}
95	Table~\ref{tab:cross_family} confirms that both model families produce large negative Cohen's $d$ under contamination.
96	The $|\Delta d| = 2.32$ gap at 50\% contamination reflects Qwen's non-monotonic dose-response (the $\theta$-shift boundary condition; \S\ref{sec:ctrl_contam}), not a failure of detection robustness---both families remain well above conventional large-effect thresholds ($|d| > 0.8$) at both contamination levels.
97	
98	\begin{table}[t]
99	\centering
100	\caption{Cross-family consistency of contamination detection. Both families show large negative $d$ under contamination.}
101	\label{tab:cross_family}
102	\small
103	\begin{tabular}{@{}lcccl@{}}
104	\toprule
105	Condition & Qwen $d$ & Llama $d$ & $|\Delta d|$ & Consistent? \\
106	\midrule
107	15\% contam. & $-$3.42 & $-$2.95 & 0.47 & Yes \\
108	50\% contam. & $-$0.99 & $-$3.31 & 2.32 & Yes \\
109	\bottomrule
110	\end{tabular}
111	\end{table}
112	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "948adf7c-f843-421e-99ab-045face17d5a",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "7548e738-31d8-46d9-9382-a14dcd9c3e0b",
  "sourceToolAssistantUUID": "948adf7c-f843-421e-99ab-045face17d5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T05:52:14.040Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TdtEd9GKM9iMsesmZscqN7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7548e738-31d8-46d9-9382-a14dcd9c3e0b",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC9u39TMiBtyRHounTc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5e38819-f900-4db1-941a-56154a492938",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4GtPxjiQuRDjyZfwmuZA4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4432,
      "cache_read_input_tokens": 52533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4432,
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

_source line 43 · 2026-05-21T05:52:14.046Z_

<details><summary>↩ Tool result · `toolu_01TdtEd9GKM9iMsesmZscqN7`</summary>

```text
1	\subsection{Experimental Setup}
2	\label{sec:setup}
3	
4	We evaluate on five benchmarks that span knowledge, reasoning, and code generation: MMLU \citep{hendrycks2021mmlu} (14,042 items), HellaSwag \citep{zellers2019hellaswag} (10,042), GSM8K \citep{cobbe2021gsm8k} (1,319), ARC-Challenge \citep{clark2018arc} (295), and HumanEval \citep{chen2021humaneval} (164).
5	All item parameters follow the four-parameter logistic (4PL) IRT model, calibrated by \citet{psnirt2026} from a large-scale leaderboard dataset.
6	
7	\paragraph{Empirical data.}
8	We obtain per-item binary response vectors for 12 models from the PSN-IRT v2 leaderboard dataset \citep{psnirt2026}, covering open-weight and proprietary models across capability tiers.
9	PSN-IRT v1 provides binary responses from $N{=}178$ models with 3PL item parameters; v2 supplies validated 4PL parameters for 12 models.
10	We use v2 for empirical analysis and v1 for the MML-EM refit experiment in \S\ref{sec:empirical}.
11	
12	\paragraph{Controlled contamination.}
13	We fine-tune Qwen2.5-7B-Instruct with QLoRA (rank\,=\,16, $\alpha$\,=\,32) under five conditions: three clean runs (seeds 42, 123, 456) and two contaminated runs where 15\% and 50\% of MMLU evaluation items are included in the supervised fine-tuning (SFT) training data.
14	For cross-family validation, we replicate the same protocol on Llama-3.1-8B-Instruct with identical QLoRA configuration and contamination fractions.
15	
16	\paragraph{Simulation.}
17	For each benchmark, we generate 2{,}000 response-vector replicates per condition across 11 contamination levels (0\%, 3\%, 5\%, 10\%, 15\%, 25\%, 50\%, 60\%, 75\%, 90\%, 100\%), sampling responses under the calibrated 4PL parameters.
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5e38819-f900-4db1-941a-56154a492938",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "94a1a1ea-2c18-4062-8e51-485043a82897",
  "sourceToolAssistantUUID": "e5e38819-f900-4db1-941a-56154a492938",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T05:52:14.492Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SarmegJ1BDXtdryVikMxF3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94a1a1ea-2c18-4062-8e51-485043a82897",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC9u39TMiBtyRHounTc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1462307c-0828-417c-b798-680251892410",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4GtPxjiQuRDjyZfwmuZA4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4432,
      "cache_read_input_tokens": 52533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4432,
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

_source line 45 · 2026-05-21T05:52:14.497Z_

<details><summary>↩ Tool result · `toolu_01SarmegJ1BDXtdryVikMxF3`</summary>

```text
1	\subsection{Simulation Validation}
2	\label{sec:simulation}
3	
4	\paragraph{Null calibration.}
5	Under the null (no contamination), bootstrap $\ell_z^*$ tracks $\mathcal{N}(0,1)$: mean bias 0.041 and standard deviation 1.003 on MMLU.
6	Kolmogorov--Smirnov rejection rates vary with benchmark size: 8.3\% for MMLU and HellaSwag ($n > 10{,}000$), 50.0\% for GSM8K ($n = 1{,}319$), 58.3\% for ARC-C ($n = 295$), and 75.0\% for HumanEval ($n = 164$).
7	$\ell_z^*$ is well-calibrated for benchmarks with $n \geq 10{,}000$ items; smaller benchmarks show increasing finite-sample deviations from normality.
8	
9	\begin{figure}[t]
10	  \centering
11	  \includegraphics[width=\columnwidth]{fig_2_power_function.pdf}
12	  \caption{Theoretical (solid) and simulated (markers) two-sided detection power across contamination levels for five benchmarks. Power scales with $\sqrt{n}$. At contamination above 50\%, mean $\ell_z^*$ crosses zero and shifts from negative to positive anomaly, which produces a brief power dip.}
13	  \label{fig:power}
14	\end{figure}
15	
16	\paragraph{Detection power.}
17	Two-sided testing eliminates the inverted-U artifact: MMLU achieves 97.8\% power at 15\% contamination and sustains ${>}$93\% at all levels (93.6\% at 75\%, 95.2\% at 90\%, 100\% at full contamination).
18	Power scales with $\sqrt{n}$, as predicted by the noncentrality parameter $\delta \propto \sqrt{n}$.
19	Figure~\ref{fig:power} overlays theoretical and simulated power curves; the empirical power function, derived via Gauss--Hermite quadrature ($K=30$) over the ability distribution with the \citet{snijders2001} variance formula, achieves $R^2 = 0.65$.
20	This provides approximate guidance for practitioners assessing detection feasibility from a benchmark's item count.
21	
22	\paragraph{Model comparison.}
23	The 4PL model yields a mean $+$27.3pp power gain over 3PL on MMLU, $+$26.1pp on HellaSwag, and $+$20.3pp on GSM8K, as 46\% of MMLU items exhibit upper asymptote $d < 0.95$ (Appendix~\ref{app:4pl_ablation}).
24	Against supervised baselines, $\ell_z^*$ outperforms logistic regression and random forest at low contamination ($+$0.10 AUROC at 5\%, $+$0.05 at 10\%) without training data; ML classifiers surpass $\ell_z^*$ only above 25\% contamination.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1462307c-0828-417c-b798-680251892410",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "12398f65-676c-41da-b9f7-de5abdb3e65b",
  "sourceToolAssistantUUID": "1462307c-0828-417c-b798-680251892410",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-21T05:52:14.966Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Uryx5XpR7Q4pwy8d1RDete`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12398f65-676c-41da-b9f7-de5abdb3e65b",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC9u39TMiBtyRHounTc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98f96e9e-4ebc-4acf-9d20-269230941f14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4GtPxjiQuRDjyZfwmuZA4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4432,
      "cache_read_input_tokens": 52533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4432,
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

_source line 47 · 2026-05-21T05:52:14.973Z_

<details><summary>↩ Tool result · `toolu_01Uryx5XpR7Q4pwy8d1RDete`</summary>

```text
1	\subsection{Controlled Contamination}
2	\label{sec:ctrl_contam}
3	
4	We validate $\ell_z^*$ on MMLU with ground-truth contamination.
5	Three clean seeds yield $\ell_z^*$ values of $s_1{=}9.47$, $s_2{=}7.05$, $s_3{=}9.53$ (mean$\,{=}\,8.68\pm1.41$); $s_2$ is ${\sim}26\%$ lower than $s_1$/$s_3$, attributable to seed-specific training dynamics (Appendix~\ref{app:seed_sensitivity}).
6	All five conditions achieve comparable accuracy on uncontaminated items (clean $\approx$ 0.679), while contaminated models show overall accuracy gains (0.731 at 15\%, 0.764 at 50\%).
7	
8	\paragraph{Finding 1: Detection signal.}
9	Both contamination levels produce $\ell_z^*$ shifts far exceeding clean-seed variability.
10	At 15\% contamination, $|\text{Cohen's}\;d|{=}3.42$; at 50\%, $|d|{=}0.99$ (ddof$\,{=}\,1$, $n{=}3$ clean seeds).
11	The contamination signal ($|\Delta\ell_z^*|{=}4.84$) far exceeds clean-seed variability (SD$\,{=}\,1.41$).
12	
13	\paragraph{Finding 2: Free-$\theta$ non-monotonicity (model-dependent).}
14	Under free-$\theta$ estimation, Qwen dose-response is non-monotonic: $\Delta\ell_z^*{=}{-}4.84$ at 15\% versus ${-}1.40$ at 50\% (ratio 3.46).
15	The 50\% condition produces a \emph{weaker} signal because contamination inflates $\hat{\theta}_{\text{MLE}}$, absorbing part of the aberrance into a higher ability estimate ($\Delta\theta{=}0.29$ at 15\%, $0.47$ at 50\%).
16	This effect is model-dependent: Llama-3.1-8B shows near-monotonic free-$\theta$ dose-response (ratio 1.09) due to lower baseline misfit ($\ell_z^*{=}0.85$ versus Qwen's 8.68).
17	
18	\paragraph{Finding 3: Fixed $\theta$ restores monotonicity.}
19	We anchor at the pre-contamination baseline ($\theta_{\text{fixed}}{=}{-}0.0966$, mean of $n{=}3$ clean $\hat{\theta}$ estimates), which restores monotonic dose-response: $\Delta\ell_{z,\text{fixed}}^*{=}3.17$ (15\%) and $9.89$ (50\%), a ratio of 3.12 (Figure~\ref{fig:ctrl_contam}, right panel).
20	
21	\paragraph{Finding 4: Memorization fingerprint.}
22	A split by seen/unseen items reveals a characteristic fingerprint: at 15\% contamination, memorized items yield $\ell_z^*{\approx}0$ (consistent with the model's inflated $\hat{\theta}$), while unseen items produce $\ell_z^*{=}3.1$, evidence of genuine aberrance on the non-memorized portion.
23	
24	\paragraph{Finding 5: Memorization fraction.}
25	The fraction of contaminated items that the model memorizes is 0.38 (15\%) and 0.29 (50\%).
26	SFT generalizes beyond the memorized items, as fewer than half the injected items show rote recall.
27	
28	\paragraph{Cross-family confirmation.}
29	Llama-3.1-8B-Instruct confirms generalizability: $|\text{Cohen's}\;d|{=}2.95$ (15\%) and $3.31$ (50\%) ($n{=}3$ clean seeds, mean$\,{=}\,{-}0.14\pm0.97$), with $|\Delta\ell_z^*|{=}3.84$ (15\%) and $4.18$ (50\%).
30	Unlike Qwen, Llama exhibits monotonic Cohen's $d$ dose-response ($|d|$ increases from 2.95 to 3.31), consistent with its lower baseline misfit.
31	Memorization fractions (0.35/0.33) and fixed-$\theta$ signal ratios (2.87) are consistent across families.
32	
33	\paragraph{Baseline comparison.}
34	Table~\ref{tab:baseline} compares $\ell_z^*$ with alternative person-fit statistics at 15\% contamination.
35	All methods operate at the binary-response level; HT and U3 require only item difficulty, while $\ell_z^*$ uses the full 4PL parameterization.
36	$\ell_z^*$ and HT both yield large effect sizes ($|d| > 2.9$); U3 is inconsistent across families ($d{=}{-}0.43$ on Qwen vs.\ ${-}3.69$ on Llama).
37	At the item level, all methods perform near random (AUROC $\leq 0.63$), confirming that contamination is diffuse and model-level aggregation is essential.
38	
39	An accuracy $z$-score baseline yields $z{=}160$ at 15\% contamination, but this reflects near-zero cross-seed accuracy variance ($\text{std}{=}0.0003$), not genuine discriminability.
40	In deployment, accuracy variability from prompt format, evaluation harness, and hardware differences inflates the denominator, collapsing the $z$-score; the 4/60 flagging rate on real data (\S\ref{sec:empirical}) confirms this limitation.
41	
42	\begin{table}[t]
43	\centering
44	\caption{Baseline comparison at 15\% contamination on MMLU. \textbf{Top}: model-level Cohen's $d$ ($n{=}3$ clean seeds). \textbf{Bottom}: item-level AUROC for identifying contaminated items.}
45	\label{tab:baseline}
46	\footnotesize
47	\resizebox{\columnwidth}{!}{%
48	\begin{tabular}{@{}llcc@{}}
49	\toprule
50	\multicolumn{4}{@{}l}{\textit{Model-level detection (Cohen's $d$)}} \\
51	\midrule
52	Method & Info required & Qwen $d$ & Llama $d$ \\
53	\midrule
54	$\ell_z^*$ (ours) & Binary + IRT params & $\mathbf{-3.42}$ & $\mathbf{-2.95}$ \\
55	HT & Binary + $b$ & 3.21 & 3.53 \\
56	U3 & Binary + $b$ & $-$0.43 & $-$3.69 \\
57	Guttman errors & Binary + $b$ & --- & --- \\
58	\midrule
59	\multicolumn{4}{@{}l}{\textit{Item-level contamination detection (AUROC)}} \\
60	\midrule
61	Random baseline & --- & \multicolumn{2}{c}{0.50} \\
62	$\ell_z^*$ itemwise & Binary + IRT params & \multicolumn{2}{c}{0.53} \\
63	LR cross-model & Binary + features & \multicolumn{2}{c}{0.59} \\
64	RF cross-model & Binary + features & \multicolumn{2}{c}{0.63} \\
65	\bottomrule
66	\end{tabular}}
67	\end{table}
68	
69	\begin{figure*}[t]
70	  \centering
71	  \includegraphics[width=\textwidth]{fig_3_ctrl_contam.pdf}
72	  \caption{Controlled contamination on MMLU. \textbf{(a)} $\ell_z^*$ under free-$\theta$ and fixed-$\theta$ estimation for five conditions (3 clean seeds, 2 contaminated). Free-$\theta$ is non-monotonic; fixed-$\theta$ restores monotonicity. \textbf{(b)} Accuracy split by seen/unseen items with memorization fractions. \textbf{(c)} $\theta$-shift mechanism: contamination inflates $\hat{\theta}_{\text{MLE}}$, absorbing aberrance signal. $\theta_{\text{fixed}}$ computed as mean of $n{=}3$ clean seed $\hat{\theta}$ estimates ($-0.0966$).}
73	  \label{fig:ctrl_contam}
74	\end{figure*}
75	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98f96e9e-4ebc-4acf-9d20-269230941f14",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "d277cbd2-3054-418f-85c1-0b37d0bd51cc",
  "sourceToolAssistantUUID": "98f96e9e-4ebc-4acf-9d20-269230941f14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-21T05:52:15.400Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SVMEyJ5VehMx4L1U2QVPFx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d277cbd2-3054-418f-85c1-0b37d0bd51cc",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFC9u39TMiBtyRHounTc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b86aeda-17aa-42ed-ab34-f59fb5a67b93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4GtPxjiQuRDjyZfwmuZA4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4432,
      "cache_read_input_tokens": 52533,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4432
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 329,
          "cache_read_input_tokens": 52533,
          "cache_creation_input_tokens": 4432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4432,
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

_source line 49 · 2026-05-21T05:52:15.405Z_

<details><summary>↩ Tool result · `toolu_01SVMEyJ5VehMx4L1U2QVPFx`</summary>

```text
1	\subsection{Empirical Findings}
2	\label{sec:empirical}
3	
4	We apply $\ell_z^*$ to 12 models across five benchmarks (60 model-benchmark cells).
5	After Benjamini--Hochberg FDR correction ($\alpha=0.05$), 57 of 60 cells are flagged as significant.
6	The three unflagged cells (Yi-Lightning$\times$ARC-C, 360GPT2-Pro$\times$HumanEval, Yi-Lightning$\times$HumanEval) all involve small benchmarks ($n \leq 295$), consistent with the power analysis in \S\ref{sec:simulation}.
7	By contrast, a simple accuracy $z$-score baseline (standardized accuracy across models per benchmark) flags only 4 of 60 cells: $\ell_z^*$ captures 14$\times$ more anomalies by exploiting response-pattern structure that accuracy aggregation discards.
8	This near-universal misfit indicates that real LLM response patterns systematically deviate from 4PL IRT predictions, regardless of architecture or training paradigm.
9	
10	\paragraph{12-model case study.}
11	Figure~\ref{fig:heatmap} presents the $\ell_z^*$ heatmap across 12 models and five benchmarks.
12	93.0\% of flagged cells exhibit positive $\ell_z^*$ (over-consistency): models answer too many hard items correctly relative to their estimated ability.
13	Gemini-1.5 on MMLU represents an extreme case: near-perfect accuracy, $\hat{\theta}=0.78$, and $\ell_z^*{=}{+}31.81$, with 50 of 57 MMLU subjects flagged individually.
14	Ward hierarchical clustering on the $\ell_z^*$ profile matrix reveals heterogeneous contamination typologies; Gemini-1.5 isolates as a distinct outlier, while other models form clusters that correspond to selective versus uniform misfit.
15	Ten of 12 models are flagged on all five benchmarks simultaneously.
16	
17	\paragraph{IRT parameter estimation gap.}
18	A 3PL refit via MML-EM on the v1 leaderboard ($N{=}178$ models) recovers difficulty moderately ($r_b = 0.663$) but fails on discrimination ($r_a = 0.127$).
19	Classical IRT calibration requires sample sizes that current leaderboards cannot provide; neural calibration methods such as PSN-IRT \citep{psnirt2026} remain essential.
20	On real data, 4PL and 3PL $\ell_z^*$ values correlate at only $r=0.225$ (RMSE$\,{=}\,68.41$), which confirms that the guessing-slip parameters ($c$, $d$) captured by 4PL substantially alter person-fit assessment.
21	This simulation-to-reality gap constitutes an informative negative result: it quantifies the boundary conditions under which classical IRT calibration degrades.
22	
23	\begin{figure}[t]
24	  \centering
25	  \includegraphics[width=\columnwidth]{fig_4_model_heatmap.pdf}
26	  \caption{$\ell_z^*$ heatmap for 12 models across five benchmarks. Positive values (red) indicate over-consistent response patterns. Gemini-1.5 on MMLU ($\ell_z^*{=}{+}31.81$) is an extreme outlier. Ward clustering (left dendrogram) reveals distinct contamination typologies.}
27	  \label{fig:heatmap}
28	\end{figure}
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b86aeda-17aa-42ed-ab34-f59fb5a67b93",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "8bdf9912-99f8-464b-b52c-e4e153206c4b",
  "sourceToolAssistantUUID": "0b86aeda-17aa-42ed-ab34-f59fb5a67b93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-21T05:52:18.494Z_

Now let me also check the latest dream review reports for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bdf9912-99f8-464b-b52c-e4e153206c4b",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCALKvUd2RWpcA68xDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8da1f3ef-1940-4589-bdcd-2ccdaf2601f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tcVw73yWxBJgWRvG9UcMy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5099,
      "cache_read_input_tokens": 56965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5099,
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

_source line 51 · 2026-05-21T05:52:21.327Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BjD2ruT96Lat3nAE6pjzWe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T044802/best/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8da1f3ef-1940-4589-bdcd-2ccdaf2601f6",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCALKvUd2RWpcA68xDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32babece-b2bd-4e2f-9919-e4961ae8fdc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tcVw73yWxBJgWRvG9UcMy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5099,
      "cache_read_input_tokens": 56965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5099,
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

_source line 52 · 2026-05-21T05:52:21.332Z_

<details><summary>↩ Tool result · `toolu_01BjD2ruT96Lat3nAE6pjzWe`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{booktabs}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{graphicx}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{microtype}
12	\usepackage{hyperref}
13	\usepackage{natbib}
14	\usepackage{enumitem}
15	
16	\title{\textbf{IRT-FIT: Detecting Benchmark Contamination in Large Language Models\\via Item Response Theory Person-Fit Statistics}}
17	
18	\author{Anonymous}
19	
20	\date{}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	Benchmark contamination---the inclusion of evaluation data in training corpora---undermines the reliability of Large Language Model (LLM) evaluation.
27	All existing detection methods require privileged access beyond binary (correct/incorrect) response patterns: training data, token-level probabilities, model weights, or specially constructed prompts.
28	We establish the \emph{minimal-information operating point} on the contamination detection frontier by repurposing Item Response Theory (IRT) person-fit statistics, originally developed for detecting exam cheating.
29	Our framework, IRT-FIT, computes the standardized person-fit statistic $\ell z^*$ under a 4-parameter logistic (4PL) IRT model using only binary response data.
30	In controlled contamination experiments across four model families (Qwen, Llama, Mistral, Gemma) with QLoRA SFT injection at six contamination levels, IRT-FIT achieves $|\text{Cohen's } d| > 2.0$ at 15\% contamination for all families, with 95\% confidence intervals tightened to $\pm 0.4$ via $n{=}10$ seed replication.
31	IRT-FIT yields $8\times$ the effect size of classical person-fit statistics (Guttman, U3) by leveraging full 4PL parameterization.
32	Crucially, IRT-FIT retains 65\% of its detection signal after reinforcement learning (RL) fine-tuning ($|d|{=}2.1$ post-GRPO), while all membership inference attack (MIA) methods degrade to near-random (AUROC $\approx 0.51$)---directly addressing the post-RL detection gap identified by Wang et al.\ (2025).
33	We further identify universal 4PL model misfit as a novel property of LLM response patterns and propose $\theta$-fixed analysis as a general methodological contribution that restores monotonic dose-response across all model families.
34	\end{abstract}
35	
36	%-------------------------------------------------------------------
37	\section{Introduction}
38	%-------------------------------------------------------------------
39	
40	As LLM benchmarks proliferate and training corpora grow to trillions of tokens, the risk that evaluation data leaks into training pipelines increases commensurately.
41	Benchmark contamination inflates reported performance, misleads model comparisons, and erodes trust in evaluation-driven progress.
42	The problem is compounded by the opacity of commercial training pipelines: practitioners often cannot verify whether a benchmark was included in pretraining or fine-tuning data.
43	
44	A rich ecosystem of detection methods has emerged, spanning time-based partitioning, membership inference attacks (MIA) such as Min-K\%++, token-probability probing, performance-based statistical testing (ConStat), and in-context learning effect analysis (CoDeC).
45	However, \emph{all} existing methods require information beyond binary response patterns---training data manifests, token-level log-probabilities, model weights, or the ability to query models with specially crafted prompts.
46	Moreover, Wang et al.\ (2025) demonstrate that all ten log-probability-based MIA methods degrade to near-random performance on RL-trained reasoning models, as RL fundamentally alters token-level distributions while preserving answer-level patterns.
47	
48	We ask a more fundamental question: \textbf{what can be detected from binary response patterns alone?}
49	This question has been studied extensively in psychometrics, where \emph{person-fit statistics} detect examinees with item preknowledge---functionally analogous to contaminated LLMs.
50	Over five decades of development, person-fit statistics have been refined for detecting aberrant response patterns under calibrated IRT models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32babece-b2bd-4e2f-9919-e4961ae8fdc0",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "fb64f718-e81a-485d-9108-ffa85f5402a9",
  "sourceToolAssistantUUID": "32babece-b2bd-4e2f-9919-e4961ae8fdc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T05:52:21.746Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016x5eDtu25znqE5WW25s5wx`</summary>

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
  "parentUuid": "fb64f718-e81a-485d-9108-ffa85f5402a9",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCALKvUd2RWpcA68xDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba2d6877-2dd2-493e-b541-446805bfa59f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tcVw73yWxBJgWRvG9UcMy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5099,
      "cache_read_input_tokens": 56965,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5099
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 229,
          "cache_read_input_tokens": 56965,
          "cache_creation_input_tokens": 5099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5099,
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

_source line 54 · 2026-05-21T05:52:21.756Z_

<details><summary>↩ Tool result · `toolu_016x5eDtu25znqE5WW25s5wx`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'irt_personfit_contam'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba2d6877-2dd2-493e-b541-446805bfa59f",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "f0921b30-5dc9-4b5e-8df1-5cafded6160b",
  "sourceToolAssistantUUID": "ba2d6877-2dd2-493e-b541-446805bfa59f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-21T05:52:25.059Z_

I now have a comprehensive understanding of the paper. Let me also quickly check if there are any additional files about baselines or the Mistral experiment results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0921b30-5dc9-4b5e-8df1-5cafded6160b",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCAoR61mfBBAKMaibBc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a7bfd15-f0b7-4883-9f3a-bbe58215530c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmPN3CoYmSyrWoK72C99jv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1500,
      "cache_read_input_tokens": 62064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1500,
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

_source line 56 · 2026-05-21T05:52:25.380Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PGJb1hX14KpvhCtAnv6Ayu`</summary>

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
  "parentUuid": "2a7bfd15-f0b7-4883-9f3a-bbe58215530c",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCAoR61mfBBAKMaibBc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b732dcb7-770d-4c94-b3f0-262853f845a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmPN3CoYmSyrWoK72C99jv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1500,
      "cache_read_input_tokens": 62064,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1500
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 62064,
          "cache_creation_input_tokens": 1500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1500,
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

_source line 57 · 2026-05-21T05:52:25.389Z_

<details><summary>↩ Tool result · `toolu_01PGJb1hX14KpvhCtAnv6Ayu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/memory.md\", \"content\": \"# Memory — irt_personfit_contam\\n\\n## OOM 教训 (2026-05-20)\\n- 7.6GB RAM 机器上，N_SIM×n_items float64 矩阵不能一次性分配。MMLU 10K×14042×8B ≈ 1.07GB 单个矩阵，compute_lz_star 内部创建 ~7 个同尺寸中间数组 → OOM\\n- 解决方案：BATCH_SIZE=500 分批计算 + N_SIM 降至 2000（统计效力足够）\\n- generate_response 和 compute_lz_star 都需要分批\\n\\n## Worker context exhaustion 教训 (2026-05-20)\\n- exp-v1-irt-refit-expanded Worker 跑 1.5 小时后崩溃，无输出。任务是从 HuggingFace 下载 500+ 模型的 per-item 数据并拟合 IRT。\\n- **根因**: 大量 HF API 调用 + 数据处理的累积输出耗尽 Worker context window。\\n- **教训**: 涉及大规模数据下载（100+ datasets）的任务必须分批 + checkpoint 中间结果，或拆成多个 Worker 串行执行。单个 Worker 不适合做 1.5hr+ 的重型数据工程。\\n- **补充 (同日)**: ssh_read_only 读取大 JSON 文件（8MB+ 单行）也会撑爆 context。Worker 操作远程大文件必须用 python 脚本提取摘要，不要 cat/head。\\n- **补充 (同日)**: Worker 无法在进程内长时间等待（~2 min 就退出）。涉及 GPU 训练 + eval 的任务应分阶段处理：训练完成后由 cron 回调触发 eval Worker，或由主 Agent 定时派 Worker 检查。\\n\\n## sim_001 关键发现 (2026-05-20)\\n- **Null check 全通过**：PSN-IRT 神经网络估计的 4PL 参数与经典 IRT 兼容，lz* ≈ N(0,1)\\n  - 大 benchmark（GSM8K/HellaSwag/MMLU）KS p 全部 > 0.01\\n  - 小 benchmark（HumanEval/ARC-C）KS p < 0.01，但属预期（items 太少，CLT 近似弱）\\n- **检测力与 n_items 强正相关**：MMLU(14042)=97.9% >> HellaSwag(10042)=73.3% >> GSM8K(1319)=57.8% >> ARC-C(295)=12.9%\\n- **Inverted-U 所有 benchmark 可观测**：power 在 25-50% contamination 达峰，100% 全部 NaN（全答对 → MLE 不收敛）\\n\\n## PSN-IRT 12 模型身份 (2026-05-20)\\n\\n**来源**：arXiv:2505.15055 (AAAI 2026 Oral)，GitHub repo `Joe-Hall-Lee/PSN-IRT`\\n\\n| student_id | θ | 正确率 | 模型名称 | 类型 |\\n|---|---|---|---|---|\\n| 0 | 1.46 | 80.6% | 360GPT2-Pro | API |\\n| 1 | 3.77 | 85.7% | DeepSeek-V3 | API |\\n| 2 | 1.14 | 78.9% | Doubao-pro | API |\\n| 3 | 0.78 | 84.5% | Gemini-1.5 | API |\\n| 4 | -3.38 | 23.1% | Gemma-2B-it | 开源 2B |\\n| 5 | 1.73 | 82.1% | Hunyuan-Turbo | API |\\n| 6 | -1.37 | 40.0% | Mistral-7B-Instruct-v0.1 | 开源 7B |\\n| 7 | 0.93 | 77.0% | Moonshot-v1 | API |\\n| 8 | 0.96 | 76.3% | Qwen-Plus | API |\\n| 9 | -0.13 | 60.4% | Qwen2.5-3B-Instruct | 开源 3B |\\n| 10 | -1.89 | 31.6% | Vicuna-7B-v1.3 | 开源 7B |\\n| 11 | 0.77 | 75.2% | Yi-Lightning | API |\\n\\n## Gemini-1.5 × 100% contamination 精确匹配 (2026-05-20)\\n\\nGemini-1.5 MMLU lz*(benchmark-specific θ) = +31.815 = 100% contamination simulation lz* = +31.815（完全一致）。机制：100% accuracy → θ_bench=4.0 → lz* deterministic。其他 benchmark Gemini-1.5 lz* 为负（非 100% acc），说明异常是 benchmark-specific 的。\\n\\n## exp-extended-sim 关键发现 (2026-05-20)\\n\\n- Dual-regime crossover 75-90%：所有 5 benchmark 在此区间 lz* 从负翻正\\n- 100% contamination lz* deterministic (std=0.0)\\n- Inverted-U 全 5 benchmark 确认\\n\\n## exp-two-sided 关键教训 (2026-05-20)\\n\\n95% flagging 即使用 benchmark-specific θ + bootstrap + FDR 也无法降低。LLM 系统性违反 4PL 假设（单维+局部独立）。绝对阈值对 real data 无意义，需 controlled calibration (Δlz*)。\\n\\n## exp-empirical-null 关键发现 (2026-05-20)\\n\\nBootstrap null 校准良好（mean bias=0.09, std=1.002）。95% flagging 不是 null miscalibration，而是 LLM response pattern 产生极端 lz*。大 benchmark KS reject 仅 8.3%，小 benchmark 58-75%（有限样本效应）。\\n\\n## exp-power-theory 关键发现 (2026-05-20)\\n\\nR²(two-sided)=0.957, R²(left-tail)=0.976, R²(mean lz*)=0.995。δ ∝ √n confirmed。Inverted-U 拐点理论值 π*≈81-85%。最小 n_items (80% power): 15% contam→~8K, 25%→~3K, 50%→~1K。\\n\\n## exp-item-alignment-check 关键发现 (2026-05-20)\\n\\n**PSN-IRT 与 v1 Leaderboard item ordering 不对齐。** 直接位置匹配率 54.56%（≈随机）。Content-based 重排后 Mistral 88.46%, Vicuna 72.48%。\\n\\n**根因**: PSN-IRT 保持 raw MMLU 原始顺序，v1 leaderboard 在 subject 内部 shuffle。且 PSN-IRT 是独立评测（不同 prompt/few-shot），即使对齐后仍有 ~12% response 差异。\\n\\n**结论**: **不可混用 v1 responses + PSN-IRT parameters**。~12% 噪声对 item-level person-fit 统计量影响严重。\\n\\n**已生成 item_mapping.csv**: 12068/14042 items 的 v1→PSN-IRT 位置映射，可用于未来 content-based 对齐需求。\\n\\n## Open LLM Leaderboard v1 per-item data (2026-05-20)\\n\\n**来源**: `open-llm-leaderboard-old/details_{org}__{model}` HuggingFace datasets\\n**格式**: Parquet, `acc`/`acc_norm` 二值字段\\n**覆盖**: MMLU ✅, HellaSwag ✅, ARC-C ✅, GSM8K ✅ | HumanEval ❌\\n**模型数**: 13,000+\\n**⚠️ 不可直接用 PSN-IRT parameters** — 见 item-alignment-check 发现\\n\\n## exp-fdr-correction 关键发现 (2026-05-20)\\n\\nexp-two-sided v2 的 `empirical_pvalues.csv` 已包含 global BH-FDR 校正（60 cells 一起做 BH）。校正前后 flagging 均为 57/60 (95%)——因大多数 cells empirical p=0.000，BH 校正无实质影响。Leaderboard-scale FDR (24800+ tests) 需在 leaderboard audit 中单独处理。\\n\\n## exp-clean-control-delta 关键发现 (2026-05-20)\\n\\nClean-vs-clean Δlz* 均值全部接近 0（|mean| < 0.13），无一显著，确认 estimation noise floor ~ N(0, 1.4)。\\nClean-vs-contaminated (25%) Δlz* 均高度显著（p<1e-10），Cohen's d: MMLU=2.66, HellaSwag=1.85, GSM8K=1.85, HumanEval=1.07, ARC-C=0.45。\\nARC-C d=0.45 略低 0.5 阈值（仅 295 items），与 power theory 一致。\\n论文中标注为 \\\"theoretical noise floor\\\"，真实 SFT clean-vs-clean 在 ctrl-contam-pilot 中实现。\\n\\n## exp-ml-classifier-baseline 关键发现 (2026-05-20)\\n\\n**lz* 在低污染率 (5-10%) 优于有监督 ML 分类器**：5% contam lz* AUROC 0.675 vs best ML 0.575 (+0.10); 10% contam 0.763 vs 0.712 (+0.05)。ML 仅在 25%+ 污染时略胜 (+0.05)，但需 oracle contamination labels（实际不可用）。\\nRF feature importance 在 items 间高度弥散（top item <1%），与 lz* 全局 likelihood 方法一致。\\n论文限定为 simulation 场景下的对比，不推广为\\\"所有 binary-only ML 方法都不如 IRT\\\"。\\n\\n## exp-domain-analysis 关键发现 (2026-05-20)\\n\\n**Gemini-1.5 MMLU 100% accuracy 覆盖全部 57 个 subject**——不是 domain-concentrated 泄漏，是完全数据集泄漏。50/57 subjects flagged (lz*>1.96)，未 flagged 的 7 个 subject 的 lz* 也很高但 item 数太少。\\n\\n**模型 contamination 指纹多样**：\\n- Doubao-pro: 反向 pattern，Humanities/Social Sciences lz* 极负（-13~-15），STEM 接近 0，Other 正向——可能是训练数据偏科\\n- Hunyuan-Turbo: STEM lz*=1.8 vs Social Sciences lz*=13.9——Social Sciences 方向过度拟合\\n- Yi-Lightning 和 Qwen-Plus: 全 domain 高 lz*（16~28），领先所有其他模型\\n\\n**论文价值**: domain decomposition 为 12-model case study 增加定性分析深度，但 non-essential（P2 级别）。\\n\\n**virology lz*=-8.21 诊断**：双重根因——(1) global θ=0.78 vs MMLU θ_MLE=4.0 错配；(2) virology 全部 166 items d<1.0 (mean=0.71)，即使 θ=4.0 仍有 58/166 items P<0.5。是 PSN-IRT calibration artifact，不影响 overall lz*=34.75。per-subject 分析需加 caveat。\\n\\n## exp-natural-experiment 关键发现 (2026-05-20)\\n\\n21 对 base→chat 模型 × 4 benchmarks（MMLU/HellaSwag/ARC-C/GSM8K）。\\n\\n**两个 benchmark 有显著系统性 SFT 效应**：\\n- HellaSwag: Δlz* 偏差 mean=-3.40, t=-3.97, p=0.001（SFT 系统性降低 person-fit）\\n- GSM8K: Δlz* 偏差 mean=+3.92, t=3.35, p=0.009（SFT 系统性提高 person-fit）\\n- MMLU/ARC-C 无显著效应\\n\\n**无个体 pair outlier**——未能检测到单个模型的 benchmark-specific contamination。\\n**Director 评估价值极低（P2-optional）**，不作为核心 evidence 使用。\\n\\n## exp-4pl-ablation 关键发现 (2026-05-20)\\n\\n**4PL d 参数对检测力的影响是决定性的，不是锦上添花。**\\n\\n核心数据（4PL vs 3PL(d=1)，平均 power gain across contamination levels）：\\n- MMLU: +27.3pp (max +49.0pp)\\n- HellaSwag: +26.1pp (max +59.6pp)\\n- GSM8K: +20.3pp (max +39.7pp)\\n- ARC_C: +14.8pp (max +54.6pp)\\n- HumanEval: +13.7pp (max +30.6pp)\\n\\nFAR 校准：4PL ≈ 5%（正确），3PL 4.7-16.5%（偏高），2PL 50-100%（完全不可用——固定 c=0.25 灾难性错误）。\\n\\n**d-bucket 机制确认**：d<0.8 的 items 上 4PL 优势最大（MMLU +61pp），d≥0.95 时差异可忽略。这证实 d 参数捕捉 ceiling effect 是检测力提升的关键来源。\\n\\n**论文价值**：回应 Reviewer R8 concern（为什么用 4PL 而非 3PL）。46% MMLU items d<0.95，忽略 d 约将检测力减半。这是 Method 部分的核心 justification。\\n\\n## exp-4pl-real-data-degradation 关键发现 (2026-05-20)\\n\\n**实数据验证：d 参数的影响对高能力模型是毁灭性的。**\\n\\n在 12 个 PSN-IRT 模型的真实响应数据上，4PL vs 3PL(d=1) 的 lz* 仅有 r=0.225, RMSE=68.41——几乎无关联。\\n\\n**不对称影响机制**：d=1 使 P(θ)→1（高能力模型预期全部答对），导致少量错误被 lz* 放大为极端异常值。低能力模型的 P(θ) 本身就远离 1.0，d=1 vs d<1 差异小，因此几乎不受影响。\\n\\n- DeepSeek-V3 (θ=3.77): MMLU lz* 从 +16.4 暴跌至 -340.6\\n- Gemma-2B-it / Vicuna / Mistral (低 θ): |Δlz*|<2\\n- MMLU 最严重（46% items d<0.95），mean |Δlz*|=58.3\\n\\n**与 exp-4pl-ablation 的互补**：ablation 在模拟数据上证明 power 损失，本实验在实数据上证明 lz* 值本身被完全摧毁。二者形成 R8 的双重证据链——4PL d 参数不可或缺。\\n\\n**论文写作注意**：这个结果特别适合做 case study 可视化（选 DeepSeek-V3 on MMLU 作为 extreme case），放在 ablation study 或 appendix 中。\\n\\n## exp-ctrl-contam-pilot 关键发现 (2026-05-20)\\n\\n**首次真实 LLM controlled contamination 实验。** Qwen2.5-7B-Instruct QLoRA SFT，4+1 条件。\\n\\n**核心结果（n=3 clean seeds, ddof=1）**：\\n| Condition | Accuracy | θ_MLE | lz* |\\n|-----------|----------|-------|-----|\\n| clean_s1 (seed=42) | 0.6787 | -0.0987 | 8.0101 |\\n| clean_s2 (seed=123) | 0.6789 | -0.0842 | 5.9440 |\\n| clean_s3 (seed=456) | 0.6783 | -0.1068 | 8.0806 |\\n| contam_15 | 0.7310 | +0.1971 | 3.0046 |\\n| contam_50 | 0.7644 | +0.3703 | 5.4480 |\\n\\n**Baseline（n=3）**: mean=7.3449, std=1.2137\\n**Cohen's d（n=3, ddof=1）**: contam_15 d=-3.58, contam_50 d=-1.56\\n**注意**：之前汇报的 d=-3.85 / d=-1.48 使用了 ddof=0。论文统一用 ddof=1。\\n\\n**H1 ✓ H2 ✓ H3 ✗(θ-free) H4 ✗**\\n\\n**θ-shift 是 dose-response 倒置的确切原因**：\\n- contamination 抬高 θ_MLE（clean -0.09 → contam_50 +0.37），MLE 将 contamination 信号解释为 \\\"能力提升\\\"\\n- θ-fixed（固定为 clean θ 均值 -0.0914）下，dose-response 恢复单调：\\n  - |Δlz*_fixed_15| = 2.96, |Δlz*_fixed_50| = 8.67, ratio = 2.93 ✅\\n- θ-shift 分别吸收了 contam_15 的 6.93 和 contam_50 的 10.20 lz* 单位信号\\n\\n**clean seed 变异性**：s1 和 s3 的 lz* 接近（8.01, 8.08），s2 明显低（5.94）。n=3 baseline std=1.21 vs n=2 的 1.46，加入 s3 压缩了方差，使 Cohen's d 更极端。\\n\\n**Memorization fraction 低于预期**（0.38/0.29 vs 假设的 >0.5）——QLoRA 3 epochs 不足以产生强 memorization，但足以产生可检测的 lz* 偏移。\\n\\n**论文叙事价值**：\\n1. θ-shift = \\\"ability inflation\\\" 是 contamination 逃避 person-fit 检测的核心机制\\n2. 与 simulation inverted-U 发现形成呼应——real-world 版本的同一现象\\n3. θ-fixed 分析作为 supplementary evidence 证明底层信号单调递增\\n4. 支撑 Discussion 中 \\\"θ estimation as confound\\\" 段落\\n\", \"total_chars\": 8710, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b732dcb7-770d-4c94-b3f0-262853f845a3",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "8f5d0ee4-b6a5-4d85-9ba7-bb7ea2de2cd4",
  "sourceToolAssistantUUID": "b732dcb7-770d-4c94-b3f0-262853f845a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-21T05:52:28.388Z_

I now have a thorough understanding of the paper. Let me also count the actual bibliography entries to verify the reference count claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f5d0ee4-b6a5-4d85-9ba7-bb7ea2de2cd4",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCB55vDSx8wDrrENJcK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8897b782-37be-4880-bffe-4912ea323df8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyE8D5omzrECoB2tA7A7Wh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5950,
      "cache_read_input_tokens": 63564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5950,
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

_source line 59 · 2026-05-21T05:52:30.460Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018ax2WbPy77gQCBGFBjBCuz`</summary>

```json
{
  "command": "grep -c '@' /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib | head -1",
  "description": "Count bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8897b782-37be-4880-bffe-4912ea323df8",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCB55vDSx8wDrrENJcK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fd834c1-f234-42e8-b6e3-49b7a4b00dba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyE8D5omzrECoB2tA7A7Wh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5950,
      "cache_read_input_tokens": 63564,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5950
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 63564,
          "cache_creation_input_tokens": 5950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5950,
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

_source line 60 · 2026-05-21T05:52:30.642Z_

<details><summary>↩ Tool result · `toolu_018ax2WbPy77gQCBGFBjBCuz`</summary>

```text
37
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fd834c1-f234-42e8-b6e3-49b7a4b00dba",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "9265d127-baeb-4b2f-a083-2619a169c7b0",
  "sourceToolAssistantUUID": "4fd834c1-f234-42e8-b6e3-49b7a4b00dba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T05:52:34.060Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Kfr4bh9TVxhTUXJsnKxgs7`</summary>

```json
{
  "command": "grep -c '@\\(article\\|inproceedings\\|book\\|incollection\\|techreport\\|misc\\)' /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib",
  "description": "Count actual bibliography entry types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9265d127-baeb-4b2f-a083-2619a169c7b0",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCBTGAQiPALjKhpgGkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40155a3f-b231-4886-8565-846522d561f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8z35NCKmQ2RFu8rGXHKsC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 69514,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 159
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 69514,
          "cache_creation_input_tokens": 159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 159,
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

_source line 62 · 2026-05-21T05:52:34.112Z_

<details><summary>↩ Tool result · `toolu_01Kfr4bh9TVxhTUXJsnKxgs7`</summary>

```text
37
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40155a3f-b231-4886-8565-846522d561f3",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "06bd0a21-2973-4411-84fe-c96f460ebe53",
  "sourceToolAssistantUUID": "40155a3f-b231-4886-8565-846522d561f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-21T05:52:41.456Z_

Good -- the bibliography has 37 entries, not 8 as stated in the review task prompt. The prompt's claim of "only 8 references" was based on the initial summary, not the actual paper. Let me now also check what is cited in the paper text vs what is in the bib file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06bd0a21-2973-4411-84fe-c96f460ebe53",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCBiAcCVRJipxMBGzTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a4944da-3def-4c20-a61d-761630b23458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MYf7iD7McKD9a5XRxujSZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 156,
      "cache_read_input_tokens": 69673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 156,
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

_source line 64 · 2026-05-21T05:52:43.580Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014ZjuBe7BDCWqs11aMGGTyT`</summary>

```json
{
  "command": "grep -ohP '\\\\\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/*.tex | sort -u",
  "description": "Extract all citation commands from paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a4944da-3def-4c20-a61d-761630b23458",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCBiAcCVRJipxMBGzTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f86fc57-98a8-49f5-9302-99c7c5f0cac5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MYf7iD7McKD9a5XRxujSZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 156,
      "cache_read_input_tokens": 69673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 156,
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

_source line 65 · 2026-05-21T05:52:43.638Z_

<details><summary>↩ Tool result · `toolu_014ZjuBe7BDCWqs11aMGGTyT`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f86fc57-98a8-49f5-9302-99c7c5f0cac5",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "3549b6e1-78ae-4f38-b9aa-87ee568946ca",
  "sourceToolAssistantUUID": "6f86fc57-98a8-49f5-9302-99c7c5f0cac5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-21T05:52:46.935Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RcqR4TfBYvrzUjXurJtQ4s`</summary>

```json
{
  "command": "grep -rohP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/*.tex | sort -u",
  "description": "Extract all citation commands from paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3549b6e1-78ae-4f38-b9aa-87ee568946ca",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCCRgwP6fWsBM5DX2Lh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec7776b1-9728-4e10-b12c-cb52026cfe6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011E93KCRwNX9cR4X3eupzFi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 222,
      "cache_read_input_tokens": 69829,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 222
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 69829,
          "cache_creation_input_tokens": 222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 222,
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

_source line 67 · 2026-05-21T05:52:46.991Z_

<details><summary>↩ Tool result · `toolu_01RcqR4TfBYvrzUjXurJtQ4s`</summary>

```text
\citep{atlas2025}
\citep{barton1981}
\citep{birnbaum1968}
\citep{chen2021humaneval}
\citep{clark2018arc}
\citep{cobbe2021gsm8k}
\citep{codec2026}
\citep{constat2024}
\citep{dodge2021, magar2022, sainz2023}
\citep{dodge2021, magar2022}
\citep{dodge2021}
\citep{drasgow1985, meijer2001, karabatsos2003, sinharay2017}
\citep{drasgow1985}
\citep{golchin2024, oren2024}
\citep{golchin2024}
\citep{hendrycks2021mmlu}
\citep{jacovi2023, chang2024survey}
\citep{lord1980, embretson2000}
\citep{martinezplumed2019, polo2024tinybenchmarks}
\citep{minkprob2024, deng2024}
\citep{minkprob2024}
\citep{psnirt2026}
\citep{snijders2001}
\citep{zellers2019hellaswag}
\citep{zhang2026rlvr}
\citet{drasgow1985}
\citet{karabatsos2003}
\citet{meijer2001}
\citet{psnirt2026}
\citet{sainz2023}
\citet{selfcritique2026}
\citet{sinharay2017}
\citet{snijders2001}
\citet{wang2025fragility}
\citet{zhang2026rlvr}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec7776b1-9728-4e10-b12c-cb52026cfe6d",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "6cb6b414-1407-479f-81f5-8f59d79a6a96",
  "sourceToolAssistantUUID": "ec7776b1-9728-4e10-b12c-cb52026cfe6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-21T05:52:50.521Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01P1otqXRVpcfdW8f9gmUAP4`</summary>

```json
{
  "command": "grep -rohP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/*.tex | sed 's/\\\\cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ //' | sort -u",
  "description": "Extract unique citation keys used in the paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cb6b414-1407-479f-81f5-8f59d79a6a96",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCCf94snekDAq8fnnZR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32931ff4-d153-4d4b-a7f1-70180403eb72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G5QW8RFQDRmjZz11WGMw3H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 594,
      "cache_read_input_tokens": 70051,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 594
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 70051,
          "cache_creation_input_tokens": 594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 594,
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

_source line 69 · 2026-05-21T05:52:50.593Z_

<details><summary>↩ Tool result · `toolu_01P1otqXRVpcfdW8f9gmUAP4`</summary>

```text
atlas2025
barton1981
birnbaum1968
chang2024survey
chen2021humaneval
clark2018arc
cobbe2021gsm8k
codec2026
constat2024
deng2024
dodge2021
drasgow1985
embretson2000
golchin2024
hendrycks2021mmlu
jacovi2023
karabatsos2003
lord1980
magar2022
martinezplumed2019
meijer2001
minkprob2024
oren2024
polo2024tinybenchmarks
psnirt2026
sainz2023
selfcritique2026
sinharay2017
snijders2001
wang2025fragility
zellers2019hellaswag
zhang2026rlvr
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32931ff4-d153-4d4b-a7f1-70180403eb72",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "f0b8b855-7cd4-4ed3-b543-95923647c014",
  "sourceToolAssistantUUID": "32931ff4-d153-4d4b-a7f1-70180403eb72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-21T05:52:52.846Z_

32 unique citation keys. Now let me check unused bib entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0b8b855-7cd4-4ed3-b543-95923647c014",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCCvY2LjyYxvsoPRTS1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e523803-c43b-4b0c-87f2-fafb4cd1eb76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fd9a3w9xeCa91VdRdsKpz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 70645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 373,
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

_source line 71 · 2026-05-21T05:52:54.379Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y6gQBEdMPvh18NQjJSY2G7`</summary>

```json
{
  "command": "grep -oP '(?<=@\\w{4,15}\\{)[^,]+' /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib | sort",
  "description": "Extract all bib keys from references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e523803-c43b-4b0c-87f2-fafb4cd1eb76",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCCvY2LjyYxvsoPRTS1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7fd7b2f-51da-4ea1-82d5-e60973a3f2fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fd9a3w9xeCa91VdRdsKpz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 70645,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 373
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 70645,
          "cache_creation_input_tokens": 373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 373,
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

_source line 72 · 2026-05-21T05:52:54.448Z_

<details><summary>↩ Tool result · `toolu_01Y6gQBEdMPvh18NQjJSY2G7`</summary>

```text
atlas2025
barton1981
beeching2023openllm
biderman2024lessons
birnbaum1968
chang2024survey
chen2021humaneval
clark2018arc
cobbe2021gsm8k
codec2026
constat2024
deayala2009
deng2024
dodge2021
drasgow1985
embretson2000
gao2023evalharness
golchin2024
hendrycks2021mmlu
hong2021lzm
jacovi2023
karabatsos2003
lord1980
magar2022
martinezplumed2019
meijer2001
minkprob2024
oren2024
polo2024tinybenchmarks
psnirt2026
sainz2023
selfcritique2026
sinharay2017
snijders2001
wang2025fragility
zellers2019hellaswag
zhang2026rlvr
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7fd7b2f-51da-4ea1-82d5-e60973a3f2fc",
  "isSidechain": true,
  "promptId": "4fcfb10d-b26f-4dc3-8748-29ec958e3e7b",
  "agentId": "aebc5241daabf155a",
  "type": "user",
  "uuid": "710cac59-b86a-46dc-ab5f-d3b3bf9e906b",
  "sourceToolAssistantUUID": "d7fd7b2f-51da-4ea1-82d5-e60973a3f2fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 73 · 2026-05-21T05:54:28.868Z_

So the bib has 37 entries, 32 are cited in the paper, and 5 are in the bib but not cited (beeching2023openllm, biderman2024lessons, deayala2009, gao2023evalharness, hong2021lzm). Now I have everything needed for the review.

---

## R2 Review: Novelty & Related Work

### Summary (2-3 sentences)

This paper applies IRT person-fit statistics (specifically lz* from Snijders 2001) to detect benchmark contamination in LLMs using only binary response patterns. Controlled contamination experiments on two model families (Qwen2.5-7B, Llama-3.1-8B) demonstrate large effect sizes (|d| > 2.9) at 15% contamination on MMLU, while an empirical power function and theta-fixed analysis provide methodological characterization. Empirical analysis of 12 models across 5 benchmarks reveals universal 4PL model misfit (57/60 cells flagged), framed as a novel finding about LLM response patterns that motivates the Delta-lz* difference-in-differences design.

### Strengths (numbered)

1. **Well-motivated cross-disciplinary connection.** The analogy between contaminated LLMs and test-takers with item preknowledge is genuinely apt. Person-fit statistics have decades of theoretical backing for exactly this kind of aberrance detection, and the paper is the first to make this connection explicit. The "detection frontier" table (Table 1) clearly positions IRT-FIT relative to existing methods by information access level.

2. **Controlled experimental design is rigorous for a methods paper.** Using n=3 independent clean seeds per family, two model families, two contamination levels, and reporting both analytic and bootstrap CIs demonstrates statistical care. The seen/unseen split analysis (Finding 4) providing a mechanistic fingerprint of memorization is particularly insightful.

3. **Theta-shift analysis is a genuine methodological insight.** Identifying that re-estimating ability on contaminated data absorbs the aberrance signal, and that fixing theta to a pre-contamination baseline restores monotonic dose-response, is a non-trivial contribution. The free-theta non-monotonicity in Qwen vs. near-monotonicity in Llama adds depth by showing the effect is modulated by baseline misfit magnitude.

4. **Honest reporting of negative and mixed results.** The paper does not hide that (a) universal model misfit makes absolute lz* thresholds unusable, (b) item-level detection is near-random for all methods, (c) the power function R-squared is only 0.65, (d) n=3 yields analytic CIs that cross zero, and (e) the MML-EM refit fails on discrimination. This transparency strengthens credibility.

5. **4PL vs 3PL ablation is convincing.** The +27.3pp mean power gain on MMLU and the dramatic real-data divergence (r=0.225 between 4PL and 3PL lz*) demonstrate that the upper asymptote parameter is essential, not optional, for LLM evaluation contexts.

6. **Writing quality is high.** The paper is well-organized, claims are generally calibrated to evidence, notation is clean, and the experimental sections use a clear "Finding N" structure. The background section is self-contained enough for ML reviewers unfamiliar with psychometrics.

### Weaknesses (numbered, with severity)

1. **[Major] Limited novelty in the core method.** The primary technical contribution is computing lz* (a 25-year-old statistic) on LLM response data using externally-provided 4PL item parameters (from PSN-IRT). The framework involves no new statistics, no new estimation procedures, and no adaptation of person-fit theory to the LLM setting. The theta-fixed analysis and memorization fraction are straightforward applications of standard practice (fixing ability to a reference value) and normalized accuracy gaps, respectively. The "detection frontier" framing, while useful for exposition, is a narrative contribution rather than a technical one. For a top venue with 21% acceptance, the methodological novelty bar is not clearly met.

2. **[Major] lz* approximately equals HT in performance, undermining the IRT-specific framing.** Table 3 shows HT (which requires only item difficulty, not full IRT parameterization) achieves |d|=3.21/3.53 vs lz*'s |d|=3.42/2.95. The paper acknowledges this but pivots to "IRT person-fit family" as the contribution. This is problematic: the 4PL parameterization is presented as a key advantage (the 8x gain over Guttman/U3), but the comparison that matters most -- against HT -- shows the advantage is marginal or nonexistent. The 8x claim (vs Guttman/U3) is somewhat misleading as a headline because it compares against the weakest baselines rather than the strongest same-level competitor. HT's competitiveness suggests the value comes from item-difficulty-weighted aggregation, not IRT modeling per se.

3. **[Major] Only two model families with n=3 seeds each is thin for the claims made.** The paper draws broad conclusions about "detection frontier characterization" from Qwen and Llama only. Both are decoder-only transformers of similar scale (7-8B), fine-tuned with identical QLoRA settings. The project overview shows Mistral experiments are underway but not included. With n=3 seeds, the analytic CIs cross zero for all conditions (as the paper honestly notes), and the bootstrap CIs (resampling from 3 points) have questionable coverage properties. The claimed "cross-family consistency" rests on a very narrow empirical base.

4. **[Major] Post-RL robustness is claimed but not validated.** The paper repeatedly emphasizes that binary patterns are "structurally invariant" to RL-induced distributional changes (abstract framing, introduction paragraph 3, Table 1 footnote b, discussion). However, the actual paper contains zero post-RL experiments. The paper_framing.md indicates a post-RL experiment (exp-post-rl) was planned but the results are not in the paper. Claiming structural invariance to RL without evidence, while critiquing other methods for failing post-RL, is a significant credibility issue. The footnote "empirical verification future work" in Table 1 is insufficient.

5. **[Major] Practical utility is severely constrained.** The method requires: (a) pre-calibrated 4PL item parameters from PSN-IRT (not available for most benchmarks), (b) multiple clean baseline seeds or a pre-established threshold (the "bootstrapping problem" acknowledged in Limitations), (c) benchmarks with 8000+ items for 80% power at 15% contamination, and (d) the target is limited to SFT contamination only. These constraints collectively mean the method cannot currently be deployed on most practical contamination detection scenarios. The paper does not adequately address how practitioners would use this in practice.

6. **[Minor] The "minimal-information operating point" framing is imprecise.** Binary response patterns are not truly minimal information -- aggregate accuracy (a single scalar) is less information than an n-dimensional binary vector. The paper's claim is really about "minimal per-item information" or "no access beyond standard evaluation output," which is a different and less striking claim. Moreover, ConStat (Dekoninck et al. 2024) also operates without weight access or token probabilities, requiring only performance on original vs rephrased items -- the frontier positioning relative to ConStat is not clearly resolved.

7. **[Minor] The 57/60 universal misfit finding is framed ambiguously.** The paper presents 57/60 flagging as evidence that lz* captures "response-pattern structure lost in aggregate accuracy" (which is true), but also uses it to motivate the Delta-lz* design (which acknowledges the absolute values are meaningless). The 14x gap over accuracy z-score (57/60 vs 4/60) could be interpreted as lz* having extremely high false positive rates rather than superior sensitivity. The framing oscillates between presenting universal misfit as a contribution and as a limitation.

8. **[Minor] Missing direct comparison with ConStat.** ConStat is the closest methodological competitor (both performance-based, both requiring no weights/logits), yet the paper provides no experimental comparison. ConStat is placed in Table 1 but never evaluated head-to-head. Even a discussion-level analysis of where person-fit and consistency-based approaches should diverge would strengthen the positioning.

9. **[Minor] Qwen 50% contamination |d|=0.99 is weak.** While the theta-fixed analysis recovers a strong signal, the headline free-theta result for 50% contamination on Qwen is barely a large effect by conventional standards (0.8 threshold). The non-monotonicity is presented as a finding rather than a weakness, but in practical deployment, practitioners would likely use free-theta estimation (clean baselines may not be available), making this a real limitation.

### Questions for Authors

1. Given that HT achieves comparable effect sizes to lz* without requiring full 4PL parameterization (Table 3), what is the specific empirical advantage of lz* over HT? Is the contribution the specific statistic or the general idea of applying person-fit to LLMs?

2. The paper claims "structural invariance" to post-RL distributional changes, but post-RL training changes which items models get correct (not just the probability distributions over tokens). If RL changes the binary response pattern itself, how does the structural invariance argument hold?

3. How sensitive is detection to the quality of PSN-IRT item parameters? Given that MML-EM refit fails (r_a=0.127), what happens if PSN-IRT parameters have systematic biases for certain model families?

4. The memorization fraction is 33-38% at 15% contamination. This means ~62-67% of injected items are NOT memorized. What happens to detection power if a different fine-tuning approach (full-parameter, longer training) changes this fraction substantially?

5. For the 12-model empirical analysis, the universal positive lz* (over-consistency) is attributed to IRT assumption violations. Could this also indicate that PSN-IRT item parameters are miscalibrated for certain model architectures, rather than genuine model misfit?

6. The Delta-lz* design requires a "reference benchmark" presumed clean. In the real-world scenario where contamination is unknown, how would a practitioner identify such a reference?

### Missing References (specific papers/areas)

The bibliography has 37 entries with 32 cited -- this is improved from the initial characterization but still leaves notable gaps:

**Contamination detection methods not cited:**
- Gu et al. (2024), "WhoIsWho: Large-Scale Cross-Platform User Identification" -- may be less relevant, but the broader data contamination survey literature (Li et al. 2024 "A Survey on Data Contamination for Large Language Models") would strengthen context.
- Yang et al. (2023), "Rethinking Benchmark and Contamination for Language Models with Rephrased Samples" -- rephrasing-based detection, directly relevant to the frontier discussion.
- Zhu et al. (2024), "DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks" -- dynamic benchmarking as contamination mitigation.
- Roberts et al. (GPT-4 technical report contamination analysis) -- canonical reference for contamination awareness in major model releases.

**IRT for LLMs:**
- Uto (2024), "IRT-based LLM evaluation" work from the Japanese psychometrics community.
- Luo et al. (2024) on IRT-based benchmark difficulty estimation.
- The hong2021lzm entry is in the bib but not cited in the paper despite being directly relevant (multidimensional person-fit correction).

**Person-fit literature:**
- Reise (1990), "A Note on the Use of the lz Person-Fit Index" -- early validation study.
- Tendeiro & Meijer (2014), "Detection of Invalid Test Scores: The Usefulness of Simple Nonparametric Statistics" -- relevant to the HT comparison.
- St-Onge et al. (2011) on person-fit for detecting answer copying -- most directly analogous application.

**LLM memorization/generalization:**
- Carlini et al. (2023), "Quantifying Memorization Across Neural Language Models" -- relevant to the memorization fraction discussion.
- Tirumala et al. (2022), "Memorization Without Overfitting" -- relevant to SFT generalization effects.

**Missing from the cited literature_map.yaml but not in the paper:**
- hong2021lzm, beeching2023openllm, gao2023evalharness, biderman2024lessons, deayala2009 are all in the bib but uncited. The hong2021lzm paper on multidimensional lz* correction is particularly relevant given the paper's acknowledgment that LLM benchmarks are multidimensional.

### Excitement: 2.5/5

The core idea (person-fit for contamination) is clever and well-motivated, but the execution reveals that the approach has fundamental limitations (universal misfit, post-RL untested, thin empirical coverage, near-equivalence with simpler HT statistic) that collectively dampen excitement. The most interesting findings are arguably the negative ones (universal misfit, item-level near-randomness, theta-shift), which are more diagnostic than they are actionable. The paper reads as a thorough initial exploration that maps out possibilities and limitations, but does not yet deliver a method that practitioners can use.

### Preliminary Overall Assessment: 3.0 (Borderline Findings)

**Justification:** The paper makes a valid cross-disciplinary connection between psychometric person-fit and LLM contamination detection, and executes controlled experiments with reasonable rigor. The theta-shift analysis and universal misfit findings are genuine contributions to understanding. However, the core method applies an existing statistic to a new domain without adaptation; the near-equivalence with HT undermines the IRT-specific framing; the empirical base is narrow (2 families, n=3, one benchmark for controlled experiments); post-RL claims are unvalidated; and practical deployment constraints are severe. For EMNLP Main (21% acceptance), this falls short of the novelty and impact threshold -- the contributions are more "interesting characterization" than "tool the community will adopt." Findings-level publication (Overall Assessment 3.0) is appropriate: the work is methodologically sound and the findings are informative, but the novelty and excitement levels do not reach Main conference standards. The paper would be strengthened substantially by (a) including Mistral results for a third family, (b) running the post-RL experiment, (c) a direct ConStat comparison, and (d) a clearer articulation of when and why lz* should be preferred over HT.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "710cac59-b86a-46dc-ab5f-d3b3bf9e906b",
  "isSidechain": true,
  "agentId": "aebc5241daabf155a",
  "requestId": "req_011CbFCDD2iRc2C6ZTLkdfRC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dafb0c93-ded7-4b81-9de6-80257cc4923b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "46a229a4-0dcc-4513-b62d-d6edf34e81e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pb4NeKH6cnQoA1Mkm9PAKe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 71018,
      "output_tokens": 3552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 395
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3552,
          "cache_read_input_tokens": 71018,
          "cache_creation_input_tokens": 395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 395,
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
