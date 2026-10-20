# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus is **Methods and Experiments**. Review the paper below rig

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2ffc38510f39fa08.jsonl`
- **Structured JSON:** [`90a2f827205816e1a924.json`](../../sessions/90/90a2f827205816e1a924.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-21T02:07:38.735Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus is **Methods and Experiments**. Review the paper below rigorously against a top ML venue standard (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

## Paper Summary

**Title:** "Psychometric Characterization of Item-Level Instability in LLM Benchmarks via Differential Item Functioning"

The paper applies Differential Item Functioning (DIF) — a classical psychometric method — to the METABENCH response matrix (5,227 models × 12,508 MMLU items) to characterize item-level behavioral drift across model generations. It defines temporal cohorts (pre-2024 reference vs 2024-H1 focal) and uses the Mantel-Haenszel χ² procedure with ETS effect-size classification.

**4 Core Claims:**
1. **38% of MMLU items are functionally unstable** (ETS C category, |Δ_MH|≥1.5) across model generations. Per-subject C% ranges 31-45%. Random-split sanity check: C%=0.18%. Capability improvement confound: ρ=0.307 between C% and domain accuracy gains. The paper frames this as a "mixture" that cannot be decomposed.
2. **Methodological gap in contamination detection validation**: web-overlap labels (Li et al.) measure global item exposure, not differential functioning. Enrichment ≈1.0 between DIF flags and web-overlap labels. Semi-synthetic injection confirms DIF's detection power (ΔTPR=+0.508).
3. **Semi-synthetic validation framework**: Injects differential contamination into real response matrices, measures ΔTPR. Cross-subject matching eliminates FPR inflation (ΔFPR=0.000 vs +0.186 for within-subject). Cross-benchmark replication on GSM8K (ΔTPR=+0.818).
4. **DIF as diagnostic lens**: ρ≈0.997 after removing 31% DIF items (measurement redundancy). But DIF items carry disproportionate discriminative signal (z=−8 to −49σ vs random removal). GSM1K cross-benchmark evidence (r=−0.478, p=0.005, N=33) is "suggestive."

**Robustness Analyses (Section 5):**
- 5.1 Architecture-Stratified DIF: Decoder-only subset → C% drops from 31.3% to 28.2%, RMSEA 0.089→0.067, CFI 0.78→0.83. Still below 0.90 threshold.
- 5.2 Item-Focused Trees: IFT flags 28.4% (Jaccard=0.72 with categorical), 14% nonlinear DIF trajectories.
- 5.3 Reasoning-RL Robustness: N=13 reasoning-RL models. DIF flag retention 86%. ConStat AUROC 0.72→0.54, Min-K% 0.68→0.49. DeLong p=0.087, TOST p=0.11. Reported as "preliminary."
- 5.4 Graceful Degradation: Progressive replacement 5-50%. ρ=0.972 at 50%. Near-linear bound ρ ≥ 1−1.3r.
- 5.5 Cumulative Bayesian DIF: Simulation-only. Power 0.41→0.74 over 4 administrations for δ=1.0.

**Complementary Baselines (Section 6):**
- 6.1 ConStat perturbation: 248 items, 15 models. Detection rate 12.7% (FDR=0.10). AUROC vs Li labels = 0.61.
- 6.2 DVD: 300 items, 12 models, 50 gens/item, T=0.8. AUROC 0.71 (verbatim), 0.63 (variant). 62 GPU-hours.
- 6.3 Ensemble: 2-of-3 voting AUROC=0.66 (vs best individual 0.62). Negative result — orthogonal mechanisms.

**Pilot Studies (Section 7):**
- 7.1 Bifactor IRT Equating: General + 57 subject factors. CFI=0.87, TLI=0.84 (marginal). Anchor items: 1,842. Equated ρ=0.93 (below target 0.95).
- 7.2 LLM Item Generation: 200 items, 156 pass quality filter. Student simulation difficulty ρ=0.64 (vs prompt-based 0.31). Holdout panel correlation 0.58. 187 GPU-hours.

**Experiment Coverage Reference (from review_context.yaml):**
The full experiment plan included 10 imagined experiments. The paper covers all of them, though several are acknowledged as underpowered, pilot-level, or simulation-only. Key issues flagged in the design document:
- RL robustness (plan_002): N=13 is too few; TOST equivalence fails (p=0.11); DeLong marginal (p=0.087)
- Bifactor equating (plan_005): CFI=0.87 marginal; equated ρ=0.93 below 0.95 target
- Item generation (plan_006): Difficulty ρ=0.64 below published benchmarks (0.75-0.82); holdout transfer ρ=0.58
- Ensemble (plan_003c): Effectively a negative result, ensemble provides minimal lift
- Bayesian DIF (plan_007): Purely simulation-based, no real longitudinal data
- Architecture DIF (plan_010): CFI still below 0.90 even after stratification

## Your Review Task

Evaluate the following dimensions in depth:

### 1. Methodological Soundness
- Is the MH DIF procedure appropriately applied? Is the 2PL IRT model justified for binary MMLU responses?
- Is the temporal cohort definition (pre-2024 vs 2024-H1) principled or arbitrary?
- Is matching on total score appropriate given MMLU's 57-subject structure?
- Evaluate the semi-synthetic injection protocol: is flipping incorrect→correct a realistic contamination model?
- Cross-subject matching: is this technically sound for eliminating FPR inflation?

### 2. Statistical Rigor
- The 38% claim: given the acknowledged ρ=0.307 capability confound, how interpretable is this number?
- IRT model fit is poor (RMSEA=0.089, CFI=0.78 for full population). How much does this undermine the DIF analysis?
- Multiple testing: 12,508 items tested — is multiple comparison correction applied?
- The ρ=0.997 redundancy finding: is this meaningful or tautological given MMLU's 12,508 items?
- GSM1K evidence: N=33 with contamination gap as proxy — how robust is this?

### 3. Experimental Coverage and Quality
- Are the robustness analyses sufficient to address key threats?
- Are pilot studies (bifactor equating, item generation) mature enough for inclusion?
- Is the negative ensemble result well-characterized?

### 4. Reproducibility
- METABENCH is used but no code/data is provided (promised upon publication). Is the methodology described in sufficient detail?

### Output Format
Provide your review as:

**Summary:** 2-3 sentences on what the paper does.

**Strengths:** Bulleted list (S1, S2, ...) with specific evidence.

**Weaknesses:** Bulleted list (W1, W2, ...) with specific evidence and severity (minor/moderate/major).

**Questions for Authors:** Numbered list of clarification questions.

**Missing Experiments / Analyses:** What's absent that should be present?

**Preliminary Score:** X/6 with one-sentence justification.

**Confidence:** 1-5 scale.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "99bbef4a-f607-4d57-895b-5ad4fe9e395d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T02:07:38.742Z_

```json
{
  "parentUuid": "99bbef4a-f607-4d57-895b-5ad4fe9e395d",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
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
  "uuid": "a21f3c42-6d6b-4bd8-9281-af8f59ef41a1",
  "timestamp": "2026-05-21T02:07:38.742Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T02:07:41.124Z_



I'll start by reading the paper and any relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a21f3c42-6d6b-4bd8-9281-af8f59ef41a1",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu2udh9CMkprh1U4zUH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dc9fcfd-85a2-4b88-996f-29517127c58f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBtMr6CZLqdaWgBSX1J2WS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7935,
      "cache_read_input_tokens": 8254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7935,
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

_source line 4 · 2026-05-21T02:07:42.263Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012Co8m9pu49xyiV6TS7SV87`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dc9fcfd-85a2-4b88-996f-29517127c58f",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu2udh9CMkprh1U4zUH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d5ee333-6ed9-4ddf-a992-0879f312a838",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBtMr6CZLqdaWgBSX1J2WS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7935,
      "cache_read_input_tokens": 8254,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7935
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 8254,
          "cache_creation_input_tokens": 7935,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7935,
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

_source line 5 · 2026-05-21T02:07:42.268Z_

<details><summary>↩ Tool result · `toolu_012Co8m9pu49xyiV6TS7SV87`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d5ee333-6ed9-4ddf-a992-0879f312a838",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "7a7dcf2a-c113-4470-b985-1d4d2b2ae8de",
  "sourceToolAssistantUUID": "6d5ee333-6ed9-4ddf-a992-0879f312a838",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T02:07:44.554Z_



Let me read the paper report and other relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a7dcf2a-c113-4470-b985-1d4d2b2ae8de",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu3AxBwhSJ6N1J8q2uD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca111e26-fa9b-4955-9cc0-996a3169cd40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TwyMAba6Xe3Ei4SbY3j5u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 7 · 2026-05-21T02:07:45.972Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AVkmH8M5N5xcLF2wYA9w2d`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca111e26-fa9b-4955-9cc0-996a3169cd40",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu3AxBwhSJ6N1J8q2uD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "207967e5-22b2-42a0-9454-853845cdbaa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TwyMAba6Xe3Ei4SbY3j5u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 8 · 2026-05-21T02:07:45.988Z_

<details><summary>↩ Tool result · `toolu_01AVkmH8M5N5xcLF2wYA9w2d`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\\n\\n## 近期结论\\n- **plan_004_gsm8k_cross_benchmark** (negative): GSM8K 的 temporal DIF (2023 vs 2024) 将展示与 MMLU 类似的 30-40% ETS C%，证明 temporal DIF 现象跨 benchmark 泛化。使用 METABENCH 其他 benchmarks 总分做 external matching（GSM8K 无 subject 分层），预期 baseline FPR 更可控。如果 C% 在同一量级 → DIF 作为 benchmark health diagnostic 的泛化性得到验证。 ← 基于 plan_001_real_data_dif_mmlu\\n- **plan_017_downstream_impact** (negative): 移除 temporal DIF-flagged items (ETS C, ~31% of MMLU items) 后，模型跨代排名更稳定（Spearman ρ 提升），且稳定性提升显著优于随机移除相同数量 items 的 baseline。这证明 DIF 不只标记 noise，而是精确识别了 problematic items，为 DIF 作为 benchmark quality tool 提供 downstream evidence。 ← 基于 plan_001_real_data_dif_mmlu\\n- **plan_016_within_subject_semi_synthetic** (success): 在 subject 内部使用 within-subject total score 做 MH 分层的 semi-synthetic injection 中，DIF 仍能检测差异性污染（ΔTPR > 0.3 at p=0.5）。这证明 DIF 方法在 subject 级别也有效，plan_014 的 38% within-subject C% 反映的是真实代际能力差异而非方法失败。 ← 基于 plan_014_within_subject_dif\\n  [plan_016_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md) | [plan_016_dose_response](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response.csv) | [plan_016_revised_dose_response](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response_e6d86f.csv) | [plan_016_revised_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md)\\n\\n## 趋势\\n成功 5 / 负向 6 / 失败 0 / 共 11\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 2009, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "207967e5-22b2-42a0-9454-853845cdbaa7",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "6f4b821c-0ac3-49b1-bf0e-d4df4c032020",
  "sourceToolAssistantUUID": "207967e5-22b2-42a0-9454-853845cdbaa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T02:07:46.458Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CcXfQKoQs1ZPpZaqFyHm7C`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f4b821c-0ac3-49b1-bf0e-d4df4c032020",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu3AxBwhSJ6N1J8q2uD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36857fc9-6758-4d28-8662-59fa46840737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TwyMAba6Xe3Ei4SbY3j5u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 10 · 2026-05-21T02:07:46.477Z_

<details><summary>↩ Tool result · `toolu_01CcXfQKoQs1ZPpZaqFyHm7C`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/decisions.yaml\", \"content\": \"_next_id: 15\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:50 UTC\\n  summary: MVP DIF 检测采用 ETS C 分类（效应量+显著性双阈值）替代 BH 校正 p 值作为主判定标准\\n  rationale: Monte Carlo 模拟显示 BH 校正在 200 items 场景下将 TPR 压缩 40-60%，所有核心条件均 FAIL/GRAY。但\\n    ETS C 分类（|Δ_MH|≥1.5 + 显著性，教育测量 gold standard）在 N≥80, δ≥1.4 时 TPR=0.72-0.85, FPR<0.05，满足\\n    pass criteria。ETS C 是 DIF 领域标准实践（Holland & Thayer 1988），使用效应量阈值比纯 p 值更稳健。操作点 N≥80,\\n    δ≥1.4 与 GSM1K 文档的重度污染效应量吻合。小效应由 ensemble 其他信号覆盖。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'BH-corrected: all FAIL/GRAY; ETS C: PASS at N≥80,δ≥1.4 (TPR=0.72-0.85,\\n      FPR<0.05)'\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:31 UTC\\n  summary: MVP 通过：DIF+ETS C 在 N≥80,δ≥1.4 下功效达标，推荐 N≥100 为主操作点\\n  rationale: Phase 1 合成参数 + Phase 2 真实参数（PSN-IRT）均验证 ETS C TPR≥0.65 at N≥80,δ≥1.4。Phase\\n    2 比 Phase 1 降低 3-6pp 符合预期。N=80,δ=1.4 裕度仅 0.032，推荐 N≥100 为主 claim。数据源为 PSN-IRT\\n    而非 ROADMAP 指定的 METABENCH，research 阶段需用 METABENCH 补充验证。限制：δ<1.0 需 ensemble 其他信号。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'Phase 1 conditional pass: ETS C TPR=0.72-0.85 at N≥80,δ≥1.4'\\n  - exp_id: mvp_dif_power_sim_phase2\\n    role: evidence\\n    result: 'Phase 2 pass: ETS C TPR=0.68-0.80 at N≥80,δ≥1.4 with real MMLU params'\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 20:49 UTC\\n  summary: 'Dream analysis (dream_20260520T194223): 6 confirmed actions from cross-tier\\n    synthesis, 2 new experiments added (plan_010/011), framing qualified'\\n  rationale: 'Dream scores met thresholds (best=4/6, median=3.5/6, worst=3/6). Cross-tier\\n    analysis identified 6 confirmed issues (≥2 tiers): (1) contamination-capability\\n    confound → within-family analysis added to plan_001; (2) RL evidence underpowered\\n    → bootstrap CIs + equivalence testing added to plan_002; (3) partial exploitation\\n    gap → power analysis added to plan_002; (4) ground truth circularity → plan_011\\n    semi-synthetic validation added; (5) related work thin → Paper Agent writing-phase\\n    task; (6) Growing Pains differentiation → Paper Agent task. Additionally: plan_010\\n    architecture-stratified DIF added as P1 proactive defense from worst-case; novelty\\n    claim qualified from \\\"first self-healing benchmark\\\" to \\\"psychometric monitoring\\n    framework\\\". Re-dream required before P0 approval.'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 21:14 UTC\\n  summary: plan_001 temporal cohort DIF 证伪（enrichment=0.96），根因是 impact vs DIF 混淆。批准\\n    matched-ability DIF 作为方法改进方向 1\\n  rationale: Temporal cohort MH-DIF 标记 31.3% items 为 ETS C，但 enrichment=0.96（clean\\n    和 contaminated 标记概率相同）—— DIF 检测的是系统性能力提升而非污染。Within-family (Llama-2 vs Llama-3)\\n    61.3% C 进一步证实。这是经典 impact vs DIF 混淆（Dream D2 预测过）。但 ability-quintile enrichment=1.19\\n    + FPR=2.7% 表明信号存在但弱。方向1 matched-ability temporal DIF 在 quintile 内做时间对比，是最快验证能力匹配能否放大信号的路径。方向2\\n    IRT equating 并行准备作为 fallback。\\n  related_experiments:\\n  - exp_id: plan_001_real_data_dif_mmlu\\n    role: evidence\\n    result: negative - temporal cohort enrichment 0.96, ability quintile enrichment\\n      1.19\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-20 21:24 UTC\\n  summary: 方向 1 (matched-ability DIF) 失败确认，所有 quintile enrichment 0.94-1.04。plan_011\\n    是唯一决定性实验\\n  rationale: Quintile 内 temporal DIF 仍 enrichment≈1.0，ability matching 未能分离污染信号。但\\n    Reviewer 指出关键洞察：Li et al. web-overlap 是全局性污染（Common Crawl 对所有模型可用），不应产生 group-specific\\n    DIF。enrichment≈1.0 可能是 ground truth 不匹配而非方法失败。plan_011 注入的是已知差异性污染（仅 focal group），是唯一能区分\\\"DIF\\n    不 work\\\"和\\\"ground truth 不对\\\"的实验。方向 2 (IRT θ-matching) 如果问题出在 ground truth 也无法解决。\\n  related_experiments:\\n  - exp_id: plan_001b_matched_ability_dif\\n    role: evidence\\n    result: negative - all quintiles enrichment 0.94-1.04\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-20 21:56 UTC\\n  summary: 'plan_011 positive: MH-DIF 检测差异性污染有效 (p=0.5 TPR=0.834, p=1.0 TPR=1.0)，但\\n    baseline FPR=31% 需 IRT θ-conditioning 降低。启动方向 2'\\n  rationale: Semi-synthetic validation 确认 DIF 能检测差异性污染（剂量-响应单调，Fisher p<1e-21）。plan_001/001b\\n    失败归因于 Li et al. web-overlap 是全局性标注，不产生 group-specific DIF。但 baseline FPR=31% (temporal)\\n    / 49% (ability) 意味着 DIF 是筛查工具（高召回、中等精度），不是确诊工具。Precision ~44% at p=1.0。两个推进方向：(1)\\n    IRT θ-conditioning 降低 baseline FPR (方向 2)，(2) Ensemble 信号 (Claim 2) 过滤假阳性——DIF\\n    高召回 + ConStat 高精度自然衔接。同时需 Yen's Q3 诊断局部独立性（审稿 WC4），局部依赖可能是 FPR 膨胀的部分原因。\\n  related_experiments:\\n  - exp_id: plan_011_semi_synthetic\\n    role: evidence\\n    result: positive - TPR 0.834 at p=0.5, 1.0 at p=1.0; but baseline FPR 0.314\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-20 21:58 UTC\\n  summary: 'Story pivot: semi-synthetic validation 作为核心效度证据，Li et al. enrichment≈1.0\\n    重新定位为\\\"全局 vs 差异性污染\\\"的发现。IRT θ-conditioning 继续（降 FPR），但不期望改善 Li enrichment'\\n  rationale: 'Agent 和 Reviewer 均指出：即使 IRT θ 完美控制能力，Li et al. web-overlap 仍是全局标注，enrichment\\n    仍≈1.0。plan_011 semi-synthetic (ΔTPR=+0.674, Fisher p<1e-42) 是 DIF 方法有效性的决定性证据。Li\\n    et al. enrichment≈1.0 不是方法失败，而是揭示了现有\\\"污染标注\\\"实际测量的是全局 web 曝光（所有模型共享），不是差异性训练数据包含。这是一个有价值的发现：DIF\\n    检测差异性污染，现有标签标注存在性污染，两者度量不同。Story: DIF 是差异性污染的高灵敏度筛查工具 + ensemble 提升精度 + 全局/差异性污染区分是方法论贡献。'\\n  related_experiments:\\n  - exp_id: plan_011_semi_synthetic\\n    role: evidence\\n    result: positive\\n  - exp_id: plan_001_real_data_dif_mmlu\\n    role: evidence\\n    result: negative - reinterpreted as ground truth mismatch\\n  - exp_id: plan_001b_matched_ability_dif\\n    role: evidence\\n    result: negative - reinterpreted as ground truth mismatch\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-20 22:12 UTC\\n  summary: 方向 2 (IRT θ-conditioning) 失败，1D 路线穷尽。plan_011 ability cohort TPR 修正（76%→21%，73%\\n    是能力混淆）。启动 plan_005 bifactor IRT 作为最后结构性改进\\n  rationale: logit(p) 与 total score 相关 0.9986，所有 θ 变体 FPR 31-35%。plan_011 ability\\n    cohort 在 θ 10/20-bin conditioning 下 TPR 从 76% 降到 21%（p=0.5）——原 5-bin 分层不足以消除 Q1-2\\n    vs Q4-5 极端能力差异。DIF 面临 TPR-FPR tradeoff：temporal 高 TPR 但 FPR=31%，ability (proper)\\n    低 FPR=8% 但 TPR=21%。根因：temporal cohort 间差异是多维的（不同学科能力提升不均匀），1D θ 无法捕获。Bifactor\\n    model (general + 57 subject factors) 是唯一能吸收学科级差异的结构性方法。已尝试 2 种不同类型改进方向，bifactor\\n    是第 3 种。计算量大（5227×12508×58 factors），可能需要服务器。\\n  related_experiments:\\n  - exp_id: plan_012_irt_theta_conditioning\\n    role: evidence\\n    result: negative - temporal FPR stuck at 31%, ability TPR corrected to 21%\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-20 22:17 UTC\\n  summary: 'Dream #2 分析：best=3/6, median=3-4/6, worst=3/6。跨档一致：impact-vs-DIF confound\\n    为首要问题，bifactor 是正确方向。新发现：ensemble 不优于 DIF alone、SIBTEST/MIMIC 未尝试、detection trilemma\\n    概念'\\n  rationale: 三档审稿一致认为 within-family confound (42-62% overlap) 是最致命问题——没有 bifactor\\n    分离学科级能力差异，DIF flags 的可解释性无法建立。worst case 新增 SIBTEST/MIMIC 作为 established impact-vs-DIF\\n    solutions 的替代方案需要考虑。median 指出 ensemble AUROC (0.72) 低于 DIF alone (0.76)，Claim\\n    2 需要重新评估。worst case 提出 detection trilemma (IRT fit ↔ power ↔ confound control)\\n    作为潜在概念贡献。行动：(1) 优先完成 bifactor，(2) 考虑 SIBTEST/MIMIC 作为备选，(3) 推迟 ensemble 设计到 bifactor\\n    结果出来后，(4) 补充 impact-vs-DIF 文献\\n  related_experiments:\\n  - exp_id: dream_20260520T205007\\n    role: dream_simulation\\n    result: best=3/6, median=3-4/6, worst=3/6\\n  depends_on:\\n  - D008\\n  - D007\\n  - D006\\n- id: D010\\n  date: 2026-05-20 22:29 UTC\\n  summary: 方向 3 (Bifactor) pre-check 否定：within-subject temporal C%=38.1% (range 31-45%)，高于\\n    overall 31%。Bifactor 移除的 between-subject variance 反而在压低 C%。三种结构性改进方向全部失败，Method→Analysis\\n    pivot 前提 (a)(b) 已满足\\n  rationale: 'plan_014 within-subject DIF 前置检查：5 个 subject 的 within-subject temporal\\n    C% 平均 38.1%，没有一个低于 30%。Cross-subject matching 仅 Δ=-2.4pp。这证明 temporal DIF 是 item-specific\\n    的真实差异（能力提升+污染+其他），不是 matching artifact。Bifactor 即使完美运行也无法降 FPR 到 15% 以下。决策链：D005(方向1失败)\\n    → D008(方向2失败) → D010(方向3 pre-mortem 证伪)。Oracle: plan_011 semi-synthetic ΔTPR=+0.508\\n    确认方法本身有效。Pivot 前提 (c) 待用户确认投稿目标调整。'\\n  related_experiments:\\n  - exp_id: plan_014_within_subject_dif\\n    role: pre-check\\n    result: within-subject C%=38.1%, bifactor not viable\\n  - exp_id: plan_011_semi_synthetic\\n    role: oracle\\n    result: ΔTPR=+0.508, method works for differential contamination\\n  depends_on:\\n  - D008\\n  - D009\\n  - D005\\n- id: D011\\n  date: 2026-05-20 23:23 UTC\\n  summary: Pivot 拍板：从\\\"DIF 检测方法\\\"转向\\\"LLM benchmark psychometric characterization + DIF\\n    methodology\\\"。Cross-subject matching ΔFPR=0.000 是方法论突破，31-38% temporal DIF 是实证发现。保持\\n    ICLR 2027 目标不降级\\n  rationale: 三种结构性改进全部穷尽（D005/D008/D010），oracle 确认方法有效（plan_011 ΔTPR=+0.508）。但 pivot\\n    不等于降级：(1) cross-subject matching ΔFPR=0.000 是干净的方法论贡献——解决了 matching variable contamination\\n    这个 MH-DIF 领域的实际问题；(2) 31-38% temporal DIF 是首次大规模量化 LLM benchmark item instability；(3)\\n    global vs differential contamination 区分是概念贡献；(4) semi-synthetic validation framework\\n    可独立复用；(5) detection trilemma 是 characterization 贡献。这些组合起来是 ICLR 级别的 empirical\\n    findings paper，不需要降到 findings track。用户批评\\\"等我点头\\\"正确——这是 PI 的决策责任。\\n  related_experiments:\\n  - exp_id: plan_016_within_subject_semi_synthetic\\n    role: final_validation\\n    result: cross-subject ΔFPR=0.000, 4/5 ΔTPR>0.3\\n  - exp_id: plan_014_within_subject_dif\\n    role: pre-check\\n    result: within-subject C%=38.1%\\n  - exp_id: plan_011_semi_synthetic\\n    role: oracle\\n    result: ΔTPR=+0.508\\n  depends_on:\\n  - D010\\n  - D009\\n  - D006\\n- id: D012\\n  date: 2026-05-20 23:28 UTC\\n  summary: Story 定稿：Candidate 1 (benchmark quality tool) + ground truth meta-critique\\n    + semi-synthetic infrastructure。降级 cross-subject matching 为 recommendation（非 breakthrough）。新增\\n    downstream impact 实验（移除 DIF items → ranking stability）作为 ICLR 关键补充\\n  rationale: Reviewer 评估：(1) 三候选中 Candidate 1 最自洽，(2) cross-subject matching 是 external\\n    matching 的自然推广非新方法（降级），(3) enrichment≈1.0 + semi-synthetic positive 证明现有污染 ground\\n    truth 自身有缺陷（meta-contribution），(4) \\\"so what?\\\" 缺口是 ICLR vs findings track 的分水岭——需\\n    downstream impact 实验回答。38% 与 domain specificity ρ=0.307 的关系必须在 limitations 诚实讨论。\\n  related_experiments:\\n  - exp_id: plan_014_within_subject_dif\\n    role: finding\\n    result: 38% temporal DIF\\n  - exp_id: plan_016_within_subject_semi_synthetic\\n    role: method\\n    result: cross-subject ΔFPR=0.000\\n  - exp_id: plan_001_real_data_dif_mmlu\\n    role: finding\\n    result: enrichment≈1.0 → ground truth meta-critique\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-21 00:06 UTC\\n  summary: plan_017 downstream impact negative 但 informative：DIF items 是浓缩差异化信号载体而非噪声。Claim\\n    4 从 placeholder \\\"remove for stability\\\" 转为 finding \\\"DIF as diagnostic lens\\\"。DIF\\n    items 移除造成更大排名扰动（21/21 条件显著），phi-3/llama-3 获益最多，mistral merge 被压制\\n  rationale: plan_017 全面证伪了\\\"移除 DIF items 改善排名稳定性\\\"的 hypothesis：(1) full vs stable-only\\n    ρ=0.996-0.999 说明排名本身极鲁棒，(2) DIF removal 扰动显著大于 random removal（z=-8 to -49σ），(3)\\n    DIF items 的跨代准确率变化是 full benchmark 的 1.09×。这意味着 DIF items 不是\\\"坏题\\\"而是\\\"模型代际差异的诊断标记\\\"。对\\n    paper narrative 的影响：从\\\"remove unstable items\\\"转向\\\"DIF as diagnostic lens for understanding\\n    model evolution\\\"。这个 negative result 比 positive 更有深度——\\\"keep these items, they tell\\n    you something\\\" 是更有价值的 benchmark design recommendation。\\n  related_experiments:\\n  - exp_id: plan_017_downstream_impact\\n    role: hypothesis_test\\n    result: negative - DIF items carry MORE discriminative signal, not less\\n  depends_on:\\n  - D012\\n  - D011\\n- id: D014\\n  date: 2026-05-21 01:25 UTC\\n  summary: 'plan_004 Step 3 GSM1K: |r|=0.478 显著但方向为负——DIF 不标记 contamination，而是标记 contamination\\n    无法到达的 capability-discriminative items'\\n  rationale: r=−0.478 (p=0.005), Spearman ρ=−0.403 (p=0.020), partial r=−0.385 (p=0.027\\n    控制 overall accuracy), permutation p=0.014, leave-one-out robust (min |r|=0.374)。N=33\\n    matched models。171 个 focal-favoring DIF-C items 驱动负相关 (r=−0.347, p=0.048)：contaminated\\n    models 在这些 genuine capability improvement items 上表现更差。这不支持 \\\"DIF = contamination\\n    detector\\\" 假设，但强力支撑 pivot 后 \\\"DIF as diagnostic lens\\\" 叙事：DIF 捕获的是真实能力差异，contamination\\n    产生的浅层提升无法到达这些 items。与 plan_017 (DIF items = discriminative signal carriers) 形成双重验证。不升级\\n    ICLR 为 \\\"validated method\\\"，但显著加强 characterization paper 的深度和跨 benchmark 证据。\\n  related_experiments:\\n  - exp_id: plan_004_gsm8k_cross_benchmark\\n    role: primary\\n    result: negative_but_informative\\n  - exp_id: plan_017_downstream_impact\\n    role: corroborating\\n    result: negative_but_informative\\n  depends_on:\\n  - D013\\n  - D011\\n\", \"total_chars\": 12255, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36857fc9-6758-4d28-8662-59fa46840737",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "056e9754-21c6-4b7d-8314-7568d8dea9f5",
  "sourceToolAssistantUUID": "36857fc9-6758-4d28-8662-59fa46840737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T02:07:47.203Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KVK2WGZ6XhYewBRdjnKTwm`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "056e9754-21c6-4b7d-8314-7568d8dea9f5",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu3AxBwhSJ6N1J8q2uD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eef7ebaf-dce9-4b21-80e0-eec009f665a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TwyMAba6Xe3Ei4SbY3j5u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16189,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1291
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 16189,
          "cache_creation_input_tokens": 1291,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1291,
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

_source line 12 · 2026-05-21T02:07:47.213Z_

<details><summary>↩ Tool result · `toolu_01KVK2WGZ6XhYewBRdjnKTwm`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eef7ebaf-dce9-4b21-80e0-eec009f665a5",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "1b73e60a-0de3-4cee-a617-d51b080d720a",
  "sourceToolAssistantUUID": "eef7ebaf-dce9-4b21-80e0-eec009f665a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T02:07:51.573Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01USdyi2P7KDFmMtF7Dd1qVf`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b73e60a-0de3-4cee-a617-d51b080d720a",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu3Y2DAPvDvjuJqcGP7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff45913a-f0f6-4fda-b237-67c8b3de7c45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGe4giE5Tntv8acDdWdmSq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8033,
      "cache_read_input_tokens": 17480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8033,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 14 · 2026-05-21T02:07:51.590Z_

<details><summary>↩ Tool result · `toolu_01USdyi2P7KDFmMtF7Dd1qVf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md\", \"content\": \"# Paper Framing — irt_equated_bench_regen\\n\\n## Target Venue\\n- Primary: ICLR 2027 (expected deadline ~October 2026)\\n\\n## Paper Type\\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \\\"DIF reveals benchmark structural problems,\\\" not \\\"DIF detects contamination.\\\"\\n\\n## Core Claims (4 条, 可证伪)\\n\\n**Claim 1 (Temporal Comparability Concern)**: 38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. This instability persists within every subject domain (within-subject C%=31-45%, avg 38.1%), is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). This means cross-temporal MMLU score comparisons carry uncontrolled item-level variance.\\n- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%)\\n- Honesty requirement: ρ=0.307 means \\\"item instability\\\" may mainly reflect \\\"models got better at those domains\\\" — we cannot decompose 38% into contamination vs capability improvement\\n\\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\\n- Framing: aggressive — \\\"the field's standard validation approach is fundamentally mismatched for item-level detection\\\"\\n\\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\\n\\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\\n2. **DIF items = discriminative signal carriers**: DIF removal causes significantly MORE ranking disruption than random removal (z=-8 to -49σ, 21/21 conditions). DIF items carry 1.09× cross-cohort accuracy swing vs 0.96× for stable items — they concentrate the information that differentiates model generations.\\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \\\"find bad items and remove\\\" but \\\"understand what changed and why.\\\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\\n4. **Cross-benchmark validation — DIF captures capability, not contamination**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005; partial r=−0.385 controlling accuracy; permutation p=0.014). Contaminated models (high GSM8K-GSM1K gap: Phi, Gemma families) perform WORSE on DIF items. DIF captures genuine capability-discriminative items that contamination cannot fake — contamination produces shallow performance gains concentrated on non-DIF items. N=33 matched models, leave-one-out robust (min |r|=0.374).\\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_004 Step 3 (r=−0.478, p=0.005, 33 models)\\n- Growing Pains互补: \\\"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\\\" — mutual value positioning\\n- Caveats (→ limitations): super-family analysis limited to N≥20 families; GSM1K validation N=33 (CI wide); contamination gap is proxy, not ground truth\\n\\n## Story Spine\\n\\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \\\"Model B outperforms Model A on MMLU,\\\" we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.\\n\\n**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\\n\\n**What we find**: Three discoveries, each a contribution:\\n\\n1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.\\n\\n2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.\\n\\n3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.\\n\\n4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K confirms: DIF flags anti-correlate with contamination (r=−0.478, p=0.005) — contaminated models can't fake performance on DIF items, which capture genuine capability differences. DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.\\n\\n**Headline result**: \\\"Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF flags anti-correlate with contamination (r=−0.478, p=0.005): DIF captures genuine capability-discriminative items that contamination cannot replicate. We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000).\\\"\\n\\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\\n\\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\\n\\n## Venue Fit\\n\\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\\n- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 38% instability, (2) the ground truth meta-critique affecting the field, (3) the semi-synthetic framework. Frame as \\\"bringing mature psychometric tools to characterize an urgent ML evaluation problem.\\\"\\n\\n## Anticipated Reviewer Concerns (updated for pivot)\\n\\n1. **\\\"38% could just mean models got better\\\"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.\\n\\n2. **\\\"Ground truth critique is obvious — of course web labels don't capture differential effects\\\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\\n\\n3. **\\\"Semi-synthetic injection is artificial\\\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\\n\\n4. **\\\"DIF power is only sufficient for large effects\\\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\\n\\n5. **\\\"Only validated on MMLU\\\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\\n\\n6. **\\\"Higher methods (MIMIC, propensity-score) could solve the confounding\\\"** — Acknowledged as future work. We frame our three-attempt negative results as \\\"empirical observation\\\" that motivates these directions, not as impossibility.\\n\\n## Dropped from Original Framing\\n\\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\\n- **Detection as primary contribution**: Pivoted from \\\"we detect contamination\\\" to \\\"we characterize benchmark properties.\\\"\\n\", \"total_chars\": 11796, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff45913a-f0f6-4fda-b237-67c8b3de7c45",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "7fedb408-ea4c-4f73-b7f7-a0568d17baff",
  "sourceToolAssistantUUID": "ff45913a-f0f6-4fda-b237-67c8b3de7c45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T02:07:52.572Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CKrUcoMx1BmA6rAEix7rWH`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fedb408-ea4c-4f73-b7f7-a0568d17baff",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu3Y2DAPvDvjuJqcGP7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5db62c0a-afd2-461b-bb0f-694f0fc74069",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGe4giE5Tntv8acDdWdmSq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8033,
      "cache_read_input_tokens": 17480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8033,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 16 · 2026-05-21T02:07:52.586Z_

<details><summary>↩ Tool result · `toolu_01CKrUcoMx1BmA6rAEix7rWH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/writing_plan.yaml\", \"content\": \"meta:\\n  venue: ICLR 2027\\n  track: main\\n  template: \\\"\\\"\\n  template_note: \\\"ICLR 2027 template not yet available locally; will download or reuse iclr2025 when entering Step 2\\\"\\n  page_limit: 9\\n  deadline: \\\"2026-10-01\\\"\\n  core_claim: >-\\n    Applying DIF to MMLU (5,227 models × 12,508 items) reveals 38% item-level\\n    functional instability across model generations, exposes a fundamental gap\\n    in contamination ground truth labels, and provides a semi-synthetic\\n    validation framework for item-level detectors.\\n  created_at: \\\"2026-05-20T23:45:00Z\\\"\\n  story_arc:\\n    hook: >-\\n      When we say \\\"Model B outperforms Model A on MMLU,\\\" we assume temporal\\n      comparability — but 38% of MMLU items function differently across model\\n      generations.\\n    gap: >-\\n      Existing contamination labels (web-overlap, n-gram) measure global\\n      exposure, not differential item functioning — every validation study\\n      using these labels has a blind spot. This is a fundamental validation\\n      methodology gap affecting the entire contamination detection field.\\n    insight: >-\\n      DIF detects differential contamination (semi-synthetic ΔTPR=+0.508) but\\n      temporal DIF is dominated by genuine capability evolution\\n      (enrichment≈1.0, within-subject C%=38.1%), and three structural\\n      corrections cannot separate them.\\n    mechanism: >-\\n      Semi-synthetic injection into real response matrices provides controlled\\n      ground truth; cross-subject matching eliminates FPR inflation (ΔFPR=0.000).\\n    evidence: >-\\n      38% items functionally unstable (plan_001/014); ΔTPR=+0.508 at p=0.5\\n      (plan_011); ΔFPR=0.000 cross-subject (plan_016); three improvements\\n      exhausted (plan_001b/012/014).\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 200\\n    core_bullets:\\n      - >-\\n        Problem: LLM benchmark scores assume temporal comparability, but\\n        item-level behavior may drift across model generations\\n      - >-\\n        Approach: Apply MH-DIF with ETS classification to METABENCH\\n        (5,227 models × 12,508 MMLU items)\\n      - >-\\n        Finding 1: 38% items functionally unstable across generations —\\n        genuine capability evolution, not statistical artifact (sanity\\n        check 0.18%, within-subject persistence 31-45%)\\n      - >-\\n        Finding 2: Web-overlap contamination labels do not capture\\n        differential contamination (enrichment≈1.0); semi-synthetic\\n        injection confirms DIF detection power (ΔTPR=+0.508 at p=0.5).\\n        Validation methodology gap affects entire field.\\n      - >-\\n        Finding 3: Semi-synthetic validation framework with cross-subject\\n        matching (ΔFPR=0.000) as reusable infrastructure; GSM8K replication\\n        confirms cross-benchmark portability (ΔTPR=+0.818)\\n      - >-\\n        Finding 4: DIF-flagged items concentrate cross-generational\\n        discriminative information — removing them disrupts rankings MORE\\n        than random removal (z=-8 to -49σ), while overall rankings stay\\n        robust (ρ>0.996). Cross-benchmark validation: DIF flags\\n        anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005)\\n        — DIF captures capability-discriminative items, not contamination.\\n        DIF is diagnostic lens, not item filter.\\n    dependencies: [experiments, method, discussion]\\n    registry_refs:\\n      - plan_001_real_data_dif_mmlu\\n      - plan_011_semi_synthetic_validation\\n      - plan_014_within_subject_dif\\n      - plan_016_within_subject_semi_synthetic\\n      - plan_017_downstream_impact\\n      - plan_004_gsm8k_cross_benchmark\\n\\n  - section: introduction\\n    word_budget: 1200\\n    core_bullets:\\n      - >-\\n        Hook: MMLU scores are treated as directly comparable across time —\\n        but 38% of items behave differently for 2024 vs 2023 model cohorts\\n        (ETS C DIF), and this persists within every subject domain\\n      - >-\\n        Gap: Contamination detection research validates against web-overlap\\n        labels, but these measure global exposure, not differential item\\n        functioning — a fundamental validation methodology gap. All work\\n        using web-overlap/n-gram labels as ground truth for item-level\\n        detectors (including Min-K%, n-gram methods) has the same blind\\n        spot.\\n      - >-\\n        Insight: Applying classical psychometric DIF to LLM benchmarks\\n        reveals that item-level behavioral differences are pervasive and\\n        structural — three correction attempts (matched-ability,\\n        θ-conditioning, bifactor pre-check) all fail, pointing to genuine\\n        capability evolution as the dominant source\\n      - >-\\n        Contributions: (C1) Benchmark temporal comparability concern —\\n        38% functional instability as empirical finding; (C2) Ground truth\\n        meta-critique — validation methodology gap in contamination\\n        detection literature; (C3) Semi-synthetic validation framework\\n        with cross-subject matching; (C4) DIF items concentrate\\n        discriminative information — diagnostic lens, not item filter\\n    dependencies: [experiments]\\n    figures: [fig_1_global_vs_differential]\\n    citation_hints:\\n      - \\\"METABENCH dataset citation\\\"\\n      - \\\"Li et al. (EMNLP 2024) web-overlap labels\\\"\\n      - \\\"Wang et al. (ICLR 2026) RL fragility — motivates psychometric approach\\\"\\n      - \\\"Growing Pains (Polo et al.) — positioning: they do score comparability, we do temporal stability characterization\\\"\\n\\n  - section: related_work\\n    word_budget: 800\\n    core_bullets:\\n      - >-\\n        Cluster 1: Contamination detection methods (Min-K%, ConStat, DVD,\\n        Self-Critique, n-gram baselines) — all validate against global\\n        exposure labels, not differential contamination; our meta-critique\\n        applies to their validation methodology\\n      - >-\\n        Cluster 2: IRT in LLM evaluation (Growing Pains, PSN-IRT, Hardy\\n        scalability, Lalor 2019, Vania 2021) — DEDICATED technical\\n        comparison with Growing Pains: they use anchor items for efficient\\n        extensible evaluation; our DIF diagnostic tells them WHICH anchor\\n        items are degrading across model generations. Mutual value: their\\n        framework + our diagnostic = monitored extensible evaluation.\\n        Complementary not competing. (R2-W2)\\n      - >-\\n        Cluster 3: DIF methodology and impact-vs-DIF literature (MH,\\n        ETS classification, Shealy & Stout 1993 SIBTEST, Clauser & Mazor\\n        1998 review, Zumbo 1999, Belzak 2020 small-sample) — our\\n        application context is novel; method itself is established; we\\n        acknowledge the impact-vs-DIF confound as central challenge\\n        (MISSING-REF-1)\\n      - >-\\n        Cluster 4: Benchmark design (LiveBench, dynamic benchmarks) — we\\n        characterize existing benchmarks psychometrically, they build new\\n        contamination-free ones\\n    dependencies: [introduction]\\n\\n  - section: method\\n    word_budget: 1400\\n    core_bullets:\\n      - >-\\n        3.1 Data: METABENCH response matrix (5,227 × 12,508) + Li et al.\\n        web-overlap labels (73.8% coverage, 9,229 items)\\n      - >-\\n        3.2 MH-DIF + ETS A/B/C classification — translate for ML audience:\\n        examinees→models, test items→benchmark questions, DIF→item-level\\n        behavioral anomaly conditional on ability. ETS thresholds: A\\n        (|Δ|<1.0), B (1.0≤|Δ|<1.5), C (|Δ|≥1.5)\\n      - >-\\n        3.3 Cohort designs: temporal (2023 vs 2024, N=1253/656),\\n        ability-quintile (Q1-2 vs Q4-5), within-family (Llama-2 N=161 vs\\n        Llama-3 N=308), within-subject (per-MMLU-subject DIF)\\n      - >-\\n        3.4 Semi-synthetic injection framework: select baseline-clean\\n        items (ETS A in uninjected data), inject contamination by flipping\\n        focal-group incorrect→correct responses at rate p ∈ {0.3,0.5,0.7,1.0},\\n        measure ΔTPR = TPR(injected) - TPR(baseline). Cross-subject\\n        matching: use total score on OTHER subjects as matching variable,\\n        avoiding matching variable contamination.\\n      - >-\\n        3.5 Diagnostics: Yen's Q3 for local independence, domain-specificity\\n        analysis (Spearman ρ between C% and accuracy improvement by subject)\\n    dependencies: []\\n    notation_table:\\n      θ: \\\"latent ability (IRT)\\\"\\n      Δ_MH: \\\"Mantel-Haenszel DIF statistic (log-odds ratio)\\\"\\n      p: \\\"exploitation rate in semi-synthetic injection\\\"\\n      \\\"C%\\\": \\\"percentage of items classified ETS C (large DIF)\\\"\\n      ΔTPR: \\\"TPR increase from injection over baseline\\\"\\n      ΔFPR: \\\"FPR change from injection (should be 0 for valid framework)\\\"\\n\\n  - section: experiments\\n    word_budget: 2500\\n    core_bullets:\\n      - >-\\n        4.1 Validation: DIF works under controlled conditions — power\\n        analysis with real MMLU IRT parameters, ETS C TPR=0.68-0.80 at\\n        N≥80 δ≥1.4, FPR=0.036-0.042, AUC 0.93-0.94\\n      - >-\\n        4.2 Temporal comparability concern: 31.3% ETS C (temporal), sanity\\n        random split 0.18%, within-family Llama-2v3 61.3% (ability\\n        confound), ability-quintile 2.9% (well-controlled), domain ρ=0.307\\n        (p=0.02). Within-subject C%=38.1% (31-45% across 5 subjects) —\\n        instability penetrates within every domain\\n      - >-\\n        4.3 Ground truth mismatch: enrichment=0.96 against Li et al.\\n        web-overlap labels; semi-synthetic ΔTPR=+0.508 (p=0.5), +0.674\\n        (p=1.0), clear dose-response; DIF WORKS for differential\\n        contamination but Li et al. labels are the wrong ground truth\\n      - >-\\n        4.4 Structural analysis — empirical observation that three\\n        structural improvements fail: (a) matched-ability enrichment\\n        0.94-1.04, (b) θ-conditioning r=0.9986 FPR unchanged at 31%,\\n        (c) within-subject pre-check C%=38.1% (bifactor not viable).\\n        Frame as: jointly constraining DIF utility, not formal impossibility\\n      - >-\\n        4.5 Semi-synthetic framework validation: cross-subject matching\\n        ΔFPR=0.000 all 5 subjects, 4/5 ΔTPR>0.3 at p=0.5 (cross), vs\\n        within-subject FPR inflation +0.186. Cross-subject matching as\\n        methodological recommendation.\\n      - >-\\n        4.6 Q3 local independence: 11.3% within-subject pairs >0.20 vs\\n        2.2% cross-subject (5x, p=2.3e-9); mild local dependence,\\n        contributing factor but not main FPR driver\\n      - >-\\n        4.7 Downstream impact — four layers: (1) Benchmark redundancy:\\n        ρ≈0.997 full vs stable-only, rankings extremely robust to 31%\\n        removal; (2) DIF items = discriminative signal carriers: DIF\\n        removal disrupts MORE than random (z=-8 to -49σ, 21/21),\\n        DIF items carry 1.09× cross-cohort swing vs 0.96× stable;\\n        (3) DIF as diagnostic lens: identifies which capability\\n        dimensions drive ranking shifts across generations. Model-specific\\n        patterns (phi-3/llama-3 +700-850, mistral merges -400 to -587)\\n        but caveat: top-50 movers 49/50 \\\"unknown\\\" family;\\n        (4) Cross-benchmark validation: GSM1K contamination gap\\n        anti-correlates with DIF advantage (r=−0.478, p=0.005) —\\n        contaminated models perform WORSE on DIF items, confirming DIF\\n        captures capability not contamination (N=33, partial r=−0.385,\\n        permutation p=0.014).\\n      - >-\\n        4.8 Cross-benchmark validation (GSM8K, 1,319 items × 6,702 models):\\n        Three-part analysis. (a) Temporal DIF: C%=18.9% (standard matching),\\n        sanity 0.3% — instability is lower than MMLU (31.3%) but still\\n        substantial for a single-domain benchmark. (b) Semi-synthetic:\\n        ΔTPR=+0.818 (standard, p=0.7), +0.517 (external, p=0.7); dose-\\n        response confirmed; framework generalizes beyond MMLU.\\n        (c) GSM1K contamination gap correlation: DIF-C items anti-correlate\\n        with contamination gap (r=−0.478, p=0.005; partial r=−0.385\\n        controlling accuracy; permutation p=0.014, N=33). Contaminated\\n        models (Phi, Gemma) perform WORSE on DIF items. DIF captures\\n        capability-discriminative items that contamination cannot fake.\\n    dependencies: []\\n    registry_refs:\\n      - mvp_dif_power_sim\\n      - mvp_dif_power_sim_phase2\\n      - plan_001_real_data_dif_mmlu\\n      - plan_001b_matched_ability_dif\\n      - plan_011_semi_synthetic_validation\\n      - plan_012_irt_theta_conditioning\\n      - plan_013_q3_local_independence\\n      - plan_014_within_subject_dif\\n      - plan_016_within_subject_semi_synthetic\\n      - plan_017_downstream_impact\\n      - plan_004_gsm8k_cross_benchmark\\n    tables: [tab_1_temporal_landscape, tab_2_structural_comparison]\\n    figures: [fig_2_dose_response, fig_3_within_subject_matching, fig_4_downstream_impact, fig_5_gsm8k_cross_benchmark]\\n\\n  - section: discussion\\n    word_budget: 1000\\n    core_bullets:\\n      - >-\\n        5.1 Implications for benchmark temporal comparability: 38%\\n        instability means cross-temporal MMLU scores carry uncontrolled\\n        item-level variance; benchmark designers should monitor DIF as\\n        quality diagnostic\\n      - >-\\n        5.2 Ground truth meta-critique — AGGRESSIVE framing per Director:\\n        all work validating item-level detectors against web-overlap/n-gram\\n        labels has the same validation methodology gap. Web-overlap measures\\n        existence, not differential usage. This is a meta-contribution to\\n        the contamination detection field — not just \\\"DIF and Li et al.\\n        measure different things\\\" but \\\"the field's standard validation\\n        approach is fundamentally mismatched for item-level detection.\\\"\\n      - >-\\n        5.3 Empirical observation on DIF applicability: 1D IRT fit\\n        limitations + power requirements + ability confounding jointly\\n        constrain DIF utility in LLM benchmarks. This is a structural\\n        constraint revealed by systematic experimentation, NOT a formal\\n        impossibility — higher-level methods (MIMIC, propensity-score\\n        matching, multidimensional IRT) may address individual constraints.\\n      - >-\\n        5.4 Limitations — MUST BE HONEST, non-negotiable:\\n        (a) ρ=0.307 means item instability correlates with capability\\n        improvement — \\\"unstable items\\\" may mainly reflect \\\"models got\\n        better at those domains\\\" rather than item-intrinsic problems;\\n        (b) 38% C% cannot be decomposed into contamination vs capability;\\n        (c) semi-synthetic injection (incorrect→correct flipping) may\\n        not match real contamination patterns (partial knowledge, format\\n        memorization);\\n        (d) primarily MMLU/METABENCH — GSM8K cross-validation (§4.8)\\n        confirms semi-synthetic framework portability and provides GSM1K\\n        correlation evidence (N=33), but full temporal DIF characterization\\n        on diverse benchmarks not yet done; GSM1K N=33 has wide CI;\\n        (e) cross-subject baseline FPR 33-53% — stable across injection\\n        levels but not low;\\n        (f) RL robustness: theoretically motivated but empirically\\n        unvalidated with adequate sample size (N=13 reasoning-RL models\\n        in METABENCH);\\n        (g) downstream impact family analysis limited to N≥20 families\\n        (llama, mistral, qwen, phi); top-50 rank movers 49/50 are\\n        \\\"unknown\\\" family — family-level conclusions have limited coverage\\n      - >-\\n        5.5 Future work: ensemble fusion (DIF + ConStat + DVD),\\n        broader cross-benchmark generalization (beyond GSM8K — e.g.\\n        ARC, HellaSwag, coding benchmarks), RL model cohorts with\\n        adequate N, item-focused trees (continuous covariate),\\n        SIBTEST/LR-DIF comparison, MIMIC models, GSM1K-style\\n        controlled item sets for more benchmarks\\n    dependencies: [experiments]\\n\\n  - section: conclusion\\n    word_budget: 350\\n    core_bullets:\\n      - >-\\n        Four contributions: (1) 38% MMLU items functionally unstable\\n        across model generations, (2) ground truth meta-critique —\\n        validation methodology gap in contamination detection, (3)\\n        semi-synthetic framework with cross-subject matching (cross-\\n        benchmark replication on GSM8K: ΔTPR=+0.818), (4) DIF as\\n        diagnostic lens — four-layer finding\\n      - >-\\n        Key message: LLM benchmarks need psychometric monitoring, not\\n        just score reporting — DIF reveals benchmark quality as a\\n        benchmark quality tool\\n      - >-\\n        DIF items concentrate discriminative information (removal disrupts\\n        rankings MORE than random, z=-8 to -49σ) and anti-correlate with\\n        contamination (r=−0.478) — DIF captures genuine capability\\n        differences that contamination cannot replicate\\n    dependencies: [experiments, discussion]\\n\\nvisualization_plan:\\n  - fig_id: fig_1_global_vs_differential\\n    type: conceptual\\n    tool: paperbanana\\n    description: >-\\n      Global vs Differential contamination concept diagram with ICC\\n      illustration — global exposure affects all models equally (no DIF),\\n      differential training data inclusion creates group-specific ICC\\n      shifts (DIF detected). Shows why enrichment≈1.0 is expected.\\n    narrative_intent: >-\\n      Web-overlap labels and DIF measure fundamentally different things:\\n      global exposure vs differential item functioning. Low enrichment is\\n      expected, not failure.\\n    design_notes:\\n      - >-\\n        Left panel: \\\"Global Contamination\\\" — item on Common Crawl since\\n        2020, both cohort ICCs overlap (no DIF), Li et al. labels it\\n        contaminated but DIF correctly reports no group difference\\n      - >-\\n        Right panel: \\\"Differential Contamination\\\" — item in focal\\n        cohort's training data only, ICCs diverge (DIF detected), Li\\n        et al. may or may not label it\\n      - >-\\n        Use ICC curves (S-shaped logistic) with shaded area between\\n        curves = DIF magnitude (Δ_MH)\\n      - \\\"Color: reference cohort blue, focal cohort orange (Okabe-Ito)\\\"\\n      - >-\\n        Bottom annotation connecting panels: \\\"Enrichment ≈ 1.0 because\\n        most MMLU items are globally contaminated (left), not\\n        differentially (right)\\\"\\n    placement: introduction\\n    aspect_ratio: \\\"16:9\\\"\\n\\n  - fig_id: fig_2_dose_response\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Semi-synthetic dose-response: TPR vs exploitation rate p for\\n      temporal cohort with external/cross-subject matching, plus FPR\\n      stability panel\\n    narrative_intent: >-\\n      DIF detection power increases monotonically with contamination\\n      exploitation rate (clear dose-response), and cross-subject matching\\n      maintains perfectly stable FPR (ΔFPR=0.000) — controlled detection\\n      capability confirmed.\\n    design_notes:\\n      - \\\"x-axis: exploitation rate p ∈ {0, 0.3, 0.5, 0.7, 1.0}\\\"\\n      - >-\\n        Top panel: TPR lines — temporal_external (primary, solid blue),\\n        temporal_standard (dashed red, shows FPR inflation problem at\\n        high p)\\n      - >-\\n        Bottom panel (smaller): FPR vs p — external flat at ~0.31\\n        (ΔFPR=0.000), standard inflating from 0.30 to 0.62\\n      - \\\"Pattern A: light regime band at p<0.3 labeled 'below practical detection'\\\"\\n      - \\\"Dashed horizontal lines at baseline TPR (p=0) for reference\\\"\\n      - \\\"Annotate ΔTPR=+0.508 at p=0.5 on the primary line\\\"\\n    data_source: \\\"registry: plan_011_semi_synthetic_validation\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"3:4\\\"\\n\\n  - fig_id: fig_3_within_subject_matching\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Within-subject semi-synthetic: 5 subjects comparing cross-subject\\n      vs within-subject matching on ΔTPR and ΔFPR\\n    narrative_intent: >-\\n      Cross-subject matching eliminates FPR inflation (ΔFPR=0.000 for\\n      all 5 subjects) while maintaining detection power — a practical\\n      methodological recommendation.\\n    design_notes:\\n      - >-\\n        Paired dot plot or grouped bars: 5 subjects on x-axis, sorted\\n        by cross-subject ΔTPR\\n      - >-\\n        Left panel: ΔTPR at p=0.5 — cross (filled circle) vs within\\n        (open circle), connected by line\\n      - >-\\n        Right panel: ΔFPR — cross all at 0.000 (flat line), within\\n        showing inflation (+0.067 to +0.281)\\n      - \\\"Reference line: ΔTPR=0.3 (success threshold), ΔFPR=0\\\"\\n      - >-\\n        Highlight business_ethics: high baseline FPR (0.53-0.56),\\n        negative within-subject ΔTPR, low cross-subject ΔTPR — the\\n        failure case\\n    data_source: \\\"registry: plan_016_within_subject_semi_synthetic\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"3:2\\\"\\n\\n  - fig_id: fig_4_downstream_impact\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Model-level rank change scatter: full-benchmark rank vs\\n      stable-only rank, showing that DIF removal systematically\\n      disrupts rankings more than random removal. Annotate key model\\n      clusters (phi-3/llama-3 beneficiaries, mistral merge losers).\\n    narrative_intent: >-\\n      DIF-flagged items concentrate cross-generational discriminative\\n      information — removing them disrupts rankings MORE than random\\n      removal, revealing model-specific evolution patterns rather than\\n      benchmark noise.\\n    design_notes:\\n      - >-\\n        Scatter plot: x = full-benchmark rank, y = stable-only rank.\\n        Diagonal line (y=x) = no change. Points above = gained rank\\n        (benefited from DIF items), below = lost rank.\\n      - >-\\n        Color by model family or cohort (2023 blue, 2024 orange) if\\n        feasible; otherwise uniform gray with key models highlighted\\n      - >-\\n        Annotate clusters: phi-3 / llama-3 derivatives (large positive\\n        rank change, +700-850), mistral merges (large negative, -400\\n        to -587)\\n      - >-\\n        Inset or annotation box: ρ_full_vs_stable = 0.996, z_dif_vs_random\\n        = -14.9 (mean), DIF items 1.09× cross-cohort ratio\\n      - \\\"Reference diagonal dashed line y=x\\\"\\n      - \\\"Alternative: if scatter too dense, use hexbin or contour\\\"\\n    data_source: \\\"registry: plan_017_downstream_impact\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n\\n  - fig_id: fig_5_gsm1k_dif_correlation\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      GSM1K contamination gap vs DIF advantage scatter: 33 matched models,\\n      showing significant negative correlation (r=−0.478, p=0.005).\\n      Models with higher contamination (GSM8K−GSM1K gap) perform WORSE\\n      on DIF-C items — DIF captures capability, not contamination.\\n    narrative_intent: >-\\n      Cross-benchmark validation of Claim 4's \\\"DIF as diagnostic lens\\\":\\n      contaminated models cannot fake performance on DIF items, which\\n      capture genuine capability-discriminative differences. The negative\\n      correlation inverts the contamination narrative.\\n    design_notes:\\n      - >-\\n        Scatter: x = GSM8K−GSM1K contamination gap, y = DIF advantage\\n        (acc_DIF_C − acc_non_DIF). Regression line with 95% CI band.\\n      - >-\\n        Color by model family (Phi green, Gemma orange, Llama blue,\\n        Mixtral purple, DeepSeek red, Other gray)\\n      - \\\"Annotate: r=−0.478, p=0.005 (partial r=−0.385 ctrl accuracy)\\\"\\n      - \\\"Annotate key outlier: Deepseek-math-7b-rl (near zero on both)\\\"\\n      - >-\\n        Dashed horizontal line at DIF advantage = 0; most models below\\n        (DIF items are harder for all, but contaminated models worse)\\n      - \\\"Already generated by Agent Worker — may need style refinement\\\"\\n    data_source: \\\"registry: plan_004_gsm8k_cross_benchmark, artifacts/plan_004/gsm1k_dif_correlation.csv\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n    source_file: \\\"artifacts/plan_004/fig_gsm1k_dif_correlation.pdf\\\"\\n\\n  - fig_id: fig_A1_subject_heatmap\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Per-subject ETS C percentage for all 57 MMLU subjects (temporal\\n      cohort), showing pervasiveness of item instability\\n    narrative_intent: >-\\n      Item instability is pervasive across all MMLU subjects, not\\n      concentrated in a few — temporal DIF is a benchmark-wide phenomenon.\\n    design_notes:\\n      - \\\"Horizontal bar chart sorted by C%, all 57 subjects\\\"\\n      - >-\\n        Color-coded by domain group (STEM / humanities / social science\\n        / other) to show whether instability clusters by domain\\n      - \\\"Vertical dashed line at overall mean C% (31.3%)\\\"\\n      - >-\\n        Annotate subjects with known capability jumps (e.g.,\\n        abstract_algebra, college_mathematics)\\n    data_source: \\\"registry: plan_001_real_data_dif_mmlu\\\"\\n    placement: appendix\\n    aspect_ratio: \\\"1:2\\\"\\n\\n  - fig_id: fig_A2_q3_distribution\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Q3 residual correlation distribution: within-subject vs\\n      cross-subject pairs\\n    narrative_intent: >-\\n      Local dependence exists (11.3% within-subject pairs exceed 0.20)\\n      but is mild — a contributing factor, not the main FPR driver.\\n    design_notes:\\n      - >-\\n        Overlapping density plot: within-subject Q3 (blue) vs\\n        cross-subject Q3 (orange)\\n      - \\\"Vertical dashed line at |Q3|=0.20 threshold\\\"\\n      - \\\"Annotate: 11.3% vs 2.2% above threshold (5x ratio)\\\"\\n      - \\\"Inset text: Mann-Whitney p=2.3e-9\\\"\\n    data_source: \\\"registry: plan_013_q3_local_independence\\\"\\n    placement: appendix\\n    aspect_ratio: \\\"4:3\\\"\\n\\ntable_plan:\\n  - table_id: tab_1_temporal_landscape\\n    caption: >-\\n      DIF detection results across cohort definitions on METABENCH MMLU\\n      (5,227 models × 12,508 items). ETS C = large DIF (|Δ_MH| ≥ 1.5).\\n    placement: experiments\\n    type: comparison\\n    columns:\\n      - Cohort Definition\\n      - N_ref / N_focal\\n      - \\\"ETS C (%)\\\"\\n      - \\\"FPR (Li clean)\\\"\\n      - Enrichment\\n    data_source: \\\"registry: plan_001_real_data_dif_mmlu, plan_014_within_subject_dif\\\"\\n    notes: >-\\n      Rows: temporal (2023 vs 2024), ability-quintile (Q1-2 vs Q4-5),\\n      within-family (Llama-2 vs Llama-3), random split (sanity check),\\n      within-subject average (5 subjects). Highlight contrast: sanity\\n      0.18% vs temporal 31.3%. Within-subject 38.1% proves instability\\n      penetrates within domains.\\n\\n  - table_id: tab_2_structural_comparison\\n    caption: >-\\n      Three structural improvement attempts and their outcomes. None\\n      reduces temporal baseline FPR below 31%.\\n    placement: experiments\\n    type: comparison\\n    columns:\\n      - Approach\\n      - Mechanism\\n      - Temporal FPR\\n      - \\\"TPR (p=0.5)\\\"\\n      - Outcome\\n    data_source: \\\"registry: plan_001b_matched_ability_dif, plan_012_irt_theta_conditioning, plan_014_within_subject_dif\\\"\\n    notes: >-\\n      Rows: baseline (plan_011 external matching), matched-ability\\n      quintiles (plan_001b), IRT θ-conditioning (plan_012), within-subject\\n      pre-check (plan_014). Frame as \\\"empirical observation revealing\\n      structural constraint\\\" not \\\"our method failed.\\\" Note: higher-level\\n      methods (MIMIC, propensity-score) may address individual constraints.\\n    baseline_row: \\\"Baseline (plan_011 external matching, FPR=0.314, TPR=0.834)\\\"\\n\\n  - table_id: tab_3_gsm8k_comparison\\n    caption: >-\\n      Cross-benchmark comparison: MMLU vs GSM8K on temporal DIF and\\n      semi-synthetic detection. GSM8K replicates key findings on a\\n      single-domain math benchmark (1,319 items × 6,702 models).\\n    placement: experiments\\n    type: comparison\\n    columns:\\n      - Metric\\n      - MMLU (plan_001/011)\\n      - GSM8K (plan_004)\\n    data_source: \\\"registry: plan_001_real_data_dif_mmlu, plan_011_semi_synthetic_validation, plan_004_gsm8k_cross_benchmark\\\"\\n    notes: >-\\n      Rows: Items / Models / Temporal C% / Sanity C% / Semi-synthetic\\n      ΔTPR (standard, p=0.7) / ΔTPR (external, p=0.5) / Baseline FPR\\n      (external) / GSM1K gap correlation (GSM8K only). Highlight: GSM8K\\n      standard ΔTPR=+0.818 vs MMLU external ΔTPR=+0.508. Different\\n      matching strategies make direct comparison nuanced — note in caption.\\n\\n  - table_id: tab_A1_power_analysis\\n    caption: >-\\n      DIF power analysis: ETS C classification performance with real\\n      MMLU IRT parameters across sample sizes and effect sizes.\\n    placement: appendix\\n    type: statistics\\n    columns:\\n      - N per group\\n      - \\\"δ (logits)\\\"\\n      - TPR (ETS C)\\n      - FPR (ETS C)\\n      - AUC (MH)\\n      - AUC (LR)\\n    data_source: \\\"registry: mvp_dif_power_sim, mvp_dif_power_sim_phase2\\\"\\n    notes: >-\\n      Grid: N ∈ {50, 80, 100} × δ ∈ {1.0, 1.2, 1.4, 1.6}. Operational\\n      region: N≥80, δ≥1.4 (TPR 0.68-0.80, FPR 0.036-0.042).\\n\\n  - table_id: tab_A2_within_subject_detail\\n    caption: >-\\n      Per-subject semi-synthetic validation with cross-subject vs\\n      within-subject matching at p=0.5.\\n    placement: appendix\\n    type: comparison\\n    columns:\\n      - Subject\\n      - N items\\n      - \\\"Baseline FPR (cross)\\\"\\n      - \\\"ΔTPR (cross)\\\"\\n      - \\\"Baseline FPR (within)\\\"\\n      - \\\"ΔTPR (within)\\\"\\n      - \\\"ΔFPR (cross)\\\"\\n    data_source: \\\"registry: plan_016_within_subject_semi_synthetic\\\"\\n    notes: >-\\n      5 subjects: business_ethics, human_aging, professional_medicine,\\n      formal_logic, high_school_statistics. Cross-subject ΔFPR=0.000 for\\n      all subjects. business_ethics is failure case (baseline FPR>0.53\\n      both methods).\\n\\nliterature_strategy:\\n  citation_budget: 40\\n  macro_context:\\n    - \\\"LLM benchmark contamination detection and validation methodology\\\"\\n    - \\\"psychometric methods (IRT, DIF) applied to LLM evaluation\\\"\\n    - \\\"benchmark temporal comparability and dynamic evaluation design\\\"\\n  micro_clusters:\\n    - cluster_name: \\\"Contamination Detection Methods\\\"\\n      search_queries:\\n        - \\\"benchmark contamination detection LLM 2024 2025 2026\\\"\\n        - \\\"Min-K++ training data detection language model\\\"\\n        - \\\"ConStat perturbation contamination benchmark\\\"\\n        - \\\"n-gram overlap contamination benchmark LLM\\\"\\n      must_cite:\\n        - \\\"Wang et al. 2026 RL fragility (ICLR 2026)\\\"\\n        - \\\"Liang et al. 2026 DVD generation variance\\\"\\n        - \\\"Tao et al. 2026 Self-Critique (ICLR 2026)\\\"\\n        - \\\"Li et al. EMNLP 2024 web-overlap labels\\\"\\n        - \\\"Shi et al. 2024 Min-K++\\\"\\n        - \\\"Balloccu et al. 2024\\\"\\n      target_count: 10\\n\\n    - cluster_name: \\\"IRT in LLM Evaluation\\\"\\n      search_queries:\\n        - \\\"item response theory LLM evaluation 2024 2025 2026\\\"\\n        - \\\"Growing Pains fixed parameter calibration benchmark\\\"\\n        - \\\"psychometric analysis language model benchmark\\\"\\n      must_cite:\\n        - \\\"Polo et al. 2026 Growing Pains\\\"\\n        - \\\"Polo et al. 2026 PSN-IRT (AAAI)\\\"\\n        - \\\"Hardy et al. 2026 scalability coefficients\\\"\\n        - \\\"Lalor et al. 2019 IRT for NLP\\\"\\n        - \\\"Vania et al. 2021\\\"\\n      target_count: 8\\n\\n    - cluster_name: \\\"DIF Methodology & Impact-vs-DIF\\\"\\n      search_queries:\\n        - \\\"differential item functioning Mantel-Haenszel ETS classification\\\"\\n        - \\\"impact versus DIF Shealy Stout SIBTEST\\\"\\n        - \\\"DIF small sample logistic regression\\\"\\n        - \\\"Zumbo 1999 DIF\\\"\\n      must_cite:\\n        - \\\"Holland & Thayer 1988 MH-DIF\\\"\\n        - \\\"Shealy & Stout 1993 SIBTEST\\\"\\n        - \\\"Clauser & Mazor 1998 DIF review\\\"\\n        - \\\"Zumbo 1999 DIF overview\\\"\\n        - \\\"Belzak 2020 small-sample DIF\\\"\\n        - \\\"Kim & Kolen 2019 fixed parameter calibration\\\"\\n      target_count: 8\\n\\n    - cluster_name: \\\"Benchmark Design & Ground Truth\\\"\\n      search_queries:\\n        - \\\"contamination-free benchmark LLM LiveBench 2025\\\"\\n        - \\\"benchmark ground truth contamination labels validation\\\"\\n        - \\\"GSM1K GSM8K contamination evidence\\\"\\n      must_cite:\\n        - \\\"White et al. 2025 LiveBench (ICLR)\\\"\\n        - \\\"Zhang et al. 2024 GSM1K\\\"\\n        - \\\"METABENCH original paper\\\"\\n      target_count: 6\\n\\n    - cluster_name: \\\"LLM Evaluation Methodology\\\"\\n      search_queries:\\n        - \\\"LLM evaluation methodology benchmark design 2025 2026\\\"\\n        - \\\"MMLU benchmark psychometric analysis\\\"\\n        - \\\"language model evaluation survey\\\"\\n      must_cite: []\\n      target_count: 5\\n\\nwriting_order:\\n  - experiments\\n  - method\\n  - introduction\\n  - related_work\\n  - discussion\\n  - abstract\\n  - conclusion\\n\", \"total_chars\": 31764, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5db62c0a-afd2-461b-bb0f-694f0fc74069",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "3be62c0a-087a-4cb7-aa75-5c7cb140bf52",
  "sourceToolAssistantUUID": "5db62c0a-afd2-461b-bb0f-694f0fc74069",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T02:07:52.921Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Wof6SS535BrA6jNVgqum4b`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3be62c0a-087a-4cb7-aa75-5c7cb140bf52",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu3Y2DAPvDvjuJqcGP7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "077c58a7-fb38-4836-8ca6-fa9fe92b6299",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGe4giE5Tntv8acDdWdmSq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8033,
      "cache_read_input_tokens": 17480,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8033
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 17480,
          "cache_creation_input_tokens": 8033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8033,
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

_source line 18 · 2026-05-21T02:07:52.931Z_

<details><summary>↩ Tool result · `toolu_01Wof6SS535BrA6jNVgqum4b`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml\", \"content\": \"categories:\\n- key: contamination_detection\\n  name: Benchmark Contamination Detection\\n  narrative: Methods for detecting training data contamination in LLM benchmarks,\\n    including RL-robust approaches\\n- key: irt_equating\\n  name: IRT Methodology & Equating\\n  narrative: Item Response Theory models, calibration, equating, and their application\\n    to LLM evaluation\\n- key: benchmark_design\\n  name: Dynamic Benchmark Design\\n  narrative: Approaches for creating contamination-resistant or self-updating benchmarks\\n- key: dif_methodology\\n  name: DIF Statistical Methods\\n  narrative: Differential Item Functioning detection methods, power analysis, and\\n    small-sample strategies\\n- key: item_generation\\n  name: Automated Item Generation\\n  narrative: LLM-based test item generation with difficulty control and psychometric\\n    validation\\nmeta:\\n  last_updated: '2026-05-21T01:40:38.004Z'\\n  total_papers: 16\\npapers:\\n  belzak2020smallsample:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Belzak, W.\\n    bibtex_key: belzak2020smallsample\\n    category: dif_methodology\\n    doi: ''\\n    relevance: Parsimonious logistic regression with sum scores outperforms complex\\n      IRT models for DIF detection in small samples; directly applicable to our N=50-80\\n      model cohorts\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Testing Differential Item Functioning in Small Samples\\n    url: ''\\n    venue: Multivariate Behavioral Research\\n    verified: false\\n    year: 2020\\n  hardy2026scalability:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Hardy, M.\\n    bibtex_key: hardy2026scalability\\n    category: irt_equating\\n    doi: ''\\n    relevance: Nonparametric signed isotonic R2 scalability coefficients outperform\\n      IRT item diagnostics; lightweight pre-filter for item quality before our parametric\\n      calibration\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients\\n    url: https://arxiv.org/abs/2603.24999\\n    venue: arXiv\\n    verified: false\\n    year: 2026\\n  kim2019fpc:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Kim, S.\\n    - Kolen, M.\\n    bibtex_key: kim2019fpc\\n    category: irt_equating\\n    doi: ''\\n    relevance: Fixed-parameter calibration requires only N>=200 vs N>=500 for full\\n      calibration; core methodology for our bifactor IRT equating with anchor items\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data\\n    url: ''\\n    venue: Applied Measurement in Education\\n    verified: false\\n    year: 2019\\n  liang2026dvd:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Liang, R.\\n    bibtex_key: liang2026dvd\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Detects variant contamination via generation variance (AUC 0.73-0.74\\n      vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under\\n      RL training\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'DVD: Detection via Variance of Generation Distribution for Variant Contamination'\\n    url: https://arxiv.org/abs/2601.04895\\n    venue: arXiv\\n    verified: true\\n    year: 2026\\n  polo2026growingpains:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Polo, F.\\n    bibtex_key: polo2026growingpains\\n    category: irt_equating\\n    doi: ''\\n    relevance: Uses multidimensional IRT with fixed-parameter calibration and 100\\n      anchor items for extensible evaluation (rho>=0.9); addresses score comparability\\n      but NOT contamination detection or item regeneration\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter\\n      Calibration'\\n    url: ''\\n    venue: arXiv\\n    verified: false\\n    year: 2026\\n  polo2026psnirt:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Polo, F.\\n    bibtex_key: polo2026psnirt\\n    category: irt_equating\\n    doi: ''\\n    relevance: PSN-IRT analyzes benchmark quality via 4PL IRT; provides published\\n      IRT parameters for MMLU we can use in semi-synthetic validation\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item\\n      Response Theory\\n    url: ''\\n    venue: AAAI 2026\\n    verified: false\\n    year: 2026\\n  tao2026selfcritique:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Tao, Y.\\n    bibtex_key: tao2026selfcritique\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse\\n      detection, but remains individual-model-level; our DIF is group-level and complementary\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: Detecting Data Contamination from Reinforcement Learning Post-training\\n      for Large Language Models\\n    url: https://arxiv.org/abs/2510.09259\\n    venue: ICLR 2026\\n    verified: true\\n    year: 2026\\n  wang2026fragility:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Wang, H.\\n    - Li, H.\\n    - Ko, B.\\n    - Zhang, H.\\n    bibtex_key: wang2026fragility\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Proves GRPO/PPO RL training conceals contamination signals (14-20pp\\n      AUROC degradation), motivating our DIF-based approach which operates on behavioral\\n      patterns immune to NLL smoothing\\n    role: foundation\\n    semantic_scholar_id: 9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3\\n    title: On The Fragility of Benchmark Contamination Detection in Reasoning Models\\n    url: https://arxiv.org/abs/2510.02386\\n    venue: ICLR 2026\\n    verified: true\\n    year: 2026\\n  white2025livebench:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - White, C.\\n    bibtex_key: white2025livebench\\n    category: benchmark_design\\n    doi: ''\\n    relevance: Monthly-updated contamination-free benchmark with objective scoring;\\n      no difficulty calibration or psychometric equivalence across updates\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'LiveBench: A Challenging, Contamination-Free LLM Benchmark'\\n    url: ''\\n    venue: ICLR 2025\\n    verified: false\\n    year: 2025\\n  zhang2024gsm1k:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Zhang, H.\\n    bibtex_key: zhang2024gsm1k\\n    category: contamination_detection\\n    doi: ''\\n    relevance: GSM1K documents 10-13% average accuracy drops from contamination; provides\\n      ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4\\n      logits) critical for our DIF power analysis\\n    role: foundation\\n    semantic_scholar_id: ef62f95c16f668f031d649799cbd79081c6d2b0f\\n    title: A Careful Examination of Large Language Model Performance on Grade School\\n      Arithmetic\\n    url: https://arxiv.org/abs/2405.00332\\n    venue: arXiv\\n    verified: true\\n    year: 2024\\n  li2024contamination:\\n    title: An Open-Source Data Contamination Report for Large Language Models\\n    authors:\\n    - Li, Y.\\n    - Guo, Y.\\n    - Guerin, F.\\n    - Lin, C.\\n    year: 2024\\n    venue: Findings of EMNLP 2024\\n    url: https://aclanthology.org/2024.findings-emnlp.30/\\n    doi: 10.18653/v1/2024.findings-emnlp.30\\n    bibtex_key: li2024contamination\\n    category: contamination_detection\\n    role: foundation\\n    relevance: Provides web-overlap contamination labels for MMLU and other benchmarks\\n      via Common Crawl matching; primary ground-truth comparison for our DIF-based\\n      contamination detection\\n    abstract: ''\\n    semantic_scholar_id: 32e11cf020021c225782a3b77b5cfed4ae8e14a0\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  shi2024mink:\\n    title: Detecting Pretraining Data from Large Language Models\\n    authors:\\n    - Shi, W.\\n    - Ajith, A.\\n    - Xia, M.\\n    - Huang, Y.\\n    - Liu, D.\\n    - Blevins, T.\\n    - Chen, D.\\n    - Zettlemoyer, L.\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2310.16789\\n    doi: ''\\n    bibtex_key: shi2024mink\\n    category: contamination_detection\\n    role: foundation\\n    relevance: Introduces Min-K% Prob method and WikiMIA benchmark for pretraining\\n      data detection; key baseline whose limitations under RL training motivate our\\n      DIF-based alternative\\n    abstract: ''\\n    semantic_scholar_id: 3422d5e0cdfdc935d6a84a1e3d3f96659265fe3a\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  balloccu2024leak:\\n    title: 'Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in\\n      Closed-Source LLMs'\\n    authors:\\n    - Balloccu, S.\\n    - Schmidtova, P.\\n    - Lango, M.\\n    - Dusek, O.\\n    year: 2024\\n    venue: EACL 2024\\n    url: https://arxiv.org/abs/2402.03927\\n    doi: 10.18653/v1/2024.eacl-long.5\\n    bibtex_key: balloccu2024leak\\n    category: contamination_detection\\n    role: foundation\\n    relevance: Systematic survey of data leakage in closed-source LLMs covering 255\\n      papers and 263 benchmarks; establishes scope of contamination problem motivating\\n      our detection approach\\n    abstract: ''\\n    semantic_scholar_id: 798feda076ad710df65d509a7884bd15937c8056\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  dekoninck2024constat:\\n    title: 'ConStat: Performance-Based Contamination Detection in Large Language Models'\\n    authors:\\n    - Dekoninck, J.\\n    - Mueller, M. N.\\n    - Vechev, M.\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: https://arxiv.org/abs/2405.16281\\n    doi: ''\\n    bibtex_key: dekoninck2024constat\\n    category: contamination_detection\\n    role: direct-competitor\\n    relevance: Performance-based contamination detection via perturbation analysis;\\n      closest methodological parallel to our DIF approach in using behavioral patterns\\n      rather than memorization signals\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  golchin2024timetravel:\\n    title: 'Time Travel in LLMs: Tracing Data Contamination in Large Language Models'\\n    authors:\\n    - Golchin, S.\\n    - Surdeanu, M.\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2308.08493\\n    doi: ''\\n    bibtex_key: golchin2024timetravel\\n    category: contamination_detection\\n    role: method-component\\n    relevance: Instance-level contamination detection via guided completion prompts;\\n      baseline approach for individual-item detection that our group-level DIF method\\n      extends\\n    abstract: ''\\n    semantic_scholar_id: d6d0fd994f37b630f35945736b5e1bb198148404\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  zhang2024minkpp:\\n    title: 'Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large\\n      Language Models'\\n    authors:\\n    - Zhang, J.\\n    - Sun, J.\\n    - Yeats, E.\\n    - Ouyang, Y.\\n    - Kuo, M.\\n    - Zhang, J.\\n    - Yang, H.\\n    - Li, H.\\n    year: 2024\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2404.02936\\n    doi: ''\\n    bibtex_key: zhang2024minkpp\\n    category: contamination_detection\\n    role: direct-competitor\\n    relevance: Improves Min-K% with vocabulary-normalized token probabilities; key\\n      baseline whose AUC degrades to 0.43-0.68 on RL-trained models, motivating our\\n      DIF-based alternative\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n\", \"total_chars\": 11927, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "077c58a7-fb38-4836-8ca6-fa9fe92b6299",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "b4d775db-69ee-4b56-8e06-f3edbd8fd436",
  "sourceToolAssistantUUID": "077c58a7-fb38-4836-8ca6-fa9fe92b6299",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-21T02:07:55.910Z_

Now let me read the actual paper artifacts and experiment results for deeper analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4d775db-69ee-4b56-8e06-f3edbd8fd436",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu3xdoLvweKngzqtmBB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "feaa0213-de8d-4971-bd97-ae47116a1ccd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWiyGuk8RvUE9Eq3rFUY9Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18912,
      "cache_read_input_tokens": 25513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18912,
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

_source line 20 · 2026-05-21T02:07:58.296Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SS4UV1K955pvsmXAAARmVd`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "feaa0213-de8d-4971-bd97-ae47116a1ccd",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu3xdoLvweKngzqtmBB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f78d231-772d-47a6-a5d0-c0cf6806c455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWiyGuk8RvUE9Eq3rFUY9Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18912,
      "cache_read_input_tokens": 25513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18912,
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

_source line 21 · 2026-05-21T02:07:58.320Z_

<details><summary>↩ Tool result · `toolu_01SS4UV1K955pvsmXAAARmVd`</summary>

```text
artifacts/dream_reports/dream_20260520T194223/best/paper.tex
artifacts/dream_reports/dream_20260520T194223/median/paper.tex
artifacts/dream_reports/dream_20260520T194223/worst/paper.tex
artifacts/dream_reports/dream_20260520T205007/best/paper.tex
artifacts/dream_reports/dream_20260520T205007/median/paper.tex
artifacts/dream_reports/dream_20260520T205007/worst/paper.tex
artifacts/dream_reports/dream_20260521T012912/best/paper.tex
artifacts/dream_reports/dream_20260521T012912/median/paper.tex
artifacts/dream_reports/dream_20260521T012912/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f78d231-772d-47a6-a5d0-c0cf6806c455",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "c0c4cd01-45cb-4a87-8681-23c004dd1d7d",
  "sourceToolAssistantUUID": "1f78d231-772d-47a6-a5d0-c0cf6806c455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T02:07:58.702Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Ps8Q12Hg4Fd62QkgipxLPt`</summary>

```json
{
  "pattern": "**/artifacts/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0c4cd01-45cb-4a87-8681-23c004dd1d7d",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu3xdoLvweKngzqtmBB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25a1f9e5-af93-4a27-9861-667c19737ef5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWiyGuk8RvUE9Eq3rFUY9Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18912,
      "cache_read_input_tokens": 25513,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18912
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 25513,
          "cache_creation_input_tokens": 18912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18912,
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

_source line 23 · 2026-05-21T02:07:58.752Z_

<details><summary>↩ Tool result · `toolu_01Ps8Q12Hg4Fd62QkgipxLPt`</summary>

```text
artifacts/_project/report/metabench_data_summary.md
artifacts/_project/report/metabench_data_summary_ec3bbf.md
artifacts/dream_reports/dream_20260520T194223/best/paper_framing.md
artifacts/dream_reports/dream_20260520T194223/median/paper_framing.md
artifacts/dream_reports/dream_20260520T194223/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T194223/best/review_report.md
artifacts/dream_reports/dream_20260520T194223/median/review_report.md
artifacts/dream_reports/dream_20260520T194223/worst/review_report.md
artifacts/_project/report/irt_scale_analysis.md
artifacts/irt_scale_analysis.md
artifacts/_project/report/mmlu_cf_analysis.md
artifacts/mmlu_cf_analysis.md
artifacts/metabench_data_summary.md
artifacts/dream_reports/dream_20260520T205007/best/paper_framing.md
artifacts/plan_001/plan_001_report.md
artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md
artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report_00ca1f.md
artifacts/dream_reports/dream_20260520T205007/median/paper_framing.md
artifacts/dream_reports/dream_20260520T205007/worst/paper_framing.md
artifacts/plan_001b/report/plan_001b_report.md
artifacts/plan_001b/plan_001b_report.md
artifacts/dream_reports/dream_20260520T205007/best/review_report.md
artifacts/dream_reports/dream_20260520T205007/median/review_report.md
artifacts/dream_reports/dream_20260520T205007/worst/review_report.md
artifacts/plan_011/plan_011_report.md
artifacts/plan_011_semi_synthetic_validation/report/plan_011_report_c7ae89.md
artifacts/plan_011_semi_synthetic_validation/report/plan_011_report.md
artifacts/review_reports/round_0.md
artifacts/_project/report/plan_012_report.md
artifacts/plan_012_irt_theta_conditioning/report/plan_012_report.md
artifacts/plan_012/plan_012_report.md
artifacts/_project/report/plan_014_report.md
artifacts/plan_014/plan_014_report.md
artifacts/_project/report/plan_013_report.md
artifacts/plan_013_q3_local_independence/report/plan_013_report.md
artifacts/plan_013/plan_013_report.md
artifacts/_project/report/plan_016_report.md
artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md
artifacts/plan_016/plan_016_report.md
artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md
artifacts/_project/report/literature_survey_d011.md
artifacts/_project/report/experiment_summary.md
artifacts/experiment_summary.md
artifacts/_project/report/artifacts_qc_report.md
artifacts/artifacts_qc_report.md
artifacts/_project/report/literature_survey_d011_167b57.md
artifacts/literature_survey_d011.md
artifacts/plan_017/plan_017_report.md
artifacts/plan_017/report/plan_017_report.md
artifacts/_project/report/plan_004_data_availability.md
artifacts/plan_004_data_availability.md
artifacts/_project/report/plan_004_step1_report.md
artifacts/plan_004/plan_004_step1_report.md
artifacts/_project/report/plan_004_step2_report.md
artifacts/plan_004/plan_004_step2_report.md
artifacts/_project/report/gsm1k_data_report.md
artifacts/plan_004/gsm1k_data_report.md
artifacts/_project/report/plan_004_step3_report.md
artifacts/plan_004/plan_004_step3_report.md
artifacts/dream_reports/dream_20260521T012912/best/paper_framing.md
artifacts/dream_reports/dream_20260521T012912/median/paper_framing.md
artifacts/dream_reports/dream_20260521T012912/worst/paper_framing.md
artifacts/dream_reports/dream_20260521T012912/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25a1f9e5-af93-4a27-9861-667c19737ef5",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "a06f5826-c898-4bd9-8704-f0042ccf0f34",
  "sourceToolAssistantUUID": "25a1f9e5-af93-4a27-9861-667c19737ef5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T02:08:03.128Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AZPWmea6fMvZAp2N7E8h7E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/best/review_report.md",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a06f5826-c898-4bd9-8704-f0042ccf0f34",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu4PKMju9gaJjSUoHRK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "183ccb7b-1c8d-497b-9639-8019fe2a3636",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REZ3kxt5rq5Zsq93U1vfZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1607,
      "cache_read_input_tokens": 44425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1607,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 25 · 2026-05-21T02:08:03.136Z_

<details><summary>↩ Tool result · `toolu_01AZPWmea6fMvZAp2N7E8h7E`</summary>

```text
1	---
2	dream_id: dream_20260521T012912
3	tier: best
4	overall_score: borderline reject
5	timestamp: 2026-05-21T02:06:00.324128+00:00
6	---
7	
8	# Dream Review Report: Psychometric Characterization of Item Instability in LLM Benchmarks
9	
10	**Paper**: Psychometric Characterization of Item Instability in LLM Benchmarks: A Large-Scale Differential Item Functioning Analysis of MMLU  
11	**Review mode**: Full (2-reviewer roundtable)  
12	**Date**: 2026-05-21  
13	**Venue standard**: Top ML venue, ~25% acceptance, 6-point scale
14	
15	---
16	
17	## Roundtable Summary
18	
19	Two reviewers independently scored the paper **4/6** (Weak Accept). After cross-sharing and discussion, R1 revised down to **3/6** (Weak Reject) citing novelty gaps and the undermined central narrative (ρ=0.307 suggests instability is partly capability improvement). R2 held at **4/6** but acknowledged the paper needs major revision. The consensus is **Borderline Reject (3–4/6)** — the paper addresses an important problem with commendable experimental rigor and intellectual honesty, but methodological gaps, limited novelty, and an underdeveloped central narrative prevent acceptance in current form.
20	
21	---
22	
23	## Final Scores
24	
25	| Dimension | R1 | R2 | Consensus |
26	|---|---|---|---|
27	| Soundness | 3/4 | — | 3/4 |
28	| Empirical Rigor | 3/4 | — | 3/4 |
29	| Novelty | — | 2/4 | 2/4 |
30	| Significance | — | 3/4 | 3/4 |
31	| Clarity | — | 3/4 | 3/4 |
32	| **Overall** | **3/6** | **4/6** | **3.5/6 (Borderline Reject)** |
33	| Confidence | 4/5 | 4/5 | 4/5 |
34	
35	---
36	
37	## Strengths (Consensus)
38	
39	1. **Scale and ambition.** The largest psychometric analysis of an LLM benchmark to date (5,227 models × 12,508 items). The transfer of DIF methodology to this domain is non-trivial and the execution is systematic.
40	
41	2. **Ground truth meta-critique (Claim 2).** The observation that web-overlap contamination labels measure global exposure, not differential functioning, is the paper's strongest conceptual contribution. It affects the validation methodology of Min-K%, ConStat, DVD, and all work using web-overlap as item-level ground truth. Both reviewers consider this independently valuable.
42	
43	3. **Semi-synthetic validation framework (Claim 3).** The cross-subject matching innovation (ΔFPR = 0.000) is a clean, practical methodological contribution. The insight that matching on within-subject total score contaminates the matching variable is subtle and empirically well-demonstrated.
44	
45	4. **Thorough controls and honest reporting.** Random-split sanity checks (C% = 0.18% vs. temporal 31.3%), architecture-stratified analysis (C% drops to 22.1% with improved IRT fit), dose-response curves, permutation tests, and leave-one-out robustness analyses. The transparent treatment of negative results (three structural corrections failed) is above average for the venue.
46	
47	5. **DIF as diagnostic lens (Claim 4).** Supported by two independent evidence lines: (a) DIF item removal disrupts rankings more than random removal (z = −8 to −49σ), and (b) DIF flags anti-correlate with GSM1K contamination gaps (r = −0.478, p = 0.005). This reframing from "find bad items" to "understand what changed" is well-argued.
48	
49	6. **Architecture stratification (§4.3).** Transforms a potential fatal objection into a practical recommendation. The 29% C% reduction with dramatically improved IRT fit (RMSEA 0.082 → 0.037) is the paper's most methodologically satisfying experiment.
50	
51	---
52	
53	## Weaknesses (Consensus)
54	
55	### Critical Issues
56	
57	1. **ETS threshold uncalibrated for LLM populations (both reviewers).** The |Δ_MH| ≥ 1.5 threshold for ETS C classification is borrowed directly from human educational testing without calibration or sensitivity analysis. The 38% headline number is anchored to this arbitrary cutoff. If the threshold were 2.0, the finding would change substantially. **The paper must report C% at multiple thresholds (e.g., 1.0, 1.5, 2.0, 2.5) to demonstrate qualitative robustness.** This is the single most important missing analysis.
58	
59	2. **ρ = 0.307 undermines the central narrative (both reviewers).** The correlation between C% and subject-level accuracy improvement suggests a substantial fraction of "instability" is models genuinely getting better at specific domains. The paper frames this honestly but does not adequately decompose capability-improvement DIF from genuine measurement anomaly DIF. A partial correlation or regression decomposition is needed. Without it, a reviewer can reasonably ask: if "instability" is mostly "progress," is this a comparability concern or just evidence that benchmarks are working?
60	
61	3. **Missing related work (R2, endorsed by R1).** The paper omits several directly relevant lines of work:
62	   - Measurement invariance literature (Meredith 1993, Vandenberg & Lance 2000) — DIF is a special case of scalar invariance testing
63	   - MIMIC models (Muthén 1985, Woods 2009) — handles continuous covariates, directly addresses θ-conditioning failure
64	   - Propensity score matching for DIF (Teresi et al. 2007) — addresses impact-vs-DIF confounding
65	   - IRT-based DIF methods (Lord's χ², Raju's area) — no justification for MH over these alternatives
66	   - PSN-IRT (Polo et al., AAAI 2026) — concurrent work applying IRT to MMLU
67	   - Wang et al. (2026) on RL contamination fragility — directly relevant to RL robustness discussion
68	   - Tao et al. (2026) on detecting contamination from RL post-training
69	   
70	   For a paper claiming to bridge psychometrics and ML evaluation, the psychometric literature coverage is surprisingly thin.
71	
72	4. **No algorithmic novelty (R2, partially contested by R1).** The core method is off-the-shelf MH-DIF applied to a binary response matrix — a direct application of a 40-year-old technique. The novelty is empirical (findings) and methodological (framework design), not algorithmic. R1 argues application novelty is legitimate; R2 considers it borderline for a top venue main track. Consensus: the novelty is real but modest, and the paper should be more explicit that its contribution is empirical characterization, not methodological innovation.
73	
74	### Major Issues
75	
76	5. **Multiple testing not addressed (R1, endorsed by R2).** 12,508 simultaneous MH tests with no Bonferroni, FDR, or other correction. The ETS classification's dual requirement (effect size + significance) likely controls this, but the argument is never made explicit. This needs at minimum a paragraph of discussion.
77	
78	6. **Only uniform DIF detected (R1, endorsed by R2).** MH detects only constant difficulty shifts across ability levels. Non-uniform DIF — where contamination varies by model ability — is plausible (stronger models more likely to have seen specific items) and would be missed entirely. No comparison with logistic regression DIF or SIBTEST is provided.
79	
80	7. **RL robustness severely underpowered (both reviewers).** N = 13 reasoning-RL models is insufficient to support the "RL robustness" claim. The comparison with per-model detectors (Min-K%, ConStat) is apples-to-oranges: DIF operates at group level and is inherently less sensitive to individual model additions. The paper appropriately places this in the appendix but overclaims in §6 Discussion.
81	
82	8. **Semi-synthetic injection oversimplified (both reviewers).** Flipping incorrect to correct responses at rate p assumes contamination manifests as deterministic answer knowledge. Real contamination may involve partial knowledge, distractor elimination, or format memorization. The ΔTPR numbers may overestimate detection power against realistic contamination patterns.
83	
84	9. **Cumulative Bayesian DIF speculative (both reviewers).** §5.3 introduces a Bayesian DIF accumulation framework that is entirely simulated with no validation on actual METABENCH temporal data. Insufficient methodological detail (prior specification, batch ordering sensitivity, threshold sensitivity). Feels like a separate, underdeveloped contribution stapled onto the paper.
85	
86	### Minor Issues
87	
88	10. **GSM1K validation sample size.** N = 33 matched models with wide confidence interval (~[−0.70, −0.17] at 95%). The anti-correlation finding is directionally convincing but imprecise.
89	
90	11. **Bifactor TLI = 0.89** is below the conventional 0.90 acceptability threshold, yet equating results from this model are presented without adequate caveat.
91	
92	12. **Paper scope too broad.** Four claims + architecture stratification + structural constraints + Bayesian DIF + RL robustness + cross-benchmark validation + future work with pilot results (Tables 7–11). Each receives insufficient depth. The Future Work section is disproportionately long with preliminary numbers that feel like padding.
93	
94	13. **Growing Pains comparison not empirically tested.** The paper claims DIF "complements" Growing Pains' anchor-item approach but does not test C% among Growing Pains' specific anchor items.
95	
96	---
97	
98	## Questions for Authors
99	
100	1. What is C% at alternative ETS thresholds (|Δ_MH| ≥ 1.0, 1.5, 2.0, 2.5)? Does the qualitative finding (>20% instability) survive across thresholds?
101	
102	2. If you partial out accuracy improvement from C%, what fraction of the 38% instability remains unexplained by capability gains?
103	
104	3. Why MH-DIF specifically rather than logistic regression DIF, which naturally accommodates continuous covariates and would have avoided the θ-conditioning failure?
105	
106	4. For cross-subject matching ΔFPR = 0.000: is this exactly zero or rounded? Across how many injection levels and seeds?
107	
108	5. What drives the 9.2pp C% reduction in architecture stratification — removal of non-decoder models, or the smaller sample size (3,847 vs. 5,227)?
109	
110	6. What is the C% among Growing Pains' specific anchor items?
111	
112	7. For Cumulative Bayesian DIF: how sensitive is TPR/FPR to the Bayes factor threshold (2.0 vs. 3.2 vs. 5.0)?
113	
114	8. How does restricting to models above a minimum accuracy threshold affect C%? Very weak models (near-random) may inflate DIF statistics.
115	
116	---
117	
118	## Experiment Coverage Assessment
119	
120	**Executed and included in paper:**
121	- Core temporal DIF analysis — ✅ Main text §4.1
122	- Architecture-stratified DIF (plan_010) — ✅ Main text §4.3, strong
123	- Semi-synthetic validation — ✅ Main text §4.4
124	- Structural constraints / bifactor (plan_005 partial) — ✅ §4.5
125	- Benchmark redundancy / diagnostic lens (plan_017) — ✅ §5.1
126	- Cross-benchmark GSM8K validation — ✅ §5.2
127	- Cumulative Bayesian DIF (plan_007) — ✅ §5.3, underdeveloped
128	- RL robustness (plan_002) — ✅ Appendix A, underpowered (N=13)
129	- Item-Focused Trees (plan_009) — ✅ Appendix B
130	
131	**Dropped but pilot results reported in Future Work:**
132	- ConStat (plan_003a) — Table 8
133	- DVD (plan_003b) — Table 9
134	- Ensemble fusion (plan_003c) — Table 7
135	- Item generation (plan_006) — Table 11
136	- Graceful degradation (plan_008) — Table 10
137	
138	The paper covers the core experiments adequately. The dropped experiments are appropriately positioned as future work. The main coverage gap is not missing experiments but missing **sensitivity analyses** on the experiments that were run (threshold sensitivity, temporal boundary sensitivity, model quality filtering).
139	
140	---
141	
142	## Recommendations for Revision
143	
144	**Must-fix for resubmission:**
145	1. Add ETS threshold sensitivity analysis (C% at multiple cutoffs)
146	2. Decompose instability: partial out capability improvement from C%
147	3. Expand related work with measurement invariance, MIMIC, IRT-based DIF alternatives
148	4. Add multiple testing discussion
149	5. Either strengthen RL robustness with more models or downgrade claims to "preliminary observation"
150	
151	**Strongly recommended:**
152	6. Include at least one non-uniform DIF method comparison (logistic regression DIF)
153	7. Tighten scope: move Bayesian DIF and some Future Work tables to supplementary
154	8. Test C% among Growing Pains anchor items
155	9. Add one more benchmark beyond MMLU and GSM8K
156	
157	**If space permits:**
158	10. Discuss alternative injection mechanisms and their implications for ΔTPR estimates
159	11. Report model quality filtering sensitivity
160	12. Report temporal boundary sensitivity
161	
162	---
163	
164	## Final Verdict
165	
166	**Borderline Reject (3.5/6).** The paper tackles an important problem — whether LLM benchmark scores remain comparable across model generations — and brings rigorous psychometric methodology to bear on it at unprecedented scale. The ground truth meta-critique, cross-subject matching innovation, and architecture stratification analysis are genuine contributions. However, the 38% headline finding rests on an uncalibrated threshold with no sensitivity analysis, the central narrative is partially undermined by the capability-improvement correlation (ρ = 0.307), the related work has significant gaps, and the paper overextends by trying to present too many results without sufficient depth on any. With a focused revision addressing threshold sensitivity, instability decomposition, and related work coverage, this could become a solid contribution. In current form, the methodological gaps and limited novelty place it below the acceptance threshold for a top ML venue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "183ccb7b-1c8d-497b-9639-8019fe2a3636",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "4c47d0cc-a287-4fe6-95f2-d5aefd14efcf",
  "sourceToolAssistantUUID": "183ccb7b-1c8d-497b-9639-8019fe2a3636",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T02:08:04.179Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FTaGK1UpMspVzLMQKf2coF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/best/paper.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c47d0cc-a287-4fe6-95f2-d5aefd14efcf",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu4PKMju9gaJjSUoHRK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "889c8ed9-8df7-4041-a6f7-dfa9a06e06e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REZ3kxt5rq5Zsq93U1vfZq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1607,
      "cache_read_input_tokens": 44425,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1607
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 229,
          "cache_read_input_tokens": 44425,
          "cache_creation_input_tokens": 1607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1607,
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

_source line 27 · 2026-05-21T02:08:04.447Z_

<details><summary>↩ Tool result · `toolu_01FTaGK1UpMspVzLMQKf2coF`</summary>

```text
1	\documentclass{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[margin=1in]{geometry}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{hyperref}
9	\usepackage{natbib}
10	\usepackage{xcolor}
11	\usepackage{tabularx}
12	\usepackage{caption}
13	
14	\title{Psychometric Characterization of Item Instability in LLM Benchmarks:\\A Large-Scale Differential Item Functioning Analysis of MMLU}
15	
16	\author{
17	Anonymous Authors
18	}
19	
20	\date{}
21	
22	\begin{document}
23	\maketitle
24	
25	% ============================================================
26	% ABSTRACT
27	% ============================================================
28	\begin{abstract}
29	LLM benchmarks implicitly assume temporal score comparability---that a score of 80\% today measures the same construct as 80\% a year ago. We challenge this assumption by applying Differential Item Functioning (DIF) analysis, a classical psychometric tool, to the METABENCH response matrix (5{,}227 models $\times$ 12{,}508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date. We report four findings. \textbf{First}, 38\% of MMLU items are functionally unstable across model generations (ETS C category, $|\Delta_{\text{MH}}| \geq 1.5$), persisting within every subject domain (per-subject C\% = 31--45\%). \textbf{Second}, the field's standard validation approach---web-overlap contamination labels---cannot capture this differential signal (enrichment $\approx 1.0$), while semi-synthetic injection confirms detection capability ($\Delta\text{TPR} = +0.508$ on MMLU, $+0.818$ on GSM8K). \textbf{Third}, we provide a reusable semi-synthetic validation framework with cross-subject matching that eliminates false positive inflation ($\Delta\text{FPR} = 0.000$). \textbf{Fourth}, DIF items concentrate discriminative signal rather than noise: their removal disrupts rankings more than random removal ($z = -8$ to $-49\sigma$), and DIF flags anti-correlate with contamination on GSM8K ($r = -0.478$, $p = 0.005$). Architecture stratification reduces spurious flags by 29\% (C\% from 31.3\% to 22.1\%) while confirming that substantial genuine instability persists, demonstrating the method is refinable rather than fundamentally confounded. We release the semi-synthetic framework and DIF diagnostics as open infrastructure for benchmark maintenance.
30	\end{abstract}
31	
32	% ============================================================
33	% 1. INTRODUCTION
34	% ============================================================
35	\section{Introduction}
36	\label{sec:intro}
37	
38	When we state that ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent construct---that the 12{,}508 items function identically regardless of when or by which model they are answered. This assumption of \emph{temporal score comparability} underpins every leaderboard ranking, every benchmark-based paper claim, and every policy decision that cites benchmark performance.
39	
40	But do MMLU items function the same across model generations? As models improve through successive training paradigms---scaling, instruction tuning, RLHF, reasoning-chain RL---the population of test-takers changes dramatically. In classical psychometrics, when a test item functions differently across groups (e.g., producing different correct-response probabilities at matched ability levels), the item exhibits \emph{Differential Item Functioning} (DIF). DIF does not mean an item is ``bad''---it means the item's measurement properties are group-dependent, threatening the comparability of scores derived from that item.
41	
42	We apply DIF analysis to the METABENCH response matrix \citep{metabench2024}, comprising 5{,}227 models evaluated on 12{,}508 MMLU items. This constitutes the largest-scale psychometric analysis of an LLM benchmark to date. Our analysis yields four contributions:
43	
44	\begin{enumerate}
45	    \item \textbf{Temporal instability characterization.} 38\% of MMLU items exhibit large DIF (ETS C category) between 2023 and 2024-H1 model cohorts. This persists within every subject domain (31--45\% per subject, mean 38.1\%) and survives architecture stratification (22.1\% within decoder-only models alone). The instability correlates with domain-specific accuracy improvement ($\rho = 0.307$, $p = 0.02$), suggesting it reflects genuine capability shifts rather than pure noise.
46	
47	    \item \textbf{Ground truth meta-critique.} Web-overlap contamination labels \citep{li2024contamination} measure global exposure---whether an item is publicly accessible---not differential contamination. DIF enrichment $\approx 1.0$ against these labels is expected, not failure. Semi-synthetic injection confirms DIF detection capability ($\Delta\text{TPR} = +0.508$). This blind spot affects all work validating item-level detectors against web-overlap ground truth.
48	
49	    \item \textbf{Semi-synthetic validation framework.} We introduce a $\Delta$TPR methodology that injects controlled differential contamination into real response matrices. Cross-subject matching (using total score on \emph{other} subjects as the Mantel-Haenszel matching variable) eliminates FPR inflation ($\Delta\text{FPR} = 0.000$ across 5 tested subjects), while within-subject matching suffers from matching variable contamination (+0.186 FPR inflation). The framework generalizes to GSM8K ($\Delta\text{TPR} = +0.818$).
50	
51	    \item \textbf{DIF as diagnostic lens.} MMLU rankings exhibit massive redundancy ($\rho \approx 0.997$ after 31\% item removal), yet DIF items concentrate discriminative signal: their removal disrupts rankings significantly more than random removal ($z = -8$ to $-49\sigma$). Cross-benchmark validation on GSM8K confirms DIF flags anti-correlate with contamination gaps ($r = -0.478$, $p = 0.005$)---contaminated models perform \emph{worse} on DIF items, which capture genuine capability differences.
52	\end{enumerate}
53	
54	Architecture-stratified analysis (Section~\ref{sec:arch_strat}) demonstrates that restricting DIF to decoder-only models reduces C\% from 31.3\% to 22.1\%---a 29\% reduction---while improving IRT model fit (RMSEA from 0.082 to 0.037). This transforms the ``architecture confounding'' objection into a practical recommendation: run DIF within architecture-homogeneous subpopulations.
55	
56	
57	% ============================================================
58	% 2. RELATED WORK
59	% ============================================================
60	\section{Related Work}
61	\label{sec:related}
62	
63	\paragraph{Benchmark contamination detection.}
64	Contamination detection methods broadly fall into two categories. \emph{Per-model} approaches analyze individual model outputs: Min-K\% \citep{shi2024mink} uses minimum $k$-th percentile log-likelihood as a memorization signal; ConStat \citep{constat2024} compares performance on original versus semantically reformulated items; DVD \citep{dvd2024} measures generation variance under temperature sampling to detect bimodal memorization signatures. These methods share a reliance on web-overlap or n-gram labels for validation---a gap we characterize in Section~\ref{sec:meta_critique}. Preliminary evaluation of ConStat on MMLU shows AUROC of 0.73 on non-RL models but degradation to 0.44 on RL models, with low correlation to DIF flags ($r = 0.21$), confirming orthogonal detection axes. DVD achieves moderate AUROC (0.66 for verbatim contamination) at high computational cost (65 GPU-hours for 12 models), with similarly low DIF correlation ($r = 0.15$).
65	
66	\paragraph{DIF in educational testing.}
67	Differential Item Functioning analysis has a 40-year history in psychometrics \citep{holland1993dif}. The Mantel-Haenszel (MH) procedure \citep{mantel1959mh} remains the most widely used method due to its simplicity and robust statistical properties. The ETS classification system (A/B/C categories) provides operational thresholds: C items ($|\Delta_{\text{MH}}| \geq 1.5$ and significantly different from 1.0) warrant review or removal. Item-Focused Trees \citep{tutz2016ift} extend DIF detection to continuous covariates, enabling finer temporal resolution. We include an IFT analysis in Appendix~\ref{app:ift} showing concordance with categorical DIF (Jaccard = 0.76) and temporal split points aligning with major model release waves.
68	
69	\paragraph{Benchmark integrity and maintenance.}
70	Growing Pains \citep{growingpains2024} identifies anchor items for efficient evaluation; our DIF diagnostic complements this by detecting which anchor items are degrading across model generations. LiveBench \citep{livebench2024} and similar dynamic benchmarks address contamination through item refresh; our analysis provides psychometric infrastructure for deciding \emph{which} items to refresh and validating that replacements maintain construct equivalence.
71	
72	
73	% ============================================================
74	% 3. METHOD
75	% ============================================================
76	\section{Method}
77	\label{sec:method}
78	
79	\subsection{Differential Item Functioning: A Primer for ML Researchers}
80	\label{sec:dif_primer}
81	
82	Consider a binary response matrix $\mathbf{X} \in \{0,1\}^{N \times J}$ where $X_{ij} = 1$ if model $i$ answers item $j$ correctly. In DIF analysis, we partition models into a \emph{reference group} $R$ and a \emph{focal group} $F$ (here: temporal cohorts, e.g., pre-2024 vs.\ 2024-H1 models) and ask: does item $j$ function differently across groups, \emph{after conditioning on overall ability}?
83	
84	The Mantel-Haenszel (MH) procedure conditions on a discrete matching variable (total score or score stratum $k$) and computes the common odds ratio:
85	\begin{equation}
86	    \hat{\alpha}_{\text{MH}} = \frac{\sum_k A_k D_k / T_k}{\sum_k B_k C_k / T_k}
87	\end{equation}
88	where $A_k, B_k, C_k, D_k$ are cells of the $2 \times 2$ table (group $\times$ response) at stratum $k$, and $T_k$ is the stratum total. The log-odds ratio is converted to the ETS $\Delta$ scale:
89	\begin{equation}
90	    \Delta_{\text{MH}} = -2.35 \ln(\hat{\alpha}_{\text{MH}})
91	\end{equation}
92	
93	Items are classified using the ETS system:
94	\begin{itemize}
95	    \item \textbf{A} (negligible): $|\Delta_{\text{MH}}| < 1.0$ or not statistically significant
96	    \item \textbf{B} (moderate): $1.0 \leq |\Delta_{\text{MH}}| < 1.5$ and significant
97	    \item \textbf{C} (large): $|\Delta_{\text{MH}}| \geq 1.5$ and significantly different from 1.0
98	\end{itemize}
99	
100	\noindent\textbf{ML translation.} DIF analysis is analogous to checking whether a feature's predictive relationship with the outcome changes across subpopulations after controlling for a confounder. An item with large DIF is one where the ``decision boundary'' between correct and incorrect shifts across model generations at matched ability---the item measures something different for newer models than for older ones.
101	
102	\subsection{Semi-Synthetic Validation Framework}
103	\label{sec:semi_synthetic}
104	
105	Validating item-level contamination detectors requires ground truth at the item$\times$model level---which items are contaminated \emph{for which models}. No such ground truth exists naturally. We construct it via \emph{semi-synthetic injection}: starting from the real METABENCH response matrix, we flip a fraction $p$ of incorrect responses to correct for selected items in the focal group, simulating differential contamination.
106	
107	The key metric is $\Delta$TPR: the increase in DIF detection rate from injection. If a detector responds to injected differential contamination, $\Delta\text{TPR} > 0$; if it cannot distinguish injected items from naturally unstable ones, $\Delta\text{TPR} \approx 0$.
108	
109	\paragraph{Cross-subject matching.} A critical methodological choice is the MH matching variable. When injecting contamination into subject $s$, using the total score on subject $s$ as the matching variable inflates FPR because the matching variable itself is contaminated. We instead match on the total score on \emph{all other subjects} $S \setminus \{s\}$. This eliminates FPR inflation ($\Delta\text{FPR} = 0.000$ across all 5 tested subjects) while preserving detection power ($\Delta\text{TPR} > 0.3$ in 4/5 subjects).
110	
111	
112	% ============================================================
113	% 4. EXPERIMENTS: TEMPORAL DIF ON MMLU
114	% ============================================================
115	\section{Experiments}
116	\label{sec:experiments}
117	
118	\subsection{Large-Scale Temporal DIF Analysis}
119	\label{sec:temporal_dif}
120	
121	\paragraph{Setup.} We analyze the METABENCH response matrix: 5{,}227 models $\times$ 12{,}508 MMLU items. Models are partitioned into temporal cohorts based on release date (reference: pre-2024; focal: 2024-H1). The MH procedure is applied to each item with total MMLU score as the matching variable.
122	
123	\paragraph{Results.} Table~\ref{tab:main_dif} summarizes the main findings. 31.3\% of items fall into ETS category C (large DIF) in the full-population analysis. A random-split sanity check (randomly assigning models to groups) yields C\% = 0.18\%, confirming the temporal signal is not a statistical artifact. Within-subject analysis (running DIF separately per MMLU subject) reveals C\% ranges from 31\% to 45\% across subjects, with mean 38.1\%---instability is pervasive, not concentrated in a few subjects.
124	
125	The correlation between subject-level C\% and subject-level accuracy improvement is $\rho = 0.307$ ($p = 0.02$), indicating that domains where models improved most also exhibit greater item instability. This is consistent with the interpretation that rapid capability improvement changes how items function---models that ``got better'' at a domain interact differently with items testing that domain.
126	
127	DIF enrichment against Li et al.\ web-overlap contamination labels is 0.96 ($\approx 1.0$), a result we analyze in Section~\ref{sec:meta_critique}.
128	
129	\begin{table}[t]
130	\centering
131	\caption{Temporal DIF analysis on MMLU (5{,}227 models $\times$ 12{,}508 items). C\% denotes the percentage of items classified as ETS category C ($|\Delta_{\text{MH}}| \geq 1.5$, significantly different from 1.0).}
132	\label{tab:main_dif}
133	\begin{tabular}{lcc}
134	\toprule
135	\textbf{Analysis} & \textbf{C\%} & \textbf{Note} \\
136	\midrule
137	Full population (temporal cohorts) & 31.3\% & Reference: pre-2024; Focal: 2024-H1 \\
138	Random-split sanity check & 0.18\% & Models randomly assigned to groups \\
139	Within-subject (per MMLU subject) & 38.1\% (avg) & Range: 31--45\% across 57 subjects \\
140	Accuracy-improvement correlation & $\rho = 0.307$ & $p = 0.02$, subject-level \\
141	Li et al.\ enrichment & 0.96 & $\approx 1.0$; see \S\ref{sec:meta_critique} \\
142	\bottomrule
143	\end{tabular}
144	\end{table}
145	
146	
147	\subsection{Ground Truth Meta-Critique}
148	\label{sec:meta_critique}
149	
150	The near-unity enrichment ($\approx 1.0$) between DIF flags and web-overlap labels is expected rather than surprising. Web-overlap labels \citep{li2024contamination} measure \emph{global exposure}---whether an item text appears on the public internet. Since virtually all MMLU items have been on Common Crawl since 2020, nearly all items have equal global exposure. DIF, by contrast, detects \emph{differential functioning}---whether an item behaves differently across model cohorts at matched ability. These are orthogonal signals: global exposure is a static, model-agnostic property; differential functioning is dynamic and group-specific.
151	
152	This has a broader implication: \emph{any} contamination detection method validated against web-overlap labels at the item level faces the same blind spot. If the ground truth cannot distinguish ``contaminated for model A but not model B'' from ``equally exposed to all models,'' it cannot evaluate item-level differential detectors. This affects Min-K\%, n-gram methods, and all work using web-overlap as ground truth for item-level validation.
153	
154	Semi-synthetic injection (Section~\ref{sec:semi_synthetic_results}) confirms that DIF \emph{can} detect differential contamination when it exists ($\Delta\text{TPR} = +0.508$)---the problem is the ground truth, not the detector.
155	
156	
157	\subsection{Architecture-Stratified DIF Analysis}
158	\label{sec:arch_strat}
159	
160	A natural concern is that DIF flags may reflect architecture differences (encoder-decoder vs.\ decoder-only vs.\ mixture-of-experts) rather than genuine temporal instability. We address this directly by restricting DIF analysis to decoder-only models only ($N = 3{,}847$; reference: $n = 892$, focal: $n = 541$).
161	
162	\paragraph{Results.} Table~\ref{tab:arch_irt} shows IRT model fit diagnostics. Restricting to decoder-only models dramatically improves fit: RMSEA drops from 0.082 (poor) to 0.037 (acceptable), CFI increases to 0.93, and SRMR falls to 0.028. This confirms that architecture heterogeneity was driving model misspecification, not the items themselves.
163	
164	Table~\ref{tab:arch_dif} presents DIF detection rates. C\% drops from 31.3\% to 22.1\%---a 29.4\% reduction---meaning approximately 9 percentage points of the original flags were architecture-confounded. The remaining 22.1\% represents genuine temporal instability within a homogeneous architecture population. Semi-synthetic validation improves correspondingly: FPR drops from 0.314 to 0.221, and $\Delta$TPR increases from 0.674 to 0.72.
165	
166	A sanity check (random split within decoder-only models) yields C\% = 0.12\%, confirming the reduction is not from power loss. Flag overlap with the full-population analysis (Jaccard = 0.68) shows the core DIF items persist---architecture stratification refines rather than contradicts the original finding.
167	
168	\begin{table}[t]
169	\centering
170	\caption{IRT model fit diagnostics: full population vs.\ decoder-only subgroup.}
171	\label{tab:arch_irt}
172	\begin{tabular}{lccccc}
173	\toprule
174	\textbf{Population} & \textbf{N} & \textbf{RMSEA} & \textbf{CFI} & \textbf{TLI} & \textbf{SRMR} \\
175	\midrule
176	Full (all architectures) & 5{,}227 & 0.082 & --- & --- & --- \\
177	Decoder-only & 3{,}847 & 0.037 & 0.93 & 0.91 & 0.028 \\
178	\bottomrule
179	\end{tabular}
180	\end{table}
181	
182	\begin{table}[t]
183	\centering
184	\caption{DIF detection rates and semi-synthetic validation: architecture-stratified vs.\ full population.}
185	\label{tab:arch_dif}
186	\begin{tabular}{lcccc}
187	\toprule
188	\textbf{Population} & \textbf{C\%} & \textbf{$\Delta$TPR} & \textbf{FPR} & \textbf{Sanity C\%} \\
189	\midrule
190	Full population & 31.3\% & 0.674 & 0.314 & 0.18\% \\
191	Decoder-only & 22.1\% & 0.720 & 0.221 & 0.12\% \\
192	\midrule
193	\textbf{Reduction} & \textbf{29.4\%} & +6.8\% & $-$29.6\% & --- \\
194	\bottomrule
195	\end{tabular}
196	\end{table}
197	
198	\paragraph{Practical recommendation.} Architecture stratification is simple, zero-cost, and immediately actionable: when applying DIF to LLM benchmarks, restrict the analysis to architecture-homogeneous subpopulations. This reduces spurious flags from architecture confounding while improving IRT model assumptions.
199	
200	
201	\subsection{Semi-Synthetic Validation Results}
202	\label{sec:semi_synthetic_results}
203	
204	Table~\ref{tab:semi_synthetic} presents semi-synthetic validation results across benchmarks and matching strategies. On MMLU, cross-subject matching achieves $\Delta\text{TPR} = +0.508$ at injection probability $p = 0.5$, with strict $\Delta\text{FPR} = 0.000$ (4/5 subjects show $\Delta\text{TPR} > 0.3$). Within-subject matching suffers from matching variable contamination, inflating FPR by +0.186. The dose-response relationship (increasing $\Delta$TPR from $p = 0.3$ to $p = 1.0$) confirms the signal is driven by injected contamination rather than distributional artifacts.
205	
206	Cross-benchmark replication on GSM8K (1{,}319 items $\times$ 6{,}702 models from METABENCH) yields $\Delta\text{TPR} = +0.818$ with standard matching and $+0.517$ with external matching, confirming framework portability. GSM8K's temporal DIF rate is C\% = 18.9\%, lower than MMLU's 31.3\%, consistent with its narrower construct (single-domain math).
207	
208	\begin{table}[t]
209	\centering
210	\caption{Semi-synthetic validation: $\Delta$TPR and $\Delta$FPR across benchmarks and matching strategies.}
211	\label{tab:semi_synthetic}
212	\begin{tabular}{llcc}
213	\toprule
214	\textbf{Benchmark} & \textbf{Matching Strategy} & \textbf{$\Delta$TPR} & \textbf{$\Delta$FPR} \\
215	\midrule
216	MMLU & Cross-subject & +0.508 & 0.000 \\
217	MMLU & Within-subject & --- & +0.186 (inflated) \\
218	GSM8K & Standard & +0.818 & --- \\
219	GSM8K & External & +0.517 & --- \\
220	\bottomrule
221	\end{tabular}
222	\end{table}
223	
224	
225	\subsection{Structural Constraints on DIF}
226	\label{sec:structural}
227	
228	We investigated whether structural improvements to DIF methodology could reduce the baseline instability rate. Three approaches were tested:
229	
230	\begin{enumerate}
231	    \item \textbf{Matched-ability cohort design}: Balancing temporal cohorts on overall ability does not reduce C\% below 31\%, because DIF is already ability-conditioned.
232	    \item \textbf{IRT $\theta$-conditioning}: Replacing discrete score strata with continuous IRT ability estimates yields near-identical flags ($r = 0.9986$ with MH flags), confirming discretization is not the issue.
233	    \item \textbf{Bifactor pre-check}: A bifactor IRT model (general + subject-specific factors) confirms MMLU has genuine multidimensional structure (general factor: 42\% variance, subject factors: 18\% average; RMSEA = 0.038, CFI = 0.91). However, anchoring on DIF-free items reduces C\% only to 33.5\%---multidimensionality accounts for merely $\sim$2.4 pp of the instability.
234	\end{enumerate}
235	
236	Table~\ref{tab:bifactor} summarizes the bifactor analysis. The equated score correlation ($\rho = 0.965$) meets the $\geq 0.95$ criterion, but this reflects MMLU's massive redundancy rather than successful decontamination. These results constitute an empirical observation: standard psychometric corrections---matched-ability, $\theta$-conditioning, bifactor equating---are insufficient to reduce baseline DIF below 31\% while maintaining detection power. Higher-dimensional methods (MIMIC, multidimensional IRT, propensity-score matching) may address individual constraints and are directions for future work.
237	
238	\begin{table}[t]
239	\centering
240	\caption{Bifactor IRT equating pilot: model fit and DIF reduction.}
241	\label{tab:bifactor}
242	\begin{tabular}{lc}
243	\toprule
244	\textbf{Metric} & \textbf{Value} \\
245	\midrule
246	Bifactor RMSEA & 0.038 \\
247	Bifactor CFI / TLI & 0.91 / 0.89 \\
248	General factor variance explained & 42\% \\
249	Subject factor avg.\ variance & 18\% \\
250	Anchor items selected & 4{,}200 \\
251	C\% after equating & 33.5\% \\
252	Equated score $\rho$ (original vs.\ replaced) & 0.965 \\
253	\bottomrule
254	\end{tabular}
255	\end{table}
256	
257	
258	% ============================================================
259	% 5. DIF AS DIAGNOSTIC LENS
260	% ============================================================
261	\section{DIF as Diagnostic Lens}
262	\label{sec:diagnostic}
263	
264	\subsection{Benchmark Redundancy and Discriminative Signal}
265	\label{sec:redundancy}
266	
267	Removing all C-category DIF items (31\% of MMLU) barely changes model rankings: the Spearman correlation between full and stable-only rankings is $\rho \approx 0.997$. This reveals massive measurement redundancy---MMLU has approximately $3\times$ more items than needed for stable rankings.
268	
269	Yet DIF items are not noise. Their removal disrupts rankings \emph{significantly more} than random removal of equal size ($z = -8$ to $-49\sigma$ across 21 conditions). DIF items carry $1.09\times$ cross-cohort accuracy swing versus $0.96\times$ for stable items---they concentrate the information that differentiates model generations. Model-specific patterns emerge: phi-3 and llama-3 families gain $+700$ to $+850$ ranks from DIF items, while mistral merges lose $-400$ to $-587$ ranks.
270	
271	DIF items thus function as \emph{diagnostic markers}: they identify which capability dimensions are changing across model generations. This reframes DIF from ``find bad items and remove'' to ``understand what changed and why''---complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.
272	
273	
274	\subsection{Cross-Benchmark Validation: GSM8K and GSM1K}
275	\label{sec:cross_benchmark}
276	
277	On GSM8K (1{,}319 items $\times$ 6{,}702 models), DIF flags anti-correlate with GSM1K contamination gaps ($r = -0.478$, $p = 0.005$; partial $r = -0.385$ controlling for accuracy; permutation $p = 0.014$). Models with high contamination gaps (Phi, Gemma families) perform \emph{worse} on DIF items. This confirms that DIF captures genuine capability-discriminative items that contamination cannot fake---contaminated models achieve shallow performance gains concentrated on non-DIF items. The analysis includes $N = 33$ matched models and is leave-one-out robust (min $|r| = 0.374$).
278	
279	
280	\subsection{Cumulative Bayesian DIF for Operational Monitoring}
281	\label{sec:bayesian}
282	
283	Single-shot DIF detection has limited power for medium effects ($\text{TPR} = 0.42$ at $\delta = 1.0$). We propose cumulative Bayesian DIF priors that accumulate evidence across successive benchmark administrations.
284	
285	Table~\ref{tab:bayesian} shows power improvement over four simulated administrations ($N = 200$ models per administration). Each administration adds approximately 15 percentage points of TPR for medium effects ($\delta = 1.0$), reaching 0.71 after three administrations. FPR remains stable at $\sim$0.04 because Bayesian updating with proper priors is conservative on non-DIF items. At the operational threshold ($\delta = 1.4$), power reaches 0.89 by administration 4. The Bayes factor threshold of 3.2 (``substantial evidence'') provides a principled decision criterion superior to the arbitrary $|\Delta_{\text{MH}}| \geq 1.5$ cutoff.
286	
287	\begin{table}[t]
288	\centering
289	\caption{Cumulative Bayesian DIF: power by administration $\times$ effect size. FPR remains stable across administrations ($\sim$0.04). $N = 200$ simulated models per administration; BF threshold = 3.2.}
290	\label{tab:bayesian}
291	\begin{tabular}{lcccc}
292	\toprule
293	\textbf{Effect Size ($\delta$)} & \textbf{Admin 1} & \textbf{Admin 2} & \textbf{Admin 3} & \textbf{Admin 4} \\
294	\midrule
295	0.8 & --- & --- & --- & 0.53 \\
296	1.0 & 0.42 & 0.58 & 0.71 & 0.78 \\
297	1.2 & --- & --- & --- & --- \\
298	1.4 & --- & --- & --- & 0.89 \\
299	\midrule
300	FPR (Admin 1) & \multicolumn{4}{c}{0.041} \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "889c8ed9-8df7-4041-a6f7-dfa9a06e06e4",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "a731e9bf-c8eb-4bb0-9f42-6882790cec08",
  "sourceToolAssistantUUID": "889c8ed9-8df7-4041-a6f7-dfa9a06e06e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T02:08:09.735Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AdLZHoJB3fxF7Xo4pPij2a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/best/paper.tex",
  "offset": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a731e9bf-c8eb-4bb0-9f42-6882790cec08",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu4oW9xMC4jYrpKE59H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2cef4ca-bda6-4407-a4f4-1d6da257d464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmyNRowph4nx1ZL761Be1a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12361,
      "cache_read_input_tokens": 46032,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12361
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 46032,
          "cache_creation_input_tokens": 12361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12361,
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

_source line 29 · 2026-05-21T02:08:09.754Z_

<details><summary>↩ Tool result · `toolu_01AdLZHoJB3fxF7Xo4pPij2a`</summary>

```text
300	FPR (Admin 1) & \multicolumn{4}{c}{0.041} \\
301	FPR (Admin 4) & \multicolumn{4}{c}{0.039} \\
302	Prior-posterior shrinkage & \multicolumn{4}{c}{0.35} \\
303	\bottomrule
304	\end{tabular}
305	\end{table}
306	
307	\paragraph{Operational recommendation.} Benchmark maintainers should accumulate DIF evidence across evaluation rounds rather than relying on single-shot detection. Three to four administrations suffice for reliable detection of operationally relevant effects ($\delta \geq 1.0$).
308	
309	
310	% ============================================================
311	% 6. DISCUSSION
312	% ============================================================
313	\section{Discussion}
314	\label{sec:discussion}
315	
316	\paragraph{RL robustness.}
317	A natural concern is whether reasoning-RL models (GRPO/PPO-trained) break DIF analysis. We evaluate this in Appendix~\ref{app:rl}: adding 13 reasoning-RL models to METABENCH cohorts barely perturbs DIF flags (Jaccard = 0.88, TOST equivalence $p = 0.008$). By contrast, traditional per-model detectors degrade sharply on RL models (Min-K\% AUROC: 0.81 $\rightarrow$ 0.52; ConStat AUROC: 0.77 $\rightarrow$ 0.48). DIF's group-level architecture is fundamentally orthogonal to the NLL-gap-contraction mechanism that defeats per-model detectors. The $N = 13$ sample is small and we acknowledge this as a limitation; the directional evidence is nonetheless unambiguous.
318	
319	\paragraph{Cause vs.\ characterization.}
320	We emphasize that 38\% instability is a \emph{characterization finding}, not a contamination claim. The correlation with accuracy improvement ($\rho = 0.307$) means we cannot decompose instability into contamination vs.\ genuine capability improvement. DIF reveals \emph{that} items function differently---not \emph{why}. This is the appropriate scope for a characterization study; causal decomposition requires controlled experiments (training models with and without specific items) that are beyond current infrastructure.
321	
322	
323	% ============================================================
324	% 7. FUTURE WORK
325	% ============================================================
326	\section{Future Work}
327	\label{sec:future}
328	
329	Our analysis suggests several natural extensions organized around three themes.
330	
331	\paragraph{Multi-signal ensemble detection.}
332	DIF, ConStat, and DVD capture orthogonal contamination signals (pairwise correlations $r \leq 0.21$). Preliminary ensemble fusion achieves AUROC 0.89 with FPR 0.07 under 2-of-3 voting (Table~\ref{tab:ensemble}). Weighted fusion yields a modest improvement (AUROC 0.89 vs.\ 0.86 uniform), with stable cross-validated weights ($\sigma = 0.03$). A standalone methods paper exploring this ensemble is planned.
333	
334	\begin{table}[t]
335	\centering
336	\caption{Preliminary ensemble fusion results (DIF + ConStat + DVD). All results are from pilot evaluation and are planned for a follow-up study.}
337	\label{tab:ensemble}
338	\begin{tabular}{lc}
339	\toprule
340	\textbf{Metric} & \textbf{Value} \\
341	\midrule
342	2-of-3 voting TPR & 0.84 \\
343	2-of-3 voting FPR & 0.07 \\
344	Weighted fusion AUROC & 0.89 \\
345	Uniform weight AUROC & 0.86 \\
346	Cross-validated weight stability ($\sigma$) & 0.03 \\
347	Effective coverage (union) & 0.78 \\
348	\bottomrule
349	\end{tabular}
350	\end{table}
351	
352	\paragraph{Per-model detection baselines.}
353	ConStat achieves AUROC 0.73 on non-RL models (Table~\ref{tab:constat}) but degrades to 0.44 on RL models, consistent with PPO's smoothing of original-vs-reformulated accuracy gaps (effect size drops from 0.85 to 0.31). DVD detects verbatim contamination at AUROC 0.66 (Table~\ref{tab:dvd}) but is weak on variant contamination (0.58) and costly (65 GPU-hours for 12 models). These per-model approaches are complementary to DIF's group-level analysis.
354	
355	\begin{table}[t]
356	\centering
357	\caption{ConStat perturbation testing on MMLU (240 reformulated items $\times$ 15 models).}
358	\label{tab:constat}
359	\begin{tabular}{lc}
360	\toprule
361	\textbf{Metric} & \textbf{Value} \\
362	\midrule
363	Paraphrase semantic similarity & 0.94 \\
364	Detection rate (FDR = 0.10) & 0.32 \\
365	AUROC (non-RL models) & 0.73 \\
366	AUROC (RL models) & 0.44 \\
367	Correlation with DIF flags & 0.21 \\
368	Effect size (verbatim contaminated) & 0.85 \\
369	Effect size (paraphrase contaminated) & 0.31 \\
370	\bottomrule
371	\end{tabular}
372	\end{table}
373	
374	\begin{table}[t]
375	\centering
376	\caption{DVD generation variance on MMLU (12 models $\times$ 2{,}400 items, 50 responses/item at $T = 0.8$).}
377	\label{tab:dvd}
378	\begin{tabular}{lc}
379	\toprule
380	\textbf{Metric} & \textbf{Value} \\
381	\midrule
382	AUROC (verbatim contamination) & 0.66 \\
383	AUROC (variant contamination) & 0.58 \\
384	Bimodal detection rate & 0.14 \\
385	Correlation with DIF flags & 0.15 \\
386	GPU-hours consumed & 65 \\
387	\bottomrule
388	\end{tabular}
389	\end{table}
390	
391	\paragraph{Automated benchmark maintenance.}
392	The massive redundancy we observe ($\rho = 0.997$ after 31\% item removal) suggests benchmark maintenance via item replacement is feasible. Preliminary analysis (Table~\ref{tab:degradation}) confirms MMLU tolerates aggressive replacement: $\rho = 0.994$ at 20\% replacement with 96\% construct coverage. A pilot item generation study using student simulation \citep{studentsim2025} achieves difficulty calibration $\rho = 0.71$ (Table~\ref{tab:itemgen}), substantially outperforming prompt-based targeting ($\rho = 0.28$). These components---DIF identifies which items to replace, student simulation calibrates replacements, graceful degradation bounds validate the process---form a complete pipeline for future work.
393	
394	\begin{table}[t]
395	\centering
396	\caption{Graceful degradation: validity metrics under progressive item replacement.}
397	\label{tab:degradation}
398	\begin{tabular}{lccc}
399	\toprule
400	\textbf{Replacement Rate} & \textbf{Ranking $\rho$} & \textbf{SHR} & \textbf{Construct Coverage} \\
401	\midrule
402	5\% & 0.9991 & --- & --- \\
403	10\% & 0.9978 & --- & --- \\
404	20\% & 0.9943 & 0.988 & 0.96 \\
405	50\% & 0.9821 & --- & 0.88 \\
406	\midrule
407	\multicolumn{4}{l}{Theoretical bound: $\rho \geq 1 - 2r(1-r)$; empirical-theoretical gap = 0.008} \\
408	\bottomrule
409	\end{tabular}
410	\end{table}
411	
412	\begin{table}[t]
413	\centering
414	\caption{Item generation calibration pilot (500 generated items $\times$ 30 MMLU subjects).}
415	\label{tab:itemgen}
416	\begin{tabular}{lcc}
417	\toprule
418	\textbf{Metric} & \textbf{Student Sim.} & \textbf{Prompt-based} \\
419	\midrule
420	Difficulty $\rho$ (calibration) & 0.71 & 0.28 \\
421	Discrimination $\rho$ (calibration) & 0.58 & --- \\
422	Difficulty $\rho$ (holdout, $N=50$) & 0.64 & --- \\
423	Discrimination $\rho$ (holdout) & 0.49 & --- \\
424	Construct coverage (Jaccard) & 0.82 & --- \\
425	\bottomrule
426	\end{tabular}
427	\end{table}
428	
429	
430	% ============================================================
431	% 8. CONCLUSION
432	% ============================================================
433	\section{Conclusion}
434	\label{sec:conclusion}
435	
436	We present the largest-scale psychometric analysis of an LLM benchmark, revealing that 38\% of MMLU items are functionally unstable across model generations. This instability persists within every subject domain, survives architecture stratification (22.1\% within decoder-only models), and correlates with capability improvement---models getting better at specific domains changes how items function.
437	
438	Our analysis exposes a fundamental blind spot in the field's validation methodology: web-overlap contamination labels cannot evaluate item-level differential detectors. The semi-synthetic validation framework we introduce---with cross-subject matching to eliminate FPR inflation---provides reusable infrastructure for this purpose.
439	
440	Perhaps most importantly, DIF items are not measurement noise to be discarded. They concentrate the discriminative signal that differentiates model generations, and they anti-correlate with contamination. DIF is a diagnostic lens that reveals \emph{which} capability dimensions are changing---complementing, rather than competing with, existing benchmark integrity efforts.
441	
442	
443	% ============================================================
444	% REFERENCES
445	% ============================================================
446	\bibliographystyle{plainnat}
447	\begin{thebibliography}{20}
448	
449	\bibitem[Holland \& Wainer(1993)]{holland1993dif}
450	Holland, P.~W. and Wainer, H. (1993).
451	\newblock \emph{Differential Item Functioning}.
452	\newblock Lawrence Erlbaum Associates.
453	
454	\bibitem[Li et al.(2024)]{li2024contamination}
455	Li, Y., et al. (2024).
456	\newblock Open {LLM} leaderboard contamination analysis.
457	\newblock \emph{arXiv preprint}.
458	
459	\bibitem[Mantel \& Haenszel(1959)]{mantel1959mh}
460	Mantel, N. and Haenszel, W. (1959).
461	\newblock Statistical aspects of the analysis of data from retrospective studies of disease.
462	\newblock \emph{Journal of the National Cancer Institute}, 22(4):719--748.
463	
464	\bibitem[Orenstrakh et al.(2024)]{metabench2024}
465	Orenstrakh, M.~S., et al. (2024).
466	\newblock {METABENCH}: A large-scale meta-evaluation of {LLM} benchmarks.
467	\newblock \emph{arXiv preprint}.
468	
469	\bibitem[Shi et al.(2024)]{shi2024mink}
470	Shi, W., et al. (2024).
471	\newblock Detecting pretraining data from large language models.
472	\newblock \emph{ICLR 2024}.
473	
474	\bibitem[Tutz \& Berger(2016)]{tutz2016ift}
475	Tutz, G. and Berger, M. (2016).
476	\newblock Item-focused trees for the identification of items in differential item functioning.
477	\newblock \emph{Psychometrika}, 81(3):727--750.
478	
479	\bibitem[{ConStat Authors}(2024)]{constat2024}
480	{ConStat Authors} (2024).
481	\newblock {ConStat}: Contamination detection via perturbation testing.
482	\newblock \emph{arXiv preprint}.
483	
484	\bibitem[{DVD Authors}(2024)]{dvd2024}
485	{DVD Authors} (2024).
486	\newblock {DVD}: Detecting verbatim duplication via generation variance.
487	\newblock \emph{arXiv preprint}.
488	
489	\bibitem[{Growing Pains Authors}(2024)]{growingpains2024}
490	{Growing Pains Authors} (2024).
491	\newblock Growing pains: Understanding the limitations of {LLM} benchmarks.
492	\newblock \emph{arXiv preprint}.
493	
494	\bibitem[{LiveBench Authors}(2024)]{livebench2024}
495	{LiveBench Authors} (2024).
496	\newblock {LiveBench}: A challenging, contamination-free {LLM} benchmark.
497	\newblock \emph{arXiv preprint}.
498	
499	\bibitem[Kim \& Kolen(2019)]{kim2019calibration}
500	Kim, S. and Kolen, M.~J. (2019).
501	\newblock \emph{Test Equating, Scaling, and Linking}.
502	\newblock Springer, 3rd edition.
503	
504	\bibitem[{Student Simulation Authors}(2025)]{studentsim2025}
505	{Student Simulation Authors} (2025).
506	\newblock Student simulation for benchmark item calibration.
507	\newblock \emph{arXiv:2601.09953}.
508	
509	\end{thebibliography}
510	
511	
512	% ============================================================
513	% APPENDICES
514	% ============================================================
515	\appendix
516	
517	\section{RL Robustness Validation}
518	\label{app:rl}
519	
520	We evaluate DIF robustness to reasoning-RL models by adding 13 open-weight GRPO/PPO models to METABENCH temporal cohorts (existing cohort: 477 alignment-RL models, remainder SFT-only).
521	
522	Table~\ref{tab:rl_stability} shows DIF flag stability. Adding reasoning-RL models produces Jaccard similarity of 0.88 with the original flags and a retention ratio of 0.93. TOST equivalence testing confirms equivalence ($p = 0.008$).
523	
524	Table~\ref{tab:rl_detectors} compares detector performance across training regimes. Traditional per-model detectors degrade sharply on reasoning-RL models: Min-K\% AUROC drops from 0.81 (SFT-only) to 0.52 (reasoning-RL), and ConStat drops from 0.77 to 0.48. DIF maintains bootstrap CI of [0.87, 0.94]. The detection boundary at exploitation rate 0.45 indicates DIF maintains power above the operationally relevant regime.
525	
526	\begin{table}[h]
527	\centering
528	\caption{DIF flag stability under cohort composition perturbation.}
529	\label{tab:rl_stability}
530	\begin{tabular}{lc}
531	\toprule
532	\textbf{Metric} & \textbf{Value} \\
533	\midrule
534	Reasoning-RL models added & 13 \\
535	Alignment-RL models (existing) & 477 \\
536	DIF flag Jaccard (with vs.\ without RL) & 0.88 \\
537	DIF retention ratio & 0.93 \\
538	TOST equivalence $p$ & 0.008 \\
539	\bottomrule
540	\end{tabular}
541	\end{table}
542	
543	\begin{table}[h]
544	\centering
545	\caption{Traditional detector AUROC by model training regime with bootstrap 95\% CIs.}
546	\label{tab:rl_detectors}
547	\begin{tabular}{lccc}
548	\toprule
549	\textbf{Detector} & \textbf{SFT-only} & \textbf{Alignment-RL} & \textbf{Reasoning-RL} \\
550	\midrule
551	Min-K\% & 0.81 & 0.74 & 0.52 [0.41, 0.63] \\
552	ConStat & 0.77 & --- & 0.48 \\
553	DIF (bootstrap CI) & \multicolumn{3}{c}{[0.87, 0.94]} \\
554	\bottomrule
555	\end{tabular}
556	\end{table}
557	
558	
559	\section{Item-Focused Trees Analysis}
560	\label{app:ift}
561	
562	Item-Focused Trees \citep{tutz2016ift} treat model release date as a continuous covariate (days since 2023-01-01) rather than imposing categorical cohort splits. Table~\ref{tab:ift} compares IFT with categorical DIF across 12{,}508 items.
563	
564	IFT identifies 28.4\% of items as functionally unstable (vs.\ 31.3\% categorical)---slightly fewer because continuous modeling avoids artificial inflation from binary cohort splits. Jaccard overlap is 0.76, with 412 unique IFT detections capturing items with smooth temporal drift (34\% show gradual transition patterns). Semi-synthetic AUC is 0.91 (vs.\ 0.88 categorical). Tree split points cluster around 2023-Q4 and 2024-Q2, aligning with major model release waves (Llama-2$\rightarrow$3, Qwen-1.5$\rightarrow$2), providing temporal resolution that categorical DIF cannot offer.
565	
566	\begin{table}[h]
567	\centering
568	\caption{Item-Focused Trees vs.\ categorical DIF detection concordance.}
569	\label{tab:ift}
570	\begin{tabular}{lcc}
571	\toprule
572	\textbf{Metric} & \textbf{IFT} & \textbf{Categorical DIF} \\
573	\midrule
574	C\%-equivalent & 28.4\% & 31.3\% \\
575	Semi-synthetic AUC & 0.91 & 0.88 \\
576	Unique flags & 412 & 891 \\
577	Smooth transition detection & 34\% & --- \\
578	Median tree depth & 3 & --- \\
579	Flag overlap (Jaccard) & \multicolumn{2}{c}{0.76} \\
580	Split point clusters & \multicolumn{2}{c}{2023-Q4, 2024-Q2} \\
581	\bottomrule
582	\end{tabular}
583	\end{table}
584	
585	
586	\end{document}
587	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2cef4ca-bda6-4407-a4f4-1d6da257d464",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "8785cf9a-4ce0-4421-8fca-b64c55b7e80e",
  "sourceToolAssistantUUID": "b2cef4ca-bda6-4407-a4f4-1d6da257d464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-21T02:08:14.776Z_

Now let me also read some of the key experiment reports for deeper technical assessment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8785cf9a-4ce0-4421-8fca-b64c55b7e80e",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu5Ccx1539kv9o83veR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f915bd3-19b8-4ace-9952-44f46eb27aa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GYUts9DGrpLCMgDxyHSxm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5334,
      "cache_read_input_tokens": 58393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5334,
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

_source line 31 · 2026-05-21T02:08:17.709Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XCMGBf1XzYfais4aBZ9V7r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/report/plan_011_report.md",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f915bd3-19b8-4ace-9952-44f46eb27aa2",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu5Ccx1539kv9o83veR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9180e676-5e14-4a98-a73e-5af32accd33f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GYUts9DGrpLCMgDxyHSxm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5334,
      "cache_read_input_tokens": 58393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5334,
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

### Tool result

_source line 32 · 2026-05-21T02:08:17.729Z_

<details><summary>↩ Tool result · `toolu_01XCMGBf1XzYfais4aBZ9V7r`</summary>

```text
1	# Plan 011: Semi-Synthetic DIF Validation
2	
3	## 1. Objective
4	
5	Inject known **differential** contamination into real MMLU response data and test
6	whether MH-DIF can detect it. This validates whether plan_001/001b's failure to find
7	enrichment was due to Li et al. labels being non-differential (global contamination)
8	rather than a fundamental limitation of MH-DIF.
9	
10	## 2. Setup
11	
12	- **Baseline items**: 500 (clean in Li et al. + ETS A in plan_001 ability DIF)
13	- **Contaminated per run**: 100 of 500
14	- **Injection probabilities**: [0.0, 0.3, 0.5, 0.7, 1.0]
15	- **Seeds per p**: 5
16	
17	### Cohort definitions
18	
19	- **ability**: ref N=2092, foc N=2089, foc inject N=2089
20	- **temporal**: ref N=1080, foc N=807, foc inject N=787
21	
22	> **Note**: Ability quintiles (Q1-2 vs Q4-5) have no accuracy overlap by construction (ref max=0.6319, foc min=0.6772). All focal models used for injection. MH stratification handles ability matching.
23	
24	### MH variants
25	
26	| Variant | Matching variable | Rationale |
27	|---------|-------------------|-----------|
28	| standard | sum of 500 items − current | Same as plan_001; susceptible to matching variable contamination when 20% items injected |
29	| anchor | sum of 400 known-clean items | Eliminates matching variable contamination; assumes oracle knowledge of clean items |
30	| external | sum of all 12,508 items (original, pre-injection) | Best matching precision; immune to injection; requires external ability estimate |
31	
32	## 3. Results by MH Variant
33	
34	### Standard MH
35	
36	| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
37	|--------|---|----------------|----------------|------|-----------|----------|
38	| ability | 0.0 | 0.594±0.053 | 0.611±0.013 | +0.000 | 0.96 | 0.4231 |
39	| ability | 0.3 | 0.700±0.057 | 0.609±0.026 | +0.106 | 1.58 | 0.2555 |
40	| ability | 0.5 | 0.760±0.046 | 0.600±0.021 | +0.166 | 2.21 | 0.0067 |
41	| ability | 0.7 | 0.806±0.036 | 0.598±0.030 | +0.212 | 2.90 | 0.0002 |
42	| ability | 1.0 | 0.816±0.035 | 0.596±0.023 | +0.222 | 3.17 | 0.0001 |
43	| temporal | 0.0 | 0.308±0.047 | 0.298±0.012 | +0.000 | 1.07 | 0.8081 |
44	| temporal | 0.3 | 0.424±0.059 | 0.390±0.018 | +0.116 | 1.18 | 0.6435 |
45	| temporal | 0.5 | 0.682±0.045 | 0.453±0.021 | +0.374 | 2.63 | 0.0001 |
46	| temporal | 0.7 | 0.966±0.009 | 0.503±0.021 | +0.658 | 30.34 | 0.0000 |
47	| temporal | 1.0 | 1.000±0.000 | 0.616±0.014 | +0.692 | inf | 0.0000 |
48	
49	### Anchor MH
50	
51	| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
52	|--------|---|----------------|----------------|------|-----------|----------|
53	| ability | 0.0 | 0.600±0.060 | 0.596±0.022 | +0.000 | 1.04 | 0.4893 |
54	| ability | 0.3 | 0.700±0.051 | 0.596±0.022 | +0.100 | 1.64 | 0.1731 |
55	| ability | 0.5 | 0.764±0.038 | 0.596±0.022 | +0.164 | 2.24 | 0.0014 |
56	| ability | 0.7 | 0.808±0.041 | 0.596±0.022 | +0.208 | 2.98 | 0.0001 |
57	| ability | 1.0 | 0.818±0.033 | 0.596±0.022 | +0.218 | 3.16 | 0.0001 |
58	| temporal | 0.0 | 0.314±0.053 | 0.307±0.018 | +0.000 | 1.07 | 0.5465 |
59	| temporal | 0.3 | 0.522±0.054 | 0.307±0.018 | +0.208 | 2.49 | 0.0001 |
60	| temporal | 0.5 | 0.806±0.034 | 0.307±0.018 | +0.492 | 9.59 | 0.0000 |
61	| temporal | 0.7 | 0.990±0.010 | 0.307±0.018 | +0.676 | inf | 0.0000 |
62	| temporal | 1.0 | 1.000±0.000 | 0.307±0.018 | +0.686 | inf | 0.0000 |
63	
64	### External MH
65	
66	| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
67	|--------|---|----------------|----------------|------|-----------|----------|
68	| ability | 0.0 | 0.498±0.041 | 0.493±0.010 | +0.000 | 1.04 | 0.5025 |
69	| ability | 0.3 | 0.662±0.044 | 0.493±0.010 | +0.164 | 2.07 | 0.0051 |
70	| ability | 0.5 | 0.756±0.041 | 0.493±0.010 | +0.258 | 3.31 | 0.0000 |
71	| ability | 0.7 | 0.792±0.034 | 0.493±0.010 | +0.294 | 4.04 | 0.0000 |
72	| ability | 1.0 | 0.800±0.038 | 0.493±0.010 | +0.302 | 4.30 | 0.0000 |
73	| temporal | 0.0 | 0.326±0.035 | 0.314±0.009 | +0.000 | 1.07 | 0.7203 |
74	| temporal | 0.3 | 0.548±0.033 | 0.314±0.009 | +0.222 | 2.67 | 0.0000 |
75	| temporal | 0.5 | 0.834±0.027 | 0.314±0.009 | +0.508 | 11.22 | 0.0000 |
76	| temporal | 0.7 | 0.990±0.010 | 0.314±0.009 | +0.664 | inf | 0.0000 |
77	| temporal | 1.0 | 1.000±0.000 | 0.314±0.009 | +0.674 | inf | 0.0000 |
78	
79	## 4. Key Comparison: Baseline FPR by Variant
80	
81	| Cohort | standard | anchor | external |
82	|--------|----------|--------|----------|
83	| ability | 0.611 | 0.596 | 0.493 |
84	| temporal | 0.298 | 0.307 | 0.314 |
85	
86	If external FPR ≪ standard FPR, the high baseline rate is from matching precision,
87	not inherent DIF in the selected items.
88	
89	## 5. Sanity Checks
90	
91	### Density change (focal × contaminated items)
92	
93	| Cohort | p | Orig density | Post density | Responses flipped |
94	|--------|---|--------------|--------------|-------------------|
95	| ability | 0.3 | 0.6772 | 0.7744 | 20301 |
96	| temporal | 0.3 | 0.5800 | 0.7068 | 9981 |
97	| ability | 0.5 | 0.6772 | 0.8386 | 33706 |
98	| temporal | 0.5 | 0.5800 | 0.7903 | 16553 |
99	| ability | 0.7 | 0.6772 | 0.9031 | 47177 |
100	| temporal | 0.7 | 0.5800 | 0.8741 | 23148 |
101	| ability | 1.0 | 0.6772 | 1.0000 | 67424 |
102	| temporal | 1.0 | 0.5800 | 1.0000 | 33053 |
103	
104	## 6. Verdict
105	
106	### Standard MH
107	
108	**ability**: baseline TPR=0.594/FPR=0.611, p=1.0 TPR=0.816/FPR=0.596, ΔTPR=+0.222
109	→ **PARTIAL**: detectable signal (ΔTPR=0.222) but modest
110	
111	**temporal**: baseline TPR=0.308/FPR=0.298, p=1.0 TPR=1.000/FPR=0.616, ΔTPR=+0.692
112	→ **SUCCESS**: injection raises TPR by 0.692 with clear dose-response
113	
114	### Anchor MH
115	
116	**ability**: baseline TPR=0.600/FPR=0.596, p=1.0 TPR=0.818/FPR=0.596, ΔTPR=+0.218
117	→ **PARTIAL**: detectable signal (ΔTPR=0.218) but modest
118	
119	**temporal**: baseline TPR=0.314/FPR=0.307, p=1.0 TPR=1.000/FPR=0.307, ΔTPR=+0.686
120	→ **SUCCESS**: injection raises TPR by 0.686 with clear dose-response
121	
122	### External MH
123	
124	**ability**: baseline TPR=0.498/FPR=0.493, p=1.0 TPR=0.800/FPR=0.493, ΔTPR=+0.302
125	→ **SUCCESS**: injection raises TPR by 0.302 with clear dose-response
126	
127	**temporal**: baseline TPR=0.326/FPR=0.314, p=1.0 TPR=1.000/FPR=0.314, ΔTPR=+0.674
128	→ **SUCCESS**: injection raises TPR by 0.674 with clear dose-response
129	
130	## 7. Overall Interpretation
131	
132	### Does MH-DIF detect differential contamination?
133	
134	- **Temporal + external matching**: TPR rises 0.326 → 1.000 (ΔTPR=+0.674), FPR 0.314 → 0.314
135	- **Ability + external matching**: TPR rises 0.498 → 0.800 (ΔTPR=+0.302), FPR 0.493 → 0.493
136	
137	### Implications for plan_001
138	
139	If semi-synthetic injection is detectable → plan_001's failure to find enrichment
140	against Li et al. labels is because Li et al. contamination is **non-differential**
141	(Common Crawl data available to all models), not because MH-DIF is fundamentally limited.
142	
143	### Matching variable contamination
144	
145	When 20% of items are injected, standard MH's matching variable (total score) is
146	corrupted by injected items, inflating FPR. This is a known limitation when DIF items
147	constitute a large fraction of the test. In practice, iterative purification (exclude
148	suspected DIF items from matching) or external ability estimates mitigate this.
149	
150	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9180e676-5e14-4a98-a73e-5af32accd33f",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "e2ace216-faa1-4464-b943-5ce9db011345",
  "sourceToolAssistantUUID": "9180e676-5e14-4a98-a73e-5af32accd33f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T02:08:18.631Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AudYWQfJHQneFeNSJjRCYB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017/report/plan_017_report.md",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2ace216-faa1-4464-b943-5ce9db011345",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu5Ccx1539kv9o83veR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5fcf3e2-f1bf-4f43-96a4-261b4106b8f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GYUts9DGrpLCMgDxyHSxm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5334,
      "cache_read_input_tokens": 58393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5334,
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

### Tool result

_source line 34 · 2026-05-21T02:08:18.641Z_

<details><summary>↩ Tool result · `toolu_01AudYWQfJHQneFeNSJjRCYB`</summary>

```text
1	# plan_017: Downstream Impact Analysis — DIF Item Removal → Ranking Stability
2	
3	## Summary
4	
5	This analysis evaluates whether removing temporally unstable (DIF) items from MMLU
6	produces more stable and reliable model rankings.
7	
8	
9	## Data
10	
11	- Response matrix: 5227 models × 12508 items
12	- Temporal cohorts: 2023 (1080 models), 2024 (807 models)
13	- DIF classification: ETS A=6332, B=2258, C=3918
14	- Stable items (A+B): 8590 (68.7%)
15	- DIF items (C): 3918 (31.3%)
16	
17	
18	## Part 1: Full vs Stable-Only Ranking
19	
20	| Cohort | N models | ρ(full, stable) | 95% CI | SHR full | SHR stable |
21	|--------|----------|-----------------|--------|----------|------------|
22	| 2023 | 1080 | 0.998851 | [0.998490, 0.999028] | 0.9970±0.0005 | 0.9955±0.0007 |
23	| 2024 | 807 | 0.997014 | [0.995997, 0.997642] | 0.9923±0.0024 | 0.9890±0.0030 |
24	| all | 5227 | 0.996451 | [0.995977, 0.996808] | 0.9934±0.0018 | 0.9919±0.0016 |
25	
26	
27	## Part 2: Progressive DIF Removal
28	
29	| Frac | Removed | Remaining | Cohort | ρ(full, reduced) | 95% CI |
30	|------|---------|-----------|--------|------------------|--------|
31	| 0.00 | 0 | 12508 | 2023 | 1.000000 | [1.000000, 1.000000] |
32	| 0.00 | 0 | 12508 | 2024 | 1.000000 | [1.000000, 1.000000] |
33	| 0.00 | 0 | 12508 | all | 1.000000 | [1.000000, 1.000000] |
34	| 0.05 | 625 | 11883 | 2023 | 0.999846 | [0.999777, 0.999862] |
35	| 0.05 | 625 | 11883 | 2024 | 0.999351 | [0.999033, 0.999458] |
36	| 0.05 | 625 | 11883 | all | 0.998926 | [0.998730, 0.999062] |
37	| 0.10 | 1250 | 11258 | 2023 | 0.999641 | [0.999498, 0.999707] |
38	| 0.10 | 1250 | 11258 | 2024 | 0.998676 | [0.998120, 0.998969] |
39	| 0.10 | 1250 | 11258 | all | 0.997700 | [0.997313, 0.997990] |
40	| 0.15 | 1876 | 10632 | 2023 | 0.999458 | [0.999283, 0.999545] |
41	| 0.15 | 1876 | 10632 | 2024 | 0.997849 | [0.996921, 0.998397] |
42	| 0.15 | 1876 | 10632 | all | 0.997698 | [0.997344, 0.997998] |
43	| 0.20 | 2501 | 10007 | 2023 | 0.999344 | [0.999157, 0.999426] |
44	| 0.20 | 2501 | 10007 | 2024 | 0.997483 | [0.996414, 0.998024] |
45	| 0.20 | 2501 | 10007 | all | 0.997397 | [0.997027, 0.997747] |
46	| 0.25 | 3127 | 9381 | 2023 | 0.999192 | [0.998935, 0.999316] |
47	| 0.25 | 3127 | 9381 | 2024 | 0.997558 | [0.996460, 0.997958] |
48	| 0.25 | 3127 | 9381 | all | 0.997049 | [0.996577, 0.997407] |
49	| 0.30 | 3752 | 8756 | 2023 | 0.998865 | [0.998484, 0.999019] |
50	| 0.30 | 3752 | 8756 | 2024 | 0.997229 | [0.996209, 0.997794] |
51	| 0.30 | 3752 | 8756 | all | 0.996451 | [0.995945, 0.996938] |
52	| 0.38 | 4753 | 7755 | 2023 | 0.998644 | [0.998305, 0.998842] |
53	| 0.38 | 4753 | 7755 | 2024 | 0.995266 | [0.993763, 0.996262] |
54	| 0.38 | 4753 | 7755 | all | 0.996645 | [0.996159, 0.997027] |
55	
56	
57	## Part 3: DIF vs Random Removal Comparison
58	
59	Negative z-score = DIF removal causes *more* rank disruption than random.
60	
61	| Frac | Cohort | ρ DIF | ρ Random (mean±std) | z-score |
62	|------|--------|-------|---------------------|---------|
63	| 0.05 | 2023 | 0.999846 | 0.999942±0.000009 | -10.20 |
64	| 0.05 | 2024 | 0.999351 | 0.999844±0.000042 | -11.70 |
65	| 0.05 | all | 0.998926 | 0.999886±0.000033 | -29.07 |
66	| 0.10 | 2023 | 0.999641 | 0.999898±0.000010 | -25.12 |
67	| 0.10 | 2024 | 0.998676 | 0.999727±0.000095 | -11.00 |
68	| 0.10 | all | 0.997700 | 0.999795±0.000042 | -49.44 |
69	| 0.15 | 2023 | 0.999458 | 0.999823±0.000031 | -11.71 |
70	| 0.15 | 2024 | 0.997849 | 0.999552±0.000151 | -11.28 |
71	| 0.15 | all | 0.997698 | 0.999611±0.000157 | -12.22 |
72	| 0.20 | 2023 | 0.999344 | 0.999774±0.000046 | -9.42 |
73	| 0.20 | 2024 | 0.997483 | 0.999415±0.000152 | -12.72 |
74	| 0.20 | all | 0.997397 | 0.999477±0.000171 | -12.15 |
75	| 0.25 | 2023 | 0.999192 | 0.999713±0.000040 | -12.89 |
76	| 0.25 | 2024 | 0.997558 | 0.999247±0.000203 | -8.33 |
77	| 0.25 | all | 0.997049 | 0.999370±0.000163 | -14.26 |
78	| 0.30 | 2023 | 0.998865 | 0.999648±0.000041 | -19.02 |
79	| 0.30 | 2024 | 0.997229 | 0.999084±0.000227 | -8.16 |
80	| 0.30 | all | 0.996451 | 0.999219±0.000244 | -11.35 |
81	| 0.38 | 2023 | 0.998644 | 0.999499±0.000065 | -13.18 |
82	| 0.38 | 2024 | 0.995266 | 0.998777±0.000326 | -10.76 |
83	| 0.38 | all | 0.996645 | 0.998850±0.000241 | -9.16 |
84	
85	
86	## Part 4: Top Rank Movers (all models, full → stable-only)
87	
88	### Biggest rank *drops* (benefited from DIF items)
89	
90	| Model | Family | Method | Rank Full | Rank Stable | ΔRank |
91	|-------|--------|--------|-----------|-------------|-------|
92	| Sao10K/14B-Glacier-Stack | unknown | unknown | 555 | 1406 | +851 |
93	| AA051611/A0118 | unknown | unknown | 1169 | 1996 | +827 |
94	| DeepMount00/phi_3 | phi-3 | unknown | 736 | 1545 | +809 |
95	| Mihaiii/Pallas-0.5-frankenmerge | unknown | unknown | 455 | 1264 | +809 |
96	| DeepMount00/Phi-3-Mini-4K-Boost | phi-3 | unknown | 738 | 1546 | +808 |
97	| vonjack/phi-3-mini-4k-instruct-llamafied | phi-3 | unknown | 534 | 1334 | +800 |
98	| vonjack/Phi-3-mini-4k-instruct-LLaMAfied | phi-3 | unknown | 533 | 1330 | +797 |
99	| nbeerbower/llama-3-dragonmaid-8B-v2 | llama-3 | unknown | 576 | 1369 | +793 |
100	| raincandy-u/phillama-3.8b-v0.1 | llama-3 | unknown | 733 | 1500 | +767 |
101	| nbeerbower/llama-3-stinky-8B | llama-3 | unknown | 553 | 1300 | +747 |
102	| cognitivecomputations/yayi2-30b-llama | unknown | unknown | 469 | 1202 | +733 |
103	| cstr/llama3-8b-spaetzle-v13 | llama-3 | unknown | 705 | 1437 | +732 |
104	| shyamieee/JARVIS-v1.0 | unknown | unknown | 616 | 1345 | +729 |
105	| Nitral-AI/Poppy_Porpoise-0.96-L3-8B | unknown | unknown | 712 | 1430 | +718 |
106	| nbeerbower/llama-3-stella-8B | llama-3 | unknown | 588 | 1287 | +699 |
107	| FairMind/Phi-3-mini-4k-instruct-bnb-4bit-Ita | phi-3 | unknown | 956 | 1651 | +695 |
108	| rhysjones/Phi-3-mini-mango-1-llamafied | phi-3 | unknown | 563 | 1258 | +695 |
109	| GeorgiaTech/0.0005_llama_nodpo_3iters_bs128_531lr_ | unknown | unknown | 495 | 1182 | +687 |
110	| KnutJaegersberg/YaYi-30b-EverythingLM | yi | unknown | 887 | 1568 | +681 |
111	| Qwen/Qwen1.5-14B-Chat | qwen-1.5 | unknown | 591 | 1272 | +681 |
112	
113	### Biggest rank *gains* (hurt by DIF items)
114	
115	| Model | Family | Method | Rank Full | Rank Stable | ΔRank |
116	|-------|--------|--------|-----------|-------------|-------|
117	| liminerity/Blurstral-7b-slerp | unknown | unknown | 1410 | 823 | -587 |
118	| DreadPoor/PAIN_LeDestroy-7B-task_arithmetic | unknown | unknown | 1186 | 619 | -567 |
119	| flammenai/flammen26-mistral-7B | mistral | unknown | 1335 | 793 | -542 |
120	| Gille/StrangeMerges_2-7B-slerp | unknown | unknown | 1320 | 801 | -519 |
121	| jambroz/sixtyoneeighty-7b | unknown | unknown | 1270 | 782 | -488 |
122	| jambroz/sixtyoneeighty-7b-chat | unknown | unknown | 1271 | 783 | -488 |
123	| Gille/StrangeMerges_12-7B-slerp | unknown | unknown | 1347 | 860 | -487 |
124	| antiven0m/reverie-7b | unknown | unknown | 1288 | 805 | -483 |
125	| GreenNode/GreenNodeLM-7B-v2leo | unknown | unknown | 1333 | 852 | -481 |
126	| jambroz/sixtyoneeighty-7b-dpo | nan | DPO | 1303 | 835 | -468 |
127	| DreadPoor/Sphinx-7B-Model_Stock | unknown | unknown | 1282 | 817 | -465 |
128	| SanjiWatsuki/Kunoichi-DPO-7B | nan | DPO | 1314 | 857 | -457 |
129	| Inv/Konstanta-V4-Alpha-7B | unknown | unknown | 1231 | 777 | -454 |
130	| allknowingroger/LimyQstar-7B-slerp | unknown | unknown | 987 | 534 | -453 |
131	| mncai/mistral-7b-dpo-v6 | mistral-0.1 | DPO | 1202 | 756 | -446 |
132	| Gille/StrangeMerges_17-7B-dare_ties | unknown | unknown | 1491 | 1051 | -440 |
133	| Vasanth/Valor_Macaroni_moe | unknown | unknown | 1284 | 859 | -425 |
134	| flammenai/flammen27-mistral-7B | mistral | unknown | 939 | 523 | -416 |
135	| nbeerbower/bruphin-iota | unknown | unknown | 1215 | 803 | -412 |
136	| rishiraj/oswald-2x7b | unknown | unknown | 1731 | 1327 | -404 |
137	
138	
139	## Part 5: Cross-Cohort Super-Family Accuracy Shifts
140	
141	Super-families in both cohorts: 8
142	
143	- Mean |Δaccuracy| on full benchmark: 0.0900
144	- Mean |Δaccuracy| on stable items:   0.0863
145	- Mean |Δaccuracy| on DIF items:      0.0983
146	- Ratio stable/full: 0.9581
147	- Ratio DIF/full: 1.0919
148	- DIF items show *larger* cross-cohort accuracy swings → they capture temporal instability.
149	
150	| Super-family | N23 | N24 | Δacc full | Δacc stable | Δacc DIF |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5fcf3e2-f1bf-4f43-96a4-261b4106b8f7",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "f8858bc8-972f-4358-b6a1-7477ca7a09c0",
  "sourceToolAssistantUUID": "d5fcf3e2-f1bf-4f43-96a4-261b4106b8f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T02:08:19.389Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Mf9bUwtUeoa2P1A7CEVF5P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step3_report.md",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8858bc8-972f-4358-b6a1-7477ca7a09c0",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu5Ccx1539kv9o83veR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "374de670-88a0-4fa8-bae6-38758d5209f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GYUts9DGrpLCMgDxyHSxm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5334,
      "cache_read_input_tokens": 58393,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5334
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 341,
          "cache_read_input_tokens": 58393,
          "cache_creation_input_tokens": 5334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5334,
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

_source line 36 · 2026-05-21T02:08:19.396Z_

<details><summary>↩ Tool result · `toolu_01Mf9bUwtUeoa2P1A7CEVF5P`</summary>

```text
1	# Plan 004 Step 3: GSM1K Contamination Gap × DIF Flag Correlation
2	
3	## Summary
4	
5	**Core finding**: Pearson r = −0.478 (p = 0.005). The correlation is significant and exceeds the |r| > 0.3 threshold, but the direction is **negative** — opposite to the contamination hypothesis. Models with larger GSM8K–GSM1K gaps show *less* advantage on DIF-C items, not more.
6	
7	## Data
8	
9	| Component | Count |
10	|-----------|-------|
11	| Matched models (in both GSM1K paper and MetaBench response matrix) | 33 |
12	| DIF-C items (standard matching, ETS class C) | 249 |
13	| Non-DIF items (ETS class A + B) | 1070 |
14	| Excluded: tiiuae/falcon-180B-chat (not in MetaBench) | 1 |
15	
16	## Main Analysis
17	
18	| Metric | Value | p-value |
19	|--------|-------|---------|
20	| Pearson r | −0.478 | 0.005 |
21	| Spearman ρ | −0.403 | 0.020 |
22	
23	All 33 models (except Deepseek-math-7b-rl) show **negative DIF advantage** — accuracy on DIF-C items is consistently lower than on non-DIF items. Models with larger contamination gaps show even more negative DIF advantage.
24	
25	## Control Analyses
26	
27	### Partial Correlation (controlling GSM8K overall accuracy)
28	
29	| Metric | Value | p-value |
30	|--------|-------|---------|
31	| Partial r | −0.385 | 0.027 |
32	
33	The correlation survives after controlling for overall accuracy, ruling out the confound that "strong models do better on everything."
34	
35	### Permutation Test (n = 1000)
36	
37	| Metric | Value |
38	|--------|-------|
39	| Observed r | −0.478 |
40	| Null mean | −0.007 |
41	| Null SD | 0.197 |
42	| Null 95% CI | [−0.383, 0.366] |
43	| Empirical p (two-tailed) | 0.014 |
44	
45	The observed correlation falls outside the null distribution's 95% CI. The DIF-C item set produces a significantly stronger negative correlation with contamination gap than random item subsets of the same size.
46	
47	### DIF-C Directionality Analysis
48	
49	DIF-C items split by direction (α_MH relative to 1):
50	
51	| Subset | n | Mean advantage | r with gap | p |
52	|--------|---|----------------|------------|---|
53	| DIF-C favoring reference (older, α>1) | 78 | +0.031 | −0.143 | 0.429 |
54	| DIF-C favoring focal (newer, α<1) | 171 | −0.194 | −0.347 | 0.048 |
55	
56	The overall negative correlation is driven primarily by the 171 focal-favoring DIF-C items (α<1, easier for 2024 models). These items capture genuine generational capability gains, yet high-contamination models struggle disproportionately on them — contamination's "shallow" boost fails to generalize to items that discriminate real ability. The 78 reference-favoring items show no significant relationship with contamination gap.
57	
58	## Outlier Analysis
59	
60	### Cook's Distance (top 5)
61	
62	| Model | Cook's D | Gap | DIF Advantage |
63	|-------|----------|-----|---------------|
64	| Deepseek-math-7b-rl | 0.300 | −0.022 | +0.003 |
65	| GPT-2-xl | 0.161 | 0.004 | −0.001 |
66	| Smaug-2-72B | 0.129 | 0.061 | −0.069 |
67	| Gemma-2b-it | 0.075 | −0.001 | −0.033 |
68	| Deepseek-llm-67b-base | 0.071 | 0.093 | −0.155 |
69	
70	Deepseek-math-7b-rl is the most influential point (negative gap, near-zero DIF advantage).
71	
72	### Leave-One-Out
73	
74	| Removed model | r without | Δr |
75	|---------------|-----------|-----|
76	| Deepseek-math-7b-rl | −0.374 | −0.105 |
77	| Smaug-2-72B | −0.537 | +0.058 |
78	| Gemma-2b-it | −0.438 | −0.040 |
79	| Mistral-7B-Instruct-v0.2 | −0.516 | +0.038 |
80	| GPT-2-xl | −0.442 | −0.037 |
81	
82	Removing Deepseek-math-7b-rl weakens the correlation to r = −0.374, but it remains significant (still > 0.3). No single point drives the result; the correlation is robust.
83	
84	## Model Family Observations
85	
86	| Family | n | Mean gap | Mean DIF advantage |
87	|--------|---|----------|--------------------|
88	| Smaug | 2 | 0.065 | −0.128 |
89	| Phi | 4 | 0.037 | −0.174 |
90	| Gemma | 5 | 0.051 | −0.143 |
91	| Llama/CodeLlama | 9 | 0.028 | −0.117 |
92	| Mixtral | 4 | 0.028 | −0.143 |
93	| DeepSeek | 2 | 0.036 | −0.076 |
94	
95	No single family dominates the trend. Phi models show high DIF disadvantage but moderate gaps. Gemma models cluster at moderate gap + moderate DIF disadvantage. The correlation is not an artifact of one family.
96	
97	## Interpretation
98	
99	### Against the contamination hypothesis
100	
101	The original hypothesis predicted **positive** correlation: contaminated models should gain disproportionate advantage on DIF-C items. The observed **negative** correlation (r = −0.478) contradicts this.
102	
103	### What DIF-C items capture
104	
105	DIF-C items are not simply "contaminated items." They are items with large differential functioning between temporal cohorts. 171/249 DIF-C items have α_MH < 1, meaning they are *easier* for focal (2024) models — these items capture genuine generational capability improvements. The remaining 78 items (α>1) favor reference (2023) models.
106	
107	The negative correlation (r = −0.347, p = 0.048) on the 171 focal-favoring items reveals a key insight: contaminated models (high GSM8K–GSM1K gap) perform *worse* on exactly the items that differentiate real capability gains. This suggests:
108	
109	1. DIF items capture genuine capability differences between model generations, not contamination artifacts
110	2. Contamination produces a "shallow" performance boost that fails to generalize to items requiring real problem-solving improvement
111	3. DIF analysis identifies construct-relevant item differences — items where true ability matters most
112	
113	### The negative correlation means
114	
115	Models with higher contamination gaps (suspected contamination) do *worse* on DIF items — they show a narrower advantage pattern concentrated on non-DIF items. Contamination produces a uniform boost on "normal" items but fails on items with atypical difficulty characteristics that genuinely discriminate between capability levels.
116	
117	### Success criteria assessment
118	
119	| Criterion | Result |
120	|-----------|--------|
121	| \|r\| > 0.3 (breakthrough) | ✅ \|r\| = 0.478 |
122	| Direction as hypothesized | ❌ Negative, not positive |
123	| Survives controls | ✅ Partial r = −0.385, permutation p = 0.014 |
124	
125	**Verdict**: The effect size meets the breakthrough threshold, but the direction inverts the contamination narrative. DIF-C items do not flag contaminated content — they flag items where contaminated models are actually *weaker*. This is still a strong, publishable finding: it demonstrates that DIF analysis captures genuine measurement anomalies orthogonal to contamination, supporting DIF as a tool for identifying construct-relevant item differences rather than data leakage.
126	
127	## Output Files
128	
129	- `gsm1k_dif_correlation.csv` — per-model data (33 rows)
130	- `fig_gsm1k_dif_correlation.png/pdf` — scatter plot with regression
131	- `fig_gsm1k_dif_perm_null.png` — permutation null distribution
132	- `plan_004_step3_gsm1k_dif_correlation.py` — analysis script
133	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "374de670-88a0-4fa8-bae6-38758d5209f6",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "c9d69370-df57-4d1e-a85d-17505b807a9d",
  "sourceToolAssistantUUID": "374de670-88a0-4fa8-bae6-38758d5209f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-21T02:08:22.201Z_

Now let me read the review context file to understand the experiment plan fully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9d69370-df57-4d1e-a85d-17505b807a9d",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu5ucHbmjKC5sRiQjHa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e6f6a57-4b5d-437d-9f45-e9156ee94bbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHYxfuP9N9hve5xsU1ShLz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10783,
      "cache_read_input_tokens": 63727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10783,
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

_source line 38 · 2026-05-21T02:08:24.150Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FR86Ykt7CYnCo1E9m73tUh`</summary>

```json
{
  "pattern": "**/review_context*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e6f6a57-4b5d-437d-9f45-e9156ee94bbd",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu5ucHbmjKC5sRiQjHa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9b9b364-3ff7-4a3b-b1de-76bc874927e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHYxfuP9N9hve5xsU1ShLz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10783,
      "cache_read_input_tokens": 63727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10783,
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

_source line 39 · 2026-05-21T02:08:24.172Z_

<details><summary>↩ Tool result · `toolu_01FR86Ykt7CYnCo1E9m73tUh`</summary>

```text
artifacts/dream_reports/dream_20260520T194223/best/review_context.yaml
artifacts/dream_reports/dream_20260520T194223/median/review_context.yaml
artifacts/dream_reports/dream_20260520T194223/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T205007/best/review_context.yaml
artifacts/dream_reports/dream_20260520T205007/median/review_context.yaml
artifacts/dream_reports/dream_20260520T205007/worst/review_context.yaml
artifacts/dream_reports/dream_20260521T012912/best/review_context.yaml
artifacts/dream_reports/dream_20260521T012912/median/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9b9b364-3ff7-4a3b-b1de-76bc874927e6",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "568acef7-8124-4a57-b2ed-21ffaa8a2be7",
  "sourceToolAssistantUUID": "c9b9b364-3ff7-4a3b-b1de-76bc874927e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T02:08:25.151Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XBTVYEfVmFYJHMmVa4RGac`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_0.md",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "568acef7-8124-4a57-b2ed-21ffaa8a2be7",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu5ucHbmjKC5sRiQjHa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18740fdb-6323-415e-a65a-fb95dc645041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHYxfuP9N9hve5xsU1ShLz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10783,
      "cache_read_input_tokens": 63727,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10783
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 63727,
          "cache_creation_input_tokens": 10783,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10783,
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

_source line 41 · 2026-05-21T02:08:25.157Z_

<details><summary>↩ Tool result · `toolu_01XBTVYEfVmFYJHMmVa4RGac`</summary>

```text
1	---
2	round: 0
3	review_mode: 
4	overall_score: borderline
5	timestamp: 2026-05-20T21:51:43.210272+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	
12	# 圆桌审稿报告 — Round 1
13	
14	**论文**: "Psychometric Detection and Regeneration of Contaminated LLM Benchmark Items: DIF-Based Detection, Multi-Signal Ensemble, and IRT-Equated Benchmark Regeneration"
15	
16	**审稿组**: R1（Methods & Experiments）+ R2（Novelty & Related Work）
17	**日期**: 2026-05-20
18	**轮次**: Round 1（初审 + 交叉回应，1 轮收敛）
19	
20	---
21	
22	## Summary
23	
24	本文将 LLM 基准测试污染检测重新定义为心理测量学问题，利用差异项目功能（DIF）在 5,219 模型 × 12,508 MMLU 题目的大规模矩阵上检测污染项目。论文构建了 DIF+ConStat 集成检测器（AUROC 0.72），提出半合成验证框架，并通过 bifactor IRT 等值进行基准再生（holdout ρ=0.91）。实验覆盖 11 个组件，从 IRT 拟合诊断到退化分析，构成完整技术栈。
25	
26	---
27	
28	## Strengths
29	
30	**S1. 跨学科概念贡献** [共识]
31	将心理测量学中成熟的 DIF 方法论引入 LLM 污染检测，是一个有实际价值的概念桥梁。DIF 在群体层面运作，对单模型输出平滑具有理论上的天然鲁棒性（§3.2, Table 3: DIF AUROC 0.82-0.91 vs ConStat 0.51-0.75 on RL models）。两位 Reviewer 均认可此论点。
32	
33	**S2. 分析规模与覆盖面** [共识]
34	5,219 模型 × 12,508 题目是目前已知最大的 IRT-for-LLM 分析之一。11 个实验组件系统覆盖从检测到再生的完整技术栈。
35	
36	**S3. 架构异质性诊断** [共识]
37	Table 5 展示 full-population RMSEA=0.105 vs decoder-only 0.068，分层后 spurious DIF 减少 24%（Table 6）。R2 在交叉回应中承认初审低估了这一诊断工作的价值。
38	
39	**S4. 诚实报告负面结果** [共识]
40	DVD AUROC 0.56、κ=0.14 外部验证、within-family 46% overlap 均如实呈现。在同类工作中属于高标准的透明度。
41	
42	**S5. 退化分析** [共识]
43	Table 18 给出明确操作阈值（~35% 替换为临界点），ρ 以 ~0.003/百分点线性退化，为实际部署提供可规划的安全边界。
44	
45	---
46	
47	## Weaknesses
48	
49	### Critical（影响接收决定）
50	
51	**WC1. DIF 标记效度验证严重不足** [共识: R1+R2]
52	- MMLU-CF 验证 κ=0.14 本质上是随机一致水平，几乎没有验证价值
53	- GSM8K 交叉验证 r=0.36（Table 11）解释变异不到 13%，仅为暗示性佐证
54	- Within-family 46% overlap 意味着过半 DIF 标记可能由架构差异或能力增长驱动，而非真正的污染
55	- 论文未提供正式的 precision 估计；PPV ≈ 0.55 意味着约半数标记为假阳性
56	- **底线**：如果无法区分"真污染"和"能力进步"，整个检测管线的可信度是未知的
57	
58	**WC2. 推理-RL 鲁棒性声明严重欠缺统计效力** [共识: R1+R2]
59	- 推理-RL 分析仅基于 13 个模型，AUROC 估计 95% CI 约为 ±0.15-0.20
60	- DeLong p=0.002 是在 alignment-RL（N=477）上报告的，**不是**推理-RL（N=13），存在统计推断误导
61	- 推理-RL 恰恰是论文声称最重要的前沿场景，但证据最薄弱
62	- 13 个模型的 family 分布未披露，可能存在选择偏差
63	
64	**WC3. 半合成验证存在循环性风险** [共识: R1+R2]
65	- "200 clean items" 的选取标准不明——如果用 DIF 相关指标筛选 clean items 再评估 DIF，则 TPR 估计向上偏倚
66	- Semi-synthetic TPR "consistently exceeds pure simulation by 3-8bps" 可能恰好反映了 existing contamination 的叠加效应
67	- 无法证明选取独立性时，整个 semi-synthetic validation 的说服力大打折扣
68	
69	**WC4. 2PL 局部独立性假设可能严重违反** [共识: R1+R2]
70	- MMLU 57 个学科内部题目高度相关，严重违反 2PL 局部独立性假设
71	- 核心 DIF 分析（§3-4）使用普通 2PL，未检测或处理局部依赖
72	- 违反局部独立性会膨胀 MH 统计量，导致 DIF 假阳性率升高——与 WC1 叠加
73	- 论文在 §7.1 的 bifactor 模型中处理了这个问题，但未在核心检测阶段应用
74	- RMSEA 0.068（decoder-only 分层后）仍处于"可接受"边缘（标准 ≤0.06 为"良好"）
75	
76	### Warning（影响评分但不一票否决）
77	
78	**WW1. 引用准确性存疑** [分歧: R2=critical, R1=minor]
79	- R2 指出 "Iron-Fenced Trees (Tets & Berger, 2016)" 应为 "Item-Focussed Trees (Tutz & Berger, 2016)"，以及 DVD 引用的作者/年份不符
80	- R1 反驳称论文写的是 "Item-Focused Trees"（美式拼写变体），"Iron-Fenced Trees" 在论文中不存在；可能存在的是 author name typo（Totz/Tets → Tutz）
81	- **Director 判断**：存在事实争议，需作者逐一核查所有引用。如仅为拼写 typo 则属 camera-ready 级修正；如存在虚构引用则严重性显著提升。Wang et al. (2026) 引用同样无法独立核实（R1、R2 均同意此关切）。
82	
83	**WW2. 新颖性定位偏差** [分歧缩窄: R1=4/6, R2=3/6]
84	- DIF 是 1988 年的经典技术，论文未对其做任何适配 LLM 场景的技术修改
85	- 对有心理测量学背景者，"contamination = DIF" 的映射近乎显然
86	- Growing Pains (Zhang et al., 2026) 已建立 "IRT for LLM evaluation" 范式，进一步降低概念桥梁的非显然性
87	- **但**：对 ML 社区多数研究者而言 DIF 是陌生工具，完整管线（检测→集成→验证→等值→再生→退化分析）超越了单一方法应用
88	- **Director 判断**：论文当前 framing 偏向方法论贡献声明，在 DIF 本身无创新的情况下略显 overclaiming。建议重新定位为"实证发现驱动的系统论文"
89	
90	**WW3. 与 Growing Pains 区分不足** [共识: R1+R2]
91	- 两者在 IRT 建模层面高度相似，论文仅一句话带过
92	
93	**WW4. 多处不可核实引用** [共识: R1+R2]
94	- Wang et al. (2026) 无法通过搜索找到完全匹配的论文
95	- DVD "Dunn et al. (2024)" 的作者/年份可能不符
96	
97	**WW5. MH 程序选择未论证** [共识: R1+R2]
98	- 仅检测 uniform DIF，对 non-uniform DIF 不敏感
99	- 未与 logistic regression DIF、SIBTEST 等替代方案对比
100	
101	**WW6. 多重比较校正缺失** [共识: R1+R2]
102	- 12,508 个 MH 检验未提及 FDR 控制
103	- α=0.05 下预期约 625 个假阳性，可能部分解释 46% within-family overlap
104	
105	**WW7. ETS A/B/C 阈值未校准** [R2 提出]
106	- 直接沿用人类测试标准，未讨论对 LLM 群体的适用性
107	
108	---
109	
110	## Reviewer Consensus [AGREE]
111	
112	以下问题两位 Reviewer 达成完全共识：
113	
114	1. **DIF 效度验证是核心瓶颈**（κ=0.14 + 46% overlap）——论文最需要回应的问题
115	2. **N=13 推理-RL 无法支撑核心贡献声明**——需 bootstrap CI 或扩大样本
116	3. **半合成验证的 clean items 选取需证明独立性**
117	4. **2PL 局部独立性需诊断**（Yen's Q3 或在 bifactor 上重做 DIF）
118	5. **缺失关键相关工作**：Lalor et al. (2019)、Vania et al. (2021)、Min-K%++ (Shi et al., 2024)、Balloccu et al. (2024)
119	6. **Wang et al. (2026) 引用需提供可核实信息**
120	7. **退化分析的实用价值**——Table 18 的 ~35% 临界点是有操作价值的发现
121	8. **诚实报告负面结果**值得肯定
122	
123	---
124	
125	## Reviewer Divergence [REBUT]
126	
127	以下问题存在分歧，双方已充分论证：
128	
129	### 1. 引用错误严重性
130	- **R2**：至少 2 处引用严重错误（Iron-Fenced Trees、Tets），呈典型 LLM 幻觉特征，[critical] 级别
131	- **R1**：论文写的是 "Item-Focused Trees" 而非 "Iron-Fenced Trees"，R2 的核心指控本身有误；可能存在的 author name typo 属 camera-ready 级修正
132	- **Director 裁定**：降级为 warning。R2 的 "Iron-Fenced Trees" 指控存在事实争议，但引用准确性仍需全面核查。如核查后确认存在虚构引用则重新升级。
133	
134	### 2. 新颖性评分
135	- **R1**：4/6——跨学科概念桥接 + 大规模实证 + 完整管线
136	- **R2**：3/6——方法层面零创新，概念映射对有背景者近乎显然
137	- **Director 裁定**：3.5/6。论文有概念贡献和系统工程价值，但缺乏 DIF 方法本身的技术适配（如利用 logprob 的连续 DIF、处理 LLM 极端 response 的 robust MH）限制了新颖性上限。
138	
139	### 3. Ensemble 是正面贡献还是负面结果
140	- **R2**：Table 10 显示 DIF 单独 TPR 在 δ≥1.4 时已达 0.78，ensemble 未带来一致性提升
141	- **R1**：反驳——Table 10 完整数据显示 ensemble 在所有维度更优（δ≥1.4: 0.82>0.78; δ≥0.8: 0.72 vs 0.51; coverage: 73% vs 36%）；R2 选择性引用了单一维度
142	- **Director 裁定**：R1 的数据引用更完整，ensemble 在中等效应区间（δ≥0.8）确有实质性改善。但 DVD 信号贡献微弱，有效 ensemble 实际上是 DIF+ConStat 双信号系统。建议论文更精确地表述 ensemble 的组成和边际贡献。
143	
144	### 4. 再生题目质量退化
145	- **R1**：因子载荷 -18%、区分度 -19% 被低估，需 TIF 对比
146	- **R2**：反驳——论文在 Table 18 和 §7.3 中已系统量化退化，处理充分；缺 TIF 是有价值的补充但非 Major
147	- **Director 裁定**：同意 R2，退化处理基本充分，TIF 对比为可选补充。
148	
149	---
150	
151	## Questions for Authors
152	
153	1. **[高优先]** Within-family 46% overlap 的方向性：是 full-population DIF flags 包含 within-family flags，还是两者有不同的 flag 集合？方向性对结论有根本影响。
154	2. **[高优先]** κ=0.14（与 MMLU-CF 一致性）为何不构成对 DIF 方法的否定证据？如果认为 MMLU-CF 本身不可靠，需提供独立论证。
155	3. **[高优先]** 半合成验证中 clean items 的选取标准是什么？选取是否完全独立于 DIF 指标？
156	4. **[高优先]** 推理-RL 13 个模型的完整列表、family 分布、以及 N=13 下独立的 DeLong p 值或 bootstrap CI。
157	5. Bifactor 模型中学科特定因子的方差解释比例？general factor 占 62%，35 个学科因子各占多少？
158	6. IFT 的时间分割点（2023年9月）如何区分污染效应 vs GPT-4 发布后的自然能力跳跃？
159	7. ETS A/B/C 阈值（为人类校准）对 LLM 群体是否适用？是否进行过阈值敏感性分析？
160	8. 请确认所有引用的准确性，特别是：Tutz/Tets 拼写、DVD 引用来源、Wang et al. (2026) 的完整引用信息。
161	
162	---
163	
164	## Missing References
165	
166	两位 Reviewer 共同识别的缺失引用：
167	1. **Lalor et al. (2019)** "Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds" — IRT 应用于 NLP 的先驱工作
168	2. **Vania et al. (2021)** — 用 IRT 分析 NLU benchmark
169	3. **Shi et al. (2024) Min-K%++** — MIA 用于污染检测，与 DIF 的群体级方法形成 individual-level vs population-level 对比
170	4. **Balloccu et al. (2024)** "Leak, Cheat, Repeat" — 污染检测领域最近的综述
171	5. **N-gram/perplexity 基线方法** — 最简单的污染检测基线，论文未将 DIF 与之对比
172	
173	---
174	
175	## External Review (Stanford Agentic Reviewer)
176	
177	**状态：未请求。** 本轮未配置外部审稿。
178	
179	---
180	
181	## Visual Layout Check
182	
183	**状态：未启动。** 本轮未派发视觉审查 Agent。
184	
185	---
186	
187	## Overall Assessment
188	
189	### 评分汇总
190	
191	| 维度 | R1 (修正后) | R2 (修正后) | Director 综合 |
192	|------|-------------|-------------|---------------|
193	| Novelty | 4/6 | 3/6 | 3.5/6 |
194	| Soundness | 3/6 | 3/6 | 3/6 |
195	| Significance | 4/6 | 3.5/6 | 3.5/6 |
196	| Clarity | 4/6 | 3.5/6 | 3.5/6 |
197	| Reproducibility | 3/6 | 2.5/6 | 2.5/6 |
198	| **Overall** | **4/6** | **3/6** | **3.5/6** |
199	
200	### 总体判断：**Borderline** (3.5/6)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18740fdb-6323-415e-a65a-fb95dc645041",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "e71720fb-6033-40b1-b740-ecf08d01f2a2",
  "sourceToolAssistantUUID": "18740fdb-6323-415e-a65a-fb95dc645041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-21T02:08:28.357Z_

Now I have sufficient material for a thorough review. Let me also check the experiment summary for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e71720fb-6033-40b1-b740-ecf08d01f2a2",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu6LBQBQ6W3TTY3YgfL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c688c69-7448-41b5-9af9-574c6bec8fbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XdrMGWzJSToVseY1JqNCi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5738,
      "cache_read_input_tokens": 74510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5738,
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

_source line 43 · 2026-05-21T02:08:29.661Z_

<details open><summary>🔧 Tool call — Read · `toolu_011aYBBvRzswHioiLC3riTPq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/experiment_summary.md",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c688c69-7448-41b5-9af9-574c6bec8fbb",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu6LBQBQ6W3TTY3YgfL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c94ae7ad-0790-4bb6-89d2-6b9633a0ebcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XdrMGWzJSToVseY1JqNCi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5738,
      "cache_read_input_tokens": 74510,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5738
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 74510,
          "cache_creation_input_tokens": 5738,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5738,
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

_source line 44 · 2026-05-21T02:08:29.667Z_

<details><summary>↩ Tool result · `toolu_011aYBBvRzswHioiLC3riTPq`</summary>

````text
1	# Experiment Summary: IRT-Equated Benchmark Regeneration
2	
3	## Overview
4	
5	This project investigated whether Differential Item Functioning (DIF) analysis — a psychometric technique from educational testing — can detect benchmark contamination in LLMs. Starting from the hypothesis that MH-DIF could identify differentially contaminated items between temporal cohorts (2023 vs 2024 models), we ran a systematic chain of 11 experiments on the METABENCH dataset (5227 models × 12508 MMLU items).
6	
7	The core finding is a pivot: temporal DIF does not primarily detect contamination but reflects **genuine capability improvement** across model generations. Three independent approaches to reduce the 31% baseline DIF rate all failed (matched-ability, θ-conditioning, within-subject isolation), while semi-synthetic injection validated that the DIF methodology itself works correctly (ΔTPR=+0.674). The project pivoted from "DIF as contamination detector" to "psychometric characterization of LLM benchmark item instability" — the first large-scale quantification of how benchmark items behave differentially across model generations.
8	
9	## Experiment Chain
10	
11	### MVP Phase 1: DIF Power Simulation (Synthetic)
12	- **Exp ID**: mvp_dif_power_sim
13	- **Hypothesis**: MH + Logistic Regression DIF achieves TPR≥0.70, FPR≤0.10 at N≥50-80/group, δ≥1.0 logits on synthetic 2PL IRT data
14	- **Result**: BH-corrected p-value detection FAIL (TPR 0.04-0.07). ETS C classification conditional PASS: TPR=0.72-0.85 at N≥80, δ≥1.4; FPR<0.05; AUC=0.91-0.96
15	- **Conclusion**: Conditional success — ETS C replaces p-value as primary detector (D001)
16	- **Story contribution**: Established operational parameters (N≥80, δ≥1.4) and the ETS C classification as the primary DIF detection criterion
17	
18	### MVP Phase 2: DIF Power Simulation (Real IRT Parameters)
19	- **Exp ID**: mvp_dif_power_sim_phase2
20	- **Hypothesis**: ETS C maintains TPR≥0.65, FPR≤0.10 at N≥80, δ≥1.4 with real MMLU 2PL parameters from PSN-IRT
21	- **Result**: TPR=0.68 (N=80,δ=1.4) to 0.80 (N=100,δ=1.6); FPR=0.036-0.042; AUC=0.93
22	- **Conclusion**: Success — real parameter distributions degrade TPR by 3-6pp, within tolerance (D002)
23	- **Story contribution**: Validates DIF power under realistic item parameter distributions; recommends N≥100 as primary operating point
24	
25	### Plan 001: Real-Data MH-DIF on METABENCH MMLU
26	- **Exp ID**: plan_001_real_data_dif_mmlu
27	- **Hypothesis**: Temporal cohort MH-DIF flags items enriched in Li et al. contaminated set (enrichment >1.0, FPR≤0.05)
28	- **Result**: Temporal C%=31.3%, enrichment=0.96 (no enrichment); ability C%=2.9%, enrichment=1.19; within-family Llama-2 vs 3 C%=61.3%; domain ρ=0.307 (p=0.02); sanity random-split C%=0.18%
29	- **Conclusion**: Negative — temporal DIF detects systematic capability improvement, not contamination (D004)
30	- **Story contribution**: Key negative finding that motivated the entire pivot. The 31.3% temporal C% becomes the headline number for "item instability." Domain ρ=0.307 shows DIF is capability-driven. Sanity check (0.18%) proves the method isn't broken.
31	
32	### Plan 001b: Matched-Ability Temporal DIF
33	- **Exp ID**: plan_001b_matched_ability_dif
34	- **Hypothesis**: Within each accuracy quintile, temporal DIF enrichment rises to >1.5 after controlling for ability
35	- **Result**: All quintile enrichments 0.94-1.04
36	- **Conclusion**: Negative — ability matching cannot isolate contamination signal (D005)
37	- **Story contribution**: Eliminates "ability confound" as the sole explanation. Reviewer insight: Li et al. web-overlap is global contamination (available to all models), fundamentally incompatible with DIF which measures differential effects.
38	
39	### Plan 011: Semi-Synthetic DIF Validation
40	- **Exp ID**: plan_011_semi_synthetic_validation
41	- **Hypothesis**: MH-DIF detects injected differential contamination (focal-only incorrect→correct flips) with TPR>0.5, FPR<0.05 on ability cohort
42	- **Result**: Temporal+external: ΔTPR=+0.674 (0.326→1.000), FPR constant at 0.314; clear dose-response across p={0.3,0.5,0.7,1.0}; matching variable contamination discovered (standard MH FPR 0.298→0.616 at 20% injection, anchor/external immune)
43	- **Conclusion**: Success — DIF methodology validated; plan_001 failure attributed to ground truth mismatch (D006)
44	- **Story contribution**: The decisive validation experiment. Proves DIF works for differential contamination. Reinterprets Li et al. enrichment≈1.0 as "global vs differential contamination" insight (conceptual contribution). Matching variable contamination finding motivates external/anchor matching.
45	
46	### Plan 012: IRT θ-Conditioning
47	- **Exp ID**: plan_012_irt_theta_conditioning
48	- **Hypothesis**: Logit θ stratification (10-20 bins) reduces temporal baseline FPR from 31% to <10% while maintaining TPR>0.70
49	- **Result**: θ corr with total score = 0.9986; temporal FPR = 31-35% across all variants (no improvement); ability cohort θ-bins reduce FPR 49%→8% but TPR collapses 76%→21% (proving plan_011 ability TPR was mostly ability confounding)
50	- **Conclusion**: Negative — 1D θ ≡ total score, cannot reduce temporal FPR (D008)
51	- **Story contribution**: Proves temporal DIF is genuinely multidimensional — 1D ability cannot explain it. Corrects plan_011 ability cohort interpretation: 73% of apparent TPR was ability confounding.
52	
53	### Plan 013: Yen's Q3 Local Independence Diagnostic
54	- **Exp ID**: plan_013_q3_local_independence
55	- **Hypothesis**: Within-subject Q3 mean > 0.20, significantly higher than cross-subject, explaining part of 31% FPR
56	- **Result**: Within-subject mean Q3=0.0086 (below threshold), but 11.3% of pairs |Q3|>0.20 (vs 2.2% cross-subject, 5x ratio, Mann-Whitney p=2.3e-9); worst subjects: moral_scenarios 34.2%, world_religions 18%, marketing 17.5%
57	- **Conclusion**: Partial — local dependence exists but is moderate; not the primary driver of 31% FPR
58	- **Story contribution**: Addresses reviewer concern about IRT assumptions. Local dependence is a contributing factor but insufficient to explain 31% FPR, strengthening the "genuine temporal DIF" interpretation. Identifies specific problematic subjects for Discussion section.
59	
60	### Plan 014: Within-Subject Temporal DIF (Bifactor Pre-Check)
61	- **Exp ID**: plan_014_within_subject_dif
62	- **Hypothesis**: Within-subject C% < 15% in high-C% subjects, indicating between-subject ability differences drive overall C%
63	- **Result**: Average within-subject C%=38.1% (range 31.1-45.2%); cross-subject C%=40.5% (Δ=-2.4pp); all 5 subjects exceed 25% threshold
64	- **Conclusion**: Negative — temporal DIF penetrates into every subject; bifactor model cannot solve FPR (D010)
65	- **Story contribution**: Proves temporal DIF is pervasive and item-specific, not an artifact of between-subject ability differences. The 38.1% within-subject figure is a robustness check for the 31.3% global finding. Kills bifactor direction before wasting compute.
66	
67	### Plan 015: Bifactor IRT (Killed)
68	- **Exp ID**: plan_015_bifactor_irt
69	- **Hypothesis**: Bifactor (1 general + 57 subject factors) reduces temporal FPR to <15%
70	- **Conclusion**: Killed based on plan_014 pre-check (D010) — within-subject C%=38.1% proves bifactor cannot solve the problem
71	- **Story contribution**: Demonstrates methodological rigor — pre-mortem analysis saved compute and confirmed the exhaustive nature of the investigation
72	
73	### Plan 016: Within-Subject Semi-Synthetic Injection
74	- **Exp ID**: plan_016_within_subject_semi_synthetic
75	- **Hypothesis**: Within-subject DIF still detects injected contamination (ΔTPR>0.3 at p=0.5), validating plan_014's 38% as genuine
76	- **Result**: Cross-subject matching 4/5 subjects ΔTPR>0.3 at p=0.5; ΔFPR=0.000 across all 5 subjects (completely stable); within-subject matching 3/5 pass but FPR inflates +0.067 to +0.281
77	- **Conclusion**: Success — DIF works at subject level; cross-subject matching eliminates FPR inflation (D011)
78	- **Story contribution**: Final validation. Cross-subject ΔFPR=0.000 is a clean methodological contribution (solves matching variable contamination at subject level). Confirms plan_014's 38% is real temporal DIF, not method failure.
79	
80	### Plan 017: Downstream Impact (Preparing)
81	- **Exp ID**: plan_017_downstream_impact
82	- **Hypothesis**: Removing DIF-flagged items (~31% of MMLU) improves cross-generation model ranking stability (Spearman ρ), significantly better than random removal baseline
83	- **Status**: PREPARING
84	- **Story contribution**: Answers the "so what?" question — if DIF-flagged items cause ranking instability, removing them improves benchmark quality, providing downstream evidence for DIF as a benchmark quality tool
85	
86	## Decision Chain (D001-D012)
87	
88	```
89	D001 (ETS C > p-value) → D002 (MVP pass) → D003 (Dream #1)
90	    → D004 (temporal DIF = capability, not contamination)
91	        → D005 (matched-ability fails)
92	            → D006 (semi-synthetic validates DIF method)
93	                → D007 (story pivot: global vs differential contamination)
94	                    → D008 (θ-conditioning fails, 1D exhausted)
95	                        → D009 (Dream #2: bifactor is last hope)
96	                            → D010 (within-subject C%=38%, bifactor killed)
97	                                → D011 (pivot confirmed, cross-matching ΔFPR=0.000)
98	                                    → D012 (story finalized: benchmark quality tool)
99	```
100	
101	Three failed remediation directions:
102	1. **D005**: Matched-ability DIF → enrichment still ~1.0
103	2. **D008**: IRT θ-conditioning → θ ≡ total score (r=0.9986), FPR unchanged
104	3. **D010**: Bifactor pre-check → within-subject C%=38.1% > overall 31.3%
105	
106	## Key Numbers for Paper
107	
108	| Metric | Value | Source | Paper use |
109	|--------|-------|--------|-----------|
110	| METABENCH dataset size | 5227 models × 12508 items | data | Section 3 (Data) |
111	| Temporal C% (ETS C flagged) | 31.3% | plan_001 | Key finding: item instability rate |
112	| Ability C% | 2.9% | plan_001 | Contrast: ability-based DIF well-controlled |
113	| Li et al. enrichment (temporal) | 0.96 | plan_001 | Global vs differential contamination |
114	| Li et al. enrichment (ability) | 1.19 | plan_001 | Weak positive in ability cohort |
115	| Within-family C% (Llama-2 vs 3) | 61.3% | plan_001 | Impact-vs-DIF confound demonstration |
116	| Domain specificity ρ(C%, ΔAcc) | 0.307 (p=0.02) | plan_001 | Capability-driven DIF evidence |
117	| Sanity check C% (random split) | 0.18% | plan_001 | Method validity |
118	| Semi-synthetic ΔTPR (temporal, p=1.0) | +0.674 | plan_011 | Core validation: DIF detects differential contamination |
119	| Semi-synthetic FPR stability | 0.314 → 0.314 | plan_011 | FPR constant under injection |
120	| Semi-synthetic dose-response p=0.5 | TPR=0.834 | plan_011 | Detection at moderate effect |
121	| Matching variable contamination ΔFPR | 0.298 → 0.616 | plan_011 | Motivates external matching |
122	| θ–total score correlation | 0.9986 | plan_012 | 1D θ ≡ total score |
123	| Ability cohort corrected TPR (θ-bins) | 21% (was 76%) | plan_012 | 73% of ability TPR was confounding |
124	| Q3 within-subject |Q3|>0.20 | 11.3% (vs 2.2% cross) | plan_013 | Local dependence: moderate, not primary |
125	| Worst Q3 subject (moral_scenarios) | 34.2% pairs |Q3|>0.20 | plan_013 | Discussion: problematic subjects |
126	| Within-subject temporal C% (average) | 38.1% (range 31-45%) | plan_014 | Robustness: DIF pervasive within domains |
127	| Within vs cross-subject Δ | -2.4pp | plan_014 | Signal robust to matching choice |
128	| Cross-matching ΔFPR (all subjects) | 0.000 | plan_016 | Method: FPR completely stable |
129	| Cross-matching subjects with ΔTPR>0.3 | 4/5 at p=0.5 | plan_016 | Subject-level detection works |
130	| Within-matching FPR inflation at p=1.0 | +0.067 to +0.281 | plan_016 | Motivates cross-matching |
131	| MVP ETS C TPR at N=100, δ=1.6 | 0.80 | mvp_phase2 | Power analysis: method is powered |
132	| MVP ETS C FPR range | 0.036-0.042 | mvp_phase2 | Controlled false positive rate |
133	
134	## Evidence Chain Summary
135	
136	**Conclusion: Temporal DIF = genuine capability improvement, not contamination artifact.**
137	
138	The evidence chain:
139	
140	1. **DIF works** (plan_011): Semi-synthetic injection with known differential contamination yields ΔTPR=+0.674, perfect dose-response, and constant FPR — the methodology is sound.
141	
142	2. **But temporal DIF doesn't align with contamination labels** (plan_001): Enrichment=0.96 against Li et al. web-overlap labels. This is because web-overlap is *global* contamination (available to all models via Common Crawl), which by definition cannot produce group-specific DIF.
143	
144	3. **31% is not an ability-matching artifact**:
145	   - Matched-ability DIF still shows enrichment≈1.0 (plan_001b)
146	   - IRT θ is indistinguishable from total score (r=0.9986), finer binning doesn't help (plan_012)
147	   - Within-subject C%=38.1% — higher than global 31.3%, ruling out between-subject confounds (plan_014)
148	   - Local dependence (Q3) is moderate (11.3% >0.20) but insufficient to explain 31% (plan_013)
149	
150	4. **The method is validated at subject level** (plan_016): Cross-subject matching achieves ΔFPR=0.000 across all 5 tested subjects, with 4/5 showing ΔTPR>0.3 at p=0.5 injection level.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c94ae7ad-0790-4bb6-89d2-6b9633a0ebcc",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "01634e01-729d-4ae4-bac1-3a87d0f0aa93",
  "sourceToolAssistantUUID": "c94ae7ad-0790-4bb6-89d2-6b9633a0ebcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-21T02:08:33.187Z_

I now have comprehensive understanding of the paper, its experimental evidence, internal decision chain, and the prior dream review. Let me write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01634e01-729d-4ae4-bac1-3a87d0f0aa93",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu6fcCQ2Xd9WVgHXWqj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6166d1a1-b1a1-4678-b58a-51f82602c4a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGBtMYwznXd2TPLvGet7Ft",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4568,
      "cache_read_input_tokens": 80248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4568,
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

_source line 46 · 2026-05-21T02:08:38.381Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QwPnxCLUqC113hXWpDLW2u`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6166d1a1-b1a1-4678-b58a-51f82602c4a9",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu6fcCQ2Xd9WVgHXWqj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35378bc4-6e6d-4377-b444-4e87447266e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGBtMYwznXd2TPLvGet7Ft",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4568,
      "cache_read_input_tokens": 80248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4568,
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

_source line 47 · 2026-05-21T02:08:38.395Z_

<details><summary>↩ Tool result · `toolu_01QwPnxCLUqC113hXWpDLW2u`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ROADMAP.md\", \"content\": \"# irt_equated_bench_regen — Research Dashboard\\n\\n> 最后更新: 2026-05-21 01:28 UTC | 更新原因: D014 plan_004 Step 3 GSM1K 完成 + paper_framing.md 更新\\n\\n## 核心方向\\n**Pivot 完成 (D011)**：从\\\"DIF 检测方法\\\"转向\\\"LLM benchmark psychometric characterization + DIF methodology\\\"。ICLR 2027 目标不变。详见 paper_framing.md。\\n\\n**GSM1K 结果 (D014)**：DIF flags 与 contamination gap 显著负相关（r=−0.478, p=0.005）。DIF 不标记 contamination，而是标记 contamination 无法到达的 capability-discriminative items。强化 \\\"diagnostic lens\\\" 叙事。\\n\\n## 当前进展\\n- **阶段**: **Writing**（全部实验完成）\\n- **实验**: 12 完成（5 success / 5 negative / 0 failed），plan_004 全 3 步完成\\n- **Key results**:\\n  - MMLU: semi-synthetic ΔTPR=+0.508 | cross-subject ΔFPR=0.000 | within-subject C%=38.1% | downstream z=-8 to -49σ\\n  - GSM8K: temporal C%=18.9% | semi-synthetic ΔTPR=+0.818 | GSM1K gap r=−0.478 (p=0.005)\\n- **Paper Agent**: writing_plan.yaml 审批通过，figures 4/6 完成 + fig_1/fig_4 进行中\\n- **审稿**: Round 1 borderline 3.5/6，14 issues tracked\\n\\n## 近期任务\\n- [ ] Agent: 修正 Step 3 report 方向标签（Reviewer CRITICAL）\\n- [ ] Paper Agent: 更新 writing_plan.yaml 整合 GSM8K/GSM1K 章节 + 新 figure\\n- [ ] Paper Agent: 完成 fig_1（统一 \\\"2024-H1\\\" → \\\"2024\\\"）+ fig_4\\n- [ ] Paper Agent: Step 3 正文写作\\n- [ ] Post-pivot Dream（Step 3 完成后，写作定稿前评估 ICLR viability）\\n\\n## Completed\\n- ✅ plan_001-017: 10 个 MMLU 实验全部完成\\n- ✅ plan_004 Step 1-3: GSM8K cross-benchmark 验证全部完成\\n- ✅ 文献调查 22 篇 + experiment_summary.md + artifacts QC\\n- ✅ paper_framing.md 更新至 D014（Claim 4 four-layer, Claim 3 cross-benchmark）\\n- ✅ writing_plan.yaml 审批通过，figures fig_2/3/A1/A2 完成\\n\\n## GPU 预算\\nP0: 250h | P1: 350h | 已用: 0h（全部 CPU analysis）\\n无 GPU 需求。\\n\\n## 投稿目标\\nICLR 2027（~2026年10月 DDL）— 不降级\\n评估: main borderline 5.5-6/6, findings solid 6.5-7/6。GSM1K negative r 不升级为 validated method，但 cross-benchmark evidence chain 显著加强 characterization paper 深度。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D014 | 2026-05-21 | plan_004 Step 3 GSM1K: |r|=0.478 显著但方向为负——DIF 不标记  | plan_004_gsm8k_cross_benchmark, plan_017_downstream_impact |\\n| D013 | 2026-05-21 | plan_017 downstream impact negative 但 informative： | plan_017_downstream_impact |\\n| D012 | 2026-05-20 | Story 定稿：Candidate 1 (benchmark quality tool) + gr | plan_014_within_subject_dif, plan_016_within_subject_semi_synthetic, plan_001_real_data_dif_mmlu |\\n| D011 | 2026-05-20 | Pivot 拍板：从\\\"DIF 检测方法\\\"转向\\\"LLM benchmark psychometric  | plan_016_within_subject_semi_synthetic, plan_014_within_subject_dif, plan_011_semi_synthetic |\\n| D010 | 2026-05-20 | 方向 3 (Bifactor) pre-check 否定：within-subject tempor | plan_014_within_subject_dif, plan_011_semi_synthetic |\\n| D009 | 2026-05-20 | Dream #2 分析：best=3/6, median=3-4/6, worst=3/6。跨档一致 | dream_20260520T205007 |\\n| D008 | 2026-05-20 | 方向 2 (IRT θ-conditioning) 失败，1D 路线穷尽。plan_011 abil | plan_012_irt_theta_conditioning |\\n| D007 | 2026-05-20 | Story pivot: semi-synthetic validation 作为核心效度证据，Li | plan_011_semi_synthetic, plan_001_real_data_dif_mmlu, plan_001b_matched_ability_dif |\\n| D006 | 2026-05-20 | plan_011 positive: MH-DIF 检测差异性污染有效 (p=0.5 TPR=0.8 | plan_011_semi_synthetic |\\n| D005 | 2026-05-20 | 方向 1 (matched-ability DIF) 失败确认，所有 quintile enrich | plan_001b_matched_ability_dif |\\n\\n\\n\", \"total_chars\": 3101, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35378bc4-6e6d-4377-b444-4e87447266e4",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a2ffc38510f39fa08",
  "type": "user",
  "uuid": "2bdbf6a2-e979-4bb7-8512-25895a1be3e0",
  "sourceToolAssistantUUID": "35378bc4-6e6d-4377-b444-4e87447266e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-21T02:10:23.093Z_

Now I have a thorough understanding of the full paper, its experimental infrastructure, the decision chain, and prior review context. Here is my review.

---

**Summary:** This paper applies the Mantel-Haenszel DIF procedure from classical psychometrics to the METABENCH response matrix (5,227 models x 12,508 MMLU items) to characterize item-level behavioral drift across model generations. It reports that 38% of items exhibit large DIF (ETS C), that web-overlap contamination labels are mismatched for evaluating item-level differential detectors (enrichment ~1.0), and provides a semi-synthetic validation framework with cross-subject matching. The paper repositions DIF items as diagnostic markers of capability evolution rather than contamination indicators.

---

**Strengths:**

- **S1. Unprecedented scale and systematic experimental design.** 5,227 models x 12,508 items is the largest psychometric analysis of an LLM benchmark. The experimental chain (11 completed experiments with a clear decision graph D001-D014) is unusually thorough and well-documented. The sanity check (random-split C%=0.18% vs temporal 31.3%) is a model of good experimental practice.

- **S2. The ground truth meta-critique (Claim 2) is the paper's most valuable contribution.** The argument that web-overlap labels measure global exposure (a static, model-agnostic property) while DIF detects differential functioning (a dynamic, group-specific signal) is both correct and consequential. The enrichment ~1.0 result combined with semi-synthetic ΔTPR=+0.508 provides a clean empirical demonstration. This observation genuinely affects how the community should evaluate contamination detection papers.

- **S3. Cross-subject matching (ΔFPR=0.000) is a clean methodological contribution.** The insight that matching on within-subject total score contaminates the matching variable is subtle and the fix (match on OTHER subjects) is simple, effective, and empirically validated across 5 subjects. The within-subject FPR inflation (+0.186) provides a concrete demonstration of the problem. This is independently useful infrastructure.

- **S4. Architecture stratification transforms an objection into a recommendation.** The decoder-only restriction (C% drops from 31.3% to 22.1%, RMSEA from 0.082 to 0.037, CFI to 0.93) is the most methodologically satisfying experiment. It simultaneously addresses model fit concerns and demonstrates that the method is refinable.

- **S5. Honest treatment of negative results throughout.** The paper reports three failed structural corrections (matched-ability, theta-conditioning, bifactor pre-check), the negative downstream impact hypothesis (DIF items carry MORE discriminative signal, not less), and the inverted GSM1K correlation (r=-0.478). The transparent framing of these as empirical observations rather than hiding them is commendable and above the venue average.

- **S6. DIF as diagnostic lens (Claim 4) is well-supported by two independent evidence lines.** The z=-8 to -49 sigma ranking disruption comparison (21/21 conditions) and the GSM1K anti-correlation (r=-0.478, p=0.005, partial r=-0.385) converge on the same interpretation. The reframing from "find bad items and remove" to "understand what changed" is intellectually productive.

---

**Weaknesses:**

- **W1 (Major). The 38% headline finding is substantially confounded and its interpretability is unclear.** The acknowledged rho=0.307 between C% and domain-level accuracy improvement means item "instability" and "models getting better" are entangled. More critically, the paper does not attempt to decompose this correlation: no partial correlation analysis, no regression decomposition, no attempt to identify what fraction of the 38% remains after partialing out capability improvement. The paper acknowledges this honestly in limitations but still leads with 38% as the headline result. A reviewer can reasonably ask: if most of the instability is just progress, is this a temporal comparability concern or evidence that benchmarks are working correctly? The paper needs either a decomposition or a substantially more qualified framing. *The architecture-stratified 22.1% is the more defensible number but is presented as secondary.*

- **W2 (Major). ETS threshold sensitivity analysis is absent.** The ETS C threshold (|Delta_MH| >= 1.5) was calibrated for human educational testing populations and is applied without recalibration to LLM populations that have fundamentally different ability distributions (e.g., near-random to near-ceiling on the same test). The 38% number is entirely anchored to this threshold. The paper does not report C% at alternative thresholds (1.0, 2.0, 2.5). Without this sensitivity analysis, a reader cannot assess whether the qualitative finding (substantial instability) is robust to threshold choice. This is a straightforward analysis that could be done in hours and its absence is surprising.

- **W3 (Major). Poor IRT model fit for the full-population analysis undermines the core DIF statistics.** The full-population RMSEA=0.082, with no reported CFI or TLI, represents mediocre model fit. MH-DIF conditions on total score as a proxy for latent ability, but when the underlying IRT model fits poorly, total-score conditioning may not adequately control for ability differences. The architecture-stratified analysis (RMSEA=0.037, CFI=0.93) substantially improves fit, but the paper presents the full-population 31.3%/38% as the primary findings rather than the better-fitting 22.1%. The paper should either lead with the architecture-stratified numbers or provide a formal argument for why MH-DIF is robust to model misspecification in this regime.

- **W4 (Major). Multiple testing correction is not addressed.** 12,508 simultaneous MH chi-squared tests are performed. The ETS classification's dual requirement (effect size + significance) likely provides implicit multiplicity protection, but this argument is never made explicit. At alpha=0.05, approximately 625 false positives are expected by chance alone. The sanity check (C%=0.18% on random split, i.e., ~22 items) suggests the problem may be controlled in practice, but the paper should either formally show that ETS C controls FDR or apply standard corrections and report the impact on C%.

- **W5 (Moderate). Only uniform DIF is detected.** The MH procedure detects only constant difficulty shifts (uniform DIF) across ability levels. Non-uniform DIF -- where item functioning differences vary by model ability -- is plausible in this setting: stronger models may be more likely to have encountered specific items during training, creating ability-dependent contamination effects. No logistic regression DIF, SIBTEST, or other non-uniform DIF method is compared. The IFT analysis in the appendix partially addresses this (Jaccard=0.76 with categorical DIF), but IFT is not a direct test for non-uniform DIF either. The exclusive reliance on MH without justification is a gap.

- **W6 (Moderate). The semi-synthetic injection model is oversimplified.** Flipping incorrect-to-correct responses at rate p models contamination as deterministic answer knowledge. Real contamination may manifest as partial knowledge (improved probability of selecting the correct answer among distractors rather than certainty), distractor elimination (ruling out some wrong answers without knowing the right one), or format/template memorization (recognizing question structure). The ΔTPR numbers likely overestimate detection power for realistic contamination patterns. The dose-response relationship is clean for this specific injection model but may not transfer to more nuanced contamination mechanisms. The paper acknowledges this in limitations but does not explore alternative injection models.

- **W7 (Moderate). The Bayesian DIF section (5.5) is purely simulation-based and underdeveloped.** No validation on actual temporal METABENCH data. Prior specification, batch ordering sensitivity, and threshold sensitivity are underexplored. The Bayes factor threshold of 3.2 is presented without sensitivity analysis. This section reads as a separate, premature contribution. It could be cut entirely without weakening the paper's core story.

- **W8 (Moderate). RL robustness claim is severely underpowered (N=13).** The TOST equivalence p=0.11 fails the standard equivalence threshold and the DeLong p=0.087 is marginal. Claiming DIF is "robust to reasoning-RL" on N=13 models exceeds what the data support. The paper appropriately hedges ("preliminary"), but the Discussion section (Section 6) still uses language like "barely perturbs DIF flags (Jaccard=0.88, TOST equivalence p=0.008)" -- noting the 0.008 figure in the tex appears to differ from the 0.11 in the review summary. This discrepancy needs clarification. Regardless, N=13 cannot support robust conclusions about RL invariance.

- **W9 (Minor). GSM1K cross-benchmark validation has limited statistical power.** N=33 models yields wide confidence intervals (approximately [-0.70, -0.17] at 95% for r=-0.478). The result is directionally convincing and leave-one-out robust (min |r|=0.374), but the paper should report the confidence interval explicitly rather than just the point estimate and p-value. Using "contamination gap" (GSM8K - GSM1K accuracy) as a proxy for contamination is an assumption: the gap could reflect distributional differences between GSM8K and GSM1K items rather than contamination per se.

- **W10 (Minor). Pilot studies (bifactor equating, item generation) are too immature for main-text inclusion.** The bifactor equating (CFI=0.87 below the 0.90 threshold, TLI=0.89 marginal, equated rho=0.93 below the 0.95 target) and item generation (difficulty rho=0.64 below published benchmarks of 0.75-0.82) are presented in Future Work but with enough detail to suggest they are contributions. They are not. They are preliminary explorations that fall short of their own success criteria. Moving them to a clearly delineated appendix would sharpen the paper.

- **W11 (Minor). Related work coverage of the psychometric literature is thin for a paper claiming to bridge psychometrics and ML.** The measurement invariance literature (Meredith 1993, Vandenberg & Lance 2000) is entirely absent -- DIF is a special case of scalar invariance testing and this connection should be drawn. MIMIC models (Muthen 1985) and propensity-score matching for DIF (Teresi et al. 2007) are mentioned as future work but not discussed as existing alternatives. Lord's chi-squared and Raju's area DIF methods are not compared. The justification for choosing MH over these alternatives amounts to "simplicity and robust statistical properties" -- insufficient for a paper positioning itself at the intersection of two fields.

---

**Questions for Authors:**

1. What is C% at alternative ETS thresholds (|Delta_MH| >= 1.0, 2.0, 2.5)? Does the qualitative finding of substantial instability (>15%) survive at stricter thresholds? This is the single most important missing analysis.

2. Can you decompose the 38% instability by partialing out subject-level accuracy improvement (rho=0.307)? What fraction of DIF-flagged items remain after controlling for capability gains? A partial correlation or regression analysis at the item level (not just domain level) would be informative.

3. Why MH-DIF rather than logistic regression DIF, which handles continuous covariates and naturally detects non-uniform DIF? The theta-conditioning failure (plan_012) might have been avoided entirely with a different DIF method.

4. The TOST p-value for RL robustness appears as p=0.008 in the paper but p=0.11 in the review summary. Which is correct, and what is the equivalence margin used?

5. For cross-subject matching ΔFPR=0.000: is this exactly zero (to machine precision) or rounded? Across how many injection levels and random seeds? If exactly zero, this is suspiciously clean and warrants explanation.

6. How does excluding models below a minimum accuracy threshold (e.g., bottom 10%) affect C%? Near-random models may inflate DIF statistics if they contribute noise to the MH stratification.

7. What is the C% among the specific anchor items identified by Growing Pains? If their anchor items show low DIF, the complementary framing is strengthened; if high, the implication is different.

8. The paper states equated rho=0.965 for the bifactor model. However, the review summary states rho=0.93 "below target 0.95." Which is the correct number, and what accounts for the discrepancy?

---

**Missing Experiments / Analyses:**

1. **ETS threshold sensitivity analysis** -- C% at thresholds {1.0, 1.5, 2.0, 2.5}. This is the highest-priority gap because the 38% headline is entirely anchored to the 1.5 cutoff.

2. **Instability decomposition** -- partial correlation or item-level regression separating capability-improvement DIF from residual instability. The domain-level rho=0.307 is suggestive but the decomposition needs to happen at item level.

3. **Non-uniform DIF comparison** -- logistic regression DIF or SIBTEST on a representative subset, to assess whether restricting to uniform DIF misses a substantial fraction of differential functioning.

4. **Multiple testing formal analysis** -- either showing that ETS C classification implicitly controls FDR (via simulation or analytical argument) or applying BH correction and reporting the impact.

5. **Model quality filtering sensitivity** -- excluding bottom-quintile models and reporting C% to assess whether weak models inflate DIF statistics.

6. **Alternative injection models** -- at minimum, a probabilistic injection (increase P(correct) by delta rather than deterministic flip) to assess ΔTPR sensitivity to the contamination mechanism.

7. **Growing Pains anchor item overlap** -- testing C% among their specific anchor items to substantiate the claimed complementarity.

---

**Preliminary Score:** 4/6 (Weak Accept)

The paper addresses an important problem -- whether LLM benchmark item functioning is stable across model generations -- at unprecedented scale with commendable experimental rigor and intellectual honesty. The ground truth meta-critique (Claim 2), cross-subject matching innovation (Claim 3), and architecture stratification are genuine contributions. The "DIF as diagnostic lens" reframing (Claim 4) is supported by two independent evidence lines. However, the 38% headline rests on an uncalibrated threshold without sensitivity analysis (W2), the capability-improvement confound is acknowledged but not decomposed (W1), IRT model fit is poor for the primary analysis (W3), and multiple testing is not addressed (W4). These are addressable issues that do not invalidate the core contributions, but they currently prevent a fully confident acceptance. The paper is above average in honesty and experimental coverage but below the threshold in statistical rigor on several key points. A revision addressing W1-W4 would likely push this to a clear accept.

**Confidence:** 4/5. I have strong familiarity with DIF methodology and IRT, have read the full paper and all supporting experiment reports, and have cross-referenced claims against raw experimental data. My uncertainty stems primarily from not being able to assess the METABENCH data quality firsthand and from the unresolved TOST p-value discrepancy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bdbf6a2-e979-4bb7-8512-25895a1be3e0",
  "isSidechain": true,
  "agentId": "a2ffc38510f39fa08",
  "requestId": "req_011CbEu7L2ziGpcSbLGELbJQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98fbf843-1089-4b9d-abed-5a0620733a34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYRT1j2s53WfReYUXmLqMP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 84816,
      "output_tokens": 3673,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1902
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3673,
          "cache_read_input_tokens": 84816,
          "cache_creation_input_tokens": 1902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1902,
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
