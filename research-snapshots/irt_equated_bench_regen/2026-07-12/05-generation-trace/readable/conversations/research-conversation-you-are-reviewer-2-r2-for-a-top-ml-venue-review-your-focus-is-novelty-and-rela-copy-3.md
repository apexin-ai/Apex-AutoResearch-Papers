# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty and related work**. Review the paper below us

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a0cd16afcb8320959.jsonl`
- **Structured JSON:** [`7caa9c63ef99c743a4bb.json`](../../sessions/7c/7caa9c63ef99c743a4bb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-21T02:00:34.366Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty and related work**. Review the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Acceptance rate ~25%.

## Paper Summary

**Title**: Psychometric Characterization of Item Instability in LLM Benchmarks: A Large-Scale Differential Item Functioning Analysis of MMLU

**Abstract**: Applies Differential Item Functioning (DIF) analysis to the METABENCH response matrix (5,227 models × 12,508 MMLU items). Four findings: (1) 38% of MMLU items are functionally unstable across model generations; (2) web-overlap contamination labels cannot capture differential contamination—semi-synthetic injection confirms DIF detection capability; (3) a reusable semi-synthetic validation framework with cross-subject matching; (4) DIF items concentrate discriminative signal and anti-correlate with contamination.

## Paper Structure and Content

**§1 Introduction**: Frames the problem as temporal score comparability — whether MMLU scores mean the same thing across model generations. Introduces DIF as the psychometric tool for this. Lists 4 contributions.

**§2 Related Work**:
- Benchmark contamination detection: Min-K% (Shi et al., 2024), ConStat (2024), DVD (2024). Preliminary ConStat AUROC 0.73 non-RL / 0.44 RL. DVD AUROC 0.66. Low DIF correlations (r=0.21, r=0.15) confirm orthogonal axes.
- DIF in educational testing: 40-year history. MH procedure (Mantel & Haenszel, 1959). ETS A/B/C categories. Item-Focused Trees (Tutz & Berger, 2016) — included in Appendix B.
- Benchmark integrity: Growing Pains (2024) — anchor items; LiveBench (2024) — dynamic benchmarks. Paper positions DIF as complementary.

**§3 Method**:
- §3.1: DIF primer — MH common odds ratio, ETS Δ scale, A/B/C classification
- §3.2: Semi-synthetic validation — injection methodology, cross-subject matching to avoid FPR inflation

**Key Results** (summarized):
- 31.3% C-items full population, 38.1% within-subject, 22.1% decoder-only
- Architecture stratification: C% drops 29%, IRT fit improves dramatically (RMSEA 0.082→0.037)
- Semi-synthetic: ΔTPR=+0.508 with zero FPR inflation via cross-subject matching
- GSM8K cross-benchmark validation: DIF flags anti-correlate with contamination (r=-0.478)
- Cumulative Bayesian DIF: power improves ~15pp per administration
- RL robustness: DIF maintains Jaccard=0.88, while Min-K% drops to 0.52 and ConStat to 0.48
- DIF items carry 1.09× discriminative signal, removal z-scores from -8 to -49σ

**§6 Discussion**: Explicitly frames as characterization (not contamination claim). Acknowledges ρ=0.307 means cannot decompose instability into contamination vs. genuine capability shifts.

**§7 Future Work**: Multi-signal ensemble (AUROC 0.89 pilot), per-model baselines, automated benchmark maintenance via item generation.

**§8 Conclusion**: Reframes DIF as diagnostic lens complementing (not competing with) existing approaches.

**References**: Holland & Wainer 1993, Li et al. 2024, Mantel & Haenszel 1959, Orenstrakh et al. 2024 (METABENCH), Shi et al. 2024 (Min-K%), Tutz & Berger 2016, ConStat Authors 2024, DVD Authors 2024, Growing Pains Authors 2024, LiveBench Authors 2024, Kim & Kolen 2019, Student Simulation Authors 2025.

## Your Review Task

Evaluate:
1. **Novelty**: How novel is applying DIF to LLM benchmarks? Is the cross-subject matching innovation significant? Is the "DIF as diagnostic lens" framing genuinely new?
2. **Related work coverage**: Are there missing related works? Is the positioning accurate? Does the paper fairly represent prior work?
3. **Contribution significance**: Does the 38% instability finding matter for the ML community? Is the ground truth meta-critique impactful? Is the semi-synthetic framework a real contribution?
4. **Framing and clarity**: Is the paper well-written? Is the psychometric background accessible to ML audiences? Is the characterization vs. contamination distinction clear?
5. **Scope and positioning**: Is this positioned correctly relative to Growing Pains, LiveBench, Min-K%, ConStat? Does it over-claim or under-claim?

Consider specifically:
- DIF has been used in educational testing for 40+ years but not applied to LLM benchmarks at this scale
- The ground truth meta-critique (web-overlap ≠ differential contamination) is a methodological observation affecting the entire field
- The paper explicitly avoids claiming to solve contamination detection — is this appropriate scope?
- Growing Pains (2024) uses anchor items — how does this paper's DIF analysis complement/overlap?
- Are there other psychometric methods that should have been discussed (e.g., measurement invariance, MIMIC models, propensity score matching)?

Format your output as:
### R2 Independent Review: Novelty & Related Work

**Summary** (2-3 sentences)

**Strengths** (bulleted)

**Weaknesses** (bulleted)

**Questions for Authors** (bulleted)

**Missing Related Work** (bulleted)

**Novelty Score**: X/4
**Significance Score**: X/4
**Clarity Score**: X/4
**Overall Score**: X/6
**Confidence**: X/5


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "27741ca6-31a4-40a5-9308-cb23e7795590",
  "agentId": "a0cd16afcb8320959",
  "type": "user",
  "uuid": "43dd210c-91dd-4ad2-b420-4300f182032b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T02:00:34.372Z_

```json
{
  "parentUuid": "43dd210c-91dd-4ad2-b420-4300f182032b",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
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
  "uuid": "fffde69f-a7ad-49cb-adcf-1885be93dde9",
  "timestamp": "2026-05-21T02:00:34.372Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T02:00:37.109Z_



I need to review the paper thoroughly. Let me first read the actual paper and related project files to understand the full content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fffde69f-a7ad-49cb-adcf-1885be93dde9",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtVdHKcsDb9dLudENbm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4af22126-ba08-4017-b843-b8fbea0f5faa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AkR87x8ytXCPFjaN4aH48o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7417,
      "cache_read_input_tokens": 8254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7417,
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

_source line 4 · 2026-05-21T02:00:38.082Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JaX4SHatcVX9Qzb6ejgEvM`</summary>

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
  "parentUuid": "4af22126-ba08-4017-b843-b8fbea0f5faa",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtVdHKcsDb9dLudENbm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "adc8ef4b-7668-40b8-8854-4f924b8c8b7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AkR87x8ytXCPFjaN4aH48o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7417,
      "cache_read_input_tokens": 8254,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7417
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 114,
          "cache_read_input_tokens": 8254,
          "cache_creation_input_tokens": 7417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7417,
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

_source line 5 · 2026-05-21T02:00:38.085Z_

<details><summary>↩ Tool result · `toolu_01JaX4SHatcVX9Qzb6ejgEvM`</summary>

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
  "parentUuid": "adc8ef4b-7668-40b8-8854-4f924b8c8b7b",
  "isSidechain": true,
  "promptId": "27741ca6-31a4-40a5-9308-cb23e7795590",
  "agentId": "a0cd16afcb8320959",
  "type": "user",
  "uuid": "d7232d8a-a41a-4025-b010-0657b1b5ac11",
  "sourceToolAssistantUUID": "adc8ef4b-7668-40b8-8854-4f924b8c8b7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T02:00:40.378Z_



Let me read the key project files to get full context on the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7232d8a-a41a-4025-b010-0657b1b5ac11",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtVuKyZDUsjP1qZn98g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1da24eb7-c24c-46a6-8346-c9b79209b331",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hE7YWsBHXGxuQJrQWZZJm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 15671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1296,
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

_source line 7 · 2026-05-21T02:00:41.799Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KpQ2sD9pUswm8WEQpk9ME8`</summary>

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
  "parentUuid": "1da24eb7-c24c-46a6-8346-c9b79209b331",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtVuKyZDUsjP1qZn98g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "780e831b-08a4-428e-a3e9-0408e260295d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hE7YWsBHXGxuQJrQWZZJm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 15671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1296,
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

_source line 8 · 2026-05-21T02:00:41.814Z_

<details><summary>↩ Tool result · `toolu_01KpQ2sD9pUswm8WEQpk9ME8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\\n\\n## 近期结论\\n- **plan_004_gsm8k_cross_benchmark** (negative): GSM8K 的 temporal DIF (2023 vs 2024) 将展示与 MMLU 类似的 30-40% ETS C%，证明 temporal DIF 现象跨 benchmark 泛化。使用 METABENCH 其他 benchmarks 总分做 external matching（GSM8K 无 subject 分层），预期 baseline FPR 更可控。如果 C% 在同一量级 → DIF 作为 benchmark health diagnostic 的泛化性得到验证。 ← 基于 plan_001_real_data_dif_mmlu\\n- **plan_017_downstream_impact** (negative): 移除 temporal DIF-flagged items (ETS C, ~31% of MMLU items) 后，模型跨代排名更稳定（Spearman ρ 提升），且稳定性提升显著优于随机移除相同数量 items 的 baseline。这证明 DIF 不只标记 noise，而是精确识别了 problematic items，为 DIF 作为 benchmark quality tool 提供 downstream evidence。 ← 基于 plan_001_real_data_dif_mmlu\\n- **plan_016_within_subject_semi_synthetic** (success): 在 subject 内部使用 within-subject total score 做 MH 分层的 semi-synthetic injection 中，DIF 仍能检测差异性污染（ΔTPR > 0.3 at p=0.5）。这证明 DIF 方法在 subject 级别也有效，plan_014 的 38% within-subject C% 反映的是真实代际能力差异而非方法失败。 ← 基于 plan_014_within_subject_dif\\n  [plan_016_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md) | [plan_016_dose_response](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response.csv) | [plan_016_revised_dose_response](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response_e6d86f.csv) | [plan_016_revised_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md)\\n\\n## 趋势\\n成功 5 / 负向 6 / 失败 0 / 共 11\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 2009, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "780e831b-08a4-428e-a3e9-0408e260295d",
  "isSidechain": true,
  "promptId": "27741ca6-31a4-40a5-9308-cb23e7795590",
  "agentId": "a0cd16afcb8320959",
  "type": "user",
  "uuid": "bccc5872-d0a2-4b7f-a371-c7ba84e96aac",
  "sourceToolAssistantUUID": "780e831b-08a4-428e-a3e9-0408e260295d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T02:00:42.274Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013m98VX7eUNXakr1zHBY7JJ`</summary>

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
  "parentUuid": "bccc5872-d0a2-4b7f-a371-c7ba84e96aac",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtVuKyZDUsjP1qZn98g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c70bd4c-85d7-4018-8d37-7099716900ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hE7YWsBHXGxuQJrQWZZJm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 15671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1296,
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

_source line 10 · 2026-05-21T02:00:42.285Z_

<details><summary>↩ Tool result · `toolu_013m98VX7eUNXakr1zHBY7JJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md\", \"content\": \"# Paper Framing — irt_equated_bench_regen\\n\\n## Target Venue\\n- Primary: ICLR 2027 (expected deadline ~October 2026)\\n\\n## Paper Type\\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \\\"DIF reveals benchmark structural problems,\\\" not \\\"DIF detects contamination.\\\"\\n\\n## Core Claims (4 条, 可证伪)\\n\\n**Claim 1 (Temporal Comparability Concern)**: 38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. This instability persists within every subject domain (within-subject C%=31-45%, avg 38.1%), is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). This means cross-temporal MMLU score comparisons carry uncontrolled item-level variance.\\n- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%)\\n- Honesty requirement: ρ=0.307 means \\\"item instability\\\" may mainly reflect \\\"models got better at those domains\\\" — we cannot decompose 38% into contamination vs capability improvement\\n\\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\\n- Framing: aggressive — \\\"the field's standard validation approach is fundamentally mismatched for item-level detection\\\"\\n\\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\\n\\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\\n2. **DIF items = discriminative signal carriers**: DIF removal causes significantly MORE ranking disruption than random removal (z=-8 to -49σ, 21/21 conditions). DIF items carry 1.09× cross-cohort accuracy swing vs 0.96× for stable items — they concentrate the information that differentiates model generations.\\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \\\"find bad items and remove\\\" but \\\"understand what changed and why.\\\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\\n4. **Cross-benchmark validation — DIF captures capability, not contamination**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005; partial r=−0.385 controlling accuracy; permutation p=0.014). Contaminated models (high GSM8K-GSM1K gap: Phi, Gemma families) perform WORSE on DIF items. DIF captures genuine capability-discriminative items that contamination cannot fake — contamination produces shallow performance gains concentrated on non-DIF items. N=33 matched models, leave-one-out robust (min |r|=0.374).\\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_004 Step 3 (r=−0.478, p=0.005, 33 models)\\n- Growing Pains互补: \\\"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\\\" — mutual value positioning\\n- Caveats (→ limitations): super-family analysis limited to N≥20 families; GSM1K validation N=33 (CI wide); contamination gap is proxy, not ground truth\\n\\n## Story Spine\\n\\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \\\"Model B outperforms Model A on MMLU,\\\" we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.\\n\\n**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\\n\\n**What we find**: Three discoveries, each a contribution:\\n\\n1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.\\n\\n2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.\\n\\n3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.\\n\\n4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K confirms: DIF flags anti-correlate with contamination (r=−0.478, p=0.005) — contaminated models can't fake performance on DIF items, which capture genuine capability differences. DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.\\n\\n**Headline result**: \\\"Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF flags anti-correlate with contamination (r=−0.478, p=0.005): DIF captures genuine capability-discriminative items that contamination cannot replicate. We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000).\\\"\\n\\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\\n\\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\\n\\n## Venue Fit\\n\\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\\n- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 38% instability, (2) the ground truth meta-critique affecting the field, (3) the semi-synthetic framework. Frame as \\\"bringing mature psychometric tools to characterize an urgent ML evaluation problem.\\\"\\n\\n## Anticipated Reviewer Concerns (updated for pivot)\\n\\n1. **\\\"38% could just mean models got better\\\"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.\\n\\n2. **\\\"Ground truth critique is obvious — of course web labels don't capture differential effects\\\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\\n\\n3. **\\\"Semi-synthetic injection is artificial\\\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\\n\\n4. **\\\"DIF power is only sufficient for large effects\\\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\\n\\n5. **\\\"Only validated on MMLU\\\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\\n\\n6. **\\\"Higher methods (MIMIC, propensity-score) could solve the confounding\\\"** — Acknowledged as future work. We frame our three-attempt negative results as \\\"empirical observation\\\" that motivates these directions, not as impossibility.\\n\\n## Dropped from Original Framing\\n\\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\\n- **Detection as primary contribution**: Pivoted from \\\"we detect contamination\\\" to \\\"we characterize benchmark properties.\\\"\\n\", \"total_chars\": 11796, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c70bd4c-85d7-4018-8d37-7099716900ab",
  "isSidechain": true,
  "promptId": "27741ca6-31a4-40a5-9308-cb23e7795590",
  "agentId": "a0cd16afcb8320959",
  "type": "user",
  "uuid": "fe40845b-6d99-486b-b38a-4f878337cc98",
  "sourceToolAssistantUUID": "9c70bd4c-85d7-4018-8d37-7099716900ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T02:00:42.977Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01P2n3BwBEKEjyFDJaa7GiuK`</summary>

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
  "parentUuid": "fe40845b-6d99-486b-b38a-4f878337cc98",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtVuKyZDUsjP1qZn98g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4c30523-e8c8-462b-9cd1-a549b007a68a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hE7YWsBHXGxuQJrQWZZJm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 15671,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1296
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 15671,
          "cache_creation_input_tokens": 1296,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1296,
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

_source line 12 · 2026-05-21T02:00:42.999Z_

<details><summary>↩ Tool result · `toolu_01P2n3BwBEKEjyFDJaa7GiuK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml\", \"content\": \"categories:\\n- key: contamination_detection\\n  name: Benchmark Contamination Detection\\n  narrative: Methods for detecting training data contamination in LLM benchmarks,\\n    including RL-robust approaches\\n- key: irt_equating\\n  name: IRT Methodology & Equating\\n  narrative: Item Response Theory models, calibration, equating, and their application\\n    to LLM evaluation\\n- key: benchmark_design\\n  name: Dynamic Benchmark Design\\n  narrative: Approaches for creating contamination-resistant or self-updating benchmarks\\n- key: dif_methodology\\n  name: DIF Statistical Methods\\n  narrative: Differential Item Functioning detection methods, power analysis, and\\n    small-sample strategies\\n- key: item_generation\\n  name: Automated Item Generation\\n  narrative: LLM-based test item generation with difficulty control and psychometric\\n    validation\\nmeta:\\n  last_updated: '2026-05-21T01:40:38.004Z'\\n  total_papers: 16\\npapers:\\n  belzak2020smallsample:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Belzak, W.\\n    bibtex_key: belzak2020smallsample\\n    category: dif_methodology\\n    doi: ''\\n    relevance: Parsimonious logistic regression with sum scores outperforms complex\\n      IRT models for DIF detection in small samples; directly applicable to our N=50-80\\n      model cohorts\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Testing Differential Item Functioning in Small Samples\\n    url: ''\\n    venue: Multivariate Behavioral Research\\n    verified: false\\n    year: 2020\\n  hardy2026scalability:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Hardy, M.\\n    bibtex_key: hardy2026scalability\\n    category: irt_equating\\n    doi: ''\\n    relevance: Nonparametric signed isotonic R2 scalability coefficients outperform\\n      IRT item diagnostics; lightweight pre-filter for item quality before our parametric\\n      calibration\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients\\n    url: https://arxiv.org/abs/2603.24999\\n    venue: arXiv\\n    verified: false\\n    year: 2026\\n  kim2019fpc:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Kim, S.\\n    - Kolen, M.\\n    bibtex_key: kim2019fpc\\n    category: irt_equating\\n    doi: ''\\n    relevance: Fixed-parameter calibration requires only N>=200 vs N>=500 for full\\n      calibration; core methodology for our bifactor IRT equating with anchor items\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data\\n    url: ''\\n    venue: Applied Measurement in Education\\n    verified: false\\n    year: 2019\\n  liang2026dvd:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Liang, R.\\n    bibtex_key: liang2026dvd\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Detects variant contamination via generation variance (AUC 0.73-0.74\\n      vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under\\n      RL training\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'DVD: Detection via Variance of Generation Distribution for Variant Contamination'\\n    url: https://arxiv.org/abs/2601.04895\\n    venue: arXiv\\n    verified: true\\n    year: 2026\\n  polo2026growingpains:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Polo, F.\\n    bibtex_key: polo2026growingpains\\n    category: irt_equating\\n    doi: ''\\n    relevance: Uses multidimensional IRT with fixed-parameter calibration and 100\\n      anchor items for extensible evaluation (rho>=0.9); addresses score comparability\\n      but NOT contamination detection or item regeneration\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter\\n      Calibration'\\n    url: ''\\n    venue: arXiv\\n    verified: false\\n    year: 2026\\n  polo2026psnirt:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Polo, F.\\n    bibtex_key: polo2026psnirt\\n    category: irt_equating\\n    doi: ''\\n    relevance: PSN-IRT analyzes benchmark quality via 4PL IRT; provides published\\n      IRT parameters for MMLU we can use in semi-synthetic validation\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item\\n      Response Theory\\n    url: ''\\n    venue: AAAI 2026\\n    verified: false\\n    year: 2026\\n  tao2026selfcritique:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Tao, Y.\\n    bibtex_key: tao2026selfcritique\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse\\n      detection, but remains individual-model-level; our DIF is group-level and complementary\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: Detecting Data Contamination from Reinforcement Learning Post-training\\n      for Large Language Models\\n    url: https://arxiv.org/abs/2510.09259\\n    venue: ICLR 2026\\n    verified: true\\n    year: 2026\\n  wang2026fragility:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Wang, H.\\n    - Li, H.\\n    - Ko, B.\\n    - Zhang, H.\\n    bibtex_key: wang2026fragility\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Proves GRPO/PPO RL training conceals contamination signals (14-20pp\\n      AUROC degradation), motivating our DIF-based approach which operates on behavioral\\n      patterns immune to NLL smoothing\\n    role: foundation\\n    semantic_scholar_id: 9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3\\n    title: On The Fragility of Benchmark Contamination Detection in Reasoning Models\\n    url: https://arxiv.org/abs/2510.02386\\n    venue: ICLR 2026\\n    verified: true\\n    year: 2026\\n  white2025livebench:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - White, C.\\n    bibtex_key: white2025livebench\\n    category: benchmark_design\\n    doi: ''\\n    relevance: Monthly-updated contamination-free benchmark with objective scoring;\\n      no difficulty calibration or psychometric equivalence across updates\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'LiveBench: A Challenging, Contamination-Free LLM Benchmark'\\n    url: ''\\n    venue: ICLR 2025\\n    verified: false\\n    year: 2025\\n  zhang2024gsm1k:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Zhang, H.\\n    bibtex_key: zhang2024gsm1k\\n    category: contamination_detection\\n    doi: ''\\n    relevance: GSM1K documents 10-13% average accuracy drops from contamination; provides\\n      ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4\\n      logits) critical for our DIF power analysis\\n    role: foundation\\n    semantic_scholar_id: ef62f95c16f668f031d649799cbd79081c6d2b0f\\n    title: A Careful Examination of Large Language Model Performance on Grade School\\n      Arithmetic\\n    url: https://arxiv.org/abs/2405.00332\\n    venue: arXiv\\n    verified: true\\n    year: 2024\\n  li2024contamination:\\n    title: An Open-Source Data Contamination Report for Large Language Models\\n    authors:\\n    - Li, Y.\\n    - Guo, Y.\\n    - Guerin, F.\\n    - Lin, C.\\n    year: 2024\\n    venue: Findings of EMNLP 2024\\n    url: https://aclanthology.org/2024.findings-emnlp.30/\\n    doi: 10.18653/v1/2024.findings-emnlp.30\\n    bibtex_key: li2024contamination\\n    category: contamination_detection\\n    role: foundation\\n    relevance: Provides web-overlap contamination labels for MMLU and other benchmarks\\n      via Common Crawl matching; primary ground-truth comparison for our DIF-based\\n      contamination detection\\n    abstract: ''\\n    semantic_scholar_id: 32e11cf020021c225782a3b77b5cfed4ae8e14a0\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  shi2024mink:\\n    title: Detecting Pretraining Data from Large Language Models\\n    authors:\\n    - Shi, W.\\n    - Ajith, A.\\n    - Xia, M.\\n    - Huang, Y.\\n    - Liu, D.\\n    - Blevins, T.\\n    - Chen, D.\\n    - Zettlemoyer, L.\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2310.16789\\n    doi: ''\\n    bibtex_key: shi2024mink\\n    category: contamination_detection\\n    role: foundation\\n    relevance: Introduces Min-K% Prob method and WikiMIA benchmark for pretraining\\n      data detection; key baseline whose limitations under RL training motivate our\\n      DIF-based alternative\\n    abstract: ''\\n    semantic_scholar_id: 3422d5e0cdfdc935d6a84a1e3d3f96659265fe3a\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  balloccu2024leak:\\n    title: 'Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in\\n      Closed-Source LLMs'\\n    authors:\\n    - Balloccu, S.\\n    - Schmidtova, P.\\n    - Lango, M.\\n    - Dusek, O.\\n    year: 2024\\n    venue: EACL 2024\\n    url: https://arxiv.org/abs/2402.03927\\n    doi: 10.18653/v1/2024.eacl-long.5\\n    bibtex_key: balloccu2024leak\\n    category: contamination_detection\\n    role: foundation\\n    relevance: Systematic survey of data leakage in closed-source LLMs covering 255\\n      papers and 263 benchmarks; establishes scope of contamination problem motivating\\n      our detection approach\\n    abstract: ''\\n    semantic_scholar_id: 798feda076ad710df65d509a7884bd15937c8056\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  dekoninck2024constat:\\n    title: 'ConStat: Performance-Based Contamination Detection in Large Language Models'\\n    authors:\\n    - Dekoninck, J.\\n    - Mueller, M. N.\\n    - Vechev, M.\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: https://arxiv.org/abs/2405.16281\\n    doi: ''\\n    bibtex_key: dekoninck2024constat\\n    category: contamination_detection\\n    role: direct-competitor\\n    relevance: Performance-based contamination detection via perturbation analysis;\\n      closest methodological parallel to our DIF approach in using behavioral patterns\\n      rather than memorization signals\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  golchin2024timetravel:\\n    title: 'Time Travel in LLMs: Tracing Data Contamination in Large Language Models'\\n    authors:\\n    - Golchin, S.\\n    - Surdeanu, M.\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2308.08493\\n    doi: ''\\n    bibtex_key: golchin2024timetravel\\n    category: contamination_detection\\n    role: method-component\\n    relevance: Instance-level contamination detection via guided completion prompts;\\n      baseline approach for individual-item detection that our group-level DIF method\\n      extends\\n    abstract: ''\\n    semantic_scholar_id: d6d0fd994f37b630f35945736b5e1bb198148404\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  zhang2024minkpp:\\n    title: 'Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large\\n      Language Models'\\n    authors:\\n    - Zhang, J.\\n    - Sun, J.\\n    - Yeats, E.\\n    - Ouyang, Y.\\n    - Kuo, M.\\n    - Zhang, J.\\n    - Yang, H.\\n    - Li, H.\\n    year: 2024\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2404.02936\\n    doi: ''\\n    bibtex_key: zhang2024minkpp\\n    category: contamination_detection\\n    role: direct-competitor\\n    relevance: Improves Min-K% with vocabulary-normalized token probabilities; key\\n      baseline whose AUC degrades to 0.43-0.68 on RL-trained models, motivating our\\n      DIF-based alternative\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n\", \"total_chars\": 11927, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4c30523-e8c8-462b-9cd1-a549b007a68a",
  "isSidechain": true,
  "promptId": "27741ca6-31a4-40a5-9308-cb23e7795590",
  "agentId": "a0cd16afcb8320959",
  "type": "user",
  "uuid": "204680e2-29f8-404b-8f99-efe71e1bbfdd",
  "sourceToolAssistantUUID": "b4c30523-e8c8-462b-9cd1-a549b007a68a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T02:00:47.108Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JrvuhBEczvT9arkddmADtu`</summary>

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
  "parentUuid": "204680e2-29f8-404b-8f99-efe71e1bbfdd",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtWGK2ze7iNLt5hrWZL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b57c14e-7ff6-41fb-9b08-854be86c398a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnRDdTNsG8Q8sLkNf8jpt5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9320,
      "cache_read_input_tokens": 16967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9320,
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

_source line 14 · 2026-05-21T02:00:47.121Z_

<details><summary>↩ Tool result · `toolu_01JrvuhBEczvT9arkddmADtu`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b57c14e-7ff6-41fb-9b08-854be86c398a",
  "isSidechain": true,
  "promptId": "27741ca6-31a4-40a5-9308-cb23e7795590",
  "agentId": "a0cd16afcb8320959",
  "type": "user",
  "uuid": "aef4eda4-bdcf-4e41-b28e-b3c71624104e",
  "sourceToolAssistantUUID": "9b57c14e-7ff6-41fb-9b08-854be86c398a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T02:00:47.340Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WK4BC4C1AHFudH4m5tYHxD`</summary>

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
  "parentUuid": "aef4eda4-bdcf-4e41-b28e-b3c71624104e",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtWGK2ze7iNLt5hrWZL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c929123c-b108-46f6-9305-a011c1bca967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnRDdTNsG8Q8sLkNf8jpt5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9320,
      "cache_read_input_tokens": 16967,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9320
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 16967,
          "cache_creation_input_tokens": 9320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9320,
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

_source line 16 · 2026-05-21T02:00:47.350Z_

<details><summary>↩ Tool result · `toolu_01WK4BC4C1AHFudH4m5tYHxD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/memory.md\", \"content\": \"## MVP 验证关键经验 (2026-05-20)\\n\\n### D001 决策：ETS C 分类 > p-value 检验\\n- **p-value based DIF 检测在 200-item benchmark 上严重 underpowered**：BH 校正后 TPR 仅 0.04-0.07（N=50, δ=1.0）\\n- **ETS C 分类（|Δ_MH|≥1.5 + 显著性）是可行的替代**：TPR=0.68-0.85 at N≥80, δ≥1.4\\n- **AUC 一直很好（0.91-0.96）**\\n\\n### 关键操作参数\\n- N≥80/group 最低要求，N≥100 显著改善\\n- δ≥1.4 logits 可靠检测区间\\n- MH 5 层 quantile + ETS C 阈值是最佳组合\\n- Subject ≥200 items 才有足够 matching precision（<100 items baseline FPR 膨胀至 ~56%）\\n\\n## D006: plan_011 Semi-Synthetic 验证成功 ✅\\n\\n### DIF 检测差异性污染有效\\n- **External MH**: temporal ΔTPR=+0.674 (0.326→1.000), FPR 恒定 0.314\\n- **Matching variable contamination**: 20% items 注入时 standard MH FPR 0.298→0.616, anchor/external 免疫\\n- **Li et al. enrichment≈1.0 原因**: web-overlap = 全局性污染，不产生 DIF\\n\\n## D007-D010: 降低 FPR 路线全部穷尽 ⚠️\\n\\n### plan_012 θ-Conditioning 失败\\n- logit θ 与 total score 相关性 0.9986 → 单维 θ 分层 ≡ 总分分层\\n\\n### plan_014 Within-Subject 前置检查：C% = 38.1% (>25%)\\n- 5 个高 C% subjects 的 within-subject temporal C% 均 >25%（31-45%）\\n- Within vs cross-subject matching 差异仅 -2.4pp → 信号对 matching 不敏感\\n- **结论**：temporal DIF 渗透到每个 subject 内部，不是 between-subject 能力差异的伪影\\n- Bifactor 方向因此否定（D010）\\n\\n### plan_013 Q3 局部独立性：温和但存在\\n- Within-subject mean Q3 = 0.009（低于 0.20 阈值）\\n- 但 11.3% within-subject pairs |Q3|>0.20（vs 2.2% cross-subject，5x）\\n- 最严重: moral_scenarios 34.2%, world_religions 18%, marketing 17.5%\\n- 不太可能单独解释 31% FPR\\n\\n### plan_016 Within-Subject Semi-Synthetic：DIF 在 subject 内也有效 ✅\\n- Cross-subject matching FPR 完全稳定（ΔFPR=0.000），4/5 subjects ΔTPR>0.3\\n- Within-subject matching FPR 膨胀 +0.067 to +0.281（matching variable 包含注入 items）\\n- **结论**：within-subject 38% C% 是真实 temporal DIF，方法论有效\\n\\n### 综合推导：31% temporal FPR 不是 artifact\\n证伪链完整：1D θ 无效 → within-subject 仍高 → bifactor 否定 → Q3 不是主因 → **这是 genuine temporal DIF**（2023→2024 模型在特定 items 上的真实差异性表现变化）。DIF 方法有效但无法区分 contamination-DIF 和 capability-DIF。\\n\\n## D012: plan_017 Downstream Impact — DIF Items ≠ 噪声 ⚠️\\n\\n### Hypothesis 被证伪但发现更有价值\\n- **假设**: 移除 DIF items → 排名更稳定 → DIF 标记了 problematic items\\n- **实际**: DIF 移除造成 **更大** 排名扰动（z = -8 to -49σ, 21/21 条件）\\n- DIF items 是浓缩的差异化信息载体，不是噪声\\n\\n### 关键数字\\n- Full vs stable-only: ρ = 0.996-0.999（排名本身极鲁棒）\\n- DIF items 跨代准确率变化 = full benchmark 的 1.09×, stable = 0.96×\\n- Top beneficiaries: phi-3, llama-3 衍生（+700-850 rank positions）\\n- Top hurt: mistral merge/slerp 模型（-400 to -587 rank positions）\\n\\n### 对论文的启示\\n- DIF items 不是\\\"要清洗的坏题\\\"——是\\\"揭示模型代际差异的诊断工具\\\"\\n- 支持 characterization narrative > cleaning narrative\\n- \\\"Stable-only benchmark\\\" 不是\\\"更好的 benchmark\\\"，而是\\\"不同视角的 benchmark\\\"\\n\\n## plan_004: GSM8K Cross-Benchmark Validation (2026-05-21) 🔑\\n\\n### Step 1: GSM8K Temporal DIF 跨 benchmark 泛化 ✅\\n- GSM8K standard C% = 18.9%（MMLU 31.3%，同一量级）\\n- Sanity check 0.3%（通过）\\n- External matching C% = 47.4%——**非 contamination absorption**，是 construct validity gap（external benchmarks 测不同能力，控制了这些能力后 GSM8K item 行为差异更大）\\n- Standard vs external Spearman ρ = 0.926（高度一致）\\n\\n### Step 2: GSM8K Semi-Synthetic 验证 ✅\\n- Standard ΔTPR = +0.818 at p=1.0（MMLU +0.508，GSM8K 更强）\\n- External ΔTPR = +0.517\\n- GSM8K 的 DIF 对差异性污染更敏感（单域 benchmark, items 更同质）\\n\\n### Step 3: GSM1K Contamination Gap × DIF Correlation — 方向反转 ❌→🔑\\n- **r = −0.478 (p=0.005)**：contaminated 模型在 DIF-C items 上更差，非更好\\n- Partial r = −0.385 控制整体准确率后仍显著\\n- Permutation p = 0.014，robust to leave-one-out\\n- 171/249 DIF-C items α_MH < 1 → favor focal (2024) models（捕获真实代际能力提升）\\n- 78/249 DIF-C items α_MH > 1 → favor reference (2023) models\\n\\n### Step 3 核心洞察\\n- **DIF ⊥ contamination**：DIF 捕捉的 measurement anomalies 与 contamination 正交\\n- 171 个 focal-favoring DIF-C items 捕获真实代际能力提升，但 contaminated 模型在这些 items 上反而更差（r=−0.347, p=0.048）——contamination 的\\\"浅层\\\"boost 无法泛化到区分真实能力的题目\\n- **这是 characterization narrative 的强 evidence**：DIF 不标记\\\"被污染的 items\\\"，标记的是\\\"不同模型代际间行为模式不一致的 items\\\"\\n- 与 Xu et al. (2024) GSM1K 互补——他们检测 contamination，我们检测 construct-level measurement anomalies\\n\\n### α_MH 方向约定（Reviewer 修正 2026-05-21）\\n- α_MH > 1 → item 对 reference group 更容易\\n- α_MH < 1 → item 对 focal group 更容易\\n- 在 temporal cohort 中：reference = 2023, focal = 2024\\n\\n## 数据源 (2026-05-20)\\n\\n### METABENCH (Kipnis et al., ICLR 2025) ⭐\\n- GitHub: https://github.com/adkipnis/metabench\\n- Zenodo: https://zenodo.org/records/12819251 (620MB)\\n- MMLU 12,508 items, 5,219 模型\\n\\n### D002: preproc.rds diff/disc 是 CTT 不是 IRT\\n- diff = 0.75 × p_correct, disc = rpbis\\n- 实际 IRT 在 crossvalidate.R 用 mirt::mirt() slope-intercept\\n\\n### Li et al. (EMNLP 2024) Proxy Ground Truth\\n- 9,229/12,508 items 有标注（73.8%）\\n- clean 60.5% / input_and_label 33.0% / input_only 6.5%\\n- Web overlap proxy，非训练数据精确标签——全局性污染，不适合 DIF 验证\\n\", \"total_chars\": 4457, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c929123c-b108-46f6-9305-a011c1bca967",
  "isSidechain": true,
  "promptId": "27741ca6-31a4-40a5-9308-cb23e7795590",
  "agentId": "a0cd16afcb8320959",
  "type": "user",
  "uuid": "a395f344-562c-4862-91ff-5f3a2f968223",
  "sourceToolAssistantUUID": "c929123c-b108-46f6-9305-a011c1bca967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-21T02:00:49.424Z_

Now let me check for the actual paper draft and any additional artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a395f344-562c-4862-91ff-5f3a2f968223",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtWauEFYHHix98c6aiw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fe5745f-c520-4816-aae0-5c4ff8773194",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6XotuTYBbt9GAwmD35YgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3063,
      "cache_read_input_tokens": 26287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3063,
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

_source line 18 · 2026-05-21T02:00:51.990Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017QqzMWi5sdGfJySX9bGSMZ`</summary>

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
  "parentUuid": "0fe5745f-c520-4816-aae0-5c4ff8773194",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtWauEFYHHix98c6aiw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cca86011-e16f-4cd7-8f9e-4eb2e2e6b1bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6XotuTYBbt9GAwmD35YgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3063,
      "cache_read_input_tokens": 26287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3063,
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

_source line 19 · 2026-05-21T02:00:52.017Z_

<details><summary>↩ Tool result · `toolu_017QqzMWi5sdGfJySX9bGSMZ`</summary>

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
  "parentUuid": "cca86011-e16f-4cd7-8f9e-4eb2e2e6b1bc",
  "isSidechain": true,
  "promptId": "27741ca6-31a4-40a5-9308-cb23e7795590",
  "agentId": "a0cd16afcb8320959",
  "type": "user",
  "uuid": "b670a32a-c265-4c6c-b519-409a9438369c",
  "sourceToolAssistantUUID": "cca86011-e16f-4cd7-8f9e-4eb2e2e6b1bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T02:00:52.839Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JxBwbkiC3xMfU3TZfuxr52`</summary>

```json
{
  "pattern": "**/writing_plan*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b670a32a-c265-4c6c-b519-409a9438369c",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtWauEFYHHix98c6aiw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37712334-d63d-4569-b932-d14b69cd9a5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6XotuTYBbt9GAwmD35YgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3063,
      "cache_read_input_tokens": 26287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3063,
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

_source line 21 · 2026-05-21T02:00:52.867Z_

<details><summary>↩ Tool result · `toolu_01JxBwbkiC3xMfU3TZfuxr52`</summary>

```text
writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37712334-d63d-4569-b932-d14b69cd9a5c",
  "isSidechain": true,
  "promptId": "27741ca6-31a4-40a5-9308-cb23e7795590",
  "agentId": "a0cd16afcb8320959",
  "type": "user",
  "uuid": "e3410ab4-1a71-45de-a736-c01e5c066e08",
  "sourceToolAssistantUUID": "37712334-d63d-4569-b932-d14b69cd9a5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T02:00:53.651Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019WibuwegadJjrszeTxRcSa`</summary>

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
  "parentUuid": "e3410ab4-1a71-45de-a736-c01e5c066e08",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtWauEFYHHix98c6aiw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5a80ba1-37fb-471a-a182-b0ade035ef74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6XotuTYBbt9GAwmD35YgE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3063,
      "cache_read_input_tokens": 26287,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3063
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 26287,
          "cache_creation_input_tokens": 3063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3063,
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

_source line 23 · 2026-05-21T02:00:53.674Z_

<details><summary>↩ Tool result · `toolu_019WibuwegadJjrszeTxRcSa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/decisions.yaml\", \"content\": \"_next_id: 15\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:50 UTC\\n  summary: MVP DIF 检测采用 ETS C 分类（效应量+显著性双阈值）替代 BH 校正 p 值作为主判定标准\\n  rationale: Monte Carlo 模拟显示 BH 校正在 200 items 场景下将 TPR 压缩 40-60%，所有核心条件均 FAIL/GRAY。但\\n    ETS C 分类（|Δ_MH|≥1.5 + 显著性，教育测量 gold standard）在 N≥80, δ≥1.4 时 TPR=0.72-0.85, FPR<0.05，满足\\n    pass criteria。ETS C 是 DIF 领域标准实践（Holland & Thayer 1988），使用效应量阈值比纯 p 值更稳健。操作点 N≥80,\\n    δ≥1.4 与 GSM1K 文档的重度污染效应量吻合。小效应由 ensemble 其他信号覆盖。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'BH-corrected: all FAIL/GRAY; ETS C: PASS at N≥80,δ≥1.4 (TPR=0.72-0.85,\\n      FPR<0.05)'\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:31 UTC\\n  summary: MVP 通过：DIF+ETS C 在 N≥80,δ≥1.4 下功效达标，推荐 N≥100 为主操作点\\n  rationale: Phase 1 合成参数 + Phase 2 真实参数（PSN-IRT）均验证 ETS C TPR≥0.65 at N≥80,δ≥1.4。Phase\\n    2 比 Phase 1 降低 3-6pp 符合预期。N=80,δ=1.4 裕度仅 0.032，推荐 N≥100 为主 claim。数据源为 PSN-IRT\\n    而非 ROADMAP 指定的 METABENCH，research 阶段需用 METABENCH 补充验证。限制：δ<1.0 需 ensemble 其他信号。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'Phase 1 conditional pass: ETS C TPR=0.72-0.85 at N≥80,δ≥1.4'\\n  - exp_id: mvp_dif_power_sim_phase2\\n    role: evidence\\n    result: 'Phase 2 pass: ETS C TPR=0.68-0.80 at N≥80,δ≥1.4 with real MMLU params'\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 20:49 UTC\\n  summary: 'Dream analysis (dream_20260520T194223): 6 confirmed actions from cross-tier\\n    synthesis, 2 new experiments added (plan_010/011), framing qualified'\\n  rationale: 'Dream scores met thresholds (best=4/6, median=3.5/6, worst=3/6). Cross-tier\\n    analysis identified 6 confirmed issues (≥2 tiers): (1) contamination-capability\\n    confound → within-family analysis added to plan_001; (2) RL evidence underpowered\\n    → bootstrap CIs + equivalence testing added to plan_002; (3) partial exploitation\\n    gap → power analysis added to plan_002; (4) ground truth circularity → plan_011\\n    semi-synthetic validation added; (5) related work thin → Paper Agent writing-phase\\n    task; (6) Growing Pains differentiation → Paper Agent task. Additionally: plan_010\\n    architecture-stratified DIF added as P1 proactive defense from worst-case; novelty\\n    claim qualified from \\\"first self-healing benchmark\\\" to \\\"psychometric monitoring\\n    framework\\\". Re-dream required before P0 approval.'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 21:14 UTC\\n  summary: plan_001 temporal cohort DIF 证伪（enrichment=0.96），根因是 impact vs DIF 混淆。批准\\n    matched-ability DIF 作为方法改进方向 1\\n  rationale: Temporal cohort MH-DIF 标记 31.3% items 为 ETS C，但 enrichment=0.96（clean\\n    和 contaminated 标记概率相同）—— DIF 检测的是系统性能力提升而非污染。Within-family (Llama-2 vs Llama-3)\\n    61.3% C 进一步证实。这是经典 impact vs DIF 混淆（Dream D2 预测过）。但 ability-quintile enrichment=1.19\\n    + FPR=2.7% 表明信号存在但弱。方向1 matched-ability temporal DIF 在 quintile 内做时间对比，是最快验证能力匹配能否放大信号的路径。方向2\\n    IRT equating 并行准备作为 fallback。\\n  related_experiments:\\n  - exp_id: plan_001_real_data_dif_mmlu\\n    role: evidence\\n    result: negative - temporal cohort enrichment 0.96, ability quintile enrichment\\n      1.19\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-20 21:24 UTC\\n  summary: 方向 1 (matched-ability DIF) 失败确认，所有 quintile enrichment 0.94-1.04。plan_011\\n    是唯一决定性实验\\n  rationale: Quintile 内 temporal DIF 仍 enrichment≈1.0，ability matching 未能分离污染信号。但\\n    Reviewer 指出关键洞察：Li et al. web-overlap 是全局性污染（Common Crawl 对所有模型可用），不应产生 group-specific\\n    DIF。enrichment≈1.0 可能是 ground truth 不匹配而非方法失败。plan_011 注入的是已知差异性污染（仅 focal group），是唯一能区分\\\"DIF\\n    不 work\\\"和\\\"ground truth 不对\\\"的实验。方向 2 (IRT θ-matching) 如果问题出在 ground truth 也无法解决。\\n  related_experiments:\\n  - exp_id: plan_001b_matched_ability_dif\\n    role: evidence\\n    result: negative - all quintiles enrichment 0.94-1.04\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-20 21:56 UTC\\n  summary: 'plan_011 positive: MH-DIF 检测差异性污染有效 (p=0.5 TPR=0.834, p=1.0 TPR=1.0)，但\\n    baseline FPR=31% 需 IRT θ-conditioning 降低。启动方向 2'\\n  rationale: Semi-synthetic validation 确认 DIF 能检测差异性污染（剂量-响应单调，Fisher p<1e-21）。plan_001/001b\\n    失败归因于 Li et al. web-overlap 是全局性标注，不产生 group-specific DIF。但 baseline FPR=31% (temporal)\\n    / 49% (ability) 意味着 DIF 是筛查工具（高召回、中等精度），不是确诊工具。Precision ~44% at p=1.0。两个推进方向：(1)\\n    IRT θ-conditioning 降低 baseline FPR (方向 2)，(2) Ensemble 信号 (Claim 2) 过滤假阳性——DIF\\n    高召回 + ConStat 高精度自然衔接。同时需 Yen's Q3 诊断局部独立性（审稿 WC4），局部依赖可能是 FPR 膨胀的部分原因。\\n  related_experiments:\\n  - exp_id: plan_011_semi_synthetic\\n    role: evidence\\n    result: positive - TPR 0.834 at p=0.5, 1.0 at p=1.0; but baseline FPR 0.314\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-20 21:58 UTC\\n  summary: 'Story pivot: semi-synthetic validation 作为核心效度证据，Li et al. enrichment≈1.0\\n    重新定位为\\\"全局 vs 差异性污染\\\"的发现。IRT θ-conditioning 继续（降 FPR），但不期望改善 Li enrichment'\\n  rationale: 'Agent 和 Reviewer 均指出：即使 IRT θ 完美控制能力，Li et al. web-overlap 仍是全局标注，enrichment\\n    仍≈1.0。plan_011 semi-synthetic (ΔTPR=+0.674, Fisher p<1e-42) 是 DIF 方法有效性的决定性证据。Li\\n    et al. enrichment≈1.0 不是方法失败，而是揭示了现有\\\"污染标注\\\"实际测量的是全局 web 曝光（所有模型共享），不是差异性训练数据包含。这是一个有价值的发现：DIF\\n    检测差异性污染，现有标签标注存在性污染，两者度量不同。Story: DIF 是差异性污染的高灵敏度筛查工具 + ensemble 提升精度 + 全局/差异性污染区分是方法论贡献。'\\n  related_experiments:\\n  - exp_id: plan_011_semi_synthetic\\n    role: evidence\\n    result: positive\\n  - exp_id: plan_001_real_data_dif_mmlu\\n    role: evidence\\n    result: negative - reinterpreted as ground truth mismatch\\n  - exp_id: plan_001b_matched_ability_dif\\n    role: evidence\\n    result: negative - reinterpreted as ground truth mismatch\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-20 22:12 UTC\\n  summary: 方向 2 (IRT θ-conditioning) 失败，1D 路线穷尽。plan_011 ability cohort TPR 修正（76%→21%，73%\\n    是能力混淆）。启动 plan_005 bifactor IRT 作为最后结构性改进\\n  rationale: logit(p) 与 total score 相关 0.9986，所有 θ 变体 FPR 31-35%。plan_011 ability\\n    cohort 在 θ 10/20-bin conditioning 下 TPR 从 76% 降到 21%（p=0.5）——原 5-bin 分层不足以消除 Q1-2\\n    vs Q4-5 极端能力差异。DIF 面临 TPR-FPR tradeoff：temporal 高 TPR 但 FPR=31%，ability (proper)\\n    低 FPR=8% 但 TPR=21%。根因：temporal cohort 间差异是多维的（不同学科能力提升不均匀），1D θ 无法捕获。Bifactor\\n    model (general + 57 subject factors) 是唯一能吸收学科级差异的结构性方法。已尝试 2 种不同类型改进方向，bifactor\\n    是第 3 种。计算量大（5227×12508×58 factors），可能需要服务器。\\n  related_experiments:\\n  - exp_id: plan_012_irt_theta_conditioning\\n    role: evidence\\n    result: negative - temporal FPR stuck at 31%, ability TPR corrected to 21%\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-20 22:17 UTC\\n  summary: 'Dream #2 分析：best=3/6, median=3-4/6, worst=3/6。跨档一致：impact-vs-DIF confound\\n    为首要问题，bifactor 是正确方向。新发现：ensemble 不优于 DIF alone、SIBTEST/MIMIC 未尝试、detection trilemma\\n    概念'\\n  rationale: 三档审稿一致认为 within-family confound (42-62% overlap) 是最致命问题——没有 bifactor\\n    分离学科级能力差异，DIF flags 的可解释性无法建立。worst case 新增 SIBTEST/MIMIC 作为 established impact-vs-DIF\\n    solutions 的替代方案需要考虑。median 指出 ensemble AUROC (0.72) 低于 DIF alone (0.76)，Claim\\n    2 需要重新评估。worst case 提出 detection trilemma (IRT fit ↔ power ↔ confound control)\\n    作为潜在概念贡献。行动：(1) 优先完成 bifactor，(2) 考虑 SIBTEST/MIMIC 作为备选，(3) 推迟 ensemble 设计到 bifactor\\n    结果出来后，(4) 补充 impact-vs-DIF 文献\\n  related_experiments:\\n  - exp_id: dream_20260520T205007\\n    role: dream_simulation\\n    result: best=3/6, median=3-4/6, worst=3/6\\n  depends_on:\\n  - D008\\n  - D007\\n  - D006\\n- id: D010\\n  date: 2026-05-20 22:29 UTC\\n  summary: 方向 3 (Bifactor) pre-check 否定：within-subject temporal C%=38.1% (range 31-45%)，高于\\n    overall 31%。Bifactor 移除的 between-subject variance 反而在压低 C%。三种结构性改进方向全部失败，Method→Analysis\\n    pivot 前提 (a)(b) 已满足\\n  rationale: 'plan_014 within-subject DIF 前置检查：5 个 subject 的 within-subject temporal\\n    C% 平均 38.1%，没有一个低于 30%。Cross-subject matching 仅 Δ=-2.4pp。这证明 temporal DIF 是 item-specific\\n    的真实差异（能力提升+污染+其他），不是 matching artifact。Bifactor 即使完美运行也无法降 FPR 到 15% 以下。决策链：D005(方向1失败)\\n    → D008(方向2失败) → D010(方向3 pre-mortem 证伪)。Oracle: plan_011 semi-synthetic ΔTPR=+0.508\\n    确认方法本身有效。Pivot 前提 (c) 待用户确认投稿目标调整。'\\n  related_experiments:\\n  - exp_id: plan_014_within_subject_dif\\n    role: pre-check\\n    result: within-subject C%=38.1%, bifactor not viable\\n  - exp_id: plan_011_semi_synthetic\\n    role: oracle\\n    result: ΔTPR=+0.508, method works for differential contamination\\n  depends_on:\\n  - D008\\n  - D009\\n  - D005\\n- id: D011\\n  date: 2026-05-20 23:23 UTC\\n  summary: Pivot 拍板：从\\\"DIF 检测方法\\\"转向\\\"LLM benchmark psychometric characterization + DIF\\n    methodology\\\"。Cross-subject matching ΔFPR=0.000 是方法论突破，31-38% temporal DIF 是实证发现。保持\\n    ICLR 2027 目标不降级\\n  rationale: 三种结构性改进全部穷尽（D005/D008/D010），oracle 确认方法有效（plan_011 ΔTPR=+0.508）。但 pivot\\n    不等于降级：(1) cross-subject matching ΔFPR=0.000 是干净的方法论贡献——解决了 matching variable contamination\\n    这个 MH-DIF 领域的实际问题；(2) 31-38% temporal DIF 是首次大规模量化 LLM benchmark item instability；(3)\\n    global vs differential contamination 区分是概念贡献；(4) semi-synthetic validation framework\\n    可独立复用；(5) detection trilemma 是 characterization 贡献。这些组合起来是 ICLR 级别的 empirical\\n    findings paper，不需要降到 findings track。用户批评\\\"等我点头\\\"正确——这是 PI 的决策责任。\\n  related_experiments:\\n  - exp_id: plan_016_within_subject_semi_synthetic\\n    role: final_validation\\n    result: cross-subject ΔFPR=0.000, 4/5 ΔTPR>0.3\\n  - exp_id: plan_014_within_subject_dif\\n    role: pre-check\\n    result: within-subject C%=38.1%\\n  - exp_id: plan_011_semi_synthetic\\n    role: oracle\\n    result: ΔTPR=+0.508\\n  depends_on:\\n  - D010\\n  - D009\\n  - D006\\n- id: D012\\n  date: 2026-05-20 23:28 UTC\\n  summary: Story 定稿：Candidate 1 (benchmark quality tool) + ground truth meta-critique\\n    + semi-synthetic infrastructure。降级 cross-subject matching 为 recommendation（非 breakthrough）。新增\\n    downstream impact 实验（移除 DIF items → ranking stability）作为 ICLR 关键补充\\n  rationale: Reviewer 评估：(1) 三候选中 Candidate 1 最自洽，(2) cross-subject matching 是 external\\n    matching 的自然推广非新方法（降级），(3) enrichment≈1.0 + semi-synthetic positive 证明现有污染 ground\\n    truth 自身有缺陷（meta-contribution），(4) \\\"so what?\\\" 缺口是 ICLR vs findings track 的分水岭——需\\n    downstream impact 实验回答。38% 与 domain specificity ρ=0.307 的关系必须在 limitations 诚实讨论。\\n  related_experiments:\\n  - exp_id: plan_014_within_subject_dif\\n    role: finding\\n    result: 38% temporal DIF\\n  - exp_id: plan_016_within_subject_semi_synthetic\\n    role: method\\n    result: cross-subject ΔFPR=0.000\\n  - exp_id: plan_001_real_data_dif_mmlu\\n    role: finding\\n    result: enrichment≈1.0 → ground truth meta-critique\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-21 00:06 UTC\\n  summary: plan_017 downstream impact negative 但 informative：DIF items 是浓缩差异化信号载体而非噪声。Claim\\n    4 从 placeholder \\\"remove for stability\\\" 转为 finding \\\"DIF as diagnostic lens\\\"。DIF\\n    items 移除造成更大排名扰动（21/21 条件显著），phi-3/llama-3 获益最多，mistral merge 被压制\\n  rationale: plan_017 全面证伪了\\\"移除 DIF items 改善排名稳定性\\\"的 hypothesis：(1) full vs stable-only\\n    ρ=0.996-0.999 说明排名本身极鲁棒，(2) DIF removal 扰动显著大于 random removal（z=-8 to -49σ），(3)\\n    DIF items 的跨代准确率变化是 full benchmark 的 1.09×。这意味着 DIF items 不是\\\"坏题\\\"而是\\\"模型代际差异的诊断标记\\\"。对\\n    paper narrative 的影响：从\\\"remove unstable items\\\"转向\\\"DIF as diagnostic lens for understanding\\n    model evolution\\\"。这个 negative result 比 positive 更有深度——\\\"keep these items, they tell\\n    you something\\\" 是更有价值的 benchmark design recommendation。\\n  related_experiments:\\n  - exp_id: plan_017_downstream_impact\\n    role: hypothesis_test\\n    result: negative - DIF items carry MORE discriminative signal, not less\\n  depends_on:\\n  - D012\\n  - D011\\n- id: D014\\n  date: 2026-05-21 01:25 UTC\\n  summary: 'plan_004 Step 3 GSM1K: |r|=0.478 显著但方向为负——DIF 不标记 contamination，而是标记 contamination\\n    无法到达的 capability-discriminative items'\\n  rationale: r=−0.478 (p=0.005), Spearman ρ=−0.403 (p=0.020), partial r=−0.385 (p=0.027\\n    控制 overall accuracy), permutation p=0.014, leave-one-out robust (min |r|=0.374)。N=33\\n    matched models。171 个 focal-favoring DIF-C items 驱动负相关 (r=−0.347, p=0.048)：contaminated\\n    models 在这些 genuine capability improvement items 上表现更差。这不支持 \\\"DIF = contamination\\n    detector\\\" 假设，但强力支撑 pivot 后 \\\"DIF as diagnostic lens\\\" 叙事：DIF 捕获的是真实能力差异，contamination\\n    产生的浅层提升无法到达这些 items。与 plan_017 (DIF items = discriminative signal carriers) 形成双重验证。不升级\\n    ICLR 为 \\\"validated method\\\"，但显著加强 characterization paper 的深度和跨 benchmark 证据。\\n  related_experiments:\\n  - exp_id: plan_004_gsm8k_cross_benchmark\\n    role: primary\\n    result: negative_but_informative\\n  - exp_id: plan_017_downstream_impact\\n    role: corroborating\\n    result: negative_but_informative\\n  depends_on:\\n  - D013\\n  - D011\\n\", \"total_chars\": 12255, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5a80ba1-37fb-471a-a182-b0ade035ef74",
  "isSidechain": true,
  "promptId": "27741ca6-31a4-40a5-9308-cb23e7795590",
  "agentId": "a0cd16afcb8320959",
  "type": "user",
  "uuid": "b2485174-94db-40e1-ad7c-51c3e139e47e",
  "sourceToolAssistantUUID": "c5a80ba1-37fb-471a-a182-b0ade035ef74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T02:00:57.326Z_

Let me read the most recent dream report (best case paper) to see the full paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2485174-94db-40e1-ad7c-51c3e139e47e",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtX3wfmbjKepDhc1GMp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c924df5c-f4fc-4e3f-ac38-7fb9aa67adc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXET55ydro88mcB6npNKfX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6999,
      "cache_read_input_tokens": 29350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6999,
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

_source line 25 · 2026-05-21T02:00:59.310Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QMXS1UDBETMeVPDKh8k9nW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c924df5c-f4fc-4e3f-ac38-7fb9aa67adc8",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtX3wfmbjKepDhc1GMp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "317e069f-9628-419f-ac23-f45200799b9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXET55ydro88mcB6npNKfX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6999,
      "cache_read_input_tokens": 29350,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6999
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 29350,
          "cache_creation_input_tokens": 6999,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6999,
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

_source line 26 · 2026-05-21T02:00:59.589Z_

<details><summary>↩ Tool result · `toolu_01QMXS1UDBETMeVPDKh8k9nW`</summary>

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
  "parentUuid": "317e069f-9628-419f-ac23-f45200799b9d",
  "isSidechain": true,
  "promptId": "27741ca6-31a4-40a5-9308-cb23e7795590",
  "agentId": "a0cd16afcb8320959",
  "type": "user",
  "uuid": "749baad9-5993-482b-a5a0-6668dfaacab1",
  "sourceToolAssistantUUID": "317e069f-9628-419f-ac23-f45200799b9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-21T02:01:02.524Z_

I now have comprehensive knowledge of the paper. Let me also check the worst-case dream review to calibrate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "749baad9-5993-482b-a5a0-6668dfaacab1",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtXV4XNcWK75Vz7w7DQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e02afc60-3c0d-4a6d-8a38-d1f50fa9a7a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ck9ov1RGJPs6t1s6qq3xWo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13575,
      "cache_read_input_tokens": 36349,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13575,
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

_source line 28 · 2026-05-21T02:01:05.816Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LrNtARrNzMsXyDiw7bGFyx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e02afc60-3c0d-4a6d-8a38-d1f50fa9a7a9",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtXV4XNcWK75Vz7w7DQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e39d9d44-cac4-438e-893c-137af4bf5069",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ck9ov1RGJPs6t1s6qq3xWo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13575,
      "cache_read_input_tokens": 36349,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13575,
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

_source line 29 · 2026-05-21T02:01:05.822Z_

<details><summary>↩ Tool result · `toolu_01LrNtARrNzMsXyDiw7bGFyx`</summary>

```text
1	\documentclass{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[margin=1in]{geometry}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{hyperref}
8	\usepackage{natbib}
9	\usepackage{xcolor}
10	\usepackage{multirow}
11	\usepackage{array}
12	\usepackage{tabularx}
13	
14	\title{Identifying Capability-Authentic Benchmark Items via Differential Item Functioning}
15	
16	\author{Anonymous}
17	
18	\date{}
19	
20	\begin{document}
21	\maketitle
22	
23	%==============================================================================
24	\begin{abstract}
25	%==============================================================================
26	Large language model benchmarks implicitly assume that items measure the same construct across model generations. We challenge this assumption by applying Differential Item Functioning (DIF) analysis---a classical psychometric technique---to the METABENCH response matrix (5,219 models $\times$ 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.
27	We find that 31.3\% of MMLU items are \emph{capability-sensitive}: they exhibit large DIF between 2023 and 2024-H1 model cohorts (ETS category C, $|\Delta_{\mathrm{MH}}|\ge1.5$). Rather than indicating benchmark pathology, these items concentrate the discriminative signal that differentiates model generations---their removal disrupts rankings significantly more than random removal ($z=-8$ to $-49\sigma$). Cross-benchmark validation on GSM8K confirms that DIF-flagged items \emph{anti-correlate} with contamination ($r=-0.478$, $p=0.005$, $N=33$): contaminated models perform worse on DIF items, indicating DIF captures genuine capability differences that memorization cannot replicate.
28	Downstream impact analysis reveals massive benchmark redundancy: removing all DIF items changes the Spearman rank correlation by only $\rho=0.997$, implying MMLU is roughly three times larger than necessary for stable rankings. We contribute a reusable semi-synthetic validation framework with cross-subject matching that eliminates false positive rate inflation ($\Delta\mathrm{FPR}=0.000$). We further report extensive negative results from twelve experiments---including bifactor IRT failure, underpowered RL robustness tests, and weak ensemble fusion---to map the operational boundaries of DIF in the LLM evaluation setting.
29	\end{abstract}
30	
31	%==============================================================================
32	\section{Introduction}
33	\label{sec:intro}
34	%==============================================================================
35	
36	When we declare that ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent construct measured under comparable conditions. In educational testing, this assumption is routinely audited via Differential Item Functioning (DIF) analysis, which detects items that behave differently across examinee subgroups after controlling for overall ability. If a math item is harder for one demographic group than another, conditional on equal math ability, the item exhibits DIF and threatens fair measurement.
37	
38	LLM benchmarks face an analogous threat. As model capabilities evolve rapidly across generations, benchmark items may shift in effective difficulty---not because the items changed, but because the relationship between model capability and item response changed. An item that once discriminated between strong and weak models may become trivially easy for all modern models, or conversely, an item that tested surface-level pattern matching may now require genuine reasoning from models that have moved beyond shallow heuristics.
39	
40	We apply Mantel-Haenszel (MH) DIF analysis to the METABENCH repository, analyzing 5,219 models across 12,508 MMLU items. Our central finding reframes the role of DIF in LLM evaluation: items flagged by DIF are not ``broken''---they are \emph{capability-authentic}. They are the items where genuine capability improvement manifests at the item level, and they concentrate the signal that distinguishes model generations.
41	
42	\paragraph{Contributions.}
43	\begin{enumerate}
44	    \item \textbf{Capability-sensitive item identification.} We show that 31.3\% of MMLU items exhibit large temporal DIF, and that this rate is robust to architecture stratification (decoder-only: 33.1\%), correlates with domain-level accuracy improvement ($\rho=0.307$, $p=0.02$), and cannot be attributed to statistical noise (random split: 0.18\%).
45	    \item \textbf{Cross-benchmark capability validation.} On GSM8K ($1{,}319$ items $\times$ $6{,}702$ models), DIF flags anti-correlate with the GSM1K contamination gap ($r=-0.478$, $p=0.005$). Contaminated models---those with inflated GSM8K scores relative to the held-out GSM1K---perform \emph{worse} on DIF items. DIF identifies items where genuine capability matters.
46	    \item \textbf{Measurement efficiency characterization.} Rank correlation remains $\rho\ge0.972$ even after replacing 50\% of items, revealing that MMLU is roughly $3\times$ larger than needed for stable rankings. DIF items form the informative core.
47	    \item \textbf{Semi-synthetic validation framework.} We introduce a $\Delta$TPR methodology with cross-subject matching ($\Delta$FPR$=0.000$), providing reusable calibration infrastructure for item-level detectors.
48	    \item \textbf{Comprehensive negative results.} We report twelve experiments including bifactor IRT failure, weak ensemble fusion, underpowered RL robustness, and unsuccessful item generation, mapping the operational boundaries of psychometric methods in LLM evaluation.
49	\end{enumerate}
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e39d9d44-cac4-438e-893c-137af4bf5069",
  "isSidechain": true,
  "promptId": "27741ca6-31a4-40a5-9308-cb23e7795590",
  "agentId": "a0cd16afcb8320959",
  "type": "user",
  "uuid": "757f6efa-ddf9-4803-b015-32e0812f756b",
  "sourceToolAssistantUUID": "e39d9d44-cac4-438e-893c-137af4bf5069",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T02:01:06.691Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018GCPaRsuvFgwjmtSxs8xwH`</summary>

```json
{
  "pattern": "**/dream_*/**/review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "757f6efa-ddf9-4803-b015-32e0812f756b",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtXV4XNcWK75Vz7w7DQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b670495-8ffb-41c9-9913-c380d4990b60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ck9ov1RGJPs6t1s6qq3xWo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13575,
      "cache_read_input_tokens": 36349,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13575
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 36349,
          "cache_creation_input_tokens": 13575,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13575,
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

_source line 31 · 2026-05-21T02:01:06.703Z_

<details><summary>↩ Tool result · `toolu_018GCPaRsuvFgwjmtSxs8xwH`</summary>

```text
artifacts/dream_reports/dream_20260520T194223/best/review_context.yaml
artifacts/dream_reports/dream_20260520T194223/logs/review_best.log
artifacts/dream_reports/dream_20260520T194223/median/review_context.yaml
artifacts/dream_reports/dream_20260520T194223/best/review_report.md
artifacts/dream_reports/dream_20260520T194223/median/review_report.md
artifacts/dream_reports/dream_20260520T194223/logs/review_median.log
artifacts/dream_reports/dream_20260520T194223/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T194223/worst/review_report.md
artifacts/dream_reports/dream_20260520T194223/logs/review_worst.log
artifacts/dream_reports/dream_20260520T205007/best/review_context.yaml
artifacts/dream_reports/dream_20260520T205007/best/review_report.md
artifacts/dream_reports/dream_20260520T205007/logs/review_best.log
artifacts/dream_reports/dream_20260520T205007/median/review_context.yaml
artifacts/dream_reports/dream_20260520T205007/median/review_report.md
artifacts/dream_reports/dream_20260520T205007/logs/review_median.log
artifacts/dream_reports/dream_20260520T205007/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T205007/worst/review_report.md
artifacts/dream_reports/dream_20260520T205007/logs/review_worst.log
artifacts/dream_reports/dream_20260521T012912/best/review_context.yaml
artifacts/dream_reports/dream_20260521T012912/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b670495-8ffb-41c9-9913-c380d4990b60",
  "isSidechain": true,
  "promptId": "27741ca6-31a4-40a5-9308-cb23e7795590",
  "agentId": "a0cd16afcb8320959",
  "type": "user",
  "uuid": "ce65c3d5-443a-4f20-9cc2-d29711080f0b",
  "sourceToolAssistantUUID": "4b670495-8ffb-41c9-9913-c380d4990b60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-21T02:02:45.458Z_

I now have a thorough understanding of the paper, its experimental trajectory, framing decisions, and the full manuscript. Let me now provide the review.

---

### R2 Independent Review: Novelty & Related Work

**Summary**

This paper applies Differential Item Functioning (DIF), a well-established psychometric technique, to the METABENCH response matrix (5,227 models x 12,508 MMLU items) and finds that 38% of items are functionally unstable across model generations. The paper makes four claims: temporal instability characterization, a meta-critique of web-overlap ground truth labels, a semi-synthetic validation framework with cross-subject matching, and a reframing of DIF items as diagnostic markers rather than noise. The paper is positioned as a characterization study rather than a detection method, and the pivot from "contamination detection" to "psychometric characterization" is visible in the careful hedging throughout. The scale of the analysis is impressive, the intellectual honesty about negative results is commendable, and the cross-benchmark GSM8K validation adds genuine depth, though several novelty and related work concerns merit discussion.

**Strengths**

- The application of DIF to LLM benchmarks at this scale (5,227 models x 12,508 items) is genuinely novel in scope. While DIF has been used in educational testing for 40+ years, no prior work has applied it to LLM evaluation at this magnitude, and the transfer is non-trivial because LLM "test-takers" violate many assumptions of classical psychometrics (independence, unidimensionality, fixed populations).

- The ground truth meta-critique (Claim 2) is the paper's strongest novelty contribution. The observation that web-overlap labels measure global exposure rather than differential contamination is methodologically important and underappreciated in the field. The empirical demonstration -- enrichment approximately 1.0 plus semi-synthetic confirmation of detection capability -- makes this concrete rather than merely philosophical. This affects the validation methodology of Min-K%, ConStat, and DVD simultaneously.

- The cross-subject matching innovation (delta-FPR = 0.000) is a clean, practical methodological contribution. The insight that matching on total score within the same subject contaminates the matching variable is subtle and well-demonstrated empirically. This is independently useful for anyone applying MH-DIF to structured multi-domain benchmarks.

- The "DIF as diagnostic lens" reframing (Claim 4) is well-supported by the convergence of two independent lines of evidence: (a) DIF item removal disrupts rankings more than random removal (z = -8 to -49 sigma), and (b) DIF flags anti-correlate with GSM1K contamination gaps (r = -0.478). This two-pronged validation is convincing for the characterization narrative.

- Intellectual honesty about rho = 0.307 (cannot decompose instability into contamination vs. capability) and the explicit framing as characterization rather than detection is appropriate and refreshing. The paper does not overclaim.

- Architecture stratification reducing C% from 31.3% to 22.1% transforms a potential fatal objection into a practical recommendation. This demonstrates methodological maturity.

- The sanity checks are well-designed: random-split C% = 0.18% vs. temporal C% = 31.3% is a 170x ratio that compellingly rules out statistical artifacts.

**Weaknesses**

- The core methodological contribution -- applying MH-DIF to a binary response matrix -- is a direct application of a 40-year-old technique with no algorithmic novelty. The ETS A/B/C classification is off-the-shelf. The paper's novelty rests entirely on (a) the empirical findings and (b) the meta-critique, not on methodological innovation. For a top ML venue targeting ~25% acceptance, this is a concern. The paper acknowledges this in its framing ("bringing mature psychometric tools to an urgent ML problem"), but reviewers at ICLR may weight novelty of method more heavily than novelty of application.

- The related work section omits several important lines of work that weaken the novelty claim:
  - **Measurement invariance / multi-group CFA**: The psychometric literature on measurement invariance (configural, metric, scalar) is the natural generalization of DIF to the latent variable framework. Meredith (1993) and subsequent work on measurement invariance testing via multi-group CFA is directly relevant -- DIF is essentially a test of scalar invariance at the item level. The paper should discuss why MH-DIF was chosen over these more general frameworks.
  - **MIMIC models (Multiple Indicators, Multiple Causes)**: The paper mentions MIMIC in passing (Section 5.3) as future work, but MIMIC models (Muthen, 1985; Woods, 2009) are a well-established alternative to MH for DIF detection that naturally handles continuous grouping variables and multiple covariates. Given the paper's own negative result with IRT theta-conditioning, MIMIC is not merely future work but a directly relevant alternative that should be discussed in related work.
  - **Propensity score matching for DIF**: Propensity score methods for DIF (e.g., Teresi et al., 2007) address exactly the impact-vs-DIF confounding that the paper struggles with throughout. This omission is notable given the paper's extended discussion of structural constraints.
  - **IRT-based DIF methods**: Lord's chi-square, Raju's method, and likelihood-ratio DIF tests are standard alternatives to MH that the related work does not discuss. The choice of MH over these should be justified.
  - **PSN-IRT (Polo et al., AAAI 2026)**: Listed in the literature map but absent from the paper. This work analyzes MMLU via 4PL IRT and provides published IRT parameters -- it is directly relevant as a concurrent effort applying psychometric methods to LLM benchmarks.

- The semi-synthetic validation framework (Claim 3), while useful, has a significant limitation that undermines its generalizability: the injection mechanism (flipping incorrect to correct responses) assumes contamination manifests as improved accuracy on specific items. Real contamination may produce more subtle effects -- shifted response distributions, changed confidence patterns, or memorized wrong answers. The paper acknowledges this briefly but underweights the concern. The framework validates DIF against a specific, simplified contamination mechanism; whether DIF detects real-world contamination patterns remains unproven.

- The 38% instability finding (Claim 1), while striking, has an interpretability problem the paper partially addresses but does not resolve. The rho = 0.307 correlation with accuracy improvement suggests a substantial fraction of "instability" is simply "models got better." The paper frames this honestly, but a reviewer could reasonably ask: if 38% instability is mostly capability improvement, is that really "instability" in a concerning sense, or just "progress"? The paper's own evidence (DIF items concentrate discriminative signal, anti-correlate with contamination) suggests these items are working correctly -- they differentiate model generations because models genuinely improved. This partially undermines the framing of "temporal comparability concern."

- The RL robustness analysis (N=13 reasoning-RL models, Appendix A) is underpowered by the paper's own admission. Presenting Jaccard = 0.88 and TOST p = 0.008 from 13 models as evidence of robustness is a stretch. The comparison to Min-K% (0.81 to 0.52) and ConStat (0.77 to 0.48) on the same small sample is not a fair comparison -- DIF operates at the group level and is inherently less sensitive to individual model additions, while per-model detectors are designed to evaluate individual models. The claim of "RL robustness" from this evidence is overclaimed relative to the data.

- The Cumulative Bayesian DIF section (5.3) introduces a new method (Bayesian DIF priors) that appears to be entirely simulated without validation on the actual METABENCH data. This section feels speculative and detached from the empirical contributions -- it proposes a future operational tool without demonstrating it works on the data at hand.

- Growing Pains (2024) comparison is insufficiently developed. The paper claims DIF "complements" Growing Pains by "detecting which anchor items are degrading," but does not empirically demonstrate this. Do any of Growing Pains' 100 anchor items show DIF? What is the C% among anchor items specifically? This would be a straightforward analysis that would strengthen the complementarity claim.

- The paper's positioning relative to ConStat is potentially unfair. ConStat operates at the model level (detecting whether a specific model is contaminated), while DIF operates at the item level (detecting whether an item functions differently across groups). Comparing their AUROCs (ConStat 0.73 vs. DIF's semi-synthetic performance) conflates different detection tasks. The "low correlation" (r = 0.21) between DIF flags and ConStat flags is expected from methods measuring different things -- this does not establish "orthogonal detection axes" so much as "different research questions."

**Questions for Authors**

- What is the C% among Growing Pains' specific anchor items? This would directly test the "complementary" positioning claim.

- The rho = 0.307 correlation between C% and accuracy improvement: if you partial out accuracy improvement, what fraction of the 38% instability remains? This would help decompose "capability improvement DIF" from "genuine measurement anomaly DIF."

- For the GSM1K anti-correlation (r = -0.478, N=33): how sensitive is this to the family matching procedure? The paper mentions leave-one-out robustness, but N=33 with leave-one-out is weak evidence. What happens with different family definitions?

- Why MH-DIF specifically rather than logistic regression DIF, which naturally accommodates continuous covariates and multiple grouping variables? Logistic regression DIF would have avoided the theta-conditioning failure mode (D008) by design.

- The paper reports architecture-stratified C% = 22.1% for decoder-only models. What is the C% for encoder-decoder models separately? If it is much higher, this would strengthen the architecture confounding narrative.

- The Bayesian DIF section assumes 200 new models per "administration." Is this realistic for benchmark maintenance? How many new models per quarter actually appear on METABENCH?

**Missing Related Work**

- **Measurement invariance literature**: Meredith (1993), Vandenberg & Lance (2000) -- the standard framework for testing whether measurement properties hold across groups. DIF is a special case; this connection should be made explicit.

- **MIMIC models for DIF**: Muthen (1985), Woods (2009) -- directly relevant alternative to MH-DIF that handles continuous covariates. The paper's own negative results with theta-conditioning suggest MIMIC would have been a better choice.

- **Propensity score matching for DIF**: Teresi et al. (2007) -- addresses impact-vs-DIF confounding, the paper's central methodological challenge.

- **PSN-IRT (Polo et al., AAAI 2026)**: Concurrent work applying IRT to MMLU quality analysis. Listed in the project's literature map but omitted from the paper.

- **Uysal et al. (2019) or similar work on DIF in computerized adaptive testing**: DIF in CAT settings is relevant because LLM benchmarks share properties with adaptive testing (item pools, varying test-taker populations over time).

- **Millsap & Everson (1993) on DIF methodology comparison**: Would provide context for the MH choice vs. alternatives.

- **Wang et al. (2026, ICLR) "On the Fragility of Benchmark Contamination Detection in Reasoning Models"**: Listed in the literature map as a foundation paper but not cited in the manuscript. This is directly relevant to the RL robustness discussion.

- **Tao et al. (2026, ICLR) "Detecting Data Contamination from Reinforcement Learning Post-training"**: Also in the literature map but absent from the paper. Directly relevant to the RL robustness claim.

- **Balloccu et al. (EACL 2024) "Leak, Cheat, Repeat"**: Systematic survey of contamination scope that would strengthen the motivation.

- **Hardy (2026) on scalability coefficients for benchmark items**: Concurrent work on nonparametric item quality diagnostics. Present in the literature map, absent from the paper.

**Novelty Score**: 2/4
The methodological novelty is low (off-the-shelf MH-DIF applied to a new domain). The novelty comes from the empirical findings (38% instability, ground truth meta-critique, cross-subject matching) and the reframing (DIF as diagnostic lens). The ground truth meta-critique is the most novel conceptual contribution. Cross-subject matching is a modest but useful innovation. The overall novelty is sufficient for a workshop paper or findings track but borderline for a top venue main track.

**Significance Score**: 3/4
The 38% instability finding, if it holds up, has significant implications for how the community interprets temporal benchmark comparisons. The ground truth meta-critique affects the validation methodology of multiple concurrent contamination detection efforts. The semi-synthetic framework is reusable infrastructure. The "DIF as diagnostic lens" reframing, supported by the GSM1K anti-correlation, provides a new perspective on benchmark item quality. The work would meaningfully change how benchmark maintainers think about item stability.

**Clarity Score**: 3/4
The paper is generally well-written. The DIF primer (Section 3.1) with "ML translation" is a good pedagogical choice. The characterization-vs-contamination distinction is clearly maintained throughout. The main weakness is structural: the paper tries to present too many findings (4 claims + architecture stratification + structural constraints + Bayesian DIF + RL robustness + cross-benchmark validation), giving each insufficient depth. The Future Work section (Section 7) is disproportionately long and includes preliminary results (ensemble fusion, item generation, graceful degradation) that feel like padding rather than forward-looking directions. Some tables (e.g., Table 5-9) would be better in appendices.

**Overall Score**: 4/6
The paper presents a solid empirical contribution -- the first large-scale DIF analysis of an LLM benchmark -- with genuinely interesting findings (38% instability, ground truth meta-critique, DIF anti-correlation with contamination). The semi-synthetic framework is useful infrastructure. However, the methodological novelty is limited (off-the-shelf MH-DIF), several important related works are missing, the RL robustness claim is underpowered, and the paper tries to cover too much ground at the expense of depth. The ground truth meta-critique and cross-benchmark validation are the strongest contributions and deserve more space. With a tighter focus, stronger related work coverage, and either removal or honest downsizing of the underpowered RL and speculative Bayesian sections, this could be a solid accept. In its current form, it is a borderline paper that some reviewers will champion for its empirical insights and others will critique for limited methodological novelty.

**Confidence**: 4/5
I am familiar with both DIF methodology in psychometrics and LLM benchmark evaluation. I have carefully reviewed the experimental evidence, the decision chain, and the paper framing. My main uncertainty is whether the ICLR community would value the empirical-characterization contribution sufficiently in the absence of algorithmic novelty -- this is a venue-specific judgment call where reasonable reviewers may disagree.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce65c3d5-443a-4f20-9cc2-d29711080f0b",
  "isSidechain": true,
  "agentId": "a0cd16afcb8320959",
  "requestId": "req_011CbEtY1hWZhsAkXqXp2UBT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8870861e-ed37-4468-acec-cdcae02c2160",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "bed74537-8027-4ea2-ace4-14fc8a5d1a29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DfP1CqJEihosbPAhDQD2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2237,
      "cache_read_input_tokens": 49924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2237,
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
