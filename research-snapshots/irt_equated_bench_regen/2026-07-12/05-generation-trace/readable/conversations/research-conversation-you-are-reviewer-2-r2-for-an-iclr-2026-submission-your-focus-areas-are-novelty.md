# Research conversation: You are Reviewer 2 (R2) for an ICLR 2026 submission. Your focus areas are **novelty, significance, related work, and pos

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad75a1b970c226edb.jsonl`
- **Structured JSON:** [`87973da1f125d31d5532.json`](../../sessions/87/87973da1f125d31d5532.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

49 recorded events

### User

_source line 1 · 2026-05-21T05:13:04.445Z_

You are Reviewer 2 (R2) for an ICLR 2026 submission. Your focus areas are **novelty, significance, related work, and positioning**. You must evaluate whether this is a genuine contribution to the field and whether it is properly contextualized.

## Venue: ICLR 2026
Rating scale: {0, 2, 4, 6, 8, 10}
- 10: Top 5% of accepted papers, seminal
- 8: Top 15%, strong accept
- 6: Marginally above acceptance threshold (weak accept)
- 4: Marginally below acceptance threshold (weak reject)
- 2: Reject
- 0: Strong reject

## Paper Summary

**Title**: "Temporal Item Instability in LLM Benchmarks: A Large-Scale Differential Item Functioning Analysis of MMLU"

The paper applies Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis from psychometrics to the METABENCH MMLU response matrix (5,227 models × 12,508 items). Key findings and claims:

1. **Claim 1 (Empirical discovery)**: 31.3% of MMLU items exhibit large temporal DIF (ETS Category C) between 2023 and 2024-H1 model cohorts. Robust across thresholds, not driven by capability gains (≤7.6%), architecturally trivial (99.98% decoder-only).

2. **Claim 2 (Ground truth meta-critique)**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment ≈ 0.96 against Li et al. labels is expected, not a failure. All item-level detectors validated against web-overlap ground truth share this blind spot.

3. **Claim 3 (Semi-synthetic validation framework)**: ΔTPR methodology with cross-subject matching (ΔFPR = 0.000). Portable across benchmarks (GSM8K: ΔTPR = +0.818).

4. **Claim 4 (DIF as diagnostic lens)**: DIF items are the least disruptive for non-random removal (ρ ≈ 0.997). GSM1K anti-correlation (r = −0.478): models with larger contamination gaps perform worse on DIF-C items.

## Related Work as Presented (§2)

The paper covers four areas:
1. **LLM Benchmark Contamination Detection**: Positions against Min-K% (Shi et al., 2024), ConStat (Dekoninck et al., 2024), DVD (2024). Claims DIF operates on binary response matrices and detects group-level differential functioning — fundamentally different signal.
2. **Web-Overlap and N-gram Methods**: Cites Li et al. (2024), Yang et al. (2023). Argues these conflate global exposure with differential contamination.
3. **Benchmark Maintenance and Temporal Stability**: Cites GSM1K (Zhang et al., 2024), Growing Pains (Perlitz et al., 2024). Claims DIF complements these by identifying which anchor items are degrading.
4. **Psychometric Methods for LLM Evaluation**: Cites IRT-LLM (2024), Holland & Thayer (1993), Zumbo (2007). Claims DIF has not been systematically applied to LLM evaluation at scale.

## Method

- Classical Mantel-Haenszel DIF with ETS A/B/C classification
- Temporal cohorts: 2023 (reference, N=1,253) vs 2024-H1 (focal, N=656)
- Semi-synthetic injection framework with cross-subject matching
- Cross-benchmark replication on GSM8K (1,319 items × 6,702 models)
- GSM1K contamination gap correlation (N=33)

## Appendices Cover

A: RL robustness (DIF vs Min-K% vs ConStat on reasoning-RL models)
B: ConStat perturbation evaluation
C: DVD generation variance evaluation
D: Ensemble fusion (DIF + ConStat + DVD)
E: Bifactor IRT and equating pilot
F: Item generation calibration
G: Cumulative Bayesian DIF
H: Graceful degradation under item replacement
I: Item-Focused Trees

## Key References (from the paper's bibliography)

Holland & Thayer (1993) — original MH-DIF
Zumbo (2007) — three generations of DIF
Li et al. (2024) — task contamination / web-overlap
Yang et al. (2023) — rephrased samples
Shi et al. (2024) — Min-K%
Dekoninck et al. (2024) — ConStat
DVD (2024) — generation variance
Zhang et al. (2024) — GSM1K
Perlitz et al. (2024) — Growing Pains
METABENCH (2024) — data source
IRT-LLM (2024) — IRT for LLM evaluation

## Your Task

Write a detailed ICLR-style review focusing on:

1. **Summary** (2-3 sentences)
2. **Strengths** (novelty, significance, related work coverage, numbered list)
3. **Weaknesses** (novelty concerns, missing related work, positioning issues, numbered list)
4. **Questions for Authors** (numbered list)
5. **Missing Related Work** (specific papers or research areas that should be discussed)
6. **Minor Issues**
7. **Preliminary Scores**:
   - Soundness (1-4)
   - Presentation (1-4)
   - Contribution (1-4)
   - Overall recommendation (0-10 ICLR scale with label)
   - Confidence (1-5)

Critical evaluation criteria for novelty:
- Is applying MH-DIF to LLM benchmarks a genuine intellectual contribution, or merely an application of a known method to a new dataset?
- Does the ground truth meta-critique (Claim 2) represent a genuine insight or an obvious observation?
- Is the semi-synthetic framework (Claim 3) sufficiently novel given that injection-based validation is common?
- Are there prior works applying DIF or similar psychometric methods to LLM evaluation that are not cited?
- Does the paper adequately distinguish its contribution from the IRT-LLM (2024) line of work?

Be rigorous and independent. Return your full review as plain text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "470daad6-3314-40bd-85b7-8e4ede9ffcb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T05:13:04.448Z_

```json
{
  "parentUuid": "470daad6-3314-40bd-85b7-8e4ede9ffcb1",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
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
  "uuid": "c6feec54-45d6-4542-9ec0-d8dab88da495",
  "timestamp": "2026-05-21T05:13:04.448Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T05:13:07.361Z_



I need to read the paper and related project files to provide a thorough review. Let me start by loading the necessary tools and reading the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6feec54-45d6-4542-9ec0-d8dab88da495",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9B31oXoFUtbQjv59Qm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e886eec5-5f46-4418-b5b3-126d53eda9b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQCnpL3dZ9PiuxRdbSCuZ2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7500,
      "cache_read_input_tokens": 8254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7500,
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

_source line 4 · 2026-05-21T05:13:08.164Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Qb4Ptgr6zxG4hQhqaUQ2qB`</summary>

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
  "parentUuid": "e886eec5-5f46-4418-b5b3-126d53eda9b9",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9B31oXoFUtbQjv59Qm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f72a9170-d28d-4590-a092-f1148c7c9031",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQCnpL3dZ9PiuxRdbSCuZ2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7500,
      "cache_read_input_tokens": 8254,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7500
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 8254,
          "cache_creation_input_tokens": 7500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7500,
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

_source line 5 · 2026-05-21T05:13:08.167Z_

<details><summary>↩ Tool result · `toolu_01Qb4Ptgr6zxG4hQhqaUQ2qB`</summary>

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
  "parentUuid": "f72a9170-d28d-4590-a092-f1148c7c9031",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "deab049a-027c-469e-b9f9-e826cde69d58",
  "sourceToolAssistantUUID": "f72a9170-d28d-4590-a092-f1148c7c9031",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T05:13:10.681Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "deab049a-027c-469e-b9f9-e826cde69d58",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9BJpKN7dDdMVGFbfTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e1aa251-ebb0-48bc-a818-e95d13631f35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ac5XUqFgGEkTfi8dkHvGPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 15754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1302,
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

_source line 7 · 2026-05-21T05:13:12.165Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GFuQNdUK6nQ9wXFqiHo4Dy`</summary>

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
  "parentUuid": "6e1aa251-ebb0-48bc-a818-e95d13631f35",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9BJpKN7dDdMVGFbfTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdae0adb-7579-4725-9f02-464247395feb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ac5XUqFgGEkTfi8dkHvGPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 15754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1302,
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

_source line 8 · 2026-05-21T05:13:12.203Z_

<details><summary>↩ Tool result · `toolu_01GFuQNdUK6nQ9wXFqiHo4Dy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\\n\\n## 近期结论\\n- **plan_004_gsm8k_cross_benchmark** (negative): GSM8K 的 temporal DIF (2023 vs 2024) 将展示与 MMLU 类似的 30-40% ETS C%，证明 temporal DIF 现象跨 benchmark 泛化。使用 METABENCH 其他 benchmarks 总分做 external matching（GSM8K 无 subject 分层），预期 baseline FPR 更可控。如果 C% 在同一量级 → DIF 作为 benchmark health diagnostic 的泛化性得到验证。 ← 基于 plan_001_real_data_dif_mmlu\\n- **plan_017_downstream_impact** (negative): 移除 temporal DIF-flagged items (ETS C, ~31% of MMLU items) 后，模型跨代排名更稳定（Spearman ρ 提升），且稳定性提升显著优于随机移除相同数量 items 的 baseline。这证明 DIF 不只标记 noise，而是精确识别了 problematic items，为 DIF 作为 benchmark quality tool 提供 downstream evidence。 ← 基于 plan_001_real_data_dif_mmlu\\n- **plan_016_within_subject_semi_synthetic** (success): 在 subject 内部使用 within-subject total score 做 MH 分层的 semi-synthetic injection 中，DIF 仍能检测差异性污染（ΔTPR > 0.3 at p=0.5）。这证明 DIF 方法在 subject 级别也有效，plan_014 的 38% within-subject C% 反映的是真实代际能力差异而非方法失败。 ← 基于 plan_014_within_subject_dif\\n  [plan_016_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md) | [plan_016_dose_response](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response.csv) | [plan_016_revised_dose_response](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response_e6d86f.csv) | [plan_016_revised_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md)\\n\\n## 趋势\\n成功 5 / 负向 6 / 失败 0 / 共 11\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 2009, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdae0adb-7579-4725-9f02-464247395feb",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "d4af3a91-3aaa-4523-b864-ba8ffbf40100",
  "sourceToolAssistantUUID": "bdae0adb-7579-4725-9f02-464247395feb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T05:13:12.815Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Kxr68wxn2bMw3oMnDEW9WT`</summary>

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
  "parentUuid": "d4af3a91-3aaa-4523-b864-ba8ffbf40100",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9BJpKN7dDdMVGFbfTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "742a223f-0462-4614-8917-d5b6a12c3ad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ac5XUqFgGEkTfi8dkHvGPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 15754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1302,
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

_source line 10 · 2026-05-21T05:13:12.832Z_

<details><summary>↩ Tool result · `toolu_01Kxr68wxn2bMw3oMnDEW9WT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml\", \"content\": \"categories:\\n- key: contamination_detection\\n  name: Benchmark Contamination Detection\\n  narrative: Methods for detecting training data contamination in LLM benchmarks,\\n    including RL-robust approaches\\n- key: irt_equating\\n  name: IRT Methodology & Equating\\n  narrative: Item Response Theory models, calibration, equating, and their application\\n    to LLM evaluation\\n- key: benchmark_design\\n  name: Dynamic Benchmark Design\\n  narrative: Approaches for creating contamination-resistant or self-updating benchmarks\\n- key: dif_methodology\\n  name: DIF Statistical Methods\\n  narrative: Differential Item Functioning detection methods, power analysis, and\\n    small-sample strategies\\n- key: item_generation\\n  name: Automated Item Generation\\n  narrative: LLM-based test item generation with difficulty control and psychometric\\n    validation\\n- key: llm_evaluation\\n  name: LLM Evaluation Methodology\\n  narrative: General LLM evaluation methodology, benchmark psychometric analysis,\\n    evaluation surveys, and benchmark design principles\\nmeta:\\n  last_updated: '2026-05-21T03:50:29.840Z'\\n  total_papers: 45\\npapers:\\n  balloccu2024leak:\\n    abstract: ''\\n    added_at: '2026-05-21T01:40:37.987Z'\\n    added_by: literature-gap-fill\\n    authors:\\n    - Balloccu, S.\\n    - Schmidtova, P.\\n    - Lango, M.\\n    - Dusek, O.\\n    bibtex_key: balloccu2024leak\\n    category: contamination_detection\\n    doi: 10.18653/v1/2024.eacl-long.5\\n    relevance: Systematic survey of data leakage in closed-source LLMs covering 255\\n      papers and 263 benchmarks; establishes scope of contamination problem motivating\\n      our detection approach\\n    role: foundation\\n    semantic_scholar_id: 798feda076ad710df65d509a7884bd15937c8056\\n    title: 'Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in\\n      Closed-Source LLMs'\\n    url: https://arxiv.org/abs/2402.03927\\n    venue: EACL 2024\\n    verified: true\\n    year: 2024\\n  belzak2020smallsample:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Belzak, W.\\n    bibtex_key: belzak2020smallsample\\n    category: dif_methodology\\n    doi: 10.1080/00273171.2019.1671162\\n    relevance: Parsimonious logistic regression with sum scores outperforms complex\\n      IRT models for DIF detection in small samples; directly applicable to our N=50-80\\n      model cohorts\\n    role: method-component\\n    semantic_scholar_id: 8f13882b6f37be1ade68c40539156277e5723395\\n    title: Testing Differential Item Functioning in Small Samples\\n    url: https://www.tandfonline.com/doi/abs/10.1080/00273171.2019.1671162\\n    venue: Multivariate Behavioral Research\\n    verified: true\\n    year: 2020\\n  dekoninck2024constat:\\n    abstract: ''\\n    added_at: '2026-05-21T01:40:37.987Z'\\n    added_by: literature-gap-fill\\n    authors:\\n    - Dekoninck, J.\\n    - Mueller, M. N.\\n    - Vechev, M.\\n    bibtex_key: dekoninck2024constat\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Performance-based contamination detection via perturbation analysis;\\n      closest methodological parallel to our DIF approach in using behavioral patterns\\n      rather than memorization signals\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'ConStat: Performance-Based Contamination Detection in Large Language Models'\\n    url: https://arxiv.org/abs/2405.16281\\n    venue: NeurIPS 2024\\n    verified: true\\n    year: 2024\\n  golchin2024timetravel:\\n    abstract: ''\\n    added_at: '2026-05-21T01:40:37.987Z'\\n    added_by: literature-gap-fill\\n    authors:\\n    - Golchin, S.\\n    - Surdeanu, M.\\n    bibtex_key: golchin2024timetravel\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Instance-level contamination detection via guided completion prompts;\\n      baseline approach for individual-item detection that our group-level DIF method\\n      extends\\n    role: method-component\\n    semantic_scholar_id: d6d0fd994f37b630f35945736b5e1bb198148404\\n    title: 'Time Travel in LLMs: Tracing Data Contamination in Large Language Models'\\n    url: https://arxiv.org/abs/2308.08493\\n    venue: ICLR 2024\\n    verified: true\\n    year: 2024\\n  hardy2026scalability:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Hardy, M.\\n    - Gilbert, J.\\n    - Domingue, B.\\n    bibtex_key: hardy2026scalability\\n    category: irt_equating\\n    doi: 10.48550/arXiv.2603.24999\\n    relevance: Nonparametric signed isotonic R2 scalability coefficients outperform\\n      IRT item diagnostics; lightweight pre-filter for item quality before our parametric\\n      calibration\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients\\n    url: https://arxiv.org/abs/2603.24999\\n    venue: arXiv\\n    verified: true\\n    year: 2026\\n  kim2019fpc:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Kim, S.\\n    - Kolen, M.\\n    bibtex_key: kim2019fpc\\n    category: irt_equating\\n    doi: 10.1080/08957347.2019.1660344\\n    relevance: Fixed-parameter calibration requires only N>=200 vs N>=500 for full\\n      calibration; core methodology for our bifactor IRT equating with anchor items\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data\\n    url: https://www.tandfonline.com/doi/abs/10.1080/08957347.2019.1660344\\n    venue: Applied Measurement in Education\\n    verified: true\\n    year: 2019\\n  li2024contamination:\\n    abstract: ''\\n    added_at: '2026-05-21T01:40:37.987Z'\\n    added_by: literature-gap-fill\\n    authors:\\n    - Li, Y.\\n    - Guo, Y.\\n    - Guerin, F.\\n    - Lin, C.\\n    bibtex_key: li2024contamination\\n    category: contamination_detection\\n    doi: 10.18653/v1/2024.findings-emnlp.30\\n    relevance: Provides web-overlap contamination labels for MMLU and other benchmarks\\n      via Common Crawl matching; primary ground-truth comparison for our DIF-based\\n      contamination detection\\n    role: foundation\\n    semantic_scholar_id: 32e11cf020021c225782a3b77b5cfed4ae8e14a0\\n    title: An Open-Source Data Contamination Report for Large Language Models\\n    url: https://aclanthology.org/2024.findings-emnlp.30/\\n    venue: Findings of EMNLP 2024\\n    verified: true\\n    year: 2024\\n  liang2026dvd:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Liang, R.\\n    bibtex_key: liang2026dvd\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Detects variant contamination via generation variance (AUC 0.73-0.74\\n      vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under\\n      RL training\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'DVD: Detection via Variance of Generation Distribution for Variant Contamination'\\n    url: https://arxiv.org/abs/2601.04895\\n    venue: arXiv\\n    verified: true\\n    year: 2026\\n  shi2024mink:\\n    abstract: ''\\n    added_at: '2026-05-21T01:40:37.987Z'\\n    added_by: literature-gap-fill\\n    authors:\\n    - Shi, W.\\n    - Ajith, A.\\n    - Xia, M.\\n    - Huang, Y.\\n    - Liu, D.\\n    - Blevins, T.\\n    - Chen, D.\\n    - Zettlemoyer, L.\\n    bibtex_key: shi2024mink\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Introduces Min-K% Prob method and WikiMIA benchmark for pretraining\\n      data detection; key baseline whose limitations under RL training motivate our\\n      DIF-based alternative\\n    role: foundation\\n    semantic_scholar_id: 3422d5e0cdfdc935d6a84a1e3d3f96659265fe3a\\n    title: Detecting Pretraining Data from Large Language Models\\n    url: https://arxiv.org/abs/2310.16789\\n    venue: ICLR 2024\\n    verified: true\\n    year: 2024\\n  tao2026selfcritique:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Tao, Y.\\n    bibtex_key: tao2026selfcritique\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse\\n      detection, but remains individual-model-level; our DIF is group-level and complementary\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: Detecting Data Contamination from Reinforcement Learning Post-training\\n      for Large Language Models\\n    url: https://arxiv.org/abs/2510.09259\\n    venue: ICLR 2026\\n    verified: true\\n    year: 2026\\n  wang2026fragility:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Wang, H.\\n    - Li, H.\\n    - Ko, B.\\n    - Zhang, H.\\n    bibtex_key: wang2026fragility\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Proves GRPO/PPO RL training conceals contamination signals (14-20pp\\n      AUROC degradation), motivating our DIF-based approach which operates on behavioral\\n      patterns immune to NLL smoothing\\n    role: foundation\\n    semantic_scholar_id: 9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3\\n    title: On The Fragility of Benchmark Contamination Detection in Reasoning Models\\n    url: https://arxiv.org/abs/2510.02386\\n    venue: ICLR 2026\\n    verified: true\\n    year: 2026\\n  white2025livebench:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - White, C.\\n    bibtex_key: white2025livebench\\n    category: benchmark_design\\n    doi: 10.48550/arXiv.2406.19314\\n    relevance: Monthly-updated contamination-free benchmark with objective scoring;\\n      no difficulty calibration or psychometric equivalence across updates\\n    role: direct-competitor\\n    semantic_scholar_id: 4e5d86ea8eacd341d13123852d50d1ef62738744\\n    title: 'LiveBench: A Challenging, Contamination-Free LLM Benchmark'\\n    url: https://arxiv.org/abs/2406.19314\\n    venue: ICLR 2025\\n    verified: true\\n    year: 2025\\n  zhang2024gsm1k:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Zhang, H.\\n    bibtex_key: zhang2024gsm1k\\n    category: contamination_detection\\n    doi: ''\\n    relevance: GSM1K documents 10-13% average accuracy drops from contamination; provides\\n      ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4\\n      logits) critical for our DIF power analysis\\n    role: foundation\\n    semantic_scholar_id: ef62f95c16f668f031d649799cbd79081c6d2b0f\\n    title: A Careful Examination of Large Language Model Performance on Grade School\\n      Arithmetic\\n    url: https://arxiv.org/abs/2405.00332\\n    venue: arXiv\\n    verified: true\\n    year: 2024\\n  zhang2024minkpp:\\n    abstract: ''\\n    added_at: '2026-05-21T01:40:37.987Z'\\n    added_by: literature-gap-fill\\n    authors:\\n    - Zhang, J.\\n    - Sun, J.\\n    - Yeats, E.\\n    - Ouyang, Y.\\n    - Kuo, M.\\n    - Zhang, J.\\n    - Yang, H.\\n    - Li, H.\\n    bibtex_key: zhang2024minkpp\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Improves Min-K% with vocabulary-normalized token probabilities; key\\n      baseline whose AUC degrades to 0.43-0.68 on RL-trained models, motivating our\\n      DIF-based alternative\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large\\n      Language Models'\\n    url: https://arxiv.org/abs/2404.02936\\n    venue: arXiv\\n    verified: true\\n    year: 2024\\n  lalor2019irt:\\n    title: 'Learning Latent Parameters without Human Response Patterns: Item Response\\n      Theory with Artificial Crowds'\\n    authors:\\n    - Lalor, J.\\n    - Wu, H.\\n    - Yu, H.\\n    year: 2019\\n    venue: EMNLP-IJCNLP 2019\\n    url: https://aclanthology.org/D19-1434/\\n    doi: 10.18653/v1/D19-1434\\n    bibtex_key: lalor2019irt\\n    category: irt_equating\\n    role: foundation\\n    relevance: Pioneering application of IRT to NLP evaluation using artificial crowds\\n      of DNN models; establishes that IRT parameters from machine response patterns\\n      correlate with human-calibrated parameters\\n    abstract: ''\\n    semantic_scholar_id: df6cd8a8d836e75690141deb732f6d19f0176a2e\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T02:29:19.632Z'\\n  vania2021irt:\\n    title: Comparing Test Sets with Item Response Theory\\n    authors:\\n    - Vania, C.\\n    - Htut, P.M.\\n    - Huang, W.\\n    - Mungra, D.\\n    - Pang, R.Y.\\n    - Phang, J.\\n    - Liu, H.\\n    - Cho, K.\\n    - Bowman, S.R.\\n    year: 2021\\n    venue: ACL 2021\\n    url: https://aclanthology.org/2021.acl-long.92/\\n    doi: 10.18653/v1/2021.acl-long.92\\n    bibtex_key: vania2021irt\\n    category: irt_equating\\n    role: foundation\\n    relevance: IRT-based analysis of NLU benchmark discriminability; shows which test\\n      sets remain effective at differentiating strong models and which are saturated\\n    abstract: ''\\n    semantic_scholar_id: 4ca39cf99747b8962fe37e7e025e284872df3425\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T02:29:19.632Z'\\n  li2025atlas:\\n    title: 'Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static\\n      Benchmarks'\\n    authors:\\n    - Li, P.\\n    - Tang, X.\\n    - Chen, S.\\n    - Cheng, Y.\\n    - Metoyer, R.\\n    - Hua, T.\\n    - Chawla, N.V.\\n    year: 2025\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2511.04689\\n    doi: 10.48550/arXiv.2511.04689\\n    bibtex_key: li2025atlas\\n    category: irt_equating\\n    role: method-component\\n    relevance: IRT-based adaptive testing framework (ATLAS) reduces benchmark items\\n      by 90% while preserving ability estimates; demonstrates IRT enables efficient\\n      LLM evaluation\\n    abstract: ''\\n    semantic_scholar_id: 087ce2837a0d5562bc95a40e77a327a6d033366c\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T02:29:19.632Z'\\n  chen2025irtnet:\\n    title: Learning Compact Representations of LLM Abilities via Item Response Theory\\n    authors:\\n    - Chen, J.\\n    - Wang, C.\\n    - Zhang, G.\\n    - Ye, P.\\n    - Bai, L.\\n    - Hu, W.\\n    - Qu, Y.\\n    - Hu, S.\\n    year: 2025\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2510.00844\\n    doi: 10.48550/arXiv.2510.00844\\n    bibtex_key: chen2025irtnet\\n    category: irt_equating\\n    role: method-component\\n    relevance: Multidimensional IRT with MoE network for learning LLM ability vectors\\n      and query discrimination/difficulty; demonstrates IRT-based model routing and\\n      benchmark prediction\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T02:29:19.632Z'\\n  choi2026llmjudgeirt:\\n    title: Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory\\n    authors:\\n    - Choi, J.\\n    - Park, S.\\n    - Cho, C.\\n    - Park, H.\\n    - Kim, B.\\n    year: 2026\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2602.00521\\n    doi: 10.48550/arXiv.2602.00521\\n    bibtex_key: choi2026llmjudgeirt\\n    category: irt_equating\\n    role: method-component\\n    relevance: Applies IRT Graded Response Model to diagnose LLM judge reliability;\\n      extends IRT application beyond benchmark scoring to evaluation pipeline quality\\n      assessment\\n    abstract: ''\\n    semantic_scholar_id: 4fc931a456c8162716deadbc9db6fd770189e632\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T02:29:19.632Z'\\n  holland1988mh:\\n    title: Differential Item Functioning and the Mantel-Haenszel Procedure\\n    authors:\\n    - Holland, P.W.\\n    - Thayer, D.T.\\n    year: 1988\\n    venue: In H. Wainer & H.I. Braun (Eds.), Test Validity, Lawrence Erlbaum\\n    url: https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2330-8516.1986.tb00186.x\\n    doi: 10.1002/j.2330-8516.1986.tb00186.x\\n    bibtex_key: holland1988mh\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Seminal paper introducing the Mantel-Haenszel procedure for DIF detection;\\n      establishes the ETS classification system (A/B/C) used as standard DIF effect-size\\n      metric\\n    abstract: ''\\n    semantic_scholar_id: 5fbc064e7104036b77a2bf6f0ad509031965c275\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  shealy1993sibtest:\\n    title: A Model-Based Standardization Approach that Separates True Bias/DIF from\\n      Group Ability Differences and Detects Test Bias/DTF as Well as Item Bias/DIF\\n    authors:\\n    - Shealy, R.\\n    - Stout, W.\\n    year: 1993\\n    venue: Psychometrika\\n    url: https://link.springer.com/article/10.1007/BF02294572\\n    doi: 10.1007/BF02294572\\n    bibtex_key: shealy1993sibtest\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Introduces SIBTEST, a nonparametric DIF detection method that separates\\n      true item bias from group ability differences; alternative to MH that handles\\n      non-uniform DIF\\n    abstract: ''\\n    semantic_scholar_id: 82f3db496626afd828fedb01a41f719a50dbfc2c\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  clauser1998dif:\\n    title: Using Statistical Procedures to Identify Differentially Functioning Test\\n      Items\\n    authors:\\n    - Clauser, B.E.\\n    - Mazor, K.M.\\n    year: 1998\\n    venue: 'Educational Measurement: Issues and Practice'\\n    url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3992.1998.tb00619.x\\n    doi: 10.1111/j.1745-3992.1998.tb00619.x\\n    bibtex_key: clauser1998dif\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Comprehensive review of DIF detection methods (MH, SIBTEST, logistic\\n      regression, IRT-based); standard reference for comparing statistical approaches\\n      to DIF\\n    abstract: ''\\n    semantic_scholar_id: c2377c505c95b924e972e61dadec81e9c87dea18\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  zumbo1999handbook:\\n    title: 'A Handbook on the Theory and Methods of Differential Item Functioning\\n      (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type\\n      (Ordinal) Item Scores'\\n    authors:\\n    - Zumbo, B.D.\\n    year: 1999\\n    venue: 'Ottawa: Directorate of Human Resources Research and Evaluation, Department\\n      of National Defense'\\n    url: https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf\\n    doi: ''\\n    bibtex_key: zumbo1999handbook\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Foundational DIF handbook presenting logistic regression as a unitary\\n      framework for DIF analysis; establishes the Zumbo-Thomas logistic regression\\n      approach widely used in applied DIF research\\n    abstract: ''\\n    semantic_scholar_id: 7f88fb0ad98645582665532600d7c46406fa2db6\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  meredith1993invariance:\\n    title: Measurement Invariance, Factor Analysis and Factorial Invariance\\n    authors:\\n    - Meredith, W.\\n    year: 1993\\n    venue: Psychometrika\\n    url: https://link.springer.com/article/10.1007/BF02294825\\n    doi: 10.1007/BF02294825\\n    bibtex_key: meredith1993invariance\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Defines the measurement invariance hierarchy (configural, metric, scalar,\\n      strict factorial invariance); theoretical foundation linking DIF to latent variable\\n      fairness\\n    abstract: ''\\n    semantic_scholar_id: 7eb541983de0a39586a699e255563b26e9291340\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  vandenberg2000invariance:\\n    title: 'A Review and Synthesis of the Measurement Invariance Literature: Suggestions,\\n      Practices, and Recommendations for Organizational Research'\\n    authors:\\n    - Vandenberg, R.J.\\n    - Lance, C.E.\\n    year: 2000\\n    venue: Organizational Research Methods\\n    url: https://journals.sagepub.com/doi/10.1177/109442810031002\\n    doi: 10.1177/109442810031002\\n    bibtex_key: vandenberg2000invariance\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Comprehensive review of measurement invariance testing practices; establishes\\n      CFA-based invariance testing as prerequisite for valid cross-group comparisons,\\n      analogous to our cross-model DIF analysis\\n    abstract: ''\\n    semantic_scholar_id: 1c9389250c1fac06eda5dcf39a8ea16cf8c92c89\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  swaminathan1990logistic:\\n    title: Detecting Differential Item Functioning Using Logistic Regression Procedures\\n    authors:\\n    - Swaminathan, H.\\n    - Rogers, H.J.\\n    year: 1990\\n    venue: Journal of Educational Measurement\\n    url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x\\n    doi: 10.1111/j.1745-3984.1990.tb00754.x\\n    bibtex_key: swaminathan1990logistic\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Introduces logistic regression for DIF detection, distinguishing uniform\\n      and non-uniform DIF; more powerful than MH for non-uniform DIF and directly\\n      applicable to our contamination-as-DIF framework\\n    abstract: ''\\n    semantic_scholar_id: d14b3b6e927ff8e51406fad1010244ecabc07da0\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  teresi2007dif:\\n    title: Differential Item Functioning and Health Assessment\\n    authors:\\n    - Teresi, J.A.\\n    - Fleishman, J.A.\\n    year: 2007\\n    venue: Quality of Life Research\\n    url: https://link.springer.com/article/10.1007/s11136-007-9184-6\\n    doi: 10.1007/s11136-007-9184-6\\n    bibtex_key: teresi2007dif\\n    category: dif_methodology\\n    role: method-component\\n    relevance: Reviews DIF detection strategies including propensity score matching\\n      approaches for controlling confounders; methodological basis for our propensity-matched\\n      contamination group comparison\\n    abstract: ''\\n    semantic_scholar_id: 5ddbe080c2c0cdff671d9b9c2a795e366b6eb098\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  lord1980irt:\\n    title: Applications of Item Response Theory to Practical Testing Problems\\n    authors:\\n    - Lord, F.M.\\n    year: 1980\\n    venue: 'Hillsdale, NJ: Lawrence Erlbaum Associates'\\n    url: https://www.routledge.com/Applications-of-Item-Response-Theory-To-Practical-Testing-Problems/Lord/p/book/9780898590067\\n    doi: ''\\n    bibtex_key: lord1980irt\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Introduces Lord's chi-square test for IRT-based DIF detection by comparing\\n      item parameters across groups; foundational IRT reference for our parametric\\n      DIF approach\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  raju1988area:\\n    title: The Area between Two Item Characteristic Curves\\n    authors:\\n    - Raju, N.S.\\n    year: 1988\\n    venue: Psychometrika\\n    url: https://link.springer.com/article/10.1007/BF02294403\\n    doi: 10.1007/BF02294403\\n    bibtex_key: raju1988area\\n    category: dif_methodology\\n    role: method-component\\n    relevance: Develops signed and unsigned area measures between item characteristic\\n      curves for IRT-based DIF quantification; provides effect-size metrics complementing\\n      statistical significance tests\\n    abstract: ''\\n    semantic_scholar_id: 545c20c1f2575833f81418f4757cb78446465cd7\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  muthen1985mimic:\\n    title: A Method for Studying the Homogeneity of Test Items with Respect to Other\\n      Relevant Variables\\n    authors:\\n    - Muthén, B.\\n    year: 1985\\n    venue: Journal of Educational Statistics\\n    url: ''\\n    doi: 10.2307/1164966\\n    bibtex_key: muthen1985mimic\\n    category: dif_methodology\\n    role: method-component\\n    relevance: Seminal MIMIC model for DIF with continuous covariates; future-work\\n      alternative to failed θ-conditioning (plan_012)\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper_agent\\n    added_at: '2026-05-21T03:34:08.189Z'\\n  woods2009mimic:\\n    title: Empirical Selection of Anchors for Tests of Differential Item Functioning\\n    authors:\\n    - Woods, C.M.\\n    year: 2009\\n    venue: Applied Psychological Measurement\\n    url: ''\\n    doi: 10.1177/0146621609331279\\n    bibtex_key: woods2009mimic\\n    category: dif_methodology\\n    role: method-component\\n    relevance: Modern MIMIC-based DIF detection with anchor selection; addresses impact-vs-DIF\\n      confound in our future work\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper_agent\\n    added_at: '2026-05-21T03:34:08.189Z'\\n  habba2026growingpains:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Habba, E.\\n    - Itzhak, I.\\n    - Yehudai, A.\\n    - Perlitz, Y.\\n    - Bandel, E.\\n    - Shmueli-Scheuer, M.\\n    - Choshen, L.\\n    - Stanovsky, G.\\n    bibtex_key: habba2026growingpains\\n    category: irt_equating\\n    doi: 10.48550/arXiv.2604.12843\\n    relevance: Uses multidimensional IRT with fixed-parameter calibration and 100\\n      anchor items for extensible evaluation (rho>=0.9); addresses score comparability\\n      but NOT contamination detection or item regeneration\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter\\n      Calibration'\\n    url: https://arxiv.org/abs/2604.12843\\n    venue: arXiv\\n    verified: true\\n    year: 2026\\n  zhou2026psnirt:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Zhou, H.\\n    - Huang, H.\\n    - Zhao, Z.\\n    - Han, L.\\n    - Wang, H.\\n    - Chen, K.\\n    - Yang, M.\\n    - Bao, W.\\n    - Dong, J.\\n    - Xu, B.\\n    - Zhu, C.\\n    - Cao, H.\\n    - Zhao, T.\\n    bibtex_key: zhou2026psnirt\\n    category: irt_equating\\n    doi: ''\\n    relevance: PSN-IRT analyzes benchmark quality via 4PL IRT; provides published\\n      IRT parameters for MMLU we can use in semi-synthetic validation\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item\\n      Response Theory\\n    url: https://arxiv.org/abs/2505.15055\\n    venue: AAAI 2026\\n    verified: true\\n    year: 2026\\n  kipnis2024metabench:\\n    title: metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language\\n      Models\\n    authors:\\n    - Kipnis, A.\\n    - Voudouris, K.\\n    - Schulze Buschoff, L.M.\\n    - Schulz, E.\\n    year: 2024\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2407.12844\\n    doi: 10.48550/arXiv.2407.12844\\n    bibtex_key: kipnis2024metabench\\n    category: benchmark_design\\n    role: foundation\\n    relevance: Primary data source providing item-level response matrix across 5000+\\n      LLMs on 6 benchmarks; IRT-based item selection methodology enables our DIF analysis\\n      on compressed benchmark items\\n    abstract: ''\\n    semantic_scholar_id: dfd5186def202285a0f23cd3f08415a5780895c1\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:43:39.896Z'\\n  hendrycks2021mmlu:\\n    title: Measuring Massive Multitask Language Understanding\\n    authors:\\n    - Hendrycks, D.\\n    - Burns, C.\\n    - Basart, S.\\n    - Zou, A.\\n    - Mazeika, M.\\n    - Song, D.\\n    - Steinhardt, J.\\n    year: 2021\\n    venue: ICLR 2021\\n    url: https://arxiv.org/abs/2009.03300\\n    doi: ''\\n    bibtex_key: hendrycks2021mmlu\\n    category: benchmark_design\\n    role: foundation\\n    relevance: Seminal 57-subject benchmark for LLM evaluation; primary benchmark\\n      in our DIF analysis due to documented contamination and available IRT parameters\\n    abstract: ''\\n    semantic_scholar_id: 814a4f680b9ba6baba23b93499f4b48af1a27678\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:43:39.896Z'\\n  liang2023helm:\\n    title: Holistic Evaluation of Language Models\\n    authors:\\n    - Liang, P.\\n    - Bommasani, R.\\n    - Lee, T.\\n    - Tsipras, D.\\n    - Soylu, D.\\n    - Yasunaga, M.\\n    - Zhang, Y.\\n    - Narayanan, D.\\n    - Wu, Y.\\n    - Kumar, A.\\n    year: 2023\\n    venue: TMLR 2023\\n    url: https://arxiv.org/abs/2211.09110\\n    doi: 10.1111/nyas.15007\\n    bibtex_key: liang2023helm\\n    category: benchmark_design\\n    role: foundation\\n    relevance: Holistic multi-metric evaluation framework covering accuracy, calibration,\\n      robustness, fairness, and bias; establishes multi-dimensional evaluation philosophy\\n      complementary to our psychometric approach\\n    abstract: ''\\n    semantic_scholar_id: ce913026f693101e54d3ab9152e107034d81fce1\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:43:39.896Z'\\n  chiang2024chatbot:\\n    title: 'Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference'\\n    authors:\\n    - Chiang, W.-L.\\n    - Zheng, L.\\n    - Sheng, Y.\\n    - Angelopoulos, A.N.\\n    - Li, T.\\n    - Li, D.\\n    - Zhang, H.\\n    - Zhu, B.\\n    - Jordan, M.I.\\n    - Gonzalez, J.E.\\n    - Stoica, I.\\n    year: 2024\\n    venue: ICML 2024\\n    url: https://arxiv.org/abs/2403.04132\\n    doi: 10.48550/arXiv.2403.04132\\n    bibtex_key: chiang2024chatbot\\n    category: benchmark_design\\n    role: method-component\\n    relevance: Crowdsourced pairwise comparison with ELO ranking as contamination-resistant\\n      alternative to static benchmarks; contrasts with our item-level psychometric\\n      approach\\n    abstract: ''\\n    semantic_scholar_id: 53f4fb0e9972989194368faf288ff8e3cba5bd60\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:43:39.896Z'\\n  mialon2023gaia:\\n    title: 'GAIA: a benchmark for General AI Assistants'\\n    authors:\\n    - Mialon, G.\\n    - Fourrier, C.\\n    - Swift, C.\\n    - Wolf, T.\\n    - LeCun, Y.\\n    - Scialom, T.\\n    year: 2023\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2311.12983\\n    doi: 10.48550/arXiv.2311.12983\\n    bibtex_key: mialon2023gaia\\n    category: benchmark_design\\n    role: method-component\\n    relevance: Benchmark with verifiable ground-truth answers designed to resist memorization;\\n      exemplifies objective-scoring benchmark design philosophy shared by our regenerated\\n      items\\n    abstract: ''\\n    semantic_scholar_id: ab8169d6e4dfabfe7c30ebec1bb871bf3e1551cd\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:43:39.896Z'\\n  li2024latesteval:\\n    title: 'LatestEval: Addressing Data Contamination in Language Model Evaluation\\n      through Dynamic and Time-Sensitive Test Construction'\\n    authors:\\n    - Li, Y.\\n    - Guerin, F.\\n    - Lin, C.\\n    year: 2024\\n    venue: AAAI 2024\\n    url: https://arxiv.org/abs/2312.12343\\n    doi: 10.48550/arXiv.2312.12343\\n    bibtex_key: li2024latesteval\\n    category: benchmark_design\\n    role: direct-competitor\\n    relevance: Automated dynamic test construction from recent texts to avoid contamination;\\n      addresses temporal contamination but lacks psychometric difficulty calibration\\n      across test versions\\n    abstract: ''\\n    semantic_scholar_id: 8106d03fb984afd8c3d066cd4f993eb2616a0da5\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:43:39.896Z'\\n  kiela2021dynabench:\\n    title: 'Dynabench: Rethinking Benchmarking in NLP'\\n    authors:\\n    - Kiela, D.\\n    - Bartolo, M.\\n    - Nie, Y.\\n    - Kaushik, D.\\n    - Geiger, A.\\n    - Wu, Z.\\n    - Vidgen, B.\\n    - Prasad, G.\\n    - Singh, A.\\n    - Ringshia, P.\\n    - Ma, Z.\\n    - Thrush, T.\\n    - Riedel, S.\\n    - Talat, Z.\\n    - Stenetorp, P.\\n    - Jia, R.\\n    year: 2021\\n    venue: NAACL 2021\\n    url: https://arxiv.org/abs/2104.14337\\n    doi: 10.18653/v1/2021.naacl-main.324\\n    bibtex_key: kiela2021dynabench\\n    category: benchmark_design\\n    role: foundation\\n    relevance: Seminal dynamic adversarial benchmarking platform with human-and-model-in-the-loop\\n      dataset creation; establishes the paradigm of continuously evolving benchmarks\\n      that our IRT-equated regeneration extends with psychometric equivalence guarantees\\n    abstract: ''\\n    semantic_scholar_id: 77a096d80eb4dd4ccd103d1660c5a5498f7d026b\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:43:39.896Z'\\n  burnell2023rethink:\\n    title: Rethink reporting of evaluation results in AI\\n    authors:\\n    - Burnell, R.\\n    - Schellaert, W.\\n    - Burden, J.\\n    - Ullman, T.D.\\n    - Martinez-Plumed, F.\\n    - Tenenbaum, J.B.\\n    - Rutar, D.\\n    - Cheke, L.G.\\n    - Sohl-Dickstein, J.\\n    - Mitchell, M.\\n    - Kiela, D.\\n    - Shanahan, M.\\n    - Voorhees, E.M.\\n    - Cohn, A.G.\\n    - Leibo, J.Z.\\n    - Hernandez-Orallo, J.\\n    year: 2023\\n    venue: Science\\n    url: https://www.science.org/doi/10.1126/science.adf6369\\n    doi: 10.1126/science.adf6369\\n    bibtex_key: burnell2023rethink\\n    category: llm_evaluation\\n    role: background\\n    relevance: Argues that aggregate metrics and lack of item-level transparency in\\n      AI evaluation limit understanding of model capabilities; motivates psychometric\\n      item-level analysis\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper_agent\\n    added_at: '2026-05-21T03:50:29.780Z'\\n  chang2024survey:\\n    title: A Survey on Evaluation of Large Language Models\\n    authors:\\n    - Chang, Y.\\n    - Wang, X.\\n    - Wang, J.\\n    - Wu, Y.\\n    - Zhu, K.\\n    - Chen, H.\\n    - Yang, L.\\n    - Yi, X.\\n    - Wang, C.\\n    - Wang, Y.\\n    - Ye, W.\\n    - Zhang, Y.\\n    - Chang, Y.\\n    - Yu, P.S.\\n    - Yang, Q.\\n    - Xie, X.\\n    year: 2024\\n    venue: ACM Transactions on Intelligent Systems and Technology\\n    url: https://dl.acm.org/doi/full/10.1145/3641289\\n    doi: 10.1145/3641289\\n    bibtex_key: chang2024survey\\n    category: llm_evaluation\\n    role: background\\n    relevance: Comprehensive survey covering what/where/how to evaluate LLMs across\\n      tasks and societal dimensions; provides landscape context for our psychometric\\n      evaluation approach\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper_agent\\n    added_at: '2026-05-21T03:50:29.780Z'\\n  maiapolo2024tinybenchmarks:\\n    title: 'tinyBenchmarks: evaluating LLMs with fewer examples'\\n    authors:\\n    - Maia Polo, F.\\n    - Weber, L.\\n    - Choshen, L.\\n    - Sun, Y.\\n    - Xu, G.\\n    - Yurochkin, M.\\n    year: 2024\\n    venue: ICML 2024\\n    url: https://proceedings.mlr.press/v235/maia-polo24a.html\\n    doi: ''\\n    bibtex_key: maiapolo2024tinybenchmarks\\n    category: llm_evaluation\\n    role: direct-competitor\\n    relevance: Uses IRT to select representative benchmark subsets for efficient LLM\\n      evaluation with 100 items approximating full MMLU; directly related to our IRT-based\\n      equating methodology\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper_agent\\n    added_at: '2026-05-21T03:50:29.780Z'\\n  wang2024mmlupro:\\n    title: 'MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding\\n      Benchmark'\\n    authors:\\n    - Wang, Y.\\n    - Ma, X.\\n    - Zhang, G.\\n    - Ni, Y.\\n    - Chandra, A.\\n    - Guo, S.\\n    - Ren, W.\\n    - Arulraj, A.\\n    - He, X.\\n    - Jiang, Z.\\n    - Li, T.\\n    - Ku, M.\\n    - Wang, K.\\n    - Zhuang, A.\\n    - Fan, R.\\n    - Xue, X.\\n    - Chen, W.\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: https://arxiv.org/abs/2406.01574\\n    doi: ''\\n    bibtex_key: wang2024mmlupro\\n    category: llm_evaluation\\n    role: evaluation\\n    relevance: Extends MMLU with harder reasoning items and 10-option format causing\\n      16-33% accuracy drop; demonstrates benchmark evolution that motivates psychometric\\n      equating across versions\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper_agent\\n    added_at: '2026-05-21T03:50:29.780Z'\\n  ott2022benchmark:\\n    title: Mapping global dynamics of benchmark creation and saturation in artificial\\n      intelligence\\n    authors:\\n    - Ott, S.\\n    - Barbosa-Silva, A.\\n    - Blagec, K.\\n    - Brauner, J.\\n    - Samwald, M.\\n    year: 2022\\n    venue: Nature Communications\\n    url: https://www.nature.com/articles/s41467-022-34591-0\\n    doi: 10.1038/s41467-022-34591-0\\n    bibtex_key: ott2022benchmark\\n    category: llm_evaluation\\n    role: background\\n    relevance: Large-scale analysis of 3765 AI benchmarks showing rapid saturation\\n      dynamics; supports our argument that static benchmarks need psychometric equating\\n      and regeneration\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper_agent\\n    added_at: '2026-05-21T03:50:29.780Z'\\n\", \"total_chars\": 36146, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "742a223f-0462-4614-8917-d5b6a12c3ad1",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "f12b618f-6331-4387-88e3-0138c3201c8c",
  "sourceToolAssistantUUID": "742a223f-0462-4614-8917-d5b6a12c3ad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T05:13:13.488Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018wzwXPiht4vEZGdEiycNdr`</summary>

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
  "parentUuid": "f12b618f-6331-4387-88e3-0138c3201c8c",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9BJpKN7dDdMVGFbfTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "675d89fa-0cdf-4cdf-b92e-a7b1622f684c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ac5XUqFgGEkTfi8dkHvGPn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 15754,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1302
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 15754,
          "cache_creation_input_tokens": 1302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1302,
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

_source line 12 · 2026-05-21T05:13:13.509Z_

<details><summary>↩ Tool result · `toolu_018wzwXPiht4vEZGdEiycNdr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md\", \"content\": \"# Paper Framing — irt_equated_bench_regen\\n\\n## Target Venue\\n- Primary: ICLR 2027 (expected deadline ~October 2026)\\n\\n## Paper Type\\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \\\"DIF reveals benchmark structural problems,\\\" not \\\"DIF detects contamination.\\\"\\n\\n## Core Claims (4 条, 可证伪)\\n\\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement)\\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\\n\\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\\n- Framing: aggressive — \\\"the field's standard validation approach is fundamentally mismatched for item-level detection\\\"\\n\\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\\n\\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \\\"items that changed across generations,\\\" not \\\"good items.\\\"\\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \\\"find bad items and remove\\\" but \\\"understand what changed and why.\\\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\\n4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% BCa CI [−0.714, −0.155]; Spearman ρ=−0.403, p=0.020, CI [−0.687, −0.031]; partial r=−0.385 controlling GSM8K accuracy, p=0.030, CI [−0.640, −0.058]; permutation p=0.014). All CIs exclude zero. Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.\\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33)\\n- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.\\n- Growing Pains互补: \\\"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\\\"\\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\\n\\n## Story Spine (v2 — no-pivot narrative)\\n\\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \\\"Model B outperforms Model A on MMLU,\\\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\\n\\n**Key narrative principle**: \\\"Instability ≠ invalidity.\\\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\\n\\n**What we find** (4 contributions, focused):\\n\\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \\\"models got better.\\\"\\n\\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\\n\\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\\n\\n4. **DIF as diagnostic lens**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. Cross-benchmark: DIF items resist contamination-based gains (r=−0.478, BCa CI [−0.71, −0.16]).\\n\\n**Headline result**: \\\"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF items resist contamination-based gains (r=−0.478) and serve as a diagnostic lens for understanding what changed across model generations.\\\"\\n\\n## Scope Control (main body vs appendix)\\n\\n**MAIN BODY (4 claims + robustness)**:\\n- §1 Introduction (problem + \\\"instability ≠ invalidity\\\" framing upfront)\\n- §2 Related Work (45 papers, 5 clusters)\\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\\n- §5 Discussion + Limitations\\n- §6 Conclusion\\n\\n**APPENDIX (pruned from main body)**:\\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\\n- RL robustness (plan_002) — N=13, underpowered\\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\\n- Bifactor equating pilot — below target fit\\n- Item generation pilot — below benchmarks\\n- Graceful degradation — clean but supplementary\\n- Item-Focused Trees — robustness check, supplementary\\n- ConStat/DVD comparisons — complementary baselines\\n\\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\\n\\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\\n\\n## Venue Fit\\n\\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\\n\\n## Novelty Articulation (三层，显式化)\\n\\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\\n\\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\\n\\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\\n\\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\\n\\n**Framing**: \\\"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\\\"\\n\\n## Anticipated Reviewer Concerns (updated for pivot)\\n\\n1. **\\\"38% could just mean models got better\\\"** — ✅ RESOLVED (plan_019). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%). Subject-level ρ=0.307 is an ecological correlation that grossly overstates the item-level relationship (pseudo R²=0.0007). The instability is predominantly item-specific. Present Model 1 (2.4pp) as primary; acknowledge confounder-vs-mediator ambiguity in Model 2 as honest discussion.\\n\\n2. **\\\"Ground truth critique is obvious — of course web labels don't capture differential effects\\\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\\n\\n3. **\\\"Semi-synthetic injection is artificial\\\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\\n\\n4. **\\\"DIF power is only sufficient for large effects\\\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\\n\\n5. **\\\"Only validated on MMLU\\\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\\n\\n6. **\\\"Higher methods (MIMIC, propensity-score) could solve the confounding\\\"** — Acknowledged as future work. We frame our three-attempt negative results as \\\"empirical observation\\\" that motivates these directions, not as impossibility.\\n\\n7. **\\\"ETS threshold is uncalibrated for LLM populations\\\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \\\"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\\\" Do NOT claim \\\">15% at all thresholds\\\" — be honest that 2.5 drops below.\\n\\n8. **\\\"Multiple testing: 12,508 simultaneous tests without correction\\\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\\n\\n9. **\\\"Only uniform DIF — non-uniform DIF plausible for LLMs\\\"** — Apply SIBTEST or logistic regression DIF to 5-10 representative subjects as robustness check. Show MH results are not missing substantial non-uniform DIF.\\n\\n10. **\\\"Ranking disruption result is tautological\\\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\\n\\n## Dropped from Original Framing\\n\\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\\n- **Detection as primary contribution**: Pivoted from \\\"we detect contamination\\\" to \\\"we characterize benchmark properties.\\\"\\n\", \"total_chars\": 17540, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "675d89fa-0cdf-4cdf-b92e-a7b1622f684c",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "13fb101d-c8ae-4fa1-b08a-935026752afb",
  "sourceToolAssistantUUID": "675d89fa-0cdf-4cdf-b92e-a7b1622f684c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-21T05:13:16.357Z_

Now let me read the actual paper manuscript and any additional artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13fb101d-c8ae-4fa1-b08a-935026752afb",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9BhnSTmK387HhntQfY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b4337ec-3265-4d31-bf2e-9dbd823b6482",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2DtgzvUrJazbYxazouXkZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20697,
      "cache_read_input_tokens": 17056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20697,
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

_source line 14 · 2026-05-21T05:13:18.783Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CbwrRU5THWSKZmSm8oAPtA`</summary>

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
  "parentUuid": "2b4337ec-3265-4d31-bf2e-9dbd823b6482",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9BhnSTmK387HhntQfY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd3cf05f-794d-40e7-a0f2-fc2eb8971de0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2DtgzvUrJazbYxazouXkZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20697,
      "cache_read_input_tokens": 17056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20697,
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

_source line 15 · 2026-05-21T05:13:18.805Z_

<details><summary>↩ Tool result · `toolu_01CbwrRU5THWSKZmSm8oAPtA`</summary>

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
artifacts/dream_reports/dream_20260521T032826/best/paper.tex
artifacts/dream_reports/dream_20260521T032826/worst/paper.tex
paper/math_commands.tex
paper/main.tex
artifacts/_project/paper/experiments.tex
paper/sections/experiments.tex
paper/sections/appendix.tex
paper/sections/abstract.tex
paper/sections/conclusion.tex
docs/paper/introduction.tex
paper/sections/introduction.tex
paper/sections/related_work.tex
paper/sections/method.tex
artifacts/dream_reports/dream_20260521T042647/best/paper.tex
paper/sections/discussion.tex
artifacts/dream_reports/dream_20260521T042647/median/paper.tex
artifacts/dream_reports/dream_20260521T042647/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd3cf05f-794d-40e7-a0f2-fc2eb8971de0",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "ac34000b-ec94-44d7-bfd5-2152e7762048",
  "sourceToolAssistantUUID": "cd3cf05f-794d-40e7-a0f2-fc2eb8971de0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T05:13:19.719Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YFDdtdKw5ULBU8Hx7ifKsX`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac34000b-ec94-44d7-bfd5-2152e7762048",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9BhnSTmK387HhntQfY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da61b78f-e346-4c5a-b024-6adb3ee02842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2DtgzvUrJazbYxazouXkZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20697,
      "cache_read_input_tokens": 17056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20697,
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

_source line 17 · 2026-05-21T05:13:19.730Z_

<details><summary>↩ Tool result · `toolu_01YFDdtdKw5ULBU8Hx7ifKsX`</summary>

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
artifacts/dream_reports/dream_20260520T194223/best/paper.pdf
artifacts/dream_reports/dream_20260520T194223/median/paper.pdf
artifacts/dream_reports/dream_20260520T194223/worst/paper.pdf
artifacts/dream_reports/dream_20260520T205007/best/paper.pdf
artifacts/dream_reports/dream_20260520T205007/median/paper.pdf
artifacts/dream_reports/dream_20260520T205007/worst/paper.pdf
figures/paper/fig_2_dose_response.pdf
artifacts/_project/chart/fig_2_dose_response.pdf
figures/paper/fig_3_within_subject_matching.pdf
artifacts/_project/chart/fig_3_within_subject_matching.pdf
figures/paper/fig_A1_subject_heatmap.pdf
artifacts/_project/chart/fig_A1_subject_heatmap.pdf
figures/paper/fig_A2_q3_distribution.pdf
artifacts/_project/chart/fig_A2_q3_distribution.pdf
figures/paper/fig_4_downstream_impact.pdf
artifacts/_project/chart/fig_4_downstream_impact.pdf
artifacts/_project/chart/fig_gsm1k_dif_correlation.pdf
artifacts/plan_004/fig_gsm1k_dif_correlation.pdf
artifacts/_project/chart/fig_1_global_vs_differential.pdf
figures/paper/fig_1_global_vs_differential.pdf
figures/paper/fig_5_gsm1k_dif_correlation.pdf
artifacts/_project/chart/fig_5_gsm1k_dif_correlation.pdf
artifacts/dream_reports/dream_20260521T012912/best/paper.pdf
artifacts/dream_reports/dream_20260521T012912/median/paper.pdf
artifacts/dream_reports/dream_20260521T012912/worst/paper.pdf
artifacts/dream_reports/dream_20260521T032826/best/paper.pdf
artifacts/dream_reports/dream_20260521T032826/worst/paper.pdf
paper/main.pdf
artifacts/dream_reports/dream_20260521T042647/best/paper.pdf
artifacts/dream_reports/dream_20260521T042647/median/paper.pdf
artifacts/dream_reports/dream_20260521T042647/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da61b78f-e346-4c5a-b024-6adb3ee02842",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "f8e65a2f-3521-4b20-a1b1-e95b6d51ee89",
  "sourceToolAssistantUUID": "da61b78f-e346-4c5a-b024-6adb3ee02842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T05:13:20.409Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01R5mYQ5CLBuc4rXZRC8dT7s`</summary>

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
  "parentUuid": "f8e65a2f-3521-4b20-a1b1-e95b6d51ee89",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9BhnSTmK387HhntQfY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bc85bcc-beae-4de7-b5db-aef02599b628",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2DtgzvUrJazbYxazouXkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20697,
      "cache_read_input_tokens": 17056,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20697
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 295,
          "cache_read_input_tokens": 17056,
          "cache_creation_input_tokens": 20697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20697,
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

_source line 19 · 2026-05-21T05:13:20.417Z_

<details><summary>↩ Tool result · `toolu_01R5mYQ5CLBuc4rXZRC8dT7s`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bc85bcc-beae-4de7-b5db-aef02599b628",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "b6b6cb33-d258-4359-86c9-d8d623c09577",
  "sourceToolAssistantUUID": "9bc85bcc-beae-4de7-b5db-aef02599b628",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-21T05:13:23.433Z_

Let me read the main paper sections systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6b6cb33-d258-4359-86c9-d8d623c09577",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9CEBnX2XZbQfQRb9My",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16589353-d8e8-4a96-a219-acdc49622ebc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNroELKMh1CFNNAoqbfDdb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1564,
      "cache_read_input_tokens": 37753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1564,
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

_source line 21 · 2026-05-21T05:13:23.974Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MNPab9a5v3snZvetAepQV5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16589353-d8e8-4a96-a219-acdc49622ebc",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9CEBnX2XZbQfQRb9My",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a7ff4cb-461f-4290-81d5-e7d835255a86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNroELKMh1CFNNAoqbfDdb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1564,
      "cache_read_input_tokens": 37753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1564,
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

_source line 22 · 2026-05-21T05:13:23.979Z_

<details><summary>↩ Tool result · `toolu_01MNPab9a5v3snZvetAepQV5`</summary>

```text
1	\documentclass{article}
2	\usepackage{iclr2026_conference,times}
3	\input{math_commands.tex}
4	
5	\usepackage{hyperref}
6	\usepackage{url}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{microtype}
11	\usepackage{multirow}
12	\usepackage{subcaption}
13	\usepackage{cleveref}
14	
15	\graphicspath{{../figures/paper/}}
16	
17	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
18	
19	%\iclrfinalcopy
20	
21	\newcommand{\fix}{\marginpar{FIX}}
22	\newcommand{\new}{\marginpar{NEW}}
23	
24	\begin{document}
25	
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\bibliography{references}
37	\bibliographystyle{iclr2026_conference}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a7ff4cb-461f-4290-81d5-e7d835255a86",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "ec8d0f08-6e4e-4026-a9a8-38000f019573",
  "sourceToolAssistantUUID": "9a7ff4cb-461f-4290-81d5-e7d835255a86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T05:13:24.867Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C1pfedNHSRoHPdNJFYSJbG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec8d0f08-6e4e-4026-a9a8-38000f019573",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9CEBnX2XZbQfQRb9My",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46c381ae-7cb0-423f-b770-bb26830c5678",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNroELKMh1CFNNAoqbfDdb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1564,
      "cache_read_input_tokens": 37753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1564,
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

_source line 24 · 2026-05-21T05:13:24.884Z_

<details><summary>↩ Tool result · `toolu_01C1pfedNHSRoHPdNJFYSJbG`</summary>

```text
1	% Placeholder for abstract
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46c381ae-7cb0-423f-b770-bb26830c5678",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "206cbdb9-2af3-430a-9cb1-9f585e501e50",
  "sourceToolAssistantUUID": "46c381ae-7cb0-423f-b770-bb26830c5678",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T05:13:24.998Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LsPx6kWNVmJ2DNUxUViVuq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "206cbdb9-2af3-430a-9cb1-9f585e501e50",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9CEBnX2XZbQfQRb9My",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aee40d27-b587-4e6e-830e-545242d62ac0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNroELKMh1CFNNAoqbfDdb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1564,
      "cache_read_input_tokens": 37753,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1564
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 37753,
          "cache_creation_input_tokens": 1564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1564,
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

_source line 26 · 2026-05-21T05:13:25.007Z_

<details><summary>↩ Tool result · `toolu_01LsPx6kWNVmJ2DNUxUViVuq`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. Applying Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench}, we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. The instability persists within every MMLU subject domain, with domain-level C\% ranging from 31\% to 45\% (mean 38.1\%), and item-level regression shows that 92.4\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{liang2026dvd}, and Self-Critique~\citep{tao2026selfcritique}. These methods validate detection accuracy primarily against web-overlap labels such as those of \citet{li2024contamination}, which classify benchmark items as contaminated based on verbatim or near-verbatim matches in publicly accessible training corpora. Such labels measure \emph{global exposure}: whether an item exists in the data ecosystem that all training pipelines can access. They do not measure \emph{differential item functioning}: whether an item behaves differently across model cohorts that may have had varying degrees of exposure or different training methodologies. \Cref{fig:global_vs_differential} illustrates the distinction. Most MMLU items are globally contaminated in the sense that they exist in web-accessible text, so all model cohorts encounter them and no differential signal arises. The items that function differentially are those where exposure or training methodology changed asymmetrically across cohorts. Validating differential detectors against global-exposure labels therefore conflates two phenomena, and the near-chance enrichment (0.96) between DIF flags and web-overlap labels is the expected outcome of this mismatch.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{fig_1_global_vs_differential.pdf}
11	\caption{Global vs.\ differential contamination, illustrated via Item Characteristic Curves (ICCs). \textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts because only that cohort was disproportionately exposed during training. The enrichment ratio of $\approx 1.0$ between DIF flags and web-overlap labels is expected because most MMLU items fall into the left category.}
12	\label{fig:global_vs_differential}
13	\end{figure}
14	
15	We apply classical MH-DIF with ETS classification to the full METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date. This psychometric approach complements concurrent work on anchor-item calibration for score comparability~\citep{habba2026growingpains} and addresses the fragility of existing contamination detectors under post-training perturbation~\citep{wang2026fragility}. Semi-synthetic injection experiments confirm that DIF detects differential contamination when present ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$), and our cross-subject matching protocol eliminates false positive inflation ($\Delta\mathrm{FPR} = 0.000$). Three structural controls (matched-ability quintile analysis, IRT $\theta$-conditioning, and within-subject pre-checks) confirm that the 31\% temporal instability cannot be attributed to methodological artifacts, establishing it as a robust empirical finding about MMLU's measurement properties.
16	
17	MMLU's 12,508 items provide sufficient measurement redundancy that removing nearly a third does not alter rank order. DIF should therefore be understood as a diagnostic lens (which items changed and for which model families) rather than a quality filter (remove bad items to improve the benchmark). Despite aggregate ranking stability, DIF-flagged items concentrate discriminative signal that differentiates model generations: removing DIF items degrades ranking discriminability more than removing an equal number of random items ($z = -8$ to $-49\sigma$ across 21 conditions). Individual model families show distinctive DIF profiles: Phi-3 and Llama-3 gain ${+}700$ to ${+}850$ rank positions under stable-item evaluation, while Mistral-based merges lose $-400$ to $-587$ positions.
18	
19	We do not modify the MH-DIF procedure itself; the contributions are empirical, not algorithmic. Three layers of genuine novelty emerge: (a)~we discover that 31\% temporal instability is robust across thresholds and unrelated to capability improvement, the first large-scale characterization of item-level benchmark stability at 5,227 models; (b)~we expose a fundamental validation methodology gap in the contamination detection literature, showing that web-overlap labels cannot serve as ground truth for item-level differential detectors; and (c)~we provide a reusable semi-synthetic validation framework with cross-subject matching ($\Delta\mathrm{FPR} = 0.000$), confirmed on GSM8K with independent contamination validation through the GSM1K held-out set~\citep{zhang2024gsm1k}. We make the following contributions:
20	
21	\begin{enumerate}
22	\item \textbf{Benchmark temporal comparability} (Claim 1): 31\% of MMLU items are functionally unstable across model generations under ETS~C classification, with the instability persisting within every subject domain (mean C\% $= 38.1\%$) and confirmed non-random by random-split control at 0.18\% (\Cref{sec:temporal}).
23	
24	\item \textbf{Ground truth meta-critique} (Claim 2): Web-overlap contamination labels~\citep{li2024contamination} cannot evaluate item-level differential detectors. The enrichment between DIF flags and web-overlap labels is 0.96 (chance level), exposing a validation methodology gap in the contamination detection literature (\Cref{sec:groundtruth}).
25	
26	\item \textbf{Semi-synthetic validation framework} (Claim 3): Controlled injection with cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$); cross-benchmark replication on GSM8K confirms generality (\Cref{sec:semisynthetic,sec:gsm8k}).
27	
28	\item \textbf{DIF as diagnostic lens} (Claim 4): DIF-flagged items concentrate discriminative information ($z = -8$ to $-49\sigma$ vs.\ random removal) and anti-correlate with the GSM1K contamination gap ($r = -0.478$, suggestive at $N = 33$), indicating that DIF captures item-level behavioral change distinct from simple memorization (\Cref{sec:downstream,sec:gsm8k}).
29	\end{enumerate}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aee40d27-b587-4e6e-830e-545242d62ac0",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "55cdc738-5dd0-4acc-b68b-053931d17a2e",
  "sourceToolAssistantUUID": "aee40d27-b587-4e6e-830e-545242d62ac0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T05:13:29.050Z_

<details open><summary>🔧 Tool call — Read · `toolu_013cy53KQ9CUKZsQ5ECmEQvU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55cdc738-5dd0-4acc-b68b-053931d17a2e",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9CYtRcajn7twpyWk3R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e37a28f3-aacc-44b3-b01f-ee65ed38b4ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176ERFdgRTnY8CHRMm4Khdu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 39317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2841,
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

_source line 28 · 2026-05-21T05:13:29.056Z_

<details><summary>↩ Tool result · `toolu_013cy53KQ9CUKZsQ5ECmEQvU`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues. Performance-based detectors identify contamination through statistical anomalies: ConStat \citep{dekoninck2024constat} tests performance gaps between original and perturbed items, DVD \citep{liang2026dvd} uses distributional verification, and Self-Critique \citep{tao2026selfcritique} employs model self-evaluation. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This distinction is central to our Claim~2 (\Cref{sec:groundtruth}): web-overlap labels cannot serve as ground truth for differential detectors, because most benchmark items are globally exposed to all model cohorts. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, which further motivates behavioral approaches grounded in psychometric theory rather than NLL-based signals.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	Item Response Theory (IRT) provides a principled framework for jointly analyzing test items and examinee ability, and its adoption in LLM evaluation has accelerated. \citet{lalor2019irt} introduced IRT to NLP by fitting item parameters to human and model response data; their analysis revealed that item difficulty and discrimination vary substantially across benchmark questions. \citet{vania2021irt} applied IRT to assess test set discriminability and found that many items in standard NLP benchmarks contribute little information about model differences. Recent extensions include PSN-IRT \citep{zhou2026psnirt}, which fits four-parameter logistic models to characterize benchmark quality at scale, and scalability coefficients \citep{hardy2026scalability} as lightweight item quality pre-filters. TinyBenchmarks \citep{maiapolo2024tinybenchmarks} uses IRT-based item selection to construct representative benchmark subsets that predict full-benchmark scores with far fewer items. ATLAS \citep{li2025atlas} and IRTNet \citep{chen2025irtnet} explore neural extensions of classical IRT for LLM ability estimation, and \citet{choi2026llmjudgeirt} apply IRT to calibrate LLM-as-judge evaluations.
9	
10	The closest concurrent work is Growing Pains \citep{habba2026growingpains}, which addresses score comparability across model generations through fixed-parameter calibration \citep[FPC;][]{kim2019fpc}. FPC anchors a common ability scale by fixing the item parameters of a shared anchor set, so that models calibrated at different times receive scores on the same metric. Their framework selects 100 anchor items with stable IRT parameters and calibrates new models against this fixed scale, which enables extensible evaluation without full re-calibration. Our work is complementary: Growing Pains assumes anchor item stability, while DIF analysis diagnoses which items violate this assumption. The combination yields a monitored extensible evaluation system: DIF flags anchor items whose functioning has degraded, and the calibration framework triggers re-selection when the stable anchor set shrinks below a validity threshold.
11	
12	\paragraph{DIF Methodology and Measurement Invariance.}
13	The Mantel-Haenszel procedure for DIF detection was introduced by \citet{holland1988mh} and remains the most widely used method in educational testing due to its simplicity and well-characterized statistical properties \citep{clauser1998dif}. Alternative approaches include logistic regression DIF \citep{swaminathan1990logistic}, SIBTEST \citep{shealy1993sibtest}, Lord's $\chi^2$ test \citep{lord1980irt}, and the Raju area method \citep{raju1988area}; \citet{zumbo1999handbook} provides a comprehensive comparison. DIF analysis is a specific instance of measurement invariance testing \citep{meredith1993invariance, vandenberg2000invariance}, which examines whether a measurement instrument functions equivalently across populations. MIMIC models offer a latent-variable approach to the same problem \citep{muthen1985mimic, woods2009mimic}, and \citet{teresi2007dif} reviews DIF methods across applied domains. We do not modify the MH procedure; our contribution is the application context. The scale of this analysis (5,227 examinees across a 57-subject multidimensional ability space) exceeds typical educational testing applications, where \citet{belzak2020smallsample} note that DIF methods can behave differently at extreme sample sizes. The primary methodological challenge is the impact-versus-DIF confound: genuine ability differences between temporal cohorts can inflate DIF estimates. We address this through matched-ability quintile analysis, IRT $\theta$-conditioning, and a random-split control (\Cref{sec:temporal}).
14	
15	\paragraph{Benchmark Design and Concurrent Work.}
16	Our analysis psychometrically characterizes an existing benchmark (MMLU; \citealp{hendrycks2021mmlu}) rather than constructing a new one. Several concurrent efforts address benchmark limitations through design. Dynamic benchmarks such as Dynabench \citep{kiela2021dynabench} and LatestEval \citep{li2024latesteval} generate items adversarially or from recent sources to prevent memorization, and LiveBench \citep{white2025livebench} refreshes items monthly from contemporary material. Chatbot Arena \citep{chiang2024chatbot} and GAIA \citep{mialon2023gaia} sidestep static benchmarks entirely through pairwise human preference or real-world task completion. HELM \citep{liang2023helm} standardizes evaluation across tasks but does not address item-level stability. These approaches mitigate contamination by construction, yet none provides psychometric equating across versions: a model's score on LiveBench v3 is not directly comparable to its score on v1 without an anchoring mechanism such as that of \citet{habba2026growingpains}. METABENCH \citep{kipnis2024metabench} provides the large-scale response matrix (5,227 models $\times$ 12,508 items) that makes our analysis possible.
17	
18	\paragraph{LLM Evaluation Methodology.}
19	Broader surveys of LLM evaluation \citep{chang2024survey} identify benchmark saturation and lack of item-level transparency as systemic challenges. \citet{burnell2023rethink} argue that current practices treat benchmarks as monolithic scores, which obscures item-level variation in difficulty, discrimination, and stability. MMLU-Pro \citep{wang2024mmlupro} addresses saturation by increasing item difficulty, and \citet{ott2022benchmark} document how benchmark scores plateau as models improve. These diagnoses converge on a common gap: the absence of tools that operate at the item level rather than the benchmark level. Our DIF analysis fills this role by identifying which items within a benchmark have become unreliable for cross-generation comparison.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e37a28f3-aacc-44b3-b01f-ee65ed38b4ec",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "46ffd6fb-f50c-4f25-bf22-fa89fd51306c",
  "sourceToolAssistantUUID": "e37a28f3-aacc-44b3-b01f-ee65ed38b4ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T05:13:29.531Z_

<details open><summary>🔧 Tool call — Read · `toolu_0151CLMbsoCVf4KFhZqvhNWk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46ffd6fb-f50c-4f25-bf22-fa89fd51306c",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9CYtRcajn7twpyWk3R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "527ecf23-2d7b-4593-b602-e5f8242de734",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176ERFdgRTnY8CHRMm4Khdu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 39317,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2841
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 39317,
          "cache_creation_input_tokens": 2841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2841,
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

_source line 30 · 2026-05-21T05:13:29.536Z_

<details><summary>↩ Tool result · `toolu_0151CLMbsoCVf4KFhZqvhNWk`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, a semi-synthetic validation framework, diagnostic checks, and statistical controls.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees into $K$ score bins based on total score (a proxy for $\theta$), where $K$ equals the number of distinct total scores observed in the combined sample, and computing a common odds ratio across strata. Within each stratum $k$, the responses of the reference group and the focal group form a $2 \times 2$ contingency table:
17	
18	\begin{equation}
19	\label{eq:mh}
20	\alpha_{\mathrm{MH}} = \frac{\displaystyle\sum_{k=1}^{K} A_k D_k \,/\, T_k}{\displaystyle\sum_{k=1}^{K} B_k C_k \,/\, T_k}\,,
21	\end{equation}
22	
23	\noindent where $A_k$ and $B_k$ are the number of correct and incorrect responses in the reference group for stratum $k$, $C_k$ and $D_k$ are the corresponding counts for the focal group, and $T_k$ is the total number of examinees in stratum $k$. Under the null hypothesis of no DIF, $\alpha_{\mathrm{MH}} = 1$. The log odds ratio is converted to the ETS delta scale:
24	
25	\begin{equation}
26	\label{eq:delta}
27	\Delta_{\mathrm{MH}} = -2.35 \ln(\alpha_{\mathrm{MH}})\,.
28	\end{equation}
29	
30	The Educational Testing Service (ETS) classifies DIF severity into three categories based on $|\Delta_{\mathrm{MH}}|$. Category~A (negligible) requires $|\Delta_{\mathrm{MH}}| < 1.0$. Category~C (large) requires both $|\Delta_{\mathrm{MH}}| \geq 1.5$ and statistical significance at $p < 0.05$ from the MH chi-squared test. Category~B (moderate) includes all remaining items: those with $1.0 \leq |\Delta_{\mathrm{MH}}| < 1.5$, or $|\Delta_{\mathrm{MH}}| \geq 1.5$ without statistical significance. The dual threshold in ETS~C (effect size \emph{and} significance) guards against flagging items that show large but unreliable effect sizes. Throughout this paper, we report the percentage of items classified as ETS~C, denoted C\%.
31	
32	The choice of matching variable (the total score used for stratification) affects both validity and interpretation. We distinguish three matching strategies: (1)~\emph{standard matching} uses the within-benchmark total score on all items of the same benchmark; (2)~\emph{cross-subject matching} uses the total score on all subjects \emph{other than} the one containing the item under test, preventing the matching variable from absorbing injected contamination signals (\Cref{sec:injection}); and (3)~\emph{external matching} uses the total score on a different benchmark entirely (e.g., MMLU total score as the matching variable when testing DIF on GSM8K items), providing an independent ability proxy uncontaminated by the target benchmark. Cross-subject and external matching both address matching variable contamination but at different granularities: cross-subject operates within a multi-domain benchmark, while external operates across benchmarks.
33	
34	\subsection{Cohort Designs}
35	\label{sec:cohorts}
36	
37	DIF requires defining a reference group and a focal group. We construct five cohort comparisons, each designed to isolate a different source of variation.
38	
39	\paragraph{Temporal.} The reference group consists of models released in 2023 ($N = 1{,}080$) and the focal group consists of models released in 2024 ($N = 807$). This is the primary comparison for detecting items whose functioning changed across model generations.
40	
41	\paragraph{Ability-quintile.} Models within the same temporal window are divided by total score into quintiles. The focal group contains the lowest-scoring models (Q1--Q2) and the reference group contains the highest-scoring models (Q4--Q5). This comparison tests whether ability differences alone produce DIF, without temporal confounds.
42	
43	\paragraph{Within-family.} Llama-2 models ($N = 161$) serve as the reference group and Llama-3 models ($N = 308$) as the focal group. This comparison isolates generational changes within a single model family.
44	
45	\paragraph{Within-subject.} DIF is computed separately for each of the 57 MMLU subjects, with the matching variable (total score) restricted to items within the same subject. This design tests whether instability concentrates in specific knowledge domains.
46	
47	\paragraph{Random split.} The 2023 cohort is divided into two equal random halves ($N = 540$ each). This serves as a sanity check: no systematic DIF should appear between two random subsets of the same population (expected C\% $\approx 0$).
48	
49	\subsection{Semi-Synthetic Injection Framework}
50	\label{sec:injection}
51	
52	To evaluate whether MH-DIF can detect differential contamination when it is present, we construct a semi-synthetic framework with controlled ground truth.
53	
54	\paragraph{Procedure.} From items classified as ETS~A in the uninjected data (negligible DIF), we select 20\% uniformly at random as the ``contaminated'' set. For each contaminated item, we flip incorrect responses to correct in the focal group at exploitation rate $p \in \{0.0, 0.3, 0.5, 0.7, 1.0\}$. We then run MH-DIF on the modified response matrix and measure detection performance. We report $\Delta\mathrm{TPR} = \mathrm{TPR}(\text{injected}) - \mathrm{TPR}(\text{baseline})$ and $\Delta\mathrm{FPR} = \mathrm{FPR}(\text{injected}) - \mathrm{FPR}(\text{baseline})$, where TPR is the true positive rate on injected items and FPR is the false positive rate on uninjected items. Each injection level is repeated across 5 random seeds for uncertainty estimation.
55	
56	\paragraph{Cross-subject matching.} The choice of matching variable is critical for valid semi-synthetic evaluation. When contamination is injected into items within subject $X$, the total score on subject $X$ absorbs part of the injection signal. Using this contaminated total score as the MH matching variable violates the conditional independence assumption and inflates FPR. Cross-subject matching resolves this problem by computing the matching variable from all subjects \emph{other than} the one being tested. Under this protocol, $\Delta\mathrm{FPR} = 0.000$ across all five MMLU domains, while detection power is preserved ($\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$ for four of five subjects). We adopt cross-subject matching as the standard protocol for all semi-synthetic analyses.
57	
58	\subsection{Diagnostics}
59	\label{sec:diagnostics}
60	
61	Three diagnostic procedures complement the primary DIF analysis.
62	
63	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
64	
65	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
66	
67	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
68	
69	\subsection{Statistical Considerations}
70	\label{sec:statistical}
71	
72	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini-Hochberg FDR correction at $q = 0.05$. The random-split sanity check provides an empirical estimate of the false positive rate under the null hypothesis.
73	
74	\paragraph{Threshold sensitivity.} We report results across a range of DIF thresholds ($|\Delta_{\mathrm{MH}}| \in \{1.0, 1.5, 2.0, 2.5\}$) to verify that qualitative conclusions do not depend on the specific ETS~C cutoff. The standard threshold of $|\Delta_{\mathrm{MH}}| \geq 1.5$ corresponds to the ETS~C definition used throughout the paper.
75	
76	\paragraph{Architecture heterogeneity.} The METABENCH MMLU population consists of 99.98\% decoder-only models (5,226 of 5,227). This near-complete architectural homogeneity eliminates architecture as a confound for DIF analysis. We verify this by excluding the single encoder-decoder model and confirming identical results.
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "527ecf23-2d7b-4593-b602-e5f8242de734",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "c39559f2-d196-4656-b162-7315a884084c",
  "sourceToolAssistantUUID": "527ecf23-2d7b-4593-b602-e5f8242de734",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T05:13:32.858Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xa9g9k3QGfYWrg8RcjUi6M`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c39559f2-d196-4656-b162-7315a884084c",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9CtDGrmpcfwkTwYgri",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5434902-1d8c-44cf-a02e-c84d70e1cde8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AisuL4ZG5qrtNt9YgGJzEV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5120,
      "cache_read_input_tokens": 42158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5120,
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

_source line 32 · 2026-05-21T05:13:32.863Z_

<details><summary>↩ Tool result · `toolu_01Xa9g9k3QGfYWrg8RcjUi6M`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH dataset~\citep{kipnis2024metabench}, which provides sparse response matrices for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. All temporal analyses define reference and focal cohorts by model release date (2023 vs.\ 2024). We validate detection power through simulation, characterize temporal instability across multiple cohort designs, evaluate the relationship between DIF flags and existing contamination labels, and assess downstream consequences for benchmark rankings. Replication on GSM8K with cross-benchmark contamination validation appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	To confirm that MH-DIF detects differential item functioning at the sample sizes available in METABENCH, we conduct a power analysis using empirical MMLU IRT parameters. We simulate item response matrices where a controlled subset of items has injected DIF of varying magnitude ($|\Delta_{\mathrm{MH}}| \geq 1.4$) and evaluate ETS~C classification across sample sizes $N \in \{40, 80, 160, 320\}$ per cohort. At $N \geq 80$, ETS~C achieves true positive rates of 0.68--0.80 with false positive rates of 0.036--0.042 and AUC of 0.93--0.94. The temporal cohort sizes in our analysis ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold, and statistical power is not a limiting factor for the results reported below. Full simulation results with confidence intervals appear in Appendix~Table~A1.
10	
11	\subsection{Temporal Comparability: 31\% Item Instability}
12	\label{sec:temporal}
13	
14	The central finding of this paper is that a substantial fraction of MMLU items behave differently across model generations. Comparing models released in 2023 ($N = 1{,}080$) against models released in 2024 ($N = 807$), 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$). Applying Benjamini-Hochberg FDR correction at $q = 0.05$ reduces this from 31.32\% to 31.30\%, removing only 3 items. The minimal impact of FDR correction reflects the fact that the ETS classification system imposes a dual threshold on both effect size and statistical significance, which already provides implicit multiple-testing protection. In absolute terms, nearly one in three MMLU items exhibits a large shift in its statistical relationship to overall model ability between the two cohort periods.
15	
16	Three control conditions establish that this instability reflects genuine temporal change rather than methodological artifacts. A random split of the 2023 cohort into two equal halves produces only 0.18\% ETS~C items, confirming that sampling noise alone does not generate large-scale DIF. An ability-quintile comparison (lowest-scoring vs.\ highest-scoring models within the same temporal cohort) yields 2.9\% ETS~C items, indicating that ability differences alone are insufficient to produce the observed instability. A within-family comparison of Llama-2 ($N = 161$) and Llama-3 ($N = 308$) models produces 61.3\% ETS~C items. This elevated rate is consistent with the known sensitivity of MH-DIF to ability differences between groups~\citep{holland1988mh}: models from different generations within a single family exhibit large ability gaps that confound the DIF signal. The contrast between 2.9\% (ability-controlled) and 61.3\% (ability-confounded) brackets the temporal rate of 31.3\% and confirms that it captures a mixture of genuine item instability and residual ability differences.
17	
18	The instability penetrates within every knowledge domain. Within-subject analysis yields an average of 38.1\% ETS~C items across all five MMLU subjects (range: 31--45\%), and the ecological correlation between subject-level accuracy improvement and subject-level C\% is $\rho = 0.307$ ($p = 0.02$). This ecological correlation could suggest that domains where models improved most also exhibit the most instability. Item-level logistic regression, however, reveals that domain accuracy improvement explains only 2.4 percentage points of the 31.3\% temporal C\% (pseudo $R^2 = 0.0007$; counterfactual C\% with domain improvement regressed out $= 29.0\%$). Of the observed instability, 92.4\% is unrelated to aggregate domain-level accuracy gains and instead reflects item-specific changes in how models interact with individual questions. After controlling for item difficulty and discrimination (pseudo $R^2 = 0.042$), the coefficient of domain improvement reverses sign (Simpson's paradox), further confirming that domain-level accuracy gains do not drive the observed instability.
19	
20	Architecture heterogeneity is a non-issue for this analysis. The METABENCH MMLU population is 99.98\% decoder-only (5,226 of 5,227 models). Excluding the single encoder-decoder model yields C\% $= 31.32\%$ with Jaccard similarity of 1.0 between flagged item sets. Threshold sensitivity analysis confirms robustness across the full ETS range: C\% $= 48.9\%$ at $|\Delta_{\mathrm{MH}}| \geq 1.0$, $31.3\%$ at $\geq 1.5$ (the standard ETS~C threshold), $18.3\%$ at $\geq 2.0$, and $10.2\%$ at $\geq 2.5$. The qualitative conclusion holds at every threshold. \Cref{tab:temporal_landscape} summarizes the DIF landscape across all cohort comparisons.
21	
22	\begin{table}[t]
23	\centering
24	\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\Delta_{\mathrm{MH}}| \geq 1.5$. FPR is measured against Li et al.\ web-overlap labels on the ``clean'' (non-overlapping) subset. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels.}
25	\label{tab:temporal_landscape}
26	\small
27	\begin{tabular}{lcccc}
28	\toprule
29	Cohort Definition & $N_{\mathrm{ref}}$ / $N_{\mathrm{focal}}$ & ETS~C (\%) & FPR (Li clean) & Enrichment \\
30	\midrule
31	Temporal (2023 vs.\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.96 \\
32	Ability quintile (Q1--2 vs.\ Q4--5) & ${\sim}$2,600 / ${\sim}$2,600 & 2.9 & 0.027 & 1.19 \\
33	Within-family (Llama-2 vs.\ 3) & 161 / 308 & 61.3 & -- & -- \\
34	Random split (sanity) & 540 / 540 & 0.18 & -- & -- \\
35	Within-subject (avg, 5 subjects) & \textit{varies} & 38.1 & -- & -- \\
36	\bottomrule
37	\end{tabular}
38	\end{table}
39	
40	\subsection{Ground Truth Mismatch}
41	\label{sec:groundtruth}
42	
43	If DIF captures differential contamination, flagged items should overlap with independently identified contaminated items. We evaluate this hypothesis against the web-overlap labels of \citet{li2024contamination}, which classify MMLU items as ``contaminated'' based on verbatim matches in web training corpora. The enrichment ratio of DIF flags against these labels is 0.96 (\Cref{tab:temporal_landscape}), indistinguishable from chance. This null result does not indicate that DIF fails to detect contamination. Semi-synthetic injection experiments demonstrate a clear dose-response relationship: injecting controlled differential contamination at exploitation rate $p = 0.5$ produces $\Delta\mathrm{TPR} = {+}0.508$, and at $p = 1.0$, $\Delta\mathrm{TPR} = {+}0.674$ (\Cref{fig:dose_response}). The disconnect between DIF flags and web-overlap labels arises because the two methods answer fundamentally different questions.
44	
45	Web-overlap labels measure \emph{global exposure}: whether an item exists in publicly accessible training data. DIF measures \emph{differential functioning}: whether an item's statistical relationship to overall ability changes across temporal cohorts. An item can be globally contaminated yet function identically across cohorts if all model generations have comparable access to the same training data. Conversely, an item can exhibit large DIF without any identifiable contamination source if changes in training methodology alter how models process certain question types. The Li et al.\ labels are therefore the wrong ground truth for evaluating a differential detection method: the near-chance enrichment is expected, not evidence of failure.
46	
47	\begin{figure}[t]
48	\centering
49	\includegraphics[width=\columnwidth]{fig_2_dose_response.pdf}
50	\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\Delta\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF detects differential contamination when present. Baseline (no injection) produces $\Delta\mathrm{TPR} \approx 0$.}
51	\label{fig:dose_response}
52	\end{figure}
53	
54	\subsection{Structural Analysis}
55	\label{sec:structural}
56	
57	Three progressively refined approaches fail to reduce the temporal false positive rate below 31\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal FPR unchanged at approximately 0.31. IRT $\theta$-conditioning with 20 ability strata achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ and FPR $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. Within-subject DIF analysis, intended to isolate subject-specific effects, finds C\% $= 38.1\%$ across subjects, exceeding the 25\% threshold that would indicate viable bifactor structure. \Cref{tab:structural_comparison} summarizes these results. The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\% of within-subject item pairs exceed $|Q3| > 0.20$, vs.\ 2.2\% cross-subject; $5{\times}$ ratio, $p = 2.3 \times 10^{-9}$), which contributes to elevated within-subject DIF rates but is not the primary driver: the cross-subject matching protocol addresses this bias, and temporal C\% persists under external matching (full Q3 distributions in Appendix~Figure~A2).
58	
59	\begin{table}[t]
60	\centering
61	\caption{Structural approaches to reducing temporal DIF. None reduces baseline FPR below 31\%, indicating that the observed instability is not an artifact of ability matching. Subscript $\pm$ values denote standard deviations across 5 injection seeds (baseline row only).}
62	\label{tab:structural_comparison}
63	\small
64	\begin{tabular}{lcccc}
65	\toprule
66	Approach & Mechanism & Temporal FPR & TPR ($p{=}0.5$) & Outcome \\
67	\midrule
68	Baseline (external) & Cross-benchmark total score & $0.314_{\pm.009}$ & $0.834_{\pm.027}$ & Reference \\
69	Matched-ability & Within-quintile temporal DIF & ${\sim}$0.31 & -- & Enrich.\ 0.94--1.04 \\
70	$\theta$-conditioning & $\theta$ replaces total score & 0.312 & 0.876 & $r(\theta,\mathrm{total}) {=} 0.9986$ \\
71	Within-subject & Per-subject DIF & -- & -- & C\% $= 38.1\%$ ($>$25\%) \\
72	\bottomrule
73	\end{tabular}
74	\end{table}
75	
76	\subsection{Semi-Synthetic Framework Validation}
77	\label{sec:semisynthetic}
78	
79	The semi-synthetic injection framework enables controlled evaluation of DIF detection by flipping incorrect responses to correct for a designated ``contaminated'' subset of items in the focal cohort at a specified exploitation rate $p$. The critical methodological finding is that the choice of matching strategy determines whether the framework produces valid results. Cross-subject matching computes the matching variable from subjects \emph{other than} the one being tested, ensuring that the conditioning variable is unaffected by the injected contamination. Under this protocol, $\Delta\mathrm{FPR} = 0.000$ across all five MMLU subjects, and four of five subjects produce $\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$ (\Cref{fig:within_subject}). Within-subject matching, by contrast, computes the matching variable from the same subject where contamination was injected, which inflates FPR by an average of ${+}0.186$ because the matching variable absorbs part of the injection signal and violates the conditional independence assumption of the MH procedure. We adopt cross-subject matching as the standard protocol for all subsequent analyses and recommend it as default for semi-synthetic DIF evaluation on multi-subject benchmarks.
80	
81	\begin{figure}[t]
82	\centering
83	\includegraphics[width=\columnwidth]{fig_3_within_subject_matching.pdf}
84	\caption{Cross-subject vs.\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}
85	\label{fig:within_subject}
86	\end{figure}
87	
88	\subsection{Downstream Impact}
89	\label{sec:downstream}
90	
91	The practical relevance of 31\% item instability depends on whether unstable items affect model evaluation and benchmark rankings. We investigate this through a four-layer analysis that progresses from aggregate statistics to model-specific diagnostics.
92	
93	\paragraph{Layer 1: Benchmark redundancy.} Spearman correlation between model rankings computed on all 12,508 items versus stable-only items (ETS~A/B) is $\rho \approx 0.997$. At the level of aggregate rankings, removing 31\% of items changes almost nothing. This redundancy is a consequence of the large item pool: 12,508 items provide sufficient statistical mass that removing nearly a third does not alter rank order.
94	
95	\paragraph{Layer 2: Signal concentration with circularity check.} Despite aggregate redundancy, DIF-flagged items carry more discriminative signal than the average item. Removing DIF items degrades ranking discriminability more than removing an equal number of random items ($z = -8$ to $-49$ across 21 experimental conditions). A circularity ablation, however, places this in context: DIF-based removal is the \emph{least} disruptive among non-random removal strategies. Accuracy-gap removal produces $z = -156.5$, high-variance removal $z = -107.9$, and high-discrimination removal $z = -15.8$, compared to $z = -9.5$ for DIF removal. The Jaccard overlap between DIF-flagged and high-discrimination items is only 0.12. DIF items carry more signal than average, but DIF isolates differential behavior across cohorts specifically, not generally informative items.
96	
97	\paragraph{Layer 3: Diagnostic lens.} Individual model families show distinctive DIF profiles that reveal which families disproportionately benefit from unstable items. Phi-3 and Llama-3 models gain ${+}700$ to ${+}850$ rank positions when evaluated on stable items only, suggesting inflated performance on items whose function changed between 2023 and 2024. Mistral-based model merges show the opposite pattern, losing $-400$ to $-587$ positions. A caveat applies: among the top 50 rank movers, most lack documented training details in METABENCH, limiting interpretation of what training choices drive these rank shifts.
98	
99	\paragraph{Layer 4: Cross-benchmark signal.} The DIF instability pattern extends beyond MMLU. \Cref{sec:gsm8k} presents a full replication on GSM8K with independent contamination validation using the GSM1K held-out set~\citep{zhang2024gsm1k}. \Cref{fig:downstream} visualizes the relationship between full and DIF-filtered rankings.
100	
101	\begin{figure}[t]
102	\centering
103	\includegraphics[width=\columnwidth]{fig_4_downstream_impact.pdf}
104	\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\rho \approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only, with Phi-3 and Llama-3 gaining and Mistral merges losing rank positions.}
105	\label{fig:downstream}
106	\end{figure}
107	
108	\subsection{Cross-Benchmark Validation: GSM8K}
109	\label{sec:gsm8k}
110	
111	To test whether temporal DIF is specific to MMLU or reflects a broader phenomenon in LLM benchmarking, we replicate the full analysis pipeline on GSM8K (1,319 items $\times$ 6,702 models from METABENCH).
112	
113	\paragraph{Temporal DIF.} Standard matching yields C\% $= 18.9\%$ for the temporal cohort comparison, with a random-split sanity check at 0.3\%. The lower instability rate compared to MMLU (31.3\%) is consistent with GSM8K's more homogeneous item structure: single-domain mathematical reasoning versus MMLU's 57 diverse subjects. The sanity check confirms that the signal is non-random.
114	
115	\paragraph{Semi-synthetic validation.} Dose-response confirms detection power on this benchmark. Standard matching achieves $\Delta\mathrm{TPR} = {+}0.818$ at exploitation rate $p = 0.7$. External matching (using scores on ARC, HellaSwag, TruthfulQA, and Winogrande to match models) yields $\Delta\mathrm{TPR} = {+}0.514$ at $p = 0.5$, comparable to MMLU's ${+}0.508$ at the same exploitation rate, with $\Delta\mathrm{FPR}$ well-controlled. \Cref{tab:gsm8k_comparison} compares key metrics across both benchmarks.
116	
117	\paragraph{GSM1K contamination gap.} The GSM1K dataset~\citep{zhang2024gsm1k} provides an independent measure of per-model contamination by comparing performance on the original GSM8K versus a held-out set of novel problems. For $N = 33$ models with both GSM1K scores and METABENCH evaluations, we correlate each model's contamination gap (GSM8K accuracy minus GSM1K accuracy) with the ranking advantage gained from DIF-flagged items. The observed correlation is $r = -0.478$ (95\% CI $= [-0.71, -0.16]$, $p = 0.005$; item-permutation $p = 0.014$), with partial $r = -0.385$ ($p = 0.027$) after controlling for overall accuracy. Our original hypothesis predicted a \emph{positive} correlation: models benefiting more from contamination should also benefit more from DIF items. The observed \emph{negative} correlation indicates the opposite. DIF-C items resist contamination-based performance gains, and models with larger contamination gaps benefit \emph{less} from these items. This result is suggestive at $N = 33$ and warrants replication with larger model populations, but it aligns with the broader interpretation that DIF captures item-level behavioral change distinct from simple memorization of training data. \Cref{fig:gsm1k} shows the correlation scatter.
118	
119	\begin{figure}[t]
120	\centering
121	\includegraphics[width=\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}
122	\caption{GSM1K contamination gap vs.\ DIF ranking advantage for $N = 33$ models. The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items, contrary to the initial positive-correlation hypothesis.}
123	\label{fig:gsm1k}
124	\end{figure}
125	
126	\begin{table}[t]
127	\centering
128	\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal item instability with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\pm$ values denote standard deviations across 5 random injection seeds.}
129	\label{tab:gsm8k_comparison}
130	\small
131	\begin{tabular}{lcc}
132	\toprule
133	Metric & MMLU & GSM8K \\
134	\midrule
135	Items & 12,508 & 1,319 \\
136	Models & 5,227 & 6,702 \\
137	Temporal C\% & 31.3\% & 18.9\% \\
138	Sanity C\% & 0.18\% & 0.3\% \\
139	$\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\pm.006}$ \\
140	$\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\pm.027}$ & $+0.514_{\pm.028}$ \\
141	\bottomrule
142	\end{tabular}
143	\end{table}
144	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5434902-1d8c-44cf-a02e-c84d70e1cde8",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "4163224d-c00c-4c4b-a719-f29b38d97e60",
  "sourceToolAssistantUUID": "a5434902-1d8c-44cf-a02e-c84d70e1cde8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T05:13:36.892Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QRuR3svPi6EGuYdaUxjHsp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4163224d-c00c-4c4b-a719-f29b38d97e60",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9D8QJnEnbsBe7j9Yvm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65c77fee-631b-457c-b803-ff2c35f2d8aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2CQohN1TiMd9YZ87nZNYR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5943,
      "cache_read_input_tokens": 47278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5943,
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

_source line 34 · 2026-05-21T05:13:36.896Z_

<details><summary>↩ Tool result · `toolu_01QRuR3svPi6EGuYdaUxjHsp`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications for Benchmark Temporal Comparability}
5	\label{sec:disc_temporal}
6	
7	The 31\% ETS~C instability rate is robust across thresholds (10\% at $|\Delta_{\mathrm{MH}}| \geq 2.5$, rising to 49\% at $\geq 1.0$), and three structural controls (\Cref{sec:structural}) confirm it is not a methodological artifact. This means that cross-generation MMLU score comparisons carry uncontrolled item-level variance: nearly one in three items functions differently depending on when the evaluated model was trained. The instability decomposition (\Cref{sec:temporal}) sharpens this interpretation. Domain-level accuracy improvement explains only 2.4 percentage points of the 31.3\% C\% (pseudo $R^2 = 0.0007$), so 92.4\% of the instability is unrelated to aggregate capability gains. The items that change are not simply the ones that newer models answer correctly because they are better at a domain; instead, they change in item-specific ways that domain-level trends do not predict.
8	
9	This instability does not invalidate MMLU as a ranking instrument. Spearman $\rho \approx 0.997$ between full and stable-item rankings confirms that aggregate model ordering is preserved. The instability is diagnostic, not destructive: it identifies which measurement units shift across model generations without rendering the overall score unreliable. Benchmark designers should therefore consider monitoring DIF as a quality diagnostic alongside accuracy metrics. An item pool where C\% grows over successive model cohorts signals that the benchmark's measurement properties are drifting, even if rank ordering remains intact.
10	
11	\subsection{Ground Truth Meta-Critique}
12	\label{sec:disc_groundtruth}
13	
14	The near-chance enrichment (0.96) between DIF flags and web-overlap labels raises a question that extends beyond our specific analysis. All prior work that validates item-level contamination detectors against web-overlap or $n$-gram labels faces the same methodological gap: these labels measure whether an item exists in publicly accessible training corpora, not whether exposure differentially affects model behavior. Global exposure is a property of the data ecosystem; differential functioning is a property of how model cohorts interact with individual items. Most MMLU items are globally contaminated in the sense that they appear in web text, so web-overlap labels identify a condition shared by nearly all items rather than one that differentiates model cohorts. Validating differential detectors against such labels conflates two distinct phenomena.
15	
16	This observation constitutes a meta-contribution to the contamination detection literature. The enrichment ratio of $\approx 1.0$ is not evidence that DIF fails; it is the expected outcome when a differential method is evaluated against a global-exposure reference. Semi-synthetic injection confirms that DIF detects differential contamination when present ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \Cref{sec:semisynthetic}). The field needs validation methodologies that match the granularity of the detection task: item-level differential detectors require item-level differential ground truth, not item-level global-exposure labels.
17	
18	\subsection{DIF as Diagnostic Lens}
19	\label{sec:disc_diagnostic}
20	
21	\paragraph{Capability diagnostic.} The GSM1K correlation ($r = -0.478$, $p = 0.005$, $N = 33$; \Cref{sec:gsm8k}) provides evidence that DIF-flagged items capture behavioral change distinct from memorization. Models with larger contamination gaps (higher GSM8K minus GSM1K accuracy) benefit \emph{less} from DIF-C items, the opposite of what a pure memorization account would predict. Of the 249 focal-favoring DIF-C items, 171 have discrimination $\alpha < 1$, and the negative correlation concentrates in this low-discrimination subset. This pattern suggests that contamination produces a ``shallow'' performance boost on items that DIF does not flag, while DIF-C items capture genuine capability differences that contamination does not confer. Partial correlation ($r = -0.385$, $p = 0.027$) after controlling for overall accuracy confirms that the effect is not an artifact of general model quality. Several caveats apply: the confidence interval is wide (95\% CI $= [-0.71, -0.16]$), item difficulty as a confound is not fully excluded, and $N = 33$ limits generalizability. This result is suggestive and warrants replication with larger model populations.
22	
23	\paragraph{Structural constraints on DIF applicability.} Systematic experimentation reveals three structural constraints that jointly limit DIF utility in LLM benchmarks. First, 1D IRT model fit is imperfect: MMLU's multi-domain structure produces mild local dependence (11.3\% of within-subject item pairs exceed $|Q3| > 0.20$; \Cref{sec:structural}), which elevates within-subject DIF rates relative to cross-subject baselines. Second, the power analysis (\Cref{sec:validation}) establishes minimum requirements of $N \geq 80$ per cohort and $|\Delta_{\mathrm{MH}}| \geq 1.4$ for reliable detection. Benchmarks with small model populations or modest effect sizes will lack statistical power for DIF analysis. Third, ability differences between temporal cohorts confound the DIF signal: the within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% C\%, elevated above the 31.3\% temporal rate by the large ability gap between model generations. These are structural constraints revealed by our experimentation, not fundamental impossibilities. Higher-level methods (MIMIC models, propensity-score matching, multidimensional IRT) may address individual constraints, and their investigation on LLM benchmark data is a natural next step.
24	
25	\subsection{Limitations}
26	\label{sec:disc_limitations}
27	
28	\paragraph{(a) Ecological vs.\ item-level decomposition.} The ecological correlation between subject-level C\% and accuracy improvement is $\rho = 0.307$ ($p = 0.02$), but item-level decomposition shows that domain improvement explains only 2.4 percentage points (7.6\%) of 31.3\% C\%. The remaining 92.4\% cannot be fully attributed to contamination; other sources of capability change (training methodology, data composition, optimization procedures) may contribute, and our analysis does not isolate these factors.
29	
30	\paragraph{(b) Instability attribution.} The 31\% C\% measures items that function differently across cohorts, but the method does not distinguish contamination from legitimate capability change. DIF identifies \emph{that} items changed, not \emph{why}. The semi-synthetic framework validates detection power for one specific mechanism (differential exposure), but real-world instability likely reflects multiple interacting causes.
31	
32	\paragraph{(c) Semi-synthetic injection fidelity.} The injection procedure flips incorrect responses to correct at a specified rate, simulating an idealized contamination scenario. Real contamination may manifest as partial knowledge, format memorization, or selective retrieval rather than wholesale answer flipping. The gap between our injection model and realistic contamination mechanisms is unknown.
33	
34	\paragraph{(d) Benchmark scope.} The primary analysis covers MMLU with cross-benchmark validation on GSM8K (\Cref{sec:gsm8k}). GSM8K replication confirms framework portability and provides the GSM1K contamination correlation ($N = 33$), but full temporal DIF characterization on diverse benchmarks (code generation, long-form reasoning, multimodal tasks) has not been conducted. The GSM1K sample ($N = 33$) produces wide confidence intervals that limit the precision of the negative correlation estimate.
35	
36	\paragraph{(e) Cross-subject baseline false positive rate.} The cross-subject matching protocol achieves $\Delta\mathrm{FPR} = 0.000$ for injected contamination but does not reduce the baseline temporal FPR of 33--53\% across subjects. This rate is stable across injection levels, confirming it reflects genuine temporal instability rather than methodological error, but it means that a large fraction of flagged items in temporal comparisons are not attributable to the specific contamination mechanism under test.
37	
38	\paragraph{(f) RL model robustness.} Reinforcement learning from human feedback may alter item-level response patterns in ways that differ from pretraining-based contamination. The theoretical motivation for DIF robustness to RL (RL modifies the ability distribution rather than item parameters) is plausible but empirically unvalidated with adequate sample size: METABENCH contains only $N = 13$ models with documented reasoning-RL training.
39	
40	\paragraph{(g) Model family coverage.} Downstream impact analysis is limited to families with $N \geq 20$ models (Llama, Mistral, Qwen, Phi). Among the top 50 rank movers, 49 of 50 belong to the ``unknown'' family category in METABENCH, precluding interpretation of what training choices produce large rank shifts.
41	
42	\paragraph{(h) Future directions.} Cross-benchmark generalization to code, multimodal, and long-form reasoning benchmarks would test DIF applicability beyond factual knowledge tasks. RL model cohorts with adequate $N$ would enable empirical validation of the RL robustness hypothesis. MIMIC models and propensity-score matching could address the ability confounding that the current MH-DIF framework does not fully resolve.
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65c77fee-631b-457c-b803-ff2c35f2d8aa",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "355b3a14-1a73-4f2a-a211-06191dbd145c",
  "sourceToolAssistantUUID": "65c77fee-631b-457c-b803-ff2c35f2d8aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T05:13:37.390Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GFCKTPasZLcPqFHXJRB537`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "355b3a14-1a73-4f2a-a211-06191dbd145c",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9D8QJnEnbsBe7j9Yvm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10af6b66-e06c-4f04-9df6-5244c7c78160",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2CQohN1TiMd9YZ87nZNYR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5943,
      "cache_read_input_tokens": 47278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5943,
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

_source line 36 · 2026-05-21T05:13:37.396Z_

<details><summary>↩ Tool result · `toolu_01GFCKTPasZLcPqFHXJRB537`</summary>

```text
1	% Placeholder for conclusion
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10af6b66-e06c-4f04-9df6-5244c7c78160",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "4b48e999-7078-4daa-b6a2-8c709f678c04",
  "sourceToolAssistantUUID": "10af6b66-e06c-4f04-9df6-5244c7c78160",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T05:13:37.928Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LhpXhs4PT5y6TdkmoZbw3R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b48e999-7078-4daa-b6a2-8c709f678c04",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9D8QJnEnbsBe7j9Yvm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ab00a97-5503-4a96-a24c-2b262d5f9d8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2CQohN1TiMd9YZ87nZNYR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5943,
      "cache_read_input_tokens": 47278,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5943
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 47278,
          "cache_creation_input_tokens": 5943,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5943,
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

_source line 38 · 2026-05-21T05:13:37.933Z_

<details><summary>↩ Tool result · `toolu_01LhpXhs4PT5y6TdkmoZbw3R`</summary>

```text
1	% Placeholder for appendix
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ab00a97-5503-4a96-a24c-2b262d5f9d8d",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "95ee6f35-bf53-4787-877e-55a9be68e007",
  "sourceToolAssistantUUID": "4ab00a97-5503-4a96-a24c-2b262d5f9d8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-21T05:13:40.734Z_

Now let me check the actual paper PDF to see if there are additional figures and content, and also look at the dream review reports for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95ee6f35-bf53-4787-877e-55a9be68e007",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9DW8Wn3uvtHywjj8Gx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d263bd6-67df-46c1-8346-a2af348c3d25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LZ4U54rwSCPtJFkXd3N8NL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2696,
      "cache_read_input_tokens": 53221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2696,
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

_source line 40 · 2026-05-21T05:13:43.625Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01BaFwVinFmr7ctVJi8XVY3R`</summary>

```json
{
  "pattern": "**/dream_*/**/review*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d263bd6-67df-46c1-8346-a2af348c3d25",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9DW8Wn3uvtHywjj8Gx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d1fc4bf-e04d-4122-ba7d-fd1b68d5b579",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LZ4U54rwSCPtJFkXd3N8NL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2696,
      "cache_read_input_tokens": 53221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2696,
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

_source line 41 · 2026-05-21T05:13:43.651Z_

<details><summary>↩ Tool result · `toolu_01BaFwVinFmr7ctVJi8XVY3R`</summary>

```text
artifacts/dream_reports/dream_20260520T194223/best/review_report.md
artifacts/dream_reports/dream_20260520T194223/median/review_report.md
artifacts/dream_reports/dream_20260520T194223/worst/review_report.md
artifacts/dream_reports/dream_20260520T205007/best/review_report.md
artifacts/dream_reports/dream_20260520T205007/median/review_report.md
artifacts/dream_reports/dream_20260520T205007/worst/review_report.md
artifacts/dream_reports/dream_20260521T012912/best/review_report.md
artifacts/dream_reports/dream_20260521T012912/median/review_report.md
artifacts/dream_reports/dream_20260521T012912/worst/review_report.md
artifacts/dream_reports/dream_20260521T032826/best/review_report.md
artifacts/dream_reports/dream_20260521T032826/worst/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d1fc4bf-e04d-4122-ba7d-fd1b68d5b579",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "0dd0a8e9-e199-47bd-8b8d-0193691f54af",
  "sourceToolAssistantUUID": "4d1fc4bf-e04d-4122-ba7d-fd1b68d5b579",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T05:13:44.490Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HvdnUMCync7Mk1dBZ2UTrj`</summary>

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
  "parentUuid": "0dd0a8e9-e199-47bd-8b8d-0193691f54af",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9DW8Wn3uvtHywjj8Gx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f56d977-8741-4f47-9edf-6893975f87d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LZ4U54rwSCPtJFkXd3N8NL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2696,
      "cache_read_input_tokens": 53221,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2696
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 53221,
          "cache_creation_input_tokens": 2696,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2696,
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

_source line 43 · 2026-05-21T05:13:44.502Z_

<details><summary>↩ Tool result · `toolu_01HvdnUMCync7Mk1dBZ2UTrj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/memory.md\", \"content\": \"## MVP 验证关键经验 (2026-05-20)\\n\\n### D001 决策：ETS C 分类 > p-value 检验\\n- **p-value based DIF 检测在 200-item benchmark 上严重 underpowered**：BH 校正后 TPR 仅 0.04-0.07（N=50, δ=1.0）\\n- **ETS C 分类（|Δ_MH|≥1.5 + 显著性）是可行的替代**：TPR=0.68-0.85 at N≥80, δ≥1.4\\n- **AUC 一直很好（0.91-0.96）**\\n\\n### 关键操作参数\\n- N≥80/group 最低要求，N≥100 显著改善\\n- δ≥1.4 logits 可靠检测区间\\n- MH 5 层 quantile + ETS C 阈值是最佳组合\\n- Subject ≥200 items 才有足够 matching precision（<100 items baseline FPR 膨胀至 ~56%）\\n\\n## D006: plan_011 Semi-Synthetic 验证成功 ✅\\n\\n### DIF 检测差异性污染有效\\n- **External MH**: temporal ΔTPR=+0.674 (0.326→1.000), FPR 恒定 0.314\\n- **Matching variable contamination**: 20% items 注入时 standard MH FPR 0.298→0.616, anchor/external 免疫\\n- **Li et al. enrichment≈1.0 原因**: web-overlap = 全局性污染，不产生 DIF\\n\\n## D007-D010: 降低 FPR 路线全部穷尽 ⚠️\\n\\n### plan_012 θ-Conditioning 失败\\n- logit θ 与 total score 相关性 0.9986 → 单维 θ 分层 ≡ 总分分层\\n\\n### plan_014 Within-Subject 前置检查：C% = 38.1% (>25%)\\n- 5 个高 C% subjects 的 within-subject temporal C% 均 >25%（31-45%）\\n- Within vs cross-subject matching 差异仅 -2.4pp → 信号对 matching 不敏感\\n- **结论**：temporal DIF 渗透到每个 subject 内部，不是 between-subject 能力差异的伪影\\n- Bifactor 方向因此否定（D010）\\n\\n### plan_013 Q3 局部独立性：温和但存在\\n- Within-subject mean Q3 = 0.009（低于 0.20 阈值）\\n- 但 11.3% within-subject pairs |Q3|>0.20（vs 2.2% cross-subject，5x）\\n- 最严重: moral_scenarios 34.2%, world_religions 18%, marketing 17.5%\\n- 不太可能单独解释 31% FPR\\n\\n### plan_016 Within-Subject Semi-Synthetic：DIF 在 subject 内也有效 ✅\\n- Cross-subject matching FPR 完全稳定（ΔFPR=0.000），4/5 subjects ΔTPR>0.3\\n- Within-subject matching FPR 膨胀 +0.067 to +0.281（matching variable 包含注入 items）\\n- **结论**：within-subject 38% C% 是真实 temporal DIF，方法论有效\\n\\n### 综合推导：31% temporal FPR 不是 artifact\\n证伪链完整：1D θ 无效 → within-subject 仍高 → bifactor 否定 → Q3 不是主因 → **这是 genuine temporal DIF**（2023→2024 模型在特定 items 上的真实差异性表现变化）。DIF 方法有效但无法区分 contamination-DIF 和 capability-DIF。\\n\\n## D012: plan_017 Downstream Impact — DIF Items ≠ 噪声 ⚠️\\n\\n### Hypothesis 被证伪但发现更有价值\\n- **假设**: 移除 DIF items → 排名更稳定 → DIF 标记了 problematic items\\n- **实际**: DIF 移除造成 **更大** 排名扰动（z = -8 to -49σ, 21/21 条件）\\n- DIF items 是浓缩的差异化信息载体，不是噪声\\n\\n### 关键数字\\n- Full vs stable-only: ρ = 0.996-0.999（排名本身极鲁棒）\\n- DIF items 跨代准确率变化 = full benchmark 的 1.09×, stable = 0.96×\\n- Top beneficiaries: phi-3, llama-3 衍生（+700-850 rank positions）\\n- Top hurt: mistral merge/slerp 模型（-400 to -587 rank positions）\\n\\n### 对论文的启示\\n- DIF items 不是\\\"要清洗的坏题\\\"——是\\\"揭示模型代际差异的诊断工具\\\"\\n- 支持 characterization narrative > cleaning narrative\\n- \\\"Stable-only benchmark\\\" 不是\\\"更好的 benchmark\\\"，而是\\\"不同视角的 benchmark\\\"\\n\\n## plan_004: GSM8K Cross-Benchmark Validation (2026-05-21) 🔑\\n\\n### Step 1: GSM8K Temporal DIF 跨 benchmark 泛化 ✅\\n- GSM8K standard C% = 18.9%（MMLU 31.3%，同一量级）\\n- Sanity check 0.3%（通过）\\n- External matching C% = 47.4%——**非 contamination absorption**，是 construct validity gap（external benchmarks 测不同能力，控制了这些能力后 GSM8K item 行为差异更大）\\n- Standard vs external Spearman ρ = 0.926（高度一致）\\n\\n### Step 2: GSM8K Semi-Synthetic 验证 ✅\\n- Standard ΔTPR = +0.818 at p=1.0（MMLU +0.508，GSM8K 更强）\\n- External ΔTPR = +0.517\\n- GSM8K 的 DIF 对差异性污染更敏感（单域 benchmark, items 更同质）\\n\\n### Step 3: GSM1K Contamination Gap × DIF Correlation — 方向反转 ❌→🔑\\n- **r = −0.478 (p=0.005)**：contaminated 模型在 DIF-C items 上更差，非更好\\n- Partial r = −0.385 控制整体准确率后仍显著\\n- Permutation p = 0.014，robust to leave-one-out\\n- 171/249 DIF-C items α_MH < 1 → favor focal (2024) models（捕获真实代际能力提升）\\n- 78/249 DIF-C items α_MH > 1 → favor reference (2023) models\\n\\n### Step 3 核心洞察\\n- **DIF ⊥ contamination**：DIF 捕捉的 measurement anomalies 与 contamination 正交\\n- 171 个 focal-favoring DIF-C items 捕获真实代际能力提升，但 contaminated 模型在这些 items 上反而更差（r=−0.347, p=0.048）——contamination 的\\\"浅层\\\"boost 无法泛化到区分真实能力的题目\\n- **这是 characterization narrative 的强 evidence**：DIF 不标记\\\"被污染的 items\\\"，标记的是\\\"不同模型代际间行为模式不一致的 items\\\"\\n- 与 Xu et al. (2024) GSM1K 互补——他们检测 contamination，我们检测 construct-level measurement anomalies\\n\\n### α_MH 方向约定（Reviewer 修正 2026-05-21）\\n- α_MH > 1 → item 对 reference group 更容易\\n- α_MH < 1 → item 对 focal group 更容易\\n- 在 temporal cohort 中：reference = 2023, focal = 2024\\n\\n## 数据源 (2026-05-20)\\n\\n### METABENCH (Kipnis et al., ICLR 2025) ⭐\\n- GitHub: https://github.com/adkipnis/metabench\\n- Zenodo: https://zenodo.org/records/12819251 (620MB)\\n- MMLU 12,508 items, 5,219 模型\\n\\n### D002: preproc.rds diff/disc 是 CTT 不是 IRT\\n- diff = 0.75 × p_correct, disc = rpbis\\n- 实际 IRT 在 crossvalidate.R 用 mirt::mirt() slope-intercept\\n\\n### Li et al. (EMNLP 2024) Proxy Ground Truth\\n- 9,229/12,508 items 有标注（73.8%）\\n- clean 60.5% / input_and_label 33.0% / input_only 6.5%\\n- Web overlap proxy，非训练数据精确标签——全局性污染，不适合 DIF 验证\\n\", \"total_chars\": 4457, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f56d977-8741-4f47-9edf-6893975f87d0",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "d4aade64-d2fc-4da6-a4fd-1af2405e2d21",
  "sourceToolAssistantUUID": "5f56d977-8741-4f47-9edf-6893975f87d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-21T05:13:47.206Z_

I now have a thorough understanding of the paper. Let me also check the latest dream review to understand what prior reviewers noted.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4aade64-d2fc-4da6-a4fd-1af2405e2d21",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9DzCDjfpgSzHnfCxd2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db94ba49-28de-40b6-ad84-006abb09c596",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkCQXsDjbgE1EXeFMFdd9N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3289,
      "cache_read_input_tokens": 55917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3289,
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

_source line 45 · 2026-05-21T05:13:49.364Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TorETVLpGBv1wese2p2weE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db94ba49-28de-40b6-ad84-006abb09c596",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9DzCDjfpgSzHnfCxd2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c4cdbf0-5aff-4125-94e6-e662cd51ac62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkCQXsDjbgE1EXeFMFdd9N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3289,
      "cache_read_input_tokens": 55917,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3289
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 55917,
          "cache_creation_input_tokens": 3289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3289,
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

_source line 46 · 2026-05-21T05:13:49.368Z_

<details><summary>↩ Tool result · reported error · `toolu_01TorETVLpGBv1wese2p2weE`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c4cdbf0-5aff-4125-94e6-e662cd51ac62",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "6dad18e7-c2e8-4a28-86cb-6a6622c0d7da",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen.",
  "sourceToolAssistantUUID": "3c4cdbf0-5aff-4125-94e6-e662cd51ac62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T05:13:52.685Z_

<details open><summary>🔧 Tool call — Read · `toolu_014eX8UWE1y3Lt1ADNroVqga`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dad18e7-c2e8-4a28-86cb-6a6622c0d7da",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9EM3qqe5G5SStPGSmH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eaee04bc-be68-4d0f-b7e9-ea71fd37d877",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DbSEJ4GVMHvxgNGhyMRPE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 199,
      "cache_read_input_tokens": 59206,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 199
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 59206,
          "cache_creation_input_tokens": 199,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 199,
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

_source line 48 · 2026-05-21T05:13:52.703Z_

<details><summary>↩ Tool result · `toolu_014eX8UWE1y3Lt1ADNroVqga`</summary>

```text
1	---
2	dream_id: dream_20260521T032826
3	tier: best
4	overall_score: 3 — Weak Reject
5	timestamp: 2026-05-21T03:57:18.068414+00:00
6	---
7	
8	# Review Report: Psychometric Analysis Reveals Structural Benchmark Instability That Contamination Validation Cannot Detect
9	
10	## Summary
11	
12	The paper applies Differential Item Functioning (DIF) from classical psychometrics to the METABENCH response matrix (5,227 models × 12,508 MMLU items) and finds that 28–30% of items are temporally unstable across model generations. It argues this instability persists within architecture-homogeneous decoder-only populations (RMSEA=0.024), survives controlling for domain accuracy improvement (partial ρ=0.22), and is invisible to web-overlap contamination labels. The paper further presents RL-robustness comparisons, complementary detection methods (ConStat, DVD, ensemble), continuous monitoring extensions (IFT, Bayesian DIF), and an equating-based benchmark maintenance framework.
13	
14	---
15	
16	## Strengths
17	
18	**S1. Novel and timely cross-disciplinary contribution.** Applying DIF — a well-validated psychometric tool with decades of theory — to LLM benchmark evaluation is genuinely original. The framing of "temporal score comparability" as a testable psychometric assumption, rather than taking it for granted, is an important conceptual contribution that the ML evaluation community needs.
19	
20	**S2. Architecture-stratified analysis is rigorous and preemptively addresses the strongest objection.** The decision to stratify to decoder-only models and demonstrate that IRT fit becomes excellent (RMSEA=0.024, CFI=0.966) while DIF persists at 29.1% effectively eliminates the multidimensionality confound. The random-split sanity check (0.14%) and the quantification of architecture-mixing contribution (~2pp) are well-designed controls. This is the strongest section of the paper.
21	
22	**S3. Instability decomposition is a thoughtful analysis.** Separating domain-level accuracy improvement (ρ=0.307) from residual item function change (partial ρ=0.22) addresses the natural objection that DIF simply reflects "models got better." The honest disclosure that domain accuracy explains 9.4% of variance, with residual instability persisting, is scientifically rigorous.
23	
24	**S4. Scale is unprecedented.** 5,227 models × 12,508 items is by far the largest DIF analysis applied to LLM benchmarks. The METABENCH dataset enables population-level inferences that smaller studies cannot support.
25	
26	**S5. Non-uniform DIF robustness check validates methodological choice.** The 78% SIBTEST–MH overlap and low logistic regression interaction R²=0.008 provide principled justification for using MH as the primary DIF method. This level of methodological care is appreciated.
27	
28	**S6. Honest limitations.** The paper explicitly acknowledges N=13 for reasoning-RL, wide bootstrap CIs, simplified injection mechanisms, and the need for generalization beyond MMLU/GSM8K.
29	
30	---
31	
32	## Weaknesses
33	
34	**W1. (Major) Two of four claimed contributions lack experimental sections in the paper body.** The abstract and introduction prominently claim Contribution 2 (ground truth meta-critique: enrichment≈1.0 between DIF flags and web-overlap labels) and Contribution 3 (semi-synthetic validation framework: ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Neither has a corresponding section in §3–§9. The ΔTPR numbers, cross-subject matching (ΔFPR=0.000), and enrichment analysis appear only in the abstract. Similarly, Contribution 4's GSM8K cross-benchmark validation (r=−0.478, p=0.005) and measurement redundancy (ρ≈0.997 after 31% removal) are stated in the introduction but never presented with methodology or tables. This is a fundamental structural defect — the paper's own claimed contributions are unsupported by its body.
35	
36	**W2. (Major) Severe scope overextension — breadth at the cost of depth.** The paper attempts to present 10+ distinct experiments across architecture stratification, RL robustness, ConStat, DVD, ensemble fusion, IFT, Bayesian DIF, bifactor equating, item generation, and graceful degradation — all in 8 pages. Many sections (§5, §6, §7) read as catalogs of results with one paragraph of context and one table each. The equating pilot (§7.1), item generation (§7.2), and degradation analysis (§7.3) each deserve multi-page treatments but receive a paragraph. This compression prevents adequate description of methodology, assumptions, and limitations for each experiment. A focused paper on §3 + §4 + the missing Claims 2–3 sections would be far stronger.
37	
38	**W3. (Major) The instability decomposition's practical significance is overstated.** Partial ρ=0.22 explains 4.8% of item instability variance. While statistically significant (p=0.012), this is a small effect. The paper frames this as evidence of "genuine item function change" — technically correct but potentially misleading. The remaining ~86% of instability variance is unexplained. The paper should discuss what else might drive instability (item-specific memorization patterns, distractor sensitivity to generation strategies, positional biases, etc.) rather than leaving 86% as a black box.
39	
40	**W4. (Moderate) Conflation of temporal instability with contamination.** DIF measures differential item functioning between temporal cohorts — this can arise from contamination, but also from architectural evolution, training data composition shifts, RLHF/instruction-tuning effects, or genuine capability emergence. The paper's title and framing strongly imply DIF detects contamination ("Contamination Validation Cannot Detect"), but the relationship between DIF flags and actual contamination is never directly established. The low Jaccard overlap with ConStat (0.18) and DVD (0.13) — methods that do target contamination directly — suggests DIF may be measuring something quite different. This ambiguity should be foregrounded, not buried.
41	
42	**W5. (Moderate) Reasoning-RL comparison is underpowered and over-interpreted.** N=13 reasoning-RL models is acknowledged as a limitation, but the comparison with traditional detectors (Table 5) is presented as a headline finding (abstract, §4). The DeLong p-values (0.003, 0.008) are computed on a sample where the DIF group has only 13 observations — statistical significance with such small N is fragile. The paper should present this as preliminary evidence, not a demonstrated advantage.
43	
44	**W6. (Moderate) Missing Related Work section.** There is no survey of existing contamination detection literature. ConStat, Min-K%, GSM1K, and other methods are mentioned in passing but never properly situated. For a venue submission, a Related Work section contextualizing DIF against (a) existing contamination detectors, (b) prior psychometric applications to NLP/ML, and (c) benchmark validity literature is expected.
45	
46	**W7. (Minor) Ensemble evaluation lacks clear ground truth specification.** Table 8 reports AUROC for various detection strategies, but the paper never clearly defines what ground truth labels are used. Is it the semi-synthetic injection? If so, this methodology is absent from the paper body (see W1). The reader cannot assess whether these AUROCs are meaningful without knowing the evaluation protocol.
47	
48	**W8. (Minor) References are sparse.** Only 10 references for a paper spanning psychometrics, contamination detection, IRT modeling, ensemble methods, Bayesian updating, and item generation. Key citations are missing: the original MH-DIF literature beyond Holland & Thayer, the student simulation paper (mentioned as arXiv 2601.09953 in the context but not cited), recent benchmark validity work (e.g., Burnell et al., Raji et al.), and foundational IRT texts.
49	
50	---
51	
52	## Questions for Authors
53	
54	1. Where are the experimental details for Claims 2 and 3? The enrichment analysis, semi-synthetic injection framework, ΔTPR methodology, and GSM8K cross-benchmark validation are all absent from §3–§9. Are these intended as separate sections that were omitted for space?
55	
56	2. What explains the remaining ~86% of item instability variance after the decomposition in §3.4? Have you explored item-level predictors (e.g., distractor structure, domain, difficulty level, item format)?
57	
58	3. How sensitive are results to the temporal cutoff? The IFT analysis (§6.1) finds optimal split at 2023-09, yet the main analysis uses a 2023/2024-H1 boundary. Have you verified that the 29.1% C-rate is stable across nearby cutoff choices?
59	
60	4. For the ensemble AUROC (Table 8), what ground truth labels define "contaminated" vs "clean"? If semi-synthetic injection, please describe the injection protocol.
61	
62	5. The bifactor model (§7.1) has RMSEA=0.019 — better than the decoder-only unidimensional model (0.024). Why not use the bifactor model for the primary DIF analysis? Does DIF under a bifactor model yield different flag rates?
63	
64	---
65	
66	## Experiment Coverage Assessment
67	
68	Relative to the full experimental design, the paper covers all 10 planned experiments:
69	- **§3**: architecture_stratified_dif ✓ (load-bearing, well-presented)
70	- **§4**: rl_robustness_validation ✓ (underpowered but present)
71	- **§5.1**: constat_perturbation_eval ✓ (compressed)
72	- **§5.2**: dvd_generation_variance_eval ✓ (compressed)
73	- **§5.3**: ensemble_fusion ✓ (lacks ground truth specification)
74	- **§6.1**: item_focused_trees ✓ (adequate)
75	- **§6.2**: cumulative_bayesian_dif ✓ (simulation, adequate)
76	- **§7.1**: bifactor_irt_equating_pilot ✓ (severely compressed)
77	- **§7.2**: item_generation_calibration ✓ (severely compressed)
78	- **§7.3**: graceful_degradation_analysis ✓ (adequate for the space)
79	
80	However, experiments for two of the four headline claims (web-overlap enrichment analysis, semi-synthetic ΔTPR framework, GSM8K cross-validation) appear to be missing from the paper despite being referenced in the abstract.
81	
82	---
83	
84	## Minor Issues
85	
86	- Table 2: "Total temporal C variance" row with null ρ and p is confusing; clarify what this row represents.
87	- §3.1: N=5,219 in Table 1 vs N=5,227 in abstract — reconcile.
88	- §5.2: DVD cost (58 GPU-hours) is mentioned but ConStat cost is not. Report compute costs consistently.
89	- The paper has no figures — only tables. For a venue submission, at least 2–3 figures would substantially improve readability (e.g., RMSEA improvement scatter, detection power curves, instability decomposition partial regression plot).
90	
91	---
92	
93	## Overall Assessment
94	
95	The core idea — applying psychometric DIF to expose temporal benchmark instability — is novel, important, and well-motivated. The architecture-stratified analysis (§3) is the paper's strongest contribution: rigorous, well-controlled, and yielding a compelling finding (29% instability persists under excellent IRT fit). The instability decomposition, while modest in effect size, adds interpretive value.
96	
97	However, the paper has structural problems that prevent acceptance in its current form. Two of four claimed contributions are absent from the body. The scope is far too broad — attempting to cover 10 experiments in 8 pages results in many sections that are catalogs rather than analyses. The relationship between DIF-detected instability and actual contamination remains unclear, yet the paper's framing implies a strong connection. The reasoning-RL comparison, while interesting, is underpowered.
98	
99	**Recommendation**: Focus the paper on §3 (architecture-stratified DIF) + the missing Claims 2–3 (web-overlap meta-critique and semi-synthetic validation) + §4 (RL robustness with explicit caveats). Move §5–§7 to supplementary material or a follow-up paper. Add a Related Work section and figures. This would yield a focused, rigorous paper with four well-supported claims.
100	
101	---
102	
103	## Scores
104	
105	| Criterion | Score | Justification |
106	|-----------|-------|--------------|
107	| Novelty | 5 | Cross-disciplinary application of DIF to LLM benchmarks is genuinely new |
108	| Soundness | 3 | Core analysis is sound, but missing sections for 2/4 claims; instability decomposition effect size is small; RL comparison underpowered |
109	| Significance | 4 | Important practical implications for benchmark validity; tempered by unclear DIF–contamination relationship |
110	| Clarity | 3 | Clean writing but severe compression; missing sections; no figures; no Related Work |
111	| Completeness | 2 | Two claimed contributions have no experimental sections; most sections lack methodological depth |
112	| Reproducibility | 3 | Uses public METABENCH data (good), but many methodological details are omitted due to compression |
113	
114	**Overall Score: 3 (Weak Reject)**
115	
116	The core contribution is above the bar for a top ML venue, but the current draft's structural incompleteness (missing sections for claimed contributions), scope overextension, and presentational issues require major revision. A focused rewrite concentrating on the strongest 3–4 experiments with full methodological detail would likely reach acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eaee04bc-be68-4d0f-b7e9-ea71fd37d877",
  "isSidechain": true,
  "promptId": "11ffd75c-7a75-4de3-81c2-88dc0db90025",
  "agentId": "ad75a1b970c226edb",
  "type": "user",
  "uuid": "58d6c4f3-e3ba-4fde-bfad-152003ba7c05",
  "sourceToolAssistantUUID": "eaee04bc-be68-4d0f-b7e9-ea71fd37d877",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-21T05:15:51.158Z_

Now I have a comprehensive understanding of the paper. Let me write my review as Reviewer 2, focusing on novelty, significance, related work, and positioning.

---

## ICLR 2026 Review -- Reviewer 2 (R2)

**Paper**: "Temporal Item Instability in LLM Benchmarks: A Large-Scale Differential Item Functioning Analysis of MMLU"

---

### 1. Summary

This paper applies Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis from educational measurement to the METABENCH response matrix (5,227 models x 12,508 MMLU items), finding that 31.3% of items exhibit large temporal DIF (ETS Category C) between 2023 and 2024 model cohorts. The authors argue this instability is predominantly item-specific (not driven by capability gains), that web-overlap contamination labels are fundamentally mismatched as ground truth for differential detectors, and that DIF serves as a diagnostic lens rather than a quality filter. A semi-synthetic injection framework with cross-subject matching validates detection power, and cross-benchmark replication on GSM8K provides partial generalization evidence.

---

### 2. Strengths

**S1. Genuine conceptual contribution in problem formulation.** The paper's most important intellectual contribution is not the MH-DIF procedure itself but the formulation of the *temporal comparability assumption* as a testable psychometric hypothesis. The ML evaluation community largely takes for granted that benchmark scores are comparable across model generations. Framing this as a measurement invariance problem and importing the mature DIF apparatus to test it is a valuable cross-disciplinary insight. The "instability does not equal invalidity" framing (rho ~ 0.997) is nuanced and avoids the trap of over-claiming.

**S2. Unprecedented scale with appropriate controls.** 5,227 models x 12,508 items is by far the largest DIF analysis in any domain, let alone LLM evaluation. The controls are well-chosen: random-split sanity check (0.18%), ability-quintile comparison (2.9%), architecture homogeneity verification (99.98% decoder-only), threshold sensitivity (10-49% across cutoffs), and BH FDR correction (negligible impact). The instability decomposition showing domain improvement explains at most 2.4pp (7.6%) of the 31.3% C% is a particularly careful analysis that preempts the obvious objection.

**S3. The ground truth meta-critique (Claim 2) has genuine field-wide implications.** The observation that web-overlap labels measure global exposure rather than differential contamination, while not a deep theoretical insight, is practically important because the contamination detection literature routinely uses these labels for validation. The empirical demonstration (enrichment = 0.96) combined with the semi-synthetic proof of concept (DTPR = +0.508) makes this a well-supported critique. This is the strongest novelty claim in the paper.

**S4. Cross-subject matching is a useful methodological innovation.** The insight that within-subject matching contaminates the conditioning variable (FPR inflation +0.186) while cross-subject matching achieves DFPR = 0.000 is subtle and practically important. This is a reusable contribution beyond the specific DIF application.

**S5. Thorough and honest limitations section.** The paper is admirably transparent about what DIF does and does not establish. The explicit acknowledgment that DIF detects *that* items changed but not *why*, the caveats about N=33 for the GSM1K correlation, the disclosure of wide confidence intervals, and the frank discussion of RL robustness being empirically unvalidated (N=13) reflect scientific integrity.

**S6. Related work is comprehensive and well-structured.** The five-paragraph Related Work section covers contamination detection, IRT in LLM evaluation, DIF methodology, benchmark design, and LLM evaluation methodology with 40+ citations. The positioning against Growing Pains (complementary: they assume anchor stability, DIF diagnoses which anchors are degrading) is particularly well-articulated.

---

### 3. Weaknesses

**W1. (Major) The core intellectual contribution -- applying MH-DIF without modification to a new dataset -- sits at the boundary of "application" versus "contribution."** The paper explicitly acknowledges that it does not modify the MH-DIF procedure, and the three claimed layers of novelty are: (a) empirical discovery, (b) ground truth critique, (c) validation framework. Of these, (a) is a measurement result on a specific dataset, (b) is an observation about existing validation practice, and (c) is a simulation protocol. None involves algorithmic innovation. The paper argues that "the contribution is the empirical findings, not a new algorithm," which is a legitimate stance -- but the bar for a pure empirical-discovery paper at ICLR is high. The 31% number itself, while striking, is a function of an arbitrary threshold (ETS C at |Delta_MH| >= 1.5) calibrated for human educational testing, not LLM populations. The paper provides threshold sensitivity analysis (10-49% across cutoffs), which is commendable, but this also means the "headline number" is one point on a continuous curve rather than a discrete finding. The novelty claim would be substantially stronger if the paper established why the ETS thresholds, developed for human examinees with sample sizes of hundreds to low thousands, are meaningful for an LLM population of 5,227 heterogeneous models.

**W2. (Major) The causal interpretation of DIF flags is fundamentally ambiguous, and this ambiguity limits significance.** The paper correctly states that DIF detects *that* items function differently across cohorts, not *why*. But the entire narrative arc -- from the title referencing "instability" to the GSM1K anti-correlation to the model family diagnostic profiles -- implicitly suggests that DIF captures something pathological about benchmark items. The paper says "diagnostic, not destructive," but the framing throughout treats DIF-C items as problematic. The 31% instability could equally reflect: (i) legitimate capability emergence in specific knowledge areas, (ii) changes in distractor sensitivity due to different RLHF procedures, (iii) spurious correlations between model release date and training data composition, or (iv) actual differential contamination. The paper's decomposition analysis rules out (i) at the *domain* level but not at the *item* level -- an item could become easier for 2024 models because they genuinely became better at that specific type of reasoning, not because of contamination. The inability to distinguish these causes limits the actionability of the findings.

**W3. (Major) The GSM1K anti-correlation (r = -0.478) is presented as a key validation result but has serious interpretive problems.** First, N=33 is very small, and the 95% CI [-0.71, -0.16] spans a wide range from moderate to large effects. Second, the direction was opposite to the original hypothesis (the authors expected a positive correlation), and the post-hoc interpretation ("DIF items resist contamination-based gains") is unfalsifiable -- any direction of correlation could be rationalized. Third, the correlation is between two aggregate model-level scores (contamination gap and DIF ranking advantage), which are both functions of the same underlying response matrix, introducing shared variance that inflates the correlation. Fourth, the partial correlation controlling for overall accuracy (r = -0.385, p = 0.030) has a CI upper bound of -0.058, barely excluding zero. This result should be described as exploratory, not confirmatory.

**W4. (Moderate) Missing engagement with prior psychometric work on LLM evaluation that directly relates to DIF.** While the paper cites IRT-LLM, Growing Pains, PSN-IRT, and others, it does not adequately engage with prior work that has studied *measurement invariance* or *item stability* in ML evaluation contexts. Specifically:

- Polo et al. (2024, tinyBenchmarks) select representative items using IRT -- their item selection implicitly assumes temporal stability, which the current paper challenges. The paper should discuss whether tinyBenchmarks' selected items are disproportionately DIF-flagged.
- The DIF methodology literature is cited extensively (Holland & Thayer, Clauser & Mazor, Swaminathan & Rogers, etc.), but the paper does not discuss *why* MH-DIF was chosen over logistic regression DIF or SIBTEST for the primary analysis. Given the large N (5,227) and the potential for non-uniform DIF in LLM populations, logistic regression DIF would seem more appropriate as the primary method, with MH as a robustness check. The choice of MH appears driven by simplicity rather than principled selection.
- Raju (1988) area measures and Lord's chi-square are cited but never used or discussed as alternatives that might provide different conclusions.

**W5. (Moderate) The semi-synthetic injection framework (Claim 3), while technically sound, is not sufficiently novel.** Injection-based validation -- flipping responses from incorrect to correct to simulate contamination and measuring detection power -- is a standard evaluation protocol in the contamination detection literature. ConStat uses perturbation-based validation, and numerous studies use synthetic injection to establish detection baselines. The specific innovation here is the cross-subject matching protocol (DFPR = 0.000), which is a useful practical contribution but does not constitute a major methodological advance. The paper overweights this as a standalone contribution.

**W6. (Moderate) The "benchmark redundancy" finding (rho ~ 0.997) undercuts the practical significance of the other claims.** If removing 31% of items changes essentially nothing about model rankings, then the instability is, by the paper's own metric, inconsequential for the primary use case of benchmarks (ranking models). The paper tries to have it both ways: the instability is large enough to be a "finding" (31%!) but small enough to be "not destructive" (rho ~ 0.997). This tension is intellectually honest but raises questions about practical significance. Who should care about item-level instability that does not affect any downstream decision? The "diagnostic lens" framing is an attempt to answer this, but the diagnostic value is limited by the causal ambiguity noted in W2.

**W7. (Minor) The Llama-2 vs. Llama-3 within-family comparison (61.3% C%) is presented as a bracketing analysis, but it actually raises concerns about the method.** The authors attribute the 61.3% to "ability differences confounding the DIF signal." But this is exactly the problem: MH-DIF conditions on total score, which should control for ability differences. If ability differences between Llama-2 and Llama-3 produce 61.3% C% despite conditioning, this suggests that the MH conditioning is insufficient when ability gaps are large -- which is precisely the situation in temporal cohorts (2023 models are generally weaker than 2024 models). The paper's 31.3% temporal C% may therefore still be inflated by residual ability confounding that the MH procedure does not fully remove.

---

### 4. Questions for Authors

1. The ETS A/B/C thresholds were developed for human educational testing with typical sample sizes of 500-5,000. What is the justification for applying these thresholds to an LLM population of 5,227 highly heterogeneous models? Have you considered calibrating thresholds empirically for this population (e.g., using the random-split null distribution)?

2. The within-family Llama-2 vs. Llama-3 comparison yields 61.3% C%, attributed to ability confounding. But the ability-quintile comparison within the same temporal window yields only 2.9%. These two results seem contradictory: both involve ability differences, yet the rates differ by 20x. What explains this discrepancy? Is it that within-family comparisons have correlated item-level response patterns that amplify DIF, independent of ability?

3. Why was MH-DIF chosen over logistic regression DIF as the primary method? Logistic regression naturally handles non-uniform DIF and provides effect sizes (Nagelkerke R-squared) that may be more interpretable for this population. Was logistic regression DIF computed at all?

4. The GSM1K correlation was originally hypothesized to be positive but turned out negative. Can you provide a pre-registered or a priori justification for why the negative direction is meaningful, rather than a post-hoc narrative?

5. The paper states that domain improvement explains at most 2.4pp of 31.3% C% at the item level. But could item-level capability improvement (not domain-level) explain a larger fraction? Items testing reasoning chains, multi-step inference, or world knowledge that improved between 2023 and 2024 might show DIF without any contamination. Have you controlled for item-level properties beyond difficulty and discrimination (e.g., reasoning depth, question format, answer position)?

6. What fraction of the 5,227 models are fine-tunes, merges, or quantizations of a small number of base models? If the "model population" is actually 50 independent base models with hundreds of derivative variants, the effective sample size for DIF is much smaller than 5,227, and the statistical significance of the MH tests may be inflated.

---

### 5. Missing Related Work

**5a. Measurement invariance in NLP/ML evaluation.** The paper frames DIF as a measurement invariance test but does not cite the substantial body of work on measurement invariance testing in psychology using CFA (beyond the general Meredith 1993 and Vandenberg 2000 citations). More importantly, the paper should discuss whether multi-group CFA invariance testing (configural/metric/scalar) has been applied to LLM benchmark data, and if not, why DIF is preferred over the CFA framework.

**5b. Item parameter drift in computerized adaptive testing (CAT).** The educational measurement literature has extensive work on detecting item parameter drift over time -- exactly the phenomenon this paper studies. Key references include Veerkamp & Glas (2000, "Detection of item parameter drift"), Bock et al. (1988), and Wells et al. (2002). These methods are directly relevant and should be discussed as alternatives to MH-DIF for temporal analysis.

**5c. Benchmark dynamics and temporal analysis.** Dehghani et al. (2021, "The Benchmark Lottery") and Ethayarajh & Jurafsky (2020, "Utility is in the Eye of the User") discuss how benchmark rankings depend on item composition and evaluation choices, which is closely related to the redundancy finding. Koch et al. (2021) study temporal trends in NLP evaluation.

**5d. Data contamination beyond web-overlap.** Sainz et al. (2023, "Did ChatGPT cheat on your test?") and Jacovi et al. (2023) discuss contamination through indirect channels (synthetic data, distillation) that web-overlap labels cannot capture -- directly relevant to the ground truth meta-critique.

**5e. Concurrent work on IRT-based benchmark analysis.** Song et al. (2025, "BenchMAX") and similar concurrent works applying IRT to benchmark analysis should be discussed and differentiated.

---

### 6. Minor Issues

- The abstract and conclusion sections are placeholders in the submitted draft. This is a significant presentation gap.
- Table 1: The enrichment column for within-family and random-split rows shows "--" without explanation.
- The paper uses "C%" as shorthand without defining it in a notation table.
- Section 4.5 references "21 experimental conditions" without specifying what they are.
- The partial R-squared for domain improvement (0.0007) is extremely small. Reporting this as "pseudo R-squared" without specifying which pseudo R-squared (McFadden, Cox-Snell, Nagelkerke) limits interpretability.
- Figure 1 (global vs. differential ICC diagram) is conceptually helpful but should include actual ICC curves from the data rather than schematic illustrations.
- The paper should report confidence intervals for the 31.3% C% estimate itself. Is there uncertainty from the choice of temporal cutoff, model inclusion criteria, or item subsampling?

---

### 7. Preliminary Scores

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | 3 | Core MH-DIF analysis is technically correct; controls are well-designed; but causal ambiguity (W2), the GSM1K post-hoc interpretation (W3), and residual ability confounding (W7) leave meaningful gaps in the inferential chain. |
| **Presentation** | 2 | Missing abstract and conclusion; the main body is well-written where it exists, but placeholder sections in a submission are a serious presentation failure. Related work section is strong. |
| **Contribution** | 2 | The cross-disciplinary framing (S1) and ground truth meta-critique (S3) are genuine contributions, but applying an unmodified 1988 procedure to a new dataset, with the primary finding being a percentage (31%) that depends on a threshold calibrated for a different population, falls below the novelty bar for ICLR. The practical significance is undercut by the redundancy finding (W6). The semi-synthetic framework is incremental (W5). |
| **Overall** | 4 -- Marginally below acceptance threshold (weak reject) | The paper tackles an important problem and demonstrates scientific rigor in its controls and honest limitations. The ground truth meta-critique and the temporal comparability framing are valuable. However, the novelty is primarily empirical-observational rather than methodological, the 31% finding's significance depends on thresholds not calibrated for LLMs, the GSM1K validation is underpowered and post-hoc, the causal interpretation of DIF flags remains fundamentally ambiguous, and placeholder sections indicate an incomplete manuscript. A revision addressing the threshold calibration question (Q1), the ability confounding concern (W7/Q2), and completing the manuscript would strengthen the paper. |
| **Confidence** | 4 | I am familiar with both the DIF/psychometric methodology and the LLM evaluation literature. My main uncertainty is whether the ML evaluation community values pure empirical-discovery contributions at this level, which is a venue-fit judgment rather than a technical one. |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58d6c4f3-e3ba-4fde-bfad-152003ba7c05",
  "isSidechain": true,
  "agentId": "ad75a1b970c226edb",
  "requestId": "req_011CbF9EbEcvTDy2ptj7qyDV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e23f3fff-fddb-4209-916b-2794bb06c86c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f47ef9e2-3bdc-4328-afa5-da8117d03f95",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bh3ZsRoxyJA3YfiJ1qURpv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3635,
      "cache_read_input_tokens": 59405,
      "output_tokens": 4277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3635
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4277,
          "cache_read_input_tokens": 59405,
          "cache_creation_input_tokens": 3635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3635,
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
