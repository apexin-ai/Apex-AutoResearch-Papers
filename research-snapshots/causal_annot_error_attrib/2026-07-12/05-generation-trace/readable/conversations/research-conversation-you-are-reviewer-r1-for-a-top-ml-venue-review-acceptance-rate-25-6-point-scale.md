# Research conversation: You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a3d9dc7c1ad2f4c98.jsonl`
- **Structured JSON:** [`719455b7b2b483d72ea9.json`](../../sessions/71/719455b7b2b483d72ea9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

55 recorded events

### User

_source line 1 · 2026-05-20T08:57:11.590Z_

You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus areas are **Methods** and **Experiments**.

## Paper Summary

**Title:** "Multi-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies"

**Authors:** Anonymous (11 pages)

**Three contributions:**
1. **Multi-class bias taxonomy** — Closed-form bias expressions for K=3 and matrix-form for general K, across 6 canonical DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door). Key finding: exposure misclassification is the only topology where non-differential K≥3 error produces direction reversal (85% reversal rate in 100K random confusion matrices). The remaining 5 topologies preserve bias direction but vary in magnitude. Theory matches MC in 32/42 (76%) topology-structure combinations.

2. **Annotation Sensitivity Values (ASVs)** — analogous to E-values for unmeasured confounding. Quantifies minimum annotation error amplification δ to overturn a conclusion. Formal monotonicity+sharpness proved for confounding; monotonicity for mediation/instrument; collider fails monotonicity in 7% of C structures; front-door 3% violations. Aggregate 95% coverage = 0.85 across all 6 topologies.

3. **Correction guidance framework + toolkit** — Decision framework mapping {topology × error structure × ASV} → correction methods (MLA, PPI, DSL, gold labels). 78% accuracy (vs 65% trivial "always MLA" baseline). Identifies 12% of scenarios where no existing method is adequate. Open-source `annot-sensitivity` Python toolkit, pip-installable, K=2–15, 6 topologies.

**Empirical validation:** 3 LLMs (Llama 4 Maverick, Qwen 3.5 Plus, DeepSeek V4) × 3 CSS tasks (protest event coding K=5, stance detection K=3, toxicity K=2), ~270K annotations. All empirical confusion matrices are diagonal-dominant. Inter-model error κ = 0.58–0.67. Downstream bias >0.05 in 2–3/9 combinations. No direction reversal observed. ASV: 5/9 trivially robust (>50), 4/9 meaningful, perfect concordance on meaningful cases.

## Key Tables and Results

**Table 1 (Bias Taxonomy):** 6 topologies. Exposure: 85% reversal, bias range -0.84 to 0.42, "Unpredictable". All others: 0% reversal, monotone direction classes. Theory-MC match: confounding 6/6, exposure 5/6, mediation 5/6, collider 4/6, M-bias 4/6, instrument 5/6, front-door 3/6.

**Table 2 (Theory-MC Detail):** 32/42 (76%) match. Mismatches in complex topologies with extreme C structures (near-permutation, block-diagonal, asymmetric).

**Table 3 (Eigendecomposition for K=5,7):** Confounding: dominant eigenvalue captures ≥76% variance through K=7. Collider: only 49% at K=7, needs 4 modes for 90%. Worst-case bounds grow 1.8–3.2× conservative.

**Table 4 (Binarization):** Max delta = 0.091 (confounding, K=7). 4/6 topologies exceed Δ=0.05. No direction reversal from binarization. Only K=3 reported for 5 of 6 topologies (K=5,7 missing for non-confounding).

**Tables 5–6 (ASV):** Confounding: formal monotonicity + sharpness, coverage 0.88/0.93/0.97. Mediation: formal monotonicity, no sharpness (1.4–1.8× conservative). Collider: 7% monotonicity violations, coverage 0.74/0.78/0.85. M-bias: monotone (0/1000), conservative (1.6–2.1×), cov95=0.86. Instrument: monotone, near-sharp (1.1×), cov95=0.88. Front-door: 3% violations, conservative (1.8–2.4×), cov95=0.76.

**Table 7 (Spectral):** λ₂/λ₁ > 0.6 predicts exposure reversal (AUC=0.92). Diagonal dominance <0.45 (AUC=0.89). For other topologies, λ₁ and spectral gap predict bias magnitude (R²=0.78).

**Tables 8–10 (Empirical):** All confusion matrices diagonal-dominant (0.74–0.87). Accuracy 0.68–0.88. Max downstream bias = 0.12 (protest/Qwen). No reversal.

**Table 11 (ASV Calibration):** 5/9 trivially robust (ASV>50), 4 meaningful: protest/Qwen ASV=2.3 (fragile), protest/Llama ASV=4.1 (moderate), protest/DeepSeek ASV=8.5 (moderate), stance/DeepSeek ASV=18.7 (robust).

**Table 12 (Correction Framework):** Overall accuracy 0.78, MLA fraction 0.65. Collider accuracy lowest (0.68). Exposure "no method" fraction 0.35.

## Experiment Design Reference (what the full design envisions)

The full experiment design includes 9 planned experiments:
1. Six-topology bias taxonomy (K=3) — covered
2. General-K matrix expressions (K=5,7) — partially covered (only 3 topologies)
3. Empirical confusion matrices (3 LLMs × 3 tasks) — covered
4. Binarization collapse analysis — partially covered (K=5,7 only for confounding)
5. ASV formal proofs (confounding, mediation, collider) — covered
6. ASV MC validation (M-bias, instrument, front-door) — covered
7. ASV empirical calibration — covered
8. Correction guidance framework — covered
9. Pathological confusion matrix analysis (spectral) — covered
10. annot-sensitivity Python toolkit — covered (described, not deeply evaluated)

## Your Task

Write a detailed review focusing on:

**Methods:**
- Soundness of the bias derivations and the theory-MC validation approach
- Appropriateness of the ASV definition and its formal properties
- Adequacy of the correction guidance framework design
- Any methodological gaps or questionable assumptions

**Experiments:**
- Completeness and rigor of the experimental evaluation
- Whether the empirical validation adequately supports the claims
- Statistical concerns (sample sizes, coverage calibration, etc.)
- Missing experiments or baselines

Structure your review as:
1. Summary (2–3 sentences)
2. Strengths (bulleted)
3. Weaknesses (bulleted, with severity: major/minor)
4. Questions for authors
5. Missing experiments or analyses
6. Preliminary score (1–6) with justification
7. Confidence (1–5)

Be rigorous but fair. This is a blind review — evaluate the paper on its merits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "12b03455-4fd9-46bc-b0ba-361ac9c8867e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T08:57:11.598Z_

```json
{
  "parentUuid": "12b03455-4fd9-46bc-b0ba-361ac9c8867e",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
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
  "uuid": "65cdacc3-0a70-434d-a67c-f7a8c849469b",
  "timestamp": "2026-05-20T08:57:11.598Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T08:57:14.588Z_



I'll start by reading the project files to understand the full paper and experimental details before writing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65cdacc3-0a70-434d-a67c-f7a8c849469b",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYTNB6Hi2atTw673C3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e28bbc9-66f8-4299-8142-a435dbfd8bde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Ptx8RUo6p5sMziR4wx6cB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8147,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8147,
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

_source line 4 · 2026-05-20T08:57:15.219Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HZ2Ep8yVNbStg5i8xRJiDV`</summary>

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
  "parentUuid": "3e28bbc9-66f8-4299-8142-a435dbfd8bde",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYTNB6Hi2atTw673C3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bd980af-f961-4458-a736-1d841b417253",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Ptx8RUo6p5sMziR4wx6cB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8147,
      "cache_read_input_tokens": 8250,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8147
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 8147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8147,
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

_source line 5 · 2026-05-20T08:57:15.225Z_

<details><summary>↩ Tool result · `toolu_01HZ2Ep8yVNbStg5i8xRJiDV`</summary>

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
  "parentUuid": "5bd980af-f961-4458-a736-1d841b417253",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "b95c2df7-d0b3-4006-8ae2-ab5f56d53e82",
  "sourceToolAssistantUUID": "5bd980af-f961-4458-a736-1d841b417253",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T08:57:18.423Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01BSAfCDzWPxKumrWWnYMQms`</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b95c2df7-d0b3-4006-8ae2-ab5f56d53e82",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYTdv8wNDzk2zz4HQMb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d3db2be-dcf3-4718-9ba8-81726368a602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173YVMeiH6vQuhVtk1Epj5D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 16397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 7 · 2026-05-20T08:57:18.455Z_

<details><summary>↩ Tool result · `toolu_01BSAfCDzWPxKumrWWnYMQms`</summary>

```text
{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (3 个)\n\n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **mvp_exposure_dirichlet_subspace** (success): Dirichlet(1,1,1) 均匀先验下 85% 违反率在高对角占优子空间（min(diag(C))≥0.7，接近真实 LLM 精度）是否骤降：若 >10% 则论文 claim 对实际 LLM 有现实意义，若 <1% 需标注适用范围\n- **mvp_exposure_dag** (success): K=3 非差异性 exposure 误分类打破二分类 bias-toward-null 保证：存在 C 结构使 treatment effect 估计产生符号反转或效应放大，而 K=2 下非差异性误分类始终保证衰减\n- **mvp_confounding_dag** (success): K=3 混淆矩阵下 confounding DAG 的 OLS 偏差可由 plim=(E[Z'Z])^{-1}E[Z'X]β 精确预测，且 K=3 偏差与二分类折叠偏差系统性不同（多分类保留更多混杂信息）\n\n## 趋势\n成功 3 / 负向 0 / 失败 0 / 共 3\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d3db2be-dcf3-4718-9ba8-81726368a602",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "a29df77c-875d-409e-8e42-895ce1c8d859",
  "sourceToolAssistantUUID": "9d3db2be-dcf3-4718-9ba8-81726368a602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T08:57:19.064Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MmDyaECj7kAjybTS2x9DUZ`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a29df77c-875d-409e-8e42-895ce1c8d859",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYTdv8wNDzk2zz4HQMb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef968efe-11b3-4254-9d01-b76e7504a506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173YVMeiH6vQuhVtk1Epj5D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 16397,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1450
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 170,
          "cache_read_input_tokens": 16397,
          "cache_creation_input_tokens": 1450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1450,
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

_source line 9 · 2026-05-20T08:57:19.074Z_

<details><summary>↩ Tool result · `toolu_01MmDyaECj7kAjybTS2x9DUZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_exposure_dirichlet_subspace** (success): Dirichlet(1,1,1) 均匀先验下 85% 违反率在高对角占优子空间（min(diag(C))≥0.7，接近真实 LLM 精度）是否骤降：若 >10% 则论文 claim 对实际 LLM 有现实意义，若 <1% 需标注适用范围\\n- **mvp_exposure_dag** (success): K=3 非差异性 exposure 误分类打破二分类 bias-toward-null 保证：存在 C 结构使 treatment effect 估计产生符号反转或效应放大，而 K=2 下非差异性误分类始终保证衰减\\n- **mvp_confounding_dag** (success): K=3 混淆矩阵下 confounding DAG 的 OLS 偏差可由 plim=(E[Z'Z])^{-1}E[Z'X]β 精确预测，且 K=3 偏差与二分类折叠偏差系统性不同（多分类保留更多混杂信息）\\n\\n## 趋势\\n成功 3 / 负向 0 / 失败 0 / 共 3\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nhome-1x5090: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 652, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef968efe-11b3-4254-9d01-b76e7504a506",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "b29933b0-238a-4a55-aac6-3202902a53f3",
  "sourceToolAssistantUUID": "ef968efe-11b3-4254-9d01-b76e7504a506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T08:57:22.280Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01291FULSN5n84hrsmynpXAf`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b29933b0-238a-4a55-aac6-3202902a53f3",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYTvDR5ERb9DYca1Tph",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ee396ac-530c-421f-a7f6-78124ead093c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnZ7XVaGgB9xCtSmU51h6T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1478,
      "cache_read_input_tokens": 17847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1478,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 11 · 2026-05-20T08:57:22.289Z_

<details><summary>↩ Tool result · `toolu_01291FULSN5n84hrsmynpXAf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/ROADMAP.md\", \"content\": \"# causal_annot_error_attrib — Research Dashboard\\n\\n> 最后更新: 2026-05-20 07:40 UTC | 更新原因: Exposure DAG 确认方向反转，Version A framing 成立，更新进展和风险\\n\\n## 核心方向\\n多分类 LLM 标注误差在因果推断中的偏差传播：推导 K×K 混淆矩阵在 6 种 DAG 拓扑下的偏差表达式，构建 Annotation Sensitivity Values (ASVs) 灵敏度分析框架。详见 paper_framing.md。\\n\\n## 当前阶段：Research（MVP 2026-05-20 通过）\\n\\n### 核心假设验证状态\\n- ✅ **方向反转已确认（D004）**：Exposure DAG K=3 — 85% random C 违反 bias-toward-null，83.4% 符号反转\\n- ✅ **二分类保证仍成立**：K=2 exposure DAG 6/6 toward null\\n- ✅ **拓扑依赖性验证**：Confounding DAG 单调 vs Exposure DAG 不可预测\\n- ✅ **折叠损失**：K=3 vs binary Δ up to 0.103\\n- → **Version A framing 确认**（D003 checkpoint resolved）\\n\\n### Target Venue\\n- Primary: AAAI 2027（abstract 2026-07-21, paper 2026-07-28, ~62 天）\\n- Secondary: ARR October 2026（→ NAACL/ACL 2027）\\n\\n### Core Claims（详见 paper_framing.md）\\n1. Multi-class bias taxonomy — 6 DAG 拓扑 × K×K 混淆矩阵结构交互（**核心已验证**）\\n2. Annotation Sensitivity Values (ASVs) — 标注误差灵敏度分析\\n3. Correction guidance framework — 诊断驱动的纠偏方法选择\\n\\n### 实验覆盖（详见 experiment_plan.yaml）\\n- P0: plan_001(6 DAG K=3), plan_003(3 LLM实证), plan_004(ASV证明), plan_006(ASV实证), plan_008(二分类折叠)\\n- P1: plan_002(K=5,7), plan_005(ASV扩展), plan_007(纠偏框架), plan_010(工具包)\\n- P2: plan_009(病态C分析)\\n\\n## 当前进展\\n- ✅ MVP 通过（D001）— confounding DAG 框架验证\\n- ✅ Exposure DAG 方向反转确认（D002/D004）— Claim 1 最强形式成立\\n- ✅ paper_framing.md 双版本 → Version A 确认\\n- ✅ experiment_plan.yaml 10 个实验\\n- ⏳ Dream 模拟运行中（dream_20260520T072911，full review）\\n- ⏳ 等 Dream 回调后审批 P0 实验\\n\\n## 近期任务\\n- [ ] 等 Dream 回调 → 评估 framing/plan 是否需调整\\n- [ ] Dream 通过后：派 Agent 启动 plan_001（剩余 4 canonical DAG 拓扑推导 + MC）\\n- [ ] 并行：plan_003 金标数据获取确认（ACLED ToS / SemEval / Civil Comments）\\n- [ ] 并行：plan_003 API key 准备（Llama 4 / Qwen 3.5 / DeepSeek V4）\\n\\n## GPU 预算\\n本项目 GPU 需求极低（总计 15-30h）。当前 0 GPU 分配。\\n服务器：home-1x5090（sonny），已绑定但未部署项目代码。\\n\\n## 关键风险\\n1. ~~方向反转是否出现~~ → ✅ 已确认（exposure DAG 85%）\\n2. Lee & Wood-Doughty (2024) 重叠 → 已区分 observed vs unobserved confounding\\n3. AAAI DDL 62 天 → 关键路径：plan_001(~5d) → plan_004(~7d) → plan_006(~3d)，留 ~47 天写论文\\n4. plan_004 ASV sharpness 证明可能卡住 → 退路：MC-validated conjectures（framing 已预留）\\n5. Brenner (1993) 精确引用需核实 → 论文撰写时处理\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D004 | 2026-05-20 | D003 checkpoint 提前解决：Version A 成立，exposure DAG K=3 | art_20260520_207c62, art_20260520_f08c30 |\\n| D003 | 2026-05-20 | plan_001 完成后设 checkpoint gate：方向反转拓扑数 → framing 版本 | plan_001 |\\n| D002 | 2026-05-20 | Research 阶段第一优先级：exposure misclassification DAG K= | — |\\n| D001 | 2026-05-20 | MVP PASS — Confounding DAG K=3 理论框架验证通过，进入 researc | — |\\n\\n\\n\", \"total_chars\": 2489, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ee396ac-530c-421f-a7f6-78124ead093c",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "ced8c347-1c2f-4bca-963f-e2697aaa7b6b",
  "sourceToolAssistantUUID": "7ee396ac-530c-421f-a7f6-78124ead093c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T08:57:23.228Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Mys9SpUtDN2LU78owDNwn9`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ced8c347-1c2f-4bca-963f-e2697aaa7b6b",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYTvDR5ERb9DYca1Tph",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78ae0bdb-48ab-4d62-9d51-7ab3a9fea524",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnZ7XVaGgB9xCtSmU51h6T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1478,
      "cache_read_input_tokens": 17847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1478,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 13 · 2026-05-20T08:57:23.239Z_

<details><summary>↩ Tool result · `toolu_01Mys9SpUtDN2LU78owDNwn9`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'causal_annot_error_attrib'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78ae0bdb-48ab-4d62-9d51-7ab3a9fea524",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "5d37b8ae-202f-4a06-a22b-deff2cbb6f9e",
  "sourceToolAssistantUUID": "78ae0bdb-48ab-4d62-9d51-7ab3a9fea524",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T08:57:23.868Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013bHYZLyCw6WCr8S2DSPwbR`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d37b8ae-202f-4a06-a22b-deff2cbb6f9e",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYTvDR5ERb9DYca1Tph",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7395525d-fca3-4c45-995a-e282faa4e0f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnZ7XVaGgB9xCtSmU51h6T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1478,
      "cache_read_input_tokens": 17847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1478,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 15 · 2026-05-20T08:57:23.879Z_

<details><summary>↩ Tool result · `toolu_013bHYZLyCw6WCr8S2DSPwbR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/memory.md\", \"content\": \"# Project Memory\\n\\n## MVP 验证发现 (2026-05-20)\\n\\n### Exposure DAG: bias-toward-null 保证在 K=3 下失效（核心发现）\\n**100k 随机 C 搜索：85% 违反 bias-toward-null，83.4% 产生符号反转。** 二分类 K=2 下全部满足 toward null 保证。\\n\\n具体 named structure 结果：\\n- C3_STRUCTURAL_12: β_2=-0.5 → γ̂_2=+0.06（符号反转）\\n- C4_WEAK_DIAG: β_1=1.0 → γ̂_1≈0（近消失）\\n- C5_NEAR_PERM: β_2=-0.5 → γ̂_2=+1.25（符号反转 + 2.5x 放大，最极端）\\n\\n极端随机案例：β_1=1.0 → γ̂_1=-0.84（符号反转），severity=2.83x。\\n\\n**关键洞察**：exposure 误分类场景（A→Y）下，多分类 C 矩阵的交叉污染使得回归将某类的 Y 值归因到错误标签，产生符号反转。这在二分类中不可能发生（只有 2 个类，误标只导致衰减）。\\n\\n### Dirichlet 子空间分析：高精度 LLM 仍有显著违反（关键补充）\\n**即使 min(diag(C))≥0.9（对应高精度 LLM），amplification 违反率仍达 11.9%。** 分层结果：\\n\\n| 子空间 | 违反率 | 符号反转 | 放大 |\\n|--------|--------|----------|------|\\n| 全空间 | 84.9% | 83.3% | 27.5% |\\n| diag≥0.5 | 32.5% | 21.6% | 11.3% |\\n| diag≥0.7 | 13.7% | 2.1% | 11.7% |\\n| diag≥0.9 | 11.9% | 0.0% | 11.9% |\\n\\n**关键 pattern**：随着 C 对角占优增加，符号反转迅速消失（diag≥0.9 降至 0%），但 amplification 保持稳定在 ~12%。这意味着：\\n- 低精度 LLM（<70%）：符号反转是主要风险\\n- 高精度 LLM（>90%）：符号反转消除，但 amplification 持久存在\\n- **论文 framing 可以声称：即使 LLM 精度 >90%，multiclass 效应放大仍以 >10% 概率发生**\\n\\n采样方法：truncated Beta(1,2) 直接采样（非 rejection sampling），50k samples/subspace。首版 rejection sampling 因 diag≥0.9 接受率 ~10⁻⁶ 导致 OOM。\\n\\n### Confounding DAG: 偏差方向性质（对比发现）\\n100k 随机 C 搜索均未发现负偏差。Confounding DAG (A→T, A→Y, T→Y) 中，K=3 误分类偏差始终与 OVB 同向。量级差异显著（K=3 偏差 0.13-0.30 vs binary collapse 0.24-0.30），但无方向反转。\\n\\n**两个 DAG 的差异**：confounding DAG 下 A 通过 T 间接影响 Y，误分类 A 导致残余混杂但方向固定；exposure DAG 下 A 直接决定 Y 的期望，标签交换直接翻转效应估计。\\n\\n### Lee & Wood-Doughty (2024) 技术区分\\n本项目：observed exposure/confounder with noisy LLM annotation（A 可观测，A* 用于规模化）。LWD：unobserved confounding with proxy（A 不可观测）。关键区别：我们的 C 是可从 validation data 估计的 design parameter。\\n\\n### DGP 参数\\n- Confounding DAG: P(A)=[0.4, 0.35, 0.25], alpha=[1.5, -1.0], beta_T=2.0, beta_A=[1.0, -0.5], sigma=1.0\\n- Exposure DAG: P(A)=[0.4, 0.35, 0.25], beta=[0, 1.0, -0.5], sigma_Y=1.0\\n\", \"total_chars\": 1842, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7395525d-fca3-4c45-995a-e282faa4e0f0",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "ec0169f4-26c5-4b8a-b488-5df3ff22da7b",
  "sourceToolAssistantUUID": "7395525d-fca3-4c45-995a-e282faa4e0f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T08:57:24.335Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SNfuj2213frhhfbP9gadXA`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec0169f4-26c5-4b8a-b488-5df3ff22da7b",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYTvDR5ERb9DYca1Tph",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f317c0fa-b992-4350-8ff0-b4d62ea88dd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnZ7XVaGgB9xCtSmU51h6T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1478,
      "cache_read_input_tokens": 17847,
      "output_tokens": 398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1478
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 398,
          "cache_read_input_tokens": 17847,
          "cache_creation_input_tokens": 1478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1478,
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

_source line 17 · 2026-05-20T08:57:24.345Z_

<details><summary>↩ Tool result · `toolu_01SNfuj2213frhhfbP9gadXA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/paper_framing.md\", \"content\": \"# Paper Framing — causal_annot_error_attrib\\n\\n## Target Venue\\n- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)\\n- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)\\n- Tertiary: ICWSM 2027 Round 2 (2026-09-15)\\n\\n## Title\\nMulti-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies\\n\\n## Core Claims (3 条)\\n\\n1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 6 canonical social-science DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door).\\n\\n2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of differential annotation error needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Reported alongside estimates, analogous to E-values for unmeasured confounding. Formal proofs (monotonicity + sharpness) for 3 priority topologies; MC-validated conjectures for the remaining 3.\\n\\n3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI, MLA, naive plug-in), characterizing regimes where each applies and where no existing method suffices — including dependence-aware multi-LLM correction as an open problem.\\n\\n## Story Spine\\n\\n- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31% of downstream conclusions are already incorrect. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable.\\n\\n- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.\\n\\n- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.\\n\\n- **Headline result template**: \\\"Across 6 DAG topologies with K=3,5,7, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. On 3 CSS tasks annotated by 3 LLMs, ASVs provide calibrated robustness indicators, and our taxonomy identifies cases where commonly applied corrections would increase rather than decrease bias.\\\"\\n\\n## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001\\n\\n### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)\\nThe binary guarantee that \\\"non-differential exposure misclassification biases toward the null\\\" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification (\\\"bias can go in either direction\\\"); we provide the first systematic characterization across 6 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to \\\"escape\\\" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).\\n\\n### Version B (no direction reversal found across topologies)\\nMulti-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.\\n\\n**Gate**: plan_001 results determine which version. ≥2 topologies with reversal → A; 1 → A with that topology as lead; 0 → B. See D003.\\n\\n## MVP Evidence\\n\\n**Confounding DAG + K=3** (confounder misclassification):\\n- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated\\n- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization\\n- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is \\\"well-behaved\\\" (predictable direction)\\n- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.\\n\\n**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):\\n- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification\\n- K=2 control: 6/6 toward null (binary guarantee holds)\\n- Worst case: β=1.0 → estimate=-0.84 (sign reversal + 2.83x amplification)\\n- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)\\n- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim\\n\\n**Dirichlet subspace analysis** (practical relevance validation):\\n- diag≥0.5: 32.5% violation, 21.6% sign reversal, 11.3% amplification\\n- diag≥0.7 (typical LLM accuracy): **13.7% violation**, 2.1% sign reversal, **11.7% amplification**\\n- diag≥0.9 (high-accuracy LLM): **11.9% violation**, 0% sign reversal, **11.9% amplification**\\n- Key pattern: sign reversal vanishes at high accuracy, but **amplification persists at ~12% regardless of accuracy**\\n- Implication: even 90%+ accuracy LLMs face non-trivial effect amplification risk — no \\\"safe accuracy threshold\\\" exists\\n\\n## Venue Fit Risks\\n\\n- **AAAI**: Broad AI audience — emphasize general methodology for \\\"automated annotation measurement error,\\\" not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.\\n- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.\\n- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.\\n\\n## Anticipated Reviewer Concerns & Planned Responses\\n\\n1. **\\\"Trivial extension of binary to multi-class\\\"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 6 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]\\n\\n2. **\\\"Lee & Wood-Doughty (2024) already did categorical\\\"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 6 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]\\n\\n3. **\\\"Why these 6 DAG topologies?\\\"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]\\n\\n4. **\\\"K≥5 expressions aren't actionable\\\"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]\\n\\n5. **\\\"ASV sharpness only proved for 3 topologies\\\"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]\\n\\n6. **\\\"Correlated multi-LLM errors?\\\"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]\\n\\n7. **\\\"Empirical validation scope\\\"** → 3 CSS tasks × 3 LLMs × 3 DAG-relevant scenarios. Tasks selected to cover K=2,3,5 annotation complexity. [Experiments: plan_003, plan_006]\\n\", \"total_chars\": 10212, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f317c0fa-b992-4350-8ff0-b4d62ea88dd3",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "578f5441-a777-4d2b-a98d-9e80107cffa3",
  "sourceToolAssistantUUID": "f317c0fa-b992-4350-8ff0-b4d62ea88dd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T08:57:27.236Z_

Now let me read the experiment plan, any artifacts, and the literature map for deeper understanding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "578f5441-a777-4d2b-a98d-9e80107cffa3",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYUJeYBZtAnDTF4PJZF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd2096ec-db5e-45b6-a5f7-e63911b2c776",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5nzatJTTdGDpzPGmxCTgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6640,
      "cache_read_input_tokens": 19325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6640,
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

_source line 19 · 2026-05-20T08:57:28.139Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017DkzqzJJCWxTLdeHke9UGj`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd2096ec-db5e-45b6-a5f7-e63911b2c776",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYUJeYBZtAnDTF4PJZF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea28aa7f-296d-4a56-84ce-d06ea9077374",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5nzatJTTdGDpzPGmxCTgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6640,
      "cache_read_input_tokens": 19325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6640,
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

_source line 20 · 2026-05-20T08:57:28.149Z_

<details><summary>↩ Tool result · `toolu_017DkzqzJJCWxTLdeHke9UGj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/literature_map.yaml\", \"content\": \"papers:\\n  wood_doughty2018:\\n    title: \\\"Challenges of Using Text Classifiers for Causal Inference\\\"\\n    authors: [\\\"Wood-Doughty, Z.\\\", \\\"Shpitser, I.\\\", \\\"Dredze, M.\\\"]\\n    year: 2018\\n    venue: \\\"EMNLP\\\"\\n    category: \\\"causal-text-classification\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"First to apply DAG reasoning to text classifier measurement error; no formal bias theorems or identifiability conditions; binary only. Direct predecessor — our work extends to multi-class with formal bias expressions.\\\"\\n    abstract: \\\"Applies causal DAG reasoning to analyze how text classifier errors propagate to downstream causal estimates. Proposes matrix adjustment correction but notes severe instability.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    arxiv_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  teblunthuis2024:\\n    title: \\\"Misclassification in Automated Content Analysis Causes Bias in Regression. Can We Fix It? Yes We Can!\\\"\\n    authors: [\\\"TeBlunthuis, N.\\\", \\\"Hase, V.\\\", \\\"Chan, C.\\\"]\\n    year: 2024\\n    venue: \\\"Communication Methods and Measures\\\"\\n    category: \\\"causal-text-classification\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Most complete binary treatment: 4 DAG scenarios (differential/non-differential × IV/DV), testable conditions, MLA method. But binary only, single classifier. Our work generalizes to multi-class K×K confusion matrices.\\\"\\n    abstract: \\\"Provides four DAG scenarios for text classifier measurement error with likelihood ratio tests and Maximum Likelihood Adjustment (MLA) correction for binary classification.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    arxiv_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  hernan_cole2009:\\n    title: \\\"Causal Diagrams and Measurement Bias\\\"\\n    authors: [\\\"Hernán, M.A.\\\", \\\"Cole, S.R.\\\"]\\n    year: 2009\\n    venue: \\\"American Journal of Epidemiology\\\"\\n    doi: \\\"10.1093/aje/kwp293\\\"\\n    category: \\\"measurement-error-epidemiology\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Formalizes starred-node DAGs with differential/non-differential and independent/dependent error taxonomy. Core theoretical foundation for our DAG-based framework.\\\"\\n    abstract: \\\"Formalizes the use of causal DAGs for reasoning about measurement bias, introducing starred-node notation and taxonomy of error types.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  vanderweele_li2019:\\n    title: \\\"Simple Sensitivity Analysis for Differential Measurement Error\\\"\\n    authors: [\\\"VanderWeele, T.J.\\\", \\\"Li, Y.\\\"]\\n    year: 2019\\n    venue: \\\"American Journal of Epidemiology\\\"\\n    doi: \\\"10.1093/aje/kwz062\\\"\\n    category: \\\"sensitivity-analysis\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Provides sensitivity bounds for differential measurement error using risk ratios, but only for binary exposure/outcome. Our ASV framework extends this to multi-class confusion matrices.\\\"\\n    abstract: \\\"Develops simple sensitivity analysis techniques for differential measurement error in binary exposure/outcome settings using risk ratios.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  vanderweele_ding2017:\\n    title: \\\"Sensitivity Analysis in Observational Research: Introducing the E-Value\\\"\\n    authors: [\\\"VanderWeele, T.J.\\\", \\\"Ding, P.\\\"]\\n    year: 2017\\n    venue: \\\"Annals of Internal Medicine\\\"\\n    doi: \\\"10.7326/M16-2607\\\"\\n    category: \\\"sensitivity-analysis\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Introduces E-values for unmeasured confounding — the sensitivity analysis paradigm our ASVs mirror for annotation-induced bias.\\\"\\n    abstract: \\\"Proposes the E-value as an interpretable sensitivity analysis measure for unmeasured confounding in observational studies.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  brenner1993:\\n    title: \\\"Bias due to non-differential misclassification of polytomous confounders\\\"\\n    authors: [\\\"Brenner, H.\\\"]\\n    year: 1993\\n    venue: \\\"Journal of Clinical Epidemiology\\\"\\n    doi: \\\"10.1016/0895-4356(93)90148-T\\\"\\n    category: \\\"measurement-error-epidemiology\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Key result: non-differential misclassification of polytomous confounders can bias in EITHER direction — breaks the binary 'toward null' guarantee. Core motivation for our multi-class taxonomy.\\\"\\n    abstract: \\\"Analyzes bias from non-differential misclassification of polytomous confounders, showing bias can go in either direction unlike the binary case.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  veirod_laake2001:\\n    title: \\\"Exposure misclassification: bias in category specific Poisson regression coefficients\\\"\\n    authors: [\\\"Veierød, M.B.\\\", \\\"Laake, P.\\\"]\\n    year: 2001\\n    venue: \\\"Statistics in Medicine\\\"\\n    doi: \\\"10.1002/sim.900\\\"\\n    category: \\\"measurement-error-epidemiology\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Derives bias expressions for multi-category exposure misclassification in Poisson regression — bias depends on ALL true coefficients weighted by full misclassification matrix. We extend from regression-only to full DAG-based causal framework.\\\"\\n    abstract: \\\"Proves that multi-category exposure misclassification produces bias depending on all true category-specific coefficients weighted by the full misclassification probability matrix.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  baumann2025:\\n    title: \\\"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation\\\"\\n    authors: [\\\"Baumann, M.\\\", \\\"Röttger, P.\\\", \\\"Urman, A.\\\", \\\"Wendsjö, S.\\\", \\\"Plaza-del-Arco, F.M.\\\", \\\"Gruber, N.\\\", \\\"Hovy, D.\\\"]\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2509.08825\\\"\\n    category: \\\"llm-annotation-quality\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Strongest empirical motivation: 37 tasks, 21 studies, 13M labels, 18 models — 31% incorrect downstream conclusions with SOTA LLMs. Coins 'LLM hacking'. Diagnoses the problem we solve.\\\"\\n    abstract: \\\"Demonstrates across 37 annotation tasks from 21 published social science studies that approximately 31% of hypotheses yield incorrect conclusions with SOTA LLMs, rising to 50% for smaller models.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  lee_wood_doughty2024:\\n    title: \\\"Categorical Variables and Measurement Error in Causal Inference with LLM Classifiers\\\"\\n    authors: [\\\"Lee, S.\\\", \\\"Wood-Doughty, Z.\\\"]\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2411.03004\\\"\\n    category: \\\"causal-text-classification\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Extends Wood-Doughty (2018) to categorical + LLM classifiers on MIMIC clinical data. But covers only 1 DAG topology (unobserved confounding), no bias taxonomy, no sensitivity analysis. Key differentiation target.\\\"\\n    abstract: \\\"Extends causal measurement error framework to categorical text classifiers and LLMs, applied to clinical NLP on MIMIC data.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  gligoric2025:\\n    title: \\\"Can Unconfident LLM Annotations Be Used for Confident Conclusions?\\\"\\n    authors: [\\\"Gligorić, K.\\\", \\\"Jurafsky, D.\\\", \\\"Zou, J.\\\"]\\n    year: 2025\\n    venue: \\\"NAACL\\\"\\n    category: \\\"llm-annotation-correction\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Notes correlated errors bias estimates, proposes DSL/PPI corrections. One of the correction methods our guidance framework evaluates.\\\"\\n    abstract: \\\"Investigates when LLM annotations with varying confidence can still yield valid downstream conclusions, proposing design-based supervised learning and prediction-powered inference corrections.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  messing2026:\\n    title: \\\"Hidden Measurement Error in LLM Pipelines\\\"\\n    authors: [\\\"Messing, S.\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2604.11581\\\"\\n    category: \\\"llm-annotation-quality\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Decomposes LLM pipeline variance via linear mixed models (item-judge interaction dominates at 44%). Explicitly excludes causal identification — the gap we fill.\\\"\\n    abstract: \\\"Decomposes variance in LLM annotation pipelines using linear mixed models, finding item-judge interaction dominates at 44%, but excludes causal identification.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  kim_garg2025:\\n    title: \\\"Correlated Errors in Large Language Models\\\"\\n    authors: [\\\"Kim, J.\\\", \\\"Garg, S.\\\", \\\"Peng, Y.\\\", \\\"Garg, N.\\\"]\\n    year: 2025\\n    venue: \\\"ICML\\\"\\n    arxiv_id: \\\"2506.07962\\\"\\n    category: \\\"llm-annotation-quality\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Shows models agree 60% when both err, larger models have highly correlated errors across architectures. Undermines ensemble-as-fix assumption — strengthens case that error STRUCTURE analysis (our contribution) is irreplaceable.\\\"\\n    abstract: \\\"Demonstrates that LLM errors are highly correlated across models, with 60% agreement when both err, challenging independence assumptions in ensemble methods.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\", \"total_chars\": 8959, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea28aa7f-296d-4a56-84ce-d06ea9077374",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "f7e5b17a-eb08-4354-999a-bb0b2845150a",
  "sourceToolAssistantUUID": "ea28aa7f-296d-4a56-84ce-d06ea9077374",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T08:57:29.143Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UFhvUENF3WGzRRbtiSA1Yw`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7e5b17a-eb08-4354-999a-bb0b2845150a",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYUJeYBZtAnDTF4PJZF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96fdaba0-e116-4e8a-b743-5ebf67e4d0ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5nzatJTTdGDpzPGmxCTgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6640,
      "cache_read_input_tokens": 19325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6640,
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

_source line 22 · 2026-05-20T08:57:29.163Z_

<details><summary>↩ Tool result · `toolu_01UFhvUENF3WGzRRbtiSA1Yw`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'causal_annot_error_attrib'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96fdaba0-e116-4e8a-b743-5ebf67e4d0ac",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "baff94c4-322c-4217-a632-727c72b6aeb7",
  "sourceToolAssistantUUID": "96fdaba0-e116-4e8a-b743-5ebf67e4d0ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T08:57:29.673Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014GW7jz2FRWRxk4XmbMBgfT`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "baff94c4-322c-4217-a632-727c72b6aeb7",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYUJeYBZtAnDTF4PJZF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "876f6b07-3d92-4aaa-be52-cde0ab64eb74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5nzatJTTdGDpzPGmxCTgQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6640,
      "cache_read_input_tokens": 19325,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6640
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 322,
          "cache_read_input_tokens": 19325,
          "cache_creation_input_tokens": 6640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6640,
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

_source line 24 · 2026-05-20T08:57:29.682Z_

<details><summary>↩ Tool result · `toolu_014GW7jz2FRWRxk4XmbMBgfT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/decisions.yaml\", \"content\": \"_next_id: 5\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 07:25 UTC\\n  summary: MVP PASS — Confounding DAG K=3 理论框架验证通过，进入 research 阶段\\n  rationale: 三项 pass 标准全部满足：(1) 理论预测 vs MC 95% CI 一致 5/5，(2) 所有非差异性 C 产生远离零偏差 0.20-0.30，(3)\\n    二分类折叠偏差与三分类预测显著不同（最大 Δ=0.089）。附加发现：100k 随机 C 矩阵搜索在 confounding DAG 下未发现方向反转——偏差始终与\\n    OVB 同向。这是有价值的 characterization result：confounding DAG 偏差方向可预测（单调），方向反转假设需要在其他\\n    DAG 拓扑（mediator、collider）中验证，属于 research 阶段的核心任务。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 07:30 UTC\\n  summary: Research 阶段第一优先级：exposure misclassification DAG K=3 验证 bias-toward-null\\n    是否在多分类下打破\\n  rationale: Reviewer 指出 MVP criterion 2 在 confounding DAG 下不具区分力（二分类也 pass）。\\\"Bias\\n    toward null\\\" 保证（Bross 1954）特指 exposure 误分类，正确测试需要 exposure DAG（A→Y，用 A* 替代 A）。若\\n    K=3 下此 DAG 出现方向反转或 bias-away-from-null 结构性差异，则 Claim 1 最强形式成立；若不出现，需重新框定核心 claim。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 07:31 UTC\\n  summary: plan_001 完成后设 checkpoint gate：方向反转拓扑数 → framing 版本选择\\n  rationale: 'Reviewer [severity: critical] 指出 plan_001 是存在性检验但无 kill criterion。当前\\n    core insight 依赖方向反转（\\\"binary guarantee breaks\\\"），但 MVP 已证明 confounding DAG 无反转。若\\n    6 拓扑全无反转，framing 需 pivot。三级响应：(A) ≥2 拓扑有反转 → 当前 framing 成立，方向反转为 lead finding；(B)\\n    1 拓扑有反转 → 该拓扑为 lead case，framing 可调整；(C) 0 拓扑有反转 → pivot 到版本 B：\\\"multi-class 偏差\\n    magnitude 不可由 binary 推算 + binarization 本身有害\\\"，方向反转降为 topology-specific finding。注意：0\\n    反转 ≠ 项目 kill——binarization inequality + magnitude unpredictability + ASVs 本身够一篇论文，但\\n    framing 必须诚实。'\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: gate\\n    result: pending\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-20 07:39 UTC\\n  summary: D003 checkpoint 提前解决：Version A 成立，exposure DAG K=3 确认方向反转（85% random C）\\n  rationale: Exposure misclassification DAG 结果：100k 随机 C 矩阵中 85% 违反 bias-toward-null，83.4%\\n    产生符号反转，14.1% 产生效应放大。K=2 对照全部 toward null（6/6）。最极端案例：β_1=1.0 → γ̂_1=-0.84（符号反转\\n    2.83x）。机制清晰：近置换 C 导致标签交换直接翻转效应方向，这在 K=2 中结构性不可能。D003 三级响应解析为 Version A（≥1 topology\\n    with reversal）。Core insight 确认：\\\"non-differential exposure misclassification biases\\n    toward null\\\" 保证在 K≥3 下打破。两个 DAG 已形成有力对比：confounding DAG 偏差单调可预测 vs exposure DAG\\n    偏差方向不可预测——验证\\\"偏差取决于 C 结构 × DAG 拓扑交互\\\"。\\n  related_experiments:\\n  - exp_id: art_20260520_207c62\\n    role: validation\\n    result: 85% bias-toward-null violation, 83.4% sign reversal\\n  - exp_id: art_20260520_f08c30\\n    role: baseline\\n    result: confounding DAG monotonic, no reversal\\n  depends_on:\\n  - D002\\n  - D003\\n\", \"total_chars\": 2539, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "876f6b07-3d92-4aaa-be52-cde0ab64eb74",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "6ef447ae-3f0e-4495-b3dc-1d5545bd5b9f",
  "sourceToolAssistantUUID": "876f6b07-3d92-4aaa-be52-cde0ab64eb74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T08:57:33.696Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013eeyRJNZvRKtH3ZsMBCVGx`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ef447ae-3f0e-4495-b3dc-1d5545bd5b9f",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYUhfPQoJnv5JMAWwnH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d6e0a7e-0052-45d4-b257-6c265c730fa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ht6j23fzdNErk82T9paMov",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5363,
      "cache_read_input_tokens": 25965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5363,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 26 · 2026-05-20T08:57:33.714Z_

<details><summary>↩ Tool result · `toolu_013eeyRJNZvRKtH3ZsMBCVGx`</summary>

```text
artifacts/_project/data/mvp_confounding_dag.py
artifacts/mvp_confounding_dag.py
artifacts/_project/data/mvp_exposure_dag.py
artifacts/mvp_exposure_dag.py
artifacts/_project/report/mvp_exposure_dirichlet_subspace.py
artifacts/mvp_exposure_dirichlet_subspace.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d6e0a7e-0052-45d4-b257-6c265c730fa2",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "59e4ae64-6599-4a18-8f52-5073b42dafb4",
  "sourceToolAssistantUUID": "5d6e0a7e-0052-45d4-b257-6c265c730fa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T08:57:34.278Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013UusbJANJAa2EriNZWSKJQ`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59e4ae64-6599-4a18-8f52-5073b42dafb4",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYUhfPQoJnv5JMAWwnH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f785a056-cdc5-4cc6-9f6c-2c09edf2d8ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ht6j23fzdNErk82T9paMov",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5363,
      "cache_read_input_tokens": 25965,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5363
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 25965,
          "cache_creation_input_tokens": 5363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5363,
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

_source line 28 · 2026-05-20T08:57:34.294Z_

<details><summary>↩ Tool result · `toolu_013UusbJANJAa2EriNZWSKJQ`</summary>

```text
literature_map.yaml
experiment_plan.yaml
decisions.yaml
mistakes.yaml
artifacts/manifest.yaml
registry.yaml
artifacts/dream_reports/dream_20260520T074549/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T074549/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T074549/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T074549/best/review_context.yaml
artifacts/dream_reports/dream_20260520T074549/median/review_context.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260520T074549/worst/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f785a056-cdc5-4cc6-9f6c-2c09edf2d8ef",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "a71a7687-7f71-4953-9055-e27f43916c95",
  "sourceToolAssistantUUID": "f785a056-cdc5-4cc6-9f6c-2c09edf2d8ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T08:57:37.615Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JBzE1WDUCsAF8fym4wLUTE`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "experiment_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a71a7687-7f71-4953-9055-e27f43916c95",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYV3BtcaE2tYwMZWcai",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9926ce14-0621-4171-a604-e0aafb3e0145",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfoUs6aehVso7maMWeGFbu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 505,
      "cache_read_input_tokens": 31328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 505,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
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

_source line 30 · 2026-05-20T08:57:37.623Z_

<details><summary>↩ Tool result · `toolu_01JBzE1WDUCsAF8fym4wLUTE`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9926ce14-0621-4171-a604-e0aafb3e0145",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "cabf9883-897e-4f79-a2c2-22ef2fe8e768",
  "sourceToolAssistantUUID": "9926ce14-0621-4171-a604-e0aafb3e0145",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T08:57:38.115Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VVfDXGkC5gd1sR7hRfKiuQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_exposure_dag.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cabf9883-897e-4f79-a2c2-22ef2fe8e768",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYV3BtcaE2tYwMZWcai",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb4c12c8-e895-4a63-b638-919cacbd5af0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfoUs6aehVso7maMWeGFbu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 505,
      "cache_read_input_tokens": 31328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 505,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
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

_source line 32 · 2026-05-20T08:57:38.121Z_

<details><summary>↩ Tool result · `toolu_01VVfDXGkC5gd1sR7hRfKiuQ`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	MVP Validation: Exposure Misclassification DAG — K=3 vs K=2
4	
5	Tests whether the binary "bias toward null" guarantee for non-differential
6	exposure misclassification breaks in the multiclass (K>=3) setting.
7	
8	== Technical Setting ==
9	A is the EXPOSURE/TREATMENT variable, measured with error via LLM annotation.
10	No confounders. Simplest possible misclassification scenario.
11	
12	  DAG: A -> Y, A -> A*
13	  DGP: Y = beta_0 + beta_1*1[A=1] + beta_2*1[A=2] + eps
14	  Misclassification: P(A*=j|A=i) = C[j,i], C column-stochastic
15	
16	Researcher regresses Y ~ 1 + 1[A*=1] + 1[A*=2] instead of Y ~ 1 + 1[A=1] + 1[A=2].
17	
18	== Binary Guarantee (K=2) ==
19	Non-differential misclassification of binary exposure guarantees bias toward
20	null: the estimated effect is attenuated (|gamma_hat| <= |beta|). This is
21	a classical result in measurement error literature.
22	
23	== Key Question ==
24	Does this guarantee extend to K=3? Or can certain confusion matrix structures
25	produce:
26	  - SIGN REVERSAL: sign(gamma_hat_k) != sign(beta_k)
27	  - AMPLIFICATION: |gamma_hat_k| > |beta_k|
28	
29	== Distinction from Lee & Wood-Doughty (2024) ==
30	We study OBSERVED exposure with noisy measurement (A observable, A* used at
31	scale). LWD study UNOBSERVED confounding with proxy (different identifiability).
32	
33	Dependencies: numpy
34	"""
35	
36	import numpy as np
37	from collections import OrderedDict
38	import time
39	
40	
41	# ============================================================
42	# DGP Parameters
43	# ============================================================
44	N_SAMPLES = 10_000
45	M_REPS = 1_000
46	N_RANDOM_SEARCH = 100_000
47	SEED = 42
48	
49	P_A = np.array([0.4, 0.35, 0.25])
50	BETA = np.array([0.0, 1.0, -0.5])    # beta_0, beta_1, beta_2
51	SIGMA_Y = 1.0
52	
53	
54	# ============================================================
55	# Confusion Matrix Structures (reused from confounding DAG MVP)
56	# ============================================================
57	
58	C1_SYMMETRIC_HIGH = np.array([
59	    [0.80, 0.10, 0.10],
60	    [0.10, 0.80, 0.10],
61	    [0.10, 0.10, 0.80],
62	])
63	C1_DESC = "Symmetric high-accuracy: diag=0.8, uniform off-diagonal=0.1"
64	
65	C2_ASYMMETRIC = np.array([
66	    [0.65, 0.05, 0.10],
67	    [0.30, 0.85, 0.10],
68	    [0.05, 0.10, 0.80],
69	])
70	C2_DESC = "Asymmetric: P(A*=1|A=0)=0.30 >> P(A*=0|A=1)=0.05"
71	
72	C3_STRUCTURAL_12 = np.array([
73	    [0.96, 0.01, 0.01],
74	    [0.02, 0.69, 0.30],
75	    [0.02, 0.30, 0.69],
76	])
77	C3_DESC = "Structural: classes 1<->2 heavily confused (0.30), class 0 clean"
78	
79	C4_WEAK_DIAG = np.array([
80	    [0.40, 0.35, 0.25],
81	    [0.35, 0.40, 0.35],
82	    [0.25, 0.25, 0.40],
83	])
84	C4_DESC = "Weak diagonal dominance: diag~0.4, non-uniform off-diagonal"
85	
86	C5_NEAR_PERM = np.array([
87	    [0.05, 0.05, 0.90],
88	    [0.90, 0.05, 0.05],
89	    [0.05, 0.90, 0.05],
90	])
91	C5_DESC = "Near-permutation: cyclic 0->1, 1->2, 2->0 (p=0.90)"
92	
93	C6_DIFF_BASE = np.array([
94	    [0.80, 0.10, 0.10],
95	    [0.10, 0.80, 0.10],
96	    [0.10, 0.10, 0.80],
97	])
98	C6_DESC = "Differential base (=C1 in non-diff exposure setting; Y-dependent in MC)"
99	
100	
101	def make_confusion_matrices():
102	    """6 confusion matrix structures."""
103	    matrices = OrderedDict([
104	        ("1_sym_high",   (C1_SYMMETRIC_HIGH, C1_DESC)),
105	        ("2_asymmetric", (C2_ASYMMETRIC,     C2_DESC)),
106	        ("3_struct_12",  (C3_STRUCTURAL_12,  C3_DESC)),
107	        ("4_weak_diag",  (C4_WEAK_DIAG,      C4_DESC)),
108	        ("5_near_perm",  (C5_NEAR_PERM,      C5_DESC)),
109	        ("6_diff_base",  (C6_DIFF_BASE,      C6_DESC)),
110	    ])
111	    for name, (C, _) in matrices.items():
112	        assert np.allclose(C.sum(axis=0), 1.0), f"{name}: columns don't sum to 1"
113	    return matrices
114	
115	
116	# ============================================================
117	# Theoretical bias (exact)
118	# ============================================================
119	def theoretical_bias_exposure(C, p_A, beta):
120	    """
121	    plim gamma = (E[Z'Z])^{-1} E[Z'X] beta
122	    Z = (1, D*_1, D*_2),  X = (1, D_1, D_2)
123	
124	    Returns: (plim_gamma, bias_vector)
125	    """
126	    p0, p1, p2 = p_A
127	    q = C @ p_A
128	
129	    EZZ = np.array([
130	        [1.0,  q[1], q[2]],
131	        [q[1], q[1], 0.0],
132	        [q[2], 0.0,  q[2]],
133	    ])
134	
135	    EZX = np.array([
136	        [1.0,  p1,            p2],
137	        [q[1], C[1, 1] * p1,  C[1, 2] * p2],
138	        [q[2], C[2, 1] * p1,  C[2, 2] * p2],
139	    ])
140	
141	    plim = np.linalg.solve(EZZ, EZX @ beta)
142	    return plim, plim - beta
143	
144	
145	# ============================================================
146	# Data generation & OLS
147	# ============================================================
148	def _generate_Astar(A, C, rng):
149	    """Vectorized A* sampling from confusion matrix."""
150	    probs = C[:, A]
151	    cum = np.cumsum(probs, axis=0)
152	    u = rng.uniform(size=len(A))
153	    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))
154	
155	
156	def _generate_Astar_diff_Y(A, Y, C_base, rng, factor=2.0):
157	    """Differential: Y > median => off-diagonal rates scaled by factor."""
158	    C_high = C_base.copy()
159	    for col in range(3):
160	        diag_val = C_high[col, col]
161	        off_sum = 1.0 - diag_val
162	        new_off_sum = min(off_sum * factor, 0.95)
163	        scale = new_off_sum / off_sum if off_sum > 0 else 1.0
164	        for row in range(3):
165	            if row != col:
166	                C_high[row, col] *= scale
167	        C_high[col, col] = 1.0 - sum(C_high[r, col] for r in range(3) if r != col)
168	
169	    Y_med = np.median(Y)
170	    high = Y > Y_med
171	    probs_low = C_base[:, A]
172	    probs_high = C_high[:, A]
173	    probs = np.where(high[np.newaxis, :], probs_high, probs_low)
174	    cum = np.cumsum(probs, axis=0)
175	    u = rng.uniform(size=len(A))
176	    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))
177	
178	
179	def ols_coefs(X, Y):
180	    """OLS coefficients."""
181	    return np.linalg.lstsq(X, Y, rcond=None)[0]
182	
183	
184	# ============================================================
185	# Monte Carlo
186	# ============================================================
187	def run_mc_exposure(M, N, C, p_A, beta, sigma_Y, seed, differential=False):
188	    rng = np.random.default_rng(seed)
189	    bias_misclass = np.empty((M, 3))
190	
191	    for m in range(M):
192	        A = rng.choice(3, size=N, p=p_A)
193	        D1 = (A == 1).astype(float)
194	        D2 = (A == 2).astype(float)
195	        Y = beta[0] + beta[1] * D1 + beta[2] * D2 + rng.normal(0, sigma_Y, N)
196	
197	        if differential:
198	            A_star = _generate_Astar_diff_Y(A, Y, C, rng)
199	        else:
200	            A_star = _generate_Astar(A, C, rng)
201	
202	        D1s = (A_star == 1).astype(float)
203	        D2s = (A_star == 2).astype(float)
204	        X_star = np.column_stack([np.ones(N), D1s, D2s])
205	        gamma_hat = ols_coefs(X_star, Y)
206	        bias_misclass[m] = gamma_hat - beta
207	
208	    return bias_misclass
209	
210	
211	# ============================================================
212	# Binary comparison
213	# ============================================================
214	def binary_attenuation_theory(C_bin, p_bin, beta_bin):
215	    """
216	    Binary exposure misclassification: plim from 2x2 system.
217	    Z = (1, D*), X = (1, D), beta = (beta_0, beta_1)
218	    """
219	    p0, p1 = p_bin
220	    q1 = C_bin[1, 0] * p0 + C_bin[1, 1] * p1
221	
222	    EZZ = np.array([[1.0, q1], [q1, q1]])
223	    EZX = np.array([[1.0, p1], [q1, C_bin[1, 1] * p1]])
224	
225	    plim = np.linalg.solve(EZZ, EZX @ beta_bin)
226	    return plim[1], plim[1] / beta_bin[1] if abs(beta_bin[1]) > 1e-10 else np.nan
227	
228	
229	def collapse_to_binary(C, p_A):
230	    """Derive 2x2 C from 3x3 by collapsing {1,2} -> 1."""
231	    p0, p1, p2 = p_A
232	    pB1 = p1 + p2
233	
234	    c00 = C[0, 0]
235	    c10 = C[1, 0] + C[2, 0]
236	    c01 = (C[0, 1] * p1 + C[0, 2] * p2) / pB1
237	    c11 = 1.0 - c01
238	
239	    C_bin = np.array([[c00, c01], [c10, c11]])
240	    p_bin = np.array([p0, pB1])
241	    beta_bin_eff = (BETA[1] * p1 + BETA[2] * p2) / pB1
242	    beta_bin = np.array([BETA[0], beta_bin_eff])
243	
244	    return C_bin, p_bin, beta_bin
245	
246	
247	# ============================================================
248	# Random search for sign reversal / amplification
249	# ============================================================
250	def classify_bias(plim_gamma, beta):
251	    """Classify bias type for each component (1 and 2)."""
252	    results = {}
253	    for k in [1, 2]:
254	        g = plim_gamma[k]
255	        b = beta[k]
256	        if abs(b) < 1e-10:
257	            results[k] = "zero_true"
258	            continue
259	        if g * b < 0:
260	            results[k] = "SIGN_REVERSAL"
261	        elif abs(g) > abs(b):
262	            results[k] = "AMPLIFICATION"
263	        else:
264	            results[k] = "toward_null"
265	    return results
266	
267	
268	def random_search(n_search, p_A, beta, seed=0):
269	    """Search random column-stochastic C for bias-toward-null violations."""
270	    rng = np.random.default_rng(seed)
271	
272	    sign_rev_count = 0
273	    amp_count = 0
274	    either_count = 0
275	    worst_cases = []
276	
277	    for i in range(n_search):
278	        C = rng.dirichlet([1, 1, 1], size=3).T
279	        try:
280	            plim, bias = theoretical_bias_exposure(C, p_A, beta)
281	        except np.linalg.LinAlgError:
282	            continue
283	
284	        types = classify_bias(plim, beta)
285	        has_sr = any(v == "SIGN_REVERSAL" for v in types.values())
286	        has_amp = any(v == "AMPLIFICATION" for v in types.values())
287	
288	        if has_sr:
289	            sign_rev_count += 1
290	        if has_amp:
291	            amp_count += 1
292	        if has_sr or has_amp:
293	            either_count += 1
294	            severity = max(
295	                abs(plim[1] / beta[1]) if abs(beta[1]) > 1e-10 else 0,
296	                abs(plim[2] / beta[2]) if abs(beta[2]) > 1e-10 else 0,
297	            )
298	            worst_cases.append((severity, C.copy(), plim.copy(), types.copy()))
299	
300	    worst_cases.sort(key=lambda x: -x[0])
301	    return {
302	        "n_searched": n_search,
303	        "sign_reversal": sign_rev_count,
304	        "amplification": amp_count,
305	        "either": either_count,
306	        "worst_cases": worst_cases[:10],
307	    }
308	
309	
310	# ============================================================
311	# Main
312	# ============================================================
313	def main():
314	    t_start = time.time()
315	
316	    print("=" * 85)
317	    print("Exposure Misclassification DAG — K=3 Bias-Toward-Null Test")
318	    print("=" * 85)
319	    print()
320	    print("DAG: A -> Y, A -> A*  (no confounders, exposure misclassification only)")
321	    print(f"DGP: P(A)=[{P_A[0]}, {P_A[1]}, {P_A[2]}], "
322	          f"beta=[{BETA[0]}, {BETA[1]}, {BETA[2]}], sigma_Y={SIGMA_Y}")
323	    print(f"MC:  N={N_SAMPLES:,}, M={M_REPS:,}, seed={SEED}")
324	    print(f"Random search: {N_RANDOM_SEARCH:,} matrices")
325	    print()
326	    print("Binary guarantee: non-diff misclassification => |gamma| <= |beta| (attenuation)")
327	    print("K=3 question: does this hold for all C? Or can we get sign reversal / amplification?")
328	
329	    matrices = make_confusion_matrices()
330	
331	    # ── PART A: Theory + MC for 6 structures ─────────────────
332	    print("\n" + "=" * 85)
333	    print("PART A: K=3 Exposure — Theory vs Monte Carlo  (6 structures)")
334	    print("=" * 85)
335	
336	    results = {}
337	    print(f"\n{'#':<2} {'Config':<14} | {'beta_1':>6} {'g1_th':>8} {'g1_mc':>8} {'type_1':>15} "
338	          f"| {'beta_2':>6} {'g2_th':>8} {'g2_mc':>8} {'type_2':>15} | {'Match':>5}")
339	    print("-" * 115)
340	
341	    for name, (C, desc) in matrices.items():
342	        t0 = time.time()
343	        idx = name[0]
344	        is_diff = (name == "6_diff_base")
345	
346	        # Theory (exact for non-differential; C6 base = C1, so same theory)
347	        plim_th, bias_th = theoretical_bias_exposure(C, P_A, BETA)
348	
349	        # MC
350	        mc_bias = run_mc_exposure(M_REPS, N_SAMPLES, C, P_A, BETA, SIGMA_Y, SEED,
351	                                  differential=is_diff)
352	
353	        mc_mean = mc_bias.mean(axis=0)
354	        mc_se = mc_bias.std(axis=0, ddof=1)
355	        ci_lo = mc_mean - 1.96 * mc_se / np.sqrt(M_REPS)
356	        ci_hi = mc_mean + 1.96 * mc_se / np.sqrt(M_REPS)
357	
358	        match_1 = ci_lo[1] <= bias_th[1] <= ci_hi[1]
359	        match_2 = ci_lo[2] <= bias_th[2] <= ci_hi[2]
360	        if is_diff:
361	            match_all = True  # no exact theory for differential
362	            match_str = "N/A"
363	        else:
364	            match_all = match_1 and match_2
365	            match_str = "YES" if match_all else "**NO**"
366	
367	        types = classify_bias(plim_th, BETA)
368	        elapsed = time.time() - t0
369	
370	        results[name] = dict(
371	            plim=plim_th, bias=bias_th, mc_mean=mc_mean + BETA,
372	            mc_bias_mean=mc_mean, ci=(ci_lo, ci_hi), match=match_all,
373	            types=types, is_diff=is_diff)
374	
375	        g1_mc = mc_mean[1] + BETA[1]  # plim gamma_1
376	        g2_mc = mc_mean[2] + BETA[2]
377	
378	        print(f"{idx:<2} {name:<14} | {BETA[1]:>6.2f} {plim_th[1]:>8.4f} {g1_mc:>8.4f} "
379	              f"{types[1]:>15} | {BETA[2]:>6.2f} {plim_th[2]:>8.4f} {g2_mc:>8.4f} "
380	              f"{types[2]:>15} | {match_str:>5}  ({elapsed:.1f}s)")
381	
382	    # ── PART B: 100k Random Search ───────────────────────────
383	    print("\n" + "=" * 85)
384	    print(f"PART B: Random Search — {N_RANDOM_SEARCH:,} column-stochastic C matrices")
385	    print("=" * 85)
386	
387	    t0 = time.time()
388	    search = random_search(N_RANDOM_SEARCH, P_A, BETA, seed=12345)
389	    elapsed_search = time.time() - t0
390	
391	    print(f"\nSearched: {search['n_searched']:,} matrices ({elapsed_search:.1f}s)")
392	    print(f"Sign reversal (any component):  {search['sign_reversal']:,} "
393	          f"({100*search['sign_reversal']/search['n_searched']:.1f}%)")
394	    print(f"Amplification (any component):  {search['amplification']:,} "
395	          f"({100*search['amplification']/search['n_searched']:.1f}%)")
396	    print(f"Either violation:               {search['either']:,} "
397	          f"({100*search['either']/search['n_searched']:.1f}%)")
398	
399	    if search['worst_cases']:
400	        print(f"\nTop-5 most extreme violations (by max |gamma_k/beta_k|):")
401	        print(f"  {'Severity':>8} {'g1':>8} {'type_1':>15} {'g2':>8} {'type_2':>15}")
402	        print(f"  {'-'*58}")
403	        for sev, C_worst, plim_worst, types_worst in search['worst_cases'][:5]:
404	            print(f"  {sev:>8.2f} {plim_worst[1]:>8.4f} {types_worst[1]:>15} "
405	                  f"{plim_worst[2]:>8.4f} {types_worst[2]:>15}")
406	            for row in C_worst:
407	                print(f"    [{row[0]:.3f}  {row[1]:.3f}  {row[2]:.3f}]")
408	            print()
409	
410	    # ── PART C: MC validation of worst-case C ────────────────
411	    if search['worst_cases']:
412	        print("=" * 85)
413	        print("PART C: MC Validation of Worst-Case C from Random Search")
414	        print("=" * 85)
415	
416	        _, C_worst, plim_worst, types_worst = search['worst_cases'][0]
417	        print(f"\nWorst-case C (severity={search['worst_cases'][0][0]:.2f}):")
418	        for row in C_worst:
419	            print(f"  [{row[0]:.3f}  {row[1]:.3f}  {row[2]:.3f}]")
420	
421	        mc_worst = run_mc_exposure(M_REPS, N_SAMPLES, C_worst, P_A, BETA, SIGMA_Y, SEED + 1)
422	        mc_mean_w = mc_worst.mean(axis=0)
423	        mc_se_w = mc_worst.std(axis=0, ddof=1)
424	
425	        print(f"\n{'Component':<10} {'beta':>8} {'Theory':>8} {'MC Mean':>8} "
426	              f"{'MC SE':>8} {'Type':>15}")
427	        print("-" * 60)
428	        for k in [1, 2]:
429	            th_g = plim_worst[k]
430	            mc_g = mc_mean_w[k] + BETA[k]
431	            print(f"{'beta_'+str(k):<10} {BETA[k]:>8.4f} {th_g:>8.4f} {mc_g:>8.4f} "
432	                  f"{mc_se_w[k]:>8.4f} {types_worst[k]:>15}")
433	
434	    # ── PART D: Binary K=2 Comparison ────────────────────────
435	    print("\n" + "=" * 85)
436	    print("PART D: Binary (K=2) Comparison — Attenuation Guarantee")
437	    print("=" * 85)
438	
439	    print(f"\nCollapse: B=1[A in {{1,2}}]. Binary beta_B = "
440	          f"E[beta_1*p1 + beta_2*p2]/(p1+p2) = "
441	          f"{(BETA[1]*P_A[1] + BETA[2]*P_A[2])/(P_A[1]+P_A[2]):.4f}")
442	
443	    print(f"\n{'#':<2} {'Config':<14} {'C_bin diag':>10} {'beta_B':>8} "
444	          f"{'gamma_B':>8} {'ratio':>8} {'Toward null?':>13}")
445	    print("-" * 72)
446	
447	    for name, (C, desc) in matrices.items():
448	        C_bin, p_bin, beta_bin = collapse_to_binary(C, P_A)
449	        gamma_B, ratio = binary_attenuation_theory(C_bin, p_bin, beta_bin)
450	        toward_null = abs(gamma_B) <= abs(beta_bin[1]) + 1e-10
451	        idx = name[0]
452	
453	        print(f"{idx:<2} {name:<14} [{C_bin[0,0]:.2f},{C_bin[1,1]:.2f}] "
454	              f"{beta_bin[1]:>8.4f} {gamma_B:>8.4f} {ratio:>8.4f} "
455	              f"{'YES (|r|<=1)' if toward_null else '**NO**':>13}")
456	
457	    # ── PART E: K=3 vs K=2 Direct Comparison ─────────────────
458	    print("\n" + "=" * 85)
459	    print("PART E: K=3 vs K=2 — Does Binary Guarantee Extend to Multiclass?")
460	    print("=" * 85)
461	
462	    print(f"\n{'#':<2} {'Config':<14} | {'K3: g1':>8} {'type_1':>15} {'g2':>8} "
463	          f"{'type_2':>15} | {'K2: toward_null':>15}")
464	    print("-" * 95)
465	
466	    k3_violations = 0
467	    for name, (C, desc) in matrices.items():
468	        idx = name[0]
469	        r = results[name]
470	        C_bin, p_bin, beta_bin = collapse_to_binary(C, P_A)
471	        gamma_B, ratio = binary_attenuation_theory(C_bin, p_bin, beta_bin)
472	        k2_tn = abs(ratio) <= 1.0 + 1e-10
473	
474	        has_violation = any(v in ("SIGN_REVERSAL", "AMPLIFICATION")
475	                          for v in r['types'].values())
476	        if has_violation:
477	            k3_violations += 1
478	
479	        print(f"{idx:<2} {name:<14} | {r['plim'][1]:>8.4f} {r['types'][1]:>15} "
480	              f"{r['plim'][2]:>8.4f} {r['types'][2]:>15} | "
481	              f"{'YES' if k2_tn else 'NO':>15}")
482	
483	    # ── Pass/Fail ────────────────────────────────────────────
484	    print("\n" + "=" * 85)
485	    print("PASS / FAIL SUMMARY")
486	    print("=" * 85)
487	
488	    # C1: Theory-MC match (non-differential only)
489	    nondiff_results = {n: r for n, r in results.items() if not r['is_diff']}
490	    n_match = sum(1 for r in nondiff_results.values() if r['match'])
491	    n_nondiff = len(nondiff_results)
492	    c1 = n_match == n_nondiff
493	    print(f"\n1. Theory vs MC match (non-diff): {n_match}/{n_nondiff}  "
494	          f"{'PASS' if c1 else 'FAIL'}")
495	    for name, r in nondiff_results.items():
496	        ci = r['ci']
497	        print(f"   {name}: th_bias=[{r['bias'][1]:.6f}, {r['bias'][2]:.6f}], "
498	              f"CI_1=[{ci[0][1]:.6f}, {ci[1][1]:.6f}], "
499	              f"CI_2=[{ci[0][2]:.6f}, {ci[1][2]:.6f}] -> "
500	              f"{'OK' if r['match'] else 'MISMATCH'}")
501	
502	    # C2: Sign reversal or amplification found
503	    c2_struct = k3_violations > 0
504	    c2_search = search['either'] > 0
505	    c2 = c2_struct or c2_search
506	    print(f"\n2. Bias-toward-null violation found: "
507	          f"{'PASS' if c2 else 'FAIL'}")
508	    print(f"   Named structures with violation: {k3_violations}/6")
509	    print(f"   Random search violations: {search['either']:,}/{search['n_searched']:,}")
510	
511	    # C3: Binary always toward null, K=3 sometimes not
512	    all_k2_tn = True
513	    for name, (C, desc) in matrices.items():
514	        C_bin, p_bin, beta_bin = collapse_to_binary(C, P_A)
515	        _, ratio = binary_attenuation_theory(C_bin, p_bin, beta_bin)
516	        if abs(ratio) > 1.0 + 1e-10:
517	            all_k2_tn = False
518	    c3 = all_k2_tn and c2
519	    print(f"\n3. K=2 always toward null AND K=3 sometimes not: "
520	          f"{'PASS' if c3 else 'FAIL'}")
521	    print(f"   K=2 all toward null: {'YES' if all_k2_tn else 'NO'}")
522	    print(f"   K=3 has violations: {'YES' if c2 else 'NO'}")
523	
524	    overall = c1 and c2 and c3
525	    print(f"\nOVERALL: {'PASS' if overall else 'FAIL'}")
526	
527	    # ── Appendix: Confusion Matrices ─────────────────────────
528	    print("\n" + "=" * 85)
529	    print("APPENDIX: Confusion Matrix Definitions")
530	    print("=" * 85)
531	    for name, (C, desc) in matrices.items():
532	        print(f"\n{name}: {desc}")
533	        for row in C:
534	            print(f"  [{row[0]:.2f}  {row[1]:.2f}  {row[2]:.2f}]")
535	
536	    elapsed_total = time.time() - t_start
537	    print(f"\nTotal runtime: {elapsed_total:.1f}s")
538	
539	
540	if __name__ == "__main__":
541	    main()
542	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb4c12c8-e895-4a63-b638-919cacbd5af0",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "b0f5050e-8f91-47f6-a920-a4fbedabc10b",
  "sourceToolAssistantUUID": "bb4c12c8-e895-4a63-b638-919cacbd5af0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T08:57:38.446Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N17KmbJCJGPuZ3pZBjFu1W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_confounding_dag.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0f5050e-8f91-47f6-a920-a4fbedabc10b",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYV3BtcaE2tYwMZWcai",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "013285f4-3eb7-4e9c-9113-fed2eb3f0533",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfoUs6aehVso7maMWeGFbu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 505,
      "cache_read_input_tokens": 31328,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 505
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 262,
          "cache_read_input_tokens": 31328,
          "cache_creation_input_tokens": 505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 505,
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

_source line 34 · 2026-05-20T08:57:38.451Z_

<details><summary>↩ Tool result · `toolu_01N17KmbJCJGPuZ3pZBjFu1W`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	MVP Validation: Confounding DAG with K=3 Multiclass Annotation Error
4	
5	== Technical Setting ==
6	A is an OBSERVED confounder measured with error via LLM annotation.
7	The researcher observes A but uses A* (LLM-annotated proxy) to control
8	for confounding in regression adjustment.
9	
10	  DAG: A -> T, A -> Y, T -> Y, A -> A*
11	  Estimand: E[Y|do(T=t)] estimated via OLS adjusting for A*
12	
13	This differs from Lee & Wood-Doughty (2024), who study UNOBSERVED
14	confounding where A is never observed and A* is the only available proxy.
15	Their setting involves different identifiability conditions (proxy must
16	satisfy relevance + exclusion). Our setting: A is observable in principle
17	but measured with classification error by an LLM annotator, creating a
18	known-structure noise process (confusion matrix C).
19	
20	== DGP ==
21	  A in {0,1,2}: true 3-class confounder, P(A=k) configurable
22	  T = alpha_1*1[A=1] + alpha_2*1[A=2] + eta,  eta ~ N(0, sigma_T^2)
23	  Y = beta_T*T + beta_1*1[A=1] + beta_2*1[A=2] + eps,  eps ~ N(0, sigma_Y^2)
24	  P(A*=j|A=i) = C[j,i]  (C is column-stochastic 3x3 matrix)
25	
26	== Key Result ==
27	  plim gamma_hat = (E[Z'Z])^{-1} E[Z'X] beta
28	  where Z = (1, T, D*_1, D*_2), X = (1, T, D_1, D_2)
29	  Theoretical bias on beta_T = gamma_hat[1] - beta_T
30	
31	== Pass Criteria ==
32	  1. Theory vs MC 95% CI match: 6/6
33	  2. >=1 non-differential C produces away-from-null bias
34	  3. Binary collapse bias != multiclass theory prediction
35	
36	Dependencies: numpy, scipy
37	"""
38	
39	import numpy as np
40	from collections import OrderedDict
41	import time
42	
43	
44	# ============================================================
45	# DGP Parameters
46	# ============================================================
47	N_SAMPLES = 10_000
48	M_REPS = 1_000
49	SEED = 42
50	
51	P_A = np.array([0.4, 0.35, 0.25])
52	ALPHA = np.array([1.5, -1.0])        # alpha_1, alpha_2
53	BETA_T = 2.0                          # true causal effect of T on Y
54	BETA_A = np.array([1.0, -0.5])       # beta_1, beta_2 (direct A->Y)
55	SIGMA_T = 1.0
56	SIGMA_Y = 1.0
57	
58	
59	# ============================================================
60	# Confusion Matrix Structures (named constants)
61	# ============================================================
62	
63	# --- Non-differential (C independent of T) ---
64	
65	C1_SYMMETRIC_HIGH = np.array([
66	    [0.80, 0.10, 0.10],
67	    [0.10, 0.80, 0.10],
68	    [0.10, 0.10, 0.80],
69	])
70	C1_DESC = "Symmetric high-accuracy: diag=0.8, uniform off-diagonal=0.1"
71	
72	C2_ASYMMETRIC = np.array([
73	    [0.65, 0.05, 0.10],
74	    [0.30, 0.85, 0.10],
75	    [0.05, 0.10, 0.80],
76	])
77	C2_DESC = "Asymmetric: P(A*=1|A=0)=0.30 >> P(A*=0|A=1)=0.05"
78	
79	C3_STRUCTURAL_12 = np.array([
80	    [0.96, 0.01, 0.01],
81	    [0.02, 0.69, 0.30],
82	    [0.02, 0.30, 0.69],
83	])
84	C3_DESC = "Structural: classes 1<->2 heavily confused (0.30), class 0 clean (off<0.02)"
85	
86	C4_WEAK_DIAG = np.array([
87	    [0.40, 0.35, 0.25],
88	    [0.35, 0.40, 0.35],
89	    [0.25, 0.25, 0.40],
90	])
91	C4_DESC = "Weak diagonal dominance: diag~0.4, non-uniform off-diagonal"
92	
93	C5_NEAR_PERM = np.array([
94	    [0.05, 0.05, 0.90],
95	    [0.90, 0.05, 0.05],
96	    [0.05, 0.90, 0.05],
97	])
98	C5_DESC = "Near-permutation: cyclic shift 0->1, 1->2, 2->0 (p=0.90)"
99	
100	# --- Differential (C depends on T) ---
101	
102	C6_DIFF_BASE = np.array([
103	    [0.80, 0.10, 0.10],
104	    [0.10, 0.80, 0.10],
105	    [0.10, 0.10, 0.80],
106	])
107	C6_DESC = "Differential: base=C1, off-diagonal doubled when T>median"
108	
109	
110	def make_confusion_matrices():
111	    """6 confusion matrix structures: 5 non-differential + 1 differential."""
112	    matrices = OrderedDict([
113	        ("1_sym_high",   (C1_SYMMETRIC_HIGH, False, C1_DESC)),
114	        ("2_asymmetric", (C2_ASYMMETRIC,     False, C2_DESC)),
115	        ("3_struct_12",  (C3_STRUCTURAL_12,  False, C3_DESC)),
116	        ("4_weak_diag",  (C4_WEAK_DIAG,      False, C4_DESC)),
117	        ("5_near_perm",  (C5_NEAR_PERM,      False, C5_DESC)),
118	        ("6_differen",   (C6_DIFF_BASE,      True,  C6_DESC)),
119	    ])
120	    for name, (C, _, desc) in matrices.items():
121	        assert np.allclose(C.sum(axis=0), 1.0), f"{name}: columns don't sum to 1"
122	        assert (C >= 0).all(), f"{name}: negative entries"
123	    return matrices
124	
125	
126	# ============================================================
127	# Theoretical bias (exact, for non-differential C)
128	# ============================================================
129	def theoretical_bias_exact(C, p_A, alpha, beta_T, beta_A, sigma_T):
130	    """
131	    plim gamma = (E[Z'Z])^{-1} E[Z'X] beta
132	    Z = (1, T, D*_1, D*_2),  X = (1, T, D_1, D_2)
133	    """
134	    p0, p1, p2 = p_A
135	    a1, a2 = alpha
136	    b1, b2 = beta_A
137	    beta = np.array([0.0, beta_T, b1, b2])
138	
139	    ET = a1 * p1 + a2 * p2
140	    ET2 = a1**2 * p1 + a2**2 * p2 + sigma_T**2
141	    q = C @ p_A
142	    ET_Ds = np.array([a1 * C[j, 1] * p1 + a2 * C[j, 2] * p2 for j in range(3)])
143	
144	    EZZ = np.array([
145	        [1.0,  ET,       q[1],      q[2]],
146	        [ET,   ET2,      ET_Ds[1],  ET_Ds[2]],
147	        [q[1], ET_Ds[1], q[1],      0.0],
148	        [q[2], ET_Ds[2], 0.0,       q[2]],
149	    ])
150	    EZX = np.array([
151	        [1.0,  ET,       p1,             p2],
152	        [ET,   ET2,      a1 * p1,        a2 * p2],
153	        [q[1], ET_Ds[1], C[1, 1] * p1,   C[1, 2] * p2],
154	        [q[2], ET_Ds[2], C[2, 1] * p1,   C[2, 2] * p2],
155	    ])
156	
157	    plim = np.linalg.solve(EZZ, EZX @ beta)
158	    return plim[1] - beta_T, plim
159	
160	
161	def theoretical_bias_largesample(C_base, p_A, alpha, beta_T, beta_A,
162	                                  sigma_T, sigma_Y, N_approx=2_000_000,
163	                                  seed=999):
164	    """Approximate theoretical bias for differential C via large-sample moments."""
165	    rng = np.random.default_rng(seed)
166	    a1, a2 = alpha
167	
168	    A = rng.choice(3, size=N_approx, p=p_A)
169	    D1 = (A == 1).astype(np.float64)
170	    D2 = (A == 2).astype(np.float64)
171	    T = a1 * D1 + a2 * D2 + rng.normal(0, sigma_T, N_approx)
172	
173	    A_star = _generate_Astar_differential(A, T, C_base, rng)
174	    D1s = (A_star == 1).astype(np.float64)
175	    D2s = (A_star == 2).astype(np.float64)
176	
177	    beta = np.array([0.0, beta_T, beta_A[0], beta_A[1]])
178	    ones = np.ones(N_approx)
179	    Z = np.column_stack([ones, T, D1s, D2s])
180	    X = np.column_stack([ones, T, D1, D2])
181	
182	    EZZ = (Z.T @ Z) / N_approx
183	    EZX = (Z.T @ X) / N_approx
184	    plim = np.linalg.solve(EZZ, EZX @ beta)
185	    return plim[1] - beta_T, plim
186	
187	
188	# ============================================================
189	# Data generation
190	# ============================================================
191	def _generate_Astar_nondiff(A, C, rng):
192	    """Vectorized: sample A* from C[:, A[i]] for each i."""
193	    probs = C[:, A]                          # (3, N)
194	    cum = np.cumsum(probs, axis=0)           # (3, N)
195	    u = rng.uniform(size=A.shape[0])
196	    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))
197	
198	
199	def _make_C_high(C_base, factor=2.0):
200	    """Scale off-diagonal entries by factor, renormalize columns."""
201	    C_high = C_base.copy()
202	    for col in range(3):
203	        diag_val = C_high[col, col]
204	        off_sum = 1.0 - diag_val
205	        new_off_sum = min(off_sum * factor, 0.95)
206	        scale = new_off_sum / off_sum if off_sum > 0 else 1.0
207	        for row in range(3):
208	            if row != col:
209	                C_high[row, col] *= scale
210	        C_high[col, col] = 1.0 - sum(C_high[r, col] for r in range(3) if r != col)
211	    return C_high
212	
213	
214	def _generate_Astar_differential(A, T, C_base, rng):
215	    """T > median => off-diagonal rates doubled."""
216	    N = len(A)
217	    C_high = _make_C_high(C_base, factor=2.0)
218	    T_med = np.median(T)
219	    high = T > T_med
220	
221	    probs_low = C_base[:, A]
222	    probs_high = C_high[:, A]
223	    probs = np.where(high[np.newaxis, :], probs_high, probs_low)
224	
225	    cum = np.cumsum(probs, axis=0)
226	    u = rng.uniform(size=N)
227	    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))
228	
229	
230	def generate_data(N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,
231	                  differential, rng):
232	    a1, a2 = alpha
233	    b1, b2 = beta_A
234	
235	    A = rng.choice(3, size=N, p=p_A)
236	    D1 = (A == 1).astype(np.float64)
237	    D2 = (A == 2).astype(np.float64)
238	    T = a1 * D1 + a2 * D2 + rng.normal(0, sigma_T, N)
239	    Y = beta_T * T + b1 * D1 + b2 * D2 + rng.normal(0, sigma_Y, N)
240	
241	    if differential:
242	        A_star = _generate_Astar_differential(A, T, C, rng)
243	    else:
244	        A_star = _generate_Astar_nondiff(A, C, rng)
245	
246	    return A, T, Y, A_star
247	
248	
249	# ============================================================
250	# OLS helper
251	# ============================================================
252	def ols_beta_T(T, Y, dummies):
253	    """OLS Y ~ 1 + T + dummies, return coefficient on T."""
254	    X = np.column_stack([np.ones(len(T)), T, dummies])
255	    coef, _, _, _ = np.linalg.lstsq(X, Y, rcond=None)
256	    return coef[1]
257	
258	
259	# ============================================================
260	# Monte Carlo
261	# ============================================================
262	def run_mc(M, N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,
263	           differential, seed):
264	    rng = np.random.default_rng(seed)
265	    bias_true = np.empty(M)
266	    bias_misclass = np.empty(M)
267	
268	    for m in range(M):
269	        A, T, Y, A_star = generate_data(
270	            N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,
271	            differential, rng)
272	        D_true = np.column_stack([(A == 1).astype(float), (A == 2).astype(float)])
273	        D_star = np.column_stack([(A_star == 1).astype(float),
274	                                   (A_star == 2).astype(float)])
275	        bias_true[m] = ols_beta_T(T, Y, D_true) - beta_T
276	        bias_misclass[m] = ols_beta_T(T, Y, D_star) - beta_T
277	
278	    return bias_true, bias_misclass
279	
280	
281	# ============================================================
282	# Unadjusted bias (omitted variable reference)
283	# ============================================================
284	def unadjusted_bias(p_A, alpha, beta_T, beta_A, sigma_T):
285	    """plim of OLS Y ~ 1 + T (no confounder control)."""
286	    p0, p1, p2 = p_A
287	    a1, a2 = alpha
288	    b1, b2 = beta_A
289	    ET = a1 * p1 + a2 * p2
290	    VarT = a1**2 * p1 + a2**2 * p2 + sigma_T**2 - ET**2
291	    CovD1T = a1 * p1 - p1 * ET
292	    CovD2T = a2 * p2 - p2 * ET
293	    return (b1 * CovD1T + b2 * CovD2T) / VarT
294	
295	
296	# ============================================================
297	# Binary collapse analysis
298	# ============================================================
299	def theoretical_bias_binary_from_C3(C, p_A, alpha, beta_T, beta_A, sigma_T):
300	    """
301	    Theoretical bias when collapsing A to B=1[A in {1,2}], B*=1[A* in {1,2}].
302	    Z = (1, T, B*),  X = (1, T, D1, D2)
303	    plim = (E[Z'Z])^{-1} E[Z'X] beta
304	    """
305	    p0, p1, p2 = p_A
306	    a1, a2 = alpha
307	    b1, b2 = beta_A
308	    beta = np.array([0.0, beta_T, b1, b2])
309	
310	    ET = a1 * p1 + a2 * p2
311	    ET2 = a1**2 * p1 + a2**2 * p2 + sigma_T**2
312	
313	    q = C @ p_A
314	    q_Bs = q[1] + q[2]
315	
316	    ET_Ds = np.array([a1 * C[j, 1] * p1 + a2 * C[j, 2] * p2 for j in range(3)])
317	    ET_Bs = ET_Ds[1] + ET_Ds[2]
318	
319	    EZZ = np.array([
320	        [1.0,    ET,    q_Bs],
321	        [ET,     ET2,   ET_Bs],
322	        [q_Bs,   ET_Bs, q_Bs],
323	    ])
324	
325	    EB_D1 = (1.0 - C[0, 1]) * p1
326	    EB_D2 = (1.0 - C[0, 2]) * p2
327	
328	    EZX = np.array([
329	        [1.0,    ET,     p1,       p2],
330	        [ET,     ET2,    a1 * p1,  a2 * p2],
331	        [q_Bs,   ET_Bs,  EB_D1,    EB_D2],
332	    ])
333	
334	    plim = np.linalg.solve(EZZ, EZX @ beta)
335	    return plim[1] - beta_T
336	
337	
338	def run_mc_binary_collapse(M, N, C, p_A, alpha, beta_T, beta_A,
339	                           sigma_T, sigma_Y, differential, seed):
340	    """MC with binary collapse: B=1[A in {1,2}], B*=1[A* in {1,2}]."""
341	    rng = np.random.default_rng(seed)
342	    bias_bin = np.empty(M)
343	
344	    for m in range(M):
345	        A, T, Y, A_star = generate_data(
346	            N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,
347	            differential, rng)
348	        B_star = ((A_star == 1) | (A_star == 2)).astype(float).reshape(-1, 1)
349	        bias_bin[m] = ols_beta_T(T, Y, B_star) - beta_T
350	
351	    return bias_bin
352	
353	
354	# ============================================================
355	# Main
356	# ============================================================
357	def main():
358	    print("=" * 85)
359	    print("MVP Validation: Confounding DAG — K=3 Multiclass Annotation Error Bias")
360	    print("=" * 85)
361	    print()
362	    print("Setting: A is OBSERVED confounder with noisy LLM annotation A*.")
363	    print("         Researcher adjusts for A* (not A) in OLS.  DAG: A->T, A->Y, T->Y, A->A*")
364	    print("         (cf. Lee & Wood-Doughty 2024: UNOBSERVED confounding with proxy)")
365	    print()
366	    print(f"DGP: P(A)=[{P_A[0]}, {P_A[1]}, {P_A[2]}], "
367	          f"alpha=[{ALPHA[0]}, {ALPHA[1]}], "
368	          f"beta_T={BETA_T}, beta_A=[{BETA_A[0]}, {BETA_A[1]}]")
369	    print(f"     sigma_T={SIGMA_T}, sigma_Y={SIGMA_Y}")
370	    print(f"MC:  N={N_SAMPLES:,}, M={M_REPS:,}, seed={SEED}")
371	
372	    ovb = unadjusted_bias(P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)
373	    print(f"\nUnadjusted OVB (no A control): {ovb:.6f}")
374	    print(f"  => plim(beta_T_hat_unadj) = {BETA_T + ovb:.6f}")
375	    print(f"  => Direction: {'toward null' if ovb * BETA_T < 0 else 'away from null'}")
376	
377	    matrices = make_confusion_matrices()
378	
379	    # ── PART A: K=3 Theory vs MC ──────────────────────────────
380	    print("\n" + "=" * 85)
381	    print("PART A: K=3 Multiclass — Theory vs Monte Carlo  (6 structures)")
382	    print("=" * 85)
383	
384	    results_k3 = {}
385	    header = (f"{'#':<2} {'Config':<14} {'Theory':>10} {'MC Mean':>10} "
386	              f"{'MC 95% CI':>22} {'Match?':>7} {'Direction':>14}")
387	    print(f"\n{header}")
388	    print("-" * len(header))
389	
390	    for name, (C, is_diff, desc) in matrices.items():
391	        t0 = time.time()
392	        idx = name[0]
393	
394	        if is_diff:
395	            th_bias, _ = theoretical_bias_largesample(
396	                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T, SIGMA_Y)
397	        else:
398	            th_bias, _ = theoretical_bias_exact(
399	                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)
400	
401	        _, mc_bias = run_mc(M_REPS, N_SAMPLES, C, P_A, ALPHA, BETA_T,
402	                            BETA_A, SIGMA_T, SIGMA_Y, is_diff, SEED)
403	
404	        mc_mean = mc_bias.mean()
405	        mc_se = mc_bias.std(ddof=1)
406	        ci_lo = mc_mean - 1.96 * mc_se / np.sqrt(M_REPS)
407	        ci_hi = mc_mean + 1.96 * mc_se / np.sqrt(M_REPS)
408	        match = ci_lo <= th_bias <= ci_hi
409	
410	        if abs(th_bias) < 1e-6:
411	            direction = "~zero"
412	        elif th_bias * BETA_T > 0:
413	            direction = "AWAY from null"
414	        else:
415	            direction = "toward null"
416	
417	        elapsed = time.time() - t0
418	        results_k3[name] = dict(
419	            th_bias=th_bias, mc_mean=mc_mean, ci=(ci_lo, ci_hi),
420	            match=match, direction=direction, mc_bias_arr=mc_bias,
421	            is_diff=is_diff)
422	
423	        print(f"{idx:<2} {name:<14} {th_bias:>10.6f} {mc_mean:>10.6f} "
424	              f"[{ci_lo:>9.6f}, {ci_hi:>9.6f}] "
425	              f"{'YES' if match else '**NO**':>7} "
426	              f"{direction:>14}  ({elapsed:.1f}s)")
427	
428	    # ── PART B: Binary collapse ──────────────────────────────
429	    print("\n" + "=" * 85)
430	    print("PART B: Binary Collapse — B=1[A in {1,2}]")
431	    print("=" * 85)
432	
433	    header_b = (f"{'#':<2} {'Config':<14} {'K3 Bias':>10} {'Bin Bias':>10} "
434	                f"{'Bin MC':>10} {'Bin MC 95% CI':>22} {'K3!=Bin?':>8}")
435	    print(f"\n{header_b}")
436	    print("-" * len(header_b))
437	
438	    pass_criterion_3 = False
439	    bin_results = {}
440	
441	    for name, (C, is_diff, desc) in matrices.items():
442	        t0 = time.time()
443	        idx = name[0]
444	        k3_bias = results_k3[name]["th_bias"]
445	
446	        if not is_diff:
447	            bin_th = theoretical_bias_binary_from_C3(
448	                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)
449	        else:
450	            rng_approx = np.random.default_rng(888)
451	            N_ap = 2_000_000
452	            A_ap = rng_approx.choice(3, size=N_ap, p=P_A)
453	            D1_ap = (A_ap == 1).astype(np.float64)
454	            D2_ap = (A_ap == 2).astype(np.float64)
455	            T_ap = (ALPHA[0] * D1_ap + ALPHA[1] * D2_ap
456	                    + rng_approx.normal(0, SIGMA_T, N_ap))
457	            As_ap = _generate_Astar_differential(A_ap, T_ap, C, rng_approx)
458	            Bs_ap = ((As_ap == 1) | (As_ap == 2)).astype(np.float64)
459	            beta_vec = np.array([0.0, BETA_T, BETA_A[0], BETA_A[1]])
460	            ones_ap = np.ones(N_ap)
461	            Z_b = np.column_stack([ones_ap, T_ap, Bs_ap])
462	            X_f = np.column_stack([ones_ap, T_ap, D1_ap, D2_ap])
463	            EZZ_b = (Z_b.T @ Z_b) / N_ap
464	            EZX_b = (Z_b.T @ X_f) / N_ap
465	            plim_b = np.linalg.solve(EZZ_b, EZX_b @ beta_vec)
466	            bin_th = plim_b[1] - BETA_T
467	
468	        bin_mc = run_mc_binary_collapse(
469	            M_REPS, N_SAMPLES, C, P_A, ALPHA, BETA_T, BETA_A,
470	            SIGMA_T, SIGMA_Y, is_diff, SEED)
471	
472	        bin_mean = bin_mc.mean()
473	        bin_se = bin_mc.std(ddof=1)
474	        bin_ci_lo = bin_mean - 1.96 * bin_se / np.sqrt(M_REPS)
475	        bin_ci_hi = bin_mean + 1.96 * bin_se / np.sqrt(M_REPS)
476	
477	        k3_ne_bin = abs(k3_bias - bin_th) > 0.001
478	        if k3_ne_bin:
479	            pass_criterion_3 = True
480	
481	        bin_results[name] = dict(bin_th=bin_th, bin_mean=bin_mean, k3_ne_bin=k3_ne_bin)
482	
483	        elapsed = time.time() - t0
484	        print(f"{idx:<2} {name:<14} {k3_bias:>10.6f} {bin_th:>10.6f} "
485	              f"{bin_mean:>10.6f} [{bin_ci_lo:>9.6f}, {bin_ci_hi:>9.6f}] "
486	              f"{'YES' if k3_ne_bin else 'no':>8}  ({elapsed:.1f}s)")
487	
488	    # ── Pass/Fail ────────────────────────────────────────────
489	    print("\n" + "=" * 85)
490	    print("PASS / FAIL SUMMARY")
491	    print("=" * 85)
492	
493	    n_total = len(results_k3)
494	    n_match = sum(1 for r in results_k3.values() if r["match"])
495	    c1 = n_match == n_total
496	    print(f"\n1. Theory vs MC 95% CI match: {n_match}/{n_total}  "
497	          f"{'PASS' if c1 else 'FAIL'}")
498	
499	    # Per-structure detail
500	    for name, r in results_k3.items():
501	        status = "OK" if r["match"] else "MISMATCH"
502	        print(f"   {name}: th={r['th_bias']:.6f}, "
503	              f"CI=[{r['ci'][0]:.6f}, {r['ci'][1]:.6f}] -> {status}")
504	
505	    away_nondiff = [name for name, r in results_k3.items()
506	                    if not r["is_diff"] and r["direction"] == "AWAY from null"]
507	    c2 = len(away_nondiff) >= 1
508	    print(f"\n2. Non-diff C with away-from-null bias: {len(away_nondiff)}/5  "
509	          f"{'PASS' if c2 else 'FAIL'}")
510	    for name in away_nondiff:
511	        print(f"   {name}: bias={results_k3[name]['th_bias']:.6f}")
512	
513	    c3 = pass_criterion_3
514	    diff_names = [n for n, r in bin_results.items() if r["k3_ne_bin"]]
515	    print(f"\n3. Binary collapse bias != K=3 theory: "
516	          f"{len(diff_names)}/{n_total}  "
517	          f"{'PASS' if c3 else 'FAIL'}")
518	    for name in diff_names:
519	        k3b = results_k3[name]["th_bias"]
520	        bb = bin_results[name]["bin_th"]
521	        print(f"   {name}: K3={k3b:.6f}, Bin={bb:.6f}, Delta={k3b - bb:.6f}")
522	
523	    overall = c1 and c2 and c3
524	    print(f"\nOVERALL: {'PASS' if overall else 'FAIL'}")
525	
526	    # ── Appendix ─────────────────────────────────────────────
527	    print("\n" + "=" * 85)
528	    print("APPENDIX: Confusion Matrix Definitions")
529	    print("=" * 85)
530	    for name, (C, is_diff, desc) in matrices.items():
531	        tag = " [DIFFERENTIAL]" if is_diff else " [NON-DIFF]"
532	        print(f"\n{name}{tag}")
533	        print(f"  {desc}")
534	        for row in C:
535	            print(f"  [{row[0]:.2f}  {row[1]:.2f}  {row[2]:.2f}]")
536	        if is_diff:
537	            C_high = _make_C_high(C, factor=2.0)
538	            print(f"  C_high (T>median):")
539	            for row in C_high:
540	                print(f"  [{row[0]:.2f}  {row[1]:.2f}  {row[2]:.2f}]")
541	
542	    print("\n" + "=" * 85)
543	    print("TECHNICAL NOTE: Lee & Wood-Doughty (2024) Distinction")
544	    print("=" * 85)
545	    print("""
546	This MVP studies OBSERVED confounding with noisy measurement:
547	  - A is an observable confounder (e.g., sentiment, topic)
548	  - Researcher uses LLM to annotate A, producing A* with known error structure
549	  - A* substitutes for A in regression adjustment for confounding
550	  - Error structure: P(A*=j|A=i) = C[j,i], C is estimable from validation data
551	
552	Lee & Wood-Doughty (2024) study UNOBSERVED confounding with proxy:
553	  - A is never observed (latent confounder)
554	  - A* is the only available proxy (not a noisy version of something observed)
555	  - Requires proxy relevance + exclusion restrictions for identification
556	  - Different bias structure: proxy must satisfy E[T|A,A*] = E[T|A]
557	
558	Key implication: our bias formula plim = (E[Z'Z])^{-1} E[Z'X] beta assumes
559	the researcher COULD observe A (and does, for validation), but CHOOSES to use
560	A* at scale. The confusion matrix C is a design parameter, not a nuisance.
561	""")
562	
563	
564	if __name__ == "__main__":
565	    main()
566	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "013285f4-3eb7-4e9c-9113-fed2eb3f0533",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "e87e33f8-638b-426f-b4cf-3080ed43df44",
  "sourceToolAssistantUUID": "013285f4-3eb7-4e9c-9113-fed2eb3f0533",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T08:57:43.639Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VQc8UkaaonW3142zp9rgYk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_exposure_dirichlet_subspace.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e87e33f8-638b-426f-b4cf-3080ed43df44",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYVM1hCyMtXGAuGfbqB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6bd543a-0a14-4ce0-9eec-f72ab6c6c2ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtBQFENCYRSYKe9eauh4w6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19001,
      "cache_read_input_tokens": 31833,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19001,
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

_source line 36 · 2026-05-20T08:57:43.646Z_

<details><summary>↩ Tool result · `toolu_01VQc8UkaaonW3142zp9rgYk`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Dirichlet Prior Subspace Analysis for Exposure Misclassification
4	
5	The 85% violation rate from mvp_exposure_dag.py uses Dirichlet(1,1,1) uniform
6	prior over column-stochastic matrices. Actual LLM confusion matrices are far
7	more diagonal-dominant. This script stratifies the violation rate by minimum
8	diagonal value of C to assess practical relevance.
9	
10	Subspaces:
11	  - Full space (no diagonal constraint, equiv. Dirichlet(1,1,1))
12	  - min(diag(C)) >= 0.5
13	  - min(diag(C)) >= 0.7  (realistic LLM accuracy)
14	  - min(diag(C)) >= 0.9  (high-accuracy LLM)
15	
16	Method: direct sampling via truncated Beta(1,2) for diagonal entries +
17	uniform simplex split for off-diagonal. Equivalent to uniform distribution
18	on the constrained space, but O(n) time/memory vs rejection sampling.
19	
20	For K=3, each column's diagonal entry d ~ Beta(1,2) truncated to [thresh,1],
21	density f(d) = 2(1-d)/(1-thresh)^2. Inverse CDF: d = 1-(1-thresh)*sqrt(1-U).
22	
23	Dependencies: numpy
24	"""
25	
26	import numpy as np
27	import time
28	
29	P_A = np.array([0.4, 0.35, 0.25])
30	BETA = np.array([0.0, 1.0, -0.5])
31	
32	DIAG_THRESHOLDS = [0.0, 0.5, 0.7, 0.9]
33	N_SAMPLES = 50_000
34	
35	
36	def theoretical_plim(C, p_A, beta):
37	    """plim gamma = (E[Z'Z])^{-1} E[Z'X] beta for exposure DAG."""
38	    p0, p1, p2 = p_A
39	    q = C @ p_A
40	    EZZ = np.array([
41	        [1.0,  q[1], q[2]],
42	        [q[1], q[1], 0.0],
43	        [q[2], 0.0,  q[2]],
44	    ])
45	    EZX = np.array([
46	        [1.0,  p1,            p2],
47	        [q[1], C[1, 1] * p1,  C[1, 2] * p2],
48	        [q[2], C[2, 1] * p1,  C[2, 2] * p2],
49	    ])
50	    return np.linalg.solve(EZZ, EZX @ beta)
51	
52	
53	def sample_and_analyze(n, diag_thresh, p_A, beta, rng):
54	    """
55	    Sample n column-stochastic 3x3 C with min(diag) >= diag_thresh,
56	    compute plim for each, return statistics. No large array stored.
57	    """
58	    n_sr = 0       # sign reversal (any component)
59	    n_amp = 0      # amplification (any component)
60	    n_either = 0   # any violation
61	    n_valid = 0
62	
63	    worst_sev = 0.0
64	    worst_C = None
65	    worst_plim = None
66	
67	    # Process in manageable chunks
68	    chunk = min(n, 5000)
69	    remaining = n
70	
71	    while remaining > 0:
72	        batch = min(chunk, remaining)
73	        remaining -= batch
74	
75	        # Direct sampling: each column independently
76	        C_batch = np.empty((batch, 3, 3))
77	        for col in range(3):
78	            U = rng.uniform(size=batch)
79	            d = 1.0 - (1.0 - diag_thresh) * np.sqrt(1.0 - U)
80	            V = rng.uniform(size=batch)
81	            rem = 1.0 - d
82	
83	            off = [r for r in range(3) if r != col]
84	            C_batch[:, col, col] = d
85	            C_batch[:, off[0], col] = rem * V
86	            C_batch[:, off[1], col] = rem * (1.0 - V)
87	
88	        # Analyze each C
89	        for i in range(batch):
90	            C = C_batch[i]
91	            try:
92	                plim = theoretical_plim(C, p_A, beta)
93	            except np.linalg.LinAlgError:
94	                continue
95	
96	            n_valid += 1
97	            sr = False
98	            amp = False
99	            for k in [1, 2]:
100	                if abs(beta[k]) < 1e-10:
101	                    continue
102	                if plim[k] * beta[k] < 0:
103	                    sr = True
104	                if abs(plim[k]) > abs(beta[k]):
105	                    amp = True
106	
107	            if sr:
108	                n_sr += 1
109	            if amp:
110	                n_amp += 1
111	            if sr or amp:
112	                n_either += 1
113	                sev = max(
114	                    abs(plim[1] / beta[1]) if abs(beta[1]) > 1e-10 else 0,
115	                    abs(plim[2] / beta[2]) if abs(beta[2]) > 1e-10 else 0,
116	                )
117	                if sev > worst_sev:
118	                    worst_sev = sev
119	                    worst_C = C.copy()
120	                    worst_plim = plim.copy()
121	
122	    return {
123	        "n_valid": n_valid,
124	        "n_violation": n_either,
125	        "n_sign_rev": n_sr,
126	        "n_amp": n_amp,
127	        "violation_rate": n_either / n_valid if n_valid > 0 else 0,
128	        "sign_rev_rate": n_sr / n_valid if n_valid > 0 else 0,
129	        "amp_rate": n_amp / n_valid if n_valid > 0 else 0,
130	        "worst_severity": worst_sev,
131	        "worst_C": worst_C,
132	        "worst_plim": worst_plim,
133	    }
134	
135	
136	def main():
137	    t_start = time.time()
138	    rng = np.random.default_rng(42)
139	
140	    print("=" * 85)
141	    print("Dirichlet Subspace Analysis: Exposure Misclassification Violation Rates")
142	    print("=" * 85)
143	    print()
144	    print(f"DGP: P(A)=[{P_A[0]}, {P_A[1]}, {P_A[2]}], "
145	          f"beta=[{BETA[0]}, {BETA[1]}, {BETA[2]}]")
146	    print(f"Samples per subspace: {N_SAMPLES:,}")
147	    print(f"Method: direct sampling (truncated Beta(1,2) diagonal + uniform split)")
148	
149	    # ── Main table ───────────────────────────────────────────
150	    print(f"\n{'Subspace':>12} {'N':>8} {'Violation%':>11} "
151	          f"{'SignRev%':>10} {'Amplif%':>10} {'Worst':>8} {'Time':>7}")
152	    print("-" * 70)
153	
154	    all_results = {}
155	
156	    for thresh in DIAG_THRESHOLDS:
157	        t0 = time.time()
158	        label = f"diag>={thresh:.1f}" if thresh > 0 else "full"
159	
160	        res = sample_and_analyze(N_SAMPLES, thresh, P_A, BETA, rng)
161	        elapsed = time.time() - t0
162	
163	        all_results[thresh] = res
164	
165	        print(f"{label:>12} {res['n_valid']:>8,} {100*res['violation_rate']:>10.1f}% "
166	              f"{100*res['sign_rev_rate']:>9.1f}% {100*res['amp_rate']:>9.1f}% "
167	              f"{res['worst_severity']:>8.2f} {elapsed:>6.1f}s")
168	
169	    # ── Worst-case per subspace ──────────────────────────────
170	    print("\n" + "=" * 85)
171	    print("Worst-Case C per Subspace")
172	    print("=" * 85)
173	
174	    for thresh, res in all_results.items():
175	        label = f"diag>={thresh:.1f}" if thresh > 0 else "full"
176	        if res['worst_C'] is None:
177	            print(f"\n{label}: no violations found")
178	            continue
179	
180	        C_w = res['worst_C']
181	        p_w = res['worst_plim']
182	        print(f"\n{label} (severity={res['worst_severity']:.2f}, "
183	              f"diag=[{C_w[0,0]:.3f}, {C_w[1,1]:.3f}, {C_w[2,2]:.3f}]):")
184	        for row in C_w:
185	            print(f"  [{row[0]:.3f}  {row[1]:.3f}  {row[2]:.3f}]")
186	
187	        for k in [1, 2]:
188	            if abs(BETA[k]) > 1e-10:
189	                ratio = p_w[k] / BETA[k]
190	                if p_w[k] * BETA[k] < 0:
191	                    tag = "SIGN REVERSAL"
192	                elif abs(p_w[k]) > abs(BETA[k]):
193	                    tag = "AMPLIFICATION"
194	                else:
195	                    tag = "toward null"
196	                print(f"  beta_{k}={BETA[k]:.2f} -> gamma_{k}={p_w[k]:.4f} "
197	                      f"(ratio={ratio:.2f}, {tag})")
198	
199	    # ── Paper framing guidance ───────────────────────────────
200	    print("\n" + "=" * 85)
201	    print("PAPER FRAMING GUIDANCE")
202	    print("=" * 85)
203	
204	    print(f"\n{'Subspace':<15} {'Violation':>10} {'SignRev':>10} {'Amplif':>10} {'Assessment':>25}")
205	    print("-" * 73)
206	    for thresh, res in all_results.items():
207	        label = f"diag>={thresh:.1f}" if thresh > 0 else "full space"
208	        vr = res['violation_rate']
209	        if vr > 0.10:
210	            assess = "STRONG argument"
211	        elif vr > 0.01:
212	            assess = "moderate (note scope)"
213	        elif vr > 0.001:
214	            assess = "weak (flag in paper)"
215	        elif vr > 0:
216	            assess = "rare (theoretical only)"
217	        else:
218	            assess = "no violations"
219	        print(f"{label:<15} {100*vr:>9.1f}% {100*res['sign_rev_rate']:>9.1f}% "
220	              f"{100*res['amp_rate']:>9.1f}% {assess:>25}")
221	
222	    elapsed_total = time.time() - t_start
223	    print(f"\nTotal runtime: {elapsed_total:.1f}s")
224	
225	
226	if __name__ == "__main__":
227	    main()
228	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6bd543a-0a14-4ce0-9eec-f72ab6c6c2ae",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "c235f10b-3610-4721-9475-b094c4e9332d",
  "sourceToolAssistantUUID": "a6bd543a-0a14-4ce0-9eec-f72ab6c6c2ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T08:57:43.835Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Uv4fuSP6n774LTeqhzaVRC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c235f10b-3610-4721-9475-b094c4e9332d",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYVM1hCyMtXGAuGfbqB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08eaf5cb-3c7a-4e7d-a8e4-8f227a1a1a12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtBQFENCYRSYKe9eauh4w6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19001,
      "cache_read_input_tokens": 31833,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19001
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 31833,
          "cache_creation_input_tokens": 19001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19001,
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

_source line 38 · 2026-05-20T08:57:43.842Z_

<details><summary>↩ Tool result · `toolu_01Uv4fuSP6n774LTeqhzaVRC`</summary>

```text
1	experiments:
2	  # =============================================
3	  # Claim 1: Multi-class bias taxonomy
4	  # =============================================
5	
6	  - id: plan_001
7	    claim: 1
8	    description: "Derive and MC-validate bias expressions for 6 DAG topologies with K=3"
9	    priority: P0
10	    gpu_budget_hours: 0
11	    deps: []
12	    registry_id: null  # MVP confounding DAG = art_20260520_f08c30 (1/6 done)
13	    details: >
14	      For each topology (confounding, mediation, collider, M-bias, instrument, front-door):
15	      derive closed-form K=3 bias expression, validate with MC (1000 reps × N=10000,
16	      6 confusion matrix structures including near-permutation extreme).
17	      Key question: which topologies show direction reversal under non-differential error?
18	      Confounding already validated in MVP (no reversal, monotonic toward OVB).
19	
20	  - id: plan_002
21	    claim: 1
22	    description: "Extend bias expressions to K=5,7 — matrix notation + interpretability tools"
23	    priority: P1
24	    gpu_budget_hours: 0
25	    deps: [plan_001]
26	    details: >
27	      Matrix-form expressions for general K. Three interpretability tools:
28	      (a) eigendecomposition summaries identifying dominant bias modes,
29	      (b) worst-case scalar bounds collapsing matrix to conservative scalar,
30	      (c) diagnostic visualizations mapping confusion matrix regions to bias magnitude.
31	      Validate on confounding + mediation + collider DAGs with K=5,7.
32	
33	  - id: plan_003
34	    claim: 1
35	    description: "Empirical confusion matrices: 3 LLMs × 3 CSS tasks vs gold-standard"
36	    priority: P0
37	    gpu_budget_hours: 0
38	    api_cost_estimate: "$300-550"
39	    deps: []
40	    details: >
41	      Tasks: protest event coding (K=5, ACLED/GPT-RE), stance detection (K=3, SemEval/VAST),
42	      toxicity (K=2, as special case / consistency check, Civil Comments).
43	      Models: Llama 4 Maverick (Together.ai), Qwen 3.5 Plus (OpenRouter), DeepSeek V4 (DeepSeek API).
44	      ~30K annotations per model × 3 datasets × 3 prompt variants.
45	      Output: empirical confusion matrices, inter-model correlation analysis,
46	      downstream regression bias vs gold-standard baseline.
47	
48	  - id: plan_008
49	    claim: 1
50	    description: "Binarization collapse analysis: K→2 folding bias across all 6 topologies"
51	    priority: P0
52	    gpu_budget_hours: 0
53	    deps: [plan_001]
54	    details: >
55	      For each of 6 topologies with K=3,5,7: collapse to binary, compare bias
56	      from full multi-class expression vs binarized expression.
57	      Demonstrate that binarization is not a safe shortcut — can amplify or reverse bias.
58	      MVP showed Δ up to 0.089 for confounding DAG K=3.
59	
60	  # =============================================
61	  # Claim 2: Annotation Sensitivity Values (ASVs)
62	  # =============================================
63	
64	  - id: plan_004
65	    claim: 2
66	    description: "ASV framework: formal proofs for confounding, mediation, collider"
67	    priority: P0
68	    gpu_budget_hours: 0
69	    deps: [plan_001]
70	    details: >
71	      Derive ASV expressions for 3 priority topologies.
72	      Formal proofs of: (a) monotonicity (ASV increases with δ amplification),
73	      (b) sharpness (bound is achievable for some confusion matrix).
74	      MC validation: coverage at 90%, 95%, 99% levels across 1000 scenarios.
75	
76	  - id: plan_005
77	    claim: 2
78	    description: "ASV MC validation for M-bias, instrument, front-door topologies"
79	    priority: P1
80	    gpu_budget_hours: 0
81	    deps: [plan_004]
82	    details: >
83	      ASV expressions + MC validation of monotonicity and coverage.
84	      Sharpness stated as conjectures supported by numerical evidence.
85	      If any topology fails monotonicity under MC, flag and investigate.
86	
87	  - id: plan_006
88	    claim: 2
89	    description: "ASV calibration on empirical data (3 CSS tasks × 3 LLMs)"
90	    priority: P0
91	    gpu_budget_hours: 0
92	    deps: [plan_003, plan_004]
93	    details: >
94	      Apply ASVs to empirical confusion matrices from plan_003.
95	      Validate coverage on held-out gold-standard splits.
96	      Report ASV alongside downstream effect estimates for each task.
97	      Compare ASV interpretability with raw confusion matrix reporting.
98	
99	  # =============================================
100	  # Claim 3: Correction guidance framework
101	  # =============================================
102	
103	  - id: plan_007
104	    claim: 3
105	    description: "Correction guidance framework: decision mapping + validation"
106	    priority: P1
107	    gpu_budget_hours: 0
108	    deps: [plan_001, plan_004, plan_003]
109	    details: >
110	      Decision framework: {topology × error structure × ASV} → correction method
111	      (DSL / PPI / MLA / naive plug-in / "no existing method adequate").
112	      MC validation: recommended method produces least bias in ≥90% of scenarios.
113	      Empirical validation on plan_003 data.
114	      Characterize regimes where no existing method suffices (correlated errors,
115	      differential multi-class, etc.) — identify as open problems.
116	
117	  # =============================================
118	  # Robustness / Ablation
119	  # =============================================
120	
121	  - id: plan_009
122	    claim: 1
123	    description: "Pathological confusion matrix analysis (near-permutation, rank-deficient)"
124	    priority: P2
125	    gpu_budget_hours: 0
126	    deps: [plan_001]
127	    details: >
128	      Extreme C structures: near-permutation, rank-deficient, block-diagonal.
129	      Characterize when bias becomes catastrophic across topologies.
130	      Identify structural conditions (spectral gap, diagonal dominance ratio)
131	      that predict bias severity — candidate features for practitioners.
132	
133	  # =============================================
134	  # Software / Reproducibility
135	  # =============================================
136	
137	  - id: plan_010
138	    claim: [1, 2, 3]
139	    description: "annot-sensitivity Python toolkit (open-source release)"
140	    priority: P1
141	    gpu_budget_hours: 0
142	    deps: [plan_001, plan_004, plan_007]
143	    details: >
144	      Package: user-specified DAG + confusion matrix(es) + downstream estimate →
145	      bias expressions (scalar K≤3, matrix K>3 with interpretability) +
146	      ASV bounds + sensitivity curves + correction recommendation + diagnostic plots.
147	      pip-installable, with worked examples for each topology.
148	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08eaf5cb-3c7a-4e7d-a8e4-8f227a1a1a12",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "1aa77b8d-0c98-4a22-b140-5d6c90683124",
  "sourceToolAssistantUUID": "08eaf5cb-3c7a-4e7d-a8e4-8f227a1a1a12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T08:57:46.856Z_

Now let me read the dream review reports for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aa77b8d-0c98-4a22-b140-5d6c90683124",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYVk9zHpFJtzguLJHsg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af94d828-256f-4915-af37-0247c3144192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAQpYZ5q2WNGGHM9HU24CE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5552,
      "cache_read_input_tokens": 50834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5552,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 40 · 2026-05-20T08:57:49.196Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BFr2B4UCSdYyKztm72pidy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af94d828-256f-4915-af37-0247c3144192",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYVk9zHpFJtzguLJHsg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6e95c3a-08a8-43c1-b38e-2087b45fcac3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAQpYZ5q2WNGGHM9HU24CE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5552,
      "cache_read_input_tokens": 50834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5552,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 41 · 2026-05-20T08:57:49.457Z_

<details><summary>↩ Tool result · `toolu_01BFr2B4UCSdYyKztm72pidy`</summary>

```text
1	narrative_guidance: 'Version A 完全成立。Lead finding: non-differential K≥3 误分类在 4 个 DAG
2	  拓扑（exposure, mediation, collider, front-door）中打破经典 toward-null 保证， 而 confounding
3	  和 instrument 保持单调性。反转模式严格拓扑依赖——同一混淆矩阵在 confounding DAG 中仅引起可预测的残差偏倚，在 mediation/collider
4	  DAG 中却产生方向反转。 Headline: "the same confusion matrix that is benign in confounding
5	  topology produces direction-reversing bias in mediation and collider topologies."
6	  ASV 框架在三个优先拓扑上均有完整单调性+紧性形式化证明，经验校准良好。Correction framework 在 95% 场景推荐最优方法。 Binarization
7	  collapse 分析强化了核心论点：K→2 折叠最大额外偏倚达 Δ=0.19，证明 binarization 不是安全退路。
8	
9	  '
10	imagined_experiments:
11	- name: Multi-topology bias derivation and MC validation (K=3)
12	  plan_id: plan_001
13	  description: '对 6 个 DAG 拓扑（confounding, mediation, collider, M-bias, instrument,
14	    front-door）推导 K=3 闭式偏倚表达式， 每个拓扑用 6 种混淆矩阵结构 × 1000 MC reps × N=10000 验证。另对 mediation/collider/front-door/M-bias/instrument
15	    执行 100k random C 搜索，检测方向反转违背率。
16	
17	    '
18	  expected_results:
19	    theory_mc_match_rate: 0.972
20	    theory_mc_match_detail: 35/36 structure×topology 组合落入 95% MC CI；1 个边界 case（front-door
21	      + rank-deficient C）偏差 0.003 超 CI 上界，增加到 N=50000 后收敛
22	    reversal_topologies_count: 4
23	    reversal_topologies:
24	    - exposure (MVP)
25	    - mediation
26	    - collider
27	    - front-door
28	    non_reversal_topologies:
29	    - confounding
30	    - instrument
31	    mediation_violation_rate: 0.52
32	    mediation_sign_reversal_rate: 0.47
33	    mediation_amplification_rate: 0.11
34	    collider_violation_rate: 0.41
35	    collider_sign_reversal_rate: 0.36
36	    collider_amplification_rate: 0.09
37	    frontdoor_violation_rate: 0.34
38	    frontdoor_sign_reversal_rate: 0.28
39	    frontdoor_amplification_rate: 0.12
40	    mbias_violation_rate: 0.0
41	    mbias_bias_range:
42	    - 0.04
43	    - 0.18
44	    instrument_violation_rate: 0.0
45	    instrument_bias_range:
46	    - 0.02
47	    - 0.14
48	    confounding_violation_rate: 0.0
49	    confounding_bias_range:
50	    - 0.063
51	    - 0.298
52	    mediation_worst_case: β_indirect=0.5 → estimate=-0.31 (sign reversal, 1.62x amplification)
53	    collider_worst_case: β_XY=0.0 (null) → estimate=0.44 (spurious effect creation
54	      + direction assignment)
55	    frontdoor_worst_case: β_total=0.8 → estimate=-0.22 (sign reversal via second-stage
56	      distortion)
57	  result_rationale: 'Mediation (violation rate 0.52): 间接效应 = β_XM × β_MY|X。K≥3 非差异误分类扭曲
58	    M→Y|X 回归系数—— 近置换矩阵 C 使相邻类别标签互换，导致 β_MY|X 符号翻转，从而间接效应反转。K=2 下非差异误分类只能将 β_MY|X  向零压缩（attenuation），结构上不可能越过零点。violation
59	    rate 0.52 而非更高（对比 exposure 的 0.85）， 因为间接效应经过两步回归（X→M 和 M→Y|X），仅当 C 同时严重扰动 M 的条件分布时才出现反转，
60	    而 exposure 误分类直接作用于处理变量，单步即可反转。
61	
62	    Collider (violation rate 0.41): 对 collider C̃ 条件化打开伪路径 X←U→C←V→Y。K≥3 误分类改变条件化的
63	    有效权重——不同类别的合并创造不同的伪关联模式。violation rate 低于 mediation 因为反转需要 C 矩阵 使 X-path 和 Y-path
64	    的贡献权重同时满足特定比例条件，约束更强。
65	
66	    Front-door (violation rate 0.34): 前门调整涉及两阶段估计（X→M 和 M→Y|do(X)）。K≥3 误分类不对称地 扭曲两个阶段——第一阶段
67	    attenuation 与第二阶段 distortion 的交互可使整体估计翻转。violation rate  最低因为反转需要两阶段同时被 C 严重扰动且扰动方向"配合"，是三个反转拓扑中约束最强的。
68	
69	    Confounding (violation rate 0.0): 已由 MVP 确认。残差混淆始终朝向 OVB 方向，因为误分类只能减少 confounder
70	    的解释力（信息丢失），不能创造新的混淆结构。K≥3 增加了更多丢失信息的方式但不改变方向性。
71	
72	    Instrument (violation rate 0.0): Wald estimator = Cov(Y,Z̃)/Cov(X,Z̃)。非差异误分类对
73	    Z 的两个 协方差施加相同方向的 attenuation（均乘以 C 的特征值相关因子），比值的符号不变。 K≥3 下分子分母的 attenuation 系数不再相同（不同特征值），导致幅度偏倚但符号保持。
74	
75	    M-bias (violation rate 0.0): M-bias（蝴蝶 DAG）中被误分类的变量本不应被条件化。 误分类使条件化效应减弱（信息丢失方向），偏倚幅度变化但不反转。
76	
77	    '
78	  tables:
79	  - name: 'Table 1: Topology × Reversal Summary'
80	    columns:
81	    - Topology
82	    - Role of Annotated Variable
83	    - Violation Rate (100k)
84	    - Sign Reversal Rate
85	    - Amplification Rate
86	    - Worst-Case Severity
87	    - K=2 Control
88	    rows:
89	    - - Confounding
90	      - Confounder
91	      - '0.000'
92	      - '0.000'
93	      - '0.000'
94	      - 0.298 (toward OVB)
95	      - toward OVB ✓
96	    - - Exposure (MVP)
97	      - Treatment
98	      - '0.850'
99	      - '0.834'
100	      - '0.141'
101	      - 2.83x amplification
102	      - toward null ✓
103	    - - Mediation
104	      - Mediator
105	      - '0.520'
106	      - '0.470'
107	      - '0.110'
108	      - 1.62x + sign reversal
109	      - toward null ✓
110	    - - Collider
111	      - Collider
112	      - '0.410'
113	      - '0.360'
114	      - '0.090'
115	      - spurious 0.44 from null
116	      - attenuated ✓
117	    - - M-bias
118	      - M-bias variable
119	      - '0.000'
120	      - '0.000'
121	      - '0.000'
122	      - 0.18 (attenuated)
123	      - attenuated ✓
124	    - - Instrument
125	      - Instrument
126	      - '0.000'
127	      - '0.000'
128	      - '0.000'
129	      - ratio distortion 0.14
130	      - attenuated ✓
131	    - - Front-door
132	      - Front-door variable
133	      - '0.340'
134	      - '0.280'
135	      - '0.120'
136	      - sign reversal
137	      - toward null ✓
138	  - name: 'Table 2: Theory-MC Match per Topology × C Structure'
139	    columns:
140	    - Topology
141	    - Diagonal-dominant
142	    - Moderate off-diag
143	    - Uniform off-diag
144	    - Block-diagonal
145	    - Near-permutation
146	    - Rank-deficient
147	    - Match Rate
148	    rows:
149	    - - Confounding
150	      - ✓
151	      - ✓
152	      - ✓
153	      - ✓
154	      - ✓
155	      - ✓
156	      - 6/6
157	    - - Mediation
158	      - ✓
159	      - ✓
160	      - ✓
161	      - ✓
162	      - ✓
163	      - ✓
164	      - 6/6
165	    - - Collider
166	      - ✓
167	      - ✓
168	      - ✓
169	      - ✓
170	      - ✓
171	      - ✓
172	      - 6/6
173	    - - M-bias
174	      - ✓
175	      - ✓
176	      - ✓
177	      - ✓
178	      - ✓
179	      - ✓
180	      - 6/6
181	    - - Instrument
182	      - ✓
183	      - ✓
184	      - ✓
185	      - ✓
186	      - ✓
187	      - ✓
188	      - 6/6
189	    - - Front-door
190	      - ✓
191	      - ✓
192	      - ✓
193	      - ✓
194	      - ✓
195	      - △*
196	      - 5/6
197	  figures_description:
198	  - 'Fig 1: 6-panel heatmap (one per topology), x=true effect size, y=confusion matrix
199	    diagonal dominance ratio, color=bias magnitude with sign (blue=toward null, red=away/reversal).
200	    清晰展示 mediation/collider/front-door 的红色反转区域 vs confounding/instrument/M-bias 的全蓝区域。'
201	  - 'Fig 2: Violin plots of 100k random C bias distribution per topology. Mediation/collider/front-door
202	    分布跨越零线；confounding/instrument/M-bias 分布完全在一侧。'
203	  - 'Fig 3: K=2 vs K=3 对比散点图（per topology）。所有 K=2 点落在 toward-null 区域，K=3 点在 mediation/collider/front-door
204	    中散布到反转区域。'
205	  analysis: '核心发现：非差异 K≥3 误分类的方向反转是拓扑依赖的。6 个拓扑分为两类：(1) 信息丢失型（confounding, instrument,
206	    M-bias）—— 误分类只能减少变量的信息量，偏倚方向可预测；(2) 结构扭曲型（exposure, mediation, collider, front-door）——
207	    误分类改变变量在 DAG 中的功能角色（如 mediator 的类别标签互换等价于改变 M→Y 的函数形式）， 导致不可预测的方向反转。这一二分法是论文的核心理论贡献。Confounding
208	    DAG 的"良性"行为不可推广到其他拓扑， 这直接挑战了实践者"non-differential error is conservative"的默认假设。
209	
210	    '
211	- name: General K bias expressions with interpretability tools (K=5,7)
212	  plan_id: plan_002
213	  description: '将偏倚表达式推广到矩阵形式（一般 K）。开发三种可解释性工具：(a) 特征分解摘要，(b) 最坏情况标量界， (c) 诊断可视化。在
214	    confounding + mediation + collider DAG 上用 K=5,7 验证。
215	
216	    '
217	  expected_results:
218	    eigendecomposition_variance_captured_top2: 0.87
219	    eigendecomposition_variance_captured_top3: 0.96
220	    worstcase_bound_tightness: 0.88
221	    worstcase_bound_tightness_detail: 最坏情况标量界在 88% 的场景中与真实最坏情况偏差 <15%
222	    K5_mediation_violation_rate: 0.61
223	    K5_collider_violation_rate: 0.49
224	    K7_mediation_violation_rate: 0.68
225	    K7_collider_violation_rate: 0.55
226	    K5_confounding_reversal: false
227	    K7_confounding_reversal: false
228	    theory_mc_match_K5: 17/18 within 95% CI
229	    theory_mc_match_K7: 16/18 within 95% CI
230	  result_rationale: 'K 增大时 violation rate 单调上升（mediation: 0.52→0.61→0.68；collider:
231	    0.41→0.49→0.55）， 因为混淆矩阵的自由参数从 K=3 的 6 个增长到 K=5 的 20 个、K=7 的 42 个。 更高维度的 C 矩阵有更多"方向"可以扭曲类别映射，使得
232	    random search 中遇到反转配置的概率增加。
233	
234	    特征分解 top-2 捕获 87% 方差：偏倚矩阵 B = f(C) 的谱结构由 C 的谱结构决定。 C 通常是行随机矩阵（行和为 1），其最大特征值为 1（对应"保真"模式），第二大特征值
235	    对应主要误分类模式。因此 B 的前 2 个特征值对应"无偏"基线和"主误分类方向"， 合计解释大部分方差。top-3 达 96% 因为第三个模式捕获了次要误分类模式。
236	
237	    最坏情况标量界紧度 88%：该界通过对 B 的谱范数取上界得到，对于高对角优势 C  这个界很紧（谱范数 ≈ 最大特征值），但对于结构化偏差（如 block-diagonal
238	    C） 谱范数高估约 25-30%，拉低了整体紧度。
239	
240	    Theory-MC match 在 K=7 时略降（16/18 vs K=3 的 35/36）：高维 MC 模拟的方差增大， 需要更大 N 才能达到同样精度。2
241	    个未匹配 case 均为 near-permutation extreme， 增加到 N=50000 后收敛。
242	
243	    '
244	  tables:
245	  - name: 'Table 3: Violation Rate Scaling with K'
246	    columns:
247	    - Topology
248	    - K=3
249	    - K=5
250	    - K=7
251	    - Trend
252	    rows:
253	    - - Confounding
254	      - '0.000'
255	      - '0.000'
256	      - '0.000'
257	      - Stable at 0 (monotonic toward OVB)
258	    - - Mediation
259	      - '0.520'
260	      - '0.610'
261	      - '0.680'
262	      - Monotonically increasing
263	    - - Collider
264	      - '0.410'
265	      - '0.490'
266	      - '0.550'
267	      - Monotonically increasing
268	  - name: 'Table 4: Eigendecomposition Variance Explained'
269	    columns:
270	    - Topology
271	    - K
272	    - Top-1 EV%
273	    - Top-2 EV%
274	    - Top-3 EV%
275	    rows:
276	    - - Confounding
277	      - '5'
278	      - 72%
279	      - 89%
280	      - 97%
281	    - - Confounding
282	      - '7'
283	      - 68%
284	      - 85%
285	      - 95%
286	    - - Mediation
287	      - '5'
288	      - 70%
289	      - 87%
290	      - 96%
291	    - - Mediation
292	      - '7'
293	      - 65%
294	      - 84%
295	      - 94%
296	    - - Collider
297	      - '5'
298	      - 71%
299	      - 88%
300	      - 96%
301	    - - Collider
302	      - '7'
303	      - 66%
304	      - 85%
305	      - 95%
306	  figures_description:
307	  - 'Fig 4: Bias matrix eigenspectrum plots (K=5,7) per topology，展示前 3 个特征值占主导地位，剩余特征值快速衰减。'
308	  - 'Fig 5: Worst-case bound vs true worst-case scatter plot，color by C structure
309	    type。Block-diagonal 点偏离对角线最远，diagonal-dominant 点最接近。'
310	  - 'Fig 6: Diagnostic heatmap——K=5 confusion matrix region → bias magnitude，用户可直接定位其实证
311	    C 落在哪个 bias regime。'
312	  analysis: 'K 增大强化了核心论点：随着分类粒度增加，binary 近似的失效更严重，方向反转概率上升。 可解释性工具使 K≥5 的矩阵偏倚表达式在实践中可用：研究者无需理解完整
313	    K×K 偏倚矩阵， 只需检查 top-2 特征模式即可判断偏倚的方向和严重程度。最坏情况标量界为风险厌恶型研究者 提供保守但可操作的单一数字。
314	
315	    '
316	- name: 'Empirical confusion matrices: 3 LLMs × 3 CSS tasks'
317	  plan_id: plan_003
318	  description: '收集 3 个 LLM（Llama 4 Maverick, Qwen 3.5 Plus, DeepSeek V4）在 3 个 CSS
319	    任务 （protest event coding K=5, stance detection K=3, toxicity K=2）上的实证混淆矩阵。 ~30K
320	    annotations per model × 3 datasets × 3 prompt variants。
321	
322	    '
323	  expected_results:
324	    total_annotations: ~270K (3 models × 3 tasks × ~30K)
325	    protest_K5_avg_diagonal_dominance: 0.62
326	    protest_K5_inter_model_kappa: 0.71
327	    stance_K3_avg_diagonal_dominance: 0.74
328	    stance_K3_inter_model_kappa: 0.68
329	    toxicity_K2_avg_accuracy: 0.89
330	    toxicity_K2_inter_model_kappa: 0.76
331	    cross_model_error_correlation: 0.58
332	    cross_model_error_correlation_detail: 当两个模型均出错时，58% 的 case 错向同一类别（与 Kim et al.
333	      的 60% 一致）
334	    distinct_C_structures_observed: 9
335	    near_permutation_cases: 2
336	    block_diagonal_cases: 3
337	    prompt_variant_C_shift: prompt 变体导致 C 结构在 Frobenius 距离上变化 0.04-0.12
338	    downstream_bias_vs_gold_protest:
339	    - -0.08
340	    - 0.15
341	    downstream_bias_vs_gold_stance:
342	    - -0.05
343	    - 0.09
344	    downstream_bias_vs_gold_toxicity:
345	    - -0.02
346	    - 0.03
347	  result_rationale: 'Protest event coding (K=5) 对角优势最低（0.62）：5 类任务（peaceful protest,
348	    violent protest,  strategic development, government response, other）存在固有歧义——"strategic
349	    development"与  "peaceful protest"常被混淆，LLM 倾向于对 borderline case 系统性偏向高频类别。 低对角优势意味着
350	    C 矩阵偏离对角，更接近 random search 中产生反转的区域。
351	
352	    Stance detection (K=3) 对角优势较高（0.74）：3 类（favor, against, neutral）语义距离较大， 但 neutral
353	    与 against 的边界模糊导致特定 off-diagonal 元素偏高，形成 block-diagonal 结构 （favor 与 against/neutral
354	    分离，但 against-neutral 互相混淆）。
355	
356	    Toxicity (K=2) 准确率最高（0.89）：二分类任务较简单，且 toxicity 有较清晰的语言标记。 作为 binary special case
357	    / consistency check——K=2 下所有模型的偏倚均 toward null， 与理论预测一致。
358	
359	    跨模型错误相关 0.58：Kim et al. (ICML 2025) 报告 60%，我们的 0.58 高度一致。 这不是巧合——LLM 共享类似的预训练数据和推理模式，对同类歧义样本倾向于犯同类错误。
360	    这个发现强化了我们的论点：多模型集成无法消除系统性偏倚，必须分析 C 结构。
361	
362	    9 种不同 C 结构（3 models × 3 tasks）为后续 ASV 校准提供了充分多样性。 2 个 near-permutation cases 出现在
363	    protest coding 的特定 prompt 变体下（过度指令化导致 类别定义混乱），3 个 block-diagonal cases 出现在 stance
364	    detection 中（favor 孤立）。
365	
366	    '
367	  tables:
368	  - name: 'Table 5: Empirical Confusion Matrix Summary'
369	    columns:
370	    - Task
371	    - K
372	    - Model
373	    - Accuracy
374	    - Diagonal Dominance
375	    - Largest Off-Diag
376	    - C Structure Type
377	    rows:
378	    - - Protest
379	      - '5'
380	      - Llama 4 Maverick
381	      - '0.64'
382	      - '0.60'
383	      - 0.18 (strat_dev→peaceful)
384	      - Moderate off-diag
385	    - - Protest
386	      - '5'
387	      - Qwen 3.5 Plus
388	      - '0.60'
389	      - '0.57'
390	      - 0.21 (strat_dev→peaceful)
391	      - Near-permutation
392	    - - Protest
393	      - '5'
394	      - DeepSeek V4
395	      - '0.67'
396	      - '0.63'
397	      - 0.15 (other→gov_resp)
398	      - Block-diagonal
399	    - - Stance
400	      - '3'
401	      - Llama 4 Maverick
402	      - '0.77'
403	      - '0.76'
404	      - 0.14 (neutral→against)
405	      - Block-diagonal
406	    - - Stance
407	      - '3'
408	      - Qwen 3.5 Plus
409	      - '0.73'
410	      - '0.72'
411	      - 0.16 (against→neutral)
412	      - Block-diagonal
413	    - - Stance
414	      - '3'
415	      - DeepSeek V4
416	      - '0.76'
417	      - '0.75'
418	      - 0.13 (neutral→against)
419	      - Block-diagonal
420	    - - Toxicity
421	      - '2'
422	      - Llama 4 Maverick
423	      - '0.91'
424	      - '0.91'
425	      - 0.09 (toxic→non-toxic)
426	      - Diagonal-dominant
427	    - - Toxicity
428	      - '2'
429	      - Qwen 3.5 Plus
430	      - '0.87'
431	      - '0.87'
432	      - 0.13 (non-toxic→toxic)
433	      - Diagonal-dominant
434	    - - Toxicity
435	      - '2'
436	      - DeepSeek V4
437	      - '0.90'
438	      - '0.90'
439	      - 0.10 (toxic→non-toxic)
440	      - Diagonal-dominant
441	  - name: 'Table 6: Inter-Model Error Agreement'
442	    columns:
443	    - Task
444	    - Model Pair
445	    - Cohen's κ
446	    - Error Agreement Rate
447	    - Same-Direction Error %
448	    rows:
449	    - - Protest
450	      - Llama-Qwen
451	      - '0.69'
452	      - '0.24'
453	      - '0.61'
454	    - - Protest
455	      - Llama-DeepSeek
456	      - '0.72'
457	      - '0.21'
458	      - '0.57'
459	    - - Protest
460	      - Qwen-DeepSeek
461	      - '0.68'
462	      - '0.25'
463	      - '0.56'
464	    - - Stance
465	      - Llama-Qwen
466	      - '0.67'
467	      - '0.18'
468	      - '0.59'
469	    - - Stance
470	      - Llama-DeepSeek
471	      - '0.70'
472	      - '0.16'
473	      - '0.58'
474	    - - Stance
475	      - Qwen-DeepSeek
476	      - '0.66'
477	      - '0.19'
478	      - '0.57'
479	    - - Toxicity
480	      - All pairs avg
481	      - '0.76'
482	      - '0.09'
483	      - '0.62'
484	  figures_description:
485	  - 'Fig 7: 9 个实证混淆矩阵热力图（3×3 grid: rows=models, cols=tasks）。Protest 列明显更''散''（低对角优势），toxicity
486	    列高度集中在对角。'
487	  - 'Fig 8: PCA projection of 9 confusion matrices onto theoretical C structure space，标注每个矩阵落在
488	    random search 偏倚分布的哪个区域。'
489	  analysis: '实证 C 矩阵覆盖了理论分析中的多种结构类型（diagonal-dominant, block-diagonal, near-permutation），
490	    为后续 ASV 校准和 correction framework 验证提供了现实基础。关键观察： (1) Protest coding 的 C 矩阵接近 plan_001
491	    中产生反转的区域，预示该任务在 mediation/collider  拓扑下风险最高；(2) 跨模型错误高度相关，确认多 LLM 集成不是解决方案； (3)
492	    Prompt 变体可显著移动 C 结构（Frobenius Δ 达 0.12），暗示 prompt engineering  本身是一种（未被充分认识的）bias
493	    intervention。
494	
495	    '
496	- name: Binarization collapse analysis across all topologies
497	  plan_id: plan_008
498	  description: '对 6 个拓扑 + exposure（共 7 个拓扑），K=3,5,7 条件下，将 K 类变量折叠为二分类， 比较完整多类偏倚表达式
499	    vs 二值化后偏倚表达式的差异 Δ。
500	
501	    '
502	  expected_results:
503	    binarization_max_delta: 0.19
504	    binarization_max_delta_topology: mediation
505	    binarization_max_delta_K: 7
506	    binarization_avg_delta_K3: 0.08
507	    binarization_avg_delta_K5: 0.13
508	    binarization_avg_delta_K7: 0.16
509	    binarization_direction_reversal_cases: 12% of K=5,7 scenarios show Δ that flips
510	      bias direction
511	    binarization_delta_by_topology:
512	      confounding_K3: 0.06
513	      confounding_K5: 0.09
514	      confounding_K7: 0.11
515	      mediation_K3: 0.1
516	      mediation_K5: 0.15
517	      mediation_K7: 0.19
518	      collider_K3: 0.09
519	      collider_K5: 0.14
520	      collider_K7: 0.17
521	      exposure_K3: 0.08
522	      exposure_K5: 0.12
523	      exposure_K7: 0.15
524	      mbias_K3: 0.05
525	      mbias_K5: 0.08
526	      mbias_K7: 0.1
527	      instrument_K3: 0.04
528	      instrument_K5: 0.07
529	      instrument_K7: 0.09
530	      frontdoor_K3: 0.09
531	      frontdoor_K5: 0.13
532	      frontdoor_K7: 0.16
533	  result_rationale: 'Binarization max Δ = 0.19（mediation, K=7）：折叠 7 类 mediator 为二分类丢弃了类别间的
534	    细粒度偏倚结构。Mediation DAG 中间接效应依赖 M 的分布形状——当 7 个类别被折叠为 2 个时， 被合并的类别可能具有相反方向的 M→Y 效应，导致折叠后的间接效应与原始间接效应方向相反。
535	    K=7 比 K=3 更严重因为折叠时信息丢失更多（5 个类别被合并 vs 1 个类别被合并）。
536	
537	    Δ 随 K 单调增大（avg: 0.08→0.13→0.16）：这是信息论上的必然——K→2 折叠的信息丢失 量为 log(K)-log(2)，K 越大丢失越多。
538	
539	    12% 的 K=5,7 场景中 Δ 本身导致方向翻转：这意味着研究者试图通过 binarization  "逃入"二分类安全区域的策略不仅无效（因为折叠引入新偏倚），而且在
540	    12% 的场景中 反而比保留多类更危险。这个发现直接回应了一个预期的 reviewer concern： "既然 binary case 有保证，为什么不直接
541	    binarize？"
542	
543	    Mediation > Collider > Front-door > Exposure > Confounding > M-bias > Instrument
544	    的 Δ 排序： Mediation 最大因为间接效应的非线性依赖 M 的类别分布；Instrument 最小因为 IV 估计 主要依赖 Z 的第一阶段 F-statistic，对类别合并方式的敏感度较低。
545	
546	    '
547	  tables:
548	  - name: 'Table 7: Binarization Collapse Δ by Topology × K'
549	    columns:
550	    - Topology
551	    - K=3 Δ
552	    - K=5 Δ
553	    - K=7 Δ
554	    - Max Δ
555	    - Direction Reversal by Δ?
556	    rows:
557	    - - Confounding
558	      - '0.06'
559	      - '0.09'
560	      - '0.11'
561	      - '0.11'
562	      - 'No'
563	    - - Exposure
564	      - '0.08'
565	      - '0.12'
566	      - '0.15'
567	      - '0.15'
568	      - Yes (3% of K=7)
569	    - - Mediation
570	      - '0.10'
571	      - '0.15'
572	      - '0.19'
573	      - '0.19'
574	      - Yes (18% of K=7)
575	    - - Collider
576	      - '0.09'
577	      - '0.14'
578	      - '0.17'
579	      - '0.17'
580	      - Yes (14% of K=7)
581	    - - M-bias
582	      - '0.05'
583	      - '0.08'
584	      - '0.10'
585	      - '0.10'
586	      - 'No'
587	    - - Instrument
588	      - '0.04'
589	      - '0.07'
590	      - '0.09'
591	      - '0.09'
592	      - 'No'
593	    - - Front-door
594	      - '0.09'
595	      - '0.13'
596	      - '0.16'
597	      - '0.16'
598	      - Yes (11% of K=7)
599	  figures_description:
600	  - 'Fig 9: Δ vs K 折线图（7 条线 = 7 拓扑），清晰展示 Δ 随 K 单调增长且拓扑间差异系统性存在。'
601	  - 'Fig 10: Scatter plot of multi-class bias vs binarized bias per topology，对角线 =
602	    无折叠偏倚。偏离对角线的点即 Δ ≠ 0，红点 = 方向翻转 case。'
603	  analysis: 'Binarization 不是安全退路。Max Δ = 0.19 在实际社会科学研究中足以改变实质性结论 （典型效应量 0.1-0.3）。这一结果与
604	    MVP 中 confounding DAG 的 Δ=0.103 一致且推广： 更多拓扑、更高 K 值下 Δ 更大。结合 plan_001 的方向反转结果，完整论点是：
605	    (1) 保留多类可能导致方向反转，(2) 折叠为二类也不安全——研究者无处可逃，必须使用 ASV 框架 诊断其具体 {C × topology} 组合的偏倚性质。
606	
607	    '
608	- name: ASV formal proofs for 3 priority topologies
609	  plan_id: plan_004
610	  description: '推导 confounding, mediation, collider 三个优先拓扑的 ASV 表达式。 形式化证明单调性（ASV
611	    随 δ 增大而增大）和紧性（bound 可被某个 C 达到）。 MC 验证：1000 scenarios × coverage at 90%, 95%, 99%
612	    levels。
613	
614	    '
615	  expected_results:
616	    asv_sharpness_formal_proofs: 3
617	    asv_monotonicity_proofs: 3
618	    proof_technique_confounding: algebraic — closed-form ASV as function of spectral
619	      gap of C and δ
620	    proof_technique_mediation: algebraic + envelope theorem — indirect effect ASV
621	      via product-of-coefficients decomposition
622	    proof_technique_collider: algebraic + Lagrangian optimization — ASV as constrained
623	      optimization over C perturbation space
624	    asv_coverage_90_nominal: 0.912
625	    asv_coverage_95_nominal: 0.952
626	    asv_coverage_99_nominal: 0.988
627	    asv_coverage_by_topology:
628	      confounding_95: 0.958
629	      mediation_95: 0.949
630	      collider_95: 0.948
631	    mc_scenarios: 1000
632	    mc_reps_per_scenario: 500
633	    sharpness_achieving_C_found: 100% of scenarios — constructive proof provides explicit
634	      C* achieving bound
635	  result_rationale: '三个证明均成功（asv_sharpness_formal_proofs = 3）：这是 best tier 的硬性要求，但也是
636	    数学上可行的，因为三个拓扑的偏倚表达式在 K=3 时有足够简洁的闭式形式。
637	
638	    Confounding ASV：残差混淆偏倚 = OVB × (1 - f(C))，其中 f(C) 是 C 的对角优势函数。 ASV = min{δ : |OVB
639	    × (1-f(C·diag(1+δ)))| > threshold}。单调性：f 关于 δ 单调递减 （扰动增大→C 偏离对角→更多残差混淆），因此 ASV
640	    单调。紧性：构造 C* = 在 δ 约束下 使 f(C*) 最小化的行随机矩阵（显式构造）。
641	
642	    Mediation ASV：间接效应 = β_XM × β_MY|X，两者均是 C 的函数。ASV 通过乘积分解为 两个单调函数的乘积——当两者符号一致时整体单调，当符号不一致时需要
643	    envelope theorem 处理极值切换，但最终仍可证明关于 δ 的单调性。紧性通过构造性 Lagrangian 求解 使间接效应恰好等于 threshold
644	    的 C*。
645	
646	    Collider ASV：条件化打开伪路径的效应大小是 C 的非线性函数。通过 Lagrangian 优化 在 {C : ||C - I|| ≤ g(δ)}
647	    约束集上求解伪效应的极值，证明该极值关于 δ 单调。 紧性：Lagrangian 的 KKT 条件给出显式 C*。
648	
649	    Coverage at 95% nominal = 0.952（在 [0.93, 0.97] 范围内）：轻微过覆盖（0.952 > 0.950） 是因为 ASV
650	    bound 使用了保守的 worst-case C 方向，而大多数实际 C 不在最坏方向上。 这种过覆盖是良性的（保守偏倚）。Mediation (0.949)
651	    和 collider (0.948) 的覆盖率 略低于 confounding (0.958)，因为这两个拓扑的偏倚函数非线性更强， ASV 的线性化近似在极端
652	    δ 值附近不够精确。
653	
654	    '
655	  tables:
656	  - name: 'Table 8: ASV Formal Proof Summary'
657	    columns:
658	    - Topology
659	    - Monotonicity
660	    - Sharpness
661	    - Proof Technique
662	    - Constructive C*?
663	    rows:
664	    - - Confounding
665	      - ✓ Proved
666	      - ✓ Proved
667	      - Algebraic (spectral gap)
668	      - Yes — explicit
669	    - - Mediation
670	      - ✓ Proved
671	      - ✓ Proved
672	      - Algebraic + envelope theorem
673	      - Yes — explicit
674	    - - Collider
675	      - ✓ Proved
676	      - ✓ Proved
677	      - Lagrangian optimization + KKT
678	      - Yes — explicit
679	  - name: 'Table 9: ASV Coverage Calibration (MC, 1000 scenarios)'
680	    columns:
681	    - Topology
682	    - Nominal 90%
683	    - Actual 90%
684	    - Nominal 95%
685	    - Actual 95%
686	    - Nominal 99%
687	    - Actual 99%
688	    rows:
689	    - - Confounding
690	      - 90%
691	      - 91.8%
692	      - 95%
693	      - 95.8%
694	      - 99%
695	      - 99.2%
696	    - - Mediation
697	      - 90%
698	      - 90.9%
699	      - 95%
700	      - 94.9%
701	      - 99%
702	      - 98.7%
703	    - - Collider
704	      - 90%
705	      - 90.8%
706	      - 95%
707	      - 94.8%
708	      - 99%
709	      - 98.5%
710	    - - Average
711	      - 90%
712	      - 91.2%
713	      - 95%
714	      - 95.2%
715	      - 99%
716	      - 98.8%
717	  figures_description:
718	  - 'Fig 11: ASV sensitivity curves per topology——x=δ, y=bias bound, with MC point
719	    estimates overlaid. 证明 bound 确实是上界且紧。'
720	  - 'Fig 12: Coverage probability plot——nominal level (x) vs actual coverage (y)。理想情况为对角线。三个拓扑均紧贴对角线，confounding
721	    略微过覆盖。'
722	  analysis: '三个完整形式化证明是本论文最重要的理论贡献之一。ASV 类比于因果推断中的 E-value： E-value 量化 "多大的未测量混淆才能推翻结论"，ASV
723	    量化 "多大的标注误差才能推翻结论"。 关键区别：E-value 只需一个标量参数（RR），ASV 需要参考混淆矩阵 + δ 方向， 因此证明复杂度更高。构造性紧性证明（显式
724	    C*）不仅有理论价值，还有实践价值—— 研究者可以检查 "使结论翻转的最近 C* 与我的实证 C 有多远"，获得直觉性理解。
725	
726	    '
727	- name: ASV MC validation for remaining 3 topologies
728	  plan_id: plan_005
729	  description: '对 M-bias, instrument, front-door 三个拓扑推导 ASV 表达式，MC 验证单调性和覆盖率。 紧性作为猜想，用数值证据支持。
730	
731	    '
732	  expected_results:
733	    asv_monotonicity_mc_validated: 3
734	    asv_monotonicity_violations: 0
735	    asv_coverage_95_mbias: 0.954
736	    asv_coverage_95_instrument: 0.961
737	    asv_coverage_95_frontdoor: 0.943
738	    sharpness_numerical_gap: < 0.008 across all 3 topologies (bound within 0.8% of
739	      achievable)
740	    sharpness_conjecture_status: Supported by 1000 scenario numerical optimization
741	      — no counterexample found
742	    frontdoor_asv_note: Front-door ASV 涉及两阶段估计的联合扰动，闭式紧性证明需要解决双线性约束优化，identified as
743	      immediate future work
744	  result_rationale: '单调性在所有 3 个拓扑的 MC 验证中均成立（0 violations）：单调性是一个"自然"性质—— 更大的标注误差（更大的
745	    δ）只能增加偏倚的潜在范围，不能减少它。这在直觉上成立： δ 增大扩展了 C 的可行域，而偏倚 bound 是在可行域上的 supremum， 可行域扩大
746	    → supremum 不减。形式化证明的技术难点在于处理非凸可行域， 但 MC 验证表明即使在解析证明困难的情况下，性质仍成立。
747	
748	    紧性作为猜想而非证明：M-bias 的 DAG 结构（butterfly）使偏倚表达式涉及 4 个 条件概率的乘积，优化问题是四次多项式约束优化，闭式解不可行。
749	    Instrument 的 Wald ratio 使约束优化涉及分式规划。 Front-door 的两阶段结构使约束是双线性的。 数值优化（sequential
750	    quadratic programming）在所有场景中找到的最优 C  与 ASV bound 的差距 < 0.008，强烈支持紧性但不构成证明。
751	
752	    Front-door coverage 略低（0.943）：两阶段估计的非线性使 ASV 的线性化近似 在 extreme δ 附近不够精确，但仍在 [0.93,
753	    0.97] 范围内。
754	
755	    '
756	  tables:
757	  - name: 'Table 10: ASV Validation for Remaining Topologies'
758	    columns:
759	    - Topology
760	    - Monotonicity
761	    - Coverage @95%
762	    - Sharpness Gap
763	    - Formal Proof Status
764	    rows:
765	    - - M-bias
766	      - ✓ MC-validated (0 violations/1000)
767	      - 95.4%
768	      - '0.006'
769	      - Conjecture (numerical)
770	    - - Instrument
771	      - ✓ MC-validated (0 violations/1000)
772	      - 96.1%
773	      - '0.005'
774	      - Conjecture (numerical)
775	    - - Front-door
776	      - ✓ MC-validated (0 violations/1000)
777	      - 94.3%
778	      - '0.008'
779	      - Conjecture (numerical)
780	  figures_description:
781	  - 'Fig 13: Monotonicity verification——对每个拓扑展示 1000 个 scenario 的 ASV(δ) 曲线，全部单调递增，无一例外。'
782	  - 'Fig 14: Sharpness gap histogram——gap 集中在 0.002-0.008 范围，远小于 ASV 值本身（通常 0.1-0.5），支持紧性猜想。'
783	  analysis: '诚实地将紧性限定为猜想（而非证明）是策略性选择：(1) 避免 reviewer 质疑证明严谨性， (2) 数值证据已经足够有说服力（gap
784	    < 0.008），(3) 完整证明作为 immediate future work  为后续论文提供了明确方向。六个拓扑的 ASV 框架完整性：3 个有完整证明
785	    + 3 个有强数值支持， 覆盖了实践者可能遇到的所有主要 DAG 设计。
786	
787	    '
788	- name: ASV calibration on empirical data
789	  plan_id: plan_006
790	  description: '将 ASV 框架应用于 plan_003 的实证混淆矩阵。在 held-out gold-standard splits 上验证覆盖率。
791	    报告 ASV alongside downstream effect estimates。比较 ASV 可解释性与原始混淆矩阵报告。
792	
793	    '
794	  expected_results:
795	    empirical_asv_concordance: 8
796	    empirical_asv_concordance_detail: 9 个 scenario（3 tasks × 3 topological contexts）中
797	      8 个 ASV 排序与实际 bias 严重度一致
798	    discordant_case: 'protest × instrument context: ASV 排序 DeepSeek > Qwen，实际 bias
799	      Qwen > DeepSeek（差异 0.02，在 noise margin 内）'
800	    asv_interpretability_rating: 研究者 pilot（N=5）中 4/5 偏好 ASV + sensitivity curve 而非原始
801	      C 矩阵
802	    held_out_coverage_95: 0.94
803	    asv_actionable_alerts: 3/9 scenarios ASV < 1.5（结论脆弱），6/9 ASV > 3.0（结论稳健）
804	    asv_correctly_flags_reversal_risk: 2/2 scenarios where empirical C falls in reversal
805	      zone are flagged by ASV < 1.5
806	  result_rationale: 'Concordance 8/9：ASV 是基于 worst-case perturbation 的 bound，而非 point
807	    estimate。 在大多数场景中，worst-case 方向与实际偏倚方向一致，因此排序一致。 唯一 discordant case 出现在 instrument
808	    context，因为 Wald ratio 对 C 的微小差异 极其敏感（分母接近零时），导致 ASV 排序与实际偏倚排序在 noise margin 内翻转。
809	    差异仅 0.02，在实际意义上可忽略。
810	
811	    3/9 scenarios ASV < 1.5：这些对应 protest coding（K=5, 低对角优势 C）在  mediation 和 collider
812	    拓扑下的应用。ASV < 1.5 意味着仅需 50% 的额外标注误差 即可推翻结论——这是一个强警告信号。6/9 ASV > 3.0 对应较简单的 toxicity
813	    任务 和 confounding 拓扑，结论稳健。
814	
815	    ASV 正确标记了 2 个落入反转区域的实证 C：这是 ASV 框架实用价值的最直接证据。 研究者报告原始 C 矩阵时无法判断"这个 C 有多危险"——ASV
816	    提供了这个判断。
817	
818	    Held-out coverage 0.94（vs 理论 0.95）：轻微欠覆盖因为实证 C 的估计本身有 sampling variance（~30K annotations），引入了理论分析未考虑的噪声。
819	    但 0.94 在可接受范围内。
820	
821	    '
822	  tables:
823	  - name: 'Table 11: ASV Concordance with Empirical Bias Severity'
824	    columns:
825	    - Task
826	    - Topological Context
827	    - Model Ranking by ASV
828	    - Model Ranking by Actual Bias
829	    - Concordant?
830	    rows:
831	    - - Protest
832	      - Mediation
833	      - Qwen < Llama < DeepSeek
834	      - Qwen < Llama < DeepSeek
835	      - ✓
836	    - - Protest
837	      - Collider
838	      - Qwen < Llama < DeepSeek
839	      - Qwen < Llama < DeepSeek
840	      - ✓
841	    - - Protest
842	      - Instrument
843	      - DeepSeek < Qwen < Llama
844	      - Qwen < DeepSeek < Llama
845	      - ✗ (margin 0.02)
846	    - - Stance
847	      - Mediation
848	      - Qwen < Llama < DeepSeek
849	      - Qwen < Llama < DeepSeek
850	      - ✓
851	    - - Stance
852	      - Collider
853	      - Llama < Qwen < DeepSeek
854	      - Llama < Qwen < DeepSeek
855	      - ✓
856	    - - Stance
857	      - Confounding
858	      - Llama < Qwen < DeepSeek
859	      - Llama < Qwen < DeepSeek
860	      - ✓
861	    - - Toxicity
862	      - Mediation
863	      - Qwen < Llama < DeepSeek
864	      - Qwen < Llama < DeepSeek
865	      - ✓
866	    - - Toxicity
867	      - Collider
868	      - Qwen < DeepSeek < Llama
869	      - Qwen < DeepSeek < Llama
870	      - ✓
871	    - - Toxicity
872	      - Confounding
873	      - Qwen < Llama < DeepSeek
874	      - Qwen < Llama < DeepSeek
875	      - ✓
876	  - name: 'Table 12: ASV Robustness Classification'
877	    columns:
878	    - Task
879	    - Context
880	    - Best Model ASV
881	    - Worst Model ASV
882	    - Classification
883	    rows:
884	    - - Protest
885	      - Mediation
886	      - 2.1 (DeepSeek)
887	      - 0.9 (Qwen)
888	      - FRAGILE — reversal risk
889	    - - Protest
890	      - Collider
891	      - 1.8 (DeepSeek)
892	      - 1.1 (Qwen)
893	      - FRAGILE — reversal risk
894	    - - Protest
895	      - Instrument
896	      - 3.2 (Llama)
897	      - 2.4 (DeepSeek)
898	      - Moderate
899	    - - Stance
900	      - Mediation
901	      - 4.1 (DeepSeek)
902	      - 2.8 (Qwen)
903	      - Robust
904	    - - Stance
905	      - Collider
906	      - 3.8 (DeepSeek)
907	      - 2.5 (Llama)
908	      - Moderate
909	    - - Stance
910	      - Confounding
911	      - 5.2 (DeepSeek)
912	      - 3.9 (Llama)
913	      - Robust
914	    - - Toxicity
915	      - Mediation
916	      - 7.3 (Llama)
917	      - 5.1 (Qwen)
918	      - Robust
919	    - - Toxicity
920	      - Collider
921	      - 6.8 (Llama)
922	      - 4.9 (Qwen)
923	      - Robust
924	    - - Toxicity
925	      - Confounding
926	      - 8.1 (DeepSeek)
927	      - 6.2 (Qwen)
928	      - Robust
929	  figures_description:
930	  - 'Fig 15: ASV sensitivity curves for 9 empirical scenarios，实证 C 的位置标注在曲线上。FRAGILE
931	    scenarios 的 C 落在曲线陡峭区域（小 δ 即翻转）。'
932	  - 'Fig 16: Side-by-side comparison——左：原始 C 矩阵热力图（研究者通常报告的）；右：ASV robustness gauge（绿/黄/红）。直观展示
933	    ASV 的信息增益。'
934	  analysis: '8/9 concordance 证明 ASV 在实践中是有效的偏倚严重度指标。唯一 discordance 出现在 noise margin
935	    内，且在 instrument context（本身就是高方差估计）。关键实用发现： protest event coding 在 mediation/collider
936	    context 下使用 Qwen 3.5 Plus 时 ASV < 1.0—— 这意味着研究者如果用 Qwen 做 protest 分类并将其作为 mediator/collider，其下游因果结论
937	    几乎肯定不可靠。这种 actionable alert 是单纯报告混淆矩阵无法提供的。
938	
939	    '
940	- name: Correction guidance framework validation
941	  plan_id: plan_007
942	  description: '构建决策框架：{topology × error structure × ASV} → correction method（DSL
943	    / PPI / MLA / naive plug-in / "无现有方法适用"）。 MC 验证推荐方法在各场景中是否产生最小偏倚。在 plan_003 数据上经验验证。
944	
945	    '
946	  expected_results:
947	    correction_framework_accuracy: 0.95
948	    correction_framework_accuracy_detail: 432 个 MC scenario 中 411 个推荐方法产生最小 bias
949	    scenarios_tested: 432
950	    scenario_breakdown: 6 topologies × 6 C structures × 3 K values × 4 effect sizes
951	      = 432
952	    method_recommendation_distribution:
953	      DSL: 18% of scenarios
954	      PPI: 24% of scenarios
955	      MLA: 31% of scenarios
956	      naive_plugin: 12% of scenarios
957	      no_adequate_method: 15% of scenarios
958	    no_adequate_method_conditions: 'primarily: correlated multi-LLM errors + differential
959	      K≥5 + collider/front-door topology'
960	    failure_cases: 21/432 — 14 cases where MLA and PPI are within 0.005 of each other
961	      (recommendation arbitrary), 7 cases where extreme C + small N makes all methods
962	      unstable
963	    empirical_validation_plan003: 8/9 empirical scenarios — recommended method produces
964	      bias reduction ≥40% vs uncorrected
965	    empirical_failure: '1/9 — protest × collider × Qwen: no method adequate (flagged
966	      correctly as ''no adequate method'')'
967	  result_rationale: '95% accuracy（411/432）：决策框架基于理论偏倚表达式的 closed-form 分析， 在每个 {topology
968	    × C structure} cell 中选择使残差偏倚最小化的方法。 14 个"失败"case 实际上是 MLA 和 PPI 表现几乎相同（差异 < 0.005）的场景——
969	    框架推荐了其中一个，但另一个同样好。这不是真正的失败，只是不确定性。 7 个真正失败的 case 出现在极端 C（near-permutation）+ 小样本（N=1000）下，
970	    所有方法都不稳定——这种场景下正确答案可能是"收集更多数据"而非选择方法。
971	
972	    Method distribution：MLA（31%）最常被推荐因为它直接利用 C 矩阵做 deconvolution， 在 C 已知时通常最优。PPI（24%）在
973	    C 有不确定性时被推荐（利用少量 gold-standard 数据 做 prediction-powered inference）。DSL（18%）在 confounding
974	    topology +  high diagonal dominance C 下被推荐（double sampling + likelihood correction）。
975	    Naive plug-in（12%）仅在 ASV > 5.0（结论非常稳健）时被推荐——此时 correction  的 variance cost 大于
976	    bias reduction benefit。
977	
978	    15% "no adequate method"：这些场景主要涉及 correlated multi-LLM errors +  differential
979	    K≥5 + collider/front-door topology。这是论文 Claim 3 的一部分—— 识别现有方法不足的区域并标记为 open problems。其中
980	    dependence-aware multi-LLM  correction 是最重要的 open problem（回应 Kim et al. ICML 2025）。
981	
982	    Empirical 8/9：1 个"failure"实际上是框架正确标记为"no adequate method" （protest × collider
983	    × Qwen，C 接近 near-permutation + 模型间误差高度相关）。 这是一个 success case of honest scoping，而非真正失败。
984	
985	    '
986	  tables:
987	  - name: 'Table 13: Correction Method Recommendation Distribution'
988	    columns:
989	    - Method
990	    - '% Scenarios'
991	    - Typical Condition
992	    - Avg Bias Reduction
993	    rows:
994	    - - MLA
995	      - 31%
996	      - C known, K≤5, non-differential
997	      - 72%
998	    - - PPI
999	      - 24%
1000	      - C uncertain, gold-standard available
1001	      - 65%
1002	    - - DSL
1003	      - 18%
1004	      - Confounding topology, high diag. dominance
1005	      - 58%
1006	    - - Naive plug-in
1007	      - 12%
1008	      - ASV > 5.0 (robust conclusions)
1009	      - N/A (unnecessary)
1010	    - - No adequate method
1011	      - 15%
1012	      - Correlated errors + differential + collider/front-door
1013	      - N/A
1014	  - name: 'Table 14: Framework Accuracy by Topology'
1015	    columns:
1016	    - Topology
1017	    - Scenarios
1018	    - Correct
1019	    - Accuracy
1020	    - Most Common Failure Mode
1021	    rows:
1022	    - - Confounding
1023	      - '72'
1024	      - '71'
1025	      - 98.6%
1026	      - MLA ≈ PPI (indistinguishable)
1027	    - - Mediation
1028	      - '72'
1029	      - '69'
1030	      - 95.8%
1031	      - Extreme C + small N
1032	    - - Collider
1033	      - '72'
1034	      - '67'
1035	      - 93.1%
1036	      - MLA ≈ PPI + extreme C
1037	    - - M-bias
1038	      - '72'
1039	      - '70'
1040	      - 97.2%
1041	      - Rare edge case
1042	    - - Instrument
1043	      - '72'
1044	      - '69'
1045	      - 95.8%
1046	      - Wald ratio instability
1047	    - - Front-door
1048	      - '72'
1049	      - '65'
1050	      - 90.3%
1051	      - Two-stage estimation complexity
1052	  figures_description:
1053	  - 'Fig 17: Decision tree visualization——研究者输入 {topology, C estimate, ASV}，沿路径得到推荐方法
1054	    + 置信度。'
1055	  - 'Fig 18: Empirical bias before vs after correction，per scenario。9 个点，8 个在 ''improvement''
1056	    区域，1 个在 ''no method'' 区域（correctly flagged）。'
1057	  analysis: '95% 准确率表明基于理论的决策框架在实践中可靠。最重要的发现不是哪个方法最好， 而是 "方法选择是拓扑依赖的"——在 confounding
1058	    DAG 中最优的方法在 collider DAG 中 可能增加偏倚。这直接回应了 Jerzak et al. (EMNLP 2025) 的 unconditional
1059	    benchmarking  方法论：如果不考虑拓扑，benchmarking 本身就是误导性的。 15% "no adequate method" 区域是诚实的
1060	    open problem identification， 为后续方法论研究提供了明确方向。
1061	
1062	    '
1063	- name: Pathological confusion matrix analysis
1064	  plan_id: plan_009
1065	  description: '分析极端 C 结构（near-permutation, rank-deficient, block-diagonal）在所有拓扑中的
1066	    偏倚行为。识别预测偏倚严重度的结构性指标（spectral gap, diagonal dominance ratio）。
1067	
1068	    '
1069	  expected_results:
1070	    spectral_gap_bias_correlation: 0.91
1071	    diagonal_dominance_bias_correlation: 0.87
1072	    best_predictor: spectral gap (1 - λ₂/λ₁) explains 83% of bias magnitude variance
1073	    catastrophic_bias_threshold: spectral gap < 0.15 → bias > 2x effect size in ≥80%
1074	      of reversal-prone topologies
1075	    near_permutation_analysis: all near-permutation C (spectral gap < 0.05) produce
1076	      reversal in mediation/collider/front-door; severity 1.5-3x
1077	    rank_deficient_analysis: rank-deficient C always produce catastrophic bias regardless
1078	      of topology — information loss is complete for collapsed dimensions
1079	    block_diagonal_analysis: bias depends on which classes are in same block — if
1080	      classes with opposite effects are merged, reversal guaranteed
1081	    practitioner_diagnostic: 'two-number summary: (spectral gap, diagonal dominance
1082	      ratio) → risk category (low/medium/high/catastrophic)'
1083	  result_rationale: 'Spectral gap 与偏倚强相关（r=0.91）：混淆矩阵 C 的第二大特征值 λ₂ 控制了 "主误分类模式"的强度。当
1084	    spectral gap = 1-λ₂/λ₁ 接近 0 时，C 接近非满秩， 信息丢失严重，偏倚灾难性。这不是偶然——偏倚表达式中 C 的逆（或伪逆）出现在
1085	    correction 中，spectral gap 控制了逆的条件数。
1086	
1087	    Diagonal dominance 相关性略低（0.87 vs 0.91）因为 diagonal dominance  是一个粗糙的指标——它只看对角元素与行和的比值，不捕获
1088	    off-diagonal 的结构 （如 block-diagonal 的特殊性）。Spectral gap 通过特征分解捕获了完整的  off-diagonal
1089	    结构信息。
1090	
1091	    Near-permutation 全部产生反转（在反转敏感拓扑中）：near-permutation C  等价于类别标签几乎完全互换，这在 K≥3 时结构性地翻转效应方向（而
1092	    K=2 时 近置换 = 高误分类率，仍然只 attenuate toward null）。
1093	
1094	    Block-diagonal 的方向依赖于块结构：如果具有相反效应的类别被合并在同一块中， 块内平均化可以翻转块的净效应方向。这与 binarization
1095	    collapse 的机制相同， 但发生在 C 矩阵内部而非研究者的显式折叠中。
1096	
1097	    '
1098	  tables:
1099	  - name: 'Table 15: Structural Predictors of Bias Severity'
1100	    columns:
1101	    - Predictor
1102	    - Correlation with |Bias|
1103	    - R² (univariate)
1104	    - Threshold for Catastrophic Bias
1105	    rows:
1106	    - - Spectral gap (1-λ₂/λ₁)
1107	      - '-0.91'
1108	      - '0.83'
1109	      - < 0.15
1110	    - - Diagonal dominance ratio
1111	      - '-0.87'
1112	      - '0.76'
1113	      - < 0.55
1114	    - - Condition number of C
1115	      - '0.89'
1116	      - '0.79'
1117	      - '> 12'
1118	    - - Min diagonal element
1119	      - '-0.84'
1120	      - '0.71'
1121	      - < 0.3
1122	    - - Spectral gap + diag. dom. (joint)
1123	      - —
1124	      - '0.89'
1125	      - Combined threshold
1126	  figures_description:
1127	  - 'Fig 19: Spectral gap vs bias magnitude scatter，color by topology。Reversal-prone
1128	    topologies（mediation/collider/front-door）的红色点集中在低 spectral gap 区域。'
1129	  - 'Fig 20: Practitioner risk map——x=spectral gap, y=diagonal dominance, zones colored
1130	    by risk level。研究者可将自己的 C 矩阵定位到此图上。'
1131	  analysis: '为实践者提供了两个可操作的诊断数字：spectral gap 和 diagonal dominance ratio。 研究者无需理解完整的偏倚理论，只需计算其实证
1132	    C 矩阵的这两个指标， 即可判断偏倚风险等级。这补充了 ASV 框架——ASV 告诉你"结论多稳健"， 而 spectral diagnostics 告诉你"为什么不稳健"和"C
1133	    的哪个方面最危险"。 Catastrophic threshold（spectral gap < 0.15）在 plan_003 的实证数据中 对应 Qwen
1134	    在 protest coding 某些 prompt 变体下的 C 矩阵——与 ASV < 1.0  的 fragile classification 完全一致。
1135	
1136	    '
1137	- name: annot-sensitivity Python toolkit
1138	  plan_id: plan_010
1139	  description: '开源 Python 包：用户输入 DAG + confusion matrix + downstream estimate → 输出
1140	    bias expressions + ASV bounds + sensitivity curves + correction recommendation
1141	    + diagnostic plots。 pip-installable，含每个拓扑的 worked examples。
1142	
1143	    '
1144	  expected_results:
1145	    package_name: annot-sensitivity
1146	    pip_installable: true
1147	    supported_topologies: 6
1148	    supported_K_range: 2-20
1149	    api_surface: '3 main functions: bias_expression(), asv_bound(), recommend_correction()'
1150	    documentation: 6 topology-specific tutorials (Jupyter notebooks), API reference,
1151	      quickstart guide
1152	    test_coverage: '>90%'
1153	    benchmark: bias_expression() < 0.1s for K≤7; asv_bound() < 1s for K≤7; recommend_correction()
1154	      < 0.5s
1155	    dependencies: numpy, scipy, matplotlib (minimal)
1156	    worked_examples: 6
1157	  result_rationale: 'Toolkit 是论文影响力的关键放大器。学术论文的理论贡献如果没有可用工具， 很难被实践者采纳。三个主函数对应论文三个
1158	    claims：bias_expression() → Claim 1（taxonomy）， asv_bound() → Claim 2（ASV），recommend_correction()
1159	    → Claim 3（correction guidance）。
1160	
1161	    K 支持范围 2-20：K=2 作为 consistency check（应恢复经典二分类结果）， K>7 用矩阵表达式 + 特征分解可解释性工具。K>20
1162	    实际中极罕见且计算成本高 （C 矩阵有 K(K-1) 自由参数），故限定上界。
1163	
1164	    性能目标（< 1s for K≤7）：bias_expression 和 recommend_correction 是闭式计算， 主要耗时在矩阵运算。asv_bound
1165	    涉及优化问题（构造性紧性需要求解约束优化）， K≤7 时维度足够低，SQP 在 1s 内收敛。
1166	
1167	    最小依赖（numpy, scipy, matplotlib）：降低安装门槛，compatible with  任何 Python 科学计算环境。不依赖 PyTorch/TensorFlow
1168	    因为所有计算是 解析数学而非机器学习。
1169	
1170	    '
1171	  tables: []
1172	  figures_description:
1173	  - 'Fig 21 (不在论文中，在 toolkit README): 示例输出截图——bias sensitivity curve + ASV gauge +
1174	    correction recommendation 的组合 dashboard。'
1175	  analysis: Toolkit 的设计哲学是"一个函数回答一个问题"。研究者的典型 workflow： (1) 收集 gold-standard 子集 →
1176	    估计 C；(2) 调用 bias_expression(dag, C, K) →  了解偏倚结构；(3) 调用 asv_bound(dag, C, estimate,
1177	    threshold) → 了解结论稳健性； (4) 调用 recommend_correction(dag, C, asv, n_gold) → 选择校正方法。
1178	    开源发布对 AAAI/ARR 审稿均加分——artifact evaluation 是近年趋势。
1179	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6e95c3a-08a8-43c1-b38e-2087b45fcac3",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "268f490c-acf5-436b-ad39-d843ee0f5257",
  "sourceToolAssistantUUID": "f6e95c3a-08a8-43c1-b38e-2087b45fcac3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T08:57:49.803Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KrgNC5YKYoiBhVkaiFrUfc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "268f490c-acf5-436b-ad39-d843ee0f5257",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYVk9zHpFJtzguLJHsg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "349aa139-658e-499e-b7c2-da7830a76efa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAQpYZ5q2WNGGHM9HU24CE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5552,
      "cache_read_input_tokens": 50834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5552,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 43 · 2026-05-20T08:57:50.066Z_

<details><summary>↩ Tool result · `toolu_01KrgNC5YKYoiBhVkaiFrUfc`</summary>

```text
1	narrative_guidance: 'Version A 成立但 scope 收窄至 2 个反转拓扑：exposure（MVP 已确认，violation rate
2	  85%）+ mediation（plan_001 新发现，violation rate 23%，条件性反转——仅在 off-diagonal dominance
3	  > 0.6 且 |indirect effect| > 0.2 时触发）。
4	
5	  其余 4 个拓扑（confounding, collider, M-bias, instrument, front-door）保持单调性，但 magnitude
6	  变异显著（如 collider bias range 0.04–0.21）。
7	
8	  Lead finding 聚焦于 exposure vs mediation 的对比：exposure 反转是"广泛性的"（85%，几乎所有非对角 C），mediation
9	  反转是"条件性的"（23%，需要双重门控）。这一对比本身就是核心贡献——同样的 non-differential error 在不同拓扑下产生质变差异。
10	
11	  Claim 1 调整：taxonomy 有效，但方向反转是 topology-specific 而非 universal；magnitude 不可预测性作为补充论据（所有
12	  6 个拓扑均存在）。
13	
14	  Claim 2 调整：ASV 紧性降级为 2 个拓扑有形式化证明（confounding + mediation）+ 4 个有 MC 数值证据；增加一段讨论 collider
15	  conditioning structure 导致优化非凸的技术障碍。
16	
17	  Claim 3 不变。
18	
19	  需补充实验：(1) 对 exposure 和 mediation 做 C structure 条件分析（反转边界的精确刻画——何时反转、何时不反转），(2) 增加
20	  1 个经验任务（如 emotion detection K=6）以补偿理论覆盖面的缩窄，使经验证据更丰富。
21	
22	  '
23	imagined_experiments:
24	- name: K=3 Bias Expressions and MC Validation Across 6 DAG Topologies
25	  plan_id: plan_001
26	  description: '对 6 个 DAG 拓扑（confounding, mediation, collider, M-bias, instrument,
27	    front-door）推导 K=3 closed-form bias 表达式，
28	
29	    MC 验证：1000 reps × N=10000 × 6 confusion matrix structures/topology = 36 scenarios。
30	
31	    每个拓扑做 100k random C search 检测方向反转。Confounding 为 MVP 再验证；其余 5 个为新推导。
32	
33	    结合 MVP exposure 结果，total reversal topologies = 2。
34	
35	    '
36	  expected_results:
37	    total_scenarios: 36
38	    theory_mc_match: 33/36
39	    theory_mc_match_rate: 0.917
40	    reversal_in_plan_001: 1
41	    reversal_topology_new: mediation
42	    combined_reversal_topologies: 2
43	    combined_reversal_list:
44	    - exposure (MVP)
45	    - mediation (new)
46	    confounding:
47	      violation_rate: 0.0
48	      bias_range:
49	      - 0.132
50	      - 0.298
51	      theory_mc: 6/6
52	      mechanism: residual confounding, monotonic toward OVB
53	    mediation:
54	      violation_rate: 0.23
55	      sign_reversal_rate: 0.18
56	      amplification_rate: 0.05
57	      worst_severity: 1.62
58	      named_structures_with_violation: 2/6 (near-permutation, block-off-diagonal)
59	      theory_mc: 6/6
60	      reversal_condition: off-diagonal dominance > 0.6 AND |indirect effect| > 0.2
61	      indirect_bias_range:
62	      - -0.18
63	      - 0.14
64	    collider:
65	      violation_rate: 0.0
66	      bias_range:
67	      - 0.04
68	      - 0.21
69	      attenuation_range: 15-60% reduction vs no misclassification
70	      theory_mc: 5/6
71	      mechanism: misclassification smooths conditioning variable, reduces collider
72	        bias magnitude, preserves direction
73	    mbias:
74	      violation_rate: 0.0
75	      bias_range:
76	      - 0.02
77	      - 0.16
78	      theory_mc: 5/6
79	      mechanism: spurious pathway weakened by misclassification of M-bias variable
80	    instrument:
81	      violation_rate: 0.0
82	      bias_range:
83	      - 0.03
84	      - 0.19
85	      theory_mc: 6/6
86	      mechanism: instrument weakened, Wald estimator biased toward OLS, direction
87	        preserved
88	    frontdoor:
89	      violation_rate: 0.0
90	      bias_range:
91	      - 0.05
92	      - 0.22
93	      theory_mc: 5/6
94	      mechanism: front-door estimate attenuated, identification weakened but direction
95	        stable
96	    mc_mismatch_detail: 3 mismatches in collider(1), M-bias(1), front-door(1) — all
97	      near-permutation C where MC variance is highest due to complex bias formulas
98	      (conditioning, ratio estimators)
99	  result_rationale: 'Mediation（23% violation）：misclassifying mediator M 影响间接路径 X→M→Y。反转需要双重门控：
100	
101	    (a) C matrix off-diagonal dominance > 0.6（标签大幅置换），AND (b) |true indirect effect|
102	    > 0.2（间接效应足够大可以被反转）。
103	
104	    因为间接效应 = X→M 系数 × M→Y 系数的乘积，两条路径都必须被实质性扰动才能反转——这种双重门控将 violation rate 限制在 23%。
105	
106	    对比 exposure（MVP 85% violation）：exposure misclassification 直接作用于单一 X→Y 路径，无衰减机制，几乎所有非对角
107	    C 都触发反转。
108	
109	    这一机制差异（直接路径 vs 乘积路径）是 median 档的核心发现——direction reversal 是 topology-specific 的。
110	
111	
112	    Collider（0% violation）：misclassifying Z（collider）并 conditioning on Z* 时，误分类平滑了
113	    Z 的分布，
114	
115	    削弱了 selection effect 的强度但不改变其方向。方向由结构方程的符号决定（与测量质量无关）。
116	
117	    100k random C 中无一例外。
118	
119	
120	    M-bias/Instrument/Front-door（0% violation）：这些拓扑涉及辅助变量，misclassification 削弱 identification
121	    但不反转估计方向。
122	
123	    Instrument 特殊之处在于 Wald estimator 的分母受影响（偏向 OLS），但符号不变。
124	
125	    Front-door 的 double summation 使 MC 方差在极端 C 下偏高，导致 1/6 mismatch。
126	
127	
128	    3 个 MC mismatch 均出现在 near-permutation C structure 下——这些拓扑的 bias formula 含有 conditioning
129	    或 ratio 结构，
130	
131	    MC 在极端 C 下方差更大，理论值落在 95% CI 边缘外。
132	
133	    '
134	  tables:
135	  - name: Direction Reversal Summary by Topology (plan_001 + MVP exposure)
136	    columns:
137	    - topology
138	    - misclassified_var
139	    - violation_rate
140	    - sign_reversal
141	    - worst_severity
142	    - theory_mc
143	    - direction
144	    rows:
145	    - - exposure (MVP)
146	      - treatment X
147	      - 0.85
148	      - 0.834
149	      - 2.83
150	      - 5/5
151	      - reversal-dominant
152	    - - confounding
153	      - confounder U
154	      - 0.0
155	      - 0.0
156	      - 1.00×OVB
157	      - 6/6
158	      - monotonic toward OVB
159	    - - mediation
160	      - mediator M
161	      - 0.23
162	      - 0.18
163	      - 1.62
164	      - 6/6
165	      - conditional reversal
166	    - - collider
167	      - collider Z
168	      - 0.0
169	      - 0.0
170	      - 0.85×(attenuated)
171	      - 5/6
172	      - monotonic attenuation
173	    - - M-bias
174	      - M-bias var
175	      - 0.0
176	      - 0.0
177	      - 0.92×(attenuated)
178	      - 5/6
179	      - monotonic attenuation
180	    - - instrument
181	      - instrument Z
182	      - 0.0
183	      - 0.0
184	      - 0.78×(toward OLS)
185	      - 6/6
186	      - monotonic toward OLS
187	    - - front-door
188	      - front-door M
189	      - 0.0
190	      - 0.0
191	      - 0.88×(attenuated)
192	      - 5/6
193	      - monotonic attenuation
194	  - name: Mediation Reversal Conditions (100k Random C, K=3)
195	    columns:
196	    - C_structure_category
197	    - pct_of_random_C
198	    - violation_rate
199	    - sign_reversal_rate
200	    rows:
201	    - - near-permutation (off-diag dom > 0.6)
202	      - 30%
203	      - 0.57
204	      - 0.44
205	    - - moderate (off-diag dom 0.3–0.6)
206	      - 40%
207	      - 0.14
208	      - 0.09
209	    - - diagonal-dominant (off-diag dom < 0.3)
210	      - 30%
211	      - 0.0
212	      - 0.0
213	    - - overall
214	      - 100%
215	      - 0.23
216	      - 0.18
217	  figures_description:
218	  - 'Fig 1: Heatmap — topology (rows) × named C structure (cols) → bias magnitude
219	    (color intensity) and direction (red=reversal, blue=toward-null). Exposure 行几乎全红，mediation
220	    行 2/6 红，其余行全蓝。'
221	  - 'Fig 2: Violin plots — 100k random C 下各 topology 的 bias 分布。Exposure 为跨零的宽双峰分布；mediation
222	    右偏但有负值尾部；其余单峰正值。'
223	  - 'Fig 3: Mediation 反转 phase diagram — off-diagonal dominance (x) × |indirect effect|
224	    (y) → reversal probability (color). 在 dominance > 0.6、|indirect| > 0.2 处有清晰边界。'
225	  analysis: 'plan_001 确认 median 档的核心结果：6 个拓扑中仅 mediation 出现新的反转（结合 MVP exposure =
226	    2 个反转拓扑）。
227	
228	    关键发现是反转机制的不对称性：exposure 是"广泛性反转"（label swap 直接作用于 treatment 对比），
229	
230	    mediation 是"条件性反转"（需双重门控：C 足够非对角 + 间接效应足够大）。
231	
232	    这一不对称性本身就是论文的核心贡献——它证明了 direction reversal 是 topology-specific 的，
233	
234	    不能仅从 confusion matrix 结构预测，必须结合 DAG 拓扑分析。
235	
236	    4 个单调拓扑的 magnitude 变异（如 collider 0.04–0.21）支持补充论据：即使方向保持，
237	
238	    bias magnitude 仍不可从 binary 框架预测。
239	
240	    需要补充实验：对 mediation 的 phase diagram 做更精细的 grid search（Fig 3 的分辨率不够用于实用指导）。
241	
242	    '
243	- name: General-K Matrix Bias Expressions and Interpretability Tools
244	  plan_id: plan_002
245	  description: '将 bias 表达式扩展到 K=5,7 的矩阵形式。开发 3 个可解释性工具：
246	
247	    (a) eigendecomposition summaries，(b) worst-case scalar bounds，(c) diagnostic visualizations。
248	
249	    在 confounding + mediation + collider + exposure DAGs 上验证 K=5,7。
250	
251	    '
252	  expected_results:
253	    K5_theory_mc_match_rate: 0.89
254	    K7_theory_mc_match_rate: 0.85
255	    K5_scenarios_tested: 24
256	    K7_scenarios_tested: 24
257	    eigendecomp_variance_explained_top2_K5:
258	      confounding: 0.87
259	      exposure: 0.91
260	      mediation: 0.83
261	      collider: 0.88
262	    eigendecomp_variance_explained_top3_K7:
263	      confounding: 0.84
264	      exposure: 0.88
265	      mediation: 0.8
266	      collider: 0.85
267	    worst_case_bound_conservatism_median: 2.6×
268	    worst_case_bound_conservatism_range: 2.1–3.4×
269	    K5_exposure_violation_rate: 0.88
270	    K5_mediation_violation_rate: 0.28
271	    K7_exposure_violation_rate: 0.9
272	    K7_mediation_violation_rate: 0.31
273	    reversal_pattern_persistence: true
274	    dominant_eigenmode_interpretation:
275	      mode_1: diagonal dominance deviation (how far C is from identity)
276	      mode_2: permutation component (which off-diagonal entries dominate)
277	  result_rationale: 'K=5,7 的 match rate 低于 K=3（0.89/0.85 vs 0.917）因为 MC 方差随 C 的自由参数数
278	    K(K-1) 增长——K=5 有 20 个自由参数，K=7 有 42 个，
279	
280	    相同 MC replications 下 confidence interval 更宽。
281	
282	
283	    Eigendecomposition 的 top 2 modes 能解释 83–91% 方差，因为实际 confusion matrix 具有低有效秩结构：
284	
285	    主导误差模式是"相邻类别混淆"（语义相似的类别被混淆），产生带对角扰动结构，被 2–3 个 eigenmodes 良好捕获。
286	
287	    Mediation 的方差解释率略低（0.83 K=5）因为间接效应涉及乘积，放大了二阶 eigenmode 的贡献。
288	
289	
290	    Worst-case bounds 保守（median 2.6×）因为它们对给定 diagonal dominance 下所有 C 做极值优化，
291	
292	    包括实际罕见的对抗性配置。作为安全边界是可接受的——类似 E-values 的保守性。
293	
294	
295	    Violation rates 随 K 轻微上升（mediation 23% → 28% → 31%）因为更大的 K 增加了 off-diagonal confusion
296	    路径，
297	
298	    使 label permutation 更可能。Exposure 接近饱和（85% → 88% → 90%）。
299	
300	    '
301	  tables:
302	  - name: 'Eigendecomposition: Variance Explained by Top Modes'
303	    columns:
304	    - topology
305	    - K
306	    - mode_1
307	    - mode_2
308	    - mode_3
309	    - cumulative_top2
310	    - cumulative_top3
311	    rows:
312	    - - confounding
313	      - 5
314	      - 0.68
315	      - 0.19
316	      - 0.08
317	      - 0.87
318	      - 0.95
319	    - - confounding
320	      - 7
321	      - 0.59
322	      - 0.17
323	      - 0.08
324	      - 0.76
325	      - 0.84
326	    - - exposure
327	      - 5
328	      - 0.74
329	      - 0.17
330	      - 0.05
331	      - 0.91
332	      - 0.96
333	    - - exposure
334	      - 7
335	      - 0.65
336	      - 0.15
337	      - 0.08
338	      - 0.8
339	      - 0.88
340	    - - mediation
341	      - 5
342	      - 0.61
343	      - 0.22
344	      - 0.09
345	      - 0.83
346	      - 0.92
347	    - - mediation
348	      - 7
349	      - 0.52
350	      - 0.19
351	      - 0.09
352	      - 0.71
353	      - 0.8
354	    - - collider
355	      - 5
356	      - 0.7
357	      - 0.18
358	      - 0.06
359	      - 0.88
360	      - 0.94
361	    - - collider
362	      - 7
363	      - 0.62
364	      - 0.16
365	      - 0.07
366	      - 0.78
367	      - 0.85
368	  - name: Violation Rate Scaling with K
369	    columns:
370	    - topology
371	    - K=3
372	    - K=5
373	    - K=7
374	    - trend
375	    rows:
376	    - - exposure
377	      - 0.85
378	      - 0.88
379	      - 0.9
380	      - near saturation
381	    - - mediation
382	      - 0.23
383	      - 0.28
384	      - 0.31
385	      - monotonic increase
386	    - - confounding
387	      - 0.0
388	      - 0.0
389	      - 0.0
390	      - flat (monotonic)
391	    - - collider
392	      - 0.0
393	      - 0.0
394	      - 0.0
395	      - flat (monotonic)
396	  figures_description:
397	  - 'Fig 5: Eigenspectrum bar charts — eigenvalue magnitude by mode index，各 topology
398	    at K=3,5,7。快速衰减，elbow 在 mode 2 (K=3,5) 或 mode 3 (K=7)。'
399	  - 'Fig 6: Bias magnitude scaling — K on x-axis，mean + 95th percentile bias on y-axis，一条线/topology。Exposure/mediation
400	    单调增长，其余平缓。'
401	  - 'Fig 7: Diagnostic heatmap — 5×5 C 的 diagonal dominance vs largest off-diagonal
402	    映射到预测 bias 量级。toolkit 交互版。'
403	  analysis: 'Matrix-form 表达式成功泛化 K=3 结果。实用发现：top 2 eigenmodes 在 K≤5 下足够（>83% 方差解释），
404	
405	    K=7 可能需要 3 个 modes。这指导 toolkit 设计——默认 2-mode summary 加可选扩展。
406	
407	    Reversal patterns 在 K=5,7 持续，确认 K=3 理论分析不是 special case。
408	
409	    Worst-case bounds 的保守性（2.6×）是 tradeoff：tight bounds 需要 topology-specific 优化（随
410	    K 扩展性差），
411	
412	    conservative bounds 计算快且作为安全边界仍有实用价值。
413	
414	    '
415	- name: 'Empirical Confusion Matrices: 3 LLMs × 3 CSS Tasks'
416	  plan_id: plan_003
417	  description: '从 Llama 4 Maverick, Qwen 3.5 Plus, DeepSeek V4 收集经验 confusion matrices。
418	
419	    3 个 CSS 任务：protest event coding (K=5, ACLED), stance detection (K=3, SemEval/VAST),
420	    toxicity (K=2, Civil Comments)。
421	
422	    ~30K annotations/model × 3 tasks × 3 prompt variants = ~270K total annotations。
423	
424	    '
425	  expected_results:
426	    api_cost_actual: $420
427	    total_annotations: 270000
428	    protest_K5:
429	      llama4_macro_f1: 0.71
430	      llama4_accuracy: 0.74
431	      qwen35_macro_f1: 0.68
432	      qwen35_accuracy: 0.71
433	      deepseek_macro_f1: 0.73
434	      deepseek_accuracy: 0.76
435	      inter_model_error_agreement: 0.58
436	      downstream_bias_range_abs:
437	      - 0.05
438	      - 0.12
439	      dominant_error_pattern: adjacent-category confusion (riot↔protest, strategic↔organized)
440	    stance_K3:
441	      llama4_macro_f1: 0.76
442	      llama4_accuracy: 0.79
443	      qwen35_macro_f1: 0.74
444	      qwen35_accuracy: 0.77
445	      deepseek_macro_f1: 0.78
446	      deepseek_accuracy: 0.81
447	      inter_model_error_agreement: 0.62
448	      downstream_bias_range_abs:
449	      - 0.03
450	      - 0.08
451	      dominant_error_pattern: neutral-as-default bias (favor→neutral, against→neutral)
452	    toxicity_K2:
453	      llama4_f1: 0.88
454	      llama4_accuracy: 0.9
455	      qwen35_f1: 0.86
456	      qwen35_accuracy: 0.88
457	      deepseek_f1: 0.89
458	      deepseek_accuracy: 0.91
459	      inter_model_error_agreement: 0.64
460	      downstream_bias_range_abs:
461	      - 0.01
462	      - 0.04
463	      dominant_error_pattern: slight FN bias (under-flagging toxicity)
464	    prompt_variant_stability: macro-F1 varies ±0.03; confusion matrix structure stable
465	      across prompts
466	    cross_model_error_correlation_mean: 0.61
467	  result_rationale: '性能水平反映 2025–2026 LLMs 在 CSS 任务上的典型表现：K=5 protest coding 最难（事件类型间区分微妙），
468	
469	    K=3 stance 中等（neutral 类别歧义性高），K=2 toxicity 最易（信号明确）。
470	
471	
472	    Inter-model error agreement（0.58–0.64）与 Kim et al.（ICML 2025）报告的 ~60% 一致。
473	
474	    Toxicity 略高因为 binary task 出错方式更少。
475	
476	    这验证了论文的动机前提：LLM errors are correlated，ensemble averaging 效果有限。
477	
478	
479	    Downstream bias 范围是中等的（非 dramatic）因为真实 LLM confusion matrices 是 moderately diagonal-dominant
480	    的——
481	
482	    不是 near-permutation 极端。这是 median 档的预期：理论极端（near-permutation C 导致 2.83× severity）
483	
484	    在当前 LLMs 中不会实际出现，但 bias 是可检测的且非 trivial 的。
485	
486	
487	    Prompt variant 稳定性（±0.03 F1，C structure stable）支持论文聚焦于 confusion matrix structure
488	    而非 prompt engineering——
489	
490	    error 的结构模式对 prompting 鲁棒，即使边际性能有移动。
491	
492	    '
493	  tables:
494	  - name: Empirical Performance Summary
495	    columns:
496	    - task
497	    - K
498	    - model
499	    - macro_F1
500	    - accuracy
501	    - dominant_error
502	    rows:
503	    - - protest
504	      - 5
505	      - Llama 4 Maverick
506	      - 0.71
507	      - 0.74
508	      - riot↔protest (0.15)
509	    - - protest
510	      - 5
511	      - Qwen 3.5 Plus
512	      - 0.68
513	      - 0.71
514	      - riot↔protest (0.18), remote↔organized (0.12)
515	    - - protest
516	      - 5
517	      - DeepSeek V4
518	      - 0.73
519	      - 0.76
520	      - riot↔protest (0.13)
521	    - - stance
522	      - 3
523	      - Llama 4 Maverick
524	      - 0.76
525	      - 0.79
526	      - favor→neutral (0.18)
527	    - - stance
528	      - 3
529	      - Qwen 3.5 Plus
530	      - 0.74
531	      - 0.77
532	      - favor→neutral (0.21), against→neutral (0.14)
533	    - - stance
534	      - 3
535	      - DeepSeek V4
536	      - 0.78
537	      - 0.81
538	      - favor→neutral (0.15)
539	    - - toxicity
540	      - 2
541	      - Llama 4 Maverick
542	      - 0.88
543	      - 0.9
544	      - FN toxic→non-toxic (0.12)
545	    - - toxicity
546	      - 2
547	      - Qwen 3.5 Plus
548	      - 0.86
549	      - 0.88
550	      - FN toxic→non-toxic (0.14)
551	    - - toxicity
552	      - 2
553	      - DeepSeek V4
554	      - 0.89
555	      - 0.91
556	      - FN toxic→non-toxic (0.10)
557	  - name: Inter-Model Error Correlation
558	    columns:
559	    - task
560	    - model_pair
561	    - error_agreement_when_both_err
562	    - kappa_on_errors
563	    rows:
564	    - - protest
565	      - Llama4–Qwen35
566	      - 0.56
567	      - 0.31
568	    - - protest
569	      - Llama4–DeepSeek
570	      - 0.61
571	      - 0.38
572	    - - protest
573	      - Qwen35–DeepSeek
574	      - 0.57
575	      - 0.33
576	    - - stance
577	      - Llama4–Qwen35
578	      - 0.6
579	      - 0.35
580	    - - stance
581	      - Llama4–DeepSeek
582	      - 0.64
583	      - 0.41
584	    - - stance
585	      - Qwen35–DeepSeek
586	      - 0.62
587	      - 0.37
588	    - - toxicity
589	      - Llama4–Qwen35
590	      - 0.63
591	      - 0.39
592	    - - toxicity
593	      - Llama4–DeepSeek
594	      - 0.66
595	      - 0.44
596	    - - toxicity
597	      - Qwen35–DeepSeek
598	      - 0.64
599	      - 0.41
600	  figures_description:
601	  - 'Fig 8: Confusion matrix heatmaps — 3×3 grid (models × tasks)，empirical C matrices
602	    with magnitude coloring。Adjacent-category confusion 在 protest K=5 可见，neutral-absorbing
603	    在 stance K=3 可见。'
604	  - 'Fig 9: Inter-model error scatter — per task，scatter of (model_A error, model_B
605	    error) per sample，colored by agreement。显示 correlation clustering。'
606	  - 'Fig 10: Downstream bias bar chart — gold-standard effect vs LLM-annotated effect
607	    for 9 model-task pairs。Bootstrap error bars。Bias 可见但不极端。'
608	  analysis: '经验 confusion matrices 确认真实 LLMs 产生 moderately diagonal-dominant 的 C matrix——
609	
610	    远离 near-permutation 极端但有足够 off-diagonal mass 产生可检测的 downstream bias。
611	
612	    关键经验发现：C structure 是 task-dependent（adjacent-category for protest，neutral-absorbing
613	    for stance）
614	
615	    且 model-stable（同一 task 下 3 个模型展示相似结构模式）。
616	
617	    这意味着理论 taxonomy 的 per-topology 预测适用于真实 LLM 场景——C structure 可从 task 预测，不取决于模型选择。
618	
619	    Inter-model error correlation 直接支持论文 framing：ensembles 无法修复系统性误差。
620	
621	    '
622	- name: Binarization Collapse Analysis Across 6 Topologies
623	  plan_id: plan_008
624	  description: '对 6 个拓扑在 K=3,5,7 下：将 K-class 变量折叠为 binary，
625	
626	    比较 full multi-class bias expression vs binarized expression。
627	
628	    评估何时 binarization 安全、何时危险。
629	
630	    '
631	  expected_results:
632	    max_delta_overall: 0.13
633	    max_delta_by_K:
634	      K3: 0.103
635	      K5: 0.13
636	      K7: 0.13
637	    worst_delta_topology: mediation (K=5)
638	    binarization_direction_reversal_topologies:
639	    - exposure
640	    - mediation
641	    safe_binarization_topologies:
642	    - collider
643	    - M-bias
644	    - instrument
645	    lossy_but_direction_safe:
646	    - confounding
647	    - front-door
648	    delta_by_topology_K3:
649	      confounding: 0.103
650	      mediation: 0.09
651	      collider: 0.07
652	      mbias: 0.06
653	      instrument: 0.05
654	      frontdoor: 0.08
655	    delta_by_topology_K5:
656	      confounding: 0.11
657	      mediation: 0.13
658	      collider: 0.09
659	      mbias: 0.08
660	      instrument: 0.06
661	      frontdoor: 0.09
662	  result_rationale: 'Binarization delta 在 K=5 达到峰值（0.13）并在 K=7 持平，因为 K→2 的信息损失在 K=5–7
663	    饱和——
664	
665	    超过 K=7 后额外类别的边际信息递减。
666	
667	
668	    Mediation 的 delta 最大（K=5 时 0.13）因为 binarizing mediator M 将间接路径折叠为单一对比，
669	
670	    丢失了 multi-class expression 捕获的 category-specific indirect effects。
671	
672	    对 exposure 和 mediation，某些 binarization folding 产生方向反转：
673	
674	    将 category 1+2 vs 3 折叠可能将相反方向的效应分配到同一 binary class。
675	
676	
677	    Confounding delta 高（K=3 0.103，来自 MVP）因为 binarizing confounder 丢失了残差混杂控制。
678	
679	    但方向保持（direction-safe, magnitude-unsafe）。
680	
681	
682	    Collider/M-bias/instrument delta 较小因为这些拓扑涉及辅助变量，
683	
684	    binary 近似更接近 multi-class truth——关键量（induced bias direction）更依赖 conditioning operation
685	    而非变量粒度。
686	
687	    '
688	  tables:
689	  - name: Binarization Delta Summary
690	    columns:
691	    - topology
692	    - K
693	    - max_delta
694	    - direction_reversal_from_binarization
695	    - safety_class
696	    rows:
697	    - - confounding
698	      - 3
699	      - 0.103
700	      - false
701	      - direction-safe, magnitude-unsafe
702	    - - confounding
703	      - 5
704	      - 0.11
705	      - false
706	      - direction-safe, magnitude-unsafe
707	    - - mediation
708	      - 3
709	      - 0.09
710	      - true
711	      - unsafe
712	    - - mediation
713	      - 5
714	      - 0.13
715	      - true
716	      - unsafe
717	    - - exposure (ref)
718	      - 3
719	      - 0.09
720	      - true
721	      - unsafe
722	    - - exposure (ref)
723	      - 5
724	      - 0.1
725	      - true
726	      - unsafe
727	    - - collider
728	      - 3
729	      - 0.07
730	      - false
731	      - safe
732	    - - collider
733	      - 5
734	      - 0.09
735	      - false
736	      - safe
737	    - - M-bias
738	      - 3
739	      - 0.06
740	      - false
741	      - safe
742	    - - instrument
743	      - 3
744	      - 0.05
745	      - false
746	      - safe
747	    - - front-door
748	      - 3
749	      - 0.08
750	      - false
751	      - direction-safe, magnitude-marginal
752	  figures_description:
753	  - 'Fig 11: Delta bar chart — grouped by topology，colored by K。Mediation 为最差 case，monotonic
754	    topologies 偏低。'
755	  - 'Fig 12: Binarization reversal case studies — 2 panels showing K=3 estimate (correct
756	    direction) vs binary estimate (reversed) for exposure and mediation，with specific
757	    C matrix and folding scheme。'
758	  analysis: 'Binarization 不是逃离 K≥3 复杂性的安全手段。Max delta 0.13（mediation K=5）在典型 CSS 回归中
759	
760	    （effect size 0.1–0.5）足以主导估计。
761	
762	    拓扑分三组：(1) binarization-unsafe（exposure, mediation——可能反转方向），
763	
764	    (2) binarization-lossy（confounding, front-door——保持方向但损失量级精度），
765	
766	    (3) binarization-tolerable（collider, M-bias, instrument——delta 小，安全）。
767	
768	    这支持论文的 multi-class treatment is necessary 论点。
769	
770	    '
771	- name: 'ASV Framework: Formal Proofs for Confounding, Mediation, Collider'
772	  plan_id: plan_004
773	  description: '推导 3 个优先拓扑的 ASV 表达式。形式化证明 monotonicity 和 sharpness。
774	
775	    MC 验证：coverage at 90%, 95%, 99% across 1000 scenarios/topology。
776	
777	    '
778	  expected_results:
779	    monotonicity_proved:
780	    - confounding
781	    - mediation
782	    - collider
783	    sharpness_proved:
784	    - confounding
785	    - mediation
786	    sharpness_incomplete:
787	    - collider
788	    sharpness_formal_proofs_count: 2
789	    collider_sharpness_numerical: achieving 93% of bound in 10k optimization runs
790	    coverage_at_95_nominal:
791	      confounding: 0.93
792	      mediation: 0.9
793	      collider: 0.91
794	    coverage_at_90_nominal:
795	      confounding: 0.95
796	      mediation: 0.92
797	      collider: 0.93
798	    coverage_at_99_nominal:
799	      confounding: 0.97
800	      mediation: 0.96
801	      collider: 0.95
802	    average_coverage_95: 0.913
803	  result_rationale: 'Monotonicity 对所有 3 个拓扑成立（proved）因为：更大的 δ 意味着 sensitivity set
804	    中考虑更极端的 C →
805	
806	    overturn conclusion 所需的 minimum perturbation 只能增加或不变。
807	
808	    这与 underlying bias 是否单调无关——ASV 是 min-over-C 量，不是 pointwise bias。
809	
810	
811	    Confounding sharpness：bias 在 C 的 off-diagonal elements 上是线性的，supremum 有 clean
812	    convex structure，
813	
814	    sharpness-achieving C 在 feasible set 的顶点。构造性证明。
815	
816	
817	    Mediation sharpness：尽管存在方向反转，ASV sharpness 仍可证——通过分别分析 attenuation regime 和 reversal
818	    regime。
819	
820	    Reversal boundary 处的 worst-case C 恰好达到 bound——构造性证明利用 phase transition 结构。
821	
822	    这是一个 nice 的结果：有反转的拓扑仍然有 tight bound，加强了 ASV 框架的可信度。
823	
824	
825	    Collider sharpness INCOMPLETE：bias 表达式涉及 conditioning on misclassified Z，
826	
827	    产生 E[Y|X,Z*] = Σ_z P(Z=z|Z*) E[Y|X,Z=z]。
828	
829	    对 C 做 supremum 要求联合优化 P(Z=z|Z*)，subject to C 为 valid confusion matrix，
830	
831	    产生非凸 bilinear 约束。数值优化达到 analytical bound 的 93%，强烈暗示 sharpness，
832	
833	    但形式化证明 supremum is attained 被 feasible set 的非凸拓扑阻断。
834	
835	
836	    Coverage 略低于 nominal（average 91.3% at 95% nominal）因为 ASV bounds 在已知 exact C 下推导，
837	
838	    而 MC 用的是有限样本估计的 C。Gap（3.7%）反映估计不确定性而非 bound failure。
839	
840	    '
841	  tables:
842	  - name: ASV Proof Status and Coverage (Priority Topologies)
843	    columns:
844	    - topology
845	    - monotonicity
846	    - sharpness
847	    - coverage_90
848	    - coverage_95
849	    - coverage_99
850	    rows:
851	    - - confounding
852	      - formal proof
853	      - formal proof
854	      - 0.95
855	      - 0.93
856	      - 0.97
857	    - - mediation
858	      - formal proof
859	      - formal proof
860	      - 0.92
861	      - 0.9
862	      - 0.96
863	    - - collider
864	      - formal proof
865	      - numerical only (93%)
866	      - 0.93
867	      - 0.91
868	      - 0.95
869	  figures_description:
870	  - 'Fig 13: ASV curves — ASV vs δ for 3 topologies，with MC pointwise confidence bands。Monotonicity
871	    直观可见。Mediation 曲线斜率更陡（对 amplification 更敏感）。'
872	  - 'Fig 14: Coverage calibration plots — nominal level (x) vs empirical coverage
873	    (y)。全部略低于对角线（mildly anti-conservative），confounding 最接近校准。'
874	  - 'Fig 15: Sharpness illustration — confounding + mediation 展示 achieving C matrix
875	    + bound value；collider 展示 best numerical C 与 analytical bound 的 gap。'
876	  analysis: 'ASV 框架在 3 个优先拓扑上验证：monotonicity universally proved，sharpness 2/3 proved。
877	
878	    Collider sharpness gap（7%）是主要技术障碍——论文应增加一段讨论 conditioning-on-misclassified-variable
879	    导致的非凸优化问题，
880	
881	    并标记 convex relaxation approach 为 future work。
882	
883	    Mediation 的更陡 ASV 曲线意味着 mediation DAGs 的结论对 annotation error 更敏感——
884	
885	    与 direction reversal 发现一致，自然连接 Claim 1 和 Claim 2。
886	
887	    '
888	- name: ASV MC Validation for M-bias, Instrument, Front-door
889	  plan_id: plan_005
890	  description: '推导剩余 3 个拓扑的 ASV 表达式 + MC 验证。
891	
892	    Monotonicity 和 coverage 验证。Sharpness 作为 conjectures + numerical evidence。
893	
894	    '
895	  expected_results:
896	    monotonicity_holds:
897	    - M-bias
898	    - instrument
899	    - front-door
900	    monotonicity_failures: 0
901	    sharpness_numerical:
902	      mbias: achieving 92% of bound
903	      instrument: achieving 89% of bound
904	      frontdoor: achieving 94% of bound
905	    coverage_at_95_nominal:
906	      mbias: 0.9
907	      instrument: 0.89
908	      frontdoor: 0.91
909	    instrument_conservatism: ASV bounds 1.8× wider than necessary
910	    total_asv_coverage_6_topologies: 0.907
911	  result_rationale: 'Monotonicity 对所有 3 个拓扑成立——与 plan_004 相同的结构性论证：
912	
913	    ASV 是 minimum-over-perturbation 量，在 perturbation budget δ 中固有单调。
914	
915	
916	    Sharpness numerical evidence 有差异：front-door 最接近 tight（94%，identification structure
917	    较简单），
918	
919	    M-bias 中等（92%），instrument 最远（89%）。
920	
921	    Instrument gap 反映 Wald estimator 的 ratio structure——supremum 涉及优化 misclassified
922	    量的 ratio，
923	
924	    landscape 有多个 local optima。
925	
926	
927	    Instrument ASV 显著保守（1.8× wider）因为 Wald estimator 放大小分母扰动，
928	
929	    worst-case bound 比 typical case 差很多。这是 IV sensitivity analysis 的已知问题（非本框架特有）。
930	
931	    '
932	  tables:
933	  - name: ASV Results for Secondary Topologies
934	    columns:
935	    - topology
936	    - monotonicity
937	    - sharpness_numerical_pct
938	    - coverage_95
939	    - conservatism
940	    rows:
941	    - - M-bias
942	      - holds
943	      - 92%
944	      - 0.9
945	      - comparable to collider
946	    - - instrument
947	      - holds
948	      - 89%
949	      - 0.89
950	      - 1.8× conservative (Wald ratio)
951	    - - front-door
952	      - holds
953	      - 94%
954	      - 0.91
955	      - near-tight
956	  - name: All 6 Topologies ASV Summary
957	    columns:
958	    - topology
959	    - monotonicity
960	    - sharpness_status
961	    - coverage_95
962	    rows:
963	    - - confounding
964	      - proved
965	      - proved (formal)
966	      - 0.93
967	    - - mediation
968	      - proved
969	      - proved (formal)
970	      - 0.9
971	    - - collider
972	      - proved
973	      - 93% numerical
974	      - 0.91
975	    - - M-bias
976	      - proved
977	      - 92% numerical
978	      - 0.9
979	    - - instrument
980	      - proved
981	      - 89% numerical
982	      - 0.89
983	    - - front-door
984	      - proved
985	      - 94% numerical
986	      - 0.91
987	  figures_description:
988	  - 'Fig 16: ASV curves for secondary topologies — same format as Fig 13。Instrument
989	    曲线显著更宽（更保守）。'
990	  - 'Fig 17: Sharpness gap comparison — 6 topologies bar chart of (1 − numerical_achievement/bound)。Confounding
991	    + mediation at 0% (proved)，others at 6–11%。'
992	  analysis: '6 个拓扑全部有 ASV 表达式 + validated monotonicity。Sharpness landscape：
993	
994	    2 proved (confounding, mediation) + 4 numerical (collider 93%, front-door 94%,
995	    M-bias 92%, instrument 89%)。
996	
997	    Instrument 是最弱环节——ASV 保守性限制了实用性。论文应诚实讨论并标记 tighter instrument-specific bounds
998	    为 future work。
999	
1000	    Overall average 95%-nominal coverage = 0.907，在 median 档 [0.88, 0.93] 范围内。
1001	
1002	    '
1003	- name: ASV Calibration on Empirical Data
1004	  plan_id: plan_006
1005	  description: '将 ASVs 应用于 plan_003 的经验 confusion matrices，跨 3 CSS tasks × 3 LLMs。
1006	
1007	    在 held-out gold-standard splits 上验证 coverage。
1008	
1009	    比较 ASV 可解释性与 raw confusion matrix reporting。
1010	
1011	    '
1012	  expected_results:
1013	    total_scenarios: 9
1014	    empirical_asv_concordance: 7
1015	    concordance_failures: 2
1016	    failure_scenarios:
1017	    - toxicity-Llama4 vs toxicity-Qwen35
1018	    - toxicity-Qwen35 vs toxicity-DeepSeek
1019	    failure_reason: all 3 models produce high ASVs (>2.0) for toxicity K=2; differences
1020	      within estimation noise
1021	    asv_ranking:
1022	      protest: DeepSeek (0.91) > Llama4 (0.82) > Qwen35 (0.68) — correct
1023	      stance: DeepSeek (1.41) > Llama4 (1.24) > Qwen35 (1.08) — correct
1024	      toxicity: DeepSeek (2.44) ≈ Llama4 (2.31) ≈ Qwen35 (2.18) — indistinguishable
1025	    held_out_coverage_95: 0.89
1026	  result_rationale: 'Concordance 7/9：ASV 在 protest (K=5) 和 stance (K=3) 任务上正确排序模型鲁棒性——
1027	
1028	    这些任务的 confusion matrix 差异足够大，产生有区分力的 ASV 值。
1029	
1030	    Failure 出现在 toxicity (K=2)：所有 3 个模型有 near-diagonal C（accuracy > 0.86），
1031	
1032	    产生高 ASVs (>2.0)，差异在 MC estimation noise 内——无法区分模型。
1033	
1034	
1035	    这是 low-bias regime 的结构性限制：annotation quality 高时（K=2 toxicity），
1036	
1037	    ASVs 正确指示"robust"但不能 rank-order models。
1038	
1039	    这实际上是合适的——如果所有模型产生 negligible bias，ranking 本身就无信息量。
1040	
1041	
1042	    Held-out coverage (0.89 at 95% nominal) 略低于 MC coverage (0.91) 因为 empirical C
1043	    有额外的
1044	
1045	    gold-standard sample size 估计噪声。Gap 小且在预期范围内。
1046	
1047	    '
1048	  tables:
1049	  - name: ASV Values and Concordance by Task × Model
1050	    columns:
1051	    - task
1052	    - model
1053	    - ASV_95
1054	    - observed_abs_bias
1055	    - robust_flag
1056	    - concordant
1057	    rows:
1058	    - - protest
1059	      - Llama 4
1060	      - 0.82
1061	      - 0.09
1062	      - moderate
1063	      - true
1064	    - - protest
1065	      - Qwen 3.5
1066	      - 0.68
1067	      - 0.12
1068	      - fragile
1069	      - true
1070	    - - protest
1071	      - DeepSeek
1072	      - 0.91
1073	      - 0.05
1074	      - moderate-high
1075	      - true
1076	    - - stance
1077	      - Llama 4
1078	      - 1.24
1079	      - 0.06
1080	      - moderate-high
1081	      - true
1082	    - - stance
1083	      - Qwen 3.5
1084	      - 1.08
1085	      - 0.08
1086	      - moderate
1087	      - true
1088	    - - stance
1089	      - DeepSeek
1090	      - 1.41
1091	      - 0.03
1092	      - high
1093	      - true
1094	    - - toxicity
1095	      - Llama 4
1096	      - 2.31
1097	      - 0.02
1098	      - high
1099	      - true
1100	    - - toxicity
1101	      - Qwen 3.5
1102	      - 2.18
1103	      - 0.04
1104	      - high
1105	      - false
1106	    - - toxicity
1107	      - DeepSeek
1108	      - 2.44
1109	      - 0.01
1110	      - high
1111	      - false
1112	  figures_description:
1113	  - 'Fig 18: ASV vs observed absolute bias scatter — 9 scenarios。Protest + stance
1114	    展示 negative correlation；toxicity 聚集在右上角（high ASV, low bias, indistinguishable）。'
1115	  - 'Fig 19: ASV vs raw C matrix comparison — side-by-side 对比 2 个 example scenarios，展示
1116	    ASV 提供 single interpretable number vs 9–25 cell matrix。'
1117	  analysis: 'ASVs 在 moderate-to-high bias scenarios 中具有经验实用性（protest K=5, stance K=3），
1118	
1119	    但在 low-bias regime 失去区分力（toxicity K=2）。这是诚实且预期的——
1120	
1121	    类似 E-values 在 confounding 小时不 informative。
1122	
1123	    论文应 frame 为："ASVs are most valuable when annotation error is non-trivial (K≥3,
1124	    accuracy <0.85)——
1125	
1126	    precisely the scenarios where researchers lack existing diagnostic tools。"
1127	
1128	    7/9 concordance 支持 Claim 2 的实用价值。
1129	
1130	    '
1131	- name: 'Correction Guidance Framework: Decision Mapping and Validation'
1132	  plan_id: plan_007
1133	  description: 'Decision framework: {topology × error structure × ASV} → correction
1134	    method
1135	
1136	    (DSL / PPI / MLA / naive plug-in / "no existing method adequate")。
1137	
1138	    MC validation: 90 scenarios + empirical validation on plan_003 data。
1139	
1140	    '
1141	  expected_results:
1142	    total_mc_scenarios: 90
1143	    correction_framework_accuracy: 0.89
1144	    correct_recommendations: 80
1145	    boundary_indistinguishable_cases: 3
1146	    hard_failure_cases: 7
1147	    failure_breakdown:
1148	      near_diagonal_all_methods_equivalent: 3
1149	      differential_intermediate_mismatch: 2
1150	      false_recommendation_in_hopeless_regime: 2
1151	    method_dominance:
1152	      DSL: best in 28/90 (diagonal-dominant C, confounding/mediation)
1153	      PPI: best in 22/90 (moderate C, exposure/front-door)
1154	      MLA: best in 18/90 (high off-diagonal, confounding/collider)
1155	      naive_plugin: best in 12/90 (near-diagonal, any topology)
1156	      no_method_adequate: 10/90 (near-permutation + reversal topologies)
1157	    empirical_validation_plan003:
1158	      protest_correct: true
1159	      stance_correct: true
1160	      toxicity_correct: true
1161	    open_problems:
1162	    - dependence-aware multi-LLM correction
1163	    - differential K≥3 error correction
1164	    - collider + near-permutation C (no method reduces bias below 50%)
1165	  result_rationale: '89% accuracy 反映框架在 clear-cut scenarios（方法性能明显分离）的优势和 boundary
1166	    cases 的弱点。
1167	
1168	
1169	    3 个 boundary cases 是结构性不可区分的：near-diagonal C（low error）下所有方法结果相近（within 5%），
1170	
1171	    "best" recommendation 是任意的。这不是框架的失败而是问题本身的 degeneracy。
1172	
1173	
1174	    7 个 hard failures：
1175	
1176	    (a) 3 cases: near-diagonal C 使所有方法等效但框架因 threshold effects 选了次优方法；
1177	
1178	    (b) 2 cases: intermediate differential error 处框架的 non-differential/differential
1179	    二分类
1180	
1181	    无法捕获 differentiality 的连续性质；
1182	
1183	    (c) 2 cases: 框架推荐了方法但正确答案是"no method adequate"（near-permutation C + reversal topology）。
1184	
1185	
1186	    Method dominance 是 topology-driven 的：DSL 擅长 confounding（调整 misclassified confounder
1187	    是其 native use case），
1188	
1189	    PPI 擅长 exposure（regression-calibration 处理 treatment misclassification），
1190	
1191	    MLA 擅长 high off-diagonal error（maximum likelihood 直接建模 C）。
1192	
1193	
1194	    10/90 "no method adequate" 集中在 reversal topologies（exposure, mediation）+ extreme
1195	    C——
1196	
1197	    这些是 current correction literature 的真实 gaps。
1198	
1199	    '
1200	  tables:
1201	  - name: Correction Method Dominance Map
1202	    columns:
1203	    - method
1204	    - best_in_n
1205	    - primary_topology
1206	    - primary_error_regime
1207	    rows:
1208	    - - DSL
1209	      - 28
1210	      - confounding, mediation
1211	      - diagonal-dominant C
1212	    - - PPI
1213	      - 22
1214	      - exposure, front-door
1215	      - moderate off-diagonal
1216	    - - MLA
1217	      - 18
1218	      - confounding, collider
1219	      - high off-diagonal
1220	    - - naive plug-in
1221	      - 12
1222	      - any
1223	      - near-diagonal
1224	    - - no method
1225	      - 10
1226	      - exposure, mediation
1227	      - near-permutation
1228	  - name: Framework Failure Analysis
1229	    columns:
1230	    - failure_type
1231	    - count
1232	    - impact
1233	    - mitigation
1234	    rows:
1235	    - - boundary (methods ≤5% apart)
1236	      - 3
1237	      - low
1238	      - any recommendation acceptable
1239	    - - differential mismatch
1240	      - 2
1241	      - moderate
1242	      - add continuous differentiality parameter
1243	    - - false recommendation in hopeless regime
1244	      - 2
1245	      - high
1246	      - 'add safety check: if reversal topology + extreme C → flag'
1247	  figures_description:
1248	  - 'Fig 20: Decision tree / flowchart — {topology, error structure, ASV} → recommended
1249	    method。Color-coded by method，boundary regions highlighted。'
1250	  - 'Fig 21: Method accuracy heatmap — topology (rows) × error structure bins (cols)
1251	    → recommendation accuracy。Diagonal patterns showing topology-method alignment。'
1252	  - 'Fig 22: Open problems map — (off-diagonal mass, differentiality) 2D scatter colored
1253	    by adequate method existence。Gap region in upper-right clearly visible。'
1254	  analysis: 'Correction framework 达到主要目标：89% 正确识别 best correction method。
1255	
1256	    11% failure rate 集中在固有歧义的 boundary cases（3%）和真正困难的 regimes（8%）。
1257	
1258	    2 个"false recommendation in hopeless regime"最令人担忧——框架提供了虚假信心。
1259	
1260	    论文应明确讨论此风险并建议 practitioners 始终在 held-out data 上验证 corrections。
1261	
1262	    10 个"no method adequate"scenarios 是论文对 open problems 的贡献——
1263	
1264	    特别是 dependence-aware multi-LLM correction（结合 plan_003 的 correlation 发现）。
1265	
1266	    '
1267	- name: Pathological Confusion Matrix Analysis
1268	  plan_id: plan_009
1269	  description: '极端 C 结构分析：near-permutation, rank-deficient, block-diagonal。
1270	
1271	    刻画 catastrophic bias 条件并识别结构性预测因子。
1272	
1273	    '
1274	  expected_results:
1275	    spectral_gap_predictive_R2: 0.78
1276	    diagonal_dominance_predictive_R2: 0.71
1277	    combined_predictor_R2: 0.84
1278	    catastrophic_threshold_spectral_gap: 0.3
1279	    catastrophic_threshold_diagonal_dominance: 0.5
1280	    near_permutation_universally_catastrophic: true
1281	    rank_deficient_topology_dependent: true
1282	    rank_deficient_worst:
1283	    - front-door
1284	    - instrument
1285	    block_diagonal_worst: mediation (blocks indirect path)
1286	  result_rationale: 'Spectral gap（C 的第一和第二 eigenvalue 之差）预测 bias severity（R²=0.78）
1287	
1288	    因为它捕获了 C 距 permutation matrix 的距离——反转的结构性来源。
1289	
1290	    R²=0.78 表示强但不完美的预测；剩余方差来自 topology-specific interactions。
1291	
1292	
1293	    Diagonal dominance（minimum diagonal element）是更简单的 proxy，R² 略低（0.71）。
1294	
1295	    Combined spectral gap + diagonal dominance 达到 R²=0.84——两个 features 捕获了大部分 bias-relevant
1296	    C structure。
1297	
1298	
1299	    Near-permutation 普遍 catastrophic 因为 label-swapping 搅乱所有拓扑。
1300	
1301	    Rank-deficient C 是 topology-dependent：front-door 和 instrument 的 identification
1302	    formula
1303	
1304	    含有 C-dependent 分母——C rank-deficient 时分母趋零，bias unbounded。
1305	
1306	    Confounding/mediation/collider 对 rank deficiency 处理更 graceful（无 ratio estimator）。
1307	
1308	
1309	    Block-diagonal C 对 mediation 最 severe——block 结构可以创造 artifact category boundaries
1310	    上的 apparent indirect effects。
1311	
1312	    '
1313	  tables:
1314	  - name: Structural Predictors of Bias Severity
1315	    columns:
1316	    - predictor
1317	    - R2_overall
1318	    - best_topology_R2
1319	    - worst_topology_R2
1320	    rows:
1321	    - - spectral gap
1322	      - 0.78
1323	      - exposure (0.85)
1324	      - M-bias (0.67)
1325	    - - diagonal dominance
1326	      - 0.71
1327	      - confounding (0.82)
1328	      - front-door (0.58)
1329	    - - spectral gap + diag dom
1330	      - 0.84
1331	      - exposure (0.91)
1332	      - instrument (0.74)
1333	  - name: Catastrophic Bias Conditions by Topology and C Structure
1334	    columns:
1335	    - topology
1336	    - near_permutation
1337	    - rank_deficient
1338	    - block_diagonal
1339	    rows:
1340	    - - confounding
1341	      - severe (OVB > 2×)
1342	      - moderate
1343	      - moderate
1344	    - - exposure
1345	      - catastrophic (reversal)
1346	      - severe
1347	      - severe (block reversal)
1348	    - - mediation
1349	      - severe (reversal)
1350	      - moderate
1351	      - severe (block indirect effects)
1352	    - - collider
1353	      - severe (attenuation > 60%)
1354	      - moderate
1355	      - moderate
1356	    - - M-bias
1357	      - moderate
1358	      - moderate
1359	      - mild
1360	    - - instrument
1361	      - moderate
1362	      - catastrophic (Wald denom → 0)
1363	      - moderate
1364	    - - front-door
1365	      - moderate
1366	      - catastrophic (identification loss)
1367	      - moderate
1368	  figures_description:
1369	  - 'Fig 23: Spectral gap vs bias severity scatter — one panel/topology，threshold
1370	    at 0.3 where bias becomes catastrophic。'
1371	  - 'Fig 24: Phase diagram — spectral gap (x) × diagonal dominance (y) → bias regime
1372	    (safe/moderate/catastrophic)。Sharp boundaries visible。'
1373	  - 'Fig 25: Rank deficiency impact — bias magnitude vs effective matrix rank for
1374	    each topology。Front-door + instrument 在 rank 降低时 diverge。'
1375	  analysis: '实用 takeaway：spectral gap < 0.3 OR diagonal dominance < 0.5 → 所有拓扑均高风险。
1376	
1377	    这一双阈值规则足够简单可用且捕获 84% 的 bias variance。
1378	
1379	    Front-door 和 instrument 对 rank-deficient C 特别脆弱（ratio estimator 分母问题）。
1380	
1381	    这些 structural predictors 是 toolkit (plan_010) 的 automatic diagnostic features
1382	    候选。
1383	
1384	    '
1385	- name: annot-sensitivity Python Toolkit
1386	  plan_id: plan_010
1387	  description: 'Open-source pip-installable package：user-specified DAG + confusion
1388	    matrix + downstream estimate
1389	
1390	    → bias expressions + ASV + sensitivity curves + correction recommendation + diagnostic
1391	    plots。
1392	
1393	    '
1394	  expected_results:
1395	    package_name: annot-sensitivity
1396	    supported_topologies: 6
1397	    supported_K_range: 2–10
1398	    core_api:
1399	    - compute_bias(dag, C, estimate) → BiasResult
1400	    - compute_asv(dag, C, estimate, delta_range) → ASVResult
1401	    - recommend_correction(dag, C, asv) → CorrectionRecommendation
1402	    - diagnostic_plot(result) → Figure
1403	    - eigendecomp_summary(C, K) → EigenSummary
1404	    - check_pathological(C) → PathologyReport (spectral gap + diag dom thresholds)
1405	    worked_examples: 3
1406	    example_topologies:
1407	    - confounding (baseline)
1408	    - exposure (reversal)
1409	    - mediation (conditional reversal)
1410	    test_coverage: 0.87
1411	    documentation: API reference + 3 tutorial notebooks + quick-start guide
1412	    known_limitations:
1413	    - K>7 eigendecomposition slow (>10s/computation)
1414	    - correction accuracy inherits plan_007 limitations (89%)
1415	    - CLI + notebook only, no GUI
1416	    - 3/6 topologies lack detailed tutorials (M-bias, instrument, front-door)
1417	  result_rationale: '3 个 worked examples（而非 6）因为 median 档 scope 有限——优先覆盖 3 个 reversal-relevant
1418	    拓扑
1419	
1420	    （confounding 作为 baseline，exposure + mediation 作为反转案例）。剩余 3 个拓扑在 API 中支持但缺少详细 tutorial。
1421	
1422	
1423	    K>7 性能限制反映 eigendecomposition 的 O(K³) 成本——对典型 CSS 使用（K=3–7）可接受，
1424	
1425	    对罕见 high-K 应用偏慢。
1426	
1427	
1428	    Test coverage 0.87 反映核心计算（bias expressions, ASV）的 thorough unit testing
1429	
1430	    和 visualization/correction recommendation 组件的 lighter testing。
1431	
1432	
1433	    check_pathological() 集成 plan_009 的 spectral gap + diagonal dominance 阈值，
1434	
1435	    为 practitioner 提供自动 C matrix 质量诊断。
1436	
1437	    '
1438	  tables: []
1439	  figures_description:
1440	  - 'Fig 26 (toolkit demo): Notebook screenshot — exposure DAG K=3 的完整输出：bias expression,
1441	    ASV curve, correction recommendation, diagnostic plot，in a single cell。'
1442	  analysis: 'Toolkit 是 functional deliverable，使论文的理论贡献对 practitioners 可及。
1443	
1444	    3 个 worked examples 覆盖最重要的场景（reversal cases）。
1445	
1446	    主要 gap：3 个拓扑缺少 tutorial，可能限制 M-bias/instrument/front-door 用户的采纳。
1447	
1448	    Post-publication 低成本 follow-up。'
1449	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "349aa139-658e-499e-b7c2-da7830a76efa",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "3685aeb5-43ce-421b-a751-6beef6bfeb8b",
  "sourceToolAssistantUUID": "349aa139-658e-499e-b7c2-da7830a76efa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T08:57:50.351Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PRhZSP3yzVN7drVpSqK8Tn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3685aeb5-43ce-421b-a751-6beef6bfeb8b",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYVk9zHpFJtzguLJHsg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45e60c74-972e-4edd-bb2a-f509ce8fb774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAQpYZ5q2WNGGHM9HU24CE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5552,
      "cache_read_input_tokens": 50834,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5552
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 50834,
          "cache_creation_input_tokens": 5552,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5552,
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

_source line 45 · 2026-05-20T08:57:50.628Z_

<details><summary>↩ Tool result · `toolu_01PRhZSP3yzVN7drVpSqK8Tn`</summary>

```text
1	narrative_guidance: 'Version B framing. Lead finding: "multi-class annotation error
2	  的危险性是 topology-dependent 的：
3	
4	  exposure misclassification 在方向和幅度上均不可预测，其余拓扑方向可预测但幅度需全 K×K 矩阵
5	
6	  才能量化——binary 框架在两种情况下均不足。" Claim 1 从 "breaks guarantees across topologies"
7	
8	  调整为 "reveals a sharp topology-dependent dichotomy"——exposure 是唯一方向不可预测的拓扑，
9	
10	  这本身是重要发现（exposure 是 CSS 中最常被 LLM 标注的变量）。Claim 2 的 ASV 从
11	
12	  "robustness to direction reversal" 调整为 "robustness to magnitude uncertainty"，
13	
14	  因 collider ASV 单调性部分失效（7% violations），需修改定义或加条件，降低紧性要求。
15	
16	  Claim 3 权重增加——correction guidance 的实用价值成为主要卖点，弥补 taxonomy 发现不够 dramatic。
17	
18	  需额外投入：(a) spectral 分析深挖 exposure 反转机制（λ₂/λ₁ 阈值），
19	
20	  (b) 经验实验扩充至 4-5 个 task 以补偿理论贡献缩窄，
21	
22	  (c) 考虑 user study 展示 ASV 对研究者决策的影响。
23	
24	  theory-MC match 在复杂拓扑（front-door, collider）偏低，需坦诚承认闭合形式表达式的近似局限性，
25	
26	  将 MC 验证本身作为补充贡献。经验混淆矩阵 diagonal-dominant，极端 C 结构罕见——
27	
28	  ASV 在多数实证场景输出 "robust"，实用区分力有限，需通过 semi-synthetic 注入实验补救。
29	
30	  '
31	imagined_experiments:
32	- name: Six-topology bias taxonomy (K=3)
33	  plan_id: plan_001
34	  description: '对 6 个 DAG 拓扑（confounding, mediation, collider, M-bias, instrument,
35	    front-door）
36	
37	    推导 K=3 闭合形式 bias 表达式，用 MC 验证（1000 reps × N=10000 × 6 种 C 结构）。
38	
39	    核心问题：哪些拓扑在 non-differential K≥3 误分类下出现方向反转？
40	
41	    '
42	  expected_results:
43	    reversal_topologies_count: 1
44	    confounding_reversal_rate: 0.0
45	    confounding_theory_mc_match: 6/6
46	    confounding_bias_range: 0.063–0.298
47	    exposure_reversal_rate: 0.85
48	    exposure_sign_reversal_rate: 0.834
49	    exposure_amplification_rate: 0.141
50	    exposure_theory_mc_match: 5/6
51	    exposure_bias_range: -0.84–0.42
52	    mediation_reversal_rate: 0.0
53	    mediation_theory_mc_match: 5/6
54	    mediation_bias_range: 0.00–0.15
55	    collider_reversal_rate: 0.0
56	    collider_theory_mc_match: 4/6
57	    collider_bias_range: 0.02–0.18
58	    mbias_reversal_rate: 0.0
59	    mbias_theory_mc_match: 4/6
60	    mbias_bias_range: 0.04–0.22
61	    instrument_reversal_rate: 0.0
62	    instrument_theory_mc_match: 5/6
63	    instrument_bias_range: 0.03–0.25
64	    frontdoor_reversal_rate: 0.0
65	    frontdoor_theory_mc_match: 3/6
66	    frontdoor_bias_range: 0.01–0.19
67	    overall_theory_mc_match: 32/42 (0.76)
68	    random_100k_reversal_topologies: exposure only
69	  result_rationale: 'Worst 档的核心预测：仅 exposure DAG 出现方向反转。机制上，exposure misclassification
70	
71	    直接扰乱 treatment assignment labels——当 K≥3 时，near-permutation C 导致 label swap，
72	
73	    将 treatment A 的 outcome 映射到 treatment B 的估计上，产生符号翻转。这在 K=2 时
74	
75	    结构性不可能（binary 只有"正确/错误"两种状态，non-differential 保证 bias toward null）。
76	
77	    其余 5 个拓扑中，misclassified 变量（confounder/mediator/collider/instrument/front-door
78	    variable）
79	
80	    不直接定义 treatment contrast，其误分类调制 bias magnitude 但不翻转 numerator/denominator，
81	
82	    因此方向可预测。Theory-MC match 率 0.76 偏低的原因：collider（conditioning 引入非线性）、
83	
84	    M-bias（双 confounder 路径交互）、front-door（复合 mediation 步骤）的闭合形式表达式
85	
86	    在 extreme C structures 下需要高阶 Taylor 项，一阶近似不够精确。Front-door 最差（3/6），
87	
88	    因为 front-door criterion 涉及两步 mediation，每步的近似误差在复合后被放大。
89	
90	    '
91	  tables:
92	  - name: 'Table 1: Six-Topology Bias Taxonomy Summary (K=3)'
93	    description: '6 rows (topologies) × columns: reversal_rate_100k, named_structure_match
94	      (x/6),
95	
96	      bias_range [min, max], bias_direction_class (monotonic-toward-null / monotonic-toward-OVB
97	      /
98	
99	      unpredictable), mechanism_summary.
100	
101	      Key pattern: exposure 行显著异于其余——reversal 85%，direction unpredictable；
102	
103	      其余 5 行 reversal 0%，方向可预测，但 magnitude range 差异大
104	
105	      （confounding 0.06-0.30 vs mediation 0.00-0.15 vs collider 0.02-0.18）。
106	
107	      '
108	  - name: 'Table 2: Theory vs MC Bias — Per-Structure Detail'
109	    description: '42 rows (6 topologies × ~7 structures including identity-adjacent,
110	      uniform-leaning,
111	
112	      near-permutation, block-diagonal, asymmetric, random-moderate, plus MVP-inherited).
113	
114	      Columns: topology, C_structure, theoretical_bias, mc_mean, mc_95ci, match (✓/✗).
115	
116	      10 个 ✗ 集中在 collider-near-permutation, mbias-block-diagonal,
117	
118	      frontdoor-near-permutation/asymmetric/block-diagonal。
119	
120	      '
121	  figures_description:
122	  - 'Fig 1: Heatmap — topology (y) × C-structure (x)，color = signed bias magnitude。Exposure
123	    行出现蓝红交替（正负 bias），其余行单色渐变（单调）。最直观的 ''dichotomy'' 可视化。'
124	  - 'Fig 2: Scatter — theoretical bias (x) vs MC mean bias (y)，per topology color-coded。理想
125	    y=x 线上 confounding/exposure 点紧贴，front-door 点偏离最大。附 R² per topology。'
126	  - 'Fig 3: 100k random C density plot — per topology 的 bias distribution。Exposure
127	    双峰分布（正负），其余单峰。'
128	  analysis: '核心结论：topology-dependent dichotomy 成立但 dramatic 程度有限。Exposure 是唯一 "dangerous"
129	
130	    拓扑，其余 5 个是 "well-behaved"。这支持 Version B framing，但问题是 5 个 well-behaved
131	
132	    拓扑的故事不够 exciting——"magnitude varies but direction is predictable" 比
133	
134	    "guarantees break" 弱得多。Theory-MC mismatch 在复杂拓扑的存在是双刃剑：一方面暴露
135	
136	    闭合表达式的局限性（reviewer concern），另一方面 MC 验证本身成为必要贡献
137	
138	    （"我们提供的不仅是理论，还有数值验证"）。Front-door 3/6 match 可能需要在论文中
139	
140	    降格为 "MC-validated conjecture" 而非 "theorem"。
141	
142	    Version B lead: 虽然 5 个拓扑方向可预测，但 magnitude range 的跨拓扑差异
143	
144	    （confounding 0.06-0.30 vs mediation 0.00-0.15）本身有信息量——研究者需要知道
145	
146	    自己的 DAG topology 处于哪个 magnitude regime，binary 框架无法提供这个信息。
147	
148	    '
149	- name: General-K matrix expressions and interpretability (K=5,7)
150	  plan_id: plan_002
151	  description: '将 bias 表达式推广到 K=5,7 的矩阵形式，开发三个可解释性工具：
152	
153	    (a) eigendecomposition 摘要，(b) worst-case scalar bounds，(c) diagnostic visualizations。
154	
155	    在 confounding + mediation + collider 上验证。
156	
157	    '
158	  expected_results:
159	    confounding_K5_dominant_eigenvalue_fraction: 0.82
160	    confounding_K7_dominant_eigenvalue_fraction: 0.76
161	    mediation_K5_dominant_eigenvalue_fraction: 0.75
162	    mediation_K7_dominant_eigenvalue_fraction: 0.68
163	    collider_K5_dominant_eigenvalue_fraction: 0.58
164	    collider_K7_dominant_eigenvalue_fraction: 0.49
165	    K5_theory_mc_match_rate: 0.7
166	    K7_theory_mc_match_rate: 0.63
167	    worst_case_bound_tightness_K5: 1.8–2.5x conservative
168	    worst_case_bound_tightness_K7: 2.5–3.2x conservative
169	    modes_needed_for_90pct_variance_collider_K7: 4
170	  result_rationale: 'K 增大时，C 的自由度从 K=3 的 6 个增长到 K=5 的 20 个、K=7 的 42 个。
171	
172	    Confounding DAG 的 bias 有简单的方向结构（residual confounding 沿单一方向累积），
173	
174	    因此 dominant eigenvalue 即使在 K=7 仍捕获 76% variance——eigendecomposition 是有效的摘要工具。
175	
176	    Collider DAG 的 bias 来自 conditioning 引入的伪相关，其方向依赖于 collider 各类别间的
177	
178	    相对误分类强度——K=7 时 7 个类别的两两误分类形成多维度干扰，dominant eigenvalue 仅捕获
179	
180	    49%，需要 4 个 mode 才能解释 90% variance，eigendecomposition 失去摘要价值。
181	
182	    Worst-case bounds 松的原因：bounds 必须覆盖 adversarial C 结构，但实际 C 的 feasible region
183	
184	    在高 K 时是高维空间中的低维 manifold——bounds 优化的 supremum 在实践中不可达。
185	
186	    Theory-MC match 在 K=7 降至 0.63，因为矩阵形式表达式中的 Kronecker product 项
187	
188	    在数值求解时积累舍入误差，且 MC 的 N=10000 在 K=7 时 per-cell 样本量不足
189	
190	    （7×7=49 cells，某些 cell 可能 <50 observations）。
191	
192	    '
193	  tables:
194	  - name: 'Table 3: Eigendecomposition Summary — K=3,5,7 × 3 Topologies'
195	    description: '9 rows (3 K × 3 topologies) × columns: K, topology, λ₁/tr(Λ), modes_for_90pct,
196	
197	      dominant_mode_interpretation, bound_tightness_ratio.
198	
199	      Key pattern: confounding 始终 clean（1-2 modes），collider 随 K 增长迅速恶化。
200	
201	      '
202	  - name: 'Table 4: Worst-Case Scalar Bound vs Actual MC Maximum Bias'
203	    description: '展示 bound 的 conservativeness。Columns: topology, K, worst_case_bound,
204	
205	      mc_observed_max, ratio. Ratio 从 K=3 的 1.3x 增长到 K=7 的 3.2x。
206	
207	      '
208	  figures_description:
209	  - 'Fig 4: Eigenvalue spectrum bar chart — 3 panels (K=3,5,7)，每 panel 3 条 bar groups
210	    (topologies)，bar height = eigenvalue magnitude。展示 confounding 的 spectral concentration
211	    vs collider 的 dispersion。'
212	  - 'Fig 5: Diagnostic heatmap — 对 K=5 confounding DAG，将 C 的 20 维参数空间降至 2D (PCA)，color
213	    = bias magnitude。展示 bias landscape 的可视化工具原型。'
214	  analysis: 'Worst 档下，K=5,7 的 interpretability tools 对 confounding/mediation 有效但对
215	    collider 不足。
216	
217	    这意味着论文中 "eigendecomposition as interpretability tool" 的 claim 需要加 caveat：
218	
219	    仅对 bias 有清晰方向结构的拓扑有效。Worst-case bounds 的 3x conservativeness
220	
221	    使其实用价值有限——bound 告诉你 "bias 最多这么大" 但实际远小于此。
222	
223	    建议：对 collider/M-bias 拓扑放弃 eigendecomposition 摘要，改用 worst-case bound +
224	
225	    diagnostic visualization 的组合。论文中坦诚分拓扑讨论可解释性工具的适用范围。
226	
227	    '
228	- name: Empirical confusion matrices (3 LLMs × 3 CSS tasks)
229	  plan_id: plan_003
230	  description: '收集 Llama 4 Maverick / Qwen 3.5 Plus / DeepSeek V4 在 protest event
231	    coding (K=5),
232	
233	    stance detection (K=3), toxicity (K=2) 上的经验混淆矩阵，分析 inter-model 相关性
234	
235	    和 downstream regression bias。
236	
237	    '
238	  expected_results:
239	    protest_accuracy_range: 0.68–0.73
240	    protest_diagonal_dominance_range: 0.74–0.80
241	    stance_accuracy_range: 0.76–0.81
242	    stance_diagonal_dominance_range: 0.82–0.87
243	    toxicity_accuracy_range: 0.83–0.88
244	    inter_model_error_kappa: 0.58–0.67
245	    near_permutation_structures_observed: 0
246	    downstream_bias_gt_005_count: 2–3 out of 9
247	    downstream_direction_reversal_observed: false
248	    max_downstream_bias: 0.12
249	    total_annotations: ~270K (30K × 3 models × 3 tasks)
250	    api_cost_actual: $350–480
251	  result_rationale: '当前 SOTA LLMs 在 well-studied CSS tasks 上准确率 0.68-0.88，产出的混淆矩阵
252	
253	    必然 diagonal-dominant。Off-diagonal mass 集中在语义相邻类别（如 stance detection 中
254	
255	    "support" 与 "somewhat support" 互混），而非随机分散——这意味着 C 结构远离
256	
257	    near-permutation 极端。Inter-model error kappa 0.58-0.67 与 Kim et al. (ICML 2025)
258	
259	    的 60% error agreement 一致，因为 LLM 的错误模式受 pre-training data distribution
260	
261	    驱动，不同模型在相同 "难" 样本上犯相似错误。Downstream bias 多数 <0.05 因为
262	
263	    diagonal-dominant C 的 bias 表达式给出小值；2-3 个 >0.05 的案例出现在 protest event
264	
265	    coding（K=5，准确率最低）与较弱模型（Qwen 3.5 Plus）的组合。无方向反转因为：
266	
267	    (a) 经验 C 是 diagonal-dominant，远未到 near-permutation threshold，
268	
269	    (b) 如果实验设计中 annotated variable 是 confounder/mediator（非 exposure），
270	
271	    则即使 C 极端也不会反转（worst 档核心假设）。
272	
273	    这是 worst 档最关键的弱点：经验数据 "太好了"，极端 C 结构罕见，
274	
275	    ASV 和 bias taxonomy 的实用展示受限。
276	
277	    '
278	  tables:
279	  - name: 'Table 5: Empirical Confusion Matrices — 9 Combinations'
280	    description: '9 个混淆矩阵（3 LLMs × 3 tasks），每个附 accuracy, diagonal_dominance_ratio,
281	
282	      Frobenius_distance_to_identity. Protest K=5 的矩阵最 "丰富"（off-diagonal 分散），
283	
284	      toxicity K=2 的矩阵最 diagonal-dominant。
285	
286	      '
287	  - name: 'Table 6: Inter-Model Error Correlation'
288	    description: '3×3 模型对的 error agreement matrix（pairwise kappa on error cells）。
289	
290	      值 0.58-0.67，证实跨模型错误高度相关。附 per-category breakdown。
291	
292	      '
293	  - name: 'Table 7: Downstream Regression Bias vs Gold Standard'
294	    description: '9 rows × columns: task, model, DAG_topology_assumed, effect_gold,
295	      effect_annotated,
296	
297	      bias, bias_direction, theoretical_prediction, match (✓/✗).
298	
299	      2-3 行 bias >0.05，其余 <0.05。
300	
301	      '
302	  figures_description:
303	  - 'Fig 6: 9-panel 混淆矩阵 heatmap grid (3 models × 3 tasks)。Color intensity = cell
304	    probability。视觉上全部 diagonal-dominant，off-diagonal 仅在 protest K=5 panel 较显著。'
305	  - 'Fig 7: Inter-model error Venn diagram — 展示 3 模型在 stance detection 上的 error overlap。~60%
306	    三模型共同犯错的样本，呼应 Kim et al. 发现。'
307	  analysis: 'Worst 档的关键困境：经验混淆矩阵全部 diagonal-dominant，无 near-permutation 结构。
308	
309	    这意味着：(1) bias taxonomy 的 "dramatic" 案例（direction reversal）在实证中不出现，
310	
311	    (2) ASV 多数输出 "robust"（大 ASV 值），区分力有限，(3) correction guidance 在多数场景
312	
313	    退化为 "MLA suffices"。应对策略：(a) semi-synthetic 实验——在经验 C 基础上注入
314	
315	    controlled perturbation，展示 "如果 LLM 准确率再低 10% 会怎样"，
316	
317	    (b) 将 diagonal-dominant 本身作为 positive finding（"当前 LLM 的错误模式在多数 CSS
318	
319	    tasks 上落在 safe zone——但 ASV 量化了 safe zone 的边界"），
320	
321	    (c) 增加 4th/5th task（低资源语言 stance detection 或 fine-grained emotion K=7）
322	
323	    以提高观察到 non-diagonal-dominant C 的概率。
324	
325	    '
326	- name: Binarization collapse analysis (K→2 across 6 topologies)
327	  plan_id: plan_008
328	  description: '对 6 个拓扑的 K=3,5,7 变量做 binary collapse，比较 full multi-class bias expression
329	
330	    与 binarized bias expression 的差异，证明 binarization 不是安全捷径。
331	
332	    '
333	  expected_results:
334	    confounding_K3_max_delta: 0.078
335	    confounding_K5_max_delta: 0.085
336	    confounding_K7_max_delta: 0.091
337	    exposure_K3_max_delta: 0.072
338	    mediation_K3_max_delta: 0.041
339	    collider_K3_max_delta: 0.068
340	    mbias_K3_max_delta: 0.055
341	    instrument_K3_max_delta: 0.038
342	    frontdoor_K3_max_delta: 0.045
343	    overall_max_delta: 0.091
344	    topologies_with_delta_gt_005: 4
345	    topologies_with_delta_gt_008: 2
346	    binarization_can_reverse_direction: false
347	  result_rationale: 'Binarization 将 K-class variable collapse 为 binary，丢弃类别间的 fine-grained
348	
349	    误分类信息。在 worst 档下，max delta 0.091 低于 MVP 的 0.103（MVP 的 0.103
350	
351	    来自特定 near-permutation C 结构 + confounding DAG 的最优案例）。系统搜索发现
352	
353	    confounding DAG 仍是 binarization effect 最大的拓扑（residual confounding 对
354	
355	    class-collapse 最敏感），而 mediation/instrument 的 delta 较小（<0.05）因为这些拓扑中
356	
357	    annotated variable 的 misclassification 本身效应就小，binarization 损失的信息量有限。
358	
359	    关键限制：binarization 在 worst 档下未导致方向反转（仅改变 magnitude），
360	
361	    削弱了 "binarization is hazardous" 的 claim 力度。Delta 0.091 在统计上显著
362	
363	    但实质意义存疑——reviewer 可能质疑 "0.09 的额外 bias 在社会科学效应量通常 0.1-0.3
364	
365	    的语境下是否 material"。
366	
367	    '
368	  tables:
369	  - name: 'Table 8: Binarization Delta — 6 Topologies × K=3,5,7'
370	    description: '~18 rows (6 topologies × 3 K values) × columns: topology, K, folding_scheme,
371	
372	      bias_multiclass, bias_binary, delta, delta/bias_multiclass (relative),
373	
374	      direction_change (all "No"). Max delta bolded. Confounding rows consistently
375	
376	      highest delta.
377	
378	      '
379	  figures_description:
380	  - 'Fig 8: Grouped bar chart — x = topology, grouped bars = K=3/5/7, y = |Δ|。 Horizontal
381	    line at Δ=0.05 作为 ''material threshold''。展示 4/18 bars 超过 threshold。'
382	  - 'Fig 9: Scatter — multi-class bias (x) vs binary bias (y) per configuration, 45°
383	    reference line。 Points below line = binarization underestimates bias。展示系统性偏离但
384	    magnitude 有限。'
385	  analysis: 'Worst 档下 binarization 分析的结论是 "real but modest"。Max Δ=0.091 支持
386	
387	    "binary 框架不足" 的 claim，但不够 dramatic 作为 standalone finding。在 Version B
388	
389	    framing 中，binarization 分析应作为 supporting evidence 而非 lead result——
390	
391	    它回答的问题从 "binarization is dangerous" 降级为 "binarization loses information
392	
393	    that matters for magnitude estimation"。建议：在论文中将 binarization 分析压缩为
394	
395	    1 段 + 1 figure，将篇幅让给 exposure 反转机制的 spectral 分析和 correction framework。
396	
397	    '
398	- name: ASV formal proofs (confounding, mediation, collider)
399	  plan_id: plan_004
400	  description: '为 3 个优先拓扑推导 ASV 表达式，证明 monotonicity 和 sharpness，
401	
402	    MC 验证 coverage（90%, 95%, 99%）。
403	
404	    '
405	  expected_results:
406	    confounding_monotonicity: PROVED (formal)
407	    confounding_sharpness: PROVED (formal)
408	    confounding_coverage_90: 0.88
409	    confounding_coverage_95: 0.93
410	    confounding_coverage_99: 0.97
411	    mediation_monotonicity: PROVED (formal)
412	    mediation_sharpness: FAILED — bound conservative by factor 1.4–1.8x
413	    mediation_coverage_90: 0.86
414	    mediation_coverage_95: 0.91
415	    mediation_coverage_99: 0.96
416	    collider_monotonicity: FAILED — 7% of C structures show non-monotone ASV in δ
417	    collider_sharpness: N/A (requires monotonicity)
418	    collider_coverage_90: 0.74
419	    collider_coverage_95: 0.78
420	    collider_coverage_99: 0.85
421	    asv_sharpness_formal_proofs: 1
422	    collider_monotonicity_violation_delta_range: 0.3–0.5
423	    collider_violation_C_characterization: off-diagonal mass concentrated in 2 adjacent
424	      cells
425	  result_rationale: 'Confounding ASV monotonicity 成立因为 residual confounding 是 δ 的单调函数——
426	
427	    更大的 annotation error amplification 只能增加残差混淆，不能减少。Sharpness 成立因为
428	
429	    near-permutation C 结构确实实现了 bound（近似完全 label swap 达到最大 residual confounding）。
430	
431	
432	    Mediation ASV monotonicity 成立因为 indirect effect 的 attenuation 随 mediator
433	
434	    misclassification 单调增加。但 sharpness 失败因为 mediation bias 的 maximum 受限于
435	
436	    direct effect magnitude——即使 C 完全 permutation，bias 也不能超过 direct effect，
437	
438	    而 ASV bound 的推导假设 bias 可以达到 "worst-case over all C in δ-ball"，
439	
440	    其中包含了结构上不可达的 C 配置。Bound conservative 1.4-1.8x。
441	
442	
443	    Collider ASV 是 worst 档的关键难点。Collider bias 来自 conditioning on a common effect——
444	
445	    当 collider variable 被 misclassify 时，conditioning 的 "打开" 程度取决于 C 结构。
446	
447	    在某些 C 结构下（off-diagonal mass 集中在 2 个相邻 cell），δ 从 0.3 增到 0.5 时
448	
449	    bias 先增后减——因为中等 misclassification 部分打开 collider path 但保留 conditioning
450	
451	    结构，而更大的 misclassification 反而 "破坏" 了 conditioning 的精确性，使 collider path
452	
453	    的打开效果被噪声稀释。这产生 non-monotone ASV，7% violation rate。
454	
455	    修补方案：restricted ASV（限制 δ-path 在 monotone region）或 conditional ASV
456	
457	    （对 C 结构分区域定义）。两种方案都增加框架复杂度，降低实用性。
458	
459	    '
460	  tables:
461	  - name: 'Table 9: ASV Proof Status Summary'
462	    description: '3 rows (topologies) × columns: monotonicity (✓/✗ + proof type),
463	
464	      sharpness (✓/✗ + proof type), coverage_90/95/99, notes.
465	
466	      Confounding 行全绿，mediation 行部分黄（sharpness ✗），collider 行红（monotonicity ✗）。
467	
468	      '
469	  - name: 'Table 10: ASV Coverage — 1000 Scenario MC Validation'
470	    description: '详细 coverage 分析。Per topology 的 coverage 分布（不是单个数字）——
471	
472	      histogram of "actual coverage across 1000 scenarios"。Confounding 集中在 0.92-0.95，
473	
474	      collider 分散在 0.65-0.90 with a tail of under-coverage。
475	
476	      '
477	  figures_description:
478	  - 'Fig 10: ASV monotonicity diagnostic — 3 panels (topologies)。每 panel 画 ASV(δ)
479	    curve for 20 randomly sampled C structures。Confounding/mediation: all curves monotonically
480	    increasing。Collider: 2-3 curves show a ''bump'' (local maximum) at δ≈0.35，demonstrating
481	    non-monotonicity。'
482	  - 'Fig 11: Coverage calibration plot — nominal coverage (x, 0.80-0.99) vs empirical
483	    coverage (y)。45° line = perfect calibration。Confounding 紧贴 45° 线，collider 系统性低于
484	    45° 线。'
485	  analysis: 'ASV 框架在 worst 档下遭遇了预期中的 collider 难题。Sharpness 仅 1 个拓扑完成证明，
486	
487	    低于理想但在 [1,2] 范围内。Collider 的 non-monotonicity 是论文的潜在 weakness——
488	
489	    reviewer 会问 "如果 ASV 在 collider 拓扑不 monotone，你的框架怎么用？"
490	
491	    应对：(1) 论文中诚实报告 collider 的限制，提出 restricted ASV 定义，
492	
493	    (2) 强调 collider 在 CSS 实证中相对少见（mediation/confounding 更常见），
494	
495	    (3) 将 collider ASV 修复标记为 "important future work" 而非尝试勉强证明。
496	
497	    Coverage 0.85 (aggregated) 在 [0.80, 0.88] 范围内——不是灾难性的 under-coverage，
498	
499	    但需要在论文中解释为什么 coverage 低于 nominal 并建议 practitioners 使用 99% level
500	
501	    而非 95% level 作为 conservative 选择。
502	
503	    '
504	- name: ASV MC validation (M-bias, instrument, front-door)
505	  plan_id: plan_005
506	  description: '对剩余 3 个拓扑推导 ASV 表达式并做 MC 验证。
507	
508	    Monotonicity 和 sharpness 作为 conjecture + numerical evidence，不要求 formal proof。
509	
510	    '
511	  expected_results:
512	    mbias_monotonicity_mc: holds (0/1000 violations)
513	    mbias_sharpness_mc: not achieved — bound conservative by 1.6–2.1x
514	    mbias_coverage_95: 0.86
515	    instrument_monotonicity_mc: holds (0/1000 violations)
516	    instrument_sharpness_mc: near-sharp — within 1.1x in 3% of scenarios
517	    instrument_coverage_95: 0.88
518	    frontdoor_monotonicity_mc: holds for 97% of scenarios (3% violations at extreme
519	      C)
520	    frontdoor_sharpness_mc: not achieved — bound conservative by 1.8–2.4x
521	    frontdoor_coverage_95: 0.76
522	    aggregate_coverage_95_all_6: 0.85
523	  result_rationale: 'M-bias 的 monotonicity 成立因为 M-bias 的 bias 结构本质上是两条 confounding
524	    path 的
525	
526	    叠加——每条 path 的 bias 对 δ 单调，叠加后仍单调。但 sharpness 不成立因为
527	
528	    两条 path 的 maximum bias 不能同时达到——worst-case C 对 path 1 最优时，
529	
530	    对 path 2 不一定最优，dual-confounder 结构限制了 joint worst case 的可达性。
531	
532	
533	    Instrument 的 monotonicity 成立因为 IV estimation 的 bias 在 instrument misclassification
534	
535	    下是线性的——Wald estimator 的分母（first-stage coefficient）被 attenuation，
536	
537	    bias = true_effect × (1 - attenuation_factor)，monotone in δ。Near-sharp 因为
538	
539	    IV 的 linear structure 使 bound 很接近 achievable maximum。
540	
541	
542	    Front-door 有 3% violations 因为 front-door criterion 涉及两步：(1) exposure → mediator
543	
544	    和 (2) mediator → outcome（调整 exposure）。在极端 C 下（near-rank-deficient），
545	
546	    步骤 (2) 的调整不稳定——small δ change 可能 flip 步骤 (2) 的调整方向，
547	
548	    导致总 bias 的 local non-monotonicity。这是 compound estimation 的固有问题，
549	
550	    与 collider 的 non-monotonicity 机制不同（collider 是 conditioning 问题，front-door 是
551	
552	    调整稳定性问题）。
553	
554	
555	    Aggregate coverage 0.85：front-door 的 0.76 拉低整体。如果排除 front-door，
556	
557	    remaining 5 topologies 的 mean coverage 是 0.87。
558	
559	    '
560	  tables:
561	  - name: 'Table 11: ASV Validation Summary — Remaining 3 Topologies'
562	    description: '3 rows × columns: topology, monotonicity_status, violation_rate,
563	
564	      sharpness_status, bound_tightness, coverage_90/95/99.
565	
566	      附注释解释 front-door 3% violations 的机制。
567	
568	      '
569	  - name: 'Table 12: Aggregate ASV Framework Status — All 6 Topologies'
570	    description: '综合 Table 9 和 Table 11 的 summary view。6 rows，每行标注
571	
572	      proof_type (formal / MC-conjecture) 和 overall_status (full / partial / needs-repair)。
573	
574	      Color-coded: confounding=green, mediation/instrument/mbias=yellow,
575	
576	      collider/frontdoor=orange。
577	
578	      '
579	  figures_description:
580	  - 'Fig 12: ASV(δ) curves for M-bias/instrument/front-door，与 Fig 10 对应。Instrument
581	    curves 最 clean（几乎线性），front-door 有 2-3 条 curves 在极端 C 下出现微弱 non-monotonicity。'
582	  analysis: '5/6 拓扑 monotonicity 基本成立（collider 7% violations + front-door 3% violations
583	
584	    是仅有的例外）。从论文叙事角度，这支持 "ASV 框架在大多数实用场景下有效" 的 claim，
585	
586	    但 "大多数" 而非 "所有" 是 worst 档的定义性特征。Sharpness 普遍不足——
587	
588	    6 个拓扑中仅 confounding 达到 formal sharpness，instrument 接近。
589	
590	    这意味着 ASV 在实践中偏 conservative（报告的 robustness 比实际更悲观），
591	
592	    对 practitioners 来说是 safe 的方向但削弱了 ASV 的 "precision" selling point。
593	
594	    Version B framing 将 ASV 定位为 "magnitude uncertainty 的 robustness measure"
595	
596	    而非 "direction reversal 的 guard"——这个定位与 sharpness 不足是兼容的
597	
598	    （magnitude uncertainty 不需要 tight bound，conservative 即可）。
599	
600	    '
601	- name: ASV empirical calibration (3 tasks × 3 LLMs)
602	  plan_id: plan_006
603	  description: '将 ASV 应用到 plan_003 的经验混淆矩阵，在 held-out gold-standard splits 上验证 coverage，
604	
605	    报告 ASV alongside downstream effect estimates。
606	
607	    '
608	  expected_results:
609	    meaningful_asv_count: 4
610	    vacuous_asv_count: 5
611	    concordance_meaningful: 4/4 (all meaningful ASVs correctly classify robust vs
612	      fragile)
613	    concordance_total: 4/9 (5 vacuous cases are trivially correct but uninformative)
614	    empirical_asv_concordance: 4
615	    asv_infinite_or_very_large_cases: 5
616	    protest_Qwen_asv: finite, ASV=2.3 (fragile)
617	    protest_Llama_asv: finite, ASV=4.1 (moderate)
618	    stance_DeepSeek_asv: large, ASV=18.7 (robust)
619	    toxicity_all_asv: '>50 (robust, binary special case)'
620	  result_rationale: '经验混淆矩阵 diagonal-dominant（plan_003 结果），因此达到 direction-reversing
621	    或
622	
623	    magnitude-significant 的 δ threshold 很高——ASV 值大（甚至无穷）。
624	
625	    5/9 combinations 的 ASV ≫10，意味着 "需要当前 annotation error 放大 10 倍以上
626	
627	    才会产生有意义的 bias"——technically correct 但 uninformative（研究者已经知道
628	
629	    高准确率 LLM 产生的 bias 小）。4/9 meaningful cases 出现在 K=5 protest event coding
630	
631	    （准确率最低，off-diagonal mass 最大）和 K=3 stance detection 与较弱模型的组合。
632	
633	    这些 meaningful cases 中 ASV 正确区分了 fragile（ASV<5）vs robust（ASV>10）——
634	
635	    但样本量太小（4 cases）无法做统计检验。
636	
637	
638	    Worst 档的核心困境在此体现：ASV 的理论价值依赖于经验 C 足够 "interesting"，
639	
640	    但 SOTA LLMs 太好了，经验 C 太 "boring"。
641	
642	    '
643	  tables:
644	  - name: 'Table 13: ASV Values — 9 Combinations'
645	    description: '9 rows × columns: task, model, K, accuracy, diagonal_dominance,
646	
647	      ASV_value, ASV_classification (fragile/moderate/robust),
648	
649	      held_out_bias, held_out_direction, concordance (✓/✗/trivial).
650	
651	      5 行标注 "trivial" (ASV>50)，4 行标注 ✓。
652	
653	      '
654	  - name: 'Table 14: ASV vs Raw Confusion Matrix — Interpretability Comparison'
655	    description: '对 4 个 meaningful cases，并排展示 ASV summary 和 raw confusion matrix，
656	
657	      说明 ASV 提供了哪些 confusion matrix 本身不直接给出的信息
658	
659	      （主要是 "离 danger zone 有多远" 的距离度量）。
660	
661	      '
662	  figures_description:
663	  - 'Fig 13: ASV sensitivity curve — 对 protest/Qwen (ASV=2.3) case，画 bias magnitude
664	    as function of δ amplification factor。Vertical line at δ=1 (current error)，δ=2.3
665	    处 bias crosses significance threshold。展示 ASV 的可视化解读。'
666	  - 'Fig 14: ASV distribution across 9 combinations — dot plot with log scale y axis。Clear
667	    separation between 4 finite-meaningful (ASV 2-5) and 5 vacuous (ASV >15) cases。'
668	  analysis: '4/9 concordance 在 [3,6] 范围的低端。论文叙事需要将这个结果 reframe：
669	
670	    不是 "ASV 在 9 个场景中只有 4 个有用"，而是 "ASV 正确识别了 4 个值得关注的
671	
672	    high-risk combinations——这些是研究者在没有 ASV 的情况下可能忽略的"。
673	
674	    对 5 个 vacuous cases，论文可以说 "ASV 为这些 combinations 提供了 formal robustness
675	
676	    guarantee，研究者可以安心使用"——但 reviewer 可能反驳 "any reasonable researcher
677	
678	    wouldn''t worry about a 85%-accurate annotator"。
679	
680	
681	    增强策略：(a) semi-synthetic 注入——在经验 C 上添加 controlled degradation
682	
683	    （accuracy 从 0.8 降至 0.5），展示 ASV 如何从 "robust" 转变为 "fragile"，
684	
685	    (b) 增加低资源任务（如小语种情感分析 K=7），提高观察到 meaningful ASV 的概率，
686	
687	    (c) user study——给研究者展示 ASV vs 不展示 ASV，测量决策质量差异。
688	
689	    '
690	- name: Correction guidance framework
691	  plan_id: plan_007
692	  description: '构建 {topology × error structure × ASV} → correction method 的决策框架，
693	
694	    MC 验证 recommended method 在 ≥90% scenarios 产生最小 bias，
695	
696	    经验数据验证。
697	
698	    '
699	  expected_results:
700	    overall_accuracy: 0.78
701	    mla_recommendation_fraction: 0.65
702	    exposure_reversal_recommendation: gold label collection / no adequate correction
703	    exposure_accuracy: 0.85
704	    confounding_accuracy: 0.82
705	    collider_accuracy: 0.68
706	    scenarios_where_no_method_adequate: 0.12
707	    ppi_outperforms_mla_fraction: 0.08
708	    dsl_applicable_fraction: 0.05
709	    naive_plugin_never_recommended: true
710	    correction_framework_accuracy: 0.78
711	    decision_tree_depth: 4
712	    decision_tree_leaf_purity: 0.73
713	  result_rationale: 'Correction framework accuracy 0.78 反映了 worst 档的核心预测：framework
714	    在多数场景
715	
716	    退化为 "use MLA"。当 65% 的 scenarios 的最优推荐是 MLA 时，一个 trivial baseline
717	
718	    "always recommend MLA" 就有 65% accuracy——framework 的 0.78 仅比 trivial baseline
719	
720	    高 13 个百分点，discriminative value 有限。
721	
722	
723	    MLA 主导的原因：MLA (Measurement-error Likelihood Adjustment) 是最 general 的方法，
724	
725	    它利用 C 矩阵估计对 likelihood 做调整，适用于任何 topology + 任何 error structure。
726	
727	    在 5 个 "well-behaved" topology（方向可预测）中，MLA 几乎总是最优选择因为它直接
728	
729	    纠正 bias magnitude。PPI 仅在 finite-sample regime（small gold sample + large LLM sample）
730	
731	    优于 MLA（8% scenarios）。DSL 仅在 very specific conditions（已知 C + linear model）下
732	
733	    优于 MLA（5% scenarios）。
734	
735	
736	    Exposure topology 是 framework 最有价值的部分——对 reversal-risk scenarios，framework
737	
738	    正确推荐 "no correction adequate without gold labels"，这是 non-trivial guidance
739	
740	    （naive researcher 可能尝试 MLA 但 MLA 在 sign-reversed regime 可能 amplify error）。
741	
742	
743	    Collider accuracy 最低（0.68）因为 collider bias correction 依赖于 conditioning strategy——
744	
745	    "correct the annotation then re-condition" vs "don''t condition at all" 的选择
746	
747	    取决于 effect magnitude 和 C structure 的交互，decision tree 难以准确捕获。
748	
749	    '
750	  tables:
751	  - name: 'Table 15: Correction Guidance Decision Framework'
752	    description: 'Matrix format: rows = topologies (6), columns = error structure
753	      categories
754	
755	      (diagonal-dominant / moderate / near-permutation × differential / non-differential),
756	
757	      cells = recommended method + ASV threshold. 大量 cells 填入 "MLA"。
758	
759	      Exposure 行的 near-permutation cells 标红 "gold labels required"。
760	
761	      '
762	  - name: 'Table 16: Framework Accuracy — MC Validation'
763	    description: 'Per topology accuracy, per error-structure accuracy, confusion matrix
764	      of
765	
766	      {recommended method × actually-best method}. 最大 off-diagonal cluster:
767	
768	      MLA recommended but PPI actually marginally better (差异 <0.01 bias)。
769	
770	      '
771	  - name: 'Table 17: Open Problem Identification'
772	    description: '12% of scenarios 标记为 "no existing method adequate"。
773	
774	      Columns: scenario_description, why_inadequate, required_capability.
775	
776	      主要集中在 differential multi-class error + complex topology (M-bias, front-door)
777	
778	      和 correlated multi-LLM error。
779	
780	      '
781	  figures_description:
782	  - 'Fig 15: Decision tree visualization — depth 4, 12 leaves。Color = recommended
783	    method。大量绿色叶节点（MLA），少量红色（gold labels）和蓝色（PPI）。视觉上展示 ''MLA 主导'' 的现实。'
784	  - 'Fig 16: Framework accuracy vs ASV — scatter plot，x = ASV magnitude，y = framework
785	    recommendation correct (1/0)。低 ASV（fragile）区域 accuracy 更高（framework 更有价值），高 ASV（robust）区域
786	    accuracy 无意义（任何推荐都 work）。'
787	  analysis: 'Correction framework 在 worst 档下的 selling point 不是 accuracy 而是 completeness——
788	
789	    "first systematic mapping of when each correction method applies, with identified
790	    open problems"。
791	
792	    0.78 accuracy 加上 MLA 65% dominance 意味着 framework 的 practical value 集中在
793	
794	    ~35% non-MLA scenarios（exposure reversal + PPI edge cases + no-method-adequate
795	    regimes）。
796	
797	    Version B narrative 中 Claim 3 权重增加，需要将 framework 包装为 "practitioner''s guide"
798	
799	    而非 "automated decision system"——降低 accuracy 期望，强调 "the framework identifies
800	
801	    what you should worry about, not just what to do"。
802	
803	    Open problems 部分（12% no-method-adequate）可能是最有 citation value 的贡献——
804	
805	    明确指出 correlated multi-LLM error correction 是 unsolved problem，引导后续研究。
806	
807	    '
808	- name: Pathological confusion matrix analysis (spectral)
809	  plan_id: plan_009
810	  description: '分析极端 C 结构（near-permutation, rank-deficient, block-diagonal）在 6 个拓扑下的
811	
812	    bias 行为，用 spectral 分析（eigenvalue spectrum of C）识别 bias severity 的
813	
814	    structural predictors。
815	
816	    '
817	  expected_results:
818	    exposure_reversal_spectral_threshold: λ₂/λ₁ > 0.6 for K=3
819	    exposure_reversal_prediction_auc: 0.92
820	    diagonal_dominance_as_simple_predictor: reversal when diag_dom < 0.45
821	    diagonal_dominance_prediction_auc: 0.89
822	    other_topologies_spectral_finding: monotone relationship between λ₁ and bias magnitude;
823	      no reversal threshold exists
824	    spectral_gap_predicts_magnitude_R2: 0.78
825	    block_diagonal_C_magnitude_effect: 1.5–2.3x bias amplification vs random C of
826	      same accuracy
827	    rank_deficient_C_behavior: bias expressions numerically unstable, need regularization
828	  result_rationale: 'Exposure DAG 的反转机制有清晰的 spectral interpretation：C 矩阵的 eigendecomposition
829	
830	    中，λ₁ 对应 "correct classification" mode（沿 identity 方向），λ₂ 对应 "dominant confusion"
831	
832	    mode（label swap 方向）。当 λ₂/λ₁ > 0.6 时，confusion mode 足够强以翻转 treatment
833	
834	    assignment 的有效方向，产生 sign reversal。这个阈值在 K=3 下给出 AUC 0.92 的
835	
836	    reversal 预测——spectral gap 是一个 principled predictor。
837	
838	    Diagonal dominance（diag_dom = min_i C_ii / max_i Σ_{j≠i} C_ij）是更简单的 proxy，
839	
840	    AUC 0.89 略低但更直观。
841	
842	
843	    对其余 5 个拓扑，spectral 分析揭示 λ₁ 与 bias magnitude 的 monotone relationship
844	
845	    （R²=0.78），但没有 "reversal threshold"——bias 方向由 topology 的结构性质决定
846	
847	    （confounding → toward OVB, mediation → toward attenuation, etc.），C 的 spectrum
848	
849	    只调制 magnitude。这在理论上不意外（worst 档假设），但提供了一个
850	
851	    compact characterization。
852	
853	
854	    Block-diagonal C（如 K=6 分成两个 K=3 block，block 间无混淆）产生 1.5-2.3x
855	
856	    bias amplification 因为 block 结构创造了 "structured confusion"——模型在 block 内
857	
858	    混淆但 block 间清晰，这比同等 accuracy 的 random C 产生更大 bias
859	
860	    因为 confusion 集中而非分散。
861	
862	
863	    Rank-deficient C 导致某些 bias 表达式的矩阵求逆不稳定——这是实际计算中的
864	
865	    nuisance，不是理论 insight，但需要在 toolkit 中处理（regularization）。
866	
867	    '
868	  tables:
869	  - name: 'Table 18: Spectral Predictors of Bias Severity'
870	    description: 'Columns: predictor (λ₂/λ₁, diag_dom, spectral_gap, Frobenius_norm),
871	
872	      target (reversal_binary, bias_magnitude), topology, AUC_or_R².
873	
874	      Exposure rows 有 reversal prediction AUC，其余行仅有 magnitude R²。
875	
876	      '
877	  - name: 'Table 19: Pathological C Structure Catalog'
878	    description: 'Catalog of 4 pathological C types × 6 topologies × {bias_magnitude,
879	
880	      direction_preserved, numerical_stability}。27 行 summary。
881	
882	      '
883	  figures_description:
884	  - 'Fig 17: Spectral gap vs bias — 2 panels。Left: exposure DAG，scatter with reversal
885	    colored red/blue，clear threshold at λ₂/λ₁=0.6。Right: confounding DAG，smooth monotone
886	    curve，no threshold。最直观的 ''dichotomy'' spectral evidence。'
887	  - 'Fig 18: Block-diagonal C amplification — bar chart comparing bias from block-diagonal
888	    vs random C at matched accuracy, across 6 topologies。展示 structured confusion 的
889	    amplification effect。'
890	  analysis: 'Spectral 分析在 worst 档下提供了 exposure 反转的 mechanistic explanation——
891	
892	    这是 narrative 需要的 "deep dive"。λ₂/λ₁ > 0.6 threshold 是一个 actionable
893	
894	    practitioner guideline（"检查你的 confusion matrix 的 spectral gap，如果 < 0.4
895	
896	    则 exposure 标注安全"）。对其余拓扑，spectral 分析的贡献更 modest——
897	
898	    确认了 "方向可预测，magnitude 依赖 C" 的结论但没有 surprising insight。
899	
900	    Block-diagonal 发现是 bonus 内容——在 CSS 中，block-diagonal C 对应
901	
902	    "模型区分粗粒度类别但混淆细粒度类别" 的常见模式，有实际意义。
903	
904	    建议在论文中将 spectral 分析作为 Section 4 的 highlight（exposure deep dive），
905	
906	    其余拓扑的 spectral 结果放 appendix。
907	
908	    '
909	- name: annot-sensitivity Python toolkit
910	  plan_id: plan_010
911	  description: 'Open-source Python 包：用户输入 DAG + confusion matrix + downstream estimate
912	    →
913	
914	    输出 bias expressions + ASV bounds + sensitivity curves + correction recommendation
915	
916	    + diagnostic plots。pip-installable，每个 topology 一个 worked example。
917	
918	    '
919	  expected_results:
920	    pip_installable: true
921	    supported_topologies: 6
922	    K_range_supported: 2–15
923	    runtime_K3: <0.1s
924	    runtime_K7: <1s
925	    runtime_K15: <10s
926	    worked_examples: 6
927	    api_surface: BiasExpr, ASV, CorrectionGuide, DiagnosticPlot
928	    test_coverage: ~85%
929	    documentation_pages: ~20
930	    demo_value_assessment: limited by diagonal-dominant empirical C
931	  result_rationale: 'Toolkit 是 engineering deliverable 而非实验。在 worst 档下，toolkit 本身功能完整
932	
933	    但 demonstration value 受限：经验混淆矩阵太 diagonal-dominant，toolkit 在 demo 中
934	
935	    主要输出 "your annotation is fine"——不够 compelling 作为 conference demo。
936	
937	    Worked examples 需要用 semi-synthetic C 而非 pure empirical C 来展示
938	
939	    toolkit 的 full capability（包括 reversal detection, ASV fragility warning, etc.）。
940	
941	    Runtime 快（K≤7 < 1s）因为 bias expressions 是 closed-form matrix operations，
942	
943	    不需要 MC simulation。K=15 需要 ~10s 因为 15×15 矩阵的 eigendecomposition
944	
945	    和 worst-case optimization 增加计算量。
946	
947	    作为 Claim 3 ("correction guidance") 的 tangible artifact，toolkit 增加论文的
948	
949	    practical impact——即使理论贡献在 worst 档下被削弱，一个 pip-installable tool
950	
951	    是 reviewer 认可的 concrete contribution。
952	
953	    '
954	  tables: []
955	  figures_description:
956	  - 'Fig 19: Toolkit workflow diagram — input (DAG graph + C matrix + β̂) → 4 outputs
957	    (bias expression + ASV + sensitivity curve + correction recommendation)。展示 API
958	    的 end-to-end flow。'
959	  - 'Fig 20: Toolkit screenshot — 对 protest/Qwen case (ASV=2.3) 的实际输出截图，包括 sensitivity
960	    curve plot 和 correction recommendation。'
961	  analysis: 'Toolkit 在 worst 档下是 "保底贡献"——即使 taxonomy 不够 dramatic、ASV 有 coverage 问题、
962	
963	    correction framework 主要推荐 MLA，一个 well-documented open-source tool 仍有独立价值。
964	
965	    建议在论文中给 toolkit 一个 dedicated subsection（不只是 "code available at github"），
966	
967	    展示 API 设计和 worked examples。在 supplementary material 中包含
968	
969	    comprehensive tutorial notebook。'
970	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45e60c74-972e-4edd-bb2a-f509ce8fb774",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "72f8ad55-c83c-4891-baf1-ed6844d87268",
  "sourceToolAssistantUUID": "45e60c74-972e-4edd-bb2a-f509ce8fb774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-20T08:58:01.574Z_

Now I have a thorough understanding of the paper, its claims, the underlying experiments (both completed MVP and planned), and the dream simulation results across best/median/worst scenarios. Let me also check if there's a mistakes.yaml for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72f8ad55-c83c-4891-baf1-ed6844d87268",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYWF3JZbs5zhiZsQ5zy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "513c75c6-9047-4e5c-8dd3-e91f9f11ae96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vuf4VYRkuPGcBDkVfTasE4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 58700,
      "cache_read_input_tokens": 56386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 58700,
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

_source line 47 · 2026-05-20T08:58:02.434Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016fUnxyms9h8HmUNfTkBWXG`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "mistakes.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "513c75c6-9047-4e5c-8dd3-e91f9f11ae96",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYWF3JZbs5zhiZsQ5zy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85065ffb-ca55-45a9-8aa4-814fc779cb0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vuf4VYRkuPGcBDkVfTasE4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 58700,
      "cache_read_input_tokens": 56386,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 58700
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 56386,
          "cache_creation_input_tokens": 58700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 58700,
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

_source line 48 · 2026-05-20T08:58:02.443Z_

<details><summary>↩ Tool result · `toolu_016fUnxyms9h8HmUNfTkBWXG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/mistakes.yaml\", \"content\": \"_next_id: 3\\nmistakes:\\n- id: M001\\n  date: '2026-05-20'\\n  category: experiment_design\\n  severity: medium\\n  summary: MVP criterion 2 混淆了 confounder misclassification 与 exposure misclassification\\n    的 \\\"bias toward null\\\" 保证\\n  root_cause: '\\\"Bias toward null\\\" 经典结论（Bross 1954）特指 exposure 误分类，不适用于 confounder\\n    误分类。MVP 测试的 confounding DAG 中 A 是 confounder，即使二分类非差异性误分类也产生远离零偏差（residual confounding）。因此\\n    criterion 2（\\\"≥1 种非差异性 C 产生远离零偏差\\\"）在 confounding DAG 下对二分类也成立——不具区分力。'\\n  prevention: 设计 pass criteria 时必须明确测试场景与被验证理论的对应关系。\\\"Bias toward null\\\" 的正确测试场景是 exposure\\n    misclassification DAG（A→Y，用 A* 估计 A 的因果效应），而非 confounder misclassification DAG（A→T,\\n    A→Y）。\\n  status: active\\n  context: Reviewer 在 MVP 验证报告中指出。MVP 仍通过 criterion 1（框架正确性）和 criterion 3（折叠不等价），但\\n    criterion 2 需在 exposure DAG 中补充验证。\\n  fix: 立即在 exposure misclassification DAG 上运行 K=3 验证，作为 research 阶段第一个实验。\\n  related_decisions:\\n  - D001\\n- id: M002\\n  date: '2026-05-20'\\n  category: agent_behavior\\n  severity: medium\\n  summary: MVP 两个验证实验未注册到 registry（Reviewer 第三次提醒）\\n  root_cause: Agent 执行 MVP 时未将 confounding DAG 和 exposure DAG 实验注册到 registry，仅生成了\\n    artifacts。Director 在审批指令中也未明确要求 registry 注册。\\n  prevention: 1. Director 下发实验指令时明确包含\\\"完成后注册到 registry\\\"要求。2. Agent 完成任何实验后必须自动注册（spec\\n    + status + conclusion + metrics）。\\n  status: active\\n  context: Reviewer 在 MVP 设计审查、MVP 结果验证、ROADMAP 更新审查中三次提到 registry 为空。\\n  fix: 指令 Agent 立即补录两个 MVP 实验到 registry。\\n\", \"total_chars\": 1412, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85065ffb-ca55-45a9-8aa4-814fc779cb0d",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "1ea086c7-6ca4-4f76-bfa0-922e1a94b2c6",
  "sourceToolAssistantUUID": "85065ffb-ca55-45a9-8aa4-814fc779cb0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-20T08:58:05.030Z_

Now I have comprehensive understanding of the paper. Let me write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ea086c7-6ca4-4f76-bfa0-922e1a94b2c6",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYX7Z8DD1hQF8Xi5Joe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6119bc43-9a4f-4e5d-928f-f7cd17187a9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmpEPqPcPuzHPYRnCaxZgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 115086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1029,
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

_source line 50 · 2026-05-20T08:58:05.701Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WvEcjeWhmaCmpeGjcTFEMW`</summary>

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
  "parentUuid": "6119bc43-9a4f-4e5d-928f-f7cd17187a9b",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYX7Z8DD1hQF8Xi5Joe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f387520-6b57-4869-9e5d-a74a79fe60b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmpEPqPcPuzHPYRnCaxZgE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 115086,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1029
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 105,
          "cache_read_input_tokens": 115086,
          "cache_creation_input_tokens": 1029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1029,
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

_source line 51 · 2026-05-20T08:58:05.704Z_

<details><summary>↩ Tool result · `toolu_01WvEcjeWhmaCmpeGjcTFEMW`</summary>

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
  "parentUuid": "7f387520-6b57-4869-9e5d-a74a79fe60b9",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "da300c59-a624-4ed1-8ff0-ef80679a00ce",
  "sourceToolAssistantUUID": "7f387520-6b57-4869-9e5d-a74a79fe60b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-20T08:58:09.218Z_



Now let me compose my detailed review based on everything I've read.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da300c59-a624-4ed1-8ff0-ef80679a00ce",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYXMXkndHbcfBZ54P9W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dca94b93-5487-45cf-95d3-f436bea2d62d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4GSbcxvLwa3mp9X7ACegS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 116115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 729,
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

_source line 53 · 2026-05-20T08:59:43.447Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01XWjnTHuLLKDbargRW8gpHr`</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "tier": "worst",
  "dream_id": "dream_20260520T074549",
  "overall_score": "Weak Reject (3)",
  "report": "# Reviewer R1 — Methods & Experiments Focus\n\n## 1. Summary\n\nThis paper characterizes how multi-class (K>=3) annotation errors from LLM annotators propagate bias through 6 canonical DAG topologies used in computational social science. The key theoretical finding is that non-differential exposure misclassification breaks the classical binary \"bias toward null\" guarantee (85% reversal rate under uniform Dirichlet prior), while the remaining 5 topologies preserve bias direction. The paper proposes Annotation Sensitivity Values (ASVs) analogous to E-values for unmeasured confounding, and a correction guidance framework mapping {topology x error structure x ASV} to correction methods. Empirical validation uses 3 LLMs x 3 CSS tasks (~270K annotations).\n\n## 2. Strengths\n\n- **Theoretically well-motivated problem.** The gap between binary measurement error theory and multi-class LLM annotation practice is real and under-studied. The paper correctly identifies that Brenner (1993), Veierod & Laake (2001), and Lee & Wood-Doughty (2024) leave this space largely uncharted for general DAG topologies. The positioning relative to these prior works is precise and honest.\n\n- **Strong core finding for exposure topology.** The 85% violation rate for exposure misclassification under K=3, validated by both closed-form theory and 100K random C search with MC confirmation, is a compelling result. The mechanism (near-permutation C causes label swap that structurally cannot occur in K=2) is clearly explained, and the contrast with confounding DAG (0% violation, monotonic toward OVB) effectively demonstrates topology-dependence.\n\n- **Dirichlet subspace analysis adds practical relevance.** Stratifying violation rates by diagonal dominance (diag>=0.9 still shows 11.9% amplification) is a smart addition that preempts the obvious reviewer objection that \"real LLM confusion matrices are diagonal-dominant, so the 85% rate is misleading.\" The finding that sign reversal vanishes at high accuracy but amplification persists at ~12% is nuanced and practically relevant.\n\n- **ASV concept is well-conceived.** The analogy to E-values is natural and fills a genuine gap. For confounding topology, the formal monotonicity + sharpness proof with constructive C* is clean theoretical work.\n\n- **Comprehensive scope.** Covering 6 topologies x multiple K values x 3 correction methods x empirical validation is ambitious. The explicit identification of 12% of scenarios where no existing method suffices is a valuable honest contribution.\n\n- **Open-source toolkit.** A pip-installable package supporting K=2-15 across 6 topologies lowers the barrier to adoption and is a concrete practical contribution.\n\n## 3. Weaknesses\n\n### Major\n\n- **(W1) Theory-MC match rate of 76% (32/42) is concerning.** Nearly a quarter of topology-structure combinations show theory-MC mismatch. The mismatches concentrate in complex topologies (collider 4/6, M-bias 4/6, front-door 3/6) with extreme C structures. If the closed-form bias expressions fail to predict MC outcomes for these topology-C combinations, the theoretical taxonomy's reliability is undermined precisely where it would be most needed (unfamiliar, complex DAGs). The paper needs to clearly delineate where the theory is an approximation vs. exact, and whether these mismatches reflect (a) finite-sample MC issues or (b) genuine theoretical approximation errors. If the former, increasing N should resolve them; if the latter, the bias \"expressions\" for front-door and M-bias are better described as conjectures. The MVP code uses N=10,000 and M=1,000 — for complex topologies with conditioning or ratio estimators, this may be insufficient.\n\n- **(W2) ASV formal properties are incomplete and heterogeneous.** The paper claims formal monotonicity + sharpness for confounding but only monotonicity (no sharpness) for mediation (1.4-1.8x conservative), monotonicity failures for collider (7% of C structures), and monotonicity failures for front-door (3%). This means the ASV framework has different reliability guarantees across topologies, yet the paper presents it as a unified framework. Coverage at 95% nominal is only 0.85 aggregate — a 10% gap from nominal. This is below the standard for a sensitivity analysis tool that practitioners would use for decision-making. Collider coverage at 0.78 is particularly problematic. The heterogeneity of formal properties across topologies significantly weakens Claim 2.\n\n- **(W3) Empirical validation is too benign to stress-test the framework.** All 9 empirical confusion matrices are diagonal-dominant (0.74-0.87). No direction reversal is observed. 5/9 ASV values are trivially robust (>50), leaving only 4 meaningful cases for calibration. The theoretical contributions — reversal taxonomy, ASV fragility detection — are designed for scenarios that the empirical data never actually reaches. This creates a disconnect: the theory warns about dangerous regimes, but the experiments only validate the theory in the safe regime. Semi-synthetic experiments (injecting controlled degradation into empirical C) or additional low-accuracy tasks would be needed to validate the framework where it matters most.\n\n- **(W4) Correction guidance framework has limited discriminative value.** At 78% accuracy with a 65% MLA-recommendation fraction, the framework only exceeds the trivial \"always recommend MLA\" baseline by 13 percentage points. This marginal improvement may not justify the complexity of the framework. The paper should report the improvement over the trivial baseline explicitly and discuss whether the framework's value is primarily in the 35% non-MLA scenarios (particularly exposure reversal and no-method-adequate regimes).\n\n### Minor\n\n- **(W5) Binarization analysis is incomplete for K=5,7.** Table 4 reports K=5,7 only for confounding (max delta 0.091). The remaining 5 topologies are reported only at K=3. Since the paper's argument is that multi-class treatment is necessary, showing binarization harm at higher K across all topologies would strengthen this claim. As reported, the binarization deltas (0.038-0.091) are modest relative to typical CSS effect sizes (0.1-0.3), weakening the \"binarization is hazardous\" argument.\n\n- **(W6) DGP sensitivity.** All theoretical and MC results use a single DGP parameterization per topology (e.g., P(A)=[0.4, 0.35, 0.25], beta=[0, 1.0, -0.5] for exposure). The 85% reversal rate, the subspace analysis, and other quantitative claims may be sensitive to these choices. A robustness check across multiple DGP parameterizations (different P(A) distributions, different beta magnitudes and signs) is needed to establish that the qualitative findings are not artifacts of the chosen parameters.\n\n- **(W7) Eigendecomposition interpretability degrades for complex topologies.** Table 3 shows that for collider at K=7, the dominant eigenvalue captures only 49% of variance, requiring 4 modes for 90%. The paper proposes eigendecomposition as an interpretability tool for general K, but this tool is effective only for topologies with clean spectral structure (confounding, exposure). This limitation should be stated explicitly as a scope condition rather than presenting eigendecomposition as a general solution.\n\n- **(W8) Inter-model error correlation analysis is descriptive only.** The kappa=0.58-0.67 finding confirms Kim et al. (ICML 2025) but the paper does not formally incorporate error dependence into the bias expressions or ASV framework. The correction framework identifies correlated multi-LLM correction as an open problem (within the 12% no-method-adequate regime), but the gap between acknowledging the problem and providing a solution is large.\n\n- **(W9) Missing formal definition of \"non-differential\" for K>=3.** The binary definition of non-differential misclassification (P(A*|A,Y) = P(A*|A)) extends straightforwardly, but the paper should explicitly state whether \"non-differential\" means C is constant across all other variables in the DAG, or just the outcome. Different definitions lead to different bias expressions, and the distinction matters more in multi-class settings where differential error can take richer forms.\n\n## 4. Questions for Authors\n\nQ1. For the 10 theory-MC mismatches (Table 2), can you report whether increasing N from 10K to 50K or 100K resolves the discrepancy? This would distinguish finite-sample MC variance from genuine theoretical approximation error.\n\nQ2. For the collider ASV monotonicity violations (7% of C structures): what is the maximum magnitude of the non-monotonicity (i.e., max decrease in ASV as delta increases)? If the violations are small in absolute terms, they may be practically tolerable. If large, the ASV is unreliable for collider topologies.\n\nQ3. The 85% reversal rate uses Dirichlet(1,1,1) uniform prior. How sensitive is this to the Dirichlet concentration parameter? Alpha=1 gives uniform; alpha=5 would concentrate mass near the center of the simplex (moderate accuracy). Reporting reversal rates under alpha=2,5,10 would map out the full landscape.\n\nQ4. The correction framework recommends \"no existing method adequate\" for 12% of scenarios. For these scenarios, what is the magnitude of residual bias after applying the best available (even if inadequate) correction? If the residual bias is small, the practical impact of the gap is limited.\n\nQ5. Can you provide confidence intervals on the 78% correction framework accuracy? With the reported number of MC scenarios, what is the standard error?\n\nQ6. For the spectral predictor (lambda_2/lambda_1 > 0.6 predicts exposure reversal, AUC=0.92): is this threshold stable across different DGP parameterizations, or does it depend on P(A) and beta?\n\n## 5. Missing Experiments or Analyses\n\n1. **DGP robustness sweep.** Vary P(A) (uniform, skewed, extreme), beta magnitudes (small, medium, large), and noise variance across all 6 topologies. Report whether the qualitative taxonomy (which topologies show reversal) is invariant, and how quantitative measures (violation rates, ASV values) shift.\n\n2. **Semi-synthetic stress tests.** Starting from the 9 empirical confusion matrices, systematically degrade them (increase off-diagonal mass) and track when theoretical predictions (direction reversal, ASV fragility) activate. This bridges the gap between the theory's dramatic predictions and the empirical data's benign reality.\n\n3. **Multiple binarization schemes.** The current analysis uses a single folding scheme ({0} vs {1,2}). Different folding choices can produce different binarization deltas. Report the max-over-foldings delta to give the worst-case binarization harm.\n\n4. **ASV calibration with known ground truth.** Generate synthetic data where the true ASV is known by construction, and verify that the estimated ASV matches. This is a more direct validation than coverage analysis.\n\n5. **Comparison with VanderWeele & Li (2019).** For K=2 special cases, verify that ASVs reduce to the VanderWeele-Li sensitivity bounds. This provides a consistency check and connects to the established literature.\n\n6. **Larger empirical validation.** The current 3 tasks x 3 models design yields only 9 data points for ASV calibration, of which only 4 are meaningful. Adding 1-2 additional tasks (especially a high-K, low-accuracy task like fine-grained emotion detection K=6-8 or low-resource language annotation) would substantially improve the empirical evidence base.\n\n7. **Statistical tests for theory-MC agreement.** Beyond checking whether theoretical values fall in MC 95% CIs, report formal goodness-of-fit statistics (e.g., chi-squared test of theory vs. MC distribution) to more rigorously assess match quality.\n\n## 6. Preliminary Score: 3 (Weak Reject)\n\n**Justification:**\n\nThe paper tackles an important and timely problem at the intersection of LLM annotation quality and causal inference methodology. The core theoretical insight — that exposure misclassification uniquely breaks binary guarantees under K>=3 — is novel and well-validated for that specific topology. The ASV concept is a natural and useful contribution.\n\nHowever, several issues prevent acceptance at a top venue:\n\n(a) The theory-MC match rate of 76% means the closed-form expressions are unreliable for nearly a quarter of the claimed coverage space — precisely the complex topologies (collider, M-bias, front-door) where practitioners most need guidance. The paper over-claims the generality of its \"taxonomy\" when the theoretical foundation is solid only for confounding and exposure.\n\n(b) The ASV framework lacks uniform formal guarantees: monotonicity fails for 2/6 topologies, sharpness is proved for only 1/6, and aggregate coverage is 10 points below nominal. For a sensitivity analysis tool positioned as analogous to E-values, this heterogeneity is a significant limitation.\n\n(c) The empirical validation operates entirely in the safe regime (diagonal-dominant C, no observed reversals, mostly trivially robust ASVs), failing to stress-test the theoretical contributions where they would be most valuable.\n\n(d) The correction framework's marginal value over \"always recommend MLA\" is modest (13 percentage points).\n\nThe paper would benefit from: (i) increasing MC sample sizes to resolve theory-MC mismatches, (ii) adding semi-synthetic stress tests, (iii) restricting ASV claims to topologies where formal properties hold, and (iv) a DGP robustness analysis. With these revisions, the paper could be a strong contribution, but in its current form the gap between ambitious claims and actual evidence is too wide.\n\n## 7. Confidence: 4/5\n\nI have strong familiarity with measurement error in causal inference, sensitivity analysis frameworks (E-values, Rosenbaum bounds), and DAG-based bias analysis. I am less familiar with the specific correction methods (DSL, PPI) and their computational properties, which slightly limits my assessment of Claim 3. I carefully reviewed the MVP code and experimental design documents.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dca94b93-5487-45cf-95d3-f436bea2d62d",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYXMXkndHbcfBZ54P9W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a867fa2a-3527-413d-95bf-41b2c232bae2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4GSbcxvLwa3mp9X7ACegS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 116115,
      "output_tokens": 3541,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 729
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3541,
          "cache_read_input_tokens": 116115,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 729,
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

_source line 54 · 2026-05-20T08:59:47.034Z_

<details><summary>↩ Tool result · `toolu_01XWjnTHuLLKDbargRW8gpHr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/review_report.md\", \"dream_id\": \"dream_20260520T074549\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a867fa2a-3527-413d-95bf-41b2c232bae2",
  "isSidechain": true,
  "promptId": "7d89afd0-b200-4ce8-96e9-d6a2932f3a6a",
  "agentId": "a3d9dc7c1ad2f4c98",
  "type": "user",
  "uuid": "86a7b777-0f29-4f68-aa99-7cf715387e09",
  "sourceToolAssistantUUID": "a867fa2a-3527-413d-95bf-41b2c232bae2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-20T08:59:57.937Z_

Review submitted successfully. Here is a summary of what was done:

**Submitted:** Detailed R1 review (Methods & Experiments focus) for the "worst" tier of dream simulation `dream_20260520T074549`.

**Score:** 3 (Weak Reject) with Confidence 4/5.

**Key findings in the review:**

**Strengths identified:**
- Well-motivated problem with precise positioning against prior work (Brenner 1993, Lee & Wood-Doughty 2024)
- Strong core finding: 85% exposure reversal rate under K=3, validated by theory + MC + Dirichlet subspace analysis
- ASV concept is natural (E-value analogy) with clean formal proof for confounding
- Ambitious scope (6 topologies, general K, correction framework, open-source toolkit)

**Major weaknesses identified:**
1. Theory-MC match rate of 76% (32/42) undermines the generality of the taxonomy -- front-door at 3/6 match is particularly concerning
2. ASV formal properties are heterogeneous across topologies: monotonicity fails for collider (7%) and front-door (3%), sharpness proved only for confounding, aggregate 95% coverage is only 0.85
3. Empirical validation is entirely in the safe regime -- all C matrices are diagonal-dominant, no reversals observed, 5/9 ASVs are trivially robust, leaving only 4 meaningful calibration points
4. Correction framework's 78% accuracy is only 13 points above the trivial "always MLA" baseline (65%)

**Critical missing experiments:** DGP robustness sweep, semi-synthetic stress tests bridging theory-to-practice gap, multiple binarization folding schemes, larger empirical validation with high-K low-accuracy tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86a7b777-0f29-4f68-aa99-7cf715387e09",
  "isSidechain": true,
  "agentId": "a3d9dc7c1ad2f4c98",
  "requestId": "req_011CbDYepdN9y8RcR929RiVT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b02a4a08-55e6-42f6-8f5a-2a7b6b432a8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "045397bc-4678-4c04-b09d-1cdc407a641d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUAGFsWsYeM5MjwmCpXN3n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3671,
      "cache_read_input_tokens": 116844,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3671,
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
