# Research conversation: You are Reviewer R2 for a DREAM review roundtable. Your focus areas: **Novelty** and **Related Work**. ## Venue: AAAI 20

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a3c902c84adde37f7.jsonl`
- **Structured JSON:** [`e58e047a5670f40ce19f.json`](../../sessions/e5/e58e047a5670f40ce19f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-13T18:03:51.453Z_

You are Reviewer R2 for a DREAM review roundtable. Your focus areas: **Novelty** and **Related Work**.

## Venue: AAAI 2027 (using AAAI-26 standards)
- Scale: 1–10 (10=best). Acceptance rate ~17.6%.
- Dimensions: significance/novelty, soundness, relevance, clarity, reproducibility.
- Scores 5.0–5.8 are "upper middle" but many 5.5–6.5 papers were rejected at AAAI-26.

## Paper Summary
**Title**: ContamCal: Calibrating LLM Benchmark Scores via Contamination-Augmented Item Response Theory

**Core idea**: A two-stage framework:
- Stage 1: Fuse 4 contamination detection signals (embedding retrieval, Min-K%++, ConStat, Self-Critique) via RRF → per-item exposure scores
- Stage 2: Fit contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model → calibrated scores + Bayesian credible intervals

**Three claimed contributions**:
1. ContamCal framework: MAE 3.1±0.5pp, 87% coverage at 95% nominal, outperforms 7 baselines under SFT regime
2. Signal survival analysis: systematic signal×regime AUC mapping (embedding/Min-K%++ collapse post-RL, Self-Critique partially survives)
3. Dual-track validation: controlled SFT injection (2 families, 4 scales) + ecological RL case study with expected regret

## Related Work as Presented in the Paper (Section 2)
The paper covers 5 categories:
1. **Contamination detection**: Min-K%++ (Shi et al., 2024), KDS (Duan et al., 2024), ConStat (Dekoninck et al., 2024), CDD (Dong et al., 2024), Self-Critique approaches
2. **Benchmark mitigation**: LiveBench (White et al., 2024), rephrasing strategies, Emperor's New Clothes finding (Xu et al., 2024) that 20 mitigation strategies systematically fail
3. **IRT for LLM evaluation**: Lalor et al. 2024 (HiBayES), TinyBenchmarks (Polo et al., 2024), Growing Pains, ATLAS — none model contamination
4. **Post-hoc calibration**: DCR (Dong et al., 2024) — adjusted accuracy via fuzzy inference, lacks UQ. Remove-and-rescore
5. **Item compromise in educational measurement**: Eckerly 2017, Sinharay 2017 — item compromise IRT adapted with 3 modifications (single model→joint, binary→continuous exposure, stable→regime-conditional ability)

## Key Method Details
- 4PL IRT: P(Y=1) = c_i + (d_i - c_i) · σ(a_i(θ_j + γ_k · τ_ji - b_i))
- γ_k is per-benchmark contamination coefficient
- τ_ji is latent true exposure (observed noisily via RRF)
- Measurement error: e_ji ~ N(τ_ji, σ_e²)
- Calibrated score: set τ_ji=0 for all items
- RRF chosen over learned aggregation to avoid meta-circularity

## Key Results for Context
- Beats 5/7 baselines significantly; DCR marginal (p=0.042), linear regression not significant (p=0.087)
- Signal survival heatmap is claimed as "strongest empirical contribution"
- 87% coverage at 95% nominal (8pp gap attributed to local independence violation)
- Multi-family (Llama): direction consistent but 1.8pp MAE gap
- RL regime: wide CIs (10.5-18pp) framed as "correct behavior, not limitation"

## Your Task
Provide a detailed review focusing on:

### Novelty Assessment
1. How novel is the core idea of using IRT with contamination covariates for LLM benchmark calibration? The paper draws from item compromise literature (Eckerly 2017, Sinharay 2017) — how significant are the adaptations?
2. Is the signal survival analysis (signal×regime AUC mapping) genuinely novel? Has anyone systematically mapped detection signal performance across training regimes before?
3. Is RRF fusion of detection signals novel, or is it a straightforward application of a known technique?
4. The measurement error model for noisy exposure — how novel is this in the IRT context?
5. The per-benchmark γ_k (heterogeneous contamination susceptibility) — novel or expected extension?
6. Overall, is this a "novel framework" or a "competent integration of existing components"?

### Related Work Assessment
1. Is the related work comprehensive? Are there important missing references?
   - Consider: Bayesian IRT calibration literature, other contamination calibration approaches
   - Are there works on IRT identifiability that should be cited?
   - San Martín et al. 2009 is cited in references but not discussed in related work — is it adequately used?
2. Is the paper fairly positioned relative to DCR (Dong et al., 2024)? DCR achieves MAE 4.1pp vs ContamCal's 3.1pp, but comparison is p=0.042
3. Is the Emperor's New Clothes (Xu et al., 2024) finding properly leveraged as motivation?
4. Are there concurrent works (2025-2026) on contamination-aware evaluation that should be discussed?
5. Is Growing Pains / PSN-IRT / ATLAS literature adequately engaged with?
6. Is the item compromise IRT literature (Eckerly, Sinharay) properly credited and differentiated?

### Positioning and Framing
1. Does the paper oversell its contributions? Are the claims proportionate to the evidence?
2. The "signal survival" being elevated to "Core Contribution 2" — is this justified given it's primarily an empirical observation?
3. Is the "dual-track validation" really a distinct contribution, or is it experimental design?
4. Are the limitations honestly stated? (local independence, SFT-only controlled, scale, cross-family)
5. Does the paper properly acknowledge what it cannot do (precise RL calibration)?

### Writing Quality and Clarity
1. Is the paper well-organized and clearly written?
2. Are the mathematical formulations clear?
3. Is the paper self-contained for the AAAI audience?

Output format:
```
## R2 Review: Novelty + Related Work

### Summary
[2-3 sentences]

### Strengths (Novelty)
[Numbered list]

### Strengths (Related Work & Positioning)
[Numbered list]

### Weaknesses (Novelty)
[Numbered list, with severity: minor/moderate/major]

### Weaknesses (Related Work & Positioning)
[Numbered list, with severity: minor/moderate/major]

### Questions for Authors
[Numbered list]

### Missing References
[Specific papers/areas that should be cited]

### Scores (AAAI 1-10 scale)
- Novelty: X/10
- Related Work: X/10
- Clarity: X/10
- Overall recommendation: X/10
- Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "6469a16e-2d30-4f59-84e8-84181572cdfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T18:03:51.469Z_

```json
{
  "parentUuid": "6469a16e-2d30-4f59-84e8-84181572cdfb",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
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
  "uuid": "7c37e68a-c86d-467e-b42e-56c7caa9724f",
  "timestamp": "2026-05-13T18:03:51.469Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T18:03:56.069Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c37e68a-c86d-467e-b42e-56c7caa9724f",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11UmsVBncZpogWSbrG7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82ade528-0635-4dca-b21c-4506ba3bcc1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyfaKKGoKvpGuxSgNhH1Ey",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7635,
      "cache_read_input_tokens": 8253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7635,
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

_source line 4 · 2026-05-13T18:03:57.868Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Cd3DYikmFPPBJX1515Mx6V`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82ade528-0635-4dca-b21c-4506ba3bcc1d",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11UmsVBncZpogWSbrG7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a6663d0-b534-4fb4-91c6-28d3a3233d0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyfaKKGoKvpGuxSgNhH1Ey",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7635,
      "cache_read_input_tokens": 8253,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7635
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 141,
          "cache_read_input_tokens": 8253,
          "cache_creation_input_tokens": 7635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7635,
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

_source line 5 · 2026-05-13T18:03:57.876Z_

<details><summary>↩ Tool result · `toolu_01Cd3DYikmFPPBJX1515Mx6V`</summary>

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
  "parentUuid": "0a6663d0-b534-4fb4-91c6-28d3a3233d0b",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "37987f78-2ecb-455a-9426-b7c0256e94d1",
  "sourceToolAssistantUUID": "0a6663d0-b534-4fb4-91c6-28d3a3233d0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T18:04:04.048Z_



Let me read the paper and supporting materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37987f78-2ecb-455a-9426-b7c0256e94d1",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11VFZNnAsKiRgXCcf7G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c0f851d-fdc4-4310-bf1f-38998515d7b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRWVfk1AjNT2BnYXX8Ed23",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 15888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2014,
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

_source line 7 · 2026-05-13T18:04:05.228Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01S3yDXf5zGSruqgJFSkygRU`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c0f851d-fdc4-4310-bf1f-38998515d7b4",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11VFZNnAsKiRgXCcf7G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a072cc4f-c235-4115-aaee-c446459e4658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRWVfk1AjNT2BnYXX8Ed23",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 15888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2014,
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

_source line 8 · 2026-05-13T18:04:05.280Z_

<details><summary>↩ Tool result · `toolu_01S3yDXf5zGSruqgJFSkygRU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_004_sim_sweep | 4PL+γ IRT parameter recovery degrades gracefully with exposure signal quality (AUC); there exists a minimum AUC threshold below which γ 95% CI width exceeds 15pp; recovery improves with N_models; prior sensitivity is bounded | — | — | — |\\n\\n## 待处理\\n- exp_001_sft_injection（准备中）\\n\\n## 近期结论\\n- **mvp_sim_confounding** (success): 4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure\\n- **mvp_sim_4pl_gamma** (success): 4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9\\n\\n## 趋势\\n成功 2 / 负向 0 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-21977: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 939, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a072cc4f-c235-4115-aaee-c446459e4658",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "d0b0d0cb-f2e9-43a7-adc3-9f63271a7276",
  "sourceToolAssistantUUID": "a072cc4f-c235-4115-aaee-c446459e4658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T18:04:06.133Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01W12S6oJa41SzHgUvgo5wnm`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0b0d0cb-f2e9-43a7-adc3-9f63271a7276",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11VFZNnAsKiRgXCcf7G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38b24baf-01c9-48ff-b167-974effb7c4ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRWVfk1AjNT2BnYXX8Ed23",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 15888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2014,
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

_source line 10 · 2026-05-13T18:04:06.172Z_

<details><summary>↩ Tool result · `toolu_01W12S6oJa41SzHgUvgo5wnm`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38b24baf-01c9-48ff-b167-974effb7c4ad",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "af1d4ea0-d513-4aa2-b4f2-15355c44778b",
  "sourceToolAssistantUUID": "38b24baf-01c9-48ff-b167-974effb7c4ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T18:04:06.610Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AuMggWBxPwroERF9QJS9HK`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af1d4ea0-d513-4aa2-b4f2-15355c44778b",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11VFZNnAsKiRgXCcf7G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "031ac709-b689-48b1-a853-51faaebe1f2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRWVfk1AjNT2BnYXX8Ed23",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 15888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2014,
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

_source line 12 · 2026-05-13T18:04:06.631Z_

<details><summary>↩ Tool result · `toolu_01AuMggWBxPwroERF9QJS9HK`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "031ac709-b689-48b1-a853-51faaebe1f2a",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "d2463971-34ea-4c8f-ba68-8e69d80be878",
  "sourceToolAssistantUUID": "031ac709-b689-48b1-a853-51faaebe1f2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T18:04:07.316Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01E3xDhKXVvRHCyHD9cSddSx`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2463971-34ea-4c8f-ba68-8e69d80be878",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11VFZNnAsKiRgXCcf7G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ac3a318-34c6-4583-bd66-b69149f6b442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRWVfk1AjNT2BnYXX8Ed23",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 15888,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2014
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 411,
          "cache_read_input_tokens": 15888,
          "cache_creation_input_tokens": 2014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2014,
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

_source line 14 · 2026-05-13T18:04:07.356Z_

<details><summary>↩ Tool result · `toolu_01E3xDhKXVvRHCyHD9cSddSx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\n- Track: Machine Learning for NLP / Resources and Evaluation\\n- Aligns with EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" (explicitly invites contamination/data governance work)\\n\\n## Core Insight\\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.\\n\\n## Core Claims (3 条)\\n\\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B) within the Qwen2.5 family and 4 benchmarks. (Multi-family generalization is a rebuttal-ready extension via exp-014, not initial submission scope.)\\n\\n2. **Signal Survival & Aggregation Claim**: Contamination detection signals degrade systematically under RL post-training (cliff-like, not gradual). Training-free RRF fusion provides a principled, robust design choice for exposure estimation without meta-circularity. Signal × regime AUC mapping establishes which signals survive under which training regimes.\\n\\n3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — SFT models get tighter CIs, RL models get appropriately wider CIs reflecting genuine epistemic uncertainty.\\n\\n## Contributions (Hierarchical)\\n\\n### Core\\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals\\n2. Signal survival analysis: systematic signal × regime AUC mapping showing cliff-like degradation under RL — an empirically novel finding with practical implications for the detection community (elevated from Supporting per Dream review)\\n3. Dual-track validation: controlled SFT injection across multiple model scales within the Qwen2.5 family (internal validity) + ecological RL case study (external validity)\\n\\n### Supporting\\n4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds\\n5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology\\n\\n## Story Spine\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering \\\"what would this model's score be if it had never seen the test data?\\\"\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\\n- **Our framing**: ContamCal is a \\\"statistical safety net\\\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware signal selection).\\n- **Headline result template**: \\\"On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage.\\\"\\n\\n## Venue Fit Risks\\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \\\"new algorithm\\\" — positioned as (a) signal survival analysis as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \\\"calibration is only as good as its inputs.\\\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\\n\\n## Anticipated Reviewer Concerns & Defenses\\n\\n| # | Concern | Defense | Experiment |\\n|---|---------|---------|------------|\\n| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |\\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \\\"best-available proxy\\\", acknowledged as limitation | exp-006, exp-009 |\\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\\n| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |\\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\\n\\n## Evaluation Protocol (5 Metrics)\\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\\n\\n## Benchmarks (4)\\n1. **MMLU** — knowledge-intensive multiple-choice (14K items)\\n2. **GSM8K** — mathematical reasoning free-form (~1.3K items)\\n3. **ARC-Challenge** — science reasoning multiple-choice\\n4. **HumanEval** — code generation with execution evaluation (N=164, noted as potential limitation for 4PL estimation)\\n- Day-8 contingency: reduce to MMLU + GSM8K\\n\\n## Baselines (7)\\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\\n\\n## Local Independence Discussion\\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\\n\\n## Citation Requirements (30+ minimum)\\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\\n\", \"total_chars\": 11645, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ac3a318-34c6-4583-bd66-b69149f6b442",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "6af7a2f0-376d-4126-a70c-96b91e7ff84b",
  "sourceToolAssistantUUID": "6ac3a318-34c6-4583-bd66-b69149f6b442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T18:04:15.512Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DqGyaSEj4mjxL7botuTw3c`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6af7a2f0-376d-4126-a70c-96b91e7ff84b",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11Vwt2dZRQSduG72GUK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b501607-1548-4180-a1f2-a93be0b8e75f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5sMP1pMPMH7Dx64o5gHz4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4533,
      "cache_read_input_tokens": 17902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4533,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 16 · 2026-05-13T18:04:15.560Z_

<details><summary>↩ Tool result · `toolu_01DqGyaSEj4mjxL7botuTw3c`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-13 17:14 UTC | 更新原因: D006: 投稿目标改回 EMNLP 2026 ARR May 25，12 天冲刺计划\\n\\n## 核心方向\\nContamCal：post-hoc statistical calibration via contamination-augmented 4PL IRT。详见 paper_framing.md。\\n\\n## 投稿目标\\n**EMNLP 2026 ARR May 25**（D006, 距今 12 天）\\n- Track: ML for NLP / Resources and Evaluation\\n- Special theme: \\\"New Missions for NLP Research\\\" — contamination/data governance\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-13 通过）\\n- **exp-004**: subset sweep 运行中（12 conditions × 10 seeds，~8-12h CPU）\\n- **论文**: Agent 正在写 Introduction + Method LaTeX 初稿\\n- **Dream D2**: re-dream 运行中（dream_20260513T171200），验证 framing/plan 修改\\n- **GPU**: 等待用户开服务器（用户承诺充足资源）\\n\\n## 12 天冲刺计划\\n\\n### Day 1-2 (May 13-14): 基础设施 + 并行启动\\n- [ ] 用户开 GPU 服务器（4+ H100/A100-80G）\\n- [x] exp-004 subset sweep 运行中\\n- [ ] exp-001 SFT injection 启动（15 runs 并行化到 4 GPU，wall-clock ~13h）\\n- [ ] 论文 Introduction + Method 初稿完成\\n\\n### Day 3-4 (May 15-16): 信号计算\\n- [ ] exp-002 信号 pipeline（4 signals on all models）\\n- [ ] exp-003 RRF ablation\\n- [ ] exp-004 全量 sweep（如 subset 结果 OK）\\n- [ ] exp-005 noise propagation\\n\\n### Day 5-6 (May 17-18): IRT 校准 + 分析\\n- [ ] exp-006 IRT calibration + 7 baselines\\n- [ ] exp-008 signal survival analysis（P0）\\n- [ ] 分析 + 图表生成\\n\\n### Day 7-8 (May 19-20): 论文 + P1 实验\\n- [ ] Paper Agent full draft\\n- [ ] exp-007 7B scale-bridging（如 GPU 允许）\\n- [ ] exp-009 RL case study（如时间允许）\\n- [ ] **Day-8 checkpoint**: behind schedule → cut to MMLU+GSM8K，drop P1\\n\\n### Day 9-10 (May 21-22): 迭代\\n- [ ] Reviewer 审查 + 修改循环\\n- [ ] 引用验证（30+ citations）\\n- [ ] 图表打磨\\n\\n### Day 11-12 (May 23-24): 最终提交\\n- [ ] Camera-ready polish\\n- [ ] ARR submission\\n\\n## GPU 预算\\n- P0: 90h | P1: 60h | P2: 20h (deferred) | Buffer: 30h\\n- 冲刺优先: P0 全跑 + exp-008 (P0) + exp-007/009 (P1, 时间允许)\\n- exp-014 (multi-family) 和 P2 推迟到 camera-ready/rebuttal\\n\\n## 实验优先级（冲刺模式）\\n1. exp-001 → exp-002 → exp-003 → exp-006（critical path，~80h GPU）\\n2. exp-004, exp-005（CPU，并行）\\n3. exp-008（P0，10h GPU）\\n4. exp-007（P1，30h GPU，时间允许才跑）\\n5. exp-009（P1，15h GPU，时间允许才跑）\\n6. exp-014, exp-012, exp-013 → deferred to rebuttal\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D007 | 2026-05-13 | Re-dream gate 从阻塞改为 advisory：D2 结果不再阻塞 P0 实验启动，改为  | — |\\n| D006 | 2026-05-13 | 投稿目标改回 EMNLP 2026 ARR May 25（撤销 D001），12 天冲刺 | — |\\n| D005 | 2026-05-13 | Dream 审稿分析：best=5/10, median=5/10, worst=4/10。识别 6 | dream_20260513T155040 |\\n| D004 | 2026-05-13 | MVP 通过，进入 Research 阶段 | mvp_sim_4pl_gamma, mvp_sim_confounding |\\n| D003 | 2026-05-13 | Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMS | mvp_sim_4pl_gamma |\\n| D002 | 2026-05-13 | 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-e | — |\\n| D001 | 2026-05-13 | MVP 用 simulation identifiability test 验证 4PL+γ IRT | — |\\n\\n\", \"total_chars\": 2695, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b501607-1548-4180-a1f2-a93be0b8e75f",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "be26828d-020e-4b54-a81f-fc6e2d8f86c0",
  "sourceToolAssistantUUID": "0b501607-1548-4180-a1f2-a93be0b8e75f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T18:04:15.834Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FdqHFNab4cbunA8CvmNA6d`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be26828d-020e-4b54-a81f-fc6e2d8f86c0",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11Vwt2dZRQSduG72GUK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da7e43de-3cd6-4ff8-afbc-810343d265a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5sMP1pMPMH7Dx64o5gHz4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4533,
      "cache_read_input_tokens": 17902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4533,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 18 · 2026-05-13T18:04:15.854Z_

<details><summary>↩ Tool result · `toolu_01FdqHFNab4cbunA8CvmNA6d`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No memory.md found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da7e43de-3cd6-4ff8-afbc-810343d265a5",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "422f5ded-e8be-4c75-bd4f-7e94ea3c32bc",
  "sourceToolAssistantUUID": "da7e43de-3cd6-4ff8-afbc-810343d265a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T18:04:16.472Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017QyykSn9r6YNykn6p2awo7`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "422f5ded-e8be-4c75-bd4f-7e94ea3c32bc",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11Vwt2dZRQSduG72GUK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d828aefb-2381-48ff-8086-0e9d93d0f357",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5sMP1pMPMH7Dx64o5gHz4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4533,
      "cache_read_input_tokens": 17902,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4533
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 298,
          "cache_read_input_tokens": 17902,
          "cache_creation_input_tokens": 4533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4533,
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

_source line 20 · 2026-05-13T18:04:16.506Z_

<details><summary>↩ Tool result · `toolu_017QyykSn9r6YNykn6p2awo7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml\", \"content\": \"_next_id: 8\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:26 UTC\\n  summary: MVP 用 simulation identifiability test 验证 4PL+γ IRT 核心假设，放弃 EMNLP 2026 May\\n    ARR\\n  rationale: 核心假设是 γ 与 θ 可分离——这在合成数据上可验证，无需 GPU。12 天内完成完整论文不现实，目标改为 AAAI 2027 / ICLR\\n    2027。MVP 通过后再配置 GPU 进入 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:29 UTC\\n  summary: 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-exposure confounding +\\n    加 FPR/FNR 噪声模型\\n  rationale: Reviewer 指出原 MVP simulation 条件过于理想化。θ-exposure confounding 是 γ identifiability\\n    的核心威胁，必须在 MVP 阶段覆盖。参数 grid 扩展（18 conditions）和 FPR/FNR 噪声增量成本约 4-8h CPU，不影响时间线。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 10:57 UTC\\n  summary: Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMSE 阈值从 0.2 放宽至 0.30\\n  rationale: 'Variant A (N_items=300, 4PL NUTS): γ_rel_bias=6.8%, θ_corr=0.943, 收敛完美。N_items=100\\n    的 borderline fail 确认为信息量不足（c/d 参数估计需要更多 items），非方法论缺陷。θ_RMSE 阈值从 0.2 放宽至 0.30，Reviewer\\n    论证理论最优 SE≈0.18-0.26，0.2 在 N=50 models 下不可达。ADVI 在 4PL 上彻底失败（bad local mode），MVP\\n    阶段放弃 ADVI，仅用 NUTS。2PL+γ 在 4PL 生成数据上严重 misspecified（γ=0.16），确认 4PL 的必要性。'\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: primary\\n    result: Phase A PASS (Variant A)\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-13 15:45 UTC\\n  summary: MVP 通过，进入 Research 阶段\\n  rationale: Phase A (identifiability) 和 P2 (confounding robustness) 两个 gate 全部 PASS。4PL+γ\\n    NUTS 在 N_items=300 条件下 γ 相对偏差 <8%，θ 相关性 >0.94，混淆分离后残差相关 0.058。ADVI 和 2PL 被排除。核心假设\\\"IRT\\n    模型可分离污染效应与真实能力\\\"在合成数据上得到验证。\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: Phase A identifiability\\n    result: PASS at N_items=300\\n  - exp_id: mvp_sim_confounding\\n    role: P2 confounding robustness\\n    result: PASS with confound_corr=0.38\\n  depends_on:\\n  - D002\\n  - D003\\n- id: D005\\n  date: 2026-05-13 17:11 UTC\\n  summary: Dream 审稿分析：best=5/10, median=5/10, worst=4/10。识别 6 个确认行动项，修改 framing +\\n    plan，需 re-dream\\n  rationale: Dream full review 暴露 6 个跨三档一致的结构性问题：(1) 单一全局 γ misspecified → 加 per-benchmark\\n    γ_k 变体；(2) 引用不足 10 refs → 目标 30+；(3) Stage 1 uncertainty 未传播 → 加 measurement error\\n    model 为默认；(4) 可识别性阈值无理论依据 → 加 Fisher Information 分析；(5) Signal survival 应为核心贡献\\n    → 升级；(6) 单一模型家族 → 加 exp-014 multi-family。DCR baseline 此前已修复。RL regret ground truth\\n    明确为 held-out clean benchmark。Local independence 加显式讨论。方向正确但执行需加强，不降 venue。\\n  related_experiments:\\n  - exp_id: dream_20260513T155040\\n    role: Dream simulation\\n    result: best=5/10, median=5/10, worst=4/10\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 17:14 UTC\\n  summary: 投稿目标改回 EMNLP 2026 ARR May 25（撤销 D001），12 天冲刺\\n  rationale: 用户明确指令：改回 EMNLP 2026 ARR May 25，承诺提供充足资源，不担心 DDL。EMNLP 2026 special theme\\n    明确邀请 contamination/data governance 工作，venue fit 最佳。12 天冲刺计划：4+ GPU 并行 SFT injection，AI\\n    团队 24/7，Day-8 contingency 保底。P2 实验和 exp-014 (multi-family) 推迟到 camera-ready 或\\n    rebuttal。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D005\\n- id: D007\\n  date: 2026-05-13 17:23 UTC\\n  summary: Re-dream gate 从阻塞改为 advisory：D2 结果不再阻塞 P0 实验启动，改为 advisory 参考\\n  rationale: D006 确立 12 天冲刺后，re-dream 等待时间（~25min）虽短但 GPU 到位后不应因 dream 结果阻塞实验启动。Dream\\n    D2 结果仍会分析并据此调整 framing/plan，但不作为 P0 实验的 hard gate。准备工作（代码/数据/环境）立即并行推进。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n\", \"total_chars\": 3319, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d828aefb-2381-48ff-8086-0e9d93d0f357",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "720ecd35-2c7f-4494-8dce-1a85d0d082e1",
  "sourceToolAssistantUUID": "d828aefb-2381-48ff-8086-0e9d93d0f357",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-13T18:04:22.412Z_

Now let me look at the actual paper artifacts and any LaTeX drafts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "720ecd35-2c7f-4494-8dce-1a85d0d082e1",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11Wd1FPjUviqWsX6Txa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07a4bf27-6ae7-4c20-89c2-9cb723fb787a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REm3eAPPQDt956uw8WdwFQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4302,
      "cache_read_input_tokens": 22435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4302,
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

_source line 22 · 2026-05-13T18:04:24.832Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JPrXCZTZnBXhg9B45e1AqD`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07a4bf27-6ae7-4c20-89c2-9cb723fb787a",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11Wd1FPjUviqWsX6Txa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b3405d0-2ea9-432d-bf43-b53ff1abf4ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REm3eAPPQDt956uw8WdwFQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4302,
      "cache_read_input_tokens": 22435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4302,
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

_source line 23 · 2026-05-13T18:04:24.971Z_

<details><summary>↩ Tool result · `toolu_01JPrXCZTZnBXhg9B45e1AqD`</summary>

```text
artifacts/dream_reports/dream_20260513T155040/best/paper.tex
artifacts/dream_reports/dream_20260513T155040/median/paper.tex
artifacts/dream_reports/dream_20260513T155040/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/paper_draft/main.tex
artifacts/paper_draft/introduction.tex
artifacts/paper_draft/related_work.tex
artifacts/dream_reports/dream_20260513T171200/best/paper.tex
artifacts/dream_reports/dream_20260513T171200/median/paper.tex
artifacts/paper_draft/method.tex
artifacts/dream_reports/dream_20260513T171200/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b3405d0-2ea9-432d-bf43-b53ff1abf4ba",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "ebbfda15-00d7-469f-95da-2be65df8e41d",
  "sourceToolAssistantUUID": "2b3405d0-2ea9-432d-bf43-b53ff1abf4ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-13T18:04:25.777Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018UuUoydyKAQNrnUpMqAQYj`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebbfda15-00d7-469f-95da-2be65df8e41d",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11Wd1FPjUviqWsX6Txa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "260f501f-1a2f-4a2a-833d-1ec90775edcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REm3eAPPQDt956uw8WdwFQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4302,
      "cache_read_input_tokens": 22435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4302,
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

_source line 25 · 2026-05-13T18:04:25.975Z_

<details><summary>↩ Tool result · `toolu_018UuUoydyKAQNrnUpMqAQYj`</summary>

```text
.venv/lib/python3.14/site-packages/pip/__init__.py
.venv/lib/python3.14/site-packages/pip/__main__.py
.venv/lib/python3.14/site-packages/pip/__pip-runner__.py
.venv/lib/python3.14/site-packages/pip/_internal/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/build_env.py
.venv/lib/python3.14/site-packages/pip/_internal/cache.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/autocompletion.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/base_command.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/cmdoptions.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/command_context.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/index_command.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/main.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/main_parser.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/parser.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/progress_bars.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/req_command.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/spinners.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/status_codes.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/cache.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/check.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/completion.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/debug.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/download.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/freeze.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/hash.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/help.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/index.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/inspect.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/install.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/list.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/lock.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/search.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/show.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/uninstall.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/wheel.py
.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
.venv/lib/python3.14/site-packages/pip/_internal/distributions/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/distributions/base.py
.venv/lib/python3.14/site-packages/pip/_internal/distributions/installed.py
.venv/lib/python3.14/site-packages/pip/_internal/distributions/sdist.py
.venv/lib/python3.14/site-packages/pip/_internal/distributions/wheel.py
.venv/lib/python3.14/site-packages/pip/_internal/exceptions.py
.venv/lib/python3.14/site-packages/pip/_internal/index/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/index/collector.py
.venv/lib/python3.14/site-packages/pip/_internal/index/package_finder.py
.venv/lib/python3.14/site-packages/pip/_internal/index/sources.py
.venv/lib/python3.14/site-packages/pip/_internal/locations/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/locations/_distutils.py
.venv/lib/python3.14/site-packages/pip/_internal/locations/_sysconfig.py
.venv/lib/python3.14/site-packages/pip/_internal/locations/base.py
.venv/lib/python3.14/site-packages/pip/_internal/main.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/_json.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/base.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_compat.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_dists.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_envs.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/pkg_resources.py
.venv/lib/python3.14/site-packages/pip/_internal/models/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/models/candidate.py
.venv/lib/python3.14/site-packages/pip/_internal/models/direct_url.py
.venv/lib/python3.14/site-packages/pip/_internal/models/format_control.py
.venv/lib/python3.14/site-packages/pip/_internal/models/index.py
.venv/lib/python3.14/site-packages/pip/_internal/models/installation_report.py
.venv/lib/python3.14/site-packages/pip/_internal/models/link.py
.venv/lib/python3.14/site-packages/pip/_internal/models/pylock.py
.venv/lib/python3.14/site-packages/pip/_internal/models/scheme.py
.venv/lib/python3.14/site-packages/pip/_internal/models/search_scope.py
.venv/lib/python3.14/site-packages/pip/_internal/models/selection_prefs.py
.venv/lib/python3.14/site-packages/pip/_internal/models/target_python.py
.venv/lib/python3.14/site-packages/pip/_internal/models/wheel.py
.venv/lib/python3.14/site-packages/pip/_internal/network/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/network/auth.py
.venv/lib/python3.14/site-packages/pip/_internal/network/cache.py
.venv/lib/python3.14/site-packages/pip/_internal/network/download.py
.venv/lib/python3.14/site-packages/pip/_internal/network/lazy_wheel.py
.venv/lib/python3.14/site-packages/pip/_internal/network/session.py
.venv/lib/python3.14/site-packages/pip/_internal/network/utils.py
.venv/lib/python3.14/site-packages/pip/_internal/network/xmlrpc.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/build_tracker.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata_editable.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata_legacy.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel_editable.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel_legacy.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/check.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/freeze.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/install/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/install/editable_legacy.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/install/wheel.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/prepare.py
.venv/lib/python3.14/site-packages/pip/_internal/pyproject.py
.venv/lib/python3.14/site-packages/pip/_internal/req/__init__.py
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "260f501f-1a2f-4a2a-833d-1ec90775edcc",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "c819cec3-3169-47e4-a2d3-fb7c6802026e",
  "sourceToolAssistantUUID": "260f501f-1a2f-4a2a-833d-1ec90775edcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-13T18:04:26.401Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015f9yw7mDioXWD86ZeGc6WH`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "ARCHITECTURE.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c819cec3-3169-47e4-a2d3-fb7c6802026e",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11Wd1FPjUviqWsX6Txa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff39fa08-0df1-424f-a43d-508be628bbf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REm3eAPPQDt956uw8WdwFQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4302,
      "cache_read_input_tokens": 22435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4302,
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

_source line 27 · 2026-05-13T18:04:26.447Z_

<details><summary>↩ Tool result · `toolu_015f9yw7mDioXWD86ZeGc6WH`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ARCHITECTURE.md found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff39fa08-0df1-424f-a43d-508be628bbf8",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "3e09fc82-759c-4ce1-83c7-7270e8272cec",
  "sourceToolAssistantUUID": "ff39fa08-0df1-424f-a43d-508be628bbf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-13T18:04:30.163Z_

Let me read the dream report papers and the actual paper drafts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e09fc82-759c-4ce1-83c7-7270e8272cec",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11XMaLMZTzgRtZaLUM2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48d57059-2fa2-4891-a6f9-56344e945d94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPVgbaMF28YLmVDJcqq2tV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3213,
      "cache_read_input_tokens": 26737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3213,
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

_source line 29 · 2026-05-13T18:04:32.106Z_

<details open><summary>🔧 Tool call — Read · `toolu_0167xWgEwMjVvTrE4Bff3TNG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48d57059-2fa2-4891-a6f9-56344e945d94",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11XMaLMZTzgRtZaLUM2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c076644-9ecd-4f49-8162-842b9960cffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPVgbaMF28YLmVDJcqq2tV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3213,
      "cache_read_input_tokens": 26737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3213,
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

_source line 30 · 2026-05-13T18:04:32.388Z_

<details><summary>↩ Tool result · `toolu_0167xWgEwMjVvTrE4Bff3TNG`</summary>

```text
1	\documentclass[letterpaper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{amsmath,amssymb,amsfonts}
4	\usepackage{booktabs}
5	\usepackage{graphicx}
6	\usepackage{multirow}
7	\usepackage{xcolor}
8	\usepackage{hyperref}
9	\usepackage{natbib}
10	\usepackage{array}
11	\usepackage{enumitem}
12	\usepackage{microtype}
13	\usepackage{tabularx}
14	
15	\title{ContamCal: Calibrating LLM Benchmark Scores\\via Contamination-Augmented Item Response Theory}
16	\author{
17	  Anonymous Authors
18	}
19	\date{}
20	
21	\begin{document}
22	\maketitle
23	
24	% ===========================================================================
25	\begin{abstract}
26	Benchmark contamination --- where test items leak into training data --- inflates LLM evaluation scores by 8--15 percentage points, and all known mitigation strategies have been shown to be ineffective.
27	We introduce \textsc{ContamCal}, a two-stage framework that \emph{calibrates} contaminated benchmark scores rather than attempting to eliminate contamination.
28	Stage~1 computes per-item exposure scores by fusing four detection signals via Reciprocal Rank Fusion (RRF), a parameter-free aggregator that avoids meta-circularity.
29	Stage~2 fits a contamination-augmented 4PL IRT model with per-benchmark contamination parameters~$\gamma_k$ and a measurement error model that propagates detection uncertainty into Bayesian credible intervals.
30	On controlled SFT contamination injection across 3 model scales (0.5B--7B), 2 additional model families (Llama, Pythia), and 4 benchmarks (MMLU, GSM8K, ARC, HumanEval), ContamCal recovers true performance within 1.5\,pp MAE with 93\% credible interval coverage at the 95\% nominal level, while naive scores overestimate by 11.2\,pp.
31	ContamCal significantly outperforms all 7 baselines including DCR ($\Delta$=1.9\,pp, $p$=0.003).
32	A systematic signal$\times$regime analysis reveals cliff-like degradation of logit-based signals under RL post-training, while meta-cognitive signals survive (AUC=0.65), enabling ContamCal to function in RL regimes with appropriately wider credible intervals.
33	Fisher Information analysis and a 144-condition simulation sweep establish theoretically grounded identifiability bounds (AUC$\geq$0.68, $N_{\text{models}}\geq$35).
34	\end{abstract}
35	
36	% ===========================================================================
37	\section{Introduction}
38	\label{sec:intro}
39	
40	Large language model evaluation relies on standardized benchmarks, yet training data contamination systematically inflates benchmark scores.
41	Paraphrased test items that evade $n$-gram decontamination can inflate MMLU accuracy by 8--15 percentage points~\citep{yang2023rethinking,dekoninck2024evading}.
42	The Emperor's New Clothes study~\citep{xu2025emperor} tested 20 mitigation strategies and found \emph{none} effective --- rephrased and shuffled variants still fail to eliminate contamination effects.
43	This motivates a fundamental shift from contamination \emph{elimination} to contamination \emph{calibration}: instead of removing contaminated items (which does not work), we statistically control for contamination and produce adjusted scores with proper uncertainty quantification.
44	
45	This shift mirrors the evolution in causal inference from eliminating confounders to statistically controlling for them~\citep{rosenbaum1983central}.
46	In educational measurement, item compromise IRT~\citep{eckerly2017detecting,sinharay2017detection} models the effect of leaked exam items on examinee scores --- we adapt this framework to LLM evaluation with three non-trivial structural changes.
47	
48	\textbf{Contributions.}
49	(1)~We propose \textsc{ContamCal}, a two-stage framework that maps detection signals to per-item exposure scores via RRF and fits a contamination-augmented 4PL IRT model with per-benchmark $\gamma_k$ parameters and a measurement error model, producing calibrated benchmark scores with Bayesian credible intervals.
50	(2)~We provide a systematic signal$\times$regime AUC analysis revealing cliff-like degradation of logit-based detection signals under RL post-training, with meta-cognitive signals surviving --- an empirically novel finding with practical implications.
51	(3)~We validate ContamCal via controlled SFT injection (internal validity) across 3 model families and 4 scales, plus an ecological RL case study (external validity), establishing dual-track evidence.
52	
53	% ===========================================================================
54	\section{Related Work}
55	\label{sec:related}
56	
57	\textbf{Contamination detection.}
58	Detection methods identify whether test items appeared in training data.
59	Min-K\%++~\citep{zhang2024minkpp} uses token-level likelihood; ConStat~\citep{dekoninck2024constat} compares original vs.\ paraphrased performance; Self-Critique~\citep{wentzel2024selfcritique} elicits model meta-cognition.
60	Embedding-based retrieval~\citep{golchin2024time} searches for semantic matches between training data and test items.
61	These methods \emph{detect} contamination but do not produce calibrated scores.
62	
63	\textbf{IRT for LLM evaluation.}
64	Item Response Theory has been applied to LLM evaluation~\citep{lalor2024benchmarking,martinez2024item}, with HiBayES~\citep{polo2024tinybenchmarks} providing Bayesian uncertainty quantification.
65	Growing Pains~\citep{burnell2023rethink} identifies challenges in applying IRT to LLMs.
66	However, existing IRT approaches for LLMs do not model contamination.
67	In educational measurement, item compromise IRT~\citep{eckerly2017detecting,sinharay2017detection} models leaked items, and explanatory IRT~\citep{deboeck2004explanatory} incorporates item-level covariates --- ContamCal adapts these traditions.
68	
69	\textbf{Contamination adjustment.}
70	DCR~\citep{yang2025dcr} provides adjusted accuracy via fuzzy inference but lacks uncertainty bounds and RL handling.
71	Remove-and-rescore drops flagged items but loses information and requires arbitrary thresholds.
72	Emperor's mitigation strategies (rephrasing, option shuffling) have been shown ineffective~\citep{xu2025emperor}.
73	Dynamic benchmarks like LiveBench~\citep{white2024livebench} sidestep contamination but require continuous curation.
74	
75	% ===========================================================================
76	\section{Method}
77	\label{sec:method}
78	
79	ContamCal operates in two stages: (1) provenance mapping via multi-signal fusion, and (2) contamination-augmented IRT calibration with measurement error modeling.
80	
81	\subsection{Stage 1: Multi-Signal Exposure Estimation}
82	\label{sec:stage1}
83	
84	Given a model $m$ and benchmark item $i$, we compute four per-item detection signals: embedding retrieval similarity, Min-K\%++ likelihood ratio, ConStat original-vs-paraphrase gap, and Self-Critique meta-cognitive score.
85	Each signal $s \in \{1,\ldots,4\}$ produces a score $r_{s,i} \in [0,1]$.
86	
87	We aggregate signals via Reciprocal Rank Fusion~\citep{cormack2009reciprocal}:
88	\begin{equation}
89	  \text{RRF}(i) = \sum_{s=1}^{S} \frac{1}{k + \text{rank}_s(i)}
90	  \label{eq:rrf}
91	\end{equation}
92	where $\text{rank}_s(i)$ is the rank of item $i$ under signal $s$ and $k=60$ is the standard smoothing constant.
93	RRF is parameter-free and avoids meta-circularity: a learned aggregator would require contamination labels for training, which may themselves be contaminated.
94	
95	The composite RRF score is normalized to $[0,1]$ to yield the exposure estimate $\hat{\tau}_i$.
96	
97	\subsection{Stage 2: Contamination-Augmented 4PL IRT}
98	\label{sec:stage2}
99	
100	\textbf{Standard 4PL.}
101	The four-parameter logistic IRT model defines the probability of model $j$ correctly answering item $i$ as:
102	\begin{equation}
103	  P(Y_{ij}=1 \mid \theta_j, \mathbf{w}_i) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i)\bigr)
104	  \label{eq:4pl}
105	\end{equation}
106	where $\theta_j$ is model ability, $a_i$ is item discrimination, $b_i$ is item difficulty, $c_i$ is guessing, $d_i$ is slip, and $\sigma(\cdot)$ is the logistic function.
107	
108	\textbf{Contamination augmentation.}
109	We introduce per-benchmark contamination parameters $\gamma_k$ ($k$ indexes benchmarks) that modulate the effect of exposure:
110	\begin{equation}
111	  P(Y_{ij}=1 \mid \theta_j, \mathbf{w}_i, \gamma_k, \tau_{ij}) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j + \gamma_k \tau_{ij} - b_i)\bigr)
112	  \label{eq:contamcal}
113	\end{equation}
114	where $\tau_{ij}$ is the latent exposure of model $j$ to item $i$ and $\gamma_k > 0$ quantifies the contamination inflation effect on benchmark $k$.
115	The calibrated ability is $\theta_j$ (contamination effect subtracted out), and the calibrated score is computed by setting $\tau_{ij}=0$ in Eq.~\ref{eq:contamcal}.
116	
117	\textbf{Measurement error model.}
118	Stage~1 exposure estimates $\hat{\tau}_{ij}$ are noisy observations of the latent exposure $\tau_{ij}$:
119	\begin{equation}
120	  \hat{\tau}_{ij} \sim \mathcal{N}(\tau_{ij}, \sigma_e^2)
121	  \label{eq:measurement}
122	\end{equation}
123	where $\sigma_e$ is estimated from the data.
124	This propagates Stage~1 uncertainty into the posteriors of $\theta_j$ and $\gamma_k$, producing wider credible intervals when detection signals are noisy (e.g., under RL post-training, $\hat{\sigma}_e = 0.28$) and tighter intervals when signals are clean (SFT, $\hat{\sigma}_e = 0.12$).
125	Without this model, credible interval coverage degrades from 93\% to 83\% at the 95\% nominal level.
126	
127	\textbf{Three structural adaptations from educational IRT.}
128	(a)~Independent examinees $\to$ single model with joint item distribution: responses are correlated through shared model parameters, altering local independence semantics.
129	We fit IRT per-benchmark to reduce correlation scope and empirically verify via posterior predictive checks (residual correlations $\leq 0.09$).
130	(b)~Binary leakage $\to$ continuous exposure scores: standard in explanatory IRT~\citep{deboeck2004explanatory} but requires the measurement error model (Eq.~\ref{eq:measurement}).
131	(c)~Stable ability $\to$ regime-conditional ability: SFT and RL regimes require different signal selections due to differential signal survival (\S\ref{sec:signal_survival}).
132	
133	\textbf{Inference.}
134	We use Hamiltonian Monte Carlo (4 chains, 2000 warmup, 2000 sampling) with weakly informative priors: $\gamma_k \sim \text{HalfNormal}(0.5)$, $\theta_j \sim \mathcal{N}(0,1)$, $a_i \sim \text{LogNormal}(0,0.5)$.
135	Convergence is assessed via $\hat{R} < 1.01$ and effective sample size $> 400$.
136	
137	% ===========================================================================
138	\section{Experimental Setup}
139	\label{sec:setup}
140	
141	\subsection{Controlled Contamination Injection}
142	\label{sec:injection}
143	
144	We construct a controlled contamination testbed using Qwen2.5 at three scales (0.5B, 1.5B, 3B) with 5 dosage levels (0\%, 5\%, 25\%, 50\%, 100\%) $\times$ 3 random seeds = 45 SFT runs.
145	A 72B-Instruct model generates paraphrases satisfying BLEU$<$0.3 and cosine similarity$>$0.85, ensuring lexical divergence while preserving semantic contamination.
146	The resulting paraphrases evade $n$-gram decontamination at 97.3\% rate, with mean cosine similarity 0.89 and mean BLEU 0.22.
147	
148	\subsection{Benchmarks and Baselines}
149	
150	\textbf{Benchmarks}: MMLU (14K items), GSM8K ($\sim$1.3K items), ARC-Challenge, and HumanEval (164 items).
151	
152	\textbf{Baselines} (7): (0)~Raw (no adjustment), (1)~Remove-and-rescore, (2)~Single-signal 2PL+$\gamma$, (3)~Vanilla 4PL (no contamination covariate), (4)~Linear exposure regression + bootstrap CI, (5a)~Emperor rephrasing, (5b)~Emperor shuffling, (6)~DCR fuzzy inference.
153	
154	\subsection{Evaluation Metrics}
155	(1)~Calibration MAE (pp) between calibrated and ground-truth clean accuracy;
156	(2)~Credible interval coverage at 50\%/80\%/95\% nominal levels;
157	(3)~Interval sharpness (CI width);
158	(4)~Ranking preservation (Kendall's $\tau$);
159	(5)~Dose-response monotonicity ($R^2$).
160	
161	% ===========================================================================
162	\section{Results}
163	\label{sec:results}
164	
165	\subsection{Contamination Inflation}
166	\label{sec:inflation}
167	
168	Table~\ref{tab:inflation} reports contamination-induced inflation across benchmarks, dosage levels, and model scales.
169	Inflation increases monotonically with dosage: from 1.8\,pp at 5\% to 14.3\,pp at 100\% on MMLU.
170	At 100\% dosage, GSM8K inflates by 11.7\,pp, ARC by 12.4\,pp, and HumanEval by 8.9\,pp.
171	Cross-seed standard deviation is only 0.6\,pp, indicating high reproducibility.
172	The scale effect ratio (3B vs.\ 0.5B) is 1.15$\times$, confirming scale is secondary to dosage.
173	All inflation values at 5\%+ dosage are statistically significant ($p<0.05$; $p<0.001$ for 25\%+).
174	
175	\begin{table}[t]
176	\centering
177	\caption{Contamination inflation (pp) by benchmark and dosage at 100\%. Cross-scale mean $\pm$ std across 3 seeds.}
178	\label{tab:inflation}
179	\begin{tabular}{lcccc}
180	\toprule
181	Dosage & MMLU & GSM8K & ARC & HumanEval \\
182	\midrule
183	0\%   & $0.0 \pm 0.0$ & $0.0 \pm 0.0$ & $0.0 \pm 0.0$ & $0.0 \pm 0.0$ \\
184	5\%   & $1.8 \pm 0.6$ & --- & --- & --- \\
185	25\%  & $5.2 \pm 0.6$ & --- & --- & --- \\
186	50\%  & $9.1 \pm 0.6$ & --- & --- & --- \\
187	100\% & $14.3 \pm 0.6$ & $11.7 \pm 0.6$ & $12.4 \pm 0.6$ & $8.9 \pm 0.6$ \\
188	\bottomrule
189	\end{tabular}
190	\end{table}
191	
192	\subsection{Stage 1: Detection Signals}
193	\label{sec:signals}
194	
195	Table~\ref{tab:signals} reports per-signal AUC for distinguishing contaminated from clean items.
196	Embedding retrieval achieves the highest AUC (0.88 at 100\% dosage), followed by Min-K\%++ (0.84), ConStat (0.81), and Self-Critique (0.77).
197	Signal ranking is consistent across model scales (rank correlation = 0.91).
198	All signals degrade at lower dosages: at 5\%, the best signal (embedding) achieves AUC=0.71, while the weakest (Self-Critique) drops to 0.59.
199	
200	\begin{table}[t]
201	\centering
202	\caption{Per-signal AUC for contamination detection (SFT regime).}
203	\label{tab:signals}
204	\begin{tabular}{lccc}
205	\toprule
206	Signal & 5\% dose & 25\% dose & 100\% dose \\
207	\midrule
208	Embedding Retrieval & 0.71 & 0.82 & 0.88 \\
209	Min-K\%++           & 0.64 & 0.76 & 0.84 \\
210	ConStat             & 0.62 & 0.74 & 0.81 \\
211	Self-Critique       & 0.59 & 0.70 & 0.77 \\
212	\bottomrule
213	\end{tabular}
214	\end{table}
215	
216	\subsection{RRF Aggregation}
217	\label{sec:rrf}
218	
219	Table~\ref{tab:rrf} compares aggregation methods.
220	RRF composite achieves AUC=0.92 at 100\% dosage, outperforming rank averaging (0.89, $\Delta$=0.03) and the best single signal (0.88, $\Delta$=0.04).
221	Calibration-weighted RRF (0.91) slightly \emph{underperforms} standard RRF, supporting the meta-circularity argument: learned weights introduce circular dependency with contamination labels.
222	RRF is robust to false positive injection (AUC=0.89 at 10\% FP, 0.85 at 20\% FP).
223	A 2-signal mode (ConStat + Self-Critique only, for closed-weight models) achieves AUC=0.83.
224	
225	\begin{table}[t]
226	\centering
227	\caption{Aggregation method comparison (SFT regime, AUC).}
228	\label{tab:rrf}
229	\begin{tabular}{lccc}
230	\toprule
231	Method & 5\% dose & 25\% dose & 100\% dose \\
232	\midrule
233	RRF (4 signals)      & 0.78 & 0.85 & 0.92 \\
234	Rank Averaging        & ---  & ---  & 0.89 \\
235	Cal-Weighted RRF      & ---  & ---  & 0.91 \\
236	Best Single Signal    & 0.71 & 0.82 & 0.88 \\
237	2-Signal Mode         & ---  & ---  & 0.83 \\
238	\bottomrule
239	\end{tabular}
240	\end{table}
241	
242	\subsection{Identifiability Analysis}
243	\label{sec:identifiability}
244	
245	We conduct a 144-condition simulation sweep: 6 AUC levels $\times$ 4 model counts ($N$) $\times$ 3 priors $\times$ 2 exposure types, with 10 seeds each (Table~\ref{tab:identifiability}).
246	
247	\textbf{Practical identifiability boundary.}
248	At AUC$\geq$0.70 and $N\geq$50, $\gamma$ recovery RMSE = 0.06--0.09, with 95\% credible intervals excluding zero in 94\% of runs.
249	Below AUC=0.55, CI excludes zero in only 48\% of runs --- the ``cannot distinguish'' zone.
250	
251	\textbf{Fisher Information analysis.}
252	The Fisher Information for $\gamma$ is $I(\gamma) \propto N \cdot \text{AUC}^2 / (1-\text{AUC}^2)$.
253	The analytical threshold (AUC=0.68) closely matches the empirical practical boundary ($\sim$0.70), providing theoretical grounding.
254	Structural identifiability (mathematical uniqueness) holds down to AUC=0.58, but estimation precision is insufficient for decisions below the practical boundary.
255	
256	\textbf{Posterior correlation.}
257	$\theta$--$\gamma$ posterior correlation is $-0.18$ at AUC=0.70, decreasing to $-0.07$ at AUC=0.90 --- mild and not sufficient to cause identifiability failure.
258	
259	\textbf{Coverage.}
260	At AUC$\geq$0.70 / $N\geq$50: 93\% coverage at 95\% nominal, 82\% at 80\% nominal.
261	Prior sensitivity is minimal at $N\geq$50 (RMSE range = 0.02 across 3 priors).
262	Growing Pains pre-estimation improves RMSE by 0.04 at $N=20$.
263	Overall convergence rate: 98.6\% across all 144 conditions.
264	
265	\begin{table}[t]
266	\centering
267	\caption{$\gamma$ recovery RMSE and 95\% CI coverage across AUC and $N_{\text{models}}$. Practical identifiability boundary at AUC$\approx$0.68--0.70.}
268	\label{tab:identifiability}
269	\begin{tabular}{lcccc}
270	\toprule
271	 & \multicolumn{2}{c}{$N=20$} & \multicolumn{2}{c}{$N=50$} \\
272	\cmidrule(lr){2-3}\cmidrule(lr){4-5}
273	AUC & RMSE & Cov.\ 95\% & RMSE & Cov.\ 95\% \\
274	\midrule
275	0.55 & --- & 48\% & 0.21 & 78\% \\
276	0.60 & --- & 72\% & --- & --- \\
277	0.70 & --- & --- & 0.09 & 94\% \\
278	0.80 & --- & --- & 0.06 & 93\% \\
279	\bottomrule
280	\end{tabular}
281	\vspace{-2mm}
282	\end{table}
283	
284	\begin{table}[t]
285	\centering
286	\caption{Fisher Information thresholds vs.\ empirical simulation boundaries.}
287	\label{tab:fisher}
288	\begin{tabular}{lcc}
289	\toprule
290	Boundary Type & Fisher Analytical & Empirical \\
291	\midrule
292	Structural identifiability & --- & AUC = 0.58 \\
293	Practical identifiability  & AUC = 0.68 & AUC $\approx$ 0.70 \\
294	$N_{\text{models}}$ threshold & 35 & $\sim$35--50 \\
295	\bottomrule
296	\end{tabular}
297	\end{table}
298	
299	\subsection{Noise Propagation and Measurement Error}
300	\label{sec:noise}
301	
302	Table~\ref{tab:coverage_noise} compares credible interval coverage with and without the measurement error model.
303	
304	Without measurement error modeling, 95\% coverage degrades to 83\% (12\,pp below nominal) because point-estimate exposures freeze Stage~1 uncertainty.
305	The measurement error model restores coverage to 93\%.
306	CI width increases from 1.8\,pp to 3.1\,pp (SFT) --- the cost of honest uncertainty.
307	In RL regimes, $\hat{\sigma}_e = 0.28$ (vs.\ 0.12 for SFT), yielding appropriately wider CIs of 7.2\,pp.
308	Post-hoc noise injection at $2\times$ independently validates this correction (coverage = 93\%).
309	Bias is nearly unchanged (0.04 $\to$ 0.05) --- the model improves precision without sacrificing accuracy.
310	
311	\begin{table}[t]
312	\centering
313	\caption{Coverage comparison: point estimate vs.\ measurement error model.}
314	\label{tab:coverage_noise}
315	\begin{tabular}{lccc}
316	\toprule
317	 & \multicolumn{2}{c}{Coverage} & CI Width \\
318	\cmidrule(lr){2-3}
319	Method & 80\% nom. & 95\% nom. & (SFT, pp) \\
320	\midrule
321	Point estimate      & 69\% & 83\% & 1.8 \\
322	Measurement error   & 81\% & 93\% & 3.1 \\
323	Post-hoc $2\times$  & ---  & 93\% & --- \\
324	\bottomrule
325	\end{tabular}
326	\end{table}
327	
328	\subsection{Main Calibration Results}
329	\label{sec:calibration}
330	
331	Table~\ref{tab:main} presents the central result: ContamCal per-benchmark $\gamma_k$ vs.\ 7 baselines across 4 benchmarks.
332	
333	\textbf{Calibration error.}
334	ContamCal achieves average MAE = 1.5\,pp across benchmarks (MMLU: 1.2, GSM8K: 1.5, ARC: 1.4, HumanEval: 1.9\,pp), compared to 11.2\,pp for raw scores.
335	It significantly outperforms all 7 baselines ($p < 0.05$ for all pairwise comparisons).
336	The closest competitor, DCR, achieves 3.4\,pp MAE --- ContamCal improves by 1.9\,pp ($p = 0.003$).
337	
338	\textbf{Per-benchmark $\gamma_k$.}
339	Contamination effects are heterogeneous: $\gamma_k = 0.42$ for MMLU (knowledge-intensive), 0.35 for GSM8K, 0.38 for ARC, and 0.28 for HumanEval (code generation).
340	All four $\gamma_k$ CIs exclude zero, validating per-benchmark modeling.
341	The global $\gamma$ variant yields higher MAE (2.1\,pp) with degraded coverage (88\%), confirming that benchmark heterogeneity matters.
342	
343	\textbf{Coverage and sharpness.}
344	95\% coverage = 93\%, 80\% coverage = 81\%, 50\% coverage = 52\% --- all near nominal.
345	Average CI width = 3.1\,pp (SFT regime).
346	
347	\textbf{Ranking and dose-response.}
348	Kendall's $\tau$ = 0.96, indicating near-perfect ranking preservation.
349	Dose-response is strictly monotonic with $R^2 = 0.97$.
350	
351	\begin{table}[t]
352	\centering
353	\caption{Calibration MAE (pp) --- ContamCal vs.\ baselines. $\dagger$: $p < 0.05$, $\ddagger$: $p < 0.01$ vs.\ ContamCal (per-$\gamma_k$). Std across seeds.}
354	\label{tab:main}
355	\begin{tabular}{lccccc}
356	\toprule
357	Method & MMLU & GSM8K & ARC & HEval & Avg \\
358	\midrule
359	\textbf{ContamCal} (per-$\gamma_k$) & \textbf{1.2} & \textbf{1.5} & \textbf{1.4} & \textbf{1.9} & \textbf{1.5} \\
360	ContamCal (global $\gamma$)  & 1.8 & 2.2 & 2.0 & 2.4 & 2.1$^\dagger$ \\
361	DCR$^\ddagger$               & 2.8 & 3.5 & 3.4 & 3.9 & 3.4 \\
362	Single-sig.\ 2PL+$\gamma^\ddagger$  & 3.3 & 4.0 & 3.8 & 4.5 & 3.9 \\
363	Linear regression$^\ddagger$ & 3.6 & 4.3 & 4.1 & 4.8 & 4.2 \\
364	Remove-rescore$^\ddagger$    & 5.8 & 7.0 & 6.5 & 7.9 & 6.8 \\
365	Emperor rephrase$^\ddagger$  & 6.1 & 7.3 & 7.0 & 8.0 & 7.1 \\
366	Vanilla 4PL$^\ddagger$       & 7.2 & 8.6 & 8.2 & 9.6 & 8.4 \\
367	Emperor shuffle$^\ddagger$   & 8.1 & 9.5 & 9.0 & 10.6 & 9.3 \\
368	Raw$^\ddagger$               & 9.8 & 11.5 & 11.0 & 12.5 & 11.2 \\
369	\bottomrule
370	\end{tabular}
371	\end{table}
372	
373	\begin{table}[t]
374	\centering
375	\caption{Coverage and sharpness (ContamCal per-$\gamma_k$, SFT regime).}
376	\label{tab:coverage_main}
377	\begin{tabular}{lcccc}
378	\toprule
379	Metric & MMLU & GSM8K & ARC & HEval \\
380	\midrule
381	Coverage (95\%) & 94\% & 93\% & 93\% & 92\% \\
382	Coverage (80\%) & 82\% & 81\% & 81\% & 80\% \\
383	Coverage (50\%) & 53\% & 52\% & 52\% & 51\% \\
384	CI width (pp)   & 2.8  & 3.1  & 3.0  & 3.5  \\
385	\bottomrule
386	\end{tabular}
387	\end{table}
388	
389	\begin{table}[t]
390	\centering
391	\caption{Per-benchmark $\gamma_k$ estimates (ContamCal, SFT controlled data).}
392	\label{tab:gamma}
393	\begin{tabular}{lccc}
394	\toprule
395	Benchmark & $\gamma_k$ & 95\% CI & Excl.\ zero? \\
396	\midrule
397	MMLU      & 0.42 & [0.31, 0.54] & Yes \\
398	GSM8K     & 0.35 & [0.22, 0.49] & Yes \\
399	ARC       & 0.38 & [0.25, 0.52] & Yes \\
400	HumanEval & 0.28 & [0.11, 0.47] & Yes \\
401	\bottomrule
402	\end{tabular}
403	\end{table}
404	
405	\subsection{Scale Bridging: 7B Validation}
406	\label{sec:scale7b}
407	
408	To verify scalability beyond the 0.5B--3B training-efficient regime, we run controlled SFT injection on Qwen2.5-7B (Table~\ref{tab:scale7b}).
409	ContamCal achieves MAE = 1.6\,pp (vs.\ 1.5\,pp at smaller scales, gap = 0.1\,pp, not statistically significant), with 92\% coverage at 95\% nominal.
410	MMLU inflation at 100\% is 15.1\,pp (slightly higher than smaller models due to increased memorization capacity), yet $\gamma_k$(MMLU) = 0.44 --- naturally absorbed by the per-benchmark parameterization.
411	Kendall's $\tau$ with smaller models = 0.95.
412	
413	\begin{table}[t]
414	\centering
415	\caption{Scale bridging: 0.5B--3B (pooled) vs.\ 7B.}
416	\label{tab:scale7b}
417	\begin{tabular}{lcccc}
418	\toprule
419	Scale & MAE (pp) & Cov.\ 95\% & CI width & $\gamma_k$(MMLU) \\
420	\midrule
421	0.5B--3B & 1.5 & 93\% & 3.1\,pp & 0.42 \\
422	7B       & 1.6 & 92\% & 3.3\,pp & 0.44 \\
423	\bottomrule
424	\end{tabular}
425	\end{table}
426	
427	\subsection{Signal Survival Under RL Post-Training}
428	\label{sec:signal_survival}
429	
430	Table~\ref{tab:survival} presents the signal$\times$regime AUC heatmap --- the core of Contribution~2.
431	
432	\textbf{Cliff-like degradation.}
433	Embedding retrieval and Min-K\%++ achieve AUC 0.88 and 0.84 in SFT-contaminated regime but collapse to 0.54 and 0.51 (near chance) after RL post-training.
434	The transition is abrupt: cliff sharpness indices are 0.95 (embedding) and 0.92 (Min-K\%++), with onset at epoch~2 of RL training.
435	The mechanism: RL (GRPO) optimizes behavioral reward, erasing the logit/embedding fingerprints of SFT-stage contamination.
436	
437	\textbf{Meta-cognitive survival.}
438	Self-Critique partially survives RL (AUC = 0.65), as meta-cognitive signals (``have you seen this?'') are not directly optimized by reward-based RL.
439	ConStat shows moderate survival (AUC = 0.58).
440	The signal$\times$regime interaction is highly significant ($p < 0.001$): signal rankings qualitatively reverse between SFT and RL regimes.
441	
442	\begin{table}[t]
443	\centering
444	\caption{Signal $\times$ regime AUC heatmap. Bold: above identifiability threshold (0.65).}
445	\label{tab:survival}
446	\begin{tabular}{lcccc}
447	\toprule
448	Signal & Base & SFT-clean & SFT-contam & RL-post \\
449	\midrule
450	Embedding    & 0.55 & 0.57 & \textbf{0.88} & 0.54 \\
451	Min-K\%++    & 0.52 & 0.53 & \textbf{0.84} & 0.51 \\
452	ConStat      & 0.51 & 0.52 & \textbf{0.81} & 0.58 \\
453	Self-Critique & 0.50 & 0.51 & \textbf{0.77} & \textbf{0.65} \\
454	\bottomrule
455	\end{tabular}
456	\end{table}
457	
458	\subsection{Multi-Family Validation}
459	\label{sec:multifamily}
460	
461	Table~\ref{tab:family} validates ContamCal across model families.
462	Llama-3.2-1B achieves MAE = 1.7\,pp (coverage 91\%), Pythia-1.4B achieves MAE = 1.8\,pp (coverage 90\%).
463	The MAE gap vs.\ Qwen is 0.3\,pp --- not statistically significant.
464	$\gamma_k$(MMLU) values (Llama: 0.39, Pythia: 0.37) are consistent with Qwen (0.42), indicating architecture-agnostic contamination modeling.
465	Identifiability boundaries (AUC $\approx$ 0.70) hold across all families.
466	
467	\begin{table}[t]
468	\centering
469	\caption{Multi-family calibration at matched scale ($\sim$1.5B).}
470	\label{tab:family}
471	\begin{tabular}{lcccc}
472	\toprule
473	Family & MAE (pp) & Cov.\ 95\% & $\gamma_k$(MMLU) & $\tau$ \\
474	\midrule
475	Qwen2.5-1.5B  & 1.5 & 93\% & 0.42 & 0.96 \\
476	Llama-3.2-1B  & 1.7 & 91\% & 0.39 & 0.94 \\
477	Pythia-1.4B   & 1.8 & 90\% & 0.37 & 0.94 \\
478	\bottomrule
479	\end{tabular}
480	\end{table}
481	
482	\subsection{RL Observational Case Study}
483	\label{sec:rl_case}
484	
485	Table~\ref{tab:rl_gamma} reports $\gamma$ estimates for RL-trained models.
486	Point estimates are positive but moderate (0.15--0.22 for MMLU), with wide CIs reflecting genuine epistemic uncertainty ($\text{avg width} = 7.8$\,pp).
487	Coverage remains at 91\% (using held-out clean benchmark as ground truth, avoiding circularity).
488	
489	\textbf{Specificity check.}
490	On a known-clean benchmark (LiveBench recent items), $\gamma = 0.02$ with CI including zero --- ContamCal does not hallucinate contamination on clean data.
491	
492	\textbf{Expected regret.}
493	Table~\ref{tab:regret} quantifies model selection regret.
494	Uncalibrated top-5 selection incurs 40\% regret (selecting wrong models due to inflated scores).
495	ContamCal reduces regret to 10\%, compared to 25\% for remove-and-rescore.
496	Ground truth is held-out clean benchmark scores, not calibrated scores.
497	
498	\begin{table}[t]
499	\centering
500	\caption{$\gamma$ estimates for RL-trained models (MMLU).}
501	\label{tab:rl_gamma}
502	\begin{tabular}{lcc}
503	\toprule
504	Model & $\gamma$(MMLU) & CI width (pp) \\
505	\midrule
506	Qwen2.5-Instruct-3B  & 0.18 & 7.8 \\
507	Qwen2.5-Instruct-7B  & 0.22 & 7.8 \\
508	DeepSeek-R1-Distill-7B & 0.15 & 7.8 \\
509	\midrule
510	Clean benchmark (neg.\ control) & 0.02 & --- \\
511	\bottomrule
512	\end{tabular}
513	\end{table}
514	
515	\begin{table}[t]
516	\centering
517	\caption{Top-$K$ model selection regret (\%).}
518	\label{tab:regret}
519	\begin{tabular}{lccc}
520	\toprule
521	Method & $K=3$ & $K=5$ & $K=10$ \\
522	\midrule
523	Uncalibrated     & --- & 40\% & --- \\
524	Remove-rescore   & --- & 25\% & --- \\
525	ContamCal        & --- & 10\% & --- \\
526	\bottomrule
527	\end{tabular}
528	\end{table}
529	
530	\subsection{72B Observational Analysis}
531	\label{sec:72b}
532	
533	Qwen2.5-72B inference-only analysis extends ecological validity to frontier scale (Table~\ref{tab:72b}).
534	$\gamma$(MMLU) = 0.25 with CI [0.08, 0.43] suggests $\sim$5.8\,pp score overestimation, but wide CI (8.5\,pp) reflects that (1)~only one model exists at this scale, and (2)~RL post-training degrades signals.
535	Self-Critique AUC = 0.62 (at the identifiability boundary) --- 72B's stronger meta-cognition partially compensates for RL signal degradation.
536	This result provides ecological validity at frontier scale, not quantitative precision.
537	
538	\begin{table}[t]
539	\centering
540	\caption{72B observational results (MMLU).}
541	\label{tab:72b}
542	\begin{tabular}{lccc}
543	\toprule
544	& $\gamma$(MMLU) & 95\% CI & Calib.\ shift (pp) \\
545	\midrule
546	Qwen2.5-72B & 0.25 & [0.08, 0.43] & 5.8 \\
547	\bottomrule
548	\end{tabular}
549	\end{table}
550	
551	\subsection{Closed-Weight 2-Signal Mode}
552	\label{sec:2signal}
553	
554	For closed-weight models (GPT-4, Claude) where logits and embeddings are unavailable, ContamCal operates in a degraded 2-signal mode using ConStat + Self-Critique only (Table~\ref{tab:2signal}).
555	This mode achieves MAE = 2.4\,pp (vs.\ 1.5\,pp for 4-signal, gap = 0.9\,pp) with 90\% coverage at 95\% nominal and CI width = 4.8\,pp.
556	Despite the degradation, 2-signal mode still outperforms all baselines including DCR (3.4\,pp), demonstrating that the IRT structure provides value beyond signal quality alone.
557	
558	\begin{table}[t]
559	\centering
560	\caption{4-signal vs.\ 2-signal (closed-weight) mode comparison.}
561	\label{tab:2signal}
562	\begin{tabular}{lccc}
563	\toprule
564	Mode & MAE (pp) & Cov.\ 95\% & CI width (pp) \\
565	\midrule
566	4-signal (full) & 1.5 & 93\% & 3.1 \\
567	2-signal (closed) & 2.4 & 90\% & 4.8 \\
568	\midrule
569	DCR (baseline) & 3.4 & --- & --- \\
570	\bottomrule
571	\end{tabular}
572	\end{table}
573	
574	% ===========================================================================
575	\section{Discussion}
576	\label{sec:discussion}
577	
578	\textbf{Wide CIs are the correct answer.}
579	Under RL post-training, ContamCal produces CIs of 7--8\,pp width.
580	This is not a limitation but an honest reflection of epistemic uncertainty: when detection signals degrade, the calibrated estimate should carry wider uncertainty.
581	A method that produces narrow CIs despite noisy inputs would be miscalibrated.
582	
583	\textbf{Local independence.}
584	Standard IRT assumes independent examinees, but a single LLM produces all item responses.
585	Our per-benchmark fitting reduces correlation scope, and posterior predictive checks show residual correlations $\leq$0.09.
586	The measurement error model partially compensates by widening CIs.
587	
588	\textbf{Limitations.}
589	(1)~Controlled SFT injection is the best-available proxy but may not capture all real-world contamination mechanisms.
590	(2)~The 72B observational analysis involves $N=1$ at that scale, limiting precision.
591	(3)~HumanEval's small item count ($N=164$) increases estimation uncertainty ($\gamma_k$ CI width is widest).
592	(4)~We do not evaluate on instruction-following benchmarks (e.g., MT-Bench) where contamination dynamics may differ.
593	
594	% ===========================================================================
595	\section{Conclusion}
596	\label{sec:conclusion}
597	
598	ContamCal shifts the paradigm from contamination elimination to contamination calibration.
599	By fusing multiple detection signals via parameter-free RRF and fitting a contamination-augmented 4PL IRT model with measurement error propagation, it recovers true benchmark performance within 1.5\,pp MAE with near-nominal credible interval coverage (93\% at 95\% level), significantly outperforming all 7 baselines including DCR.
600	Our signal survival analysis reveals cliff-like degradation of logit-based signals under RL, while meta-cognitive signals survive --- a finding with immediate practical implications for the detection community.
601	Fisher Information-grounded identifiability bounds (AUC$\geq$0.68) provide theoretical assurance for when calibration can and cannot be trusted.
602	ContamCal is a statistical safety net: it does not fix benchmark contamination, but it tells you how much it matters.
603	
604	% ===========================================================================
605	{\small
606	\bibliographystyle{plainnat}
607	
608	\begin{thebibliography}{30}
609	
610	\bibitem[Adams et~al.(1997)]{adams1997multidimensional}
611	Adams, R.~J., Wilson, M., and Wang, W.
612	\newblock The multidimensional random coefficients multinomial logit model.
613	\newblock \emph{Applied Psychological Measurement}, 21(1):1--23, 1997.
614	
615	\bibitem[Burnell et~al.(2023)]{burnell2023rethink}
616	Burnell, R., Schellaert, W., Burden, J., et~al.
617	\newblock Rethink reporting of evaluation results in {AI}.
618	\newblock \emph{Science}, 380(6641):136--138, 2023.
619	
620	\bibitem[Cormack et~al.(2009)]{cormack2009reciprocal}
621	Cormack, G.~V., Clarke, C.~L., and Buettcher, S.
622	\newblock Reciprocal rank fusion outperforms condorcet and individual rank learning methods.
623	\newblock In \emph{SIGIR}, pp.~758--759, 2009.
624	
625	\bibitem[De~Boeck and Wilson(2004)]{deboeck2004explanatory}
626	De~Boeck, P. and Wilson, M.
627	\newblock \emph{Explanatory Item Response Models}.
628	\newblock Springer, 2004.
629	
630	\bibitem[Dekoninck et~al.(2024a)]{dekoninck2024constat}
631	Dekoninck, J., Müller, M., Fischer, M., and Vechev, M.
632	\newblock {ConStat}: Performance-based contamination detection in large language models.
633	\newblock In \emph{NeurIPS}, 2024.
634	
635	\bibitem[Dekoninck et~al.(2024b)]{dekoninck2024evading}
636	Dekoninck, J., Müller, M., Fischer, M., and Vechev, M.
637	\newblock Evading data contamination detection for language models is (too) easy.
638	\newblock \emph{arXiv:2402.02823}, 2024.
639	
640	\bibitem[Eckerly(2017)]{eckerly2017detecting}
641	Eckerly, C.~A.
642	\newblock Detecting item compromise in educational testing: A comparison of methods.
643	\newblock PhD thesis, University of Iowa, 2017.
644	
645	\bibitem[Golchin and Surdeanu(2024)]{golchin2024time}
646	Golchin, S. and Surdeanu, M.
647	\newblock Time travel in {LLMs}: Tracing data contamination in large language models.
648	\newblock In \emph{ICLR}, 2024.
649	
650	\bibitem[Lalor et~al.(2024)]{lalor2024benchmarking}
651	Lalor, J.~P., Yang, Y., Smith, K., Forsythe, N., and Ji, H.
652	\newblock Benchmarking large language models on {CMExam} --- a comprehensive {Chinese} medical exam dataset.
653	\newblock In \emph{AAAI}, 2024.
654	
655	\bibitem[Maris and Bechger(2009)]{maris2009equivalence}
656	Maris, G. and Bechger, T.
657	\newblock On interpreting the model parameters for the three parameter logistic model.
658	\newblock \emph{Measurement}, 7(2):75--88, 2009.
659	
660	\bibitem[Martinez et~al.(2024)]{martinez2024item}
661	Martinez, R.~D., et~al.
662	\newblock Item response theory for {AI} evaluation.
663	\newblock \emph{arXiv:2401.07133}, 2024.
664	
665	\bibitem[Mislevy(1986)]{mislevy1986bayes}
666	Mislevy, R.~J.
667	\newblock Bayes modal estimation in item response models.
668	\newblock \emph{Psychometrika}, 51(2):177--195, 1986.
669	
670	\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}
671	Polo, F.~M., Weber, L., Choshen, L., Sun, Y., Xu, G., and Yurochkin, M.
672	\newblock {tinyBenchmarks}: evaluating {LLMs} with fewer examples.
673	\newblock In \emph{ICML}, 2024.
674	
675	\bibitem[Rosenbaum and Rubin(1983)]{rosenbaum1983central}
676	Rosenbaum, P.~R. and Rubin, D.~B.
677	\newblock The central role of the propensity score in observational studies for causal effects.
678	\newblock \emph{Biometrika}, 70(1):41--55, 1983.
679	
680	\bibitem[San~Mart\'in et~al.(2009)]{sanmartin2009identifiability}
681	San~Mart\'in, E., Gonzalez, J., and Tuerlinckx, F.
682	\newblock On the identifiability of the fixed-effects 3{PL} model.
683	\newblock \emph{Psychometrika}, 74:293--312, 2009.
684	
685	\bibitem[Sinharay(2017)]{sinharay2017detection}
686	Sinharay, S.
687	\newblock Detection of item preknowledge using likelihood-ratio test and score test.
688	\newblock \emph{Journal of Educational and Behavioral Statistics}, 42(1):46--68, 2017.
689	
690	\bibitem[Talts et~al.(2018)]{talts2018sbc}
691	Talts, S., Betancourt, M., Simpson, D., Vehtari, A., and Gelman, A.
692	\newblock Validating {Bayesian} inference algorithms with simulation-based calibration.
693	\newblock \emph{arXiv:1804.06788}, 2018.
694	
695	\bibitem[Wentzel et~al.(2024)]{wentzel2024selfcritique}
696	Wentzel, J., et~al.
697	\newblock Self-critique for benchmark contamination detection.
698	\newblock \emph{arXiv:2406.12345}, 2024.
699	
700	\bibitem[White et~al.(2024)]{white2024livebench}
701	White, C., Dooley, S., Roberts, M., Pal, A., Feuer, B., et~al.
702	\newblock {LiveBench}: A challenging, contamination-free {LLM} benchmark.
703	\newblock \emph{arXiv:2406.19314}, 2024.
704	
705	\bibitem[Xu et~al.(2025)]{xu2025emperor}
706	Xu, R., et~al.
707	\newblock Benchmarking benchmark leakage in large language models.
708	\newblock In \emph{ICML}, 2025.
709	
710	\bibitem[Yang et~al.(2023)]{yang2023rethinking}
711	Yang, S., Chiang, W.-L., Zheng, L., Gonzalez, J.~E., and Stoica, I.
712	\newblock Rethinking benchmark and contamination for language models with rephrased samples.
713	\newblock \emph{arXiv:2311.04850}, 2023.
714	
715	\bibitem[Yang et~al.(2025)]{yang2025dcr}
716	Yang, S., et~al.
717	\newblock {DCR}: Decontaminated calibration and re-evaluation for benchmark integrity.
718	\newblock In \emph{EMNLP}, 2025.
719	
720	\bibitem[Zhang et~al.(2024)]{zhang2024minkpp}
721	Zhang, J., Li, J., Xiao, C., et~al.
722	\newblock Min-{K}\%++: Improved baseline for detecting pre-training data from large language models.
723	\newblock In \emph{ICLR}, 2024.
724	
725	\end{thebibliography}
726	}
727	
728	\end{document}
729	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c076644-9ecd-4f49-8162-842b9960cffc",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "b8e2edb1-5cdf-44c2-9cc1-ebf765c77bce",
  "sourceToolAssistantUUID": "3c076644-9ecd-4f49-8162-842b9960cffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-13T18:04:32.829Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YFBWtEY7KRSqWeUhEvJmzp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8e2edb1-5cdf-44c2-9cc1-ebf765c77bce",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11XMaLMZTzgRtZaLUM2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34dea097-a6b0-48ec-82df-17afd80e26c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPVgbaMF28YLmVDJcqq2tV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3213,
      "cache_read_input_tokens": 26737,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3213
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 26737,
          "cache_creation_input_tokens": 3213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3213,
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

_source line 32 · 2026-05-13T18:04:32.850Z_

<details><summary>↩ Tool result · `toolu_01YFBWtEY7KRSqWeUhEvJmzp`</summary>

```text
1	% EMNLP 2026 ARR submission — acl_latex template
2	% Download style files: https://github.com/acl-org/acl-style-files
3	\documentclass[11pt]{article}
4	% TODO: uncomment when acl2023.sty is placed in this directory
5	% \usepackage[hyperref]{acl2023}
6	\usepackage{times}
7	\usepackage[hyphens]{url}
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb,amsfonts}
10	\usepackage{natbib}
11	\usepackage{booktabs}
12	\usepackage[margin=1in]{geometry}
13	\usepackage{xcolor}
14	\usepackage{microtype}
15	\usepackage{hyperref}
16	
17	\title{ContamCal: Post-Hoc Calibration of Benchmark Scores\\
18	under Training Data Contamination via\\
19	Contamination-Augmented Item Response Theory}
20	
21	\author{Anonymous ARR Submission}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\textbf{TODO: Abstract to be written after experiments.}
28	\end{abstract}
29	
30	\input{introduction}
31	
32	\input{related_work}
33	
34	\input{method}
35	
36	% TODO: Experiments, Results, Discussion, Conclusion
37	
38	% TODO: switch to acl_natbib when style file is in place
39	\bibliographystyle{plainnat}
40	\bibliography{references}
41	
42	\end{document}
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34dea097-a6b0-48ec-82df-17afd80e26c8",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "b67f6cab-0bf5-44d7-a953-ccc1efda7aba",
  "sourceToolAssistantUUID": "34dea097-a6b0-48ec-82df-17afd80e26c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-13T18:04:36.651Z_

Now let me read the related work and method sections from the paper draft, and also check the dream review reports.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b67f6cab-0bf5-44d7-a953-ccc1efda7aba",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11Xq25izRGsPdBfdv2V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67c66305-56bc-4e03-94e5-d7410838be70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CX5ZRwRMpJcvbN6sB7pX3n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15511,
      "cache_read_input_tokens": 29950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15511,
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

_source line 34 · 2026-05-13T18:04:38.652Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T1XwjZwBUpGnpXC47RZ3s8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67c66305-56bc-4e03-94e5-d7410838be70",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11Xq25izRGsPdBfdv2V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea0c818d-f509-4f2d-95a5-245198e5b6a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CX5ZRwRMpJcvbN6sB7pX3n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15511,
      "cache_read_input_tokens": 29950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15511,
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

_source line 35 · 2026-05-13T18:04:38.679Z_

<details><summary>↩ Tool result · `toolu_01T1XwjZwBUpGnpXC47RZ3s8`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Benchmark Contamination Detection}
5	\label{sec:related:detection}
6	
7	Detecting training data contamination in LLMs has produced a diverse methodological landscape spanning at least eight paradigms. Time-based partitioning uses temporal cutoffs to identify potentially leaked items, while canary string insertion (e.g., BIG-Bench) provides direct memorization probes \citep{chang2025benchmarking}. Min-K\%++ \citep{duan2025minkpp} performs membership inference by examining token-level probability distributions, achieving strong detection on pre-training contamination. Time Travel \citep{oren2024proving} uses guided completion to detect black-box contamination without model weight access. ConStat \citep{dekoninck2024constat} measures performance gaps between original and paraphrased benchmark items, targeting surface-form memorization. Self-Critique \citep{wust2025selfcritique} identifies contamination through entropy collapse in model self-evaluations---a signal that, unlike probability-based methods, partially survives reinforcement learning post-training. Hierarchical semantic detection approaches match items at multiple granularity levels to training corpora. KDS \citep{xu2025kds} uses knowledge distillation signatures to achieve near-perfect detection (Spearman $\rho = 0.99$) but requires per-model LoRA fine-tuning, limiting scalability.
8	
9	A critical finding is that detection methods are fragile under RL post-training: \citet{wang2025fragility} show that GRPO and similar procedures degrade probability-based detection signals substantially, while Self-Critique's entropy-based signal achieves only 0.60--0.70 AUC on RL-trained models \citep{wust2025selfcritique}. Despite this rich detection toolkit, all existing methods produce binary or continuous \emph{flags}---they diagnose contamination without prescribing how to adjust the reported accuracy that end-users rely on.
10	
11	\subsection{Contamination Impact and Mitigation}
12	\label{sec:related:mitigation}
13	
14	Understanding contamination's quantitative impact has advanced rapidly. \citet{dong2026dose} establish dose-response curves showing that score inflation scales monotonically with both model size and contamination dosage. \citet{yang2026rl} further demonstrate that SFT inflates accuracy only on contaminated tasks, while GRPO amplifies inflation even on structurally similar uncontaminated items---a cross-contamination effect that complicates attribution. \citet{zhang2025forget} show that contamination persists in model weights following standard decontamination, with forgetting curves following scaling laws that make complete removal impractical.
15	
16	The mitigation landscape is equally sobering. \citet{xu2025emperor} systematically evaluate twenty strategies---item rephrasing, option shuffling, filtering, dynamic benchmark construction, and more---across ten LLMs and five benchmarks, finding that none reliably eliminates contamination effects. Dynamic benchmarks such as LiveBench \citep{white2024livebench} circumvent contamination by generating fresh items but cannot retroactively calibrate existing benchmark scores. Inference-Time Decontamination \citep{yang2024inference} rewrites items at test time but operates during inference rather than producing post-hoc calibrated scores. DCR \citep{li2025dcr} is the closest existing method to ours, producing adjusted accuracy via fuzzy inference over detection signals; however, it provides point estimates without uncertainty bounds and does not address signal degradation under RL. \citet{rao2026silicon} propose a router-worker audit framework that produces contamination flags rather than calibrated scores. Collectively, these findings motivate a paradigm shift: from contamination \emph{prevention}---which demonstrably fails---to post-hoc statistical \emph{adjustment} with proper uncertainty quantification.
17	
18	\subsection{IRT for LLM Evaluation}
19	\label{sec:related:irt}
20	
21	Item response theory has gained traction as a principled framework for LLM evaluation. \citet{lalor2024irt} demonstrate that IRT-based evaluation yields more informative model comparisons than raw accuracy. PSN-IRT \citep{gu2026psnirt} scales this to 41,871 items across 11 benchmarks using a 4PL model with neural network parameter estimation, establishing item difficulty and discrimination profiles but without modeling contamination or producing adjusted scores. \citet{polo2026growing} fit multidimensional 2PL IRT with anchor items to over 400 models, validating IRT's applicability at scale while identifying practical limitations in the few-examinee regime; contamination is not addressed. ATLAS \citep{lyu2025atlas} leverages IRT for adaptive testing, reducing evaluation cost through maximally informative item selection. TinyBenchmarks \citep{polo2024tinybenchmarks} similarly exploits IRT-informed item selection for efficient evaluation. HiBayES \citep{zhuang2025hibayes} provides hierarchical Bayesian credible intervals over model ability estimates but treats all items as equally trustworthy. \citet{han2026probing} quantify contamination effects within psychometric evaluations but do not use IRT or produce calibrated scores. Across this body of work, contamination has not been modeled as a covariate within the IRT framework---a gap that ContamCal addresses by augmenting the item response function with exposure parameters.
22	
23	\subsection{Item Compromise in Educational Measurement}
24	\label{sec:related:edumeasure}
25	
26	The psychometric literature has long addressed item compromise---the unauthorized disclosure of test content prior to administration. \citet{eckerly2017} develops IRT models that incorporate compromise indicators to simultaneously estimate item parameters and compromise effects, while \citet{sinharay2017} proposes likelihood ratio and score tests for detecting item preknowledge. The explanatory IRT tradition \citep{deboeck2004,adams1997} provides the theoretical foundation for embedding external covariates within item response functions, and \citet{mislevy1986} establishes Bayesian estimation procedures for such augmented models.
27	
28	Adapting this tradition to LLM evaluation requires three non-trivial structural modifications---from independent examinees to shared-parameter models, from binary leakage to continuous noisy exposure, and from stable ability to regime-conditional behavior---detailed in \S\ref{sec:stage2}.
29	
30	\paragraph{Positioning.} ContamCal bridges contamination detection (which flags but does not calibrate), IRT-based LLM evaluation (which models ability but ignores contamination), and educational item compromise models (which handle leaked items but assume independent examinees with binary exposure). Table~\ref{tab:positioning} summarizes the capabilities of representative methods.
31	
32	\begin{table}[t]
33	\centering
34	\small
35	\begin{tabular}{lcccc}
36	\toprule
37	\textbf{Method} & \textbf{Detects} & \textbf{Calibrates} & \textbf{UQ} & \textbf{RL-robust} \\
38	\midrule
39	Min-K\%++ & \checkmark & & & \\
40	ConStat & \checkmark & & & \\
41	Self-Critique & \checkmark & & & \checkmark \\
42	KDS & \checkmark & & & ? \\
43	DCR & \checkmark & \checkmark & & \\
44	PSN-IRT & & & & \\
45	HiBayES & & & \checkmark & \\
46	\textbf{ContamCal} & \checkmark & \checkmark & \checkmark & \checkmark \\
47	\bottomrule
48	\end{tabular}
49	\caption{Capability comparison of contamination-aware evaluation methods. UQ = uncertainty quantification via credible intervals. RL-robust = maintains effectiveness after RL post-training.}
50	\label{tab:positioning}
51	\end{table}
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea0c818d-f509-4f2d-95a5-245198e5b6a4",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "24e9ad0b-3c38-42d1-bec0-1680094e0a4f",
  "sourceToolAssistantUUID": "ea0c818d-f509-4f2d-95a5-245198e5b6a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-13T18:04:39.087Z_

<details open><summary>🔧 Tool call — Read · `toolu_012CGCo1vgYuk2TPFirnRyrw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24e9ad0b-3c38-42d1-bec0-1680094e0a4f",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11Xq25izRGsPdBfdv2V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "531a6ade-6b30-4908-9e43-29826bf56fee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CX5ZRwRMpJcvbN6sB7pX3n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15511,
      "cache_read_input_tokens": 29950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15511,
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

_source line 37 · 2026-05-13T18:04:39.237Z_

<details><summary>↩ Tool result · `toolu_012CGCo1vgYuk2TPFirnRyrw`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages. Stage~1 (\S\ref{sec:stage1}) estimates per-item contamination exposure by fusing multiple detection signals into a single score. Stage~2 (\S\ref{sec:stage2}--\S\ref{sec:calibrated}) embeds these scores as covariates in a contamination-augmented IRT model, performing Bayesian inference to produce calibrated benchmark scores with credible intervals.
5	
6	\subsection{Stage 1: Multi-Signal Provenance Mapping}
7	\label{sec:stage1}
8	
9	For each model~$i$ and benchmark item~$j$, we compute four complementary detection signals that capture different facets of contamination evidence.
10	
11	\paragraph{Embedding-based near-duplicate retrieval.}
12	We embed both training corpus segments and benchmark items using a sentence transformer encoder and build a FAISS index over training embeddings for efficient retrieval. The signal $s_1(i,j)$ is the maximum cosine similarity between item~$j$ and the top-$K$ retrieved training segments for model~$i$'s training corpus, capturing semantic overlap that survives paraphrasing and surface-level reformulation.
13	
14	\paragraph{Min-K\%++ membership inference.}
15	Following \citet{duan2025minkpp}, we compute the average log-probability of the $k\%$ least-likely tokens in each benchmark item under model~$i$, z-scored against a reference (clean) model. Contaminated items yield systematically higher (less negative) Min-K\%++ scores, as the model assigns elevated probability to tokens it has memorized during training. The signal $s_2(i,j)$ is the resulting membership inference statistic. We use a simplified variant that z-normalizes per-item against a single reference model's mean and standard deviation, rather than the per-token z-scoring of the original formulation; since the downstream RRF aggregation operates on ranks rather than raw scores, this simplification preserves signal ordering while reducing computational cost.
16	
17	\paragraph{ConStat performance gap.}
18	For each benchmark item, we generate a semantically equivalent paraphrased variant using an independent rewriter model. The signal $s_3(i,j)$ is the accuracy gap between model~$i$'s performance on the original item versus its paraphrased counterpart \citep{dekoninck2024constat}. A model that has memorized the original surface form but genuinely understands the underlying concept should perform comparably on both versions; a large gap indicates surface-level memorization rather than robust capability.
19	
20	\paragraph{Self-Critique entropy collapse.}
21	When model~$i$ is prompted to evaluate the correctness of its own response to item~$j$, contaminated items elicit low-entropy self-evaluation distributions---the model exhibits overconfidence in its assessment of memorized content \citep{wust2025selfcritique}. The signal $s_4(i,j)$ is the negative entropy of the self-critique distribution. This signal is particularly valuable because it operates at the meta-cognitive level and exhibits greater robustness to RL post-training than signals relying on token-level statistics (\S\ref{sec:signal_survival}).
22	
23	\paragraph{Signal survival analysis.}
24	\label{sec:signal_survival}
25	Prior work suggests that detection signals do not degrade uniformly across training regimes. \citet{wang2025fragility} demonstrate that RL post-training with GRPO substantially degrades probability-based detection signals (Min-K\%++, ConStat), while entropy-based approaches such as Self-Critique retain greater robustness by exploiting policy collapse rather than probability gaps. This motivates our inclusion of Self-Critique alongside probability-based signals: if the signal~$\times$~regime interaction is confirmed in our controlled experiments, it has two practical consequences. First, exposure estimates for RL-trained models would carry higher uncertainty, which the measurement error model in Stage~2 propagates into appropriately wider credible intervals. Second, a cliff-like (rather than gradual) degradation pattern would imply that RL fundamentally restructures the model's relationship to memorized content, rather than merely attenuating detection signals. We systematically evaluate signal survival across training regimes in \S\ref{sec:experiments}.% TODO: fill in quantitative AUC values from exp-008 results
26	
27	\paragraph{RRF aggregation.}
28	We aggregate the four signals via reciprocal rank fusion \citep{cormack2009}. For each model~$i$, items are ranked independently by each signal~$s$, and the fused exposure score is:
29	\begin{equation}
30	\label{eq:rrf}
31	    e_{ij} = \sum_{s=1}^{4} \frac{1}{k + r_{s,i}(j)},
32	\end{equation}
33	where $r_{s,i}(j)$ is the rank of item~$j$ under signal~$s$ for model~$i$, and $k = 60$ is the standard RRF smoothing constant. RRF is a deliberate design choice over learned aggregation (\emph{e.g.}, logistic regression over signal scores). A learned aggregator requires labeled training data indicating which items are truly contaminated---but ground-truth contamination labels are precisely what we lack, and the aggregator's training data may itself be contaminated, creating meta-circularity. RRF avoids this by requiring no training, providing a robust, parameter-free fusion baseline.
34	
35	We note that KDS \citep{xu2025kds} provides a complementary detection signal based on knowledge distillation signatures, but requires per-model LoRA fine-tuning at $O(N^2)$ computational cost. We include KDS in ablation experiments but exclude it from the default pipeline for scalability.
36	
37	\subsection{Stage 2: Contamination-Augmented 4PL IRT}
38	\label{sec:stage2}
39	
40	\paragraph{Model specification.}
41	We augment the standard four-parameter logistic (4PL) IRT model \citep{lord1980} with a contamination covariate. The probability that model~$i$ correctly answers item~$j$ is:
42	\begin{equation}
43	\label{eq:4pl}
44	    P(y_{ij} = 1 \mid \boldsymbol{\psi}) = c_j + (d_j - c_j)\,\sigma\!\bigl(a_j(\theta_i - b_j) + \gamma \cdot \tau_{ij}\bigr),
45	\end{equation}
46	where $\sigma(\cdot)$ denotes the logistic function, $y_{ij} \in \{0,1\}$ is the binary response, and $\boldsymbol{\psi}$ collects all parameters. The standard IRT parameters are: $\theta_i \in \mathbb{R}$ (ability of model~$i$), $a_j > 0$ (discrimination of item~$j$), $b_j \in \mathbb{R}$ (difficulty of item~$j$), $c_j \in [0,1]$ (guessing/lower asymptote), and $d_j \in [0,1]$ (upper asymptote/slip parameter). The contamination-specific parameters are: $\gamma \in \mathbb{R}$ (global contamination effect) and $\tau_{ij} \geq 0$ (latent true exposure of model~$i$ to item~$j$).
47	
48	The additive structure $a_j(\theta_i - b_j) + \gamma \cdot \tau_{ij}$ admits a natural interpretation: contamination exposure shifts the effective ability of a model on a given item by $\gamma \cdot \tau_{ij} / a_j$ units on the ability scale. When $\tau_{ij} = 0$ (no contamination), Eq.~\eqref{eq:4pl} reduces to the standard 4PL model. A positive~$\gamma$ indicates that contamination inflates performance, as expected.
49	
50	\paragraph{Measurement error model.}
51	The latent exposure $\tau_{ij}$ is not directly observed; we observe the noisy RRF-derived estimate $e_{ij}$ from Stage~1. We model this relationship as:
52	\begin{equation}
53	\label{eq:measurement_error}
54	    \tau_{ij} \sim \mathcal{N}(e_{ij},\, \sigma_e^2),
55	\end{equation}
56	where $\sigma_e^2$ is the measurement error variance, estimated jointly with other model parameters. This formulation treats the observed exposure scores as noisy proxies for latent contamination and has two critical consequences. First, uncertainty in the detection signals is automatically propagated into the posterior over ability~$\theta_i$ and contamination effect~$\gamma$, yielding appropriately wider credible intervals when signals are unreliable. Second, under RL post-training---where signal degradation is severe (\S\ref{sec:signal_survival})---the posterior distribution of~$\tau_{ij}$ becomes more diffuse, producing wider credible intervals that honestly reflect our reduced ability to distinguish contaminated from clean items.
57	
58	\paragraph{Prior specification.}
59	We assign the following priors:
60	\begin{align}
61	    \theta_i &\sim \mathcal{N}(0, 1), \label{eq:prior_theta} \\
62	    a_j &\sim \text{LogNormal}(0, 0.5), \label{eq:prior_a} \\
63	    b_j &\sim \mathcal{N}(0, 1), \label{eq:prior_b} \\
64	    c_j &\sim \text{Beta}(5, 20), \label{eq:prior_c} \\
65	    d_j &\sim \text{Beta}(20, 5), \label{eq:prior_d} \\
66	    \gamma &\sim \mathcal{N}(0, 1). \label{eq:prior_gamma}
67	\end{align}
68	The $\text{Beta}(5, 20)$ prior on~$c_j$ encodes the expectation that guessing rates are low (mean $\approx 0.2$) but non-negligible for multiple-choice items. The $\text{Beta}(20, 5)$ prior on~$d_j$ reflects the expectation that upper asymptotes are high (mean $\approx 0.8$) but not necessarily unity, allowing for careless errors or ambiguous items. The $\text{LogNormal}(0, 0.5)$ prior on~$a_j$ constrains discrimination to be positive with moderate magnitude (median $= 1$). The weakly informative $\mathcal{N}(0, 1)$ prior on~$\gamma$ permits both positive and negative contamination effects; we conduct sensitivity analyses under $\mathcal{N}(0, 0.5)$ and $\mathcal{N}(0, 2)$ to assess robustness to this specification (\S\ref{sec:experiments}).
69	
70	\paragraph{Connection to item compromise IRT.}
71	Equation~\eqref{eq:4pl} extends the item compromise IRT tradition \citep{eckerly2017,sinharay2017} with three structural adaptations for the LLM evaluation setting.
72	
73	\emph{Adaptation~1: Independent examinees $\to$ shared item pool.} In educational testing, each examinee independently samples from a population ability distribution. In LLM evaluation, a single model responds to all items, and its responses are correlated through shared model parameters. This alters the local independence assumption: conditional on~$\theta_i$, item responses within a single model may remain correlated through model-specific idiosyncrasies not captured by the scalar ability parameter \citep{mislevy1986,sanmartin2009}. We mitigate this by fitting IRT models per-benchmark---reducing the scope of potential violations---and empirically assessing residual correlations via posterior predictive checks (\S\ref{sec:experiments}).
74	
75	\emph{Adaptation~2: Binary leakage $\to$ continuous exposure.} Classical item compromise models use binary indicators $e_{ij} \in \{0, 1\}$ \citep{sinharay2017}. We generalize to continuous exposure scores $\tau_{ij} \in \mathbb{R}^+$ derived from noisy detection signals, which is standard in explanatory IRT \citep{deboeck2004} but necessitates the measurement error formulation of Eq.~\eqref{eq:measurement_error} to prevent attenuation bias from regression dilution \citep{maris2009}.
76	
77	\emph{Adaptation~3: Stable ability $\to$ regime-conditional ability.} An examinee's ability is typically assumed stable across test items. For LLMs, the training regime (SFT vs.\ RL) qualitatively changes both the model's ability profile and the reliability of detection signals. We handle this through the signal survival analysis (\S\ref{sec:signal_survival}), which informs the measurement error variance, rather than through regime-specific ability parameters---preserving model parsimony while acknowledging regime effects through the uncertainty channel.
78	
79	\subsection{Bayesian Inference}
80	\label{sec:inference}
81	
82	We perform full Bayesian inference using the No-U-Turn Sampler \citep[NUTS;][]{hoffman2014} implemented in CmdStanPy \citep{carpenter2017}. We run four independent Markov chains and assess convergence via three diagnostics: split-$\hat{R} < 1.01$ for all parameters, effective sample size $\text{ESS} > 400$ per parameter, and fewer than 0.1\% divergent transitions. The target acceptance probability is set to $\texttt{adapt\_delta} = 0.95$ to reduce divergences in the high-curvature posterior geometry induced by the 4PL model's bounded response function.
83	
84	\paragraph{Per-benchmark fitting.}
85	Rather than fitting a single IRT model jointly across all benchmarks, we fit separate models per benchmark. This design choice reduces the scope of local independence violations: within a single benchmark, items share a common knowledge domain, making the conditional independence assumption more defensible than across heterogeneous benchmarks encompassing knowledge recall, mathematical reasoning, and code generation \citep{sanmartin2009}. Per-benchmark fitting also naturally yields benchmark-specific contamination effects~$\gamma_k$ (\S\ref{sec:calibrated}), the primary specification in our framework.
86	
87	\paragraph{Few-examinee regime.}
88	Standard IRT applications assume large examinee populations ($N > 200$), but current LLM evaluation studies may include as few as 20--50 models. In this low-$N$ regime, item parameter estimation becomes unstable without informative priors. We address this by incorporating empirical Bayes priors for item parameters derived from the Growing Pains study \citep{polo2026growing}, which provides item parameter estimates from a pool of 400+ models. Specifically, the item difficulty and discrimination priors are centered at the Growing Pains point estimates with moderately inflated variances, serving as a regularizing anchor while permitting data-driven updating. We validate this prior transfer procedure via simulation-based calibration \citep[SBC;][]{talts2018sbc}, confirming that posteriors are well-calibrated under the specified priors across a range of sample sizes (\S\ref{sec:experiments}). Automatic differentiation variational inference \citep[ADVI;][]{ulitzsch2022} is explored as a scalability option for larger item pools in the appendix, though preliminary results indicate ADVI may fail to converge for the 4PL specification due to the bounded response function's multimodal posterior geometry; we include the comparison for completeness.
89	
90	\subsection{Calibrated Score Computation}
91	\label{sec:calibrated}
92	
93	Given the posterior distribution over all parameters, we compute the calibrated (decontaminated) accuracy for model~$i$ on benchmark~$B$ by setting exposure to zero and marginalizing over posterior uncertainty:
94	\begin{equation}
95	\label{eq:calibrated}
96	    \text{Acc}_{i}^{\text{cal}} = \frac{1}{|B|} \sum_{j \in B}\, \mathbb{E}_{\boldsymbol{\psi} \sim p(\boldsymbol{\psi} \mid \mathbf{y})} \!\left[ c_j + (d_j - c_j)\,\sigma\!\bigl(a_j(\theta_i - b_j)\bigr) \right],
97	\end{equation}
98	where the expectation is taken over posterior draws of~$\boldsymbol{\psi}$ and the contamination term $\gamma \cdot \tau_{ij}$ has been removed. This counterfactual quantity answers: \emph{what would model~$i$'s expected accuracy be on benchmark~$B$ had it never been exposed to any test items during training?}
99	
100	In practice, we approximate Eq.~\eqref{eq:calibrated} by averaging over $L$ posterior draws $\{\boldsymbol{\psi}^{(\ell)}\}_{\ell=1}^{L}$:
101	\begin{equation}
102	\label{eq:calibrated_mc}
103	    \widehat{\text{Acc}}_{i}^{\text{cal}} = \frac{1}{L} \sum_{\ell=1}^{L} \frac{1}{|B|} \sum_{j \in B} \left[ c_j^{(\ell)} + (d_j^{(\ell)} - c_j^{(\ell)})\,\sigma\!\bigl(a_j^{(\ell)}(\theta_i^{(\ell)} - b_j^{(\ell)})\bigr) \right].
104	\end{equation}
105	Credible intervals at level~$\alpha$ are obtained from the empirical quantiles of $\{\text{Acc}_{i}^{\text{cal},(\ell)}\}_{\ell=1}^{L}$. We report 50\%, 80\%, and 95\% intervals. By construction, models with higher exposure scores and noisier detection signals---whose $\tau_{ij}$ posteriors are more diffuse---receive wider credible intervals, encoding the principle that calibration is only as reliable as its inputs.
106	
107	\paragraph{Per-benchmark contamination effects.}
108	Since we fit independent models per benchmark (\S\ref{sec:inference}), each benchmark naturally yields its own contamination effect parameter~$\gamma_k$:
109	\begin{equation}
110	\label{eq:per_benchmark_gamma}
111	    P(y_{ij} = 1 \mid \boldsymbol{\psi}_k) = c_j + (d_j - c_j)\,\sigma\!\bigl(a_j(\theta_i - b_j) + \gamma_k \cdot \tau_{ij}\bigr),
112	\end{equation}
113	where $\gamma_k$ is the contamination effect specific to benchmark~$k$, with independent priors $\gamma_k \sim \mathcal{N}(0, 1)$. This is the primary specification, permitting heterogeneous contamination effects across benchmarks---for instance, knowledge-intensive benchmarks (MMLU) may exhibit larger contamination inflation than multi-step reasoning benchmarks (GSM8K). As an ablation, we also fit a joint model across all benchmarks with a shared global~$\gamma$ to test whether the contamination effect is homogeneous (\S\ref{sec:experiments}).
114	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "531a6ade-6b30-4908-9e43-29826bf56fee",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "ede84bf2-a1b5-4a37-b9bd-ac0a13f0efb1",
  "sourceToolAssistantUUID": "531a6ade-6b30-4908-9e43-29826bf56fee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-13T18:04:39.553Z_

<details open><summary>🔧 Tool call — Read · `toolu_016em8FCzbUsJ9T9YGa8KniE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ede84bf2-a1b5-4a37-b9bd-ac0a13f0efb1",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11Xq25izRGsPdBfdv2V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58f04e20-1501-4b06-ab6d-7ce8972f0590",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CX5ZRwRMpJcvbN6sB7pX3n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15511,
      "cache_read_input_tokens": 29950,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15511
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 29950,
          "cache_creation_input_tokens": 15511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15511,
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

_source line 39 · 2026-05-13T18:04:39.568Z_

<details><summary>↩ Tool result · `toolu_016em8FCzbUsJ9T9YGa8KniE`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Large language model (LLM) evaluation increasingly relies on standardized benchmarks to compare models and track progress, yet mounting evidence reveals that these benchmarks are systematically compromised by training data contamination \citep{chang2025benchmarking}. \citet{yang2026rl} demonstrate that rephrased benchmark items appearing in training corpora inflate MMLU accuracy by 8--15 percentage points while evading standard $n$-gram decontamination, and that reinforcement learning (RL) post-training with GRPO further amplifies contamination-driven gains while simultaneously concealing the detection signals that would reveal them. Dose-response analyses confirm a monotonic relationship between contamination exposure and score inflation, with effects persisting across model scales \citep{dong2026dose}. Even minor perturbations to benchmark item surface forms---which should not affect genuinely capable models---produce substantial accuracy drops, questioning the validity of reported scores \citep{wang2025fragility}. Together, these findings point to a reliability crisis in LLM evaluation: reported benchmark scores increasingly conflate memorization with generalizable capability \citep{rao2026silicon}.
5	
6	Several methods have been developed to detect benchmark contamination. Min-K\%++ \citep{duan2025minkpp} and Time Travel \citep{oren2024proving} perform membership inference against pre-training corpora; ConStat \citep{dekoninck2024constat} measures performance gaps between original and paraphrased items; Self-Critique \citep{wust2025selfcritique} identifies memorization through entropy collapse in model self-evaluations; and KDS \citep{xu2025kds} uses knowledge distillation signatures to flag leaked items. While these methods can detect contamination, none produces calibrated benchmark scores that answer the central evaluation question: \emph{what would this model's accuracy be had it never seen the test data?} On the psychometric side, item response theory (IRT) has been increasingly applied to LLM evaluation. PSN-IRT \citep{gu2026psnirt} models item difficulty and discrimination but does not account for contamination. \citet{polo2026growing} validate IRT at the scale of 400+ models yet treat all items as equally trustworthy. ATLAS \citep{lyu2025atlas} and \citet{lalor2024irt} further develop IRT-based evaluation without contamination modeling, and TinyBenchmarks \citep{polo2024tinybenchmarks} demonstrates that carefully selected item subsets can approximate full benchmark scores, but again without contamination awareness. HiBayES \citep{zhuang2025hibayes} provides hierarchical Bayesian uncertainty quantification but ignores item compromise. Inference-time decontamination \citep{yang2024inference} and targeted probing \citep{han2026probing} attempt to adjust or detect contamination effects at evaluation time, but neither produces fully calibrated scores with uncertainty quantification. The closest predecessor, DCR \citep{li2025dcr}, provides adjusted accuracy through fuzzy inference over detection signals but offers no uncertainty bounds and does not address the systematic signal degradation under RL post-training that we document in this work.
7	
8	The case for post-hoc calibration rests on a sobering empirical finding: contamination prevention does not work. \citet{xu2025emperor} systematically evaluate twenty mitigation strategies---including item rephrasing, option shuffling, filtering, and dynamic benchmark construction---and find that none reliably eliminates contamination effects across models and benchmarks. \citet{zhang2025forget} further demonstrate that standard decontamination procedures fail to fully remove memorized content from model weights. While dynamic benchmarks such as LiveBench \citep{white2024livebench} sidestep contamination by continuously generating new items, and efficient evaluation via item subsampling \citep{polo2024tinybenchmarks} can mitigate item-specific biases, neither approach provides calibrated scores for existing contaminated benchmarks. These findings motivate a paradigm shift from contamination \emph{elimination} to contamination \emph{adjustment}: rather than attempting to remove a confounder that resists removal, we measure it and statistically control for it. The analogy to observational causal inference is instructive---when randomization is infeasible, valid estimates are obtained not by eliminating confounders but by measuring and adjusting for them under clearly stated assumptions. ContamCal instantiates this ``statistical safety net'' philosophy for benchmark evaluation.
9	
10	Our approach is grounded in educational measurement's longstanding treatment of item compromise---the leaking of test content to examinees prior to administration. Item compromise IRT models \citep{eckerly2017,sinharay2017} incorporate exposure indicators as covariates within the item response function, enabling joint estimation of compromise effects alongside standard item and person parameters. Explanatory IRT \citep{deboeck2004,adams1997} provides the broader theoretical framework for embedding external covariates in item response models. Adapting this psychometric tradition to LLM evaluation requires three non-trivial structural modifications. First, whereas educational IRT assumes independent examinees, LLM evaluation involves individual models producing all responses to a shared item pool, fundamentally altering local independence semantics \citep{mislevy1986}. Second, binary leakage indicators (compromised vs.\ uncompromised) must be replaced with continuous exposure scores derived from noisy, imperfect detection signals---necessitating a measurement error model that propagates detection uncertainty into ability estimates. Third, stable examinee ability must give way to regime-conditional ability, as models undergoing supervised fine-tuning (SFT) versus RL post-training exhibit qualitatively different contamination signatures that affect both detection signal reliability and contamination effect magnitude.
11	
12	We propose ContamCal, a two-stage post-hoc calibration framework for contamination-adjusted benchmark scoring. In Stage~1 (\emph{Multi-Signal Provenance Mapping}), four training-free detection signals---embedding-based near-duplicate retrieval, Min-K\%++ membership inference, ConStat performance gaps, and Self-Critique entropy collapse---are aggregated via reciprocal rank fusion \citep[RRF;][]{cormack2009} to produce per-item exposure scores. RRF is a deliberate design choice: a learned aggregator would face meta-circularity, as its own training data may be contaminated, precluding unbiased weight estimation. In Stage~2 (\emph{Contamination-Augmented 4PL IRT}), exposure scores enter a four-parameter logistic IRT model as covariates, with a global contamination effect parameter~$\gamma$ estimated jointly with item and ability parameters via Bayesian inference. A measurement error model treats the observed exposure scores as noisy proxies for latent contamination status, automatically propagating detection uncertainty into posterior estimates. Calibrated scores are obtained by setting exposure to zero and marginalizing over parameter uncertainty, producing point estimates with 50\%/80\%/95\% Bayesian credible intervals. Models trained via RL receive appropriately wider intervals, reflecting the genuine epistemic uncertainty that arises when detection signals are degraded.
13	
14	Our contributions are organized hierarchically. At the core: (1)~the ContamCal framework itself---a two-stage pipeline comprising RRF-based provenance mapping and contamination-augmented 4PL IRT with per-benchmark contamination effects and a measurement error model for exposure---that produces calibrated benchmark scores with Bayesian credible intervals; (2)~a signal survival analysis demonstrating that contamination detection signals degrade in a cliff-like, rather than gradual, manner under RL post-training, yielding a signal~$\times$~regime AUC mapping with practical implications for the detection community; and (3)~dual-track validation through controlled SFT contamination injection across multiple model scales (0.5B--7B) within the Qwen2.5 family (internal validity) combined with an ecological RL case study (external validity). Supporting these core contributions: (4)~a simulation identifiability study grounded in Fisher information analysis, with a 144-condition sweep establishing minimum signal quality and model count thresholds for reliable parameter recovery; and (5)~comprehensive evaluation against seven baselines using five quantitative metrics---calibration MAE, credible interval coverage, interval sharpness, ranking preservation (Kendall's~$\tau$), and dose-response monotonicity---with bootstrap confidence intervals on all comparisons.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58f04e20-1501-4b06-ab6d-7ce8972f0590",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "d1673d35-0d79-49bf-a6ec-598d67fcdb25",
  "sourceToolAssistantUUID": "58f04e20-1501-4b06-ab6d-7ce8972f0590",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-13T18:04:42.576Z_

Now let me also check the dream review reports from both rounds.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1673d35-0d79-49bf-a6ec-598d67fcdb25",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11YKxsNRRXGLVKCA343",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6323c4b6-921d-4d67-b137-0327556b6ba5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YHR1aPQ4SoMJFGYxFKMTN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9346,
      "cache_read_input_tokens": 45461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9346,
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

_source line 41 · 2026-05-13T18:04:45.042Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012juLc8kMmFqahXELTeJYDj`</summary>

```json
{
  "pattern": "**/dream_reports/**/review_report.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6323c4b6-921d-4d67-b137-0327556b6ba5",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11YKxsNRRXGLVKCA343",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63286abf-6c50-4e6c-b523-b3cc19430793",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YHR1aPQ4SoMJFGYxFKMTN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9346,
      "cache_read_input_tokens": 45461,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9346
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 45461,
          "cache_creation_input_tokens": 9346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9346,
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

_source line 42 · 2026-05-13T18:04:45.163Z_

<details><summary>↩ Tool result · `toolu_012juLc8kMmFqahXELTeJYDj`</summary>

```text
artifacts/dream_reports/dream_20260513T155040/best/review_report.md
artifacts/dream_reports/dream_20260513T155040/median/review_report.md
artifacts/dream_reports/dream_20260513T155040/worst/review_report.md
artifacts/dream_reports/dream_20260513T171200/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63286abf-6c50-4e6c-b523-b3cc19430793",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "8db7d8b8-c007-47b4-a731-c71996952df6",
  "sourceToolAssistantUUID": "63286abf-6c50-4e6c-b523-b3cc19430793",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-13T18:04:51.794Z_

<details open><summary>🔧 Tool call — Read · `toolu_013kb1TaH2h5LaKFnR9KiqPA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8db7d8b8-c007-47b4-a731-c71996952df6",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11YjQmcKzvQ7e4KeeZ5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2dcef7db-a730-40f0-be9e-349cb96ee138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THsUVBLBWtHPhr3Z2jXnJi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 227,
      "cache_read_input_tokens": 54807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 227,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 44 · 2026-05-13T18:04:51.810Z_

<details><summary>↩ Tool result · `toolu_013kb1TaH2h5LaKFnR9KiqPA`</summary>

```text
1	---
2	dream_id: dream_20260513T171200
3	tier: best
4	overall_score: weak reject
5	timestamp: 2026-05-13T18:01:12.992962+00:00
6	---
7	
8	
9	# Dream Review Report: ContamCal
10	
11	**Paper**: ContamCal: Calibrating LLM Benchmark Scores via Contamination-Augmented Item Response Theory
12	**Venue**: AAAI 2027 (using AAAI 2026 standards: acceptance rate 17.6%, 1-10 scale)
13	**Review Mode**: Full (2 Reviewers + Roundtable)
14	**Dream ID**: 20260513T171200
15	
16	---
17	
18	## Reviewer Assignments
19	
20	| Reviewer | Focus | Overall | Confidence |
21	|----------|-------|---------|------------|
22	| R1 | Methodology + Experiments | 3/10 | 4/5 |
23	| R2 | Novelty + Related Work | 5/10 | 4/5 |
24	
25	---
26	
27	## R1 Review: Methodology & Experiments
28	
29	### Summary
30	ContamCal proposes a two-stage framework (RRF signal fusion + contamination-augmented 4PL IRT with measurement error model) for calibrating contaminated LLM benchmark scores. The core model specification is sound and well-grounded in educational measurement. However, the paper presents 16 tables of results with multiple suspicious numerical patterns — uniform noise across benchmarks, identical CI widths across diverse models, and near-identical coverage across benchmarks with 85x difference in item count — suggesting the results are projected rather than empirically observed.
31	
32	### Strengths
33	**S1. Well-motivated problem and framing.** The shift from contamination elimination to calibration is compelling. The Emperor's New Clothes motivation (all 20 mitigation strategies fail) makes the case clearly. The "statistical safety net" framing is honest and defensible.
34	
35	**S2. Sound core model specification.** The contamination-augmented 4PL (Eq. 3) is a natural extension of item compromise IRT. The additive γ_k·τ_ij term in logit space is well-motivated. Per-benchmark γ_k is the correct parameterization.
36	
37	**S3. Measurement error model is architecturally necessary.** The formulation τ̂_ij ~ N(τ_ij, σ_e²) correctly treats Stage 1 output as noisy. The coverage improvement (83% → 93%) demonstrates necessity. Regime-dependent σ_e (0.12 SFT, 0.28 RL) is principled.
38	
39	**S4. Meta-circularity argument for RRF is sound.** The result that calibration-weighted RRF (0.91) slightly underperforms standard RRF (0.92) provides empirical support. Correctly positioned as design choice, not contribution.
40	
41	**S5. Comprehensive experimental design.** 12 experiments covering controlled injection, signal evaluation, aggregation ablation, identifiability simulation, noise propagation, 7 baselines, scale bridging, signal survival, multi-family, RL case study, 72B observational, and closed-weight mode. Dual-track validation is well-structured.
42	
43	**S6. Fisher Information provides theoretical grounding.** I(γ) ∝ N·AUC²/(1-AUC²) gives a closed-form basis for identifiability thresholds. The match between analytical (0.68) and empirical (~0.70) boundaries is reassuring.
44	
45	**S7. Signal survival finding is genuinely novel.** Cliff-like degradation of logit-based signals under RL with meta-cognitive survival, and the qualitative reversal of signal rankings between SFT and RL regimes, is striking.
46	
47	### Weaknesses
48	**W1. Suspiciously uniform noise patterns across tables (CRITICAL).** Multiple numerical patterns undermine credibility:
49	- Table 1: Cross-seed std is exactly 0.6 pp for every benchmark at every dosage. Real SFT with different item counts (MMLU 14K vs HumanEval 164) would produce variable noise.
50	- Table 13: All three RL models (Qwen-3B, Qwen-7B, DeepSeek-R1-7B) have identical CI width of 7.8 pp despite different architectures and scales. Bayesian posterior precision varies with model-specific signal quality and MCMC mixing.
51	- Table 8: Coverage is near-uniformly nominal across benchmarks (94/93/93/92% at 95% level) despite 85x item count difference. HumanEval (N=164) should show notably worse coverage than MMLU (N=14K).
52	
53	**W2. Selective reporting in several tables (CRITICAL).** Table 1 reports intermediate dosages (5/25/50%) only for MMLU — GSM8K, ARC, HumanEval show only 100%. If the experiment ran all 5 dosages on all 4 benchmarks (Section 4.1), why omit? This undermines the dose-response monotonicity claim (R²=0.97) since monotonicity is only shown for MMLU. Table 4 has many missing cells in what should be a fully computable 6×4 matrix from 144 simulation conditions. Table 14 reports regret only at K=5, not K=3 and K=10 as designed.
54	
55	**W3. Fisher Information derivation is missing.** The paper claims I(γ) ∝ N·AUC²/(1-AUC²) without proof. For a 4PL model with latent exposure, measurement error, and per-benchmark γ_k, the Fisher Information is non-trivial. Without the derivation, the analytical threshold AUC=0.68 cannot be verified.
56	
57	**W4. Three structural adaptations are overclaimed.** (a) Independent examinees → single model: per-benchmark fitting + residual check is pragmatic but not a solution. No formalization of what local independence means for a single model. (b) Binary → continuous exposure: standard in explanatory IRT (De Boeck & Wilson 2004). (c) Regime-conditional ability: reduces to using different signals for different regimes — an engineering decision, not modeling contribution.
58	
59	**W5. 72B analysis is internally inconsistent.** Self-Critique AUC=0.62 is below the paper's own practical identifiability threshold of AUC≥0.68. Reporting a 5.8pp calibrated shift from a model operating below your own identifiability boundary is misleading.
60	
61	**W6. Multi-family validation is thin.** Only 3 dosage levels (vs 5 for Qwen), single model per family at single scale (~1.5B). Insufficient to claim cross-family generalization.
62	
63	**W7. No figures.** Zero figures for a two-stage Bayesian pipeline with 12 experiments and 16 tables. Missing: pipeline overview, calibrated-vs-true scatter, signal-regime heatmap, dose-response curves, identifiability phase diagram.
64	
65	**W8. RL specificity check uses only one clean benchmark.** Near-zero γ=0.02 on LiveBench alone is insufficient. Multiple independent clean benchmarks needed.
66	
67	**W9. Prior choices lack demonstrated sensitivity analysis.** HalfNormal(0.5) on γ_k is informative (95% mass below 1.0). No posterior-prior sensitivity comparisons shown.
68	
69	### Questions for Authors
70	Q1. Derivation of I(γ) ∝ N·AUC²/(1-AUC²)? How does the measurement error model factor in, and what assumptions relate exposure noise to signal AUC?
71	
72	Q2. Why identical CI widths (7.8pp) in Table 13 across architecturally distinct RL models?
73	
74	Q3. Why omit intermediate dosages for GSM8K, ARC, HumanEval in Table 1?
75	
76	Q4. How is σ_e estimated? Jointly in the Bayesian model or fixed externally?
77	
78	Q5. How are per-benchmark θ estimates reconciled into a single calibrated ability for cross-benchmark model comparison?
79	
80	Q6. Computational cost of NUTS HMC on 14K MMLU items with measurement error?
81	
82	### Scores (R1)
83	- Soundness: 2/4
84	- Empirical Methodology: 1/4
85	- Clarity: 2/4
86	- **Overall: 3/10** (Reject)
87	- Confidence: 4/5
88	
89	---
90	
91	## R2 Review: Novelty & Related Work
92	
93	### Summary
94	ContamCal assembles four existing detection signals via an off-the-shelf fusion technique (RRF) and feeds them into a standard psychometric model (explanatory IRT with contamination covariate) using standard Bayesian inference. The novelty lies in the specific combination and application context rather than any individual methodological advance. The signal survival analysis under RL is the most genuinely novel empirical contribution, though it is descriptive rather than explanatory. The paper addresses an important problem competently but does not clear the novelty bar for AAAI at 17.6% acceptance.
95	
96	### Strengths
97	**S1. Problem framing fills a genuine gap.** The field has many detection methods and many IRT-based evaluation methods, but nothing bridging them into calibrated scores with UQ. The Emperor's New Clothes motivation is compelling.
98	
99	**S2. Signal survival analysis is genuinely novel.** The cliff-like (not gradual) degradation of logit-based signals under RL, with meta-cognitive survival and qualitative ranking reversal, is an important empirical finding with value beyond ContamCal for the detection community.
100	
101	**S3. Honest and mature treatment of limitations.** Wide CIs framed as honest uncertainty, RL case study framed as observational, transparent mapping of where calibration works and doesn't. Unusual and credibility-enhancing.
102	
103	**S4. Meta-circularity argument is intellectually honest.** Correctly identifies that a learned aggregator's training data may itself be contaminated. Stating RRF is a design choice, not a contribution, is rare honesty.
104	
105	**S5. Comprehensive baseline comparison.** Seven baselines including DCR (most directly comparable) with five evaluation metrics and bootstrap CIs exceeds typical evaluation thoroughness.
106	
107	### Weaknesses
108	**W1. Limited methodological novelty — fundamentally a synthesis paper.** Eq. 3 adds one linear contamination covariate to standard 4PL IRT (direct application of Eckerly 2017 / Sinharay 2017). RRF is off-the-shelf (Cormack et al. 2009). Measurement error model is classical errors-in-variables. Bayesian inference via Stan NUTS is routine. Each component is borrowed. The three structural adaptations are individually either standard or engineering decisions. For AAAI at 17.6%, synthesis papers need the combination to produce emergent value — unclear here.
109	
110	**W2. Causal inference analogy is suggestive but undeveloped.** No DAG, no formal identification argument for counterfactual θ*, no sensitivity analysis for unmeasured confounding (contamination channels undetected by all four signals). The analogy remains narrative framing, not formal methodology.
111	
112	**W3. Missing engagement with important related work areas.**
113	- **DIF literature** (Holland & Wainer 1993, Thissen et al. 1993): Direct statistical precursor — ContamCal essentially performs DIF between contaminated and clean subgroups
114	- **ML calibration** (Guo et al. 2017, Platt scaling): Must disambiguate "calibration" (decontamination vs probability calibration)
115	- **Conformal prediction** (Angelopoulos & Bates 2023): Alternative UQ with distribution-free coverage guarantees
116	- **Data attribution** (TracIn, TRAK): Alternative exposure estimation signals
117	- **Benchmark design** (HELM, BIG-bench, Open LLM Leaderboard): Broader evaluation ecosystem
118	- **Multidimensional IRT / CDMs**: Unidimensional θ assumption questionable for MMLU (57 subjects)
119	- **LMSYS / Chatbot Arena**: Contamination-resistant by design (live human evaluation)
120	
121	**W4. Signal survival analysis lacks mechanistic depth for a core contribution.** The degradation is documented but not explained mechanistically. No validation across different RL algorithms (PPO vs GRPO vs DPO), reward model architectures, or base model families. Generalizability of cliff-like pattern is asserted but not established.
122	
123	**W5. Paper does not adequately distinguish borrowed vs new.** A psychometrician would recognize Stage 2 as routine explanatory IRT. An IR researcher would recognize RRF as textbook. The paper should be explicit about where the intellectual contribution lies.
124	
125	**W6. Practical adoption barriers not discussed.** ContamCal requires 50+ models for identifiability, weight access for 2 of 4 signals, Stan infrastructure, and per-benchmark fitting. What practitioner population can actually use this?
126	
127	### Missing Related Work (specific gaps)
128	- DIF: Holland & Wainer (1993), Thissen et al. (1993), Zumbo (1999)
129	- ML calibration: Guo et al. (2017), Platt (1999), temperature scaling
130	- Conformal prediction: Angelopoulos & Bates (2023), Vovk et al. (2005)
131	- Data attribution: TracIn (Pruthi et al. 2020), TRAK (Park et al. 2023)
132	- Benchmark ecosystem: HELM (Liang et al. 2022), BIG-bench (Srivastava et al. 2023)
133	- Multidimensional IRT: Reckase (2009), de la Torre (2011)
134	- IRT identifiability: San Martín et al. (2009) — cited but not discussed in depth
135	- Contamination surveys: Balloccu et al. (2024), Jacovi et al. (2023)
136	- CDD: Oren et al. (2023) "Proving Test Set Contamination in Black Box Language Models"
137	
138	### Novelty Assessment (per contribution)
139	- **Contribution 1 (ContamCal framework)**: Incremental (2/4). Competent synthesis of existing components. No new technique — value is in the combination and application context.
140	- **Contribution 2 (Signal survival analysis)**: Moderate (3/4). Genuinely novel empirical finding with practical implications. Descriptive rather than explanatory. Extension of prior observations about RL fragility.
141	- **Contribution 3 (Dual-track validation)**: Low (1.5/4). Controlled injection is standard methodology. Observational RL case study is valuable but routine.
142	
143	### Scores (R2)
144	- Novelty: 2/4
145	- Significance: 3/4
146	- Related Work: 2/4
147	- **Overall: 5/10** (Borderline reject)
148	- Confidence: 4/5
149	
150	---
151	
152	## Roundtable
153	
154	### Step 2: Cross-Sharing
155	
156	**R1 → R2**: R1's identification of suspicious numerical patterns (uniform std in Table 1, identical CI widths in Table 13, near-identical coverage across benchmarks with vastly different item counts in Table 8) is compelling evidence that the results are projected rather than empirically observed. R2 agrees these patterns would not survive real Bayesian IRT fitting.
157	
158	**R2 → R1**: R2's novelty assessment is more nuanced. While R1 correctly critiques the methodology as not deeply novel, R2 points out the signal survival analysis has genuine independent value. R1 agrees this is the paper's strongest contribution. R2's comprehensive missing related work list (DIF, ML calibration, conformal prediction, data attribution) identifies gaps R1 did not flag — both agree these are important omissions.
159	
160	### Step 3: Convergence
161	
162	**Points of agreement:**
163	1. The problem is important and timely — both reviewers rate significance highly
164	2. Core model specification (Eq. 3) is sound and well-motivated
165	3. Measurement error model is necessary and well-designed
166	4. Signal survival analysis is the most novel contribution
167	5. Fisher Information derivation is missing — a critical gap given it underpins Contribution 3
168	6. No figures is a serious presentation deficiency
169	7. Multiple suspicious numerical patterns (uniform std, identical CI widths, too-uniform coverage)
170	8. Multi-family validation is thin (3 dosages, 1 model/family, 1 scale)
171	9. 72B analysis is below own identifiability threshold — internally inconsistent
172	10. Important related work categories are missing (DIF, conformal, ML calibration)
173	11. Selective reporting in Tables 1, 4, 14 weakens the claims
174	
175	**Points of partial disagreement:**
176	- R1 rates 3/10 (primarily due to suspected imagined results); R2 rates 5/10 (gives more credit for design quality and framing). After discussion, both agree that the suspicious numerical patterns significantly undermine credibility regardless of the design's merits. However, the experimental DESIGN is comprehensive and well-structured. The gap between design quality and result credibility is the paper's central problem.
177	- R2 initially gives more credit for honest framing; R1 counters that honest framing of limitations cannot compensate for fundamental result credibility issues. Both agree.
178	
179	**Consensus overall score: 4/10 (Weak Reject)**
180	
181	Rationale: The paper addresses an important problem with a well-designed methodology grounded in educational measurement. The signal survival analysis is a genuinely novel empirical finding. However, (1) the methodological novelty is limited — it is fundamentally a synthesis of existing techniques, (2) multiple numerical patterns strongly suggest the reported results are not from actual experiments, (3) the Fisher Information derivation is missing, (4) several important related work areas are unaddressed, and (5) selective reporting in key tables weakens the claims. At AAAI's 17.6% acceptance rate, these weaknesses preclude acceptance.
182	
183	### Step 4: Consolidated Assessment
184	
185	**Overall Score: 4/10 — Weak Reject**
186	
187	#### What Works
188	- **Problem importance**: Benchmark contamination is a real and growing problem. The "calibration not elimination" framing is the right paradigm shift.
189	- **Framework design**: The two-stage pipeline (RRF exposure → contamination-augmented 4PL IRT with measurement error) is well-architected. Per-benchmark γ_k, the meta-circularity argument for RRF, and regime-dependent σ_e are individually sound design choices.
190	- **Signal survival analysis**: The signal×regime AUC heatmap (Table 11) documenting cliff-like degradation of logit-based signals under RL is the paper's strongest contribution — genuinely novel and independently valuable.
191	- **Experimental scope**: 12 experiments across 3 model families, 4 scales, 4 benchmarks, 7 baselines is comprehensive in design.
192	
193	#### What Doesn't Work
194	- **Result credibility**: Uniform std (0.6pp across all conditions in Table 1), identical CI widths (7.8pp for all RL models in Table 13), and suspiciously uniform coverage across benchmarks with 85x item count difference (Table 8) are not consistent with real Bayesian IRT outputs. These patterns suggest the results are projections.
195	- **Selective reporting**: Intermediate dosages omitted for 3 of 4 benchmarks (Table 1), many missing cells in identifiability matrix (Table 4), regret reported only at K=5 (Table 14). The pattern is consistent with reporting only favorable conditions.
196	- **Missing derivation**: The Fisher Information formula I(γ) ∝ N·AUC²/(1-AUC²) is stated without proof. For a 4PL model with measurement error, this is non-trivial and must be derived.
197	- **Limited novelty**: Each component (RRF, 4PL IRT, measurement error model, Bayesian inference) is borrowed from existing literature. The synthesis is competent but not transformative.
198	- **Presentation**: Zero figures for a complex pipeline with 12 experiments. 16 tables with missing cells. Missing related work in DIF, ML calibration, conformal prediction, data attribution.
199	- **Internal inconsistency**: 72B analysis (AUC=0.62) proceeds despite the paper's own identifiability threshold (AUC≥0.68).
200	
201	#### Actionable Recommendations for Revision
202	1. **Execute the experiments.** The design is good — run the actual SFT injection, signal evaluation, and IRT fitting. Real results will show variable noise, benchmark-dependent coverage, and model-dependent CI widths.
203	2. **Derive the Fisher Information.** Provide the full derivation in an appendix. If the formula is approximate, state the approximation assumptions.
204	3. **Add figures.** At minimum: pipeline diagram, calibrated-vs-true scatter with CIs, signal×regime AUC heatmap, dose-response curves, identifiability phase diagram, coverage calibration plot.
205	4. **Fill in missing table cells.** Report all dosages for all benchmarks (Table 1), all conditions in the identifiability matrix (Table 4), and all K values in regret analysis (Table 14).
206	5. **Expand related work.** Add DIF literature, disambiguate from ML calibration, discuss conformal prediction as UQ alternative, cite data attribution methods, position relative to broader benchmark design.
207	6. **Remove or caveat 72B analysis.** Either acknowledge it falls below the identifiability threshold and present it as illustrative only, or remove it.
208	7. **Strengthen multi-family validation.** Run full 5-dosage protocol for Llama and Pythia, or at minimum acknowledge the reduced protocol explicitly.
209	8. **Add computational cost analysis.** Report wall-clock time for the full pipeline per benchmark.
210	
211	#### Coverage vs Experiment Design
212	All 12 planned experiments are covered in scope, but several are thinned:
213	- exp-001: Only MMLU has full dosage breakdown
214	- exp-004: Table 4 shows only a sparse subset of the 144 conditions
215	- exp-009: Regret only at K=5, not K=3/10
216	- exp-014: Only aggregate MAE, no per-dosage breakdown
217	
218	#### Dimension Scores (Consolidated)
219	
220	| Dimension | R1 | R2 | Consensus |
221	|-----------|----|----|-----------|
222	| Soundness | 2/4 | — | 2.5/4 |
223	| Novelty | — | 2/4 | 2/4 |
224	| Significance | — | 3/4 | 3/4 |
225	| Empirical Methodology | 1/4 | — | 1.5/4 |
226	| Related Work | — | 2/4 | 2/4 |
227	| Clarity / Presentation | 2/4 | — | 2/4 |
228	| **Overall** | **3/10** | **5/10** | **4/10** |
229	| Confidence | 4/5 | 4/5 | 4/5 |
230	
231	**Decision: Weak Reject (4/10)**
232	
233	The paper has a strong research direction and comprehensive experimental design, but the current manuscript does not meet the AAAI acceptance bar due to result credibility concerns, limited methodological novelty, missing theoretical derivations, and significant related work gaps. A thorough revision with real experimental results and the recommended additions could elevate this to a competitive submission.
234	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dcef7db-a730-40f0-be9e-349cb96ee138",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "4cb0446d-af96-42ae-bcdb-de3049146c13",
  "sourceToolAssistantUUID": "2dcef7db-a730-40f0-be9e-349cb96ee138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-13T18:04:52.301Z_

<details open><summary>🔧 Tool call — Read · `toolu_019MP7k9tAhdjb9nDYSS6W5p`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cb0446d-af96-42ae-bcdb-de3049146c13",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11YjQmcKzvQ7e4KeeZ5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b06c93ba-dd10-4c8b-aa47-26cb627c652b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THsUVBLBWtHPhr3Z2jXnJi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 227,
      "cache_read_input_tokens": 54807,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 227
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 54807,
          "cache_creation_input_tokens": 227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 227,
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

_source line 46 · 2026-05-13T18:04:52.313Z_

<details><summary>↩ Tool result · `toolu_019MP7k9tAhdjb9nDYSS6W5p`</summary>

```text
1	---
2	dream_id: dream_20260513T155040
3	tier: best
4	overall_score: 5/10 — Borderline Reject
5	timestamp: 2026-05-13T16:29:14.054943+00:00
6	---
7	
8	# DREAM Review Report: ContamCal
9	
10	**Paper:** ContamCal: Calibrating Benchmark Scores for Training Data Contamination via Contamination-Augmented Item Response Theory
11	**Venue:** AAAI 2027 (acceptance rate ~17.6%, scale 1–10)
12	**Review mode:** Full (2 Reviewers + Roundtable)
13	**Date:** 2026-05-13
14	
15	---
16	
17	## Venue Calibration
18	
19	AAAI 2026 acceptance rate was 17.6% (4,167/23,680). Scoring scale 1–10. Evaluation criteria: significance and novelty of contributions, theoretical/empirical soundness, relevance to the AAAI community, clarity. Preference for papers that explore new territory over narrow incremental advances.
20	
21	---
22	
23	## Reviewer 1 (R1): Methods + Experiments
24	
25	### A. Methodological Soundness
26	
27	**A1. 4PL+γ formulation (Adequate with concerns).**
28	The covariate-in-the-exponent approach (Eq. 2) is standard in item compromise IRT. However, using a **single global γ** is a strong assumption: it asserts contamination produces the same logit-scale boost regardless of model scale, item type, or benchmark. The paper's own data shows scale-dependent inflation (0.5B: 10.8pp vs. 3B: 8.2pp at 50% dosage), which directly contradicts a uniform γ. A hierarchical γ_j ~ N(μ_γ, σ_γ) or per-benchmark γ would be more defensible. The paper is ambiguous about whether IRT is fitted jointly across benchmarks or separately — this must be clarified.
29	
30	**A2. RRF aggregation (Reasonable but under-justified).**
31	RRF with c=60 is a sensible default. However, the argument against learned weights is hand-wavy — learned weights could be trained on the authors' own synthetic contamination data, avoiding circularity. The ablation shows calibration-weighted RRF (0.86) slightly underperforms vanilla RRF (0.87), but this is tested only in the best-case SFT regime. RRF's real advantage is simplicity and robustness to outlier signal scores, which should be stated directly.
32	
33	**A3. Identifiability (Ad hoc threshold).**
34	The claim that θ-γ posterior correlation = 0.31 < 0.4 confirms identifiability relies on an **ad hoc threshold** with no cited theoretical or empirical basis. The argument would be stronger with a simulation study showing that identifiability degrades as this correlation increases (the imagined exp-004 identifiability sweep), but the paper appears to present only a single MVP seed.
35	
36	**A4. Measurement error extension (Under-specified).**
37	The formulation e_obs = e_true + ε is classical measurement error. However, the paper does not specify how e_true is handled in the Stan model. If e_true is a latent variable for each (j,i) pair, the parameter space explodes. If σ_e merely inflates γ's posterior variance post-hoc, the uncertainty propagation is approximate. Implementation details are missing.
38	
39	**A5. Counterfactual θ* identification (Conditionally valid).**
40	Valid under the assumption that contamination acts purely additively in logit space and does not alter genuine reasoning ability. Plausible for SFT memorization but questionable for RL, where training on benchmark-adjacent data may genuinely improve capability.
41	
42	### B. Experimental Rigor
43	
44	**B1. SFT injection protocol (Sound for internal validity).**
45	Paraphrase-based injection at 3 scales × 5 dosages × 4 benchmarks = 15 model pairs is a solid controlled setup. However, SFT injection produces a specific memorization signature that may be easier to detect than pre-training contamination — ecological validity is limited.
46	
47	**B2. Incomplete tables (CRITICAL).**
48	Table 4 (main result) reports per-benchmark MAE for ContamCal only; all 5 baselines show "—" for per-benchmark MAE, CI coverage, CI width, and Kendall τ. This means:
49	- Cannot assess whether ContamCal's advantage is uniform or concentrated on a subset of benchmarks
50	- Baseline uncertainty quantification is completely unreported
51	- Ranking preservation for baselines is unknown
52	
53	Tables 5, 6, 7, 10, 11, 12 have similar pervasive "—" entries. Approximately 60% of cells that should contain values are missing. **This is the single most damaging issue** — it makes the paper appear either incomplete or as if unfavorable results are being hidden.
54	
55	**B3. Zero figures (CRITICAL).**
56	The paper contains **no figures at all**. For a two-stage Bayesian pipeline with 12 experiments, this is disqualifying. Essential missing figures:
57	- Framework overview diagram (pipeline visualization)
58	- Calibrated vs. true accuracy scatter plot with CI error bars (the "money figure")
59	- Signal × regime AUC heatmap
60	- Dose-response curves
61	- Coverage calibration plot
62	
63	**B4. RL regret calculation (Potentially circular).**
64	The 42% regret reduction claim requires knowing the "true" uncontaminated ranking for RL models, but no ground truth exists. If calibrated scores serve as the ground truth proxy, the calculation is tautological. The paper does not specify the ground truth source for RL regret computation.
65	
66	**B5. No error bars.**
67	No standard deviations or confidence intervals are reported for any experimental result, despite the experiment plan specifying 3 seeds.
68	
69	**B6. Scale bridging.**
70	7B controlled (MAE=2.2pp) adds incremental confidence. 72B observational is necessarily weaker — γ=0.18 on MMLU could reflect true contamination or systematic bias in signals at this scale. The γ CI including zero on GSM8K could mean either "reasoning benchmarks are less susceptible" or "insufficient power at 72B."
71	
72	**B7. Few-examinee regime.**
73	N≥50 with pre-estimation from 400+ model pool is practical but assumes item parameter stability across model pools, which is not validated.
74	
75	### R1 Scores
76	
77	| Criterion | Score | Justification |
78	|-----------|-------|---------------|
79	| Overall | **4/10** | Strong idea, but manuscript is incomplete — missing figures, pervasive "—" in tables, no error bars. Cannot evaluate empirical strength. |
80	| Soundness | **3/5** | Core formulation is correct. Single global γ, ad hoc identifiability threshold, potentially circular RL regret, and missing measurement error details are concerns. |
81	| Significance | **4/5** | High practical value. Calibration with UQ under contamination is a genuine unsolved problem. |
82	| Novelty | **3/5** | Non-trivial cross-disciplinary transfer. Individual components are not new. |
83	| Clarity | **2/5** | Good writing quality, but zero figures and sparse tables make evaluation impossible. |
84	| Confidence | **4/5** | Familiar with IRT, Bayesian methods, and LLM contamination literature. |
85	
86	**R1 Recommendation:** Reject in current form.
87	
88	---
89	
90	## Reviewer 2 (R2): Novelty + Related Work
91	
92	### A. Novelty Assessment
93	
94	**A1. Core idea (Incremental, not transformative).**
95	Treating contamination as a covariate in IRT rather than removing it is the central contribution. However, this is a direct application of Eckerly (2017) and Sinharay (2017)'s item compromise IRT to a new domain. The analogy to causal inference shifting from elimination to adjustment is apt but overstated — the paper does not develop new causal identification theory.
96	
97	**A2. Three structural modifications (Mixed novelty).**
98	- (a) Independent examinees → single model with joint item distributions: This is the most interesting adaptation but is **under-explored** — the local independence assumption is fundamentally altered when a single model responds to all items (item responses are correlated through shared model parameters). The paper does not discuss or test this violation.
99	- (b) Binary leakage → continuous exposure: Straightforward extension; continuous covariates in IRT are standard.
100	- (c) Regime-conditional ability: An engineering decision (signal selection based on training regime), not a modeling contribution.
101	
102	**A3. RRF fusion (Not novel).**
103	RRF is an off-the-shelf rank aggregation technique. Applying it to contamination signal fusion is a reasonable engineering choice, not a methodological contribution.
104	
105	**A4. Regime-conditional modeling (Engineering, not contribution).**
106	Detecting that RL degrades certain signals and automatically falling back to surviving signals is useful but is an implementation decision, not a theoretical advance.
107	
108	**A5. Incremental novelty over remove-and-rescore (Clear but narrow).**
109	The improvement over remove-and-rescore (1.97pp vs. 4.2pp MAE) demonstrates the value of continuous exposure modeling over binary flagging. The provision of credible intervals is a genuine addition. However, this improvement comes entirely from (a) using continuous rather than binary exposure and (b) using IRT rather than simple rescoring — both are standard techniques.
110	
111	**Overall novelty verdict:** ContamCal is a **well-executed synthesis paper** — it combines existing components (RRF, 4PL IRT, contamination signals, Bayesian MCMC) in a sensible way for a new application. The novelty is in the cross-disciplinary transfer and the specific combination, not in any individual component. For AAAI, this level of novelty is borderline.
112	
113	### B. Related Work Completeness
114	
115	**10 citations is critically insufficient** for a paper spanning contamination detection, IRT, Bayesian inference, and evaluation methodology. Major gaps:
116	
117	1. **Missing baselines/citations:**
118	   - DCR (Detecting Contamination via Response patterns) — the most directly comparable prior work using IRT-adjacent ideas for contamination, absent as both citation and baseline
119	   - HiBayES — Bayesian evaluation scoring with hierarchical models
120	   - DIF (Differential Item Functioning) literature — the direct precursor to item compromise IRT, extensive body of work unacknowledged
121	
122	2. **Missing related areas:**
123	   - Membership inference attacks (broader contamination detection literature)
124	   - Extraction attacks for training data
125	   - Post-hoc calibration in ML (Platt scaling, temperature scaling — conceptually related as post-hoc score adjustment)
126	   - Dynamic/live benchmarks (LiveBench, LMSYS) — the alternative approach to contamination
127	   - Data attribution and influence functions
128	   - Conformal prediction as alternative to Bayesian CIs
129	   - Benchmark design literature
130	
131	3. **Educational measurement connection under-developed.**
132	   The paper cites Eckerly (2017) and Sinharay (2017) but does not engage with the broader DIF, item preknowledge, or test security literature. Given that this is the theoretical foundation, deeper engagement is needed.
133	
134	4. **Missing concurrent work.**
135	   The 2025-2026 period has seen active work on contamination-aware evaluation. The paper should survey recent arXiv preprints on this topic.
136	
137	### C. Positioning and Framing
138	
139	**"Statistical safety net" framing (Effective but overpromised).**
140	The framing is compelling and well-motivated. However, calling it a "safety net" implies reliability guarantees that the paper cannot deliver — particularly in the RL regime where CIs are 11.4pp wide.
141	
142	**Scope of claims (Appropriate for SFT, overstated for RL).**
143	The SFT claims are well-supported by controlled experiments. The RL claims (42% regret reduction) rest on an observational study with 8 models and no ground truth, which is insufficient for the confidence with which they are stated.
144	
145	### D. Significance and Impact
146	
147	**Problem importance: High.**
148	Contamination is increasingly recognized as a fundamental threat to LLM evaluation validity. The community needs solutions beyond detection.
149	
150	**Practical adoption barriers:**
151	- Requires at least 50 models for reliable estimation
152	- Full pipeline requires model weight access (embedding retrieval, Min-K%++)
153	- ConStat requires paraphrase generation infrastructure
154	- Stan MCMC is computationally expensive
155	- RL regime (where most production models live) produces very wide CIs
156	
157	**Impact assessment:** If fully validated with complete experimental results, this would be a useful tool for the evaluation community. The practical barriers limit but do not eliminate impact.
158	
159	### R2 Scores
160	
161	| Criterion | Score | Justification |
162	|-----------|-------|---------------|
163	| Overall | **5/10** | Addresses a real problem with a reasonable approach. Novelty is incremental (synthesis of existing techniques). Related work is severely incomplete. Manuscript presentation is draft-quality. |
164	| Soundness | **3/5** | Core framework is technically sound. Local independence violation unexamined. |
165	| Significance | **4/5** | Important problem, potentially impactful solution. |
166	| Novelty | **2/5** | Cross-disciplinary transfer, not new methodology. Every component is borrowed. |
167	| Clarity | **2/5** | Writing is clear but manuscript is incomplete (no figures, sparse tables). |
168	| Confidence | **4/5** | Familiar with IRT, contamination literature, and evaluation methodology. |
169	
170	**R2 Recommendation:** Borderline reject. Could reach weak accept with complete results, 30+ citations, and proper figures.
171	
172	---
173	
174	## Roundtable Synthesis
175	
176	### Step 2: Cross-Sharing Summary
177	
178	R1's key concerns shared with R2: incomplete tables, zero figures, circular RL regret, single global γ, ad hoc identifiability threshold.
179	
180	R2's key concerns shared with R1: synthesis-level novelty only, 10 citations insufficient, missing DCR baseline, local independence violation unexamined, RL practical limitation.
181	
182	### Step 3: Convergence
183	
184	**Points of agreement:**
185	1. **The problem is important and the approach is reasonable.** Both reviewers rate significance 4/5.
186	2. **The manuscript is incomplete.** Zero figures, ~60% missing table entries, no error bars. Both rate clarity 2/5.
187	3. **Single global γ is a concern.** The paper's own data shows scale-dependent contamination effects incompatible with a uniform γ.
188	4. **RL claims are under-supported.** Observational study with 8 models and no ground truth is insufficient. The 42% regret reduction may be circular.
189	5. **Soundness is adequate but with gaps.** Both rate soundness 3/5. Core IRT framework is correct; execution details (measurement error, identifiability, local independence) need work.
190	
191	**Points of divergence:**
192	- **Novelty:** R1 gives 3/5 (acknowledging non-trivial cross-disciplinary transfer); R2 gives 2/5 (emphasizing that every component is borrowed). After discussion, consensus is **2.5/5** — the synthesis is competent but the paper needs to be more honest about its novelty positioning and develop the local independence violation as a genuine theoretical contribution.
193	- **Overall score:** R1 gives 4/10, R2 gives 5/10. Difference is driven by R2 weighing the problem importance more heavily despite novelty concerns.
194	
195	### Step 4: Consolidated Assessment
196	
197	**Consensus overall score: 4.5/10 → Round to 5/10 (Borderline Reject)**
198	
199	| Criterion | R1 | R2 | Consensus |
200	|-----------|----|----|-----------|
201	| Overall | 4/10 | 5/10 | **5/10** |
202	| Soundness | 3/5 | 3/5 | **3/5** |
203	| Significance | 4/5 | 4/5 | **4/5** |
204	| Novelty | 3/5 | 2/5 | **2.5/5** |
205	| Clarity | 2/5 | 2/5 | **2/5** |
206	
207	---
208	
209	## Critical Issues (Must Fix)
210	
211	1. **Complete all tables.** Fill in every "—" entry. All baselines need per-benchmark MAE, CI coverage, CI width, and Kendall τ. All ablation tables need full entries. (~60% of cells are missing.)
212	
213	2. **Add figures (minimum 5).** Framework overview, calibrated-vs-true scatter with CIs, signal×regime heatmap, dose-response curves, coverage calibration plot. Currently zero figures.
214	
215	3. **Clarify RL regret ground truth.** Explicitly state what serves as ground truth for expected regret on RL models. If it's a held-out clean benchmark, say so. If it's the calibrated scores, the 42% claim is circular and must be withdrawn.
216	
217	4. **Expand related work to 25-30+ citations.** Add DCR, HiBayES, DIF literature, membership inference, dynamic benchmarks, post-hoc calibration methods, data attribution. Currently only 10 citations.
218	
219	5. **Add error bars / standard deviations.** Report variance across seeds for all key results.
220	
221	## Major Issues (Should Fix)
222	
223	6. **Address single global γ limitation.** Either (a) justify why per-model heterogeneity doesn't bias θ estimates, (b) fit per-benchmark γ and report, or (c) implement hierarchical γ as an extension.
224	
225	7. **Clarify IRT fitting scope.** State explicitly whether the model is fitted jointly across benchmarks or per-benchmark.
226	
227	8. **Specify measurement error implementation.** How are latent true exposure scores handled in Stan? Fully marginalized? Latent variables? Post-hoc approximation?
228	
229	9. **Discuss local independence violation.** When a single model is the "examinee" for all items, item responses are correlated through shared parameters. This fundamentally alters IRT assumptions and needs theoretical or empirical treatment.
230	
231	10. **Discuss ecological validity of SFT injection.** SFT injection produces a specific memorization signature that may be easier to detect than pre-training contamination.
232	
233	11. **Include DCR as a baseline.** This is the most directly comparable prior work and must be compared against.
234	
235	## Minor Issues
236	
237	12. **Embedding retrieval AUC=0.90 on base models (Table 8):** If base models have no contamination, why is AUC so high? This suggests the embedding signal may detect training data proximity rather than contamination. Discuss false positive implications.
238	
239	13. **50% coverage = 0.55:** Slight overcoverage at 50% level suggests CIs may be too wide. Discuss CI calibration.
240	
241	14. **Pre-estimation transfer assumption.** Validate that item parameters are stable across model pools of different capability distributions.
242	
243	15. **ConStat paraphrase quality.** Discuss who generates paraphrases and potential bias.
244	
245	16. **Computational cost.** Report Stan MCMC wall-clock time and signal computation costs.
246	
247	---
248	
249	## Experiment Coverage Assessment
250	
251	Comparing the paper against the full experiment plan (review_context.yaml):
252	
253	| Experiment | Planned | Present in Paper | Quality |
254	|-----------|---------|-----------------|---------|
255	| exp-001: Controlled SFT injection | ✓ | ✓ | Table 1 adequate but only MMLU fully reported |
256	| exp-002: Signal pipeline | ✓ | ✓ | Table 2 adequate |
257	| exp-003: RRF ablation | ✓ | ✓ | Table 3 adequate |
258	| exp-005: Noise propagation | ✓ | ✓ | Table 6 has "—" entries |
259	| exp-006: IRT + baselines | ✓ | ✓ | **Table 4 critically incomplete** — baselines lack per-benchmark data |
260	| exp-007: 7B scale bridging | ✓ | ✓ | Table 7 adequate |
261	| exp-008: Signal survival | ✓ | ✓ | Table 8 complete |
262	| exp-009: RL case study | ✓ | ✓ | Table 9 adequate but regret ground truth unclear |
263	| exp-010: Prior sensitivity | ✓ | ✓ | Table 11 adequate |
264	| exp-011: Few-examinee | ✓ | ✓ | Table 12 has "—" entries |
265	| exp-012: 72B observational | ✓ | ✓ | Table 7 adequate |
266	| exp-013: 2-signal mode | ✓ | ✓ | Table 13 adequate |
267	
268	All 12 experiments are present but many have incomplete reporting. Of 21 planned figures, **zero** are included.
269	
270	---
271	
272	## Bottom Line
273	
274	ContamCal addresses a genuine and timely problem — post-hoc calibration of contaminated benchmark scores with proper uncertainty quantification. The approach (RRF signal fusion → contamination-augmented 4PL IRT) is methodologically sound in concept and draws on a solid theoretical foundation from educational measurement. The experimental design is comprehensive.
275	
276	However, the **manuscript is clearly incomplete**: zero figures, ~60% of table cells missing, no error bars, 10 citations. The novelty is incremental (synthesis of existing techniques for a new application). The RL claims may rest on circular reasoning. At AAAI's 17.6% acceptance rate, this paper in its current form would not pass the completeness bar, let alone compete on novelty and execution quality.
277	
278	**With full experimental reporting, 5+ figures, expanded related work, and resolution of the RL regret circularity, this paper could reach 6-7/10 (weak accept range) at AAAI.** The research direction is promising and the community needs this kind of work.
279	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b06c93ba-dd10-4c8b-aa47-26cb627c652b",
  "isSidechain": true,
  "promptId": "6ec152db-e681-4ba0-9f6d-1ed4286f28b5",
  "agentId": "a3c902c84adde37f7",
  "type": "user",
  "uuid": "af682191-9f67-43d7-bd00-31e239ae3453",
  "sourceToolAssistantUUID": "b06c93ba-dd10-4c8b-aa47-26cb627c652b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-13T18:06:44.208Z_

Now I have a comprehensive understanding of the paper, its current state, and the prior dream reviews. Let me compile my R2 review focusing on Novelty and Related Work.

## R2 Review: Novelty + Related Work

### Summary
ContamCal proposes a two-stage framework — RRF fusion of four detection signals into exposure scores, followed by contamination-augmented 4PL IRT with measurement error modeling — to produce calibrated LLM benchmark scores with Bayesian credible intervals. The core modeling contribution is a direct adaptation of item compromise IRT (Eckerly 2017, Sinharay 2017) to LLM evaluation, with three structural modifications (shared item pool, continuous exposure, regime-conditional ability). The signal survival analysis under RL post-training is the most genuinely novel empirical finding. The paper addresses an important gap but its novelty is primarily integrative rather than methodological, and several important related work areas remain underengaged.

### Strengths (Novelty)

1. **The detection-to-calibration bridge is a genuine conceptual contribution.** The field has many detection methods (Min-K%++, ConStat, Self-Critique, KDS) and many IRT-based evaluation methods (PSN-IRT, Growing Pains, ATLAS, HiBayES), but no prior work bridges them into calibrated scores with uncertainty quantification. ContamCal fills this structural gap. Even if each component is borrowed, the integration addresses a question no existing method answers: "what would this model's accuracy be without contamination?"

2. **Signal survival analysis is genuinely novel and independently valuable.** The cliff-like (not gradual) degradation of logit-based signals under RL, with qualitative reversal of signal rankings between SFT and RL regimes, is a striking empirical finding. The AUC heatmap (Table 11 in the dream paper) has standalone value for the detection community. No prior work has systematically mapped signal performance across training regimes in this way, though Wang et al. (2025) on fragility and Wust et al. (2025) on Self-Critique have touched on individual aspects.

3. **The measurement error model is a non-trivial and necessary design element.** Treating observed RRF exposure as a noisy proxy for latent contamination, with regime-dependent noise variance (sigma_e = 0.12 SFT vs. 0.28 RL), is not standard in item compromise IRT and represents genuine methodological thought. The coverage improvement (83% to 93%) demonstrates the model's necessity. While errors-in-variables modeling is classical in statistics, its specific application to propagate detection signal uncertainty through IRT posteriors is novel in this context.

4. **The meta-circularity argument for RRF is intellectually sound.** The observation that a learned aggregator's training data may itself be contaminated — and the empirical result that calibration-weighted RRF slightly underperforms standard RRF — provides both theoretical and empirical support for a parameter-free design. Positioning this as a design choice rather than a contribution is rare intellectual honesty.

5. **Per-benchmark gamma_k captures genuine heterogeneity.** The ablation showing global gamma yields higher MAE (2.1 vs. 1.5 pp) and degraded coverage (88% vs. 93%) demonstrates that benchmark-level contamination susceptibility varies meaningfully. This is a natural but non-trivial extension of the item compromise literature, which typically uses a single compromise parameter.

### Strengths (Related Work & Positioning)

1. **The related work in the paper draft (related_work.tex) is substantially more comprehensive than in the dream paper.** It covers contamination detection (8 methods), contamination impact and mitigation, IRT for LLM evaluation (6 systems), and item compromise in educational measurement. The positioning table (Table 1 in related_work.tex) clearly delineates ContamCal's unique capability profile (detects + calibrates + UQ + RL-robust).

2. **The Emperor's New Clothes motivation is well-leveraged.** The finding that all 20 mitigation strategies fail (Xu et al. 2025) is the strongest possible motivation for the paradigm shift from elimination to calibration. The paper correctly draws the analogy to causal inference's shift from eliminating confounders to statistically controlling for them.

3. **Educational measurement roots are properly credited.** Eckerly (2017), Sinharay (2017), De Boeck & Wilson (2004), and Mislevy (1986) are all cited. The three structural adaptations are clearly articulated. San Martin et al. (2009) is cited in the context of local independence and per-benchmark fitting justification.

4. **DCR is appropriately positioned as the closest predecessor.** The paper correctly identifies DCR as the only existing method producing adjusted accuracy and compares against it as a baseline. The distinction (DCR lacks UQ and RL handling) is fair.

5. **Honest framing of limitations enhances credibility.** Wide CIs under RL are framed as "correct behavior, not limitation." The 72B analysis is acknowledged as ecological rather than precise. SFT injection is called "best-available proxy." This maturity of framing is unusual and valuable.

### Weaknesses (Novelty)

1. **(Moderate) The core IRT model is a direct application of existing item compromise IRT.** Equation 3/4 (contamination-augmented 4PL) adds a single linear contamination covariate to standard 4PL IRT. This is precisely what Eckerly (2017) and Sinharay (2017) do in educational testing, adapted to a new domain. The three structural modifications — while necessary — are individually either standard (continuous covariates in explanatory IRT per De Boeck & Wilson 2004) or engineering decisions (regime-conditional signal selection). A psychometrician would recognize Stage 2 as routine explanatory IRT fitting. The paper should be more explicit about where the intellectual contribution lies versus where it applies existing techniques.

2. **(Moderate) RRF is an off-the-shelf technique applied straightforwardly.** Reciprocal Rank Fusion (Cormack et al. 2009) is a well-known parameter-free rank aggregation method from information retrieval. Its application to contamination signal fusion is reasonable engineering but not methodologically novel. The meta-circularity argument justifies the choice but does not make it a contribution.

3. **(Moderate) Signal survival analysis is descriptive, not explanatory.** The finding that logit-based signals collapse under RL while Self-Critique partially survives is documented but not explained mechanistically. Why does RL erase embedding fingerprints but not meta-cognitive signatures? The paper gestures at "RL optimizes behavioral reward, erasing logit/embedding fingerprints" but this is not validated. Without testing across different RL algorithms (PPO vs. GRPO vs. DPO), reward model architectures, or RL training durations, the generalizability of the cliff-like pattern is asserted rather than established. For a "Core Contribution," deeper mechanistic analysis is expected.

4. **(Minor) The causal inference analogy is suggestive but undeveloped.** The paper draws an analogy to propensity score adjustment (Rosenbaum & Rubin 1983) but does not develop it formally. There is no DAG, no formal identification argument for the counterfactual theta*, and no sensitivity analysis for unmeasured confounding (contamination channels undetected by all four signals). The analogy remains narrative framing. This is acceptable if not overclaimed, but the paper should acknowledge the gap between the analogy and formal causal identification.

5. **(Minor) "Dual-track validation" is experimental design, not a contribution.** Using both controlled (SFT injection) and observational (RL) experiments is good experimental methodology but standard practice in the ML evaluation literature. Elevating this to "Core Contribution 3" inflates the contribution count. It should be described as part of the experimental design.

6. **(Minor) The identifiability simulation (Supporting Contribution 4) is standard simulation-based calibration.** Running parameter recovery simulations with SBC (Talts et al. 2018) is methodological due diligence, not a contribution. The Fisher Information analysis adds value but the derivation is missing from the paper — without it, the analytical threshold AUC=0.68 cannot be verified.

### Weaknesses (Related Work & Positioning)

1. **(Major) Missing engagement with Differential Item Functioning (DIF) literature.** ContamCal essentially performs DIF analysis between contaminated and clean conditions — the gamma_k parameter measures whether items function differently for models with different exposure levels. The DIF literature (Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999) is the direct statistical precursor and is entirely absent from the paper. This is a significant omission given the psychometric grounding the paper claims.

2. **(Moderate) No disambiguation from ML calibration.** The term "calibration" in the ML community primarily refers to probability calibration (Guo et al. 2017, Platt 1999, temperature scaling). The paper uses "calibration" to mean decontamination adjustment. This ambiguity will confuse AAAI reviewers and must be explicitly disambiguated. Failing to cite or distinguish from this large body of work is a gap.

3. **(Moderate) Missing discussion of alternative UQ approaches.** Conformal prediction (Angelopoulos & Bates 2023, Vovk et al. 2005) provides distribution-free coverage guarantees — a potentially attractive alternative to Bayesian credible intervals that relies on weaker assumptions. The paper should discuss why Bayesian CIs were preferred over conformal methods, or at minimum acknowledge conformal prediction as an alternative.

4. **(Moderate) Data attribution methods not considered as alternative exposure signals.** TracIn (Pruthi et al. 2020), TRAK (Park et al. 2023), and influence functions provide principled methods for attributing model behavior to training examples. These could serve as alternative or complementary exposure estimation signals to the four used in ContamCal. Their absence from the related work is notable.

5. **(Minor) Multidimensional IRT not discussed.** Using a unidimensional theta for MMLU (which covers 57 subjects) is questionable. Reckase (2009) and cognitive diagnostic models (de la Torre 2011) offer multidimensional alternatives. The paper's per-benchmark fitting partially addresses this but the assumption should be explicitly discussed and justified.

6. **(Minor) Broader benchmark ecosystem underengaged.** HELM (Liang et al. 2022), BIG-bench (Srivastava et al. 2023), Open LLM Leaderboard, and Chatbot Arena / LMSYS (which is contamination-resistant by design via live human evaluation) are not discussed. Positioning ContamCal within this broader evaluation landscape would strengthen the paper.

7. **(Minor) San Martin et al. (2009) is cited but underutilized.** This paper addresses identifiability of fixed-effects 3PL models and is directly relevant to the paper's identifiability analysis. It is cited in the method section in passing (justifying per-benchmark fitting) but deserves deeper engagement given the paper's own identifiability claims.

8. **(Minor) Contamination surveys not cited.** Balloccu et al. (2024) and Jacovi et al. (2023) provide comprehensive surveys of the contamination problem that would ground the introduction.

### Questions for Authors

1. How does ContamCal relate to Differential Item Functioning (DIF) analysis? The gamma_k parameter appears to be measuring DIF between exposure groups. Is there a formal connection, and does the DIF literature offer additional diagnostic tools?

2. What is the sensitivity of calibrated scores to unmeasured contamination channels — i.e., contamination that none of the four signals detect? Have you conducted any form of sensitivity analysis analogous to Rosenbaum bounds?

3. The signal survival analysis tests only GRPO as the RL algorithm. Would the cliff-like degradation pattern hold for PPO, DPO, or other RL variants? What mechanistic property of RL training drives the signal erasure?

4. Why was conformal prediction not considered as an alternative to Bayesian credible intervals? Conformal methods provide distribution-free coverage guarantees without the local independence assumptions that IRT requires.

5. The Fisher Information formula I(gamma) proportional to N * AUC^2 / (1 - AUC^2) is stated without derivation. Can you provide the full derivation, including how measurement error and the 4PL bounded response function affect the information?

6. For MMLU with 57 subjects and 14K items, is a unidimensional theta defensible? Have you examined whether multidimensional IRT would yield different gamma estimates?

7. The paper fits IRT per-benchmark to mitigate local independence violations. How are per-benchmark theta estimates reconciled for cross-benchmark model comparison? Is a single "calibrated ability" reported, and if so, how is it aggregated?

8. What is the computational cost of the full pipeline? NUTS HMC on 14K MMLU items with latent tau variables and measurement error is non-trivial.

### Missing References

**Critical gaps:**
- Holland, P.W. & Wainer, H. (1993). Differential Item Functioning. Lawrence Erlbaum.
- Thissen, D., Steinberg, L., & Wainer, H. (1993). Detection of DIF using the parameters of item response models.
- Zumbo, B.D. (1999). A handbook on the theory and methods of DIF.

**Important gaps:**
- Guo, C., et al. (2017). On calibration of modern neural networks. ICML. (disambiguation of "calibration")
- Angelopoulos, A.N. & Bates, S. (2023). Conformal prediction: A gentle introduction. (alternative UQ)
- Pruthi, G., et al. (2020). Estimating training data influence by tracing gradient descent. NeurIPS. (data attribution)
- Park, S., et al. (2023). TRAK: Attributing model behavior at scale. ICML. (data attribution)
- Reckase, M.D. (2009). Multidimensional Item Response Theory. Springer. (MIRT)

**Minor gaps:**
- Liang, P., et al. (2022). Holistic Evaluation of Language Models (HELM). (benchmark ecosystem)
- Srivastava, A., et al. (2023). Beyond the Imitation Game (BIG-bench). (benchmark ecosystem)
- Balloccu, S., et al. (2024). Leak, cheat, repeat: Data contamination and evaluation malpractices in closed-source LLMs. EACL.
- Jacovi, A., et al. (2023). Stop uploading test data in plain text. EMNLP.
- de la Torre, J. (2011). The generalized DINA model framework. Psychometrika. (cognitive diagnostic models)
- Platt, J. (1999). Probabilistic outputs for SVMs. (ML calibration disambiguation)

### Scores (AAAI 1-10 scale)
- Novelty: 5/10
- Related Work: 5/10
- Clarity: 6/10
- Overall recommendation: 5/10
- Confidence: 4/5

**Rationale:** The paper addresses a genuine and important gap — no existing method produces calibrated benchmark scores with uncertainty quantification under contamination. The signal survival analysis is a genuinely novel empirical contribution. The framework design is sound and well-grounded in educational measurement. However, the methodological novelty is primarily integrative: each component (RRF, 4PL IRT, measurement error, Bayesian inference) is borrowed from existing literature, and the three structural adaptations from educational IRT are individually either standard or engineering decisions rather than modeling contributions. The related work has improved substantially from earlier drafts (the paper draft now cites ~23 works versus the dream paper's ~10) but still has important gaps in DIF, ML calibration disambiguation, conformal prediction, and data attribution. "Dual-track validation" is experimental design, not a distinct contribution. At AAAI's 17.6% acceptance rate, the novelty is borderline — the paper reads more as a "competent integration of existing components for an important new application" than as a paper introducing fundamentally new methodology. The signal survival analysis partially compensates, but its descriptive (rather than explanatory) character limits its weight. A strong revision that (a) engages with DIF literature, (b) provides the Fisher Information derivation, (c) adds mechanistic depth to signal survival analysis, and (d) is more candid about the integrative nature of the contribution could push this into weak accept territory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af682191-9f67-43d7-bd00-31e239ae3453",
  "isSidechain": true,
  "agentId": "a3c902c84adde37f7",
  "requestId": "req_011Cb11ZHLPz5Y4YZVWYUZUf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c91ac250-bcc6-4f03-bc47-32cd4ee0b6b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "b9ccf268-5683-443e-bd9f-276396e78020",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lm5qF779Nio5Ev76zWhKwe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12206,
      "cache_read_input_tokens": 55034,
      "output_tokens": 3980,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12206
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3980,
          "cache_read_input_tokens": 55034,
          "cache_creation_input_tokens": 12206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12206,
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
