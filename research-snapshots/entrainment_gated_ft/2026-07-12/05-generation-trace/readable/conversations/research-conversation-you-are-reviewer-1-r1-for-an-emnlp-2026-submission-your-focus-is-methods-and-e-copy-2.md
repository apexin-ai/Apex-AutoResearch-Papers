# Research conversation: You are Reviewer 1 (R1) for an EMNLP 2026 submission. Your focus is **Methods and Experiments**. You must produce a rigo

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-afdcfe4979fa0befe.jsonl`
- **Structured JSON:** [`81c3d854435d5fdce7ff.json`](../../sessions/81/81c3d854435d5fdce7ff.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

56 recorded events

### User

_source line 1 · 2026-05-19T15:32:08.666Z_

You are Reviewer 1 (R1) for an EMNLP 2026 submission. Your focus is **Methods and Experiments**. You must produce a rigorous, calibrated review. EMNLP 2026 uses ARR unified review with Overall Assessment on a 1–5 half-point scale (5=Award top 2.5%, 4=Main conference, 3=Findings, 2=Resubmit, 1=Do not resubmit). Main acceptance ~21%.

## Paper Summary
Title: "Task-Dependent Convergence and Per-Example Divergence in Attention-Augmented Linear Recurrent Models"
Submitted to EMNLP 2026 (anonymous).

The paper uses 72 publicly available hybrid recurrent models (Wang et al. 2025 model zoo: GatedDeltaNet, RetNet, HGRN2; 5 attention ratios h0/h3/h6/h12/h24; 2 scales 340M/1.3B) to analyze how attention affects cross-architecture behavioral diversity at the per-example level. Three claims:

1. **Task-dependent convergence**: On retrieval-heavy LAMBADA, attention reduces cross-architecture std by 79% (ρ=−1.0, permutation p=0.017). Suggestive trends on BoolQ (ρ=−0.8, p=0.083), StoryCloze (ρ=−0.7, p=0.117). No convergence on reasoning tasks. MMLU excluded as GDN artifact (sign flip when GDN removed).

2. **Scale-dependent convergence**: 1.3B shows monotonic convergence; 340M shows non-monotonic rebound at h8 (35-40% std increase vs h6 minimum). Rebound is architecture-specific (RetNet +55%, GDN +30%, HGRN2 +20%). Rebound samples are harder (longer context p=0.03, higher baseline ppl p=0.01).

3. **Per-example divergence**: Despite aggregate convergence, pairwise Jaccard of helped/hurt sets < 0.10 on LAMBADA. Surface features/baseline ppl don't predict helped/hurt within architecture (all p>0.2). Cross-architecture comparison shows systematically different difficulty profiles (KW p=0.0005 for hurt, p=0.02 for helped). Convergence-divergence "scissors" co-evolution (ρ=−0.95, p=0.05, n=4 points).

Additional analyses: Attention weight descriptive analysis (cosine sim=0.35 across architectures, r=0.22 attention-effect correlation). Bootstrap CI [−1.0, −0.7] with 100% valid resamples ρ<0. BH-FDR: no benchmark survives at α=0.05 (LAMBADA adj-p=0.075).

Paper is 8 pages (within limit), has Limitations section, References section. No Responsible NLP checklist visible in PDF.

## Experiment Design Reference (from review_context.yaml)
The full experiment plan had these experiments:
- exp-001: Task-specificity characterization (6→9 benchmarks) — covered in paper
- exp-002: Multi-benchmark per-example analysis — covered in paper  
- exp-003: Helped/hurt sample characterization — covered in paper
- exp-004: Attention weight extraction — covered in paper (§4.5)
- exp-005: Architecture expansion check — found 0 additional architectures (n=3 is hard limit) — acknowledged in Limitations
- exp-006: 7B evaluation — CANCELLED (unavailable) — acknowledged
- exp-007: 340M rebound analysis — covered in paper (§4.3)
- exp-008: Statistical robustness framework — covered in paper (§4.2)
- exp-009: Wang et al. differentiation — covered in Discussion
- exp-010: Convergence-divergence bridge — covered in §4.6
- exp-011: Additional benchmarks (StoryCloze/BoolQ/COPA) — covered in paper

Coverage: All non-cancelled experiments appear represented.

## Your Task
Evaluate the paper on these dimensions with detailed justification:

### Soundness (1-5)
- Are the statistical methods appropriate? 
- Is the experimental design valid?
- Are claims well-supported by evidence?
- Are there methodological flaws?

Key issues to consider:
- n=3 architectures, n=5 attention ratios → very low statistical power for Spearman tests
- LAMBADA is the ONLY benchmark with uncorrected p<0.05; nothing survives BH-FDR
- Bootstrap CI has 11.25% degenerate resamples — is the CI trustworthy?
- The "scissors" co-evolution has n=4 data points (p=0.05 borderline)
- Scale comparison confounded by training tokens (20B vs 100B)
- Attention weight analysis: r=0.22 is very weak
- GDN-excluded sensitivity: removing 1 of 3 architectures is removing 33% of data
- Are the Jaccard values appropriately baselined? What's the expected Jaccard under null?

### Reproducibility (1-5)
- Is there enough detail to reproduce?
- Are models publicly available?
- Is code promised?

### Excitement (1-5)
- How interesting/important are the findings?
- Do the findings advance our understanding?

### Overall Assessment (1-5, half-point scale)
Calibrate to EMNLP 2026: 4=Main (~top 21%), 3=Findings, 2=Resubmit.

### Strengths (bulleted)
### Weaknesses (bulleted)
### Questions for Authors
### Minor Issues

Format your output as a structured review with all sections above. Be rigorous but fair. The paper is honest about its limitations — credit that, but also assess whether the evidence actually supports the claims at a venue-worthy level.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "6aee14b2-d850-46d1-95c4-1cdb6d96d1ea",
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

_source line 2 · 2026-05-19T15:32:08.671Z_

```json
{
  "parentUuid": "6aee14b2-d850-46d1-95c4-1cdb6d96d1ea",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
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
  "uuid": "ba5a2ac5-3816-43dc-abe8-1e36aec74db2",
  "timestamp": "2026-05-19T15:32:08.671Z",
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

_source line 3 · 2026-05-19T15:32:12.988Z_



I'll start by reading the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba5a2ac5-3816-43dc-abe8-1e36aec74db2",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAmGCMjtCj1wRA9UrpJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb0225b5-282b-471c-bbfe-05c78ee15cb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5LWLtXLGbssuE8azpa5f2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15989,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15989,
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

_source line 4 · 2026-05-19T15:32:13.572Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BspTkdwnoGf9YYgTHxueZS`</summary>

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
  "parentUuid": "eb0225b5-282b-471c-bbfe-05c78ee15cb2",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAmGCMjtCj1wRA9UrpJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a97743b-258e-40ea-a1ea-34535f9f63b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5LWLtXLGbssuE8azpa5f2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15989,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15989
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15989,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15989,
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

_source line 5 · 2026-05-19T15:32:13.577Z_

<details><summary>↩ Tool result · `toolu_01BspTkdwnoGf9YYgTHxueZS`</summary>

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
  "parentUuid": "9a97743b-258e-40ea-a1ea-34535f9f63b6",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "f56eec79-e8cf-45b0-a1f7-22d84efd77f2",
  "sourceToolAssistantUUID": "9a97743b-258e-40ea-a1ea-34535f9f63b6",
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

_source line 6 · 2026-05-19T15:32:16.725Z_



Let me gather all the relevant materials for this review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f56eec79-e8cf-45b0-a1f7-22d84efd77f2",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAmdRoP7suL58dMja8Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f83a97b-4f57-4c6a-a71a-cf7e9156b528",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQjfXFKxQokuxTHQ543oLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 7 · 2026-05-19T15:32:17.250Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_017VppbKwb7ndUDsvqzWaJFU`</summary>

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
  "parentUuid": "7f83a97b-4f57-4c6a-a71a-cf7e9156b528",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAmdRoP7suL58dMja8Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fce25860-4217-4932-a60a-2a1b67c665fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQjfXFKxQokuxTHQ543oLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 8 · 2026-05-19T15:32:17.300Z_

<details><summary>↩ Tool result · `toolu_017VppbKwb7ndUDsvqzWaJFU`</summary>

```text
{"result":"# 项目 entrainment_gated_ft 概况\n\n## 实验状态 (11 个)\n\n- **exp-010**: DONE (success) — \n- **exp-011**: RUNNING — \n- **exp-001**: DONE (success) — \n- **exp-008**: DONE (success) — \n- **exp-003-p2v2**: PREPARING (killed) — \n- **exp-003-p2**: DONE (negative) — \n- **exp-003**: DONE (negative) — \n- **exp-009**: DONE (success) — \n- **eval_340m_retnet_hgrn2**: DONE (success) — \n- **hgrn2_eval_h3_1**: DONE (success) — \n- **hgrn2_eval_1_3b_all**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-011 | Cross-architecture variance on additional retrieval-dependent benchmarks (StoryCloze, BoolQ, COPA, PIQA, SciQ) decreases monotonically with attention ratio, providing a second statistically significant anchor (exact permutation p<0.05, two-tailed) beyond LAMBADA after Bonferroni correction | — | — | — |\n\n## 待处理\n- exp-003-p2v2: Helped samples have higher pure-model perplexity (model uncertain → attention helped) while hurt samples have lower perplexity (model confident → attention interfered), with architecture-specific patterns across GDN/RetNet/HGRN2. Retry with HGRN2 monkey-patch fix for _tied_weights_keys AttributeError.（准备中）\n\n## 近期结论\n- **exp-010** (success): Aggregate convergence (cross-arch std decreasing with attention ratio) and per-example divergence (low Jaccard of helped/hurt sets) co-evolve as attention ratio increases on LAMBADA — demonstrating underspecification: architectures converge in aggregate performance while helping/hurting almost entirely different samples ← 基于 exp-001\n- **exp-001** (success): Cross-architecture variance (std) on retrieval-dependent tasks decreases monotonically with attention ratio at 1.3B scale, while reasoning-dependent tasks show no convergence — establishing task-specificity as a principled feature of the equalizer effect, not a limitation\n  [task_specificity_results](/api/workspace-files/projects/entrainment_gated_ft/artifacts/exp-001/data/task_specificity_results.csv) | [task_specificity_figure](/api/workspace-files/projects/entrainment_gated_ft/artifacts/exp-001/chart/task_specificity_figure_info.txt)\n- **exp-008** (success): Replacing scipy.stats.spearmanr asymptotic p-values with exact permutation tests (n=5, 120 permutations, two-tailed) corrects the spurious p=1.4e-24 bug; expected: LAMBADA raw p≈0.017, Bonferroni adj-p≈0.100 (not significant), confirming need for additional benchmarks ← 基于 exp-001\n\n## 趋势\n成功 6 / 负向 2 / 失败 0 / 共 9\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-48145: 无 GPU 信息\n\n## 告警\n- hgrn2_eval_1_3b_all: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fce25860-4217-4932-a60a-2a1b67c665fa",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "0db35613-7c48-47e9-9a60-7db8391fb1ff",
  "sourceToolAssistantUUID": "fce25860-4217-4932-a60a-2a1b67c665fa",
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

_source line 9 · 2026-05-19T15:32:17.783Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LUBTSJHM9AkUjjZnUgg9J3`</summary>

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
  "parentUuid": "0db35613-7c48-47e9-9a60-7db8391fb1ff",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAmdRoP7suL58dMja8Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb25905c-6972-48a9-b4a2-a7138c4f7280",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQjfXFKxQokuxTHQ543oLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 10 · 2026-05-19T15:32:17.792Z_

<details><summary>↩ Tool result · `toolu_01LUBTSJHM9AkUjjZnUgg9J3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/report.md\", \"content\": \"# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp-011 | Cross-architecture variance on additional retrieval-dependent benchmarks (StoryCloze, BoolQ, COPA, PIQA, SciQ) decreases monotonically with attention ratio, providing a second statistically significant anchor (exact permutation p<0.05, two-tailed) beyond LAMBADA after Bonferroni correction | — | — | — |\\n\\n## 待处理\\n- exp-003-p2v2: Helped samples have higher pure-model perplexity (model uncertain → attention helped) while hurt samples have lower perplexity (model confident → attention interfered), with architecture-specific patterns across GDN/RetNet/HGRN2. Retry with HGRN2 monkey-patch fix for _tied_weights_keys AttributeError.（准备中）\\n\\n## 近期结论\\n- **exp-010** (success): Aggregate convergence (cross-arch std decreasing with attention ratio) and per-example divergence (low Jaccard of helped/hurt sets) co-evolve as attention ratio increases on LAMBADA — demonstrating underspecification: architectures converge in aggregate performance while helping/hurting almost entirely different samples ← 基于 exp-001\\n- **exp-001** (success): Cross-architecture variance (std) on retrieval-dependent tasks decreases monotonically with attention ratio at 1.3B scale, while reasoning-dependent tasks show no convergence — establishing task-specificity as a principled feature of the equalizer effect, not a limitation\\n  [task_specificity_results](/api/workspace-files/projects/entrainment_gated_ft/artifacts/exp-001/data/task_specificity_results.csv) | [task_specificity_figure](/api/workspace-files/projects/entrainment_gated_ft/artifacts/exp-001/chart/task_specificity_figure_info.txt)\\n- **exp-008** (success): Replacing scipy.stats.spearmanr asymptotic p-values with exact permutation tests (n=5, 120 permutations, two-tailed) corrects the spurious p=1.4e-24 bug; expected: LAMBADA raw p≈0.017, Bonferroni adj-p≈0.100 (not significant), confirming need for additional benchmarks ← 基于 exp-001\\n\\n## 趋势\\n成功 6 / 负向 2 / 失败 0 / 共 9\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestb-48145: 无 GPU 信息\\n\\n## 告警\\n- hgrn2_eval_1_3b_all: 已被终止 — unknown\\n\", \"total_chars\": 2179, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb25905c-6972-48a9-b4a2-a7138c4f7280",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "9b550ef8-7042-43f0-823e-69064ec475a9",
  "sourceToolAssistantUUID": "cb25905c-6972-48a9-b4a2-a7138c4f7280",
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

_source line 11 · 2026-05-19T15:32:18.423Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RHYGEJvBni3J8ykLNEakNx`</summary>

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
  "parentUuid": "9b550ef8-7042-43f0-823e-69064ec475a9",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAmdRoP7suL58dMja8Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b1b462a-30dd-4c12-89ca-852e636ab0fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQjfXFKxQokuxTHQ543oLJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15989,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1448
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 272,
          "cache_read_input_tokens": 15989,
          "cache_creation_input_tokens": 1448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1448,
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

_source line 12 · 2026-05-19T15:32:18.431Z_

<details><summary>↩ Tool result · `toolu_01RHYGEJvBni3J8ykLNEakNx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/ROADMAP.md\", \"content\": \"# entrainment_gated_ft — Research Dashboard\\n\\n> 最后更新: 2026-05-19 15:10 UTC | 更新原因: exp-010 完成(success) + exp-011 运行中(4/16)\\n\\n## 核心方向\\n**Quantifying per-example divergence under aggregate convergence in hybrid recurrent architectures**. Attention 使不同 recurrent 架构在 retrieval tasks 上趋同，但 per-example 效应几乎不重叠（Jaccard < 0.10）。这是 underspecification 现象在 hybrid 架构中的具体表现。详见 paper_framing.md。\\n\\n## 当前阶段\\n**Research 阶段** — Post-Dream 重大调整（D006），exp-011 关键实验运行中\\n\\n## 战略状态\\n- **Dream best case = 2.5/5 (Borderline Findings)**\\n- 四个 Major weakness 已识别并纳入 plan（W1-W4）\\n- 目标：EMNLP 2026 Findings (3.0)，stretch: Main\\n- DDL: ARR June 2026 (~June 15)，距今 ~27 天\\n- Dream dream_20260519T143201 正在自动重试中（imagining 阶段）\\n\\n## 当前进展\\n- ✅ MVP FAIL → pivot to equalizer effect（D005）\\n- ✅ 26 models × 6 benchmarks 完整评估\\n- ✅ exp-001: Task-specificity（PASS，LAMBADA 唯一显著，连续谱 framing）\\n- ✅ exp-009: Wang et al. differentiation（PASS，4 维度分析完成）\\n- ✅ exp-003: Surface features 全阴性 → 排除 trivial 解释；跨架构 KW 显著\\n- ✅ exp-003-p2: Perplexity 分析（negative within-arch，但跨架构 KW p=0.0005 for hurt）\\n- ✅ exp-008: Statistical robustness（exact permutation p, BCa CI, GDN-excluded sensitivity）\\n- 🔄 **exp-011: Additional retrieval benchmarks — 运行中**（4/16 模型完成，~8min/model，预计 UTC 16:40 完成）\\n- ⚠️ StoryCloze 不可用，xstorycloze_en **已批准追加**（exp-011 主批次后，lambada_standard 不追加）\\n- ✅ exp-010: Convergence-divergence bridge（success — σ 5x单调下降，Jaccard平坦~0.10，paradoxical coexistence）\\n- 🔜 exp-002: Multi-benchmark per-example（20h GPU）\\n- 🔜 exp-004: Attention weight analysis（4h GPU）\\n\\n## 近期任务（按优先级）\\n- [ ] 等 exp-011 批量完成（~UTC 16:40）→ 收敛分析（Spearman + exact permutation）\\n- [ ] exp-011 后追加 xstorycloze_en 评估（~2h GPU，16 模型，Director 已批准）\\n- [x] 修复 experiment_plan.yaml registry_id 映射 ✅\\n- [x] 修复 exp-001 registry p-value ✅（0.008 → 0.0167 two-tailed）\\n- [x] exp-010: Convergence-divergence bridge ✅（paradoxical coexistence confirmed）\\n- [ ] exp-002: Multi-benchmark per-example（20h GPU）\\n- [ ] exp-004: Attention weight analysis（4h GPU）\\n- [ ] 论文写作启动（目标 June 5-7，Paper Agent）\\n\\n## GPU 预算\\n- 分配：westb-48145 cuda:0（RTX PRO 6000 × 1）\\n- 当前：**exp-011 占用中**（批量评估 4/16，~8min/model，cron 监控中）\\n- P0 GPU 总需：~35h（exp-002 20h + exp-011 ~9h含xstorycloze + exp-004 4h + exp-007 2h）\\n- P1 GPU：exp-005 6h\\n\\n## 已知风险\\n- COPA 仅 100 测试样本，Spearman 分析不稳定，不作主要证据\\n- Transformer baseline 必须从收敛分析中排除\\n- 如 4 个新 benchmark + xstorycloze_en 均不显著 → W1 无法解决，Findings 路径受阻\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D008 | 2026-05-19 | exp-010 \\\"co-evolution\\\" → \\\"decoupling\\\" framing：per- | exp-010 |\\n| D008 | 2026-05-19 | Claim 3 叙事修正：decoupling 替代 co-evolution/paradox（退化点膨胀） | exp-010 |\\n| D007 | 2026-05-19 | MMLU blacklisted from convergence evidence — GDN-e | exp-008 |\\n| D006 | 2026-05-19 | Dream best case 2.5/5 → 重大 framing 调整：放弃 \\\"paradox\\\" | exp-001, exp-003 |\\n| D005 | 2026-05-19 | MVP 原始 entrainment 假设 FAIL，pivot to Equalizer Effe | eval_340m_retnet_hgrn2, hgrn2_eval_h3_1 |\\n| D004 | 2026-05-18 | GDN hybrid-3-1 存在 attn.num_heads confound（16 vs 32 | — |\\n| D003 | 2026-05-18 | 预注册 benchmark composition depth 赋值（结果出来前锁定，不可事后调整） | — |\\n| D002 | 2026-05-18 | 1.3B 也无 function composition ICL 能力，MVP 从 syntheti | — |\\n| D001 | 2026-05-18 | MVP Direct variant 340M 全模型 random-chance → 先跑 log | — |\\n\\n\", \"total_chars\": 3184, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b1b462a-30dd-4c12-89ca-852e636ab0fb",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "13491f66-bcc3-4708-bcc2-11a734cd04ee",
  "sourceToolAssistantUUID": "0b1b462a-30dd-4c12-89ca-852e636ab0fb",
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

_source line 13 · 2026-05-19T15:32:21.820Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Ms4V9XVJQFUXLU3tB3ATrQ`</summary>

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
  "parentUuid": "13491f66-bcc3-4708-bcc2-11a734cd04ee",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAmyypBMNeZiodi99ku",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d9c171a-6503-45ee-9bfb-dd562faac203",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMLvzRV8QuoUctdy5x9iB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4171,
      "cache_read_input_tokens": 17437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4171,
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

_source line 14 · 2026-05-19T15:32:21.834Z_

<details><summary>↩ Tool result · `toolu_01Ms4V9XVJQFUXLU3tB3ATrQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/paper_framing.md\", \"content\": \"# Paper Framing — entrainment_gated_ft\\n\\n> Revised 2026-05-19 after Dream review (best case = 2.5/5). Major reframing: drop \\\"paradox\\\" narrative, engage related work, add retrieval benchmarks.\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Findings (via ARR)\\n- Stretch: EMNLP 2026 Main\\n- Deadline: ARR June 2026 cycle (submission ~June 15)\\n\\n## Paper Type\\nEmpirical analysis paper — quantifying a known phenomenon (per-example divergence under aggregate convergence) in a specific important domain (hybrid recurrent architectures)\\n\\n## Core Claims (3 条)\\n\\n### Claim 1: Task-Dependent Convergence\\nAdding attention layers to different linear recurrent architectures (GatedDeltaNet, RetNet, HGRN2) induces aggregate performance convergence whose strength varies with task type. Convergence is strongest on LAMBADA (ρ=-1.0, p=0.017 two-tailed, cross-arch std drops 79%), suggestive on ARC-Easy (ρ=-0.7, p=0.233, underpowered at n=5), and absent on reasoning-heavy tasks. **Critical need**: a second high-retrieval benchmark showing significant convergence to survive multi-comparison correction.\\n\\n### Claim 2: Scale-Dependent Convergence\\nThe convergence effect requires sufficient model capacity: monotonically complete at 1.3B (ρ=-1.0, p=0.017 two-tailed) but only partial at 340M with a non-monotonic rebound. Only two scale points (Wang et al. cap at 1.3B). Frame as binary contrast, not extrapolatable trend.\\n\\n### Claim 3: Per-Example Divergence Under Aggregate Convergence\\nDespite aggregate convergence, attention acts on nearly non-overlapping sample subsets per architecture (pairwise Jaccard < 0.10). This is an instance of the well-documented underspecification phenomenon (D'Amour et al. 2022) applied to hybrid architectures. Our contribution is **quantifying** it in this specific context, NOT claiming to discover it. Surface features AND baseline model perplexity do not differentiate helped/hurt samples within an architecture — the effect is opaque to standard features. However, cross-architecture comparison reveals systematic differences in baseline difficulty profiles of affected samples (Kruskal-Wallis p=0.0005 for hurt samples), confirming the architecture-specificity is structured, not random noise.\\n\\n**Decoupling finding (exp-010, D008)**: Aggregate convergence and per-example divergence are **decoupled** — they operate on different timescales w.r.t. attention ratio:\\n- Aggregate σ decreases **gradually** across 5 attention levels (0.024 → 0.016 → 0.014 → 0.006 → 0.005)\\n- Per-example Jaccard **saturates immediately** at the first attention level (4%) and remains flat (~0.095)\\n- Net asymmetry (HGRN2 net positive vs GDN/RetNet net negative) **increases** with attention (0.013 → 0.040)\\n- Implication: minimal attention creates full per-example architecture-specificity; gradual increases only affect aggregate convergence\\n\\n⚠️ Do NOT frame as \\\"co-evolution.\\\" Spearman ρ=-0.70 (p=0.23) is inflated by degenerate pure=0 point (Jaccard=NaN→0); excluding it: ρ=-0.40, p=0.75. The correct narrative is **decoupling**, which is a stronger finding: aggregate metrics converge while per-example dynamics increasingly diverge.\\n\\n## Story Spine\\n\\n### Problem\\nHybrid architectures mixing linear recurrence with full attention are becoming standard. While Wang et al. (2025) provide an extensive model zoo, the community lacks quantitative understanding of how attention affects cross-architecture behavioral diversity at the per-example level.\\n\\n### Related Work Positioning (CRITICAL — Dream W2)\\nThe observation that models with similar aggregate performance differ per-example is well-established:\\n- **Ensemble diversity**: Krogh & Vedelsby (1995), Kuncheva & Whitaker (2003) — diverse ensemble members err on different examples by construction\\n- **Underspecification**: D'Amour et al. (2022) — equivalent aggregate performance masks prediction-level differences\\n- **Dataset cartography**: Swayamdipta et al. (2020) — per-example difficulty varies across models\\n- **Simpson's paradox / ecological fallacy**: Aggregate-vs-disaggregate discrepancy is a textbook phenomenon\\n\\nOur contribution is NOT discovering this phenomenon. It IS quantifying how it manifests specifically when attention is added to linear recurrent models, and characterizing its task-dependency and scale-dependency. This is valuable because hybrid architectures are a design choice practitioners make — understanding per-example implications informs that choice.\\n\\n### Our Framing\\nWe provide the first systematic per-example analysis of attention's equalizing effect in hybrid recurrent architectures. Using Wang et al.'s public model zoo (72 models), we quantify (a) task-dependent convergence strength, (b) scale-dependent convergence completeness, and (c) architecture-specific per-example divergence patterns. Our contribution is analytical depth on public infrastructure, not new methods or models.\\n\\n### Headline Result Template\\n\\\"At 1.3B scale, adding attention to hybrid recurrent models reduces cross-architecture variance by 79% on LAMBADA, yet per-example analysis reveals nearly non-overlapping affected sample subsets (Jaccard < 0.10) — a manifestation of underspecification that has practical implications for architecture selection.\\\"\\n\\n## Dream Review Findings (D006) — Must Address\\n\\n### W1: Single-benchmark significance [MAJOR, blocking]\\nAfter Bonferroni (6 benchmarks, α=0.0083), LAMBADA p=0.017 (two-tailed) does NOT survive. Need: (a) FDR correction (Benjamini-Hochberg) as primary reporting, (b) additional high-retrieval benchmarks for a second significant anchor. Candidates: StoryCloze, BoolQ, COPA, closed-book QA tasks available in lm-eval.\\n\\n### W2: Missing related work [MAJOR, blocking for submission]\\nNeed 20+ references engaging ensemble diversity, underspecification, dataset cartography, attention interpretability, hybrid architectures (Jamba, RWKV-6, RecurrentGemma). Paper Agent handles this during writing.\\n\\n### W3: Mechanistic overclaiming [MAJOR, partially addressed]\\nAlready reworded Claim 3 from \\\"Mechanism\\\" to \\\"Effects\\\". Must NOT use \\\"mechanistic analysis\\\" in paper — use \\\"characterization\\\" or \\\"decomposition\\\" instead. Attention weight analysis (exp-004) is descriptive, not causal. Frame honestly.\\n\\n### W4: Incremental over Wang et al. [MAJOR]\\nMitigate by: (a) engaging related work to show the QUESTION we ask is independently motivated by ensemble/underspecification literature, (b) framing contribution as analytical toolkit + quantitative characterization, not re-analysis. (c) Per-example analysis is genuinely novel for this model family.\\n\\n## Venue Fit Risks\\n(unchanged from previous version, see git history)\\n\\n## Anticipated Reviewer Concerns\\n\\n### Concern A: \\\"This is just a re-analysis of Wang et al.'s models\\\"\\nResponse: Yes, and that's the point — public infrastructure enables community analysis. Our per-example decomposition, task-dependency characterization, and scale-dependency analysis are not in Wang et al. The contribution is analytical, like meta-analyses in medicine.\\nRequired: Strong Related Work positioning; frame as \\\"community analysis\\\" paper.\\n\\n### Concern B: \\\"Only one task shows the effect\\\" + Bonferroni failure\\n**Statistical strategy** (from exp-008, verified by Reviewer with independent reproduction):\\n1. **Lead with percentile CI (valid-only)**: BCa degenerates at ρ=-1.0 boundary (z0=-3.86); fall back to percentile CI on valid bootstrap resamples (8875/10000; 11.25% degenerate from n=3 same-architecture redraws). Valid-only percentile CI = **[-1.0, -0.7]**, 100% of valid resamples have ρ<0. Full percentile CI (degenerate-as-zero) = [-1.0, 0.0] touches zero. Paper leads with valid-only CI; BCa degeneracy + degenerate-sample treatment in appendix.\\n2. **Report exact permutation p**: LAMBADA p=0.017 (two-tailed, 2/120 permutations). Honest and transparent.\\n3. **Bonferroni in supplementary**: adj-p=0.100 (two-tailed). Report honestly as \\\"does not survive Bonferroni.\\\" BH-FDR also gives 0.100 (no additional benefit with only 1 small p-value). If exp-011 produces a second significant benchmark, BH-FDR becomes more favorable than Bonferroni.\\n4. **GDN-excluded sensitivity**: Excluding GDN (D004 confound): LAMBADA ρ drops to -0.7 (p=0.233); ARC-Easy ρ **improves** from -0.7 to -0.9 (p=0.083, suggestive — D004 noise removed); **⚠️ MMLU ρ FLIPS from -0.7 to +0.6** — MMLU apparent convergence was entirely GDN-driven and MUST NOT appear as convergence evidence anywhere in the paper (D007). Report both full and GDN-excluded analyses. The ARC-Easy improvement after confound removal is itself informative, especially in exp-011 context.\\n5. **exp-011**: Additional retrieval benchmarks (StoryCloze/BoolQ/COPA) for a potential second significant anchor. CRITICAL for acceptance — with exp-011 data, BH-FDR could diverge favorably from Bonferroni.\\n6. **Effect sizes**: Cohen's d CI crosses zero; omega² near zero. Do NOT lead with effect sizes — lead with BCa CI and convergence magnitude (std 0.024→0.005, 79% reduction).\\n\\nRequired experiments: exp-011 (additional retrieval benchmarks), exp-008 (robustness with corrected p-values), exp-002 (per-example validation).\\n\\n### Concern C: \\\"The per-example divergence is a known phenomenon\\\"\\nResponse: Acknowledge explicitly. Our contribution is quantification in hybrid architectures, not discovery of the phenomenon. Cite ensemble diversity + underspecification.\\nRequired: Related Work section (Paper Agent).\\n\\n### Concern D: \\\"n=3 architectures is too few\\\"\\nResponse: 3 architectures × 5 ratios × 2 scales = 30 models. Per-example analysis provides 5153 data points per comparison. Check for additional architectures (exp-005).\\n\\n### Concern E: \\\"Two scales don't establish a trend\\\"\\nResponse: Binary contrast, not trend. 7B unavailable. Frame as \\\"scale is a necessary condition.\\\" exp-007 for 340M rebound mechanism.\\n\\n### Concern F: \\\"No causal mechanism\\\" (NEW from Dream)\\nResponse: We do NOT claim causal mechanism. We characterize and describe. Attention weight analysis (exp-004) is descriptive. Interventional experiments (head swaps, ablations) are acknowledged as future work. Honest framing prevents overclaiming.\\n\", \"total_chars\": 10106, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d9c171a-6503-45ee-9bfb-dd562faac203",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "3ea673a4-31c5-4200-b3e6-1942ae62acdf",
  "sourceToolAssistantUUID": "7d9c171a-6503-45ee-9bfb-dd562faac203",
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

_source line 15 · 2026-05-19T15:32:22.805Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KALkigRmdqJQsuAFjxbp39`</summary>

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
  "parentUuid": "3ea673a4-31c5-4200-b3e6-1942ae62acdf",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAmyypBMNeZiodi99ku",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "751f4b2d-166a-43f6-afab-7c830275fda6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMLvzRV8QuoUctdy5x9iB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4171,
      "cache_read_input_tokens": 17437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4171,
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

_source line 16 · 2026-05-19T15:32:22.813Z_

<details><summary>↩ Tool result · `toolu_01KALkigRmdqJQsuAFjxbp39`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/decisions.yaml\", \"content\": \"_next_id: 9\\ndecisions:\\n- id: D001\\n  date: 2026-05-18 07:24 UTC\\n  summary: MVP Direct variant 340M 全模型 random-chance → 先跑 log-prob 评估，同时查 1.3B 模型可用性\\n  rationale: 16 个模型（含 Transformer baseline）在 depth 1-5 上全部 ~10% accuracy。根因：340M 模型无法通过\\n    generation 完成 in-context function lookup（输出\\\"1998/1999\\\"而非执行查找）。Transformer ceiling\\n    0% → ROADMAP 的 ceiling≥50% 过滤器触发，无 eligible depth。核心理论未被证伪，只是 340M+generation\\n    这个探针失效。下一步：(1) log-prob 评估（30min，测 internal representation 差异），(2) 并行查 1.3B 模型可用性。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-18 09:50 UTC\\n  summary: 1.3B 也无 function composition ICL 能力，MVP 从 synthetic task 双轨 pivot：7B task\\n    validation + 1.3B standard benchmarks\\n  rationale: 两轮实验（340M generation+logprob, 1.3B generation+logprob）一致确认 Ye et al.\\n    的 L-FuncComp 对 Wang et al. base models 不可行——Transformer baseline 自身也只有 random-chance，无法建立\\n    ceiling。根因：pretrained base models 在 ≤1.3B 规模未习得 arbitrary lookup table 的 ICL 能力。核心理论未被证伪，但\\n    synthetic task 作为 probe 在此 scale 下失效。Pivot 方案：(1) 7B Instruct 快速验证 task design\\n    是否本身有问题，(2) 在已有 1.3B hybrid 模型上跑 standard benchmarks（LAMBADA/HellaSwag/ARC/MMLU）检测架构差异信号——如果\\n    attention ratio 对不同难度 benchmark 的影响不同，MVP 仍可 pass，且论文更有 practical relevance。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-18 09:54 UTC\\n  summary: 预注册 benchmark composition depth 赋值（结果出来前锁定，不可事后调整）\\n  rationale: 'IDEA_BRIEF 要求 \\\"composition depth must be derivable from task structure\\n    alone, not from empirical performance\\\"。在 Track 1 benchmark 结果出来前锁定每个 task 的 depth\\n    赋值，防止 post-hoc rationalization。赋值基于 task 的计算结构分析：depth 1 = 单步模式匹配/句法判断（无需跨 context\\n    组合信息）；depth 2 = 需要检索 + 单步推理组合；depth 3 = 需要多步推理链或跨多个 context 片段组合。\\n\\n\\n    预注册赋值：\\n\\n    - Depth 1: lambada_openai (last-word prediction, 单步 pattern completion), blimp\\n    (单条句法规则判断)\\n\\n    - Depth 2: hellaswag (situation model + completion matching), winogrande (coreference:\\n    world knowledge + reasoning), arc_easy (单步 science reasoning), mmlu 5-shot (knowledge\\n    retrieval + single-step reasoning)\\n\\n    - Depth 3: arc_challenge (multi-step science reasoning, 需要推理链)\\n\\n\\n    需补充 depth 3+ 任务使 Spearman 相关性有足够 depth 分层。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-18 16:33 UTC\\n  summary: GDN hybrid-3-1 存在 attn.num_heads confound（16 vs 32），论文分析需区分 GDN（有 confound）和\\n    RetNet/HGRN2（无 confound）\\n  rationale: Wang et al. 的 GDN hybrid-3-1 在 340M 和 1.3B 规模都使用 attn.num_heads=16（GQA\\n    2:1），而 h6/h12/h24 使用 32（GQA 4:1）。这意味着 h3-1 不仅 attention 层更多，per-layer attention\\n    capacity 也不同。RetNet 和 HGRN2 所有 ratio 统一 16 heads，无此问题。论文中 GDN 跨 ratio 趋势需标注此 caveat；如果\\n    RetNet/HGRN2 的 clean 数据显示一致趋势，可缓解 GDN confound 的影响。\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-19 12:50 UTC\\n  summary: MVP 原始 entrainment 假设 FAIL，pivot to Equalizer Effect story，target EMNLP\\n    2026\\n  rationale: 26 模型 ×6 benchmarks 全面否定原假设。但发现 equalizer effect（attention 使不同架构在 LAMBADA\\n    上收敛）+ scale dependency（1.3B 完全 vs 340M 部分）+ per-example mechanism（不同架构不同 sample\\n    子集，Jaccard ~0.09）。用户设定 venue=EMNLP 2026，表明继续推进。Pivot 方向：empirical analysis paper，围绕\\n    equalizer effect 的 quantitative characterization + scale dependency + mechanistic\\n    analysis。\\n  related_experiments:\\n  - exp_id: eval_340m_retnet_hgrn2\\n    role: evidence\\n    result: 340M partial convergence confirmed\\n  - exp_id: hgrn2_eval_h3_1\\n    role: evidence\\n    result: architecture-dependent direction confirmed\\n  depends_on:\\n  - D002\\n  - D003\\n  - D004\\n- id: D006\\n  date: 2026-05-19 13:53 UTC\\n  summary: Dream best case 2.5/5 → 重大 framing 调整：放弃 \\\"paradox\\\" 叙事，转为 \\\"quantification\\n    of known phenomenon in hybrid architectures\\\"；补 high-retrieval benchmarks；补 Related\\n    Work\\n  rationale: Dream 模拟审稿（best case）暴露四个 Major weakness：(1) 单 benchmark 统计显著性——Bonferroni\\n    下 LAMBADA p=0.017 不通过；(2) \\\"equalizer paradox\\\" 是已知现象（ensemble diversity, underspecification）——我们不能声称发现\\n    paradox；(3) mechanistic claims 是 correlational 不是 causal；(4) 纯 re-analysis Wang\\n    et al. 模型的 incremental contribution。Path to Findings (3.0) 需要：Related Work 20+\\n    refs、去掉 paradox framing、额外 high-retrieval benchmark（第二个显著 anchor）。Path to Main\\n    (4.0) 需要 interventional experiments + 7B，不可行。调整策略目标：EMNLP Findings (3.0)。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: evidence\\n    result: only LAMBADA significant, W1 confirmed\\n  - exp_id: exp-003\\n    role: evidence\\n    result: surface features negative, W3 weakens mechanism claims\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-19 14:31 UTC\\n  summary: MMLU blacklisted from convergence evidence — GDN-excluded sensitivity reveals\\n    ρ flips to +0.6\\n  rationale: exp-008 GDN-excluded sensitivity analysis shows MMLU ρ flips from -0.7\\n    to +0.6 when GDN (carrying D004 confound) is removed. The apparent MMLU convergence\\n    was entirely driven by GDN. Any reviewer running GDN-excluded robustness check\\n    would catch this immediately. MMLU must NOT appear as convergence support in the\\n    paper. ARC-Easy improves from -0.7 to -0.9 (p=0.083) after GDN exclusion — signal\\n    is cleaner, usable as suggestive evidence especially alongside exp-011.\\n  related_experiments:\\n  - exp_id: exp-008\\n    role: source\\n    result: MMLU convergence entirely GDN-driven; ARC-Easy signal improves post-exclusion\\n  depends_on:\\n  - D004\\n- id: D008\\n  date: 2026-05-19 15:11 UTC\\n  summary: exp-010 \\\"co-evolution\\\" → \\\"decoupling\\\" framing：per-example divergence 在\\n    4% attention 即饱和，aggregate convergence 逐步递减，二者解耦\\n  rationale: Reviewer 发现 5-point Spearman ρ=-0.70 (p=0.23) 被 pure=0 退化点膨胀（Jaccard=NaN→0）。去掉后\\n    4-point ρ=-0.40, p=0.75。实际 pattern 是 Jaccard 在首个 attention level 即饱和 (~0.095)，aggregate\\n    σ 逐步下降。\\\"Decoupling\\\" 是比 \\\"co-evolution\\\" 更准确且更强的叙事——aggregate 趋同掩盖了 increasingly\\n    divergent per-example dynamics。Net asymmetry 递增 (0.013→0.040) 进一步支持此解读。\\n  related_experiments:\\n  - exp_id: exp-010\\n    role: evidence\\n    result: Aggregate σ monotonically decreasing; Jaccard flat ~0.095; net asymmetry\\n      increasing\\n  depends_on:\\n  - D006\\n\", \"total_chars\": 5998, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "751f4b2d-166a-43f6-afab-7c830275fda6",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "251e09c0-e2c0-406d-928d-a6a8793234bb",
  "sourceToolAssistantUUID": "751f4b2d-166a-43f6-afab-7c830275fda6",
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

_source line 17 · 2026-05-19T15:32:23.202Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Cj9DWpEvy7RmZG9abS8Wfp`</summary>

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
  "parentUuid": "251e09c0-e2c0-406d-928d-a6a8793234bb",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAmyypBMNeZiodi99ku",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55613026-86d0-49d2-9f95-3a42d1cd1e2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMLvzRV8QuoUctdy5x9iB7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4171,
      "cache_read_input_tokens": 17437,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4171
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 17437,
          "cache_creation_input_tokens": 4171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4171,
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

_source line 18 · 2026-05-19T15:32:23.215Z_

<details><summary>↩ Tool result · `toolu_01Cj9DWpEvy7RmZG9abS8Wfp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/memory.md\", \"content\": \"# FLA 版本与 m-a-p 模型兼容性调查结果 (2026-05-18)\\n\\n## 核心结论：fla 0.5.0 与 m-a-p 模型兼容，attn.D 丢弃无影响\\n\\n### 1. attn.D 参数真相\\n\\n- **m-a-p GatedDeltaNet 模型**（如 `1.3B-100B-GatedDeltaNet-pure`）的 checkpoint 中包含 `attn.D` 参数（每层一个，共 24 个）\\n- `self.D` 在 fla 的 GatedDeltaNet 初始实现（commit `4064237`, 2024-12-20）中被声明为 `nn.Parameter(torch.ones(num_heads))`，继承自 Mamba2 的 skip connection 设计\\n- **但 self.D 从未在 forward() 中被使用** — 它是死参数，训练过程中不参与计算、不接收梯度，始终保持初始值 `ones`\\n- `self.D` 在 commit `834989c` (2025-03-12) 中被移除，对应 issue #226 \\\"Remove redundant parameter\\\"\\n- fla v0.1.0 (2025-03-20) 起所有版本均不含 self.D\\n- **结论：加载模型时 attn.D 被 strict=False 静默丢弃，对模型行为和评估结果无任何影响**\\n\\n### 2. m-a-p 模型训练环境\\n\\n- **论文**: Wang et al. \\\"A Systematic Analysis of Hybrid Linear Attention\\\" (arXiv 2507.06457, July 2025)\\n- **训练框架**: flash-linear-attention (fla) + flame (基于 torchtitan)\\n- **训练数据**: FineWeb-Edu\\n- **模型规模**: 72 个模型（36×340M/20B tokens + 36×1.3B/100B tokens）\\n- **transformers 版本**: \\n  - 1.3B GatedDeltaNet-pure: 4.51.3 (2025-04-14)\\n  - RetNet / 340M New GatedDeltaNet: 4.49.0 (~2025-02)\\n- **fla 版本**: 未在论文或模型卡中明确标注。根据 self.D 存在于 checkpoint 推断，训练使用的是 2025-03-12 之前的 fla 开发版本（pre-v0.1.0）\\n- **HuggingFace 集合**: https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e\\n\\n### 3. fla PyPI 版本历史\\n\\n| 版本 | 发布日期 | 备注 |\\n|------|----------|------|\\n| 0.1.0 | 2025-03-20 | 首个 tagged release，已无 self.D |\\n| 0.1.1 | 2025-03-24 | |\\n| 0.1.2 | 2025-03-31 | |\\n| 0.2.0 | 2025-04-11 | |\\n| 0.2.1 | 2025-04-23 | |\\n| 0.2.2 | 2025-06-05 | GDN GVA support |\\n| 0.3.0 | 2025-07-14 | MesaNet/PaTH/Comba/MLA; head_first deprecated |\\n| 0.3.2 | 2025-09-10 | fla-core 包分离 |\\n| 0.4.0 | 2025-10-27 | KDA |\\n| 0.4.1 | 2025-12-24 | |\\n| 0.4.2 | 2026-03-12 | |\\n| 0.5.0 | 2026-04-21 | 当前版本 |\\n\\n### 4. RetNet 模型情况\\n\\n- RetNet 模型 checkpoint 中**没有 attn.D**，不存在参数丢弃问题\\n- config 使用 transformers 4.49.0\\n- 模型参数结构（q/k/v/g_proj, g_norm_swish_gate, o_proj）与 fla MultiScaleRetention 层一致\\n\\n### 5. 建议\\n\\n**使用 fla 0.5.0（或任何 >=0.1.0 版本）加载 m-a-p 模型是安全的**，只需确保加载时 `strict=False`。attn.D 被丢弃不会影响模型输出。\\n\\n---\\n\\n# 统计报告规则 (2026-05-19, Director 硬约束)\\n\\n**所有分析报告中的统计 claim 必须附原始数值 (ρ=X, p=Y)，不允许只写结论。**\\n\\n事件：wang_et_al_differentiation.md 中 Worker 产出 \\\"4/6 benchmarks 显著收敛\\\" 的虚假 claim（实际仅 LAMBADA 1/6 显著）。Director 发现后标记为 CRITICAL。\\n\\n规则：\\n- 每个 \\\"显著/不显著\\\" claim 后必须跟 (ρ=X, p=Y) 或对应的检验统计量\\n- \\\"majority\\\"/\\\"most\\\" 等量化词必须有准确计数支撑（如 \\\"4/6\\\" 必须逐一列出哪 4 个）\\n- 此规则适用于所有项目产出（分析报告、论文章节、汇报材料）\\n\\n---\\n\\n# exp-003 表面特征分析教训 (2026-05-19)\\n\\n**表面特征（token frequency、context length、lexical diversity）无法区分 LAMBADA 上的 helped/hurt 样本。**\\n\\n- GDN/HGRN2：所有特征 p > 0.2，无信号\\n- RetNet：context_length p=0.012, r=-0.096（统计显著但效应量微不足道）；context_unique_tokens p=0.009, r=-0.099\\n- 跨架构比较：三架构 helped 样本特征分布无显著差异\\n\\n**启示**：per-example 效应的机制在模型内部（attention pattern / representation level），不在输入表面特征。这排除了 \\\"attention 只帮助长上下文\\\" 或 \\\"attention 只帮助低频词\\\" 等 trivial 解释，强化了 Claim 3（architecture-specific mechanism）的论证——需要 exp-004（attention weight extraction）来揭示真正的机制。\\n\\n---\\n\\n# exp-010 Bridge 分析：Decoupling 叙事 (2026-05-19, D008 修正)\\n\\n**正确叙事是 \\\"decoupling\\\"（解耦），不是 \\\"co-evolution\\\" 或 \\\"paradoxical coexistence\\\"。**\\n\\nReviewer 发现方法论问题：5-point Spearman ρ=-0.70 (p=0.23) 几乎完全由 pure=0 退化点驱动（Jaccard=NaN 赋值 0）。去掉 pure 后 ρ=-0.40, p=0.75，本质无关。\\n\\n**实际 pattern**：\\n- Jaccard 在 4% attention（h24-1）即饱和到 ~0.095，之后平坦\\n- Aggregate σ 从 0.024 逐步递减到 0.005\\n- 两个过程运行在**不同时间尺度**上\\n\\n**论文写作硬约束**：\\n- 禁用：co-evolution, paradoxical coexistence, paradox\\n- 使用：decoupling, different timescales\\n- Net asymmetry 递增（0.013→0.040）是真实 pattern，可强调\\n- 可视化应突出两条曲线的不同时间尺度，而非相关性\\n\", \"total_chars\": 3437, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55613026-86d0-49d2-9f95-3a42d1cd1e2f",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "380e8dd7-4b08-4828-8800-49195432b80b",
  "sourceToolAssistantUUID": "55613026-86d0-49d2-9f95-3a42d1cd1e2f",
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

_source line 19 · 2026-05-19T15:32:27.042Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014FzcHje8jR62yr2YufHvXp`</summary>

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
  "parentUuid": "380e8dd7-4b08-4828-8800-49195432b80b",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAnLXLNvdKXGwLbBqKS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0014fc1-2df6-4963-8220-f8ec2f33f7a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALYVWEpZm6KRgr8YqqFc8s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8826,
      "cache_read_input_tokens": 21608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8826,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 20 · 2026-05-19T15:32:27.063Z_

<details><summary>↩ Tool result · `toolu_014FzcHje8jR62yr2YufHvXp`</summary>

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
  "parentUuid": "e0014fc1-2df6-4963-8220-f8ec2f33f7a6",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "307339e4-521f-4fb1-bbe6-03607ce9c5a5",
  "sourceToolAssistantUUID": "e0014fc1-2df6-4963-8220-f8ec2f33f7a6",
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

_source line 21 · 2026-05-19T15:32:27.530Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DsCsRy7SJi8oXQ2Ez1Ytbq`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "307339e4-521f-4fb1-bbe6-03607ce9c5a5",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAnLXLNvdKXGwLbBqKS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d932001-5ba6-4d6f-a266-9e47cc5a5580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALYVWEpZm6KRgr8YqqFc8s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8826,
      "cache_read_input_tokens": 21608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8826,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 22 · 2026-05-19T15:32:27.545Z_

<details><summary>↩ Tool result · `toolu_01DsCsRy7SJi8oXQ2Ez1Ytbq`</summary>

```text
artifacts/dream_reports/dream_20260519T131014/best/paper.pdf
artifacts/dream_reports/dream_20260519T131014/median/paper.pdf
artifacts/dream_reports/dream_20260519T131014/worst/paper.pdf
artifacts/dream_reports/dream_20260519T135121/best/paper.pdf
artifacts/dream_reports/dream_20260519T135121/median/paper.pdf
artifacts/dream_reports/dream_20260519T135121/worst/paper.pdf
artifacts/dream_reports/dream_20260519T143201/best/paper.pdf
artifacts/dream_reports/dream_20260519T143201/median/paper.pdf
artifacts/dream_reports/dream_20260519T143201/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d932001-5ba6-4d6f-a266-9e47cc5a5580",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "1188aa80-8c7a-40a9-bced-2b5574e1c7c2",
  "sourceToolAssistantUUID": "3d932001-5ba6-4d6f-a266-9e47cc5a5580",
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

_source line 23 · 2026-05-19T15:32:28.460Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UVBRejiS73aYorHepMexSc`</summary>

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
  "parentUuid": "1188aa80-8c7a-40a9-bced-2b5574e1c7c2",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAnLXLNvdKXGwLbBqKS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b727861-d5fb-43df-a0db-01cba9634f67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALYVWEpZm6KRgr8YqqFc8s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8826,
      "cache_read_input_tokens": 21608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8826,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 24 · 2026-05-19T15:32:28.470Z_

<details><summary>↩ Tool result · `toolu_01UVBRejiS73aYorHepMexSc`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'entrainment_gated_ft'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b727861-d5fb-43df-a0db-01cba9634f67",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "b80dc836-60c0-4c4a-901d-b511a7b9fc91",
  "sourceToolAssistantUUID": "3b727861-d5fb-43df-a0db-01cba9634f67",
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

_source line 25 · 2026-05-19T15:32:28.985Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JHfinVUg6igPFimvuTBsDh`</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b80dc836-60c0-4c4a-901d-b511a7b9fc91",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAnLXLNvdKXGwLbBqKS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0886dd73-1f18-4c9c-82a2-d3c038645aad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALYVWEpZm6KRgr8YqqFc8s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8826,
      "cache_read_input_tokens": 21608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8826,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 26 · 2026-05-19T15:32:29.001Z_

<details><summary>↩ Tool result · `toolu_01JHfinVUg6igPFimvuTBsDh`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'entrainment_gated_ft'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0886dd73-1f18-4c9c-82a2-d3c038645aad",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "c2b060ac-7748-4cb2-8539-7f2cb27ddaa5",
  "sourceToolAssistantUUID": "0886dd73-1f18-4c9c-82a2-d3c038645aad",
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

_source line 27 · 2026-05-19T15:32:32.079Z_

Let me read the most recent "best case" paper to review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2b060ac-7748-4cb2-8539-7f2cb27ddaa5",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAnm7givarVtPhWGdzx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64ea5441-1f63-4bca-baad-6d9485ead642",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsfUSsEeAUDtMuJPv1dkcT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 30434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1082,
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

_source line 28 · 2026-05-19T15:32:32.334Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SQUAGDKWVCBkTCgq3gc2DG`</summary>

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
  "parentUuid": "64ea5441-1f63-4bca-baad-6d9485ead642",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAnm7givarVtPhWGdzx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bec04de-4687-4868-93ee-ac440c00bf6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsfUSsEeAUDtMuJPv1dkcT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 30434,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1082
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 30434,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1082,
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

_source line 29 · 2026-05-19T15:32:32.638Z_

<details><summary>↩ Tool result · `toolu_01SQUAGDKWVCBkTCgq3gc2DG`</summary>

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
  "parentUuid": "5bec04de-4687-4868-93ee-ac440c00bf6f",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "6947f734-44fd-494f-8ce5-c258e5a44207",
  "sourceToolAssistantUUID": "5bec04de-4687-4868-93ee-ac440c00bf6f",
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

_source line 30 · 2026-05-19T15:32:37.443Z_

Now let me also read the dream review reports to understand what the automated review found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6947f734-44fd-494f-8ce5-c258e5a44207",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAo2XdtayJ5SW4Zh2ks",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17b3a569-1c35-44d4-87d0-208294e1be5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0148f21LW7uqNTxConEQHycv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14871,
      "cache_read_input_tokens": 31516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14871,
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

_source line 31 · 2026-05-19T15:32:39.958Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KvCujujr2fp2ArFFaMrhzM`</summary>

```json
{
  "pattern": "**/dream_reports/dream_20260519T143201/best/review*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17b3a569-1c35-44d4-87d0-208294e1be5b",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAo2XdtayJ5SW4Zh2ks",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb8a5fc1-d895-4ef7-a845-cebd3aa41e19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0148f21LW7uqNTxConEQHycv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14871,
      "cache_read_input_tokens": 31516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14871,
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

_source line 32 · 2026-05-19T15:32:39.995Z_

<details><summary>↩ Tool result · `toolu_01KvCujujr2fp2ArFFaMrhzM`</summary>

```text
artifacts/dream_reports/dream_20260519T143201/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb8a5fc1-d895-4ef7-a845-cebd3aa41e19",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "7689e732-1d0d-4dc6-95c1-7428f538e9c4",
  "sourceToolAssistantUUID": "fb8a5fc1-d895-4ef7-a845-cebd3aa41e19",
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

_source line 33 · 2026-05-19T15:32:41.183Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01T6y9wLyKKg9WL9xnot9U1j`</summary>

```json
{
  "pattern": "**/dream_reports/dream_20260519T143201/**/*review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7689e732-1d0d-4dc6-95c1-7428f538e9c4",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAo2XdtayJ5SW4Zh2ks",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5a653d7-417f-45a0-b468-02fa67e3427c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0148f21LW7uqNTxConEQHycv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14871,
      "cache_read_input_tokens": 31516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14871,
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

_source line 34 · 2026-05-19T15:32:41.198Z_

<details><summary>↩ Tool result · `toolu_01T6y9wLyKKg9WL9xnot9U1j`</summary>

```text
artifacts/dream_reports/dream_20260519T143201/best/review_context.yaml
artifacts/dream_reports/dream_20260519T143201/best/review_report.md
artifacts/dream_reports/dream_20260519T143201/logs/review_best.log
artifacts/dream_reports/dream_20260519T143201/median/review_context.yaml
artifacts/dream_reports/dream_20260519T143201/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5a653d7-417f-45a0-b468-02fa67e3427c",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "898f075f-f306-4b6b-988b-24639f0e312c",
  "sourceToolAssistantUUID": "e5a653d7-417f-45a0-b468-02fa67e3427c",
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

_source line 35 · 2026-05-19T15:32:41.618Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HCfDcGMcGtkZKD1RjahvEE`</summary>

```json
{
  "pattern": "**/dream_reports/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "898f075f-f306-4b6b-988b-24639f0e312c",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAo2XdtayJ5SW4Zh2ks",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26140acf-1a93-4775-9c1f-d5b6abfb8a63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0148f21LW7uqNTxConEQHycv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14871,
      "cache_read_input_tokens": 31516,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14871
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 321,
          "cache_read_input_tokens": 31516,
          "cache_creation_input_tokens": 14871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14871,
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

_source line 36 · 2026-05-19T15:32:41.633Z_

<details><summary>↩ Tool result · `toolu_01HCfDcGMcGtkZKD1RjahvEE`</summary>

```text
artifacts/dream_reports/dream_20260519T125419/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T131014/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T131014/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T131014/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T131014/best/review_context.yaml
artifacts/dream_reports/dream_20260519T131014/median/review_context.yaml
artifacts/dream_reports/dream_20260519T135121/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T135121/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T135121/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T135121/best/review_context.yaml
artifacts/dream_reports/dream_20260519T135121/median/review_context.yaml
artifacts/dream_reports/dream_20260519T135121/worst/review_context.yaml
artifacts/dream_reports/dream_20260519T143201/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T143201/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T143201/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260519T143201/best/review_context.yaml
artifacts/dream_reports/dream_20260519T143201/median/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26140acf-1a93-4775-9c1f-d5b6abfb8a63",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "ae6dd35c-bf16-4c0c-8e8c-598924ed090a",
  "sourceToolAssistantUUID": "26140acf-1a93-4775-9c1f-d5b6abfb8a63",
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

_source line 37 · 2026-05-19T15:32:45.299Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tovmq75w3ZHLeHGU4Ayvoc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T143201/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae6dd35c-bf16-4c0c-8e8c-598924ed090a",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAoh7s2iGtFBSonUS2b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52927afb-eab2-4640-9fa9-1bce48fd312d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MS5jDQNAwXfhRVdBBYGoMi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 942,
      "cache_read_input_tokens": 46387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 942,
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

### Tool call

_source line 38 · 2026-05-19T15:32:45.705Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AVeLbaxVbnuugGGX1VrFWk`</summary>

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
  "parentUuid": "52927afb-eab2-4640-9fa9-1bce48fd312d",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAoh7s2iGtFBSonUS2b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39690d9c-e8f9-4db1-b18c-4472d52d0774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MS5jDQNAwXfhRVdBBYGoMi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 942,
      "cache_read_input_tokens": 46387,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 942
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 46387,
          "cache_creation_input_tokens": 942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 942,
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

_source line 39 · 2026-05-19T15:32:45.718Z_

<details><summary>↩ Tool result · `toolu_01AVeLbaxVbnuugGGX1VrFWk`</summary>

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
  "parentUuid": "39690d9c-e8f9-4db1-b18c-4472d52d0774",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "17d0609e-fb33-4e9e-bfd5-26987cd0d0e7",
  "sourceToolAssistantUUID": "39690d9c-e8f9-4db1-b18c-4472d52d0774",
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

### Tool result

_source line 40 · 2026-05-19T15:32:46.008Z_

<details><summary>↩ Tool result · `toolu_01Tovmq75w3ZHLeHGU4Ayvoc`</summary>

```text
1	narrative_guidance: 'Task-dependent convergence 在 LAMBADA + StoryCloze 两个独立 retrieval
2	  benchmark 上成立
3	
4	  （均 ρ=-1.0, two-tailed exact permutation p=0.017）。统计策略：exp-001 taxonomy 先于
5	
6	  exp-011 建立 retrieval-task subset（m=5）作为 pre-specified correction scope——
7	
8	  BH-FDR 保留 2 个 benchmark（adj_p=0.042），Bonferroni 在 confirmatory subset（m=3）
9	
10	  borderline 保留 1 个（adj_p=0.050）。Full m=9 correction 下无 benchmark 显著——诚实报告。
11	
12	  Per-example divergence 在 4 个架构上量化（+Mamba2-hybrid, exp-005），Jaccard 0.05-0.09。
13	
14	  exp-003 两层 negative（surface features + perplexity 均不预测 within-arch helped/hurt）
15	
16	  排除 trivial explanations；cross-arch KW（p=0.0005）确认 structured specificity。
17	
18	  Attention pattern 提供中等描述性关联（mean r=0.36, exp-004）。
19	
20	  340M rebound 有 capacity bottleneck 解释（rebound samples 73% 在 top difficulty quartile）。
21	
22	  W1 降级为 addressed；W4 通过第 4 架构 + per-example 独立贡献缓解。目标 EMNLP Main。
23	
24	  '
25	imagined_experiments:
26	- name: Task-specificity characterization of equalizer effect
27	  plan_id: exp-001
28	  description: 6 benchmark 跨架构 std 轨迹 + exact permutation Spearman + 任务分类体系（已完成，actual
29	    results）
30	  expected_results:
31	    LAMBADA_rho: -1.0
32	    LAMBADA_p_two_tailed: 0.017
33	    LAMBADA_std_pure: 0.024
34	    LAMBADA_std_h3_1: 0.005
35	    LAMBADA_std_reduction_pct: 79
36	    HellaSwag_rho: 0.3
37	    ARC_C_rho: 0.6
38	    Winogrande_rho: 0.1
39	    ARC_Easy_rho: -0.7
40	    ARC_Easy_p: 0.233
41	    MMLU_rho: -0.7
42	    MMLU_p: 0.233
43	    significant_count: 1/6
44	    taxonomy:
45	      retrieval_dependent:
46	      - LAMBADA
47	      mixed:
48	      - ARC-Easy
49	      - MMLU
50	      reasoning_dependent:
51	      - HellaSwag
52	      - ARC-C
53	      - Winogrande
54	  result_rationale: '已完成实验的实际结果。Best 档解读的关键：taxonomy 是 PREDICTIVE framework，不是 post-hoc
55	    rationalization。
56	
57	    LAMBADA（last-word prediction from passage）依赖 attention 的 copy/induction-head retrieval
58	    mechanism——
59	
60	    所有架构的 attention 都学会类似的 context retrieval → 性能趋同。
61	
62	    Reasoning 任务（HellaSwag/ARC-C/Winogrande）依赖 recurrent state 的 compositional inference，
63	
64	    attention 不系统性改变这一计算 → ρ ≈ 0 或正值。
65	
66	    Mixed 类（ARC-Easy ρ=-0.7, MMLU ρ=-0.7）有 factual retrieval 成分但不纯粹 → suggestive trend。
67	
68	    核心价值：taxonomy 为 exp-011 提供了 a priori prediction——高 retrieval demand 的新 benchmark
69	
70	    应显示 convergence——使 exp-011 从 fishing expedition 变为 hypothesis-driven confirmatory
71	    test。
72	
73	    '
74	  tables:
75	  - 'Table 1: Cross-architecture convergence by benchmark (ρ, exact permutation p,
76	    taxonomy)'
77	  figures_description:
78	  - 'Fig 1a: Cross-arch std vs attention ratio (5 points × 6 benchmarks), color-coded
79	    by taxonomy'
80	  analysis: 'Taxonomy 成立。ρ 值沿 retrieval demand gradient 单调递减：
81	
82	    LAMBADA(-1.0) > ARC-Easy/MMLU(-0.7) > ARC-C(0.6)/HellaSwag(0.3)/Winogrande(0.1)。
83	
84	    这个 gradient 本身是一个 finding：convergence strength 是 retrieval demand 的函数。
85	
86	    '
87	- name: Multi-benchmark per-example analysis
88	  plan_id: exp-002
89	  description: HellaSwag/ARC-Easy/ARC-Challenge 收集 --log_samples 数据（10×340M + 3×1.3B），验证
90	    per-example task-specificity
91	  expected_results:
92	    n_models_evaluated: 13
93	    gpu_hours_used: 18
94	    LAMBADA_jaccard_mean: 0.07
95	    ARC_Easy_jaccard_mean: 0.09
96	    ARC_Challenge_jaccard_mean: 0.14
97	    HellaSwag_jaccard_mean: 0.16
98	    LAMBADA_mean_effect_magnitude: 0.055
99	    ARC_Easy_mean_effect_magnitude: 0.038
100	    ARC_Challenge_mean_effect_magnitude: 0.025
101	    HellaSwag_mean_effect_magnitude: 0.02
102	    task_specificity_per_example_confirmed: true
103	    jaccard_retrieval_demand_correlation: -0.92
104	  result_rationale: 'LAMBADA 低 Jaccard（0.07）：不同架构的 attention 用不同 retrieval strategy（copy-head
105	    vs
106	
107	    induction-head vs local-window）rescue 不同的 sample——每种 recurrence bias 与 attention
108	    的
109	
110	    互补方式不同，导致 "被 rescue 的 sample 集合" 高度 architecture-specific。
111	
112	    HellaSwag 高 Jaccard（0.16）：reasoning 任务上 attention 的 per-example 效应缺乏 systematic
113	    pattern，
114	
115	    帮助/伤害更接近随机重排。随机集合的 expected Jaccard 高于 structured 集合——这正是
116	
117	    "reasoning 任务无 systematic convergence" 在 per-example 层面的 signature。
118	
119	    |effect| gradient（LAMBADA 0.055 > ARC-E 0.038 > ARC-C 0.025 > HellaSwag 0.020）
120	
121	    与 Jaccard gradient 一致：retrieval 任务上 attention 效应更强且更 structured。
122	
123	    Combined Jaccard-retrieval demand correlation（ρ=-0.92）量化了 dose-response 关系。
124	
125	    '
126	  tables:
127	  - 'Table 2: Per-example divergence metrics by benchmark (Jaccard, |effect|, n_helped,
128	    n_hurt)'
129	  figures_description:
130	  - 'Fig 3: Jaccard heatmap — architecture pair × benchmark; LAMBADA 列深蓝，reasoning
131	    列浅色'
132	  - 'Fig 4: Per-example effect maps — ARC-Easy (structured blocks) vs HellaSwag (salt-and-pepper)'
133	  analysis: 'Per-example 数据将 task-specificity 从 aggregate-only 提升为 multi-level validation。
134	
135	    Jaccard gradient 是 exp-001 taxonomy 在 per-example 层面的独立确认。
136	
137	    HellaSwag per-example non-convergence 排除了 "hidden convergence masked by aggregate
138	    noise"。
139	
140	    '
141	- name: Helped/hurt sample characterization
142	  plan_id: exp-003
143	  description: Surface features（Phase 1）+ baseline perplexity（Phase 2）分析（两 phase 均已完成，actual
144	    results）
145	  expected_results:
146	    within_arch_surface_features_any_significant: false
147	    RetNet_context_length_p: 0.012
148	    RetNet_context_length_r: -0.096
149	    RetNet_unique_tokens_p: 0.009
150	    RetNet_unique_tokens_r: -0.099
151	    GDN_all_p_values_gt: 0.5
152	    HGRN2_all_p_values_gt: 0.2
153	    cross_arch_surface_difference: not_significant
154	    within_arch_perplexity_significant: false
155	    GDN_ppl_U: 148410
156	    GDN_ppl_p: 0.209
157	    GDN_ppl_r_rb: -0.045
158	    RetNet_ppl_p: 0.659
159	    RetNet_ppl_r_rb: -0.017
160	    HGRN2_ppl_p: 0.248
161	    HGRN2_ppl_r_rb: -0.044
162	    cross_arch_hurt_KW_p: 0.0005
163	    cross_arch_helped_KW_p: 0.02
164	  result_rationale: 'Best 档解读：两层 negative 是 asset 而非 liability。
165	
166	    Phase 1 negative：token frequency、context length、lexical diversity 不预测 helped/hurt
167	    →
168	
169	    排除 "attention 只帮长句子" 或 "只帮罕见词" 等 trivial explanation。
170	
171	    Phase 2 negative：baseline perplexity 也不预测（r_rb ≈ -0.04, p > 0.2 三架构均如此）→
172	
173	    排除最自然的 first-order hypothesis "attention rescues uncertain samples"。
174	
175	    这两层 negative 共同确立：per-example effect 不由 sample 的固有属性或 baseline difficulty 驱动，
176	
177	    而由 architecture-attention 交互的 higher-order structure 驱动。
178	
179	    Cross-arch KW 显著（hurt p=0.0005）是 KEY positive result：
180	
181	    不同架构 hurt 的 sample 有系统性不同的 baseline difficulty profile。
182	
183	    GDN hurt mean ppl=3.34, RetNet=3.42, HGRN2=3.35——差异虽不大但统计显著，
184	
185	    因为 n 大（462-615 per architecture）。
186	
187	    叙事：underspecification 不是 trivially predictable（within-arch negative）但也不是 random
188	    noise
189	
190	    （cross-arch structured）。这是 underspecification 文献中的 characteristic signature。
191	
192	    '
193	  tables:
194	  - 'Table 3a: Within-arch tests — surface features (all NS) + perplexity (all NS)'
195	  - 'Table 3b: Cross-arch Kruskal-Wallis — hurt KW p=0.0005, helped KW p=0.020'
196	  figures_description:
197	  - 'Fig 5: Violin plot — hurt sample baseline perplexity per architecture (3 distributions,
198	    KW p=0.0005)'
199	  analysis: '负面结果的叙事价值在 best 档下充分发挥：两层 negative + cross-arch positive
200	
201	    构成 "opaque within, structured across" 的完整 characterization。
202	
203	    为 exp-004 的 attention analysis 设定了 expectation：mechanism 不在 sample-level features，
204	
205	    而在 model-sample 交互的 attention dynamics。
206	
207	    '
208	- name: Attention weight extraction and visualization
209	  plan_id: exp-004
210	  description: 提取 GDN/RetNet/HGRN2 h3-1 的 attention weights，分析 attention pattern 与
211	    per-example effect 关联
212	  expected_results:
213	    n_models_analyzed: 3
214	    GDN_attn_concentration_effect_r: 0.37
215	    GDN_attn_concentration_effect_p: 0.004
216	    RetNet_attn_concentration_effect_r: 0.4
217	    RetNet_attn_concentration_effect_p: 0.001
218	    HGRN2_attn_concentration_effect_r: 0.31
219	    HGRN2_attn_concentration_effect_p: 0.011
220	    mean_r_across_archs: 0.36
221	    n_archs_with_r_gt_0_3: 3
222	    cross_arch_attn_pattern_cosine_sim: 0.21
223	    helped_attn_entropy_lower_than_hurt: true
224	    GDN_modal_attn_distance: 3-8 tokens (compensating delta-rule recent-context decay)
225	    RetNet_modal_attn_distance: 8-20 tokens (compensating exponential mid-range decay)
226	    HGRN2_modal_attn_distance: 5-15 tokens (variable, hierarchical gate-dependent)
227	    gpu_hours_used: 3.5
228	  result_rationale: 'Attention concentration（低 entropy）与 per-example positive effect
229	    的中等相关（mean r=0.36）
230	
231	    来源于两个 complementary mechanism：
232	
233	    (1) Helped samples：attention 成功定位 recurrent state 缺失的信息位置
234	
235	    （LAMBADA → target word 的 semantic antecedent），产生集中的 attention pattern（低 entropy）。
236	
237	    (2) Hurt samples：recurrent state 已充分编码必要信息，attention 的额外 computation 分散
238	
239	    probability mass（高 entropy, diffuse attention），反而干扰。
240	
241	    r ≈ 0.36 而非更高（<0.5）有三个原因：
242	
243	    (a) multi-head aggregation 是 coarse proxy——不同 head 有不同 role；
244	
245	    (b) 部分 concentrated-but-wrong（attention 聚焦错误位置 → still hurt）；
246	
247	    (c) 部分 diffuse-but-helpful（weak signal > no signal when recurrent state 很弱）。
248	
249	    Cross-arch attention similarity 低（cosine 0.21）直接解释低 Jaccard：
250	
251	    GDN attention 补偿 delta-rule 的近距离衰减（聚焦 3-8 tokens），
252	
253	    RetNet 补偿 exponential 的中距离衰减（8-20 tokens），
254	
255	    HGRN2 补偿 hierarchical gate 的不规则 retention（5-15, variable）。
256	
257	    关键：这是 DESCRIPTIVE correlation。exp-003 Phase 2 的 negative perplexity result 意味着
258	
259	    attention pattern 不能还原为 "rescue uncertain tokens"——它是 attention-recurrence 交互的
260	
261	    emergent property，不可从 sample 属性预测。避免 mechanistic overclaiming（W3）。
262	
263	    '
264	  tables:
265	  - 'Table 4: Attention entropy vs per-example effect (per architecture, Mann-Whitney
266	    + rank-biserial r)'
267	  - 'Table 5: Attention focus distance comparison across architectures'
268	  figures_description:
269	  - 'Fig 6: Attention heatmaps — 3 archs × 3 sample types (helped-by-all, helped-by-one,
270	    hurt-by-all)'
271	  - 'Fig 7: Scatter — attention entropy vs effect magnitude, 3 colors for 3 architectures,
272	    negative trend'
273	  analysis: 'r=0.36 满足 >0.3 threshold，支持 "partial descriptive account"。
274	
275	    不同架构的不同 dominant pattern 给读者 intuitive mental model for architecture-specificity。
276	
277	    结合 exp-003 negative：per-example effect 不由 sample 属性驱动（exp-003），
278	
279	    而由 model-sample 交互的 attention dynamics 部分解释（exp-004）——这正是 underspecification
280	
281	    的 operational definition：same aggregate outcome, architecture-specific per-example
282	    pathways。
283	
284	    '
285	- name: Architecture expansion check
286	  plan_id: exp-005
287	  description: 搜索 Wang et al. model zoo + 其他来源的额外 hybrid 架构，评估 LAMBADA convergence
288	    泛化性
289	  expected_results:
290	    additional_arch_found: Mamba2-Attention hybrid
291	    source: Wang et al. extended model set or community reproduction
292	    n_attention_ratios_available: 5
293	    mamba2_lambada_scores:
294	    - 0.598
295	    - 0.617
296	    - 0.632
297	    - 0.641
298	    - 0.648
299	    mamba2_standalone_rho: -0.9
300	    mamba2_standalone_p_two_tailed: 0.083
301	    cross_arch_std_4arch:
302	      h0_pure: 0.029
303	      h24_1: 0.019
304	      h12_1: 0.014
305	      h6_1: 0.007
306	      h3_1: 0.006
307	    convergence_rho_4arch: -1.0
308	    convergence_p_4arch: 0.017
309	    std_reduction_4arch_pct: 80
310	    mamba2_jaccard_vs_GDN: 0.06
311	    mamba2_jaccard_vs_RetNet: 0.08
312	    mamba2_jaccard_vs_HGRN2: 0.09
313	    n_architectures_total: 4
314	    gpu_hours_used: 5
315	  result_rationale: 'Mamba2（selective SSM）与 GDN（delta rule）、RetNet（exponential decay）、
316	
317	    HGRN2（hierarchical gating）在 recurrence mechanism 上完全不同——最强的 independent replication。
318	
319	    4 架构 cross-arch std trajectory 仍然 ρ=-1.0, p=0.017：
320	
321	    Spearman 检验是在 5-point std trajectory 上（n=5 attention ratios），
322	
323	    不因架构数增加而改变——测的是 trajectory shape，不是 raw scores。
324	
325	    Mamba2 standalone ρ=-0.9（p=0.083, not significant）因为 selective SSM 的 attention
326	    需要
327	
328	    更多层才能 override SSM 的 strong sequence modeling 能力——effect 方向一致但 magnitude 弱于三大架构。
329	
330	    h0 处 std 从 0.024（3 arch）增至 0.029（4 arch）因为 Mamba2 baseline 与其他三家差异更大。
331	
332	    h3-1 仍收敛到 0.006。Reduction = (0.029-0.006)/0.029 = 80%。
333	
334	    Jaccard 0.06-0.09 确认 Mamba2 的 per-example effect 也是 architecture-specific——
335	
336	    selective SSM 有又一套不同的 information retention blind spots。
337	
338	    4 架构的价值不在 p-value（仍然 0.017）而在 generalizability：
339	
340	    四种 fundamentally different recurrence mechanisms 都 converge under attention。
341	
342	    '
343	  tables:
344	  - 'Table 6: Cross-arch std with 4 architectures (LAMBADA 1.3B)'
345	  - 'Table 7: 4×4 Jaccard matrix (helped/hurt sets)'
346	  figures_description:
347	  - 'Fig 2 (updated): Cross-arch std trajectory with 4 architectures — wider initial
348	    spread, same endpoint'
349	  analysis: '从 n=3 到 n=4 直接回应 Reviewer Concern D。
350	
351	    四种机制跨越 delta rule / exponential decay / hierarchical gating / selective SSM，
352	
353	    finding 不是 coincidental。W4 缓解：Wang et al. 无第 4 架构 per-example 分析。
354	
355	    '
356	- name: 7B model evaluation
357	  plan_id: exp-006
358	  description: 已取消——Wang et al. model zoo 仅 340M + 1.3B（72 models），无 7B 可用
359	  expected_results:
360	    status: cancelled
361	    reason: 7B models unavailable
362	    mitigation: exp-007 升级 P0，深化 340M vs 1.3B binary contrast + capacity bottleneck
363	      mechanism
364	  result_rationale: '硬约束。Best 档通过 exp-007 的 mechanistic explanation 补偿：
365	
366	    binary contrast + mechanism 比三个 data points without mechanism 更有说服力。
367	
368	    Paper Limitations 明确承认 two-scale 约束。
369	
370	    '
371	  tables: []
372	  figures_description: []
373	  analysis: N/A — cancelled
374	- name: 340M rebound mechanism analysis
375	  plan_id: exp-007
376	  description: 340M 非单调 rebound 的 per-example cross-scale 分析 + capacity bottleneck
377	    解释
378	  expected_results:
379	    rebound_onset: h12-1 (50% attention layers)
380	    n_rebound_samples: 145
381	    rebound_pct_top_difficulty_quartile: 0.73
382	    rebound_mean_ppl_340m: 4.62
383	    rebound_mean_ppl_1_3b: 3.15
384	    matched_1_3b_acc_on_rebound_samples: 0.68
385	    matched_340m_h6_1_acc_on_rebound: 0.49
386	    matched_340m_h3_1_acc_on_rebound: 0.35
387	    ppl_gap_rebound_correlation: 0.38
388	    training_token_confound_ruled_out: true
389	    rebound_std_increase_from_minimum: 0.009
390	    gpu_hours_used: 2
391	  result_rationale: '340M 的 parameter budget 是 zero-sum：每增加一个 attention layer 就减少一个
392	    recurrent layer。
393	
394	    h12-1 以上（>50% attention），recurrent pathway capacity 不足以维持高难度 sample 的 representation
395	    quality。
396	
397	    Rebound samples 73% 集中在 top difficulty quartile（baseline ppl 最高）——这些 sample
398	
399	    需要 strong recurrent state AND effective attention，但 340M 的总 capacity 不够同时满足。
400	
401	    1.3B 无 rebound 因为 capacity 充足：同样的 sample，1.3B acc=0.68 vs 340M h3-1 acc=0.35。
402	
403	    Training token confound（340M: 20B tokens, 1.3B: 100B tokens）通过 ratio-specificity
404	    排除：
405	
406	    如果是 training tokens 主因，应看到 uniform degradation across all ratios，
407	
408	    而非 specific rebound at h12-1+。ratio-specific onset 指向 parameter allocation 而非
409	    training duration。
410	
411	    ppl gap（340M vs 1.3B baseline perplexity）与 rebound magnitude 中等正相关（r=0.38）：
412	
413	    capacity difference 最大的 sample（ppl gap 大）恰好最容易 rebound。
414	
415	    Best 档叙事：rebound 不是 inconvenient noise，而是 capacity bottleneck 的 PREDICTED failure
416	    mode——
417	
418	    convergence requires sufficient capacity，340M 的 failure mode 恰好验证了这个 prediction。
419	
420	    '
421	  tables:
422	  - 'Table 8: Rebound vs non-rebound sample characterization (n, ppl, accuracy at
423	    3 configs)'
424	  - 'Table 9: Scale comparison — convergence completeness (1.3B monotonic vs 340M
425	    rebound)'
426	  figures_description:
427	  - 'Fig 8: Dual-scale convergence trajectory — 1.3B monotonic vs 340M rebound, rebound
428	    region shaded'
429	  - 'Fig 9: Difficulty distribution of rebound vs non-rebound samples (clear quartile
430	    separation)'
431	  analysis: 'Capacity bottleneck 将 Claim 2 从 "binary contrast" 升级为 "mechanistic binary
432	    contrast"。
433	
434	    不需要 7B 来 establish trend——mechanism 解释了 WHY scale matters，且 predicts larger models
435	
436	    不会 rebound（capacity sufficient for both pathways）。
437	
438	    Concern E 回应：two scales + mechanism > three scales without mechanism。
439	
440	    '
441	- name: Statistical robustness framework
442	  plan_id: exp-008
443	  description: Bootstrap CI + exact permutation + 多重比较校正 + GDN-excluded sensitivity（核心已完成，best
444	    档含 exp-011 数据后的 updated correction）
445	  expected_results:
446	    LAMBADA_bootstrap_CI:
447	    - -1.0
448	    - -0.7
449	    LAMBADA_CI_method: percentile on 8875/10000 valid resamples (BCa degenerate at
450	      ρ=-1.0)
451	    LAMBADA_exact_p_two_tailed: 0.017
452	    StoryCloze_exact_p_two_tailed: 0.017
453	    BH_FDR_retrieval_m5:
454	      benchmarks:
455	      - LAMBADA
456	      - StoryCloze
457	      - ARC-Easy
458	      - BoolQ
459	      - COPA
460	      sorted_p:
461	      - 0.017
462	      - 0.017
463	      - 0.233
464	      - 0.233
465	      - 0.683
466	      step_up_largest_k: 2
467	      step_up_threshold_k2: 0.02
468	      LAMBADA_adj_p: 0.042
469	      StoryCloze_adj_p: 0.042
470	      n_significant: 2
471	    Bonferroni_confirmatory_m3:
472	      benchmarks:
473	      - StoryCloze
474	      - BoolQ
475	      - COPA
476	      StoryCloze_adj_p: 0.05
477	      n_significant: 1
478	      note: 'borderline: 0.0167 × 3 = 0.050 = α exactly'
479	    BH_FDR_full_m9:
480	      rank_1_threshold: 0.0056
481	      p_1: 0.017
482	      n_significant: 0
483	      note: honestly reported — full correction includes reasoning benchmarks with
484	        no convergence prediction
485	    GDN_excluded_ARC_Easy_rho: -0.9
486	    GDN_excluded_ARC_Easy_p_two_tailed: 0.083
487	    GDN_excluded_ARC_Easy_p_one_tailed: 0.042
488	    GDN_excluded_note: one-tailed defensible as sensitivity analysis (direction pre-specified)
489	  result_rationale: '统计策略三层（全部基于 two-tailed exact permutation，与已完成 exp-008 一致）：
490	
491	
492	    Layer 1 — Pre-specified retrieval subset（m=5）：
493	
494	    基于 exp-001 taxonomy（在 exp-011 之前确定），只对有 a priori convergence prediction 的
495	
496	    benchmark 做校正。BH step-up：p(1)=p(2)=0.017, rank-2 threshold = 2/5 × 0.05 = 0.020,
497	
498	    0.017 ≤ 0.020 → reject both。BH adj_p = min(0.017 × 5/2, ...) = 0.042。
499	
500	    两个 benchmark 显著（adj_p=0.042 < 0.05）。
501	
502	    这不是 p-hacking：taxonomy 在 exp-011 之前由 exp-001 独立建立，
503	
504	    对 reasoning benchmarks 做校正在 methodologically 上 overly conservative
505	
506	    （no theoretical prediction of convergence on reasoning tasks）。
507	
508	
509	    Layer 2 — Confirmatory subset（m=3, 仅 exp-011 新增）：
510	
511	    Discovery/confirmatory split 是标准方法论。LAMBADA 是 discovery，不参与 confirmatory correction。
512	
513	    StoryCloze p=0.017 ≤ 1/3 × 0.05 = 0.0167——精确相等（1/60 = 1/60），borderline pass。
514	
515	    Bonferroni: 0.017 × 3 = 0.050 = α → borderline pass。1 个 Bonferroni-significant。
516	
517	
518	    Layer 3 — Full correction（m=9）：
519	
520	    rank-1 threshold = 0.05/9 = 0.0056，p=0.017 > 0.0056 → 0 rejections。
521	
522	    诚实报告。但 include reasoning benchmarks in correction is arguable——
523	
524	    对其做校正等于 penalize for testing things we predicted wouldn''t work。
525	
526	
527	    GDN-excluded：ARC-Easy improves from ρ=-0.7 to ρ=-0.9（D004 confound removed），
528	
529	    one-tailed p=0.042 < 0.05（方向 pre-specified）。Converging evidence，不作为 primary claim。
530	
531	    '
532	  tables:
533	  - 'Table S1: Full 9-benchmark correction table (raw p, BH-FDR adj_p, Bonferroni
534	    adj_p)'
535	  - 'Table S2: Pre-specified retrieval subset (m=5) BH-FDR step-up computation'
536	  - 'Table S3: GDN-excluded sensitivity (6 benchmarks, ρ change, direction)'
537	  figures_description:
538	  - 'Fig S1: Bootstrap distribution of LAMBADA ρ (8875 valid resamples, CI [-1.0,
539	    -0.7])'
540	  analysis: 'Pre-specified retrieval subset 是 best 档统计 narrative 的核心 innovation。
541	
542	    Paper 透明呈现所有三层 correction：reader 可自行判断 appropriate scope。
543	
544	    BH-FDR m=5 保留 2 个 benchmark 是 primary reporting；
545	
546	    full m=9 failure 在 supplementary 诚实披露。
547	
548	    W1 从 "blocking" 降级为 "addressed with principled subset correction + second independent
549	    benchmark"。
550	
551	    '
552	- name: Wang et al. explicit differentiation
553	  plan_id: exp-009
554	  description: 与 Wang et al.（arXiv 2507.06457）的系统性差异化分析（已完成，actual）
555	  expected_results:
556	    n_differentiators: 5
557	    diff_1: 'Cross-arch std convergence trajectory + Spearman + exact permutation
558	      (Wang: qualitative only)'
559	    diff_2: 'Per-example decomposition with Jaccard quantification (Wang: absent entirely)'
560	    diff_3: 'Scale-dependent convergence + capacity bottleneck mechanism (Wang: binary
561	      statement)'
562	    diff_4: 'Task-specificity taxonomy with statistical validation (Wang: ratio-sensitivity
563	      without taxonomy)'
564	    diff_5: 'Multi-benchmark convergence with pre-specified retrieval subset (Wang:
565	      no cross-benchmark analysis)'
566	    wang_convergence_treatment: qualitative side observation in discussion, 1-2 sentences
567	  result_rationale: 'Wang et al. focus 是 model zoo design + training recipe，convergence
568	    是 side observation。
569	
570	    5 个 differentiator 每个都是 quantitative analysis WITH statistical test。
571	
572	    Best 档下 exp-011 新增第 5 个：multi-benchmark convergence analysis。
573	
574	    Framing：community analysis paper——public infrastructure enables independent analytical
575	    contribution，
576	
577	    类比 medical meta-analysis。
578	
579	    '
580	  tables:
581	  - 'Table 10: Side-by-side comparison (5 dimensions, Wang et al. vs ours)'
582	  figures_description: []
583	  analysis: 'W4 回应核心。不是 re-analysis，而是 independently motivated analytical contribution
584	
585	    grounded in ensemble diversity + underspecification literature。
586	
587	    '
588	- name: Convergence-divergence bridge analysis
589	  plan_id: exp-010
590	  description: Aggregate convergence 与 per-example divergence 作为 attention ratio 函数的
591	    co-evolution 量化
592	  expected_results:
593	    cross_arch_std_trajectory:
594	    - 0.024
595	    - 0.016
596	    - 0.014
597	    - 0.006
598	    - 0.005
599	    mean_effect_magnitude_trajectory:
600	    - 0.0
601	    - 0.028
602	    - 0.035
603	    - 0.045
604	    - 0.055
605	    helped_set_jaccard_trajectory:
606	    - null
607	    - 0.12
608	    - 0.09
609	    - 0.07
610	    - 0.06
611	    co_evolution_rho_std_vs_effect: -1.0
612	    co_evolution_p_two_tailed: 0.017
613	    monotonic: true
614	  result_rationale: 'Co-evolution 接近 deterministic：两个指标都是 attention ratio 的单调函数，
615	
616	    由同一 mechanism 驱动。
617	
618	    更多 attention → 更多 architecture-specific blind-spot compensation →
619	
620	    (a) aggregate std ↓（各架构被补偿到相似水平 → convergence）
621	
622	    (b) |effect| ↑（更多 sample 被 attention 改变 → per-example effects 更强）
623	
624	    (c) helped Jaccard ↓（更多 attention routing = 更多 architecture-specific selection
625	    → divergence）
626	
627	    std strictly decreasing + |effect| strictly increasing on same 5 points → ranks
628	    perfectly reversed → ρ=-1.0。
629	
630	    p=0.017 two-tailed（n=5, exact permutation）。
631	
632	    h0 处 |effect|=0 by definition（pure vs pure = no difference），但仍是 valid data point。
633	
634	    Jaccard 从 h24-1 处 0.12 降至 h3-1 处 0.06——attention 量越多，
635	
636	    per-example effects 越 architecture-specific。
637	
638	    '
639	  tables:
640	  - 'Table 11: Co-evolution table (attention ratio × std × |effect| × Jaccard)'
641	  figures_description:
642	  - 'Fig 2 (paper headline): Dual-axis — cross-arch std (blue ↓, left) vs mean |effect|
643	    (red ↑, right) vs attention ratio (x). Opposite trajectories = equalizer paradox
644	    in one figure.'
645	  analysis: 'Signature visualization。一张图传达整个 contribution：
646	
647	    aggregate convergence（Claim 1）+ per-example divergence（Claim 3）作为 attention 的函数。
648	
649	    ρ=-1.0 量化了 "paradox" 的精确程度。
650	
651	    Reviewer 看到这张图应立即 grasp 论文的核心 insight。
652	
653	    '
654	- name: Additional high-retrieval benchmarks
655	  plan_id: exp-011
656	  description: StoryCloze/BoolQ/COPA 评估——Dream W1 的核心回应，建立 second significant anchor
657	  expected_results:
658	    StoryCloze:
659	      rho: -1.0
660	      exact_p_two_tailed: 0.017
661	      std_trajectory:
662	      - 0.019
663	      - 0.013
664	      - 0.01
665	      - 0.006
666	      - 0.004
667	      std_reduction_pct: 79
668	      significant: true
669	    BoolQ:
670	      rho: -0.7
671	      exact_p_two_tailed: 0.233
672	      std_trajectory:
673	      - 0.022
674	      - 0.019
675	      - 0.017
676	      - 0.015
677	      - 0.012
678	      std_reduction_pct: 45
679	      significant: false
680	    COPA:
681	      rho: -0.3
682	      exact_p_two_tailed: 0.683
683	      std_trajectory:
684	      - 0.031
685	      - 0.028
686	      - 0.03
687	      - 0.026
688	      - 0.025
689	      std_reduction_pct: 19
690	      significant: false
691	    n_new_significant: 1
692	    second_anchor: StoryCloze
693	    retrieval_demand_gradient_confirmed: true
694	    combined_BH_FDR_retrieval_m5_significant: 2
695	    combined_Bonferroni_confirmatory_m3_significant: 1
696	    gpu_hours_used: 7
697	  result_rationale: 'StoryCloze 最可能成为 second anchor，因为 task structure 最接近 LAMBADA：
698	
699	    LAMBADA = passage → predict last word（open-vocabulary context completion）。
700	
701	    StoryCloze = 4-sentence story → predict correct ending（binary context completion）。
702	
703	    核心 retrieval demand 相同：从 narrative context 中 extract 信息来判断 completion。
704	
705	    Attention 的 copy/induction-head mechanism 在 StoryCloze 上应产生类似的 cross-arch convergence。
706	
707	    ρ=-1.0（而非 -0.9）因为 convergence pattern 在 5 attention ratios 上严格单调——
708	
709	    与 LAMBADA 相同的 structural property。Std reduction 79% 也与 LAMBADA 近似。
710	
711	
712	    BoolQ（ρ=-0.7, NS）：passage-based yes/no 需要 retrieval + boolean reasoning 混合。
713	
714	    Retrieval 部分 converge，reasoning 部分不 converge → aggregate 被 dilute。
715	
716	    Exactly what the taxonomy predicts for mixed retrieval/reasoning tasks。
717	
718	
719	    COPA（ρ=-0.3, NS）：causal reasoning from two sentences，retrieval demand 最低。
720	
721	    Attention 对 causal inference 的贡献 architecture-invariant 程度低。
722	
723	
724	    Three-benchmark gradient（StoryCloze > BoolQ > COPA）是 exp-001 taxonomy 的
725	
726	    out-of-sample prediction：retrieval demand 递减 → convergence 递减。
727	
728	    这不是 arbitrary outcome，而是 theoretical framework 的 validation。
729	
730	
731	    BH-FDR retrieval subset（m=5）：LAMBADA + StoryCloze 均 adj_p=0.042 → 2 significant。
732	
733	    Bonferroni confirmatory（m=3）：StoryCloze adj_p=0.050 → 1 significant（borderline）。
734	
735	    W1 从 "blocking" 降级为 "addressed"——论文不再依赖 single benchmark。
736	
737	    '
738	  tables:
739	  - 'Table 12: New benchmark convergence (ρ, p, std reduction) + original 6 for comparison'
740	  figures_description:
741	  - 'Fig 1b: Cross-arch std trajectories for StoryCloze/BoolQ/COPA alongside LAMBADA'
742	  - 'Fig 1c: 9-benchmark retrieval demand dose-response (ρ vs retrieval demand index)'
743	  analysis: 'StoryCloze 是 best 档的 linchpin——从 "one-benchmark curiosity" 升级为
744	
745	    "retrieval-task phenomenon confirmed on two independent benchmarks"。
746	
747	    BoolQ/COPA gradient strengthens taxonomy without needing to be significant themselves。
748	
749	    Combined 9-benchmark dose-response plot（convergence strength vs retrieval demand）
750	
751	    成为 Claim 1 的 definitive visualization。'
752	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52927afb-eab2-4640-9fa9-1bce48fd312d",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "629f5ed2-0a3d-4e7c-9043-41fb06a20f27",
  "sourceToolAssistantUUID": "52927afb-eab2-4640-9fa9-1bce48fd312d",
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

_source line 41 · 2026-05-19T15:32:49.221Z_

Now let me look at the experiment artifacts to understand the actual data available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "629f5ed2-0a3d-4e7c-9043-41fb06a20f27",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAp1gZnF5jMYqKBfsoJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a3c5e13-fcef-4b2b-b11a-7f01cd64f5a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBVvKJJAsf8CGFDQrac1mZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3897,
      "cache_creation_input_tokens": 12023,
      "cache_read_input_tokens": 47329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12023,
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

_source line 42 · 2026-05-19T15:32:51.256Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011umK3mxy46ng7yVhPum76a`</summary>

```json
{
  "pattern": "**/exp-001/**/*.csv",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a3c5e13-fcef-4b2b-b11a-7f01cd64f5a4",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAp1gZnF5jMYqKBfsoJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8bdb7c51-8895-4b4c-a04a-e22dc22e28e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBVvKJJAsf8CGFDQrac1mZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3897,
      "cache_creation_input_tokens": 12023,
      "cache_read_input_tokens": 47329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12023,
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

_source line 43 · 2026-05-19T15:32:51.278Z_

<details><summary>↩ Tool result · `toolu_011umK3mxy46ng7yVhPum76a`</summary>

```text
artifacts/exp-001/data/task_specificity_results.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bdb7c51-8895-4b4c-a04a-e22dc22e28e1",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "85e6f29f-eff0-4a0e-8c38-5d94d62a0859",
  "sourceToolAssistantUUID": "8bdb7c51-8895-4b4c-a04a-e22dc22e28e1",
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

_source line 44 · 2026-05-19T15:32:52.201Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01S33BJVrR8awzEvXdhtpnj4`</summary>

```json
{
  "pattern": "**/exp-008/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85e6f29f-eff0-4a0e-8c38-5d94d62a0859",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAp1gZnF5jMYqKBfsoJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "874ca5ea-023e-4529-a389-53574004512e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBVvKJJAsf8CGFDQrac1mZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3897,
      "cache_creation_input_tokens": 12023,
      "cache_read_input_tokens": 47329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12023,
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

_source line 45 · 2026-05-19T15:32:52.212Z_

<details><summary>↩ Tool result · `toolu_01S33BJVrR8awzEvXdhtpnj4`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "874ca5ea-023e-4529-a389-53574004512e",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "e3abbfec-3c84-45b4-996f-008a141ac351",
  "sourceToolAssistantUUID": "874ca5ea-023e-4529-a389-53574004512e",
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

_source line 46 · 2026-05-19T15:32:52.557Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JHWAgjF1CnkthS4P8bhb1t`</summary>

```json
{
  "pattern": "**/exp-010/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3abbfec-3c84-45b4-996f-008a141ac351",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAp1gZnF5jMYqKBfsoJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "958dbb8f-2565-4d4a-95b1-93741a67c88d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBVvKJJAsf8CGFDQrac1mZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3897,
      "cache_creation_input_tokens": 12023,
      "cache_read_input_tokens": 47329,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12023
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3897,
          "output_tokens": 295,
          "cache_read_input_tokens": 47329,
          "cache_creation_input_tokens": 12023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12023,
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

_source line 47 · 2026-05-19T15:32:52.567Z_

<details><summary>↩ Tool result · `toolu_01JHWAgjF1CnkthS4P8bhb1t`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "958dbb8f-2565-4d4a-95b1-93741a67c88d",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "8b3e99da-876a-44a7-a1a8-994c86b61085",
  "sourceToolAssistantUUID": "958dbb8f-2565-4d4a-95b1-93741a67c88d",
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

_source line 48 · 2026-05-19T15:32:57.007Z_

<details open><summary>🔧 Tool call — Read · `toolu_0187Pg88n14GLP1696Zg6QLY`</summary>

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
  "parentUuid": "8b3e99da-876a-44a7-a1a8-994c86b61085",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCApVyfZsSaj69edsXzg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "341ffe64-2177-4bde-9d2f-0c89367be288",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPnEwACGTV7kbrqmGwNQrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4401,
      "cache_read_input_tokens": 59352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4401,
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

_source line 49 · 2026-05-19T15:32:57.012Z_

<details><summary>↩ Tool result · `toolu_0187Pg88n14GLP1696Zg6QLY`</summary>

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
  "parentUuid": "341ffe64-2177-4bde-9d2f-0c89367be288",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "51bed1ac-4b36-4c7d-b0ee-484b0d1cbbcf",
  "sourceToolAssistantUUID": "341ffe64-2177-4bde-9d2f-0c89367be288",
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

_source line 50 · 2026-05-19T15:32:57.430Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017dEEAvWBYx2sGs78Vg77B9`</summary>

```json
{
  "pattern": "**/exp-003/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51bed1ac-4b36-4c7d-b0ee-484b0d1cbbcf",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCApVyfZsSaj69edsXzg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb2c6b12-337d-4f0c-b3f8-c793e6a4e145",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPnEwACGTV7kbrqmGwNQrf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4401,
      "cache_read_input_tokens": 59352,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4401
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 59352,
          "cache_creation_input_tokens": 4401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4401,
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

_source line 51 · 2026-05-19T15:32:57.450Z_

<details><summary>↩ Tool result · `toolu_017dEEAvWBYx2sGs78Vg77B9`</summary>

```text
artifacts/exp-003/data/sample_characterization_results.csv
artifacts/exp-003/chart/sample_characterization_figure_pointer.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb2c6b12-337d-4f0c-b3f8-c793e6a4e145",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "8c76602d-692b-4d62-a3f7-672058a2ae8d",
  "sourceToolAssistantUUID": "bb2c6b12-337d-4f0c-b3f8-c793e6a4e145",
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

_source line 52 · 2026-05-19T15:33:00.758Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TV4EbA4WsixBe7hmHJ7hJv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/exp-003/data/sample_characterization_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c76602d-692b-4d62-a3f7-672058a2ae8d",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAprmKXb8QJNeyU1pUK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f380d9ef-9c7c-4e94-ad36-9cf22df7d6eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012pEKCLTGu9uhDWbh543QBX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 947,
      "cache_read_input_tokens": 63753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 947,
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

_source line 53 · 2026-05-19T15:33:00.763Z_

<details><summary>↩ Tool result · `toolu_01TV4EbA4WsixBe7hmHJ7hJv`</summary>

```text
1	comparison,feature,helped_median,hurt_median,helped_mean,hurt_mean,helped_n,hurt_n,U_statistic,p_value,rank_biserial_r
2	GDN: helped vs hurt,context_length,81.0,81.0,83.80,83.26,462,615,141635.5,0.932,0.003
3	GDN: helped vs hurt,target_token_frequency,2.0,2.0,2.79,2.70,462,615,145298.0,0.503,-0.023
4	GDN: helped vs hurt,context_unique_tokens,61.0,61.0,62.18,61.68,462,615,144090.0,0.688,-0.014
5	HGRN2: helped vs hurt,context_length,82.0,81.0,83.99,83.27,548,395,113423.0,0.208,-0.048
6	HGRN2: helped vs hurt,target_token_frequency,2.0,2.0,2.92,2.82,548,395,111962.5,0.346,-0.034
7	HGRN2: helped vs hurt,context_unique_tokens,62.0,60.0,62.40,61.93,548,395,113510.0,0.200,-0.049
8	RetNet: helped vs hurt,context_length,82.0,81.0,85.02,82.62,426,495,115506.5,0.012,-0.096
9	RetNet: helped vs hurt,target_token_frequency,2.0,2.0,2.92,3.02,426,495,102511.5,0.453,0.028
10	RetNet: helped vs hurt,context_unique_tokens,61.5,61.0,62.86,61.07,426,495,115907.5,0.009,-0.099
11	helped: GDN vs HGRN2,context_length,81.0,82.0,83.80,83.99,462,548,122083.0,0.329,0.036
12	helped: GDN vs HGRN2,target_token_frequency,2.0,2.0,2.79,2.92,462,548,123104.0,0.432,0.028
13	helped: GDN vs HGRN2,context_unique_tokens,61.0,62.0,62.18,62.40,462,548,122218.5,0.344,0.035
14	helped: GDN vs RetNet,context_length,81.0,82.0,83.80,85.02,462,426,91805.5,0.084,0.067
15	helped: GDN vs RetNet,target_token_frequency,2.0,2.0,2.79,2.92,462,426,95517.0,0.432,0.029
16	helped: GDN vs RetNet,context_unique_tokens,61.0,61.5,62.18,62.86,462,426,93547.5,0.203,0.049
17	helped: HGRN2 vs RetNet,context_length,82.0,82.0,83.99,85.02,548,426,112892.0,0.379,0.033
18	helped: HGRN2 vs RetNet,target_token_frequency,2.0,2.0,2.92,2.92,548,426,116557.5,0.968,0.001
19	helped: HGRN2 vs RetNet,context_unique_tokens,62.0,61.5,62.40,62.86,548,426,114863.5,0.669,0.016
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f380d9ef-9c7c-4e94-ad36-9cf22df7d6eb",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "2d175b62-4499-4097-92e7-9ad6879ed329",
  "sourceToolAssistantUUID": "f380d9ef-9c7c-4e94-ad36-9cf22df7d6eb",
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

_source line 54 · 2026-05-19T15:33:01.210Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018589UcYGofWHzp6GxRcMzM`</summary>

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
  "parentUuid": "2d175b62-4499-4097-92e7-9ad6879ed329",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAprmKXb8QJNeyU1pUK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58d87a02-941b-4d7b-ad33-bee139562ff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012pEKCLTGu9uhDWbh543QBX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 947,
      "cache_read_input_tokens": 63753,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 947
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 63753,
          "cache_creation_input_tokens": 947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 947,
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

_source line 55 · 2026-05-19T15:33:01.219Z_

<details><summary>↩ Tool result · `toolu_018589UcYGofWHzp6GxRcMzM`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'entrainment_gated_ft'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58d87a02-941b-4d7b-ad33-bee139562ff4",
  "isSidechain": true,
  "promptId": "4badaa79-deae-4472-a900-f7e492282b8e",
  "agentId": "afdcfe4979fa0befe",
  "type": "user",
  "uuid": "f8ad34b9-6dae-4055-860a-e6884044a296",
  "sourceToolAssistantUUID": "58d87a02-941b-4d7b-ad33-bee139562ff4",
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

_source line 56 · 2026-05-19T15:34:54.143Z_

Now I have a comprehensive understanding of the paper, the actual experimental data, the review context, and the framing decisions. Let me produce the review.

---

# EMNLP 2026 (ARR) Review — Reviewer 1 (Methods and Experiments)

**Paper:** "Task-Dependent Convergence and Per-Example Divergence in Attention-Augmented Linear Recurrent Models"

---

## Paper Summary

This paper uses a public model zoo of 72 hybrid recurrent-attention models (GatedDeltaNet, RetNet, HGRN2; 5 attention ratios; 2 scales from Wang et al. 2025) to study how adding attention layers affects cross-architecture behavioral diversity at the per-example level. Three claims are advanced: (1) attention-induced convergence is task-dependent, strongest on retrieval tasks (LAMBADA rho=-1.0, p=0.017); (2) convergence is scale-dependent, monotonic at 1.3B but non-monotonic at 340M; (3) despite aggregate convergence, attention affects nearly non-overlapping sample subsets across architectures (Jaccard < 0.10). The paper frames itself as a "community analysis" quantifying a known phenomenon (underspecification) in the specific context of hybrid architectures.

---

## Soundness: 2.5 / 5

The paper is commendably transparent about its statistical limitations, but several fundamental methodological issues undermine the claims.

**1. Extreme low statistical power (n=5 Spearman tests).** The entire convergence framework rests on Spearman correlation over 5 attention ratios. The minimum achievable two-tailed p-value is 2/120 = 0.0167, which is the exact value obtained for every "significant" result. This means: (a) any perfectly monotonic 5-point sequence achieves p=0.017 regardless of effect size or practical significance; (b) the test cannot distinguish a true dose-response from any monotonic confound correlated with attention ratio (e.g., changes in effective parameter allocation, implicit regularization effects); (c) there is zero resolution between "barely significant" and "strongly significant." The paper treats p=0.017 as meaningful evidence, but this is the floor of the test, not a compelling result.

**2. Missing Jaccard null baseline -- this is critical.** The headline per-example claim (Claim 3) states Jaccard < 0.10 indicates "nearly non-overlapping" sample subsets. This is uninterpretable without a random-null comparison. The helped sets contain roughly 400-550 samples out of ~5,153 total LAMBADA examples (from the actual data: GDN 462, RetNet 426, HGRN2 548 helped). For sets of size ~500 drawn from 5,153, the expected Jaccard under random independent draws is approximately:

E[J] = (n_A * n_B / N) / (n_A + n_B - n_A * n_B / N)

For n_A=462, n_B=548, N=5153: E[J] approximately 0.054. For n_A=462, n_B=426: approximately 0.045. The observed values of 0.07-0.10 may actually be *above* the random null, meaning attention acts on *more overlapping* sets than chance would predict. If so, the entire Claim 3 narrative reverses: per-example effects would be *less* architecture-specific than random, not more. Without this computation, the paper's central finding is potentially backwards.

**3. BH-FDR correction scope is debatable.** The paper defines a "pre-specified retrieval subset" (m=5) to limit the correction scope and reports BH-FDR adj-p=0.042. However, the taxonomy was built from the initial 6-benchmark analysis (exp-001 data), which includes some of the same benchmarks. True pre-specification requires the taxonomy to be established *before any data is observed*, or on entirely separate data. Using 6-benchmark data to build the taxonomy, then testing on a superset that includes 3 of those same 6, is not clean discovery/confirmation separation. The confirmatory subset (m=3, Bonferroni) is cleaner, and StoryCloze's adj-p=0.050 at the exact alpha boundary is borderline. Under the full honest correction (m=9), nothing survives.

**4. Co-evolution analysis (Section 5.4 / Table 7) is inflated by a definitional point.** The h0 row has |Delta|=0.0 *by definition* (pure recurrence vs. pure recurrence produces zero effect). Including this tautological anchor point in a 5-point Spearman correlation inflates the result toward rho=-1.0. The project's own internal review (D008) acknowledged this exact issue when analyzing Jaccard co-evolution and shifted to "decoupling" framing. Yet the paper still reports rho=-1.0 (p=0.017) for sigma-vs-|Delta| co-evolution without disclosing the h0 issue. Excluding h0 would leave 4 data points, likely yielding a non-significant result (minimum 4-point two-tailed p = 2/24 = 0.083).

**5. Scale comparison confounded by training tokens.** 340M models trained on 20B tokens vs. 1.3B on 100B tokens. The paper's counter-argument (that training-token effects would be "uniform across ratios") is hand-waving, not a formal test. The interaction between training duration and attention ratio is plausible: high-attention configurations may benefit disproportionately from more training data because attention heads require more examples to learn useful patterns. Without intermediate checkpoint analysis or models matched on training tokens, the capacity-bottleneck interpretation of the 340M rebound is one of multiple possible explanations.

**6. GDN confound (D004) undermines n=3 generality.** GDN's hybrid-3-1 configuration has a known attn.num_heads confound (16 vs 32 heads). When GDN is excluded, LAMBADA rho drops to -0.7 (p=0.233, non-significant), and MMLU rho *flips* from -0.7 to +0.6. This means: (a) the LAMBADA convergence result is sensitive to including a confounded architecture; (b) with only n=2 clean architectures (RetNet, HGRN2), no meaningful Spearman test can be computed. The paper appropriately excludes MMLU but does not sufficiently grapple with the LAMBADA sensitivity.

**7. Bootstrap CI methodology.** The bootstrap CI [-1.0, -0.7] is reported on 8,875/10,000 "valid" resamples, with 11.25% degenerate resamples excluded. These degenerate resamples arise from resampling the same architecture 3 times (drawing 3 from 3 with replacement), producing undefined rho. Excluding 11.25% of bootstrap samples and reporting "100% of valid resamples have rho<0" is methodologically questionable -- the degenerate samples represent a real failure mode of the estimator when n=3. A conservative approach would treat degenerate resamples as rho=0 (no evidence for correlation), yielding a CI of [-1.0, 0.0] that touches zero.

**8. Attention weight analysis is very weak.** r=0.22 cross-architecture correlation (in the summary) or r=0.36 mean attention-entropy-effect correlation (in the paper) explains 5-13% of variance. The paper correctly labels this as descriptive, but it is presented as partial explanation when it barely meets the threshold for a meaningful effect. The focus-distance analysis (GDN 3-8, RetNet 8-20, HGRN2 5-15) is narrative, not statistical.

---

## Reproducibility: 4.5 / 5

Reproducibility is a clear strength. All 72 models are publicly available on HuggingFace (Wang et al. model zoo). Evaluation uses the standard lm-evaluation-harness with --log_samples. Statistical tests are fully specified (exact permutation with 120 permutations, two-tailed). Attention ratios and model identifiers are explicit.

The 0.5 deduction is for: (a) ambiguity about the Mamba2-hybrid provenance in the "best case" paper -- it is unclear whether these models are from Wang et al.'s extended set, independently trained, or hypothetical; (b) no code release at review time (though presumably planned); (c) the bootstrap procedure's treatment of degenerate samples should be documented in code.

---

## Excitement: 2 / 5

The core finding -- that models with similar aggregate performance differ at the per-example level -- is the expected prediction from the underspecification literature the paper itself cites (D'Amour et al. 2022). The paper is transparent about this, framing its contribution as "quantification in a specific domain." However, the specifics of that quantification are not surprising: retrieval tasks benefiting from attention is a known property of attention mechanisms; different architectures affecting different samples is the definition of underspecification; the effect being stronger at larger scale is a generic scaling finding.

The most potentially interesting finding -- the co-evolution of aggregate convergence and per-example divergence as a function of attention ratio -- is undermined by the h0 definitional issue and the very limited statistical power.

The task-dependency taxonomy is a reasonable organizational contribution but applies only within this specific model zoo (3-4 architectures, 2 scales, shared training recipe). Generalizability to production hybrid models (Jamba, RecurrentGemma, RWKV-6) trained under different conditions is unknown.

The practical implication (ensembles of different hybrid architectures may have diversity benefits) is speculative and untested.

---

## Overall Assessment: 2.5 / 5 (Borderline Findings)

**Calibration rationale:** The paper demonstrates genuine analytical effort and exemplary statistical transparency. However, the evidence does not robustly support the claims at the level required for EMNLP:

- Claim 1 (task-dependent convergence): Rests on the minimum possible p-value of a 5-point Spearman test; nothing survives full multiple comparison correction; the pre-specified subset correction is debatable.
- Claim 2 (scale-dependent convergence): Two scale points confounded by training tokens.
- Claim 3 (per-example divergence): Missing random-null baseline makes the Jaccard results potentially uninterpretable or even reversed in meaning.

The paper is honest about its limitations, which I credit. But honesty about limitations does not substitute for addressing them. Several of the critical issues (Jaccard null, co-evolution h0 correction) could be computed from existing data without new experiments.

---

## Strengths

- **Exemplary statistical transparency.** Three-layer multiple comparison correction with all three reported honestly, including the full-correction failure. This level of intellectual honesty is rare and commendable.

- **Pre-specified confirmatory design.** The taxonomy was established before evaluating StoryCloze/BoolQ/COPA, making the confirmatory structure more credible than post-hoc analysis, even if the pre-specification is not perfectly clean.

- **Informative negative results.** The within-architecture sample characterization (surface features all non-significant, baseline perplexity non-significant) rules out trivial explanations. The two-layer negative + cross-architecture positive structure is a well-constructed argument.

- **Public infrastructure enables reproduction.** All models, benchmarks, and evaluation tooling are publicly available. This is a model for reproducible empirical research.

- **Clear Wang et al. differentiation.** The five-dimension comparison table (Appendix A) concretely establishes what is new vs. what is inherited.

- **Appropriate epistemic caution.** The paper avoids mechanistic overclaiming and correctly labels attention analysis as descriptive. The "community analysis paper" framing is appropriate and honest.

---

## Weaknesses

- **[Critical] Missing Jaccard random-null baseline.** Without expected Jaccard under random set assignment, Claim 3's "nearly non-overlapping" characterization is uninterpretable. Back-of-envelope calculations suggest observed Jaccard may be at or above the random null, potentially reversing the finding.

- **[Critical] Statistical power ceiling at n=5 attention ratios.** Every significant result achieves exactly the minimum possible p-value (0.017). The test cannot distinguish genuine convergence from any monotonic confound. No result can be "more significant than p=0.017" in this framework.

- **[Major] Co-evolution correlation inflated by definitional anchor.** h0 has |Delta|=0 by construction. The reported rho=-1.0 includes this tautological point. Excluding it likely yields a non-significant 4-point correlation.

- **[Major] Scale comparison confounded by 5x training token difference.** The capacity-bottleneck explanation for the 340M rebound is one hypothesis among several, not a demonstrated mechanism. No formal test rules out training-duration interaction with attention ratio.

- **[Major] BH-FDR pre-specification is imperfect.** The taxonomy was built on initial benchmark data overlapping with the correction set. Under full correction (m=9), no benchmark survives. The strongest correction that yields any significant result (BH-FDR m=5, adj-p=0.042) depends on the correction scope definition.

- **[Major] GDN confound sensitivity.** Excluding the confounded architecture reduces LAMBADA from rho=-1.0 (p=0.017) to rho=-0.7 (p=0.233). The main result is fragile to removal of 33% of the data.

- **[Moderate] Bootstrap CI excludes 11.25% degenerate samples.** Reporting "100% of valid resamples have rho<0" is misleading when the degenerate resamples (same-architecture triplicates) represent a genuine limitation of n=3. Conservative treatment yields CI touching zero.

- **[Moderate] No figures.** A tables-only paper at a top venue is unusual and fails to communicate the core patterns visually. The convergence trajectories, Jaccard values, and co-evolution would benefit enormously from visualization.

- **[Moderate] StoryCloze per-example decomposition appears absent.** The second statistical anchor lacks the Jaccard analysis that is central to Claim 3.

---

## Questions for Authors

1. What is the expected Jaccard similarity under random set assignment given the actual helped/hurt set sizes? How many standard deviations above or below this null are the observed values? If observed Jaccard exceeds the random null, how does this change Claim 3?

2. What is the sigma-vs-|Delta| Spearman correlation excluding the definitional h0 point? If non-significant at 4 points, does the co-evolution section need to be rewritten or removed?

3. Were per-example decompositions (Jaccard, effect magnitude) computed for StoryCloze? If so, please report them. If not, this is a significant omission for the second statistical anchor.

4. The Mamba2-hybrid models in the "best case" paper: what is their exact provenance? Were they trained by the authors, sourced from Wang et al., or hypothetical/imagined for the best-case scenario?

5. Can you rule out that attention ratio interacts with training duration? For example, do intermediate training checkpoints exist for the 340M models that would allow examining convergence trajectories at matched token counts?

6. The GDN-excluded sensitivity analysis drops LAMBADA to rho=-0.7 (non-significant). Given the known D004 confound, should the paper lead with RetNet+HGRN2-only results and present GDN as supplementary, rather than the reverse?

7. For the bootstrap CI, what is the result if degenerate resamples are assigned rho=0 rather than excluded? Does the CI still exclude zero?

---

## Minor Issues

- Table 1 reports "--" for sigma values on several benchmarks. These should be filled in even for non-converging tasks; the reader needs to see actual variance levels.
- The abstract claims "four recurrence mechanisms (GatedDeltaNet, RetNet, HGRN2, Mamba2-hybrid)" but the core analysis is on three from Wang et al. The fourth's provenance is unclear.
- The BH-FDR step-up computation in Section 4.4 should show the explicit step-up procedure (sorted p-values, rank thresholds) for full transparency, not just the result.
- No Responsible NLP Research Checklist is visible. EMNLP 2026 requires Sections A-E; absence risks desk rejection.
- The paper does not discuss that all models share the same training data (FineWeb-Edu) and training recipe, limiting generalizability to production hybrids.
- The MMLU exclusion (GDN-driven sign flip) is discussed only in the appendix sensitivity analysis. This should be noted in the main text where MMLU appears in Table 1.
- Page 6, Section 5.4: "co-evolution" terminology was internally flagged as inappropriate (D008 recommends "decoupling"). The paper uses "co-evolution" in the section heading and text.

---

**Recommendation:** 2.5 -- Borderline Findings. The paper has genuine merit in its transparency and systematic approach, but critical methodological gaps (especially the missing Jaccard null and the n=5 power ceiling) prevent the evidence from robustly supporting the claims. Addressing the Jaccard null computation could either strengthen or invalidate Claim 3 -- it is surprising this was not computed. The co-evolution correction and additional figures could move this to a solid 3.0 (Findings) with revisions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8ad34b9-6dae-4055-860a-e6884044a296",
  "isSidechain": true,
  "agentId": "afdcfe4979fa0befe",
  "requestId": "req_011CbCAq8ztAbyt4WBx5r1Cg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a204ec6-c19f-49c7-b95b-fb6059d54b31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d5f8c2b8-a1ca-4a4a-8211-80150d29dabf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvGFdgPZ4JrNqDKNiUpS9K",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1259,
      "cache_read_input_tokens": 64700,
      "output_tokens": 4245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1259
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4245,
          "cache_read_input_tokens": 64700,
          "cache_creation_input_tokens": 1259,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1259,
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
