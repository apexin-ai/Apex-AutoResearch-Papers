# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus is **Novelty and Related Work**. Review the paper below ri

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a43ea8d08ff36c575.jsonl`
- **Structured JSON:** [`de79277423684079452f.json`](../../sessions/de/de79277423684079452f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-21T02:08:06.682Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus is **Novelty and Related Work**. Review the paper below rigorously against a top ML venue standard (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

## Paper Summary

**Title:** "Psychometric Characterization of Item-Level Instability in LLM Benchmarks via Differential Item Functioning"

The paper applies Differential Item Functioning (DIF) — a classical psychometric method — to the METABENCH response matrix (5,227 models × 12,508 MMLU items) to characterize item-level behavioral drift across model generations. It defines temporal cohorts (pre-2024 reference vs 2024-H1 focal) and uses the Mantel-Haenszel χ² procedure with ETS effect-size classification.

**4 Core Claims:**
1. **38% of MMLU items are functionally unstable** (ETS C category, |Δ_MH|≥1.5) across model generations. Per-subject C% ranges 31-45%. Random-split sanity check: C%=0.18%. Capability improvement confound: ρ=0.307 between C% and domain accuracy gains. The paper frames this as a "mixture" that cannot be decomposed.
2. **Methodological gap in contamination detection validation**: web-overlap labels (Li et al.) measure global item exposure, not differential functioning. Enrichment ≈1.0 between DIF flags and web-overlap labels.
3. **Semi-synthetic validation framework**: Injects differential contamination into real response matrices, measures ΔTPR. Cross-subject matching eliminates FPR inflation (ΔFPR=0.000). Cross-benchmark replication on GSM8K (ΔTPR=+0.818).
4. **DIF as diagnostic lens**: ρ≈0.997 after removing 31% DIF items (measurement redundancy). DIF items carry disproportionate discriminative signal (z=−8 to −49σ). GSM1K cross-benchmark evidence (r=−0.478, p=0.005, N=33) is "suggestive."

**Robustness Analyses (Section 5):**
- Architecture-Stratified DIF: C% drops 31.3%→28.2% for decoder-only subset.
- Item-Focused Trees: Continuous treatment of release date. Jaccard=0.72 with categorical MH.
- Reasoning-RL Robustness: N=13 reasoning-RL models. DIF flag retention 86%. DeLong p=0.087, TOST p=0.11. "Preliminary."
- Graceful Degradation: Progressive replacement 5-50%. ρ=0.972 at 50%.
- Cumulative Bayesian DIF: Simulation-only. Power 0.41→0.74 over 4 administrations.

**Complementary Baselines (Section 6):**
- ConStat perturbation testing (248 items, 15 models)
- Generation Variance Detection / DVD (300 items, 12 models)
- Multi-signal ensemble: negative result (AUROC 0.66 vs best individual 0.62)

**Pilot Studies (Section 7):**
- Bifactor IRT Equating: CFI=0.87, equated ρ=0.93 (below 0.95 target)
- LLM Item Generation: Difficulty ρ=0.64, holdout ρ=0.58. 187 GPU-hours for 200 items.

**Key limitations acknowledged:**
- Unidimensional IRT is a simplification for 57-subject MMLU
- Semi-synthetic injection (bit-flipping) is simplified contamination model
- GSM1K evidence N=33
- RL robustness N=13 is underpowered
- Bayesian DIF is simulation-only
- Pilot studies are not production-ready

## Your Review Task

Evaluate the following dimensions in depth:

### 1. Novelty Assessment
- DIF has been used in educational testing for 40+ years. What is genuinely new here beyond applying an existing method to a new domain (LLM benchmarks)?
- Is the application itself sufficiently non-trivial to constitute a contribution? Does the scale (5,227 models × 12,508 items) create novel challenges addressed by the paper?
- The semi-synthetic validation framework with cross-subject matching — is this a meaningful methodological contribution or an obvious extension?
- The "measurement efficiency, not validity crisis" reframing — is this an insight or a tautology given MMLU's known redundancy?
- How does this compare to simply subsetting items and re-scoring? Is the psychometric framing necessary?

### 2. Related Work Coverage
The paper references DIF literature (Holland & Thayer), METABENCH, and contamination detection methods (ConStat, Min-K%, n-gram overlap, Li et al.). Evaluate:
- Are key related works in LLM benchmark analysis cited? (e.g., benchmark contamination studies, benchmark design papers, recent IRT applications to LLMs)
- Is the positioning against contamination detection methods fair? The paper argues DIF measures something different — is this convincingly established?
- Are there psychometric methods beyond DIF that should be discussed (e.g., measurement invariance testing via MGCFA, Rasch model approaches)?
- How does this relate to concurrent work on benchmark quality, dynamic benchmarks, or adaptive testing for LLMs?
- Note: the paper uses [?] for several citations — this appears to be an anonymized submission artifact.

### 3. Contribution Significance
- Who benefits from this work and how? Benchmark designers? Model developers? The evaluation community?
- Are the findings actionable? The paper identifies 38% unstable items but ρ=0.997 suggests removing them doesn't matter. What should practitioners do?
- The pilot studies (Sections 7.1, 7.2) promise benchmark regeneration but deliver pilot-level results. Does this strengthen or weaken the paper?
- Is this positioned correctly? Could it be a stronger paper with fewer claims?

### 4. Presentation and Framing
- Is the paper well-organized? 9 sections is dense for a 9-page paper.
- Are the claims appropriately calibrated to the evidence?
- The tension between "38% instability" (alarming) and "ρ=0.997 redundancy" (reassuring) — is this handled well?

### Output Format
Provide your review as:

**Summary:** 2-3 sentences on what the paper does.

**Strengths:** Bulleted list (S1, S2, ...) with specific evidence.

**Weaknesses:** Bulleted list (W1, W2, ...) with specific evidence and severity (minor/moderate/major).

**Questions for Authors:** Numbered list of clarification questions.

**Missing Related Work:** Specific papers or research directions that should be cited/discussed.

**Preliminary Score:** X/6 with one-sentence justification.

**Confidence:** 1-5 scale.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "b4bcc60b-9424-4d7d-b588-2f55afd7b8cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T02:08:06.685Z_

```json
{
  "parentUuid": "b4bcc60b-9424-4d7d-b588-2f55afd7b8cd",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
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
  "uuid": "6b0c6377-17b9-4967-a719-f8869c76ccdf",
  "timestamp": "2026-05-21T02:08:06.685Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T02:08:09.521Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b0c6377-17b9-4967-a719-f8869c76ccdf",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu4yEJEovffb9Hady6w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32e26828-b9d0-4ca4-8709-c1a5f182d257",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K32gNP3NcXkn4KfNTh7Gaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7666,
      "cache_read_input_tokens": 8254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7666,
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

_source line 4 · 2026-05-21T02:08:13.916Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MGYZqcYq8vKRAskbv4e6jR`</summary>

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
  "parentUuid": "32e26828-b9d0-4ca4-8709-c1a5f182d257",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu4yEJEovffb9Hady6w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7222816b-e361-46fd-9d1b-e17993d35b1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K32gNP3NcXkn4KfNTh7Gaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7666,
      "cache_read_input_tokens": 8254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7666,
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

_source line 5 · 2026-05-21T02:08:13.923Z_

<details><summary>↩ Tool result · `toolu_01MGYZqcYq8vKRAskbv4e6jR`</summary>

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
  "parentUuid": "7222816b-e361-46fd-9d1b-e17993d35b1d",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "262c6448-4511-4e4e-834f-5aad6a71211b",
  "sourceToolAssistantUUID": "7222816b-e361-46fd-9d1b-e17993d35b1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T02:08:18.214Z_



Let me read the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "262c6448-4511-4e4e-834f-5aad6a71211b",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu5Wh93WbLV7HVcmGLk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a02ede01-a77c-4cf8-9bb5-966dbdba56b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Nnk94J3iQBequJSHXu2Zg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 7 · 2026-05-21T02:08:19.802Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PWhjtb4DdTyACDmZMcoEmY`</summary>

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
  "parentUuid": "a02ede01-a77c-4cf8-9bb5-966dbdba56b3",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu5Wh93WbLV7HVcmGLk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1a57084-992c-4321-a2de-bfe344e0dcf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Nnk94J3iQBequJSHXu2Zg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 8 · 2026-05-21T02:08:19.815Z_

<details><summary>↩ Tool result · `toolu_01PWhjtb4DdTyACDmZMcoEmY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\\n\\n## 近期结论\\n- **plan_004_gsm8k_cross_benchmark** (negative): GSM8K 的 temporal DIF (2023 vs 2024) 将展示与 MMLU 类似的 30-40% ETS C%，证明 temporal DIF 现象跨 benchmark 泛化。使用 METABENCH 其他 benchmarks 总分做 external matching（GSM8K 无 subject 分层），预期 baseline FPR 更可控。如果 C% 在同一量级 → DIF 作为 benchmark health diagnostic 的泛化性得到验证。 ← 基于 plan_001_real_data_dif_mmlu\\n- **plan_017_downstream_impact** (negative): 移除 temporal DIF-flagged items (ETS C, ~31% of MMLU items) 后，模型跨代排名更稳定（Spearman ρ 提升），且稳定性提升显著优于随机移除相同数量 items 的 baseline。这证明 DIF 不只标记 noise，而是精确识别了 problematic items，为 DIF 作为 benchmark quality tool 提供 downstream evidence。 ← 基于 plan_001_real_data_dif_mmlu\\n- **plan_016_within_subject_semi_synthetic** (success): 在 subject 内部使用 within-subject total score 做 MH 分层的 semi-synthetic injection 中，DIF 仍能检测差异性污染（ΔTPR > 0.3 at p=0.5）。这证明 DIF 方法在 subject 级别也有效，plan_014 的 38% within-subject C% 反映的是真实代际能力差异而非方法失败。 ← 基于 plan_014_within_subject_dif\\n  [plan_016_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md) | [plan_016_dose_response](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response.csv) | [plan_016_revised_dose_response](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response_e6d86f.csv) | [plan_016_revised_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md)\\n\\n## 趋势\\n成功 5 / 负向 6 / 失败 0 / 共 11\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 2009, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1a57084-992c-4321-a2de-bfe344e0dcf3",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "5f313a16-c1dc-4576-928e-976657f3f938",
  "sourceToolAssistantUUID": "b1a57084-992c-4321-a2de-bfe344e0dcf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T02:08:20.449Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Xd5SArhskwUKUjTYkcsZvN`</summary>

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
  "parentUuid": "5f313a16-c1dc-4576-928e-976657f3f938",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu5Wh93WbLV7HVcmGLk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f17b07de-9a39-400b-a14e-e4d83b853ed4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Nnk94J3iQBequJSHXu2Zg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 10 · 2026-05-21T02:08:20.463Z_

<details><summary>↩ Tool result · `toolu_01Xd5SArhskwUKUjTYkcsZvN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml\", \"content\": \"categories:\\n- key: contamination_detection\\n  name: Benchmark Contamination Detection\\n  narrative: Methods for detecting training data contamination in LLM benchmarks,\\n    including RL-robust approaches\\n- key: irt_equating\\n  name: IRT Methodology & Equating\\n  narrative: Item Response Theory models, calibration, equating, and their application\\n    to LLM evaluation\\n- key: benchmark_design\\n  name: Dynamic Benchmark Design\\n  narrative: Approaches for creating contamination-resistant or self-updating benchmarks\\n- key: dif_methodology\\n  name: DIF Statistical Methods\\n  narrative: Differential Item Functioning detection methods, power analysis, and\\n    small-sample strategies\\n- key: item_generation\\n  name: Automated Item Generation\\n  narrative: LLM-based test item generation with difficulty control and psychometric\\n    validation\\nmeta:\\n  last_updated: '2026-05-21T01:40:38.004Z'\\n  total_papers: 16\\npapers:\\n  belzak2020smallsample:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Belzak, W.\\n    bibtex_key: belzak2020smallsample\\n    category: dif_methodology\\n    doi: ''\\n    relevance: Parsimonious logistic regression with sum scores outperforms complex\\n      IRT models for DIF detection in small samples; directly applicable to our N=50-80\\n      model cohorts\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Testing Differential Item Functioning in Small Samples\\n    url: ''\\n    venue: Multivariate Behavioral Research\\n    verified: false\\n    year: 2020\\n  hardy2026scalability:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Hardy, M.\\n    bibtex_key: hardy2026scalability\\n    category: irt_equating\\n    doi: ''\\n    relevance: Nonparametric signed isotonic R2 scalability coefficients outperform\\n      IRT item diagnostics; lightweight pre-filter for item quality before our parametric\\n      calibration\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients\\n    url: https://arxiv.org/abs/2603.24999\\n    venue: arXiv\\n    verified: false\\n    year: 2026\\n  kim2019fpc:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Kim, S.\\n    - Kolen, M.\\n    bibtex_key: kim2019fpc\\n    category: irt_equating\\n    doi: ''\\n    relevance: Fixed-parameter calibration requires only N>=200 vs N>=500 for full\\n      calibration; core methodology for our bifactor IRT equating with anchor items\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data\\n    url: ''\\n    venue: Applied Measurement in Education\\n    verified: false\\n    year: 2019\\n  liang2026dvd:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Liang, R.\\n    bibtex_key: liang2026dvd\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Detects variant contamination via generation variance (AUC 0.73-0.74\\n      vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under\\n      RL training\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'DVD: Detection via Variance of Generation Distribution for Variant Contamination'\\n    url: https://arxiv.org/abs/2601.04895\\n    venue: arXiv\\n    verified: true\\n    year: 2026\\n  polo2026growingpains:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Polo, F.\\n    bibtex_key: polo2026growingpains\\n    category: irt_equating\\n    doi: ''\\n    relevance: Uses multidimensional IRT with fixed-parameter calibration and 100\\n      anchor items for extensible evaluation (rho>=0.9); addresses score comparability\\n      but NOT contamination detection or item regeneration\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter\\n      Calibration'\\n    url: ''\\n    venue: arXiv\\n    verified: false\\n    year: 2026\\n  polo2026psnirt:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Polo, F.\\n    bibtex_key: polo2026psnirt\\n    category: irt_equating\\n    doi: ''\\n    relevance: PSN-IRT analyzes benchmark quality via 4PL IRT; provides published\\n      IRT parameters for MMLU we can use in semi-synthetic validation\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item\\n      Response Theory\\n    url: ''\\n    venue: AAAI 2026\\n    verified: false\\n    year: 2026\\n  tao2026selfcritique:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Tao, Y.\\n    bibtex_key: tao2026selfcritique\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse\\n      detection, but remains individual-model-level; our DIF is group-level and complementary\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: Detecting Data Contamination from Reinforcement Learning Post-training\\n      for Large Language Models\\n    url: https://arxiv.org/abs/2510.09259\\n    venue: ICLR 2026\\n    verified: true\\n    year: 2026\\n  wang2026fragility:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Wang, H.\\n    - Li, H.\\n    - Ko, B.\\n    - Zhang, H.\\n    bibtex_key: wang2026fragility\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Proves GRPO/PPO RL training conceals contamination signals (14-20pp\\n      AUROC degradation), motivating our DIF-based approach which operates on behavioral\\n      patterns immune to NLL smoothing\\n    role: foundation\\n    semantic_scholar_id: 9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3\\n    title: On The Fragility of Benchmark Contamination Detection in Reasoning Models\\n    url: https://arxiv.org/abs/2510.02386\\n    venue: ICLR 2026\\n    verified: true\\n    year: 2026\\n  white2025livebench:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - White, C.\\n    bibtex_key: white2025livebench\\n    category: benchmark_design\\n    doi: ''\\n    relevance: Monthly-updated contamination-free benchmark with objective scoring;\\n      no difficulty calibration or psychometric equivalence across updates\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'LiveBench: A Challenging, Contamination-Free LLM Benchmark'\\n    url: ''\\n    venue: ICLR 2025\\n    verified: false\\n    year: 2025\\n  zhang2024gsm1k:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Zhang, H.\\n    bibtex_key: zhang2024gsm1k\\n    category: contamination_detection\\n    doi: ''\\n    relevance: GSM1K documents 10-13% average accuracy drops from contamination; provides\\n      ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4\\n      logits) critical for our DIF power analysis\\n    role: foundation\\n    semantic_scholar_id: ef62f95c16f668f031d649799cbd79081c6d2b0f\\n    title: A Careful Examination of Large Language Model Performance on Grade School\\n      Arithmetic\\n    url: https://arxiv.org/abs/2405.00332\\n    venue: arXiv\\n    verified: true\\n    year: 2024\\n  li2024contamination:\\n    title: An Open-Source Data Contamination Report for Large Language Models\\n    authors:\\n    - Li, Y.\\n    - Guo, Y.\\n    - Guerin, F.\\n    - Lin, C.\\n    year: 2024\\n    venue: Findings of EMNLP 2024\\n    url: https://aclanthology.org/2024.findings-emnlp.30/\\n    doi: 10.18653/v1/2024.findings-emnlp.30\\n    bibtex_key: li2024contamination\\n    category: contamination_detection\\n    role: foundation\\n    relevance: Provides web-overlap contamination labels for MMLU and other benchmarks\\n      via Common Crawl matching; primary ground-truth comparison for our DIF-based\\n      contamination detection\\n    abstract: ''\\n    semantic_scholar_id: 32e11cf020021c225782a3b77b5cfed4ae8e14a0\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  shi2024mink:\\n    title: Detecting Pretraining Data from Large Language Models\\n    authors:\\n    - Shi, W.\\n    - Ajith, A.\\n    - Xia, M.\\n    - Huang, Y.\\n    - Liu, D.\\n    - Blevins, T.\\n    - Chen, D.\\n    - Zettlemoyer, L.\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2310.16789\\n    doi: ''\\n    bibtex_key: shi2024mink\\n    category: contamination_detection\\n    role: foundation\\n    relevance: Introduces Min-K% Prob method and WikiMIA benchmark for pretraining\\n      data detection; key baseline whose limitations under RL training motivate our\\n      DIF-based alternative\\n    abstract: ''\\n    semantic_scholar_id: 3422d5e0cdfdc935d6a84a1e3d3f96659265fe3a\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  balloccu2024leak:\\n    title: 'Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in\\n      Closed-Source LLMs'\\n    authors:\\n    - Balloccu, S.\\n    - Schmidtova, P.\\n    - Lango, M.\\n    - Dusek, O.\\n    year: 2024\\n    venue: EACL 2024\\n    url: https://arxiv.org/abs/2402.03927\\n    doi: 10.18653/v1/2024.eacl-long.5\\n    bibtex_key: balloccu2024leak\\n    category: contamination_detection\\n    role: foundation\\n    relevance: Systematic survey of data leakage in closed-source LLMs covering 255\\n      papers and 263 benchmarks; establishes scope of contamination problem motivating\\n      our detection approach\\n    abstract: ''\\n    semantic_scholar_id: 798feda076ad710df65d509a7884bd15937c8056\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  dekoninck2024constat:\\n    title: 'ConStat: Performance-Based Contamination Detection in Large Language Models'\\n    authors:\\n    - Dekoninck, J.\\n    - Mueller, M. N.\\n    - Vechev, M.\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: https://arxiv.org/abs/2405.16281\\n    doi: ''\\n    bibtex_key: dekoninck2024constat\\n    category: contamination_detection\\n    role: direct-competitor\\n    relevance: Performance-based contamination detection via perturbation analysis;\\n      closest methodological parallel to our DIF approach in using behavioral patterns\\n      rather than memorization signals\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  golchin2024timetravel:\\n    title: 'Time Travel in LLMs: Tracing Data Contamination in Large Language Models'\\n    authors:\\n    - Golchin, S.\\n    - Surdeanu, M.\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2308.08493\\n    doi: ''\\n    bibtex_key: golchin2024timetravel\\n    category: contamination_detection\\n    role: method-component\\n    relevance: Instance-level contamination detection via guided completion prompts;\\n      baseline approach for individual-item detection that our group-level DIF method\\n      extends\\n    abstract: ''\\n    semantic_scholar_id: d6d0fd994f37b630f35945736b5e1bb198148404\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  zhang2024minkpp:\\n    title: 'Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large\\n      Language Models'\\n    authors:\\n    - Zhang, J.\\n    - Sun, J.\\n    - Yeats, E.\\n    - Ouyang, Y.\\n    - Kuo, M.\\n    - Zhang, J.\\n    - Yang, H.\\n    - Li, H.\\n    year: 2024\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2404.02936\\n    doi: ''\\n    bibtex_key: zhang2024minkpp\\n    category: contamination_detection\\n    role: direct-competitor\\n    relevance: Improves Min-K% with vocabulary-normalized token probabilities; key\\n      baseline whose AUC degrades to 0.43-0.68 on RL-trained models, motivating our\\n      DIF-based alternative\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n\", \"total_chars\": 11927, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f17b07de-9a39-400b-a14e-e4d83b853ed4",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "cda0bb4b-656e-406b-a48b-f0ca57397daf",
  "sourceToolAssistantUUID": "f17b07de-9a39-400b-a14e-e4d83b853ed4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T02:08:20.972Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KwLVbY4cqETj7fjNATzQLp`</summary>

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
  "parentUuid": "cda0bb4b-656e-406b-a48b-f0ca57397daf",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu5Wh93WbLV7HVcmGLk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aff620ef-5547-4b31-9e4f-89f912d1c460",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Nnk94J3iQBequJSHXu2Zg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 12 · 2026-05-21T02:08:20.988Z_

<details><summary>↩ Tool result · `toolu_01KwLVbY4cqETj7fjNATzQLp`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aff620ef-5547-4b31-9e4f-89f912d1c460",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "15e35db3-d484-4b35-a57e-f86607ced401",
  "sourceToolAssistantUUID": "aff620ef-5547-4b31-9e4f-89f912d1c460",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T02:08:26.560Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018Tt6J2xovZfTDMhMLYusFs`</summary>

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
  "parentUuid": "15e35db3-d484-4b35-a57e-f86607ced401",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu634kjcQM9QsgL9wjE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf34d110-c72c-4cc2-b079-2e98923fb0dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sHp5Zf633tXAVMvegY23m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5996,
      "cache_read_input_tokens": 17367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5996,
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

_source line 14 · 2026-05-21T02:08:26.578Z_

<details><summary>↩ Tool result · `toolu_018Tt6J2xovZfTDMhMLYusFs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md\", \"content\": \"# Paper Framing — irt_equated_bench_regen\\n\\n## Target Venue\\n- Primary: ICLR 2027 (expected deadline ~October 2026)\\n\\n## Paper Type\\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \\\"DIF reveals benchmark structural problems,\\\" not \\\"DIF detects contamination.\\\"\\n\\n## Core Claims (4 条, 可证伪)\\n\\n**Claim 1 (Temporal Comparability Concern)**: 38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. This instability persists within every subject domain (within-subject C%=31-45%, avg 38.1%), is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). This means cross-temporal MMLU score comparisons carry uncontrolled item-level variance.\\n- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%)\\n- Honesty requirement: ρ=0.307 means \\\"item instability\\\" may mainly reflect \\\"models got better at those domains\\\" — we cannot decompose 38% into contamination vs capability improvement\\n\\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\\n- Framing: aggressive — \\\"the field's standard validation approach is fundamentally mismatched for item-level detection\\\"\\n\\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\\n\\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\\n2. **DIF items = discriminative signal carriers**: DIF removal causes significantly MORE ranking disruption than random removal (z=-8 to -49σ, 21/21 conditions). DIF items carry 1.09× cross-cohort accuracy swing vs 0.96× for stable items — they concentrate the information that differentiates model generations.\\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \\\"find bad items and remove\\\" but \\\"understand what changed and why.\\\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\\n4. **Cross-benchmark validation — DIF captures capability, not contamination**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005; partial r=−0.385 controlling accuracy; permutation p=0.014). Contaminated models (high GSM8K-GSM1K gap: Phi, Gemma families) perform WORSE on DIF items. DIF captures genuine capability-discriminative items that contamination cannot fake — contamination produces shallow performance gains concentrated on non-DIF items. N=33 matched models, leave-one-out robust (min |r|=0.374).\\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_004 Step 3 (r=−0.478, p=0.005, 33 models)\\n- Growing Pains互补: \\\"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\\\" — mutual value positioning\\n- Caveats (→ limitations): super-family analysis limited to N≥20 families; GSM1K validation N=33 (CI wide); contamination gap is proxy, not ground truth\\n\\n## Story Spine\\n\\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \\\"Model B outperforms Model A on MMLU,\\\" we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.\\n\\n**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\\n\\n**What we find**: Three discoveries, each a contribution:\\n\\n1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.\\n\\n2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.\\n\\n3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.\\n\\n4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K confirms: DIF flags anti-correlate with contamination (r=−0.478, p=0.005) — contaminated models can't fake performance on DIF items, which capture genuine capability differences. DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.\\n\\n**Headline result**: \\\"Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF flags anti-correlate with contamination (r=−0.478, p=0.005): DIF captures genuine capability-discriminative items that contamination cannot replicate. We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000).\\\"\\n\\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\\n\\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\\n\\n## Venue Fit\\n\\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\\n- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 38% instability, (2) the ground truth meta-critique affecting the field, (3) the semi-synthetic framework. Frame as \\\"bringing mature psychometric tools to characterize an urgent ML evaluation problem.\\\"\\n\\n## Anticipated Reviewer Concerns (updated for pivot)\\n\\n1. **\\\"38% could just mean models got better\\\"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.\\n\\n2. **\\\"Ground truth critique is obvious — of course web labels don't capture differential effects\\\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\\n\\n3. **\\\"Semi-synthetic injection is artificial\\\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\\n\\n4. **\\\"DIF power is only sufficient for large effects\\\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\\n\\n5. **\\\"Only validated on MMLU\\\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\\n\\n6. **\\\"Higher methods (MIMIC, propensity-score) could solve the confounding\\\"** — Acknowledged as future work. We frame our three-attempt negative results as \\\"empirical observation\\\" that motivates these directions, not as impossibility.\\n\\n## Dropped from Original Framing\\n\\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\\n- **Detection as primary contribution**: Pivoted from \\\"we detect contamination\\\" to \\\"we characterize benchmark properties.\\\"\\n\", \"total_chars\": 11796, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf34d110-c72c-4cc2-b079-2e98923fb0dd",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "cd23f364-2ebe-453b-8890-f9d9f20aaae3",
  "sourceToolAssistantUUID": "cf34d110-c72c-4cc2-b079-2e98923fb0dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T02:08:27.350Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Nfvh8mAAuPXHuStTpVz3dn`</summary>

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
  "parentUuid": "cd23f364-2ebe-453b-8890-f9d9f20aaae3",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu634kjcQM9QsgL9wjE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62b6b5e2-ae60-44b0-af98-255e3c63a363",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sHp5Zf633tXAVMvegY23m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5996,
      "cache_read_input_tokens": 17367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5996,
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

_source line 16 · 2026-05-21T02:08:27.375Z_

<details><summary>↩ Tool result · `toolu_01Nfvh8mAAuPXHuStTpVz3dn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ROADMAP.md\", \"content\": \"# irt_equated_bench_regen — Research Dashboard\\n\\n> 最后更新: 2026-05-21 01:28 UTC | 更新原因: D014 plan_004 Step 3 GSM1K 完成 + paper_framing.md 更新\\n\\n## 核心方向\\n**Pivot 完成 (D011)**：从\\\"DIF 检测方法\\\"转向\\\"LLM benchmark psychometric characterization + DIF methodology\\\"。ICLR 2027 目标不变。详见 paper_framing.md。\\n\\n**GSM1K 结果 (D014)**：DIF flags 与 contamination gap 显著负相关（r=−0.478, p=0.005）。DIF 不标记 contamination，而是标记 contamination 无法到达的 capability-discriminative items。强化 \\\"diagnostic lens\\\" 叙事。\\n\\n## 当前进展\\n- **阶段**: **Writing**（全部实验完成）\\n- **实验**: 12 完成（5 success / 5 negative / 0 failed），plan_004 全 3 步完成\\n- **Key results**:\\n  - MMLU: semi-synthetic ΔTPR=+0.508 | cross-subject ΔFPR=0.000 | within-subject C%=38.1% | downstream z=-8 to -49σ\\n  - GSM8K: temporal C%=18.9% | semi-synthetic ΔTPR=+0.818 | GSM1K gap r=−0.478 (p=0.005)\\n- **Paper Agent**: writing_plan.yaml 审批通过，figures 4/6 完成 + fig_1/fig_4 进行中\\n- **审稿**: Round 1 borderline 3.5/6，14 issues tracked\\n\\n## 近期任务\\n- [ ] Agent: 修正 Step 3 report 方向标签（Reviewer CRITICAL）\\n- [ ] Paper Agent: 更新 writing_plan.yaml 整合 GSM8K/GSM1K 章节 + 新 figure\\n- [ ] Paper Agent: 完成 fig_1（统一 \\\"2024-H1\\\" → \\\"2024\\\"）+ fig_4\\n- [ ] Paper Agent: Step 3 正文写作\\n- [ ] Post-pivot Dream（Step 3 完成后，写作定稿前评估 ICLR viability）\\n\\n## Completed\\n- ✅ plan_001-017: 10 个 MMLU 实验全部完成\\n- ✅ plan_004 Step 1-3: GSM8K cross-benchmark 验证全部完成\\n- ✅ 文献调查 22 篇 + experiment_summary.md + artifacts QC\\n- ✅ paper_framing.md 更新至 D014（Claim 4 four-layer, Claim 3 cross-benchmark）\\n- ✅ writing_plan.yaml 审批通过，figures fig_2/3/A1/A2 完成\\n\\n## GPU 预算\\nP0: 250h | P1: 350h | 已用: 0h（全部 CPU analysis）\\n无 GPU 需求。\\n\\n## 投稿目标\\nICLR 2027（~2026年10月 DDL）— 不降级\\n评估: main borderline 5.5-6/6, findings solid 6.5-7/6。GSM1K negative r 不升级为 validated method，但 cross-benchmark evidence chain 显著加强 characterization paper 深度。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D014 | 2026-05-21 | plan_004 Step 3 GSM1K: |r|=0.478 显著但方向为负——DIF 不标记  | plan_004_gsm8k_cross_benchmark, plan_017_downstream_impact |\\n| D013 | 2026-05-21 | plan_017 downstream impact negative 但 informative： | plan_017_downstream_impact |\\n| D012 | 2026-05-20 | Story 定稿：Candidate 1 (benchmark quality tool) + gr | plan_014_within_subject_dif, plan_016_within_subject_semi_synthetic, plan_001_real_data_dif_mmlu |\\n| D011 | 2026-05-20 | Pivot 拍板：从\\\"DIF 检测方法\\\"转向\\\"LLM benchmark psychometric  | plan_016_within_subject_semi_synthetic, plan_014_within_subject_dif, plan_011_semi_synthetic |\\n| D010 | 2026-05-20 | 方向 3 (Bifactor) pre-check 否定：within-subject tempor | plan_014_within_subject_dif, plan_011_semi_synthetic |\\n| D009 | 2026-05-20 | Dream #2 分析：best=3/6, median=3-4/6, worst=3/6。跨档一致 | dream_20260520T205007 |\\n| D008 | 2026-05-20 | 方向 2 (IRT θ-conditioning) 失败，1D 路线穷尽。plan_011 abil | plan_012_irt_theta_conditioning |\\n| D007 | 2026-05-20 | Story pivot: semi-synthetic validation 作为核心效度证据，Li | plan_011_semi_synthetic, plan_001_real_data_dif_mmlu, plan_001b_matched_ability_dif |\\n| D006 | 2026-05-20 | plan_011 positive: MH-DIF 检测差异性污染有效 (p=0.5 TPR=0.8 | plan_011_semi_synthetic |\\n| D005 | 2026-05-20 | 方向 1 (matched-ability DIF) 失败确认，所有 quintile enrich | plan_001b_matched_ability_dif |\\n\\n\\n\", \"total_chars\": 3101, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62b6b5e2-ae60-44b0-af98-255e3c63a363",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "c1ab1a39-50e9-4c59-8a78-fd47642a9671",
  "sourceToolAssistantUUID": "62b6b5e2-ae60-44b0-af98-255e3c63a363",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T02:08:28.595Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Tacf9GMZf575u9rq5r9WYY`</summary>

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
  "parentUuid": "c1ab1a39-50e9-4c59-8a78-fd47642a9671",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu634kjcQM9QsgL9wjE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e006d88c-dc6b-4a89-a1ab-e3d66c73d2bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sHp5Zf633tXAVMvegY23m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5996,
      "cache_read_input_tokens": 17367,
      "output_tokens": 295,
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
          "output_tokens": 295,
          "cache_read_input_tokens": 17367,
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

_source line 18 · 2026-05-21T02:08:28.615Z_

<details><summary>↩ Tool result · `toolu_01Tacf9GMZf575u9rq5r9WYY`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e006d88c-dc6b-4a89-a1ab-e3d66c73d2bc",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "7aeed0d5-c487-48e5-90f6-3545f0b7bdb8",
  "sourceToolAssistantUUID": "e006d88c-dc6b-4a89-a1ab-e3d66c73d2bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-21T02:08:31.561Z_

Let me read the latest dream report papers to get the most current version of the manuscript.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7aeed0d5-c487-48e5-90f6-3545f0b7bdb8",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu6arhLqpLhUcnArjsw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa1bfee8-fdf5-4c54-b582-ddb66f69c1e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Y5Sokiv9uhxwpbnjdWKG1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5709,
      "cache_read_input_tokens": 23363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5709,
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

_source line 20 · 2026-05-21T02:08:33.661Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JUzzidjduqrNo7jwGUURDf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa1bfee8-fdf5-4c54-b582-ddb66f69c1e9",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu6arhLqpLhUcnArjsw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8303da40-fbee-4243-b5ec-d9cb69a2e8e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Y5Sokiv9uhxwpbnjdWKG1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5709,
      "cache_read_input_tokens": 23363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5709,
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

_source line 21 · 2026-05-21T02:08:33.675Z_

<details><summary>↩ Tool result · `toolu_01JUzzidjduqrNo7jwGUURDf`</summary>

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
11	\usepackage{tabularx}
12	\usepackage{caption}
13	
14	\title{Psychometric Characterization of Item Instability in LLM Benchmarks:\\A Large-Scale Differential Item Functioning Analysis of MMLU}
15	
16	\author{
17	Anonymous Authors
18	}
19	
20	\date{}
21	
22	\begin{document}
23	\maketitle
24	
25	% ============================================================
26	% ABSTRACT
27	% ============================================================
28	\begin{abstract}
29	LLM benchmarks implicitly assume temporal score comparability---that a score of 80\% today measures the same construct as 80\% a year ago. We challenge this assumption by applying Differential Item Functioning (DIF) analysis, a classical psychometric tool, to the METABENCH response matrix (5{,}227 models $\times$ 12{,}508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date. We report four findings. \textbf{First}, 38\% of MMLU items are functionally unstable across model generations (ETS C category, $|\Delta_{\text{MH}}| \geq 1.5$), persisting within every subject domain (per-subject C\% = 31--45\%). \textbf{Second}, the field's standard validation approach---web-overlap contamination labels---cannot capture this differential signal (enrichment $\approx 1.0$), while semi-synthetic injection confirms detection capability ($\Delta\text{TPR} = +0.508$ on MMLU, $+0.818$ on GSM8K). \textbf{Third}, we provide a reusable semi-synthetic validation framework with cross-subject matching that eliminates false positive inflation ($\Delta\text{FPR} = 0.000$). \textbf{Fourth}, DIF items concentrate discriminative signal rather than noise: their removal disrupts rankings more than random removal ($z = -8$ to $-49\sigma$), and DIF flags anti-correlate with contamination on GSM8K ($r = -0.478$, $p = 0.005$). Architecture stratification reduces spurious flags by 29\% (C\% from 31.3\% to 22.1\%) while confirming that substantial genuine instability persists, demonstrating the method is refinable rather than fundamentally confounded. We release the semi-synthetic framework and DIF diagnostics as open infrastructure for benchmark maintenance.
30	\end{abstract}
31	
32	% ============================================================
33	% 1. INTRODUCTION
34	% ============================================================
35	\section{Introduction}
36	\label{sec:intro}
37	
38	When we state that ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent construct---that the 12{,}508 items function identically regardless of when or by which model they are answered. This assumption of \emph{temporal score comparability} underpins every leaderboard ranking, every benchmark-based paper claim, and every policy decision that cites benchmark performance.
39	
40	But do MMLU items function the same across model generations? As models improve through successive training paradigms---scaling, instruction tuning, RLHF, reasoning-chain RL---the population of test-takers changes dramatically. In classical psychometrics, when a test item functions differently across groups (e.g., producing different correct-response probabilities at matched ability levels), the item exhibits \emph{Differential Item Functioning} (DIF). DIF does not mean an item is ``bad''---it means the item's measurement properties are group-dependent, threatening the comparability of scores derived from that item.
41	
42	We apply DIF analysis to the METABENCH response matrix \citep{metabench2024}, comprising 5{,}227 models evaluated on 12{,}508 MMLU items. This constitutes the largest-scale psychometric analysis of an LLM benchmark to date. Our analysis yields four contributions:
43	
44	\begin{enumerate}
45	    \item \textbf{Temporal instability characterization.} 38\% of MMLU items exhibit large DIF (ETS C category) between 2023 and 2024-H1 model cohorts. This persists within every subject domain (31--45\% per subject, mean 38.1\%) and survives architecture stratification (22.1\% within decoder-only models alone). The instability correlates with domain-specific accuracy improvement ($\rho = 0.307$, $p = 0.02$), suggesting it reflects genuine capability shifts rather than pure noise.
46	
47	    \item \textbf{Ground truth meta-critique.} Web-overlap contamination labels \citep{li2024contamination} measure global exposure---whether an item is publicly accessible---not differential contamination. DIF enrichment $\approx 1.0$ against these labels is expected, not failure. Semi-synthetic injection confirms DIF detection capability ($\Delta\text{TPR} = +0.508$). This blind spot affects all work validating item-level detectors against web-overlap ground truth.
48	
49	    \item \textbf{Semi-synthetic validation framework.} We introduce a $\Delta$TPR methodology that injects controlled differential contamination into real response matrices. Cross-subject matching (using total score on \emph{other} subjects as the Mantel-Haenszel matching variable) eliminates FPR inflation ($\Delta\text{FPR} = 0.000$ across 5 tested subjects), while within-subject matching suffers from matching variable contamination (+0.186 FPR inflation). The framework generalizes to GSM8K ($\Delta\text{TPR} = +0.818$).
50	
51	    \item \textbf{DIF as diagnostic lens.} MMLU rankings exhibit massive redundancy ($\rho \approx 0.997$ after 31\% item removal), yet DIF items concentrate discriminative signal: their removal disrupts rankings significantly more than random removal ($z = -8$ to $-49\sigma$). Cross-benchmark validation on GSM8K confirms DIF flags anti-correlate with contamination gaps ($r = -0.478$, $p = 0.005$)---contaminated models perform \emph{worse} on DIF items, which capture genuine capability differences.
52	\end{enumerate}
53	
54	Architecture-stratified analysis (Section~\ref{sec:arch_strat}) demonstrates that restricting DIF to decoder-only models reduces C\% from 31.3\% to 22.1\%---a 29\% reduction---while improving IRT model fit (RMSEA from 0.082 to 0.037). This transforms the ``architecture confounding'' objection into a practical recommendation: run DIF within architecture-homogeneous subpopulations.
55	
56	
57	% ============================================================
58	% 2. RELATED WORK
59	% ============================================================
60	\section{Related Work}
61	\label{sec:related}
62	
63	\paragraph{Benchmark contamination detection.}
64	Contamination detection methods broadly fall into two categories. \emph{Per-model} approaches analyze individual model outputs: Min-K\% \citep{shi2024mink} uses minimum $k$-th percentile log-likelihood as a memorization signal; ConStat \citep{constat2024} compares performance on original versus semantically reformulated items; DVD \citep{dvd2024} measures generation variance under temperature sampling to detect bimodal memorization signatures. These methods share a reliance on web-overlap or n-gram labels for validation---a gap we characterize in Section~\ref{sec:meta_critique}. Preliminary evaluation of ConStat on MMLU shows AUROC of 0.73 on non-RL models but degradation to 0.44 on RL models, with low correlation to DIF flags ($r = 0.21$), confirming orthogonal detection axes. DVD achieves moderate AUROC (0.66 for verbatim contamination) at high computational cost (65 GPU-hours for 12 models), with similarly low DIF correlation ($r = 0.15$).
65	
66	\paragraph{DIF in educational testing.}
67	Differential Item Functioning analysis has a 40-year history in psychometrics \citep{holland1993dif}. The Mantel-Haenszel (MH) procedure \citep{mantel1959mh} remains the most widely used method due to its simplicity and robust statistical properties. The ETS classification system (A/B/C categories) provides operational thresholds: C items ($|\Delta_{\text{MH}}| \geq 1.5$ and significantly different from 1.0) warrant review or removal. Item-Focused Trees \citep{tutz2016ift} extend DIF detection to continuous covariates, enabling finer temporal resolution. We include an IFT analysis in Appendix~\ref{app:ift} showing concordance with categorical DIF (Jaccard = 0.76) and temporal split points aligning with major model release waves.
68	
69	\paragraph{Benchmark integrity and maintenance.}
70	Growing Pains \citep{growingpains2024} identifies anchor items for efficient evaluation; our DIF diagnostic complements this by detecting which anchor items are degrading across model generations. LiveBench \citep{livebench2024} and similar dynamic benchmarks address contamination through item refresh; our analysis provides psychometric infrastructure for deciding \emph{which} items to refresh and validating that replacements maintain construct equivalence.
71	
72	
73	% ============================================================
74	% 3. METHOD
75	% ============================================================
76	\section{Method}
77	\label{sec:method}
78	
79	\subsection{Differential Item Functioning: A Primer for ML Researchers}
80	\label{sec:dif_primer}
81	
82	Consider a binary response matrix $\mathbf{X} \in \{0,1\}^{N \times J}$ where $X_{ij} = 1$ if model $i$ answers item $j$ correctly. In DIF analysis, we partition models into a \emph{reference group} $R$ and a \emph{focal group} $F$ (here: temporal cohorts, e.g., pre-2024 vs.\ 2024-H1 models) and ask: does item $j$ function differently across groups, \emph{after conditioning on overall ability}?
83	
84	The Mantel-Haenszel (MH) procedure conditions on a discrete matching variable (total score or score stratum $k$) and computes the common odds ratio:
85	\begin{equation}
86	    \hat{\alpha}_{\text{MH}} = \frac{\sum_k A_k D_k / T_k}{\sum_k B_k C_k / T_k}
87	\end{equation}
88	where $A_k, B_k, C_k, D_k$ are cells of the $2 \times 2$ table (group $\times$ response) at stratum $k$, and $T_k$ is the stratum total. The log-odds ratio is converted to the ETS $\Delta$ scale:
89	\begin{equation}
90	    \Delta_{\text{MH}} = -2.35 \ln(\hat{\alpha}_{\text{MH}})
91	\end{equation}
92	
93	Items are classified using the ETS system:
94	\begin{itemize}
95	    \item \textbf{A} (negligible): $|\Delta_{\text{MH}}| < 1.0$ or not statistically significant
96	    \item \textbf{B} (moderate): $1.0 \leq |\Delta_{\text{MH}}| < 1.5$ and significant
97	    \item \textbf{C} (large): $|\Delta_{\text{MH}}| \geq 1.5$ and significantly different from 1.0
98	\end{itemize}
99	
100	\noindent\textbf{ML translation.} DIF analysis is analogous to checking whether a feature's predictive relationship with the outcome changes across subpopulations after controlling for a confounder. An item with large DIF is one where the ``decision boundary'' between correct and incorrect shifts across model generations at matched ability---the item measures something different for newer models than for older ones.
101	
102	\subsection{Semi-Synthetic Validation Framework}
103	\label{sec:semi_synthetic}
104	
105	Validating item-level contamination detectors requires ground truth at the item$\times$model level---which items are contaminated \emph{for which models}. No such ground truth exists naturally. We construct it via \emph{semi-synthetic injection}: starting from the real METABENCH response matrix, we flip a fraction $p$ of incorrect responses to correct for selected items in the focal group, simulating differential contamination.
106	
107	The key metric is $\Delta$TPR: the increase in DIF detection rate from injection. If a detector responds to injected differential contamination, $\Delta\text{TPR} > 0$; if it cannot distinguish injected items from naturally unstable ones, $\Delta\text{TPR} \approx 0$.
108	
109	\paragraph{Cross-subject matching.} A critical methodological choice is the MH matching variable. When injecting contamination into subject $s$, using the total score on subject $s$ as the matching variable inflates FPR because the matching variable itself is contaminated. We instead match on the total score on \emph{all other subjects} $S \setminus \{s\}$. This eliminates FPR inflation ($\Delta\text{FPR} = 0.000$ across all 5 tested subjects) while preserving detection power ($\Delta\text{TPR} > 0.3$ in 4/5 subjects).
110	
111	
112	% ============================================================
113	% 4. EXPERIMENTS: TEMPORAL DIF ON MMLU
114	% ============================================================
115	\section{Experiments}
116	\label{sec:experiments}
117	
118	\subsection{Large-Scale Temporal DIF Analysis}
119	\label{sec:temporal_dif}
120	
121	\paragraph{Setup.} We analyze the METABENCH response matrix: 5{,}227 models $\times$ 12{,}508 MMLU items. Models are partitioned into temporal cohorts based on release date (reference: pre-2024; focal: 2024-H1). The MH procedure is applied to each item with total MMLU score as the matching variable.
122	
123	\paragraph{Results.} Table~\ref{tab:main_dif} summarizes the main findings. 31.3\% of items fall into ETS category C (large DIF) in the full-population analysis. A random-split sanity check (randomly assigning models to groups) yields C\% = 0.18\%, confirming the temporal signal is not a statistical artifact. Within-subject analysis (running DIF separately per MMLU subject) reveals C\% ranges from 31\% to 45\% across subjects, with mean 38.1\%---instability is pervasive, not concentrated in a few subjects.
124	
125	The correlation between subject-level C\% and subject-level accuracy improvement is $\rho = 0.307$ ($p = 0.02$), indicating that domains where models improved most also exhibit greater item instability. This is consistent with the interpretation that rapid capability improvement changes how items function---models that ``got better'' at a domain interact differently with items testing that domain.
126	
127	DIF enrichment against Li et al.\ web-overlap contamination labels is 0.96 ($\approx 1.0$), a result we analyze in Section~\ref{sec:meta_critique}.
128	
129	\begin{table}[t]
130	\centering
131	\caption{Temporal DIF analysis on MMLU (5{,}227 models $\times$ 12{,}508 items). C\% denotes the percentage of items classified as ETS category C ($|\Delta_{\text{MH}}| \geq 1.5$, significantly different from 1.0).}
132	\label{tab:main_dif}
133	\begin{tabular}{lcc}
134	\toprule
135	\textbf{Analysis} & \textbf{C\%} & \textbf{Note} \\
136	\midrule
137	Full population (temporal cohorts) & 31.3\% & Reference: pre-2024; Focal: 2024-H1 \\
138	Random-split sanity check & 0.18\% & Models randomly assigned to groups \\
139	Within-subject (per MMLU subject) & 38.1\% (avg) & Range: 31--45\% across 57 subjects \\
140	Accuracy-improvement correlation & $\rho = 0.307$ & $p = 0.02$, subject-level \\
141	Li et al.\ enrichment & 0.96 & $\approx 1.0$; see \S\ref{sec:meta_critique} \\
142	\bottomrule
143	\end{tabular}
144	\end{table}
145	
146	
147	\subsection{Ground Truth Meta-Critique}
148	\label{sec:meta_critique}
149	
150	The near-unity enrichment ($\approx 1.0$) between DIF flags and web-overlap labels is expected rather than surprising. Web-overlap labels \citep{li2024contamination} measure \emph{global exposure}---whether an item text appears on the public internet. Since virtually all MMLU items have been on Common Crawl since 2020, nearly all items have equal global exposure. DIF, by contrast, detects \emph{differential functioning}---whether an item behaves differently across model cohorts at matched ability. These are orthogonal signals: global exposure is a static, model-agnostic property; differential functioning is dynamic and group-specific.
151	
152	This has a broader implication: \emph{any} contamination detection method validated against web-overlap labels at the item level faces the same blind spot. If the ground truth cannot distinguish ``contaminated for model A but not model B'' from ``equally exposed to all models,'' it cannot evaluate item-level differential detectors. This affects Min-K\%, n-gram methods, and all work using web-overlap as ground truth for item-level validation.
153	
154	Semi-synthetic injection (Section~\ref{sec:semi_synthetic_results}) confirms that DIF \emph{can} detect differential contamination when it exists ($\Delta\text{TPR} = +0.508$)---the problem is the ground truth, not the detector.
155	
156	
157	\subsection{Architecture-Stratified DIF Analysis}
158	\label{sec:arch_strat}
159	
160	A natural concern is that DIF flags may reflect architecture differences (encoder-decoder vs.\ decoder-only vs.\ mixture-of-experts) rather than genuine temporal instability. We address this directly by restricting DIF analysis to decoder-only models only ($N = 3{,}847$; reference: $n = 892$, focal: $n = 541$).
161	
162	\paragraph{Results.} Table~\ref{tab:arch_irt} shows IRT model fit diagnostics. Restricting to decoder-only models dramatically improves fit: RMSEA drops from 0.082 (poor) to 0.037 (acceptable), CFI increases to 0.93, and SRMR falls to 0.028. This confirms that architecture heterogeneity was driving model misspecification, not the items themselves.
163	
164	Table~\ref{tab:arch_dif} presents DIF detection rates. C\% drops from 31.3\% to 22.1\%---a 29.4\% reduction---meaning approximately 9 percentage points of the original flags were architecture-confounded. The remaining 22.1\% represents genuine temporal instability within a homogeneous architecture population. Semi-synthetic validation improves correspondingly: FPR drops from 0.314 to 0.221, and $\Delta$TPR increases from 0.674 to 0.72.
165	
166	A sanity check (random split within decoder-only models) yields C\% = 0.12\%, confirming the reduction is not from power loss. Flag overlap with the full-population analysis (Jaccard = 0.68) shows the core DIF items persist---architecture stratification refines rather than contradicts the original finding.
167	
168	\begin{table}[t]
169	\centering
170	\caption{IRT model fit diagnostics: full population vs.\ decoder-only subgroup.}
171	\label{tab:arch_irt}
172	\begin{tabular}{lccccc}
173	\toprule
174	\textbf{Population} & \textbf{N} & \textbf{RMSEA} & \textbf{CFI} & \textbf{TLI} & \textbf{SRMR} \\
175	\midrule
176	Full (all architectures) & 5{,}227 & 0.082 & --- & --- & --- \\
177	Decoder-only & 3{,}847 & 0.037 & 0.93 & 0.91 & 0.028 \\
178	\bottomrule
179	\end{tabular}
180	\end{table}
181	
182	\begin{table}[t]
183	\centering
184	\caption{DIF detection rates and semi-synthetic validation: architecture-stratified vs.\ full population.}
185	\label{tab:arch_dif}
186	\begin{tabular}{lcccc}
187	\toprule
188	\textbf{Population} & \textbf{C\%} & \textbf{$\Delta$TPR} & \textbf{FPR} & \textbf{Sanity C\%} \\
189	\midrule
190	Full population & 31.3\% & 0.674 & 0.314 & 0.18\% \\
191	Decoder-only & 22.1\% & 0.720 & 0.221 & 0.12\% \\
192	\midrule
193	\textbf{Reduction} & \textbf{29.4\%} & +6.8\% & $-$29.6\% & --- \\
194	\bottomrule
195	\end{tabular}
196	\end{table}
197	
198	\paragraph{Practical recommendation.} Architecture stratification is simple, zero-cost, and immediately actionable: when applying DIF to LLM benchmarks, restrict the analysis to architecture-homogeneous subpopulations. This reduces spurious flags from architecture confounding while improving IRT model assumptions.
199	
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8303da40-fbee-4243-b5ec-d9cb69a2e8e9",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "821bf132-590f-4029-8e1a-8da1cdf32614",
  "sourceToolAssistantUUID": "8303da40-fbee-4243-b5ec-d9cb69a2e8e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T02:08:34.603Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S2cF7RSeLLTSbKdFmX9pdU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "821bf132-590f-4029-8e1a-8da1cdf32614",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu6arhLqpLhUcnArjsw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b5c5cd2-33e7-4141-bc22-27012e303c39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Y5Sokiv9uhxwpbnjdWKG1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5709,
      "cache_read_input_tokens": 23363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5709,
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

_source line 23 · 2026-05-21T02:08:34.612Z_

<details><summary>↩ Tool result · `toolu_01S2cF7RSeLLTSbKdFmX9pdU`</summary>

```text
1	\documentclass[10pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{amsmath,amssymb}
4	\usepackage{booktabs}
5	\usepackage{graphicx}
6	\usepackage{hyperref}
7	\usepackage{xcolor}
8	\usepackage{multirow}
9	\usepackage{natbib}
10	\usepackage[small]{caption}
11	
12	\title{Psychometric Characterization of Item-Level Instability\\in LLM Benchmarks via Differential Item Functioning}
13	
14	\author{Anonymous}
15	\date{}
16	
17	\begin{document}
18	\maketitle
19	
20	%% ============================================================
21	%% ABSTRACT
22	%% ============================================================
23	\begin{abstract}
24	Large Language Model (LLM) benchmarks implicitly assume temporal score comparability: a score of 80\% today should reflect the same latent ability as 80\% one year ago.
25	We test this assumption by applying Differential Item Functioning (DIF) analysis---a classical psychometric method for detecting item-level behavioral anomalies---to the METABENCH response matrix (5{,}227 models $\times$ 12{,}508 MMLU items).
26	We report three findings.
27	First, 38\% of MMLU items exhibit large DIF (ETS C category) between 2023 and 2024-H1 model cohorts, persisting within every subject domain (per-subject C\%: 31--45\%).
28	This instability reflects a mixture of genuine capability improvement ($\rho{=}0.307$ with domain accuracy gains) and differential item functioning, and cannot be decomposed into a single cause.
29	Second, we identify an underappreciated methodological gap in contamination detection validation: web-overlap labels measure global item exposure, not differential functioning, producing expected enrichment ${\approx}1.0$ against DIF flags.
30	Third, we propose a semi-synthetic validation framework that injects controlled differential contamination into real response matrices; cross-subject matching eliminates false-positive inflation ($\Delta\text{FPR}{=}0.000$) while confirming detection power ($\Delta\text{TPR}{=}{+}0.508$ on MMLU, ${+}0.818$ on GSM8K).
31	We further show that MMLU exhibits massive measurement redundancy ($\rho{\approx}0.997$ after removing 31\% of items), reframing the instability as a measurement efficiency problem rather than a validity crisis.
32	Code and data will be released upon publication.
33	\end{abstract}
34	
35	%% ============================================================
36	%% 1  INTRODUCTION
37	%% ============================================================
38	\section{Introduction}
39	
40	Benchmarks such as MMLU~\citep{hendrycks2021mmlu} underpin comparative evaluation of LLMs.
41	When practitioners report that ``Model B outperforms Model A by 5 points on MMLU,'' they implicitly assume both scores reflect the same latent construct measured under equivalent conditions.
42	Psychometrics calls this assumption \emph{measurement invariance}: the test functions identically across examinee populations.
43	
44	This assumption is unlikely to hold in the LLM ecosystem, where models released months apart differ in training data composition, architecture, and optimization objective.
45	If a subset of items behaves differently across model generations---due to data contamination, capability shifts, or both---cross-temporal score comparisons carry uncontrolled item-level variance.
46	
47	We bring Differential Item Functioning (DIF)---a family of methods developed over four decades in educational testing~\citep{holland1993dif}---to characterize item-level behavioral drift in LLM benchmarks at unprecedented scale.
48	Applying the Mantel--Haenszel (MH) procedure to the METABENCH response matrix (5{,}227 models $\times$ 12{,}508 MMLU items), we find:
49	
50	\begin{enumerate}
51	\item \textbf{38\% of MMLU items are functionally unstable} across model generations (ETS C category, $|\Delta_\text{MH}|{\geq}1.5$). This persists within every subject domain (31--45\% per subject) and is not a statistical artifact (random-split sanity check: 0.18\%). The instability reflects a mixture of capability improvement and differential item functioning ($\rho{=}0.307$ between C\% and domain accuracy gains).
52	
53	\item \textbf{An underappreciated methodological gap} in contamination detection validation: web-overlap labels~\citep{li2024contamination} measure whether items are publicly accessible---a global, model-agnostic property---rather than whether items function differently across cohorts. Enrichment ${\approx}1.0$ between DIF flags and web-overlap labels is expected, not indicative of detector failure. Semi-synthetic injection confirms DIF's detection power ($\Delta\text{TPR}{=}{+}0.508$).
54	
55	\item \textbf{A reusable semi-synthetic validation framework} for any item-level contamination detector. By injecting known differential contamination into real response matrices and measuring $\Delta\text{TPR}$, the framework provides controlled evaluation infrastructure. Cross-subject matching eliminates matching-variable contamination ($\Delta\text{FPR}{=}0.000$), and the framework generalizes across benchmarks (GSM8K: $\Delta\text{TPR}{=}{+}0.818$).
56	
57	\item \textbf{DIF as diagnostic lens}: MMLU rankings exhibit massive measurement redundancy ($\rho{\approx}0.997$ after 31\% item removal), but DIF items concentrate discriminative signal (removal causes more ranking disruption than random, $z{=}{-}8$ to ${-}49\sigma$). Suggestive cross-benchmark evidence from GSM1K contamination gaps ($r{=}{-}0.478$, $p{=}0.005$, $N{=}33$) indicates DIF flags capture genuine capability differences rather than contamination artifacts.
58	\end{enumerate}
59	
60	We additionally report extensive robustness analyses (architecture stratification, item-focused trees, RL-model sensitivity), complementary detection baselines (ConStat perturbation, generation variance), a negative result on multi-signal ensemble fusion, and pilot studies on benchmark regeneration via IRT equating and LLM-based item generation.
61	
62	%% ============================================================
63	%% 2  BACKGROUND
64	%% ============================================================
65	\section{Preliminaries: DIF for LLM Benchmarks}
66	
67	\paragraph{Differential Item Functioning.}
68	An item exhibits DIF when examinees of equal ability from different groups have unequal probabilities of answering correctly.
69	In educational testing, groups are typically demographic (e.g., gender, ethnicity); we define groups \emph{temporally}: a reference cohort (models released before 2024) and a focal cohort (models released 2024-H1).
70	
71	\paragraph{Mantel--Haenszel procedure.}
72	We use the MH $\chi^2$ test with ETS $\Delta_\text{MH}$ effect-size classification:
73	\textbf{A} (negligible, $|\Delta_\text{MH}|{<}1.0$),
74	\textbf{B} (moderate, $1.0{\leq}|\Delta_\text{MH}|{<}1.5$), and
75	\textbf{C} (large, $|\Delta_\text{MH}|{\geq}1.5$).
76	Items are matched on total score to control for overall ability differences.
77	
78	\paragraph{IRT context.}
79	Item Response Theory (IRT) models item responses as a function of latent ability $\theta$.
80	A 2-parameter logistic (2PL) model specifies $P(X_{ij}{=}1|\theta_j) = \text{logistic}(a_i(\theta_j - b_i))$, where $a_i$ is discrimination and $b_i$ is difficulty.
81	DIF manifests as cross-group differences in item parameters.
82	We use IRT primarily for bifactor modeling and equating analyses (Sections~\ref{sec:bifactor} and~\ref{sec:calibration}).
83	
84	\paragraph{Why DIF, not contamination detection?}
85	Contamination detectors (Min-K\%, ConStat, n-gram overlap) answer: ``Is this model contaminated?''
86	DIF answers a different question: ``Does this item function differently across model cohorts?''
87	This distinction is critical---DIF is a \emph{characterization} tool for benchmark quality, not a per-model contamination detector.
88	
89	%% ============================================================
90	%% 3  EXPERIMENTAL SETUP
91	%% ============================================================
92	\section{Experimental Setup}
93	
94	\paragraph{Data.}
95	We use the METABENCH response matrix~\citep{metabench2024}: binary item responses for 5{,}227 models on 12{,}508 MMLU items across 57 subject domains.
96	Temporal cohorts are defined by model release date: reference (pre-2024, $N_\text{ref}{=}2{,}891$) and focal (2024-H1, $N_\text{foc}{=}2{,}336$).
97	For cross-benchmark analyses, we additionally use METABENCH's GSM8K partition (1{,}319 items $\times$ 6{,}702 models).
98	
99	\paragraph{DIF analysis pipeline.}
100	For each of the 12{,}508 items, we compute the MH $\Delta_\text{MH}$ statistic using total score on remaining items as the matching variable.
101	Items are classified into ETS A/B/C categories.
102	We define C\% as the proportion of items in category C.
103	
104	\paragraph{Semi-synthetic injection protocol.}
105	To validate detection power, we inject differential contamination by flipping incorrect$\rightarrow$correct responses for randomly selected items in the focal cohort at controlled injection probabilities $p \in \{0.3, 0.5, 0.7, 1.0\}$.
106	Detection power is measured as $\Delta\text{TPR} = \text{TPR}_\text{injected} - \text{TPR}_\text{baseline}$.
107	
108	%% ============================================================
109	%% 4  CORE FINDINGS
110	%% ============================================================
111	\section{Core Findings}
112	
113	\subsection{Item Instability Across Model Generations (Claim 1)}
114	\label{sec:instability}
115	
116	Applying MH DIF analysis to all 12{,}508 MMLU items yields C\%${=}31.3$\%, with 3{,}912 items exhibiting large differential functioning between temporal cohorts.
117	Within-subject analysis confirms this is not driven by cross-domain confounding: every one of 57 MMLU subjects shows C\% between 31\% and 45\%, with a mean of 38.1\%.
118	
119	A random-split sanity check (randomly assigning models to pseudo-cohorts regardless of release date) produces C\%${=}0.18$\%, confirming the temporal signal is not a statistical artifact.
120	
121	\paragraph{Capability improvement confound.}
122	The correlation between per-subject C\% and domain accuracy improvement is $\rho{=}0.307$ ($p{=}0.02$), indicating that item instability is partially explained by models improving differentially across domains.
123	We emphasize that the 38\% figure reflects a \emph{mixture} of genuine capability improvement and differential item functioning---we cannot decompose these contributions with available data.
124	
125	\subsection{Ground Truth Methodology Gap (Claim 2)}
126	\label{sec:groundtruth}
127	
128	Web-overlap contamination labels~\citep{li2024contamination} classify items as ``contaminated'' based on n-gram presence in Common Crawl.
129	These labels measure a \emph{global} property (public accessibility) that applies nearly uniformly to MMLU items, which have been publicly available since 2020.
130	DIF, by contrast, measures a \emph{differential} property: whether an item functions differently across model cohorts.
131	
132	Empirically, DIF flag enrichment against Li et al.\ labels is ${\approx}1.0$ (no enrichment).
133	This is expected when web-overlap labels lack item-level discriminative power for the quantity DIF measures.
134	This represents an underappreciated methodological gap: studies validating item-level contamination detectors against web-overlap labels are evaluating against a reference standard that cannot distinguish differentially-functioning items from stable ones.
135	
136	Semi-synthetic injection (Section~\ref{sec:semisynthetic}) confirms DIF can detect differential contamination ($\Delta\text{TPR}{=}{+}0.508$ at injection probability $p{=}0.5$), demonstrating that the enrichment ${\approx}1.0$ result reflects ground-truth limitations, not detector failure.
137	
138	\subsection{Semi-Synthetic Validation Framework (Claim 3)}
139	\label{sec:semisynthetic}
140	
141	We propose a reusable validation framework for item-level contamination detectors.
142	The key innovation is the matching variable: using total score on \emph{other} subjects (cross-subject matching) rather than total score on the same subject (within-subject matching) as the MH conditioning variable.
143	
144	\paragraph{Cross-subject matching eliminates FPR inflation.}
145	Within-subject matching suffers from matching-variable contamination: if injected items inflate total score on that subject, the matching variable is no longer a clean ability proxy.
146	Cross-subject matching avoids this because injection targets are restricted to one subject, while matching uses scores on the remaining 56.
147	Across all 5 tested subjects, cross-subject matching yields $\Delta\text{FPR}{=}0.000$, whereas within-subject matching produces FPR inflation of ${+}0.186$.
148	
149	\paragraph{Detection power.}
150	On MMLU, $\Delta\text{TPR}{=}{+}0.508$ at $p{=}0.5$, with dose--response across injection probabilities ($p{=}0.3$: lower; $p{=}1.0$: higher).
151	Four of five tested subjects show $\Delta\text{TPR}{>}0.3$.
152	
153	\paragraph{Cross-benchmark replication.}
154	On GSM8K (1{,}319 items $\times$ 6{,}702 models), the framework yields $\Delta\text{TPR}{=}{+}0.818$ (standard matching) and ${+}0.517$ (external matching), confirming portability to single-domain math benchmarks.
155	GSM8K temporal DIF analysis independently reveals C\%${=}18.9$\%, lower than MMLU but non-trivial.
156	
157	\subsection{DIF as Diagnostic Lens (Claim 4)}
158	\label{sec:diagnostic}
159	
160	\paragraph{Measurement redundancy.}
161	Removing all 31\% C-category DIF items and re-ranking models yields Spearman $\rho{\approx}0.997$ with the full-item ranking.
162	This extreme robustness reveals that MMLU contains massive measurement redundancy: the stable 69\% of items suffice to preserve model ordering.
163	We reframe this as a \emph{measurement efficiency} problem---MMLU uses 12{,}508 items where ${\sim}8{,}600$ would produce equivalent rankings.
164	
165	\paragraph{DIF items carry discriminative signal.}
166	Despite ranking robustness, DIF item removal causes significantly \emph{more} ranking disruption than random removal of the same number of items ($z{=}{-}8$ to ${-}49\sigma$ across 21/21 conditions).
167	DIF items exhibit $1.09\times$ cross-cohort accuracy swing versus $0.96\times$ for stable items---they concentrate the information that differentiates model generations.
168	
169	\paragraph{Model-specific patterns.}
170	DIF analysis reveals which models benefit most from unstable items: phi-3 and llama-3 families gain ${+}700$--$850$ ranks from DIF items, while mistral-merge models lose $-400$ to $-587$ ranks.
171	
172	\paragraph{GSM1K cross-benchmark evidence (suggestive).}
173	On 33 matched models with GSM1K contamination gap data, DIF flags anti-correlate with contamination ($r{=}{-}0.478$, $p{=}0.005$; partial $r{=}{-}0.385$ controlling for accuracy; permutation $p{=}0.014$).
174	Models with high contamination gaps (Phi, Gemma families) perform \emph{worse} on DIF items.
175	This provides suggestive evidence that DIF captures genuine capability-discriminative items rather than contamination artifacts, though the sample size ($N{=}33$) and the use of contamination gap as a proxy warrant caution in interpretation.
176	
177	%% ============================================================
178	%% 5  ROBUSTNESS ANALYSES
179	%% ============================================================
180	\section{Robustness and Sensitivity Analyses}
181	
182	\subsection{Architecture-Stratified DIF}
183	\label{sec:archstrat}
184	
185	A natural concern is that DIF flags reflect architecture heterogeneity rather than temporal effects.
186	We restrict analysis to decoder-only models ($N{=}3{,}412$; reference: 891, focal: 523) and re-run MH DIF.
187	
188	\begin{table}[h]
189	\centering
190	\caption{IRT fit and DIF rates: full population vs.\ decoder-only subset.}
191	\label{tab:arch_strat}
192	\small
193	\begin{tabular}{lcccc}
194	\toprule
195	Metric & Full Population & Decoder-Only & $\Delta$ & Threshold \\
196	\midrule
197	RMSEA & 0.089 & 0.067 & $-0.022$ & ${<}0.05$ \\
198	CFI   & 0.78  & 0.83  & $+0.05$  & ${\geq}0.90$ \\
199	TLI   & 0.75  & 0.81  & $+0.06$  & ${\geq}0.90$ \\
200	SRMR  & 0.074 & 0.058 & $-0.016$ & ${<}0.05$ \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b5c5cd2-33e7-4141-bc22-27012e303c39",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "6671b69e-9e89-4dea-a1e1-bed6941bd634",
  "sourceToolAssistantUUID": "2b5c5cd2-33e7-4141-bc22-27012e303c39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T02:08:39.240Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S2K6JgmhLyHAaEGX9uQ8Jw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6671b69e-9e89-4dea-a1e1-bed6941bd634",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu73LewysXRkZjoVDhy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fe645ba-00f1-4adc-80dd-d18b74ee40d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TGmJaE4vjpbcYTE8LxhpRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10862,
      "cache_read_input_tokens": 29072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10862,
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

_source line 25 · 2026-05-21T02:08:39.247Z_

<details><summary>↩ Tool result · `toolu_01S2K6JgmhLyHAaEGX9uQ8Jw`</summary>

```text
200	SRMR  & 0.074 & 0.058 & $-0.016$ & ${<}0.05$ \\
201	C\%   & 31.3\% & 28.2\% & $-3.1$pp & --- \\
202	\bottomrule
203	\end{tabular}
204	\end{table}
205	
206	Architecture stratification modestly reduces C\% from 31.3\% to 28.2\% and improves IRT model fit (RMSEA: $0.089 \to 0.067$), confirming that population heterogeneity contributes some spurious DIF.
207	However, the improvement is modest: CFI remains below the 0.90 threshold, and 28.2\% of items still show large DIF within a homogeneous architecture family.
208	Jaccard overlap between decoder-only and full-population DIF flags is 0.81, indicating the core finding is robust to architecture stratification.
209	
210	We interpret the range [28.2\%, 31.3\%] as bounding the true C\% under varying assumptions about population homogeneity.
211	
212	\subsection{Item-Focused Trees}
213	\label{sec:ift}
214	
215	Categorical DIF uses an arbitrary binary temporal split (pre-2024 vs.\ 2024-H1).
216	Item-Focused Trees (IFT) treat model release date as a continuous covariate, allowing data-driven detection of split points and nonlinear DIF trajectories.
217	
218	\begin{table}[h]
219	\centering
220	\caption{IFT vs.\ categorical MH DIF comparison.}
221	\label{tab:ift}
222	\small
223	\begin{tabular}{lcccc}
224	\toprule
225	Method & Items Flagged & Unique Flags & Jaccard & Time (hrs) \\
226	\midrule
227	Categorical MH & 31.3\% & 12\% & --- & 0.3 \\
228	IFT (continuous) & 28.4\% & 8\% & 0.72 & 4.2 \\
229	\bottomrule
230	\end{tabular}
231	\end{table}
232	
233	IFT flags 28.4\% of items (vs.\ 31.3\% categorical), with Jaccard overlap of 0.72.
234	The median data-driven split point is 2023-09-15, close to our pre-specified boundary.
235	14\% of flagged items show nonlinear DIF trajectories (e.g., U-shaped: early and late models struggle, middle cohort excels), warranting future investigation.
236	The continuous approach validates the binary split without substantially changing conclusions.
237	
238	\subsection{Reasoning-RL Model Robustness}
239	\label{sec:rl_robust}
240	
241	Reasoning-RL models (trained with GRPO/PPO for chain-of-thought) represent a qualitatively different training regime.
242	We test whether DIF analysis remains stable when 13 reasoning-RL models are added to the focal cohort alongside 477 alignment-RL models.
243	
244	\begin{table}[h]
245	\centering
246	\caption{DIF vs.\ traditional detectors under RL model inclusion.}
247	\label{tab:rl_robust}
248	\small
249	\begin{tabular}{lccccc}
250	\toprule
251	Detector & AUROC (SFT) & AUROC (Align-RL) & AUROC (Reason-RL) & $\Delta$ & 95\% CI \\
252	\midrule
253	DIF (MH) & --- & --- & ret.=0.86 & $-0.14$ & [$-0.21$, $-0.07$] \\
254	ConStat & 0.72 & 0.69 & 0.54 & $-0.18$ & [$-0.31$, $-0.05$] \\
255	Min-K\% & 0.68 & 0.64 & 0.49 & $-0.19$ & [$-0.33$, $-0.06$] \\
256	\bottomrule
257	\end{tabular}
258	\end{table}
259	
260	DIF flag retention is 86\% (Jaccard 0.83 between SFT-only and RL-augmented cohorts), indicating group-level DIF is relatively robust to RL model inclusion.
261	Traditional per-model detectors degrade more sharply: ConStat AUROC drops from 0.72 to 0.54 and Min-K\% from 0.68 to 0.49 on reasoning-RL models.
262	However, with only $N{=}13$ reasoning-RL models, this comparison is statistically underpowered (DeLong test: $p{=}0.087$ for DIF vs.\ ConStat; TOST equivalence: $p{=}0.11$).
263	We report this as preliminary evidence consistent with theoretical robustness predictions, not as a definitive claim.
264	
265	\subsection{Graceful Degradation Under Item Replacement}
266	\label{sec:graceful}
267	
268	To formalize the measurement redundancy finding from Section~\ref{sec:diagnostic}, we progressively replace 5--50\% of items and track validity metrics.
269	
270	\begin{table}[h]
271	\centering
272	\caption{Validity metrics under progressive item replacement.}
273	\label{tab:graceful}
274	\small
275	\begin{tabular}{lcccc}
276	\toprule
277	Replacement \% & Spearman $\rho$ & Cronbach $\alpha$ & Construct Coverage & Max Rank $\Delta$ \\
278	\midrule
279	0\% (baseline) & 1.000 & 0.943 & 1.00 & 0 \\
280	5\% & 0.998 & 0.941 & 0.97 & 23 \\
281	10\% & 0.996 & 0.938 & 0.95 & 47 \\
282	20\% & 0.991 & 0.932 & 0.91 & 112 \\
283	50\% & 0.972 & 0.921 & 0.84 & 341 \\
284	\bottomrule
285	\end{tabular}
286	\end{table}
287	
288	Even at 50\% replacement, $\rho{=}0.972$---rankings are remarkably robust.
289	The empirical relationship $\rho \geq 1 - 1.3r$ (where $r$ is the replacement fraction) holds up to $r{=}0.4$.
290	The critical threshold where $\rho$ drops below 0.98 is approximately 35\%, close to the observed 38\% DIF rate.
291	DIF-targeted replacement produces $\rho$ only 0.008 lower than random replacement, suggesting DIF items are not pathologically clustered.
292	
293	This result cuts both ways: it validates the feasibility of item replacement (Section~\ref{sec:bifactor}) but also shows that benchmark rankings are robust even without intervention.
294	The practical concern is measurement \emph{efficiency}, not \emph{validity}: 12{,}508 items contain substantial redundancy relative to the ranking information they provide.
295	
296	\subsection{Cumulative Bayesian DIF Monitoring}
297	\label{sec:bayesian}
298	
299	Single-administration DIF has limited power for medium-effect items ($\delta{=}1.0$: power${=}0.41$).
300	We simulate a cumulative Bayesian DIF framework that accumulates evidence across successive benchmark administrations using informative priors.
301	
302	\begin{table}[h]
303	\centering
304	\caption{Detection power by number of cumulative administrations and effect size.}
305	\label{tab:bayesian}
306	\small
307	\begin{tabular}{lcccc}
308	\toprule
309	Administrations & $\delta{=}0.8$ & $\delta{=}1.0$ & $\delta{=}1.2$ & $\delta{=}1.4$ \\
310	\midrule
311	1 & 0.24 & 0.41 & 0.55 & 0.68 \\
312	2 & 0.37 & 0.54 & 0.69 & 0.81 \\
313	3 & 0.48 & 0.67 & 0.79 & 0.89 \\
314	4 & 0.54 & 0.74 & 0.84 & 0.92 \\
315	\bottomrule
316	\end{tabular}
317	\end{table}
318	
319	Power improves from 0.41 to 0.74 over four administrations for medium effects, with diminishing returns (gains: $+0.13$, $+0.13$, $+0.07$).
320	False-positive rate remains controlled (0.042 $\to$ 0.051) due to Bayesian shrinkage.
321	After four administrations, 68\% of items with Bayes factor ${>}3$ are detectable.
322	
323	This analysis is simulation-based---longitudinal benchmark data with four temporal waves does not yet exist.
324	We position it as a concrete recommendation for benchmark maintainers: collecting response matrices over time enables cumulative evidence accumulation for item quality monitoring, an established psychometric practice~\citep{sinharay2006bayesian} not yet adopted in LLM evaluation.
325	
326	%% ============================================================
327	%% 6  COMPLEMENTARY DETECTION METHODS
328	%% ============================================================
329	\section{Complementary Detection Baselines}
330	
331	\subsection{ConStat Perturbation Testing}
332	\label{sec:constat}
333	
334	ConStat-style perturbation testing~\citep{dekoninck2024constat} operates at the per-model level by comparing performance on original vs.\ semantically reformulated items.
335	We generate LLM-based reformulations for 248 MMLU items and test across 15 models.
336	
337	\begin{table}[h]
338	\centering
339	\caption{ConStat detection rates by model training category.}
340	\label{tab:constat}
341	\small
342	\begin{tabular}{lccc}
343	\toprule
344	Model Category & $N$ Models & Detection Rate (FDR=0.10) & Mean $d$ \\
345	\midrule
346	SFT-only & 6 & 0.153 & 0.81 \\
347	Alignment-RL (DPO) & 5 & 0.134 & 0.69 \\
348	Reasoning-RL (GRPO) & 4 & 0.071 & 0.42 \\
349	\bottomrule
350	\end{tabular}
351	\end{table}
352	
353	ConStat detects surface-form sensitivity primarily in SFT and alignment-RL models (detection rate 13--15\%, effect size $d{=}0.69$--$0.81$) but fails on reasoning-RL models (detection rate 7.1\%, $d{=}0.42$), which generalize beyond verbatim patterns.
354	AUROC against Li et al.\ web-overlap labels is 0.61, consistent with the ground-truth mismatch discussed in Section~\ref{sec:groundtruth}.
355	AUROC on non-RL models (0.67) vs.\ RL models (0.52) confirms ConStat detects a complementary signal to DIF: per-model surface-form memorization rather than cross-cohort differential functioning.
356	
357	\subsection{Generation Variance Detection (DVD)}
358	\label{sec:dvd}
359	
360	DVD detects contamination via reduced generation variance: memorized items elicit consistently correct responses across temperature-varied generations.
361	We generate 50 responses per item ($T{=}0.8$) for 300 MMLU items across 12 open-weight models (62 GPU-hours).
362	
363	\begin{table}[h]
364	\centering
365	\caption{DVD detection characteristics by contamination type.}
366	\label{tab:dvd}
367	\small
368	\begin{tabular}{lccc}
369	\toprule
370	Contamination Type & AUROC & Detection Rate ($\tau{=}0.10$) & Mean Var.\ Reduction \\
371	\midrule
372	Verbatim & 0.71 & 0.134 & 0.21 \\
373	Variant/Paraphrase & 0.63 & 0.072 & 0.12 \\
374	None (clean) & --- & 0.031 (FPR) & --- \\
375	\bottomrule
376	\end{tabular}
377	\end{table}
378	
379	DVD achieves moderate detection of verbatim contamination (AUROC 0.71) but weaker performance on paraphrase contamination (AUROC 0.63).
380	Correspondence with DIF flags is low (AUROC 0.58), reflecting fundamentally different signals: DIF measures cross-group differentials, DVD measures within-model consistency.
381	The 62 GPU-hour cost for 12 models on 300 items raises scalability concerns for full-benchmark deployment.
382	
383	\subsection{Multi-Signal Ensemble}
384	\label{sec:ensemble}
385	
386	We attempt to fuse DIF, ConStat, and DVD into a multi-signal ensemble via majority voting (2-of-3) and learned weighted fusion.
387	
388	\begin{table}[h]
389	\centering
390	\caption{Ensemble vs.\ individual detector performance.}
391	\label{tab:ensemble}
392	\small
393	\begin{tabular}{lccc}
394	\toprule
395	Method & AUROC & Prec.@FPR=0.10 & Coverage \\
396	\midrule
397	DIF (MH) & 0.62 & 0.38 & 31.3\% \\
398	ConStat & 0.61 & 0.34 & 12.7\% \\
399	DVD & 0.58 & 0.29 & 9.4\% \\
400	Ensemble (2-of-3) & 0.66 & 0.41 & 6.8\% \\
401	Ensemble (weighted) & 0.66 & 0.43 & 8.2\% \\
402	\bottomrule
403	\end{tabular}
404	\end{table}
405	
406	The ensemble yields only modest AUROC improvement ($0.66$ vs.\ best individual $0.62$) because the three methods target orthogonal contamination mechanisms with limited overlap (pairwise coverage overlap: DIF--ConStat 31\%, DIF--DVD 22\%, ConStat--DVD 38\%).
407	Cross-validation weight variance is high (0.15), indicating unstable calibration.
408	We report this as a \emph{negative result}: ensemble approaches require partially redundant signals; when detection mechanisms are orthogonal, fusion provides minimal lift.
409	This negative result paradoxically supports our reframing: DIF measures something fundamentally different from per-model detectors, and combining them does not produce a unified contamination signal.
410	
411	%% ============================================================
412	%% 7  TOWARD BENCHMARK REGENERATION
413	%% ============================================================
414	\section{Pilot Studies: Benchmark Regeneration}
415	
416	\subsection{Bifactor IRT Equating}
417	\label{sec:bifactor}
418	
419	We fit a bifactor IRT model (one general factor + 57 subject-specific factors) to the METABENCH MMLU response matrix and attempt test equating via DIF-stable anchor items.
420	
421	\begin{table}[h]
422	\centering
423	\caption{Bifactor model fit indices.}
424	\label{tab:bifactor}
425	\small
426	\begin{tabular}{lccc}
427	\toprule
428	Index & Value & Acceptable & Good \\
429	\midrule
430	RMSEA & 0.041 & ${<}0.08$ \checkmark & ${<}0.05$ \checkmark \\
431	CFI   & 0.87  & ${\geq}0.90$ \texttimes & ${\geq}0.95$ \texttimes \\
432	TLI   & 0.84  & ${\geq}0.90$ \texttimes & ${\geq}0.95$ \texttimes \\
433	SRMR  & 0.063 & ${<}0.08$ \checkmark & ${<}0.05$ \texttimes \\
434	\bottomrule
435	\end{tabular}
436	\end{table}
437	
438	The bifactor model converges after 847 iterations with acceptable RMSEA (0.041) but marginal CFI (0.87) and TLI (0.84).
439	The general factor explains 62\% of variance; individual subjects contribute 14\% on average.
440	Using 1{,}842 DIF-A anchor items, equated score correlation between original and replacement forms is $\rho{=}0.93$---below the target $\rho{\geq}0.95$ due to replacement item calibration error (RMSE${=}0.38$).
441	Fixed-parameter calibration is acceptable for 68\% of replacement items.
442	
443	We conclude that IRT-based equating is \emph{feasible in principle} but the marginal model fit and below-target equated correlation indicate that multidimensional IRT or domain-clustered approaches are needed for production-quality benchmark regeneration.
444	
445	\subsection{LLM-Based Item Generation and Calibration}
446	\label{sec:calibration}
447	
448	We generate 200 replacement items targeting DIF-flagged MMLU questions, using LLM generation with construct constraints and student-simulation calibration.
449	
450	\begin{table}[h]
451	\centering
452	\caption{Calibration method comparison for generated items.}
453	\label{tab:itemgen}
454	\small
455	\begin{tabular}{lccc}
456	\toprule
457	Method & Difficulty $\rho$ & Discrim.\ $\rho$ & \% Within ${\pm}0.5$ Target \\
458	\midrule
459	Prompt-based targeting & 0.31 & 0.28 & 24\% \\
460	Student sim.\ (5 students) & 0.64 & 0.42 & 43\% \\
461	Student sim.\ (20 students) & 0.68 & 0.45 & 47\% \\
462	\bottomrule
463	\end{tabular}
464	\end{table}
465	
466	Student simulation substantially improves difficulty prediction ($\rho{=}0.64$ with 5 students, $0.68$ with 20) over prompt-based targeting ($\rho{=}0.31$).
467	Construct alignment is reasonable (78\% human-rated), but holdout panel correlation is moderate (0.58), indicating limited transferability to unseen models.
468	Only 43\% of items fall within ${\pm}0.5$ difficulty of their targets, suggesting iterative recalibration would be needed.
469	At 187 GPU-hours for 200 items, cost remains a practical barrier to full-scale deployment.
470	These results indicate that LLM-based item generation is a viable but immature pipeline requiring human-in-the-loop validation for production use.
471	
472	%% ============================================================
473	%% 8  DISCUSSION
474	%% ============================================================
475	\section{Discussion}
476	
477	\paragraph{Measurement efficiency, not validity crisis.}
478	The central tension in our findings is that 38\% of MMLU items are functionally unstable, yet removing them barely changes model rankings ($\rho{\approx}0.997$).
479	We resolve this by reframing: MMLU's 12{,}508 items contain massive measurement redundancy.
480	The stable subset suffices to preserve rankings, but the unstable items carry disproportionate discriminative information ($z{=}{-}8$ to ${-}49\sigma$ vs.\ random removal).
481	The practical implication is not ``MMLU is broken'' but ``MMLU could achieve equivalent measurement precision with fewer, better-characterized items''---a measurement efficiency problem.
482	
483	\paragraph{The 38\% figure: honest interpretation.}
484	We cannot decompose the 38\% instability into contamination vs.\ capability improvement.
485	The $\rho{=}0.307$ correlation with domain accuracy gains suggests capability improvement is a substantial component.
486	Architecture stratification reduces C\% to 28.2\% (Section~\ref{sec:archstrat}), providing a lower bound under controlled conditions.
487	The range [28\%, 38\%] represents our best estimate of temporal item instability under varying methodological assumptions.
488	
489	\paragraph{Complementary detection landscape.}
490	Our experiments with ConStat (Section~\ref{sec:constat}), DVD (Section~\ref{sec:dvd}), and ensemble fusion (Section~\ref{sec:ensemble}) reveal that contamination detection methods target orthogonal mechanisms.
491	DIF detects cross-cohort differential functioning; ConStat detects per-model surface-form sensitivity; DVD detects within-model generation consistency.
492	The negative ensemble result confirms these are fundamentally different signals, not noisy measurements of the same underlying phenomenon.
493	
494	\paragraph{Semi-synthetic framework as portable contribution.}
495	The $\Delta\text{TPR}$/$\Delta\text{FPR}$ framework with cross-subject matching is agnostic to the underlying detector.
496	Any item-level contamination detection method can be validated by injecting known differential contamination and measuring detection power increase.
497	Cross-benchmark replication (MMLU $\to$ GSM8K) demonstrates portability.
498	We consider this the most immediately reusable contribution for the evaluation community.
499	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fe645ba-00f1-4adc-80dd-d18b74ee40d8",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "daab2c2b-3e21-408e-a44e-d897fd6519ed",
  "sourceToolAssistantUUID": "6fe645ba-00f1-4adc-80dd-d18b74ee40d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T02:08:40.252Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NK4w2GeX8yJiAEzCako3ci`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "daab2c2b-3e21-408e-a44e-d897fd6519ed",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu73LewysXRkZjoVDhy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98dad424-38ee-4be0-9b8d-f74a8964b676",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TGmJaE4vjpbcYTE8LxhpRY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10862,
      "cache_read_input_tokens": 29072,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10862
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 261,
          "cache_read_input_tokens": 29072,
          "cache_creation_input_tokens": 10862,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10862,
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

_source line 27 · 2026-05-21T02:08:40.258Z_

<details><summary>↩ Tool result · `toolu_01NK4w2GeX8yJiAEzCako3ci`</summary>

```text
200	
201	\subsection{Semi-Synthetic Validation Results}
202	\label{sec:semi_synthetic_results}
203	
204	Table~\ref{tab:semi_synthetic} presents semi-synthetic validation results across benchmarks and matching strategies. On MMLU, cross-subject matching achieves $\Delta\text{TPR} = +0.508$ at injection probability $p = 0.5$, with strict $\Delta\text{FPR} = 0.000$ (4/5 subjects show $\Delta\text{TPR} > 0.3$). Within-subject matching suffers from matching variable contamination, inflating FPR by +0.186. The dose-response relationship (increasing $\Delta$TPR from $p = 0.3$ to $p = 1.0$) confirms the signal is driven by injected contamination rather than distributional artifacts.
205	
206	Cross-benchmark replication on GSM8K (1{,}319 items $\times$ 6{,}702 models from METABENCH) yields $\Delta\text{TPR} = +0.818$ with standard matching and $+0.517$ with external matching, confirming framework portability. GSM8K's temporal DIF rate is C\% = 18.9\%, lower than MMLU's 31.3\%, consistent with its narrower construct (single-domain math).
207	
208	\begin{table}[t]
209	\centering
210	\caption{Semi-synthetic validation: $\Delta$TPR and $\Delta$FPR across benchmarks and matching strategies.}
211	\label{tab:semi_synthetic}
212	\begin{tabular}{llcc}
213	\toprule
214	\textbf{Benchmark} & \textbf{Matching Strategy} & \textbf{$\Delta$TPR} & \textbf{$\Delta$FPR} \\
215	\midrule
216	MMLU & Cross-subject & +0.508 & 0.000 \\
217	MMLU & Within-subject & --- & +0.186 (inflated) \\
218	GSM8K & Standard & +0.818 & --- \\
219	GSM8K & External & +0.517 & --- \\
220	\bottomrule
221	\end{tabular}
222	\end{table}
223	
224	
225	\subsection{Structural Constraints on DIF}
226	\label{sec:structural}
227	
228	We investigated whether structural improvements to DIF methodology could reduce the baseline instability rate. Three approaches were tested:
229	
230	\begin{enumerate}
231	    \item \textbf{Matched-ability cohort design}: Balancing temporal cohorts on overall ability does not reduce C\% below 31\%, because DIF is already ability-conditioned.
232	    \item \textbf{IRT $\theta$-conditioning}: Replacing discrete score strata with continuous IRT ability estimates yields near-identical flags ($r = 0.9986$ with MH flags), confirming discretization is not the issue.
233	    \item \textbf{Bifactor pre-check}: A bifactor IRT model (general + subject-specific factors) confirms MMLU has genuine multidimensional structure (general factor: 42\% variance, subject factors: 18\% average; RMSEA = 0.038, CFI = 0.91). However, anchoring on DIF-free items reduces C\% only to 33.5\%---multidimensionality accounts for merely $\sim$2.4 pp of the instability.
234	\end{enumerate}
235	
236	Table~\ref{tab:bifactor} summarizes the bifactor analysis. The equated score correlation ($\rho = 0.965$) meets the $\geq 0.95$ criterion, but this reflects MMLU's massive redundancy rather than successful decontamination. These results constitute an empirical observation: standard psychometric corrections---matched-ability, $\theta$-conditioning, bifactor equating---are insufficient to reduce baseline DIF below 31\% while maintaining detection power. Higher-dimensional methods (MIMIC, multidimensional IRT, propensity-score matching) may address individual constraints and are directions for future work.
237	
238	\begin{table}[t]
239	\centering
240	\caption{Bifactor IRT equating pilot: model fit and DIF reduction.}
241	\label{tab:bifactor}
242	\begin{tabular}{lc}
243	\toprule
244	\textbf{Metric} & \textbf{Value} \\
245	\midrule
246	Bifactor RMSEA & 0.038 \\
247	Bifactor CFI / TLI & 0.91 / 0.89 \\
248	General factor variance explained & 42\% \\
249	Subject factor avg.\ variance & 18\% \\
250	Anchor items selected & 4{,}200 \\
251	C\% after equating & 33.5\% \\
252	Equated score $\rho$ (original vs.\ replaced) & 0.965 \\
253	\bottomrule
254	\end{tabular}
255	\end{table}
256	
257	
258	% ============================================================
259	% 5. DIF AS DIAGNOSTIC LENS
260	% ============================================================
261	\section{DIF as Diagnostic Lens}
262	\label{sec:diagnostic}
263	
264	\subsection{Benchmark Redundancy and Discriminative Signal}
265	\label{sec:redundancy}
266	
267	Removing all C-category DIF items (31\% of MMLU) barely changes model rankings: the Spearman correlation between full and stable-only rankings is $\rho \approx 0.997$. This reveals massive measurement redundancy---MMLU has approximately $3\times$ more items than needed for stable rankings.
268	
269	Yet DIF items are not noise. Their removal disrupts rankings \emph{significantly more} than random removal of equal size ($z = -8$ to $-49\sigma$ across 21 conditions). DIF items carry $1.09\times$ cross-cohort accuracy swing versus $0.96\times$ for stable items---they concentrate the information that differentiates model generations. Model-specific patterns emerge: phi-3 and llama-3 families gain $+700$ to $+850$ ranks from DIF items, while mistral merges lose $-400$ to $-587$ ranks.
270	
271	DIF items thus function as \emph{diagnostic markers}: they identify which capability dimensions are changing across model generations. This reframes DIF from ``find bad items and remove'' to ``understand what changed and why''---complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.
272	
273	
274	\subsection{Cross-Benchmark Validation: GSM8K and GSM1K}
275	\label{sec:cross_benchmark}
276	
277	On GSM8K (1{,}319 items $\times$ 6{,}702 models), DIF flags anti-correlate with GSM1K contamination gaps ($r = -0.478$, $p = 0.005$; partial $r = -0.385$ controlling for accuracy; permutation $p = 0.014$). Models with high contamination gaps (Phi, Gemma families) perform \emph{worse} on DIF items. This confirms that DIF captures genuine capability-discriminative items that contamination cannot fake---contaminated models achieve shallow performance gains concentrated on non-DIF items. The analysis includes $N = 33$ matched models and is leave-one-out robust (min $|r| = 0.374$).
278	
279	
280	\subsection{Cumulative Bayesian DIF for Operational Monitoring}
281	\label{sec:bayesian}
282	
283	Single-shot DIF detection has limited power for medium effects ($\text{TPR} = 0.42$ at $\delta = 1.0$). We propose cumulative Bayesian DIF priors that accumulate evidence across successive benchmark administrations.
284	
285	Table~\ref{tab:bayesian} shows power improvement over four simulated administrations ($N = 200$ models per administration). Each administration adds approximately 15 percentage points of TPR for medium effects ($\delta = 1.0$), reaching 0.71 after three administrations. FPR remains stable at $\sim$0.04 because Bayesian updating with proper priors is conservative on non-DIF items. At the operational threshold ($\delta = 1.4$), power reaches 0.89 by administration 4. The Bayes factor threshold of 3.2 (``substantial evidence'') provides a principled decision criterion superior to the arbitrary $|\Delta_{\text{MH}}| \geq 1.5$ cutoff.
286	
287	\begin{table}[t]
288	\centering
289	\caption{Cumulative Bayesian DIF: power by administration $\times$ effect size. FPR remains stable across administrations ($\sim$0.04). $N = 200$ simulated models per administration; BF threshold = 3.2.}
290	\label{tab:bayesian}
291	\begin{tabular}{lcccc}
292	\toprule
293	\textbf{Effect Size ($\delta$)} & \textbf{Admin 1} & \textbf{Admin 2} & \textbf{Admin 3} & \textbf{Admin 4} \\
294	\midrule
295	0.8 & --- & --- & --- & 0.53 \\
296	1.0 & 0.42 & 0.58 & 0.71 & 0.78 \\
297	1.2 & --- & --- & --- & --- \\
298	1.4 & --- & --- & --- & 0.89 \\
299	\midrule
300	FPR (Admin 1) & \multicolumn{4}{c}{0.041} \\
301	FPR (Admin 4) & \multicolumn{4}{c}{0.039} \\
302	Prior-posterior shrinkage & \multicolumn{4}{c}{0.35} \\
303	\bottomrule
304	\end{tabular}
305	\end{table}
306	
307	\paragraph{Operational recommendation.} Benchmark maintainers should accumulate DIF evidence across evaluation rounds rather than relying on single-shot detection. Three to four administrations suffice for reliable detection of operationally relevant effects ($\delta \geq 1.0$).
308	
309	
310	% ============================================================
311	% 6. DISCUSSION
312	% ============================================================
313	\section{Discussion}
314	\label{sec:discussion}
315	
316	\paragraph{RL robustness.}
317	A natural concern is whether reasoning-RL models (GRPO/PPO-trained) break DIF analysis. We evaluate this in Appendix~\ref{app:rl}: adding 13 reasoning-RL models to METABENCH cohorts barely perturbs DIF flags (Jaccard = 0.88, TOST equivalence $p = 0.008$). By contrast, traditional per-model detectors degrade sharply on RL models (Min-K\% AUROC: 0.81 $\rightarrow$ 0.52; ConStat AUROC: 0.77 $\rightarrow$ 0.48). DIF's group-level architecture is fundamentally orthogonal to the NLL-gap-contraction mechanism that defeats per-model detectors. The $N = 13$ sample is small and we acknowledge this as a limitation; the directional evidence is nonetheless unambiguous.
318	
319	\paragraph{Cause vs.\ characterization.}
320	We emphasize that 38\% instability is a \emph{characterization finding}, not a contamination claim. The correlation with accuracy improvement ($\rho = 0.307$) means we cannot decompose instability into contamination vs.\ genuine capability improvement. DIF reveals \emph{that} items function differently---not \emph{why}. This is the appropriate scope for a characterization study; causal decomposition requires controlled experiments (training models with and without specific items) that are beyond current infrastructure.
321	
322	
323	% ============================================================
324	% 7. FUTURE WORK
325	% ============================================================
326	\section{Future Work}
327	\label{sec:future}
328	
329	Our analysis suggests several natural extensions organized around three themes.
330	
331	\paragraph{Multi-signal ensemble detection.}
332	DIF, ConStat, and DVD capture orthogonal contamination signals (pairwise correlations $r \leq 0.21$). Preliminary ensemble fusion achieves AUROC 0.89 with FPR 0.07 under 2-of-3 voting (Table~\ref{tab:ensemble}). Weighted fusion yields a modest improvement (AUROC 0.89 vs.\ 0.86 uniform), with stable cross-validated weights ($\sigma = 0.03$). A standalone methods paper exploring this ensemble is planned.
333	
334	\begin{table}[t]
335	\centering
336	\caption{Preliminary ensemble fusion results (DIF + ConStat + DVD). All results are from pilot evaluation and are planned for a follow-up study.}
337	\label{tab:ensemble}
338	\begin{tabular}{lc}
339	\toprule
340	\textbf{Metric} & \textbf{Value} \\
341	\midrule
342	2-of-3 voting TPR & 0.84 \\
343	2-of-3 voting FPR & 0.07 \\
344	Weighted fusion AUROC & 0.89 \\
345	Uniform weight AUROC & 0.86 \\
346	Cross-validated weight stability ($\sigma$) & 0.03 \\
347	Effective coverage (union) & 0.78 \\
348	\bottomrule
349	\end{tabular}
350	\end{table}
351	
352	\paragraph{Per-model detection baselines.}
353	ConStat achieves AUROC 0.73 on non-RL models (Table~\ref{tab:constat}) but degrades to 0.44 on RL models, consistent with PPO's smoothing of original-vs-reformulated accuracy gaps (effect size drops from 0.85 to 0.31). DVD detects verbatim contamination at AUROC 0.66 (Table~\ref{tab:dvd}) but is weak on variant contamination (0.58) and costly (65 GPU-hours for 12 models). These per-model approaches are complementary to DIF's group-level analysis.
354	
355	\begin{table}[t]
356	\centering
357	\caption{ConStat perturbation testing on MMLU (240 reformulated items $\times$ 15 models).}
358	\label{tab:constat}
359	\begin{tabular}{lc}
360	\toprule
361	\textbf{Metric} & \textbf{Value} \\
362	\midrule
363	Paraphrase semantic similarity & 0.94 \\
364	Detection rate (FDR = 0.10) & 0.32 \\
365	AUROC (non-RL models) & 0.73 \\
366	AUROC (RL models) & 0.44 \\
367	Correlation with DIF flags & 0.21 \\
368	Effect size (verbatim contaminated) & 0.85 \\
369	Effect size (paraphrase contaminated) & 0.31 \\
370	\bottomrule
371	\end{tabular}
372	\end{table}
373	
374	\begin{table}[t]
375	\centering
376	\caption{DVD generation variance on MMLU (12 models $\times$ 2{,}400 items, 50 responses/item at $T = 0.8$).}
377	\label{tab:dvd}
378	\begin{tabular}{lc}
379	\toprule
380	\textbf{Metric} & \textbf{Value} \\
381	\midrule
382	AUROC (verbatim contamination) & 0.66 \\
383	AUROC (variant contamination) & 0.58 \\
384	Bimodal detection rate & 0.14 \\
385	Correlation with DIF flags & 0.15 \\
386	GPU-hours consumed & 65 \\
387	\bottomrule
388	\end{tabular}
389	\end{table}
390	
391	\paragraph{Automated benchmark maintenance.}
392	The massive redundancy we observe ($\rho = 0.997$ after 31\% item removal) suggests benchmark maintenance via item replacement is feasible. Preliminary analysis (Table~\ref{tab:degradation}) confirms MMLU tolerates aggressive replacement: $\rho = 0.994$ at 20\% replacement with 96\% construct coverage. A pilot item generation study using student simulation \citep{studentsim2025} achieves difficulty calibration $\rho = 0.71$ (Table~\ref{tab:itemgen}), substantially outperforming prompt-based targeting ($\rho = 0.28$). These components---DIF identifies which items to replace, student simulation calibrates replacements, graceful degradation bounds validate the process---form a complete pipeline for future work.
393	
394	\begin{table}[t]
395	\centering
396	\caption{Graceful degradation: validity metrics under progressive item replacement.}
397	\label{tab:degradation}
398	\begin{tabular}{lccc}
399	\toprule
400	\textbf{Replacement Rate} & \textbf{Ranking $\rho$} & \textbf{SHR} & \textbf{Construct Coverage} \\
401	\midrule
402	5\% & 0.9991 & --- & --- \\
403	10\% & 0.9978 & --- & --- \\
404	20\% & 0.9943 & 0.988 & 0.96 \\
405	50\% & 0.9821 & --- & 0.88 \\
406	\midrule
407	\multicolumn{4}{l}{Theoretical bound: $\rho \geq 1 - 2r(1-r)$; empirical-theoretical gap = 0.008} \\
408	\bottomrule
409	\end{tabular}
410	\end{table}
411	
412	\begin{table}[t]
413	\centering
414	\caption{Item generation calibration pilot (500 generated items $\times$ 30 MMLU subjects).}
415	\label{tab:itemgen}
416	\begin{tabular}{lcc}
417	\toprule
418	\textbf{Metric} & \textbf{Student Sim.} & \textbf{Prompt-based} \\
419	\midrule
420	Difficulty $\rho$ (calibration) & 0.71 & 0.28 \\
421	Discrimination $\rho$ (calibration) & 0.58 & --- \\
422	Difficulty $\rho$ (holdout, $N=50$) & 0.64 & --- \\
423	Discrimination $\rho$ (holdout) & 0.49 & --- \\
424	Construct coverage (Jaccard) & 0.82 & --- \\
425	\bottomrule
426	\end{tabular}
427	\end{table}
428	
429	
430	% ============================================================
431	% 8. CONCLUSION
432	% ============================================================
433	\section{Conclusion}
434	\label{sec:conclusion}
435	
436	We present the largest-scale psychometric analysis of an LLM benchmark, revealing that 38\% of MMLU items are functionally unstable across model generations. This instability persists within every subject domain, survives architecture stratification (22.1\% within decoder-only models), and correlates with capability improvement---models getting better at specific domains changes how items function.
437	
438	Our analysis exposes a fundamental blind spot in the field's validation methodology: web-overlap contamination labels cannot evaluate item-level differential detectors. The semi-synthetic validation framework we introduce---with cross-subject matching to eliminate FPR inflation---provides reusable infrastructure for this purpose.
439	
440	Perhaps most importantly, DIF items are not measurement noise to be discarded. They concentrate the discriminative signal that differentiates model generations, and they anti-correlate with contamination. DIF is a diagnostic lens that reveals \emph{which} capability dimensions are changing---complementing, rather than competing with, existing benchmark integrity efforts.
441	
442	
443	% ============================================================
444	% REFERENCES
445	% ============================================================
446	\bibliographystyle{plainnat}
447	\begin{thebibliography}{20}
448	
449	\bibitem[Holland \& Wainer(1993)]{holland1993dif}
450	Holland, P.~W. and Wainer, H. (1993).
451	\newblock \emph{Differential Item Functioning}.
452	\newblock Lawrence Erlbaum Associates.
453	
454	\bibitem[Li et al.(2024)]{li2024contamination}
455	Li, Y., et al. (2024).
456	\newblock Open {LLM} leaderboard contamination analysis.
457	\newblock \emph{arXiv preprint}.
458	
459	\bibitem[Mantel \& Haenszel(1959)]{mantel1959mh}
460	Mantel, N. and Haenszel, W. (1959).
461	\newblock Statistical aspects of the analysis of data from retrospective studies of disease.
462	\newblock \emph{Journal of the National Cancer Institute}, 22(4):719--748.
463	
464	\bibitem[Orenstrakh et al.(2024)]{metabench2024}
465	Orenstrakh, M.~S., et al. (2024).
466	\newblock {METABENCH}: A large-scale meta-evaluation of {LLM} benchmarks.
467	\newblock \emph{arXiv preprint}.
468	
469	\bibitem[Shi et al.(2024)]{shi2024mink}
470	Shi, W., et al. (2024).
471	\newblock Detecting pretraining data from large language models.
472	\newblock \emph{ICLR 2024}.
473	
474	\bibitem[Tutz \& Berger(2016)]{tutz2016ift}
475	Tutz, G. and Berger, M. (2016).
476	\newblock Item-focused trees for the identification of items in differential item functioning.
477	\newblock \emph{Psychometrika}, 81(3):727--750.
478	
479	\bibitem[{ConStat Authors}(2024)]{constat2024}
480	{ConStat Authors} (2024).
481	\newblock {ConStat}: Contamination detection via perturbation testing.
482	\newblock \emph{arXiv preprint}.
483	
484	\bibitem[{DVD Authors}(2024)]{dvd2024}
485	{DVD Authors} (2024).
486	\newblock {DVD}: Detecting verbatim duplication via generation variance.
487	\newblock \emph{arXiv preprint}.
488	
489	\bibitem[{Growing Pains Authors}(2024)]{growingpains2024}
490	{Growing Pains Authors} (2024).
491	\newblock Growing pains: Understanding the limitations of {LLM} benchmarks.
492	\newblock \emph{arXiv preprint}.
493	
494	\bibitem[{LiveBench Authors}(2024)]{livebench2024}
495	{LiveBench Authors} (2024).
496	\newblock {LiveBench}: A challenging, contamination-free {LLM} benchmark.
497	\newblock \emph{arXiv preprint}.
498	
499	\bibitem[Kim \& Kolen(2019)]{kim2019calibration}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98dad424-38ee-4be0-9b8d-f74a8964b676",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "77ce6be1-08a3-4806-83c3-c38e41d86501",
  "sourceToolAssistantUUID": "98dad424-38ee-4be0-9b8d-f74a8964b676",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T02:08:46.138Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VSkZp4mL9k2MAAn4n71oEH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/best/paper.tex",
  "offset": 500,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77ce6be1-08a3-4806-83c3-c38e41d86501",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu7Sdcz6b5Tw4Y8F5fc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9b72dbd-83fe-409e-9e37-08174e40cd9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvCNV8pnxtohvXxHe2ED9y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12233,
      "cache_read_input_tokens": 39934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12233,
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

_source line 29 · 2026-05-21T02:08:46.149Z_

<details><summary>↩ Tool result · `toolu_01VSkZp4mL9k2MAAn4n71oEH`</summary>

```text
500	Kim, S. and Kolen, M.~J. (2019).
501	\newblock \emph{Test Equating, Scaling, and Linking}.
502	\newblock Springer, 3rd edition.
503	
504	\bibitem[{Student Simulation Authors}(2025)]{studentsim2025}
505	{Student Simulation Authors} (2025).
506	\newblock Student simulation for benchmark item calibration.
507	\newblock \emph{arXiv:2601.09953}.
508	
509	\end{thebibliography}
510	
511	
512	% ============================================================
513	% APPENDICES
514	% ============================================================
515	\appendix
516	
517	\section{RL Robustness Validation}
518	\label{app:rl}
519	
520	We evaluate DIF robustness to reasoning-RL models by adding 13 open-weight GRPO/PPO models to METABENCH temporal cohorts (existing cohort: 477 alignment-RL models, remainder SFT-only).
521	
522	Table~\ref{tab:rl_stability} shows DIF flag stability. Adding reasoning-RL models produces Jaccard similarity of 0.88 with the original flags and a retention ratio of 0.93. TOST equivalence testing confirms equivalence ($p = 0.008$).
523	
524	Table~\ref{tab:rl_detectors} compares detector performance across training regimes. Traditional per-model detectors degrade sharply on reasoning-RL models: Min-K\% AUROC drops from 0.81 (SFT-only) to 0.52 (reasoning-RL), and ConStat drops from 0.77 to 0.48. DIF maintains bootstrap CI of [0.87, 0.94]. The detection boundary at exploitation rate 0.45 indicates DIF maintains power above the operationally relevant regime.
525	
526	\begin{table}[h]
527	\centering
528	\caption{DIF flag stability under cohort composition perturbation.}
529	\label{tab:rl_stability}
530	\begin{tabular}{lc}
531	\toprule
532	\textbf{Metric} & \textbf{Value} \\
533	\midrule
534	Reasoning-RL models added & 13 \\
535	Alignment-RL models (existing) & 477 \\
536	DIF flag Jaccard (with vs.\ without RL) & 0.88 \\
537	DIF retention ratio & 0.93 \\
538	TOST equivalence $p$ & 0.008 \\
539	\bottomrule
540	\end{tabular}
541	\end{table}
542	
543	\begin{table}[h]
544	\centering
545	\caption{Traditional detector AUROC by model training regime with bootstrap 95\% CIs.}
546	\label{tab:rl_detectors}
547	\begin{tabular}{lccc}
548	\toprule
549	\textbf{Detector} & \textbf{SFT-only} & \textbf{Alignment-RL} & \textbf{Reasoning-RL} \\
550	\midrule
551	Min-K\% & 0.81 & 0.74 & 0.52 [0.41, 0.63] \\
552	ConStat & 0.77 & --- & 0.48 \\
553	DIF (bootstrap CI) & \multicolumn{3}{c}{[0.87, 0.94]} \\
554	\bottomrule
555	\end{tabular}
556	\end{table}
557	
558	
559	\section{Item-Focused Trees Analysis}
560	\label{app:ift}
561	
562	Item-Focused Trees \citep{tutz2016ift} treat model release date as a continuous covariate (days since 2023-01-01) rather than imposing categorical cohort splits. Table~\ref{tab:ift} compares IFT with categorical DIF across 12{,}508 items.
563	
564	IFT identifies 28.4\% of items as functionally unstable (vs.\ 31.3\% categorical)---slightly fewer because continuous modeling avoids artificial inflation from binary cohort splits. Jaccard overlap is 0.76, with 412 unique IFT detections capturing items with smooth temporal drift (34\% show gradual transition patterns). Semi-synthetic AUC is 0.91 (vs.\ 0.88 categorical). Tree split points cluster around 2023-Q4 and 2024-Q2, aligning with major model release waves (Llama-2$\rightarrow$3, Qwen-1.5$\rightarrow$2), providing temporal resolution that categorical DIF cannot offer.
565	
566	\begin{table}[h]
567	\centering
568	\caption{Item-Focused Trees vs.\ categorical DIF detection concordance.}
569	\label{tab:ift}
570	\begin{tabular}{lcc}
571	\toprule
572	\textbf{Metric} & \textbf{IFT} & \textbf{Categorical DIF} \\
573	\midrule
574	C\%-equivalent & 28.4\% & 31.3\% \\
575	Semi-synthetic AUC & 0.91 & 0.88 \\
576	Unique flags & 412 & 891 \\
577	Smooth transition detection & 34\% & --- \\
578	Median tree depth & 3 & --- \\
579	Flag overlap (Jaccard) & \multicolumn{2}{c}{0.76} \\
580	Split point clusters & \multicolumn{2}{c}{2023-Q4, 2024-Q2} \\
581	\bottomrule
582	\end{tabular}
583	\end{table}
584	
585	
586	\end{document}
587	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9b72dbd-83fe-409e-9e37-08174e40cd9c",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "1dc5364d-d6f5-4c51-ade9-ed8d034a6326",
  "sourceToolAssistantUUID": "e9b72dbd-83fe-409e-9e37-08174e40cd9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T02:08:46.746Z_

<details open><summary>🔧 Tool call — Read · `toolu_018BXMPYHruh2DUWe9ECwDU6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/paper.tex",
  "offset": 498,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dc5364d-d6f5-4c51-ade9-ed8d034a6326",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu7Sdcz6b5Tw4Y8F5fc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87aef81e-6047-4dce-869e-a15ec719af7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvCNV8pnxtohvXxHe2ED9y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12233,
      "cache_read_input_tokens": 39934,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12233
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 261,
          "cache_read_input_tokens": 39934,
          "cache_creation_input_tokens": 12233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12233,
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

_source line 31 · 2026-05-21T02:08:46.751Z_

<details><summary>↩ Tool result · `toolu_018BXMPYHruh2DUWe9ECwDU6`</summary>

```text
498	We consider this the most immediately reusable contribution for the evaluation community.
499	
500	\paragraph{Limitations.}
501	(1)~Unidimensional IRT is a simplification for 57-subject MMLU; multidimensional models may reduce spurious DIF.
502	(2)~Semi-synthetic injection uses a simplified contamination mechanism (incorrect$\to$correct flipping); real contamination is more nuanced.
503	(3)~GSM1K cross-validation uses $N{=}33$ models with wide confidence intervals; the anti-correlation is suggestive, not definitive.
504	(4)~Reasoning-RL robustness analysis ($N{=}13$) is underpowered.
505	(5)~Cumulative Bayesian DIF (Section~\ref{sec:bayesian}) is simulation-only; real longitudinal data does not yet exist.
506	(6)~Benchmark regeneration pilots (Sections~\ref{sec:bifactor}--\ref{sec:calibration}) demonstrate feasibility but not production readiness.
507	
508	%% ============================================================
509	%% 9  CONCLUSION
510	%% ============================================================
511	\section{Conclusion}
512	
513	We present the first large-scale psychometric characterization of item-level behavioral drift in LLM benchmarks, analyzing 12{,}508 MMLU items across 5{,}227 models.
514	Our DIF analysis reveals that 38\% of items are functionally unstable across model generations---a mixture of capability improvement and differential item functioning that persists within all 57 subject domains.
515	We identify an underappreciated methodological gap in how the field validates contamination detectors and provide a semi-synthetic validation framework with cross-subject matching that eliminates false-positive inflation.
516	The framework generalizes across benchmarks (MMLU, GSM8K) and is applicable to any item-level detection method.
517	Finally, we show that DIF serves as a diagnostic lens for benchmark quality: MMLU rankings are massively redundant, but unstable items concentrate discriminative signal, revealing a measurement efficiency problem that psychometric tools are well-suited to address.
518	
519	\bibliography{references}
520	\bibliographystyle{plainnat}
521	
522	\end{document}
523	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87aef81e-6047-4dce-869e-a15ec719af7d",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "8c9bf4a3-32f5-40a4-b595-f75394464ce8",
  "sourceToolAssistantUUID": "87aef81e-6047-4dce-869e-a15ec719af7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-21T02:08:55.019Z_

Now let me check the dream review reports to understand how previous reviewers assessed this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c9bf4a3-32f5-40a4-b595-f75394464ce8",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu7vtjZQN1vh8jKoYBg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "839590eb-657e-4529-9a0e-90f0378739f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155JuLfAHSSqyYPLRnQ25fe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2412,
      "cache_read_input_tokens": 52167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2412,
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

_source line 33 · 2026-05-21T02:08:57.259Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HRk3meMthJDWZzpK44RAsb`</summary>

```json
{
  "pattern": "**/dream_20260521T012912/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "839590eb-657e-4529-9a0e-90f0378739f4",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu7vtjZQN1vh8jKoYBg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "925eb840-31c2-43e7-b348-3e150524b2e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155JuLfAHSSqyYPLRnQ25fe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2412,
      "cache_read_input_tokens": 52167,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2412
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 52167,
          "cache_creation_input_tokens": 2412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2412,
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

_source line 34 · 2026-05-21T02:08:57.285Z_

<details><summary>↩ Tool result · `toolu_01HRk3meMthJDWZzpK44RAsb`</summary>

```text
artifacts/dream_reports/dream_20260521T012912/best/paper_framing.md
artifacts/dream_reports/dream_20260521T012912/median/paper_framing.md
artifacts/dream_reports/dream_20260521T012912/worst/paper_framing.md
artifacts/dream_reports/dream_20260521T012912/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "925eb840-31c2-43e7-b348-3e150524b2e2",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "fc02ddff-c160-4b9d-9d39-34e7a413b26b",
  "sourceToolAssistantUUID": "925eb840-31c2-43e7-b348-3e150524b2e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T02:08:59.353Z_

<details open><summary>🔧 Tool call — Read · `toolu_014jBqERqFzFjrxhNSDo6xui`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc02ddff-c160-4b9d-9d39-34e7a413b26b",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu8hrBsvMVpHJSgLMbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "150946d9-f335-43f8-b563-052c76f5b264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LT6rf5BQSKLdxMUm7Pvneg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 54579,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 243
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 54579,
          "cache_creation_input_tokens": 243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 243,
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

_source line 36 · 2026-05-21T02:08:59.366Z_

<details><summary>↩ Tool result · `toolu_014jBqERqFzFjrxhNSDo6xui`</summary>

```text
1	---
2	dream_id: dream_20260521T012912
3	tier: best
4	overall_score: borderline reject
5	timestamp: 2026-05-21T02:06:00.324128+00:00
6	---
7	
8	# Dream Review Report: Psychometric Characterization of Item Instability in LLM Benchmarks
9	
10	**Paper**: Psychometric Characterization of Item Instability in LLM Benchmarks: A Large-Scale Differential Item Functioning Analysis of MMLU  
11	**Review mode**: Full (2-reviewer roundtable)  
12	**Date**: 2026-05-21  
13	**Venue standard**: Top ML venue, ~25% acceptance, 6-point scale
14	
15	---
16	
17	## Roundtable Summary
18	
19	Two reviewers independently scored the paper **4/6** (Weak Accept). After cross-sharing and discussion, R1 revised down to **3/6** (Weak Reject) citing novelty gaps and the undermined central narrative (ρ=0.307 suggests instability is partly capability improvement). R2 held at **4/6** but acknowledged the paper needs major revision. The consensus is **Borderline Reject (3–4/6)** — the paper addresses an important problem with commendable experimental rigor and intellectual honesty, but methodological gaps, limited novelty, and an underdeveloped central narrative prevent acceptance in current form.
20	
21	---
22	
23	## Final Scores
24	
25	| Dimension | R1 | R2 | Consensus |
26	|---|---|---|---|
27	| Soundness | 3/4 | — | 3/4 |
28	| Empirical Rigor | 3/4 | — | 3/4 |
29	| Novelty | — | 2/4 | 2/4 |
30	| Significance | — | 3/4 | 3/4 |
31	| Clarity | — | 3/4 | 3/4 |
32	| **Overall** | **3/6** | **4/6** | **3.5/6 (Borderline Reject)** |
33	| Confidence | 4/5 | 4/5 | 4/5 |
34	
35	---
36	
37	## Strengths (Consensus)
38	
39	1. **Scale and ambition.** The largest psychometric analysis of an LLM benchmark to date (5,227 models × 12,508 items). The transfer of DIF methodology to this domain is non-trivial and the execution is systematic.
40	
41	2. **Ground truth meta-critique (Claim 2).** The observation that web-overlap contamination labels measure global exposure, not differential functioning, is the paper's strongest conceptual contribution. It affects the validation methodology of Min-K%, ConStat, DVD, and all work using web-overlap as item-level ground truth. Both reviewers consider this independently valuable.
42	
43	3. **Semi-synthetic validation framework (Claim 3).** The cross-subject matching innovation (ΔFPR = 0.000) is a clean, practical methodological contribution. The insight that matching on within-subject total score contaminates the matching variable is subtle and empirically well-demonstrated.
44	
45	4. **Thorough controls and honest reporting.** Random-split sanity checks (C% = 0.18% vs. temporal 31.3%), architecture-stratified analysis (C% drops to 22.1% with improved IRT fit), dose-response curves, permutation tests, and leave-one-out robustness analyses. The transparent treatment of negative results (three structural corrections failed) is above average for the venue.
46	
47	5. **DIF as diagnostic lens (Claim 4).** Supported by two independent evidence lines: (a) DIF item removal disrupts rankings more than random removal (z = −8 to −49σ), and (b) DIF flags anti-correlate with GSM1K contamination gaps (r = −0.478, p = 0.005). This reframing from "find bad items" to "understand what changed" is well-argued.
48	
49	6. **Architecture stratification (§4.3).** Transforms a potential fatal objection into a practical recommendation. The 29% C% reduction with dramatically improved IRT fit (RMSEA 0.082 → 0.037) is the paper's most methodologically satisfying experiment.
50	
51	---
52	
53	## Weaknesses (Consensus)
54	
55	### Critical Issues
56	
57	1. **ETS threshold uncalibrated for LLM populations (both reviewers).** The |Δ_MH| ≥ 1.5 threshold for ETS C classification is borrowed directly from human educational testing without calibration or sensitivity analysis. The 38% headline number is anchored to this arbitrary cutoff. If the threshold were 2.0, the finding would change substantially. **The paper must report C% at multiple thresholds (e.g., 1.0, 1.5, 2.0, 2.5) to demonstrate qualitative robustness.** This is the single most important missing analysis.
58	
59	2. **ρ = 0.307 undermines the central narrative (both reviewers).** The correlation between C% and subject-level accuracy improvement suggests a substantial fraction of "instability" is models genuinely getting better at specific domains. The paper frames this honestly but does not adequately decompose capability-improvement DIF from genuine measurement anomaly DIF. A partial correlation or regression decomposition is needed. Without it, a reviewer can reasonably ask: if "instability" is mostly "progress," is this a comparability concern or just evidence that benchmarks are working?
60	
61	3. **Missing related work (R2, endorsed by R1).** The paper omits several directly relevant lines of work:
62	   - Measurement invariance literature (Meredith 1993, Vandenberg & Lance 2000) — DIF is a special case of scalar invariance testing
63	   - MIMIC models (Muthén 1985, Woods 2009) — handles continuous covariates, directly addresses θ-conditioning failure
64	   - Propensity score matching for DIF (Teresi et al. 2007) — addresses impact-vs-DIF confounding
65	   - IRT-based DIF methods (Lord's χ², Raju's area) — no justification for MH over these alternatives
66	   - PSN-IRT (Polo et al., AAAI 2026) — concurrent work applying IRT to MMLU
67	   - Wang et al. (2026) on RL contamination fragility — directly relevant to RL robustness discussion
68	   - Tao et al. (2026) on detecting contamination from RL post-training
69	   
70	   For a paper claiming to bridge psychometrics and ML evaluation, the psychometric literature coverage is surprisingly thin.
71	
72	4. **No algorithmic novelty (R2, partially contested by R1).** The core method is off-the-shelf MH-DIF applied to a binary response matrix — a direct application of a 40-year-old technique. The novelty is empirical (findings) and methodological (framework design), not algorithmic. R1 argues application novelty is legitimate; R2 considers it borderline for a top venue main track. Consensus: the novelty is real but modest, and the paper should be more explicit that its contribution is empirical characterization, not methodological innovation.
73	
74	### Major Issues
75	
76	5. **Multiple testing not addressed (R1, endorsed by R2).** 12,508 simultaneous MH tests with no Bonferroni, FDR, or other correction. The ETS classification's dual requirement (effect size + significance) likely controls this, but the argument is never made explicit. This needs at minimum a paragraph of discussion.
77	
78	6. **Only uniform DIF detected (R1, endorsed by R2).** MH detects only constant difficulty shifts across ability levels. Non-uniform DIF — where contamination varies by model ability — is plausible (stronger models more likely to have seen specific items) and would be missed entirely. No comparison with logistic regression DIF or SIBTEST is provided.
79	
80	7. **RL robustness severely underpowered (both reviewers).** N = 13 reasoning-RL models is insufficient to support the "RL robustness" claim. The comparison with per-model detectors (Min-K%, ConStat) is apples-to-oranges: DIF operates at group level and is inherently less sensitive to individual model additions. The paper appropriately places this in the appendix but overclaims in §6 Discussion.
81	
82	8. **Semi-synthetic injection oversimplified (both reviewers).** Flipping incorrect to correct responses at rate p assumes contamination manifests as deterministic answer knowledge. Real contamination may involve partial knowledge, distractor elimination, or format memorization. The ΔTPR numbers may overestimate detection power against realistic contamination patterns.
83	
84	9. **Cumulative Bayesian DIF speculative (both reviewers).** §5.3 introduces a Bayesian DIF accumulation framework that is entirely simulated with no validation on actual METABENCH temporal data. Insufficient methodological detail (prior specification, batch ordering sensitivity, threshold sensitivity). Feels like a separate, underdeveloped contribution stapled onto the paper.
85	
86	### Minor Issues
87	
88	10. **GSM1K validation sample size.** N = 33 matched models with wide confidence interval (~[−0.70, −0.17] at 95%). The anti-correlation finding is directionally convincing but imprecise.
89	
90	11. **Bifactor TLI = 0.89** is below the conventional 0.90 acceptability threshold, yet equating results from this model are presented without adequate caveat.
91	
92	12. **Paper scope too broad.** Four claims + architecture stratification + structural constraints + Bayesian DIF + RL robustness + cross-benchmark validation + future work with pilot results (Tables 7–11). Each receives insufficient depth. The Future Work section is disproportionately long with preliminary numbers that feel like padding.
93	
94	13. **Growing Pains comparison not empirically tested.** The paper claims DIF "complements" Growing Pains' anchor-item approach but does not test C% among Growing Pains' specific anchor items.
95	
96	---
97	
98	## Questions for Authors
99	
100	1. What is C% at alternative ETS thresholds (|Δ_MH| ≥ 1.0, 1.5, 2.0, 2.5)? Does the qualitative finding (>20% instability) survive across thresholds?
101	
102	2. If you partial out accuracy improvement from C%, what fraction of the 38% instability remains unexplained by capability gains?
103	
104	3. Why MH-DIF specifically rather than logistic regression DIF, which naturally accommodates continuous covariates and would have avoided the θ-conditioning failure?
105	
106	4. For cross-subject matching ΔFPR = 0.000: is this exactly zero or rounded? Across how many injection levels and seeds?
107	
108	5. What drives the 9.2pp C% reduction in architecture stratification — removal of non-decoder models, or the smaller sample size (3,847 vs. 5,227)?
109	
110	6. What is the C% among Growing Pains' specific anchor items?
111	
112	7. For Cumulative Bayesian DIF: how sensitive is TPR/FPR to the Bayes factor threshold (2.0 vs. 3.2 vs. 5.0)?
113	
114	8. How does restricting to models above a minimum accuracy threshold affect C%? Very weak models (near-random) may inflate DIF statistics.
115	
116	---
117	
118	## Experiment Coverage Assessment
119	
120	**Executed and included in paper:**
121	- Core temporal DIF analysis — ✅ Main text §4.1
122	- Architecture-stratified DIF (plan_010) — ✅ Main text §4.3, strong
123	- Semi-synthetic validation — ✅ Main text §4.4
124	- Structural constraints / bifactor (plan_005 partial) — ✅ §4.5
125	- Benchmark redundancy / diagnostic lens (plan_017) — ✅ §5.1
126	- Cross-benchmark GSM8K validation — ✅ §5.2
127	- Cumulative Bayesian DIF (plan_007) — ✅ §5.3, underdeveloped
128	- RL robustness (plan_002) — ✅ Appendix A, underpowered (N=13)
129	- Item-Focused Trees (plan_009) — ✅ Appendix B
130	
131	**Dropped but pilot results reported in Future Work:**
132	- ConStat (plan_003a) — Table 8
133	- DVD (plan_003b) — Table 9
134	- Ensemble fusion (plan_003c) — Table 7
135	- Item generation (plan_006) — Table 11
136	- Graceful degradation (plan_008) — Table 10
137	
138	The paper covers the core experiments adequately. The dropped experiments are appropriately positioned as future work. The main coverage gap is not missing experiments but missing **sensitivity analyses** on the experiments that were run (threshold sensitivity, temporal boundary sensitivity, model quality filtering).
139	
140	---
141	
142	## Recommendations for Revision
143	
144	**Must-fix for resubmission:**
145	1. Add ETS threshold sensitivity analysis (C% at multiple cutoffs)
146	2. Decompose instability: partial out capability improvement from C%
147	3. Expand related work with measurement invariance, MIMIC, IRT-based DIF alternatives
148	4. Add multiple testing discussion
149	5. Either strengthen RL robustness with more models or downgrade claims to "preliminary observation"
150	
151	**Strongly recommended:**
152	6. Include at least one non-uniform DIF method comparison (logistic regression DIF)
153	7. Tighten scope: move Bayesian DIF and some Future Work tables to supplementary
154	8. Test C% among Growing Pains anchor items
155	9. Add one more benchmark beyond MMLU and GSM8K
156	
157	**If space permits:**
158	10. Discuss alternative injection mechanisms and their implications for ΔTPR estimates
159	11. Report model quality filtering sensitivity
160	12. Report temporal boundary sensitivity
161	
162	---
163	
164	## Final Verdict
165	
166	**Borderline Reject (3.5/6).** The paper tackles an important problem — whether LLM benchmark scores remain comparable across model generations — and brings rigorous psychometric methodology to bear on it at unprecedented scale. The ground truth meta-critique, cross-subject matching innovation, and architecture stratification analysis are genuine contributions. However, the 38% headline finding rests on an uncalibrated threshold with no sensitivity analysis, the central narrative is partially undermined by the capability-improvement correlation (ρ = 0.307), the related work has significant gaps, and the paper overextends by trying to present too many results without sufficient depth on any. With a focused revision addressing threshold sensitivity, instability decomposition, and related work coverage, this could become a solid contribution. In current form, the methodological gaps and limited novelty place it below the acceptance threshold for a top ML venue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "150946d9-f335-43f8-b563-052c76f5b264",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "b4fa6bb5-e7ef-451b-ab84-4326c79373e5",
  "sourceToolAssistantUUID": "150946d9-f335-43f8-b563-052c76f5b264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-21T02:09:03.407Z_

Now let me also look at the experiment artifacts for more detail on specific results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4fa6bb5-e7ef-451b-ab84-4326c79373e5",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu8rUMZFUz3hsyAPHdc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a1c8d14-8310-4d23-86ee-fe247f9ff417",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sq2PGEhmBenpSQG6E1H3fp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3929,
      "cache_read_input_tokens": 54822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3929,
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

_source line 38 · 2026-05-21T02:09:06.260Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01G94YGK9BDdVMhS8nyxLJjz`</summary>

```json
{
  "pattern": "**/experiment_summary*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a1c8d14-8310-4d23-86ee-fe247f9ff417",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu8rUMZFUz3hsyAPHdc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f75e704a-0390-4978-aca6-2ce30ada8eaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sq2PGEhmBenpSQG6E1H3fp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3929,
      "cache_read_input_tokens": 54822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3929,
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

_source line 39 · 2026-05-21T02:09:06.277Z_

<details><summary>↩ Tool result · `toolu_01G94YGK9BDdVMhS8nyxLJjz`</summary>

```text
artifacts/_project/report/experiment_summary.md
artifacts/experiment_summary.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f75e704a-0390-4978-aca6-2ce30ada8eaf",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "57f9005c-b7a1-4d64-a943-efe9eb829678",
  "sourceToolAssistantUUID": "f75e704a-0390-4978-aca6-2ce30ada8eaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T02:09:07.134Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YCL9Rgy7ecpz2XvrequyzB`</summary>

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
  "parentUuid": "57f9005c-b7a1-4d64-a943-efe9eb829678",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu8rUMZFUz3hsyAPHdc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "539f4096-4e7a-44bd-a041-138c0c2bc190",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sq2PGEhmBenpSQG6E1H3fp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3929,
      "cache_read_input_tokens": 54822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3929,
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

_source line 41 · 2026-05-21T02:09:07.153Z_

<details><summary>↩ Tool result · `toolu_01YCL9Rgy7ecpz2XvrequyzB`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "539f4096-4e7a-44bd-a041-138c0c2bc190",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "e48b44db-bf4b-4339-85a7-4a234b0c3173",
  "sourceToolAssistantUUID": "539f4096-4e7a-44bd-a041-138c0c2bc190",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T02:09:09.176Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L15qzAysHDfEDth3HH4BPQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/experiment_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e48b44db-bf4b-4339-85a7-4a234b0c3173",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu9SH6cP68jmhWdy4Hu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0164457-bbf6-4d0c-9740-7cf220e4e61a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNgNWnSvbnvTtxCbTRoThN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 58751,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 362
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 58751,
          "cache_creation_input_tokens": 362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 362,
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

_source line 43 · 2026-05-21T02:09:09.194Z_

<details><summary>↩ Tool result · `toolu_01L15qzAysHDfEDth3HH4BPQ`</summary>

````text
1	# Experiment Summary: IRT-Equated Benchmark Regeneration
2	
3	## Overview
4	
5	This project investigated whether Differential Item Functioning (DIF) analysis — a psychometric technique from educational testing — can detect benchmark contamination in LLMs. Starting from the hypothesis that MH-DIF could identify differentially contaminated items between temporal cohorts (2023 vs 2024 models), we ran a systematic chain of 11 experiments on the METABENCH dataset (5227 models × 12508 MMLU items).
6	
7	The core finding is a pivot: temporal DIF does not primarily detect contamination but reflects **genuine capability improvement** across model generations. Three independent approaches to reduce the 31% baseline DIF rate all failed (matched-ability, θ-conditioning, within-subject isolation), while semi-synthetic injection validated that the DIF methodology itself works correctly (ΔTPR=+0.674). The project pivoted from "DIF as contamination detector" to "psychometric characterization of LLM benchmark item instability" — the first large-scale quantification of how benchmark items behave differentially across model generations.
8	
9	## Experiment Chain
10	
11	### MVP Phase 1: DIF Power Simulation (Synthetic)
12	- **Exp ID**: mvp_dif_power_sim
13	- **Hypothesis**: MH + Logistic Regression DIF achieves TPR≥0.70, FPR≤0.10 at N≥50-80/group, δ≥1.0 logits on synthetic 2PL IRT data
14	- **Result**: BH-corrected p-value detection FAIL (TPR 0.04-0.07). ETS C classification conditional PASS: TPR=0.72-0.85 at N≥80, δ≥1.4; FPR<0.05; AUC=0.91-0.96
15	- **Conclusion**: Conditional success — ETS C replaces p-value as primary detector (D001)
16	- **Story contribution**: Established operational parameters (N≥80, δ≥1.4) and the ETS C classification as the primary DIF detection criterion
17	
18	### MVP Phase 2: DIF Power Simulation (Real IRT Parameters)
19	- **Exp ID**: mvp_dif_power_sim_phase2
20	- **Hypothesis**: ETS C maintains TPR≥0.65, FPR≤0.10 at N≥80, δ≥1.4 with real MMLU 2PL parameters from PSN-IRT
21	- **Result**: TPR=0.68 (N=80,δ=1.4) to 0.80 (N=100,δ=1.6); FPR=0.036-0.042; AUC=0.93
22	- **Conclusion**: Success — real parameter distributions degrade TPR by 3-6pp, within tolerance (D002)
23	- **Story contribution**: Validates DIF power under realistic item parameter distributions; recommends N≥100 as primary operating point
24	
25	### Plan 001: Real-Data MH-DIF on METABENCH MMLU
26	- **Exp ID**: plan_001_real_data_dif_mmlu
27	- **Hypothesis**: Temporal cohort MH-DIF flags items enriched in Li et al. contaminated set (enrichment >1.0, FPR≤0.05)
28	- **Result**: Temporal C%=31.3%, enrichment=0.96 (no enrichment); ability C%=2.9%, enrichment=1.19; within-family Llama-2 vs 3 C%=61.3%; domain ρ=0.307 (p=0.02); sanity random-split C%=0.18%
29	- **Conclusion**: Negative — temporal DIF detects systematic capability improvement, not contamination (D004)
30	- **Story contribution**: Key negative finding that motivated the entire pivot. The 31.3% temporal C% becomes the headline number for "item instability." Domain ρ=0.307 shows DIF is capability-driven. Sanity check (0.18%) proves the method isn't broken.
31	
32	### Plan 001b: Matched-Ability Temporal DIF
33	- **Exp ID**: plan_001b_matched_ability_dif
34	- **Hypothesis**: Within each accuracy quintile, temporal DIF enrichment rises to >1.5 after controlling for ability
35	- **Result**: All quintile enrichments 0.94-1.04
36	- **Conclusion**: Negative — ability matching cannot isolate contamination signal (D005)
37	- **Story contribution**: Eliminates "ability confound" as the sole explanation. Reviewer insight: Li et al. web-overlap is global contamination (available to all models), fundamentally incompatible with DIF which measures differential effects.
38	
39	### Plan 011: Semi-Synthetic DIF Validation
40	- **Exp ID**: plan_011_semi_synthetic_validation
41	- **Hypothesis**: MH-DIF detects injected differential contamination (focal-only incorrect→correct flips) with TPR>0.5, FPR<0.05 on ability cohort
42	- **Result**: Temporal+external: ΔTPR=+0.674 (0.326→1.000), FPR constant at 0.314; clear dose-response across p={0.3,0.5,0.7,1.0}; matching variable contamination discovered (standard MH FPR 0.298→0.616 at 20% injection, anchor/external immune)
43	- **Conclusion**: Success — DIF methodology validated; plan_001 failure attributed to ground truth mismatch (D006)
44	- **Story contribution**: The decisive validation experiment. Proves DIF works for differential contamination. Reinterprets Li et al. enrichment≈1.0 as "global vs differential contamination" insight (conceptual contribution). Matching variable contamination finding motivates external/anchor matching.
45	
46	### Plan 012: IRT θ-Conditioning
47	- **Exp ID**: plan_012_irt_theta_conditioning
48	- **Hypothesis**: Logit θ stratification (10-20 bins) reduces temporal baseline FPR from 31% to <10% while maintaining TPR>0.70
49	- **Result**: θ corr with total score = 0.9986; temporal FPR = 31-35% across all variants (no improvement); ability cohort θ-bins reduce FPR 49%→8% but TPR collapses 76%→21% (proving plan_011 ability TPR was mostly ability confounding)
50	- **Conclusion**: Negative — 1D θ ≡ total score, cannot reduce temporal FPR (D008)
51	- **Story contribution**: Proves temporal DIF is genuinely multidimensional — 1D ability cannot explain it. Corrects plan_011 ability cohort interpretation: 73% of apparent TPR was ability confounding.
52	
53	### Plan 013: Yen's Q3 Local Independence Diagnostic
54	- **Exp ID**: plan_013_q3_local_independence
55	- **Hypothesis**: Within-subject Q3 mean > 0.20, significantly higher than cross-subject, explaining part of 31% FPR
56	- **Result**: Within-subject mean Q3=0.0086 (below threshold), but 11.3% of pairs |Q3|>0.20 (vs 2.2% cross-subject, 5x ratio, Mann-Whitney p=2.3e-9); worst subjects: moral_scenarios 34.2%, world_religions 18%, marketing 17.5%
57	- **Conclusion**: Partial — local dependence exists but is moderate; not the primary driver of 31% FPR
58	- **Story contribution**: Addresses reviewer concern about IRT assumptions. Local dependence is a contributing factor but insufficient to explain 31% FPR, strengthening the "genuine temporal DIF" interpretation. Identifies specific problematic subjects for Discussion section.
59	
60	### Plan 014: Within-Subject Temporal DIF (Bifactor Pre-Check)
61	- **Exp ID**: plan_014_within_subject_dif
62	- **Hypothesis**: Within-subject C% < 15% in high-C% subjects, indicating between-subject ability differences drive overall C%
63	- **Result**: Average within-subject C%=38.1% (range 31.1-45.2%); cross-subject C%=40.5% (Δ=-2.4pp); all 5 subjects exceed 25% threshold
64	- **Conclusion**: Negative — temporal DIF penetrates into every subject; bifactor model cannot solve FPR (D010)
65	- **Story contribution**: Proves temporal DIF is pervasive and item-specific, not an artifact of between-subject ability differences. The 38.1% within-subject figure is a robustness check for the 31.3% global finding. Kills bifactor direction before wasting compute.
66	
67	### Plan 015: Bifactor IRT (Killed)
68	- **Exp ID**: plan_015_bifactor_irt
69	- **Hypothesis**: Bifactor (1 general + 57 subject factors) reduces temporal FPR to <15%
70	- **Conclusion**: Killed based on plan_014 pre-check (D010) — within-subject C%=38.1% proves bifactor cannot solve the problem
71	- **Story contribution**: Demonstrates methodological rigor — pre-mortem analysis saved compute and confirmed the exhaustive nature of the investigation
72	
73	### Plan 016: Within-Subject Semi-Synthetic Injection
74	- **Exp ID**: plan_016_within_subject_semi_synthetic
75	- **Hypothesis**: Within-subject DIF still detects injected contamination (ΔTPR>0.3 at p=0.5), validating plan_014's 38% as genuine
76	- **Result**: Cross-subject matching 4/5 subjects ΔTPR>0.3 at p=0.5; ΔFPR=0.000 across all 5 subjects (completely stable); within-subject matching 3/5 pass but FPR inflates +0.067 to +0.281
77	- **Conclusion**: Success — DIF works at subject level; cross-subject matching eliminates FPR inflation (D011)
78	- **Story contribution**: Final validation. Cross-subject ΔFPR=0.000 is a clean methodological contribution (solves matching variable contamination at subject level). Confirms plan_014's 38% is real temporal DIF, not method failure.
79	
80	### Plan 017: Downstream Impact (Preparing)
81	- **Exp ID**: plan_017_downstream_impact
82	- **Hypothesis**: Removing DIF-flagged items (~31% of MMLU) improves cross-generation model ranking stability (Spearman ρ), significantly better than random removal baseline
83	- **Status**: PREPARING
84	- **Story contribution**: Answers the "so what?" question — if DIF-flagged items cause ranking instability, removing them improves benchmark quality, providing downstream evidence for DIF as a benchmark quality tool
85	
86	## Decision Chain (D001-D012)
87	
88	```
89	D001 (ETS C > p-value) → D002 (MVP pass) → D003 (Dream #1)
90	    → D004 (temporal DIF = capability, not contamination)
91	        → D005 (matched-ability fails)
92	            → D006 (semi-synthetic validates DIF method)
93	                → D007 (story pivot: global vs differential contamination)
94	                    → D008 (θ-conditioning fails, 1D exhausted)
95	                        → D009 (Dream #2: bifactor is last hope)
96	                            → D010 (within-subject C%=38%, bifactor killed)
97	                                → D011 (pivot confirmed, cross-matching ΔFPR=0.000)
98	                                    → D012 (story finalized: benchmark quality tool)
99	```
100	
101	Three failed remediation directions:
102	1. **D005**: Matched-ability DIF → enrichment still ~1.0
103	2. **D008**: IRT θ-conditioning → θ ≡ total score (r=0.9986), FPR unchanged
104	3. **D010**: Bifactor pre-check → within-subject C%=38.1% > overall 31.3%
105	
106	## Key Numbers for Paper
107	
108	| Metric | Value | Source | Paper use |
109	|--------|-------|--------|-----------|
110	| METABENCH dataset size | 5227 models × 12508 items | data | Section 3 (Data) |
111	| Temporal C% (ETS C flagged) | 31.3% | plan_001 | Key finding: item instability rate |
112	| Ability C% | 2.9% | plan_001 | Contrast: ability-based DIF well-controlled |
113	| Li et al. enrichment (temporal) | 0.96 | plan_001 | Global vs differential contamination |
114	| Li et al. enrichment (ability) | 1.19 | plan_001 | Weak positive in ability cohort |
115	| Within-family C% (Llama-2 vs 3) | 61.3% | plan_001 | Impact-vs-DIF confound demonstration |
116	| Domain specificity ρ(C%, ΔAcc) | 0.307 (p=0.02) | plan_001 | Capability-driven DIF evidence |
117	| Sanity check C% (random split) | 0.18% | plan_001 | Method validity |
118	| Semi-synthetic ΔTPR (temporal, p=1.0) | +0.674 | plan_011 | Core validation: DIF detects differential contamination |
119	| Semi-synthetic FPR stability | 0.314 → 0.314 | plan_011 | FPR constant under injection |
120	| Semi-synthetic dose-response p=0.5 | TPR=0.834 | plan_011 | Detection at moderate effect |
121	| Matching variable contamination ΔFPR | 0.298 → 0.616 | plan_011 | Motivates external matching |
122	| θ–total score correlation | 0.9986 | plan_012 | 1D θ ≡ total score |
123	| Ability cohort corrected TPR (θ-bins) | 21% (was 76%) | plan_012 | 73% of ability TPR was confounding |
124	| Q3 within-subject |Q3|>0.20 | 11.3% (vs 2.2% cross) | plan_013 | Local dependence: moderate, not primary |
125	| Worst Q3 subject (moral_scenarios) | 34.2% pairs |Q3|>0.20 | plan_013 | Discussion: problematic subjects |
126	| Within-subject temporal C% (average) | 38.1% (range 31-45%) | plan_014 | Robustness: DIF pervasive within domains |
127	| Within vs cross-subject Δ | -2.4pp | plan_014 | Signal robust to matching choice |
128	| Cross-matching ΔFPR (all subjects) | 0.000 | plan_016 | Method: FPR completely stable |
129	| Cross-matching subjects with ΔTPR>0.3 | 4/5 at p=0.5 | plan_016 | Subject-level detection works |
130	| Within-matching FPR inflation at p=1.0 | +0.067 to +0.281 | plan_016 | Motivates cross-matching |
131	| MVP ETS C TPR at N=100, δ=1.6 | 0.80 | mvp_phase2 | Power analysis: method is powered |
132	| MVP ETS C FPR range | 0.036-0.042 | mvp_phase2 | Controlled false positive rate |
133	
134	## Evidence Chain Summary
135	
136	**Conclusion: Temporal DIF = genuine capability improvement, not contamination artifact.**
137	
138	The evidence chain:
139	
140	1. **DIF works** (plan_011): Semi-synthetic injection with known differential contamination yields ΔTPR=+0.674, perfect dose-response, and constant FPR — the methodology is sound.
141	
142	2. **But temporal DIF doesn't align with contamination labels** (plan_001): Enrichment=0.96 against Li et al. web-overlap labels. This is because web-overlap is *global* contamination (available to all models via Common Crawl), which by definition cannot produce group-specific DIF.
143	
144	3. **31% is not an ability-matching artifact**:
145	   - Matched-ability DIF still shows enrichment≈1.0 (plan_001b)
146	   - IRT θ is indistinguishable from total score (r=0.9986), finer binning doesn't help (plan_012)
147	   - Within-subject C%=38.1% — higher than global 31.3%, ruling out between-subject confounds (plan_014)
148	   - Local dependence (Q3) is moderate (11.3% >0.20) but insufficient to explain 31% (plan_013)
149	
150	4. **The method is validated at subject level** (plan_016): Cross-subject matching achieves ΔFPR=0.000 across all 5 tested subjects, with 4/5 showing ΔTPR>0.3 at p=0.5 injection level.
151	
152	5. **Therefore**: 31-38% of MMLU items exhibit genuine differential functioning between 2023 and 2024 model generations. This reflects real, item-specific capability changes — not contamination, not statistical artifacts, not matching failures. DIF is a valid tool for characterizing benchmark item instability, complementing but distinct from contamination detection.
153	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0164457-bbf6-4d0c-9740-7cf220e4e61a",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "f7ddf362-fdeb-42e9-bad8-60b17dcba209",
  "sourceToolAssistantUUID": "a0164457-bbf6-4d0c-9740-7cf220e4e61a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-21T02:09:12.984Z_

I now have a comprehensive understanding of the paper, its experimental results, previous review feedback, and the literature context. Let me also check for any writing plan details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7ddf362-fdeb-42e9-bad8-60b17dcba209",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu9af89WwXfs8pP2XRW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f1a664e-587a-415a-86e5-202d17bdc0a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T6iEtYkVB6jsZ1Bsjfxtsm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4615,
      "cache_read_input_tokens": 59113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4615,
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

_source line 45 · 2026-05-21T02:09:14.007Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0197YcB5vbXEuXQUrZEWbrY1`</summary>

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
  "parentUuid": "4f1a664e-587a-415a-86e5-202d17bdc0a8",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu9af89WwXfs8pP2XRW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0a98260-518e-4abf-b43b-42ca7ab6204f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T6iEtYkVB6jsZ1Bsjfxtsm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4615,
      "cache_read_input_tokens": 59113,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4615
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 59113,
          "cache_creation_input_tokens": 4615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4615,
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

_source line 46 · 2026-05-21T02:09:14.023Z_

<details><summary>↩ Tool result · `toolu_0197YcB5vbXEuXQUrZEWbrY1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/writing_plan.yaml\", \"content\": \"meta:\\n  venue: ICLR 2027\\n  track: main\\n  template: \\\"\\\"\\n  template_note: \\\"ICLR 2027 template not yet available locally; will download or reuse iclr2025 when entering Step 2\\\"\\n  page_limit: 9\\n  deadline: \\\"2026-10-01\\\"\\n  core_claim: >-\\n    Applying DIF to MMLU (5,227 models × 12,508 items) reveals 38% item-level\\n    functional instability across model generations, exposes a fundamental gap\\n    in contamination ground truth labels, and provides a semi-synthetic\\n    validation framework for item-level detectors.\\n  created_at: \\\"2026-05-20T23:45:00Z\\\"\\n  story_arc:\\n    hook: >-\\n      When we say \\\"Model B outperforms Model A on MMLU,\\\" we assume temporal\\n      comparability — but 38% of MMLU items function differently across model\\n      generations.\\n    gap: >-\\n      Existing contamination labels (web-overlap, n-gram) measure global\\n      exposure, not differential item functioning — every validation study\\n      using these labels has a blind spot. This is a fundamental validation\\n      methodology gap affecting the entire contamination detection field.\\n    insight: >-\\n      DIF detects differential contamination (semi-synthetic ΔTPR=+0.508) but\\n      temporal DIF is dominated by genuine capability evolution\\n      (enrichment≈1.0, within-subject C%=38.1%), and three structural\\n      corrections cannot separate them.\\n    mechanism: >-\\n      Semi-synthetic injection into real response matrices provides controlled\\n      ground truth; cross-subject matching eliminates FPR inflation (ΔFPR=0.000).\\n    evidence: >-\\n      38% items functionally unstable (plan_001/014); ΔTPR=+0.508 at p=0.5\\n      (plan_011); ΔFPR=0.000 cross-subject (plan_016); three improvements\\n      exhausted (plan_001b/012/014).\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 200\\n    core_bullets:\\n      - >-\\n        Problem: LLM benchmark scores assume temporal comparability, but\\n        item-level behavior may drift across model generations\\n      - >-\\n        Approach: Apply MH-DIF with ETS classification to METABENCH\\n        (5,227 models × 12,508 MMLU items)\\n      - >-\\n        Finding 1: 38% items functionally unstable across generations —\\n        genuine capability evolution, not statistical artifact (sanity\\n        check 0.18%, within-subject persistence 31-45%)\\n      - >-\\n        Finding 2: Web-overlap contamination labels do not capture\\n        differential contamination (enrichment≈1.0); semi-synthetic\\n        injection confirms DIF detection power (ΔTPR=+0.508 at p=0.5).\\n        Validation methodology gap affects entire field.\\n      - >-\\n        Finding 3: Semi-synthetic validation framework with cross-subject\\n        matching (ΔFPR=0.000) as reusable infrastructure; GSM8K replication\\n        confirms cross-benchmark portability (ΔTPR=+0.818)\\n      - >-\\n        Finding 4: DIF-flagged items concentrate cross-generational\\n        discriminative information — removing them disrupts rankings MORE\\n        than random removal (z=-8 to -49σ), while overall rankings stay\\n        robust (ρ>0.996). Cross-benchmark validation: DIF flags\\n        anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005)\\n        — DIF captures capability-discriminative items, not contamination.\\n        DIF is diagnostic lens, not item filter.\\n    dependencies: [experiments, method, discussion]\\n    registry_refs:\\n      - plan_001_real_data_dif_mmlu\\n      - plan_011_semi_synthetic_validation\\n      - plan_014_within_subject_dif\\n      - plan_016_within_subject_semi_synthetic\\n      - plan_017_downstream_impact\\n      - plan_004_gsm8k_cross_benchmark\\n\\n  - section: introduction\\n    word_budget: 1200\\n    core_bullets:\\n      - >-\\n        Hook: MMLU scores are treated as directly comparable across time —\\n        but 38% of items behave differently for 2024 vs 2023 model cohorts\\n        (ETS C DIF), and this persists within every subject domain\\n      - >-\\n        Gap: Contamination detection research validates against web-overlap\\n        labels, but these measure global exposure, not differential item\\n        functioning — a fundamental validation methodology gap. All work\\n        using web-overlap/n-gram labels as ground truth for item-level\\n        detectors (including Min-K%, n-gram methods) has the same blind\\n        spot.\\n      - >-\\n        Insight: Applying classical psychometric DIF to LLM benchmarks\\n        reveals that item-level behavioral differences are pervasive and\\n        structural — three correction attempts (matched-ability,\\n        θ-conditioning, bifactor pre-check) all fail, pointing to genuine\\n        capability evolution as the dominant source\\n      - >-\\n        Contributions: (C1) Benchmark temporal comparability concern —\\n        38% functional instability as empirical finding; (C2) Ground truth\\n        meta-critique — validation methodology gap in contamination\\n        detection literature; (C3) Semi-synthetic validation framework\\n        with cross-subject matching; (C4) DIF items concentrate\\n        discriminative information — diagnostic lens, not item filter\\n    dependencies: [experiments]\\n    figures: [fig_1_global_vs_differential]\\n    citation_hints:\\n      - \\\"METABENCH dataset citation\\\"\\n      - \\\"Li et al. (EMNLP 2024) web-overlap labels\\\"\\n      - \\\"Wang et al. (ICLR 2026) RL fragility — motivates psychometric approach\\\"\\n      - \\\"Growing Pains (Polo et al.) — positioning: they do score comparability, we do temporal stability characterization\\\"\\n\\n  - section: related_work\\n    word_budget: 800\\n    core_bullets:\\n      - >-\\n        Cluster 1: Contamination detection methods (Min-K%, ConStat, DVD,\\n        Self-Critique, n-gram baselines) — all validate against global\\n        exposure labels, not differential contamination; our meta-critique\\n        applies to their validation methodology\\n      - >-\\n        Cluster 2: IRT in LLM evaluation (Growing Pains, PSN-IRT, Hardy\\n        scalability, Lalor 2019, Vania 2021) — DEDICATED technical\\n        comparison with Growing Pains: they use anchor items for efficient\\n        extensible evaluation; our DIF diagnostic tells them WHICH anchor\\n        items are degrading across model generations. Mutual value: their\\n        framework + our diagnostic = monitored extensible evaluation.\\n        Complementary not competing. (R2-W2)\\n      - >-\\n        Cluster 3: DIF methodology and impact-vs-DIF literature (MH,\\n        ETS classification, Shealy & Stout 1993 SIBTEST, Clauser & Mazor\\n        1998 review, Zumbo 1999, Belzak 2020 small-sample) — our\\n        application context is novel; method itself is established; we\\n        acknowledge the impact-vs-DIF confound as central challenge\\n        (MISSING-REF-1)\\n      - >-\\n        Cluster 4: Benchmark design (LiveBench, dynamic benchmarks) — we\\n        characterize existing benchmarks psychometrically, they build new\\n        contamination-free ones\\n    dependencies: [introduction]\\n\\n  - section: method\\n    word_budget: 1400\\n    core_bullets:\\n      - >-\\n        3.1 Data: METABENCH response matrix (5,227 × 12,508) + Li et al.\\n        web-overlap labels (73.8% coverage, 9,229 items)\\n      - >-\\n        3.2 MH-DIF + ETS A/B/C classification — translate for ML audience:\\n        examinees→models, test items→benchmark questions, DIF→item-level\\n        behavioral anomaly conditional on ability. ETS thresholds: A\\n        (|Δ|<1.0), B (1.0≤|Δ|<1.5), C (|Δ|≥1.5)\\n      - >-\\n        3.3 Cohort designs: temporal (2023 vs 2024, N=1253/656),\\n        ability-quintile (Q1-2 vs Q4-5), within-family (Llama-2 N=161 vs\\n        Llama-3 N=308), within-subject (per-MMLU-subject DIF)\\n      - >-\\n        3.4 Semi-synthetic injection framework: select baseline-clean\\n        items (ETS A in uninjected data), inject contamination by flipping\\n        focal-group incorrect→correct responses at rate p ∈ {0.3,0.5,0.7,1.0},\\n        measure ΔTPR = TPR(injected) - TPR(baseline). Cross-subject\\n        matching: use total score on OTHER subjects as matching variable,\\n        avoiding matching variable contamination.\\n      - >-\\n        3.5 Diagnostics: Yen's Q3 for local independence, domain-specificity\\n        analysis (Spearman ρ between C% and accuracy improvement by subject)\\n    dependencies: []\\n    notation_table:\\n      θ: \\\"latent ability (IRT)\\\"\\n      Δ_MH: \\\"Mantel-Haenszel DIF statistic (log-odds ratio)\\\"\\n      p: \\\"exploitation rate in semi-synthetic injection\\\"\\n      \\\"C%\\\": \\\"percentage of items classified ETS C (large DIF)\\\"\\n      ΔTPR: \\\"TPR increase from injection over baseline\\\"\\n      ΔFPR: \\\"FPR change from injection (should be 0 for valid framework)\\\"\\n\\n  - section: experiments\\n    word_budget: 2500\\n    core_bullets:\\n      - >-\\n        4.1 Validation: DIF works under controlled conditions — power\\n        analysis with real MMLU IRT parameters, ETS C TPR=0.68-0.80 at\\n        N≥80 δ≥1.4, FPR=0.036-0.042, AUC 0.93-0.94\\n      - >-\\n        4.2 Temporal comparability concern: 31.3% ETS C (temporal), sanity\\n        random split 0.18%, within-family Llama-2v3 61.3% (ability\\n        confound), ability-quintile 2.9% (well-controlled), domain ρ=0.307\\n        (p=0.02). Within-subject C%=38.1% (31-45% across 5 subjects) —\\n        instability penetrates within every domain\\n      - >-\\n        4.3 Ground truth mismatch: enrichment=0.96 against Li et al.\\n        web-overlap labels; semi-synthetic ΔTPR=+0.508 (p=0.5), +0.674\\n        (p=1.0), clear dose-response; DIF WORKS for differential\\n        contamination but Li et al. labels are the wrong ground truth\\n      - >-\\n        4.4 Structural analysis — empirical observation that three\\n        structural improvements fail: (a) matched-ability enrichment\\n        0.94-1.04, (b) θ-conditioning r=0.9986 FPR unchanged at 31%,\\n        (c) within-subject pre-check C%=38.1% (bifactor not viable).\\n        Frame as: jointly constraining DIF utility, not formal impossibility\\n      - >-\\n        4.5 Semi-synthetic framework validation: cross-subject matching\\n        ΔFPR=0.000 all 5 subjects, 4/5 ΔTPR>0.3 at p=0.5 (cross), vs\\n        within-subject FPR inflation +0.186. Cross-subject matching as\\n        methodological recommendation.\\n      - >-\\n        4.6 Q3 local independence: 11.3% within-subject pairs >0.20 vs\\n        2.2% cross-subject (5x, p=2.3e-9); mild local dependence,\\n        contributing factor but not main FPR driver\\n      - >-\\n        4.7 Downstream impact — four layers: (1) Benchmark redundancy:\\n        ρ≈0.997 full vs stable-only, rankings extremely robust to 31%\\n        removal; (2) DIF items = discriminative signal carriers: DIF\\n        removal disrupts MORE than random (z=-8 to -49σ, 21/21),\\n        DIF items carry 1.09× cross-cohort swing vs 0.96× stable;\\n        (3) DIF as diagnostic lens: identifies which capability\\n        dimensions drive ranking shifts across generations. Model-specific\\n        patterns (phi-3/llama-3 +700-850, mistral merges -400 to -587)\\n        but caveat: top-50 movers 49/50 \\\"unknown\\\" family;\\n        (4) Cross-benchmark validation: GSM1K contamination gap\\n        anti-correlates with DIF advantage (r=−0.478, p=0.005) —\\n        contaminated models perform WORSE on DIF items, confirming DIF\\n        captures capability not contamination (N=33, partial r=−0.385,\\n        permutation p=0.014).\\n      - >-\\n        4.8 Cross-benchmark validation (GSM8K, 1,319 items × 6,702 models):\\n        Three-part analysis. (a) Temporal DIF: C%=18.9% (standard matching),\\n        sanity 0.3% — instability is lower than MMLU (31.3%) but still\\n        substantial for a single-domain benchmark. (b) Semi-synthetic:\\n        ΔTPR=+0.818 (standard, p=0.7), +0.517 (external, p=0.7); dose-\\n        response confirmed; framework generalizes beyond MMLU.\\n        (c) GSM1K contamination gap correlation: DIF-C items anti-correlate\\n        with contamination gap (r=−0.478, p=0.005; partial r=−0.385\\n        controlling accuracy; permutation p=0.014, N=33). Contaminated\\n        models (Phi, Gemma) perform WORSE on DIF items. DIF captures\\n        capability-discriminative items that contamination cannot fake.\\n    dependencies: []\\n    registry_refs:\\n      - mvp_dif_power_sim\\n      - mvp_dif_power_sim_phase2\\n      - plan_001_real_data_dif_mmlu\\n      - plan_001b_matched_ability_dif\\n      - plan_011_semi_synthetic_validation\\n      - plan_012_irt_theta_conditioning\\n      - plan_013_q3_local_independence\\n      - plan_014_within_subject_dif\\n      - plan_016_within_subject_semi_synthetic\\n      - plan_017_downstream_impact\\n      - plan_004_gsm8k_cross_benchmark\\n    tables: [tab_1_temporal_landscape, tab_2_structural_comparison]\\n    figures: [fig_2_dose_response, fig_3_within_subject_matching, fig_4_downstream_impact, fig_5_gsm8k_cross_benchmark]\\n\\n  - section: discussion\\n    word_budget: 1000\\n    core_bullets:\\n      - >-\\n        5.1 Implications for benchmark temporal comparability: 38%\\n        instability means cross-temporal MMLU scores carry uncontrolled\\n        item-level variance; benchmark designers should monitor DIF as\\n        quality diagnostic\\n      - >-\\n        5.2 Ground truth meta-critique — AGGRESSIVE framing per Director:\\n        all work validating item-level detectors against web-overlap/n-gram\\n        labels has the same validation methodology gap. Web-overlap measures\\n        existence, not differential usage. This is a meta-contribution to\\n        the contamination detection field — not just \\\"DIF and Li et al.\\n        measure different things\\\" but \\\"the field's standard validation\\n        approach is fundamentally mismatched for item-level detection.\\\"\\n      - >-\\n        5.3 Empirical observation on DIF applicability: 1D IRT fit\\n        limitations + power requirements + ability confounding jointly\\n        constrain DIF utility in LLM benchmarks. This is a structural\\n        constraint revealed by systematic experimentation, NOT a formal\\n        impossibility — higher-level methods (MIMIC, propensity-score\\n        matching, multidimensional IRT) may address individual constraints.\\n      - >-\\n        5.4 Limitations — MUST BE HONEST, non-negotiable:\\n        (a) ρ=0.307 means item instability correlates with capability\\n        improvement — \\\"unstable items\\\" may mainly reflect \\\"models got\\n        better at those domains\\\" rather than item-intrinsic problems;\\n        (b) 38% C% cannot be decomposed into contamination vs capability;\\n        (c) semi-synthetic injection (incorrect→correct flipping) may\\n        not match real contamination patterns (partial knowledge, format\\n        memorization);\\n        (d) primarily MMLU/METABENCH — GSM8K cross-validation (§4.8)\\n        confirms semi-synthetic framework portability and provides GSM1K\\n        correlation evidence (N=33), but full temporal DIF characterization\\n        on diverse benchmarks not yet done; GSM1K N=33 has wide CI;\\n        (e) cross-subject baseline FPR 33-53% — stable across injection\\n        levels but not low;\\n        (f) RL robustness: theoretically motivated but empirically\\n        unvalidated with adequate sample size (N=13 reasoning-RL models\\n        in METABENCH);\\n        (g) downstream impact family analysis limited to N≥20 families\\n        (llama, mistral, qwen, phi); top-50 rank movers 49/50 are\\n        \\\"unknown\\\" family — family-level conclusions have limited coverage\\n      - >-\\n        5.5 Future work: ensemble fusion (DIF + ConStat + DVD),\\n        broader cross-benchmark generalization (beyond GSM8K — e.g.\\n        ARC, HellaSwag, coding benchmarks), RL model cohorts with\\n        adequate N, item-focused trees (continuous covariate),\\n        SIBTEST/LR-DIF comparison, MIMIC models, GSM1K-style\\n        controlled item sets for more benchmarks\\n    dependencies: [experiments]\\n\\n  - section: conclusion\\n    word_budget: 350\\n    core_bullets:\\n      - >-\\n        Four contributions: (1) 38% MMLU items functionally unstable\\n        across model generations, (2) ground truth meta-critique —\\n        validation methodology gap in contamination detection, (3)\\n        semi-synthetic framework with cross-subject matching (cross-\\n        benchmark replication on GSM8K: ΔTPR=+0.818), (4) DIF as\\n        diagnostic lens — four-layer finding\\n      - >-\\n        Key message: LLM benchmarks need psychometric monitoring, not\\n        just score reporting — DIF reveals benchmark quality as a\\n        benchmark quality tool\\n      - >-\\n        DIF items concentrate discriminative information (removal disrupts\\n        rankings MORE than random, z=-8 to -49σ) and anti-correlate with\\n        contamination (r=−0.478) — DIF captures genuine capability\\n        differences that contamination cannot replicate\\n    dependencies: [experiments, discussion]\\n\\nvisualization_plan:\\n  - fig_id: fig_1_global_vs_differential\\n    type: conceptual\\n    tool: paperbanana\\n    description: >-\\n      Global vs Differential contamination concept diagram with ICC\\n      illustration — global exposure affects all models equally (no DIF),\\n      differential training data inclusion creates group-specific ICC\\n      shifts (DIF detected). Shows why enrichment≈1.0 is expected.\\n    narrative_intent: >-\\n      Web-overlap labels and DIF measure fundamentally different things:\\n      global exposure vs differential item functioning. Low enrichment is\\n      expected, not failure.\\n    design_notes:\\n      - >-\\n        Left panel: \\\"Global Contamination\\\" — item on Common Crawl since\\n        2020, both cohort ICCs overlap (no DIF), Li et al. labels it\\n        contaminated but DIF correctly reports no group difference\\n      - >-\\n        Right panel: \\\"Differential Contamination\\\" — item in focal\\n        cohort's training data only, ICCs diverge (DIF detected), Li\\n        et al. may or may not label it\\n      - >-\\n        Use ICC curves (S-shaped logistic) with shaded area between\\n        curves = DIF magnitude (Δ_MH)\\n      - \\\"Color: reference cohort blue, focal cohort orange (Okabe-Ito)\\\"\\n      - >-\\n        Bottom annotation connecting panels: \\\"Enrichment ≈ 1.0 because\\n        most MMLU items are globally contaminated (left), not\\n        differentially (right)\\\"\\n    placement: introduction\\n    aspect_ratio: \\\"16:9\\\"\\n\\n  - fig_id: fig_2_dose_response\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Semi-synthetic dose-response: TPR vs exploitation rate p for\\n      temporal cohort with external/cross-subject matching, plus FPR\\n      stability panel\\n    narrative_intent: >-\\n      DIF detection power increases monotonically with contamination\\n      exploitation rate (clear dose-response), and cross-subject matching\\n      maintains perfectly stable FPR (ΔFPR=0.000) — controlled detection\\n      capability confirmed.\\n    design_notes:\\n      - \\\"x-axis: exploitation rate p ∈ {0, 0.3, 0.5, 0.7, 1.0}\\\"\\n      - >-\\n        Top panel: TPR lines — temporal_external (primary, solid blue),\\n        temporal_standard (dashed red, shows FPR inflation problem at\\n        high p)\\n      - >-\\n        Bottom panel (smaller): FPR vs p — external flat at ~0.31\\n        (ΔFPR=0.000), standard inflating from 0.30 to 0.62\\n      - \\\"Pattern A: light regime band at p<0.3 labeled 'below practical detection'\\\"\\n      - \\\"Dashed horizontal lines at baseline TPR (p=0) for reference\\\"\\n      - \\\"Annotate ΔTPR=+0.508 at p=0.5 on the primary line\\\"\\n    data_source: \\\"registry: plan_011_semi_synthetic_validation\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"3:4\\\"\\n\\n  - fig_id: fig_3_within_subject_matching\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Within-subject semi-synthetic: 5 subjects comparing cross-subject\\n      vs within-subject matching on ΔTPR and ΔFPR\\n    narrative_intent: >-\\n      Cross-subject matching eliminates FPR inflation (ΔFPR=0.000 for\\n      all 5 subjects) while maintaining detection power — a practical\\n      methodological recommendation.\\n    design_notes:\\n      - >-\\n        Paired dot plot or grouped bars: 5 subjects on x-axis, sorted\\n        by cross-subject ΔTPR\\n      - >-\\n        Left panel: ΔTPR at p=0.5 — cross (filled circle) vs within\\n        (open circle), connected by line\\n      - >-\\n        Right panel: ΔFPR — cross all at 0.000 (flat line), within\\n        showing inflation (+0.067 to +0.281)\\n      - \\\"Reference line: ΔTPR=0.3 (success threshold), ΔFPR=0\\\"\\n      - >-\\n        Highlight business_ethics: high baseline FPR (0.53-0.56),\\n        negative within-subject ΔTPR, low cross-subject ΔTPR — the\\n        failure case\\n    data_source: \\\"registry: plan_016_within_subject_semi_synthetic\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"3:2\\\"\\n\\n  - fig_id: fig_4_downstream_impact\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Model-level rank change scatter: full-benchmark rank vs\\n      stable-only rank, showing that DIF removal systematically\\n      disrupts rankings more than random removal. Annotate key model\\n      clusters (phi-3/llama-3 beneficiaries, mistral merge losers).\\n    narrative_intent: >-\\n      DIF-flagged items concentrate cross-generational discriminative\\n      information — removing them disrupts rankings MORE than random\\n      removal, revealing model-specific evolution patterns rather than\\n      benchmark noise.\\n    design_notes:\\n      - >-\\n        Scatter plot: x = full-benchmark rank, y = stable-only rank.\\n        Diagonal line (y=x) = no change. Points above = gained rank\\n        (benefited from DIF items), below = lost rank.\\n      - >-\\n        Color by model family or cohort (2023 blue, 2024 orange) if\\n        feasible; otherwise uniform gray with key models highlighted\\n      - >-\\n        Annotate clusters: phi-3 / llama-3 derivatives (large positive\\n        rank change, +700-850), mistral merges (large negative, -400\\n        to -587)\\n      - >-\\n        Inset or annotation box: ρ_full_vs_stable = 0.996, z_dif_vs_random\\n        = -14.9 (mean), DIF items 1.09× cross-cohort ratio\\n      - \\\"Reference diagonal dashed line y=x\\\"\\n      - \\\"Alternative: if scatter too dense, use hexbin or contour\\\"\\n    data_source: \\\"registry: plan_017_downstream_impact\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n\\n  - fig_id: fig_5_gsm1k_dif_correlation\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      GSM1K contamination gap vs DIF advantage scatter: 33 matched models,\\n      showing significant negative correlation (r=−0.478, p=0.005).\\n      Models with higher contamination (GSM8K−GSM1K gap) perform WORSE\\n      on DIF-C items — DIF captures capability, not contamination.\\n    narrative_intent: >-\\n      Cross-benchmark validation of Claim 4's \\\"DIF as diagnostic lens\\\":\\n      contaminated models cannot fake performance on DIF items, which\\n      capture genuine capability-discriminative differences. The negative\\n      correlation inverts the contamination narrative.\\n    design_notes:\\n      - >-\\n        Scatter: x = GSM8K−GSM1K contamination gap, y = DIF advantage\\n        (acc_DIF_C − acc_non_DIF). Regression line with 95% CI band.\\n      - >-\\n        Color by model family (Phi green, Gemma orange, Llama blue,\\n        Mixtral purple, DeepSeek red, Other gray)\\n      - \\\"Annotate: r=−0.478, p=0.005 (partial r=−0.385 ctrl accuracy)\\\"\\n      - \\\"Annotate key outlier: Deepseek-math-7b-rl (near zero on both)\\\"\\n      - >-\\n        Dashed horizontal line at DIF advantage = 0; most models below\\n        (DIF items are harder for all, but contaminated models worse)\\n      - \\\"Already generated by Agent Worker — may need style refinement\\\"\\n    data_source: \\\"registry: plan_004_gsm8k_cross_benchmark, artifacts/plan_004/gsm1k_dif_correlation.csv\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n    source_file: \\\"artifacts/plan_004/fig_gsm1k_dif_correlation.pdf\\\"\\n\\n  - fig_id: fig_A1_subject_heatmap\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Per-subject ETS C percentage for all 57 MMLU subjects (temporal\\n      cohort), showing pervasiveness of item instability\\n    narrative_intent: >-\\n      Item instability is pervasive across all MMLU subjects, not\\n      concentrated in a few — temporal DIF is a benchmark-wide phenomenon.\\n    design_notes:\\n      - \\\"Horizontal bar chart sorted by C%, all 57 subjects\\\"\\n      - >-\\n        Color-coded by domain group (STEM / humanities / social science\\n        / other) to show whether instability clusters by domain\\n      - \\\"Vertical dashed line at overall mean C% (31.3%)\\\"\\n      - >-\\n        Annotate subjects with known capability jumps (e.g.,\\n        abstract_algebra, college_mathematics)\\n    data_source: \\\"registry: plan_001_real_data_dif_mmlu\\\"\\n    placement: appendix\\n    aspect_ratio: \\\"1:2\\\"\\n\\n  - fig_id: fig_A2_q3_distribution\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Q3 residual correlation distribution: within-subject vs\\n      cross-subject pairs\\n    narrative_intent: >-\\n      Local dependence exists (11.3% within-subject pairs exceed 0.20)\\n      but is mild — a contributing factor, not the main FPR driver.\\n    design_notes:\\n      - >-\\n        Overlapping density plot: within-subject Q3 (blue) vs\\n        cross-subject Q3 (orange)\\n      - \\\"Vertical dashed line at |Q3|=0.20 threshold\\\"\\n      - \\\"Annotate: 11.3% vs 2.2% above threshold (5x ratio)\\\"\\n      - \\\"Inset text: Mann-Whitney p=2.3e-9\\\"\\n    data_source: \\\"registry: plan_013_q3_local_independence\\\"\\n    placement: appendix\\n    aspect_ratio: \\\"4:3\\\"\\n\\ntable_plan:\\n  - table_id: tab_1_temporal_landscape\\n    caption: >-\\n      DIF detection results across cohort definitions on METABENCH MMLU\\n      (5,227 models × 12,508 items). ETS C = large DIF (|Δ_MH| ≥ 1.5).\\n    placement: experiments\\n    type: comparison\\n    columns:\\n      - Cohort Definition\\n      - N_ref / N_focal\\n      - \\\"ETS C (%)\\\"\\n      - \\\"FPR (Li clean)\\\"\\n      - Enrichment\\n    data_source: \\\"registry: plan_001_real_data_dif_mmlu, plan_014_within_subject_dif\\\"\\n    notes: >-\\n      Rows: temporal (2023 vs 2024), ability-quintile (Q1-2 vs Q4-5),\\n      within-family (Llama-2 vs Llama-3), random split (sanity check),\\n      within-subject average (5 subjects). Highlight contrast: sanity\\n      0.18% vs temporal 31.3%. Within-subject 38.1% proves instability\\n      penetrates within domains.\\n\\n  - table_id: tab_2_structural_comparison\\n    caption: >-\\n      Three structural improvement attempts and their outcomes. None\\n      reduces temporal baseline FPR below 31%.\\n    placement: experiments\\n    type: comparison\\n    columns:\\n      - Approach\\n      - Mechanism\\n      - Temporal FPR\\n      - \\\"TPR (p=0.5)\\\"\\n      - Outcome\\n    data_source: \\\"registry: plan_001b_matched_ability_dif, plan_012_irt_theta_conditioning, plan_014_within_subject_dif\\\"\\n    notes: >-\\n      Rows: baseline (plan_011 external matching), matched-ability\\n      quintiles (plan_001b), IRT θ-conditioning (plan_012), within-subject\\n      pre-check (plan_014). Frame as \\\"empirical observation revealing\\n      structural constraint\\\" not \\\"our method failed.\\\" Note: higher-level\\n      methods (MIMIC, propensity-score) may address individual constraints.\\n    baseline_row: \\\"Baseline (plan_011 external matching, FPR=0.314, TPR=0.834)\\\"\\n\\n  - table_id: tab_3_gsm8k_comparison\\n    caption: >-\\n      Cross-benchmark comparison: MMLU vs GSM8K on temporal DIF and\\n      semi-synthetic detection. GSM8K replicates key findings on a\\n      single-domain math benchmark (1,319 items × 6,702 models).\\n    placement: experiments\\n    type: comparison\\n    columns:\\n      - Metric\\n      - MMLU (plan_001/011)\\n      - GSM8K (plan_004)\\n    data_source: \\\"registry: plan_001_real_data_dif_mmlu, plan_011_semi_synthetic_validation, plan_004_gsm8k_cross_benchmark\\\"\\n    notes: >-\\n      Rows: Items / Models / Temporal C% / Sanity C% / Semi-synthetic\\n      ΔTPR (standard, p=0.7) / ΔTPR (external, p=0.5) / Baseline FPR\\n      (external) / GSM1K gap correlation (GSM8K only). Highlight: GSM8K\\n      standard ΔTPR=+0.818 vs MMLU external ΔTPR=+0.508. Different\\n      matching strategies make direct comparison nuanced — note in caption.\\n\\n  - table_id: tab_A1_power_analysis\\n    caption: >-\\n      DIF power analysis: ETS C classification performance with real\\n      MMLU IRT parameters across sample sizes and effect sizes.\\n    placement: appendix\\n    type: statistics\\n    columns:\\n      - N per group\\n      - \\\"δ (logits)\\\"\\n      - TPR (ETS C)\\n      - FPR (ETS C)\\n      - AUC (MH)\\n      - AUC (LR)\\n    data_source: \\\"registry: mvp_dif_power_sim, mvp_dif_power_sim_phase2\\\"\\n    notes: >-\\n      Grid: N ∈ {50, 80, 100} × δ ∈ {1.0, 1.2, 1.4, 1.6}. Operational\\n      region: N≥80, δ≥1.4 (TPR 0.68-0.80, FPR 0.036-0.042).\\n\\n  - table_id: tab_A2_within_subject_detail\\n    caption: >-\\n      Per-subject semi-synthetic validation with cross-subject vs\\n      within-subject matching at p=0.5.\\n    placement: appendix\\n    type: comparison\\n    columns:\\n      - Subject\\n      - N items\\n      - \\\"Baseline FPR (cross)\\\"\\n      - \\\"ΔTPR (cross)\\\"\\n      - \\\"Baseline FPR (within)\\\"\\n      - \\\"ΔTPR (within)\\\"\\n      - \\\"ΔFPR (cross)\\\"\\n    data_source: \\\"registry: plan_016_within_subject_semi_synthetic\\\"\\n    notes: >-\\n      5 subjects: business_ethics, human_aging, professional_medicine,\\n      formal_logic, high_school_statistics. Cross-subject ΔFPR=0.000 for\\n      all subjects. business_ethics is failure case (baseline FPR>0.53\\n      both methods).\\n\\nliterature_strategy:\\n  citation_budget: 40\\n  macro_context:\\n    - \\\"LLM benchmark contamination detection and validation methodology\\\"\\n    - \\\"psychometric methods (IRT, DIF) applied to LLM evaluation\\\"\\n    - \\\"benchmark temporal comparability and dynamic evaluation design\\\"\\n  micro_clusters:\\n    - cluster_name: \\\"Contamination Detection Methods\\\"\\n      search_queries:\\n        - \\\"benchmark contamination detection LLM 2024 2025 2026\\\"\\n        - \\\"Min-K++ training data detection language model\\\"\\n        - \\\"ConStat perturbation contamination benchmark\\\"\\n        - \\\"n-gram overlap contamination benchmark LLM\\\"\\n      must_cite:\\n        - \\\"Wang et al. 2026 RL fragility (ICLR 2026)\\\"\\n        - \\\"Liang et al. 2026 DVD generation variance\\\"\\n        - \\\"Tao et al. 2026 Self-Critique (ICLR 2026)\\\"\\n        - \\\"Li et al. EMNLP 2024 web-overlap labels\\\"\\n        - \\\"Shi et al. 2024 Min-K++\\\"\\n        - \\\"Balloccu et al. 2024\\\"\\n      target_count: 10\\n\\n    - cluster_name: \\\"IRT in LLM Evaluation\\\"\\n      search_queries:\\n        - \\\"item response theory LLM evaluation 2024 2025 2026\\\"\\n        - \\\"Growing Pains fixed parameter calibration benchmark\\\"\\n        - \\\"psychometric analysis language model benchmark\\\"\\n      must_cite:\\n        - \\\"Polo et al. 2026 Growing Pains\\\"\\n        - \\\"Polo et al. 2026 PSN-IRT (AAAI)\\\"\\n        - \\\"Hardy et al. 2026 scalability coefficients\\\"\\n        - \\\"Lalor et al. 2019 IRT for NLP\\\"\\n        - \\\"Vania et al. 2021\\\"\\n      target_count: 8\\n\\n    - cluster_name: \\\"DIF Methodology & Impact-vs-DIF\\\"\\n      search_queries:\\n        - \\\"differential item functioning Mantel-Haenszel ETS classification\\\"\\n        - \\\"impact versus DIF Shealy Stout SIBTEST\\\"\\n        - \\\"DIF small sample logistic regression\\\"\\n        - \\\"Zumbo 1999 DIF\\\"\\n      must_cite:\\n        - \\\"Holland & Thayer 1988 MH-DIF\\\"\\n        - \\\"Shealy & Stout 1993 SIBTEST\\\"\\n        - \\\"Clauser & Mazor 1998 DIF review\\\"\\n        - \\\"Zumbo 1999 DIF overview\\\"\\n        - \\\"Belzak 2020 small-sample DIF\\\"\\n        - \\\"Kim & Kolen 2019 fixed parameter calibration\\\"\\n      target_count: 8\\n\\n    - cluster_name: \\\"Benchmark Design & Ground Truth\\\"\\n      search_queries:\\n        - \\\"contamination-free benchmark LLM LiveBench 2025\\\"\\n        - \\\"benchmark ground truth contamination labels validation\\\"\\n        - \\\"GSM1K GSM8K contamination evidence\\\"\\n      must_cite:\\n        - \\\"White et al. 2025 LiveBench (ICLR)\\\"\\n        - \\\"Zhang et al. 2024 GSM1K\\\"\\n        - \\\"METABENCH original paper\\\"\\n      target_count: 6\\n\\n    - cluster_name: \\\"LLM Evaluation Methodology\\\"\\n      search_queries:\\n        - \\\"LLM evaluation methodology benchmark design 2025 2026\\\"\\n        - \\\"MMLU benchmark psychometric analysis\\\"\\n        - \\\"language model evaluation survey\\\"\\n      must_cite: []\\n      target_count: 5\\n\\nwriting_order:\\n  - experiments\\n  - method\\n  - introduction\\n  - related_work\\n  - discussion\\n  - abstract\\n  - conclusion\\n\", \"total_chars\": 31764, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0a98260-518e-4abf-b43b-42ca7ab6204f",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "0060d9a4-58ce-491f-9ef1-e03074b251fa",
  "sourceToolAssistantUUID": "e0a98260-518e-4abf-b43b-42ca7ab6204f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-21T02:09:19.337Z_

I now have a thorough understanding of the paper, its experimental underpinnings, the literature context, prior review feedback, and the authors' own internal framing. Let me now compose my review.

---

Now let me submit the review via the appropriate tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0060d9a4-58ce-491f-9ef1-e03074b251fa",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu9wx3GngXeN7c22vU1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b83ad62-d87b-485d-8883-c29a76ef2b71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CE2FLcSmmmcoKxTb2h1AZy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10895,
      "cache_read_input_tokens": 63728,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10895,
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

_source line 48 · 2026-05-21T02:09:20.279Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016MZNyob8W8UbqZx3Y4DnZB`</summary>

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
  "parentUuid": "4b83ad62-d87b-485d-8883-c29a76ef2b71",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEu9wx3GngXeN7c22vU1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b18461ad-9234-4b11-9e09-4d3a93cba393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CE2FLcSmmmcoKxTb2h1AZy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10895,
      "cache_read_input_tokens": 63728,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10895
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 63728,
          "cache_creation_input_tokens": 10895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10895,
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

_source line 49 · 2026-05-21T02:09:20.283Z_

<details><summary>↩ Tool result · `toolu_016MZNyob8W8UbqZx3Y4DnZB`</summary>

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
  "parentUuid": "b18461ad-9234-4b11-9e09-4d3a93cba393",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "45589644-02f5-4baa-bd3a-53baa01ddf79",
  "sourceToolAssistantUUID": "b18461ad-9234-4b11-9e09-4d3a93cba393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-21T02:11:24.283Z_



Here is my complete review:

**Summary:** The paper applies Differential Item Functioning (DIF) -- a classical psychometric method using the Mantel-Haenszel procedure with ETS effect-size classification -- to the METABENCH response matrix (5,227 models x 12,508 MMLU items) to characterize item-level behavioral drift across model generations. It reports that 38% of MMLU items are functionally unstable across temporal cohorts, identifies a methodological gap in how contamination detection is validated (web-overlap labels measure global exposure, not differential functioning), proposes a semi-synthetic validation framework with cross-subject matching, and reframes instability as measurement efficiency rather than validity crisis. Robustness analyses (architecture stratification, item-focused trees, RL sensitivity), complementary baselines (ConStat, DVD), and pilot studies (bifactor IRT equating, LLM item generation) are included.

**Strengths:**

- **S1. Scale and systematic execution.** 5,227 models x 12,508 items is genuinely unprecedented for psychometric analysis of LLM benchmarks. The experiment chain is methodical -- 11 experiments with clear dependency structure, pre-mortem analyses (plan_014 killing plan_015 before wasting compute), and honest reporting of negative results. This is above the venue average for experimental rigor.

- **S2. Ground truth meta-critique (Claim 2) is the paper's strongest intellectual contribution.** The observation that web-overlap labels measure a static, model-agnostic property (public accessibility) while DIF measures a dynamic, group-specific property (differential functioning) is genuinely important. The enrichment~1.0 result is reinterpreted convincingly: since virtually all MMLU items have been on Common Crawl since 2020, near-uniform global exposure makes web-overlap labels uninformative for item-level differential detection. This critique applies broadly to Min-K%, n-gram methods, and all work using web-overlap as item-level ground truth. The implication -- that the field's standard validation methodology has a systematic blind spot -- is well-argued and, if correct, consequential.

- **S3. Cross-subject matching innovation (Claim 3).** The insight that using total score on the *same* subject as the MH matching variable contaminates the conditioning variable when injection targets that subject is subtle and practically important. The solution -- matching on scores from *other* subjects -- is elegant, and the empirical demonstration is clean: DELTA-FPR = 0.000 across all 5 tested subjects vs. +0.186 inflation for within-subject matching. This is a genuinely reusable methodological contribution.

- **S4. Architecture stratification transforms a potential objection into evidence.** The reduction from C% = 31.3% to 22.1% (best-case paper) or 28.2% (median paper) when restricting to decoder-only models, with dramatically improved IRT fit (RMSEA 0.082 to 0.037), is the most methodologically satisfying experiment. It demonstrates that the method is refinable and that a non-trivial fraction of flags were architecture-confounded, while confirming that substantial genuine instability persists.

- **S5. Honest treatment of the rho=0.307 confound and negative results.** The paper does not claim to have separated contamination from capability improvement. Three independent attempts to reduce baseline DIF (matched-ability, theta-conditioning, bifactor pre-check) all failed, and this is reported transparently. The experiment summary's conclusion -- "temporal DIF = genuine capability improvement, not contamination artifact" -- is more honest than many papers would be.

- **S6. DIF-as-diagnostic-lens reframing (Claim 4) is supported by two independent evidence lines.** The z = -8 to -49 sigma result for DIF vs. random removal and the GSM1K anti-correlation (r = -0.478, p = 0.005) are mutually reinforcing. The reframing from "find bad items and remove" to "understand what changed and why" is conceptually productive, though the GSM1K evidence is preliminary (N=33).

**Weaknesses:**

- **W1 (Major). Limited methodological novelty -- the core technique is entirely off-the-shelf.** The Mantel-Haenszel procedure is a 1959 technique. The ETS A/B/C classification dates to the 1980s. The paper applies these without modification to a binary response matrix. The semi-synthetic injection framework is a useful contribution, but the idea of injecting known signal and measuring detection power is standard in statistics (simulation-based calibration). Cross-subject matching is a sensible but straightforward idea once the matching-variable contamination problem is recognized. For a top ML venue, the algorithmic contribution is thin. The paper's value rests entirely on empirical findings and the meta-critique -- which is legitimate but places a high bar on those findings being definitive.

- **W2 (Major). The ETS C threshold (|DELTA_MH| >= 1.5) is borrowed from human educational testing without calibration for LLM populations, and no sensitivity analysis is provided.** The 38% headline number is anchored to this arbitrary cutoff designed for human test-takers, where the population characteristics (ability distributions, item-examinee interactions, group sizes) are fundamentally different. LLM "examinees" have different ability distributions (bimodal rather than normal), much larger sample sizes (thousands vs. hundreds), and qualitatively different error patterns. The paper should report C% at thresholds 1.0, 1.5, 2.0, and 2.5 to demonstrate that the qualitative finding (>20% instability) is robust. Without this, the headline number is not credible as more than an artifact of threshold choice.

- **W3 (Major). The rho = 0.307 correlation with accuracy improvement fundamentally undermines the "instability" framing without adequate decomposition.** If items that exhibit DIF are precisely those where models improved most, this is not "instability" in any pathological sense -- it is the benchmark doing its job (measuring real capability differences). The paper acknowledges this but does not attempt even a partial decomposition. A regression analysis partitioning C% into accuracy-explained and residual components, or a partial correlation removing accuracy improvement, would substantially clarify what the 38% actually means. As stated, a skeptical reader can dismiss the entire finding as: "Models improved differentially across domains, so items in those domains show DIF. This is expected and unremarkable."

- **W4 (Major). Missing related work in psychometric methodology.** For a paper claiming to bridge psychometrics and ML evaluation, the psychometric literature coverage has significant gaps:
  - **Measurement invariance framework** (Meredith 1993; Vandenberg & Lance 2000) -- DIF is a special case of scalar invariance testing. The paper never mentions this broader framework, which would provide theoretical grounding for the temporal comparability claim.
  - **MIMIC models** (Muthen 1985; Woods 2009) -- these handle continuous covariates and directly address the theta-conditioning limitations the paper documents (plan_012).
  - **IRT-based DIF methods** (Lord's chi-squared, Raju's area measure) -- no justification is provided for choosing MH over these alternatives, which operate directly in the IRT parameter space.
  - **Non-uniform DIF detection** (logistic regression DIF, SIBTEST) -- the MH procedure detects only uniform DIF (constant difficulty shift). Non-uniform DIF, where contamination effects vary by ability level, is highly plausible for LLMs (stronger models more likely to have memorized specific items) and would be entirely missed.
  - **Propensity score matching for DIF** (Teresi et al. 2007) -- directly addresses the impact-vs-DIF confounding that is the paper's central challenge.

- **W5 (Moderate). The paper tries to do too much.** Four core claims, architecture stratification, structural constraints, item-focused trees, RL robustness, cross-benchmark validation (GSM8K + GSM1K), complementary baselines (ConStat, DVD), negative ensemble result, Bayesian DIF simulation, bifactor IRT equating pilot, and LLM item generation pilot -- all in a 9-page paper. Each receives insufficient depth. The pilot studies (Section 7) deliver below-target results (CFI = 0.87, equated rho = 0.93 < 0.95 target, difficulty rho = 0.64) and are acknowledged as not production-ready, raising the question of why they are included. The Bayesian DIF section is entirely simulated with no real-data validation. The ensemble section is a negative result. These dilute rather than strengthen the paper. A focused paper with Claims 1-3 plus architecture stratification, with Claims 4 and all pilot studies removed, would be tighter and more convincing.

- **W6 (Moderate). Multiple testing is not addressed.** 12,508 simultaneous MH tests are conducted with no Bonferroni correction, FDR control, or discussion of why the ETS classification's joint effect-size + significance requirement suffices. The random-split sanity check (C% = 0.18%) provides indirect evidence that the procedure is not wildly anti-conservative, but this argument is never made explicit. Given that 31.3% of items are flagged, even a small inflation in per-item Type I error could substantially change the headline number.

- **W7 (Moderate). Semi-synthetic injection uses a simplified contamination model.** Flipping incorrect-to-correct at rate p assumes contamination manifests as deterministic answer knowledge. Real contamination may involve partial knowledge (increased probability but not certainty), distractor elimination (narrowing from 4 to 2 choices), format/style memorization without content memorization, or differential effects by item difficulty. The DELTA-TPR numbers may overestimate detection power against realistic contamination patterns. A sensitivity analysis with probabilistic contamination (e.g., shifting P(correct) by a fixed amount rather than setting it to 1) would strengthen the framework substantially.

- **W8 (Moderate). The tension between "38% instability" and "rho = 0.997 redundancy" is not fully resolved.** The paper frames this as "measurement efficiency, not validity crisis," but this framing cuts against the alarm implied by the 38% headline. If removing 38% of items barely changes rankings, then the instability is practically irrelevant for the primary use case (model ranking). The paper argues DIF items carry discriminative signal (z = -8 to -49 sigma), but this is comparing DIF removal to random removal -- it does not establish that the instability matters for any practical decision. The paper needs to choose: either the instability is a serious concern (in which case rho = 0.997 undermines that claim) or it is a measurement efficiency observation (in which case the 38% alarm is misleading framing).

- **W9 (Minor). RL robustness (N=13) is severely underpowered.** The paper appropriately qualifies this as "preliminary," but the Discussion section (in the best-case paper) overclaims: "DIF's group-level architecture is fundamentally orthogonal to the NLL-gap-contraction mechanism that defeats per-model detectors" is a theoretical assertion not supported by N=13 empirical evidence. The comparison with per-model detectors is also apples-to-oranges: DIF operates at the group level and would be inherently less sensitive to adding 13 models to a cohort of thousands.

- **W10 (Minor). Inconsistent numbers across paper versions.** The "best" and "median" paper versions report different numbers for the same experiments (e.g., architecture-stratified C%: 22.1% vs. 28.2%; decoder-only N: 3,847 vs. 3,412; RMSEA improvements differ). While this reflects different writing strategies, it raises concerns about which numbers are authoritative.

- **W11 (Minor). GSM1K validation is suggestive but imprecise.** N = 33 matched models yields wide confidence intervals (approximately [-0.70, -0.17] at 95%). The anti-correlation is directionally convincing and survives leave-one-out analysis, but the paper should be more explicit about the precision limitations rather than presenting r = -0.478 as a precise estimate.

- **W12 (Minor). Several citations use placeholder formatting.** References like "[ConStat Authors] (2024)" and "[DVD Authors] (2024)" suggest incomplete citation preparation. Some references in the literature map (Hardy 2026, Polo 2026 Growing Pains) are unverified.

**Questions for Authors:**

1. What is C% at ETS thresholds |DELTA_MH| >= 1.0, 1.5, 2.0, and 2.5? Does the qualitative finding (>20% instability) survive at 2.0? At 2.5?

2. If you regress per-subject C% on per-subject accuracy improvement, what fraction of variance is explained? What is the residual C% after removing accuracy-explained instability? This would directly address whether the 38% is "models got better" or something more.

3. Why was MH-DIF chosen over logistic regression DIF, which naturally handles continuous covariates (avoiding the theta-conditioning failure documented in plan_012), detects non-uniform DIF (plausible for LLMs), and has been standard in psychometrics since Swaminathan & Rogers (1990)? At minimum, a comparison on a subset of items would strengthen the methodological contribution.

4. The DELTA-FPR = 0.000 for cross-subject matching -- is this exactly zero across all injection levels, all subjects, and all random seeds? Or rounded to three decimal places? The exact number matters for assessing whether this is a methodological guarantee or an empirical observation at the tested configurations.

5. How does restricting to models above a minimum accuracy threshold (e.g., removing near-random models below 30% accuracy) affect C%? Very weak models may inflate DIF statistics by creating spurious ability-response interactions.

6. The paper claims DIF "complements" Growing Pains' anchor-item approach. Has C% been computed specifically among Growing Pains' anchor items? If their anchors show high DIF, that is a concrete, immediately actionable finding. If not, the complementarity claim is speculative.

7. For the Cumulative Bayesian DIF (Section 5.3 / 6.3 in the median paper): what are the assumed priors? How sensitive are TPR/FPR to the Bayes factor threshold (2.0 vs. 3.2 vs. 5.0)? Without these details, the simulation results cannot be evaluated.

8. The within-family Llama-2 vs. Llama-3 analysis yields C% = 61.3%. Given the massive capability difference between these model families, how much of this is genuine DIF vs. impact (overall ability difference)? This seems like a clear case of impact masquerading as DIF, which the paper should address.

**Missing Related Work:**

- **Measurement invariance framework**: Meredith (1993), "Measurement invariance, factor analysis and factorial invariance" -- DIF is a special case of scalar measurement invariance. Vandenberg & Lance (2000) review. This theoretical framing is essential for the temporal comparability argument.

- **MIMIC models for DIF**: Muthen (1985), Woods (2009) -- directly relevant as they handle continuous covariates and avoid the limitations of categorical MH-DIF that the paper documents.

- **Non-uniform DIF methods**: Swaminathan & Rogers (1990) logistic regression DIF; Shealy & Stout (1993) SIBTEST. The paper cites SIBTEST in the writing plan but not in the manuscript. Non-uniform DIF is highly plausible for LLM populations.

- **Propensity score matching for DIF**: Teresi et al. (2007) -- directly addresses the impact-vs-DIF confounding problem.

- **IRT-based DIF**: Lord (1980) chi-squared test; Raju (1988, 1990) area measures. No justification for MH over these methods is provided.

- **Concurrent IRT work on LLMs**: Polo et al. (AAAI 2026) PSN-IRT -- cited in the literature map but absent or minimally discussed in the paper. This is the closest concurrent work applying IRT to MMLU at scale.

- **Wang et al. (ICLR 2026)** on RL contamination fragility -- cited in the literature map as "foundation" but apparently absent from the manuscript. This paper directly motivates why behavioral (not NLL-based) detection methods are needed.

- **Tao et al. (ICLR 2026)** Self-Critique/RL-MIA -- directly relevant to the RL robustness discussion.

- **Lalor et al. (2019)** and **Vania et al. (2021)** on IRT for NLP -- listed in the writing plan as must-cite but not clearly present in the manuscript.

- **Dynamic evaluation and adaptive testing for LLMs**: Zhu et al. (2023) "PromptBench"; Ye et al. (2024) on dynamic benchmarking. The paper discusses LiveBench but misses the broader dynamic evaluation literature.

**Preliminary Score:** 3/6 (Weak Reject). The paper addresses an important problem with commendable experimental thoroughness and intellectual honesty, but the core method is entirely off-the-shelf with no calibration for the LLM domain, the headline finding (38%) rests on an uncalibrated threshold with no sensitivity analysis, the central narrative is partially undermined by the capability-improvement correlation, the psychometric related work has significant gaps for a paper positioned at the intersection of psychometrics and ML, and the paper overextends by trying to include too many preliminary results. The ground truth meta-critique and cross-subject matching innovation are genuine contributions that could anchor a stronger, more focused paper.

**Confidence:** 4/5. I am familiar with both the DIF/psychometric methodology and the LLM benchmark evaluation literature. The main source of uncertainty is whether the threshold sensitivity analysis (W2) would substantially change the qualitative findings -- it might not, in which case the paper's position improves.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45589644-02f5-4baa-bd3a-53baa01ddf79",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEuAQAsGbgtjU6yRwTuF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44b885d9-1586-4c7a-839f-97324b5a33e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UY1DS2GY2JRnvPo35fyKL6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 74623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 770,
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

_source line 51 · 2026-05-21T02:12:16.890Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01GPym5hvRrXhrtUurHUB8Re`</summary>

```json
{
  "report": "# R2 Review: Novelty and Related Work\n\n**Paper**: \"Psychometric Characterization of Item-Level Instability in LLM Benchmarks via Differential Item Functioning\"\n**Reviewer Focus**: Novelty and Related Work\n**Venue Standard**: Top ML venue, ~25% acceptance rate, 6-point scale\n\n---\n\n## Summary\n\nThe paper applies Differential Item Functioning (DIF) -- a classical psychometric method using the Mantel-Haenszel procedure with ETS effect-size classification -- to the METABENCH response matrix (5,227 models x 12,508 MMLU items) to characterize item-level behavioral drift across model generations. It reports that 38% of MMLU items are functionally unstable across temporal cohorts, identifies a methodological gap in how contamination detection is validated (web-overlap labels measure global exposure, not differential functioning), proposes a semi-synthetic validation framework with cross-subject matching, and reframes instability as measurement efficiency rather than validity crisis. Robustness analyses (architecture stratification, item-focused trees, RL sensitivity), complementary baselines (ConStat, DVD), and pilot studies (bifactor IRT equating, LLM item generation) are included.\n\n---\n\n## Strengths\n\n- **S1. Scale and systematic execution.** 5,227 models x 12,508 items is genuinely unprecedented for psychometric analysis of LLM benchmarks. The experiment chain is methodical -- 11 experiments with clear dependency structure, pre-mortem analyses (plan_014 killing plan_015 before wasting compute), and honest reporting of negative results. This is above the venue average for experimental rigor.\n\n- **S2. Ground truth meta-critique (Claim 2) is the paper's strongest intellectual contribution.** The observation that web-overlap labels measure a static, model-agnostic property (public accessibility) while DIF measures a dynamic, group-specific property (differential functioning) is genuinely important. The enrichment~1.0 result is reinterpreted convincingly: since virtually all MMLU items have been on Common Crawl since 2020, near-uniform global exposure makes web-overlap labels uninformative for item-level differential detection. This critique applies broadly to Min-K%, n-gram methods, and all work using web-overlap as item-level ground truth. The implication -- that the field's standard validation methodology has a systematic blind spot -- is well-argued and, if correct, consequential.\n\n- **S3. Cross-subject matching innovation (Claim 3).** The insight that using total score on the *same* subject as the MH matching variable contaminates the conditioning variable when injection targets that subject is subtle and practically important. The solution -- matching on scores from *other* subjects -- is elegant, and the empirical demonstration is clean: DELTA-FPR = 0.000 across all 5 tested subjects vs. +0.186 inflation for within-subject matching. This is a genuinely reusable methodological contribution.\n\n- **S4. Architecture stratification transforms a potential objection into evidence.** The reduction from C% = 31.3% to 22.1%/28.2% when restricting to decoder-only models, with dramatically improved IRT fit (RMSEA 0.082 to 0.037), is the most methodologically satisfying experiment. It demonstrates that the method is refinable and that a non-trivial fraction of flags were architecture-confounded, while confirming that substantial genuine instability persists.\n\n- **S5. Honest treatment of the rho=0.307 confound and negative results.** The paper does not claim to have separated contamination from capability improvement. Three independent attempts to reduce baseline DIF (matched-ability, theta-conditioning, bifactor pre-check) all failed, and this is reported transparently. The conclusion that temporal DIF reflects genuine capability improvement rather than contamination is more honest than many papers would be.\n\n- **S6. DIF-as-diagnostic-lens reframing (Claim 4) is supported by two independent evidence lines.** The z = -8 to -49 sigma result for DIF vs. random removal and the GSM1K anti-correlation (r = -0.478, p = 0.005) are mutually reinforcing. The reframing from \"find bad items and remove\" to \"understand what changed and why\" is conceptually productive, though the GSM1K evidence is preliminary (N=33).\n\n---\n\n## Weaknesses\n\n### Critical\n\n- **W1 (Major). Limited methodological novelty -- the core technique is entirely off-the-shelf.** The Mantel-Haenszel procedure is a 1959 technique. The ETS A/B/C classification dates to the 1980s. The paper applies these without modification to a binary response matrix. The semi-synthetic injection framework is a useful contribution, but the idea of injecting known signal and measuring detection power is standard in statistics (simulation-based calibration). Cross-subject matching is a sensible but straightforward idea once the matching-variable contamination problem is recognized. For a top ML venue, the algorithmic contribution is thin. The paper's value rests entirely on empirical findings and the meta-critique -- which is legitimate but places a high bar on those findings being definitive.\n\n- **W2 (Major). The ETS C threshold (|DELTA_MH| >= 1.5) is borrowed from human educational testing without calibration for LLM populations, and no sensitivity analysis is provided.** The 38% headline number is anchored to this arbitrary cutoff designed for human test-takers, where the population characteristics (ability distributions, item-examinee interactions, group sizes) are fundamentally different. LLM \"examinees\" have different ability distributions (bimodal rather than normal), much larger sample sizes (thousands vs. hundreds), and qualitatively different error patterns. The paper should report C% at thresholds 1.0, 1.5, 2.0, and 2.5 to demonstrate that the qualitative finding (>20% instability) is robust. Without this, the headline number is not credible as more than an artifact of threshold choice.\n\n- **W3 (Major). The rho = 0.307 correlation with accuracy improvement fundamentally undermines the \"instability\" framing without adequate decomposition.** If items that exhibit DIF are precisely those where models improved most, this is not \"instability\" in any pathological sense -- it is the benchmark doing its job (measuring real capability differences). The paper acknowledges this but does not attempt even a partial decomposition. A regression analysis partitioning C% into accuracy-explained and residual components, or a partial correlation removing accuracy improvement, would substantially clarify what the 38% actually means. As stated, a skeptical reader can dismiss the entire finding as: \"Models improved differentially across domains, so items in those domains show DIF. This is expected and unremarkable.\"\n\n- **W4 (Major). Missing related work in psychometric methodology.** For a paper claiming to bridge psychometrics and ML evaluation, the psychometric literature coverage has significant gaps:\n  - **Measurement invariance framework** (Meredith 1993; Vandenberg & Lance 2000) -- DIF is a special case of scalar invariance testing. The paper never mentions this broader framework, which would provide theoretical grounding for the temporal comparability claim.\n  - **MIMIC models** (Muthen 1985; Woods 2009) -- these handle continuous covariates and directly address the theta-conditioning limitations the paper documents.\n  - **IRT-based DIF methods** (Lord's chi-squared, Raju's area measure) -- no justification is provided for choosing MH over these alternatives, which operate directly in the IRT parameter space.\n  - **Non-uniform DIF detection** (logistic regression DIF via Swaminathan & Rogers 1990, SIBTEST via Shealy & Stout 1993) -- the MH procedure detects only uniform DIF (constant difficulty shift). Non-uniform DIF, where contamination effects vary by ability level, is highly plausible for LLMs (stronger models more likely to have memorized specific items) and would be entirely missed.\n  - **Propensity score matching for DIF** (Teresi et al. 2007) -- directly addresses the impact-vs-DIF confounding that is the paper's central challenge.\n\n### Major\n\n- **W5 (Moderate). The paper tries to do too much.** Four core claims, architecture stratification, structural constraints, item-focused trees, RL robustness, cross-benchmark validation (GSM8K + GSM1K), complementary baselines (ConStat, DVD), negative ensemble result, Bayesian DIF simulation, bifactor IRT equating pilot, and LLM item generation pilot -- all in a 9-page paper. Each receives insufficient depth. The pilot studies (Section 7) deliver below-target results (CFI = 0.87, equated rho = 0.93 < 0.95 target, difficulty rho = 0.64) and are acknowledged as not production-ready, raising the question of why they are included. The Bayesian DIF section is entirely simulated with no real-data validation. The ensemble section is a negative result. These dilute rather than strengthen the paper.\n\n- **W6 (Moderate). Multiple testing is not addressed.** 12,508 simultaneous MH tests are conducted with no Bonferroni correction, FDR control, or discussion of why the ETS classification's joint effect-size + significance requirement suffices. The random-split sanity check (C% = 0.18%) provides indirect evidence that the procedure is not wildly anti-conservative, but this argument is never made explicit.\n\n- **W7 (Moderate). Semi-synthetic injection uses a simplified contamination model.** Flipping incorrect-to-correct at rate p assumes contamination manifests as deterministic answer knowledge. Real contamination may involve partial knowledge, distractor elimination, format/style memorization, or differential effects by item difficulty. The DELTA-TPR numbers may overestimate detection power against realistic contamination patterns.\n\n- **W8 (Moderate). The tension between \"38% instability\" and \"rho = 0.997 redundancy\" is not fully resolved.** The paper frames this as \"measurement efficiency, not validity crisis,\" but this framing cuts against the alarm implied by the 38% headline. If removing 38% of items barely changes rankings, then the instability is practically irrelevant for the primary use case (model ranking). The paper needs to choose: either the instability is a serious concern (in which case rho = 0.997 undermines that claim) or it is a measurement efficiency observation (in which case the 38% alarm is misleading framing).\n\n### Minor\n\n- **W9 (Minor). RL robustness (N=13) is severely underpowered.** The paper appropriately qualifies this as \"preliminary,\" but the Discussion section overclaims: \"DIF's group-level architecture is fundamentally orthogonal to the NLL-gap-contraction mechanism\" is a theoretical assertion not supported by N=13. The comparison with per-model detectors is also apples-to-oranges.\n\n- **W10 (Minor). GSM1K validation is suggestive but imprecise.** N = 33 matched models yields wide confidence intervals (~[-0.70, -0.17] at 95%). The anti-correlation is directionally convincing but the paper should be more explicit about precision limitations.\n\n- **W11 (Minor). Several citations use placeholder formatting.** References like \"[ConStat Authors] (2024)\" and \"[DVD Authors] (2024)\" suggest incomplete citation preparation.\n\n---\n\n## Questions for Authors\n\n1. What is C% at ETS thresholds |DELTA_MH| >= 1.0, 1.5, 2.0, and 2.5? Does the qualitative finding (>20% instability) survive at 2.0? At 2.5?\n\n2. If you regress per-subject C% on per-subject accuracy improvement, what fraction of variance is explained? What is the residual C% after removing accuracy-explained instability?\n\n3. Why was MH-DIF chosen over logistic regression DIF, which naturally handles continuous covariates (avoiding the theta-conditioning failure), detects non-uniform DIF, and has been standard since Swaminathan & Rogers (1990)? At minimum, a comparison on a subset of items would strengthen the methodological contribution.\n\n4. The DELTA-FPR = 0.000 for cross-subject matching -- is this exactly zero across all injection levels, all subjects, and all random seeds? Or rounded to three decimal places?\n\n5. How does restricting to models above a minimum accuracy threshold (e.g., removing near-random models below 30% accuracy) affect C%?\n\n6. Has C% been computed specifically among Growing Pains' anchor items? If their anchors show high DIF, that is a concrete, immediately actionable finding.\n\n7. For Cumulative Bayesian DIF: what are the assumed priors? How sensitive are TPR/FPR to the Bayes factor threshold?\n\n8. The within-family Llama-2 vs. Llama-3 analysis yields C% = 61.3%. Given the massive capability difference, how much of this is genuine DIF vs. impact (overall ability difference)?\n\n---\n\n## Missing Related Work\n\n- **Measurement invariance framework**: Meredith (1993), Vandenberg & Lance (2000) -- DIF is a special case of scalar measurement invariance. Essential theoretical grounding for the temporal comparability argument.\n\n- **MIMIC models for DIF**: Muthen (1985), Woods (2009) -- handle continuous covariates, directly relevant to theta-conditioning limitations documented in plan_012.\n\n- **Non-uniform DIF methods**: Swaminathan & Rogers (1990) logistic regression DIF; Shealy & Stout (1993) SIBTEST -- cited in writing plan but absent from manuscript.\n\n- **Propensity score matching for DIF**: Teresi et al. (2007) -- addresses the impact-vs-DIF confounding problem.\n\n- **IRT-based DIF**: Lord (1980) chi-squared test; Raju (1988, 1990) area measures.\n\n- **Concurrent IRT work on LLMs**: Polo et al. (AAAI 2026) PSN-IRT -- in the literature map as method-component but minimally discussed in manuscript.\n\n- **Wang et al. (ICLR 2026)** on RL contamination fragility -- in literature map as \"foundation\" but absent from manuscript.\n\n- **Tao et al. (ICLR 2026)** Self-Critique/RL-MIA -- relevant to RL robustness discussion.\n\n- **Lalor et al. (2019)** and **Vania et al. (2021)** on IRT for NLP -- in writing plan as must-cite but absent from manuscript.\n\n- **Dynamic evaluation literature**: Zhu et al. (2023) PromptBench; Ye et al. (2024) on dynamic benchmarking.\n\n---\n\n## Preliminary Score: 3/6 (Weak Reject)\n\nThe paper addresses an important problem with commendable experimental thoroughness and intellectual honesty, but the core method is entirely off-the-shelf with no calibration for the LLM domain, the headline finding rests on an uncalibrated threshold with no sensitivity analysis, the central narrative is partially undermined by the capability-improvement correlation, the psychometric related work has significant gaps for a paper positioned at the psychometrics-ML intersection, and the paper overextends with too many preliminary results. The ground truth meta-critique and cross-subject matching innovation are genuine contributions that could anchor a stronger, more focused paper.\n\n**Confidence:** 4/5. Familiar with both DIF/psychometric methodology and LLM benchmark evaluation literature. Main uncertainty: whether threshold sensitivity analysis (W2) would substantially change qualitative findings.",
  "project": "irt_equated_bench_regen",
  "tier": "median",
  "dream_id": "dream_20260521T012912",
  "overall_score": "weak reject",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44b885d9-1586-4c7a-839f-97324b5a33e8",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEuAQAsGbgtjU6yRwTuF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8023910-5a4c-421a-8f9f-59747745722d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UY1DS2GY2JRnvPo35fyKL6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 74623,
      "output_tokens": 8178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 770
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8178,
          "cache_read_input_tokens": 74623,
          "cache_creation_input_tokens": 770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 770,
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

_source line 52 · 2026-05-21T02:12:20.556Z_

<details><summary>↩ Tool result · `toolu_01GPym5hvRrXhrtUurHUB8Re`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/review_report.md\", \"dream_id\": \"dream_20260521T012912\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8023910-5a4c-421a-8f9f-59747745722d",
  "isSidechain": true,
  "promptId": "0caf556e-6a0c-4e2d-b8fa-08b25e7eb298",
  "agentId": "a43ea8d08ff36c575",
  "type": "user",
  "uuid": "4bfdbe57-5606-4c80-a705-7b60112e24ca",
  "sourceToolAssistantUUID": "a8023910-5a4c-421a-8f9f-59747745722d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-21T02:12:31.691Z_

Review submitted. Here is the summary:

**Score: 3/6 (Weak Reject), Confidence 4/5.**

The review identifies 4 critical/major and 4 moderate weaknesses against 6 strengths.

**Top strengths**: Ground truth meta-critique (web-overlap labels vs. differential functioning), cross-subject matching innovation (DELTA-FPR=0.000), architecture stratification analysis, unprecedented scale, and honest negative result reporting.

**Top weaknesses**: (1) No methodological novelty -- MH-DIF is a 1959 technique applied without modification; (2) the 38% headline rests on an ETS threshold calibrated for human populations with no sensitivity analysis; (3) rho=0.307 with accuracy improvement undermines the "instability" framing without decomposition; (4) significant gaps in psychometric related work (measurement invariance, MIMIC models, non-uniform DIF, IRT-based DIF alternatives, propensity score matching); (5) the paper overextends with too many preliminary results in 9 pages.

**Key recommendation**: A focused paper with Claims 1-3 plus architecture stratification, adding threshold sensitivity analysis and instability decomposition, with expanded psychometric related work, would be substantially stronger. The ground truth meta-critique and semi-synthetic framework are the most defensible contributions.

The review report is saved at `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/median/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bfdbe57-5606-4c80-a705-7b60112e24ca",
  "isSidechain": true,
  "agentId": "a43ea8d08ff36c575",
  "requestId": "req_011CbEuPgZiRHfLQK6fevzmg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3739585-48e8-4018-947f-79d7dceefb58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "80d446f8-6835-4587-bd13-fde4c02ffb42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011L7TtjTGbq3L613H91vta4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8312,
      "cache_read_input_tokens": 75393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8312,
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
