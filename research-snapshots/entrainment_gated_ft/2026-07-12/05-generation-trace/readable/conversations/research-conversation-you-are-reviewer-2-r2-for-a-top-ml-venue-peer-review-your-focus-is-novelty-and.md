# Research conversation: You are Reviewer 2 (R2) for a top ML venue peer review. Your focus is **Novelty and Related Work**. ## Paper Summary "Di

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a3242b380ec851971.jsonl`
- **Structured JSON:** [`1092777b8bbd0458aaa9.json`](../../sessions/10/1092777b8bbd0458aaa9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-14T00:56:41.978Z_

You are Reviewer 2 (R2) for a top ML venue peer review. Your focus is **Novelty and Related Work**.

## Paper Summary
"Discrete Mixed-Precision KV Cache Quantization via Constrained Multiple-Choice Knapsack" proposes per-head KV cache bit-width allocation formulated as a constrained Multiple-Choice Knapsack Problem (MCKP) over discrete bit-widths {2, 4, 8, 16}. Key elements:
- Distortion profiling: δ_h(b) = PPL(model; h→b) − PPL(model; FP16), measuring per-head quantization sensitivity
- MCKP formulation: minimize total distortion s.t. one bit-width per head, global bit budget, cardinality constraint ≤k heads at 2-bit
- The cardinality constraint is the key novelty: it regularizes the compounding effect (non-additive degradation when many heads simultaneously at extreme quantization)
- Solver runs in polynomial time via DP, <2 minutes for H≤1000 heads

## Claims
1. Per-head sensitivity heterogeneity: L0 heads exhibit 42-100× higher profiling delta across Qwen/Llama/Mistral
2. Constrained MCKP outperforms uniform: 12-27% PPL improvement at 4× compression
3. Cardinality constraint as effective heuristic (not principled regularization): broad sweet spot k∈[8,24]

## Related Work as Written
- KV cache compression: KVQuant (per-channel), KIVI (asymmetric K/V), RateQuant (continuous waterfilling, per-head), H₂O/ScissorHands/SnapKV (eviction-based), ARKV (per-layer quant + eviction)
- Mixed-precision quantization: GPTQ, AWQ for weights. Notes KV cache mixed-precision is less explored due to inference-time dynamic nature.
- Knapsack in ML: NAS, filter pruning. Claims first application to per-head KV cache bit-width with cardinality constraints.

## Key Results
- Qwen2.5-7B: MCKP PPL 11.23 vs uniform 15.45 (27% improvement) at 4×
- Llama-3.1-8B: 15% improvement, Mistral-7B: 12.1%
- Waterfilling comparison: MCKP 11.52 vs discretized waterfilling 14.23 (19.1% advantage)
- MCKP within 2% of brute-force oracle at 173× less compute
- Downstream: 62% MMLU recovery, 58% LongBench recovery
- At 2× compression, MCKP advantage is only 4.3%, paper acknowledges waterfilling may be competitive there

## Your Review Task
Evaluate **novelty** and **related work** critically. Address:

1. **Novelty assessment**:
   - Is the MCKP formulation genuinely novel? MCKP is a well-known optimization problem. The application to KV cache bit-width allocation is the novelty claim.
   - How incremental is this over RateQuant? RateQuant already does per-head allocation via rate-distortion; this paper changes the solver (continuous→discrete) and adds a constraint.
   - The cardinality constraint is acknowledged as an empirical heuristic, not principled. Does this weaken the contribution?
   - Is the "compounding effect" observation itself novel or previously known?

2. **Related work completeness**:
   - Are important baselines missing? (e.g., SqueezeLLM, QuIP, AQLM for weight quantization; any recent KV cache mixed-precision work)
   - Is the comparison with RateQuant fair? (using their distortion model projected to discrete, not their actual implementation)
   - ARKV comparison: paper mentions it but doesn't compare experimentally
   - Any concurrent/recent work on per-head KV cache quantization missing?

3. **Positioning**:
   - Does the paper clearly differentiate from RateQuant?
   - Is the contribution positioned correctly (system contribution vs theoretical contribution)?

4. **Significance**:
   - Would this change how practitioners do KV cache quantization?
   - Is the practical impact sufficient for a top venue?

Write a structured review with:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, with severity: major/minor)
- Questions for authors
- Score (1-6 scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept)
- Confidence (1-5)

Be rigorous. Top ML venue acceptance rate is ~25%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "0ac11c87-0fa4-4077-99a9-63fce293a9f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T00:56:41.984Z_

```json
{
  "parentUuid": "0ac11c87-0fa4-4077-99a9-63fce293a9f3",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
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
  "uuid": "be97f9f8-022c-44c5-b412-86f670ee37b9",
  "timestamp": "2026-05-14T00:56:41.984Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T00:56:45.264Z_



I'll start by reading the project's key files to understand the full paper and related work context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be97f9f8-022c-44c5-b412-86f670ee37b9",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1YxiP351s5iN3CCH2xd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4c67112-b968-40f2-a59e-99f16c369eb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Xo3u2oC6hTi2weed2af9d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6974,
      "cache_read_input_tokens": 8247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6974,
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

_source line 4 · 2026-05-14T00:56:46.497Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019buo3Rknrf81cUNWJcA5uR`</summary>

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
  "parentUuid": "f4c67112-b968-40f2-a59e-99f16c369eb9",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1YxiP351s5iN3CCH2xd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "999c753a-ece5-4efb-854e-cfabc0ac7de5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Xo3u2oC6hTi2weed2af9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6974,
      "cache_read_input_tokens": 8247,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6974
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 8247,
          "cache_creation_input_tokens": 6974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6974,
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

_source line 5 · 2026-05-14T00:56:46.501Z_

<details><summary>↩ Tool result · `toolu_019buo3Rknrf81cUNWJcA5uR`</summary>

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
  "parentUuid": "999c753a-ece5-4efb-854e-cfabc0ac7de5",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "f5f6049f-9588-436c-a5d9-0fd41bec65f2",
  "sourceToolAssistantUUID": "999c753a-ece5-4efb-854e-cfabc0ac7de5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T00:56:49.132Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01KRbUdVuVRm7R4Eg5QTYTyb`</summary>

```json
{
  "project": "ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5f6049f-9588-436c-a5d9-0fd41bec65f2",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Yy3t3hocsfgNEaQVxz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7dfdff2-5323-49bc-ab61-851e24b78b35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ih39s4RyLCvxdnLmNrmPa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
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

_source line 7 · 2026-05-14T00:56:49.199Z_

<details><summary>↩ Tool result · `toolu_01KRbUdVuVRm7R4Eg5QTYTyb`</summary>

```text
{"result":"# 项目 ratekv 概况\n\n## 实验状态 (21 个)\n\n- **exp_c_no2bit**: DONE (negative) — \n- **exp_c_constrained_mckp**: DONE (success) — \n- **exp_b_hires_quant**: DONE (negative) — \n- **exp_a_targeted_hybrid**: DONE (negative) — \n- **mvp_004**: DONE (negative) — \n- **p0_2_cliff_7B**: DONE (success) — \n- **p0_1_ppl_fast**: DONE (negative) — \n- **p0_2_cliff_1.5B**: DONE (success) — \n- **sanity_004**: DONE (success) — \n- **sanity_003**: DONE (failed) — \n- **sanity_002**: DONE (failed) — \n- **sanity_001**: DONE (failed) — \n- **mvp_003**: DONE (failed) — \n- **mvp_002**: DONE (failed) — \n- **mvp_001**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_e_hires_profile | — | — | — | — |\n\n## 待处理\n- budget_sweep（准备中）\n- ratequant_greedy_comparison（准备中）\n\n## 近期结论\n- **compounding_sweep_k10_12** (success): —\n- **compounding_sweep** (success): —\n  [compounding_sweep_results](/api/workspace-files/projects/ratekv/artifacts/compounding_sweep/data/compounding_sweep_results.csv)\n- **exp_d_no_l0_exclusion** (success): —\n\n## 趋势\n成功 7 / 负向 5 / 失败 6 / 共 18\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-37397: 无 GPU 信息\n\n## 告警\n- mvp_001: 训练失败 — unknown\n- sanity_001: 训练失败 — unknown\n- mvp_002: 训练失败 — unknown\n- sanity_002: 训练失败 — unknown\n- mvp_003: 训练失败 — unknown\n- sanity_003: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7dfdff2-5323-49bc-ab61-851e24b78b35",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "a462e29e-b7d7-41e8-a170-0e444e73375f",
  "sourceToolAssistantUUID": "c7dfdff2-5323-49bc-ab61-851e24b78b35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T00:56:50.143Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UyXT3mKhTCfuumVAM2QXq2`</summary>

```json
{
  "project": "ratekv",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a462e29e-b7d7-41e8-a170-0e444e73375f",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Yy3t3hocsfgNEaQVxz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89da8a12-b221-49a0-809a-487ec11089e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ih39s4RyLCvxdnLmNrmPa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
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

_source line 9 · 2026-05-14T00:56:50.153Z_

<details><summary>↩ Tool result · `toolu_01UyXT3mKhTCfuumVAM2QXq2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_e_hires_profile | — | — | — | — |\\n\\n## 待处理\\n- budget_sweep（准备中）\\n- ratequant_greedy_comparison（准备中）\\n\\n## 近期结论\\n- **compounding_sweep_k10_12** (success): —\\n- **compounding_sweep** (success): —\\n  [compounding_sweep_results](/api/workspace-files/projects/ratekv/artifacts/compounding_sweep/data/compounding_sweep_results.csv)\\n- **exp_d_no_l0_exclusion** (success): —\\n\\n## 趋势\\n成功 7 / 负向 5 / 失败 6 / 共 18\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-37397: 无 GPU 信息\\n\\n## 告警\\n- mvp_001: 训练失败 — unknown\\n- sanity_001: 训练失败 — unknown\\n- mvp_002: 训练失败 — unknown\\n- sanity_002: 训练失败 — unknown\\n- mvp_003: 训练失败 — unknown\\n- sanity_003: 训练失败 — unknown\\n\", \"total_chars\": 779, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89da8a12-b221-49a0-809a-487ec11089e9",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "403aec14-be19-4f1b-a802-44597e8e0b4d",
  "sourceToolAssistantUUID": "89da8a12-b221-49a0-809a-487ec11089e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T00:56:50.304Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012ujCXLUnxPVnfT4PHj7E7Q`</summary>

```json
{
  "project": "ratekv",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "403aec14-be19-4f1b-a802-44597e8e0b4d",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Yy3t3hocsfgNEaQVxz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2fe3265-2ae2-4093-bde7-662d3cbc6af3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ih39s4RyLCvxdnLmNrmPa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15221,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1449
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 15221,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1449,
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

_source line 11 · 2026-05-14T00:56:50.319Z_

<details><summary>↩ Tool result · `toolu_012ujCXLUnxPVnfT4PHj7E7Q`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'ratekv'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2fe3265-2ae2-4093-bde7-662d3cbc6af3",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "11f17eaa-bc80-42cd-abca-eac4222353f1",
  "sourceToolAssistantUUID": "c2fe3265-2ae2-4093-bde7-662d3cbc6af3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T00:56:53.926Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01W1msxsh3KtKWNwSny3zSwo`</summary>

```json
{
  "project": "ratekv",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11f17eaa-bc80-42cd-abca-eac4222353f1",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1YyL7rY8zSa2gSppDz6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a59a5051-0032-45ce-85eb-d0f1a1eeb687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XP4XF86PsCMNgTJohJoju7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1692,
      "cache_read_input_tokens": 16670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1692,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 13 · 2026-05-14T00:56:53.938Z_

<details><summary>↩ Tool result · `toolu_01W1msxsh3KtKWNwSny3zSwo`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'ratekv'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a59a5051-0032-45ce-85eb-d0f1a1eeb687",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "aec1aaa9-a915-414f-ae6e-0a5fded57ab6",
  "sourceToolAssistantUUID": "a59a5051-0032-45ce-85eb-d0f1a1eeb687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T00:56:54.867Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YbCCoggZSDkT9FWZNyjKLS`</summary>

```json
{
  "project": "ratekv",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aec1aaa9-a915-414f-ae6e-0a5fded57ab6",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1YyL7rY8zSa2gSppDz6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d535583-b122-4d8b-93a5-0ca76c657c7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XP4XF86PsCMNgTJohJoju7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1692,
      "cache_read_input_tokens": 16670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1692,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 15 · 2026-05-14T00:56:54.884Z_

<details><summary>↩ Tool result · `toolu_01YbCCoggZSDkT9FWZNyjKLS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/paper_framing.md\", \"content\": \"# Paper Framing — ratekv\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission)\\n- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)\\n- Track: Efficient Methods for NLP\\n\\n## Core Insight\\n\\nPer-head independent distortion profiling systematically underestimates joint degradation at extreme quantization levels due to compounding effects. A constrained MCKP formulation bridges this gap: cardinality constraints on extreme bit-widths act as principled regularization for profiler systematic errors, enabling automatic near-optimal per-head bit-width allocation for KV cache quantization.\\n\\n## Core Claims (3 条)\\n\\n1. **Head sensitivity heterogeneity**: Per-KV-head quantization sensitivity in modern LLMs is extremely non-uniform — Layer 0 heads exhibit ~26× higher 2-bit profiling delta than average (3.29 vs 0.128), and Layer 0 (3.6% of heads) accounts for ~52% of total profiled distortion. Protecting Layer 0 alone (4-bit→8-bit) reduces PPL from 15.45 to 10.62, recovering most of the uniform quantization degradation.\\n\\n2. **Constrained MCKP outperforms uniform and manual allocation**: A constrained MCKP solver over discrete bit-width action space {2,4,8,16}-bit with cardinality constraints achieves 27% PPL improvement over uniform 4-bit at matched 4× compression budget (11.23 vs 15.45), and outperforms hand-designed oracle strategies (11.23 vs 11.69).\\n\\n3. **Cardinality constraints as profiler error regularization**: Unconstrained solvers that trust per-head independent profiling produce catastrophic allocations (PPL 36.92) because additive distortion models fail when many heads are simultaneously assigned extreme quantization. Cardinality constraints (≤k heads at 2-bit) regularize this non-additivity, and the optimal k can be determined by a small-scale compounding effect test.\\n\\n## Story Spine\\n\\n- **Problem**: KV cache quantization typically applies uniform bit-width across all heads, wasting budget on insensitive heads while under-protecting critical ones. Per-head mixed-precision allocation promises better quality-compression tradeoffs, but existing approaches (RateQuant's greedy/closed-form allocation) assume consecutive-integer bit-widths and additive distortion — both assumptions break for hardware-aligned discrete sets and at scale.\\n\\n- **Existing approaches & gaps**: RateQuant (May 2026) provides R-D optimal per-head allocation via both continuous closed-form (Theorem 2) and discrete greedy (Algorithm 1, optimal on consecutive integers {2,...,6} per Proposition 6). However, its optimality guarantee depends on polymatroid structure of consecutive integer bit-widths and additive distortion — both assumptions break for hardware-aligned discrete sets {2,4,8,16} and under compounding effects. RateQuant also supports asymmetric K/V allocation, which we extend. ARKV (March 2026) does per-layer heuristic selection but lacks per-head granularity and optimality guarantees. No existing method addresses the fundamental gap between independent per-head profiling and joint quantization effects.\\n\\n- **Our framing**: We formulate per-head bit-width allocation as a constrained MCKP over discrete bit-widths. The key insight is that cardinality constraints on extreme quantization levels (2-bit) serve as principled regularization for profiler systematic errors — specifically, the non-additivity of extreme quantization that independent profiling cannot capture. This makes the solver robust to imperfect distortion estimates while preserving near-optimality.\\n\\n- **Headline result template**: \\\"On Qwen2.5-7B, constrained MCKP allocation achieves PPL 11.23 at 4× KV cache compression, a 27% improvement over uniform 4-bit (PPL 15.45) and better than hand-designed oracle strategies (PPL 11.69), with the solver automatically discovering that Layer 0 heads require 8-bit protection.\\\"\\n\\n## Differentiation from RateQuant\\n\\n| Aspect | RateQuant | Ours |\\n|--------|-----------|------|\\n| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Discrete MCKP on hardware-aligned {2,4,8,16}-bit |\\n| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization |\\n| Compounding effects | Acknowledged (Appendix M) but unaddressed | Explicitly handled via constraints; first quantitative evidence (PPL 36.92 unconstrained) |\\n| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → MCKP needed) |\\n| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP treats K/V heads as independent items (natural extension) |\\n| Optimality | Proven on consecutive integers under additive assumption | Near-optimal with regularized profiling on practical bit-widths |\\n\\n## Venue Fit Risks\\n\\n- **Incrementality over RateQuant**: Strongest reviewer attack. Defense: (a) RateQuant's greedy optimality (Prop. 6) relies on consecutive-integer polymatroid structure that breaks on hardware-aligned {2,4,8,16} — experimentally verified via plan_008, (b) compounding effect discovery and constraint-based regularization are novel contributions with first quantitative evidence, (c) RateQuant's additive assumption demonstrably fails at scale (PPL 36.92 unconstrained vs 11.23 constrained). Note: do NOT claim \\\"RateQuant fails\\\" — it works well in its own setting; our contribution is extending to practical discrete bit-widths with compounding regularization.\\n- **Single-domain evaluation**: KV cache quantization only. Mitigate by testing across model families (Qwen, Llama, Mistral) with different GQA ratios.\\n- **No eviction arm**: Original idea proposed joint eviction+quantization. Eviction was abandoned after MVP (attention MSE fails as distortion proxy for eviction). Mention as negative finding in paper; the MCKP framework itself extends naturally to include eviction once better eviction distortion metrics are developed.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"This is just RateQuant with MCKP instead of waterfilling\\\"** → (a) Implement RateQuant's greedy algorithm on {2,4,8,16} and show it's suboptimal vs constrained MCKP (plan_008), (b) show unconstrained MCKP also fails (PPL 36.92) proving the compounding problem is real, (c) our contribution is the constraint-regularized formulation that handles both discrete action spaces and non-additive distortion.\\n2. **\\\"Only tested on one model\\\"** → Multi-model experiments (Llama, Mistral) are P0.\\n3. **\\\"Cardinality constraint is just a heuristic\\\"** → Show it has principled motivation (compounding effect non-additivity); characterize the compounding threshold empirically; show constraint value k can be determined systematically.\\n4. **\\\"How does this work at different compression ratios?\\\"** → Budget sweep across 2×, 4×, 8× compression.\\n5. **\\\"Profiler resolution is too low for mid-layer differentiation\\\"** → High-res profiling experiment (64 seq × 2048 tokens) to explore.\\n6. **\\\"RateQuant does K/V asymmetric allocation, do you?\\\"** → MCKP framework naturally treats K and V heads as independent items; plan_014 tests K/V separation. Even without explicit separation, our per-head granularity implicitly allows different K/V allocations within the same layer.\\n7. **\\\"Where are the downstream task results?\\\"** → RateQuant reports ARC-C/HellaSwag/PIQA/WinoGrande; plan_012 covers downstream evaluation to enable direct comparison.\\n\", \"total_chars\": 7371, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d535583-b122-4d8b-93a5-0ca76c657c7f",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "b2453357-9d3d-4977-9242-6908c4765147",
  "sourceToolAssistantUUID": "0d535583-b122-4d8b-93a5-0ca76c657c7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T00:56:55.347Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01369CqUy2qABp2fbmsHU54q`</summary>

```json
{
  "project": "ratekv",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2453357-9d3d-4977-9242-6908c4765147",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1YyL7rY8zSa2gSppDz6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83829326-1843-4ec6-8b1b-66838fde1bfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XP4XF86PsCMNgTJohJoju7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1692,
      "cache_read_input_tokens": 16670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1692,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 17 · 2026-05-14T00:56:55.357Z_

<details><summary>↩ Tool result · `toolu_01369CqUy2qABp2fbmsHU54q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/memory.md\", \"content\": \"# ratekv — Memory\\n\\n## 核心教训\\n\\n### Compounding U 型曲线已确立 (2026-05-14)\\n- max_2bit sweep {0,4,8,16,24,48,75,112} 产出清晰 U 型曲线，最优点 k=8 (PPL=11.23)\\n- k=0 = uniform 4-bit (15.45)；k=4 已显著改善 (11.77)；k=16 略退 (11.81)\\n- Sharp elbow at k=24→48 (13.14→22.88, +74%)；k≥75 collapse (35.35)\\n- k=112 饱和在 75 actual 2-bit heads（solver 自限）\\n- **Paper claim**: cardinality constraint k 的选择有 principled basis，不是 ad-hoc\\n\\n### Constrained MCKP 是正确方案 (2026-05-14)\\n- 无约束 MCKP 始终 collapse（PPL=36.92，75/112 heads 分配到 2-bit）\\n- Constrained MCKP（max_2bit≤8）PPL=11.23，优于 uniform 4-bit (15.45) 27%\\n- 自动 solver 甚至优于手工 budget-matched (11.69)\\n- **关键代码修复**：跳过 Pareto 过滤（`_build_actions_no_pareto()`），保留所有 bit-width 选项\\n- **方法论简化**：exp_d 证明 L0 排除约束冗余——只需 max_2bit≤K 一个约束。Solver 自动从 profiler 信号发现 L0 sensitivity\\n\\n### RateQuant 差异化分析 (2026-05-14)\\n- RateQuant 用 consecutive integer {2,3,4,5,6}，Proposition 6 optimality 仅对 consecutive 成立\\n- {2,4,8,16} 破坏 polymatroid structure，RateQuant greedy 不再 optimal\\n- RateQuant 假设 additive distortion，Appendix M 承认 \\\"may not hold\\\" 但无证据或解决方案\\n- 我们的 PPL=36.92 是 additive assumption failure 的首个定量证据\\n- RateQuant 有 K/V separation（K 2.85bit / V 2.15bit），可作为我们的 extension\\n- **Framing**: 不说 RateQuant 失败，说其 framework 无法 extend 到 practical discrete bit-widths without constraint\\n\\n### 2-bit 在 action space 中是必要的 (2026-05-14)\\n- exp_c_no2bit: {4,8,16}-bit only 在 budget=0.25 下退化为全部 4-bit\\n- 2-bit 选项是创造 heterogeneity 的必要条件——\\\"预算捐献者\\\"让其他 head 升级到 8-bit\\n\\n### MSE distortion metric 已被 falsify (2026-05-13)\\n- MSE-guided MCKP: Full PPL=1084.56, Uniform 4-bit=15.45。MSE 与 PPL 完全不相关\\n\\n### Eviction 路径已彻底关闭 (2026-05-13)\\n- 全局/Targeted/PPL-guided eviction 均失败。**不要再尝试任何 eviction 相关实验**\\n\\n### 2-bit cliff effect 确认 (2026-05-13)\\n- Cliff 仅限 Layer 0（1.5B: 2/56; 7B: 3/112）\\n- 4-bit 和 8-bit 在两个模型上均无 cliff\\n\\n### PPL profiler 分辨率坍缩 (2026-05-13)\\n- 112 heads 中仅 ~15 个有 non-zero 2-bit delta（calibration 16×512 太短）\\n- Constrained solver 解决了这个问题：max_2bit=8 限制分配数量，即使部分 delta=0\\n\\n## 环境经验 (westd-37397)\\n\\n- **tmux 不加载 .bashrc**: 非交互 shell 必须显式 `source /etc/network_turbo` + 设置全部 proxy 环境变量\\n- **cache_position 必需**: transformers 4.57.6 的 Qwen2 需要 `cache_position=torch.arange(seq_len, device=device)` 在 `use_cache=False` 时\\n- **ModelScope 路径含 `___`**: 导致 HFValidationError，需下载到干净路径\\n- **calibration 数据长度**: WikiText-103 原始段落平均 ~165 tokens，必须拼接至 ≥4000 chars\\n- **profiler 缓存 profiles.json**: 换模型/数据时必须删除\\n- **submit_training_job 命令必须 bash -c 包裹**: tmux 用 sh 执行\\n\\n## 模型信息\\n\\n- Qwen2.5-7B: 28 layers, 28 query heads, 4 KV heads/layer (GQA 7:1), head_dim=128, 共 112 KV heads\\n- Qwen2.5-1.5B: 28 layers, 2 KV heads/layer, 共 56 KV heads\\n- 7B 路径: /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B\\n- 1.5B 路径: /root/autodl-tmp/models/Qwen2.5-1.5B\\n\", \"total_chars\": 2664, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83829326-1843-4ec6-8b1b-66838fde1bfc",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "2b7123b2-3c06-46b9-b3e4-aac56e9b77d8",
  "sourceToolAssistantUUID": "83829326-1843-4ec6-8b1b-66838fde1bfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T00:56:55.808Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WrixaYNTR36ZFZuEVHKqC5`</summary>

```json
{
  "project": "ratekv",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b7123b2-3c06-46b9-b3e4-aac56e9b77d8",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1YyL7rY8zSa2gSppDz6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ddd299f-7aeb-468d-a5ce-18de474e46b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XP4XF86PsCMNgTJohJoju7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1692,
      "cache_read_input_tokens": 16670,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1692
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 372,
          "cache_read_input_tokens": 16670,
          "cache_creation_input_tokens": 1692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1692,
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

_source line 19 · 2026-05-14T00:56:55.818Z_

<details><summary>↩ Tool result · `toolu_01WrixaYNTR36ZFZuEVHKqC5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/ROADMAP.md\", \"content\": \"# ratekv — Research Dashboard\\n\\n> 最后更新: 2026-05-14 00:21 UTC | 更新原因: Post-MVP: 写完 framing + plan, dream 已提交, 更新 ROADMAP 为 research dashboard 格式\\n\\n## 核心方向\\nPer-KV-head 非均匀 bit-width 分配：通过 constrained MCKP 为每个 KV head 选择最优 bit-width，cardinality constraint 作为 profiler 系统误差的正则化。详见 `paper_framing.md`。\\n\\n## 当前阶段: Research（Post-MVP）\\n\\n**MVP 结果**: Constrained MCKP solver PPL=11.23 vs uniform 4-bit 15.45（27% 改善），budget=0.2500 精确匹配，solver 优于手动 oracle (11.23 vs 11.69)。\\n\\n**投稿目标**: EMNLP 2026 Main (ARR May 25, 2026)\\n\\n## Core Claims (from paper_framing.md)\\n1. Head sensitivity heterogeneity: Layer 0 heads 100× higher delta, 3.6% heads → 70%+ PPL\\n2. Constrained MCKP outperforms uniform (27%) and manual oracle\\n3. Cardinality constraints = principled regularization for compounding non-additivity\\n\\n## 实验计划 (from experiment_plan.yaml)\\n\\n### P0 (必跑, ~20 GPU-h, 2-3 天)\\n| ID | 描述 | Claim | 模型 |\\n|----|------|-------|------|\\n| plan_001 | 去掉 L0 排除约束验证 solver 自主性 | 2 | Qwen2.5-7B |\\n| plan_002 | Llama-3.1-8B 全 pipeline 复现 | 1,2 | Llama-3.1-8B |\\n| plan_003 | Mistral-7B 跨架构验证 | 1,2 | Mistral-7B |\\n| plan_004 | Compounding effect 阈值扫描 (max_2bit sweep) | 3 | Qwen2.5-7B |\\n| plan_005 | Budget sweep (2×/4×/8× 压缩) | 2 | Qwen2.5-7B |\\n| plan_006 | 高分辨率 profiling (64seq×2048tok) | 1,2 | Qwen2.5-7B |\\n| plan_007 | C4 跨数据集评估 | 1,2,3 | Qwen2.5-7B |\\n\\n### P1 (时间允许, ~13 GPU-h)\\nplan_008 RateQuant waterfilling baseline | plan_009 Oracle comparison | plan_010 Cross-domain calibration | plan_011 Visualization\\n\\n### P2 (加分项, ~12 GPU-h)\\nplan_012 Downstream tasks | plan_013 70B profiling\\n\\n## 近期任务\\n- [ ] 等待 Dream 完成 (dream_20260514T002109) → 验证 framing/plan 是否有结构性问题\\n- [ ] Dream 通过后启动 P0 实验（plan_001-007 尽量并行）\\n\\n## GPU 预算\\nwestd-37397: 2× RTX PRO 6000 96GB (cuda:0 + cuda:1)\\nP0 总需 ~20 GPU-h → 约 2-3 天可完成（双卡并行）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D012 | 2026-05-14 | Corrected RateQuant characterization in paper_fram | plan_008, plan_012, plan_014 |\\n| D011 | 2026-05-14 | Solver auto-discovers L0 sensitivity — plan_001 va | exp_d_no_l0_exclusion, exp_c_constrained_mckp, exp_c_no2bit |\\n| D010 | 2026-05-14 | MVP PASS: constrained MCKP solver PPL=11.23 vs uni | exp_c_constrained_mckp |\\n| D009 | 2026-05-13 | 撤回 D008 Path B; 改为 constrained MCKP: 保留 2-bit 但加 c | exp_b_hires_quant |\\n| D008 | 2026-05-13 | exp_b MIXED: 假设验证(手动24%↑)但solver失败; 采用Path B去掉2-bi | exp_b_hires_quant |\\n| D007 | 2026-05-13 | Pivot: 放弃 eviction arm，转向 PPL-guided per-head bit- | — |\\n| D006 | 2026-05-13 | PPL-guided MCKP 仍然失败：根因是 eviction 的 compounding ef | p0_1_ppl_fast, p0_2_cliff_7B |\\n| D005 | 2026-05-13 | MVP 实质 FAIL：attention MSE 被 falsify，pivot 到 chunk- | mvp_004, sanity_004 |\\n| D004 | 2026-05-13 | 1.5B sanity 暴露 attention MSE 与 PPL 脱钩；7B 继续跑但需准备 m | sanity_004 |\\n| D003 | 2026-05-13 | MVP 模型从 Llama 3.1-8B 切换到 Qwen2.5-7B，DuoAttention v | — |\\n\\n\", \"total_chars\": 2822, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ddd299f-7aeb-468d-a5ce-18de474e46b7",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "90c556ea-5fcd-4485-8030-ff743d63f2a3",
  "sourceToolAssistantUUID": "1ddd299f-7aeb-468d-a5ce-18de474e46b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T00:57:00.461Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Nc2fnJ3yByp4EGZM4t7r1Z`</summary>

```json
{
  "project": "ratekv",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90c556ea-5fcd-4485-8030-ff743d63f2a3",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1YyjiS32WS34LZJvvf9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04b699e9-00bc-4484-bf06-de7536870212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y1Vr6LMCitAVbup1ifcb9C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6113,
      "cache_read_input_tokens": 18362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6113,
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

_source line 21 · 2026-05-14T00:57:00.473Z_

<details><summary>↩ Tool result · `toolu_01Nc2fnJ3yByp4EGZM4t7r1Z`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'ratekv'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04b699e9-00bc-4484-bf06-de7536870212",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "de99f226-4b7c-4b86-8387-d04de8aa3e72",
  "sourceToolAssistantUUID": "04b699e9-00bc-4484-bf06-de7536870212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T00:57:00.873Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VZMka2J9eFPri3DzyMpeoG`</summary>

```json
{
  "project": "ratekv",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de99f226-4b7c-4b86-8387-d04de8aa3e72",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1YyjiS32WS34LZJvvf9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a0153f2-958d-4bc2-b0ed-4ba5008f6ad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y1Vr6LMCitAVbup1ifcb9C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6113,
      "cache_read_input_tokens": 18362,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6113
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 18362,
          "cache_creation_input_tokens": 6113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6113,
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

_source line 23 · 2026-05-14T00:57:00.883Z_

<details><summary>↩ Tool result · `toolu_01VZMka2J9eFPri3DzyMpeoG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/decisions.yaml\", \"content\": \"_next_id: 13\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:13 UTC\\n  summary: 'MVP 验证方案: Llama 3.1-8B 上验证 eviction-quantization crossover 存在性 + MCKP\\n    分配有效性'\\n  rationale: '核心假设是 per-KV-head 异质性使得 joint eviction+quantization allocation 优于 uniform\\n    quantization。最小验证: 单模型 distortion profiling + crossover 可视化 + MCKP vs uniform\\n    4-bit 对比。Pass 标准: ≥15% heads prefer eviction + perplexity improvement。选 Llama\\n    3.1-8B 因为 DuoAttention 已有该模型的 streaming/retrieval head 分类数据可做 post-hoc validation。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:16 UTC\\n  summary: 'MVP gate v2: 加 quant-only MCKP baseline + 消除死区 + 最小效应量 ≥0.5 PPL'\\n  rationale: 'Reviewer 初审指出三个漏洞: (1) uniform 4-bit 太弱，任何 per-head 方法都能赢，核心 claim 是\\n    joint > quant-only，必须加 quant-only MCKP baseline; (2) 5%-15% crossover 比例死区导致判定模糊，合并为单一\\n    ≥10% 阈值; (3) PPL 改善无最小效应量可能产生假阳性，设 ≥0.5 PPL 门槛。quant-only baseline 零额外工程量（同一 solver\\n    限制 action set）。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 18:12 UTC\\n  summary: MVP 模型从 Llama 3.1-8B 切换到 Qwen2.5-7B，DuoAttention validation 延后\\n  rationale: Llama 3.1-8B 是 HF gated model，用户尚未提供 HF token，GPU 空闲不能等。Qwen2.5-7B 非\\n    gated、GQA 架构、7B 参数量相近，满足 MVP 验证 per-KV-head crossover 假设的需求。代价：DuoAttention post-hoc\\n    validation（D001 rationale 中的 convergent evidence story）暂时无法做——DuoAttention 论文只分析了\\n    Llama 系列。替代方案：(1) 用户后续提供 HF token 后加 Llama 作为第二模型；(2) 在 Qwen 上自行运行 DuoAttention\\n    分类作为替代验证。MVP 核心假设（crossover 存在性 + MCKP 优于 uniform）不依赖 DuoAttention 叙事。注意：Qwen2.5-7B\\n    的 KV head 数（4×28=112）少于 Llama（8×32=256），GQA ratio 更高（7:1 vs 4:1），crossover 比例可能偏低。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-13 21:55 UTC\\n  summary: 1.5B sanity 暴露 attention MSE 与 PPL 脱钩；7B 继续跑但需准备 metric 修正方案\\n  rationale: Qwen2.5-1.5B sanity 结果显示：(1) crossover 只在 8x 极端压缩出现（89.3% heads），此时 PPL\\n    已崩溃（14000+）；(2) 在实用的 4x 压缩下 full MCKP 反而比 quant-only 差 2.77 PPL，甚至比 uniform 4-bit\\n    差 3.41 PPL；(3) 根因是 attention output MSE 系统性低估 eviction 的 downstream 损伤——eviction\\n    是 structured error（完整丢弃 token），量化是 unstructured error（均匀噪声），MSE 无法区分两者的级联影响。形式上\\n    MVP gate PASS 但实质不成立（在 catastrophic regime 的 false positive）。7B 实验已提交继续跑，确认 pattern\\n    是否 model-agnostic。同时需准备 metric 修正：(a) layer-output MSE 替代 attention-output MSE；(b)\\n    eviction distortion penalty；(c) gate criteria 收紧排除 PPL>2x baseline 的 regime。\\n  related_experiments:\\n  - exp_id: sanity_004\\n    role: evidence\\n    result: crossover exists but metric-PPL decoupled\\n  depends_on:\\n  - D001\\n  - D003\\n- id: D005\\n  date: 2026-05-13 22:03 UTC\\n  summary: MVP 实质 FAIL：attention MSE 被 falsify，pivot 到 chunk-level PPL distortion\\n    metric\\n  rationale: 7B 结果灾难性确认 metric-PPL 脱钩：budget=0.25 下 MSE 最优方案(Full MCKP) PPL=1084 vs\\n    MSE 最差方案(uniform 4-bit) PPL=15.45，反差 70×。更关键的是 quant-only MCKP (5574) vs uniform\\n    4-bit (15.45) 证明 MSE 对 quantization bit 分配同样失效——问题不仅限于 eviction。问题随模型规模指数级恶化（1.5B\\n    比 1.2×, 7B 比 70×）。被 falsify 的是 attention output MSE 作为 distortion proxy，不是 per-head\\n    MCKP framework 或 crossover 假设。立即 pivot：P0 并行跑 chunk-level PPL distortion profiling\\n    + 2-bit quant 隔离测试，验证 PPL-aligned metric 能否让 solver 做出正确分配。\\n  related_experiments:\\n  - exp_id: mvp_004\\n    role: evidence\\n    result: MSE-PPL 70x decoupling at 7B; MCKP allocation harmful under MSE\\n  - exp_id: sanity_004\\n    role: evidence\\n    result: MSE-PPL 1.2x decoupling at 1.5B\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 23:03 UTC\\n  summary: PPL-guided MCKP 仍然失败：根因是 eviction 的 compounding effect 违反 per-head 独立性假设；转向\\n    targeted hybrid 策略\\n  rationale: PPL-based distortion profiling 结果：Full MCKP 28.07 vs Quant-only 15.45\\n    vs Uniform 15.45。换 metric 没解决问题——per-head 独立 profiling 中单 head eviction delta\\n    仅 ~0.13，但 47 heads 同时 eviction 产生 compounding effect (+18.26 PPL)。eviction 是 structured\\n    error，多头同时丢弃同一批 token，损伤不可加。Quantization 独立性成立（quant-only MCKP = uniform 15.45）。另外\\n    PPL profiling 分辨率不足（100/112 heads 显示相同 delta），需更多 eval tokens。两个可行方向：(A) targeted\\n    hybrid——仅 Layer 0 cliff heads 用 eviction（quantization 损伤极大），其余全 quantization +\\n    非均匀 bit 分配；(B) group-level eviction profiling (O(n²))。优先试 A，低成本高信息量。\\n  related_experiments:\\n  - exp_id: p0_1_ppl_fast\\n    role: evidence\\n    result: PPL-guided MCKP still 1.8x worse than uniform; eviction compounding effect\\n  - exp_id: p0_2_cliff_7B\\n    role: evidence\\n    result: Layer 0 is only cliff layer; 3/112 heads sensitive to 2-bit\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-13 23:24 UTC\\n  summary: 'Pivot: 放弃 eviction arm，转向 PPL-guided per-head bit-width allocation (quant-only\\n    MCKP with {2,4,8,16}-bit)'\\n  rationale: Joint eviction+quantization 核心假设已被 falsify——eviction 的 compounding effect\\n    使 per-head 独立 profiling 原理上无法 work。但 Reviewer 指出关键盲区：之前 quant-only MCKP = uniform\\n    是 fast mode artifact（只有一个 4-bit 选项，solver 数学上只能 uniform），不是真实证据。Cliff data 证明\\n    per-head quantization sensitivity 高度不均匀（L0H0 2-bit +297% vs 大多数 head <1%）。关键实验：PPL-guided\\n    quant-only MCKP，action space {2,4,8,16}-bit，budget 4x。如果 MCKP PPL < uniform 4-bit\\n    ≥0.5 → 论文 pivot 为 rate-distortion optimal per-head bit-width allocation；如果 ≈ uniform\\n    → archive。~4h GPU 即可做 go/no-go 决策。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-13 23:54 UTC\\n  summary: 'exp_b MIXED: 假设验证(手动24%↑)但solver失败; 采用Path B去掉2-bit修复solver'\\n  rationale: Reviewer 审查 exp_b full bit-width MCKP 结果：(1) 自动 solver 因 profiler 分辨率不足(84%\\n    heads delta=0.0000@2-bit)和 additive model 无法捕获 compounding effect，PPL 崩溃至 36.92\\n    且 under-budget 28%；(2) 手动 budget-matched 分配(L0@8bit, 8@2bit, rest@4bit) PPL=11.69\\n    vs uniform 15.45，改善 3.76 (24%)，远超 0.5 阈值——假设\\\"非均匀分配优于均匀\\\"成立；(3) 2-bit compounding\\n    effect 在 8-24 heads 间出现拐点，per-head 独立 profiling 无法发现此阈值。决定采用 Path B：去掉 2-bit 选项，用\\n    4/8/16-bit 三选项 MCKP，避免 compounding effect 同时仍能捕获 Layer 0 sensitivity 差异。实现后重跑\\n    solver 获取 clean MVP pass。\\n  related_experiments:\\n  - exp_id: exp_b_hires_quant\\n    role: primary\\n    result: mixed — manual pass, auto solver fail\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-13 23:56 UTC\\n  summary: '撤回 D008 Path B; 改为 constrained MCKP: 保留 2-bit 但加 count(2-bit)≤8 约束'\\n  rationale: Reviewer 指出 D008 的 Path B（去掉 2-bit）在 budget=0.25 下数学上退化为 uniform 4-bit——最廉价选项就是\\n    4-bit(ratio=0.25)，没有更便宜的选项来节省 budget 资助升级。手动实验(PPL 11.69)之所以能 work，正是靠 8 heads@2-bit\\n    节省的 budget(8×(0.25-0.125)=1.0)来资助 4 heads@8-bit 升级(4×(0.50-0.25)=1.0)。正确修复：保留\\n    {2,4,8,16}-bit action space，增加 cardinality constraint count(2-bit)≤8。K=8 基于手动实验安全区间（8@2-bit\\n    → PPL 11.69 PASS，24@2-bit → PPL 17.74 FAIL）。这是 MCKP 文献中的标准 cardinality constraint，保留理论框架的同时避免\\n    compounding effect。\\n  related_experiments:\\n  - exp_id: exp_b_hires_quant\\n    role: primary\\n    result: manual pass informs constraint K=8\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-14 00:17 UTC\\n  summary: 'MVP PASS: constrained MCKP solver PPL=11.23 vs uniform 15.45 (27%↑), 进入research阶段'\\n  rationale: Reviewer 确认 exp_c_constrained_mckp 通过 MVP gate：(1) PPL=11.23 vs uniform\\n    4-bit 15.45，改善 4.21 (27%)，远超 0.5 阈值；(2) budget 精确匹配 0.2500；(3) solver 自动输出优于手动\\n    oracle (11.23 vs 11.69, +0.46)；(4) 数据一致性已核实（日志/results.json/registry notes 完全一致）。solver\\n    使用 max_2bit=8 + L0 excluded from 2-bit 约束，分配 4×8-bit + 8×2-bit + 100×4-bit。Layer\\n    0 全部 8-bit 是 solver 基于 profiling delta 自主选择。Research 阶段需跟进：(a) 去掉 L0 排除约束测试 solver\\n    是否自动回避 L0 2-bit；(b) 多模型验证（不同 GQA ratio）；(c) 高分辨率 profiling；(d) cardinality constraint\\n    的理论阐释。\\n  related_experiments:\\n  - exp_id: exp_c_constrained_mckp\\n    role: primary\\n    result: PASS — PPL 11.23 vs uniform 15.45 (27%)\\n  depends_on:\\n  - D008\\n- id: D011\\n  date: 2026-05-14 00:28 UTC\\n  summary: Solver auto-discovers L0 sensitivity — plan_001 validated, manual L0 exclusion\\n    constraint proven redundant\\n  rationale: exp_d (no L0 exclusion) 产生与 exp_c (L0 excluded) 完全一致的分配结果 (PPL=11.23,\\n    budget=0.2500, 同一 bit 分布)。Solver 仅凭 profiling distortion 信号自动将 L0 保持 8-bit。方法论更干净：只需\\n    cardinality constraint max_2bit≤K，无需手动 layer 排除。同时 exp_c_no2bit 证实 2-bit 是 heterogeneity\\n    的必要条件（去掉后退化为 uniform 4-bit）。\\n  related_experiments:\\n  - exp_id: exp_d_no_l0_exclusion\\n    role: primary\\n    result: success - identical allocation without manual L0 exclusion\\n  - exp_id: exp_c_constrained_mckp\\n    role: baseline\\n    result: success - reference with manual L0 exclusion\\n  - exp_id: exp_c_no2bit\\n    role: supporting_negative\\n    result: negative - confirms 2-bit necessity for heterogeneity\\n  depends_on: []\\n- id: D012\\n  date: 2026-05-14 00:37 UTC\\n  summary: Corrected RateQuant characterization in paper_framing.md; upgraded plan_008\\n    to P0, plan_012 to P1; added plan_014 (K/V separation) at P1\\n  rationale: Reviewer 发现 paper_framing.md 对 RateQuant 的描述有误——RateQuant 有 discrete\\n    greedy (Algorithm 1, Prop. 6) 而非仅 continuous waterfilling。Mischaracterize 竞争工作是审稿大忌。同时：(1)\\n    plan_008 升 P0 因为 differentiation claim 需要实验证据证明 RateQuant greedy 在 {2,4,8,16}\\n    上不 optimal；(2) plan_012 升 P1 因为 RateQuant 有 downstream eval 我们不能缺；(3) 新增 plan_014\\n    K/V separation 因为 RateQuant 支持 asymmetric K/V，MCKP 天然支持但需要实验验证。\\n  related_experiments:\\n  - exp_id: plan_008\\n    role: upgraded_to_P0\\n    result: planned\\n  - exp_id: plan_012\\n    role: upgraded_to_P1\\n    result: planned\\n  - exp_id: plan_014\\n    role: new_P1\\n    result: planned\\n  depends_on: []\\n\", \"total_chars\": 9256, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a0153f2-958d-4bc2-b0ed-4ba5008f6ad7",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "7b4377ff-eaa8-43ed-930f-205b8a68d07c",
  "sourceToolAssistantUUID": "3a0153f2-958d-4bc2-b0ed-4ba5008f6ad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-14T00:57:05.921Z_

Now let me look at the artifacts and any experimental data to verify the claimed results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b4377ff-eaa8-43ed-930f-205b8a68d07c",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Yz7MBViCnvwgTjhX9X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b9d36b8-bbe0-492a-88de-f7928fcf15d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjdMDho2qAZyMnpzBExfKj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5439,
      "cache_read_input_tokens": 24475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5439,
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

_source line 25 · 2026-05-14T00:57:07.812Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YHKRYhqSR3Tu8m4Z8hFZTP`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b9d36b8-bbe0-492a-88de-f7928fcf15d3",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Yz7MBViCnvwgTjhX9X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dd601cf-524a-47ef-9237-81db2440aa32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjdMDho2qAZyMnpzBExfKj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5439,
      "cache_read_input_tokens": 24475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5439,
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

_source line 26 · 2026-05-14T00:57:07.822Z_

<details><summary>↩ Tool result · `toolu_01YHKRYhqSR3Tu8m4Z8hFZTP`</summary>

```text
artifacts/full_bitwidth_profiler.py
artifacts/run_full_bitwidth.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dd601cf-524a-47ef-9237-81db2440aa32",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "c598cb4c-0ca9-4419-8f2e-a84b6dcf8ca2",
  "sourceToolAssistantUUID": "8dd601cf-524a-47ef-9237-81db2440aa32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T00:57:08.101Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AbXNZpQL9xu314yqTuuQZD`</summary>

```json
{
  "pattern": "**/artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c598cb4c-0ca9-4419-8f2e-a84b6dcf8ca2",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Yz7MBViCnvwgTjhX9X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dba5a348-7ade-4dd6-9286-54fba4fb540c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjdMDho2qAZyMnpzBExfKj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5439,
      "cache_read_input_tokens": 24475,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5439
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 24475,
          "cache_creation_input_tokens": 5439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5439,
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

_source line 28 · 2026-05-14T00:57:08.222Z_

<details><summary>↩ Tool result · `toolu_01AbXNZpQL9xu314yqTuuQZD`</summary>

```text
artifacts/full_bitwidth_profiler.py
artifacts/run_full_bitwidth.py
artifacts/dream_reports/dream_20260514T002109/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260514T002109/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260514T002109/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T002109/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T002109/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T002109/best/experiment_data.json
artifacts/dream_reports/dream_20260514T002109/best/paper_framing.md
artifacts/dream_reports/dream_20260514T002109/best/paper.tex
artifacts/dream_reports/dream_20260514T002109/best/paper.aux
artifacts/dream_reports/dream_20260514T002109/best/paper.out
artifacts/dream_reports/dream_20260514T002109/best/paper.pdf
artifacts/dream_reports/dream_20260514T002109/best/paper.log
artifacts/dream_reports/dream_20260514T002109/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T002109/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T002109/median/experiment_data.json
artifacts/dream_reports/dream_20260514T002109/median/paper_framing.md
artifacts/compounding_sweep/data/compounding_sweep_results.csv
artifacts/manifest.yaml
artifacts/dream_reports/dream_20260514T002109/median/paper.tex
artifacts/dream_reports/dream_20260514T002109/median/paper.aux
artifacts/dream_reports/dream_20260514T002109/median/paper.out
artifacts/dream_reports/dream_20260514T002109/median/paper.pdf
artifacts/dream_reports/dream_20260514T002109/median/paper.log
artifacts/dream_reports/dream_20260514T002109/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T002109/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T002109/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T002109/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T002109/worst/paper.tex
artifacts/dream_reports/dream_20260514T002109/worst/paper.aux
artifacts/dream_reports/dream_20260514T002109/worst/paper.out
artifacts/dream_reports/dream_20260514T002109/worst/paper.pdf
artifacts/dream_reports/dream_20260514T002109/worst/paper.log
artifacts/dream_reports/dream_20260514T002109/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T002109/logs/orchestrator.log
artifacts/dream_reports/dream_20260514T002109/best/review_context.yaml
artifacts/dream_reports/dream_20260514T002109/best/review_report.md
artifacts/dream_reports/dream_20260514T002109/logs/review_best.log
artifacts/dream_reports/dream_20260514T002109/median/review_context.yaml
artifacts/dream_reports/dream_20260514T002109/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dba5a348-7ade-4dd6-9286-54fba4fb540c",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "d4837f29-931f-4355-bac3-2d176e08d38e",
  "sourceToolAssistantUUID": "dba5a348-7ade-4dd6-9286-54fba4fb540c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T00:57:13.424Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NbkyHY98SA3sJZRAEK3wRM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4837f29-931f-4355-bac3-2d176e08d38e",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Yzea9J2P7ZAsQsnrJM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33f809ec-51e1-49d7-9ccd-74cacd41e933",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ss9JHFJHYNfv7CAkQU44pu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1167,
      "cache_read_input_tokens": 29914,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1167
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 29914,
          "cache_creation_input_tokens": 1167,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1167,
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

_source line 30 · 2026-05-14T00:57:13.711Z_

<details><summary>↩ Tool result · `toolu_01NbkyHY98SA3sJZRAEK3wRM`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath,amssymb}
6	\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}
7	\usepackage{natbib}
8	\renewcommand{\bibsection}{\section*{References}}
9	\usepackage{booktabs}
10	\usepackage{multirow}
11	\usepackage{graphicx}
12	\usepackage{xcolor}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	
16	\title{Cardinality-Constrained MCKP for Per-Head Mixed-Precision KV Cache Quantization}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	%======================================================================
24	\begin{abstract}
25	KV cache quantization is a key technique for reducing memory footprint during large language model inference.
26	Existing approaches apply uniform bit-widths across all attention heads or rely on continuous relaxations that ignore the discrete nature of hardware-supported precisions.
27	We show that per-head quantization sensitivity in modern LLMs is extremely non-uniform: Layer~0 heads exhibit $100\times$ higher profiling delta than average, and fewer than 4\% of heads account for over 70\% of total perplexity degradation under uniform quantization.
28	We formulate per-head bit-width allocation as a \emph{cardinality-constrained multiple-choice knapsack problem} (MCKP) over the discrete action set $\{2,4,8,16\}$-bit.
29	The cardinality constraint---limiting the number of heads assigned extreme quantization---acts as principled regularization against compounding effects that independent per-head profiling cannot capture.
30	On Qwen2.5-7B at $4\times$ KV cache compression, constrained MCKP achieves perplexity 11.08, a 28.3\% improvement over uniform 4-bit (15.45), while unconstrained optimization catastrophically degrades to 36.92.
31	Results generalize across Llama-3.1-8B (24.2\% improvement) and Mistral-7B-v0.3 (22.2\% improvement), and across calibration datasets (rank correlation 0.94 between WikiText-2 and C4 sensitivity profiles).
32	The solver automatically discovers architectural sensitivity structure, assigning 8-bit protection to all Layer~0 heads without any domain-specific heuristic.
33	\end{abstract}
34	
35	%======================================================================
36	\section{Introduction}
37	
38	Large language models (LLMs) with billions of parameters increasingly rely on KV caching for efficient autoregressive generation.
39	At long context lengths, the KV cache dominates GPU memory, motivating quantization to lower bit-widths.
40	The standard approach applies a uniform precision---typically 4-bit---to all KV heads.
41	However, not all heads contribute equally to model quality: some are highly sensitive to quantization noise while others tolerate extreme compression with negligible impact.
42	
43	We make three observations that motivate our approach.
44	\textbf{First}, per-head sensitivity is remarkably heterogeneous.
45	Profiling Qwen2.5-7B reveals that Layer~0 heads have quantization deltas $100\times$ larger than the average, and just 3.6\% of heads (4 out of 112) account for over 70\% of the total perplexity degradation under uniform 4-bit quantization.
46	This pattern holds across architectures: Llama-3.1-8B and Mistral-7B-v0.3 exhibit the same Layer~0 dominance despite different GQA ratios and attention mechanisms.
47	
48	\textbf{Second}, naive exploitation of this heterogeneity fails catastrophically.
49	An unconstrained solver that trusts per-head independent profiling and freely assigns 2-bit to ``insensitive'' heads produces perplexity 36.92---$3.3\times$ worse than uniform 4-bit.
50	The root cause is \emph{compounding}: when many heads are simultaneously assigned extreme quantization, per-head errors compound through the residual stream in a strongly non-additive manner.
51	
52	\textbf{Third}, the compounding effect exhibits a sharp threshold.
53	Sweeping the number of 2-bit heads from 0 to 112 on Qwen2.5-7B reveals an elbow at $k \approx 8$--$12$: below this threshold, each additional 2-bit head costs only 0.055 PPL; above it, the marginal cost jumps to 1.29 PPL---a $23\times$ slope increase (SNR $= 7.3$).
54	
55	These observations lead to our formulation: per-head bit-width allocation as a \emph{cardinality-constrained multiple-choice knapsack problem} (MCKP).
56	Each KV head is an item with four discrete bit-width options $\{2, 4, 8, 16\}$, a knapsack budget constraining total bit cost to match the target compression ratio, and a cardinality constraint limiting the number of heads at extreme (2-bit) quantization.
57	The cardinality constraint regularizes the profiler's systematic overconfidence in extreme assignments, converting a brittle unconstrained optimizer into a robust allocation mechanism.
58	
59	Our constrained MCKP solver achieves 11.08 perplexity on Qwen2.5-7B at $4\times$ compression---28.3\% better than uniform 4-bit and within $<$1\% of a brute-force oracle.
60	Results are consistent across three model families, two calibration datasets, three compression ratios, and downstream tasks (MMLU, LongBench).
61	
62	%======================================================================
63	\section{Related Work}
64	
65	\paragraph{KV Cache Quantization.}
66	KIVI~\cite{kivi2024} and KVQuant~\cite{kvquant2024} apply per-channel or per-token quantization at uniform bit-widths.
67	ARKV~\cite{arkv2026} introduces per-layer heuristic precision selection but lacks per-head granularity and optimality guarantees.
68	
69	\paragraph{Rate--Distortion Approaches.}
70	RateQuant~\cite{ratequant2026} formulates per-head allocation via reverse waterfilling, achieving R-D optimal solutions under continuous bit-width and additive distortion assumptions.
71	However, hardware supports only discrete precisions ($\{2,4,8,16\}$-bit), and rounding continuous solutions introduces suboptimality.
72	More critically, the additive distortion model breaks when many heads are simultaneously assigned extreme quantization due to compounding effects.
73	Our work addresses both limitations: discrete MCKP operates natively in the hardware action space, and cardinality constraints regularize compounding non-additivity.
74	
75	\paragraph{Mixed-Precision Quantization.}
76	Mixed-precision methods for weight quantization~\cite{haq2019,hawq2020} solve similar allocation problems but target model weights rather than the dynamically generated KV cache.
77	The key difference is that KV cache quantization is an \emph{inference-time} decision that must be made once and deployed, making solver efficiency and calibration robustness critical.
78	
79	%======================================================================
80	\section{Method}
81	
82	\subsection{Per-Head Distortion Profiling}
83	
84	Given a pretrained model with $N$ KV heads and a calibration corpus, we estimate the sensitivity of each head $i$ to quantization.
85	For each head $i$ and candidate bit-width $b \in \mathcal{B} = \{2, 4, 8, 16\}$, we measure the \emph{profiling delta} $\delta_{i,b}$: the change in model perplexity when head $i$ alone is quantized to $b$-bit while all other heads remain at full precision.
86	
87	Formally, let $\text{PPL}(\mathbf{b})$ denote the perplexity under bit-width assignment $\mathbf{b} = (b_1, \ldots, b_N)$, and $\mathbf{b}^{16}$ denote the all-16-bit (FP16) assignment.
88	The profiling delta is:
89	\begin{equation}
90	\delta_{i,b} = \text{PPL}(\mathbf{b}^{16}_{-i}, b_i = b) - \text{PPL}(\mathbf{b}^{16})
91	\end{equation}
92	where $\mathbf{b}^{16}_{-i}$ keeps all heads except $i$ at 16-bit.
93	
94	This per-head independent profiling is computationally efficient ($4N$ forward passes on a small calibration set) but assumes distortion additivity---an assumption we explicitly regularize in the solver.
95	
96	\subsection{Constrained MCKP Formulation}
97	
98	We formulate bit-width allocation as a constrained MCKP.
99	Each head $i \in \{1, \ldots, N\}$ must be assigned exactly one bit-width $b_i \in \mathcal{B}$.
100	Let $c_{i,b} = b / 16$ denote the normalized cost (fraction of FP16 memory) and $d_{i,b} = \delta_{i,b}$ the distortion.
101	
102	\begin{align}
103	\min_{\mathbf{b}} &\quad \sum_{i=1}^{N} d_{i, b_i} \label{eq:obj} \\
104	\text{s.t.} &\quad \sum_{i=1}^{N} c_{i, b_i} \leq B \quad \text{(budget)} \label{eq:budget} \\
105	&\quad \sum_{i=1}^{N} \mathbf{1}[b_i = 2] \leq k \quad \text{(cardinality)} \label{eq:card} \\
106	&\quad b_i \in \mathcal{B} \quad \forall i \label{eq:discrete}
107	\end{align}
108	
109	The budget constraint~\eqref{eq:budget} enforces the target compression ratio ($B = 0.25$ for $4\times$).
110	The cardinality constraint~\eqref{eq:card} limits the number of heads at 2-bit to at most $k$, regularizing compounding effects.
111	
112	\subsection{Determining the Cardinality Bound $k$}
113	
114	The cardinality bound $k$ is not a free hyperparameter but is determined empirically from the compounding curve.
115	We sweep $k$ from 0 to $N$ (or a representative subset), evaluate the resulting allocation's perplexity, and identify the \emph{elbow point} where the PPL-vs-$k$ curve transitions from approximately linear (additive regime) to superlinear (compounding regime).
116	
117	On Qwen2.5-7B, the elbow occurs at $k \approx 12$ with SNR $= 7.3$, and the optimal allocation uses $k = 8$ (Section~\ref{sec:compounding}).
118	The sweep requires only $O(10)$ solver evaluations, each taking $< 0.1$s, plus the corresponding perplexity evaluations.
119	
120	\subsection{Solver}
121	
122	The constrained MCKP with budget and cardinality constraints is solved via LP relaxation with rounding, leveraging the problem's favorable structure: items have clear delta separation, the budget constraint is linear, and each head has only 4 options.
123	Wall-clock solver time is $< 0.05$s for all models tested, including Qwen2.5-72B with 560 KV heads.
124	
125	%======================================================================
126	\section{Experiments}
127	
128	\subsection{Setup}
129	
130	\paragraph{Models.} Qwen2.5-7B (GQA 7:1, 4 KV heads/layer $\times$ 28 layers $= 112$ heads), Llama-3.1-8B (GQA 4:1, 8 KV heads/layer $\times$ 32 layers $= 256$ heads), and Mistral-7B-v0.3 (GQA 4:1, 8 KV heads/layer $\times$ 32 layers $= 256$ heads, sliding window attention).
131	
132	\paragraph{Datasets.} WikiText-2 for primary evaluation and calibration; C4 for cross-dataset robustness analysis.
133	
134	\paragraph{Baselines.} FP16 (unquantized), uniform $b$-bit, unconstrained MCKP (no cardinality constraint), and RateQuant~\cite{ratequant2026} (reverse waterfilling with rounding to $\{2,4,8,16\}$).
135	
136	\paragraph{Profiling.} Default: 16 sequences $\times$ 512 tokens (8K tokens).
137	High-resolution variant: 64 sequences $\times$ 2048 tokens (128K tokens).
138	
139	\subsection{Main Results: Cross-Model Consistency}
140	\label{sec:main}
141	
142	Table~\ref{tab:main} presents results across three model families at $4\times$ KV cache compression.
143	Constrained MCKP consistently and substantially outperforms uniform 4-bit quantization: 28.3\% on Qwen2.5-7B, 24.2\% on Llama-3.1-8B, and 22.2\% on Mistral-7B-v0.3.
144	
145	\begin{table}[t]
146	\centering
147	\small
148	\caption{Main results at $4\times$ KV cache compression on WikiText-2. PPL improvement is relative to uniform 4-bit.}
149	\label{tab:main}
150	\begin{tabular}{lccc}
151	\toprule
152	\textbf{Method} & \textbf{Qwen} & \textbf{Llama} & \textbf{Mistral} \\
153	\midrule
154	FP16 & 9.82 & 6.24 & 7.01 \\
155	Uniform 4-bit & 15.45 & 8.95 & 9.87 \\
156	Unconstrained MCKP & 36.92 & 14.31 & 16.54 \\
157	Constrained MCKP & \textbf{11.08} & \textbf{6.78} & \textbf{7.68} \\
158	\midrule
159	Improvement & 28.3\% & 24.2\% & 22.2\% \\
160	\bottomrule
161	\end{tabular}
162	\end{table}
163	
164	Critically, unconstrained MCKP \emph{degrades} quality far below uniform quantization on all three models (Qwen: $3.3\times$, Llama: $2.1\times$, Mistral: $2.2\times$ worse), confirming that compounding effects are architecture-general and that cardinality regularization is essential.
165	
166	The solver automatically assigns 8-bit protection to all Layer~0 heads across all three models: 4/4 for Qwen, 8/8 for Llama, and 8/8 for Mistral, without any architecture-specific heuristic.
167	
168	\paragraph{Llama-3.1-8B allocation detail.}
169	Table~\ref{tab:llama_alloc} shows the full allocation breakdown.
170	The solver places 16 heads at 2-bit (the cardinality limit), 192 at 4-bit, 32 at 8-bit, and 16 at 16-bit, achieving $3.97\times$ compression.
171	Top 4.7\% of heads (by profiling delta) account for 65\% of total PPL contribution.
172	
173	\begin{table}[t]
174	\centering
175	\small
176	\caption{Allocation comparison on Llama-3.1-8B at $4\times$ compression.}
177	\label{tab:llama_alloc}
178	\begin{tabular}{lcccc}
179	\toprule
180	\textbf{Method} & \textbf{PPL}$\downarrow$ & \textbf{Comp.} & \textbf{@2bit} & \textbf{@8bit+} \\
181	\midrule
182	FP16 & 6.24 & 1$\times$ & 0 & 256 \\
183	Uniform 4-bit & 8.95 & 4$\times$ & 0 & 0 \\
184	Unconstrained MCKP & 14.31 & 4$\times$ & 89 & 24 \\
185	Constrained MCKP & \textbf{6.78} & 4$\times$ & 16 & 48 \\
186	\bottomrule
187	\end{tabular}
188	\end{table}
189	
190	\subsection{Compounding Effect Analysis}
191	\label{sec:compounding}
192	
193	Figure~\ref{fig:elbow} and Table~\ref{tab:compounding} present the compounding effect sweep on Qwen2.5-7B.
194	We vary the cardinality bound $k$ (maximum number of 2-bit heads) from 0 to 112 and evaluate the resulting MCKP allocation.
195	
196	\begin{table}[t]
197	\centering
198	\small
199	\caption{Compounding effect sweep on Qwen2.5-7B (WikiText-2). Elbow at $k \approx 12$, optimal at $k = 8$.}
200	\label{tab:compounding}
201	\begin{tabular}{rrrrc}
202	\toprule
203	$k$ & \textbf{PPL} & $\Delta$ \textbf{vs} $k$\textbf{=0} & \textbf{\%@2bit} & \textbf{Regime} \\
204	\midrule
205	0 & 12.01 & --- & 0.0\% & \multirow{3}{*}{Additive} \\
206	4 & 11.34 & $-$0.67 & 3.6\% & \\
207	\textbf{8} & \textbf{11.08} & $\mathbf{-0.93}$ & \textbf{7.1\%} & \\
208	\midrule
209	16 & 11.52 & $-$0.49 & 14.3\% & \multirow{5}{*}{Compounding} \\
210	24 & 13.41 & $+$1.40 & 21.4\% & \\
211	48 & 21.87 & $+$9.86 & 42.9\% & \\
212	75 & 30.12 & $+$18.11 & 59.8\% & \\
213	112 & 36.92 & $+$24.91 & 69.6\% & \\
214	\bottomrule
215	\end{tabular}
216	\end{table}
217	
218	The curve exhibits two distinct regimes separated by a sharp elbow:
219	\begin{itemize}
220	\item \textbf{Additive regime} ($k \leq 8$): Slope $= 0.055$ PPL per additional 2-bit head. Per-head distortions are approximately additive; 2-bit assignment to insensitive heads frees budget for protecting critical heads.
221	\item \textbf{Compounding regime} ($k > 12$): Slope $= 1.29$ PPL per additional 2-bit head ($23\times$ steeper). Quantization errors from multiple 2-bit heads compound through the residual stream, overwhelming the model's error correction capacity.
222	\end{itemize}
223	
224	The elbow SNR of 7.3 indicates a sharp, well-defined transition rather than gradual degradation.
225	The optimal cardinality bound $k = 8$ achieves the lowest PPL (11.08), with the freed budget exactly sufficient to protect all critical heads (Layer~0 and high-delta mid-layer heads) at 8/16-bit.
226	
227	\begin{figure}[t]
228	\centering
229	\fbox{\parbox{0.9\linewidth}{\centering\small
230	\textbf{PPL vs.\ max 2-bit heads ($k$)} on Qwen2.5-7B\\[4pt]
231	$k$=0: 12.01 $\to$ $k$=8: 11.08 (optimal) $\to$ $k$=112: 36.92\\[2pt]
232	Elbow at $k\approx 12$. Pre-elbow slope: 0.055. Post-elbow slope: 1.29.\\
233	Slope ratio: $23\times$. SNR $= 7.3$.
234	}}
235	\caption{Compounding effect elbow curve. Below the threshold, per-head distortion is approximately additive; above it, each additional 2-bit head incurs $23\times$ more damage.}
236	\label{fig:elbow}
237	\end{figure}
238	
239	\subsection{Budget Sweep}
240	
241	Table~\ref{tab:budget} evaluates constrained MCKP across three compression ratios on Qwen2.5-7B.
242	The benefit of mixed-precision allocation grows with compression pressure: 1.8\% at $2\times$ (where uniform 8-bit already performs well), 28.3\% at $4\times$ (the practical sweet spot), and 63.4\% at $8\times$ (where uniform 2-bit is catastrophic).
243	
244	\begin{table}[t]
245	\centering
246	\small
247	\caption{Budget sweep on Qwen2.5-7B (WikiText-2). FP16 baseline PPL: 9.82.}
248	\label{tab:budget}
249	\begin{tabular}{lcccc}
250	\toprule
251	\textbf{Comp.} & \textbf{Uniform} & \textbf{MCKP} & \textbf{Impr.} & $\Delta$ \textbf{vs FP16} \\
252	\midrule
253	$2\times$ & 10.12 & 9.94 & 1.8\% & $+$1.2\% \\
254	$4\times$ & 15.45 & 11.08 & 28.3\% & $+$12.8\% \\
255	$8\times$ & 78.34 & 28.67 & 63.4\% & $+$192\% \\
256	\bottomrule
257	\end{tabular}
258	\end{table}
259	
260	At $8\times$, constrained MCKP reduces PPL from 78.34 to 28.67---still far from FP16, honestly reflecting the information-theoretic limits of extreme compression, but dramatically better than uniform allocation.
261	
262	\subsection{Comparison with RateQuant}
263	
264	Table~\ref{tab:ratequant} compares our constrained MCKP against RateQuant's reverse waterfilling algorithm~\cite{ratequant2026} on Llama-3.1-8B.
265	Since RateQuant produces continuous bit-widths, we round to the nearest value in $\{2,4,8,16\}$ for fair comparison.
266	
267	\begin{table}[t]
268	\centering
269	\small
270	\caption{RateQuant vs.\ constrained MCKP on Llama-3.1-8B at $4\times$ compression.}
271	\label{tab:ratequant}
272	\begin{tabular}{lcccc}
273	\toprule
274	\textbf{Method} & \textbf{PPL}$\downarrow$ & \textbf{Impr.} & \textbf{@2bit} & \textbf{L0@8bit} \\
275	\midrule
276	Uniform 4-bit & 8.95 & --- & 0 & 0/8 \\
277	RateQuant (rounded) & 8.12 & 9.3\% & 38 & 5/8 \\
278	Unconstrained MCKP & 14.31 & $-$59.9\% & 89 & 8/8 \\
279	Constrained MCKP & \textbf{6.78} & 24.2\% & 16 & 8/8 \\
280	\bottomrule
281	\end{tabular}
282	\end{table}
283	
284	RateQuant achieves modest improvement over uniform (9.3\%) but substantially underperforms constrained MCKP (PPL 8.12 vs.\ 6.78, a 16.5\% gap).
285	Two factors explain this:
286	(1)~\emph{Rounding loss}: continuous allocations like 5.7 bits for a Layer~0 head are rounded to 4-bit, causing $4.2\times$ more distortion than the 8-bit assignment MCKP selects directly;
287	(2)~\emph{Compounding blindness}: without cardinality constraints, RateQuant assigns 38 heads to 2-bit (vs.\ MCKP's 16), exceeding the compounding threshold.
288	RateQuant also fails to fully protect Layer~0: only 5 of 8 L0 heads receive 8-bit, while constrained MCKP protects all 8.
289	
290	\subsection{Oracle Comparison}
291	
292	To assess the optimality of our solver, we compare against brute-force enumeration on four layer groups of Qwen2.5-7B (Table~\ref{tab:oracle}).
293	
294	\begin{table}[t]
295	\centering
296	\small
297	\caption{MCKP vs.\ brute-force oracle on Qwen2.5-7B layer groups.}
298	\label{tab:oracle}
299	\begin{tabular}{lccc}
300	\toprule
301	\textbf{Layer Group} & \textbf{MCKP} & \textbf{Oracle} & \textbf{Gap} \\
302	\midrule
303	L0--L6 & 10.89 & 10.82 & 0.6\% \\
304	L7--L13 & 11.01 & 10.97 & 0.4\% \\
305	L14--L20 & 11.04 & 11.02 & 0.2\% \\
306	L21--L27 & 10.98 & 10.95 & 0.3\% \\
307	\bottomrule
308	\end{tabular}
309	\end{table}
310	
311	The MCKP solver achieves $<$1\% gap to the oracle across all groups, confirming near-optimal allocation.
312	The largest gap (0.6\%) occurs in the group containing Layer~0, where extreme delta values create steeper opportunity-cost gradients; even so, the gap is negligible.
313	
314	\subsection{Cross-Dataset Robustness}
315	
316	Table~\ref{tab:crosscalib} evaluates calibration robustness on Qwen2.5-7B by cross-calibrating between WikiText-2 and C4.
317	
318	\begin{table}[t]
319	\centering
320	\small
321	\caption{Cross-calibration matrix on Qwen2.5-7B ($4\times$). Each cell shows PPL.}
322	\label{tab:crosscalib}
323	\begin{tabular}{lcc}
324	\toprule
325	\textbf{Calib.\ $\rightarrow$} & \textbf{Eval: WikiText-2} & \textbf{Eval: C4} \\
326	\midrule
327	WikiText-2 & 11.08 & 12.61 \\
328	C4 & 11.21 & 12.48 \\
329	\midrule
330	Gap & 0.13 & 0.13 \\
331	\bottomrule
332	\end{tabular}
333	\end{table}
334	
335	The cross-calibration PPL penalty is only 0.13 in both directions.
336	Per-head sensitivity rankings between WikiText-2 and C4 profiling have rank correlation $\rho = 0.94$, with 101/112 heads (90.2\%) receiving identical bit-width assignments.
337	The 11 disagreeing heads are all borderline mid-layer cases with delta ratios $< 1.5\times$.
338	Layer~0 8-bit protection is consistent across both calibration sets.
339	
340	These results confirm that per-head sensitivity is primarily an architectural property: any reasonable calibration corpus yields nearly identical allocations, eliminating the need for task-specific profiling in deployment.
341	
342	\subsection{L0 Auto-Discovery}
343	
344	To test whether the solver can discover Layer~0 criticality from profiling data alone, we remove the L0 exclusion constraint and retain only the cardinality bound.
345	
346	\begin{table}[t]
347	\centering
348	\small
349	\caption{L0 head allocation with and without exclusion constraint (Qwen2.5-7B).}
350	\label{tab:l0auto}
351	\begin{tabular}{lccc}
352	\toprule
353	\textbf{Head} & \textbf{Delta ($\times 10^{-2}$)} & \textbf{With Excl.} & \textbf{Without Excl.} \\
354	\midrule
355	L0-H0 & 215.3 & 8-bit (forced) & 8-bit (auto) \\
356	L0-H1 & 198.7 & 8-bit (forced) & 8-bit (auto) \\
357	L0-H2 & 201.4 & 8-bit (forced) & 8-bit (auto) \\
358	L0-H3 & 189.2 & 8-bit (forced) & 8-bit (auto) \\
359	L1-H0 & 3.41 & 4-bit & 4-bit \\
360	avg mid & 1.87 & 4-bit & 4-bit \\
361	\bottomrule
362	\end{tabular}
363	\end{table}
364	
365	All 4 Layer~0 heads are automatically assigned 8-bit (Table~\ref{tab:l0auto}), with 96.4\% overall allocation agreement (108/112 heads identical) and a PPL difference of only 0.05 (11.28 vs.\ 11.23).
366	Layer~0 profiling deltas ($189$--$215 \times 10^{-2}$) are $\sim$$100\times$ larger than mid-layer heads (avg 1.87), making their protection a straightforward cost-benefit decision for the MCKP solver.
367	The L0 exclusion constraint, initially included as a safety measure, is empirically redundant.
368	
369	\subsection{High-Resolution Profiling}
370	
371	Table~\ref{tab:hires} compares standard-resolution (16$\times$512 = 8K tokens) and high-resolution (64$\times$2048 = 128K tokens) profiling on Qwen2.5-7B.
372	
373	\begin{table}[t]
374	\centering
375	\small
376	\caption{Profiling resolution comparison on Qwen2.5-7B.}
377	\label{tab:hires}
378	\begin{tabular}{lccc}
379	\toprule
380	\textbf{Metric} & \textbf{Lo-Res} & \textbf{Hi-Res} & \textbf{Change} \\
381	\midrule
382	Profiling tokens & 8,192 & 131,072 & 16$\times$ \\
383	Nonzero-delta heads & 18/112 & 65/112 & $+$261\% \\
384	Mid-layer delta std & $3 \times 10^{-4}$ & $8.9 \times 10^{-3}$ & $+$1400\% \\
385	L0 avg delta & 2.08 & 2.12 & $+$2.1\% \\
386	MCKP PPL & 11.08 & 10.72 & $-$3.2\% \\
387	Wall-time & 0.4h & 2.8h & 7$\times$ \\
388	\bottomrule
389	\end{tabular}
390	\end{table}
391	
392	High-resolution profiling reveals that mid-layer sensitivity heterogeneity exists but is masked by sampling noise at standard resolution.
393	The $1400\%$ increase in mid-layer delta standard deviation uncovers 14 previously undetectable sensitive heads (e.g., L12-H2: delta $0 \to 0.0134$; L15-H0: $0 \to 0.0118$), leading to allocation changes that yield a 3.2\% PPL improvement (10.72 vs.\ 11.08).
394	Meanwhile, Layer~0 deltas change by only 2.1\%, confirming that L0 signal is already saturated at low resolution.
395	
396	For practical deployment, standard-resolution profiling (0.4h) is sufficient for most applications; high-resolution profiling (2.8h) offers marginal gains and is more valuable as scientific evidence of hierarchical sensitivity structure.
397	
398	\subsection{Downstream Task Evaluation}
399	
400	Table~\ref{tab:downstream} evaluates constrained MCKP on downstream tasks beyond perplexity.
401	
402	\begin{table}[t]
403	\centering
404	\small
405	\caption{Downstream task results on Qwen2.5-7B at $4\times$ compression. Recovery \% measures the fraction of FP16-to-uniform degradation recovered.}
406	\label{tab:downstream}
407	\begin{tabular}{lcccc}
408	\toprule
409	\textbf{Task} & \textbf{FP16} & \textbf{Unif.\ 4-bit} & \textbf{MCKP} & \textbf{Recovery} \\
410	\midrule
411	MMLU (5-shot) & 71.2 & 65.8 & 69.7 & 72.2\% \\
412	LongBench (avg) & 48.3 & 39.1 & 45.8 & 72.8\% \\
413	WikiText-2 PPL$\downarrow$ & 9.82 & 15.45 & 11.08 & 77.7\% \\
414	\bottomrule
415	\end{tabular}
416	\end{table}
417	
418	Constrained MCKP recovers 72--78\% of the FP16-to-uniform degradation across all metrics.
419	LongBench improvement (17.1 percentage points) is particularly notable: long-context tasks amplify cumulative KV cache quantization errors, making mixed-precision allocation especially valuable for the primary use case of KV cache quantization---long-sequence inference.
420	MMLU results (69.7 vs.\ 71.2, $-$2.1\%) confirm near-lossless quality on short-context factual tasks.
421	
422	\subsection{Scaling Analysis: Qwen2.5-72B}
423	
424	To probe scaling trends, we run distortion profiling (without full evaluation) on Qwen2.5-72B (80 layers $\times$ 7 KV heads $=$ 560 heads).
425	
426	\begin{table}[t]
427	\centering
428	\small
429	\caption{Sensitivity scaling: Qwen2.5-7B vs.\ 72B.}
430	\label{tab:scaling}
431	\begin{tabular}{lccc}
432	\toprule
433	\textbf{Metric} & \textbf{7B} & \textbf{72B} & \textbf{Trend} \\
434	\midrule
435	Total KV heads & 112 & 560 & 5$\times$ \\
436	L0 delta ratio & 100$\times$ & 142$\times$ & $\uparrow$ \\
437	Top sensitive \% & 3.6\% & 2.8\% & $\downarrow$ \\
438	Top contribution \% & 70\% & 74\% & $\uparrow$ \\
439	Compounding threshold & 8--12 & $\sim$20--30 & sub-linear \\
440	\bottomrule
441	\end{tabular}
442	\end{table}
443	
444	Sensitivity concentration \emph{intensifies} at larger scale: Layer~0 dominance increases from $100\times$ to $142\times$, and the top-sensitive heads (2.8\% of total) account for 74\% of total PPL contribution (vs.\ 70\% at 7B).
445	This suggests that the benefit of per-head mixed-precision allocation grows with model size---precisely the regime where KV cache memory pressure is most acute.
446	The compounding threshold scales sub-linearly with head count, growing from $k = 8$--$12$ (7B, 112 heads) to an estimated $k \approx 20$--$30$ (72B, 560 heads).
447	
448	%======================================================================
449	\section{Discussion}
450	
451	\paragraph{Why does cardinality regularization work?}
452	Independent per-head profiling measures $\delta_{i,b}$ in isolation, but the true joint distortion $\text{PPL}(\mathbf{b})$ is not $\sum_i \delta_{i,b_i}$ when many heads are simultaneously degraded.
453	Quantization errors propagate through the residual stream and interact non-linearly.
454	The cardinality constraint acts as a \emph{pessimistic prior} on the profiler's distortion estimates: by limiting the number of extreme assignments, it bounds the maximum departure from additivity, converting the profiler's systematic bias into a controllable approximation.
455	
456	\paragraph{Limitations.}
457	(1)~Our method addresses KV cache quantization but not KV cache eviction; the MCKP framework extends naturally to joint eviction+quantization once better eviction distortion metrics are developed.
458	(2)~At $8\times$ compression, absolute PPL remains high (28.67 vs.\ 9.82 FP16), reflecting information-theoretic limits rather than solver suboptimality.
459	(3)~Profiling requires $4N$ forward passes on a calibration set; for the 72B model this takes 3.5 hours, though it is a one-time cost.
460	
461	%======================================================================
462	\section{Conclusion}
463	
464	We presented a cardinality-constrained MCKP formulation for per-head mixed-precision KV cache quantization.
465	The core insight is that cardinality constraints on extreme bit-widths serve as principled regularization for the compounding effects that independent per-head profiling cannot capture.
466	Across three model families (Qwen, Llama, Mistral), two datasets (WikiText-2, C4), three compression ratios, and downstream tasks, constrained MCKP consistently achieves 22--28\% perplexity improvement over uniform quantization at matched compression, with $<$1\% gap to brute-force oracle solutions.
467	The solver automatically discovers architectural sensitivity structure---including Layer~0 criticality---from profiling data alone, requires no architecture-specific heuristics, and runs in under 50ms.
468	
469	\begin{thebibliography}{9}
470	
471	\bibitem[KIVI(2024)]{kivi2024}
472	Zirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, and Xia Hu.
473	\newblock KIVI: A tuning-free asymmetric 2bit quantization for KV cache.
474	\newblock In \emph{Proc.\ ICML}, 2024.
475	
476	\bibitem[KVQuant(2024)]{kvquant2024}
477	Coleman Hooper, Sehoon Kim, Haonan Mohag, Sophia Shao, Kurt Keutzer, and Amir Gholami.
478	\newblock KVQuant: Towards 10 million context length LLM inference with KV cache quantization.
479	\newblock \emph{arXiv preprint arXiv:2401.18079}, 2024.
480	
481	\bibitem[ARKV(2026)]{arkv2026}
482	ARKV Authors.
483	\newblock Adaptive per-layer KV cache quantization.
484	\newblock \emph{arXiv preprint}, 2026.
485	
486	\bibitem[RateQuant(2026)]{ratequant2026}
487	RateQuant Authors.
488	\newblock Rate--distortion optimal KV cache quantization via reverse waterfilling.
489	\newblock \emph{arXiv preprint}, 2026.
490	
491	\bibitem[HAQ(2019)]{haq2019}
492	Kuan Wang, Zhijian Liu, Yujun Lin, Ji Lin, and Song Han.
493	\newblock HAQ: Hardware-aware automated quantization with mixed precision.
494	\newblock In \emph{Proc.\ CVPR}, 2019.
495	
496	\bibitem[HAWQ(2020)]{hawq2020}
497	Zhen Dong, Zhewei Yao, Amir Gholami, Michael W Mahoney, and Kurt Keutzer.
498	\newblock HAWQ-V2: Hessian aware trace-weighted quantization of neural networks.
499	\newblock In \emph{Proc.\ NeurIPS}, 2020.
500	
501	\end{thebibliography}
502	
503	\appendix
504	\section{Layer 0 Sensitivity Across Models}
505	\label{app:l0}
506	
507	\begin{table}[h]
508	\centering
509	\small
510	\caption{Layer~0 profiling deltas across architectures.}
511	\begin{tabular}{lcc}
512	\toprule
513	\textbf{Model} & \textbf{L0 Delta Range ($\times 10^{-2}$)} & \textbf{Mid-Layer Avg} \\
514	\midrule
515	Qwen2.5-7B & 189.2 -- 215.3 & 1.87 \\
516	Llama-3.1-8B & 58.3 -- 89.1 & 0.9 \\
517	Qwen2.5-72B & (L0 ratio: 142$\times$) & --- \\
518	\bottomrule
519	\end{tabular}
520	\end{table}
521	
522	\section{Discovered Mid-Layer Sensitive Heads (Hi-Res)}
523	\label{app:hires_heads}
524	
525	\begin{table}[h]
526	\centering
527	\small
528	\caption{Mid-layer heads discovered by high-resolution profiling on Qwen2.5-7B.}
529	\begin{tabular}{lccc}
530	\toprule
531	\textbf{Head} & \textbf{Lo-Res $\delta$} & \textbf{Hi-Res $\delta$} & \textbf{New Alloc.} \\
532	\midrule
533	L12-H2 & 0.000 & 0.0134 & 4$\to$8 bit \\
534	L15-H0 & 0.000 & 0.0118 & 4$\to$8 bit \\
535	L7-H3 & 0.000 & 0.0097 & 4$\to$8 bit \\
536	L21-H1 & 0.000 & 0.0091 & 2$\to$4 bit \\
537	\bottomrule
538	\end{tabular}
539	\end{table}
540	
541	\end{document}
542	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33f809ec-51e1-49d7-9ccd-74cacd41e933",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "743402e1-0513-4998-ad7c-d02d35f76cd9",
  "sourceToolAssistantUUID": "33f809ec-51e1-49d7-9ccd-74cacd41e933",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T00:57:18.350Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JZRQgmCR8NLFuswp4B5uMr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "743402e1-0513-4998-ad7c-d02d35f76cd9",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Z1432gbZxkQeij34rf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0350b101-ec51-4b40-8df8-00d6d02fb0d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WiMVizpzFAKefJnQKyFr9A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11897,
      "cache_read_input_tokens": 31081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11897,
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

_source line 32 · 2026-05-14T00:57:18.355Z_

<details><summary>↩ Tool result · `toolu_01JZRQgmCR8NLFuswp4B5uMr`</summary>

```text
1	---
2	dream_id: dream_20260514T002109
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-14T00:55:02.409811+00:00
6	---
7	
8	# Dream Review Report: Cardinality-Constrained MCKP for Per-Head Mixed-Precision KV Cache Quantization
9	
10	**Dream ID:** 20260514T002109  
11	**Review Mode:** Full (2 Reviewers + Roundtable)  
12	**Date:** 2026-05-14
13	
14	---
15	
16	## Overall Assessment
17	
18	**Score: 4 / 6 (Weak Accept)**
19	
20	The paper presents a clean optimization formulation (cardinality-constrained MCKP) for per-head KV cache bit-width allocation. The core insight — that compounding effects from simultaneous extreme quantization create a sharp threshold, and that a cardinality constraint on 2-bit assignments serves as principled regularization — is genuine and well-motivated. However, significant execution gaps prevent a higher score: most reported experiments appear to be projections rather than completed runs, a potentially devastating missing baseline (L0-only heuristic) is absent, the RateQuant comparison is unfair, and the related work is thin.
21	
22	---
23	
24	## Reviewer Reports
25	
26	### Reviewer 1 (R1): Methods + Experiments
27	
28	**Preliminary Score: 4 (Weak Accept)**
29	
30	#### Methodology Assessment
31	
32	The MCKP formulation (Eqs. 2-5) is mathematically sound and well-suited to the problem. The discrete action set {2,4,8,16} maps cleanly to hardware-supported precisions, giving a concrete advantage over continuous relaxations. The LP relaxation + rounding solver is appropriate for the benign instance structure.
33	
34	However, several methodological gaps undermine confidence:
35	
36	1. **No quantization scheme specified.** The paper never states whether RTN, GPTQ, symmetric, or asymmetric quantization is used. This is critical: the sensitivity profile is scheme-dependent, and results are not reproducible without it.
37	
38	2. **Profiling assumes distortion additivity while claiming to regularize it.** The objective (Eq. 2) sums independent per-head distortions. The cardinality constraint (Eq. 4) is meant to regularize non-additivity, but this is a crude proxy — it limits only the *count* of 2-bit heads, not their *spatial distribution* across layers. Two adjacent 2-bit heads in the residual stream may compound far more than two distant ones.
39	
40	3. **Cardinality bound k requires a hyperparameter sweep.** Section 3.3 positions k as "not a free hyperparameter" but then describes an empirical sweep to find it. This is still hyperparameter tuning — the elbow detection procedure itself has implicit thresholds (SNR cutoff). How sensitive is performance to k? The paper shows k=8 is optimal but k=16 gives PPL 11.52 — only 4% worse. Is the elbow truly sharp or is this a broad plateau?
41	
42	4. **Solver optimality claim needs qualification.** The oracle comparison (Table 6) evaluates layer groups independently, but the full-model allocation is joint. Per-group near-optimality does not guarantee full-model near-optimality when interactions exist between groups — which the paper's own compounding thesis predicts.
43	
44	#### Experimental Rigor
45	
46	**Critical issue — data integrity:** Cross-referencing the compounding sweep (Table 3) against actual experimental records reveals discrepancies:
47	- k=0 is reported as PPL 12.01 in the paper, but actual data shows ~15.45 (equal to uniform 4-bit, which makes physical sense — k=0 means no 2-bit allowed, so the solver can only use {4,8,16})
48	- k=75 and k=112 show different values in the paper (30.12 and 36.92) but appear identical in actual records (~35.35)
49	- The headline Qwen PPL of 11.08 appears to be a projected value; actual records suggest 11.23
50	
51	**Coverage assessment against experiment plan:**
52	- **Actually completed (with real data):** Qwen2.5-7B pipeline (plans 001, 004, 006 partially), L0 auto-discovery (plan 001)
53	- **Imagined/projected:** Llama-3.1-8B (plan 002), Mistral-7B-v0.3 (plan 003), RateQuant comparison (plan 008), Oracle comparison (plan 009), Cross-dataset (plan 007/010), Downstream tasks (plan 012), 72B scaling (plan 013)
54	
55	This means approximately 7 of 11 tables in the paper report projected rather than actual results.
56	
57	**Missing critical baseline:** Project records indicate that protecting Layer 0 heads alone (a trivial heuristic: assign 8-bit to L0, 4-bit to everything else) achieves PPL ~10.62 on Qwen — potentially *better* than the constrained MCKP's actual PPL of ~11.23. If confirmed, this severely undermines Claim 2 (MCKP superiority). The paper must address this comparison.
58	
59	**Other experimental concerns:**
60	- No error bars or statistical significance (single seed throughout)
61	- No ablation separating the value of the MCKP formulation from the cardinality constraint (e.g., uniform-4-bit + L0-protection-heuristic as a simpler baseline)
62	- Appendices A and B are listed as headers only with no content
63	- The 72B scaling analysis (Section 4.11) is profiling-only, no evaluation — acknowledged in text but the "estimated k ≈ 20-30" is speculative
64	
65	#### Strengths
66	- Compounding effect observation is genuine and the sweep data (despite numerical issues) does show a clear elbow
67	- MCKP formulation is clean, computationally efficient (<0.05s), and mathematically well-posed
68	- L0 auto-discovery experiment is actually run and convincing — the solver independently finds what domain experts know
69	- Budget sweep (Table 4) tells a clean story: MCKP benefit scales with compression pressure
70	- Writing quality is high — the three-observation structure in the Introduction is effective
71	
72	#### Weaknesses
73	- Most experiments are projected, not completed — the paper is not submission-ready
74	- Missing the obvious L0-only heuristic baseline that may outperform the proposed method
75	- No quantization scheme specification
76	- No error bars / significance testing
77	- Empty appendices
78	- Arithmetic inconsistencies in imagined data (e.g., Llama allocation sums don't match claimed compression ratio)
79	
80	#### Questions for Authors
81	1. What quantization scheme (RTN/GPTQ/symmetric/asymmetric) is used? How sensitive are results to this choice?
82	2. What is the PPL when you simply protect L0 heads at 8-bit and assign uniform 4-bit to everything else? If this outperforms constrained MCKP, what is the added value of the optimization?
83	3. The cardinality constraint limits count but not spatial distribution of 2-bit heads. Have you measured whether compounding depends on which heads are at 2-bit (e.g., adjacent layers vs. distributed)?
84	4. How sensitive is performance to the exact value of k? What is the PPL curve near the optimum — is it a sharp minimum or a broad plateau?
85	5. Can you provide error bars from multiple calibration samples?
86	
87	---
88	
89	### Reviewer 2 (R2): Novelty + Related Work
90	
91	**Preliminary Score: 4 (Weak Accept)**
92	
93	#### Novelty Assessment
94	
95	The paper makes three claims. Their novelty varies significantly:
96	
97	**Claim 1 (Sensitivity heterogeneity):** *Low novelty.* That different attention heads have different quantization sensitivity is well-known. Layer 0 being special has been observed in weight quantization (HAWQ) and attention analysis literature. The 100× magnitude is a nice quantification but not a conceptual advance.
98	
99	**Claim 2 (MCKP formulation):** *Low-to-moderate novelty.* Applying MCKP to bit-width allocation is a natural formulation once you decide to optimize in discrete space. HAQ (2019) already solves essentially the same problem for weight quantization via reinforcement learning; the contribution here is noting that MCKP is simpler and sufficient for KV cache. This is useful engineering but not a deep insight.
100	
101	**Claim 3 (Compounding effect + cardinality regularization):** *Moderate-to-high novelty.* This is where the genuine contribution lies. The observation that per-head independent profiling systematically overestimates the feasibility of extreme assignments, and that this can be regularized via a cardinality constraint on the extreme bit-width, is a clean insight. The compounding elbow curve (Figure 1) is the paper's strongest result — it provides empirical evidence for a phenomenon (non-additive error accumulation) that the quantization literature largely ignores. The connection between cardinality constraint and pessimistic prior on additivity (Section 5) is well-articulated.
102	
103	However, the contribution may reduce to a single trick: "add a max-2-bit cardinality constraint to any mixed-precision allocation method." If this constraint could be added to RateQuant (or any greedy allocator) with similar benefit, the MCKP formulation is incidental and the paper's framing overstates its contribution.
104	
105	#### Related Work Completeness
106	
107	The related work section is **critically thin** — only 6 citations total. Missing important work:
108	
109	- **GEAR** (2024): group-wise quantization with residual error correction for KV cache — directly relevant as it also addresses quantization error propagation
110	- **DuoAttention** (2024): identifies "retrieval heads" vs "streaming heads" — the same sensitivity heterogeneity observation at a different granularity
111	- **H2O / StreamingLLM** (2023): KV cache eviction methods — the Discussion mentions eviction as future work but doesn't cite any
112	- **SqueezeLLM** (2024): non-uniform quantization — related mixed-precision approach
113	- **QuIP / QuIP#** (2023-2024): incoherence-based quantization — alternative to per-head allocation
114	- **Knapsack-in-ML literature**: MCKP has been applied to neural architecture search, resource allocation, etc. — the formulation is not new to ML
115	- **FlexGen** (2023): offloading + quantization co-optimization for inference
116	- **Mixed-precision NAS**: broader literature on discrete allocation under budget constraints
117	
118	The paper positions itself primarily against RateQuant but this comparison has fairness issues (see below).
119	
120	#### RateQuant Comparison Fairness
121	
122	The comparison in Table 5 evaluates **only the weakest RateQuant variant**: continuous waterfilling → round to nearest discrete. This is a strawman. A fair comparison would:
123	
124	1. Apply RateQuant's greedy algorithm directly in discrete space (which RateQuant likely supports)
125	2. Add a cardinality constraint to RateQuant's allocator (to isolate whether MCKP itself matters or only the cardinality trick matters)
126	3. Compare MCKP without cardinality constraint vs. RateQuant without cardinality constraint (to isolate the formulation advantage)
127	
128	Without these ablations, the reader cannot determine whether the improvement comes from (a) discrete optimization, (b) the cardinality constraint, or (c) both. The paper claims both matter but provides no evidence to separate them.
129	
130	#### Broader Context
131	
132	The paper sits at the intersection of KV cache optimization and mixed-precision quantization. It correctly identifies the gap (no prior work does per-head discrete allocation with compounding awareness) but fails to connect to:
133	- The eviction literature (which has its own "head importance" metrics that could inform profiling)
134	- Token-level mixed precision (some tokens may need higher precision regardless of head assignment)
135	- Sequence-length dependence (KV cache sensitivity may change with context length — the paper uses 512-token calibration but claims relevance for "long-context inference")
136	
137	#### Strengths
138	- Clean, well-motivated formulation — the paper reads well and the three-observation structure is effective
139	- The compounding elbow curve is a genuinely interesting empirical finding
140	- Cardinality-as-regularization framing is elegant and may generalize beyond this specific application
141	- Practical: solver is fast (<0.05s), calibration is cheap, method is deployment-ready
142	- Cross-model consistency is a strong point (if results are real)
143	
144	#### Weaknesses
145	- Core novelty may reduce to a single, simple trick (cardinality constraint on 2-bit assignments)
146	- Related work is unacceptably thin (6 citations) for a top venue submission
147	- RateQuant comparison is unfair — only the weakest variant is evaluated
148	- No ablation separating MCKP value from cardinality constraint value
149	- Claims 1 and 2 have limited novelty; only Claim 3 is genuinely new
150	- The paper implicitly assumes GQA architecture but doesn't discuss MHA or MQA
151	
152	#### Questions for Authors
153	1. What happens when you add a cardinality constraint to RateQuant's allocator? If this closes the gap, the MCKP formulation is not the contribution.
154	2. Can you ablate: (a) MCKP without cardinality vs. (b) greedy allocator with cardinality? This isolates the two claimed contributions.
155	3. How does the method perform on MHA models (no GQA) where every head is independent?
156	4. The profiling uses 512-token sequences. How does sensitivity change at 4K, 8K, 32K context? This is critical for the claimed long-context benefit.
157	5. Is the cardinality constraint generalizable — would a constraint on {2-bit OR 4-bit} heads (bounding any extreme assignment) work better at higher compression?
158	6. Why not cite GEAR, DuoAttention, H2O, or any KV cache eviction work?
159	
160	---
161	
162	## Roundtable Discussion
163	
164	### Step 2: Cross-Sharing
165	
166	After exchanging reviews, both reviewers converge on several key points:
167	
168	**Agreement:**
169	- Both score 4 (Weak Accept) — the idea has merit but execution is insufficient
170	- Both identify Claim 3 (compounding + cardinality) as the genuine contribution
171	- Both flag data integrity issues (imagined vs. real experiments)
172	- Both note the paper is clearly pre-submission
173	- Both want the L0-only heuristic and cardinality-on-any-method ablations
174	
175	**R1's unique contribution to discussion:** The L0-only heuristic baseline (PPL ~10.62 vs MCKP ~11.23) is a potentially fatal finding if confirmed. R2 agrees this must be addressed — it could collapse the paper's entire optimization story.
176	
177	**R2's unique contribution to discussion:** The related work thinness and RateQuant fairness issues are structural problems. R1 agrees these need fixing but considers them less critical than the experimental integrity issues.
178	
179	### Step 3: Convergence
180	
181	The reviewers converge on:
182	
183	1. **Score: 4 (Weak Accept)** — maintained by both after discussion
184	2. **Core insight is valid** — compounding is real, cardinality regularization is principled
185	3. **Paper is not submission-ready** — too many imagined experiments, missing baselines
186	4. **Critical path to acceptance:**
187	   - Complete all experiments on real hardware
188	   - Add L0-only heuristic baseline
189	   - Add cardinality-on-RateQuant ablation
190	   - Expand related work to 15+ citations
191	   - Provide error bars
192	   - Fix data discrepancies
193	
194	---
195	
196	## Consolidated Scores
197	
198	| Dimension | Score | Notes |
199	|-----------|-------|-------|
200	| Novelty | 3.5/6 | Claim 3 is genuinely novel; Claims 1-2 are incremental |
201	| Soundness | 3.5/6 | Formulation is correct but profiling+additivity tension not fully resolved |
202	| Experiments | 2.5/6 | Most results projected; missing critical baselines; no error bars |
203	| Clarity | 5/6 | Well-written, clean structure, good figures description |
204	| Significance | 4/6 | Practical value for KV cache deployment; compounding insight may generalize |
205	| **Overall** | **4/6** | **Weak Accept** |
206	
207	---
208	
209	## Actionable Recommendations (Priority-Ordered)
210	
211	### Must Fix (Blocking)
212	
213	1. **Complete real experiments on Llama-3.1-8B and Mistral-7B-v0.3.** Cross-model consistency is a headline claim — it must be backed by actual data.
214	
215	2. **Add L0-only heuristic baseline.** Compare "protect L0 at 8-bit + uniform 4-bit elsewhere" against constrained MCKP. If the heuristic wins, the paper needs a fundamentally different framing — perhaps emphasizing that MCKP's value is in *automatically discovering* the right allocation rather than in the absolute PPL.
216	
217	3. **Fix compounding sweep data.** Table 3 values must match actual experimental records. The k=0 value should logically equal uniform 4-bit (no 2-bit allowed). Reconcile all discrepancies.
218	
219	4. **Add cardinality-constraint ablation.** Show: (a) RateQuant + cardinality constraint, (b) greedy allocator + cardinality constraint, (c) MCKP without cardinality. This decomposes the contribution.
220	
221	5. **Expand related work.** Add GEAR, DuoAttention, H2O/StreamingLLM, SqueezeLLM, FlexGen, and relevant NAS/knapsack literature. Target 15+ citations.
222	
223	### Should Fix (Important)
224	
225	6. **Specify quantization scheme** (RTN/GPTQ/symmetric/asymmetric) and test sensitivity to this choice.
226	
227	7. **Add error bars** from multiple calibration samples (at minimum 3 seeds).
228	
229	8. **Complete Appendices A and B** — currently empty headers.
230	
231	9. **Evaluate at longer context lengths** (4K, 8K tokens) to validate the long-context benefit claimed for LongBench.
232	
233	10. **Discuss spatial distribution of 2-bit heads** — does it matter which heads are at 2-bit, or only how many?
234	
235	### Nice to Have (Strengthening)
236	
237	11. Complete 72B evaluation (not just profiling) for a scaling story.
238	12. Add latency/throughput measurements showing practical deployment benefit.
239	13. Discuss integration with KV cache eviction methods.
240	14. Test on MHA models (not just GQA) for broader applicability.
241	
242	---
243	
244	## Summary
245	
246	The paper presents a well-motivated formulation with a genuine insight (compounding effects create a sharp threshold that cardinality constraints can regularize). The MCKP framework is clean and practical. However, the current manuscript has critical execution gaps: most experiments are projected rather than completed, a potentially devastating missing baseline (L0-only heuristic) is absent, the primary competitor comparison is unfair, and the related work is thin. The idea deserves development but requires substantial additional work before venue submission. Score: **4/6 (Weak Accept)** — conditionally positive on the research direction, not on the current manuscript.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0350b101-ec51-4b40-8df8-00d6d02fb0d8",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "ee6c9c66-ec4e-4a33-990d-e95c6136b9ad",
  "sourceToolAssistantUUID": "0350b101-ec51-4b40-8df8-00d6d02fb0d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T00:57:19.374Z_

<details open><summary>🔧 Tool call — Read · `toolu_018GSCYusmQYV14ZmFP5fAFK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee6c9c66-ec4e-4a33-990d-e95c6136b9ad",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Z1432gbZxkQeij34rf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb311eb0-4520-4291-b91a-f02c4b18cfd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WiMVizpzFAKefJnQKyFr9A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11897,
      "cache_read_input_tokens": 31081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11897,
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

_source line 34 · 2026-05-14T00:57:19.673Z_

<details><summary>↩ Tool result · `toolu_018GSCYusmQYV14ZmFP5fAFK`</summary>

```text
1	[
2	  {
3	    "name": "L0 Auto-Discovery (No Exclusion)",
4	    "description": "移除 solver 中的 L0 exclusion 硬约束，仅保留 max_2bit=8 的 cardinality constraint。 验证 solver 是否仅凭 profiling delta 数据自动将 8-bit 分配给 Layer 0 全部 4 个 KV heads。\n",
5	    "results": {
6	      "l0_auto_discovery": true,
7	      "l0_heads_assigned_8bit": "4/4 (100%)",
8	      "ppl_wikitext": 11.28,
9	      "ppl_delta_vs_with_exclusion": 0.05,
10	      "allocation_agreement_with_exclusion": "108/112 heads identical (96.4%)",
11	      "solver_time_seconds": 0.03
12	    },
13	    "tables": [
14	      {
15	        "name": "Table: L0 Head Allocation Comparison",
16	        "columns": [
17	          "Head",
18	          "Delta (×10⁻²)",
19	          "With Exclusion",
20	          "Without Exclusion"
21	        ],
22	        "rows": [
23	          [
24	            "L0-H0",
25	            "215.3",
26	            "8-bit (forced)",
27	            "8-bit (auto)"
28	          ],
29	          [
30	            "L0-H1",
31	            "198.7",
32	            "8-bit (forced)",
33	            "8-bit (auto)"
34	          ],
35	          [
36	            "L0-H2",
37	            "201.4",
38	            "8-bit (forced)",
39	            "8-bit (auto)"
40	          ],
41	          [
42	            "L0-H3",
43	            "189.2",
44	            "8-bit (forced)",
45	            "8-bit (auto)"
46	          ],
47	          [
48	            "L1-H0",
49	            "3.41",
50	            "4-bit",
51	            "4-bit"
52	          ],
53	          [
54	            "avg mid-layer",
55	            "1.87",
56	            "4-bit",
57	            "4-bit"
58	          ]
59	        ]
60	      },
61	      {
62	        "name": "Table: PPL Comparison",
63	        "columns": [
64	          "Configuration",
65	          "PPL (WikiText-2)"
66	        ],
67	        "rows": [
68	          [
69	            "Constrained MCKP (with L0 exclusion)",
70	            "11.23"
71	          ],
72	          [
73	            "Constrained MCKP (without L0 exclusion)",
74	            "11.28"
75	          ],
76	          [
77	            "Uniform 4-bit",
78	            "15.45"
79	          ]
80	        ]
81	      }
82	    ],
83	    "figures": [],
84	    "analysis": "这是论文中最具叙事力的实验之一。它把 \"solver automatically discovers architectural sensitivity structure\" 从修辞变成了实证。4/4 L0 heads 被自动发现说明 profiling delta 的 signal-to-noise 足够高，不需要任何领域先验。96.4% 的 allocation 一致率说明 exclusion constraint 本来就是冗余的——solver 自己就会做出正确决策。 PPL 差异 <0.5% 进一步确认了这一点。论文叙事可以正面使用： \"We initially included L0 exclusion as a safety constraint, but found the solver independently discovers L0 criticality from profiling data alone.\"\n\n\nLayer 0 heads 的 profiling delta 比 mid-layer heads 高 ~100×（delta ≈ 2.1 vs 均值 0.02）。 在 MCKP 的 objective 中，将 L0 heads 从 4-bit 提升到 8-bit 的边际收益远超任何 mid-layer head， 因此即使没有 exclusion 硬约束，纯 cost-benefit optimization 也会自动选择保护 L0。 PPL 几乎不变（+0.05）是因为 solver 自由度增加后在 mid-layer 有微小重分配，但 L0 保护 这个核心决策完全一致。少数 4 个 head 的分配差异出现在 delta 接近的 mid-layer 边界 heads。\n"
85	  },
86	  {
87	    "name": "Llama-3.1-8B Full Pipeline",
88	    "description": "在 Llama-3.1-8B（GQA 4:1, 8 KV heads/layer × 32 layers = 256 KV heads）上 完整复现 pipeline：profiling → constrained MCKP → evaluation。\n",
89	    "results": {
90	      "fp16_baseline_ppl": 6.24,
91	      "uniform_4bit_ppl": 8.95,
92	      "constrained_mckp_ppl": 6.78,
93	      "unconstrained_mckp_ppl": 14.31,
94	      "ppl_improvement_pct": 24.2,
95	      "max_2bit_used": 16,
96	      "l0_heads_assigned_8bit": "8/8 (100%)",
97	      "heads_at_2bit": 16,
98	      "heads_at_4bit": 192,
99	      "heads_at_8bit": 32,
100	      "heads_at_16bit": 16,
101	      "compression_ratio": "3.97×",
102	      "top_sensitive_heads_pct": "4.7%",
103	      "top_sensitive_heads_ppl_contribution_pct": "65%"
104	    },
105	    "tables": [
106	      {
107	        "name": "Table: Llama-3.1-8B Allocation Results",
108	        "columns": [
109	          "Method",
110	          "PPL ↓",
111	          "Compression",
112	          "Heads@2bit",
113	          "Heads@8bit+"
114	        ],
115	        "rows": [
116	          [
117	            "FP16 (baseline)",
118	            "6.24",
119	            "1×",
120	            "0",
121	            "256"
122	          ],
123	          [
124	            "Uniform 4-bit",
125	            "8.95",
126	            "4×",
127	            "0",
128	            "0"
129	          ],
130	          [
131	            "Unconstrained MCKP",
132	            "14.31",
133	            "4×",
134	            "89",
135	            "24"
136	          ],
137	          [
138	            "Constrained MCKP (max_2bit=16)",
139	            "6.78",
140	            "4×",
141	            "16",
142	            "48"
143	          ]
144	        ]
145	      },
146	      {
147	        "name": "Table: Layer 0 Sensitivity (Llama)",
148	        "columns": [
149	          "Head",
150	          "Delta (×10⁻²)",
151	          "Assigned"
152	        ],
153	        "rows": [
154	          [
155	            "L0-H0 ~ L0-H7",
156	            "58.3 ~ 89.1",
157	            "all 8-bit"
158	          ],
159	          [
160	            "L1-H0 ~ L1-H7",
161	            "2.1 ~ 4.8",
162	            "mixed 4/8-bit"
163	          ],
164	          [
165	            "avg mid-layer",
166	            "0.9",
167	            "4-bit"
168	          ]
169	        ]
170	      }
171	    ],
172	    "figures": [],
173	    "analysis": "Llama-3.1-8B 的成功复现是论文 generalizability 的关键支撑。GQA 4:1 vs 7:1 的差异 测试了方法对不同 KV head 共享结构的鲁棒性。24.2% 的改进虽然略低于 Qwen 的 27%， 但仍然显著且一致。unconstrained 崩溃的复现（2.1× 恶化）确认 compounding effect 不是 Qwen 特有的 artifact。跨架构 L0 dominance 的一致性支持 Claim 1 的强形式： \"Layer 0 sensitivity is an architectural invariant, not a model-specific phenomenon.\"\n\n\nLlama-3.1-8B 的 GQA ratio 为 4:1（32 query heads / 8 KV heads），KV heads 数量是 Qwen 的 2.3 倍（256 vs 112）。更多的 heads 意味着 per-head 分配的自由度更高，MCKP 有更大的 优化空间。但 GQA 4:1 也意味着每个 KV head 被更少的 query heads 共享（4 vs 7）， 所以单个 head 的影响力相对更分散，sensitivity heterogeneity 可能略低于 Qwen。 24.2% 的 PPL improvement 在 best tier 范围 [20,30] 内，略低于 Qwen 的 27% 是因为 Llama 的 attention head 结构更均匀（GQA ratio 更低→ per-KV-head 影响更分散）。 Unconstrained MCKP 仍然崩溃（14.31 vs 6.78）确认 compounding effect 在不同架构上一致存在， 但绝对恶化程度低于 Qwen（Qwen 36.92/11.23 = 3.3× vs Llama 14.31/6.78 = 2.1×）， 因为 256 heads 中同时被分配 2-bit 的比例在相同 max_2bit 约束下更低。 L0 dominance pattern 复现：Layer 0 的 8 个 KV heads profiling delta 显著高于其他层。\n"
174	  },
175	  {
176	    "name": "Mistral-7B-v0.3 Full Pipeline",
177	    "description": "在 Mistral-7B-v0.3（GQA 4:1, 8 KV heads/layer × 32 layers = 256 KV heads， sliding window attention）上完整复现 pipeline。\n",
178	    "results": {
179	      "fp16_baseline_ppl": 7.01,
180	      "uniform_4bit_ppl": 9.87,
181	      "constrained_mckp_ppl": 7.68,
182	      "unconstrained_mckp_ppl": 16.54,
183	      "ppl_improvement_pct": 22.2,
184	      "max_2bit_used": 14,
185	      "l0_heads_assigned_8bit": "8/8 (100%)",
186	      "heads_at_2bit": 14,
187	      "heads_at_4bit": 198,
188	      "heads_at_8bit": 28,
189	      "heads_at_16bit": 16,
190	      "compression_ratio": "3.98×",
191	      "sliding_window_impact": "window boundary layers show elevated sensitivity"
192	    },
193	    "tables": [
194	      {
195	        "name": "Table: Mistral-7B Results",
196	        "columns": [
197	          "Method",
198	          "PPL ↓",
199	          "Compression",
200	          "Improvement"
201	        ],
202	        "rows": [
203	          [
204	            "FP16 (baseline)",
205	            "7.01",
206	            "1×",
207	            "—"
208	          ],
209	          [
210	            "Uniform 4-bit",
211	            "9.87",
212	            "4×",
213	            "—"
214	          ],
215	          [
216	            "Unconstrained MCKP",
217	            "16.54",
218	            "4×",
219	            "−67.6%"
220	          ],
221	          [
222	            "Constrained MCKP",
223	            "7.68",
224	            "4×",
225	            "+22.2%"
226	          ]
227	        ]
228	      }
229	    ],
230	    "figures": [],
231	    "analysis": "三模型中最低的 PPL improvement（22.2%），但仍在 best tier 范围内。Sliding window 是一个有意义的 architectural variation，成功复现说明方法不依赖于 full attention 假设。 论文可以额外指出 sliding window boundary layers 的 elevated sensitivity 作为 一个 interesting observation，但不要过度解释。\n\n\nMistral-7B-v0.3 使用 sliding window attention（window=4096），这在 KV cache 的使用模式 上与 full attention 不同：window 边界附近的 layers 承担更多的\"信息中继\"职责， sensitivity 分布可能比 Llama 更不均匀。22.2% 的 PPL improvement 在 best tier 范围 [18,28] 内，略低于 Llama 的 24.2%，因为 Mistral 的 sliding window 使得 KV cache 在长序列上的有效利用率本来就较高（无需缓存超出 window 的 KV），4-bit uniform 对 Mistral 的相对伤害比 full-attention 模型更小。但 constrained MCKP 仍然显著优于 uniform，确认方法在 sliding window 架构下同样有效。 L0 dominance pattern 第三次复现：即使有 sliding window，Layer 0 heads 仍然是最敏感的， 因为它们处理的是 token embedding 的直接变换，与 attention pattern 无关。\n"
232	  },
233	  {
234	    "name": "Compounding Effect Elbow Curve",
235	    "description": "在 Qwen2.5-7B 上 sweep max_2bit 从 0 到 112（全部 KV heads）， 8 个点：0, 4, 8, 16, 24, 48, 75, 112。绘制 PPL vs max_2bit 曲线， 定位 compounding threshold（elbow point）。\n",
236	    "results": {
237	      "sweep_results": {
238	        "max_2bit_0": {
239	          "ppl": 12.01,
240	          "heads_at_2bit": 0,
241	          "note": "no 2-bit allowed, solver uses 4/8/16 only"
242	        },
243	        "max_2bit_4": {
244	          "ppl": 11.34,
245	          "heads_at_2bit": 4,
246	          "note": "4 most expendable heads at 2-bit, frees budget for 8-bit on L0"
247	        },
248	        "max_2bit_8": {
249	          "ppl": 11.08,
250	          "heads_at_2bit": 8,
251	          "note": "near-optimal, all freed budget protecting critical heads"
252	        },
253	        "max_2bit_16": {
254	          "ppl": 11.52,
255	          "heads_at_2bit": 16,
256	          "note": "slight degradation begins, compounding starts"
257	        },
258	        "max_2bit_24": {
259	          "ppl": 13.41,
260	          "heads_at_2bit": 24,
261	          "note": "clear compounding, 2-bit heads interacting"
262	        },
263	        "max_2bit_48": {
264	          "ppl": 21.87,
265	          "heads_at_2bit": 48,
266	          "note": "severe compounding, 43% of heads at extreme quant"
267	        },
268	        "max_2bit_75": {
269	          "ppl": 30.12,
270	          "heads_at_2bit": 67,
271	          "note": "catastrophic, solver can't use all 75 slots optimally"
272	        },
273	        "max_2bit_112": {
274	          "ppl": 36.92,
275	          "heads_at_2bit": 78,
276	          "note": "unconstrained equivalent, full compounding"
277	        }
278	      },
279	      "elbow_k": 12,
280	      "elbow_snr": 7.3,
281	      "optimal_k": 8,
282	      "optimal_ppl": 11.08,
283	      "pre_elbow_slope": 0.055,
284	      "post_elbow_slope": 1.29
285	    },
286	    "tables": [
287	      {
288	        "name": "Table: Compounding Effect Sweep",
289	        "columns": [
290	          "max_2bit (k)",
291	          "PPL ↓",
292	          "Δ PPL vs k=0",
293	          "Heads@2bit",
294	          "% Heads@2bit"
295	        ],
296	        "rows": [
297	          [
298	            "0",
299	            "12.01",
300	            "—",
301	            "0",
302	            "0%"
303	          ],
304	          [
305	            "4",
306	            "11.34",
307	            "−0.67",
308	            "4",
309	            "3.6%"
310	          ],
311	          [
312	            "8",
313	            "11.08",
314	            "−0.93",
315	            "8",
316	            "7.1%"
317	          ],
318	          [
319	            "16",
320	            "11.52",
321	            "−0.49",
322	            "16",
323	            "14.3%"
324	          ],
325	          [
326	            "24",
327	            "13.41",
328	            "+1.40",
329	            "24",
330	            "21.4%"
331	          ],
332	          [
333	            "48",
334	            "21.87",
335	            "+9.86",
336	            "48",
337	            "42.9%"
338	          ],
339	          [
340	            "75",
341	            "30.12",
342	            "+18.11",
343	            "67",
344	            "59.8%"
345	          ],
346	          [
347	            "112",
348	            "36.92",
349	            "+24.91",
350	            "78",
351	            "69.6%"
352	          ]
353	        ]
354	      }
355	    ],
356	    "figures": [],
357	    "analysis": "这是论文的 signature figure，直接支撑 Claim 3。elbow curve 提供了 cardinality constraint 的 principled justification：不是 arbitrary heuristic，而是 compounding non-additivity 的 empirical boundary。23× slope ratio 是一个 striking result，可以用一句话总结论文的核心发现： \"Below the compounding threshold, per-head distortion is approximately additive (slope=0.055); above it, each additional extreme-quantized head incurs 23× more damage due to error propagation through the residual stream.\" 建议在论文 Introduction 的 Figure 1 位置放置此图。\n\n\nCompounding effect 的物理机制：当多个 heads 同时被 quantize 到 2-bit 时，每个 head 的 quantization error 通过 residual stream 传播到下游 layers。单个 head 的 2-bit error 可以被其他 head 的正常精度\"吸收\"，但当足够多的 heads 同时 degraded 时，error 累积 超过模型的 error correction capacity。这是一个典型的 threshold phenomenon。 elbow 在 k≈8-12 是因为 Qwen2.5-7B 有 112 个 KV heads（28 layers × 4 heads）， 当 ~7-10% 的 heads 被设为 2-bit 时达到 compounding onset。k=8（7.1% of heads） 是 optimal：此时 freed budget 恰好足够保护所有 critical heads（L0 + 少量 high-delta mid-layer heads）at 8/16-bit，而 2-bit heads 都是 truly expendable 的。 SNR=7.3 远超阈值 5，说明 elbow 是 sharp 的，不是 gradual degradation。 pre-elbow slope 0.055 PPL/head 说明在 safe region 内每增加一个 2-bit head 几乎 无影响；post-elbow slope 1.29 PPL/head 说明超过 elbow 后每增加一个 2-bit head 带来 >1 PPL 的恶化——23× 的 slope ratio 是 compounding non-additivity 的直接证据。\n"
358	  },
359	  {
360	    "name": "Budget Sweep (2×/4×/8× Compression)",
361	    "description": "在 Qwen2.5-7B 上测试 constrained MCKP 在三个压缩比下的表现： 2×（budget=0.5）、4×（budget=0.25）、8×（budget=0.125）， 每个压缩比与同 budget 的 uniform baseline 对比。\n",
362	    "results": {
363	      "results_2x": {
364	        "uniform_8bit_ppl": 10.12,
365	        "constrained_mckp_ppl": 9.94,
366	        "improvement_pct": 1.8,
367	        "allocation": "mostly 8-bit with 12 heads at 16-bit, 8 heads at 4-bit"
368	      },
369	      "results_4x": {
370	        "uniform_4bit_ppl": 15.45,
371	        "constrained_mckp_ppl": 11.08,
372	        "improvement_pct": 28.3,
373	        "allocation": "8 heads@2bit, 76 heads@4bit, 20 heads@8bit, 8 heads@16bit"
374	      },
375	      "results_8x": {
376	        "uniform_2bit_ppl": 78.34,
377	        "constrained_mckp_ppl": 28.67,
378	        "improvement_pct": 63.4,
379	        "allocation": "64 heads@2bit, 32 heads@4bit, 12 heads@8bit, 4 heads@16bit"
380	      },
381	      "fp16_baseline": 9.82
382	    },
383	    "tables": [
384	      {
385	        "name": "Table: Budget Sweep Results (Qwen2.5-7B, WikiText-2)",
386	        "columns": [
387	          "Compression",
388	          "Budget",
389	          "Uniform PPL",
390	          "MCKP PPL",
391	          "Improvement",
392	          "Δ vs FP16"
393	        ],
394	        "rows": [
395	          [
396	            "2×",
397	            "0.50",
398	            "10.12",
399	            "9.94",
400	            "1.8%",
401	            "+1.2%"
402	          ],
403	          [
404	            "4×",
405	            "0.25",
406	            "15.45",
407	            "11.08",
408	            "28.3%",
409	            "+12.8%"
410	          ],
411	          [
412	            "8×",
413	            "0.125",
414	            "78.34",
415	            "28.67",
416	            "63.4%",
417	            "+192%"
418	          ],
419	          [
420	            "FP16",
421	            "1.00",
422	            "9.82",
423	            "—",
424	            "—",
425	            "—"
426	          ]
427	        ]
428	      }
429	    ],
430	    "figures": [],
431	    "analysis": "Budget sweep 回应了 reviewer concern #4（\"How does this work at different compression ratios?\"）。1.8% → 28.3% → 63.4% 的递增趋势是一个 clean story： mixed-precision 的价值在压缩压力大时最显著。4× 是论文的 headline compression ratio， 既是实际部署最常见的 target，也是 MCKP 优势最 striking 的 sweet spot。 8× 的结果可以诚实报告：MCKP 大幅优于 uniform 但绝对 PPL 仍然高， 说明方法的局限性（不能 violate information-theoretic limits）。\n\n\n不同压缩比下 MCKP 优势的差异源于 sensitivity heterogeneity 的利用空间： (1) 2× 压缩：budget 充裕，uniform 8-bit 已经接近 FP16（+3.1%），MCKP 只能通过 将少量 insensitive heads 降到 4-bit 并将 freed budget 给最 sensitive heads 升到 16-bit 来获得微小改进。1.8% 的 improvement 虽小但说明 heterogeneity 确实存在。 (2) 4× 压缩：sweet spot——uniform 4-bit 已有 57% 的 PPL degradation，而 MCKP 可以充分利用 head 间的 sensitivity 差异。28.3% 的 improvement 是 headline result。 (3) 8× 压缩：uniform 2-bit 是灾难性的（PPL 78.34, 8× baseline），MCKP 通过 保护 ~15% 的 critical heads 在 8/16-bit 将 PPL 控制在 28.67——仍然很差， 但比 uniform 好 63.4%。这说明即使在极端压缩下，intelligent allocation 仍然 有巨大价值，但也诚实地表明 8× 压缩的绝对质量不够实用。 整体趋势：MCKP 的相对优势随压缩比增加而增大，因为更激进的压缩放大了 sensitivity heterogeneity 的重要性。\n"
432	  },
433	  {
434	    "name": "High-Resolution Profiling",
435	    "description": "将 profiling 从 16 seq × 512 tokens 提升到 64 seq × 2048 tokens（8× 数据量）。 在 Qwen2.5-7B 上重新 profile，rerun MCKP，评估是否能区分 mid-layer heads。\n",
436	    "results": {
437	      "lores_nonzero_head_pct": 16.1,
438	      "hires_nonzero_head_pct": 58.0,
439	      "lores_delta_std_midlayers": 0.0003,
440	      "hires_delta_std_midlayers": 0.0089,
441	      "hires_mckp_ppl": 10.72,
442	      "lores_mckp_ppl": 11.08,
443	      "ppl_improvement_from_hires": 3.2,
444	      "new_sensitive_heads_discovered": 14,
445	      "l0_delta_change_pct": "+2.1%",
446	      "mid_layer_delta_change_pct": "+1400%",
447	      "profiling_time_hours": 2.8
448	    },
449	    "tables": [
450	      {
451	        "name": "Table: Profiling Resolution Comparison",
452	        "columns": [
453	          "Metric",
454	          "Lo-Res (16×512)",
455	          "Hi-Res (64×2048)",
456	          "Change"
457	        ],
458	        "rows": [
459	          [
460	            "Total profiling tokens",
461	            "8,192",
462	            "131,072",
463	            "16×"
464	          ],
465	          [
466	            "Nonzero-delta heads",
467	            "18/112 (16.1%)",
468	            "65/112 (58.0%)",
469	            "+261%"
470	          ],
471	          [
472	            "Mid-layer delta std",
473	            "3×10⁻⁴",
474	            "8.9×10⁻³",
475	            "+1400%"
476	          ],
477	          [
478	            "L0 avg delta",
479	            "2.08",
480	            "2.12",
481	            "+2.1%"
482	          ],
483	          [
484	            "MCKP PPL",
485	            "11.08",
486	            "10.72",
487	            "−3.2%"
488	          ],
489	          [
490	            "Allocation changes vs lo-res",
491	            "—",
492	            "14 heads",
493	            "—"
494	          ],
495	          [
496	            "Profiling wall-time",
497	            "0.4h",
498	            "2.8h",
499	            "7×"
500	          ]
501	        ]
502	      },
503	      {
504	        "name": "Table: Discovered Mid-Layer Sensitive Heads",
505	        "columns": [
506	          "Head",
507	          "Lo-Res Delta",
508	          "Hi-Res Delta",
509	          "New Allocation"
510	        ],
511	        "rows": [
512	          [
513	            "L12-H2",
514	            "0.000",
515	            "0.0134",
516	            "4→8 bit"
517	          ],
518	          [
519	            "L15-H0",
520	            "0.000",
521	            "0.0118",
522	            "4→8 bit"
523	          ],
524	          [
525	            "L7-H3",
526	            "0.000",
527	            "0.0097",
528	            "4→8 bit"
529	          ],
530	          [
531	            "L21-H1",
532	            "0.000",
533	            "0.0091",
534	            "2→4 bit"
535	          ],
536	          [
537	            "... (10 more)",
538	            "—",
539	            "—",
540	            "—"
541	          ]
542	        ]
543	      }
544	    ],
545	    "figures": [],
546	    "analysis": "高分辨率 profiling 的 3.2% PPL improvement 不大，但它的主要价值是 scientific： 证明了 mid-layer heterogeneity 的存在（之前被 noise 掩盖），使 Claim 1 从 \"L0 dominates\" 扩展为 \"sensitivity is hierarchically structured — L0 dominates, but mid-layer heterogeneity also matters at finer resolution\"。 论文建议：hi-res profiling 可以作为一个 optional enhancement， main results 使用 lo-res（更实用），hi-res 在 analysis section 展示 以支持 Claim 1 的完整叙事。2.8h 的 profiling 成本说明 hi-res 在实践中 不是 free 的，但对于 one-time offline allocation 是可接受的。\n\n\n低分辨率 profiling（16×512 = 8K tokens）的 mid-layer delta 被 sampling noise 淹没：大多数 mid-layer heads 的 true delta 在 10⁻⁴ 量级，而 sampling variance 在 ~10⁻³ 量级，导致 84% 的 heads 被 round 到 delta=0。高分辨率（64×2048 = 128K tokens） 将 sampling variance 降低 √16 ≈ 4×，使得 10⁻⁴ 量级的 true delta 开始可分辨。 58% nonzero（从 16.1% 提升）意味着约 47 个之前被认为 delta=0 的 head 现在有了 可测量的 sensitivity signal。其中 14 个 head 的 delta 足够大以改变 MCKP allocation。 3.2% 的 PPL improvement（10.72 vs 11.08）说明 mid-layer heterogeneity 确实存在且 有实际价值，但主要贡献仍来自 L0 的 correct allocation（L0 delta 变化仅 2.1%， 说明 L0 signal 在低分辨率下就已经 saturated）。 1400% 的 mid-layer delta std 提升是最 striking 的数字： 从 0.0003 到 0.0089，说明 mid-layer 内部确实有显著的 head-level heterogeneity， 只是之前被 noise 掩盖了。\n"
547	  },
548	  {
549	    "name": "C4 Cross-Dataset Evaluation",
550	    "description": "在 Qwen2.5-7B 上用 WikiText-2 calibrated allocations 在 C4 上评估， 同时用 C4 数据 rerun profiling + MCKP 并在 C4 上评估。 计算两种 allocation 的 rank correlation。\n",
551	    "results": {
552	      "c4_fp16_ppl": 11.87,
553	      "c4_uniform_4bit_ppl": 17.42,
554	      "c4_constrained_mckp_ppl_wikitext_calib": 12.61,
555	      "c4_constrained_mckp_ppl_c4_calib": 12.48,
556	      "c4_ppl_improvement_pct": 27.6,
557	      "wikitext_c4_rank_correlation": 0.94,
558	      "allocation_agreement_rate": "101/112 heads (90.2%)",
559	      "l0_protection_consistent": true,
560	      "cross_calib_ppl_gap": 0.13
561	    },
562	    "tables": [
563	      {
564	        "name": "Table: C4 Evaluation Results",
565	        "columns": [
566	          "Method",
567	          "WikiText-2 PPL",
568	          "C4 PPL",
569	          "Improvement"
570	        ],
571	        "rows": [
572	          [
573	            "FP16",
574	            "9.82",
575	            "11.87",
576	            "—"
577	          ],
578	          [
579	            "Uniform 4-bit",
580	            "15.45",
581	            "17.42",
582	            "—"
583	          ],
584	          [
585	            "Constrained MCKP (WT2-calib)",
586	            "11.08",
587	            "12.61",
588	            "27.6%"
589	          ],
590	          [
591	            "Constrained MCKP (C4-calib)",
592	            "—",
593	            "12.48",
594	            "28.3%"
595	          ],
596	          [
597	            "Unconstrained MCKP",
598	            "36.92",
599	            "41.23",
600	            "−136.5%"
601	          ]
602	        ]
603	      },
604	      {
605	        "name": "Table: Cross-Dataset Calibration Robustness",
606	        "columns": [
607	          "Metric",
608	          "Value"
609	        ],
610	        "rows": [
611	          [
612	            "Rank correlation (head delta ordering)",
613	            "0.94"
614	          ],
615	          [
616	            "Allocation agreement (same bit-width)",
617	            "90.2%"
618	          ],
619	          [
620	            "Cross-calib PPL gap",
621	            "0.13"
622	          ],
623	          [
624	            "L0 8-bit protection consistent",
625	            "Yes"
626	          ]
627	        ]
628	      }
629	    ],
630	    "figures": [],
631	    "analysis": "C4 实验完成了 \"multi-dataset\" 维度的验证。0.94 的 rank correlation 和 90.2% 的 allocation agreement 是强结果，支持论文的核心论点：per-head sensitivity 是 architectural property，calibration dataset 的选择不 critical。 Cross-calib PPL gap 仅 0.13 说明在实际部署中可以用任何 reasonable dataset 做 one-time calibration，不需要 task-specific profiling。\n\n\nC4 是 web-crawl 数据，domain 比 WikiText-2 更广。PPL 绝对值更高（FP16 11.87 vs 9.82） 是因为 C4 的 vocabulary diversity 和 noise。但 quantization sensitivity 的 relative ordering 高度一致（rank correlation 0.94）：哪些 heads 敏感、哪些不敏感， 这是 architectural property 而非 data-dependent property。L0 heads 在 C4 profiling 下同样是最敏感的，进一步支持 \"sensitivity is architecturally determined\"。 90.2% 的 allocation agreement 说明 WikiText-2 calibrated allocation 在 C4 上 几乎同样有效（PPL gap 仅 0.13）。27.6% 的 improvement 与 WikiText-2 上的 28.3% 接近，说明方法的效果不依赖于特定 dataset。 0.94 的 rank correlation 在 best tier 范围 [0.88, 0.98] 内。\n"
632	  },
633	  {
634	    "name": "RateQuant Baseline Comparison",
635	    "description": "实现 RateQuant 的 reverse waterfilling 算法，应用在我们的 discrete action set {2,4,8,16}-bit 上（rounding to nearest）。在 Llama-3.1-8B 上与 constrained MCKP 对比。\n",
636	    "results": {
637	      "ratequant_continuous_optimal_bits": "avg 4.0 (continuous)",
638	      "ratequant_rounded_ppl": 8.12,
639	      "constrained_mckp_ppl": 6.78,
640	      "uniform_4bit_ppl": 8.95,
641	      "ratequant_improvement_vs_uniform": 9.3,
642	      "mckp_improvement_vs_uniform": 24.2,
643	      "mckp_improvement_vs_ratequant": 16.5,
644	      "ratequant_heads_at_2bit": 38,
645	      "ratequant_l0_protection": "partial (5/8 heads at 8-bit, 3 at 4-bit)"
646	    },
647	    "tables": [
648	      {
649	        "name": "Table: RateQuant vs Constrained MCKP (Llama-3.1-8B)",
650	        "columns": [
651	          "Method",
652	          "PPL ↓",
653	          "Impr. vs Uniform",
654	          "Heads@2bit",
655	          "L0 at 8-bit"
656	        ],
657	        "rows": [
658	          [
659	            "Uniform 4-bit",
660	            "8.95",
661	            "—",
662	            "0",
663	            "0/8"
664	          ],
665	          [
666	            "RateQuant (rounded)",
667	            "8.12",
668	            "9.3%",
669	            "38",
670	            "5/8"
671	          ],
672	          [
673	            "Unconstrained MCKP",
674	            "14.31",
675	            "−59.9%",
676	            "89",
677	            "8/8"
678	          ],
679	          [
680	            "Constrained MCKP",
681	            "6.78",
682	            "24.2%",
683	            "16",
684	            "8/8"
685	          ]
686	        ]
687	      }
688	    ],
689	    "figures": [],
690	    "analysis": "这是论文 differentiation 的实证基础。RateQuant 失败的两个原因清晰可分： rounding loss 和 compounding blindness。论文可以构造一个 didactic example： \"RateQuant assigns continuous 5.7 bits to L0-H3 (optimal under continuous assumption), but rounding to 4-bit causes 4.2× more distortion than rounding to 8-bit — a loss that MCKP avoids by directly optimizing in discrete space.\" 结合 L0 partial protection failure，这给出了一个 compelling narrative：continuous methods fail at the granularity that matters.\n\n\nRateQuant 的 reverse waterfilling 假设 distortion D(b) = α·β^{-b} 是 continuous 且 additive 的。在 continuous regime 下这给出 R-D optimal allocation。但 rounding to discrete {2,4,8,16} 引入两个问题： (1) Rounding loss：continuous 5.3-bit 被 round 到 4-bit 或 8-bit，两者都不是 optimal。MCKP 直接在 discrete space 上优化，避免了 rounding suboptimality。 (2) Compounding blindness：waterfilling 没有 cardinality constraint，round 后 38 个 heads 被分配 2-bit（vs MCKP 的 16 个），超过 compounding threshold。 这导致 PPL 8.12——比 uniform 好（9.3%）但远逊于 constrained MCKP（6.78）。 L0 保护不完整（仅 5/8 at 8-bit）是因为 waterfilling 的 continuous optimal 对 L0 的某些 heads 分配了 ~6-7 bit，round 到 4 或 8 取决于 arbitrary threshold。 16.5% 的 MCKP vs RateQuant 优势直接支撑论文的 core differentiation。\n"
691	  },
692	  {
693	    "name": "Oracle Comparison (Subset Brute-Force)",
694	    "description": "在 Qwen2.5-7B 的 4 个 layer groups（each 7 layers, 28 heads per group）上 brute-force enumerate 所有 allocation，计算 MCKP 与 true oracle 的 gap。\n",
695	    "results": {
696	      "group_1_layers": "L0-L6",
697	      "group_1_mckp_ppl": 10.89,
698	      "group_1_oracle_ppl": 10.82,
699	      "group_1_gap": "0.6%",
700	      "group_2_layers": "L7-L13",
701	      "group_2_mckp_ppl": 11.01,
702	      "group_2_oracle_ppl": 10.97,
703	      "group_2_gap": "0.4%",
704	      "group_3_layers": "L14-L20",
705	      "group_3_mckp_ppl": 11.04,
706	      "group_3_oracle_ppl": 11.02,
707	      "group_3_gap": "0.2%",
708	      "group_4_layers": "L21-L27",
709	      "group_4_mckp_ppl": 10.98,
710	      "group_4_oracle_ppl": 10.95,
711	      "group_4_gap": "0.3%",
712	      "overall_estimated_gap": "<1%",
713	      "brute_force_configs_evaluated": "4^28 per group ≈ 7.2×10^16 (sampled 10^6 + DP)"
714	    },
715	    "tables": [
716	      {
717	        "name": "Table: MCKP vs Oracle Gap",
718	        "columns": [
719	          "Layer Group",
720	          "MCKP PPL",
721	          "Oracle PPL",
722	          "Gap (%)"
723	        ],
724	        "rows": [
725	          [
726	            "L0-L6",
727	            "10.89",
728	            "10.82",
729	            "0.6%"
730	          ],
731	          [
732	            "L7-L13",
733	            "11.01",
734	            "10.97",
735	            "0.4%"
736	          ],
737	          [
738	            "L14-L20",
739	            "11.04",
740	            "11.02",
741	            "0.2%"
742	          ],
743	          [
744	            "L21-L27",
745	            "10.98",
746	            "10.95",
747	            "0.3%"
748	          ]
749	        ]
750	      }
751	    ],
752	    "figures": [],
753	    "analysis": "<1% oracle gap 是一个 reassuring result。论文可以声明 \"our constrained MCKP solver achieves near-optimal allocation\" 并用此实验作为 evidence。 这是 P1 priority，如果时间紧可以缩减到 2 个 groups。\n\n\nMCKP 是 NP-hard in general，但我们的 instance 结构良好：(1) items (heads) 在 profiling delta 上有 clear separation（不是 adversarial instance）， (2) budget constraint 是 linear，(3) 每个 head 的 action set 只有 4 个选项。 在这种 \"benign\" instance 上，greedy-based MCKP solver（通过 LP relaxation + rounding）接近 optimal。<1% 的 gap 说明 constrained MCKP 是 practically optimal， 不需要 exponential-time exact solver。Group 1（包含 L0）的 gap 最大（0.6%） 是因为 L0 heads 的 extreme delta 创造了更大的 \"opportunity cost\" gradient， 但即使如此 gap 也很小。\n"
754	  },
755	  {
756	    "name": "Cross-Domain Calibration Robustness",
757	    "description": "用 C4 calibrate profiling，在 WikiText-2 上评估（反向也做）。 报告 per-head allocation agreement rate。\n",
758	    "results": {
759	      "c4_calib_wikitext_eval_ppl": 11.21,
760	      "wikitext_calib_wikitext_eval_ppl": 11.08,
761	      "wikitext_calib_c4_eval_ppl": 12.61,
762	      "c4_calib_c4_eval_ppl": 12.48,
763	      "cross_calib_ppl_penalty": "0.13 (WikiText), 0.13 (C4)",
764	      "allocation_agreement": "101/112 (90.2%)",
765	      "disagreement_analysis": "11 borderline mid-layer heads with delta ratio <1.5×"
766	    },
767	    "tables": [
768	      {
769	        "name": "Table: Cross-Calibration Matrix",
770	        "columns": [
771	          "Calibration →",
772	          "Eval: WikiText-2",
773	          "Eval: C4"
774	        ],
775	        "rows": [
776	          [
777	            "WikiText-2",
778	            "11.08",
779	            "12.61"
780	          ],
781	          [
782	            "C4",
783	            "11.21",
784	            "12.48"
785	          ],
786	          [
787	            "Gap",
788	            "0.13",
789	            "0.13"
790	          ]
791	        ]
792	      }
793	    ],
794	    "figures": [],
795	    "analysis": "Cross-calibration robustness 回答了一个 practical deployment question： \"Do I need task-specific calibration data?\" 答案是 no——0.13 的 cross-calib penalty 说明 any reasonable text corpus works。这简化了 deployment story。\n\n\nPer-head sensitivity 主要由 weight matrix 结构决定（architectural property）， calibration data 只影响 activation statistics 的 estimation。不同 domain 的 activation 分布在大模型中高度 overlap（因为 pretrain data 本身就是 multi-domain）， 所以 calibration source 对 sensitivity ranking 的影响很小。 90.2% agreement 中不一致的 11 个 heads 都是 borderline cases——delta 接近 decision boundary 的 mid-layer heads，微小的 activation distribution shift 就足以翻转 4-bit vs 2-bit 的决策。但这些 heads 本身就是 \"doesn't matter much\" 的 heads（delta 很小），所以翻转对 PPL 影响极小（0.13 penalty）。\n"
796	  },
797	  {
798	    "name": "Head Sensitivity Visualization",
799	    "description": "生成论文质量的 figures：per-head delta heatmap, compounding curve, allocation comparison。\n",
800	    "results": {
801	      "figures_generated": 4,
802	      "figure_1": "Per-head profiling delta heatmap (28×4 for Qwen, 32×8 for Llama/Mistral)",
803	      "figure_2": "Compounding effect elbow curve (from plan_004)",
804	      "figure_3": "Budget allocation comparison bar charts (uniform vs MCKP at 3 compression ratios)",
805	      "figure_4": "Cross-model L0 dominance comparison"
806	    },
807	    "tables": [],
808	    "figures": [],
809	    "analysis": "Figure 1 (compounding curve) 和 Figure 2 (heatmap) 是论文最重要的两张图。 建议 Figure 1 放在 Introduction，Figure 2 放在 Method section 的 motivation 段落。Figure 3 和 4 放在 Experiments section。\n\n\n这些 figures 直接对应论文的三条 claims：heatmap → Claim 1 (heterogeneity)， allocation comparison → Claim 2 (MCKP superiority)，elbow curve → Claim 3 (cardinality regularization)。Cross-model figure 是 generalizability 的 visual proof。\n"
810	  },
811	  {
812	    "name": "Downstream Task Evaluation (MMLU / LongBench)",
813	    "description": "在 Qwen2.5-7B 4× compression 下评估 MMLU（5-shot）和 LongBench。 验证 PPL improvement 是否 transfer 到 downstream performance。\n",
814	    "results": {
815	      "mmlu_fp16": 71.2,
816	      "mmlu_uniform_4bit": 65.8,
817	      "mmlu_constrained_mckp": 69.7,
818	      "mmlu_improvement_pct": 5.9,
819	      "longbench_fp16_avg": 48.3,
820	      "longbench_uniform_4bit_avg": 39.1,
821	      "longbench_constrained_mckp_avg": 45.8,
822	      "longbench_improvement_pct": 17.1
823	    },
824	    "tables": [
825	      {
826	        "name": "Table: Downstream Task Results (Qwen2.5-7B, 4× Compression)",
827	        "columns": [
828	          "Task",
829	          "FP16",
830	          "Uniform 4-bit",
831	          "Constrained MCKP",
832	          "Recovery %"
833	        ],
834	        "rows": [
835	          [
836	            "MMLU (5-shot)",
837	            "71.2",
838	            "65.8",
839	            "69.7",
840	            "72.2%"
841	          ],
842	          [
843	            "LongBench (avg)",
844	            "48.3",
845	            "39.1",
846	            "45.8",
847	            "72.8%"
848	          ],
849	          [
850	            "WikiText-2 PPL ↓",
851	            "9.82",
852	            "15.45",
853	            "11.08",
854	            "77.7%"
855	          ]
856	        ]
857	      }
858	    ],
859	    "figures": [],
860	    "analysis": "Downstream 结果确认 PPL improvement 不是 metric-hacking——实际 task performance 也显著提升。LongBench 的 17.1% improvement 特别有说服力，因为 KV cache 在 long-context 场景下是 critical bottleneck。论文可以用 \"72-78% of FP16-to-uniform degradation recovered by constrained MCKP\" 作为 unified summary。 这是 P2，如果时间紧可以只做 MMLU（更快，更 standard benchmark）。\n\n\nMMLU 主要测 short-context factual knowledge retrieval，KV cache quantization 对 MMLU 的影响相对较小（因为 sequence length 短，KV cache 的 cumulative error 小）。 所以 uniform 4-bit 的 MMLU 下降不大（65.8 vs 71.2, −7.6%），MCKP 的 improvement 也相应较小（+5.9 pp 的 recovery）。 LongBench 测 long-context tasks，KV cache quality 直接影响 long-range dependency 的保留。uniform 4-bit 下降更大（39.1 vs 48.3, −19.0%），MCKP 的 recovery 也更显著 （+17.1 pp）。这符合预期：mixed-precision KV cache 的价值在 long-context 场景下 最大，因为 cumulative quantization error 在长序列上被 amplified。 69.7 vs 71.2 的 MMLU（−2.1%）说明 constrained MCKP 在 4× 压缩下几乎无损。\n"
861	  },
862	  {
863	    "name": "70B Profiling-Only (Scale Analysis)",
864	    "description": "在 Qwen2.5-72B 上仅做 distortion profiling（不做 full eval）， 分析 sensitivity patterns 是否随 model size 变化。\n",
865	    "results": {
866	      "total_kv_heads": 560,
867	      "layers": 80,
868	      "kv_heads_per_layer": 7,
869	      "l0_avg_delta": 3.47,
870	      "l0_delta_ratio_vs_mean": "142×",
871	      "mid_layer_nonzero_pct": "12.3% (lo-res)",
872	      "top_sensitive_pct": "2.8%",
873	      "top_sensitive_contribution": "74%",
874	      "compounding_threshold_estimated_k": "~20-30 (extrapolated)",
875	      "profiling_time_hours": 3.5
876	    },
877	    "tables": [
878	      {
879	        "name": "Table: Sensitivity Scaling (7B vs 72B)",
880	        "columns": [
881	          "Metric",
882	          "Qwen2.5-7B",
883	          "Qwen2.5-72B",
884	          "Trend"
885	        ],
886	        "rows": [
887	          [
888	            "Total KV heads",
889	            "112",
890	            "560",
891	            "5×"
892	          ],
893	          [
894	            "L0 delta ratio",
895	            "100×",
896	            "142×",
897	            "↑"
898	          ],
899	          [
900	            "Top sensitive %",
901	            "3.6%",
902	            "2.8%",
903	            "↓ (more concentrated)"
904	          ],
905	          [
906	            "Top contribution %",
907	            "70%",
908	            "74%",
909	            "↑"
910	          ],
911	          [
912	            "Compounding threshold k",
913	            "8-12",
914	            "~20-30 (est.)",
915	            "scales sub-linearly"
916	          ]
917	        ]
918	      }
919	    ],
920	    "figures": [],
921	    "analysis": "70B profiling-only 是一个 \"scaling teaser\"——不做 full eval 但提供了 scale 维度的 evidence。142× L0 dominance 和 74% concentration 是 compelling numbers， 支持论文 Discussion 中的 \"as models scale, the potential benefit of per-head mixed-precision allocation grows\" 论点。 P2 priority，如果时间紧可以放在 Appendix 或 Discussion 的一段话中。 不需要 full eval 就已经有足够的 narrative value。\n\n72B model 有 80 layers × 7 KV heads = 560 KV heads。L0 dominance 更强（142× vs 100×） 是因为更深的 model 使得 L0 的 \"information gateway\" 角色更 critical—— 所有下游 79 layers 都依赖 L0 产出的 representation。更大的 depth 意味着 L0 error 有更多 layers 来 accumulate。 Top sensitive heads 占比从 3.6%（7B）降到 2.8%（72B）是因为 heads 总数增加 但 critical heads 数量增加更慢（L0 的 7 heads + 少量 early-layer heads ≈ 15-16 heads）。 74% 的 contribution（vs 7B 的 70%）说明 concentration 进一步加剧。 这支持一个 scaling hypothesis：模型越大，sensitivity heterogeneity 越强， mixed-precision 的 potential benefit 越大。\n"
922	  }
923	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb311eb0-4520-4291-b91a-f02c4b18cfd9",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "6d0611ef-12ba-48fc-838a-66e084d5bdbd",
  "sourceToolAssistantUUID": "eb311eb0-4520-4291-b91a-f02c4b18cfd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T00:57:19.944Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JhpjZXx1mwL5PHnfAEedhT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/compounding_sweep/data/compounding_sweep_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d0611ef-12ba-48fc-838a-66e084d5bdbd",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Z1432gbZxkQeij34rf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f925541e-2893-49be-b910-f93f3a58f547",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WiMVizpzFAKefJnQKyFr9A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11897,
      "cache_read_input_tokens": 31081,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11897
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 261,
          "cache_read_input_tokens": 31081,
          "cache_creation_input_tokens": 11897,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11897,
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

_source line 36 · 2026-05-14T00:57:19.952Z_

<details><summary>↩ Tool result · `toolu_01JhpjZXx1mwL5PHnfAEedhT`</summary>

```text
1	max_2bit,ppl,n_2bit,n_4bit,n_8bit,n_16bit,mem_ratio
2	0,15.4454,0,112,0,0,0.25
3	4,11.7706,4,106,2,0,0.25
4	8,11.2312,8,100,4,0,0.25
5	16,11.809,16,92,2,2,0.25
6	24,13.1448,24,84,0,4,0.25
7	48,22.8826,48,56,0,8,0.25
8	75,35.348,75,25,0,12,0.2467
9	112,35.348,75,25,0,12,0.2467
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f925541e-2893-49be-b910-f93f3a58f547",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "c0aaa2fa-9182-4780-afbb-37fd3871a27a",
  "sourceToolAssistantUUID": "f925541e-2893-49be-b910-f93f3a58f547",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-14T00:57:24.282Z_

Now I have a thorough understanding of the paper, the actual experimental data, and the "dream" (projected) experiments. Let me also check for the review context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0aaa2fa-9182-4780-afbb-37fd3871a27a",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Z1WjdZJi99FHGGYXGd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d831b512-59c7-4011-acf7-a7e1abee5220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqfNGCbQ27wbKq4TsNdwPQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21870,
      "cache_read_input_tokens": 42978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21870,
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

_source line 38 · 2026-05-14T00:57:26.613Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tp6R3RY8hM5u7fmtfjvRPc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d831b512-59c7-4011-acf7-a7e1abee5220",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Z1WjdZJi99FHGGYXGd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67eb5def-3b09-471c-9953-54f93251d0fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqfNGCbQ27wbKq4TsNdwPQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21870,
      "cache_read_input_tokens": 42978,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21870
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 42978,
          "cache_creation_input_tokens": 21870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21870,
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

_source line 39 · 2026-05-14T00:57:26.917Z_

<details><summary>↩ Tool result · `toolu_01Tp6R3RY8hM5u7fmtfjvRPc`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。三条 claims 在 Qwen/Llama/Mistral 三模型、WikiText-2/C4
2	  双数据集上 完整成立。compounding effect 有干净的 elbow curve（SNR≥5），solver 在去掉 L0 exclusion 后
3	  仍自动将 8-bit 分配给 Layer 0 heads。叙事核心："cardinality-constrained MCKP as principled regularization
4	  for compounding effects"。与 RateQuant 差异化清晰：discrete vs continuous + compounding
5	  regularization 是 qualitatively different contribution。论文可以直接用 "三模型一致性"作为 generalizability
6	  的强证据，用 compounding elbow curve 作为 cardinality constraint 的 principled motivation。
7	
8	  '
9	imagined_experiments:
10	- name: L0 Auto-Discovery (No Exclusion)
11	  plan_id: plan_001
12	  description: '移除 solver 中的 L0 exclusion 硬约束，仅保留 max_2bit=8 的 cardinality constraint。
13	    验证 solver 是否仅凭 profiling delta 数据自动将 8-bit 分配给 Layer 0 全部 4 个 KV heads。
14	
15	    '
16	  expected_results:
17	    l0_auto_discovery: true
18	    l0_heads_assigned_8bit: 4/4 (100%)
19	    ppl_wikitext: 11.28
20	    ppl_delta_vs_with_exclusion: 0.05
21	    allocation_agreement_with_exclusion: 108/112 heads identical (96.4%)
22	    solver_time_seconds: 0.03
23	  result_rationale: 'Layer 0 heads 的 profiling delta 比 mid-layer heads 高 ~100×（delta
24	    ≈ 2.1 vs 均值 0.02）。 在 MCKP 的 objective 中，将 L0 heads 从 4-bit 提升到 8-bit 的边际收益远超任何
25	    mid-layer head， 因此即使没有 exclusion 硬约束，纯 cost-benefit optimization 也会自动选择保护 L0。
26	    PPL 几乎不变（+0.05）是因为 solver 自由度增加后在 mid-layer 有微小重分配，但 L0 保护 这个核心决策完全一致。少数 4 个 head
27	    的分配差异出现在 delta 接近的 mid-layer 边界 heads。
28	
29	    '
30	  tables:
31	  - name: 'Table: L0 Head Allocation Comparison'
32	    columns:
33	    - Head
34	    - Delta (×10⁻²)
35	    - With Exclusion
36	    - Without Exclusion
37	    rows:
38	    - - L0-H0
39	      - '215.3'
40	      - 8-bit (forced)
41	      - 8-bit (auto)
42	    - - L0-H1
43	      - '198.7'
44	      - 8-bit (forced)
45	      - 8-bit (auto)
46	    - - L0-H2
47	      - '201.4'
48	      - 8-bit (forced)
49	      - 8-bit (auto)
50	    - - L0-H3
51	      - '189.2'
52	      - 8-bit (forced)
53	      - 8-bit (auto)
54	    - - L1-H0
55	      - '3.41'
56	      - 4-bit
57	      - 4-bit
58	    - - avg mid-layer
59	      - '1.87'
60	      - 4-bit
61	      - 4-bit
62	  - name: 'Table: PPL Comparison'
63	    columns:
64	    - Configuration
65	    - PPL (WikiText-2)
66	    rows:
67	    - - Constrained MCKP (with L0 exclusion)
68	      - '11.23'
69	    - - Constrained MCKP (without L0 exclusion)
70	      - '11.28'
71	    - - Uniform 4-bit
72	      - '15.45'
73	  figures_description:
74	  - 'Bar chart: per-head bit-width allocation side-by-side (with vs without exclusion),
75	    color-coded by bit-width. Visual emphasis on L0 heads being identical in both
76	    conditions.'
77	  analysis: '这是论文中最具叙事力的实验之一。它把 "solver automatically discovers architectural sensitivity
78	    structure" 从修辞变成了实证。4/4 L0 heads 被自动发现说明 profiling delta 的 signal-to-noise 足够高，不需要任何领域先验。96.4%
79	    的 allocation 一致率说明 exclusion constraint 本来就是冗余的——solver 自己就会做出正确决策。 PPL 差异 <0.5%
80	    进一步确认了这一点。论文叙事可以正面使用： "We initially included L0 exclusion as a safety constraint,
81	    but found the solver independently discovers L0 criticality from profiling data
82	    alone."
83	
84	    '
85	- name: Llama-3.1-8B Full Pipeline
86	  plan_id: plan_002
87	  description: '在 Llama-3.1-8B（GQA 4:1, 8 KV heads/layer × 32 layers = 256 KV heads）上
88	    完整复现 pipeline：profiling → constrained MCKP → evaluation。
89	
90	    '
91	  expected_results:
92	    fp16_baseline_ppl: 6.24
93	    uniform_4bit_ppl: 8.95
94	    constrained_mckp_ppl: 6.78
95	    unconstrained_mckp_ppl: 14.31
96	    ppl_improvement_pct: 24.2
97	    max_2bit_used: 16
98	    l0_heads_assigned_8bit: 8/8 (100%)
99	    heads_at_2bit: 16
100	    heads_at_4bit: 192
101	    heads_at_8bit: 32
102	    heads_at_16bit: 16
103	    compression_ratio: 3.97×
104	    top_sensitive_heads_pct: 4.7%
105	    top_sensitive_heads_ppl_contribution_pct: 65%
106	  result_rationale: 'Llama-3.1-8B 的 GQA ratio 为 4:1（32 query heads / 8 KV heads），KV
107	    heads 数量是 Qwen 的 2.3 倍（256 vs 112）。更多的 heads 意味着 per-head 分配的自由度更高，MCKP 有更大的 优化空间。但
108	    GQA 4:1 也意味着每个 KV head 被更少的 query heads 共享（4 vs 7）， 所以单个 head 的影响力相对更分散，sensitivity
109	    heterogeneity 可能略低于 Qwen。 24.2% 的 PPL improvement 在 best tier 范围 [20,30] 内，略低于
110	    Qwen 的 27% 是因为 Llama 的 attention head 结构更均匀（GQA ratio 更低→ per-KV-head 影响更分散）。
111	    Unconstrained MCKP 仍然崩溃（14.31 vs 6.78）确认 compounding effect 在不同架构上一致存在， 但绝对恶化程度低于
112	    Qwen（Qwen 36.92/11.23 = 3.3× vs Llama 14.31/6.78 = 2.1×）， 因为 256 heads 中同时被分配
113	    2-bit 的比例在相同 max_2bit 约束下更低。 L0 dominance pattern 复现：Layer 0 的 8 个 KV heads profiling
114	    delta 显著高于其他层。
115	
116	    '
117	  tables:
118	  - name: 'Table: Llama-3.1-8B Allocation Results'
119	    columns:
120	    - Method
121	    - PPL ↓
122	    - Compression
123	    - Heads@2bit
124	    - Heads@8bit+
125	    rows:
126	    - - FP16 (baseline)
127	      - '6.24'
128	      - 1×
129	      - '0'
130	      - '256'
131	    - - Uniform 4-bit
132	      - '8.95'
133	      - 4×
134	      - '0'
135	      - '0'
136	    - - Unconstrained MCKP
137	      - '14.31'
138	      - 4×
139	      - '89'
140	      - '24'
141	    - - Constrained MCKP (max_2bit=16)
142	      - '6.78'
143	      - 4×
144	      - '16'
145	      - '48'
146	  - name: 'Table: Layer 0 Sensitivity (Llama)'
147	    columns:
148	    - Head
149	    - Delta (×10⁻²)
150	    - Assigned
151	    rows:
152	    - - L0-H0 ~ L0-H7
153	      - 58.3 ~ 89.1
154	      - all 8-bit
155	    - - L1-H0 ~ L1-H7
156	      - 2.1 ~ 4.8
157	      - mixed 4/8-bit
158	    - - avg mid-layer
159	      - '0.9'
160	      - 4-bit
161	  figures_description:
162	  - 'Heatmap: 32×8 grid of per-head profiling delta for Llama-3.1-8B, showing L0 dominance
163	    and sparse mid-layer heterogeneity.'
164	  - 'Side-by-side allocation map: Qwen (28×4) vs Llama (32×8), demonstrating consistent
165	    L0 protection pattern across architectures.'
166	  analysis: 'Llama-3.1-8B 的成功复现是论文 generalizability 的关键支撑。GQA 4:1 vs 7:1 的差异 测试了方法对不同
167	    KV head 共享结构的鲁棒性。24.2% 的改进虽然略低于 Qwen 的 27%， 但仍然显著且一致。unconstrained 崩溃的复现（2.1×
168	    恶化）确认 compounding effect 不是 Qwen 特有的 artifact。跨架构 L0 dominance 的一致性支持 Claim 1
169	    的强形式： "Layer 0 sensitivity is an architectural invariant, not a model-specific
170	    phenomenon."
171	
172	    '
173	- name: Mistral-7B-v0.3 Full Pipeline
174	  plan_id: plan_003
175	  description: '在 Mistral-7B-v0.3（GQA 4:1, 8 KV heads/layer × 32 layers = 256 KV heads，
176	    sliding window attention）上完整复现 pipeline。
177	
178	    '
179	  expected_results:
180	    fp16_baseline_ppl: 7.01
181	    uniform_4bit_ppl: 9.87
182	    constrained_mckp_ppl: 7.68
183	    unconstrained_mckp_ppl: 16.54
184	    ppl_improvement_pct: 22.2
185	    max_2bit_used: 14
186	    l0_heads_assigned_8bit: 8/8 (100%)
187	    heads_at_2bit: 14
188	    heads_at_4bit: 198
189	    heads_at_8bit: 28
190	    heads_at_16bit: 16
191	    compression_ratio: 3.98×
192	    sliding_window_impact: window boundary layers show elevated sensitivity
193	  result_rationale: 'Mistral-7B-v0.3 使用 sliding window attention（window=4096），这在 KV
194	    cache 的使用模式 上与 full attention 不同：window 边界附近的 layers 承担更多的"信息中继"职责， sensitivity
195	    分布可能比 Llama 更不均匀。22.2% 的 PPL improvement 在 best tier 范围 [18,28] 内，略低于 Llama 的
196	    24.2%，因为 Mistral 的 sliding window 使得 KV cache 在长序列上的有效利用率本来就较高（无需缓存超出 window 的
197	    KV），4-bit uniform 对 Mistral 的相对伤害比 full-attention 模型更小。但 constrained MCKP 仍然显著优于
198	    uniform，确认方法在 sliding window 架构下同样有效。 L0 dominance pattern 第三次复现：即使有 sliding window，Layer
199	    0 heads 仍然是最敏感的， 因为它们处理的是 token embedding 的直接变换，与 attention pattern 无关。
200	
201	    '
202	  tables:
203	  - name: 'Table: Mistral-7B Results'
204	    columns:
205	    - Method
206	    - PPL ↓
207	    - Compression
208	    - Improvement
209	    rows:
210	    - - FP16 (baseline)
211	      - '7.01'
212	      - 1×
213	      - —
214	    - - Uniform 4-bit
215	      - '9.87'
216	      - 4×
217	      - —
218	    - - Unconstrained MCKP
219	      - '16.54'
220	      - 4×
221	      - −67.6%
222	    - - Constrained MCKP
223	      - '7.68'
224	      - 4×
225	      - +22.2%
226	  figures_description:
227	  - Per-head delta heatmap for Mistral, annotating sliding window boundary layers
228	    with elevated sensitivity.
229	  analysis: '三模型中最低的 PPL improvement（22.2%），但仍在 best tier 范围内。Sliding window 是一个有意义的
230	    architectural variation，成功复现说明方法不依赖于 full attention 假设。 论文可以额外指出 sliding window
231	    boundary layers 的 elevated sensitivity 作为 一个 interesting observation，但不要过度解释。
232	
233	    '
234	- name: Compounding Effect Elbow Curve
235	  plan_id: plan_004
236	  description: '在 Qwen2.5-7B 上 sweep max_2bit 从 0 到 112（全部 KV heads）， 8 个点：0, 4, 8,
237	    16, 24, 48, 75, 112。绘制 PPL vs max_2bit 曲线， 定位 compounding threshold（elbow point）。
238	
239	    '
240	  expected_results:
241	    sweep_results:
242	      max_2bit_0:
243	        ppl: 12.01
244	        heads_at_2bit: 0
245	        note: no 2-bit allowed, solver uses 4/8/16 only
246	      max_2bit_4:
247	        ppl: 11.34
248	        heads_at_2bit: 4
249	        note: 4 most expendable heads at 2-bit, frees budget for 8-bit on L0
250	      max_2bit_8:
251	        ppl: 11.08
252	        heads_at_2bit: 8
253	        note: near-optimal, all freed budget protecting critical heads
254	      max_2bit_16:
255	        ppl: 11.52
256	        heads_at_2bit: 16
257	        note: slight degradation begins, compounding starts
258	      max_2bit_24:
259	        ppl: 13.41
260	        heads_at_2bit: 24
261	        note: clear compounding, 2-bit heads interacting
262	      max_2bit_48:
263	        ppl: 21.87
264	        heads_at_2bit: 48
265	        note: severe compounding, 43% of heads at extreme quant
266	      max_2bit_75:
267	        ppl: 30.12
268	        heads_at_2bit: 67
269	        note: catastrophic, solver can't use all 75 slots optimally
270	      max_2bit_112:
271	        ppl: 36.92
272	        heads_at_2bit: 78
273	        note: unconstrained equivalent, full compounding
274	    elbow_k: 12
275	    elbow_snr: 7.3
276	    optimal_k: 8
277	    optimal_ppl: 11.08
278	    pre_elbow_slope: 0.055
279	    post_elbow_slope: 1.29
280	  result_rationale: 'Compounding effect 的物理机制：当多个 heads 同时被 quantize 到 2-bit 时，每个
281	    head 的 quantization error 通过 residual stream 传播到下游 layers。单个 head 的 2-bit error
282	    可以被其他 head 的正常精度"吸收"，但当足够多的 heads 同时 degraded 时，error 累积 超过模型的 error correction
283	    capacity。这是一个典型的 threshold phenomenon。 elbow 在 k≈8-12 是因为 Qwen2.5-7B 有 112 个 KV
284	    heads（28 layers × 4 heads）， 当 ~7-10% 的 heads 被设为 2-bit 时达到 compounding onset。k=8（7.1%
285	    of heads） 是 optimal：此时 freed budget 恰好足够保护所有 critical heads（L0 + 少量 high-delta
286	    mid-layer heads）at 8/16-bit，而 2-bit heads 都是 truly expendable 的。 SNR=7.3 远超阈值
287	    5，说明 elbow 是 sharp 的，不是 gradual degradation。 pre-elbow slope 0.055 PPL/head 说明在
288	    safe region 内每增加一个 2-bit head 几乎 无影响；post-elbow slope 1.29 PPL/head 说明超过 elbow
289	    后每增加一个 2-bit head 带来 >1 PPL 的恶化——23× 的 slope ratio 是 compounding non-additivity
290	    的直接证据。
291	
292	    '
293	  tables:
294	  - name: 'Table: Compounding Effect Sweep'
295	    columns:
296	    - max_2bit (k)
297	    - PPL ↓
298	    - Δ PPL vs k=0
299	    - Heads@2bit
300	    - '% Heads@2bit'
301	    rows:
302	    - - '0'
303	      - '12.01'
304	      - —
305	      - '0'
306	      - 0%
307	    - - '4'
308	      - '11.34'
309	      - −0.67
310	      - '4'
311	      - 3.6%
312	    - - '8'
313	      - '11.08'
314	      - −0.93
315	      - '8'
316	      - 7.1%
317	    - - '16'
318	      - '11.52'
319	      - −0.49
320	      - '16'
321	      - 14.3%
322	    - - '24'
323	      - '13.41'
324	      - '+1.40'
325	      - '24'
326	      - 21.4%
327	    - - '48'
328	      - '21.87'
329	      - '+9.86'
330	      - '48'
331	      - 42.9%
332	    - - '75'
333	      - '30.12'
334	      - '+18.11'
335	      - '67'
336	      - 59.8%
337	    - - '112'
338	      - '36.92'
339	      - '+24.91'
340	      - '78'
341	      - 69.6%
342	  figures_description:
343	  - '核心 Figure：PPL vs max_2bit (k) 曲线。X 轴为 max_2bit constraint value， Y 轴为 PPL（log
344	    scale）。标注 elbow point (k=12) 和 optimal point (k=8)。 用灰色 band 标注 "safe zone" (k≤12)
345	    和 "compounding zone" (k>12)。 右侧 y 轴叠加 Δ PPL per additional 2-bit head（local slope），
346	    清晰展示 slope 在 elbow 处的 discontinuity。
347	
348	    '
349	  - 'Inset figure：log-log plot of residual PPL increment vs k， 展示 pre-elbow region
350	    为 sublinear（additive model valid）、 post-elbow region 为 superlinear（compounding
351	    dominates）。
352	
353	    '
354	  analysis: '这是论文的 signature figure，直接支撑 Claim 3。elbow curve 提供了 cardinality constraint
355	    的 principled justification：不是 arbitrary heuristic，而是 compounding non-additivity
356	    的 empirical boundary。23× slope ratio 是一个 striking result，可以用一句话总结论文的核心发现： "Below
357	    the compounding threshold, per-head distortion is approximately additive (slope=0.055);
358	    above it, each additional extreme-quantized head incurs 23× more damage due to
359	    error propagation through the residual stream." 建议在论文 Introduction 的 Figure 1
360	    位置放置此图。
361	
362	    '
363	- name: Budget Sweep (2×/4×/8× Compression)
364	  plan_id: plan_005
365	  description: '在 Qwen2.5-7B 上测试 constrained MCKP 在三个压缩比下的表现： 2×（budget=0.5）、4×（budget=0.25）、8×（budget=0.125），
366	    每个压缩比与同 budget 的 uniform baseline 对比。
367	
368	    '
369	  expected_results:
370	    results_2x:
371	      uniform_8bit_ppl: 10.12
372	      constrained_mckp_ppl: 9.94
373	      improvement_pct: 1.8
374	      allocation: mostly 8-bit with 12 heads at 16-bit, 8 heads at 4-bit
375	    results_4x:
376	      uniform_4bit_ppl: 15.45
377	      constrained_mckp_ppl: 11.08
378	      improvement_pct: 28.3
379	      allocation: 8 heads@2bit, 76 heads@4bit, 20 heads@8bit, 8 heads@16bit
380	    results_8x:
381	      uniform_2bit_ppl: 78.34
382	      constrained_mckp_ppl: 28.67
383	      improvement_pct: 63.4
384	      allocation: 64 heads@2bit, 32 heads@4bit, 12 heads@8bit, 4 heads@16bit
385	    fp16_baseline: 9.82
386	  result_rationale: '不同压缩比下 MCKP 优势的差异源于 sensitivity heterogeneity 的利用空间： (1) 2× 压缩：budget
387	    充裕，uniform 8-bit 已经接近 FP16（+3.1%），MCKP 只能通过 将少量 insensitive heads 降到 4-bit 并将
388	    freed budget 给最 sensitive heads 升到 16-bit 来获得微小改进。1.8% 的 improvement 虽小但说明 heterogeneity
389	    确实存在。 (2) 4× 压缩：sweet spot——uniform 4-bit 已有 57% 的 PPL degradation，而 MCKP 可以充分利用
390	    head 间的 sensitivity 差异。28.3% 的 improvement 是 headline result。 (3) 8× 压缩：uniform
391	    2-bit 是灾难性的（PPL 78.34, 8× baseline），MCKP 通过 保护 ~15% 的 critical heads 在 8/16-bit
392	    将 PPL 控制在 28.67——仍然很差， 但比 uniform 好 63.4%。这说明即使在极端压缩下，intelligent allocation 仍然
393	    有巨大价值，但也诚实地表明 8× 压缩的绝对质量不够实用。 整体趋势：MCKP 的相对优势随压缩比增加而增大，因为更激进的压缩放大了 sensitivity
394	    heterogeneity 的重要性。
395	
396	    '
397	  tables:
398	  - name: 'Table: Budget Sweep Results (Qwen2.5-7B, WikiText-2)'
399	    columns:
400	    - Compression
401	    - Budget
402	    - Uniform PPL
403	    - MCKP PPL
404	    - Improvement
405	    - Δ vs FP16
406	    rows:
407	    - - 2×
408	      - '0.50'
409	      - '10.12'
410	      - '9.94'
411	      - 1.8%
412	      - +1.2%
413	    - - 4×
414	      - '0.25'
415	      - '15.45'
416	      - '11.08'
417	      - 28.3%
418	      - +12.8%
419	    - - 8×
420	      - '0.125'
421	      - '78.34'
422	      - '28.67'
423	      - 63.4%
424	      - +192%
425	    - - FP16
426	      - '1.00'
427	      - '9.82'
428	      - —
429	      - —
430	      - —
431	  figures_description:
432	  - '双 Y 轴图：左 Y 轴为 PPL（log scale），X 轴为 compression ratio， 两条线（uniform vs constrained
433	    MCKP）。右 Y 轴为 improvement percentage。 Fan-out pattern 清晰展示：压缩比越高，MCKP 优势越大。 标注
434	    4× 为 "practical sweet spot"。
435	
436	    '
437	  analysis: 'Budget sweep 回应了 reviewer concern #4（"How does this work at different
438	    compression ratios?"）。1.8% → 28.3% → 63.4% 的递增趋势是一个 clean story： mixed-precision
439	    的价值在压缩压力大时最显著。4× 是论文的 headline compression ratio， 既是实际部署最常见的 target，也是 MCKP 优势最
440	    striking 的 sweet spot。 8× 的结果可以诚实报告：MCKP 大幅优于 uniform 但绝对 PPL 仍然高， 说明方法的局限性（不能
441	    violate information-theoretic limits）。
442	
443	    '
444	- name: High-Resolution Profiling
445	  plan_id: plan_006
446	  description: '将 profiling 从 16 seq × 512 tokens 提升到 64 seq × 2048 tokens（8× 数据量）。
447	    在 Qwen2.5-7B 上重新 profile，rerun MCKP，评估是否能区分 mid-layer heads。
448	
449	    '
450	  expected_results:
451	    lores_nonzero_head_pct: 16.1
452	    hires_nonzero_head_pct: 58.0
453	    lores_delta_std_midlayers: 0.0003
454	    hires_delta_std_midlayers: 0.0089
455	    hires_mckp_ppl: 10.72
456	    lores_mckp_ppl: 11.08
457	    ppl_improvement_from_hires: 3.2
458	    new_sensitive_heads_discovered: 14
459	    l0_delta_change_pct: +2.1%
460	    mid_layer_delta_change_pct: +1400%
461	    profiling_time_hours: 2.8
462	  result_rationale: '低分辨率 profiling（16×512 = 8K tokens）的 mid-layer delta 被 sampling
463	    noise 淹没：大多数 mid-layer heads 的 true delta 在 10⁻⁴ 量级，而 sampling variance 在 ~10⁻³
464	    量级，导致 84% 的 heads 被 round 到 delta=0。高分辨率（64×2048 = 128K tokens） 将 sampling variance
465	    降低 √16 ≈ 4×，使得 10⁻⁴ 量级的 true delta 开始可分辨。 58% nonzero（从 16.1% 提升）意味着约 47 个之前被认为
466	    delta=0 的 head 现在有了 可测量的 sensitivity signal。其中 14 个 head 的 delta 足够大以改变 MCKP allocation。
467	    3.2% 的 PPL improvement（10.72 vs 11.08）说明 mid-layer heterogeneity 确实存在且 有实际价值，但主要贡献仍来自
468	    L0 的 correct allocation（L0 delta 变化仅 2.1%， 说明 L0 signal 在低分辨率下就已经 saturated）。
469	    1400% 的 mid-layer delta std 提升是最 striking 的数字： 从 0.0003 到 0.0089，说明 mid-layer
470	    内部确实有显著的 head-level heterogeneity， 只是之前被 noise 掩盖了。
471	
472	    '
473	  tables:
474	  - name: 'Table: Profiling Resolution Comparison'
475	    columns:
476	    - Metric
477	    - Lo-Res (16×512)
478	    - Hi-Res (64×2048)
479	    - Change
480	    rows:
481	    - - Total profiling tokens
482	      - 8,192
483	      - 131,072
484	      - 16×
485	    - - Nonzero-delta heads
486	      - 18/112 (16.1%)
487	      - 65/112 (58.0%)
488	      - +261%
489	    - - Mid-layer delta std
490	      - 3×10⁻⁴
491	      - 8.9×10⁻³
492	      - +1400%
493	    - - L0 avg delta
494	      - '2.08'
495	      - '2.12'
496	      - +2.1%
497	    - - MCKP PPL
498	      - '11.08'
499	      - '10.72'
500	      - −3.2%
501	    - - Allocation changes vs lo-res
502	      - —
503	      - 14 heads
504	      - —
505	    - - Profiling wall-time
506	      - 0.4h
507	      - 2.8h
508	      - 7×
509	  - name: 'Table: Discovered Mid-Layer Sensitive Heads'
510	    columns:
511	    - Head
512	    - Lo-Res Delta
513	    - Hi-Res Delta
514	    - New Allocation
515	    rows:
516	    - - L12-H2
517	      - '0.000'
518	      - '0.0134'
519	      - 4→8 bit
520	    - - L15-H0
521	      - '0.000'
522	      - '0.0118'
523	      - 4→8 bit
524	    - - L7-H3
525	      - '0.000'
526	      - '0.0097'
527	      - 4→8 bit
528	    - - L21-H1
529	      - '0.000'
530	      - '0.0091'
531	      - 2→4 bit
532	    - - '... (10 more)'
533	      - —
534	      - —
535	      - —
536	  figures_description:
537	  - '双面板 heatmap：左为 lo-res delta（28×4 grid，大量 white=0）， 右为 hi-res delta（同 grid，明显更多
538	    non-zero entries，color gradient 揭示 mid-layer heterogeneity）。共享 colorbar（log scale）。
539	
540	    '
541	  - 'Histogram：lo-res vs hi-res delta 分布，展示 hi-res 下 delta=0 的 spike 大幅缩小，被一个 continuous
542	    distribution 取代。
543	
544	    '
545	  analysis: '高分辨率 profiling 的 3.2% PPL improvement 不大，但它的主要价值是 scientific： 证明了 mid-layer
546	    heterogeneity 的存在（之前被 noise 掩盖），使 Claim 1 从 "L0 dominates" 扩展为 "sensitivity is
547	    hierarchically structured — L0 dominates, but mid-layer heterogeneity also matters
548	    at finer resolution"。 论文建议：hi-res profiling 可以作为一个 optional enhancement， main
549	    results 使用 lo-res（更实用），hi-res 在 analysis section 展示 以支持 Claim 1 的完整叙事。2.8h 的 profiling
550	    成本说明 hi-res 在实践中 不是 free 的，但对于 one-time offline allocation 是可接受的。
551	
552	    '
553	- name: C4 Cross-Dataset Evaluation
554	  plan_id: plan_007
555	  description: '在 Qwen2.5-7B 上用 WikiText-2 calibrated allocations 在 C4 上评估， 同时用 C4
556	    数据 rerun profiling + MCKP 并在 C4 上评估。 计算两种 allocation 的 rank correlation。
557	
558	    '
559	  expected_results:
560	    c4_fp16_ppl: 11.87
561	    c4_uniform_4bit_ppl: 17.42
562	    c4_constrained_mckp_ppl_wikitext_calib: 12.61
563	    c4_constrained_mckp_ppl_c4_calib: 12.48
564	    c4_ppl_improvement_pct: 27.6
565	    wikitext_c4_rank_correlation: 0.94
566	    allocation_agreement_rate: 101/112 heads (90.2%)
567	    l0_protection_consistent: true
568	    cross_calib_ppl_gap: 0.13
569	  result_rationale: 'C4 是 web-crawl 数据，domain 比 WikiText-2 更广。PPL 绝对值更高（FP16 11.87
570	    vs 9.82） 是因为 C4 的 vocabulary diversity 和 noise。但 quantization sensitivity 的 relative
571	    ordering 高度一致（rank correlation 0.94）：哪些 heads 敏感、哪些不敏感， 这是 architectural property
572	    而非 data-dependent property。L0 heads 在 C4 profiling 下同样是最敏感的，进一步支持 "sensitivity
573	    is architecturally determined"。 90.2% 的 allocation agreement 说明 WikiText-2 calibrated
574	    allocation 在 C4 上 几乎同样有效（PPL gap 仅 0.13）。27.6% 的 improvement 与 WikiText-2 上的 28.3%
575	    接近，说明方法的效果不依赖于特定 dataset。 0.94 的 rank correlation 在 best tier 范围 [0.88, 0.98]
576	    内。
577	
578	    '
579	  tables:
580	  - name: 'Table: C4 Evaluation Results'
581	    columns:
582	    - Method
583	    - WikiText-2 PPL
584	    - C4 PPL
585	    - Improvement
586	    rows:
587	    - - FP16
588	      - '9.82'
589	      - '11.87'
590	      - —
591	    - - Uniform 4-bit
592	      - '15.45'
593	      - '17.42'
594	      - —
595	    - - Constrained MCKP (WT2-calib)
596	      - '11.08'
597	      - '12.61'
598	      - 27.6%
599	    - - Constrained MCKP (C4-calib)
600	      - —
601	      - '12.48'
602	      - 28.3%
603	    - - Unconstrained MCKP
604	      - '36.92'
605	      - '41.23'
606	      - −136.5%
607	  - name: 'Table: Cross-Dataset Calibration Robustness'
608	    columns:
609	    - Metric
610	    - Value
611	    rows:
612	    - - Rank correlation (head delta ordering)
613	      - '0.94'
614	    - - Allocation agreement (same bit-width)
615	      - 90.2%
616	    - - Cross-calib PPL gap
617	      - '0.13'
618	    - - L0 8-bit protection consistent
619	      - 'Yes'
620	  figures_description:
621	  - 'Scatter plot：WikiText-2 per-head delta (x-axis) vs C4 per-head delta (y-axis)，
622	    112 个点，标注 Spearman ρ=0.94。L0 heads 用不同 marker 标注， 位于右上角，远离 cluster。
623	
624	    '
625	  analysis: 'C4 实验完成了 "multi-dataset" 维度的验证。0.94 的 rank correlation 和 90.2% 的 allocation
626	    agreement 是强结果，支持论文的核心论点：per-head sensitivity 是 architectural property，calibration
627	    dataset 的选择不 critical。 Cross-calib PPL gap 仅 0.13 说明在实际部署中可以用任何 reasonable dataset
628	    做 one-time calibration，不需要 task-specific profiling。
629	
630	    '
631	- name: RateQuant Baseline Comparison
632	  plan_id: plan_008
633	  description: '实现 RateQuant 的 reverse waterfilling 算法，应用在我们的 discrete action set
634	    {2,4,8,16}-bit 上（rounding to nearest）。在 Llama-3.1-8B 上与 constrained MCKP 对比。
635	
636	    '
637	  expected_results:
638	    ratequant_continuous_optimal_bits: avg 4.0 (continuous)
639	    ratequant_rounded_ppl: 8.12
640	    constrained_mckp_ppl: 6.78
641	    uniform_4bit_ppl: 8.95
642	    ratequant_improvement_vs_uniform: 9.3
643	    mckp_improvement_vs_uniform: 24.2
644	    mckp_improvement_vs_ratequant: 16.5
645	    ratequant_heads_at_2bit: 38
646	    ratequant_l0_protection: partial (5/8 heads at 8-bit, 3 at 4-bit)
647	  result_rationale: 'RateQuant 的 reverse waterfilling 假设 distortion D(b) = α·β^{-b}
648	    是 continuous 且 additive 的。在 continuous regime 下这给出 R-D optimal allocation。但 rounding
649	    to discrete {2,4,8,16} 引入两个问题： (1) Rounding loss：continuous 5.3-bit 被 round 到
650	    4-bit 或 8-bit，两者都不是 optimal。MCKP 直接在 discrete space 上优化，避免了 rounding suboptimality。
651	    (2) Compounding blindness：waterfilling 没有 cardinality constraint，round 后 38 个
652	    heads 被分配 2-bit（vs MCKP 的 16 个），超过 compounding threshold。 这导致 PPL 8.12——比 uniform
653	    好（9.3%）但远逊于 constrained MCKP（6.78）。 L0 保护不完整（仅 5/8 at 8-bit）是因为 waterfilling 的
654	    continuous optimal 对 L0 的某些 heads 分配了 ~6-7 bit，round 到 4 或 8 取决于 arbitrary threshold。
655	    16.5% 的 MCKP vs RateQuant 优势直接支撑论文的 core differentiation。
656	
657	    '
658	  tables:
659	  - name: 'Table: RateQuant vs Constrained MCKP (Llama-3.1-8B)'
660	    columns:
661	    - Method
662	    - PPL ↓
663	    - Impr. vs Uniform
664	    - Heads@2bit
665	    - L0 at 8-bit
666	    rows:
667	    - - Uniform 4-bit
668	      - '8.95'
669	      - —
670	      - '0'
671	      - 0/8
672	    - - RateQuant (rounded)
673	      - '8.12'
674	      - 9.3%
675	      - '38'
676	      - 5/8
677	    - - Unconstrained MCKP
678	      - '14.31'
679	      - −59.9%
680	      - '89'
681	      - 8/8
682	    - - Constrained MCKP
683	      - '6.78'
684	      - 24.2%
685	      - '16'
686	      - 8/8
687	  figures_description:
688	  - 'Side-by-side allocation heatmaps (32×8)：RateQuant rounded vs Constrained MCKP。
689	    标注 L0 row 差异（RateQuant 的 3 个 L0 heads 未被保护）和 2-bit 分布差异 （RateQuant 散布过多 2-bit
690	    heads）。
691	
692	    '
693	  analysis: '这是论文 differentiation 的实证基础。RateQuant 失败的两个原因清晰可分： rounding loss 和 compounding
694	    blindness。论文可以构造一个 didactic example： "RateQuant assigns continuous 5.7 bits to
695	    L0-H3 (optimal under continuous assumption), but rounding to 4-bit causes 4.2×
696	    more distortion than rounding to 8-bit — a loss that MCKP avoids by directly optimizing
697	    in discrete space." 结合 L0 partial protection failure，这给出了一个 compelling narrative：continuous
698	    methods fail at the granularity that matters.
699	
700	    '
701	- name: Oracle Comparison (Subset Brute-Force)
702	  plan_id: plan_009
703	  description: '在 Qwen2.5-7B 的 4 个 layer groups（each 7 layers, 28 heads per group）上
704	    brute-force enumerate 所有 allocation，计算 MCKP 与 true oracle 的 gap。
705	
706	    '
707	  expected_results:
708	    group_1_layers: L0-L6
709	    group_1_mckp_ppl: 10.89
710	    group_1_oracle_ppl: 10.82
711	    group_1_gap: 0.6%
712	    group_2_layers: L7-L13
713	    group_2_mckp_ppl: 11.01
714	    group_2_oracle_ppl: 10.97
715	    group_2_gap: 0.4%
716	    group_3_layers: L14-L20
717	    group_3_mckp_ppl: 11.04
718	    group_3_oracle_ppl: 11.02
719	    group_3_gap: 0.2%
720	    group_4_layers: L21-L27
721	    group_4_mckp_ppl: 10.98
722	    group_4_oracle_ppl: 10.95
723	    group_4_gap: 0.3%
724	    overall_estimated_gap: <1%
725	    brute_force_configs_evaluated: 4^28 per group ≈ 7.2×10^16 (sampled 10^6 + DP)
726	  result_rationale: 'MCKP 是 NP-hard in general，但我们的 instance 结构良好：(1) items (heads)
727	    在 profiling delta 上有 clear separation（不是 adversarial instance）， (2) budget constraint
728	    是 linear，(3) 每个 head 的 action set 只有 4 个选项。 在这种 "benign" instance 上，greedy-based
729	    MCKP solver（通过 LP relaxation + rounding）接近 optimal。<1% 的 gap 说明 constrained MCKP
730	    是 practically optimal， 不需要 exponential-time exact solver。Group 1（包含 L0）的 gap 最大（0.6%）
731	    是因为 L0 heads 的 extreme delta 创造了更大的 "opportunity cost" gradient， 但即使如此 gap 也很小。
732	
733	    '
734	  tables:
735	  - name: 'Table: MCKP vs Oracle Gap'
736	    columns:
737	    - Layer Group
738	    - MCKP PPL
739	    - Oracle PPL
740	    - Gap (%)
741	    rows:
742	    - - L0-L6
743	      - '10.89'
744	      - '10.82'
745	      - 0.6%
746	    - - L7-L13
747	      - '11.01'
748	      - '10.97'
749	      - 0.4%
750	    - - L14-L20
751	      - '11.04'
752	      - '11.02'
753	      - 0.2%
754	    - - L21-L27
755	      - '10.98'
756	      - '10.95'
757	      - 0.3%
758	  figures_description:
759	  - Bar chart：每个 group 的 MCKP PPL vs Oracle PPL，gap 用 annotation 标注。
760	  analysis: '<1% oracle gap 是一个 reassuring result。论文可以声明 "our constrained MCKP solver
761	    achieves near-optimal allocation" 并用此实验作为 evidence。 这是 P1 priority，如果时间紧可以缩减到
762	    2 个 groups。
763	
764	    '
765	- name: Cross-Domain Calibration Robustness
766	  plan_id: plan_010
767	  description: '用 C4 calibrate profiling，在 WikiText-2 上评估（反向也做）。 报告 per-head allocation
768	    agreement rate。
769	
770	    '
771	  expected_results:
772	    c4_calib_wikitext_eval_ppl: 11.21
773	    wikitext_calib_wikitext_eval_ppl: 11.08
774	    wikitext_calib_c4_eval_ppl: 12.61
775	    c4_calib_c4_eval_ppl: 12.48
776	    cross_calib_ppl_penalty: 0.13 (WikiText), 0.13 (C4)
777	    allocation_agreement: 101/112 (90.2%)
778	    disagreement_analysis: 11 borderline mid-layer heads with delta ratio <1.5×
779	  result_rationale: 'Per-head sensitivity 主要由 weight matrix 结构决定（architectural property），
780	    calibration data 只影响 activation statistics 的 estimation。不同 domain 的 activation
781	    分布在大模型中高度 overlap（因为 pretrain data 本身就是 multi-domain）， 所以 calibration source 对
782	    sensitivity ranking 的影响很小。 90.2% agreement 中不一致的 11 个 heads 都是 borderline cases——delta
783	    接近 decision boundary 的 mid-layer heads，微小的 activation distribution shift 就足以翻转
784	    4-bit vs 2-bit 的决策。但这些 heads 本身就是 "doesn''t matter much" 的 heads（delta 很小），所以翻转对
785	    PPL 影响极小（0.13 penalty）。
786	
787	    '
788	  tables:
789	  - name: 'Table: Cross-Calibration Matrix'
790	    columns:
791	    - Calibration →
792	    - 'Eval: WikiText-2'
793	    - 'Eval: C4'
794	    rows:
795	    - - WikiText-2
796	      - '11.08'
797	      - '12.61'
798	    - - C4
799	      - '11.21'
800	      - '12.48'
801	    - - Gap
802	      - '0.13'
803	      - '0.13'
804	  figures_description:
805	  - 'Confusion matrix 风格的 2×2 heatmap，cells 为 PPL 值， diagonal 为 matched calibration，off-diagonal
806	    为 cross-calibration。
807	
808	    '
809	  analysis: 'Cross-calibration robustness 回答了一个 practical deployment question： "Do
810	    I need task-specific calibration data?" 答案是 no——0.13 的 cross-calib penalty 说明
811	    any reasonable text corpus works。这简化了 deployment story。
812	
813	    '
814	- name: Head Sensitivity Visualization
815	  plan_id: plan_011
816	  description: '生成论文质量的 figures：per-head delta heatmap, compounding curve, allocation
817	    comparison。
818	
819	    '
820	  expected_results:
821	    figures_generated: 4
822	    figure_1: Per-head profiling delta heatmap (28×4 for Qwen, 32×8 for Llama/Mistral)
823	    figure_2: Compounding effect elbow curve (from plan_004)
824	    figure_3: Budget allocation comparison bar charts (uniform vs MCKP at 3 compression
825	      ratios)
826	    figure_4: Cross-model L0 dominance comparison
827	  result_rationale: '这些 figures 直接对应论文的三条 claims：heatmap → Claim 1 (heterogeneity)，
828	    allocation comparison → Claim 2 (MCKP superiority)，elbow curve → Claim 3 (cardinality
829	    regularization)。Cross-model figure 是 generalizability 的 visual proof。
830	
831	    '
832	  tables: []
833	  figures_description:
834	  - 'Figure 1 (Paper Figure 2)：三模型 per-head delta heatmap 并排。 Log-scale colorbar。L0
835	    row 用 box 标注。每个 heatmap 下方加 一个 marginal bar chart 显示 per-layer aggregated delta。
836	
837	    '
838	  - 'Figure 2 (Paper Figure 1/Introduction)：Compounding elbow curve， annotated with
839	    safe zone / compounding zone。
840	
841	    '
842	  - 'Figure 3 (Paper Figure 3)：Grouped bar chart，三个 compression ratios， 每组三个 bars（uniform,
843	    unconstrained MCKP, constrained MCKP）。
844	
845	    '
846	  - 'Figure 4 (Paper Figure 4)：三模型 L0 delta vs rest-of-model delta 的 box plot，showing
847	    consistent 100× gap。
848	
849	    '
850	  analysis: 'Figure 1 (compounding curve) 和 Figure 2 (heatmap) 是论文最重要的两张图。 建议 Figure
851	    1 放在 Introduction，Figure 2 放在 Method section 的 motivation 段落。Figure 3 和 4 放在 Experiments
852	    section。
853	
854	    '
855	- name: Downstream Task Evaluation (MMLU / LongBench)
856	  plan_id: plan_012
857	  description: '在 Qwen2.5-7B 4× compression 下评估 MMLU（5-shot）和 LongBench。 验证 PPL improvement
858	    是否 transfer 到 downstream performance。
859	
860	    '
861	  expected_results:
862	    mmlu_fp16: 71.2
863	    mmlu_uniform_4bit: 65.8
864	    mmlu_constrained_mckp: 69.7
865	    mmlu_improvement_pct: 5.9
866	    longbench_fp16_avg: 48.3
867	    longbench_uniform_4bit_avg: 39.1
868	    longbench_constrained_mckp_avg: 45.8
869	    longbench_improvement_pct: 17.1
870	  result_rationale: 'MMLU 主要测 short-context factual knowledge retrieval，KV cache quantization
871	    对 MMLU 的影响相对较小（因为 sequence length 短，KV cache 的 cumulative error 小）。 所以 uniform
872	    4-bit 的 MMLU 下降不大（65.8 vs 71.2, −7.6%），MCKP 的 improvement 也相应较小（+5.9 pp 的 recovery）。
873	    LongBench 测 long-context tasks，KV cache quality 直接影响 long-range dependency 的保留。uniform
874	    4-bit 下降更大（39.1 vs 48.3, −19.0%），MCKP 的 recovery 也更显著 （+17.1 pp）。这符合预期：mixed-precision
875	    KV cache 的价值在 long-context 场景下 最大，因为 cumulative quantization error 在长序列上被 amplified。
876	    69.7 vs 71.2 的 MMLU（−2.1%）说明 constrained MCKP 在 4× 压缩下几乎无损。
877	
878	    '
879	  tables:
880	  - name: 'Table: Downstream Task Results (Qwen2.5-7B, 4× Compression)'
881	    columns:
882	    - Task
883	    - FP16
884	    - Uniform 4-bit
885	    - Constrained MCKP
886	    - Recovery %
887	    rows:
888	    - - MMLU (5-shot)
889	      - '71.2'
890	      - '65.8'
891	      - '69.7'
892	      - 72.2%
893	    - - LongBench (avg)
894	      - '48.3'
895	      - '39.1'
896	      - '45.8'
897	      - 72.8%
898	    - - WikiText-2 PPL ↓
899	      - '9.82'
900	      - '15.45'
901	      - '11.08'
902	      - 77.7%
903	  figures_description:
904	  - Radar chart 或 grouped bar chart：FP16 / Uniform / MCKP 在三个 metrics 上的对比。
905	  analysis: 'Downstream 结果确认 PPL improvement 不是 metric-hacking——实际 task performance
906	    也显著提升。LongBench 的 17.1% improvement 特别有说服力，因为 KV cache 在 long-context 场景下是 critical
907	    bottleneck。论文可以用 "72-78% of FP16-to-uniform degradation recovered by constrained
908	    MCKP" 作为 unified summary。 这是 P2，如果时间紧可以只做 MMLU（更快，更 standard benchmark）。
909	
910	    '
911	- name: 70B Profiling-Only (Scale Analysis)
912	  plan_id: plan_013
913	  description: '在 Qwen2.5-72B 上仅做 distortion profiling（不做 full eval）， 分析 sensitivity
914	    patterns 是否随 model size 变化。
915	
916	    '
917	  expected_results:
918	    total_kv_heads: 560
919	    layers: 80
920	    kv_heads_per_layer: 7
921	    l0_avg_delta: 3.47
922	    l0_delta_ratio_vs_mean: 142×
923	    mid_layer_nonzero_pct: 12.3% (lo-res)
924	    top_sensitive_pct: 2.8%
925	    top_sensitive_contribution: 74%
926	    compounding_threshold_estimated_k: ~20-30 (extrapolated)
927	    profiling_time_hours: 3.5
928	  result_rationale: '72B model 有 80 layers × 7 KV heads = 560 KV heads。L0 dominance
929	    更强（142× vs 100×） 是因为更深的 model 使得 L0 的 "information gateway" 角色更 critical—— 所有下游
930	    79 layers 都依赖 L0 产出的 representation。更大的 depth 意味着 L0 error 有更多 layers 来 accumulate。
931	    Top sensitive heads 占比从 3.6%（7B）降到 2.8%（72B）是因为 heads 总数增加 但 critical heads 数量增加更慢（L0
932	    的 7 heads + 少量 early-layer heads ≈ 15-16 heads）。 74% 的 contribution（vs 7B 的 70%）说明
933	    concentration 进一步加剧。 这支持一个 scaling hypothesis：模型越大，sensitivity heterogeneity 越强，
934	    mixed-precision 的 potential benefit 越大。
935	
936	    '
937	  tables:
938	  - name: 'Table: Sensitivity Scaling (7B vs 72B)'
939	    columns:
940	    - Metric
941	    - Qwen2.5-7B
942	    - Qwen2.5-72B
943	    - Trend
944	    rows:
945	    - - Total KV heads
946	      - '112'
947	      - '560'
948	      - 5×
949	    - - L0 delta ratio
950	      - 100×
951	      - 142×
952	      - ↑
953	    - - Top sensitive %
954	      - 3.6%
955	      - 2.8%
956	      - ↓ (more concentrated)
957	    - - Top contribution %
958	      - 70%
959	      - 74%
960	      - ↑
961	    - - Compounding threshold k
962	      - 8-12
963	      - ~20-30 (est.)
964	      - scales sub-linearly
965	  figures_description:
966	  - '80×7 heatmap for 72B, side-by-side with 28×4 heatmap for 7B (same colorscale)。
967	    Visual emphasis on increased sparsity of sensitive heads at larger scale。
968	
969	    '
970	  analysis: 70B profiling-only 是一个 "scaling teaser"——不做 full eval 但提供了 scale 维度的 evidence。142×
971	    L0 dominance 和 74% concentration 是 compelling numbers， 支持论文 Discussion 中的 "as
972	    models scale, the potential benefit of per-head mixed-precision allocation grows"
973	    论点。 P2 priority，如果时间紧可以放在 Appendix 或 Discussion 的一段话中。 不需要 full eval 就已经有足够的 narrative
974	    value。
975	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67eb5def-3b09-471c-9953-54f93251d0fb",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "080fbac0-2162-4c69-872c-7769cbe7be3c",
  "sourceToolAssistantUUID": "67eb5def-3b09-471c-9953-54f93251d0fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-14T00:57:32.780Z_

Now I have a comprehensive understanding of the paper, the actual vs. imagined experimental data, the decisions log, and the prior review. Let me now write my R2 review focused on Novelty and Related Work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "080fbac0-2162-4c69-872c-7769cbe7be3c",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Z23YY5R36fAYXxo1En",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0129ded-af4f-4769-be72-843affcaeaae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdDaY7j5ygrs9JNFRo5BZp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17200,
      "cache_read_input_tokens": 64848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17200,
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

_source line 41 · 2026-05-14T00:57:34.020Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KMPXU3yieDmm6vkZnuYjgw`</summary>

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
  "parentUuid": "c0129ded-af4f-4769-be72-843affcaeaae",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Z23YY5R36fAYXxo1En",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "553ca92f-6d93-43d8-93db-0411c2c62201",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdDaY7j5ygrs9JNFRo5BZp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17200,
      "cache_read_input_tokens": 64848,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17200
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 64848,
          "cache_creation_input_tokens": 17200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17200,
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

_source line 42 · 2026-05-14T00:57:34.022Z_

<details><summary>↩ Tool result · `toolu_01KMPXU3yieDmm6vkZnuYjgw`</summary>

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
  "parentUuid": "553ca92f-6d93-43d8-93db-0411c2c62201",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "24a0b2cb-524c-4421-a00b-f8140c545f89",
  "sourceToolAssistantUUID": "553ca92f-6d93-43d8-93db-0411c2c62201",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-14T00:57:47.067Z_



Now I have all the information needed. Let me cross-reference the actual experimental data against the paper's claims before writing the review.

Key discrepancies I've identified from the actual `compounding_sweep_results.csv`:
- **k=0**: Actual PPL = **15.4454** (= uniform 4-bit). Paper reports **12.01**. This is fabricated -- k=0 means no 2-bit heads allowed, so the solver can only use {4,8,16}, and at budget=0.25 the cheapest option is 4-bit, making it identical to uniform. The paper's 12.01 implies budget is being spent on 8-bit upgrades without any 2-bit "donors", which is physically impossible at budget=0.25.
- **k=8**: Actual PPL = **11.2312**. Paper reports **11.08**. Inflated.
- **k=4**: Actual PPL = **11.7706**. Paper reports **11.34**. Inflated.
- **k=75 and k=112**: Both actual PPL = **35.348** with identical allocations (75 heads at 2-bit). Paper reports 30.12 and 36.92 respectively.
- Only the Qwen 7B experiments are actually completed. Llama, Mistral, RateQuant comparison, downstream tasks, cross-dataset, oracle comparison, high-res profiling, and 72B scaling are all **imagined/projected**.

Now I'll write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24a0b2cb-524c-4421-a00b-f8140c545f89",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Z2ZLBKxUnJRxbgJBKG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3beed012-888e-4eda-9755-e807f6794fbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdHVfyYZZhwyDHj6sgJJqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 82048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 816,
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

_source line 44 · 2026-05-14T00:59:21.526Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01CLHW5J4q2RVBoFEVBuDo6a`</summary>

```json
{
  "report": "---\nreviewer: R2 (Novelty and Related Work)\nscore: 3/6 (Weak Reject)\nconfidence: 4/5\n---\n\n# Review: Cardinality-Constrained MCKP for Per-Head Mixed-Precision KV Cache Quantization\n\n## Summary\n\nThe paper formulates per-head KV cache bit-width allocation as a cardinality-constrained multiple-choice knapsack problem (MCKP) over discrete hardware-aligned bit-widths {2,4,8,16}. The main claimed contribution is that a cardinality constraint limiting the number of 2-bit head assignments regularizes compounding effects that independent per-head profiling cannot capture. Results on Qwen2.5-7B at 4x compression show 27% PPL improvement over uniform 4-bit. Multi-model and multi-dataset results are reported but appear to be projections rather than completed experiments.\n\n## Strengths\n\n- **Compounding effect observation is the genuine contribution.** The elbow curve showing a sharp transition from additive to compounding regimes (slope ratio ~23x) is an empirically interesting finding. This phenomenon -- that independent per-head profiling systematically overestimates feasibility of extreme assignments -- is underappreciated in the quantization literature and deserves documentation.\n\n- **Clean formulation.** The MCKP framing is mathematically well-posed, maps directly to hardware-supported precisions, and the solver is fast (<0.05s). The formulation is a natural and correct way to frame this problem.\n\n- **L0 auto-discovery experiment is convincing.** The solver independently assigns 8-bit to all Layer 0 heads without explicit constraints, with 96.4% allocation agreement. This demonstrates that the profiling signal is strong enough to guide optimization without domain heuristics.\n\n- **Honest acknowledgment of limitations.** The paper correctly notes that at 2x compression, MCKP advantage is marginal (actual: ~4.3%), and that 8x compression remains far from FP16 quality. This calibrated tone is appropriate.\n\n- **Practical relevance.** KV cache memory is a real deployment bottleneck, and a fast solver for bit-width allocation has clear practical value.\n\n## Weaknesses\n\n### Major\n\n- **(M1) The novelty is incremental over RateQuant.** RateQuant (May 2026) already performs per-head bit-width allocation via rate-distortion optimization. This paper's contribution reduces to two modifications: (a) changing the solver from continuous waterfilling to discrete MCKP, and (b) adding a cardinality constraint. Modification (a) is a straightforward engineering choice -- MCKP is a textbook optimization problem, and applying it to a discrete resource allocation setting is standard. Modification (b) is the genuine insight, but it is a single empirical heuristic. The paper itself acknowledges the cardinality constraint is not principled but empirical (Section 3.3: the bound k is \"determined empirically from the compounding curve\"). Despite language like \"principled regularization,\" this is post-hoc tuning of a single integer hyperparameter. The question for a top venue is whether \"apply MCKP + add a count constraint\" constitutes a sufficient contribution. I believe it does not, especially given that the cardinality trick could likely be added to RateQuant's greedy algorithm with similar effect -- and this ablation is conspicuously absent.\n\n- **(M2) RateQuant comparison is a strawman.** The paper compares only against RateQuant's continuous waterfilling with naive rounding to {2,4,8,16}. This is the weakest possible RateQuant variant. RateQuant provides a discrete greedy algorithm (Algorithm 1) with optimality guarantees on consecutive-integer bit-widths (Proposition 6). A fair comparison would: (a) apply RateQuant's greedy algorithm directly in discrete space, (b) add a cardinality constraint to RateQuant's allocator to isolate whether MCKP matters or only the constraint matters, (c) compare both methods without cardinality constraints to isolate the formulation advantage. Without these ablations, the 16.5% improvement over \"RateQuant\" is uninterpretable -- it may be entirely attributable to the cardinality constraint, meaning MCKP contributes nothing beyond what RateQuant + constraint would achieve.\n\n- **(M3) Critical data integrity issues.** Cross-referencing the paper's Table 3 (compounding sweep) against the actual experimental CSV reveals systematic fabrication:\n  - k=0: Paper reports PPL 12.01; actual data shows 15.4454 (identical to uniform 4-bit, which is the only physically consistent value -- at budget=0.25, the solver with no 2-bit option can only assign all heads to 4-bit)\n  - k=8: Paper reports 11.08; actual data shows 11.2312\n  - k=4: Paper reports 11.34; actual data shows 11.7706\n  - k=75 and k=112: Paper reports 30.12 and 36.92; actual data shows both are 35.348 with identical allocations\n  - The \"headline\" Qwen PPL of 11.08 does not match any actual experimental record (closest is 11.23)\n  \n  These are not rounding errors. The k=0 discrepancy is particularly damaging: reporting 12.01 instead of 15.45 makes the improvement over k=0 appear as a modest optimization (12.01 -> 11.08 = 7.7%) rather than what it actually is (mostly the same as uniform 4-bit). The paper's entire \"U-shaped curve\" narrative changes when k=0 is correctly reported as 15.45.\n\n- **(M4) Most experiments are imagined.** Of the 11 experimental tables in the paper, approximately 7-8 report projected rather than actual results. The Llama-3.1-8B, Mistral-7B-v0.3, RateQuant comparison, oracle comparison, cross-dataset evaluation, downstream tasks, high-resolution profiling, and 72B scaling experiments appear to be \"dream\" projections with fabricated numbers. Cross-model consistency is a headline claim but rests on no actual cross-model data.\n\n- **(M5) Missing devastating baseline: L0-only heuristic.** Project records indicate that simply protecting Layer 0 heads at 8-bit while keeping everything else at uniform 4-bit achieves PPL ~10.62 on Qwen2.5-7B -- potentially *better* than the constrained MCKP result of ~11.23. If confirmed, this collapses the entire optimization story: a trivial 4-line heuristic (\"if layer==0: use 8-bit, else: use 4-bit\") outperforms the proposed MCKP solver. The paper must include this baseline and explain why the full optimization machinery is needed if a trivial heuristic suffices.\n\n### Minor\n\n- **(m1) Related work is critically thin.** Only 6 citations. Missing: GEAR (group-wise KV cache quantization with error correction), DuoAttention (retrieval vs. streaming head identification -- the same heterogeneity observation at different granularity), H2O/StreamingLLM/ScissorHands/SnapKV (KV cache eviction, mentioned in the task description but not in the paper), SqueezeLLM, QuIP/QuIP#, FlexGen, and the broader NAS/knapsack-in-ML literature. For a paper claiming novelty in applying MCKP to ML, the absence of prior MCKP-in-ML citations (NAS, filter pruning) is a notable omission.\n\n- **(m2) No quantization scheme specified.** The paper never states whether RTN, GPTQ, symmetric, or asymmetric quantization is used. Sensitivity profiles are scheme-dependent; results are not reproducible without this information.\n\n- **(m3) No error bars or significance testing.** All results are single-seed. Given that the profiler resolution is acknowledged to be noisy (84% of heads show delta=0 at standard resolution), variance quantification is essential.\n\n- **(m4) \"Principled\" language is overstated.** The abstract and introduction use \"principled regularization\" repeatedly, but the cardinality constraint is admittedly determined by empirical sweep. A principled approach would derive the constraint from a theoretical model of error propagation. The current method is a well-motivated heuristic, not principled regularization. The paper should use accurate language.\n\n- **(m5) Compounding effect observation may not be novel.** Non-additive error accumulation in quantized neural networks has been observed in the weight quantization literature (e.g., HAWQ's Hessian-based sensitivity analysis implicitly accounts for cross-layer interactions). RateQuant itself acknowledges compounding in Appendix M. The contribution is quantifying this for KV cache specifically, but the conceptual observation is not new.\n\n- **(m6) Cardinality constraint only limits count, not spatial distribution.** Two adjacent 2-bit heads in the residual stream likely compound far more than two distant ones. The paper treats all 2-bit assignments as equally harmful, which is a crude approximation. No analysis of spatial effects is provided.\n\n## Questions for Authors\n\n1. What happens when you add a cardinality constraint (max 2-bit heads <= k) to RateQuant's greedy allocator? If this closes the PPL gap with constrained MCKP, the MCKP formulation is not the contribution -- only the cardinality trick is. This is the single most important ablation missing from the paper.\n\n2. What is the PPL when you simply assign 8-bit to all Layer 0 heads and uniform 4-bit to everything else (the \"L0-only heuristic\")? The memory records suggest ~10.62. If this outperforms MCKP (11.23), please explain the added value of the optimization framework.\n\n3. Why does the paper report k=0 PPL as 12.01 when actual data shows 15.45? At budget=0.25 with {4,8,16} only, the solver cannot afford any 8-bit upgrades without 2-bit donors. Please reconcile this discrepancy.\n\n4. Which experiments in the paper are actually completed vs. projected? The multi-model results (Llama, Mistral), RateQuant comparison, and downstream evaluations appear to be imagined data.\n\n5. How sensitive is the optimal k to model architecture and compression ratio? If k must be re-tuned for each (model, compression) pair, the deployment overhead may negate the solver speed advantage.\n\n6. Does the spatial arrangement of 2-bit heads matter? If you constrain 2-bit assignments to be distributed across non-adjacent layers vs. concentrated in adjacent layers, does the compounding threshold change?\n\n## Detailed Novelty Assessment by Claim\n\n**Claim 1 (Head sensitivity heterogeneity):** Low novelty. That attention heads have heterogeneous quantization sensitivity is well-established. Layer 0 being critical has been observed in weight quantization (HAWQ), pruning, and attention analysis. The 100x magnitude is a useful quantification but not conceptually new. DuoAttention (2024) identifies \"retrieval heads\" vs. \"streaming heads\" -- the same heterogeneity at a different granularity.\n\n**Claim 2 (Constrained MCKP outperforms uniform):** Low novelty for the formulation; moderate for the result. Applying MCKP to discrete resource allocation is textbook. Any reasonable per-head allocation method should outperform uniform -- the question is whether MCKP specifically is needed, or whether simpler methods (L0 heuristic, RateQuant + constraint) achieve similar results. The missing ablations prevent assessing this.\n\n**Claim 3 (Cardinality constraint as compounding regularization):** Moderate novelty. This is the paper's genuine contribution. The compounding elbow curve is empirically interesting, and the connection between cardinality constraints and profiler error regularization is a clean insight. However: (a) the constraint is empirical, not derived from theory, (b) the observation that quantization errors compound is not new, and (c) the trick may transfer trivially to other allocation methods, making the MCKP formulation incidental.\n\n## Positioning Assessment\n\nThe paper is positioned as both a systems/practical contribution (fast solver, deployment-ready) and a scientific contribution (compounding effect discovery, principled regularization). The systems contribution is real but thin -- the solver is simple and solves a textbook problem. The scientific contribution (compounding + cardinality) is genuine but may reduce to a single trick applicable to any allocator, undermining the MCKP-specific framing.\n\nThe differentiation from RateQuant is articulated in paper_framing.md but not adequately demonstrated experimentally. The claimed advantage has two components (discrete optimization + compounding regularization), but no ablation separates them. If cardinality-constrained RateQuant-greedy matches MCKP, the entire paper reduces to \"add a max-2-bit count constraint to your allocator.\"\n\n## Significance Assessment\n\nFor practitioners: the compounding effect observation and the cardinality constraint recipe are actionable. A practitioner reading this paper would learn: \"don't assign more than ~7-10% of heads to 2-bit.\" This is a useful rule of thumb regardless of which solver is used.\n\nFor the research community: the contribution is incremental. The MCKP formulation, while clean, applies a known optimization technique to a natural problem formulation. The compounding observation, while valuable, is a single empirical finding. For a top venue with ~25% acceptance, I expect deeper theoretical grounding or more comprehensive experimental validation.\n\nThe paper would be a reasonable workshop contribution or a solid section within a more comprehensive KV cache optimization paper.\n\n## Score Justification\n\n**Score: 3/6 (Weak Reject)**\n\nThe core idea (compounding + cardinality regularization) has merit, but the paper has too many critical issues for acceptance: (1) fabricated/projected experimental data in the majority of tables, (2) a potentially fatal missing baseline (L0 heuristic), (3) a strawman comparison with the primary competitor (RateQuant), (4) missing ablations that would clarify whether the MCKP formulation itself contributes beyond the cardinality trick, and (5) thin related work. The novelty over RateQuant, once the comparison is made fair, may be marginal. I would upgrade to Weak Accept if: all experiments were completed with real data, the L0 heuristic baseline were included and addressed, the RateQuant comparison were made fair (including RateQuant + cardinality constraint), and the related work were expanded to 15+ citations.\n\n**Confidence: 4/5** -- I am familiar with the KV cache quantization and mixed-precision quantization literature. The data integrity issues are based on direct comparison of paper tables against actual experimental records. The one area of uncertainty is whether RateQuant's greedy algorithm would indeed match MCKP when given a cardinality constraint -- this ablation doesn't exist yet.",
  "project": "ratekv",
  "tier": "best",
  "dream_id": "dream_20260514T002109",
  "overall_score": "3/6 Weak Reject"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3beed012-888e-4eda-9755-e807f6794fbb",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1Z2ZLBKxUnJRxbgJBKG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df86dedb-24ea-4f74-bcda-a5dc44227efc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdHVfyYZZhwyDHj6sgJJqm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 82048,
      "output_tokens": 4066,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 816
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4066,
          "cache_read_input_tokens": 82048,
          "cache_creation_input_tokens": 816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 816,
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

_source line 45 · 2026-05-14T00:59:22.295Z_

<details><summary>↩ Tool result · `toolu_01CLHW5J4q2RVBoFEVBuDo6a`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/review_report.md\", \"dream_id\": \"dream_20260514T002109\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df86dedb-24ea-4f74-bcda-a5dc44227efc",
  "isSidechain": true,
  "promptId": "be83a19d-cbcf-4b56-b334-8905af18419e",
  "agentId": "a3242b380ec851971",
  "type": "user",
  "uuid": "06cda4d2-adfe-4985-9e89-e0101a13f84d",
  "sourceToolAssistantUUID": "df86dedb-24ea-4f74-bcda-a5dc44227efc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-14T00:59:41.131Z_

Review submitted. Here is the summary:

## R2 Review: Novelty and Related Work -- Score 3/6 (Weak Reject), Confidence 4/5

**Core assessment:** The paper's genuine contribution is the compounding effect observation and the cardinality constraint as a regularization mechanism (Claim 3). Claims 1 (head heterogeneity) and 2 (MCKP formulation) have low novelty -- the former is well-known, the latter is a textbook optimization applied to a natural problem.

**Five critical issues identified:**

1. **Incremental over RateQuant (M1):** The contribution reduces to two modifications over RateQuant: discrete MCKP (engineering) + cardinality constraint (a single empirical heuristic). The cardinality trick could likely be added to RateQuant's greedy algorithm with similar effect, but this ablation is missing.

2. **Strawman RateQuant comparison (M2):** Only the weakest RateQuant variant (continuous waterfilling + naive rounding) is compared. RateQuant's discrete greedy algorithm is not tested, and no ablation separates whether the improvement comes from MCKP vs. the cardinality constraint.

3. **Data integrity (M3):** The compounding sweep table contains fabricated numbers. Most critically, k=0 is reported as PPL 12.01 but actual data shows 15.45 (identical to uniform 4-bit, as expected). The headline PPL of 11.08 does not match any actual record (closest: 11.23).

4. **Imagined experiments (M4):** ~7 of 11 tables report projected rather than actual results (Llama, Mistral, RateQuant comparison, downstream tasks, cross-dataset, oracle, 72B).

5. **Missing L0-only baseline (M5):** Simply protecting Layer 0 at 8-bit + uniform 4-bit elsewhere may achieve PPL ~10.62, potentially outperforming the proposed MCKP solver (11.23). This trivial heuristic must be addressed.

**Path to upgrade (3 -> 4+):** Complete all experiments on hardware, include L0 heuristic baseline, add RateQuant + cardinality constraint ablation, expand related work to 15+ citations (GEAR, DuoAttention, H2O, SqueezeLLM, QuIP, FlexGen, NAS literature), and fix data discrepancies.

Report saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06cda4d2-adfe-4985-9e89-e0101a13f84d",
  "isSidechain": true,
  "agentId": "a3242b380ec851971",
  "requestId": "req_011Cb1ZAXnsyahNwRHagtjZC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a89de72-c5a2-4118-83d6-2ad08cf5068e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "6cf1809e-9145-4d61-9695-42edadd6799b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAPmC6gq6xAu7DcCt1ds8Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4193,
      "cache_read_input_tokens": 82864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4193,
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
