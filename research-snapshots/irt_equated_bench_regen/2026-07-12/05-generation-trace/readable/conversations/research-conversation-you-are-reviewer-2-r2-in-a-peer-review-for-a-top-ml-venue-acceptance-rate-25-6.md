# Research conversation: You are Reviewer 2 (R2) in a peer review for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Rej

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-afd9dbd7380df2dbd.jsonl`
- **Structured JSON:** [`ad43ea55203e6756c93b.json`](../../sessions/ad/ad43ea55203e6756c93b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-20T20:12:30.419Z_

You are Reviewer 2 (R2) in a peer review for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus: **Novelty and Related Work**.

## Paper Summary
Title: "Self-Healing Benchmarks: RL-Robust Contamination Detection via Differential Item Functioning and Psychometrically Equated Benchmark Regeneration"

The paper proposes a "self-healing benchmark" framework with three components:
1. **DIF-based contamination detection**: Uses Differential Item Functioning (ETS C, Mantel-Haenszel Δ_MH) from educational testing to detect benchmark contamination. Key claim: RL-robust because DIF operates on group-level behavioral patterns, not within-model output distributions.
2. **Multi-signal ensemble**: Combines DIF + ConStat perturbation + DVD generation variance. Weighted fusion achieves 87% TPR.
3. **Bifactor IRT equating for regeneration**: Fits bifactor model, selects anchor items, generates+calibrates replacement items, equates scores.
Additional: Cumulative Bayesian DIF, Item-Focused Trees, GSM8K cross-validation.

## Related Work Section (§2)
Three subsections:
- **Contamination Detection**: Covers Min-K%, perplexity, compression, DetectGPT, reference-model, ConStat, DVD. Notes shared vulnerability to RL smoothing.
- **Benchmark Evolution**: LiveBench (monthly updates, no psychometric calibration), Growing Pains (arXiv 2026, multidimensional IRT for cross-task comparability). Claims "no existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration."
- **Psychometrics in NLP Evaluation**: IRT for ability estimation, bifactor models, DIF in educational testing. Claims novel application of DIF to LLM contamination.

## Key Claims of Novelty
1. DIF as RL-robust contamination detector (reframing contamination as psychometric DIF)
2. Theoretical argument for RL-robustness (group-level ICC vs within-model distributions)
3. Multi-signal ensemble covering full effect-size spectrum
4. Bifactor IRT equating for benchmark regeneration
5. Student simulation calibration for generated items
6. Cumulative Bayesian DIF for medium effects
7. Item-Focused Trees for continuous temporal modeling
8. Full "self-healing benchmark" pipeline integrating detection → generation → equating

## Key Results
- DIF maintains 96% power retention under RL (Table 3-4) while 10 methods degrade to random
- Ensemble achieves 87% TPR full-spectrum (Table 7)
- Bifactor equating ρ=0.97 (Table 12)
- GSM8K cross-validation confirms generalizability (Table 9)
- Graceful degradation: safe up to 20% replacement (Table 16)

## Your Review Task
Evaluate:

1. **Novelty**: How novel is each component? Is the DIF application to LLM contamination truly new? Is the RL-robustness argument original? Is the ensemble approach novel or incremental? Is bifactor equating for benchmark regeneration new?

2. **Related work completeness**: Are important related works missing? Is the positioning fair? Are claims of novelty over-stated?

3. **Conceptual contribution**: Does this paper change how the community thinks about contamination? Is the "self-healing benchmark" framing compelling?

4. **Incremental vs transformative**: Is this a collection of known techniques applied to a new domain, or does it provide genuine new insight?

5. **Significance and impact**: Would this influence future benchmark design? Is it practically useful?

6. **Presentation and framing**: Is the narrative coherent? Is the paper well-written for the target audience?

Produce a structured review with:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, with severity: major/minor)
- Questions for authors
- Detailed comments on novelty and related work
- Preliminary score (1-6) with confidence (1-5)

Be rigorous but fair. Focus on whether the novelty is sufficient for a top venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "09b18ff5-d8a8-4786-9177-9477d1e058f7",
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

_source line 2 · 2026-05-20T20:12:30.425Z_

```json
{
  "parentUuid": "09b18ff5-d8a8-4786-9177-9477d1e058f7",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
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
  "uuid": "488f96f5-b715-4d99-815c-c9ff0e408200",
  "timestamp": "2026-05-20T20:12:30.425Z",
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

_source line 3 · 2026-05-20T20:12:35.220Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "488f96f5-b715-4d99-815c-c9ff0e408200",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERxBZ7gzDQf35k72zdy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09ca7543-eb76-4bad-8566-ab651cd10bdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6fgYyPJEFoZjBmupp8SNj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6988,
      "cache_read_input_tokens": 8254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6988,
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

_source line 4 · 2026-05-20T20:12:35.758Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019zTp9vym2o4FGDEXvmbnNS`</summary>

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
  "parentUuid": "09ca7543-eb76-4bad-8566-ab651cd10bdf",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERxBZ7gzDQf35k72zdy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb08f89e-d2c9-468a-abd0-5837ec8c454a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6fgYyPJEFoZjBmupp8SNj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6988,
      "cache_read_input_tokens": 8254,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6988
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 8254,
          "cache_creation_input_tokens": 6988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6988,
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

_source line 5 · 2026-05-20T20:12:35.760Z_

<details><summary>↩ Tool result · `toolu_019zTp9vym2o4FGDEXvmbnNS`</summary>

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
  "parentUuid": "bb08f89e-d2c9-468a-abd0-5837ec8c454a",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "6867f3ec-e2a4-4a4d-b4b5-55a01def1d37",
  "sourceToolAssistantUUID": "bb08f89e-d2c9-468a-abd0-5837ec8c454a",
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

_source line 6 · 2026-05-20T20:12:39.129Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01WULWRuBW8RX66WAhnjQMvK`</summary>

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
  "parentUuid": "6867f3ec-e2a4-4a4d-b4b5-55a01def1d37",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERxaXF5SKq4XKNyFNWu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80b8442c-c400-4b14-b48b-9592da421b90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4RnrDeyVXABnCoAQFWPkL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15242,
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

_source line 7 · 2026-05-20T20:12:39.146Z_

<details><summary>↩ Tool result · `toolu_01WULWRuBW8RX66WAhnjQMvK`</summary>

```text
{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (2 个)\n\n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **mvp_dif_power_sim_phase2** (success): ETS C 分类在 METABENCH 真实 MMLU 2PL IRT 参数（非理想化分布）下，仍能在 N≥80/group、δ≥1.4 时达到 TPR≥0.65、FPR≤0.10。Phase 1 用合成参数（a~LogNormal, b~N(0,1)）条件性通过，需验证真实参数分布（可能有偏态、聚集、极端值）不会降解检测功效。 ← 基于 mvp_dif_power_sim\n- **mvp_dif_power_sim** (success): DIF 跨模型批次分析（MH + Logistic Regression）在 N=50-80/group、污染效应量 δ≥1.0 logits 时，对 10% 污染 items 的检测功效 TPR≥0.70 且 FPR≤0.10。这是整个 pipeline 的前提假设——若 DIF 在理想合成数据上都 underpowered，则后续真实数据方案不成立。\n  [Phase 1 DIF Power Results CSV](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_power_results.csv) | [Phase 1 DIF Power Curves](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/chart/dif_power_curves.pdf) | [DIF Diagnostic P-value Distribution](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/chart/dif_diagnostic_pvalue_dist.pdf) | [DIF Diagnostic TPR Comparison (Raw vs BH vs Bonferroni)](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_diagnostic_tpr_comparison.csv)\n\n## 趋势\n成功 2 / 负向 0 / 失败 0 / 共 2\nbest_auc_lr: 0.9405 ↓（近 2 次 success）\nbest_auc_mh: 0.9254 ↓（近 2 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\n（无服务器配置）\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80b8442c-c400-4b14-b48b-9592da421b90",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "34d30547-3a03-4234-b2df-cc5adc5d635b",
  "sourceToolAssistantUUID": "80b8442c-c400-4b14-b48b-9592da421b90",
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

_source line 8 · 2026-05-20T20:12:39.538Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AdbYQHwQEByzepjBqsW1ch`</summary>

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
  "parentUuid": "34d30547-3a03-4234-b2df-cc5adc5d635b",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERxaXF5SKq4XKNyFNWu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bafa6310-f7f4-4f9f-a687-84cd43494e28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4RnrDeyVXABnCoAQFWPkL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15242,
      "output_tokens": 170,
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
          "output_tokens": 170,
          "cache_read_input_tokens": 15242,
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

_source line 9 · 2026-05-20T20:12:39.554Z_

<details><summary>↩ Tool result · `toolu_01AdbYQHwQEByzepjBqsW1ch`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_dif_power_sim_phase2** (success): ETS C 分类在 METABENCH 真实 MMLU 2PL IRT 参数（非理想化分布）下，仍能在 N≥80/group、δ≥1.4 时达到 TPR≥0.65、FPR≤0.10。Phase 1 用合成参数（a~LogNormal, b~N(0,1)）条件性通过，需验证真实参数分布（可能有偏态、聚集、极端值）不会降解检测功效。 ← 基于 mvp_dif_power_sim\\n- **mvp_dif_power_sim** (success): DIF 跨模型批次分析（MH + Logistic Regression）在 N=50-80/group、污染效应量 δ≥1.0 logits 时，对 10% 污染 items 的检测功效 TPR≥0.70 且 FPR≤0.10。这是整个 pipeline 的前提假设——若 DIF 在理想合成数据上都 underpowered，则后续真实数据方案不成立。\\n  [Phase 1 DIF Power Results CSV](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_power_results.csv) | [Phase 1 DIF Power Curves](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/chart/dif_power_curves.pdf) | [DIF Diagnostic P-value Distribution](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/chart/dif_diagnostic_pvalue_dist.pdf) | [DIF Diagnostic TPR Comparison (Raw vs BH vs Bonferroni)](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_diagnostic_tpr_comparison.csv)\\n\\n## 趋势\\n成功 2 / 负向 0 / 失败 0 / 共 2\\nbest_auc_lr: 0.9405 ↓（近 2 次 success）\\nbest_auc_mh: 0.9254 ↓（近 2 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1333, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bafa6310-f7f4-4f9f-a687-84cd43494e28",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "fa7d7d0b-caf4-4bc6-ac7c-1672120b57e0",
  "sourceToolAssistantUUID": "bafa6310-f7f4-4f9f-a687-84cd43494e28",
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

_source line 10 · 2026-05-20T20:12:43.336Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PVwmi25StBsqej1zmpJsza`</summary>

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
  "parentUuid": "fa7d7d0b-caf4-4bc6-ac7c-1672120b57e0",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERxraPB6U4inMTP2dYe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "727d28ab-80df-44fd-8f9d-defd7d9a5b11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AV1tkBxbUQjM3r4jUxYpRw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2044,
      "cache_read_input_tokens": 16689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2044,
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

_source line 11 · 2026-05-20T20:12:43.350Z_

<details><summary>↩ Tool result · `toolu_01PVwmi25StBsqej1zmpJsza`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "727d28ab-80df-44fd-8f9d-defd7d9a5b11",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "22fbf03c-1399-4ea1-abff-e421152751e0",
  "sourceToolAssistantUUID": "727d28ab-80df-44fd-8f9d-defd7d9a5b11",
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

_source line 12 · 2026-05-20T20:12:44.358Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QTdv1SGbLbd61w1jdYPc2g`</summary>

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
  "parentUuid": "22fbf03c-1399-4ea1-abff-e421152751e0",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERxraPB6U4inMTP2dYe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ea46dde-e8e2-4b5c-bb3e-e9b3d5c93343",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AV1tkBxbUQjM3r4jUxYpRw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2044,
      "cache_read_input_tokens": 16689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2044,
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

_source line 13 · 2026-05-20T20:12:44.369Z_

<details><summary>↩ Tool result · `toolu_01QTdv1SGbLbd61w1jdYPc2g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ROADMAP.md\", \"content\": \"# irt_equated_bench_regen — Research Dashboard\\n\\n> 最后更新: 2026-05-20 19:43 UTC | 更新原因: BE 重启恢复：更新 Dream ID + plan_003 拆分为 003a/003b/003c + METABENCH 下载状态\\n\\n## 核心方向\\n用 DIF 跨模型发布批次检测 benchmark 污染（RL-robust），结合多信号 ensemble 和 bifactor IRT equating 实现 benchmark 自愈。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 已通过 D002，2026-05-20）\\n- **Framing**: 3 条 Core Claims（Detection / Ensemble / Regeneration）\\n- **Plan**: 11 个实验（P0×5 / P1×3 / P2×3），总 GPU 预估 600h\\n- **Dream**: dream_20260520T194223 pending（full review，原 dream 因 BE 重启崩溃后自动重跑）\\n- **服务器/GPU**: 未配置（等 Dream 通过后配置）\\n- **文献图谱**: 10 篇，待蒸馏\\n\\n## Core Claims (from paper_framing.md)\\n1. **Detection**: DIF + ETS C 在 N≥80, δ≥1.4 时 TPR=0.72-0.85, FPR<0.05，RL-robust\\n2. **Ensemble**: DIF + ConStat + DVD 多信号覆盖全效应量谱\\n3. **Regeneration**: Bifactor IRT equating 实现心理测量等价的 item 替换\\n\\n## Experiment Plan Summary (from experiment_plan.yaml)\\n| ID | Name | Claim | Priority | GPU(h) | Deps |\\n|----|------|-------|----------|--------|------|\\n| plan_001 | real_data_dif_mmlu | 1 | P0 | 0 | - |\\n| plan_002 | rl_robustness_validation | 1 | P0 | 100 | 001 |\\n| plan_003a | constat_perturbation_eval | 2 | P0 | 80 | 001 |\\n| plan_003b | dvd_generation_variance_eval | 2 | P0 | 70 | 001 |\\n| plan_003c | ensemble_fusion | 2 | P0 | 0 | 001,003a,003b |\\n| plan_004 | cross_benchmark_gsm8k | 1 | P1 | 100 | 001 |\\n| plan_005 | bifactor_irt_equating_pilot | 3 | P1 | 50 | 001 |\\n| plan_006 | item_generation_calibration | 3 | P1 | 200 | 005 |\\n| plan_007 | cumulative_bayesian_dif | 1 | P2 | 0 | 001 |\\n| plan_008 | graceful_degradation | 3 | P2 | 0 | 005,006 |\\n| plan_009 | item_focused_trees | 1 | P2 | 0 | 001 |\\n\\n## 近期任务\\n- [ ] 等 Dream 回调（dream_20260520T194223），审查模拟审稿\\n- [ ] METABENCH 数据下载（首次 Worker 失败，Agent 处理中）\\n- [ ] Dream 通过后：配置服务器/GPU，批准 P0 实验\\n- [ ] 用户触发文献蒸馏\\n\\n## GPU 预算\\nP0: 250h | P1: 350h | P2: 0h | 总计 600h（项目预算 900-1200h，留余量）\\n\\n## 投稿目标\\nICLR 2027（~2026年10月 DDL，主目标）| AAAI 2027（2026.07.28）| EACL 2027 ARR August（2026.08.03）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D002 | 2026-05-20 | MVP 通过：DIF+ETS C 在 N≥80,δ≥1.4 下功效达标，推荐 N≥100 为主操作点 | mvp_dif_power_sim, mvp_dif_power_sim_phase2 |\\n| D001 | 2026-05-20 | MVP DIF 检测采用 ETS C 分类（效应量+显著性双阈值）替代 BH 校正 p 值作为主判定 | mvp_dif_power_sim |\\n\\n\\n\\n\", \"total_chars\": 2226, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ea46dde-e8e2-4b5c-bb3e-e9b3d5c93343",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "2021d934-ac97-4dc9-b471-fec185a28aae",
  "sourceToolAssistantUUID": "7ea46dde-e8e2-4b5c-bb3e-e9b3d5c93343",
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

_source line 14 · 2026-05-20T20:12:45.256Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Hzf7Tg52QysUCcdHRe3c8y`</summary>

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
  "parentUuid": "2021d934-ac97-4dc9-b471-fec185a28aae",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERxraPB6U4inMTP2dYe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75bb12ed-fe87-4094-860f-ef46740bfe98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AV1tkBxbUQjM3r4jUxYpRw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2044,
      "cache_read_input_tokens": 16689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2044,
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

_source line 15 · 2026-05-20T20:12:45.268Z_

<details><summary>↩ Tool result · `toolu_01Hzf7Tg52QysUCcdHRe3c8y`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/memory.md\", \"content\": \"## MVP 验证关键经验 (2026-05-20)\\n\\n### D001 决策：ETS C 分类 > p-value 检验\\n- **p-value based DIF 检测在 200-item benchmark 上严重 underpowered**：BH 校正后 TPR 仅 0.04-0.07（N=50, δ=1.0）。即使 raw（不校正）TPR 也只有 0.36-0.39，远低于 0.70 目标\\n- **ETS C 分类（|Δ_MH|≥1.5 + 显著性）是可行的替代**：TPR=0.68-0.85 at N≥80, δ≥1.4。本质是 magnitude-based detection，绕过了多重检验问题\\n- **AUC 一直很好（0.91-0.96）**：说明 DIF 统计量的区分能力没问题，问题在假设检验的 threshold，不在信号本身\\n- **原因**：200 个 items 做 BH 校正，需要极小的 p-value 才能过。N=50-100 per group 对 MH/LR 的 per-item 统计功效不够产生 p<0.001 级别的 evidence\\n\\n### Phase 2 验证：真实参数稳健\\n- **PSN-IRT 真实 MMLU 参数** vs 合成参数差异显著：b_mean=-0.84（真实）vs 0.0（合成），即真实 MMLU items 偏容易\\n- 尽管参数分布差异大，ETS C TPR 在真实参数下反而更高（N=100, δ=1.6: 0.80 vs Phase 1 的 0.85）——差异不大，结论稳健\\n- **Phase 2 用了 PSN-IRT 而非 METABENCH**：PSN-IRT 的 item_parameters.csv 可直接使用（14042 items），无需下载 620MB 大包\\n\\n### 关键操作参数\\n- N≥80/group 是最低要求，N≥100 显著改善功效\\n- δ≥1.4 logits 是可靠检测区间，δ=1.0 在边界\\n- MH 5 层 quantile-based 分层 + ETS C 阈值是当前最佳组合\\n- LR 方法与 MH 表现相当，无显著优势\\n\\n## Phase 2 数据源调研 (2026-05-20)\\n\\n### PSN-IRT (AAAI 2026)\\n\\n- **论文全名**: \\\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\\\"\\n- **作者**: Joe-Hall-Lee et al.\\n- **发表**: AAAI 2026 Oral\\n- **GitHub**: https://github.com/Joe-Hall-Lee/PSN-IRT\\n- **IRT 参数公开**: ✅ 是\\n  - `results/item_parameters.csv`: 全部 41,871 items 的 4PL 参数 (a=discrimination, b=difficulty, c=guessing, d=feasibility)\\n  - `results/student_abilities.csv`: 12 个模型的 latent abilities (θ)\\n  - `data/combine.csv`: 12 LLMs × 11 benchmarks 的 binary response matrix\\n- **MMLU 覆盖**: 14,042 items（MMLU 全集）\\n- **模型数**: 仅 12 个\\n- **局限**: 12 个模型太少，IRT 参数估计的可靠性存疑（经典 IRT 通常需要 ≥200 考生）\\n\\n### METABENCH (Kipnis et al., ICLR 2025) ⭐ 推荐\\n\\n- **论文全名**: \\\"metabench — A Sparse Benchmark of Reasoning and Knowledge in Large Language Models\\\"\\n- **GitHub**: https://github.com/adkipnis/metabench\\n- **Zenodo 数据**: https://zenodo.org/records/12819251 (`data.tgz`, 620MB)\\n- **MMLU 覆盖**: 12,508 items\\n- **模型数**: 5,219 个模型（RDS 预处理后）\\n- **优势**: 模型数量充足（5000+），IRT 估计可靠\\n\\n### 数据规模对比\\n\\n| 数据源 | 模型数 | MMLU items | IRT 参数 | 获取难度 |\\n|--------|--------|------------|----------|----------|\\n| **METABENCH** | 5,219 | 12,508 | 2PL (预拟合) | ⭐ 低 |\\n| **PSN-IRT** | 12 | 14,042 | 4PL (PSN) | ⭐ 低 |\\n| **Open LLM LB v1** | ~数千 | ~14,042 | 无 | 中 |\\n\\n## METABENCH 数据探索关键发现 (2026-05-20)\\n\\n### RDS 预拟合 IRT 参数\\n- `mmlu-preproc.rds` 包含 **12,508 items 的 2PL IRT 参数** (difficulty, discrimination)\\n- Difficulty range: [0.008, 0.689], mean=0.444; Discrimination range: [-0.551, 0.291], mean=0.076\\n- 1,926 items (15.4%) 有负区分度\\n- 258 floor items (p<0.05), 0 ceiling items (p>0.95)\\n- **可直接使用，无需自行拟合 IRT**\\n\\n### 响应矩阵 & Train/Test Split\\n- 完整 5219×12508 响应矩阵在 RDS 中\\n- 预建 train/test split: 4,755 train / 464 test models\\n\\n### Cohort 可行性\\n- 通过模型名正则分类：仅 1,929/5,219 (37%) 可归类到已知 family\\n- **2 个年度 cohort 满足 N≥80**: 2023 (N=1,253), 2024 (N=658)\\n- 63% 模型无法从名称分类（社区微调/合并模型）\\n- **结论**: 粗粒度 2-cohort (2023 vs 2024) 可行；细粒度年度 cohort 需外部元数据\\n\\n### RL-trained 模型\\n- **477 个模型**名称含 RL/alignment 信号: DPO(346), ORPO(52), PPO(11), KTO(6)\\n- 大量隐式 RLHF 模型（Llama-3, Qwen-2 等）名称不含标记\\n- **结论**: RL 模型充足，可用于污染检测 validation\\n\\n### 模型准确率分布\\n- Mean=0.592, Std=0.160, Range=[0.218, 0.911]\\n- 366 (7%) 模型低于随机水平 (0.25)\\n- Top families: mistral-0.1 (400), llama-3 (308), llama-2 (161)\\n\\n### CSV vs RDS 差异\\n- CSV: 5,227 模型; RDS: 5,219 模型（8 个被预处理过滤）\\n- 每个 subject 的模型数在 5,225-5,227 之间（近完整覆盖）\\n\", \"total_chars\": 3288, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75bb12ed-fe87-4094-860f-ef46740bfe98",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "af470b5d-f9c8-4365-87e0-75a43549f87f",
  "sourceToolAssistantUUID": "75bb12ed-fe87-4094-860f-ef46740bfe98",
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

_source line 16 · 2026-05-20T20:12:45.545Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01J387u19DE5YpGN4BRcBcvK`</summary>

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
  "parentUuid": "af470b5d-f9c8-4365-87e0-75a43549f87f",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERxraPB6U4inMTP2dYe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54c0f26a-74f1-4c23-aeb6-43325bbab6a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AV1tkBxbUQjM3r4jUxYpRw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2044,
      "cache_read_input_tokens": 16689,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2044
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 397,
          "cache_read_input_tokens": 16689,
          "cache_creation_input_tokens": 2044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2044,
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

_source line 17 · 2026-05-20T20:12:45.560Z_

<details><summary>↩ Tool result · `toolu_01J387u19DE5YpGN4BRcBcvK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-20T17:30:00.000Z\\\"\\n  total_papers: 10\\ncategories:\\n  - key: \\\"contamination_detection\\\"\\n    name: \\\"Benchmark Contamination Detection\\\"\\n    narrative: \\\"Methods for detecting training data contamination in LLM benchmarks, including RL-robust approaches\\\"\\n  - key: \\\"irt_equating\\\"\\n    name: \\\"IRT Methodology & Equating\\\"\\n    narrative: \\\"Item Response Theory models, calibration, equating, and their application to LLM evaluation\\\"\\n  - key: \\\"benchmark_design\\\"\\n    name: \\\"Dynamic Benchmark Design\\\"\\n    narrative: \\\"Approaches for creating contamination-resistant or self-updating benchmarks\\\"\\n  - key: \\\"dif_methodology\\\"\\n    name: \\\"DIF Statistical Methods\\\"\\n    narrative: \\\"Differential Item Functioning detection methods, power analysis, and small-sample strategies\\\"\\n  - key: \\\"item_generation\\\"\\n    name: \\\"Automated Item Generation\\\"\\n    narrative: \\\"LLM-based test item generation with difficulty control and psychometric validation\\\"\\npapers:\\n  wang2026fragility:\\n    title: \\\"On The Fragility of Benchmark Contamination Detection in Reasoning Models\\\"\\n    authors:\\n      - \\\"Wang, Y.\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2510.02386\\\"\\n    bibtex_key: \\\"wang2026fragility\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Proves GRPO/PPO RL training conceals contamination signals (14-20pp AUROC degradation), motivating our DIF-based approach which operates on behavioral patterns immune to NLL smoothing\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  liang2026dvd:\\n    title: \\\"DVD: Detection via Variance of Generation Distribution for Variant Contamination\\\"\\n    authors:\\n      - \\\"Liang, Y.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2601.04895\\\"\\n    bibtex_key: \\\"liang2026dvd\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Detects variant contamination via generation variance (AUC 0.73-0.74 vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under RL training\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  tao2026selfcritique:\\n    title: \\\"Detecting Data Contamination from Reinforcement Learning Post-training\\\"\\n    authors:\\n      - \\\"Tao, S.\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2510.09259\\\"\\n    bibtex_key: \\\"tao2026selfcritique\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse detection, but remains individual-model-level; our DIF is group-level and complementary\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  polo2026growingpains:\\n    title: \\\"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\\\"\\n    authors:\\n      - \\\"Polo, F.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"polo2026growingpains\\\"\\n    category: \\\"irt_equating\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Uses multidimensional IRT with fixed-parameter calibration and 100 anchor items for extensible evaluation (rho>=0.9); addresses score comparability but NOT contamination detection or item regeneration\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  polo2026psnirt:\\n    title: \\\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\\\"\\n    authors:\\n      - \\\"Polo, F.\\\"\\n    year: 2026\\n    venue: \\\"AAAI 2026\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"polo2026psnirt\\\"\\n    category: \\\"irt_equating\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"PSN-IRT analyzes benchmark quality via 4PL IRT; provides published IRT parameters for MMLU we can use in semi-synthetic validation\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  white2025livebench:\\n    title: \\\"LiveBench: A Challenging, Contamination-Free LLM Benchmark\\\"\\n    authors:\\n      - \\\"White, C.\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"white2025livebench\\\"\\n    category: \\\"benchmark_design\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Monthly-updated contamination-free benchmark with objective scoring; no difficulty calibration or psychometric equivalence across updates\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  zhang2024gsm1k:\\n    title: \\\"A Careful Examination of Large Language Model Performance on Grade School Arithmetic\\\"\\n    authors:\\n      - \\\"Zhang, H.\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2405.00332\\\"\\n    bibtex_key: \\\"zhang2024gsm1k\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"GSM1K documents 10-13% average accuracy drops from contamination; provides ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4 logits) critical for our DIF power analysis\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  hardy2026scalability:\\n    title: \\\"Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients\\\"\\n    authors:\\n      - \\\"Hardy, M.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2603.24999\\\"\\n    bibtex_key: \\\"hardy2026scalability\\\"\\n    category: \\\"irt_equating\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Nonparametric signed isotonic R2 scalability coefficients outperform IRT item diagnostics; lightweight pre-filter for item quality before our parametric calibration\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  kim2019fpc:\\n    title: \\\"Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data\\\"\\n    authors:\\n      - \\\"Kim, S.\\\"\\n      - \\\"Kolen, M.\\\"\\n    year: 2019\\n    venue: \\\"Applied Measurement in Education\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"kim2019fpc\\\"\\n    category: \\\"irt_equating\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Fixed-parameter calibration requires only N>=200 vs N>=500 for full calibration; core methodology for our bifactor IRT equating with anchor items\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  belzak2020smallsample:\\n    title: \\\"Testing Differential Item Functioning in Small Samples\\\"\\n    authors:\\n      - \\\"Belzak, W.\\\"\\n    year: 2020\\n    venue: \\\"Multivariate Behavioral Research\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"belzak2020smallsample\\\"\\n    category: \\\"dif_methodology\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Parsimonious logistic regression with sum scores outperforms complex IRT models for DIF detection in small samples; directly applicable to our N=50-80 model cohorts\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n\", \"total_chars\": 7312, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54c0f26a-74f1-4c23-aeb6-43325bbab6a1",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "e5c80810-dd4a-4cb8-91fe-f1e5cc5d308e",
  "sourceToolAssistantUUID": "54c0f26a-74f1-4c23-aeb6-43325bbab6a1",
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

_source line 18 · 2026-05-20T20:12:49.264Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0154Rh8p2f5zQ7eSZMkAbSh9`</summary>

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
  "parentUuid": "e5c80810-dd4a-4cb8-91fe-f1e5cc5d308e",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERyJBkoPQtcxDLb4Smf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52d77f95-3763-4c72-8fb9-e5fb8bf7587a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AX1izjnkrkEU9beh5E6RJG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7442,
      "cache_read_input_tokens": 18733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7442,
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

_source line 19 · 2026-05-20T20:12:49.277Z_

<details><summary>↩ Tool result · `toolu_0154Rh8p2f5zQ7eSZMkAbSh9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md\", \"content\": \"# Paper Framing — irt_equated_bench_regen\\n\\n## Target Venue\\n- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)\\n- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)\\n- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)\\n\\n## Core Claims (3 条, 可证伪)\\n\\n**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.\\n\\n**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.\\n\\n**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.\\n\\n## Story Spine\\n\\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \\\"Model B outperforms Model A on MMLU,\\\" we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.\\n\\n**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\\n\\n**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates the first self-healing benchmark framework.\\n\\n**Headline result template**: \\\"On MMLU with 5,000+ models spanning 1.5 years of active LLM development (2023–mid 2024), DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026).\\\"\\n\\n## Venue Fit Risks\\n\\n- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ \\\"fairness testing for items\\\").\\n- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: \\\"examinees\\\" → \\\"models\\\", \\\"test items\\\" → \\\"benchmark questions\\\", \\\"DIF\\\" → \\\"item-level contamination signal\\\", \\\"equating\\\" → \\\"score comparability across benchmark versions\\\".\\n- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as \\\"bringing mature psychometric tools to solve an urgent ML problem\\\" rather than \\\"inventing new statistics.\\\"\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"DIF power is only sufficient for large effects (δ≥1.4)\\\"**\\n   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.\\n   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)\\n\\n2. **\\\"Model cohort sample sizes are too small for classical DIF\\\"**\\n   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.\\n   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)\\n\\n3. **\\\"Only validated in simulation\\\"**\\n   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.\\n   - Evidence needed: plan_001, plan_004\\n\\n4. **\\\"Item regeneration quality — how do you ensure replacements measure the same construct?\\\"**\\n   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.\\n   - Evidence needed: plan_005, plan_006\\n\\n5. **\\\"RL robustness is only theoretical — where's the empirical evidence?\\\"**\\n   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.\\n   - Evidence needed: plan_002\\n\\n6. **\\\"Computational cost of the full pipeline\\\"**\\n   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.\\n\", \"total_chars\": 6493, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52d77f95-3763-4c72-8fb9-e5fb8bf7587a",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "1f5a4d23-416f-4b48-8de5-cac82327108c",
  "sourceToolAssistantUUID": "52d77f95-3763-4c72-8fb9-e5fb8bf7587a",
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

_source line 20 · 2026-05-20T20:12:49.855Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FfunTLeQZPHGKPV4ZnfxZe`</summary>

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
  "parentUuid": "1f5a4d23-416f-4b48-8de5-cac82327108c",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERyJBkoPQtcxDLb4Smf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54961c9b-3130-4940-9033-e58da8d2a6fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AX1izjnkrkEU9beh5E6RJG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7442,
      "cache_read_input_tokens": 18733,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7442
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 18733,
          "cache_creation_input_tokens": 7442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7442,
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

_source line 21 · 2026-05-20T20:12:49.864Z_

<details><summary>↩ Tool result · `toolu_01FfunTLeQZPHGKPV4ZnfxZe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/decisions.yaml\", \"content\": \"_next_id: 3\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:50 UTC\\n  summary: MVP DIF 检测采用 ETS C 分类（效应量+显著性双阈值）替代 BH 校正 p 值作为主判定标准\\n  rationale: Monte Carlo 模拟显示 BH 校正在 200 items 场景下将 TPR 压缩 40-60%，所有核心条件均 FAIL/GRAY。但\\n    ETS C 分类（|Δ_MH|≥1.5 + 显著性，教育测量 gold standard）在 N≥80, δ≥1.4 时 TPR=0.72-0.85, FPR<0.05，满足\\n    pass criteria。ETS C 是 DIF 领域标准实践（Holland & Thayer 1988），使用效应量阈值比纯 p 值更稳健。操作点 N≥80,\\n    δ≥1.4 与 GSM1K 文档的重度污染效应量吻合。小效应由 ensemble 其他信号覆盖。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'BH-corrected: all FAIL/GRAY; ETS C: PASS at N≥80,δ≥1.4 (TPR=0.72-0.85,\\n      FPR<0.05)'\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:31 UTC\\n  summary: MVP 通过：DIF+ETS C 在 N≥80,δ≥1.4 下功效达标，推荐 N≥100 为主操作点\\n  rationale: Phase 1 合成参数 + Phase 2 真实参数（PSN-IRT）均验证 ETS C TPR≥0.65 at N≥80,δ≥1.4。Phase\\n    2 比 Phase 1 降低 3-6pp 符合预期。N=80,δ=1.4 裕度仅 0.032，推荐 N≥100 为主 claim。数据源为 PSN-IRT\\n    而非 ROADMAP 指定的 METABENCH，research 阶段需用 METABENCH 补充验证。限制：δ<1.0 需 ensemble 其他信号。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'Phase 1 conditional pass: ETS C TPR=0.72-0.85 at N≥80,δ≥1.4'\\n  - exp_id: mvp_dif_power_sim_phase2\\n    role: evidence\\n    result: 'Phase 2 pass: ETS C TPR=0.68-0.80 at N≥80,δ≥1.4 with real MMLU params'\\n  depends_on:\\n  - D001\\n\", \"total_chars\": 1300, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54961c9b-3130-4940-9033-e58da8d2a6fe",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "3a5bd2fd-b22a-4caa-b445-2d784ee5282b",
  "sourceToolAssistantUUID": "54961c9b-3130-4940-9033-e58da8d2a6fe",
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

_source line 22 · 2026-05-20T20:12:52.962Z_

Now let me look at the actual paper artifacts and experiment code/results to get a more complete picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a5bd2fd-b22a-4caa-b445-2d784ee5282b",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERyceWdzeyVH1WTbzNt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89440820-4eb7-4276-a2c6-ddfa9105d136",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoeGHdbpCs5DB7i3XGbncN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3264,
      "cache_read_input_tokens": 26175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3264,
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

_source line 23 · 2026-05-20T20:12:54.393Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013kQmx1HoY9CsVTmNRvNtsV`</summary>

```json
{
  "pattern": "**/*.{tex,pdf,md}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89440820-4eb7-4276-a2c6-ddfa9105d136",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERyceWdzeyVH1WTbzNt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcb06438-e68b-4180-8da8-177b780baa3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoeGHdbpCs5DB7i3XGbncN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3264,
      "cache_read_input_tokens": 26175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3264,
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

_source line 24 · 2026-05-20T20:12:54.414Z_

<details><summary>↩ Tool result · `toolu_013kQmx1HoY9CsVTmNRvNtsV`</summary>

```text
artifacts/_project/chart/dif_power_curves.pdf
artifacts/mvp_dif_power_sim/chart/dif_power_curves.pdf
artifacts/dif_power_curves.pdf
artifacts/dif_diagnostic_pvalue_dist.pdf
artifacts/mvp_dif_power_sim/chart/dif_diagnostic_pvalue_dist.pdf
artifacts/_project/chart/dif_phase2_param_distribution.pdf
artifacts/dif_phase2_param_distribution.pdf
artifacts/_project/chart/dif_phase2_power_curves.pdf
artifacts/dif_phase2_power_curves.pdf
artifacts/_project/report/metabench_data_summary.md
artifacts/_project/report/metabench_data_summary_ec3bbf.md
artifacts/metabench_data_summary.md
artifacts/dream_reports/dream_20260520T194223/best/paper_framing.md
artifacts/dream_reports/dream_20260520T194223/best/paper.tex
artifacts/dream_reports/dream_20260520T194223/best/paper.pdf
artifacts/dream_reports/dream_20260520T194223/median/paper_framing.md
artifacts/dream_reports/dream_20260520T194223/median/paper.tex
artifacts/dream_reports/dream_20260520T194223/median/paper.pdf
artifacts/dream_reports/dream_20260520T194223/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T194223/worst/paper.tex
artifacts/dream_reports/dream_20260520T194223/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcb06438-e68b-4180-8da8-177b780baa3f",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "7fa9a3fc-82a6-4bfb-ae7f-fd82710a3cb0",
  "sourceToolAssistantUUID": "bcb06438-e68b-4180-8da8-177b780baa3f",
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

_source line 25 · 2026-05-20T20:12:54.858Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Bm5C99E7aX2FY9pqkCSEfE`</summary>

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
  "parentUuid": "7fa9a3fc-82a6-4bfb-ae7f-fd82710a3cb0",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERyceWdzeyVH1WTbzNt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27dfd223-ff2b-431f-b95f-fc3e2dad9207",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoeGHdbpCs5DB7i3XGbncN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3264,
      "cache_read_input_tokens": 26175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3264,
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

_source line 26 · 2026-05-20T20:12:54.866Z_

<details><summary>↩ Tool result · `toolu_01Bm5C99E7aX2FY9pqkCSEfE`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27dfd223-ff2b-431f-b95f-fc3e2dad9207",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "c3b82e3d-e6b2-41f4-89b3-3ffab937afd7",
  "sourceToolAssistantUUID": "27dfd223-ff2b-431f-b95f-fc3e2dad9207",
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

_source line 27 · 2026-05-20T20:12:55.533Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01G31AfcWAXmBUobW9mcqqt6`</summary>

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
  "parentUuid": "c3b82e3d-e6b2-41f4-89b3-3ffab937afd7",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERyceWdzeyVH1WTbzNt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15985d8e-5a6e-48f8-9843-2b2c61efbca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoeGHdbpCs5DB7i3XGbncN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3264,
      "cache_read_input_tokens": 26175,
      "output_tokens": 324,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3264
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 324,
          "cache_read_input_tokens": 26175,
          "cache_creation_input_tokens": 3264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3264,
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

_source line 28 · 2026-05-20T20:12:55.542Z_

<details><summary>↩ Tool result · `toolu_01G31AfcWAXmBUobW9mcqqt6`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15985d8e-5a6e-48f8-9843-2b2c61efbca9",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "d4a109ab-1e50-4a5e-b50a-ab300944f204",
  "sourceToolAssistantUUID": "15985d8e-5a6e-48f8-9843-2b2c61efbca9",
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

_source line 29 · 2026-05-20T20:12:59.009Z_

Let me read the best dream paper (the simulated paper draft) to understand the full claims and related work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4a109ab-1e50-4a5e-b50a-ab300944f204",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERz31im9QoiE8dQXcQ7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8a610e7-398b-4a37-8629-b445b36953b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjfL4dkWQFM1tTcpPpo7ZY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 933,
      "cache_read_input_tokens": 29439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 933,
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

_source line 30 · 2026-05-20T20:12:59.506Z_

<details open><summary>🔧 Tool call — Read · `toolu_018mBfvtYSGA2pRC2nHA9Vxb`</summary>

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
  "parentUuid": "e8a610e7-398b-4a37-8629-b445b36953b9",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERz31im9QoiE8dQXcQ7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bf95e81-3223-4c38-9fff-50a63e485290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjfL4dkWQFM1tTcpPpo7ZY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 933,
      "cache_read_input_tokens": 29439,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 933
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 29439,
          "cache_creation_input_tokens": 933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 933,
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

_source line 31 · 2026-05-20T20:13:00.046Z_

<details><summary>↩ Tool result · `toolu_018mBfvtYSGA2pRC2nHA9Vxb`</summary>

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
  "parentUuid": "7bf95e81-3223-4c38-9fff-50a63e485290",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "28704e7f-de96-48cc-a926-40560c214038",
  "sourceToolAssistantUUID": "7bf95e81-3223-4c38-9fff-50a63e485290",
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

_source line 32 · 2026-05-20T20:13:02.862Z_

Now let me also read the dream review report and the best/worst paper framings to understand the full context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28704e7f-de96-48cc-a926-40560c214038",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERzN5CGJjVdh9997AxZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b681a1e8-00cd-45ef-a54d-1dca16c22530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrfSDF5DGYNX2B55hSaeFP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13083,
      "cache_read_input_tokens": 30372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13083,
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

_source line 33 · 2026-05-20T20:13:05.881Z_

<details open><summary>🔧 Tool call — Read · `toolu_017t9SbZWFBHgkZ36sv6d3RR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b681a1e8-00cd-45ef-a54d-1dca16c22530",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERzN5CGJjVdh9997AxZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7496fe4-fa2c-4496-8aaf-b5cfb2d16e35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrfSDF5DGYNX2B55hSaeFP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13083,
      "cache_read_input_tokens": 30372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13083,
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

_source line 34 · 2026-05-20T20:13:05.886Z_

<details><summary>↩ Tool result · `toolu_017t9SbZWFBHgkZ36sv6d3RR`</summary>

```text
1	# Paper Framing — irt_equated_bench_regen
2	
3	## Target Venue
4	- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)
5	- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)
6	- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)
7	
8	## Core Claims (3 条, 可证伪)
9	
10	**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.
11	
12	**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.
13	
14	**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.
15	
16	## Story Spine
17	
18	**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.
19	
20	**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.
21	
22	**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates the first self-healing benchmark framework.
23	
24	**Headline result template**: "On MMLU with 5,000+ models spanning 3 years of releases, DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026)."
25	
26	## Venue Fit Risks
27	
28	- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ "fairness testing for items").
29	- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: "examinees" → "models", "test items" → "benchmark questions", "DIF" → "item-level contamination signal", "equating" → "score comparability across benchmark versions".
30	- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as "bringing mature psychometric tools to solve an urgent ML problem" rather than "inventing new statistics."
31	
32	## Anticipated Reviewer Concerns
33	
34	1. **"DIF power is only sufficient for large effects (δ≥1.4)"**
35	   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.
36	   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)
37	
38	2. **"Model cohort sample sizes are too small for classical DIF"**
39	   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.
40	   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)
41	
42	3. **"Only validated in simulation"**
43	   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.
44	   - Evidence needed: plan_001, plan_004
45	
46	4. **"Item regeneration quality — how do you ensure replacements measure the same construct?"**
47	   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.
48	   - Evidence needed: plan_005, plan_006
49	
50	5. **"RL robustness is only theoretical — where's the empirical evidence?"**
51	   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.
52	   - Evidence needed: plan_002
53	
54	6. **"Computational cost of the full pipeline"**
55	   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7496fe4-fa2c-4496-8aaf-b5cfb2d16e35",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "a7f5c5cb-72a2-4082-8c0e-96b05b57f369",
  "sourceToolAssistantUUID": "f7496fe4-fa2c-4496-8aaf-b5cfb2d16e35",
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

_source line 35 · 2026-05-20T20:13:06.631Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019iqvG66uDmbgBfNyUosc2B`</summary>

```json
{
  "pattern": "**/dream_*/**/*.{md,yaml,json}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7f5c5cb-72a2-4082-8c0e-96b05b57f369",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERzN5CGJjVdh9997AxZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3534054e-3e95-49aa-9add-a7a2fcac5f59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrfSDF5DGYNX2B55hSaeFP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13083,
      "cache_read_input_tokens": 30372,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13083
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 30372,
          "cache_creation_input_tokens": 13083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13083,
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

_source line 36 · 2026-05-20T20:13:06.645Z_

<details><summary>↩ Tool result · `toolu_019iqvG66uDmbgBfNyUosc2B`</summary>

```text
artifacts/dream_reports/dream_20260520T194223/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194223/best/experiment_data.json
artifacts/dream_reports/dream_20260520T194223/best/paper_framing.md
artifacts/dream_reports/dream_20260520T194223/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194223/median/experiment_data.json
artifacts/dream_reports/dream_20260520T194223/median/paper_framing.md
artifacts/dream_reports/dream_20260520T194223/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194223/worst/experiment_data.json
artifacts/dream_reports/dream_20260520T194223/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T194223/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3534054e-3e95-49aa-9add-a7a2fcac5f59",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "d918ad35-6d89-4355-a284-ee6d660543ea",
  "sourceToolAssistantUUID": "3534054e-3e95-49aa-9add-a7a2fcac5f59",
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

_source line 37 · 2026-05-20T20:13:09.579Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HfJCqpGpjJXbraKYsAbLkK`</summary>

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
  "parentUuid": "d918ad35-6d89-4355-a284-ee6d660543ea",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERzrWDxFv9RyyjNnyCH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72de2998-4c06-4e29-ae83-ed93015b2106",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkTLF3SY6u1qKFqSawWMwX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2334,
      "cache_read_input_tokens": 43455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2334,
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

_source line 38 · 2026-05-20T20:13:10.044Z_

<details><summary>↩ Tool result · `toolu_01HfJCqpGpjJXbraKYsAbLkK`</summary>

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
  "parentUuid": "72de2998-4c06-4e29-ae83-ed93015b2106",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "f2d5cbfc-d473-4126-90e8-3c6b3afadf60",
  "sourceToolAssistantUUID": "72de2998-4c06-4e29-ae83-ed93015b2106",
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

_source line 39 · 2026-05-20T20:13:10.103Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T7d8FWt8s5gVcCn6sNs2tQ`</summary>

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
  "parentUuid": "f2d5cbfc-d473-4126-90e8-3c6b3afadf60",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbERzrWDxFv9RyyjNnyCH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "477e54cf-173f-4e83-acd7-88a81697a954",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkTLF3SY6u1qKFqSawWMwX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2334,
      "cache_read_input_tokens": 43455,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2334
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 43455,
          "cache_creation_input_tokens": 2334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2334,
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

_source line 40 · 2026-05-20T20:13:10.373Z_

<details><summary>↩ Tool result · `toolu_01T7d8FWt8s5gVcCn6sNs2tQ`</summary>

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
  "parentUuid": "477e54cf-173f-4e83-acd7-88a81697a954",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "f71aaf3c-e6cb-44d6-a012-33f6544d49cb",
  "sourceToolAssistantUUID": "477e54cf-173f-4e83-acd7-88a81697a954",
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

_source line 41 · 2026-05-20T20:13:15.747Z_

Now I have a thorough understanding of the paper. Let me also check the Self-Critique/RL-MIA paper (Tao et al., ICLR 2026) cited in the literature map, as it is a key competitor that addresses the same RL-robustness problem. Let me now formulate the review.

Now let me submit the review via the appropriate tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f71aaf3c-e6cb-44d6-a012-33f6544d49cb",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbES18DY55ep5xxdkqNZC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b737b256-62bd-49d2-b5b5-41dc65c6c5a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StDkpmb78nHWybBgDa83cw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38034,
      "cache_read_input_tokens": 45789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 38034,
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

_source line 42 · 2026-05-20T20:13:16.223Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01X3iEJ2gbvuumBuhE52JVvk`</summary>

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
  "parentUuid": "b737b256-62bd-49d2-b5b5-41dc65c6c5a7",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbES18DY55ep5xxdkqNZC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1710afc9-10b0-44ce-9c23-95e89b063078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StDkpmb78nHWybBgDa83cw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38034,
      "cache_read_input_tokens": 45789,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 38034
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 45789,
          "cache_creation_input_tokens": 38034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 38034,
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

_source line 43 · 2026-05-20T20:13:16.225Z_

<details><summary>↩ Tool result · `toolu_01X3iEJ2gbvuumBuhE52JVvk`</summary>

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
  "parentUuid": "1710afc9-10b0-44ce-9c23-95e89b063078",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "dcbdf9ce-219f-4c00-b283-fd25a5439a55",
  "sourceToolAssistantUUID": "1710afc9-10b0-44ce-9c23-95e89b063078",
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

_source line 44 · 2026-05-20T20:14:59.645Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01WdE5czQEro1hcuru81d3wD`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "tier": "best",
  "dream_id": "dream_20260520T194223",
  "overall_score": "Weak Accept (4/6)",
  "report": "# Reviewer 2 (R2): Novelty and Related Work\n\n## Summary\n\nThis paper reframes LLM benchmark contamination as a psychometric phenomenon — Differential Item Functioning (DIF) — and proposes a \"self-healing benchmark\" framework combining DIF-based detection, a multi-signal ensemble (DIF + ConStat + DVD), and bifactor IRT equating for benchmark regeneration. The central insight is that DIF operates on group-level behavioral patterns immune to the within-model distribution smoothing that RL training performs, achieving 96% power retention where 10 existing detectors degrade to near-random. The paper is ambitious in scope, attempting to close the full loop from detection through generation to psychometrically equated regeneration.\n\n## Strengths\n\n- **Compelling conceptual reframing.** Casting contamination as DIF is a genuinely insightful bridge between educational measurement and ML evaluation. The argument that group-level ICC-based detection is orthogonal to within-model distribution smoothing is theoretically well-motivated and represents a real conceptual contribution. This reframing, if validated, could shift how the community thinks about contamination — from a model-level anomaly detection problem to a population-level psychometric one.\n\n- **RL-robustness argument is the paper's strongest novelty.** The theoretical argument (RL cannot eliminate the behavioral fact of answering memorized items correctly without negating contamination's purpose) is elegant and non-obvious. The 96% power retention result (Table 3-4) against 10 baselines degrading to near-random is a striking empirical demonstration. This is timely given the ecosystem shift toward RL-trained reasoning models.\n\n- **Comprehensive system design.** The full pipeline (detection → ensemble → generation → calibration → equating → graceful degradation) is well-architected. Each component addresses a genuine limitation of the previous one. The graceful degradation analysis (Table 16) with formal bounds is particularly thoughtful and practically useful.\n\n- **Strong external validation strategy.** Using MMLU-CF as partial ground truth for MMLU (phi=0.42) and GSM1K as independent ground truth for GSM8K (rho=0.43) provides convergent evidence from two entirely different validation sources. The honest acknowledgment that phi=0.42 is moderate (not perfect) because MMLU-CF modifications do not correspond one-to-one with contamination is scientifically responsible.\n\n- **Scale of evaluation.** METABENCH with 5,055 models and 12,508 items is a serious evaluation at realistic scale, not a toy setup. The sensitivity analysis across cohort splits (Table 1) showing TPR stability in 0.72-0.83 is reassuring.\n\n- **Complementarity analysis is well-executed.** Table 8's decomposition of unique detections per signal (12-28% each) empirically justifies the ensemble design rather than just asserting complementarity.\n\n## Weaknesses\n\n### Major\n\n- **(M1) DIF is not new, and the novelty claim needs more careful positioning.** DIF (Holland & Thayer, 1988) and the ETS A/B/C classification are standard tools in educational measurement with 35+ years of history. The Mantel-Haenszel statistic is a textbook method. The paper's novelty rests entirely on the *application* of these existing tools to LLM benchmark contamination and the *argument* for RL-robustness. The related work section (§2, \"Psychometrics in NLP Evaluation\") is too brief — it names IRT, bifactor models, and DIF in educational testing in three sentences without engaging with the substantial body of work applying IRT to NLP evaluation (e.g., Lalor et al. 2019; Rodriguez et al. 2021; Vania et al. 2021; Polo et al. PSN-IRT). The paper should explicitly acknowledge that it is importing mature methodology rather than creating new statistics, and argue more carefully why this cross-disciplinary transfer constitutes sufficient novelty. As written, a psychometrics reviewer would see no methodological novelty, while an ML reviewer might overestimate the statistical contribution.\n\n- **(M2) The RL-robustness argument has a significant gap: it is validated only against RL models that happen to exist, not against RL specifically optimized to evade DIF.** The theoretical argument (\"RL cannot eliminate the behavioral fact\") assumes the adversary's goal is only to inflate scores. But a sophisticated adversary could train with a contamination-aware RL objective that selectively suppresses performance on known-contaminated items for a subset of the cohort, introducing noise into the DIF signal. The paper does not address adversarial robustness — only \"natural\" RL robustness. This distinction matters because the paper frames DIF as having a fundamental advantage (\"the only way to defeat DIF would be for the model to deliberately answer memorized items incorrectly\"), but a more nuanced adversarial strategy (e.g., answering correctly only on a random subset, or calibrating confidence to match clean-item patterns) could degrade DIF without fully negating contamination benefit. The 14 RL models tested are all \"honest\" RL models, not adversarial ones.\n\n- **(M3) Missing critical related work: Tao et al. (ICLR 2026) \"Self-Critique\" / RL-MIA.** This paper is listed in the literature map but barely discussed in the paper itself. Tao et al. directly address the same problem (detecting contamination post-RL training) via policy-collapse detection. The paper needs a detailed comparison: What is DIF's advantage over Self-Critique? Is Self-Critique also group-level or individual-model-level? What are the complementary strengths? Without this comparison, the claim \"no existing work\" addresses RL-robust detection is incomplete. Additionally, the related work omits: (a) Dekoninck et al.'s full ConStat paper details (cited but not discussed mechanistically); (b) MMLU-CF (Li et al., 2024) which is used as ground truth but not discussed as related work on contamination-resistant benchmarks; (c) Oren et al. (2024) on proving test set contamination; (d) Deng et al. (2024) on investigating data contamination in modern benchmarks.\n\n- **(M4) The ensemble contribution (Claim 2) is incremental.** Combining three existing detection signals with weighted fusion is standard methodology. The complementarity analysis is well-done but the ensemble design itself (optimize weights on calibration set, compare majority voting vs. weighted fusion) involves no methodological novelty. The specific weight values (0.45/0.30/0.25) appear optimized on the same data used for evaluation — is there a held-out calibration/test split? If not, the 87% TPR may be optimistically biased.\n\n### Minor\n\n- **(m1) Bifactor IRT equating for MMLU is a natural application, not a novel method.** Bifactor models and fixed-parameter calibration with anchor items are standard psychometric practice (Kolen & Brennan, 2014; Kim & Kolen, 2019 — already cited). The contribution is demonstrating feasibility on MMLU, not methodological innovation. The paper should be more explicit about this.\n\n- **(m2) The \"self-healing benchmark\" framing, while catchy, slightly overpromises.** The system requires human-in-the-loop decisions (cohort definitions, anchor item selection criteria, quality filtering of generated items at 84% pass rate, weight calibration). It is more accurately a \"semi-automated benchmark maintenance framework\" than a self-healing one. The terminology risks creating expectations of a fully autonomous system.\n\n- **(m3) Item-Focused Trees (§5.8) and Cumulative Bayesian DIF (§5.7) add breadth but limited depth.** IFT provides only +3pp TPR improvement over ETS C at 12x computational cost. The Bayesian DIF is a straightforward sequential updating application. Neither component individually would constitute a publishable contribution, and their inclusion dilutes focus from the core DIF + ensemble + equating story.\n\n- **(m4) Table 3 comparison fairness.** Comparing DIF (which requires a population of models) against individual-model detectors (Min-K%, perplexity, etc.) is somewhat apples-to-oranges. DIF has strictly more information available (group-level patterns across many models). The paper should acknowledge this information asymmetry rather than presenting the comparison as purely about detection mechanism quality.\n\n- **(m5) ConStat TPR inversion at delta >= 1.4.** The explanation (extremely contaminated items are intrinsically easy) is plausible but not empirically verified. Are the high-delta items actually easier? This should be checked.\n\n## Questions for Authors\n\n1. **Adversarial robustness**: What happens if an adversary deliberately trains a model to answer known-contaminated items correctly only 70% of the time (vs. 95%+ for clean items at the same difficulty)? This would reduce the DIF signal while retaining most contamination benefit. Have you analyzed DIF sensitivity to partial contamination exploitation?\n\n2. **Cohort definition sensitivity**: The temporal cohort split is a critical design choice. How sensitive are results to the exact cutoff date? What if contamination onset varies by model family (as your IFT analysis suggests)? Does using a single global cutoff introduce systematic bias?\n\n3. **Circular validation concern**: The DIF detection uses METABENCH model release dates to define cohorts. The MMLU-CF validation also uses temporal assumptions (items were modified because they were suspected to be contaminated over time). Is there a risk of circular reasoning where both DIF and the ground truth are driven by the same temporal confound (models genuinely improving over time on certain items, not contamination)?\n\n4. **Bifactor model identifiability**: With 57 subject-specific factors and 5,055 models, what is the effective sample size per factor? Some MMLU subjects have very few items. Did you encounter convergence issues? What estimation method was used (MCMC, EM, MHRM)?\n\n5. **Comparison with Tao et al. (ICLR 2026)**: Can you provide a direct empirical comparison of DIF vs. Self-Critique/RL-MIA on the same model set? Both claim RL-robustness — which performs better, and under what conditions?\n\n6. **Ensemble calibration**: Were the ensemble weights (0.45/0.30/0.25) optimized on the same data used to report the 87% TPR? If so, what is the cross-validated TPR estimate?\n\n## Detailed Comments on Novelty and Related Work\n\n### Component-by-Component Novelty Assessment\n\n| Component | Novelty Level | Justification |\n|-----------|--------------|---------------|\n| DIF for contamination | Moderate-High (application) | Genuinely new application of established method to an important problem. The reframing itself is insightful. |\n| RL-robustness argument | High (conceptual) | The theoretical argument is original and the empirical demonstration is compelling, though limited to non-adversarial settings. |\n| Multi-signal ensemble | Low | Standard weighted fusion of existing signals. Well-executed engineering but not methodologically novel. |\n| Bifactor IRT equating | Moderate (application) | First demonstration on LLM benchmarks. Standard psychometric methodology applied to a new domain. |\n| Student simulation calibration | Low-Moderate | Builds on existing work (arXiv 2601.09953). The comparison with prompt-based targeting is useful but not surprising. |\n| Cumulative Bayesian DIF | Low | Standard Bayesian sequential updating. |\n| Item-Focused Trees | Low | Existing method applied to contamination timing. The changepoint finding is interesting but secondary. |\n| Full pipeline integration | Moderate-High | No prior work connects detection, generation, calibration, and equating in a single framework. The integration is the contribution. |\n\n### Related Work Gaps\n\nThe related work section is the paper's weakest component from a novelty-and-positioning perspective:\n\n1. **Missing IRT-for-NLP papers**: Lalor et al. (2019, \"Learning Latent Parameters without Human Response Patterns\"), Rodriguez et al. (2021, \"Evaluation Examples Are Not Equally Informative\"), Vania et al. (2021, \"Comparing Test Sets with Item Response Theory\"). These directly apply IRT to NLP evaluation and should be discussed.\n\n2. **Missing contamination detection papers**: Oren et al. (2024, \"Proving Test Set Contamination in Black Box Language Models\"), Deng et al. (2024, \"Investigating Data Contamination in Modern Benchmarks\"), Xu et al. (2024, \"Benchmarking Benchmark Leakage\"). The coverage of the contamination detection landscape is incomplete.\n\n3. **Missing benchmark robustness work**: MMLU-CF (Li et al., 2024) is used as ground truth but not discussed as related work. HELMET, SEAL, and other contamination-resistant benchmark designs should be mentioned.\n\n4. **Tao et al. (ICLR 2026) insufficiently discussed**: This is the most direct competitor on RL-robust detection. The paper must engage with it substantively.\n\n5. **DIF methodology in education**: The paper uses DIF tools but does not cite the core DIF methodology literature beyond Holland & Thayer. Zumbo (1999), Penfield & Camilli (2007), and Magis et al. (2010) on DIF methodology should be cited to show awareness of the field being borrowed from.\n\n### Is This Incremental or Transformative?\n\nThe paper sits in between. It is not incremental in the dismissive sense — the DIF reframing is a genuine conceptual contribution that could influence how the community approaches contamination detection. The RL-robustness argument, if it holds under adversarial conditions, is practically important. However, it is also not transformative in the sense of introducing new methods: every statistical tool used (MH test, ETS classification, bifactor IRT, fixed-parameter calibration, Bayesian updating, Item-Focused Trees) is imported from educational measurement without modification. The contribution is in the assembly and application, not in the parts.\n\nFor a top ML venue, this positions the paper in the \"strong application of existing theory to important new domain\" category. This can be sufficient for acceptance if: (a) the problem is important enough (contamination is), (b) the application is non-trivial (the RL-robustness argument is), and (c) the execution is thorough (it is). The risk is that reviewers without psychometric background may overestimate novelty, while those with psychometric background may underestimate the contribution of the cross-disciplinary transfer.\n\n## Preliminary Score\n\n**Score: 4 (Weak Accept)**\n\n**Confidence: 4 (High)**\n\n### Justification\n\nThe paper addresses a genuinely important problem (RL-robust contamination detection) with a well-motivated approach (DIF reframing). The core conceptual contribution — that contamination creates DIF, and DIF is immune to RL smoothing because it operates on group-level behavioral patterns — is insightful and timely. The scale of evaluation (5,055 models, 12,508 items) and the dual external validation (MMLU-CF + GSM1K) are commendable.\n\nHowever, the novelty is primarily in application and integration, not in methodology. The related work section has significant gaps, particularly the insufficient engagement with Tao et al. (ICLR 2026) and the broader IRT-for-NLP literature. The RL-robustness claim, while compelling in non-adversarial settings, is not tested against adversarial RL strategies. The ensemble contribution is incremental. The paper tries to do too much (9 experiments, 19 tables), diluting focus — a tighter paper focused on DIF detection + RL robustness + one validation (either MMLU or GSM8K cross-validation) would be more impactful.\n\nI lean toward acceptance because: (1) the problem is urgent and worsening, (2) the DIF reframing is a genuine insight the community needs, (3) the empirical evaluation is thorough, and (4) the full-pipeline integration from detection to regeneration is practically valuable. But the paper needs to honestly position itself as importing psychometric methodology rather than inventing it, fill the related work gaps, and address the adversarial robustness limitation.\n\nA revised version addressing M1-M4 would move to a solid Accept (5/6).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcbdf9ce-219f-4c00-b283-fd25a5439a55",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbES1ZJec3Agdcpnr8gxU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ac44e75-ea6e-4ffd-9838-0eebdffddca0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012qzb7f9T8usxkjExzFUtuy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 83823,
      "output_tokens": 4026,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 800
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4026,
          "cache_read_input_tokens": 83823,
          "cache_creation_input_tokens": 800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 800,
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

_source line 45 · 2026-05-20T20:15:03.200Z_

<details><summary>↩ Tool result · `toolu_01WdE5czQEro1hcuru81d3wD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/review_report.md\", \"dream_id\": \"dream_20260520T194223\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ac44e75-ea6e-4ffd-9838-0eebdffddca0",
  "isSidechain": true,
  "promptId": "f8776afe-622a-4cd0-bd98-dbde869589d2",
  "agentId": "afd9dbd7380df2dbd",
  "type": "user",
  "uuid": "f661d327-58f3-40d4-9ff0-2f54febd2ca6",
  "sourceToolAssistantUUID": "5ac44e75-ea6e-4ffd-9838-0eebdffddca0",
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

_source line 46 · 2026-05-20T20:15:15.338Z_

Review submitted. Here is the summary:

**Score: 4/6 (Weak Accept), Confidence: 4/5 (High)**

**Key findings from the review:**

**Strengths identified:**
- The DIF reframing of contamination is a genuine conceptual contribution -- insightful cross-disciplinary bridge
- RL-robustness argument (group-level ICC vs. within-model distributions) is the paper's strongest novelty, both theoretically elegant and empirically supported (96% power retention vs. 10 baselines degrading to near-random)
- Thorough evaluation at realistic scale (5,055 models, 12,508 items) with dual external validation (MMLU-CF + GSM1K)
- Full pipeline integration (detection through regeneration) is practically valuable

**Major weaknesses flagged:**
- **(M1)** DIF itself is a 35-year-old textbook method; the related work on "Psychometrics in NLP Evaluation" is too thin (3 sentences) and misses key IRT-for-NLP papers (Lalor et al., Rodriguez et al., Vania et al.)
- **(M2)** RL-robustness is only validated against "honest" RL models, not adversarial RL designed to evade DIF -- the theoretical argument has gaps around partial exploitation strategies
- **(M3)** Tao et al. (ICLR 2026) Self-Critique/RL-MIA is the most direct competitor on RL-robust detection and is insufficiently discussed; several other contamination detection papers are missing
- **(M4)** Ensemble contribution (Claim 2) is incremental -- standard weighted fusion with possible overfitting concern on the 0.45/0.30/0.25 weights

**Bottom line:** The paper is in the "strong application of existing theory to an important new domain" category. The DIF reframing and RL-robustness argument are genuine contributions sufficient for a top venue, but the paper needs honest positioning about importing (not inventing) psychometric methodology, substantially expanded related work, and adversarial robustness analysis. Addressing the four major weaknesses would move the score to Accept (5/6).

Report saved to: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/review_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f661d327-58f3-40d4-9ff0-2f54febd2ca6",
  "isSidechain": true,
  "agentId": "afd9dbd7380df2dbd",
  "requestId": "req_011CbES9Sb4KmgruMy33oQQH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56cab91a-afa3-4f34-8236-d13d7129fa00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6c9cb23b-471b-4124-99d0-b8415cd0b2d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CkFFdR21yX95kszsm9nQQs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4159,
      "cache_read_input_tokens": 84623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4159,
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
