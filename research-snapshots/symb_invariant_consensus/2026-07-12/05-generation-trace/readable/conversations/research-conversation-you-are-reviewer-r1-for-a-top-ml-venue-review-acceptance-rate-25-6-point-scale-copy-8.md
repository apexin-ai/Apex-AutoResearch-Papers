# Research conversation: You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac26df3bc4b77c860.jsonl`
- **Structured JSON:** [`06f45d4d641748ec2fbb.json`](../../sessions/06/06f45d4d641748ec2fbb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

57 recorded events

### User

_source line 1 · 2026-05-16T06:19:37.821Z_

You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus areas are **methodology soundness** and **experimental rigor**.

## Paper Summary
"When Does Symbolic Consensus Help? Characterizing the Operating Regime of Constraint-Based LLM Aggregation"

The paper proposes SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic (FOL) constraints from LLM reasoning traces and resolves answer selection via weighted partial MAX-SAT. Rather than claiming universal improvement over Self-Consistency (SC), the paper asks "when does symbolic consensus help?" and introduces C0 (multi-candidate rate) as a zero-cost diagnostic.

Key results:
- Table 1: FOLIO (n=204): +4.4pp over SC (p=0.034); ProofWriter-D5 (n=600): +0.2pp (p=0.45); Combined macro: +2.3pp (p=0.082)
- Table 2: Tiebreak analysis on 42 tied questions: SICA 64.3% vs random 50%, McNemar p=0.19
- Table 3: K ablation (K=6,8,12,16,20) on 60 questions: SICA ≥ SC at all K, gap co-varies with tie frequency
- Table 4: Model scaling (7B/14B/72B instruction + QwQ-32B reasoning): C0 decreases with scale, gap decreases correspondingly
- Table 5: QwQ-32B: C0≈0 across domains, SICA≡SC
- Table 6: Overhead 12.7% marginal over SC
- Table 7: C0 vs gap: Spearman ρ=0.78 (p=0.001), R²=0.52, threshold C0=0.25

Method: For each trace, extract FOL constraints, deduplicate, weight by frequency, formulate per-candidate weighted partial MAX-SAT instances using Z3, select answer maximizing satisfied constraint weight. C0 defined as fraction of questions with ≥2 distinct answers across K samples.

## Experiment Design Reference (from review_context.yaml)
The full experiment plan includes 9 experiments:
1. sica_expanded_14b (exp-001): Main results on FOLIO 204 + PW-D5 600 — COVERED in paper
2. sica_k_ablation_14b (exp-002): K sensitivity on 60 questions — COVERED in paper
3. tiebreak_baseline_analysis (exp-003): 4 tiebreak strategies on ties — COVERED in paper
4. sica_7b_scaling (exp-004): 7B model on 60 questions — COVERED in paper (Table 4)
5. qwq_32b_operating_regime (exp-005): QwQ-32B data — COVERED in paper (Tables 4-5)
6. c0_diagnostic_validation (exp-006): C0 vs gap scatter across 14 configs — COVERED in paper (Table 7, though scatter plot figure not shown)
7. sica_72b_awq (exp-007): 72B-AWQ on 60 questions — COVERED in paper (Table 4)
8. constraint_quality_case_studies (exp-008): Qualitative analysis of 10 questions — COVERED in paper (Section 5.2)
9. overhead_analysis (exp-009): Wall-time decomposition — COVERED in paper (Table 6)

## Your Task
Write a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (methodology and experiments)
3. **Weaknesses** (methodology and experiments)
4. **Questions for Authors**
5. **Minor Issues**
6. **Score** (1-6) and **Confidence** (1-5)

Focus especially on:
- Is the MAX-SAT formulation well-motivated and correct?
- Is the constraint extraction pipeline well-described and reproducible?
- Are the experimental comparisons fair?
- Is the statistical methodology appropriate? Are the p-values and bootstrap procedures sound?
- Sample sizes and statistical power — are claims well-supported?
- Is the C0 diagnostic analysis convincing?
- Coverage of the experiment plan — are key experiments missing or underreported?
- Are there missing baselines or ablations?

Be rigorous but fair. Write in English.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "c8fdf179-381a-4733-b801-8655d8dcd5b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T06:19:37.827Z_

```json
{
  "parentUuid": "c8fdf179-381a-4733-b801-8655d8dcd5b6",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
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
  "uuid": "61e0399c-6a70-461e-827e-2f28726cdad8",
  "timestamp": "2026-05-16T06:19:37.827Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T06:19:41.316Z_



I'll start by reading the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61e0399c-6a70-461e-827e-2f28726cdad8",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mCpj5iqQQ2fsdNW9db",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "223bf024-2d06-4b37-8074-65421fc41add",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4YHm3goKxLfwDkNFNcgN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15176,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15176,
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

_source line 4 · 2026-05-16T06:19:41.807Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0152deRjirDvzPVhZQ5MBb1x`</summary>

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
  "parentUuid": "223bf024-2d06-4b37-8074-65421fc41add",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mCpj5iqQQ2fsdNW9db",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8450fa8e-e968-413f-8495-c489f9e64623",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4YHm3goKxLfwDkNFNcgN1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15176,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15176
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15176,
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

_source line 5 · 2026-05-16T06:19:41.815Z_

<details><summary>↩ Tool result · `toolu_0152deRjirDvzPVhZQ5MBb1x`</summary>

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
  "parentUuid": "8450fa8e-e968-413f-8495-c489f9e64623",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "dc9deb40-f7a9-435d-b6e8-02b1e3013d56",
  "sourceToolAssistantUUID": "8450fa8e-e968-413f-8495-c489f9e64623",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T06:19:45.176Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01SmPqJF9Gg4qeu1r3VsE7qx`</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc9deb40-f7a9-435d-b6e8-02b1e3013d56",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mD7xfnPYCz3D1rQ9gY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9ad1c24-7d80-410e-b8c5-a02a07d0cbb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LZhKzEKfpyiXwgikMmYyNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 7 · 2026-05-16T06:19:45.259Z_

<details><summary>↩ Tool result · `toolu_01SmPqJF9Gg4qeu1r3VsE7qx`</summary>

```text
{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (15 个)\n\n- **sica_expanded_14b**: RUNNING — \n- **sica_k_sensitivity_14b**: QUEUED — \n- **sica_d012_14b**: DONE (success) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_temp_diversity**: DONE (negative) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| sica_expanded_14b | — | — | — | — |\n\n## 待处理\n- sica_k_sensitivity_14b（排队等待 GPU）\n- smoke-test-5q（准备中）\n\n## 近期结论\n- **sica_d012_14b** (success): —\n  [D012 Full Evaluation Report - sica_d012_14b](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_d012_14b/report/d012_report_sica_d012_14b.md) | [D017 Tiebreak Baseline Analysis](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_d012_14b/report/tiebreak_analysis_report.md)\n- **sica_folio30** (killed): 逻辑域（FOLIO）上 SICA 能否利用 FOL 标注检测跨路径矛盾并超越 SC@K=12——FOLIO 有天然 FOL 标注，是 SICA 约束提取的理想场景 ← 基于 sica_aime30_v3\n  [FOLIO C0 Precheck Report](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_folio30/report/folio_c0_precheck_report.md)\n- **sica_d016_c0_precheck** (success): D016 模型 pivot C0 预检：Qwen2.5-14B-Instruct 在逻辑域是否产生足够 trace 多样性（多候选率 ≥20%） ← 基于 sica_proofwriter30_v2\n\n## 趋势\n成功 4 / 负向 1 / 失败 1 / 共 12\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-32608: 无 GPU 信息\n\n## 告警\n- mvp_math50_t07: 已被终止 — unknown\n- sica_aime30_t07: 已被终止 — unknown\n- sica_aime30_v2: 已被终止 — unknown\n- sica_aime30_v3: 已被终止 — unknown\n- sica_proofwriter30: 训练失败 — unknown\n- sica_folio30: 已被终止 — unknown\n- sica_proofwriter30_v2: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9ad1c24-7d80-410e-b8c5-a02a07d0cbb7",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "3e724f2c-af5d-4b51-a715-131f48574540",
  "sourceToolAssistantUUID": "b9ad1c24-7d80-410e-b8c5-a02a07d0cbb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T06:19:45.734Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0126PqCBZAGmcKogzu9EZhhX`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e724f2c-af5d-4b51-a715-131f48574540",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mD7xfnPYCz3D1rQ9gY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfc3a1a8-0480-4b6c-84a2-fb3851a0e742",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LZhKzEKfpyiXwgikMmYyNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 9 · 2026-05-16T06:19:45.756Z_

<details><summary>↩ Tool result · `toolu_0126PqCBZAGmcKogzu9EZhhX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| sica_expanded_14b | — | — | — | — |\\n\\n## 待处理\\n- sica_k_sensitivity_14b（排队等待 GPU）\\n- smoke-test-5q（准备中）\\n\\n## 近期结论\\n- **sica_d012_14b** (success): —\\n  [D012 Full Evaluation Report - sica_d012_14b](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_d012_14b/report/d012_report_sica_d012_14b.md) | [D017 Tiebreak Baseline Analysis](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_d012_14b/report/tiebreak_analysis_report.md)\\n- **sica_folio30** (killed): 逻辑域（FOLIO）上 SICA 能否利用 FOL 标注检测跨路径矛盾并超越 SC@K=12——FOLIO 有天然 FOL 标注，是 SICA 约束提取的理想场景 ← 基于 sica_aime30_v3\\n  [FOLIO C0 Precheck Report](/api/workspace-files/projects/symb_invariant_consensus/artifacts/sica_folio30/report/folio_c0_precheck_report.md)\\n- **sica_d016_c0_precheck** (success): D016 模型 pivot C0 预检：Qwen2.5-14B-Instruct 在逻辑域是否产生足够 trace 多样性（多候选率 ≥20%） ← 基于 sica_proofwriter30_v2\\n\\n## 趋势\\n成功 4 / 负向 1 / 失败 1 / 共 12\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-32608: 无 GPU 信息\\n\\n## 告警\\n- mvp_math50_t07: 已被终止 — unknown\\n- sica_aime30_t07: 已被终止 — unknown\\n- sica_aime30_v2: 已被终止 — unknown\\n- sica_aime30_v3: 已被终止 — unknown\\n- sica_proofwriter30: 训练失败 — unknown\\n- sica_folio30: 已被终止 — unknown\\n- sica_proofwriter30_v2: 已被终止 — unknown\\n\", \"total_chars\": 1362, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfc3a1a8-0480-4b6c-84a2-fb3851a0e742",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "193fce40-9f5c-4cad-ad9a-7d0a1d7cd6da",
  "sourceToolAssistantUUID": "bfc3a1a8-0480-4b6c-84a2-fb3851a0e742",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T06:19:49.204Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0137Db7nsNBUwffvBRRVBPWo`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "193fce40-9f5c-4cad-ad9a-7d0a1d7cd6da",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mDS9YmtXeCr7Q9kDhe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2942b042-b2cf-49e9-8267-674fcd9ded40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VU2SR66bBYStxtorJ31A7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2260,
      "cache_read_input_tokens": 16624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2260,
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

_source line 11 · 2026-05-16T06:19:49.233Z_

<details><summary>↩ Tool result · `toolu_0137Db7nsNBUwffvBRRVBPWo`</summary>

```text
artifacts/dream_reports/dream_20260516T051642/best/paper.tex
artifacts/dream_reports/dream_20260516T051642/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/best/paper.tex
artifacts/dream_reports/dream_20260516T054054/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2942b042-b2cf-49e9-8267-674fcd9ded40",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "a51e355a-11fb-4c56-babe-30515d2eaf05",
  "sourceToolAssistantUUID": "2942b042-b2cf-49e9-8267-674fcd9ded40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T06:19:49.557Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013qTEPvVx1TFS4HeMgmXV8d`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a51e355a-11fb-4c56-babe-30515d2eaf05",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mDS9YmtXeCr7Q9kDhe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "006c10f2-e34f-4b18-b644-c3ef3cee2c58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VU2SR66bBYStxtorJ31A7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2260,
      "cache_read_input_tokens": 16624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2260,
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

_source line 13 · 2026-05-16T06:19:49.582Z_

<details><summary>↩ Tool result · `toolu_013qTEPvVx1TFS4HeMgmXV8d`</summary>

```text
artifacts/dream_reports/dream_20260516T051642/best/paper.pdf
artifacts/dream_reports/dream_20260516T051642/median/paper.pdf
artifacts/dream_reports/dream_20260516T054054/best/paper.pdf
artifacts/dream_reports/dream_20260516T054054/median/paper.pdf
artifacts/dream_reports/dream_20260516T054054/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "006c10f2-e34f-4b18-b644-c3ef3cee2c58",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "44e626d4-2f62-4f30-8f83-64275491ef37",
  "sourceToolAssistantUUID": "006c10f2-e34f-4b18-b644-c3ef3cee2c58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T06:19:50.496Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011NVVbBRx2Uj65VGM9Z7YxJ`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44e626d4-2f62-4f30-8f83-64275491ef37",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mDS9YmtXeCr7Q9kDhe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "225c5899-c500-4463-acb2-82ceef79280a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VU2SR66bBYStxtorJ31A7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2260,
      "cache_read_input_tokens": 16624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2260,
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

_source line 15 · 2026-05-16T06:19:50.515Z_

<details><summary>↩ Tool result · `toolu_011NVVbBRx2Uj65VGM9Z7YxJ`</summary>

```text
literature_map.yaml
artifacts/dream_reports/dream_20260516T051642/best/imagined_experiments.yaml
artifacts/manifest.yaml
artifacts/dream_reports/dream_20260516T051642/median/imagined_experiments.yaml
registry.yaml
artifacts/dream_reports/dream_20260516T051642/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T054054/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T054054/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T054054/worst/imagined_experiments.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260516T054054/best/review_context.yaml
decisions.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260516T054054/median/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "225c5899-c500-4463-acb2-82ceef79280a",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "02819dd0-9071-48ec-9b21-e2bb726d5eb4",
  "sourceToolAssistantUUID": "225c5899-c500-4463-acb2-82ceef79280a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T06:19:50.783Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UTqvxa1Fa6t5VAuPozaWQh`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02819dd0-9071-48ec-9b21-e2bb726d5eb4",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mDS9YmtXeCr7Q9kDhe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b2c12db-242b-488a-a2b5-4390df3da855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VU2SR66bBYStxtorJ31A7T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2260,
      "cache_read_input_tokens": 16624,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2260
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 345,
          "cache_read_input_tokens": 16624,
          "cache_creation_input_tokens": 2260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2260,
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

_source line 17 · 2026-05-16T06:19:50.804Z_

<details><summary>↩ Tool result · `toolu_01UTqvxa1Fa6t5VAuPozaWQh`</summary>

```text
artifacts/constraint_extractor.py
artifacts/trace_generator.py
artifacts/pipeline.py
artifacts/run_mvp.py
artifacts/prepare_proofwriter.py
artifacts/run_full_mvp.py
artifacts/constraint_extractor_fixed.py
artifacts/z3_maxsat_patched.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b2c12db-242b-488a-a2b5-4390df3da855",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "f83b05da-95f6-4069-8893-367c9222acc5",
  "sourceToolAssistantUUID": "0b2c12db-242b-488a-a2b5-4390df3da855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-16T06:19:53.441Z_

Let me read the paper and the review context files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f83b05da-95f6-4069-8893-367c9222acc5",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mDnHWtnXRb1i6cEqU5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21e90acf-7aec-40ac-8040-14a6715c1989",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCaD68Dydukst2XAA8yn7N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 959,
      "cache_read_input_tokens": 18884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 959,
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

_source line 19 · 2026-05-16T06:19:53.683Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HpqAQxbFCVJz7pRCv3zNy7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21e90acf-7aec-40ac-8040-14a6715c1989",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mDnHWtnXRb1i6cEqU5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a78e2c4-47d5-4a9f-8793-67e61cd1d476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCaD68Dydukst2XAA8yn7N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 959,
      "cache_read_input_tokens": 18884,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 959
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 18884,
          "cache_creation_input_tokens": 959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 959,
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

_source line 20 · 2026-05-16T06:19:53.690Z_

<details><summary>↩ Tool result · `toolu_01HpqAQxbFCVJz7pRCv3zNy7`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{url}
12	\usepackage{natbib}
13	\usepackage{enumitem}
14	
15	\title{Principled Symbolic Consensus Improves LLM Reasoning}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\begin{abstract}
23	Self-Consistency (SC) aggregates multiple LLM reasoning traces via majority voting but discards the logical structure within each trace.
24	When votes are tied, SC falls back to arbitrary heuristics (alphabetical ordering, random selection) with no principled resolution mechanism.
25	We introduce \textbf{SICA} (Symbolic Invariant Consensus Aggregation), which extracts first-order logic constraints from reasoning traces and resolves ties through weighted partial MAX-SAT solving.
26	On 804 questions spanning FOLIO and ProofWriter benchmarks, SICA achieves 71.3\% accuracy versus SC's 67.5\% (+3.8pp, $p=0.023$) with Qwen2.5-14B-Instruct.
27	SICA wins 75.9\% of tie cases, compared to 50\% expected from random tiebreaking.
28	However, we show that SICA's effectiveness is \emph{conditional on trace diversity}: with QwQ-32B, a reasoning model whose outputs are near-deterministic (multi-candidate rate $C_0=3.6\%$), SICA degenerates to SC.
29	We formalize this as the \textbf{operating regime} of symbolic consensus and demonstrate that $C_0$---a zero-cost diagnostic computable before running SICA---predicts the SICA--SC gap with Pearson $r=0.94$ across four model scales.
30	Our results establish when symbolic consensus adds value and when it does not, providing practitioners with a principled deployment criterion.
31	\end{abstract}
32	
33	%-------------------------------------------------------------
34	\section{Introduction}
35	\label{sec:intro}
36	
37	Large language models (LLMs) have demonstrated remarkable reasoning capabilities across diverse tasks, yet their outputs remain stochastic---sampling the same model multiple times on the same question yields different reasoning traces and sometimes different answers.
38	Self-Consistency (Wang et al., 2023) exploits this stochasticity by sampling $K$ traces and selecting the answer with the most votes (majority voting).
39	While effective, SC treats each reasoning trace as an opaque vote, discarding the rich logical structure contained within the chain-of-thought.
40	
41	A fundamental limitation of majority voting emerges when votes are tied.
42	With even $K$ and questions that elicit diverse answers, ties occur in 8--15\% of cases.
43	SC resolves these ties through arbitrary heuristics---alphabetical ordering, random selection, or first-seen preference---none of which leverage the reasoning content.
44	
45	We propose \textbf{SICA} (Symbolic Invariant Consensus Aggregation), a method that extracts first-order logic (FOL) constraints from reasoning traces and uses weighted partial MAX-SAT to find the answer most consistent with the extracted symbolic structure.
46	SICA operates as a drop-in replacement for SC's aggregation step: it uses the same $K$ sampled traces, adds a constraint extraction phase, and resolves both ties and close votes through principled symbolic optimization.
47	
48	Our investigation reveals that SICA's effectiveness is not universal but is governed by a model property we call \textbf{trace diversity}, quantified by the multi-candidate rate $C_0$ (the fraction of questions where sampled traces produce more than one distinct answer).
49	Instruction-tuned models exhibit high trace diversity ($C_0 = 30\text{--}68\%$) and benefit substantially from SICA.
50	Reasoning models like QwQ-32B produce near-deterministic outputs ($C_0 = 3.6\%$), causing SICA to mathematically degenerate to SC.
51	This distinction is a \emph{model property}, not a task property: the same FOLIO questions yield $C_0 = 42\%$ with Qwen2.5-14B-Instruct but $C_0 \approx 0\%$ with QwQ-32B.
52	
53	Our contributions are:
54	\begin{enumerate}
55	    \item \textbf{Principled Tiebreaking.} SICA achieves +3.8pp over SC on 804 questions ($p = 0.023$), with 75.9\% win rate on tied questions. The gain holds across both FOLIO (+5.9pp) and ProofWriter (+1.8pp).
56	    \item \textbf{Operating Regime Characterization.} We show that symbolic consensus effectiveness is conditional on trace diversity and provide the first formal characterization of when it helps versus degenerates.
57	    \item \textbf{$C_0$ as Practical Diagnostic.} Multi-candidate rate $C_0$ predicts the SICA--SC gap with $r = 0.94$ ($R^2 = 0.88$) across four model scales, enabling zero-cost deployment decisions.
58	\end{enumerate}
59	
60	
61	%-------------------------------------------------------------
62	\section{Related Work}
63	\label{sec:related}
64	
65	\paragraph{Self-Consistency and Voting Methods.}
66	Wang et al.\ (2023) introduced Self-Consistency (SC), which samples diverse reasoning paths and marginalizes over them via majority voting.
67	Universal Self-Consistency (Chen et al., 2023) extends SC to free-form tasks but remains voting-based.
68	Neither method exploits the logical structure within reasoning traces for consensus.
69	
70	\paragraph{Symbolic Reasoning with LLMs.}
71	Recent work has explored translating natural language reasoning into formal logic for verification.
72	Pan et al.\ (2023) use LLM-generated FOL for logical reasoning tasks.
73	Ye et al.\ (2023) combine symbolic solvers with neural reasoning.
74	Our work differs in using symbolic extraction not for answer generation but for \emph{consensus aggregation} among multiple reasoning traces.
75	
76	\paragraph{Ensemble and Aggregation Methods.}
77	Beyond simple voting, weighted ensembles and learned verifiers have been proposed for aggregating LLM outputs.
78	Our approach is distinguished by deriving weights from the logical consistency of extracted constraints, requiring no additional training data or learned components.
79	
80	
81	%-------------------------------------------------------------
82	\section{Method}
83	\label{sec:method}
84	
85	\subsection{Problem Setup}
86	
87	Given a reasoning question $q$, we sample $K$ reasoning traces $\{t_1, \ldots, t_K\}$ from an LLM at temperature $T$.
88	Each trace $t_i$ produces an answer $a_i \in \mathcal{A}$.
89	SC selects $\hat{a}_{\text{SC}} = \arg\max_{a \in \mathcal{A}} |\{i : a_i = a\}|$.
90	When multiple answers achieve the maximum vote count (a \emph{tie}), SC falls back to an arbitrary tiebreaking rule.
91	
92	\subsection{Constraint Extraction}
93	
94	For each trace $t_i$, SICA prompts the same LLM to extract a set of first-order logic constraints $\mathcal{C}_i = \{c_{i,1}, \ldots, c_{i,m_i}\}$.
95	Each constraint $c_{i,j}$ is a FOL formula expressing a logical relationship stated or derived in the reasoning trace.
96	On average, we extract 13.2 constraints per trace, yielding approximately 28.7 unique constraints per question after deduplication.
97	The extraction failure rate is 2\%, and malformed constraints are discarded.
98	
99	\subsection{Weighted Partial MAX-SAT Aggregation}
100	
101	We formulate answer selection as a weighted partial MAX-SAT problem.
102	For each candidate answer $a \in \mathcal{A}$, let $\mathcal{C}^{(a)} = \bigcup_{i: a_i = a} \mathcal{C}_i$ be the constraints extracted from traces supporting $a$.
103	We assign each constraint a weight proportional to the consistency of the trace from which it was extracted:
104	\begin{equation}
105	    w(c_{i,j}) = \frac{|\{c \in \mathcal{C}_i : c \text{ is satisfiable with } c_{i,j}\}|}{|\mathcal{C}_i|}
106	\end{equation}
107	The SICA answer is:
108	\begin{equation}
109	    \hat{a}_{\text{SICA}} = \arg\max_{a \in \mathcal{A}} \sum_{c \in \mathcal{C}^{(a)}} w(c)
110	\end{equation}
111	When no tie exists in majority voting and SICA agrees with SC, the result is identical.
112	SICA's effect is concentrated on tied and near-tied questions where constraint quality can distinguish between competing answers.
113	We use Z3 as the MAX-SAT solver; solving takes 47ms on average per question.
114	
115	\subsection{Multi-Candidate Rate ($C_0$)}
116	
117	We define the multi-candidate rate $C_0$ as:
118	\begin{equation}
119	    C_0 = \frac{|\{q : |\{a_i : i = 1, \ldots, K\}| > 1\}|}{|Q|}
120	\end{equation}
121	where $Q$ is the question set.
122	$C_0$ measures the fraction of questions where sampled traces produce more than one distinct answer---a necessary condition for SICA to differ from SC.
123	Critically, $C_0$ is computable from the SC pipeline alone, requiring no additional inference.
124	
125	
126	%-------------------------------------------------------------
127	\section{Experimental Setup}
128	\label{sec:setup}
129	
130	\paragraph{Benchmarks.}
131	We evaluate on two logic reasoning benchmarks:
132	\textbf{FOLIO} (204 questions), which requires first-order logic reasoning over natural language premises, and
133	\textbf{ProofWriter} depth-5 (600 questions), which requires multi-step deductive reasoning over rule bases.
134	Combined, our evaluation spans 804 questions.
135	
136	\paragraph{Models.}
137	We evaluate four models spanning different scales and architectures:
138	\textbf{Qwen2.5-7B-Instruct} (7B, instruction),
139	\textbf{Qwen2.5-14B-Instruct} (14B, instruction),
140	\textbf{Qwen2.5-72B-Instruct-AWQ} (72B, instruction, 4-bit quantized), and
141	\textbf{QwQ-32B} (32B, reasoning).
142	
143	\paragraph{Configuration.}
144	Unless otherwise noted, we use $K=12$ traces at temperature $T=0.7$.
145	For K ablation studies, we vary $K \in \{6, 8, 12, 16, 20\}$.
146	All experiments use the same constraint extraction prompt.
147	Statistical significance is assessed via bootstrap resampling (10,000 iterations).
148	
149	
150	%-------------------------------------------------------------
151	\section{Results}
152	\label{sec:results}
153	
154	\subsection{Main Results: SICA vs.\ SC}
155	\label{sec:main_results}
156	
157	Table~\ref{tab:main} presents the full-scale evaluation on 804 questions with Qwen2.5-14B-Instruct.
158	SICA achieves 71.3\% accuracy versus SC's 67.5\%, a gain of +3.8 percentage points ($p = 0.023$).
159	The improvement is consistent across both benchmarks: +5.9pp on FOLIO ($p = 0.018$) and +1.8pp on ProofWriter ($p = 0.11$).
160	The combined result crosses the $p < 0.05$ significance threshold, supporting the claim that SICA provides a statistically significant improvement over SC.
161	
162	The ProofWriter gain, while not individually significant at $\alpha = 0.05$, is nonzero (+1.8pp), eliminating the concern that SICA only works on a single domain.
163	
164	\begin{table}[t]
165	\centering
166	\small
167	\begin{tabular}{lccccc}
168	\toprule
169	\textbf{Dataset} & \textbf{N} & \textbf{SC} & \textbf{SICA} & \textbf{Gap} & \textbf{$p$} \\
170	\midrule
171	FOLIO        & 204 & 73.5 & 79.4 & +5.9 & 0.018 \\
172	ProofWriter  & 600 & 66.8 & 68.6 & +1.8 & 0.11  \\
173	\midrule
174	Combined     & 804 & 67.5 & 71.3 & +3.8 & 0.023 \\
175	\bottomrule
176	\end{tabular}
177	\caption{Main results: SICA vs.\ SC accuracy (\%) on 804 questions with Qwen2.5-14B-Instruct ($K\!=\!12$, $T\!=\!0.7$). Gap in percentage points. $p$-values from bootstrap resampling.}
178	\label{tab:main}
179	\end{table}
180	
181	
182	\subsection{Tiebreak Analysis}
183	\label{sec:tiebreak}
184	
185	Table~\ref{tab:tiebreak} analyzes SICA's behavior on tied questions specifically.
186	Of 804 questions, 87 (10.8\%) result in ties under $K = 12$.
187	On these tied questions, SICA selects the correct answer 75.9\% of the time, compared to 50\% expected from random tiebreaking and 60\% from alphabetical ordering.
188	
189	The tie frequency of 10.8\% is consistent with the binomial prediction: for questions with two candidate answers (fraction $\approx C_0 = 0.47$), the probability of a 6:6 tie with $K = 12$ is $\binom{12}{6}/2^{12} \approx 0.225$, giving expected tie rate $\approx 0.225 \times 0.47 \approx 10.6\%$.
190	
191	\begin{table}[t]
192	\centering
193	\small
194	\begin{tabular}{lccc}
195	\toprule
196	\textbf{Metric} & \textbf{FOLIO} & \textbf{PW} & \textbf{Combined} \\
197	\midrule
198	Tie questions     & 27/204   & 60/600   & 87/804   \\
199	                  & (13.2\%) & (10.0\%) & (10.8\%) \\
200	SICA wins         & 21/27    & 45/60    & 66/87    \\
201	                  & (77.8\%) & (75.0\%) & (75.9\%) \\
202	SC wins           & 6/27     & 15/60    & 21/87    \\
203	                  & (22.2\%) & (25.0\%) & (24.1\%) \\
204	\bottomrule
205	\end{tabular}
206	\caption{Tiebreak analysis under $K = 12$. ``SICA wins'' means SICA selects the correct answer on a tied question where SC's arbitrary tiebreak would not.}
207	\label{tab:tiebreak}
208	\end{table}
209	
210	
211	\subsection{Tiebreak Strategy Comparison}
212	\label{sec:tiebreak_baselines}
213	
214	A natural concern is whether SICA's gain merely reflects a poor default tiebreaker in SC.
215	Table~\ref{tab:tiebreak_baseline} compares SICA against three alternative tiebreaking strategies on the full 804 questions.
216	SICA outperforms all baselines, including SC-random (+3.2pp), which is the fairest comparison since it introduces no systematic bias on ties.
217	The first-seen heuristic performs worst (67.0\%), as the initial trace tends to follow a greedy-like pattern that is more error-prone on difficult questions.
218	
219	\begin{table}[t]
220	\centering
221	\small
222	\begin{tabular}{lcc}
223	\toprule
224	\textbf{Method} & \textbf{Acc (\%)} & \textbf{Tiebreak Mechanism} \\
225	\midrule
226	SICA             & 71.3 & MaxSAT weighted constraints \\
227	SC-random        & 68.1 & Uniform random on ties \\
228	SC-alphabetical  & 67.5 & Alphabetical first on ties \\
229	SC-first-seen    & 67.0 & First generated answer \\
230	\bottomrule
231	\end{tabular}
232	\caption{Comparison of tiebreak strategies on 804 questions (Qwen2.5-14B-Instruct, $K=12$). SICA outperforms all heuristic tiebreakers.}
233	\label{tab:tiebreak_baseline}
234	\end{table}
235	
236	
237	\subsection{$K$ Ablation}
238	\label{sec:k_ablation}
239	
240	Table~\ref{tab:k_ablation} reports the effect of varying $K$ on 60 questions from the pilot set with Qwen2.5-14B-Instruct.
241	The SICA--SC gap increases monotonically from 1.7pp ($K = 6$) to 5.0pp ($K = 16$), then plateaus at $K = 20$.
242	This pattern reflects two competing effects as $K$ grows: (1) more traces provide more constraints for MAX-SAT, improving tiebreak quality; (2) SC's majority vote stabilizes (law of large numbers), raising the SC baseline.
243	The peak gap at $K = 16$ represents the sweet spot.
244	$K = 12$ offers the best cost-performance tradeoff at 75\% of the compute cost of $K = 16$ with a 3.3pp gap.
245	
246	\begin{table}[t]
247	\centering
248	\small
249	\begin{tabular}{ccccccc}
250	\toprule
251	$K$ & \textbf{SC} & \textbf{SICA} & \textbf{Gap} & \textbf{Tie\%} & $C_0$ \\
252	\midrule
253	6  & 70.0 & 71.7 & +1.7 & 6.7  & 0.483 \\
254	8  & 70.0 & 73.3 & +3.3 & 8.3  & 0.517 \\
255	12 & 70.0 & 73.3 & +3.3 & 11.7 & 0.533 \\
256	16 & 70.0 & 75.0 & +5.0 & 13.3 & 0.550 \\
257	20 & 71.7 & 76.7 & +5.0 & 11.7 & 0.567 \\
258	\bottomrule
259	\end{tabular}
260	\caption{$K$ ablation on 60 pilot questions (Qwen2.5-14B-Instruct). Accuracy in \%, gap in pp. Tie\% is the fraction of questions with tied votes.}
261	\label{tab:k_ablation}
262	\end{table}
263	
264	
265	\subsection{Model Scaling and Operating Regime}
266	\label{sec:scaling}
267	
268	Table~\ref{tab:scaling} presents results across four models spanning 7B to 72B parameters plus a reasoning model.
269	A clear pattern emerges: as model capability increases within the instruction-tuned family, $C_0$ decreases and the SICA--SC gap shrinks.
270	Critically, the transition from instruction to reasoning architecture (QwQ-32B) causes $C_0$ to collapse to 3.6\% and the gap to vanish entirely.
271	
272	\begin{table}[t]
273	\centering
274	\small
275	\begin{tabular}{llccccc}
276	\toprule
277	\textbf{Model} & \textbf{Type} & \textbf{SC} & \textbf{SICA} & \textbf{Gap} & $C_0$ \\
278	\midrule
279	7B-Instruct   & Instr. & 56.7 & 63.3 & +6.7 & 0.683 \\
280	14B-Instruct  & Instr. & 70.0 & 73.3 & +3.3 & 0.533 \\
281	72B-AWQ       & Instr. & 78.3 & 80.0 & +1.7 & 0.300 \\
282	QwQ-32B       & Reas.  & ---  & ---  & 0.0  & 0.036 \\
283	\bottomrule
284	\end{tabular}
285	\caption{Model scaling results on 60 pilot questions ($K\!=\!12$). Accuracy in \%. QwQ-32B produces identical SC and SICA outputs due to near-zero trace diversity.}
286	\label{tab:scaling}
287	\end{table}
288	
289	The QwQ-32B result is not a failure of SICA but an expected consequence of its operating regime.
290	Reasoning models perform internal multi-path search and self-verification during generation, compressing the output distribution.
291	Trace entropy quantifies this: QwQ-32B has 0.12 bits versus 1.83 bits for 14B-Instruct---a 15$\times$ difference.
292	When all $K$ traces converge to the same answer, MAX-SAT optimization is vacuous regardless of constraint quality.
293	
294	\subsection{$C_0$ as a Predictor of SICA Effectiveness}
295	\label{sec:c0}
296	
297	Figure~\ref{fig:c0} and Table~\ref{tab:c0_regression} present the relationship between $C_0$ and the SICA--SC gap across all models and $K$ values.
298	Across 8 data points spanning $C_0$ from 3.6\% (QwQ-32B) to 68.3\% (7B-Instruct), we observe a strong linear relationship: Pearson $r = 0.94$, Spearman $\rho = 0.93$, $R^2 = 0.88$.
299	
300	The fitted relationship is:
301	\begin{equation}
302	    \text{Gap (pp)} = 10.2 \times C_0 - 2.1
303	\end{equation}
304	This implies a threshold of $C_0 \approx 0.21$ for SICA to yield positive gains over SC.
305	The causal direction is clear: $C_0$ is an input to SICA (computed from the SC pipeline), not an outcome.
306	The $K$ ablation data (5 points from the same model at different $K$) controls for model capability as a confound, confirming that the $C_0$--gap relationship holds even within a single model.
307	
308	\begin{table}[t]
309	\centering
310	\small
311	\begin{tabular}{lc}
312	\toprule
313	\textbf{Metric} & \textbf{Value} \\
314	\midrule
315	Pearson $r$     & 0.94 \\
316	Spearman $\rho$ & 0.93 \\
317	Slope           & 10.2 pp per unit $C_0$ \\
318	Intercept       & $-2.1$ pp \\
319	$R^2$           & 0.88 \\
320	$C_0$ threshold & 0.21 \\
321	\bottomrule
322	\end{tabular}
323	\caption{Linear regression of SICA--SC gap on $C_0$ across 8 data points (4 models $\times$ varying $K$).}
324	\label{tab:c0_regression}
325	\end{table}
326	
327	
328	\subsection{Qualitative Analysis: Constraint Quality}
329	\label{sec:qualitative}
330	
331	To understand \emph{why} SICA's tiebreaking works, we analyze 8 representative questions spanning both benchmarks.
332	
333	\paragraph{SICA win (FOLIO).}
334	On a question about organizational membership and property inheritance, the 12 traces split 6:6.
335	The 6 True-supporting traces extract mutually consistent constraints (92\% cross-satisfaction rate), including the key axiom $\forall x(\text{Member}(x, \text{Org}) \to \text{HasProperty}(x, P))$ with weight 0.83.
336	The 6 False-supporting traces produce self-contradictory constraints (61\% satisfaction rate).
337	MAX-SAT correctly selects True.
338	
339	\paragraph{SICA failure (ProofWriter).}
340	On a depth-5 chain reasoning question, 7 of 12 traces contain the same FOL translation error (a negation omission in an intermediate step), causing the extracted constraints to point toward the wrong answer.
341	This illustrates SICA's primary failure mode: systematic extraction errors amplified by MAX-SAT.
342	
343	Of 8 analyzed cases, 5 show correct and helpful constraints, 1 shows correct but redundant constraints, 1 shows an incorrect constraint correctly excluded by the consistency filter, and 1 shows a harmful systematic error.
344	The overall constraint extraction failure rate is 2\%, with a MAX-SAT exclusion rate of 3.1\% for inconsistent constraints.
345	
346	
347	\subsection{Overhead Analysis}
348	\label{sec:overhead}
349	
350	Table~\ref{tab:overhead} breaks down the wall-time cost per question.
351	SICA adds 39\% overhead compared to SC, with constraint extraction (25.4\% of total time) as the dominant additional cost and MAX-SAT solving contributing negligibly (2.4\%, average 47ms per question).
352	
353	The overhead is dominated by LLM inference for constraint extraction, meaning it decreases proportionally with inference speedups.
354	Compared to the alternative of doubling $K$ to $2K$ traces for SC (100\% overhead, typically $<$2pp gain), SICA's 39\% overhead for 3.8pp gain offers superior cost-effectiveness.
355	
356	\begin{table}[t]
357	\centering
358	\small
359	\begin{tabular}{lccc}
360	\toprule
361	\textbf{Stage} & \textbf{Time (s)} & \textbf{Frac.} & \textbf{Parallel?} \\
362	\midrule
363	Trace generation     & 42.1 & 72.2\% & Yes (batched) \\
364	Constraint extract.  & 14.8 & 25.4\% & Yes (per-trace) \\
365	MAX-SAT solving      & 1.4  & 2.4\%  & No \\
366	\midrule
367	Total (SICA)         & 58.3 & 100\%  & --- \\
368	Total (SC only)      & 42.1 & ---    & --- \\
369	SICA overhead        & 16.2 & +38.5\% & --- \\
370	\bottomrule
371	\end{tabular}
372	\caption{Wall-time breakdown per question (Qwen2.5-14B-Instruct, $K\!=\!12$, averaged over 804 questions).}
373	\label{tab:overhead}
374	\end{table}
375	
376	
377	%-------------------------------------------------------------
378	\section{Discussion}
379	\label{sec:discussion}
380	
381	\paragraph{Operating Regime as a Design Principle.}
382	Our results suggest a practical heuristic: compute $C_0$ from a small pilot set before deploying SICA.
383	If $C_0 > 0.21$, SICA is expected to yield positive gains; if $C_0 < 0.05$, the model's output distribution is too concentrated for symbolic consensus to add value.
384	This transforms SICA from a universal method into a \emph{conditional} method with formally characterizable applicability boundaries.
385	
386	\paragraph{Why Not Just Use a Reasoning Model?}
387	QwQ-32B's near-zero $C_0$ might suggest that reasoning models render SICA unnecessary.
388	However, instruction models remain dominant in deployment due to lower cost, lower latency, and broader availability.
389	SICA provides a way to improve instruction model reasoning without switching architectures.
390	
391	\paragraph{Limitations.}
392	Our evaluation is limited to logic reasoning benchmarks (FOLIO, ProofWriter) where FOL extraction is natural.
393	Extending SICA to mathematical reasoning or commonsense tasks requires domain-appropriate constraint languages.
394	The $C_0$--gap relationship is established on 8 data points from a single model family (Qwen2.5); validation on other architectures (Llama, Mistral) is needed.
395	The constraint extraction step depends on the same LLM's ability to produce valid FOL, creating a potential failure mode when model FOL competence is low.
396	
397	
398	%-------------------------------------------------------------
399	\section{Conclusion}
400	\label{sec:conclusion}
401	
402	We presented SICA, a symbolic consensus method that resolves Self-Consistency voting ties through weighted MAX-SAT over extracted logical constraints.
403	SICA achieves +3.8pp over SC on 804 logic reasoning questions ($p = 0.023$) with 75.9\% tiebreak win rate.
404	We identified the operating regime of symbolic consensus: SICA adds value when trace diversity is high ($C_0 > 21\%$, instruction models) and degenerates to SC when it is low ($C_0 < 5\%$, reasoning models).
405	The multi-candidate rate $C_0$ serves as a zero-cost diagnostic ($r = 0.94$) for practitioners to determine whether SICA deployment is worthwhile.
406	Our work contributes not just a method but a framework for understanding \emph{when} symbolic consensus is and is not effective.
407	
408	\bibliographystyle{plainnat}
409	
410	
411	\end{document}
412	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a78e2c4-47d5-4a9f-8793-67e61cd1d476",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "eb516a13-8ad6-4be5-b15c-f5e6c10dafc0",
  "sourceToolAssistantUUID": "2a78e2c4-47d5-4a9f-8793-67e61cd1d476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-16T06:19:56.701Z_

Now let me read the review context and imagined experiments files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb516a13-8ad6-4be5-b15c-f5e6c10dafc0",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mDzeA87VCK4V1SWSgm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60c895b8-f6c1-4bae-952a-ac6d549645a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwHqKxNvwxjE4fiU9c1M78",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8279,
      "cache_read_input_tokens": 19843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8279,
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

_source line 22 · 2026-05-16T06:19:59.102Z_

<details open><summary>🔧 Tool call — Read · `toolu_013bwrq38VSabDLUmor5pf5Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60c895b8-f6c1-4bae-952a-ac6d549645a8",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mDzeA87VCK4V1SWSgm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63733342-b757-49de-88bc-a0fab11487e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwHqKxNvwxjE4fiU9c1M78",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8279,
      "cache_read_input_tokens": 19843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8279,
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

_source line 23 · 2026-05-16T06:19:59.113Z_

<details><summary>↩ Tool result · `toolu_013bwrq38VSabDLUmor5pf5Q`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 framing 完全成立。标题可用 "Principled Symbolic Consensus Improves
3	  LLM Reasoning"。 三条 claim 原样保留：C1 用扩展实验的显著 p 值支撑，C2 用 QwQ 负结果 + 多模型 C0 梯度支撑， C3 用
4	  C0-gap 散点图支撑。ProofWriter 非零增益消除 "domain-specific" 攻击面。 Operating regime 作为理论贡献锦上添花，而非防御性
5	  reframe。EMNLP main 强投。
6	
7	  '
8	imagined_experiments:
9	- name: sica_expanded_14b
10	  plan_id: exp-001
11	  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,
12	    T=0.7'
13	  expected_results:
14	    sica_accuracy_combined: 0.713
15	    sc_accuracy_combined: 0.675
16	    sica_sc_gap_combined_pp: 3.8
17	    folio_sica_accuracy: 0.794
18	    folio_sc_accuracy: 0.735
19	    folio_gap_pp: 5.9
20	    proofwriter_sica_accuracy: 0.686
21	    proofwriter_sc_accuracy: 0.668
22	    proofwriter_gap_pp: 1.8
23	    bootstrap_p_combined: 0.023
24	    bootstrap_p_folio: 0.018
25	    bootstrap_p_proofwriter: 0.11
26	    c0_combined: 0.47
27	    c0_folio: 0.42
28	    c0_proofwriter: 0.5
29	    tie_question_fraction_combined: 0.11
30	    tie_question_fraction_folio: 0.13
31	    tie_question_fraction_proofwriter: 0.1
32	    tiebreak_win_rate: 0.76
33	    total_constraints_raw: ~78000
34	    total_constraints_unique: ~23000
35	    maxsat_exclusion_rate: 0.031
36	    wall_time_hours: ~13
37	  result_rationale: 'D012 的 60 题结果中，14B 的 C0=53.3%，说明约半数题存在多候选答案，SICA 有操作空间。 扩展到 804
38	    题后，FOLIO 从 30→204 题——该数据集本身推理链多样性高（FOL 翻译歧义多）， C0 预期维持 ~42%，gap 从 6.7pp 略回归均值至
39	    ~5.9pp（60 题的 6.7pp 含抽样方差上浮）。 ProofWriter D5 是深度推理链（depth-5），14B 在长链上更容易产生中间步骤分歧，
40	    C0 预期 ~50%；但 PW 的正确答案更确定（二分类 True/False）， MaxSAT 的约束质量在形式化推理上更高，使 tiebreak 有效但
41	    margin 较小（1.8pp）。 804 题的 bootstrap 显著性：combined gap 3.8pp 在 n=804 下标准误约 1.5pp，
42	    z≈2.5 对应 p≈0.023，落入 [0.01, 0.05] 区间。 Tie 频率 ~11% 符合 K=12 偶数采样的概率预期： K=12 下 6:6
43	    tie 概率约 C(12,6)/2^12 ≈ 0.225 乘以双候选题比例 ~0.47 ≈ 0.106。 Tiebreak 胜率 76% 反映 MaxSAT
44	    约束加权在多数情况下指向正确答案， 但约 24% 的 tie 中约束本身也有噪声导致错判。
45	
46	    '
47	  tables:
48	  - name: 'Table 1: Main Results — SICA vs SC on 804 Questions'
49	    columns:
50	    - Dataset
51	    - N
52	    - SC_Acc
53	    - SICA_Acc
54	    - Gap_pp
55	    - p_value
56	    - C0
57	    rows:
58	    - - FOLIO
59	      - 204
60	      - 73.5
61	      - 79.4
62	      - 5.9
63	      - 0.018
64	      - 0.42
65	    - - ProofWriter_D5
66	      - 600
67	      - 66.8
68	      - 68.6
69	      - 1.8
70	      - 0.11
71	      - 0.5
72	    - - Combined
73	      - 804
74	      - 67.5
75	      - 71.3
76	      - 3.8
77	      - 0.023
78	      - 0.47
79	  - name: 'Table 2: Tiebreak Analysis (K=12)'
80	    columns:
81	    - Metric
82	    - FOLIO
83	    - ProofWriter
84	    - Combined
85	    rows:
86	    - - Tie_questions
87	      - 27/204 (13.2%)
88	      - 60/600 (10.0%)
89	      - 87/804 (10.8%)
90	    - - SICA_wins_on_ties
91	      - 21/27 (77.8%)
92	      - 45/60 (75.0%)
93	      - 66/87 (75.9%)
94	    - - SC_wins_on_ties
95	      - 6/27 (22.2%)
96	      - 15/60 (25.0%)
97	      - 21/87 (24.1%)
98	  figures_description:
99	  - 'Fig 1: Per-question accuracy delta (SICA − SC) histogram, 804 questions. 大部分
100	    delta=0（非 tie 题），正向 spike 在 tie 题上清晰可见。'
101	  - 'Fig 2: Accuracy vs question index, FOLIO 204 题，SC 和 SICA 曲线对比，标注 tie 题位置。'
102	  analysis: '核心发现：60→804 扩展后 gap 从 3.3pp 微增至 3.8pp（FOLIO 贡献主力）， p 值从 0.226 降至 0.023，跨过
103	    0.05 显著性门槛。 ProofWriter 从 0pp 升至 1.8pp——虽然单域不显著（p=0.11）， 但非零增益消除了 "SICA only works
104	    on FOLIO" 的攻击面。 Combined p=0.023 支撑 C1 的统计显著性 claim。 Tie 频率 10.8% 落入预期区间 [8%,
105	    15%]，说明 K=12 的 tie 机制是稳健的、非偶发的。
106	
107	    '
108	- name: sica_k_ablation_14b
109	  plan_id: exp-002
110	  description: K sensitivity (K=6,8,12,16,20) on D012's 60 questions
111	  expected_results:
112	    K6_sica_acc: 0.717
113	    K6_sc_acc: 0.7
114	    K6_gap_pp: 1.7
115	    K6_tie_fraction: 0.067
116	    K6_c0: 0.483
117	    K8_sica_acc: 0.733
118	    K8_sc_acc: 0.7
119	    K8_gap_pp: 3.3
120	    K8_tie_fraction: 0.083
121	    K8_c0: 0.517
122	    K12_sica_acc: 0.733
123	    K12_sc_acc: 0.7
124	    K12_gap_pp: 3.3
125	    K12_tie_fraction: 0.117
126	    K12_c0: 0.533
127	    K16_sica_acc: 0.75
128	    K16_sc_acc: 0.7
129	    K16_gap_pp: 5.0
130	    K16_tie_fraction: 0.133
131	    K16_c0: 0.55
132	    K20_sica_acc: 0.767
133	    K20_sc_acc: 0.717
134	    K20_gap_pp: 5.0
135	    K20_tie_fraction: 0.117
136	    K20_c0: 0.567
137	    best_gap_K: 16
138	    best_gap_pp: 5.0
139	    gpu_hours: ~4.5
140	  result_rationale: 'K ablation 的物理直觉：K 增大 → 采样更多 traces → 两个效应同时发生： (1) SC 的 majority
141	    vote 更稳定（law of large numbers），SC accuracy 微升； (2) 偶数 K 下 tie 概率先升后降（binomial
142	    分布 C(K,K/2)/2^K 在 K=12~16 附近最高）， 且更多 traces 给 MaxSAT 更多约束信息，tiebreak 质量提升。 K=6：tie
143	    概率低（C(6,3)/2^6=0.3125，但仅对多候选题），约 3-4 题出现 tie， SICA 赢其中 2-3 题，gap 小（1.7pp）。 K=8：tie
144	    频率上升，gap 达到 3.3pp。 K=12：已有实验数据，3.3pp 复现。 K=16：tie 的绝对数虽然与 K=12 相近（binomial peak
145	    开始移走），但约束数量翻倍， MaxSAT 对 tie 的判断更准确，gap 升至 5.0pp。这是 best-gap K。 K=20：SC 自身稳定性提高（更多
146	    votes 压低 tie 概率），tie_fraction 回落至与 K=12 持平， 但 SC baseline 也升至 71.7%，gap 维持 5.0pp。
147	    总体呈现 "先升后平" 的 gap-vs-K 曲线，best gap 在 K=16，符合 [4.0, 7.0] 区间。
148	
149	    '
150	  tables:
151	  - name: 'Table 3: K Ablation on 60 Questions (Qwen2.5-14B-Instruct)'
152	    columns:
153	    - K
154	    - SC_Acc
155	    - SICA_Acc
156	    - Gap_pp
157	    - Tie_Frac
158	    - C0
159	    - Constraints_per_Q
160	    rows:
161	    - - 6
162	      - 70.0
163	      - 71.7
164	      - 1.7
165	      - 6.7%
166	      - 0.483
167	      - ~80
168	    - - 8
169	      - 70.0
170	      - 73.3
171	      - 3.3
172	      - 8.3%
173	      - 0.517
174	      - ~110
175	    - - 12
176	      - 70.0
177	      - 73.3
178	      - 3.3
179	      - 11.7%
180	      - 0.533
181	      - ~150
182	    - - 16
183	      - 70.0
184	      - 75.0
185	      - 5.0
186	      - 13.3%
187	      - 0.55
188	      - ~195
189	    - - 20
190	      - 71.7
191	      - 76.7
192	      - 5.0
193	      - 11.7%
194	      - 0.567
195	      - ~240
196	  figures_description:
197	  - 'Fig 3: SICA-SC gap (pp) vs K, bar chart with tie_fraction overlay line. 显示 gap
198	    随 K 增大先陡升后趋平。'
199	  - 'Fig 4: Tiebreak win rate vs K, 显示约束数量增加提升 tiebreak 质量。'
200	  analysis: 'K ablation 回答两个关键问题：(1) SICA 的增益是否仅依赖 tie——是的，非 tie 题上 SICA≡SC， 但 tie
201	    频率随 K 变化是可预测的（binomial 模型）；(2) 最佳 K 是什么——K=16 达到 peak gap 5.0pp， 但 K=12 是 cost-performance
202	    最优点（gap 3.3pp，GPU 时间仅 K=16 的 75%）。 这为论文提供了 practical recommendation：K=12 作为默认值，K=16
203	    如果预算允许。 Odd-K 未测试（odd K 不产生精确 tie），留作 appendix 说明。
204	
205	    '
206	- name: tiebreak_baseline_analysis
207	  plan_id: exp-003
208	  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available
209	    data
210	  expected_results:
211	    sica_acc_804: 0.713
212	    sc_alphabetical_acc_804: 0.675
213	    sc_random_acc_804: 0.681
214	    sc_first_seen_acc_804: 0.67
215	    sica_vs_random_gap_pp: 3.2
216	    sica_vs_alphabetical_gap_pp: 3.8
217	    sica_vs_first_seen_gap_pp: 4.3
218	    sica_tiebreak_win_60q: 4/5 (80%)
219	    random_tiebreak_expected_60q: 2.5/5 (50%)
220	    alphabetical_tiebreak_60q: 3/5 (60%)
221	    first_seen_tiebreak_60q: 2/5 (40%)
222	  result_rationale: 'Tiebreak baseline 分析的关键在于：SC-random 是最公平的 baseline，因为它不引入系统性偏差。
223	    在 804 题上，SC-random 的期望准确率 = SC-deterministic 在非 tie 题上的准确率 + 0.5 × tie 题数量 / 总题数（tie
224	    时 50/50 猜对）。 计算：非 tie 题 717/804 的 SC acc 约 73.1%，tie 题 87/804 随机猜对 ~50%， 所以 SC-random
225	    ≈ 0.731 × (717/804) + 0.5 × (87/804) ≈ 0.681。 SICA 在 tie 题上 76% win rate → SICA
226	    比 random 多赢 ~26% × 87 ≈ 22.6 题 → gap ≈ 2.8pp。 但 SICA 在约束明确的 tie 题上几乎必赢，在约束噪声大的
227	    tie 题上也不比 random 差太多 （MaxSAT 在约束矛盾时退化为多数约束投票，仍然 ≥ random），因此 gap 为正。 这回答了 reviewer
228	    的 "random tiebreak closes the gap" 攻击： 不能，因为 SICA 的 tiebreak 是 informed（基于逻辑约束），胜率显著高于
229	    chance。
230	
231	    '
232	  tables:
233	  - name: 'Table 4: Tiebreak Strategy Comparison (804 Questions)'
234	    columns:
235	    - Method
236	    - Acc
237	    - Gap_vs_SICA_pp
238	    - Tiebreak_Mechanism
239	    rows:
240	    - - SICA
241	      - 71.3
242	      - —
243	      - MaxSAT weighted constraints
244	    - - SC-random
245	      - 68.1
246	      - -3.2
247	      - Uniform random on ties
248	    - - SC-alphabetical
249	      - 67.5
250	      - -3.8
251	      - Alphabetical first on ties
252	    - - SC-first-seen
253	      - 67.0
254	      - -4.3
255	      - First generated answer on ties
256	  figures_description:
257	  - 'Fig 5: Tiebreak accuracy comparison bar chart, 仅在 tie 题子集上展示四种方法的准确率。SICA 76%
258	    vs random 50% vs alphabetical 55% vs first-seen 43%。'
259	  analysis: 'SICA 对 SC-random（最公平 baseline）仍有 3.2pp 优势，说明增益不是 "刚好比一个差的 tiebreak 规则好"，
260	    而是 MaxSAT 约束确实编码了有用的推理信息。First-seen 最差（67.0%）因为第一条 trace 往往是 greedy-like 的，遇到难题时更可能犯错。Alphabetical
261	    的 60% 有偶然成分（某些答案碰巧排序靠前且正确）。
262	
263	    '
264	- name: sica_7b_scaling
265	  plan_id: exp-004
266	  description: Run SICA with Qwen2.5-7B-Instruct on same 60 questions
267	  expected_results:
268	    sica_accuracy: 0.633
269	    sc_accuracy: 0.567
270	    sica_sc_gap_pp: 6.7
271	    c0_multi_candidate_rate: 0.683
272	    tie_question_fraction: 0.15
273	    tiebreak_win_rate: 0.78
274	    folio_sica: 0.7
275	    folio_sc: 0.6
276	    folio_gap_pp: 10.0
277	    proofwriter_sica: 0.6
278	    proofwriter_sc: 0.55
279	    proofwriter_gap_pp: 5.0
280	    bootstrap_p: 0.087
281	    total_constraints_raw: ~4800
282	    constraint_quality_vs_14b: lower — more parse failures, ~15% extraction failure
283	      rate
284	    gpu_hours: ~1.5
285	  result_rationale: '7B 模型比 14B 弱，两个关键效应： (1) SC baseline 更低（56.7% vs 70.0%），因为 7B
286	    的推理能力更弱； (2) C0 更高（68.3% vs 53.3%），因为 7B 的 trace 多样性更大—— 弱模型对同一问题产生不同推理路径的概率更高，表现为更多多候选答案和更多
287	    ties。 更高的 C0 + 更多 ties → SICA 有更大操作空间 → gap 扩大至 6.7pp。 但约束提取质量下降（7B 的 FOL 翻译更多语法错误），部分抵消了
288	    diversity 带来的优势。 净效应：gap 翻倍（6.7 vs 3.3），但 absolute accuracy 下降。 这完美支撑 C2（operating
289	    regime）和 C3（C0 as predictor）： C0 从 14B 的 53% 升至 7B 的 68%，gap 从 3.3pp 升至 6.7pp，单调正相关。
290	    Bootstrap p=0.087 在 60 题上不显著（预期内，n 太小），但方向一致。
291	
292	    '
293	  tables:
294	  - name: 'Table 5: 7B vs 14B Comparison (60 Questions)'
295	    columns:
296	    - Model
297	    - SC_Acc
298	    - SICA_Acc
299	    - Gap_pp
300	    - C0
301	    - Tie_Frac
302	    rows:
303	    - - Qwen2.5-7B-Instruct
304	      - 56.7
305	      - 63.3
306	      - 6.7
307	      - 0.683
308	      - 0.15
309	    - - Qwen2.5-14B-Instruct
310	      - 70.0
311	      - 73.3
312	      - 3.3
313	      - 0.533
314	      - 0.117
315	  figures_description:
316	  - 'Fig 6: C0 vs SICA-SC gap scatter plot (初步两点 + QwQ 零点)。7B 在右上角，14B 在中间，QwQ 在原点附近。'
317	  analysis: '7B 数据点完美落在 C0-gap 正相关线上。结合 QwQ 的 (C0=3.6%, gap=0pp) 数据点， 三点已经初步支撑 C3
318	    claim。等 72B 数据补上后四点拟合将更有说服力。 一个有趣的 insight：7B 的 SICA gap 更大，但 absolute accuracy
319	    更低。 这意味着 SICA 不是 "让弱模型变强" 的银弹，而是 "在模型本身的能力范围内最大化共识质量"。
320	
321	    '
322	- name: qwq_32b_operating_regime
323	  plan_id: exp-005
324	  description: QwQ-32B negative results formatted for Operating Regime Analysis section
325	  expected_results:
326	    aime_c0: 0.0
327	    aime_sica_sc_gap: 0.0
328	    folio_c0: 0.0
329	    folio_sica_sc_gap: 0.0
330	    proofwriter_c0: 0.1875
331	    proofwriter_sica_sc_gap: 0.0
332	    combined_c0: 0.036
333	    combined_sica_sc_gap: 0.0
334	    n_total: 48
335	    trace_entropy_qwq: 0.12
336	    trace_entropy_14b: 1.83
337	    trace_entropy_7b: 2.41
338	  result_rationale: 'QwQ-32B 是 reasoning model，其 CoT 过程内部已经执行了隐式的 "多路径搜索 + 自我验证"，
339	    导致不同 temperature 采样出的 traces 几乎收敛到同一答案（C0≈0%）。 这不是因为 QwQ 更 "聪明"（它确实更聪明，但关键不在准确率），
340	    而是因为 reasoning model 的训练目标（extended thinking + verification）压缩了输出分布。 SICA 需要 trace
341	    diversity 来工作——当所有 K 条 traces 给出相同答案， MaxSAT 无论怎么加权都只能选同一个答案。SICA 在数学上退化为 SC。
342	    Trace entropy 量化了这一点：QwQ 的 0.12 bits 对比 14B 的 1.83 bits（15x 差距）。 ProofWriter 上
343	    QwQ 有 18.75% C0，但 n=16 太小且增益为零—— 因为 C0=18.75% 中的多候选题上 QwQ 的 "错误" trace 其约束一致性也很高（reasoning
344	    model 连犯错都很自洽）， MaxSAT 无法区分正确和错误的一致性约束。
345	
346	    '
347	  tables:
348	  - name: 'Table 6: Operating Regime — Reasoning vs Instruction Models'
349	    columns:
350	    - Model
351	    - Type
352	    - C0
353	    - SICA-SC_Gap
354	    - Trace_Entropy
355	    - N
356	    rows:
357	    - - QwQ-32B
358	      - Reasoning
359	      - 3.6%
360	      - 0.0pp
361	      - 0.12
362	      - 48
363	    - - Qwen2.5-14B-Instruct
364	      - Instruction
365	      - 53.3%
366	      - +3.3pp
367	      - 1.83
368	      - 60
369	    - - Qwen2.5-7B-Instruct
370	      - Instruction
371	      - 68.3%
372	      - +6.7pp
373	      - 2.41
374	      - 60
375	  figures_description:
376	  - 'Fig 7: Operating regime diagram. X 轴 = C0, Y 轴 = SICA-SC gap. 左侧 ''degenerate
377	    zone'' (C0<10%), 右侧 ''effective zone'' (C0>20%). QwQ 在左，两个 instruction models
378	    在右。'
379	  analysis: '这是论文的核心 intellectual contribution。不说 "SICA 不如 reasoning model"， 而是说 "SICA
380	    和 reasoning model 解决不同的问题"：reasoning model 通过内部验证压缩了输出分布， 不需要外部共识机制；instruction
381	    model 输出多样性高，需要也能够从外部共识中获益。 这是一个 model property，不是 task property——同一个 task (FOLIO)
382	    在两种模型上表现完全不同。
383	
384	    '
385	- name: c0_diagnostic_validation
386	  plan_id: exp-006
387	  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0
388	    as predictor.
389	  expected_results:
390	    data_points:
391	    - model: QwQ-32B
392	      K: 12
393	      C0: 0.036
394	      gap_pp: 0.0
395	    - model: Qwen2.5-72B-AWQ
396	      K: 12
397	      C0: 0.3
398	      gap_pp: 1.7
399	    - model: Qwen2.5-14B-Instruct
400	      K: 6
401	      C0: 0.483
402	      gap_pp: 1.7
403	    - model: Qwen2.5-14B-Instruct
404	      K: 8
405	      C0: 0.517
406	      gap_pp: 3.3
407	    - model: Qwen2.5-14B-Instruct
408	      K: 12
409	      C0: 0.533
410	      gap_pp: 3.3
411	    - model: Qwen2.5-14B-Instruct
412	      K: 16
413	      C0: 0.55
414	      gap_pp: 5.0
415	    - model: Qwen2.5-14B-Instruct
416	      K: 20
417	      C0: 0.567
418	      gap_pp: 5.0
419	    - model: Qwen2.5-7B-Instruct
420	      K: 12
421	      C0: 0.683
422	      gap_pp: 6.7
423	    pearson_r: 0.94
424	    spearman_rho: 0.93
425	    linear_fit_slope: 10.2
426	    linear_fit_intercept: -2.1
427	    linear_fit_r2: 0.88
428	    c0_threshold_for_positive_gap: 0.21
429	  result_rationale: 'C0 与 gap 的正相关来自因果链：C0 高 → 更多题存在多候选 → 更多 tie → SICA 有操作空间 → gap
430	    大。 这不是 confound（比如 "弱模型 C0 高且 gap 大是因为 baseline 低"）， 因为 K ablation 在同一模型上也展现了
431	    C0-gap 正相关（K 增大 → C0 微增 → gap 增大）， 排除了模型能力这个 confound。 8 个数据点（4 models × varying
432	    K）的 Pearson r=0.94，线性拟合 R²=0.88。 斜率 10.2 表示 C0 每增加 10pp，SICA-SC gap 增加约 1.0pp。
433	    截距 -2.1 表示 C0 需要超过 ~21% 才能期望正增益——这与 QwQ 的 C0=3.6%→gap=0 和 D016 precheck 的 C0≥20%
434	    作为 go/no-go 门槛一致。 Spearman ρ=0.93 确认单调性（非线性关系也 OK）。
435	
436	    '
437	  tables:
438	  - name: 'Table 7: C0 as Predictor — Linear Regression'
439	    columns:
440	    - Metric
441	    - Value
442	    rows:
443	    - - Pearson_r
444	      - 0.94
445	    - - Spearman_ρ
446	      - 0.93
447	    - - Slope
448	      - 10.2 pp gap per unit C0
449	    - - Intercept
450	      - -2.1pp
451	    - - R²
452	      - 0.88
453	    - - C0_threshold
454	      - 0.21 (gap > 0)
455	  figures_description:
456	  - 'Fig 8 (论文核心图): C0 vs SICA-SC gap 散点图。X 轴 C0 [0, 0.7], Y 轴 gap [-1, 8]pp。4 种 model
457	    用不同 marker，同 model 不同 K 用颜色深浅。线性回归线 + 95% CI band。阴影区域标注 ''Degenerate Zone'' (C0<0.21)
458	    和 ''Effective Zone''。'
459	  - 'Fig 9: C0 的计算不需要运行 MaxSAT（只需要 traces），所以是 zero-cost predictor。示意图展示 practitioner
460	    workflow: generate K traces → compute C0 → if C0>20% then run SICA, else use SC。'
461	  analysis: 'C3 claim 的核心证据。Pearson r=0.94 和 R²=0.88 在 8 个数据点上非常强。 reviewer 可能的攻击：(1)
462	    只有 8 个点——回应是这是 4 个不同模型 + K 变化，覆盖了 C0 从 3.6% 到 68% 的全范围； (2) 因果方向不确定——回应是 C0 是
463	    SICA 的输入（先于 MaxSAT 计算），因果方向明确； (3) 更多模型可能打破单调性——acknowledge as limitation，但当前
464	    4 models 跨越了 3B-72B 规模和 reasoning/instruction 两种类型。
465	
466	    '
467	- name: sica_72b_awq
468	  plan_id: exp-007
469	  description: Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions
470	  expected_results:
471	    sica_accuracy: 0.8
472	    sc_accuracy: 0.783
473	    sica_sc_gap_pp: 1.7
474	    c0_multi_candidate_rate: 0.3
475	    tie_question_fraction: 0.067
476	    tiebreak_win_rate: 0.75
477	    folio_sica: 0.867
478	    folio_sc: 0.833
479	    folio_gap_pp: 3.3
480	    proofwriter_sica: 0.767
481	    proofwriter_sc: 0.767
482	    proofwriter_gap_pp: 0.0
483	    bootstrap_p: 0.34
484	    constraint_quality: higher than 14B — fewer parse errors, more precise FOL
485	    gpu_hours: ~3.5
486	    gpu_mem_gib: ~52
487	  result_rationale: '72B 是 "强 instruction model"——比 14B 聪明但仍是 instruction 架构（非 reasoning
488	    model）， 所以 C0 不会像 QwQ 那样降到零，但会显著低于 14B。 预期 C0=30%：72B 的推理一致性更高（更多题所有 traces 给出相同答案），
489	    但遇到真正难题时仍会产生 divergence。 SC baseline 高（78.3%），已接近 FOLIO/PW 的天花板，留给 SICA 的空间很小。
490	    Tie 频率低（6.7%），只有 ~4 题出现 tie，其中 SICA 赢 3 题 → gap 1.7pp。 ProofWriter 上 72B 的 accuracy
491	    已经够高，tie 可能 0-1 题 → gap 0pp。 这个结果完美支撑 operating regime 叙事：72B 在 QwQ（C0→0, gap→0）和
492	    14B（C0=53%, gap=3.3pp）之间， 形成 7B→14B→72B→QwQ 的 C0 递减、gap 递减梯度。 Bootstrap p=0.34
493	    在 60 题上不显著——预期内，因为只有 4 题 tie 无法产生统计 power。 这正是为什么 exp-007 是 P1 而非 P0：它的价值在于 C0-gap
494	    散点图的第四个点， 不在于独立的显著性检验。
495	
496	    '
497	  tables:
498	  - name: 'Table 8: Model Scaling — 7B / 14B / 72B / QwQ (60 Questions)'
499	    columns:
500	    - Model
501	    - Size
502	    - Type
503	    - SC_Acc
504	    - SICA_Acc
505	    - Gap_pp
506	    - C0
507	    rows:
508	    - - Qwen2.5-7B-Instruct
509	      - 7B
510	      - Instruction
511	      - 56.7
512	      - 63.3
513	      - 6.7
514	      - 0.683
515	    - - Qwen2.5-14B-Instruct
516	      - 14B
517	      - Instruction
518	      - 70.0
519	      - 73.3
520	      - 3.3
521	      - 0.533
522	    - - Qwen2.5-72B-AWQ
523	      - 72B
524	      - Instruction
525	      - 78.3
526	      - 80.0
527	      - 1.7
528	      - 0.3
529	    - - QwQ-32B
530	      - 32B
531	      - Reasoning
532	      - —
533	      - —
534	      - 0.0
535	      - 0.036
536	  figures_description:
537	  - 'Fig 10: 四模型的 C0 和 gap 条形图并列。清晰展示 instruction model 的 size↑ → C0↓ → gap↓ 梯度，以及
538	    reasoning model 的断崖式 C0 下降。'
539	  analysis: '72B 数据确认了 operating regime 的 scaling dimension：即使在同一架构系列内， 模型规模增大也会降低
540	    trace diversity（更强的模型更自信、更一致）， 从而缩小 SICA 的操作空间。但关键区分是 "缩小" vs "消失"： 72B 的 C0=30%
541	    仍远高于 QwQ 的 3.6%，说明 instruction→reasoning 的跃迁才是决定性的， 而非单纯的规模增大。这为论文提供了更精细的 insight。
542	
543	    '
544	- name: constraint_quality_case_studies
545	  plan_id: exp-008
546	  description: Qualitative analysis of extracted constraints on 5-10 representative
547	    questions
548	  expected_results:
549	    cases_analyzed: 8
550	    categories:
551	      correct_and_helpful: 5
552	      correct_but_redundant: 1
553	      incorrect_but_excluded: 1
554	      incorrect_and_harmful: 1
555	    example_folio_tie_win:
556	      question_summary: FOLIO question about organizational membership and property
557	        inheritance
558	      k12_vote_split: '6 True : 6 False'
559	      sica_answer: True (correct)
560	      sc_alphabetical: False (wrong)
561	      key_constraint: ∀x(Member(x,Org) → HasProperty(x,P)), weight=0.83
562	      why_sica_wins: 6 True-traces 提取的约束互相一致（满足率 92%），6 False-traces 的约束自相矛盾（满足率 61%），MaxSAT
563	        正确偏向 True。
564	    example_proofwriter_miss:
565	      question_summary: PW D5 深度链推理，5步推导
566	      sica_answer: False (wrong)
567	      correct_answer: 'True'
568	      why_sica_fails: 中间步骤的 FOL 翻译错误（否定词遗漏），导致约束指向错误方向。7/12 traces 含相同翻译错误。
569	    extraction_failure_rate: 0.02
570	    avg_constraints_per_trace: 13.2
571	    avg_unique_constraints_per_question: 28.7
572	  result_rationale: 'Case study 的目的是让 reviewer 看到 SICA 不是黑盒——约束有语义可解释性。 在 best tier
573	    下，多数 case 展示 SICA 的约束确实编码了推理中的逻辑关系， MaxSAT 的加权机制合理地偏向了一致性更高的答案。 选择 8 个 case：5
574	    个 SICA 正确发挥、1 个冗余但无害、1 个错误约束被 exclusion 机制过滤、 1 个 SICA 犯错的反例（诚实展示局限性）。 FOLIO 的
575	    tie-win case 最有说服力：展示 MaxSAT 如何利用约束一致性区分两组 traces。 ProofWriter 的 failure case
576	    揭示了约束提取的瓶颈（FOL 翻译质量）， 为 future work（更好的 FOL extractor）提供了明确方向。
577	
578	    '
579	  tables: []
580	  figures_description:
581	  - 'Fig 11: 一个 FOLIO tie-win case 的完整可视化：12 条 traces 的投票分布、提取的约束集合、MaxSAT 权重、最终判决。用颜色编码正确/错误
582	    traces 和满足/违反的约束。'
583	  - 'Fig 12: 约束质量分布直方图：extraction rate、parse success rate、semantic correctness rate（人工标注
584	    50 条约束）。'
585	  analysis: 'Case studies 将 SICA 从 "accuracy number goes up" 提升为 "we understand WHY
586	    it goes up"。 5/8 cases 展示了约束的语义意义，1/8 的 failure case 防止 reviewer 说 "cherry-picked"。
587	    这是 qualitative contribution，在 EMNLP 评审中有加分作用。
588	
589	    '
590	- name: overhead_analysis
591	  plan_id: exp-009
592	  description: 'Wall-time breakdown per question: generation, constraint extraction,
593	    MaxSAT solving'
594	  expected_results:
595	    avg_total_time_per_question_s: 58.3
596	    avg_generation_time_s: 42.1
597	    avg_extraction_time_s: 14.8
598	    avg_maxsat_time_s: 1.4
599	    generation_fraction: 0.722
600	    extraction_fraction: 0.254
601	    maxsat_fraction: 0.024
602	    overhead_vs_sc_multiplier: 1.39
603	    overhead_vs_sc_description: SC 只需 generation (42.1s)，SICA 额外需要 extraction+MaxSAT
604	      (16.2s)，增加 39% wall time
605	    marginal_cost_per_pp_gain: 4.3s per 1pp accuracy gain
606	    maxsat_z3_avg_time_ms: 47
607	    maxsat_z3_max_time_ms: 312
608	    constraint_extraction_method: LLM-based (same model, separate prompt)
609	    extraction_tokens_per_question: ~2800
610	  result_rationale: 'Overhead 分析对 reviewer concern "is it worth it" 至关重要。 Generation
611	    占 72% wall time——这与 SC 相同（K=12 条 traces），不是 SICA 的 overhead。 SICA 的真正 overhead
612	    是 constraint extraction (25%) + MaxSAT solving (2.4%)。 Extraction 用同模型做 FOL 翻译，每条
613	    trace ~2800 tokens，12 traces 串行处理需要 ~14.8s。 MaxSAT (Z3) 平均 47ms 每题——trivially
614	    fast，因为约束数通常 <100（Z3 处理数千约束毫无压力）。 总 overhead multiplier 1.39x 意味着每题多花 39% 时间换取
615	    3.8pp accuracy gain—— 这在多数应用场景下是 acceptable 的 trade-off。 进一步：extraction 可以并行化（12
616	    traces 同时提取），理论上压缩到 ~3s， 使 multiplier 降至 1.10x。但当前实现是串行的，论文报告实际数字更诚实。
617	
618	    '
619	  tables:
620	  - name: 'Table 9: Overhead Analysis (Qwen2.5-14B-Instruct, K=12, 804 Questions)'
621	    columns:
622	    - Stage
623	    - Avg_Time_s
624	    - Fraction
625	    - Parallelizable
626	    rows:
627	    - - Trace_Generation
628	      - 42.1
629	      - 72.2%
630	      - Yes (vLLM batched)
631	    - - Constraint_Extraction
632	      - 14.8
633	      - 25.4%
634	      - Yes (per-trace independent)
635	    - - MaxSAT_Solving
636	      - 1.4
637	      - 2.4%
638	      - No (single Z3 call)
639	    - - Total
640	      - 58.3
641	      - 100%
642	      - ''
643	    - - SC_Equivalent
644	      - 42.1
645	      - —
646	      - ''
647	    - - SICA_Overhead
648	      - 16.2
649	      - +38.5%
650	      - ''
651	  figures_description:
652	  - 'Fig 13: Stacked bar chart 展示 per-question wall time 分解。SC bar 只有 generation，SICA
653	    bar 有 generation + extraction + MaxSAT。MaxSAT 几乎不可见（太小了）。'
654	  analysis: Key talking point：SICA 的 "重" 在约束提取（LLM 调用），不在 MaxSAT 求解。 这意味着 (1) overhead
655	    随 LLM inference 成本线性下降（模型越快，overhead 越低）， (2) MaxSAT 本身不是瓶颈（可以扩展到更多约束）， (3) 如果用
656	    fine-tuned 小模型做 extraction 可以进一步降低 overhead（future work）。 39% overhead 换 3.8pp
657	    gain 的 cost-effectiveness 优于大多数 ensembling 方法 （如 majority voting over 2K traces
658	    需要 100% overhead 且 gain 通常 <2pp）。
659	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63733342-b757-49de-88bc-a0fab11487e5",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "e591e64c-819c-47f1-acd6-64a763367729",
  "sourceToolAssistantUUID": "63733342-b757-49de-88bc-a0fab11487e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T06:19:59.443Z_

<details open><summary>🔧 Tool call — Read · `toolu_014gmhVfBmsrpD2oNbiaL4D4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e591e64c-819c-47f1-acd6-64a763367729",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mDzeA87VCK4V1SWSgm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b86cba79-1e28-4082-acae-bf01294ae23b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwHqKxNvwxjE4fiU9c1M78",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8279,
      "cache_read_input_tokens": 19843,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8279
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 19843,
          "cache_creation_input_tokens": 8279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8279,
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

_source line 25 · 2026-05-16T06:19:59.450Z_

<details><summary>↩ Tool result · `toolu_014gmhVfBmsrpD2oNbiaL4D4`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。标题可用 "Principled Symbolic Consensus Improves
2	  LLM Reasoning"。 三条 claim 原样保留：C1 用扩展实验的显著 p 值支撑，C2 用 QwQ 负结果 + 多模型 C0 梯度支撑， C3 用
3	  C0-gap 散点图支撑。ProofWriter 非零增益消除 "domain-specific" 攻击面。 Operating regime 作为理论贡献锦上添花，而非防御性
4	  reframe。EMNLP main 强投。
5	
6	  '
7	imagined_experiments:
8	- name: sica_expanded_14b
9	  plan_id: exp-001
10	  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,
11	    T=0.7'
12	  expected_results:
13	    sica_accuracy_combined: 0.713
14	    sc_accuracy_combined: 0.675
15	    sica_sc_gap_combined_pp: 3.8
16	    folio_sica_accuracy: 0.794
17	    folio_sc_accuracy: 0.735
18	    folio_gap_pp: 5.9
19	    proofwriter_sica_accuracy: 0.686
20	    proofwriter_sc_accuracy: 0.668
21	    proofwriter_gap_pp: 1.8
22	    bootstrap_p_combined: 0.023
23	    bootstrap_p_folio: 0.018
24	    bootstrap_p_proofwriter: 0.11
25	    c0_combined: 0.47
26	    c0_folio: 0.42
27	    c0_proofwriter: 0.5
28	    tie_question_fraction_combined: 0.11
29	    tie_question_fraction_folio: 0.13
30	    tie_question_fraction_proofwriter: 0.1
31	    tiebreak_win_rate: 0.76
32	    total_constraints_raw: ~78000
33	    total_constraints_unique: ~23000
34	    maxsat_exclusion_rate: 0.031
35	    wall_time_hours: ~13
36	  result_rationale: 'D012 的 60 题结果中，14B 的 C0=53.3%，说明约半数题存在多候选答案，SICA 有操作空间。 扩展到 804
37	    题后，FOLIO 从 30→204 题——该数据集本身推理链多样性高（FOL 翻译歧义多）， C0 预期维持 ~42%，gap 从 6.7pp 略回归均值至
38	    ~5.9pp（60 题的 6.7pp 含抽样方差上浮）。 ProofWriter D5 是深度推理链（depth-5），14B 在长链上更容易产生中间步骤分歧，
39	    C0 预期 ~50%；但 PW 的正确答案更确定（二分类 True/False）， MaxSAT 的约束质量在形式化推理上更高，使 tiebreak 有效但
40	    margin 较小（1.8pp）。 804 题的 bootstrap 显著性：combined gap 3.8pp 在 n=804 下标准误约 1.5pp，
41	    z≈2.5 对应 p≈0.023，落入 [0.01, 0.05] 区间。 Tie 频率 ~11% 符合 K=12 偶数采样的概率预期： K=12 下 6:6
42	    tie 概率约 C(12,6)/2^12 ≈ 0.225 乘以双候选题比例 ~0.47 ≈ 0.106。 Tiebreak 胜率 76% 反映 MaxSAT
43	    约束加权在多数情况下指向正确答案， 但约 24% 的 tie 中约束本身也有噪声导致错判。
44	
45	    '
46	  tables:
47	  - name: 'Table 1: Main Results — SICA vs SC on 804 Questions'
48	    columns:
49	    - Dataset
50	    - N
51	    - SC_Acc
52	    - SICA_Acc
53	    - Gap_pp
54	    - p_value
55	    - C0
56	    rows:
57	    - - FOLIO
58	      - 204
59	      - 73.5
60	      - 79.4
61	      - 5.9
62	      - 0.018
63	      - 0.42
64	    - - ProofWriter_D5
65	      - 600
66	      - 66.8
67	      - 68.6
68	      - 1.8
69	      - 0.11
70	      - 0.5
71	    - - Combined
72	      - 804
73	      - 67.5
74	      - 71.3
75	      - 3.8
76	      - 0.023
77	      - 0.47
78	  - name: 'Table 2: Tiebreak Analysis (K=12)'
79	    columns:
80	    - Metric
81	    - FOLIO
82	    - ProofWriter
83	    - Combined
84	    rows:
85	    - - Tie_questions
86	      - 27/204 (13.2%)
87	      - 60/600 (10.0%)
88	      - 87/804 (10.8%)
89	    - - SICA_wins_on_ties
90	      - 21/27 (77.8%)
91	      - 45/60 (75.0%)
92	      - 66/87 (75.9%)
93	    - - SC_wins_on_ties
94	      - 6/27 (22.2%)
95	      - 15/60 (25.0%)
96	      - 21/87 (24.1%)
97	  figures_description:
98	  - 'Fig 1: Per-question accuracy delta (SICA − SC) histogram, 804 questions. 大部分
99	    delta=0（非 tie 题），正向 spike 在 tie 题上清晰可见。'
100	  - 'Fig 2: Accuracy vs question index, FOLIO 204 题，SC 和 SICA 曲线对比，标注 tie 题位置。'
101	  analysis: '核心发现：60→804 扩展后 gap 从 3.3pp 微增至 3.8pp（FOLIO 贡献主力）， p 值从 0.226 降至 0.023，跨过
102	    0.05 显著性门槛。 ProofWriter 从 0pp 升至 1.8pp——虽然单域不显著（p=0.11）， 但非零增益消除了 "SICA only works
103	    on FOLIO" 的攻击面。 Combined p=0.023 支撑 C1 的统计显著性 claim。 Tie 频率 10.8% 落入预期区间 [8%,
104	    15%]，说明 K=12 的 tie 机制是稳健的、非偶发的。
105	
106	    '
107	- name: sica_k_ablation_14b
108	  plan_id: exp-002
109	  description: K sensitivity (K=6,8,12,16,20) on D012's 60 questions
110	  expected_results:
111	    K6_sica_acc: 0.717
112	    K6_sc_acc: 0.7
113	    K6_gap_pp: 1.7
114	    K6_tie_fraction: 0.067
115	    K6_c0: 0.483
116	    K8_sica_acc: 0.733
117	    K8_sc_acc: 0.7
118	    K8_gap_pp: 3.3
119	    K8_tie_fraction: 0.083
120	    K8_c0: 0.517
121	    K12_sica_acc: 0.733
122	    K12_sc_acc: 0.7
123	    K12_gap_pp: 3.3
124	    K12_tie_fraction: 0.117
125	    K12_c0: 0.533
126	    K16_sica_acc: 0.75
127	    K16_sc_acc: 0.7
128	    K16_gap_pp: 5.0
129	    K16_tie_fraction: 0.133
130	    K16_c0: 0.55
131	    K20_sica_acc: 0.767
132	    K20_sc_acc: 0.717
133	    K20_gap_pp: 5.0
134	    K20_tie_fraction: 0.117
135	    K20_c0: 0.567
136	    best_gap_K: 16
137	    best_gap_pp: 5.0
138	    gpu_hours: ~4.5
139	  result_rationale: 'K ablation 的物理直觉：K 增大 → 采样更多 traces → 两个效应同时发生： (1) SC 的 majority
140	    vote 更稳定（law of large numbers），SC accuracy 微升； (2) 偶数 K 下 tie 概率先升后降（binomial
141	    分布 C(K,K/2)/2^K 在 K=12~16 附近最高）， 且更多 traces 给 MaxSAT 更多约束信息，tiebreak 质量提升。 K=6：tie
142	    概率低（C(6,3)/2^6=0.3125，但仅对多候选题），约 3-4 题出现 tie， SICA 赢其中 2-3 题，gap 小（1.7pp）。 K=8：tie
143	    频率上升，gap 达到 3.3pp。 K=12：已有实验数据，3.3pp 复现。 K=16：tie 的绝对数虽然与 K=12 相近（binomial peak
144	    开始移走），但约束数量翻倍， MaxSAT 对 tie 的判断更准确，gap 升至 5.0pp。这是 best-gap K。 K=20：SC 自身稳定性提高（更多
145	    votes 压低 tie 概率），tie_fraction 回落至与 K=12 持平， 但 SC baseline 也升至 71.7%，gap 维持 5.0pp。
146	    总体呈现 "先升后平" 的 gap-vs-K 曲线，best gap 在 K=16，符合 [4.0, 7.0] 区间。
147	
148	    '
149	  tables:
150	  - name: 'Table 3: K Ablation on 60 Questions (Qwen2.5-14B-Instruct)'
151	    columns:
152	    - K
153	    - SC_Acc
154	    - SICA_Acc
155	    - Gap_pp
156	    - Tie_Frac
157	    - C0
158	    - Constraints_per_Q
159	    rows:
160	    - - 6
161	      - 70.0
162	      - 71.7
163	      - 1.7
164	      - 6.7%
165	      - 0.483
166	      - ~80
167	    - - 8
168	      - 70.0
169	      - 73.3
170	      - 3.3
171	      - 8.3%
172	      - 0.517
173	      - ~110
174	    - - 12
175	      - 70.0
176	      - 73.3
177	      - 3.3
178	      - 11.7%
179	      - 0.533
180	      - ~150
181	    - - 16
182	      - 70.0
183	      - 75.0
184	      - 5.0
185	      - 13.3%
186	      - 0.55
187	      - ~195
188	    - - 20
189	      - 71.7
190	      - 76.7
191	      - 5.0
192	      - 11.7%
193	      - 0.567
194	      - ~240
195	  figures_description:
196	  - 'Fig 3: SICA-SC gap (pp) vs K, bar chart with tie_fraction overlay line. 显示 gap
197	    随 K 增大先陡升后趋平。'
198	  - 'Fig 4: Tiebreak win rate vs K, 显示约束数量增加提升 tiebreak 质量。'
199	  analysis: 'K ablation 回答两个关键问题：(1) SICA 的增益是否仅依赖 tie——是的，非 tie 题上 SICA≡SC， 但 tie
200	    频率随 K 变化是可预测的（binomial 模型）；(2) 最佳 K 是什么——K=16 达到 peak gap 5.0pp， 但 K=12 是 cost-performance
201	    最优点（gap 3.3pp，GPU 时间仅 K=16 的 75%）。 这为论文提供了 practical recommendation：K=12 作为默认值，K=16
202	    如果预算允许。 Odd-K 未测试（odd K 不产生精确 tie），留作 appendix 说明。
203	
204	    '
205	- name: tiebreak_baseline_analysis
206	  plan_id: exp-003
207	  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available
208	    data
209	  expected_results:
210	    sica_acc_804: 0.713
211	    sc_alphabetical_acc_804: 0.675
212	    sc_random_acc_804: 0.681
213	    sc_first_seen_acc_804: 0.67
214	    sica_vs_random_gap_pp: 3.2
215	    sica_vs_alphabetical_gap_pp: 3.8
216	    sica_vs_first_seen_gap_pp: 4.3
217	    sica_tiebreak_win_60q: 4/5 (80%)
218	    random_tiebreak_expected_60q: 2.5/5 (50%)
219	    alphabetical_tiebreak_60q: 3/5 (60%)
220	    first_seen_tiebreak_60q: 2/5 (40%)
221	  result_rationale: 'Tiebreak baseline 分析的关键在于：SC-random 是最公平的 baseline，因为它不引入系统性偏差。
222	    在 804 题上，SC-random 的期望准确率 = SC-deterministic 在非 tie 题上的准确率 + 0.5 × tie 题数量 / 总题数（tie
223	    时 50/50 猜对）。 计算：非 tie 题 717/804 的 SC acc 约 73.1%，tie 题 87/804 随机猜对 ~50%， 所以 SC-random
224	    ≈ 0.731 × (717/804) + 0.5 × (87/804) ≈ 0.681。 SICA 在 tie 题上 76% win rate → SICA
225	    比 random 多赢 ~26% × 87 ≈ 22.6 题 → gap ≈ 2.8pp。 但 SICA 在约束明确的 tie 题上几乎必赢，在约束噪声大的
226	    tie 题上也不比 random 差太多 （MaxSAT 在约束矛盾时退化为多数约束投票，仍然 ≥ random），因此 gap 为正。 这回答了 reviewer
227	    的 "random tiebreak closes the gap" 攻击： 不能，因为 SICA 的 tiebreak 是 informed（基于逻辑约束），胜率显著高于
228	    chance。
229	
230	    '
231	  tables:
232	  - name: 'Table 4: Tiebreak Strategy Comparison (804 Questions)'
233	    columns:
234	    - Method
235	    - Acc
236	    - Gap_vs_SICA_pp
237	    - Tiebreak_Mechanism
238	    rows:
239	    - - SICA
240	      - 71.3
241	      - —
242	      - MaxSAT weighted constraints
243	    - - SC-random
244	      - 68.1
245	      - -3.2
246	      - Uniform random on ties
247	    - - SC-alphabetical
248	      - 67.5
249	      - -3.8
250	      - Alphabetical first on ties
251	    - - SC-first-seen
252	      - 67.0
253	      - -4.3
254	      - First generated answer on ties
255	  figures_description:
256	  - 'Fig 5: Tiebreak accuracy comparison bar chart, 仅在 tie 题子集上展示四种方法的准确率。SICA 76%
257	    vs random 50% vs alphabetical 55% vs first-seen 43%。'
258	  analysis: 'SICA 对 SC-random（最公平 baseline）仍有 3.2pp 优势，说明增益不是 "刚好比一个差的 tiebreak 规则好"，
259	    而是 MaxSAT 约束确实编码了有用的推理信息。First-seen 最差（67.0%）因为第一条 trace 往往是 greedy-like 的，遇到难题时更可能犯错。Alphabetical
260	    的 60% 有偶然成分（某些答案碰巧排序靠前且正确）。
261	
262	    '
263	- name: sica_7b_scaling
264	  plan_id: exp-004
265	  description: Run SICA with Qwen2.5-7B-Instruct on same 60 questions
266	  expected_results:
267	    sica_accuracy: 0.633
268	    sc_accuracy: 0.567
269	    sica_sc_gap_pp: 6.7
270	    c0_multi_candidate_rate: 0.683
271	    tie_question_fraction: 0.15
272	    tiebreak_win_rate: 0.78
273	    folio_sica: 0.7
274	    folio_sc: 0.6
275	    folio_gap_pp: 10.0
276	    proofwriter_sica: 0.6
277	    proofwriter_sc: 0.55
278	    proofwriter_gap_pp: 5.0
279	    bootstrap_p: 0.087
280	    total_constraints_raw: ~4800
281	    constraint_quality_vs_14b: lower — more parse failures, ~15% extraction failure
282	      rate
283	    gpu_hours: ~1.5
284	  result_rationale: '7B 模型比 14B 弱，两个关键效应： (1) SC baseline 更低（56.7% vs 70.0%），因为 7B
285	    的推理能力更弱； (2) C0 更高（68.3% vs 53.3%），因为 7B 的 trace 多样性更大—— 弱模型对同一问题产生不同推理路径的概率更高，表现为更多多候选答案和更多
286	    ties。 更高的 C0 + 更多 ties → SICA 有更大操作空间 → gap 扩大至 6.7pp。 但约束提取质量下降（7B 的 FOL 翻译更多语法错误），部分抵消了
287	    diversity 带来的优势。 净效应：gap 翻倍（6.7 vs 3.3），但 absolute accuracy 下降。 这完美支撑 C2（operating
288	    regime）和 C3（C0 as predictor）： C0 从 14B 的 53% 升至 7B 的 68%，gap 从 3.3pp 升至 6.7pp，单调正相关。
289	    Bootstrap p=0.087 在 60 题上不显著（预期内，n 太小），但方向一致。
290	
291	    '
292	  tables:
293	  - name: 'Table 5: 7B vs 14B Comparison (60 Questions)'
294	    columns:
295	    - Model
296	    - SC_Acc
297	    - SICA_Acc
298	    - Gap_pp
299	    - C0
300	    - Tie_Frac
301	    rows:
302	    - - Qwen2.5-7B-Instruct
303	      - 56.7
304	      - 63.3
305	      - 6.7
306	      - 0.683
307	      - 0.15
308	    - - Qwen2.5-14B-Instruct
309	      - 70.0
310	      - 73.3
311	      - 3.3
312	      - 0.533
313	      - 0.117
314	  figures_description:
315	  - 'Fig 6: C0 vs SICA-SC gap scatter plot (初步两点 + QwQ 零点)。7B 在右上角，14B 在中间，QwQ 在原点附近。'
316	  analysis: '7B 数据点完美落在 C0-gap 正相关线上。结合 QwQ 的 (C0=3.6%, gap=0pp) 数据点， 三点已经初步支撑 C3
317	    claim。等 72B 数据补上后四点拟合将更有说服力。 一个有趣的 insight：7B 的 SICA gap 更大，但 absolute accuracy
318	    更低。 这意味着 SICA 不是 "让弱模型变强" 的银弹，而是 "在模型本身的能力范围内最大化共识质量"。
319	
320	    '
321	- name: qwq_32b_operating_regime
322	  plan_id: exp-005
323	  description: QwQ-32B negative results formatted for Operating Regime Analysis section
324	  expected_results:
325	    aime_c0: 0.0
326	    aime_sica_sc_gap: 0.0
327	    folio_c0: 0.0
328	    folio_sica_sc_gap: 0.0
329	    proofwriter_c0: 0.1875
330	    proofwriter_sica_sc_gap: 0.0
331	    combined_c0: 0.036
332	    combined_sica_sc_gap: 0.0
333	    n_total: 48
334	    trace_entropy_qwq: 0.12
335	    trace_entropy_14b: 1.83
336	    trace_entropy_7b: 2.41
337	  result_rationale: 'QwQ-32B 是 reasoning model，其 CoT 过程内部已经执行了隐式的 "多路径搜索 + 自我验证"，
338	    导致不同 temperature 采样出的 traces 几乎收敛到同一答案（C0≈0%）。 这不是因为 QwQ 更 "聪明"（它确实更聪明，但关键不在准确率），
339	    而是因为 reasoning model 的训练目标（extended thinking + verification）压缩了输出分布。 SICA 需要 trace
340	    diversity 来工作——当所有 K 条 traces 给出相同答案， MaxSAT 无论怎么加权都只能选同一个答案。SICA 在数学上退化为 SC。
341	    Trace entropy 量化了这一点：QwQ 的 0.12 bits 对比 14B 的 1.83 bits（15x 差距）。 ProofWriter 上
342	    QwQ 有 18.75% C0，但 n=16 太小且增益为零—— 因为 C0=18.75% 中的多候选题上 QwQ 的 "错误" trace 其约束一致性也很高（reasoning
343	    model 连犯错都很自洽）， MaxSAT 无法区分正确和错误的一致性约束。
344	
345	    '
346	  tables:
347	  - name: 'Table 6: Operating Regime — Reasoning vs Instruction Models'
348	    columns:
349	    - Model
350	    - Type
351	    - C0
352	    - SICA-SC_Gap
353	    - Trace_Entropy
354	    - N
355	    rows:
356	    - - QwQ-32B
357	      - Reasoning
358	      - 3.6%
359	      - 0.0pp
360	      - 0.12
361	      - 48
362	    - - Qwen2.5-14B-Instruct
363	      - Instruction
364	      - 53.3%
365	      - +3.3pp
366	      - 1.83
367	      - 60
368	    - - Qwen2.5-7B-Instruct
369	      - Instruction
370	      - 68.3%
371	      - +6.7pp
372	      - 2.41
373	      - 60
374	  figures_description:
375	  - 'Fig 7: Operating regime diagram. X 轴 = C0, Y 轴 = SICA-SC gap. 左侧 ''degenerate
376	    zone'' (C0<10%), 右侧 ''effective zone'' (C0>20%). QwQ 在左，两个 instruction models
377	    在右。'
378	  analysis: '这是论文的核心 intellectual contribution。不说 "SICA 不如 reasoning model"， 而是说 "SICA
379	    和 reasoning model 解决不同的问题"：reasoning model 通过内部验证压缩了输出分布， 不需要外部共识机制；instruction
380	    model 输出多样性高，需要也能够从外部共识中获益。 这是一个 model property，不是 task property——同一个 task (FOLIO)
381	    在两种模型上表现完全不同。
382	
383	    '
384	- name: c0_diagnostic_validation
385	  plan_id: exp-006
386	  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0
387	    as predictor.
388	  expected_results:
389	    data_points:
390	    - model: QwQ-32B
391	      K: 12
392	      C0: 0.036
393	      gap_pp: 0.0
394	    - model: Qwen2.5-72B-AWQ
395	      K: 12
396	      C0: 0.3
397	      gap_pp: 1.7
398	    - model: Qwen2.5-14B-Instruct
399	      K: 6
400	      C0: 0.483
401	      gap_pp: 1.7
402	    - model: Qwen2.5-14B-Instruct
403	      K: 8
404	      C0: 0.517
405	      gap_pp: 3.3
406	    - model: Qwen2.5-14B-Instruct
407	      K: 12
408	      C0: 0.533
409	      gap_pp: 3.3
410	    - model: Qwen2.5-14B-Instruct
411	      K: 16
412	      C0: 0.55
413	      gap_pp: 5.0
414	    - model: Qwen2.5-14B-Instruct
415	      K: 20
416	      C0: 0.567
417	      gap_pp: 5.0
418	    - model: Qwen2.5-7B-Instruct
419	      K: 12
420	      C0: 0.683
421	      gap_pp: 6.7
422	    pearson_r: 0.94
423	    spearman_rho: 0.93
424	    linear_fit_slope: 10.2
425	    linear_fit_intercept: -2.1
426	    linear_fit_r2: 0.88
427	    c0_threshold_for_positive_gap: 0.21
428	  result_rationale: 'C0 与 gap 的正相关来自因果链：C0 高 → 更多题存在多候选 → 更多 tie → SICA 有操作空间 → gap
429	    大。 这不是 confound（比如 "弱模型 C0 高且 gap 大是因为 baseline 低"）， 因为 K ablation 在同一模型上也展现了
430	    C0-gap 正相关（K 增大 → C0 微增 → gap 增大）， 排除了模型能力这个 confound。 8 个数据点（4 models × varying
431	    K）的 Pearson r=0.94，线性拟合 R²=0.88。 斜率 10.2 表示 C0 每增加 10pp，SICA-SC gap 增加约 1.0pp。
432	    截距 -2.1 表示 C0 需要超过 ~21% 才能期望正增益——这与 QwQ 的 C0=3.6%→gap=0 和 D016 precheck 的 C0≥20%
433	    作为 go/no-go 门槛一致。 Spearman ρ=0.93 确认单调性（非线性关系也 OK）。
434	
435	    '
436	  tables:
437	  - name: 'Table 7: C0 as Predictor — Linear Regression'
438	    columns:
439	    - Metric
440	    - Value
441	    rows:
442	    - - Pearson_r
443	      - 0.94
444	    - - Spearman_ρ
445	      - 0.93
446	    - - Slope
447	      - 10.2 pp gap per unit C0
448	    - - Intercept
449	      - -2.1pp
450	    - - R²
451	      - 0.88
452	    - - C0_threshold
453	      - 0.21 (gap > 0)
454	  figures_description:
455	  - 'Fig 8 (论文核心图): C0 vs SICA-SC gap 散点图。X 轴 C0 [0, 0.7], Y 轴 gap [-1, 8]pp。4 种 model
456	    用不同 marker，同 model 不同 K 用颜色深浅。线性回归线 + 95% CI band。阴影区域标注 ''Degenerate Zone'' (C0<0.21)
457	    和 ''Effective Zone''。'
458	  - 'Fig 9: C0 的计算不需要运行 MaxSAT（只需要 traces），所以是 zero-cost predictor。示意图展示 practitioner
459	    workflow: generate K traces → compute C0 → if C0>20% then run SICA, else use SC。'
460	  analysis: 'C3 claim 的核心证据。Pearson r=0.94 和 R²=0.88 在 8 个数据点上非常强。 reviewer 可能的攻击：(1)
461	    只有 8 个点——回应是这是 4 个不同模型 + K 变化，覆盖了 C0 从 3.6% 到 68% 的全范围； (2) 因果方向不确定——回应是 C0 是
462	    SICA 的输入（先于 MaxSAT 计算），因果方向明确； (3) 更多模型可能打破单调性——acknowledge as limitation，但当前
463	    4 models 跨越了 3B-72B 规模和 reasoning/instruction 两种类型。
464	
465	    '
466	- name: sica_72b_awq
467	  plan_id: exp-007
468	  description: Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions
469	  expected_results:
470	    sica_accuracy: 0.8
471	    sc_accuracy: 0.783
472	    sica_sc_gap_pp: 1.7
473	    c0_multi_candidate_rate: 0.3
474	    tie_question_fraction: 0.067
475	    tiebreak_win_rate: 0.75
476	    folio_sica: 0.867
477	    folio_sc: 0.833
478	    folio_gap_pp: 3.3
479	    proofwriter_sica: 0.767
480	    proofwriter_sc: 0.767
481	    proofwriter_gap_pp: 0.0
482	    bootstrap_p: 0.34
483	    constraint_quality: higher than 14B — fewer parse errors, more precise FOL
484	    gpu_hours: ~3.5
485	    gpu_mem_gib: ~52
486	  result_rationale: '72B 是 "强 instruction model"——比 14B 聪明但仍是 instruction 架构（非 reasoning
487	    model）， 所以 C0 不会像 QwQ 那样降到零，但会显著低于 14B。 预期 C0=30%：72B 的推理一致性更高（更多题所有 traces 给出相同答案），
488	    但遇到真正难题时仍会产生 divergence。 SC baseline 高（78.3%），已接近 FOLIO/PW 的天花板，留给 SICA 的空间很小。
489	    Tie 频率低（6.7%），只有 ~4 题出现 tie，其中 SICA 赢 3 题 → gap 1.7pp。 ProofWriter 上 72B 的 accuracy
490	    已经够高，tie 可能 0-1 题 → gap 0pp。 这个结果完美支撑 operating regime 叙事：72B 在 QwQ（C0→0, gap→0）和
491	    14B（C0=53%, gap=3.3pp）之间， 形成 7B→14B→72B→QwQ 的 C0 递减、gap 递减梯度。 Bootstrap p=0.34
492	    在 60 题上不显著——预期内，因为只有 4 题 tie 无法产生统计 power。 这正是为什么 exp-007 是 P1 而非 P0：它的价值在于 C0-gap
493	    散点图的第四个点， 不在于独立的显著性检验。
494	
495	    '
496	  tables:
497	  - name: 'Table 8: Model Scaling — 7B / 14B / 72B / QwQ (60 Questions)'
498	    columns:
499	    - Model
500	    - Size
501	    - Type
502	    - SC_Acc
503	    - SICA_Acc
504	    - Gap_pp
505	    - C0
506	    rows:
507	    - - Qwen2.5-7B-Instruct
508	      - 7B
509	      - Instruction
510	      - 56.7
511	      - 63.3
512	      - 6.7
513	      - 0.683
514	    - - Qwen2.5-14B-Instruct
515	      - 14B
516	      - Instruction
517	      - 70.0
518	      - 73.3
519	      - 3.3
520	      - 0.533
521	    - - Qwen2.5-72B-AWQ
522	      - 72B
523	      - Instruction
524	      - 78.3
525	      - 80.0
526	      - 1.7
527	      - 0.3
528	    - - QwQ-32B
529	      - 32B
530	      - Reasoning
531	      - —
532	      - —
533	      - 0.0
534	      - 0.036
535	  figures_description:
536	  - 'Fig 10: 四模型的 C0 和 gap 条形图并列。清晰展示 instruction model 的 size↑ → C0↓ → gap↓ 梯度，以及
537	    reasoning model 的断崖式 C0 下降。'
538	  analysis: '72B 数据确认了 operating regime 的 scaling dimension：即使在同一架构系列内， 模型规模增大也会降低
539	    trace diversity（更强的模型更自信、更一致）， 从而缩小 SICA 的操作空间。但关键区分是 "缩小" vs "消失"： 72B 的 C0=30%
540	    仍远高于 QwQ 的 3.6%，说明 instruction→reasoning 的跃迁才是决定性的， 而非单纯的规模增大。这为论文提供了更精细的 insight。
541	
542	    '
543	- name: constraint_quality_case_studies
544	  plan_id: exp-008
545	  description: Qualitative analysis of extracted constraints on 5-10 representative
546	    questions
547	  expected_results:
548	    cases_analyzed: 8
549	    categories:
550	      correct_and_helpful: 5
551	      correct_but_redundant: 1
552	      incorrect_but_excluded: 1
553	      incorrect_and_harmful: 1
554	    example_folio_tie_win:
555	      question_summary: FOLIO question about organizational membership and property
556	        inheritance
557	      k12_vote_split: '6 True : 6 False'
558	      sica_answer: True (correct)
559	      sc_alphabetical: False (wrong)
560	      key_constraint: ∀x(Member(x,Org) → HasProperty(x,P)), weight=0.83
561	      why_sica_wins: 6 True-traces 提取的约束互相一致（满足率 92%），6 False-traces 的约束自相矛盾（满足率 61%），MaxSAT
562	        正确偏向 True。
563	    example_proofwriter_miss:
564	      question_summary: PW D5 深度链推理，5步推导
565	      sica_answer: False (wrong)
566	      correct_answer: 'True'
567	      why_sica_fails: 中间步骤的 FOL 翻译错误（否定词遗漏），导致约束指向错误方向。7/12 traces 含相同翻译错误。
568	    extraction_failure_rate: 0.02
569	    avg_constraints_per_trace: 13.2
570	    avg_unique_constraints_per_question: 28.7
571	  result_rationale: 'Case study 的目的是让 reviewer 看到 SICA 不是黑盒——约束有语义可解释性。 在 best tier
572	    下，多数 case 展示 SICA 的约束确实编码了推理中的逻辑关系， MaxSAT 的加权机制合理地偏向了一致性更高的答案。 选择 8 个 case：5
573	    个 SICA 正确发挥、1 个冗余但无害、1 个错误约束被 exclusion 机制过滤、 1 个 SICA 犯错的反例（诚实展示局限性）。 FOLIO 的
574	    tie-win case 最有说服力：展示 MaxSAT 如何利用约束一致性区分两组 traces。 ProofWriter 的 failure case
575	    揭示了约束提取的瓶颈（FOL 翻译质量）， 为 future work（更好的 FOL extractor）提供了明确方向。
576	
577	    '
578	  tables: []
579	  figures_description:
580	  - 'Fig 11: 一个 FOLIO tie-win case 的完整可视化：12 条 traces 的投票分布、提取的约束集合、MaxSAT 权重、最终判决。用颜色编码正确/错误
581	    traces 和满足/违反的约束。'
582	  - 'Fig 12: 约束质量分布直方图：extraction rate、parse success rate、semantic correctness rate（人工标注
583	    50 条约束）。'
584	  analysis: 'Case studies 将 SICA 从 "accuracy number goes up" 提升为 "we understand WHY
585	    it goes up"。 5/8 cases 展示了约束的语义意义，1/8 的 failure case 防止 reviewer 说 "cherry-picked"。
586	    这是 qualitative contribution，在 EMNLP 评审中有加分作用。
587	
588	    '
589	- name: overhead_analysis
590	  plan_id: exp-009
591	  description: 'Wall-time breakdown per question: generation, constraint extraction,
592	    MaxSAT solving'
593	  expected_results:
594	    avg_total_time_per_question_s: 58.3
595	    avg_generation_time_s: 42.1
596	    avg_extraction_time_s: 14.8
597	    avg_maxsat_time_s: 1.4
598	    generation_fraction: 0.722
599	    extraction_fraction: 0.254
600	    maxsat_fraction: 0.024
601	    overhead_vs_sc_multiplier: 1.39
602	    overhead_vs_sc_description: SC 只需 generation (42.1s)，SICA 额外需要 extraction+MaxSAT
603	      (16.2s)，增加 39% wall time
604	    marginal_cost_per_pp_gain: 4.3s per 1pp accuracy gain
605	    maxsat_z3_avg_time_ms: 47
606	    maxsat_z3_max_time_ms: 312
607	    constraint_extraction_method: LLM-based (same model, separate prompt)
608	    extraction_tokens_per_question: ~2800
609	  result_rationale: 'Overhead 分析对 reviewer concern "is it worth it" 至关重要。 Generation
610	    占 72% wall time——这与 SC 相同（K=12 条 traces），不是 SICA 的 overhead。 SICA 的真正 overhead
611	    是 constraint extraction (25%) + MaxSAT solving (2.4%)。 Extraction 用同模型做 FOL 翻译，每条
612	    trace ~2800 tokens，12 traces 串行处理需要 ~14.8s。 MaxSAT (Z3) 平均 47ms 每题——trivially
613	    fast，因为约束数通常 <100（Z3 处理数千约束毫无压力）。 总 overhead multiplier 1.39x 意味着每题多花 39% 时间换取
614	    3.8pp accuracy gain—— 这在多数应用场景下是 acceptable 的 trade-off。 进一步：extraction 可以并行化（12
615	    traces 同时提取），理论上压缩到 ~3s， 使 multiplier 降至 1.10x。但当前实现是串行的，论文报告实际数字更诚实。
616	
617	    '
618	  tables:
619	  - name: 'Table 9: Overhead Analysis (Qwen2.5-14B-Instruct, K=12, 804 Questions)'
620	    columns:
621	    - Stage
622	    - Avg_Time_s
623	    - Fraction
624	    - Parallelizable
625	    rows:
626	    - - Trace_Generation
627	      - 42.1
628	      - 72.2%
629	      - Yes (vLLM batched)
630	    - - Constraint_Extraction
631	      - 14.8
632	      - 25.4%
633	      - Yes (per-trace independent)
634	    - - MaxSAT_Solving
635	      - 1.4
636	      - 2.4%
637	      - No (single Z3 call)
638	    - - Total
639	      - 58.3
640	      - 100%
641	      - ''
642	    - - SC_Equivalent
643	      - 42.1
644	      - —
645	      - ''
646	    - - SICA_Overhead
647	      - 16.2
648	      - +38.5%
649	      - ''
650	  figures_description:
651	  - 'Fig 13: Stacked bar chart 展示 per-question wall time 分解。SC bar 只有 generation，SICA
652	    bar 有 generation + extraction + MaxSAT。MaxSAT 几乎不可见（太小了）。'
653	  analysis: Key talking point：SICA 的 "重" 在约束提取（LLM 调用），不在 MaxSAT 求解。 这意味着 (1) overhead
654	    随 LLM inference 成本线性下降（模型越快，overhead 越低）， (2) MaxSAT 本身不是瓶颈（可以扩展到更多约束）， (3) 如果用
655	    fine-tuned 小模型做 extraction 可以进一步降低 overhead（future work）。 39% overhead 换 3.8pp
656	    gain 的 cost-effectiveness 优于大多数 ensembling 方法 （如 majority voting over 2K traces
657	    需要 100% overhead 且 gain 通常 <2pp）。
658	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b86cba79-1e28-4082-acae-bf01294ae23b",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "f93f5926-6b65-4e7b-9e3f-c2234b7d12f7",
  "sourceToolAssistantUUID": "b86cba79-1e28-4082-acae-bf01294ae23b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-16T06:20:05.384Z_

Now let me read the other paper versions and the pipeline code to understand the implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f93f5926-6b65-4e7b-9e3f-c2234b7d12f7",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mERFkjeVW2wX1b1XSH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3599a4b6-7aa2-406e-8c09-e42b400889bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SaHTegLMvRwdC6DQodpzEo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25809,
      "cache_read_input_tokens": 28122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25809,
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

_source line 27 · 2026-05-16T06:20:06.932Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HxWZN8B3rcjRF3pKYkDiCc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3599a4b6-7aa2-406e-8c09-e42b400889bc",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mERFkjeVW2wX1b1XSH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "683dd69b-d701-477e-ad1e-d4f2bbd3fda6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SaHTegLMvRwdC6DQodpzEo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25809,
      "cache_read_input_tokens": 28122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25809,
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

_source line 28 · 2026-05-16T06:20:06.940Z_

<details><summary>↩ Tool result · `toolu_01HxWZN8B3rcjRF3pKYkDiCc`</summary>

```text
1	"""
2	SICA end-to-end pipeline: trace generation -> constraint extraction -> Z3 dedup -> MAX-SAT -> scoring -> answer selection.
3	Input: problem dict with "problem" and "answer" fields
4	Output: result dict with answer, score, constraint stats, maxsat stats
5	Dependencies: trace_generator, constraint_extractor, z3_maxsat, scorer
6	"""
7	from __future__ import annotations
8	
9	import logging
10	import time
11	from collections import Counter
12	
13	from .trace_generator import TraceGenerator
14	from .constraint_extractor import ConstraintExtractor
15	from .z3_maxsat import ConstraintDeduplicator, MaxSATSolver
16	from .scorer import InvariantScorer
17	
18	logger = logging.getLogger(__name__)
19	
20	
21	class SICAPipeline:
22	    def __init__(
23	        self,
24	        trace_generator: TraceGenerator,
25	        constraint_extractor: ConstraintExtractor,
26	        k: int = 12,
27	        maxsat_timeout_ms: int = 10000,
28	    ):
29	        self.trace_generator = trace_generator
30	        self.constraint_extractor = constraint_extractor
31	        self.k = k
32	        self.deduplicator = ConstraintDeduplicator()
33	        self.solver = MaxSATSolver()
34	        self.scorer = InvariantScorer()
35	        self.maxsat_timeout_ms = maxsat_timeout_ms
36	
37	    def run_single(self, problem: dict) -> dict:
38	        """Run full SICA pipeline on a single problem."""
39	        t_start = time.perf_counter()
40	
41	        # 1. Generate K traces
42	        t0 = time.perf_counter()
43	        traces = self.trace_generator.generate(problem["problem"], k=self.k)
44	        trace_time = time.perf_counter() - t0
45	
46	        # 2. Extract constraints from each trace (batch for concurrency)
47	        t0 = time.perf_counter()
48	        all_constraints = self.constraint_extractor.extract_batch(
49	            [t["trace"] for t in traces]
50	        )
51	        extract_time = time.perf_counter() - t0
52	
53	        total_constraints = sum(len(c) for c in all_constraints)
54	        non_empty = sum(1 for c in all_constraints if c)
55	
56	        # 3. Deduplicate via z3 equivalence
57	        t0 = time.perf_counter()
58	        unique_constraints = self.deduplicator.deduplicate(all_constraints)
59	        dedup_time = time.perf_counter() - t0
60	
61	        # 4. MAX-SAT solve
62	        t0 = time.perf_counter()
63	        maxsat_result = self.solver.solve(unique_constraints, timeout_ms=self.maxsat_timeout_ms)
64	        maxsat_time = time.perf_counter() - t0
65	
66	        # 5. Score candidates
67	        candidates = list(set(t["answer"] for t in traces if t["answer"]))
68	        answer_counts = Counter(t["answer"] for t in traces if t["answer"])
69	        scores = self.scorer.score(maxsat_result, traces, candidates)
70	        selected = self.scorer.select_answer(scores, answer_counts)
71	
72	        total_time = time.perf_counter() - t_start
73	
74	        return {
75	            "answer": selected,
76	            "scores": scores,
77	            "answer_counts": dict(answer_counts),
78	            "traces": traces,
79	            "constraints_stats": {
80	                "total_extracted": total_constraints,
81	                "traces_with_constraints": non_empty,
82	                "unique_after_dedup": len(unique_constraints),
83	            },
84	            "maxsat_stats": {
85	                "satisfied": len(maxsat_result.satisfied),
86	                "excluded": len(maxsat_result.excluded),
87	                "total_weight": maxsat_result.total_weight,
88	                "solve_time_ms": maxsat_result.solve_time_ms,
89	            },
90	            "timing": {
91	                "trace_gen_s": round(trace_time, 3),
92	                "extraction_s": round(extract_time, 3),
93	                "dedup_s": round(dedup_time, 3),
94	                "maxsat_s": round(maxsat_time, 3),
95	                "total_s": round(total_time, 3),
96	            },
97	        }
98	
99	    def run_batch(self, problems: list[dict]) -> list[dict]:
100	        """Run pipeline on a batch of problems."""
101	        results = []
102	        for i, p in enumerate(problems):
103	            logger.info("Processing problem %d/%d", i + 1, len(problems))
104	            result = self.run_single(p)
105	            result["problem_idx"] = i
106	            results.append(result)
107	        return results
108	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "683dd69b-d701-477e-ad1e-d4f2bbd3fda6",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "03611051-51f3-4da5-9677-358b643f255c",
  "sourceToolAssistantUUID": "683dd69b-d701-477e-ad1e-d4f2bbd3fda6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T06:20:07.461Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AhBNLnrPqhzF2C71d4zShM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/constraint_extractor.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03611051-51f3-4da5-9677-358b643f255c",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mERFkjeVW2wX1b1XSH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9270df56-4734-4d0e-9b82-b51d5b68b770",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SaHTegLMvRwdC6DQodpzEo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25809,
      "cache_read_input_tokens": 28122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25809,
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

_source line 30 · 2026-05-16T06:20:07.485Z_

<details><summary>↩ Tool result · `toolu_01AhBNLnrPqhzF2C71d4zShM`</summary>

````text
1	"""
2	Constraint extractor: extract structured math constraints from LLM reasoning traces.
3	Input: reasoning trace string
4	Output: list of constraint dicts with type, expression, z3_formula, source_step
5	Dependencies: json, re, openai (optional)
6	"""
7	from __future__ import annotations
8	
9	import asyncio
10	import json
11	import logging
12	import re
13	from abc import ABC, abstractmethod
14	from dataclasses import dataclass, field
15	
16	logger = logging.getLogger(__name__)
17	
18	EXTRACTION_PROMPT = '''You are a mathematical constraint extractor. Given a step-by-step reasoning trace for a math problem, extract all mathematical constraints (equations, inequalities, predicates) that appear in the reasoning.
19	
20	**Variable naming rules:**
21	- Use standard variable names: x, y, z, a, b, c, n, m, k
22	- If the problem names specific quantities (e.g., "length", "width"), use descriptive short names (e.g., l, w)
23	- Be consistent: the same quantity must use the same variable name across all constraints
24	- Use the SAME variable names that appear in the reasoning trace
25	
26	**Output format:** Return a JSON object with this exact structure:
27	```json
28	{{
29	  "constraints": [
30	    {{
31	      "type": "equation|inequality|predicate",
32	      "expression": "human-readable expression, e.g. x + y == 14",
33	      "z3_formula": "Z3-compatible Python expression, e.g. x + y == 14",
34	      "source_step": 3
35	    }}
36	  ],
37	  "answer": "the final numerical answer from this trace",
38	  "variables": ["x", "y"]
39	}}
40	```
41	
42	**Constraint types:**
43	- equation: equality (==), e.g. "x + y == 14"
44	- inequality: <, >, <=, >=, e.g. "x > 0"
45	- predicate: logical assertion, e.g. "x % 2 == 0" (x is even)
46	
47	**Z3 formula rules:**
48	- Use Python syntax: ==, !=, <, >, <=, >=, +, -, *, /, **
49	- Division: use / (Z3 Real division)
50	- Integer modulo: use %
51	- All variables are Real by default
52	
53	**Example 1:**
54	Trace: "Let the two numbers be x and y. We know x + y = 14 and x * y = 48. From x + y = 14, y = 14 - x. Substituting: x(14-x) = 48, 14x - x^2 = 48, x^2 - 14x + 48 = 0. Factoring: (x-6)(x-8) = 0. So x = 6 or x = 8. The answer is \\\\boxed{{6}}."
55	
56	Output:
57	```json
58	{{
59	  "constraints": [
60	    {{"type": "equation", "expression": "x + y == 14", "z3_formula": "x + y == 14", "source_step": 1}},
61	    {{"type": "equation", "expression": "x * y == 48", "z3_formula": "x * y == 48", "source_step": 1}},
62	    {{"type": "equation", "expression": "y == 14 - x", "z3_formula": "y == 14 - x", "source_step": 2}},
63	    {{"type": "equation", "expression": "x**2 - 14*x + 48 == 0", "z3_formula": "x**2 - 14*x + 48 == 0", "source_step": 3}}
64	  ],
65	  "answer": "6",
66	  "variables": ["x", "y"]
67	}}
68	```
69	
70	**Example 2:**
71	Trace: "A rectangle has perimeter 30 and area 50. Let length = l, width = w. Then 2(l+w) = 30, so l+w = 15. Also l*w = 50. We need l - w. (l-w)^2 = (l+w)^2 - 4lw = 225 - 200 = 25. So l-w = 5. The answer is \\\\boxed{{5}}."
72	
73	Output:
74	```json
75	{{
76	  "constraints": [
77	    {{"type": "equation", "expression": "2*(l + w) == 30", "z3_formula": "2*(l + w) == 30", "source_step": 1}},
78	    {{"type": "equation", "expression": "l + w == 15", "z3_formula": "l + w == 15", "source_step": 2}},
79	    {{"type": "equation", "expression": "l * w == 50", "z3_formula": "l * w == 50", "source_step": 2}},
80	    {{"type": "equation", "expression": "(l - w)**2 == 25", "z3_formula": "(l - w)**2 == 25", "source_step": 3}}
81	  ],
82	  "answer": "5",
83	  "variables": ["l", "w"]
84	}}
85	```
86	
87	Now extract constraints from this trace:
88	
89	{trace}
90	
91	Return ONLY the JSON object, no other text.'''
92	
93	
94	class LLMBackend(ABC):
95	    """LLM 调用抽象基类"""
96	    @abstractmethod
97	    def call(self, prompt: str) -> str:
98	        ...
99	
100	
101	class VLLMBackend(LLMBackend):
102	    """通过 OpenAI-compatible API 调用本地 vLLM"""
103	
104	    def __init__(self, base_url: str = "http://localhost:8000/v1", model: str | None = None):
105	        from openai import OpenAI, AsyncOpenAI
106	        self.client = OpenAI(base_url=base_url, api_key="[REDACTED]")
107	        self.async_client = AsyncOpenAI(base_url=base_url, api_key="[REDACTED]")
108	        if model is None:
109	            models = self.client.models.list()
110	            self.model = models.data[0].id
111	        else:
112	            self.model = model
113	
114	    def call(self, prompt: str) -> str:
115	        response = self.client.chat.completions.create(
116	            model=self.model,
117	            messages=[{"role": "user", "content": prompt}],
118	            temperature=0.3,
119	            max_tokens=2048,
120	        )
121	        return response.choices[0].message.content or ""
122	
123	    async def async_call(self, prompt: str) -> str:
124	        response = await self.async_client.chat.completions.create(
125	            model=self.model,
126	            messages=[{"role": "user", "content": prompt}],
127	            temperature=0.3,
128	            max_tokens=2048,
129	        )
130	        return response.choices[0].message.content or ""
131	
132	    def batch_call(self, prompts: list[str]) -> list[str]:
133	        """批量调用，用 asyncio 并发"""
134	        async def _run():
135	            tasks = [self.async_call(p) for p in prompts]
136	            return await asyncio.gather(*tasks)
137	        try:
138	            loop = asyncio.get_running_loop()
139	            import nest_asyncio
140	            nest_asyncio.apply()
141	            return loop.run_until_complete(_run())
142	        except RuntimeError:
143	            return asyncio.run(_run())
144	
145	
146	class MockLLM(LLMBackend):
147	    """Returns pre-set responses for testing."""
148	
149	    def __init__(self, responses: list[str] | None = None):
150	        self._responses = responses or []
151	        self._idx = 0
152	
153	    def call(self, prompt: str) -> str:
154	        if self._responses:
155	            resp = self._responses[self._idx % len(self._responses)]
156	            self._idx += 1
157	            return resp
158	        return json.dumps({"constraints": [
159	            {"type": "equation", "expression": "x - 7", "z3_formula": "x == 7", "source_step": 1},
160	            {"type": "equation", "expression": "x + 5 - 12", "z3_formula": "x + 5 == 12", "source_step": 2},
161	        ], "answer": "7", "variables": ["x"]})
162	
163	
164	class APIBasedLLM(LLMBackend):
165	    """LLM backend using OpenAI-compatible API (e.g. vLLM server)."""
166	
167	    def __init__(self, base_url: str = "http://localhost:8000/v1",
168	                 api_key: [REDACTED] = "EMPTY", model: str | None = None,
169	                 temperature: float = 0.1, max_tokens: int = 2048):
170	        import openai
171	        self.client = openai.OpenAI(base_url=base_url, api_key=[REDACTED]
172	        self.temperature = temperature
173	        self.max_tokens = max_tokens
174	        if model:
175	            self.model = model
176	        else:
177	            models = self.client.models.list()
178	            self.model = models.data[0].id
179	
180	    def call(self, prompt: str) -> str:
181	        resp = self.client.chat.completions.create(
182	            model=self.model,
183	            messages=[{"role": "user", "content": prompt}],
184	            temperature=self.temperature,
185	            max_tokens=self.max_tokens,
186	        )
187	        return resp.choices[0].message.content or ""
188	
189	
190	@dataclass
191	class ExtractionStats:
192	    success: int = 0
193	    fail_json_parse: int = 0
194	    fail_empty: int = 0
195	    fail_invalid_expr: int = 0
196	
197	    @property
198	    def total_fail(self) -> int:
199	        return self.fail_json_parse + self.fail_empty + self.fail_invalid_expr
200	
201	
202	class ConstraintExtractor:
203	    def __init__(self, llm: LLMBackend | None = None):
204	        self.llm = llm or MockLLM()
205	        self.stats = ExtractionStats()
206	
207	    def _build_prompt(self, trace: str) -> str:
208	        return EXTRACTION_PROMPT.format(trace=trace)
209	
210	    def _parse_response(self, raw: str, trace: str) -> list[dict]:
211	        """Parse a raw LLM response into constraint list."""
212	        json_str = raw.strip()
213	        m = re.search(r'```(?:json)?\s*(.*?)```', json_str, re.DOTALL)
214	        if m:
215	            json_str = m.group(1).strip()
216	
217	        try:
218	            data = json.loads(json_str)
219	        except json.JSONDecodeError:
220	            logger.warning("JSON parse failed for trace: %s...", trace[:80])
221	            self.stats.fail_json_parse += 1
222	            return []
223	
224	        constraints = data.get("constraints", [])
225	        if not constraints:
226	            self.stats.fail_empty += 1
227	            return []
228	
229	        valid = []
230	        for c in constraints:
231	            if not all(k in c for k in ("type", "expression", "z3_formula", "source_step")):
232	                continue
233	            if c["type"] not in ("equation", "inequality", "predicate"):
234	                continue
235	            valid.append(c)
236	
237	        if not valid:
238	            self.stats.fail_invalid_expr += 1
239	            return []
240	
241	        self.stats.success += 1
242	        return valid
243	
244	    def extract(self, trace: str) -> list[dict]:
245	        """Extract structured constraints from a reasoning trace."""
246	        prompt = self._build_prompt(trace)
247	        raw = self.llm.call(prompt)
248	        return self._parse_response(raw, trace)
249	
250	    def extract_batch(self, traces: list[str]) -> list[list[dict]]:
251	        """批量提取约束，如果 LLM 后端支持 batch_call 则并发执行"""
252	        if hasattr(self.llm, 'batch_call'):
253	            prompts = [self._build_prompt(t) for t in traces]
254	            raw_results = self.llm.batch_call(prompts)
255	            return [self._parse_response(raw, trace)
256	                    for raw, trace in zip(raw_results, traces)]
257	        return [self.extract(t) for t in traces]
258	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9270df56-4734-4d0e-9b82-b51d5b68b770",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "8c1b28ca-5262-47de-bbde-1ac49d79af76",
  "sourceToolAssistantUUID": "9270df56-4734-4d0e-9b82-b51d5b68b770",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T06:20:08.009Z_

<details open><summary>🔧 Tool call — Read · `toolu_017pgSmv4G6YPXzBAE8Q9xkn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/z3_maxsat_patched.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c1b28ca-5262-47de-bbde-1ac49d79af76",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mERFkjeVW2wX1b1XSH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "549a831c-8774-4650-9bda-c27526ea544e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SaHTegLMvRwdC6DQodpzEo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25809,
      "cache_read_input_tokens": 28122,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25809
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 28122,
          "cache_creation_input_tokens": 25809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25809,
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

_source line 32 · 2026-05-16T06:20:08.028Z_

<details><summary>↩ Tool result · `toolu_017pgSmv4G6YPXzBAE8Q9xkn`</summary>

```text
1	"""
2	Z3-based weighted partial MAX-SAT solver for constraint consensus.
3	Input: multi-trace constraint lists (list of list of dicts)
4	Output: optimal satisfiable constraint subset, excluded contradictions, per-answer scores
5	Dependencies: z3-solver
6	"""
7	from __future__ import annotations
8	
9	import logging
10	import re
11	import time
12	from dataclasses import dataclass, field
13	
14	import z3
15	
16	logger = logging.getLogger(__name__)
17	
18	_BOOL_INDICATORS = re.compile(r'\bImplies\s*\(|==\s*True|==\s*False|\bNot\s*\(|\bAnd\s*\(|\bOr\s*\(')
19	
20	
21	def _is_boolean_formula(formula_str: str) -> bool:
22	    """Detect whether a formula uses boolean logic (vs arithmetic)."""
23	    return bool(_BOOL_INDICATORS.search(formula_str))
24	
25	
26	def _preprocess_formula(formula_str: str) -> str:
27	    """Normalize common LLM output patterns before z3 eval."""
28	    s = formula_str.strip()
29	    # Sum -> sum
30	    s = re.sub(r'\bSum\b', 'sum', s)
31	    # sum([x1, x2, ...]) -> sum(x1, x2, ...)
32	    s = re.sub(r'\bsum\(\[([^\[\]]*)\]\)', r'sum(\1)', s)
33	    # pow(a, b) -> (a)**(b)
34	    s = re.sub(r'\bpow\(([^,]+),\s*([^)]+)\)', r'(\1)**(\2)', s)
35	    # Abs -> abs
36	    s = re.sub(r'\bAbs\b', 'abs', s)
37	    return s
38	
39	
40	def parse_z3_formula(formula_str: str, var_type: str = "auto") -> z3.ExprRef | None:
41	    """Safely parse a string into a z3 expression.
42	
43	    Supports:
44	      - Arithmetic: +, -, *, /, **, ==, !=, <, >, <=, >= (Real variables)
45	      - Boolean: Implies, And, Or, Not, == True/False (Bool variables)
46	      - Functions: sum, max, min, abs (z3-compatible wrappers)
47	    Auto-declares unknown variables as z3.Real or z3.Bool based on context.
48	    Returns None on parse failure or non-boolean result.
49	    """
50	    if not formula_str or not formula_str.strip():
51	        return None
52	
53	    formula_str = _preprocess_formula(formula_str)
54	
55	    use_bool = (var_type == "bool") or (var_type == "auto" and _is_boolean_formula(formula_str))
56	
57	    tokens = set(re.findall(r'\b([a-zA-Z_]\w*)\b', formula_str))
58	    reserved = {
59	        'True', 'False', 'And', 'Or', 'Not', 'Implies', 'If',
60	        'abs', 'Abs', 'Bool', 'Real', 'Int',
61	        'sum', 'Sum', 'max', 'min', 'len', 'int', 'Mod', 'pow',
62	    }
63	    var_names = tokens - reserved
64	
65	    ns: dict = {}
66	    for name in var_names:
67	        ns[name] = z3.Bool(name) if use_bool else z3.Real(name)
68	
69	    ns['And'] = z3.And
70	    ns['Or'] = z3.Or
71	    ns['Not'] = z3.Not
72	    ns['Implies'] = z3.Implies
73	    ns['If'] = z3.If
74	    ns['Bool'] = z3.Bool
75	    ns['Real'] = z3.Real
76	    ns['Int'] = z3.Int
77	    ns['True'] = True
78	    ns['False'] = False
79	    ns['Mod'] = lambda a, b: a % b
80	    ns['pow'] = lambda a, b: a ** b
81	
82	    ns['abs'] = lambda x: z3.If(x >= 0, x, -x) if isinstance(x, z3.ArithRef) else abs(x)
83	
84	    def _z3_sum(*args):
85	        items = []
86	        for a in args:
87	            if hasattr(a, '__iter__') and not isinstance(a, z3.ExprRef):
88	                items.extend(a)
89	            else:
90	                items.append(a)
91	        if not items:
92	            return 0
93	        result = items[0]
94	        for item in items[1:]:
95	            result = result + item
96	        return result
97	
98	    def _z3_max(*args):
99	        items = []
100	        for a in args:
101	            if hasattr(a, '__iter__') and not isinstance(a, z3.ExprRef):
102	                items.extend(a)
103	            else:
104	                items.append(a)
105	        if not items:
106	            raise ValueError("max() requires at least one argument")
107	        result = items[0]
108	        for item in items[1:]:
109	            if isinstance(result, z3.ExprRef) or isinstance(item, z3.ExprRef):
110	                result = z3.If(result >= item, result, item)
111	            else:
112	                result = result if result >= item else item
113	        return result
114	
115	    def _z3_min(*args):
116	        items = []
117	        for a in args:
118	            if hasattr(a, '__iter__') and not isinstance(a, z3.ExprRef):
119	                items.extend(a)
120	            else:
121	                items.append(a)
122	        if not items:
123	            raise ValueError("min() requires at least one argument")
124	        result = items[0]
125	        for item in items[1:]:
126	            if isinstance(result, z3.ExprRef) or isinstance(item, z3.ExprRef):
127	                result = z3.If(result <= item, result, item)
128	            else:
129	                result = result if result <= item else item
130	        return result
131	
132	    ns['sum'] = _z3_sum
133	    ns['Sum'] = _z3_sum
134	    ns['max'] = _z3_max
135	    ns['min'] = _z3_min
136	    ns['len'] = len
137	    ns['int'] = lambda x: x
138	
139	    try:
140	        result = eval(formula_str, {"__builtins__": {}}, ns)
141	        if isinstance(result, z3.ExprRef) and z3.is_bool(result):
142	            return result
143	        if isinstance(result, bool):
144	            return z3.BoolVal(result)
145	        return None
146	    except Exception as e:
147	        logger.debug("Failed to parse z3 formula '%s': %s", formula_str, e)
148	        return None
149	
150	
151	def check_equivalence(f1: z3.ExprRef, f2: z3.ExprRef, timeout_ms: int = 1000) -> bool:
152	    """Check if two z3 formulas are logically equivalent (f1 ⟺ f2)."""
153	    if not z3.is_bool(f1) or not z3.is_bool(f2):
154	        return False
155	    s = z3.Solver()
156	    s.set("timeout", timeout_ms)
157	    s.add(z3.Not(f1 == f2))
158	    result = s.check()
159	    return result == z3.unsat
160	
161	
162	@dataclass
163	class UniqueConstraint:
164	    expression: str
165	    z3_formula: z3.ExprRef
166	    weight: int  # cross-trace frequency
167	    source_traces: list[int] = field(default_factory=list)
168	
169	    def __repr__(self) -> str:
170	        return f"UniqueConstraint(expr='{self.expression}', w={self.weight}, traces={self.source_traces})"
171	
172	
173	@dataclass
174	class MaxSATResult:
175	    satisfied: list[UniqueConstraint]
176	    excluded: list[UniqueConstraint]
177	    total_weight: int
178	    solve_time_ms: float
179	
180	
181	class ConstraintDeduplicator:
182	    """Deduplicate constraints across traces using z3 equivalence checking."""
183	
184	    def __init__(self, equiv_timeout_ms: int = 1000):
185	        self.equiv_timeout_ms = equiv_timeout_ms
186	
187	    def deduplicate(self, all_constraints: list[list[dict]]) -> list[UniqueConstraint]:
188	        """Merge equivalent constraints across K traces.
189	
190	        Args:
191	            all_constraints: K lists of constraint dicts, one per trace.
192	        Returns:
193	            Deduplicated list with frequency weights.
194	        """
195	        unique: list[UniqueConstraint] = []
196	
197	        for trace_idx, trace_constraints in enumerate(all_constraints):
198	            for c in trace_constraints:
199	                z3_f = parse_z3_formula(c.get("z3_formula", ""))
200	                if z3_f is None:
201	                    logger.debug("Skipping unparseable constraint: %s", c.get("z3_formula"))
202	                    continue
203	
204	                merged = False
205	                for uc in unique:
206	                    try:
207	                        if check_equivalence(uc.z3_formula, z3_f, self.equiv_timeout_ms):
208	                            uc.weight += 1
209	                            if trace_idx not in uc.source_traces:
210	                                uc.source_traces.append(trace_idx)
211	                            merged = True
212	                            break
213	                    except Exception:
214	                        continue
215	
216	                if not merged:
217	                    unique.append(UniqueConstraint(
218	                        expression=c.get("expression", ""),
219	                        z3_formula=z3_f,
220	                        weight=1,
221	                        source_traces=[trace_idx],
222	                    ))
223	
224	        return unique
225	
226	
227	class MaxSATSolver:
228	    """Weighted partial MAX-SAT solver using z3.Optimize."""
229	
230	    def solve(self, unique_constraints: list[UniqueConstraint], timeout_ms: int = 10000) -> MaxSATResult:
231	        """Find the maximum-weight satisfiable subset of constraints."""
232	        if not unique_constraints:
233	            return MaxSATResult(satisfied=[], excluded=[], total_weight=0, solve_time_ms=0.0)
234	
235	        opt = z3.Optimize()
236	        opt.set("timeout", timeout_ms)
237	
238	        indicators = []
239	        active_mask = []
240	        for i, uc in enumerate(unique_constraints):
241	            ind = z3.Bool(f"__ind_{i}")
242	            indicators.append(ind)
243	            try:
244	                if not z3.is_bool(uc.z3_formula):
245	                    active_mask.append(False)
246	                    continue
247	                opt.add(z3.Implies(ind, uc.z3_formula))
248	                opt.add_soft(ind, weight=uc.weight)
249	                active_mask.append(True)
250	            except Exception as e:
251	                logger.debug("Skipping constraint %d in MaxSAT: %s", i, e)
252	                active_mask.append(False)
253	
254	        if not any(active_mask):
255	            return MaxSATResult(satisfied=[], excluded=list(unique_constraints),
256	                                total_weight=0, solve_time_ms=0.0)
257	
258	        t0 = time.perf_counter()
259	        result = opt.check()
260	        solve_time = (time.perf_counter() - t0) * 1000
261	
262	        satisfied = []
263	        excluded = []
264	
265	        if result in (z3.sat, z3.unknown):
266	            model = opt.model()
267	            for i, uc in enumerate(unique_constraints):
268	                if not active_mask[i]:
269	                    excluded.append(uc)
270	                    continue
271	                val = model.evaluate(indicators[i], model_completion=True)
272	                if z3.is_true(val):
273	                    satisfied.append(uc)
274	                else:
275	                    excluded.append(uc)
276	        else:
277	            excluded = list(unique_constraints)
278	
279	        total_w = sum(uc.weight for uc in satisfied)
280	        return MaxSATResult(
281	            satisfied=satisfied,
282	            excluded=excluded,
283	            total_weight=total_w,
284	            solve_time_ms=solve_time,
285	        )
286	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "549a831c-8774-4650-9bda-c27526ea544e",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "7c8b0231-1542-48b3-b1b6-f46f027e647a",
  "sourceToolAssistantUUID": "549a831c-8774-4650-9bda-c27526ea544e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-16T06:20:12.004Z_

Now let me also read the other relevant project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c8b0231-1542-48b3-b1b6-f46f027e647a",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mF4BG9Y9bVSpvFQ16U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "acdea8dd-6d7c-4ac1-991e-f9ebcb4b7e4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01STYrgzWixhy9C9gru36h11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8920,
      "cache_read_input_tokens": 53931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8920,
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

_source line 34 · 2026-05-16T06:20:13.519Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01A5MhGpjAXbzqyf3Xfruqxv`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "experiment_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acdea8dd-6d7c-4ac1-991e-f9ebcb4b7e4d",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mF4BG9Y9bVSpvFQ16U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "639ff9e2-5f63-4178-a75f-0fe81ac0042c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01STYrgzWixhy9C9gru36h11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8920,
      "cache_read_input_tokens": 53931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8920,
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

### Tool result

_source line 35 · 2026-05-16T06:20:13.542Z_

<details><summary>↩ Tool result · `toolu_01A5MhGpjAXbzqyf3Xfruqxv`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "639ff9e2-5f63-4178-a75f-0fe81ac0042c",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "8dd7b188-e054-476b-a640-25e49d90e22c",
  "sourceToolAssistantUUID": "639ff9e2-5f63-4178-a75f-0fe81ac0042c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T06:20:13.781Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019BTWPCdLPFNorqBYRJxu9D`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dd7b188-e054-476b-a640-25e49d90e22c",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mF4BG9Y9bVSpvFQ16U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3647e0d3-d45c-4b2f-b2c4-507fd389a6b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01STYrgzWixhy9C9gru36h11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8920,
      "cache_read_input_tokens": 53931,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8920
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 53931,
          "cache_creation_input_tokens": 8920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8920,
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

_source line 37 · 2026-05-16T06:20:13.798Z_

<details><summary>↩ Tool result · `toolu_019BTWPCdLPFNorqBYRJxu9D`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/decisions.yaml\", \"content\": \"_next_id: 22\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 08:47 UTC\\n  summary: MVP 验证方案：50 题 MATH-500 分层子集，SICA vs SC@K=12\\n  rationale: SICA 核心价值取决于两个前提：(1) 能从推理 trace 可靠提取符号约束；(2) 跨路径矛盾率足够高（>5%）使形式化验证有意义。Reviewer\\n    给 impact 3/5，核心担忧是\\\"若矛盾率<5%则动机不成立\\\"。MVP 直接验证这两个前提，50 题按难度分层可同时观察 Extraction-Verification\\n    Paradox（难题提取差但矛盾多）。Pass 则进入全量实验冲 EMNLP/AAAI，Fail 则及时止损。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 08:52 UTC\\n  summary: 拒绝 CRD pivot，要求回归 SICA 原始方案\\n  rationale: Reviewer critical 审查发现 Agent 实施的是\\\"跨表征分歧诊断\\\"(CRD)，与 IDEA_BRIEF 定义的 SICA\\n    完全不同：CRD 用双表征（FOL+SymPy）做单解分歧检测，无多路径采样、无 MAX-SAT 共识——这正是 SICA 区别于 VERGE/D&P 的核心创新点。CRD\\n    的 novelty 定位与 VERGE 高度重叠（单输出验证+修复），无法支撑 EMNLP 投稿。同时 MVP 标准被静默替换，ROADMAP 的三条 pass\\n    criteria 从未测试。98GB GPU 完全能跑 QwQ-32B，无理由换 Qwen3-32B-AWQ。必须回归 SICA：K=12 多路径采样 →\\n    符号约束提取 → Z3 加权 partial MAX-SAT → 不变量共识打分。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 08:54 UTC\\n  summary: MVP 标准 v2：三档判定 + 矛盾绝对数 ≥5 + accuracy ≥SC+2pp + ProofWriter sanity check\\n  rationale: Reviewer warning 指出：(1) 5% 矛盾率阈值在 50 题上仅 2.5 题，置信区间极宽——改为绝对数 ≥5 题；(2)\\n    ≥SC+0.1pp 也过关无意义——改为 ≥2pp 或 p<0.1；(3) 灰色区间无处理——新增 Inconclusive 档，触发扩展到 100 题重测；(4)\\n    单域 MATH-500 不够——加 10 题 ProofWriter 做逻辑域 sanity check；(5) 模型不能模糊——固定 QwQ-32B，不可替换。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP T=0.7 继续跑完（需要完整数据），diagnostic 自然结束后 GPU 带宽恢复；AIME 30 题排在 MVP 之后\\n  rationale: Temperature 诊断 4/5 题显示 T=0.7/0.9/1.0 均几乎不产生答案分歧——C2/C3 高风险 FAIL。但仍决定让\\n    MVP 跑完：(1) 50 题完整数据无论正负都有价值（负面结果=SICA 在强模型上无信号，本身是发现）；(2) GPU 已分配且无其他实验排队；(3)\\n    smoke test L5 有 3 条矛盾，50 题中 L4-5 有 20 题可能产生更多信号。MVP 完成后立即跑 AIME 30 题（QwQ-32B ~79.5%，分歧应更明显），作为\\\"高难度\\n    sweet spot\\\"的补充验证。如果 MATH+AIME 均 SICA≈SC → 准备 FAIL 路径决策。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-15 12:16 UTC\\n  summary: 'D005: 采用双管齐下方案——MATH-500 MVP 继续 + AIME 30 题紧跟，暂不换模型'\\n  rationale: Temperature 诊断确认 QwQ-32B 在 T=0.7/0.9/1.0 下均产生近零答案分歧——reasoning model\\n    的确定性推理压制采样随机性。MATH-500 MVP 高概率 FAIL on C2/C3，但数据仍有价值（负面结果本身有意义）。AIME 2024 是 QwQ-32B\\n    弱项（~79.5%），更可能产生 trace 分歧——如果 SICA 在 AIME 上有信号，paper story 改为\\\"SICA 在高难度/高不确定性场景下最有价值\\\"，反而比\\\"通用提升\\\"更有深度。模型切换（Qwen2.5-7B\\n    等）改变论文定位太大，留作 AIME 也失败后的最后手段。执行顺序：MATH MVP 跑完 → AIME 30 题 → 基于两组结果做 PASS/FAIL\\n    最终判定。\\n  related_experiments: []\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-15 12:19 UTC\\n  summary: 'D006: Kill 当前 MATH MVP（有 bug + 25-30h 不可接受），修 bug 后 AIME 30 题优先'\\n  rationale: D005 假设 MVP 4-7h 出结果，但实际第一题 20min+ 未完成（serial trace gen + extraction\\n    回归 5/12 JSON parse fail），外推 25-30h。加上多样性诊断已定论（零分歧），继续烧 25-30h GPU 等一个几乎确定 FAIL\\n    的结果不合理。改为：(1) Kill 当前 MVP；(2) 修两个 bug——trace gen 用 n=K batch 而非串行、extraction 回归（ProofWriter\\n    prompt 合并后可能破坏了 math 域的 JSON parse）；(3) AIME 30 题优先跑（QwQ-32B 弱项，最可能出现分歧，30 题修复后\\n    ~3-4h）；(4) AIME 有信号 → 回来跑修复后的 MATH MVP；AIME 也无信号 → FAIL。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-15 16:31 UTC\\n  summary: 'D007: z3 parser 是 0pp 差距根因——并行修 parser + scorer，v3 继续跑后批量重打分'\\n  rationale: '7/30 题 Reviewer 分析发现 parse_z3_formula() 损失率 41-100%（P7: 72→1, 98.6%），LLM\\n    提取的约束在 z3 转换时被大量丢弃，MAX-SAT 无法工作。P7（SC 1/12 极度分散）是 SICA 理论最佳场景但因 parser 失效无法发挥。策略：v3\\n    继续跑收集全部 traces（最贵部分），并行修 parser + scorer，30 题完成后批量重打分作为真正 MVP 结果。'\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: 数据来源\\n    result: running, 7/30 done, 0pp差距但因parser bug无效\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-15 17:40 UTC\\n  summary: 'D008: P5 翻转为虚假声明（硬编码），A+C 实际翻转数=0。答案提取率过低是 C3 根本瓶颈，提升为最高优先级'\\n  rationale: '调查发现 P5 \\\"120→80 flip\\\" 是 rescore_pure.py 硬编码的对照值，v3 P5 实际仅 1 个候选答案 \\\"80\\\"。P7\\n    的 72→1 也是 parser 仍无法处理（2.8% parse rate），非 dedup 逻辑 bug。11/30 中 SICA=SC 的根因是答案提取率极低（P5:\\n    1/12, P2/P8/P9/P11: 0/12），多候选竞争场景不存在，任何 scorer 都无法差异化。将答案提取改进提升为最高优先级。'\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: 数据来源\\n    result: 11/30 done, SICA=SC=63.6%, 0pp\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-15 17:53 UTC\\n  summary: 'D009: max_tokens=10240 截断是 0-vote 根因，修为 16384 + fallback extraction +\\n    save intermediates，v3 完成后 v4 重跑截断题'\\n  rationale: P8/P9/P11 的 0/12 答案提取全因 trace 在 10240 tokens 截断，\\\\boxed{} 未生成。P11 有 60\\n    raw constraints（11/12 提取成功）证明模型推理充分但 token 不够。trace 耗时与截断强相关：350-435s→12/12 votes,\\n    730-810s→0-1/12 votes。修复 max_tokens + fallback extraction 预计恢复 P8/P9/P11 答案，创造多候选场景让\\n    SICA 有差异化空间。v3 继续跑（非截断题有效），v4 只重跑截断题，合并为最终 MVP。\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: 数据来源\\n    result: 12/30 done, P8/P9/P11 confirmed truncated at 10240 tokens\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-15 19:11 UTC\\n  summary: 'D010: AIME 0pp gap 是结构性的——QwQ-32B 单候选主导，SICA≡SC。MATH-50 升为关键判定实验'\\n  rationale: Reviewer 审查 22/30 题发现：所有非空 SC vote 分布仅含 1 个候选答案（unanimous among voting\\n    traces）。SICA 只能在多候选竞争时产生差异，单候选场景下无论约束打分如何都选同一答案。这不是 parser/scorer bug，是 QwQ-32B\\n    在 AIME 上答案高度一致的结构性特征（temp_diversity 实验已佐证）。v4 修复 max_tokens+fallback 可能恢复截断题的答案，但如果恢复的仍是同一答案则\\n    0pp 不变。MATH-500 Level 1-5 混合难度可能存在更多答案多样性（模型错误率 ~9.4%，错题上不同 trace 可能给出不同错答案），是验证\\n    SICA 核心假设的关键实验。调整优先级：v3 完成 → vote diversity 分析 → v4 快速验证 → MATH-50（决定性实验）。\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: evidence\\n    result: 22/30 完成, SICA=SC=72.7%, 0pp gap, 0 题多候选\\n  depends_on:\\n  - D007\\n  - D009\\n- id: D011\\n  date: 2026-05-15 19:47 UTC\\n  summary: 'D011: Reviewer 预判 MATH-50 将重现单候选模式（已有 32 题零分歧证据），修订策略：MATH-10 快速诊断 → 逻辑域优先'\\n  rationale: Reviewer 指出 temp_diversity 实验是在 MATH L4-5 上做的（非 AIME），3 个温度 × 5 题 = 零答案分歧；加上\\n    smoke_5q（5 题 MATH）和 AIME 22 题，共 32 题零多候选。QwQ-32B 答案一致性是模型级特征（CoT 链逻辑约束远强于采样温度），非任务特定。全量\\n    MATH-50（7-8h GPU）几乎确定重现 0pp。修订策略：(1) v3 完成后做 vote diversity 分析；(2) 取消 v4 AIME\\n    re-run，改为 MATH-10 trace-only 诊断（v4 代码，~1h）验证修复 + 确认/否定单候选假设；(3) 如确认单候选 → 立即转向\\n    ProofWriter + FOLIO 作为主实验（逻辑域 FOL 规范化程度高、answer distribution 天然多候选、Z3 parser 损耗低）；(4)\\n    MATH/AIME 数据保留为 domain boundary 分析。\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: evidence\\n    result: 22/30 单候选\\n  - exp_id: sica_temp_diversity\\n    role: evidence\\n    result: MATH L4-5 三温度零分歧\\n  - exp_id: smoke_5q\\n    role: evidence\\n    result: 5题MATH单候选\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-15 22:24 UTC\\n  summary: 'D012: 逻辑域 MVP 判定标准——ProofWriter-30 + FOLIO-30 合并 60 题，沿用 D003 框架 + 新增多候选前置条件'\\n  rationale: 'D011 将主实验从 MATH-500 pivot 到逻辑域，但 D003 判定标准仍针对 MATH-500，ProofWriter 定位仅为\\\"sanity\\n    check 不影响 PASS/FAIL\\\"。Reviewer 指出 proofwriter30_v2 完成后无法判定。新标准沿用 D003 框架（保持一致性避免\\n    goalpost-moving），新增多候选前置条件（吸取 AIME/MATH 教训）：\\n\\n\\n    PASS（全部满足）：\\n\\n    - C1: 约束提取率 ≥ 50%\\n\\n    - C2: 跨路径矛盾检出 ≥ 5 题（绝对数）\\n\\n    - C3: SICA accuracy ≥ SC + 2pp（合并 60 题），或 paired bootstrap p < 0.1\\n\\n    - C0（前置）: 多候选率 ≥ 20%（≥12/60 题有 >1 个 unique candidate）\\n\\n\\n    INCONCLUSIVE（触发扩展重测）：\\n\\n    - C3 为 +0~2pp，其余满足\\n\\n\\n    FAIL（任一触发）：\\n\\n    - C0 < 20% 多候选 → 结构性失效，同 MATH/AIME\\n\\n    - C1 < 30%\\n\\n    - C2 < 3 题\\n\\n    - C3 < SC\\n\\n\\n    ProofWriter-30 和 FOLIO-30 合并判定（60 题），但分别报告以观察域差异。'\\n  related_experiments:\\n  - exp_id: sica_proofwriter30_v2\\n    role: target\\n    result: running\\n  - exp_id: sica_folio30\\n    role: target\\n    result: planned\\n  depends_on:\\n  - D003\\n  - D011\\n- id: D013\\n  date: 2026-05-16 01:30 UTC\\n  summary: 'D013: ProofWriter 中期 CRITICAL——MaxSAT 结构性失效(16/16 excluded=0)，终止当前实验，紧急诊断根因后再决定\\n    FOLIO'\\n  rationale: Reviewer 独立核实 16/30 题中期数据：C0/C1/C2/C3 四项全 FAIL。最关键的是 C2=0（矛盾检出为零），MaxSAT\\n    satisfied_ratio=1.000 贯穿全部问题，SICA 核心机制从未激活。C3=-6.25pp 说明 SICA 不仅无效还主动伤害准确率。继续跑剩余\\n    14 题无意义。需紧急诊断 MaxSAT 全满足的根因：(a) 约束太粗/抽象无法矛盾→设计缺陷 (b) SAT 编码 bug→可修 (c) 去重后约束太少→可调。根因决定\\n    FOLIO 是否值得跑以及 MVP 是否有救。May 19 checkpoint 仅剩 3 天。\\n  related_experiments:\\n  - exp_id: sica_proofwriter30_v2\\n    role: primary\\n    result: C2=0 structural failure, all 4 D012 criteria FAIL at midpoint\\n  depends_on:\\n  - D012\\n- id: D014\\n  date: 2026-05-16 01:39 UTC\\n  summary: 'D014: MaxSAT 结构性失效根因确认——约束编码缺 answer assertion + 提取失败率 54%。选 A 方案：L3+L1\\n    修复 → 5 题验证 → 全量'\\n  rationale: 诊断 6/6 注入测试通过证明 MaxSAT 求解器无 bug。satisfied_ratio=1.0 的根因是：(1) 不同答案的 trace\\n    未注入 answer assertion 约束，MaxSAT 无法产生冲突；(2) 提取失败率 54.4%（QwQ 重新推理而非输出 JSON）。L3 修复（注入\\n    answer==trace_answer）是 SICA 能否工作的架构前提，L1（prompt 强制 JSON）是质量保障。先 5 题验证再全量，避免浪费\\n    GPU。\\n  related_experiments:\\n  - exp_id: sica_proofwriter30_v2\\n    role: trigger\\n    result: MaxSAT 16/16 satisfied_ratio=1.0, SICA worse than SC by 6.2pp\\n  depends_on:\\n  - D013\\n- id: D015\\n  date: 2026-05-16 02:48 UTC\\n  summary: 'D015: FOLIO C0 预检 0% 多候选率——QwQ-32B 跨三域自一致性是模型级特征，SICA 核心前提（trace 分歧）不成立。等\\n    L3+L1 五题验证后做最终 MVP 判定。'\\n  rationale: FOLIO 10 题 K=6 traces 全部 unanimous（0% 多候选），与 AIME 0%、ProofWriter 18.8%\\n    汇总后，C0 合并判定确定性 FAIL（远低于 ≥20% 门槛）。QwQ-32B 在数学+逻辑+FOL 三个域均表现出极高 trace 一致性，SICA 的差异化空间不存在。5\\n    题 L3+L1 验证仍在跑，用于确认机制 soundness（与使用场景独立），完成后做最终 MVP 判定。\\n  related_experiments:\\n  - exp_id: sica_folio30\\n    role: C0 precheck\\n    result: 0/10 multi-candidate, all unanimous\\n  - exp_id: sica_proofwriter30_v2\\n    role: context\\n    result: 3/16 multi-candidate = 18.8%\\n  - exp_id: sica_temp_diversity\\n    role: context\\n    result: 0% diversity across 3 temperatures\\n  depends_on:\\n  - D012\\n  - D014\\n- id: D016\\n  date: 2026-05-16 02:51 UTC\\n  summary: 'D016: QwQ-32B MVP FAIL，模型 pivot 到 Qwen2.5-14B-Instruct——全域 C0=3.6% 远低于\\n    20% 阈值，模型级自一致性使 SICA≡SC，切换非 reasoning model 验证算法本身有效性'\\n  rationale: 全域证据（MATH 0%, AIME 0%, ProofWriter 18.75%, FOLIO 0%，合并 3/83=3.6%）确认 QwQ-32B\\n    自一致性是模型级特征而非域特征。SICA 算法需要多候选输入才能与 SC 产生差异。模型替换是唯一可测试\\\"算法本身是否有效\\\"的路径。选择 Qwen2.5-14B-Instruct：非\\n    reasoning model 采样多样性高、14B 在 98GB GPU 上轻松部署、Qwen2.5 系列逻辑能力强。预计 C0 预检 1h + 完整评估\\n    4h，May 19 checkpoint 可控。\\n  related_experiments:\\n  - exp_id: sica_folio30\\n    role: trigger\\n    result: FOLIO C0=0%\\n  - exp_id: sica_proofwriter30_v2\\n    role: evidence\\n    result: ProofWriter C0=18.75%\\n  - exp_id: sica_temp_diversity\\n    role: evidence\\n    result: 3 temps 0% diversity\\n  - exp_id: sica_aime30_v3\\n    role: evidence\\n    result: AIME 0pp gap\\n  depends_on:\\n  - D012\\n  - D015\\n- id: D017\\n  date: 2026-05-16 05:11 UTC\\n  summary: 'D017: D012 技术 PASS（C3 +3.3pp）但统计 INCONCLUSIVE（p=0.317）——全部增益来自 4 个 6:6\\n    tiebreak，SICA 机制是 principled tiebreaking 而非 constraint override。扩展实验到 200 题 +\\n    K 敏感性分析争取统计效力'\\n  rationale: 60 题中仅 4 题 SICA≠SC，全部为 6:6 精确平票。56 个非平票题 SICA=SC（约束从未推翻明确多数）。McNemar\\n    p=0.317，二项检验 p=0.3125，均不显著。FOLIO +6.7pp 但 ProofWriter 0pp，域泛化不成立。SICA 的实际贡献是 principled\\n    tiebreaking 而非原始假设的 symbolic constraint override。需要更多数据点来判断 tiebreaking 模式是否稳定可复现。扩展到全量\\n    PW+FOLIO + K=8/16/20 敏感性分析是最高效的统计加固路径。\\n  related_experiments:\\n  - exp_id: sica_d012_14b\\n    role: evidence\\n    result: C3 +3.3pp, p=0.317, 4 tiebreaks only\\n  depends_on:\\n  - D016\\n  - D012\\n- id: D018\\n  date: 2026-05-16 05:14 UTC\\n  summary: 'D017: D012 PASS, MVP 通过——SICA 在有多样性输入时确实≠SC（+3.3pp），核心假设验证。研究阶段首要任务：扩大样本量\\n    + tiebreak 基线分析 + K 消融'\\n  rationale: D012 四项标准全部技术达标：C0=53.3%, C1=100%, C2=34题, C3=+3.3pp。但 C3 实质弱点明确：全部增益来自\\n    4 个 6:6 平票（SICA 3/4 正确 vs SC 1/4），p=0.317 不显著，FOLIO +6.7pp / PW 0pp。MVP 标准以 OR\\n    条件通过（+3.3pp ≥ +2pp），核心假设\\\"SICA 在有多样性输入时≠SC\\\"已验证——机制是 principled tiebreaking via\\n    constraint weights。模型对照（QwQ-32B C0=3.6%, SICA≡SC）强化了\\\"多样性是 SICA 前提\\\"的结论。研究阶段需解决统计弱点：扩展到\\n    200+ 题、K sensitivity、random tiebreak baseline。\\n  related_experiments:\\n  - exp_id: sica_d012_14b\\n    role: primary\\n    result: SICA 73.3% vs SC 70.0%, +3.3pp, 4 tiebreaks, p=0.317\\n  depends_on:\\n  - D012\\n  - D016\\n- id: D019\\n  date: 2026-05-16 05:22 UTC\\n  summary: exp-007 (72B-AWQ) 从 P2 提升到 P1，Claim 2 至少需要 4 个模型\\n  rationale: Reviewer 指出 Claim 2 \\\"Operating Regime Characterization\\\" 仅有 QwQ-32B 和\\n    Qwen2.5-14B 两个模型，不足以支撑 \\\"model property, not task property\\\" 的论断。加上 exp-004 (7B)\\n    也只有 3 个模型。72B-AWQ 补齐后形成 7B/14B/72B instruction + 32B reasoning 的完整 scaling 证据链，4\\n    个模型是 \\\"operating regime\\\" claim 的最低门槛。GPU 时间预算 ~4h，串行排在 exp-002 和 exp-004 之后，总计\\n    ~22.5h，May 25 DDL 前充裕。\\n  related_experiments:\\n  - exp_id: exp-007\\n    role: promoted to P1\\n  - exp_id: exp-004\\n    role: P1 scaling point\\n  - exp_id: exp-005\\n    role: existing QwQ-32B data\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-16 05:29 UTC\\n  summary: 'D020: Kill 140题进程B，保留804题进程A以最大化统计力'\\n  rationale: Reviewer 发现两个进程同时请求 vLLM（违反独占规则）。进程A（PID 181491，804题 PW+FOLIO）预计~67个tie，统计力远优于进程B（140题，~12个tie）。13.4h\\n    ETA 在 May 19 checkpoint 前充裕。MVP 核心瓶颈是 p=0.317 统计不显著，最大化 N 是第一优先。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: target\\n    result: 保留804题运行，kill 140题重复进程\\n  depends_on: []\\n- id: D021\\n  date: 2026-05-16 06:16 UTC\\n  summary: 'D021: Scope 扩展——补 3 个非 Qwen 模型 + GSM8K 跨域 + constraint ablation，Claim\\n    2 reframe 为 C0=epistemic uncertainty'\\n  rationale: 用户指出 scope 不足，Reviewer 审计确认：(1) 全 Qwen 家族是 Claim 2 致命弱点 (critical)；(2)\\n    单域数据无法支撑 \\\"model property not task property\\\"；(3) 缺 constraint ablation 防御 \\\"over-engineering\\\"\\n    attack。补 Mistral-7B + LLaMA-8B + DeepSeek-R1-7B（跨 3 家族 + reasoning 第二点）+ GSM8K\\n    30题 pilot（跨域）+ CPU constraint ablation。总额外 GPU ~7h，May 25 ARR 前充裕。Claim 2 从 \\\"model\\n    architecture determines regime\\\" 升级为 \\\"C0 tracks epistemic uncertainty, correlates\\n    with but not identical to architecture\\\"。\\n  related_experiments:\\n  - exp_id: exp-010\\n    role: new\\n    result: planned\\n  - exp_id: exp-011\\n    role: new\\n    result: planned\\n  - exp_id: exp-012\\n    role: new\\n    result: planned\\n  - exp_id: exp-013\\n    role: new\\n    result: planned\\n  - exp_id: exp-014\\n    role: new\\n    result: planned\\n  depends_on:\\n  - D018\\n  - D019\\n\", \"total_chars\": 13280, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3647e0d3-d45c-4b2f-b2c4-507fd389a6b4",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "4d42e1f9-f105-4e82-897f-87b443133a3c",
  "sourceToolAssistantUUID": "3647e0d3-d45c-4b2f-b2c4-507fd389a6b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-16T06:20:17.466Z_

Now let me read the literature map and the median/worst paper versions for comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d42e1f9-f105-4e82-897f-87b443133a3c",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mFURn9Nc3fzFoR8aw4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45d261d9-389d-49cd-8dcd-bd84e3c3c77b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6bgrxfkB5y6Wafkr1UaFv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9154,
      "cache_read_input_tokens": 62851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9154,
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

_source line 39 · 2026-05-16T06:20:18.455Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0132aFwWAz1TLCSjMUTbbhGc`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45d261d9-389d-49cd-8dcd-bd84e3c3c77b",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mFURn9Nc3fzFoR8aw4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d540d3b-90d8-4b58-9b30-b6df4b867805",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6bgrxfkB5y6Wafkr1UaFv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9154,
      "cache_read_input_tokens": 62851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9154,
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

_source line 40 · 2026-05-16T06:20:18.482Z_

<details><summary>↩ Tool result · `toolu_0132aFwWAz1TLCSjMUTbbhGc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml\", \"content\": \"# Literature Map — symb_invariant_consensus (SICA)\\n# Last updated: 2026-05-16\\n# Purpose: Track related work coverage for EMNLP 2026 submission\\n\\ndimensions:\\n\\n  self_consistency_and_variants:\\n    description: \\\"Self-Consistency (SC) decoding and improvements\\\"\\n    papers:\\n      - id: wang2023sc\\n        title: \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\"\\n        authors: \\\"Wang et al.\\\"\\n        venue: \\\"ICLR 2023\\\"\\n        arxiv: \\\"2203.11171\\\"\\n        relevance: \\\"Foundational SC method; our primary baseline\\\"\\n        status: must_cite\\n\\n      - id: chen2024usc\\n        title: \\\"Universal Self-Consistency for Large Language Model Generation\\\"\\n        authors: \\\"Chen et al.\\\"\\n        venue: \\\"ICML 2024\\\"\\n        arxiv: \\\"2311.17311\\\"\\n        relevance: \\\"Extends SC to free-form answers via LLM-based selection; alternative aggregation\\\"\\n        status: must_cite\\n\\n      - id: taubenfeld2025cisc\\n        title: \\\"Confidence Improves Self-Consistency in LLMs\\\"\\n        authors: \\\"Taubenfeld et al.\\\"\\n        venue: \\\"ACL Findings 2025\\\"\\n        arxiv: \\\"2502.06233\\\"\\n        relevance: \\\"Weighted voting via model confidence; reduces samples 40-50%. Shows SC can be improved with non-uniform weighting — SICA uses constraint-based weighting instead\\\"\\n        status: must_cite\\n\\n      - id: kim2026reasc\\n        title: \\\"Reliability-Aware Adaptive Self-Consistency (ReASC)\\\"\\n        authors: \\\"Kim et al.\\\"\\n        venue: \\\"2026\\\"\\n        relevance: \\\"Response-level confidence for early halting; 70-80% cost saving vs naive SC\\\"\\n        status: should_cite\\n\\n      - id: loo2025reevaluating\\n        title: \\\"Reevaluating Self-Consistency Scaling in Multi-Agent Systems\\\"\\n        authors: \\\"Loo et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2511.00751\\\"\\n        relevance: \\\"CRITICAL — shows SC gains plateau early and can decline at high sample counts for strong models. Directly supports our QwQ-32B finding (SICA≡SC when model is too consistent)\\\"\\n        status: must_cite\\n\\n      - id: wan2024rasc\\n        title: \\\"Reasoning-Aware Self-Consistency (RASC)\\\"\\n        authors: \\\"Wan et al.\\\"\\n        venue: \\\"2024\\\"\\n        relevance: \\\"Combines answer-level and rationale-level features; reduces samples ~88%\\\"\\n        status: should_cite\\n\\n      - id: dsc2025\\n        title: \\\"Difficulty-Adaptive Self-Consistency\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"NAACL Findings 2025\\\"\\n        relevance: \\\"Ranks problem difficulty to allocate sampling budget; complementary efficiency approach\\\"\\n        status: optional\\n\\n  symbolic_reasoning_llm:\\n    description: \\\"Neuro-symbolic methods combining LLMs with formal solvers\\\"\\n    papers:\\n      - id: pan2023logiclm\\n        title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n        authors: \\\"Pan et al.\\\"\\n        venue: \\\"EMNLP Findings 2023\\\"\\n        arxiv: \\\"2305.12295\\\"\\n        relevance: \\\"LLM→FOL→solver pipeline; closest architectural ancestor to SICA. Key difference: Logic-LM uses single-path translation, SICA aggregates across multiple paths\\\"\\n        status: must_cite\\n\\n      - id: xu2026dylos\\n        title: \\\"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (DyLoS)\\\"\\n        authors: \\\"Xu et al.\\\"\\n        venue: \\\"EACL 2026\\\"\\n        arxiv: \\\"2510.06774\\\"\\n        relevance: \\\"Multi-paradigm solver selection (LP/FOL/CSP/SMT); evaluated on FOLIO+ProofWriter. Outperforms Logic-LM. Key difference: DyLoS selects solver type, SICA aggregates constraints across paths\\\"\\n        status: must_cite\\n\\n      - id: fover2025\\n        title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"TACL 2025\\\"\\n        relevance: \\\"FOL verification for NL reasoning; strong results on ProofWriter+FOLIO. Uses verification rather than aggregation\\\"\\n        status: must_cite\\n\\n      - id: li2025survey\\n        title: \\\"A Survey on LLM Symbolic Reasoning\\\"\\n        authors: \\\"Li et al.\\\"\\n        venue: \\\"2025 (under review)\\\"\\n        relevance: \\\"Comprehensive survey; positions SICA within the broader landscape\\\"\\n        status: should_cite\\n\\n      - id: constraintllm2025\\n        title: \\\"ConstraintLLM: A Neuro-Symbolic Framework for Industrial Constraint Programming\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP 2025\\\"\\n        relevance: \\\"Multi-instruction SFT for constraint extraction; different domain (industrial) but related extraction methodology\\\"\\n        status: optional\\n\\n  maxsat_constraint_nlp:\\n    description: \\\"MAX-SAT and constraint satisfaction applied to NLP/reasoning\\\"\\n    papers:\\n      - id: llm_meets_cp2025\\n        title: \\\"Large Language Model Meets Constraint Propagation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"IJCAI 2025\\\"\\n        relevance: \\\"LLM+constraint propagation integration; validates feasibility of constraint-based reasoning with LLMs\\\"\\n        status: should_cite\\n\\n      - id: satbench2025\\n        title: \\\"SATBench: Benchmarking LLMs' Logical Reasoning via SAT Problems\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP 2025\\\"\\n        relevance: \\\"Evaluates LLMs on SAT-formulated problems; establishes that LLMs struggle with pure SAT but can benefit from solver integration\\\"\\n        status: should_cite\\n\\n      - id: maxsat_local_search2025\\n        title: \\\"Optimizing Local Search-based Partial MaxSAT Solving via Initial Assignment Prediction\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"Science China Information Sciences 2025\\\"\\n        relevance: \\\"Solver-side advances in partial MaxSAT; technical reference for our WPMS formulation\\\"\\n        status: optional\\n\\n  folio_proofwriter_sota:\\n    description: \\\"State-of-the-art methods on FOLIO and ProofWriter benchmarks\\\"\\n    papers:\\n      - id: logicagent2025\\n        title: \\\"From Ambiguity to Verdict: A Semiotic-Grounded Multi-Perspective Agent for LLM Logical Reasoning (LogicAgent)\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2509.24765\\\"\\n        relevance: \\\"Multi-perspective logical reasoning; SOTA on logical reasoning benchmarks including FOLIO. +7.05% average gain\\\"\\n        status: must_cite\\n\\n      - id: aristotle2025\\n        title: \\\"Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"ACL 2025\\\"\\n        relevance: \\\"Logic-complete decomposition framework; strong ProofWriter/FOLIO results\\\"\\n        status: must_cite\\n\\n      - id: qi2025symbolic_provers\\n        title: \\\"Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation\\\"\\n        authors: \\\"Qi et al.\\\"\\n        venue: \\\"ICLR 2025\\\"\\n        arxiv: \\\"2502.06563\\\"\\n        relevance: \\\"LLM+symbolic prover combination; evaluated on FOLIO\\\"\\n        status: should_cite\\n\\n      - id: dissecting2025\\n        title: \\\"Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP Findings 2025\\\"\\n        arxiv: \\\"2506.04810\\\"\\n        relevance: \\\"Fine-grained analysis of LLM logical reasoning capabilities on ProofWriter/FOLIO\\\"\\n        status: optional\\n\\n  reasoning_model_diversity:\\n    description: \\\"Trace diversity in reasoning vs non-reasoning models; supports our QwQ-32B finding\\\"\\n    papers:\\n      - id: loo2025reevaluating\\n        title: \\\"Reevaluating Self-Consistency Scaling in Multi-Agent Systems\\\"\\n        authors: \\\"Loo et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2511.00751\\\"\\n        relevance: \\\"CRITICAL — strong models produce near-identical paths, SC gains plateau/decline. Direct support for SICA≡SC on QwQ-32B\\\"\\n        status: must_cite\\n\\n      - id: diversity_aware_tts2025\\n        title: \\\"Diversity-Aware Training for Test-Time Scaling\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"Under review 2025\\\"\\n        relevance: \\\"Independent reasoning attempts collapse into similar solutions; diversity training needed to unlock test-time scaling. Supports our claim that non-reasoning models have more useful diversity\\\"\\n        status: must_cite\\n\\n      - id: snell2025scaling_tts\\n        title: \\\"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters\\\"\\n        authors: \\\"Snell et al.\\\"\\n        venue: \\\"ICLR 2025 (Oral)\\\"\\n        arxiv: \\\"2408.03314\\\"\\n        relevance: \\\"Foundational test-time compute scaling; shows compute-optimal strategies vary by difficulty. Contextualizes why SICA needs diverse paths\\\"\\n        status: should_cite\\n\\n      - id: deepseek_r1_2025\\n        title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n        authors: \\\"DeepSeek-AI\\\"\\n        venue: \\\"Nature 2025\\\"\\n        arxiv: \\\"2501.12948\\\"\\n        relevance: \\\"Defines the reasoning model paradigm (RL-trained extended thinking); reference for why these models are highly self-consistent\\\"\\n        status: must_cite\\n\\n      - id: base_models_reason2025\\n        title: \\\"Base Models Know How to Reason, Thinking Models Learn When\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2510.07364\\\"\\n        relevance: \\\"RL teaches activation timing not new skills; implies reasoning models converge to similar reasoning patterns, reducing trace diversity\\\"\\n        status: should_cite\\n\\n      - id: korikov2025sc_ranking\\n        title: \\\"The Impact of LLM Self-Consistency and Reasoning Effort on Automated Scoring\\\"\\n        authors: \\\"Korikov et al.\\\"\\n        venue: \\\"arXiv 2026\\\"\\n        arxiv: \\\"2604.26954\\\"\\n        relevance: \\\"Temperature sampling helps but ensemble size (1→7) produces no significant gains; supports diminishing returns of naive SC\\\"\\n        status: optional\\n\\n  multi_path_aggregation:\\n    description: \\\"Methods for aggregating multiple reasoning paths beyond majority voting\\\"\\n    papers:\\n      - id: rc2025\\n        title: \\\"Representation Consistency for Accurate and Coherent LLM Answer Aggregation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2506.21590\\\"\\n        relevance: \\\"Aggregation via representation similarity; down-weights incoherent reasoning. Semantic alternative to SICA's symbolic approach\\\"\\n        status: should_cite\\n\\n      - id: multi_path_plan2025\\n        title: \\\"Enhancing Long Chain-of-Thought Reasoning through Multi-Path Plan Aggregation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2510.11620\\\"\\n        relevance: \\\"Multi-path aggregation at plan level rather than answer level\\\"\\n        status: optional\\n\\n      - id: crest2025\\n        title: \\\"Improving LLMs' Reasoning with Consistency-Driven Self-Training (CREST)\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"NAACL 2025\\\"\\n        relevance: \\\"Consistency as training signal rather than inference-time aggregation\\\"\\n        status: optional\\n\\ngaps:\\n  resolved: []\\n  remaining:\\n    - dimension: \\\"reasoning_model_diversity\\\"\\n      gap: \\\"No published paper explicitly studies QwQ-32B trace diversity collapse under temperature sampling. Our empirical finding (3.6% multi-candidate across 83 problems) is novel but needs positioning against Loo et al. 2025 and Diversity-Aware TTS\\\"\\n    - dimension: \\\"maxsat_constraint_nlp\\\"\\n      gap: \\\"No direct precedent for weighted partial MAX-SAT as multi-path consensus mechanism in NLI. SICA's formulation appears novel — must frame clearly in Related Work\\\"\\n    - dimension: \\\"self_consistency_and_variants\\\"\\n      gap: \\\"Should verify if CRAFT (mentioned in project docs) is a real published method or internal shorthand\\\"\\n\", \"total_chars\": 11286, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d540d3b-90d8-4b58-9b30-b6df4b867805",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "3d5d5f24-7604-43e3-87da-486848c9dd06",
  "sourceToolAssistantUUID": "5d540d3b-90d8-4b58-9b30-b6df4b867805",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T06:20:20.384Z_

<details open><summary>🔧 Tool call — Read · `toolu_014AVpYJ4jrMZ6UrqNbn7zJ7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d5d5f24-7604-43e3-87da-486848c9dd06",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mFURn9Nc3fzFoR8aw4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0eb73fe-848f-40f7-af65-8f1032c5c9cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6bgrxfkB5y6Wafkr1UaFv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9154,
      "cache_read_input_tokens": 62851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9154,
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

_source line 42 · 2026-05-16T06:20:20.411Z_

<details><summary>↩ Tool result · `toolu_014AVpYJ4jrMZ6UrqNbn7zJ7`</summary>

```text
1	narrative_guidance: '核心叙事从 "SICA achieves higher accuracy" 转向 "Characterizing when
2	  symbolic consensus helps"。 扩展实验显示 FOLIO 正向增益（~4.4pp, p=0.034）但 ProofWriter 接近零（~0.2pp），
3	  combined bootstrap p=0.082（边缘显著）。Accuracy gain 不能作为独立 headline claim， 需用 K ablation
4	  跨 K 一致性补强（"SICA ≥ SC at all K=6,8,12,16,20"）。 ProofWriter 零增益从弱点转为验证点（C0 较低 + constraint
5	  质量差 → 预期无增益 → 实际无增益）。 C0 散点图正相关但 R² 中等（~0.52），C0 降级为 supporting diagnostic 而非独立
6	  headline claim。 标题方向："When Does Symbolic Consensus Help? Characterizing the Operating
7	  Regime of Constraint-Based LLM Aggregation"。仍投 EMNLP main，需 K ablation + 7B 数据齐备。
8	
9	  '
10	imagined_experiments:
11	- name: sica_expanded_14b
12	  plan_id: exp-001
13	  description: 'Qwen2.5-14B-Instruct, FOLIO 204题 + ProofWriter D5 600题 = 804题, K=12,
14	    T=0.7。最大化统计 power。
15	
16	    '
17	  expected_results:
18	    folio_n: 204
19	    folio_sc_accuracy: 0.721
20	    folio_sica_accuracy: 0.765
21	    folio_gap_pp: 4.4
22	    folio_bootstrap_p: 0.034
23	    folio_c0: 0.4
24	    folio_tie_count: 18
25	    pw_n: 600
26	    pw_sc_accuracy: 0.568
27	    pw_sica_accuracy: 0.57
28	    pw_gap_pp: 0.2
29	    pw_bootstrap_p: 0.45
30	    pw_c0: 0.3
31	    pw_tie_count: 24
32	    combined_n: 804
33	    combined_gap_macro_pp: 2.3
34	    combined_gap_micro_pp: 1.2
35	    combined_bootstrap_p: 0.082
36	    combined_c0_macro: 0.35
37	    tie_questions_total: 42
38	    tie_question_fraction: 0.052
39	    sica_tiebreak_accuracy_on_ties: 0.643
40	    sc_tiebreak_accuracy_on_ties: 0.405
41	    total_constraints_raw: ~78000
42	    total_constraints_unique: ~22000
43	    maxsat_exclusion_rate: 0.031
44	    wall_time_hours: 14.2
45	  result_rationale: 'FOLIO gap 从 d012 的 6.7pp 回落至 4.4pp：d012 的 30 题中 SICA 在 4 道 tie
46	    题上 75% win rate 属小样本高方差，204 题后 tie 比例稳定在 ~9% 但 tiebreak win rate 从 75% 回归至 ~64%，暴露了部分
47	    constraint 质量不足的 tie 题。FOLIO 作为 FOL 推理任务， constraint 提取与任务原生表示对齐（精度 ~78%），C0=0.40
48	    提供了充足的 trace diversity， SICA 的 weighted MAX-SAT 能有效区分 trace 质量，产生稳健的正向增益。
49	
50	    ProofWriter D5 gap≈0 由两因素叠加：(1) D5 深度-5 证明链使推理路径受任务结构约束， C0=0.30 低于 FOLIO；(2)
51	    PW 的 closed-world assumption 和 negation-as-failure 产生的 FOL constraint 质量差——提取出的
52	    constraint 多为 tautological 或 non-discriminative， MAX-SAT 加权无法区分正确与错误 trace。即使
53	    24 题有 tie，SICA 在 PW tie 上 win rate 仅略高于 50%。
54	
55	    Combined p=0.082 因 PW 600 题零增益数据大幅稀释 FOLIO 信号——micro gap 仅 1.2pp。 Macro-average
56	    2.3pp 更好反映 per-dataset 效果。边缘 p 值需 K ablation 趋势一致性补强。
57	
58	    '
59	  tables:
60	  - name: 'Table 1: Main Results — SICA vs SC on Expanded Benchmarks'
61	    columns:
62	    - Dataset
63	    - N
64	    - SC_Acc
65	    - SICA_Acc
66	    - Gap_pp
67	    - p_boot
68	    - C0
69	    rows:
70	    - - FOLIO
71	      - 204
72	      - 72.1%
73	      - 76.5%
74	      - '+4.4'
75	      - 0.034
76	      - 0.4
77	    - - ProofWriter-D5
78	      - 600
79	      - 56.8%
80	      - 57.0%
81	      - '+0.2'
82	      - 0.45
83	      - 0.3
84	    - - Combined (macro)
85	      - 804
86	      - —
87	      - —
88	      - '+2.3'
89	      - 0.082
90	      - 0.35
91	  figures_description:
92	  - Per-dataset accuracy bar chart + 95% bootstrap CI error bars。FOLIO 两柱 CI 刚好不重叠或轻微重叠，PW
93	    两柱完全重合。直观传达 'SICA helps on FOLIO, not PW'。
94	  analysis: 'Median 档核心数据。FOLIO p=0.034 刚进显著区间，PW 零增益如预期。 Combined p=0.082 不满足 0.05
95	    阈值，accuracy gain 不能独立支撑 headline claim， 需与 K ablation 一致性和 operating regime 共同构成论证。
96	    Paper Section 4.1 呈现，强调 "gain concentrated where C0 is high, as predicted"。
97	
98	    '
99	- name: sica_k_ablation_14b
100	  plan_id: exp-002
101	  description: 'K=6,8,12,16,20 在 d012 60 题上的 sensitivity 分析。 SICA 增益是否依赖特定 K？tie 频率如何随
102	    K 变化？
103	
104	    '
105	  expected_results:
106	    dataset: d012_60q
107	    results_by_k:
108	      k6:
109	        sc: 0.667
110	        sica: 0.7
111	        gap_pp: 3.3
112	        c0: 0.47
113	        tie_frac: 0.117
114	        ties: 7
115	      k8:
116	        sc: 0.683
117	        sica: 0.717
118	        gap_pp: 3.3
119	        c0: 0.5
120	        tie_frac: 0.083
121	        ties: 5
122	      k12:
123	        sc: 0.7
124	        sica: 0.733
125	        gap_pp: 3.3
126	        c0: 0.53
127	        tie_frac: 0.067
128	        ties: 4
129	      k16:
130	        sc: 0.717
131	        sica: 0.733
132	        gap_pp: 1.7
133	        c0: 0.55
134	        tie_frac: 0.05
135	        ties: 3
136	      k20:
137	        sc: 0.733
138	        sica: 0.75
139	        gap_pp: 1.7
140	        c0: 0.58
141	        tie_frac: 0.033
142	        ties: 2
143	    best_gap_pp: 3.3
144	    best_gap_k:
145	    - 6
146	    - 8
147	    - 12
148	    sica_geq_sc_all_k: true
149	    gpu_hours: ~4.5
150	  result_rationale: 'SC accuracy 随 K 单调递增（66.7%→73.3%）：更多 vote 使 majority 更稳定。 SICA
151	    accuracy 也递增但斜率更平——SICA 在低 K 时已通过 constraint weighting 补偿 vote 不足。
152	
153	    Gap 在 K≤12 稳定 3.3pp（+2题），K≥16 降至 1.7pp（+1题），因为 tie 频率 从 K=6 的 11.7% 单调降至 K=20
154	    的 3.3%——偶数 K 精确 tie 概率按 C(K,K/2)/2^K 下降。 K≤12 时 tie 数量（4-7题）足够使 ~65% tiebreak
155	    win rate 产出 +2 净增； K≥16 tie 仅 2-3 题，统计上只翻转 1 题。
156	
157	    C0 随 K 递增（0.47→0.58）：更多 sample 更可能采到少数答案——p=0.8 的题 在 K=6 有 26% 概率只看到主答案（0.8^6），K=20
158	    仅 1.2%。 C0 增而 gap 不增说明 tie（而非 C0 本身）是 SICA 增益的直接机制。
159	
160	    关键叙事价值：5 个 K 值全部 SICA ≥ SC，为 p=0.082 提供 trend consistency 补强。
161	
162	    '
163	  tables:
164	  - name: 'Table 2: K Sensitivity — SICA vs SC across Sample Sizes'
165	    columns:
166	    - K
167	    - SC
168	    - SICA
169	    - Gap
170	    - C0
171	    - Tie%
172	    - Ties
173	    rows:
174	    - - 6
175	      - 66.7%
176	      - 70.0%
177	      - '+3.3'
178	      - 0.47
179	      - 11.7%
180	      - 7
181	    - - 8
182	      - 68.3%
183	      - 71.7%
184	      - '+3.3'
185	      - 0.5
186	      - 8.3%
187	      - 5
188	    - - 12
189	      - 70.0%
190	      - 73.3%
191	      - '+3.3'
192	      - 0.53
193	      - 6.7%
194	      - 4
195	    - - 16
196	      - 71.7%
197	      - 73.3%
198	      - '+1.7'
199	      - 0.55
200	      - 5.0%
201	      - 3
202	    - - 20
203	      - 73.3%
204	      - 75.0%
205	      - '+1.7'
206	      - 0.58
207	      - 3.3%
208	      - 2
209	  figures_description:
210	  - 双 Y 轴折线图。左轴 accuracy（SC 虚线, SICA 实线，SICA 始终在上方），右轴 tie fraction（灰色下降柱）。X 轴为 K。传达
211	    gap 与 tie frequency 共变。
212	  analysis: 'K ablation 承担两个角色：(1) 5 个 K 全部 SICA≥SC 消除 "cherry-picked K" 质疑， 为边缘 p
213	    值提供 robustness；(2) gap 与 tie fraction 共变而非与 C0 共变， 确认 tiebreaking 是增益主机制。60 题粒度（1.67pp/题）导致
214	    gap 只有两个离散值， 这是 limitation 也是扩展至 200+ 题的动机。Paper Section 4.3。
215	
216	    '
217	- name: tiebreak_baseline_analysis
218	  plan_id: exp-003
219	  description: 'SICA vs SC-random vs SC-alphabetical vs SC-first-seen tiebreak 比较。
220	    d012 已有结果 + exp-001 扩展数据预测。CPU-only。
221	
222	    '
223	  expected_results:
224	    d012_ties: 5
225	    d012_sica_win_rate: 0.8
226	    expanded_tie_count: 42
227	    expanded_sica_correct: 27
228	    expanded_sica_win_rate: 0.643
229	    expanded_random_correct: ~21
230	    expanded_random_win_rate: 0.5
231	    expanded_alphabetical_correct: 22
232	    expanded_alphabetical_win_rate: 0.524
233	    expanded_firstseen_correct: 18
234	    expanded_firstseen_win_rate: 0.429
235	    sica_vs_random_head_to_head:
236	      sica_wins: 14
237	      random_wins: 8
238	      both_correct: 10
239	      both_wrong: 10
240	      win_rate: 0.636
241	    mcnemar_p: 0.19
242	  result_rationale: 'd012 的 80% tiebreak win rate（4/5）在 42 题上回归至 64.3%——小样本极端值 收敛到
243	    constraint weighting 的 "真实" win rate。64% 显著高于 random 50% 但非压倒性，因为 FOLIO tie 上
244	    win rate ~68%（constraint 好）而 PW tie 上 仅 ~58%（constraint 差，接近随机）。
245	
246	    Alphabetical 略高于 random（52.4%）说明数据集正确答案在字母序有轻微偏置。 First-seen 最低（42.9%）因为模型对难题往往先产出
247	    hallucinated 答案，后续修正。
248	
249	    McNemar p=0.19 无法拒绝 SICA=random 零假设（42 题不够），但方向一致 且与 K ablation 跨 K 一致性互补。
250	
251	    '
252	  tables:
253	  - name: 'Table 3: Tiebreak Resolution — SICA vs Baseline Rules'
254	    columns:
255	    - Method
256	    - Correct
257	    - Win_Rate
258	    - Mechanism
259	    rows:
260	    - - SICA
261	      - 27/42
262	      - 64.3%
263	      - Constraint-weighted MAX-SAT
264	    - - SC-random
265	      - ~21/42
266	      - 50.0%
267	      - Uniform random
268	    - - SC-alphabetical
269	      - 22/42
270	      - 52.4%
271	      - Alphabetical order
272	    - - SC-first-seen
273	      - 18/42
274	      - 42.9%
275	      - First generated answer
276	  figures_description:
277	  - 水平 bar chart 比较四种 tiebreak 策略 accuracy。SICA 最长，random 居中（带 ±1σ），first-seen 最短。
278	  analysis: 'Tiebreak 分析从 headline 降级为 mechanism 分析。64% 说明 constraint weighting 优于盲选但非压倒性。Paper
279	    Section 4.2 "Tiebreak Mechanism"。 强调 SICA 提供 principled（非 arbitrary）tiebreak，而非
280	    "always correct"。
281	
282	    '
283	- name: sica_7b_scaling
284	  plan_id: exp-004
285	  description: 'Qwen2.5-7B-Instruct 在 d012 60 题上运行。 验证 weaker model → higher C0 →
286	    larger gap。
287	
288	    '
289	  expected_results:
290	    model: Qwen2.5-7B-Instruct
291	    n: 60
292	    c0: 0.63
293	    sc_accuracy: 0.55
294	    sica_accuracy: 0.6
295	    gap_pp: 5.0
296	    folio_sc: 0.567
297	    folio_sica: 0.633
298	    folio_gap_pp: 6.7
299	    folio_c0: 0.7
300	    pw_sc: 0.533
301	    pw_sica: 0.567
302	    pw_gap_pp: 3.3
303	    pw_c0: 0.57
304	    bootstrap_p: 0.11
305	    tie_fraction: 0.133
306	    tie_count: 8
307	    tiebreak_win_rate: 0.625
308	    constraint_extraction_failures: ~3
309	    wall_time_hours: ~1.5
310	  result_rationale: '7B 与 14B 在三个维度形成对比：
311	
312	    (1) C0 显著更高（0.63 vs 0.53）：reasoning 能力更弱导致 T=0.7 下更大 answer diversity，tie 比例从
313	    6.7% 升至 13.3%。
314	
315	    (2) Gap 更大（5.0pp vs 3.3pp）：8 道 tie 中 SICA 赢 5 道（62.5%），net +2 题。 PW 上也出现 +3.3pp（vs
316	    14B 的 0pp），因为 7B 在 PW 上 C0 极高（0.57）， tie 基数大到即使 win rate 一般也产出净增。
317	
318	    (3) Baseline accuracy 更低（55% vs 70%）：SICA 不能替代更强模型， 它在给定模型能力下从 trace diversity
319	    中提取额外信号。
320	
321	    Constraint 提取质量略低于 14B（精度 ~65% vs ~78%），但 diversity 更大使 MAX-SAT 仍有足够 discriminative
322	    signal。Bootstrap p=0.11 不显著， 但价值在于构成 C0-gap 散点图的关键数据点。
323	
324	    '
325	  tables:
326	  - name: 'Table 4 row: 7B'
327	    columns:
328	    - Model
329	    - N
330	    - C0
331	    - SC
332	    - SICA
333	    - Gap
334	    - p
335	    rows:
336	    - - Qwen2.5-7B
337	      - 60
338	      - 0.63
339	      - 55.0%
340	      - 60.0%
341	      - '+5.0'
342	      - 0.11
343	  figures_description:
344	  - 数据纳入 exp-006 C0-gap 散点图和 model scaling 汇总表，不单独出图。
345	  analysis: 'C0-as-predictor 的关键验证点：C0 更高 → gap 更大，方向符合预测。 与 QwQ（C0≈0, gap=0）形成 instruction
346	    vs reasoning model 的 operating regime 对比。 7B 低绝对准确率回应 "why not use a better model"——SICA
347	    是 budget-constrained 场景下的增强手段。Paper Section 4.4。
348	
349	    '
350	- name: qwq_32b_operating_regime
351	  plan_id: exp-005
352	  description: 'QwQ-32B MVP 阶段已有数据格式化。无新 GPU。
353	
354	    '
355	  expected_results:
356	    model: QwQ-32B
357	    model_type: reasoning
358	    aime:
359	      n: 22
360	      c0: 0.0
361	      gap_pp: 0
362	    pw:
363	      n: 16
364	      c0: 0.1875
365	      gap_pp: 0
366	    folio:
367	      n: 10
368	      c0: 0.0
369	      gap_pp: 0
370	    combined:
371	      n: 48
372	      c0: 0.036
373	      gap_pp: 0
374	    sica_equiv_sc: true
375	    constraint_exclusion_rate: 0.387
376	  result_rationale: 'QwQ-32B 的内置 chain-of-thought 在采样时产生高度确定性推理链， C0=3.6% 意味着 SICA
377	    数学上退化为 SC（所有 candidate weighted vote 相同 → MAX-SAT 无 discriminative signal → 等价于纯
378	    majority vote）。
379	
380	    Constraint exclusion rate 仍为 38.7%——推理模型 trace 虽答案一致但路径有差异， 部分 constraint 被排除。然而排除后仍指向同一答案，exclusion
381	    mechanism 是 active 的但在 zero-diversity 场景下无效。
382	
383	    PW C0=18.75%（3/16 多候选题）是唯一非零 domain，但 3 题太少产生 power， 且 SICA tiebreak 与 SC 无差异。
384	
385	    '
386	  tables:
387	  - name: 'Table 5: QwQ-32B Per-Domain Breakdown'
388	    columns:
389	    - Domain
390	    - N
391	    - C0
392	    - Gap
393	    - Finding
394	    rows:
395	    - - AIME
396	      - 22
397	      - 0.0%
398	      - 0.0
399	      - Zero diversity — deterministic reasoning
400	    - - ProofWriter
401	      - 16
402	      - 18.8%
403	      - 0.0
404	      - Minimal diversity — insufficient signal
405	    - - FOLIO
406	      - 10
407	      - 0.0%
408	      - 0.0
409	      - Zero diversity
410	  figures_description:
411	  - Operating regime 概念图：X 轴 model type (reasoning→instruction)，Y 轴 C0/gap。QwQ 左下（zero），7B/14B
412	    右上（positive），72B 中间。核心 insight 可视化。
413	  analysis: '从 "negative result" 升级为 operating regime 反面验证。 "Reasoning models don''t
414	    need SICA because they''re already self-consistent。" C0≈0 是 structural finding（与样本量无关），回应
415	    reviewer N 太小的质疑。 Paper Section 4.4 核心之一。
416	
417	    '
418	- name: c0_diagnostic_validation
419	  plan_id: exp-006
420	  description: '跨所有模型和 K 值绘制 C0 vs SICA-SC gap 散点图。 验证 C0 作为 SICA 有效性 diagnostic。
421	
422	    '
423	  expected_results:
424	    total_data_points: 14
425	    data_points:
426	    - model: 14B
427	      config: K6
428	      c0: 0.47
429	      gap_pp: 3.3
430	    - model: 14B
431	      config: K8
432	      c0: 0.5
433	      gap_pp: 3.3
434	    - model: 14B
435	      config: K12
436	      c0: 0.53
437	      gap_pp: 3.3
438	    - model: 14B
439	      config: K16
440	      c0: 0.55
441	      gap_pp: 1.7
442	    - model: 14B
443	      config: K20
444	      c0: 0.58
445	      gap_pp: 1.7
446	    - model: 14B-exp
447	      dataset: FOLIO
448	      c0: 0.4
449	      gap_pp: 4.4
450	    - model: 14B-exp
451	      dataset: PW-D5
452	      c0: 0.3
453	      gap_pp: 0.2
454	    - model: 7B
455	      dataset: FOLIO
456	      c0: 0.7
457	      gap_pp: 6.7
458	    - model: 7B
459	      dataset: PW
460	      c0: 0.57
461	      gap_pp: 3.3
462	    - model: 72B
463	      dataset: FOLIO
464	      c0: 0.33
465	      gap_pp: 3.3
466	    - model: 72B
467	      dataset: PW
468	      c0: 0.27
469	      gap_pp: 0.0
470	    - model: QwQ
471	      dataset: AIME
472	      c0: 0.0
473	      gap_pp: 0.0
474	    - model: QwQ
475	      dataset: PW
476	      c0: 0.19
477	      gap_pp: 0.0
478	    - model: QwQ
479	      dataset: FOLIO
480	      c0: 0.0
481	      gap_pp: 0.0
482	    r_squared: 0.52
483	    spearman_rho: 0.78
484	    spearman_p: 0.001
485	    pearson_r: 0.72
486	    empirical_c0_threshold: 0.25
487	    mean_gap_above_threshold_pp: 3.1
488	    mean_gap_below_threshold_pp: 0.15
489	  result_rationale: 'R²=0.52：C0 解释约一半的 gap 方差。散点正相关但有明显结构：
490	
491	    (1) 14B K ablation 5 点形成 "水平带"（C0 0.47-0.58 但 gap 仅 1.7/3.3）， 因为 60 题粒度和 tie frequency（非
492	    C0）驱动 gap，拉低 R²。
493	
494	    (2) QwQ 3 点锚定左下角，7B-FOLIO 锚定右上角。去掉 K ablation 后 R²~0.70。
495	
496	    (3) PW 系统性低于 FOLIO（同 C0 下 gap 更低），反映 constraint quality 的 dataset-specific 效应。C0
497	    是 necessary condition 非 sufficient。
498	
499	    Spearman ρ=0.78 > Pearson r=0.72 说明关系单调但非严格线性。 C0=0.25 是 empirical threshold：above
500	    → mean gap 3.1pp，below → 0.15pp。 100% 精度预测 "no-gain" 配置（C0<0.25 全为零增益）。
501	
502	    '
503	  tables:
504	  - name: 'Table 6: C0 Diagnostic — Regression Statistics'
505	    columns:
506	    - Metric
507	    - Value
508	    rows:
509	    - - R²
510	      - 0.52
511	    - - Spearman ρ
512	      - 0.78 (p=0.001)
513	    - - Pearson r
514	      - 0.72
515	    - - Threshold
516	      - 0.25
517	    - - Mean gap above
518	      - 3.1pp
519	    - - Mean gap below
520	      - 0.15pp
521	  figures_description:
522	  - 散点图：X=C0, Y=gap(pp)。Model 用 marker 区分（14B圆/7B△/72B□/QwQ×），dataset 用颜色（FOLIO蓝/PW红/AIME灰）。C0=0.25
523	    虚线分隔。附 regression line + 95% CI band。Paper 核心图。
524	  analysis: 'R²=0.52 不支撑 "C0 is a reliable predictor" 强 claim，故 C0 降级为 supporting
525	    diagnostic。Paper Section 5 开头呈现，framing 为： "C0 correctly identifies configurations
526	    where SICA will NOT help (100% precision on no-gain prediction), but cannot fully
527	    predict gain magnitude。" 将 C0 从 predictor 降级为 negative-case diagnostic 更 defensible。
528	
529	    '
530	- name: sica_72b_awq
531	  plan_id: exp-007
532	  description: 'Qwen2.5-72B-Instruct-AWQ 4-bit 在 60 题上运行。 高 baseline 非 reasoning 模型的
533	    scaling 数据点。
534	
535	    '
536	  expected_results:
537	    model: Qwen2.5-72B-Instruct-AWQ
538	    quantization: AWQ-4bit
539	    n: 60
540	    c0: 0.3
541	    sc_accuracy: 0.783
542	    sica_accuracy: 0.8
543	    gap_pp: 1.7
544	    folio_sc: 0.833
545	    folio_sica: 0.867
546	    folio_gap_pp: 3.3
547	    folio_c0: 0.33
548	    pw_sc: 0.733
549	    pw_sica: 0.733
550	    pw_gap_pp: 0.0
551	    pw_c0: 0.27
552	    bootstrap_p: 0.31
553	    tie_fraction: 0.05
554	    tie_count: 3
555	    tiebreak_win_rate: 0.667
556	    vram_usage_gb: ~52
557	    wall_time_hours: ~3.5
558	  result_rationale: '72B（即使 4-bit 量化）推理能力显著强于 14B：
559	
560	    (1) Baseline 更高（SC 78.3% vs 70.0%）：大多数 trace 收敛到正确答案， C0 从 0.53 降至 0.30，tie 仅
561	    3 题。
562	
563	    (2) PW gap 再次为 0pp：72B 在 PW 上 C0 更低（0.27）， 且 constraint 质量问题是任务结构固有特征（与模型大小无关）。
564	
565	    (3) FOLIO +3.3pp（+1/30 题）：仍有少量 tie，SICA 赢 1 题。 绝对值小于 14B 的 FOLIO gap，符合 "更强模型
566	    → 更少 diversity → 更小 gain"。
567	
568	    72B 在 scaling 叙事中填补 14B 与 QwQ 之间的空白：instruction model 的 SICA gain 随能力递减但仍非零（vs
569	    reasoning model 严格零）。 4-bit 量化可能轻微增加 output variance（量化噪声），使 C0 略偏高—— 对 SICA gain
570	    是 conservative estimate。
571	
572	    '
573	  tables:
574	  - name: 'Table 4 row: 72B-AWQ'
575	    columns:
576	    - Model
577	    - N
578	    - C0
579	    - SC
580	    - SICA
581	    - Gap
582	    - p
583	    rows:
584	    - - Qwen2.5-72B-AWQ
585	      - 60
586	      - 0.3
587	      - 78.3%
588	      - 80.0%
589	      - '+1.7'
590	      - 0.31
591	  figures_description:
592	  - 纳入 Table 4 汇总表和 C0-gap 散点图，不单独出图。
593	  analysis: '与 7B/14B/QwQ 并列于 Table 4 形成完整 scaling 序列： 7B(C0=0.63,+5.0) → 14B(0.53,+3.3)
594	    → 72B(0.30,+1.7) → QwQ(0.04,+0.0)。 Section 4.4 核心证据。p=0.31 不显著但无需独立显著性—— 角色是 scaling
595	    trend 数据点。
596	
597	    '
598	- name: constraint_quality_case_studies
599	  plan_id: exp-008
600	  description: '5-10 道代表性题目的 constraint 定性分析。 Constraints 语义是否有意义？排除的 constraints
601	    是否对应推理错误？
602	
603	    '
604	  expected_results:
605	    total_cases: 10
606	    folio_cases: 5
607	    pw_cases: 5
608	    folio_constraint_precision: 0.78
609	    pw_constraint_precision: 0.41
610	    folio_exclusion_correct_rate: 0.82
611	    pw_exclusion_correct_rate: 0.53
612	    key_findings:
613	    - FOLIO constraints 与 FOL ground truth 高度对齐（~78%），排除的 82% 对应实际推理错误
614	    - PW constraints 多为 tautological（'if A then A'）或 over-general（'all entities have
615	      properties'），仅 41% discriminative
616	    - PW exclusion 几乎随机（53%），因 tautological constraints 的 satisfied/violated 与答案正确性无关
617	    - FOLIO SICA 翻转 case：错误 trace 的 contradictory constraints 被排除，正确 trace 获更高权重
618	    - PW D5 failure case：5 步链产出 12 constraints，8 个是中间步骤 trivial restatement
619	  result_rationale: 'FOLIO 高精度（78%）源于任务-方法对齐：FOLIO 要求 FOL 推理，模型 trace 自然产出 类 FOL 语句，LLM-based
620	    FOL extraction 能准确捕获。排除 constraints 中 82% 对应推理错误说明 MAX-SAT satisfiability checking
621	    在 FOLIO 上是有效错误检测器。
622	
623	    PW 低精度（41%）揭示结构性局限：closed-world assumption 推理（"not stated → false"） 难以被标准 FOL
624	    constraints 捕获。模型 PW trace 更像 if-then 规则机械应用 而非 FOL 推导，提取为低信息量 tautologies。MAX-SAT
625	    在这些 constraints 上 判断几乎随机（53%），解释 PW C0>0 但 gap≈0。
626	
627	    定性分析为 "C0 necessary but not sufficient" 提供 mechanistic 解释。
628	
629	    '
630	  tables: []
631	  figures_description:
632	  - 并排 case study：FOLIO（左）和 PW（右），各展示原题/trace 摘要/constraints（标注 correct/incorrect/tautological）/MAX-SAT
633	    结果。FOLIO 展示有效 weighting，PW 展示 non-discriminative 本质。
634	  analysis: '回答 "are constraints meaningful?" 质疑。FOLIO/PW 对比直接解释 为何同方法在不同 dataset
635	    表现迥异——constraint extraction 质量是 dataset-dependent 特性。Paper Section 5.2 或 Appendix。
636	
637	    '
638	- name: overhead_analysis
639	  plan_id: exp-009
640	  description: 'Wall-time 分解：generation / constraint extraction / MaxSAT solving。
641	    回应 "is the overhead worth it"。
642	
643	    '
644	  expected_results:
645	    source: exp-001 (804 questions)
646	    total_wall_time_hours: 14.2
647	    avg_per_question_s: 63.6
648	    breakdown:
649	      generation:
650	        pct: 87.3
651	        avg_s: 55.5
652	        shared_with_sc: true
653	      extraction:
654	        pct: 9.8
655	        avg_s: 6.2
656	        shared_with_sc: false
657	      maxsat:
658	        pct: 0.4
659	        avg_s: 0.25
660	        shared_with_sc: false
661	      io_preprocess:
662	        pct: 2.5
663	        avg_s: 1.6
664	        shared_with_sc: partial
665	    marginal_overhead_vs_sc_pct: 12.7
666	    marginal_overhead_per_question_s: 8.1
667	    sc_equivalent_time_hours: 12.6
668	    maxsat_p99_s: 0.8
669	    maxsat_worst_case_s: 2.3
670	  result_rationale: 'Generation（K=12 traces）占 87.3%，这是 SICA 与 SC 共享成本——SC 同样需要 K 条
671	    trace。SICA marginal overhead 仅 12.7%（每题 ~8s），主要来自 constraint extraction（每 trace
672	    1 次短 LLM call，12 次 × ~0.5s）。
673	
674	    MaxSAT solving 可忽略（0.4%，avg 0.25s）：~100 unique constraints 对 Z3 是 trivial 规模。最慢
675	    case 2.3s 出现在 ~300 constraints + 高 contradiction 题。
676	
677	    12.7% overhead 在实际部署中可接受——SC 已跑 K=12 traces 后加 SICA 仅增 ~1.5h（14h total runtime
678	    中）。Trade-off：12.7% 额外计算换 2.3pp macro-average gain（FOLIO 上 4.4pp），high-C0 场景 ROI
679	    为正。
680	
681	    '
682	  tables:
683	  - name: 'Table 7: SICA Computational Overhead'
684	    columns:
685	    - Component
686	    - '%Total'
687	    - Avg/Q
688	    - Shared
689	    rows:
690	    - - Generation
691	      - 87.3%
692	      - 55.5s
693	      - 'Yes'
694	    - - Extraction
695	      - 9.8%
696	      - 6.2s
697	      - 'No'
698	    - - MaxSAT
699	      - 0.4%
700	      - 0.25s
701	      - 'No'
702	    - - I/O
703	      - 2.5%
704	      - 1.6s
705	      - Partial
706	    - - '**Marginal**'
707	      - '**12.7%**'
708	      - '**8.1s**'
709	      - —
710	  figures_description:
711	  - 'Stacked bar 展示 time breakdown。Generation 深蓝占压倒比例，extraction 浅蓝窄段，MaxSAT 红色几乎不可见。Caption:
712	    ''SICA adds only 12.7% marginal overhead.''。'
713	  analysis: 回应 reviewer "is it worth it"。结论："yes, if C0 is high"。 与 C0 diagnostic
714	    结合：practitioners 应先检查 C0（零成本——跑完 SC 数 unique answers）， 再决定是否付 12.7% SICA overhead。Overhead
715	    concern 转化为 C0 diagnostic 卖点。 Paper Section 4.5 或 Appendix B。
716	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0eb73fe-848f-40f7-af65-8f1032c5c9cb",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "5dc58daf-4cfe-479a-9146-d415a2fa79ee",
  "sourceToolAssistantUUID": "b0eb73fe-848f-40f7-af65-8f1032c5c9cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-16T06:20:24.020Z_

Now let me read the constraint_extractor_fixed.py to understand the fix and the scorer module.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5dc58daf-4cfe-479a-9146-d415a2fa79ee",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mFxzFcKDhoCBZGgeYP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ef400ea-58ef-4903-9df9-6ffc82c409f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKSDJ7sEASLBSBcKXNJQpt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15826,
      "cache_read_input_tokens": 72005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15826,
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

_source line 44 · 2026-05-16T06:20:25.913Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QoYQVihiCuNggThWj7QpSG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/constraint_extractor_fixed.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ef400ea-58ef-4903-9df9-6ffc82c409f4",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mFxzFcKDhoCBZGgeYP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef14f5e4-99bb-4d31-8d2e-2b2e0843ab01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKSDJ7sEASLBSBcKXNJQpt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15826,
      "cache_read_input_tokens": 72005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15826,
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

_source line 45 · 2026-05-16T06:20:25.933Z_

<details><summary>↩ Tool result · `toolu_01QoYQVihiCuNggThWj7QpSG`</summary>

````text
1	"""
2	Constraint extractor: extract structured math constraints from LLM reasoning traces.
3	Input: reasoning trace string
4	Output: list of constraint dicts with type, expression, z3_formula, source_step
5	Dependencies: json, re, openai (optional)
6	"""
7	from __future__ import annotations
8	
9	import json
10	import logging
11	import re
12	import time
13	import random
14	from abc import ABC, abstractmethod
15	from concurrent.futures import ThreadPoolExecutor, as_completed
16	from dataclasses import dataclass, field
17	
18	logger = logging.getLogger(__name__)
19	
20	EXTRACTION_PROMPT = '''Extract mathematical constraints from this reasoning trace as a JSON object.
21	
22	Rules:
23	- type: "equation", "inequality", or "predicate"
24	- expression: human-readable, e.g. "x + y == 14"
25	- z3_formula: Python Z3 syntax (==, !=, <, >, +, -, *, /, **)
26	- source_step: step number where the constraint appears
27	- Use variable names from the trace
28	
29	Output ONLY the JSON below, nothing else:
30	{{"constraints": [{{"type": "equation", "expression": "x + y == 14", "z3_formula": "x + y == 14", "source_step": 1}}], "answer": "final_answer", "variables": ["x", "y"]}}
31	
32	Trace:
33	{trace}'''
34	
35	LOGIC_EXTRACTION_PROMPT = '''Extract logical constraints from this reasoning trace about a logic problem.
36	
37	The problem has facts (base assertions), rules (grounded implications), and derived conclusions.
38	Convert each into a Z3 boolean formula.
39	
40	Variable naming:
41	- Unary property: property_entity (e.g., kind_anne, red_charlie, round_fiona)
42	- Binary relation: relation_subject_object (e.g., eats_bear_squirrel, likes_lion_cat)
43	- Use lowercase with underscores only, no spaces or special characters
44	
45	Constraint types:
46	- "fact": a given assertion, e.g., kind_anne == True
47	- "rule": a grounded implication over specific entities, e.g., Implies(kind_anne, nice_anne)
48	- "derived": an inferred conclusion from facts + rules, e.g., nice_anne == True
49	
50	Z3 operators:
51	- Implies(a, b) for if-then rules
52	- And(a, b, ...) for conjunctive conditions
53	- Or(a, b, ...) for disjunctive conditions
54	- Not(a) for negation
55	- == True / == False for boolean assertions
56	
57	Output ONLY the JSON below, nothing else:
58	{{"constraints": [{{"type": "fact", "expression": "kind(anne)", "z3_formula": "kind_anne == True", "source_step": 1}}], "answer": "True or False or Unknown", "variables": ["kind_anne"]}}
59	
60	Example 1:
61	Trace: "Anne is kind. Kind things are nice. Therefore Anne is nice. The answer is True."
62	Output:
63	{{"constraints": [
64	  {{"type": "fact", "expression": "kind(anne)", "z3_formula": "kind_anne == True", "source_step": 1}},
65	  {{"type": "rule", "expression": "kind(X) -> nice(X)", "z3_formula": "Implies(kind_anne, nice_anne)", "source_step": 2}},
66	  {{"type": "derived", "expression": "nice(anne)", "z3_formula": "nice_anne == True", "source_step": 3}}
67	], "answer": "True", "variables": ["kind_anne", "nice_anne"]}}
68	
69	Example 2:
70	Trace: "The bear eats the squirrel. If someone eats the squirrel then the squirrel is red. So the squirrel is red. The answer is True."
71	Output:
72	{{"constraints": [
73	  {{"type": "fact", "expression": "eats(bear, squirrel)", "z3_formula": "eats_bear_squirrel == True", "source_step": 1}},
74	  {{"type": "rule", "expression": "eats(X, squirrel) -> red(squirrel)", "z3_formula": "Implies(eats_bear_squirrel, red_squirrel)", "source_step": 2}},
75	  {{"type": "derived", "expression": "red(squirrel)", "z3_formula": "red_squirrel == True", "source_step": 3}}
76	], "answer": "True", "variables": ["eats_bear_squirrel", "red_squirrel"]}}
77	
78	Example 3 (multi-condition rule):
79	Trace: "Gary is big. Gary is quiet. Big things are smart. Quiet, cold things are white. Gary is smart. But Gary is not cold. So we cannot determine if Gary is furry. The answer is Unknown."
80	Output:
81	{{"constraints": [
82	  {{"type": "fact", "expression": "big(gary)", "z3_formula": "big_gary == True", "source_step": 1}},
83	  {{"type": "fact", "expression": "quiet(gary)", "z3_formula": "quiet_gary == True", "source_step": 2}},
84	  {{"type": "rule", "expression": "big(X) -> smart(X)", "z3_formula": "Implies(big_gary, smart_gary)", "source_step": 3}},
85	  {{"type": "rule", "expression": "quiet(X) & cold(X) -> white(X)", "z3_formula": "Implies(And(quiet_gary, cold_gary), white_gary)", "source_step": 4}},
86	  {{"type": "derived", "expression": "smart(gary)", "z3_formula": "smart_gary == True", "source_step": 5}}
87	], "answer": "Unknown", "variables": ["big_gary", "quiet_gary", "smart_gary", "cold_gary", "white_gary"]}}
88	
89	Trace:
90	{trace}'''
91	
92	_MATH_TYPES = {"equation", "inequality", "predicate"}
93	_LOGIC_TYPES = {"fact", "rule", "derived"}
94	
95	
96	
97	def _retry_with_backoff(func, max_retries=2, base_delay=0.5):
98	    for attempt in range(max_retries + 1):
99	        try:
100	            return func()
101	        except Exception as e:
102	            if attempt == max_retries:
103	                raise
104	            delay = base_delay * (2 ** attempt) + random.uniform(0, 0.5)
105	            logger.warning("Retry %d/%d after %.1fs: %s", attempt + 1, max_retries, delay, e)
106	            time.sleep(delay)
107	
108	
109	class LLMBackend(ABC):
110	    """LLM abstract base class"""
111	    @abstractmethod
112	    def call(self, prompt: str) -> str:
113	        ...
114	
115	
116	class VLLMBackend(LLMBackend):
117	    """OpenAI-compatible API backend for local vLLM"""
118	
119	    def __init__(self, base_url: str = "http://localhost:8000/v1", model: str | None = None,
120	                 max_tokens: int = 4096):
121	        from openai import OpenAI
122	        self.client = OpenAI(base_url=base_url, api_key="[REDACTED]")
123	        self.max_tokens = max_tokens
124	        if model is None:
125	            models = self.client.models.list()
126	            self.model = models.data[0].id
127	        else:
128	            self.model = model
129	
130	    def call(self, prompt: str) -> str:
131	        return _retry_with_backoff(lambda: self.client.chat.completions.create(
132	            model=self.model,
133	            messages=[{"role": "user", "content": prompt}],
134	            temperature=0.3,
135	            max_tokens=self.max_tokens,
136	        ).choices[0].message.content or "")
137	
138	    def batch_call(self, prompts: list[str], max_workers: int = 4) -> list[str]:
139	        results = [None] * len(prompts)
140	        with ThreadPoolExecutor(max_workers=max_workers) as executor:
141	            future_to_idx = {executor.submit(self.call, p): i for i, p in enumerate(prompts)}
142	            for future in as_completed(future_to_idx):
143	                idx = future_to_idx[future]
144	                try:
145	                    results[idx] = future.result()
146	                except Exception as e:
147	                    logger.error("Extraction %d failed: %s", idx, e)
148	                    results[idx] = ""
149	        return results
150	
151	
152	class MockLLM(LLMBackend):
153	    """Returns pre-set responses for testing."""
154	
155	    def __init__(self, responses: list[str] | None = None, domain: str = "math"):
156	        self._responses = responses or []
157	        self._idx = 0
158	        self._domain = domain
159	
160	    def call(self, prompt: str) -> str:
161	        if self._responses:
162	            resp = self._responses[self._idx % len(self._responses)]
163	            self._idx += 1
164	            return resp
165	        if self._domain == "logic":
166	            return json.dumps({"constraints": [
167	                {"type": "fact", "expression": "kind(anne)", "z3_formula": "kind_anne == True", "source_step": 1},
168	                {"type": "rule", "expression": "kind(X) -> nice(X)", "z3_formula": "Implies(kind_anne, nice_anne)", "source_step": 2},
169	                {"type": "derived", "expression": "nice(anne)", "z3_formula": "nice_anne == True", "source_step": 3},
170	            ], "answer": "True", "variables": ["kind_anne", "nice_anne"]})
171	        return json.dumps({"constraints": [
172	            {"type": "equation", "expression": "x - 7", "z3_formula": "x == 7", "source_step": 1},
173	            {"type": "equation", "expression": "x + 5 - 12", "z3_formula": "x + 5 == 12", "source_step": 2},
174	        ], "answer": "7", "variables": ["x"]})
175	
176	
177	class APIBasedLLM(LLMBackend):
178	    """LLM backend using OpenAI-compatible API (e.g. vLLM server)."""
179	
180	    def __init__(self, base_url: str = "http://localhost:8000/v1",
181	                 api_key: [REDACTED] = "EMPTY", model: str | None = None,
182	                 temperature: float = 0.1, max_tokens: int = 4096):
183	        import openai
184	        self.client = openai.OpenAI(base_url=base_url, api_key=[REDACTED]
185	        self.temperature = temperature
186	        self.max_tokens = max_tokens
187	        if model:
188	            self.model = model
189	        else:
190	            models = self.client.models.list()
191	            self.model = models.data[0].id
192	
193	    def call(self, prompt: str) -> str:
194	        return _retry_with_backoff(lambda: self.client.chat.completions.create(
195	            model=self.model,
196	            messages=[{"role": "user", "content": prompt}],
197	            temperature=self.temperature,
198	            max_tokens=self.max_tokens,
199	        ).choices[0].message.content or "")
200	
201	    def batch_call(self, prompts: list[str], max_workers: int = 4) -> list[str]:
202	        results = [None] * len(prompts)
203	        with ThreadPoolExecutor(max_workers=max_workers) as executor:
204	            future_to_idx = {executor.submit(self.call, p): i for i, p in enumerate(prompts)}
205	            for future in as_completed(future_to_idx):
206	                idx = future_to_idx[future]
207	                try:
208	                    results[idx] = future.result()
209	                except Exception as e:
210	                    logger.error("Extraction %d failed: %s", idx, e)
211	                    results[idx] = ""
212	        return results
213	
214	
215	@dataclass
216	class ExtractionStats:
217	    success: int = 0
218	    fail_json_parse: int = 0
219	    fail_empty: int = 0
220	    fail_invalid_expr: int = 0
221	
222	    @property
223	    def total_fail(self) -> int:
224	        return self.fail_json_parse + self.fail_empty + self.fail_invalid_expr
225	
226	
227	class ConstraintExtractor:
228	    def __init__(self, llm: LLMBackend | None = None, parse_retries: int = 1,
229	                 domain: str = "math"):
230	        self.llm = llm or MockLLM()
231	        self.stats = ExtractionStats()
232	        self.parse_retries = parse_retries
233	        self.domain = domain
234	
235	    def _build_prompt(self, trace: str) -> str:
236	        template = LOGIC_EXTRACTION_PROMPT if self.domain == "logic" else EXTRACTION_PROMPT
237	        return template.format(trace=trace)
238	
239	    @staticmethod
240	    def _strip_thinking(text: str) -> str:
241	        """Remove &lt;think>...&lt;/think> blocks, handling truncated tags."""
242	        idx = text.find('&lt;/think>')
243	        if idx != -1:
244	            return text[idx + len('&lt;/think>'):].strip()
245	        # Truncated thinking: &lt;think> present but no &lt;/think> — entire output is thinking
246	        idx = text.find('&lt;think>')
247	        if idx != -1:
248	            return ''
249	        return text
250	
251	    @staticmethod
252	    def _extract_json_str(text: str) -> str | None:
253	        """Try multiple strategies to extract a JSON object string."""
254	        # Strategy 1: fenced code block ```json ... ```
255	        m = re.search(r'```(?:json)?\s*(.*?)```', text, re.DOTALL)
256	        if m:
257	            return m.group(1).strip()
258	        # Strategy 2: find outermost { ... } braces
259	        start = text.find('{')
260	        if start != -1:
261	            depth = 0
262	            for i in range(start, len(text)):
263	                if text[i] == '{':
264	                    depth += 1
265	                elif text[i] == '}':
266	                    depth -= 1
267	                    if depth == 0:
268	                        return text[start:i + 1]
269	        return None
270	
271	    @staticmethod
272	    def _repair_json(s: str) -> str:
273	        """Fix common JSON errors from LLMs."""
274	        # Remove trailing commas before } or ]
275	        s = re.sub(r',\s*([}\]])', r'\1', s)
276	        # Replace single quotes with double quotes
277	        s = s.replace("'", '"')
278	        return s
279	
280	    def _parse_response(self, raw: str, trace: str) -> list[dict]:
281	        text = self._strip_thinking(raw.strip())
282	        if not text:
283	            logger.warning("Empty after stripping thinking for trace: %s...", trace[:80])
284	            self.stats.fail_json_parse += 1
285	            return []
286	
287	        json_str = self._extract_json_str(text)
288	        if json_str is None:
289	            logger.warning("No JSON found in response for trace: %s...", trace[:80])
290	            self.stats.fail_json_parse += 1
291	            return []
292	
293	        data = None
294	        try:
295	            data = json.loads(json_str)
296	        except json.JSONDecodeError:
297	            try:
298	                data = json.loads(self._repair_json(json_str))
299	            except json.JSONDecodeError:
300	                logger.warning("JSON parse failed for trace: %s...", trace[:80])
301	                self.stats.fail_json_parse += 1
302	                return []
303	
304	        constraints = data.get("constraints", [])
305	        if not constraints:
306	            self.stats.fail_empty += 1
307	            return []
308	
309	        valid = []
310	        for c in constraints:
311	            if not all(k in c for k in ("type", "expression", "z3_formula", "source_step")):
312	                continue
313	            valid_types = _LOGIC_TYPES if self.domain == "logic" else _MATH_TYPES
314	            if c["type"] not in valid_types:
315	                continue
316	            valid.append(c)
317	
318	        if not valid:
319	            self.stats.fail_invalid_expr += 1
320	            return []
321	
322	        self.stats.success += 1
323	        return valid
324	
325	    def extract(self, trace: str) -> list[dict]:
326	        prompt = self._build_prompt(trace)
327	        for attempt in range(self.parse_retries + 1):
328	            raw = self.llm.call(prompt)
329	            result = self._parse_response(raw, trace)
330	            if result or attempt == self.parse_retries:
331	                return result
332	            logger.info("Re-extracting constraints (attempt %d/%d)", attempt + 1, self.parse_retries)
333	        return []
334	
335	    def extract_batch(self, traces: list[str]) -> list[list[dict]]:
336	        if hasattr(self.llm, 'batch_call'):
337	            prompts = [self._build_prompt(t) for t in traces]
338	            raw_results = self.llm.batch_call(prompts)
339	            return [self._parse_response(raw, trace)
340	                    for raw, trace in zip(raw_results, traces)]
341	        return [self.extract(t) for t in traces]
342	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef14f5e4-99bb-4d31-8d2e-2b2e0843ab01",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "74479b29-a7d2-4d26-8788-5d8ecc205102",
  "sourceToolAssistantUUID": "ef14f5e4-99bb-4d31-8d2e-2b2e0843ab01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-16T06:20:26.142Z_

<details open><summary>🔧 Tool call — Read · `toolu_012oCYMrw78DdhMKbwAE5mm2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/trace_generator.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74479b29-a7d2-4d26-8788-5d8ecc205102",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mFxzFcKDhoCBZGgeYP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f3bc35f-a830-4500-b9df-38c1a7806355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKSDJ7sEASLBSBcKXNJQpt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15826,
      "cache_read_input_tokens": 72005,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15826
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 72005,
          "cache_creation_input_tokens": 15826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15826,
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

_source line 47 · 2026-05-16T06:20:26.156Z_

<details><summary>↩ Tool result · `toolu_012oCYMrw78DdhMKbwAE5mm2`</summary>

```text
1	"""
2	Reasoning trace generator. Supports vLLM API, external API, and mock mode.
3	Input: math problem string, K (number of traces)
4	Output: list of {"trace": str, "answer": str} dicts
5	Dependencies: openai, re, asyncio
6	"""
7	from __future__ import annotations
8	
9	import asyncio
10	import re
11	import logging
12	from abc import ABC, abstractmethod
13	
14	logger = logging.getLogger(__name__)
15	
16	SOLVE_PROMPT = """Solve the following math problem step by step. Show all your reasoning.
17	At the end, put your final answer in \\boxed{{}}.
18	
19	Problem: {problem}"""
20	
21	
22	def extract_boxed_answer(text: str) -> str:
23	    """Extract the last \\boxed{...} content from text."""
24	    matches = re.findall(r'\\boxed\{([^}]*(?:\{[^}]*\}[^}]*)*)\}', text)
25	    return matches[-1].strip() if matches else ""
26	
27	
28	class TraceGenerator(ABC):
29	    @abstractmethod
30	    def generate(self, problem: str, k: int = 12) -> list[dict]:
31	        """Generate K reasoning traces. Returns list of {"trace": str, "answer": str}."""
32	        ...
33	
34	
35	class VLLMGenerator(TraceGenerator):
36	    """vLLM server inference via OpenAI-compatible API with async concurrency."""
37	
38	    def __init__(self, base_url: str = "http://localhost:8000/v1",
39	                 api_key: [REDACTED] = "EMPTY", model: str | None = None,
40	                 temperature: float = 0.7, top_p: float = 0.95,
41	                 max_tokens: int = 4096):
42	        import openai
43	        self.client = openai.OpenAI(base_url=base_url, api_key=[REDACTED]
44	        self.async_client = openai.AsyncOpenAI(base_url=base_url, api_key=[REDACTED]
45	        self.temperature = temperature
46	        self.top_p = top_p
47	        self.max_tokens = max_tokens
48	        if model:
49	            self.model = model
50	        else:
51	            models = self.client.models.list()
52	            self.model = models.data[0].id
53	            logger.info("Auto-detected model: %s", self.model)
54	
55	    def _build_prompt(self, problem: str) -> str:
56	        return SOLVE_PROMPT.format(problem=problem)
57	
58	    async def _generate_single(self, prompt: str, trace_idx: int) -> dict:
59	        response = await self.async_client.chat.completions.create(
60	            model=self.model,
61	            messages=[{"role": "user", "content": prompt}],
62	            temperature=self.temperature,
63	            top_p=self.top_p,
64	            max_tokens=self.max_tokens,
65	        )
66	        text = response.choices[0].message.content or ""
67	        answer = extract_boxed_answer(text)
68	        return {"trace": text, "answer": answer, "trace_idx": trace_idx}
69	
70	    def generate(self, problem: str, k: int = 12) -> list[dict]:
71	        """并发生成 K 条 traces"""
72	        prompt = self._build_prompt(problem)
73	
74	        async def _run():
75	            tasks = [self._generate_single(prompt, i) for i in range(k)]
76	            return await asyncio.gather(*tasks)
77	
78	        try:
79	            loop = asyncio.get_running_loop()
80	            import nest_asyncio
81	            nest_asyncio.apply()
82	            return loop.run_until_complete(_run())
83	        except RuntimeError:
84	            return asyncio.run(_run())
85	
86	
87	class APIGenerator(TraceGenerator):
88	    """Generic OpenAI-compatible API inference."""
89	
90	    def __init__(self, base_url: str, api_key: [REDACTED], model: str,
91	                 temperature: float = 0.7, top_p: float = 0.95,
92	                 max_tokens: int = 4096):
93	        import openai
94	        self.client = openai.OpenAI(base_url=base_url, api_key=[REDACTED]
95	        self.model = model
96	        self.temperature = temperature
97	        self.top_p = top_p
98	        self.max_tokens = max_tokens
99	
100	    def generate(self, problem: str, k: int = 12) -> list[dict]:
101	        prompt = SOLVE_PROMPT.format(problem=problem)
102	        results = []
103	        for i in range(k):
104	            resp = self.client.chat.completions.create(
105	                model=self.model,
106	                messages=[{"role": "user", "content": prompt}],
107	                temperature=self.temperature,
108	                top_p=self.top_p,
109	                max_tokens=self.max_tokens,
110	            )
111	            text = resp.choices[0].message.content or ""
112	            answer = extract_boxed_answer(text)
113	            results.append({"trace": text, "answer": answer, "trace_idx": i})
114	        return results
115	
116	
117	class MockGenerator(TraceGenerator):
118	    """Mock generator for testing. Returns preset traces."""
119	
120	    def __init__(self, preset_traces: list[dict] | None = None):
121	        self._presets = preset_traces
122	
123	    def generate(self, problem: str, k: int = 12) -> list[dict]:
124	        if self._presets:
125	            return [
126	                {**t, "trace_idx": i}
127	                for i, t in enumerate(self._presets[:k])
128	            ]
129	        results = []
130	        for i in range(k):
131	            if i < k // 2:
132	                trace = (f"Step 1: Let x be the answer.\n"
133	                         f"Step 2: From the problem, x + 5 = 12.\n"
134	                         f"Step 3: Therefore x = 7.\n"
135	                         f"The answer is \\boxed{{7}}")
136	                answer = "7"
137	            elif i < k * 3 // 4:
138	                trace = (f"Step 1: Define x as the unknown.\n"
139	                         f"Step 2: We have x + 5 = 12, so x = 7.\n"
140	                         f"Step 3: Check: 7 + 5 = 12. Correct.\n"
141	                         f"The answer is \\boxed{{7}}")
142	                answer = "7"
143	            else:
144	                trace = (f"Step 1: Let x be the value.\n"
145	                         f"Step 2: x + 5 = 13 (misread).\n"
146	                         f"Step 3: x = 8.\n"
147	                         f"The answer is \\boxed{{8}}")
148	                answer = "8"
149	            results.append({"trace": trace, "answer": answer, "trace_idx": i})
150	        return results
151	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f3bc35f-a830-4500-b9df-38c1a7806355",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "f4a97d0a-4986-4ee6-a515-a398372fa91d",
  "sourceToolAssistantUUID": "2f3bc35f-a830-4500-b9df-38c1a7806355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-16T06:20:30.068Z_

Now I have a thorough understanding of the paper, the experimental context, the codebase, and the review context. Let me also check the median paper version for comparison with the "best" scenario presented.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4a97d0a-4986-4ee6-a515-a398372fa91d",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mGPUecMU2pfVMLpMYh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "065b60f3-2875-41e1-8290-116bedbf0f11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F3yqusiQje8oYzad52a5eS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7276,
      "cache_read_input_tokens": 87831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7276,
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

_source line 49 · 2026-05-16T06:20:32.846Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DeponuhJjymtqBVk9oyU83`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/median/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "065b60f3-2875-41e1-8290-116bedbf0f11",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mGPUecMU2pfVMLpMYh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92d82f49-f0cd-44b1-bfb9-faacc26a7c08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F3yqusiQje8oYzad52a5eS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7276,
      "cache_read_input_tokens": 87831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7276,
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

_source line 50 · 2026-05-16T06:20:32.854Z_

<details><summary>↩ Tool result · `toolu_01DeponuhJjymtqBVk9oyU83`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{natbib}
12	\usepackage[colorlinks,citecolor=blue,urlcolor=blue]{hyperref}
13	\usepackage{url}
14	
15	\newcommand{\sica}{\textsc{Sica}}
16	\newcommand{\selfcon}{\textsc{SC}}
17	
18	\title{When Does Symbolic Consensus Help?\\Characterizing the Operating Regime of\\Constraint-Based LLM Aggregation}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	% ============================================================
26	\begin{abstract}
27	Self-Consistency (SC) aggregates multiple LLM reasoning chains via majority voting but discards the logical structure within each chain.
28	We propose \textbf{Symbolic Invariant Consensus Aggregation} (\sica{}), which extracts first-order logic constraints from reasoning traces and resolves answer selection through weighted partial MAX-SAT.
29	Rather than claiming uniform improvement, we ask: \emph{when does symbolic consensus help?}
30	On FOLIO with Qwen2.5-14B-Instruct ($n{=}204$), \sica{} improves accuracy by 4.4 percentage points over SC ($p{=}0.034$), while on ProofWriter-D5 ($n{=}600$) the gain is negligible (+0.2pp), as predicted by low constraint quality on that benchmark.
31	We show that the multi-candidate rate $C_0$ (fraction of questions with $\geq 2$ distinct answers across $K$ samples) governs \sica{}'s effectiveness: $C_0 > 0.25$ yields a mean gain of 3.1pp, while $C_0 < 0.25$ yields near-zero gain (Spearman $\rho{=}0.78$, $p{=}0.001$).
32	Reasoning models such as QwQ-32B exhibit $C_0 \approx 0$, causing \sica{} to provably degenerate to SC, while instruction-tuned models across 7B--72B scales show positive $C_0$ and consistent \sica{} $\geq$ SC.
33	Our results reframe symbolic consensus from a universal accuracy booster to a method with formally characterizable applicability boundaries, and provide practitioners a zero-cost diagnostic ($C_0$) to decide whether symbolic aggregation is warranted.
34	\end{abstract}
35	
36	% ============================================================
37	\section{Introduction}
38	\label{sec:intro}
39	
40	Self-Consistency \citep{wang2023selfconsistency} is the dominant strategy for aggregating multiple reasoning chains from large language models: sample $K$ chains, extract answers, and take a majority vote.
41	While effective, SC treats each chain as an opaque vote, discarding the internal logical structure that distinguishes sound reasoning from plausible-sounding errors.
42	When votes are tied---an event that grows more likely as trace diversity increases---SC resorts to arbitrary resolution rules (random selection, alphabetical order), leaving accuracy to chance.
43	
44	We propose \textbf{Symbolic Invariant Consensus Aggregation} (\sica{}), which opens the black box of each reasoning chain by extracting first-order logic (FOL) constraints and using weighted partial MAX-SAT to find the answer most consistent with the aggregate symbolic evidence.
45	\sica{} shares SC's generation phase ($K$ sampled traces) but replaces the counting step with a structured inference step.
46	
47	A natural question arises: does symbolic consensus \emph{always} help?
48	Our experiments reveal that it does not.
49	The effectiveness of \sica{} is governed by \textbf{trace diversity}---specifically, whether the model produces multiple distinct candidate answers across $K$ samples.
50	We formalize this through the \textbf{multi-candidate rate} $C_0$: the fraction of questions for which at least two distinct answers appear.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92d82f49-f0cd-44b1-bfb9-faacc26a7c08",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "ec7b617e-96c2-4115-a80e-10273f9c5afd",
  "sourceToolAssistantUUID": "92d82f49-f0cd-44b1-bfb9-faacc26a7c08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-16T06:20:36.202Z_

I now have comprehensive knowledge of all relevant materials. Let me now write the review and submit it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec7b617e-96c2-4115-a80e-10273f9c5afd",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mGtQhC8gkKDKFUzk5K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e634b447-379e-4ffe-9965-2fce20aff033",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xWh6c3aRDgetE5tsuBJsY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1286,
      "cache_read_input_tokens": 95107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1286,
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

_source line 52 · 2026-05-16T06:20:36.808Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Getj6h8yvpiRTdGyhs56Ed`</summary>

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
  "parentUuid": "e634b447-379e-4ffe-9965-2fce20aff033",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mGtQhC8gkKDKFUzk5K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "055a2a6e-cd9a-45ef-be3e-d5e7ba47600c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xWh6c3aRDgetE5tsuBJsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1286,
      "cache_read_input_tokens": 95107,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1286
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 95107,
          "cache_creation_input_tokens": 1286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1286,
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

_source line 53 · 2026-05-16T06:20:36.811Z_

<details><summary>↩ Tool result · `toolu_01Getj6h8yvpiRTdGyhs56Ed`</summary>

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
  "parentUuid": "055a2a6e-cd9a-45ef-be3e-d5e7ba47600c",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "039cfa21-1099-47c6-b666-8dce33509ac5",
  "sourceToolAssistantUUID": "055a2a6e-cd9a-45ef-be3e-d5e7ba47600c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-16T06:20:40.127Z_



Now I have all the information needed. Let me compose and submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "039cfa21-1099-47c6-b666-8dce33509ac5",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mHBAm84ayRy5s4aUBY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8497b3f-f789-491b-b734-a2ab0dce5b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2e57Cp7HcLuZSLv7oho1x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 96393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 688,
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

_source line 55 · 2026-05-16T06:22:23.433Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01KLp9FtfkuYbRdrfPVEbLkD`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "tier": "best",
  "dream_id": "dream_20260516T054054",
  "overall_score": "Weak Accept (4/6)",
  "report": "# Review Report — Reviewer R1 (Methodology & Experimental Rigor)\n\n**Paper:** \"Principled Symbolic Consensus Improves LLM Reasoning\" (best tier)\n\n---\n\n## 1. Summary\n\nThe paper introduces SICA, a method that extracts first-order logic (FOL) constraints from multiple LLM reasoning traces and resolves answer selection via weighted partial MAX-SAT, serving as a principled replacement for arbitrary tiebreaking in Self-Consistency (SC). On 804 logic reasoning questions (FOLIO + ProofWriter-D5) with Qwen2.5-14B-Instruct, SICA achieves +3.8pp over SC (p=0.023). The paper's main intellectual contribution is characterizing the \"operating regime\" of symbolic consensus: the multi-candidate rate C0 predicts SICA's effectiveness (r=0.94 across 4 model scales), with reasoning models like QwQ-32B causing SICA to degenerate to SC due to near-zero trace diversity.\n\n---\n\n## 2. Strengths\n\n### Methodology Strengths\n\n**S1. Well-motivated problem formulation.** The paper identifies a genuine and under-studied weakness of SC: arbitrary tiebreaking on tied votes. The shift from \"SICA is universally better\" to \"when does symbolic consensus help?\" is a mature framing that adds credibility. Characterizing applicability boundaries is more valuable than overfitting to headline numbers.\n\n**S2. Technically sound MAX-SAT formulation.** The weighted partial MAX-SAT formulation is principled. Using Z3's Optimize with soft constraints weighted by cross-trace consistency is a reasonable encoding. The per-constraint weight defined as the fraction of co-satisfiable constraints within a trace (Equation 1) provides a clean measure of internal coherence. The code confirms the formulation is implemented correctly: indicator variables with `Implies(ind, formula)` and `add_soft(ind, weight=w)` is textbook weighted partial MAX-SAT.\n\n**S3. Honest negative results elevate the contribution.** The QwQ-32B experiments showing SICA degenerating to SC are presented not as failures but as evidence for the operating regime thesis. This is the right way to handle negative results and significantly strengthens the paper's intellectual contribution.\n\n**S4. C0 as a zero-cost diagnostic is practically useful.** The observation that C0 can be computed from SC's pipeline alone (no additional inference) makes it immediately actionable for practitioners. The proposed workflow (compute C0 first, then decide whether to run SICA) is sensible.\n\n### Experimental Strengths\n\n**S5. Comprehensive experiment coverage.** All 9 experiments from the plan are covered: main results (exp-001), K ablation (exp-002), tiebreak baselines (exp-003), 7B scaling (exp-004), QwQ-32B operating regime (exp-005), C0 diagnostic validation (exp-006), 72B-AWQ (exp-007), qualitative case studies (exp-008), and overhead analysis (exp-009). This is thorough.\n\n**S6. Multi-scale model evaluation.** Testing across 7B, 14B, 72B instruction models plus a 32B reasoning model provides a credible scaling story. The monotonic C0 decrease (68.3% -> 53.3% -> 30.0% -> 3.6%) across the scaling ladder is compelling.\n\n**S7. Fair tiebreak baseline comparison (Table 3).** Including SC-random as a baseline is critical. SICA's +3.2pp advantage over SC-random (the fairest comparison) confirms the gain is not an artifact of a poor default tiebreaker.\n\n**S8. Overhead analysis is transparent.** The 39% (or 12.7% marginal in the median scenario) overhead is honestly reported with a clear breakdown. The observation that MAX-SAT solving is negligible (2.4%) and the bottleneck is constraint extraction (LLM calls) is informative.\n\n---\n\n## 3. Weaknesses\n\n### Methodology Weaknesses\n\n**W1. The MAX-SAT formulation does not actually perform MAX-SAT across competing answers (Critical).** Equations 1-2 describe computing a per-answer aggregate constraint weight, then selecting the answer with the highest total weight. This is NOT solving a single MAX-SAT instance that trades off constraints from competing answers. It is solving (or scoring) each candidate independently and comparing scores. The paper calls this \"MAX-SAT\" but the actual mechanism is closer to weighted constraint counting per candidate. Reviewing the code confirms this: `self.solver.solve(unique_constraints)` is called once on ALL constraints, not per-candidate. The `scorer.score()` function then redistributes the MAX-SAT result across candidates. This conflation of \"MAX-SAT solving\" with \"weighted scoring after MAX-SAT\" should be clarified. The theoretical motivation for MAX-SAT (finding the optimal satisfiable subset under contradictions) is weakened if the actual discriminative mechanism is aggregate weight comparison.\n\n**W2. Constraint extraction reproducibility is under-specified (Major).** The paper states constraints are extracted by \"prompting the same LLM\" but provides no details on the extraction prompt, the output format expected, or how malformed outputs are handled. The code reveals two very different extraction prompts (EXTRACTION_PROMPT for math, LOGIC_EXTRACTION_PROMPT for logic) with different constraint type taxonomies ({equation, inequality, predicate} vs {fact, rule, derived}). The paper does not mention this domain-specific bifurcation. Additionally, the extraction prompt instructs the model to output Z3-compatible Python expressions directly, which is a strong assumption about the LLM's Z3 knowledge. The 2% extraction failure rate reported in the paper seems optimistically low given the decisions.yaml documents a 54.4% extraction failure rate during development (D014), suggesting significant prompt engineering was needed to reach 2%.\n\n**W3. The weight function (Equation 1) is not what the code implements (Major).** Equation 1 defines w(c_{i,j}) as the fraction of constraints within the same trace that are co-satisfiable with c_{i,j}. This requires O(m^2) pairwise satisfiability checks per trace. However, the code's `ConstraintDeduplicator` simply counts cross-trace frequency (how many traces produce an equivalent constraint), and the `MaxSATSolver` uses this frequency as the weight for `add_soft`. The paper's formula and the code's implementation appear to describe different weighting schemes. This discrepancy needs resolution.\n\n**W4. SICA's effect is mechanistically limited to tiebreaking (Moderate).** The paper acknowledges that \"SICA's effect is concentrated on tied and near-tied questions\" (Section 3.3), and the decisions.yaml (D017) confirms \"all 4 tiebreaks\" account for the entire gain on the 60-question pilot. On 804 questions, 87 ties (10.8%) are the sole source of improvement. SICA never overrides a clear SC majority. This means SICA is essentially an informed tiebreaker, not a \"symbolic consensus\" method that leverages constraint structure to override potentially wrong majorities. The title \"Principled Symbolic Consensus\" overpromises relative to the actual mechanism.\n\n### Experimental Weaknesses\n\n**W5. The C0 regression (r=0.94, R^2=0.88) is based on only 8 data points with limited independence (Major).** Five of the 8 points come from the same model (14B) at different K values. These points are not independent: they share the same underlying question set, model, and temperature. The remaining 3 points are from different models but on only 60 questions. Furthermore, comparing the \"best\" tier (r=0.94, R^2=0.88) with the \"median\" tier (rho=0.78, R^2=0.52) in the review context reveals that the strong linear relationship is scenario-dependent. The median scenario's R^2=0.52 is far more modest and would not support the strong \"C0 predicts SICA effectiveness\" claim. The paper should present the 14-point analysis (median) rather than the cherry-picked 8-point analysis.\n\n**W6. Statistical power on the K ablation and scaling experiments is very low (Major).** The K ablation and model scaling experiments use only 60 questions. With 60 binary-outcome questions, the minimum detectable effect at 80% power and alpha=0.05 is approximately 12-15pp. None of the reported gaps (1.7-6.7pp) would be individually significant. The paper reports no p-values for any of the 60-question experiments (K ablation Table 4, scaling Table 5), which obscures this issue. The gap values (1.7pp = 1 question, 3.3pp = 2 questions, 5.0pp = 3 questions, 6.7pp = 4 questions on N=60) are extremely granular and could easily be noise.\n\n**W7. ProofWriter contributes 75% of the data but shows negligible improvement (Moderate).** ProofWriter (600/804 = 74.6% of questions) shows +1.8pp (p=0.11), not individually significant. The \"combined\" p=0.023 is heavily influenced by the FOLIO signal. The paper should more prominently discuss that SICA's demonstrated benefit is primarily on FOLIO-type tasks where the constraint extraction naturally aligns with the task's FOL structure, rather than claiming broad logical reasoning improvement.\n\n**W8. Single model family (Qwen2.5) limits generalizability (Moderate).** All experiments use Qwen2.5 variants (7B/14B/72B instruction + QwQ-32B reasoning). The decisions.yaml (D021) acknowledges this as a \"致命弱点\" (fatal weakness) and planned Mistral/LLaMA/DeepSeek experiments, but these are not in the paper. The C0-gap relationship could be Qwen-specific (e.g., Qwen's particular FOL competence in constraint extraction).\n\n**W9. No comparison with other symbolic/neuro-symbolic baselines (Moderate).** The literature map identifies Logic-LM (Pan et al., 2023), DyLoS (Xu et al., 2026), FoVer (2025), and Aristotle (2025) as closely related methods evaluated on the same benchmarks (FOLIO, ProofWriter). None are compared against. Even if these methods solve a slightly different problem (single-path vs. multi-path), their absolute accuracy numbers on FOLIO/PW would contextualize SICA's results.\n\n**W10. The qualitative analysis (Section 5.2) covers only 8 cases with no systematic evaluation of constraint quality (Minor).** The paper reports 2% extraction failure rate and 3.1% MAX-SAT exclusion rate but provides no systematic assessment of constraint semantic correctness. The median review context suggests FOLIO constraint precision is ~78% and PW precision is ~41%, which would be very informative to include.\n\n---\n\n## 4. Questions for Authors\n\n**Q1.** Can you clarify the discrepancy between the weight function in Equation 1 (intra-trace co-satisfiability) and the implementation (cross-trace frequency)? Which one was actually used in the reported experiments?\n\n**Q2.** The paper states the MAX-SAT formulation selects the answer maximizing satisfied constraint weight (Equation 2). Is this computed by solving a separate MAX-SAT instance per candidate answer, or by solving one global instance and then partitioning the result? The code suggests the latter, but the paper's description is ambiguous.\n\n**Q3.** On the 87 tied questions, how many had exactly 2 candidates versus 3+ candidates? For 2-candidate ties, SICA's 75.9% win rate means it selected the correct answer ~66/87 times. What is the baseline accuracy of simply selecting the answer whose supporting traces have longer/more detailed reasoning (a simpler heuristic that also leverages trace content)?\n\n**Q4.** The K ablation shows SC accuracy is constant at 70.0% for K=6,8,12,16 (Table 4). This seems unlikely -- with different K values, the majority vote should fluctuate. Were the same base traces reused (sampling K from a pool of 20), or were fresh traces generated for each K?\n\n**Q5.** For the C0 analysis, what happens if you regress gap on tie frequency instead of C0? Since SICA's mechanism is tiebreaking, tie frequency seems like the more direct causal variable. C0 may be a proxy.\n\n**Q6.** The development history (decisions.yaml) reveals that the original experiments on QwQ-32B with MATH/AIME domains showed structural failures (0pp gap, parser bugs, 54% extraction failure rate), leading to a pivot to logic domains and the 14B model. How much of the final experimental design was informed by preliminary results on the same data? Is there a risk of overfitting the evaluation to favorable conditions?\n\n---\n\n## 5. Minor Issues\n\n- The paper lacks a bibliography (\\bibliography{} command is empty). No references are actually compiled.\n- Table 5 (QwQ-32B) shows \"--\" for SC and SICA accuracy without reporting the actual values. Even if they are identical, the absolute accuracy should be reported.\n- The paper claims \"75.9% win rate on tied questions\" but also \"SICA wins 66/87\" in Table 2. 66/87 = 75.86%, but 21/87 = 24.14% for SC. This sums to 100%, implying there are no \"draw\" cases where both methods get the same answer on ties. This should be clarified -- does \"SICA wins\" mean SICA is correct and SC-alphabetical is wrong, or just that SICA is correct?\n- Section 3.2 reports \"13.2 constraints per trace\" and \"28.7 unique constraints per question after deduplication.\" With K=12 traces, this means 158.4 raw constraints deduplicated to 28.7 (81.9% reduction). This deduplication rate should be discussed -- is it primarily syntactic or semantic (Z3 equivalence)?\n- The trace generator code uses a math-specific prompt (SOLVE_PROMPT with \\boxed{}) but the paper evaluates on logic tasks (True/False/Unknown answers). The logic-domain trace generation prompt is not shown in the codebase, suggesting it may be separate.\n- Equation 3 (C0 definition) has a notation issue: the inner set {a_i : i = 1,...,K} should be {a_i(q) : i = 1,...,K} to indicate the answers are specific to question q.\n\n---\n\n## 6. Score and Confidence\n\n**Score: 4 (Weak Accept)**\n\nThe paper addresses a real problem (SC tiebreaking), proposes a technically reasonable solution, and -- most valuably -- honestly characterizes when the method works and when it does not. The operating regime analysis with C0 as a diagnostic is a genuine contribution. The experimental coverage is thorough in breadth (9 experiments, 4 model scales).\n\nHowever, the methodology has concerning discrepancies between the paper's formalization and the actual implementation (W1, W3), the C0 regression's strength depends on optimistic assumptions about point independence (W5), the core mechanism is limited to tiebreaking rather than deep symbolic consensus (W4), and generalizability is constrained by the single model family (W8) and the domain-specificity of the constraint extraction approach (W7). The development history suggests significant experimental iteration that may have led to favorable evaluation conditions (Q6).\n\nThe paper would benefit from: (1) aligning the formalization with the implementation, (2) expanding to at least one non-Qwen model family, (3) reporting the 14-point C0 analysis with the more modest R^2, and (4) reframing the contribution more precisely as \"principled tiebreaking via constraint analysis\" rather than \"symbolic consensus.\"\n\n**Confidence: 4 (High)**\n\nI have carefully examined the paper, the implementation code (pipeline.py, constraint_extractor.py, z3_maxsat_patched.py, trace_generator.py), the full experiment plan and review context for both best and median tiers, the development decision log (22 decisions), and the literature map. I have identified specific discrepancies between the paper's claims and the implementation. The main uncertainty is whether the reported numbers are from actual experiments (sica_expanded_14b is still RUNNING per the project overview) or projections.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8497b3f-f789-491b-b734-a2ab0dce5b47",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mHBAm84ayRy5s4aUBY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ec51dbf-574c-4f8b-8882-6f00239a8fe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2e57Cp7HcLuZSLv7oho1x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 96393,
      "output_tokens": 4087,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 688
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4087,
          "cache_read_input_tokens": 96393,
          "cache_creation_input_tokens": 688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 688,
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

_source line 56 · 2026-05-16T06:22:27.405Z_

<details><summary>↩ Tool result · `toolu_01KLp9FtfkuYbRdrfPVEbLkD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/review_report.md\", \"dream_id\": \"dream_20260516T054054\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ec51dbf-574c-4f8b-8882-6f00239a8fe8",
  "isSidechain": true,
  "promptId": "43c43d27-5e3d-499e-b0f2-6b1e26e80f23",
  "agentId": "ac26df3bc4b77c860",
  "type": "user",
  "uuid": "e7642780-614e-47b5-8447-98463cbaa017",
  "sourceToolAssistantUUID": "5ec51dbf-574c-4f8b-8882-6f00239a8fe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-16T06:22:36.413Z_

The review has been submitted. Here is a summary of the key findings:

**Score: 4/6 (Weak Accept), Confidence: 4/5 (High)**

**Core assessment:** The paper addresses a genuine problem (SC tiebreaking) and contributes a useful operating regime analysis with C0 as a zero-cost diagnostic. The experimental coverage is thorough (all 9 planned experiments covered, 4 model scales).

**Critical issues identified:**

1. **Formalization-implementation mismatch (W1, W3):** The weight function in Equation 1 (intra-trace co-satisfiability) differs from the code (cross-trace frequency). The MAX-SAT framing overpromises relative to what is actually a weighted constraint scoring mechanism.

2. **C0 regression inflated (W5):** The r=0.94 claim rests on 8 points, 5 of which are non-independent (same model, different K). The median scenario's R^2=0.52 is far more representative.

3. **Mechanism is tiebreaking only (W4):** SICA never overrides a clear SC majority. The entire gain comes from 87 tied questions (10.8% of data). The title "Symbolic Consensus" overpromises.

4. **Single model family (W8):** All Qwen2.5 variants. The planned Mistral/LLaMA/DeepSeek experiments (D021) are absent.

5. **ProofWriter dominates data but shows no gain (W7):** 75% of questions contribute negligible improvement.

The review was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7642780-614e-47b5-8447-98463cbaa017",
  "isSidechain": true,
  "agentId": "ac26df3bc4b77c860",
  "requestId": "req_011Cb5mRKfDGdpinFF6pmANN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d26f3a3a-73cc-45b7-8c45-8d11fd70f109",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "78f4268f-add9-4f5f-97a8-4d696a1c2e4e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LU59Ljkb1rqFNgdkRFNAoh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4218,
      "cache_read_input_tokens": 97081,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4218
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 435,
          "cache_read_input_tokens": 97081,
          "cache_creation_input_tokens": 4218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4218,
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
