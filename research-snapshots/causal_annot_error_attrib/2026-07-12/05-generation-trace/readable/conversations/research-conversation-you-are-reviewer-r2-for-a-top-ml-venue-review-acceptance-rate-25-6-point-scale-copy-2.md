# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-acd414964c7e72df6.jsonl`
- **Structured JSON:** [`bf16d2d49a928f5ac744.json`](../../sessions/bf/bf16d2d49a928f5ac744.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-20T08:49:28.577Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus is **novelty and related work**.

## Paper Summary

**Title:** "Multi-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies"

The paper develops a systematic framework for analyzing multi-class annotation error propagation in causal inference. Three contributions:
1. **Multi-class bias taxonomy**: Closed-form bias expressions for K=3 and matrix-form for general K across 6 DAG topologies (confounding, exposure, mediation, collider, instrument, front-door). Key finding: direction reversal is topology-specific — exposure produces pervasive reversal (85%), mediation conditional reversal (23%), four others preserve monotonicity.
2. **Annotation Sensitivity Values (ASVs)**: Analogous to E-values for unmeasured confounding. Monotonicity proved for all 6 topologies. Sharpness formally proved for confounding and mediation, numerical evidence (89–94%) for the other four. Average 95%-nominal coverage = 0.907.
3. **Correction guidance framework**: Maps {topology × error structure × ASV} → correction method (DSL, PPI, MLA, naive plug-in, or "no method adequate"). 89% accuracy across 90 MC scenarios.

Empirical validation: 3 CSS tasks (protest K=5, stance K=3, toxicity K=2) × 3 LLMs (Llama 4 Maverick, Qwen 3.5 Plus, DeepSeek V4), ~270K annotations. ASV concordance 7/9. Inter-model error agreement ~61%.

## Related Work as Presented in Paper (Section 2)

Three paragraphs:

**Measurement error in causal inference:**
- Classical: Bross (1954) — binary non-differential misclassification attenuates. Carroll et al. (2006) — textbook.
- Polytomous: Brenner (1993) — polytomous confounder misclassification can bias in either direction, no systematic characterization.
- VanderWeele and Li (2019) — sensitivity bounds for binary risk ratios.
- Paper's claim: "first systematic multi-class treatment across six DAG topologies"

**Text classification errors in CSS:**
- Wood-Doughty et al. (2018) — DAG reasoning about text classifier errors, binary only, no formal bias theorems.
- TeBlunthuis et al. (2024) — MLA correction for binary classifiers.
- Lee and Wood-Doughty (2024) — extended to categorical LLM classifiers, one DAG topology (unobserved confounding), one dataset (MIMIC).
- Paper's claim: "covers six topologies with a systematic taxonomy, sensitivity analysis, and correction guidance"

**LLM annotation quality:**
- Ziems et al. (2024), Jerzak et al. (2025) — benchmarking.
- Kim et al. (2025) — cross-model error correlations ~60%.
- Paper's claim: "provides the diagnostic layer that tells researchers which error structures are dangerous given their specific causal design"

**References list** (11 total): Baumann 2025, Brenner 1993, Bross 1954, Carroll et al. 2006, Hernán & Cole 2009, Jerzak et al. 2025, Kim et al. 2025, Lee & Wood-Doughty 2024, TeBlunthuis et al. 2024, VanderWeele & Li 2019, Wood-Doughty et al. 2018, Ziems et al. 2024.

## Key Claims to Evaluate for Novelty

1. "First systematic multi-class treatment across six DAG topologies" — Is this truly novel vs Brenner 1993, Carroll et al. 2006, VanderWeele & Li 2019?
2. "Direction reversal is topology-specific" — Is this a genuinely new finding or well-known?
3. ASVs as analogous to E-values — How novel is this adaptation? VanderWeele & Li 2019 already did sensitivity bounds for measurement error.
4. Correction guidance framework — How novel vs Jerzak et al. 2025 benchmarking?
5. The exposure–mediation contrast as "core theoretical contribution"

## Your Task

Provide a detailed review focusing on:
1. **Novelty assessment**: How original are the three contributions? What is truly new vs incremental extension of existing work?
2. **Related work completeness**: Are there missing references? Is the positioning fair and accurate?
3. **Claims vs evidence**: Are the novelty claims supported?
4. **Significance**: Would this paper change how researchers practice? Is the impact sufficient for a top venue?
5. **Framing and positioning**: Is the paper well-framed for the ML/NLP audience?

Consider these potentially missing references:
- Hernán & Cole (2009) is cited but only in references — how is it used?
- Epidemiology literature on polytomous exposure misclassification (beyond Brenner 1993)
- Recent work on PPI (prediction-powered inference) by Angelopoulos et al. (2023)
- Sensitivity analysis literature beyond E-values (Rosenbaum bounds, Ding & VanderWeele)
- SIMEX and regression calibration for measurement error
- Differential misclassification literature

Output format:
```
## R2 Review: Novelty and Related Work

### Summary
[2-3 sentences]

### Strengths
S1. ...
S2. ...
...

### Weaknesses
W1. ...
W2. ...
...

### Questions for Authors
Q1. ...
Q2. ...
...

### Minor Issues
M1. ...
...

### Missing References
[List specific papers/areas that should be cited and discussed]

### Novelty Assessment
[Detailed breakdown of what is genuinely new vs. incremental]

### Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "e63a1040-ae66-47ab-aa1a-498d723a4abb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T08:49:28.581Z_

```json
{
  "parentUuid": "e63a1040-ae66-47ab-aa1a-498d723a4abb",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
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
  "uuid": "140b0521-950a-40ce-8e67-28fb142404bf",
  "timestamp": "2026-05-20T08:49:28.581Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T08:49:32.075Z_



I'll start by reading the project's key files to understand the full context of this paper before writing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "140b0521-950a-40ce-8e67-28fb142404bf",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXsENLng733eJnzRkeo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9707943-b3e0-4852-bd8a-20fe487181c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011iZCBKPDr9ZYVKJKpbV9Kt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7799,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7799,
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

_source line 4 · 2026-05-20T08:49:32.231Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017ScAC6x9ywcnZFi247zWAi`</summary>

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
  "parentUuid": "e9707943-b3e0-4852-bd8a-20fe487181c6",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXsENLng733eJnzRkeo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11d42321-7337-4ec2-be0e-886bb4a7b7e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011iZCBKPDr9ZYVKJKpbV9Kt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7799,
      "cache_read_input_tokens": 8250,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7799
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 112,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7799,
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

_source line 5 · 2026-05-20T08:49:32.234Z_

<details><summary>↩ Tool result · `toolu_017ScAC6x9ywcnZFi247zWAi`</summary>

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
  "parentUuid": "11d42321-7337-4ec2-be0e-886bb4a7b7e0",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "63ac9a79-8d7f-41ec-aedc-38412694431d",
  "sourceToolAssistantUUID": "11d42321-7337-4ec2-be0e-886bb4a7b7e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T08:49:35.793Z_



Let me read the key project files to get full context on the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63ac9a79-8d7f-41ec-aedc-38412694431d",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXsWJo1W2xtuUP6pU2m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c38f5cd-bc71-485d-8e56-7b7d144e9197",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzpK8jmNXayMsLLAdU4pnU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 16049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1294,
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

_source line 7 · 2026-05-20T08:49:36.267Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FF7SGrMamcNYLTNEhoY2Bn`</summary>

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
  "parentUuid": "5c38f5cd-bc71-485d-8e56-7b7d144e9197",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXsWJo1W2xtuUP6pU2m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa9d7134-e076-4009-92fc-b7aa46ab64dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzpK8jmNXayMsLLAdU4pnU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 16049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1294,
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

_source line 8 · 2026-05-20T08:49:36.279Z_

<details><summary>↩ Tool result · `toolu_01FF7SGrMamcNYLTNEhoY2Bn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_exposure_dirichlet_subspace** (success): Dirichlet(1,1,1) 均匀先验下 85% 违反率在高对角占优子空间（min(diag(C))≥0.7，接近真实 LLM 精度）是否骤降：若 >10% 则论文 claim 对实际 LLM 有现实意义，若 <1% 需标注适用范围\\n- **mvp_exposure_dag** (success): K=3 非差异性 exposure 误分类打破二分类 bias-toward-null 保证：存在 C 结构使 treatment effect 估计产生符号反转或效应放大，而 K=2 下非差异性误分类始终保证衰减\\n- **mvp_confounding_dag** (success): K=3 混淆矩阵下 confounding DAG 的 OLS 偏差可由 plim=(E[Z'Z])^{-1}E[Z'X]β 精确预测，且 K=3 偏差与二分类折叠偏差系统性不同（多分类保留更多混杂信息）\\n\\n## 趋势\\n成功 3 / 负向 0 / 失败 0 / 共 3\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nhome-1x5090: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 652, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa9d7134-e076-4009-92fc-b7aa46ab64dd",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "27a56ba8-dc85-4048-9708-1b113c44137c",
  "sourceToolAssistantUUID": "fa9d7134-e076-4009-92fc-b7aa46ab64dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T08:49:37.453Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014e2aVachpbXAaGUYU21HHR`</summary>

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
  "parentUuid": "27a56ba8-dc85-4048-9708-1b113c44137c",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXsWJo1W2xtuUP6pU2m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e165691-f55c-4c71-885d-36a40007fdf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzpK8jmNXayMsLLAdU4pnU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 16049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1294,
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

_source line 10 · 2026-05-20T08:49:37.463Z_

<details><summary>↩ Tool result · `toolu_014e2aVachpbXAaGUYU21HHR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/literature_map.yaml\", \"content\": \"papers:\\n  wood_doughty2018:\\n    title: \\\"Challenges of Using Text Classifiers for Causal Inference\\\"\\n    authors: [\\\"Wood-Doughty, Z.\\\", \\\"Shpitser, I.\\\", \\\"Dredze, M.\\\"]\\n    year: 2018\\n    venue: \\\"EMNLP\\\"\\n    category: \\\"causal-text-classification\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"First to apply DAG reasoning to text classifier measurement error; no formal bias theorems or identifiability conditions; binary only. Direct predecessor — our work extends to multi-class with formal bias expressions.\\\"\\n    abstract: \\\"Applies causal DAG reasoning to analyze how text classifier errors propagate to downstream causal estimates. Proposes matrix adjustment correction but notes severe instability.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    arxiv_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  teblunthuis2024:\\n    title: \\\"Misclassification in Automated Content Analysis Causes Bias in Regression. Can We Fix It? Yes We Can!\\\"\\n    authors: [\\\"TeBlunthuis, N.\\\", \\\"Hase, V.\\\", \\\"Chan, C.\\\"]\\n    year: 2024\\n    venue: \\\"Communication Methods and Measures\\\"\\n    category: \\\"causal-text-classification\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Most complete binary treatment: 4 DAG scenarios (differential/non-differential × IV/DV), testable conditions, MLA method. But binary only, single classifier. Our work generalizes to multi-class K×K confusion matrices.\\\"\\n    abstract: \\\"Provides four DAG scenarios for text classifier measurement error with likelihood ratio tests and Maximum Likelihood Adjustment (MLA) correction for binary classification.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    arxiv_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  hernan_cole2009:\\n    title: \\\"Causal Diagrams and Measurement Bias\\\"\\n    authors: [\\\"Hernán, M.A.\\\", \\\"Cole, S.R.\\\"]\\n    year: 2009\\n    venue: \\\"American Journal of Epidemiology\\\"\\n    doi: \\\"10.1093/aje/kwp293\\\"\\n    category: \\\"measurement-error-epidemiology\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Formalizes starred-node DAGs with differential/non-differential and independent/dependent error taxonomy. Core theoretical foundation for our DAG-based framework.\\\"\\n    abstract: \\\"Formalizes the use of causal DAGs for reasoning about measurement bias, introducing starred-node notation and taxonomy of error types.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  vanderweele_li2019:\\n    title: \\\"Simple Sensitivity Analysis for Differential Measurement Error\\\"\\n    authors: [\\\"VanderWeele, T.J.\\\", \\\"Li, Y.\\\"]\\n    year: 2019\\n    venue: \\\"American Journal of Epidemiology\\\"\\n    doi: \\\"10.1093/aje/kwz062\\\"\\n    category: \\\"sensitivity-analysis\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Provides sensitivity bounds for differential measurement error using risk ratios, but only for binary exposure/outcome. Our ASV framework extends this to multi-class confusion matrices.\\\"\\n    abstract: \\\"Develops simple sensitivity analysis techniques for differential measurement error in binary exposure/outcome settings using risk ratios.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  vanderweele_ding2017:\\n    title: \\\"Sensitivity Analysis in Observational Research: Introducing the E-Value\\\"\\n    authors: [\\\"VanderWeele, T.J.\\\", \\\"Ding, P.\\\"]\\n    year: 2017\\n    venue: \\\"Annals of Internal Medicine\\\"\\n    doi: \\\"10.7326/M16-2607\\\"\\n    category: \\\"sensitivity-analysis\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Introduces E-values for unmeasured confounding — the sensitivity analysis paradigm our ASVs mirror for annotation-induced bias.\\\"\\n    abstract: \\\"Proposes the E-value as an interpretable sensitivity analysis measure for unmeasured confounding in observational studies.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  brenner1993:\\n    title: \\\"Bias due to non-differential misclassification of polytomous confounders\\\"\\n    authors: [\\\"Brenner, H.\\\"]\\n    year: 1993\\n    venue: \\\"Journal of Clinical Epidemiology\\\"\\n    doi: \\\"10.1016/0895-4356(93)90148-T\\\"\\n    category: \\\"measurement-error-epidemiology\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Key result: non-differential misclassification of polytomous confounders can bias in EITHER direction — breaks the binary 'toward null' guarantee. Core motivation for our multi-class taxonomy.\\\"\\n    abstract: \\\"Analyzes bias from non-differential misclassification of polytomous confounders, showing bias can go in either direction unlike the binary case.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  veirod_laake2001:\\n    title: \\\"Exposure misclassification: bias in category specific Poisson regression coefficients\\\"\\n    authors: [\\\"Veierød, M.B.\\\", \\\"Laake, P.\\\"]\\n    year: 2001\\n    venue: \\\"Statistics in Medicine\\\"\\n    doi: \\\"10.1002/sim.900\\\"\\n    category: \\\"measurement-error-epidemiology\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Derives bias expressions for multi-category exposure misclassification in Poisson regression — bias depends on ALL true coefficients weighted by full misclassification matrix. We extend from regression-only to full DAG-based causal framework.\\\"\\n    abstract: \\\"Proves that multi-category exposure misclassification produces bias depending on all true category-specific coefficients weighted by the full misclassification probability matrix.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  baumann2025:\\n    title: \\\"Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation\\\"\\n    authors: [\\\"Baumann, M.\\\", \\\"Röttger, P.\\\", \\\"Urman, A.\\\", \\\"Wendsjö, S.\\\", \\\"Plaza-del-Arco, F.M.\\\", \\\"Gruber, N.\\\", \\\"Hovy, D.\\\"]\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2509.08825\\\"\\n    category: \\\"llm-annotation-quality\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Strongest empirical motivation: 37 tasks, 21 studies, 13M labels, 18 models — 31% incorrect downstream conclusions with SOTA LLMs. Coins 'LLM hacking'. Diagnoses the problem we solve.\\\"\\n    abstract: \\\"Demonstrates across 37 annotation tasks from 21 published social science studies that approximately 31% of hypotheses yield incorrect conclusions with SOTA LLMs, rising to 50% for smaller models.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  lee_wood_doughty2024:\\n    title: \\\"Categorical Variables and Measurement Error in Causal Inference with LLM Classifiers\\\"\\n    authors: [\\\"Lee, S.\\\", \\\"Wood-Doughty, Z.\\\"]\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2411.03004\\\"\\n    category: \\\"causal-text-classification\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Extends Wood-Doughty (2018) to categorical + LLM classifiers on MIMIC clinical data. But covers only 1 DAG topology (unobserved confounding), no bias taxonomy, no sensitivity analysis. Key differentiation target.\\\"\\n    abstract: \\\"Extends causal measurement error framework to categorical text classifiers and LLMs, applied to clinical NLP on MIMIC data.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  gligoric2025:\\n    title: \\\"Can Unconfident LLM Annotations Be Used for Confident Conclusions?\\\"\\n    authors: [\\\"Gligorić, K.\\\", \\\"Jurafsky, D.\\\", \\\"Zou, J.\\\"]\\n    year: 2025\\n    venue: \\\"NAACL\\\"\\n    category: \\\"llm-annotation-correction\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Notes correlated errors bias estimates, proposes DSL/PPI corrections. One of the correction methods our guidance framework evaluates.\\\"\\n    abstract: \\\"Investigates when LLM annotations with varying confidence can still yield valid downstream conclusions, proposing design-based supervised learning and prediction-powered inference corrections.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  messing2026:\\n    title: \\\"Hidden Measurement Error in LLM Pipelines\\\"\\n    authors: [\\\"Messing, S.\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2604.11581\\\"\\n    category: \\\"llm-annotation-quality\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Decomposes LLM pipeline variance via linear mixed models (item-judge interaction dominates at 44%). Explicitly excludes causal identification — the gap we fill.\\\"\\n    abstract: \\\"Decomposes variance in LLM annotation pipelines using linear mixed models, finding item-judge interaction dominates at 44%, but excludes causal identification.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\\n  kim_garg2025:\\n    title: \\\"Correlated Errors in Large Language Models\\\"\\n    authors: [\\\"Kim, J.\\\", \\\"Garg, S.\\\", \\\"Peng, Y.\\\", \\\"Garg, N.\\\"]\\n    year: 2025\\n    venue: \\\"ICML\\\"\\n    arxiv_id: \\\"2506.07962\\\"\\n    category: \\\"llm-annotation-quality\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Shows models agree 60% when both err, larger models have highly correlated errors across architectures. Undermines ensemble-as-fix assumption — strengthens case that error STRUCTURE analysis (our contribution) is irreplaceable.\\\"\\n    abstract: \\\"Demonstrates that LLM errors are highly correlated across models, with 60% agreement when both err, challenging independence assumptions in ensemble methods.\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n\", \"total_chars\": 8959, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e165691-f55c-4c71-885d-36a40007fdf3",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "8755aa48-5a7f-43bb-a1f9-63156b598387",
  "sourceToolAssistantUUID": "2e165691-f55c-4c71-885d-36a40007fdf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T08:49:37.902Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MMQ7nvfTzs1mvr1DZGxrku`</summary>

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
  "parentUuid": "8755aa48-5a7f-43bb-a1f9-63156b598387",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXsWJo1W2xtuUP6pU2m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea6ddeb5-e1eb-4025-93d7-2ebfbebc776b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzpK8jmNXayMsLLAdU4pnU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 16049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1294,
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

_source line 12 · 2026-05-20T08:49:37.911Z_

<details><summary>↩ Tool result · `toolu_01MMQ7nvfTzs1mvr1DZGxrku`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/paper_framing.md\", \"content\": \"# Paper Framing — causal_annot_error_attrib\\n\\n## Target Venue\\n- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)\\n- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)\\n- Tertiary: ICWSM 2027 Round 2 (2026-09-15)\\n\\n## Title\\nMulti-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies\\n\\n## Core Claims (3 条)\\n\\n1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 6 canonical social-science DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door).\\n\\n2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of differential annotation error needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Reported alongside estimates, analogous to E-values for unmeasured confounding. Formal proofs (monotonicity + sharpness) for 3 priority topologies; MC-validated conjectures for the remaining 3.\\n\\n3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI, MLA, naive plug-in), characterizing regimes where each applies and where no existing method suffices — including dependence-aware multi-LLM correction as an open problem.\\n\\n## Story Spine\\n\\n- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31% of downstream conclusions are already incorrect. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable.\\n\\n- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.\\n\\n- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.\\n\\n- **Headline result template**: \\\"Across 6 DAG topologies with K=3,5,7, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. On 3 CSS tasks annotated by 3 LLMs, ASVs provide calibrated robustness indicators, and our taxonomy identifies cases where commonly applied corrections would increase rather than decrease bias.\\\"\\n\\n## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001\\n\\n### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)\\nThe binary guarantee that \\\"non-differential exposure misclassification biases toward the null\\\" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification (\\\"bias can go in either direction\\\"); we provide the first systematic characterization across 6 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to \\\"escape\\\" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).\\n\\n### Version B (no direction reversal found across topologies)\\nMulti-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.\\n\\n**Gate**: plan_001 results determine which version. ≥2 topologies with reversal → A; 1 → A with that topology as lead; 0 → B. See D003.\\n\\n## MVP Evidence\\n\\n**Confounding DAG + K=3** (confounder misclassification):\\n- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated\\n- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization\\n- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is \\\"well-behaved\\\" (predictable direction)\\n- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.\\n\\n**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):\\n- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification\\n- K=2 control: 6/6 toward null (binary guarantee holds)\\n- Worst case: β=1.0 → estimate=-0.84 (sign reversal + 2.83x amplification)\\n- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)\\n- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim\\n\\n**Dirichlet subspace analysis** (practical relevance validation):\\n- diag≥0.5: 32.5% violation, 21.6% sign reversal, 11.3% amplification\\n- diag≥0.7 (typical LLM accuracy): **13.7% violation**, 2.1% sign reversal, **11.7% amplification**\\n- diag≥0.9 (high-accuracy LLM): **11.9% violation**, 0% sign reversal, **11.9% amplification**\\n- Key pattern: sign reversal vanishes at high accuracy, but **amplification persists at ~12% regardless of accuracy**\\n- Implication: even 90%+ accuracy LLMs face non-trivial effect amplification risk — no \\\"safe accuracy threshold\\\" exists\\n\\n## Venue Fit Risks\\n\\n- **AAAI**: Broad AI audience — emphasize general methodology for \\\"automated annotation measurement error,\\\" not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.\\n- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.\\n- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.\\n\\n## Anticipated Reviewer Concerns & Planned Responses\\n\\n1. **\\\"Trivial extension of binary to multi-class\\\"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 6 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]\\n\\n2. **\\\"Lee & Wood-Doughty (2024) already did categorical\\\"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 6 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]\\n\\n3. **\\\"Why these 6 DAG topologies?\\\"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]\\n\\n4. **\\\"K≥5 expressions aren't actionable\\\"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]\\n\\n5. **\\\"ASV sharpness only proved for 3 topologies\\\"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]\\n\\n6. **\\\"Correlated multi-LLM errors?\\\"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]\\n\\n7. **\\\"Empirical validation scope\\\"** → 3 CSS tasks × 3 LLMs × 3 DAG-relevant scenarios. Tasks selected to cover K=2,3,5 annotation complexity. [Experiments: plan_003, plan_006]\\n\", \"total_chars\": 10212, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea6ddeb5-e1eb-4025-93d7-2ebfbebc776b",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "ac967cad-760a-403c-b9d6-3338631132bb",
  "sourceToolAssistantUUID": "ea6ddeb5-e1eb-4025-93d7-2ebfbebc776b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T08:49:41.535Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WTeBq2Sv2bJYMUdjc13Zxq`</summary>

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
  "parentUuid": "ac967cad-760a-403c-b9d6-3338631132bb",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXsw9HGEocKrFpNSKr2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "171d59d2-1db4-4840-b303-f25e863a5f78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2vDhAdLD2mkqW9qsxtfh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7297,
      "cache_read_input_tokens": 17343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7297,
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

_source line 14 · 2026-05-20T08:49:41.548Z_

<details><summary>↩ Tool result · `toolu_01WTeBq2Sv2bJYMUdjc13Zxq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/ROADMAP.md\", \"content\": \"# causal_annot_error_attrib — Research Dashboard\\n\\n> 最后更新: 2026-05-20 07:40 UTC | 更新原因: Exposure DAG 确认方向反转，Version A framing 成立，更新进展和风险\\n\\n## 核心方向\\n多分类 LLM 标注误差在因果推断中的偏差传播：推导 K×K 混淆矩阵在 6 种 DAG 拓扑下的偏差表达式，构建 Annotation Sensitivity Values (ASVs) 灵敏度分析框架。详见 paper_framing.md。\\n\\n## 当前阶段：Research（MVP 2026-05-20 通过）\\n\\n### 核心假设验证状态\\n- ✅ **方向反转已确认（D004）**：Exposure DAG K=3 — 85% random C 违反 bias-toward-null，83.4% 符号反转\\n- ✅ **二分类保证仍成立**：K=2 exposure DAG 6/6 toward null\\n- ✅ **拓扑依赖性验证**：Confounding DAG 单调 vs Exposure DAG 不可预测\\n- ✅ **折叠损失**：K=3 vs binary Δ up to 0.103\\n- → **Version A framing 确认**（D003 checkpoint resolved）\\n\\n### Target Venue\\n- Primary: AAAI 2027（abstract 2026-07-21, paper 2026-07-28, ~62 天）\\n- Secondary: ARR October 2026（→ NAACL/ACL 2027）\\n\\n### Core Claims（详见 paper_framing.md）\\n1. Multi-class bias taxonomy — 6 DAG 拓扑 × K×K 混淆矩阵结构交互（**核心已验证**）\\n2. Annotation Sensitivity Values (ASVs) — 标注误差灵敏度分析\\n3. Correction guidance framework — 诊断驱动的纠偏方法选择\\n\\n### 实验覆盖（详见 experiment_plan.yaml）\\n- P0: plan_001(6 DAG K=3), plan_003(3 LLM实证), plan_004(ASV证明), plan_006(ASV实证), plan_008(二分类折叠)\\n- P1: plan_002(K=5,7), plan_005(ASV扩展), plan_007(纠偏框架), plan_010(工具包)\\n- P2: plan_009(病态C分析)\\n\\n## 当前进展\\n- ✅ MVP 通过（D001）— confounding DAG 框架验证\\n- ✅ Exposure DAG 方向反转确认（D002/D004）— Claim 1 最强形式成立\\n- ✅ paper_framing.md 双版本 → Version A 确认\\n- ✅ experiment_plan.yaml 10 个实验\\n- ⏳ Dream 模拟运行中（dream_20260520T072911，full review）\\n- ⏳ 等 Dream 回调后审批 P0 实验\\n\\n## 近期任务\\n- [ ] 等 Dream 回调 → 评估 framing/plan 是否需调整\\n- [ ] Dream 通过后：派 Agent 启动 plan_001（剩余 4 canonical DAG 拓扑推导 + MC）\\n- [ ] 并行：plan_003 金标数据获取确认（ACLED ToS / SemEval / Civil Comments）\\n- [ ] 并行：plan_003 API key 准备（Llama 4 / Qwen 3.5 / DeepSeek V4）\\n\\n## GPU 预算\\n本项目 GPU 需求极低（总计 15-30h）。当前 0 GPU 分配。\\n服务器：home-1x5090（sonny），已绑定但未部署项目代码。\\n\\n## 关键风险\\n1. ~~方向反转是否出现~~ → ✅ 已确认（exposure DAG 85%）\\n2. Lee & Wood-Doughty (2024) 重叠 → 已区分 observed vs unobserved confounding\\n3. AAAI DDL 62 天 → 关键路径：plan_001(~5d) → plan_004(~7d) → plan_006(~3d)，留 ~47 天写论文\\n4. plan_004 ASV sharpness 证明可能卡住 → 退路：MC-validated conjectures（framing 已预留）\\n5. Brenner (1993) 精确引用需核实 → 论文撰写时处理\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D004 | 2026-05-20 | D003 checkpoint 提前解决：Version A 成立，exposure DAG K=3 | art_20260520_207c62, art_20260520_f08c30 |\\n| D003 | 2026-05-20 | plan_001 完成后设 checkpoint gate：方向反转拓扑数 → framing 版本 | plan_001 |\\n| D002 | 2026-05-20 | Research 阶段第一优先级：exposure misclassification DAG K= | — |\\n| D001 | 2026-05-20 | MVP PASS — Confounding DAG K=3 理论框架验证通过，进入 researc | — |\\n\\n\\n\", \"total_chars\": 2489, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "171d59d2-1db4-4840-b303-f25e863a5f78",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "c932fae1-696a-4376-ac49-7ba4fa2cd211",
  "sourceToolAssistantUUID": "171d59d2-1db4-4840-b303-f25e863a5f78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T08:49:42.498Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DFPcJEpzfP1sHjLW3UBjWi`</summary>

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
  "parentUuid": "c932fae1-696a-4376-ac49-7ba4fa2cd211",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXsw9HGEocKrFpNSKr2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec1527d0-d82f-4582-9969-3ae777a8d685",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2vDhAdLD2mkqW9qsxtfh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7297,
      "cache_read_input_tokens": 17343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7297,
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

_source line 16 · 2026-05-20T08:49:42.508Z_

<details><summary>↩ Tool result · `toolu_01DFPcJEpzfP1sHjLW3UBjWi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/memory.md\", \"content\": \"# Project Memory\\n\\n## MVP 验证发现 (2026-05-20)\\n\\n### Exposure DAG: bias-toward-null 保证在 K=3 下失效（核心发现）\\n**100k 随机 C 搜索：85% 违反 bias-toward-null，83.4% 产生符号反转。** 二分类 K=2 下全部满足 toward null 保证。\\n\\n具体 named structure 结果：\\n- C3_STRUCTURAL_12: β_2=-0.5 → γ̂_2=+0.06（符号反转）\\n- C4_WEAK_DIAG: β_1=1.0 → γ̂_1≈0（近消失）\\n- C5_NEAR_PERM: β_2=-0.5 → γ̂_2=+1.25（符号反转 + 2.5x 放大，最极端）\\n\\n极端随机案例：β_1=1.0 → γ̂_1=-0.84（符号反转），severity=2.83x。\\n\\n**关键洞察**：exposure 误分类场景（A→Y）下，多分类 C 矩阵的交叉污染使得回归将某类的 Y 值归因到错误标签，产生符号反转。这在二分类中不可能发生（只有 2 个类，误标只导致衰减）。\\n\\n### Dirichlet 子空间分析：高精度 LLM 仍有显著违反（关键补充）\\n**即使 min(diag(C))≥0.9（对应高精度 LLM），amplification 违反率仍达 11.9%。** 分层结果：\\n\\n| 子空间 | 违反率 | 符号反转 | 放大 |\\n|--------|--------|----------|------|\\n| 全空间 | 84.9% | 83.3% | 27.5% |\\n| diag≥0.5 | 32.5% | 21.6% | 11.3% |\\n| diag≥0.7 | 13.7% | 2.1% | 11.7% |\\n| diag≥0.9 | 11.9% | 0.0% | 11.9% |\\n\\n**关键 pattern**：随着 C 对角占优增加，符号反转迅速消失（diag≥0.9 降至 0%），但 amplification 保持稳定在 ~12%。这意味着：\\n- 低精度 LLM（<70%）：符号反转是主要风险\\n- 高精度 LLM（>90%）：符号反转消除，但 amplification 持久存在\\n- **论文 framing 可以声称：即使 LLM 精度 >90%，multiclass 效应放大仍以 >10% 概率发生**\\n\\n采样方法：truncated Beta(1,2) 直接采样（非 rejection sampling），50k samples/subspace。首版 rejection sampling 因 diag≥0.9 接受率 ~10⁻⁶ 导致 OOM。\\n\\n### Confounding DAG: 偏差方向性质（对比发现）\\n100k 随机 C 搜索均未发现负偏差。Confounding DAG (A→T, A→Y, T→Y) 中，K=3 误分类偏差始终与 OVB 同向。量级差异显著（K=3 偏差 0.13-0.30 vs binary collapse 0.24-0.30），但无方向反转。\\n\\n**两个 DAG 的差异**：confounding DAG 下 A 通过 T 间接影响 Y，误分类 A 导致残余混杂但方向固定；exposure DAG 下 A 直接决定 Y 的期望，标签交换直接翻转效应估计。\\n\\n### Lee & Wood-Doughty (2024) 技术区分\\n本项目：observed exposure/confounder with noisy LLM annotation（A 可观测，A* 用于规模化）。LWD：unobserved confounding with proxy（A 不可观测）。关键区别：我们的 C 是可从 validation data 估计的 design parameter。\\n\\n### DGP 参数\\n- Confounding DAG: P(A)=[0.4, 0.35, 0.25], alpha=[1.5, -1.0], beta_T=2.0, beta_A=[1.0, -0.5], sigma=1.0\\n- Exposure DAG: P(A)=[0.4, 0.35, 0.25], beta=[0, 1.0, -0.5], sigma_Y=1.0\\n\", \"total_chars\": 1842, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec1527d0-d82f-4582-9969-3ae777a8d685",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "fa02a31d-5b05-4788-9810-d978f61bb45b",
  "sourceToolAssistantUUID": "ec1527d0-d82f-4582-9969-3ae777a8d685",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T08:49:42.796Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014GQNQLP9eSzVzwWv9oBrd2`</summary>

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
  "parentUuid": "fa02a31d-5b05-4788-9810-d978f61bb45b",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXsw9HGEocKrFpNSKr2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78b09e67-47f8-4302-a7a5-b38c27791f10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2vDhAdLD2mkqW9qsxtfh8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7297,
      "cache_read_input_tokens": 17343,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7297
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 301,
          "cache_read_input_tokens": 17343,
          "cache_creation_input_tokens": 7297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7297,
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

_source line 18 · 2026-05-20T08:49:42.805Z_

<details><summary>↩ Tool result · `toolu_014GQNQLP9eSzVzwWv9oBrd2`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'causal_annot_error_attrib'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78b09e67-47f8-4302-a7a5-b38c27791f10",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "6f6fbb84-f4f9-49fc-bbcd-f28b0189ddca",
  "sourceToolAssistantUUID": "78b09e67-47f8-4302-a7a5-b38c27791f10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T08:49:45.641Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VQ3N2kV1Se7Y2tXmaHStGY`</summary>

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
  "parentUuid": "6f6fbb84-f4f9-49fc-bbcd-f28b0189ddca",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXtHRB6jQF76gak3Bti",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e0cf489-0cf4-4ac2-aae1-b94625418000",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RS9EjRn6njrRbF9XKvzBLf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3567,
      "cache_read_input_tokens": 24640,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3567
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 111,
          "cache_read_input_tokens": 24640,
          "cache_creation_input_tokens": 3567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3567,
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

_source line 20 · 2026-05-20T08:49:45.654Z_

<details><summary>↩ Tool result · `toolu_01VQ3N2kV1Se7Y2tXmaHStGY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/decisions.yaml\", \"content\": \"_next_id: 5\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 07:25 UTC\\n  summary: MVP PASS — Confounding DAG K=3 理论框架验证通过，进入 research 阶段\\n  rationale: 三项 pass 标准全部满足：(1) 理论预测 vs MC 95% CI 一致 5/5，(2) 所有非差异性 C 产生远离零偏差 0.20-0.30，(3)\\n    二分类折叠偏差与三分类预测显著不同（最大 Δ=0.089）。附加发现：100k 随机 C 矩阵搜索在 confounding DAG 下未发现方向反转——偏差始终与\\n    OVB 同向。这是有价值的 characterization result：confounding DAG 偏差方向可预测（单调），方向反转假设需要在其他\\n    DAG 拓扑（mediator、collider）中验证，属于 research 阶段的核心任务。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 07:30 UTC\\n  summary: Research 阶段第一优先级：exposure misclassification DAG K=3 验证 bias-toward-null\\n    是否在多分类下打破\\n  rationale: Reviewer 指出 MVP criterion 2 在 confounding DAG 下不具区分力（二分类也 pass）。\\\"Bias\\n    toward null\\\" 保证（Bross 1954）特指 exposure 误分类，正确测试需要 exposure DAG（A→Y，用 A* 替代 A）。若\\n    K=3 下此 DAG 出现方向反转或 bias-away-from-null 结构性差异，则 Claim 1 最强形式成立；若不出现，需重新框定核心 claim。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 07:31 UTC\\n  summary: plan_001 完成后设 checkpoint gate：方向反转拓扑数 → framing 版本选择\\n  rationale: 'Reviewer [severity: critical] 指出 plan_001 是存在性检验但无 kill criterion。当前\\n    core insight 依赖方向反转（\\\"binary guarantee breaks\\\"），但 MVP 已证明 confounding DAG 无反转。若\\n    6 拓扑全无反转，framing 需 pivot。三级响应：(A) ≥2 拓扑有反转 → 当前 framing 成立，方向反转为 lead finding；(B)\\n    1 拓扑有反转 → 该拓扑为 lead case，framing 可调整；(C) 0 拓扑有反转 → pivot 到版本 B：\\\"multi-class 偏差\\n    magnitude 不可由 binary 推算 + binarization 本身有害\\\"，方向反转降为 topology-specific finding。注意：0\\n    反转 ≠ 项目 kill——binarization inequality + magnitude unpredictability + ASVs 本身够一篇论文，但\\n    framing 必须诚实。'\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: gate\\n    result: pending\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-20 07:39 UTC\\n  summary: D003 checkpoint 提前解决：Version A 成立，exposure DAG K=3 确认方向反转（85% random C）\\n  rationale: Exposure misclassification DAG 结果：100k 随机 C 矩阵中 85% 违反 bias-toward-null，83.4%\\n    产生符号反转，14.1% 产生效应放大。K=2 对照全部 toward null（6/6）。最极端案例：β_1=1.0 → γ̂_1=-0.84（符号反转\\n    2.83x）。机制清晰：近置换 C 导致标签交换直接翻转效应方向，这在 K=2 中结构性不可能。D003 三级响应解析为 Version A（≥1 topology\\n    with reversal）。Core insight 确认：\\\"non-differential exposure misclassification biases\\n    toward null\\\" 保证在 K≥3 下打破。两个 DAG 已形成有力对比：confounding DAG 偏差单调可预测 vs exposure DAG\\n    偏差方向不可预测——验证\\\"偏差取决于 C 结构 × DAG 拓扑交互\\\"。\\n  related_experiments:\\n  - exp_id: art_20260520_207c62\\n    role: validation\\n    result: 85% bias-toward-null violation, 83.4% sign reversal\\n  - exp_id: art_20260520_f08c30\\n    role: baseline\\n    result: confounding DAG monotonic, no reversal\\n  depends_on:\\n  - D002\\n  - D003\\n\", \"total_chars\": 2539, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e0cf489-0cf4-4ac2-aae1-b94625418000",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "0fc99e20-ffbd-46e2-8856-fb3100a921ab",
  "sourceToolAssistantUUID": "9e0cf489-0cf4-4ac2-aae1-b94625418000",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T08:49:48.832Z_

Now let me also check if there are any paper drafts or additional artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fc99e20-ffbd-46e2-8856-fb3100a921ab",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXtVbA7bg9wpBznYHXa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8df7688-1def-4aba-b3d3-de02f3e661ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhAPE5ZVUjmvwKTc9jvMgV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 28207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1683,
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

_source line 22 · 2026-05-20T08:49:49.285Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YEgTtBjBYhErjsVvbeMpdf`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8df7688-1def-4aba-b3d3-de02f3e661ef",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXtVbA7bg9wpBznYHXa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f037c3c4-d6d4-459d-97bd-ff265b03c775",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhAPE5ZVUjmvwKTc9jvMgV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 28207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1683,
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

_source line 23 · 2026-05-20T08:49:49.297Z_

<details><summary>↩ Tool result · `toolu_01YEgTtBjBYhErjsVvbeMpdf`</summary>

```text
artifacts/dream_reports/dream_20260520T074549/best/paper.tex
artifacts/dream_reports/dream_20260520T074549/median/paper.tex
artifacts/dream_reports/dream_20260520T074549/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f037c3c4-d6d4-459d-97bd-ff265b03c775",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "254def96-00b4-4569-ac12-08ab8beeea99",
  "sourceToolAssistantUUID": "f037c3c4-d6d4-459d-97bd-ff265b03c775",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T08:49:50.025Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SJmzfYif4tUpgfXAcGRv2S`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "254def96-00b4-4569-ac12-08ab8beeea99",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXtVbA7bg9wpBznYHXa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28229e6d-d60f-4bb7-9940-46c87efba5a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhAPE5ZVUjmvwKTc9jvMgV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 28207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1683,
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

_source line 25 · 2026-05-20T08:49:50.042Z_

<details><summary>↩ Tool result · `toolu_01SJmzfYif4tUpgfXAcGRv2S`</summary>

```text
artifacts/dream_reports/dream_20260520T074549/best/paper.pdf
artifacts/dream_reports/dream_20260520T074549/median/paper.pdf
artifacts/dream_reports/dream_20260520T074549/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28229e6d-d60f-4bb7-9940-46c87efba5a1",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "c9e51f2d-1d57-41be-bdc7-f790228dbbb8",
  "sourceToolAssistantUUID": "28229e6d-d60f-4bb7-9940-46c87efba5a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T08:49:50.697Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QZyaDysPP4sBwXGyoLD25R`</summary>

```json
{
  "pattern": "**/artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9e51f2d-1d57-41be-bdc7-f790228dbbb8",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXtVbA7bg9wpBznYHXa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cf5b717-9dc9-4680-84a1-55b12fd9adec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhAPE5ZVUjmvwKTc9jvMgV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 28207,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1683
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 278,
          "cache_read_input_tokens": 28207,
          "cache_creation_input_tokens": 1683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1683,
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

_source line 27 · 2026-05-20T08:49:50.712Z_

<details><summary>↩ Tool result · `toolu_01QZyaDysPP4sBwXGyoLD25R`</summary>

```text
artifacts/_project/data/mvp_confounding_dag.py
artifacts/mvp_confounding_dag.py
artifacts/dream_reports/dream_20260520T072911/logs/orchestrator.log
artifacts/dream_reports/dream_20260520T072911/logs/phase1_attempt0.log
artifacts/_project/data/mvp_exposure_dag.py
artifacts/mvp_exposure_dag.py
artifacts/dream_reports/dream_20260520T072911/logs/phase2_best_attempt0.log
artifacts/_project/report/mvp_exposure_dag_output.log
artifacts/mvp_exposure_dag_output.log
artifacts/_project/report/mvp_confounding_dag_output.log
artifacts/mvp_confounding_dag_output.log
artifacts/dream_reports/dream_20260520T072911/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260520T072911/logs/phase2_worst_attempt0.log
artifacts/_project/report/mvp_exposure_dirichlet_subspace.py
artifacts/mvp_exposure_dirichlet_subspace.py
artifacts/dream_reports/dream_20260520T074549/logs/phase1_attempt0.log
artifacts/_project/report/mvp_exposure_dirichlet_subspace_output.log
artifacts/mvp_exposure_dirichlet_subspace_output.log
artifacts/manifest.yaml
artifacts/dream_reports/dream_20260520T074549/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260520T074549/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260520T074549/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260520T074549/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json
artifacts/dream_reports/dream_20260520T074549/best/paper_framing.md
artifacts/dream_reports/dream_20260520T074549/best/paper.tex
artifacts/dream_reports/dream_20260520T074549/best/paper.aux
artifacts/dream_reports/dream_20260520T074549/best/paper.out
artifacts/dream_reports/dream_20260520T074549/best/paper.pdf
artifacts/dream_reports/dream_20260520T074549/best/paper.log
artifacts/dream_reports/dream_20260520T074549/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260520T074549/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json
artifacts/dream_reports/dream_20260520T074549/median/paper_framing.md
artifacts/dream_reports/dream_20260520T074549/median/paper.tex
artifacts/dream_reports/dream_20260520T074549/median/paper.aux
artifacts/dream_reports/dream_20260520T074549/median/paper.pdf
artifacts/dream_reports/dream_20260520T074549/median/paper.log
artifacts/dream_reports/dream_20260520T074549/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260520T074549/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T074549/worst/experiment_data.json
artifacts/dream_reports/dream_20260520T074549/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T074549/worst/paper.tex
artifacts/dream_reports/dream_20260520T074549/worst/paper.aux
artifacts/dream_reports/dream_20260520T074549/worst/paper.out
artifacts/dream_reports/dream_20260520T074549/worst/paper.pdf
artifacts/dream_reports/dream_20260520T074549/worst/paper.log
artifacts/dream_reports/dream_20260520T074549/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260520T074549/best/review_context.yaml
artifacts/dream_reports/dream_20260520T074549/logs/orchestrator.log
artifacts/dream_reports/dream_20260520T074549/best/review_report.md
artifacts/dream_reports/dream_20260520T074549/logs/review_best.log
artifacts/dream_reports/dream_20260520T074549/median/review_context.yaml
artifacts/dream_reports/dream_20260520T074549/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cf5b717-9dc9-4680-84a1-55b12fd9adec",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "53f41cc7-e425-4e6d-95e3-cac595f04536",
  "sourceToolAssistantUUID": "7cf5b717-9dc9-4680-84a1-55b12fd9adec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-20T08:49:53.968Z_

Let me read the dream report review and the best paper draft to get the full picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53f41cc7-e425-4e6d-95e3-cac595f04536",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXtsFu67ukChRsjMgcf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25d1bf34-7051-4534-8bed-86074fb68964",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ugXk3cd6jHnJaPtKa2p8M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1637,
      "cache_read_input_tokens": 29890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1637,
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

_source line 29 · 2026-05-20T08:49:54.444Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T9ciHRqiWRBDSV7LQaut7p`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25d1bf34-7051-4534-8bed-86074fb68964",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXtsFu67ukChRsjMgcf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e93b630-1377-4a52-ba31-7dec5dd7f0c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ugXk3cd6jHnJaPtKa2p8M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1637,
      "cache_read_input_tokens": 29890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1637,
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

_source line 30 · 2026-05-20T08:49:54.458Z_

<details><summary>↩ Tool result · `toolu_01T9ciHRqiWRBDSV7LQaut7p`</summary>

```text
1	---
2	dream_id: dream_20260520T074549
3	tier: best
4	overall_score: 4 - Weak Accept
5	timestamp: 2026-05-20T08:47:38.552129+00:00
6	---
7	
8	# Dream Review Report
9	
10	**Paper:** Multi-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies
11	
12	**Review mode:** Full (2 Reviewers, complete roundtable)
13	**Rating scale:** 6-point (1=Strong Reject … 6=Strong Accept), top ML venue standard (~25% acceptance)
14	
15	---
16	
17	## Overall Assessment
18	
19	**Overall Score: 4 (Weak Accept)**
20	
21	This paper makes a genuine and timely contribution by demonstrating that the classical "toward-null" guarantee for non-differential misclassification breaks down when annotated variables have K≥3 categories, and that the failure pattern is strictly topology-dependent. The three-part contribution — bias taxonomy, ASV sensitivity framework, and correction guidance — forms a coherent theory-to-practice pipeline. The work is technically sound, covers all planned experiments comprehensively, and provides substantial empirical validation (~270K annotations). However, significant presentation issues (complete absence of figures, no proof appendix) and an under-discussed core assumption (non-differential misclassification) prevent a higher score.
22	
23	---
24	
25	## Reviewer Scores
26	
27	| Dimension | R1 (Methods/Experiments) | R2 (Novelty/Related Work) | Consensus |
28	|---|---|---|---|
29	| Technical Soundness | 5 | — | 5 |
30	| Experimental Design & Execution | 5 | — | 5 |
31	| Reproducibility | 4 | — | 4 |
32	| Statistical Rigor | 5 | — | 5 |
33	| Novelty & Significance | — | 5 | 5 |
34	| Related Work Coverage | — | 4 | 4 |
35	| Clarity & Presentation | — | 5 | 4* |
36	| Impact & Practical Value | — | 5 | 5 |
37	| **Overall** | **4** | **4** | **4** |
38	
39	*Clarity downgraded in consensus due to zero figures and possible page-limit concerns.
40	
41	---
42	
43	## Strengths
44	
45	### S1: Novel and well-characterized core finding
46	The topology-dependent reversal result is the paper's crown jewel. The clean dichotomy — information-loss topologies (confounding, instrument, M-bias) preserve bias direction while structural-distortion topologies (exposure, mediation, collider, front-door) produce unpredictable reversal — is conceptually elegant and empirically well-validated. The 100K random confusion matrix search per topology provides convincing evidence, and the K=2 consistency checks anchor the results to classical theory.
47	
48	### S2: Comprehensive experimental coverage
49	All 10 planned experiments are fully implemented: multi-topology MC validation (plan_001), general-K extensions (plan_002), empirical confusion matrices (plan_003), ASV formal proofs (plan_004), ASV MC validation for remaining topologies (plan_005), ASV empirical calibration (plan_006), correction framework (plan_007), binarization collapse (plan_008), pathological C analysis (plan_009), and the annot-sensitivity toolkit (plan_010). The 97.2% theory-MC match rate (35/36 combinations within 95% CI) is strong evidence of derivation correctness. The 432-scenario correction framework validation and 8/9 empirical concordance further substantiate the claims.
50	
51	### S3: Honest scope management
52	The paper makes strategic and intellectually honest choices: ASV sharpness is formally proved for 3 priority topologies (confounding, mediation, collider) with different proof techniques (algebraic, envelope theorem, Lagrangian/KKT), while the remaining 3 are presented as MC-validated conjectures with explicit numerical sharpness gaps (<0.008). The 15% "no adequate method" region in the correction framework is honestly identified as an open problem rather than swept under the rug. This level of scientific candor strengthens credibility.
53	
54	---
55	
56	## Weaknesses
57	
58	### W1 [Major]: Complete absence of figures
59	The experiment design reference specifies 20+ figures (heatmaps, violin plots, sensitivity curves, scatter plots, PCA projections, diagnostic dashboards). The submitted paper contains **zero figures**. This is a critical presentation failure for a paper whose core results are inherently visual — the topology-dependent reversal pattern, the ASV sensitivity curves, and the spectral gap risk map would all benefit enormously from visualization. For a top ML venue, this is a significant deficit that hampers both comprehension and persuasiveness. Tables alone cannot convey the full structure of these results.
60	
61	**Recommendation:** Add at minimum: (1) a topology × reversal heatmap (planned Fig 1), (2) ASV sensitivity curves with empirical C overlay (planned Fig 15), (3) the practitioner risk map (planned Fig 20). These three figures would dramatically improve the paper.
62	
63	### W2 [Major]: Non-differential misclassification assumption insufficiently discussed
64	Both reviewers flagged this independently. The paper assumes P(Ṽ | V, other variables) = P(Ṽ | V) — the error depends only on the true value. However, LLM annotation errors are likely influenced by context, text features, and task framing, making the non-differential assumption potentially too strong in practice. The paper's own empirical finding that prompt variants shift C structure by Frobenius distance 0.04–0.12 (mentioned in the YAML but not prominently in the paper) hints at this concern. The Limitations section mentions extension to differential misclassification as future work but does not discuss:
65	- Under what conditions is the non-differential assumption approximately valid for LLMs?
66	- How sensitive are the reversal results to mild violations of non-differentiality?
67	- Could the ASV framework be extended to handle bounded differential error?
68	
69	This is particularly important because the paper targets CSS practitioners who use LLMs — if the core assumption fails in their setting, the practical value is diminished.
70	
71	### W3 [Moderate]: Missing proof appendix
72	Theorems 1 (Monotonicity) and 2 (Sharpness) are stated with proof technique descriptions but without actual proofs. For a paper that claims formal proofs as a core contribution, the absence of a supplementary appendix with complete proofs is a notable gap. The stated proof techniques are plausible (algebraic for confounding, envelope theorem for mediation, Lagrangian/KKT for collider), but without the proofs themselves, the theoretical claims are unverifiable by reviewers.
73	
74	**Recommendation:** Provide a supplementary appendix with complete proofs. This is standard practice at top ML venues and would strengthen the theoretical contribution substantially.
75	
76	### W4 [Moderate]: Missing related work
77	The paper cites the core references adequately but misses several important works:
78	- **Ogburn & VanderWeele (2012)** on mediator misclassification — directly relevant to the mediation topology analysis
79	- **Imai & Yamamoto (2010)** on sensitivity analysis for causal mediation — relevant to the ASV framework for mediation
80	- **Angelopoulos et al. (2023)** on prediction-powered inference — the PPI method in the correction framework originates here
81	- **Carroll et al. (2006)** textbook on measurement error in nonlinear models — provides the foundational theory the paper extends
82	- **Edwards et al.** on outcome misclassification — relevant to the exposure topology
83	
84	### W5 [Minor]: Reproducibility gaps in empirical setup
85	The paper reports using Llama 4 Maverick, Qwen 3.5 Plus, and DeepSeek V4 on three CSS tasks with ~30K instances × 3 prompt variants, but does not provide:
86	- Exact prompt templates used
87	- Dataset sources and preprocessing
88	- Gold-standard label procurement methodology
89	- Specific model versions/API endpoints
90	- How the three "topological contexts" were assigned to each task (the tasks have inherent structures, but the paper seems to impose mediation/collider/instrument contexts on the same data — is this realistic?)
91	
92	### W6 [Minor]: Empirical topological contexts may be artificial
93	R2 raised that the empirical validation (§6.3) places each CSS task into three topological contexts (mediation, collider, confounding/instrument), but it is unclear whether these represent real research designs. If the topological assignments are hypothetical rather than drawn from actual published studies, the empirical validation is weaker than presented. The paper would benefit from either (a) citing real CSS studies that use these tasks in these topological roles, or (b) being more explicit that the empirical validation demonstrates the framework's mechanics rather than its real-world deployment.
94	
95	---
96	
97	## Questions for Authors
98	
99	1. **Non-differential assumption robustness:** Have you tested what happens to the reversal rates when mild differential misclassification is introduced (e.g., error rates that vary by 10-20% across conditioning strata)? Does the topology-dependent dichotomy survive?
100	
101	2. **Proof availability:** Will a supplementary appendix with complete proofs be provided? For Theorem 2 (Sharpness), can you provide the constructive C* for at least one worked example?
102	
103	3. **Empirical topological contexts:** For the 9 scenarios in Table 12, are the topological contexts drawn from real published CSS research designs, or are they hypothetical assignments to demonstrate the framework?
104	
105	4. **Figure plans:** The paper currently has zero figures. Are figures planned for a revision? Which ones do you consider highest priority?
106	
107	5. **Page count:** The main text appears to extend to ~10 pages. What is the target venue's page limit, and how will the paper be condensed?
108	
109	6. **Toolkit availability:** Is `annot-sensitivity` currently available for reviewer inspection, or is it planned for release upon acceptance?
110	
111	---
112	
113	## Experiment Coverage Assessment
114	
115	| Experiment (Plan ID) | Status | Notes |
116	|---|---|---|
117	| Multi-topology bias derivation, K=3 (001) | ✅ Fully covered | Tables 1-2, §3.2-3.3 |
118	| General K expressions, K=5,7 (002) | ✅ Fully covered | Tables 3-4, §3.4 |
119	| Empirical confusion matrices (003) | ✅ Fully covered | Tables 10-11, §6.1-6.2 |
120	| ASV formal proofs, 3 topologies (004) | ✅ Fully covered | Theorems 1-2, Table 6, §4.2 |
121	| ASV MC validation, remaining 3 (005) | ✅ Fully covered | Table 7, §4.4 |
122	| ASV empirical calibration (006) | ✅ Fully covered | Tables 12-13, §6.3 |
123	| Correction framework (007) | ✅ Fully covered | Tables 8-9, §5-5.1, §6.4 |
124	| Binarization collapse (008) | ✅ Fully covered | Table 5, §3.5 |
125	| Pathological C analysis (009) | ✅ Fully covered | Table 14, §7 |
126	| annot-sensitivity toolkit (010) | ✅ Fully covered | §8 |
127	
128	**Coverage: 10/10 experiments implemented.** All planned experiments from the design reference appear in the paper with results consistent with the expected outcomes. The paper achieves full coverage of the experimental design.
129	
130	---
131	
132	## Detailed Scoring Rationale
133	
134	### Technical Soundness: 5 (Accept)
135	The theoretical framework is carefully constructed. The 97.2% theory-MC match rate across 36 topology×C-structure combinations validates the bias derivations. The ASV definition is mathematically clean, the formal proofs use appropriate techniques, and the honest separation of proved (3 topologies) vs. conjectured (3 topologies) results reflects sound mathematical practice. The correction framework's 95% accuracy across 432 scenarios is well-validated with transparent failure analysis (14 near-ties, 7 extreme cases). One concern: the front-door with rank-deficient C boundary case (the 1/36 mismatch) could receive more discussion.
136	
137	### Experimental Design: 5 (Accept)
138	The experimental design is impressively comprehensive. The MC validation uses appropriate sample sizes (N=10,000, 1000 reps), the 100K random C search is adequate for estimating violation rates, and the K=5,7 extensions demonstrate scaling behavior. The empirical validation with 3 LLMs × 3 tasks × 3 prompt variants × ~30K instances per condition is substantial. The binarization collapse analysis completes the argumentative arc by closing the "escape to binary" loophole. The K=2 consistency check throughout is a strong design choice.
139	
140	### Reproducibility: 4 (Weak Accept)
141	MC simulation details are sufficient (N, reps, C structures, topology specifications). However, the empirical component lacks prompt templates, dataset sources, and gold-standard methodology. The annot-sensitivity toolkit is described but not verified. Improving from 4 to 5 requires releasing the toolkit code, providing supplementary experimental details, and making MC simulation code available.
142	
143	### Novelty & Significance: 5 (Accept)
144	The core finding is genuinely novel: while Brenner (1993) noted that polytomous confounder misclassification can bias in either direction, no prior work has systematically characterized this across multiple DAG topologies with closed-form expressions and a clean dichotomy. The ASV framework is a meaningful conceptual advance — applying the E-value paradigm to annotation error is non-obvious and practically useful. The correction guidance framework directly addresses the "what should I do about it?" question that practitioners face.
145	
146	### Related Work: 4 (Weak Accept)
147	Core positioning is accurate. The paper correctly identifies its contributions relative to the binary measurement error literature (Bross 1954), the NLP/CSS line (Wood-Doughty 2018 → TeBlunthuis 2024 → Lee & Wood-Doughty 2024 → Jerzak 2025), and the sensitivity analysis tradition (VanderWeele & Ding 2017). However, the omission of Ogburn & VanderWeele (2012) on mediator misclassification is notable given that mediation is a key topology. The PPI method in the correction framework should cite Angelopoulos et al. (2023).
148	
149	### Clarity & Presentation: 4 (Weak Accept)
150	The writing is clear, concise, and well-organized. The three-contribution structure is cleanly delineated. Tables are informative and well-formatted. However, the complete absence of figures — in a paper where the results are inherently visual — is a significant presentation failure. The information-loss vs. structural-distortion dichotomy, the ASV sensitivity curves, and the spectral gap diagnostics all cry out for visualization. Additionally, the main text may exceed the 8-page limit for top venues, requiring restructuring.
151	
152	### Impact & Practical Value: 5 (Accept)
153	The paper provides a complete pipeline from theory to practice: diagnosis (bias taxonomy + structural diagnostics) → assessment (ASV) → action (correction guidance) → implementation (toolkit). The identification of specific danger zones (e.g., protest coding with Qwen in mediation/collider contexts, ASV < 1.0) demonstrates concrete practical value. The finding that binarization is not a safe retreat is immediately actionable — it prevents practitioners from making a common but harmful simplification.
154	
155	---
156	
157	## Meta-Review Summary
158	
159	This paper addresses a real and timely problem at the intersection of LLM annotation, measurement error theory, and causal inference. Its core finding — that the classical toward-null guarantee breaks down for multi-class non-differential misclassification in a topology-dependent manner — is novel, well-supported, and practically important. The execution is thorough, covering all planned experiments with appropriate validation methodology.
160	
161	The paper falls short of a higher score primarily due to presentation issues: zero figures, no proof appendix, and possible page-limit concerns. The under-discussion of the non-differential assumption is a substantive concern that weakens the bridge from theory to LLM practice.
162	
163	**With revisions addressing (1) adding key figures, (2) providing a proof appendix, (3) discussing the non-differential assumption more thoroughly, and (4) adding missing references, this paper would likely merit a score of 5 (Accept).**
164	
165	As submitted, it is a solid borderline accept: the contributions are real and the execution is thorough, but the presentation does not yet do justice to the underlying work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e93b630-1377-4a52-ba31-7dec5dd7f0c8",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "6e79ee2b-1589-436f-a698-f666a2b2e77c",
  "sourceToolAssistantUUID": "0e93b630-1377-4a52-ba31-7dec5dd7f0c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T08:49:55.006Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KeKeCmB1hN27gjqCb3xrjD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e79ee2b-1589-436f-a698-f666a2b2e77c",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXtsFu67ukChRsjMgcf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cff7a4c3-6019-47eb-9cb7-1d66689467c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ugXk3cd6jHnJaPtKa2p8M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1637,
      "cache_read_input_tokens": 29890,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1637
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 29890,
          "cache_creation_input_tokens": 1637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1637,
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

_source line 32 · 2026-05-20T08:49:55.334Z_

<details><summary>↩ Tool result · `toolu_01KeKeCmB1hN27gjqCb3xrjD`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsthm}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage[margin=1in]{geometry}
10	\usepackage{natbib}
11	\usepackage{hyperref}
12	\usepackage{tabularx}
13	\usepackage{array}
14	\usepackage{adjustbox}
15	
16	\newtheorem{theorem}{Theorem}
17	\newtheorem{proposition}{Proposition}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\newtheorem{conjecture}{Conjecture}
21	
22	\newcommand{\bC}{\mathbf{C}}
23	\newcommand{\bI}{\mathbf{I}}
24	\newcommand{\bB}{\mathbf{B}}
25	
26	\title{Multi-Class Annotation Errors Are Not Created Equal:\\Bias Taxonomy, Sensitivity Analysis, and Correction Guidance\\for LLM-Annotated Causal Studies}
27	
28	\author{Anonymous}
29	
30	\date{}
31	
32	\begin{document}
33	
34	\maketitle
35	
36	%% ============================================================
37	%% ABSTRACT
38	%% ============================================================
39	\begin{abstract}
40	Large language models (LLMs) are rapidly replacing human annotators in computational social science, yet recent audits show that 31\% of downstream causal conclusions drawn from LLM-annotated data are incorrect.
41	We show that the classical guarantee---non-differential misclassification biases toward the null---breaks when annotated variables have $K\!\ge\!3$ categories.
42	The bias behavior is \emph{topology-dependent}: the same confusion matrix that produces innocuous residual bias in a confounding DAG can produce direction-reversing bias in mediation or collider DAGs.
43	We make three contributions.
44	\textbf{(1)}~A \emph{multi-class bias taxonomy}: closed-form bias expressions for $K\!=\!3$ and matrix-form expressions with eigendecomposition-based interpretability tools for general $K$, across six canonical DAG topologies.
45	Four of six topologies (exposure, mediation, collider, front-door) exhibit direction reversal under non-differential $K\!\ge\!3$ error; confounding and instrument topologies preserve monotonicity.
46	\textbf{(2)}~\emph{Annotation Sensitivity Values} (ASVs), analogous to E-values for unmeasured confounding, that quantify how much annotation error is needed to overturn a conclusion.
47	We prove monotonicity and sharpness for three priority topologies and provide MC-validated conjectures for the remaining three.
48	\textbf{(3)}~A \emph{correction guidance framework} mapping \{topology $\times$ error structure $\times$ ASV\} to the appropriate correction method, achieving 95\% recommendation accuracy across 432 simulated scenarios and validated on three CSS tasks annotated by three LLMs (${\sim}270$K annotations).
49	Binarizing a $K$-class variable to retreat into the binary safe zone is itself hazardous: collapsing $K\!=\!7$ to binary introduces up to $\Delta\!=\!0.19$ additional bias, with 12\% of scenarios exhibiting direction reversal from binarization alone.
50	We release \texttt{annot-sensitivity}, an open-source Python toolkit implementing the full framework.
51	\end{abstract}
52	
53	%% ============================================================
54	%% 1  INTRODUCTION
55	%% ============================================================
56	\section{Introduction}
57	\label{sec:intro}
58	
59	LLMs have become the default annotation engine in computational social science (CSS).
60	Their speed and cost advantages are undeniable, but measurement error in LLM annotations propagates into downstream causal estimates.
61	\citet{baumann2025} audit this pipeline and find that 31\% of downstream conclusions are already incorrect.
62	\citet{kim2025} show that cross-model annotation errors are highly correlated---when two LLMs both err, 60\% of the time they err toward the same category---meaning multi-model ensembles cannot eliminate systematic bias.
63	
64	The classical measurement-error literature provides reassurance for the binary case: non-differential misclassification of a binary exposure biases toward the null \citep{bross1954}.
65	Practitioners routinely extend this guarantee to multi-class variables by binarizing: collapsing $K$-class annotations into two categories before analysis.
66	We show that both the original guarantee and the binarization escape route fail for $K\!\ge\!3$.
67	
68	\paragraph{Core finding.}
69	Non-differential $K\!\ge\!3$ misclassification breaks the toward-null guarantee in 4 of 6 canonical DAG topologies.
70	The reversal pattern is strictly topology-dependent: the same confusion matrix that is benign in the confounding topology produces direction-reversing bias in mediation and collider topologies.
71	In our Monte Carlo experiments, the mediation topology exhibits a 52\% violation rate (47\% sign reversal), the collider topology 41\% (36\% sign reversal), the front-door topology 34\% (28\% sign reversal), and the exposure topology 85\% (83.4\% sign reversal) under 100K random confusion matrices.
72	Confounding and instrument topologies maintain zero violations.
73	
74	\paragraph{Why binarization is not a safe retreat.}
75	Collapsing a $K$-class variable to binary discards inter-category bias structure.
76	We show that binarization introduces additional bias up to $\Delta\!=\!0.19$ (mediation, $K\!=\!7$), and in 12\% of $K\!=\!5{,}7$ scenarios the binarization itself flips the bias direction---making the collapsed estimate \emph{worse} than the multi-class estimate.
77	
78	\paragraph{Contributions.}
79	\textbf{(1)}~A multi-class bias taxonomy with closed-form and matrix-form bias expressions across six DAG topologies (\S\ref{sec:taxonomy}).
80	\textbf{(2)}~Annotation Sensitivity Values (ASVs) with formal monotonicity and sharpness proofs for three topologies and MC-validated conjectures for three more (\S\ref{sec:asv}).
81	\textbf{(3)}~A correction guidance framework achieving 95\% recommendation accuracy (\S\ref{sec:correction}).
82	We validate all results on empirical confusion matrices from three LLMs across three CSS tasks (\S\ref{sec:empirical}) and release the \texttt{annot-sensitivity} Python toolkit.
83	
84	
85	%% ============================================================
86	%% 2  RELATED WORK
87	%% ============================================================
88	\section{Related Work}
89	\label{sec:related}
90	
91	\paragraph{Measurement error in causal inference.}
92	The epidemiological literature on exposure misclassification dates to \citet{bross1954}, with \citet{brenner1993} first noting that polytomous confounder misclassification can bias in either direction.
93	\citet{vanderweele2019} provide sensitivity bounds for binary risk ratios.
94	None of these works provide systematic multi-class bias expressions across multiple DAG topologies.
95	
96	\paragraph{Annotation error in NLP/CSS.}
97	\citet{wooddoughty2018} apply DAG reasoning to text classifier errors but produce no formal bias theorems and are limited to binary variables.
98	\citet{teblunthuis2024} provide the most complete binary treatment with MLA correction but are limited to $K\!=\!2$ and a single classifier.
99	\citet{lee2024} extend to categorical variables and LLM classifiers but cover only one DAG topology (unobserved confounding) on one dataset, with no systematic taxonomy or sensitivity analysis.
100	\citet{jerzak2025} benchmark correction methods but treat annotation error as monolithic---if different confusion matrix structures produce qualitatively different bias in different topologies, unconditional benchmarking is itself misleading.
101	
102	\paragraph{Sensitivity analysis.}
103	E-values \citep{vanderweele2017} quantify robustness to unmeasured confounding via a single scalar.
104	Our ASVs serve an analogous role for annotation error but require a reference confusion matrix and amplification direction, reflecting the richer parameterization of $K\!\times\!K$ error structures.
105	
106	
107	%% ============================================================
108	%% 3  MULTI-CLASS BIAS TAXONOMY
109	%% ============================================================
110	\section{Multi-Class Bias Taxonomy}
111	\label{sec:taxonomy}
112	
113	\subsection{Setup and Notation}
114	
115	Let $\tilde{V}$ denote the observed (LLM-annotated) version of a $K$-class variable $V$.
116	The misclassification process is characterized by the $K\!\times\!K$ confusion matrix $\bC$, where $C_{jk} = P(\tilde{V}=k \mid V=j)$.
117	Non-differential misclassification requires $P(\tilde{V} \mid V, \text{other variables}) = P(\tilde{V} \mid V)$, i.e., the error depends only on the true value.
118	We consider six canonical DAG topologies where $V$ plays distinct structural roles: confounder, treatment (exposure), mediator, collider, instrument, and front-door criterion variable.
119	
120	For $K\!=\!3$, we derive closed-form bias expressions as functions of $\bC$ and the structural parameters of each DAG.
121	For general $K$, we provide matrix-form expressions and develop three interpretability tools: (a) eigendecomposition summaries, (b) worst-case scalar bounds, and (c) spectral diagnostic indicators.
122	
123	\subsection{Closed-Form Bias Expressions (K=3)}
124	\label{sec:kthree}
125	
126	For each topology, we derive the bias $B(\bC) = \hat{\theta}(\tilde{V}) - \theta^*(V)$ as a function of $\bC$ and the true structural parameters.
127	The derivation proceeds by expressing the observed conditional distributions in terms of the true distributions and $\bC$, then computing the resulting distortion in the estimand.
128	
129	\paragraph{Validation.}
130	We validate all closed-form expressions via Monte Carlo simulation: 6 confusion matrix structures $\times$ 6 topologies $\times$ 1000 replications at $N\!=\!10{,}000$.
131	The theory-MC match rate is 97.2\% (35/36 structure$\times$topology combinations fall within 95\% MC confidence intervals).
132	The single boundary case---front-door with rank-deficient $\bC$---shows a discrepancy of 0.003 above the CI upper bound, which resolves at $N\!=\!50{,}000$.
133	Table~\ref{tab:theory-mc} reports the full match matrix.
134	
135	\subsection{Topology-Dependent Reversal}
136	\label{sec:reversal}
137	
138	We execute a 100K random $\bC$ search for each topology, testing whether the bias violates the classical toward-null guarantee.
139	The topologies separate cleanly into two classes:
140	
141	\begin{itemize}
142	    \item \textbf{Information-loss topologies} (confounding, instrument, M-bias): misclassification only reduces the variable's information content; bias direction is predictable. Violation rate = 0 across all three.
143	    \item \textbf{Structural-distortion topologies} (exposure, mediation, collider, front-door): misclassification alters the variable's functional role in the DAG, producing unpredictable direction reversal.
144	\end{itemize}
145	
146	Table~\ref{tab:topology-reversal} reports the complete reversal analysis.
147	The exposure topology exhibits the highest violation rate (85.0\%) because misclassification acts directly on the treatment variable.
148	The mediation topology (52.0\%) is next: a near-permutation $\bC$ that swaps adjacent category labels effectively flips the sign of $\beta_{MY|X}$, reversing the indirect effect.
149	Worst-case severity reaches $1.62\times$ amplification with sign reversal in mediation, and spurious effect creation of 0.44 from a null truth in the collider topology.
150	
151	\begin{table}[t]
152	\centering
153	\caption{Topology $\times$ reversal summary under 100K random confusion matrices ($K\!=\!3$).}
154	\label{tab:topology-reversal}
155	\small
156	\begin{adjustbox}{max width=\textwidth}
157	\begin{tabular}{lcccccc}
158	\toprule
159	Topology & Role & Violation & Sign Rev. & Amplif. & Worst-Case & $K\!=\!2$ \\
160	\midrule
161	Confounding & Confounder & 0.000 & 0.000 & 0.000 & 0.298 (toward OVB) & toward OVB $\checkmark$ \\
162	Exposure & Treatment & 0.850 & 0.834 & 0.141 & 2.83$\times$ amplification & toward null $\checkmark$ \\
163	Mediation & Mediator & 0.520 & 0.470 & 0.110 & 1.62$\times$ + sign reversal & toward null $\checkmark$ \\
164	Collider & Collider & 0.410 & 0.360 & 0.090 & spurious 0.44 from null & attenuated $\checkmark$ \\
165	M-bias & M-bias var. & 0.000 & 0.000 & 0.000 & 0.18 (attenuated) & attenuated $\checkmark$ \\
166	Instrument & Instrument & 0.000 & 0.000 & 0.000 & ratio distortion 0.14 & attenuated $\checkmark$ \\
167	Front-door & Front-door var. & 0.340 & 0.280 & 0.120 & sign reversal & toward null $\checkmark$ \\
168	\bottomrule
169	\end{tabular}
170	\end{adjustbox}
171	\end{table}
172	
173	
174	\begin{table}[t]
175	\centering
176	\caption{Theory--MC match by topology $\times$ confusion matrix structure ($K\!=\!3$, $N\!=\!10{,}000$, 1000 reps). $\checkmark$: within 95\% MC CI. $\triangle^*$: boundary case resolved at $N\!=\!50{,}000$.}
177	\label{tab:theory-mc}
178	\small
179	\begin{adjustbox}{max width=\textwidth}
180	\begin{tabular}{lccccccc}
181	\toprule
182	Topology & Diag.-dom. & Mod.~off-diag & Unif.~off-diag & Block-diag & Near-perm. & Rank-def. & Match \\
183	\midrule
184	Confounding & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & 6/6 \\
185	Mediation   & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & 6/6 \\
186	Collider    & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & 6/6 \\
187	M-bias      & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & 6/6 \\
188	Instrument  & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & 6/6 \\
189	Front-door  & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\checkmark$ & $\triangle^*$ & 5/6 \\
190	\bottomrule
191	\end{tabular}
192	\end{adjustbox}
193	\end{table}
194	
195	
196	\subsection{General K: Matrix-Form Expressions and Interpretability Tools}
197	\label{sec:generalk}
198	
199	For $K \ge 5$, the bias $\bB(\bC)$ is a matrix-valued function whose entries are not individually interpretable.
200	We develop three tools to make these expressions actionable.
201	
202	\paragraph{Eigendecomposition summary.}
203	The spectral decomposition of $\bB$ reveals that the top-2 eigenvalues capture 87\% of bias variance and the top-3 capture 96\% (averaged over topologies and $K$ values; Table~\ref{tab:eigendecomp}).
204	The first eigenvalue corresponds to the ``fidelity'' mode (baseline attenuation) and the second to the dominant misclassification direction.
205	
206	\paragraph{Worst-case scalar bound.}
207	The spectral norm $\|\bB\|_2$ provides a scalar upper bound on bias magnitude.
208	This bound has 88\% tightness---in 88\% of scenarios it is within 15\% of the true worst-case bias.
209	
210	\paragraph{Scaling with $K$.}
211	As $K$ increases, the violation rate rises monotonically: mediation goes from 0.52 ($K\!=\!3$) to 0.61 ($K\!=\!5$) to 0.68 ($K\!=\!7$); collider from 0.41 to 0.49 to 0.55 (Table~\ref{tab:violation-scaling}).
212	Confounding remains at zero regardless of $K$.
213	Theory--MC match rates are 17/18 for $K\!=\!5$ and 16/18 for $K\!=\!7$; the 2 unmatched cases at $K\!=\!7$ are near-permutation extremes that converge at $N\!=\!50{,}000$.
214	
215	\begin{table}[t]
216	\centering
217	\caption{Violation rate scaling with $K$.}
218	\label{tab:violation-scaling}
219	\small
220	\begin{tabular}{lcccc}
221	\toprule
222	Topology & $K\!=\!3$ & $K\!=\!5$ & $K\!=\!7$ & Trend \\
223	\midrule
224	Confounding & 0.000 & 0.000 & 0.000 & Stable at 0 \\
225	Mediation   & 0.520 & 0.610 & 0.680 & Monotonically increasing \\
226	Collider    & 0.410 & 0.490 & 0.550 & Monotonically increasing \\
227	\bottomrule
228	\end{tabular}
229	\end{table}
230	
231	\begin{table}[t]
232	\centering
233	\caption{Eigendecomposition variance explained by top eigenvalues of the bias matrix.}
234	\label{tab:eigendecomp}
235	\small
236	\begin{tabular}{llccc}
237	\toprule
238	Topology & $K$ & Top-1 & Top-2 & Top-3 \\
239	\midrule
240	Confounding & 5 & 72\% & 89\% & 97\% \\
241	Confounding & 7 & 68\% & 85\% & 95\% \\
242	Mediation   & 5 & 70\% & 87\% & 96\% \\
243	Mediation   & 7 & 65\% & 84\% & 94\% \\
244	Collider    & 5 & 71\% & 88\% & 96\% \\
245	Collider    & 7 & 66\% & 85\% & 95\% \\
246	\bottomrule
247	\end{tabular}
248	\end{table}
249	
250	
251	\subsection{Binarization Collapse Analysis}
252	\label{sec:binarization}
253	
254	A natural practitioner response to the multi-class reversal result is: ``binarize the variable to recover the binary guarantee.''
255	We show this strategy is hazardous.
256	For each of 7 topologies (6 canonical + exposure) at $K\!=\!3{,}5{,}7$, we compute the additional bias $\Delta$ introduced by collapsing $K$ categories to 2.
257	
258	The maximum $\Delta$ is 0.19 (mediation, $K\!=\!7$), which is large enough to reverse substantive conclusions in typical CSS studies where effect sizes are 0.1--0.3.
259	Average $\Delta$ increases monotonically with $K$: 0.08 ($K\!=\!3$), 0.13 ($K\!=\!5$), 0.16 ($K\!=\!7$).
260	In 12\% of $K\!=\!5{,}7$ scenarios, $\Delta$ itself flips the bias direction---making the binarized estimate worse than the multi-class estimate.
261	Table~\ref{tab:binarization} reports the full results.
262	
263	\begin{table}[t]
264	\centering
265	\caption{Binarization collapse $\Delta$ by topology $\times$ $K$. Direction reversal indicates cases where binarization flips the bias direction.}
266	\label{tab:binarization}
267	\small
268	\begin{adjustbox}{max width=\textwidth}
269	\begin{tabular}{lccccc}
270	\toprule
271	Topology & $K\!=\!3$ $\Delta$ & $K\!=\!5$ $\Delta$ & $K\!=\!7$ $\Delta$ & Max $\Delta$ & Direction Reversal? \\
272	\midrule
273	Confounding & 0.06 & 0.09 & 0.11 & 0.11 & No \\
274	Exposure    & 0.08 & 0.12 & 0.15 & 0.15 & Yes (3\% of $K\!=\!7$) \\
275	Mediation   & 0.10 & 0.15 & 0.19 & 0.19 & Yes (18\% of $K\!=\!7$) \\
276	Collider    & 0.09 & 0.14 & 0.17 & 0.17 & Yes (14\% of $K\!=\!7$) \\
277	M-bias      & 0.05 & 0.08 & 0.10 & 0.10 & No \\
278	Instrument  & 0.04 & 0.07 & 0.09 & 0.09 & No \\
279	Front-door  & 0.09 & 0.13 & 0.16 & 0.16 & Yes (11\% of $K\!=\!7$) \\
280	\bottomrule
281	\end{tabular}
282	\end{adjustbox}
283	\end{table}
284	
285	
286	%% ============================================================
287	%% 4  ANNOTATION SENSITIVITY VALUES
288	%% ============================================================
289	\section{Annotation Sensitivity Values}
290	\label{sec:asv}
291	
292	\subsection{Definition}
293	
294	\begin{definition}[Annotation Sensitivity Value]
295	Given a DAG topology $\mathcal{G}$, a reference confusion matrix $\bC_0$, and a downstream estimate $\hat\theta$, the ASV at threshold $\theta_0$ is
296	\[
297	\text{ASV}(\hat\theta, \theta_0, \bC_0, \mathcal{G}) = \inf\!\big\{\delta > 0 : \exists\, \bC \text{ with } \|\bC - \bC_0\|_F \le g(\delta),\; B(\bC, \mathcal{G}) \text{ overturns } \hat\theta \text{ past } \theta_0 \big\},
298	\]
299	where $g(\delta)$ maps the amplification factor $\delta$ to the Frobenius perturbation radius of the confusion matrix.
300	\end{definition}
301	
302	ASVs are reported alongside effect estimates, analogous to E-values for unmeasured confounding.
303	An ASV of 1.5 means that annotation error only 50\% larger than the estimated confusion matrix would suffice to overturn the conclusion.
304	An ASV $>\!3$ indicates a robust conclusion.
305	
306	\subsection{Formal Proofs for Priority Topologies}
307	
308	We prove two properties for three priority topologies:
309	
310	\begin{theorem}[Monotonicity]
311	For $\mathcal{G} \in \{\text{confounding, mediation, collider}\}$, $\text{ASV}(\delta)$ is monotonically non-decreasing in $\delta$.
312	\end{theorem}
313	
314	\begin{theorem}[Sharpness]
315	For each $\delta > 0$ and $\mathcal{G} \in \{\text{confounding, mediation, collider}\}$, there exists an explicit $\bC^*(\delta)$ achieving the ASV bound.
316	\end{theorem}
317	
318	The proof techniques are topology-specific.
319	\textbf{Confounding}: algebraic---ASV is a closed-form function of the spectral gap of $\bC$ and $\delta$.
320	\textbf{Mediation}: algebraic combined with the envelope theorem---the indirect effect ASV decomposes via the product of coefficients.
321	\textbf{Collider}: Lagrangian optimization with KKT conditions over the $\bC$ perturbation space.
322	All three proofs are constructive: they provide explicit $\bC^*$ matrices achieving the bound in 100\% of tested scenarios.
323	
324	\subsection{MC Validation}
325	
326	We validate ASV coverage via 1000 scenarios $\times$ 500 MC replications per scenario.
327	Table~\ref{tab:asv-coverage} reports coverage at nominal 90\%, 95\%, and 99\% levels.
328	Average coverage at 95\% nominal is 95.2\%, indicating slight conservative over-coverage.
329	
330	\begin{table}[t]
331	\centering
332	\caption{ASV coverage calibration (1000 MC scenarios, 500 reps each).}
333	\label{tab:asv-coverage}
334	\small
335	\begin{tabular}{lcccccc}
336	\toprule
337	Topology & Nom.~90\% & Act.~90\% & Nom.~95\% & Act.~95\% & Nom.~99\% & Act.~99\% \\
338	\midrule
339	Confounding & 90\% & 91.8\% & 95\% & 95.8\% & 99\% & 99.2\% \\
340	Mediation   & 90\% & 90.9\% & 95\% & 94.9\% & 99\% & 98.7\% \\
341	Collider    & 90\% & 90.8\% & 95\% & 94.8\% & 99\% & 98.5\% \\
342	Average     & 90\% & 91.2\% & 95\% & 95.2\% & 99\% & 98.8\% \\
343	\bottomrule
344	\end{tabular}
345	\end{table}
346	
347	
348	\subsection{Remaining Topologies: MC-Validated Conjectures}
349	
350	For M-bias, instrument, and front-door topologies, we derive ASV expressions and validate them via MC simulation, but report sharpness as conjectures rather than formal proofs due to algebraic complexity.
351	
352	\begin{conjecture}
353	The ASV bounds for M-bias, instrument, and front-door topologies are sharp.
354	\end{conjecture}
355	
356	Evidence: MC validation shows zero monotonicity violations across 1000 scenarios for all three topologies, and the numerical sharpness gap is $<\!0.008$ (Table~\ref{tab:asv-remaining}).
357	Front-door ASV involves joint perturbation of a two-stage estimator; a closed-form sharpness proof requires solving a bilinear constrained optimization, which we identify as immediate future work.
358	
359	\begin{table}[t]
360	\centering
361	\caption{ASV validation for remaining topologies (1000 MC scenarios).}
362	\label{tab:asv-remaining}
363	\small
364	\begin{tabular}{lcccc}
365	\toprule
366	Topology & Monotonicity & Coverage @95\% & Sharpness Gap & Status \\
367	\midrule
368	M-bias     & $\checkmark$ (0 violations) & 95.4\% & 0.006 & Conjecture \\
369	Instrument & $\checkmark$ (0 violations) & 96.1\% & 0.005 & Conjecture \\
370	Front-door & $\checkmark$ (0 violations) & 94.3\% & 0.008 & Conjecture \\
371	\bottomrule
372	\end{tabular}
373	\end{table}
374	
375	
376	%% ============================================================
377	%% 5  CORRECTION GUIDANCE FRAMEWORK
378	%% ============================================================
379	\section{Correction Guidance Framework}
380	\label{sec:correction}
381	
382	We construct a principled decision framework: given \{topology $\times$ confusion matrix structure $\times$ ASV\}, the framework recommends the correction method that minimizes residual bias.
383	Candidate methods include: matrix-based likelihood adjustment (MLA), prediction-powered inference (PPI), double-sampling likelihood (DSL), and naive plug-in.
384	The framework also identifies regimes where no existing method suffices.
385	
386	\subsection{MC Validation}
387	
388	We test the framework across 432 scenarios: 6 topologies $\times$ 6 confusion matrix structures $\times$ 3 $K$ values $\times$ 4 effect sizes.
389	The framework recommends the optimal method in 411/432 scenarios (95.0\% accuracy).
390	Table~\ref{tab:correction-distribution} reports the recommendation distribution, and Table~\ref{tab:correction-accuracy} reports accuracy by topology.
391	
392	Among the 21 non-optimal recommendations, 14 are cases where MLA and PPI perform within 0.005 of each other (the recommendation is arbitrary), and 7 are extreme-$\bC$ + small-$N$ cases where all methods are unstable.
393	
394	\begin{table}[t]
395	\centering
396	\caption{Correction method recommendation distribution across 432 MC scenarios.}
397	\label{tab:correction-distribution}
398	\small
399	\begin{tabular}{lccc}
400	\toprule
401	Method & \% Scenarios & Typical Condition & Avg Bias Reduction \\
402	\midrule
403	MLA & 31\% & $\bC$ known, $K\!\le\!5$, non-differential & 72\% \\
404	PPI & 24\% & $\bC$ uncertain, gold-standard available & 65\% \\
405	DSL & 18\% & Confounding, high diag.~dominance & 58\% \\
406	Naive plug-in & 12\% & ASV $>\!5.0$ (robust) & N/A (unnecessary) \\
407	No adequate method & 15\% & Correlated errors + differential + collider/front-door & N/A \\
408	\bottomrule
409	\end{tabular}
410	\end{table}
411	
412	\begin{table}[t]
413	\centering
414	\caption{Framework accuracy by topology (432 scenarios total, 72 per topology).}
415	\label{tab:correction-accuracy}
416	\small
417	\begin{tabular}{lcccc}
418	\toprule
419	Topology & Scenarios & Correct & Accuracy & Most Common Failure \\
420	\midrule
421	Confounding & 72 & 71 & 98.6\% & MLA $\approx$ PPI \\
422	Mediation   & 72 & 69 & 95.8\% & Extreme $\bC$ + small $N$ \\
423	Collider    & 72 & 67 & 93.1\% & MLA $\approx$ PPI + extreme $\bC$ \\
424	M-bias      & 72 & 70 & 97.2\% & Rare edge case \\
425	Instrument  & 72 & 69 & 95.8\% & Wald ratio instability \\
426	Front-door  & 72 & 65 & 90.3\% & Two-stage complexity \\
427	\bottomrule
428	\end{tabular}
429	\end{table}
430	
431	The 15\% of scenarios classified as ``no adequate method'' occur primarily under correlated multi-LLM errors combined with differential $K\!\ge\!5$ misclassification in collider or front-door topologies.
432	We identify dependence-aware multi-LLM correction as the most important open problem in this space, directly motivated by the findings of \citet{kim2025}.
433	
434	
435	%% ============================================================
436	%% 6  EMPIRICAL VALIDATION
437	%% ============================================================
438	\section{Empirical Validation}
439	\label{sec:empirical}
440	
441	\subsection{LLM Annotation Setup}
442	
443	We collect empirical confusion matrices from three LLMs---Llama~4 Maverick, Qwen~3.5 Plus, and DeepSeek~V4---on three CSS annotation tasks:
444	(1)~protest event coding ($K\!=\!5$: peaceful protest, violent protest, strategic development, government response, other),
445	(2)~stance detection ($K\!=\!3$: favor, against, neutral), and
446	(3)~toxicity detection ($K\!=\!2$: toxic, non-toxic).
447	Each model annotates ${\sim}30$K instances per task across 3 prompt variants, yielding ${\sim}270$K total annotations.
448	Table~\ref{tab:empirical-C} summarizes the confusion matrix characteristics.
449	
450	\begin{table}[t]
451	\centering
452	\caption{Empirical confusion matrix summary (${\sim}270$K annotations).}
453	\label{tab:empirical-C}
454	\small
455	\begin{adjustbox}{max width=\textwidth}
456	\begin{tabular}{llccccl}
457	\toprule
458	Task & $K$ & Model & Accuracy & Diag.~Dom. & Largest Off-Diag & $\bC$ Structure \\
459	\midrule
460	Protest & 5 & Llama 4 Maverick & 0.64 & 0.60 & 0.18 (strat\_dev$\to$peaceful) & Moderate off-diag \\
461	Protest & 5 & Qwen 3.5 Plus    & 0.60 & 0.57 & 0.21 (strat\_dev$\to$peaceful) & Near-permutation \\
462	Protest & 5 & DeepSeek V4       & 0.67 & 0.63 & 0.15 (other$\to$gov\_resp)     & Block-diagonal \\
463	Stance  & 3 & Llama 4 Maverick & 0.77 & 0.76 & 0.14 (neutral$\to$against) & Block-diagonal \\
464	Stance  & 3 & Qwen 3.5 Plus    & 0.73 & 0.72 & 0.16 (against$\to$neutral) & Block-diagonal \\
465	Stance  & 3 & DeepSeek V4       & 0.76 & 0.75 & 0.13 (neutral$\to$against) & Block-diagonal \\
466	Toxicity& 2 & Llama 4 Maverick & 0.91 & 0.91 & 0.09 (toxic$\to$non-toxic) & Diagonal-dominant \\
467	Toxicity& 2 & Qwen 3.5 Plus    & 0.87 & 0.87 & 0.13 (non-toxic$\to$toxic) & Diagonal-dominant \\
468	Toxicity& 2 & DeepSeek V4       & 0.90 & 0.90 & 0.10 (toxic$\to$non-toxic) & Diagonal-dominant \\
469	\bottomrule
470	\end{tabular}
471	\end{adjustbox}
472	\end{table}
473	
474	
475	\subsection{Inter-Model Error Correlation}
476	
477	Table~\ref{tab:inter-model} reports inter-model agreement.
478	The average same-direction error rate is 58\%, consistent with the 60\% reported by \citet{kim2025}.
479	This confirms that multi-LLM ensembles cannot eliminate systematic annotation bias---errors are correlated because LLMs share similar pre-training data and reasoning patterns.
480	
481	\begin{table}[t]
482	\centering
483	\caption{Inter-model error agreement.}
484	\label{tab:inter-model}
485	\small
486	\begin{tabular}{llccc}
487	\toprule
488	Task & Model Pair & Cohen's $\kappa$ & Error Agree. & Same-Dir. \\
489	\midrule
490	Protest & Llama--Qwen     & 0.69 & 0.24 & 0.61 \\
491	Protest & Llama--DeepSeek  & 0.72 & 0.21 & 0.57 \\
492	Protest & Qwen--DeepSeek   & 0.68 & 0.25 & 0.56 \\
493	Stance  & Llama--Qwen     & 0.67 & 0.18 & 0.59 \\
494	Stance  & Llama--DeepSeek  & 0.70 & 0.16 & 0.58 \\
495	Stance  & Qwen--DeepSeek   & 0.66 & 0.19 & 0.57 \\
496	Toxicity& All pairs avg   & 0.76 & 0.09 & 0.62 \\
497	\bottomrule
498	\end{tabular}
499	\end{table}
500	
501	
502	\subsection{ASV Calibration on Empirical Data}
503	
504	We apply the ASV framework to the empirical confusion matrices, placing each task in three topological contexts (mediation, collider, confounding or instrument as appropriate) and computing ASVs.
505	Table~\ref{tab:asv-concordance} reports concordance between ASV-based model rankings and actual bias severity rankings.
506	ASV ranking agrees with actual bias ranking in 8/9 scenarios.
507	The single discordant case (protest $\times$ instrument, DeepSeek vs.\ Qwen) involves a difference of only 0.02, within the noise margin of Wald ratio estimation.
508	
509	\begin{table}[t]
510	\centering
511	\caption{ASV concordance with empirical bias severity (9 scenarios).}
512	\label{tab:asv-concordance}
513	\small
514	\begin{adjustbox}{max width=\textwidth}
515	\begin{tabular}{llllc}
516	\toprule
517	Task & Context & ASV Ranking & Actual Bias Ranking & Concordant \\
518	\midrule
519	Protest  & Mediation   & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\checkmark$ \\
520	Protest  & Collider    & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\checkmark$ \\
521	Protest  & Instrument  & DeepSeek $<$ Qwen $<$ Llama & Qwen $<$ DeepSeek $<$ Llama & $\times$ {\scriptsize(0.02)} \\
522	Stance   & Mediation   & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\checkmark$ \\
523	Stance   & Collider    & Llama $<$ Qwen $<$ DeepSeek & Llama $<$ Qwen $<$ DeepSeek & $\checkmark$ \\
524	Stance   & Confounding & Llama $<$ Qwen $<$ DeepSeek & Llama $<$ Qwen $<$ DeepSeek & $\checkmark$ \\
525	Toxicity & Mediation   & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\checkmark$ \\
526	Toxicity & Collider    & Qwen $<$ DeepSeek $<$ Llama & Qwen $<$ DeepSeek $<$ Llama & $\checkmark$ \\
527	Toxicity & Confounding & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\checkmark$ \\
528	\bottomrule
529	\end{tabular}
530	\end{adjustbox}
531	\end{table}
532	
533	Table~\ref{tab:asv-robustness} classifies each scenario by ASV-based robustness.
534	Protest event coding in mediation and collider contexts is flagged as \textsc{fragile} (ASV $<\!1.5$), with Qwen~3.5 Plus reaching ASV $=\!0.9$ in the mediation context---meaning even modest additional annotation error would overturn the downstream conclusion.
535	Both empirical scenarios where $\bC$ falls in the theoretical reversal zone are correctly flagged by ASV $<\!1.5$.
536	Held-out gold-standard coverage at the 95\% nominal level is 94\%.
537	
538	\begin{table}[t]
539	\centering
540	\caption{ASV robustness classification across empirical scenarios.}
541	\label{tab:asv-robustness}
542	\small
543	\begin{adjustbox}{max width=\textwidth}
544	\begin{tabular}{llccl}
545	\toprule
546	Task & Context & Best ASV & Worst ASV & Classification \\
547	\midrule
548	Protest  & Mediation   & 2.1 (DeepSeek) & 0.9 (Qwen) & \textsc{Fragile} \\
549	Protest  & Collider    & 1.8 (DeepSeek) & 1.1 (Qwen) & \textsc{Fragile} \\
550	Protest  & Instrument  & 3.2 (Llama)    & 2.4 (DeepSeek) & Moderate \\
551	Stance   & Mediation   & 4.1 (DeepSeek) & 2.8 (Qwen) & Robust \\
552	Stance   & Collider    & 3.8 (DeepSeek) & 2.5 (Llama) & Moderate \\
553	Stance   & Confounding & 5.2 (DeepSeek) & 3.9 (Llama) & Robust \\
554	Toxicity & Mediation   & 7.3 (Llama)    & 5.1 (Qwen) & Robust \\
555	Toxicity & Collider    & 6.8 (Llama)    & 4.9 (Qwen) & Robust \\
556	Toxicity & Confounding & 8.1 (DeepSeek) & 6.2 (Qwen) & Robust \\
557	\bottomrule
558	\end{tabular}
559	\end{adjustbox}
560	\end{table}
561	
562	
563	\subsection{Correction Framework on Empirical Data}
564	
565	On the 9 empirical scenarios, the correction guidance framework recommends the method producing $\ge\!40\%$ bias reduction in 8/9 cases.
566	The single exception (protest $\times$ collider $\times$ Qwen) is correctly classified as ``no adequate method''---the near-permutation confusion matrix combined with high inter-model error correlation places this scenario outside the range of current correction approaches.
567	
568	
569	%% ============================================================
570	%% 7  PATHOLOGICAL CONFUSION MATRIX ANALYSIS
571	%% ============================================================
572	\section{Structural Diagnostics for Confusion Matrices}
573	\label{sec:diagnostics}
574	
575	To provide practitioners with actionable early-warning indicators, we analyze which properties of $\bC$ predict bias severity.
576	
577	\paragraph{Spectral gap.}
578	The spectral gap $(1 - \lambda_2/\lambda_1)$ of $\bC$ explains 83\% of bias magnitude variance ($R^2 = 0.83$, $r = -0.91$).
579	A spectral gap below 0.15 predicts catastrophic bias ($>\!2\times$ effect size) in $\ge\!80\%$ of reversal-prone topologies.
580	
581	\paragraph{Diagonal dominance ratio.}
582	The diagonal dominance ratio has $R^2 = 0.76$ ($r = -0.87$).
583	A ratio below 0.55 signals high risk.
584	
585	\paragraph{Two-number diagnostic.}
586	We propose a practitioner-facing two-number summary: (spectral gap, diagonal dominance ratio) $\to$ risk category \{low, medium, high, catastrophic\}.
587	The joint model achieves $R^2 = 0.89$.
588	Table~\ref{tab:structural-predictors} reports all structural predictors.
589	
590	\begin{table}[t]
591	\centering
592	\caption{Structural predictors of bias severity.}
593	\label{tab:structural-predictors}
594	\small
595	\begin{tabular}{lccc}
596	\toprule
597	Predictor & $r$ with $|$Bias$|$ & $R^2$ & Catastrophic Threshold \\
598	\midrule
599	Spectral gap $(1-\lambda_2/\lambda_1)$ & $-0.91$ & 0.83 & $<\!0.15$ \\
600	Diagonal dominance ratio & $-0.87$ & 0.76 & $<\!0.55$ \\
601	Condition number of $\bC$ & $+0.89$ & 0.79 & $>\!12$ \\
602	Min diagonal element     & $-0.84$ & 0.71 & $<\!0.3$ \\
603	Spectral gap + diag.~dom.~(joint) & --- & 0.89 & Combined \\
604	\bottomrule
605	\end{tabular}
606	\end{table}
607	
608	Near-permutation confusion matrices (spectral gap $<\!0.05$) produce reversal in all structural-distortion topologies with severity $1.5$--$3\times$.
609	Rank-deficient matrices produce catastrophic bias regardless of topology.
610	Block-diagonal matrices exhibit direction-dependent behavior: reversal is guaranteed when classes with opposite effects are merged within the same block.
611	
612	In the empirical data, the spectral gap diagnostic for Qwen~3.5 Plus on protest coding under certain prompt variants falls below 0.15, consistent with the ASV $<\!1.0$ fragile classification in \S\ref{sec:empirical}.
613	
614	
615	%% ============================================================
616	%% 8  TOOLKIT
617	%% ============================================================
618	\section{The \texttt{annot-sensitivity} Toolkit}
619	\label{sec:toolkit}
620	
621	We release \texttt{annot-sensitivity}, a pip-installable Python package implementing the full framework.
622	The API surface consists of three functions corresponding to the three contributions:
623	\begin{itemize}
624	    \item \texttt{bias\_expression(dag, C, K)}: returns the closed-form or matrix-form bias expression for the specified topology.
625	    \item \texttt{asv\_bound(dag, C, estimate, threshold)}: computes the ASV and the constructive $\bC^*$ achieving the bound.
626	    \item \texttt{recommend\_correction(dag, C, asv, n\_gold)}: recommends the appropriate correction method.
627	\end{itemize}
628	
629	The package supports $K = 2$--$20$, all 6 topologies, and runs in $<\!1$s for $K\!\le\!7$.
630	Dependencies are minimal (NumPy, SciPy, Matplotlib).
631	Six topology-specific Jupyter notebook tutorials are included.
632	Test coverage exceeds 90\%.
633	
634	
635	%% ============================================================
636	%% 9  CONCLUSION
637	%% ============================================================
638	\section{Conclusion}
639	\label{sec:conclusion}
640	
641	We have shown that multi-class annotation errors interact with DAG topology in ways that break classical binary guarantees.
642	Four of six canonical topologies exhibit direction-reversing bias under non-differential $K\!\ge\!3$ misclassification, and binarization is not a safe escape.
643	Our three contributions---the bias taxonomy, ASV sensitivity analysis, and correction guidance framework---provide the diagnostic layer that has been missing from the LLM annotation pipeline.
644	
645	\paragraph{Limitations.}
646	ASV sharpness is formally proved for only three topologies; the remaining three are supported by strong numerical evidence.
647	The correction framework achieves 90.3\% accuracy on the front-door topology, the lowest among all topologies.
648	The 15\% of scenarios where no existing correction method is adequate---primarily involving correlated multi-LLM errors---remain an open problem.
649	Our empirical validation covers three CSS tasks; broader coverage across domains (e.g., biomedical NLP) is left to future work.
650	
651	\paragraph{Future directions.}
652	Formal sharpness proofs for the remaining three topologies (particularly front-door, which requires solving bilinear constrained optimization).
653	Dependence-aware multi-LLM correction methods that account for the 58\% cross-model error correlation we observe.
654	Extension to differential misclassification, where the error process depends on other variables in the DAG.
655	
656	
657	%% ============================================================
658	%% REFERENCES
659	%% ============================================================
660	\bibliographystyle{plainnat}
661	
662	\begin{thebibliography}{20}
663	
664	\bibitem[Baumann et~al.(2025)]{baumann2025}
665	Baumann, L., et~al. (2025).
666	\newblock Auditing LLM annotations in computational social science.
667	\newblock \emph{Proceedings of ACL 2025}.
668	
669	\bibitem[Brenner(1993)]{brenner1993}
670	Brenner, H. (1993).
671	\newblock Bias due to non-differential misclassification of polytomous confounders.
672	\newblock \emph{Journal of Clinical Epidemiology}, 46(1):57--63.
673	
674	\bibitem[Bross(1954)]{bross1954}
675	Bross, I.~D. (1954).
676	\newblock Misclassification in 2$\times$2 tables.
677	\newblock \emph{Biometrics}, 10(4):478--486.
678	
679	\bibitem[Hern{\'a}n and Cole(2009)]{hernan2009}
680	Hern{\'a}n, M.~A. and Cole, S.~R. (2009).
681	\newblock Invited commentary: Causal diagrams and measurement bias.
682	\newblock \emph{American Journal of Epidemiology}, 170(8):959--964.
683	
684	\bibitem[Jerzak et~al.(2025)]{jerzak2025}
685	Jerzak, C.~T., et~al. (2025).
686	\newblock Benchmarking correction methods for LLM annotation errors.
687	\newblock \emph{Proceedings of EMNLP 2025}.
688	
689	\bibitem[Kim et~al.(2025)]{kim2025}
690	Kim, S., et~al. (2025).
691	\newblock Correlated errors in multi-LLM annotation pipelines.
692	\newblock \emph{Proceedings of ICML 2025}.
693	
694	\bibitem[Lee and Wood-Doughty(2024)]{lee2024}
695	Lee, S. and Wood-Doughty, Z. (2024).
696	\newblock Categorical annotation errors in causal inference with LLM classifiers.
697	\newblock \emph{Proceedings of EMNLP 2024}.
698	
699	\bibitem[TeBlunthuis et~al.(2024)]{teblunthuis2024}
700	TeBlunthuis, N., et~al. (2024).
701	\newblock Measurement error correction for binary text classifiers in causal inference.
702	\newblock \emph{Proceedings of NAACL 2024}.
703	
704	\bibitem[VanderWeele and Ding(2017)]{vanderweele2017}
705	VanderWeele, T.~J. and Ding, P. (2017).
706	\newblock Sensitivity analysis in observational research: Introducing the E-value.
707	\newblock \emph{Annals of Internal Medicine}, 167(4):268--274.
708	
709	\bibitem[VanderWeele and Li(2019)]{vanderweele2019}
710	VanderWeele, T.~J. and Li, Y. (2019).
711	\newblock Simple sensitivity analysis for differential measurement error.
712	\newblock \emph{American Journal of Epidemiology}, 188(10):1823--1829.
713	
714	\bibitem[Wood-Doughty et~al.(2018)]{wooddoughty2018}
715	Wood-Doughty, Z., et~al. (2018).
716	\newblock Challenges of using text classifiers for causal inference.
717	\newblock \emph{Proceedings of EMNLP 2018}.
718	
719	\end{thebibliography}
720	
721	\end{document}
722	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cff7a4c3-6019-47eb-9cb7-1d66689467c9",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "3d734a46-57bd-4ae9-8c38-808cfbc03b4d",
  "sourceToolAssistantUUID": "cff7a4c3-6019-47eb-9cb7-1d66689467c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-20T08:49:58.900Z_

Now I have a thorough understanding of the paper. Let me also check the experiment plan and any other review reports for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d734a46-57bd-4ae9-8c38-808cfbc03b4d",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXuCtbg8iC8YPGHfSVU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f26a4727-7ee8-406e-bcea-0682052b4b0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dcku9jBoXGVaGVNHQ46wHP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19202,
      "cache_read_input_tokens": 31527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19202,
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

_source line 34 · 2026-05-20T08:50:00.434Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UWRrTcd8ujDGki45fHzJhL`</summary>

```json
{
  "pattern": "**/review_report.md",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f26a4727-7ee8-406e-bcea-0682052b4b0b",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXuCtbg8iC8YPGHfSVU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88d4fe9f-7cd0-4dac-a6b8-116795aa6571",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dcku9jBoXGVaGVNHQ46wHP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19202,
      "cache_read_input_tokens": 31527,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19202
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 31527,
          "cache_creation_input_tokens": 19202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19202,
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

_source line 35 · 2026-05-20T08:50:00.446Z_

<details><summary>↩ Tool result · `toolu_01UWRrTcd8ujDGki45fHzJhL`</summary>

```text
artifacts/dream_reports/dream_20260520T074549/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88d4fe9f-7cd0-4dac-a6b8-116795aa6571",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "a68b8643-7e48-4415-bcca-7e1a6fa3b772",
  "sourceToolAssistantUUID": "88d4fe9f-7cd0-4dac-a6b8-116795aa6571",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-20T08:50:03.232Z_

Now let me submit my R2 review focused on novelty and related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a68b8643-7e48-4415-bcca-7e1a6fa3b772",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXuanE1Sf3f4jf65g4U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c0e53fb-deb8-4674-b66c-dd19fa1d85b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3YpU6GAcxhRx3Yh1oKbgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 164,
      "cache_read_input_tokens": 50729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 164,
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

_source line 37 · 2026-05-20T08:50:03.616Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KXp5rqaBbuGxJvgtEmvKta`</summary>

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
  "parentUuid": "0c0e53fb-deb8-4674-b66c-dd19fa1d85b7",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXuanE1Sf3f4jf65g4U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e6539f5-784f-4725-98f3-2fb7cbb10d6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3YpU6GAcxhRx3Yh1oKbgK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 164,
      "cache_read_input_tokens": 50729,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 164
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 50729,
          "cache_creation_input_tokens": 164,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 164,
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

_source line 38 · 2026-05-20T08:50:03.619Z_

<details><summary>↩ Tool result · `toolu_01KXp5rqaBbuGxJvgtEmvKta`</summary>

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
  "parentUuid": "8e6539f5-784f-4725-98f3-2fb7cbb10d6d",
  "isSidechain": true,
  "promptId": "af5eafdd-18df-466b-baef-eae9a8b502e4",
  "agentId": "acd414964c7e72df6",
  "type": "user",
  "uuid": "17a735c5-de8c-4ad4-b606-884899a2bfb5",
  "sourceToolAssistantUUID": "8e6539f5-784f-4725-98f3-2fb7cbb10d6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T08:51:49.923Z_



Now I have all the context needed. Let me produce the R2 review.

## R2 Review: Novelty and Related Work

### Summary
This paper systematically characterizes how multi-class (K>=3) annotation errors propagate through six canonical DAG topologies in causal inference, introduces Annotation Sensitivity Values (ASVs) analogous to E-values, and provides a correction guidance framework. The core finding -- that the classical binary "toward-null" guarantee breaks in a topology-dependent manner for K>=3 -- is genuinely novel in its systematic scope, though the individual pieces draw heavily on well-established measurement error theory. The paper occupies a valuable niche between the epidemiology measurement error literature and the NLP/CSS annotation error literature, but under-acknowledges the depth of prior work in both fields.

### Strengths

S1. **The topology-dependent dichotomy is a genuine contribution.** While Brenner (1993) showed polytomous confounder misclassification can bias in either direction, no prior work has systematically mapped this phenomenon across multiple DAG topologies. The clean separation into "information-loss" topologies (confounding, instrument, M-bias: zero violations) versus "structural-distortion" topologies (exposure, mediation, collider, front-door: 34-85% violations) is conceptually elegant and, to my knowledge, new. This is the kind of organizing result that changes how practitioners think about the problem.

S2. **The ASV framework is a non-trivial conceptual adaptation.** Adapting the E-value paradigm from unmeasured confounding to annotation error is not a trivial mapping. The key difficulty -- that annotation error is parameterized by a K x K matrix rather than a scalar -- requires meaningful technical innovation. The Frobenius-norm perturbation parameterization and the topology-specific proof techniques (algebraic, envelope theorem, Lagrangian/KKT) reflect genuine mathematical work. The honest separation of proved versus conjectured results is commendable.

S3. **The binarization collapse analysis closes an important loophole.** A predictable reviewer objection is "just binarize." Showing that binarization itself introduces up to Delta=0.19 additional bias and can flip bias direction in 12% of scenarios is a valuable and actionable finding. This preempts the most natural practitioner escape route and strengthens the motivation for the full multi-class framework.

S4. **Theory-to-practice completeness.** The paper delivers a full pipeline: diagnosis (taxonomy) -> assessment (ASV) -> action (correction guidance) -> implementation (toolkit). This is rare in measurement-error theory papers, which typically stop at the characterization stage. The 95% recommendation accuracy of the correction framework across 432 scenarios is a strong practical result.

S5. **The Dirichlet subspace analysis (mentioned in project memory but underplayed in the paper) provides crucial practical calibration.** The finding that amplification persists at ~12% even at diag>=0.9 demonstrates that the reversal phenomenon is not merely a pathological curiosity but a real risk even for high-accuracy LLMs.

### Weaknesses

W1. **[Major] The "first systematic multi-class treatment" claim overstates novelty relative to the epidemiology literature.** The paper cites Brenner (1993) for the direction-reversal observation and Carroll et al. (2006) as a textbook, but the epidemiology literature on polytomous misclassification is substantially deeper than this two-citation treatment suggests. Specifically:

- **Veierod and Laake (2001)** derive bias expressions for multi-category exposure misclassification in Poisson regression, showing bias depends on all true coefficients weighted by the full misclassification matrix. This is listed in the project's own literature_map.yaml but absent from the paper. The paper's exposure DAG bias expressions are extensions of this work to a broader DAG framework, not wholly new.
- **Dosemeci et al. (1990)** and **Birkett (1992)** provide early systematic treatments of polytomous exposure misclassification showing away-from-null bias.
- **Ogburn and VanderWeele (2012)** specifically address mediator misclassification -- directly relevant to the mediation topology that is one of the paper's headline results.
- **Jurek et al. (2005)** provide a systematic review of exposure misclassification bias direction in epidemiological studies, including multi-category cases.

The paper's contribution is real -- none of these prior works cover six topologies systematically or provide the clean dichotomy -- but the framing of "first" is misleading without properly engaging this prior art. The related work section gives the impression that Brenner (1993) is the only predecessor for polytomous misclassification, when in fact there is a substantial body of work that the paper needs to position against more carefully.

W2. **[Major] The ASV framework's relationship to existing sensitivity analysis tools is under-discussed.** The paper cites VanderWeele and Ding (2017) for E-values and VanderWeele and Li (2019) for binary measurement error sensitivity bounds, but the sensitivity analysis literature is much richer:

- **Rosenbaum (2002)** sensitivity analysis framework for observational studies, which uses a similar "how much violation of the assumption is needed to overturn the conclusion" structure.
- **Ding and VanderWeele (2016)** provide sensitivity analysis for unmeasured confounding with multi-valued treatments -- the multi-valued treatment case parallels the multi-class annotation case.
- **Lash et al. (2009, 2014)** probabilistic bias analysis for misclassification, which uses the confusion matrix directly as a sensitivity parameter -- this is strikingly similar to the ASV approach.
- **Fox et al. (2005)** provide a tutorial on applying probabilistic sensitivity analysis to misclassification that includes multi-category variables.

The ASV framework appears to be a fusion of the E-value reporting paradigm with probabilistic bias analysis for misclassification. This is a useful synthesis, but the novelty claim is weakened by not acknowledging these predecessors. The paper should clearly delineate what ASVs add beyond applying existing probabilistic bias analysis with E-value-style reporting.

W3. **[Moderate] The correction guidance framework's novelty is unclear relative to Jerzak et al. (2025).** The paper criticizes Jerzak et al. for "treating annotation error as monolithic" and claims the guidance framework conditions on topology and C structure. However, the paper does not describe the decision logic of the framework in sufficient detail for a reviewer to assess whether this is a principled methodological contribution or an engineering exercise. Is the recommendation rule a formal decision-theoretic framework, a lookup table from simulation results, or a heuristic? The 95% accuracy metric is meaningful only if the recommendation rule generalizes beyond the 432 training scenarios. Without clarity on the framework's internal logic, it is difficult to evaluate novelty.

W4. **[Moderate] PPI citation is missing.** The correction framework recommends PPI (prediction-powered inference) in 24% of scenarios, but the paper does not cite **Angelopoulos et al. (2023)** who introduced PPI. This is a significant omission -- recommending a method without citing its source undermines scholarly rigor. Similarly, the DSL method should cite **Gligoric et al. (2025)** (listed in the literature map but absent from the references).

W5. **[Moderate] Hernan and Cole (2009) is cited in the references but never discussed in the text.** This paper formalizes starred-node DAGs and the differential/non-differential error taxonomy that is foundational to the current paper's framework. The literature_map.yaml describes it as a "core theoretical foundation," yet it appears only as a phantom citation. The paper should explicitly acknowledge this as the source of its DAG-based error reasoning framework.

W6. **[Minor] The claim that direction reversal is "topology-specific" is somewhat oversold.** Brenner (1993) already showed direction reversal for polytomous confounder misclassification -- but the paper's own results show ZERO violations for the confounding topology. This means either (a) Brenner's result applies to a different estimand/setup than the paper tests, or (b) there is an inconsistency. The paper should clarify this discrepancy explicitly. If Brenner's "either direction" result applies to a different parameterization (e.g., stratified analysis rather than OLS regression), this should be stated.

W7. **[Minor] The SIMEX and regression calibration literatures are entirely absent.** SIMEX (Cook and Stefanski, 1994) and regression calibration (Carroll et al., 2006 Chapter 4) are standard methods for measurement error correction. Even if they are less applicable to the multi-class categorical case, they should be discussed as the dominant paradigm in measurement error correction that the paper's correction framework complements or supersedes.

### Questions for Authors

Q1. How does the exposure DAG bias expression relate to Veierod and Laake (2001)'s result for multi-category exposure misclassification? Is the closed-form expression in Section 3.2 a generalization, a special case, or an independent derivation of the same result? This relationship must be made explicit.

Q2. How does the ASV framework differ from probabilistic bias analysis (Lash et al., 2009) applied to confusion matrices? Both use the confusion matrix as a sensitivity parameter and ask "how much misclassification is needed to change the conclusion." If the key difference is the E-value-style scalar reporting, this should be stated explicitly.

Q3. The confounding topology shows zero violations in 100K random C matrices, but Brenner (1993) showed polytomous confounder misclassification can bias "in either direction." Can you reconcile this? Is Brenner's result about a different estimand, a different definition of "toward null," or does your DGP not cover Brenner's counterexample?

Q4. What is the decision logic of the correction guidance framework? Is it a formal decision rule (e.g., minimizing expected posterior loss), a simulation-calibrated lookup table, or expert-encoded heuristics? How would it generalize to a topology/C structure combination not in the 432 training scenarios?

Q5. The non-differential misclassification assumption is central to all theoretical results. LLM annotation errors are known to be context-dependent (e.g., longer texts may be harder to classify). Have you characterized the sensitivity of the reversal rates to violations of non-differentiality?

Q6. The empirical validation places each CSS task into three "topological contexts." Are these drawn from real published research designs, or are they hypothetical? If hypothetical, the empirical validation demonstrates framework mechanics rather than real-world applicability, and the framing should reflect this.

### Minor Issues

M1. Carroll et al. (2006) is listed as a key reference in the literature map and mentioned in the paper summary but does not appear in the actual bibliography of the submitted paper. It should be cited.

M2. The paper lists 11 references. For a paper that claims to bridge epidemiology measurement error theory, NLP annotation error, and sensitivity analysis, this is thin. I would expect 25-35 references for adequate coverage.

M3. Baumann et al. (2025) is cited as "Baumann, L., et al." but the literature map lists the first author as "Baumann, M." -- verify the correct attribution.

M4. The abstract mentions "six canonical DAG topologies" but the paper actually covers seven rows in Table 1 (adding "exposure" separately from "confounding"). Clarify whether these are six or seven distinct topologies.

M5. Table 1 lists "M-bias" as a topology, but M-bias is typically described as a type of confounding structure (butterfly DAG), not a standard "canonical" topology in the CSS literature. Justify its inclusion or replace with a more standard choice.

M6. The paper uses "structural-distortion" versus "information-loss" as topology categories -- these are useful but appear to be novel terminology. Provide formal definitions, not just intuitive descriptions.

### Missing References

**Epidemiology / measurement error (must cite):**
- Veierod, M.B. and Laake, P. (2001). "Exposure misclassification: bias in category specific Poisson regression coefficients." *Statistics in Medicine*, 20(3):411-421. -- Multi-category exposure misclassification bias expressions.
- Ogburn, E.L. and VanderWeele, T.J. (2012). "Analytic results on the bias due to nondifferential misclassification of a binary mediator." *AJE*, 176(6):555-561. -- Directly relevant to the mediation topology.
- Lash, T.L., Fox, M.P., and Fink, A.K. (2009/2014). *Applying Quantitative Bias Analysis to Epidemiologic Data.* Springer. -- Probabilistic bias analysis using confusion matrices as sensitivity parameters.
- Dosemeci, M., Wacholder, S., and Lubin, J.H. (1990). "Does nondifferential misclassification of exposure always bias a true effect toward the null value?" *AJE*, 132(4):746-748. -- Early demonstration that the toward-null guarantee fails for polytomous exposure.
- Jurek, A.M., Greenland, S., Maldonado, G., and Church, T.R. (2005). "Proper interpretation of non-differential misclassification effects: expectations vs observations." *IJE*, 34(3):680-687. -- Systematic review of when toward-null fails.

**Sensitivity analysis (should cite):**
- Rosenbaum, P.R. (2002). *Observational Studies.* Springer. -- Foundational sensitivity analysis framework.
- Ding, P. and VanderWeele, T.J. (2016). "Sensitivity analysis without assumptions." *Epidemiology*, 27(3):368-377. -- Multi-valued treatment sensitivity analysis.
- Fox, M.P., Lash, T.L., and Greenland, S. (2005). "A method to automate probabilistic sensitivity analyses of misclassified binary variables." *IJE*, 34(6):1370-1376.

**Correction methods (must cite):**
- Angelopoulos, A.N., et al. (2023). "Prediction-powered inference." *Science*, 382(6671):669-674. -- Source of the PPI method recommended by the correction framework.
- Gligoric, K., Jurafsky, D., and Zou, J. (2025). "Can unconfident LLM annotations be used for confident conclusions?" *NAACL 2025*. -- Source of the DSL method.

**Measurement error correction (should discuss):**
- Cook, J.R. and Stefanski, L.A. (1994). "Simulation-extrapolation estimation in parametric measurement error models." *JASA*, 89(428):1314-1328. -- SIMEX, the dominant simulation-based correction approach.

**Additional NLP/CSS:**
- Messing, S. (2026). "Hidden Measurement Error in LLM Pipelines." *arXiv:2604.11581*. -- Variance decomposition that explicitly excludes causal identification (the gap this paper fills).

### Novelty Assessment

**Contribution 1 (Multi-class bias taxonomy): Moderate-to-high novelty.**
The individual bias expressions for specific topologies build on established measurement error theory (Brenner 1993, Veierod & Laake 2001, Ogburn & VanderWeele 2012). The genuinely novel element is the *systematic comparison across six topologies* yielding the information-loss vs. structural-distortion dichotomy. No prior work has produced this organizing result. However, the novelty is diminished by (a) the under-acknowledged depth of prior polytomous misclassification literature, and (b) the fact that Dosemeci et al. (1990) already demonstrated away-from-null bias for polytomous non-differential exposure misclassification 35 years ago. The paper's contribution is systematic characterization, not the first observation of the phenomenon.

**Contribution 2 (ASVs): Moderate novelty.**
The conceptual move of applying E-value-style reporting to measurement error is valuable, but probabilistic bias analysis (Lash et al., 2009) already uses confusion matrices as sensitivity parameters and asks equivalent questions. The novelty is in (a) the formal monotonicity/sharpness proofs, (b) the topology-specific proof techniques, and (c) the single-scalar reporting format. The E-value analogy is apt but also limiting -- the richer parameterization of K x K matrices means ASVs inevitably sacrifice information relative to full probabilistic bias analysis. The paper should discuss this tradeoff.

**Contribution 3 (Correction guidance): Low-to-moderate novelty.**
Without clarity on the decision logic, this reads as a simulation-calibrated lookup table rather than a principled methodological contribution. The value is practical (practitioners need actionable guidance), but the intellectual contribution is thin unless the decision framework has a formal basis. The missing citations for PPI and DSL further weaken this contribution.

**Overall:** The paper's novelty is concentrated in Contribution 1 (the topology-dependent dichotomy). This is a genuine and useful organizing result that synthesizes scattered prior observations into a coherent framework. Contributions 2 and 3 are useful but more incremental. The paper would benefit from more honest positioning: "we provide the first systematic multi-class treatment across six DAG topologies" is defensible; "first systematic multi-class treatment" without the topology qualifier overstates novelty relative to the substantial prior epidemiology literature.

### Score: 4/6
### Confidence: 4/5

**Rationale:** The topology-dependent dichotomy is a genuine contribution that merits publication at a top venue, but the related work coverage has significant gaps that inflate the perceived novelty. The missing citations for PPI/DSL, the under-engagement with the epidemiology polytomous misclassification literature, and the unclear novelty of the correction framework prevent a higher score. With thorough revision of the related work section (expanding from 11 to ~30 references), explicit engagement with Veierod & Laake (2001) and Lash et al. (2009/2014), and clarification of the correction framework's decision logic, this paper would likely merit a 5. The core result is strong; the packaging needs work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17a735c5-de8c-4ad4-b606-884899a2bfb5",
  "isSidechain": true,
  "agentId": "acd414964c7e72df6",
  "requestId": "req_011CbDXupPnBdvLzZ6eKmDVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39c0aef4-c2f4-4cfc-a350-faedfd800281",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "44efd5d7-3d5f-464d-80ca-d3c01b5a58d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01875QMnYQ9uqrBM95GwQt8n",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 50893,
      "output_tokens": 4373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 731
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4373,
          "cache_read_input_tokens": 50893,
          "cache_creation_input_tokens": 731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 731,
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
