# Research conversation: You are Reviewer 1 (R1) in a peer review for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Rej

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aa9ac48b1a21999a9.jsonl`
- **Structured JSON:** [`157d962b25a57ac3b665.json`](../../sessions/15/157d962b25a57ac3b665.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

54 recorded events

### User

_source line 1 · 2026-05-20T20:12:11.878Z_

You are Reviewer 1 (R1) in a peer review for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus: **Methods and Experiments**.

## Paper Summary
Title: "Self-Healing Benchmarks: RL-Robust Contamination Detection via Differential Item Functioning and Psychometrically Equated Benchmark Regeneration"

The paper proposes a "self-healing benchmark" framework with three components:
1. **DIF-based contamination detection** (§3.1, §4.1-4.2): Uses Differential Item Functioning (ETS C classification based on Mantel-Haenszel Δ_MH) to detect benchmark contamination. Splits models into temporal cohorts (pre-2024 reference vs post-2024 focal). Claims RL-robustness because DIF operates on group-level behavioral patterns (correct/incorrect conditional on ability), not within-model output distributions.
2. **Multi-signal ensemble** (§3.2, §4.3-4.5): Combines DIF + ConStat perturbation + DVD generation variance. Weighted fusion (0.45/0.30/0.25) achieves 87% TPR full-spectrum.
3. **Bifactor IRT equating for regeneration** (§3.3, §4.7-4.10): Fits bifactor model on MMLU (general factor + 57 subject factors), selects anchor items, generates replacement items via LLM + student simulation calibration, equates via fixed-parameter calibration.

Additional components: Cumulative Bayesian DIF (§3.4, §4.9), Item-Focused Trees (§4.11), cross-benchmark validation on GSM8K (§4.6), graceful degradation analysis (§4.10).

## Key Experimental Results
- Table 1: DIF on METABENCH MMLU (5,055 models × 12,508 items). TPR=0.78 at δ≥1.4, FPR=0.038.
- Table 2: MMLU-CF external validation. φ=0.42 between DIF flags and CF modification.
- Table 3: DIF vs 10 traditional detectors under RL. DIF degrades 1pp (AUROC 0.91→0.90, p=0.62); traditional methods degrade 6-21pp to near-random.
- Table 4: DIF power retention by RL intensity. Heavy RL retention=0.95.
- Table 5: ConStat TPR=0.68 on non-RL at δ≥0.6, drops to 0.31 on RL.
- Table 6: DVD TPR=0.65 for variant contamination (non-RL), 0.38 for verbatim.
- Table 7: Ensemble weighted fusion TPR=0.87 full-spectrum, AUROC=0.93.
- Table 8: Signal complementarity — DIF unique 28%, ConStat unique 15%, DVD unique 12%.
- Table 9: GSM8K cross-validation: TPR=0.74, Spearman ρ=0.43 with GSM1K gap.
- Table 11: Bifactor model fit: RMSEA=0.028, CFI=0.96, TLI=0.95.
- Table 12: Equating ρ=0.97, classification agreement=0.94, χ² p=0.34.
- Table 13: Student simulation difficulty ρ=0.78 vs prompt targeting ρ=0.28.
- Table 15: Bayesian DIF power doubles over 4 administrations (0.38→0.78 at δ=1.0).
- Table 16: Graceful degradation: ρ≥0.95 up to 20% replacement.
- Table 18: IFT TPR=0.81 at δ≥1.4, +3pp over ETS C.

## Experiment Design Context
The review_context.yaml lists 9 imagined experiments (plan_001 through plan_009). All are fully reflected in the paper (§4.1-§4.11). The paper numbers match the expected results in the YAML almost exactly.

## Your Review Task
Evaluate the paper on:

1. **Methodological soundness**: Is the DIF formulation correct? Is the 2PL IRT model appropriate? Is the ETS C classification well-justified? Is the bifactor equating methodology sound? Are the statistical tests appropriate?

2. **Experimental rigor**: Are the experiments well-designed? Are there confounds? Is the evaluation comprehensive? Are baselines fair? Is the ground truth (MMLU-CF, GSM1K) adequate?

3. **Reproducibility**: Is there enough detail to reproduce? Are hyperparameters specified?

4. **Statistical concerns**: Sample sizes, multiple comparisons, effect size interpretation, p-value usage.

5. **Weaknesses in methods/experiments**: What's missing? What could be stronger?

Produce a structured review with:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, with severity: major/minor)
- Questions for authors
- Detailed comments on specific sections/tables
- Preliminary score (1-6) with confidence (1-5)

Be rigorous but fair. This is a top venue review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "32adbcd7-f7f7-428a-9a8b-76bcc767d3a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T20:12:11.883Z_

```json
{
  "parentUuid": "32adbcd7-f7f7-428a-9a8b-76bcc767d3a5",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
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
  "uuid": "caabee47-68ab-4588-ac2d-0903a1629a1e",
  "timestamp": "2026-05-20T20:12:11.883Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T20:12:14.285Z_



I'll start by reading the paper and the review context to provide a thorough methods/experiments review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caabee47-68ab-4588-ac2d-0903a1629a1e",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERvpLtQ7f717Xz2ses5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37075266-5d5d-4b6e-b7c1-c92fc647734a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011t6ZGwNxTMZ2ZMNEA8YMSS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15524,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15524,
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

_source line 4 · 2026-05-20T20:12:15.169Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DcXku5umpDsb4Bpqj1c6wj`</summary>

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
  "parentUuid": "37075266-5d5d-4b6e-b7c1-c92fc647734a",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERvpLtQ7f717Xz2ses5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e37b9037-4e39-488d-9648-445d299b612d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011t6ZGwNxTMZ2ZMNEA8YMSS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15524,
      "cache_read_input_tokens": 0,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15524
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15524,
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

_source line 5 · 2026-05-20T20:12:15.174Z_

<details><summary>↩ Tool result · `toolu_01DcXku5umpDsb4Bpqj1c6wj`</summary>

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
  "parentUuid": "e37b9037-4e39-488d-9648-445d299b612d",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "2dff20c5-46a5-48ca-a8b3-1e15adffc674",
  "sourceToolAssistantUUID": "e37b9037-4e39-488d-9648-445d299b612d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T20:12:18.124Z_



Let me read the paper, review context, and supporting files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dff20c5-46a5-48ca-a8b3-1e15adffc674",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERw4KGf2LTC2G3oQjzZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6fa7f57-c1e7-4210-a394-0dd3cb3f9dc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWvWb7rsadxzoGMeeuBvX7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
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

_source line 7 · 2026-05-20T20:12:19.149Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01C9iCfZPejvtJqHCdyCM17N`</summary>

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
  "parentUuid": "e6fa7f57-c1e7-4210-a394-0dd3cb3f9dc8",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERw4KGf2LTC2G3oQjzZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1304e5f-8a39-433a-8418-80d9f1d26dc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWvWb7rsadxzoGMeeuBvX7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
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

_source line 8 · 2026-05-20T20:12:19.166Z_

<details><summary>↩ Tool result · `toolu_01C9iCfZPejvtJqHCdyCM17N`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_dif_power_sim_phase2** (success): ETS C 分类在 METABENCH 真实 MMLU 2PL IRT 参数（非理想化分布）下，仍能在 N≥80/group、δ≥1.4 时达到 TPR≥0.65、FPR≤0.10。Phase 1 用合成参数（a~LogNormal, b~N(0,1)）条件性通过，需验证真实参数分布（可能有偏态、聚集、极端值）不会降解检测功效。 ← 基于 mvp_dif_power_sim\\n- **mvp_dif_power_sim** (success): DIF 跨模型批次分析（MH + Logistic Regression）在 N=50-80/group、污染效应量 δ≥1.0 logits 时，对 10% 污染 items 的检测功效 TPR≥0.70 且 FPR≤0.10。这是整个 pipeline 的前提假设——若 DIF 在理想合成数据上都 underpowered，则后续真实数据方案不成立。\\n  [Phase 1 DIF Power Results CSV](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_power_results.csv) | [Phase 1 DIF Power Curves](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/chart/dif_power_curves.pdf) | [DIF Diagnostic P-value Distribution](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/chart/dif_diagnostic_pvalue_dist.pdf) | [DIF Diagnostic TPR Comparison (Raw vs BH vs Bonferroni)](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_diagnostic_tpr_comparison.csv)\\n\\n## 趋势\\n成功 2 / 负向 0 / 失败 0 / 共 2\\nbest_auc_lr: 0.9405 ↓（近 2 次 success）\\nbest_auc_mh: 0.9254 ↓（近 2 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1333, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1304e5f-8a39-433a-8418-80d9f1d26dc7",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "070013df-dd4b-4cf5-b75e-17f55d1eb8c6",
  "sourceToolAssistantUUID": "a1304e5f-8a39-433a-8418-80d9f1d26dc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T20:12:19.358Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01DJB2DyzcH6psL8aAzme4zo`</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "070013df-dd4b-4cf5-b75e-17f55d1eb8c6",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERw4KGf2LTC2G3oQjzZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ea61d67-e07a-4d11-8cbc-2813d98895ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWvWb7rsadxzoGMeeuBvX7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15524,
      "output_tokens": 190,
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
          "output_tokens": 190,
          "cache_read_input_tokens": 15524,
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

_source line 10 · 2026-05-20T20:12:19.386Z_

<details><summary>↩ Tool result · `toolu_01DJB2DyzcH6psL8aAzme4zo`</summary>

```text
{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (2 个)\n\n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **mvp_dif_power_sim_phase2** (success): ETS C 分类在 METABENCH 真实 MMLU 2PL IRT 参数（非理想化分布）下，仍能在 N≥80/group、δ≥1.4 时达到 TPR≥0.65、FPR≤0.10。Phase 1 用合成参数（a~LogNormal, b~N(0,1)）条件性通过，需验证真实参数分布（可能有偏态、聚集、极端值）不会降解检测功效。 ← 基于 mvp_dif_power_sim\n- **mvp_dif_power_sim** (success): DIF 跨模型批次分析（MH + Logistic Regression）在 N=50-80/group、污染效应量 δ≥1.0 logits 时，对 10% 污染 items 的检测功效 TPR≥0.70 且 FPR≤0.10。这是整个 pipeline 的前提假设——若 DIF 在理想合成数据上都 underpowered，则后续真实数据方案不成立。\n  [Phase 1 DIF Power Results CSV](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_power_results.csv) | [Phase 1 DIF Power Curves](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/chart/dif_power_curves.pdf) | [DIF Diagnostic P-value Distribution](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/chart/dif_diagnostic_pvalue_dist.pdf) | [DIF Diagnostic TPR Comparison (Raw vs BH vs Bonferroni)](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_diagnostic_tpr_comparison.csv)\n\n## 趋势\n成功 2 / 负向 0 / 失败 0 / 共 2\nbest_auc_lr: 0.9405 ↓（近 2 次 success）\nbest_auc_mh: 0.9254 ↓（近 2 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\n（无服务器配置）\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ea61d67-e07a-4d11-8cbc-2813d98895ae",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "39715b69-ce52-4292-900f-8f88f993fee4",
  "sourceToolAssistantUUID": "0ea61d67-e07a-4d11-8cbc-2813d98895ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T20:12:22.316Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GU3AWTT8WFhCHnSy7tLY2v`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39715b69-ce52-4292-900f-8f88f993fee4",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERwNHWEr3A8GCJbkyqZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "883b67c4-2636-463a-a219-82709ef25f0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SK1ePQfYGTvFyVCpffbTKx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2065,
      "cache_read_input_tokens": 16974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2065,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
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

_source line 12 · 2026-05-20T20:12:22.326Z_

<details><summary>↩ Tool result · `toolu_01GU3AWTT8WFhCHnSy7tLY2v`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "883b67c4-2636-463a-a219-82709ef25f0c",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "b6d6a24d-33d2-4d3c-aa38-ec5e735f6fa8",
  "sourceToolAssistantUUID": "883b67c4-2636-463a-a219-82709ef25f0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T20:12:23.250Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RgmyJGVei6tiHnExNxhqS5`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6d6a24d-33d2-4d3c-aa38-ec5e735f6fa8",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERwNHWEr3A8GCJbkyqZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18901315-c3b9-4a36-97f7-c2b5e4a718cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SK1ePQfYGTvFyVCpffbTKx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2065,
      "cache_read_input_tokens": 16974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2065,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
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

_source line 14 · 2026-05-20T20:12:23.261Z_

<details><summary>↩ Tool result · `toolu_01RgmyJGVei6tiHnExNxhqS5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/memory.md\", \"content\": \"## MVP 验证关键经验 (2026-05-20)\\n\\n### D001 决策：ETS C 分类 > p-value 检验\\n- **p-value based DIF 检测在 200-item benchmark 上严重 underpowered**：BH 校正后 TPR 仅 0.04-0.07（N=50, δ=1.0）。即使 raw（不校正）TPR 也只有 0.36-0.39，远低于 0.70 目标\\n- **ETS C 分类（|Δ_MH|≥1.5 + 显著性）是可行的替代**：TPR=0.68-0.85 at N≥80, δ≥1.4。本质是 magnitude-based detection，绕过了多重检验问题\\n- **AUC 一直很好（0.91-0.96）**：说明 DIF 统计量的区分能力没问题，问题在假设检验的 threshold，不在信号本身\\n- **原因**：200 个 items 做 BH 校正，需要极小的 p-value 才能过。N=50-100 per group 对 MH/LR 的 per-item 统计功效不够产生 p<0.001 级别的 evidence\\n\\n### Phase 2 验证：真实参数稳健\\n- **PSN-IRT 真实 MMLU 参数** vs 合成参数差异显著：b_mean=-0.84（真实）vs 0.0（合成），即真实 MMLU items 偏容易\\n- 尽管参数分布差异大，ETS C TPR 在真实参数下反而更高（N=100, δ=1.6: 0.80 vs Phase 1 的 0.85）——差异不大，结论稳健\\n- **Phase 2 用了 PSN-IRT 而非 METABENCH**：PSN-IRT 的 item_parameters.csv 可直接使用（14042 items），无需下载 620MB 大包\\n\\n### 关键操作参数\\n- N≥80/group 是最低要求，N≥100 显著改善功效\\n- δ≥1.4 logits 是可靠检测区间，δ=1.0 在边界\\n- MH 5 层 quantile-based 分层 + ETS C 阈值是当前最佳组合\\n- LR 方法与 MH 表现相当，无显著优势\\n\\n## Phase 2 数据源调研 (2026-05-20)\\n\\n### PSN-IRT (AAAI 2026)\\n\\n- **论文全名**: \\\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\\\"\\n- **作者**: Joe-Hall-Lee et al.\\n- **发表**: AAAI 2026 Oral\\n- **GitHub**: https://github.com/Joe-Hall-Lee/PSN-IRT\\n- **IRT 参数公开**: ✅ 是\\n  - `results/item_parameters.csv`: 全部 41,871 items 的 4PL 参数 (a=discrimination, b=difficulty, c=guessing, d=feasibility)\\n  - `results/student_abilities.csv`: 12 个模型的 latent abilities (θ)\\n  - `data/combine.csv`: 12 LLMs × 11 benchmarks 的 binary response matrix\\n- **MMLU 覆盖**: 14,042 items（MMLU 全集）\\n- **模型数**: 仅 12 个\\n- **局限**: 12 个模型太少，IRT 参数估计的可靠性存疑（经典 IRT 通常需要 ≥200 考生）\\n\\n### METABENCH (Kipnis et al., ICLR 2025) ⭐ 推荐\\n\\n- **论文全名**: \\\"metabench — A Sparse Benchmark of Reasoning and Knowledge in Large Language Models\\\"\\n- **GitHub**: https://github.com/adkipnis/metabench\\n- **Zenodo 数据**: https://zenodo.org/records/12819251 (`data.tgz`, 620MB)\\n- **MMLU 覆盖**: 12,508 items\\n- **模型数**: 5,219 个模型（RDS 预处理后）\\n- **优势**: 模型数量充足（5000+），IRT 估计可靠\\n\\n### 数据规模对比\\n\\n| 数据源 | 模型数 | MMLU items | IRT 参数 | 获取难度 |\\n|--------|--------|------------|----------|----------|\\n| **METABENCH** | 5,219 | 12,508 | 2PL (预拟合) | ⭐ 低 |\\n| **PSN-IRT** | 12 | 14,042 | 4PL (PSN) | ⭐ 低 |\\n| **Open LLM LB v1** | ~数千 | ~14,042 | 无 | 中 |\\n\\n## METABENCH 数据探索关键发现 (2026-05-20)\\n\\n### RDS 预拟合 IRT 参数\\n- `mmlu-preproc.rds` 包含 **12,508 items 的 2PL IRT 参数** (difficulty, discrimination)\\n- Difficulty range: [0.008, 0.689], mean=0.444; Discrimination range: [-0.551, 0.291], mean=0.076\\n- 1,926 items (15.4%) 有负区分度\\n- 258 floor items (p<0.05), 0 ceiling items (p>0.95)\\n- **可直接使用，无需自行拟合 IRT**\\n\\n### 响应矩阵 & Train/Test Split\\n- 完整 5219×12508 响应矩阵在 RDS 中\\n- 预建 train/test split: 4,755 train / 464 test models\\n\\n### Cohort 可行性\\n- 通过模型名正则分类：仅 1,929/5,219 (37%) 可归类到已知 family\\n- **2 个年度 cohort 满足 N≥80**: 2023 (N=1,253), 2024 (N=658)\\n- 63% 模型无法从名称分类（社区微调/合并模型）\\n- **结论**: 粗粒度 2-cohort (2023 vs 2024) 可行；细粒度年度 cohort 需外部元数据\\n\\n### RL-trained 模型\\n- **477 个模型**名称含 RL/alignment 信号: DPO(346), ORPO(52), PPO(11), KTO(6)\\n- 大量隐式 RLHF 模型（Llama-3, Qwen-2 等）名称不含标记\\n- **结论**: RL 模型充足，可用于污染检测 validation\\n\\n### 模型准确率分布\\n- Mean=0.592, Std=0.160, Range=[0.218, 0.911]\\n- 366 (7%) 模型低于随机水平 (0.25)\\n- Top families: mistral-0.1 (400), llama-3 (308), llama-2 (161)\\n\\n### CSV vs RDS 差异\\n- CSV: 5,227 模型; RDS: 5,219 模型（8 个被预处理过滤）\\n- 每个 subject 的模型数在 5,225-5,227 之间（近完整覆盖）\\n\", \"total_chars\": 3288, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18901315-c3b9-4a36-97f7-c2b5e4a718cc",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "a8bac900-8d20-46ea-814d-b9fffe5eaa39",
  "sourceToolAssistantUUID": "18901315-c3b9-4a36-97f7-c2b5e4a718cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T20:12:23.710Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01U3R1EPkGy5zv7ebVViSe9f`</summary>

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
  "parentUuid": "a8bac900-8d20-46ea-814d-b9fffe5eaa39",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERwNHWEr3A8GCJbkyqZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fbad740-792d-4363-8f6c-55d4850ee8f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SK1ePQfYGTvFyVCpffbTKx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2065,
      "cache_read_input_tokens": 16974,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2065
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 301,
          "cache_read_input_tokens": 16974,
          "cache_creation_input_tokens": 2065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2065,
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

_source line 16 · 2026-05-20T20:12:23.721Z_

<details><summary>↩ Tool result · `toolu_01U3R1EPkGy5zv7ebVViSe9f`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ROADMAP.md\", \"content\": \"# irt_equated_bench_regen — Research Dashboard\\n\\n> 最后更新: 2026-05-20 19:43 UTC | 更新原因: BE 重启恢复：更新 Dream ID + plan_003 拆分为 003a/003b/003c + METABENCH 下载状态\\n\\n## 核心方向\\n用 DIF 跨模型发布批次检测 benchmark 污染（RL-robust），结合多信号 ensemble 和 bifactor IRT equating 实现 benchmark 自愈。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 已通过 D002，2026-05-20）\\n- **Framing**: 3 条 Core Claims（Detection / Ensemble / Regeneration）\\n- **Plan**: 11 个实验（P0×5 / P1×3 / P2×3），总 GPU 预估 600h\\n- **Dream**: dream_20260520T194223 pending（full review，原 dream 因 BE 重启崩溃后自动重跑）\\n- **服务器/GPU**: 未配置（等 Dream 通过后配置）\\n- **文献图谱**: 10 篇，待蒸馏\\n\\n## Core Claims (from paper_framing.md)\\n1. **Detection**: DIF + ETS C 在 N≥80, δ≥1.4 时 TPR=0.72-0.85, FPR<0.05，RL-robust\\n2. **Ensemble**: DIF + ConStat + DVD 多信号覆盖全效应量谱\\n3. **Regeneration**: Bifactor IRT equating 实现心理测量等价的 item 替换\\n\\n## Experiment Plan Summary (from experiment_plan.yaml)\\n| ID | Name | Claim | Priority | GPU(h) | Deps |\\n|----|------|-------|----------|--------|------|\\n| plan_001 | real_data_dif_mmlu | 1 | P0 | 0 | - |\\n| plan_002 | rl_robustness_validation | 1 | P0 | 100 | 001 |\\n| plan_003a | constat_perturbation_eval | 2 | P0 | 80 | 001 |\\n| plan_003b | dvd_generation_variance_eval | 2 | P0 | 70 | 001 |\\n| plan_003c | ensemble_fusion | 2 | P0 | 0 | 001,003a,003b |\\n| plan_004 | cross_benchmark_gsm8k | 1 | P1 | 100 | 001 |\\n| plan_005 | bifactor_irt_equating_pilot | 3 | P1 | 50 | 001 |\\n| plan_006 | item_generation_calibration | 3 | P1 | 200 | 005 |\\n| plan_007 | cumulative_bayesian_dif | 1 | P2 | 0 | 001 |\\n| plan_008 | graceful_degradation | 3 | P2 | 0 | 005,006 |\\n| plan_009 | item_focused_trees | 1 | P2 | 0 | 001 |\\n\\n## 近期任务\\n- [ ] 等 Dream 回调（dream_20260520T194223），审查模拟审稿\\n- [ ] METABENCH 数据下载（首次 Worker 失败，Agent 处理中）\\n- [ ] Dream 通过后：配置服务器/GPU，批准 P0 实验\\n- [ ] 用户触发文献蒸馏\\n\\n## GPU 预算\\nP0: 250h | P1: 350h | P2: 0h | 总计 600h（项目预算 900-1200h，留余量）\\n\\n## 投稿目标\\nICLR 2027（~2026年10月 DDL，主目标）| AAAI 2027（2026.07.28）| EACL 2027 ARR August（2026.08.03）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D002 | 2026-05-20 | MVP 通过：DIF+ETS C 在 N≥80,δ≥1.4 下功效达标，推荐 N≥100 为主操作点 | mvp_dif_power_sim, mvp_dif_power_sim_phase2 |\\n| D001 | 2026-05-20 | MVP DIF 检测采用 ETS C 分类（效应量+显著性双阈值）替代 BH 校正 p 值作为主判定 | mvp_dif_power_sim |\\n\\n\\n\\n\", \"total_chars\": 2226, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fbad740-792d-4363-8f6c-55d4850ee8f6",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "c681856f-08ce-4513-b23c-707f08138a9c",
  "sourceToolAssistantUUID": "9fbad740-792d-4363-8f6c-55d4850ee8f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T20:12:26.284Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SnTma3XvESDbcFsXL1qdHL`</summary>

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
  "parentUuid": "c681856f-08ce-4513-b23c-707f08138a9c",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERwgrDRi1cY9JfpEqKZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7627a1db-5ddb-477d-8ea9-4f1cba05d98b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ys5L866XHPZNZWrwBS9nG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4151,
      "cache_read_input_tokens": 19039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4151,
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

_source line 18 · 2026-05-20T20:12:26.294Z_

<details><summary>↩ Tool result · `toolu_01SnTma3XvESDbcFsXL1qdHL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md\", \"content\": \"# Paper Framing — irt_equated_bench_regen\\n\\n## Target Venue\\n- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)\\n- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)\\n- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)\\n\\n## Core Claims (3 条, 可证伪)\\n\\n**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.\\n\\n**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.\\n\\n**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.\\n\\n## Story Spine\\n\\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \\\"Model B outperforms Model A on MMLU,\\\" we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.\\n\\n**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\\n\\n**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates the first self-healing benchmark framework.\\n\\n**Headline result template**: \\\"On MMLU with 5,000+ models spanning 1.5 years of active LLM development (2023–mid 2024), DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026).\\\"\\n\\n## Venue Fit Risks\\n\\n- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ \\\"fairness testing for items\\\").\\n- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: \\\"examinees\\\" → \\\"models\\\", \\\"test items\\\" → \\\"benchmark questions\\\", \\\"DIF\\\" → \\\"item-level contamination signal\\\", \\\"equating\\\" → \\\"score comparability across benchmark versions\\\".\\n- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as \\\"bringing mature psychometric tools to solve an urgent ML problem\\\" rather than \\\"inventing new statistics.\\\"\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"DIF power is only sufficient for large effects (δ≥1.4)\\\"**\\n   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.\\n   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)\\n\\n2. **\\\"Model cohort sample sizes are too small for classical DIF\\\"**\\n   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.\\n   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)\\n\\n3. **\\\"Only validated in simulation\\\"**\\n   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.\\n   - Evidence needed: plan_001, plan_004\\n\\n4. **\\\"Item regeneration quality — how do you ensure replacements measure the same construct?\\\"**\\n   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.\\n   - Evidence needed: plan_005, plan_006\\n\\n5. **\\\"RL robustness is only theoretical — where's the empirical evidence?\\\"**\\n   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.\\n   - Evidence needed: plan_002\\n\\n6. **\\\"Computational cost of the full pipeline\\\"**\\n   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.\\n\", \"total_chars\": 6493, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7627a1db-5ddb-477d-8ea9-4f1cba05d98b",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "a91e59ef-23f6-4b2a-a277-f1d86ca1cabc",
  "sourceToolAssistantUUID": "7627a1db-5ddb-477d-8ea9-4f1cba05d98b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T20:12:27.254Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WsLpRK8A8HTySxn9pgWr88`</summary>

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
  "parentUuid": "a91e59ef-23f6-4b2a-a277-f1d86ca1cabc",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERwgrDRi1cY9JfpEqKZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bb46eb2-f6e1-439a-9eed-a2adbfb67635",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ys5L866XHPZNZWrwBS9nG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4151,
      "cache_read_input_tokens": 19039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4151,
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

_source line 20 · 2026-05-20T20:12:27.264Z_

<details><summary>↩ Tool result · `toolu_01WsLpRK8A8HTySxn9pgWr88`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/decisions.yaml\", \"content\": \"_next_id: 3\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:50 UTC\\n  summary: MVP DIF 检测采用 ETS C 分类（效应量+显著性双阈值）替代 BH 校正 p 值作为主判定标准\\n  rationale: Monte Carlo 模拟显示 BH 校正在 200 items 场景下将 TPR 压缩 40-60%，所有核心条件均 FAIL/GRAY。但\\n    ETS C 分类（|Δ_MH|≥1.5 + 显著性，教育测量 gold standard）在 N≥80, δ≥1.4 时 TPR=0.72-0.85, FPR<0.05，满足\\n    pass criteria。ETS C 是 DIF 领域标准实践（Holland & Thayer 1988），使用效应量阈值比纯 p 值更稳健。操作点 N≥80,\\n    δ≥1.4 与 GSM1K 文档的重度污染效应量吻合。小效应由 ensemble 其他信号覆盖。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'BH-corrected: all FAIL/GRAY; ETS C: PASS at N≥80,δ≥1.4 (TPR=0.72-0.85,\\n      FPR<0.05)'\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:31 UTC\\n  summary: MVP 通过：DIF+ETS C 在 N≥80,δ≥1.4 下功效达标，推荐 N≥100 为主操作点\\n  rationale: Phase 1 合成参数 + Phase 2 真实参数（PSN-IRT）均验证 ETS C TPR≥0.65 at N≥80,δ≥1.4。Phase\\n    2 比 Phase 1 降低 3-6pp 符合预期。N=80,δ=1.4 裕度仅 0.032，推荐 N≥100 为主 claim。数据源为 PSN-IRT\\n    而非 ROADMAP 指定的 METABENCH，research 阶段需用 METABENCH 补充验证。限制：δ<1.0 需 ensemble 其他信号。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'Phase 1 conditional pass: ETS C TPR=0.72-0.85 at N≥80,δ≥1.4'\\n  - exp_id: mvp_dif_power_sim_phase2\\n    role: evidence\\n    result: 'Phase 2 pass: ETS C TPR=0.68-0.80 at N≥80,δ≥1.4 with real MMLU params'\\n  depends_on:\\n  - D001\\n\", \"total_chars\": 1300, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bb46eb2-f6e1-439a-9eed-a2adbfb67635",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "3fc6d94a-4ba9-462e-9709-bd99a8fa33c3",
  "sourceToolAssistantUUID": "3bb46eb2-f6e1-439a-9eed-a2adbfb67635",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T20:12:27.818Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WN8zwAEagPAs1vvM5gAdbd`</summary>

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
  "parentUuid": "3fc6d94a-4ba9-462e-9709-bd99a8fa33c3",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERwgrDRi1cY9JfpEqKZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95ef7bfd-7146-4443-8071-efb9aab5a860",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ys5L866XHPZNZWrwBS9nG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4151,
      "cache_read_input_tokens": 19039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4151,
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

_source line 22 · 2026-05-20T20:12:27.827Z_

<details><summary>↩ Tool result · `toolu_01WN8zwAEagPAs1vvM5gAdbd`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95ef7bfd-7146-4443-8071-efb9aab5a860",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "18585e56-7a2a-436e-ad85-420d8199219b",
  "sourceToolAssistantUUID": "95ef7bfd-7146-4443-8071-efb9aab5a860",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-20T20:12:31.247Z_

Now let me read the experiment plan and the paper itself.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18585e56-7a2a-436e-ad85-420d8199219b",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERx14qTxJiveZMy9or8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca32081e-fc23-47ab-b35e-ed29b30f8876",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Va39Rehno6pJZovbowegGo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3448,
      "cache_read_input_tokens": 23190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3448,
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

_source line 24 · 2026-05-20T20:12:31.961Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01RNDkqeGNKLdFKibtedT6VU`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca32081e-fc23-47ab-b35e-ed29b30f8876",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERx14qTxJiveZMy9or8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "136fe967-8c2b-4375-9cb3-2faa98ec6619",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Va39Rehno6pJZovbowegGo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3448,
      "cache_read_input_tokens": 23190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3448,
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

_source line 25 · 2026-05-20T20:12:31.984Z_

<details><summary>↩ Tool result · `toolu_01RNDkqeGNKLdFKibtedT6VU`</summary>

```text
literature_map.yaml
registry.yaml
decisions.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260520T194223/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194223/median/imagined_experiments.yaml
artifacts/manifest.yaml
artifacts/dream_reports/dream_20260520T194223/worst/imagined_experiments.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260520T194223/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "136fe967-8c2b-4375-9cb3-2faa98ec6619",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "6befe091-d74f-4497-91d2-a098f18efed0",
  "sourceToolAssistantUUID": "136fe967-8c2b-4375-9cb3-2faa98ec6619",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T20:12:32.677Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01BvBC37rtmD3Cvm6muCa64z`</summary>

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
  "parentUuid": "6befe091-d74f-4497-91d2-a098f18efed0",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERx14qTxJiveZMy9or8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54ba17d2-cef0-4787-8077-9466a2748a06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Va39Rehno6pJZovbowegGo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3448,
      "cache_read_input_tokens": 23190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3448,
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

_source line 27 · 2026-05-20T20:12:32.694Z_

<details><summary>↩ Tool result · `toolu_01BvBC37rtmD3Cvm6muCa64z`</summary>

```text
artifacts/dream_reports/dream_20260520T194223/best/paper.tex
artifacts/dream_reports/dream_20260520T194223/median/paper.tex
artifacts/dream_reports/dream_20260520T194223/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54ba17d2-cef0-4787-8077-9466a2748a06",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "7c7560c2-7c71-4660-81c4-9ce5c53bdb41",
  "sourceToolAssistantUUID": "54ba17d2-cef0-4787-8077-9466a2748a06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T20:12:32.950Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01G4GXBXaYJ7NmTKnKyc12y8`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c7560c2-7c71-4660-81c4-9ce5c53bdb41",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERx14qTxJiveZMy9or8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "841a664f-f867-4bc8-b611-7625f922c835",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Va39Rehno6pJZovbowegGo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3448,
      "cache_read_input_tokens": 23190,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3448
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 285,
          "cache_read_input_tokens": 23190,
          "cache_creation_input_tokens": 3448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3448,
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

_source line 29 · 2026-05-20T20:12:32.967Z_

<details><summary>↩ Tool result · `toolu_01G4GXBXaYJ7NmTKnKyc12y8`</summary>

```text
report.md
docs/IDEA_BRIEF.md
ROADMAP.md
artifacts/_project/report/metabench_data_summary.md
artifacts/_project/report/metabench_data_summary_ec3bbf.md
artifacts/metabench_data_summary.md
memory.md
.claude/sessions/reviewer_430cd31d/CLAUDE.md
.claude/sessions/reviewer_430cd31d/AGENTS.md
paper_framing.md
artifacts/dream_reports/dream_20260520T194223/best/paper_framing.md
.claude/sessions/agent_9c4a2fd1/CLAUDE.md
.claude/sessions/agent_9c4a2fd1/AGENTS.md
artifacts/dream_reports/dream_20260520T194223/median/paper_framing.md
.claude/CLAUDE.md
AGENTS.md
.claude/sessions/director_af61c18a/CLAUDE.md
.claude/sessions/director_af61c18a/AGENTS.md
artifacts/dream_reports/dream_20260520T194223/worst/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "841a664f-f867-4bc8-b611-7625f922c835",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "a69c70ed-d288-4707-8ef9-1a92914b315c",
  "sourceToolAssistantUUID": "841a664f-f867-4bc8-b611-7625f922c835",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T20:12:35.597Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BZJVi4iwPXYth6usrED2Do`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a69c70ed-d288-4707-8ef9-1a92914b315c",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERxNnoANxiSCsfXTHX8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5c3bbea-bb4a-4ab2-b380-2c2004790186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015AsHyhJZDcYsfjZzyH7FT5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 832,
      "cache_read_input_tokens": 26638,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 832
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 105,
          "cache_read_input_tokens": 26638,
          "cache_creation_input_tokens": 832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 832,
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

_source line 31 · 2026-05-20T20:12:35.884Z_

<details><summary>↩ Tool result · `toolu_01BZJVi4iwPXYth6usrED2Do`</summary>

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
11	\usepackage{array}
12	\usepackage{tabularx}
13	\usepackage{caption}
14	
15	\title{Self-Healing Benchmarks: RL-Robust Contamination Detection via Differential Item Functioning and Psychometrically Equated Benchmark Regeneration}
16	
17	\author{Anonymous}
18	\date{}
19	
20	\begin{document}
21	\maketitle
22	
23	%======================================================================
24	\begin{abstract}
25	LLM benchmark scores are only meaningful if they reflect genuine ability rather than memorization of test items.
26	Existing contamination detectors rely on within-model output distributions (perplexity, token probabilities, generation variance) that reinforcement learning (RL) training smooths away---Wang et al.\ (ICLR 2026) report 14--20 percentage-point AUROC degradation after $\sim$156 GRPO steps, reducing most methods to near-random.
27	We reframe contamination as a psychometric phenomenon---Differential Item Functioning (DIF)---where contaminated items become differentially easier for exposed model cohorts beyond what latent ability predicts.
28	Because DIF operates on group-level behavioral patterns (correct/incorrect conditional on ability), it is orthogonal to the within-model distribution smoothing that RL performs.
29	On METABENCH MMLU (5,055 models $\times$ 12,508 items), DIF-based ETS~C detection achieves 78--83\% TPR at $<$5\% FPR for large contamination effects ($\delta \ge 1.4$), maintaining 96\% power retention where 10 existing methods degrade to random under RL training.
30	We further propose a multi-signal ensemble combining DIF, ConStat-style perturbation testing, and DVD generation variance that achieves 87\% TPR across the full effect-size spectrum.
31	Finally, we demonstrate that bifactor IRT equating enables psychometrically equivalent benchmark regeneration: replacing flagged items with empirically calibrated alternatives preserves model rankings ($\rho = 0.97$) and score reliability ($\alpha > 0.91$) at up to 20\% replacement rate.
32	Together, these components constitute the first \emph{self-healing benchmark} framework.
33	\end{abstract}
34	
35	%======================================================================
36	\section{Introduction}
37	\label{sec:intro}
38	
39	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume temporal score comparability---that both scores reflect the same latent ability measured under equivalent conditions.
40	Benchmark contamination systematically violates this assumption: models trained on benchmark items receive inflated scores that no longer reflect genuine capability.
41	
42	The problem is worsening.
43	The shift toward RL-trained reasoning models (o1, o3, DeepSeek-R1) introduces a new challenge: RL training conceals contamination signals.
44	Wang et al.\ (ICLR 2026) demonstrate that $\sim$156 GRPO steps reduce 10 reference-free contamination detectors to near-random performance ($\sim$50\% AUROC), because policy optimization smooths the within-model output distributions these methods rely on.
45	As the model ecosystem moves toward RL, existing detection approaches face obsolescence.
46	
47	We observe that contamination is fundamentally a \emph{psychometric} problem.
48	In educational testing, when a test item functions differently for groups of examinees \emph{after controlling for overall ability}, the item exhibits Differential Item Functioning (DIF).
49	Benchmark contamination creates exactly this pattern: a model cohort trained after a benchmark leaked into training data will find contaminated items differentially easier than their latent ability predicts.
50	Crucially, DIF operates on \emph{group-level Item Characteristic Curves} conditional on ability---not on within-model token distributions.
51	RL training cannot eliminate this signal without negating the purpose of contamination itself: a model that memorized an item must still answer it correctly, preserving the behavioral anomaly at the population level.
52	
53	This paper makes three contributions:
54	
55	\begin{enumerate}
56	    \item \textbf{RL-Robust Detection} (\S\ref{sec:exp_dif}--\ref{sec:exp_rl}): DIF-based ETS~C detection achieves 78--83\% TPR with $<$5\% FPR on METABENCH MMLU real data, maintaining 96\% power retention under RL training where 10 traditional detectors degrade by 6--21 percentage points to near-random.
57	
58	    \item \textbf{Full-Spectrum Ensemble} (\S\ref{sec:exp_ensemble}): A multi-signal sentinel combining DIF (large effects, RL-robust), ConStat perturbation testing (non-RL medium effects), and DVD generation variance (variant contamination) achieves 87\% TPR and 0.93 AUROC across the full effect-size and model-type landscape.
59	
60	    \item \textbf{Psychometrically Equated Regeneration} (\S\ref{sec:exp_equating}--\ref{sec:exp_degradation}): Bifactor IRT equating with anchor items enables benchmark regeneration that preserves model rankings ($\rho = 0.97$), score reliability ($\alpha > 0.91$), and construct validity through a formal graceful-degradation framework.
61	\end{enumerate}
62	
63	%======================================================================
64	\section{Related Work}
65	\label{sec:related}
66	
67	\paragraph{Contamination Detection.}
68	Reference-free methods detect contamination from model outputs alone.
69	Min-K\% Prob identifies memorized text via low-probability token ratios.
70	Perplexity-based and compression-based methods (zlib ratio) flag suspiciously fluent outputs.
71	DetectGPT uses curvature in log-probability space.
72	Reference-model approaches compare target model loss against a clean reference.
73	These methods share a common vulnerability: they operate on within-model output distributions that RL training smooths.
74	ConStat (Dekoninck et al., 2024) tests whether model performance degrades under semantically equivalent reformulations, providing FDR-controlled detection but relying on surface-form-specific memorization patterns vulnerable to RL.
75	DVD (Dong et al., 2024) detects variant contamination via generation variance and bimodal response distributions.
76	
77	\paragraph{Benchmark Evolution.}
78	LiveBench updates monthly from recent sources but applies no psychometric calibration across updates, making temporal comparisons unreliable.
79	Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability across tasks, not contamination.
80	No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.
81	
82	\paragraph{Psychometrics in NLP Evaluation.}
83	Item Response Theory has been applied to NLP evaluation for ability estimation and item analysis.
84	Bifactor models have been used in educational testing to separate general from domain-specific factors.
85	DIF analysis is a standard tool in educational measurement for detecting item bias.
86	Our contribution is the novel application of DIF to LLM benchmark contamination, the theoretical and empirical demonstration of its RL-robustness, and integration with bifactor equating for benchmark regeneration.
87	
88	%======================================================================
89	\section{Method}
90	\label{sec:method}
91	
92	\subsection{DIF-Based Contamination Detection}
93	\label{sec:method_dif}
94	
95	Let $U_{ij} \in \{0, 1\}$ denote the binary response of model $i$ on item $j$.
96	Under a 2PL IRT model, the probability of a correct response is:
97	\begin{equation}
98	    P(U_{ij} = 1 \mid \theta_i) = \frac{1}{1 + \exp(-a_j(\theta_i - b_j))}
99	\end{equation}
100	where $\theta_i$ is the latent ability of model $i$, $a_j$ is the item discrimination, and $b_j$ is the item difficulty.
101	
102	DIF occurs when the Item Characteristic Curve (ICC) differs between a \emph{reference group} (e.g., models released before a benchmark was widely available) and a \emph{focal group} (e.g., models released after):
103	\begin{equation}
104	    P(U_{ij} = 1 \mid \theta, G = \text{focal}) \neq P(U_{ij} = 1 \mid \theta, G = \text{ref})
105	\end{equation}
106	for some $\theta$ values, after controlling for overall ability.
107	
108	We use the ETS classification system based on the Mantel-Haenszel $\Delta_\text{MH}$ statistic:
109	\begin{itemize}
110	    \item \textbf{A} (negligible): $|\Delta_\text{MH}| < 1.0$
111	    \item \textbf{B} (moderate): $1.0 \leq |\Delta_\text{MH}| < 1.5$
112	    \item \textbf{C} (large): $|\Delta_\text{MH}| \geq 1.5$
113	\end{itemize}
114	
115	Items classified as ETS~C are flagged as contaminated. This effect-size-based criterion, rather than p-value-based testing, reduces sensitivity to sample size and focuses on practically meaningful contamination.
116	
117	\paragraph{Why DIF is RL-robust.}
118	Traditional detectors operate on within-model output distributions (token probabilities, generation variance).
119	RL training (GRPO/PPO) optimizes the policy to smooth these distributions, eliminating detectable anomalies.
120	DIF, by contrast, compares \emph{group-level behavioral patterns}: ``given the same latent ability $\theta$, does the focal group have higher probability of answering item $j$ correctly?''
121	RL can smooth output token distributions but cannot eliminate the behavioral fact that a model answers a memorized item correctly.
122	The only way to defeat DIF would be for the model to deliberately answer memorized items \emph{incorrectly}---which negates the purpose of contamination.
123	
124	\subsection{Multi-Signal Ensemble}
125	\label{sec:method_ensemble}
126	
127	No single signal covers the full contamination landscape. We combine three complementary detectors:
128	
129	\begin{enumerate}
130	    \item \textbf{DIF (ETS~C)}: Strongest for large effects ($\delta \geq 1.4$) and RL-trained models.
131	    \item \textbf{ConStat perturbation}: Effective for medium effects ($\delta \geq 0.6$) on non-RL models, where surface-form memorization creates detectable performance drops under semantic reformulation.
132	    \item \textbf{DVD generation variance}: Targets variant contamination (partial memorization from exposure to item variants), where bimodal generation distributions emerge.
133	\end{enumerate}
134	
135	We evaluate two fusion strategies: (a) \emph{majority voting} ($\geq$2/3 signals agree) and (b) \emph{weighted fusion} with per-signal weights optimized on a calibration set. Weighted fusion with weights $w_\text{DIF} = 0.45$, $w_\text{ConStat} = 0.30$, $w_\text{DVD} = 0.25$ allows high-confidence single-signal detections to trigger flags, avoiding the over-conservatism of majority voting in regimes where only one signal is active.
136	
137	\subsection{Bifactor IRT Equating for Benchmark Regeneration}
138	\label{sec:method_equating}
139	
140	Given a set of contaminated items, we regenerate the benchmark through three steps:
141	
142	\paragraph{Step 1: Bifactor Model Fitting.}
143	MMLU has a natural bifactor structure: a general cognitive ability factor $g$ plus subject-specific factors $s_k$ ($k = 1, \ldots, K$). We fit a bifactor IRT model:
144	\begin{equation}
145	    P(U_{ij} = 1 \mid \theta_{ig}, \theta_{is_k}) = \frac{1}{1 + \exp(-[a_{jg}\theta_{ig} + a_{js_k}\theta_{is_k} - d_j])}
146	\end{equation}
147	where $a_{jg}$ and $a_{js_k}$ are the general and specific factor loadings.
148	
149	\paragraph{Step 2: Anchor Item Selection.}
150	We select DIF-free items (ETS~A classification, discrimination $a > 0.8$, low missingness) as anchor items. These provide the calibration bridge between original and regenerated benchmark versions.
151	
152	\paragraph{Step 3: Fixed-Parameter Calibration.}
153	Replacement items are generated via LLM and calibrated through student simulation (using a panel of diverse models as simulated examinees). Item parameters are estimated on the anchor item scale through fixed-parameter calibration, ensuring score comparability.
154	
155	\subsection{Cumulative Bayesian DIF}
156	\label{sec:method_bayesian}
157	
158	For medium-effect contamination ($\delta \approx 1.0$) where single-administration power is limited, we implement a Bayesian framework that accumulates evidence across successive model cohorts. The posterior from administration $t$ serves as the prior for administration $t+1$:
159	\begin{equation}
160	    p(\Delta_j \mid \mathbf{D}_{1:t}) \propto p(\mathbf{D}_t \mid \Delta_j) \cdot p(\Delta_j \mid \mathbf{D}_{1:t-1})
161	\end{equation}
162	where $\Delta_j$ is the DIF effect size for item $j$ and $\mathbf{D}_{1:t}$ denotes data from all administrations up to $t$. A Bayes factor threshold of $\text{BF} \geq 3.0$ triggers flagging.
163	
164	%======================================================================
165	\section{Experiments}
166	\label{sec:experiments}
167	
168	\subsection{DIF Detection on METABENCH MMLU Real Data}
169	\label{sec:exp_dif}
170	
171	We apply DIF analysis to the METABENCH MMLU response matrix comprising 5,055 models and 12,508 items. Models are split into temporal cohorts: a reference group of 3,235 pre-2024 models and a focal group of 1,820 post-2024 models. We also evaluate finer annual cohort splits.
172	
173	\begin{table}[h]
174	\centering
175	\caption{DIF Detection Power on METABENCH MMLU Real Data}
176	\label{tab:dif_mmlu}
177	\small
178	\begin{tabular}{lrrcrcc}
179	\toprule
180	Cohort Split & $N_\text{focal}$ & $N_\text{ref}$ & $\delta$ range & TPR & FPR & AUC \\
181	\midrule
182	pre2024 vs post2024 & 1,820 & 3,235 & $\geq 1.4$ & 0.78 & 0.038 & 0.92 \\
183	pre2024 vs post2024 & 1,820 & 3,235 & $\geq 1.6$ & 0.83 & 0.038 & 0.94 \\
184	pre2024 vs post2024 & 1,820 & 3,235 & $\geq 1.0$ & 0.51 & 0.041 & 0.83 \\
185	2022 vs 2024 & 920 & 2,100 & $\geq 1.4$ & 0.76 & 0.036 & 0.91 \\
186	2023 vs 2025 & 680 & 1,340 & $\geq 1.4$ & 0.74 & 0.039 & 0.90 \\
187	Annual (finest) & 92 & 2,100 & $\geq 1.4$ & 0.72 & 0.042 & 0.88 \\
188	\bottomrule
189	\end{tabular}
190	\end{table}
191	
192	ETS~C flags 1,340 items at the C level (10.7\% of MMLU), concentrated in STEM subjects.
193	TPR ranges from 72\% to 83\% depending on cohort granularity and effect-size threshold, while FPR remains consistently below 5\%.
194	Even the finest annual split ($N_\text{focal} = 92$) achieves TPR = 0.72, consistent with simulation predictions at this sample size.
195	Real IRT parameters (mean $a = 1.18$, mean $b = -0.79$) closely match our simulation settings, validating ecological validity.
196	
197	\paragraph{External Validation with MMLU-CF.}
198	We use MMLU-CF as partial ground truth. Among 2,780 items that MMLU-CF modified (indicating suspected contamination vulnerability), 61\% are DIF-flagged. Among 9,728 unmodified items, only 7\% are flagged ($\phi = 0.42$, tetrachoric $r = 0.48$).
199	
200	\begin{table}[h]
201	\centering
202	\caption{MMLU-CF External Validation}
203	\label{tab:mmlu_cf}
204	\small
205	\begin{tabular}{lrcl}
206	\toprule
207	Category & $n$ items & DIF flagged rate & Description \\
208	\midrule
209	CF-modified items & 2,780 & 0.61 & Items changed in MMLU-CF \\
210	CF-unmodified items & 9,728 & 0.07 & Items unchanged in MMLU-CF \\
211	\midrule
212	$\phi$ coefficient & --- & 0.42 & Association between DIF flag \& CF modification \\
213	Tetrachoric $r$ & --- & 0.48 & Latent correlation estimate \\
214	\bottomrule
215	\end{tabular}
216	\end{table}
217	
218	The moderate-to-strong association ($\phi = 0.42$) reflects the partial nature of this ground truth: MMLU-CF's modification strategy does not correspond one-to-one with contamination, making perfect correlation neither expected nor credible.
219	
220	\subsection{RL-Robustness Validation}
221	\label{sec:exp_rl}
222	
223	We evaluate DIF alongside 10 traditional detectors on cohorts including 14 RL-trained models (DeepSeek-R1, QwQ-32B, Skywork-OR1, Eurus-2-PRIME, and others) and 40 SFT-only models.
224	
225	\begin{table}[h]
226	\centering
227	\caption{DIF vs Traditional Detectors Under RL Training}
228	\label{tab:rl_robustness}
229	\small
230	\begin{tabular}{lcccc}
231	\toprule
232	Method & AUROC (SFT) & AUROC (RL) & Degradation (pp) & $p$-value \\
233	\midrule
234	DIF (ETS~C) & 0.91 & 0.90 & 1 & 0.62 \\
235	\midrule
236	Min-K\% & 0.72 & 0.51 & 21 & 0.0002 \\
237	ConStat (perturbation) & 0.68 & 0.53 & 15 & 0.001 \\
238	DVD (gen.\ variance) & 0.65 & 0.54 & 11 & 0.004 \\
239	Perplexity & 0.61 & 0.50 & 11 & 0.003 \\
240	Lowercase & 0.58 & 0.49 & 9 & 0.008 \\
241	zlib ratio & 0.60 & 0.50 & 10 & 0.005 \\
242	Top-K prob & 0.63 & 0.52 & 11 & 0.003 \\
243	Ref-model loss & 0.67 & 0.53 & 14 & 0.002 \\
244	Neighbor text & 0.59 & 0.50 & 9 & 0.007 \\
245	DetectGPT & 0.55 & 0.49 & 6 & 0.040 \\
246	\bottomrule
247	\end{tabular}
248	\end{table}
249	
250	DIF exhibits 1~pp AUROC degradation ($p = 0.62$, not significant), while traditional methods degrade by 6--21~pp to near-random performance (mean AUROC = 0.51). The power retention ratio of DIF is 0.96 ($p = 0.62$ for paired $t$-test of SFT vs RL cohort TPRs), compared to statistically significant degradation for all traditional methods ($p < 0.01$).
251	
252	\begin{table}[h]
253	\centering
254	\caption{DIF Power Retention by RL Training Intensity}
255	\label{tab:rl_intensity}
256	\small
257	\begin{tabular}{lcccr}
258	\toprule
259	Model Group & $n$ & TPR ($\delta \geq 1.4$) & FPR & Retention \\
260	\midrule
261	SFT only & 40 & 0.79 & 0.037 & 1.00 \\
262	Light RL ($<$500 steps) & 6 & 0.78 & 0.039 & 0.99 \\
263	Heavy RL ($>$500 steps) & 8 & 0.75 & 0.041 & 0.95 \\
264	All RL & 14 & 0.76 & 0.041 & 0.96 \\
265	\bottomrule
266	\end{tabular}
267	\end{table}
268	
269	Even heavy RL training ($>$500 optimization steps) reduces DIF power by only 5\% (retention = 0.95), attributable to higher general ability compressing effect-size estimates rather than mechanistic failure.
270	
271	\subsection{ConStat Perturbation Evaluation}
272	\label{sec:exp_constat}
273	
274	We independently evaluate ConStat-style perturbation testing by generating 5 semantically equivalent reformulations (semantic similarity 0.91) for each of 240 MMLU items across 35 models.
275	
276	\begin{table}[h]
277	\centering
278	\caption{ConStat Detection Power by Effect Size and Model Type}
279	\label{tab:constat}
280	\small
281	\begin{tabular}{llrccc}
282	\toprule
283	Model Type & $\delta$ range & $n$ items & TPR & FPR & FDR \\
284	\midrule
285	non-RL & $\geq 0.6$ & 142 & 0.68 & 0.06 & 0.048 \\
286	non-RL & $\geq 1.0$ & 87 & 0.74 & 0.06 & 0.041 \\
287	non-RL & $\geq 1.4$ & 48 & 0.62 & 0.06 & 0.052 \\
288	RL & $\geq 0.6$ & 142 & 0.31 & 0.08 & 0.120 \\
289	RL & $\geq 1.0$ & 87 & 0.38 & 0.08 & 0.100 \\
290	All models & $\geq 0.6$ & 142 & 0.52 & 0.07 & 0.070 \\
291	\bottomrule
292	\end{tabular}
293	\end{table}
294	
295	ConStat achieves TPR = 0.68 on non-RL models at $\delta \geq 0.6$, filling DIF's blind spot in the medium-effect regime.
296	Under RL training, TPR drops to 0.31, consistent with RL smoothing of surface-form memorization.
297	Mean accuracy drop on contaminated items is 0.18 vs 0.03 on clean items under reformulation, confirming the perturbation mechanism.
298	The inverted pattern at $\delta \geq 1.4$ (TPR = 0.62, lower than at $\delta \geq 1.0$) reflects that extremely contaminated items are often intrinsically easy, reducing the reformulation-induced accuracy drop.
299	
300	\subsection{DVD Generation Variance Evaluation}
301	\label{sec:exp_dvd}
302	
303	We evaluate DVD on 12 open-weight models, generating 50 responses per item at temperatures 0.7--1.0 across 2,000 MMLU items.
304	
305	\begin{table}[h]
306	\centering
307	\caption{DVD Detection Power by Contamination Type}
308	\label{tab:dvd}
309	\small
310	\begin{tabular}{llrccc}
311	\toprule
312	Contamination Type & Model Type & $n$ items & TPR & FPR & AUROC \\
313	\midrule
314	Variant & non-RL & 320 & 0.65 & 0.07 & 0.78 \\
315	Verbatim & non-RL & 480 & 0.38 & 0.07 & 0.62 \\
316	All & non-RL & 800 & 0.52 & 0.07 & 0.71 \\
317	Variant & RL & 320 & 0.47 & 0.09 & 0.68 \\
318	Verbatim & RL & 480 & 0.29 & 0.09 & 0.57 \\
319	All & RL & 800 & 0.38 & 0.09 & 0.63 \\
320	\bottomrule
321	\end{tabular}
322	\end{table}
323	
324	DVD is most effective for variant contamination on non-RL models (TPR = 0.65), where partial memorization creates bimodal generation patterns (bimodal detection rate: 0.58 for contaminated vs 0.04 for clean items).
325	Its lower performance on verbatim contamination (TPR = 0.38) is expected: fully memorized items produce consistently confident outputs with low generation variance, eliminating the bimodal signal.
326	This complementarity with DIF (strongest on verbatim large effects) motivates the ensemble design.
327	
328	\subsection{Ensemble Fusion}
329	\label{sec:exp_ensemble}
330	
331	We fuse DIF, ConStat, and DVD signals using both majority voting and weighted fusion strategies.
332	
333	\begin{table}[h]
334	\centering
335	\caption{Ensemble vs Individual Signal Detection Power}
336	\label{tab:ensemble}
337	\small
338	\begin{tabular}{lccccc}
339	\toprule
340	Method & TPR (full) & TPR ($\geq$1.4) & TPR ($\geq$0.6) & FPR & AUROC \\
341	\midrule
342	DIF only & 0.58 & 0.78 & 0.35 & 0.038 & 0.84 \\
343	ConStat only & 0.44 & 0.62 & 0.68 & 0.060 & 0.76 \\
344	DVD only & 0.38 & 0.38 & 0.45 & 0.070 & 0.71 \\
345	Majority (2/3) & 0.72 & 0.81 & 0.64 & 0.040 & 0.89 \\
346	Weighted fusion & \textbf{0.87} & \textbf{0.91} & \textbf{0.78} & 0.080 & \textbf{0.93} \\
347	\bottomrule
348	\end{tabular}
349	\end{table}
350	
351	Weighted fusion achieves 87\% TPR across the full effect-size spectrum---a 29~pp improvement over the best individual signal (DIF at 0.58 full-spectrum).
352	The 15~pp advantage over majority voting reflects the systematic complementarity: in most detection regimes, only 1--2 signals are active, and the 2-of-3 agreement requirement of majority voting filters out valid single-signal detections.
353	
354	\begin{table}[h]
355	\centering
356	\caption{Signal Complementarity Analysis}
357	\label{tab:complementarity}
358	\small
359	\begin{tabular}{lcl}
360	\toprule
361	Detection Source & \% of Total & Primary Regime \\
362	\midrule
363	DIF unique & 28\% & Large effect + RL models \\
364	ConStat unique & 15\% & Medium effect + non-RL \\
365	DVD unique & 12\% & Variant contamination \\
366	DIF $\cap$ ConStat & 8\% & Large effect + non-RL \\
367	DIF $\cap$ DVD & 4\% & Large variant + RL \\
368	ConStat $\cap$ DVD & 2\% & Medium variant + non-RL \\
369	All three & 31\% & Large effect + non-RL + verbatim \\
370	\bottomrule
371	\end{tabular}
372	\end{table}
373	
374	Each signal contributes 12--28\% unique detections that no other signal captures, confirming that no individual signal is dispensable.
375	On RL models, ensemble TPR reaches 0.82 (vs 0.90 on non-RL), with DIF's RL-robustness partially compensating for ConStat's RL-induced degradation.
376	
377	\subsection{Cross-Benchmark Validation on GSM8K}
378	\label{sec:exp_gsm8k}
379	
380	To test generalizability, we replicate DIF analysis on GSM8K (1,319 items, 62 models), using GSM1K---a distribution-matched but entirely novel test set---as independent ground truth.
381	
382	\begin{table}[h]
383	\centering
384	\caption{DIF Detection on GSM8K with GSM1K Ground Truth}
385	\label{tab:gsm8k}
386	\small
387	\begin{tabular}{lr}
388	\toprule
389	Metric & Value \\
390	\midrule
391	Models evaluated & 62 \\
392	Items evaluated & 1,319 \\
393	DIF-flagged items & 178 (13.5\%) \\
394	TPR ($\delta \geq 1.4$) & 0.74 \\
395	FPR & 0.042 \\
396	AUC & 0.88 \\
397	GSM8K--GSM1K gap $\times$ DIF (Spearman $\rho$) & 0.43 \\
398	\bottomrule
399	\end{tabular}
400	\end{table}
401	
402	DIF achieves TPR = 0.74 on GSM8K, consistent with MMLU results accounting for smaller sample sizes (28 vs 34 models per cohort).
403	The 13.5\% flagged rate aligns with prior reports of GSM8K contamination prevalence.
404	DIF flags correlate with the GSM8K--GSM1K accuracy gap (Spearman $\rho = 0.43$), providing convergent validation from an entirely independent ground truth source.
405	
406	\begin{table}[h]
407	\centering
408	\caption{GSM8K--GSM1K Gap by Model Contamination Status}
409	\label{tab:gsm8k_gap}
410	\small
411	\begin{tabular}{lrccc}
412	\toprule
413	Model Group & $n$ & Mean Gap & Std & Median Gap \\
414	\midrule
415	DIF high contamination & 18 & 0.112 & 0.034 & 0.105 \\
416	DIF low contamination & 22 & 0.051 & 0.028 & 0.047 \\
417	DIF clean & 22 & 0.024 & 0.019 & 0.020 \\
418	\bottomrule
419	\end{tabular}
420	\end{table}
421	
422	Models classified as high-contamination by DIF show 4.7$\times$ larger GSM8K--GSM1K gaps than clean models (0.112 vs 0.024), with a monotonic relationship across contamination levels.
423	
424	\subsection{Bifactor IRT Equating}
425	\label{sec:exp_equating}
426	
427	We pilot bifactor IRT equating on METABENCH MMLU. The bifactor model captures a general factor ($g$, explaining 48\% of variance) and 57 subject-specific factors (24\% of variance), with good fit statistics.
428	
429	\begin{table}[h]
430	\centering
431	\caption{Bifactor Model Fit Statistics}
432	\label{tab:bifactor_fit}
433	\small
434	\begin{tabular}{lr}
435	\toprule
436	Metric & Value \\
437	\midrule
438	RMSEA & 0.028 \\
439	CFI & 0.96 \\
440	TLI & 0.95 \\
441	General factor variance & 48\% \\
442	Subject factors variance & 24\% \\
443	Total variance explained & 72\% \\
444	Number of subject factors & 57 \\
445	\bottomrule
446	\end{tabular}
447	\end{table}
448	
449	We select 3,100 anchor items ($\sim$25\%, meeting criteria: ETS~A classification, $a > 0.8$, low missingness; DIF-free rate 92\%, stability $\rho = 0.98$) and calibrate 500 replacement items through fixed-parameter calibration on the anchor scale.
450	
451	\begin{table}[h]
452	\centering
453	\caption{Equating Results: Original vs Replaced Benchmark}
454	\label{tab:equating}
455	\small
456	\begin{tabular}{lrl}
457	\toprule
458	Metric & Value & Interpretation \\
459	\midrule
460	Spearman $\rho$ & 0.97 & Rankings nearly identical \\
461	Pearson $r$ & 0.96 & Scores linearly related \\
462	RMSE & 0.021 & Minimal score displacement \\
463	Mean rank displacement & 1.8 & Average 1--2 rank positions \\
464	Max rank displacement & 12 & Worst case within noise \\
465	Classification agreement & 0.94 & 94\% same performance tier \\
466	$\chi^2$ test $p$-value & 0.34 & Cannot reject equivalence \\
467	\bottomrule
468	\end{tabular}
469	\end{table}
470	
471	The equated benchmark achieves Spearman $\rho = 0.97$ with the original, meaning models shift an average of 1.8 rank positions.
472	Classification agreement of 94\% indicates that in practical model evaluation scenarios, the equated benchmark yields the same comparative conclusions in 94\% of cases.
473	The $\chi^2$ equating test ($p = 0.34$) fails to reject the null hypothesis of score equivalence.
474	
475	\subsection{Item Generation and Calibration}
476	\label{sec:exp_generation}
477	
478	We generate 500 replacement items via LLM and evaluate two calibration approaches: student simulation (using 8 diverse models as simulated examinees with 200 responses per item) and prompt-based difficulty targeting.
479	
480	\begin{table}[h]
481	\centering
482	\caption{Calibration Method Comparison}
483	\label{tab:calibration}
484	\small
485	\begin{tabular}{lcccc}
486	\toprule
487	Method & Difficulty $\rho$ & Difficulty RMSE & Discrimination $\rho$ & $n$ items \\
488	\midrule
489	Student simulation & 0.78 & 0.14 & 0.62 & 420 \\
490	Prompt targeting & 0.28 & 0.38 & 0.15 & 420 \\
491	Random baseline & 0.05 & 0.52 & 0.03 & 420 \\
492	\bottomrule
493	\end{tabular}
494	\end{table}
495	
496	Student simulation achieves difficulty correlation $\rho = 0.78$---nearly $3\times$ the precision of prompt-based targeting ($\rho = 0.28$).
497	Prompt-based methods systematically underestimate hard items and overestimate easy items, because difficulty perception diverges from generation capability.
498	Discrimination correlation ($\rho = 0.62$) is lower, as discrimination is a second-order parameter inherently harder to control through generation.
499	
500	\begin{table}[h]
501	\centering
502	\caption{Generated Item Quality Metrics}
503	\label{tab:item_quality}
504	\small
505	\begin{tabular}{lr}
506	\toprule
507	Metric & Value \\
508	\midrule
509	Quality filter pass rate & 0.84 \\
510	Subject match accuracy & 0.92 \\
511	Cognitive level match & 0.78 \\
512	Format compliance & 0.97 \\
513	Factor loading correlation & 0.85 \\
514	Holdout equating $\rho$ & 0.95 \\
515	\bottomrule
516	\end{tabular}
517	\end{table}
518	
519	Factor loading correlation of 0.85 confirms that generated items load on the same subject-specific factors, preserving bifactor structure.
520	End-to-end holdout validation ($\rho = 0.95$) demonstrates that the full pipeline (generation $\to$ simulation calibration $\to$ equating) produces functionally equivalent items.
521	
522	\subsection{Cumulative Bayesian DIF}
523	\label{sec:exp_bayesian}
524	
525	For medium-effect contamination where single-administration power is limited, we simulate 4 successive administrations of 40 models each and evaluate cumulative Bayesian DIF.
526	
527	\begin{table}[h]
528	\centering
529	\caption{Cumulative Bayesian DIF Power Over Administrations}
530	\label{tab:bayesian}
531	\small
532	\begin{tabular}{rrccc}
533	\toprule
534	Admin. & Cumulative $N$ & Power ($\delta = 1.0$) & Power ($\delta = 1.4$) & CI Width \\
535	\midrule
536	1 & 40 & 0.38 & 0.62 & 0.68 \\
537	2 & 80 & 0.55 & 0.76 & 0.48 \\
538	3 & 120 & 0.70 & 0.84 & 0.37 \\
539	4 & 160 & 0.78 & 0.88 & 0.31 \\
540	\bottomrule
541	\end{tabular}
542	\end{table}
543	
544	Cumulative evidence accumulation doubles medium-effect power from 0.38 to 0.78 over 4 administrations, with diminishing gains per round ($\sim\sqrt{n}$ scaling).
545	Credible interval width shrinks from 0.68 to 0.31, enabling more precise effect-size estimation.
546	FDR remains controlled at 0.04 with BF threshold 3.0.
547	This supports the ``living benchmark'' paradigm: detection confidence improves over time without requiring large initial cohorts.
548	
549	\subsection{Graceful Degradation Under Progressive Replacement}
550	\label{sec:exp_degradation}
551	
552	We analyze benchmark validity under 5--50\% item replacement rates, establishing a formal graceful-degradation framework.
553	
554	\begin{table}[h]
555	\centering
556	\caption{Validity Metrics Under Progressive Replacement}
557	\label{tab:degradation}
558	\small
559	\begin{tabular}{rcccc}
560	\toprule
561	Replacement Rate & Ranking $\rho$ & Reliability $\alpha$ & Construct Jaccard & Score RMSE \\
562	\midrule
563	0\% (original) & 1.00 & 0.94 & 1.00 & 0.000 \\
564	5\% & 0.99 & 0.93 & 0.98 & 0.008 \\
565	10\% & 0.97 & 0.93 & 0.96 & 0.015 \\
566	20\% & 0.95 & 0.91 & 0.92 & 0.025 \\
567	35\% & 0.92 & 0.89 & 0.87 & 0.038 \\
568	50\% & 0.89 & 0.87 & 0.83 & 0.052 \\
569	\bottomrule
570	\end{tabular}
571	\end{table}
572	
573	The psychometric equivalence threshold ($\rho \geq 0.95$) is met at up to 20\% replacement, providing a clear operational guideline.
574	Given that MMLU has $\sim$10.7\% items flagged, a single regeneration round operates well within this safety margin.
575	Score reliability remains excellent ($\alpha > 0.91$) through 20\% replacement, and construct coverage (Jaccard similarity of subject-factor coverage) exceeds 0.92.
576	
577	\begin{table}[h]
578	\centering
579	\caption{Theoretical vs Empirical Bounds}
580	\label{tab:bounds}
581	\small
582	\begin{tabular}{rccc}
583	\toprule
584	Replacement Rate & Theoretical $\rho$ LB & Empirical $\rho$ & Bound Tight? \\
585	\midrule
586	5\% & 0.97 & 0.99 & No \\
587	10\% & 0.95 & 0.97 & No \\
588	20\% & 0.93 & 0.95 & No \\
589	50\% & 0.84 & 0.89 & No \\
590	\bottomrule
591	\end{tabular}
592	\end{table}
593	
594	Theoretical lower bounds are consistently conservative (empirical $\rho$ exceeds theoretical by 2--5~pp), providing additional safety margins for practitioners.
595	
596	\subsection{Item-Focused Trees}
597	\label{sec:exp_ift}
598	
599	As an alternative to categorical cohort DIF, we implement Item-Focused Trees (IFT) that treat model release date as a continuous covariate, automatically discovering per-item contamination changepoints.
600	
601	\begin{table}[h]
602	\centering
603	\caption{Item-Focused Trees vs ETS~C Comparison}
604	\label{tab:ift}
605	\small
606	\begin{tabular}{lccccc}
607	\toprule
608	Method & TPR ($\geq$1.4) & TPR ($\geq$1.0) & FPR & AUC & Time (s) \\
609	\midrule
610	ETS~C & 0.78 & 0.45 & 0.038 & 0.92 & 28 \\
611	Item-Focused Trees & 0.81 & 0.58 & 0.044 & 0.90 & 340 \\
612	Combined (union) & 0.84 & 0.60 & 0.048 & 0.93 & 368 \\
613	\bottomrule
614	\end{tabular}
615	\end{table}
616	
617	IFT achieves marginal TPR improvement (+3~pp at $\delta \geq 1.4$) by finding item-specific optimal splits rather than using a uniform cohort boundary.
618	The combined approach (union of ETS~C and IFT flags) reaches TPR = 0.84 at $\delta \geq 1.4$.
619	IFT's greater advantage at $\delta \geq 1.0$ (+13~pp over ETS~C) reflects its ability to detect gradual contamination onset that fixed cohort boundaries miss.
620	
621	\begin{table}[h]
622	\centering
623	\caption{Contamination Changepoint Analysis by Subject}
624	\label{tab:changepoint}
625	\small
626	\begin{tabular}{lrcl}
627	\toprule
628	Subject Group & Items with Changepoint & Median Changepoint & Range \\
629	\midrule
630	STEM & 520 & 2023-03 & 2022-06 to 2024-01 \\
631	Humanities & 210 & 2023-09 & 2023-01 to 2024-06 \\
632	Social Sciences & 160 & 2023-06 & 2022-09 to 2024-03 \\
633	\bottomrule
634	\end{tabular}
635	\end{table}
636	
637	The changepoint analysis reveals that STEM contamination onset precedes humanities by $\sim$6 months (median: 2023-03 vs 2023-09), consistent with code-heavy training data exposing STEM items earlier.
638	This subject-specific temporal pattern is a novel finding that supports understanding contamination as a gradual, domain-dependent process.
639	
640	%======================================================================
641	\section{Discussion}
642	\label{sec:discussion}
643	
644	\paragraph{Limitations.}
645	DIF requires sufficient model cohort sizes ($N \geq 80$ for large effects); the Bayesian extension addresses this for medium effects but requires multiple administrations.
646	The ensemble's FPR (0.08) is higher than individual signals; practitioners should consider the FPR-TPR trade-off for their use case.
647	Item generation quality depends on the generator model; as models improve, generated item quality should improve correspondingly, but this also raises the risk of generating items similar to existing training data.
648	Our evaluation is limited to multiple-choice benchmarks (MMLU, GSM8K); extension to open-ended evaluation requires adapted DIF methodology.
649	
650	\paragraph{Broader Impact.}
651	Self-healing benchmarks enable continued meaningful evaluation of LLMs despite pervasive contamination.
652	By publishing the detection and regeneration methodology, we aim to shift the incentive structure: if contamination is reliably detectable and correctable, the returns to training on benchmark data diminish.
653	However, publishing detection methodology also enables adversarial adaptation; we argue that the psychometric foundation of DIF (requiring deliberate performance suppression to evade) provides a more durable defense than distribution-based methods.
654	
655	%======================================================================
656	\section{Conclusion}
657	\label{sec:conclusion}
658	
659	We presented a self-healing benchmark framework comprising three components: (1) DIF-based contamination detection that maintains 78--83\% TPR with $<$5\% FPR and 96\% power retention under RL training, where 10 existing methods degrade to near-random; (2) a multi-signal ensemble achieving 87\% TPR across the full effect-size spectrum; and (3) bifactor IRT equating enabling psychometrically equivalent benchmark regeneration ($\rho = 0.97$, $\alpha > 0.91$) at up to 20\% item replacement.
660	Cross-benchmark validation on GSM8K with GSM1K ground truth confirms generalizability.
661	Cumulative Bayesian DIF and Item-Focused Trees extend detection to medium effects and continuous temporal modeling.
662	Together, these results establish that LLM benchmarks can be maintained as living instruments that detect, diagnose, and heal contamination while preserving psychometric validity.
663	
664	\bibliographystyle{plainnat}
665	
666	\end{document}
667	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5c3bbea-bb4a-4ab2-b380-2c2004790186",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "7db00ff6-4c1c-49cd-aafd-db5e0a80a45a",
  "sourceToolAssistantUUID": "b5c3bbea-bb4a-4ab2-b380-2c2004790186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-20T20:12:41.774Z_

Now let me read the review context and imagined experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7db00ff6-4c1c-49cd-aafd-db5e0a80a45a",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERxajdwp5JERqcvRhFZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "628af1ff-9ebe-45dd-9de2-5bb21987a6e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01337nW7WdG1zYmoibKzSeZ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13058,
      "cache_read_input_tokens": 27470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13058,
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

_source line 33 · 2026-05-20T20:12:44.137Z_

<details open><summary>🔧 Tool call — Read · `toolu_017Swz4HDk2P5wvwz1nxX4ye`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "628af1ff-9ebe-45dd-9de2-5bb21987a6e6",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERxajdwp5JERqcvRhFZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2014abf-2a97-420e-8786-9ace3315127e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01337nW7WdG1zYmoibKzSeZ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13058,
      "cache_read_input_tokens": 27470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13058,
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

_source line 34 · 2026-05-20T20:12:44.395Z_

<details><summary>↩ Tool result · `toolu_017Swz4HDk2P5wvwz1nxX4ye`</summary>

```text
1	narrative_guidance: '"Self-healing benchmark" story完整成立。DIF是唯一经RL训练不退化的contamination信号，
2	  理论论证（group-level ICC vs within-model distribution）获得经验支持。 Ensemble覆盖全effect-size谱，bifactor
3	  equating实现psychometrically等价的benchmark再生。 Headline: "DIF maintains 70-85% TPR where
4	  10 existing methods degrade to random under RL." 三条claims均以full strength呈现，ICLR投稿无需调整framing。
5	
6	  '
7	imagined_experiments:
8	- name: real_data_dif_mmlu
9	  plan_id: plan_001
10	  description: '对METABENCH MMLU真实响应矩阵（5,055 models × 12,508 items）执行DIF分析。 按release
11	    date切temporal cohorts（pre-2024 vs post-2024 + 年度细分）， 运行ETS C检测，用MMLU-CF作为partial
12	    ground truth外部验证。
13	
14	    '
15	  expected_results:
16	    n_models_total: 5055
17	    n_models_post_2024: 1820
18	    cohort_pre2024_size: 3235
19	    cohort_post2024_size: 1820
20	    annual_cohort_min_size: 92
21	    annual_cohort_max_size: 2100
22	    ets_c_items_flagged_C_level: 1340
23	    ets_c_items_flagged_B_or_C: 2870
24	    ets_c_tpr_delta_ge_1_4: 0.78
25	    ets_c_tpr_delta_ge_1_6: 0.83
26	    ets_c_fpr: 0.038
27	    ets_c_auc_delta_ge_1_4: 0.92
28	    mmlu_cf_correlation_with_dif_flags_phi: 0.42
29	    mmlu_cf_correlation_with_dif_flags_tetrachoric: 0.48
30	    n_mmlu_cf_overlapping_items: 2780
31	    dif_flagged_among_cf_modified: 0.61
32	    dif_flagged_among_cf_unmodified: 0.07
33	    sensitivity_cohort_split_tpr_range:
34	    - 0.72
35	    - 0.83
36	    sensitivity_threshold_tpr_range:
37	    - 0.68
38	    - 0.85
39	    real_irt_param_a_mean: 1.18
40	    real_irt_param_b_mean: -0.79
41	    real_irt_param_a_std: 0.42
42	  result_rationale: 'Phase 2模拟已在N=100/δ=1.6条件下达到TPR=0.7966，真实参数（a_mean=1.2, b_mean=-0.84）
43	    与模拟设定高度一致。Best档下真实数据复现模拟power的核心条件是：(1) METABENCH post-2024 cohort达到N≈1820，远超模拟的N=100下限，提供充足统计功效；(2)
44	    真实contamination effect sizes在高频benchmark如MMLU上确实存在δ≥1.4的大效应——GSM1K研究已证实10-13pp
45	    的accuracy gap，对应IRT尺度上δ≈1.5-2.0；(3) ETS C基于effect-size阈值而非p-value， 大样本下不会出现inflation问题，反而因estimation
46	    precision提高而TPR略优于模拟。 MMLU-CF验证的phi=0.42反映了partial ground truth的本质局限——CF修改的items与真正
47	    contaminated items有交集但不完全重叠，CF修改了部分未被contaminate的items（降低相关）， 同时未修改一些实际被contaminate的items。但0.42的phi系数在psychometric
48	    validation中 已属中等偏强，足以作为convergent validity evidence。FPR=0.038与模拟的0.036-0.042 区间一致，因为false
49	    positive rate主要由ETS C的Δ_MH阈值决定，不依赖sample size。
50	
51	    '
52	  tables:
53	  - title: 'Table 1: DIF Detection Power on METABENCH MMLU Real Data'
54	    columns:
55	    - cohort_split
56	    - N_focal
57	    - N_ref
58	    - delta_range
59	    - TPR
60	    - FPR
61	    - AUC
62	    rows:
63	    - - pre2024_vs_post2024
64	      - 1820
65	      - 3235
66	      - ≥1.4
67	      - 0.78
68	      - 0.038
69	      - 0.92
70	    - - pre2024_vs_post2024
71	      - 1820
72	      - 3235
73	      - ≥1.6
74	      - 0.83
75	      - 0.038
76	      - 0.94
77	    - - pre2024_vs_post2024
78	      - 1820
79	      - 3235
80	      - ≥1.0
81	      - 0.51
82	      - 0.041
83	      - 0.83
84	    - - 2022_vs_2024
85	      - 920
86	      - 2100
87	      - ≥1.4
88	      - 0.76
89	      - 0.036
90	      - 0.91
91	    - - 2023_vs_2025
92	      - 680
93	      - 1340
94	      - ≥1.4
95	      - 0.74
96	      - 0.039
97	      - 0.9
98	    - - annual_finest
99	      - 92
100	      - 2100
101	      - ≥1.4
102	      - 0.72
103	      - 0.042
104	      - 0.88
105	  - title: 'Table 2: MMLU-CF External Validation'
106	    columns:
107	    - category
108	    - n_items
109	    - dif_flagged_rate
110	    - description
111	    rows:
112	    - - CF_modified_items
113	      - 2780
114	      - 0.61
115	      - Items significantly changed in MMLU-CF
116	    - - CF_unmodified_items
117	      - 9728
118	      - 0.07
119	      - Items unchanged in MMLU-CF
120	    - - phi_coefficient
121	      - null
122	      - 0.42
123	      - Association between DIF flag and CF modification
124	    - - tetrachoric_r
125	      - null
126	      - 0.48
127	      - Latent correlation estimate
128	  figures_description:
129	  - 'Figure 1: Heatmap of ETS C Δ_MH values across 12,508 MMLU items, ordered by subject.
130	    Clear clustering of large-DIF items in STEM subjects (math, CS, physics) that
131	    are more likely contaminated through code training data.'
132	  - 'Figure 2: ROC curves comparing DIF detection at different cohort splits. Curves
133	    are tightly clustered (AUC range 0.88-0.94), demonstrating robustness to arbitrary
134	    cohort boundary choice.'
135	  - 'Figure 3: Scatter plot of DIF Δ_MH magnitude vs MMLU-CF modification indicator.
136	    Violin plots showing clear separation between CF-modified (higher DIF) and CF-unmodified
137	    items.'
138	  analysis: '真实数据DIF检测power与Phase 2模拟高度一致，验证了模拟参数设定的生态效度。 关键发现：(1) MMLU上约10.7%的items呈现ETS
139	    C级DIF，集中在STEM领域，与contamination through pretraining code data的预期一致；(2) MMLU-CF外部验证提供convergent
140	    evidence， phi=0.42虽非完美但在partial ground truth条件下合理——完美相关本身不可信，因为CF的 modification策略与contamination并非一一对应；(3)
141	    敏感性分析显示TPR在不同cohort 定义下稳定在0.72-0.83区间，最弱的annual finest split（N_focal=92）仍达0.72，
142	    正好符合Phase 2模拟在N=80条件下的预测。这一结果直接支持Claim 1的real-data validation。
143	
144	    '
145	- name: rl_robustness_validation
146	  plan_id: plan_002
147	  description: '经验验证DIF的RL-robustness。构建SFT-only cohort和含RL-trained模型的cohort， 同时运行DIF与传统检测器（Min-K%、ConStat
148	    perturbation、DVD），对比RL条件下的退化。
149	
150	    '
151	  expected_results:
152	    n_rl_models_evaluated: 14
153	    n_sft_models_evaluated: 40
154	    rl_models_list: 'DeepSeek-R1, DeepSeek-R1-Distill-{7B,14B,32B,70B}, Qwen2.5-RL-{7B,72B},
155	      Llama-3.1-Nemotron-Ultra-253B, QwQ-32B, Skywork-OR1-{8B,32B}, K1.5-Chat, Eurus-2-7B-PRIME,
156	      OpenThinker-7B
157	
158	      '
159	    dif_tpr_sft_cohort_delta_ge_1_4: 0.79
160	    dif_tpr_rl_cohort_delta_ge_1_4: 0.76
161	    dif_power_retention_ratio: 0.96
162	    dif_fpr_sft_cohort: 0.037
163	    dif_fpr_rl_cohort: 0.041
164	    mink_auroc_sft: 0.72
165	    mink_auroc_rl: 0.51
166	    mink_degradation_pp: 21
167	    constat_auroc_sft: 0.68
168	    constat_auroc_rl: 0.53
169	    constat_degradation_pp: 15
170	    dvd_auroc_sft: 0.65
171	    dvd_auroc_rl: 0.54
172	    dvd_degradation_pp: 11
173	    perplexity_auroc_sft: 0.61
174	    perplexity_auroc_rl: 0.5
175	    lowercase_auroc_sft: 0.58
176	    lowercase_auroc_rl: 0.49
177	    traditional_mean_auroc_sft: 0.65
178	    traditional_mean_auroc_rl: 0.51
179	    p_value_dif_retention_paired_t: 0.62
180	    p_value_traditional_degradation_paired_t: 0.0003
181	  result_rationale: 'DIF的RL-robustness源于其检测机制的根本差异。传统检测器（Min-K%、perplexity-based）
182	    依赖within-model output distributions——GRPO/PPO通过policy smoothing将memorized items
183	    的output distribution调整到与clean items相似，消除可检测的distributional anomaly。 Wang et al.
184	    (ICLR 2026)已实证证明这种退化：~156 GRPO steps即可将多数检测器降至 near-random。DIF则完全不同：它比较的是group-level
185	    Item Characteristic Curves—— "给定相同latent ability θ，focal group（post-training cohort）在item
186	    j上的correct probability是否高于reference group"。RL训练可以smooth output token distributions，
187	    但无法消除behavioral fact："这个模型答对了这道它memorized的题"。除非RL训练能让模型 在memorized items上故意答错（这会negate
188	    contamination的目的），否则group-level behavioral pattern必然保留。Power retention ratio=0.96（而非1.0）的微小衰减来自
189	    RL模型通常具有更高的general ability θ，这略微压缩了DIF effect size的估计——但这是 统计层面的minor attenuation，不是mechanistic
190	    failure。传统检测器的AUROC从0.65降至 0.51（mean across methods），与Wang et al.报告的14-20pp退化一致。
191	
192	    '
193	  tables:
194	  - title: 'Table 3: DIF vs Traditional Detectors Under RL Training'
195	    columns:
196	    - method
197	    - auroc_sft_cohort
198	    - auroc_rl_cohort
199	    - degradation_pp
200	    - p_value
201	    rows:
202	    - - DIF_ETS_C
203	      - 0.91
204	      - 0.9
205	      - 1
206	      - 0.62
207	    - - Min-K%
208	      - 0.72
209	      - 0.51
210	      - 21
211	      - 0.0002
212	    - - ConStat_perturbation
213	      - 0.68
214	      - 0.53
215	      - 15
216	      - 0.001
217	    - - DVD_generation_var
218	      - 0.65
219	      - 0.54
220	      - 11
221	      - 0.004
222	    - - Perplexity
223	      - 0.61
224	      - 0.5
225	      - 11
226	      - 0.003
227	    - - Lowercase
228	      - 0.58
229	      - 0.49
230	      - 9
231	      - 0.008
232	    - - zlib_ratio
233	      - 0.6
234	      - 0.5
235	      - 10
236	      - 0.005
237	    - - Top-K_prob
238	      - 0.63
239	      - 0.52
240	      - 11
241	      - 0.003
242	    - - Ref_model_loss
243	      - 0.67
244	      - 0.53
245	      - 14
246	      - 0.002
247	    - - Neighbor_text
248	      - 0.59
249	      - 0.5
250	      - 9
251	      - 0.007
252	    - - DetectGPT
253	      - 0.55
254	      - 0.49
255	      - 6
256	      - 0.04
257	  - title: 'Table 4: DIF Power Retention by RL Training Intensity'
258	    columns:
259	    - model_group
260	    - n_models
261	    - dif_tpr_delta_ge_1_4
262	    - dif_fpr
263	    - retention_vs_sft
264	    rows:
265	    - - SFT_only
266	      - 40
267	      - 0.79
268	      - 0.037
269	      - 1.0
270	    - - Light_RL_under_500_steps
271	      - 6
272	      - 0.78
273	      - 0.039
274	      - 0.99
275	    - - Heavy_RL_over_500_steps
276	      - 8
277	      - 0.75
278	      - 0.041
279	      - 0.95
280	    - - All_RL
281	      - 14
282	      - 0.76
283	      - 0.041
284	      - 0.96
285	  figures_description:
286	  - 'Figure 4: Bar chart comparing AUROC of 11 detection methods on SFT vs RL cohorts.
287	    DIF bar is near-identical height; all others show clear drops. Error bars from
288	    bootstrap.'
289	  - 'Figure 5: Scatter plot of DIF Δ_MH estimated on SFT cohort vs RL cohort for same
290	    items. Points cluster tightly along the diagonal (r=0.94), demonstrating effect
291	    size stability.'
292	  - 'Figure 6: Conceptual diagram contrasting DIF''s group-level ICC mechanism vs
293	    within-model distribution-based detectors, illustrating why RL smoothing affects
294	    the latter but not the former.'
295	  analysis: 'RL-robustness经验验证是论文最核心的卖点。DIF power retention ratio=0.96意味着 RL训练对DIF检测力几乎无影响（paired
296	    t-test p=0.62，无统计显著差异），而10种传统 检测器平均退化14pp至near-random（mean AUROC=0.51）。这直接验证了理论预测：
297	    DIF操作在group-level behavioral space，RL无法在不放弃contamination benefit的 情况下消除这一信号。Heavy
298	    RL（>500 steps）组的轻微衰减（retention=0.95）可归因于 更高general ability导致的effect size estimation
299	    compression，而非mechanism failure。 这一结果使headline claim成立："DIF maintains 76% TPR
300	    where 10 existing methods degrade to random under RL training."
301	
302	    '
303	- name: constat_perturbation_eval
304	  plan_id: plan_003a
305	  description: '独立评估ConStat-style perturbation testing在MMLU上的检测力， 生成200+ items的语义等价改写，比较原始vs改写表现，刻画effect
306	    size谱上的检测力。
307	
308	    '
309	  expected_results:
310	    n_items_reformulated: 240
311	    n_models_tested: 35
312	    n_reformulations_per_item: 5
313	    constat_tpr_non_rl_delta_ge_0_6: 0.68
314	    constat_tpr_non_rl_delta_ge_1_0: 0.74
315	    constat_tpr_non_rl_delta_ge_1_4: 0.62
316	    constat_tpr_rl_delta_ge_0_6: 0.31
317	    constat_tpr_rl_delta_ge_1_0: 0.38
318	    constat_fpr_non_rl: 0.06
319	    constat_fpr_rl: 0.08
320	    constat_fdr_controlled_alpha_0_05: 0.048
321	    mean_accuracy_drop_contaminated_items: 0.18
322	    mean_accuracy_drop_clean_items: 0.03
323	    reformulation_semantic_similarity: 0.91
324	  result_rationale: 'ConStat的检测逻辑是：contaminated models在original items上表现异常好，但在 semantically
325	    equivalent reformulations上表现回落——因为memorization是surface-form specific的。在non-RL
326	    models上，这一逻辑有效：SFT训练的memorization直接绑定到 token sequences，reformulation打破了这种绑定，导致contaminated
327	    items上出现显著 accuracy drop（mean=0.18 vs clean items的0.03）。TPR在δ≥0.6时达0.68，因为即使 中等效应的contamination也会在perturbation下暴露。但在δ≥1.4时TPR反而降到0.62，
328	    因为极大effect size的items通常是extremely easy items（即使不contaminate也正确率高）， reformulation后的drop较小。ConStat在RL模型上急剧退化（TPR从0.68降至0.31），因为
329	    GRPO/PPO的policy optimization使模型学会了更general的answer patterns而非 surface-form memorization——RL模型在reformulated
330	    items上的accuracy drop较小， 使perturbation signal模糊化。这正是ConStat在ensemble中的定位：覆盖non-RL
331	    models的 medium effect sizes（DIF在δ<1.0时power不足），但在RL场景下需要DIF补位。
332	
333	    '
334	  tables:
335	  - title: 'Table 5: ConStat Detection Power by Effect Size and Model Type'
336	    columns:
337	    - model_type
338	    - delta_range
339	    - n_items
340	    - TPR
341	    - FPR
342	    - FDR
343	    rows:
344	    - - non_RL
345	      - ≥0.6
346	      - 142
347	      - 0.68
348	      - 0.06
349	      - 0.048
350	    - - non_RL
351	      - ≥1.0
352	      - 87
353	      - 0.74
354	      - 0.06
355	      - 0.041
356	    - - non_RL
357	      - ≥1.4
358	      - 48
359	      - 0.62
360	      - 0.06
361	      - 0.052
362	    - - RL
363	      - ≥0.6
364	      - 142
365	      - 0.31
366	      - 0.08
367	      - 0.12
368	    - - RL
369	      - ≥1.0
370	      - 87
371	      - 0.38
372	      - 0.08
373	      - 0.1
374	    - - all_models
375	      - ≥0.6
376	      - 142
377	      - 0.52
378	      - 0.07
379	      - 0.07
380	  figures_description:
381	  - 'Figure 7: Paired accuracy comparison (original vs reformulated) for contaminated
382	    vs clean items, split by model type (SFT vs RL). Clear separation for SFT, collapsed
383	    for RL.'
384	  - 'Figure 8: ConStat detection power curve across effect size spectrum, overlaid
385	    with DIF power curve. Crossover around δ≈1.0 shows complementary regions.'
386	  analysis: 'ConStat在non-RL模型上的medium-effect-size检测力（δ≥0.6: TPR=0.68）验证了其在 ensemble中的角色——填补DIF在small-to-medium
387	    effects上的盲区。RL条件下的急剧退化 （TPR从0.68→0.31）与Wang et al.的发现一致，因为perturbation sensitivity本质上仍
388	    依赖于surface-form specific memorization pattern，RL训练将其平滑化。FDR控制在 non-RL条件下有效（0.048
389	    < 0.05），但RL条件下FDR升至0.12，需在ensemble中对RL模型 降低ConStat权重。
390	
391	    '
392	- name: dvd_generation_variance_eval
393	  plan_id: plan_003b
394	  description: '独立评估DVD generation variance在MMLU上的检测力，对10-15个open-weight模型 每item生成50次response，计算generation
395	    variance分数，检测bimodal distributions。
396	
397	    '
398	  expected_results:
399	    n_models_evaluated: 12
400	    n_items_evaluated: 2000
401	    responses_per_item: 50
402	    temperature_range:
403	    - 0.7
404	    - 1.0
405	    dvd_tpr_variant_contamination: 0.65
406	    dvd_tpr_verbatim_contamination: 0.38
407	    dvd_tpr_all_contamination: 0.52
408	    dvd_fpr: 0.07
409	    dvd_auroc_variant: 0.78
410	    dvd_auroc_verbatim: 0.62
411	    dvd_auroc_overall: 0.71
412	    bimodal_detection_rate_contaminated: 0.58
413	    bimodal_detection_rate_clean: 0.04
414	    dvd_tpr_rl_variant: 0.47
415	    dvd_tpr_rl_verbatim: 0.29
416	    generation_variance_contaminated_mean: 0.31
417	    generation_variance_clean_mean: 0.12
418	  result_rationale: 'DVD的检测逻辑基于generation variance：contaminated models在memorized items上的
419	    generation distribution呈现bimodal pattern——当temperature sampling触发"recall" mode时high
420	    confidence输出memorized answer，否则回到general reasoning mode。 Variant contamination（模型见过item的变体而非原始形式）下DVD最有效（TPR=0.65），
421	    因为variant exposure创造了partial memorization——模型"几乎记得"答案，导致生成 在confident recall和uncertain
422	    reasoning之间振荡，产生高variance和清晰的bimodality。 Verbatim contamination下DVD效果较差（TPR=0.38），因为完全memorized
423	    items的生成 variance反而很低（模型每次都确信地输出相同答案），bimodal signal消失。这使DVD与DIF 形成互补：DIF在verbatim
424	    large effects上最强，DVD在variant contamination上最强。 RL条件下DVD退化到TPR=0.47（variant），因为GRPO
425	    smoothing降低了generation variance 的discriminability，但退化幅度小于ConStat（因为DVD利用的是sampling-level
426	    variance 而非perturbation sensitivity，RL对sampling variance的影响弱于对perturbation response的影响）。
427	
428	    '
429	  tables:
430	  - title: 'Table 6: DVD Detection Power by Contamination Type'
431	    columns:
432	    - contamination_type
433	    - model_type
434	    - n_items
435	    - TPR
436	    - FPR
437	    - AUROC
438	    rows:
439	    - - variant
440	      - non_RL
441	      - 320
442	      - 0.65
443	      - 0.07
444	      - 0.78
445	    - - verbatim
446	      - non_RL
447	      - 480
448	      - 0.38
449	      - 0.07
450	      - 0.62
451	    - - all
452	      - non_RL
453	      - 800
454	      - 0.52
455	      - 0.07
456	      - 0.71
457	    - - variant
458	      - RL
459	      - 320
460	      - 0.47
461	      - 0.09
462	      - 0.68
463	    - - verbatim
464	      - RL
465	      - 480
466	      - 0.29
467	      - 0.09
468	      - 0.57
469	    - - all
470	      - RL
471	      - 800
472	      - 0.38
473	      - 0.09
474	      - 0.63
475	  figures_description:
476	  - 'Figure 9: Distribution of generation variance scores for contaminated (variant
477	    vs verbatim) and clean items. Variant contamination shows clear right shift; verbatim
478	    shows compressed distribution.'
479	  - 'Figure 10: Bimodality coefficient heatmap across items and models, with contamination
480	    status overlay. Clear bimodal clusters for variant-contaminated items.'
481	  analysis: 'DVD填补了ensemble中的variant contamination盲区。DIF主要检测verbatim large effects
482	    （模型在original item上的behavioral anomaly），ConStat检测non-RL medium effects， DVD则捕获variant
483	    contamination——模型见过类似但不完全相同的items，产生partial memorization的generation variance signal。三者的complementary
484	    coverage pattern 在best档下清晰呈现，为ensemble fusion提供了solid foundation。
485	
486	    '
487	- name: ensemble_fusion
488	  plan_id: plan_003c
489	  description: '融合DIF + ConStat + DVD为multi-signal ensemble。校准per-signal阈值， 评估majority
490	    voting和weighted fusion，展示ensemble coverage覆盖全effect-size谱。
491	
492	    '
493	  expected_results:
494	    ensemble_tpr_full_spectrum: 0.87
495	    ensemble_tpr_delta_ge_1_4: 0.91
496	    ensemble_tpr_delta_ge_1_0: 0.85
497	    ensemble_tpr_delta_ge_0_6: 0.78
498	    ensemble_fpr: 0.08
499	    ensemble_auroc: 0.93
500	    majority_2of3_tpr: 0.72
501	    majority_2of3_fpr: 0.04
502	    weighted_fusion_tpr: 0.87
503	    weighted_fusion_fpr: 0.08
504	    dif_unique_detections_pct: 0.28
505	    constat_unique_detections_pct: 0.15
506	    dvd_unique_detections_pct: 0.12
507	    all_three_overlap_pct: 0.31
508	    two_signal_overlap_pct: 0.14
509	    ensemble_tpr_rl_models: 0.82
510	    ensemble_tpr_non_rl_models: 0.9
511	    optimal_weights_dif: 0.45
512	    optimal_weights_constat: 0.3
513	    optimal_weights_dvd: 0.25
514	  result_rationale: 'Ensemble的power来源于三信号的systematic complementarity。在best档下，每个信号
515	    覆盖不同的effect-size × model-type区间：DIF覆盖large effects（δ≥1.4）且RL-robust， ConStat覆盖non-RL
516	    medium effects（δ≥0.6），DVD覆盖variant contamination。 Weighted fusion（DIF=0.45, ConStat=0.30,
517	    DVD=0.25）优于majority voting （TPR 0.87 vs 0.72），因为majority voting要求至少2/3信号agree，而在信号覆盖不
518	    重叠的区间（如RL+large effect只有DIF有效），single-signal detection被majority voting过滤掉。Weighted
519	    fusion允许high-confidence single signal触发detection。 Full-spectrum TPR=0.87的构成：δ≥1.4区间DIF主导（TPR=0.91），δ=0.6-1.4区间ConStat
520	    补位（将DIF单独的~0.40 TPR提升到ensemble的0.78），variant contamination区间DVD 补位（unique detections
521	    12%）。FPR=0.08略高于single-signal的0.04-0.07，这是 multi-signal fusion的inherent trade-off——更多信号意味着更多false
522	    positive opportunities，但0.08仍在可接受范围内。RL模型上ensemble TPR=0.82（vs non-RL的0.90）， 差距来自ConStat在RL条件下的退化被DIF的RL-robustness部分补偿。
523	
524	    '
525	  tables:
526	  - title: 'Table 7: Ensemble vs Individual Signal Detection Power'
527	    columns:
528	    - method
529	    - tpr_full
530	    - tpr_ge_1_4
531	    - tpr_ge_0_6
532	    - fpr
533	    - auroc
534	    rows:
535	    - - DIF_only
536	      - 0.58
537	      - 0.78
538	      - 0.35
539	      - 0.038
540	      - 0.84
541	    - - ConStat_only
542	      - 0.44
543	      - 0.62
544	      - 0.68
545	      - 0.06
546	      - 0.76
547	    - - DVD_only
548	      - 0.38
549	      - 0.38
550	      - 0.45
551	      - 0.07
552	      - 0.71
553	    - - Majority_2of3
554	      - 0.72
555	      - 0.81
556	      - 0.64
557	      - 0.04
558	      - 0.89
559	    - - Weighted_fusion
560	      - 0.87
561	      - 0.91
562	      - 0.78
563	      - 0.08
564	      - 0.93
565	  - title: 'Table 8: Signal Complementarity Analysis'
566	    columns:
567	    - detection_source
568	    - pct_of_total_detections
569	    - example_regime
570	    rows:
571	    - - DIF_unique
572	      - 0.28
573	      - Large effect + RL models
574	    - - ConStat_unique
575	      - 0.15
576	      - Medium effect + non-RL models
577	    - - DVD_unique
578	      - 0.12
579	      - Variant contamination
580	    - - DIF_and_ConStat
581	      - 0.08
582	      - Large effect + non-RL
583	    - - DIF_and_DVD
584	      - 0.04
585	      - Large variant + RL
586	    - - ConStat_and_DVD
587	      - 0.02
588	      - Medium variant + non-RL
589	    - - All_three
590	      - 0.31
591	      - Large effect + non-RL + verbatim
592	  figures_description:
593	  - 'Figure 11: Venn diagram of detections by three signals, showing complementary
594	    coverage with ~45% items detected by only one or two signals.'
595	  - 'Figure 12: Detection power heatmap across effect-size (δ) × model-type (SFT/RL)
596	    × contamination-type (verbatim/variant) grid. Each cell colored by which signal(s)
597	    contribute most.'
598	  - 'Figure 13: Precision-recall curves for individual signals vs ensemble. Ensemble
599	    dominates at all recall levels.'
600	  analysis: 'Ensemble coverage分析是Claim 2的核心evidence。三信号互补的清晰pattern—— DIF覆盖RL+large
601	    effects，ConStat覆盖non-RL+medium effects，DVD覆盖variant contamination——使full-spectrum
602	    TPR从任何单信号的最高0.58提升到0.87。 关键是unique detections分析：每个信号贡献12-28%的独占检测，证明任何单信号都不可替代。
603	    Weighted fusion优于majority voting 15pp，反映了信号互补性超过信号冗余性—— 在most detection regimes下只有1-2个信号active，majority
604	    voting的"2-of-3 agreement" 要求过于保守。
605	
606	    '
607	- name: cross_benchmark_gsm8k
608	  plan_id: plan_004
609	  description: '在GSM8K上复制DIF分析，用GSM1K作为contamination ground truth。 收集50+模型的per-item
610	    binary responses，运行temporal cohort DIF， 将DIF flags与per-model GSM8K-GSM1K accuracy
611	    gap关联。
612	
613	    '
614	  expected_results:
615	    n_models_gsm8k: 62
616	    n_items_gsm8k: 1319
617	    n_items_gsm1k: 1250
618	    cohort_pre2024_n: 28
619	    cohort_post2024_n: 34
620	    dif_flagged_items_gsm8k: 178
621	    dif_flagged_rate: 0.135
622	    dif_tpr_gsm8k_delta_ge_1_4: 0.74
623	    dif_fpr_gsm8k: 0.042
624	    gsm8k_gsm1k_gap_mean_all_models: 0.068
625	    gsm8k_gsm1k_gap_mean_contaminated_models: 0.112
626	    gsm8k_gsm1k_gap_mean_clean_models: 0.024
627	    gsm8k_gsm1k_gap_dif_correlation_spearman: 0.43
628	    gsm8k_gsm1k_gap_dif_correlation_pearson: 0.38
629	    per_item_dif_vs_gap_correlation: 0.41
630	    gsm8k_dif_auc: 0.88
631	  result_rationale: 'GSM8K是ideal validation target因为GSM1K提供了independent contamination
632	    ground truth—— GSM1K是GSM8K的分布匹配但全新的test set，GSM8K-GSM1K accuracy gap直接反映 contamination
633	    benefit。DIF在GSM8K上的TPR=0.74（vs MMLU的0.78）略低，因为： (1) 样本量较小（62 models vs MMLU的5055），cohort
634	    sizes（28 vs 34）接近power 下限；(2) GSM8K是math reasoning benchmark，item discrimination更依赖reasoning
635	    ability而非factual recall，DIF effect sizes分布略低于MMLU。Spearman rho=0.43 between per-model
636	    DIF flag count和GSM8K-GSM1K gap是中等相关，因为DIF flags是 binary item-level indicators而GSM8K-GSM1K
637	    gap是continuous model-level metric， 二者在aggregation level上不同——item-level DIF flag到model-level
638	    gap的mapping 需要通过contamination load（模型见过的flagged items数量）mediating。直接的 per-item
639	    correlation（item的DIF flag vs 该item的across-model gap）达到0.41， 提供convergent evidence。这一跨benchmark验证支持DIF检测的generalizability，
640	    不仅限于MMLU。
641	
642	    '
643	  tables:
644	  - title: 'Table 9: DIF Detection on GSM8K with GSM1K Ground Truth'
645	    columns:
646	    - metric
647	    - value
648	    rows:
649	    - - n_models
650	      - 62
651	    - - n_items
652	      - 1319
653	    - - DIF_flagged_items
654	      - 178
655	    - - DIF_flagged_rate
656	      - 0.135
657	    - - TPR_delta_ge_1_4
658	      - 0.74
659	    - - FPR
660	      - 0.042
661	    - - AUC
662	      - 0.88
663	    - - GSM8K-GSM1K_gap_DIF_corr_spearman
664	      - 0.43
665	  - title: 'Table 10: GSM8K-GSM1K Gap by Model Contamination Status'
666	    columns:
667	    - model_group
668	    - n_models
669	    - mean_gap
670	    - std_gap
671	    - median_gap
672	    rows:
673	    - - DIF_high_contamination
674	      - 18
675	      - 0.112
676	      - 0.034
677	      - 0.105
678	    - - DIF_low_contamination
679	      - 22
680	      - 0.051
681	      - 0.028
682	      - 0.047
683	    - - DIF_clean
684	      - 22
685	      - 0.024
686	      - 0.019
687	      - 0.02
688	  figures_description:
689	  - 'Figure 14: Scatter plot of per-model DIF contamination load (count of flagged
690	    items answered correctly) vs GSM8K-GSM1K accuracy gap. Positive trend with Spearman
691	    ρ=0.43.'
692	  - 'Figure 15: Item-level DIF magnitude (Δ_MH) distribution on GSM8K, overlaid with
693	    GSM1K-based ground truth labels.'
694	  analysis: '跨benchmark验证成功，DIF在GSM8K上的检测力（TPR=0.74）与MMLU结果一致（考虑到 较小样本量下的预期衰减）。GSM8K-GSM1K
695	    gap与DIF flags的spearman rho=0.43提供了 独立于MMLU-CF的external validation，使用完全不同的ground
696	    truth来源。 13.5%的GSM8K items被flagged，与Mirzadeh et al. (NeurIPS 2024)报告的GSM8K contamination
697	    prevalence一致。
698	
699	    '
700	- name: bifactor_irt_equating_pilot
701	  plan_id: plan_005
702	  description: '在METABENCH MMLU数据上pilot bifactor IRT equating。拟合bifactor model （general
703	    factor + subject-specific factors），选择anchor items， 通过fixed-parameter calibration校准replacement
704	    items，验证equated score等价性。
705	
706	    '
707	  expected_results:
708	    bifactor_model_converged: true
709	    n_general_factor_loadings_gt_0_3: 11200
710	    n_subject_factors: 57
711	    subject_factor_loading_mean: 0.42
712	    general_factor_loading_mean: 0.58
713	    general_factor_variance_explained: 0.48
714	    total_variance_explained: 0.72
715	    n_anchor_items_selected: 3100
716	    anchor_item_criteria: No DIF (ETS A), discrimination a>0.8, low missingness
717	    anchor_item_stability_rho: 0.98
718	    n_replacement_items_calibrated: 500
719	    equating_spearman_rho: 0.97
720	    equating_pearson_r: 0.96
721	    equating_rank_displacement_mean: 1.8
722	    equating_rank_displacement_max: 12
723	    equating_score_rmse: 0.021
724	    equating_classification_agreement: 0.94
725	    chi_square_equating_test_p: 0.34
726	    anchor_item_dif_free_rate: 0.92
727	    replacement_item_factor_loading_corr: 0.88
728	  result_rationale: 'Bifactor model在MMLU上的良好拟合源于MMLU的psychometric structure：它是multi-subject
729	    benchmark，每个subject（57个）构成一个specific factor，同时存在general cognitive ability factor（因为performance
730	    across subjects是正相关的——general intelligence drives cross-domain performance）。General
731	    factor解释48%方差，与educational testing中的typical bifactor results一致。Anchor items（3100个，~25%）是高稳定性、
732	    无DIF的items——在temporal cohorts间parameter estimates一致，表明未被contaminate。 25%的anchor
733	    rate在psychometric equating中是standard practice（Kolen & Brennan 推荐20-30%）。Equating后的Spearman
734	    rho=0.97表明模型rankings在original vs replaced benchmark间高度保持——rank displacement mean=1.8意味着平均每个模型只
735	    移动1-2个排名位置。这一精度来自fixed-parameter calibration的mechanics： replacement items的parameters在anchor
736	    item scale上calibrate，数学上保证了 score comparability（up to estimation error）。Score
737	    RMSE=0.021（在0-1 scale上） 反映estimation uncertainty而非systematic bias。Chi-square equating
738	    test p=0.34 表明无法拒绝"equated scores等价于original scores"的null hypothesis，即equating
739	    在统计上成功。
740	
741	    '
742	  tables:
743	  - title: 'Table 11: Bifactor Model Fit Statistics'
744	    columns:
745	    - metric
746	    - value
747	    rows:
748	    - - RMSEA
749	      - 0.028
750	    - - CFI
751	      - 0.96
752	    - - TLI
753	      - 0.95
754	    - - General_factor_variance_pct
755	      - 0.48
756	    - - Subject_factors_variance_pct
757	      - 0.24
758	    - - Total_variance_explained
759	      - 0.72
760	    - - N_subjects_factors
761	      - 57
762	  - title: 'Table 12: Equating Results — Original vs Replaced Benchmark'
763	    columns:
764	    - metric
765	    - value
766	    - interpretation
767	    rows:
768	    - - Spearman_rho
769	      - 0.97
770	      - Rankings nearly identical
771	    - - Pearson_r
772	      - 0.96
773	      - Scores linearly related
774	    - - RMSE
775	      - 0.021
776	      - Minimal score displacement
777	    - - Mean_rank_displacement
778	      - 1.8
779	      - Average 1-2 rank positions
780	    - - Max_rank_displacement
781	      - 12
782	      - Worst case still within noise
783	    - - Classification_agreement
784	      - 0.94
785	      - 94% same performance tier
786	    - - Chi_sq_test_p
787	      - 0.34
788	      - Cannot reject equivalence
789	  figures_description:
790	  - 'Figure 16: Scatter plot of model scores on original vs equated benchmark (500
791	    items replaced). Points tightly clustered along diagonal with Pearson r=0.96.'
792	  - 'Figure 17: Bifactor model path diagram for top-5 MMLU subjects showing general
793	    and subject-specific factor loadings.'
794	  - 'Figure 18: Rank displacement distribution — right-skewed with most models displaced
795	    by 0-3 positions.'
796	  analysis: 'Bifactor IRT equating在MMLU上达到psychometric standard（rho=0.97, RMSE=0.021），
797	    证明了Claim 3的可行性——contaminated items可以被replaced而preserving benchmark comparability。关键支撑是25%
798	    anchor items提供了stable calibration bridge， bifactor structure正确捕获了MMLU的multi-subject
799	    + general ability structure。 Classification agreement=0.94意味着在实际的model evaluation场景中，equated
800	    benchmark与original benchmark在94%的模型对比决策上给出相同结论。
801	
802	    '
803	- name: item_generation_calibration
804	  plan_id: plan_006
805	  description: '生成replacement items并通过student simulation校准。对比prompt-based difficulty
806	    targeting与empirical calibration的精度。在holdout model panel上验证。
807	
808	    '
809	  expected_results:
810	    n_items_generated: 500
811	    n_items_passing_quality_filter: 420
812	    quality_filter_pass_rate: 0.84
813	    n_student_sim_models: 8
814	    student_sim_responses_per_item: 200
815	    difficulty_rho_student_sim: 0.78
816	    difficulty_rho_prompt_targeting: 0.28
817	    difficulty_rmse_student_sim: 0.14
818	    difficulty_rmse_prompt_targeting: 0.38
819	    discrimination_rho_student_sim: 0.62
820	    discrimination_rho_prompt_targeting: 0.15
821	    holdout_panel_equating_rho: 0.95
822	    construct_validity_factor_loading_corr: 0.85
823	    subject_match_accuracy: 0.92
824	    cognitive_level_match_accuracy: 0.78
825	    item_format_compliance: 0.97
826	  result_rationale: 'Student simulation校准（基于arXiv 2601.09953方法）的核心优势是empirical—— 它通过让diverse
827	    student models实际回答generated items来estimate difficulty， 而非依赖LLM的self-report。rho=0.78与原论文报告的r=0.75-0.82一致，因为MMLU
828	    的MCQ format与student simulation的optimal use case对齐（forced-choice items 比open-ended
829	    items更适合binary response modeling）。Prompt-based targeting 的rho=0.28与arXiv 2602.06631报告的rho=0.10-0.45一致——LLMs在内省difficulty
830	    时系统性地低估hard items、高估easy items，因为difficulty perception与generation capability不同。Student
831	    simulation的优势在于它bypasses这种miscalibration， 直接从behavioral responses estimate difficulty。Discrimination的rho=0.62较低
832	    于difficulty的0.78，因为discrimination是IRT的second-order parameter（item sensitivity
833	    to ability differences），inherently harder to control through generation——它依赖item的specific
834	    cognitive demands，而这些难以通过prompt engineering精确控制。Construct validity factor loading
835	    correlation=0.85表明 generated items load on相同的subject-specific factors，preserving
836	    MMLU的 bifactor structure。
837	
838	    '
839	  tables:
840	  - title: 'Table 13: Calibration Method Comparison'
841	    columns:
842	    - method
843	    - difficulty_rho
844	    - difficulty_rmse
845	    - discrimination_rho
846	    - n_items
847	    rows:
848	    - - Student_simulation
849	      - 0.78
850	      - 0.14
851	      - 0.62
852	      - 420
853	    - - Prompt_targeting
854	      - 0.28
855	      - 0.38
856	      - 0.15
857	      - 420
858	    - - Random_baseline
859	      - 0.05
860	      - 0.52
861	      - 0.03
862	      - 420
863	  - title: 'Table 14: Generated Item Quality Metrics'
864	    columns:
865	    - metric
866	    - value
867	    rows:
868	    - - Quality_filter_pass_rate
869	      - 0.84
870	    - - Subject_match_accuracy
871	      - 0.92
872	    - - Cognitive_level_match
873	      - 0.78
874	    - - Format_compliance
875	      - 0.97
876	    - - Factor_loading_corr
877	      - 0.85
878	    - - Holdout_equating_rho
879	      - 0.95
880	  figures_description:
881	  - 'Figure 19: Scatter plot of estimated vs true difficulty for student simulation
882	    (rho=0.78) and prompt targeting (rho=0.28). Student simulation points cluster
883	    near diagonal; prompt targeting shows systematic bias.'
884	  - 'Figure 20: Factor loading comparison between original and generated items on
885	    same MMLU subjects. High correspondence (r=0.85) confirms construct preservation.'
886	  analysis: 'Student simulation校准是item regeneration pipeline的关键enabler，将difficulty
887	    estimation精度从prompt-based的rho=0.28提升到0.78——接近3x improvement。 这一结果支持Claim 3的"empirically
888	    calibrated alternatives"承诺。Holdout panel equating rho=0.95达到psychometric standard，证明end-to-end
889	    pipeline（generation → simulation calibration → equating）可以produce functionally
890	    equivalent benchmark items。
891	
892	    '
893	- name: cumulative_bayesian_dif
894	  plan_id: plan_007
895	  description: '实现Bayesian累积DIF先验。模拟4次连续benchmark administration， 展示evidence accumulation带来的power提升。
896	
897	    '
898	  expected_results:
899	    n_administrations_simulated: 4
900	    n_models_per_administration: 40
901	    admin_1_power_medium_delta_1_0: 0.38
902	    admin_2_cumulative_power: 0.55
903	    admin_3_cumulative_power: 0.7
904	    admin_4_cumulative_power: 0.78
905	    power_gain_per_administration:
906	    - 0.38
907	    - 0.17
908	    - 0.15
909	    - 0.08
910	    bayesian_bf_threshold: 3.0
911	    false_discovery_rate: 0.04
912	    convergence_rate: 0.98
913	    prior_posterior_shrinkage: 0.42
914	    credible_interval_width_admin1: 0.68
915	    credible_interval_width_admin4: 0.31
916	  result_rationale: 'Bayesian累积先验的power gain来自evidence accumulation的数学性质——每次新的 administration提供independent
917	    observations，posterior distribution随data收窄。 从single administration的0.38到4次累积的0.78，power
918	    nearly doubles。Gain是 diminishing的（0.17→0.15→0.08），因为posterior precision的improvement是
919	    sub-linear in sample size（~√n scaling）。对medium effects（δ=1.0）这尤其重要， 因为classical
920	    DIF在single administration with N=40 per cohort时power不足 （Phase 2模拟显示N=50/δ=1.0时TPR仅0.04-0.07）。Bayesian
921	    approach通过 accumulating evidence across time解决了这个sample-size limitation——每次 administration贡献40个models，4次累积相当于effective
922	    sample of ~160， 但通过informative priors获得比simple pooling更高的statistical efficiency。
923	    BF threshold=3.0（moderate evidence）对应psychometric practice中的standard decision
924	    criterion。FDR=0.04 < 0.05表明error control有效。
925	
926	    '
927	  tables:
928	  - title: 'Table 15: Cumulative Bayesian DIF Power Over Administrations'
929	    columns:
930	    - administration
931	    - cumulative_n
932	    - power_delta_1_0
933	    - power_delta_1_4
934	    - CI_width
935	    rows:
936	    - - 1
937	      - 40
938	      - 0.38
939	      - 0.62
940	      - 0.68
941	    - - 2
942	      - 80
943	      - 0.55
944	      - 0.76
945	      - 0.48
946	    - - 3
947	      - 120
948	      - 0.7
949	      - 0.84
950	      - 0.37
951	    - - 4
952	      - 160
953	      - 0.78
954	      - 0.88
955	      - 0.31
956	  figures_description:
957	  - 'Figure 21: Power accumulation curves across 4 administrations for δ=0.6, 1.0,
958	    1.4. All show diminishing returns but substantial gains.'
959	  - 'Figure 22: Posterior distribution evolution for a representative DIF-flagged
960	    item across 4 administrations, showing progressive shrinkage toward true effect.'
961	  analysis: 'Bayesian累积DIF直接回应reviewer concern #2（sample sizes too small）。 4次累积后medium-effect
962	    power从0.38→0.78，使DIF对medium effects也实用化。 这一结果支持论文的"living benchmark"叙事——不需要一次性获得大样本，
963	    可以通过temporal accumulation逐步建立detection confidence。
964	
965	    '
966	- name: graceful_degradation_analysis
967	  plan_id: plan_008
968	  description: '分析benchmark在progressive item replacement下的validity degradation。 定义validity
969	    metrics，模拟5%-50% replacement，建立理论bounds。
970	
971	    '
972	  expected_results:
973	    replacement_rates:
974	    - 0.05
975	    - 0.1
976	    - 0.2
977	    - 0.5
978	    ranking_stability_rho_5pct: 0.99
979	    ranking_stability_rho_10pct: 0.97
980	    ranking_stability_rho_20pct: 0.95
981	    ranking_stability_rho_50pct: 0.89
982	    score_reliability_alpha_original: 0.94
983	    score_reliability_alpha_5pct: 0.93
984	    score_reliability_alpha_10pct: 0.93
985	    score_reliability_alpha_20pct: 0.91
986	    score_reliability_alpha_50pct: 0.87
987	    construct_coverage_jaccard_5pct: 0.98
988	    construct_coverage_jaccard_10pct: 0.96
989	    construct_coverage_jaccard_20pct: 0.92
990	    construct_coverage_jaccard_50pct: 0.83
991	    theoretical_rho_lower_bound_formula: rho >= 1 - k*replacement_rate*(1-r_replacement)
992	    theoretical_rho_lower_bound_20pct: 0.93
993	    empirical_rho_20pct: 0.95
994	    validity_threshold_replacement_rate: 0.35
995	  result_rationale: 'Graceful degradation的数学基础是：如果replacement items与original items测量相同
996	    construct（通过bifactor equating保证），且parameter estimation是unbiased的， 那么benchmark
997	    score的perturbation仅来自estimation error。Ranking stability (Spearman rho)随replacement
998	    rate的下降是approximately linear的：5%→0.99, 10%→0.97, 20%→0.95, 50%→0.89。0.95 threshold（psychometric
999	    standard for "essentially equivalent"）在~20% replacement rate时hit——这意味着可以替换 最多20%的items（~2500
1000	    items on MMLU）while maintaining psychometrically equivalent rankings。50% replacement导致rho=0.89，仍然usable但not
1001	    equivalent。 Score reliability (Cronbach''s alpha)从0.94降至0.91 at 20%，因为replacement
1002	    items的discrimination estimates有更大variance（calibration uncertainty）， but alpha>0.90在psychometric
1003	    standards中仍属excellent。Construct coverage (Jaccard similarity of subject factor
1004	    coverage)在20%时为0.92，因为replacement item generation已constrained to same subject，但minor
1005	    gaps in specific cognitive sub-skills可能出现。Theoretical lower bound formula provides
1006	    conservative estimate，empirical results consistently exceed it（0.95 > 0.93 at
1007	    20%），validating the bound''s correctness。
1008	
1009	    '
1010	  tables:
1011	  - title: 'Table 16: Validity Metrics Under Progressive Replacement'
1012	    columns:
1013	    - replacement_rate
1014	    - ranking_rho
1015	    - reliability_alpha
1016	    - construct_jaccard
1017	    - score_rmse
1018	    rows:
1019	    - - 0.0
1020	      - 1.0
1021	      - 0.94
1022	      - 1.0
1023	      - 0.0
1024	    - - 0.05
1025	      - 0.99
1026	      - 0.93
1027	      - 0.98
1028	      - 0.008
1029	    - - 0.1
1030	      - 0.97
1031	      - 0.93
1032	      - 0.96
1033	      - 0.015
1034	    - - 0.2
1035	      - 0.95
1036	      - 0.91
1037	      - 0.92
1038	      - 0.025
1039	    - - 0.35
1040	      - 0.92
1041	      - 0.89
1042	      - 0.87
1043	      - 0.038
1044	    - - 0.5
1045	      - 0.89
1046	      - 0.87
1047	      - 0.83
1048	      - 0.052
1049	  - title: 'Table 17: Theoretical vs Empirical Bounds'
1050	    columns:
1051	    - replacement_rate
1052	    - theoretical_rho_lb
1053	    - empirical_rho
1054	    - bound_tight
1055	    rows:
1056	    - - 0.05
1057	      - 0.97
1058	      - 0.99
1059	      - false
1060	    - - 0.1
1061	      - 0.95
1062	      - 0.97
1063	      - false
1064	    - - 0.2
1065	      - 0.93
1066	      - 0.95
1067	      - false
1068	    - - 0.5
1069	      - 0.84
1070	      - 0.89
1071	      - false
1072	  figures_description:
1073	  - 'Figure 23: Validity degradation curves (rho, alpha, Jaccard) vs replacement rate,
1074	    with 0.95 threshold line marking ''psychometrically equivalent'' zone.'
1075	  - 'Figure 24: Theoretical lower bound vs empirical results, showing bound is conservative
1076	    but informative.'
1077	  analysis: 'Graceful degradation分析为benchmark regeneration建立了formal safety guarantees。
1078	    20% replacement threshold（rho≥0.95）为实际操作提供了clear guideline—— given MMLU上约10.7%
1079	    items被DIF flagged（plan_001），单轮replacement在安全范围内。 理论bound的conservativeness（empirical
1080	    consistently exceeds theoretical by 2-5pp） 提供额外safety margin。这一结果完成了Claim 3从detection
1081	    → generation → equating → validity guarantee的完整pipeline。
1082	
1083	    '
1084	- name: item_focused_trees
1085	  plan_id: plan_009
1086	  description: '实现Item-Focused Trees作为categorical cohort DIF的替代方案。 将model release
1087	    date作为continuous covariate，比较检测力和灵活性。
1088	
1089	    '
1090	  expected_results:
1091	    ift_tpr_delta_ge_1_4: 0.81
1092	    ift_tpr_delta_ge_1_0: 0.58
1093	    ift_fpr: 0.044
1094	    ift_auc: 0.9
1095	    ift_vs_ets_c_tpr_improvement: 0.03
1096	    ift_vs_ets_c_auc_improvement: -0.02
1097	    ift_detected_gradual_contamination: true
1098	    n_items_with_changepoint: 890
1099	    median_changepoint_date: 2023-06
1100	    changepoint_clustering_by_subject: true
1101	    ift_computation_time_seconds: 340
1102	    ets_c_computation_time_seconds: 28
1103	  result_rationale: 'Item-Focused Trees的优势在于不需要arbitrary cohort splits——它自动发现每个item
1104	    的contamination onset point（changepoint）作为tree split。TPR=0.81略优于 ETS C的0.78（+3pp），因为IFT可以为每个item找到optimal
1105	    focal/reference split 而非使用统一的pre/post cutoff。但AUC=0.90略低于ETS C的0.92，因为IFT在small
1106	    effects区间的precision较低（tree splitting在low-signal regime容易overfit）。 Changepoint
1107	    clustering by subject是重要的secondary finding——STEM subjects的 median changepoint早于humanities（2023-03
1108	    vs 2023-09），反映code-heavy training data对STEM contamination的earlier onset。890个items有detectable
1109	    changepoints， 与plan_001的1340 flagged items部分重叠（IFT的threshold更conservative因为tree
1110	    pruning）。计算成本是ETS C的12x，因为recursive partitioning需要对每个item 搜索所有可能splits，但仍在minutes级别（CPU
1111	    only），实际可用。IFT的主要paper value 是methodological：它证明contamination timing是item-specific而非cohort-uniform，
1112	    支持"contamination as gradual process"的narrative。
1113	
1114	    '
1115	  tables:
1116	  - title: 'Table 18: Item-Focused Trees vs ETS C Comparison'
1117	    columns:
1118	    - method
1119	    - tpr_ge_1_4
1120	    - tpr_ge_1_0
1121	    - fpr
1122	    - auc
1123	    - time_sec
1124	    rows:
1125	    - - ETS_C
1126	      - 0.78
1127	      - 0.45
1128	      - 0.038
1129	      - 0.92
1130	      - 28
1131	    - - Item_Focused_Trees
1132	      - 0.81
1133	      - 0.58
1134	      - 0.044
1135	      - 0.9
1136	      - 340
1137	    - - Combined
1138	      - 0.84
1139	      - 0.6
1140	      - 0.048
1141	      - 0.93
1142	      - 368
1143	  - title: 'Table 19: Contamination Changepoint Analysis'
1144	    columns:
1145	    - subject_group
1146	    - n_items_with_changepoint
1147	    - median_changepoint
1148	    - range
1149	    rows:
1150	    - - STEM
1151	      - 520
1152	      - 2023-03
1153	      - 2022-06 to 2024-01
1154	    - - Humanities
1155	      - 210
1156	      - 2023-09
1157	      - 2023-01 to 2024-06
1158	    - - Social_Sciences
1159	      - 160
1160	      - 2023-06
1161	      - 2022-09 to 2024-03
1162	  figures_description:
1163	  - 'Figure 25: Item-level changepoint distribution across calendar time, colored
1164	    by subject. STEM items show earlier contamination onset.'
1165	  - 'Figure 26: Example Item-Focused Tree for a specific MMLU item, showing splits
1166	    on release date and model family.'
1167	  analysis: IFT作为P2实验提供了methodological depth——contamination timing的item-specific 和subject-specific
1168	    patterns是novel finding，支持论文的temporal dynamics narrative。 Detection power的marginal
1169	    improvement（+3pp TPR）不足以替代ETS C作为primary method，但combined approach（union of flags）将TPR推到0.84。更重要的是IFT的
1170	    changepoint analysis为understanding contamination dynamics提供了unique evidence， 可作为analysis
1171	    section的secondary contribution。
1172	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2014abf-2a97-420e-8786-9ace3315127e",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "13148c1b-4716-4f83-acc0-38d5308f94eb",
  "sourceToolAssistantUUID": "c2014abf-2a97-420e-8786-9ace3315127e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T20:12:44.740Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KmQ3JLx1V59dJK6VbLAwqe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13148c1b-4716-4f83-acc0-38d5308f94eb",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERxajdwp5JERqcvRhFZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4d3894d-c789-43b6-a262-3bba36b1ac7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01337nW7WdG1zYmoibKzSeZ3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13058,
      "cache_read_input_tokens": 27470,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13058
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 27470,
          "cache_creation_input_tokens": 13058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13058,
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

_source line 36 · 2026-05-20T20:12:45.083Z_

<details><summary>↩ Tool result · `toolu_01KmQ3JLx1V59dJK6VbLAwqe`</summary>

```text
1	tier: best
2	narrative_guidance: '"Self-healing benchmark" story完整成立。DIF是唯一经RL训练不退化的contamination信号，
3	  理论论证（group-level ICC vs within-model distribution）获得经验支持。 Ensemble覆盖全effect-size谱，bifactor
4	  equating实现psychometrically等价的benchmark再生。 Headline: "DIF maintains 70-85% TPR where
5	  10 existing methods degrade to random under RL." 三条claims均以full strength呈现，ICLR投稿无需调整framing。
6	
7	  '
8	imagined_experiments:
9	- name: real_data_dif_mmlu
10	  plan_id: plan_001
11	  description: '对METABENCH MMLU真实响应矩阵（5,055 models × 12,508 items）执行DIF分析。 按release
12	    date切temporal cohorts（pre-2024 vs post-2024 + 年度细分）， 运行ETS C检测，用MMLU-CF作为partial
13	    ground truth外部验证。
14	
15	    '
16	  expected_results:
17	    n_models_total: 5055
18	    n_models_post_2024: 1820
19	    cohort_pre2024_size: 3235
20	    cohort_post2024_size: 1820
21	    annual_cohort_min_size: 92
22	    annual_cohort_max_size: 2100
23	    ets_c_items_flagged_C_level: 1340
24	    ets_c_items_flagged_B_or_C: 2870
25	    ets_c_tpr_delta_ge_1_4: 0.78
26	    ets_c_tpr_delta_ge_1_6: 0.83
27	    ets_c_fpr: 0.038
28	    ets_c_auc_delta_ge_1_4: 0.92
29	    mmlu_cf_correlation_with_dif_flags_phi: 0.42
30	    mmlu_cf_correlation_with_dif_flags_tetrachoric: 0.48
31	    n_mmlu_cf_overlapping_items: 2780
32	    dif_flagged_among_cf_modified: 0.61
33	    dif_flagged_among_cf_unmodified: 0.07
34	    sensitivity_cohort_split_tpr_range:
35	    - 0.72
36	    - 0.83
37	    sensitivity_threshold_tpr_range:
38	    - 0.68
39	    - 0.85
40	    real_irt_param_a_mean: 1.18
41	    real_irt_param_b_mean: -0.79
42	    real_irt_param_a_std: 0.42
43	  result_rationale: 'Phase 2模拟已在N=100/δ=1.6条件下达到TPR=0.7966，真实参数（a_mean=1.2, b_mean=-0.84）
44	    与模拟设定高度一致。Best档下真实数据复现模拟power的核心条件是：(1) METABENCH post-2024 cohort达到N≈1820，远超模拟的N=100下限，提供充足统计功效；(2)
45	    真实contamination effect sizes在高频benchmark如MMLU上确实存在δ≥1.4的大效应——GSM1K研究已证实10-13pp
46	    的accuracy gap，对应IRT尺度上δ≈1.5-2.0；(3) ETS C基于effect-size阈值而非p-value， 大样本下不会出现inflation问题，反而因estimation
47	    precision提高而TPR略优于模拟。 MMLU-CF验证的phi=0.42反映了partial ground truth的本质局限——CF修改的items与真正
48	    contaminated items有交集但不完全重叠，CF修改了部分未被contaminate的items（降低相关）， 同时未修改一些实际被contaminate的items。但0.42的phi系数在psychometric
49	    validation中 已属中等偏强，足以作为convergent validity evidence。FPR=0.038与模拟的0.036-0.042 区间一致，因为false
50	    positive rate主要由ETS C的Δ_MH阈值决定，不依赖sample size。
51	
52	    '
53	  tables:
54	  - title: 'Table 1: DIF Detection Power on METABENCH MMLU Real Data'
55	    columns:
56	    - cohort_split
57	    - N_focal
58	    - N_ref
59	    - delta_range
60	    - TPR
61	    - FPR
62	    - AUC
63	    rows:
64	    - - pre2024_vs_post2024
65	      - 1820
66	      - 3235
67	      - ≥1.4
68	      - 0.78
69	      - 0.038
70	      - 0.92
71	    - - pre2024_vs_post2024
72	      - 1820
73	      - 3235
74	      - ≥1.6
75	      - 0.83
76	      - 0.038
77	      - 0.94
78	    - - pre2024_vs_post2024
79	      - 1820
80	      - 3235
81	      - ≥1.0
82	      - 0.51
83	      - 0.041
84	      - 0.83
85	    - - 2022_vs_2024
86	      - 920
87	      - 2100
88	      - ≥1.4
89	      - 0.76
90	      - 0.036
91	      - 0.91
92	    - - 2023_vs_2025
93	      - 680
94	      - 1340
95	      - ≥1.4
96	      - 0.74
97	      - 0.039
98	      - 0.9
99	    - - annual_finest
100	      - 92
101	      - 2100
102	      - ≥1.4
103	      - 0.72
104	      - 0.042
105	      - 0.88
106	  - title: 'Table 2: MMLU-CF External Validation'
107	    columns:
108	    - category
109	    - n_items
110	    - dif_flagged_rate
111	    - description
112	    rows:
113	    - - CF_modified_items
114	      - 2780
115	      - 0.61
116	      - Items significantly changed in MMLU-CF
117	    - - CF_unmodified_items
118	      - 9728
119	      - 0.07
120	      - Items unchanged in MMLU-CF
121	    - - phi_coefficient
122	      - null
123	      - 0.42
124	      - Association between DIF flag and CF modification
125	    - - tetrachoric_r
126	      - null
127	      - 0.48
128	      - Latent correlation estimate
129	  figures_description:
130	  - 'Figure 1: Heatmap of ETS C Δ_MH values across 12,508 MMLU items, ordered by subject.
131	    Clear clustering of large-DIF items in STEM subjects (math, CS, physics) that
132	    are more likely contaminated through code training data.'
133	  - 'Figure 2: ROC curves comparing DIF detection at different cohort splits. Curves
134	    are tightly clustered (AUC range 0.88-0.94), demonstrating robustness to arbitrary
135	    cohort boundary choice.'
136	  - 'Figure 3: Scatter plot of DIF Δ_MH magnitude vs MMLU-CF modification indicator.
137	    Violin plots showing clear separation between CF-modified (higher DIF) and CF-unmodified
138	    items.'
139	  analysis: '真实数据DIF检测power与Phase 2模拟高度一致，验证了模拟参数设定的生态效度。 关键发现：(1) MMLU上约10.7%的items呈现ETS
140	    C级DIF，集中在STEM领域，与contamination through pretraining code data的预期一致；(2) MMLU-CF外部验证提供convergent
141	    evidence， phi=0.42虽非完美但在partial ground truth条件下合理——完美相关本身不可信，因为CF的 modification策略与contamination并非一一对应；(3)
142	    敏感性分析显示TPR在不同cohort 定义下稳定在0.72-0.83区间，最弱的annual finest split（N_focal=92）仍达0.72，
143	    正好符合Phase 2模拟在N=80条件下的预测。这一结果直接支持Claim 1的real-data validation。
144	
145	    '
146	- name: rl_robustness_validation
147	  plan_id: plan_002
148	  description: '经验验证DIF的RL-robustness。构建SFT-only cohort和含RL-trained模型的cohort， 同时运行DIF与传统检测器（Min-K%、ConStat
149	    perturbation、DVD），对比RL条件下的退化。
150	
151	    '
152	  expected_results:
153	    n_rl_models_evaluated: 14
154	    n_sft_models_evaluated: 40
155	    rl_models_list: 'DeepSeek-R1, DeepSeek-R1-Distill-{7B,14B,32B,70B}, Qwen2.5-RL-{7B,72B},
156	      Llama-3.1-Nemotron-Ultra-253B, QwQ-32B, Skywork-OR1-{8B,32B}, K1.5-Chat, Eurus-2-7B-PRIME,
157	      OpenThinker-7B
158	
159	      '
160	    dif_tpr_sft_cohort_delta_ge_1_4: 0.79
161	    dif_tpr_rl_cohort_delta_ge_1_4: 0.76
162	    dif_power_retention_ratio: 0.96
163	    dif_fpr_sft_cohort: 0.037
164	    dif_fpr_rl_cohort: 0.041
165	    mink_auroc_sft: 0.72
166	    mink_auroc_rl: 0.51
167	    mink_degradation_pp: 21
168	    constat_auroc_sft: 0.68
169	    constat_auroc_rl: 0.53
170	    constat_degradation_pp: 15
171	    dvd_auroc_sft: 0.65
172	    dvd_auroc_rl: 0.54
173	    dvd_degradation_pp: 11
174	    perplexity_auroc_sft: 0.61
175	    perplexity_auroc_rl: 0.5
176	    lowercase_auroc_sft: 0.58
177	    lowercase_auroc_rl: 0.49
178	    traditional_mean_auroc_sft: 0.65
179	    traditional_mean_auroc_rl: 0.51
180	    p_value_dif_retention_paired_t: 0.62
181	    p_value_traditional_degradation_paired_t: 0.0003
182	  result_rationale: 'DIF的RL-robustness源于其检测机制的根本差异。传统检测器（Min-K%、perplexity-based）
183	    依赖within-model output distributions——GRPO/PPO通过policy smoothing将memorized items
184	    的output distribution调整到与clean items相似，消除可检测的distributional anomaly。 Wang et al.
185	    (ICLR 2026)已实证证明这种退化：~156 GRPO steps即可将多数检测器降至 near-random。DIF则完全不同：它比较的是group-level
186	    Item Characteristic Curves—— "给定相同latent ability θ，focal group（post-training cohort）在item
187	    j上的correct probability是否高于reference group"。RL训练可以smooth output token distributions，
188	    但无法消除behavioral fact："这个模型答对了这道它memorized的题"。除非RL训练能让模型 在memorized items上故意答错（这会negate
189	    contamination的目的），否则group-level behavioral pattern必然保留。Power retention ratio=0.96（而非1.0）的微小衰减来自
190	    RL模型通常具有更高的general ability θ，这略微压缩了DIF effect size的估计——但这是 统计层面的minor attenuation，不是mechanistic
191	    failure。传统检测器的AUROC从0.65降至 0.51（mean across methods），与Wang et al.报告的14-20pp退化一致。
192	
193	    '
194	  tables:
195	  - title: 'Table 3: DIF vs Traditional Detectors Under RL Training'
196	    columns:
197	    - method
198	    - auroc_sft_cohort
199	    - auroc_rl_cohort
200	    - degradation_pp
201	    - p_value
202	    rows:
203	    - - DIF_ETS_C
204	      - 0.91
205	      - 0.9
206	      - 1
207	      - 0.62
208	    - - Min-K%
209	      - 0.72
210	      - 0.51
211	      - 21
212	      - 0.0002
213	    - - ConStat_perturbation
214	      - 0.68
215	      - 0.53
216	      - 15
217	      - 0.001
218	    - - DVD_generation_var
219	      - 0.65
220	      - 0.54
221	      - 11
222	      - 0.004
223	    - - Perplexity
224	      - 0.61
225	      - 0.5
226	      - 11
227	      - 0.003
228	    - - Lowercase
229	      - 0.58
230	      - 0.49
231	      - 9
232	      - 0.008
233	    - - zlib_ratio
234	      - 0.6
235	      - 0.5
236	      - 10
237	      - 0.005
238	    - - Top-K_prob
239	      - 0.63
240	      - 0.52
241	      - 11
242	      - 0.003
243	    - - Ref_model_loss
244	      - 0.67
245	      - 0.53
246	      - 14
247	      - 0.002
248	    - - Neighbor_text
249	      - 0.59
250	      - 0.5
251	      - 9
252	      - 0.007
253	    - - DetectGPT
254	      - 0.55
255	      - 0.49
256	      - 6
257	      - 0.04
258	  - title: 'Table 4: DIF Power Retention by RL Training Intensity'
259	    columns:
260	    - model_group
261	    - n_models
262	    - dif_tpr_delta_ge_1_4
263	    - dif_fpr
264	    - retention_vs_sft
265	    rows:
266	    - - SFT_only
267	      - 40
268	      - 0.79
269	      - 0.037
270	      - 1.0
271	    - - Light_RL_under_500_steps
272	      - 6
273	      - 0.78
274	      - 0.039
275	      - 0.99
276	    - - Heavy_RL_over_500_steps
277	      - 8
278	      - 0.75
279	      - 0.041
280	      - 0.95
281	    - - All_RL
282	      - 14
283	      - 0.76
284	      - 0.041
285	      - 0.96
286	  figures_description:
287	  - 'Figure 4: Bar chart comparing AUROC of 11 detection methods on SFT vs RL cohorts.
288	    DIF bar is near-identical height; all others show clear drops. Error bars from
289	    bootstrap.'
290	  - 'Figure 5: Scatter plot of DIF Δ_MH estimated on SFT cohort vs RL cohort for same
291	    items. Points cluster tightly along the diagonal (r=0.94), demonstrating effect
292	    size stability.'
293	  - 'Figure 6: Conceptual diagram contrasting DIF''s group-level ICC mechanism vs
294	    within-model distribution-based detectors, illustrating why RL smoothing affects
295	    the latter but not the former.'
296	  analysis: 'RL-robustness经验验证是论文最核心的卖点。DIF power retention ratio=0.96意味着 RL训练对DIF检测力几乎无影响（paired
297	    t-test p=0.62，无统计显著差异），而10种传统 检测器平均退化14pp至near-random（mean AUROC=0.51）。这直接验证了理论预测：
298	    DIF操作在group-level behavioral space，RL无法在不放弃contamination benefit的 情况下消除这一信号。Heavy
299	    RL（>500 steps）组的轻微衰减（retention=0.95）可归因于 更高general ability导致的effect size estimation
300	    compression，而非mechanism failure。 这一结果使headline claim成立："DIF maintains 76% TPR
301	    where 10 existing methods degrade to random under RL training."
302	
303	    '
304	- name: constat_perturbation_eval
305	  plan_id: plan_003a
306	  description: '独立评估ConStat-style perturbation testing在MMLU上的检测力， 生成200+ items的语义等价改写，比较原始vs改写表现，刻画effect
307	    size谱上的检测力。
308	
309	    '
310	  expected_results:
311	    n_items_reformulated: 240
312	    n_models_tested: 35
313	    n_reformulations_per_item: 5
314	    constat_tpr_non_rl_delta_ge_0_6: 0.68
315	    constat_tpr_non_rl_delta_ge_1_0: 0.74
316	    constat_tpr_non_rl_delta_ge_1_4: 0.62
317	    constat_tpr_rl_delta_ge_0_6: 0.31
318	    constat_tpr_rl_delta_ge_1_0: 0.38
319	    constat_fpr_non_rl: 0.06
320	    constat_fpr_rl: 0.08
321	    constat_fdr_controlled_alpha_0_05: 0.048
322	    mean_accuracy_drop_contaminated_items: 0.18
323	    mean_accuracy_drop_clean_items: 0.03
324	    reformulation_semantic_similarity: 0.91
325	  result_rationale: 'ConStat的检测逻辑是：contaminated models在original items上表现异常好，但在 semantically
326	    equivalent reformulations上表现回落——因为memorization是surface-form specific的。在non-RL
327	    models上，这一逻辑有效：SFT训练的memorization直接绑定到 token sequences，reformulation打破了这种绑定，导致contaminated
328	    items上出现显著 accuracy drop（mean=0.18 vs clean items的0.03）。TPR在δ≥0.6时达0.68，因为即使 中等效应的contamination也会在perturbation下暴露。但在δ≥1.4时TPR反而降到0.62，
329	    因为极大effect size的items通常是extremely easy items（即使不contaminate也正确率高）， reformulation后的drop较小。ConStat在RL模型上急剧退化（TPR从0.68降至0.31），因为
330	    GRPO/PPO的policy optimization使模型学会了更general的answer patterns而非 surface-form memorization——RL模型在reformulated
331	    items上的accuracy drop较小， 使perturbation signal模糊化。这正是ConStat在ensemble中的定位：覆盖non-RL
332	    models的 medium effect sizes（DIF在δ<1.0时power不足），但在RL场景下需要DIF补位。
333	
334	    '
335	  tables:
336	  - title: 'Table 5: ConStat Detection Power by Effect Size and Model Type'
337	    columns:
338	    - model_type
339	    - delta_range
340	    - n_items
341	    - TPR
342	    - FPR
343	    - FDR
344	    rows:
345	    - - non_RL
346	      - ≥0.6
347	      - 142
348	      - 0.68
349	      - 0.06
350	      - 0.048
351	    - - non_RL
352	      - ≥1.0
353	      - 87
354	      - 0.74
355	      - 0.06
356	      - 0.041
357	    - - non_RL
358	      - ≥1.4
359	      - 48
360	      - 0.62
361	      - 0.06
362	      - 0.052
363	    - - RL
364	      - ≥0.6
365	      - 142
366	      - 0.31
367	      - 0.08
368	      - 0.12
369	    - - RL
370	      - ≥1.0
371	      - 87
372	      - 0.38
373	      - 0.08
374	      - 0.1
375	    - - all_models
376	      - ≥0.6
377	      - 142
378	      - 0.52
379	      - 0.07
380	      - 0.07
381	  figures_description:
382	  - 'Figure 7: Paired accuracy comparison (original vs reformulated) for contaminated
383	    vs clean items, split by model type (SFT vs RL). Clear separation for SFT, collapsed
384	    for RL.'
385	  - 'Figure 8: ConStat detection power curve across effect size spectrum, overlaid
386	    with DIF power curve. Crossover around δ≈1.0 shows complementary regions.'
387	  analysis: 'ConStat在non-RL模型上的medium-effect-size检测力（δ≥0.6: TPR=0.68）验证了其在 ensemble中的角色——填补DIF在small-to-medium
388	    effects上的盲区。RL条件下的急剧退化 （TPR从0.68→0.31）与Wang et al.的发现一致，因为perturbation sensitivity本质上仍
389	    依赖于surface-form specific memorization pattern，RL训练将其平滑化。FDR控制在 non-RL条件下有效（0.048
390	    < 0.05），但RL条件下FDR升至0.12，需在ensemble中对RL模型 降低ConStat权重。
391	
392	    '
393	- name: dvd_generation_variance_eval
394	  plan_id: plan_003b
395	  description: '独立评估DVD generation variance在MMLU上的检测力，对10-15个open-weight模型 每item生成50次response，计算generation
396	    variance分数，检测bimodal distributions。
397	
398	    '
399	  expected_results:
400	    n_models_evaluated: 12
401	    n_items_evaluated: 2000
402	    responses_per_item: 50
403	    temperature_range:
404	    - 0.7
405	    - 1.0
406	    dvd_tpr_variant_contamination: 0.65
407	    dvd_tpr_verbatim_contamination: 0.38
408	    dvd_tpr_all_contamination: 0.52
409	    dvd_fpr: 0.07
410	    dvd_auroc_variant: 0.78
411	    dvd_auroc_verbatim: 0.62
412	    dvd_auroc_overall: 0.71
413	    bimodal_detection_rate_contaminated: 0.58
414	    bimodal_detection_rate_clean: 0.04
415	    dvd_tpr_rl_variant: 0.47
416	    dvd_tpr_rl_verbatim: 0.29
417	    generation_variance_contaminated_mean: 0.31
418	    generation_variance_clean_mean: 0.12
419	  result_rationale: 'DVD的检测逻辑基于generation variance：contaminated models在memorized items上的
420	    generation distribution呈现bimodal pattern——当temperature sampling触发"recall" mode时high
421	    confidence输出memorized answer，否则回到general reasoning mode。 Variant contamination（模型见过item的变体而非原始形式）下DVD最有效（TPR=0.65），
422	    因为variant exposure创造了partial memorization——模型"几乎记得"答案，导致生成 在confident recall和uncertain
423	    reasoning之间振荡，产生高variance和清晰的bimodality。 Verbatim contamination下DVD效果较差（TPR=0.38），因为完全memorized
424	    items的生成 variance反而很低（模型每次都确信地输出相同答案），bimodal signal消失。这使DVD与DIF 形成互补：DIF在verbatim
425	    large effects上最强，DVD在variant contamination上最强。 RL条件下DVD退化到TPR=0.47（variant），因为GRPO
426	    smoothing降低了generation variance 的discriminability，但退化幅度小于ConStat（因为DVD利用的是sampling-level
427	    variance 而非perturbation sensitivity，RL对sampling variance的影响弱于对perturbation response的影响）。
428	
429	    '
430	  tables:
431	  - title: 'Table 6: DVD Detection Power by Contamination Type'
432	    columns:
433	    - contamination_type
434	    - model_type
435	    - n_items
436	    - TPR
437	    - FPR
438	    - AUROC
439	    rows:
440	    - - variant
441	      - non_RL
442	      - 320
443	      - 0.65
444	      - 0.07
445	      - 0.78
446	    - - verbatim
447	      - non_RL
448	      - 480
449	      - 0.38
450	      - 0.07
451	      - 0.62
452	    - - all
453	      - non_RL
454	      - 800
455	      - 0.52
456	      - 0.07
457	      - 0.71
458	    - - variant
459	      - RL
460	      - 320
461	      - 0.47
462	      - 0.09
463	      - 0.68
464	    - - verbatim
465	      - RL
466	      - 480
467	      - 0.29
468	      - 0.09
469	      - 0.57
470	    - - all
471	      - RL
472	      - 800
473	      - 0.38
474	      - 0.09
475	      - 0.63
476	  figures_description:
477	  - 'Figure 9: Distribution of generation variance scores for contaminated (variant
478	    vs verbatim) and clean items. Variant contamination shows clear right shift; verbatim
479	    shows compressed distribution.'
480	  - 'Figure 10: Bimodality coefficient heatmap across items and models, with contamination
481	    status overlay. Clear bimodal clusters for variant-contaminated items.'
482	  analysis: 'DVD填补了ensemble中的variant contamination盲区。DIF主要检测verbatim large effects
483	    （模型在original item上的behavioral anomaly），ConStat检测non-RL medium effects， DVD则捕获variant
484	    contamination——模型见过类似但不完全相同的items，产生partial memorization的generation variance signal。三者的complementary
485	    coverage pattern 在best档下清晰呈现，为ensemble fusion提供了solid foundation。
486	
487	    '
488	- name: ensemble_fusion
489	  plan_id: plan_003c
490	  description: '融合DIF + ConStat + DVD为multi-signal ensemble。校准per-signal阈值， 评估majority
491	    voting和weighted fusion，展示ensemble coverage覆盖全effect-size谱。
492	
493	    '
494	  expected_results:
495	    ensemble_tpr_full_spectrum: 0.87
496	    ensemble_tpr_delta_ge_1_4: 0.91
497	    ensemble_tpr_delta_ge_1_0: 0.85
498	    ensemble_tpr_delta_ge_0_6: 0.78
499	    ensemble_fpr: 0.08
500	    ensemble_auroc: 0.93
501	    majority_2of3_tpr: 0.72
502	    majority_2of3_fpr: 0.04
503	    weighted_fusion_tpr: 0.87
504	    weighted_fusion_fpr: 0.08
505	    dif_unique_detections_pct: 0.28
506	    constat_unique_detections_pct: 0.15
507	    dvd_unique_detections_pct: 0.12
508	    all_three_overlap_pct: 0.31
509	    two_signal_overlap_pct: 0.14
510	    ensemble_tpr_rl_models: 0.82
511	    ensemble_tpr_non_rl_models: 0.9
512	    optimal_weights_dif: 0.45
513	    optimal_weights_constat: 0.3
514	    optimal_weights_dvd: 0.25
515	  result_rationale: 'Ensemble的power来源于三信号的systematic complementarity。在best档下，每个信号
516	    覆盖不同的effect-size × model-type区间：DIF覆盖large effects（δ≥1.4）且RL-robust， ConStat覆盖non-RL
517	    medium effects（δ≥0.6），DVD覆盖variant contamination。 Weighted fusion（DIF=0.45, ConStat=0.30,
518	    DVD=0.25）优于majority voting （TPR 0.87 vs 0.72），因为majority voting要求至少2/3信号agree，而在信号覆盖不
519	    重叠的区间（如RL+large effect只有DIF有效），single-signal detection被majority voting过滤掉。Weighted
520	    fusion允许high-confidence single signal触发detection。 Full-spectrum TPR=0.87的构成：δ≥1.4区间DIF主导（TPR=0.91），δ=0.6-1.4区间ConStat
521	    补位（将DIF单独的~0.40 TPR提升到ensemble的0.78），variant contamination区间DVD 补位（unique detections
522	    12%）。FPR=0.08略高于single-signal的0.04-0.07，这是 multi-signal fusion的inherent trade-off——更多信号意味着更多false
523	    positive opportunities，但0.08仍在可接受范围内。RL模型上ensemble TPR=0.82（vs non-RL的0.90）， 差距来自ConStat在RL条件下的退化被DIF的RL-robustness部分补偿。
524	
525	    '
526	  tables:
527	  - title: 'Table 7: Ensemble vs Individual Signal Detection Power'
528	    columns:
529	    - method
530	    - tpr_full
531	    - tpr_ge_1_4
532	    - tpr_ge_0_6
533	    - fpr
534	    - auroc
535	    rows:
536	    - - DIF_only
537	      - 0.58
538	      - 0.78
539	      - 0.35
540	      - 0.038
541	      - 0.84
542	    - - ConStat_only
543	      - 0.44
544	      - 0.62
545	      - 0.68
546	      - 0.06
547	      - 0.76
548	    - - DVD_only
549	      - 0.38
550	      - 0.38
551	      - 0.45
552	      - 0.07
553	      - 0.71
554	    - - Majority_2of3
555	      - 0.72
556	      - 0.81
557	      - 0.64
558	      - 0.04
559	      - 0.89
560	    - - Weighted_fusion
561	      - 0.87
562	      - 0.91
563	      - 0.78
564	      - 0.08
565	      - 0.93
566	  - title: 'Table 8: Signal Complementarity Analysis'
567	    columns:
568	    - detection_source
569	    - pct_of_total_detections
570	    - example_regime
571	    rows:
572	    - - DIF_unique
573	      - 0.28
574	      - Large effect + RL models
575	    - - ConStat_unique
576	      - 0.15
577	      - Medium effect + non-RL models
578	    - - DVD_unique
579	      - 0.12
580	      - Variant contamination
581	    - - DIF_and_ConStat
582	      - 0.08
583	      - Large effect + non-RL
584	    - - DIF_and_DVD
585	      - 0.04
586	      - Large variant + RL
587	    - - ConStat_and_DVD
588	      - 0.02
589	      - Medium variant + non-RL
590	    - - All_three
591	      - 0.31
592	      - Large effect + non-RL + verbatim
593	  figures_description:
594	  - 'Figure 11: Venn diagram of detections by three signals, showing complementary
595	    coverage with ~45% items detected by only one or two signals.'
596	  - 'Figure 12: Detection power heatmap across effect-size (δ) × model-type (SFT/RL)
597	    × contamination-type (verbatim/variant) grid. Each cell colored by which signal(s)
598	    contribute most.'
599	  - 'Figure 13: Precision-recall curves for individual signals vs ensemble. Ensemble
600	    dominates at all recall levels.'
601	  analysis: 'Ensemble coverage分析是Claim 2的核心evidence。三信号互补的清晰pattern—— DIF覆盖RL+large
602	    effects，ConStat覆盖non-RL+medium effects，DVD覆盖variant contamination——使full-spectrum
603	    TPR从任何单信号的最高0.58提升到0.87。 关键是unique detections分析：每个信号贡献12-28%的独占检测，证明任何单信号都不可替代。
604	    Weighted fusion优于majority voting 15pp，反映了信号互补性超过信号冗余性—— 在most detection regimes下只有1-2个信号active，majority
605	    voting的"2-of-3 agreement" 要求过于保守。
606	
607	    '
608	- name: cross_benchmark_gsm8k
609	  plan_id: plan_004
610	  description: '在GSM8K上复制DIF分析，用GSM1K作为contamination ground truth。 收集50+模型的per-item
611	    binary responses，运行temporal cohort DIF， 将DIF flags与per-model GSM8K-GSM1K accuracy
612	    gap关联。
613	
614	    '
615	  expected_results:
616	    n_models_gsm8k: 62
617	    n_items_gsm8k: 1319
618	    n_items_gsm1k: 1250
619	    cohort_pre2024_n: 28
620	    cohort_post2024_n: 34
621	    dif_flagged_items_gsm8k: 178
622	    dif_flagged_rate: 0.135
623	    dif_tpr_gsm8k_delta_ge_1_4: 0.74
624	    dif_fpr_gsm8k: 0.042
625	    gsm8k_gsm1k_gap_mean_all_models: 0.068
626	    gsm8k_gsm1k_gap_mean_contaminated_models: 0.112
627	    gsm8k_gsm1k_gap_mean_clean_models: 0.024
628	    gsm8k_gsm1k_gap_dif_correlation_spearman: 0.43
629	    gsm8k_gsm1k_gap_dif_correlation_pearson: 0.38
630	    per_item_dif_vs_gap_correlation: 0.41
631	    gsm8k_dif_auc: 0.88
632	  result_rationale: 'GSM8K是ideal validation target因为GSM1K提供了independent contamination
633	    ground truth—— GSM1K是GSM8K的分布匹配但全新的test set，GSM8K-GSM1K accuracy gap直接反映 contamination
634	    benefit。DIF在GSM8K上的TPR=0.74（vs MMLU的0.78）略低，因为： (1) 样本量较小（62 models vs MMLU的5055），cohort
635	    sizes（28 vs 34）接近power 下限；(2) GSM8K是math reasoning benchmark，item discrimination更依赖reasoning
636	    ability而非factual recall，DIF effect sizes分布略低于MMLU。Spearman rho=0.43 between per-model
637	    DIF flag count和GSM8K-GSM1K gap是中等相关，因为DIF flags是 binary item-level indicators而GSM8K-GSM1K
638	    gap是continuous model-level metric， 二者在aggregation level上不同——item-level DIF flag到model-level
639	    gap的mapping 需要通过contamination load（模型见过的flagged items数量）mediating。直接的 per-item
640	    correlation（item的DIF flag vs 该item的across-model gap）达到0.41， 提供convergent evidence。这一跨benchmark验证支持DIF检测的generalizability，
641	    不仅限于MMLU。
642	
643	    '
644	  tables:
645	  - title: 'Table 9: DIF Detection on GSM8K with GSM1K Ground Truth'
646	    columns:
647	    - metric
648	    - value
649	    rows:
650	    - - n_models
651	      - 62
652	    - - n_items
653	      - 1319
654	    - - DIF_flagged_items
655	      - 178
656	    - - DIF_flagged_rate
657	      - 0.135
658	    - - TPR_delta_ge_1_4
659	      - 0.74
660	    - - FPR
661	      - 0.042
662	    - - AUC
663	      - 0.88
664	    - - GSM8K-GSM1K_gap_DIF_corr_spearman
665	      - 0.43
666	  - title: 'Table 10: GSM8K-GSM1K Gap by Model Contamination Status'
667	    columns:
668	    - model_group
669	    - n_models
670	    - mean_gap
671	    - std_gap
672	    - median_gap
673	    rows:
674	    - - DIF_high_contamination
675	      - 18
676	      - 0.112
677	      - 0.034
678	      - 0.105
679	    - - DIF_low_contamination
680	      - 22
681	      - 0.051
682	      - 0.028
683	      - 0.047
684	    - - DIF_clean
685	      - 22
686	      - 0.024
687	      - 0.019
688	      - 0.02
689	  figures_description:
690	  - 'Figure 14: Scatter plot of per-model DIF contamination load (count of flagged
691	    items answered correctly) vs GSM8K-GSM1K accuracy gap. Positive trend with Spearman
692	    ρ=0.43.'
693	  - 'Figure 15: Item-level DIF magnitude (Δ_MH) distribution on GSM8K, overlaid with
694	    GSM1K-based ground truth labels.'
695	  analysis: '跨benchmark验证成功，DIF在GSM8K上的检测力（TPR=0.74）与MMLU结果一致（考虑到 较小样本量下的预期衰减）。GSM8K-GSM1K
696	    gap与DIF flags的spearman rho=0.43提供了 独立于MMLU-CF的external validation，使用完全不同的ground
697	    truth来源。 13.5%的GSM8K items被flagged，与Mirzadeh et al. (NeurIPS 2024)报告的GSM8K contamination
698	    prevalence一致。
699	
700	    '
701	- name: bifactor_irt_equating_pilot
702	  plan_id: plan_005
703	  description: '在METABENCH MMLU数据上pilot bifactor IRT equating。拟合bifactor model （general
704	    factor + subject-specific factors），选择anchor items， 通过fixed-parameter calibration校准replacement
705	    items，验证equated score等价性。
706	
707	    '
708	  expected_results:
709	    bifactor_model_converged: true
710	    n_general_factor_loadings_gt_0_3: 11200
711	    n_subject_factors: 57
712	    subject_factor_loading_mean: 0.42
713	    general_factor_loading_mean: 0.58
714	    general_factor_variance_explained: 0.48
715	    total_variance_explained: 0.72
716	    n_anchor_items_selected: 3100
717	    anchor_item_criteria: No DIF (ETS A), discrimination a>0.8, low missingness
718	    anchor_item_stability_rho: 0.98
719	    n_replacement_items_calibrated: 500
720	    equating_spearman_rho: 0.97
721	    equating_pearson_r: 0.96
722	    equating_rank_displacement_mean: 1.8
723	    equating_rank_displacement_max: 12
724	    equating_score_rmse: 0.021
725	    equating_classification_agreement: 0.94
726	    chi_square_equating_test_p: 0.34
727	    anchor_item_dif_free_rate: 0.92
728	    replacement_item_factor_loading_corr: 0.88
729	  result_rationale: 'Bifactor model在MMLU上的良好拟合源于MMLU的psychometric structure：它是multi-subject
730	    benchmark，每个subject（57个）构成一个specific factor，同时存在general cognitive ability factor（因为performance
731	    across subjects是正相关的——general intelligence drives cross-domain performance）。General
732	    factor解释48%方差，与educational testing中的typical bifactor results一致。Anchor items（3100个，~25%）是高稳定性、
733	    无DIF的items——在temporal cohorts间parameter estimates一致，表明未被contaminate。 25%的anchor
734	    rate在psychometric equating中是standard practice（Kolen & Brennan 推荐20-30%）。Equating后的Spearman
735	    rho=0.97表明模型rankings在original vs replaced benchmark间高度保持——rank displacement mean=1.8意味着平均每个模型只
736	    移动1-2个排名位置。这一精度来自fixed-parameter calibration的mechanics： replacement items的parameters在anchor
737	    item scale上calibrate，数学上保证了 score comparability（up to estimation error）。Score
738	    RMSE=0.021（在0-1 scale上） 反映estimation uncertainty而非systematic bias。Chi-square equating
739	    test p=0.34 表明无法拒绝"equated scores等价于original scores"的null hypothesis，即equating
740	    在统计上成功。
741	
742	    '
743	  tables:
744	  - title: 'Table 11: Bifactor Model Fit Statistics'
745	    columns:
746	    - metric
747	    - value
748	    rows:
749	    - - RMSEA
750	      - 0.028
751	    - - CFI
752	      - 0.96
753	    - - TLI
754	      - 0.95
755	    - - General_factor_variance_pct
756	      - 0.48
757	    - - Subject_factors_variance_pct
758	      - 0.24
759	    - - Total_variance_explained
760	      - 0.72
761	    - - N_subjects_factors
762	      - 57
763	  - title: 'Table 12: Equating Results — Original vs Replaced Benchmark'
764	    columns:
765	    - metric
766	    - value
767	    - interpretation
768	    rows:
769	    - - Spearman_rho
770	      - 0.97
771	      - Rankings nearly identical
772	    - - Pearson_r
773	      - 0.96
774	      - Scores linearly related
775	    - - RMSE
776	      - 0.021
777	      - Minimal score displacement
778	    - - Mean_rank_displacement
779	      - 1.8
780	      - Average 1-2 rank positions
781	    - - Max_rank_displacement
782	      - 12
783	      - Worst case still within noise
784	    - - Classification_agreement
785	      - 0.94
786	      - 94% same performance tier
787	    - - Chi_sq_test_p
788	      - 0.34
789	      - Cannot reject equivalence
790	  figures_description:
791	  - 'Figure 16: Scatter plot of model scores on original vs equated benchmark (500
792	    items replaced). Points tightly clustered along diagonal with Pearson r=0.96.'
793	  - 'Figure 17: Bifactor model path diagram for top-5 MMLU subjects showing general
794	    and subject-specific factor loadings.'
795	  - 'Figure 18: Rank displacement distribution — right-skewed with most models displaced
796	    by 0-3 positions.'
797	  analysis: 'Bifactor IRT equating在MMLU上达到psychometric standard（rho=0.97, RMSE=0.021），
798	    证明了Claim 3的可行性——contaminated items可以被replaced而preserving benchmark comparability。关键支撑是25%
799	    anchor items提供了stable calibration bridge， bifactor structure正确捕获了MMLU的multi-subject
800	    + general ability structure。 Classification agreement=0.94意味着在实际的model evaluation场景中，equated
801	    benchmark与original benchmark在94%的模型对比决策上给出相同结论。
802	
803	    '
804	- name: item_generation_calibration
805	  plan_id: plan_006
806	  description: '生成replacement items并通过student simulation校准。对比prompt-based difficulty
807	    targeting与empirical calibration的精度。在holdout model panel上验证。
808	
809	    '
810	  expected_results:
811	    n_items_generated: 500
812	    n_items_passing_quality_filter: 420
813	    quality_filter_pass_rate: 0.84
814	    n_student_sim_models: 8
815	    student_sim_responses_per_item: 200
816	    difficulty_rho_student_sim: 0.78
817	    difficulty_rho_prompt_targeting: 0.28
818	    difficulty_rmse_student_sim: 0.14
819	    difficulty_rmse_prompt_targeting: 0.38
820	    discrimination_rho_student_sim: 0.62
821	    discrimination_rho_prompt_targeting: 0.15
822	    holdout_panel_equating_rho: 0.95
823	    construct_validity_factor_loading_corr: 0.85
824	    subject_match_accuracy: 0.92
825	    cognitive_level_match_accuracy: 0.78
826	    item_format_compliance: 0.97
827	  result_rationale: 'Student simulation校准（基于arXiv 2601.09953方法）的核心优势是empirical—— 它通过让diverse
828	    student models实际回答generated items来estimate difficulty， 而非依赖LLM的self-report。rho=0.78与原论文报告的r=0.75-0.82一致，因为MMLU
829	    的MCQ format与student simulation的optimal use case对齐（forced-choice items 比open-ended
830	    items更适合binary response modeling）。Prompt-based targeting 的rho=0.28与arXiv 2602.06631报告的rho=0.10-0.45一致——LLMs在内省difficulty
831	    时系统性地低估hard items、高估easy items，因为difficulty perception与generation capability不同。Student
832	    simulation的优势在于它bypasses这种miscalibration， 直接从behavioral responses estimate difficulty。Discrimination的rho=0.62较低
833	    于difficulty的0.78，因为discrimination是IRT的second-order parameter（item sensitivity
834	    to ability differences），inherently harder to control through generation——它依赖item的specific
835	    cognitive demands，而这些难以通过prompt engineering精确控制。Construct validity factor loading
836	    correlation=0.85表明 generated items load on相同的subject-specific factors，preserving
837	    MMLU的 bifactor structure。
838	
839	    '
840	  tables:
841	  - title: 'Table 13: Calibration Method Comparison'
842	    columns:
843	    - method
844	    - difficulty_rho
845	    - difficulty_rmse
846	    - discrimination_rho
847	    - n_items
848	    rows:
849	    - - Student_simulation
850	      - 0.78
851	      - 0.14
852	      - 0.62
853	      - 420
854	    - - Prompt_targeting
855	      - 0.28
856	      - 0.38
857	      - 0.15
858	      - 420
859	    - - Random_baseline
860	      - 0.05
861	      - 0.52
862	      - 0.03
863	      - 420
864	  - title: 'Table 14: Generated Item Quality Metrics'
865	    columns:
866	    - metric
867	    - value
868	    rows:
869	    - - Quality_filter_pass_rate
870	      - 0.84
871	    - - Subject_match_accuracy
872	      - 0.92
873	    - - Cognitive_level_match
874	      - 0.78
875	    - - Format_compliance
876	      - 0.97
877	    - - Factor_loading_corr
878	      - 0.85
879	    - - Holdout_equating_rho
880	      - 0.95
881	  figures_description:
882	  - 'Figure 19: Scatter plot of estimated vs true difficulty for student simulation
883	    (rho=0.78) and prompt targeting (rho=0.28). Student simulation points cluster
884	    near diagonal; prompt targeting shows systematic bias.'
885	  - 'Figure 20: Factor loading comparison between original and generated items on
886	    same MMLU subjects. High correspondence (r=0.85) confirms construct preservation.'
887	  analysis: 'Student simulation校准是item regeneration pipeline的关键enabler，将difficulty
888	    estimation精度从prompt-based的rho=0.28提升到0.78——接近3x improvement。 这一结果支持Claim 3的"empirically
889	    calibrated alternatives"承诺。Holdout panel equating rho=0.95达到psychometric standard，证明end-to-end
890	    pipeline（generation → simulation calibration → equating）可以produce functionally
891	    equivalent benchmark items。
892	
893	    '
894	- name: cumulative_bayesian_dif
895	  plan_id: plan_007
896	  description: '实现Bayesian累积DIF先验。模拟4次连续benchmark administration， 展示evidence accumulation带来的power提升。
897	
898	    '
899	  expected_results:
900	    n_administrations_simulated: 4
901	    n_models_per_administration: 40
902	    admin_1_power_medium_delta_1_0: 0.38
903	    admin_2_cumulative_power: 0.55
904	    admin_3_cumulative_power: 0.7
905	    admin_4_cumulative_power: 0.78
906	    power_gain_per_administration:
907	    - 0.38
908	    - 0.17
909	    - 0.15
910	    - 0.08
911	    bayesian_bf_threshold: 3.0
912	    false_discovery_rate: 0.04
913	    convergence_rate: 0.98
914	    prior_posterior_shrinkage: 0.42
915	    credible_interval_width_admin1: 0.68
916	    credible_interval_width_admin4: 0.31
917	  result_rationale: 'Bayesian累积先验的power gain来自evidence accumulation的数学性质——每次新的 administration提供independent
918	    observations，posterior distribution随data收窄。 从single administration的0.38到4次累积的0.78，power
919	    nearly doubles。Gain是 diminishing的（0.17→0.15→0.08），因为posterior precision的improvement是
920	    sub-linear in sample size（~√n scaling）。对medium effects（δ=1.0）这尤其重要， 因为classical
921	    DIF在single administration with N=40 per cohort时power不足 （Phase 2模拟显示N=50/δ=1.0时TPR仅0.04-0.07）。Bayesian
922	    approach通过 accumulating evidence across time解决了这个sample-size limitation——每次 administration贡献40个models，4次累积相当于effective
923	    sample of ~160， 但通过informative priors获得比simple pooling更高的statistical efficiency。
924	    BF threshold=3.0（moderate evidence）对应psychometric practice中的standard decision
925	    criterion。FDR=0.04 < 0.05表明error control有效。
926	
927	    '
928	  tables:
929	  - title: 'Table 15: Cumulative Bayesian DIF Power Over Administrations'
930	    columns:
931	    - administration
932	    - cumulative_n
933	    - power_delta_1_0
934	    - power_delta_1_4
935	    - CI_width
936	    rows:
937	    - - 1
938	      - 40
939	      - 0.38
940	      - 0.62
941	      - 0.68
942	    - - 2
943	      - 80
944	      - 0.55
945	      - 0.76
946	      - 0.48
947	    - - 3
948	      - 120
949	      - 0.7
950	      - 0.84
951	      - 0.37
952	    - - 4
953	      - 160
954	      - 0.78
955	      - 0.88
956	      - 0.31
957	  figures_description:
958	  - 'Figure 21: Power accumulation curves across 4 administrations for δ=0.6, 1.0,
959	    1.4. All show diminishing returns but substantial gains.'
960	  - 'Figure 22: Posterior distribution evolution for a representative DIF-flagged
961	    item across 4 administrations, showing progressive shrinkage toward true effect.'
962	  analysis: 'Bayesian累积DIF直接回应reviewer concern #2（sample sizes too small）。 4次累积后medium-effect
963	    power从0.38→0.78，使DIF对medium effects也实用化。 这一结果支持论文的"living benchmark"叙事——不需要一次性获得大样本，
964	    可以通过temporal accumulation逐步建立detection confidence。
965	
966	    '
967	- name: graceful_degradation_analysis
968	  plan_id: plan_008
969	  description: '分析benchmark在progressive item replacement下的validity degradation。 定义validity
970	    metrics，模拟5%-50% replacement，建立理论bounds。
971	
972	    '
973	  expected_results:
974	    replacement_rates:
975	    - 0.05
976	    - 0.1
977	    - 0.2
978	    - 0.5
979	    ranking_stability_rho_5pct: 0.99
980	    ranking_stability_rho_10pct: 0.97
981	    ranking_stability_rho_20pct: 0.95
982	    ranking_stability_rho_50pct: 0.89
983	    score_reliability_alpha_original: 0.94
984	    score_reliability_alpha_5pct: 0.93
985	    score_reliability_alpha_10pct: 0.93
986	    score_reliability_alpha_20pct: 0.91
987	    score_reliability_alpha_50pct: 0.87
988	    construct_coverage_jaccard_5pct: 0.98
989	    construct_coverage_jaccard_10pct: 0.96
990	    construct_coverage_jaccard_20pct: 0.92
991	    construct_coverage_jaccard_50pct: 0.83
992	    theoretical_rho_lower_bound_formula: rho >= 1 - k*replacement_rate*(1-r_replacement)
993	    theoretical_rho_lower_bound_20pct: 0.93
994	    empirical_rho_20pct: 0.95
995	    validity_threshold_replacement_rate: 0.35
996	  result_rationale: 'Graceful degradation的数学基础是：如果replacement items与original items测量相同
997	    construct（通过bifactor equating保证），且parameter estimation是unbiased的， 那么benchmark
998	    score的perturbation仅来自estimation error。Ranking stability (Spearman rho)随replacement
999	    rate的下降是approximately linear的：5%→0.99, 10%→0.97, 20%→0.95, 50%→0.89。0.95 threshold（psychometric
1000	    standard for "essentially equivalent"）在~20% replacement rate时hit——这意味着可以替换 最多20%的items（~2500
1001	    items on MMLU）while maintaining psychometrically equivalent rankings。50% replacement导致rho=0.89，仍然usable但not
1002	    equivalent。 Score reliability (Cronbach''s alpha)从0.94降至0.91 at 20%，因为replacement
1003	    items的discrimination estimates有更大variance（calibration uncertainty）， but alpha>0.90在psychometric
1004	    standards中仍属excellent。Construct coverage (Jaccard similarity of subject factor
1005	    coverage)在20%时为0.92，因为replacement item generation已constrained to same subject，但minor
1006	    gaps in specific cognitive sub-skills可能出现。Theoretical lower bound formula provides
1007	    conservative estimate，empirical results consistently exceed it（0.95 > 0.93 at
1008	    20%），validating the bound''s correctness。
1009	
1010	    '
1011	  tables:
1012	  - title: 'Table 16: Validity Metrics Under Progressive Replacement'
1013	    columns:
1014	    - replacement_rate
1015	    - ranking_rho
1016	    - reliability_alpha
1017	    - construct_jaccard
1018	    - score_rmse
1019	    rows:
1020	    - - 0.0
1021	      - 1.0
1022	      - 0.94
1023	      - 1.0
1024	      - 0.0
1025	    - - 0.05
1026	      - 0.99
1027	      - 0.93
1028	      - 0.98
1029	      - 0.008
1030	    - - 0.1
1031	      - 0.97
1032	      - 0.93
1033	      - 0.96
1034	      - 0.015
1035	    - - 0.2
1036	      - 0.95
1037	      - 0.91
1038	      - 0.92
1039	      - 0.025
1040	    - - 0.35
1041	      - 0.92
1042	      - 0.89
1043	      - 0.87
1044	      - 0.038
1045	    - - 0.5
1046	      - 0.89
1047	      - 0.87
1048	      - 0.83
1049	      - 0.052
1050	  - title: 'Table 17: Theoretical vs Empirical Bounds'
1051	    columns:
1052	    - replacement_rate
1053	    - theoretical_rho_lb
1054	    - empirical_rho
1055	    - bound_tight
1056	    rows:
1057	    - - 0.05
1058	      - 0.97
1059	      - 0.99
1060	      - false
1061	    - - 0.1
1062	      - 0.95
1063	      - 0.97
1064	      - false
1065	    - - 0.2
1066	      - 0.93
1067	      - 0.95
1068	      - false
1069	    - - 0.5
1070	      - 0.84
1071	      - 0.89
1072	      - false
1073	  figures_description:
1074	  - 'Figure 23: Validity degradation curves (rho, alpha, Jaccard) vs replacement rate,
1075	    with 0.95 threshold line marking ''psychometrically equivalent'' zone.'
1076	  - 'Figure 24: Theoretical lower bound vs empirical results, showing bound is conservative
1077	    but informative.'
1078	  analysis: 'Graceful degradation分析为benchmark regeneration建立了formal safety guarantees。
1079	    20% replacement threshold（rho≥0.95）为实际操作提供了clear guideline—— given MMLU上约10.7%
1080	    items被DIF flagged（plan_001），单轮replacement在安全范围内。 理论bound的conservativeness（empirical
1081	    consistently exceeds theoretical by 2-5pp） 提供额外safety margin。这一结果完成了Claim 3从detection
1082	    → generation → equating → validity guarantee的完整pipeline。
1083	
1084	    '
1085	- name: item_focused_trees
1086	  plan_id: plan_009
1087	  description: '实现Item-Focused Trees作为categorical cohort DIF的替代方案。 将model release
1088	    date作为continuous covariate，比较检测力和灵活性。
1089	
1090	    '
1091	  expected_results:
1092	    ift_tpr_delta_ge_1_4: 0.81
1093	    ift_tpr_delta_ge_1_0: 0.58
1094	    ift_fpr: 0.044
1095	    ift_auc: 0.9
1096	    ift_vs_ets_c_tpr_improvement: 0.03
1097	    ift_vs_ets_c_auc_improvement: -0.02
1098	    ift_detected_gradual_contamination: true
1099	    n_items_with_changepoint: 890
1100	    median_changepoint_date: 2023-06
1101	    changepoint_clustering_by_subject: true
1102	    ift_computation_time_seconds: 340
1103	    ets_c_computation_time_seconds: 28
1104	  result_rationale: 'Item-Focused Trees的优势在于不需要arbitrary cohort splits——它自动发现每个item
1105	    的contamination onset point（changepoint）作为tree split。TPR=0.81略优于 ETS C的0.78（+3pp），因为IFT可以为每个item找到optimal
1106	    focal/reference split 而非使用统一的pre/post cutoff。但AUC=0.90略低于ETS C的0.92，因为IFT在small
1107	    effects区间的precision较低（tree splitting在low-signal regime容易overfit）。 Changepoint
1108	    clustering by subject是重要的secondary finding——STEM subjects的 median changepoint早于humanities（2023-03
1109	    vs 2023-09），反映code-heavy training data对STEM contamination的earlier onset。890个items有detectable
1110	    changepoints， 与plan_001的1340 flagged items部分重叠（IFT的threshold更conservative因为tree
1111	    pruning）。计算成本是ETS C的12x，因为recursive partitioning需要对每个item 搜索所有可能splits，但仍在minutes级别（CPU
1112	    only），实际可用。IFT的主要paper value 是methodological：它证明contamination timing是item-specific而非cohort-uniform，
1113	    支持"contamination as gradual process"的narrative。
1114	
1115	    '
1116	  tables:
1117	  - title: 'Table 18: Item-Focused Trees vs ETS C Comparison'
1118	    columns:
1119	    - method
1120	    - tpr_ge_1_4
1121	    - tpr_ge_1_0
1122	    - fpr
1123	    - auc
1124	    - time_sec
1125	    rows:
1126	    - - ETS_C
1127	      - 0.78
1128	      - 0.45
1129	      - 0.038
1130	      - 0.92
1131	      - 28
1132	    - - Item_Focused_Trees
1133	      - 0.81
1134	      - 0.58
1135	      - 0.044
1136	      - 0.9
1137	      - 340
1138	    - - Combined
1139	      - 0.84
1140	      - 0.6
1141	      - 0.048
1142	      - 0.93
1143	      - 368
1144	  - title: 'Table 19: Contamination Changepoint Analysis'
1145	    columns:
1146	    - subject_group
1147	    - n_items_with_changepoint
1148	    - median_changepoint
1149	    - range
1150	    rows:
1151	    - - STEM
1152	      - 520
1153	      - 2023-03
1154	      - 2022-06 to 2024-01
1155	    - - Humanities
1156	      - 210
1157	      - 2023-09
1158	      - 2023-01 to 2024-06
1159	    - - Social_Sciences
1160	      - 160
1161	      - 2023-06
1162	      - 2022-09 to 2024-03
1163	  figures_description:
1164	  - 'Figure 25: Item-level changepoint distribution across calendar time, colored
1165	    by subject. STEM items show earlier contamination onset.'
1166	  - 'Figure 26: Example Item-Focused Tree for a specific MMLU item, showing splits
1167	    on release date and model family.'
1168	  analysis: IFT作为P2实验提供了methodological depth——contamination timing的item-specific 和subject-specific
1169	    patterns是novel finding，支持论文的temporal dynamics narrative。 Detection power的marginal
1170	    improvement（+3pp TPR）不足以替代ETS C作为primary method，但combined approach（union of flags）将TPR推到0.84。更重要的是IFT的
1171	    changepoint analysis为understanding contamination dynamics提供了unique evidence， 可作为analysis
1172	    section的secondary contribution。
1173	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4d3894d-c789-43b6-a262-3bba36b1ac7e",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "e32ef337-059a-431b-90d5-e08e7b25947b",
  "sourceToolAssistantUUID": "d4d3894d-c789-43b6-a262-3bba36b1ac7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-20T20:12:49.282Z_

Now let me also read the experiment plan and literature map for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e32ef337-059a-431b-90d5-e08e7b25947b",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERyG8jKbmdZzDdJDcqm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4354c30e-552f-4047-aecf-5e61883aeaec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZ9m3qxeu3KgeYZRBsn5dX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37945,
      "cache_read_input_tokens": 40528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37945,
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

_source line 38 · 2026-05-20T20:12:51.168Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AexNeH9pCQn4kRCQcADCA3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4354c30e-552f-4047-aecf-5e61883aeaec",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERyG8jKbmdZzDdJDcqm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c828749b-f7cb-4e5c-9e41-d811dea40b69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZ9m3qxeu3KgeYZRBsn5dX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37945,
      "cache_read_input_tokens": 40528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37945,
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

_source line 39 · 2026-05-20T20:12:51.173Z_

<details><summary>↩ Tool result · `toolu_01AexNeH9pCQn4kRCQcADCA3`</summary>

```text
1	experiments:
2	  # === P0: Headline Results (must run) ===
3	
4	  - id: plan_001
5	    name: real_data_dif_mmlu
6	    claim: 1
7	    description: >
8	      Apply DIF analysis to METABENCH MMLU response matrix (5,219 models × 12,508 items).
9	      Data characteristics: only 37% models classifiable by family (1,929); effective temporal
10	      span ~1.5 years (2023: N=1,253, 2024-H1: N=656); 15.4% items have negative discrimination.
11	      Design:
12	      (a) Primary cohort: temporal split (2023 vs 2024-H1, both N≥80 ✓)
13	      (b) Alternative cohort: accuracy-quintile split (ability-based grouping, uses all models)
14	      (c) Item filtering: run with and without negative-discrimination items (sensitivity analysis)
15	      Run ETS C DIF detection on all items under both cohort definitions.
16	      Validate against MMLU-CF (ACL 2025) contamination-free items as partial ground truth.
17	      Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix.
18	    priority: P0
19	    gpu_budget_hours: 0
20	    deps: []
21	    registry_id: ""
22	
23	  - id: plan_002
24	    name: rl_robustness_validation
25	    claim: 1
26	    description: >
27	      Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:
28	      - "Alignment RL" (DPO/ORPO/KTO) = offline preference optimization, does NOT produce
29	        the NLL gap contraction that Wang et al. demonstrate. METABENCH has 477 such models.
30	      - "Reasoning RL" (GRPO/PPO online training) = the mechanism that conceals contamination
31	        signals. This is what Claim 1 targets. METABENCH has almost none of these.
32	      Design: (a) SFT-only cohort from METABENCH, (b) alignment-RL cohort (DPO/ORPO) from
33	      METABENCH as intermediate control, (c) reasoning-RL cohort via inference on 10-15
34	      open-weight GRPO/PPO models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) on MMLU.
35	      Run DIF + traditional detectors (Min-K%, ConStat, DVD) on all three scenarios.
36	      Show: DIF maintains power across all three; traditional detectors degrade specifically
37	      on reasoning-RL cohort (c). The 3-way comparison strengthens the argument by showing
38	      alignment RL is NOT the threat (detectors still work), reasoning RL IS (detectors fail,
39	      DIF doesn't).
40	    priority: P0
41	    gpu_budget_hours: 100
42	    deps: [plan_001]
43	    registry_id: ""
44	
45	  - id: plan_003a
46	    name: constat_perturbation_eval
47	    claim: 2
48	    description: >
49	      Independent evaluation of ConStat-style perturbation testing on MMLU:
50	      (a) Generate semantically equivalent reformulations for 200+ MMLU items using LLM paraphrasing
51	      (b) Compare model performance on original vs reformulated items
52	      (c) Apply FDR-controlled detection (ConStat protocol)
53	      (d) Characterize detection power by effect size — expected strength on non-RL models, weakness on RL
54	      Even if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.
55	    priority: P0
56	    gpu_budget_hours: 80
57	    deps: [plan_001]
58	    registry_id: ""
59	
60	  - id: plan_003b
61	    name: dvd_generation_variance_eval
62	    claim: 2
63	    description: >
64	      Independent evaluation of DVD generation variance on MMLU:
65	      (a) Select 10-15 open-weight models with inference access
66	      (b) Generate 50 responses per item via temperature sampling (T=0.7-1.0)
67	      (c) Compute generation variance scores; detect bimodal distributions (contamination signal)
68	      (d) Characterize detection power for variant contamination vs verbatim contamination
69	      Standalone results provide variant-contamination detection baseline independent of DIF.
70	    priority: P0
71	    gpu_budget_hours: 70
72	    deps: [plan_001]
73	    registry_id: ""
74	
75	  - id: plan_003c
76	    name: ensemble_fusion
77	    claim: 2
78	    description: >
79	      Fuse DIF + ConStat + DVD into multi-signal ensemble:
80	      (a) Calibrate per-signal thresholds on subset of items with known contamination status
81	      (b) Evaluate 2-of-3 majority voting and weighted fusion strategies
82	      (c) Show ensemble coverage: DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant
83	      (d) Precision analysis: ensemble FPR<0.10 across all configurations
84	      Depends on 003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.
85	    priority: P0
86	    gpu_budget_hours: 0
87	    deps: [plan_001, plan_003a, plan_003b]
88	    registry_id: ""
89	
90	  # === P1: Strengthening Evidence ===
91	
92	  - id: plan_004
93	    name: cross_benchmark_gsm8k
94	    claim: 1
95	    description: >
96	      Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.
97	      Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard data
98	      or inference). Run DIF across temporal cohorts. Correlate DIF flags with
99	      per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability
100	      and provides an independent ground truth beyond MMLU-CF.
101	    priority: P1
102	    gpu_budget_hours: 100
103	    deps: [plan_001]
104	    registry_id: ""
105	
106	  - id: plan_005
107	    name: bifactor_irt_equating_pilot
108	    claim: 3
109	    description: >
110	      Pilot bifactor IRT equating on MMLU:
111	      (a) Fit bifactor model to METABENCH MMLU data (general factor + subject-specific factors)
112	      (b) Select anchor items (high-stability, no DIF across cohorts)
113	      (c) Calibrate replacement items via fixed-parameter calibration (Kim & Kolen 2019)
114	      (d) Demonstrate equated score equivalence: model rankings on original vs replaced benchmark
115	      should correlate at Spearman rho ≥ 0.95 after equating.
116	    priority: P1
117	    gpu_budget_hours: 50
118	    deps: [plan_001]
119	    registry_id: ""
120	
121	  - id: plan_006
122	    name: item_generation_calibration
123	    claim: 3
124	    description: >
125	      Generate replacement items for DIF-flagged MMLU questions:
126	      (a) Use LLM generation with construct constraints (same subject, same cognitive level)
127	      (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty estimation)
128	      (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45 per arXiv 2602.06631)
129	      vs empirical calibration via student simulation
130	      (d) Validate on holdout model panel
131	    priority: P1
132	    gpu_budget_hours: 200
133	    deps: [plan_005]
134	    registry_id: ""
135	
136	  # === P2: Bonus / Extension ===
137	
138	  - id: plan_007
139	    name: cumulative_bayesian_dif
140	    claim: 1
141	    description: >
142	      Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).
143	      Simulate 4 successive benchmark administrations. Show power improvement
144	      from accumulating evidence: individual administration power ~0.40
145	      → cumulative power ~0.70 after 3 administrations for medium effects (δ=1.0).
146	    priority: P2
147	    gpu_budget_hours: 0
148	    deps: [plan_001]
149	    registry_id: ""
150	
151	  - id: plan_008
152	    name: graceful_degradation_analysis
153	    claim: 3
154	    description: >
155	      Formal analysis of benchmark validity under item replacement:
156	      (a) Define validity metrics (ranking stability, score reliability, construct coverage)
157	      (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced)
158	      (c) Establish theoretical bounds on validity degradation as function of replacement rate
159	      (d) Empirical validation using METABENCH data
160	    priority: P2
161	    gpu_budget_hours: 0
162	    deps: [plan_005, plan_006]
163	    registry_id: ""
164	
165	  - id: plan_009
166	    name: item_focused_trees
167	    claim: 1
168	    description: >
169	      Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative to
170	      categorical cohort DIF. Treat model release date as continuous covariate.
171	      Compare detection power and flexibility vs categorical DIF.
172	      Advantages: avoids arbitrary cohort splits, uses full model sample.
173	    priority: P2
174	    gpu_budget_hours: 0
175	    deps: [plan_001]
176	    registry_id: ""
177	
178	# GPU Budget Summary:
179	# P0: 250 hours (plan_001: 0h + plan_002: 100h + plan_003a: 80h + plan_003b: 70h + plan_003c: 0h)
180	# P1: 350 hours (plan_004: 100h + plan_005: 50h + plan_006: 200h)
181	# P2: 0 hours (all simulation/analysis)
182	# Total: 600 hours (within 900-1200h project budget, leaving margin for reruns)
183	# Claim 2 resilience: if one signal fails, 2-signal ensemble still publishable
184	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c828749b-f7cb-4e5c-9e41-d811dea40b69",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "14068588-7897-48ae-9b90-2a8d845d1905",
  "sourceToolAssistantUUID": "c828749b-f7cb-4e5c-9e41-d811dea40b69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T20:12:51.520Z_

<details open><summary>🔧 Tool call — Read · `toolu_018eeUgz62kYN5xXx7GsynX3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14068588-7897-48ae-9b90-2a8d845d1905",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERyG8jKbmdZzDdJDcqm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcef2627-26ac-4214-9e0d-0d277b67ac4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZ9m3qxeu3KgeYZRBsn5dX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37945,
      "cache_read_input_tokens": 40528,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 37945
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 40528,
          "cache_creation_input_tokens": 37945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 37945,
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

_source line 41 · 2026-05-20T20:12:51.537Z_

<details><summary>↩ Tool result · `toolu_018eeUgz62kYN5xXx7GsynX3`</summary>

```text
1	meta:
2	  last_updated: "2026-05-20T17:30:00.000Z"
3	  total_papers: 10
4	categories:
5	  - key: "contamination_detection"
6	    name: "Benchmark Contamination Detection"
7	    narrative: "Methods for detecting training data contamination in LLM benchmarks, including RL-robust approaches"
8	  - key: "irt_equating"
9	    name: "IRT Methodology & Equating"
10	    narrative: "Item Response Theory models, calibration, equating, and their application to LLM evaluation"
11	  - key: "benchmark_design"
12	    name: "Dynamic Benchmark Design"
13	    narrative: "Approaches for creating contamination-resistant or self-updating benchmarks"
14	  - key: "dif_methodology"
15	    name: "DIF Statistical Methods"
16	    narrative: "Differential Item Functioning detection methods, power analysis, and small-sample strategies"
17	  - key: "item_generation"
18	    name: "Automated Item Generation"
19	    narrative: "LLM-based test item generation with difficulty control and psychometric validation"
20	papers:
21	  wang2026fragility:
22	    title: "On The Fragility of Benchmark Contamination Detection in Reasoning Models"
23	    authors:
24	      - "Wang, Y."
25	    year: 2026
26	    venue: "ICLR 2026"
27	    doi: ""
28	    url: "https://arxiv.org/abs/2510.02386"
29	    bibtex_key: "wang2026fragility"
30	    category: "contamination_detection"
31	    role: "foundation"
32	    relevance: "Proves GRPO/PPO RL training conceals contamination signals (14-20pp AUROC degradation), motivating our DIF-based approach which operates on behavioral patterns immune to NLL smoothing"
33	    abstract: ""
34	    semantic_scholar_id: ""
35	    verified: false
36	    added_by: "director"
37	    added_at: "2026-05-20T17:30:00.000Z"
38	  liang2026dvd:
39	    title: "DVD: Detection via Variance of Generation Distribution for Variant Contamination"
40	    authors:
41	      - "Liang, Y."
42	    year: 2026
43	    venue: "arXiv"
44	    doi: ""
45	    url: "https://arxiv.org/abs/2601.04895"
46	    bibtex_key: "liang2026dvd"
47	    category: "contamination_detection"
48	    role: "direct-competitor"
49	    relevance: "Detects variant contamination via generation variance (AUC 0.73-0.74 vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under RL training"
50	    abstract: ""
51	    semantic_scholar_id: ""
52	    verified: false
53	    added_by: "director"
54	    added_at: "2026-05-20T17:30:00.000Z"
55	  tao2026selfcritique:
56	    title: "Detecting Data Contamination from Reinforcement Learning Post-training"
57	    authors:
58	      - "Tao, S."
59	    year: 2026
60	    venue: "ICLR 2026"
61	    doi: ""
62	    url: "https://arxiv.org/abs/2510.09259"
63	    bibtex_key: "tao2026selfcritique"
64	    category: "contamination_detection"
65	    role: "direct-competitor"
66	    relevance: "Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse detection, but remains individual-model-level; our DIF is group-level and complementary"
67	    abstract: ""
68	    semantic_scholar_id: ""
69	    verified: false
70	    added_by: "director"
71	    added_at: "2026-05-20T17:30:00.000Z"
72	  polo2026growingpains:
73	    title: "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration"
74	    authors:
75	      - "Polo, F."
76	    year: 2026
77	    venue: "arXiv"
78	    doi: ""
79	    url: ""
80	    bibtex_key: "polo2026growingpains"
81	    category: "irt_equating"
82	    role: "direct-competitor"
83	    relevance: "Uses multidimensional IRT with fixed-parameter calibration and 100 anchor items for extensible evaluation (rho>=0.9); addresses score comparability but NOT contamination detection or item regeneration"
84	    abstract: ""
85	    semantic_scholar_id: ""
86	    verified: false
87	    added_by: "director"
88	    added_at: "2026-05-20T17:30:00.000Z"
89	  polo2026psnirt:
90	    title: "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"
91	    authors:
92	      - "Polo, F."
93	    year: 2026
94	    venue: "AAAI 2026"
95	    doi: ""
96	    url: ""
97	    bibtex_key: "polo2026psnirt"
98	    category: "irt_equating"
99	    role: "method-component"
100	    relevance: "PSN-IRT analyzes benchmark quality via 4PL IRT; provides published IRT parameters for MMLU we can use in semi-synthetic validation"
101	    abstract: ""
102	    semantic_scholar_id: ""
103	    verified: false
104	    added_by: "director"
105	    added_at: "2026-05-20T17:30:00.000Z"
106	  white2025livebench:
107	    title: "LiveBench: A Challenging, Contamination-Free LLM Benchmark"
108	    authors:
109	      - "White, C."
110	    year: 2025
111	    venue: "ICLR 2025"
112	    doi: ""
113	    url: ""
114	    bibtex_key: "white2025livebench"
115	    category: "benchmark_design"
116	    role: "direct-competitor"
117	    relevance: "Monthly-updated contamination-free benchmark with objective scoring; no difficulty calibration or psychometric equivalence across updates"
118	    abstract: ""
119	    semantic_scholar_id: ""
120	    verified: false
121	    added_by: "director"
122	    added_at: "2026-05-20T17:30:00.000Z"
123	  zhang2024gsm1k:
124	    title: "A Careful Examination of Large Language Model Performance on Grade School Arithmetic"
125	    authors:
126	      - "Zhang, H."
127	    year: 2024
128	    venue: "arXiv"
129	    doi: ""
130	    url: "https://arxiv.org/abs/2405.00332"
131	    bibtex_key: "zhang2024gsm1k"
132	    category: "contamination_detection"
133	    role: "foundation"
134	    relevance: "GSM1K documents 10-13% average accuracy drops from contamination; provides ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4 logits) critical for our DIF power analysis"
135	    abstract: ""
136	    semantic_scholar_id: ""
137	    verified: false
138	    added_by: "director"
139	    added_at: "2026-05-20T17:30:00.000Z"
140	  hardy2026scalability:
141	    title: "Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients"
142	    authors:
143	      - "Hardy, M."
144	    year: 2026
145	    venue: "arXiv"
146	    doi: ""
147	    url: "https://arxiv.org/abs/2603.24999"
148	    bibtex_key: "hardy2026scalability"
149	    category: "irt_equating"
150	    role: "method-component"
151	    relevance: "Nonparametric signed isotonic R2 scalability coefficients outperform IRT item diagnostics; lightweight pre-filter for item quality before our parametric calibration"
152	    abstract: ""
153	    semantic_scholar_id: ""
154	    verified: false
155	    added_by: "director"
156	    added_at: "2026-05-20T17:30:00.000Z"
157	  kim2019fpc:
158	    title: "Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data"
159	    authors:
160	      - "Kim, S."
161	      - "Kolen, M."
162	    year: 2019
163	    venue: "Applied Measurement in Education"
164	    doi: ""
165	    url: ""
166	    bibtex_key: "kim2019fpc"
167	    category: "irt_equating"
168	    role: "method-component"
169	    relevance: "Fixed-parameter calibration requires only N>=200 vs N>=500 for full calibration; core methodology for our bifactor IRT equating with anchor items"
170	    abstract: ""
171	    semantic_scholar_id: ""
172	    verified: false
173	    added_by: "director"
174	    added_at: "2026-05-20T17:30:00.000Z"
175	  belzak2020smallsample:
176	    title: "Testing Differential Item Functioning in Small Samples"
177	    authors:
178	      - "Belzak, W."
179	    year: 2020
180	    venue: "Multivariate Behavioral Research"
181	    doi: ""
182	    url: ""
183	    bibtex_key: "belzak2020smallsample"
184	    category: "dif_methodology"
185	    role: "method-component"
186	    relevance: "Parsimonious logistic regression with sum scores outperforms complex IRT models for DIF detection in small samples; directly applicable to our N=50-80 model cohorts"
187	    abstract: ""
188	    semantic_scholar_id: ""
189	    verified: false
190	    added_by: "director"
191	    added_at: "2026-05-20T17:30:00.000Z"
192	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcef2627-26ac-4214-9e0d-0d277b67ac4e",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "d155baec-4144-4453-8592-3e1cf0604de7",
  "sourceToolAssistantUUID": "fcef2627-26ac-4214-9e0d-0d277b67ac4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-20T20:12:54.789Z_

Now let me also check the MVP experiment artifacts to understand what has actually been run vs. imagined.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d155baec-4144-4453-8592-3e1cf0604de7",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERyjsLVQH9YaUjZEyqi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91d1ce9f-8a15-4d91-bffc-26b521e21cc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ueePnUkmx4UPfU8HeyVXt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5996,
      "cache_read_input_tokens": 78473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5996,
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

_source line 43 · 2026-05-20T20:12:57.153Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QA8z3WXd1UhQQoaefG2GRF`</summary>

```json
{
  "pattern": "artifacts/mvp_dif_power_sim/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91d1ce9f-8a15-4d91-bffc-26b521e21cc1",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERyjsLVQH9YaUjZEyqi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b09717e-361a-4720-860f-a247959e9891",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ueePnUkmx4UPfU8HeyVXt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5996,
      "cache_read_input_tokens": 78473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5996,
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

_source line 44 · 2026-05-20T20:12:57.169Z_

<details><summary>↩ Tool result · `toolu_01QA8z3WXd1UhQQoaefG2GRF`</summary>

```text
artifacts/mvp_dif_power_sim/data/dif_power_results.csv
artifacts/mvp_dif_power_sim/chart/dif_power_curves.pdf
artifacts/mvp_dif_power_sim/data/dif_diagnostic_tpr_comparison.csv
artifacts/mvp_dif_power_sim/chart/dif_diagnostic_pvalue_dist.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b09717e-361a-4720-860f-a247959e9891",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "0b52e59f-c758-489b-a87f-539f4bd3b655",
  "sourceToolAssistantUUID": "3b09717e-361a-4720-860f-a247959e9891",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T20:12:57.578Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VAiAqVi5PxeZPL3j7YN6UW`</summary>

```json
{
  "pattern": "artifacts/mvp_dif_power_sim_phase2/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b52e59f-c758-489b-a87f-539f4bd3b655",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERyjsLVQH9YaUjZEyqi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45c71da5-7dce-4d7d-ac67-ceb63b07e800",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ueePnUkmx4UPfU8HeyVXt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5996,
      "cache_read_input_tokens": 78473,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5996
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 78473,
          "cache_creation_input_tokens": 5996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5996,
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

_source line 46 · 2026-05-20T20:12:57.611Z_

<details><summary>↩ Tool result · `toolu_01VAiAqVi5PxeZPL3j7YN6UW`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45c71da5-7dce-4d7d-ac67-ceb63b07e800",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "9dca65d6-6b89-41dd-ab07-38f978fcd040",
  "sourceToolAssistantUUID": "45c71da5-7dce-4d7d-ac67-ceb63b07e800",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T20:13:01.341Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Vew9BunActbJ3TeJXsg7iR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_power_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dca65d6-6b89-41dd-ab07-38f978fcd040",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERzC2wrN6QbbXSgjFzL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba9a8503-80d6-4296-b1de-3b794f9ff034",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NbpLbP9n2iPj4TQcJoNxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 393,
      "cache_read_input_tokens": 84469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 393,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 48 · 2026-05-20T20:13:01.349Z_

<details><summary>↩ Tool result · `toolu_01Vew9BunActbJ3TeJXsg7iR`</summary>

```text
1	n_per_group,delta,method,tpr,fpr,auc,ets_c_tpr,ets_c_fpr,n_reps,fpr_exceeds_015,verdict
2	30,0.4,MH,0.0001,0.0,0.5498,0.0381,0.0199,1000,False,N/A
3	30,0.4,LR,0.0019,0.0009,0.5495,,,1000,False,N/A
4	30,0.6,MH,0.0004,0.0,0.5921,0.0686,0.0204,1000,False,N/A
5	30,0.6,LR,0.0046,0.0011,0.5897,,,1000,False,N/A
6	30,0.8,MH,0.002,0.0,0.6358,0.1128,0.0208,1000,False,N/A
7	30,0.8,LR,0.0116,0.0011,0.6377,,,1000,False,N/A
8	30,1.0,MH,0.0052,0.0,0.6798,0.1767,0.0208,1000,False,N/A
9	30,1.0,LR,0.0269,0.0014,0.6919,,,1000,False,N/A
10	30,1.2,MH,0.014,0.0001,0.7148,0.2485,0.0215,1000,False,N/A
11	30,1.2,LR,0.0549,0.002,0.7389,,,1000,False,N/A
12	30,1.4,MH,0.0345,0.0001,0.7404,0.3215,0.0224,1000,False,N/A
13	30,1.4,LR,0.1016,0.0027,0.7802,,,1000,False,N/A
14	30,1.6,MH,0.0731,0.0001,0.7648,0.3923,0.023,1000,False,N/A
15	30,1.6,LR,0.1681,0.0037,0.8165,,,1000,False,N/A
16	50,0.4,MH,0.0006,0.0001,0.5866,0.0706,0.0265,1000,False,N/A
17	50,0.4,LR,0.0022,0.0006,0.5743,,,1000,False,N/A
18	50,0.6,MH,0.0031,0.0001,0.6562,0.1401,0.0268,1000,False,N/A
19	50,0.6,LR,0.0098,0.0008,0.6374,,,1000,False,N/A
20	50,0.8,MH,0.0131,0.0001,0.7186,0.2326,0.0276,1000,False,N/A
21	50,0.8,LR,0.0282,0.0009,0.7053,,,1000,False,N/A
22	50,1.0,MH,0.0416,0.0002,0.7733,0.3369,0.0295,1000,False,FAIL
23	50,1.0,LR,0.0703,0.0015,0.7683,,,1000,False,FAIL
24	50,1.2,MH,0.1013,0.0003,0.8141,0.4412,0.0306,1000,False,FAIL
25	50,1.2,LR,0.1532,0.0023,0.8189,,,1000,False,FAIL
26	50,1.4,MH,0.192,0.0006,0.8404,0.5346,0.0304,1000,False,FAIL
27	50,1.4,LR,0.2447,0.0035,0.8569,,,1000,False,FAIL
28	50,1.6,MH,0.2981,0.0008,0.8604,0.615,0.0326,1000,False,FAIL
29	50,1.6,LR,0.359,0.0047,0.8895,,,1000,False,FAIL
30	80,0.4,MH,0.0014,0.0001,0.6252,0.1168,0.0311,1000,False,N/A
31	80,0.4,LR,0.0038,0.0005,0.602,,,1000,False,N/A
32	80,0.6,MH,0.0126,0.0001,0.717,0.2361,0.0318,1000,False,N/A
33	80,0.6,LR,0.0206,0.0005,0.6916,,,1000,False,N/A
34	80,0.8,MH,0.0576,0.0003,0.796,0.3839,0.0336,1000,False,N/A
35	80,0.8,LR,0.0748,0.0012,0.7745,,,1000,False,N/A
36	80,1.0,MH,0.1645,0.0006,0.8484,0.5228,0.0353,1000,False,FAIL
37	80,1.0,LR,0.1874,0.002,0.836,,,1000,False,FAIL
38	80,1.2,MH,0.2979,0.001,0.8867,0.6367,0.0372,1000,False,FAIL
39	80,1.2,LR,0.3195,0.0035,0.8857,,,1000,False,FAIL
40	80,1.4,MH,0.4448,0.0019,0.9069,0.7254,0.04,1000,False,FAIL
41	80,1.4,LR,0.4681,0.005,0.9182,,,1000,False,FAIL
42	80,1.6,MH,0.5546,0.0027,0.918,0.7869,0.0436,1000,False,GRAY
43	80,1.6,LR,0.5762,0.0064,0.9397,,,1000,False,GRAY
44	100,0.4,MH,0.0036,0.0001,0.6525,0.1446,0.0333,1000,False,N/A
45	100,0.4,LR,0.006,0.0004,0.6266,,,1000,False,N/A
46	100,0.6,MH,0.0254,0.0002,0.7481,0.2938,0.0338,1000,False,N/A
47	100,0.6,LR,0.0322,0.0006,0.7224,,,1000,False,N/A
48	100,0.8,MH,0.1077,0.0005,0.831,0.4649,0.0354,1000,False,N/A
49	100,0.8,LR,0.12,0.0015,0.812,,,1000,False,N/A
50	100,1.0,MH,0.2613,0.0013,0.8796,0.6055,0.0383,1000,False,FAIL
51	100,1.0,LR,0.2693,0.0029,0.8658,,,1000,False,FAIL
52	100,1.2,MH,0.4171,0.002,0.9111,0.7184,0.0406,1000,False,FAIL
53	100,1.2,LR,0.429,0.0042,0.9102,,,1000,False,FAIL
54	100,1.4,MH,0.5613,0.0029,0.9293,0.7938,0.0434,1000,False,GRAY
55	100,1.4,LR,0.5693,0.0059,0.9386,,,1000,False,GRAY
56	100,1.6,MH,0.6817,0.0039,0.9393,0.8508,0.0472,1000,False,GRAY
57	100,1.6,LR,0.6869,0.0075,0.9593,,,1000,False,GRAY
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba9a8503-80d6-4296-b1de-3b794f9ff034",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "9060334c-06c0-42ae-b6ed-e2d5f44e9f63",
  "sourceToolAssistantUUID": "ba9a8503-80d6-4296-b1de-3b794f9ff034",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T20:13:01.956Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LrGotLawxfmLkYryufEhYD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_diagnostic_tpr_comparison.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9060334c-06c0-42ae-b6ed-e2d5f44e9f63",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERzC2wrN6QbbXSgjFzL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ab5fc89-da20-4a65-acd7-f9afc0c26d14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NbpLbP9n2iPj4TQcJoNxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 393,
      "cache_read_input_tokens": 84469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 393,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 50 · 2026-05-20T20:13:01.961Z_

<details><summary>↩ Tool result · `toolu_01LrGotLawxfmLkYryufEhYD`</summary>

```text
1	n_per_group,delta,method,tpr_raw,fpr_raw,tpr_bh,fpr_bh,tpr_bonf,fpr_bonf
2	30,0.4,MH,0.053,0.021,0.0,0.0,0.0,0.0
3	30,0.4,LR,0.126,0.0709,0.001,0.001,0.001,0.0008
4	30,0.6,MH,0.073,0.0199,0.001,0.0,0.001,0.0
5	30,0.6,LR,0.136,0.0719,0.008,0.0017,0.004,0.0011
6	30,0.8,MH,0.125,0.021,0.0,0.0,0.0,0.0
7	30,0.8,LR,0.206,0.0696,0.006,0.0009,0.005,0.0006
8	30,1.0,MH,0.2,0.0204,0.004,0.0,0.004,0.0
9	30,1.0,LR,0.278,0.0754,0.026,0.0013,0.019,0.0009
10	30,1.2,MH,0.26,0.0214,0.014,0.0,0.014,0.0
11	30,1.2,LR,0.346,0.0794,0.048,0.0017,0.037,0.0006
12	30,1.4,MH,0.344,0.0238,0.031,0.0001,0.023,0.0
13	30,1.4,LR,0.446,0.0727,0.103,0.0029,0.068,0.0006
14	30,1.6,MH,0.427,0.0204,0.054,0.0002,0.041,0.0001
15	30,1.6,LR,0.533,0.0716,0.147,0.0032,0.099,0.0009
16	50,0.4,MH,0.087,0.0272,0.0,0.0002,0.0,0.0
17	50,0.4,LR,0.124,0.0604,0.002,0.0008,0.002,0.0006
18	50,0.6,MH,0.146,0.0252,0.0,0.0,0.0,0.0
19	50,0.6,LR,0.193,0.0597,0.009,0.0006,0.007,0.0001
20	50,0.8,MH,0.235,0.0293,0.017,0.0006,0.015,0.0004
21	50,0.8,LR,0.287,0.0629,0.022,0.0011,0.019,0.0008
22	50,1.0,MH,0.36,0.0288,0.062,0.0002,0.042,0.0001
23	50,1.0,LR,0.394,0.0653,0.083,0.0012,0.055,0.0008
24	50,1.2,MH,0.443,0.0313,0.111,0.0003,0.063,0.0002
25	50,1.2,LR,0.466,0.0647,0.127,0.0019,0.082,0.0007
26	50,1.4,MH,0.544,0.0301,0.187,0.0002,0.116,0.0
27	50,1.4,LR,0.596,0.0632,0.245,0.0031,0.142,0.0003
28	50,1.6,MH,0.64,0.0311,0.29,0.0004,0.182,0.0
29	50,1.6,LR,0.677,0.0628,0.335,0.0041,0.22,0.0003
30	80,0.4,MH,0.131,0.0307,0.004,0.0,0.004,0.0
31	80,0.4,LR,0.152,0.0516,0.004,0.0004,0.004,0.0003
32	80,0.6,MH,0.232,0.0336,0.009,0.0001,0.007,0.0001
33	80,0.6,LR,0.262,0.0603,0.013,0.001,0.01,0.0007
34	80,0.8,MH,0.366,0.0356,0.054,0.0001,0.039,0.0
35	80,0.8,LR,0.383,0.065,0.075,0.0011,0.049,0.0003
36	80,1.0,MH,0.511,0.0322,0.143,0.0011,0.085,0.0002
37	80,1.0,LR,0.508,0.0602,0.174,0.0023,0.109,0.0003
38	80,1.2,MH,0.665,0.0371,0.295,0.0017,0.17,0.0001
39	80,1.2,LR,0.661,0.0603,0.334,0.0033,0.197,0.0004
40	80,1.4,MH,0.735,0.0437,0.428,0.0017,0.262,0.0001
41	80,1.4,LR,0.732,0.0672,0.452,0.0051,0.286,0.0006
42	80,1.6,MH,0.807,0.042,0.554,0.0038,0.378,0.0003
43	80,1.6,LR,0.802,0.0676,0.582,0.0071,0.38,0.0006
44	100,0.4,MH,0.168,0.0348,0.008,0.0002,0.007,0.0002
45	100,0.4,LR,0.184,0.0543,0.012,0.0004,0.01,0.0002
46	100,0.6,MH,0.285,0.0332,0.034,0.0002,0.027,0.0001
47	100,0.6,LR,0.304,0.0547,0.037,0.0006,0.031,0.0003
48	100,0.8,MH,0.479,0.0376,0.122,0.0004,0.079,0.0001
49	100,0.8,LR,0.474,0.059,0.12,0.0004,0.083,0.0001
50	100,1.0,MH,0.597,0.04,0.23,0.0011,0.147,0.0001
51	100,1.0,LR,0.603,0.0636,0.255,0.0028,0.166,0.0004
52	100,1.2,MH,0.749,0.0407,0.422,0.002,0.254,0.0003
53	100,1.2,LR,0.735,0.0684,0.435,0.005,0.256,0.0009
54	100,1.4,MH,0.797,0.0428,0.54,0.003,0.362,0.0
55	100,1.4,LR,0.79,0.0678,0.562,0.0057,0.381,0.0004
56	100,1.6,MH,0.893,0.0487,0.686,0.0041,0.484,0.0002
57	100,1.6,LR,0.878,0.0681,0.676,0.0079,0.503,0.0008
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ab5fc89-da20-4a65-acd7-f9afc0c26d14",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "e4711d20-4328-45ef-8ec5-fef2f011ab4d",
  "sourceToolAssistantUUID": "2ab5fc89-da20-4a65-acd7-f9afc0c26d14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-20T20:13:06.320Z_

I now have a thorough understanding of the paper, the experimental design, the review context, and the actual experimental evidence vs. imagined results. Let me also check for the IDEA_BRIEF to understand the original research conception.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4711d20-4328-45ef-8ec5-fef2f011ab4d",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERzWcPqgvpeWb1SfLxp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f68c01b2-f2ff-4964-8f8a-5346905057fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FomgJG7gpwt1rGTMD9F3dW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4676,
      "cache_read_input_tokens": 84862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4676,
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

_source line 52 · 2026-05-20T20:13:08.046Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SkbRULSbrzbXrf2NcsN1dZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f68c01b2-f2ff-4964-8f8a-5346905057fc",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERzWcPqgvpeWb1SfLxp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b3da728-d41c-40cc-99f2-b78348374784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FomgJG7gpwt1rGTMD9F3dW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4676,
      "cache_read_input_tokens": 84862,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4676
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 84862,
          "cache_creation_input_tokens": 4676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4676,
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

_source line 53 · 2026-05-20T20:13:08.340Z_

<details><summary>↩ Tool result · `toolu_01SkbRULSbrzbXrf2NcsN1dZ`</summary>

```text
1	# Idea Brief: Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating
2	
3	
4	- **Idea ID**: `idea_038`
5	- **Created**: 2026-05-20
6	- **Approved**: 2026-05-20
7	- **Source**: foreign:be-idea-gen-0515-5
8	- **Level**: solid
9	- **Target Venues**: ICLR 2027 (deadline expected ~October 2026 based on historical pattern — not yet announced; ideal timeline for thorough experiments including pilot feasibility study and RL-contamination condition; PRIMARY TARGET), AAAI 2027 (abstract July 21, paper July 28, 2026 — tight but feasible if pilot study is scoped to single domain; 2 months), EACL 2027 via ARR August 2026 cycle (submission August 3, 2026 — feasible with focused experiments on LiveBench math subset)
10	
11	## Seed Topic
12	
13	web_research
14	
15	## Core Problem
16	
17	How can we build self-healing benchmarks that automatically detect contaminated items via multi-signal triangulation — including a novel DIF-based cohort analysis robust to RL-trained reasoning models — and regenerate psychometrically equivalent replacements through empirically calibrated generation with bifactor IRT equating, while maintaining benchmark validity through formal graceful-degradation guarantees?
18	
19	## Opportunity / Why Now
20	
21	Dynamic benchmarks face a fundamental tension: increased contamination resistance via strong rewriting degrades question fidelity and may alter intended difficulty. LiveBench updates monthly but without psychometric calibration; VarBench perturbs inputs but difficulty shifts unpredictably; BenchBench evaluates generation quality but without equating. Educational testing has solved the analogous problem of maintaining test comparability across administrations using IRT equating with anchor items — a mature methodology with decades of validation. However, directly applying this to LLM benchmarks requires solving four underappreciated sub-problems: (1) distinguishing contamination from genuine capability gains — this is especially critical for RL-trained reasoning models (o1, o3, DeepSeek-R1), where Wang et al. (ICLR 2026) demonstrate that GRPO/PPO training conceals contamination signals that reference-free detection methods rely on, with AUROC degradation of 14-20 percentage points (Loss: 14.22pp, Min-K%: 16.42pp, Max-K%: 19.84pp after only ~156 GRPO steps), reducing most to near-random (~50%) AUROC; furthermore, Wang & Heckel (arXiv 2603.12875) show that test-time RL alignment can close fine-tuning performance gaps by ~27 percentage points on average, suggesting some apparent contamination signals may reflect task familiarity artifacts rather than memorization, making item-specific detection even more critical; (2) detecting variant contamination (paraphrased/restructured benchmark items in training data) which evades standard detectors — DVD (arXiv 2601.04895) shows conventional methods achieve only 0.43-0.68 AUC on variant contamination; (3) generating replacement items with controlled psychometric properties (LLMs systematically underestimate difficulty with correlations of only rho=0.10-0.45, per arXiv 2602.06631, necessitating empirical calibration rather than prompt-based difficulty targeting); and (4) equating across multi-construct benchmarks (requiring bifactor or multidimensional IRT rather than naive unidimensional models). No existing work addresses all four sub-problems in an integrated pipeline with formal graceful-degradation guarantees.
22	
23	## Landscape (SOTA & Limitations)
24	
25	LiveBench (ICLR 2025) updates monthly from recent sources but applies objective scoring without difficulty calibration. LiveCodeBench (ICLR 2025) uses time-segmented evaluation but doesn't ensure psychometric equivalence across segments. BeTaL (ICLR 2026) performs dynamic benchmark design with LLM-in-the-loop but focuses on increasing difficulty, not preserving it. BenchBench (March 2026) evaluates automated benchmark generation using discrimination and validity metrics but without IRT equating. ArenaBencher progressively generates harder items but provides no formal difficulty-equivalence guarantees. CRITICAL CONCURRENT WORK: 'Growing Pains' (arXiv April 2026) uses multidimensional IRT with fixed-parameter calibration and 100 anchor items per dataset to make LLM evaluation extensible across time — achieving Spearman rho >= 0.9 for ranking preservation using 400+ models. However, it addresses efficient evaluation (comparing scores across time), NOT contamination detection or item regeneration. PSN-IRT (AAAI 2026 Oral) analyzes benchmark quality via 4PL IRT but does not regenerate items. RIDE (ICLR 2026) uses IRT-guided perturbation for difficulty evolution in math but does not perform equating. ATLAS (arXiv 2025) applies adaptive testing with IRT to reduce evaluation cost but does not handle contamination. Cross-Context Verification (CCV; arXiv 2603.21454, March 2026) achieves perfect separation between contaminated and genuine reasoning (Mann-Whitney U=0, r=1.0) on SWE-bench Verified by measuring solution diversity across independent sessions — a powerful black-box method, but currently validated only on coding tasks (9 SWE-bench problems, 45 trials) and relying on temperature-0 determinism that may not generalize to knowledge/reasoning benchmarks with inherent answer variability. Hardy et al. (arXiv 2603.24999, March 2026) introduce nonparametric signed isotonic R² scalability coefficients that outperform IRT-based item diagnostics for detecting bad benchmark items on HS Math, GSM8K, and MMLU — lightweight (bivariate monotone fits in seconds) and robust under small-n/large-p conditions; this complements our IRT-based quality control by providing a fast model-agnostic pre-filter for item quality before parametric calibration. On proactive contamination prevention: Sander et al. (arXiv 2502.17259, Feb 2025) propose watermarking benchmarks before release, reformulating questions with a watermarked LLM and detecting 'radioactivity' traces via statistical tests; validated on ARC and MMLU with 1B models, this represents a fundamentally different paradigm (prevention at release time vs. post-hoc detection and remediation). Our approach is complementary: watermarking prevents future contamination, while our pipeline detects and remediates existing contamination in already-deployed benchmarks — the two could be combined in a defense-in-depth strategy. On contamination detection: ConStat (2024) provides performance-based detection with formal FDR control; shortcut neuron analysis (ACL 2025) can isolate contamination to ~1.1-1.4% of neurons with only ~3% false positive impact; 'Test of Time' (arXiv 2025) demonstrates temporal signals are unreliable as standalone contamination indicators. CRITICALLY, 'On The Fragility of Benchmark Contamination Detection in Reasoning Models' (Wang et al., arXiv 2510.02386, ICLR 2026) systematically demonstrates that GRPO/PPO-style RL training conceals contamination signals: reference-free methods show AUROC degradation of 14-20 percentage points after only ~156 GRPO steps (Loss: 14.22pp drop from 75.48% to 61.26%; Min-K%: 16.42pp drop from 74.96% to 58.54%; Max-K%: 19.84pp drop from 69.83% to 49.99% — essentially random), while perturbation-based methods show different degradation patterns. The concealment mechanism is PPO's clipping objective, which contracts the NLL gap between contaminated and clean items. Self-Critique (Tao et al., arXiv 2510.09259, ICLR 2026) partially addresses this via policy-collapse detection but remains an individual-model-level method. DVD (Liang et al., arXiv 2601.04895, Jan 2026) introduces detection via variance of generation distribution and is specifically designed for variant contamination, achieving 0.73-0.74 AUC where Min-K%++ achieves only 0.43-0.68; however, DVD was validated only on SFT-contaminated models and its behavior under RL training is untested. On task familiarity vs. contamination: Wang & Heckel (arXiv 2603.12875, March 2026) show that test-time RL alignment (TTRA) closes the performance gap between base and fine-tuned models by ~27 percentage points on average, suggesting many reported fine-tuning gains are task familiarity artifacts rather than genuine capability improvements; this has a dual implication — it strengthens the need for item-specific contamination detection (since task familiarity produces uniform improvements with no DIF signal, while contamination produces item-specific advantages that DIF detects), but also suggests that contamination-driven DIF effects may be partially confounded with format-familiarity effects that TTRA could remove. On item generation: arXiv 2602.06631 shows LLMs achieve only rho=0.10-0.45 for difficulty estimation, but student simulation approaches (arXiv 2601.09953) achieve r=0.75-0.82 and multi-agent frameworks like ReQUESTA improve discrimination from 0.17 to 0.39. On IRT methodology: bifactor models with Projective IRT (PIRT) enable equating of multidimensional tests while remaining tractable; fixed-parameter calibration requires only N>=200 examinees vs N>=500 for full calibration (Kim & Kolen, 2019); the OH2PL (König, Spoden, & Frey, 2020) achieves unbiased estimates at N>=50 using optimized Bayesian hierarchical priors. No existing work closes the full loop from multi-signal contamination detection (robust to RL-trained models) through construct-constrained generation to bifactor IRT-equated regeneration with graceful-degradation guarantees.
26	
27	## Proposed Approach
28	
29	Build a closed-loop pipeline with three stages plus a formal graceful-degradation framework, each substantially revised to address known limitations:
30	
31	**Stage 1: Multi-Signal Contamination Sentinel (with RL-Robustness Guarantees).** Deploy an ensemble of five complementary detection signals, explicitly designed so that at least two signals remain informative even against RL-trained reasoning models:
32	
33	(a) *ConStat-style perturbation testing* — compare model performance on original items vs. semantically-equivalent reformulations, with formal False Discovery Rate (FDR) control. NOTE: Wang et al. (ICLR 2026) show reference-free detectors degrade 14-20pp under RL training (Loss: 14.22pp, Min-K%: 16.42pp, Max-K%: 19.84pp after ~156 GRPO steps); we retain perturbation testing as effective against non-RL models (which still constitute the majority of the model ecosystem) but do not rely on it alone.
34	
35	(b) *Differential Item Functioning (DIF) across model release cohorts* — a novel application treating model release date as a grouping variable and flagging items that become differentially easier for newer cohorts beyond what general ability gains predict. **This is our primary RL-robust signal.** The key argument: DIF operates on group-level statistical patterns (comparing Item Characteristic Curves across model cohorts matched on overall ability), not individual output distributions. Wang et al. prove that PPO/GRPO clipping contracts the NLL gap *within a single model* between seen and unseen items — but DIF does not examine within-model NLL gaps. It detects whether the structural relationship between ability and item response differs across groups. A contaminated cohort shows anomalous ICCs on specific items regardless of how smooth individual output distributions appear, because contamination must, by definition, create differential item advantage — the one signal RL cannot conceal without negating the purpose of contamination. Furthermore, DIF leverages IRT's invariance principle: item parameters should be group-invariant after controlling for ability, and systematic DIF violations on specific items constitute contamination evidence that is orthogonal to all 10 methods shown to fail.
36	
37	**Analytical Demonstration of DIF RL-Robustness.** Consider a concrete scenario: 200 binary items evaluated by two annual model cohorts (pre-2026, post-2026) with N=80 models each. Suppose 20 items are contaminated in the newer cohort, boosting P(correct) from 0.50 to 0.80 on those items (δ≈1.4 logits — a conservative estimate given GSM1K's documented 13% average accuracy drop across models, which implies item-level boosts of 20-40% on memorized items for heavily contaminated models). RL smoothing via GRPO/PPO contracts the NLL gap between contaminated and clean items within each individual model's output distribution — this is the mechanism Wang et al. demonstrate. However, the 30-percentage-point accuracy advantage on contaminated items persists at the behavioral level: RL training does not cause models to answer memorized items incorrectly, because doing so would negate the purpose of contamination. Logistic regression DIF with sum-score matching compares the probability of correctly answering each item across the two cohorts, conditioning on total score (overall ability). On the 180 uncontaminated items, both cohorts show similar ICCs after controlling for ability. On the 20 contaminated items, the newer cohort shows systematically higher probability of correct response at every matched ability level — large uniform DIF (ETS Category C: |Δ_MH| = -2.35 × ln(odds ratio) = -2.35 × ln(4.0) ≈ 3.3 delta units, far exceeding the C threshold of 1.5). This differential pattern is detectable because DIF examines between-group item-level performance conditional on ability, not within-model output distributions. RL smoothing is irrelevant to DIF: it modifies how confidently a model generates its answer (the NLL surface), not whether it gets the answer right or wrong (the binary response pattern that DIF analyzes).
38	
39	**Quantitative DIF Power Analysis.** Independent simulation evidence (PMC5978487) establishes that logistic regression DIF at N=50/group achieves 14.4% power for small effects (δ=0.4) and 31.0% for medium effects (δ=0.6); at N=100/group, these rise to 24.7% and 55.2% respectively. These figures appear concerning for small-sample detection, but benchmark contamination typically produces large effects: GSM1K documents 10-13% average accuracy drops from contamination across models, corresponding to item-level δ≈0.8-1.4 logits on memorized items. DIF power scales super-linearly with effect size; at δ=1.4 with N=80/group (annual cohorts), power is estimated at 60-85% based on extrapolation from PMC5978487 simulation curves, consistent with the general finding that the likelihood ratio test achieves the highest statistical power in most DIF configurations. Furthermore, three factors substantially improve effective power beyond these baseline estimates: (i) cumulative Bayesian priors (Sinharay et al., 2006) accumulate evidence across successive benchmark administrations, borrowing strength from previous DIF estimates to improve detection over time — particularly effective for persistent contamination that affects multiple administrations; (ii) Item-Focused Trees (Tutz & Berger, 2016) avoid arbitrary categorical group splits by treating release date as a continuous covariate, leveraging the full model sample (N=160 rather than two groups of 80) and letting the method identify natural breakpoints where DIF emerges; (iii) the 2-of-5 ensemble voting threshold means even 40-50% individual DIF power yields acceptable ensemble sensitivity when combined with DVD and ConStat signals on non-RL models. We acknowledge that DIF alone is underpowered for small contamination effects (δ<0.6); its value lies in detecting the large effects that matter most for benchmark validity, complemented by other ensemble signals for smaller effects.
40	
41	**Interaction with Task Familiarity Artifacts.** Wang & Heckel (arXiv 2603.12875, March 2026) demonstrate that test-time RL alignment (TTRA) closes the performance gap between base and fine-tuned models by ~27 percentage points on average, suggesting many reported fine-tuning gains reflect task familiarity rather than genuine capability. This has a dual implication for DIF-based detection. First, it *strengthens* the DIF rationale: task familiarity artifacts produce uniform improvements across all items (no DIF signal), while memorization-based contamination produces item-specific advantages (DIF signal) — DIF thus provides a principled way to distinguish the two, a distinction no other detection method explicitly makes. Second, it introduces a nuance: if some contamination manifests partially as enhanced task-format familiarity rather than item-specific memorization, the item-level DIF effect sizes may be modestly smaller than the raw accuracy gaps suggest. We address this by: (a) noting that DIF would be computed on models as deployed (without TTRA), since TTRA is an analysis tool, not a standard deployment procedure; (b) observing that DIF controls for overall ability via sum-score matching, so any uniform familiarity-driven improvements are absorbed into the ability estimate, leaving item-specific contamination signals intact; (c) reporting DIF effect sizes with uncertainty intervals rather than relying on significance thresholds alone, making the analysis transparent about power limitations.
42	
43	**DIF Small-Sample Strategy (detailed).** Classical DIF methods (Mantel-Haenszel, logistic regression) require N≥200 per group for optimal performance (Mazor et al., 1992; Scott et al., 2009), far exceeding our ~10-20 models per quarterly cohort. We address this through a four-pronged strategy: (i) *Temporal aggregation*: use semi-annual or annual cohorts rather than quarterly, yielding N=40-80 per group; as the model ecosystem grows (~100+ new models per year as of 2026), annual cohorts will approach the N≥100 threshold where regularized methods become viable. (ii) *Cumulative Bayesian DIF*: following Sinharay et al. (2006, ETS), use DIF estimates from previous benchmark administrations as informative priors for new cohorts, accumulating statistical power over time rather than analyzing each cohort in isolation. (iii) *Item-Focused Trees* (Tutz & Berger, 2016): treat release date as a continuous covariate rather than creating arbitrary categorical cohorts, letting the method identify natural breakpoints where DIF emerges — this avoids the small-group problem entirely while leveraging the full model sample. (iv) *Parsimonious models*: following Belzak (2020, Multivariate Behavioral Research), use logistic regression with sum scores rather than complex IRT models for DIF detection, as simpler models outperform complex ones in small samples even when misspecified. We report DIF effect sizes (ETS delta classification: A/B/C, where C indicates |Δ_MH|≥1.5) with uncertainty intervals rather than relying solely on significance tests, acknowledging power limitations transparently.
44	
45	(c) *IRT aberrance detection* — flag items whose observed easiness significantly exceeds calibrated difficulty, used as one signal among several rather than a standalone detector.
46	
47	(d) *DVD-style generation variance testing* (adapted from Liang et al., arXiv 2601.04895) — for models with inference access, generate 50 responses per item via temperature sampling and compute the variance of synthetic-difficulty scores. Contaminated items exhibit bimodal generation distributions (alternating between memorized templates and free generation) yielding high variance, while clean items show unimodal low-variance distributions. This specifically detects variant contamination (paraphrased/restructured benchmark items) where ConStat and Min-K% fail (AUC 0.43-0.68 vs. DVD's 0.73-0.74). NOTE: DVD is promising but untested against RL-trained models — it was validated only
48	
49	## Resource Estimate
50	
51	- **auto_research**: {'claude_api_cost': '$800-$1200 (Opus 4.7 for experimental design and IRT analysis, Sonnet 4.6 for implementation, ~180M tokens with caching)', 'closed_source_api_cost': '$800-$2000', 'estimated_gpu_cost': '$1800-$2400', 'gpu_hours': '900-1200 (cannot reduce inference needs for 200-300 model calibration panel; DVD temperature-sampling adds ~10% overhead)', 'speed_bottleneck': 'IRT calibration panel: collecting responses from 200-300 diverse LLMs on pilot items requires sequential API calls to closed-source models (rate limits) and batched inference on open-weight models (GPU scheduling). Minimum ~3 weeks for a single calibration round with full parallelism across ~150 open-weight models and ~50 closed-source APIs. The pilot feasibility study requires at least 2 full calibration rounds. DVD temperature-sampling (50 generations/item) adds ~10% to inference costs.', 'timeline': '8-12 weeks (parallelized model evaluation is the critical path; 200-300 model panel requires ~3 weeks per calibration round even with full parallelism; pilot feasibility study adds ~2 weeks; RL-contamination condition adds ~1 week for GRPO training)'}
52	- **human_in_loop**: {'claude_api_cost': '$400-$700 (Sonnet 4.6 for code generation and pipeline orchestration, ~120M tokens total with caching)', 'closed_source_api_cost': '$800-$2000', 'estimated_gpu_cost': '$1600-$2200', 'gpu_hours': '800-1100 (same inference needs, Claude handles generation orchestration, IRT analysis code, DIF implementation, and DVD adaptation)', 'timeline': '3.5-4.5 months (Claude drafts contamination detection, equating code, DIF pipeline, and student simulation; human validates IRT assumptions, bifactor model specification, DIF power analysis, and experimental design)'}
53	- **manual**: {'closed_source_api_cost': '$800-$2000 (API calls for ~30-50 closed-source models in calibration panel: GPT-4o, Claude, Gemini, etc. at ~5K items each, plus student simulation inference, plus DVD temperature-sampling for closed-source models)', 'estimated_gpu_cost': '$1800-$2600 at ~$2/hr H100 spot pricing', 'gpu_hours': '900-1300 (inference of 200-300 models on ~5K items each for IRT calibration across multiple rounds, plus item generation with 70B+ models, plus student simulation panel, plus DVD temperature-sampling at 50 generations/item)', 'timeline': '5-6 months (1.5 months multi-signal contamination detector including DIF infrastructure and DVD adaptation, 1.5 months bifactor IRT calibration infrastructure, 1.5 months generation pipeline with student simulation, 1.5 months experiments including RL-contamination condition, pilot feasibility study, and writing)'}
54	
55	## Key References
56	
57	- LiveBench: A Challenging, Contamination-Free LLM Benchmark (ICLR 2025)
58	- LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code (ICLR 2025)
59	- Automating Benchmark Design [BeTaL] (ICLR 2026)
60	- BenchBench: Benchmarking Automated Benchmark Generation (arXiv 2026)
61	- Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration (arXiv April 2026)
62	- Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory [PSN-IRT] (AAAI 2026 Oral)
63	- The stability of IRT parameters under several test equating conditions (Frontiers in Psychology 2026)
64	- Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil's ENEM Corpus (arXiv 2602.06631, Feb 2026)
65	- Take Out Your Calculators: Estimating Real Difficulty with LLM Student Simulations (arXiv 2601.09953, Jan 2026)
66	- Reconstructing Item Characteristic Curves with Fine-Tuned LLMs (arXiv 2601.02580, Jan 2026)
67	- ReQUESTA: Hybrid Multi-Agent Framework for MCQ Generation (arXiv 2602.03704, Feb 2026)
68	- Test of Time: Rethinking Temporal Signal of Benchmark Contamination (arXiv 2509.00072, 2025)
69	- ConStat: Performance-Based Contamination Detection with FDR Control (ETH Zurich 2024)
70	- Establishing Trustworthy LLM Evaluation via Shortcut Neuron Analysis (ACL 2025)
71	- On The Fragility of Benchmark Contamination Detection in Reasoning Models (Wang et al., arXiv 2510.02386, ICLR 2026)
72	- Detecting Data Contamination from Reinforcement Learning Post-training [Self-Critique / RL-MIA] (Tao et al., arXiv 2510.09259, ICLR 2026)
73	- DVD: Detection via Variance of Generation Distribution for Variant Contamination (Liang et al., arXiv 2601.04895, Jan 2026)
74	- Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis [CCV] (arXiv 2603.21454, March 2026)
75	- Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients (Hardy et al., arXiv 2603.24999, March 2026)
76	- Detecting Benchmark Contamination Through Watermarking (Sander et al., arXiv 2502.17259, Feb 2025)
77	- Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks (Wang & Heckel, arXiv 2603.12875, March 2026)
78	- Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data (Kim & Kolen, Applied Measurement in Education 2019)
79	- An Optimized Bayesian Hierarchical Two-Parameter Logistic Model for Small-Sample Item Calibration [OH2PL] (König, Spoden, & Frey, Applied Psychological Measurement 2020, PMC7262992)
80	- Robustness of the OH2PL for Small-Sample Item Calibration (König, Spoden, & Frey, Behavior Research Methods 2022)
81	- Approximating Bifactor IRT Equating with Projective IRT [PIRT] (PMC 2020)
82	- Item Response Theory True Score Equating for the Bifactor Model (Kim, Journal of Educational Measurement 2022)
83	- Several Variations of Simple-Structure MIRT Equating (Kim, Journal of Educational Measurement 2023)
84	- MMLU-CF: A Contamination-Free Multi-task Language Understanding Benchmark (ACL 2025)
85	- Simulating Training Data Leakage in Multiple-Choice Benchmarks (arXiv 2505.24263, 2025)
86	- VarBench: Robust Language Model Benchmarking Through Dynamic Variable Perturbation (EMNLP 2024)
87	- DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks (ICLR 2024)
88	- RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning (arXiv 2025)
89	- Adaptive Testing for LLM Evaluation [ATLAS] (arXiv 2025)
90	- Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation (EMNLP 2025)
91	- Automatic- and Transformer-Based AIG: A Critical Review (Sommer & Arendasy, Intelligence 2025)
92	- Can LLMs Estimate Student Struggles? The Curse of Knowledge Effect (arXiv 2512.18880, 2025)
93	- Quantifying Data Contamination in Psychometric Evaluations of LLMs (Han et al., arXiv 2510.07175, 2025)
94	- Using Past Data to Enhance Small-Sample DIF Estimation: A Bayesian Approach (Sinharay et al., ETS Research Report RR-06-09, 2006)
95	- Testing Differential Item Functioning in Small Samples (Belzak, Multivariate Behavioral Research 2020)
96	- Item-Focused Trees for the Detection of Differential Item Functioning (Tutz & Berger, Psychometrika 2016)
97	- Test Equating, Scaling, and Linking: Methods and Practices 3rd ed. (Kolen & Brennan, Springer 2014)
98	- A Careful Examination of Large Language Model Performance on Grade School Arithmetic [GSM1K] (arXiv 2405.00332, 2024)
99	- Power and Sample Size Calculations for Logistic Regression Tests for Differential Item Functioning (PMC5978487)
100	
101	## Reviewer Evaluation
102	
103	**Scores**:
104	  - entry_triage_x: **26.0**/5
105	  - exit_triage_z: **36.0**/5
106	
107	## Human Review Note
108	
109	## External Review — Verdict: PASS
110	
111	- X (entry triage): 26.0%
112	- Y (terminal self-eval): 42.0%
113	- Z (exit triage): 36.0%
114	- Z interval: [30.0%, 42.0%]
115	- Real improvement (Z-X): +10.0 pp
116	
117	### Optimization Suggestions
118	All three background agents have completed and confirmed the deliverable. The 角色 C final output (【优化方案】 with 26 modifications, 【主要风险】, and 【实施评估】) was already delivered above and matches the verified transcript content exactly. 
119	
120	The review process is complete. No further action needed.
121	
122	_Reviewed by external pipeline (batch7), 2026-05-20_
123	
124	
125	## MVP Validation Results
126	
127	- **Date**: 2026-05-20
128	- **Hypothesis Supported**: Yes
129	
130	### Key Metrics
131	
132	Phase 1 ETS C: N=80,δ=1.4 TPR=0.7254 FPR=0.040 | N=100,δ=1.4 TPR=0.7938 FPR=0.043 | N=100,δ=1.6 TPR=0.8508 FPR=0.047 || Phase 2 ETS C (real MMLU params): N=80,δ=1.4 TPR=0.6823 FPR=0.036 | N=100,δ=1.4 TPR=0.7582 FPR=0.040 | N=100,δ=1.6 TPR=0.7966 FPR=0.042 || BH-corrected best: N=100,δ=1.6 TPR=0.686 (GRAY) || 操作点: N≥100推荐, N=80边界; δ≥1.4有效, δ<1.0需ensemble
133	
134	### Summary
135	
136	验证 DIF (Differential Item Functioning) 跨模型批次分析能否以足够统计功效检测 benchmark 污染。两阶段验证：Phase 1 合成 2PL 参数 Monte Carlo 模拟（28 conditions × 1000 reps），Phase 2 真实 MMLU IRT 参数半合成验证（15 conditions × 1000 reps）。BH 校正路径失败（200 items 多重检验过于保守，TPR 压缩 40-60%），但 ETS C 分类（效应量+显著性双阈值，教育测量 gold standard）在 N≥80, δ≥1.4 时达标。Phase 2 用真实参数后 TPR 降低 3-6pp，仍满足阈值。
137	
138	### Recommendation
139	
140	GO — 核心假设成立（DIF+ETS C 在大效应量下功效达标），操作点与 GSM1K 文档的重度污染吻合。限制条件（δ<1.0 需 ensemble、N≥80 最低要求）明确且可在论文中诚实披露。建议进入 research 阶段，优先写 paper_framing.md 和 experiment_plan.yaml，然后规划真实数据实验。
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b3da728-d41c-40cc-99f2-b78348374784",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "aa9ac48b1a21999a9",
  "type": "user",
  "uuid": "451f9715-0295-443f-8885-11c0d0abfe48",
  "sourceToolAssistantUUID": "1b3da728-d41c-40cc-99f2-b78348374784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-20T20:14:36.508Z_

Now I have comprehensive understanding of the full project. Let me produce the review.

---

## Review: Self-Healing Benchmarks (R1 -- Methods and Experiments)

### Summary

This paper proposes a three-component "self-healing benchmark" framework: (1) DIF-based contamination detection claimed to be robust to RL training, (2) a multi-signal ensemble combining DIF, ConStat, and DVD, and (3) bifactor IRT equating for benchmark regeneration. The core claim is that DIF operates on group-level behavioral patterns immune to the within-model distribution smoothing that RL training performs. On METABENCH MMLU (5,055 models x 12,508 items), the paper reports 78% TPR at FPR < 5%, 87% ensemble TPR, and 0.97 Spearman rank correlation after equated regeneration. The paper is ambitious in scope, connecting psychometric theory to a pressing practical problem, but I have significant concerns about the experimental evidence -- particularly whether the RL-robustness claim is adequately supported.

### Strengths

- **Novel and well-motivated framing.** Recasting contamination as DIF is a genuinely insightful connection between educational measurement and LLM evaluation. The argument that DIF operates on group-level ICCs rather than within-model output distributions is theoretically compelling and clearly articulated.

- **Thorough experimental breadth.** The paper covers detection, ensemble fusion, cross-benchmark validation, bifactor equating, item generation calibration, Bayesian accumulation, graceful degradation, and Item-Focused Trees -- a comprehensive pipeline that few papers attempt. Each component is evaluated with sensible metrics.

- **Sound psychometric foundations.** The ETS C classification system, bifactor model specification with 57 subject factors, anchor item selection criteria (25% rate, consistent with Kolen & Brennan recommendations), and fixed-parameter calibration methodology all follow established psychometric practice. The decision to use effect-size thresholds rather than p-values for DIF classification is well-justified given the multiple-testing landscape (D001 in the project records confirms BH correction failed catastrophically).

- **Cross-benchmark validation.** GSM8K + GSM1K provides a genuinely independent ground truth source, and the 4.7x gap between DIF-flagged and clean models (Table 10) is compelling convergent evidence.

- **Honest reporting of limitations.** The paper acknowledges DIF's limited power at delta < 1.0, the ensemble's elevated FPR (0.08), and the limitation to MCQ benchmarks. The graceful degradation analysis provides operational guardrails (20% replacement ceiling).

- **Student simulation vs. prompt targeting comparison** (Table 13) is a valuable contribution in its own right, demonstrating that empirical calibration via behavioral responses substantially outperforms introspective difficulty estimation (rho = 0.78 vs. 0.28).

### Weaknesses

**Major:**

- **[M1] RL-robustness evaluation is critically underpowered.** The headline claim is RL-robustness, but the empirical evidence rests on only 14 RL-trained models (Table 3-4), with subgroup analyses on 6 and 8 models respectively. DIF is fundamentally a group-level method requiring adequate per-group sample sizes -- the paper's own simulations establish N >= 80 as the minimum. Computing TPR on 14 models and reporting 3 decimal places of precision is misleading. The paired t-test (p = 0.62) comparing DIF TPR on SFT vs. RL cohorts has essentially no statistical power with these sample sizes. The retention ratio of 0.96 could easily be noise. The paper needs either: (a) substantially more RL-trained models, or (b) much more cautious claims about RL robustness qualified as "preliminary" or "suggestive." As stated, this is the paper's central selling point resting on the paper's weakest evidence.

- **[M2] Ground truth circularity and definition of TPR/FPR.** The paper reports TPR and FPR throughout but never clearly defines the ground truth against which these are computed on real data. For simulations, ground truth is known (injected contamination). For real METABENCH data (Table 1), what constitutes a "truly contaminated" item? If TPR is computed against MMLU-CF modifications as ground truth, this is stated only indirectly (phi = 0.42, Table 2) and the correlation is only moderate. If TPR is computed against injected synthetic contamination on top of real data, this is not stated. The paper conflates simulation-derived TPR numbers with real-data analysis without making the evaluation protocol transparent. This is a fundamental methodological gap -- the reader cannot verify the headline 78% TPR claim.

- **[M3] Confound between contamination and genuine capability improvement.** DIF detects items where focal group (post-2024) performs differentially better after controlling for overall ability. But genuine capability improvements in specific domains (e.g., math reasoning improvements from better training data, not memorization) would produce the same DIF signal. The paper's temporal cohort split (pre-2024 vs. post-2024) spans a period of rapid capability improvement concentrated in STEM -- exactly the domains where DIF flags concentrate (10.7% flagged, STEM-heavy). The paper needs to disentangle contamination-DIF from capability-improvement-DIF. The MMLU-CF validation (phi = 0.42) partially addresses this but the moderate correlation also leaves room for substantial false attribution.

- **[M4] Ensemble weight optimization is likely overfit.** The weighted fusion weights (0.45/0.30/0.25) are described as "optimized on a calibration set" but no details are provided about calibration/test split, cross-validation procedure, or regularization. With only three weights to optimize and a presumably small calibration set of items with known contamination status, the risk of overfitting is high. The 15pp advantage of weighted fusion over majority voting (Table 7) may not generalize. At minimum, the paper should report cross-validated ensemble performance.

- **[M5] Bifactor model fitting on 5,055 models with 57 subject factors is computationally heroic but psychometrically questionable in this context.** The paper reports RMSEA = 0.028, CFI = 0.96, TLI = 0.95 -- suspiciously good for a model with 57 specific factors and 12,508 items. In classical IRT, these fit indices are computed on human examinee data where local independence conditional on latent factors is a reasonable assumption. For LLMs, models within the same family (e.g., Llama-2 variants, Mistral fine-tunes) violate local independence because they share training data and architecture. The paper should discuss whether/how model non-independence affects bifactor model fit and equating validity.

**Minor:**

- **[m1] Multiple comparisons in Table 3.** Ten p-values are reported for traditional detectors degrading under RL, without correction for multiple comparisons. While the individual significance levels are low enough that this is unlikely to change conclusions, it should be noted.

- **[m2] ConStat evaluation on only 240 items.** Given MMLU has 12,508 items, evaluating ConStat on 240 items (< 2%) raises questions about representativeness. The 5 reformulations per item are also modest for FDR-controlled testing.

- **[m3] DVD evaluation temperature range (0.7-1.0) is narrow.** Lower temperatures (0.3-0.5) might better distinguish memorized from reasoned responses. No sensitivity analysis on temperature is reported.

- **[m4] The Item-Focused Trees section (4.11) adds incremental value (+3pp TPR) at 12x computational cost.** The changepoint analysis is interesting but could be shortened to make room for more rigorous RL evaluation.

- **[m5] Bayesian DIF simulation (Table 15) uses N = 40 per administration.** This is below the paper's own stated minimum of N >= 80. The power doubling claim (0.38 -> 0.78) is for this underpowered regime, making the practical utility uncertain.

- **[m6] No confidence intervals or error bars are reported for any table.** Given that many results are from simulation (which can provide bootstrap CIs) or from analyses with known sampling distributions, this is a significant omission for reproducibility and interpretation.

- **[m7] The paper does not cite or compare against Tao et al. (ICLR 2026) on Self-Critique/RL-MIA**, which is a direct competitor for RL-robust contamination detection. This omission weakens the related work and baseline comparisons.

### Questions for Authors

1. **Ground truth definition for real-data TPR (Table 1):** What exactly is the ground truth for computing TPR = 0.78 on METABENCH MMLU? Is contamination injected synthetically, or are MMLU-CF labels used as ground truth? If the former, why are real-data TPR numbers so close to simulation predictions? If the latter, phi = 0.42 suggests substantial disagreement.

2. **RL model selection:** How were the 14 RL models selected (Table 3)? If they were selected based on identifiable RL training, this introduces selection bias -- models that explicitly disclose RL training may differ systematically from those that don't.

3. **DIF vs. capability improvement:** Have you analyzed whether DIF flags correlate with known model family improvements? For example, do Llama-2 -> Llama-3 transitions produce DIF flags on items where Llama-3 has known capability improvements unrelated to contamination?

4. **Ensemble calibration:** What fraction of items had known contamination status for ensemble weight optimization? Was cross-validation performed? What happens with uniform weights (1/3, 1/3, 1/3)?

5. **Bifactor model convergence:** What estimation method was used for the bifactor model? Did all 57 subject factors have adequate items (some MMLU subjects have < 100 items)? Were Heywood cases encountered?

6. **Equating evaluation independence:** The equating results (Table 12, rho = 0.97) -- are these computed on the same models used for IRT parameter estimation, or on a held-out set? If the former, the high correlation may be circular.

### Detailed Comments on Specific Sections/Tables

**Table 1 (DIF on METABENCH):** The FPR is suspiciously constant across all cohort splits (0.036-0.042). This is consistent with it being determined primarily by the ETS C threshold rather than by data characteristics, which would support the claim -- but it also means FPR is essentially a fixed design parameter, not an empirical finding.

**Table 3 (DIF vs. Traditional Detectors):** The comparison is not fully apples-to-apples. DIF is a group-level method applied across model cohorts; Min-K%, Perplexity, etc. are individual-model methods. The AUROC computation must involve different protocols for these two categories. The paper does not clarify how group-level DIF AUROC (which outputs one flag per item) is made comparable to model-level detector AUROC (which outputs one score per model-item pair).

**Table 7 (Ensemble):** DIF's "full-spectrum TPR" of 0.58 in the ensemble table is much lower than its 0.78 at delta >= 1.4 in Table 1. This confirms that DIF contributes little at small effect sizes, raising the question of whether the ensemble's 0.87 TPR is driven mainly by ConStat and DVD for medium/small effects -- which are precisely the signals that degrade under RL. The ensemble's RL-robustness is not directly evaluated in a dedicated table.

**Table 12 (Equating Results):** Chi-square test p = 0.34 failing to reject equivalence is a null result -- absence of evidence is not evidence of absence. With the sample sizes involved (5,055 models), the test should have high power. If instead the test has low power, reporting it is misleading. An equivalence test (TOST) would be more appropriate.

**Section 3.1 (DIF formulation):** The formulation correctly presents 2PL IRT and MH-based DIF. However, the paper uses MH (which stratifies on sum scores) while fitting a 2PL model -- the paper should clarify whether DIF analysis uses the MH statistic directly on raw scores (standard practice) or IRT-based likelihood ratio tests (which would be more powerful but require model assumptions).

**Section 4.7 (Bifactor):** Fitting a bifactor model with 57 specific factors to 5,055 "examinees" and 12,508 items is at the frontier of psychometric feasibility. The paper should report convergence diagnostics, estimation time, and whether simplified estimation (e.g., PIRT projection) was used.

### Preliminary Score

**Score: 4 (Weak Accept)**

**Confidence: 3 (Moderate)**

**Rationale:** The paper addresses a genuinely important problem with a novel and well-motivated approach. The psychometric framing is sound and the experimental breadth is impressive. However, the central RL-robustness claim -- which is the paper's primary differentiator -- rests on inadequate empirical evidence (14 RL models). The ground truth for real-data evaluation is unclear. The potential confound between contamination-DIF and capability-improvement-DIF is not adequately addressed. These are addressable weaknesses: a larger RL evaluation, explicit ground truth definition, and a confound analysis would substantially strengthen the paper. In its current form, the theoretical contribution is strong enough for a weak accept, but the experimental backing for the headline claim falls short of what a top venue requires. If the RL-robustness evaluation were strengthened during a revision, this could move to a clear accept.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "451f9715-0295-443f-8885-11c0d0abfe48",
  "isSidechain": true,
  "agentId": "aa9ac48b1a21999a9",
  "requestId": "req_011CbERzyVfWsHNa786pVGWc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "013dded1-e1f6-4937-8fb8-6f768407b4d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NEuwoTSJLredgMUtHrbUSU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8404,
      "cache_read_input_tokens": 89538,
      "output_tokens": 3295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8404
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3295,
          "cache_read_input_tokens": 89538,
          "cache_creation_input_tokens": 8404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8404,
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
