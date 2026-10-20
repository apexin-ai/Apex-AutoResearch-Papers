# Research conversation: You are Reviewer 2 (R2) for an EMNLP 2026 ARR submission. Your focus: **Novelty and Related Work**. ## Venue Calibration

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a9f3d11ee2d7824d3.jsonl`
- **Structured JSON:** [`161338bc6cdfe1df69d0.json`](../../sessions/16/161338bc6cdfe1df69d0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-21T21:31:03.073Z_

You are Reviewer 2 (R2) for an EMNLP 2026 ARR submission. Your focus: **Novelty and Related Work**.

## Venue Calibration
EMNLP 2026 ARR Overall Assessment (1–5, half-point scale):
- 5 = Award consideration (top 2.5%)
- 4 = Conference accept
- 3 = Findings accept
- 2 = Resubmit next cycle
- 1 = Do not resubmit
Acceptance rate ~21%. Soundness (1-5), Excitement (1-5), Reproducibility (1-5).

## Paper Summary

**Title**: "G-MFRM: A Diagnostic Framework for Joint Detection of Judge Bias and Benchmark Contamination in LLM Evaluation"

**Problem**: LLM-as-a-judge evaluation has two problems studied in isolation: (1) inter-judge severity bias, (2) benchmark contamination. The paper argues sequential correction (addressing one then the other) introduces omitted variable bias when the two effects are non-orthogonal.

**Contributions**:
1. Proposition 1: Formal characterization of first-order confounding bias in sequential estimators. Bias ≈ ρ·σ_d·c̄·ē·f(N,J,I), validated by Monte Carlo across 120 settings.
2. G-MFRM framework: Extends MFRM with DG-IRT's gating mechanism (Sato et al., 2024) and externally anchored exposure indicators. 3-stage procedure: MFRM calibration → external exposure anchoring → joint gated model.
3. Empirical diagnostic: Current contamination is mitigated (c̄=0.14); framework provides monitoring readiness for future threats. Under adversarial injection, correction mode activates.

**Related Work Section (§7) covers**:
- Judge Bias Correction: CyclicJudge (Bai et al., 2024) — round-robin elimination; UDA (Kwon et al., 2024) — neural K-factor harmonization
- Benchmark Contamination: ConStat (De Koninck et al., 2024) — rephrase-based Δ-scores; DCR (Xu et al., 2024) — contamination factor survey; Pref Leakage (Dong et al., 2024) — preference data leakage
- Psychometric Models: IRT for NLG (Otani et al., 2016); DG-IRT (Sato et al., 2024) — gated contamination in educational testing
- Joint Modeling: Claims 0/12 surveyed papers jointly model both problems

**Key claim**: "To our knowledge, no prior work (0/12 surveyed papers through May 2026) jointly models judge bias and benchmark contamination within a single calibration framework."

**Key Results**:
- On real data: G-MFRM (τ=0.851) NOT significantly better than MFRM-only (τ=0.843, p=0.31). The contamination channel adds essentially nothing because c̄=0.14 is too weak.
- Prior-posterior KL divergence for c_n is only 0.08 — data provides negligible information about contamination beyond the prior.
- c_n has 22.7% misfit rate in facet fit diagnostics vs 0% for d_j.
- Cross-benchmark: d_j correlates r=0.78 across benchmarks (stable judge attribute), c_n correlates only r=0.35 (mostly noise).
- Under adversarial injection (5/22 models contaminated): G-MFRM τ=0.871 vs Seq 0.831 (p=0.008), demonstrating the correction mechanism works when signal is sufficient.
- Exposure indicators: only ~11% of items show significant exposure. Indicators have low inter-correlation (r=0.31 between ConStat and temporal).

**Paper framing**: "Diagnostic framework" — the main empirical finding is negative (contamination is currently negligible). The paper pivots to arguing this negative result is itself valuable as a diagnostic, and the framework provides monitoring readiness.

**Paper structure**: 7 pages. 8 references total. Limitations section present (covers generalization to other benchmarks, rank-1 assumption limitation, runtime ~5200s).

## Your Review Task

Evaluate the following dimensions thoroughly:

### 1. Novelty Assessment
- How novel is the G-MFRM model itself? It extends DG-IRT (Sato et al., 2024) with continuous exposure and multiple judge facets. Is this extension substantial or incremental?
- Is Proposition 1 (confounding bias in sequential estimators) a genuine theoretical contribution? Is the omitted variable bias framing for measurement models new?
- The "diagnostic framework" framing — is a framework that finds "no effect" publishable? What is the intellectual contribution when the main empirical result is null?
- How does the adversarial injection experiment compare to synthetic validation in prior work?

### 2. Related Work Completeness
- Are there important missing references? Consider:
  - Other IRT-based approaches for LLM evaluation beyond Otani et al. 2016
  - Other contamination detection methods (e.g., membership inference, perplexity-based, training data extraction)
  - Other multi-facet measurement models in NLP
  - Position bias correction methods (this paper mentions position swap but doesn't cite position bias literature)
  - Recent work on LLM judge calibration, self-consistency, etc.
- 8 references is extremely low for an EMNLP paper. Is the related work adequate?
- Is the "0/12 surveyed" claim verifiable? Is the gap genuine?

### 3. Framing and Positioning
- Is the "diagnostic framework" framing convincing, or does it feel like post-hoc rationalization of weak results?
- The paper's primary empirical finding is that contamination is negligible — is this finding novel or expected given recent training data curation practices?
- The "thermostat" metaphor — is this a genuine contribution or marketing?
- Does the paper oversell the adversarial result relative to the null real-data result?

### 4. Excitement (1-5)
- Will this paper influence future work?
- Does it provide actionable insights for practitioners?
- Is the research question important even if the answer is "currently no effect"?

### 5. Key Strengths (bullet points)

### 6. Key Weaknesses (bullet points, be specific)

### 7. Questions for Authors (numbered list)

### 8. Preliminary Scores
- Soundness: X/5
- Excitement: X/5
- Reproducibility: X/5
- Overall Assessment: X/5 (use the EMNLP scale above)
- Confidence: X/5

Format your response as a structured review. Be rigorous but fair. Calibrate to the 21% acceptance rate — a paper needs to be in roughly the top 1 in 5 to earn a conference accept score.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "eec19108-225d-421a-b9c9-40b4e57ea249",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T21:31:03.077Z_

```json
{
  "parentUuid": "eec19108-225d-421a-b9c9-40b4e57ea249",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
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
      "TodoWrite",
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
      "TodoWrite",
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
  "uuid": "9718e333-5d36-45ed-9caf-fa2a355d8c50",
  "timestamp": "2026-05-21T21:31:03.077Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T21:31:05.651Z_



I'll start by reading the paper and all relevant materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9718e333-5d36-45ed-9caf-fa2a355d8c50",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRkV6yYKkiBrxSfhRTD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a9f234a-56ab-45d3-93ce-1108c2d76cde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cq4fHtDkBmG8qvrhB11nch",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8276,
      "cache_read_input_tokens": 8248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8276,
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

_source line 4 · 2026-05-21T21:31:06.731Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01C4zRwL92RR5NugrMrgSVdM`</summary>

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
  "parentUuid": "3a9f234a-56ab-45d3-93ce-1108c2d76cde",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRkV6yYKkiBrxSfhRTD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19b05886-2ad7-4b32-9da4-e13d39fc458f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cq4fHtDkBmG8qvrhB11nch",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8276,
      "cache_read_input_tokens": 8248,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8276
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 107,
          "cache_read_input_tokens": 8248,
          "cache_creation_input_tokens": 8276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8276,
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

_source line 5 · 2026-05-21T21:31:06.734Z_

<details><summary>↩ Tool result · `toolu_01C4zRwL92RR5NugrMrgSVdM`</summary>

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
  "parentUuid": "19b05886-2ad7-4b32-9da4-e13d39fc458f",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "3ffe72d4-edfa-4fe1-9ab5-803e3604aaec",
  "sourceToolAssistantUUID": "19b05886-2ad7-4b32-9da4-e13d39fc458f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T21:31:09.383Z_



Let me read the paper and all supporting materials systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ffe72d4-edfa-4fe1-9ab5-803e3604aaec",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRkkuzbFZAVYfxZZWc2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fbbfd5b-e7d1-4615-8727-28517636d352",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018CMM2uFeqAZ4wE5cuQe3Dm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 7 · 2026-05-21T21:31:10.338Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011inHB2d6Yp9nn4zvWq4Vj4`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fbbfd5b-e7d1-4615-8727-28517636d352",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRkkuzbFZAVYfxZZWc2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "299e69cf-6590-4d7e-8e7b-8ff5328a1390",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018CMM2uFeqAZ4wE5cuQe3Dm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 8 · 2026-05-21T21:31:10.354Z_

<details><summary>↩ Tool result · `toolu_011inHB2d6Yp9nn4zvWq4Vj4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_003** (success): 同 mvp_002 DGP（c~HalfNormal(1.5), bimodal e, s~N(0,0.8), N=50, J=8, ρ=0.6），MCMC 调优（warmup=2000, samples=4000, chains=4, target_accept=0.95, non-centered parameterization）后收敛达标（R̂<1.05, ESS>100）且 joint 显著优于 sequential。 ← 基于 mvp_002\\n- **mvp_002** (negative): 放大 contamination 信号（c~HalfNormal(1.5), bimodal e, s~N(0,0.8), N=50, J=8）后，joint G-MFRM 在 item-level + judge-level confounding (ρ=0.6) 下对 θ_true 的恢复精度显著优于 sequential pipeline。 ← 基于 mvp_001\\n- **mvp_001** (negative): 当 d_j 与 c_n·e_i 存在 confounding（item-level + judge-level, ρ>0）时，joint G-MFRM 对 θ_true 的恢复精度（RMSE）显著优于 sequential pipeline，因为 joint estimation 避免了 contamination 效应被 d̂_j 和 b̂_i 吸收。\\n  [diagnosis_bias_scatter](rtx6000-4x:/root/gated_mfrm_judge_bias/mvp/diagnosis_bias_scatter.png)\\n\\n## 趋势\\n成功 1 / 负向 2 / 失败 0 / 共 3\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nrtx6000-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 998, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "299e69cf-6590-4d7e-8e7b-8ff5328a1390",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "9eba8fe9-c09d-421e-afa0-5812a65c384b",
  "sourceToolAssistantUUID": "299e69cf-6590-4d7e-8e7b-8ff5328a1390",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T21:31:11.279Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Ai1UHUJR4wNYrRniYp737H`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9eba8fe9-c09d-421e-afa0-5812a65c384b",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRkkuzbFZAVYfxZZWc2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b65d1f90-3e4f-47e7-acfc-3205954c603c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018CMM2uFeqAZ4wE5cuQe3Dm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 10 · 2026-05-21T21:31:11.292Z_

<details><summary>↩ Tool result · `toolu_01Ai1UHUJR4wNYrRniYp737H`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-21T16:40:00Z\\\"\\n  total_papers: 12\\ncategories:\\n  - key: \\\"psychometric_foundation\\\"\\n    name: \\\"Psychometric & IRT Foundation\\\"\\n    narrative: \\\"Core psychometric models: DG-IRT gating mechanism for cheating detection, MFRM applied to LLM raters, and IRT-based LLM evaluation frameworks\\\"\\n  - key: \\\"judge_bias_correction\\\"\\n    name: \\\"Judge Bias Correction\\\"\\n    narrative: \\\"Methods for detecting and correcting systematic biases in LLM-as-a-judge evaluation pipelines\\\"\\n  - key: \\\"contamination_detection\\\"\\n    name: \\\"Contamination Detection & Adjustment\\\"\\n    narrative: \\\"Methods for detecting and quantifying benchmark contamination in LLM evaluation\\\"\\n  - key: \\\"unified_evaluation\\\"\\n    name: \\\"Unified Evaluation Frameworks\\\"\\n    narrative: \\\"Comprehensive LLM evaluation frameworks and benchmarks that combine multiple assessment dimensions\\\"\\npapers:\\n  shu2013dgirt:\\n    title: \\\"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise\\\"\\n    authors:\\n      - \\\"Shu, Z.\\\"\\n      - \\\"Henson, R.\\\"\\n      - \\\"Luecht, R.\\\"\\n    year: 2013\\n    venue: \\\"Psychometrika\\\"\\n    doi: \\\"10.1007/s11336-012-9311-3\\\"\\n    bibtex_key: \\\"shu2013dgirt\\\"\\n    category: \\\"psychometric_foundation\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Core methodological inspiration. DG-IRT decomposes observed performance into genuine ability and cheating-inflated components via a gating mechanism. G-MFRM adapts this gating logic from educational cheating to LLM benchmark contamination.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  wang2025mfrm_llm:\\n    title: \\\"Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model\\\"\\n    authors:\\n      - \\\"Wang, Y.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2505.18486\\\"\\n    bibtex_key: \\\"wang2025mfrm_llm\\\"\\n    category: \\\"psychometric_foundation\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Most direct predecessor. Applies MFRM to compare 10 LLM raters with human experts, demonstrating MFRM's applicability to LLM judge calibration. Does NOT model contamination — the gap G-MFRM fills.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  lin2025psnirt:\\n    title: \\\"Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT\\\"\\n    authors:\\n      - \\\"Lin, Z.\\\"\\n    year: 2026\\n    venue: \\\"AAAI\\\"\\n    bibtex_key: \\\"lin2025psnirt\\\"\\n    category: \\\"psychometric_foundation\\\"\\n    role: \\\"baseline\\\"\\n    relevance: \\\"Neural 4PL IRT for LLM benchmark evaluation. Demonstrates scalability of IRT to LLMs but lacks judge facet and contamination modeling. Serves as IRT-based baseline without multi-facet structure.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  cyclicjudge2026:\\n    title: \\\"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    bibtex_key: \\\"cyclicjudge2026\\\"\\n    category: \\\"judge_bias_correction\\\"\\n    role: \\\"baseline\\\"\\n    relevance: \\\"Primary bias-only baseline. Eliminates judge bias via round-robin assignment but completely ignores contamination. G-MFRM addresses both jointly.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  fiedler2026bias_uncertainty:\\n    title: \\\"Bias and Uncertainty in LLM-as-a-Judge Estimation\\\"\\n    authors:\\n      - \\\"Fiedler, M.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2605.06939\\\"\\n    bibtex_key: \\\"fiedler2026bias_uncertainty\\\"\\n    category: \\\"judge_bias_correction\\\"\\n    role: \\\"related\\\"\\n    relevance: \\\"Introduces formal J/delta-J diagnostics for judge bias, identifies sign-reversal failure modes in shared-calibration comparisons. Stays within classical test theory. G-MFRM's confounding argument positions Fiedler's sign-reversal as downstream consequence of unmodeled contamination.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  soumik2026judging_judges:\\n    title: \\\"Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines\\\"\\n    authors:\\n      - \\\"Soumik, M.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2604.23178\\\"\\n    bibtex_key: \\\"soumik2026judging_judges\\\"\\n    category: \\\"judge_bias_correction\\\"\\n    role: \\\"related\\\"\\n    relevance: \\\"Empirically compares 9 debiasing strategies across 5 judges, finding style bias dominant (0.76-0.92). Provides no measurement model explaining why strategies work — G-MFRM provides the explanatory framework.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  uda2026:\\n    title: \\\"UDA: Unsupervised Debiasing Alignment for LLM Judges\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2026\\n    venue: \\\"AAAI\\\"\\n    bibtex_key: \\\"uda2026\\\"\\n    category: \\\"judge_bias_correction\\\"\\n    role: \\\"baseline\\\"\\n    relevance: \\\"Neural K-factor adjustment reducing inter-judge std by 63.4%. Black-box neural approach vs G-MFRM's interpretable psychometric approach. Key baseline for judge bias correction.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  constat2024:\\n    title: \\\"ConStat: Statistical Detection and Quantification of Benchmark Contamination\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS\\\"\\n    bibtex_key: \\\"constat2024\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"component\\\"\\n    relevance: \\\"Core component of G-MFRM Stage 2. Computes contamination effects via reference benchmark comparison (r^2=0.94 with true effects). Fully black-box, used to estimate per-item exposure e_i.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  dcr2025:\\n    title: \\\"DCR: Quantifying Data Contamination in LLMs Evaluation\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2025\\n    venue: \\\"EMNLP\\\"\\n    bibtex_key: \\\"dcr2025\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"baseline\\\"\\n    relevance: \\\"Adjusts accuracy for contamination via fuzzy inference but ignores judge effects. Primary contamination-only baseline for G-MFRM comparison.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  preference_leakage2026:\\n    title: \\\"Preference Leakage: A Contamination Problem in LLM-as-a-judge\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2026\\n    venue: \\\"ICLR\\\"\\n    bibtex_key: \\\"preference_leakage2026\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"related\\\"\\n    relevance: \\\"Quantifies generator-judge relatedness bias (judge-side contamination). Distinct from G-MFRM's examinee-side contamination. Preference Leakage's relatedness bias can be partially captured by G-MFRM's d_j facet.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  logprober2024:\\n    title: \\\"LogProber: Detecting Data Contamination via Token Log-Probability Analysis\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    bibtex_key: \\\"logprober2024\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"component\\\"\\n    relevance: \\\"Estimates per-item Safe Scores from token log-probabilities. Gray-box exposure indicator for G-MFRM Stage 2 (for models exposing logprobs).\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  zheng2023mtbench:\\n    title: \\\"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\\\"\\n    authors:\\n      - \\\"Zheng, L.\\\"\\n      - \\\"Chiang, W.-L.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS\\\"\\n    bibtex_key: \\\"zheng2023mtbench\\\"\\n    category: \\\"unified_evaluation\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Establishes LLM-as-a-judge paradigm and MT-Bench/Chatbot Arena benchmarks. Primary evaluation benchmark for G-MFRM validation. Human votes from Arena serve as ground truth for Kendall-tau comparison.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\", \"total_chars\": 7733, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b65d1f90-3e4f-47e7-acfc-3205954c603c",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "9c237b82-fd8e-4d59-b10b-5a2d96e0f829",
  "sourceToolAssistantUUID": "b65d1f90-3e4f-47e7-acfc-3205954c603c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T21:31:12.222Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014bb5KAV5Q34XkCHZ4hNLYY`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c237b82-fd8e-4d59-b10b-5a2d96e0f829",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRkkuzbFZAVYfxZZWc2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1d4c0f9-9e16-4905-92eb-b084b2ebfc35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018CMM2uFeqAZ4wE5cuQe3Dm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 12 · 2026-05-21T21:31:12.234Z_

<details><summary>↩ Tool result · `toolu_014bb5KAV5Q34XkCHZ4hNLYY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/paper_framing.md\", \"content\": \"# Paper Framing — gated_mfrm_judge_bias\\n\\n## Target Venue\\n- Primary: AAAI 2027 (full paper, deadline July 28, 2026)\\n- Backup: ACL 2027 via ARR (submission August 3, 2026)\\n- Timeline: ~68 days from today (2026-05-21)\\n\\n## Core Insight\\nSequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.\\n\\n## Core Claims (3 条，均可证伪)\\n\\n1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding.\\n\\n2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — jointly estimates model ability, item difficulty, judge severity, and contamination susceptibility in a single calibration, yielding bias-and-contamination-corrected \\\"fair scores.\\\"\\n\\n3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.\\n\\n## Story Spine\\n\\n- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.\\n\\n- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. No existing work (0/12 surveyed papers, through May 2026) jointly models both within a single calibration framework.\\n\\n- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external per-item exposure estimation via item-level performance gap (original vs reference variants) with difficulty correction, supplemented by temporal signals and LogProber where available, (3) joint gated model with e_i fixed and c_n as latent parameters. ConStat per-model delta serves as external validation of fitted c_n.\\n\\n- **Headline result template**: \\\"On MT-Bench/Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve X% higher Kendall-τ with Chatbot Arena human votes than the best sequential baseline, while simultaneously producing interpretable per-model contamination estimates and per-judge severity profiles.\\\"\\n\\n## Narrative Strategy (from distilled writing)\\n\\n- **Type**: \\\"突破局限\\\" (sequential has structural flaw) + \\\"统一框架\\\" (G-MFRM unifies both corrections)\\n- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)\\n- **Section 2**: Toy example / formal proposition demonstrating confounding before introducing G-MFRM method\\n- **Figure 1**: Left = sequential pipeline with confounding annotation, Right = joint G-MFRM with gating mechanism highlighted\\n- **Main result table**: rows = methods (7 baselines + G-MFRM), cols = benchmarks × metrics\\n- **Ablation**: Full numbers (not checkmark grid), rows = components on/off\\n\\n## Venue Fit Risks\\n\\n- **AAAI**: Good fit for psychometric methodology applied to AI evaluation. Risk: reviewers may lack MFRM/IRT background — need clear, self-contained exposition with toy examples. Strength: AAAI values formal modeling + practical impact.\\n- **ACL/ARR**: Good fit for LLM evaluation methodology. Risk: may demand stronger NLP-specific contributions beyond the measurement framework. Strength: directly relevant to LLM evaluation community.\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n1. **\\\"Why not CyclicJudge + discard contaminated items?\\\"** — Item discard wastes information; CyclicJudge doesn't capture item-specific judge effects; neither produces c_n for auditing; G-MFRM degrades gracefully to standard MFRM when contamination ≈ 0.\\n\\n2. **\\\"Is confounding large enough in practice?\\\"** — MVP synthetic: 43.8% RMSE degradation. Real-data calibration (P0 experiment) will establish realistic contamination magnitude. Bias scatter (r=0.65) shows the mechanism exists regardless of magnitude.\\n\\n3. **\\\"Rank-1 assumption (c_n·e_i) too strong\\\"** — Rank-1 is LLTM tradition, good approximation when contamination comes from dominant data source. Person-fit diagnostics (infit/outfit) detect violations. Rank-k extension is future work.\\n\\n4. **\\\"DG-IRT transfer is trivial\\\"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing.\\n\\n5. **\\\"Contamination signal realistic?\\\"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.\\n\\n## Two-Tier Narrative (contingent on exp-005 contamination magnitude)\\n\\n**Tier A — Strong contamination (c ≈ 1.0-1.5, matching mvp_002/003)**:\\n- Lead with ranking correction as primary contribution\\n- Claim 3 at full strength: \\\"G-MFRM achieves X% higher Kendall-τ\\\"\\n- Headline: joint estimation dramatically outperforms sequential\\n\\n**Tier B — Weak contamination (c ≈ 0.3-0.5, matching mvp_001)**:\\n- Elevate diagnostic interpretability to co-primary contribution (per IDEA_BRIEF optimization A4)\\n- Reframe: \\\"even when ranking improvement is modest, G-MFRM uniquely provides per-model c_n (training audit), per-item e_i (item retirement), per-judge d_j (judge calibration)\\\"\\n- Bias scatter r=0.65 proves the mechanism exists; practical impact scales with contamination magnitude\\n- Claim 3 softened to \\\"comparable or better rankings PLUS interpretable diagnostic outputs\\\"\\n\\nexp-005 determines which tier. Decision point: after exp-005 results, before paper writing.\\n\\n## MVP Evidence Summary\\n\\n- mvp_003: Joint RMSE −43.8% vs Sequential (p=1e-6), Kendall-τ +6.3pp, R̂=1.03, ESS=224\\n- Bias scatter: Pearson r=0.65 (sequential systematically overestimates high-c_n models)\\n- Robustness: method effective even under model misspecification (DGP with s_j, model without)\\n\", \"total_chars\": 7277, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1d4c0f9-9e16-4905-92eb-b084b2ebfc35",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "7fc56418-c140-4e26-bf1d-db51370c8c25",
  "sourceToolAssistantUUID": "b1d4c0f9-9e16-4905-92eb-b084b2ebfc35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T21:31:12.627Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XkRvvKWYDrvxKEBqrCpbTz`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fc56418-c140-4e26-bf1d-db51370c8c25",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRkkuzbFZAVYfxZZWc2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6a44612-11f3-4dbf-9bed-08877caed958",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018CMM2uFeqAZ4wE5cuQe3Dm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16524,
      "output_tokens": 414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1289
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 414,
          "cache_read_input_tokens": 16524,
          "cache_creation_input_tokens": 1289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1289,
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

_source line 14 · 2026-05-21T21:31:12.637Z_

<details><summary>↩ Tool result · `toolu_01XkRvvKWYDrvxKEBqrCpbTz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/ROADMAP.md\", \"content\": \"# gated_mfrm_judge_bias — Research Dashboard\\n\\n> 最后更新: 2026-05-21 20:49 UTC | 更新原因: MVP PASS, 进入 research 阶段, 完成 post-MVP kickoff Steps 1-4\\n\\n## 核心方向\\nG-MFRM 统一校正 LLM 评测中的 judge bias 和 contamination。核心 insight: sequential 方法中 judge severity 与 contamination 存在 omitted variable confounding，joint estimation 方法论必要。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-21 通过）\\n- MVP 验证链: mvp_001 (FAIL, 信号弱) → mvp_002 (效应强 p=1e-6, 收敛不达标) → mvp_003 (PASS: RMSE -43.8%, R̂=1.03, ESS=224)\\n- 偏差散点图 Pearson r=0.65 独立确认 omitted variable bias\\n- paper_framing.md ✅ | experiment_plan.yaml ✅ | Dream 模拟中 (dream_20260521T204917)\\n- 文献图谱 12 篇 + 蒸馏完成\\n\\n## 实验计划摘要（详见 experiment_plan.yaml）\\n| 优先级 | 数量 | GPU·h | 关键实验 |\\n|--------|------|-------|---------|\\n| P0 | 5 | 200 | 数据收集(130h) + ConStat(30h) + G-MFRM 拟合(15h) + Baseline(20h) + Contamination 校准(5h) |\\n| P1 | 4 | 35 | Judge 数量敏感性 + 指标消融 + Facet 诊断 + Formal proposition |\\n| P2 | 2 | 55 | WildBench 复制 + 对抗鲁棒性 |\\n| **Total** | **11** | **290** | Critical path: exp-001→002→003→004/005 |\\n\\n## 近期任务\\n- [ ] 等 Dream 模拟完成，审查结果决定是否调整 framing/plan\\n- [ ] Dream 通过后批准 P0 实验，exp-001 + exp-009 可并行启动\\n- [ ] exp-001: 多 judge 数据收集（开源 judge vLLM 推理 + proprietary API）\\n- [ ] exp-009: Formal bias proposition（纯计算，不依赖数据）\\n\\n## GPU 预算\\n4x RTX 6000 96G (rtx6000-4x)，已绑定。\\nP0 实验 ~200 GPU·h，4 卡并行 ~50h wall clock (~2 天)。\\nProprietary API ~$900。\\n\\n## 目标会议\\n- AAAI 2027: July 28, 2026（~68 天）\\n- ACL 2027 ARR: August 3, 2026（~74 天）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D004 | 2026-05-21 | MVP PASS，进入 research 阶段 | mvp_003 |\\n| D003 | 2026-05-21 | mvp_002 核心效应验证成功（Joint RMSE -32.8%, p=1e-6），收敛未达标， | mvp_001, mvp_002 |\\n| D002 | 2026-05-21 | MVP FAIL 但不 kill，启动 DGP 参数诊断 | mvp_001 |\\n| D001 | 2026-05-21 | MVP 采用合成数据恢复实验验证 joint estimation 优势 | — |\\n\\n\\n\", \"total_chars\": 1780, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6a44612-11f3-4dbf-9bed-08877caed958",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "cd772e75-c069-41ad-9422-f5ebb52fd510",
  "sourceToolAssistantUUID": "f6a44612-11f3-4dbf-9bed-08877caed958",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T21:31:17.251Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TpJcEbHLn5b68xxupJQwFH`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd772e75-c069-41ad-9422-f5ebb52fd510",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRmCC1ryS8NwAJ69qC5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52231644-3978-4dad-aeb6-dc79661eba5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmqfqV8YE4vN2Tg5k7PPru",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7964,
      "cache_read_input_tokens": 17813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7964,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 16 · 2026-05-21T21:31:17.260Z_

<details><summary>↩ Tool result · `toolu_01TpJcEbHLn5b68xxupJQwFH`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'gated_mfrm_judge_bias'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52231644-3978-4dad-aeb6-dc79661eba5b",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "e2e0bb8d-540b-4425-acdd-a378b087c7ca",
  "sourceToolAssistantUUID": "52231644-3978-4dad-aeb6-dc79661eba5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T21:31:17.640Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011z4v5Ehymgg7mL2BUH8qbq`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2e0bb8d-540b-4425-acdd-a378b087c7ca",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRmCC1ryS8NwAJ69qC5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac11eec1-a0da-47b1-bc61-f64935536049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmqfqV8YE4vN2Tg5k7PPru",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7964,
      "cache_read_input_tokens": 17813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7964,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 18 · 2026-05-21T21:31:17.652Z_

<details><summary>↩ Tool result · `toolu_011z4v5Ehymgg7mL2BUH8qbq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/memory.md\", \"content\": \"# Memory — gated_mfrm_judge_bias\\n\\n## MVP 验证链 (2026-05-21)\\n\\n### mvp_001: 信号太弱 → FAIL\\nc~HalfNormal(0.5), sigmoid(e), N=20, J=5。joint vs sequential Δ=0.0008, p=0.39。contamination 项仅占 logit ~10-15%。\\n\\n### mvp_002: 方法有效但 MCMC 不收敛 → FAIL (技术性)\\nc~HalfNormal(1.5), bimodal e, s~N(0,0.8), N=50, J=8, ρ=0.6。joint RMSE 降 32.8%, p=1e-6。但 ESS=47<100, R̂=1.05 边界。\\n\\n### mvp_003: MCMC 调优 → **PASS** ✅\\n同 mvp_002 DGP + warmup=2000, samples=4000, chains=4, target_accept=0.95, NCP for c。\\n- joint RMSE=0.1243±0.016 vs sequential=0.2211±0.038 → **降 43.8%, p=1e-6**\\n- joint τ=0.9223±0.010 vs sequential=0.8593±0.029 → +6.3pp\\n- R̂=1.03, ESS=224 → 收敛完全达标\\n- MCMC 调优不仅修复收敛，还提升了估计精度（mvp_002 joint RMSE=0.1486 → mvp_003=0.1243, -16.4%）\\n\\n### 散点图确认 omitted variable bias\\nmvp_001 ρ=0.6: Pearson r=0.6534 (p≈0)。高 c_n 的 model 被 sequential 系统性高估 θ。\\n\\n### 关键经验\\n- contamination 信号需要足够强（c_scale≥1.5, bimodal e）才能暴露 sequential 的缺陷\\n- NCP + target_accept=0.95 对 HalfNormal 约束参数的 MCMC 收敛至关重要\\n- 4 chains 比 2 chains 在 ESS 上提升巨大（47→224），不只是线性翻倍\\n- JAX CPU 模式下 20 seeds × 4 methods × (2000wu+4000s×4chains) 约 73 min\\n\\n## ConStat 调研 (2026-05-21)\\n\\n### 基本信息\\n- **论文**: \\\"ConStat: Performance-Based Contamination Detection in LLMs\\\", NeurIPS 2024 Poster, ETH Zurich SRI Lab\\n- **Repo**: github.com/eth-sri/ConStat, Apache-2.0, 低活跃 (4 commits)\\n- **核心定义**: Contamination = 不泛化的虚高性能（非单纯训练集包含 benchmark 样本）\\n\\n### 接口\\n`ConStat.test(scores_model, scores_model_ref_data, scores_ref_models, scores_ref_models_ref_data)` → p_value, estimated_contamination, delta, min_delta_095, 置信区间。纯黑盒，不需要 logprobs。\\n\\n### ⚠️ 对 G-MFRM 的关键 gap\\nConStat 输出 **per-model 全局污染检测**，不直接输出 **per-item e_i**。G-MFRM 需要 per-item exposure level。\\n- 可利用 `return_functions_test()` 的 spline 拟合函数推导 per-item observed vs expected 偏差作为 e_i proxy\\n- 最简方案：直接用 item-level performance gap (original vs reference benchmark) 作为 e_i proxy，ConStat spline hardness correction 作为精确校正层\\n\\n### 数据需求\\n1. Reference benchmark（与原始 benchmark 同分布但未泄露的变体）— **最大依赖**\\n2. Reference models（一组已知未污染的模型）的 per-item 评测结果（论文用 ~20 个模型）\\n3. 所有数据为 numpy per-item binary scores\\n\\n### 替代 e_i 估计方案\\n| 方法 | per-item? | 需要 logprobs? |\\n|------|-----------|---------------|\\n| ConStat spline 推导 | 间接可得 | 否 |\\n| Performance gap (orig vs ref) | 是 | 否 |\\n| LogProber | 天然 per-item | 是（无官方 repo） |\\n| Min-K% Prob | 天然 per-item | 是 |\\n\\n## Baseline 代码可用性 (2026-05-21)\\n\\n| Baseline | 代码 | License | 重实现难度 |\\n|----------|------|---------|-----------|\\n| CyclicJudge | 无 repo | — | 低 (~100行) |\\n| UDA | 无（anonymous 403） | — | 中 (2-4天) |\\n| DCR | github.com/chengxuphd/dcr | Apache-2.0 | 适配即可 |\\n| Preference Leakage | github.com/David-Li0406/Preference-Leakage | 无 license, 82% notebooks | 需整理 |\\n\\n### 下一步\\nMVP 通过后应：写 paper_framing.md + experiment_plan.yaml → 进入 research 阶段（真实数据实验）\\n\", \"total_chars\": 2712, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac11eec1-a0da-47b1-bc61-f64935536049",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "37947034-1bbc-4c2a-866e-4a5fbe3aecda",
  "sourceToolAssistantUUID": "ac11eec1-a0da-47b1-bc61-f64935536049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T21:31:18.597Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KgVCYTtRCpxMiksxU3EUzK`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37947034-1bbc-4c2a-866e-4a5fbe3aecda",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRmCC1ryS8NwAJ69qC5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa5e80f8-94d9-4166-86ef-8607e6c798ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmqfqV8YE4vN2Tg5k7PPru",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7964,
      "cache_read_input_tokens": 17813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7964,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 20 · 2026-05-21T21:31:18.607Z_

<details><summary>↩ Tool result · `toolu_01KgVCYTtRCpxMiksxU3EUzK`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'gated_mfrm_judge_bias'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa5e80f8-94d9-4166-86ef-8607e6c798ed",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "9714997c-2eff-4f41-bf01-8b22530ec473",
  "sourceToolAssistantUUID": "aa5e80f8-94d9-4166-86ef-8607e6c798ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T21:31:19.115Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PmtaqLWRU36TDMm9FuJoiW`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9714997c-2eff-4f41-bf01-8b22530ec473",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRmCC1ryS8NwAJ69qC5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "029edef0-081d-47b2-b91a-cb872c271143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmqfqV8YE4vN2Tg5k7PPru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7964,
      "cache_read_input_tokens": 17813,
      "output_tokens": 398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7964
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 398,
          "cache_read_input_tokens": 17813,
          "cache_creation_input_tokens": 7964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7964,
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

_source line 22 · 2026-05-21T21:31:19.125Z_

<details><summary>↩ Tool result · `toolu_01PmtaqLWRU36TDMm9FuJoiW`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'gated_mfrm_judge_bias'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "029edef0-081d-47b2-b91a-cb872c271143",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "0c607d76-de4e-48d2-b0f1-69c8dea907e8",
  "sourceToolAssistantUUID": "029edef0-081d-47b2-b91a-cb872c271143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-21T21:31:23.866Z_

Now let me read the actual paper draft and the experiment plan, plus the distilled research/writing skills for domain context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c607d76-de4e-48d2-b0f1-69c8dea907e8",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRmftu3ZGshGQQvD6bV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d7ef433-fbe9-4769-9a7b-65dc676a5310",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpEPaPsE9SjENCZq4Pkh1v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2479,
      "cache_read_input_tokens": 25777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2479,
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

_source line 24 · 2026-05-21T21:31:25.290Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AuYUAUWeHgy1pB189mEu56`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d7ef433-fbe9-4769-9a7b-65dc676a5310",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRmftu3ZGshGQQvD6bV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf567e02-43f3-49e0-9198-762b0d9a14ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpEPaPsE9SjENCZq4Pkh1v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2479,
      "cache_read_input_tokens": 25777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2479,
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

_source line 25 · 2026-05-21T21:31:25.300Z_

<details><summary>↩ Tool result · `toolu_01AuYUAUWeHgy1pB189mEu56`</summary>

```text
artifacts/dream_reports/dream_20260521T204917/best/paper.tex
artifacts/dream_reports/dream_20260521T204917/median/paper.tex
artifacts/dream_reports/dream_20260521T204917/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf567e02-43f3-49e0-9198-762b0d9a14ff",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "d7ee7f32-b068-40f0-9bbf-3b6e60997acf",
  "sourceToolAssistantUUID": "cf567e02-43f3-49e0-9198-762b0d9a14ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T21:31:25.764Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TdHFtQLBBgn5hK27PZn3Cq`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7ee7f32-b068-40f0-9bbf-3b6e60997acf",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRmftu3ZGshGQQvD6bV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0cb7469-716e-4a57-ba70-f9fc7be475c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpEPaPsE9SjENCZq4Pkh1v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2479,
      "cache_read_input_tokens": 25777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2479,
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

_source line 27 · 2026-05-21T21:31:25.773Z_

<details><summary>↩ Tool result · `toolu_01TdHFtQLBBgn5hK27PZn3Cq`</summary>

```text
artifacts/dream_reports/dream_20260521T204917/best/paper.pdf
artifacts/dream_reports/dream_20260521T204917/median/paper.pdf
artifacts/dream_reports/dream_20260521T204917/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0cb7469-716e-4a57-ba70-f9fc7be475c9",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "8b417dec-cdbc-4641-b95f-9fc099286918",
  "sourceToolAssistantUUID": "b0cb7469-716e-4a57-ba70-f9fc7be475c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T21:31:26.107Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01L92hc3vkHDcSeKQRib2sxh`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b417dec-cdbc-4641-b95f-9fc099286918",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRmftu3ZGshGQQvD6bV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b3d4484-22f5-4346-a2f6-97af56d421e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpEPaPsE9SjENCZq4Pkh1v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2479,
      "cache_read_input_tokens": 25777,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2479
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 280,
          "cache_read_input_tokens": 25777,
          "cache_creation_input_tokens": 2479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2479,
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

_source line 29 · 2026-05-21T21:31:26.116Z_

<details><summary>↩ Tool result · `toolu_01L92hc3vkHDcSeKQRib2sxh`</summary>

```text
literature_map.yaml
distill_tmp/wang2025mfrm_llm.yaml
distill_tmp/fiedler2026bias_uncertainty.yaml
distill_tmp/soumik2026judging_judges.yaml
distill_tmp/logprober2024.yaml
distill_tmp/shu2013dgirt.yaml
distill_tmp/preference_leakage2026.yaml
distill_tmp/cyclicjudge2026.yaml
distill_tmp/lin2025psnirt.yaml
distill_tmp/constat2024.yaml
distill_tmp/dcr2025.yaml
distill_tmp/uda2026.yaml
distill_tmp/zheng2023mtbench.yaml
mistakes.yaml
artifacts/manifest.yaml
registry.yaml
decisions.yaml
artifacts/dream_reports/dream_20260521T204917/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T204917/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T204917/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T204917/best/review_context.yaml
experiment_plan.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260521T204917/median/review_context.yaml
artifacts/dream_reports/dream_20260521T204917/worst/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b3d4484-22f5-4346-a2f6-97af56d421e4",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "0533a46d-326c-4144-8703-dc1c78ef105a",
  "sourceToolAssistantUUID": "6b3d4484-22f5-4346-a2f6-97af56d421e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T21:31:28.517Z_

<details open><summary>🔧 Tool call — Read · `toolu_014oNKLtgiwDRVXqQ3AJEXNp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0533a46d-326c-4144-8703-dc1c78ef105a",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRnBmzSEnB3ahd53edQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec1c8e54-2d0c-4057-a863-a485a4fa0b0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwYg6GmHiTVSQwmSVkanTV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 837,
      "cache_read_input_tokens": 28256,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 837
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 28256,
          "cache_creation_input_tokens": 837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 837,
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

_source line 31 · 2026-05-21T21:31:28.834Z_

<details><summary>↩ Tool result · `toolu_014oNKLtgiwDRVXqQ3AJEXNp`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage[margin=1in]{geometry}
6	\usepackage{amsmath,amssymb,amsthm}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{natbib}
10	\usepackage{hyperref}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{tabularx}
14	
15	\newtheorem{proposition}{Proposition}
16	\newtheorem{definition}{Definition}
17	
18	\title{G-MFRM: Joint Estimation of Judge Bias and Benchmark Contamination\\for Fair LLM Evaluation}
19	
20	\author{Anonymous}
21	\date{}
22	
23	\begin{document}
24	\maketitle
25	
26	%% ============================================================
27	%% ABSTRACT
28	%% ============================================================
29	\begin{abstract}
30	LLM-as-a-judge evaluation faces two well-documented distortions: inter-judge bias (systematic severity differences across judges) and benchmark contamination (inflated scores on memorized items). Existing methods address these independently, but judge severity and contamination susceptibility are confounded: bias-only correction absorbs contamination effects into ability estimates, while contamination-only adjustment misattributes judge variation as contamination signal. We formalize this as an omitted variable bias problem and prove that sequential correction pipelines produce asymptotically biased ability estimates when judge severity and contamination are non-orthogonal. We propose the Gated Many-Facet Rasch Model (G-MFRM), a unified psychometric framework that jointly estimates model ability, item difficulty, judge severity, and per-model contamination susceptibility within a single calibration. G-MFRM uses externally-anchored exposure indicators and a three-stage estimation procedure to ensure identifiability.
31	On MT-Bench and Arena-Hard with 8 Large Language Model (LLM) judges evaluating 22 target models (203,520 evaluations), G-MFRM fair scores achieve Kendall $\tau = 0.86$ and $0.85$ with Chatbot Arena human votes, significantly outperforming the best sequential baseline ($p = 0.008$ and $p = 0.041$). Beyond ranking accuracy, G-MFRM produces interpretable per-model contamination estimates that correlate consistently across benchmarks ($r = 0.68$--$0.71$) and degrade gracefully to standard MFRM when contamination is absent.
32	\end{abstract}
33	
34	%% ============================================================
35	%% 1. INTRODUCTION
36	%% ============================================================
37	\section{Introduction}
38	
39	Automated evaluation with LLM judges has become the dominant paradigm for comparing language models on open-ended generation tasks. Benchmarks such as MT-Bench \citep{zheng2023judging}, Arena-Hard \citep{li2024crowdsourced}, and WildBench \citep{lin2024wildbench} rely on one or more LLM judges to score model outputs, and the resulting rankings drive both research priorities and deployment decisions.
40	
41	Two systematic distortions threaten the validity of these rankings. First, LLM judges exhibit significant inter-judge bias: different judges assign systematically different severity levels, and their agreement is modest (Fleiss' $\kappa \approx 0.41$ in our data). Second, benchmark contamination inflates scores when target models have memorized evaluation items during pre-training, a problem that grows as benchmarks age and training corpora expand.
42	
43	A growing literature addresses each distortion separately. CyclicJudge \citep{cyclicjudge2025} and UDA \citep{uda2025} correct judge bias through round-robin protocols or neural K-factor adjustment. ConStat \citep{constat2024} and DCR \citep{dcr2025} quantify contamination effects via reference variant comparisons. However, no existing work (across 12 surveyed papers through May 2026) jointly models both within a single estimation framework. This separation is not merely incomplete; it is structurally flawed.
44	
45	The core problem is \textit{omitted variable confounding}. When judge severity ($d_j$) and contamination susceptibility ($c_n \cdot e_i$) are both present but only one is modeled, the unmodeled factor is absorbed into other parameter estimates. A bias-only method treats contamination-inflated scores as genuine ability, producing overestimates for contaminated models. A contamination-only method attributes part of the judge-driven variance to contamination, distorting the contamination signal. Sequential pipelines (correct bias first, then contamination, or vice versa) do not resolve this: the first stage's estimates are already biased by the unmodeled facet, and the second stage inherits that bias.
46	
47	We formalize this confounding and prove that under non-orthogonality of $d_j$ and $c_n \cdot e_i$, sequential estimators are asymptotically biased with a predictable direction (Proposition~\ref{prop:bias}). Our Monte Carlo validation confirms that the first-order bias approximation correctly predicts the direction of bias in 97\% of conditions across 540 parameter configurations.
48	
49	We propose the \textbf{Gated Many-Facet Rasch Model (G-MFRM)}, a unified psychometric framework that resolves confounding by jointly estimating all facets. G-MFRM extends the classical Many-Facet Rasch Model (MFRM) with a gating mechanism inspired by DG-IRT \citep{dgirt2024}, incorporating externally-anchored item exposure indicators to model contamination. A three-stage estimation procedure ensures identifiability: (1) standard MFRM for initial parameter estimates, (2) exposure anchoring via ConStat delta scores and temporal signals, (3) joint Bayesian estimation of all parameters including per-model contamination susceptibility $c_n$.
50	
51	Our contributions are:
52	\begin{itemize}
53	    \item We formalize the confounding between judge bias and benchmark contamination as an omitted variable bias problem (Proposition~\ref{prop:bias}) and validate the bias direction empirically (Section~\ref{sec:proposition}).
54	    \item We propose G-MFRM, a joint estimation framework that produces bias-and-contamination-corrected ``fair scores'' along with interpretable per-model contamination estimates (Section~\ref{sec:method}).
55	    \item We evaluate G-MFRM on MT-Bench, Arena-Hard, and WildBench with 8 LLM judges and 22 target models, showing consistent improvements over 7 baselines and graceful degradation when contamination is low (Sections~\ref{sec:main_results}--\ref{sec:wildbench}).
56	\end{itemize}
57	
58	%% ============================================================
59	%% 2. BACKGROUND AND MOTIVATION
60	%% ============================================================
61	\section{Background and Motivation}
62	\label{sec:background}
63	
64	\subsection{Many-Facet Rasch Model}
65	
66	The Many-Facet Rasch Model (MFRM) \citep{linacre1989mfrm} extends item response theory to settings with multiple facets (e.g., examinees, items, raters). In LLM evaluation, we have three facets: model ability $\theta_n$, item difficulty $b_i$, and judge severity $d_j$. The probability of model $n$ receiving a high rating from judge $j$ on item $i$ is:
67	\begin{equation}
68	\label{eq:mfrm}
69	\log \frac{P(X_{nij} \geq k)}{P(X_{nij} < k)} = \theta_n - b_i - d_j - \tau_k
70	\end{equation}
71	where $\tau_k$ are threshold parameters. MFRM produces ``fair scores'' that separate model ability from judge and item effects, but it does not account for contamination.
72	
73	\subsection{Contamination as a Latent Facet}
74	
75	Benchmark contamination occurs when a target model has been exposed to evaluation items during training. Following the DG-IRT framework \citep{dgirt2024}, we model contamination as a multiplicative interaction: a model with contamination susceptibility $c_n$ gains an advantage $c_n \cdot e_i$ on item $i$ with exposure level $e_i$. This rank-1 structure captures the dominant contamination pattern where advantage is proportional to both model memorization tendency and item exposure.
76	
77	\subsection{The Confounding Problem: A Toy Example}
78	\label{sec:toy}
79	
80	Consider two models evaluated by two judges on items with varying exposure levels. Model A has high ability but low contamination ($\theta_A = 2, c_A = 0.1$). Model B has lower ability but high contamination ($\theta_B = 1, c_B = 1.5$). Judge 1 is lenient ($d_1 = -0.5$), Judge 2 is strict ($d_2 = 0.5$).
81	
82	Under a bias-only correction (e.g., standard MFRM), the contamination-inflated scores of Model B are treated as genuine ability. The estimated $\hat{\theta}_B$ absorbs the $c_B \cdot e_i$ term, producing $\hat{\theta}_B > \theta_B$. Conversely, under contamination-only correction, the differing judge severities create phantom contamination signals: if Judge 1 (lenient) happens to evaluate more high-exposure items, the contamination estimator conflates leniency with exposure effects.
83	
84	Sequential correction does not resolve this. If we first correct for judge bias, the resulting ``debiased'' scores still contain contamination inflation, and the subsequent contamination correction inherits these inflated baselines.
85	
86	\subsection{Formal Proposition}
87	\label{sec:proposition}
88	
89	\begin{proposition}
90	\label{prop:bias}
91	Let $\hat{\theta}^{seq}_n$ denote the sequential estimator of model ability (bias correction followed by contamination correction) and $\hat{\theta}^{joint}_n$ the joint estimator. Under non-orthogonality of $d_j$ and $c_n \cdot e_i$ (i.e., $\text{Cov}(d_j, c_n \cdot e_i) \neq 0$), the first-order asymptotic bias of the sequential estimator is:
92	\[
93	\text{Bias}(\hat{\theta}^{seq}_n) \approx \frac{\text{Cov}(d_j, c_n \cdot e_i)}{\text{Var}(d_j)} \cdot d_j + O(n^{-1})
94	\]
95	The direction of bias is determined by the sign of $\text{Cov}(d_j, c_n \cdot e_i)$, and the joint estimator is asymptotically unbiased under standard regularity conditions.
96	\end{proposition}
97	
98	We validate Proposition~\ref{prop:bias} via Monte Carlo simulation across 540 parameter configurations (varying correlation $\rho$ between $d_j$ and $c_n \cdot e_i$, contamination magnitude, and sample size) with 200 replications each.
99	
100	\begin{table}[t]
101	\centering
102	\caption{Monte Carlo validation of the first-order bias approximation. The proposition correctly predicts bias direction in 97\% of conditions. Bias magnitude increases with confounding correlation $\rho$.}
103	\label{tab:proposition}
104	\begin{tabular}{lcccc}
105	\toprule
106	$\rho(d_j, c \cdot e)$ & Bias (median) & Bias 95\% CI & Direction correct (\%) & Approx.\ corr. \\
107	\midrule
108	0.1 & 0.018 & [0.005, 0.038] & 97 & 0.91 \\
109	0.2 & 0.041 & [0.012, 0.079] & 97 & 0.91 \\
110	0.3 & 0.072 & [0.021, 0.134] & 97 & 0.91 \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	Table~\ref{tab:proposition} confirms that (1) the bias direction is correctly predicted in 97\% of conditions, (2) the first-order approximation correlates at $r = 0.91$ with the true bias, and (3) bias magnitude increases monotonically with $\rho$. The proposition holds across 89\% of the realistic parameter range; the 11\% of cases where regularity conditions are violated correspond to near-zero contamination ($c < 0.1$), where the bias itself is negligible.
116	
117	%% ============================================================
118	%% 3. METHOD
119	%% ============================================================
120	\section{The Gated Many-Facet Rasch Model}
121	\label{sec:method}
122	
123	\subsection{Model Formulation}
124	
125	G-MFRM extends the standard MFRM (Eq.~\ref{eq:mfrm}) with a contamination gating term:
126	\begin{equation}
127	\label{eq:gmfrm}
128	\log \frac{P(X_{nij} \geq k)}{P(X_{nij} < k)} = \theta_n + c_n \cdot e_i - b_i - d_j - \tau_k
129	\end{equation}
130	where $c_n \geq 0$ is the contamination susceptibility of model $n$ and $e_i \in [0, 1]$ is the exposure indicator for item $i$. The key design choices are:
131	
132	\textbf{Rank-1 contamination structure.} The interaction $c_n \cdot e_i$ assumes that contamination advantage is separable into a model factor and an item factor. This follows the LLTM tradition and provides a parsimonious first approximation. Person-fit diagnostics (Section~\ref{sec:fit}) can detect violations of this assumption.
133	
134	\textbf{External exposure anchoring.} Unlike educational testing (where exposure status is known to the administrator), benchmark contamination exposure is unknown. We estimate $e_i$ externally via a composite of ConStat delta scores, temporal signals, and memorization indicators (Section~\ref{sec:exposure}), then treat $e_i$ as fixed in Stage 3.
135	
136	\textbf{Non-negative $c_n$.} Contamination can only inflate scores (or have no effect), never deflate them. We enforce $c_n \geq 0$ via a half-normal prior.
137	
138	\subsection{Three-Stage Estimation}
139	
140	\textbf{Stage 1: Standard MFRM.} We fit the standard MFRM without contamination terms to obtain initial estimates $(\hat{\theta}_n^{(0)}, \hat{b}_i^{(0)}, \hat{d}_j^{(0)})$. These serve as informative priors for Stage 3.
141	
142	\textbf{Stage 2: Exposure Estimation.} We construct composite exposure indicators $e_i$ for each item by combining three signals: (a) ConStat delta scores (comparing model performance on original items vs.\ semantically equivalent rephrased variants), (b) temporal signals (benchmark publication date relative to model training cutoff), and (c) LogProber Safe Scores (memorization indicators from probing model internals). The composite reliability is $\alpha = 0.71$ (Section~\ref{sec:exposure}).
143	
144	\textbf{Stage 3: Joint Bayesian Estimation.} We fit the full G-MFRM (Eq.~\ref{eq:gmfrm}) using NumPyro MCMC with non-centered parameterization: 2,000 warmup steps, 4,000 posterior samples, and 4 chains. Stage 1 estimates provide informative priors. The exposure indicators $e_i$ from Stage 2 are treated as fixed, and $c_n$ is estimated as a latent parameter for each target model.
145	
146	\subsection{Graceful Degradation}
147	
148	When contamination is absent ($e_i \approx 0$ for all items or $c_n \approx 0$ for all models), the gating term vanishes and G-MFRM reduces to the standard MFRM. This means G-MFRM incurs no performance penalty on clean benchmarks, eliminating the risk of over-correction.
149	
150	%% ============================================================
151	%% 4. EXPERIMENTAL SETUP
152	%% ============================================================
153	\section{Experimental Setup}
154	\label{sec:setup}
155	
156	\subsection{Data Collection}
157	
158	We evaluate 22 target models using 8 LLM judges spanning 4 model families: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick, and Gemini 2.5 Pro. Each judge evaluates all target models on MT-Bench (80 items) and Arena-Hard (500 items) with position swapping, yielding a total of 203,520 evaluations.
159	
160	\begin{table}[t]
161	\centering
162	\caption{Data collection summary. Position swapping controls for position bias (average rate 12\%). Completion rate exceeds 97\% across all judges.}
163	\label{tab:data}
164	\begin{tabular}{lccccc}
165	\toprule
166	Statistic & Value \\
167	\midrule
168	Judges & 8 (5 open-source, 3 API) \\
169	Target models & 22 \\
170	Items (MT-Bench / Arena-Hard) & 80 / 500 \\
171	Total evaluations & 203,520 \\
172	Avg.\ position bias rate & 12\% \\
173	Inter-judge agreement (Fleiss' $\kappa$) & 0.41 \\
174	Judge completion rate & $\geq$97\% \\
175	Missing data & 2.8\% (MCAR) \\
176	\bottomrule
177	\end{tabular}
178	\end{table}
179	
180	The inter-judge agreement of $\kappa = 0.41$ (Table~\ref{tab:data}) reflects the typical level of LLM judge consistency, above chance but far from perfect. This moderate agreement is precisely the condition under which MFRM-based severity modeling provides value: if judges agreed perfectly, there would be no severity to separate.
181	
182	\subsection{Exposure Indicator Construction}
183	\label{sec:exposure}
184	
185	For each benchmark item, we generate rephrased reference variants and compute ConStat delta scores as the primary exposure signal. We combine these with temporal signals (benchmark release date vs.\ model training cutoff) and LogProber Safe Scores into a composite indicator $e_i$.
186	
187	\begin{table}[t]
188	\centering
189	\caption{Exposure indicator statistics by benchmark. MT-Bench, as an older benchmark, shows higher exposure rates. The composite $e_i$ achieves acceptable reliability ($\alpha = 0.71$).}
190	\label{tab:exposure}
191	\begin{tabular}{lccccc}
192	\toprule
193	Benchmark & $n$ items & Mean $e_i$ & Std $e_i$ & High exposure (\%) & Reliability $\alpha$ \\
194	\midrule
195	MT-Bench & 80 & 0.15 & 0.22 & 35 & 0.71 \\
196	Arena-Hard & 500 & 0.15 & 0.22 & 18 & 0.71 \\
197	\bottomrule
198	\end{tabular}
199	\end{table}
200	
201	MT-Bench has substantially higher exposure (35\% of items classified as high-exposure) compared to Arena-Hard (18\%), consistent with MT-Bench being older and more widely incorporated into training data. The rephrased reference variants pass a human equivalence check ($p = 0.23$), confirming that performance differences between original and rephrased items reflect memorization rather than semantic divergence. The ConStat delta scores correlate at $r = 0.74$ (rank correlation) with ground-truth exposure levels, and the temporal signal adds moderate complementary information ($r = 0.48$ with ConStat).
202	
203	\subsection{Baselines}
204	
205	We compare G-MFRM against 7 baselines:
206	\begin{itemize}
207	\item \textbf{Raw Average}: simple multi-judge average without correction.
208	\item \textbf{MFRM-only}: standard MFRM without contamination modeling.
209	\item \textbf{Sequential (bias-first)}: MFRM for bias correction, then post-hoc contamination adjustment.
210	\item \textbf{Sequential (contam-first)}: contamination adjustment first, then MFRM.
211	\item \textbf{CyclicJudge} \citep{cyclicjudge2025}: round-robin protocol eliminating average judge bias.
212	\item \textbf{DCR} \citep{dcr2025}: contamination-aware scoring via data characterization.
213	\item \textbf{UDA} \citep{uda2025}: neural K-factor adjustment for judge bias.
214	\item \textbf{Preference Leakage} \citep{prefleak2025}: leakage-aware evaluation protocol.
215	\end{itemize}
216	
217	All methods are evaluated by Kendall $\tau$ and Spearman $\rho$ correlation with Chatbot Arena human votes, with bootstrap 95\% confidence intervals.
218	
219	%% ============================================================
220	%% 5. RESULTS
221	%% ============================================================
222	\section{Results}
223	
224	\subsection{G-MFRM Model Fit}
225	\label{sec:fit}
226	
227	\begin{table}[t]
228	\centering
229	\caption{G-MFRM convergence diagnostics. The model achieves acceptable convergence: 92\% of parameters have $\hat{R} < 1.05$.}
230	\label{tab:convergence}
231	\begin{tabular}{lccc}
232	\toprule
233	Metric & Value & Threshold & Status \\
234	\midrule
235	Max $\hat{R}$ & 1.06 & $<$1.10 & Pass \\
236	\% params $\hat{R} > 1.05$ & 8\% & $<$10\% & Pass \\
237	Min ESS & 120 & $>$100 & Pass \\
238	Divergent transitions & 12 (0.075\%) & $<$1\% & Pass \\
239	Runtime & 3.2 hours & -- & -- \\
240	\bottomrule
241	\end{tabular}
242	\end{table}
243	
244	Table~\ref{tab:convergence} shows that G-MFRM converges adequately on real data. The 8\% of parameters with $\hat{R} > 1.05$ are concentrated among high-$c_n$ models where the contamination signal is noisier. We report 12 divergent transitions (0.075\% of total), within the acceptable range for complex hierarchical models.
245	
246	\begin{table}[t]
247	\centering
248	\caption{Facet fit statistics (infit/outfit mean-square). Judge severity shows the best fit; contamination shows the highest misfit rate, reflecting the rank-1 approximation's limitations.}
249	\label{tab:facet_fit}
250	\begin{tabular}{lcccccc}
251	\toprule
252	Facet & $n$ & Infit $\bar{x}$ & Outfit $\bar{x}$ & Misfit (\%) \\
253	\midrule
254	Model ability ($\theta_n$) & 22 & 1.02 & 1.08 & 9 \\
255	Item difficulty ($b_i$) & 580 & 0.99 & 1.05 & 7 \\
256	Judge severity ($d_j$) & 8 & 1.01 & 1.03 & 0 \\
257	Contamination ($c_n$) & 22 & 1.06 & 1.15 & 18 \\
258	\bottomrule
259	\end{tabular}
260	\end{table}
261	
262	Table~\ref{tab:facet_fit} reports fit statistics across all facets. Judge severity parameters show excellent fit (0\% misfit), as expected given relatively stable judge behavior. Contamination parameters show the highest misfit rate (18\%), with outfit mean-square of 1.15. This reflects cases where the rank-1 assumption ($c_n \cdot e_i$) does not fully capture the contamination pattern for individual models. We interpret $c_n$ as a contamination \textit{tendency} rather than a precise quantity and note rank-$k$ extensions as future work. The correlation between Stage 1 person-fit statistics ($l_z$) and Stage 3 contamination estimates is $r = 0.52$, providing moderate construct validity: models that exhibit poor fit under the standard MFRM tend to have higher estimated contamination.
263	
264	\subsection{Main Results}
265	\label{sec:main_results}
266	
267	\begin{table*}[t]
268	\centering
269	\caption{Method comparison across benchmarks. G-MFRM achieves the highest correlation with Chatbot Arena human votes on both MT-Bench and Arena-Hard. $\dagger$: significant at $p < 0.05$ vs.\ G-MFRM (Wilcoxon signed-rank test). Best in \textbf{bold}, second best \underline{underlined}.}
270	\label{tab:main}
271	\begin{tabular}{lcccccc}
272	\toprule
273	\multirow{2}{*}{Method} & \multicolumn{2}{c}{MT-Bench} & \multicolumn{2}{c}{Arena-Hard} & \multicolumn{2}{c}{Average} \\
274	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
275	& $\tau$ & $\rho$ & $\tau$ & $\rho$ & $\tau$ & $\rho$ \\
276	\midrule
277	Raw Average & 0.78$^\dagger$ & 0.82 & 0.76$^\dagger$ & 0.80 & 0.77 & 0.81 \\
278	MFRM-only & 0.83$^\dagger$ & 0.86 & 0.82$^\dagger$ & 0.85 & 0.83 & 0.86 \\
279	Seq.\ (bias-first) & \underline{0.84}$^\dagger$ & \underline{0.87} & \underline{0.83}$^\dagger$ & \underline{0.86} & \underline{0.84} & \underline{0.87} \\
280	Seq.\ (contam-first) & 0.83$^\dagger$ & 0.86 & 0.82$^\dagger$ & 0.85 & 0.83 & 0.86 \\
281	CyclicJudge & 0.82$^\dagger$ & 0.85 & 0.81$^\dagger$ & 0.84 & 0.82 & 0.85 \\
282	DCR & 0.81$^\dagger$ & 0.84 & 0.80$^\dagger$ & 0.83 & 0.81 & 0.84 \\
283	UDA & \underline{0.84}$^\dagger$ & \underline{0.87} & \underline{0.83}$^\dagger$ & \underline{0.86} & \underline{0.84} & \underline{0.87} \\
284	Pref.\ Leakage & 0.80$^\dagger$ & 0.83 & 0.79$^\dagger$ & 0.82 & 0.80 & 0.83 \\
285	\midrule
286	\textbf{G-MFRM} & \textbf{0.86} & \textbf{0.89} & \textbf{0.85} & \textbf{0.88} & \textbf{0.86} & \textbf{0.89} \\
287	\bottomrule
288	\end{tabular}
289	\end{table*}
290	
291	Table~\ref{tab:main} presents the main results. G-MFRM achieves the highest Kendall $\tau$ on both benchmarks: 0.86 on MT-Bench ($p = 0.008$ vs.\ best baseline) and 0.85 on Arena-Hard ($p = 0.041$). The improvement over the best sequential baseline is $\Delta\tau = 0.02$ on both benchmarks.
292	
293	Several patterns are informative. First, all correction methods outperform Raw Average, confirming that both bias and contamination distort rankings. Second, MFRM-only already provides substantial gains over Raw Average ($+0.05$/$+0.06$ in $\tau$), demonstrating the value of judge severity modeling. Third, methods that address only one distortion (CyclicJudge for bias, DCR for contamination) underperform sequential approaches that attempt both, consistent with our confounding analysis. Fourth, UDA matches the sequential (bias-first) baseline despite being a black-box method, but neither provides contamination estimates.
294	
295	The $\Delta\tau = 0.02$ improvement may appear modest in isolation. We emphasize two points. First, Proposition~\ref{prop:bias} establishes that the sequential estimator is \textit{asymptotically biased} regardless of the magnitude of the bias in any finite sample. Joint estimation is the methodologically correct approach. Second, G-MFRM's per-model contamination estimates (Section~\ref{sec:calibration}) constitute an independent contribution with practical value for benchmark auditing, a capability that no baseline provides.
296	
297	\subsection{Contamination Magnitude Calibration}
298	\label{sec:calibration}
299	
300	\begin{table}[t]
301	\centering
302	\caption{Contamination magnitude: real data vs.\ synthetic scenarios. Real contamination falls between the two synthetic settings, closer to the mild scenario (MVP-001).}
303	\label{tab:contamination}
304	\begin{tabular}{lccccc}
305	\toprule
306	Scenario & $\bar{c}$ & Std & \% $c > 1$ & G-MFRM $\tau$ & Seq.\ $\tau$ \\
307	\midrule
308	MVP-001 (mild) & $\sim$0.5 & -- & -- & -- & -- \\
309	Real data & 0.62 & 0.35 & 18 & 0.86 & 0.84 \\
310	MVP-003 (strong) & $\sim$1.5 & -- & -- & -- & -- \\
311	\bottomrule
312	\end{tabular}
313	\end{table}
314	
315	The estimated per-model contamination susceptibility $c_n$ has mean 0.62 (median 0.51, std 0.35), with values ranging from 0.08 to 1.41 across the 22 target models (Table~\ref{tab:contamination}). The distribution is right-skewed: 23\% of models show negligible contamination ($c_n < 0.2$) while 18\% show strong contamination ($c_n > 1.0$). This heterogeneity is the critical finding: average contamination appears moderate, but a substantial tail of heavily contaminated models exists.
316	
317	The distribution is statistically indistinguishable from the mild synthetic scenario MVP-001 ($p = 0.12$, KS test) but significantly different from the strong scenario MVP-003 ($p = 0.003$). This confirms that real-world contamination is less extreme than worst-case assumptions but too prevalent to ignore.
318	
319	Two model-level correlates emerge. Training recency correlates negatively with $c_n$ ($r = -0.43$): newer models tend to have lower contamination, likely because benchmark decontamination has become standard practice. Model size correlates weakly positively with $c_n$ ($r = 0.28$), consistent with larger models having greater memorization capacity.
320	
321	\subsection{Cross-Benchmark Generalization: WildBench}
322	\label{sec:wildbench}
323	
324	To test generalization, we replicate the full G-MFRM pipeline on WildBench (1,024 items) using the same 8 judges.
325	
326	\begin{table}[t]
327	\centering
328	\caption{WildBench replication. With only 12\% high-exposure items, G-MFRM's advantage is small and non-significant, demonstrating graceful degradation.}
329	\label{tab:wildbench}
330	\begin{tabular}{lccc}
331	\toprule
332	Method & WildBench $\tau$ & $\Delta\tau$ & $p$ \\
333	\midrule
334	Sequential & 0.83 & -- & -- \\
335	G-MFRM & 0.84 & +0.01 & 0.062 \\
336	\bottomrule
337	\end{tabular}
338	\end{table}
339	
340	On WildBench, G-MFRM achieves $\tau = 0.84$ compared to the sequential baseline's 0.83 (Table~\ref{tab:wildbench}). The difference ($\Delta\tau = 0.01$) is not statistically significant ($p = 0.062$). This is expected: WildBench has only 12\% high-exposure items, providing minimal signal for contamination correction. The result confirms G-MFRM's graceful degradation property: on clean benchmarks, it performs no worse than the sequential approach, adding no over-correction penalty.
341	
342	The per-model $c_n$ estimates from WildBench correlate at $r = 0.71$ with MT-Bench estimates and $r = 0.68$ with Arena-Hard estimates. This cross-benchmark consistency provides construct validity evidence: $c_n$ captures a genuine model-level property (memorization tendency) rather than benchmark-specific artifacts. Convergence on WildBench is slightly weaker ($\hat{R}_{max} = 1.07$, ESS$_{min} = 95$), reflecting the longer and more complex items that increase judge scoring variance.
343	
344	\subsection{Judge Count Sensitivity}
345	\label{sec:judge_sensitivity}
346	
347	\begin{table}[t]
348	\centering
349	\caption{Sensitivity to the number of judges. G-MFRM requires at least 4 judges to significantly outperform the sequential baseline. Performance saturates at 6 judges.}
350	\label{tab:judge_count}
351	\begin{tabular}{lcccc}
352	\toprule
353	$n$ judges & G-MFRM $\tau$ & Seq.\ $\tau$ & $\Delta\tau$ & Conv.\ rate (\%) \\
354	\midrule
355	2 & 0.80 & 0.80 & 0.00 & 65 \\
356	4 & 0.84 & 0.82 & 0.02 & 85 \\
357	6 & 0.85 & 0.83 & 0.02 & 95 \\
358	8 & 0.86 & 0.84 & 0.02 & 100 \\
359	\bottomrule
360	\end{tabular}
361	\end{table}
362	
363	Table~\ref{tab:judge_count} reports results from subsampling 2, 4, 6, and 8 judges (20 random subsets per configuration). With only 2 judges, G-MFRM cannot separate $d_j$ from $c_n \cdot e_i$, and it degrades to MFRM-equivalent performance. The convergence rate of 65\% at 2 judges reflects fundamental identifiability limitations. Four judges represent the minimum for G-MFRM to show a significant advantage, with performance saturating around 6 judges. This provides a practical guideline: the contamination correction benefit requires moderate multi-judge setups, but 8 judges are sufficient (no need for more).
364	
365	\subsection{Exposure Indicator Ablation}
366	\label{sec:ablation}
367	
368	\begin{table}[t]
369	\centering
370	\caption{Ablation of exposure indicator components. ConStat is the dominant signal (58\% relative importance). Removing it causes the largest $\tau$ drop and severely disrupts $c_n$ ranking.}
371	\label{tab:ablation}
372	\begin{tabular}{lcccc}
373	\toprule
374	Configuration & G-MFRM $\tau$ & $\Delta\tau$ & $c_n$ rank corr. & Rel.\ import. \\
375	\midrule
376	Full composite & \textbf{0.86} & -- & 1.00 & -- \\
377	$-$ ConStat & 0.83 & $-$0.03 & 0.61 & 0.58 \\
378	$-$ Temporal & 0.85 & $-$0.01 & 0.89 & 0.22 \\
379	$-$ LogProber & 0.85 & $-$0.01 & 0.91 & 0.20 \\
380	ConStat only & 0.85 & $-$0.01 & 0.82 & -- \\
381	\bottomrule
382	\end{tabular}
383	\end{table}
384	
385	Table~\ref{tab:ablation} presents leave-one-out ablation results for the composite exposure indicator. ConStat dominates with 58\% relative importance: removing it drops $\tau$ by 0.03 and reduces $c_n$ rank correlation to 0.61. Temporal signals and LogProber each contribute approximately 20\%. ConStat alone achieves $\tau = 0.85$, nearly matching the full composite ($\tau = 0.86$), suggesting it can serve as a practical minimum when other signals are unavailable.
386	
387	The low marginal contribution of temporal signals is somewhat surprising. Training cutoff dates provide only coarse-grained information (quarterly resolution at best), while contamination is an item-level phenomenon. LogProber complements ConStat by distinguishing memorization from generalization, but its contribution is limited in the median contamination regime.
388	
389	\subsection{Adversarial Robustness}
390	\label{sec:adversarial}
391	
392	\begin{table}[t]
393	\centering
394	\caption{Adversarial robustness by attack type. G-MFRM maintains an advantage over sequential under adversarial contamination, though paraphrase attacks are difficult to detect.}
395	\label{tab:adversarial}
396	\begin{tabular}{lcccc}
397	\toprule
398	Attack type & Detection & G-MFRM $\tau$ & Seq.\ $\tau$ & FPR \\
399	\midrule
400	Direct memorization & 0.88 & 0.85 & 0.80 & 0.08 \\
401	Partial memorization & 0.62 & 0.82 & 0.78 & 0.12 \\
402	Paraphrase & 0.45 & 0.79 & 0.76 & 0.16 \\
403	\midrule
404	Overall & 0.68 & 0.82 & 0.78 & 0.12 \\
405	\bottomrule
406	\end{tabular}
407	\end{table}
408	
409	Following the adversarial evaluation protocol of \citet{wang2026adversarial}, we test G-MFRM under three types of constructed contamination (Table~\ref{tab:adversarial}). Direct memorization is detected at 88\%, but paraphrase attacks (where items are memorized in rewritten form) are detected at only 45\%. This is a fundamental limitation: ConStat's reference variant method itself relies on paraphrasing, creating overlap with the attack mechanism.
410	
411	Under adversarial conditions, G-MFRM's advantage over sequential actually increases ($\Delta\tau = 0.04$ vs.\ 0.02 under clean conditions). Adversarial contamination amplifies the confounding between $d_j$ and $c_n \cdot e_i$, making the sequential estimator's bias more pronounced and joint estimation relatively more valuable. The false positive rate of 12\% indicates that approximately 12\% of clean models are incorrectly flagged as contaminated, an acceptable but non-trivial error rate. RMSE degrades by 15\% relative to clean conditions.
412	
413	%% ============================================================
414	%% 6. RELATED WORK
415	%% ============================================================
416	\section{Related Work}
417	
418	\paragraph{LLM Judge Bias.}
419	\citet{zheng2023judging} first documented systematic biases in LLM judges, including position bias, verbosity bias, and self-enhancement. CyclicJudge \citep{cyclicjudge2025} addresses bias via round-robin evaluation, eliminating average bias but not capturing item-specific effects. UDA \citep{uda2025} uses neural K-factor adjustment and achieves substantial bias reduction, but operates as a black box without interpretable parameters. Our work differs by treating judge severity as a facet within a psychometric model, jointly estimated with contamination.
420	
421	\paragraph{Benchmark Contamination.}
422	ConStat \citep{constat2024} introduced reference variant comparison for detecting contamination, achieving $r^2 = 0.94$ with true effects. DCR \citep{dcr2025} factors out contamination via data characterization. Preference Leakage \citep{prefleak2025} formalizes contamination as a form of data leakage in preference-based evaluation. These methods quantify contamination but do not account for judge variation. G-MFRM incorporates ConStat as an exposure signal within a joint framework.
423	
424	\paragraph{Psychometric Models for NLP Evaluation.}
425	Item response theory (IRT) has been applied to NLP benchmarks for calibrated difficulty estimation \citep{irt_nlp2020}. MFRM specifically models rater effects in human evaluation \citep{linacre1989mfrm}. DG-IRT \citep{dgirt2024} introduced gating mechanisms for differential item functioning in educational testing. G-MFRM adapts DG-IRT to the LLM evaluation setting with three structural changes: binary-to-continuous exposure, single-rater-to-multi-facet, and known-to-unknown exposure status.
426	
427	%% ============================================================
428	%% 7. CONCLUSION
429	%% ============================================================
430	\section{Conclusion}
431	
432	We have identified a structural flaw in the dominant approach to LLM evaluation calibration: sequential correction of judge bias and benchmark contamination produces biased estimates due to omitted variable confounding. G-MFRM resolves this by jointly estimating model ability, item difficulty, judge severity, and contamination susceptibility within a single psychometric framework.
433	
434	The empirical gains, while consistent, are moderate ($\Delta\tau = 0.02$ on MT-Bench and Arena-Hard). We argue that the methodological contribution extends beyond these numbers. First, Proposition~\ref{prop:bias} establishes that joint estimation is asymptotically correct regardless of the empirical effect size. Second, per-model contamination estimates provide a new tool for benchmark auditing, with cross-benchmark consistency ($r = 0.68$--$0.71$) validating their meaningfulness. Third, G-MFRM degrades gracefully to standard MFRM when contamination is absent, eliminating the downside risk of adoption.
435	
436	\paragraph{Limitations.}
437	Three limitations deserve attention. First, the rank-1 contamination structure ($c_n \cdot e_i$) does not capture heterogeneous contamination patterns (18\% misfit rate for $c_n$). Rank-$k$ extensions could address this at the cost of additional parameters. Second, exposure estimation depends heavily on ConStat (58\% relative importance), and paraphrase-based attacks reduce detection to 45\%. Improving exposure indicators for adversarial settings is an open problem. Third, G-MFRM requires at least 4 judges for identifiability, limiting applicability in single-judge evaluation setups.
438	
439	\bibliography{references}
440	\bibliographystyle{plainnat}
441	
442	\end{document}
443	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec1c8e54-2d0c-4057-a863-a485a4fa0b0f",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "6e81d2d5-123f-472b-8dc0-fb1636f67d55",
  "sourceToolAssistantUUID": "ec1c8e54-2d0c-4057-a863-a485a4fa0b0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-21T21:31:32.607Z_

Now let me read the other dream paper versions and the distilled research skill for comprehensive context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e81d2d5-123f-472b-8dc0-fb1636f67d55",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRnPFJfcjcmJuiagqTG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b1b038e-4c5b-457d-a36d-9593b0ebdc04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZbj3W9zJWiDfLZxa9HKNn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 29093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11820,
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

_source line 33 · 2026-05-21T21:31:34.547Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QWQeGYx8mvrhES6F8Mrf3e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b1b038e-4c5b-457d-a36d-9593b0ebdc04",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRnPFJfcjcmJuiagqTG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a91d5a6-a990-433a-9b8e-bc9deba3a35b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZbj3W9zJWiDfLZxa9HKNn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 29093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11820,
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

_source line 34 · 2026-05-21T21:31:34.854Z_

<details><summary>↩ Tool result · `toolu_01QWQeGYx8mvrhES6F8Mrf3e`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb,amsthm}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{hyperref}
11	\usepackage[margin=1in]{geometry}
12	\usepackage{natbib}
13	\usepackage{enumitem}
14	\usepackage{pifont}
15	
16	\newcommand{\cmark}{\ding{51}}
17	\newcommand{\xmark}{\ding{55}}
18	\newtheorem{proposition}{Proposition}
19	
20	\title{Joint Calibration of Judge Bias and Benchmark Contamination\\in LLM-as-a-Judge Evaluation}
21	
22	\author{Anonymous}
23	\date{}
24	
25	\begin{document}
26	\maketitle
27	
28	% ============================================================
29	% ABSTRACT
30	% ============================================================
31	\begin{abstract}
32	LLM-as-a-judge evaluation suffers from two well-documented distortions: inter-judge severity bias and benchmark contamination of target models. Existing methods address these independently---bias correction methods ignore contamination, and contamination adjustment methods ignore judge variation---or apply them sequentially. We show that sequential correction is fundamentally flawed: when judge severity ($d_j$) and contamination susceptibility ($c_n \cdot e_i$) are non-orthogonal, any single-facet estimator absorbs the unmodeled facet into its estimates, producing systematically biased model rankings. We formalize this as a first-order bias result (Proposition~1) and validate it on real data where ignoring confounding degrades ability RMSE by 28.5\%.
33	
34	We propose the \textbf{Gated Many-Facet Rasch Model (G-MFRM)}, a psychometric framework that jointly estimates model ability ($\theta_n$), item difficulty ($b_i$), judge severity ($d_j$), and contamination susceptibility ($c_n$) in a single Bayesian calibration. G-MFRM adapts the gating mechanism from Differential Group-IRT to the multi-facet, continuous-exposure setting, using externally-anchored exposure indicators from ConStat and temporal signals. On MT-Bench and Arena-Hard with 8 LLM judges evaluating 22 target models, G-MFRM fair scores achieve Kendall-$\tau = 0.91$ with Chatbot Arena human votes, significantly outperforming the best baseline (UDA, $\tau = 0.86$; $p < 0.001$) and all six other methods. The advantage holds on WildBench ($\tau = 0.89$), requires as few as 4 judges for significance, and provides interpretable per-model contamination estimates (AUC = 0.94 for detecting adversarially contaminated models).
35	\end{abstract}
36	
37	% ============================================================
38	% 1. INTRODUCTION
39	% ============================================================
40	\section{Introduction}
41	
42	LLM-as-a-judge evaluation has become the dominant paradigm for scalable model assessment \citep{zheng2023judging}, but it introduces two systematic distortions. First, different LLM judges exhibit varying severity: a lenient judge inflates scores while a strict one deflates them. Second, benchmark contamination causes target models that have been exposed to evaluation items during training to receive artificially inflated scores on those items. Both effects corrupt model ability estimates and can alter leaderboard rankings.
43	
44	The research community has attacked these problems in separate silos. Judge bias correction methods---CyclicJudge \citep{lin2025cyclicjudge}, UDA \citep{li2024uda}---model inter-judge variation but ignore contamination. Contamination detection methods---DCR \citep{yang2024dcr}, Preference Leakage \citep{li2024preference}---quantify contamination effects but ignore judge variation. The implicit assumption is that these distortions are separable: correct one, then correct the other.
45	
46	This assumption is wrong. We demonstrate that when judge severity and contamination susceptibility coexist and are correlated---as they are in practice ($|\rho| = 0.37$ in our data)---sequential correction produces biased estimates regardless of ordering. The mechanism is omitted variable confounding: the first correction stage's parameter estimates absorb the unmodeled facet's effects, and these biased estimates propagate to the second stage. In our experiments, ignoring this confounding degrades model ability RMSE by 28.5\% and causes sequential pipelines to systematically overestimate high-contamination models (bias scatter $r = 0.61$).
47	
48	We propose the \textbf{Gated Many-Facet Rasch Model (G-MFRM)}, a joint calibration framework that resolves this confounding by estimating all facets simultaneously. G-MFRM combines the multi-facet structure of the Many-Facet Rasch Model (MFRM) \citep{linacre1989mfrm} with the gating mechanism from Differential Group Item Response Theory (DG-IRT) \citep{robitzsch2020dgirt}, adapted to the LLM evaluation setting through three non-trivial modifications: (1)~binary group membership is replaced with continuous exposure indicators, (2)~single-rater design is extended to multi-facet calibration, and (3)~unknown exposure status is resolved through external anchoring.
49	
50	Our contributions:
51	\begin{enumerate}[nosep]
52	    \item A formal analysis showing sequential correction of judge bias and contamination is asymptotically biased under non-orthogonality (Proposition~1), validated by Monte Carlo simulation ($R^2 = 0.94$) and real data.
53	    \item G-MFRM: the first framework that jointly estimates model ability, item difficulty, judge severity, and contamination susceptibility in a single Bayesian calibration.
54	    \item Comprehensive evaluation on MT-Bench, Arena-Hard, and WildBench with 8 judges and 22 target models, achieving $\tau = 0.91$ with human rankings (vs.\ $\tau = 0.86$ for the best baseline), with ablations, sensitivity analyses, and adversarial robustness tests.
55	\end{enumerate}
56	
57	% ============================================================
58	% 2. WHY SEQUENTIAL CORRECTION FAILS
59	% ============================================================
60	\section{Why Sequential Correction Fails}
61	
62	Before presenting our model, we establish why joint estimation is methodologically necessary rather than merely convenient. We first formalize the confounding mechanism, then illustrate it with real data.
63	
64	\subsection{Problem Setup}
65	
66	Consider $N$ target models evaluated by $J$ LLM judges on $I$ benchmark items. The observed score $X_{nij}$ for model $n$ on item $i$ by judge $j$ depends on:
67	\begin{itemize}[nosep]
68	    \item $\theta_n$: model $n$'s true ability,
69	    \item $b_i$: item $i$'s difficulty,
70	    \item $d_j$: judge $j$'s severity (higher = stricter),
71	    \item $c_n$: model $n$'s contamination susceptibility,
72	    \item $e_i$: item $i$'s exposure level.
73	\end{itemize}
74	
75	A \emph{sequential} pipeline either (a)~corrects for judge severity first, then adjusts for contamination on the severity-corrected scores, or (b)~adjusts for contamination first, then corrects for severity. We show both orderings produce biased $\hat{\theta}_n$ when $d_j$ and $c_n \cdot e_i$ are non-orthogonal.
76	
77	\subsection{Formal Result}
78	
79	\begin{proposition}[Sequential Estimation Bias]
80	Under non-orthogonality $\mathrm{Cov}(d_j, c_n \cdot e_i) \neq 0$, the bias-first sequential estimator $\hat{\theta}_{\mathrm{seq}}$ has first-order bias:
81	\[
82	\mathbb{E}[\hat{\theta}_{\mathrm{seq}} - \theta_n] \approx \gamma \cdot \frac{\mathrm{Cov}(d_j,\; c_n \cdot e_i)}{\mathrm{Var}(d_j)}
83	\]
84	where $\gamma$ is the contamination gating coefficient. When the covariance is positive (strict judges assign more extreme scores to high-contamination models on high-exposure items), sequential estimation overestimates high-contamination models.
85	\end{proposition}
86	
87	\noindent This follows from standard omitted variable bias analysis adapted to the psychometric setting. The key insight is structural: the bias does not vanish with more data---it is a property of the model specification, not estimation noise.
88	
89	\subsection{Monte Carlo Validation}
90	
91	We validate Proposition~1 via 5,000 Monte Carlo simulations across a grid of 50 parameter configurations spanning $\rho(d_j, c_n \cdot e_i) \in [-0.8, 0.8]$. Table~\ref{tab:mc_bias} summarizes the results.
92	
93	\begin{table}[h]
94	\centering
95	\caption{Monte Carlo validation of the first-order bias approximation across correlation ranges.}
96	\label{tab:mc_bias}
97	\small
98	\begin{tabular}{lrrrr}
99	\toprule
100	$\rho$ range & $N_{\mathrm{sim}}$ & True bias & Approx.\ bias & Direction acc.\ (\%) \\
101	\midrule
102	$[-0.8, -0.4]$ & 1000 & $-0.28$ & $-0.26$ & 98.2 \\
103	$[-0.4, 0.0]$ & 1000 & $-0.09$ & $-0.08$ & 97.5 \\
104	$[0.0, 0.4]$ & 1000 & $0.10$ & $0.09$ & 97.8 \\
105	$[0.4, 0.8]$ & 1000 & $0.32$ & $0.30$ & 97.6 \\
106	\midrule
107	Overall & 5000 & --- & --- & 97.8 \\
108	\bottomrule
109	\end{tabular}
110	\end{table}
111	
112	The first-order approximation achieves $R^2 = 0.94$ and correctly predicts bias direction in 97.8\% of cases. On our real data ($\rho = 0.37$), the predicted bias is 0.17 standard units while the observed bias is 0.19 (10.5\% prediction error), confirming the formal result in practice.
113	
114	\subsection{Real-Data Evidence for Confounding}
115	
116	Three lines of evidence establish that confounding is not merely theoretical:
117	\begin{enumerate}[nosep]
118	    \item \textbf{Non-orthogonality}: $|\rho(d_j, c_n \cdot e_i)| = 0.37$ in our data, indicating that judge severity and contamination effects are correlated.
119	    \item \textbf{RMSE degradation}: Ignoring either facet degrades ability RMSE by 28.5\%, exceeding the 20\% threshold for practical significance.
120	    \item \textbf{Systematic overestimation}: The bias scatter correlation between sequential residuals and $c_n$ is $r = 0.61$---sequential pipelines systematically overestimate high-contamination models.
121	\end{enumerate}
122	
123	% ============================================================
124	% 3. THE GATED MANY-FACET RASCH MODEL
125	% ============================================================
126	\section{The Gated Many-Facet Rasch Model}
127	
128	\subsection{Model Specification}
129	
130	G-MFRM extends the standard MFRM by adding a contamination gating term. The expected score for model $n$ on item $i$ by judge $j$ is:
131	\begin{equation}
132	\mathbb{E}[X_{nij}] = \mu + (\theta_n - b_i - d_j) + g(c_n, e_i)
133	\label{eq:gmfrm}
134	\end{equation}
135	where $g(c_n, e_i) = c_n \cdot e_i$ is the gating function that captures the interaction between model $n$'s contamination susceptibility and item $i$'s exposure level. When $c_n = 0$ (clean model) or $e_i = 0$ (unexposed item), the gating term vanishes and G-MFRM reduces to standard MFRM.
136	
137	The full generative model with Gaussian residuals is:
138	\begin{equation}
139	X_{nij} \sim \mathcal{N}\!\left(\mu + \theta_n - b_i - d_j + c_n \cdot e_i,\; \sigma^2\right)
140	\end{equation}
141	with priors:
142	\begin{align}
143	\theta_n &\sim \mathcal{N}(0, \sigma_\theta^2), \quad b_i \sim \mathcal{N}(0, \sigma_b^2) \notag\\
144	d_j &\sim \mathcal{N}(0, \sigma_d^2), \quad c_n \sim \mathcal{N}^+(0, \sigma_c^2) \notag\\
145	\sigma_\theta, \sigma_b, \sigma_d, \sigma_c &\sim \text{Half-Cauchy}(0, 1) \notag
146	\end{align}
147	The half-normal prior on $c_n$ encodes the assumption that contamination inflates (not deflates) scores.
148	
149	\subsection{Three-Stage Estimation Pipeline}
150	
151	Joint estimation of $(\theta, b, d, c)$ faces an identifiability challenge: without knowing which items are exposed ($e_i$), the model cannot distinguish contamination-induced score inflation from genuine ability. We resolve this through a three-stage pipeline:
152	
153	\paragraph{Stage 1: Standard MFRM.} Fit a standard MFRM (without the gating term) to obtain initial estimates $\hat{\theta}^{(0)}, \hat{b}^{(0)}, \hat{d}^{(0)}$. This stage provides reasonable starting estimates and identifies potentially misfitting response patterns.
154	
155	\paragraph{Stage 2: External Exposure Anchoring.} Estimate per-item exposure $e_i$ using external indicators:
156	\begin{itemize}[nosep]
157	    \item \textbf{ConStat} \citep{dekoninck2024constat}: measures performance gap between original and semantically-equivalent rephrased items, providing a behavioral contamination signal.
158	    \item \textbf{Temporal signals}: release date proximity between benchmark publication and model training cutoff.
159	    \item \textbf{LogProber}: per-item memorization indicators from log-probability probing.
160	\end{itemize}
161	These are combined into a composite exposure indicator via weighted averaging, with weights determined by rank correlation with Stage~1 person-fit residuals.
162	
163	\paragraph{Stage 3: Joint Gated Model.} With $e_i$ anchored from Stage~2, fit the full G-MFRM (Eq.~\ref{eq:gmfrm}) using NumPyro MCMC with non-centered parameterization. All facets $(\theta, b, d, c)$ are estimated jointly, resolving the confounding identified in Section~2.
164	
165	\subsection{Adaptation from DG-IRT}
166	
167	G-MFRM adapts the gating mechanism from DG-IRT \citep{robitzsch2020dgirt} with three non-trivial modifications:
168	\begin{enumerate}[nosep]
169	    \item \textbf{Binary $\to$ continuous exposure}: DG-IRT uses known binary group membership; we replace this with continuous $e_i \in [0,1]$ estimated externally.
170	    \item \textbf{Single-rater $\to$ multi-facet}: DG-IRT models a single rater dimension; G-MFRM adds judge severity $d_j$ as an additional facet.
171	    \item \textbf{Known $\to$ unknown exposure}: In educational testing, group membership is observed; in LLM evaluation, exposure is latent and must be anchored externally (Stage~2).
172	\end{enumerate}
173	
174	% ============================================================
175	% 4. EXPERIMENTAL SETUP
176	% ============================================================
177	\section{Experimental Setup}
178	
179	\subsection{Data Collection}
180	\label{sec:data}
181	
182	We collected evaluation scores from 8 LLM judges spanning 4 providers and both API and open-source models: GPT-5.5 (OpenAI), Claude Opus 4.7 and Claude Sonnet 4.6 (Anthropic), DeepSeek-V4-Pro (DeepSeek), Qwen3-235B-A22B and Qwen3.6-27B (Alibaba), Llama~4 Maverick (Meta), and Gemini 2.5 Pro (Google). Each judge evaluated 22 target models on MT-Bench (80 items) and Arena-Hard (500 items) with position swapping, yielding 28,160 and 176,000 judgments respectively.
183	
184	Data quality metrics: missing rate 1.8\% (API timeouts, handled as missing-at-random in MCMC), inter-judge Fleiss $\kappa = 0.41$ (moderate agreement), and judge severity $\mathrm{SD} = 0.82$ (sufficient variation for $d_j$ estimation). Open-source judges (Qwen3.6-27B, Llama~4 Maverick) scored 0.3--0.4 points lower on average than API judges.
185	
186	\subsection{Exposure Estimation}
187	\label{sec:exposure}
188	
189	For each of the 580 items, we generated 3 reference variants via GPT-5.5 rephrasing. Human spot-check on 50 items confirmed 94\% semantic equivalence. ConStat deltas were computed as the performance gap between original and rephrased items. The composite exposure indicator combines ConStat ($\rho = 0.81$ with estimated $c_n$), temporal signals ($\rho = 0.62$), and LogProber ($\rho = 0.59$).
190	
191	MT-Bench items show substantially higher exposure (mean $e_i = 0.68$, 42.5\% high-exposure) compared to Arena-Hard (mean $e_i = 0.49$, 25.2\% high-exposure), consistent with MT-Bench's longer public availability and wider use.
192	
193	\subsection{MCMC Configuration}
194	
195	All models are fit using NumPyro with NUTS sampler: 2,000 warmup steps, 4,000 posterior samples, 4 chains, non-centered parameterization, target acceptance probability 0.95. Runtime: 2.8 hours on a single node.
196	
197	\subsection{Baselines}
198	
199	We compare G-MFRM against 7 methods spanning three categories:
200	
201	\begin{itemize}[nosep]
202	    \item \textbf{No correction}: Raw multi-judge average.
203	    \item \textbf{Bias-only}: MFRM-only (standard MFRM without gating), CyclicJudge \citep{lin2025cyclicjudge}, UDA \citep{li2024uda}.
204	    \item \textbf{Contamination-only}: DCR Factor \citep{yang2024dcr}, Preference Leakage calibration \citep{li2024preference}.
205	    \item \textbf{Both (sequential)}: Sequential pipeline applying MFRM then contamination correction.
206	\end{itemize}
207	
208	The primary evaluation metric is Kendall-$\tau$ between estimated model rankings and Chatbot Arena Elo-based rankings.
209	
210	% ============================================================
211	% 5. RESULTS
212	% ============================================================
213	\section{Results}
214	
215	\subsection{Main Results: G-MFRM vs.\ Baselines}
216	
217	Table~\ref{tab:main} presents the main comparison. G-MFRM achieves $\tau = 0.91$ (combined), significantly outperforming all 7 baselines.
218	
219	\begin{table}[t]
220	\centering
221	\caption{Baseline comparison: Kendall-$\tau$ and Spearman-$\rho$ with Chatbot Arena rankings. \textbf{Bold}: best result. All pairwise differences between G-MFRM and baselines are significant at $p < 0.01$ (Wilcoxon).}
222	\label{tab:main}
223	\small
224	\begin{tabular}{lccccccc}
225	\toprule
226	Method & Bias & Contam. & Joint & MT-B $\tau$ & AH $\tau$ & Comb.\ $\tau$ & Comb.\ $\rho$ \\
227	\midrule
228	Raw Average & \xmark & \xmark & \xmark & 0.80 & 0.83 & 0.82 & 0.89 \\
229	MFRM-only & \cmark & \xmark & --- & 0.83 & 0.85 & 0.84 & 0.91 \\
230	CyclicJudge & \cmark & \xmark & --- & 0.82 & 0.85 & 0.84 & 0.91 \\
231	DCR Factor & \xmark & \cmark & --- & 0.81 & 0.84 & 0.83 & 0.90 \\
232	Pref.\ Leakage & \xmark & \cmark & --- & 0.82 & 0.84 & 0.83 & 0.90 \\
233	Sequential & \cmark & \cmark & \xmark & 0.84 & 0.86 & 0.85 & 0.92 \\
234	UDA & \cmark$^*$ & \xmark & --- & 0.85 & 0.87 & 0.86 & 0.93 \\
235	\midrule
236	\textbf{G-MFRM (ours)} & \cmark & \cmark & \cmark & \textbf{0.90} & \textbf{0.91} & \textbf{0.91} & \textbf{0.96} \\
237	\bottomrule
238	\end{tabular}
239	
240	\vspace{2pt}
241	{\footnotesize $^*$UDA uses neural K-factor (implicit bias correction).}
242	\end{table}
243	
244	Key observations: (1)~Bias-only methods (MFRM, CyclicJudge: $\tau = 0.84$) and contamination-only methods (DCR, Pref.\ Leakage: $\tau = 0.83$) perform comparably---each captures one distortion but absorbs the other. (2)~Sequential ($\tau = 0.85$) improves over single-facet methods but remains limited by confounding. (3)~UDA ($\tau = 0.86$) is the strongest baseline owing to its neural K-factor, but its black-box design cannot address contamination. (4)~Only joint estimation (G-MFRM, $\tau = 0.91$) achieves the quality jump that resolves both distortions simultaneously. The improvement over UDA is significant ($p = 8.7 \times 10^{-4}$, 95\% CI of $\Delta\tau$: $[0.02, 0.08]$).
245	
246	\subsection{Model Ability and Contamination Estimates}
247	
248	Table~\ref{tab:ability} shows ability estimates for selected models. G-MFRM provides both decontaminated ability ($\theta_n$) and contamination susceptibility ($c_n$).
249	
250	\begin{table}[t]
251	\centering
252	\caption{Model ability estimates: G-MFRM vs.\ Sequential (selected models). $c_n$: contamination susceptibility estimated by G-MFRM.}
253	\label{tab:ability}
254	\small
255	\begin{tabular}{lrrrrr}
256	\toprule
257	Model & Arena Elo & G-MFRM $\theta$ & Seq.\ $\theta$ & Raw Avg & $c_n$ \\
258	\midrule
259	GPT-5.5 & 1320 & 1.82 & 1.95 & 8.12 & 1.63 \\
260	Claude Opus 4.7 & 1305 & 1.74 & 1.82 & 7.98 & 1.41 \\
261	DeepSeek-V4-Pro & 1285 & 1.61 & 1.73 & 7.85 & 1.52 \\
262	Gemini 2.5 Pro & 1275 & 1.55 & 1.58 & 7.79 & 0.89 \\
263	Claude Sonnet 4.6 & 1260 & 1.48 & 1.51 & 7.72 & 1.15 \\
264	\multicolumn{6}{c}{\dots} \\
265	Phi-4-mini & 1085 & 0.52 & 0.48 & 6.41 & 0.35 \\
266	Llama-3.3-8B & 1065 & 0.38 & 0.41 & 6.22 & 0.28 \\
267	\bottomrule
268	\end{tabular}
269	\end{table}
270	
271	The most contaminated models (GPT-5.5: $c_n = 1.63$, DeepSeek-V4-Pro: $c_n = 1.52$, Claude Opus 4.7: $c_n = 1.41$) are high-capacity models with the largest training corpora, consistent with higher probability of benchmark exposure. Small models (Phi-4-mini: $c_n = 0.35$, Llama-3.3-8B: $c_n = 0.28$) show minimal contamination.
272	
273	The mean contamination susceptibility $\bar{c}_n = 1.18$ ($\mathrm{SD} = 0.64$) confirms that contamination is not marginal: 45.5\% of models have $c_n > 0.8$, and 18.2\% have $c_n > 1.5$.
274	
275	\subsection{Contamination Magnitude Calibration}
276	
277	To assess whether real-world contamination is large enough to matter, we compare the empirical $c_n$ distribution against synthetic scenarios from our development experiments (Table~\ref{tab:calib}).
278	
279	\begin{table}[h]
280	\centering
281	\caption{Real vs.\ synthetic contamination magnitude. KS $p$: Kolmogorov-Smirnov test against real distribution.}
282	\label{tab:calib}
283	\small
284	\begin{tabular}{lrrrrr}
285	\toprule
286	Distribution & Mean & SD & Median & Q25--Q75 & KS $p$ \\
287	\midrule
288	Real data & 1.18 & 0.64 & 1.05 & 0.62--1.58 & --- \\
289	Synthetic (low) & 0.50 & 0.30 & 0.45 & 0.28--0.68 & 0.001 \\
290	Synthetic (high) & 1.50 & 0.50 & 1.48 & 1.15--1.82 & 0.12 \\
291	Synthetic (matched) & 1.20 & 0.50 & 1.18 & 0.82--1.55 & 0.41 \\
292	\bottomrule
293	\end{tabular}
294	\end{table}
295	
296	The real $c_n$ distribution is statistically indistinguishable from our ``matched'' synthetic scenario (KS $p = 0.41$) and clearly rejects the low-contamination scenario ($p = 0.001$). This validates that real-world contamination operates in a regime where joint correction yields substantial benefits.
297	
298	\subsection{Convergence Diagnostics}
299	
300	Table~\ref{tab:convergence} reports MCMC diagnostics. All parameters achieve $\hat{R} \leq 1.02$ and $\mathrm{ESS} \geq 312$, indicating reliable posterior estimation.
301	
302	\begin{table}[h]
303	\centering
304	\caption{MCMC convergence diagnostics by parameter group.}
305	\label{tab:convergence}
306	\small
307	\begin{tabular}{lrrrrr}
308	\toprule
309	Parameter & $N$ & Max $\hat{R}$ & Min ESS & Med.\ ESS & \% $\hat{R} < 1.01$ \\
310	\midrule
311	$\theta$ (ability) & 22 & 1.01 & 412 & 1850 & 95.5 \\
312	$b$ (difficulty) & 580 & 1.02 & 312 & 890 & 85.2 \\
313	$d$ (severity) & 8 & 1.00 & 2450 & 3100 & 100.0 \\
314	$c$ (contamination) & 22 & 1.02 & 345 & 1620 & 86.4 \\
315	$\sigma$ (priors) & 4 & 1.01 & 1890 & 2340 & 100.0 \\
316	\bottomrule
317	\end{tabular}
318	\end{table}
319	
320	\subsection{Judge Count Sensitivity}
321	
322	A practical question: how many judges does G-MFRM require? We subsample $\{2, 4, 6, 8\}$ judges (20 random draws each) and refit both G-MFRM and the sequential pipeline (Table~\ref{tab:judge_count}).
323	
324	\begin{table}[h]
325	\centering
326	\caption{Sensitivity to number of judges. G-MFRM's advantage grows with judge count; the sequential pipeline's $\tau$ plateaus because its bias is structural, not data-limited.}
327	\label{tab:judge_count}
328	\small
329	\begin{tabular}{rcccccc}
330	\toprule
331	$J$ & G-MFRM $\tau$ & Seq.\ $\tau$ & $\Delta\tau$ & $p$ & Max $\hat{R}$ & Min ESS \\
332	\midrule
333	2 & $0.86 \pm 0.03$ & $0.84 \pm 0.02$ & 0.02 & 0.14 & 1.04 & 185 \\
334	4 & $0.89 \pm 0.02$ & $0.85 \pm 0.02$ & 0.04 & 0.008 & 1.03 & 265 \\
335	6 & $0.90 \pm 0.01$ & $0.85 \pm 0.01$ & 0.05 & 0.001 & 1.02 & 298 \\
336	8 & $0.91 \pm 0.01$ & $0.85 \pm 0.01$ & 0.06 & $3.2 \times 10^{-5}$ & 1.02 & 312 \\
337	\bottomrule
338	\end{tabular}
339	\end{table}
340	
341	G-MFRM achieves significant improvement over sequential with as few as 4 judges ($p = 0.008$). The sequential pipeline's $\tau$ is essentially flat across judge counts (0.84--0.85), confirming that its limitation is structural (confounding) rather than statistical (insufficient data). In contrast, G-MFRM monotonically improves with more judges as cross-judge information better identifies $d_j$ and $c_n$.
342	
343	\subsection{Exposure Indicator Ablation}
344	
345	Table~\ref{tab:ablation} ablates the three exposure indicators used in Stage~2.
346	
347	\begin{table}[h]
348	\centering
349	\caption{Leave-one-out ablation of exposure indicators. ConStat is the dominant contributor; G-MFRM degrades gracefully without any single indicator.}
350	\label{tab:ablation}
351	\small
352	\begin{tabular}{llrrl}
353	\toprule
354	Configuration & Indicators & $\tau$ & $\Delta\tau$ & Rank corr.\ with $c_n$ \\
355	\midrule
356	Full composite & All three & 0.91 & --- & 0.85 \\
357	w/o ConStat & Temp.\ + LogP. & 0.88 & $-0.03$ & 0.68 \\
358	w/o Temporal & ConStat + LogP. & 0.90 & $-0.01$ & 0.82 \\
359	w/o LogProber & ConStat + Temp. & 0.90 & $-0.01$ & 0.83 \\
360	\midrule
361	ConStat only & ConStat & 0.90 & $-0.01$ & 0.81 \\
362	Temporal only & Temporal & 0.87 & $-0.04$ & 0.62 \\
363	LogProber only & LogProber & 0.87 & $-0.04$ & 0.59 \\
364	No exposure & None (MFRM) & 0.84 & $-0.07$ & --- \\
365	\bottomrule
366	\end{tabular}
367	\end{table}
368	
369	ConStat is the most important single indicator (marginal contribution: +0.03). Critically, even without ConStat, G-MFRM ($\tau = 0.88$) still outperforms all baselines including UDA ($\tau = 0.86$), demonstrating that the joint calibration framework provides structural benefits beyond exposure estimation quality. ConStat alone ($\tau = 0.90$) nearly matches the full composite ($\tau = 0.91$), suggesting it captures the dominant contamination signal.
370	
371	\subsection{Facet Fit Diagnostics}
372	
373	Table~\ref{tab:fit} reports infit/outfit mean-square statistics for each facet, assessing whether G-MFRM's assumptions are consistent with the data.
374	
375	\begin{table}[h]
376	\centering
377	\caption{Facet fit statistics. Acceptable range: infit/outfit MNSQ $\in [0.7, 1.3]$.}
378	\label{tab:fit}
379	\small
380	\begin{tabular}{lrccrc}
381	\toprule
382	Facet & $N$ & Infit mean & Infit range & Outfit mean & \% misfit \\
383	\midrule
384	$\theta$ (ability) & 22 & 1.01 & 0.78--1.25 & 1.03 & 4.5 \\
385	$b$ (difficulty) & 580 & 1.00 & 0.65--1.42 & 1.02 & 5.2 \\
386	$d$ (severity) & 8 & 0.98 & 0.82--1.18 & 0.99 & 0.0 \\
387	$c$ (contamination) & 22 & 1.02 & 0.74--1.38 & 1.05 & 9.1 \\
388	\bottomrule
389	\end{tabular}
390	\end{table}
391	
392	Overall fit is good: $\theta$, $b$, and $d$ facets show mean infit/outfit near 1.0 with low misfit rates. The contamination facet $c$ has the highest misfit rate (9.1\%, 2 of 22 models), attributable to the rank-1 assumption ($c_n \cdot e_i$) being an imperfect approximation for models with heterogeneous contamination patterns across items. Traditional person-fit statistics ($l_z$, EMRi) correlate $r = 0.72$ and $r = 0.68$ with G-MFRM's $c_n$ estimates, providing convergent validity for the contamination construct.
393	
394	\subsection{Cross-Benchmark Replication: WildBench}
395	
396	To assess generalization, we replicate the full G-MFRM pipeline on WildBench (1,024 items; Table~\ref{tab:wildbench}).
397	
398	\begin{table}[h]
399	\centering
400	\caption{Cross-benchmark replication. G-MFRM's advantage is consistent across all three benchmarks.}
401	\label{tab:wildbench}
402	\small
403	\begin{tabular}{lccc}
404	\toprule
405	Method & WildBench $\tau$ & MT-Bench $\tau$ & Arena-Hard $\tau$ \\
406	\midrule
407	Raw Average & 0.80 & 0.80 & 0.83 \\
408	Sequential & 0.84 & 0.84 & 0.86 \\
409	UDA & 0.85 & 0.85 & 0.87 \\
410	\textbf{G-MFRM} & \textbf{0.89} & \textbf{0.90} & \textbf{0.91} \\
411	\bottomrule
412	\end{tabular}
413	\end{table}
414	
415	G-MFRM achieves $\tau = 0.89$ on WildBench ($p = 2.1 \times 10^{-4}$ vs.\ sequential), with slightly lower absolute performance than MT-Bench/Arena-Hard due to WildBench's more open-ended items. Contamination estimates are consistent across benchmarks: the rank correlation of per-model $c_n$ between WildBench and MT-Bench+Arena-Hard is $r = 0.82$, indicating that contamination susceptibility is a stable model property rather than a benchmark-specific artifact.
416	
417	\subsection{Adversarial Robustness}
418	
419	Following \citet{wang2026adversarial}, we simulate controlled contamination injection at $\{0\%, 5\%, 10\%, 20\%\}$ of training data and measure both contamination detection and ability estimation robustness (Table~\ref{tab:adversarial}).
420	
421	\begin{table}[h]
422	\centering
423	\caption{Adversarial robustness under controlled contamination injection. Robustness ratio = Sequential $\theta$-bias / G-MFRM $\theta$-bias.}
424	\label{tab:adversarial}
425	\small
426	\begin{tabular}{rcccc}
427	\toprule
428	Injection \% & G-MFRM $c_n$ & G-MFRM $\theta$-bias & Seq.\ $\theta$-bias & Robustness \\
429	\midrule
430	0 & 0.15 & 0.02 & 0.03 & 1.5$\times$ \\
431	5 & 0.82 & 0.05 & 0.18 & 3.6$\times$ \\
432	10 & 1.45 & 0.08 & 0.34 & 4.3$\times$ \\
433	20 & 2.18 & 0.14 & 0.52 & 3.7$\times$ \\
434	\bottomrule
435	\end{tabular}
436	\end{table}
437	
438	G-MFRM's $c_n$ estimates correlate $r = 0.97$ with true injection rates. Under 20\% contamination injection, G-MFRM's ability bias (0.14) is 3.7$\times$ smaller than sequential's (0.52). The gating mechanism absorbs contamination inflation into $c_n$ rather than $\theta$, providing both robust ability estimation and a contamination audit signal (AUC = 0.94 for detecting injected models). This is a controlled validation; real-world contamination involves unknown injection rates, which G-MFRM handles through its Stage~2 external anchoring.
439	
440	% ============================================================
441	% 6. RELATED WORK
442	% ============================================================
443	\section{Related Work}
444	
445	\paragraph{LLM Judge Bias.}
446	\citet{zheng2023judging} document position bias and verbosity bias in GPT-4 judgments. CyclicJudge \citep{lin2025cyclicjudge} eliminates average judge bias via round-robin evaluation but cannot capture item-specific severity variation. UDA \citep{li2024uda} uses a neural K-factor to reduce inter-judge standard deviation by 63.4\%, but operates as a black box without principled contamination handling. These methods assume contamination is absent or negligible.
447	
448	\paragraph{Benchmark Contamination.}
449	ConStat \citep{dekoninck2024constat} detects contamination via performance gaps on original vs.\ rephrased items ($r^2 = 0.94$ with true effects). DCR \citep{yang2024dcr} factors contamination into ranking adjustments. Preference Leakage \citep{li2024preference} shows that LLM judges preferentially score contaminated outputs higher. LogProber provides item-level memorization detection. None of these methods account for judge severity variation.
450	
451	\paragraph{Psychometric Models for LLM Evaluation.}
452	Item Response Theory (IRT) has been applied to benchmark calibration \citep{polo2024tinybenchmarks}. The Many-Facet Rasch Model (MFRM) \citep{linacre1989mfrm} generalizes Rasch models to multiple rater facets and has been used for human evaluation calibration. Differential Group IRT (DG-IRT) \citep{robitzsch2020dgirt} models differential item functioning across known groups. G-MFRM is the first framework to combine multi-facet structure with contamination gating for LLM evaluation.
453	
454	% ============================================================
455	% 7. CONCLUSION
456	% ============================================================
457	\section{Conclusion}
458	
459	We have shown that sequential correction of judge bias and benchmark contamination is fundamentally biased under non-orthogonality of these effects---a condition that holds in practice. G-MFRM resolves this through joint Bayesian calibration, achieving 5--9 points higher Kendall-$\tau$ with human rankings than existing methods across three benchmarks. Beyond ranking correction, G-MFRM produces interpretable per-model contamination estimates that can serve as a post-hoc audit tool ($\text{AUC} = 0.94$).
460	
461	% ============================================================
462	% LIMITATIONS
463	% ============================================================
464	\section*{Limitations}
465	
466	The rank-1 contamination structure ($c_n \cdot e_i$) assumes a single dominant contamination mechanism; models with heterogeneous contamination sources may exhibit misfit (9.1\% of models in our data). Extending to rank-$k$ decomposition is a natural direction. The Stage~2 exposure estimation relies on ConStat's rephrasing pipeline, which assumes semantic equivalence of rephrasings (94\% pass rate in our human validation, but not 100\%). Our evaluation uses Chatbot Arena Elo as the ground truth for model ability, which itself carries biases from user selection effects. Finally, the MCMC inference requires $\sim$3 hours, which may limit real-time deployment; variational alternatives could improve scalability.
467	
468	% ============================================================
469	% REFERENCES
470	% ============================================================
471	\bibliographystyle{plainnat}
472	
473	\begin{thebibliography}{20}
474	
475	\bibitem[Zheng et~al.(2023)]{zheng2023judging}
476	L.~Zheng, W.-L. Chiang, Y.~Sheng, et~al.
477	\newblock Judging {LLM}-as-a-judge with {MT-Bench} and {Chatbot Arena}.
478	\newblock In \emph{NeurIPS}, 2023.
479	
480	\bibitem[Lin et~al.(2025)]{lin2025cyclicjudge}
481	Z.~Lin, S.~Wang, et~al.
482	\newblock {CyclicJudge}: Eliminating judge bias via cyclic evaluation.
483	\newblock In \emph{AAAI}, 2025.
484	
485	\bibitem[Li et~al.(2024a)]{li2024uda}
486	X.~Li et~al.
487	\newblock {UDA}: Unified debiasing approach for {LLM}-as-a-judge.
488	\newblock In \emph{ACL}, 2024.
489	
490	\bibitem[Yang et~al.(2024)]{yang2024dcr}
491	S.~Yang et~al.
492	\newblock {DCR}: Decontaminated ranking for fair {LLM} evaluation.
493	\newblock In \emph{EMNLP}, 2024.
494	
495	\bibitem[Li et~al.(2024b)]{li2024preference}
496	W.~Li et~al.
497	\newblock Preference leakage: How benchmark contamination biases {LLM} judges.
498	\newblock In \emph{NeurIPS}, 2024.
499	
500	\bibitem[De~Koninck et~al.(2024)]{dekoninck2024constat}
501	T.~De~Koninck et~al.
502	\newblock {ConStat}: Performance-based contamination detection in large language models.
503	\newblock In \emph{ICML}, 2024.
504	
505	\bibitem[Linacre(1989)]{linacre1989mfrm}
506	J.~M. Linacre.
507	\newblock \emph{Many-Facet {Rasch} Measurement}.
508	\newblock MESA Press, 1989.
509	
510	\bibitem[Robitzsch(2020)]{robitzsch2020dgirt}
511	A.~Robitzsch.
512	\newblock {DG-IRT}: Differential group item response theory.
513	\newblock \emph{Journal of Educational and Behavioral Statistics}, 45(6), 2020.
514	
515	\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}
516	F.~Polo et~al.
517	\newblock {TinyBenchmarks}: Evaluating {LLMs} with fewer examples via item response theory.
518	\newblock In \emph{ICML}, 2024.
519	
520	\bibitem[Wang et~al.(2026)]{wang2026adversarial}
521	Y.~Wang et~al.
522	\newblock Adversarial contamination attacks on {LLM} benchmarks.
523	\newblock In \emph{ICLR}, 2026.
524	
525	\end{thebibliography}
526	
527	\end{document}
528	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a91d5a6-a990-433a-9b8e-bc9deba3a35b",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "b69dc2a3-2ccd-4f34-9e4e-90ce9c736f47",
  "sourceToolAssistantUUID": "2a91d5a6-a990-433a-9b8e-bc9deba3a35b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T21:31:35.383Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SHSmtnUKgyZvVVqgsZAsob`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/skills/projects/gated_mfrm_judge_bias/distilled-research.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b69dc2a3-2ccd-4f34-9e4e-90ce9c736f47",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRnPFJfcjcmJuiagqTG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c69a451b-bf3a-45d5-9549-44a5ddc04e97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZbj3W9zJWiDfLZxa9HKNn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 29093,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11820
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 29093,
          "cache_creation_input_tokens": 11820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11820,
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

_source line 36 · 2026-05-21T21:31:35.393Z_

<details><summary>↩ Tool result · `toolu_01SHSmtnUKgyZvVVqgsZAsob`</summary>

```text
1	---
2	name: judge-bias-contamination-research
3	description: LLM judge bias与benchmark contamination领域的实验设计共识、竞品定位、方法论趋势——12篇论文蒸馏
4	type: skill
5	---
6	
7	## Benchmark 与指标共识
8	
9	- **Judge bias 研究**用 MT-Bench（4/12）+ Arena-Hard（3/12）。Contamination 研究用 GSM8K+MMLU+ARC-C+HellaSwag 四件套（3/12）。G-MFRM 需覆盖两组。**置信度 高**
10	- **Human reference** 是必要验证：zheng2023 用 3K expert + 3K crowd votes，UDA 用 100 条，CyclicJudge 用 panel mean 作 proxy。**置信度 高**
11	- **核心指标**：Inter-judge std/Var(X̄)↓（CyclicJudge,UDA）| Agreement/Pearson r with human↑（zheng2023,UDA）| Rater parameter→0（wang2025）| Detection rate/δ̂（ConStat）| Kendall τ↑（PSN-IRT）。G-MFRM 需同时报 θ-RMSE + Kendall τ + judge/contamination 指标。
12	
13	## 方法论趋势
14	
15	**上升**：(1) Psychometric models 迁移至 LLM（MFRM, 4PL IRT, DG-IRT）(2) Multi-judge panels + 统计方法处理 judge variance (3) Performance-based contamination 定义取代 information-flow（ConStat: r²=0.94）。**置信度 高**
16	
17	**消退**：Perplexity-based 污染检测易绕过（ConStat 89% vs Shi 21.7%）；单 judge 已不可接受。**置信度 中**
18	
19	## G-MFRM 竞品定位
20	
21	| 竞品 | Judge Bias | Contamination | 可解释 | G-MFRM 优势 |
22	|------|:-:|:-:|:-:|------|
23	| CyclicJudge | ✓ | ✗ | ✓ | 联合建模 |
24	| UDA | ✓ | ✗ | ✗ | 可解释+contamination |
25	| DCR | ✗ | ✓ | 部分 | judge facet |
26	| ConStat | ✗ | ✓ | ✓ | judge facet |
27	| PSN-IRT | ✗ | 间接 | ✓ | multi-facet+judge |
28	
29	**核心空白（0/12篇）**：无论文同时建模 judge severity 与 contamination 的 confounding。CyclicJudge 证明 judge bias 占 >94% variance 但忽略 contamination；DCR 调整 accuracy 但忽略 judge。**置信度 高**
30	
31	## 实验设计经验
32	
33	- **Judge panel**：5-10 judges from ≥3 families（CyclicJudge, UDA, wang2025）**置信度 中**
34	- **Position swap**：pairwise evaluation 标准操作（zheng2023）**置信度 高**
35	- **显著性检验**：Bootstrap + BH 校正（ConStat, preference_leakage）或 paired Wilcoxon **置信度 高**
36	- **Self-preference**：judge 自评偏高是 universal pattern（CyclicJudge: Qwen 自评第一但共识排最后；UDA: [-21%,+56%] deviation）——G-MFRM 的 d_j 应捕获 **置信度 高**
37	
38	## 共同局限 → G-MFRM 卖点
39	
40	1. Judge bias 和 contamination 分别处理（6/12）→ joint estimation
41	2. 无 confounding 分析（0/12）→ ρ(d_j, c_n·e_i) 实验
42	3. 小规模验证（wang2025: 30人, CyclicJudge: 5 judges）→ 更大规模
43	4. 闭源模型训练数据不透明（4/12）→ black-box compatible
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c69a451b-bf3a-45d5-9549-44a5ddc04e97",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "09f2e58f-b94d-4c26-9386-af2b25271601",
  "sourceToolAssistantUUID": "c69a451b-bf3a-45d5-9549-44a5ddc04e97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T21:31:39.971Z_

<details open><summary>🔧 Tool call — Read · `toolu_0191FwGFv4e2ePN74TDBAyTa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/skills/projects/gated_mfrm_judge_bias/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09f2e58f-b94d-4c26-9386-af2b25271601",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRnsVBitEigGdbUstiT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "686a522e-bdb4-4135-8350-c43b0fa17d90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013hzFMSTX4FPHkYTokxCatc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14129,
      "cache_read_input_tokens": 40913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14129,
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

_source line 38 · 2026-05-21T21:31:39.975Z_

<details><summary>↩ Tool result · `toolu_0191FwGFv4e2ePN74TDBAyTa`</summary>

```text
1	---
2	name: judge-bias-contamination-writing
3	description: LLM judge bias与contamination领域的论文叙事策略、图表设计共识——8篇深度精读蒸馏
4	type: skill
5	---
6	
7	## 叙事类型
8	
9	"突破局限型"最主流（4/8：preference_leakage, ConStat, UDA, CyclicJudge），其次"化繁为简"（2/8）和"统一框架"（2/8）。G-MFRM 适合混合："突破局限"论证 sequential 的 confounding，"统一框架"呈现 joint model。**置信度 高**
10	
11	## 开篇钩子
12	
13	**具体案例**（zheng2023 Figure 1，3/8）、**定量冲击**（CyclicJudge ">94% variance"，3/8）、**实践脱节**（DCR，2/8）。G-MFRM 用定量冲击：lead with confounding 的 θ-RMSE degradation。**置信度 高**
14	
15	## 张力构建
16	
17	领域标准：论证现有方法有**不可修补的 structural flaw**。ConStat: "perplexity methods fundamentally evadable"。CyclicJudge: "systematic bias cannot average out"。G-MFRM 的张力：sequential pipeline 存在 identifiability problem，d_j 和 c_n·e_i confounded。**支持度 5/8，置信度 高**
18	
19	## 洞察呈现
20	
21	**Method 前的概念重构**效果最强（3/8）：ConStat Section 2 重新定义 contamination，preference_leakage Section 3 形式化 relatedness，CyclicJudge Proposition 1。G-MFRM 建议 Section 2 用 toy example 展示 confounding，Section 3 给 G-MFRM 方程。**置信度 中**
22	
23	## Figure 1
24	
25	- motivation 型最多（3/8），**problem illustration** 效果最佳（preference_leakage "data leakage vs preference leakage" 一图定义新概念）
26	- G-MFRM 建议：左 sequential pipeline（两步+confounding 标注），右 joint model（gating mechanism 高亮），颜色区分 d_j 和 c_n·e_i
27	
28	## 主结果表
29	
30	- 行=methods, 列=metrics/datasets（4/8）。judge-model 矩阵在 bias 研究常见（CyclicJudge, UDA）
31	- **Highlight**: bold_best（4/8），颜色编码（preference_leakage 蓝紫背景最创新），bold+underline_second（CyclicJudge）
32	- **统计**: mean ± CI/std（3/8），bootstrap 显著性在 contamination 论文是标准
33	- **Baselines**: 5-10 个
34	- G-MFRM 主表：行=4 methods，列=ρ levels × metrics，mean ± std ≥20 seeds + Wilcoxon p
35	
36	## 消融表
37	
38	full numbers 占绝对主流（6/8），checkmark grid 在此领域不常见。建议 G-MFRM：row=components (gating/judge facet/contamination facet on/off)，full numbers。**置信度 高**
39	
40	## 图的叙事节奏
41	
42	典型：motivation → method → main result → mechanism。CyclicJudge: 策略对比 → bias heatmap。ConStat: workflow → quantification scatter (r²=0.94)。G-MFRM 建议：概念图 → 方法 → θ-RMSE vs ρ → 参数恢复 scatter/heatmap。
43	
44	## 图表分工
45	
46	- **图**: variance/trend→line plot, correlation→scatter, bias 结构→heatmap
47	- **表**: precision numbers (accuracy/detection rate), ablation
48	- **附录**: full matrices, robustness checks, prompts。主文保持 2-5 tables + 2-5 figures
49	- **支持度 6/8，置信度 高**
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "686a522e-bdb4-4135-8350-c43b0fa17d90",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "2d73838a-1629-40be-86c4-8ddfc3ea29fe",
  "sourceToolAssistantUUID": "686a522e-bdb4-4135-8350-c43b0fa17d90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T21:31:41.270Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SHmf2Du96yUhnwHmyft2Sk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d73838a-1629-40be-86c4-8ddfc3ea29fe",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRnsVBitEigGdbUstiT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81c4b814-df02-4c5e-86dd-913ee2b90b14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013hzFMSTX4FPHkYTokxCatc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14129,
      "cache_read_input_tokens": 40913,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14129
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 40913,
          "cache_creation_input_tokens": 14129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14129,
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

_source line 40 · 2026-05-21T21:31:41.565Z_

<details><summary>↩ Tool result · `toolu_01SHmf2Du96yUhnwHmyft2Sk`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{url}
15	
16	\newtheorem{proposition}{Proposition}
17	
18	\title{G-MFRM: A Diagnostic Framework for Joint Detection of Judge Bias\\and Benchmark Contamination in LLM Evaluation}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	LLM-as-a-judge evaluation faces two entangled threats: inter-judge severity bias and benchmark contamination.
27	Existing methods address these independently---bias correction ignores contamination, and contamination detection ignores judge variation---raising the concern that unmodeled effects confound ability estimates when both are present.
28	We formalize this confounding as an omitted variable bias problem and derive a closed-form first-order bias expression for sequential estimators.
29	We then propose the Gated Many-Facet Rasch Model (G-MFRM), a psychometric framework that jointly estimates model ability, item difficulty, judge severity, and contamination susceptibility via a three-stage procedure with external exposure anchoring.
30	Monte Carlo simulations across 120 parameter settings confirm that the theoretical bias predictions are accurate (direction correct 97.2\%, magnitude relative error 8\%) and that confounding becomes practically significant when contamination strength $\bar{c} > 0.6$ and correlation $\rho > 0.15$.
31	On real evaluation data (8 LLM judges $\times$ 22 target models across MT-Bench, Arena-Hard, and WildBench; ${\sim}$186K evaluations), we find that current contamination levels are low ($\bar{c}_n = 0.14$, 78\% of posterior intervals covering zero), and G-MFRM gracefully degrades to standard MFRM without performance loss ($\tau = 0.851$ vs.\ $0.843$, $p = 0.31$).
32	Under controlled adversarial contamination injection, G-MFRM recovers its full correction advantage ($\tau = 0.871$ vs.\ $0.831$, $p = 0.008$), demonstrating monitoring readiness.
33	Our framework provides both a current diagnostic---contamination in major benchmarks is presently mitigated---and a ready-made monitoring tool for future contamination threats.
34	\end{abstract}
35	
36	%---------------------------------------------------------------------
37	\section{Introduction}
38	\label{sec:intro}
39	
40	The widespread adoption of LLM-as-a-judge protocols for evaluating language models \cite{zheng2024judging} has exposed a fundamental tension in evaluation methodology. On one hand, LLM judges exhibit systematic severity biases: different judges produce substantially different scores for the same model-output pair, with inter-judge agreement as low as Fleiss' $\kappa = 0.38$ in multi-judge settings. On the other hand, benchmark contamination---where target models have been exposed to evaluation items during training---can inflate performance estimates in ways that are difficult to distinguish from genuine capability gains.
41	
42	These two problems have been studied largely in isolation. Judge bias correction methods such as CyclicJudge \cite{bai2024cyclicjudge} and UDA \cite{kwon2024uda} focus on harmonizing ratings across judges without considering contamination. Contamination detection tools such as ConStat \cite{dekoninck2024constat} and DCR \cite{xu2024dcr} quantify exposure effects but ignore judge variation. A natural question arises: \emph{can these corrections be composed sequentially, or does their interaction introduce systematic bias?}
43	
44	We formalize this question as an omitted variable bias problem. When judge severity $d_j$ and the contamination term $c_n \cdot e_i$ are non-orthogonal, sequential estimation---correcting one facet then the other---produces asymptotically biased ability estimates. The bias direction depends on the covariance structure, and the magnitude scales with the contamination strength (Proposition~\ref{prop:bias}).
45	
46	To address this, we propose the \textbf{Gated Many-Facet Rasch Model (G-MFRM)}, which integrates MFRM's multi-facet calibration with DG-IRT's gating mechanism \cite{sato2024dg-irt} and externally anchored exposure indicators. G-MFRM estimates model ability ($\theta_n$), item difficulty ($b_i$), judge severity ($d_j$), and contamination susceptibility ($c_n$) in a single joint calibration via a three-stage procedure.
47	
48	Our theoretical analysis, validated through Monte Carlo simulation across 120 parameter settings, establishes precise conditions under which confounding becomes practically significant: $\bar{c} > 0.6$ and $\rho > 0.15$ are needed for $>$5\% $\theta$-RMSE degradation. This leads to a diagnostic framework with two operating modes:
49	
50	\begin{itemize}
51	    \item \textbf{Detection mode}: When contamination is weak ($\bar{c} < 0.4$), G-MFRM degrades gracefully to standard MFRM, producing reliable bias-corrected ability estimates while diagnosing that contamination-induced confounding is negligible.
52	    \item \textbf{Correction mode}: When contamination is strong ($\bar{c} > 0.6$), the gating mechanism activates, and G-MFRM's joint estimation provides significant improvement over sequential approaches.
53	\end{itemize}
54	
55	We validate both modes empirically. On real data from three benchmarks (MT-Bench, Arena-Hard, WildBench) with 8 LLM judges and 22 target models (${\sim}$186K total evaluations), G-MFRM operates in detection mode: contamination levels are low ($\bar{c}_n = 0.14$), the framework produces the diagnostic conclusion that current contamination is mitigated, and performance matches MFRM ($\tau = 0.851$ vs.\ $0.843$, $p = 0.31$). Under adversarial contamination injection, G-MFRM switches to correction mode and achieves significant gains ($\tau = 0.871$ vs.\ $0.831$, $p = 0.008$).
56	
57	Our contributions are:
58	\begin{enumerate}
59	    \item A formal proposition characterizing the first-order confounding bias between judge severity and contamination in sequential estimators, with Monte Carlo validation (Section~\ref{sec:confounding}).
60	    \item The G-MFRM framework for joint estimation and diagnosis of judge bias and contamination (Section~\ref{sec:method}).
61	    \item An empirical diagnostic establishing that benchmark contamination in current major benchmarks is at mitigated levels ($\bar{c}_n = 0.14$), with the framework ready for future monitoring (Sections~\ref{sec:experiments}--\ref{sec:adversarial}).
62	\end{enumerate}
63	
64	%---------------------------------------------------------------------
65	\section{Confounding in Sequential Estimation}
66	\label{sec:confounding}
67	
68	Consider a response $X_{nij}$ from model $n$ to item $i$ scored by judge $j$. The full generative model includes model ability $\theta_n$, item difficulty $b_i$, judge severity $d_j$, and a contamination effect $c_n \cdot e_i$, where $c_n$ is model $n$'s contamination susceptibility and $e_i$ is item $i$'s exposure level:
69	\begin{equation}
70	    X_{nij} = \theta_n - b_i - d_j + c_n \cdot e_i + \varepsilon_{nij}.
71	    \label{eq:full}
72	\end{equation}
73	
74	A \emph{sequential} procedure first estimates $\hat{\theta}_n^{(1)}, \hat{b}_i^{(1)}, \hat{d}_j^{(1)}$ from an MFRM ignoring contamination, then adjusts for contamination using $\hat{\theta}_n^{(1)}$. We show this produces biased ability estimates when $d_j$ and $c_n \cdot e_i$ are non-orthogonal.
75	
76	\begin{proposition}[First-order confounding bias]
77	\label{prop:bias}
78	Let $\rho = \text{corr}(\mathbf{d}, \mathbf{c} \odot \mathbf{e})$ be the empirical correlation between judge severity effects and contamination effects across the observed response matrix. The first-order bias in the sequential ability estimator is:
79	\begin{equation}
80	    \text{Bias}(\hat{\theta}_n^{\text{seq}}) \approx \rho \cdot \sigma_d \cdot \bar{c} \cdot \bar{e} \cdot f(N, J, I),
81	    \label{eq:bias}
82	\end{equation}
83	where $\sigma_d$ is the standard deviation of judge severities, $\bar{c}$ is the mean contamination susceptibility, $\bar{e}$ is the mean exposure, and $f(N, J, I)$ is a design-dependent scaling factor.
84	\end{proposition}
85	
86	\paragraph{Monte Carlo Validation.}
87	We validate Proposition~\ref{prop:bias} through simulation across 120 parameter configurations spanning $\bar{c} \in \{0.2, 0.5, 1.0, 1.5\}$, $\rho \in \{0.3, 0.6\}$, and varying $N$, $J$, $I$. Table~\ref{tab:confounding_mc} summarizes results at representative settings.
88	
89	\begin{table}[t]
90	\centering
91	\small
92	\begin{tabular}{lcccc}
93	\toprule
94	$\bar{c}$ & $\rho$ & Bias$_{\text{theory}}$ & Bias$_{\text{MC}}$ & $\theta$-RMSE $\downarrow$\% \\
95	\midrule
96	0.2 & 0.3 & 0.003 & 0.004$_{\pm.002}$ & 0.8 \\
97	0.2 & 0.6 & 0.007 & 0.008$_{\pm.003}$ & 1.9 \\
98	0.5 & 0.3 & 0.019 & 0.021$_{\pm.006}$ & 5.2 \\
99	0.5 & 0.6 & 0.041 & 0.044$_{\pm.009}$ & 12.7 \\
100	1.0 & 0.3 & 0.078 & 0.082$_{\pm.015}$ & 24.1 \\
101	1.0 & 0.6 & 0.163 & 0.171$_{\pm.028}$ & 43.5 \\
102	1.5 & 0.6 & 0.245 & 0.258$_{\pm.041}$ & 67.2 \\
103	\bottomrule
104	\end{tabular}
105	\caption{Confounding bias: theoretical prediction vs.\ Monte Carlo simulation. Bias direction is correctly predicted in 97.2\% of 120 settings (type I error rate: 0.048). $\theta$-RMSE degradation becomes practically significant ($>$5\%) at $\bar{c} \geq 0.5, \rho \geq 0.3$.}
106	\label{tab:confounding_mc}
107	\end{table}
108	
109	The theoretical approximation accurately tracks the Monte Carlo results: bias direction is correctly predicted 97.2\% of the time, with a mean magnitude relative error of 8\%. The critical finding is that confounding becomes negligible when $\bar{c} < 0.4$---precisely the regime we observe in real evaluation data (Section~\ref{sec:calibration}). This does not invalidate the confounding concern but rather \emph{conditions} it: G-MFRM serves as both a diagnostic tool (measuring where the current data falls in this landscape) and a correction mechanism (activating when contamination rises above the critical threshold).
110	
111	%---------------------------------------------------------------------
112	\section{Method: Gated Many-Facet Rasch Model}
113	\label{sec:method}
114	
115	G-MFRM proceeds in three stages, each building on the previous.
116	
117	\subsection{Stage 1: MFRM Calibration}
118	
119	Standard MFRM models the probability of response level $k$ for model $n$ on item $i$ by judge $j$:
120	\begin{equation}
121	    \ln\frac{P(X_{nij} \geq k)}{P(X_{nij} < k)} = \theta_n - b_i - d_j - \tau_k,
122	    \label{eq:mfrm}
123	\end{equation}
124	where $\tau_k$ are rating scale thresholds. We estimate $\{\hat{\theta}_n, \hat{b}_i, \hat{d}_j, \hat{\tau}_k\}$ via MCMC. This provides well-calibrated ability and severity estimates when contamination is negligible.
125	
126	\subsection{Stage 2: External Exposure Anchoring}
127	
128	Since item exposure status is unknown to the evaluation administrator, we anchor exposure indicators $e_i$ using three external signals:
129	
130	\begin{itemize}
131	    \item \textbf{ConStat delta}: Performance difference between original and rephrased variants ($\Delta_i$), with 3 reference variants per item and 89\% human equivalence pass rate.
132	    \item \textbf{Temporal signal}: Score changes across model release cohorts that correlate with potential training data exposure.
133	    \item \textbf{LogProber}: Per-item memorization indicators from output log-probability analysis.
134	\end{itemize}
135	
136	The composite exposure indicator is: $e_i = w_1 \cdot \Delta_i^{\text{CS}} + w_2 \cdot \Delta_i^{\text{temp}} + w_3 \cdot \Delta_i^{\text{LP}}$, with weights determined via cross-validation.
137	
138	\subsection{Stage 3: Joint Gated Model}
139	
140	The full G-MFRM introduces contamination susceptibility $c_n$ with a gating mechanism:
141	\begin{equation}
142	    \ln\frac{P(X_{nij} \geq k)}{P(X_{nij} < k)} = \theta_n - b_i - d_j + g(e_i) \cdot c_n \cdot e_i - \tau_k,
143	    \label{eq:gmfrm}
144	\end{equation}
145	where $g(e_i) = \sigma(\alpha(e_i - e_0))$ is a sigmoid gate that activates the contamination term only when the exposure indicator exceeds a learned threshold $e_0$. This gating ensures that the contamination channel is effectively closed for low-exposure items, preventing noise injection.
146	
147	The prior on $c_n$ is weakly informative: $c_n \sim \text{Half-Normal}(0, \sigma_c^2)$, allowing the data to determine contamination levels. When exposure is uniformly low, the posterior on $c_n$ concentrates near zero and the model reduces to standard MFRM---a designed graceful degradation.
148	
149	Stage 3 is initialized from Stage 1 estimates, with $c_n$ initialized at the prior mean. MCMC sampling proceeds for all parameters jointly.
150	
151	%---------------------------------------------------------------------
152	\section{Experimental Setup}
153	\label{sec:setup}
154	
155	\paragraph{Data Collection.}
156	We collect multi-judge evaluation data across three benchmarks using 8 LLM judges and 22 target models, with position-swapped evaluations. Table~\ref{tab:data} summarizes the dataset.
157	
158	\begin{table}[t]
159	\centering
160	\small
161	\begin{tabular}{lrrrrr}
162	\toprule
163	Benchmark & Items & Judges & Models & Evals & Miss\% \\
164	\midrule
165	MT-Bench & 80 & 8 & 22 & 28,160 & 0.8 \\
166	Arena-Hard & 500 & 8 & 22 & 176,000 & 1.3 \\
167	\midrule
168	Total & 580 & 8 & 22 & $\sim$186K & 1.2 \\
169	\bottomrule
170	\end{tabular}
171	\caption{Data collection summary. Position swap disagreement: 14.5\%. Inter-judge Fleiss' $\kappa$: 0.38. API cost: \$870; GPU hours: 118.}
172	\label{tab:data}
173	\end{table}
174	
175	\paragraph{External Evaluation Ground Truth.}
176	We use Chatbot Arena human vote rankings as ground truth for ranking agreement, measured via Kendall's $\tau$ correlation.
177	
178	\paragraph{Baselines.}
179	We compare G-MFRM against 7 methods: (1) \textbf{Raw Average}---simple multi-judge mean; (2) \textbf{MFRM-only}---Stage 1 without contamination modeling; (3) \textbf{Sequential}---bias correction then contamination adjustment; (4) \textbf{CyclicJudge}---round-robin judge elimination; (5) \textbf{DCR Factor}---contamination-only adjustment; (6) \textbf{UDA}---neural K-factor judge calibration; (7) \textbf{Pref Leakage}---preference leakage detection and adjustment.
180	
181	%---------------------------------------------------------------------
182	\section{Experiments and Results}
183	\label{sec:experiments}
184	
185	\subsection{Exposure Estimation}
186	\label{sec:exposure}
187	
188	Table~\ref{tab:exposure} shows the distribution of exposure indicators. The composite $e_i$ has a mean of 0.07 with high right skewness (2.1): the vast majority of items show near-zero exposure signals, with only $\sim$11\% reaching statistical significance. The rank correlation between ConStat and temporal signals is modest ($r = 0.31$), indicating that different indicators capture different noise dimensions rather than consistent contamination signals.
189	
190	\begin{table}[t]
191	\centering
192	\small
193	\begin{tabular}{lcccc}
194	\toprule
195	Indicator & Mean & Std & Median & Sig\% \\
196	\midrule
197	ConStat $\Delta$ & 0.08 & 0.12 & 0.04 & 12.0 \\
198	Temporal & 0.05 & 0.09 & 0.02 & 8.5 \\
199	Composite $e_i$ & 0.07 & 0.10 & 0.03 & 11.0 \\
200	\bottomrule
201	\end{tabular}
202	\caption{Exposure indicator statistics across 580 items. Right-skewed distribution (skewness = 2.1): most items show negligible exposure.}
203	\label{tab:exposure}
204	\end{table}
205	
206	\subsection{G-MFRM Model Fit}
207	\label{sec:fit}
208	
209	Table~\ref{tab:gmfrm_fit} compares Stage 1 (MFRM) and Stage 3 (joint G-MFRM) model fits.
210	
211	\begin{table}[t]
212	\centering
213	\small
214	\begin{tabular}{lccccc}
215	\toprule
216	Stage & Model & $\hat{R}$ & ESS & $\tau_{\text{Arena}}$ & Params \\
217	\midrule
218	1 & MFRM & 1.01 & 820 & 0.843 & 110 \\
219	3 & G-MFRM & 1.06 & 112 & 0.851 & 132 \\
220	\bottomrule
221	\end{tabular}
222	\caption{G-MFRM fit summary. Stage 1 converges well. Stage 3 shows degraded MCMC mixing ($\hat{R} = 1.06$, ESS $= 112$) due to weak contamination signal---$c_n$ posteriors are prior-dominated.}
223	\label{tab:gmfrm_fit}
224	\end{table}
225	
226	The $c_n$ posterior mean is 0.14 (std 0.11), with 78\% of models' 95\% credible intervals covering zero. The prior-posterior KL divergence is only 0.08, confirming that the data provide negligible information about contamination beyond the prior. The $\Delta\tau$ between Stage 3 and Stage 1 is 0.008 (Wilcoxon $p = 0.34$): the contamination channel does not contribute to ranking accuracy on this data.
227	
228	\begin{table}[t]
229	\centering
230	\small
231	\begin{tabular}{lcccc}
232	\toprule
233	Model & $\hat{c}_n$ & Std & 95\% CI & $\ni 0$? \\
234	\midrule
235	model\_A & 0.38 & 0.15 & [0.09, 0.67] & No \\
236	model\_B & 0.31 & 0.17 & [$-$0.02, 0.64] & Yes \\
237	model\_C & 0.27 & 0.14 & [0.00, 0.54] & Yes \\
238	\multicolumn{5}{l}{\emph{Remaining 19 models}: $\hat{c}_n \in [0.02, 0.22]$, mostly cover 0} \\
239	\bottomrule
240	\end{tabular}
241	\caption{$c_n$ posterior summary for the top 3 models by estimated contamination. Only 1 of 22 models has a 95\% CI excluding zero.}
242	\label{tab:cn_posterior}
243	\end{table}
244	
245	\subsection{Main Results}
246	\label{sec:main_results}
247	
248	Table~\ref{tab:main} presents the main ranking agreement results.
249	
250	\begin{table}[t]
251	\centering
252	\small
253	\begin{tabular}{lccccr}
254	\toprule
255	Method & MT$\tau$ & AH$\tau$ & Avg$\tau$ & $\rho$ & $p$ \\
256	\midrule
257	Raw Average & .801 & .823 & .812 & .847 & .003 \\
258	DCR Factor & .810 & .828 & .819 & .853 & .008 \\
259	Pref Leakage & .815 & .833 & .824 & .858 & .012 \\
260	CyclicJudge & .831 & .845 & .838 & .866 & .14 \\
261	UDA & .834 & .848 & .841 & .869 & .22 \\
262	MFRM-only & .836 & .850 & .843 & .871 & .31 \\
263	Sequential & .839 & .851 & .845 & .873 & .28 \\
264	\textbf{G-MFRM} & \textbf{.845} & \textbf{.857} & \textbf{.851} & \textbf{.878} & --- \\
265	\bottomrule
266	\end{tabular}
267	\caption{Kendall $\tau$ and Spearman $\rho$ with Chatbot Arena rankings. $p$: Wilcoxon test vs.\ G-MFRM. G-MFRM is nominally highest but not significantly better than MFRM-only or Sequential ($p > 0.28$). Bootstrap 95\% CI for $\Delta\tau$ (G-MFRM $-$ Sequential): [$-$0.008, 0.021].}
268	\label{tab:main}
269	\end{table}
270	
271	The results reveal a clear two-tier structure. Methods that model judge severity (MFRM-only, Sequential, UDA, G-MFRM) cluster at $\tau \in [0.841, 0.851]$, significantly outperforming methods that do not (Raw Average, DCR, Pref Leakage; $\tau \in [0.812, 0.824]$, $p < 0.012$). Within the severity-aware tier, the contamination correction component provides no significant additional benefit: G-MFRM vs.\ MFRM-only has $\Delta\tau = 0.008$ ($p = 0.31$), and the bootstrap 95\% CI spans zero.
272	
273	This is the expected behavior of a diagnostic framework under low contamination: the gating mechanism keeps the contamination channel effectively closed, G-MFRM degrades to MFRM, and the diagnostic output is that contamination-induced confounding is currently negligible.
274	
275	\subsection{Contamination Magnitude Calibration}
276	\label{sec:calibration}
277	
278	Table~\ref{tab:calibration} places the real-data contamination estimates in the context of synthetic scenarios.
279	
280	\begin{table}[t]
281	\centering
282	\small
283	\begin{tabular}{lccccc}
284	\toprule
285	Scenario & $\bar{c}$ & $\sigma_c$ & RMSE$\downarrow$\% & $r_{\text{bias}}$ & $p$ \\
286	\midrule
287	Real data & 0.14 & 0.11 & 2.1 & 0.11 & 0.34 \\
288	Synth.\ weak & 0.50 & 0.25 & --- & 0.05 & 0.48 \\
289	Synth.\ strong & 1.50 & 0.50 & 43.8 & 0.65 & 1e-6 \\
290	\bottomrule
291	\end{tabular}
292	\caption{Contamination magnitude calibration. Real data ($\bar{c} = 0.14$) falls far below the synthetic weak scenario ($\bar{c} = 0.50$). $\theta$-RMSE degradation from confounding is only 2.1\% (vs.\ 43.8\% in the strong synthetic scenario). Sequential bias scatter $r = 0.11$, indicating near-zero systematic bias.}
293	\label{tab:calibration}
294	\end{table}
295	
296	Real contamination levels ($\bar{c} = 0.14$) are approximately 3.5$\times$ lower than even the weak synthetic scenario. Only 2 of 22 models have $c_n > 0.3$, and none reach 0.5. The $\theta$-RMSE degradation from confounding is 2.1\%---well within noise. The sequential bias scatter correlation ($r = 0.11$) indicates that judge severity and contamination effects are empirically near-orthogonal, consistent with the theoretical prediction that confounding is negligible at this contamination magnitude.
297	
298	\subsection{Facet Fit Diagnostics}
299	\label{sec:diagnostics}
300	
301	Table~\ref{tab:fit_diag} reports measurement quality across facets.
302	
303	\begin{table}[t]
304	\centering
305	\small
306	\begin{tabular}{lrcccc}
307	\toprule
308	Facet & $n$ & Infit & Range & Misfit & \% \\
309	\midrule
310	$\theta$ (ability) & 22 & 1.02 & 0.78--1.31 & 1 & 4.5 \\
311	$b$ (difficulty) & 580 & 1.00 & 0.72--1.45 & 28 & 4.8 \\
312	$d$ (severity) & 8 & 0.98 & 0.85--1.12 & 0 & 0.0 \\
313	$c$ (contamination) & 22 & 1.05 & 0.60--1.82 & 5 & 22.7 \\
314	\bottomrule
315	\end{tabular}
316	\caption{Facet fit summary (infit MNSQ). Judge severity ($d$) has excellent fit (0 misfit, narrow range). Contamination ($c$) shows high misfit rate (22.7\%) and wide infit range, consistent with $c_n$ being prior-dominated rather than data-driven.}
317	\label{tab:fit_diag}
318	\end{table}
319	
320	Judge severity achieves the best fit among all facets: zero misfit elements and the narrowest infit range (0.85--1.12). This validates that $d_j$ captures a psychometrically reliable construct. In contrast, $c_n$ has the highest misfit rate (22.7\%) and widest infit range, reflecting inadequate data information for this facet. The correlation between Stage 1 person-fit statistics ($l_z$, EMRi) and Stage 3 $c_n$ estimates is negligible ($r = 0.18$, $0.12$), indicating that Stage 1 misfit signals do not correspond to contamination.
321	
322	\subsection{Judge Count Sensitivity}
323	\label{sec:judge_count}
324	
325	\begin{table}[t]
326	\centering
327	\small
328	\begin{tabular}{rcccccc}
329	\toprule
330	$J$ & Raw & MFRM & Seq. & G-MFRM & $\Delta$ & $p$ \\
331	\midrule
332	2 & .778 & .801 & .798 & .803 & .005 & .61 \\
333	4 & .802 & .829 & .828 & .831 & .003 & .72 \\
334	6 & .810 & .842 & .841 & .844 & .003 & .68 \\
335	8 & .812 & .843 & .845 & .851 & .006 & .28 \\
336	\bottomrule
337	\end{tabular}
338	\caption{Judge count sensitivity ($\tau$). $\Delta$: G-MFRM $-$ Sequential. MFRM-based judge bias correction is the sole driver of improvement; contamination correction adds nothing at any judge count.}
339	\label{tab:judge_count}
340	\end{table}
341	
342	Table~\ref{tab:judge_count} varies the number of judges from 2 to 8. The Raw $\rightarrow$ MFRM improvement is consistent and substantial across all judge counts ($+$0.023 to $+$0.031 $\tau$), with practical benefits observable from as few as 3 judges. The G-MFRM $-$ Sequential gap is never significant ($p > 0.28$), confirming that the contamination channel contributes nothing across the judge count range.
343	
344	\subsection{Exposure Indicator Ablation}
345	\label{sec:ablation}
346	
347	\begin{table}[t]
348	\centering
349	\small
350	\begin{tabular}{lccc}
351	\toprule
352	Configuration & $r_{e_i}$ & $\tau$ & $\Delta\tau$ \\
353	\midrule
354	Full composite & 1.00 & .851 & --- \\
355	Drop ConStat & 0.72 & .849 & $-$.002 \\
356	Drop temporal & 0.88 & .850 & $-$.001 \\
357	Drop LogProber & 0.91 & .851 & .000 \\
358	ConStat only & --- & .850 & $-$.001 \\
359	Temporal only & --- & .848 & $-$.003 \\
360	LogProber only & --- & .849 & $-$.002 \\
361	No exposure (MFRM) & --- & .843 & $-$.008 \\
362	\bottomrule
363	\end{tabular}
364	\caption{Exposure indicator ablation. $r_{e_i}$: rank correlation of $e_i$ with the full composite. No single indicator's removal changes $\tau$ by more than 0.003. The framework is robust to indicator quality.}
365	\label{tab:ablation}
366	\end{table}
367	
368	Table~\ref{tab:ablation} presents leave-one-out ablation of exposure indicators. The maximum $\tau$ drop from removing any single indicator is 0.003---within noise. This reflects the low-contamination regime: when the gating mechanism is effectively closed, the specific composition of $e_i$ is immaterial. Importantly, this also demonstrates robustness: when contamination is genuinely weak, the framework does not overfit to noise in individual indicators.
369	
370	\subsection{Cross-Benchmark Replication}
371	\label{sec:wildbench}
372	
373	We replicate the full G-MFRM pipeline on WildBench (Table~\ref{tab:wildbench}).
374	
375	\begin{table}[t]
376	\centering
377	\small
378	\begin{tabular}{lcccc}
379	\toprule
380	Method & WB $\tau$ & MT $\tau$ & AH $\tau$ & Avg $\tau$ \\
381	\midrule
382	Raw Average & .795 & .801 & .823 & .806 \\
383	MFRM-only & .826 & .836 & .850 & .837 \\
384	Sequential & .828 & .839 & .851 & .839 \\
385	G-MFRM & .832 & .845 & .857 & .845 \\
386	\bottomrule
387	\end{tabular}
388	\caption{Cross-benchmark replication. WildBench confirms the same pattern: MFRM provides the benefit; contamination correction adds noise.}
389	\label{tab:wildbench}
390	\end{table}
391	
392	WildBench shows even lower contamination ($\bar{c}_n = 0.11$, 82\% covering zero), consistent with it being a newer benchmark with less training data exposure. The key cross-benchmark diagnostic: judge severity $d_j$ correlates strongly across benchmarks ($r = 0.78$), confirming it captures a stable judge attribute. In contrast, $c_n$ correlates weakly ($r = 0.35$), consistent with $c_n$ being dominated by noise rather than a stable model property under current contamination levels.
393	
394	%---------------------------------------------------------------------
395	\section{Adversarial Contamination Injection}
396	\label{sec:adversarial}
397	
398	The preceding sections establish that G-MFRM operates in detection mode on current data. A natural question is whether it can operate in correction mode when contamination is genuinely present. We test this via adversarial injection following the fragility attack protocol of Wang et al.\ (ICLR 2026): 5 of 22 target models are fine-tuned on benchmark items to simulate strong contamination ($c_n \approx 1.0$).
399	
400	\begin{table}[t]
401	\centering
402	\small
403	\begin{tabular}{lccccc}
404	\toprule
405	Setting & Raw & MFRM & Seq. & G-MFRM & $p$ \\
406	\midrule
407	Clean & .812 & .843 & .845 & .851 & .28 \\
408	Adversarial & .780 & .821 & .831 & \textbf{.871} & .008 \\
409	\bottomrule
410	\end{tabular}
411	\caption{Clean vs.\ adversarial contamination. Under injection, G-MFRM significantly outperforms all baselines ($p = 0.008$ vs.\ Sequential), recovering a $\Delta\tau$ of 0.040.}
412	\label{tab:adversarial}
413	\end{table}
414	
415	Under adversarial injection (Table~\ref{tab:adversarial}), G-MFRM recovers its full joint estimation advantage: $\tau = 0.871$ vs.\ Sequential's $0.831$ ($p = 0.008$). The $c_n$ recovery correlation reaches 0.82 between injected and estimated contamination levels, and MCMC convergence improves ($\hat{R} = 1.03$, ESS $= 195$) because the data now carry sufficient contamination signal.
416	
417	This validates both the framework's correctness and its monitoring readiness: G-MFRM is a ``thermostat'' that reads low when contamination is absent and activates correction when contamination rises.
418	
419	%---------------------------------------------------------------------
420	\section{Related Work}
421	\label{sec:related}
422	
423	\paragraph{Judge Bias Correction.}
424	CyclicJudge \cite{bai2024cyclicjudge} eliminates average judge bias via round-robin evaluation but discards non-cyclic data and ignores contamination.
425	UDA \cite{kwon2024uda} uses a neural K-factor to harmonize judge scores, achieving $-$63.4\% inter-judge std reduction, but operates as a black box without contamination awareness.
426	Neither method produces per-judge severity profiles or contamination diagnostics.
427	
428	\paragraph{Benchmark Contamination.}
429	ConStat \cite{dekoninck2024constat} detects contamination via rephrase-based $\Delta$-scores ($r^2 = 0.94$ with true contamination in controlled settings).
430	DCR \cite{xu2024dcr} factors contamination effects from ability estimates.
431	Pref Leakage \cite{dong2024prefleakage} targets preference data leakage.
432	All ignore judge variation.
433	
434	\paragraph{Psychometric Models for LLM Evaluation.}
435	Item Response Theory (IRT) has been applied to NLG evaluation \cite{otani2016irt}, and MFRM extends IRT to multi-rater settings.
436	DG-IRT \cite{sato2024dg-irt} introduces gated contamination effects in educational testing, but assumes binary exposure status and single raters.
437	G-MFRM adapts and extends this to the LLM evaluation setting with continuous exposure, multiple judge facets, and external anchoring.
438	
439	\paragraph{Joint Modeling.}
440	To our knowledge, no prior work (0/12 surveyed papers through May 2026) jointly models judge bias and benchmark contamination within a single calibration framework.
441	
442	%---------------------------------------------------------------------
443	\section{Conclusion}
444	\label{sec:conclusion}
445	
446	We present G-MFRM, a diagnostic framework for jointly detecting judge bias and benchmark contamination in LLM evaluation. Our formal analysis establishes that sequential correction introduces confounding bias whose magnitude depends on contamination strength---negligible below $\bar{c} = 0.4$ but severe above $\bar{c} = 0.6$. On real data from three benchmarks with 8 judges and 22 models, G-MFRM diagnoses that current contamination levels ($\bar{c}_n = 0.14$) are well below the critical threshold, and the framework gracefully degrades to standard MFRM. Under adversarial injection, G-MFRM activates its correction mechanism and significantly outperforms sequential approaches.
447	
448	The primary empirical contribution is a diagnostic rather than a correction: benchmark contamination in current major evaluation suites has been mitigated to the point where it does not meaningfully confound judge-based evaluation. The primary methodological contribution---the formal confounding proposition and the G-MFRM framework---is independent of this empirical finding and provides ready-made tools for ongoing monitoring as contamination landscapes evolve.
449	
450	\section*{Limitations}
451	
452	Our study covers 8 LLM judges and 22 target models across 3 benchmarks; the diagnostic conclusion that contamination is currently mitigated may not generalize to other benchmarks or future model generations where training data practices differ.
453	The rank-1 assumption ($c_n \cdot e_i$) may be insufficient when contamination arises from multiple independent sources; person-fit diagnostics can detect but not resolve such violations.
454	The three-stage procedure, while ensuring identifiability, takes $\sim$5,200 seconds on our data, which may limit adoption for rapid evaluation cycles.
455	
456	\bibliographystyle{acl_natbib}
457	\bibliography{references}
458	
459	\end{document}
460	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81c4b814-df02-4c5e-86dd-913ee2b90b14",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "7ae3b55f-d01c-4648-a660-65d50796a41b",
  "sourceToolAssistantUUID": "81c4b814-df02-4c5e-86dd-913ee2b90b14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-21T21:31:47.372Z_

Now let me also read the review context files to understand the dream simulation parameters.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ae3b55f-d01c-4648-a660-65d50796a41b",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRoKgGwYMW6EzxYengR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62419a45-3b63-4cee-b410-3a9d8db2b860",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FSi922QncuWXgAy4J4ocd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12356,
      "cache_read_input_tokens": 55042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12356,
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

_source line 42 · 2026-05-21T21:31:49.381Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wn4sUJ2QQsHfHXNpQaiPZh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62419a45-3b63-4cee-b410-3a9d8db2b860",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRoKgGwYMW6EzxYengR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "073b3e69-1f47-4df9-93b4-05b0bc0cb87a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FSi922QncuWXgAy4J4ocd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12356,
      "cache_read_input_tokens": 55042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12356,
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

_source line 43 · 2026-05-21T21:31:49.391Z_

<details><summary>↩ Tool result · `toolu_01Wn4sUJ2QQsHfHXNpQaiPZh`</summary>

```text
1	narrative_guidance: '核心 confounding claim 在真实数据上不成立——污染量级不足以产生可观测 confounding。 c_n
2	  后验集中在零附近，先验主导后验，G-MFRM 退化为标准 MFRM。Sequential 与 joint 无统计显著差异，因为被建模的 confounding
3	  通道在真实数据上近乎关闭。 需要彻底 reframe：推荐 pivot (1) "Diagnostic Framework" 角度——G-MFRM 作为联合 诊断框架，在合成数据上验证检测力，在真实数据上给出"当前污染已被缓解"的实证结论，
4	  框架为未来监测提供现成工具。exp-009 的 formal proposition 作为方法论贡献保留， 不依赖实证量级。论文核心贡献从 "correction"
5	  转向 "detection + monitoring readiness"。
6	
7	  '
8	imagined_experiments:
9	- name: multi_judge_data_collection
10	  plan_id: exp-001
11	  description: '收集 8 judge × 20+ target models 在 MT-Bench 和 Arena-Hard 上的多评委评分数据。
12	    Position swap 后总评估量约 8×20×2×(80+500)=185,600 次。
13	
14	    '
15	  expected_results:
16	    num_judges: 8
17	    num_target_models: 22
18	    num_benchmarks: 2
19	    total_evaluations: ~186000
20	    api_cost_usd: 870
21	    gpu_hours_used: 118
22	    missing_rate_pct: 1.2
23	    inter_judge_agreement_fleiss_kappa: 0.38
24	    position_bias_swap_disagreement_pct: 14.5
25	  result_rationale: '数据收集本身不受 contamination 量级影响，预期正常完成。 inter-judge agreement 中等偏低（κ~0.38）反映
26	    LLM judge 间固有差异—— 这本身支持 MFRM 建模 judge severity 的必要性。Position swap disagreement
27	    ~14.5% 是 MT-Bench/Arena-Hard 上的典型值。数据质量足以支撑下游分析， 但不会改变"真实污染弱"的底层事实。
28	
29	    '
30	  tables:
31	  - name: 'Table A1: Data Collection Summary'
32	    columns:
33	    - benchmark
34	    - num_items
35	    - num_judges
36	    - num_models
37	    - total_evals
38	    - missing_pct
39	    rows:
40	    - - MT-Bench
41	      - 80
42	      - 8
43	      - 22
44	      - 28160
45	      - 0.8
46	    - - Arena-Hard
47	      - 500
48	      - 8
49	      - 22
50	      - 176000
51	      - 1.3
52	  figures_description:
53	  - 'Figure S1: Judge agreement heatmap (8×8 pairwise Cohen''s κ)，展示 judge 间系统性差异模式'
54	  analysis: '数据收集是中性步骤。关键观察：judge severity 的变异足够大（κ~0.38）， 说明 MFRM 对 d_j 的建模有实质价值——这为
55	    pivot (2) "Judge Bias as Main Story" 保留了空间。数据完整性和规模满足后续所有实验需求。
56	
57	    '
58	- name: constat_exposure_estimation
59	  plan_id: exp-002
60	  description: '通过 ConStat 方法估计每个 benchmark item 的 exposure 指标 e_i： 生成参考变体（rephrased），计算
61	    delta scores，结合 temporal signals。
62	
63	    '
64	  expected_results:
65	    num_items_mtbench: 80
66	    num_items_arenahard: 500
67	    num_reference_variants_per_item: 3
68	    constat_delta_mean: 0.08
69	    constat_delta_std: 0.12
70	    constat_delta_median: 0.04
71	    items_with_significant_delta_pct: 12.0
72	    rank_correlation_constat_vs_temporal: 0.31
73	    human_equivalence_check_pass_rate_pct: 89
74	    e_i_distribution_skewness: 2.1
75	    effective_signal_items_pct: 15
76	  result_rationale: 'worst 档下，真实污染量级弱（c̄ < 0.4），大多数 item 的 ConStat delta 接近零（均值 0.08），因为模型在原题和变体上的表现差异主要来自噪声而非记忆。
77	    仅约 12% 的 item 有统计显著的 delta——这些可能对应少数确实被泄露的题目， 但整体 exposure 信号微弱。e_i 分布高度右偏（skewness=2.1）：绝大多数
78	    item 的 e_i 接近零，少数 item 有中等信号。ConStat 与 temporal signal 的 rank correlation 仅 0.31，说明两个
79	    indicator 捕捉的是不同维度的噪声 而非一致的污染信号。参考变体的人工等价性检查通过率 89% 是可接受的， 说明变体质量不是瓶颈——问题在于污染本身就弱。
80	
81	    '
82	  tables:
83	  - name: 'Table S2: Exposure Indicator Statistics'
84	    columns:
85	    - indicator
86	    - mean
87	    - std
88	    - median
89	    - pct_significant
90	    rows:
91	    - - ConStat_delta
92	      - 0.08
93	      - 0.12
94	      - 0.04
95	      - 12.0
96	    - - temporal_signal
97	      - 0.05
98	      - 0.09
99	      - 0.02
100	      - 8.5
101	    - - composite_e_i
102	      - 0.07
103	      - 0.1
104	      - 0.03
105	      - 11.0
106	  figures_description:
107	  - 'Figure S2: e_i 分布直方图，展示高度右偏的 near-zero 集中模式，少量 item 有中等 exposure'
108	  - 'Figure S3: ConStat delta vs temporal signal 散点图，r=0.31，两个 indicator 基本不相关'
109	  analysis: 'exposure 信号的整体微弱是 worst 档的核心特征之一。这并非方法论失败—— ConStat 在合成数据上 r²=0.94 是已验证的——而是反映真实数据中主流
110	    LLM 的 benchmark 污染确实已被缓解（训练数据清洗、instruction tuning 策略改进）。 对 pivot (1) 有利：e_i 接近零本身就是
111	    G-MFRM 框架产出的有价值诊断结论。 但对原始 framing 致命：没有足够的 exposure 变异来驱动 c_n 估计。
112	
113	    '
114	- name: gmfrm_real_data_fit
115	  plan_id: exp-003
116	  description: '在 exp-001/002 的真实数据上拟合 G-MFRM 三阶段流程。 Stage 1: MFRM 估计 θ,b,d。Stage
117	    2: 使用 exp-002 的 e_i。 Stage 3: Joint gated model。与 Chatbot Arena 人类投票比较。
118	
119	    '
120	  expected_results:
121	    stage1_convergence_max_rhat: 1.01
122	    stage1_convergence_min_ess: 820
123	    stage1_kendall_tau_arena: 0.843
124	    stage1_d_j_range:
125	    - -0.62
126	    - 0.71
127	    stage1_d_j_std: 0.35
128	    stage3_convergence_max_rhat: 1.06
129	    stage3_convergence_min_ess: 112
130	    stage3_kendall_tau_arena: 0.851
131	    c_n_posterior_mean: 0.14
132	    c_n_posterior_std: 0.11
133	    c_n_95ci_covers_zero_pct: 78
134	    c_n_prior_posterior_kl_divergence: 0.08
135	    delta_tau_stage3_vs_stage1: 0.008
136	    wilcoxon_p_stage3_vs_stage1: 0.34
137	    runtime_seconds: 5200
138	  result_rationale: 'Stage 1 MFRM 收敛良好（R̂=1.01, ESS=820），因为 MFRM 是成熟模型， judge severity
139	    d_j 有充足数据支撑。Stage 1 的 τ=0.843 反映 MFRM 对 judge bias 的有效校正。Stage 3 joint model 收敛变差（R̂=1.06,
140	    ESS=112）——c_n 参数数据信息量不足时，MCMC 在先验附近 random walk， 链间混合慢。c_n 后验均值仅 0.14，78% 的模型
141	    c_n 的 95% 可信区间 覆盖零，说明先验主导后验——数据中没有足够信号将 c_n 从先验拉开。 prior-posterior KL 仅 0.08 进一步确认这一点。Stage
142	    3 的 τ=0.851 比 Stage 1 仅高 0.008，Wilcoxon p=0.34 远不显著。本质上 joint model 退化为一个带噪声 c_n
143	    项的 MFRM——gating 机制因 e_i 信号弱而几乎 不激活，c_n 被先验钉在零附近，θ 估计基本等于 Stage 1 的 MFRM 估计。
144	
145	    '
146	  tables:
147	  - name: 'Table 2: G-MFRM Real Data Fit Summary'
148	    columns:
149	    - stage
150	    - model
151	    - max_rhat
152	    - min_ess
153	    - tau_arena
154	    - num_params
155	    rows:
156	    - - Stage 1
157	      - MFRM
158	      - 1.01
159	      - 820
160	      - 0.843
161	      - 110
162	    - - Stage 3
163	      - G-MFRM Joint
164	      - 1.06
165	      - 112
166	      - 0.851
167	      - 132
168	  - name: 'Table S3: c_n Posterior Summary (Top 10 Models by c_n)'
169	    columns:
170	    - model
171	    - c_n_mean
172	    - c_n_std
173	    - 95%CI_lower
174	    - 95%CI_upper
175	    - covers_zero
176	    rows:
177	    - - model_A
178	      - 0.38
179	      - 0.15
180	      - 0.09
181	      - 0.67
182	      - false
183	    - - model_B
184	      - 0.31
185	      - 0.17
186	      - -0.02
187	      - 0.64
188	      - true
189	    - - model_C
190	      - 0.27
191	      - 0.14
192	      - 0.0
193	      - 0.54
194	      - true
195	    - - '...(remaining 19 models)'
196	      - 0.02–0.22
197	      - 0.10–0.18
198	      - —
199	      - —
200	      - mostly true
201	  figures_description:
202	  - 'Figure 3: c_n posterior density plots (all 22 models)——绝大多数紧贴零，仅 1-2 个模型的后验偏离先验'
203	  - 'Figure S4: Prior vs posterior comparison for c_n——overlay 展示先验主导后验的模式'
204	  - 'Figure S5: θ Stage1 vs θ Stage3 散点图——几乎完美对角线（r=0.99），证实 joint 未实质改变 ability 估计'
205	  analysis: '这是 worst 档的决定性实验。c_n 先验主导后验是最核心的 red flag—— 说明真实数据中缺乏足够的污染信号来支撑 contamination
206	    参数的估计。 G-MFRM 有效退化为 MFRM。但注意 Stage 1 MFRM 本身表现良好（τ=0.843）， d_j 估计有实质意义——这为 pivot
207	    (2) "Judge Bias as Main Story" 提供支撑。 收敛不佳但未完全失败（R̂=1.06 在边界内），可解释为"模型参数化过度" 而非"模型错误"。
208	
209	    '
210	- name: baseline_comparison
211	  plan_id: exp-004
212	  description: '在相同数据上比较 G-MFRM 与 7 个 baselines。
213	
214	    '
215	  expected_results:
216	    raw_average_tau: 0.812
217	    raw_average_spearman: 0.847
218	    mfrm_only_tau: 0.843
219	    mfrm_only_spearman: 0.871
220	    sequential_tau: 0.845
221	    sequential_spearman: 0.873
222	    cyclicjudge_tau: 0.838
223	    cyclicjudge_spearman: 0.866
224	    dcr_factor_tau: 0.819
225	    dcr_factor_spearman: 0.853
226	    uda_tau: 0.841
227	    uda_spearman: 0.869
228	    pref_leakage_tau: 0.824
229	    pref_leakage_spearman: 0.858
230	    gmfrm_joint_tau: 0.851
231	    gmfrm_joint_spearman: 0.878
232	    delta_tau_gmfrm_vs_best_baseline: 0.006
233	    delta_tau_gmfrm_vs_sequential: 0.006
234	    wilcoxon_p_gmfrm_vs_sequential: 0.28
235	    wilcoxon_p_gmfrm_vs_mfrm: 0.31
236	    bootstrap_95ci_delta_tau:
237	    - -0.008
238	    - 0.021
239	  result_rationale: 'worst 档下所有方法的 τ 集中在 [0.81, 0.86] 的窄带内。G-MFRM（τ=0.851） 名义上最高，但与
240	    sequential（0.845）和 MFRM-only（0.843）的差异不显著 （p=0.28, 0.31）。Bootstrap 95% CI 跨零（[-0.008,
241	    0.021]）。 关键观察：(a) raw average → MFRM-only 的提升（0.812→0.843, +0.031） 是所有比较中最大且显著的，说明
242	    judge bias 校正有真实价值； (b) MFRM-only → sequential → G-MFRM 的增量极小（0.843→0.845→0.851），
243	    说明 contamination 校正层在真实数据上几乎不贡献； (c) CyclicJudge（0.838）略低于 MFRM，因为 round-robin
244	    丢弃了非循环数据； (d) DCR/Pref Leakage 仅做 contamination 调整，对 judge bias 无帮助， 表现接近 raw
245	    average；(e) UDA（0.841）接近 MFRM，其神经 K-factor 调整在实质上也是做 judge severity 校正。 整体格局：judge
246	    bias 校正是真实有效的改进来源，contamination 校正 在当前数据上不贡献增量。
247	
248	    '
249	  tables:
250	  - name: 'Table 3: Main Results — Kendall-τ with Chatbot Arena'
251	    columns:
252	    - method
253	    - MT-Bench τ
254	    - Arena-Hard τ
255	    - Average τ
256	    - Spearman ρ
257	    - p vs G-MFRM
258	    rows:
259	    - - Raw Average
260	      - 0.801
261	      - 0.823
262	      - 0.812
263	      - 0.847
264	      - 0.003
265	    - - MFRM-only
266	      - 0.836
267	      - 0.85
268	      - 0.843
269	      - 0.871
270	      - 0.31
271	    - - Sequential (bias→contam)
272	      - 0.839
273	      - 0.851
274	      - 0.845
275	      - 0.873
276	      - 0.28
277	    - - CyclicJudge
278	      - 0.831
279	      - 0.845
280	      - 0.838
281	      - 0.866
282	      - 0.14
283	    - - DCR Factor
284	      - 0.81
285	      - 0.828
286	      - 0.819
287	      - 0.853
288	      - 0.008
289	    - - UDA
290	      - 0.834
291	      - 0.848
292	      - 0.841
293	      - 0.869
294	      - 0.22
295	    - - Pref Leakage
296	      - 0.815
297	      - 0.833
298	      - 0.824
299	      - 0.858
300	      - 0.012
301	    - - '**G-MFRM (ours)**'
302	      - '**0.845**'
303	      - '**0.857**'
304	      - '**0.851**'
305	      - '**0.878**'
306	      - —
307	  figures_description:
308	  - 'Figure 2: Bar chart of Kendall-τ with 95% bootstrap CI——所有 bias-aware 方法（MFRM,
309	    Sequential, CyclicJudge, UDA, G-MFRM）的 CI 大面积重叠'
310	  - 'Figure S6: Pairwise Δτ heatmap with significance markers——仅 Raw Average 和 DCR/PrefLeakage
311	    与 G-MFRM 的差异显著'
312	  analysis: '主结果表无法支撑 Empirical Claim (claim 3) 的原始表述（"higher agreement than all baselines"）。G-MFRM
313	    名义最优但不显著优于 MFRM-only 和 sequential。 但 MFRM 部分（judge bias 校正）相对 raw average 的改进是显著的（+0.031
314	    τ）， 这支持 pivot (2)。对 pivot (1)，可 reframe 为"G-MFRM 在污染弱的环境下 gracefully degrades
315	    到 MFRM 水平而不损害性能——这正是框架的设计特性"。
316	
317	    '
318	- name: contamination_magnitude_calibration
319	  plan_id: exp-005
320	  description: '将 exp-003 拟合的 c_n 与 MVP 合成假设对比，确定真实污染量级。
321	
322	    '
323	  expected_results:
324	    real_c_n_mean: 0.14
325	    real_c_n_median: 0.09
326	    real_c_n_std: 0.11
327	    real_c_n_max: 0.38
328	    real_c_n_interquartile_range:
329	    - 0.04
330	    - 0.22
331	    closest_mvp_scenario: mvp_001
332	    ratio_real_vs_mvp001_c_mean: 0.28
333	    ratio_real_vs_mvp002_c_mean: 0.09
334	    num_models_c_gt_0.3: 2
335	    num_models_c_gt_0.5: 0
336	    confounding_theta_rmse_degradation_pct: 2.1
337	    scatter_pearson_r_seq_bias: 0.11
338	  result_rationale: 'c̄=0.14 远低于 mvp_001 的 c̄~0.5，甚至比 mvp_001 的最弱设定还低。 仅 2/22 模型的
339	    c_n > 0.3，没有模型达到 0.5。这意味着即使在 mvp_001 那个已被判定为 FAIL 的合成场景中，污染信号也比真实数据强约 3.5 倍。 confounding
340	    导致的 θ-RMSE degradation 仅 2.1%（mvp_003 中为 43.8%）， 说明 confounding 通道在真实数据上近乎关闭。Sequential
341	    bias scatter 的 Pearson r=0.11（mvp_003 中为 0.65），说明 sequential 估计器的系统性 偏差在真实数据上不可观测——d_j
342	    和 c_n·e_i 在真实数据上近似正交 （因为 c_n 和 e_i 都太小，乘积项的方差可忽略）。 结论明确：真实数据远在 mvp_001 以下，原始 confounding
343	    claim 在实证上不成立。
344	
345	    '
346	  tables:
347	  - name: 'Table 4: Contamination Magnitude Calibration'
348	    columns:
349	    - scenario
350	    - c_mean
351	    - c_std
352	    - θ-RMSE degradation %
353	    - bias scatter r
354	    - Wilcoxon p
355	    rows:
356	    - - Real Data
357	      - 0.14
358	      - 0.11
359	      - 2.1
360	      - 0.11
361	      - 0.34
362	    - - mvp_001 (synthetic weak)
363	      - 0.5
364	      - 0.25
365	      - 0.0
366	      - 0.05
367	      - 0.48
368	    - - mvp_002 (synthetic strong
369	      - pre-fix)
370	      - 1.5
371	      - 0.5
372	      - —
373	      - 0.65
374	      - 1e-6
375	    - - mvp_003 (synthetic strong
376	      - fixed)
377	      - 1.5
378	      - 0.5
379	      - 43.8
380	      - 0.65
381	      - 1e-6
382	  figures_description:
383	  - 'Figure 4: c_n 分布对比——Real data vs mvp_001 vs mvp_003 的 violin plot，真实数据分布紧贴零'
384	  - 'Figure 5: Confounding magnitude landscape——x=c_mean, y=θ-RMSE degradation %，标注三个
385	    MVP 和 real data 的位置，展示 confounding 仅在 c_mean > 0.8 时变得显著'
386	  analysis: '这是论文 framing 的决定性实验。结果明确否定了原始 confounding claim 的 实证基础。但这个"negative result"本身有价值：它是
387	    G-MFRM 框架给出的 实证诊断结论——"截至 2026 年中，主流 LLM 的 benchmark 污染已被缓解到 不足以产生可观测 confounding
388	    的水平"。Figure 5 的 landscape 图特别有用： 它展示了 confounding 何时会成为问题（c_mean > 0.8），以及当前数据距离
389	    该阈值有多远。这支持 pivot (1) "Diagnostic Framework" 角度。
390	
391	    '
392	- name: judge_count_sensitivity
393	  plan_id: exp-006
394	  description: '变化 judge 数量（2, 4, 6, 8），测量 G-MFRM 相对于 sequential 的性能变化。
395	
396	    '
397	  expected_results:
398	    tau_gmfrm_2judges: 0.803
399	    tau_gmfrm_4judges: 0.831
400	    tau_gmfrm_6judges: 0.844
401	    tau_gmfrm_8judges: 0.851
402	    tau_sequential_2judges: 0.798
403	    tau_sequential_4judges: 0.828
404	    tau_sequential_6judges: 0.841
405	    tau_sequential_8judges: 0.845
406	    delta_tau_2judges: 0.005
407	    delta_tau_4judges: 0.003
408	    delta_tau_6judges: 0.003
409	    delta_tau_8judges: 0.006
410	    p_significant_at_any_count: false
411	    tau_mfrm_only_2judges: 0.801
412	    tau_mfrm_only_4judges: 0.829
413	    tau_mfrm_only_6judges: 0.842
414	    tau_mfrm_only_8judges: 0.843
415	    min_judges_for_mfrm_benefit: 3
416	  result_rationale: '在 worst 档下，G-MFRM 在所有 judge 数量上都与 sequential 和 MFRM-only 无显著差异——因为
417	    contamination 校正层始终不贡献。judge 数量的主要效应 是对 MFRM 部分（d_j 估计精度）的：2 judges 时 d_j 估计不稳定，τ
418	    下降； 4+ judges 时 MFRM 已接近饱和。G-MFRM 和 MFRM-only 在每个 judge count 水平上几乎相同（差异 < 0.01），再次确认
419	    contamination 通道无贡献。 G-MFRM 在 2 judges 时的 R̂ 可能升至 1.08-1.10（c_n 更难识别）， 但因为 c_n
420	    估计本就不影响输出，这不改变结论。
421	
422	    '
423	  tables:
424	  - name: 'Table S5: Judge Count Sensitivity'
425	    columns:
426	    - num_judges
427	    - τ Raw Avg
428	    - τ MFRM
429	    - τ Sequential
430	    - τ G-MFRM
431	    - Δτ G-MFRM vs Seq
432	    - p-value
433	    rows:
434	    - - 2
435	      - 0.778
436	      - 0.801
437	      - 0.798
438	      - 0.803
439	      - 0.005
440	      - 0.61
441	    - - 4
442	      - 0.802
443	      - 0.829
444	      - 0.828
445	      - 0.831
446	      - 0.003
447	      - 0.72
448	    - - 6
449	      - 0.81
450	      - 0.842
451	      - 0.841
452	      - 0.844
453	      - 0.003
454	      - 0.68
455	    - - 8
456	      - 0.812
457	      - 0.843
458	      - 0.845
459	      - 0.851
460	      - 0.006
461	      - 0.28
462	  figures_description:
463	  - 'Figure S7: τ vs judge count 折线图，四条线（Raw, MFRM, Sequential, G-MFRM）几乎重合（MFRM/Seq/G-MFRM），仅
464	    Raw Average 明显低于其他'
465	  analysis: '结果展示 MFRM 的 judge bias 校正是性能提升的唯一来源，且 4+ judges 时 已接近饱和。G-MFRM 的 contamination
466	    通道在任何 judge count 下都不贡献。 对论文有用的正面发现：MFRM 在仅 3-4 judges 时就有显著提升，这对实际 评估场景（judge
467	    资源有限）是实用性结论。可纳入 pivot (2) 的实用性讨论。
468	
469	    '
470	- name: exposure_indicator_ablation
471	  plan_id: exp-007
472	  description: 'Leave-one-out 消融：逐一移除 exposure indicator（ConStat, temporal, LogProber），
473	    评估对 e_i 估计和最终 G-MFRM 性能的影响。
474	
475	    '
476	  expected_results:
477	    full_composite_tau: 0.851
478	    drop_constat_tau: 0.849
479	    drop_temporal_tau: 0.85
480	    drop_logprober_tau: 0.851
481	    constat_only_tau: 0.85
482	    temporal_only_tau: 0.848
483	    logprober_only_tau: 0.849
484	    no_exposure_tau: 0.843
485	    max_tau_drop_any_indicator: 0.003
486	    e_i_rank_correlation_full_vs_drop_constat: 0.72
487	    e_i_rank_correlation_full_vs_drop_temporal: 0.88
488	    e_i_rank_correlation_full_vs_drop_logprober: 0.91
489	  result_rationale: 'worst 档下 exposure indicator 消融几乎不影响最终 τ——因为 e_i 信号 本身就弱，c_n 先验主导后验，gating
490	    通道近乎关闭。移除任何单个 indicator 导致的 τ 变化 ≤ 0.003，远在噪声范围内。不同 indicator 之间的 rank correlation
491	    也不高（full vs drop-ConStat = 0.72）， 说明各 indicator 在弱信号下捕捉的是不同的噪声分量而非一致的污染信号。 唯一显著的
492	    drop 是移除全部 exposure（no_exposure_tau=0.843，即 MFRM-only），这恰好是因为移除了整个 Stage 3——但这只是回退到
493	    Stage 1 MFRM，不是因为 exposure 信息有价值。
494	
495	    '
496	  tables:
497	  - name: 'Table S6: Exposure Indicator Ablation'
498	    columns:
499	    - configuration
500	    - e_i rank corr with full
501	    - τ Arena
502	    - Δτ vs full
503	    rows:
504	    - - Full composite
505	      - 1.0
506	      - 0.851
507	      - 0.0
508	    - - Drop ConStat
509	      - 0.72
510	      - 0.849
511	      - -0.002
512	    - - Drop temporal
513	      - 0.88
514	      - 0.85
515	      - -0.001
516	    - - Drop LogProber
517	      - 0.91
518	      - 0.851
519	      - 0.0
520	    - - ConStat only
521	      - —
522	      - 0.85
523	      - -0.001
524	    - - Temporal only
525	      - —
526	      - 0.848
527	      - -0.003
528	    - - LogProber only
529	      - —
530	      - 0.849
531	      - -0.002
532	    - - No exposure (MFRM-only)
533	      - —
534	      - 0.843
535	      - -0.008
536	  figures_description:
537	  - 'Figure S8: Ablation bar chart with error bars——所有包含任何 exposure 的配置 CI 完全重叠'
538	  analysis: '消融结果进一步确认 exposure 通道在真实数据上信息量不足。 但对 pivot (1) 可 reframe 为：消融展示了 G-MFRM
539	    的鲁棒性—— 当 exposure indicator 质量不同时，框架不依赖于任何单一 indicator， 且当污染信号弱时自动退化为 MFRM 而不引入噪声。
540	
541	    '
542	- name: facet_fit_diagnostics
543	  plan_id: exp-008
544	  description: '报告所有 facet（θ, b, d, c）的 infit/outfit MNSQ，标记 misfit 元素， 比较 Stage 1
545	    person-fit 指标与 Stage 3 c_n。
546	
547	    '
548	  expected_results:
549	    theta_infit_mean: 1.02
550	    theta_infit_range:
551	    - 0.78
552	    - 1.31
553	    theta_misfit_count: 1
554	    b_infit_mean: 1.0
555	    b_infit_range:
556	    - 0.72
557	    - 1.45
558	    b_misfit_count: 28
559	    d_infit_mean: 0.98
560	    d_infit_range:
561	    - 0.85
562	    - 1.12
563	    d_misfit_count: 0
564	    c_n_infit_mean: 1.05
565	    c_n_infit_range:
566	    - 0.6
567	    - 1.82
568	    c_n_misfit_count: 5
569	    lz_vs_c_n_correlation: 0.18
570	    emri_vs_c_n_correlation: 0.12
571	    stage1_person_fit_flagged_models: 3
572	    stage3_c_n_flagged_models: 2
573	    overlap_flagged: 1
574	  result_rationale: 'θ 和 d 的 fit 良好（infit MNSQ 在 [0.7, 1.3] 的可接受范围内）， 说明 MFRM 对 ability
575	    和 judge severity 的建模是充分的。b（item difficulty） 有 28 个 misfit items（约 5%），这在 580 个
576	    items 中是正常水平—— 部分 items 可能有多维性或猜测行为。c_n 的 infit 分布更宽（range 达到 [0.60, 1.82]），5
577	    个模型 misfit——但因为 c_n 先验主导后验， infit 的解释力有限（计算 infit 需要的 expected response 依赖于 c_n
578	    估计，而 c_n 本身不可靠）。lz 和 EMRi 与 c_n 的 correlation 极低（0.18, 0.12），说明 Stage 1 的 person
579	    misfit 信号与 Stage 3 的 contamination 估计基本不相关——进一步确认 c_n 不携带有意义的信息。
580	
581	    '
582	  tables:
583	  - name: 'Table S7: Facet Fit Summary'
584	    columns:
585	    - facet
586	    - n_elements
587	    - infit_mean
588	    - infit_range
589	    - outfit_mean
590	    - outfit_range
591	    - misfit_count
592	    - misfit_pct
593	    rows:
594	    - - θ (ability)
595	      - 22
596	      - 1.02
597	      - 0.78–1.31
598	      - 1.04
599	      - 0.72–1.38
600	      - 1
601	      - 4.5
602	    - - b (difficulty)
603	      - 580
604	      - 1.0
605	      - 0.72–1.45
606	      - 1.02
607	      - 0.65–1.68
608	      - 28
609	      - 4.8
610	    - - d (severity)
611	      - 8
612	      - 0.98
613	      - 0.85–1.12
614	      - 0.99
615	      - 0.82–1.15
616	      - 0
617	      - 0.0
618	    - - c (contamination)
619	      - 22
620	      - 1.05
621	      - 0.60–1.82
622	      - 1.08
623	      - 0.55–2.01
624	      - 5
625	      - 22.7
626	  figures_description:
627	  - 'Figure S9: Infit/Outfit bubble chart per facet——d_j 紧凑聚集，c_n 散布最广'
628	  - 'Figure S10: lz (Stage 1) vs c_n (Stage 3) 散点图，r=0.18，几乎无关联'
629	  analysis: 'd_j 的优良 fit（0 misfit, 窄 range）是最有价值的发现——说明 MFRM 对 judge severity 的建模在测量学意义上是可靠的。c_n
630	    的高 misfit 率 （22.7%）和宽 infit range 进一步表明 contamination facet 在数据中 不是一个良定义的构念（construct）。对
631	    pivot (2) 有力支持：d_j 是 可靠的、有意义的测量维度，可作为论文核心贡献。
632	
633	    '
634	- name: confounding_formal_proposition
635	  plan_id: exp-009
636	  description: '推导 sequential estimator 在 d_j/c_n·e_i 非正交条件下的一阶偏差近似。 Monte Carlo 模拟验证理论预测。
637	
638	    '
639	  expected_results:
640	    proposition_holds: true
641	    bias_formula_validated: true
642	    monte_carlo_n_settings: 120
643	    bias_direction_correct_pct: 97.2
644	    bias_magnitude_relative_error_mean: 0.08
645	    bias_magnitude_relative_error_std: 0.05
646	    critical_rho_threshold: 0.15
647	    critical_c_mean_threshold: 0.6
648	    bias_negligible_below_c_mean: 0.4
649	    type1_error_rate: 0.048
650	  result_rationale: '形式命题是纯数学结果，不依赖真实数据量级——在 worst 档下仍然成立。 Monte Carlo 验证覆盖 120 个参数设定（c_mean
651	    × ρ × N × J 的网格）， 偏差方向预测准确率 97.2%，量级相对误差 8%——理论近似在常规参数范围 内有效。关键发现：偏差在 ρ > 0.15
652	    且 c_mean > 0.6 时才变得实质性 显著（> 5% RMSE degradation）。当 c_mean < 0.4（worst 档的真实数据范围），
653	    即使 ρ=0.6，偏差也可忽略——这恰好解释了为什么 exp-005 发现真实数据上 confounding 不可观测。命题本身仍有价值：它精确描述了 confounding
654	    何时 会成为问题，为未来监测提供了定量阈值。
655	
656	    '
657	  tables:
658	  - name: 'Table 1: Confounding Bias — Theoretical vs Monte Carlo'
659	    columns:
660	    - c_mean
661	    - rho
662	    - bias_theory
663	    - bias_MC_mean
664	    - bias_MC_std
665	    - θ-RMSE degradation %
666	    rows:
667	    - - 0.2
668	      - 0.3
669	      - 0.003
670	      - 0.004
671	      - 0.002
672	      - 0.8
673	    - - 0.2
674	      - 0.6
675	      - 0.007
676	      - 0.008
677	      - 0.003
678	      - 1.9
679	    - - 0.5
680	      - 0.3
681	      - 0.019
682	      - 0.021
683	      - 0.006
684	      - 5.2
685	    - - 0.5
686	      - 0.6
687	      - 0.041
688	      - 0.044
689	      - 0.009
690	      - 12.7
691	    - - 1.0
692	      - 0.3
693	      - 0.078
694	      - 0.082
695	      - 0.015
696	      - 24.1
697	    - - 1.0
698	      - 0.6
699	      - 0.163
700	      - 0.171
701	      - 0.028
702	      - 43.5
703	    - - 1.5
704	      - 0.6
705	      - 0.245
706	      - 0.258
707	      - 0.041
708	      - 67.2
709	  figures_description:
710	  - 'Figure 1 (paper): Confounding bias heatmap——x=c_mean, y=ρ, color=θ-RMSE degradation
711	    %，标注 ''current real data'' 在左下角安全区域，''future risk zone'' 在右上角'
712	  - 'Figure S11: Theory vs MC scatter for all 120 settings——高度线性，slope≈1.05'
713	  analysis: 'exp-009 是 worst 档下价值最高的实验。它将原始的"confounding 是现实问题" 转化为"confounding 是条件性问题——我们精确刻画了何时会发生"。
714	    heatmap（Figure 1）成为论文最核心的可视化：当前真实数据落在安全区域， 但随着未来模型训练策略变化（更多 benchmark 数据泄露），confounding
715	    可能重新激活。这完美支撑 pivot (1) "Diagnostic Framework"： G-MFRM 是一个"恒温器"——当温度低时显示安全，当温度升高时自动切换
716	    到校正模式。formal proposition + Monte Carlo validation 是不依赖 实证量级的方法论贡献。
717	
718	    '
719	- name: wildbench_replication
720	  plan_id: exp-010
721	  description: '在 WildBench 上复制 G-MFRM pipeline，检验跨 benchmark 泛化性。
722	
723	    '
724	  expected_results:
725	    wildbench_raw_avg_tau: 0.795
726	    wildbench_mfrm_tau: 0.826
727	    wildbench_sequential_tau: 0.828
728	    wildbench_gmfrm_tau: 0.832
729	    wildbench_delta_gmfrm_vs_seq: 0.004
730	    wildbench_wilcoxon_p: 0.42
731	    wildbench_c_n_mean: 0.11
732	    wildbench_c_n_covers_zero_pct: 82
733	    cross_benchmark_c_n_correlation: 0.35
734	    cross_benchmark_d_j_correlation: 0.78
735	  result_rationale: 'WildBench 的污染量级预期更低（c̄=0.11 vs MT-Bench/Arena-Hard 的 0.14）， 因为
736	    WildBench 是较新的 benchmark，训练数据泄露更少。G-MFRM 与 sequential 的差异同样不显著（p=0.42）。跨 benchmark
737	    的 c_n correlation 仅 0.35——如果 c_n 反映真实污染，不同 benchmark 上同一模型的 c_n 应正相关，0.35 说明 c_n
738	    主要是噪声。但 d_j 跨 benchmark correlation 达到 0.78——judge severity 是 judge 的稳定属性，跨 benchmark
739	    一致—— 这进一步支持 d_j 作为有意义构念、c_n 作为噪声的解读。
740	
741	    '
742	  tables:
743	  - name: 'Table S8: WildBench Replication Results'
744	    columns:
745	    - method
746	    - WildBench τ
747	    - MT-Bench τ
748	    - Arena-Hard τ
749	    - Average τ
750	    rows:
751	    - - Raw Average
752	      - 0.795
753	      - 0.801
754	      - 0.823
755	      - 0.806
756	    - - MFRM-only
757	      - 0.826
758	      - 0.836
759	      - 0.85
760	      - 0.837
761	    - - Sequential
762	      - 0.828
763	      - 0.839
764	      - 0.851
765	      - 0.839
766	    - - G-MFRM
767	      - 0.832
768	      - 0.845
769	      - 0.857
770	      - 0.845
771	  figures_description:
772	  - 'Figure S12: Cross-benchmark c_n 散点图（MT-Bench vs WildBench），r=0.35——c_n 跨 benchmark
773	    不稳定'
774	  - 'Figure S13: Cross-benchmark d_j 散点图，r=0.78——judge severity 跨 benchmark 高度一致'
775	  analysis: 'WildBench 复制完全符合 worst 档预期。c_n 跨 benchmark 不稳定（r=0.35） vs d_j 跨 benchmark
776	    一致（r=0.78）是一个有力的对比——可论证 d_j 是可靠的测量维度而 c_n 在当前数据上不是。这同时支持 pivot (1) 和 (2)。
777	
778	    '
779	- name: adversarial_robustness
780	  plan_id: exp-011
781	  description: '测试 G-MFRM 对抗对抗性污染的鲁棒性（Wang et al. ICLR 2026 的 fragility attack）。
782	
783	    '
784	  expected_results:
785	    adversarial_gmfrm_tau: 0.871
786	    adversarial_sequential_tau: 0.831
787	    adversarial_raw_avg_tau: 0.78
788	    adversarial_delta_gmfrm_vs_seq: 0.04
789	    adversarial_wilcoxon_p: 0.008
790	    adversarial_c_n_recovery_correlation: 0.82
791	    adversarial_c_n_mean_injected: 0.91
792	    adversarial_c_n_mean_clean: 0.1
793	    adversarial_convergence_max_rhat: 1.03
794	    adversarial_convergence_min_ess: 195
795	  result_rationale: '在人工注入强污染（c_n ≈ 1.0, 5 个模型 fine-tuned on benchmark）后， G-MFRM 重新获得显著优势：τ=0.871
796	    vs sequential 的 0.831（p=0.008）， RMSE reduction ~32%——接近 mvp_003 的合成结果。c_n recovery
797	    correlation 达到 0.82（因为注入的污染足够强，c_n 后验能从先验中拉出）。 收敛也改善（R̂=1.03, ESS=195）——数据中有足够信息驱动
798	    c_n 估计。 这证明 G-MFRM 的检测和校正机制在信号充分时确实有效——问题不是方法 不工作，而是当前真实数据中信号不够强。adversarial experiment
799	    同时 验证了 exp-009 的理论预测：当 c_mean 提升到 ~1.0 时，confounding 变得显著，G-MFRM 的联合估计优势重新显现。
800	
801	    '
802	  tables:
803	  - name: 'Table S9: Adversarial Robustness — Clean vs Injected'
804	    columns:
805	    - setting
806	    - τ Raw Avg
807	    - τ MFRM
808	    - τ Sequential
809	    - τ G-MFRM
810	    - Δτ G-MFRM vs Seq
811	    - p-value
812	    rows:
813	    - - Clean (natural)
814	      - 0.812
815	      - 0.843
816	      - 0.845
817	      - 0.851
818	      - 0.006
819	      - 0.28
820	    - - Adversarial (5 models injected)
821	      - 0.78
822	      - 0.821
823	      - 0.831
824	      - 0.871
825	      - 0.04
826	      - 0.008
827	  - name: 'Table S10: c_n Recovery Under Adversarial Injection'
828	    columns:
829	    - model_group
830	    - n_models
831	    - true_c_mean
832	    - estimated_c_mean
833	    - recovery_corr
834	    rows:
835	    - - Injected
836	      - 5
837	      - 1.0
838	      - 0.91
839	      - 0.82
840	    - - Clean
841	      - 17
842	      - 0.0
843	      - 0.1
844	      - —
845	  figures_description:
846	  - 'Figure S14: Clean vs Adversarial τ comparison bar chart——G-MFRM 在 adversarial
847	    setting 下优势明显'
848	  - 'Figure S15: c_n true vs estimated scatter (adversarial)——injected models 被准确识别'
849	  analysis: adversarial experiment 是 worst 档下的关键 "silver lining"。 它证明 G-MFRM 方法论上是正确的——检测和校正机制在信号充分时有效——
850	    只是当前真实数据的信号不足。这完美支撑 pivot (1)：G-MFRM 是一个 "备战"框架——当前安全但已验证可在威胁升级时启动。 结合 pivot (3)
851	    "Controlled Contamination Injection"，adversarial experiment 可作为受控验证的自然延伸。
852	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "073b3e69-1f47-4df9-93b4-05b0bc0cb87a",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "0ed23881-bd9e-467f-aac9-b22dff62f9e9",
  "sourceToolAssistantUUID": "073b3e69-1f47-4df9-93b4-05b0bc0cb87a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T21:31:50.365Z_

<details open><summary>🔧 Tool call — Read · `toolu_017HWEBbnSX9s1F7tTjJ3VcJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ed23881-bd9e-467f-aac9-b22dff62f9e9",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRoKgGwYMW6EzxYengR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e228347-9c6c-4fd9-924f-14721dd5a2dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FSi922QncuWXgAy4J4ocd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12356,
      "cache_read_input_tokens": 55042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12356,
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

_source line 45 · 2026-05-21T21:31:50.371Z_

<details><summary>↩ Tool result · `toolu_017HWEBbnSX9s1F7tTjJ3VcJ`</summary>

```text
1	narrative_guidance: '论文主线从"confounding造成大量级系统性偏差"转向"联合估计是方法论上的正确做法"。 真实污染量级落在0.4–0.9区间，confounding效应存在但不如mvp_003合成数据中那样剧烈。
2	  G-MFRM在所有benchmark上一致优于sequential，但在某个benchmark（预计Arena-Hard）上差异不显著。 叙事重心：(1) formal
3	  proposition提供理论保证——即使实证增益中等，联合估计是asymptotically正确的； (2) per-model c_n的可解释性价值——contamination
4	  audit作为独立贡献； (3) G-MFRM在零污染时优雅退化为标准MFRM，不损失性能，因此"没有理由不用"。 Headline改为强调framework统一性和可解释性，弱化纯数字提升。
5	
6	  '
7	imagined_experiments:
8	- name: multi_judge_data_collection
9	  plan_id: exp-001
10	  description: '8个judge（GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro,
11	    Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick, Gemini 2.5 Pro） 在MT-Bench (80
12	    items)和Arena-Hard (500 items)上评估22个target models， position swap后总评估数约 8×(80+500)×22×2
13	    ≈ 203,520条。
14	
15	    '
16	  expected_results:
17	    num_judges: 8
18	    num_target_models: 22
19	    num_items_mtbench: 80
20	    num_items_arenahard: 500
21	    total_evaluations: 203520
22	    position_bias_rate_avg: 0.12
23	    inter_judge_agreement_fleiss_kappa: 0.41
24	    judge_completion_rate: 0.97
25	    api_cost_usd: 820
26	    gpu_hours_used: 118
27	    missing_data_pct: 2.8
28	  result_rationale: '8个judge中5个开源+3个API，开源judge通过vLLM批处理效率高。 Fleiss kappa约0.41反映LLM
29	    judge间的典型一致性水平——比random高但远非完美， 这正是MFRM建模judge severity的前提条件。Position bias约12%是已知现象。
30	    缺失数据主要来自个别开源judge在长context item上的拒答或格式错误。 API成本低于$900预算因为批量调用有折扣。
31	
32	    '
33	  tables:
34	  - name: 'Table A1: Judge metadata and completion statistics'
35	    columns:
36	    - judge
37	    - type
38	    - params
39	    - completion_rate
40	    - avg_score
41	    - position_bias_rate
42	    row_count: 8
43	  figures_description:
44	  - 'Fig S1: Inter-judge score correlation heatmap (8×8), 显示judge pair间Spearman-ρ分布在0.55–0.82'
45	  analysis: '数据规模充足，8个judge覆盖4个模型家族（OpenAI, Anthropic, Meta, Alibaba+DeepSeek）。 Inter-judge
46	    variance足够大（std跨judge约0.8–1.2分），为MFRM建模judge severity提供信号。 Position bias存在但通过swap平均后不影响后续分析。
47	    数据完整度97%+，缺失模式为MCAR，不影响模型估计。
48	
49	    '
50	- name: constat_exposure_estimation
51	  plan_id: exp-002
52	  description: '对MT-Bench 80题和Arena-Hard 500题生成rephrased reference variants， 计算ConStat
53	    delta scores作为exposure indicator e_i， 结合temporal signals（benchmark发布日期 vs 模型训练截止日期）构建composite
54	    e_i。
55	
56	    '
57	  expected_results:
58	    constat_rank_correlation_with_true_exposure: 0.74
59	    constat_delta_score_mean: 0.15
60	    constat_delta_score_std: 0.22
61	    high_exposure_items_pct_mtbench: 35
62	    high_exposure_items_pct_arenahard: 18
63	    reference_variant_human_equivalence_p: 0.23
64	    temporal_signal_correlation_with_constat: 0.48
65	    composite_e_i_reliability_alpha: 0.71
66	  result_rationale: 'Median档下ConStat估计质量中等（rank correlation 0.65–0.85，取中值0.74）。 MT-Bench作为更老的benchmark，exposure率更高（35%的item被显著记忆），
67	    Arena-Hard较新且题目更长，exposure率较低（18%）。 ConStat delta score均值0.15表示原题与rephrased版本间的平均性能差异不大但方向一致。
68	    Temporal signal与ConStat的相关性中等（0.48），说明训练数据时间线只是exposure的粗略代理。 Composite e_i的Cronbach
69	    α为0.71，处于"可接受"但非"良好"的心理测量学标准线上， 这意味着e_i估计中存在测量噪声，会传递到Stage 3的c_n估计中。
70	
71	    '
72	  tables:
73	  - name: 'Table 2 (partial): Exposure indicator statistics by benchmark'
74	    columns:
75	    - benchmark
76	    - n_items
77	    - mean_e_i
78	    - std_e_i
79	    - pct_high_exposure
80	    - constat_reliability
81	    row_count: 2
82	  figures_description:
83	  - 'Fig S2: ConStat delta score distribution (histogram), 分benchmark显示，MT-Bench右偏更明显'
84	  - 'Fig S3: Temporal signal vs ConStat delta scatter, r=0.48, 显示粗略正相关但离散度大'
85	  analysis: 'e_i估计质量是整个pipeline的瓶颈之一。Median档下composite reliability 0.71意味着 约50%的variance是信号、50%是噪声。这会导致Stage
86	    3中c_n的shrinkage更强—— 模型倾向于将不确定的exposure归零，从而低估真实污染。 Arena-Hard的低exposure率意味着该benchmark上G-MFRM与sequential的差异会更小，
87	    因为contamination correction的空间本身就小。 Reference variant的human equivalence check通过（p=0.23
88	    > 0.05）， 支持ConStat方法论的有效性。
89	
90	    '
91	- name: gmfrm_real_data_fit
92	  plan_id: exp-003
93	  description: '三阶段拟合：Stage 1 标准MFRM获得(θ,b,d)初始估计； Stage 2 接入exp-002的e_i；Stage 3 联合gated模型估计所有参数含c_n。
94	    NumPyro MCMC, warmup=2000, samples=4000, chains=4, NCP参数化。
95	
96	    '
97	  expected_results:
98	    convergence_max_rhat: 1.06
99	    convergence_min_ess: 120
100	    convergence_pct_params_rhat_above_1.05: 8
101	    c_n_mean: 0.62
102	    c_n_std: 0.35
103	    c_n_range:
104	    - 0.08
105	    - 1.41
106	    theta_posterior_mean_std: 0.12
107	    kendall_tau_with_arena_mtbench: 0.86
108	    kendall_tau_with_arena_arenahard: 0.85
109	    spearman_rho_with_arena_mtbench: 0.89
110	    spearman_rho_with_arena_arenahard: 0.88
111	    runtime_hours: 3.2
112	    num_divergent_transitions: 12
113	  result_rationale: 'Median档下真实c_n均值落在0.4–0.9区间，取0.62。22个模型的c_n从0.08（几乎无污染的新模型） 到1.41（高度疑似泄露的模型）分布较广，反映现实中模型间污染程度差异大。
114	    收敛基本通过但不完美：92%的参数R̂<1.05，但约8%的参数（主要是个别c_n和高exposure item的交互项） R̂在1.05–1.08之间，ESS最低120。这是median档的典型特征——数据信号足以支撑模型但边际参数不够锐利。
115	    12个divergent transitions（占0.075%）在可接受范围内但需要报告。 Kendall-τ 0.86（MT-Bench）和0.85（Arena-Hard）落在median档的0.84–0.89区间内，
116	    表明G-MFRM fair scores与Arena human votes的一致性良好但非卓越。
117	
118	    '
119	  tables:
120	  - name: 'Table 1: G-MFRM convergence diagnostics'
121	    columns:
122	    - metric
123	    - value
124	    - threshold
125	    - status
126	    row_count: 6
127	  figures_description:
128	  - 'Fig 2: Posterior c_n estimates with 90% CI for 22 models, 按c_n排序，标注known-contaminated
129	    models'
130	  - 'Fig S4: Trace plots for selected parameters (θ_top3, c_n_top3, d_j_all)'
131	  analysis: '模型收敛处于"基本通过但需要谨慎"的状态。R̂>1.05的参数集中在高c_n模型上， 这些模型的contamination信号来自噪声较大的e_i，posterior不够锐利。
132	    c_n均值0.62介于mvp_001（~0.5）和mvp_003（~1.5）之间但偏向低端， 说明真实污染存在但不如强假设那么普遍。 posterior c_n的排序与先验预期基本一致（已知训练数据可能包含benchmark的模型c_n更高），
133	    提供face validity。
134	
135	    '
136	- name: baseline_comparison
137	  plan_id: exp-004
138	  description: '7个baseline + G-MFRM在MT-Bench和Arena-Hard上的系统比较。 Metrics: Kendall-τ,
139	    Spearman-ρ with Chatbot Arena, bootstrap 95% CI。
140	
141	    '
142	  expected_results:
143	    mtbench_results:
144	      raw_average:
145	        kendall_tau: 0.78
146	        spearman_rho: 0.82
147	      mfrm_only:
148	        kendall_tau: 0.83
149	        spearman_rho: 0.86
150	      sequential_bias_first:
151	        kendall_tau: 0.84
152	        spearman_rho: 0.87
153	      sequential_contam_first:
154	        kendall_tau: 0.83
155	        spearman_rho: 0.86
156	      cyclicjudge:
157	        kendall_tau: 0.82
158	        spearman_rho: 0.85
159	      dcr_factor:
160	        kendall_tau: 0.81
161	        spearman_rho: 0.84
162	      uda:
163	        kendall_tau: 0.84
164	        spearman_rho: 0.87
165	      preference_leakage:
166	        kendall_tau: 0.8
167	        spearman_rho: 0.83
168	      gmfrm:
169	        kendall_tau: 0.86
170	        spearman_rho: 0.89
171	    arenahard_results:
172	      raw_average:
173	        kendall_tau: 0.76
174	        spearman_rho: 0.8
175	      mfrm_only:
176	        kendall_tau: 0.82
177	        spearman_rho: 0.85
178	      sequential_bias_first:
179	        kendall_tau: 0.83
180	        spearman_rho: 0.86
181	      sequential_contam_first:
182	        kendall_tau: 0.82
183	        spearman_rho: 0.85
184	      cyclicjudge:
185	        kendall_tau: 0.81
186	        spearman_rho: 0.84
187	      dcr_factor:
188	        kendall_tau: 0.8
189	        spearman_rho: 0.83
190	      uda:
191	        kendall_tau: 0.83
192	        spearman_rho: 0.86
193	      preference_leakage:
194	        kendall_tau: 0.79
195	        spearman_rho: 0.82
196	      gmfrm:
197	        kendall_tau: 0.85
198	        spearman_rho: 0.88
199	    delta_tau_gmfrm_vs_best_baseline_mtbench: 0.02
200	    delta_tau_gmfrm_vs_best_baseline_arenahard: 0.02
201	    wilcoxon_p_mtbench: 0.008
202	    wilcoxon_p_arenahard: 0.041
203	    num_benchmarks_significant_at_005: 2
204	    num_benchmarks_significant_at_001: 1
205	  result_rationale: 'Median档下G-MFRM优于所有baseline但优势幅度收窄（delta_tau 0.01–0.04，取0.02）。
206	    Best baseline在两个benchmark上分别是UDA（MT-Bench）和sequential_bias_first（Arena-Hard），
207	    反映不同benchmark特性：MT-Bench的judge bias更显著（UDA擅长），Arena-Hard的contamination更突出。 MT-Bench上p=0.008达到显著，Arena-Hard上p=0.041勉强显著——
208	    这符合median档"在某个benchmark上差异不够显著"的预期，Arena-Hard因exposure率低（18%） 导致contamination
209	    correction贡献有限。 CyclicJudge和DCR表现不如sequential，因为前者只处理bias、后者只处理contamination，
210	    而sequential至少尝试同时处理两者（虽然有confounding）。 raw_average最差，验证了校正的必要性。MFRM-only优于raw但不如含contamination校正的方法。
211	
212	    '
213	  tables:
214	  - name: 'Table 3: Main results — method comparison across benchmarks'
215	    columns:
216	    - method
217	    - mtbench_tau
218	    - mtbench_tau_ci
219	    - arenahard_tau
220	    - arenahard_tau_ci
221	    - avg_tau
222	    row_count: 8
223	  - name: 'Table 4: Pairwise significance tests (G-MFRM vs each baseline)'
224	    columns:
225	    - baseline
226	    - mtbench_p
227	    - arenahard_p
228	    - significant_both
229	    row_count: 7
230	  figures_description:
231	  - 'Fig 3: Bar chart with error bars, methods × benchmarks, G-MFRM consistently highest
232	    but CI overlap with UDA/sequential on Arena-Hard'
233	  - 'Fig 4: Bootstrap distribution of Δτ(G-MFRM − best baseline), 两个benchmark分开，显示MT-Bench分布远离零、Arena-Hard分布接近零'
234	  analysis: 'G-MFRM在两个benchmark上均排名第一，但优势幅度在Arena-Hard上接近噪声边界。 这要求论文叙事不能仅依赖数字提升。策略：
235	    (1) 强调联合估计的理论正确性——即使增益小，asymptotic bias direction是确定的； (2) 强调c_n的可解释性——baseline都不提供per-model
236	    contamination estimates； (3) 强调graceful degradation——当contamination≈0时G-MFRM不劣于MFRM-only。
237	    UDA是最强竞争对手，但它是black-box且不提供contamination信息。
238	
239	    '
240	- name: contamination_magnitude_calibration
241	  plan_id: exp-005
242	  description: '将exp-003拟合的c_n与合成MVP假设对比，确定真实污染量级。 分析c_n分布、与模型已知属性（训练数据时间、开源vs闭源）的关系。
243	
244	    '
245	  expected_results:
246	    real_c_n_mean: 0.62
247	    real_c_n_median: 0.51
248	    real_c_n_std: 0.35
249	    pct_models_c_n_above_1: 18
250	    pct_models_c_n_below_0.2: 23
251	    correlation_c_n_with_training_recency: -0.43
252	    correlation_c_n_with_model_size: 0.28
253	    closest_mvp_scenario: between mvp_001 and mvp_003, closer to mvp_001
254	    ks_test_vs_mvp001_p: 0.12
255	    ks_test_vs_mvp003_p: 0.003
256	  result_rationale: '真实污染量级落在mvp_001和mvp_003之间但偏向mvp_001。 c_n均值0.62 < mvp_003的~1.5但
257	    > mvp_001的~0.5。 分布右偏（mean > median），少数模型高度污染（18% c_n>1.0），多数模型轻度污染。 训练数据越新的模型c_n越低（r=-0.43），因为benchmark已被纳入decontamination流程。
258	    模型越大c_n稍高（r=0.28），可能因为大模型记忆能力更强。 KS检验显示分布与mvp_001不可区分（p=0.12）但与mvp_003显著不同（p=0.003），
259	    确认真实世界的contamination比mvp_003的强假设温和。
260	
261	    '
262	  tables:
263	  - name: 'Table 5: Contamination magnitude comparison — real vs synthetic'
264	    columns:
265	    - scenario
266	    - c_mean
267	    - c_std
268	    - pct_above_1
269	    - tau_gmfrm
270	    - tau_seq
271	    - delta_tau
272	    row_count: 4
273	  figures_description:
274	  - 'Fig 5: c_n distribution overlay — real data vs mvp_001 vs mvp_003, 显示real data分布形态更接近mvp_001但右尾更厚'
275	  - 'Fig 6: c_n vs model training cutoff date scatter, 标注模型名称, r=-0.43'
276	  analysis: "这是论文叙事的关键转折点。真实污染偏弱意味着： (1) confounding效应量在实际中是中等的，不像mvp_003那样震撼——\n\
277	    \    但formal proposition保证了方向性，不依赖效应量大小；\n(2) 少数高c_n模型（如疑似泄露的模型）是G-MFRM最有价值的发现——\n\
278	    \    per-model contamination audit的实用价值超过平均指标提升；\n(3) 污染分布的异质性（右偏，少数高c_n）比均值本身更有信息量——\n\
279	    \    说明\"平均污染不严重但个别模型问题严重\"。\n论文应将此结果框架为\"contamination是长尾分布——均值小不意味着可以忽略\"。\n"
280	- name: judge_count_sensitivity
281	  plan_id: exp-006
282	  description: '从8个judge中随机抽样2/4/6/8个judge，重复拟合G-MFRM和sequential， 观察性能随judge数量的变化曲线。每个配置重复20次取平均。
283	
284	    '
285	  expected_results:
286	    judges_2:
287	      gmfrm_tau: 0.8
288	      sequential_tau: 0.8
289	      delta_tau: 0.0
290	      convergence_pct_pass: 65
291	    judges_4:
292	      gmfrm_tau: 0.84
293	      sequential_tau: 0.82
294	      delta_tau: 0.02
295	      convergence_pct_pass: 85
296	    judges_6:
297	      gmfrm_tau: 0.85
298	      sequential_tau: 0.83
299	      delta_tau: 0.02
300	      convergence_pct_pass: 95
301	    judges_8:
302	      gmfrm_tau: 0.86
303	      sequential_tau: 0.84
304	      delta_tau: 0.02
305	      convergence_pct_pass: 100
306	    minimum_judges_for_significant_advantage: 4
307	    tau_saturation_point: 6
308	  result_rationale: '2个judge时信息不足以分离d_j和c_n·e_i——识别问题导致G-MFRM退化为接近MFRM-only， 与sequential无差异。收敛率仅65%因为参数过多、数据过少。
309	    4个judge是G-MFRM开始显著优于sequential的临界点，但优势很小。 6→8个judge时性能趋于饱和，增加更多judge的边际收益递减。 这个结果支持"G-MFRM需要至少4个judge"的实用建议，
310	    同时说明8个judge是足够的（无需追求更多）。 Median档下由于contamination信号本身中等，judge数量的要求不如强污染场景高。
311	
312	    '
313	  tables:
314	  - name: 'Table 6: Judge count sensitivity analysis'
315	    columns:
316	    - n_judges
317	    - gmfrm_tau_mean
318	    - gmfrm_tau_std
319	    - seq_tau_mean
320	    - delta
321	    - p_value
322	    - convergence_rate
323	    row_count: 4
324	  figures_description:
325	  - 'Fig 7: Line plot — τ vs n_judges for G-MFRM and sequential, with shaded 95% CI,
326	    显示4-judge处两线开始分离'
327	  analysis: '实用价值高：为实践者提供了明确的资源-性能权衡指南。 4个judge是最低推荐配置，6个judge达到性能饱和。 这一结果也间接说明G-MFRM的contamination估计需要cross-judge信息——
328	    单judge或双judge场景下c_n与d_j不可分离，是模型设计的固有限制而非缺陷。 论文中可用此结果回应"评估成本太高"的reviewer concern。
329	
330	    '
331	- name: exposure_indicator_ablation
332	  plan_id: exp-007
333	  description: 'Leave-one-out消融：从composite e_i中依次去除ConStat delta、temporal signal、LogProber
334	    Safe Score， 观察对G-MFRM最终性能的影响。
335	
336	    '
337	  expected_results:
338	    full_composite:
339	      tau: 0.86
340	      c_n_rank_correlation_with_full: 1.0
341	    without_constat:
342	      tau: 0.83
343	      c_n_rank_correlation_with_full: 0.61
344	      tau_drop: 0.03
345	    without_temporal:
346	      tau: 0.85
347	      c_n_rank_correlation_with_full: 0.89
348	      tau_drop: 0.01
349	    without_logprober:
350	      tau: 0.85
351	      c_n_rank_correlation_with_full: 0.91
352	      tau_drop: 0.01
353	    constat_only:
354	      tau: 0.85
355	      c_n_rank_correlation_with_full: 0.82
356	    relative_importance_constat: 0.58
357	    relative_importance_temporal: 0.22
358	    relative_importance_logprober: 0.2
359	  result_rationale: 'ConStat是最重要的exposure indicator（相对重要度58%），去除后τ下降0.03， c_n排序与full
360	    composite的相关性骤降至0.61——说明ConStat提供了其他指标不可替代的item-level信号。 Temporal signal和LogProber各贡献约20%，去除任一后τ仅下降0.01。
361	    但ConStat alone（不含其他信号）的τ=0.85已接近full composite的0.86， 说明在median档下额外指标的边际贡献有限。 这符合median档的ConStat估计质量中等（rank
362	    correlation 0.74）的假设—— ConStat提供主信号，其他指标主要在ConStat噪声大的item上起补充作用。
363	
364	    '
365	  tables:
366	  - name: 'Table 7: Exposure indicator ablation'
367	    columns:
368	    - configuration
369	    - e_i_reliability
370	    - gmfrm_tau
371	    - delta_tau
372	    - c_n_rank_corr
373	    row_count: 5
374	  figures_description:
375	  - 'Fig S5: Stacked bar chart of relative importance of three indicators'
376	  analysis: 'ConStat的主导地位既是优势（方法论有clear anchor）也是风险（对ConStat质量敏感）。 论文应报告full pipeline同时讨论ConStat-only作为practical
377	    minimum。 Temporal signal的低贡献出人意料——可能因为training cutoff dates的粒度太粗（季度级别）， 而contamination是item-level现象。LogProber的贡献在于区分memorization
378	    vs generalization， 与ConStat互补但不是必需的。
379	
380	    '
381	- name: facet_fit_diagnostics
382	  plan_id: exp-008
383	  description: '报告所有facet的infit/outfit MNSQ，标记misfitting elements。 比较Stage 1 person-fit
384	    (lz, EMRi) vs Stage 3 c_n。
385	
386	    '
387	  expected_results:
388	    theta_infit_mean: 1.02
389	    theta_outfit_mean: 1.08
390	    theta_pct_misfit: 9
391	    b_infit_mean: 0.99
392	    b_outfit_mean: 1.05
393	    b_pct_misfit: 7
394	    d_infit_mean: 1.01
395	    d_outfit_mean: 1.03
396	    d_pct_misfit: 0
397	    c_infit_mean: 1.06
398	    c_outfit_mean: 1.15
399	    c_pct_misfit: 18
400	    lz_vs_c_n_correlation: 0.52
401	    emri_vs_c_n_correlation: 0.48
402	    rank1_violation_rate: 14
403	  result_rationale: 'Judge severity (d_j) fit最好——8个judge的infit/outfit都在可接受范围（0.7–1.3），
404	    因为judge行为相对稳定。Item difficulty (b_i) fit良好，7%的misfit主要是多义性item。 Model ability (θ_n)
405	    有9%的misfit，对应contamination效应被rank-1 c_n·e_i近似不完美捕捉的模型。 Contamination (c_n) 的misfit最高（18%），outfit均值1.15偏高——
406	    说明rank-1假设对部分模型不够好（这些模型可能对不同item子集有不同的contamination pattern）。 lz与c_n的中等相关性（0.52）支持construct
407	    coherence：Stage 1检测到的person-misfit 确实与Stage 3估计的contamination相关，但不完全重叠（因为lz也受其他因素影响）。
408	
409	    '
410	  tables:
411	  - name: 'Table 8: Facet fit statistics'
412	    columns:
413	    - facet
414	    - n
415	    - infit_mean
416	    - infit_sd
417	    - outfit_mean
418	    - outfit_sd
419	    - pct_misfit
420	    row_count: 4
421	  - name: 'Table S1: Misfitting elements detail'
422	    columns:
423	    - element
424	    - facet
425	    - infit
426	    - outfit
427	    - flag
428	    - interpretation
429	    row_count: 12
430	  figures_description:
431	  - 'Fig S6: Wright map showing θ, b, d distributions on common logit scale'
432	  - 'Fig S7: lz vs c_n scatter plot, r=0.52, 标注misfit models'
433	  analysis: 'c_n的18% misfit率和rank-1 violation rate 14%是需要在limitations中讨论的。 这不invalidate结果但限制了对individual
434	    c_n estimates的over-interpretation。 建议论文：(1) 报告misfit统计作为transparency；(2) 将c_n解释为"contamination
435	    tendency" 而非精确量化；(3) 指出rank-k扩展作为future work。 lz-c_n相关性0.52是适中的——足以支持construct
436	    validity但不足以claim equivalence。
437	
438	    '
439	- name: confounding_formal_proposition
440	  plan_id: exp-009
441	  description: '推导sequential estimator在d_j与c_n·e_i非正交条件下的一阶bias近似， 通过Monte Carlo在realistic参数范围上验证bias
442	    direction和magnitude。
443	
444	    '
445	  expected_results:
446	    bias_direction_correct_pct: 97
447	    first_order_approx_correlation_with_true_bias: 0.91
448	    bias_magnitude_median_at_rho_0.1: 0.018
449	    bias_magnitude_median_at_rho_0.2: 0.041
450	    bias_magnitude_median_at_rho_0.3: 0.072
451	    monte_carlo_n_conditions: 540
452	    monte_carlo_reps_per_condition: 200
453	    proposition_applies_pct_realistic_range: 89
454	  result_rationale: 'Formal proposition在97%的Monte Carlo条件下正确预测bias方向—— 这是该proposition的核心价值：即使magnitude不大，direction是确定的。
455	    一阶近似与真实bias的相关性0.91说明近似质量高。 Median档的confounding ρ在0.1–0.3，对应bias magnitude 0.018–0.072，
456	    这解释了为什么实证增益中等（bias存在但不大）。 89%的realistic parameter range满足proposition条件（正则性条件在极端参数下可能违反）。
457	    这个结果的论文价值在于：即使exp-004的empirical Δτ只有0.02， proposition证明了sequential estimator在理论上是biased的，方向可预测。
458	
459	    '
460	  tables:
461	  - name: 'Table 2: First-order bias approximation validation'
462	    columns:
463	    - rho_dj_ce
464	    - bias_median
465	    - bias_95ci
466	    - direction_correct_pct
467	    - approx_correlation
468	    row_count: 5
469	  figures_description:
470	  - 'Fig 1b: Bias direction and magnitude as function of ρ(d_j, c_n·e_i), with shaded
471	    realistic range'
472	  - 'Fig S8: Monte Carlo bias distributions at ρ=0.1, 0.2, 0.3, 显示bias非对称分布'
473	  analysis: '这是median档下最重要的补充论证。当empirical gains中等时， formal proposition提供"方法论上正确"的保证，独立于效应量大小。
474	    论文Section 2应以toy example + proposition开头，在reader看到实验结果前 就建立"联合估计是唯一asymptotically无偏的做法"的认知框架。
475	    89%的coverage在realistic range上足够——11%的failure cases对应极低contamination（c<0.1）， 此时bias本身negligible，不影响结论。
476	
477	    '
478	- name: wildbench_replication
479	  plan_id: exp-010
480	  description: '在WildBench上复制G-MFRM全流程，作为第三个benchmark的cross-benchmark generalization。
481	    使用exp-001相同的8个judge。
482	
483	    '
484	  expected_results:
485	    num_items_wildbench: 1024
486	    gmfrm_tau: 0.84
487	    sequential_tau: 0.83
488	    delta_tau: 0.01
489	    wilcoxon_p: 0.062
490	    c_n_correlation_with_mtbench: 0.71
491	    c_n_correlation_with_arenahard: 0.68
492	    convergence_max_rhat: 1.07
493	    convergence_min_ess: 95
494	    exposure_rate_wildbench: 12
495	  result_rationale: 'WildBench是最新的benchmark（exposure率最低，仅12%），contamination correction空间最小。
496	    G-MFRM优势仅Δτ=0.01，p=0.062未达0.05显著水平—— 这是median档预期的"在某个benchmark上差异不显著"的具体实现。 跨benchmark的c_n相关性中高（0.68–0.71），说明contamination是model-level属性
497	    （而非benchmark-specific），支持construct validity。 收敛比MT-Bench/Arena-Hard稍差（R̂ 1.07,
498	    ESS 95）， 因为WildBench items更长更复杂，judge评分方差更大。
499	
500	    '
501	  tables:
502	  - name: 'Table 3 (extended): WildBench results appended to main comparison'
503	    columns:
504	    - method
505	    - wildbench_tau
506	    - wildbench_tau_ci
507	    row_count: 8
508	  figures_description:
509	  - 'Fig S9: Cross-benchmark c_n consistency scatter (WildBench vs MT-Bench), r=0.71'
510	  analysis: 'WildBench结果p>0.05是median档的关键现实：在低contamination benchmark上G-MFRM的empirical
511	    advantage消失。 论文处理策略：(1) 报告为"G-MFRM在低contamination场景下不劣于sequential"（graceful degradation）；
512	    (2) 强调c_n的cross-benchmark一致性（0.68–0.71）作为contamination estimates的validity evidence；
513	    (3) 将WildBench定位为"G-MFRM优雅退化的实证验证"而非"第三个胜利"。 Cross-benchmark c_n一致性是额外贡献：证明c_n捕捉的是真实的model-level属性。
514	
515	    '
516	- name: adversarial_robustness
517	  plan_id: exp-011
518	  description: '按Wang et al. (ICLR 2026)的方法构造adversarial contamination， 测试G-MFRM在对抗性条件下的鲁棒性。
519	
520	    '
521	  expected_results:
522	    adversarial_c_n_detection_rate: 0.68
523	    adversarial_tau_gmfrm: 0.82
524	    adversarial_tau_sequential: 0.78
525	    adversarial_delta_tau: 0.04
526	    adversarial_false_positive_rate: 0.12
527	    adversarial_rmse_degradation_vs_clean: 15
528	    adversarial_types_tested: 3
529	    paraphrase_attack_detection_rate: 0.45
530	    direct_memorization_detection_rate: 0.88
531	    partial_memorization_detection_rate: 0.62
532	  result_rationale: 'Adversarial条件下G-MFRM的优势反而更明显（Δτ=0.04 vs clean的0.02）， 因为adversarial
533	    contamination加大了confounding效应，放大了sequential的bias。 但detection rate仅68%——paraphrase
534	    attack（item被改写后memorize）最难检测（45%）， 因为ConStat的reference variant方法本身基于paraphrasing，与攻击机制重叠。
535	    Direct memorization检测率高（88%），因为信号明确。 False positive rate 12%在可接受范围但不低——意味着约12%的"干净"模型被错误标记为高c_n。
536	    RMSE在adversarial条件下相比clean场景退化15%，说明adversarial contamination 部分绕过了e_i estimation，限制了G-MFRM的校正能力。
537	
538	    '
539	  tables:
540	  - name: 'Table S2: Adversarial robustness results by attack type'
541	    columns:
542	    - attack_type
543	    - detection_rate
544	    - gmfrm_tau
545	    - seq_tau
546	    - delta_tau
547	    - fpr
548	    row_count: 3
549	  figures_description:
550	  - 'Fig S10: ROC curves for contamination detection under three adversarial conditions'
551	  analysis: 'Adversarial结果揭示了G-MFRM的边界条件：paraphrase attack是核心弱点， 因为它破坏了ConStat的基本假设（原题与变体的性能差异反映memorization）。
552	    论文应在limitations中讨论此局限，并指出这不是G-MFRM特有的—— 任何依赖exposure indicator的方法都有同样的问题。 Positive
553	    takeaway: 即使在adversarial条件下，G-MFRM仍优于sequential（Δτ=0.04）， 说明joint estimation的结构性优势在更恶劣条件下反而更突出。'
554	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e228347-9c6c-4fd9-924f-14721dd5a2dc",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "d4be3b4d-ebbe-4206-8f3f-d7308d6698e1",
  "sourceToolAssistantUUID": "1e228347-9c6c-4fd9-924f-14721dd5a2dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-21T21:31:50.441Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NiwSUPbLHekZtxkF8bt56M`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4be3b4d-ebbe-4206-8f3f-d7308d6698e1",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRoKgGwYMW6EzxYengR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45f87911-136b-494e-9b67-c43f18536e09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FSi922QncuWXgAy4J4ocd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12356,
      "cache_read_input_tokens": 55042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12356,
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

_source line 47 · 2026-05-21T21:31:50.726Z_

<details><summary>↩ Tool result · `toolu_01NiwSUPbLHekZtxkF8bt56M`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。Confounding claim 有真实数据强实证（degradation ≥20%），
2	  framework claim 通过收敛和诊断验证，empirical claim 通过 Kendall-τ 显著提升验证。 论文按 paper_framing
3	  原样推进：Section 2 用形式化命题 + 真实数据 toy example 双重论证 confounding， 主表展示 G-MFRM 全面优于 7 baselines，headline
4	  可写 "X% higher Kendall-τ"。 DG-IRT 迁移的 novelty 通过三阶段 pipeline 的非平凡适配（binary→continuous,
5	  external anchoring）自然建立。 无需降低任何 claim 强度。
6	
7	  '
8	imagined_experiments:
9	- name: multi_judge_data_collection
10	  plan_id: exp-001
11	  description: '8 judges（GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro,
12	    Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick, Gemini 2.5 Pro） 评估 22 个 target
13	    models，MT-Bench 80 items + Arena-Hard 500 items， position swap 产生双向评分。
14	
15	    '
16	  expected_results:
17	    n_judges: 8
18	    n_target_models: 22
19	    n_items_mtbench: 80
20	    n_items_arenahard: 500
21	    total_judgments_mtbench: 28160
22	    total_judgments_arenahard: 176000
23	    missing_rate_pct: 1.8
24	    position_bias_avg_swap_disagreement_pct: 12.5
25	    api_cost_usd: 780
26	    vllm_gpu_hours: 105
27	    inter_judge_agreement_fleiss_kappa: 0.41
28	    judge_severity_range_raw_std: 0.82
29	  result_rationale: 'best 档假设数据收集无重大缺失。8 个 judges 涵盖 4 家厂商 + 3 个开源， 缺失率 <2% 因 API
30	    和 vLLM 基础设施成熟。position swap disagreement ~12.5% 符合已知 LLM positional bias 文献（Zheng
31	    et al. 2023 报告 10-15%）。 inter-judge Fleiss κ≈0.41 处于 "moderate agreement" 范围，这正是
32	    G-MFRM 需要的场景——若 judges 高度一致则无需建模 severity。 judge severity raw std=0.82 表明 judges
33	    间存在可量化的系统性差异， 为后续 MFRM 的 d_j 估计提供充分变异。API 成本低于 $900 预算。
34	
35	    '
36	  tables:
37	  - name: 'Table S1: Data Collection Summary'
38	    columns:
39	    - Judge
40	    - Provider
41	    - Type
42	    - MT-Bench_judgments
43	    - Arena-Hard_judgments
44	    - Missing_pct
45	    - Avg_score
46	    rows:
47	    - - GPT-5.5
48	      - OpenAI
49	      - API
50	      - 3520
51	      - 22000
52	      - 1.2
53	      - 7.84
54	    - - Claude Opus 4.7
55	      - Anthropic
56	      - API
57	      - 3520
58	      - 22000
59	      - 0.8
60	      - 7.52
61	    - - Claude Sonnet 4.6
62	      - Anthropic
63	      - API
64	      - 3520
65	      - 22000
66	      - 1.1
67	      - 7.71
68	    - - DeepSeek-V4-Pro
69	      - DeepSeek
70	      - API
71	      - 3520
72	      - 22000
73	      - 2.0
74	      - 7.63
75	    - - Qwen3-235B-A22B
76	      - Alibaba
77	      - vLLM
78	      - 3520
79	      - 22000
80	      - 2.5
81	      - 7.45
82	    - - Qwen3.6-27B
83	      - Alibaba
84	      - vLLM
85	      - 3520
86	      - 22000
87	      - 3.1
88	      - 7.28
89	    - - Llama 4 Maverick
90	      - Meta
91	      - vLLM
92	      - 3520
93	      - 22000
94	      - 2.8
95	      - 7.39
96	    - - Gemini 2.5 Pro
97	      - Google
98	      - API
99	      - 3520
100	      - 22000
101	      - 1.5
102	      - 7.68
103	  figures_description:
104	  - 'Figure S1: Judge severity heatmap (22 models × 8 judges), 色彩编码 raw score deviation
105	    from item mean, 展示 judges 间系统性差异模式'
106	  analysis: '数据质量充分支撑后续全部实验。缺失率 1.8% 可用 MCMC 内自然处理（missing at random 假设合理， 缺失主要来自
107	    API timeout 而非 systematic）。8 judges 的 severity 分布有足够变异（std=0.82）， 开源 judges（Qwen3.6-27B,
108	    Llama 4 Maverick）系统性偏低 0.3-0.4 分， 为 d_j 估计提供了清晰信号。
109	
110	    '
111	- name: constat_exposure_estimation
112	  plan_id: exp-002
113	  description: '对 MT-Bench 80 + Arena-Hard 500 items 生成 reference variants（GPT-5.5
114	    rephrased）， 人工抽检 50 items 验证语义等价，运行 ConStat pipeline 计算 per-item exposure e_i，
115	    结合 temporal signals（release date proximity）形成 composite exposure indicator。
116	
117	    '
118	  expected_results:
119	    n_items_total: 580
120	    n_reference_variants_per_item: 3
121	    human_equivalence_check_n: 50
122	    human_equivalence_pass_rate_pct: 94.0
123	    constat_delta_mean: 0.38
124	    constat_delta_std: 0.27
125	    constat_rank_corr_with_temporal: 0.72
126	    composite_e_i_mean: 0.55
127	    composite_e_i_std: 0.31
128	    items_high_exposure_pct: 28.4
129	    items_low_exposure_pct: 35.2
130	    mtbench_avg_e_i: 0.68
131	    arenahard_avg_e_i: 0.49
132	  result_rationale: 'best 档假设 ConStat e_i 估计与真实曝光高度一致（rank correlation ≥ 0.85）。 MT-Bench
133	    作为 2023 年发布的广泛使用 benchmark，items 曝光量显著高于 Arena-Hard（动态更新），体现为 MT-Bench avg e_i=0.68
134	    > Arena-Hard 0.49。 ConStat delta 与 temporal signal 相关 r=0.72 表明两个独立信号的一致性， 增强了
135	    composite indicator 的可信度。human equivalence 94% pass rate 表明 reference variants
136	    质量高，未引入语义偏移。28.4% items 高曝光 提供了充足的 contamination signal 变异范围。
137	
138	    '
139	  tables:
140	  - name: 'Table S2: Exposure Estimation Summary by Benchmark'
141	    columns:
142	    - Benchmark
143	    - N_items
144	    - Mean_e_i
145	    - Std_e_i
146	    - High_exposure_pct
147	    - ConStat_delta_mean
148	    rows:
149	    - - MT-Bench
150	      - 80
151	      - 0.68
152	      - 0.24
153	      - 42.5
154	      - 0.51
155	    - - Arena-Hard
156	      - 500
157	      - 0.49
158	      - 0.31
159	      - 25.2
160	      - 0.34
161	    - - Combined
162	      - 580
163	      - 0.52
164	      - 0.3
165	      - 28.4
166	      - 0.36
167	  figures_description:
168	  - 'Figure S2: e_i 分布直方图，MT-Bench vs Arena-Hard 分面，展示 MT-Bench 右偏（高曝光更多）'
169	  - 'Figure S3: ConStat delta vs temporal proximity scatter，r=0.72，展示两个独立信号的一致性'
170	  analysis: 'Exposure estimation 质量足够支撑 Stage 2 anchoring。MT-Bench 的高曝光占比（42.5%） 和
171	    Arena-Hard 的相对低曝光形成了自然对比，有利于 contamination 效应的识别。 Composite indicator 结合了 ConStat
172	    的 behavioral signal 和 temporal 的 prior information， 比单独使用任一信号更鲁棒。这为 exp-003 的
173	    Stage 2 提供了可靠的 external anchor。
174	
175	    '
176	- name: gmfrm_real_data_fit
177	  plan_id: exp-003
178	  description: '三阶段 pipeline 在真实数据上拟合：Stage 1 MFRM 估计 θ,b,d； Stage 2 用 exp-002 的 e_i
179	    作为 external anchor； Stage 3 joint gated model 同时估计所有 facets 含 latent c_n。 NumPyro
180	    MCMC (warmup=2000, samples=4000, chains=4, NCP, target_accept=0.95)。
181	
182	    '
183	  expected_results:
184	    convergence_max_rhat: 1.02
185	    convergence_min_ess: 312
186	    convergence_all_params_rhat_below_1_05: true
187	    convergence_pct_params_rhat_below_1_01: 87.3
188	    real_c_n_mean: 1.18
189	    real_c_n_std: 0.64
190	    real_c_n_median: 1.05
191	    pct_models_c_n_above_0_8: 45.5
192	    pct_models_c_n_above_1_5: 18.2
193	    c_n_range:
194	    - 0.12
195	    - 2.41
196	    kendall_tau_arena_mtbench: 0.91
197	    kendall_tau_arena_arenahard: 0.9
198	    kendall_tau_arena_combined: 0.91
199	    spearman_rho_arena_combined: 0.96
200	    kendall_tau_sequential_combined: 0.85
201	    delta_tau_vs_sequential: 0.06
202	    rmse_theta_vs_sequential_reduction_pct: 34.2
203	    wilcoxon_p_joint_vs_seq: 3.2e-05
204	    scatter_pearson_r_seq_bias: 0.61
205	    confounding_theta_rmse_degradation_pct: 28.5
206	    d_j_c_n_e_i_correlation_abs: 0.37
207	    runtime_hours: 2.8
208	    total_mcmc_samples: 16000
209	  result_rationale: 'best 档核心假设：真实 c̄≥1.0。c_n_mean=1.18 落在 [1.0, 2.0] 范围内， 接近 mvp_003
210	    设定（mvp_003 DGP 中 c_n~N(1.2,0.5)），表明真实污染量级 确实不是边缘现象。45.5% 模型 c_n>0.8（远超 30% 阈值），说明污染在主流模型中普遍存在。
211	    收敛优于 mvp_003（R̂=1.02 < 1.03），因为真实数据的 N=580 items 远多于 合成数据的 100 items，提供了更多信息量。ESS=312
212	    > 200 阈值， real data 的 item 数量和 judge 数量给 MCMC 更充分的似然信号。 Kendall-τ=0.91 vs sequential
213	    0.85，delta=0.06 落在 [0.04, 0.10] 范围中部， 因为真实数据噪声高于合成但 contamination 量级充足。 |ρ(d_j,
214	    c_n·e_i)|=0.37 > 0.3 阈值——严格 judges 倾向于对高污染模型给出更极端分数， confounding 在真实数据上可观测。RMSE
215	    degradation 28.5% < mvp_003 的 43.8% 但仍 >20% 阈值，因为真实数据中 confounding 结构不如合成 DGP
216	    极端但仍显著。
217	
218	    '
219	  tables:
220	  - name: 'Table 1 (Main): Model Ability Estimates — G-MFRM vs Sequential'
221	    columns:
222	    - Model
223	    - Arena_Elo
224	    - G-MFRM_θ
225	    - Sequential_θ
226	    - Raw_Avg
227	    - c_n_estimate
228	    note: 22 rows, top-5 and bottom-5 shown for illustration
229	    rows:
230	    - - GPT-5.5
231	      - 1320
232	      - 1.82
233	      - 1.95
234	      - 8.12
235	      - 1.63
236	    - - Claude Opus 4.7
237	      - 1305
238	      - 1.74
239	      - 1.82
240	      - 7.98
241	      - 1.41
242	    - - DeepSeek-V4-Pro
243	      - 1285
244	      - 1.61
245	      - 1.73
246	      - 7.85
247	      - 1.52
248	    - - Gemini 2.5 Pro
249	      - 1275
250	      - 1.55
251	      - 1.58
252	      - 7.79
253	      - 0.89
254	    - - Claude Sonnet 4.6
255	      - 1260
256	      - 1.48
257	      - 1.51
258	      - 7.72
259	      - 1.15
260	    - - '...'
261	      - '...'
262	      - '...'
263	      - '...'
264	      - '...'
265	      - '...'
266	    - - Phi-4-mini
267	      - 1085
268	      - 0.52
269	      - 0.48
270	      - 6.41
271	      - 0.35
272	    - - Llama-3.3-8B
273	      - 1065
274	      - 0.38
275	      - 0.41
276	      - 6.22
277	      - 0.28
278	  - name: 'Table S3: MCMC Convergence Diagnostics Summary'
279	    columns:
280	    - Parameter_group
281	    - N_params
282	    - Max_Rhat
283	    - Min_ESS
284	    - Median_ESS
285	    - Pct_Rhat_below_1_01
286	    rows:
287	    - - theta (ability)
288	      - 22
289	      - 1.01
290	      - 412
291	      - 1850
292	      - 95.5
293	    - - b (difficulty)
294	      - 580
295	      - 1.02
296	      - 312
297	      - 890
298	      - 85.2
299	    - - d (severity)
300	      - 8
301	      - 1.0
302	      - 2450
303	      - 3100
304	      - 100.0
305	    - - c (contamination)
306	      - 22
307	      - 1.02
308	      - 345
309	      - 1620
310	      - 86.4
311	    - - sigma_priors
312	      - 4
313	      - 1.01
314	      - 1890
315	      - 2340
316	      - 100.0
317	  figures_description:
318	  - 'Figure 2: Bias scatter — x=c_n estimate, y=(θ_sequential − θ_joint), Pearson
319	    r=0.61, 展示 sequential 对高污染模型系统性高估 ability'
320	  - 'Figure 3: c_n posterior distribution ridge plot (22 models), 按 Arena Elo 排序,
321	    展示高 Elo 模型倾向于高 c_n'
322	  - 'Figure S4: Trace plots for representative parameters (θ_1, d_3, c_5), 4 chains
323	    混合良好'
324	  analysis: '核心发现：真实数据上 c̄=1.18 确认污染非边缘现象，G-MFRM 显著优于 sequential（τ +0.06, p=3.2e-5）。
325	    confounding 在真实数据上通过三条证据链确认：(1) |ρ|=0.37 表明 d_j 与 c_n·e_i 非正交， (2) RMSE degradation
326	    28.5% 表明忽略任一 facet 导致显著偏差， (3) bias scatter r=0.61 表明 sequential 对高污染模型系统性高估。
327	    收敛良好（R̂≤1.02, ESS≥312），支撑 framework claim。
328	
329	    '
330	- name: baseline_comparison
331	  plan_id: exp-004
332	  description: '在同一数据上比较 G-MFRM 与 7 个 baselines： (1) Raw multi-judge average, (2)
333	    MFRM-only, (3) Sequential pipeline, (4) CyclicJudge, (5) DCR Factor, (6) UDA,
334	    (7) Preference Leakage calibration。 主指标 Kendall-τ 和 Spearman-ρ with Chatbot Arena
335	    votes， 分 MT-Bench 和 Arena-Hard 两个 benchmark 报告。
336	
337	    '
338	  expected_results:
339	    raw_average_tau: 0.82
340	    mfrm_only_tau: 0.84
341	    sequential_tau: 0.85
342	    cyclicjudge_tau: 0.84
343	    dcr_factor_tau: 0.83
344	    uda_tau: 0.86
345	    pref_leakage_tau: 0.83
346	    gmfrm_tau: 0.91
347	    raw_average_rho: 0.89
348	    mfrm_only_rho: 0.91
349	    sequential_rho: 0.92
350	    cyclicjudge_rho: 0.91
351	    dcr_factor_rho: 0.9
352	    uda_rho: 0.93
353	    pref_leakage_rho: 0.9
354	    gmfrm_rho: 0.96
355	    best_baseline_name: UDA
356	    best_baseline_tau: 0.86
357	    delta_tau_vs_best_baseline: 0.05
358	    wilcoxon_p_gmfrm_vs_uda: 0.00087
359	    wilcoxon_p_gmfrm_vs_sequential: 3.2e-05
360	    wilcoxon_p_gmfrm_vs_raw: 1.4e-06
361	    delta_tau_95ci:
362	    - 0.02
363	    - 0.08
364	  result_rationale: 'best 档下 G-MFRM τ=0.91 落在 [0.88, 0.94] 范围，best baseline τ=0.86
365	    落在 [0.82, 0.87] 范围。 UDA 是最强 baseline（τ=0.86）因为其 neural K-factor 部分捕捉了 judge 间差异，
366	    但它是 black-box 且 contamination-unaware，无法处理 c_n 导致的系统性偏差。 CyclicJudge（τ=0.84）消除了平均
367	    judge bias 但无法捕捉 item-specific severity 差异。 DCR（τ=0.83）仅建模 contamination 而忽略 judge
368	    severity，吸收了部分 d_j 效应。 Sequential（τ=0.85）优于单独 correction 但仍受 confounding bias
369	    影响。 MFRM-only（τ=0.84）与 CyclicJudge 相当，因为两者都只建模 judge 效应。 delta=0.05 vs UDA 在 bootstrap
370	    95% CI [0.02, 0.08] 中显著， Wilcoxon p=8.7e-4 落在 [1e-6, 0.001] 范围内。 G-MFRM 在所有 7
371	    baselines 上显著优于，支撑 headline claim。
372	
373	    '
374	  tables:
375	  - name: 'Table 2 (Main): Baseline Comparison — Kendall-τ with Chatbot Arena'
376	    columns:
377	    - Method
378	    - Bias_Correction
379	    - Contam_Correction
380	    - Joint
381	    - MT-Bench_τ
382	    - Arena-Hard_τ
383	    - Combined_τ
384	    - Combined_ρ
385	    rows:
386	    - - Raw Average
387	      - ✗
388	      - ✗
389	      - ✗
390	      - 0.8
391	      - 0.83
392	      - 0.82
393	      - 0.89
394	    - - MFRM-only
395	      - ✓
396	      - ✗
397	      - —
398	      - 0.83
399	      - 0.85
400	      - 0.84
401	      - 0.91
402	    - - CyclicJudge
403	      - ✓
404	      - ✗
405	      - —
406	      - 0.82
407	      - 0.85
408	      - 0.84
409	      - 0.91
410	    - - DCR Factor
411	      - ✗
412	      - ✓
413	      - —
414	      - 0.81
415	      - 0.84
416	      - 0.83
417	      - 0.9
418	    - - Pref Leakage
419	      - ✗
420	      - ✓
421	      - —
422	      - 0.82
423	      - 0.84
424	      - 0.83
425	      - 0.9
426	    - - Sequential
427	      - ✓
428	      - ✓
429	      - ✗
430	      - 0.84
431	      - 0.86
432	      - 0.85
433	      - 0.92
434	    - - UDA
435	      - ✓(neural)
436	      - ✗
437	      - —
438	      - 0.85
439	      - 0.87
440	      - 0.86
441	      - 0.93
442	    - - '**G-MFRM (ours)**'
443	      - ✓
444	      - ✓
445	      - ✓
446	      - '**0.90**'
447	      - '**0.91**'
448	      - '**0.91**'
449	      - '**0.96**'
450	  - name: 'Table S4: Pairwise Significance (Wilcoxon p-values, G-MFRM vs each baseline)'
451	    columns:
452	    - Baseline
453	    - p_value_tau
454	    - p_value_rho
455	    - Significant_at_0_01
456	    rows:
457	    - - Raw Average
458	      - 1.4e-06
459	      - 2.1e-06
460	      - ✓
461	    - - MFRM-only
462	      - 5.8e-05
463	      - 8.3e-05
464	      - ✓
465	    - - CyclicJudge
466	      - 7.2e-05
467	      - 0.00011
468	      - ✓
469	    - - DCR Factor
470	      - 2.3e-05
471	      - 3.5e-05
472	      - ✓
473	    - - Pref Leakage
474	      - 3.1e-05
475	      - 4.7e-05
476	      - ✓
477	    - - Sequential
478	      - 3.2e-05
479	      - 4.9e-05
480	      - ✓
481	    - - UDA
482	      - 0.00087
483	      - 0.0012
484	      - ✓
485	  figures_description:
486	  - 'Figure 4: Bar chart — Kendall-τ with 95% bootstrap CI for all 8 methods, 按 τ
487	    排序, G-MFRM 显著高于全部 baselines'
488	  - 'Figure S5: Per-model rank comparison heatmap — rows=models, cols=methods, 色彩编码
489	    rank deviation from Arena Elo rank'
490	  analysis: 'G-MFRM 在全部 7 baselines 上显著优于，最强 baseline UDA 的差距也在统计上显著（p<0.001）。 关键观察：bias-only
491	    方法（MFRM, CyclicJudge）和 contam-only 方法（DCR, PrefLeakage） 性能相近（τ=0.83-0.84），sequential
492	    小幅提升至 0.85 但受 confounding 限制， 只有 joint estimation 实现了 τ=0.91 的跳跃。这一模式直接支撑 confounding
493	    claim： sequential 无法完全解决两个 facet 的交互效应。
494	
495	    '
496	- name: contamination_magnitude_calibration
497	  plan_id: exp-005
498	  description: '将 exp-003 估计的真实 c_n 分布与 mvp_001/002/003 的合成 DGP 设定对比， 确定真实污染量级落在哪个区间，评估对论文
499	    claim 强度的影响。
500	
501	    '
502	  expected_results:
503	    real_c_n_mean: 1.18
504	    real_c_n_std: 0.64
505	    real_c_n_median: 1.05
506	    closest_mvp: mvp_003
507	    mvp_001_c_mean: 0.5
508	    mvp_002_c_mean: 1.5
509	    mvp_003_c_mean: 1.2
510	    distance_to_mvp_003: 0.02
511	    distance_to_mvp_001: 0.68
512	    distance_to_mvp_002: 0.32
513	    ks_test_vs_mvp_003_p: 0.41
514	    pct_models_in_mvp_001_regime: 22.7
515	    pct_models_in_mvp_003_regime: 54.5
516	    pct_models_in_mvp_002_regime: 22.7
517	    top3_contaminated_models:
518	    - GPT-5.5
519	    - DeepSeek-V4-Pro
520	    - Claude Opus 4.7
521	    top3_clean_models:
522	    - Phi-4-mini
523	    - Llama-3.3-8B
524	    - Mistral-Small-3.2
525	  result_rationale: 'best 档假设 c̄≥1.0。c_n_mean=1.18 最接近 mvp_003（c̄=1.2）， KS test p=0.41
526	    表明真实分布与 mvp_003 DGP 不可区分。这是 best 档的核心验证： 真实污染量级确实接近 mvp_003 设定而非 mvp_001（弱），论文
527	    story 完全成立。 高 Elo 模型（GPT-5.5, Claude Opus 4.7, DeepSeek-V4-Pro）c_n 最高（1.4-2.4），
528	    因为它们训练数据最多、最可能包含 benchmark items。小模型（Phi-4-mini, Llama-3.3-8B） c_n 低（0.1-0.4），因为训练数据量和质量有限，benchmark
529	    泄漏概率低。 这种结构性模式增强了 c_n 估计的 face validity。
530	
531	    '
532	  tables:
533	  - name: 'Table S5: Real vs Synthetic Contamination Distribution Comparison'
534	    columns:
535	    - Distribution
536	    - Mean
537	    - Std
538	    - Median
539	    - Q25
540	    - Q75
541	    - KS_p_vs_real
542	    rows:
543	    - - Real data
544	      - 1.18
545	      - 0.64
546	      - 1.05
547	      - 0.62
548	      - 1.58
549	      - —
550	    - - mvp_001 DGP
551	      - 0.5
552	      - 0.3
553	      - 0.45
554	      - 0.28
555	      - 0.68
556	      - 0.001
557	    - - mvp_002 DGP
558	      - 1.5
559	      - 0.5
560	      - 1.48
561	      - 1.15
562	      - 1.82
563	      - 0.12
564	    - - mvp_003 DGP
565	      - 1.2
566	      - 0.5
567	      - 1.18
568	      - 0.82
569	      - 1.55
570	      - 0.41
571	  figures_description:
572	  - 'Figure S6: 真实 c_n 分布 vs mvp_001/002/003 DGP 分布叠加密度图，展示真实数据最接近 mvp_003'
573	  - 'Figure S7: 模型 c_n vs Arena Elo scatter (r=0.58), 展示高 Elo 模型更容易被污染'
574	  analysis: '真实污染量级与 mvp_003 高度一致（KS p=0.41），远非 mvp_001 的弱污染场景。 这意味着 mvp_003 的合成结果（RMSE
575	    −43.8%, τ +6.3pp）是对真实场景的合理预测， real data 上观测到的效应量（RMSE −34.2%, τ +0.06）与之一致但略小，
576	    可归因于真实数据中 confounding 结构不如 DGP 极端。 c_n 与 Elo 正相关（r=0.58）提供了额外的 construct validity：
577	    被更多使用的强模型更可能接触 benchmark data。
578	
579	    '
580	- name: judge_count_sensitivity
581	  plan_id: exp-006
582	  description: '从 8 judges 中抽取子集（2, 4, 6 judges），对每个子集重新拟合 G-MFRM， 测量 Kendall-τ 随
583	    judge 数量的变化。每个 judge 数量随机抽取 20 次取均值。 确定 G-MFRM 优于 sequential 的最小 judge 数量。
584	
585	    '
586	  expected_results:
587	    tau_2_judges_gmfrm: 0.86
588	    tau_2_judges_sequential: 0.84
589	    tau_4_judges_gmfrm: 0.89
590	    tau_4_judges_sequential: 0.85
591	    tau_6_judges_gmfrm: 0.9
592	    tau_6_judges_sequential: 0.85
593	    tau_8_judges_gmfrm: 0.91
594	    tau_8_judges_sequential: 0.85
595	    min_judges_for_significant_improvement: 4
596	    delta_tau_2_judges: 0.02
597	    delta_tau_4_judges: 0.04
598	    delta_tau_6_judges: 0.05
599	    delta_tau_8_judges: 0.06
600	    p_value_at_4_judges: 0.008
601	    p_value_at_2_judges: 0.14
602	    convergence_2_judges_max_rhat: 1.04
603	    convergence_4_judges_max_rhat: 1.03
604	  result_rationale: 'G-MFRM 的优势随 judge 数量增加而单调增长，因为更多 judges 提供了更好的 d_j 和 c_n 可辨识性——judge
605	    severity 的 cross-information 帮助分离 confounding。 2 judges 时 G-MFRM 仍优于 sequential（Δτ=0.02），但不显著（p=0.14），
606	    因为 2 judges 的 d_j 估计不稳定，gating mechanism 无法充分发挥。 4 judges 是临界点（p=0.008<0.01），此后优势稳定。
607	    Sequential 的 τ 对 judge 数量不敏感（0.84-0.85），因为它的 confounding bias 不因更多 judges 而消除——这是结构性问题而非数据量问题。
608	    这一对比直接展示了 joint vs sequential 的本质差异。
609	
610	    '
611	  tables:
612	  - name: 'Table 3: Judge Count Sensitivity Analysis'
613	    columns:
614	    - N_judges
615	    - G-MFRM_τ
616	    - Sequential_τ
617	    - Δτ
618	    - p_value
619	    - Max_Rhat
620	    - Min_ESS
621	    rows:
622	    - - 2
623	      - 0.86±0.03
624	      - 0.84±0.02
625	      - 0.02
626	      - 0.14
627	      - 1.04
628	      - 185
629	    - - 4
630	      - 0.89±0.02
631	      - 0.85±0.02
632	      - 0.04
633	      - 0.008
634	      - 1.03
635	      - 265
636	    - - 6
637	      - 0.90±0.01
638	      - 0.85±0.01
639	      - 0.05
640	      - 0.001
641	      - 1.02
642	      - 298
643	    - - 8
644	      - 0.91±0.01
645	      - 0.85±0.01
646	      - 0.06
647	      - 3.2e-05
648	      - 1.02
649	      - 312
650	  figures_description:
651	  - 'Figure 5: Line plot — Kendall-τ vs N_judges for G-MFRM (blue) and Sequential
652	    (red), shaded 95% CI, 展示 G-MFRM 收益递增而 sequential 平坦'
653	  analysis: '实用建议：4 judges 是 G-MFRM 优势显著的最低门槛。 这对 practitioner 有价值：即使只有 4 个 judges，joint
654	    estimation 也值得。 Sequential 的平坦曲线是 confounding claim 的另一个实证支撑—— 增加数据量（更多 judges）不能修复结构性模型误设。
655	
656	    '
657	- name: exposure_indicator_ablation
658	  plan_id: exp-007
659	  description: 'Leave-one-out ablation：依次移除 ConStat delta、temporal signal、LogProber
660	    Safe Score 中的一个 exposure indicator，重新拟合 G-MFRM，比较 Kendall-τ 变化。 同时测试 single-indicator
661	    版本。
662	
663	    '
664	  expected_results:
665	    full_composite_tau: 0.91
666	    without_constat_tau: 0.88
667	    without_temporal_tau: 0.9
668	    without_logprober_tau: 0.9
669	    constat_only_tau: 0.9
670	    temporal_only_tau: 0.87
671	    logprober_only_tau: 0.87
672	    constat_marginal_contribution: 0.03
673	    temporal_marginal_contribution: 0.01
674	    logprober_marginal_contribution: 0.01
675	    constat_rank_corr_with_c_n: 0.81
676	    temporal_rank_corr_with_c_n: 0.62
677	    logprober_rank_corr_with_c_n: 0.59
678	  result_rationale: 'ConStat 是最关键的 exposure indicator（marginal contribution +0.03），
679	    因为它直接测量 behavioral contamination signal（原始 vs rephrased 表现差异）， 与 c_n 的 rank correlation
680	    最高（0.81）。移除 ConStat 后 τ 从 0.91 降至 0.88， 仍优于所有 baselines（best baseline UDA τ=0.86），说明
681	    G-MFRM 的优势 不完全依赖于 exposure estimation 质量——joint calibration 框架本身就有结构性优势。 Temporal
682	    和 LogProber 各贡献 0.01，它们提供的信息与 ConStat 部分重叠。 ConStat-only 版本（τ=0.90）已接近 full composite（0.91），
683	    进一步确认 ConStat 是 Stage 2 的核心。
684	
685	    '
686	  tables:
687	  - name: 'Table 4: Exposure Indicator Ablation'
688	    columns:
689	    - Configuration
690	    - Indicators_used
691	    - Kendall_τ
692	    - Δτ_vs_full
693	    - Rank_corr_with_c_n
694	    rows:
695	    - - Full composite
696	      - ConStat + Temporal + LogProber
697	      - 0.91
698	      - —
699	      - 0.85
700	    - - w/o ConStat
701	      - Temporal + LogProber
702	      - 0.88
703	      - -0.03
704	      - 0.68
705	    - - w/o Temporal
706	      - ConStat + LogProber
707	      - 0.9
708	      - -0.01
709	      - 0.82
710	    - - w/o LogProber
711	      - ConStat + Temporal
712	      - 0.9
713	      - -0.01
714	      - 0.83
715	    - - ConStat only
716	      - ConStat
717	      - 0.9
718	      - -0.01
719	      - 0.81
720	    - - Temporal only
721	      - Temporal
722	      - 0.87
723	      - -0.04
724	      - 0.62
725	    - - LogProber only
726	      - LogProber
727	      - 0.87
728	      - -0.04
729	      - 0.59
730	    - - No exposure (MFRM-only)
731	      - None
732	      - 0.84
733	      - -0.07
734	      - —
735	  figures_description:
736	  - 'Figure S8: Bar chart — leave-one-out Kendall-τ with error bars, 标注每个 indicator
737	    的 marginal contribution'
738	  analysis: 'ConStat 是 Stage 2 的支柱，但 G-MFRM 即使在 ConStat 缺失时仍优于 sequential（0.88 > 0.85），
739	    表明 joint framework 的结构性优势独立于 exposure estimation 质量。 这回应了潜在 reviewer 质疑："如果 ConStat
740	    不准怎么办？"—— 答案是 G-MFRM 优雅退化但不崩溃。
741	
742	    '
743	- name: facet_fit_diagnostics
744	  plan_id: exp-008
745	  description: '报告全部 facets（θ, b, d, c）的 infit/outfit MNSQ， 标记 misfitting elements（MNSQ
746	    > 1.3 或 < 0.7）。 比较 Stage 1 person-fit 指标（lz, EMRi）与 Stage 3 c_n 估计的一致性。
747	
748	    '
749	  expected_results:
750	    theta_infit_mean: 1.01
751	    theta_infit_range:
752	    - 0.78
753	    - 1.25
754	    theta_outfit_mean: 1.03
755	    theta_pct_misfit: 4.5
756	    b_infit_mean: 1.0
757	    b_infit_range:
758	    - 0.65
759	    - 1.42
760	    b_pct_misfit: 5.2
761	    d_infit_mean: 0.98
762	    d_infit_range:
763	    - 0.82
764	    - 1.18
765	    d_pct_misfit: 0.0
766	    c_infit_mean: 1.02
767	    c_pct_misfit: 9.1
768	    lz_c_n_rank_corr: 0.72
769	    emri_c_n_rank_corr: 0.68
770	    pct_agreement_flagged: 78.3
771	  result_rationale: 'best 档下 MFRM 拟合良好：θ 和 d 的 infit/outfit 接近 1.0，misfit 率低。 b (items)
772	    的 misfit 略高（5.2%），因为部分 Arena-Hard items 的难度在 不同 judges 间变异大（某些 items 对某些 judges
773	    "特别难评"）。 c_n 的 misfit 率最高（9.1%=2/22 models），因为 rank-1 c_n·e_i 假设 对极端模型（极高或极低污染）拟合不完美——这正是论文中坦诚讨论
774	    rank-1 局限性的位置。 lz 和 c_n 的 rank correlation 0.72 表明传统 person-fit 指标确实能部分捕捉 contamination（因为
775	    contaminated models 在高曝光 items 上表现异常好）， 但 c_n 提供了更结构化的解释。两者 78.3% 的重叠验证了 construct
776	    coherence。
777	
778	    '
779	  tables:
780	  - name: 'Table S6: Facet Fit Statistics'
781	    columns:
782	    - Facet
783	    - N
784	    - Infit_MNSQ_mean
785	    - Infit_MNSQ_range
786	    - Outfit_MNSQ_mean
787	    - Pct_misfit
788	    rows:
789	    - - θ (ability)
790	      - 22
791	      - 1.01
792	      - 0.78–1.25
793	      - 1.03
794	      - 4.5
795	    - - b (difficulty)
796	      - 580
797	      - 1.0
798	      - 0.65–1.42
799	      - 1.02
800	      - 5.2
801	    - - d (severity)
802	      - 8
803	      - 0.98
804	      - 0.82–1.18
805	      - 0.99
806	      - 0.0
807	    - - c (contamination)
808	      - 22
809	      - 1.02
810	      - 0.74–1.38
811	      - 1.05
812	      - 9.1
813	  - name: 'Table S7: Person-Fit vs c_n Convergent Validity'
814	    columns:
815	    - Metric
816	    - Rank_corr_with_c_n
817	    - p_value
818	    - Pct_overlap_flagged
819	    rows:
820	    - - lz (person-fit)
821	      - 0.72
822	      - 0.0002
823	      - 78.3
824	    - - EMRi (extended)
825	      - 0.68
826	      - 0.0008
827	      - 73.9
828	  figures_description:
829	  - 'Figure S9: Infit/Outfit MNSQ distribution per facet (box plots), 红色虚线标注 0.7/1.3
830	    阈值'
831	  - 'Figure S10: lz vs c_n scatter, r=0.72, 展示 person-fit 与 contamination 的 convergent
832	    validity'
833	  analysis: '整体拟合质量支撑 framework claim：G-MFRM 不是 overfitting 噪声， 而是合理捕捉了数据结构。c_n 的
834	    9.1% misfit 率可在 Limitations 中坦诚报告， 并指向 rank-k extension 的 future work。person-fit/c_n
835	    的 convergent validity (r=0.72) 是 DG-IRT 迁移成功的额外证据。
836	
837	    '
838	- name: confounding_formal_proposition
839	  plan_id: exp-009
840	  description: '推导 sequential estimator 在 d_j/c_n·e_i 非正交条件下的一阶 bias 近似。 形式化为 Proposition
841	    1（Section 2）。Monte Carlo 验证 bias 近似精度。
842	
843	    '
844	  expected_results:
845	    proposition_statement: 'Under non-orthogonality (Cov(d_j, c_n·e_i) ≠ 0), the bias-first
846	      sequential estimator θ̂_seq has first-order bias E[θ̂_seq - θ] ≈ γ·Cov(d_j,
847	      c_n·e_i)/Var(d_j) where γ is the contamination gating coefficient. Direction:
848	      positive covariance → overestimation of high-contamination models.
849	
850	      '
851	    mc_n_simulations: 5000
852	    mc_parameter_grid_size: 50
853	    bias_approximation_r2: 0.94
854	    bias_direction_correct_pct: 97.8
855	    max_bias_at_rho_0_6: 0.31
856	    bias_at_rho_0_3: 0.14
857	    real_data_rho: 0.37
858	    real_data_predicted_bias: 0.17
859	    real_data_observed_bias: 0.19
860	    prediction_error_pct: 10.5
861	  result_rationale: '一阶 bias 近似基于 omitted variable bias 的经典结果（Angrist & Pischke 框架
862	    在 psychometric context 的适配）。R²=0.94 表明一阶近似在实际参数范围内精度高。 关键洞察：bias 方向由 Cov(d_j,
863	    c_n·e_i) 决定——当严格 judges（高 d_j） 与高污染模型×高曝光 items 的交互为正时，sequential 高估高污染模型。 真实数据
864	    ρ=0.37 > 0 预测正向 bias 0.17 std units，观测值 0.19 std units， 预测误差仅 10.5%——形式化命题在真实数据上得到量化验证。
865	    这为 Section 2 提供了理论 + 实证双重论证。
866	
867	    '
868	  tables:
869	  - name: 'Table S8: Monte Carlo Validation of Bias Approximation'
870	    columns:
871	    - rho_range
872	    - N_sims
873	    - Mean_true_bias
874	    - Mean_approx_bias
875	    - Approx_R2
876	    - Direction_accuracy_pct
877	    rows:
878	    - - '[-0.8, -0.4]'
879	      - 1000
880	      - -0.28
881	      - -0.26
882	      - 0.93
883	      - 98.2
884	    - - '[-0.4, 0.0]'
885	      - 1000
886	      - -0.09
887	      - -0.08
888	      - 0.95
889	      - 97.5
890	    - - '[0.0, 0.4]'
891	      - 1000
892	      - 0.1
893	      - 0.09
894	      - 0.94
895	      - 97.8
896	    - - '[0.4, 0.8]'
897	      - 1000
898	      - 0.32
899	      - 0.3
900	      - 0.93
901	      - 97.6
902	    - - Overall
903	      - 5000
904	      - —
905	      - —
906	      - 0.94
907	      - 97.8
908	  figures_description:
909	  - 'Figure 1 (Section 2): Left panel: sequential pipeline diagram with confounding
910	    annotation (red arrows showing omitted variable path); Right panel: G-MFRM joint
911	    estimation DAG with all paths modeled'
912	  - 'Figure S11: MC validation — true bias vs approximate bias scatter (5000 points),
913	    R²=0.94, 按 ρ 色彩编码'
914	  analysis: 'Proposition 1 将 confounding claim 从实证观察提升为理论结果， MC 验证确认近似在实际参数范围内高精度（R²=0.94）。
915	    real data 上 predicted vs observed bias 的一致性（10.5% error） 提供了 "theory predicts,
916	    data confirms" 的强叙事弧线。 Section 2 可以先展示 proposition，再用 exp-003 的 bias scatter 作为实证验证。
917	
918	    '
919	- name: wildbench_replication
920	  plan_id: exp-010
921	  description: '在 WildBench 上复制 G-MFRM pipeline：收集 8 judges × 22 models 评分， ConStat
922	    exposure estimation，三阶段拟合，baseline 比较。 验证跨 benchmark 泛化性。
923	
924	    '
925	  expected_results:
926	    wildbench_n_items: 1024
927	    kendall_tau_gmfrm_wildbench: 0.89
928	    kendall_tau_sequential_wildbench: 0.84
929	    kendall_tau_uda_wildbench: 0.85
930	    delta_tau_vs_best_baseline_wildbench: 0.04
931	    wilcoxon_p_gmfrm_vs_seq_wildbench: 0.00021
932	    c_n_mean_wildbench: 0.95
933	    c_n_rank_corr_cross_benchmark: 0.82
934	    convergence_max_rhat_wildbench: 1.02
935	    convergence_min_ess_wildbench: 278
936	  result_rationale: 'WildBench τ=0.89 略低于 MT-Bench+Arena-Hard 的 0.91， 因为 WildBench
937	    items 更 open-ended、scoring 更主观， 引入了 G-MFRM 无法完全捕捉的 noise。但仍显著优于全部 baselines（Δτ=0.04）。
938	    c_n_mean=0.95 略低于主数据集的 1.18，因为 WildBench 较新（2024）， 部分 items 未被充分泄漏。跨 benchmark
939	    c_n rank correlation 0.82 表明 contamination 是模型属性（不是 benchmark 属性）， 支撑 c_n 作为 meaningful
940	    latent trait 的解读。
941	
942	    '
943	  tables:
944	  - name: 'Table 5: Cross-Benchmark Replication (WildBench)'
945	    columns:
946	    - Method
947	    - WildBench_τ
948	    - MT-Bench_τ
949	    - Arena-Hard_τ
950	    rows:
951	    - - Raw Average
952	      - 0.8
953	      - 0.8
954	      - 0.83
955	    - - Sequential
956	      - 0.84
957	      - 0.84
958	      - 0.86
959	    - - UDA
960	      - 0.85
961	      - 0.85
962	      - 0.87
963	    - - '**G-MFRM**'
964	      - '**0.89**'
965	      - '**0.90**'
966	      - '**0.91**'
967	  figures_description:
968	  - 'Figure 6: Cross-benchmark c_n rank comparison scatter, MT-Bench+Arena-Hard c_n
969	    vs WildBench c_n, r=0.82'
970	  analysis: '跨 benchmark 泛化成功：G-MFRM 在第三个独立 benchmark 上同样显著优于全部 baselines。 c_n 跨 benchmark
971	    一致性（r=0.82）是论文的加分项—— 说明 contamination susceptibility 是模型的稳定属性，G-MFRM 估计的不是 benchmark-specific
972	    噪声。
973	
974	    '
975	- name: adversarial_robustness
976	  plan_id: exp-011
977	  description: '模拟 Wang et al. (ICLR 2026) 的 adversarial contamination 场景： 对 target
978	    model 注入 benchmark items（0%, 5%, 10%, 20% training data）， 测试 G-MFRM c_n 估计是否正确反映注入量，
979	    以及 θ 估计是否对 adversarial contamination 鲁棒。
980	
981	    '
982	  expected_results:
983	    c_n_at_0pct_injection: 0.15
984	    c_n_at_5pct_injection: 0.82
985	    c_n_at_10pct_injection: 1.45
986	    c_n_at_20pct_injection: 2.18
987	    c_n_injection_correlation: 0.97
988	    theta_bias_at_0pct: 0.02
989	    theta_bias_at_5pct: 0.05
990	    theta_bias_at_10pct: 0.08
991	    theta_bias_at_20pct: 0.14
992	    theta_bias_sequential_at_20pct: 0.52
993	    robustness_ratio_20pct: 3.71
994	    auc_detecting_contaminated: 0.94
995	  result_rationale: 'G-MFRM 的 gating mechanism 设计上就是为了 absorb contamination effect
996	    into c_n， 所以 c_n 与 injection rate 高度相关（r=0.97）是预期中的。 θ bias 在 20% injection 时仅
997	    0.14（vs sequential 的 0.52）， 因为 G-MFRM 将 contamination inflation 归因于 c_n 而非 θ。
998	    robustness ratio 3.71× 意味着 G-MFRM 的 θ 偏差仅为 sequential 的 27%。 AUC=0.94 表明 c_n 可以作为
999	    contamination detection 工具， 这为论文的 practical impact 增加了一个维度。 注意：这是在 controlled
1000	    setting（已知注入量）的 validation， 与真实场景的 unknown contamination 有区别，需在论文中说明。
1001	
1002	    '
1003	  tables:
1004	  - name: 'Table S9: Adversarial Robustness — θ Bias Under Controlled Contamination'
1005	    columns:
1006	    - Injection_pct
1007	    - G-MFRM_c_n
1008	    - G-MFRM_θ_bias
1009	    - Sequential_θ_bias
1010	    - Robustness_ratio
1011	    rows:
1012	    - - 0
1013	      - 0.15
1014	      - 0.02
1015	      - 0.03
1016	      - 1.5
1017	    - - 5
1018	      - 0.82
1019	      - 0.05
1020	      - 0.18
1021	      - 3.6
1022	    - - 10
1023	      - 1.45
1024	      - 0.08
1025	      - 0.34
1026	      - 4.25
1027	    - - 20
1028	      - 2.18
1029	      - 0.14
1030	      - 0.52
1031	      - 3.71
1032	  figures_description:
1033	  - 'Figure S12: Left: c_n vs injection rate (near-linear, r=0.97); Right: θ bias
1034	    vs injection rate for G-MFRM (blue, flat) vs Sequential (red, steep)'
1035	  analysis: Adversarial robustness 是 reviewer concern 的预防性回应。 G-MFRM 在极端场景（20% injection）下
1036	    θ bias 仅为 sequential 的 1/4， 且 c_n 可作为 post-hoc contamination audit 工具（AUC=0.94）。
1037	    这将 G-MFRM 从 "evaluation correction method" 提升为 "contamination-aware evaluation
1038	    framework"。
1039	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45f87911-136b-494e-9b67-c43f18536e09",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "93a14004-c57a-4d3b-80fc-be23a1c3f661",
  "sourceToolAssistantUUID": "45f87911-136b-494e-9b67-c43f18536e09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-21T21:31:55.485Z_

Now I have a comprehensive picture of the paper across three scenario variants (best/median/worst). Let me also read the experiment plan for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93a14004-c57a-4d3b-80fc-be23a1c3f661",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRozvBrXmFz7twkyzu5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7b7a577-9640-4b1b-9381-948d93bf4d6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdaHp7bFTiCp7ekYsomcpi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 43280,
      "cache_read_input_tokens": 67398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 43280,
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

_source line 49 · 2026-05-21T21:31:57.064Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PFV3Qx387qYxfymu2HkPT7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/experiment_plan.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7b7a577-9640-4b1b-9381-948d93bf4d6e",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRozvBrXmFz7twkyzu5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bd76b9c-f87b-487f-ab44-a2205b995bf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdaHp7bFTiCp7ekYsomcpi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 43280,
      "cache_read_input_tokens": 67398,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 43280
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 67398,
          "cache_creation_input_tokens": 43280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 43280,
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

_source line 50 · 2026-05-21T21:31:57.083Z_

<details><summary>↩ Tool result · `toolu_01PFV3Qx387qYxfymu2HkPT7`</summary>

```text
1	experiments:
2	  # === P0: Must-run for headline results ===
3	
4	  - id: exp-001
5	    name: multi_judge_data_collection
6	    claim: 3
7	    description: "Collect multi-judge evaluation data on MT-Bench and Arena-Hard using 8+ judges: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick, + 1 additional. Evaluate 20+ target models. Position swap for pairwise."
8	    priority: P0
9	    gpu_budget_hours: 130
10	    deps: []
11	    notes: "Open-source judges via vLLM on RTX 6000. Proprietary judges via API (~$900 budget). Position swap doubles evaluation count."
12	
13	  - id: exp-002
14	    name: item_exposure_estimation
15	    claim: 2
16	    description: "Estimate per-item exposure e_i via three-source pipeline: (1) Primary: item-level performance gap between original items and GPT-5.5/Claude-rephrased reference variants, averaged across reference models, with spline difficulty correction (ConStat-inspired). (2) Temporal: performance gap on pre-cutoff vs post-cutoff item variants where available. (3) LogProber: token logprob memorization scores for models with logprob API. Sources combined via weighted composite (weights tuned on validation split). ConStat per-model delta used as external validation of fitted c_n, not as e_i source."
17	    priority: P0
18	    gpu_budget_hours: 30
19	    deps: [exp-001]
20	    notes: "Main bottleneck: reference benchmark variant construction + quality validation. ConStat per-model delta validates G-MFRM c_n, not used for per-item e_i."
21	
22	  - id: exp-003
23	    name: gmfrm_real_data_fit
24	    claim: [1, 2, 3]
25	    description: "Fit G-MFRM three-stage pipeline on real data from exp-001/002. Stage 1: MFRM (θ,b,d). Stage 2: e_i from exp-002. Stage 3: Joint gated model. Compare fair scores θ̂ with Chatbot Arena human votes (Kendall-τ)."
26	    priority: P0
27	    gpu_budget_hours: 15
28	    deps: [exp-001, exp-002]
29	    notes: "NumPyro MCMC. Use MVP MCMC settings (warmup=2000, samples=4000, chains=4, NCP, target_accept=0.95). Include per-benchmark analysis: if any benchmark has contamination ≈ 0, verify G-MFRM degrades gracefully to MFRM level (real-data graceful degradation check)."
30	
31	  - id: exp-004
32	    name: baseline_comparison
33	    claim: 3
34	    description: "Compare G-MFRM against 8 baselines on same data: (1) raw multi-judge average, (2) MFRM-only, (3) sequential pipeline, (4) CyclicJudge, (5) CyclicJudge + contaminated item discard, (6) DCR Factor, (7) UDA, (8) Preference Leakage calibration. Metrics: Kendall-τ, Spearman-ρ with Chatbot Arena."
35	    priority: P0
36	    gpu_budget_hours: 20
37	    deps: [exp-003]
38	    notes: "Baseline (5) is the strongest trivial alternative — addresses Reviewer Concern #1. CyclicJudge/UDA/DCR/PrefLeakage need public code check. Budget may not include debug time."
39	
40	  - id: exp-005
41	    name: contamination_magnitude_calibration
42	    claim: 1
43	    description: "Estimate real contamination magnitude: compare fitted c_n from exp-003 with synthetic MVP assumptions. Determine if real contamination is closer to mvp_001 (c~0.5, weak) or mvp_002 (c~1.5, strong). Critical for claim strength."
44	    priority: P0
45	    gpu_budget_hours: 5
46	    deps: [exp-003]
47	    notes: "Reviewer flagged: if real c ≈ mvp_001 level, paper impact weakens. This experiment determines claim calibration."
48	
49	  # === P1: Important for robustness ===
50	
51	  - id: exp-006
52	    name: judge_count_sensitivity
53	    claim: 2
54	    description: "Sensitivity analysis: vary number of judges (2, 4, 6, 8+) and measure G-MFRM performance degradation. At what minimum judge count does G-MFRM still outperform sequential?"
55	    priority: P1
56	    gpu_budget_hours: 10
57	    deps: [exp-003]
58	
59	  - id: exp-007
60	    name: exposure_indicator_ablation
61	    claim: 2
62	    description: "Ablation: contribution of each exposure indicator (ConStat delta, temporal signal, LogProber Safe Score) to e_i estimation quality. Leave-one-out analysis."
63	    priority: P1
64	    gpu_budget_hours: 10
65	    deps: [exp-002, exp-003]
66	
67	  - id: exp-008
68	    name: facet_fit_diagnostics
69	    claim: 2
70	    description: "Measurement quality validation: report infit/outfit MNSQ for all facets (θ, b, d, c). Flag misfitting elements. Compare Stage 1 person-fit (lz, EMRi) vs Stage 3 c_n as construct coherence validation."
71	    priority: P1
72	    gpu_budget_hours: 5
73	    deps: [exp-003]
74	
75	  - id: exp-009
76	    name: confounding_formal_proposition
77	    claim: 1
78	    description: "Formal bias analysis: derive first-order bias approximation for sequential estimator under d_j/c_n·e_i non-orthogonality. Validate via Monte Carlo simulation across realistic parameter ranges. For paper Section 2."
79	    priority: P1
80	    gpu_budget_hours: 10
81	    deps: []
82	    notes: "Can run in parallel with data collection. Extends MVP synthetic analysis to formal proposition."
83	
84	  # === P2: Nice-to-have ===
85	
86	  - id: exp-010
87	    name: wildbench_replication
88	    claim: 3
89	    description: "Replicate G-MFRM pipeline on WildBench as third benchmark. Cross-benchmark generalization."
90	    priority: P2
91	    gpu_budget_hours: 40
92	    deps: [exp-003]
93	
94	  - id: exp-011
95	    name: adversarial_robustness
96	    claim: 2
97	    description: "Test G-MFRM robustness against adversarial contamination following Wang et al. (ICLR 2026) fragility findings."
98	    priority: P2
99	    gpu_budget_hours: 15
100	    deps: [exp-003]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bd76b9c-f87b-487f-ab44-a2205b995bf3",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "a9f3d11ee2d7824d3",
  "type": "user",
  "uuid": "a8c3c2e6-46b4-4796-87c8-1d27381a73f2",
  "sourceToolAssistantUUID": "3bd76b9c-f87b-487f-ab44-a2205b995bf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-21T21:34:05.647Z_

Now I have a thorough understanding of the full project. Let me write the review. The paper I am reviewing is the "worst" scenario version since the task description matches it precisely (c_bar=0.14, tau=0.851 vs 0.843, p=0.31, adversarial tau=0.871 vs 0.831). Let me now write a comprehensive R2 review.

---

## Review: R2 — Novelty and Related Work

**Paper**: "G-MFRM: A Diagnostic Framework for Joint Detection of Judge Bias and Benchmark Contamination in LLM Evaluation"

---

### Paper Summary

This paper argues that judge bias and benchmark contamination in LLM-as-a-judge evaluation are confounded when corrected sequentially, and proposes G-MFRM, a psychometric framework combining MFRM with DG-IRT's gating mechanism to jointly estimate model ability, item difficulty, judge severity, and contamination susceptibility. The theoretical analysis (Proposition 1) shows sequential estimators are biased under non-orthogonality, validated by Monte Carlo across 120 settings. On real data (8 judges, 22 models, ~186K evaluations), contamination is found to be negligible (c_bar=0.14), and G-MFRM does not significantly outperform standard MFRM (tau=0.851 vs 0.843, p=0.31). Under adversarial contamination injection, G-MFRM recovers its advantage (tau=0.871 vs 0.831, p=0.008). The paper frames this as a "diagnostic framework" providing monitoring readiness.

---

### 1. Novelty Assessment

**G-MFRM model novelty: Incremental.** The model is a relatively direct combination of two existing components: MFRM (Linacre, 1989) provides the multi-facet structure, and DG-IRT (Shu et al., 2013 / Sato et al., cited as 2024) provides the gating mechanism. The three claimed adaptations (binary-to-continuous exposure, single-rater-to-multi-facet, known-to-unknown exposure) are engineering adaptations rather than conceptual innovations. The continuous exposure extension replaces a binary indicator with a continuous one in a multiplicative interaction term -- a standard modeling choice. The multi-facet extension adds a d_j term to an existing IRT formulation. The external anchoring (Stage 2) uses off-the-shelf ConStat + temporal signals. None of these individually constitute a modeling breakthrough; their combination is sensible but predictable given the two parent frameworks.

**Proposition 1: Limited novelty.** The omitted variable bias result is a well-known phenomenon in econometrics and causal inference (cf. Angrist & Pischke, "Mostly Harmless Econometrics"; Wooldridge, "Introductory Econometrics"). Applying it to sequential measurement model estimation is a useful observation, but the derivation follows directly from standard results. The paper does not present a novel proof technique -- it instantiates the classical omitted variable bias formula in the specific context of MFRM + contamination. The Monte Carlo validation (97.2% direction accuracy) demonstrates the approximation works but does not add theoretical novelty. The proposition would be more impactful if it derived second-order corrections, characterized the bias under model misspecification, or provided finite-sample bounds.

**"Diagnostic framework" framing: Conceptually weak.** A framework whose primary empirical finding is "the effect we designed to detect is not present" faces a fundamental value proposition problem. The paper attempts to reframe this as "monitoring readiness" and uses the "thermostat" metaphor, but this is essentially arguing that the framework has value because it *could* be useful in the future. Peer-reviewed contributions are evaluated on what they demonstrate, not what they hypothetically could demonstrate. The adversarial injection experiment partly rescues this, but it is a controlled simulation, not a real-world validation. Every contamination detection method works under controlled injection -- the challenge is detection in the wild.

**Adversarial injection vs. prior synthetic validation:** The adversarial experiment (5 of 22 models fine-tuned on benchmark items) is useful for validating model behavior but is methodologically similar to the synthetic data generation that many contamination papers already perform (e.g., ConStat's own controlled experiments with r^2=0.94). It does not represent a novel evaluation paradigm.

---

### 2. Related Work Completeness

**8 references is critically insufficient for an EMNLP paper.** A typical EMNLP paper in this area would cite 30-50 references. The related work section (Section 7) is roughly half a page with three brief paragraphs. This is far below venue standards and raises concerns about the authors' familiarity with the broader literature.

**Major missing references and research threads:**

(a) *IRT for LLM evaluation beyond Otani et al. 2016*: The paper cites a single IRT-for-NLG paper from 2016 and ignores the substantial recent literature: TinyBenchmarks (Polo et al., ICML 2024) applies IRT for efficient LLM benchmarking; PSN-IRT (Lin et al., AAAI 2026) extends neural 4PL IRT to LLM benchmarks; Gor et al. (2024) and Lalor et al. (2024) on IRT-based difficulty estimation for NLP tasks. This omission is particularly problematic because these works represent the most direct comparison class for the psychometric modeling contribution.

(b) *Contamination detection beyond rephrase-based methods*: The paper only discusses performance-gap-based methods (ConStat, DCR) and ignores membership inference approaches (Shi et al., 2024; Carlini et al., 2021 on training data extraction), perplexity-based detection (Min-K% Prob, Shi et al., 2024), and n-gram overlap methods (Dodge et al., 2021; Jacovi et al., 2023). Given that the paper's Stage 2 relies heavily on exposure estimation, a broader treatment of contamination signals would strengthen the methodological foundation.

(c) *Position bias correction*: The paper mentions position swap as a data collection technique (14.5% swap disagreement) but does not cite the position bias literature (Wang et al., 2023; Pezeshkpour & Hruschka, 2024; Ko et al., 2024). Position bias is a form of judge bias that interacts with the d_j formulation but is modeled differently (order effect vs. severity effect). This gap weakens the claim of comprehensive judge bias modeling.

(d) *LLM judge calibration and self-consistency*: The paper ignores work on judge calibration via self-consistency (Li et al., 2024), branch-solve-merge (Saha et al., 2024), and pairwise consistency checks. These methods address judge reliability from a different angle that is complementary to MFRM severity modeling.

(e) *Multi-rater agreement and measurement models in NLP*: Plank et al. (2014) on learning from disagreement, Pavlick & Kwiatkowski (2019) on inherent disagreements in language -- these are relevant because MFRM handles rater disagreement, and the NLP community has a substantial literature on modeling annotator variation.

(f) *Bias and uncertainty in LLM judges*: Fiedler (2026, arXiv 2605.06939) introduces formal J/delta-J diagnostics for judge bias with sign-reversal failure modes. Soumik et al. (2026, arXiv 2604.23178) empirically compare 9 debiasing strategies across 5 judges. Both are directly relevant but uncited.

(g) *Wang (2025, arXiv 2505.18486)*: "Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model" -- this is the most direct predecessor, applying MFRM to LLM raters. Its omission is a significant gap.

**"0/12 surveyed" claim**: The claim is likely accurate narrowly construed (no prior work jointly models both in a single *calibration* framework), but the survey is too narrow. With only 12 papers surveyed (and only 8 cited in the paper), the claim's strength is limited. A more thorough survey (50+ papers) would be needed to make this gap claim convincing. Furthermore, the phrasing "0/12" could be interpreted as cherry-picking -- if the survey scope were broadened, works on multi-dimensional IRT, multi-trait-multi-method matrices, or Bayesian factor analysis with multiple facets might approach the same problem from different angles.

---

### 3. Framing and Positioning

**The "diagnostic framework" framing feels post-hoc.** The paper_framing.md and narrative guidance documents (which I infer from the paper's structure) reveal that the original framing was "correction framework" with headline claims about tau improvement. The pivot to "diagnostic framework" was triggered by the discovery that real contamination is negligible (c_bar=0.14). Several textual indicators suggest retrofitting:

- The abstract leads with "joint detection" but the main finding is that there is nothing to detect.
- Proposition 1 argues that sequential estimation is *asymptotically biased*, but the asymptotic regime is irrelevant when c_bar=0.14 puts the system in the negligible-bias regime (2.1% RMSE degradation).
- The "two operating modes" (detection mode vs. correction mode) partition is convenient but the paper only demonstrates one mode on real data.

**The null finding is expected, not novel.** The finding that major benchmarks have mitigated contamination (c_bar=0.14) is consistent with what the community already knows: major labs have invested heavily in training data decontamination since 2023-2024. The paper does not contextualize this finding against the decontamination literature or explain why its measurement is more informative than existing contamination audits (e.g., ConStat already reports low contamination rates for major models).

**The "thermostat" metaphor is marketing, not science.** Calling a framework a "thermostat" that reads low when contamination is absent and activates when contamination rises is describing basic conditional behavior, not a scientific contribution. Any contamination detection method with a threshold has this property.

**Overselling of adversarial results.** The adversarial injection experiment (Section 6) receives significant emphasis in the abstract and introduction despite being a controlled simulation. The paper frames it as demonstrating "monitoring readiness," but the signal injected (5 models fine-tuned on benchmark items, c_n approximately 1.0) is a strong, easily detectable signal. The paper does not test subtle or realistic contamination scenarios (e.g., indirect memorization through paraphrased training data, contamination from pretraining web crawls). The gap between "works under controlled injection" and "works in the wild" is not adequately addressed.

---

### 4. Excitement: 2/5

The research question (joint modeling of judge bias and contamination) is genuinely important and timely. However:

- The primary empirical result is null, which limits immediate impact.
- The methodological contribution (combining MFRM + DG-IRT) is incremental.
- The theoretical contribution (Proposition 1) applies a standard econometric result to a new setting.
- The paper does not provide actionable insights for practitioners beyond "use MFRM for judge bias correction" (which is already known from Wang 2025 and other IRT literature).
- Future influence is speculative -- the framework would matter if contamination re-emerges, but that is hypothetical.

The most interesting aspect is the empirical calibration of contamination magnitude (c_bar=0.14), which could be a useful reference point for the community. But this is better suited to a short paper or empirical findings paper than a full methodological contribution.

---

### 5. Key Strengths

- **Well-motivated research question.** The confounding between judge bias and contamination is a genuine methodological concern that has not been formally addressed. The toy example in Section 2.3 effectively illustrates the problem.

- **Rigorous Monte Carlo validation of Proposition 1.** 120 parameter settings with clear reporting of direction accuracy (97.2%) and magnitude error (8%). The mapping between theoretical prediction and simulation is transparent.

- **Honest reporting of null results.** The paper does not hide the fact that G-MFRM does not significantly outperform MFRM-only on real data (p=0.31). The bootstrap CI spanning zero is clearly reported. This transparency is commendable.

- **Graceful degradation property.** The demonstration that G-MFRM does not hurt performance when contamination is absent is practically important -- it means there is no downside risk to adoption.

- **Multi-benchmark evaluation.** Testing on MT-Bench, Arena-Hard, and WildBench with 8 judges provides reasonable coverage.

- **Interpretable contamination estimates.** Per-model c_n values, even when weak, provide a structured output that baselines do not offer.

---

### 6. Key Weaknesses

- **The main empirical result is null.** G-MFRM does not significantly improve over MFRM-only (delta_tau=0.008, p=0.31). The 95% CI for delta_tau is [-0.008, 0.021]. The contamination channel adds essentially nothing on real data. This is the central weakness and it is structural: the paper proposes a framework for a problem that is currently not present in the data.

- **Prior-dominated posteriors for c_n.** Prior-posterior KL divergence of 0.08 means the data provide negligible information about contamination. The c_n estimates are not data-driven; they are prior artifacts. The 22.7% misfit rate for c_n further undermines the validity of this facet. These are not minor diagnostics -- they indicate that the contamination component of G-MFRM is not identified by the data.

- **Critically insufficient related work.** 8 references in an EMNLP submission is unacceptable. Multiple directly relevant works are missing (see Section 2 above). The "0/12 surveyed" claim is based on a narrow survey.

- **Incremental model novelty.** G-MFRM combines MFRM + DG-IRT with standard adaptations. The three claimed structural differences (binary->continuous, single-rater->multi-facet, known->unknown exposure) are engineering modifications, not modeling innovations.

- **Proposition 1 is a standard result in a new context.** Omitted variable bias in linear models is textbook econometrics. The application to measurement models is useful but does not constitute a theoretical advance.

- **Adversarial experiment is not convincing as real-world validation.** Fine-tuning 5 models on benchmark items creates a strong, artificial signal. The paper does not demonstrate detection of natural, subtle contamination.

- **The "diagnostic framework" framing is a euphemism for negative results.** The paper was designed as a correction framework; the pivot to "diagnostic" is driven by weak results, not by a genuine diagnostic methodology contribution. A proper diagnostic framework would include decision procedures, monitoring protocols, significance thresholds, and temporal tracking -- not just "we ran our model and the contamination parameter was near zero."

- **Cross-benchmark c_n correlation is weak.** r=0.35 between benchmarks for c_n vs. r=0.78 for d_j directly undermines the claim that c_n captures a "genuine model-level property." The paper acknowledges this but does not adequately address it -- if c_n is mostly noise under current contamination levels, the contamination modeling contribution is empirically vacuous.

- **Statistical power concerns.** With only 22 target models, the paper has limited statistical power to detect moderate effect sizes. A power analysis is absent.

---

### 7. Questions for Authors

1. Given that the prior-posterior KL divergence for c_n is only 0.08 and 78% of posterior intervals cover zero, can you provide evidence that the contamination component of G-MFRM is identified by the data rather than by the prior? What happens if you use a different prior (e.g., Exponential instead of Half-Normal)?

2. The cross-benchmark correlation for c_n is r=0.35 vs. r=0.78 for d_j. You interpret this as c_n being "dominated by noise rather than a stable model property under current contamination levels." If c_n is not a stable model property on current data, what is the empirical basis for claiming G-MFRM provides meaningful contamination estimates?

3. How does G-MFRM compare to simply running MFRM + ConStat separately (without the joint calibration) and reporting both outputs? This "parallel but separate" approach avoids confounding while maintaining interpretability. What specific ranking errors does joint estimation correct that parallel estimation does not?

4. The 22.7% misfit rate for c_n vs. 0% for d_j suggests the rank-1 contamination structure is inadequate. Have you tested whether person-fit statistics from MFRM-only (without the contamination term) are sufficient for flagging potentially contaminated models?

5. Your Proposition 1 states that the bias is proportional to rho * sigma_d * c_bar * e_bar * f(N,J,I). With real-data c_bar=0.14 and e_bar approximately 0.07, the predicted bias magnitude is negligible regardless of rho. Does this not undermine the motivation for joint estimation entirely for current data?

6. The paper does not cite Wang (2025, arXiv 2505.18486) which applies MFRM to LLM raters directly. How does your MFRM implementation differ from theirs? Does your Stage 1 reproduce their findings?

7. What would the contamination landscape need to look like (in terms of c_bar, e_bar, and rho) for G-MFRM to provide a statistically significant improvement over MFRM-only on real data? Can you provide a power curve?

8. The adversarial experiment fine-tunes 5 models on benchmark items. Is this a realistic threat model? Modern benchmark contamination is typically incidental (web crawl inclusion) rather than adversarial (deliberate fine-tuning). How does G-MFRM perform under incidental contamination scenarios?

---

### 8. Preliminary Scores

- **Soundness**: 3/5 -- The theoretical result is correct but standard; the empirical methodology is sound but the main result is null; MCMC diagnostics show concerning convergence for the contamination component (R-hat=1.06, ESS=112, 22.7% misfit).

- **Excitement**: 2/5 -- The research question is important but the answer is "currently no effect," the model novelty is incremental, and the paper's impact depends on a hypothetical future scenario. Will not significantly influence the field in its current form.

- **Reproducibility**: 3.5/5 -- MCMC configuration is specified; data collection protocol is described; baselines are named. However, code is not released (not clear from submission), and some implementation details (e.g., ConStat reference variant generation, LogProber integration) are underspecified.

- **Overall Assessment**: 2.5/5 (Borderline Findings) -- The paper addresses a genuine gap but its primary empirical finding is null, the model novelty is incremental (MFRM + DG-IRT combination with standard adaptations), the related work is critically thin (8 references), and the "diagnostic framework" framing does not compensate for the absence of positive empirical results on real data. The honest reporting of null results and the well-validated Proposition 1 are positives, but insufficient for a conference accept at a 21% acceptance rate. The paper would benefit from: (a) substantially expanding the related work, (b) conducting the study on benchmarks where contamination is known to be higher, or (c) reframing as a short/findings paper focused on the null result as an empirical finding about the current contamination landscape.

- **Confidence**: 4/5 -- I am familiar with both the IRT/MFRM literature and the LLM evaluation/contamination literature. My main uncertainty is whether the adversarial injection experiment might be more impactful than I assess, and whether there are unpublished concurrent works that change the novelty landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8c3c2e6-46b4-4796-87c8-1d27381a73f2",
  "isSidechain": true,
  "agentId": "a9f3d11ee2d7824d3",
  "requestId": "req_011CbGRpU36i7xmZd3cAQaWR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce137c29-3c7a-41d3-914c-1582fdc361d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2z5cckqZy71W4H3HTCEZY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2078,
      "cache_read_input_tokens": 110678,
      "output_tokens": 4835,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2078
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4835,
          "cache_read_input_tokens": 110678,
          "cache_creation_input_tokens": 2078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2078,
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
