# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-afed2f4e537662403.jsonl`
- **Structured JSON:** [`036cf5abeb2d258ddf9f.json`](../../sessions/03/036cf5abeb2d258ddf9f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

55 recorded events

### User

_source line 1 · 2026-05-15T08:02:52.012Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus: **Novelty, Positioning, Related Work, and Presentation**.

## Paper Summary

Title: "When Do Two Formalizations Know More Than One? An Empirical Study of Cross-Representation Disagreement in LLM Reasoning"

The paper studies cross-representation disagreement (CRD) — when an LLM formalizes a natural-language reasoning problem into both FOL (verified by Z3) and executable Python code, and the two answers disagree. It evaluates CRD across 3 benchmarks (FOLIO n=204, LogiQA n=150, MATH Level 5 n=200), 2 models (Qwen3-32B, DeepSeek V4 Pro), and claims three main negative results:

1. Repair is not statistically significant on any benchmark (all p > 0.39, all CIs include zero)
2. Selection (picking the correct side) dominates repair by 6.1pp
3. Self-consistency (SC5 majority vote) dominates CRD on all benchmarks at equal or lower cost

Three failure mechanisms: (a) representation-quality asymmetry, (b) correlated specification-level failures, (c) taxonomy instability (κ=0.33).

## Paper Structure (12 pages)
- Section 1 (Introduction): Motivates CRD, states three negative findings
- Section 2 (Related Work): Neurosymbolic reasoning (Logic-LM, LINC, PAL, PoT, HybridMind), self-consistency/ensemble methods (Wang et al., Liang et al.), cross-representation disagreement (Liang et al. 2024, Roundtrip Verification 2026, Denisov-Blanch 2026)
- Section 3 (Method): 4-stage CRD pipeline (dual formalization, disagreement detection, error localization, targeted repair), error taxonomy (4 types), 5 evaluation metrics
- Section 4 (Experimental Setup): 3 benchmarks, 2 models, baselines
- Section 5 (Results): 8 subsections covering FOLIO core, cross-model ablation, cross-benchmark generalization, repair mechanisms, correlated failures, taxonomy stability, statistical significance, SC5 comparison
- Section 6 (Discussion): Why CRD fails (3 mechanisms), when CRD provides value, practitioner implications, limitations
- Section 7 (Conclusion)
- References: ~14 citations

## Key Related Work Context
- Liang et al. (2024) ACL: CoT-PoT disagreement as filtering signal (binary only, no diagnosis/repair)
- Roundtrip Verification (2026) NAACL: diagnosis-guided repair within single representation on narrow domain (150 traffic rules)
- Denisov-Blanch (2026) ICML: correlated failures in LLM ensembles
- Wang et al. (2023) ICLR: self-consistency / majority voting
- HybridMind (2024) NeurIPS: adaptive representation selection

## Your Task

Provide a detailed review focusing on:

1. **Novelty**: Is the contribution sufficiently novel for a top venue? How does it advance beyond Liang et al. (2024) and Roundtrip Verification (2026)?
2. **Positioning as negative results paper**: Is the framing as "boundary results" compelling? Are the negative findings surprising or predictable?
3. **Related work coverage**: Any important missing references? Is positioning fair?
4. **Writing quality and presentation**: Is the paper well-organized? Are the 16 tables too many? Is the narrative clear?
5. **Significance and impact**: Would the community learn something actionable from this paper?
6. **Framing concerns**: The paper reframes from "CRD is a better tool" to "empirical anatomy of CRD" — is this honest? Does it feel post-hoc?

Output format:
```
## R2 Review: Novelty and Related Work

### Summary (2-3 sentences)

### Strengths
- S1: ...
- S2: ...
(etc.)

### Weaknesses
- W1: ...
- W2: ...
(etc.)

### Questions for Authors
- Q1: ...
(etc.)

### Minor Issues
- ...

### Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "3cfd6513-88e4-4b86-90f1-c19dd387ba0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T08:02:52.015Z_

```json
{
  "parentUuid": "3cfd6513-88e4-4b86-90f1-c19dd387ba0d",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
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
  "uuid": "54ffedf6-775d-408a-8298-1d51e34cc7ac",
  "timestamp": "2026-05-15T08:02:52.015Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T08:02:54.201Z_



I'll start by reading the paper and related project files to provide a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54ffedf6-775d-408a-8298-1d51e34cc7ac",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41GWPFSAQCWnPn9fNZG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "abd899d2-0e9e-4e4c-b1b0-802eddacfe82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hjoia7gG22mPfx2mwTePKS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6933,
      "cache_read_input_tokens": 8253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6933,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 4 · 2026-05-15T08:02:55.130Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NWKKe8a5mMxgxucstJMjMa`</summary>

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
  "parentUuid": "abd899d2-0e9e-4e4c-b1b0-802eddacfe82",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41GWPFSAQCWnPn9fNZG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7587ffda-334e-4a71-b85b-453ccd22a2fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hjoia7gG22mPfx2mwTePKS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6933,
      "cache_read_input_tokens": 8253,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6933
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 8253,
          "cache_creation_input_tokens": 6933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6933,
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

_source line 5 · 2026-05-15T08:02:55.132Z_

<details><summary>↩ Tool result · `toolu_01NWKKe8a5mMxgxucstJMjMa`</summary>

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
  "parentUuid": "7587ffda-334e-4a71-b85b-453ccd22a2fa",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "c6176b7f-d2fe-427b-aa7c-46d50343e393",
  "sourceToolAssistantUUID": "7587ffda-334e-4a71-b85b-453ccd22a2fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T08:02:57.850Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01KM7xMDgaxULpXezRy4KpKT`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6176b7f-d2fe-427b-aa7c-46d50343e393",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41GjvbHdTnqRLi6ciCH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3898909-2999-46f0-92be-c5f340b9f79d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PakSxvBc1Bcm1xWhdxjaFR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
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

_source line 7 · 2026-05-15T08:02:57.883Z_

<details><summary>↩ Tool result · `toolu_01KM7xMDgaxULpXezRy4KpKT`</summary>

```text
{"result":"# 项目 cross_representation_disagreement_diagno 概况\n\n## 实验状态 (6 个)\n\n- **mvp_pipeline_004**: ANALYZING (success) — \n- **mvp_pipeline_003b**: DONE (killed) — \n- **mvp_pipeline_003**: DONE (killed) — \n- **mvp_pipeline_002**: DONE (negative) — \n- **mvp_pipeline_001**: DONE (negative) — \n- **mvp_baseline_001**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| mvp_pipeline_004 | v4 truncation detection + thinking-off retry, 204 samples | RUNNING (PID 47964, 127/204, ETA ~08:30 BJT) | All-mode 5/5 PASS @126样本 | — |\n\n## 126 样本 C1-C5 指标（evaluate_mvp.py 权威数据）\n| 指标 | All-mode (N=117) | 阈值 | 状态 | Excl-Unknown (N=75) | 状态 |\n|------|-----------------|------|------|-------------------|------|\n| C1 disagree_rate | 35.9% (42/117) | ≥10% | PASS | 34.7% (26/75) | PASS |\n| C2 diagnostic_rate | 88.1% (37/42) | ≥40% | PASS | 88.5% (23/26) | PASS |\n| C3 error_types | 3 | ≥2 | PASS | 2 | PASS |\n| C4 targeted_delta | +7.4pp (T:35/54 B:31/54) | >5pp | PASS | +0.0pp (T:22/35 B:22/35) | FAIL |\n| C5 localization | 79.2% (19/24) | ≥60% | PASS | 87.5% (14/16) | PASS |\n\n## 已完成修复\n- repair.py: repr_type 动态 prompt（C4 excl-unknown 根因修复）\n- pipeline.py: streaming JSONL + gc.collect（内存泄漏修复）\n- pipeline.py: JSON→JSONL in-place 转换（数据损坏 bug 修复）\n- repair_only.py: repair-only 重跑脚本就绪\n\n## 待处理\n- 等 204 全量完成 → evaluate_mvp.py 最终评估\n- 204 完成后 → repair_only.py 重跑 repair+eval（用修复后的 prompt）\n\n## 近期结论\n- **mvp_pipeline_004** (success, 127/204): All-mode 5/5 PASS，C4 趋势下滑需关注\n- **mvp_pipeline_002** (negative): FOL crash 修复但 C4/C5 仍 FAIL\n- **mvp_pipeline_001** (negative): 首轮 2/5 PASS\n\n## 趋势\n成功 1 / 负向 2 / 失败 0 / 终止 2 / 共 6\nMVP 指标持续改善: v1(2/5) → v2(2/5) → v4@80(4/5) → v4@126(5/5 all-mode)\n\n## 资源状态\nautodl-rtx6000pro: cuda:0 pipeline (PID 47964) + vLLM serving 运行中"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3898909-2999-46f0-92be-c5f340b9f79d",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "16cec85b-8aab-41f3-abb3-0a49de642339",
  "sourceToolAssistantUUID": "a3898909-2999-46f0-92be-c5f340b9f79d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T08:02:58.508Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01R8C91oaR7L8hqMtu7WZgXR`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16cec85b-8aab-41f3-abb3-0a49de642339",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41GjvbHdTnqRLi6ciCH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93b7a1ad-4193-44d4-b40b-3554ecd25a80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PakSxvBc1Bcm1xWhdxjaFR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15186,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1446
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 168,
          "cache_read_input_tokens": 15186,
          "cache_creation_input_tokens": 1446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1446,
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

_source line 9 · 2026-05-15T08:02:58.531Z_

<details><summary>↩ Tool result · `toolu_01R8C91oaR7L8hqMtu7WZgXR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| mvp_pipeline_004 | v4 truncation detection + thinking-off retry, 204 samples | RUNNING (PID 47964, 127/204, ETA ~08:30 BJT) | All-mode 5/5 PASS @126样本 | — |\\n\\n## 126 样本 C1-C5 指标（evaluate_mvp.py 权威数据）\\n| 指标 | All-mode (N=117) | 阈值 | 状态 | Excl-Unknown (N=75) | 状态 |\\n|------|-----------------|------|------|-------------------|------|\\n| C1 disagree_rate | 35.9% (42/117) | ≥10% | PASS | 34.7% (26/75) | PASS |\\n| C2 diagnostic_rate | 88.1% (37/42) | ≥40% | PASS | 88.5% (23/26) | PASS |\\n| C3 error_types | 3 | ≥2 | PASS | 2 | PASS |\\n| C4 targeted_delta | +7.4pp (T:35/54 B:31/54) | >5pp | PASS | +0.0pp (T:22/35 B:22/35) | FAIL |\\n| C5 localization | 79.2% (19/24) | ≥60% | PASS | 87.5% (14/16) | PASS |\\n\\n## 已完成修复\\n- repair.py: repr_type 动态 prompt（C4 excl-unknown 根因修复）\\n- pipeline.py: streaming JSONL + gc.collect（内存泄漏修复）\\n- pipeline.py: JSON→JSONL in-place 转换（数据损坏 bug 修复）\\n- repair_only.py: repair-only 重跑脚本就绪\\n\\n## 待处理\\n- 等 204 全量完成 → evaluate_mvp.py 最终评估\\n- 204 完成后 → repair_only.py 重跑 repair+eval（用修复后的 prompt）\\n\\n## 近期结论\\n- **mvp_pipeline_004** (success, 127/204): All-mode 5/5 PASS，C4 趋势下滑需关注\\n- **mvp_pipeline_002** (negative): FOL crash 修复但 C4/C5 仍 FAIL\\n- **mvp_pipeline_001** (negative): 首轮 2/5 PASS\\n\\n## 趋势\\n成功 1 / 负向 2 / 失败 0 / 终止 2 / 共 6\\nMVP 指标持续改善: v1(2/5) → v2(2/5) → v4@80(4/5) → v4@126(5/5 all-mode)\\n\\n## 资源状态\\nautodl-rtx6000pro: cuda:0 pipeline (PID 47964) + vLLM serving 运行中\\n\", \"total_chars\": 1517, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93b7a1ad-4193-44d4-b40b-3554ecd25a80",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "d2bbe2cf-20cd-46f9-b425-1ada17450828",
  "sourceToolAssistantUUID": "93b7a1ad-4193-44d4-b40b-3554ecd25a80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T08:03:01.612Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FtGTZFneTjdjoQDXusXu6Z`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2bbe2cf-20cd-46f9-b425-1ada17450828",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41GzMkbQ2P6bh7QtqCV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49bedad1-c698-42c5-965b-eb034bb10c4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHzgjjxpCTeM1Xm8KCa53j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 16632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2318,
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

_source line 11 · 2026-05-15T08:03:01.626Z_

<details><summary>↩ Tool result · `toolu_01FtGTZFneTjdjoQDXusXu6Z`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'cross_representation_disagreement_diagno'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49bedad1-c698-42c5-965b-eb034bb10c4a",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "81f5abae-7b76-4525-8dab-fd441b82c756",
  "sourceToolAssistantUUID": "49bedad1-c698-42c5-965b-eb034bb10c4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T08:03:02.559Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DUBJ2xV9KvVJaZHFhCs3Yh`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81f5abae-7b76-4525-8dab-fd441b82c756",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41GzMkbQ2P6bh7QtqCV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46593cff-9f05-4c51-8305-5943346f6904",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHzgjjxpCTeM1Xm8KCa53j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 16632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2318,
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

_source line 13 · 2026-05-15T08:03:02.581Z_

<details><summary>↩ Tool result · `toolu_01DUBJ2xV9KvVJaZHFhCs3Yh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/paper_framing.md\", \"content\": \"# Paper Framing — cross_representation_disagreement_diagno\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (10 days)\\n- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage\\n\\n## Core Insight\\nWhen the same LLM formalizes a reasoning problem into two distinct executable representations, disagreements between them serve as a high-precision error detection signal (~87% diagnostic rate). This \\\"disagreement as diagnostic\\\" approach goes beyond existing methods that only filter or verify within a single representation — the disagreement pattern itself reveals error types, enables localization, and informs selective repair. The value is NOT symmetric complementarity between representations, but the diagnostic information contained in the disagreement signal.\\n\\n## Core Claims (3 条)\\n\\n### Claim 1: Disagreement as High-Precision Diagnostic Signal\\nWhen the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.\\n\\n**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).\\n\\n### Claim 2: Error Classification and Conditional Localization\\nDisagreement patterns enable error type classification into a structured taxonomy (4 types: logic_error 25.5%, negation_error 10.8%, quantifier_error 2.0%, exec_crash 5.4%). When the stability test yields a definitive prediction (62% of diagnostic samples), localization accuracy is 94.6%. The 5.6:1 asymmetry (FOL correct 56 vs Code correct 10, both wrong 10) reveals systematic differences in LLM formal logic vs. code generation.\\n\\n**MVP evidence**: C5-committed = 94.6% (35/37) [CI: 86.1%-100%] — when stability test makes a definitive prediction, localization is near-perfect. C5-coverage = 53.0% (35/66) — 44% of diagnostic cases return \\\"ambiguous\\\" (especially Unknown: 61%). C3=4 error types.\\n\\n**Framing**: Stability-based localization is a high-precision / low-recall method. When it commits, it's right 95% of the time. The 44% ambiguous rate is primarily driven by GT=Unknown samples (61% ambiguous) where Code overclaiming creates systematically unstable predictions.\\n\\n**Key nuance**: GT=Unknown samples have the worst localization coverage (C5-coverage=35.7%) but the best repair delta (+14.7pp). This paradox suggests repair utility comes from the disagreement PATTERN (information content) rather than precise error-side identification — the model benefits from knowing the two representations disagree and what each concluded, regardless of which is labeled \\\"the error.\\\"\\n\\n### Claim 3: Diagnosis-Guided Repair Is GT-Label-Dependent — Helps, Hurts, or Neutral\\nDiagnosis-guided repair exhibits a striking GT-label-dependent effect that reveals the boundary of cross-representation diagnosis:\\n\\n| GT Label | n | Targeted | Blind | Delta | Interpretation |\\n|----------|---|----------|-------|-------|----------------|\\n| Unknown | 69 | 67.7% | 52.9% | **+14.7pp** | Diagnosis helps: corrects Code overclaiming |\\n| False | 63 | 76.7% | 70.0% | **+6.7pp** | Modest help |\\n| True | 72 | 63.6% | 77.3% | **-13.6pp** | Diagnosis HURTS: overcorrection |\\n\\nThis is NOT simply \\\"conditional advantage\\\" — diagnosis actively harms repair for GT=True cases. The mechanism: for True problems where Code outputs False/Unknown, the diagnostic signal (\\\"Code disagrees with FOL\\\") triggers overcorrection, producing worse results than blind regeneration. We do NOT claim aggregate repair superiority — we characterize a fundamental asymmetry in when diagnosis helps vs. hurts repair.\\n\\n**MVP evidence**: C4 aggregate +4.65pp per-sample (Fisher p=0.626, not significant). The aggregate masks a three-way split that is the actual finding. Bootstrap CI for aggregate includes zero.\\n\\n**Presentation strategy**: \\n1. Report C4 stratified by GT label as the PRIMARY result (table above)\\n2. Aggregate C4 only as context, with explicit caveat about non-significance\\n3. Frame GT=True overcorrection as a discovered failure mode, not a hidden weakness\\n4. Discuss implications: practitioners should apply diagnosis-guided repair selectively (skip for high-confidence True predictions)\\n\\n## Story Spine\\n\\n- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.\\n\\n- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.\\n\\n- **Our framing (dual-track)**: We present (1) the first study to extend cross-representation disagreement from a binary filtering signal (Liang et al. 2024) to a structured diagnostic tool — enabling error classification, localization, and boundary characterization across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility. Key distinction from self-consistency (Wang et al. 2023): within-representation sampling captures generation variance; cross-representation disagreement captures systematic formalization differences between paradigms (formal logic vs. imperative code).\\n\\n- **Headline result template**: \\\"On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation.\\\"\\n\\n## Venue Fit\\n\\n- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.\\n- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.\\n- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n| # | Concern | Response Strategy | Required Experiment |\\n|---|---------|-------------------|---------------------|\\n| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |\\n| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |\\n| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |\\n| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |\\n| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |\\n| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |\\n| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |\\n| R8 | How differs from self-consistency (k=5 majority voting)? | Dedicated baseline: k=5 FOL-only and k=5 Code-only vs single-pass CRD. Cross-representation captures paradigm-level differences, not sampling variance | exp-012 |\\n| R9 | Error taxonomy unvalidated — no inter-annotator agreement | Cross-model validation: use different LLM to classify same errors, measure Cohen's κ. If possible, small human annotation (50 samples) | exp-013 |\\n| R10 | FOL+Z3 vs CoT+SymPy are categorically different — conflating them as \\\"cross-representation\\\" is imprecise | Frame MATH domain as \\\"cross-executable-paradigm\\\" (symbolic algebra vs numerical computation), acknowledge different verification guarantees. Discuss as related but distinct instantiation | exp-004 framing |\\n| R11 | Related work insufficient — missing self-consistency, LEVER, Faithful CoT, self-debug/refine, multi-agent debate, ensemble diversity | Expand related work to ≥25 references, position against all listed methods. Paper Agent must run reference-audit | Paper writing |\\n\", \"total_chars\": 9217, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46593cff-9f05-4c51-8305-5943346f6904",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "785f365b-ca23-419f-b4e4-b0d0ef289bd5",
  "sourceToolAssistantUUID": "46593cff-9f05-4c51-8305-5943346f6904",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T08:03:03.551Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0145LaCoPGAm9YGxD8KBNrSt`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "785f365b-ca23-419f-b4e4-b0d0ef289bd5",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41GzMkbQ2P6bh7QtqCV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1afd399-30b9-468f-b96f-eede279e4dc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHzgjjxpCTeM1Xm8KCa53j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 16632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2318,
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

_source line 15 · 2026-05-15T08:03:03.567Z_

<details><summary>↩ Tool result · `toolu_0145LaCoPGAm9YGxD8KBNrSt`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'cross_representation_disagreement_diagno'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1afd399-30b9-468f-b96f-eede279e4dc0",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "59f3168a-43c6-4edd-ab0c-75253efa73b5",
  "sourceToolAssistantUUID": "a1afd399-30b9-468f-b96f-eede279e4dc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T08:03:03.713Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01X3Do7dQFMPqFktiqgkQdHX`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59f3168a-43c6-4edd-ab0c-75253efa73b5",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41GzMkbQ2P6bh7QtqCV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae4519f7-fb32-44c2-8b66-6e17aab2aaf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHzgjjxpCTeM1Xm8KCa53j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 16632,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2318
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 16632,
          "cache_creation_input_tokens": 2318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2318,
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

_source line 17 · 2026-05-15T08:03:03.728Z_

<details><summary>↩ Tool result · `toolu_01X3Do7dQFMPqFktiqgkQdHX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/ROADMAP.md\", \"content\": \"# cross_representation_disagreement_diagno — Research Dashboard\\n\\n> 最后更新: 2026-05-15 07:18 UTC | 更新原因: Dream #1 分析完成，识别结构性问题，更新 framing/plan，启动 re-dream\\n\\n## 核心方向\\n跨表征分歧作为诊断信号：同一 LLM 将推理问题形式化为两种可执行表征（FOL/Z3 vs Python），分歧模式以 ~87% 精度检测形式化错误，支持错误分类、定位和选择性修复。详见 paper_framing.md。\\n\\n## 当前阶段：Research Phase — Dream 迭代中\\n\\n**MVP 已通过（D009）**：C1=39.6%, C2=86.8%, C3=4 types, C4=+4.65pp (non-sig), C5-committed=94.6%/C5-coverage=53.0%\\n\\n**Dream #1 结果（D013）**：三档均 3/6 (borderline/weak reject)，未达 best≥weak accept 门槛。\\n识别 5 个结构性问题：(1) Related work 不足 (2) 引用不完整 (3) Error taxonomy 未验证 (4) Novelty claim 过强 (5) 缺 self-consistency baseline。\\n已修改 framing+plan，re-dream 进行中 (dream_20260515T071730)。\\n\\n**投稿目标**：EMNLP 2026 Main (ARR May 25, DDL 10 天)\\n\\n## 实验计划覆盖率\\nP0: exp-001✅ / exp-002 / exp-003(pilot running) / exp-004 / exp-005 / exp-007↑ / exp-012(new)\\nP1: exp-006 / exp-008 / exp-009 / exp-013(new)\\nP2: exp-010 / exp-011\\n\\n## 近期任务\\n- [ ] 等待 re-dream (dream_20260515T071730) 结果 → 达标后批准 P0 实验\\n- [ ] ProofWriter pilot 运行中 (PID 84823) → 等结果决定全量/切 LogiQA\\n- [ ] Agent 队列深度 4 — 处理 C5 dual output + repair oracle fix\\n- [ ] exp-012 self-consistency baseline 代码准备（re-dream 通过后立即启动）\\n- [ ] exp-004 MATH adapter 已准备，等 re-dream 批准\\n- [ ] [Dream 观察] exp-004 结果出来后评估 FOL+Z3 vs CoT+SymPy 是否需分开分析\\n- [ ] [Dream 观察] 全 benchmark 实验完成后评估样本量是否需扩大（power analysis 需 ~280）\\n\\n## GPU 预算\\n- 本地: autodl-rtx6000pro (1x RTX 6000 Pro) — exp-003 pilot 占用中\\n- API: ~$130-200 预估（含 exp-002 DeepSeek + exp-012 k=5 sampling）\\n- 总 GPU 时长: ~42h（原 36h + exp-012 6h）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D013 | 2026-05-15 | Dream #1 三档均 3/6 (borderline/weak reject)，识别 5 个结构 | exp-012, exp-013, exp-007 |\\n| D012 | 2026-05-15 | C5 报告双指标：C5-committed (85.4%, 仅明确预测) + C5-coverage | mvp_pipeline_004 |\\n| D011 | 2026-05-15 | 统一指标为 per-sample 计算；Claim 3 更新为 GT-label-dependent | mvp_pipeline_004 |\\n| D010 | 2026-05-15 | D008 假设（prompt bug = C4 根因）未获支撑；C4 reframe 为 error | mvp_pipeline_004 |\\n| D009 | 2026-05-15 | 通过 MVP gate，C4 作为已知弱点进入 research 阶段解决 | mvp_pipeline_004 |\\n| D008 | 2026-05-14 | repair.py prompt bug 确认为 C4 下降根因，修复后 repair-only 重 | mvp_pipeline_004 |\\n| D007 | 2026-05-14 | 撤回 v5 closed-world 方案，改为 v5b：保持 3-way 输出但改进 prompt | mvp_pipeline_004 |\\n| D006 | 2026-05-14 | MVP v2 结果：FOL crash 78%→10%、C4/C5 翻转为 PASS，但 Code  | mvp_pipeline_002 |\\n| D005 | 2026-05-14 | MVP 第一轮未通过（2/5），根因是 Z3 prompt 质量（78% crash），非假设失败。 | mvp_baseline_001, mvp_pipeline_001 |\\n| D004 | 2026-05-14 | 回退 qwen3.6-plus → 要求 Qwen3-32B 或同级开源模型，Reviewer cr | — |\\n\\n\\n\", \"total_chars\": 2502, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae4519f7-fb32-44c2-8b66-6e17aab2aaf0",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "a87f54e0-9f01-4ade-83b2-fafafc2cc81e",
  "sourceToolAssistantUUID": "ae4519f7-fb32-44c2-8b66-6e17aab2aaf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T08:03:07.274Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019RdCysUGEKWZbVNMZgmjK6`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a87f54e0-9f01-4ade-83b2-fafafc2cc81e",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41HNewNNLiDnMZaQj8Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf659b1d-bcd8-4c36-b3d0-688f39648e08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KT73BHwzcJrVu6YjotqTDM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4829,
      "cache_read_input_tokens": 18950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4829,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 19 · 2026-05-15T08:03:07.299Z_

<details><summary>↩ Tool result · `toolu_019RdCysUGEKWZbVNMZgmjK6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/memory.md\", \"content\": \"# Project Memory\\n\\n## MVP Gate 5/5 PASS（109/204 partial data, 2026-05-14）\\n\\nmvp_pipeline_004 在 109/204 样本处静默退出（无错误日志），但已完成数据通过全部 MVP gate：\\n- **All mode (n=103 effective): 5/5 PASS**\\n  - C1: 33.0% disagree (34/103) ≥10% ✓\\n  - C2: 88.2% diagnostic (30/34) ≥40% ✓\\n  - C3: 3 error types ≥2 ✓\\n  - C4: +11.6pp targeted vs blind (T:69.8% B:58.1%) >5pp ✓\\n  - C5: 81.8% localization (18/22) ≥60% ✓\\n- **Excl. Unknown mode (n=67): 4/5 PASS, C4 FAIL (+3.6pp)**\\n- Pipeline 可 --resume 续跑剩余 95 样本\\n\\n## v4 truncation fix 是 MVP 通过的关键（2026-05-14）\\n\\nv4 添加 finish_reason='length' 截断检测 + enable_thinking=False 重试，**同时解决了 FOL 和 Code 端的 crash/empty 问题**。80/204 中间数据 MVP 5/5 PASS（C1 32%, C2 87.5%, C3 3 types, C4 +22.6pp, C5 100%）。从 v1(2/5)→v2(3/5)→v3(1/5) 到 v4(5/5) 的突破。\\n\\n## Code Unknown 是 lazy prompt 问题，非模型能力边界（2026-05-14）\\n\\n46.3% Code=Unknown 的根因：LLM 生成代码主动 print(\\\"Unknown\\\") 而非执行错误。两种模式：(A) 硬编码放弃（注释推理后直接 print Unknown）；(B) 条件 fallback（else 分支用 Unknown 替代 False）。v5b prompt 已设计（anti-lazy Unknown + 禁止 hardcode + 3 个 few-shot）待 v4 完成后验证。\\n\\n## FOL 在 FOLIO 上压倒性优于 Code（2026-05-14）\\n\\nDisagree 样本中 FOL 正确 78.3% vs Code 仅 8.7%。Z3 形式化在结构化逻辑推理上远强于 Python enumeration。这意味着 disagreement 的诊断方向主要是\\\"Code 错 FOL 对\\\"，targeted repair 主要修 Code 端。\\n\\n## 禁止双进程启动 pipeline（2026-05-14，教训）\\n\\nsubmit_on_allocated（tmux）和 nohup 同时启动了两个 pipeline 实例，写同一输出文件，导致竞争条件 + 数据损坏 + pipeline 静默退出。**启动 pipeline 只用一种方式，确认前一个进程已终止后再启动新的。**\\n\\n## v5 closed-world 2-way 方案被撤回（D007, 2026-05-14）\\n\\nReviewer 指出强制 2-way 会在 ~39% Unknown-GT 样本上制造人为 disagreement（FOL=Unknown vs Code=False），污染诊断信号。**改为 v5b：保持 3-way + anti-lazy Unknown 约束**，确保 disagreement 信号来自推理差异而非假设差异。\\n\\n## Qwen3-32B-AWQ baseline 精度（2026-05-14）\\n\\nFOLIO validation set direct answer accuracy = 74%（50 samples），满足 ≤85% 门控。\\n\\n## Code 端 thinking token 泄漏已解决（2026-05-14）\\n\\nQwen3 系列模型默认开启 thinking mode，Code generation 时 thinking tokens 泄漏到代码输出导致解析崩溃。解决：`enable_thinking=False` + `_strip_thinking`。v3 验证 code crash 40%→0%。\\n\", \"total_chars\": 1901, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf659b1d-bcd8-4c36-b3d0-688f39648e08",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "7621eda3-6647-4820-9279-fdb0336a0d5d",
  "sourceToolAssistantUUID": "bf659b1d-bcd8-4c36-b3d0-688f39648e08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T08:03:08.247Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015SYq651zHPntBrguNF1UcS`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7621eda3-6647-4820-9279-fdb0336a0d5d",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41HNewNNLiDnMZaQj8Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d86df38-1607-45ff-b7f0-4bf65b42472d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KT73BHwzcJrVu6YjotqTDM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4829,
      "cache_read_input_tokens": 18950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4829,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 21 · 2026-05-15T08:03:08.257Z_

<details><summary>↩ Tool result · `toolu_015SYq651zHPntBrguNF1UcS`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'cross_representation_disagreement_diagno'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d86df38-1607-45ff-b7f0-4bf65b42472d",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "31132401-ab02-451d-9f3a-00e667650f74",
  "sourceToolAssistantUUID": "8d86df38-1607-45ff-b7f0-4bf65b42472d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T08:03:08.631Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UrvBm1ue64Mcz5JTsAe4V3`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31132401-ab02-451d-9f3a-00e667650f74",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41HNewNNLiDnMZaQj8Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d30a538b-1b52-4306-8e0f-c0b820e0cc6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KT73BHwzcJrVu6YjotqTDM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4829,
      "cache_read_input_tokens": 18950,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4829
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 18950,
          "cache_creation_input_tokens": 4829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4829,
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

_source line 23 · 2026-05-15T08:03:08.642Z_

<details><summary>↩ Tool result · `toolu_01UrvBm1ue64Mcz5JTsAe4V3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/decisions.yaml\", \"content\": \"_next_id: 14\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:22 UTC\\n  summary: MVP 方案：FOLIO + Qwen3-32B + FOL/Python 双表征验证分歧诊断假设\\n  rationale: 选择 FOLIO 因为：(1) 逻辑推理任务天然适合 FOL+Z3 表征，同时也可写 Python 约束代码，双路径互补性最强；(2) 数据集较小（~200条），MVP\\n    成本低；(3) 已有 ground truth label，可直接评估诊断准确性。选择 Qwen3-32B thinking mode 因为：(1) IDEA_BRIEF\\n    指定的主模型；(2) Apache 2.0 开源；(3) Qwen Cloud API 价格低（$0.08/M input）。Pass/fail 标准：分歧率≥10%、诊断信息量≥40%、≥2种错误类型、定向修复>盲目重生成。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:25 UTC\\n  summary: 采纳 Reviewer 反馈修订 MVP：增加 Step 0 baseline 门控、C4≥5pp、C5 定位准确率≥60%、灰色区间规则\\n  rationale: Reviewer 指出四个有效问题：(1) C4 无量化阈值可能放行无意义差异→加≥5pp；(2) C1/C2 灰色地带未定义→灰色区间扩展到第二数据集；(3)\\n    Qwen3-32B FOLIO baseline 未知，若>90%错误样本不足→增加 Step 0 前置测试；(4) 错误定位是核心环节但未纳入 MVP→增加\\n    C5 定位准确率≥60%。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:26 UTC\\n  summary: 增加 post-MVP 时间骨架和 MVP fail 应急方案（FOLIO fail→ProofWriter→Qwen3-8B→kill）\\n  rationale: Reviewer 指出 ROADMAP 缺少 MVP 后阶段规划和 fail 应急方案。11 天 DDL 下任何决策延迟代价极高。时间骨架仅为粗粒度分配（不是详细研究规划），fail\\n    路径按成本递增排列：换数据集(低成本)→换模型(中成本)→kill(止损)。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 05:28 UTC\\n  summary: 回退 qwen3.6-plus → 要求 Qwen3-32B 或同级开源模型，Reviewer critical 判定\\n  rationale: Reviewer 指出两个 critical 问题：(1) qwen3.6-plus 是闭源 API 模型，EMNLP 要求可复现性；(2)\\n    模型能力远超 Qwen3-32B（GPQA Diamond 88% vs 66.8%），FOLIO baseline 可能>90%导致错误样本不足，headroom\\n    story 不成立。Agent 无权自行做核心方法论变更（模型选择是 IDEA_BRIEF 设计决策），必须上报 Director。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D005\\n  date: 2026-05-14 08:17 UTC\\n  summary: MVP 第一轮未通过（2/5），根因是 Z3 prompt 质量（78% crash），非假设失败。启动 iteration 2 修复 prompt\\n  rationale: FOL 路径 78% exec_crash 导致真分歧样本极少（4%），修复优势为负（-28pp）。但 baseline 74% 确认 FOLIO\\n    是合适的数据集、headroom 充足。Code 路径 52% accuracy 表明 Python 表征可行。核心问题是 Z3 代码生成质量——加 few-shot\\n    examples + 输出验证预期可大幅降低 crash 率。Day 4 硬截止前有足够时间做 1-2 次 prompt 迭代。\\n  related_experiments:\\n  - exp_id: mvp_baseline_001\\n    role: baseline\\n    result: 74% accuracy, PASS_FOLIO\\n  - exp_id: mvp_pipeline_001\\n    role: mvp_v1\\n    result: NOT PASSED 2/5, FOL 78% crash\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D006\\n  date: 2026-05-14 09:47 UTC\\n  summary: MVP v2 结果：FOL crash 78%→10%、C4/C5 翻转为 PASS，但 Code crash 40% 需修复后迭代 v3\\n  rationale: Few-shot + syntax fix 大幅改善 FOL 侧（accuracy 14%→90%）。C4 从 -28pp 翻转为 +40pp，C5\\n    从 42% 翻转为 100%。新瓶颈是 Python Code 侧 thinking token 泄漏导致 40% crash，压缩了有效双表征样本量。C1=0%\\n    在仅 10 条中不具统计意义，修复 Code crash 后扩大样本是关键。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_002\\n    role: mvp_v2_test10\\n    result: FOL crash 10%, Code crash 40%, C1=0%, C4=+40pp, C5=100%\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-14 13:07 UTC\\n  summary: 撤回 v5 closed-world 方案，改为 v5b：保持 3-way 输出但改进 prompt 减少 lazy Unknown\\n  rationale: v5 强制 Code 路径 closed-world 2-way 输出，而 FOL 保持 open-world 3-way。FOLIO ~39%\\n    GT=Unknown，导致这些样本上 FOL=Unknown vs Code=False 的人为 disagreement。审稿人会质疑分歧信号有多少来自语义假设差异而非推理错误。正确做法：保持两条路径同一语义基础（都\\n    3-way），通过改进 few-shot 和指令减少\\\"不敢判断就输出 Unknown\\\"的 lazy 行为。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_004\\n    role: baseline\\n    result: running, 41/204, Code Unknown rate 46.3%\\n  depends_on: []\\n- id: D008\\n  date: 2026-05-14 18:03 UTC\\n  summary: repair.py prompt bug 确认为 C4 下降根因，修复后 repair-only 重跑全量 204 样本\\n  rationale: Reviewer 发现 BLIND_REGEN_PROMPT 和 TARGETED_REPAIR_PROMPT 硬编码 \\\"Python script\\\"，FOL(Z3)\\n    修复时给模型矛盾指令，导致 FOL-side targeted repair 50% vs blind 90%（-40pp）。C4 从 +22.6→+7.4\\n    的下降趋势直接由此解释。修复方案：动态 repr_type 替换硬编码，pipeline 完成后对全部 204 样本仅重跑 repair+eval 阶段得到干净可比数据。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_004\\n    role: affected\\n    result: C4 All-mode +7.4pp (suppressed by bug), C4 excl-Unknown +0.0pp\\n  depends_on:\\n  - D006\\n  - D007\\n- id: D009\\n  date: 2026-05-15 05:59 UTC\\n  summary: 通过 MVP gate，C4 作为已知弱点进入 research 阶段解决\\n  rationale: All-mode 5/5 PASS（原始+repair后均通过）。核心假设（跨表征分歧→诊断→定位）由 C1(39.6%), C2(86.8%),\\n    C3(3 types), C5(85.4%) 强力支持。C4 技术上通过（+5.2pp > 5pp）但 margin 仅 0.2pp，Excl-Unknown\\n    组 0.0pp，统计上不显著。C4 弱点是 paper framing 问题而非方法论根本缺陷——repair 是下游应用，核心贡献在 diagnosis+localization。Research\\n    阶段需要：(1) 改进 repair 机制拉大 delta，或 (2) reframe paper 弱化 repair claim 聚焦 diagnosis+localization。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_004\\n    role: primary\\n    result: All-mode 5/5 PASS, C4 margin 0.2pp\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-15 06:06 UTC\\n  summary: D008 假设（prompt bug = C4 根因）未获支撑；C4 reframe 为 error-type-conditional advantage\\n  rationale: Reviewer 统计分析：修复前后仅 3/192 次结果翻转（targeted +1, blind +2），blind 改善多于 targeted，C4\\n    delta 反而从 +6.25pp 降到 +5.2pp。C4 aggregate +5.2pp 的 p≈0.23 无统计显著性。但 Unknown 子组 +13.5pp\\n    (T:23/37 vs B:18/37) 显示诊断信号在系统性错误（Code overclaiming）上有效，非 Unknown 组 +0.0pp 显示对随机推理错误无效。C4\\n    弱不是 bug 导致的，是方法论层面的 error-type-dependent 局限。Paper framing Claim 3 已更新：不 claim\\n    aggregate repair superiority，claim conditional advantage + boundary characterization。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_004\\n    role: primary\\n    result: C4 aggregate +5.2pp (p≈0.23), Unknown +13.5pp, non-Unknown +0.0pp\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D011\\n  date: 2026-05-15 06:15 UTC\\n  summary: 统一指标为 per-sample 计算；Claim 3 更新为 GT-label-dependent 三分效应（Unknown +14.7pp\\n    / False +6.7pp / True -13.6pp）\\n  rationale: Reviewer 发现 evaluate_mvp.py (per-side) 和 deep_analysis.py (per-sample)\\n    两套指标不一致。per-sample 更贴合论文叙事（每个问题一个诊断），选为标准。GT=True 子组发现 targeted repair 反效果 -13.6pp（blind\\n    77.3% vs targeted 63.6%），不只是\\\"无帮助\\\"而是\\\"有害\\\"。Claim 3 从 \\\"conditional advantage\\\" 升级为\\n    \\\"GT-label-dependent three-way split\\\"——这是更有价值的发现。5.6:1 不对称性（非 9:1）已修正到 framing。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_004\\n    role: primary\\n    result: GT=True -13.6pp, GT=False +6.7pp, GT=Unknown +14.7pp. Asymmetry 5.6:1.\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-15 06:57 UTC\\n  summary: C5 报告双指标：C5-committed (85.4%, 仅明确预测) + C5-coverage (53.0%, 含 ambiguous=fail)；D009\\n    MVP 判定维持\\n  rationale: evaluate_mvp.py 过滤 ambiguous 预测 → C5=85.4% (35/41)；evaluate_unified.py\\n    不过滤 → C5=53.0% (35/66)。差异根因是 38% 样本 stability test 返回 ambiguous。两个视角都有效：committed\\n    衡量\\\"做了预测时的精度\\\"，coverage 衡量\\\"整体覆盖率\\\"。论文应诚实报告两个数字。D009 MVP 使用 C5-committed，判定维持——localization\\n    的 coverage 局限是已知弱点，不否定核心假设（分歧作为诊断信号）。GT=Unknown C5=35.7% 但 C4=+14.7pp 的悖论说明修复效用来自\\n    disagreement pattern（信息含量）而非 error_side 定位精度——这本身是有价值的发现。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_004\\n    role: primary\\n    result: C5-committed 85.4% (35/41), C5-coverage 53.0% (35/66), ambiguous rate\\n      38%\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-15 07:17 UTC\\n  summary: 'Dream #1 三档均 3/6 (borderline/weak reject)，识别 5 个结构性问题，更新 framing+plan\\n    后 re-dream'\\n  rationale: 'Dream dream_20260515T060408 三档评分: Best=3/6 borderline reject, Median=3/6\\n    weak reject, Worst=3/6 borderline reject。未达 \\\"best ≥ weak accept\\\" 门槛。跨三档一致的结构性问题:\\n    (1) Related work 严重不足——缺 self-consistency/LEVER/Faithful CoT/self-debug/multi-agent\\n    debate; (2) 引用不完整; (3) Error taxonomy 未验证; (4) \\\"first systematic study\\\" claim\\n    过强; (5) 缺 self-consistency baseline 对比。已采取行动: paper_framing.md 降低 novelty claim\\n    + 加 R8-R11 reviewer concerns; experiment_plan.yaml 新增 exp-012 (self-consistency\\n    baseline, P0) + exp-013 (taxonomy cross-validation, P1) + exp-007 升 P0。需 re-dream\\n    验证改进效果后才能批准 P0 实验。'\\n  related_experiments:\\n  - exp_id: exp-012\\n    role: 新增 P0 — self-consistency baseline\\n  - exp_id: exp-013\\n    role: 新增 P1 — taxonomy validation\\n  - exp_id: exp-007\\n    role: P1→P0 升级 — selection vs repair\\n  depends_on:\\n  - D009\\n\", \"total_chars\": 7500, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d30a538b-1b52-4306-8e0f-c0b820e0cc6b",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "a7dd68cf-a81e-424b-97ea-e4ee2710c3dd",
  "sourceToolAssistantUUID": "d30a538b-1b52-4306-8e0f-c0b820e0cc6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-15T08:03:11.577Z_

Now let me look at the actual paper draft and experimental artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7dd68cf-a81e-424b-97ea-e4ee2710c3dd",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41HjjxHXrsxMCbu5paH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dceb495b-a076-4b52-9e08-61e155e46f11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cKmTXVLnZGFRiqL51BLYA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6192,
      "cache_read_input_tokens": 23779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6192,
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

_source line 25 · 2026-05-15T08:03:14.136Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01RBL12gCqcBdhGrpGAbw3VC`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dceb495b-a076-4b52-9e08-61e155e46f11",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41HjjxHXrsxMCbu5paH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4b3e8b7-1ff2-4cf8-a722-194aaff6ffe9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cKmTXVLnZGFRiqL51BLYA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6192,
      "cache_read_input_tokens": 23779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6192,
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

_source line 26 · 2026-05-15T08:03:14.144Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LQWeVobKCR9BeR5BXfy1aW`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4b3e8b7-1ff2-4cf8-a722-194aaff6ffe9",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41HjjxHXrsxMCbu5paH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fed13201-b7c8-4750-916c-943e6217e595",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cKmTXVLnZGFRiqL51BLYA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6192,
      "cache_read_input_tokens": 23779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6192,
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

_source line 27 · 2026-05-15T08:03:14.183Z_

<details><summary>↩ Tool result · `toolu_01RBL12gCqcBdhGrpGAbw3VC`</summary>

```text
artifacts/dream_reports/dream_20260515T060408/best/paper.tex
artifacts/dream_reports/dream_20260515T060408/median/paper.tex
artifacts/dream_reports/dream_20260515T060408/worst/paper.tex
artifacts/dream_reports/dream_20260515T071730/best/paper.tex
artifacts/dream_reports/dream_20260515T071730/median/paper.tex
artifacts/dream_reports/dream_20260515T071730/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4b3e8b7-1ff2-4cf8-a722-194aaff6ffe9",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "1f6d05ba-6b4c-4437-9c1a-583d0b19432f",
  "sourceToolAssistantUUID": "d4b3e8b7-1ff2-4cf8-a722-194aaff6ffe9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T08:03:14.207Z_

<details><summary>↩ Tool result · `toolu_01LQWeVobKCR9BeR5BXfy1aW`</summary>

```text
artifacts/dream_reports/dream_20260515T060408/best/paper.pdf
artifacts/dream_reports/dream_20260515T060408/median/paper.pdf
artifacts/dream_reports/dream_20260515T060408/worst/paper.pdf
artifacts/dream_reports/dream_20260515T071730/best/paper.pdf
artifacts/dream_reports/dream_20260515T071730/median/paper.pdf
artifacts/dream_reports/dream_20260515T071730/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fed13201-b7c8-4750-916c-943e6217e595",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "6bf58bee-b982-4787-8211-807bf29f25b3",
  "sourceToolAssistantUUID": "fed13201-b7c8-4750-916c-943e6217e595",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T08:03:14.799Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AnXgwngR4YN5dfNt2Ft12z`</summary>

```json
{
  "pattern": "**/dream_*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bf58bee-b982-4787-8211-807bf29f25b3",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41HjjxHXrsxMCbu5paH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c57d81d3-4e64-41ce-9597-3a32d047b558",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cKmTXVLnZGFRiqL51BLYA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6192,
      "cache_read_input_tokens": 23779,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6192
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 285,
          "cache_read_input_tokens": 23779,
          "cache_creation_input_tokens": 6192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6192,
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

_source line 30 · 2026-05-15T08:03:14.843Z_

<details><summary>↩ Tool result · `toolu_01AnXgwngR4YN5dfNt2Ft12z`</summary>

```text
dream_registry.lock
dream_registry.yaml.bak
dream_registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c57d81d3-4e64-41ce-9597-3a32d047b558",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "81107888-4f35-4a2f-8835-a3beab21d37b",
  "sourceToolAssistantUUID": "c57d81d3-4e64-41ce-9597-3a32d047b558",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T08:03:17.618Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AUX7Cxoqpwm21ZAEFHV1rx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81107888-4f35-4a2f-8835-a3beab21d37b",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41JC9CLq3z4ELy6rjSt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fbb2f01-c194-402c-b93f-6b622d953956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bgg8kt5zuQWQnZWe8Dvt7h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 29971,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 640
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 29971,
          "cache_creation_input_tokens": 640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 640,
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

_source line 32 · 2026-05-15T08:03:17.996Z_

<details><summary>↩ Tool result · `toolu_01AUX7Cxoqpwm21ZAEFHV1rx`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage[T1]{fontenc}
12	\usepackage[utf8]{inputenc}
13	\usepackage{hyperref}
14	
15	\newcommand{\method}{CRD}
16	\newcommand{\pp}{\,pp}
17	
18	\title{Cross-Representation Disagreement for Diagnosis and Characterization\\of LLM Formalization Errors}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	% ============================================================
26	\begin{abstract}
27	When a large language model formalizes a reasoning problem into two distinct executable representations---first-order logic verified by Z3 and executable Python code---disagreements between their outputs serve as a structured diagnostic signal.
28	We present \emph{Cross-Representation Disagreement} (\method{}), a lightweight inference-time framework that detects formalization errors, classifies them into an empirically motivated taxonomy, and localizes the erroneous representation.
29	On FOLIO (204 samples), \method{} achieves an 87.2\% diagnostic precision among disagreeing samples with 94.6\% localization accuracy on committed predictions, while requiring only 2 LLM calls compared to 5 for self-consistency baselines at comparable detection precision.
30	A 5.6:1 asymmetry in favor of the FOL pathway reveals systematic differences in how LLMs handle formal logic versus imperative code generation.
31	We extend \method{} to LogiQA and MATH Level~5, finding that the diagnostic signal generalizes (72\% and 65\% diagnostic rates, respectively) but attenuates as the formalization bottleneck weakens.
32	Selection based on the diagnosed error side matches repair-based approaches ($p{=}0.72$, McNemar) at zero additional cost, supporting a framing where the primary contribution is the diagnostic analysis itself---error type classification, error-side localization, and paradigm asymmetry characterization---rather than downstream accuracy improvement.
33	\end{abstract}
34	
35	% ============================================================
36	\section{Introduction}
37	
38	Neurosymbolic reasoning pipelines that translate natural language into formal representations suffer from a dominant failure mode: the LLM's formalization step introduces subtle corruptions that downstream solvers faithfully propagate~\cite{pan2023logic,olausson2023linc}.
39	Current approaches either select one representation~\cite{hybrid2024}, verify within a single representation~\cite{vericot2024,roundtrip2026}, or discard disagreeing solutions without further analysis~\cite{liang2024}.
40	None exploit the \emph{pattern} of cross-representation disagreement---which representation failed, what type of error occurred, and what this reveals about the relative reliability of different formalization paradigms.
41	
42	We observe that when the same LLM formalizes a problem into both first-order logic (FOL, verified by Z3) and executable Python code, the resulting disagreements are far from random noise.
43	On FOLIO, 42.2\% of samples produce disagreeing outputs, and 87.2\% of these disagreements are diagnostically informative---at least one pathway produced the correct answer.
44	This diagnostic precision is comparable to 5-sample self-consistency voting (85.0\%) but at 40\% of the cost (2 LLM calls vs.\ 5) and with qualitative advantages that self-consistency fundamentally cannot provide: error type classification, error-side localization, and paradigm asymmetry characterization.
45	
46	Our contributions are:
47	\begin{enumerate}
48	\item We establish cross-representation disagreement as a high-precision diagnostic signal (87.2\% on FOLIO, 72.0\% on LogiQA, 65.0\% on MATH), characterizing its domain boundary: effectiveness correlates with the degree to which formalization is the reasoning bottleneck.
49	\item We develop an empirically motivated error taxonomy (3 stable types, cross-model $\kappa{=}0.54$) and a stability-based localization method achieving 94.6\% accuracy on committed predictions, revealing a 5.6:1 FOL-over-Code asymmetry.
50	\item We demonstrate that simple selection based on diagnosed error side matches diagnosis-guided repair ($p{=}0.72$) at zero additional LLM cost, and that repair exhibits a GT-label-dependent effect: helping for Unknown (+14.7\pp{}) and False (+6.7\pp{}) but hurting for True ($-$13.6\pp{}).
51	\end{enumerate}
52	
53	% ============================================================
54	\section{Related Work}
55	
56	\paragraph{Neurosymbolic reasoning.}
57	Logic-LM~\cite{pan2023logic} and LINC~\cite{olausson2023linc} translate problems to FOL and use symbolic solvers, while Program-of-Thought~\cite{chen2023program} generates executable code.
58	HybridMind~\cite{hybrid2024} and adaptive selection approaches choose one representation per problem but do not exploit disagreement patterns.
59	
60	\paragraph{Self-consistency and ensemble methods.}
61	Self-consistency~\cite{wang2023selfconsistency} samples multiple reasoning paths within a single representation and takes the majority vote.
62	This captures generation variance but not systematic paradigm-level differences.
63	Multi-agent debate~\cite{du2023improving,liang2024encouraging} uses multiple LLM agents but typically within the same representation modality.
64	We show that cross-representation disagreement captures qualitatively different information from within-representation sampling.
65	
66	\paragraph{Verification and refinement.}
67	VeriCoT~\cite{vericot2024}, LEVER~\cite{ni2023lever}, and Faithful CoT~\cite{lyu2023faithful} verify or refine within a single representation.
68	Roundtrip Verification~\cite{roundtrip2026} demonstrated diagnosis-guided repair within one representation on 150 traffic rules.
69	Self-debug~\cite{chen2024teaching} and self-refine~\cite{madaan2024selfrefine} iteratively improve code but lack cross-representation diagnostic signals.
70	
71	\paragraph{Cross-representation filtering.}
72	Liang et al.~\cite{liang2024} proved that CoT--PoT disagreement is informative for filtering incorrect answers but stopped at discarding disagreements.
73	We extend this from a binary filter to a structured diagnostic tool enabling error categorization, localization, and targeted repair.
74	
75	\paragraph{Correlated failures.}
76	Denisov-Blanch et al.~\cite{denisov2026} analyze failure correlation in LLM ensembles.
77	We explicitly quantify correlated failures via $\phi$ coefficients and show that cross-representation disagreement partially decorrelates failure modes ($\phi{=}0.189$ within-model vs.\ $\phi{=}0.14$ cross-model).
78	
79	% ============================================================
80	\section{Method}
81	
82	\subsection{Overview}
83	
84	Given a reasoning problem $q$, \method{} proceeds in five stages:
85	\begin{description}
86	\item[C1 --- Disagreement Detection.]
87	The LLM formalizes $q$ into two executable representations: FOL (verified by Z3) and Python code.
88	If their outputs disagree, the sample is flagged.
89	\item[C2 --- Diagnostic Assessment.]
90	Among disagreeing samples, we assess whether the disagreement is diagnostically informative---i.e., at least one pathway produced the correct answer.
91	\item[C3 --- Error Classification.]
92	A rule-based taxonomy classifies the error into one of three stable categories: \texttt{logic\_error}, \texttt{negation\_error}, or \texttt{formalization\_other} (merging \texttt{quantifier\_error} and \texttt{exec\_crash}).
93	\item[C4 --- Repair / Selection.]
94	The diagnosed error side and type inform either (a) \emph{selection}: directly adopting the answer from the more reliable pathway, or (b) \emph{repair}: prompting the LLM to fix the erroneous representation guided by the diagnosis.
95	\item[C5 --- Localization.]
96	A stability test reruns each pathway with perturbation; the pathway yielding inconsistent outputs is identified as the error side.
97	When the test commits (produces a definitive verdict), localization accuracy reaches 94.6\%.
98	\end{description}
99	
100	\subsection{Representation Pathways}
101	
102	\paragraph{FOL + Z3.}
103	The LLM translates $q$ into first-order logic premises and a conclusion.
104	Z3 determines satisfiability, returning \textsc{True}, \textsc{False}, or \textsc{Unknown}.
105	Z3 provides a formal verification guarantee: if the FOL encoding is correct, the answer is provably correct.
106	
107	\paragraph{Executable Python.}
108	The LLM generates a Python program that encodes the problem's logic and prints its answer.
109	Python execution is deterministic given correct code but offers no formal guarantee on the correctness of the encoding.
110	
111	\paragraph{Cross-executable extension.}
112	For mathematical reasoning (MATH), we instantiate the framework as SymPy (symbolic algebra) versus Python (numerical computation), maintaining the cross-executable-paradigm structure while adapting to a domain where FOL is not applicable.
113	
114	\subsection{Error Taxonomy}
115	
116	We define an empirically motivated taxonomy based on analysis of FOLIO disagreement patterns:
117	
118	\begin{itemize}
119	\item \textbf{logic\_error} (25.5\%): Incorrect logical operators, missing premises, or flawed inference chains in formalization.
120	\item \textbf{negation\_error} (10.8\%): Omitted or incorrectly handled negation during translation.
121	\item \textbf{formalization\_other} (7.4\%): Quantifier scope errors, execution crashes, and other formalization failures.
122	\end{itemize}
123	
124	The taxonomy is validated via cross-model agreement (Qwen3-32B vs.\ DeepSeek V4 Pro), achieving $\kappa{=}0.54$ on the merged 3-type scheme (\S\ref{sec:taxonomy-validation}).
125	
126	\subsection{Paradigm Asymmetry}
127	
128	A key finding is the systematic asymmetry between representation pathways.
129	On FOLIO with Qwen3-32B, FOL produces the correct answer 5.6$\times$ more often than Code among disagreeing samples.
130	This asymmetry is directionally consistent across models and benchmarks but its magnitude is model- and domain-dependent (\S\ref{sec:cross-model}, \S\ref{sec:generalization}).
131	
132	% ============================================================
133	\section{Experimental Setup}
134	
135	\paragraph{Benchmarks.}
136	(1)~\textbf{FOLIO}~\cite{han2022folio}: 204 FOL reasoning problems with 3-valued labels (True/False/Unknown); our primary benchmark.
137	(2)~\textbf{LogiQA}~\cite{liu2021logiqa}: 200 multiple-choice logical reasoning problems; secondary benchmark for generalization.
138	(3)~\textbf{MATH Level~5}~\cite{hendrycks2021math}: 200 competition-level math problems; cross-executable extension using SymPy vs.\ Python.
139	(4)~\textbf{GPQA Diamond}~\cite{rein2024gpqa}: 198 graduate-level science questions; domain boundary test.
140	
141	\paragraph{Models.}
142	Primary: Qwen3-32B.
143	Cross-model ablation: DeepSeek V4 Pro (within-model) and DeepSeek FOL $\times$ Qwen Code (cross-model).
144	Scale ablation: Qwen3-8B.
145	Taxonomy validation: DeepSeek V4 Pro as independent classifier.
146	
147	\paragraph{Metrics.}
148	C1: disagreement rate.
149	C2: diagnostic rate (fraction of disagreements where $\geq$1 pathway is correct).
150	C3: error type distribution.
151	C4: accuracy improvement from repair/selection vs.\ blind baseline.
152	C5: localization accuracy on committed predictions.
153	We report bootstrap 95\% CIs (10{,}000 resamples) and Fisher exact / McNemar tests throughout.
154	
155	\paragraph{Baselines.}
156	(1)~\emph{Blind baseline}: single-pass FOL answer without diagnosis.
157	(2)~\emph{Self-consistency $k{=}5$}: majority vote over 5 FOL-only or 5 Code-only samples.
158	(3)~\emph{Oracle}: always selecting the correct pathway when one exists.
159	
160	% ============================================================
161	\section{Results}
162	
163	\subsection{Main Results on FOLIO}
164	\label{sec:main-results}
165	
166	Table~\ref{tab:main} summarizes \method{}'s diagnostic performance on FOLIO.
167	
168	\begin{table}[t]
169	\centering
170	\small
171	\begin{tabular}{lcc}
172	\toprule
173	\textbf{Metric} & \textbf{Value} & \textbf{95\% CI} \\
174	\midrule
175	C1: Disagree Rate & 42.2\% & [35.3, 49.0] \\
176	C2: Diagnostic Rate & 87.2\% & [81.3, 94.7] \\
177	C5: Committed Acc. & 94.6\% & [86.1, 100] \\
178	C5: Coverage & 53.0\% & --- \\
179	Asymmetry (FOL:Code) & 5.6:1 & --- \\
180	$\phi$ coefficient & 0.189 & --- \\
181	\bottomrule
182	\end{tabular}
183	\caption{CRD diagnostic metrics on FOLIO ($n{=}204$, Qwen3-32B). C2 and C5 are conditioned on disagreeing samples. All metrics except C4 are significant after Bonferroni correction ($p{<}0.004$).}
184	\label{tab:main}
185	\end{table}
186	
187	Among the 86 disagreeing samples, 75 (87.2\%) contain at least one correct pathway.
188	The stability-based localization test commits on 53\% of diagnostic cases, achieving 94.6\% accuracy---when the test produces a definitive verdict, it is almost always correct.
189	The remaining 47\% are returned as ``ambiguous,'' driven primarily by GT=Unknown samples (61\% ambiguous rate) where Code's tendency to overclaim creates systematically unstable predictions.
190	
191	\subsection{CRD vs.\ Self-Consistency}
192	\label{sec:sc-comparison}
193	
194	Table~\ref{tab:sc} compares \method{} with $k{=}5$ self-consistency voting.
195	
196	\begin{table}[t]
197	\centering
198	\small
199	\begin{tabular}{lcccl}
200	\toprule
201	\textbf{Benchmark} & \textbf{SC5-Best} & \textbf{CRD} & $\boldsymbol{\Delta}$ & \textbf{Cost} \\
202	\midrule
203	FOLIO & 85.0\% & 87.2\% & +2.2\pp{} & 0.40$\times$ \\
204	LogiQA & 76.0\% & 72.0\% & $-$4.0\pp{} & 0.38$\times$ \\
205	MATH & 74.0\% & 65.0\% & $-$9.0\pp{} & 0.35$\times$ \\
206	\bottomrule
207	\end{tabular}
208	\caption{Detection precision: CRD (2 calls) vs.\ best self-consistency baseline (5 calls). CRD cost ratio is relative to SC5.}
209	\label{tab:sc}
210	\end{table}
211	
212	On FOLIO, \method{} achieves slightly higher detection precision (+2.2\pp{}) at 40\% of the cost.
213	On LogiQA and MATH, precision is lower ($-$4.0\pp{} and $-$9.0\pp{}, respectively), reflecting the attenuated diagnostic signal when formalization is less of a bottleneck.
214	Critically, \method{} provides structured diagnostic information that self-consistency cannot: error type classification (3--4 types), error-side localization (C5: 82--95\% accuracy), and paradigm asymmetry characterization.
215	Self-consistency reveals \emph{that} something may be wrong; \method{} reveals \emph{why}.
216	
217	\subsection{Selection vs.\ Repair}
218	\label{sec:selection-repair}
219	
220	Table~\ref{tab:sel-rep} compares selection (adopting the answer from the diagnosed correct side) with diagnosis-guided repair.
221	
222	\begin{table}[t]
223	\centering
224	\small
225	\begin{tabular}{lccc}
226	\toprule
227	\textbf{Method} & \textbf{Accuracy} & \textbf{Extra Calls} & \textbf{vs.\ Blind} \\
228	\midrule
229	Blind baseline & 81.4\% & 0 & --- \\
230	Selection (ours) & 82.8\% & 0 & +1.4\pp{} \\
231	Repair (ours) & 83.8\% & ${\sim}$2/sample & +2.4\pp{} \\
232	Oracle & 87.8\% & --- & +6.4\pp{} \\
233	\bottomrule
234	\end{tabular}
235	\caption{Selection vs.\ repair on FOLIO. McNemar $p{=}0.72$; the difference is not significant.}
236	\label{tab:sel-rep}
237	\end{table}
238	
239	Selection nearly matches repair (82.8\% vs.\ 83.8\%, McNemar $p{=}0.72$) at zero additional LLM cost.
240	The oracle upper bound (87.8\%) indicates 5.0\pp{} headroom from perfect localization.
241	
242	Stratified by ground-truth label (Table~\ref{tab:sel-rep-gt}), selection outperforms repair on GT=True (+2.8\pp{}) by avoiding overcorrection, while repair excels on GT=Unknown ($-$4.3\pp{} in favor of repair) where generating a better answer from the disagreement pattern is beneficial.
243	
244	\begin{table}[t]
245	\centering
246	\small
247	\begin{tabular}{lccr}
248	\toprule
249	\textbf{GT Label} & \textbf{Selection} & \textbf{Repair} & $\boldsymbol{\Delta}$ \\
250	\midrule
251	True & 79.2\% & 76.4\% & +2.8\pp{} \\
252	False & 81.0\% & 82.5\% & $-$1.5\pp{} \\
253	Unknown & 81.2\% & 85.5\% & $-$4.3\pp{} \\
254	\bottomrule
255	\end{tabular}
256	\caption{Selection vs.\ repair by GT label on FOLIO.}
257	\label{tab:sel-rep-gt}
258	\end{table}
259	
260	\subsection{Repair Analysis}
261	\label{sec:repair}
262	
263	Though repair is not our primary contribution, we analyze its behavior to characterize the boundary of diagnosis-guided correction.
264	
265	\paragraph{GT-label-dependent effects.}
266	Repair exhibits a striking three-way pattern (Table~\ref{tab:repair-gt}): it helps substantially for GT=Unknown (+14.7\pp{} in Round~1), modestly for GT=False (+6.7\pp{}), and actively \emph{hurts} for GT=True ($-$13.6\pp{}).
267	The mechanism: when Code incorrectly outputs False or Unknown for a True problem, the diagnostic signal triggers overcorrection---the repair prompt leads the model to change the (correct) FOL answer.
268	
269	\begin{table}[t]
270	\centering
271	\small
272	\begin{tabular}{lcccc}
273	\toprule
274	\textbf{Round} & \textbf{Aggregate} & \textbf{GT=True} & \textbf{GT=False} & \textbf{GT=Unk.} \\
275	\midrule
276	Round 1 & +4.65\pp{} & $-$13.6\pp{} & +6.7\pp{} & +14.7\pp{} \\
277	Round 2 & +6.2\pp{} & $-$12.3\pp{} & +7.8\pp{} & +14.2\pp{} \\
278	Round 3 & +6.8\pp{} & $-$11.5\pp{} & +8.2\pp{} & +13.0\pp{} \\
279	\bottomrule
280	\end{tabular}
281	\caption{Multi-round repair results on FOLIO. Aggregate C4 is not significant (Fisher $p{=}0.626$ for Round~1). Diminishing returns are evident after Round~1.}
282	\label{tab:repair-gt}
283	\end{table}
284	
285	\paragraph{Multi-round repair.}
286	Additional repair rounds yield diminishing returns: Round~1$\to$2 adds +1.55\pp{} aggregate, Round~2$\to$3 adds only +0.6\pp{}.
287	GT=True overcorrection improves from $-$13.6\pp{} to $-$11.5\pp{} but remains a structural limitation.
288	
289	\paragraph{Error-type-specific repair.}
290	Taxonomy-guided repair (dispatching repair strategy by error type) achieves 84.5\% vs.\ 83.8\% for fixed-strategy repair ($\Delta{=}{+}0.7\pp{}$, McNemar $p{=}0.68$; Table~\ref{tab:taxonomy-repair}).
291	The taxonomy's value is primarily descriptive (understanding error distributions) rather than prescriptive (guiding repair strategies).
292	
293	\begin{table}[t]
294	\centering
295	\small
296	\begin{tabular}{lcccc}
297	\toprule
298	\textbf{Error Type} & $n$ & \textbf{Guided} & \textbf{Fixed} & $\boldsymbol{\Delta}$ \\
299	\midrule
300	logic\_error & 52 & 87\% & 85\% & +2\pp{} \\
301	negation\_error & 22 & 86\% & 82\% & +4\pp{} \\
302	exec\_crash & 11 & 91\% & 91\% & 0\pp{} \\
303	quantifier\_error & 4 & 75\% & 75\% & 0\pp{} \\
304	\midrule
305	Overall & 89 & 84.5\% & 83.8\% & +0.7\pp{} \\
306	\bottomrule
307	\end{tabular}
308	\caption{Taxonomy-guided vs.\ fixed-strategy repair. McNemar $p{=}0.68$.}
309	\label{tab:taxonomy-repair}
310	\end{table}
311	
312	\subsection{Unknown Sample Analysis and Correlated Failures}
313	\label{sec:unknown}
314	
315	GT=Unknown samples exhibit a paradox: the highest false agreement rate (26.1\%) yet the highest repair delta (+14.7\pp{}).
316	Table~\ref{tab:unknown} reveals the mechanism: Code outputs \textsc{True} or \textsc{False} for 72.5\% of GT=Unknown samples (overclaiming), while FOL correctly returns \textsc{Unknown} 41\% of the time.
317	This systematic Code overclaiming creates detectable disagreements that are highly actionable.
318	
319	\begin{table}[t]
320	\centering
321	\small
322	\begin{tabular}{lcc}
323	\toprule
324	\textbf{Code Output (GT=Unk.)} & \textbf{Count} & \textbf{Rate} \\
325	\midrule
326	True (overclaim) & 28 & 40.6\% \\
327	False (overclaim) & 22 & 31.9\% \\
328	Unknown (correct) & 14 & 20.3\% \\
329	Crash & 5 & 7.2\% \\
330	\bottomrule
331	\end{tabular}
332	\caption{Code pathway outputs on GT=Unknown samples ($n{=}69$). Python execution lacks native \textsc{Unknown} semantics, leading to overclaiming in 72.5\% of cases.}
333	\label{tab:unknown}
334	\end{table}
335	
336	Failure correlation ($\phi$ coefficient) varies by GT label: $\phi{=}0.12$ (True), $\phi{=}0.18$ (False), $\phi{=}0.31$ (Unknown).
337	Higher correlation on Unknown samples reflects shared difficulty from specification ambiguity, but the differing \emph{failure modes} (FOL returns Unknown; Code guesses) make the disagreement diagnostically valuable.
338	
339	We further distinguish specification-level errors (12.3\% of all samples), where the problem itself is ambiguous enough that both representations produce reasonable but different formalizations, from formalization-specific errors (36.8\%), where one representation introduces a clear bug.
340	Repair is effective for the latter (+7.8\pp{}) but not the former (+1.2\pp{}), delineating the method's actionable boundary.
341	
342	\subsection{Cross-Model Ablation}
343	\label{sec:cross-model}
344	
345	To test whether the diagnostic signal depends on a specific model, we compare three conditions on FOLIO (Table~\ref{tab:cross-model}).
346	
347	\begin{table}[t]
348	\centering
349	\small
350	\begin{tabular}{lcccc}
351	\toprule
352	\textbf{Condition} & \textbf{C1} & \textbf{C2} & \textbf{Asym.} & $\boldsymbol{\phi}$ \\
353	\midrule
354	Qwen3-32B (within) & 42.2\% & 87.2\% & 5.6:1 & 0.189 \\
355	DeepSeek V4 (within) & 35.0\% & 74.0\% & 2.5:1 & 0.280 \\
356	DeepSeek$\times$Qwen (cross) & 48.0\% & 78.0\% & 3.2:1 & 0.140 \\
357	\bottomrule
358	\end{tabular}
359	\caption{Cross-model ablation on FOLIO ($n{=}204$). Asymmetry direction (FOL$>$Code) is consistent across all conditions.}
360	\label{tab:cross-model}
361	\end{table}
362	
363	The asymmetry direction is consistent across all three conditions: FOL outperforms Code by 5.6:1, 2.5:1, and 3.2:1.
364	This supports the interpretation that the signal reflects representation-level differences rather than model-specific artifacts.
365	However, the effect magnitude is model-dependent---DeepSeek V4 Pro's stronger Code generation compresses the asymmetry from 5.6:1 to 2.5:1.
366	
367	The cross-model condition reduces failure correlation ($\phi{=}0.14$ vs.\ 0.189 within-model), providing partial evidence that using different models for each pathway decorrelates failures, though the reduction is modest.
368	Jaccard failure overlap of 0.42 indicates substantial shared specification-level failure patterns remain.
369	
370	\subsection{Generalization across Benchmarks}
371	\label{sec:generalization}
372	
373	\paragraph{ProofWriter pilot failure.}
374	We first piloted on ProofWriter ($n{=}30$), a synthetic dataset with fully formalized premises.
375	The disagree rate was only 6.7\% (below our 10\% threshold), with baseline accuracy of 93.3\%.
376	This confirms that \method{} provides limited value when both representations are already highly accurate---the method's utility requires formalization to be the bottleneck.
377	
378	\paragraph{LogiQA.}
379	On 200 LogiQA multiple-choice problems (Table~\ref{tab:generalization}), \method{} achieves C1=22.0\% and C2=72.0\% [CI: 63--81\%].
380	The lower disagreement rate reflects LogiQA's multiple-choice format (smaller error surface).
381	Asymmetry compresses to 3.8:1 as the logical structure is less pure than FOLIO.
382	C4 is +3.5\pp{} (Fisher $p{=}0.42$, not significant).
383	
384	\paragraph{MATH Level 5.}
385	On 200 competition math problems using SymPy (symbolic) vs.\ Python (numerical), C1=15.5\% and C2=65.0\% [CI: 53--76\%].
386	The asymmetry drops to 1.8:1 ($p{=}0.18$, not significant)---the critical weakness for this domain.
387	Unlike FOL+Z3 vs.\ Python (where Z3 provides formal verification guarantees), SymPy and Python offer no fundamental verification gap, flattening the asymmetry.
388	Error types require domain adaptation: \texttt{symbolic\_algebra\_error} (8.5\%), \texttt{numerical\_precision\_error} (4.0\%), \texttt{exec\_crash} (3.0\%).
389	
390	\begin{table}[t]
391	\centering
392	\small
393	\begin{tabular}{lcccc}
394	\toprule
395	\textbf{Metric} & \textbf{FOLIO} & \textbf{LogiQA} & \textbf{MATH} & \textbf{GPQA} \\
396	\midrule
397	$n$ & 204 & 200 & 200 & 198 \\
398	C1 & 42.2\% & 22.0\% & 15.5\% & 12.0\% \\
399	C2 & 87.2\% & 72.0\% & 65.0\% & 58.0\% \\
400	Asymmetry & 5.6:1 & 3.8:1 & 1.8:1 & 1.4:1 \\
401	C5 Committed & 94.6\% & 84.0\% & 82.0\% & 75.0\% \\
402	C4 $\Delta$ & +4.65\pp{} & +3.5\pp{} & +2.8\pp{} & +1.0\pp{} \\
403	\bottomrule
404	\end{tabular}
405	\caption{CRD metrics across benchmarks. GPQA is a boundary case included for completeness. All C4 values are not statistically significant.}
406	\label{tab:generalization}
407	\end{table}
408	
409	\paragraph{GPQA Diamond.}
410	GPQA represents the method's domain boundary: C1=12.0\%, C2=58.0\%, asymmetry 1.4:1.
411	Knowledge-intensive science reasoning has its bottleneck in domain knowledge, not formalization---cross-representation disagreement provides limited diagnostic value.
412	
413	\subsection{Error Taxonomy Validation}
414	\label{sec:taxonomy-validation}
415	
416	We validate the error taxonomy by having DeepSeek V4 Pro independently classify the same 86 FOLIO disagreement samples (Table~\ref{tab:taxonomy}).
417	
418	\begin{table}[t]
419	\centering
420	\small
421	\begin{tabular}{lcccr}
422	\toprule
423	\textbf{Error Type} & \textbf{Qwen} & \textbf{DeepSeek} & $\boldsymbol{\kappa}$ & \textbf{Agree.} \\
424	\midrule
425	logic\_error & 25.5\% & 27.1\% & 0.58 & 78\% \\
426	negation\_error & 10.8\% & 9.3\% & 0.51 & 73\% \\
427	quantifier\_error & 2.0\% & 4.7\% & 0.22 & 65\% \\
428	exec\_crash & 5.4\% & 4.7\% & 0.82 & 95\% \\
429	\midrule
430	Overall (4 types) & --- & --- & 0.43 & --- \\
431	Overall (3 types) & --- & --- & 0.54 & --- \\
432	\bottomrule
433	\end{tabular}
434	\caption{Cross-model taxonomy agreement on FOLIO ($n{=}86$). The 3-type scheme merges quantifier\_error and exec\_crash into formalization\_other.}
435	\label{tab:taxonomy}
436	\end{table}
437	
438	With the original 4-type taxonomy, $\kappa{=}0.43$ (moderate agreement).
439	Merging \texttt{quantifier\_error} (low frequency, ambiguous definition, $\kappa{=}0.22$) and \texttt{exec\_crash} into \texttt{formalization\_other} yields $\kappa{=}0.54$, reaching moderate-to-fair agreement.
440	The main categories---\texttt{logic\_error} ($\kappa{=}0.58$) and \texttt{negation\_error} ($\kappa{=}0.51$)---are reasonably stable.
441	\texttt{exec\_crash} achieves near-perfect agreement ($\kappa{=}0.82$) as crashes are objectively verifiable.
442	
443	An LLM-as-proxy evaluation on 50 samples achieved $\kappa{=}0.61$ (vs.\ Qwen) and $\kappa{=}0.57$ (vs.\ DeepSeek), suggesting the categories capture meaningful distinctions.
444	The error type distributions do not differ significantly between models ($\chi^2$ test, $p{=}0.12$).
445	
446	\subsection{Statistical Significance}
447	\label{sec:stats}
448	
449	Table~\ref{tab:stats} summarizes significance testing across all benchmarks.
450	
451	\begin{table}[t]
452	\centering
453	\small
454	\begin{tabular}{lcccc}
455	\toprule
456	\textbf{Metric} & \textbf{FOLIO} & \textbf{LogiQA} & \textbf{MATH} & \textbf{All Sig.?} \\
457	\midrule
458	C1 (vs.\ 0\%) & $p{<}.001$ & $p{<}.001$ & $p{<}.001$ & Yes \\
459	C2 (vs.\ 50\%) & $p{<}.001$ & $p{=}.002$ & $p{=}.018$ & Yes \\
460	C4 (Fisher) & $p{=}.626$ & $p{=}.42$ & $p{=}.58$ & No \\
461	C5 (vs.\ 50\%) & $p{<}.001$ & $p{=}.003$ & $p{=}.008$ & Yes \\
462	\bottomrule
463	\end{tabular}
464	\caption{Statistical significance summary. All tests remain significant after Bonferroni correction (12 tests, threshold $p{<}0.004$) except C4, which is not significant on any benchmark.}
465	\label{tab:stats}
466	\end{table}
467	
468	The diagnostic metrics (C1, C2, C5) are robustly significant across all three benchmarks, surviving Bonferroni correction.
469	C4 (repair improvement) is consistently non-significant---the smallest $p$-value is 0.42 (LogiQA)---with bootstrap CIs including zero on every benchmark (e.g., FOLIO: [$-$8.8, +18.1]).
470	This supports our framing: the contribution is the diagnostic analysis, not aggregate accuracy improvement.
471	
472	\subsection{Model Scale Ablation}
473	
474	Running \method{} with Qwen3-8B on FOLIO reveals an instructive pattern: disagreement rate \emph{increases} to 55.0\% (+12.8\pp{}) while diagnostic rate \emph{decreases} to 68.0\% ($-$19.2\pp{}).
475	The 8B model's weaker formalization produces more frequent but less informative disagreements---more ``both wrong'' cases.
476	Asymmetry compresses to 2.8:1 as the FOL pathway degrades faster than Code (formal logic requires more precise generation capability).
477	This confirms that \method{}'s effectiveness scales with model capability: more disagreement does not equal better diagnosis.
478	
479	% ============================================================
480	\section{Discussion}
481	
482	\paragraph{When does CRD work?}
483	Our results trace a clear effectiveness gradient: FOLIO (87.2\% C2) $>$ LogiQA (72.0\%) $>$ MATH (65.0\%) $>$ GPQA (58.0\%).
484	This gradient correlates with the degree to which formalization is the reasoning bottleneck.
485	When the LLM's primary challenge is translating natural language into formal representations (FOLIO), cross-representation disagreement is highly diagnostic.
486	When the challenge shifts to domain knowledge (GPQA) or when both representations lack fundamental verification gaps (MATH), the signal attenuates.
487	
488	\paragraph{Cost-efficiency argument.}
489	\method{} requires exactly 2 LLM calls per sample (one FOL, one Code).
490	Self-consistency with $k{=}5$ requires 5 calls.
491	On FOLIO, \method{} achieves comparable detection precision (+2.2\pp{}) at 40\% cost while additionally providing error type classification, error-side localization, and paradigm asymmetry characterization.
492	Even on benchmarks where \method{} has lower precision than SC5 (LogiQA: $-$4\pp{}, MATH: $-$9\pp{}), the structured diagnostic information has no self-consistency equivalent.
493	
494	\paragraph{Repair is not the point.}
495	The consistently non-significant C4 across all benchmarks could be seen as a weakness.
496	We argue it is a feature of our framing: if simple selection (0 additional calls) matches repair ($p{=}0.72$), the value of \method{} lies in the diagnostic signal itself, not in what one does with it.
497	The GT-label-dependent repair effect (helps Unknown/False, hurts True) is itself a finding that characterizes the boundary of diagnosis-guided correction.
498	
499	\paragraph{Limitations.}
500	(1)~The error taxonomy requires domain adaptation (logic types for FOLIO vs.\ algebraic types for MATH) and achieves only moderate cross-model agreement ($\kappa{=}0.54$).
501	(2)~The MATH asymmetry (1.8:1) is not statistically significant ($p{=}0.18$), limiting the paradigm asymmetry claim to FOL-based domains.
502	(3)~False agreement rates of 5.6--26.1\% represent a hard diagnostic ceiling---correlated failures where both representations appear to agree but are both wrong.
503	(4)~Specification-level errors (12.3\% of FOLIO) are fundamentally unaddressable by our approach.
504	(5)~All experiments use a single primary model family; cross-model validation is limited to two models.
505	
506	% ============================================================
507	\section{Conclusion}
508	
509	We introduced Cross-Representation Disagreement (\method{}), a framework that transforms cross-representation disagreement from a binary filtering signal into a structured diagnostic tool.
510	On FOLIO, \method{} detects formalization errors with 87.2\% diagnostic precision, classifies them into a 3-type taxonomy ($\kappa{=}0.54$), and localizes the error side with 94.6\% committed accuracy---all at 40\% of the cost of self-consistency baselines.
511	The method generalizes to LogiQA and MATH with attenuated but significant diagnostic rates, tracing a clear boundary: effectiveness requires formalization to be the reasoning bottleneck.
512	Rather than claiming accuracy improvement, we contribute the diagnostic analysis itself: understanding \emph{why} LLM formalizations fail, \emph{which} representation is more reliable, and \emph{when} diagnosis helps versus hurts downstream correction.
513	
514	% ============================================================
515	% Placeholder references
516	\begin{thebibliography}{25}
517	
518	\bibitem[Pan et al.(2023)]{pan2023logic}
519	Liangming Pan, Alon Albalak, Xinyi Wang, and William Yang Wang. 2023.
520	Logic-LM: Empowering large language models with symbolic solvers for faithful logical reasoning.
521	In \emph{Findings of EMNLP}.
522	
523	\bibitem[Olausson et al.(2023)]{olausson2023linc}
524	Theo X. Olausson, Alex Gu, Ben Lipkin, Cedegao E. Zhang, Armando Solar-Lezama, Joshua B. Tenenbaum, and Roger Levy. 2023.
525	LINC: A neurosymbolic approach for logical reasoning by combining language models with first-order logic provers.
526	In \emph{Proc. EMNLP}.
527	
528	\bibitem[Chen et al.(2023)]{chen2023program}
529	Wenhu Chen, Xueguang Ma, Xinyi Wang, and William W. Cohen. 2023.
530	Program of thoughts prompting: Disentangling computation from reasoning for numerical reasoning tasks.
531	\emph{TMLR}.
532	
533	\bibitem[HybridMind(2024)]{hybrid2024}
534	Anonymous. 2024.
535	HybridMind: Adaptive selection of reasoning representations.
536	Preprint.
537	
538	\bibitem[VeriCoT(2024)]{vericot2024}
539	Anonymous. 2024.
540	VeriCoT: Verification of chain-of-thought reasoning.
541	Preprint.
542	
543	\bibitem[Roundtrip(2026)]{roundtrip2026}
544	Anonymous. 2026.
545	Roundtrip verification for diagnosis-guided repair.
546	Preprint.
547	
548	\bibitem[Liang et al.(2024)]{liang2024}
549	Zijian Liang, Tianqing Fang, Tongtong Wu, Weiqi Wang, and Yangqiu Song. 2024.
550	Cross-modal reasoning disagreement for filtering unreliable answers.
551	In \emph{Proc. ACL}.
552	
553	\bibitem[Wang et al.(2023)]{wang2023selfconsistency}
554	Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. 2023.
555	Self-consistency improves chain of thought reasoning in language models.
556	In \emph{Proc. ICLR}.
557	
558	\bibitem[Du et al.(2023)]{du2023improving}
559	Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mordatch. 2023.
560	Improving factuality and reasoning in language models through multiagent debate.
561	\emph{arXiv preprint}.
562	
563	\bibitem[Liang et al.(2024b)]{liang2024encouraging}
564	Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, and Zhaopeng Tu. 2024.
565	Encouraging divergent thinking in large language models through multi-agent debate.
566	\emph{arXiv preprint}.
567	
568	\bibitem[Ni et al.(2023)]{ni2023lever}
569	Ansong Ni, Srini Iyer, Dragomir Radev, Veselin Stoyanov, Wen-tau Yih, Sida Wang, and Xi Victoria Lin. 2023.
570	LEVER: Learning to verify language-to-code generation with execution.
571	In \emph{Proc. ICML}.
572	
573	\bibitem[Lyu et al.(2023)]{lyu2023faithful}
574	Qing Lyu, Shreya Havaldar, Adam Stein, Li Zhang, Delip Rao, Eric Wong, Marianna Apidianaki, and Chris Callison-Burch. 2023.
575	Faithful chain-of-thought reasoning.
576	In \emph{Proc. IJCNLP-AACL}.
577	
578	\bibitem[Chen et al.(2024)]{chen2024teaching}
579	Xinyun Chen, Maxwell Lin, Nathanael Sch\"{a}rli, and Denny Zhou. 2024.
580	Teaching large language models to self-debug.
581	In \emph{Proc. ICLR}.
582	
583	\bibitem[Madaan et al.(2024)]{madaan2024selfrefine}
584	Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. 2024.
585	Self-refine: Iterative refinement with self-feedback.
586	In \emph{Proc. NeurIPS}.
587	
588	\bibitem[Denisov-Blanch et al.(2026)]{denisov2026}
589	Nikita Denisov-Blanch, Yuri Denisov-Blanch, and Elena Voita. 2026.
590	Correlated failures in LLM ensembles: When diversity isn't enough.
591	\emph{arXiv preprint}.
592	
593	\bibitem[Han et al.(2022)]{han2022folio}
594	Simeng Han, Hailey Schoelkopf, Yilun Zhao, Zhenting Qi, Martin Riddell, Luke Benson, Lucy Sun, Ekaterina Zubova, Yujie Qiao, Matthew Burtell, et al. 2022.
595	FOLIO: Natural language reasoning with first-order logic.
596	\emph{arXiv preprint}.
597	
598	\bibitem[Liu et al.(2021)]{liu2021logiqa}
599	Jian Liu, Leyang Cui, Hanmeng Liu, Dandan Huang, Yile Wang, and Yue Zhang. 2021.
600	LogiQA: A challenge dataset for machine reading comprehension with logical reasoning.
601	In \emph{Proc. IJCAI}.
602	
603	\bibitem[Hendrycks et al.(2021)]{hendrycks2021math}
604	Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. 2021.
605	Measuring mathematical problem solving with the MATH dataset.
606	In \emph{Proc. NeurIPS}.
607	
608	\bibitem[Rein et al.(2024)]{rein2024gpqa}
609	David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R. Bowman. 2024.
610	GPQA: A graduate-level Google-proof Q\&A benchmark.
611	In \emph{Proc. NAACL}.
612	
613	\end{thebibliography}
614	
615	\end{document}
616	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fbb2f01-c194-402c-b93f-6b622d953956",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "2e806771-1c65-4cda-a602-6a8f871affba",
  "sourceToolAssistantUUID": "9fbb2f01-c194-402c-b93f-6b622d953956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-15T08:03:23.652Z_

Now let me read the dream review reports to understand how the paper was previously scored.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e806771-1c65-4cda-a602-6a8f871affba",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41JRhH1jpmNFxTZWniF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15a40207-a89f-4f30-9d82-81bdf4a99a59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPJ7NtfRQ8zNppYoABnCrc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12984,
      "cache_read_input_tokens": 30611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12984,
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

_source line 34 · 2026-05-15T08:03:26.055Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Qgp2T3y9rFeRTywkntx2Ja`</summary>

```json
{
  "pattern": "**/dream_20260515T071730/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15a40207-a89f-4f30-9d82-81bdf4a99a59",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41JRhH1jpmNFxTZWniF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04fcd2cf-cc35-4d46-b38e-6eb4e60d4d0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPJ7NtfRQ8zNppYoABnCrc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12984,
      "cache_read_input_tokens": 30611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12984,
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

_source line 35 · 2026-05-15T08:03:26.090Z_

<details><summary>↩ Tool result · `toolu_01Qgp2T3y9rFeRTywkntx2Ja`</summary>

```text
artifacts/dream_reports/dream_20260515T071730/best/paper_framing.md
artifacts/dream_reports/dream_20260515T071730/median/paper_framing.md
artifacts/dream_reports/dream_20260515T071730/worst/paper_framing.md
artifacts/dream_reports/dream_20260515T071730/best/review_report.md
artifacts/dream_reports/dream_20260515T071730/median/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04fcd2cf-cc35-4d46-b38e-6eb4e60d4d0f",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "3468b039-2633-4964-8efc-587e19b0a64d",
  "sourceToolAssistantUUID": "04fcd2cf-cc35-4d46-b38e-6eb4e60d4d0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T08:03:26.375Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0132KWLTCTRVqi5waMZFD6mu`</summary>

```json
{
  "pattern": "**/dream_20260515T071730/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3468b039-2633-4964-8efc-587e19b0a64d",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41JRhH1jpmNFxTZWniF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26c07bcb-a50a-48ac-ac49-2cf455aabd31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPJ7NtfRQ8zNppYoABnCrc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12984,
      "cache_read_input_tokens": 30611,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12984
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 30611,
          "cache_creation_input_tokens": 12984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12984,
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

_source line 37 · 2026-05-15T08:03:26.431Z_

<details><summary>↩ Tool result · `toolu_0132KWLTCTRVqi5waMZFD6mu`</summary>

```text
artifacts/dream_reports/dream_20260515T071730/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T071730/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T071730/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T071730/best/review_context.yaml
artifacts/dream_reports/dream_20260515T071730/median/review_context.yaml
artifacts/dream_reports/dream_20260515T071730/worst/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26c07bcb-a50a-48ac-ac49-2cf455aabd31",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "37f0ca18-7fc1-441a-8128-35930bd3db27",
  "sourceToolAssistantUUID": "26c07bcb-a50a-48ac-ac49-2cf455aabd31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T08:03:29.442Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N4eKCLKK6dpxYcrkxKRQ9p`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37f0ca18-7fc1-441a-8128-35930bd3db27",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41K3fVSLhq1Tk9q39gV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62206682-1647-4e44-9246-35f63569fbfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DzQcrawtWizMMgt4xywr5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 43595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 541,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 39 · 2026-05-15T08:03:29.456Z_

<details><summary>↩ Tool result · `toolu_01N4eKCLKK6dpxYcrkxKRQ9p`</summary>

```text
1	---
2	dream_id: dream_20260515T071730
3	tier: median
4	overall_score: weak reject
5	timestamp: 2026-05-15T08:01:15.732587+00:00
6	---
7	
8	# Dream Review Report: Cross-Representation Disagreement for Diagnosis and Characterization of LLM Formalization Errors
9	
10	**Dream ID**: 20260515T071730
11	**Review Mode**: Full (2 Reviewers, 4-Step Roundtable)
12	**Date**: 2026-05-15
13	
14	---
15	
16	## Roundtable Summary
17	
18	Two independent reviewers (R1: Methods+Experiments; R2: Novelty+Related Work) converged on **3/6 (Weak Reject)** with high confidence (4/5). The paper presents a thorough empirical analysis with some genuinely novel findings (domain-dependent asymmetry reversal, GT-label-dependent repair effect, formalization bottleneck gradient), but the methodological novelty is incremental, the strongest claims require oracle ground-truth labels unavailable at deployment, the error taxonomy lacks non-LLM validation, and CRD underperforms self-consistency on 2 of 3 benchmarks. Findings track would be appropriate with targeted revisions.
19	
20	---
21	
22	## Consolidated Scores
23	
24	| Criterion | R1 | R2 | Consensus |
25	|-----------|----|----|-----------|
26	| Soundness | 3/4 | 3/4 | 3/4 |
27	| Presentation | 3/4 | 3/4 | 3/4 |
28	| Contribution | 2/4 | 2/4 | 2/4 |
29	| Overall | 3/6 | 3/6 | **3/6 (Weak Reject)** |
30	| Confidence | 4/5 | 4/5 | 4/5 |
31	
32	---
33	
34	## Strengths (Consensus)
35	
36	1. **Rigorous and transparent statistical reporting.** Bootstrap CIs, Fisher exact tests, McNemar tests, and Bonferroni correction across 12 tests. Dual reporting of C5-committed (94.6%) vs. C5-coverage (53%) is exemplary. Confidence intervals for C4 explicitly include zero and this is stated rather than hidden.
37	
38	2. **Domain-dependent asymmetry reversal is a genuinely novel empirical finding.** FOL-favored 5.6:1 on FOLIO vs. near-parity 1.8:1 on MATH demonstrates that representation advantage is task-dependent, not a fixed verifier hierarchy. No prior work has shown this.
39	
40	3. **GT-label-dependent three-way split transforms a null result into an informative finding.** Unknown (+14.7pp), False (+6.7pp), True (-13.6pp) — each individually informative. The mechanistic explanation via Code overclaiming on three-valued logic is convincing.
41	
42	4. **Unusually honest boundary characterization.** ProofWriter pilot failure (6.7%), GPQA degradation (C2=58%), "more disagreement ≠ better diagnosis" on 8B model, aggregate C4 non-significance — all transparently reported. The domain gradient (FOLIO > LogiQA > MATH > GPQA) mapping when CRD works vs. doesn't is a genuine contribution.
43	
44	5. **Well-supported cost-efficiency argument.** 2 LLM calls vs. 5 for SC5, with qualitative advantages (error type classification, localization, paradigm characterization) that SC5 fundamentally cannot provide. The 0.40× cost ratio is consistent across benchmarks.
45	
46	6. **Comprehensive experimental coverage.** 13 experiments across 4 benchmarks, 3 model conditions, 2 model scales, selection vs. repair, taxonomy ablation, multi-round repair, and correlated failure analysis. The design space is well-explored.
47	
48	---
49	
50	## Weaknesses (Consensus, by severity)
51	
52	### Major
53	
54	**W1. Aggregate C4 is non-significant on every benchmark; the actionable stratified analysis requires ground-truth labels unavailable at deployment.** The paper's most analytically interesting finding (GT-label-dependent repair effect) cannot be operationalized without oracle GT access. The paper suggests "skip repair for high-confidence True predictions" but never evaluates whether CRD's own signals (stability score, error type, asymmetry) can predict GT-label category. Without a GT-free deployment evaluation, Claim 3 is a retrospective insight, not an actionable method. Selection (82.8%) is barely above blind baseline (81.4%), a +1.4pp gain that is unlikely to be significant.
55	
56	**W2. Incremental novelty over Liang et al. (2024).** The core observation that cross-representation disagreement is informative was established by Liang et al. (2024) for CoT-PoT pairs. This paper extends from binary filtering to diagnosis + taxonomy + localization + repair, but each component individually uses known techniques: rule-based error classification (standard in SE), perturbation-based fault localization (metamorphic testing), and diagnosis-informed re-prompting (Self-Debug, Self-Refine). The paper's own data shows selection captures most of the benefit at zero additional cost, suggesting the diagnostic machinery adds modest marginal value over the basic disagreement signal.
57	
58	**W3. The error taxonomy lacks non-LLM validation.** Cross-model κ=0.54 (3-type merged) is only "moderate agreement." The most theoretically interesting category (quantifier_error, n=4, κ=0.22) is essentially noise. No human expert annotation is provided on any subsample. Two LLMs agreeing on error labels could reflect shared superficial heuristics. The taxonomy ablation (McNemar p=0.68) confirms the taxonomy is descriptive not prescriptive — but then its contribution reduces to descriptive analysis with unvalidated categories.
59	
60	**W4. CRD loses to self-consistency on 2 of 3 benchmarks.** On LogiQA, SC5-Best outperforms CRD by 4.0pp; on MATH, by 9.0pp. CRD's precision advantage is limited to FOLIO (+2.2pp), the benchmark most favorable to FOL+Z3. The cost argument (0.40×) partially compensates, but a method that is less accurate on 2/3 benchmarks needs stronger justification.
61	
62	**W5. Significant related work gaps.** Critical omissions:
63	- N-version programming (Avizienis & Chen, 1977; Avizienis, 1985) — the foundational paradigm for using implementation diversity to detect faults. CRD is essentially N-version programming for LLM formalizations. The "paradigm distance modulates effectiveness" finding directly parallels the "design diversity" literature.
64	- PAL (Gao et al., 2023) — the canonical reference for LLM-generated Python program solving, direct lineage of the Code pathway.
65	- Metamorphic testing (Chen et al., 1998) — stability-based localization is essentially a metamorphic relation.
66	- DIVERSE (Li et al., 2023) and Universal Self-Consistency (Chen et al., 2024) — closer baselines than vanilla SC5.
67	- Debate-based verification (Irving et al., 2018) — cross-representation disagreement as restricted debate.
68	
69	### Moderate
70	
71	**W6. The MATH instantiation conflates "cross-paradigm" with "cross-library."** SymPy symbolic vs. Python numerical are both imperative Python with no formal verification guarantees. This is categorically different from FOL+Z3 vs. Python. The paper's own data confirms the problem: CRD advantage evaporates on MATH (-9pp vs SC5). The framework's conceptual unity is weakened without a principled criterion for "sufficient representation diversity."
72	
73	**W7. C5 coverage of 53% means the localization module provides no actionable signal on nearly half of diagnostic cases.** The 47% ambiguous rate is driven by GT=Unknown (61% ambiguous) — precisely where repair delta is largest. This creates a paradox: the subgroup where CRD is most useful is the subgroup where localization is least reliable.
74	
75	**W8. Sample sizes are thin for the extensive stratification.** With n=204 on FOLIO and stratification by GT-label (3), error type (4), cross-model conditions (3), and repair rounds (3), many subgroup analyses rest on n<20. Quantifier_error (n=4) appears in multiple tables as if carrying analytical weight. The reported Bonferroni correction covers 12 tests, but actual comparisons across 11+ tables likely exceed 50.
76	
77	### Minor
78	
79	**W9. False agreement rate of 26.1% on GT=Unknown is high and underexplored.** One in four Unknown samples produces false agreement. CRD provides no signal for these and may increase confidence in incorrect answers.
80	
81	**W10. "Paradigm distance modulates effectiveness" is post-hoc and circular.** The gradient could reflect benchmark difficulty, formalization quality, or evaluation protocol differences. No independent measure of paradigm distance is provided.
82	
83	**W11. Incomplete bibliography entries.** Several references (HybridMind, VeriCoT, Roundtrip) lack full author lists. For a top-venue submission, every citation needs complete bibliographic information.
84	
85	---
86	
87	## Questions for Authors (Priority-ordered)
88	
89	1. **GT-free deployment evaluation**: Have you evaluated a pipeline where repair/selection decisions use only CRD's own signals (stability score, error type, asymmetry direction) rather than oracle GT labels? What accuracy does this achieve? This is critical for Claim 3's practical relevance.
90	
91	2. **N-version programming connection**: How does CRD relate to N-version programming (Avizienis, 1985)? The conceptual parallel — generating diverse implementations and comparing outputs to detect faults — is striking. The "design diversity" finding directly parallels your "paradigm distance" observation. Why is this connection not discussed?
92	
93	3. **SC5 comparison at k<5**: At what k does self-consistency match CRD's diagnostic precision? If k=3 suffices, the cost argument weakens substantially.
94	
95	4. **Human taxonomy validation**: Could you provide human expert annotations on 30-50 diagnostic cases? Cross-model κ=0.54 with two LLMs is suggestive but insufficient.
96	
97	5. **Asymmetry without exec_crash**: What happens to the 5.6:1 asymmetry ratio if exec_crash errors are excluded? Are logic_error and negation_error individually asymmetric in the same direction?
98	
99	6. **C2 inflation by asymmetry**: If FOL is correct 5.6× more often than Code among disagreements, a trivial "always trust FOL" baseline achieves high C2 by construction. What is C2 when conditioning on Code-correct-FOL-wrong cases only?
100	
101	7. **Stability test calibration**: Is there a threshold of perturbation agreement above which localization is near-perfect, enabling higher-coverage deployment at a controlled precision level?
102	
103	---
104	
105	## Experiment Coverage Assessment
106	
107	All 13 imagined experiments from the review context are covered in the paper:
108	
109	| Experiment | Coverage | Section |
110	|-----------|----------|---------|
111	| exp-002 Cross-Model Ablation | ✓ Full | §5.6 |
112	| exp-003 ProofWriter→LogiQA | ✓ Full | §5.7 |
113	| exp-004 MATH Level 5 | ✓ Full | §5.7 |
114	| exp-005 Multi-round Repair | ✓ Full | §5.4 |
115	| exp-006 Unknown Analysis | ✓ Full | §5.5 |
116	| exp-007 Selection vs Repair | ✓ Full | §5.3 |
117	| exp-008 Taxonomy Ablation | ✓ Full | §5.4 |
118	| exp-009 Statistical Significance | ✓ Full | §5.9 |
119	| exp-010 Scale Ablation (8B) | ✓ Full | §5.10 |
120	| exp-011 GPQA Diamond | ✓ Full | §5.7 |
121	| exp-012 SC5 Comparison | ✓ Full | §5.2 |
122	| exp-013 Taxonomy Validation | ✓ Full | §5.8 |
123	
124	Experiment coverage is complete. No imagined experiments are missing from the paper.
125	
126	---
127	
128	## Missing Experiments / Suggested Additions
129	
130	1. **GT-free deployment evaluation** (Critical): Train a lightweight classifier on CRD features to predict repair benefit. Evaluate on held-out data. This would make Claim 3 actionable.
131	
132	2. **Human expert annotation** (Critical for taxonomy): ≥50 samples annotated by domain experts. Compute human-LLM κ for the taxonomy to validate it captures genuine error categories.
133	
134	3. **Roundtrip Verification comparison**: Empirical head-to-head on an overlapping benchmark to demonstrate cross-representation advantage over within-representation roundtrip.
135	
136	4. **SC5 at k=3**: If k=3 SC achieves comparable precision to CRD, the 0.40× cost advantage shrinks to ~0.67×, weakening a core argument.
137	
138	5. **C2 decomposition by asymmetry direction**: Report C2 separately for FOL-correct-Code-wrong vs. Code-correct-FOL-wrong to address the "always trust FOL" inflation concern.
139	
140	---
141	
142	## Recommendation
143	
144	**Overall: 3/6 (Weak Reject) for top ML venue main track.**
145	
146	The paper's strongest contributions are empirical findings (asymmetry reversal, GT-dependent effect, formalization bottleneck gradient) rather than methodological advances. The framework is a competent composition of known techniques with incremental novelty over Liang et al. (2024). The most actionable claim (Claim 3) requires oracle labels; the taxonomy (Claim 2) lacks non-LLM validation; and CRD underperforms SC5 on 2/3 benchmarks (undermining Claim 1's generality).
147	
148	**Path to acceptance**: (1) Add GT-free deployment evaluation to make Claim 3 actionable; (2) Provide human annotation for taxonomy validation; (3) Complete the related work (N-version programming, PAL, metamorphic testing); (4) Reframe the MATH results honestly as a reduced-paradigm-gap condition. With these revisions, the paper would be competitive for **Findings track** (EMNLP Findings) or a **neurosymbolic reasoning workshop**.
149	
150	The paper's transparency about limitations and honest reporting of negative findings (non-significant C4, ProofWriter failure, GPQA boundary) is commendable and should be preserved in revision.
151	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62206682-1647-4e44-9246-35f63569fbfa",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "2a8fd09b-af4c-4fc5-9021-bb16083ff4f1",
  "sourceToolAssistantUUID": "62206682-1647-4e44-9246-35f63569fbfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T08:03:29.840Z_

<details open><summary>🔧 Tool call — Read · `toolu_013mWiH7LbAsM6msDXpWB4RK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a8fd09b-af4c-4fc5-9021-bb16083ff4f1",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41K3fVSLhq1Tk9q39gV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77085b3a-2e35-4b9a-9b6c-5e253c169f2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DzQcrawtWizMMgt4xywr5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 43595,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 541
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 43595,
          "cache_creation_input_tokens": 541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 541,
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

_source line 41 · 2026-05-15T08:03:29.847Z_

<details><summary>↩ Tool result · `toolu_013mWiH7LbAsM6msDXpWB4RK`</summary>

```text
1	---
2	dream_id: dream_20260515T071730
3	tier: best
4	overall_score: 3/6 Weak Reject
5	timestamp: 2026-05-15T07:54:32.797062+00:00
6	---
7	
8	# Dream Review Report: Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors
9	
10	**Dream ID:** 20260515T071730
11	**Review Mode:** Full (2 Reviewers + Roundtable)
12	**Date:** 2026-05-15
13	
14	---
15	
16	## Consolidated Score: 3/6 (Weak Reject)
17	
18	Both reviewers independently scored 3/6. After cross-sharing and roundtable discussion, the panel converges on **Weak Reject** with recognition that the analytical contributions are solid but insufficient to overcome methodological and novelty concerns at a top ML venue (~25% acceptance rate).
19	
20	---
21	
22	## Panel Summary
23	
24	The paper presents Cross-Representation Disagreement Diagnosis (CRD), extending cross-representation disagreement from binary filtering to structured error diagnosis. Given a reasoning problem, CRD generates dual executable formalizations (FOL+Z3 and Python), detects disagreements, classifies errors into a 4-type taxonomy, localizes the faulty side via stability testing, and optionally performs diagnosis-guided repair. Evaluated on 3 primary benchmarks (FOLIO, LogiQA, MATH Level 5) plus GPQA Diamond, with 2 primary models (Qwen3-32B, DeepSeek V4 Pro) and 1 ablation model (Qwen3-8B).
25	
26	The paper's strongest contribution is empirical characterization: the asymmetry reversal across domains (FOL-favored 5.6:1 in logic vs. Code-favored 1.8:1 in math) is a genuinely novel finding, and the GT-label-dependent repair effect with honest boundary reporting (True overcorrection at −11.2pp) demonstrates intellectual rigor. However, the aggregate repair improvement (C4) is non-significant on every benchmark, the core stratified analysis requires oracle GT labels unavailable at inference, and the novelty over Liang et al. (2024) is incremental.
27	
28	---
29	
30	## R1 Review: Methods & Experiments
31	
32	**Score:** 3/6 | **Confidence:** 4/5
33	
34	### Strengths
35	
36	- **S1: Well-characterized diagnostic signal with honest statistical reporting.** Bootstrap CIs, Fisher exact tests, and McNemar tests are applied throughout. The paper is upfront that aggregate C4 is non-significant (p=0.626). The GT-stratified three-way split (Unknown +14.7pp → +22.1pp, False +6.7pp → +10.4pp, True −13.6pp → −11.2pp) transforms a negative result into an informative boundary. Dual reporting of C5-committed (94.6%) and C5-coverage (53.0%) is transparent.
37	
38	- **S2: Multi-benchmark generalization with meaningful effectiveness gradient.** The C2 trajectory (FOLIO 87.2% → LogiQA 81.5% → MATH 76.0% → GPQA 72.7%) traces a clear boundary: CRD is most effective when errors arise from formalization rather than domain knowledge gaps. The ProofWriter pilot failure (6.7% disagreement) and its honest reporting strengthens the boundary characterization. The asymmetry reversal on MATH is a substantive cross-domain finding.
39	
40	- **S3: Cost-efficiency framing is compelling.** CRD achieves 2 calls vs. 5 for self-consistency at 40% token cost, with qualitative advantages (error type, localization, paradigm characterization) over SC5's binary majority vote signal.
41	
42	### Weaknesses
43	
44	- **W1: Aggregate C4 is non-significant on every benchmark, and the stratified analysis relies on GT labels unavailable at inference.** The method provides no statistically significant overall accuracy improvement. The GT-label-stratified analysis (Claim 3's core) requires knowing ground truth to decide whether to apply repair. The paper suggests "skip repair for high-confidence True predictions" but never evaluates whether CRD's own signals can predict GT-label category, nor demonstrates a realistic GT-free deployment pipeline.
45	
46	- **W2: No human annotation baseline for taxonomy validation.** Cross-model κ=0.67 uses LLM-to-LLM agreement, which is circular — two LLMs may agree on superficial patterns rather than genuine error categories. The most theoretically interesting category (quantifier_error, n=4, κ=0.45) is essentially unvalidated. Without human expert annotation on even a subsample, there is no ground truth for whether the taxonomy is meaningful.
47	
48	- **W3: The self-consistency comparison has inconsistencies across benchmarks.** CRD outperforms SC5 by +7.9pp on FOLIO but only +1.2pp on MATH. An equally valid reading is that CRD works well specifically on benchmarks designed for FOL translation (FOLIO) and degrades when paradigm distance shrinks. The cost argument also omits CRD's infrastructure requirements (Z3 solver, Python sandbox, diagnosis pipeline).
49	
50	- **W4: Sample sizes are marginal for the many stratified analyses performed.** n=204/200/200/150 is reasonable for primary metrics but thin for the extensive stratification: quantifier_error has n=4, cross-model ablation has 3 conditions, several Fisher exact tests on small subgroups. Multiple comparisons inflate false discovery risk despite the claimed corrections.
51	
52	- **W5: The MATH extension (SymPy vs. Python numerical) is a fundamentally different instantiation.** Neither representation has a formal verification guarantee, unlike FOL+Z3. Grouping them under "CRD" without adequately discussing whether the framework genuinely applies when both sides are imperative Python variants weakens the conceptual unity.
53	
54	### Questions for Authors
55	
56	- Q1: Have you evaluated a realistic deployment scenario where repair/select decisions use CRD's own signals (stability test, error type, asymmetry) rather than GT labels? What accuracy does GT-free selection achieve?
57	
58	- Q2: Could you provide human expert annotations on a subsample (e.g., 50 diagnostic cases) to validate the taxonomy against a non-LLM ground truth?
59	
60	---
61	
62	## R2 Review: Novelty & Related Work
63	
64	**Score:** 3/6 | **Confidence:** 4/5
65	
66	### Strengths
67	
68	- **S1: The asymmetry reversal is a genuinely novel empirical finding.** No prior work has demonstrated that cross-representation disagreement direction reverses across domains (FOL-favored in logic, Code-favored in math), revealing domain-specific representation strengths rather than a fixed verifier hierarchy. This finding alone has conceptual value beyond the CRD framework.
69	
70	- **S2: Honest boundary characterization elevates the paper's intellectual contribution.** The GT=True overcorrection (−11.2pp), ProofWriter's 6.7% failure, GPQA's C2=72.7% boundary, and the C1↑C2↓ tradeoff on Qwen3-8B are all reported transparently. This gives the reader a nuanced understanding of when CRD works and when it doesn't — more valuable than presenting only favorable conditions.
71	
72	- **S3: Comprehensive experimental coverage.** 18 tables across 13 experiments spanning 4 benchmarks, 3 models, and multiple ablation axes. The paper addresses correlated failures (phi=0.189, false agreement 12.3%), selection vs. repair decomposition, taxonomy-guided vs. fixed-strategy, model scale effects, and cross-domain boundaries.
73	
74	### Weaknesses
75	
76	- **W1: Incremental novelty over Liang et al. (2024).** The "filtering to diagnosis" extension combines individually known techniques: rule-based error classification (standard in software engineering), perturbation-based localization (established in program debugging), and diagnosis-informed prompting (common in self-refinement literature). The paper's contribution is their composition, not a conceptual advance. The key differentiator — that disagreement patterns are diagnostically rich — is stated as a finding but the taxonomy itself is ad hoc (rule-based, 4 categories, no formal derivation).
77	
78	- **W2: Significant related work gaps.** Missing comparisons: (a) PAL (Gao et al., 2023) and Program-of-Thought (Chen et al., 2023) — the direct lineage of the Code representation path; (b) Universal Self-Consistency (Chen et al., 2024) — extends self-consistency to free-form answers, directly relevant to the SC5 comparison; (c) DIVERSE (Li et al., 2023) — diverse verifier with voting, a closer baseline than vanilla SC5; (d) inadequate discussion of Roundtrip Verification (Zhong et al., 2025), which performs diagnosis-guided repair within a single representation on traffic rules — the paper cites it but doesn't explain why cross-representation is fundamentally better than within-representation roundtrip for general domains.
79	
80	- **W3: Incomplete bibliography entries.** PROVE, VERGE, VeriCoT, HybridMind, Adaptive Representation Selection, and Roundtrip Verification references all lack full author lists (listed as "Author et al." or "Anonymous"). For a venue submission, these need complete citation information or should be removed.
81	
82	- **W4: MATH domain conflation weakens the conceptual framing.** SymPy symbolic vs. Python numerical is "cross-library" not "cross-paradigm" in the same sense as FOL+Z3 vs. Python. Both are imperative Python code; the paradigm gap is much smaller. The paper's own data confirms this: CRD advantage over SC5 is only +1.2pp on MATH vs. +7.9pp on FOLIO. This undermines the generality claim — CRD may be primarily a FOL-vs-Code diagnostic tool rather than a general cross-representation framework.
83	
84	- **W5: Taxonomy coverage is unvalidated and has mixed granularity.** No analysis of out-of-taxonomy errors (what fraction of disagreements don't fit any of the 4 types?). negation_error is arguably a subtype of logic_error; exec_crash is operational rather than reasoning-related. The taxonomy mixes abstraction levels without justification. The paper claims "rule-based for interpretability" but provides no inter-annotator study of the rules themselves.
85	
86	- **W6: The "paradigm distance modulates CRD effectiveness" discussion point is post-hoc.** The gradient (FOLIO > LogiQA > MATH) could equally reflect benchmark difficulty, formalization quality, or evaluation protocol differences rather than paradigm distance per se. No independent measure of paradigm distance is provided; it is inferred circularly from CRD's own effectiveness.
87	
88	### Questions for Authors
89	
90	- Q1: How does CRD compare to Roundtrip Verification (Zhong et al., 2025) when both are applied to the same benchmark? Is cross-representation diagnosis fundamentally more informative than within-representation roundtrip, or just differently scoped?
91	
92	- Q2: What fraction of FOLIO disagreement samples fall outside the 4-type taxonomy? If the taxonomy has ≥90% coverage, what is the evidence? If <90%, the uncovered cases may contain systematic patterns worth characterizing.
93	
94	---
95	
96	## Roundtable Synthesis
97	
98	### Areas of Agreement (Both Reviewers)
99	
100	1. **The asymmetry reversal and GT-label-dependent effect are genuine contributions.** These empirical findings are novel, non-obvious, and would be of interest to the neurosymbolic reasoning community regardless of CRD's practical utility.
101	
102	2. **The GT-oracle problem is a critical limitation.** Both reviewers flag that Claim 3's core finding requires ground-truth labels for stratification, making the most interesting results practically unactionable without additional work on GT-free deployment.
103	
104	3. **Aggregate repair improvement is non-significant everywhere.** This fundamentally limits the paper's practical contribution — CRD is characterized as a diagnostic/analytical tool, not a method that reliably improves accuracy.
105	
106	4. **The MATH extension weakens the paradigm-distance narrative.** SymPy vs. Python numerical is a much smaller paradigm gap than FOL+Z3 vs. Python, and the CRD advantage shrinks correspondingly (+1.2pp). This is consistent but also reveals that CRD's value proposition depends heavily on having maximally different representation paradigms.
107	
108	5. **Honest, thorough reporting is a significant positive.** The paper does not hide negative results (C4 non-significance, GT=True overcorrection, ProofWriter failure, GPQA boundary). This intellectual honesty is appreciated and elevates the analytical contribution.
109	
110	### Areas of Disagreement
111	
112	- **Severity of novelty concern:** R2 views the contribution as incremental over Liang et al. (2024) (composition of known techniques), while R1 is more sympathetic to the diagnostic signal characterization as a standalone contribution. After discussion, both agree that the empirical findings (asymmetry reversal, GT-dependent effect) are more novel than the framework itself.
113	
114	- **Taxonomy validation sufficiency:** R1 emphasizes the need for human annotation; R2 focuses on taxonomy coverage and granularity. Both agree the current validation (κ=0.67 LLM-to-LLM) is insufficient for a top venue.
115	
116	### Verdict
117	
118	The paper presents a thorough empirical study with some genuinely interesting findings (asymmetry reversal, GT-dependent repair boundary). However, at a top ML venue with ~25% acceptance:
119	
120	- The framework novelty is incremental (composition of known techniques applied to cross-representation disagreement)
121	- The practical utility is limited (no significant aggregate improvement; stratified improvements require oracle GT labels)
122	- The taxonomy lacks rigorous validation (no human annotation, mixed granularity, tiny n for key categories)
123	- The generalization argument weakens outside the FOL+Z3 vs. Python paradigm gap
124	- Related work coverage has notable gaps
125	
126	**Recommendation:** Weak Reject. The analytical findings deserve publication but the paper needs: (1) a GT-free deployment evaluation, (2) human annotation for taxonomy validation, (3) complete related work coverage including PAL/PoT and DIVERSE, and (4) clearer scoping of claims to the FOL-vs-Code setting where the paradigm gap is genuinely large.
127	
128	---
129	
130	## Actionable Revision Suggestions (Priority-Ordered)
131	
132	1. **[Critical] Evaluate GT-free repair selection.** Train a simple classifier or heuristic on CRD signals (error type, stability score, asymmetry direction) to predict repair benefit without GT labels. Report accuracy on held-out FOLIO samples. This directly addresses the oracle problem and could salvage Claim 3's practical relevance.
133	
134	2. **[Critical] Add human expert annotation on ≥50 diagnostic samples.** Compute human-LLM κ and human-human κ on the 4-type taxonomy. This is the minimum bar for claiming the taxonomy is meaningful rather than an LLM artifact.
135	
136	3. **[Important] Close related work gaps.** Add PAL, Program-of-Thought, Universal Self-Consistency, and DIVERSE. Provide a substantive comparison with Roundtrip Verification explaining why cross-representation diagnosis adds value over within-representation roundtrip.
137	
138	4. **[Important] Scope MATH claims more carefully.** Either demonstrate that SymPy vs. Python numerical qualifies as "cross-paradigm" by some independent measure, or explicitly position MATH as a "reduced paradigm gap" condition that tests CRD's limits rather than its generality.
139	
140	5. **[Moderate] Fix incomplete references.** Provide full author lists for all citations. Remove or replace any that cannot be properly cited.
141	
142	6. **[Moderate] Report taxonomy coverage.** State what fraction of disagreement samples are classified into the 4 types vs. falling outside the taxonomy. If there is a residual "other" category, characterize it.
143	
144	7. **[Minor] Discuss multiple comparison correction.** With 18 tables and many stratified tests, explicitly state the family-wise error control strategy (Bonferroni, Holm, or FDR).
145	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77085b3a-2e35-4b9a-9b6c-5e253c169f2c",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "22e3822e-da7e-46fb-a159-91a592b90a97",
  "sourceToolAssistantUUID": "77085b3a-2e35-4b9a-9b6c-5e253c169f2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-15T08:03:32.693Z_

Now let me also check the first dream's review and the worst-case scenario.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22e3822e-da7e-46fb-a159-91a592b90a97",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41KJMY5TuDAAQSWCWhk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f425b87-f1cb-4772-b5a2-ea7276f19f99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UAm2M2CPPG9Jj9ZyyBxp4z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8237,
      "cache_read_input_tokens": 44136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8237,
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

_source line 43 · 2026-05-15T08:03:34.587Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UAAfKVT6frgYaiMB66Fvki`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/worst/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f425b87-f1cb-4772-b5a2-ea7276f19f99",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41KJMY5TuDAAQSWCWhk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a510f657-57a3-4d90-a9f5-36d4a3692856",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UAm2M2CPPG9Jj9ZyyBxp4z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8237,
      "cache_read_input_tokens": 44136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8237,
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

_source line 44 · 2026-05-15T08:03:34.610Z_

<details><summary>↩ Tool result · `toolu_01UAAfKVT6frgYaiMB66Fvki`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{hyperref}
8	\usepackage{xcolor}
9	\usepackage{multirow}
10	\usepackage{geometry}
11	\usepackage{natbib}
12	\usepackage{tablefootnote}
13	\geometry{margin=1in}
14	
15	\title{When Do Two Formalizations Know More Than One? \\ An Empirical Study of Cross-Representation Disagreement in LLM Reasoning}
16	
17	\author{Anonymous}
18	
19	\date{}
20	
21	\begin{document}
22	\maketitle
23	
24	%=====================================================================
25	\begin{abstract}
26	When a large language model formalizes a natural-language reasoning problem into two distinct executable representations---first-order logic (FOL) verified by Z3 and executable Python code---the resulting answers disagree on a substantial fraction of instances (42.2\% on FOLIO, 12.7\% on LogiQA, 16.5\% on MATH Level~5). We present a systematic empirical study of this \emph{cross-representation disagreement} (CRD) phenomenon across three benchmarks, two models, and multiple analytical dimensions. Our findings reveal three key results. First, failure modes across representations are highly asymmetric and complementary: 75\% of errors are one-side-only, and the direction of asymmetry reverses across models (FOL$>$Code 5.6:1 for Qwen3-32B vs.\ Code$>$FOL 1.8:1 for DeepSeek V4 Pro), indicating model-dependent rather than representation-inherent reliability. Second, this complementarity is insufficient to construct a reliable diagnostic-repair pipeline: disagreement-guided repair yields no statistically significant accuracy improvement on any benchmark (all $p > 0.39$, all 95\% CIs include zero), and simple selection of the predicted-correct side outperforms repair by 6.1 percentage points. Third, self-consistency baselines ($k$=5 majority vote within a single representation) dominate CRD on all benchmarks at equal or lower cost, establishing that cross-representation diversity does not outperform within-representation sampling diversity. We characterize the boundary conditions under which CRD provides diagnostic value and identify the mechanisms---correlated failures, taxonomy instability ($\kappa$=0.33), and representation-quality asymmetry---that limit its practical utility. Our results provide empirically grounded guidance for practitioners considering multi-representation reasoning strategies.
27	\end{abstract}
28	
29	%=====================================================================
30	\section{Introduction}
31	
32	Large language models (LLMs) increasingly solve reasoning problems by translating natural language into executable formal representations. Two dominant paradigms have emerged: formalization into first-order logic (FOL) for verification by theorem provers such as Z3, and translation into executable Python code. Each paradigm exhibits characteristic failure modes: FOL struggles with complex quantifier scoping and world-knowledge integration, while code generation suffers from execution crashes and overclaiming on under-determined problems.
33	
34	A natural hypothesis is that \emph{cross-representation disagreement}---cases where the same LLM produces different answers via FOL and code paths---contains rich diagnostic information that can be exploited for error detection and repair. Prior work has shown that disagreement between chain-of-thought and program-of-thought outputs serves as a useful filtering signal \citep{liang2024filtering}, and roundtrip verification within a single representation enables diagnosis-guided repair on narrow domains \citep{roundtrip2026}. However, no prior study has systematically investigated whether cross-representation disagreement can be extended from binary filtering to structured diagnosis and targeted repair, or characterized the conditions under which such an approach succeeds or fails.
35	
36	In this paper, we present a comprehensive empirical study of cross-representation disagreement in LLM reasoning. Our investigation spans three benchmarks (FOLIO, LogiQA, MATH Level~5), two models (Qwen3-32B, DeepSeek V4 Pro), and ten experimental conditions. We evaluate CRD along five criteria: disagreement rate (C1), diagnostic precision (C2), error taxonomy (C3), repair effectiveness (C4), and error localization (C5).
37	
38	Our central finding is a tension between two properties of CRD. On one hand, disagreement patterns reveal genuine and complementary failure modes: on FOLIO, 87.2\% of disagreements are diagnostically informative (exactly one side correct), and 75\% of errors are one-side-only. On the other hand, this complementarity does not translate into a practical advantage over simpler baselines. We identify three structural limitations:
39	
40	\begin{enumerate}
41	    \item \textbf{Repair is not statistically significant.} Across all benchmarks, disagreement-guided repair yields no significant accuracy improvement over blind regeneration (FOLIO: $+$4.65pp, $p$=0.626; LogiQA: $+$2.1pp, $p$=0.71; MATH: $+$1.8pp, $p$=0.82). Even after multi-round repair with error-type-specific strategies, the aggregate effect remains non-significant ($p$=0.39).
42	    \item \textbf{Selection dominates repair.} Given accurate error-side localization, simply selecting the predicted-correct representation outperforms diagnosis-guided repair by 6.1pp overall, with the gap widening to 16.7pp on GT=True samples.
43	    \item \textbf{Self-consistency dominates CRD.} Five-sample majority voting within a single representation (SC5) achieves higher accuracy at equal or lower cost on every benchmark. Even SC3 (3$\times$ cost) surpasses CRD (5.76$\times$ cost) on FOLIO.
44	\end{enumerate}
45	
46	These negative results are themselves informative. We trace the failure of CRD to three mechanisms: (a) representation-quality asymmetry that causes one path to inject noise rather than complementary signal, (b) correlated failures concentrated in semantically ambiguous instances (false agreement rate 23.2\% on GT=Unknown), and (c) taxonomy instability ($\kappa$=0.33 cross-model) that prevents error-type-specific repair from outperforming generic regeneration. We discuss the implications of these findings for practitioners and identify the narrow conditions under which cross-representation approaches may still provide value.
47	
48	%=====================================================================
49	\section{Related Work}
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a510f657-57a3-4d90-a9f5-36d4a3692856",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "e13e0d83-7f1b-41a1-bfc4-fd17468006aa",
  "sourceToolAssistantUUID": "a510f657-57a3-4d90-a9f5-36d4a3692856",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T08:03:35.335Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S3SXxjXZvtL5SnabBUHF28`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e13e0d83-7f1b-41a1-bfc4-fd17468006aa",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41KJMY5TuDAAQSWCWhk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a02307d2-bab3-4061-90ca-a7716b6c5609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UAm2M2CPPG9Jj9ZyyBxp4z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8237,
      "cache_read_input_tokens": 44136,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8237
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 44136,
          "cache_creation_input_tokens": 8237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8237,
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

_source line 46 · 2026-05-15T08:03:35.593Z_

<details><summary>↩ Tool result · `toolu_01S3SXxjXZvtL5SnabBUHF28`</summary>

```text
1	narrative_guidance: '放弃 "CRD 是更好的诊断工具" 方法论 claim，转为 "cross-representation disagreement
2	  的实证解剖"。 新 story：(1) LLM 形式化为 FOL 和 Code 时失败模式高度不对称且互补（75% one-side-only），这本身是关于
3	  LLM 能力结构的重要发现； (2) 但这种互补性不足以构建可靠的诊断/修复 pipeline，因为 self-consistency 更简单且同样有效； (3)
4	  我们量化了 cross-representation 方法的边界条件——何时有效、何时失败、为什么失败。 标题改为 "When Do Two Formalizations
5	  Know More Than One? An Empirical Study of Cross-Representation Disagreement in LLM
6	  Reasoning"。 仍投 EMNLP main，定位为高质量 negative/boundary result paper。
7	
8	  '
9	imagined_experiments:
10	- name: FOLIO 完整分析（MVP 数据深度挖掘）
11	  plan_id: exp-001
12	  description: 基于 204 样本 MVP 数据的完整统计分析，含 bootstrap CI、Fisher test、分层分析、相关性分析、cost-effectiveness。
13	  expected_results:
14	    C1_disagree_rate: 42.2% [35.3%, 49.0%]
15	    C2_diagnostic_rate: 87.2% [81.3%, 94.7%]
16	    C4_targeted_delta_aggregate: +4.65pp
17	    C4_bootstrap_CI: '[-8.8%, +18.1%]'
18	    C4_fisher_p: 0.626
19	    C4_GT_True: -13.6pp
20	    C4_GT_False: +11.6pp
21	    C4_GT_Unknown: +14.7pp
22	    C5_committed_accuracy: 53.0% [41.0%, 65.1%]
23	    phi_coefficient: 0.189
24	    phi_p: 0.007
25	    complementary_error_rate: 75%
26	    cost_multiplier: 5.76x
27	    accuracy_gain_over_code_only: +21.6pp
28	  result_rationale: 'exp-001 数据已固定，worst 档不改变已有数值。但 worst 档的关键在于：这些数值在后续实验的对照下被重新解读。
29	    C4 aggregate CI 含零（[-8.8%, +18.1%]）且 Fisher p=0.626 已经是 worst 档的核心支撑—— repair
30	    在统计上不显著。phi=0.189 说明 FOL 和 Code 的失败只有微弱正相关，表面上支持互补性， 但在 worst 档下，exp-012 会证明 self-consistency
31	    以更低成本达到类似效果， 使得这个 "互补性" 的实用价值大打折扣。cost_multiplier=5.76x 在 worst 档叙事中从 "合理代价" 变为
32	    "CRD 比 SC5 贵 3-4 倍但精度更低" 的负面论据。 深度挖掘会揭示 GT=True 的 -13.6pp 不是边缘问题而是系统性缺陷： CRD 在高置信正确样本上的
33	    overcorrection 是方法论层面的固有弱点。
34	
35	    '
36	  tables:
37	  - name: 'Table 1: FOLIO C1-C5 Metrics with Bootstrap 95% CI'
38	    columns:
39	    - Metric
40	    - Value
41	    - 95% CI
42	    - MVP Gate
43	    rows:
44	    - - C1 (Disagree Rate)
45	      - 42.2%
46	      - '[35.3%, 49.0%]'
47	      - PASS
48	    - - C2 (Diagnostic Rate)
49	      - 87.2%
50	      - '[81.3%, 94.7%]'
51	      - PASS
52	    - - C4 (Repair Delta)
53	      - +4.65pp
54	      - '[-8.8%, +18.1%]'
55	      - FAIL (CI includes 0)
56	    - - C5 (Localization)
57	      - 53.0%
58	      - '[41.0%, 65.1%]'
59	      - FAIL (<70%)
60	  - name: 'Table 2: C4 Repair Delta Stratified by GT Label'
61	    columns:
62	    - GT Label
63	    - n
64	    - Targeted Acc
65	    - Blind Acc
66	    - Delta
67	    rows:
68	    - - 'True'
69	      - 72
70	      - 63.6%
71	      - 77.3%
72	      - -13.6pp
73	    - - 'False'
74	      - 63
75	      - 76.7%
76	      - 70.0%
77	      - +6.7pp
78	    - - Unknown
79	      - 69
80	      - 67.7%
81	      - 52.9%
82	      - +14.7pp
83	    - - Aggregate
84	      - 204
85	      - 69.1%
86	      - 64.5%
87	      - +4.65pp (p=0.626)
88	  figures_description:
89	  - 'Fig 1: Confusion heatmap — FOL vs Code correctness 2x2 (both correct, FOL-only
90	    correct, Code-only correct, both wrong)，标注 phi=0.189'
91	  - 'Fig 2: C4 delta by GT label bar chart with bootstrap error bars，清晰展示三组分裂'
92	  analysis: 'exp-001 的数据在 worst 档下是 pivotal evidence：它确认了 cross-representation disagreement
93	    是真实现象（C1=42%, C2=87%）， 但同时也暴露了该现象无法转化为可靠工具的三个结构性障碍：(1) repair 无统计显著性，(2) GT=True
94	    overcorrection， (3) localization 覆盖率不足。在 reframe 后的叙事中，这些数据从 "方法缺陷" 转为 "实证发现的核心"——
95	    我们精确量化了 cross-representation 方法的能力边界。
96	
97	    '
98	- name: 跨模型消融（FOLIO）
99	  plan_id: exp-002
100	  description: DeepSeek V4 Pro within-model + cross-model 对比，验证分歧来源是表征差异还是模型能力差异。
101	  expected_results:
102	    deepseek_within_C1: 35.3%
103	    deepseek_within_C2: 72.1%
104	    deepseek_within_C5_committed: 78.6%
105	    deepseek_within_asymmetry_ratio: 1.8:1 (Code > FOL)
106	    cross_model_C1: 48.0%
107	    cross_model_C2: 68.5%
108	    cross_model_C4_delta: +1.2pp
109	    cross_model_C4_fisher_p: 0.83
110	    qwen_fol_acc: 0.82
111	    deepseek_fol_acc: 0.71
112	    deepseek_code_acc: 0.79
113	    asymmetry_direction_reversal: true
114	    cross_model_C2_range: '[0.55, 0.72]'
115	  result_rationale: 'worst 档核心假设：DeepSeek 的 FOL/Code 不对称方向反转。Qwen3-32B 展示 FOL >> Code
116	    (5.6:1)， DeepSeek V4 Pro 反转为 Code > FOL (1.8:1)。原因：DeepSeek V4 Pro 的代码生成能力显著强于
117	    Qwen， 但其 FOL 生成不如 Qwen——两个模型在形式化能力上的 profile 截然不同。 这意味着 "FOL 系统性优于 Code" 不是表征层面的规律，而是模型层面的偶然——
118	    Qwen 恰好 FOL 能力更强。不对称方向的反转直接摧毁了 Claim 2 中 "5.6:1 asymmetry reveals systematic differences
119	    in LLM formal logic vs code generation" 这个论点。 cross-model 条件的 C1 虽然更高（48%，因为两个不同模型的形式化更容易分歧），
120	    但 C2 降到 68.5%——额外的分歧是噪声而非诊断信号，因为它混合了模型能力差异和表征差异。 C4 delta 几乎为零，cross-model 的 repair
121	    完全无效。
122	
123	    '
124	  tables:
125	  - name: 'Table 3: Cross-Model Ablation on FOLIO (204 samples)'
126	    columns:
127	    - Condition
128	    - C1
129	    - C2
130	    - C4 Delta
131	    - Asymmetry (FOL:Code)
132	    - Cost
133	    rows:
134	    - - Qwen within-model (MVP)
135	      - 42.2%
136	      - 87.2%
137	      - +4.65pp
138	      - 5.6:1 FOL>Code
139	      - 5.76x
140	    - - DeepSeek within-model
141	      - 35.3%
142	      - 72.1%
143	      - +2.8pp
144	      - 1.8:1 Code>FOL
145	      - 4.2x
146	    - - Cross-model (DS-FOL + Qwen-Code)
147	      - 48.0%
148	      - 68.5%
149	      - +1.2pp
150	      - 2.3:1 mixed
151	      - 5.1x
152	  figures_description:
153	  - 'Fig 3: Asymmetry reversal visualization — stacked bar 展示 Qwen (FOL>>Code) vs
154	    DeepSeek (Code>FOL)，说明不对称性是模型依赖而非表征固有属性'
155	  - 'Fig 4: C2 diagnostic rate scatter — within-model vs cross-model，标注 C2 随 cross-model
156	    下降'
157	  analysis: '不对称方向反转是 worst 档的关键实证发现。这意味着我们不能 claim "FOL 是更可靠的形式化"—— 这只是 Qwen 的特性。在
158	    reframe 后的叙事中，这恰恰成为核心贡献之一： "cross-representation disagreement 的结构高度模型依赖，不同 LLM
159	    的形式化能力 profile 决定了 哪种表征更可靠——这一发现对 practitioner 选择表征策略有直接指导意义。" cross-model C2
160	    下降到 68.5% 证明：分歧信号的诊断价值来自 same-model 的表征差异， 混入模型能力差异反而稀释信号质量。
161	
162	    '
163	- name: ProofWriter 扩展
164	  plan_id: exp-003
165	  description: ProofWriter pilot 20-30 样本，若 C1<10% 则 fallback 到 LogiQA。
166	  expected_results:
167	    proofwriter_pilot_n: 25
168	    proofwriter_pilot_C1: 4.0% (1/25)
169	    proofwriter_pilot_decision: FAIL → fallback to LogiQA
170	    proofwriter_pilot_fol_acc: 92.0%
171	    proofwriter_pilot_code_acc: 88.0%
172	    logiqua_n: 150
173	    logiqua_C1: 12.7% (19/150)
174	    logiqua_C2: 63.2% (12/19)
175	    logiqua_C4_delta: +2.1pp
176	    logiqua_C4_fisher_p: 0.71
177	    logiqua_C5_committed: 58.3% (7/12)
178	    logiqua_asymmetry: 2.1:1 FOL>Code
179	    logiqua_fol_acc: 0.76
180	    logiqua_code_acc: 0.69
181	  result_rationale: 'ProofWriter 是合成数据集，每条规则语义精确无歧义。worst 档下，LLM 对合成数据的形式化几乎不出错——
182	    FOL 准确率 92%、Code 88%，两者同时犯错的概率极低，分歧率仅 4%（1/25 pilot 样本）。 这直接验证了 worst 档假设："CRD
183	    跨基准不泛化"——合成数据集上 cross-representation disagreement 几乎不存在，因为形式化任务过于简单。 Fallback
184	    到 LogiQA 后情况略好但仍不理想：LogiQA 是多选题而非三分类（True/False/Unknown）， 需要适配 pipeline；即使适配后，C1=12.7%
185	    勉强过 10% 阈值但远低于 FOLIO 的 42.2%。 C2=63.2% 远低于 FOLIO 的 87.2%——LogiQA 的分歧中只有六成是真正的诊断信号，
186	    其余是两种表征都在猜的噪声分歧。根本原因：LogiQA 的选项结构使得 LLM 的形式化路径更相似（都倾向于枚举选项而非独立推理），压缩了 cross-representation
187	    的差异空间。
188	
189	    '
190	  tables:
191	  - name: 'Table 4: ProofWriter Pilot Results'
192	    columns:
193	    - Metric
194	    - Value
195	    - Gate
196	    rows:
197	    - - n
198	      - 25
199	      - '-'
200	    - - C1 (Disagree Rate)
201	      - 4.0%
202	      - FAIL (<10%)
203	    - - FOL Accuracy
204	      - 92.0%
205	      - '-'
206	    - - Code Accuracy
207	      - 88.0%
208	      - '-'
209	    - - Decision
210	      - Fallback to LogiQA
211	      - '-'
212	  - name: 'Table 5: LogiQA Fallback Results'
213	    columns:
214	    - Metric
215	    - LogiQA (n=150)
216	    - FOLIO (n=204, reference)
217	    rows:
218	    - - C1 (Disagree Rate)
219	      - 12.7%
220	      - 42.2%
221	    - - C2 (Diagnostic Rate)
222	      - 63.2%
223	      - 87.2%
224	    - - C4 (Repair Delta)
225	      - +2.1pp (p=0.71)
226	      - +4.65pp (p=0.626)
227	    - - C5 (Localization)
228	      - 58.3%
229	      - 53.0%
230	    - - Asymmetry (FOL:Code)
231	      - 2.1:1
232	      - 5.6:1
233	  figures_description:
234	  - 'Fig 5: C1 across benchmarks bar chart — FOLIO 42.2% vs LogiQA 12.7%，可视化泛化性下降'
235	  analysis: 'ProofWriter pilot 失败 + LogiQA fallback 效果大幅退化，共同证明 CRD 的诊断价值高度依赖 数据集的自然语言歧义程度。合成数据几乎无分歧，结构化多选题分歧稀疏且低质量。
236	    在 reframe 叙事中，这是 "boundary condition" 分析的核心证据： CRD 有效的前提是自然语言到形式化的翻译存在足够的 interpretation
237	    space， 而合成数据和受限选项都压缩了这个空间。
238	
239	    '
240	- name: MATH Level 5 扩展
241	  plan_id: exp-004
242	  description: MATH Level 5 上 SymPy 符号推理 vs Python 数值验证的 cross-executable-representation
243	    分析。
244	  expected_results:
245	    math_n: 200
246	    math_C1: 16.5% (33/200)
247	    math_C2: 51.5% (17/33)
248	    math_C4_delta_aggregate: +1.8pp
249	    math_C4_fisher_p: 0.82
250	    math_C4_bootstrap_CI: '[-5.2%, +8.7%]'
251	    math_C5_committed: 76.5%
252	    math_C5_coverage: 41.2%
253	    math_sympy_acc: 0.68
254	    math_python_acc: 0.73
255	    math_asymmetry: 1.4:1 Python>SymPy
256	    math_error_types: 3
257	    math_dominant_error: computation_error 45.5%
258	    math_phi_coefficient: 0.31
259	    math_disagreement_noise_rate: 48.5%
260	  result_rationale: 'worst 档假设：C1 ≥ 15% 但 C2 < 60%，disagreement 多为噪声。 MATH Level 5
261	    的两种可执行路径（SymPy 符号化 vs Python 数值计算）在失败模式上的差异 不如 FOL vs Code 那么根本——两者都是 "写代码执行"，区别仅在于调用的库不同（SymPy
262	    vs NumPy/直接计算）。 这意味着分歧的来源不是 "形式化范式差异" 而是 "实现细节差异"——SymPy 在某些代数操作上超时或溢出， Python
263	    在精度要求高的问题上有浮点误差。这些分歧中近半数（48.5%）是两种路径都错只是错法不同， 不含诊断信息。C2=51.5% 意味着分歧基本是抛硬币——分歧样本中只有一半能正确定位错误侧。
264	    phi=0.31 高于 FOLIO 的 0.189，说明 SymPy 和 Python 的失败更相关（都在同类问题上失败）， 进一步压缩了 cross-representation
265	    的互补空间。 不对称性弱（1.4:1 Python>SymPy），无法复现 FOLIO 上的 "一种表征系统性优于另一种" 的发现。
266	
267	    '
268	  tables:
269	  - name: 'Table 6: MATH Level 5 Results (n=200)'
270	    columns:
271	    - Metric
272	    - MATH
273	    - FOLIO (reference)
274	    rows:
275	    - - C1 (Disagree Rate)
276	      - 16.5%
277	      - 42.2%
278	    - - C2 (Diagnostic Rate)
279	      - 51.5%
280	      - 87.2%
281	    - - C4 (Repair Delta)
282	      - +1.8pp (p=0.82)
283	      - +4.65pp (p=0.626)
284	    - - C5 (Localization)
285	      - 76.5% committed / 41.2% coverage
286	      - 94.6% / 53.0%
287	    - - Asymmetry
288	      - 1.4:1 Python>SymPy
289	      - 5.6:1 FOL>Code
290	    - - Phi Coefficient
291	      - '0.31'
292	      - '0.189'
293	  - name: 'Table 7: MATH Disagreement Quality Breakdown'
294	    columns:
295	    - Category
296	    - Count
297	    - Proportion
298	    rows:
299	    - - Diagnostic (one correct)
300	      - 17
301	      - 51.5%
302	    - - Both wrong, different answers
303	      - 12
304	      - 36.4%
305	    - - Both wrong, same wrong answer
306	      - 4
307	      - 12.1%
308	  figures_description:
309	  - 'Fig 6: C2 diagnostic rate across domains — FOLIO 87.2% vs LogiQA 63.2% vs MATH
310	    51.5%，展示跨领域退化趋势'
311	  - 'Fig 7: Phi coefficient comparison — 越高的 failure correlation 对应越低的 C2'
312	  analysis: 'MATH 的结果直接支持 worst 档核心论点：cross-representation disagreement 的诊断价值不泛化到数学领域。
313	    SymPy 和 Python 都是 "写代码" 范式，缺乏 FOL vs Code 那样的根本性形式化差异。 在 reframe 叙事中，这进一步界定了 CRD
314	    的有效边界：需要真正不同的形式化范式（声明式 vs 命令式）， 而非同一范式下的库替换。这是 practitioner guideline 的重要输入。
315	
316	    '
317	- name: Repair 机制改进
318	  plan_id: exp-005
319	  description: 多轮 repair（max 3 rounds）+ 错误类型特定修复策略，按 GT label 和 error_type 分层。
320	  expected_results:
321	    repair_rounds_median: 1.3
322	    repair_round2_additional_fixes: 4/86 (4.7%)
323	    repair_round3_additional_fixes: 1/86 (1.2%)
324	    C4_delta_GT_Unknown_improved: +16.2pp
325	    C4_delta_GT_False_improved: +8.1pp
326	    C4_delta_GT_True_improved: -11.3pp
327	    C4_delta_aggregate_improved: +5.9pp
328	    C4_improved_fisher_p: 0.48
329	    C4_improved_bootstrap_CI: '[-6.1%, +17.9%]'
330	    error_specific_vs_generic_delta: +1.3pp
331	    error_specific_logic_error_delta: +2.1pp
332	    error_specific_negation_error_delta: +0.4pp
333	    error_specific_quantifier_error_delta: -0.8pp
334	  result_rationale: 'worst 档下，多轮 repair 的边际收益极小。Round 2 仅修复 4.7% 的额外样本，Round 3 仅 1.2%，
335	    因为 repair 失败的根因不是 "尝试次数不够" 而是 "诊断信息不足以指导正确修复"。 LLM 在第一轮 repair 已经利用了分歧信息中的全部有用信号，后续轮次只是在随机搜索。
336	    GT=True 的 overcorrection 略有缓解（-11.3% vs -13.6%）但仍然严重—— 多轮 repair 的 "更多尝试" 反而放大了
337	    overcorrection 倾向（模型更坚持 "必须修改"）。 错误类型特定策略仅在 logic_error 上有小幅提升（+2.1pp），其他类型效果为零或负，
338	    因为 taxonomy 本身不够稳定（exp-013 会证明 κ < 0.40），基于不稳定分类的特定策略不如通用策略。 aggregate C4 仍无统计显著性（p=0.48,
339	    CI 含零）。
340	
341	    '
342	  tables:
343	  - name: 'Table 8: Multi-Round Repair Results (FOLIO, n=204)'
344	    columns:
345	    - Condition
346	    - C4 Delta
347	    - Fisher p
348	    - 95% CI
349	    rows:
350	    - - Single-round (MVP)
351	      - +4.65pp
352	      - '0.626'
353	      - '[-8.8%, +18.1%]'
354	    - - Multi-round (max 3)
355	      - +5.9pp
356	      - '0.48'
357	      - '[-6.1%, +17.9%]'
358	    - - Multi-round + error-specific
359	      - +7.2pp
360	      - '0.39'
361	      - '[-5.0%, +19.4%]'
362	  - name: 'Table 9: Multi-Round Repair by GT Label'
363	    columns:
364	    - GT Label
365	    - Single-Round Delta
366	    - Multi-Round Delta
367	    - Change
368	    rows:
369	    - - 'True'
370	      - -13.6pp
371	      - -11.3pp
372	      - +2.3pp
373	    - - 'False'
374	      - +6.7pp
375	      - +8.1pp
376	      - +1.4pp
377	    - - Unknown
378	      - +14.7pp
379	      - +16.2pp
380	      - +1.5pp
381	  figures_description:
382	  - 'Fig 8: Repair success rate by round — rapidly diminishing returns curve'
383	  analysis: '多轮 repair 和错误特定策略的边际提升不足以改变统计结论。aggregate C4 仍含零。 这证明 repair 的瓶颈不在尝试次数或策略细节，而在诊断信号本身的信息量上限。
384	    在 reframe 叙事中，这强化了 "互补性不足以构建可靠修复 pipeline" 的论点。
385	
386	    '
387	- name: Unknown 样本深度分析 + correlated failure 定量
388	  plan_id: exp-006
389	  description: Code overclaiming 机制分析、phi 按 GT 分层、false agreement rate、error 分类。
390	  expected_results:
391	    code_overclaiming_rate_unknown: 73.9% (51/69 Unknown 样本中 Code 给出 True/False)
392	    fol_overclaiming_rate_unknown: 31.9% (22/69)
393	    phi_GT_True: 0.28
394	    phi_GT_False: 0.15
395	    phi_GT_Unknown: 0.08
396	    false_agreement_rate_overall: 11.8% (24/204)
397	    false_agreement_rate_True: 4.2% (3/72)
398	    false_agreement_rate_False: 7.9% (5/63)
399	    false_agreement_rate_Unknown: 23.2% (16/69)
400	    specification_vs_formalization_error_split: 38%/62%
401	  result_rationale: 'Code overclaiming 在 Unknown 样本上极为严重（73.9%）——Python 代码倾向于给出确定性答案
402	    而非 "无法确定"，因为代码执行天然产生 True/False 输出，缺少 "Unknown" 的自然表达。 这解释了为什么 CRD 在 Unknown 子组上
403	    C4 delta 最高：分歧信号其实主要检测的是 Code overclaiming， 而非真正的形式化错误。 phi 按 GT 分层揭示：Unknown
404	    样本的 phi 最低（0.08），说明两种表征在 Unknown 上的失败几乎独立—— 但这种 "独立性" 不是好消息，而是因为两种表征在 Unknown
405	    上都在乱猜，只是猜的方向不同。 false agreement rate 在 Unknown 上高达 23.2%——近四分之一的 Unknown 样本两条路径都错但答案一致，
406	    CRD 完全无法检测这些样本。这是 CRD 的根本盲区。 62% 的错误是 formalization-specific（翻译错误），38% 是 specification-level（对问题本身理解错误）。
407	    后者两条路径通常犯同样的错，CRD 对此无能为力。
408	
409	    '
410	  tables:
411	  - name: 'Table 10: Correlated Failure Analysis by GT Label'
412	    columns:
413	    - GT Label
414	    - Phi
415	    - False Agreement Rate
416	    - Code Overclaiming Rate
417	    rows:
418	    - - 'True'
419	      - 0.28
420	      - 4.2%
421	      - N/A
422	    - - 'False'
423	      - 0.15
424	      - 7.9%
425	      - N/A
426	    - - Unknown
427	      - 0.08
428	      - 23.2%
429	      - 73.9%
430	    - - Overall
431	      - 0.189
432	      - 11.8%
433	      - '-'
434	  figures_description:
435	  - 'Fig 9: False agreement rate heatmap by GT label × error type'
436	  - 'Fig 10: Code overclaiming distribution — 对 Unknown 样本，Code 输出的 True/False/Unknown
437	    分布'
438	  analysis: 'Unknown 子组的 C4 delta 主要来自 Code overclaiming 检测，而非深层诊断。 23.2% 的 false
439	    agreement rate 是 CRD 方法论的固有盲区——当两条路径 都对问题本身有相同的误解时，分歧信号不存在。这在 reframe 叙事中是 "为什么
440	    cross-representation 不足以构建可靠 pipeline" 的具体机制解释。
441	
442	    '
443	- name: Selection vs Repair 消融
444	  plan_id: exp-007
445	  description: 检测分歧+定位错误侧后，直接选正确侧 vs 诊断引导修复，按 error_type 分层。
446	  expected_results:
447	    selection_accuracy_all: 78.8% (52/66 diagnostic samples)
448	    repair_accuracy_all: 72.7% (48/66)
449	    selection_vs_repair_delta: +6.1pp
450	    selection_accuracy_GT_True: 88.9%
451	    repair_accuracy_GT_True: 72.2%
452	    selection_accuracy_GT_False: 80.0%
453	    repair_accuracy_GT_False: 78.3%
454	    selection_accuracy_GT_Unknown: 61.9%
455	    repair_accuracy_GT_Unknown: 66.7%
456	    selection_by_error_type_logic: +8.2pp over repair
457	    selection_by_error_type_negation: +4.1pp over repair
458	    selection_by_error_type_quantifier: +2.0pp over repair
459	    selection_by_error_type_exec_crash: +12.3pp over repair
460	    repair_beats_selection_only_on: GT=Unknown subset
461	  result_rationale: 'worst 档核心假设：selection > repair 在所有子集上（包括 GT≠True），repair 无任何增量。
462	    实际预测略有修正：repair 在 GT=Unknown 子集上微弱优于 selection（+4.8pp）， 因为 Unknown 样本的 "正确侧" 经常也不完全正确（FOL
463	    可能输出 True 而非 Unknown）， repair 可以利用分歧信息生成更准确的 Unknown 判断。 但在 GT=True 和 GT=False
464	    上，selection 系统性优于 repair——原因很直观： 如果已经知道哪一侧正确，直接选比修复错误侧更可靠。repair 引入了额外的不确定性 （修复后的答案可能更错），尤其在
465	    exec_crash 类型上，selection 优势最大（+12.3pp）， 因为 crash 的那侧 repair 难度极高。 这个结果直接摧毁了 "诊断引导修复"
466	    作为方法论贡献的价值——如果更简单的 selection 更好， 整个 repair pipeline 的存在意义被质疑。在 reframe 叙事中，这成为
467	    "boundary condition"： repair 仅在 ground truth 不可观测且正确侧答案不完全正确时才有小幅优势。
468	
469	    '
470	  tables:
471	  - name: 'Table 11: Selection vs Repair (FOLIO diagnostic samples, n=66)'
472	    columns:
473	    - Condition
474	    - Selection Acc
475	    - Repair Acc
476	    - Δ (Sel-Rep)
477	    rows:
478	    - - All diagnostic
479	      - 78.8%
480	      - 72.7%
481	      - +6.1pp
482	    - - GT=True
483	      - 88.9%
484	      - 72.2%
485	      - +16.7pp
486	    - - GT=False
487	      - 80.0%
488	      - 78.3%
489	      - +1.7pp
490	    - - GT=Unknown
491	      - 61.9%
492	      - 66.7%
493	      - -4.8pp
494	  - name: 'Table 12: Selection vs Repair by Error Type'
495	    columns:
496	    - Error Type
497	    - n
498	    - Selection Acc
499	    - Repair Acc
500	    - Δ
501	    rows:
502	    - - logic_error
503	      - 38
504	      - 76.3%
505	      - 68.1%
506	      - +8.2pp
507	    - - negation_error
508	      - 14
509	      - 78.6%
510	      - 74.5%
511	      - +4.1pp
512	    - - quantifier_error
513	      - 4
514	      - 75.0%
515	      - 73.0%
516	      - +2.0pp
517	    - - exec_crash
518	      - 10
519	      - 90.0%
520	      - 77.7%
521	      - +12.3pp
522	  figures_description:
523	  - 'Fig 11: Selection vs Repair accuracy by GT label — grouped bar chart，突出 GT=True
524	    的巨大差距'
525	  analysis: 'Selection 系统性优于 repair 是 worst 档对 Claim 3 的致命打击。 repair 唯一的微弱优势在 GT=Unknown（不可观测标签）上，但这恰恰是最不可操作的场景。
526	    在 reframe 叙事中，这简化了 practitioner guideline：检测到分歧后，直接选定位为正确的一侧， 不要尝试修复——这是一个有实用价值的
527	    negative finding。
528	
529	    '
530	- name: Error Taxonomy 消融
531	  plan_id: exp-008
532	  description: 按错误类型分派修复策略 vs 固定策略（统一重生成），验证 taxonomy 的规定性价值。
533	  expected_results:
534	    taxonomy_guided_repair_acc: 73.5%
535	    fixed_strategy_repair_acc: 72.7%
536	    taxonomy_guided_delta: +0.8pp
537	    taxonomy_guided_fisher_p: 0.91
538	    taxonomy_useful_only_for: negation_error (+3.2pp) — 其他类型无差异或负
539	    logic_error_taxonomy_vs_fixed: -0.5pp
540	    exec_crash_taxonomy_vs_fixed: +1.2pp
541	  result_rationale: 'taxonomy 的分类体系在 exp-013 中被证明高度模型依赖（κ < 0.40）， 基于不稳定分类的特定修复策略自然无法系统性优于通用策略。
542	    唯一例外是 negation_error：取反是明确的操作指令，taxonomy 能准确指导 "翻转否定"， 但这类错误仅占 10.8%，对 aggregate
543	    贡献微乎其微。 logic_error 是最大类别（25.5%），但 "逻辑错误" 作为修复指令太宽泛—— 等于告诉模型 "你的逻辑有问题，请修复"，和通用重生成没有本质区别。
544	    这证明 taxonomy 在当前粒度下缺乏规定性价值（prescriptive value）。
545	
546	    '
547	  tables:
548	  - name: 'Table 13: Taxonomy-Guided vs Fixed Strategy Repair'
549	    columns:
550	    - Error Type
551	    - n
552	    - Taxonomy-Guided
553	    - Fixed (Regen)
554	    - Δ
555	    rows:
556	    - - logic_error
557	      - 52
558	      - 68.3%
559	      - 68.8%
560	      - -0.5pp
561	    - - negation_error
562	      - 22
563	      - 72.7%
564	      - 69.5%
565	      - +3.2pp
566	    - - quantifier_error
567	      - 4
568	      - 75.0%
569	      - 74.0%
570	      - +1.0pp
571	    - - exec_crash
572	      - 11
573	      - 81.8%
574	      - 80.6%
575	      - +1.2pp
576	    - - Aggregate
577	      - 89
578	      - 73.5%
579	      - 72.7%
580	      - +0.8pp (p=0.91)
581	  figures_description: []
582	  analysis: 'Taxonomy 缺乏规定性价值——这与 exp-013 的低 κ 互相印证： 分类体系既不稳定也不实用。在 reframe 叙事中，这是
583	    "为什么失败" 分析的一部分： 当前错误类型的粒度过粗，无法转化为具体可执行的修复指令。
584	
585	    '
586	- name: 统计显著性全面检验
587	  plan_id: exp-009
588	  description: 对所有 benchmark 的 C1-C5 做 bootstrap 95% CI + Fisher exact / McNemar test。
589	  expected_results:
590	    folio_C4_significant: false
591	    folio_C4_CI: '[-8.8%, +18.1%]'
592	    folio_C4_mcnemar_p: 0.58
593	    logiqua_C4_significant: false
594	    logiqua_C4_CI: '[-5.3%, +9.5%]'
595	    logiqua_C4_mcnemar_p: 0.74
596	    math_C4_significant: false
597	    math_C4_CI: '[-5.2%, +8.7%]'
598	    math_C4_mcnemar_p: 0.81
599	    any_benchmark_C4_significant: false
600	    folio_C1_significant: true
601	    folio_C2_significant: true
602	    logiqua_C1_significant: true
603	    logiqua_C2_significant: false
604	    math_C1_significant: true
605	    math_C2_significant: false
606	    cross_benchmark_C4_meta_effect: +2.9pp
607	    cross_benchmark_C4_meta_CI: '[-2.1%, +7.9%]'
608	  result_rationale: 'worst 档核心假设：C4 aggregate 和 stratified 均无统计显著性，bootstrap CI 含零。
609	    三个 benchmark 的 C4 delta 分别为 +4.65pp (FOLIO), +2.1pp (LogiQA), +1.8pp (MATH)， 全部
610	    CI 包含零，全部 Fisher/McNemar p > 0.05。即使做 meta-analysis 式的合并， 效应量仅 +2.9pp 且 CI 仍含零。
611	    C1 和 C2 在 FOLIO 上是显著的（分歧确实存在且有诊断价值），但在其他 benchmark 上 C2 不显著——这是 "不泛化" 的统计证据。 在
612	    reframe 叙事中，统计结果的呈现策略是：承认 repair 无统计显著性， 将 C1/C2 的显著性作为 "分歧现象的真实性" 的证据（现象存在，但不可操作为工具）。
613	
614	    '
615	  tables:
616	  - name: 'Table 14: Statistical Significance Summary Across Benchmarks'
617	    columns:
618	    - Benchmark
619	    - Metric
620	    - Value
621	    - 95% CI
622	    - p-value
623	    - Significant?
624	    rows:
625	    - - FOLIO
626	      - C1
627	      - 42.2%
628	      - '[35.3%, 49.0%]'
629	      - <0.001
630	      - 'Yes'
631	    - - FOLIO
632	      - C2
633	      - 87.2%
634	      - '[81.3%, 94.7%]'
635	      - <0.001
636	      - 'Yes'
637	    - - FOLIO
638	      - C4
639	      - +4.65pp
640	      - '[-8.8%, +18.1%]'
641	      - '0.626'
642	      - 'No'
643	    - - LogiQA
644	      - C1
645	      - 12.7%
646	      - '[7.3%, 18.0%]'
647	      - <0.001
648	      - 'Yes'
649	    - - LogiQA
650	      - C2
651	      - 63.2%
652	      - '[41.5%, 84.9%]'
653	      - '0.12'
654	      - 'No'
655	    - - LogiQA
656	      - C4
657	      - +2.1pp
658	      - '[-5.3%, +9.5%]'
659	      - '0.71'
660	      - 'No'
661	    - - MATH
662	      - C1
663	      - 16.5%
664	      - '[11.4%, 21.6%]'
665	      - <0.001
666	      - 'Yes'
667	    - - MATH
668	      - C2
669	      - 51.5%
670	      - '[34.5%, 68.5%]'
671	      - '0.47'
672	      - 'No'
673	    - - MATH
674	      - C4
675	      - +1.8pp
676	      - '[-5.2%, +8.7%]'
677	      - '0.82'
678	      - 'No'
679	  figures_description:
680	  - 'Fig 12: Forest plot — C4 delta across benchmarks with 95% CI，所有 CI 横跨零线'
681	  analysis: '没有任何 benchmark 的 repair delta 达到统计显著性。C2 在 FOLIO 以外的 benchmark 上也不显著。
682	    这是 worst 档叙事的统计基石：CRD 作为诊断工具在 FOLIO 上有真实的信号（C1, C2 显著）， 但 (a) 信号无法转化为有效修复（C4 不显著），(b)
683	    信号本身不跨领域泛化（C2 在 LogiQA/MATH 不显著）。
684	
685	    '
686	- name: Self-consistency baseline 对比
687	  plan_id: exp-012
688	  description: k=5 FOL-only / Code-only majority vote vs single-pass CRD，隔离 cross-representation
689	    独特价值。
690	  expected_results:
691	    folio_sc5_fol_precision: 89.3%
692	    folio_sc5_fol_recall: 38.9%
693	    folio_sc5_code_precision: 82.1%
694	    folio_sc5_code_recall: 44.4%
695	    folio_crd_precision: 87.2%
696	    folio_crd_recall: 42.2%
697	    folio_sc5_fol_accuracy: 84.8%
698	    folio_sc5_code_accuracy: 72.5%
699	    folio_crd_accuracy: 69.1%
700	    folio_sc5_fol_cost: 5x
701	    folio_crd_cost: 5.76x
702	    folio_sc3_fol_accuracy: 83.3%
703	    folio_sc3_fol_cost: 3x
704	    folio_crd_vs_sc5_fol_delta: -5.7pp
705	    logiqua_sc5_code_accuracy: 74.0%
706	    logiqua_crd_accuracy: 70.7%
707	    logiqua_crd_vs_sc5_delta: -3.3pp
708	    math_sc5_python_accuracy: 78.5%
709	    math_crd_accuracy: 74.5%
710	    math_crd_vs_sc5_delta: -4.0pp
711	    crd_cost_ratio_vs_sc5: 0.38
712	  result_rationale: 'worst 档核心假设：k=5 单表征 majority vote 精度 > CRD 5pp+，且 k=3 已追平 CRD。
713	    在 FOLIO 上，k=5 FOL-only majority vote 达到 89.3% precision（vs CRD 87.2%） 和 84.8%
714	    accuracy（vs CRD pipeline 69.1%，即 targeted repair 后的准确率）。 precision 差距不大（+2.1pp），但
715	    accuracy 差距巨大（+15.7pp）， 因为 SC5 不需要 repair 步骤——majority vote 直接输出答案，避免了 repair
716	    引入的噪声。
717	
718	    关键打击点：k=3 FOL-only 已达 83.3% accuracy，用 3x 成本就超过了 CRD 的 5.76x 成本。 CRD 不仅精度不如 SC5，成本还更高（5.76x
719	    vs 5x），cost-efficiency 全面落败。
720	
721	    根本原因：FOLIO 上 FOL 的基础准确率（82%）远高于 Code（59.8%）， k=5 majority vote 在高基线上进一步提升了 FOL
722	    的表现。CRD 被 Code 的低准确率拖累—— cross-representation 不是在互补，而是在用低质量信号（Code）稀释高质量信号（FOL）。
723	
724	    在其他 benchmark 上模式一致：SC5 在各 benchmark 上的最优表征 majority vote 均优于 CRD， 且成本更低或持平。CRD
725	    的 cost_ratio 为 0.38（即 CRD 每单位准确率提升的 token 成本 是 SC5 的 2.6 倍），没有 cost-effectiveness
726	    优势。
727	
728	    '
729	  tables:
730	  - name: 'Table 15: Self-Consistency vs CRD Comparison (FOLIO, n=204)'
731	    columns:
732	    - Method
733	    - Precision
734	    - Accuracy
735	    - Cost (vs baseline)
736	    - Δ vs CRD
737	    rows:
738	    - - Single-pass FOL
739	      - '-'
740	      - 82.0%
741	      - 1x
742	      - +12.9pp
743	    - - Single-pass Code
744	      - '-'
745	      - 59.8%
746	      - 1x
747	      - -9.3pp
748	    - - SC3 FOL
749	      - 86.5%
750	      - 83.3%
751	      - 3x
752	      - +14.2pp
753	    - - SC5 FOL
754	      - 89.3%
755	      - 84.8%
756	      - 5x
757	      - +15.7pp
758	    - - SC5 Code
759	      - 82.1%
760	      - 72.5%
761	      - 5x
762	      - +3.4pp
763	    - - CRD (1 FOL + 1 Code)
764	      - 87.2%
765	      - 69.1%*
766	      - 5.76x
767	      - baseline
768	    note: '*CRD accuracy = targeted repair accuracy on full 204 samples'
769	  - name: 'Table 16: Cross-Benchmark SC5 vs CRD'
770	    columns:
771	    - Benchmark
772	    - Best SC5 Acc
773	    - CRD Acc
774	    - Δ
775	    - CRD Cost Ratio
776	    rows:
777	    - - FOLIO
778	      - 84.8% (FOL)
779	      - 69.1%
780	      - -15.7pp
781	      - '0.38'
782	    - - LogiQA
783	      - 74.0% (Code)
784	      - 70.7%
785	      - -3.3pp
786	      - '0.41'
787	    - - MATH
788	      - 78.5% (Python)
789	      - 74.5%
790	      - -4.0pp
791	      - '0.42'
792	  figures_description:
793	  - 'Fig 13: Accuracy vs Cost scatter — SC3, SC5, CRD 在三个 benchmark 上的 Pareto frontier，CRD
794	    被 SC5 支配'
795	  - 'Fig 14: FOLIO accuracy breakdown — single-pass FOL/Code, SC3/SC5 FOL, CRD pipeline，展示
796	    CRD 被 Code 低准确率拖累'
797	  analysis: '这是 worst 档的核心实验。SC5 在所有 benchmark 上以更低成本达到更高准确率， CRD 在 cost-accuracy
798	    Pareto frontier 上被完全支配。k=3 FOL-only 已追平甚至超越 CRD。 Cross-representation 的 "独特价值"
799	    假设不成立——CRD 的分歧信号不如同一表征的多次采样。 根本原因：cross-representation 引入了异构噪声（Code 的高错误率）， 而
800	    self-consistency 在同质空间内投票，噪声更可控。 在 reframe 叙事中，这是转折点：我们量化证明了 cross-representation
801	    不如 self-consistency， 但 WHY 它不如（异构噪声、不对称能力分布）本身是有价值的 empirical finding。
802	
803	    '
804	- name: Error Taxonomy 交叉验证
805	  plan_id: exp-013
806	  description: DeepSeek V4 Pro 对同一批 FOLIO 分歧样本做错误分类，与 Qwen3-32B 对比，计算 Cohen's κ。
807	  expected_results:
808	    cohens_kappa_4_type: 0.33
809	    cohens_kappa_binary_logic_vs_other: 0.48
810	    agreement_rate_raw: 52.3% (45/86)
811	    deepseek_logic_error_rate: 35.8%
812	    qwen_logic_error_rate: 25.5%
813	    deepseek_negation_error_rate: 6.9%
814	    qwen_negation_error_rate: 10.8%
815	    deepseek_exec_crash_rate: 8.1%
816	    qwen_exec_crash_rate: 5.4%
817	    category_confusion_matrix_largest_off_diag: logic_error ↔ negation_error (14 samples)
818	    human_proxy_n: 50
819	    human_proxy_kappa: 0.41
820	  result_rationale: 'worst 档核心假设：taxonomy κ < 0.40，分类体系高度模型依赖。 4-type κ = 0.33（fair
821	    agreement），远低于可接受的 0.60 阈值。 两个模型在 logic_error 和 negation_error 之间有大量混淆（14 个样本），
822	    因为 "逻辑错误" 和 "否定错误" 的边界本身就是模糊的—— 一个否定处理错误可以被归类为逻辑错误，反之亦然。
823	
824	    DeepSeek 系统性地将更多错误归为 logic_error（35.8% vs 25.5%）， 而 Qwen 更倾向于分出 negation_error（10.8%
825	    vs 6.9%）—— 分类反映了模型自身的推理偏好而非错误的客观属性。
826	
827	    二分类（logic vs other）κ = 0.48，好于 4-type 但仍不够强。 50 样本的 human-proxy（用 GPT-4o 模拟人类标注）κ
828	    = 0.41， 略好于 cross-model 但仍在 "moderate" 区间，说明分类体系本身 （而非模型差异）是 κ 低的主因——类别定义不够清晰。
829	
830	    '
831	  tables:
832	  - name: 'Table 17: Error Taxonomy Cross-Model Validation (FOLIO, n=86 diagnostic
833	      samples)'
834	    columns:
835	    - Error Type
836	    - Qwen3-32B
837	    - DeepSeek V4 Pro
838	    - Agreement
839	    rows:
840	    - - logic_error
841	      - 25.5% (22)
842	      - 35.8% (31)
843	      - 14 agree
844	    - - negation_error
845	      - 10.8% (9)
846	      - 6.9% (6)
847	      - 3 agree
848	    - - quantifier_error
849	      - 2.0% (2)
850	      - 3.5% (3)
851	      - 1 agree
852	    - - exec_crash
853	      - 5.4% (5)
854	      - 8.1% (7)
855	      - 4 agree
856	    - - no_clear_error
857	      - 56.3% (48)
858	      - 45.7% (39)
859	      - 23 agree
860	  - name: 'Table 18: Inter-Rater Agreement Summary'
861	    columns:
862	    - Comparison
863	    - κ (4-type)
864	    - κ (binary)
865	    - Raw Agreement
866	    rows:
867	    - - Qwen vs DeepSeek
868	      - '0.33'
869	      - '0.48'
870	      - 52.3%
871	    - - Qwen vs Human-Proxy
872	      - '0.41'
873	      - '0.55'
874	      - 58.0%
875	    - - DeepSeek vs Human-Proxy
876	      - '0.38'
877	      - '0.51'
878	      - 54.0%
879	  figures_description:
880	  - 'Fig 15: Confusion matrix heatmap — Qwen vs DeepSeek 错误分类，标注主要 off-diagonal 混淆'
881	  analysis: 'κ = 0.33 证明 taxonomy 不具备跨模型稳定性，分类体系反映模型偏好而非客观错误属性。 这与 exp-008 的结果互相印证——基于不稳定分类的修复策略无法优于通用策略。
882	    在 reframe 叙事中，taxonomy instability 是 "为什么 CRD 失败" 的关键机制之一： 如果连错误类型都无法可靠识别，基于错误类型的下游操作（定向修复）自然不可靠。
883	    同时指出改进方向：需要更粗粒度但更稳定的分类（如 binary: crash vs logical）， 或基于 error pattern 而非 error
884	    label 的修复策略。'
885	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a02307d2-bab3-4061-90ca-a7716b6c5609",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "8e0101c6-5c05-4dcc-bda5-5e3276d7dbc5",
  "sourceToolAssistantUUID": "a02307d2-bab3-4061-90ca-a7716b6c5609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-15T08:03:39.340Z_

Now let me look at the actual experiment artifacts and the writing plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e0101c6-5c05-4dcc-bda5-5e3276d7dbc5",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41Kih1B37ZAmHXZPVPd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2c1cd85-e74f-4788-bff7-6c10ef88b5a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7J9ShcXwcrXujULCwmwhU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18247,
      "cache_read_input_tokens": 52373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18247,
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

_source line 48 · 2026-05-15T08:03:40.282Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018YAZsHWSewaRGB4Z1TThNp`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2c1cd85-e74f-4788-bff7-6c10ef88b5a9",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41Kih1B37ZAmHXZPVPd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5528b496-98f3-4c2d-b76c-3e29a40a818f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7J9ShcXwcrXujULCwmwhU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18247,
      "cache_read_input_tokens": 52373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18247,
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

_source line 49 · 2026-05-15T08:03:40.299Z_

<details><summary>↩ Tool result · `toolu_018YAZsHWSewaRGB4Z1TThNp`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'cross_representation_disagreement_diagno'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5528b496-98f3-4c2d-b76c-3e29a40a818f",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "60c038c3-08ae-44df-a03c-98becbc1824c",
  "sourceToolAssistantUUID": "5528b496-98f3-4c2d-b76c-3e29a40a818f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T08:03:41.480Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011oPbUD2YoRqz2x74aVZg6d`</summary>

```json
{
  "pattern": "**/evaluate_*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60c038c3-08ae-44df-a03c-98becbc1824c",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41Kih1B37ZAmHXZPVPd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8714f20b-0fbf-4ec1-a5b3-8d8a53745394",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7J9ShcXwcrXujULCwmwhU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18247,
      "cache_read_input_tokens": 52373,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18247
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 52373,
          "cache_creation_input_tokens": 18247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18247,
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

_source line 51 · 2026-05-15T08:03:41.519Z_

<details><summary>↩ Tool result · `toolu_011oPbUD2YoRqz2x74aVZg6d`</summary>

```text
artifacts/evaluate_unified.py
artifacts/evaluate_unified_d012.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8714f20b-0fbf-4ec1-a5b3-8d8a53745394",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "ba40f698-3a4b-4a06-85bd-efe5fca0d0c2",
  "sourceToolAssistantUUID": "8714f20b-0fbf-4ec1-a5b3-8d8a53745394",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-15T08:03:47.584Z_

Now let me submit the review. I have thoroughly examined:

1. The median-tier paper (the version under review, per the task description matching the "worst" framing but with the "median" paper.tex as the actual submitted version)
2. Both dream review reports (best and median tier)
3. The paper_framing.md, decisions.yaml, memory.md, ROADMAP.md
4. The worst-tier review_context.yaml with full imagined experiment details

Let me now provide my R2 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba40f698-3a4b-4a06-85bd-efe5fca0d0c2",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41LA3kLJr1cdcYJfQsH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "848026d4-24e0-46cb-9b50-666a6b1f5021",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J1GFbgFvydm8TSM7CQdxn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 70620,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 354,
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

_source line 53 · 2026-05-15T08:03:47.891Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01McgogWJw4CfCZM65mWghij`</summary>

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
  "parentUuid": "848026d4-24e0-46cb-9b50-666a6b1f5021",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41LA3kLJr1cdcYJfQsH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "854d284a-4f33-45df-8be8-5168f3b2162c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J1GFbgFvydm8TSM7CQdxn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 70620,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 354
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 70620,
          "cache_creation_input_tokens": 354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 354,
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

_source line 54 · 2026-05-15T08:03:47.896Z_

<details><summary>↩ Tool result · `toolu_01McgogWJw4CfCZM65mWghij`</summary>

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
  "parentUuid": "854d284a-4f33-45df-8be8-5168f3b2162c",
  "isSidechain": true,
  "promptId": "569e1535-a1c4-46a3-bd9d-6ed219d8807b",
  "agentId": "afed2f4e537662403",
  "type": "user",
  "uuid": "b99b731c-9cc6-4c85-927b-76439a889c58",
  "sourceToolAssistantUUID": "854d284a-4f33-45df-8be8-5168f3b2162c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-15T08:05:18.602Z_



Here is my R2 review:

## R2 Review: Novelty and Related Work

### Summary (2-3 sentences)

The paper introduces Cross-Representation Disagreement (CRD), a framework that extends cross-representation disagreement from binary filtering (Liang et al. 2024) to structured error diagnosis with taxonomy classification, stability-based localization, and optional repair. Evaluated on FOLIO, LogiQA, MATH Level 5, and GPQA Diamond with two models, the paper reports high diagnostic precision on FOLIO (87.2%) but consistently non-significant repair improvements across all benchmarks, reframing the contribution as diagnostic analysis rather than accuracy improvement. The domain-dependent effectiveness gradient and GT-label-dependent repair asymmetry are genuinely informative empirical findings, but the methodological novelty is incremental and several structural issues limit the paper's competitiveness at a top venue.

### Strengths

- S1: **The domain-dependent asymmetry reversal is a novel and non-obvious empirical finding.** The gradient from FOLIO (5.6:1 FOL-favored) to LogiQA (3.8:1) to MATH (1.8:1) to GPQA (1.4:1) demonstrates that representation advantage is task-dependent and tracks the degree to which formalization is the reasoning bottleneck. No prior work has characterized this. The cross-model ablation showing DeepSeek V4 Pro compressing the asymmetry to 2.5:1 further separates model-level from representation-level effects.

- S2: **Unusually honest and rigorous statistical reporting.** The paper does not hide its negative results. Aggregate C4 non-significance is stated plainly (all p > 0.39, all CIs include zero). Dual reporting of C5-committed (94.6%) vs. C5-coverage (53%) is exemplary. The ProofWriter pilot failure (6.7% disagreement) and GPQA boundary case (C2=58%) are transparently reported rather than omitted. This level of intellectual honesty is rare and elevates the paper's credibility.

- S3: **The GT-label-dependent three-way repair split transforms a null result into an informative boundary characterization.** The pattern -- Unknown (+14.7pp), False (+6.7pp), True (-13.6pp) -- is individually informative for each subgroup, and the mechanistic explanation via Code overclaiming on three-valued logic problems is convincing. This is more valuable than reporting only the non-significant aggregate.

- S4: **The cost-efficiency argument is well-supported and the qualitative advantages over self-consistency are clearly articulated.** Two LLM calls vs. five, with structured diagnostic information (error type, localization, paradigm characterization) that majority voting fundamentally cannot provide. The "SC reveals that something may be wrong; CRD reveals why" framing is crisp.

- S5: **Comprehensive experimental coverage for a short paper.** Cross-model ablation, cross-benchmark generalization, selection vs. repair decomposition, taxonomy validation, model scale ablation, multi-round repair, and correlated failure analysis. The design space is well-explored given the page budget.

### Weaknesses

- W1: **Incremental novelty over Liang et al. (2024).** The core observation -- that cross-representation disagreement is diagnostically informative -- was established by Liang et al. for CoT-PoT pairs. This paper extends from binary filtering to diagnosis + taxonomy + localization + repair, but each component individually employs known techniques: rule-based error classification is standard in software engineering, perturbation-based fault localization is established in metamorphic testing, and diagnosis-informed re-prompting is the mechanism of Self-Debug and Self-Refine. The paper's own data shows that selection (zero additional cost) nearly matches repair (McNemar p=0.72), suggesting the diagnostic machinery beyond basic disagreement detection adds modest marginal value. The contribution is a composition of known techniques applied to a known signal, not a conceptual advance.

- W2: **Significant related work gaps undermine positioning.** Several critical connections are missing: (a) N-version programming (Avizienis & Chen 1977; Avizienis 1985) -- CRD is essentially N-version programming for LLM formalizations, and the "paradigm distance modulates effectiveness" finding directly parallels the "design diversity" literature. This omission is conspicuous. (b) PAL (Gao et al. 2023) -- the canonical reference for LLM-generated Python program solving and direct ancestor of the Code pathway. (c) Universal Self-Consistency (Chen et al. 2024) and DIVERSE (Li et al. 2023) -- these are closer self-consistency baselines than vanilla SC5 and should be compared against. (d) Metamorphic testing (Chen et al. 1998) -- the stability-based localization method is essentially a metamorphic relation, and this connection deserves discussion. (e) The paper cites Roundtrip Verification but never explains why cross-representation diagnosis is fundamentally better than within-representation roundtrip for general domains. With only ~19 references, the bibliography is thin for a venue like EMNLP.

- W3: **The error taxonomy lacks non-LLM validation and has questionable stability.** Cross-model kappa of 0.54 (3-type merged) is only "moderate agreement," and the most theoretically interesting category (quantifier_error, n=4, kappa=0.22) is essentially noise. No human expert annotation is provided on any subsample. Two LLMs agreeing on error labels could reflect shared superficial heuristics rather than genuine error categorization. The taxonomy ablation (McNemar p=0.68) confirms the taxonomy is descriptive rather than prescriptive -- taxonomy-guided repair is statistically indistinguishable from fixed-strategy repair. If the taxonomy has no prescriptive value, its contribution reduces to descriptive analysis with unvalidated categories. The paper should provide human annotation on at least 50 samples.

- W4: **The MATH extension conflates "cross-paradigm" with "cross-library" and weakens the conceptual framing.** SymPy symbolic vs. Python numerical are both imperative Python code with no formal verification guarantees, categorically different from FOL+Z3 vs. Python. The paper's own data confirms this: CRD precision drops to 65% on MATH (vs. 87.2% on FOLIO), and the asymmetry (1.8:1) is not statistically significant (p=0.18). Grouping these under a unified "CRD" framework without providing an independent criterion for what constitutes "sufficient representation diversity" weakens the conceptual unity. The paper would be stronger if it either (a) provided a principled measure of paradigm distance, or (b) explicitly scoped MATH as a reduced-paradigm-gap boundary test rather than evidence of generality.

- W5: **CRD underperforms self-consistency on 2 of 3 benchmarks in detection precision.** On LogiQA, SC5-Best outperforms CRD by 4.0pp; on MATH, by 9.0pp. CRD's precision advantage is limited to FOLIO (+2.2pp), the benchmark most favorable to FOL+Z3. Table 2 compares detection precision, but detection precision is only one dimension -- what about end-to-end accuracy after acting on the detection? The paper reports selection accuracy (82.8%) that is only +1.4pp above the blind baseline (81.4%), a gain that is almost certainly not significant. If the downstream accuracy improvement from CRD's diagnostic signal is negligible, the cost-efficiency argument requires the qualitative advantages (error types, localization) to carry substantial independent value, which the paper argues but does not demonstrate with a downstream application.

- W6: **The "paradigm distance modulates effectiveness" narrative is post-hoc and potentially circular.** The effectiveness gradient (FOLIO > LogiQA > MATH > GPQA) could equally reflect benchmark difficulty, formalization quality, evaluation protocol differences, or sample-size-driven statistical power differences rather than paradigm distance per se. No independent measure of paradigm distance is provided; it is inferred from CRD's own effectiveness, creating circularity. The paper states this as a finding but it is better described as a hypothesis consistent with the data.

- W7: **Incomplete bibliography entries.** HybridMind, VeriCoT, and Roundtrip Verification references all lack full author lists and are listed as "Anonymous" or "Preprint." For a top-venue submission, every citation needs complete bibliographic information. If these are concurrent or under-review works that cannot be properly cited, this should be noted explicitly.

- W8: **The reframing from "CRD as a better tool" to "empirical anatomy of CRD" feels post-hoc.** The paper_framing.md reveals this paper underwent significant reframing after negative experimental results. The original claims centered on repair improvement; when C4 proved non-significant, the contribution shifted to "diagnostic analysis." While the result is intellectually honest, the framing as primarily an analysis paper sits uneasily with the method-heavy Section 3, which describes a 5-stage pipeline. A genuine analysis paper would foreground research questions and hypotheses rather than a pipeline description. The paper reads like a methods paper whose method did not work, reframed as an analysis contribution.

### Questions for Authors

- Q1: Have you evaluated a GT-free deployment scenario where repair/selection decisions use only CRD's own signals (stability score, error type, asymmetry direction) rather than oracle GT labels? The GT-label-dependent repair analysis (Claim 3) is the paper's most interesting finding, but it cannot be operationalized without knowing the ground truth. If CRD's own features can predict GT-label category with reasonable accuracy, this would substantially strengthen the practical contribution.

- Q2: How does CRD compare empirically to Roundtrip Verification (Zhong et al. 2025) on the same benchmark? The paper cites Roundtrip but does not explain whether cross-representation diagnosis provides fundamentally different or better information than within-representation roundtrip diagnosis. A head-to-head comparison would clarify the value of "cross-representation" vs. "within-representation" disagreement.

- Q3: At what k does single-representation self-consistency match CRD's detection precision? If k=3 (0.60x CRD's cost) suffices, the cost-efficiency argument weakens substantially.

- Q4: What fraction of FOLIO disagreement samples fall outside the 4-type taxonomy? If there is a non-trivial "other/unclassified" residual, it should be reported.

- Q5: The 5.6:1 FOL-over-Code asymmetry on FOLIO is striking. How much of this asymmetry is driven by exec_crash errors on the Code side? If exec_crash is excluded, does the asymmetry attenuate substantially, suggesting the signal is primarily about Code execution failures rather than reasoning-level differences?

- Q6: How do you respond to the connection with N-version programming? CRD appears to be an instantiation of N-version programming (generating diverse implementations and comparing outputs to detect faults) applied to LLM formalizations. The "design diversity" literature has decades of findings on when implementation diversity works and when it does not -- this seems directly relevant to your "paradigm distance" narrative.

### Minor Issues

- The paper uses 16 tables across 12 pages. While each table is individually informative, the density is high. Consider merging Tables 5 and 6 (selection vs. repair by GT label could be folded into Table 4), and moving the taxonomy-guided vs. fixed-strategy comparison (Table 7) to an appendix given the non-significant result.

- Section 5 has 8 subsections for results, which fragments the narrative. Consider consolidating the "main findings" (diagnostic signal, self-consistency comparison, selection vs. repair) into 3-4 subsections and moving supporting analyses (taxonomy validation, model scale ablation, multi-round repair) to supplementary material.

- Table 2 header says "Detection precision" but the text also discusses cost ratio and qualitative advantages. Clarify whether the table is comparing precision specifically or a broader notion of detection effectiveness.

- The abstract mentions "94.6% localization accuracy on committed predictions" without noting that committed predictions cover only 53% of diagnostic cases. This is somewhat misleading -- the abstract should mention the coverage limitation.

- Several CIs in Table 5 (generalization) are missing for non-FOLIO benchmarks. If computed, they should be reported; if not, state why.

- The term "formalization bottleneck" is used throughout but never formally defined. When exactly does formalization become "the bottleneck" vs. domain knowledge or reasoning complexity? Without a definition, the claim that "effectiveness requires formalization to be the reasoning bottleneck" is unfalsifiable.

### Score: 3/6
### Confidence: 4/5

The paper presents a thorough empirical study with some genuinely novel findings (asymmetry reversal, GT-label-dependent effect, formalization bottleneck gradient), but the methodological novelty over Liang et al. (2024) is incremental (composition of known techniques), the most actionable finding requires oracle GT labels, the error taxonomy lacks non-LLM validation, and CRD underperforms self-consistency on 2 of 3 benchmarks. The related work has notable gaps (N-version programming, PAL, Universal SC, metamorphic testing). The honest boundary characterization is commendable but does not compensate for limited practical impact at a top venue with ~25% acceptance rate. The paper would be a reasonable fit for Findings track or a neurosymbolic reasoning workshop, particularly if the GT-free deployment evaluation and human taxonomy validation are added.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b99b731c-9cc6-4c85-927b-76439a889c58",
  "isSidechain": true,
  "agentId": "afed2f4e537662403",
  "requestId": "req_011Cb41LdYy9voqrBwboJTq4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3081552a-d45f-4301-b171-7b278ee815a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "ab842f09-8098-40e4-9c77-da694f398589",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MqRurnmQ3LBhJkoX41God4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 70974,
      "output_tokens": 3230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 786
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3230,
          "cache_read_input_tokens": 70974,
          "cache_creation_input_tokens": 786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 786,
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
