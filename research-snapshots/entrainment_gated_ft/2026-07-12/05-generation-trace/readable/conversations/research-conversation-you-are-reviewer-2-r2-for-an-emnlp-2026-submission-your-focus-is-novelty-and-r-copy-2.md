# Research conversation: You are Reviewer 2 (R2) for an EMNLP 2026 submission. Your focus is **Novelty and Related Work**. You must produce a rig

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-af582cd3fea4c7abc.jsonl`
- **Structured JSON:** [`7c1fc7e8943f86c807e3.json`](../../sessions/7c/7c1fc7e8943f86c807e3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-19T15:32:36.250Z_

You are Reviewer 2 (R2) for an EMNLP 2026 submission. Your focus is **Novelty and Related Work**. You must produce a rigorous, calibrated review. EMNLP 2026 uses ARR unified review with Overall Assessment on a 1–5 half-point scale (5=Award top 2.5%, 4=Main conference, 3=Findings, 2=Resubmit, 1=Do not resubmit). Main acceptance ~21%.

## Paper Summary
Title: "Task-Dependent Convergence and Per-Example Divergence in Attention-Augmented Linear Recurrent Models"
Submitted to EMNLP 2026 (anonymous).

The paper uses 72 publicly available hybrid recurrent models from Wang et al. (2025) model zoo (GatedDeltaNet, RetNet, HGRN2; 5 attention ratios; 2 scales 340M/1.3B) to analyze how attention shapes cross-architecture behavioral diversity at the per-example level. Three claims:

1. **Task-dependent convergence**: On retrieval-heavy LAMBADA, cross-arch std reduces 79% (ρ=−1.0, p=0.017 uncorrected). BoolQ/StoryCloze suggestive. Nothing on reasoning tasks. MMLU excluded (GDN artifact).
2. **Scale-dependent convergence**: 1.3B monotonic, 340M non-monotonic rebound at h8.
3. **Per-example divergence**: Jaccard < 0.10 across architectures on LAMBADA despite aggregate convergence. KW p=0.0005 cross-arch difference in hurt profiles. "Scissors" co-evolution pattern.

The paper explicitly states: "Our contribution is analytical depth on public infrastructure: we do not propose new methods or models." It frames the relationship to Wang et al. as analogous to medical meta-analyses on public data.

Key related work the paper cites:
- Wang et al. (2025): The model zoo paper. Authors claim 4 analytical dimensions absent from Wang et al.
- D'Amour et al. (2022): Underspecification framework — the paper claims to quantify this in hybrid recurrent architectures
- Fort et al. (2019), McCoy et al. (2020): Deep ensemble diversity, BERT disagreement
- Swayamdipta et al. (2020): Dataset cartography
- Krogh & Vedelsby (1994), Kuncheva & Whitaker (2003): Ensemble diversity theory
- Arora et al. (2024): Attention's role in recurrent architectures (training dynamics, not per-example)
- Jamba (Lieber 2024), Griffin (De 2024), Mamba-2 (Dao & Gu 2024): Hybrid architectures
- Clark et al. (2019), Vig (2019), Jain & Wallace (2019), Wiegreffe & Pinter (2019): Attention interpretability

## Experiment Design Context
From the experiment plan, the paper was designed with a narrative: "Claim 1 weakened to 'convergence on retrieval-heavy tasks with suggestive evidence on related benchmarks'. LAMBADA remains the only BH-FDR significant anchor. Claim 3 per-example divergence becomes the paper's relatively strongest independent contribution. Target: EMNLP Findings, honest framing."

The differentiation from Wang et al. (exp-009) identified 4 points: (1) quantified cross-arch std trajectories, (2) per-example analysis, (3) scale-dependent convergence, (4) attention characterization. Wang et al.'s convergence observation was a single qualitative sentence.

## Your Task
Evaluate the paper on these dimensions with detailed justification:

### Novelty Assessment
- How novel are the research questions?
- How novel are the methods/analyses?
- Is this a sufficient contribution for EMNLP 2026?
- The paper applies well-known analysis techniques (Jaccard, Spearman, KW, bootstrap) to a specific domain — is this enough?
- The paper explicitly says per-example divergence is a "well-documented phenomenon" (D'Amour 2022, Fort 2019, McCoy 2020) and they are "quantifying it in a new domain" — assess whether the domain application alone is sufficient contribution.

### Related Work Assessment
- Is the related work comprehensive?
- Are there important missing references?
- Consider: Are there papers on per-example analysis of SSMs/recurrent models? Papers on attention's role in hybrid architectures beyond Arora et al.? Papers on model diversity in efficient architectures?
- Is the positioning relative to Wang et al. appropriate? Is the "meta-analysis" framing convincing or does it undersell/oversell?
- Does the paper adequately differentiate from ensemble diversity literature?

### Framing and Positioning
- Is the paper's narrative compelling?
- Does the "underspecification" framing add value or is it window-dressing on straightforward analysis?
- Is the practical implications argument (architecture selection) convincing given the evidence strength?

### Soundness (1-5)
### Excitement (1-5) 
### Reproducibility (1-5)
### Overall Assessment (1-5, half-point scale)
Calibrate strictly: 4=Main (~top 21%), 3=Findings, 2=Resubmit.

### Strengths (bulleted)
### Weaknesses (bulleted)
### Questions for Authors
### Missing References (if any)

Format as a structured review. Be rigorous but fair. Credit intellectual honesty but assess whether the contribution clears the venue bar.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "0f8dc22d-c40a-4074-95b3-c9b67973efc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T15:32:36.253Z_

```json
{
  "parentUuid": "0f8dc22d-c40a-4074-95b3-c9b67973efc6",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
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
  "uuid": "773bf41c-403f-43ef-a1a9-c99226d94ced",
  "timestamp": "2026-05-19T15:32:36.253Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-19T15:32:39.978Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "773bf41c-403f-43ef-a1a9-c99226d94ced",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAoJBUWJfKch3DkZRjw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9b15793-3765-4542-a53d-c28b3ab8b7d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017PEauajd1LEpmb3VWdsqTQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7648,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7648,
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

_source line 4 · 2026-05-19T15:32:40.580Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JEEC3mGm5zdeKSQogdtKGY`</summary>

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
  "parentUuid": "e9b15793-3765-4542-a53d-c28b3ab8b7d0",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAoJBUWJfKch3DkZRjw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8e0bf8e-14fa-4f91-8cf3-83c05381983b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017PEauajd1LEpmb3VWdsqTQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7648,
      "cache_read_input_tokens": 8252,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7648
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 7648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7648,
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

_source line 5 · 2026-05-19T15:32:40.583Z_

<details><summary>↩ Tool result · `toolu_01JEEC3mGm5zdeKSQogdtKGY`</summary>

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
  "parentUuid": "c8e0bf8e-14fa-4f91-8cf3-83c05381983b",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "03c61393-affc-4ac5-862a-14a9332ac4c0",
  "sourceToolAssistantUUID": "c8e0bf8e-14fa-4f91-8cf3-83c05381983b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T15:32:43.661Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_018VEDnmyQpu7TRawGRB5m4D`</summary>

```json
{
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03c61393-affc-4ac5-862a-14a9332ac4c0",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAocXHoHSLyRH8axYtP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3700c8f-3968-469b-8fd4-4e4f8a93879d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013nWdvncpGAvLpNuMMzWQh9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15900,
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

_source line 7 · 2026-05-19T15:32:43.702Z_

<details><summary>↩ Tool result · `toolu_018VEDnmyQpu7TRawGRB5m4D`</summary>

```text
{"result":"# 项目 entrainment_gated_ft 概况\n\n## 实验状态 (11 个)\n\n- **exp-010**: DONE (success) — \n- **exp-011**: RUNNING — \n- **exp-001**: DONE (success) — \n- **exp-008**: DONE (success) — \n- **exp-003-p2v2**: PREPARING (killed) — \n- **exp-003-p2**: DONE (negative) — \n- **exp-003**: DONE (negative) — \n- **exp-009**: DONE (success) — \n- **eval_340m_retnet_hgrn2**: DONE (success) — \n- **hgrn2_eval_h3_1**: DONE (success) — \n- **hgrn2_eval_1_3b_all**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-011 | Cross-architecture variance on additional retrieval-dependent benchmarks (StoryCloze, BoolQ, COPA, PIQA, SciQ) decreases monotonically with attention ratio, providing a second statistically significant anchor (exact permutation p<0.05, two-tailed) beyond LAMBADA after Bonferroni correction | — | — | — |\n\n## 待处理\n- exp-003-p2v2: Helped samples have higher pure-model perplexity (model uncertain → attention helped) while hurt samples have lower perplexity (model confident → attention interfered), with architecture-specific patterns across GDN/RetNet/HGRN2. Retry with HGRN2 monkey-patch fix for _tied_weights_keys AttributeError.（准备中）\n\n## 近期结论\n- **exp-010** (success): Aggregate convergence (cross-arch std decreasing with attention ratio) and per-example divergence (low Jaccard of helped/hurt sets) co-evolve as attention ratio increases on LAMBADA — demonstrating underspecification: architectures converge in aggregate performance while helping/hurting almost entirely different samples ← 基于 exp-001\n- **exp-001** (success): Cross-architecture variance (std) on retrieval-dependent tasks decreases monotonically with attention ratio at 1.3B scale, while reasoning-dependent tasks show no convergence — establishing task-specificity as a principled feature of the equalizer effect, not a limitation\n  [task_specificity_results](/api/workspace-files/projects/entrainment_gated_ft/artifacts/exp-001/data/task_specificity_results.csv) | [task_specificity_figure](/api/workspace-files/projects/entrainment_gated_ft/artifacts/exp-001/chart/task_specificity_figure_info.txt)\n- **exp-008** (success): Replacing scipy.stats.spearmanr asymptotic p-values with exact permutation tests (n=5, 120 permutations, two-tailed) corrects the spurious p=1.4e-24 bug; expected: LAMBADA raw p≈0.017, Bonferroni adj-p≈0.100 (not significant), confirming need for additional benchmarks ← 基于 exp-001\n\n## 趋势\n成功 6 / 负向 2 / 失败 0 / 共 9\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-48145: 无 GPU 信息\n\n## 告警\n- hgrn2_eval_1_3b_all: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3700c8f-3968-469b-8fd4-4e4f8a93879d",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "8883b494-04ae-4e05-91eb-95d17cdee34b",
  "sourceToolAssistantUUID": "b3700c8f-3968-469b-8fd4-4e4f8a93879d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T15:32:44.518Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SmMbGJx9o8VTM1SR5PqH31`</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8883b494-04ae-4e05-91eb-95d17cdee34b",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAocXHoHSLyRH8axYtP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6594f47-eee5-4db3-a1ed-4911ee1c3fbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013nWdvncpGAvLpNuMMzWQh9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15900,
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

_source line 9 · 2026-05-19T15:32:44.527Z_

<details><summary>↩ Tool result · `toolu_01SmMbGJx9o8VTM1SR5PqH31`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/report.md\", \"content\": \"# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp-011 | Cross-architecture variance on additional retrieval-dependent benchmarks (StoryCloze, BoolQ, COPA, PIQA, SciQ) decreases monotonically with attention ratio, providing a second statistically significant anchor (exact permutation p<0.05, two-tailed) beyond LAMBADA after Bonferroni correction | — | — | — |\\n\\n## 待处理\\n- exp-003-p2v2: Helped samples have higher pure-model perplexity (model uncertain → attention helped) while hurt samples have lower perplexity (model confident → attention interfered), with architecture-specific patterns across GDN/RetNet/HGRN2. Retry with HGRN2 monkey-patch fix for _tied_weights_keys AttributeError.（准备中）\\n\\n## 近期结论\\n- **exp-010** (success): Aggregate convergence (cross-arch std decreasing with attention ratio) and per-example divergence (low Jaccard of helped/hurt sets) co-evolve as attention ratio increases on LAMBADA — demonstrating underspecification: architectures converge in aggregate performance while helping/hurting almost entirely different samples ← 基于 exp-001\\n- **exp-001** (success): Cross-architecture variance (std) on retrieval-dependent tasks decreases monotonically with attention ratio at 1.3B scale, while reasoning-dependent tasks show no convergence — establishing task-specificity as a principled feature of the equalizer effect, not a limitation\\n  [task_specificity_results](/api/workspace-files/projects/entrainment_gated_ft/artifacts/exp-001/data/task_specificity_results.csv) | [task_specificity_figure](/api/workspace-files/projects/entrainment_gated_ft/artifacts/exp-001/chart/task_specificity_figure_info.txt)\\n- **exp-008** (success): Replacing scipy.stats.spearmanr asymptotic p-values with exact permutation tests (n=5, 120 permutations, two-tailed) corrects the spurious p=1.4e-24 bug; expected: LAMBADA raw p≈0.017, Bonferroni adj-p≈0.100 (not significant), confirming need for additional benchmarks ← 基于 exp-001\\n\\n## 趋势\\n成功 6 / 负向 2 / 失败 0 / 共 9\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestb-48145: 无 GPU 信息\\n\\n## 告警\\n- hgrn2_eval_1_3b_all: 已被终止 — unknown\\n\", \"total_chars\": 2179, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6594f47-eee5-4db3-a1ed-4911ee1c3fbe",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "42a133d1-9c4a-4f58-a22e-2652235f2787",
  "sourceToolAssistantUUID": "c6594f47-eee5-4db3-a1ed-4911ee1c3fbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T15:32:44.874Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DzMHQaKfMfF96p1oUhY4cs`</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42a133d1-9c4a-4f58-a22e-2652235f2787",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAocXHoHSLyRH8axYtP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "749044ab-df51-439a-8745-01da765a4518",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013nWdvncpGAvLpNuMMzWQh9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15900,
      "output_tokens": 260,
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
          "output_tokens": 260,
          "cache_read_input_tokens": 15900,
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

_source line 11 · 2026-05-19T15:32:44.885Z_

<details><summary>↩ Tool result · `toolu_01DzMHQaKfMfF96p1oUhY4cs`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'entrainment_gated_ft'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "749044ab-df51-439a-8745-01da765a4518",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "0d724b50-58e9-42cc-b716-212a840a1951",
  "sourceToolAssistantUUID": "749044ab-df51-439a-8745-01da765a4518",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T15:32:48.976Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DR2pqahjxijgnYwdEVZFvX`</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d724b50-58e9-42cc-b716-212a840a1951",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAow6zJPjxybQfpoS5q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7fd667d-02f6-4398-b47b-d336d8060b8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YAR2oPrVXNZDWCwyYgJdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2322,
      "cache_read_input_tokens": 17347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2322,
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

_source line 13 · 2026-05-19T15:32:48.987Z_

<details><summary>↩ Tool result · `toolu_01DR2pqahjxijgnYwdEVZFvX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/paper_framing.md\", \"content\": \"# Paper Framing — entrainment_gated_ft\\n\\n> Revised 2026-05-19 after Dream review (best case = 2.5/5). Major reframing: drop \\\"paradox\\\" narrative, engage related work, add retrieval benchmarks.\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Findings (via ARR)\\n- Stretch: EMNLP 2026 Main\\n- Deadline: ARR June 2026 cycle (submission ~June 15)\\n\\n## Paper Type\\nEmpirical analysis paper — quantifying a known phenomenon (per-example divergence under aggregate convergence) in a specific important domain (hybrid recurrent architectures)\\n\\n## Core Claims (3 条)\\n\\n### Claim 1: Task-Dependent Convergence\\nAdding attention layers to different linear recurrent architectures (GatedDeltaNet, RetNet, HGRN2) induces aggregate performance convergence whose strength varies with task type. Convergence is strongest on LAMBADA (ρ=-1.0, p=0.017 two-tailed, cross-arch std drops 79%), suggestive on ARC-Easy (ρ=-0.7, p=0.233, underpowered at n=5), and absent on reasoning-heavy tasks. **Critical need**: a second high-retrieval benchmark showing significant convergence to survive multi-comparison correction.\\n\\n### Claim 2: Scale-Dependent Convergence\\nThe convergence effect requires sufficient model capacity: monotonically complete at 1.3B (ρ=-1.0, p=0.017 two-tailed) but only partial at 340M with a non-monotonic rebound. Only two scale points (Wang et al. cap at 1.3B). Frame as binary contrast, not extrapolatable trend.\\n\\n### Claim 3: Per-Example Divergence Under Aggregate Convergence\\nDespite aggregate convergence, attention acts on nearly non-overlapping sample subsets per architecture (pairwise Jaccard < 0.10). This is an instance of the well-documented underspecification phenomenon (D'Amour et al. 2022) applied to hybrid architectures. Our contribution is **quantifying** it in this specific context, NOT claiming to discover it. Surface features AND baseline model perplexity do not differentiate helped/hurt samples within an architecture — the effect is opaque to standard features. However, cross-architecture comparison reveals systematic differences in baseline difficulty profiles of affected samples (Kruskal-Wallis p=0.0005 for hurt samples), confirming the architecture-specificity is structured, not random noise.\\n\\n**Decoupling finding (exp-010, D008)**: Aggregate convergence and per-example divergence are **decoupled** — they operate on different timescales w.r.t. attention ratio:\\n- Aggregate σ decreases **gradually** across 5 attention levels (0.024 → 0.016 → 0.014 → 0.006 → 0.005)\\n- Per-example Jaccard **saturates immediately** at the first attention level (4%) and remains flat (~0.095)\\n- Net asymmetry (HGRN2 net positive vs GDN/RetNet net negative) **increases** with attention (0.013 → 0.040)\\n- Implication: minimal attention creates full per-example architecture-specificity; gradual increases only affect aggregate convergence\\n\\n⚠️ Do NOT frame as \\\"co-evolution.\\\" Spearman ρ=-0.70 (p=0.23) is inflated by degenerate pure=0 point (Jaccard=NaN→0); excluding it: ρ=-0.40, p=0.75. The correct narrative is **decoupling**, which is a stronger finding: aggregate metrics converge while per-example dynamics increasingly diverge.\\n\\n## Story Spine\\n\\n### Problem\\nHybrid architectures mixing linear recurrence with full attention are becoming standard. While Wang et al. (2025) provide an extensive model zoo, the community lacks quantitative understanding of how attention affects cross-architecture behavioral diversity at the per-example level.\\n\\n### Related Work Positioning (CRITICAL — Dream W2)\\nThe observation that models with similar aggregate performance differ per-example is well-established:\\n- **Ensemble diversity**: Krogh & Vedelsby (1995), Kuncheva & Whitaker (2003) — diverse ensemble members err on different examples by construction\\n- **Underspecification**: D'Amour et al. (2022) — equivalent aggregate performance masks prediction-level differences\\n- **Dataset cartography**: Swayamdipta et al. (2020) — per-example difficulty varies across models\\n- **Simpson's paradox / ecological fallacy**: Aggregate-vs-disaggregate discrepancy is a textbook phenomenon\\n\\nOur contribution is NOT discovering this phenomenon. It IS quantifying how it manifests specifically when attention is added to linear recurrent models, and characterizing its task-dependency and scale-dependency. This is valuable because hybrid architectures are a design choice practitioners make — understanding per-example implications informs that choice.\\n\\n### Our Framing\\nWe provide the first systematic per-example analysis of attention's equalizing effect in hybrid recurrent architectures. Using Wang et al.'s public model zoo (72 models), we quantify (a) task-dependent convergence strength, (b) scale-dependent convergence completeness, and (c) architecture-specific per-example divergence patterns. Our contribution is analytical depth on public infrastructure, not new methods or models.\\n\\n### Headline Result Template\\n\\\"At 1.3B scale, adding attention to hybrid recurrent models reduces cross-architecture variance by 79% on LAMBADA, yet per-example analysis reveals nearly non-overlapping affected sample subsets (Jaccard < 0.10) — a manifestation of underspecification that has practical implications for architecture selection.\\\"\\n\\n## Dream Review Findings (D006) — Must Address\\n\\n### W1: Single-benchmark significance [MAJOR, blocking]\\nAfter Bonferroni (6 benchmarks, α=0.0083), LAMBADA p=0.017 (two-tailed) does NOT survive. Need: (a) FDR correction (Benjamini-Hochberg) as primary reporting, (b) additional high-retrieval benchmarks for a second significant anchor. Candidates: StoryCloze, BoolQ, COPA, closed-book QA tasks available in lm-eval.\\n\\n### W2: Missing related work [MAJOR, blocking for submission]\\nNeed 20+ references engaging ensemble diversity, underspecification, dataset cartography, attention interpretability, hybrid architectures (Jamba, RWKV-6, RecurrentGemma). Paper Agent handles this during writing.\\n\\n### W3: Mechanistic overclaiming [MAJOR, partially addressed]\\nAlready reworded Claim 3 from \\\"Mechanism\\\" to \\\"Effects\\\". Must NOT use \\\"mechanistic analysis\\\" in paper — use \\\"characterization\\\" or \\\"decomposition\\\" instead. Attention weight analysis (exp-004) is descriptive, not causal. Frame honestly.\\n\\n### W4: Incremental over Wang et al. [MAJOR]\\nMitigate by: (a) engaging related work to show the QUESTION we ask is independently motivated by ensemble/underspecification literature, (b) framing contribution as analytical toolkit + quantitative characterization, not re-analysis. (c) Per-example analysis is genuinely novel for this model family.\\n\\n## Venue Fit Risks\\n(unchanged from previous version, see git history)\\n\\n## Anticipated Reviewer Concerns\\n\\n### Concern A: \\\"This is just a re-analysis of Wang et al.'s models\\\"\\nResponse: Yes, and that's the point — public infrastructure enables community analysis. Our per-example decomposition, task-dependency characterization, and scale-dependency analysis are not in Wang et al. The contribution is analytical, like meta-analyses in medicine.\\nRequired: Strong Related Work positioning; frame as \\\"community analysis\\\" paper.\\n\\n### Concern B: \\\"Only one task shows the effect\\\" + Bonferroni failure\\n**Statistical strategy** (from exp-008, verified by Reviewer with independent reproduction):\\n1. **Lead with percentile CI (valid-only)**: BCa degenerates at ρ=-1.0 boundary (z0=-3.86); fall back to percentile CI on valid bootstrap resamples (8875/10000; 11.25% degenerate from n=3 same-architecture redraws). Valid-only percentile CI = **[-1.0, -0.7]**, 100% of valid resamples have ρ<0. Full percentile CI (degenerate-as-zero) = [-1.0, 0.0] touches zero. Paper leads with valid-only CI; BCa degeneracy + degenerate-sample treatment in appendix.\\n2. **Report exact permutation p**: LAMBADA p=0.017 (two-tailed, 2/120 permutations). Honest and transparent.\\n3. **Bonferroni in supplementary**: adj-p=0.100 (two-tailed). Report honestly as \\\"does not survive Bonferroni.\\\" BH-FDR also gives 0.100 (no additional benefit with only 1 small p-value). If exp-011 produces a second significant benchmark, BH-FDR becomes more favorable than Bonferroni.\\n4. **GDN-excluded sensitivity**: Excluding GDN (D004 confound): LAMBADA ρ drops to -0.7 (p=0.233); ARC-Easy ρ **improves** from -0.7 to -0.9 (p=0.083, suggestive — D004 noise removed); **⚠️ MMLU ρ FLIPS from -0.7 to +0.6** — MMLU apparent convergence was entirely GDN-driven and MUST NOT appear as convergence evidence anywhere in the paper (D007). Report both full and GDN-excluded analyses. The ARC-Easy improvement after confound removal is itself informative, especially in exp-011 context.\\n5. **exp-011**: Additional retrieval benchmarks (StoryCloze/BoolQ/COPA) for a potential second significant anchor. CRITICAL for acceptance — with exp-011 data, BH-FDR could diverge favorably from Bonferroni.\\n6. **Effect sizes**: Cohen's d CI crosses zero; omega² near zero. Do NOT lead with effect sizes — lead with BCa CI and convergence magnitude (std 0.024→0.005, 79% reduction).\\n\\nRequired experiments: exp-011 (additional retrieval benchmarks), exp-008 (robustness with corrected p-values), exp-002 (per-example validation).\\n\\n### Concern C: \\\"The per-example divergence is a known phenomenon\\\"\\nResponse: Acknowledge explicitly. Our contribution is quantification in hybrid architectures, not discovery of the phenomenon. Cite ensemble diversity + underspecification.\\nRequired: Related Work section (Paper Agent).\\n\\n### Concern D: \\\"n=3 architectures is too few\\\"\\nResponse: 3 architectures × 5 ratios × 2 scales = 30 models. Per-example analysis provides 5153 data points per comparison. Check for additional architectures (exp-005).\\n\\n### Concern E: \\\"Two scales don't establish a trend\\\"\\nResponse: Binary contrast, not trend. 7B unavailable. Frame as \\\"scale is a necessary condition.\\\" exp-007 for 340M rebound mechanism.\\n\\n### Concern F: \\\"No causal mechanism\\\" (NEW from Dream)\\nResponse: We do NOT claim causal mechanism. We characterize and describe. Attention weight analysis (exp-004) is descriptive. Interventional experiments (head swaps, ablations) are acknowledged as future work. Honest framing prevents overclaiming.\\n\", \"total_chars\": 10106, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7fd667d-02f6-4398-b47b-d336d8060b8e",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "d41da3b2-3efb-4592-bdf3-7a09c0cd5e46",
  "sourceToolAssistantUUID": "d7fd667d-02f6-4398-b47b-d336d8060b8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T15:32:49.950Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017m6ZhkJrcjoDawykP5LaME`</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d41da3b2-3efb-4592-bdf3-7a09c0cd5e46",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAow6zJPjxybQfpoS5q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce49c682-58f5-4cc9-a819-3c8c898229d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YAR2oPrVXNZDWCwyYgJdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2322,
      "cache_read_input_tokens": 17347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2322,
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

_source line 15 · 2026-05-19T15:32:49.959Z_

<details><summary>↩ Tool result · `toolu_017m6ZhkJrcjoDawykP5LaME`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'entrainment_gated_ft'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce49c682-58f5-4cc9-a819-3c8c898229d9",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "fef69bda-fc0e-4902-9f1b-e0476f000c52",
  "sourceToolAssistantUUID": "ce49c682-58f5-4cc9-a819-3c8c898229d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T15:32:50.400Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WLsgYCwM1T9LqLvgocEjU8`</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fef69bda-fc0e-4902-9f1b-e0476f000c52",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAow6zJPjxybQfpoS5q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "214a15fa-8a0c-4175-a23e-ea289418858e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YAR2oPrVXNZDWCwyYgJdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2322,
      "cache_read_input_tokens": 17347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2322,
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

_source line 17 · 2026-05-19T15:32:50.409Z_

<details><summary>↩ Tool result · `toolu_01WLsgYCwM1T9LqLvgocEjU8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/memory.md\", \"content\": \"# FLA 版本与 m-a-p 模型兼容性调查结果 (2026-05-18)\\n\\n## 核心结论：fla 0.5.0 与 m-a-p 模型兼容，attn.D 丢弃无影响\\n\\n### 1. attn.D 参数真相\\n\\n- **m-a-p GatedDeltaNet 模型**（如 `1.3B-100B-GatedDeltaNet-pure`）的 checkpoint 中包含 `attn.D` 参数（每层一个，共 24 个）\\n- `self.D` 在 fla 的 GatedDeltaNet 初始实现（commit `4064237`, 2024-12-20）中被声明为 `nn.Parameter(torch.ones(num_heads))`，继承自 Mamba2 的 skip connection 设计\\n- **但 self.D 从未在 forward() 中被使用** — 它是死参数，训练过程中不参与计算、不接收梯度，始终保持初始值 `ones`\\n- `self.D` 在 commit `834989c` (2025-03-12) 中被移除，对应 issue #226 \\\"Remove redundant parameter\\\"\\n- fla v0.1.0 (2025-03-20) 起所有版本均不含 self.D\\n- **结论：加载模型时 attn.D 被 strict=False 静默丢弃，对模型行为和评估结果无任何影响**\\n\\n### 2. m-a-p 模型训练环境\\n\\n- **论文**: Wang et al. \\\"A Systematic Analysis of Hybrid Linear Attention\\\" (arXiv 2507.06457, July 2025)\\n- **训练框架**: flash-linear-attention (fla) + flame (基于 torchtitan)\\n- **训练数据**: FineWeb-Edu\\n- **模型规模**: 72 个模型（36×340M/20B tokens + 36×1.3B/100B tokens）\\n- **transformers 版本**: \\n  - 1.3B GatedDeltaNet-pure: 4.51.3 (2025-04-14)\\n  - RetNet / 340M New GatedDeltaNet: 4.49.0 (~2025-02)\\n- **fla 版本**: 未在论文或模型卡中明确标注。根据 self.D 存在于 checkpoint 推断，训练使用的是 2025-03-12 之前的 fla 开发版本（pre-v0.1.0）\\n- **HuggingFace 集合**: https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e\\n\\n### 3. fla PyPI 版本历史\\n\\n| 版本 | 发布日期 | 备注 |\\n|------|----------|------|\\n| 0.1.0 | 2025-03-20 | 首个 tagged release，已无 self.D |\\n| 0.1.1 | 2025-03-24 | |\\n| 0.1.2 | 2025-03-31 | |\\n| 0.2.0 | 2025-04-11 | |\\n| 0.2.1 | 2025-04-23 | |\\n| 0.2.2 | 2025-06-05 | GDN GVA support |\\n| 0.3.0 | 2025-07-14 | MesaNet/PaTH/Comba/MLA; head_first deprecated |\\n| 0.3.2 | 2025-09-10 | fla-core 包分离 |\\n| 0.4.0 | 2025-10-27 | KDA |\\n| 0.4.1 | 2025-12-24 | |\\n| 0.4.2 | 2026-03-12 | |\\n| 0.5.0 | 2026-04-21 | 当前版本 |\\n\\n### 4. RetNet 模型情况\\n\\n- RetNet 模型 checkpoint 中**没有 attn.D**，不存在参数丢弃问题\\n- config 使用 transformers 4.49.0\\n- 模型参数结构（q/k/v/g_proj, g_norm_swish_gate, o_proj）与 fla MultiScaleRetention 层一致\\n\\n### 5. 建议\\n\\n**使用 fla 0.5.0（或任何 >=0.1.0 版本）加载 m-a-p 模型是安全的**，只需确保加载时 `strict=False`。attn.D 被丢弃不会影响模型输出。\\n\\n---\\n\\n# 统计报告规则 (2026-05-19, Director 硬约束)\\n\\n**所有分析报告中的统计 claim 必须附原始数值 (ρ=X, p=Y)，不允许只写结论。**\\n\\n事件：wang_et_al_differentiation.md 中 Worker 产出 \\\"4/6 benchmarks 显著收敛\\\" 的虚假 claim（实际仅 LAMBADA 1/6 显著）。Director 发现后标记为 CRITICAL。\\n\\n规则：\\n- 每个 \\\"显著/不显著\\\" claim 后必须跟 (ρ=X, p=Y) 或对应的检验统计量\\n- \\\"majority\\\"/\\\"most\\\" 等量化词必须有准确计数支撑（如 \\\"4/6\\\" 必须逐一列出哪 4 个）\\n- 此规则适用于所有项目产出（分析报告、论文章节、汇报材料）\\n\\n---\\n\\n# exp-003 表面特征分析教训 (2026-05-19)\\n\\n**表面特征（token frequency、context length、lexical diversity）无法区分 LAMBADA 上的 helped/hurt 样本。**\\n\\n- GDN/HGRN2：所有特征 p > 0.2，无信号\\n- RetNet：context_length p=0.012, r=-0.096（统计显著但效应量微不足道）；context_unique_tokens p=0.009, r=-0.099\\n- 跨架构比较：三架构 helped 样本特征分布无显著差异\\n\\n**启示**：per-example 效应的机制在模型内部（attention pattern / representation level），不在输入表面特征。这排除了 \\\"attention 只帮助长上下文\\\" 或 \\\"attention 只帮助低频词\\\" 等 trivial 解释，强化了 Claim 3（architecture-specific mechanism）的论证——需要 exp-004（attention weight extraction）来揭示真正的机制。\\n\\n---\\n\\n# exp-010 Bridge 分析：Decoupling 叙事 (2026-05-19, D008 修正)\\n\\n**正确叙事是 \\\"decoupling\\\"（解耦），不是 \\\"co-evolution\\\" 或 \\\"paradoxical coexistence\\\"。**\\n\\nReviewer 发现方法论问题：5-point Spearman ρ=-0.70 (p=0.23) 几乎完全由 pure=0 退化点驱动（Jaccard=NaN 赋值 0）。去掉 pure 后 ρ=-0.40, p=0.75，本质无关。\\n\\n**实际 pattern**：\\n- Jaccard 在 4% attention（h24-1）即饱和到 ~0.095，之后平坦\\n- Aggregate σ 从 0.024 逐步递减到 0.005\\n- 两个过程运行在**不同时间尺度**上\\n\\n**论文写作硬约束**：\\n- 禁用：co-evolution, paradoxical coexistence, paradox\\n- 使用：decoupling, different timescales\\n- Net asymmetry 递增（0.013→0.040）是真实 pattern，可强调\\n- 可视化应突出两条曲线的不同时间尺度，而非相关性\\n\", \"total_chars\": 3437, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "214a15fa-8a0c-4175-a23e-ea289418858e",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "823172ee-4bf8-4307-9f96-cecf590305ba",
  "sourceToolAssistantUUID": "214a15fa-8a0c-4175-a23e-ea289418858e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T15:32:50.991Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DdioqSGinUmXerJgTY5yfT`</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "823172ee-4bf8-4307-9f96-cecf590305ba",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAow6zJPjxybQfpoS5q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0caade7b-59b4-4a6a-a13a-3940cfe99fe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YAR2oPrVXNZDWCwyYgJdz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2322,
      "cache_read_input_tokens": 17347,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2322
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 388,
          "cache_read_input_tokens": 17347,
          "cache_creation_input_tokens": 2322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2322,
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

_source line 19 · 2026-05-19T15:32:51.000Z_

<details><summary>↩ Tool result · `toolu_01DdioqSGinUmXerJgTY5yfT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/decisions.yaml\", \"content\": \"_next_id: 9\\ndecisions:\\n- id: D001\\n  date: 2026-05-18 07:24 UTC\\n  summary: MVP Direct variant 340M 全模型 random-chance → 先跑 log-prob 评估，同时查 1.3B 模型可用性\\n  rationale: 16 个模型（含 Transformer baseline）在 depth 1-5 上全部 ~10% accuracy。根因：340M 模型无法通过\\n    generation 完成 in-context function lookup（输出\\\"1998/1999\\\"而非执行查找）。Transformer ceiling\\n    0% → ROADMAP 的 ceiling≥50% 过滤器触发，无 eligible depth。核心理论未被证伪，只是 340M+generation\\n    这个探针失效。下一步：(1) log-prob 评估（30min，测 internal representation 差异），(2) 并行查 1.3B 模型可用性。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-18 09:50 UTC\\n  summary: 1.3B 也无 function composition ICL 能力，MVP 从 synthetic task 双轨 pivot：7B task\\n    validation + 1.3B standard benchmarks\\n  rationale: 两轮实验（340M generation+logprob, 1.3B generation+logprob）一致确认 Ye et al.\\n    的 L-FuncComp 对 Wang et al. base models 不可行——Transformer baseline 自身也只有 random-chance，无法建立\\n    ceiling。根因：pretrained base models 在 ≤1.3B 规模未习得 arbitrary lookup table 的 ICL 能力。核心理论未被证伪，但\\n    synthetic task 作为 probe 在此 scale 下失效。Pivot 方案：(1) 7B Instruct 快速验证 task design\\n    是否本身有问题，(2) 在已有 1.3B hybrid 模型上跑 standard benchmarks（LAMBADA/HellaSwag/ARC/MMLU）检测架构差异信号——如果\\n    attention ratio 对不同难度 benchmark 的影响不同，MVP 仍可 pass，且论文更有 practical relevance。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-18 09:54 UTC\\n  summary: 预注册 benchmark composition depth 赋值（结果出来前锁定，不可事后调整）\\n  rationale: 'IDEA_BRIEF 要求 \\\"composition depth must be derivable from task structure\\n    alone, not from empirical performance\\\"。在 Track 1 benchmark 结果出来前锁定每个 task 的 depth\\n    赋值，防止 post-hoc rationalization。赋值基于 task 的计算结构分析：depth 1 = 单步模式匹配/句法判断（无需跨 context\\n    组合信息）；depth 2 = 需要检索 + 单步推理组合；depth 3 = 需要多步推理链或跨多个 context 片段组合。\\n\\n\\n    预注册赋值：\\n\\n    - Depth 1: lambada_openai (last-word prediction, 单步 pattern completion), blimp\\n    (单条句法规则判断)\\n\\n    - Depth 2: hellaswag (situation model + completion matching), winogrande (coreference:\\n    world knowledge + reasoning), arc_easy (单步 science reasoning), mmlu 5-shot (knowledge\\n    retrieval + single-step reasoning)\\n\\n    - Depth 3: arc_challenge (multi-step science reasoning, 需要推理链)\\n\\n\\n    需补充 depth 3+ 任务使 Spearman 相关性有足够 depth 分层。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-18 16:33 UTC\\n  summary: GDN hybrid-3-1 存在 attn.num_heads confound（16 vs 32），论文分析需区分 GDN（有 confound）和\\n    RetNet/HGRN2（无 confound）\\n  rationale: Wang et al. 的 GDN hybrid-3-1 在 340M 和 1.3B 规模都使用 attn.num_heads=16（GQA\\n    2:1），而 h6/h12/h24 使用 32（GQA 4:1）。这意味着 h3-1 不仅 attention 层更多，per-layer attention\\n    capacity 也不同。RetNet 和 HGRN2 所有 ratio 统一 16 heads，无此问题。论文中 GDN 跨 ratio 趋势需标注此 caveat；如果\\n    RetNet/HGRN2 的 clean 数据显示一致趋势，可缓解 GDN confound 的影响。\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-19 12:50 UTC\\n  summary: MVP 原始 entrainment 假设 FAIL，pivot to Equalizer Effect story，target EMNLP\\n    2026\\n  rationale: 26 模型 ×6 benchmarks 全面否定原假设。但发现 equalizer effect（attention 使不同架构在 LAMBADA\\n    上收敛）+ scale dependency（1.3B 完全 vs 340M 部分）+ per-example mechanism（不同架构不同 sample\\n    子集，Jaccard ~0.09）。用户设定 venue=EMNLP 2026，表明继续推进。Pivot 方向：empirical analysis paper，围绕\\n    equalizer effect 的 quantitative characterization + scale dependency + mechanistic\\n    analysis。\\n  related_experiments:\\n  - exp_id: eval_340m_retnet_hgrn2\\n    role: evidence\\n    result: 340M partial convergence confirmed\\n  - exp_id: hgrn2_eval_h3_1\\n    role: evidence\\n    result: architecture-dependent direction confirmed\\n  depends_on:\\n  - D002\\n  - D003\\n  - D004\\n- id: D006\\n  date: 2026-05-19 13:53 UTC\\n  summary: Dream best case 2.5/5 → 重大 framing 调整：放弃 \\\"paradox\\\" 叙事，转为 \\\"quantification\\n    of known phenomenon in hybrid architectures\\\"；补 high-retrieval benchmarks；补 Related\\n    Work\\n  rationale: Dream 模拟审稿（best case）暴露四个 Major weakness：(1) 单 benchmark 统计显著性——Bonferroni\\n    下 LAMBADA p=0.017 不通过；(2) \\\"equalizer paradox\\\" 是已知现象（ensemble diversity, underspecification）——我们不能声称发现\\n    paradox；(3) mechanistic claims 是 correlational 不是 causal；(4) 纯 re-analysis Wang\\n    et al. 模型的 incremental contribution。Path to Findings (3.0) 需要：Related Work 20+\\n    refs、去掉 paradox framing、额外 high-retrieval benchmark（第二个显著 anchor）。Path to Main\\n    (4.0) 需要 interventional experiments + 7B，不可行。调整策略目标：EMNLP Findings (3.0)。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: evidence\\n    result: only LAMBADA significant, W1 confirmed\\n  - exp_id: exp-003\\n    role: evidence\\n    result: surface features negative, W3 weakens mechanism claims\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-19 14:31 UTC\\n  summary: MMLU blacklisted from convergence evidence — GDN-excluded sensitivity reveals\\n    ρ flips to +0.6\\n  rationale: exp-008 GDN-excluded sensitivity analysis shows MMLU ρ flips from -0.7\\n    to +0.6 when GDN (carrying D004 confound) is removed. The apparent MMLU convergence\\n    was entirely driven by GDN. Any reviewer running GDN-excluded robustness check\\n    would catch this immediately. MMLU must NOT appear as convergence support in the\\n    paper. ARC-Easy improves from -0.7 to -0.9 (p=0.083) after GDN exclusion — signal\\n    is cleaner, usable as suggestive evidence especially alongside exp-011.\\n  related_experiments:\\n  - exp_id: exp-008\\n    role: source\\n    result: MMLU convergence entirely GDN-driven; ARC-Easy signal improves post-exclusion\\n  depends_on:\\n  - D004\\n- id: D008\\n  date: 2026-05-19 15:11 UTC\\n  summary: exp-010 \\\"co-evolution\\\" → \\\"decoupling\\\" framing：per-example divergence 在\\n    4% attention 即饱和，aggregate convergence 逐步递减，二者解耦\\n  rationale: Reviewer 发现 5-point Spearman ρ=-0.70 (p=0.23) 被 pure=0 退化点膨胀（Jaccard=NaN→0）。去掉后\\n    4-point ρ=-0.40, p=0.75。实际 pattern 是 Jaccard 在首个 attention level 即饱和 (~0.095)，aggregate\\n    σ 逐步下降。\\\"Decoupling\\\" 是比 \\\"co-evolution\\\" 更准确且更强的叙事——aggregate 趋同掩盖了 increasingly\\n    divergent per-example dynamics。Net asymmetry 递增 (0.013→0.040) 进一步支持此解读。\\n  related_experiments:\\n  - exp_id: exp-010\\n    role: evidence\\n    result: Aggregate σ monotonically decreasing; Jaccard flat ~0.095; net asymmetry\\n      increasing\\n  depends_on:\\n  - D006\\n\", \"total_chars\": 5998, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0caade7b-59b4-4a6a-a13a-3940cfe99fe7",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "445fb5af-264e-4e0c-9e74-3cb2529978dd",
  "sourceToolAssistantUUID": "0caade7b-59b4-4a6a-a13a-3940cfe99fe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-19T15:32:54.614Z_

Now let me read the actual paper draft and the experiment results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "445fb5af-264e-4e0c-9e74-3cb2529978dd",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCApPiP7L2Mz4NQiZj7k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7980cd8-66e8-4850-bc08-6438cad3ca45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2w123CY4387A6jG7X1ZfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9000,
      "cache_read_input_tokens": 19669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9000,
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

_source line 21 · 2026-05-19T15:32:55.145Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012EYgQksQYPrHDqYhogtYMa`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7980cd8-66e8-4850-bc08-6438cad3ca45",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCApPiP7L2Mz4NQiZj7k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa7f4aab-04dc-428d-a09f-160be2df2c5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2w123CY4387A6jG7X1ZfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9000,
      "cache_read_input_tokens": 19669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9000,
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

_source line 22 · 2026-05-19T15:32:55.155Z_

<details><summary>↩ Tool result · `toolu_012EYgQksQYPrHDqYhogtYMa`</summary>

```text
artifacts/dream_reports/dream_20260519T131014/best/paper.tex
artifacts/dream_reports/dream_20260519T131014/median/paper.tex
artifacts/dream_reports/dream_20260519T131014/worst/paper.tex
artifacts/dream_reports/dream_20260519T135121/best/paper.tex
artifacts/dream_reports/dream_20260519T135121/median/paper.tex
artifacts/dream_reports/dream_20260519T135121/worst/paper.tex
artifacts/dream_reports/dream_20260519T143201/best/paper.tex
artifacts/dream_reports/dream_20260519T143201/median/paper.tex
artifacts/dream_reports/dream_20260519T143201/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa7f4aab-04dc-428d-a09f-160be2df2c5c",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "2aaeeb52-6fa3-4945-87b9-f7ad37f53474",
  "sourceToolAssistantUUID": "aa7f4aab-04dc-428d-a09f-160be2df2c5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T15:32:56.164Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Vk8stnAY7jT4RNhWpMq9fN`</summary>

```json
{
  "pattern": "**/artifacts/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2aaeeb52-6fa3-4945-87b9-f7ad37f53474",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCApPiP7L2Mz4NQiZj7k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0cf46236-8ece-42dd-9eb0-6cebc08843f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2w123CY4387A6jG7X1ZfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9000,
      "cache_read_input_tokens": 19669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9000,
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

_source line 24 · 2026-05-19T15:32:56.175Z_

<details><summary>↩ Tool result · `toolu_01Vk8stnAY7jT4RNhWpMq9fN`</summary>

```text
artifacts/synthetic_task_design.md
artifacts/lm_eval_1.3b_results.md
artifacts/wang_et_al_analysis.md
artifacts/_project/report/wang_7b_search_results.md
artifacts/wang_7b_search_results.md
artifacts/_project/report/per_example_data_audit.md
artifacts/per_example_data_audit.md
artifacts/dream_reports/dream_20260519T125419/best/paper_framing.md
artifacts/dream_reports/dream_20260519T131014/best/paper_framing.md
artifacts/dream_reports/dream_20260519T131014/median/paper_framing.md
artifacts/dream_reports/dream_20260519T131014/worst/paper_framing.md
artifacts/dream_reports/dream_20260519T131014/best/review_report.md
artifacts/dream_reports/dream_20260519T135121/best/paper_framing.md
artifacts/dream_reports/dream_20260519T135121/median/paper_framing.md
artifacts/dream_reports/dream_20260519T135121/worst/paper_framing.md
artifacts/dream_reports/dream_20260519T135121/best/review_report.md
artifacts/dream_reports/dream_20260519T135121/median/review_report.md
artifacts/dream_reports/dream_20260519T143201/best/paper_framing.md
artifacts/dream_reports/dream_20260519T143201/median/paper_framing.md
artifacts/dream_reports/dream_20260519T143201/worst/paper_framing.md
artifacts/dream_reports/dream_20260519T143201/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cf46236-8ece-42dd-9eb0-6cebc08843f1",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "d2dc6f9e-49d5-4d17-9349-30a24c5e61f0",
  "sourceToolAssistantUUID": "0cf46236-8ece-42dd-9eb0-6cebc08843f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T15:32:56.684Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WNvhEpop429zK5FGALkKcm`</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2dc6f9e-49d5-4d17-9349-30a24c5e61f0",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCApPiP7L2Mz4NQiZj7k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db8fb5c7-1932-4335-93c7-44c6b2209fbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2w123CY4387A6jG7X1ZfN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9000,
      "cache_read_input_tokens": 19669,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9000
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 19669,
          "cache_creation_input_tokens": 9000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9000,
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

_source line 26 · 2026-05-19T15:32:56.693Z_

<details><summary>↩ Tool result · `toolu_01WNvhEpop429zK5FGALkKcm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/ROADMAP.md\", \"content\": \"# entrainment_gated_ft — Research Dashboard\\n\\n> 最后更新: 2026-05-19 15:10 UTC | 更新原因: exp-010 完成(success) + exp-011 运行中(4/16)\\n\\n## 核心方向\\n**Quantifying per-example divergence under aggregate convergence in hybrid recurrent architectures**. Attention 使不同 recurrent 架构在 retrieval tasks 上趋同，但 per-example 效应几乎不重叠（Jaccard < 0.10）。这是 underspecification 现象在 hybrid 架构中的具体表现。详见 paper_framing.md。\\n\\n## 当前阶段\\n**Research 阶段** — Post-Dream 重大调整（D006），exp-011 关键实验运行中\\n\\n## 战略状态\\n- **Dream best case = 2.5/5 (Borderline Findings)**\\n- 四个 Major weakness 已识别并纳入 plan（W1-W4）\\n- 目标：EMNLP 2026 Findings (3.0)，stretch: Main\\n- DDL: ARR June 2026 (~June 15)，距今 ~27 天\\n- Dream dream_20260519T143201 正在自动重试中（imagining 阶段）\\n\\n## 当前进展\\n- ✅ MVP FAIL → pivot to equalizer effect（D005）\\n- ✅ 26 models × 6 benchmarks 完整评估\\n- ✅ exp-001: Task-specificity（PASS，LAMBADA 唯一显著，连续谱 framing）\\n- ✅ exp-009: Wang et al. differentiation（PASS，4 维度分析完成）\\n- ✅ exp-003: Surface features 全阴性 → 排除 trivial 解释；跨架构 KW 显著\\n- ✅ exp-003-p2: Perplexity 分析（negative within-arch，但跨架构 KW p=0.0005 for hurt）\\n- ✅ exp-008: Statistical robustness（exact permutation p, BCa CI, GDN-excluded sensitivity）\\n- 🔄 **exp-011: Additional retrieval benchmarks — 运行中**（4/16 模型完成，~8min/model，预计 UTC 16:40 完成）\\n- ⚠️ StoryCloze 不可用，xstorycloze_en **已批准追加**（exp-011 主批次后，lambada_standard 不追加）\\n- ✅ exp-010: Convergence-divergence bridge（success — σ 5x单调下降，Jaccard平坦~0.10，paradoxical coexistence）\\n- 🔜 exp-002: Multi-benchmark per-example（20h GPU）\\n- 🔜 exp-004: Attention weight analysis（4h GPU）\\n\\n## 近期任务（按优先级）\\n- [ ] 等 exp-011 批量完成（~UTC 16:40）→ 收敛分析（Spearman + exact permutation）\\n- [ ] exp-011 后追加 xstorycloze_en 评估（~2h GPU，16 模型，Director 已批准）\\n- [x] 修复 experiment_plan.yaml registry_id 映射 ✅\\n- [x] 修复 exp-001 registry p-value ✅（0.008 → 0.0167 two-tailed）\\n- [x] exp-010: Convergence-divergence bridge ✅（paradoxical coexistence confirmed）\\n- [ ] exp-002: Multi-benchmark per-example（20h GPU）\\n- [ ] exp-004: Attention weight analysis（4h GPU）\\n- [ ] 论文写作启动（目标 June 5-7，Paper Agent）\\n\\n## GPU 预算\\n- 分配：westb-48145 cuda:0（RTX PRO 6000 × 1）\\n- 当前：**exp-011 占用中**（批量评估 4/16，~8min/model，cron 监控中）\\n- P0 GPU 总需：~35h（exp-002 20h + exp-011 ~9h含xstorycloze + exp-004 4h + exp-007 2h）\\n- P1 GPU：exp-005 6h\\n\\n## 已知风险\\n- COPA 仅 100 测试样本，Spearman 分析不稳定，不作主要证据\\n- Transformer baseline 必须从收敛分析中排除\\n- 如 4 个新 benchmark + xstorycloze_en 均不显著 → W1 无法解决，Findings 路径受阻\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D008 | 2026-05-19 | exp-010 \\\"co-evolution\\\" → \\\"decoupling\\\" framing：per- | exp-010 |\\n| D008 | 2026-05-19 | Claim 3 叙事修正：decoupling 替代 co-evolution/paradox（退化点膨胀） | exp-010 |\\n| D007 | 2026-05-19 | MMLU blacklisted from convergence evidence — GDN-e | exp-008 |\\n| D006 | 2026-05-19 | Dream best case 2.5/5 → 重大 framing 调整：放弃 \\\"paradox\\\" | exp-001, exp-003 |\\n| D005 | 2026-05-19 | MVP 原始 entrainment 假设 FAIL，pivot to Equalizer Effe | eval_340m_retnet_hgrn2, hgrn2_eval_h3_1 |\\n| D004 | 2026-05-18 | GDN hybrid-3-1 存在 attn.num_heads confound（16 vs 32 | — |\\n| D003 | 2026-05-18 | 预注册 benchmark composition depth 赋值（结果出来前锁定，不可事后调整） | — |\\n| D002 | 2026-05-18 | 1.3B 也无 function composition ICL 能力，MVP 从 syntheti | — |\\n| D001 | 2026-05-18 | MVP Direct variant 340M 全模型 random-chance → 先跑 log | — |\\n\\n\", \"total_chars\": 3184, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db8fb5c7-1932-4335-93c7-44c6b2209fbe",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "e92010c5-5b2e-4aa6-8b8c-30100032cd67",
  "sourceToolAssistantUUID": "db8fb5c7-1932-4335-93c7-44c6b2209fbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T15:32:59.867Z_

<details open><summary>🔧 Tool call — Read · `toolu_015WKQG5QyqpiNtNP4dFidp3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T143201/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e92010c5-5b2e-4aa6-8b8c-30100032cd67",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCApoZLWjEBfj4M8Sn8V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5678e50-9543-4f98-bcdb-47ac77363a23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sL5fJ8zQAhfZ5HBX4zht7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2994,
      "cache_read_input_tokens": 28669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2994,
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

_source line 28 · 2026-05-19T15:33:00.160Z_

<details><summary>↩ Tool result · `toolu_015WKQG5QyqpiNtNP4dFidp3`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	
14	\title{Per-Example Analysis of Attention-Induced Convergence\\in Hybrid Recurrent Architectures}
15	
16	\author{Anonymous ACL submission}
17	
18	\begin{document}
19	\maketitle
20	
21	\begin{abstract}
22	Hybrid architectures combining linear recurrence with full attention are increasingly standard in language model design.
23	Using a public model zoo of 72+ hybrid models spanning four recurrence mechanisms (GatedDeltaNet, RetNet, HGRN2, Mamba2-hybrid), we provide a systematic per-example analysis of how attention affects cross-architecture behavioral diversity.
24	Adding attention layers induces \textit{task-dependent aggregate convergence}: cross-architecture performance variance decreases by 79\% on retrieval-demanding tasks such as LAMBADA and StoryCloze (Spearman $\rho = {-}1.0$, exact permutation $p = 0.017$ each, Benjamini-Hochberg adjusted $p = 0.042$), while reasoning-heavy tasks show no convergence.
25	This convergence requires sufficient model capacity, manifesting monotonically at 1.3B parameters but exhibiting a non-monotonic rebound at 340M due to parameter-budget constraints.
26	Per-example decomposition reveals that despite aggregate convergence, attention affects nearly non-overlapping sample subsets across architectures (pairwise Jaccard $< 0.10$), a manifestation of underspecification in hybrid architectures.
27	Neither surface features nor baseline perplexity predict which samples are affected within an architecture, yet cross-architecture comparison reveals structured differences (Kruskal-Wallis $p = 0.0005$).
28	These findings quantify the per-example implications of the attention-recurrence tradeoff and inform architecture selection for practitioners.
29	\end{abstract}
30	
31	%=============================================
32	\section{Introduction}
33	%=============================================
34	
35	Linear recurrent models such as RetNet \citep{sun2023retnet}, HGRN2 \citep{qin2024hgrn2}, and Mamba \citep{gu2023mamba} offer efficient alternatives to full Transformer attention for sequence modeling.
36	In practice, hybrid designs that interleave recurrent layers with a fraction of attention layers have become the dominant paradigm: Jamba \citep{lieber2024jamba}, RecurrentGemma \citep{botev2024recurrentgemma}, and RWKV-6 \citep{peng2024rwkv} all adopt this strategy.
37	\citet{wang2025zoo} provide an extensive model zoo of 72 hybrid models covering three recurrence mechanisms (GatedDeltaNet, RetNet, HGRN2), five attention ratios, and two scales (340M, 1.3B), offering a controlled testbed for studying attention's effect on architecture diversity.
38	
39	A natural question arises from this model zoo: does adding attention make all hybrid architectures equivalent?
40	\citet{wang2025zoo} observe convergence qualitatively as a side finding, noting in 1--2 sentences that architectures become more similar with more attention.
41	They do not quantify this observation, do not examine it at the per-example level, and do not analyze its task-dependency or scale-dependency.
42	Practitioners choosing between hybrid architectures need a more precise understanding of what convergence means and where it breaks down.
43	
44	The question of whether models with similar aggregate performance differ in their per-example predictions is well-established in the machine learning literature.
45	The underspecification framework \citep{damour2022underspecification} demonstrates that equivalent aggregate metrics can mask prediction-level differences.
46	Ensemble diversity theory \citep{krogh1995neural, kuncheva2003measures} formalizes how diverse ensemble members err on different examples by construction.
47	Dataset cartography \citep{swayamdipta2020dataset} reveals that per-example difficulty varies systematically across models.
48	Our contribution is not discovering this phenomenon; it is \textit{quantifying} how it manifests when attention is added to linear recurrent models, and characterizing its task-dependency and scale-dependency.
49	
50	We analyze Wang et al.'s model zoo supplemented with Mamba2-attention hybrids \citep{dao2024mamba2} (4 architectures $\times$ 5 attention ratios $\times$ 2 scales).
51	Our per-example decomposition, statistical framework, and multi-benchmark analysis go substantially beyond the qualitative observation in \citet{wang2025zoo}.
52	We frame this work as a \textit{community analysis paper}: public infrastructure enables independent analytical contributions, analogous to meta-analyses in medicine that draw new conclusions from existing clinical trials.
53	
54	Our contributions are:
55	\begin{enumerate}
56	\item \textbf{Task-dependent convergence.} We show that attention-induced convergence is a function of retrieval demand. Convergence is strongest on retrieval-dependent tasks (LAMBADA, StoryCloze: $\rho = {-}1.0$, $p = 0.017$, BH-FDR adjusted $p = 0.042$ on a pre-specified retrieval subset) and absent on reasoning-heavy tasks. This pattern holds across four architectures (\S\ref{sec:convergence}).
57	\item \textbf{Scale-dependent convergence.} Convergence is monotonically complete at 1.3B parameters but non-monotonic at 340M, with a rebound at high attention ratios. The rebound concentrates on the most difficult samples (73\% in the top difficulty quartile), consistent with a capacity bottleneck (\S\ref{sec:scale}).
58	\item \textbf{Per-example divergence under aggregate convergence.} Despite aggregate convergence, attention affects nearly non-overlapping sample subsets across architectures (Jaccard $< 0.10$). This architecture-specific effect is structured (cross-architecture Kruskal-Wallis $p = 0.0005$) but opaque to surface features and baseline perplexity (\S\ref{sec:perexample}).
59	\end{enumerate}
60	
61	%=============================================
62	\section{Related Work}
63	%=============================================
64	
65	\paragraph{Hybrid recurrent architectures.}
66	The design space of hybrid models mixing linear recurrence with attention has expanded rapidly.
67	GatedDeltaNet \citep{yang2024gdn} uses a delta-rule-based recurrence; RetNet \citep{sun2023retnet} uses exponential decay; HGRN2 \citep{qin2024hgrn2} uses hierarchical gating; and Mamba2 \citep{dao2024mamba2} uses selective state spaces.
68	Production systems including Jamba \citep{lieber2024jamba}, RecurrentGemma \citep{botev2024recurrentgemma}, and RWKV-6 \citep{peng2024rwkv} adopt hybrid strategies.
69	\citet{wang2025zoo} provide the most comprehensive controlled comparison to date, training 72 models with matched hyperparameters across three recurrence types, five attention ratios, and two scales.
70	Their focus is on training recipes and model zoo design; convergence is a qualitative side observation.
71	
72	\paragraph{Underspecification and ensemble diversity.}
73	\citet{damour2022underspecification} formalize underspecification: models with equivalent aggregate performance can differ arbitrarily at the prediction level.
74	This connects to classical ensemble diversity theory \citep{krogh1995neural, kuncheva2003measures}, where diverse members err on different examples by construction, and to dataset cartography \citep{swayamdipta2020dataset, ethayarajh2022understanding}, which reveals per-example difficulty variation across models.
75	Our work applies these ideas to a specific, practically important domain: hybrid recurrent architectures where the attention fraction is a tunable design choice.
76	
77	\paragraph{Attention analysis in hybrid models.}
78	Attention weight analysis has a long history starting from \citet{vaswani2017attention}.
79	In hybrid architectures, the interaction between attention and recurrence creates distinct computational roles: attention provides direct token-to-token access while recurrence compresses history into a fixed-size state.
80	Our attention pattern analysis (\S\ref{sec:attention}) is \textit{descriptive}, correlating attention concentration with per-example effects, not claiming causal mechanism.
81	
82	%=============================================
83	\section{Analytical Framework}
84	\label{sec:framework}
85	%=============================================
86	
87	\subsection{Model Zoo and Evaluation}
88	
89	We use the model zoo from \citet{wang2025zoo}, which contains 72 models: three recurrence types (GatedDeltaNet, RetNet, HGRN2) $\times$ five attention ratios $\times$ two scales (340M, 1.3B).
90	Attention ratios are denoted $h_{r:a}$ where $r$ recurrent layers alternate with $a$ attention layers: $h_0$ (pure recurrence), $h_{24:1}$, $h_{12:1}$, $h_{6:1}$, and $h_{3:1}$ (highest attention fraction).
91	We supplement this zoo with Mamba2-attention hybrids \citep{dao2024mamba2} at 1.3B scale across all five attention ratios, bringing the total to four architectures spanning delta-rule, exponential decay, hierarchical gating, and selective state-space recurrence mechanisms.
92	
93	All models are evaluated using lm-evaluation-harness \citep{gao2021framework} with \texttt{--log\_samples} to collect per-example predictions.
94	We evaluate on nine benchmarks: LAMBADA \citep{paperno2016lambada}, StoryCloze \citep{mostafazadeh2016corpus}, HellaSwag \citep{zellers2019hellaswag}, ARC-Easy and ARC-Challenge \citep{clark2018think}, Winogrande \citep{sakaguchi2020winogrande}, MMLU \citep{hendrycks2021measuring}, BoolQ \citep{clark2019boolq}, and COPA \citep{roemmele2011choice}.
95	
96	\subsection{Convergence Measurement}
97	
98	For each benchmark, we compute the cross-architecture standard deviation ($\sigma_\text{cross}$) of accuracy at each attention ratio.
99	The \textit{convergence trajectory} is the ordered sequence $[\sigma_\text{cross}(h_0), \sigma_\text{cross}(h_{24:1}), \ldots, \sigma_\text{cross}(h_{3:1})]$.
100	We quantify convergence strength using Spearman rank correlation $\rho_s$ between attention ratio rank (increasing attention) and $\sigma_\text{cross}$; a perfect monotonic decrease in variance yields $\rho_s = {-}1.0$.
101	Statistical significance is assessed via exact permutation tests (all $5! = 120$ permutations of 5 data points), yielding $p$-values with minimum resolution $2/120 \approx 0.017$ for two-tailed tests.
102	
103	\subsection{Per-Example Decomposition}
104	
105	For each pair of architectures at a given attention ratio, we identify the sets of examples \textit{helped} (incorrect $\to$ correct) and \textit{hurt} (correct $\to$ incorrect) by adding attention relative to pure recurrence.
106	We compute pairwise Jaccard similarity $J = |A \cap B| / |A \cup B|$ of helped (or hurt) sets between architecture pairs.
107	Low Jaccard indicates that attention acts on different examples depending on the architecture.
108	We also compute the mean absolute effect magnitude $|\Delta|$, the average accuracy change per example.
109	
110	\subsection{Statistical Framework}
111	\label{sec:statframework}
112	
113	We apply a layered multiple comparison correction strategy.
114	First, we establish a task taxonomy (\S\ref{sec:taxonomy}) that classifies benchmarks by retrieval demand \textit{before} conducting confirmatory tests on new benchmarks.
115	This pre-specified taxonomy defines the correction scope: only benchmarks with an a priori convergence prediction enter the retrieval-subset correction (Benjamini-Hochberg FDR, $m = 5$).
116	We also report a confirmatory-only correction (Bonferroni, $m = 3$, excluding the discovery benchmark LAMBADA) and a full correction across all 9 benchmarks ($m = 9$).
117	All three layers are presented transparently.
118	
119	%=============================================
120	\section{Task-Dependent Convergence}
121	\label{sec:convergence}
122	%=============================================
123	
124	\subsection{Cross-Architecture Convergence Across Benchmarks}
125	
126	Table~\ref{tab:benchmarks} presents convergence statistics for all nine benchmarks at 1.3B scale (three architectures: GDN, RetNet, HGRN2).
127	Convergence strength varies dramatically across tasks.
128	LAMBADA shows perfect monotonic convergence ($\rho = {-}1.0$, $p = 0.017$), with cross-architecture $\sigma$ decreasing from 0.024 (pure recurrence) to 0.005 (highest attention), a 79\% reduction.
129	StoryCloze shows an identical pattern ($\rho = {-}1.0$, $p = 0.017$, 79\% reduction).
130	BoolQ exhibits a suggestive but non-significant trend ($\rho = {-}0.7$, $p = 0.233$, 45\% reduction).
131	At the opposite extreme, reasoning-heavy tasks show no convergence: HellaSwag ($\rho = 0.3$), ARC-Challenge ($\rho = 0.6$), and Winogrande ($\rho = 0.1$) have positive or near-zero correlations, indicating that attention does not systematically reduce cross-architecture variance on these tasks.
132	
133	\begin{table*}[t]
134	\centering
135	\caption{Cross-architecture convergence across nine benchmarks (1.3B scale, three architectures). $\rho$: Spearman rank correlation between attention ratio and cross-architecture $\sigma$; $p$: two-tailed exact permutation test. Benchmarks sorted by $\rho$ within each category. Bold indicates statistical significance at $\alpha = 0.05$ (uncorrected).}
136	\label{tab:benchmarks}
137	\small
138	\begin{tabular}{llrrrrr}
139	\toprule
140	Benchmark & Category & $\rho$ & $p$ (exact) & $\sigma_{h_0}$ & $\sigma_{h_{3:1}}$ & Reduction (\%) \\
141	\midrule
142	LAMBADA & Retrieval & $\mathbf{{-}1.0}$ & $\mathbf{0.017}$ & 0.024 & 0.005 & 79 \\
143	StoryCloze & Retrieval & $\mathbf{{-}1.0}$ & $\mathbf{0.017}$ & 0.019 & 0.004 & 79 \\
144	\midrule
145	ARC-Easy & Mixed & ${-}0.7$ & 0.233 & \multicolumn{2}{c}{---} & --- \\
146	MMLU & Mixed & ${-}0.7$ & 0.233 & \multicolumn{2}{c}{---} & --- \\
147	BoolQ & Mixed & ${-}0.7$ & 0.233 & 0.022 & 0.012 & 45 \\
148	\midrule
149	COPA & Reasoning & ${-}0.3$ & 0.683 & 0.031 & 0.025 & 19 \\
150	Winogrande & Reasoning & $0.1$ & $>$0.2 & \multicolumn{2}{c}{---} & --- \\
151	HellaSwag & Reasoning & $0.3$ & $>$0.2 & \multicolumn{2}{c}{---} & --- \\
152	ARC-Challenge & Reasoning & $0.6$ & $>$0.2 & \multicolumn{2}{c}{---} & --- \\
153	\bottomrule
154	\end{tabular}
155	\end{table*}
156	
157	\subsection{Retrieval-Demand Taxonomy}
158	\label{sec:taxonomy}
159	
160	The convergence pattern follows a gradient aligned with retrieval demand.
161	LAMBADA requires predicting a final word from a passage, relying on attention's copy and induction-head mechanisms to retrieve contextual information.
162	StoryCloze requires selecting a coherent story ending, similarly demanding retrieval from narrative context.
163	Both tasks show $\rho = {-}1.0$.
164	Mixed tasks (ARC-Easy, MMLU, BoolQ) combine factual retrieval with reasoning, yielding intermediate $\rho$ values (${-}0.7$).
165	Reasoning-heavy tasks (HellaSwag, ARC-Challenge, Winogrande) depend on compositional inference that attention does not systematically improve across architectures, yielding $\rho \geq 0.1$.
166	
167	This taxonomy was established from the initial six-benchmark analysis \textit{before} evaluating StoryCloze, BoolQ, and COPA, making the confirmatory results a pre-specified hypothesis test rather than post-hoc rationalization.
168	The three new benchmarks confirm the predicted gradient: StoryCloze (high retrieval) shows $\rho = {-}1.0$; BoolQ (mixed retrieval/reasoning) shows $\rho = {-}0.7$; COPA (causal reasoning with minimal retrieval) shows $\rho = {-}0.3$.
169	
170	\subsection{Architecture Expansion with Mamba2}
171	
172	To test generalizability beyond three architectures, we evaluate Mamba2-attention hybrids at 1.3B on LAMBADA across all five attention ratios.
173	Table~\ref{tab:fourarch} shows that adding Mamba2 (selective state-space recurrence) preserves the convergence pattern.
174	Cross-architecture $\sigma$ with four architectures decreases from 0.029 at $h_0$ to 0.006 at $h_{3:1}$, an 80\% reduction ($\rho = {-}1.0$, $p = 0.017$).
175	The higher $\sigma$ at $h_0$ (0.029 vs.\ 0.024 with three architectures) reflects Mamba2's distinct baseline performance; convergence to $\sigma = 0.006$ demonstrates that four fundamentally different recurrence mechanisms (delta-rule, exponential decay, hierarchical gating, selective state-space) all converge under attention.
176	
177	Per-example analysis confirms that Mamba2's convergence is also architecture-specific: Jaccard similarity between Mamba2's helped set and those of other architectures ranges from 0.06 to 0.09, comparable to the three-architecture pairwise values.
178	Mamba2's standalone convergence trajectory approaches significance ($\rho = {-}0.9$, $p = 0.083$), with the weaker effect likely reflecting the selective state-space mechanism's stronger baseline sequence modeling.
179	
180	\begin{table}[t]
181	\centering
182	\caption{LAMBADA cross-architecture $\sigma$ with three vs.\ four architectures (1.3B). The fourth architecture (Mamba2) uses a selective state-space mechanism distinct from all three original recurrence types.}
183	\label{tab:fourarch}
184	\small
185	\begin{tabular}{lrr}
186	\toprule
187	Config & $\sigma$ (3 arch) & $\sigma$ (4 arch) \\
188	\midrule
189	$h_0$ & 0.024 & 0.029 \\
190	$h_{24:1}$ & 0.016 & 0.019 \\
191	$h_{12:1}$ & 0.014 & 0.014 \\
192	$h_{6:1}$ & 0.006 & 0.007 \\
193	$h_{3:1}$ & 0.005 & 0.006 \\
194	\midrule
195	Reduction (\%) & 79 & 80 \\
196	$\rho$ & ${-}1.0$ & ${-}1.0$ \\
197	$p$ (exact) & 0.017 & 0.017 \\
198	\bottomrule
199	\end{tabular}
200	\end{table}
201	
202	\subsection{Multiple Comparison Correction}
203	\label{sec:correction}
204	
205	Table~\ref{tab:correction} summarizes three layers of multiple comparison correction.
206	We report all three transparently.
207	
208	\textit{Layer 1: Pre-specified retrieval subset} ($m = 5$).
209	The retrieval-demand taxonomy identifies five benchmarks with an a priori convergence prediction: LAMBADA, StoryCloze, ARC-Easy, BoolQ, and COPA.
210	Benjamini-Hochberg step-up on this subset yields two significant benchmarks (LAMBADA and StoryCloze, adjusted $p = 0.042$).
211	
212	\textit{Layer 2: Confirmatory subset} ($m = 3$).
213	Treating LAMBADA as the discovery benchmark, we apply Bonferroni correction to the three newly evaluated retrieval benchmarks (StoryCloze, BoolQ, COPA).
214	StoryCloze survives at the boundary: adjusted $p = 0.050 = \alpha$ exactly.
215	
216	\textit{Layer 3: Full correction} ($m = 9$).
217	Applying BH-FDR across all nine benchmarks (including reasoning tasks with no convergence prediction), the rank-1 threshold is $0.05/9 = 0.0056$, and the smallest $p$-value (0.017) exceeds this threshold.
218	Zero benchmarks survive.
219	We report this honestly: full correction penalizes for testing benchmarks where no convergence was predicted.
220	
221	A bootstrap confidence interval for LAMBADA yields $\rho \in [{-}1.0, {-}0.7]$ (percentile method on 8,875/10,000 valid resamples; BCa is degenerate at the $\rho = {-}1.0$ boundary).
222	
223	\begin{table}[t]
224	\centering
225	\caption{Multiple comparison correction across three pre-specified scopes. BH: Benjamini-Hochberg FDR; Bonf: Bonferroni. $^\dagger$Borderline: $0.017 \times 3 = 0.050 = \alpha$.}
226	\label{tab:correction}
227	\small
228	\begin{tabular}{llrr}
229	\toprule
230	Scope & Method & $m$ & Sig. \\
231	\midrule
232	Retrieval subset & BH-FDR & 5 & 2 \\
233	Confirmatory only & Bonf. & 3 & 1$^\dagger$ \\
234	All benchmarks & BH-FDR & 9 & 0 \\
235	\bottomrule
236	\end{tabular}
237	\end{table}
238	
239	%=============================================
240	\section{Per-Example Divergence}
241	\label{sec:perexample}
242	%=============================================
243	
244	\subsection{Architecture-Specific Sample Sets}
245	
246	Table~\ref{tab:perexample} presents per-example divergence metrics at $h_{3:1}$ (1.3B) across four benchmarks with available per-example data (13 models evaluated: 10 at 340M, 3 at 1.3B; 18 GPU-hours).
247	On LAMBADA, the mean pairwise Jaccard of helped sets is 0.07: different architectures' attention rescues almost entirely different samples.
248	The mean absolute effect magnitude is 0.055, indicating substantial per-example impact.
249	
250	A clear gradient emerges: Jaccard increases from 0.07 (LAMBADA) to 0.16 (HellaSwag), while effect magnitude decreases from 0.055 to 0.020.
251	This gradient correlates strongly with the retrieval-demand taxonomy ($\rho = {-}0.92$ between Jaccard and retrieval demand).
252	On retrieval tasks, attention produces strong, architecture-specific effects (low Jaccard, high $|\Delta|$); on reasoning tasks, attention effects are weaker and less structured (higher Jaccard approaching random-set overlap, lower $|\Delta|$).
253	
254	\begin{table}[t]
255	\centering
256	\caption{Per-example divergence metrics at $h_{3:1}$ (1.3B). Lower Jaccard indicates more architecture-specific effects. Benchmarks ordered by retrieval demand. $\rho = {-}0.92$ between Jaccard and retrieval-demand rank.}
257	\label{tab:perexample}
258	\small
259	\begin{tabular}{llrr}
260	\toprule
261	Benchmark & Category & Jaccard & $|\Delta|$ \\
262	\midrule
263	LAMBADA & Retrieval & \textbf{0.07} & \textbf{0.055} \\
264	ARC-Easy & Mixed & 0.09 & 0.038 \\
265	ARC-Chall. & Reasoning & 0.14 & 0.025 \\
266	HellaSwag & Reasoning & 0.16 & 0.020 \\
267	\bottomrule
268	\end{tabular}
269	\end{table}
270	
271	\subsection{Sample Characterization}
272	\label{sec:characterization}
273	
274	We investigate what distinguishes helped from hurt samples within and across architectures on LAMBADA (Table~\ref{tab:characterization}).
275	
276	\textit{Within-architecture surface features.}
277	We test whether surface-level properties (context length, unique token count, lexical diversity) predict helped vs.\ hurt status within each architecture.
278	No test reaches practical significance: RetNet shows two nominally significant correlations (context length $p = 0.012$, $r = {-}0.096$; unique tokens $p = 0.009$, $r = {-}0.099$), but effect sizes are negligible.
279	GDN and HGRN2 show no significant features ($p > 0.2$ and $p > 0.5$ respectively).
280	This rules out trivial explanations such as ``attention only helps long sentences'' or ``attention only helps rare words.''
281	
282	\textit{Within-architecture baseline perplexity.}
283	The most natural hypothesis, that attention rescues samples where the base recurrent model is uncertain, also fails.
284	Mann-Whitney tests comparing helped vs.\ hurt samples on baseline (pure recurrence) perplexity are non-significant across all three architectures (GDN: $p = 0.209$, $r_{rb} = {-}0.045$; RetNet: $p = 0.659$, $r_{rb} = {-}0.017$; HGRN2: $p = 0.248$, $r_{rb} = {-}0.044$).
285	
286	\textit{Cross-architecture structured differences.}
287	Despite within-architecture opacity, cross-architecture comparison reveals structure.
288	A Kruskal-Wallis test on the baseline difficulty profiles of hurt samples across three architectures is highly significant ($p = 0.0005$); the helped-sample test is also significant ($p = 0.020$).
289	Different architectures systematically hurt samples with different difficulty characteristics, confirming that the per-example effect is not random noise but reflects architecture-specific computational properties.
290	
291	\begin{table}[t]
292	\centering
293	\caption{Sample characterization on LAMBADA (1.3B, $h_{3:1}$). Top: within-architecture tests (all non-significant, showing the effect is opaque to standard features). Bottom: cross-architecture Kruskal-Wallis tests (significant, confirming structured architecture-specificity).}
294	\label{tab:characterization}
295	\small
296	\begin{tabular}{lrr}
297	\toprule
298	\multicolumn{3}{l}{\textit{Within-arch: surface features}} \\
299	Architecture & Best $p$ & Best $|r|$ \\
300	\midrule
301	GDN & $>$0.5 & $<$0.05 \\
302	RetNet & 0.009 & 0.099 \\
303	HGRN2 & $>$0.2 & $<$0.05 \\
304	\midrule
305	\multicolumn{3}{l}{\textit{Within-arch: baseline perplexity}} \\
306	Architecture & $p$ (MW) & $r_{rb}$ \\
307	\midrule
308	GDN & 0.209 & ${-}0.045$ \\
309	RetNet & 0.659 & ${-}0.017$ \\
310	HGRN2 & 0.248 & ${-}0.044$ \\
311	\midrule
312	\multicolumn{3}{l}{\textit{Cross-arch: Kruskal-Wallis}} \\
313	Sample set & $p$ (KW) & \\
314	\midrule
315	Hurt & \textbf{0.0005} & \\
316	Helped & \textbf{0.020} & \\
317	\bottomrule
318	\end{tabular}
319	\end{table}
320	
321	\subsection{Attention Pattern Analysis}
322	\label{sec:attention}
323	
324	To provide a descriptive (not causal) account of per-example effects, we extract attention weights from the $h_{3:1}$ configurations of GDN, RetNet, and HGRN2 at 1.3B (3.5 GPU-hours; Table~\ref{tab:attention}).
325	We correlate attention entropy with per-example effect magnitude.
326	
327	All three architectures show a moderate positive correlation between attention concentration (low entropy) and positive per-example effect: GDN $r = 0.37$ ($p = 0.004$), RetNet $r = 0.40$ ($p = 0.001$), HGRN2 $r = 0.31$ ($p = 0.011$), with a mean of $r = 0.36$.
328	Helped samples tend to exhibit more focused attention patterns than hurt samples.
329	
330	The dominant attention focus distances differ across architectures in ways consistent with their recurrence mechanisms.
331	GDN attention concentrates on nearby tokens (3--8 positions), compensating for the delta rule's recent-context decay.
332	RetNet attention targets mid-range tokens (8--20 positions), compensating for exponential mid-range decay.
333	HGRN2 attention shows variable focus (5--15 positions), reflecting hierarchical gate-dependent retention patterns.
334	Cross-architecture attention pattern similarity is low (cosine similarity 0.21), directly explaining the low per-example Jaccard: architectures attend to different positions on the same sample, producing different helped/hurt sets.
335	
336	These results provide a partial descriptive account.
337	The moderate correlation ($r = 0.36$) leaves substantial unexplained variance, and the analysis is correlational.
338	We avoid causal claims; interventional experiments (attention head ablation, cross-architecture head swaps) remain future work.
339	
340	\begin{table}[t]
341	\centering
342	\caption{Attention concentration vs.\ per-example effect magnitude on LAMBADA ($h_{3:1}$, 1.3B). $r$: Spearman correlation between attention entropy and effect. Focus distance: dominant attention range. Cross-architecture attention similarity is low (cosine = 0.21).}
343	\label{tab:attention}
344	\small
345	\begin{tabular}{lrrl}
346	\toprule
347	Architecture & $r$ & $p$ & Focus range \\
348	\midrule
349	GDN & 0.37 & 0.004 & 3--8 tokens \\
350	RetNet & 0.40 & 0.001 & 8--20 tokens \\
351	HGRN2 & 0.31 & 0.011 & 5--15 tokens \\
352	\midrule
353	Mean & 0.36 & & \\
354	\bottomrule
355	\end{tabular}
356	\end{table}
357	
358	\subsection{Convergence-Divergence Co-evolution}
359	
360	Table~\ref{tab:coevolution} tracks the simultaneous evolution of aggregate convergence and per-example divergence as attention increases on LAMBADA (3 architectures, 1.3B).
361	As the attention ratio increases from $h_0$ to $h_{3:1}$, three metrics change monotonically: cross-architecture $\sigma$ decreases from 0.024 to 0.005 (convergence), mean effect magnitude increases from 0.0 to 0.055 (stronger per-example impact), and mean helped-set Jaccard decreases from 0.12 to 0.06 (increasing architecture-specificity).
362	
363	The rank correlation between $\sigma$ and $|\Delta|$ is $\rho = {-}1.0$ ($p = 0.017$): aggregate convergence and per-example divergence are monotonically coupled as a function of attention.
364	More attention produces both more similar aggregate outcomes \textit{and} more architecture-specific per-example effects.
365	This co-evolution is driven by a single mechanism: attention compensates for architecture-specific blind spots in the recurrent state.
366	Each architecture's recurrence has distinct information-retention weaknesses; attention fills these gaps differently, rescuing different samples (low Jaccard, high $|\Delta|$) while equalizing total performance ($\sigma$ decreases).
367	
368	\begin{table}[t]
369	\centering
370	\caption{Co-evolution of aggregate convergence and per-example divergence on LAMBADA (3 architectures, 1.3B). $\sigma$: cross-architecture std; $|\Delta|$: mean effect magnitude; $J$: mean helped-set Jaccard. Rank correlation between $\sigma$ and $|\Delta|$: $\rho = {-}1.0$, $p = 0.017$.}
371	\label{tab:coevolution}
372	\small
373	\begin{tabular}{lrrr}
374	\toprule
375	Config & $\sigma_\text{cross}$ & $|\Delta|$ & $J$ \\
376	\midrule
377	$h_0$ & 0.024 & 0.000 & --- \\
378	$h_{24:1}$ & 0.016 & 0.028 & 0.12 \\
379	$h_{12:1}$ & 0.014 & 0.035 & 0.09 \\
380	$h_{6:1}$ & 0.006 & 0.045 & 0.07 \\
381	$h_{3:1}$ & 0.005 & 0.055 & 0.06 \\
382	\bottomrule
383	\end{tabular}
384	\end{table}
385	
386	%=============================================
387	\section{Scale-Dependent Convergence}
388	\label{sec:scale}
389	%=============================================
390	
391	\subsection{Monotonic vs.\ Non-Monotonic Patterns}
392	
393	At 1.3B parameters, LAMBADA convergence is monotonically complete ($\rho = {-}1.0$, Table~\ref{tab:scale}).
394	At 340M, convergence is non-monotonic: $\sigma$ decreases from $h_0$ through $h_{12:1}$ but then rebounds, with $\sigma$ increasing by 0.009 from the minimum.
395	The rebound onset at $h_{12:1}$ (50\% attention layers) marks the point where the parameter budget becomes insufficient to maintain both effective recurrence and effective attention.
396	
397	\subsection{Capacity Bottleneck}
398	
399	We identify 145 ``rebound samples'' whose accuracy degrades at high attention ratios at 340M but not at 1.3B.
400	These samples concentrate in the top difficulty quartile (73\%) with a mean baseline perplexity of 4.62 at 340M vs.\ 3.15 at 1.3B.
401	On rebound samples, 1.3B models achieve 0.68 accuracy, while 340M models at $h_{6:1}$ achieve 0.49 and at $h_{3:1}$ only 0.35.
402	The correlation between the perplexity gap (340M vs.\ 1.3B) and rebound magnitude is $r = 0.38$: the samples with the largest capacity difference exhibit the strongest rebound.
403	
404	This pattern is consistent with a parameter-budget constraint: at 340M, each attention layer replaces a recurrent layer in a fixed total budget.
405	Beyond $h_{12:1}$, the recurrent pathway's capacity becomes insufficient for the most difficult samples, and the attention pathway cannot fully compensate.
406	At 1.3B, the total parameter budget is large enough to maintain both pathways.
407	
408	We verified that training token differences (340M: 20B tokens, 1.3B: 100B tokens) do not explain the rebound: if training duration were the primary factor, degradation would be uniform across attention ratios rather than specific to the onset at $h_{12:1}$.
409	
410	\begin{table}[t]
411	\centering
412	\caption{Scale comparison on LAMBADA. 1.3B convergence is monotonic; 340M shows a non-monotonic rebound. Rebound samples (n = 145) concentrate in the top difficulty quartile and are resolved at 1.3B scale.}
413	\label{tab:scale}
414	\small
415	\begin{tabular}{lrr}
416	\toprule
417	Metric & 1.3B & 340M \\
418	\midrule
419	Convergence pattern & Monotonic & Non-monotonic \\
420	$\rho$ & ${-}1.0$ & --- \\
421	$p$ (exact) & 0.017 & --- \\
422	Rebound onset & None & $h_{12:1}$ \\
423	\midrule
424	\multicolumn{3}{l}{\textit{Rebound samples (n = 145)}} \\
425	\% top difficulty Q & --- & 73\% \\
426	Mean baseline ppl & 3.15 & 4.62 \\
427	Acc at $h_{3:1}$ & 0.68 & 0.35 \\
428	\bottomrule
429	\end{tabular}
430	\end{table}
431	
432	%=============================================
433	\section{Discussion}
434	%=============================================
435	
436	\paragraph{Relation to \citet{wang2025zoo}.}
437	Our analysis builds on and complements \citet{wang2025zoo} across five dimensions.
438	(1) We quantify cross-architecture convergence with Spearman correlation and exact permutation tests, where Wang et al.\ provide only a qualitative observation.
439	(2) We introduce per-example decomposition with Jaccard quantification, which is entirely absent from Wang et al.
440	(3) We characterize scale-dependent convergence with a capacity bottleneck mechanism, where Wang et al.\ make only a binary statement.
441	(4) We establish a retrieval-demand taxonomy with statistical validation, where Wang et al.\ note ratio-sensitivity without categorization.
442	(5) We conduct multi-benchmark convergence analysis with pre-specified subset correction, where Wang et al.\ provide no cross-benchmark analysis.
443	These contributions are independently motivated by the underspecification and ensemble diversity literature, not by re-analyzing Wang et al.'s conclusions.
444	
445	\paragraph{Practical implications.}
446	For practitioners choosing between hybrid architectures, our findings suggest that the choice matters most on reasoning-heavy tasks and at smaller scales.
447	On retrieval-dependent tasks at 1.3B, architectural differences are substantially attenuated by attention (79\% $\sigma$ reduction), and per-example residual differences are small.
448	On reasoning tasks, architectural choice remains consequential.
449	The per-example architecture-specificity (Jaccard $< 0.10$) implies that ensembles of different hybrid architectures may yield diversity benefits even at high attention ratios.
450	
451	%=============================================
452	\section*{Limitations}
453	%=============================================
454	
455	Our analysis is constrained by the available model zoo in several ways.
456	First, we analyze only two scales (340M and 1.3B) because larger models are unavailable in \citet{wang2025zoo}.
457	The capacity bottleneck mechanism predicts that convergence should be complete at larger scales, but we cannot verify this.
458	Second, while we expand from three to four architectures with Mamba2, the statistical power of $n = 4$ remains limited.
459	Third, our convergence measurement relies on five discrete attention ratios; continuous interpolation could reveal non-monotonic patterns invisible at this resolution.
460	
461	On the statistical side, our strongest claim (task-dependent convergence) rests on two significant benchmarks after BH-FDR correction within a pre-specified retrieval subset ($m = 5$).
462	Under full correction across all nine benchmarks ($m = 9$), no benchmark survives.
463	The pre-specified subset correction is methodologically defensible (applying corrections to benchmarks where no convergence is predicted is overly conservative), but readers should weigh this choice.
464	
465	The attention pattern analysis (\S\ref{sec:attention}) provides only descriptive correlations ($r = 0.36$), not causal evidence.
466	Interventional experiments such as attention head ablation and cross-architecture head swaps would strengthen these findings but are beyond the scope of this study.
467	We do not claim to have identified the mechanism by which attention produces architecture-specific per-example effects; we characterize and quantify the phenomenon.
468	
469	%=============================================
470	\section{Conclusion}
471	%=============================================
472	
473	We present a systematic per-example analysis of attention's equalizing effect in hybrid recurrent architectures, using a model zoo of 72+ models spanning four recurrence mechanisms.
474	Our analysis reveals three complementary findings.
475	Attention-induced convergence is task-dependent, strongest on retrieval-demanding tasks and absent on reasoning tasks.
476	This convergence requires sufficient model capacity, with 340M models exhibiting a non-monotonic rebound driven by parameter-budget constraints.
477	Under aggregate convergence, per-example analysis reveals nearly non-overlapping affected sample subsets across architectures, a structured form of underspecification.
478	These findings provide quantitative grounding for architectural decisions in the growing design space of hybrid recurrent models.
479	
480	%=============================================
481	% References
482	%=============================================
483	\begin{thebibliography}{}
484	
485	\bibitem[{Benjamini and Hochberg(1995)}]{benjamini1995controlling}
486	Yoav Benjamini and Yosef Hochberg. 1995.
487	Controlling the false discovery rate: A practical and powerful approach to multiple testing.
488	\textit{Journal of the Royal Statistical Society: Series B}, 57(1):289--300.
489	
490	\bibitem[{Botev et~al.(2024)}]{botev2024recurrentgemma}
491	Aleksandar Botev, Soham De, Samuel~L.\ Smith, Anushan Fernando, George-Cristian Muraru, Ruba Haroun, Leonard Berrada, Razvan Pascanu, Pier~Giuseppe Sessa, Robert Dadashi, et~al. 2024.
492	RecurrentGemma: Moving past transformers for efficient open language models.
493	\textit{arXiv preprint arXiv:2404.07839}.
494	
495	\bibitem[{Clark et~al.(2018)}]{clark2018think}
496	Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. 2018.
497	Think you have solved question answering? Try ARC, the AI2 reasoning challenge.
498	\textit{arXiv preprint arXiv:1803.05457}.
499	
500	\bibitem[{Clark et~al.(2019)}]{clark2019boolq}
501	Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, and Kristina Toutanova. 2019.
502	BoolQ: Exploring the surprising difficulty of natural yes/no questions.
503	In \textit{Proceedings of NAACL-HLT}, pages 2924--2936.
504	
505	\bibitem[{D'Amour et~al.(2022)}]{damour2022underspecification}
506	Alexander D'Amour, Katherine Heller, Dan Moldovan, Ben Adlam, Babak Alipanahi, Alex Beutel, Christina Chen, Jonathan Deaton, Jacob Eisenstein, Matthew~D.\ Hoffman, et~al. 2022.
507	Underspecification presents challenges for credibility in modern machine learning.
508	\textit{Journal of Machine Learning Research}, 23(226):1--61.
509	
510	\bibitem[{Dao and Gu(2024)}]{dao2024mamba2}
511	Tri Dao and Albert Gu. 2024.
512	Transformers are SSMs: Generalized models and efficient algorithms through structured state space duality.
513	In \textit{Proceedings of ICML}.
514	
515	\bibitem[{Ethayarajh et~al.(2022)}]{ethayarajh2022understanding}
516	Kawin Ethayarajh, Yejin Choi, and Swabha Swayamdipta. 2022.
517	Understanding dataset difficulty with $\mathcal{V}$-usable information.
518	In \textit{Proceedings of ICML}.
519	
520	\bibitem[{Gao et~al.(2021)}]{gao2021framework}
521	Leo Gao, Jonathan Tow, Stella Biderman, Sid Black, Anthony DiPofi, Charles Foster, Laurence Golding, Jeffrey Hsu, Kyle McDonell, Niklas Muennighoff, Jason Phang, Laria Reynolds, Eric Tang, Anish Thite, Ben Wang, Kevin Wang, and Andy Zou. 2021.
522	A framework for few-shot language model evaluation.
523	Software available from \texttt{github.com/EleutherAI/lm-evaluation-harness}.
524	
525	\bibitem[{Gu and Dao(2023)}]{gu2023mamba}
526	Albert Gu and Tri Dao. 2023.
527	Mamba: Linear-time sequence modeling with selective state spaces.
528	\textit{arXiv preprint arXiv:2312.00752}.
529	
530	\bibitem[{Hendrycks et~al.(2021)}]{hendrycks2021measuring}
531	Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. 2021.
532	Measuring massive multitask language understanding.
533	In \textit{Proceedings of ICLR}.
534	
535	\bibitem[{Krogh and Vedelsby(1995)}]{krogh1995neural}
536	Anders Krogh and Jesper Vedelsby. 1995.
537	Neural network ensembles, cross validation, and active learning.
538	In \textit{Advances in Neural Information Processing Systems}, volume~7.
539	
540	\bibitem[{Kuncheva and Whitaker(2003)}]{kuncheva2003measures}
541	Ludmila~I.\ Kuncheva and Christopher~J.\ Whitaker. 2003.
542	Measures of diversity in classifier ensembles and their relationship with the ensemble accuracy.
543	\textit{Machine Learning}, 51(2):181--207.
544	
545	\bibitem[{Lieber et~al.(2024)}]{lieber2024jamba}
546	Opher Lieber, Barak Lenz, Hofit Bata, Gal Cohen, Jhonathan Osin, Itay Dalmedigos, Erez Safahi, Shaked Meirom, Yonatan Belinkov, Shai Shalev-Shwartz, et~al. 2024.
547	Jamba: A hybrid Transformer-Mamba language model.
548	\textit{arXiv preprint arXiv:2403.19887}.
549	
550	\bibitem[{Mostafazadeh et~al.(2016)}]{mostafazadeh2016corpus}
551	Nasrin Mostafazadeh, Nathanael Chambers, Xiaodong He, Devi Parikh, Dhruv Batra, Lucy Vanderwende, Pushmeet Kohli, and James Allen. 2016.
552	A corpus and cloze evaluation for deeper understanding of commonsense stories.
553	In \textit{Proceedings of NAACL-HLT}, pages 839--849.
554	
555	\bibitem[{Paperno et~al.(2016)}]{paperno2016lambada}
556	Denis Paperno, Germ{\'a}n Kruszewski, Angeliki Lazaridou, Quan~Ngoc Pham, Raffaella Bernardi, Sandro Pezzelle, Marco Baroni, Gemma Boleda, and Raquel Fern{\'a}ndez. 2016.
557	The LAMBADA dataset: Word prediction requiring a broad discourse context.
558	In \textit{Proceedings of ACL}, pages 1525--1534.
559	
560	\bibitem[{Peng et~al.(2024)}]{peng2024rwkv}
561	Bo~Peng, Daniel Goldstein, Quentin Anthony, Alon Albalak, Eric Alcaide, Stella Biderman, Eugene Cheah, Teddy Ferdinan, Haowen Hou, Przemys{\l}aw Kazienko, et~al. 2024.
562	Eagle and Finch: RWKV with matrix-valued states and dynamic recurrence.
563	In \textit{Proceedings of EMNLP Findings}.
564	
565	\bibitem[{Qin et~al.(2024)}]{qin2024hgrn2}
566	Zhen Qin, Songlin Yang, and Weixuan Sun. 2024.
567	HGRN2: Gated linear RNNs with state expansion.
568	\textit{arXiv preprint arXiv:2404.07904}.
569	
570	\bibitem[{Roemmele et~al.(2011)}]{roemmele2011choice}
571	Melissa Roemmele, Cosmin~Adrian Bejan, and Andrew~S.\ Gordon. 2011.
572	Choice of plausible alternatives: An evaluation of commonsense causal reasoning.
573	In \textit{AAAI Spring Symposium: Logical Formalizations of Commonsense Reasoning}.
574	
575	\bibitem[{Sakaguchi et~al.(2020)}]{sakaguchi2020winogrande}
576	Keisuke Sakaguchi, Ronan Le~Bras, Chandra Bhagavatula, and Yejin Choi. 2020.
577	WinoGrande: An adversarial Winograd schema challenge at scale.
578	In \textit{Proceedings of AAAI}.
579	
580	\bibitem[{Sun et~al.(2023)}]{sun2023retnet}
581	Yutao Sun, Li~Dong, Shaohan Huang, Shuming Ma, Yuqing Xia, Jilong Xue, Jianan Wang, and Furu Wei. 2023.
582	Retentive network: A successor to Transformer for large language models.
583	\textit{arXiv preprint arXiv:2307.08621}.
584	
585	\bibitem[{Swayamdipta et~al.(2020)}]{swayamdipta2020dataset}
586	Swabha Swayamdipta, Roy Schwartz, Nicholas Lourie, Yizhong Wang, Hannaneh Hajishirzi, Noah~A.\ Smith, and Yejin Choi. 2020.
587	Dataset cartography: Mapping and diagnosing datasets with training dynamics.
588	In \textit{Proceedings of EMNLP}, pages 9275--9293.
589	
590	\bibitem[{Vaswani et~al.(2017)}]{vaswani2017attention}
591	Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan~N.\ Gomez, {\L}ukasz Kaiser, and Illia Polosukhin. 2017.
592	Attention is all you need.
593	In \textit{Advances in Neural Information Processing Systems}, volume~30.
594	
595	\bibitem[{Wang et~al.(2025)}]{wang2025zoo}
596	Songlin Yang, Jan Kautz, and Ali Hatamizadeh. 2025.
597	The model zoo of hybrid sequence models.
598	\textit{arXiv preprint arXiv:2507.06457}.
599	
600	\bibitem[{Yang et~al.(2024)}]{yang2024gdn}
601	Songlin Yang, Jan Kautz, and Ali Hatamizadeh. 2024.
602	Gated delta networks: Improving mamba2 with delta rule.
603	\textit{arXiv preprint arXiv:2412.06464}.
604	
605	\bibitem[{Zellers et~al.(2019)}]{zellers2019hellaswag}
606	Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. 2019.
607	HellaSwag: Can a machine really finish your sentence?
608	In \textit{Proceedings of ACL}, pages 4791--4800.
609	
610	\end{thebibliography}
611	
612	%=============================================
613	\appendix
614	\section{Differentiation from \citet{wang2025zoo}}
615	\label{app:wang}
616	
617	Table~\ref{tab:wang} summarizes the analytical dimensions that distinguish our work from \citet{wang2025zoo}.
618	Our contributions are not a re-analysis of their conclusions but an independently motivated analytical framework grounded in the underspecification and ensemble diversity literature.
619	
620	\begin{table*}[t]
621	\centering
622	\caption{Side-by-side comparison of analytical dimensions. Wang et al.'s focus is model zoo design and training recipes; ours is quantitative convergence characterization.}
623	\label{tab:wang}
624	\small
625	\begin{tabular}{lll}
626	\toprule
627	Dimension & \citet{wang2025zoo} & This work \\
628	\midrule
629	Convergence quantification & Qualitative (1--2 sentences) & Spearman $\rho$ + exact permutation $p$ \\
630	Per-example decomposition & Absent & Jaccard + $|\Delta|$ across 4 benchmarks \\
631	Scale analysis & Binary statement & Capacity bottleneck mechanism \\
632	Task taxonomy & Ratio-sensitivity noted & Statistical validation (9 benchmarks) \\
633	Multi-benchmark correction & No cross-benchmark analysis & BH-FDR on pre-specified subset \\
634	\bottomrule
635	\end{tabular}
636	\end{table*}
637	
638	\section{GDN-Excluded Sensitivity Analysis}
639	\label{app:sensitivity}
640	
641	Excluding GDN (which has a known training confound at certain configurations), ARC-Easy $\rho$ improves from ${-}0.7$ to ${-}0.9$ (one-tailed $p = 0.042$, direction pre-specified), suggesting the confound added noise to the convergence signal.
642	This sensitivity analysis provides converging evidence for the retrieval-demand gradient but is not used as a primary claim.
643	
644	\end{document}
645	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5678e50-9543-4f98-bcdb-47ac77363a23",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "866d8c4d-6c15-40ed-8f9b-50df6f11451d",
  "sourceToolAssistantUUID": "e5678e50-9543-4f98-bcdb-47ac77363a23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T15:33:00.388Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HKU5s5opooyskUfEMKPHbx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T143201/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "866d8c4d-6c15-40ed-8f9b-50df6f11451d",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCApoZLWjEBfj4M8Sn8V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1100704a-e918-4f17-95ca-defb878cd4c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sL5fJ8zQAhfZ5HBX4zht7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2994,
      "cache_read_input_tokens": 28669,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2994
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 28669,
          "cache_creation_input_tokens": 2994,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2994,
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

_source line 30 · 2026-05-19T15:33:00.393Z_

<details><summary>↩ Tool result · `toolu_01HKU5s5opooyskUfEMKPHbx`</summary>

```text
1	---
2	dream_id: dream_20260519T143201
3	tier: best
4	overall_score: 3.0 — Findings
5	timestamp: 2026-05-19T15:30:51.083125+00:00
6	---
7	
8	# Dream Review Report — Per-Example Analysis of Attention-Induced Convergence in Hybrid Recurrent Architectures
9	
10	**Dream ID**: 20260519T143201 | **Review Mode**: full | **Venue**: EMNLP 2026 (ARR)
11	
12	---
13	
14	## 1. Paper Summary
15	
16	The paper analyzes a public model zoo of 72+ hybrid recurrent-attention models spanning four recurrence mechanisms (GatedDeltaNet, RetNet, HGRN2, Mamba2-hybrid) across five attention ratios and two scales (340M, 1.3B). It makes three claims: (1) attention-induced cross-architecture convergence is task-dependent, strongest on retrieval-demanding tasks (LAMBADA and StoryCloze, ρ=−1.0, BH-FDR adj p=0.042); (2) convergence requires sufficient model capacity, exhibiting a non-monotonic rebound at 340M; (3) despite aggregate convergence, per-example analysis reveals nearly non-overlapping affected sample subsets across architectures (Jaccard < 0.10), framed as underspecification. The paper positions itself as a "community analysis paper" drawing new conclusions from existing public infrastructure.
17	
18	---
19	
20	## 2. Consolidated Scores
21	
22	| Dimension | R1 (Methods+Exp) | R2 (Novelty+RW) | Converged |
23	|---|---|---|---|
24	| Soundness | 3 | 3 | **3** |
25	| Excitement | 3 | 2 | **2.5** |
26	| Reproducibility | 5 | 5 | **5** |
27	| Overall Assessment | 3.0 | 2.5 | **3.0** |
28	| Confidence | 4 | 4 | **4** |
29	
30	**Converged Overall: 3.0 (Findings-level)**
31	
32	**Rationale for convergence**: Both reviewers agree this falls short of Main (3.5+). R1's higher excitement reflects appreciation for the systematic characterization and honest statistical reporting; R2's lower score reflects limited novelty—standard tools applied to a known phenomenon. The converged 3.0 recognizes genuine analytical contributions (pre-specified confirmatory design, three-layer correction, per-example decomposition absent from Wang et al.) while acknowledging that the intellectual contribution does not clear the ~21% Main acceptance bar.
33	
34	---
35	
36	## 3. Strengths (Consensus)
37	
38	- **S1. Exemplary statistical transparency.** Three-layer multiple comparison correction (BH-FDR m=5, Bonferroni m=3, BH-FDR m=9) with all three reported honestly, including the full-correction failure (m=9: 0 significant). This level of transparency is rare and commendable. [Both R1, R2]
39	
40	- **S2. Pre-specified confirmatory design.** The retrieval-demand taxonomy was established from the initial six-benchmark analysis *before* evaluating StoryCloze/BoolQ/COPA, making the confirmatory results a genuine hypothesis test rather than post-hoc fishing. StoryCloze's ρ=−1.0 provides an independent second anchor. [Both R1, R2]
41	
42	- **S3. Honest negative results add value.** The within-architecture sample characterization (§5.2) reports that neither surface features nor baseline perplexity predict helped/hurt status—two layers of negative results that rule out trivial explanations and establish the phenomenon as genuinely opaque within-architecture. [R1]
43	
44	- **S4. Clear differentiation from Wang et al.** Five concrete dimensions with a side-by-side comparison table (Table 9) effectively establish that this is not a re-analysis but an independently motivated analytical contribution. The "community analysis paper" framing is appropriate. [R2]
45	
46	- **S5. High reproducibility.** All models are public (Wang et al. model zoo), evaluation uses standard lm-evaluation-harness, statistical tests are fully specified with exact permutation p-values. A reader could reproduce every result. [Both R1, R2]
47	
48	- **S6. Appropriate epistemic caution.** The attention pattern analysis (§5.3) is correctly labeled as descriptive, not causal. The paper avoids mechanistic overclaiming throughout. [R2]
49	
50	---
51	
52	## 4. Weaknesses (Consensus + Individual)
53	
54	### Critical (would block Main acceptance)
55	
56	- **W1. Missing Jaccard random-null baseline.** [Both R1, R2] The headline claim "nearly non-overlapping sample subsets (Jaccard < 0.10)" is uninterpretable without comparison to expected Jaccard under random set assignment of the same sizes. Given typical helped-set sizes (~500 of ~5000 total samples), random Jaccard could be ~0.05–0.10, meaning the observed values may be indistinguishable from chance. **Action needed**: compute expected Jaccard under random permutation and report the gap. If the gap is small, the entire per-example divergence narrative (Claim 3) is undermined.
57	
58	- **W2. Co-evolution section (§5.4) inflated by definitional anchor point.** [Both R1, R2] The ρ=−1.0 between σ_cross and |Δ| includes h0 where |Δ|=0.0 *by definition* (pure vs. pure = no difference). This is not a measurement but a tautology. Excluding h0, the remaining four points likely yield a much weaker correlation (R2 estimates ρ≈−0.40, p=0.75). The "paradox" framing rests on this inflated statistic. **Action needed**: report the correlation both with and without h0; reframe if the 4-point correlation is non-significant.
59	
60	- **W3. Novelty ceiling—standard tools on known phenomenon.** [R2, acknowledged by R1] The paper applies Jaccard similarity, Kruskal-Wallis tests, Spearman correlation, and BH-FDR correction—all textbook methods—to demonstrate that models with similar aggregate performance differ per-example. This is the *expected* outcome from the underspecification literature the paper itself cites. The finding confirms rather than overturns prior expectations. The taxonomy and the specific domain (hybrid architectures) add value, but the intellectual contribution is characterization, not discovery.
61	
62	### Major
63	
64	- **W4. Statistical power ceiling at n=5.** [Both R1, R2] With only 5 attention ratios, the minimum achievable two-tailed exact permutation p is 2/120 = 0.017. The paper's strongest claims achieve exactly this floor. This means: (a) no distinction between "strong" and "marginal" significance is possible, (b) any perfectly monotonic 5-point sequence gives p=0.017 regardless of effect size, (c) the Spearman test cannot distinguish genuine convergence from any monotonic confound (e.g., training duration, learning rate schedule correlation with attention ratio). The paper should acknowledge this power limitation more explicitly.
65	
66	- **W5. Training token confound inadequately addressed.** [R1] 340M models were trained on 20B tokens vs. 100B for 1.3B. The capacity bottleneck argument (§6) relies on the 340M rebound being parameter-driven, not training-duration-driven. The paper's counter-argument ("degradation would be uniform across ratios") is intuitive but not formally tested. A ratio-specific argument requires showing that training tokens don't interact with attention ratio, which is not demonstrated.
67	
68	- **W6. Two-scale limitation weakens Claim 2.** [R1] The capacity bottleneck claim (monotonic at 1.3B, rebound at 340M) rests on exactly two data points on the scale axis. This is a binary contrast, not a trend. The paper's Limitations section acknowledges this, but the main text (§6) presents the mechanism with more confidence than two data points warrant. exp-006 (7B) was cancelled, removing the possibility of validation.
69	
70	### Moderate
71	
72	- **W7. Retrieval-demand taxonomy "pre-specification" is soft.** [R2] The taxonomy was built from the initial 6-benchmark data, then "confirmed" on StoryCloze—which is structurally nearly identical to LAMBADA (narrative context → predict completion). A demanding confirmatory test would use a benchmark that is clearly retrieval-dependent but structurally dissimilar from LAMBADA (e.g., open-domain QA, fact verification). StoryCloze's confirmation is expected rather than surprising.
73	
74	- **W8. Per-example data coverage incomplete.** [R1] Table 4 reports Jaccard for only 4 of the 9 benchmarks. The two significant convergence benchmarks (LAMBADA and StoryCloze) should both have per-example decomposition to show whether Claim 3 holds on both anchors. StoryCloze per-example data appears absent.
75	
76	---
77	
78	## 5. Questions for Authors
79	
80	1. **Jaccard null**: What is the expected Jaccard under random set assignment for the observed helped/hurt set sizes? How many standard deviations below random are the observed values?
81	
82	2. **Co-evolution without h0**: What is the σ-vs-|Δ| Spearman correlation excluding the definitional h0 anchor? If non-significant, how does this change the §5.4 narrative?
83	
84	3. **StoryCloze per-example**: Was per-example decomposition (Jaccard, |Δ|) computed for StoryCloze? If so, does it confirm the low-Jaccard pattern? If not, why not?
85	
86	4. **Training token interaction**: Have you tested whether attention ratio interacts with training duration in the 340M models (e.g., by examining convergence trajectories at intermediate training checkpoints)?
87	
88	5. **Mamba2 provenance**: How were the Mamba2-attention hybrids obtained? Were they trained by the authors, sourced from Wang et al.'s extended set, or from another public repository? The paper is ambiguous.
89	
90	---
91	
92	## 6. Experiment Coverage Assessment
93	
94	Comparing against the full experiment plan (11 experiments):
95	
96	| Experiment | Status | Paper Coverage |
97	|---|---|---|
98	| exp-001 (Task taxonomy) | Complete | §4.1–4.2, Table 1 ✓ |
99	| exp-002 (Per-example multi-benchmark) | Claimed | Table 4 — but coverage limited to 4 benchmarks |
100	| exp-003 (Sample characterization) | Complete | §5.2, Table 5 ✓ |
101	| exp-004 (Attention patterns) | Claimed | §5.3, Table 6 — provenance uncertain |
102	| exp-005 (Mamba2 expansion) | Claimed | §4.3, Table 2 ✓ |
103	| exp-006 (7B evaluation) | Cancelled | Acknowledged in Limitations ✓ |
104	| exp-007 (340M rebound) | Complete | §6, Table 8 ✓ |
105	| exp-008 (Statistical framework) | Complete | §4.4, Table 3 ✓ |
106	| exp-009 (Wang differentiation) | Complete | §7, Table 9 ✓ |
107	| exp-010 (Co-evolution) | Complete | §5.4, Table 7 — but h0 issue |
108	| exp-011 (New benchmarks) | Complete | §4.1, Table 1 ✓ |
109	
110	**Notable gaps**: (1) StoryCloze per-example decomposition not reported despite being the second statistical anchor; (2) the planned figures (Jaccard heatmap, effect maps, attention heatmaps, dose-response plot) described in the experiment plan are absent from the paper—the submission appears to be tables-only with no figures, which significantly weakens visual communication of the core "paradox."
111	
112	---
113	
114	## 7. Minor Issues
115	
116	- **M1.** Table 1 reports "—" for σ values of several benchmarks (ARC-Easy, MMLU, Winogrande, HellaSwag, ARC-Challenge). These should be reported for completeness even if convergence is absent—the reader needs to see the actual variance levels.
117	- **M2.** The paper lacks any figures. The convergence-divergence co-evolution, the convergence trajectories, and the Jaccard heatmap would benefit enormously from visualization. A tables-only paper at EMNLP is unusual and a missed opportunity.
118	- **M3.** The abstract mentions "72+ hybrid models spanning four recurrence mechanisms" but the base model zoo from Wang et al. covers three; the fourth (Mamba2) is added by the authors. This should be clearer.
119	- **M4.** Missing Limitations section items: the paper does not discuss that all models share the same training data/recipe from Wang et al., which limits generalizability to production hybrids trained differently.
120	- **M5.** No Responsible NLP Research Checklist visible in the submission. EMNLP 2026 requires Sections A–E; absence risks desk reject.
121	
122	---
123	
124	## 8. Verdict and Actionable Path
125	
126	**Current level: 3.0 (Findings)**
127	
128	The paper makes a genuine analytical contribution: it is the first to quantify attention-induced convergence in hybrid architectures at the per-example level, with honest and transparent statistical methodology. However, it falls short of Main for three reasons: (1) limited novelty (characterization with standard tools), (2) critical methodological gaps (Jaccard null, co-evolution inflation), and (3) the findings confirm expected outcomes from the underspecification framework rather than producing surprising insights.
129	
130	**To reach Findings (solid 3.0–3.5):**
131	- Add Jaccard random-null comparison
132	- Fix §5.4 co-evolution (report with/without h0)
133	- Add StoryCloze per-example decomposition
134	- Include figures (at minimum: convergence trajectories, Jaccard heatmap)
135	- Complete the Responsible NLP Research Checklist
136	
137	**To reach Main (4.0):**
138	- All of the above, plus:
139	- Interventional experiments (attention head ablation, cross-architecture head swaps) to move from descriptive to mechanistic
140	- A third scale point or a formal test ruling out the training-token confound
141	- A structurally diverse confirmatory benchmark (not just StoryCloze)
142	- Ensemble-diversity practical validation (show that multi-architecture ensembles actually outperform single-architecture ensembles, as implied by Jaccard findings)
143	
144	---
145	
146	*Review conducted by R1 (Methods+Experiments) and R2 (Novelty+Related Work) with full roundtable convergence.*
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1100704a-e918-4f17-95ca-defb878cd4c6",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "b31a048a-ca05-4a81-83ec-cbba2eb11085",
  "sourceToolAssistantUUID": "1100704a-e918-4f17-95ca-defb878cd4c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-19T15:33:04.087Z_

Now let me also read the experiment details for exp-009 (Wang differentiation) and the wang_et_al_analysis to understand the positioning better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b31a048a-ca05-4a81-83ec-cbba2eb11085",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAq5EuvqSZuuB7Gy4GK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b255cc9-f9f0-44e6-a028-ed4fc2330c5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wUGCBSaDkt6iqk85NCJoi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18858,
      "cache_read_input_tokens": 31663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18858,
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

_source line 32 · 2026-05-19T15:33:05.554Z_

<details open><summary>🔧 Tool call — Read · `toolu_013eAKoNjLstxcjdspPntaLr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/wang_et_al_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b255cc9-f9f0-44e6-a028-ed4fc2330c5d",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAq5EuvqSZuuB7Gy4GK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bd7c2d4-3ca7-4392-9ec6-d11379e9ba08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wUGCBSaDkt6iqk85NCJoi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18858,
      "cache_read_input_tokens": 31663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18858,
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

_source line 33 · 2026-05-19T15:33:05.558Z_

<details><summary>↩ Tool result · `toolu_013eAKoNjLstxcjdspPntaLr`</summary>

```text
1	# Wang et al. 竞品分析报告
2	
3	## 论文基本信息
4	
5	- **标题**: A Systematic Analysis of Hybrid Linear Attention
6	- **arXiv**: 2507.06457 (2025-07-08)
7	- **作者**: Dustin Wang, Rui-Jie Zhu, Steven Abreu, Yong Shan, Taylor Kergan, Yuqi Pan, Yuhong Chou, Zheng Li, Ge Zhang, Wenhao Huang, Jason Eshraghian
8	- **机构**: UC Santa Cruz, ByteDance, University of Groningen, CASIA, PolyU, M-A-P
9	- **规模**: 72 个模型 (36×340M/20B tokens + 36×1.3B/100B tokens)，训练数据 FineWeb-Edu
10	- **开源**: HuggingFace 集合 m-a-p/hybrid-linear-attention-research
11	
12	---
13	
14	## 问题 a: 是否已报告完整 architecture × ratio × benchmark 交叉数据？
15	
16	**没有。** 他们的报告方式是聚合的：
17	
18	| 表格 | 内容 | 粒度 |
19	|------|------|------|
20	| Table 2 (340M) | 每架构最优 ratio + 6 个 LM benchmark 的分数 | arch × benchmark（仅最优 ratio） |
21	| Table 3 (1.3B) | 同上 | arch × benchmark（仅最优 ratio） |
22	| Table 4 | LM 聚合分数 | arch × ratio（平均分，无逐 benchmark 拆分） |
23	| Table 5 | Recall 聚合分数 | arch × ratio（RULER 平均分） |
24	| Table 6 | RULER 子任务拆分 | 仅 select models |
25	
26	**关键缺失**：不存在 "GatedDeltaNet 在 6:1 ratio 下 LAMBADA 得分" 这样的完整交叉表格。LM 性能只在 "最优 ratio" 下拆分到各 benchmark，其余 ratio 只报告聚合平均值。
27	
28	**他们的结论**：
29	- LM 性能跨 ratio 基本稳定（~0.55-0.57 平均），ratio 选择对 LM 影响不大
30	- Recall 性能随 full attention 比例增加而显著改善，尤其 3:1 以下
31	- 推荐 HGRN-2 或 GatedDeltaNet，ratio 3:1 到 6:1
32	
33	---
34	
35	## 问题 b: 是否发现 architecture-dependent hybridization effects？
36	
37	**是的，这是他们的核心发现之一。** 具体：
38	
39	1. **GatedDeltaNet**: standalone 最强（340M），但 hybridized 后优势缩小甚至消失
40	2. **HGRN-2**: standalone 不突出，但在 6:1 hybrid 下超越所有架构（含 Transformer），成为最佳选择
41	3. **RetNet**: fixed decay 导致 recall 能力极差，hybridization 帮助有限
42	4. **GLA**: 中等表现，3:1 时 recall 改善明显但 LM 性能无优势
43	
44	他们明确指出 "standalone scores are unreliable predictors of hybrid performance"，并分析了 selective gating 和 hierarchical recurrence 作为有利于 hybridization 的机制。
45	
46	**但他们的分析维度是 "哪个架构 hybrid 后最好"，不是 "不同架构在不同任务类型上的退化模式是否不同"。**
47	
48	---
49	
50	## 问题 c: 论文 focus
51	
52	他们的论文是一篇 **系统性 benchmark 研究**，focus 是：
53	
54	1. **主要目标**: 为从业者提供 hybrid linear attention 的架构选择指南
55	2. **核心问题**: 哪种 linear attention + 什么比例的 full attention = 最佳性价比
56	3. **分析框架**: 按 "generation"（vector state → fixed decay → data-dependent gate → delta rule）分类，解释机制差异
57	4. **不涉及**: 训练方法创新、fine-tuning、task-specific 退化分析、composition depth 理论
58	
59	本质上是 "practitioner's guide to hybrid architecture selection"。
60	
61	---
62	
63	## 问题 d: 训练设置
64	
65	| 项目 | 详情 |
66	|------|------|
67	| 数据 | FineWeb-Edu |
68	| 模型规模 | 340M (20B tokens) + 1.3B (100B tokens) |
69	| 架构数 | 6 核心 + DeltaNet（实际 7 个架构） |
70	| 比例 | pure, 24:1, 12:1, 6:1, 3:1 |
71	| 总模型数 | 72 |
72	| 变量控制 | 同数据、同 tokenizer、同训练框架 (fla + flame)、同超参（推测） |
73	| Benchmark | LM: ARC-c/e, HellaSwag, LAMBADA, OBQA, PIQA; Recall: RULER |
74	| 不含 | **MMLU, WinoGrande, BLiMP** |
75	
76	---
77	
78	## 我们数据的新颖性判断
79	
80	### 与 Wang et al. 的重叠
81	
82	| 维度 | Wang et al. | 我们 | 重叠度 |
83	|------|-------------|------|--------|
84	| 模型来源 | 同一批 m-a-p 模型 | 同一批 | 完全重叠 |
85	| 架构 | 7 个（含 HGRN, Hawk, GLA） | 3 个（GDN, RetNet, HGRN2） | 子集 |
86	| 比例 | pure, 24:1, 12:1, 6:1, 3:1 | 同 | 完全重叠 |
87	| LM Benchmark | ARC-c/e, HellaSwag, LAMBADA, OBQA, PIQA | LAMBADA, HellaSwag, ARC, **MMLU, WinoGrande, BLiMP** | 部分重叠 |
88	| 分析角度 | 架构选型指南（哪个最好） | **composition depth × architecture 交互效应** | 不重叠 |
89	
90	### 新颖性评估
91	
92	**数据层面**：中等新颖性
93	- Wang et al. 不含 MMLU/WinoGrande/BLiMP，我们有
94	- Wang et al. 不报告完整 arch × ratio × benchmark 交叉数据（只报聚合），如果我们报告完整交叉表，有增量
95	- 但原始 benchmark 跑分本身附加价值有限，因为任何人都可以复现
96	
97	**分析层面**：高新颖性（核心差异化）
98	- Wang et al. 的问题是 "which hybrid is best"（横向比较）
99	- 我们的问题是 "why do different architectures degrade differently across task types"（机制解释）
100	- composition depth 假设、task-agnostic 假设、functional segregation 假设的三假设对比框架完全不在 Wang et al. 的讨论范围内
101	- 他们观察到 "architecture-dependent hybridization effects" 但没有用 task complexity/composition depth 维度去解释这些差异
102	
103	### 结论
104	
105	**Wang et al. 提供了我们需要的基础设施（模型 + 初步 benchmark），但没有回答我们要问的问题。** 我们的增量价值不在于 "跑更多 benchmark"，而在于：
106	
107	1. **理论框架**: 用 composition depth 理论解释 architecture-ratio-task 三维交互
108	2. **新 benchmark 维度**: MMLU/WinoGrande/BLiMP 提供更宽的 task complexity 光谱
109	3. **分析深度**: 完整交叉数据 + 统计检验（Spearman ρ, permutation test），而非 "best ratio" 推荐
110	
111	**风险**: 如果我们的 composition depth 假设最终不成立（H_agnostic 胜出），那论文价值会大幅缩水，因为纯 benchmark 数据与 Wang et al. 高度重叠。
112	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bd7c2d4-3ca7-4392-9ec6-d11379e9ba08",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "d7a72f29-4555-47c8-afe6-e527a47c3a20",
  "sourceToolAssistantUUID": "2bd7c2d4-3ca7-4392-9ec6-d11379e9ba08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T15:33:06.366Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QgHojycdYaSAaR44T5C3hf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T135121/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7a72f29-4555-47c8-afe6-e527a47c3a20",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAq5EuvqSZuuB7Gy4GK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aaac24fe-71f3-4f09-a3e5-f6ce22317968",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wUGCBSaDkt6iqk85NCJoi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18858,
      "cache_read_input_tokens": 31663,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 31663,
          "cache_creation_input_tokens": 18858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18858,
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

_source line 35 · 2026-05-19T15:33:06.372Z_

<details><summary>↩ Tool result · `toolu_01QgHojycdYaSAaR44T5C3hf`</summary>

```text
1	---
2	dream_id: dream_20260519T135121
3	tier: best
4	overall_score: 1.5/5 — Resubmit after next cycle
5	timestamp: 2026-05-19T14:26:33.515739+00:00
6	---
7	
8	# R1 Review: Methods and Experiments
9	
10	**Paper:** "The Equalizer Paradox: Attention Induces Aggregate Convergence Through Architecture-Specific Mechanisms in Hybrid Recurrent Models"
11	**Venue:** EMNLP 2026 (ARR)
12	**Reviewer Focus:** Methods and Experiments
13	
14	---
15	
16	## Summary
17	
18	This paper analyzes 72 pretrained hybrid linear recurrent models from Wang et al. (2025) across 3 architectures (GatedDeltaNet, RetNet, HGRN2), 5 attention ratios, and 2 scales (340M, 1.3B), claiming an "equalizer paradox" whereby attention reduces cross-architecture performance variance at the aggregate level while per-example effects are nearly non-overlapping (Jaccard < 0.10). Three claims are made: (1) convergence strength scales with retrieval demand, (2) convergence is scale-dependent, and (3) the mechanism involves perplexity-based compensation. The statistical treatment on LAMBADA is commendably honest, but the paper is undermined by a critical discrepancy between actual and reported experimental results, single-benchmark significance, novelty overclaiming, and correlational evidence presented as causal mechanism.
19	
20	---
21	
22	## Strengths
23	
24	**S1: Rigorous statistical framework on the primary claim.** The paper applies bootstrap CIs (10,000 resamples), Bonferroni and BH-FDR correction across 6 benchmarks, exact permutation p-values, GDN-excluded sensitivity analysis, and effect sizes. The transparent admission that only LAMBADA survives Bonferroni correction (adjusted p=0.048) reflects statistical integrity uncommon in empirical NLP papers.
25	
26	**S2: Well-operationalized per-example methodology.** The helped/hurt set framework with pairwise Jaccard overlap is clean, interpretable, and provides a principled decomposition of aggregate trends. The convergence-divergence bridge (rho=-0.94, p=0.005) is an elegant analytical device.
27	
28	**S3: High reproducibility of the aggregate convergence analysis.** The model zoo is public, evaluation uses standard lm-evaluation-harness, and the aggregate convergence computation is straightforward to replicate. The actual exp-001 results confirm the LAMBADA convergence pattern (rho=-1.0, p=0.0167) and non-convergence on reasoning benchmarks.
29	
30	**S4: GDN confound handling is good practice.** The D004 confound (GDN hybrid-3-1 uses different num_heads) is identified, documented, and addressed through sensitivity analysis.
31	
32	**S5: The 340M vs. 1.3B contrast generates testable predictions.** The observation that 340M shows non-monotonic convergence while 1.3B is monotonic, combined with honest acknowledgment of the training token confound (20B vs. 100B tokens), provides a framework for future work.
33	
34	---
35	
36	## Weaknesses
37	
38	### W1 [CRITICAL]: The mechanistic results (Claim 3) contradict actual experimental findings.
39	
40	Section 4.5 reports that baseline perplexity strongly differentiates helped vs. hurt samples (Cohen's d=0.51-0.62, all p<0.001). However, the actual exp-003-p2 results state: "CONCLUSION: NEGATIVE. Pure-model perplexity does NOT distinguish helped vs hurt samples. All 3 architectures: p>0.05, |r|<0.05." Specifically: GDN p=0.209, r=-0.045; RetNet p=0.659, r=-0.017; HGRN2 p=0.248, r=-0.044. The means are nearly identical (GDN helped=3.370 vs. hurt=3.338 in log-loss space). The paper reports imagined results that are diametrically opposite to the actual experimental outcome. Claim 3 has no empirical support and has been falsified by the project's own experiments.
41	
42	### W2 [MAJOR]: Architecture expansion (Mamba2) and attention weight analysis are entirely imagined experiments.
43	
44	The project status shows exp-005 (architecture expansion) and exp-004 (attention weights) were never executed. The Mamba2 Jaccard matrix, attention entropy results, and attention position analysis have no corresponding experimental artifacts. Tables 5-9 report imagined rather than observed data.
45	
46	### W3 [MAJOR]: Single-benchmark statistical significance after correction -- and actual p-values are worse than reported.
47	
48	The actual exp-001 data shows raw p=0.0167 (two-tailed exact permutation with n=5 ratios, 3 architectures). Bonferroni-adjusted: 0.0167 x 6 = 0.100, which does NOT survive alpha=0.05 correction. The paper reports raw p=0.008 and Bonferroni=0.048 by using n=4 architectures (including imagined Mamba2 data). With the real data, no benchmark survives multiple comparison correction. The dose-response across benchmarks (rho=-0.89) is computed on n=6 points with zero individually significant benchmarks.
49	
50	### W4 [MAJOR]: The "paradox" is a known phenomenon, not a novel discovery.
51	
52	The observation that models with similar aggregate performance differ per-example is established in ensemble diversity (Krogh and Vedelsby 1995), underspecification (D'Amour et al. 2022), and dataset cartography (Swayamdipta et al. 2020). The Related Work section has only 3 paragraphs and approximately 8 references, far below EMNLP standards. The project's own D006 decision explicitly states "drop paradox narrative" yet the paper title and framing retain it.
53	
54	### W5 [MAJOR]: Training token confound undermines Claim 2.
55	
56	340M models trained on 20B tokens vs. 100B for 1.3B (5x difference). The "capacity bottleneck" explanation for the 340M rebound is entirely confounded with training duration. The paper claims "340M at matched training tokens still shows rebound pattern" but this was never tested. With only two scale points and a massive training confound, Claim 2 is unresolvable.
57	
58	---
59	
60	## Questions for Authors
61	
62	**Q1:** The exp-003-p2 summary states perplexity does NOT distinguish helped vs. hurt samples (all p>0.05, |r|<0.05). How do you reconcile this with Table 6 reporting Cohen's d=0.51-0.62 and all p<0.001? Were different perplexity computations used, or are the Table 6 values projections?
63	
64	**Q2:** The Retrieval Demand Index values (0.15-0.95) are described as "derived from published task taxonomies" without specifying which taxonomy. Were these values fixed before seeing results?
65	
66	**Q3:** How many of the 7 experiments in the paper have been fully executed with actual data, and how many report projected/imagined results?
67	
68	---
69	
70	## Minor Issues
71	
72	1. **p-value inconsistency:** Abstract p=0.003, Table 3 raw p=0.008, actual exp-001 data p=0.0167. Three different values for the same quantity.
73	
74	2. **Effect size computation is ill-defined.** Cohen's d=1.82 for "h0 vs h24 cross-arch std" -- cross-architecture std at a given ratio is a single scalar. How is Cohen's d computed from two scalars? Eta-squared=0.74 from ANOVA with n=5 data points has zero residual df unless bootstrapped (unexplained).
75	
76	3. **Table 5 columns undefined.** GDN Net and HGRN2 Net are not defined. The non-monotonic GDN trajectory is unexplained.
77	
78	4. **No figures.** A paper about co-evolving trends contains zero figures.
79	
80	5. **Zero compiled bibliography.** All citations render as [?]. This would result in desk-reject at ARR.
81	
82	6. **Title retains "Paradox" framing** despite D006 decision to drop it.
83	
84	---
85	
86	## Preliminary Scores
87	
88	| Dimension | Score | Rationale |
89	|-----------|-------|-----------|
90	| Soundness | 1.5/5 | Central mechanistic claim contradicted by actual data; multiple tables report imagined results; LAMBADA does not survive Bonferroni with real n=3 data |
91	| Excitement | 2.0/5 | Per-example decomposition has merit; helped/hurt Jaccard framework is clean; but core finding is known in other literatures |
92	| Reproducibility | 2.0/5 | Aggregate analysis reproducible from public models; majority of reported results are imagined projections, not measurements |
93	| **Overall Assessment** | **1.5/5** | **Resubmit after next cycle** |
94	| Confidence | 4/5 | Examined actual experimental artifacts, decision logs, and experiment summaries alongside paper |
95	
96	**Rationale for 1.5:** The paper presents fabricated experimental results as actual findings (Claim 3 perplexity mechanism contradicted by exp-003-p2; Mamba2 and attention weight analyses never executed). The only real finding (LAMBADA convergence at n=3) does not survive multiple comparison correction with actual data. The experiments need to be actually run, and if the real results match exp-003-p2 (negative), the narrative requires fundamental restructuring -- likely not achievable in a single ARR cycle.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aaac24fe-71f3-4f09-a3e5-f6ce22317968",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "93317638-17d3-4d9e-a1b7-b6ac9cf36d22",
  "sourceToolAssistantUUID": "aaac24fe-71f3-4f09-a3e5-f6ce22317968",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-19T15:33:10.023Z_

Now let me look at the experiment plan to understand what was actually executed vs. imagined in the latest (best) paper draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93317638-17d3-4d9e-a1b7-b6ac9cf36d22",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAqWxjDjJZFq7RCfoAW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e62a9240-c0da-4347-a94e-6eeed17a67a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZCm2n6UP7d4HL3XGN4vrC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5371,
      "cache_read_input_tokens": 50521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5371,
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

_source line 37 · 2026-05-19T15:33:11.959Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01US1gQeG1mukGUXxdSiHRuc`</summary>

```json
{
  "pattern": "**/experiment_plan.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e62a9240-c0da-4347-a94e-6eeed17a67a4",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAqWxjDjJZFq7RCfoAW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c44f20c9-af13-4795-b85a-c715035b7dd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZCm2n6UP7d4HL3XGN4vrC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5371,
      "cache_read_input_tokens": 50521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5371,
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

_source line 38 · 2026-05-19T15:33:11.971Z_

<details><summary>↩ Tool result · `toolu_01US1gQeG1mukGUXxdSiHRuc`</summary>

```text
experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c44f20c9-af13-4795-b85a-c715035b7dd3",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "2f2fecef-3a39-4785-a559-ab1bce4a937f",
  "sourceToolAssistantUUID": "c44f20c9-af13-4795-b85a-c715035b7dd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T15:33:12.647Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01D2cR236aop7Fbaq25sQrTv`</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f2fecef-3a39-4785-a559-ab1bce4a937f",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAqWxjDjJZFq7RCfoAW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70a7e594-0e1d-40a7-bd50-4aa5f6eaec44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZCm2n6UP7d4HL3XGN4vrC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5371,
      "cache_read_input_tokens": 50521,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5371
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 50521,
          "cache_creation_input_tokens": 5371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5371,
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

_source line 40 · 2026-05-19T15:33:12.663Z_

<details><summary>↩ Tool result · `toolu_01D2cR236aop7Fbaq25sQrTv`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'entrainment_gated_ft'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70a7e594-0e1d-40a7-bd50-4aa5f6eaec44",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "42e8edc1-c7b3-4501-86f3-aeaa063799bc",
  "sourceToolAssistantUUID": "70a7e594-0e1d-40a7-bd50-4aa5f6eaec44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T15:33:15.437Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LVA84nYdeXPhu78bFojwp4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42e8edc1-c7b3-4501-86f3-aeaa063799bc",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAqzDpDvk8BRkeAKFmz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aef51298-9122-4acc-af64-4a1a73ab4622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5MCsQgKcZDccRNzkkZouS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 55892,
      "output_tokens": 88,
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
          "output_tokens": 88,
          "cache_read_input_tokens": 55892,
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

_source line 42 · 2026-05-19T15:33:15.443Z_

<details><summary>↩ Tool result · `toolu_01LVA84nYdeXPhu78bFojwp4`</summary>

```text
1	experiments:
2	  # === Claim 1: Equalizer Effect (convergence across architectures) ===
3	
4	  - id: exp-001
5	    registry_id: exp-001
6	    claim: 1
7	    title: "Task-specificity characterization of equalizer effect"
8	    description: >
9	      Compute cross-architecture variance (std) at each attention ratio for all 6 benchmarks.
10	      Known: only LAMBADA shows significant convergence (p<0.05). Goal: build principled
11	      task taxonomy (retrieval-dependent vs reasoning-dependent) explaining WHY convergence
12	      is task-specific. LAMBADA = last-word retrieval from context; HellaSwag/ARC = multi-step
13	      reasoning. Show the dichotomy is a feature (task-type modulation), not a limitation.
14	    priority: P0
15	    type: analysis
16	    gpu_budget_hours: 0
17	    deps: []
18	    data_source: "existing summary_all_1.3b.csv + 340M results + cross_scale_convergence output"
19	    pass_fail: "Clear task-type dichotomy with principled taxonomy; convergence correlates with retrieval demand"
20	    reviewer_risk: "Risk A — reframed per Reviewer warning: single-task convergence → task-specificity as positive finding"
21	
22	  - id: exp-002
23	    claim: 1
24	    title: "Multi-benchmark per-example analysis (task-specificity validation)"
25	    description: >
26	      Re-run lm-eval on 1.3B models with --log_samples for HellaSwag, ARC-easy, ARC-challenge.
27	      Two goals: (a) confirm task-specificity — per-example convergence absent on reasoning tasks,
28	      (b) characterize HOW attention affects per-example behavior on non-converging tasks (random
29	      noise vs systematic but architecture-specific). Strengthens Claim 1 regardless of outcome.
30	    priority: P0
31	    type: experiment
32	    gpu_budget_hours: 20
33	    deps: [exp-001]
34	    pass_fail: "Per-example data collected for ≥3 benchmarks; task-specificity of per-example mechanism confirmed or refuted"
35	    reviewer_risk: "Risk B — outcome determines Claim 1 scope: cross-task vs retrieval-specific equalizer"
36	    note: "Budget revised to 20h per Reviewer data audit: need --log_samples for 10×340M (RetNet+HGRN2) + 3×1.3B (GDN h3-1/h6-1/h24-1). Uses freed exp-006 budget."
37	
38	  # === Claim 2: Scale-Dependent Convergence ===
39	
40	  - id: exp-006
41	    claim: 2
42	    title: "7B model evaluation — CANCELLED (unavailable)"
43	    description: >
44	      Wang et al. only have 340M + 1.3B (72 models total). Paper Limitations explicitly excludes
45	      10B+. No 7B models exist. Budget reallocated to exp-002/004/005.
46	    priority: cancelled
47	    type: experiment
48	    gpu_budget_hours: 0
49	    deps: []
50	    pass_fail: "N/A — 7B unavailable, confirmed 2026-05-19"
51	
52	  - id: exp-007
53	    claim: 2
54	    title: "340M rebound mechanism analysis (upgraded: compensate 7B absence)"
55	    description: >
56	      Deep analysis of 340M non-monotonic rebound at attn=8. Per-example comparison with 1.3B
57	      at same attention ratio to identify which samples diverge. Characterize rebound samples.
58	      With 7B unavailable, this becomes the primary vehicle for Claim 2 depth — show the
59	      binary contrast (340M partial vs 1.3B complete) has mechanistic explanation, not just
60	      correlation with scale. Analyze training token count (20B vs 100B) as confound vs scale.
61	    priority: P0
62	    type: analysis
63	    gpu_budget_hours: 2
64	    deps: [exp-002]
65	    data_source: "existing 340M results + new 1.3B per-example data"
66	    pass_fail: "Rebound mechanism identified with principled explanation; 340M vs 1.3B contrast characterized beyond aggregate metrics"
67	    note: "Upgraded from P1 to P0 after 7B cancellation. May need 340M per-example rerun (2h GPU)."
68	
69	  # === Claim 3: Architecture-Specific Mechanism (Equalizer Paradox) ===
70	
71	  - id: exp-003
72	    registry_id: exp-003
73	    claim: 3
74	    title: "Helped/hurt sample characterization"
75	    description: >
76	      For each architecture's helped/hurt samples on LAMBADA, compute:
77	      (a) target token frequency (unigram rank in training data proxy),
78	      (b) context length (token count),
79	      (c) last-sentence complexity (perplexity under baseline),
80	      (d) topic/domain distribution.
81	      Test whether architecture-specific sample subsets differ on these features.
82	    priority: P0
83	    type: analysis
84	    gpu_budget_hours: 1
85	    deps: []
86	    data_source: "existing lambada per-example logprob data"
87	    pass_fail: "≥1 feature significantly differentiates helped vs hurt samples (p<0.01), AND features differ across architectures"
88	    status_note: >
89	      Phase 1 (surface features) DONE: all non-significant within-arch (p>0.2).
90	      Phase 2 (perplexity) DONE: within-arch perplexity also non-significant (r_rb≈-0.04, p>0.2).
91	      PASS on second criterion: cross-arch KW significant (hurt p=0.0005, helped p=0.020).
92	      Different archs help/hurt samples with systematically different baseline difficulty profiles.
93	      Both negative within-arch results are informative (rules out trivial explanations).
94	      Cross-arch finding strengthens Claim 3 (architecture-specificity is structured, not random).
95	
96	  - id: exp-004
97	    claim: 3
98	    title: "Attention weight extraction and visualization"
99	    description: >
100	      Extract attention weight patterns from hybrid models (h3-1 config) for all 3 architectures.
101	      Analyze: (a) which positions attention focuses on, (b) whether attention patterns correlate
102	      with helped/hurt sample identity, (c) cross-architecture attention pattern similarity.
103	    priority: P0
104	    type: experiment
105	    gpu_budget_hours: 4
106	    deps: [exp-003]
107	    pass_fail: "Attention pattern differences documented; correlation with per-example effects > 0.3"
108	    note: "Upgraded P1→P0: mechanistic evidence is critical for Claim 3 and Reviewer Concern C"
109	
110	  # === Reviewer Concern Mitigation ===
111	
112	  - id: exp-005
113	    claim: 1
114	    title: "Architecture expansion check"
115	    description: >
116	      Search Wang et al. model zoo and other sources for additional hybrid architectures
117	      (Mamba/Mamba2 hybrids, RWKV hybrids, etc.). If found, evaluate on LAMBADA to test
118	      whether convergence generalizes beyond GDN/RetNet/HGRN2.
119	    priority: P1
120	    type: experiment
121	    gpu_budget_hours: 6
122	    deps: []
123	    pass_fail: "≥1 additional architecture evaluated and convergence pattern confirmed/denied"
124	
125	  - id: exp-008
126	    registry_id: exp-008
127	    claim: 1
128	    title: "Statistical robustness framework"
129	    description: >
130	      Implement bootstrap CIs for convergence metrics. Multi-comparison correction
131	      (Bonferroni/FDR) across benchmarks. Sensitivity analysis: does conclusion hold
132	      if GDN (with D004 confound) is excluded? Report effect sizes (Cohen's d / η²).
133	    priority: P0
134	    type: analysis
135	    gpu_budget_hours: 0
136	    deps: [exp-001]
137	    pass_fail: "All core claims survive with GDN excluded; bootstrap 95% CIs don't cross zero"
138	
139	  - id: exp-009
140	    registry_id: exp-009
141	    claim: 1
142	    title: "Wang et al. explicit differentiation"
143	    description: >
144	      Formal side-by-side comparison: what Wang et al. report vs our analysis.
145	      Extract their exact convergence-related statements. Quantify the increment:
146	      (a) they don't compute cross-arch std trajectories, (b) no per-example analysis,
147	      (c) no scale-dependent convergence characterization, (d) no mechanistic analysis.
148	    priority: P0
149	    type: analysis
150	    gpu_budget_hours: 0
151	    deps: []
152	    data_source: "Wang et al. arXiv 2507.06457"
153	    pass_fail: "Clear 4-point differentiation documented"
154	
155	  - id: exp-010
156	    registry_id: exp-010
157	    claim: 3
158	    title: "Convergence-divergence bridge analysis"
159	    description: >
160	      For LAMBADA, plot aggregate convergence curve alongside per-example divergence metrics
161	      (Jaccard, net effect asymmetry) as function of attention ratio. Show that convergence
162	      and divergence co-evolve—more attention = more aggregate convergence BUT also more
163	      architecture-specific per-example effects. Core visualization for Claim 3 (underspecification in hybrid architectures).
164	    priority: P0
165	    type: analysis
166	    gpu_budget_hours: 0
167	    deps: [exp-001, exp-003]
168	    pass_fail: "Convergence-divergence co-evolution demonstrated with significant correlation"
169	
170	  # === Dream W1 Mitigation: Additional High-Retrieval Benchmarks ===
171	
172	  - id: exp-011
173	    registry_id: exp-011
174	    claim: 1
175	    title: "Additional high-retrieval benchmarks (Dream W1 response)"
176	    description: >
177	      Dream review: LAMBADA alone does not survive Bonferroni (p=0.017 > α=0.0083).
178	      Need a second significant anchor point on a high-retrieval task.
179	      Run 1.3B models on additional retrieval-heavy benchmarks available in lm-eval:
180	      (a) StoryCloze (context completion, structurally similar to LAMBADA),
181	      (b) BoolQ (passage-based yes/no, context retrieval),
182	      (c) COPA (causal reasoning from short narratives).
183	      Compute cross-arch std at each attention ratio for each benchmark.
184	      Test for convergence (Spearman + exact permutation, two-tailed).
185	      If ANY shows significant convergence → second anchor established, W1 substantially mitigated.
186	    priority: P0
187	    type: experiment
188	    gpu_budget_hours: 8
189	    deps: []
190	    pass_fail: "≥1 additional benchmark shows significant convergence (p<0.05 two-tailed)"
191	    note: "CRITICAL for Findings acceptance. Dream best case = 2.5 without this. Added post-D006."
192	
193	# GPU budget summary (revised 2026-05-19, post Dream D006):
194	# P0 experiments: exp-002 (20h) + exp-003 (1h) + exp-004 (4h) + exp-007 (2h) + exp-011 (8h) = 35 GPU-hours
195	# P1 experiments: exp-005 (6h) = 6 GPU-hours
196	# P0 analyses (no GPU): exp-001, exp-008, exp-009, exp-010
197	# Cancelled: exp-006 (7B unavailable)
198	# Total: ~41 GPU-hours
199	# Within project allocation (1× RTX PRO 6000)
200	# exp-011 is highest priority — single most impactful for venue acceptance
201	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aef51298-9122-4acc-af64-4a1a73ab4622",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "ebe50098-91a1-42b8-a887-8b699184bc17",
  "sourceToolAssistantUUID": "aef51298-9122-4acc-af64-4a1a73ab4622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-19T15:33:19.633Z_

Now let me check what the latest dream review (the best-case one that scored 3.0) says, and look at the actual data artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebe50098-91a1-42b8-a887-8b699184bc17",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCArBp5CoyhouZUhKjng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e433b6c-2b55-494f-add8-315869206272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RDDu6zhjgigDo5rdd7gdK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3395,
      "cache_read_input_tokens": 56246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3395,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-19T15:33:20.616Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A5fPpeRre1AAZEZa4ii5Tf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/lm_eval_1.3b_results.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e433b6c-2b55-494f-add8-315869206272",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCArBp5CoyhouZUhKjng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3df8e2f0-4ff2-4689-9e28-8299ea5d5ead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RDDu6zhjgigDo5rdd7gdK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3395,
      "cache_read_input_tokens": 56246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3395,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-19T15:33:20.620Z_

<details><summary>↩ Tool result · `toolu_01A5fPpeRre1AAZEZa4ii5Tf`</summary>

```text
1	# lm_eval Benchmark Results (1.3B Scale, 100B Tokens)
2	
3	**Date:** 2026-05-18
4	**Server:** westb-48145
5	**Script:** `/root/entrainment_gated_ft/run_lmeval_clean.py` (no monkeypatch)
6	**Settings:** batch_size=16, bf16, lm_eval 0.4.12, fla 0.5.0, transformers 5.8.1
7	
8	## Results
9	
10	| Task | Metric | GDN Pure | Transformer | GDN Hybrid-12-1 | RetNet Pure |
11	|------|--------|----------|-------------|-----------------|-------------|
12	| lambada_openai | acc | **0.5430** | 0.4805 | 0.5337 | pending |
13	| lambada_openai | ppl | **8.26** | 11.46 | 8.73 | pending |
14	| hellaswag | acc_norm | 0.6080 | 0.5924 | **0.6103** | pending |
15	| winogrande | acc | 0.6077 | **0.6180** | 0.6117 | pending |
16	| arc_easy | acc | **0.7125** | 0.7113 | 0.6995 | pending |
17	| arc_challenge | acc_norm | **0.3925** | **0.3925** | 0.3857 | pending |
18	| mmlu | acc | **0.2606** | 0.2358 | 0.2541 | pending |
19	
20	## Key Findings
21	
22	1. **GDN Pure outperforms Transformer baseline** on 5/6 tasks (lambada, hellaswag, arc_easy, arc_challenge, mmlu). Only winogrande favors the transformer.
23	2. **GDN Hybrid-12-1** performs between pure GDN and transformer on most tasks, with the best hellaswag score.
24	3. **lambada ppl** shows the largest gap: GDN pure (8.26) vs transformer (11.46), a 28% relative improvement.
25	
26	## Notes
27	
28	- **RetNet Pure** checkpoint was corrupted during initial download (176/266 weight tensors all zeros in shard 1). Re-downloading from ModelScope. Results pending.
29	- piqa was dropped because the dataset was not in the HuggingFace cache on the offline server.
30	- Config fixes applied: GDN `allow_neg_eigval=True` for beta computation; RetNet `tie_weights()` for shared embeddings.
31	- fla `_tied_weights_keys` patched from list to dict format for transformers 5.8.1 compatibility.
32	
33	## Result JSON Files
34	
35	- `/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json` (132MB)
36	- `/root/entrainment_gated_ft/lm_eval_clean/transformer_1.3B_baseline.json` (123MB)
37	- `/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-hybrid-12-1.json` (132MB)
38	- `/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure.json` (pending re-download + eval)
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3df8e2f0-4ff2-4689-9e28-8299ea5d5ead",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "8a4d7611-a42e-4731-862a-c9400a036160",
  "sourceToolAssistantUUID": "3df8e2f0-4ff2-4689-9e28-8299ea5d5ead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-19T15:33:20.912Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NY6ssHESZVU9QT3hb86Yur`</summary>

```json
{
  "pattern": "**/exp-001/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a4d7611-a42e-4731-862a-c9400a036160",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCArBp5CoyhouZUhKjng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52d36fad-e1d7-4556-8fcb-4ac46e3ad375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RDDu6zhjgigDo5rdd7gdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3395,
      "cache_read_input_tokens": 56246,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3395
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 56246,
          "cache_creation_input_tokens": 3395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3395,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-19T15:33:20.922Z_

<details><summary>↩ Tool result · `toolu_01NY6ssHESZVU9QT3hb86Yur`</summary>

```text
artifacts/exp-001/data/task_specificity_results.csv
artifacts/exp-001/chart/task_specificity_figure_info.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52d36fad-e1d7-4556-8fcb-4ac46e3ad375",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "861f6dff-bd08-4425-a626-d2e3a3182d62",
  "sourceToolAssistantUUID": "52d36fad-e1d7-4556-8fcb-4ac46e3ad375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-19T15:33:23.835Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AQrUiFgpmCtCXbLJjoPhoy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/exp-001/data/task_specificity_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "861f6dff-bd08-4425-a626-d2e3a3182d62",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCArb92cK7S9KEDuhHwC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db6e8333-4cf2-4c05-b622-11ad5e540e00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANePKTGv6qE2Rj6pjbJm9N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4725,
      "cache_read_input_tokens": 56246,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4725
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 56246,
          "cache_creation_input_tokens": 4725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4725,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T15:33:23.840Z_

<details><summary>↩ Tool result · `toolu_01AQrUiFgpmCtCXbLJjoPhoy`</summary>

```text
1	benchmark,taxonomy_category,std_pure_1.3B,std_pure_340M,std_h24-1_1.3B,std_h24-1_340M,std_h12-1_1.3B,std_h12-1_340M,std_h6-1_1.3B,std_h6-1_340M,std_h3-1_1.3B,std_h3-1_340M,spearman_rho_1.3B,p_value_1.3B,significant_1.3B,spearman_rho_340M,p_value_340M,significant_340M
2	LAMBADA,Retrieval-dependent,0.0240,0.0246,0.0162,0.0109,0.0136,0.0173,0.0061,0.0108,0.0049,0.0151,-1.000,0.0167,True,-0.500,0.4500,False
3	HellaSwag,Reasoning-dependent,0.0117,0.0087,0.0086,0.0228,0.0095,0.0098,0.0092,0.0111,0.0118,0.0133,+0.300,0.6833,False,+0.400,0.5167,False
4	ARC-C,Reasoning-dependent,0.0096,0.0137,0.0077,0.0147,0.0077,0.0115,0.0126,0.0111,0.0132,0.0088,+0.600,0.3500,False,-0.900,0.0833,False
5	WinoGrande,Reasoning-dependent,0.0067,0.0043,0.0212,0.0035,0.0097,0.0105,0.0076,0.0054,0.0078,0.0131,+0.100,0.9500,False,+0.800,0.1333,False
6	ARC-E,Mixed,0.0100,0.0315,0.0195,0.0256,0.0168,0.0379,0.0046,0.0307,0.0013,0.0209,-0.700,0.2333,False,-0.500,0.4500,False
7	MMLU,Mixed,0.0092,0.0071,0.0053,0.0042,0.0084,0.0057,0.0071,0.0081,0.0040,0.0025,-0.700,0.2333,False,-0.300,0.6833,False
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db6e8333-4cf2-4c05-b622-11ad5e540e00",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "95ffdee0-5db5-49f8-b93c-7a742568c6b8",
  "sourceToolAssistantUUID": "db6e8333-4cf2-4c05-b622-11ad5e540e00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-19T15:33:26.963Z_

Now I have a comprehensive understanding of the project. Let me now produce the review as R2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95ffdee0-5db5-49f8-b93c-7a742568c6b8",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAroRTh7P6Ag9ZkUgmZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "800ab5f2-9887-4b67-9d35-a72f64d6274e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLzYe9RjGdivCpnMZQgyoT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 60971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 777,
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

_source line 51 · 2026-05-19T15:33:27.517Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GcnGAGk1Ei4b8AGA7Zc2gL`</summary>

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
  "parentUuid": "800ab5f2-9887-4b67-9d35-a72f64d6274e",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAroRTh7P6Ag9ZkUgmZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73a37432-baaa-48ca-930c-f804afe66324",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLzYe9RjGdivCpnMZQgyoT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 60971,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 777
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 60971,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 777,
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

_source line 52 · 2026-05-19T15:33:27.523Z_

<details><summary>↩ Tool result · `toolu_01GcnGAGk1Ei4b8AGA7Zc2gL`</summary>

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
  "parentUuid": "73a37432-baaa-48ca-930c-f804afe66324",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "af582cd3fea4c7abc",
  "type": "user",
  "uuid": "03330600-2fd7-4c0a-9565-a5fcab0b0014",
  "sourceToolAssistantUUID": "73a37432-baaa-48ca-930c-f804afe66324",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-19T15:35:43.938Z_



Now I have all the materials needed to produce a rigorous R2 review. Let me synthesize my findings.

---

## R2 Review: Novelty and Related Work

**Paper:** "Task-Dependent Convergence and Per-Example Divergence in Attention-Augmented Linear Recurrent Models"
**Venue:** EMNLP 2026 (ARR)
**Reviewer Focus:** Novelty and Related Work

---

### Paper Summary

The paper uses 72 publicly available hybrid recurrent models from Wang et al. (2025) spanning three architectures (GatedDeltaNet, RetNet, HGRN2), five attention ratios, and two scales (340M, 1.3B) to study how attention affects cross-architecture behavioral diversity. The "best-case" draft additionally claims Mamba2 expansion (4th architecture) and attention weight analysis, though the experiment log shows these have not been executed. Three claims are advanced: (1) task-dependent convergence on retrieval tasks (LAMBADA rho=-1.0, p=0.017; StoryCloze rho=-1.0, p=0.017; BH-FDR adj p=0.042 on pre-specified retrieval subset), (2) scale-dependent convergence (1.3B monotonic, 340M non-monotonic rebound), and (3) per-example divergence under aggregate convergence (Jaccard < 0.10, KW p=0.0005 cross-architecture). The paper explicitly frames itself as a "community analysis paper" applying known analytical techniques to a specific domain.

---

### Novelty Assessment

**Research questions: Low-to-moderate novelty.**

The central question -- "do models with similar aggregate performance differ per-example?" -- is the definition of underspecification (D'Amour et al. 2022). The paper acknowledges this. The more specific question -- "does adding attention to linear recurrent models induce convergence, and is it task-dependent?" -- is moderately novel in its specificity, but Wang et al. (2025) already qualitatively observed convergence. The paper's contribution is quantifying what Wang et al. noted in 1-2 sentences. This is a valid scientific contribution (quantification matters), but the intellectual distance is short.

**Methods/analyses: Low novelty.**

The analytical toolkit is entirely standard: Spearman rank correlation, exact permutation tests, Jaccard similarity, Kruskal-Wallis tests, Benjamini-Hochberg FDR, bootstrap confidence intervals. No new method is proposed. The per-example helped/hurt decomposition with Jaccard is clean and well-operationalized but not methodologically novel -- it is a direct application of set-overlap measures used routinely in ensemble diversity literature (Kuncheva & Whitaker 2003).

**Sufficiency for EMNLP 2026:**

The paper is honest that its contribution is "analytical depth on public infrastructure." This is a legitimate contribution type -- the "community analysis" / "meta-analysis" framing is appropriate. However, EMNLP Main acceptance (~21%) requires either (a) surprising findings that change how the community thinks, or (b) substantial methodological contribution. This paper offers neither. The finding that per-example divergence exists under aggregate convergence is the *expected* prediction from underspecification theory. The task-dependency finding (retrieval > reasoning) is intuitive given that attention's known strength is direct token-to-token retrieval. The scale-dependency finding rests on two data points. For Findings, the bar is lower, but the contribution must still be "solid" -- and the statistical fragility (see below) weakens even this case.

**Domain application alone:**

The paper positions its contribution as "quantifying a well-documented phenomenon in a new domain." This is a recognized contribution type, but its value depends on whether the domain application reveals something unexpected. Here:
- Per-example divergence (Jaccard < 0.10) is expected from underspecification theory -- CONFIRMED, not surprising.
- Task-dependency of convergence is intuitive from attention's known computational role -- CONFIRMED, not surprising.
- The decoupling of aggregate convergence and per-example divergence timescales (Jaccard saturates immediately at 4% attention while aggregate sigma decreases gradually) is the most interesting finding, but the paper's own internal review (D008) reveals this was initially mis-analyzed as "co-evolution" and corrected to "decoupling" after the correlation was found to be inflated by a degenerate anchor point.

The strongest novelty claim is the specific quantitative characterization in hybrid recurrent architectures -- what the exact Jaccard values are, how they vary by task type, and how they relate to attention ratio. This is useful empirical knowledge for the hybrid architecture community. Whether it clears the Findings bar depends heavily on execution quality and statistical rigor.

---

### Related Work Assessment

**Comprehensiveness: Adequate but could be stronger.**

The best-case draft cites ~20 references spanning hybrid architectures, underspecification, ensemble diversity, dataset cartography, and attention analysis. This is a reasonable set. The Related Work section is organized into three clear paragraphs (hybrid architectures, underspecification/diversity, attention analysis).

**Missing references -- important gaps:**

1. **Fort et al. (2019), "Deep Ensembles: A Loss Landscape Perspective."** Cited in the paper framing but absent from the actual best-case paper draft. This is the most directly relevant work on per-example disagreement in deep ensembles and should be cited.

2. **McCoy et al. (2020), "BERTs of a feather do not generalize together."** Also cited in the framing as a key related work but absent from the draft. Demonstrates per-example disagreement across BERT fine-tuning runs -- directly relevant precedent.

3. **Arora et al. (2024)** on attention's role in recurrent architectures (training dynamics). Cited in the paper summary but absent from the draft. This is the closest work on understanding attention in hybrid models.

4. **Vig (2019), Jain & Wallace (2019), Wiegreffe & Pinter (2019)** -- attention interpretability papers. The paper includes an attention pattern analysis section but cites only Vaswani et al. (2017) for attention analysis history. The attention interpretability debate (are attention weights explanations?) is directly relevant to Section 5.3's claims about attention concentration correlating with per-example effects.

5. **De et al. (2024), Griffin.** Another hybrid architecture missing from the Related Work. RecurrentGemma is cited (which builds on Griffin), but Griffin itself is not.

6. **Poli et al. (2023), Hyena** and **Fu et al. (2023), H3** -- earlier hybrid architectures that motivate the design space. Their absence weakens the historical narrative.

7. **Csordas et al. (2024)** or related work on per-example analysis specific to SSMs/state-space models. If such work exists, its absence is a gap; if it does not exist, the paper should note this explicitly to strengthen its novelty claim.

8. **Teney et al. (2022), "Evading the Simplicity Bias"** and related work on shortcut learning -- relevant to the finding that surface features don't predict helped/hurt status.

**Positioning relative to Wang et al.:**

The differentiation is well-executed. The side-by-side comparison table (Table 9 in the appendix) lists five concrete analytical dimensions absent from Wang et al. The "community analysis paper" framing is appropriate and honest. However, there is a tension: the paper depends entirely on Wang et al.'s infrastructure (models, training recipes, controlled variables) while claiming analytical independence. This is not a flaw per se -- the medical meta-analysis analogy is apt -- but it does limit the ceiling on novelty. The paper cannot claim any insight about model design or training because it controls neither.

The framing could be improved by more explicitly engaging with what Wang et al. *did* observe about convergence. Currently the paper says Wang et al. made a "qualitative observation" in "1-2 sentences." A more thorough treatment would quote those sentences, explain what they did and did not claim, and show precisely where our analysis begins where theirs ends.

**Differentiation from ensemble diversity literature:**

Adequate but thin. The paper cites Krogh & Vedelsby (1995) and Kuncheva & Whitaker (2003) and positions its contribution as "applying these ideas to a specific, practically important domain." This is honest. But the paper does not engage deeply enough with *why* the hybrid architecture domain might yield different insights than classical ensemble diversity. In ensemble diversity, diverse members are trained with different initializations/hyperparameters/data subsets -- diversity is *constructed*. Here, diversity arises from architectural mechanism differences under identical training conditions. This distinction is important and underemphasized.

---

### Framing and Positioning

**Narrative: Improved from earlier drafts, but still fragile.**

The evolution from "Equalizer Paradox" (earlier dream) to "Task-Dependent Convergence and Per-Example Divergence" (current) is a significant improvement. The paper no longer overclaims novelty by calling a known phenomenon a "paradox." The "community analysis paper" framing is appropriate.

However, the narrative has a structural weakness: the three claims are not tightly connected. Claim 1 (task-dependent convergence) and Claim 3 (per-example divergence) are somewhat independent findings that happen to use the same data. The bridge between them (Section 5.4, convergence-divergence co-evolution / decoupling) was found to be statistically inflated (D008: the 5-point Spearman rho=-0.70, p=0.23 was driven by a degenerate pure=0 anchor; excluding it gives rho=-0.40, p=0.75). The best-case draft still presents a "co-evolution" table with rho=-1.0 (p=0.017) between sigma and |Delta|, which includes the definitional h0 point where |Delta|=0.0 by construction. This is methodologically problematic and reviewers will catch it.

**Underspecification framing: Adds value, but risks being seen as window-dressing.**

Framing the per-example divergence finding as "underspecification in hybrid architectures" is legitimate -- D'Amour et al. (2022) is the right theoretical frame. But the framing adds more to the literature review than to the analysis. The paper does not extend underspecification theory; it applies the concept descriptively. A reviewer sympathetic to the framing will see this as appropriate positioning; an unsympathetic reviewer will see it as borrowing prestige from a high-profile JMLR paper to dress up a straightforward analysis.

**Practical implications: Weak.**

The paper claims that findings "inform architecture selection for practitioners." This is overstated given the evidence. The concrete practical takeaway is: "on retrieval tasks at 1.3B, architectural choice matters less; on reasoning tasks, it matters more." This is useful but not actionable -- practitioners already make architecture choices based on many factors (speed, memory, training stability) that this paper does not address. The ensemble diversity implication (different hybrid architectures may yield diversity benefits) is stated but not validated -- no ensemble experiment is conducted.

---

### Scores

**Soundness: 3/5**

The statistical methodology is honest and transparent -- the three-layer multiple comparison correction is commendable, and the exact permutation tests are appropriate for n=5. However: (1) the co-evolution section includes a definitional anchor point inflating the correlation; (2) the Jaccard values are reported without a random-null baseline, making "nearly non-overlapping" uninterpretable; (3) the Mamba2 expansion and attention weight analysis appear in the best-case draft but have not been executed (exp-004, exp-005 not done per the experiment log); (4) LAMBADA and StoryCloze achieving significance under BH-FDR (m=5) but not under full correction (m=9) is honestly reported but leaves the statistical case thin.

**Excitement: 2/5**

The findings confirm rather than overturn prior expectations. Per-example divergence under aggregate convergence is the expected prediction from underspecification theory. Task-dependency of attention-induced convergence is intuitive. The decoupling finding (Jaccard saturates immediately while aggregate sigma decreases gradually) is the most interesting result but is undermined by the statistical issues noted above. No surprising insight emerges that would change how the community designs or evaluates hybrid architectures.

**Reproducibility: 5/5**

All models are public. Evaluation uses standard lm-evaluation-harness. Statistical tests are fully specified. A reader could reproduce every claimed result. This is exemplary.

**Overall Assessment: 2.5 / 5 (Borderline Findings)**

---

### Strengths

- **Exemplary statistical transparency.** Three-layer multiple comparison correction with honest reporting of all three, including the full-correction failure (m=9: 0 significant). The exact permutation test with explicit minimum resolution (2/120 = 0.017) is better statistical practice than most empirical NLP papers.

- **Appropriate epistemic calibration.** The paper does not claim to discover per-example divergence; it claims to quantify it in a new domain. Attention analysis is labeled "descriptive, not causal." These are correct framings. The Limitations section is substantive and honest.

- **Clean per-example decomposition framework.** The helped/hurt set identification with pairwise Jaccard is well-operationalized, interpretable, and provides a principled decomposition. The gradient from low Jaccard (retrieval tasks) to higher Jaccard (reasoning tasks) is a coherent finding.

- **Effective differentiation from Wang et al.** Five concrete analytical dimensions with a side-by-side comparison table. The "community analysis paper" framing is appropriate and the medical meta-analysis analogy is convincing.

- **Pre-specified confirmatory design.** The retrieval-demand taxonomy was established before evaluating new benchmarks (StoryCloze, BoolQ, COPA). StoryCloze's rho=-1.0 provides genuine confirmatory evidence, not post-hoc fishing.

- **Perfect reproducibility.** Public models, standard tools, fully specified tests.

- **Informative negative results.** Surface features and baseline perplexity failing to predict helped/hurt status within architectures, combined with significant cross-architecture differences (KW p=0.0005), rules out trivial explanations and establishes the phenomenon as structured but opaque.

### Weaknesses

- **W1 [Major]: Limited novelty -- standard tools on a known phenomenon.** The paper applies textbook statistical methods (Jaccard, Spearman, KW, BH-FDR) to confirm the expected prediction of underspecification theory in a specific domain. No new method is proposed. No surprising finding emerges. The task-dependency of convergence is intuitive given attention's known retrieval role. The per-example divergence is the *definition* of underspecification. The contribution is characterization, not discovery, and the characterization does not yield actionable insights beyond what a practitioner would already expect.

- **W2 [Major]: Missing Jaccard random-null baseline.** The headline "Jaccard < 0.10" is uninterpretable without comparison to expected Jaccard under random set assignment of the same sizes. For helped sets of ~500 out of ~5000 samples, random Jaccard is approximately |A intersect B| / |A union B| where |A|=|B|=500, N=5000. Expected overlap under independence is ~50/950 = ~0.053. An observed Jaccard of 0.07 may be only marginally above chance. Without this baseline, the entire Claim 3 narrative ("nearly non-overlapping") could be an artifact of set size.

- **W3 [Major]: Co-evolution / decoupling section is statistically unsound.** Section 5.4 / Table 7 reports rho=-1.0 (p=0.017) between sigma_cross and |Delta|. This includes h0 where |Delta|=0.0 by definition (comparing pure models to themselves). This is not a measurement but a tautology that anchors the correlation. The project's own D008 decision acknowledges this: excluding h0, rho=-0.40, p=0.75. The best-case draft retains "co-evolution" framing (Table 7 caption, Section 5.4 text) despite the internal decision to switch to "decoupling." This is a significant inconsistency between the internal analysis and the paper.

- **W4 [Major]: Several results in the best-case draft appear to be projections rather than measurements.** The experiment log shows exp-004 (attention weight analysis) and exp-005 (Mamba2 expansion) have not been executed. Yet Section 4.3 reports Mamba2 results with specific sigma values and Jaccard ranges, and Section 5.3 reports attention entropy correlations (r=0.31-0.40) and focus distance ranges. If these are projections/plans rather than measurements, they must not appear as results.

- **W5 [Moderate]: Related work gaps.** Fort et al. (2019), McCoy et al. (2020), and Arora et al. (2024) are cited in the project framing documents but absent from the paper draft. The attention interpretability literature (Jain & Wallace 2019, Wiegreffe & Pinter 2019) is absent despite Section 5.3's attention pattern analysis. These are significant omissions for a paper that positions itself relative to ensemble diversity and attention analysis.

- **W6 [Moderate]: StoryCloze as confirmation is structurally expected.** StoryCloze (narrative context -> predict ending) is structurally very similar to LAMBADA (passage context -> predict last word). A more demanding confirmatory test would use a retrieval-dependent benchmark structurally dissimilar from LAMBADA (e.g., open-domain QA, fact verification, passage retrieval). StoryCloze's confirmation adds statistical weight (second p=0.017) but limited intellectual weight.

- **W7 [Moderate]: Practical implications overstated.** The paper claims findings "inform architecture selection for practitioners" but provides no actionable framework. The ensemble diversity implication (multi-architecture ensembles may benefit from low Jaccard) is suggested but not validated experimentally.

- **W8 [Minor]: No figures.** A paper about co-evolving trajectories, convergence curves, and heatmaps contains zero figures in the best-case draft. This significantly weakens communication and is unusual for EMNLP.

### Questions for Authors

1. **Jaccard null baseline:** What is the expected Jaccard similarity under random set assignment for the observed helped/hurt set sizes? How many standard deviations above random are the observed Jaccard values? If the gap is small, how does this change the Claim 3 narrative?

2. **Co-evolution without h0:** What is the sigma-vs-|Delta| Spearman correlation excluding the definitional h0 anchor point? If it is rho=-0.40 (p=0.75) as your internal analysis (D008) suggests, how does this change the Section 5.4 narrative?

3. **Mamba2 and attention analysis provenance:** Have exp-004 (attention weight extraction) and exp-005 (Mamba2 expansion) been executed? If the results in Sections 4.3 and 5.3 are projections, they should be clearly marked as such or removed.

4. **Why not validate the ensemble implication?** Given that the per-example Jaccard finding directly predicts that multi-architecture ensembles should outperform single-architecture ensembles, a simple majority-vote ensemble experiment on LAMBADA would be a compelling validation. Was this considered?

5. **Retrieval-demand taxonomy justification:** The classification of benchmarks into retrieval/mixed/reasoning categories is central to Claim 1, but the criteria are informal. Could you formalize the retrieval-demand dimension (e.g., proportion of questions answerable from the passage alone) and show it correlates with convergence strength?

6. **Broader architectural coverage:** Wang et al. also include GLA, HGRN, Hawk, and DeltaNet models. Why were these excluded? If included, do they support the convergence pattern?

### Missing References

1. Fort, S., Hu, H., & Lakshminarayanan, B. (2019). Deep ensembles: A loss landscape perspective. NeurIPS.
2. McCoy, R.T., Pavlick, E., & Linzen, T. (2020). Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference. ACL.
3. Arora, S., et al. (2024). Simple linear attention language models balance the recall-throughput tradeoff. ICML.
4. Jain, S. & Wallace, B.C. (2019). Attention is not explanation. NAACL.
5. Wiegreffe, S. & Pinter, Y. (2019). Attention is not not explanation. EMNLP.
6. De, S., et al. (2024). Griffin: Mixing gated linear recurrences with local attention for efficient language models. ICML.
7. Poli, M., et al. (2023). Hyena hierarchy: Towards larger convolutional language models. ICML.
8. Teney, D., et al. (2022). Evading the simplicity bias: Training a diverse set of models discovers solutions with superior OOD generalization. CVPR.

---

### Summary Justification for 2.5 (Borderline Findings)

The paper demonstrates good scientific practice: honest statistical reporting, appropriate epistemic calibration, and clean operationalization. The per-example decomposition framework applied to hybrid recurrent architectures is a genuine empirical contribution. However, the novelty ceiling is low -- the findings confirm expected predictions from existing theory using standard methods. The statistical case, while honestly presented, is thin (two benchmarks under pre-specified subset correction, zero under full correction). The Jaccard null-baseline omission, the co-evolution inflation, and the apparent inclusion of unexecuted experiments in the draft are methodological concerns that weaken the case. The paper is borderline between "useful empirical characterization for Findings" and "needs more substance to clear even the Findings bar." I land at 2.5, which reflects that addressing the Jaccard null, fixing the co-evolution section, and completing the claimed experiments could push it to a solid 3.0. In its current state, it does not quite reach Findings quality.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03330600-2fd7-4c0a-9565-a5fcab0b0014",
  "isSidechain": true,
  "agentId": "af582cd3fea4c7abc",
  "requestId": "req_011CbCAs5ScqaZbdiE3G2fN4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "507d1540-4605-4e58-a22d-c62bbe485d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNJcF7KQSoTcmVQE7onzUa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 61748,
      "output_tokens": 5345,
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
          "output_tokens": 5345,
          "cache_read_input_tokens": 61748,
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
