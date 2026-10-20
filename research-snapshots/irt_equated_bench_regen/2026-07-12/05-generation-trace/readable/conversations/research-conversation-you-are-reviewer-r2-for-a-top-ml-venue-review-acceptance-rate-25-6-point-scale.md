# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a1db4df44a4eb5957.jsonl`
- **Structured JSON:** [`0bebbe26c5d8d91a4a13.json`](../../sessions/0b/0bebbe26c5d8d91a4a13.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-20T21:28:20.668Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus is **novelty and related work**.

## Paper Summary
Title: "Benchmark Contamination Is a Psychometric Problem: DIF-Based Detection, Multi-Signal Ensemble, and IRT-Equated Benchmark Regeneration"

The paper reframes LLM benchmark contamination as a psychometric problem. Three contributions:
1. **RL-Robust Detection**: DIF-based ETS C detection achieves TPR 0.72–0.85 / FPR <0.05 at δ≥1.4, maintaining AUROC=0.91 on RL-trained models where ConStat/Min-K% degrade to ≤0.53.
2. **Full-Spectrum Ensemble**: DIF + ConStat + DVD achieves 82% contamination coverage (up from 58% DIF-only).
3. **Psychometric Regeneration**: Bifactor IRT equating enables benchmark regeneration preserving rank-order stability (ρ=0.975).

## Paper Structure (10 pages, 18 tables, no figures)
- Section 1: Introduction — frames contamination as psychometric problem, DIF is orthogonal to RL smoothing
- Section 2: Related Work — contamination detection, IRT for LLM eval, benchmark maintenance, DIF in psychometrics. Cited works: Li et al. (contamination labels), Wang et al. ICLR 2026 (RL degrades detectors), ConStat (Binkyte et al. 2024), LiveBench (White et al. 2024), Growing Pains (arXiv 2026), Polo et al. (IRT for benchmarks), DynaBoard/Dynabench, Sinharay et al. 2006 (cumulative Bayesian DIF), Tutz & Berger 2016 (Item-Focused Trees), student simulation (arXiv 2601.09953)
- Section 3: Method — 3.1 Problem formulation (2PL IRT), 3.2 DIF via ETS classification (MH procedure), 3.3 Multi-signal ensemble (ConStat + DVD + weighted fusion), 3.4 Bifactor IRT equating
- Section 4: DIF Detection at Scale — 4.1 Real-data DIF on METABENCH MMLU (5,219 models × 12,508 items), 4.2 RL Robustness (Table 3: DIF AUROC 0.91 vs ConStat 0.53/Min-K% 0.51 on RL models), 4.3 Architecture-Stratified DIF, 4.4 Item-Focused Trees
- Section 5: Multi-Signal Ensemble — ConStat perturbation testing, DVD generation variance, ensemble fusion achieving 82% coverage
- Section 6: Validation — GSM8K cross-validation (r=0.58 with GSM1K gap), semi-synthetic injection, cumulative Bayesian DIF
- Section 7: Regeneration — Bifactor IRT equating (ρ=0.975), student simulation calibration (ρ=0.79), graceful degradation (critical threshold ~35%)
- Section 8: Conclusion + Limitations

## Your Review Task
Produce a structured review focusing on:

1. **Novelty Assessment** (detailed)
   - The core idea is applying DIF (a 60+ year old psychometric tool) to LLM contamination. Is this a genuine conceptual contribution or "well-known method → new domain" transfer?
   - The RL robustness argument (group-level ICC vs individual output distribution) — is this insight genuinely new, or would any psychometrician have predicted it?
   - The ensemble (DIF + ConStat + DVD) — how novel is the combination vs. simply running three existing detectors?
   - Bifactor IRT equating for benchmark regeneration — is this a new idea or standard psychometric practice applied to a new setting?
   - The "full loop" (detection → ensemble → generation → equating → graceful degradation) — does integration itself constitute novelty?
   
2. **Related Work Completeness** (detailed)
   - Are there missing citations? Consider:
     * Other IRT applications to LLM evaluation (e.g., Elo rating systems, TrueSkill adaptations)
     * Other contamination detection methods not cited (e.g., n-gram overlap, embedding similarity, training data extraction)
     * DIF literature: is the connection to measurement invariance / fairness testing discussed?
     * Benchmark refresh/rotation strategies beyond LiveBench
     * Test security literature from educational testing (item exposure control, adaptive testing)
   - Is the positioning fair to prior work? Does the paper strawman any baselines?
   - Is the Wang et al. (ICLR 2026) claim about RL degrading detectors taken at face value without independent verification?
   
3. **Framing and Claims** (critical)
   - "the one contamination signal RL cannot conceal" — is this overclaimed? Under what conditions could DIF fail?
   - "provably orthogonal" — is there an actual proof, or is this an informal argument?
   - "largest DIF analysis in LLM evaluation to date" — is this meaningful or just scaling an existing method?
   - Are the three contributions genuinely distinct, or is this one contribution (apply DIF) with two extensions?
   
4. **Significance and Impact**
   - Would this paper change how the community does benchmark evaluation?
   - Is there a clear path to adoption? Who would implement this?
   - Does the work open new research directions?

5. **Scores**:
   - Novelty (1-4)
   - Significance (1-4)
   - Overall Score (1-6)
   - Confidence (1-5)

Format your review as a structured markdown document. Be thorough and specific. Do NOT be generous — apply the standards of a top ML venue with ~25% acceptance rate. A paper that competently applies known tools to a new domain without genuine methodological innovation should be scored accordingly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "5a36b6c3-5062-4457-b738-8d1fa2074f78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T21:28:20.671Z_

```json
{
  "parentUuid": "5a36b6c3-5062-4457-b738-8d1fa2074f78",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
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
  "uuid": "6ff8449e-b467-4d95-8a99-2712b6472d4a",
  "timestamp": "2026-05-20T21:28:20.671Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T21:28:26.108Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ff8449e-b467-4d95-8a99-2712b6472d4a",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXjbdYp9RMM8RdZCjkB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38d8ba23-8fb6-4a6a-99f9-288034fd9a8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uiZXEL4HshSXW2ByoQNJL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7447,
      "cache_read_input_tokens": 8254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7447,
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

_source line 4 · 2026-05-20T21:28:26.607Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015WTiwuHbL9riN5eLdbVQMB`</summary>

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
  "parentUuid": "38d8ba23-8fb6-4a6a-99f9-288034fd9a8e",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXjbdYp9RMM8RdZCjkB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53fe554f-e680-4bc6-8c92-802269b7fd55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uiZXEL4HshSXW2ByoQNJL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7447,
      "cache_read_input_tokens": 8254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7447,
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

_source line 5 · 2026-05-20T21:28:26.610Z_

<details><summary>↩ Tool result · `toolu_015WTiwuHbL9riN5eLdbVQMB`</summary>

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
  "parentUuid": "53fe554f-e680-4bc6-8c92-802269b7fd55",
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "485544dc-6cbc-48b1-8f79-97e051080dc6",
  "sourceToolAssistantUUID": "53fe554f-e680-4bc6-8c92-802269b7fd55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T21:28:30.662Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01QUubnYeBMe7vHd3ECPnFfa`</summary>

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
  "parentUuid": "485544dc-6cbc-48b1-8f79-97e051080dc6",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXk4Aymm4UyDhYGKvcg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39667c8a-1bd9-4766-9e40-0b97497dc30e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yeHNVzfS5Wf1eLczdhoJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 7 · 2026-05-20T21:28:30.699Z_

<details><summary>↩ Tool result · `toolu_01QUubnYeBMe7vHd3ECPnFfa`</summary>

```text
{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (3 个)\n\n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_001_real_data_dif_mmlu** (negative): MH-DIF 在 METABENCH 真实 MMLU 数据（5227 模型 × 12508 items）上，用时间 cohort (2023 vs 2024) 和能力分位 cohort 分组时，ETS C 标记的 items 在 Li et al. clean items 中的 FPR ≤ 0.05，且 ETS C 标记在 contaminated items 中的比例显著高于 clean items。这验证 DIF 在真实数据上不会产生过多假阳性，且能捕捉到与 web-overlap 污染信号一致的差异性。 ← 基于 mvp_dif_power_sim_phase2\n  [plan_001_analysis_script](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/plan_001_analysis.py) | [plan_001_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md) | [dif_results_temporal](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_temporal.csv) | [dif_results_ability](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_ability.csv) | [dif_summary](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_summary.csv) | [within_family_dif](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/within_family_dif.csv) | [cross_analysis](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/cross_analysis.csv) | [domain_specificity](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/domain_specificity.csv) | [neg_disc_sensitivity](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/neg_disc_sensitivity.csv) | [plan_001_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report_00ca1f.md) | [plan_001_dif_results_temporal](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_temporal_69f998.csv) | [plan_001_dif_results_ability](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_ability_c17059.csv) | [plan_001_analysis_script](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/intermediate/plan_001_analysis.py)\n- **mvp_dif_power_sim_phase2** (success): ETS C 分类在 METABENCH 真实 MMLU 2PL IRT 参数（非理想化分布）下，仍能在 N≥80/group、δ≥1.4 时达到 TPR≥0.65、FPR≤0.10。Phase 1 用合成参数（a~LogNormal, b~N(0,1)）条件性通过，需验证真实参数分布（可能有偏态、聚集、极端值）不会降解检测功效。 ← 基于 mvp_dif_power_sim\n- **mvp_dif_power_sim** (success): DIF 跨模型批次分析（MH + Logistic Regression）在 N=50-80/group、污染效应量 δ≥1.0 logits 时，对 10% 污染 items 的检测功效 TPR≥0.70 且 FPR≤0.10。这是整个 pipeline 的前提假设——若 DIF 在理想合成数据上都 underpowered，则后续真实数据方案不成立。\n  [Phase 1 DIF Power Results CSV](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_power_results.csv) | [Phase 1 DIF Power Curves](/api/workspace-files/projects/irt_equated_benc"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39667c8a-1bd9-4766-9e40-0b97497dc30e",
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "08b4459b-5751-405c-bbc3-39b66d37781e",
  "sourceToolAssistantUUID": "39667c8a-1bd9-4766-9e40-0b97497dc30e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T21:28:31.434Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TqMrRdxaQkgesim46Jtwr4`</summary>

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
  "parentUuid": "08b4459b-5751-405c-bbc3-39b66d37781e",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXk4Aymm4UyDhYGKvcg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "013fc9fe-f34b-4771-a120-8e7d2b1f7639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yeHNVzfS5Wf1eLczdhoJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 9 · 2026-05-20T21:28:31.448Z_

<details><summary>↩ Tool result · `toolu_01TqMrRdxaQkgesim46Jtwr4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **plan_001_real_data_dif_mmlu** (negative): MH-DIF 在 METABENCH 真实 MMLU 数据（5227 模型 × 12508 items）上，用时间 cohort (2023 vs 2024) 和能力分位 cohort 分组时，ETS C 标记的 items 在 Li et al. clean items 中的 FPR ≤ 0.05，且 ETS C 标记在 contaminated items 中的比例显著高于 clean items。这验证 DIF 在真实数据上不会产生过多假阳性，且能捕捉到与 web-overlap 污染信号一致的差异性。 ← 基于 mvp_dif_power_sim_phase2\\n  [plan_001_analysis_script](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/plan_001_analysis.py) | [plan_001_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md) | [dif_results_temporal](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_temporal.csv) | [dif_results_ability](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_ability.csv) | [dif_summary](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_summary.csv) | [within_family_dif](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/within_family_dif.csv) | [cross_analysis](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/cross_analysis.csv) | [domain_specificity](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/domain_specificity.csv) | [neg_disc_sensitivity](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/neg_disc_sensitivity.csv) | [plan_001_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report_00ca1f.md) | [plan_001_dif_results_temporal](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_temporal_69f998.csv) | [plan_001_dif_results_ability](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_ability_c17059.csv) | [plan_001_analysis_script](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/intermediate/plan_001_analysis.py)\\n- **mvp_dif_power_sim_phase2** (success): ETS C 分类在 METABENCH 真实 MMLU 2PL IRT 参数（非理想化分布）下，仍能在 N≥80/group、δ≥1.4 时达到 TPR≥0.65、FPR≤0.10。Phase 1 用合成参数（a~LogNormal, b~N(0,1)）条件性通过，需验证真实参数分布（可能有偏态、聚集、极端值）不会降解检测功效。 ← 基于 mvp_dif_power_sim\\n- **mvp_dif_power_sim** (success): DIF 跨模型批次分析（MH + Logistic Regression）在 N=50-80/group、污染效应量 δ≥1.0 logits 时，对 10% 污染 items 的检测功效 TPR≥0.70 且 FPR≤0.10。这是整个 pipeline 的前提假设——若 DIF 在理想合成数据上都 underpowered，则后续真实数据方案不成立。\\n  [Phase 1 DIF Power Results CSV](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_power_results.csv) | [Phase 1 DIF Power Curves](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/chart/dif_power_curves.pdf) | [DIF Diagnostic P-value Distribution](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/chart/dif_diagnostic_pvalue_dist.pdf) | [DIF Diagnostic TPR Comparison (Raw vs BH vs Bonferroni)](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_diagnostic_tpr_comparison.csv)\\n\\n## 趋势\\n成功 2 / 负向 1 / 失败 0 / 共 3\\nbest_auc_lr: 0.9405 ↓（近 2 次 success）\\nbest_auc_mh: 0.9254 ↓（近 2 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 3576, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "013fc9fe-f34b-4771-a120-8e7d2b1f7639",
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "5223cf80-d8ec-4c37-89a7-8830d9a0c53e",
  "sourceToolAssistantUUID": "013fc9fe-f34b-4771-a120-8e7d2b1f7639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T21:28:35.341Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EGMUMHba4vwvEa19PUUya5`</summary>

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
  "parentUuid": "5223cf80-d8ec-4c37-89a7-8830d9a0c53e",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXkQW6qkRzU5yUH23uk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fb19a1e-693a-4051-9dd8-f87a56d46789",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fs39Ap6oQb6d1zLJFVZr9a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3631,
      "cache_read_input_tokens": 17148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3631,
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

_source line 11 · 2026-05-20T21:28:35.350Z_

<details><summary>↩ Tool result · `toolu_01EGMUMHba4vwvEa19PUUya5`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fb19a1e-693a-4051-9dd8-f87a56d46789",
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "eb2ceca4-eecd-405a-b835-14796e887d1d",
  "sourceToolAssistantUUID": "4fb19a1e-693a-4051-9dd8-f87a56d46789",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T21:28:35.824Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FCCxzDVZwNPWDrcvwXTTJQ`</summary>

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
  "parentUuid": "eb2ceca4-eecd-405a-b835-14796e887d1d",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXkQW6qkRzU5yUH23uk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "840332e2-34dc-4bf5-a0b7-04300d58f659",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fs39Ap6oQb6d1zLJFVZr9a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3631,
      "cache_read_input_tokens": 17148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3631,
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

_source line 13 · 2026-05-20T21:28:35.832Z_

<details><summary>↩ Tool result · `toolu_01FCCxzDVZwNPWDrcvwXTTJQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/memory.md\", \"content\": \"## MVP 验证关键经验 (2026-05-20)\\n\\n### D001 决策：ETS C 分类 > p-value 检验\\n- **p-value based DIF 检测在 200-item benchmark 上严重 underpowered**：BH 校正后 TPR 仅 0.04-0.07（N=50, δ=1.0）。即使 raw（不校正）TPR 也只有 0.36-0.39，远低于 0.70 目标\\n- **ETS C 分类（|Δ_MH|≥1.5 + 显著性）是可行的替代**：TPR=0.68-0.85 at N≥80, δ≥1.4。本质是 magnitude-based detection，绕过了多重检验问题\\n- **AUC 一直很好（0.91-0.96）**：说明 DIF 统计量的区分能力没问题，问题在假设检验的 threshold，不在信号本身\\n- **原因**：200 个 items 做 BH 校正，需要极小的 p-value 才能过。N=50-100 per group 对 MH/LR 的 per-item 统计功效不够产生 p<0.001 级别的 evidence\\n\\n### Phase 2 验证：真实参数稳健\\n- **PSN-IRT 真实 MMLU 参数** vs 合成参数差异显著：b_mean=-0.84（真实）vs 0.0（合成），即真实 MMLU items 偏容易\\n- 尽管参数分布差异大，ETS C TPR 在真实参数下反而更高（N=100, δ=1.6: 0.80 vs Phase 1 的 0.85）——差异不大，结论稳健\\n- **Phase 2 用了 PSN-IRT 而非 METABENCH**：PSN-IRT 的 item_parameters.csv 可直接使用（14042 items），无需下载 620MB 大包\\n\\n### 关键操作参数\\n- N≥80/group 是最低要求，N≥100 显著改善功效\\n- δ≥1.4 logits 是可靠检测区间，δ=1.0 在边界\\n- MH 5 层 quantile-based 分层 + ETS C 阈值是当前最佳组合\\n- LR 方法与 MH 表现相当，无显著优势\\n\\n## plan_001 关键教训 (2026-05-20) ⚠️\\n\\n### D003: 朴素 MH-DIF 无法区分污染与能力提升\\n- **Temporal cohort (2023 vs 2024)**: 31.3% ETS C，enrichment=0.96（clean 和 contaminated 被标记概率相同）\\n- **根因**：2024 模型整体比 2023 强，MH-DIF 捕获的是系统性能力差异，不是 item-level 污染信号\\n- **证据链**：\\n  - Within-family (Llama-2 vs Llama-3): 61.3% C — 代际能力差距 >> temporal cohort\\n  - Domain ρ(C_rate, Δacc)=0.307, p=0.02 — 准确率提升越大的 subject DIF 越高\\n  - 两种 cohort 的 C 类 items Jaccard 仅 0.014 — 两种 DIF 检测的完全不同的东西\\n  - Sanity check: 随机半分 0.18% C — MH 方法本身没问题\\n- **Ability cohort (Q1-2 vs Q4-5)**: 2.9% C, enrichment=1.19, FPR=2.7% — 弱正向信号但 enrichment 不够强\\n- **结论**：MH-DIF 必须在能力匹配的组间比较才有意义。不能直接用时间分组。需要 IRT equating 或 matched-ability 设计来控制能力混淆\\n\\n### 下一步方向（待 Director 决策）\\n1. **Matched-ability DIF**: 在同 accuracy quintile 内做时间 cohort DIF（控制能力后隔离污染信号）\\n2. **IRT equating**: 从响应矩阵拟合 2PL IRT，用 IRT equating 消除能力差异后做 DIF\\n3. **DPO/RL-specific DIF**: 用 RL-trained (477) vs non-RL 分组，控制能力后检测 training method 相关的 DIF\\n\\n## Phase 2 数据源调研 (2026-05-20)\\n\\n### PSN-IRT (AAAI 2026)\\n- **论文全名**: \\\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\\\"\\n- **GitHub**: https://github.com/Joe-Hall-Lee/PSN-IRT\\n- MMLU 14,042 items, 仅 12 模型\\n\\n### METABENCH (Kipnis et al., ICLR 2025) ⭐ 推荐\\n- **论文全名**: \\\"metabench — A Sparse Benchmark of Reasoning and Knowledge in Large Language Models\\\"\\n- **GitHub**: https://github.com/adkipnis/metabench\\n- **Zenodo**: https://zenodo.org/records/12819251 (620MB)\\n- MMLU 12,508 items, 5,219 模型\\n\\n## METABENCH 数据探索关键发现 (2026-05-20)\\n\\n### ⚠️ D002: preproc.rds 的 diff/disc 是 CTT 统计量，不是 IRT 参数\\n- **diff** = 0.75 × p_correct（猜测校正正确率），概率尺度 [0, 0.75]，**不是** IRT 的 b 参数\\n- **disc** = 点双列相关系数（rpbis），[-1, 1]，**不是** IRT 的 a 参数\\n- **CTT → IRT 不可直接转换**，必须从响应矩阵重新用 `mirt` 拟合\\n- METABENCH 的实际 IRT 拟合在 `crossvalidate.R` 中用 `mirt::mirt()` slope-intercept 参数化 (a1, d)\\n- 源码证据：`analysis/preprocess.R` lines 52-77\\n\\n### Cohort & RL 模型\\n- 2 个年度 cohort ≥80: 2023 (N=1,253), 2024 (N=658)\\n- 477 RL-labeled models: DPO(346), ORPO(52), PPO(11), KTO(6)\\n- 63% 模型无法从名称分类\\n\\n### Li et al. (EMNLP 2024) Proxy Ground Truth\\n- 9,229/12,508 items 有标注（73.8% 覆盖）\\n- clean 60.5% / input_and_label 33.0% / input_only 6.5%\\n- Web overlap proxy，非训练数据精确标签\\n\", \"total_chars\": 3099, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "840332e2-34dc-4bf5-a0b7-04300d58f659",
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "1d94166e-7a46-42a5-b874-7330c74718a5",
  "sourceToolAssistantUUID": "840332e2-34dc-4bf5-a0b7-04300d58f659",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T21:28:36.464Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GeoFNNjcQdvNYC8kaav98v`</summary>

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
  "parentUuid": "1d94166e-7a46-42a5-b874-7330c74718a5",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXkQW6qkRzU5yUH23uk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66ad010d-b151-47e4-b0e3-6a1a7ede9d05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fs39Ap6oQb6d1zLJFVZr9a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3631,
      "cache_read_input_tokens": 17148,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3631
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 301,
          "cache_read_input_tokens": 17148,
          "cache_creation_input_tokens": 3631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3631,
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

_source line 15 · 2026-05-20T21:28:36.481Z_

<details><summary>↩ Tool result · `toolu_01GeoFNNjcQdvNYC8kaav98v`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-20T17:30:00.000Z\\\"\\n  total_papers: 10\\ncategories:\\n  - key: \\\"contamination_detection\\\"\\n    name: \\\"Benchmark Contamination Detection\\\"\\n    narrative: \\\"Methods for detecting training data contamination in LLM benchmarks, including RL-robust approaches\\\"\\n  - key: \\\"irt_equating\\\"\\n    name: \\\"IRT Methodology & Equating\\\"\\n    narrative: \\\"Item Response Theory models, calibration, equating, and their application to LLM evaluation\\\"\\n  - key: \\\"benchmark_design\\\"\\n    name: \\\"Dynamic Benchmark Design\\\"\\n    narrative: \\\"Approaches for creating contamination-resistant or self-updating benchmarks\\\"\\n  - key: \\\"dif_methodology\\\"\\n    name: \\\"DIF Statistical Methods\\\"\\n    narrative: \\\"Differential Item Functioning detection methods, power analysis, and small-sample strategies\\\"\\n  - key: \\\"item_generation\\\"\\n    name: \\\"Automated Item Generation\\\"\\n    narrative: \\\"LLM-based test item generation with difficulty control and psychometric validation\\\"\\npapers:\\n  wang2026fragility:\\n    title: \\\"On The Fragility of Benchmark Contamination Detection in Reasoning Models\\\"\\n    authors:\\n      - \\\"Wang, Y.\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2510.02386\\\"\\n    bibtex_key: \\\"wang2026fragility\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Proves GRPO/PPO RL training conceals contamination signals (14-20pp AUROC degradation), motivating our DIF-based approach which operates on behavioral patterns immune to NLL smoothing\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  liang2026dvd:\\n    title: \\\"DVD: Detection via Variance of Generation Distribution for Variant Contamination\\\"\\n    authors:\\n      - \\\"Liang, Y.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2601.04895\\\"\\n    bibtex_key: \\\"liang2026dvd\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Detects variant contamination via generation variance (AUC 0.73-0.74 vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under RL training\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  tao2026selfcritique:\\n    title: \\\"Detecting Data Contamination from Reinforcement Learning Post-training\\\"\\n    authors:\\n      - \\\"Tao, S.\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2510.09259\\\"\\n    bibtex_key: \\\"tao2026selfcritique\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse detection, but remains individual-model-level; our DIF is group-level and complementary\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  polo2026growingpains:\\n    title: \\\"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\\\"\\n    authors:\\n      - \\\"Polo, F.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"polo2026growingpains\\\"\\n    category: \\\"irt_equating\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Uses multidimensional IRT with fixed-parameter calibration and 100 anchor items for extensible evaluation (rho>=0.9); addresses score comparability but NOT contamination detection or item regeneration\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  polo2026psnirt:\\n    title: \\\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\\\"\\n    authors:\\n      - \\\"Polo, F.\\\"\\n    year: 2026\\n    venue: \\\"AAAI 2026\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"polo2026psnirt\\\"\\n    category: \\\"irt_equating\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"PSN-IRT analyzes benchmark quality via 4PL IRT; provides published IRT parameters for MMLU we can use in semi-synthetic validation\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  white2025livebench:\\n    title: \\\"LiveBench: A Challenging, Contamination-Free LLM Benchmark\\\"\\n    authors:\\n      - \\\"White, C.\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"white2025livebench\\\"\\n    category: \\\"benchmark_design\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Monthly-updated contamination-free benchmark with objective scoring; no difficulty calibration or psychometric equivalence across updates\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  zhang2024gsm1k:\\n    title: \\\"A Careful Examination of Large Language Model Performance on Grade School Arithmetic\\\"\\n    authors:\\n      - \\\"Zhang, H.\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2405.00332\\\"\\n    bibtex_key: \\\"zhang2024gsm1k\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"GSM1K documents 10-13% average accuracy drops from contamination; provides ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4 logits) critical for our DIF power analysis\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  hardy2026scalability:\\n    title: \\\"Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients\\\"\\n    authors:\\n      - \\\"Hardy, M.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2603.24999\\\"\\n    bibtex_key: \\\"hardy2026scalability\\\"\\n    category: \\\"irt_equating\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Nonparametric signed isotonic R2 scalability coefficients outperform IRT item diagnostics; lightweight pre-filter for item quality before our parametric calibration\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  kim2019fpc:\\n    title: \\\"Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data\\\"\\n    authors:\\n      - \\\"Kim, S.\\\"\\n      - \\\"Kolen, M.\\\"\\n    year: 2019\\n    venue: \\\"Applied Measurement in Education\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"kim2019fpc\\\"\\n    category: \\\"irt_equating\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Fixed-parameter calibration requires only N>=200 vs N>=500 for full calibration; core methodology for our bifactor IRT equating with anchor items\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  belzak2020smallsample:\\n    title: \\\"Testing Differential Item Functioning in Small Samples\\\"\\n    authors:\\n      - \\\"Belzak, W.\\\"\\n    year: 2020\\n    venue: \\\"Multivariate Behavioral Research\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"belzak2020smallsample\\\"\\n    category: \\\"dif_methodology\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Parsimonious logistic regression with sum scores outperforms complex IRT models for DIF detection in small samples; directly applicable to our N=50-80 model cohorts\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n\", \"total_chars\": 7312, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66ad010d-b151-47e4-b0e3-6a1a7ede9d05",
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "60b0515a-49f0-46bf-a56f-74b5083fedcf",
  "sourceToolAssistantUUID": "66ad010d-b151-47e4-b0e3-6a1a7ede9d05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-20T21:28:39.573Z_

Now let me read the actual paper draft and any related framing documents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60b0515a-49f0-46bf-a56f-74b5083fedcf",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXkmPx9ikiLQMkcmFwY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2eaeff97-a46d-4b65-8b1f-1af7c7735525",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MP1jmiwEPRyw7VUKGn8GZN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5772,
      "cache_read_input_tokens": 20779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5772,
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

_source line 17 · 2026-05-20T21:28:41.030Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01P8QbdLPN41MNWCJzxm4JKN`</summary>

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
  "parentUuid": "2eaeff97-a46d-4b65-8b1f-1af7c7735525",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXkmPx9ikiLQMkcmFwY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db02dd40-b632-4235-8e5d-906d814bf12e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MP1jmiwEPRyw7VUKGn8GZN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5772,
      "cache_read_input_tokens": 20779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5772,
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

_source line 18 · 2026-05-20T21:28:41.040Z_

<details><summary>↩ Tool result · `toolu_01P8QbdLPN41MNWCJzxm4JKN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md\", \"content\": \"# Paper Framing — irt_equated_bench_regen\\n\\n## Target Venue\\n- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)\\n- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)\\n- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)\\n\\n## Core Claims (3 条, 可证伪)\\n\\n**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.\\n\\n**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.\\n\\n**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.\\n\\n## Story Spine\\n\\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \\\"Model B outperforms Model A on MMLU,\\\" we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.\\n\\n**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\\n\\n**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. A nuance: partial exploitation (model memorizes but answers correctly only p<1 of the time) shrinks DIF effect size proportionally — we formally characterize detection power as a function of exploitation rate. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates a psychometric monitoring and regeneration framework — applying mature, validated psychometric tools to solve an urgent ML evaluation problem.\\n\\n**Headline result template**: \\\"On MMLU with 5,000+ models spanning a capability range from near-random (46% accuracy) to near-saturation (60%), DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026). Leveraging the unprecedented scale of METABENCH (5,219 models), we conduct the largest DIF analysis in LLM evaluation literature.\\\"\\n\\n## Venue Fit Risks\\n\\n- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ \\\"fairness testing for items\\\").\\n- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: \\\"examinees\\\" → \\\"models\\\", \\\"test items\\\" → \\\"benchmark questions\\\", \\\"DIF\\\" → \\\"item-level contamination signal\\\", \\\"equating\\\" → \\\"score comparability across benchmark versions\\\".\\n- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as \\\"bringing mature psychometric tools to solve an urgent ML problem\\\" rather than \\\"inventing new statistics.\\\"\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"DIF power is only sufficient for large effects (δ≥1.4)\\\"**\\n   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.\\n   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)\\n\\n2. **\\\"Model cohort sample sizes are too small for classical DIF\\\"**\\n   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.\\n   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)\\n\\n3. **\\\"Only validated in simulation\\\"**\\n   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.\\n   - Evidence needed: plan_001, plan_004\\n\\n4. **\\\"Item regeneration quality — how do you ensure replacements measure the same construct?\\\"**\\n   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.\\n   - Evidence needed: plan_005, plan_006\\n\\n5. **\\\"RL robustness is only theoretical — where's the empirical evidence?\\\"**\\n   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.\\n   - Evidence needed: plan_002\\n\\n6. **\\\"Computational cost of the full pipeline\\\"**\\n   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.\\n\\n7. **\\\"DIF flags may reflect capability improvement, not contamination\\\"**\\n   - Response: Post-2024 models are both more capable and more contaminated. We control for this via (a) within-family DIF analysis (same architecture at different training stages, e.g., Llama-2→3→3.1), where capability trajectory is known, isolating contamination-specific DIF; (b) domain-specificity analysis of DIF flags vs known capability trajectories; (c) bifactor model's subject-specific factors as covariates to absorb domain-specific capability gains.\\n   - Evidence needed: plan_001 (within-family sub-analysis), plan_005 (bifactor covariates)\\n\\n8. **\\\"Ground truth is too noisy to validate DIF\\\"**\\n   - Response: Three-layer validation strategy. (a) Li et al. (EMNLP 2024) web-overlap labels as proxy — but we frame correctly: Li et al. measures *existence* contamination (item on web), DIF measures *differential* contamination (item behaves differently across cohorts). Low concordance is expected and explained, not a failure. FPR on Li-clean items is the primary metric. (b) Semi-synthetic injection: controlled ground truth with known contamination injected into real response matrix. (c) GSM8K/GSM1K cross-benchmark validation with independent ground truth.\\n   - Evidence needed: plan_001 (Li et al. proxy), plan_011 (semi-synthetic), plan_004 (GSM8K)\\n\\n9. **\\\"Partial exploitation defeats DIF — RL models may only exploit p<1 of memorized items\\\"**\\n   - Response: Formal power analysis as function of exploitation rate p shows: at p=1.0 DIF detects with TPR=0.72-0.85; at p=0.6 effect size shrinks ~0.6×, falling to medium range where ensemble's ConStat signal provides coverage. DIF + ensemble jointly cover p≥0.4. Below p=0.4, contamination impact on rankings is minimal.\\n   - Evidence needed: plan_002 (partial exploitation analysis)\\n\", \"total_chars\": 8779, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db02dd40-b632-4235-8e5d-906d814bf12e",
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "c012f7ea-69e6-4c94-82a5-f870ee42ab22",
  "sourceToolAssistantUUID": "db02dd40-b632-4235-8e5d-906d814bf12e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T21:28:41.504Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01ALebcaUeSeqd4nBryTReWT`</summary>

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
  "parentUuid": "c012f7ea-69e6-4c94-82a5-f870ee42ab22",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXkmPx9ikiLQMkcmFwY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f5e5423-3282-4a99-a5ce-112d599dec89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MP1jmiwEPRyw7VUKGn8GZN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5772,
      "cache_read_input_tokens": 20779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5772,
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

_source line 20 · 2026-05-20T21:28:41.513Z_

<details><summary>↩ Tool result · `toolu_01ALebcaUeSeqd4nBryTReWT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ROADMAP.md\", \"content\": \"# irt_equated_bench_regen — Research Dashboard\\n\\n> 最后更新: 2026-05-20 21:18 UTC | 更新原因: Reviewer 修正：quintile×year overlap 前置检查 + plan_011 ability-matched 注入 + 核心方向措辞更新\\n\\n> 最后更新: 2026-05-20 21:25 UTC | 更新原因: Reviewer 修正（quintile×year overlap 检查 + plan_011 ability-matched 注入）\\n\\n## 核心方向\\n验证能力匹配/IRT 条件化 DIF 用于 LLM benchmark 污染检测的可行性。Naive temporal DIF 被 impact-vs-DIF 混淆淹没（D004），正在探索分离能力差异与污染信号的方法。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research — 方法改进中\\n- **MVP**: 通过（D001/D002，仿真条件下 DIF 有效）\\n- **plan_001 首轮**: ❌ Temporal cohort DIF 证伪（enrichment=0.96，D004）\\n  - 根因：impact vs DIF 混淆（能力差异淹没污染信号）\\n  - ability-quintile enrichment=1.19（微弱但方向正确）\\n- **Re-dream**: dream_20260520T205007 运行中\\n- **plan_002**: 暂停（等 DIF 基础方法跑通）\\n\\n## 方法改进三路并行（全 CPU，0 GPU-h）\\n| 方向 | 内容 | 状态 | 成功标准 |\\n|------|------|------|----------|\\n| 方向 1 | Matched-ability temporal DIF（quintile 内 2023 vs 2024） | Worker 中（需先验 quintile×year overlap） | enrichment > 1.5 + Fisher p < 0.05 |\\n| 方向 2 | IRT equating 代码准备（py-irt 2PL θ 估计） | Worker 准备中 | 代码就绪 |\\n| plan_011 | Semi-synthetic validation（已知污染注入，ability-matched 框架） | Worker 中 | TPR > 0.5 at p=1.0, FPR < 0.05 |\\n\\n**决策树**：\\n- plan_011 TPR 高 + 方向 1 enrichment 高 → 能力匹配解决问题，Claim 1 加 nuance\\n- plan_011 TPR 高 + 方向 1 失败 → 转 IRT θ-conditioning（方向 2）\\n- plan_011 TPR 低 → DIF 在此数据上根本性受限，评估 pivot\\n\\n## 近期任务\\n- [ ] 等 3 Workers 结果（方向 1 / plan_011 / 方向 2 代码）\\n- [ ] 等 re-dream 回调（dream_20260520T205007）\\n- [ ] 根据结果决定 Claim 1 修正方向\\n\\n## GPU 预算\\nP0: 250h | P1: 350h | P2: 0h | 已用: 0h（当前全部 CPU 分析）\\n\\n## 投稿目标\\nICLR 2027（~2026年10月 DDL）| AAAI 2027（2026.07.28）| EACL 2027 ARR August（2026.08.03）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D005 | 2026-05-20 | 方向 1 (matched-ability DIF) 失败确认，所有 quintile enrich | plan_001b_matched_ability_dif |\\n| D004 | 2026-05-20 | plan_001 temporal cohort DIF 证伪（enrichment=0.96），根 | plan_001_real_data_dif_mmlu |\\n| D003 | 2026-05-20 | Dream analysis (dream_20260520T194223): 6 confirme | — |\\n| D002 | 2026-05-20 | MVP 通过：DIF+ETS C 在 N≥80,δ≥1.4 下功效达标，推荐 N≥100 为主操作点 | mvp_dif_power_sim, mvp_dif_power_sim_phase2 |\\n| D001 | 2026-05-20 | MVP DIF 检测采用 ETS C 分类（效应量+显著性双阈值）替代 BH 校正 p 值作为主判定 | mvp_dif_power_sim |\\n\\n\", \"total_chars\": 2141, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f5e5423-3282-4a99-a5ce-112d599dec89",
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "a3e2b1c4-da4f-4225-922e-bb5ff4f601fa",
  "sourceToolAssistantUUID": "1f5e5423-3282-4a99-a5ce-112d599dec89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T21:28:43.138Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0161DpSnSFNW2zWd2tavPebK`</summary>

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
  "parentUuid": "a3e2b1c4-da4f-4225-922e-bb5ff4f601fa",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXkmPx9ikiLQMkcmFwY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0a2d160-d851-4e8c-8a69-d3cc38f36cc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MP1jmiwEPRyw7VUKGn8GZN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5772,
      "cache_read_input_tokens": 20779,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5772
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 311,
          "cache_read_input_tokens": 20779,
          "cache_creation_input_tokens": 5772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5772,
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

_source line 22 · 2026-05-20T21:28:43.150Z_

<details><summary>↩ Tool result · `toolu_0161DpSnSFNW2zWd2tavPebK`</summary>

```text
artifacts/dream_reports/dream_20260520T194223/best/paper.tex
artifacts/dream_reports/dream_20260520T194223/median/paper.tex
artifacts/dream_reports/dream_20260520T194223/worst/paper.tex
artifacts/dream_reports/dream_20260520T205007/best/paper.tex
artifacts/dream_reports/dream_20260520T205007/median/paper.tex
artifacts/dream_reports/dream_20260520T205007/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0a2d160-d851-4e8c-8a69-d3cc38f36cc0",
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "ae7efb8a-e19b-463d-ba9d-237103c8f5f9",
  "sourceToolAssistantUUID": "b0a2d160-d851-4e8c-8a69-d3cc38f36cc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-20T21:28:47.897Z_

Let me read the latest paper draft (the "best" version from the most recent dream report).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae7efb8a-e19b-463d-ba9d-237103c8f5f9",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXmFmWrg35LBwPBxtVg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d579dee2-4e98-429a-adb3-d6cead684813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ar77A5fAjLEESfRrEgAFP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4529,
      "cache_read_input_tokens": 26551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4529,
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

_source line 24 · 2026-05-20T21:28:49.581Z_

<details open><summary>🔧 Tool call — Read · `toolu_014ADXWgXHfU5X2cX9CAe1uR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d579dee2-4e98-429a-adb3-d6cead684813",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXmFmWrg35LBwPBxtVg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6be690a-a961-4841-a72b-65d3f07cc68d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ar77A5fAjLEESfRrEgAFP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4529,
      "cache_read_input_tokens": 26551,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4529
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 26551,
          "cache_creation_input_tokens": 4529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4529,
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

_source line 25 · 2026-05-20T21:28:49.838Z_

<details><summary>↩ Tool result · `toolu_014ADXWgXHfU5X2cX9CAe1uR`</summary>

```text
1	\documentclass{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{hyperref}
9	\usepackage[margin=1in]{geometry}
10	\usepackage{natbib}
11	\usepackage{xcolor}
12	\usepackage{array}
13	\usepackage{tabularx}
14	
15	\title{Benchmark Contamination Is a Psychometric Problem:\\DIF-Based Detection, Multi-Signal Ensemble, and\\IRT-Equated Benchmark Regeneration}
16	
17	\author{Anonymous}
18	\date{}
19	
20	\begin{document}
21	\maketitle
22	
23	%==================== ABSTRACT ====================
24	\begin{abstract}
25	LLM benchmarks implicitly assume temporal score comparability, yet contamination systematically erodes this validity.
26	Critically, reinforcement learning (GRPO/PPO) conceals contamination signals from all existing reference-free detectors, degrading them to near-random performance.
27	We reframe contamination as a psychometric problem: it creates \emph{Differential Item Functioning} (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict.
28	Because DIF operates on group-level Item Characteristic Curves conditional on ability, it is orthogonal to within-model output distribution smoothing---the one contamination signal RL cannot conceal.
29	In the largest DIF analysis in LLM evaluation to date (5,219 models on MMLU via METABENCH), ETS~C detection achieves TPR 0.72--0.85 at FPR $<$0.05 for large contamination effects ($\delta \geq 1.4$), maintaining detection power on RL-trained models where 10 existing methods degrade to near-random (AUROC $\leq 0.53$).
30	We construct a multi-signal ensemble combining DIF, perturbation-based testing, and generation variance analysis to cover the full effect-size spectrum, achieving 82\% contamination coverage.
31	Finally, we demonstrate that bifactor IRT equating enables psychometrically equivalent benchmark regeneration: replacing flagged items with empirically calibrated alternatives while preserving rank-order stability ($\rho = 0.975$) through a formal graceful-degradation framework.
32	\end{abstract}
33	
34	%==================== 1. INTRODUCTION ====================
35	\section{Introduction}
36	
37	When we claim ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent ability measured under equivalent conditions.
38	Benchmark contamination---the inclusion of test items in training data---systematically violates this assumption by inflating scores for exposed models.
39	The problem is growing: Li et al.\ found 39.5\% of MMLU items show evidence of contamination across the model ecosystem, and the shift toward RL-trained reasoning models (DeepSeek-R1, QwQ, o1/o3) makes it worse.
40	Wang et al.\ (ICLR 2026) demonstrated that GRPO/PPO training degrades all reference-free contamination detectors by 14--20 percentage points in AUROC, reducing most to near-random ($\sim$50\% AUROC) after $\sim$156 training steps.
41	
42	Existing approaches address fragments of this problem.
43	LiveBench updates items monthly from recent sources but applies no psychometric calibration across updates.
44	ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask.
45	Growing Pains uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination detection.
46	No existing work closes the full loop from RL-robust detection through calibrated generation to psychometrically equated regeneration.
47	
48	We argue that contamination is fundamentally a \emph{psychometric} problem.
49	In educational testing, Differential Item Functioning (DIF) detects items that behave differently across subgroups after controlling for overall ability---precisely the signature that contamination produces.
50	A contaminated item becomes easier for exposed models \emph{beyond what their general ability predicts}, creating a detectable shift in the item's characteristic curve at the population level.
51	This signal is orthogonal to within-model output distribution smoothing: RL can flatten a model's token-level probability distribution, but it cannot change the fact that exposed models answer contaminated items correctly more often than their ability warrants.
52	The only way to eliminate this group-level behavioral anomaly would be to make the model ``forget'' the contaminated knowledge---which contradicts the purpose of contamination.
53	
54	We make three contributions, each supported by extensive empirical validation:
55	
56	\begin{enumerate}
57	\item \textbf{RL-Robust Detection.} DIF-based ETS~C detection achieves TPR 0.72--0.85 / FPR $<$0.05 at $\delta \geq 1.4$ and maintains AUROC = 0.91 on RL-trained model cohorts, where ConStat and Min-K\% degrade to AUROC $\leq 0.53$ (Section~\ref{sec:detection}).
58	
59	\item \textbf{Full-Spectrum Ensemble.} A multi-signal sentinel combining DIF, ConStat perturbation testing, and DVD generation variance achieves 82\% contamination coverage across the full effect-size and model-type landscape (Section~\ref{sec:ensemble}).
60	
61	\item \textbf{Psychometric Regeneration.} Bifactor IRT equating with anchor items enables benchmark regeneration that preserves rank-order stability ($\rho = 0.975$, mean rank displacement 1.8) through a formal graceful-degradation framework (Section~\ref{sec:regeneration}).
62	\end{enumerate}
63	
64	%==================== 2. RELATED WORK ====================
65	\section{Related Work}
66	
67	\paragraph{Benchmark Contamination Detection.}
68	Contamination detection methods fall into two categories: \emph{output-based} methods that analyze model outputs (Min-K\%, perplexity analysis, membership inference), and \emph{performance-based} methods that analyze accuracy patterns (ConStat, benchmark comparison).
69	Output-based methods require access to model internals and are vulnerable to RL smoothing of output distributions.
70	ConStat (Binkyte et al., 2024) uses perturbation sensitivity under FDR control but degrades on RL-trained models.
71	DVD (Data Variation Detection) analyzes generation variance to identify memorized items.
72	All existing methods operate at the individual-model level, making them susceptible to RL-induced distribution smoothing.
73	
74	\paragraph{IRT for LLM Evaluation.}
75	Item Response Theory has been applied to LLM evaluation for ability estimation and item analysis.
76	Growing Pains (arXiv 2026) proposes multidimensional IRT for extensible evaluation across benchmark updates.
77	Polo et al.\ use IRT to analyze benchmark item quality.
78	None of these works apply DIF---a core psychometric tool for detecting item bias---to the contamination detection problem.
79	
80	\paragraph{Benchmark Maintenance.}
81	LiveBench (White et al., 2024) addresses staleness through monthly updates from recent sources but provides no psychometric calibration guaranteeing score comparability.
82	DynaBoard and Dynabench use adversarial data collection but do not address contamination of existing items.
83	Our bifactor IRT equating framework provides formal guarantees of score comparability across benchmark versions---a standard requirement in educational testing that has not been applied to LLM benchmarks.
84	
85	\paragraph{DIF in Psychometrics.}
86	DIF analysis is a mature methodology in educational testing, with the ETS classification system (A/B/C) providing standardized effect-size thresholds.
87	The Mantel-Haenszel procedure and logistic regression are the most common detection methods.
88	Sinharay et al.\ (2006) introduced cumulative Bayesian DIF priors for longitudinal monitoring.
89	Tutz \& Berger (2016) proposed Item-Focused Trees for continuous covariates.
90	We apply these established tools to the novel context of LLM benchmark contamination.
91	
92	%==================== 3. METHOD ====================
93	\section{Method}
94	\label{sec:method}
95	
96	\subsection{Problem Formulation}
97	
98	Let $\mathbf{X} \in \{0,1\}^{N \times J}$ be the binary response matrix of $N$ models on $J$ benchmark items, where $x_{ij} = 1$ indicates model $i$ answered item $j$ correctly.
99	Under IRT, each model has a latent ability $\theta_i$ and each item has parameters $(a_j, b_j)$ (discrimination and difficulty), with response probability:
100	\begin{equation}
101	P(X_{ij} = 1 \mid \theta_i) = \frac{1}{1 + \exp(-a_j(\theta_i - b_j))}
102	\end{equation}
103	Contamination causes item $j$'s parameters to differ between exposed (focal) and unexposed (reference) model groups.
104	Specifically, if focal-group models have memorized item $j$, the item becomes easier for them ($b_{j,\text{focal}} < b_{j,\text{ref}}$), creating DIF.
105	
106	\subsection{DIF Detection via ETS Classification}
107	
108	We use the Mantel-Haenszel (MH) procedure to detect DIF.
109	Models are stratified by ability quintiles (based on total score), and for each item, the MH odds ratio $\alpha_{\text{MH}}$ is computed.
110	The log-odds effect size $\Delta_{\text{MH}} = -2.35 \ln(\alpha_{\text{MH}})$ is classified using ETS thresholds:
111	\begin{itemize}
112	\item \textbf{A} (negligible): $|\Delta_{\text{MH}}| < 1.0$
113	\item \textbf{B} (moderate): $1.0 \leq |\Delta_{\text{MH}}| < 1.5$ and statistically significant
114	\item \textbf{C} (large): $|\Delta_{\text{MH}}| \geq 1.5$ and statistically significant
115	\end{itemize}
116	We flag items classified as ETS~C as contaminated, corresponding to $\delta \geq 1.4$ in our parameterization.
117	
118	\paragraph{Cohort Definition.}
119	We define focal/reference groups via two complementary strategies: (a) \emph{temporal cohorts} based on model release date (e.g., 2023 vs.\ 2024 models), and (b) \emph{ability quintile cohorts} comparing the highest-ability quintile (Q5) against Q1--Q3.
120	Both strategies are validated against Item-Focused Trees (Section~\ref{sec:ift}), which treat release date as a continuous covariate.
121	
122	\paragraph{RL Robustness Argument.}
123	DIF detection is inherently robust to RL training because it operates on the \emph{population-level behavioral pattern} (the proportion of models answering correctly, conditional on ability), not on any individual model's output distribution.
124	GRPO/PPO training smooths a model's token-level probabilities, but cannot change the fact that exposed models systematically answer contaminated items correctly at higher rates than their ability predicts.
125	Formally, if model $i$ has memorized item $j$ with exploitation probability $p$, the population-level DIF effect size scales as $\delta \propto p \cdot \delta_{\max}$.
126	
127	\subsection{Multi-Signal Ensemble}
128	
129	DIF excels at large effect sizes ($\delta \geq 1.4$) and is RL-robust, but its power decreases for medium effects.
130	We complement DIF with two additional signals:
131	
132	\paragraph{ConStat Perturbation Testing.}
133	For each item, we generate semantically equivalent reformulations and compare model performance on original vs.\ reformulated versions.
134	Contaminated models show disproportionate performance drops on reformulations (perturbation sensitivity).
135	This signal is effective for non-RL models (AUROC 0.78) but degrades under RL smoothing (AUROC 0.53).
136	
137	\paragraph{DVD Generation Variance.}
138	For open-weight models, we generate 50 responses per item at temperature $T \in [0.7, 1.0]$ and analyze the entropy of the response distribution.
139	Variant contamination (exposure to item variants) produces bimodal generation distributions, detectable via entropy analysis.
140	
141	\paragraph{Fusion Strategy.}
142	The three signals are combined via weighted fusion with cross-validated weights: DIF (0.45), ConStat (0.35), DVD (0.20).
143	The union of flagged items across all three signals defines the ensemble's contamination set.
144	
145	\subsection{Bifactor IRT Equating for Benchmark Regeneration}
146	
147	To replace contaminated items while preserving score comparability, we employ bifactor IRT equating:
148	
149	\paragraph{Bifactor Model.}
150	We fit a bifactor model with one general factor $g$ and $K$ subject-specific group factors $s_k$:
151	\begin{equation}
152	P(X_{ij} = 1 \mid \theta_i) = \frac{1}{1 + \exp(-a_{jg}\theta_{ig} - a_{jk}\theta_{ik} - d_j)}
153	\end{equation}
154	where $a_{jg}$ is the loading on the general factor, $a_{jk}$ is the loading on subject factor $k$, and $d_j$ is the intercept.
155	
156	\paragraph{Anchor Item Selection.}
157	From the set of DIF-clean items, we select anchor items satisfying: (a) no DIF flag across any cohort definition, (b) discrimination $a > 0.3$, (c) difficulty $b \in [-2, 2]$.
158	These anchor items fix the measurement scale across benchmark versions.
159	
160	\paragraph{Fixed-Parameter Calibration.}
161	New replacement items are calibrated by fixing anchor item parameters and estimating new item parameters on the same scale.
162	This ensures that ability estimates ($\theta$) from the regenerated benchmark are directly comparable to those from the original.
163	
164	\paragraph{Item Generation.}
165	Replacement items are generated using LLMs with construct constraints (matching subject, cognitive level, and difficulty target).
166	Difficulty is calibrated via student simulation rather than prompt-based targeting, achieving $\rho = 0.79$ between target and empirical difficulty (vs.\ $\rho = 0.28$ for prompt-based methods).
167	
168	%==================== 4. DIF DETECTION AT SCALE ====================
169	\section{DIF Detection at Scale}
170	\label{sec:detection}
171	
172	\subsection{Real-Data DIF on METABENCH MMLU}
173	
174	We apply DIF analysis to the full METABENCH dataset: 5,219 models evaluated on 12,508 MMLU items.
175	Table~\ref{tab:dif_summary} summarizes detection results across cohort definitions.
176	
177	\begin{table}[h]
178	\centering
179	\caption{DIF detection summary by cohort definition on METABENCH MMLU ($N = 5{,}219$ models, $J = 12{,}508$ items).}
180	\label{tab:dif_summary}
181	\small
182	\begin{tabular}{lrrrcc}
183	\toprule
184	Cohort Type & $N_{\text{focal}}$ & $N_{\text{ref}}$ & Flagged (C) & \% Flagged & Li Prec./Rec. \\
185	\midrule
186	Temporal (2023 vs 2024) & 658 & 1,253 & 1,850 & 14.8\% & 0.62 / 0.38 \\
187	Quintile (Q5 vs Q1--Q3) & 1,044 & 3,131 & 2,100 & 16.8\% & 0.58 / 0.42 \\
188	Temporal, neg-disc removed & 658 & 1,253 & 1,630 & 15.3\% & 0.67 / 0.34 \\
189	Within-family (Llama) & 135 & 308 & 280 & 2.2\% & --- \\
190	\bottomrule
191	\end{tabular}
192	\end{table}
193	
194	The temporal cohort flags 14.8\% of items as ETS~C, consistent with Li et al.'s 39.5\% total contamination rate---DIF captures only the large-effect-size subset.
195	The overlap between temporal and quintile flags (Jaccard = 0.58) indicates substantial agreement despite different grouping strategies.
196	
197	\paragraph{Within-Family Analysis.}
198	To control for the confound that post-2024 models are both more capable and more contaminated, we perform within-family DIF analysis on Llama (2$\to$3$\to$3.1) and Qwen families.
199	The 68\% cross-cohort overlap with the full-population DIF flags indicates that most DIF reflects contamination exposure differences rather than pure capability evolution, since within-family capability trajectories are controlled.
200	
201	\paragraph{Domain Specificity.}
202	Table~\ref{tab:domain_dif} shows that DIF flags are not uniformly distributed across domains.
203	
204	\begin{table}[h]
205	\centering
206	\caption{Domain specificity of DIF flags. STEM over-representation (OR = 1.8$\times$) is consistent with known code/math training data duplication patterns.}
207	\label{tab:domain_dif}
208	\small
209	\begin{tabular}{lrrrc}
210	\toprule
211	Domain Cluster & $N$ Items & $N$ Flagged & Flag Rate & OR vs Baseline \\
212	\midrule
213	STEM (math/physics/CS) & 3,200 & 620 & 19.4\% & 1.8 \\
214	Social Sciences & 3,800 & 510 & 13.4\% & 0.95 \\
215	Humanities & 3,100 & 340 & 11.0\% & 0.65 \\
216	Professional/Other & 2,408 & 380 & 15.8\% & 1.1 \\
217	\bottomrule
218	\end{tabular}
219	\end{table}
220	
221	STEM items are flagged at 1.8$\times$ the baseline rate, consistent with the known over-representation of code and mathematics content in LLM training corpora.
222	
223	\subsection{RL Robustness Empirical Validation}
224	
225	We evaluate DIF detection power across three model cohorts: SFT-only baseline, alignment-RL (DPO/ORPO, $N = 477$), and reasoning-RL (DeepSeek-R1, Qwen2.5-RL, and other GRPO/PPO models mixed into the focal cohort).
226	Table~\ref{tab:rl_robustness} presents the key comparison.
227	
228	\begin{table}[h]
229	\centering
230	\caption{DIF vs.\ baseline detectors across model types. DIF maintains AUROC = 0.91 on reasoning-RL models where ConStat and Min-K\% degrade to near-random.}
231	\label{tab:rl_robustness}
232	\small
233	\begin{tabular}{llcccc}
234	\toprule
235	Detector & Cohort & AUROC & 95\% CI & TPR@FPR05 \\
236	\midrule
237	DIF (ETS C) & SFT-only & 0.92 & [0.89, 0.95] & 0.79 \\
238	DIF (ETS C) & Alignment-RL mixed & 0.91 & [0.88, 0.94] & 0.78 \\
239	DIF (ETS C) & Reasoning-RL mixed & 0.91 & [0.88, 0.94] & 0.76 \\
240	\midrule
241	ConStat & SFT-only & 0.78 & [0.73, 0.83] & 0.55 \\
242	ConStat & Reasoning-RL & 0.53 & [0.47, 0.59] & 0.12 \\
243	\midrule
244	Min-K\% & SFT-only & 0.72 & [0.66, 0.78] & 0.42 \\
245	Min-K\% & Reasoning-RL & 0.51 & [0.44, 0.58] & 0.08 \\
246	\bottomrule
247	\end{tabular}
248	\end{table}
249	
250	DIF retention ratio is 0.97 for alignment-RL and 0.93 for reasoning-RL (TOST equivalence test $p = 0.02$, rejecting the hypothesis that DIF degrades under RL).
251	The DeLong test confirms the AUROC difference between DIF and ConStat on RL models is statistically significant ($p = 0.0003$).
252	
253	\paragraph{Partial Exploitation Power Curve.}
254	Table~\ref{tab:partial_exploit} characterizes detection power as a function of the exploitation rate $p$ (the probability that a model exploits memorized knowledge on a given item).
255	
256	\begin{table}[h]
257	\centering
258	\caption{Detection power as a function of exploitation rate $p$. DIF covers $p \geq 0.6$; the ensemble extends coverage to $p \approx 0.4$.}
259	\label{tab:partial_exploit}
260	\small
261	\begin{tabular}{ccccc}
262	\toprule
263	$p$ & Effective $\delta$ & ETS C TPR & Ensemble TPR & Coverage Gap \\
264	\midrule
265	1.0 & 1.6 & 0.78 & 0.82 & none \\
266	0.8 & 1.28 & 0.68 & 0.74 & none \\
267	0.6 & 0.96 & 0.52 & 0.65 & none (ConStat) \\
268	0.5 & 0.80 & 0.41 & 0.58 & marginal \\
269	0.4 & 0.64 & 0.30 & 0.48 & ensemble boundary \\
270	\bottomrule
271	\end{tabular}
272	\end{table}
273	
274	The handoff point between DIF and ensemble coverage occurs at $p \approx 0.52$, where DIF's TPR drops below 0.41 and ConStat's signal (effective for non-RL models) takes over.
275	Below $p = 0.4$, contamination impact on rankings is minimal ($\delta < 0.64$, corresponding to $<$2 rank positions).
276	
277	\subsection{Architecture-Stratified DIF}
278	\label{sec:arch_strat}
279	
280	IRT's unidimensionality assumption may be violated when the model population includes diverse architectures.
281	We compare DIF detection on the full population ($N = 5{,}219$) versus a decoder-only subset ($N = 3{,}650$).
282	
283	\begin{table}[h]
284	\centering
285	\caption{IRT fit diagnostics by population. Decoder-only subgroup achieves ``good'' fit, full population remains ``acceptable.''}
286	\label{tab:irt_fit}
287	\small
288	\begin{tabular}{lrccccl}
289	\toprule
290	Population & $N$ & RMSEA & CFI & TLI & SRMR & Fit Quality \\
291	\midrule
292	Full (all architectures) & 5,219 & 0.067 & 0.90 & 0.89 & 0.058 & acceptable \\
293	Decoder-only & 3,650 & 0.038 & 0.95 & 0.94 & 0.032 & good \\
294	Decoder-only, neg-disc removed & 3,650 & 0.031 & 0.96 & 0.96 & 0.027 & good \\
295	\bottomrule
296	\end{tabular}
297	\end{table}
298	
299	\begin{table}[h]
300	\centering
301	\caption{DIF detection quality by population. Architecture stratification reduces spurious DIF by 24\%.}
302	\label{tab:dif_quality_pop}
303	\small
304	\begin{tabular}{lccc}
305	\toprule
306	Population & TPR ($\delta \geq 1.4$) & FPR & Spurious Reduced \\
307	\midrule
308	Full & 0.78 & 0.042 & --- \\
309	Decoder-only & 0.81 & 0.032 & 125 items \\
310	\bottomrule
311	\end{tabular}
312	\end{table}
313	
314	Architecture stratification improves IRT fit from ``acceptable'' to ``good'' (RMSEA: 0.067 $\to$ 0.038) and reduces FPR by 24\%.
315	Importantly, the full-population RMSEA = 0.067 remains within the acceptable range ($\leq$0.08), so the main analysis can use the full population with the stratified analysis serving as a robustness check.
316	
317	\subsection{Item-Focused Trees}
318	\label{sec:ift}
319	
320	To address the concern of arbitrary cohort boundaries, we implement Item-Focused Trees (IFT) following Tutz \& Berger (2016), treating model release date as a continuous covariate.
321	
322	\begin{table}[h]
323	\centering
324	\caption{IFT vs.\ categorical DIF. IFT achieves comparable detection power without requiring predefined cohort boundaries.}
325	\label{tab:ift}
326	\small
327	\begin{tabular}{lcccc}
328	\toprule
329	Method & TPR ($\delta \geq 1.4$) & FPR & $N$ Flagged & Requires Cohort Def. \\
330	\midrule
331	ETS C (temporal) & 0.78 & 0.040 & 1,850 & yes \\
332	ETS C (quintile) & 0.74 & 0.050 & 2,100 & yes \\
333	Item-Focused Trees & 0.76 & 0.045 & 1,950 & no \\
334	\bottomrule
335	\end{tabular}
336	\end{table}
337	
338	IFT identifies a median split point at September 2023, consistent with the known timeline of large-scale web crawling for LLM training data.
339	Its detection power (TPR = 0.76) is comparable to categorical DIF (0.78), confirming that our cohort-based results are not artifacts of arbitrary grouping.
340	
341	%==================== 5. MULTI-SIGNAL ENSEMBLE ====================
342	\section{Multi-Signal Ensemble}
343	\label{sec:ensemble}
344	
345	\subsection{ConStat Perturbation Testing}
346	
347	We generate semantically equivalent reformulations for 250 MMLU items and evaluate perturbation sensitivity across 50 models spanning SFT-only, DPO/ORPO, and GRPO/PPO training paradigms.
348	
349	\begin{table}[h]
350	\centering
351	\caption{ConStat detection power by model type. RL smoothing reduces perturbation sensitivity by 3$\times$, degrading AUROC from 0.78 to 0.53.}
352	\label{tab:constat}
353	\small
354	\begin{tabular}{lrccc}
355	\toprule
356	Model Type & $N$ & AUROC & TPR@FDR05 & Mean Sensitivity \\
357	\midrule
358	SFT-only & 25 & 0.78 & 0.52 & 0.18 \\
359	DPO/ORPO & 15 & 0.62 & 0.35 & 0.11 \\
360	GRPO/PPO & 10 & 0.53 & 0.12 & 0.06 \\
361	All & 50 & 0.68 & 0.40 & 0.13 \\
362	\bottomrule
363	\end{tabular}
364	\end{table}
365	
366	The perturbation sensitivity ratio between non-RL and RL models (3.0$\times$) quantifies the RL smoothing effect and explains ConStat's degradation.
367	This motivates ConStat's role in the ensemble as a non-RL-model specialist rather than a universal detector.
368	
369	\subsection{DVD Generation Variance}
370	
371	For 12 open-weight models, we generate 50 responses per item ($N = 500$ items) at temperature $T \in [0.7, 1.0]$ and analyze generation entropy.
372	
373	\begin{table}[h]
374	\centering
375	\caption{DVD detection by contamination type. Variant contamination shows strong entropy separation (Cohen's $d = 1.15$).}
376	\label{tab:dvd}
377	\small
378	\begin{tabular}{lrccc}
379	\toprule
380	Contamination Type & $N$ Items & TPR & FPR & Mean Entropy \\
381	\midrule
382	Variant & 120 & 0.68 & 0.07 & 0.73 \\
383	Verbatim & 180 & 0.45 & 0.05 & 0.38 \\
384	Clean & 200 & --- & 0.07 & 1.42 \\
385	\bottomrule
386	\end{tabular}
387	\end{table}
388	
389	DVD is complementary to DIF: DIF excels at verbatim large-effect contamination (TPR 0.78), while DVD targets variant contamination (TPR 0.68) that produces bimodal generation distributions.
390	The entropy separation between clean and contaminated items (Cohen's $d = 1.15$) confirms that generation variance is a reliable contamination signal.
391	
392	\subsection{Ensemble Fusion}
393	
394	We combine DIF, ConStat, and DVD via three fusion strategies: 2-of-3 majority vote, optimized weighted fusion (5-fold cross-validated), and union.
395	
396	\begin{table}[h]
397	\centering
398	\caption{Ensemble strategy comparison. The full ensemble (union) achieves 82\% contamination coverage, up from 58\% for DIF alone.}
399	\label{tab:ensemble}
400	\small
401	\begin{tabular}{lcccc}
402	\toprule
403	Strategy & TPR ($\delta \geq 1.4$) & TPR ($\delta \geq 0.8$) & FPR & Coverage \\
404	\midrule
405	DIF only & 0.78 & 0.51 & 0.04 & 58\% \\
406	ConStat only & 0.52 & 0.45 & 0.04 & 38\% \\
407	DVD only & 0.45 & 0.42 & 0.07 & 32\% \\
408	2-of-3 majority & 0.74 & 0.62 & 0.04 & 72\% \\
409	Weighted (optimized) & 0.78 & 0.68 & 0.06 & 78\% \\
410	Weighted (uniform) & 0.75 & 0.65 & 0.055 & 75\% \\
411	Full ensemble (union) & 0.82 & 0.72 & 0.055 & 82\% \\
412	\bottomrule
413	\end{tabular}
414	\end{table}
415	
416	Each signal covers the blind spots of the others: DIF handles large effects and RL-robust detection, ConStat covers medium effects for non-RL models (marginal gain +15\%), and DVD captures variant contamination (+9\%).
417	The uniform-weight baseline (TPR 0.75) is only 3pp below the optimized weights (0.78), demonstrating robustness to weight selection.
418	Cross-validation standard deviations are small (TPR $\pm$0.03, FPR $\pm$0.01).
419	
420	%==================== 6. VALIDATION ====================
421	\section{Validation}
422	
423	\subsection{Cross-Benchmark GSM8K Validation}
424	
425	We validate DIF on GSM8K ($J = 1{,}319$ items, $N = 65$ models) using GSM1K---a fully independent set of 1,000 newly written math problems---as ground truth.
426	The per-model accuracy gap between GSM8K and GSM1K directly reflects contamination impact.
427	
428	\begin{table}[h]
429	\centering
430	\caption{GSM8K DIF flags vs.\ GSM1K accuracy gap. DIF-flagged items show 2.2$\times$ larger accuracy gaps ($r = 0.58$, $p < 10^{-5}$).}
431	\label{tab:gsm8k}
432	\small
433	\begin{tabular}{lrccc}
434	\toprule
435	Item Group & $N$ Items & Mean Gap & Std Gap & DIF Flag Rate \\
436	\midrule
437	DIF-flagged (ETS C) & 185 & 0.13 & 0.08 & 1.00 \\
438	DIF-clean & 1,134 & 0.06 & 0.05 & 0.00 \\
439	All GSM8K & 1,319 & 0.07 & 0.06 & 0.14 \\
440	\bottomrule
441	\end{tabular}
442	\end{table}
443	
444	The correlation between DIF flags and GSM8K--GSM1K accuracy gap ($r = 0.58$, $p < 10^{-5}$) provides independent cross-benchmark evidence.
445	The effect size (Cohen's $d = 0.92$) confirms that DIF-flagged items correspond to substantively contaminated items in an independent ground truth.
446	
447	\subsection{Semi-Synthetic Contamination Validation}
448	
449	To provide controlled ground truth unavailable from noisy external labels (MMLU-CF $\kappa = 0.14$), we inject known contamination signals into the real METABENCH response matrix.
450	From 500 clean items, we select 100--200 items and inject synthetic contamination by flipping responses (incorrect $\to$ correct with probability $p$) for focal-group models.
451	
452	\begin{table}[h]
453	\centering
454	\caption{Semi-synthetic validation with controlled ground truth. TPR = 0.81 at $\delta \geq 1.4$, $p = 1.0$, confirming simulation-based predictions.}
455	\label{tab:semi_synth}
456	\small
457	\begin{tabular}{cccccc}
458	\toprule
459	$p$ & $\delta$ & Focal $N$ & Prevalence & TPR & FPR \\
460	\midrule
461	1.0 & 1.6 & 80 & 15\% & 0.81 & 0.035 \\
462	1.0 & 1.4 & 80 & 15\% & 0.78 & 0.033 \\
463	0.8 & 1.4 & 80 & 15\% & 0.72 & 0.031 \\
464	0.6 & 1.4 & 80 & 15\% & 0.55 & 0.028 \\
465	1.0 & 1.4 & 40 & 15\% & 0.62 & 0.038 \\
466	1.0 & 1.4 & 200 & 15\% & 0.85 & 0.030 \\
467	1.0 & 1.4 & 80 & 5\% & 0.79 & 0.032 \\
468	1.0 & 1.4 & 80 & 30\% & 0.78 & 0.040 \\
469	\bottomrule
470	\end{tabular}
471	\end{table}
472	
473	\begin{table}[h]
474	\centering
475	\caption{Simulation vs.\ semi-synthetic comparison. Semi-synthetic TPR consistently exceeds pure simulation by 3--10pp, indicating that real data structure is favorable for DIF detection.}
476	\label{tab:sim_vs_semi}
477	\small
478	\begin{tabular}{lccc}
479	\toprule
480	Condition & Sim TPR & Semi-Synth TPR & Difference \\
481	\midrule
482	$N = 80$, $\delta = 1.4$ & 0.682 & 0.78 & +0.098 \\
483	$N = 100$, $\delta = 1.4$ & 0.758 & 0.81 & +0.052 \\
484	$N = 100$, $\delta = 1.6$ & 0.797 & 0.83 & +0.033 \\
485	\bottomrule
486	\end{tabular}
487	\end{table}
488	
489	Semi-synthetic results consistently exceed pure simulation TPR by 3--10pp, indicating that the real METABENCH data structure (item correlations, ability distribution) is \emph{favorable} for DIF detection.
490	TPR is stable across prevalence rates (5--30\%), confirming that ETS~C's magnitude-based threshold is insensitive to contamination base rate.
491	
492	\subsection{Cumulative Bayesian DIF}
493	
494	To address the power limitation at medium effect sizes ($\delta \approx 1.0$), we implement cumulative Bayesian DIF priors following Sinharay et al.\ (2006), accumulating evidence across successive benchmark administrations.
495	
496	\begin{table}[h]
497	\centering
498	\caption{Cumulative Bayesian DIF power trajectory. Three administrations raise power at $\delta = 1.0$ from 0.42 to 0.68, approaching single-administration power at $\delta = 1.4$.}
499	\label{tab:bayesian_dif}
500	\small
501	\begin{tabular}{rrccc}
502	\toprule
503	Administrations & Cumulative $N$ & Power ($\delta = 1.0$) & Power ($\delta = 0.8$) & Posterior Prob \\
504	\midrule
505	1 & 80 & 0.42 & 0.28 & 0.55 \\
506	2 & 160 & 0.55 & 0.38 & 0.68 \\
507	3 & 240 & 0.68 & 0.50 & 0.82 \\
508	4 & 320 & 0.74 & 0.58 & 0.89 \\
509	\bottomrule
510	\end{tabular}
511	\end{table}
512	
513	After three administrations, power at $\delta = 1.0$ reaches 0.68 with posterior probability 0.82---approaching the single-administration power for large effects.
514	This transforms medium-effect detection from ``infeasible in one shot'' to ``achievable through continuous monitoring,'' providing a theoretical framework for long-term benchmark health surveillance.
515	
516	%==================== 7. BENCHMARK REGENERATION ====================
517	\section{Benchmark Regeneration}
518	\label{sec:regeneration}
519	
520	\subsection{Bifactor IRT Equating}
521	
522	We fit a bifactor model on METABENCH MMLU with one general factor and 57 subject-specific factors, then perform fixed-parameter calibration equating.
523	
524	\begin{table}[h]
525	\centering
526	\caption{Bifactor model fit statistics. The decoder-only subset achieves good fit (RMSEA $< 0.05$, CFI $> 0.93$).}
527	\label{tab:bifactor_fit}
528	\small
529	\begin{tabular}{lccc}
530	\toprule
531	Metric & Full Population & Decoder-Only & Threshold \\
532	\midrule
533	RMSEA & 0.062 & 0.043 & $<$0.08 / $<$0.05 \\
534	CFI & 0.91 & 0.94 & $>$0.90 / $>$0.95 \\
535	General factor \% variance & 0.58 & 0.62 & $>$0.50 \\
536	$N$ anchor items & 780 & 800 & $>$500 \\
537	\bottomrule
538	\end{tabular}
539	\end{table}
540	
541	The general factor explains 62\% of variance in the decoder-only subset, supporting the premise that MMLU primarily measures a unitary general ability dimension.
542	We select 800 anchor items (DIF-clean, discrimination $> 0.3$, difficulty $\in [-2, 2]$) with cross-cohort DIF rate of only 2\% and ICC stability of 0.96.
543	
544	\begin{table}[h]
545	\centering
546	\caption{Equating quality metrics. Rank-order stability ($\rho = 0.975$) exceeds the 0.95 target with mean rank displacement of only 1.8 positions.}
547	\label{tab:equating_quality}
548	\small
549	\begin{tabular}{lcc}
550	\toprule
551	Metric & Value & Target \\
552	\midrule
553	Spearman $\rho$ (original vs equated) & 0.975 & $\geq 0.95$ \\
554	Kendall $\tau$ & 0.962 & $\geq 0.93$ \\
555	Mean rank displacement & 1.8 & $<$5 \\
556	Max rank displacement & 12 & $<$20 \\
557	\% models within $\pm$3 ranks & 89\% & $>$80\% \\
558	\bottomrule
559	\end{tabular}
560	\end{table}
561	
562	After replacing 500 contaminated items with empirically calibrated alternatives, the equated benchmark achieves $\rho = 0.975$ rank-order correlation with the original---89\% of models shift by 3 or fewer rank positions.
563	
564	\subsection{Item Generation and Calibration}
565	
566	We compare three approaches for generating replacement items: student simulation calibration, prompt-based difficulty targeting, and random generation.
567	
568	\begin{table}[h]
569	\centering
570	\caption{Calibration method comparison. Student simulation achieves $\rho = 0.79$ difficulty correlation, 2.8$\times$ better than prompt-based targeting.}
571	\label{tab:calibration}
572	\small
573	\begin{tabular}{lcccc}
574	\toprule
575	Method & Difficulty $\rho$ & Discrim.\ $\rho$ & Construct Match & Items Passing \\
576	\midrule
577	Student simulation & 0.79 & 0.72 & 92\% & 420 / 500 \\
578	Prompt-based targeting & 0.28 & 0.21 & 88\% & 380 / 500 \\
579	Random generation & 0.05 & 0.03 & 75\% & 280 / 500 \\
580	\bottomrule
581	\end{tabular}
582	\end{table}
583	
584	Student simulation calibration---which estimates item difficulty by simulating responses from models at varying ability levels---achieves 2.8$\times$ higher difficulty correlation than prompt-based targeting ($\rho = 0.79$ vs.\ $0.28$).
585	The pass rate of 84\% demonstrates that LLM-based item generation under construct constraints is practical at scale.
586	
587	\subsection{Graceful Degradation Analysis}
588	
589	We formalize benchmark validity degradation under progressive item replacement, establishing both theoretical bounds and empirical validation.
590	
591	\begin{table}[h]
592	\centering
593	\caption{Graceful degradation under progressive item replacement. At the observed DIF flag rate ($\sim$15\%), ranking stability remains high ($\rho > 0.98$). Critical threshold at $\sim$35\% replacement.}
594	\label{tab:degradation}
595	\small
596	\begin{tabular}{ccccc}
597	\toprule
598	Replacement Rate & Spearman $\rho$ & Score Reliability & Construct Coverage & $N$ Replaced \\
599	\midrule
600	0\% & 1.000 & 1.00 & 1.00 & 0 \\
601	5\% & 0.995 & 0.98 & 0.99 & 625 \\
602	10\% & 0.988 & 0.96 & 0.98 & 1,251 \\
603	20\% & 0.972 & 0.93 & 0.95 & 2,502 \\
604	50\% & 0.935 & 0.87 & 0.89 & 6,254 \\
605	\bottomrule
606	\end{tabular}
607	\end{table}
608	
609	Ranking stability degrades linearly at a rate of $-0.0013$ per percentage point of replacement.
610	At the observed DIF flag rate of $\sim$15\% ($\sim$1,850 items), the predicted $\rho = 0.990$ indicates excellent rank preservation.
611	The critical replacement rate---where $\rho$ drops below the conventional 0.95 threshold---is approximately 35\%, providing a large safety margin above current contamination levels.
612	
613	%==================== 8. CONCLUSION ====================
614	\section{Conclusion}
615	
616	We have presented a psychometric framework for benchmark contamination that unifies detection, monitoring, and regeneration.
617	Three key results:
618	
619	\textbf{(1)} DIF-based detection operates on group-level behavioral patterns and is provably orthogonal to RL-induced output smoothing.
620	In the largest DIF analysis of LLM benchmarks to date (5,219 models), ETS~C achieves TPR 0.72--0.85 at FPR $<$0.05 for $\delta \geq 1.4$, maintaining AUROC = 0.91 on RL-trained models where ConStat and Min-K\% degrade to $\leq 0.53$.
621	
622	\textbf{(2)} A multi-signal ensemble combining DIF, ConStat, and DVD achieves 82\% contamination coverage---up from 58\% for DIF alone---with each signal covering the others' blind spots across the effect-size and model-type landscape.
623	
624	\textbf{(3)} Bifactor IRT equating enables psychometrically principled benchmark regeneration, achieving $\rho = 0.975$ rank-order stability after replacing contaminated items, with a formal graceful-degradation framework establishing a critical replacement threshold at $\sim$35\%.
625	
626	Beyond detection, this work demonstrates that mature psychometric tools---DIF, IRT equating, bifactor modeling---provide rigorous solutions to urgent problems in LLM evaluation.
627	The cumulative Bayesian DIF framework further enables long-term monitoring, transforming contamination management from reactive replacement to proactive surveillance.
628	
629	\paragraph{Limitations.}
630	DIF requires cohort sizes of $N \geq 80$ for adequate power at large effect sizes; smaller model families cannot be individually assessed.
631	The ensemble's ConStat component degrades under RL, limiting its contribution for the growing population of reasoning models.
632	Item generation via student simulation requires a calibration panel of diverse models, introducing a bootstrapping dependency.
633	Our graceful-degradation analysis assumes replacement items are generated from the same construct universe; violations of this assumption (e.g., construct drift in generated items) would reduce the effective safety margin.
634	
635	\bibliographystyle{plainnat}
636	\bibliography{references}
637	
638	\end{document}
639	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6be690a-a961-4841-a72b-65d3f07cc68d",
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "979b627c-5909-4521-9cb1-63bc19905813",
  "sourceToolAssistantUUID": "a6be690a-a961-4841-a72b-65d3f07cc68d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-20T21:28:56.475Z_

Now let me also check the earlier dream report for comparison and any decisions log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "979b627c-5909-4521-9cb1-63bc19905813",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXmkNUAYgpW4G21ZZLQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9353332d-e8c2-4e57-b1a8-7c5f38bb0f4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwRYeQbbhfNT5dYvPDCFF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13059,
      "cache_read_input_tokens": 31080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13059,
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

_source line 27 · 2026-05-20T21:28:57.487Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011HNdZGFBigMncaH24yKroi`</summary>

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
  "parentUuid": "9353332d-e8c2-4e57-b1a8-7c5f38bb0f4f",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXmkNUAYgpW4G21ZZLQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a330b56-8f7e-4a0b-a175-c09cfb93cd8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwRYeQbbhfNT5dYvPDCFF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13059,
      "cache_read_input_tokens": 31080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13059,
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

_source line 28 · 2026-05-20T21:28:57.498Z_

<details><summary>↩ Tool result · `toolu_011HNdZGFBigMncaH24yKroi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/decisions.yaml\", \"content\": \"_next_id: 6\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:50 UTC\\n  summary: MVP DIF 检测采用 ETS C 分类（效应量+显著性双阈值）替代 BH 校正 p 值作为主判定标准\\n  rationale: Monte Carlo 模拟显示 BH 校正在 200 items 场景下将 TPR 压缩 40-60%，所有核心条件均 FAIL/GRAY。但\\n    ETS C 分类（|Δ_MH|≥1.5 + 显著性，教育测量 gold standard）在 N≥80, δ≥1.4 时 TPR=0.72-0.85, FPR<0.05，满足\\n    pass criteria。ETS C 是 DIF 领域标准实践（Holland & Thayer 1988），使用效应量阈值比纯 p 值更稳健。操作点 N≥80,\\n    δ≥1.4 与 GSM1K 文档的重度污染效应量吻合。小效应由 ensemble 其他信号覆盖。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'BH-corrected: all FAIL/GRAY; ETS C: PASS at N≥80,δ≥1.4 (TPR=0.72-0.85,\\n      FPR<0.05)'\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:31 UTC\\n  summary: MVP 通过：DIF+ETS C 在 N≥80,δ≥1.4 下功效达标，推荐 N≥100 为主操作点\\n  rationale: Phase 1 合成参数 + Phase 2 真实参数（PSN-IRT）均验证 ETS C TPR≥0.65 at N≥80,δ≥1.4。Phase\\n    2 比 Phase 1 降低 3-6pp 符合预期。N=80,δ=1.4 裕度仅 0.032，推荐 N≥100 为主 claim。数据源为 PSN-IRT\\n    而非 ROADMAP 指定的 METABENCH，research 阶段需用 METABENCH 补充验证。限制：δ<1.0 需 ensemble 其他信号。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'Phase 1 conditional pass: ETS C TPR=0.72-0.85 at N≥80,δ≥1.4'\\n  - exp_id: mvp_dif_power_sim_phase2\\n    role: evidence\\n    result: 'Phase 2 pass: ETS C TPR=0.68-0.80 at N≥80,δ≥1.4 with real MMLU params'\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 20:49 UTC\\n  summary: 'Dream analysis (dream_20260520T194223): 6 confirmed actions from cross-tier\\n    synthesis, 2 new experiments added (plan_010/011), framing qualified'\\n  rationale: 'Dream scores met thresholds (best=4/6, median=3.5/6, worst=3/6). Cross-tier\\n    analysis identified 6 confirmed issues (≥2 tiers): (1) contamination-capability\\n    confound → within-family analysis added to plan_001; (2) RL evidence underpowered\\n    → bootstrap CIs + equivalence testing added to plan_002; (3) partial exploitation\\n    gap → power analysis added to plan_002; (4) ground truth circularity → plan_011\\n    semi-synthetic validation added; (5) related work thin → Paper Agent writing-phase\\n    task; (6) Growing Pains differentiation → Paper Agent task. Additionally: plan_010\\n    architecture-stratified DIF added as P1 proactive defense from worst-case; novelty\\n    claim qualified from \\\"first self-healing benchmark\\\" to \\\"psychometric monitoring\\n    framework\\\". Re-dream required before P0 approval.'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 21:14 UTC\\n  summary: plan_001 temporal cohort DIF 证伪（enrichment=0.96），根因是 impact vs DIF 混淆。批准\\n    matched-ability DIF 作为方法改进方向 1\\n  rationale: Temporal cohort MH-DIF 标记 31.3% items 为 ETS C，但 enrichment=0.96（clean\\n    和 contaminated 标记概率相同）—— DIF 检测的是系统性能力提升而非污染。Within-family (Llama-2 vs Llama-3)\\n    61.3% C 进一步证实。这是经典 impact vs DIF 混淆（Dream D2 预测过）。但 ability-quintile enrichment=1.19\\n    + FPR=2.7% 表明信号存在但弱。方向1 matched-ability temporal DIF 在 quintile 内做时间对比，是最快验证能力匹配能否放大信号的路径。方向2\\n    IRT equating 并行准备作为 fallback。\\n  related_experiments:\\n  - exp_id: plan_001_real_data_dif_mmlu\\n    role: evidence\\n    result: negative - temporal cohort enrichment 0.96, ability quintile enrichment\\n      1.19\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-20 21:24 UTC\\n  summary: 方向 1 (matched-ability DIF) 失败确认，所有 quintile enrichment 0.94-1.04。plan_011\\n    是唯一决定性实验\\n  rationale: Quintile 内 temporal DIF 仍 enrichment≈1.0，ability matching 未能分离污染信号。但\\n    Reviewer 指出关键洞察：Li et al. web-overlap 是全局性污染（Common Crawl 对所有模型可用），不应产生 group-specific\\n    DIF。enrichment≈1.0 可能是 ground truth 不匹配而非方法失败。plan_011 注入的是已知差异性污染（仅 focal group），是唯一能区分\\\"DIF\\n    不 work\\\"和\\\"ground truth 不对\\\"的实验。方向 2 (IRT θ-matching) 如果问题出在 ground truth 也无法解决。\\n  related_experiments:\\n  - exp_id: plan_001b_matched_ability_dif\\n    role: evidence\\n    result: negative - all quintiles enrichment 0.94-1.04\\n  depends_on:\\n  - D004\\n\", \"total_chars\": 3783, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a330b56-8f7e-4a0b-a175-c09cfb93cd8d",
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "5b545034-4a8e-4ab2-97e9-1a7a7a769998",
  "sourceToolAssistantUUID": "4a330b56-8f7e-4a0b-a175-c09cfb93cd8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T21:28:59.094Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JxHkLEM4XkdbH1w1PWTZPo`</summary>

```json
{
  "pattern": "**/plan_001_report*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b545034-4a8e-4ab2-97e9-1a7a7a769998",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXmkNUAYgpW4G21ZZLQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8c9307f-a0cc-4ae2-9685-e4400df14bdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwRYeQbbhfNT5dYvPDCFF5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13059,
      "cache_read_input_tokens": 31080,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13059
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 31080,
          "cache_creation_input_tokens": 13059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13059,
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

_source line 30 · 2026-05-20T21:28:59.105Z_

<details><summary>↩ Tool result · `toolu_01JxHkLEM4XkdbH1w1PWTZPo`</summary>

```text
artifacts/plan_001/plan_001_report.md
artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md
artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report_00ca1f.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8c9307f-a0cc-4ae2-9685-e4400df14bdd",
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "ad7fb225-b6c2-4169-a1d7-23a6e837b395",
  "sourceToolAssistantUUID": "f8c9307f-a0cc-4ae2-9685-e4400df14bdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T21:29:03.179Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cp1AyEZeS51aqrQ1GCSYXW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad7fb225-b6c2-4169-a1d7-23a6e837b395",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXnSUigAtKwd8GsX1sN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "015a62ce-99b4-4ede-9879-382ff97d17f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017w7BRN6j8KzgC12xVyEozk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2387,
      "cache_read_input_tokens": 44139,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2387
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 44139,
          "cache_creation_input_tokens": 2387,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2387,
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

_source line 32 · 2026-05-20T21:29:03.184Z_

<details><summary>↩ Tool result · `toolu_01Cp1AyEZeS51aqrQ1GCSYXW`</summary>

```text
1	# Plan 001: METABENCH Real-Data MH-DIF Analysis
2	
3	## 1. Data & Setup
4	
5	- Response matrix: **5227 models × 12508 items** (binary, MMLU)
6	- Temporal cohort: ref = 2023 (N=1080), foc = 2024 (N=807), 5 strata
7	- Ability cohort: ref = Q1-2 (N=2092), foc = Q4-5 (N=2089), 10 strata
8	- Li et al. annotations: 9229 annotated items
9	
10	## 2. ETS Classification
11	
12	| Cohort | Filter | Items | A | B | C | %C | FPR (clean) | Enrichment |
13	|--------|--------|-------|---|---|---|----|-------------|------------|
14	| temporal | all | 12508 | 6332 | 2258 | 3918 | 31.32% | 0.3184 | 0.96 |
15	| ability | all | 12508 | 11052 | 1093 | 363 | 2.90% | 0.0269 | 1.19 |
16	| temporal | non_neg_disc | 10582 | 5327 | 1830 | 3425 | 32.37% | 0.3258 | 0.97 |
17	
18	## 3. Li et al. Proxy Validation
19	
20	| Cohort | FPR (clean) | Rate (contam) | Rate (clean) | Rate (unlabeled) | Enrichment |
21	|--------|-------------|---------------|--------------|------------------|------------|
22	| temporal | 0.3184 | 0.3070 | 0.3184 | 0.3114 | 0.96 |
23	| ability | 0.0269 | 0.0321 | 0.0269 | 0.0293 | 1.19 |
24	
25	## 4. Within-Family Analysis
26	
27	- **llama-2 vs llama-3**: A=2718, B=2118, C=7672 (61.34%)
28	- **mistral vs mixtral**: A=3905, B=3768, C=4835 (38.66%)
29	
30	### Cross-cohort vs within-family overlap
31	
32	- **llama-2_vs_llama-3**: both_C=2611, temp_only_C=1307, wf_only_C=5061
33	- **mistral_vs_mixtral**: both_C=2031, temp_only_C=1887, wf_only_C=2804
34	
35	## 5. Domain Specificity
36	
37	Spearman ρ(C_rate, Δacc) = **0.307** (p = 0.0201)
38	
39	Top 15 subjects by C rate (temporal cohort):
40	
41	| Subject | Items | C | %C | Acc 2023 | Acc 2024 | ΔAcc |
42	|---------|-------|---|-----|----------|----------|------|
43	| business_ethics | 93 | 45 | 48.4% | 0.558 | 0.612 | +0.054 |
44	| human_aging | 203 | 85 | 41.9% | 0.644 | 0.660 | +0.016 |
45	| formal_logic | 109 | 44 | 40.4% | 0.402 | 0.446 | +0.044 |
46	| high_school_microeconomics | 220 | 85 | 38.6% | 0.606 | 0.661 | +0.055 |
47	| professional_medicine | 248 | 94 | 37.9% | 0.595 | 0.630 | +0.035 |
48	| professional_law | 1331 | 498 | 37.4% | 0.438 | 0.454 | +0.016 |
49	| world_religions | 159 | 59 | 37.1% | 0.743 | 0.734 | -0.009 |
50	| professional_accounting | 242 | 89 | 36.8% | 0.462 | 0.481 | +0.019 |
51	| medical_genetics | 85 | 31 | 36.5% | 0.637 | 0.678 | +0.041 |
52	| high_school_statistics | 181 | 64 | 35.4% | 0.490 | 0.532 | +0.042 |
53	| moral_scenarios | 692 | 243 | 35.1% | 0.358 | 0.410 | +0.053 |
54	| econometrics | 103 | 36 | 35.0% | 0.425 | 0.482 | +0.057 |
55	| high_school_chemistry | 181 | 63 | 34.8% | 0.478 | 0.502 | +0.024 |
56	| college_mathematics | 72 | 25 | 34.7% | 0.357 | 0.370 | +0.013 |
57	| elementary_mathematics | 317 | 110 | 34.7% | 0.405 | 0.442 | +0.038 |
58	
59	## 6. Negative-Discrimination Sensitivity
60	
61	| Item Set | Items | C | %C |
62	|----------|-------|---|----|
63	| all | 12508 | 3918 | 31.32% |
64	| non_negative_disc | 10582 | 3425 | 32.37% |
65	| negative_disc_only | 1926 | 495 | 25.70% |
66	
67	## 7. Sanity Check
68	
69	Random half-split of 2023 cohort: **0.18% C** (expect < 5%)
70	
71	## 8. Cohort Overlap
72	
73	- Temporal C: 3918 items
74	- Ability C: 363 items
75	- Both C: 60 items
76	- Jaccard index: 0.014
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "015a62ce-99b4-4ede-9879-382ff97d17f5",
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "84a7114f-833d-4214-b6c9-34658c2d320c",
  "sourceToolAssistantUUID": "015a62ce-99b4-4ede-9879-382ff97d17f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-20T21:29:09.008Z_

Now I have a thorough understanding of the paper, the experimental results, the project's internal state (including the critical finding that temporal DIF was disproven with enrichment=0.96, and matched-ability DIF also failed). Let me now produce the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84a7114f-833d-4214-b6c9-34658c2d320c",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXnjbcaUWU2QX5yYB9J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8df2c05-a8dd-4003-8e73-3fb4e66d319c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3EjFsbTR6nkeVUBiQAf64",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1794,
      "cache_read_input_tokens": 46526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1794,
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

_source line 34 · 2026-05-20T21:29:10.113Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012xW6SfRyc2iiJuJQs3tyZ6`</summary>

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
  "parentUuid": "c8df2c05-a8dd-4003-8e73-3fb4e66d319c",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXnjbcaUWU2QX5yYB9J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42e40457-81df-4eec-80e8-cf3b6473d172",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3EjFsbTR6nkeVUBiQAf64",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1794,
      "cache_read_input_tokens": 46526,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1794
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 46526,
          "cache_creation_input_tokens": 1794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1794,
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

_source line 35 · 2026-05-20T21:29:10.117Z_

<details><summary>↩ Tool result · `toolu_012xW6SfRyc2iiJuJQs3tyZ6`</summary>

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
  "parentUuid": "42e40457-81df-4eec-80e8-cf3b6473d172",
  "isSidechain": true,
  "promptId": "21d1e932-690b-4b22-a5a7-c5adfd2f8ddc",
  "agentId": "a1db4df44a4eb5957",
  "type": "user",
  "uuid": "068304ab-b067-42eb-886b-57fad94a3727",
  "sourceToolAssistantUUID": "42e40457-81df-4eec-80e8-cf3b6473d172",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-20T21:31:14.220Z_



Now I have all the information needed. Let me synthesize my review. I've read the full paper, the project's internal experimental logs, the decisions history, the actual plan_001 results, and the literature map. Critically, I've discovered that the project's own experiments show temporal DIF enrichment = 0.96 (no signal) and matched-ability DIF also failed (enrichment 0.94-1.04), yet the paper presents these results as if they succeeded. Let me write the review.

---

# Review: R2 — Novelty and Related Work

## Paper: "Benchmark Contamination Is a Psychometric Problem: DIF-Based Detection, Multi-Signal Ensemble, and IRT-Equated Benchmark Regeneration"

---

## 1. Novelty Assessment

### 1.1 Core Idea: DIF for LLM Contamination Detection

The central contribution is applying Differential Item Functioning — a 60+ year old psychometric tool (Holland & Thayer, 1988) — to detect benchmark contamination in LLMs. This is a textbook "known method to new domain" transfer. The paper itself acknowledges this framing ("bringing mature psychometric tools to solve an urgent ML problem"), which is honest, but the question is whether the transfer involves any genuine methodological innovation or non-obvious insight.

**My assessment: the transfer is competent but largely predictable.** Anyone with training in both psychometrics and LLM evaluation would recognize that contamination produces DIF — this is almost definitional. The paper's Section 3.1 directly states that contamination causes item parameters to differ between exposed and unexposed groups, which is literally the textbook definition of DIF. The mapping is: examinees → models, focal/reference groups → pre/post contamination cohorts, item bias → contamination. This mapping requires no conceptual leap.

The ETS A/B/C classification system, the MH procedure, quintile-based stratification — all are off-the-shelf psychometric tools used exactly as designed. The paper does not extend, modify, or improve any of these methods.

**Novelty: Low.** This is application, not innovation.

### 1.2 The RL Robustness Argument

The paper's strongest novelty claim is that DIF is "orthogonal" to RL smoothing because it operates on group-level behavioral patterns rather than individual output distributions. This argument has some merit — it correctly identifies that GRPO/PPO smooths token-level probabilities but cannot change the binary correct/incorrect outcome pattern at the population level without eliminating the contamination advantage itself.

However, several concerns:

1. **The "provably orthogonal" claim (Section 8) has no proof.** There is no formal theorem, no mathematical derivation showing orthogonality. The argument is informal and intuitive. The paper uses the word "provably" without providing a proof — this is a serious framing issue.

2. **Any psychometrician would have predicted this.** DIF has always been robust to individual-level response strategy variation because it aggregates over examinees. The observation that group-level statistics are more robust than individual-level ones is not novel; it is a basic property of aggregation.

3. **The argument has a gap.** RL training does not merely smooth output distributions — it can change which items a model answers correctly. If RL training causes a contaminated model to answer a memorized item incorrectly some fraction of the time (partial exploitation), the DIF effect size shrinks proportionally. The paper acknowledges this (Table 5, partial exploitation curve) but does not engage with the deeper question: could RL systematically reduce exploitation probability to a level where DIF is underpowered, while still providing a net benchmark score advantage? The paper assumes exploitation rate and DIF detectability trade off linearly, but this is asserted, not demonstrated.

4. **Empirical validation is weak.** Table 3 shows DIF AUROC = 0.91 on "Reasoning-RL mixed" cohorts, but the paper does not clarify what "RL mixed" means — are these models that were confirmed to be contaminated and RL-trained? The ground truth problem is severe here. The AUROC of 0.91 is computed against what labels? If against Li et al. web-overlap labels, then the AUROC measures something different from RL robustness (it measures concordance with a noisy proxy).

**Novelty: Low-Medium.** The intuition is correct but predictable, the formalization is absent, and the empirical support is insufficient.

### 1.3 Multi-Signal Ensemble

Combining DIF + ConStat + DVD is straightforward engineering. The paper runs three existing detectors and takes their union (or weighted fusion). The fusion weights are cross-validated, which is standard practice. The "each signal covers the blind spots of the others" framing is descriptively accurate but does not constitute a methodological contribution.

The weighted fusion achieves 78% TPR versus 75% for uniform weights (Table 9) — a 3pp improvement that is within the reported cross-validation standard deviation (±3pp). This means the optimized weights are not meaningfully better than equal weighting, which further undermines any claim of a principled fusion methodology.

**Novelty: Negligible.** Running multiple detectors and taking the union is not a contribution.

### 1.4 Bifactor IRT Equating for Regeneration

Bifactor IRT models and fixed-parameter calibration equating are standard psychometric practice (Kim & Kolen, 2019; Reise, 2012). The application to LLM benchmark regeneration is new in the sense that nobody has done exactly this before, but the methodology is entirely off-the-shelf.

The student simulation calibration approach (using LLMs to simulate responses at varying ability levels for difficulty estimation) is potentially the most novel component, achieving rho=0.79 versus rho=0.28 for prompt-based targeting. However, this is presented in a single table (Table 14) with no methodological detail about the simulation procedure, what "student simulation" means concretely, or how construct constraints are operationalized. This potentially interesting contribution is underexplored.

**Novelty: Low.** Standard psychometric methodology; the student simulation idea is underexplored.

### 1.5 The "Full Loop" Integration

Does integration itself constitute novelty? The paper argues that no prior work "closes the full loop from RL-robust detection through calibrated generation to psychometrically equated regeneration." This is true — but the loop consists of independently applying three sets of existing tools (DIF detection, ensemble fusion, IRT equating), not of a genuinely integrated system where the components interact in non-trivial ways. The DIF detection does not inform the equating in any deep way; it simply produces a list of items to replace. The equating does not feed back into detection. The ensemble does not adapt based on regeneration outcomes.

**Novelty: Low.** The integration is sequential application, not synergistic combination.

### 1.6 Are the Three Contributions Genuinely Distinct?

No. Contributions 1 and 2 are both about detection (DIF alone, then DIF + two others). Contribution 3 (regeneration) is somewhat distinct but relies entirely on standard IRT methodology. A more honest framing would be: "We apply DIF to LLM contamination detection, show it complements existing detectors, and demonstrate that standard IRT equating can regenerate contaminated benchmarks." This is one idea (psychometric tools for benchmark contamination) with two corollaries.

---

## 2. Related Work Completeness

### 2.1 Missing Citations

Several important lines of work are absent:

**IRT applications to LLM evaluation beyond those cited:**
- Elo rating systems (e.g., Chatbot Arena / LMSYS) share the latent ability estimation motivation but use pairwise comparisons rather than IRT. The relationship should be discussed.
- Burnham et al. (2024) on adaptive testing for LLMs — directly relevant to item exposure control.
- The broader "LLM-as-examinee" literature, including work by Polo et al. beyond the two papers cited.

**Contamination detection methods not cited:**
- N-gram overlap methods (Dodge et al., 2021; Sainz et al., 2023) — the simplest and most widely used contamination detection approach.
- Embedding similarity methods.
- Training data extraction attacks (Carlini et al., 2021, 2023) — relevant because they provide a fundamentally different approach to contamination detection.
- Shi et al. (2024) "Detecting Pretraining Data from Large Language Models" — the Min-K% paper is cited in tables but not properly introduced or discussed.
- Dekoninck et al. (2024) on benchmark contamination in code models.

**DIF and measurement invariance:**
- The paper mentions DIF in psychometrics but does not discuss measurement invariance / factorial invariance (Meredith, 1993), which is the broader framework within which DIF operates. This omission matters because measurement invariance provides a more principled framework for deciding when items should be flagged — one that accounts for multidimensional structure rather than treating DIF as purely unidimensional.
- Millsap & Everson (1993) on DIF and measurement invariance in the context of group differences — directly relevant to the impact-vs-DIF confound the authors encountered.

**Benchmark refresh strategies:**
- HELM (Liang et al., 2022) and its approach to benchmark management.
- Kiela et al. (2021) Dynabench — cited but not substantively discussed regarding how it relates to the regeneration framework.
- LatestEval, FreshQA, and other temporal freshness approaches.

**Test security literature:**
- Item exposure control models (Sympson & Hetter, 1985; van der Linden & Veldkamp, 2007) from CAT — directly applicable.
- Test security breach detection in educational testing (Wollack & Fremer, 2013) — the closest analogue to this paper's problem, from the same psychometric tradition the authors claim to draw from. Its absence is notable.

### 2.2 Fairness of Positioning

The paper is mostly fair to prior work, but there are issues:

1. **ConStat is presented primarily as a failure case.** The paper emphasizes ConStat's degradation under RL (AUROC 0.53) without adequately acknowledging that ConStat was not designed for RL-trained models and performs well (AUROC 0.78) on the model population it was designed for.

2. **Min-K% is strawmanned.** It appears only in comparison tables showing its failure on RL models. The paper does not discuss what Min-K% was designed to detect (pretraining data membership) or why it is an unfair baseline for the RL scenario.

3. **LiveBench is characterized as "no psychometric calibration" without acknowledging that LiveBench's monthly refresh strategy fundamentally avoids the contamination problem rather than detecting it — a different and arguably more practical approach.

### 2.3 Wang et al. (ICLR 2026) Dependency

The entire motivating premise of the paper rests on Wang et al.'s claim that RL degrades contamination detectors. The paper takes this at face value without:
- Independently replicating the finding
- Discussing whether Wang et al.'s experimental setup (specific RL algorithm, number of steps, model family) generalizes
- Acknowledging that Wang et al. is a single study and the "all reference-free detectors degrade" claim may be overstated

This is a fragile foundation. If Wang et al.'s results do not generalize broadly, the paper's primary motivation evaporates.

---

## 3. Framing and Claims — Critical Assessment

### 3.1 "The one contamination signal RL cannot conceal"

This is overclaimed. DIF can fail when:
- Cohort sizes are below N=80 (acknowledged in limitations)
- Effect sizes are below delta=1.4 (acknowledged but underplayed — Table 5 shows TPR=0.30 at p=0.4)
- Contamination is uniform across cohorts (i.e., all models are equally contaminated, producing no differential functioning). The paper does not discuss this scenario, but it is increasingly realistic as training data overlap grows.
- The impact-vs-DIF confound is not resolved — **and the project's own experiments (plan_001) show this is a real problem, not a theoretical one.** Temporal DIF enrichment was 0.96 (no signal), and matched-ability DIF enrichment was 0.94-1.04. The paper presents results (Tables 1-2) that appear to show successful detection, but the project's internal records document that this approach was "disproven" (D004, D005).

### 3.2 "Provably orthogonal"

There is no proof. The word "provably" should be removed. The argument is informal: RL smooths output distributions, DIF operates on binary response patterns. But "orthogonal" has a mathematical meaning (zero covariance/correlation), and no such relationship is established formally. A weaker claim — "robust to" or "largely unaffected by" — would be more appropriate.

### 3.3 "Largest DIF analysis in LLM evaluation to date"

This is true but vacuous. As far as I know, this is also the only DIF analysis in LLM evaluation. Being the largest instance of something nobody else has done is not a meaningful superlative. It is like claiming "the largest phrenological analysis of deep learning architectures to date."

### 3.4 Three contributions or one?

As discussed in Section 1.6, these are one contribution (apply psychometric tools to contamination) with two extensions. The paper would be more honest — and potentially stronger — if it presented itself as a single unified framework rather than inflating the contribution count.

### 3.5 Critical Integrity Concern: Paper vs. Internal Results

The most serious issue I can identify: the paper presents DIF detection results (Tables 1-2) showing temporal cohort detection flagging 14.8% of items with apparent success, but the project's own experimental records (plan_001 report, decisions D004/D005) document that:

- Temporal cohort DIF enrichment = 0.96 (no discrimination between clean and contaminated items)
- Within-family DIF showed 61.3% ETS C rate for Llama-2 vs Llama-3, indicating the signal is dominated by capability differences, not contamination
- Matched-ability DIF (Direction 1) also failed with enrichment 0.94-1.04
- The ROADMAP explicitly states "Naive temporal DIF 被 impact-vs-DIF 混淆淹没"

The paper needs to reconcile these negative findings with its positive framing. Currently, the paper's tables present DIF flags and their rates but obscure the critical finding that these flags do not discriminate contaminated from clean items any better than chance (enrichment ≈ 1.0).

---

## 4. Significance and Impact

### 4.1 Would this change how the community does benchmark evaluation?

Potentially, but not in the way the paper claims. The psychometric framing is valuable as a conceptual contribution — thinking about contamination as DIF is a useful mental model. However, the practical impact is limited by:

1. DIF requires large cohorts (N >= 80), limiting applicability to well-populated benchmarks
2. The impact-vs-DIF confound is unresolved in the authors' own experiments
3. The ensemble adds engineering complexity for modest gains (3pp over uniform weighting)
4. The regeneration framework, while theoretically clean, requires substantial infrastructure (bifactor IRT calibration, student simulation, anchor item maintenance) that most benchmark maintainers are unlikely to adopt

### 4.2 Path to adoption

Unclear. The paper does not provide code, a tool, or a clear workflow that benchmark maintainers could implement. The method requires psychometric expertise that most ML practitioners lack. LiveBench's simpler approach (just refresh the items monthly) is more likely to be adopted in practice, despite being less principled.

### 4.3 New research directions

The paper does open a potentially productive direction: applying the full toolkit of educational testing (not just DIF, but also CAT, test security, item exposure control) to LLM evaluation. This is a genuinely underexplored area. However, the paper's execution does not convincingly demonstrate that this direction yields practical benefits over simpler approaches.

---

## 5. Scores

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **Novelty** | **2/4** | Competent application of known psychometric tools to a new domain. The RL robustness argument has some insight but is not formalized. No new methods are proposed. |
| **Significance** | **2/4** | The psychometric framing is conceptually useful but the practical impact is limited by unresolved confounds (impact vs. DIF), restrictive operating conditions (N>=80, delta>=1.4), and lack of clear adoption path. |
| **Overall Score** | **3/6 (Weak Reject)** | The paper competently applies existing psychometric methodology to an important problem, but (a) the novelty is insufficient for a top venue — no new methods are proposed, only known tools transferred to a new domain; (b) the core detection method's validity is undermined by the unresolved impact-vs-DIF confound evident in the authors' own real-data experiments; (c) key claims ("provably orthogonal," "the one signal RL cannot conceal") are overclaimed; (d) the related work has notable gaps in test security literature, measurement invariance, and contamination detection methods. The paper would benefit from either (i) developing genuinely new DIF methodology adapted to the LLM setting, or (ii) more honestly scoping the contribution as a position/framework paper that introduces psychometric thinking to the LLM evaluation community. |
| **Confidence** | **4/5** | I am confident in my assessment of the novelty and related work gaps. I have moderate uncertainty about the practical significance — it is possible that with more development (resolving the impact-vs-DIF confound, providing a practical tool), this direction could become impactful. |

---

## Summary for Authors

The paper identifies a real and important problem (RL-robust contamination detection) and proposes a reasonable approach (psychometric DIF analysis). However, for a top venue with ~25% acceptance rate, I expect either (a) novel methodology or (b) definitive empirical results that change practice. This paper delivers neither: the methods are entirely off-the-shelf from psychometrics, and the real-data experiments reveal an unresolved confound (impact vs. DIF) that the paper does not adequately surface. The RL robustness claim — the paper's strongest selling point — is stated informally rather than proved, and the empirical support is based on mixed cohorts rather than controlled experiments on models known to be both contaminated and RL-trained. I encourage the authors to either (1) develop DIF variants specifically adapted to the LLM setting (e.g., addressing the impact-vs-DIF confound with IRT-conditioned DIF), or (2) reframe as a shorter position paper introducing psychometric thinking to the community, which would face a lower novelty bar.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "068304ab-b067-42eb-886b-57fad94a3727",
  "isSidechain": true,
  "agentId": "a1db4df44a4eb5957",
  "requestId": "req_011CbEXoFJYBxQAM7CbaatGM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13664844-edf3-453f-8483-f3044fc985b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f0962425-fc6b-4f68-9f31-f0e56d22985d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPgVeQgwXNmBoiRmDXtQ8o",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 48320,
      "output_tokens": 4534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 771
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4534,
          "cache_read_input_tokens": 48320,
          "cache_creation_input_tokens": 771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 771,
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
